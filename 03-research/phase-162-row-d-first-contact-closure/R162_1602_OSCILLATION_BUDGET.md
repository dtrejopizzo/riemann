# R162_1602 — Oscillation budget: Sturm/Courant theory for the bottom of the primitive problem

Note. Pure mathematics, no numerics. Target: R-A of R162_1501, the oscillation budget.
Inputs: README (F1–F4), R162_590, R162_1501 (Lemma D, targets R-A/R-C), R162_504 (Thm 1, Beurling–Deny form),
R162_1301, R155_044/045/046 (Thm N3), phase-106 `106_42` (Prop 1).

**Status.**
- **NO-GO (PROVED)** for the Karlin/Gantmacher–Krein route at the resolvent level, for every model.
  Theorems K1–K3 show that no resolvent or short-time semigroup of A_T is TP₂. The obstruction is the jump
  structure itself, not the comb. Λ*1 = log cannot restore TP₂.
- **PROVED**: an exact nonlocal Courant identity (Prop C). It shows that the variational Courant method gives a test
  space of dimension 2 whatever S(F) is. So positivity of the kernel yields **no** upper bound S(F) ≤ S₀.
- **PROVED**: the comb-free archimedean ground state is symmetric decreasing (Prop R). The comb breaks the
  rearrangement inequality (Lemma R′). This is exactly where R-C (C2) loses its tool.
- **PARTIAL**: Theorem K2, non-TP₂ at every spectral shift, is proved on the whole line and for the killed and comb
  kernel up to a cited Tauberian asymptotic.
- R-A is **not** closed. The only budget statement left standing is a quantitative same-sign penalty (§5, open).

No sign is claimed. No label moves.

## 0. Corpus check, and how this note differs from what is already there

- R155_046 Thm N3: the **jump kernel** k is CM, hence log-convex, hence not PF₂. The semigroup case t ≥ 1 was left
  OPEN, and N3 notes it would not transfer through the codim-2 compression.
- 106_42 Prop 1: the **short-time off-diagonal semigroup kernel**, taken away from the ridges |x−y| = log n, is not
  TP₂.
- R162_1501: Lemma D uses TP legitimately, on the **moment side** (the Laplace kernel e^{−at} is ETP). It needs an
  upper bound on S(F) that the operator must supply.
- New here:
  1. **K1** (resolvent, all large shifts, form-level and rigorous) holds for the comb alone, for k alone, and on
     the window.
  2. **K2** (every shift): the whole-line resolvent density is CM in |x| (Stieltjes structure).
  3. **K3**: TP₂ of a Markov resolvent ⟹ locality. This is the structural reason: Perron and Karlin are
     compatible only for nearest-neighbour or diffusion generators.
  4. The nonlocal Courant identity (Prop C).
  5. The rearrangement break by the comb (Prop R, Lemma R′).
  6. The arithmetic check of whether Λ*1 = log restores TP (§4): it does not.
- grep terms used: "Karlin", "TP2", "total posit", "Courant", "Sturm", "polarization", "rearrangement",
  "Almgren". None of 1–6 above was found in phases 106–162.

## 1. Setting

Take the Beurling–Deny form of R162_504 Thm 1(ii). For real F on I_T, extended by zero:

  a_T(F) = m(0)‖F‖² + ½∬(F(t)−F(s))² k(t−s) dt ds − Σ_{n∈N_T} v_n c_F(log n),   with k(u) = Σ_{j≥0} e^{−(2j+½)|u|} > 0.

The off-diagonal part of A_T is therefore −J, where J(t,s) = k(t−s) + ½Σ v_n[δ(t−s−log n) + δ(t−s+log n)] ≥ 0.
Here v_n ≥ 0 for ζ, and for every a ≥ 0 (deletion, κ).

Fact (subordination). Each e^{−α|u|} is CM in u², so k(u) = h(u²) with h CM. Hence m(τ) − m(0) = φ(τ²) with φ a
complete Bernstein function. The archimedean process is a subordinate Brownian motion. This is new in form;
R154_013 recorded "no Bernstein-in-τ² statement".

Karlin/Gantmacher–Krein (CITED: Karlin, *Total Positivity*, Ch. 10; Gantmacher–Krein, Ch. IV). If for some shift
λ > −μ₁ the kernel of R_λ = (λ + A_T)^{−1} on I_T is an oscillation kernel, then the k-th eigenfunction has exactly
k−1 sign changes, and consecutive eigenfunctions interlace. The two-constraint bottom would then obey a budget
S ≤ 2 + index. This hypothesis is what §2 destroys.

## 2. Non-TP of the resolvent — NO-GO theorems

TP₂ is used in its measure form: a kernel R is TP₂ if det[⟨f_i, R g_j⟩]_{i,j=1,2} ≥ 0 for all 0 ≤ f₁, f₂, g₁, g₂
with supp f₁ < supp f₂ and supp g₁ < supp g₂. This form is equivalent to TP₂ of the pointwise kernel whenever
the kernel is continuous off the diagonal, and it is the form Karlin's variation-diminishing theorem uses.

**Theorem K1 (PROVED).** Suppose there are points x < y < z in int I_T with J(x,z) > 0. This holds always, since
k > 0 everywhere. It also holds with k ≡ 0 as soon as some v_n > 0 with log n < 2T. Then:
- R_λ = (λ + A_T)^{−1} is not TP₂ for all sufficiently large λ;
- e^{−sA_T} is not TP₂ for all sufficiently small s > 0.

*Proof.*
1. Choose nonnegative bumps f₁ at x, f₂ = g₁ = φ at y, and g₂ at z, all in C_c^∞(int I_T). Take their supports
   disjoint, except f₂ = g₁.
2. C_c^∞(int I_T) ⊂ D(A_T). Indeed, m(D)g is in L²(R) for Schwartz g, because the symbol has log growth. So
   a_T(g, h) = ⟨1_I m(D)g − comb g, h⟩ for all h in the form domain.
3. The resolvent identity gives R_λ g = g/λ − A g/λ² + R_λ A² g/λ²… In form, it suffices to write
   ⟨f, R_λ g⟩ = ⟨f,g⟩/λ − ⟨f, Ag⟩/λ² + ⟨Af, R_λ Ag⟩/λ²,
   and the last term is O(λ^{−3}) because A is bounded below.
4. For disjoint supports, −⟨f, Ag⟩ = ∬ f(t) g(s) J(t,s) ≥ 0. With J₁₃ := ∬ f₁ g₂ J > 0, the entries are:
   - M₁₁ = O(λ^{−2});
   - M₂₂ = O(λ^{−2});
   - M₁₂ = J₁₃/λ² + O(λ^{−3});
   - M₂₁ = ‖φ‖²/λ + O(λ^{−2}).
5. Hence det M = M₁₁M₂₂ − M₁₂M₂₁ = −J₁₃‖φ‖²/λ³ + O(λ^{−4}) < 0.
6. The semigroup case is identical, with ⟨f, e^{−sA}g⟩ = ⟨f,g⟩ − s⟨f,Ag⟩ + O(s²). ∎

- K1 covers **both** the archimedean part and the comb, **separately**.
- The comb alone, J = ½Σv_n(δ_{log n} + δ_{−log n}), already kills TP₂ through the triple (x, y, x + log n).
- The minor is negative to leading order. The sign of that order is fixed by J ≥ 0, which is **the same positivity
  that gives Perron** (R162_504 Thm 1).

**Theorem K3 (TP ⟹ locality; PROVED, finite-dimensional form).** Let Q be a symmetric generator on {1, …, N} with
Q_{ij} ≥ 0 for i ≠ j. If (λ − Q)^{−1} is TP₂ for all large λ, then Q_{ij} = 0 whenever |i−j| ≥ 2, so Q is
birth–death.

*Proof.* This is K1 with rows (i, i+1) and columns (i+1, j). The determinant equals
Q_{i,i+1}Q_{i+1,j}/λ⁴ − Q_{ij}/λ³ + O(λ^{−4}), which is < 0 if Q_{ij} > 0. ∎

- The converse is classical (Karlin–McGregor): birth–death resolvents are TP.
- **Consequence.** Every Galerkin or lattice discretisation of A_T is a full M-type matrix, so its resolvent is not
  TP₂. On a finite ordered state space, Perron (irreducible J ≥ 0) and Karlin are simultaneously available only for
  a local, tridiagonal generator.
- For A_T the jump kernel is supported everywhere, so the Sturm theorem of Gantmacher–Krein **cannot** be imported
  at any discretisation level.

**Theorem K2 (every shift).**
(a) PROVED, whole line. For every c > 0, the density G_c of (c + m(D) − m(0))^{−1} on R is completely monotone in
|x| and strictly log-convex on (0, ∞). Hence G_c(x−y) is not TP₂.
*Proof.*
1. φ is complete Bernstein, so c + φ is complete Bernstein too, and 1/(c + φ(τ²)) is a Stieltjes function of τ²:
   ∫ σ(dr)/(τ² + r). Its atom at ∞ is 0 because φ → ∞.
2. The Fourier inverse of 1/(τ² + r) is e^{−√r|x|}/(2√r). So G_c(x) = ∫ e^{−√r|x|} σ̃(dr), which is CM.
3. σ̃ is not a single atom, because a single atom would force φ to be affine in τ², i.e. a local operator.
   Cauchy–Schwarz then makes log G_c strictly convex on (0, ∞).
4. The minor at the points (0, h; d, d+h) with d > h > 0 is G(d)² − G(d−h)G(d+h) < 0. ∎

(b) PARTIAL, window. On I_T the kernel of R_λ, for any λ > −μ₁, equals G_c(x−y) minus a killing correction that
is bounded on compacts of int I_T, plus comb terms.
- The comb terms are singular only on the ridges x − y ∈ Σ ±log n. The shift-0 returns (for example, log 2 − log 2)
  are smoother than G by a factor of at least log^{−1}.
- If G_c(r) is regularly varying of index −1 at 0 (heuristically G ≍ 1/(r log²(1/r)), by the Tauberian theorem for
  the slowly varying symbol 1/log τ; CITED Bingham–Goldie–Teugels §4, **not checked here**), then the minor at
  scale d → 0 with h = d/2 is ≈ −⅓G(d)². That dominates all corrections.
- So R_λ is not TP₂ for **every** admissible λ, and hence no shift makes R_λ an oscillation kernel.
- Status: PARTIAL, pending that asymptotic.

**Reading.**
- The failure is at the **archimedean scale r → 0**. Arithmetic lives at scales ≥ log 2 and cannot touch it.
- The Karlin route is therefore closed for ζ, for deletion, for κ, for DH, and for any datum.
- This is not an F3-blindness issue. The hypothesis is false for all models, including the comb-free one.
- This settles N3's OPEN semigroup item at small time and at every resolvent shift (K1, and K2(b) modulo the
  citation). It does **not** settle large-time e^{−sA}, which Karlin would not need anyway once every R_λ fails.

## 3. What positivity does give: the nonlocal Courant identity

**Proposition C (PROVED).** Let F be real with finitely many nodal intervals D_1, …, D_M, with signs s_i. Suppose
F solves the constrained Euler–Lagrange equation A_T F = λF + r, where r ∈ span{e^{t/2}, e^{−t/2}} is the Tate
residue (eq:localweak). Put G_i = F·1_{D_i}. Then for every c ∈ R^M:

  a_T(Σc_iG_i) − λ‖Σc_iG_i‖² = Σ_i c_i²⟨r, G_i⟩ + ½Σ_{i≠j}(c_i − c_j)² s_i s_j W_{ij},   where W_{ij} = ∬|G_i(t)||G_j(s)| J(t,s) ≥ 0.

*Proof.*
1. Expand: a(ΣcG) = Σc_i² a(G_i) + Σ_{i≠j} c_i c_j a(G_i, G_j).
2. The Euler–Lagrange equation gives a(G_i) = ⟨AF, G_i⟩ − Σ_{j≠i} a(G_i, G_j) = λ‖G_i‖² + ⟨r, G_i⟩ − Σ_{j≠i} a(G_i, G_j).
3. For disjoint supports, a(G_i, G_j) = −s_i s_j W_{ij}.
4. Collect terms using c_i² − c_ic_j + c_j² − c_ic_j = (c_i − c_j)². ∎

Local Sturm–Liouville is the case W_{ij} = 0. There any M-dimensional c gives Courant's bound.

**Corollary C1 (NO-GO for the variational budget; PROVED).**
- Same-sign pairs enter with the penalty +½(c_i − c_j)²W_{ij}. Since k > 0 everywhere, W_{ij} > 0 for **all**
  pairs.
- So the Courant comparison can only use c constant on same-sign domains. That test space has dimension 2
  (c = c₊ on positive domains, c₋ on negative ones), independently of M.
- The resulting inequality, a(c₊F₊ − c₋F₋) ≤ λ‖·‖² + Tate terms, is the F₊/F₋ splitting behind Perron. It is
  insensitive to S(F).
- This is the continuum form of the Davies–Gladwell–Leydold–Stadler theorem on a complete graph: at most 2
  strong nodal domains, which says nothing about sign changes on the line.
- Hence **no bound S(F) ≤ S₀ follows from positivity (k > 0, v_n ≥ 0) plus the two constraints**. R-A needs a
  quantitative input.

**Two-constraint count (PROVED, conditional form).**
- Suppose the same-sign penalty could be neglected, i.e. the local case.
- Choose c ∈ R^M in the kernel of the 2 linear Tate functionals and of the ⟨r, G_i⟩ terms. With r in span, only
  2 + 1 conditions are needed, since Σ_i c_i²⟨r, G_i⟩ can be killed on a codim-1 cone for M ≥ 2.
- This yields a space of dimension ≥ M − 3 on which a ≤ λ. If λ is the k-th primitive level, then M − 3 ≤ k − 1,
  i.e. **S(F) = M − 1 ≤ k + 2**, which is "2 + index" (index k = 1 for the bottom: S ≤ 3, and with parity S = 2).
- For A_T this step fails exactly at the term ½Σ(c_i − c_j)² s_i s_j W_{ij}, i.e. at the positive jump mass between
  same-sign nodal intervals.

## 4. Where the comb breaks it, and whether Λ*1 = log could restore it

(i) **Comb vs rearrangement.**

**Prop R (PROVED).** For the comb-free form (v ≡ 0), the ground state is even and symmetric decreasing on I_T.
*Proof.* k(u) is symmetric decreasing in |u|. The Almgren–Lieb inequality (CITED, Almgren–Lieb 1989, Thm 9.2)
gives ∬(F* (t) − F*(s))²k ≤ ∬(F(t) − F(s))²k for F ≥ 0, with F* the symmetric decreasing rearrangement on the
centred interval. With simplicity (R162_504 Thm 1), ψ = ψ*. ∎

**Lemma R′ (PROVED).** c_F(h) ≤ c_{F*}(h) fails for the comb. Take F = 1_{[0,ε]} + 1_{[h,h+ε]} with h > 2ε. Then
c_F(h) = ε and c_{F*}(h) = 0.

Consequences:
- The effective jump kernel k + Σv_nδ_{±log n} is not decreasing in |u|. Monotonicity of ψ_T, which is R-C (C2),
  loses its only tool at the first n with v_n > 0.
- This holds for ζ, deletion, and κ alike (F3 line: only v_n > 0 at some n is used).

(ii) **The PNT main term.**
- The comb equals its main term plus a fluctuation. The main term, Λ(n) → du, is J_main(u) ≈ e^{|u|/2}. This is
  **increasing** in |u| and log-convex, so it is the most anti-TP₂ piece. It is also exactly the rank-2 Tate/polar
  correction (R162_504 §5(i)).
- In W_T = a_T + 2AB it is removed, and the remaining comb Λ(n) − (main term) is sign-changing. So W is not even
  positivity preserving: no Perron, and a fortiori no TP.
- Λ*1 = log therefore converts the comb into two pieces, an anti-TP piece (removed by the pole) and a signed
  piece. Neither piece is TP.

(iii) **Causal combs and Schoenberg.**
- The one-sided combs of 1, Λ and log have Laplace transforms ζ, −ζ′/ζ and −ζ′.
- Schoenberg's theorem (CITED) says a PF_∞ density has reciprocal Laplace transform in the Laguerre–Pólya class,
  and in particular entire.
- 1/ζ, ζ/(−ζ′) and 1/(−ζ′) are not entire. In fact any sum of ≥ 2 Diracs already fails PF₂ (log-concavity).
- The convolution identity comb(log) = comb(Λ) ∗ comb(1) is a Cauchy–Binet product of two non-PF₂ factors, so it
  carries no TP. (Note: the TP form of RH in the corpus, 12-BIN-THREE, "Φ is PF", concerns the whole-line kernel
  of Ξ. It is not the window resolvent, and nothing here touches it.)

**Falsifier line.**
- Every NO-GO above (K1–K3, C1, R′) uses only J ≥ 0 with J ≢ 0 off the diagonal, or v_n > 0 at a single n.
- It therefore holds verbatim for ζ, deletion, κ and the comb-free model. It is **not** a weight-blind positive
  claim; it is a universal obstruction.
- Any future positive budget theorem must fail for deletion or κ at their contacts (0.58–0.60). If it does not use
  Λ beyond v_n ≥ 0, it is F3-dead, like R162_504.
- Positive statements Prop R and C are F3-blind infrastructure. Prop R fails for any nonzero comb.

## 5. What remains for R-A (open, with the exact missing inequality)

The only surviving lever is quantitative. For well-separated same-sign nodal intervals, W_{ij} ≤ ‖G_i‖₁‖G_j‖₁·sup J
on dist(D_i, D_j), which is ≍ e^{−dist/2} plus comb ridges. An oscillation budget would follow from the following
statement:

  (OB) Σ_{same sign, i≠j} (c_i − c_j)² W_{ij} ≤ Σ_{opposite sign} (c_i − c_j)² W_{ij} + 2Σ c_i²|⟨r, G_i⟩|,
  on an (M − 3)-dimensional c-space.

- Nothing in the corpus proves (OB).
- On the collapsing branch (S = 2, M = 3) it is empty, so it is consistent with R162_1501, but not decisive.
- (OB) involves Λ through the comb part of W_{ij}, at ridges |t − s| = log n between nodal intervals. It is the one
  place where a Λ-specific nodal statement could live.
- Falsifier for (OB): it must fail for the deletion contact vector (whose S is unknown; the R162_1501 float counts
  are under rerun and are treated as UNKNOWN here).

## 6. For R162_590

Add to §1c:
- "Karlin/Gantmacher–Krein Sturm route at resolvent level: NO-GO for every model and every shift (R162_1602 K1, K3;
  K2 whole-line PROVED, window PARTIAL). TP₂ ⟹ locality, so Perron and Karlin are incompatible for jump generators.
  The comb and Λ*1 = log do not restore it (main term is anti-TP, fluctuation is signed; Schoenberg)."
- "Variational Courant budget from positivity: NO-GO (Prop C/C1: test space of dimension 2)."
- "Rearrangement monotonicity of ψ_T (R-C C2): comb-free PROVED, comb breaks the tool (Lemma R′)."

Add to §2:
- (OB) as the single open quantitative residue of R-A, with the deletion falsifier.
