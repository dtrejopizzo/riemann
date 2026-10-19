# Doc 169 — Adversarial audit of Doc 166 (metric deformation, Gram flow, conservation of κ)

**Program:** Riemann Hypothesis — Phase 54: index dynamics.
Mandate: destroy the theorems of Doc 166. Full 6-point protocol executed,
with closed re-derivation (no numerics). Historical pattern watched: (i) parameters as
constants, (ii) finite-dimensional cited as general, (iii) H-26 used silently,
(iv) squares that are not squares.

---

## 0. Verdict per piece

| Piece | Statement | Verdict |
|---|---|---|
| (a) Theorem 166.9, κ(G)=κ | index conservation on 𝕄 | **CORRECT-BUT-EMPTY.** True also in dim ∞, but it is Sylvester's law of inertia relabeled: κ(G) is by construction the inertia of the FIXED form Q transported by congruence. It is not a dynamical theorem; the phrase "conservation law" is rhetorical. The "jump at ∂𝕄" is not a theorem: it is where the definition stops applying. |
| (b) Hessian = L ≥ 0, "RH-free square" | 166.10(a) + 166.12 | **CORRECT-BUT-EMPTY, with scope caveat.** The Hessian is of 𝔇₂ (not of 𝔇, which is not differentiable); 𝔇₂ is quadratic BY CHOICE, so its Hessian is constant and ≥ 0 automatically: the "anti-circularity test" could not have failed. The square is genuine (HS adjoint verified, no conjugation error). Well-defined with proof only in the finite model (GAP 166.D, declared in §4.3 but absent from the §5.1 headline). The weight does NOT introduce ζ — but see §2: the "calibration" is a gauge choice presented as a discovery. |
| (c) W fixed point "unconditional"; RH = W in the cone | 166.13(a), summary §0 | **CORRECT-BUT-EMPTY + hypothesis overselling.** A_t(W)=0 is EXACTLY (H-26)(i) = V.1 of Phase 26, NOT proved. The body cites it; the executive summary says "unconditionally" — pattern (iii) at the headline level. And "RH ⟺ W>0" is the Weil criterion (Weil 1952) verbatim, with dynamical decoration: ZERO new content beyond the (correct, modest) observation that ker L = paired forms λ↔λ̄. |
| (d) Theorem 166.6, φ(b) | universal lower bound | **HOLDS.** φ(b)=2b(1−2b)^{(1−2b)/(2b)} re-derived and CORRECT (computation §4.1). It is the piece with the most real content in the document — conditional on (H-26)(ii) (genuine eigenvector v_j, V.2 not proved), correctly cited. The "strip↔weight calibration" (166.6(i)) is correct but of minor content (the weight is gauge; see §2 and §4.3). |
| (e) Theorem 166.13, linear flow, ℓ(b) | ejection + rate | **CORRECT in the model; the "scale echo" DIES.** ℓ(b)=1/(1−4b²)−2/(1−b²)+1 re-derived and correct; the ejection logic is valid (§5). BUT the coefficient 2 in ℓ(b)≈2b² is an artifact of the weight: with weight e^{−2a|t|} one gets ℓ_a(b)≈2b²/a³ (computation §4.3). The "unexplained factor 4" versus A.15 (Λ=max b²/2) is not a datum: it is gauge dependence. Only the EXPONENT 2 is invariant, and it is forced by the parity γ↦−γ — which the document itself admits and then disregards in the verdict by listing "rate 2b²" as a dividend. |
| (f) Duality with Rodgers–Tao | BRIDGE 166-DBN | **VERBAL ANALOGY with a single point of formal contact.** Both place RH "at a boundary" — that is real as a form of statement. But the table pairs a deep theorem (Λ≥0, Rodgers–Tao 2020) with a tautology (166.9) plus a rewriting of Weil (166.11(c)). "The dynamical variable of one is the conserved quantity of the other" is asymmetric in depth: monotonicity of κ under DBN is de Bruijn 1950 (real); conservation of κ under Gram is Sylvester (empty). Consistent with Doc 167 (no contradiction, §6). |

**Overall verdict:** no theorem of Doc 166 is FALSE. But of its four "non-RH-equivalent
dividends" declared in §6, only one survives intact (166.6/φ, conditional on V.2);
166.9 is dressed-up tautology, the 166.13(a)+(c) interpretation is Weil rewritten and conditional
on V.1, and the 2b² rate loses its coefficient (only the exponent survives, forced by symmetry). The document
is honest in the body (it labels its GAPs) but its executive summary and its verdict survive
better than its fine print — exactly the inflation mode this phase was meant to guard against.

---

## 1. κ(G): well-defined? what content does 166.9 have?

**Good definition.** κ(G) := dim of the negative spectral subspace of M_G := G^{−1/2}WG^{−1/2}.
With G ≥ εI bounded and W boundedly invertible (H-W), M_G is self-adjoint on the background and boundedly
invertible (M_G^{−1} = G^{1/2}W^{−1}G^{1/2}), so 0 ∉ σ(M_G) and the negative spectral projector
is well-defined. Note: the "Gram of Q in the geometry G" is strictly G^{−1}W (G-self-adjoint);
it is similar to M_G via G^{1/2}, same spectrum, same index. Well-defined: YES.

**Validity in infinite dimension.** The document's congruence argument is correct also in
dim ∞: if M ⊂ K is negative-definite for ⟨M_Gx,x⟩₀, then G^{−1/2}(M) is negative-definite for Q, a bijection
that preserves dimension; the sup of dimensions of negative subspaces is κ (H-Π), and coincides with
the negative spectral dimension because M_G is invertible (the compression to the positive
spectral subspace is ≥ ε, so the negative spectral projection is injective on every
negative-definite subspace). This is standard (Bognár 1974, ch. IV: all
fundamental decompositions of a Π_κ have the same negative part κ; Azizov–Iokhvidov 1989, ch. 1).
**The theorem is true as stated, without H-26 and without RH.** No error.

**The content.** This is where the piece dies as a "result." κ(G) is, by construction, the inertia of the
fixed form Q read in the basis/geometry G. Sylvester's law of inertia states precisely that the
inertia of ONE form does not depend on the congruence through which it is viewed. The statement "κ(G)=κ for
every G∈𝕄" is, word for word, that law: it is not being proved that some dynamical quantity is
conserved along a flow, it is being observed that a quantity that does NOT depend on G is
constant in G. Three adversarial consequences:

1. **"Exact conservation law of every deformation" is rhetorical.** It holds for continuous
   curves, discontinuous ones, and for arbitrary reassignments of G — because there is nothing to
   conserve: κ(G) never was a function of G. A dynamical conservation theorem would claim that a
   concrete flow preserves a quantity that a priori could vary. Here there is no such a priori.
2. **The no-go "no deformation of the metric can reduce κ" is true and vacuous.** κ is an
   invariant of Q alone. No one with the definition in front of them could have expected to reduce n_−(Q)
   by changing the inner product with which it is measured. The no-go blocks a strategy that was not
   coherent even as a wish.
3. **"It can only jump at ∂𝕄" is not a theorem.** At ∂𝕄, G^{−1/2} does not exist and κ(G) is not
   defined. What is proved is not "it jumps at the boundary" but "the definition expires at the boundary."
   The "theory of the index jump at ∂𝕄" (GAP 166.F) is well-named as an open problem,
   but Doc 166 does not contribute a single lemma toward it.

**The non-trivial version the document does NOT prove.** What is non-trivial in this area is spectral: e.g. that
for every Q-self-adjoint operator in Π_κ the number of pairs of non-real eigenvalues is bounded
by κ, with root subspaces λ↔λ̄ paired hyperbolically (Pontryagin 1944; Iokhvidov–Krein
1956; Krein–Langer 1973), or the classification of definitizable operators (Langer 1982). That is classical theory
cited, not a product of Doc 166. The genuine contribution of 166.9 to the program is an accounting
sentence, not a mechanism. **The "answer to the director's question" (ejection IS
conservation) conflates two levels:** ejection is a fact of the Gram flow (166.13, finite
model); conservation is a fact of the definition of κ. The second does not explain the first: what
explains ejection is 166.6(ii) (𝔇>0 in the interior) + linearity of the flow, not Sylvester.

**Verdict (a): CORRECT-BUT-EMPTY.**

---

## 2. The Hessian re-derived

**Exact object.** 𝔇 (Def. 166.5) is a sup of norms: convex, 1-homogeneous, NOT differentiable — it
has no Hessian. What has a Hessian is the substitute 𝔇₂(G) = ½∫e^{−2|t|}‖A_t(G)‖²_HS dt
+ ½‖A_J(G)‖²_HS. Since A_t and A_J are LINEAR in G, 𝔇₂ is a quadratic form and its Hessian is the
constant operator L at every point. **Re-derivation of the adjoint (check of pattern (iv)):**
⟨A_t(G),M⟩_HS = Tr((U_t^*GU_t−G)^*M) = Tr(G^*(U_tMU_t^*)) − Tr(G^*M) = ⟨G, U_tMU_t^*−M⟩_HS, hence
A_t^*(M) = U_tMU_t^* − M, exactly as in the document. Note that U_t is NOT unitary (non-real spectrum),
so U_t^* ≠ U_{−t} and order matters: the document gets this right. L = ∫e^{−2|t|}A_t^*A_t dt
+ A_J^*A_J is a genuine sum of HS squares: **the square IS a square.** No conjugation or
sign error.

**With respect to which inner product?** The HS one induced by the BACKGROUND ⟨·,·⟩₀ (RH-free, fixed), not
G. There is no dependence on the base point, no circularity through that door. Correct.

**Convergence.** In operator norm: ‖A_t‖ ≤ 1+‖U_t‖₀² ≤ C²(1+|t|)^{2d}e^{2b_max|t|}
((H-26)(iii)); the integrand e^{−2|t|}‖A_t‖² is integrable ⟺ 4b_max < 2 ⟺ b_max < ½: the same
condition as finiteness of 𝔇. BUT in HS: for generic G in dim ∞, ‖A_t(G)‖_HS = ∞ and 𝔇₂ is not
defined — GAP 166.D, which the document declares in §4.3. **Presentation finding:** Theorem 166.10
(§5.1) and point (b) of the executive summary state "the Hessian of 𝔇 is L ≥ 0" without repeating that
(α) it is 𝔇₂ and not 𝔇, and (β) the claim only has proof in the finite model. Pattern (ii) in the
headline, even though the body is labeled.

**Why could the anti-circularity test not fail?** Because 𝔇₂ was CHOSEN quadratic. Any
functional of the form ½‖T(G)‖² with T linear has constant Hessian T^*T ≥ 0. The question "is the
second variation the Weil form?" was only a live question for a non-quadratic functional
(e.g. the second variation of 𝔇 restricted to a non-linear normalization, or at the boundary
minimizer of 166.11 — not computed). The "clean negative result" of 166.10 is a fact of
design, not a discovery about the problem. Also, the comparison "L ≠ Q" is one of types: L acts
on H_h (Hermitian forms), Q on K; the document itself says so in the proof — so that the
statement "the Hessian is NOT the Weil form" is true in the weak sense that they are not even
comparable.

**Does the weight e^{−2|t|} introduce ζ?** No. The weight is a free parameter of the construction; it carries
no data of ζ (neither zeros nor primes). What there is, however, is inverted rhetoric: the document CHOOSES
the exponent 1 (resp. 2) so that the finiteness condition is "b < ½" and then announces "the critical
strip IS the region of integrability" (166.6(i)) as if the functional had discovered the
strip. With weight e^{−a|t|}, finiteness is b_max < a/2: the "calibration" is the choice a=1. It is
legitimate as design (and the useful direction is the one used: Hadamard–de la Vallée Poussin guarantees
finiteness), but it is not content: any family of groups with bounded exponential growth
admits an exponential weight making it integrable.

**Verdict (b): CORRECT-BUT-EMPTY** (genuine square, RH-free, but automatic positivity
by quadratic design; real scope = finite model).

---

## 3. W fixed point: reformulation of Weil?

**The fact.** A_t(W) = U_t^*WU_t − W = 0 ∀t ⟺ U_t is Q-unitary. That is literally hypothesis
(H-26)(i) — item V.1 of the Phase 26 bridge, which the program's memory records as NOT
proved. Likewise A_J(W)=0. Therefore:

1. **"Unconditionally" is false as an adverb.** The executive summary (§0, point (1)) and the
   interpretation of 166.13 say "A_t(W)=0, A_J(W)=0 unconditionally" / "without RH." "Without RH" is
   correct; "unconditionally" is not: it is conditional on V.1. The body of theorem 166.13 does list
   "(H-26) restricted to the model" — the fine print is honest, the headline is not. It is pattern (iii)
   in its subtlest form: the hypothesis is declared in the framework and then evaporates from the
   language of the results ("universal fixed point," "canonical," "free").
2. **The domain abuse is controlled.** W with m≥1 is indefinite: W ∉ 𝕄 and W ∉ ∂𝕄 (the boundary
   consists of positive semi-definite forms). "W is a fixed point of the flow" refers to the linear extension of
   the flow to all of H_h, and the document says so explicitly ("as a Hermitian FORM, not necessarily
   as a metric," 166.13(a)). No charge here.
3. **The content is the Weil criterion verbatim.** "RH ⟺ the fixed point W falls inside the cone
   𝕄" = "RH ⟺ W ≥ ε > 0" = positivity of the Weil form (Weil, *Sur les "formules explicites"
   de la théorie des nombres premiers*, Comm. Sém. Math. Lund 1952; with the uniformity = GAP
   166.A). The document honestly declares that 166.7 is "Weil-rewritten," but presents the dynamical
   reading of 166.13(a)+(c) ("the critical point always exists and is canonical; RH is its membership
   in the cone") as the "complete picture of the wall" — it is the SAME sentence of Weil with a flow around it.
   The only thing added by the dynamics is 166.13(b): ker L = paired forms λ↔λ̄ (correct computation:
   e^{it(λ_μ−λ̄_ν)}=1 ∀t ⟹ λ_μ=λ̄_ν or null entry). It is a standard commutant observation
   in representation theory; correct, minor.

**Verdict (c): CORRECT-BUT-EMPTY, conditional on V.1, with adverbial overselling in the headline.**
The trap of this phase ("correct reformulation with zero new content") materializes here.

---

## 4. φ(b), ℓ(b) and the factor 4 — closed re-derivation

### 4.1 φ(b): VERIFIED

g(s) = e^{−s}(e^{2bs}−1) = e^{(2b−1)s} − e^{−s}, 0<b<½. g'(s)=0 ⟺ (2b−1)e^{(2b−1)s} + e^{−s} = 0
⟺ e^{2bs} = 1/(1−2b) ⟺ s_* = −log(1−2b)/(2b) > 0. Value: e^{−s_*} = (1−2b)^{1/(2b)} and
e^{2bs_*}−1 = 2b/(1−2b), hence φ(b) = 2b(1−2b)^{1/(2b)−1} = 2b(1−2b)^{(1−2b)/(2b)}. **Matches.**
Asymptotics: (1−2b)^{1/(2b)} → e^{−1} gives φ ~ (2/e)b; b→½⁻ gives φ→1; b≥½: g does not decay, sup=∞.
Strict monotonicity: the integrand grows strictly in b at fixed s. **All correct.** The chain
of the bound too: ⟨A_t(G)v_j,v_j⟩₀ = (e^{−2b_jt}−1)⟨Gv_j,v_j⟩₀ with the chosen sign of t, and
‖A_t(G)‖₀ ≥ |⟨A_tv_j,v_j⟩|/‖v_j‖². It requires a GENUINE eigenvector v_j — (H-26)(ii) = V.2, not proved,
correctly cited in the statement. 166.6(ii),(iii) follow. **Theorem 166.6 holds exactly
as labeled.** It is the result with the most content in the document: an explicit quantitative
lower bound on the metric incompatibility due to each off-line zero.

### 4.2 ℓ(b): VERIFIED in the model

In the normal model, U_t^*E_jU_t = |e^{itλ_j}|²E_j = e^{−2b_jt}E_j, hence A_t(E_j) =
(e^{−2b_jt}−1)E_j and, since A_t^*(E_j) carries the same multiplier, A_t^*A_t(E_j) =
(e^{−2b_jt}−1)²E_j. Integral: with ∫₀^∞ e^{−2t}(e^{2ct}−1)²dt = 1/(2−4c) − 2/(2−2c) + ½ for c=±b,
sum = [1/(2−4b)+1/(2+4b)] − 2[1/(2−2b)+1/(2+2b)] + 1 = 1/(1−4b²) − 2/(1−b²) + 1. **Matches.**
Taylor: (1+4b²+16b⁴) − (2+2b²+2b⁴) + 1 = 2b² + 14b⁴ + O(b⁶) = 2b²+O(b⁴). ✓ Increasing on (0,½)
(2(1−b²)² ≥ (1−4b²)² there) and pole at b=½. ✓ A detail the document dispatches quickly and is correct: E_j
alone is NOT an eigenvector of L (A_J permutes it with E_{j'}, the reflected one); the eigenvector is E_j+E_{j'},
on which the t-part acts with the SAME ℓ(b) in both components because the integral with an even weight
is invariant under b↦−b. I also verified the Jordan chain of 166.13(c): with Gv_j=0 and G=G*≥0,
⟨G(w+itv_j), w+itv_j⟩ = ⟨Gw,w⟩ (the cross terms vanish by ⟨Gw,v_j⟩=⟨w,Gv_j⟩=0), constancy in t
forces ⟨Gw,w⟩=0 ⟹ Gw=0; the induction is correct. **Theorem 166.13 is correct in the finite model.**

### 4.3 The factor 4: it is NOT a mystery — it is gauge. The "quantitative echo" dies.

**DBN side (A.15).** Isolated-pair model under the heat flow: ż_k = Σ_{j≠k} 2/(z_k−z_j)
(Rodgers–Tao 2020, §2; de Bruijn 1950). For an isolated conjugate pair z = x±iy:
ż = 2/(z−z̄) = −i/y ⟹ ẏ = −1/y ⟹ y² = y₀² − 2t, collision at t = y₀²/2. With y₀ = b (coordinate
z = γ−ib of the zero ½+b+iγ): contribution b²/2 to Λ. **A.15 is correctly computed as an isolated-pair
heuristic.** No error on that side.

**Gram side.** ℓ(b) = 2b²+O(b⁴) — correct (§4.2) — **but the coefficient depends on the weight.** With
weight e^{−2a|t|} (a>2b_max arbitrary, equally admissible: the only structural restriction is
integrability), the same integral gives

  ℓ_a(b) = a/(a²−4b²) − 2a/(a²−b²) + 1/a = (2b²/a³) + O(b⁴/a⁵).

With a=1 one gets 2b²; with a=4^{1/3} one would get exactly b²/2. Moreover the time parameter s of the flow
Ġ=−LG has no canonical identification with the t of DBN: rescaling s rescales ℓ. **Conclusion: the
"factor-4 discrepancy" is not a datum to explain — it does not exist as an invariant.** The only
gauge-invariant thing is the EXPONENT: ℓ ~ b² and Λ ~ b², first even power allowed by the
symmetry γ↦−γ, as [BRIDGE 166-E] itself acknowledges ("structural echo, not identity") — but
then the §6 verdict should not have listed "rate 2b² — scale echo with Λ=max b²/2" as a
quantitative dividend nor should the summary have called it a "quantitative echo." It is parity, not shared physics.

**Verdict (d): HOLDS (conditional on V.2). Verdict (e): correct in the model; the
quantitative echo and the factor 4 are ELIMINATED as content.**

---

## 5. The ejection logic of the linear flow

The mandate suspected a non sequitur ("a linear flow with L≥0 decays toward ker L, it does not eject").
Examination: in the finite model, G(s) = e^{−sL}G₀ → G_∞ = P_{ker L}G₀ (HS-orthogonal projection,
spectral decomposition of L, finite-dimensional spectral gap). "Ejection" is then a
corollary, not a mechanism: (α) if G_∞ is indefinite, λ_min(G(s)) goes from >0 to <0 and by
continuity crosses 0 at s_*<∞: the trajectory LEAVES 𝕄 in finite time — valid; (β) if G_∞ ≥ 0,
by 166.13(c) ker G_∞ ⊇ N and G(s) → ∂𝕄 asymptotically (never reaching it in finite time) —
"toward" the boundary is the correct word. **The document's logic is valid and, in fact, the document
itself states it this way** ("the linear flow does NOT preserve the cone in general, and that is the content"). No logical charge. Two adversarial nuances:

1. **The cause of the ejection is not 166.9.** It is the combination (166.6(ii): 𝔇>0 in the interior) +
   (linear convergence to ker L) + (ker L ∩ 𝕄 = ∅ if m≥1). The narrative "ejection is
   conservation of inertia" superimposes tautology (a) onto a mechanism that works without it.
2. **"It crushes exactly the off-line directions": does ζ re-enter the description?** The
   crushed directions are the E_j of the eigenvectors v_j, which exist by (H-26)(ii) — the
   off-line zeros are in the DEFINITION of the finite model (they are set by hand as eigenvalues
   λ_j = γ_j+ib_j). It is not additional circularity: it is the declared hypothesis of the framework. But it
   must be said without euphemism: ALL the quantitative dynamical content of the document (166.13) lives
   in a model whose input is the positions of the zeros. "RH-free dynamics" here means
   "without assuming positivity," not "without data from ζ." The document lets this be read between the lines (Obs. 166.4,
   GAP 166.D); the summary proclaims it without that line.

**Verdict (e), logical part: HOLDS in the finite model; no proven extension to dim ∞
(GAP 166.D declared).**

---

## 6. Consistency 166 ↔ 167 and the duality with Rodgers–Tao

**Contradiction κ-conserved (166) vs κ-dissipated (167)?** No. They are flows over different
variables: the Gram flow moves G with W FIXED — and κ = n_−(W) cannot change because nothing that
touches W changes (this is again the deflationary reading of 166.9: the "conservation" is that the
dynamical variable does not appear in the quantity); DBN moves the function Ξ_t, hence the form, hence its
index can drop (de Bruijn 1950, Thm 13: the reality of the zeros is absorbing; Doc 167,
Theorem 2.3: İ = −2κ − D). **Consistent.** Fine note: on the 167 side, calling "κ" the count of
non-real pairs of H_t requires the Phase 26 bridge (κ=2m=neg.ind) which is NOT proved; both
documents declare this ([BRIDGE], Doc 167 §0; Doc 166 §4.2). Labeling coherence: correct.

**Is duality (f) structure or verb?** What is verifiable from table 166-DBN:

- "moving form/fixed metric vs moving metric/fixed form" — true as a description of the two
  setups. But there is NO mathematical map whatsoever between the two variational problems (the document
  itself records this as [WISH 166.C]). Without a map, "duality" is a word.
- "RH at the boundary in both" — formally true: RH ⟺ Λ=0 (boundary of {Λ≤0}∩{Λ≥0}, Newman
  1976 + Rodgers–Tao 2020) and RH ⟺ the infimum 0 of 𝔇 is attained (166.11(c)). But the second
  item is the Weil criterion rewritten (§3 above), so that the "duality" pairs a
  deep, new theorem (RT) with a contentless reformulation. Isomorphism of FORM of
  statement, yes — the document uses exactly that word ("isomorphic in FORM") in §0, which is
  honest; the table row "the dynamical variable of one is the conserved quantity of the other"
  is no longer quite that: it suggests a symplectic/coupled structure that nobody built, and the
  "conserved" half is Sylvester (empty).
- The only candidate for shared content was the quantitative echo 2b² ↔ b²/2 — eliminated in
  §4.3 (gauge).

**Verdict (f): honest VERBAL ANALOGY in §0, over-structured in table §4.2; consistency
166↔167 verified.**

---

## 7. Minor charges verified (without consequences)

- Prop. 166.5′(c): A_t(σG) = J^*A_{−t}(G)J re-derived with JU_t = U_{−t}J — correct; the
  J-symmetric average kills A_J by convexity — correct.
- Prop. 166.7′: U_t^*W = WU_t^{−1} from U_t^*WU_t = W with W invertible — correct; the
  partition into two unitary blocks and Stone/linear algebra — correct. Good explanatory
  piece (the metric version of the D165 wall).
- Prop. 166.2(d): T = G₁^{−1/2}G₂^{1/2}, T^*G₁T = G₂ — correct.
- Prop. 166.3(a): S₀ = sign(W), WS₀ = |W| ≥ ε — correct under (H-W); the dependence on (H-W)
  (W boundedly invertible, GAP 166.A) is the Achilles' heel of the ENTIRE transfer to the
  arithmetic object, and it is declared.
- Prop. 166.11: the change of background product to orthogonalize N ⊕ K₁ alters the value of 𝔇
  only by equivalence constants; "inf = 0" survives — correct, though it deserved a line.
- 𝔇₂ with weight e^{−2|t|} vs 𝔇 with e^{−|t|}: consistent (square of the weight for the square of the
  norm); both finite ⟺ b_max < ½ with (H-26)(iii).

---

## 8. Final summary

**Verdicts:** (a) 166.9 CORRECT-BUT-EMPTY (Sylvester relabeled; not a dynamical theorem;
"jump at ∂𝕄" not proved, only undefinedness). (b) Hessian CORRECT-BUT-EMPTY (automatic
positivity of a functional chosen to be quadratic; genuine square; proof only in the finite model;
weight = gauge, not a door for ζ). (c) W fixed point: CORRECT but conditional on V.1 — the
"unconditionally" of the summary is overselling — and "RH = W in the cone" is the Weil criterion
verbatim: zero new content. (d) 166.6/φ(b) HOLDS (exact re-derivation; conditional on V.2;
the best piece of the document). (e) 166.13/ℓ(b) correct in the model and the ejection logic is
valid; but the coefficient 2b² is an artifact of the weight (ℓ_a ≈ 2b²/a³) and the "factor 4" versus
A.15 does not exist as an invariant: the quantitative echo is eliminated, only the exponent
b² forced by parity survives. (f) Duality with Rodgers–Tao: analogy of statement form, without a map;
pairs a theorem (RT) with a tautology (166.9) + a rewriting (166.11(c)); consistent with
Doc 167 (flows over different objects, no contradiction).

**Three main findings:**

1. **No theorem is false, but the dividends degrade two levels.** Of the four
   dividends in Doc 166's §6 verdict, only 166.6 survives intact (φ(b), conditional on
   V.2). 166.9 is bookkeeping (Sylvester), the "universal fixed point" reading is Weil 1952 with
   dynamical decoration and conditional on V.1, and the only quantitative bridge with DBN (2b²↔b²/2) is
   gauge-dependent. The correct verdict for Doc 166 is not B′: it is B with ONE new conditional
   bound (166.6) and new language.
2. **The "unexplained" factor 4 is not an enigma: it is normalization.** Recomputing both sides
   in closed form: the DBN isolated-pair heuristic gives Λ ~ b²/2 (correct); ℓ(b) = 2b² is correct
   BUT with weight e^{−2a|t|} it becomes 2b²/a³ — the coefficient is not invariant under the gauge
   freedom of the weight nor of the flow's time. It should be struck from [BRIDGE 166-E] as a "datum."
3. **Pattern (iii) in the headlines:** "A_t(W)=0 unconditionally" (summary §0) is exactly
   (H-26)(i) = V.1 of Phase 26, not proved. The body of Doc 166 labels correctly; the executive
   summary and the interpretation of 166.13 speak as if V.1 were general theory. The same, to a
   lesser degree, with the finite-dimensional scope of 166.10/166.13 (GAP 166.D declared in §4.3 and
   absent from the headline statements). Recommendation: drafting errata, not mathematical ones —
   but in this program the drafting IS the line of defense.

**References.** A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
Comm. Sém. Math. Lund (1952) 252–265. — L.S. Pontryagin, Izv. Akad. Nauk SSSR 8 (1944) 243–280. —
I.S. Iokhvidov, M.G. Krein, Trudy Moskov. Mat. Obshch. 5 (1956). — J. Bognár, *Indefinite Inner
Product Spaces*, Springer 1974 (ch. IV–V). — T.Ya. Azizov, I.S. Iokhvidov, *Linear Operators in
Spaces with an Indefinite Metric*, Wiley 1989 (ch. 1 §8, ch. 2 §2). — M.G. Krein, H. Langer,
Acta Sci. Math. (Szeged) 34 (1973) 191–230. — H. Langer, *Spectral functions of definitizable
operators in Krein spaces*, LNM 948, Springer 1982. — N.G. de Bruijn, Duke Math. J. 17 (1950)
197–226. — C.M. Newman, Proc. AMS 61 (1976) 245–251. — B. Rodgers, T. Tao, Forum Math. Pi 8
(2020) e6. — M. Reed, B. Simon, *Methods of Modern Mathematical Physics I*, 1980. —
[Literature GAP] I know of no published treatment of the inertia for families of fundamental
symmetries degenerating (coincides with GAP 166.F of Doc 166); I cannot refute the novelty claim of
the functional 𝔇 with calibrated weight from known literature.
