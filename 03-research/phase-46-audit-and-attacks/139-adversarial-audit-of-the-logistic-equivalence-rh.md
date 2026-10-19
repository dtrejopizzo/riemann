# Doc 139 — Adversarial audit of the logistic equivalence: RH ⟺ lim σ_loc^(k) = 0

**Program:** Riemann Hypothesis — Phase 46, "audit and attacks"
**Mandate:** destroy the repair of the bridge Theorem 2.13(b). Audited object: Doc 136
(Corollary 5.6 and its whole chain: Defs. 3.1–3.2, Props. 3.3, 3.5, Theorems 4.1–4.4, 5.4,
Prop. 5.5) and its published version in P47 (`thm:logistic`, `def:cell`, `def:loc-scheme`,
`prop:loc-welldef`, `prop:loc-logistic`, `thm:weyl-stab`–`thm:mesh`, `lem:tail`,
`lem:vandermonde`, `thm:realiz`, `prop:RHbranch`, `thm:main`, `rem:key`).
**Context input:** Doc 133 (logistic law, Thm. 2.10; Defs. 2.1–2.4), ERRATA.md
(Phase 38 audit). Backward-only citations. Nothing is fabricated; every error claim
comes with the computation or the configuration counterexample.

---

## 0. One-line verdict per branch

| Component | Verdict |
|---|---|
| **Logistic law** x_{k+1} = 2x_k(1−x_k) (algebraic core, D133 Thm. 2.10 / P47 `thm:logistic`) | **SURVIVES** — exact, re-derived below with no hidden hypotheses. Its *transplant* to σ_loc (Prop. 3.5 "verbatim" / `prop:loc-logistic`) contains a repairable normalization (radical) error: the closed-form formula is false as written, the 0 vs ½ dichotomy survives. |
| **Branch RH ⟹ lim σ_loc^(k) = 0** (D136 Prop. 5.5 / P47 `prop:RHbranch`) | **SURVIVES** — inputs verified against ERRATA, no circularity. |
| **Branch ¬RH ⟹ lim σ_loc^(k) = ½** (D136 Thm. 5.4 / P47 `thm:realiz`) | **DIES as a "theorem with complete proof"** — two gaps in the proof: (GAP-A) Step 3 claims θ(M,w) → 0 with constants C_M, e^{a₀(M,w)}, b₀(M) that depend on M and whose uniformity is not only unproven but **false** for every fixed-support bump family (Lemma 139.1 below); (GAP-B) Step 1 does not annihilate the **resonant pairs** with both members in S and σ ∈ {σ₀, σ₀′} distinct from the target orbit, which exist for legitimate ¬RH configurations and contribute terms of uncontrolled sign. The **statement** is not refuted: GAP-B is repairable with Vandermonde in the τ coordinate, and GAP-A is probably repairable by importing the classical exponential-dominance mechanism of Weil's criterion (sketch in §3.5), but the honest status today is **CONDITIONAL/OPEN**, not a theorem. |

**Consequence for the equivalence (D136 Cor. 5.6 / P47 `thm:main`):** it is left with one
proved branch and one branch with a gap — exactly the asymmetric status Doc 133 had before
the repair. The repair truly fixed the normalization error of 2.13(b)
(this is confirmed: the localized architecture is sound and negativity does NOT escape to
cells of growing dimension), but it introduced a second error in a different coordinate — the
**uniformity in M of the Paley–Wiener constants** — exactly as one would anticipate
tends to happen in repairs.

---

## 1. Re-derivation of the logistic law (protocol 1)

### 1.1. The tensor identity, from scratch

Let Q̄ be **nondegenerate** hermitian on V, dim V = n̄ < ∞, signature (p, q). By Sylvester's
law of inertia there is a Q̄-orthogonal basis {e_i} with Q̄(e_i, e_i) = ε_i ∈ {±1},
p positive and q negative. For Q̄₁ ⊗ Q̄₂ on V₁ ⊗ V₂, the basis {e_i ⊗ f_j} is
orthogonal with signs ε_i^{(1)}ε_j^{(2)}; no diagonal entry is 0 (no isotropic
vectors in the basis) and the product form is nondegenerate (the Gram determinant
multiplies: det(G₁⊗G₂) = (det G₁)^{n₂}(det G₂)^{n₁} ≠ 0). By Sylvester,
neg.ind = number of −1 signs = p₁q₂ + q₁p₂. Applied to the doubling
Q̄^{⊗2^{k+1}} = Q̄^{⊗2^k} ⊗ Q̄^{⊗2^k}, with (P_k, K_k):

$$K_{k+1} = 2P_kK_k, \qquad P_{k+1} = P_k^2 + K_k^2,$$

and dividing by n̄^{2^{k+1}}: x_{k+1} = 2x_k(1−x_k); 1−2x_{k+1} = (1−2x_k)², whence
1−2x_k = (1−2x_0)^{2^k}. **Verified: the recursion is an exact rational identity.**

### 1.2. Is there a no-interaction hypothesis between copies assumed without proof?

**No.** The tensor product of forms is defined orthogonally by construction; the
"no-interaction" is not a hypothesis on the copies but the content of the definition
of Q⊗Q. The two real hypotheses, both satisfied and stated, are:

1. **Nondegeneracy** (without it Sylvester does not give neg.ind by sign counting): D136
   ensures it by passing to the quotient by the radical (Def. 3.2, "nondegenerate reduced
   form Q̄_N"). Correct in itself — but see §2.3: the quotient changes the denominator and
   breaks the formula of Prop. 3.5.
2. **Finite dimension per coordinate N**: satisfied (bounded cells).

The passage to standard parts is legitimate: st is a ring homomorphism on the bounded ones,
the polynomial identity is used a finite (standard) number of times per k, and each
x_k(N) ∈ [0,1]. The known erratum of Doc 106 (Cor. 3.2 requires p₁,p₂ ≥ 1,
ERRATA.md §"tensor index") **does not affect this**: identity (A), used here, is
declared INTACT in the ERRATA and is moreover re-proved self-containedly in P47
(`lem:whitney`).

**Scope warning (not an error):** the tower is a *formal* amplifier — Q̄^{⊗2^k}
is not the Weil form of any duplicated test space. Neither D136 nor P47 claims
otherwise; the arithmetic content enters only through x_0(N). Correct as stated.

### 1.3. The {0, ½} dichotomy

For σ⁰ ∈ (0,1): |1−2σ⁰| < 1 and the closed form gives ½. For σ⁰ ∈ {0,1}: 0. The
boundary case σ⁰ = 1 is excluded in the localized version by the padding (x_0 ≤ ½). All
correct **provided the base of the tower is the correct quantity** — see §2.3.

**Verdict for protocol 1: the logistic law SURVIVES as exact algebra.**

---

## 2. Audit of σ_loc: well-definedness, monotonicity, canonicity (protocol 2)

### 2.1. Well-definedness and grid monotonicity — VERIFIED

- **Inclusion 𝒢_N ⊆ 𝒢_{N+1}:** a profile p = (D,w,M,b,c,c′) ∈ 𝒢_N has D,M ≤ N ≤ N+1;
  w,b ∈ {2^{−j}: j ≤ N} ⊆ {2^{−j}: j ≤ N+1}; centers in (bℤ)²∩[−2^N,2^N]² ⊆
  (bℤ)²∩[−2^{N+1},2^{N+1}]². All restrictions relax: **inclusion verified**.
  Since Q̃_p and dim Ṽ_p depend only on p (not on N), x_0(N) = max over a growing
  family of finite sets is **nondecreasing**. ✔
- **The correct partial order:** the monotonicity used is grid growth (max
  over more cells), not Cauchy interlacing between subspaces. There is no inequality
  direction to check against Cauchy; where an interlacing is actually used (Theorem 4.2 =
  stability under rank), the three-line proof with N ∩ ker E is correct and in the
  correct direction (verified line by line). ✔
- **Canonicity in 𝒰:** a bounded monotone sequence converges; st of a convergent = limit
  for every 𝒰. Obs. 5.7 is correct for σ_loc. ✔
- **Bound x_0(N) ≤ ½:** neg.ind(Q̃_p) ≤ dim V_p ≤ (D+1)² and dim Ṽ_p = dim V_p + (D+1)²,
  so the quotient ≤ dim V_p/(dim V_p + (D+1)²) ≤ ½. ✔ (Holds even if the
  h_{g_a,φ_b} are linearly dependent and dim V_p < (D+1)².)

Two observations of candor, not fatal:

- **(O-1) Design canonicity:** σ_loc is 𝒰-canonical but NOT design-canonical: it depends
  on the bump family B^{(M)}_w "chosen once and for all" and on the grid geometry. The
  equivalence of Cor. 5.6 holds for *each* admissible design, which suffices; but the
  paper should not suggest that σ_loc is an invariant of ζ — it is an invariant of the pair
  (ζ, design).
- **(O-2) "neg.ind is computed exactly":** the Gram entries are computable real
  numbers (series over primes), not rationals; Lagrange–Sylvester is exact only
  over exact arithmetic. What is true and sufficient: "neg.ind(Q̃_p) ≥ 1" is
  **semidecidable** by interval arithmetic (a strictly negative eigenvalue is
  certified with finite precision), which is exactly what the reading of §6.2 uses. The
  phrase "is computed exactly" (Prop. 3.3(a) / `prop:loc-welldef`(a)) is a
  wording overstatement.

### 2.2. ⚠ E-139.1: the incompatible double definition of x_0(N) (the radical bug)

Def. 3.2 of D136 (and P47 `def:loc-scheme`) defines x_0(N) **twice, in an
incompatible way**:

1. In the display: x_0(N) := max_p neg.ind(Q̃_p)/**dim Ṽ_p**.
2. In the tower: "x_k(N) := neg.ind(Q̄_N^{⊗2^k})/**n̄_N**^{2^k}", which at k = 0 is
   neg.ind(Q̄_N)/n̄_N with n̄_N = dim Ṽ_{p*} − dim rad(Q̃_{p*}).

Since rad(Q̃_p) = rad(Q₂|_{V_p}) ⊕ 0 (the Id padding is nondegenerate and orthogonal to
the block), one has n̄_N = dim V_{p*} − r_N + (D+1)² with r_N := dim rad ∈ [0, dim V_{p*}].
If r_N > 0 — and nothing excludes it: under RH the compressed Gram can be degenerate, and
under ¬RH as well — the two definitions differ. Exact consequences:

- **The formula of Prop. 3.5 / `prop:loc-logistic` is FALSE as written:**
  σ_loc^(k) = ½(1 − (1−2σ_loc)^{2^k}) requires the base of the tower to be σ_loc, and the
  real base is σ_base := st([neg.ind/n̄_N]), which can differ from σ_loc.
- **The 𝒰-independence of σ_loc^(k) for k ≥ 1 is left unproven:** the tower
  sequence is not monotone in N (the argument of Prop. 3.3(c) does not cover it), so
  the intermediate values σ_loc^(k) may depend on 𝒰.

**Why the dichotomy survives (repair this audit provides, with proof):**
the ratio of denominators is bounded: dim Ṽ_p / n̄_N ∈ [1, 2] (because
n̄_N ≥ (D+1)² = ½ dim Ṽ_p). Since st is multiplicative on bounded quantities,

$$\sigma_{loc} \;\le\; \sigma_{base} \;\le\; 2\,\sigma_{loc},$$

for every 𝒰. Moreover x_base(N) = (dim V−r)/((dim V−r)+(D+1)²)-bounded ≤ ½ < 1, so
σ_base ∈ [0, ½] and the case σ⁰ = 1 remains excluded. Hence: σ_loc = 0 ⟺ σ_base = 0 ⟹
tower ≡ 0; and σ_loc > 0 ⟹ σ_base ∈ (0, ½] ⟹ tower → ½, **for every 𝒰**. The final
dichotomy lim_k σ_loc^(k) ∈ {0, ½} with 0 ⟺ σ_loc = 0 is correct; what is false is the
closed-form formula *in terms of σ_loc* and the canonicity of the intermediate levels.

**Repaired statement of Prop. 3.5:** "For every 𝒰 and every standard k,
σ_loc^(k) = ½(1 − (1−2σ_base^𝒰)^{2^k}) with σ_base^𝒰 ∈ [σ_loc, 2σ_loc] ∩ [0,½]; in
particular lim_k σ_loc^(k) = 0 if σ_loc = 0 and = ½ if σ_loc > 0, independently
of 𝒰." (Design alternative: define x_0(N) directly as neg.ind/n̄ of the winning
cell, restoring the literal formula; then the monotonicity in
N must be re-verified, which is no longer free because the maximizer of neg.ind/dim Ṽ is not
that of neg.ind/n̄.)

**Verdict for protocol 2: σ_loc is well-defined and 𝒰-canonical; the "verbatim logistic
law" contains a real error (E-139.1) repairable without losing the dichotomy.**

---

## 3. The RH branch (protocol 3) — SURVIVES

The complete chain of Prop. 5.5 / `prop:RHbranch`:

1. **Under RH, the spectral side (1.1) is diagonal:** every pair (ρ₁,ρ₂) with both
   zeros on-line is ι-fixed (ι(ρ) = 1−ρ̄ = ρ if Re ρ = ½), so Q₂(h,h) = Σ|ĥ(P)|² ≥ 0 over
   the span. Inputs: the spectral representation with absolute convergence
   [D107 Lemmas 2.2(b), 5.2(b)] and the ι symmetry of the zero multiset (functional
   equation, unconditional). Cited via D108 Prop. 2.2 — which is an immediate
   consequence of D107's spectral side, not an additional input. *Hygiene note:* D136's
   summary says "inputs D107"; the literal citation of the RH branch is D108 Prop. 2.2.
   Harmless, but should be unified.
2. **The cells live in the span:** B_w·(monomials) ∈ class by closure under x∂ₓ
   [D107]. ✔
3. **Compression and padding:** every compression of a ≥ 0 form is ≥ 0; ⊕ Id is ≥ 0;
   neg.ind = 0 on every cell; x_0(N) ≡ 0; σ_loc = 0; the tower (with or without bug
   E-139.1) is identically 0. ✔

**Cross-check with ERRATA.md (Phase 38):** the refuted objects are W_λ ≥ 0 (Doc 63 §7.1),
Doc 76, Doc 103 Thms 2.2/3.1, P39 direction ⟸, P41 Thm 3.2, P43 ledger L2, Doc 106
Cor. 3.2. **None** appears in the chain of the RH branch: D107 and D108 Prop. 2.2 are not
touched by the ERRATA; the tensor identity used is declared intact and moreover
re-proved in P47. **No circularity:** RH is used exactly once (diagonality), no
RH-equivalent uniform bound is used.

**Verdict for protocol 3: RH branch SURVIVES without reservations.**

---

## 4. The attack on the repaired step: Theorem 5.4 / `thm:realiz` (protocol 4)

### 4.1. What the repair DID achieve (and this audit confirms)

Before the findings, fairness: the main attack suggested — "does
negativity escape to cells of growing dimension, repeating the 2.13(b) error in
a different coordinate?" — **fails against the architecture**. The minimal-defect
local configuration (S, Z_σ, q, D₀ = q², μ₀, L_{p*}) is fixed by ζ, not by N: these are
standard constants. The witness cell has a fixed profile and enters 𝒢_N for every N ≥ N₀;
the dimension per cell never grows. The density dilution of Theorem 2.5 does not apply
(its hypothesis n_N → ∞ per cell deliberately fails). The conceptual key of Obs. 5.1 — the
test-accessibility constrains the *specification* of the space, not the *witness vector* — is
correct and is genuine mathematics: neg.ind of the compressed Gram is a property of
the Gram, and the witness is an object of the proof. The perturbation package
(Theorems 4.1–4.3) is verified line by line and is sound (with a constant slip
in 4.4, E-139.5 below). **The 2.13(b) error does not repeat in the dimensional
coordinate.** It repeats elsewhere.

### 4.2. GAP-A (fatal for the "complete proof" status): the Step 3 constant budget

Step 3 needs |(c)| = |tail in Ω₁| ≤ m₀²/4, and obtains it as follows: "Lemma 5.2 with
r = 1 […] gives |(c)| ≤ C₃(profile, C₁, C₂)·θ(M,w), where θ(M,w) → 0 as M → ∞ with w
fixed (the bound of Lemma 5.2 decays as M−D−4)". This is **logically invalid**: "profile"
includes M, so C₃ = C₃(M); the limit M → ∞ with C₃ treated as a constant is not
justified. What the bound of Lemma 5.2 actually gives at r = 1 is

$$|(c)| \;\le\; \underbrace{C_1^2C_2^2\,C_M^4\,e^{4a_0(M,w)\cdot\beta}\,b_0(M)^{-\text{(pow.)}}}_{\text{grows with } M}\cdot\;C^*(M{-}D)\,(\log(2{+}|\gamma_0|))^2\cdot\;2^{-(M-D-4)},$$

(β ≤ 1 the reach in Re within the strip; C₁ = Vandermonde constant, which depends
on b₀(M) = min|B^{(M)}(z_i − ic*)|, also M-dependent). The decisive question:
can the product tend to 0? The answer, in closed form:

**Lemma 139.1 (Paley–Wiener rigidity; the claim θ → 0 is false for fixed support).**
*Let B be the transform of a nonzero g ∈ C_c^∞ with logarithmic support
⊆ [−a₀, a₀] (a₀ fixed), and let C_M be the optimal constants in
|B(t)| ≤ C_M(1+|t|/w)^{−M} (t ∈ ℝ). Then for every A > 1 there exists M_A such that
C_M > A^M for every M ≥ M_A. Consequently C_M^4·2^{−M} → ∞.*

*Proof.* If C_M ≤ A^M for infinitely many M, then for |t| > Aw one would have
|B(t)| ≤ (Aw/|t|)^M → 0 along those M, so B(t) = 0 for every |t| > Aw. But B
is entire (Paley–Wiener, compact support) and not identically zero: its real zeros are
discrete — contradiction. ∎

Therefore, **with any fixed bump, the bound of Step 3 diverges in M**. And with a
family B^{(M)} (a different bump per M, growing support a₀(M))? The balance also does not
close with standard constructions. With powers of sinc (B = (sinc(a₀t/M))^M, type
a₀, C_M = (M/(a₀w))^M) the factor per pair at r = 1 is of order

$$C_M^2\,e^{2a_0}\,(1+1/w)^{-2M} \;\asymp\; \Big(\frac{M}{a_0}\Big)^{2M} e^{2a_0},$$

whose minimum over a₀ (at a₀ = M) is e^{2M} → ∞. The strip factor e^{c·a₀} —
unavoidable because the tail zeros can have Re up to the strip's edges and
|B(x+it)| ≤ B-at-Re grows like e^{a₀|x−½|} for g ≥ 0 — always defeats the polynomial
decay in Im at fixed distance r = 1. Taking w → 0 does not help: the required support
scales like M/w and e^{M/(2w)} beats (1/w)^{M}. No family with the required uniformities
is exhibited in the document, and the natural ones do not have them.

**Precise scope of the finding:** this does NOT refute Theorem 5.4 (the bound is an upper
bound; the true tail could be small, and the statement is probably true — see §4.4).
It refutes the *proof*: Step 3, as written, does not establish |(c)| ≤ m₀²/4, and
the final sentence of Lemma 5.2 ("In particular Σ_tail(r) → 0 as M → ∞ at fixed r") is
false in its instantiation because it forgets that C_g = C_g(M). The same error is in P47
(`lem:tail` "In particular it →0 as M→∞ with r fixed" and `thm:realiz` Step 3).

**Structural diagnosis:** this is the same *genre* of error that killed W_λ ≥ 0 and
2.13(b): a quantity treated as a constant that is actually a function of the parameter
being sent to infinity. In 2.13(b) it was n_W (count) confused with dim V_W
(dimension); here it is C₃("profile") treated as a constant while the profile contains M.

### 4.3. GAP-B (repairable, but real): the un-annihilated resonant pairs

Step 3(b) claims: "pairs with both members in S, distinct from the target orbit: their
σ ∈ Z_σ, where ĝ_v = 0: contribute 0". False in general, because Z_σ was defined in Step 1
**excluding** σ₀ and σ₀′: a non-target pair with both members in S and σ ∈ {σ₀, σ₀′} is
not annihilated by ĝ_v (which equals ±1 there) nor is it in the tail Ω₁ (it can have
|Im σ − γ₀| = 0 and |Im τ| arbitrarily small).

**Configuration activating the gap (legitimate under ¬RH, which is a hypothesis on ζ with
arbitrary configuration):** besides the minimal zero ρ⁰ = ½+δ₀+iγ₀, an off zero
ρ₁ = ½+2δ₀+i(γ₀+ε) and an on-line zero ρ₂ = ½+i(γ₀−ε), with ε small. Then
σ(ρ₁,ρ₂) = ½+δ₀+iγ₀ = σ₀ exactly, both members are in S, the pair is not the target
orbit, and its contribution is

$$2\,\mathrm{Re}\big[\hat h(P)\overline{\hat h(\iota P)}\big] = -\tfrac12\,\mathrm{Re}\big[\hat\varphi_v(\delta_0+i\varepsilon)\,\overline{\hat\varphi_v(-\delta_0+i\varepsilon)}\big],$$

of sign and size **uncontrolled** by the construction (φ̂_v is prescribed only at
τ = 0; at τ = δ₀+iε it is O(1)). Summed with adversarial multiplicities it can exceed
−m₀²/2 and destroy the witness's negativity. Note that in the pure-defect case of
a single quadruple there are no offenders (verified: no pair from the quadruple plus on-line
produces σ ∈ {σ₀, σ₀′} except the target), which explains why the error was not seen in the
toy case — again the pattern "proved in the toy, cited in general".

**Repair (rigorous, this audit validates it):** the offenders have τ ≠ 0 (τ = 0 and
σ = σ₀ force ρ₁ = ρ₂ = ρ⁰, the target orbit) and form a finite set
Z_τ ⊂ ℂ∖{0} fixed by the configuration. It suffices to prescribe on the τ side, via the same
Lemma 5.3 (Vandermonde with bump, already available), φ̂_v = 0 on Z_τ and φ̂_v(0) = 1,
raising D to max(|Z_σ|+1, |Z_τ|) and D₀ accordingly (standard follow-through). With this,
Step 3(b) becomes exhaustive again: σ ∈ Z_σ dies by ĝ_v, σ ∈ {σ₀,σ₀′} with τ ∈ Z_τ
dies by φ̂_v, and the image ι adds no new cases (σ(ιP) = 1−σ̄ swaps σ₀ ↔ σ₀′, already
covered). GAP-B is thus reduced to an erratum-with-patch; **but the patch enlarges D
and therefore worsens the GAP-A budget** (C₁ and the polynomial degree grow):
the two gaps are not independent and the repair must close them together.

### 4.4. Is the statement true? The honest repair route

The statement "¬RH ⟹ there exists a bounded cell with neg.ind ≥ 1" is the folded analogue
of the classical sense of Weil's criterion ("¬RH ⟹ ∃f ∈ C_c^∞ with Q(f) < 0"), which is a
classical theorem, and whose proof mechanism is **different** from D136's: the
main term is not normalized to size 1 while trying to make the tail small in absolute
terms; instead the off-zero term is let to GROW like e^{2δ·a₀} with the support a₀ → ∞
(choosing the off zero with near-extremal real part, not the one of minimal height), while
the on-line terms grow polynomially: dominance is exponential and the
M-dependent constants are absorbed by e^{2δa₀}. Transplanting that mechanism to Q₂ with
the phase control (1,−1) of the hyperbolic plane, and verifying that the resulting test enters
*some* cell of the grid with a standard profile (the required support a₀ is finite once the
configuration is fixed), is the real content that is missing. This audit does **not**
execute it (that would be fabricating a new proof in an audit document); it is logged as
**Problem 139.A**: re-prove Theorem 5.4 with an explicit constant budget,
either by exponential dominance or by a bump family with the uniformities of §4.2
proved. While 139.A is open, the ¬RH branch is CONDITIONAL.

### 4.5. Note on Theorem 4.4 (mesh constant)

Minor but exact: with b ≤ μ/(2√2·L), the proof's bound gives
‖G(p)−G(p*)‖ ≤ L·b√2·2 = 2√2·L·b ≤ μ, **not** ≤ μ/2 as claimed; and Theorem 4.1
requires strict inequality < μ. Trivial correction: b ≤ μ/(4√2·L). Nothing else is
affected (E-139.5).

**Verdict for protocol 4: the ¬RH branch DIES as a theorem (GAP-A + GAP-B); the statement
remains open-repairable, not refuted; the localization architecture is confirmed.**

---

## 5. Π₁ effectiveness (protocol 5) — VERIFIED

- D136 §6.2(5) and P47 §`sec:candid`(a) explicitly state: σ_loc = 0 is Π₁ over
  (x_0(N))_N, "exactly as unverifiable as ever"; N₀ and D₀ "are not effective from
  m̄ or from anything". **No corollary claims effectiveness.** ✔
- The only wording tension: Theorem 4.4 / `thm:mesh` says "N₀ **computable** from
  (μ, L, position)" — computable from inputs not effectively knowable. It is
  consistent (the declared status of Thm. 5.4 clarifies it), but the word "computable"
  in the lemma's statement can mislead a reader of the paper; suggestion:
  "explicit in terms of (μ, L, position)". (E-139.6, cosmetic.)
- The semidecidability of ¬RH by Grams ("run the grid until a negative eigenvalue is
  certified") survives with the precision of O-2 (§2.1): interval certification, not
  "exact arithmetic". **Important:** this semidecidability depends on the ¬RH branch
  (Theorem 5.4) — with GAP-A open, "¬RH ⟹ the machine stops" is also conditional.

---

## 6. Errata and consequences for P47

### 6.1. List of errata (for ERRATA.md and for the .tex)

| # | Location | Error | Severity / action |
|---|---|---|---|
| **E-139.1** | D136 Def. 3.2 + Prop. 3.5; P47 `def:loc-scheme` + `prop:loc-logistic` | x_0(N) defined twice incompatibly (denominator dim Ṽ_p vs n̄_N after quotienting by the radical); the closed formula σ_loc^(k) = ½(1−(1−2σ_loc)^{2^k}) is false if the winning Gram is degenerate; the 𝒰-independence of σ_loc^(k), k ≥ 1, unproven | MEDIUM. The 0 vs ½ dichotomy survives via σ_base ∈ [σ_loc, 2σ_loc] ∩ [0,½] (§2.2, proof here). Rewrite Prop. 3.5/`prop:loc-logistic` with the repaired statement. |
| **E-139.2** | D136 Thm. 5.4 Step 3 + Lemma 5.2 (final sentence); P47 `thm:realiz` Step 3 + `lem:tail` | "θ(M,w) → 0 as M → ∞" with C₃ = C₃(M): invalid; **false** for fixed-support families (Lemma 139.1); uniformity in M of C_M, e^{a₀(M,w)}, b₀(M), C₁(M) never established | **CRITICAL**. The ¬RH branch drops from "theorem over cited inputs" to CONDITIONAL (Problem 139.A). |
| **E-139.3** | D136 Thm. 5.4 Steps 1/3(b); P47 `thm:realiz` Steps 1/3(b) | Resonant pairs (both in S, σ ∈ {σ₀,σ₀′}, ≠ target orbit) not annihilated; exist under general ¬RH; uncontrolled sign | HIGH but repairable: add Vandermonde annihilation in τ over Z_τ (§4.3); D and D₀ grow (standard); interacts with E-139.2. |
| **E-139.4** | D136 Prop. 3.3(a); P47 `prop:loc-welldef`(a) | "neg.ind is computed exactly": the entries are computable reals, not rationals; the correct statement is semidecidability/interval certification | LOW. Reword. |
| **E-139.5** | D136 Thm. 4.4; P47 `thm:mesh` | 2√2·L·b ≤ μ, not μ/2; Thm. 4.1 requires strict < μ | TRIVIAL: b ≤ μ/(4√2·L). |
| **E-139.6** | P47 `thm:mesh`, `rem:collapse` | (i) "computable N₀" misleading (§5); (ii) `rem:collapse` attributes the global collapse to \cite{P40}: the collapse is Theorem 2.5 of D136 — verify that P40 actually contains it or fix the citation | LOW. Hygiene. |

### 6.2. Consequences for the text of P47

1. **Abstract and `thm:main`:** the sentence "with *both* branches theorems over cited inputs"
   and "realizability under ¬RH is now a theorem rather than a hypothesis" must be
   withdrawn or conditioned while 139.A is open. Honest wording: "the RH
   branch is a theorem; the ¬RH branch is proved modulo a quantitative uniformity of
   Paley–Wiener constants in the witness construction (stated as Problem 139.A), which
   replaces the former realizability hypothesis by a strictly narrower, purely analytic
   gap". Same for §`sec:candid`(c) item 4 ("realizability is now a theorem") and for
   `rem:key` (the phrase "dissolves it" is correct for Hypothesis D *as such* — the
   T → ∞ regime did dissolve — but the caveat did not disappear: it transmuted into the
   uniformity of constants).
2. **`prop:loc-logistic`:** replace with the repaired statement of §2.2 (dichotomy with
   σ_base; canonicity only of the limit).
3. **`lem:tail`:** delete the final sentence "In particular it →0 as M→∞ with r fixed" or
   condition it on C_g, C_φ independent of M (which is exactly what is not available).
4. **`thm:mesh`:** fix the constant (E-139.5) and the word "computable" (E-139.6).
5. **What does NOT change:** the Weil–Toeplitz/trichotomy section (independent, not
   audited here except for citation cross-checking), `thm:logistic`, `prop:RHbranch`,
   `thm:weyl-stab`, `thm:rank-stab`, `thm:lipschitz`, `lem:vandermonde`, Prop. 3.3
   (a,b,c) with the E-139.4 reformulation, and all of §2 of D136 (the global collapse and
   the refutation of 2.13(b), which this audit confirms as correct).

### 6.3. Final status of the logistic criterion

$$\mathrm{RH} \iff \lim_k \sigma_{loc}^{(k)} = 0:\qquad
\text{branch } \Rightarrow \text{ (i.e. RH} \Rightarrow 0\text{): THEOREM};\qquad
\text{branch } \Leftarrow \text{ (¬RH} \Rightarrow \tfrac12\text{): OPEN (139.A)}.$$

The repair of Doc 136 fixed the normalization error of Doc 133 and introduced an
architecture (localization + grid + monotonicity) that this audit confirms is sound; but
the "equivalence with both branches as theorems" status announced in D136 §0.3, §6.1(2),
§7 and in P47's abstract **is not sustainable today**. The program's history repeated
with precision: the repair of a refuted theorem contained the second error, and it was
where it always is — in a constant that was not constant.

---

## References

**Internal (backward-only):** Doc 136 (all); Doc 133 (Defs. 2.1–2.4, Thm. 2.10,
bridge Theorem 2.13, §5.2); Doc 108 (Prop. 2.2); Doc 107 (Lemmas 2.2(b), 5.2(b),
Thm. 5.5, Prop. 6.1, x∂ₓ closure); Doc 106 (tensor identity); P47 (main.tex,
06-papers/ERRATA.md (Phase 38); P43 (value autonomy).

**Literature:** R. Paley, N. Wiener (compact-support transforms: a nonzero entire
function has discrete real zeros — used in Lemma 139.1; standard, cf.
Hörmander I, Thm. 7.3.1); A. Weil, Comm. Sém. Math. Lund (1952) (positivity
criterion; the sense ¬RH ⟹ ∃f: Q(f)<0 and its exponential-dominance mechanism,
cited in §4.4 as a repair route, not as a used result); F. R. Gantmacher,
Vol. 2, Ch. X (Sylvester/inertia, §1.1); R. Bhatia, GTM 169 (Weyl/Courant–Fischer,
via D136 §4).

*End of Doc 139.*
