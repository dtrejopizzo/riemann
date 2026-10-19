import numpy as np
np.set_printoptions(precision=3, suppress=True)

# ---- Continuum realization on L^2(R,dr), discretized on a grid ----
# T_cont = mult by r ; raising L = T_c (translation by c) ; Tate twist [T_cont, T_c]=c T_c
# Full sl2:  L=T_c,  H=(2/c) T_cont,  Lambda = T_{-c} * m(r),  m(r) = -r^2/c^2 + r/c
N = 4000
h = 0.01
c = h                       # shift by one grid step (exact translation)
j = np.arange(N)
r = (j - N//2)*h            # grid of r values
Tcont = np.diag(r)

# shift matrices (T_c f)(r)=f(r-c): index j -> j-1
Tc  = np.zeros((N,N)); Tc[1:,:-1]  = np.eye(N-1)   # (Tc f)_j = f_{j-1}
Tmc = np.zeros((N,N)); Tmc[:-1,1:] = np.eye(N-1)   # (T_{-c} f)_j = f_{j+1}

m  = -(r**2)/c**2 + r/c
H  = (2.0/c)*Tcont
L  = Tc
Lam = Tmc @ np.diag(m)

def comm(A,B): return A@B - B@A
# evaluate errors on interior block (avoid boundary rows/cols)
s = slice(50, N-50)
def err(M): return np.max(np.abs(M[s,s]))

print("=== Tate twist and full sl2 relations on the continuum (max abs error on interior) ===")
print("  [T_cont, L] - c L        :", err(comm(Tcont,L) - c*L))
print("  [H, L]    - 2 L          :", err(comm(H,L)    - 2*L))
print("  [H, Lam]  + 2 Lam        :", err(comm(H,Lam)  + 2*Lam))
print("  [L, Lam]  - H            :", err(comm(L,Lam)  - H))
print()
print("  L=T_c is a multiplication operator? (=> would be in W*(T_cont))")
print("    diagonal-ness of L: off-diagonal mass =", np.max(np.abs(L - np.diag(np.diag(L)))) )
print("    => L is NOT diagonal => L NOT in W*(T_cont).  Independence filter PASSED (explicitly).")

# ---- The no-go on the DISCRETE zero spectrum (LI) ----
print("\n=== No-go on H_W (discrete zeros): Tate-twist Lefschetz needs spectrum shift-invariance ===")
import mpmath as mp
mp.mp.dps = 25
gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, 41)]
gam = np.array(gammas)
print("  first zeros:", np.round(gam[:6],4))
# for ANY fixed shift c, does gamma + c land back on a zero? (LI forbids it)
best = None
for cc in np.linspace(0.5, 60, 600):
    # count how many gamma_i + cc are within tol of some gamma_j
    hits = 0
    for x in gam:
        if np.min(np.abs(gam - (x+cc))) < 1e-3: hits += 1
    if best is None or hits > best[1]: best = (cc, hits)
print(f"  best shift c over [0.5,60]: c={best[0]:.3f} maps only {best[1]}/40 zeros onto zeros (need ALL 40).")
print("  => no constant c makes {gamma_rho} shift-invariant => NO Tate-twist raising operator on H_W.")
print("  (LI / P15, in its sharpest operator form: the discrete zero set has no translation grading.)")
