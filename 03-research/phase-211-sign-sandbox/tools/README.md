# tools/galerkin_mp.py — multiprecision Galerkin matrices for a_T (NUMERICAL)

Everything this module returns is NUMERICAL. Galerkin minima are upper bounds for λ_A(T)
(up to the stated matrix error); they prove nothing.

```python
import sys; sys.path.insert(0, '03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as g, mpmath as mp
D = g.build(T=1.0, N=90, dps=40)          # true Λ comb, all prime powers n < e^{2T}
D = g.build(1.0, 90, 40, comb=[(mp.log(2), v2), ...])   # any comb [(x, v)]
D['Arch'], D['Pi'], D['A'], D['B']        # mp matrices in the sine basis e_1..e_N
D['err_arch']                             # estimated max entry error of Arch
P   = g.projector(D)                      # orthogonal projector onto P_T (N x N)
Q   = g.sector_basis(D, 'ev')             # orthonormal basis of P_T ∩ even sector ('odd' likewise)
lam, par, res = g.lambda_A(D)             # Galerkin λ_A and parity of the bottom vector
eigs, vecs, all_eigs = g.bottom_eigs(D, 'ev', k=5, mu=1)   # bottom of Arch − mu Π on P_T ∩ sector
Theta, cstar = g.theta(D)                 # max_mu λ_min(Arch − mu Π on P_T)
g.principal_angles(U, V)                  # call inside mp.workdps(...)
g.cluster(all_eigs, 1e-9)                 # size of a near-null cluster
g.margin_bound(T)                         # 4e9 T exp(−15.449 T)  (cor:margin1)
```

Basis: e_k(t) = sin(kπ(t+T)/2T)/√T, k = 1..N; k odd ↔ even functions. Both forms preserve
parity, so all spectral work is done per sector (each sector carries one Tate constraint:
A+B for even, A−B for odd).

Method. Arch uses the Lévy form C_0⟨·,·⟩ + ∫_0^∞ (c(0) − c^sym(u)) K(u) du with the exact
cross-correlations of the sines; every entry reduces to the three moment families
∫_0^{2T} K sin(a_k u), ∫ K(1 − cos a_k u), ∫ K u cos(a_k u) plus the closed-form tail
∫_{2T}^∞ K = −log tanh(T/2) + π − 2 arctan e^{T}. The integrands are analytic on [0, 2T],
so composite Gauss–Legendre (N/2 + 8 panels × 30 nodes, Newton-refined at working
precision) converges geometrically; the error is estimated by a second run with 1.5× panels
and 38 nodes. Π, A, B are exact closed forms. Working precision is dps + 20 digits.
The Fourier-symbol route was rejected: |ê_j ê_k| decays only like τ^{-4} log τ against an
oscillating weight, so reaching 40 digits needs very long quadratures.

Resolution floor: eigenvalues are reliable only above ≈ 10^{-(dps+20)} × (matrix scale) and
above err_arch; at dps = 40 values below ≈ 10^{-57} are noise (raise dps).

Cache: `cache/T{T}_N{N}_d{dps}_{comb}.pkl` holds all matrices as strings of mpf (dps + 20
digits); `build` reloads automatically (pass `cache=False` to force a rebuild).

Timings (one core): build N = 60/90/120 at dps 40 ≈ 20/50/90 s; bottom eigenpairs of both
sectors ≈ 8/25/70 s; theta at N = 60 ≈ 1–2 min.

prolate_gauge_adm.py environment switches: KTOP (high-block cap; measured k_* ≈ 0.32–0.35·Nb at Nb 250–370),
FASTMUL=1 (V^T M V products in python-flint, same values), LAMA=<value> (supply λ_A from a smaller-Nb run; the mp
eigensolve at Nb ≥ 200 exceeds 15 min), STEP=s (evaluate every s-th index). Build times at dps 30: Nb 200/250/300/370 ≈
250/365/525/755 s; Nb 445 > 900 s.
tools/prolate_gauge_3blk.py (ROUND_012_B): three-block LM/H+/H- assembly; env KLIST (tops), SPLIT=range (control split by index range), PROFILE=1 (index profile of the H+/H- coupling); other switches as prolate_gauge_adm.py.
tools/prolate_tailgram.py (ROUND_014_A): class-blind b = Sa view of the high block: band profile, Gershgorin/banded/Toeplitz bounds, constrained D- and l_g-bottoms, gauge alignment; env TOP, TOPS (K sweep), SAVE.
tools/tailgram_quotient.py (ROUND_015_A): reads the SAVE npz of prolate_tailgram.py; constraint compression P_C (= tail Gram on S𝒜 exactly, Prop 1.1), gauge quotient X, band profiles of raw / compressed / removed (rank ≤ 10) / quotient operators, K sweep of the bottoms, Rayleigh quotients of P_X e_k vs m(k). Resolution: trust K ≤ 0.29·Nb.
tools/tail_direct/ (ROUND_016_B): direct tails of the high prolate block, no ξ-Galerkin. coef.py (Legendre coefficients of the
even prolates at T = 0.8, 60 digits, sign D_0 > 0, writes coef08.pkl); tail.py (u_k by the Legendre–spherical-Bessel formula on
a log grid, chirp FFTs F̂_N, ledger B_NN′ = 𝒜_∞(F_N,F_N′) − (log N + log N′)⟨F_N,F_N′⟩, polar A(𝒯u), B(𝒯u); argv[1] = ξ cut,
default 200); run2.py (NPZ=<SAVE file of prolate_tailgram.py>: bottom vectors of X for K = 56…96, chirp attribution table);
efx.py (same vectors in the window variable: Ef by Poisson in x, a_T(Ef) by the Lévy form); cellR.py / cellRp.py (idealised
R-cell limit problem on a window of length log R, without / with the polar term, constraints f(0), f(λ), A, B transported);
adm.py, lg.py, ident.py (explicit admissible probes: a_T(Ef), D, gauge leakage ℓ_g with JG gauge polynomials, and the x-space
check W_T(Ef) = 𝒲[Ψ_f] + 2A(Ψ_f)B(Ψ_f)). Run from tools/ (they import galerkin_mp). Each ≤ 5 min except lg.py (≈ 3 min per J).
tools/schur_coupling_survivor.py T Nb dps (ROUND_017_A): survivor f_* of span{ψ_0..ψ_8} cut by f(0), ℱf(0), A(Ef), B(Ef) (exact functionals), Frobenius edge data, Bessel scale check → cache/surv_*.pkl. NB: eproj vectors carry a factor λ^{1/2}.
tools/schur_coupling_galerkin.py T Nb dps: Galerkin Schur data of the survivor against P_T ⊖ Ef_* (both sectors) → cache/schur_*.pkl.
tools/schur_coupling_tail.py T Nb [nmax] [Lx]: Poisson tail Ψ of the survivor (prolate ODE + edge asymptotics + Bernoulli closed forms; checked against the finite Poisson sum), comb pairings per prime power and archimedean pairing per sine → cache/tail_*.npz (≈ 4–8 min).
tools/schur_coupling_split.py T Nb dps: arch/comb/Tate split, Schur shares by sector and eigen-direction, 5-block X, cΛ scan, a_3.
tools/rung_gram_prep.py T nP [dps] (ROUND_018_B): even prolates ψ_0..ψ_{2nP−2}, exact constraint rows, survivor, admissible null space, Frobenius/scale → cache/rung_prep_*.pkl (nP = 11: 5–11 min; nP = 21 at dps 50: 10 min).
tools/rung_gram_tail.py T nP h L: per-prolate Poisson tails on a uniform grid; 𝒜_∞ (Lévy, FFT), comb over prime powers, A, B, window masses → cache/rung_tail_*.npz (ODE cached in cache/rung_u_*.npy; first run 2–4 min parallel, then ≤ 4 min). Grid error: ρ 0.6 %, comb 3 % between h = 1e-4 and 5e-5.
tools/rung_gram_schur.py npz lamA: exact ledger, Schur balance on the admissible E-images, rungs (parity tag by ψ_{4j+2} mass), and the c-scan of the tail form (log N → c log N) with det₂ zeros.
tools/cert_window/ (ROUND_026_A): rigorous (Arb ball) lower certificate for λ_A(T) by Paper 47 prop:lowercert with a
certified floor. build_G.py T_expr tauN s_num s_den K2 [prec] [out] (T_expr ∈ {log5h, 1, 1.035, 1.098, 1.2,
log15h+0.01}; env PART/NPART for parallel node ranges): interval scan s_T ≥ s_∞ on [τ_N, τ_B], Gauss–Legendre panels
with Bernstein-ellipse remainders, spherical Bessel by ball recurrence at adaptive precision, Gram data of both parities
→ pickle. combine.py out parts… sums partial pickles. run_waves.sh T tauN K2 NP W out: resumable launcher (skips parts
already saved). cert.py G.pkl par k1 mu[,mu…]: Householder + Haynsworth + Gershgorin-on-XSXᵀ positive-definiteness
certificate (prints "certified": true/false). inertia_mid.py: NUMERICAL inertia of the midpoint Schur complement.
Validated: reproduces thm:log5A (2.5e-12 even / 3.0e-10 odd). Timings: T = 1 build 5 × 40 min, certificate 2–20 min.
