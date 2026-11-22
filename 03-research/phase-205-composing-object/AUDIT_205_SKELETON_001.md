# AUDIT_205_SKELETON_001 — Skeleton review (phase 205)

Object: `SKELETON_001.md`. Pure mathematics; a single
numerical computation (zero of m^♯, mpmath) to correct an estimate.

## Summary (≤250 words)

P3 is **correct** (rederived line by line: decomposition e^{|s|/2} = cosh(s/2) + sinh(|s|/2), derivative jump, boundary
values, β_T = 1 + ½sinh T; odd β′_T = ½sinh T − 1). But it is **not new**: it is P46 lem:polarelim (e^{u/2} ↔ −e^{−u/2}
on P_T, 𝔢(F) = (1/2π)∫|F̂|²/(¼+τ²)) extended outside P_T. The canonical form is
**M(F) = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²)** on all of L²(I_T); the skeleton's "boundary Dirichlet energy" E_G is
E_G = 𝔢 + (½sinh T − 1)ℓ² (even), a non-canonical split that manufactures the "slack" in (6.1). Φ_E is **exactly** −𝓕_T from
P46 prop:sharp = −R_Λ from PROOF_L_SHARP_B_001 Lemma 3.1 (V_001 Thm V.2.1 only shifts the trivial term ½log(1−e^{−2t}) to the
archimedean part). (6.1) is **PROVED unconditionally** (the two "2"s are the same pole), but it is the identity
W^ev = 𝔞^♯ − 𝓕_T: the slack ½sinh T − 1 is an artifact of E_G, without content. In ker ℓ ∩ L²_ev = P_T^ev, 𝔅_T = W^ev = 𝔞_T,
so **L205.★ is the compression to E_N^ev of P46 prop:sharp(ii)**: REF-D from birth (and furthermore only a necessity).
Piece 1: agreed, trivial composition. Falsifier m − σ_T: correct, but already implied by cor:H1minus. Integrable into P46:
a remark after lem:polarelim (identity M on all of L²) and the coefficients c_k; P2a as an optional technical lemma.
Typo: β_T(½log15) = 1.90370 (not 1.90474); t₀′ = 6.12587 (zero of m^♯, NUMERICAL), not "2–6." Next round: withdraw 𝔅/L205.★
as a live node, P1.c as the only open tool with content.

---

## 1. P3 — Green's identity of the pole

### 1.1 Rederivation (PROVED, confirmed)
(a) *Main term.* Π_T(F) = −Σ_{n≤X} v_n Re c_F(log n) = −∫_{(1,X]} 2t^{−½}Re c_F(log t) dψ(t). With dψ = dt + dE and
t = e^u: −∫_0^{2T} 2e^{u/2} c_F(u) du = −∫_{−2T}^{2T} e^{|u|/2}c_F(u)du = −∫∫F(x)F(y)e^{|x−y|/2}dxdy. "Density 2e^{u/2},
residue 1" means exactly: the measure dψ has main part dt (residue 1 of −ζ′/ζ at s = 1) and v_n = 2Λ(n)/√n
carries dt to 2e^{u/2}du. ✓ Stieltjes summation over (1, X]: there are no boundary terms (dψ is a measure; c_F(2T) = 0). ✓

(b) *Kernel.* e^{a} = cosh a + sinh a with a = |s|/2 and cosh even ⇒ e^{|s|/2} = cosh(s/2) + sinh(|s|/2). ✓
cosh((x−y)/2) = ch(x)ch(y) − sh(x)sh(y) ⇒ −∫∫FF cosh = −⟨F,ch⟩² + ⟨F,sh⟩². ✓
(∂² − ¼)sinh(|s|/2) = δ: away from 0 it is ¼sinh, and the derivative ½cosh(s/2)sgn s jumps by 1. ✓ Hence g := −sinh(|·|/2)∗F
satisfies −g″ + ¼g = F on I_T, and −∫∫FF sinh(|x−y|/2) = ⟨F,g⟩ = ∫(g′² + ¼g²) − [gg′]_{−T}^{T}. ✓

(c) *Boundaries, even sector.* g(T) = −∫sinh((T−y)/2)F = −sinh(T/2)ℓ + cosh(T/2)⟨F,sh⟩ = −sinh(T/2)ℓ;
g′(T) = −½∫cosh((T−y)/2)F = −½cosh(T/2)ℓ. g even, g′ odd ⇒ [gg′] = 2g(T)g′(T) = ½sinh T·ℓ². ✓
M = −ℓ² + E_G − ½sinh T ℓ² = E_G − (1 + ½sinh T)ℓ². **β_T correct.**

(d) *Odd sector.* g(T) = cosh(T/2)ℓ_s, g′(T) = ½sinh(T/2)ℓ_s, g odd, g′ even ⇒ [gg′] = ½sinh T ℓ_s²; cosh term: +ℓ_s².
M = E_G − (½sinh T − 1)ℓ_s². **β′_T correct** (PROVED, now written out).

(e) *Numerical typo.* β_{½log15} = 1 + ½·½(√15 − 1/√15) = 1.903696…, not 1.90474; slack ½sinh T − 1 = −0.09630 (the
skeleton gives −0.095). Harmless, but it must be corrected before the calibrator uses it.

### 1.2 New or rewrite? — REWRITE of P46 lem:polarelim
P46 §`subsec:polarfree`, lem:polarelim: on P_T, 2∫_0^{2T}Re c_F e^{u/2} = −2∫_0^{2T}Re c_F e^{−u/2} = −𝔢(F), with
𝔢(F) = (1/2π)∫|F̂|²/(¼+τ²) = ‖G′‖² + ¼‖G‖², G ∈ H²_0 the "clamped" potential (¼−∂²)G = F. The computation without a
moment restriction is the same with one more line: e^{|s|/2} = 2cosh(s/2) − e^{−|s|/2}, so, for **every** F ∈ L²(I_T),

  **M(F) = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²).**   (R1)

This is the canonical form: the kernel e^{−|s|/2} is the Green function of −∂² + ¼ **on the line** (exact symbol
1/(¼+τ²)) and the rank-2 term has coefficient 2, the same "2" from the pole in W^ev = 𝔄_ev + 2ℓ². On P_T (ℓ_c = ℓ_s = 0)
(R1) is lem:polarelim. In the corpus: "pole − Chebyshev main term = Poisson kernel" is PROOF_L_SHARP_B_001 Lemma 3.1
(index l.451, "PROVED, classical"), E_001 Lemma E.4, and the anatomy of MORI15_EXTREMAL_001 ("pole − Chebyshev main =
∫e^{−|u|/2}c, +0.6700"); N_BUILD_001 (phase 188) has 𝔢 = ‖G′‖² + ¼‖G‖².

The skeleton's E_G is the Dirichlet energy of the potential **on I_T without a boundary condition** (g = −sinh∗F grows as
e^{|x|/2} outside the support). Comparing with (R1):

  E_G = 𝔢 + (½sinh T − 1)ℓ²  (even),   E_G = 𝔢 + (½sinh T + 1)ℓ_s²  (odd).   (R2)

Hence the skeleton's claim "E_G has formal symbol 1/(¼+τ²)" is **false as stated**: that symbol belongs to 𝔢; E_G
differs by a T-dependent rank-one term. And the sentence "turns the 'all but one' into an identity" was already true with
(R1), with weight 2 instead of β_T. P3 = **correct REWRITE**, not a new tool; the index must record it as such (the "0
hits" in §0 of the skeleton is because it searched for "Green" and "e^{|", not "polarelim," "Poisson," "pole − main term").

### 1.3 Does it hold for P46?
Yes, in the form (R1), as a one-line remark after lem:polarelim: "The first equality uses F ∈ P_T; without it,
−∫∫F(x)F(y)e^{|x−y|/2} = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²) for every F ∈ L²(I_T)." Combined with eq:Aform this gives, on 𝒟_T and
without the Tate condition, **𝔞_T(F) = 𝔞^♯(F) − 𝓕_T(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²)** (extension of prop:sharp(ii) outside P_T),
which is the explicit version of the 𝔄 ↔ W relation of prop:WT by sectors. The E_G/β_T variant is **not** integrated
(non-canonical). Verification against P46 definitions: v_n = 2Λ(n)/√n ✓, c_F ✓, χ_ev = cosh(t/2)1_{I_T} ✓ (cor:H1minus),
𝔢 and 𝓕_T from subsec:polarfree ✓, m^♯ = m + 1/(¼+τ²) from prop:sharp(i) ✓.

## 2. Φ_E = the form of ψ(t) − t

Φ_E(F) = −∫_{(1,X]}2t^{−½}Re c_F(log t)dE(t). Comparison:
- P46 subsec:polarfree: 𝓕_T(F) = Σv_nRe c_F(log n) − 2∫_0^{2T}Re c_F e^{u/2}du = ∫2t^{−½}Re c_F(log t)d(ψ − t).
  **Φ_E = −𝓕_T exactly.** P46 calls it "the Chebyshev remainder of prop:wit-cheb."
- B_001 Lemma 3.1: R_Λ(f) = 2∫_1^μ t^{−½}c_f(log t)d(ψ(t) − t). **Φ_E = −R_Λ**, the same object.
- V_001 Thm V.2.1: R_Λ(t) = ψ(e^t) − e^t + ½log(1 − e^{−2t}). It is the same measure plus the contribution of the trivial
  zeros, which in the skeleton lives inside 𝔪 (in B_001: m^♯ = ã = Re ψ(5/4 + iτ/2) − log π already absorbs the k = 0
  term). Apart from this shift, the skeleton's pair (𝔪 + 𝔢, Φ_E) is the pair (ã-form, R_Λ) of B_001/V_001/MORI15 (index
  I6, "PROVED (REF-D)").

**Verdict 2:** 𝔅_T = 𝔪 + E_G + Φ_E = (𝔞^♯ − 𝓕_T) + (½sinh T − 1)ℓ², i.e. the V_001/B_001 decomposition rewritten in
window coordinates, plus the artifact (R2). Asking for positivity of 𝔅_T is asking for positivity of a form whose only
arithmetic term is the Chebyshev remainder; the zero side is its exact reading (index l.451: "R_Λ = ã-form − sum over
zeros, identity"). REF-D by P4/K2.

## 3. (1.4) and (6.1)

With (R1) in the even sector: 𝔄_ev = 𝔪 + Π = 𝔪 + 𝔢 − 2ℓ² + Φ_E. With H1PLUS (1.4), 𝔄_ev = Z_T − 2ℓ² ⇒ Z_T = 𝔪 + 𝔢 + Φ_E
= 𝔞^♯ − 𝓕_T on all of L²_ev. Adding (R2): **𝔅_T = Z_T + (½sinh T − 1)ℓ²**. The two "2"s are the same coefficient (that
of the pole in (R1)), so (6.1) is **PROVED given (1.4)**, with no normalization CONDITIONAL. The Mori-checked version of
the slack: −0.0963ℓ².

Does it imply anything new? **No.** The "rank-one polar slack of size e^T/4" is not an arithmetic quantity: it is the
difference (R2) between two energies of the same potential (on I_T with a free boundary vs. on ℝ). It appears in E_G and
disappears in 𝔅 − 𝔄; no inequality about ζ uses it. On ker ℓ it is zero. Nor is it "a quantity with a sign from scale e^T":
it is β_T − 2, a Γ-free number from the geometry of the window (it holds equally for a_P, cΛ, DH-with-zero-pole gives
0·…). The only thing with content is Z_T = 𝔞^♯ − 𝓕_T, already in P46.

## 4. Piece 1 / Schur by frequency

Agreed with the architect: **only trivial** composition. By Def O1.2 (O1_COMPOSITION_001), a step composes if its margin
depends on E and F in such a way that no falsifier satisfies all its premises; P1.a/P1.b are consequences of A∞ (F) plus
the compressed target inequality — this is not a step, it is the goal. Moreover, as in AUDIT_204_CSTAR_001, the
"presence" of Λ enters through Π_N, which is the same linear form in the comb: if one tried to use Π_N^ev ≽ δ_N in
⌈N/2⌉ − 1 directions as a premise, the step is linear in Λ (W-lin) ⇒ it chains. Checks: e_k with k odd are even ✓
(sin(ω_k(x+T)) = (−1)^{(k−1)/2}cos ω_k x); P1.b by min–max ✓; P1.c correctly OPEN and the correction "𝔪_⊥ ≥ 0 is not free"
is right (the sines are not band-limited). P1.c is **the only OPEN piece of the skeleton with tool content** (upper
bound of A∞): it is not REF-D, because it concerns only 𝔪 + Π in the complement and can be falsified or proved without
zeros. Nuance: Haynsworth in infinite dimension requires 𝔄_⊥ closed and coercive — standard CITED, correct as a
conditional.

P2a: G_kk rederived (sin(ω(4T − u)) = −sin ωu) ✓; G_kl with s = (−1)^{k+l} plausible and consistent with the quadrature
check; PROVED-elementary. A technical tool, not a sign step; it can go as an appendix lemma if P5 is published.

§5.3: c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²)) rederived (∫_{−T}^{T}cosh(x/2)cos ωx = 2ω cosh(T/2) sin(ωT)/(¼+ω²), with
cos ω_kT = 0 and signs that cancel) ✓; ‖χ_ev‖² = T + sinh T ✓. Remark: c_k ∝ ω_k/(¼+ω_k²) is exactly the symbol
of the rank-2 term of (R1) evaluated at ω_k — consistent.

## 5. Falsifier m − σ_T ≥ 0

σ_T(0) = Σ_{n≤e^{2T}}2Λ(n)/√n = 4e^T(1+o(1)) (partial summation, PNT CITED; ≫ e^T by Chebyshev) ✓; m(0) = C₀ ✓.
NO-GO correct. But it is **redundant**: if the symbol were ≥ 0, 𝔄_ev ≽ 0, against cor:H1minus (n₋ ≥ 1 for T ≥ 0.12) — the
NO-GO was already PROVED in P46. Label: NO-GO (PROVED; immediate corollary of cor:H1minus). The "empty tail" is
H1PLUS §4.2 ✓.

## 6. L205.★ and K1–K6

In the even sector, ker ℓ ∩ L²_ev = P_T^ev (the two moment conditions A = B = 0 reduce to ℓ = 0 by parity). On
ker ℓ, (R2) gives E_G = 𝔢, so **𝔅_T = 𝔞^♯ − 𝓕_T = 𝔞_T** (prop:sharp(ii)). Thus

  **L205.★ (math content) ≡ 𝓕_T(F) ≤ 𝔞^♯(F) ∀F ∈ E_N^ev ∩ P_T, T ≥ T₁**,

which is the compression to a subspace of dimension ⌈N/2⌉ − 1 of the P46 prop:sharp(ii) inequality — exactly the one
B_001 (Thm 4.2), H1PLUS §4.2 and V_001 left as REF-D. Consequences:
- **K2 kills it at birth**: every proof is, by (1.4), "Z_T ≥ 0 on E_N^ev ∩ P_T," and there is no slack (the term
  (β−2)ℓ² vanishes on ker ℓ). The K2 criterion as written ("Z_T ≽ −(β−2)ℓ²") suggests a slack that does not exist in
  the domain of L205.★.
- It is **weaker** than D^ev (finite compression: only necessity, P1.b) and it is not D^ev rewritten as such; it is a
  finite consequence of D^ev. Even if proved, it does not give n₋(𝔄_ev) = 1 without P1.c **and** without q_ev < −½.
- Clauses (E)/(F) ("the proof uses…") are not part of the statement; they are the requirement of Def O1.2 and must be
  formulated as declared premises of the step, verifiable against the falsifiers (K4/K5), not as intent.
- K6 becomes trivial to evaluate but with no informative killing power: n₋(𝔅|E_N ∩ ker ℓ) in ζ is n₋ of the compressed
  𝔞_T, which P46 already certifies ≥ 0 in the Mori windows (½log15); P5/K6 only reconfirms known data.
- Data correction: t₀′ (zero of m + 1/(¼+τ²) = m^♯ = Re ψ(5/4 + iτ/2) − log π) = **6.12587** (NUMERICAL, mpmath;
  B_001 gives "≲ 5.8" for the region of effective negativity). Not "2–6." Φ_E must cover ⌈2T·6.126/π⌉/2 directions:
  almost the same as A∞ (t₀ = 6.290): the "free help" from 𝔢 removes O(0.08T) directions out of ≍ 2T. That is, 𝔢 does
  **not** help in the count.

**What the architect must change:** withdraw 𝔅_T and L205.★ as a "live node." A successor to L205.★ is admissible only
if (i) its statement is not a compression of prop:sharp(ii)/Z_T ≥ 0 (test: it does not reduce by (1.4) to zero data),
(ii) it declares a step with explicit premises and shows, for a_P, Epstein, cΛ and DH, which premise fails (Def O1.2),
(iii) it states in writing why it is not h*, tests with ζ coefficients, inversion via Möbius, or the R_Λ pairing of
V_001/B_001/E_001.

## 7. Verdict

| piece | review label |
|---|---|
| P1.a, P1.b | PROVED (necessity; consequence of A∞) |
| P1.c | OPEN — the only open tool with non-REF-D content |
| (2.1) | CONDITIONAL on P1.c (Haynsworth CITED) |
| P2a G_kl | PROVED (elementary); technical tool |
| §5.3 c_k, ‖χ‖² | PROVED; integrable |
| P3 even/odd | PROVED, **REWRITE** of lem:polarelim; integrate only the canonical form (R1) |
| E_G, β_T | PROVED but non-canonical; (R2) reduces them to 𝔢 |
| Φ_E | = −𝓕_T (P46) = −R_Λ (B_001); already indexed |
| (6.1) | PROVED given (1.4) (no CONDITIONAL); content = W^ev = 𝔞^♯ − 𝓕_T; slack = artifact |
| m − σ_T ≥ 0 | NO-GO PROVED, corollary of cor:H1minus |
| 𝔅_T ≽ 0 | REF-D |
| L205.★ | REF-D at birth (K2): compression of prop:sharp(ii) to E_N^ev ∩ P_T; withdraw |
| P4 table | PROVED as a reading; Epstein OPEN; no deciding power until a step exists |
| P5 | useful only for P1.c (inertia of the complement) and for the normalization typo |

**Integrable into P46 now:** (a) a remark after lem:polarelim with (R1) and the extension of prop:sharp(ii) to 𝒟_T with
the term −2(⟨F,ch⟩² − ⟨F,sh⟩²); (b) the coefficients c_k of χ_ev in the Dirichlet basis (alongside cor:H1minus or A∞).
The editor must verify (a) against the definitions of 𝔢, 𝓕_T and eq:Aform (done here: it matches). Do not integrate
𝔅_T, (6.1) as novelty, or L205.★.

**Exact instruction for the architect's round 2:**
1. Replace P3 with (R1) in both sectors; remove β_T/E_G or leave them as (R2); correct β = 1.90370 and t₀′ = 6.12587.
2. Relabel §6: (6.1) PROVED given (1.4), content = prop:sharp(ii) extended; P2b = REF-D (already indexed: B_001, V_001).
3. Withdraw L205.★. The skeleton is left without a sign node; state this.
4. Construction priority: P1.c (upper bound of A∞ on the complement of E_N^ev, with 𝔪 + Π, no zeros), with P5 as a
   calibrator for P1.c and not for K6.
5. Any new sign node must come with (i)–(iii) from §6 in writing, and with a prior check in the index of the terms
   "polarelim," "Poisson," "R_Λ," "Chebyshev remainder," "prop:sharp."

## 8. Entry for the index (ROUTES-TRIED-INDEX)

- **SKELETON_001 + AUDIT_205_SKELETON_001 (phase 205):** P3 "pole Green identity" M = E_G − (1+½sinh T)ℓ² PROVED but
  REWRITE of P46 lem:polarelim; canonical form M = 𝔢 − 2(⟨F,ch⟩² − ⟨F,sh⟩²) on all of L²(I_T). Φ_E = −𝓕_T (prop:sharp) =
  −R_Λ (B_001/V_001). (6.1) 𝔅_T = Z_T + (½sinh T − 1)ℓ² PROVED, slack = boundary artifact. L205.★ = compression of
  prop:sharp(ii) to E_N^ev ∩ P_T: REF-D (K2), withdrawn. New and useful: c_k of χ_ev, G_kl closed; OPEN P1.c.
  m − σ_T ≥ 0: NO-GO (cor:H1minus). Do not retry "energy of the pole potential + Chebyshev remainder" as a sign object.
  Row D OPEN.
