# Round 1, memo A: the near-coincidence form along Dirichlet polynomials, by Poisson summation on ℤ

Object: Q_M(s) = s^⊤𝔸_M s for the profile F_0 of STATEMENT_001 §2 (2T_0 < log 2), N = N(M) = ⌈M e^{2T_0}⌉,
s_N(τ) = m(τ) − Σ_{2≤n<N} v_n cos(τ log n), and

    Q_M(s) = (1/2π) ∫ F̂_0(τ)² |P_s(τ)|² s_N(τ) dτ,    P_s(τ) = Σ_{m≤M} s_m m^{iτ}     (Paper 46 prop:AM(ii), CITED).

Family studied: s_w(m) = m^{−1/2} w(m/M), w ∈ C^∞[0,∞), w ≡ 1 on [0, e^{−L}], w ≡ 0 on [1,∞), L > 0 fixed.

## 0. Corrections to the formulation of the object

(0.1) PROVED. With ζ(s) = χ(s)ζ(1−s), χ(s) = π^{s−1/2} Γ((1−s)/2)/Γ(s/2):
(χ'/χ)(s) = log π − ½ψ((1−s)/2) − ½ψ(s/2); at s = ½+iτ the two digammas are conjugate, so
(χ'/χ)(½+iτ) = log π − Re ψ(¼+iτ/2) = −m(τ). Writing χ(½+iτ) = e^{−2iθ(τ)} (θ real), m(τ) = 2θ'(τ).

(0.2) PROVED, with a sign correction. v_n cos(τ log n) = 2Re(Λ(n) n^{−1/2−iτ}), hence
−Σ_{n<N} v_n cos(τ log n) = −2Re Σ_{n<N} Λ(n) n^{−s} (s = ½+iτ), which is the truncation of **+2Re(ζ'/ζ)(s)**
(not of −2Re ζ'/ζ). Differentiating the functional equation: (ζ'/ζ)(s) + (ζ'/ζ)(1−s) = (χ'/χ)(s); on the line
1−s = s̄, so 2Re(ζ'/ζ)(½+iτ) = −m(τ) wherever ζ(½+iτ) ≠ 0. Hence s_N is formally 2Re Σ_{n≥N} Λ(n) n^{−s}, and
m(τ)|ζ(½+iτ)|² = −2Re(ζ'(s) ζ(1−s)) on the whole line (both sides continuous).

## 1. The decomposition (Poisson on ℤ / Mellin–Euler–Maclaurin)

Let w̃(u) = ∫_0^∞ w(x) x^{u−1} dx. It is meromorphic in ℂ with a single pole, at u = 0, residue 1 (because w ≡ 1
near 0 all further residues w^{(k)}(0)/k! vanish), and decays faster than any power on vertical lines.

**Lemma 1 (PROVED).** For z = ½ − iτ and every K > 0,

    P_{s_w}(τ) = Σ_{m≤M} m^{−z} w(m/M) = ζ(½−iτ) + C_M(τ) + R_M(τ),    C_M(τ) = M^{1/2+iτ} w̃(½+iτ),
    R_M(τ) = (1/2πi) ∫_{(−K)} ζ(z+u) w̃(u) M^u du = O_{K,w}( M^{−K} (1+|τ|)^{K} ).

Proof. Mellin inversion gives Σ_m m^{−z} w(m/M) = (1/2πi)∫_{(c)} ζ(z+u) w̃(u) M^u du, c > ½. Move to Re u = −K:
residue at u = 1−z (pole of ζ) is M^{1−z} w̃(1−z) = C_M; residue at u = 0 (pole of w̃) is ζ(z); no other poles.
On Re u = −K, |ζ(z−K+iv)| ≪ (1+|τ|+|v|)^{K} by the functional equation and Stirling, and w̃(−K+iv) decays
rapidly in v. ∎  In t = log y the three pieces are: the lattice measure μ = Σ_m m^{−1/2} w(m/M) δ_{log m};
its continuous shadow μ_C = e^{t/2} w(e^t/M) dt; and the Poisson dual μ − μ_C. The term R_M is where the
functional equation (the Γ-kernel of the dual sum of length |τ|/(2πM)) enters; it is non-negligible only for
|τ| ≳ 2πM. NUMERICAL check: |P − C − ζ| < 3·10^{−8} at τ ∈ {0,3}, M ∈ {50,100,200} (mpmath, 30 digits).

Insert Lemma 1 in Q_M(s_w). Write Φ = F̂_0², and recall F̂_0(τ) = (τ²+¼)|ĝ(τ)|⁴, so as a function of
s = ½+iτ, Φ carries the factor s²(1−s)² (double zeros at s = 0, 1).

**Theorem 1 (PROVED, modulo the routine growth bounds stated in the proof).**

    Q_M(s_w) = M·𝒜(w) + 𝒳_M(w) + 𝒵_N + ℛ_M(w),

(a) Continuous part. 𝒜(w) = (1/2π)∫ Φ |w̃(½+iτ)|² s_N dτ is independent of M and equals the continuous window form
a_{T'}(F_0 ∗ W) of the single vector F_0 ∗ W, W(t) = e^{t/2} w(e^t), at the window T' = (L + 2T_0)/2. Proof:
C_M is the Fourier transform of μ_C, and F_0 ∗ μ_C = M^{1/2}(F_0 ∗ W)(· − log M); F_0 ∗ W vanishes for
t < −L − T_0 (there W = e^{t/2} and B(F_0) = 0) and for t > T_0, so its autocorrelation lives in |u| ≤ L + 2T_0
and only the comb atoms log n ≤ L + 2T_0 survive. Translation invariance gives the factor M. Note A(F_0∗W) = 0 but
B(F_0∗W) = Res·F̂_0'(i/2) ≠ 0 in general: the polar mode of the pole of ζ at 1 is split between C_M and ζ, so
F_0∗W is NOT in P_{T'} and 𝒜(w) ≥ 0 is not covered by λ_A(T') ≥ 0.

(b) Cross (edge) term. 𝒳_M = (1/π)Re ∫ Φ s_N ζ(½−iτ) conj C_M dτ = O_K(M^{−K}) for every K. Proof: by (0.2),
s_N ζ(z) = −[ζ'(z) + ζ(z)Σ_{n<N}Λ(n)n^{−z}] − ζ(z)[(ζ'/ζ)(1−z) + Σ_{n<N}Λ(n)n^{−(1−z)}], and conj C_M = M^{z} w̃(z).
First bracket: move to Re z = σ > 1; it becomes ζ(z)Σ_{n≥N}Λ(n)n^{−z}; since Φ is the transform of c_0
(support |u| ≤ 2T_0), |Φ| ≪ e^{2T_0σ}(1+|τ|)^{−4} there, and each atom carries (M e^{2T_0}/n)^σ ≤ 1 with
strict decay for n > N... letting σ → ∞ the integral is 0 (Paley–Wiener: the shifted supports do not meet).
Second bracket: move to Re z = −c < 0; it becomes −ζ(z)Σ_{n≥N}Λ(n)n^{−1+z}·M^{z}, of size (MN)^{−c}; the only
pole crossed is z = 0, where (ζ'/ζ)(1−z) and w̃(z) have simple poles and Φ a double zero: no residue. ∎
NUMERICAL: the archimedean and comb parts of 𝒳 are each ≈ 3·10^{−8} at M = 25 and cancel to 10^{−12} at M ≥ 50.

(c) ζ-term. 𝒵_N = (1/2π)∫ Φ |ζ(½+iτ)|² s_N dτ = (1/π) ∫_{Re s=σ} Φ ζ(s)ζ(1−s) Σ_{n≥N} Λ(n) n^{−s} dτ, any
1 < σ < 7/2, an absolutely convergent expression, hence 𝒵_N = O_σ(N^{1−σ}) = O(N^{−5/2+ε}). Proof: by (0.2) and
evenness, 𝒵_N = −(1/π)∫Φ ζ(1−s)[ζ'(s) + ζ(s)Σ_{n<N}Λ(n)n^{−s}]dτ; shift to Re s = σ (at s = 1 the double pole of
ζ' and the simple pole of ζ are cancelled by the double zero of Φ), and there ζ' = −ζ Σ_{all n}Λ(n)n^{−s}. The bound
σ < 7/2 comes from |Φ| ≪ |τ|^{−4}, |ζ(1−s)| ≪ |τ|^{σ−1/2}. ∎  The direct line integral does not converge
numerically at |τ| ≤ 300 (it oscillates between −1.4·10^{−5} and +6·10^{−4}); the shifted form gives
𝒵 ≈ −1.0·10^{−5} at M = 50 (σ = 1.3 and 1.6 agree), and |𝒵| ≲ 3·10^{−5} at M = 100, 200 (not converged).

(d) ℛ_M collects 2Re(ζ R̄) + 2Re(C R̄) + |R|² against Φ s_N. Lemma 1 with K < 3 and Φ ≪ |τ|^{−4} give
ℛ_M = O(M^{−3+ε}) ARGUED (the cross piece with C needs the same Paley–Wiener shift as (b); not written out).

NUMERICAL validation (T_0 = 0.15, b = 1, L = log 2, w = smooth step on [½,1]; Q_M from the matrix code of the
near-coincidence experiment; 𝒜 from the τ-integral):

| M | Q_M(s_w) | M·𝒜(w) (𝒜 = 1.56421·10^{−5}) | Q_M − M𝒜 |
|---|---|---|---|
| 25 | 1.4729·10^{−2} | 3.911·10^{−4} | 1.43·10^{−2} |
| 50 | 2.5975·10^{−3} | 7.821·10^{−4} | 1.82·10^{−3} |
| 100 | 1.8388·10^{−3} | 1.5642·10^{−3} | 2.75·10^{−4} |
| 200 | 3.1678·10^{−3} | 3.1284·10^{−3} | 3.9·10^{−5} |

𝒜 is constant in M to 15 digits. The remainder decays by a factor ≈ 7–8 per doubling (exponent ≈ −2.8 to −3), and is
dominated by ℛ_M (|𝒵| is two orders smaller at M = 50). Div(s_w) grows like (log M)² (8.4 → 24.9) and is cancelled by
Near and Arch to the precision shown: nothing of it survives in the decomposition.

## 2. Answers to the questions of the round

(Q1) Does the dual sum reproduce Div_M exactly? **No** (PROVED by Theorem 1). The Poisson dual (the AFE dual sum,
non-empty only for |τ| ≳ 2πM) enters only through ℛ_M, of size O(M^{−3+ε}); the exact Dirichlet coincidences
(Div_M) and the near ones (Near_M) are pure lattice bookkeeping that Poisson summation re-sums into M·𝒜(w) + ζ-term.
The relation 1∗Λ = log is used exactly once, in (c), in its analytic form ζ' = −ζ·Σ Λ n^{−s} on Re s > 1.

(Q2) Phase-190 residue: is the edge term PNT-error size or margin size? **Neither, on this family.** The edge
(cross) term 𝒳_M, which is where a smoothed Chebyshev sum at scale M would sit, is O(M^{−K}) for every K (PROVED,
(b)): the comb atoms n ≈ M are annihilated exactly against the archimedean part by the functional equation and
the support of c_0. The Λ-specific remainder is 𝒵_N = O(N^{−5/2+ε}) (margin size, absolutely convergent, no sign),
and the dominant remainder ℛ_M ~ M^{−3} is controlled by the decay |F̂_0|² ≍ |τ|^{−4}.
ARGUED (not proved): the exponent −3 of λ_min(𝔸_M) recorded in the near-coincidence experiment is the regularity
exponent of the profile (Φ ≍ |τ|^{−4}), not an arithmetic margin; test: repeat with G_0 = c_g∗c_g∗c_g
(Φ ≍ |τ|^{−8}) — the exponent should move to ≈ −7.

(Q3) Sign. On the family s_w, Q_M(s_w) ≥ 0 for all M large is equivalent (up to O(M^{−3+ε})) to 𝒜(w) ≥ 0, i.e. to
the continuous window form at the fixed window T'(w) = (L+2T_0)/2 on the one vector F_0∗W. The lattice problem
along Dirichlet polynomials is therefore transferred back to the continuous window form: a restatement, not a sign.

## 3. Falsifier test (rule 4)

Theorem 1 holds verbatim for any comb b replacing Λ, with 𝒵 replaced by 𝒵^b_N = (1/2π)∫Φ|ζ|²(m − comb^b_{<N}).
(a) cΛ: 𝒵^b → (1−c)(1/2π)∫Φ|ζ|²m ≠ 0, O(1). (b) a_P: 𝒵^b → (1/2π)∫Φ|ζ|²·(comb of Λ on p < P) ≠ 0, O(1).
(d) finite modification: 𝒵^b changes by an O(1) constant. In all three cases Q_M = M·𝒜^b(w) + O(1), so the sign for
large M is decided by 𝒜^b (a window form at fixed T' with comb b) exactly as for Λ: the decomposition does not
separate Λ from (a), (b), (d) at leading order. (c) Beurling systems whose zeta continues with a functional
equation: Lemma 1 holds with the Beurling lattice whenever ζ_B continues to Re u ≤ −K with polynomial growth, and
(b), (c) go through with Λ_B; the argument survives (c). Hence no sign step exists here; the decomposition is a
transfer identity.

## Corpus check

- Near-coincidence experiment (phase 190): EXP_003/EXP_005 found the minimiser ≈ m^{−1/2}w(m/M), λ_min ≍ M^{−3},
  and the identity s^⊤(Div+Near)s = 2Σ_N N^{−1/2}log N·E_M(N) on the pure vector m^{−1/2} (W7, no sign). Their next
  step (EXP_005 §6: bulk/edge split, is the edge a PNT error?) is answered here, differently from their
  expectation: the edge is O(M^{−K}); the bulk is M·𝒜(w); the M^{−3} is plausibly profile regularity.
  Difference from C3: C3 is an algebraic identity on the lattice for one vector; Theorem 1 is an analytic
  identity (Poisson + functional equation) for the whole smooth-cutoff family.
- AFE / Riemann–Siegel as a class (L2_012, G3C-R163_603, Z_CARRIER_001, DH_TRANSFER_001: "AFE transfers to DH,
  FE-only data"): Theorem 1 is consistent with these and adds where the dual sum sits in 𝔸_M (only in ℛ_M).
  The new reason for entering was the question of the brief (does the dual reproduce Div?); the answer is no.
- Factor ζ(½+iτ) route (DOSSIER §4.3, INV_K_001): Lemma 1 does produce the factor ζ(½−iτ) in P_{s_w}, but as a
  summand, not a multiplier of the comb; its only contribution, 𝒵_N, is Λ-specific yet margin-size and without sign.
- Paper 48, empty cell / J = χ(½+it)·reflection (P48:414–422, Table compose): NO-GO there for weight-½ forms; the
  reflection here acts on the Dirichlet polynomial, not on a modular object; the outcome (transfer, no sign) is
  the same.
- Grid and routes index: no entry for the decomposition Q_M(s_w) = M𝒜 + 𝒳 + 𝒵 + ℛ or for the vanishing of the
  edge term; proposed index row below.

Proposed index row: | P211-A | Poisson/AFE decomposition of Q_M on s_w = m^{−1/2}w(m/M): Q = M·𝒜(w) + O(M^{−K}) edge
+ 𝒵_N (ζ-tail, O(N^{−5/2})) + ℛ_M (dual sum, O(M^{−3+ε})) | lattice-to-continuum transfer | ROUND_001_A | PROVED
(identity), NO-GO for the sign (survives cΛ, a_P, finite modification, continuing Beurling at leading order) | edge
is not PNT-size; M^{−3} conjecturally profile regularity |

## Result

NO-GO with class: **lattice-to-continuum transfer by Poisson summation on ℤ / approximate functional equation for
smooth-cutoff Dirichlet polynomials.** The identity is exact and partly ζ-specific (the term 𝒵_N), but at leading
order it returns the continuous window form at a fixed window, and the falsifiers (a), (b), (d) pass through it.

## What was proved

- (0.1) m = −(χ'/χ)(½+iτ) = 2θ'; (0.2) the comb is the truncation of +2Re ζ'/ζ (sign corrected) and m|ζ|² = −2Re(ζ'ζ̄).
- Lemma 1 (exact three-term split of P_{s_w}); Theorem 1 (a), (b), (c): Q_M(s_w) = M𝒜(w) + O(M^{−K}) + 𝒵_N + ℛ_M,
  with 𝒜 the continuous window form of F_0∗W at window (L+2T_0)/2 (a vector with B ≠ 0), the edge term
  superpolynomially small, and 𝒵_N given by an absolutely convergent integral on Re s = σ, O(N^{−5/2+ε}).

## What failed and why

- The dual sum does not reproduce Div_M; it sits only in ℛ_M (|τ| ≳ 2πM) and is controlled by the decay of F̂_0.
- No sign: the leading term is a continuous window form (restatement), and the only Λ-specific term 𝒵_N is
  margin-size without sign; (a), (b), (d) change only O(1) terms. ℛ_M = O(M^{−3+ε}) is ARGUED, not proved.

## Next concrete step

Run the regularity test of (Q2): rebuild F_0 with one more autocorrelation (|F̂_0|² ≍ |τ|^{−8}) and measure
λ_min(𝔸_M) and Q_M(s_w) − M𝒜(w) for M ≤ 400. If the exponent moves from −3 to ≈ −7, the M^{−3} of the
near-coincidence experiment is a regularity effect and the near-coincidence form carries no arithmetic margin at
scale M on smooth families; the sign must then be sought on non-smooth (arithmetic) vectors, where Lemma 1's
remainder is not small.
