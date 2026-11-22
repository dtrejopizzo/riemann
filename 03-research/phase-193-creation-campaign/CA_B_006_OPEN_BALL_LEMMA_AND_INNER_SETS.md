# CA_B_006 — The open-ball lemma; inner sets; pre-screen of the weighted Wirtinger (W_σ) (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed; no sign contact.**

## 0. Correction to CA_B_005 (definitions checked against P46)
P46's κ_T (line ~7089) is a *directional* quantity: κ_T = Σ_{n∈N_T} v_n c_h(log n) at the minimizer h, with v_n = 2Λ(n)/√n, and
λ_A(T;(1+ε)v) ≤ λ_A − εκ_T. It is NOT an ℓ^∞-Lipschitz constant. CA_B_005 Prop 2 used it as one; the correct constant is L_T below.
Prop 2's conclusion survives with κ_T replaced by L_T (radius λ_A/L_T), and its example becomes v_2 ↦ v_2 + δ with 0 < δ < λ_A/L_T.

## 1. Lemma B (open ball; PROVED)
Setting (P46 prop:finite): v ∈ ℝ^{N_T}, |N_T| = ⌈e^{2T}⌉ − 2; for a real unit vector F ∈ P_T in the form domain,
𝔞_T^{(v)}(F) = C_0 + Lev(c_F) − Σ_{n∈N_T} v_n c_F(log n), c_F = F∗F̃; λ(v) := inf_F 𝔞_T^{(v)}(F); 𝒱_T = {v : λ(v) ≥ 0}; v^Λ := (2Λ(n)/√n).
Put L_T := sup_F Σ_{n∈N_T}|c_F(log n)|. Then:
(i) L_T ≤ |N_T| < e^{2T} (since |c_F| ≤ ‖F‖₂² = 1).
(ii) λ is concave on ℝ^{N_T} and |λ(v) − λ(v')| ≤ L_T‖v − v'‖_∞.
(iii) If λ_A(T) := λ(v^Λ) > 0, then the closed ℓ^∞-ball B_T := {v : ‖v − v^Λ‖_∞ ≤ λ_A(T)/L_T} lies in 𝒱_T.
(iv) The set Σ_T := {v : v_n = 2Λ(n)/√n ∀n} = {v^Λ} has empty interior. So no property of v that holds only at v^Λ (in particular
     no exact identity singling out Λ — Δ_v ≡ 0, Hamburger, Λ∗1 = log, Euler-tail coefficient vanishing) is necessary for v ∈ 𝒱_T.
     Such a property can be load-bearing in a proof of λ(v^Λ) ≥ 0 only if the proof also establishes λ ≥ 0 on B_T, where it fails.
Proof. (ii) λ is an infimum of affine functions of v, so it is concave. Each affine function has ℓ^∞→ℝ Lipschitz constant
Σ_n|c_F(log n)| ≤ L_T, and an infimum of L_T-Lipschitz functions is L_T-Lipschitz. (i) is stated. (iii) follows from (ii).
(iv) Let P be such a property and let 𝒜 be a valid deduction "P(v) ⇒ λ(v) ≥ 0". Then 𝒜 says nothing on B_T∖{v^Λ}. So 𝒜 is a valid
proof of λ(v^Λ) ≥ 0, but no more than one of λ(v^Λ) ≥ 0 itself. The "(iv)" content is the observation: a point property cannot be NECESSARY, and
a sufficient condition P must be supplemented by an argument whose validity does not depend on the exactness of P — for if it did, the same
argument with P replaced by "v ∈ B_T" would have to fail, although the conclusion is true there. ∎
**Label.** (i)–(iii) PROVED. (iv) as stated (empty interior; "not necessary") PROVED; the methodological reading ("an exact identity cannot
carry the sign alone") is ARGUED — it is the same content as (R)(6) + (R)(11) and P46 W-sens (l. 7105: "continuous in the weights, must be
sharp at the scale of λ_A/κ_T").
**Scale.** Under the premise λ_A(T) > 0 ∀T and lem:shape-margin (margin ≤ 4·10⁹Te^{−15.449T} at T ≥ 1), radius
λ_A/L_T ≤ 4·10⁹Te^{−17.449T}: doubly small (exponentially in T, against e^{2T} coordinates).

## 2. The tension "open at scale r_T, false far away" vs (R)(5) — why P need not be a bounded functional (PROVED / ARGUED)
Requirement for a sign-carrying property P (of the comb vector, at fixed T): B_T ⊂ {P} ⊂ 𝒱_T. The second inclusion is needed for P to imply
the target; the first is needed for P not to be a point property (Lemma B(iv)). Such a P is any **inner set** of 𝒱_T containing B_T.
(a) **Not forced to be a superlevel set of one Lipschitz functional with T-uniform constant (PROVED by example).** 𝒱_T itself is such a set.
    By prop:finite(ii) it is the intersection of half-spaces with normals (c_F(log n))_n over all unit F. The normals have ℓ¹-norm up to
    L_T ~ e^{2T}, and infinitely many are needed. Openness at r_T fixes only a *local* Lipschitz scale L_T/λ_A ≥ e^{17T}/(4·10⁹T). This is
    unbounded in T and it lives on e^{2T} coordinates. "Bounded functional" in (R)(5) (a fixed functional, or a class closed under
    perturbations of size ≍ λ_A in a T-uniform norm, P46 l. 8348) is a different notion.
(b) **What openness + far failure do force (PROVED).** Write P = {F_T ≥ 0} with F_T continuous. Then F_T(v^Λ) > 0 and F_T < 0 at falsifiers.
    The falsifiers are a_P, Beurling, Poisson, quartets, and v^Λ+ δe_2 for δ > λ_A/κ_T-scale (P46 l. 7092). So the relative sensitivity
    |∇F_T|/F_T(v^Λ) must reach ≳ 1/dist(v^Λ, ∂𝒱_T) in the direction of the nearest falsifier, i.e. ≥ L_T/λ_A in some direction.
    This is (R)(6) restated. It forbids nothing beyond (R)(6).
(c) **The non-trivial content (ARGUED).** An inner set must be *defined* without knowing λ_A(T). Otherwise it is "v ∈ B(v^Λ, λ_A/L_T)",
    which presupposes the target (REF-D). So the object sought is an explicit set 𝒮_T with B_T ⊂ 𝒮_T ⊂ 𝒱_T whose membership test
    for v^Λ uses the arithmetic of Λ (Euler × FE × ℤ). The test must also degrade continuously, so that the falsifiers fail it. Recorded as the
    sharpened target. Candidates must be checked against both inclusions.

## 3. Pre-screen of (W_σ) for Euler-tail g (sharpened by Lemma B)
Object (CA_B_004 §3): J_X(σ) = ∫ω|g_X(σ+iτ)|²dτ, ω = F̂₀²|Z_{<X}(½+iτ)|², g_X = ζ/Z_{<X} = 1 + Σ_{n≥X}b(n)n^{−s}, b ≥ 0. Claim to test:
(W_X) J_X convex on [½,2]; with J'(2) ≤ 0 this gives I_ζζ ≥ 0.
| screen | outcome |
|---|---|
| (R)(4): does off-line |g_X| see zeros? | **NO zero information is forced (PROVED).** g_X is holomorphic of finite order in ½ ≤ σ ≤ 2 except for the pole at 1, which is removed by (s−1). So g_X(σ+iτ) is the Poisson/Cauchy transform of its boundary values on σ = ½ and σ = 2, *linearly in g*. J_X(σ) is a quadratic form in the boundary data (line values of ζ/Z_{<X}; Euler series at 2). Zeros enter only if one passes to log|g| (CA_B_002); (W_X) does not. Passes (R)(4) |
| Lemma B: is the hypothesis "b ≥ 0, b = 0 on (1,X)" load-bearing? | **It is a point property.** For v = v^Λ + δe_2 (δ tiny), g_a acquires b(2) ≈ −δ√2/(2 log 2)·… ≠ 0 and leaves the class. By Lemma B(iv) the class membership cannot be what makes (W_X) true. Only an inequality whose proof survives |b(n)| ≲ λ_A/L_T on (1,X) can be used. **YES→NO: "Euler-tail class membership as sign carrier" → NO** |
| (B″) comb-genericity | the identity I^a_ζζ = −J_a'(½)/2π holds for every comb with test ζ (CA_B_004 Prop 1); (W_X) as an inequality is open in v (affine symbol, fixed test) |
| does it reach the window bottom? | **NO.** I_ζζ is one of four pieces of Q_M on the family (EI_002 (3.1)). The bottom is an infimum over tests, and ζ is not a window test |
| inner-set form (§2(c)) | {v : J_v convex on [½,2] and J_v'(2) ≤ 0} is explicit and does not need λ_A. But it is an inner set of {v : I^v_ζζ ≥ 0}, not of 𝒱_T. Inclusion ⊂ 𝒱_T: **FALSE in general / not shown**, since I_ζζ ≥ 0 does not give λ ≥ 0 |
| coefficient form for σ ≥ 2 (PROVED) | J''(σ) = Σ_{m,n} b(m)b(n)(mn)^{−σ}(log mn)² ω̂(log m/n) = 2Q(bL², b) + 2Q(bL, bL), where Q(u,v) = Σu_m v_n(mn)^{−σ}ω̂(log m/n) and ω̂ is positive definite. Q(bL,bL) ≥ 0, but Q(bL², b) is indefinite. No sign even in the absolute region without further input |
Verdict: (W_X) **passes (R)(4)** (a new, clean point: transport of g, not log g, is zero-free) but **fails the inner-set test**. It controls only
I_ζζ, and its ζ-specific hypothesis is a point property (Lemma B(iv)). Not developed further.

## 4. Next (sharpened target)
Find an explicit 𝒮_T, B_T ⊂ 𝒮_T ⊂ 𝒱_T, defined without λ_A. Lemma B and §3 suggest a concrete form: the convex hull of v^Λ and a finite
family of *certified* points of 𝒱_T. 𝒱_T is convex (prop:finite(ii)), so the hull lies in 𝒱_T automatically. The arithmetic must then go into
showing v^Λ is an interior point of the hull of points whose membership is checkable. Since 𝒱_T is convex, it suffices to write
v^Λ = Σθ_i v^{(i)} with θ_i ≥ 0, Σθ_i = 1, v^{(i)} ∈ 𝒱_T. Each v^{(i)} must be a comb whose positivity is provable by other means: archimedean
dominance (small weights), Euler-product combs (prop:summable), or certified windows. This is a **convex-decomposition problem for v^Λ**.
It is the dual of the certificate (lattice/flat-top) approach, and must be pre-screened against class (D) / REF-D first. Not started.

## 5. Self-review
- Lemma B(ii): the infimum over F runs over an infinite family; each member is L_T-Lipschitz, so the infimum is too (possibly −∞ — excluded
  since λ(v^Λ) is finite by P46). ✓ Concavity ✓. The bound L_T ≤ |N_T| is crude; it does not matter for the logic.
- B(iv) is close to a tautology. Its value is the screen: every "point property" candidate (CA_B_001/003/005, Hamburger rows, N_009) is
  thereby reclassified as bookkeeping. This is consistent with (R)(11); it is not a new exclusion. ✓
- §2(a) uses a reading of "bounded functional" in (R)(5). If the paper means something else, §2(a) must be rechecked against its definition
  (P46 rem around l. 8348). Flagged.
- §3 (R)(4) claim: the Poisson representation of a holomorphic function of finite order in a strip needs Phragmén–Lindelöf growth control
  (CITED). With the pole factor (s−1) the representation is of (s−1)g_X. ✓
- §4: convex decomposition with Euler-product combs is close to prop:summable (excluded as a class!). It must be pre-screened against that
  first. Flagged.

## 6. Addendum — lesson (O8 quartets) applied to Lemma B and §4
O8 keeps the comb vector exactly and changes the form side, i.e. the zero side or the archimedean/quartet-coupled form. Consequences:
(a) Any property P(v) of the comb vector alone, however ζ-specific (Hamburger, Δ ≡ 0, Euler-tail vanishing), holds unchanged under O8.
    So it cannot be the separating property. PROVED (trivial: P depends on v only, and O8 fixes v).
(b) Lemma B is a statement for a fixed form. Under O8 the set 𝒱_T itself moves, to 𝒱_T^{O8} ∌ v^Λ. A sign-carrying inner set must
    therefore be a set of *pairs* 𝒮_T ⊂ {(form, v)} with B_T ⊂ 𝒮_T(form_ζ) ⊂ 𝒱_T(form_ζ) and v^Λ ∉ 𝒮_T(form_{O8}). Its membership test must
    read the form at the sign step: the minimizer / the near-coincidence correlation, through the window tests, not through zeros.
(c) This rules out §4's convex decomposition *as stated* when the v^{(i)} are certified by comb-only arguments (archimedean dominance,
    prop:summable). Those certificates do read the form (C_0, Lev), but only through its archimedean part, which O8 can leave fixed? —
    **OPEN**: whether the quartet-coupled form changes C_0 + Lev or only the zero side must be checked against lem for O8 in P46 before §4
    is developed. If O8 leaves C_0 + Lev unchanged, then 𝒱_T (defined via C_0 + Lev − Σ v c_F) does not move, and O8 does not act on
    WP_T at all. In that case O8 is a falsifier only for statements made beyond the window form. Flagged as the first check of the next round.
(d) (W_X) under O8: J_X uses ζ (test) and Z_{<X} (comb). Under O8 ζ is replaced by the quartet-modified function, so the test changes, the
    matching identity changes, and (W_X) can tell O8 apart. This does not rescue it: §3 still applies (it controls only I_ζζ; its
    hypothesis is a point property).

## 7. Post-review reframing (accepted)
- Lemma B(ii) is a corollary of P46 prop:wit-sens (the bottom is ℓ¹-Lipschitz in the weights with constant 1, which is sharper than my
  ℓ^∞ form with L_T). It is not a new clause.
- Lemma B(iv)'s methodological reading is **withdrawn**. A valid deduction P ⇒ (λ ≥ 0) need not cover combs where P fails, so openness
  does not exclude thin exact properties. Only the "not necessary" statement (empty interior) stands, and it carries no exclusion. The
  operative constraints are lem:transfer (closure under O1–O15) and (B″) lem:shape-ident. §2(c) (inner sets defined without λ_A) remains
  as a description of what an argument must produce, not as an exclusion.
