# Prolate / time–band-limiting references (imported for phase 155, round 7a)

Bibliography only — no PDF held in the repo; every inequality taken from these is
`CITED-NOT-VERIFIED` until a copy is checked. Operator: `S_c = Q_T B_s Q_T`, `c = Ts`,
eigenvalues `1 > λ_0(c) > λ_1(c) > … > 0`, `tr S_c = 2c/π`.

1. D. Slepian, H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty — I*,
   Bell System Tech. J. **40** (1961), 43–63.
2. H. J. Landau, H. O. Pollak, *… — II*, BSTJ **40** (1961), 65–84; *… — III*, BSTJ **41** (1962), 1295–1336.
   (Source of `λ_n ∈ (0,1)`, simplicity, the plateau/plunge picture.)
3. H. J. Landau, H. Widom, *Eigenvalue distribution of time and frequency limiting*,
   J. Math. Anal. Appl. **77** (1980), 469–481.
   `#{n : λ_n(c) > θ} = 2c/π + (1/π²)·log c·log((1−θ)/θ) + o(log c)` — **asymptotic only**, no explicit `c₀`.
4. A. Bonami, A. Karoui, *Uniform bounds of prolate spheroidal wave functions and eigenvalues decay*,
   C. R. Acad. Sci. Paris Ser. I **352** (2014), 229–234.
5. A. Bonami, A. Karoui, *Uniform approximation and explicit estimates for the prolate spheroidal wave
   functions*, Constr. Approx. **43** (2016), 15–45.
6. A. Bonami, A. Karoui, *Spectral decay of time and frequency limiting operator*,
   Appl. Comput. Harmon. Anal. **42** (2017), 1–20.
   (4)–(6) are the sharpest **non-asymptotic** super-exponential decay bounds `λ_n(c) ≤ …` valid for
   `n` above a threshold of the form `n ≥ 2c/π + O(log c)`; the exact constants and thresholds must be
   read off a copy before use.
7. A. Bonami, P. Jaming, A. Karoui, *Non-asymptotic behavior of the spectrum of the sinc-kernel operator
   and related applications*, J. Math. Phys. **62** (2021), 033511.
8. A. Osipov, V. Rokhlin, H. Xiao, *Prolate Spheroidal Wave Functions of Order Zero: Mathematical Tools
   for Bandlimited Approximation*, Applied Mathematical Sciences **187**, Springer, 2013.
   (Explicit inequalities, Legendre expansion of the PSWFs, numerical algorithms.)
9. A. Israel, *The eigenvalue distribution of time-frequency localization operators*, arXiv:1502.04404.

**Note.** Round 7a's Theorem P (`R155_047 §3`) is self-contained (Ky Fan + the Legendre/spherical-Bessel
diagonal of `S_c`) and needs none of (3)–(9); those remain the reference point for sharpness.
