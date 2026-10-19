"""check.py NAME -- TASK "prove": re-evaluate the SAME f from the prime/Gamma side.
(1) prime side on the certified fine grid and on the whole [0,tau_max];
(2) residual ladder: zero side with 10/100/1000 zeros vs the exact prime side;
(3) far scan of the prime side to tau = 2000;
(4) the norm budget E1+E2+E3 that governs the honest envelope threshold.
"""
import numpy as np, json, sys, time
import dlib as D, primeside as P
import revlib as R1

NAME = sys.argv[1]; FAR = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
d = json.load(open(f"d_{NAME}.json")); T = d["T"]
win = D.Win(T, M=d["M"]); y = np.array(d["y"]); x = np.array(d["x"])
bet = np.array(d.get("beta", [0.0, 0.0]))
t00 = time.time()

def ghat(tt):
    tt = np.asarray(tt, float)
    xs, ws = np.polynomial.legendre.leggauss(600)
    u = T*(xs+1.0); wq = T*ws
    C = np.cos(np.outer(u, tt))
    return np.vstack([2*(wq*np.cosh(u/2)) @ C, 2*(wq*u*np.sinh(u/2)) @ C])

ns, lam = P.prime_table(win.Umax)
tauc = np.arange(0.0, d["taumax"]+1e-12, d["dc"])
fp_c = P.f_prime_fast(win, y, x, tauc, ns, lam) + bet @ ghat(tauc)
# refine around the prime-side minima
cand = tauc[np.argsort(fp_c)[:60]]
fine = np.unique(np.clip((cand[:, None] + np.linspace(-d['dc']/2, d['dc']/2, 51)[None, :]).ravel(),
                         0.0, d["taumax"]))
fp_f = P.f_prime_fast(win, y, x, fine, ns, lam) + bet @ ghat(fine)

gam_all = R1.load_zeros()
lad = {}
for NZ in (10, 100, 1000):
    Z = D.Zfun(win.u, gam_all[:NZ])
    fz = D.fvals(win, Z, y, x, tauc) + bet @ ghat(tauc)
    lad[str(NZ)] = {"Gamma": float(gam_all[NZ-1]),
                    "max_abs_diff": float(np.abs(fz-fp_c).max()),
                    "min_f_zero": float(fz.min())}

tfar = np.arange(win.taumax, FAR, 0.005)
ff = P.f_prime(win, y, x, tfar, ns, lam) + bet @ ghat(tfar)

# norm budget (honest envelope threshold) [amended per R155_012]
# ||nu_w||_TV for nu_w = [1/2(1-w)K + 2w cosh(u/2)]1_{|u|>=2T}du - sum_{n not in N_T}(v_n/2)w(log n)delta_{+-log n}
# The measure is EVEN: each a.c. piece counts twice (u and -u), and the atoms at +-log n
# have total mass v_n|w(log n)| (not 2v_n: the atom mass is v_n/2 on each side).
# The two a.c. pieces are combined BEFORE taking |.| (that is the TV norm, and it is smaller
# than E1+E3).  Atoms are restricted to log n > 2T (n in N_T belongs to sigma_T, not to nu_w).
u = win.u; wq = win.wq; wu = win.w_of_u(u, y, x)
K = 0.5/np.sinh(np.maximum(u, 1e-9)/2) + 0.5/np.cosh(u/2)
m = u >= 2*T
E1 = float(np.sum(wq[m]*np.abs(1-wu[m])*K[m]))            # = 2 * int 1/2|1-w|K
E3 = float(4*np.sum(wq[m]*np.abs(wu[m])*np.cosh(u[m]/2)))  # = 2 * int 2|w|cosh
logn = np.log(ns); selA = (logn > 2*T) & (logn <= win.Umax)
E2 = float(np.sum(2*lam[selA]/np.sqrt(ns[selA])*np.abs(win.w_of_u(logn[selA], y, x))))
E_ac = float(2*np.sum(wq[m]*np.abs(0.5*(1-wu[m])*K[m] + 2*wu[m]*np.cosh(u[m]/2))))
TV = E_ac + E2
out = {"name": NAME, "T": T, "beta": bet.tolist(),
       "c_lp": d["c_lp"], "certified_zero_side": d["certified"],
       "min_f_prime_coarse": float(fp_c.min()), "argmin_coarse": float(tauc[np.argmin(fp_c)]),
       "min_f_prime_fine": float(fp_f.min()), "argmin_fine": float(fine[np.argmin(fp_f)]),
       # [amended per R155_012] the refinement covers only the 60 smallest coarse
       # nodes, so the (dc/50) pad is NOT an enclosure; the enclosure over the whole interval
       # uses the coarse spacing dc.  A genuine dense enclosure is computed by dense.py.
       "B2": d["B2"], "pad_localised_NOT_an_enclosure": d["B2"]*(d["dc"]/50.0)**2/8,
       "pad_coarse_dense": d["B2"]*d["dc"]**2/8,
       "certified_prime_side": float(fp_f.min() - d["B2"]*d["dc"]**2/8),
       "min_f_prime_fine_localised": float(fp_f.min()),
       "ladder": lad, "far_scan_to": FAR, "min_f_prime_far": float(ff.min()),
       "argmin_far": float(tfar[np.argmin(ff)]),
       "E1_Ktail": E1, "E2_primes": E2, "E3_cosh": E3, "E_triangle": E1+E2+E3,
       "E_ac_exact": E_ac, "TV_exact": TV, "A_T": win.A_T,
       "log10_tau_env_honest": float((win.A_T+TV)/np.log(10) + np.log10(2*np.pi)),
       "t": time.time()-t00}
print(json.dumps(out, indent=1))
json.dump(out, open(f"chk_{NAME}.json", "w"))
