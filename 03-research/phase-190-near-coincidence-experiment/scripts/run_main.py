import numpy as np, json, sys, time
from profile import Profile
from am import *

T0 = float(sys.argv[1]); b = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
Ms = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [50, 100, 200, 400, 800, 1200, 1600, 2000, 3000]
tag = f"T0{T0}_b{b}"
P = Profile(T0, b)
GAMMA1 = 14.134725141734693

def quartet_kernel(delta, gamma):
    zs = [delta+1j*gamma, delta-1j*gamma, -delta+1j*gamma, -delta-1j*gamma]
    coef = [(z, P.Fhat(-1j*z)**2) for z in zs]
    def Q(d):
        out = np.zeros(np.shape(d), complex)
        for z, c in coef: out += c*np.exp(z*d)
        return out.real
    return Q

# sanity for quartet kernel at d=0: compare with grid integral of c0(v)*4cosh(delta v)cos(gamma v)
Q = quartet_kernel(0.1, GAMMA1)
v = P.dgrid[P.dgrid < 2*T0]; c = P.c0_grid[:len(v)]
num = 2*np.trapz(c*4*np.cosh(0.1*v)*np.cos(GAMMA1*v), v)
print('quartet kernel check d=0:', Q(0.0), num, flush=True)

def vec_stats(v, x):
    """support/smoothness/multiplicative structure of a unit vector on the lattice"""
    p = v**2
    pr = 1.0/np.sum(p**2)                       # participation ratio
    cm = np.sum(p*np.arange(1, len(v)+1))       # centre of mass in m
    sm = np.linalg.norm(np.diff(v))/np.linalg.norm(v)   # roughness in m
    # Dirichlet polynomial |P_v(tau)| peak over tau in [0, 200]
    tau = np.linspace(0, 200, 4001)
    Pv = np.abs(np.exp(1j*np.outer(tau, x)) @ v)
    return dict(part_ratio=pr, centre_m=cm, roughness=sm, dirpoly_peak=float(Pv.max()), dirpoly_argmax=float(tau[Pv.argmax()]),
                dirpoly_at0=float(Pv[0]), mass_m_le_10=float(p[:10].sum()), mass_top_half=float(p[len(v)//2:].sum()))

def near_stats(A):
    N = A.Near; M = A.M
    lamN, VN = np.linalg.eigh(N)
    sv = np.sort(np.abs(lamN))[::-1]
    lamD, VD = np.linalg.eigh(A.Div)
    lamAr, VAr = np.linalg.eigh(A.Arch)
    neg = VAr[:, lamAr < 0]
    # alignment of Near's top-|eigenvalue| eigenvectors with Arch's negative eigenspace
    idx = np.argsort(-np.abs(lamN))[:5]
    align_neg = [float(np.linalg.norm(neg.T @ VN[:, i])**2) for i in idx]
    # alignment with Div eigenvectors (top 5 by |eigenvalue|)
    idxD = np.argsort(-np.abs(lamD))[:20]
    align_div = [float(np.linalg.norm(VD[:, idxD].T @ VN[:, i])**2) for i in idx]
    # mass by atom and by additive shift h=m-kn (integer lattice only)
    mass_n, mass_h = {}, {}
    for ai, k, m, d in A.triples:
        val = np.abs(0.5*A.w[ai]*A.P.c0(d)).sum()
        n = A.pos[ai]
        mass_n[float(n)] = mass_n.get(float(n), 0.0) + float(val)
    tri = np.triu(N, 1)
    nz = tri[np.abs(tri) > 0]
    return dict(near_eigs_top=[float(lamN[i]) for i in idx], near_eig_min=float(lamN[0]), near_eig_max=float(lamN[-1]),
                near_sv_decay=[float(sv[j]) for j in (0, 1, 2, 5, 10, 20, 50, 100, 200) if j < M],
                near_rank_1em3=int((sv > 1e-3*sv[0]).sum()), near_rank_1em6=int((sv > 1e-6*sv[0]).sum()),
                near_fro=float(np.linalg.norm(N)), div_fro=float(np.linalg.norm(A.Div)), arch_fro=float(np.linalg.norm(A.Arch)),
                near_op=float(sv[0]), div_op=float(np.abs(lamD).max()), arch_op=float(np.abs(lamAr).max()),
                div_eig_min=float(lamD[0]), div_eig_max=float(lamD[-1]), arch_eig_min=float(lamAr[0]), arch_nneg=int((lamAr < 0).sum()),
                near_frac_pos=float((nz > 0).mean()), near_nnz=int(len(nz)), near_sum=float(nz.sum()), near_abs_sum=float(np.abs(nz).sum()),
                align_near_archneg=align_neg, align_near_div20=align_div,
                mass_by_atom=dict(sorted(mass_n.items())[:40]))

results = {}
for M in Ms:
    t0 = time.time()
    x = np.log(np.arange(1, M+1))
    nmax = int(M*np.exp(2*T0)) + 2
    pos, w, ns = lambda_comb(nmax)
    A = AM(P, x, pos, w)
    s = A.summary(); v = s.pop('vec'); lam = s.pop('lam')
    s['lam_low5'] = [float(l) for l in lam[:5]]
    s['vec_stats'] = vec_stats(v, x)
    # decomposition on 3 generic vectors: smooth S(log m)=m^{-1/2}, flat, and random
    for name, u in (('m^-1/2', (np.arange(1, M+1))**-0.5), ('flat', np.ones(M)), ('alt', (-1.0)**np.arange(M))):
        u = u/np.linalg.norm(u)
        s['dec_'+name] = dict(A=float(u@A.A@u), Arch=float(u@A.Arch@u), Div=float(u@A.Div@u), Near=float(u@A.Near@u))
    s['near'] = near_stats(A)
    # Rayleigh bottom relative to the Gram (function norm), regularised
    try:
        from scipy.linalg import eigh as geigh
        G = A.Gram; lg = np.linalg.eigvalsh(G)
        s['gram_cond'] = float(lg[-1]/max(lg[0], 1e-300)); s['gram_min'] = float(lg[0])
        if lg[0] > 1e-10*lg[-1]:
            lr = geigh(A.A, G, eigvals_only=True, subset_by_index=[0, 0])
            s['lam_min_rel_gram'] = float(lr[0])
    except Exception as e:
        s['gram_err'] = str(e)
    np.savez_compressed(f"../data/vec_{tag}_M{M}.npz", v=v, lam_low=lam[:50], near_eigs=np.linalg.eigvalsh(A.Near))
    s['secs'] = time.time()-t0
    results[M] = s
    print(M, {k: s[k] for k in ('lam_min', 'floor', 'n_neg', 'Arch_v', 'Div_v', 'Near_v', 'Gram_v', 'secs')}, flush=True)
    json.dump(results, open(f"../data/main_{tag}.json", 'w'), indent=1, default=float)
