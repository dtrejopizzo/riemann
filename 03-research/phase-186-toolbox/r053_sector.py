#!/usr/bin/env python3
"""R186_053 — Two-sector symbol.  python3 r053_sector.py [ABC]   (~3 min; imports r052_nyquist from the same directory)

A  Structure of H: multiplier e^{iθ/2}, H² = shift, and the sector KERNEL LEMMA:
   for a single-atom symbol s(τ) = cos(τu₀):  s(D_per)  = c(u₀) + c(2T−u₀),   s(D_anti) = c(u₀) − c(2T−u₀)
   (c(u) = symmetrized autocorrelation form), checked entrywise against Σ_l s(ω_{2l+1}) h_{l−j}h_{l−j'}.
B  The single pointwise object: diag(s_{2j}, s_{2l+1}) in the index k (circulant cone): minima by parity in ζ and in M₁.
C  Two-sector Schur reduction (Theorem 2 of the memo): N_η = even and odd modes with sample < η (projected onto 𝒫_T),
   AUTOMATIC coercivity of the complement c_η = ½(s₊^e + s₊^o), exact Schur S_η and sufficient bound S_η^low = 𝔞_NN − X*X/c_η.
"""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from r052_nyquist import (contacts, s_grid, omega, quartet_grid, fourier_matrix, primitive_min, GAM1, C0, Ktail, K, _lg)

def hvec(m): return 2 * (-1.0) ** m / (np.pi * (2 * m + 1))      # h_m = sinc(m+½)

# ----------------------------------------------------------------- part A
def cs_even_matrix(T, J, u):
    """½[c_{jj'}(u) + c_{j'j}(u)*], c_{jj'}(u) = ⟨e_j, (translation by u, truncated to I_T) e_j'⟩ (copy of r052 fourier_matrix)."""
    js = np.arange(-J, J + 1); Om = js * np.pi / T; D = Om[:, None] - Om[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        I = np.where(abs(D) < 1e-12, 2 * T - u, (np.exp(1j * D * T) - np.exp(1j * D * (-T + u))) / (1j * D))
    cu = np.exp(1j * Om[None, :] * u) * I / (2 * T); return 0.5 * (cu + cu.conj().T)

def part_A():
    print("=== A. H: multiplier, H² = shift, sector kernel lemma")
    L = 200000; m = np.arange(-L, L + 1); h = hvec(m)
    # H² = S: (H²)_{n} = Σ_m h_m h_{n-m};  expected δ_{n,-1} or δ_{n,0}... we compute n = -2..1
    for n in (-2, -1, 0, 1):
        val = np.sum(h * hvec(n - m)); print(f"   (H²)_{{n={n}}} = Σ_m h_m h_{{n−m}} = {val:+.6f}  (expected: 1 at n=−1, 0 elsewhere: H² = shift)")
    th = np.array([0.3, 1.0, 2.5, 3.0]); mult = (h[:, None] * np.exp(-1j * np.outer(m, th))).sum(axis=0)
    print("   Σ_m h_m e^{-imθ} vs e^{iθ/2} at θ=0.3,1,2.5,3: max|err| =", f"{abs(mult - np.exp(1j*th/2)).max():.1e}", "(jump at θ=±π)")
    T = np.log(2); J = 6; js = np.arange(-J, J + 1); Lo = 100000; l = np.arange(-Lo, Lo + 1)
    for u0 in (0.4, np.log(2), 1.1):
        so = np.cos(omega(T, 2 * l + 1) * u0); mm = l[:, None] - js[None, :]; H = hvec(mm)
        HDH = H.T @ (so[:, None] * H)                                    # Σ_l cos(ω_{2l+1}u₀) h_{l-j}h_{l-j'}
        anti = (cs_even_matrix(T, J, u0) - cs_even_matrix(T, J, 2 * T - u0)).real
        per = (cs_even_matrix(T, J, u0) + cs_even_matrix(T, J, 2 * T - u0)).real
        De = np.diag(np.cos(omega(T, 2 * js) * u0))
        print(f"   T=log2, u₀={u0:.3f}: |HᵀD_oH − [c(u₀) − c(2T−u₀)]|_max = {abs(HDH-anti).max():.1e} (tail ~log L/L, L=1e5);"
              f"  |D_e − [c(u₀) + c(2T−u₀)]|_max = {abs(De-per).max():.1e} (exacto)")

# ----------------------------------------------------------------- part B
def part_B():
    print("\n=== B. The single pointwise object in the index: diag(s_{2j}, s_{2l+1}); minima by parity (ζ and M₁)")
    for T in (0.5 * np.log(3), np.log(2), 0.5 * np.log(5)):
        cs = contacts(T); k = np.arange(0, 4001); s = s_grid(T, k, cs)
        line = f" T={T:.4f}: ζ  min par={s[0::2].min():+.3f} (k={2*s[0::2].argmin()}), min impar={s[1::2].min():+.3f} (k={2*s[1::2].argmin()+1});" \
               f" negativos par k={np.where(s[0::2]<0)[0]*2}, impar k={np.where(s[1::2]<0)[0]*2+1}"
        for d in (0.01, 0.1):
            sM = s + quartet_grid(T, k, GAM1, d)
            line += f"\n            M₁(δ={d}): min par={sM[0::2].min():+.3f}, min impar={sM[1::2].min():+.3f}; negativos par k={np.where(sM[0::2]<0)[0]*2}, impar k={np.where(sM[1::2]<0)[0]*2+1}"
        print(line)

# ----------------------------------------------------------------- part C
def schur_two_sector(T, J, quartet, etas, L=100000):
    cs = contacts(T); M, a, b = fourier_matrix(T, J, cs, quartet=quartet); M = M.real
    js = np.arange(-J, J + 1); n = len(js)
    se = s_grid(T, 2 * js, cs); l = np.arange(-L, L + 1); so = s_grid(T, 2 * l + 1, cs)
    if quartet is not None: se = se + quartet_grid(T, 2 * js, *quartet); so = so + quartet_grid(T, 2 * l + 1, *quartet)
    Q = np.linalg.qr(np.stack([a.real, a.imag], axis=1), mode='complete')[0][:, 2:]   # REAL ON basis of 𝒫_T (b = conj a; M real)
    Mp = Q.T @ M @ Q; Mp = 0.5 * (Mp + Mp.T); lamJ = np.linalg.eigvalsh(Mp)[0]
    print(f" T={T:.4f}{'' if quartet is None else ' M₁ δ=%g' % quartet[1]} J={J}: λ_J = {lamJ:+.4e}")
    for eta in etas:
        ie = np.where(se < eta)[0]; il = l[(so < eta)]
        s_pe = se[se >= eta].min(); s_po = so[so >= eta].min(); c_eta = 0.5 * (s_pe + s_po)
        vecs = [np.eye(n)[:, i] for i in ie] + [hvec(ll - js) for ll in il]      # e_j  and  P_J e'_l = (h_{l-j})_j
        V = Q.T @ np.stack(vecs, axis=1)                                            # projected onto 𝒫_T
        U = np.linalg.qr(V)[0]; d = U.shape[1]                                     # ON basis of N_η ⊂ 𝒫_T
        if d >= n - 2: print(f"   η={eta:.2f}: N_η = all of 𝒫_T (dim {d}); no complement"); continue
        Uc = np.linalg.qr(np.hstack([U, np.eye(n - 2)]), mode='complete')[0][:, d:]  # complement within 𝒫_T
        A_NN = U.T @ Mp @ U; X = Uc.T @ Mp @ U; A_cc = Uc.T @ Mp @ Uc
        lam_c = np.linalg.eigvalsh(A_cc)[0]
        S_ex = A_NN - X.T @ np.linalg.solve(A_cc, X); S_low = A_NN - X.T @ X / c_eta
        print(f"   η={eta:.2f}: dim N={d} (even {len(ie)}, odd {len(il)}), c_η=½(s₊^e+s₊^o)={c_eta:+.3f} [s₊^e={s_pe:.3f}, s₊^o={s_po:.3f}], "
              f"λ_min(𝔞|𝒫∩N⊥)={lam_c:+.3f} ({'≥c_η OK' if lam_c >= c_eta - 1e-9 else 'VIOLATES c_η'}), "
              f"λ_min(S_exacto)={np.linalg.eigvalsh(0.5*(S_ex+S_ex.T))[0]:+.4e}, λ_min(S_low)={np.linalg.eigvalsh(0.5*(S_low+S_low.T))[0]:+.4e}, "
              f"‖X‖²/c_η={np.linalg.norm(X,2)**2/c_eta:.3f}")

def part_C():
    print("\n=== C. Two-sector Schur reduction in the Fourier Galerkin model (J=24, exact Tate functions)")
    for T in (0.5 * np.log(3), np.log(2), 0.5 * np.log(5)):
        schur_two_sector(T, 24, None, (0.0, 0.3, 0.6, 1.0, 1.5))
    for d in (0.01, 0.1):
        schur_two_sector(np.log(2), 24, (GAM1, d), (0.0, 0.3, 0.6, 1.0, 1.5))

# ----------------------------------------------------------------- part D
def odd_tail(T, L, cs, Lmax=20000000):
    """τ_L = (2/π²) Σ_{l>L} s_{2l+1}/l² : tail of HᵀD_oH omitted by the truncation |l|≤L, ≈ (−1)^{j+j'} τ_L (h_m ~ (−1)^m/(πm))."""
    tot = 0.0
    for lo in range(L + 1, Lmax, 2000000):
        ls = np.arange(lo, min(lo + 2000000, Lmax), dtype=float); tot += np.sum(s_grid(T, 2 * ls + 1, cs) / ls ** 2)
    return 2 * tot / np.pi ** 2 + 2 * (np.log(np.pi * Lmax / (2 * np.pi * T)) + 1) / (np.pi ** 2 * Lmax)

def schur_nyquist(T, Jb, quartet, etas, L=200000, tail=False):
    """Like schur_two_sector but with the Nyquist matrix ½(D_e+HᵀD_oH) truncated to |j|≤Jb (no quadrature), exact Tate functions.
    tail=True adds the analytic tail ½τ_L(−1)^{j+j'} (alternating rank one) of the odd modes |l|>L."""
    from r052_nyquist import nyquist_matrix
    cs = contacts(T); js = np.arange(-Jb, Jb + 1); n = len(js)
    M = nyquist_matrix(T, Jb, cs, L=L, quartet=quartet); M = 0.5 * (M + M.T)
    if tail:
        tau = odd_tail(T, L, cs); v = (-1.0) ** js; M = M + 0.5 * tau * np.outer(v, v); print(f"   [odd tail τ_L = {tau:.3e} added]")
    a = (-1.0) ** js * 2 * np.sinh(T / 2) / (np.sqrt(2 * T) * (0.5 + 1j * js * np.pi / T))
    se = s_grid(T, 2 * js, cs); l = np.arange(-L, L + 1); so = s_grid(T, 2 * l + 1, cs)
    if quartet is not None: se = se + quartet_grid(T, 2 * js, *quartet); so = so + quartet_grid(T, 2 * l + 1, *quartet)
    Q = np.linalg.qr(np.stack([a.real, a.imag], axis=1), mode='complete')[0][:, 2:]
    Mp = Q.T @ M @ Q; Mp = 0.5 * (Mp + Mp.T); lamJ = np.linalg.eigvalsh(Mp)[0]
    out = [f" T={T:.4f}{'' if quartet is None else ' M₁ δ=%g' % quartet[1]} Jb={Jb} (L={L}): λ_Jb = {lamJ:+.4e}"]
    for eta in etas:
        ie = np.where(se < eta)[0]; il = l[(so < eta)]
        s_pe = se[se >= eta].min(); s_po = so[so >= eta].min(); c_eta = 0.5 * (s_pe + s_po)
        V = Q.T @ np.stack([np.eye(n)[:, i] for i in ie] + [hvec(ll - js) for ll in il], axis=1)
        U = np.linalg.qr(V)[0]; d = U.shape[1]
        if d >= n - 2: out.append(f"   η={eta:.2f}: N_η = todo 𝒫_T (dim {d}); sin complemento"); continue
        Uc = np.linalg.qr(np.hstack([U, np.eye(n - 2)]), mode='complete')[0][:, d:]
        A_NN = U.T @ Mp @ U; X = Uc.T @ Mp @ U; A_cc = Uc.T @ Mp @ Uc
        lam_c = np.linalg.eigvalsh(A_cc)[0]
        S_ex = A_NN - X.T @ np.linalg.solve(A_cc, X); S_low = A_NN - X.T @ X / c_eta
        out.append(f"   η={eta:.2f}: dim N={d}, c_η={c_eta:+.3f}, λ_min(compl)={lam_c:+.3f}, λ_min(S_ex)={np.linalg.eigvalsh(0.5*(S_ex+S_ex.T))[0]:+.4e}, "
                   f"λ_min(S_low)={np.linalg.eigvalsh(0.5*(S_low+S_low.T))[0]:+.4e}")
    print("\n".join(out), flush=True)

def part_D():
    print("\n=== D. Growth of the complement: Nyquist model |j|≤Jb, Jb = 50…800 (does S_low survive as the complement grows?)")
    for T in (0.5 * np.log(3), np.log(2)):
        for Jb in (50, 100, 200, 400, 800):
            schur_nyquist(T, Jb, None, (0.6, 1.0, 1.5, 2.5))
    print("\n--- D′. with analytic tail of the odd modes (truncation bias), log 2 and ½log5; and M₁")
    for Jb in (100, 400): schur_nyquist(np.log(2), Jb, None, (1.0, 1.5, 2.5), tail=True)
    for Jb in (100, 400): schur_nyquist(0.5 * np.log(5), Jb, None, (1.0, 1.5, 2.5, 3.5), tail=True)
    schur_nyquist(np.log(2), 100, (GAM1, 0.01), (1.0, 2.5), tail=True)

if __name__ == '__main__':
    parts = sys.argv[1] if len(sys.argv) > 1 else 'ABCD'
    if 'A' in parts: part_A()
    if 'B' in parts: part_B()
    if 'C' in parts: part_C()
    if 'D' in parts: part_D()

