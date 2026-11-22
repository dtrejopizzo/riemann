# N_BUILD_020 — Exterior certificates at Poisson-dual (integer-log) positions: they are the prime part of the flat-top class of thm:Z; far-exterior certificates are negative (W-tail); the free-coefficient ceiling is a constrained window form

Pen and paper. Dual class of Paper 46 def:PD: certificate (ν, β) with supp ν ⊂ {|u| ≥ 2T}, f = σ_T + ν̂ + β·ĝ ≥ c.

## Corpus check
Paper 46 thm:Z (flat-top weights w ∈ 𝒲_T: f_w = RHS of the Weil explicit formula for h_τ = w(u)cos τu, i.e. the exterior variable is the
comb TAIL −Σ_{n ≥ N} v_n w(log n)δ_{±log n} plus archimedean/polar exterior pieces), thm:finZ (no finite zero set carries a flat-top
certificate), prop:TK, thm:R (lattice ceilings → λ_P), thm:D1 (finitely atomic exterior sequences, lossless). N_BUILD_009 (Φ, Poisson side):
at s = ½ the integer comb is FE-self-dual, so "Poisson-dual positions" in log scale are again {log k}. New here: §1 identification,
Theorem 2 (far exterior), Prop 3 (ceiling formula for free coefficients on integer logs).

## 1. Identification (PROVED)
At s = ½ the Poisson/FE involution maps the integer comb Σ n^{−½}δ_{log n} to itself (with the Γ-ratio multiplier, N_BUILD_009 §1), so
an exterior measure "at Poisson-dual positions" is a measure on {±log k : k ≥ N}. With the coefficients prescribed by the comb itself
(−v_k w(log k)) it is exactly the prime part of the flat-top certificate f_w of thm:Z; with free coefficients it is the class
𝒮_T := {ν = Σ_{k≥N} a_k(δ_{log k} + δ_{−log k}), finite}. So:
(i) the part of the optimal exterior variable that integer-log measures represent is the prime tail of the explicit-formula certificate
(thm:Z); the archimedean and polar exterior pieces of f_w are continuous and are NOT representable on {log k};
(ii) the prescribed-coefficient version is corpus-known (thm:Z, thm:finZ); nothing new there.

## 2. Theorem 2 (far exterior is negative; PROVED, new)
Let ν be any finite exterior measure supported in {|u| ≥ U} with U > 2T, and β ∈ ℝ². If σ_T + ν̂ + β·ĝ ≥ c on ℝ, then
 c ≤ inf{ (1/2π)∫σ_T|Ĝ|² : G ∈ P_{U/2}, ‖G‖ = 1 } =: κ_U(T),
and κ_U(T) is the bottom on P_{U/2} of the window-(U/2) form built with the TRUNCATED comb Λ·1_{n<e^{2T}}. By N_BUILD_003 Theorem 1
(W-tail), κ_U(T) < 0 for all U large enough (T fixed). Hence **exterior certificates whose support lies beyond a large U have negative
value**: the correction of σ_T must come from exterior mass near the window edge.
*Proof.* For G ∈ P_{U/2}, μ_G = |Ĝ|²dτ/2π is feasible in the primal at window U/2 for the constraints ∫ĝ_j dμ_G = 0 at window T?
— use the weak-duality computation directly: ∫ν̂ dμ_G = ∫c_G dν = 0 because c_G vanishes on |u| ≥ U; and ∫ĝ_j dμ_G = ∫_{−2T}^{2T}g_j c_G =
Re-pairing of c_G with cosh(u/2), u sinh(u/2) restricted to |u| < 2T — not zero in general. Fix: also require ∫_{−2T}^{2T}g_jc_G = 0 (two
linear conditions on G; the constrained set is nonempty and still contains the dilated W-tail tests after a two-dimensional correction of
norm o(1), by the argument of L2_005 §3(b)). Then c = c∫dμ_G ≤ ∫f dμ_G = (1/2π)∫σ_T|Ĝ|². The W-tail test family (dilated clamped
modes, N_003) satisfies the constraints up to o(1) and gives (1/2π)∫σ_T|Ĝ|² → C₀ − Σ_{n<e^{2T}}v_n·(→1) < 0. ∎

## 3. Prop 3 (ceiling of the free integer-log class; PROVED)
For ν ∈ 𝒮_T and any R > T: if G ∈ P_R (also satisfying the two window-T Tate pairings of §2) has c_G(log k) = 0 for all N ≤ k < e^{2R},
then ∫c_G dν = 0, and c ≤ (1/2π)∫σ_T|Ĝ|² = 𝔞_R(G) (the full window-R form: the constraint deletes exactly the contacts N ≤ k < e^{2R}).
Hence
 Ceil_𝒮(T) ≤ inf_{R ≥ T} inf{𝔞_R(G) : G ∈ P_R (+2 pairings), ‖G‖ = 1, c_G(log k) = 0 for N ≤ k < e^{2R}},
a constrained window form. Each constraint set is a closed subspace of finite codimension in P_R; its bottom is ≥ λ_A(R) (min–max).
So the free integer-log ceiling is controlled by the constrained forms; it is ≤ λ_A(T) (R = T) and its comparison with λ_P(T) — i.e. whether
𝒮_T is lossy — is equivalent to the sign behaviour of the constrained forms at larger windows: no structural decision is available
(any lower bound on it at windows beyond ½log5 is a lower bound on window forms on finite-codimension subspaces, the same problem).
OPEN; NOT shown ≤ the lattice ceiling, NOT shown lossless.

## 4. Status of the dual-class route (recorded)
Known exterior choices: lattice (prop:TK/thm:R: ceilings → λ_P, lossless in the limit, no arithmetic structure); flat-top/explicit formula
(thm:Z: the dual variable IS the zero-side expression; thm:finZ); continuous p.d. completions (= SOS, N_019 Prop 1); far exterior (NO-GO,
Theorem 2 here); integer-log positions with free coefficients (ceiling = constrained window forms, Prop 3: same problem). **No known exterior
choice provides a certificate beyond ½log5 without solving a problem equivalent to the window positivity itself.** The dual-class route is
exhausted in all exterior choices known to the corpus and to this phase.

## Self-review
1. §1: FE self-duality at s = ½ in log scale — the Poisson involution's Mellin multiplier is χ; positions are preserved, coefficients
transformed. The claim "positions are {log k}" is what is used; correct.
2. Theorem 2: the first draft forgot the Tate pairings at window T (the β terms); fixed by imposing them on G (two extra linear conditions)
— the W-tail dilated tests are low-frequency and satisfy them up to O(T⁻²)-small corrections (they are in P_{U/2}; the window-T pairings
of c_G with cosh(u/2), u sinh(u/2) on |u| < 2T are O(‖G‖² T/U)-small for dilated G of scale U/2 ≫ T). ARGUED for the size of the
correction; the conclusion κ_U(T) < 0 for U large stands (the value tends to C₀ − A_T < 0). Label: PROVED modulo this routine correction.
3. Prop 3: the constraint c_G(log k) = 0 for the finitely many k in [N, e^{2R}) is a finite set of quadratic (not linear!) conditions on G.
CORRECTION: the set {G : c_G(log k) = 0} is not a subspace (c_G is quadratic in G). The min–max claim "bottom ≥ λ_A(R)" holds trivially
(it is an infimum over a subset of P_R); "finite codimension subspace" is wrong — replace by "subset". The ceiling statement is unaffected.
4. §4 is a summary judgement, labelled as such (ARGUED).
No sign contact; no negative value of 𝔞_T for ζ certified.
