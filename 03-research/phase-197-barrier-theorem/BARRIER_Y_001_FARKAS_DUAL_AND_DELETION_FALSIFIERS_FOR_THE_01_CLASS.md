# BARRIER_Y_001 — Track Y: Farkas dual of the {0,1}-majorization cone; the class is falsified by its own deletions

No audit yet. We assume
positivity of 𝔞_T on P_T. Labels used: PROVED / NUMÉRICO / OPEN / NO-GO.
Normalisation (P47 l.3093): v_n = 2a(n)/√n. Write w_T(n) = 2c_{F⋆}(log n)/√n and g(q) := w_T(q)·log q = 2c_{F⋆}(log q)log q/√q.
lem:degen (P47 l.3249) gives μ_T(a) ≤ λ_A(T) − ⟨a−Λ, w_T⟩. Scripts: `scripts/y001_farkas_signs.py` (Galerkin),
`scripts/y001_mp_check.py` (independent check at 30 digits).

## 0. Corpus check and the new reason
Read: BARRIER_X_001 (X1, X3, X4), AUDIT_197_HOSTILE_3 (residue (ii); the X3(a) counterexample R_2 = 1−x^k+x^{k+1}),
and the index entries W-fam, Theorem X (R186_046), W-cont (R186_048), W-tail / N_003, cor:void, thm:finmod, F-deletion, F-delT,
SPEC_A, INV_U_001 U3, X4. I also used the Galerkin construction of phase-186 `r046_X.form_x` (P47 eq:Aform).
**New reason.** Residue (ii) of AUDIT_197_HOSTILE_3 is not in the index. It asks about the sign of c_{F⋆}(log q) on the top
layer 𝒬, and how that sign interacts with the finite decision family of X3(d). cor:void and thm:finmod handle deletion
classes at large T, or tail deletions Λ1_{n≥N}. Here the deletions are the class's own admitted moves: single top-layer prime
powers q ≥ 1/(2ε) at a fixed window, with Λ kept below √N. No index entry tests these.

## 1. The exact Farkas dual (PROVED)
**Class.** 𝓘_{01} with Bohr defect Δ ≤ ε, in the regime ε < 1/(2√N) of X1(b). By Lemma X0, any change at a level p^j < √N costs
more than ε, so b_{p^j} = 1 there. For each p, let k_p ≤ … ≤ K_p be its levels in 𝒬. In the window (p^{2k_p} ≥ N),
log R_p = Σ r_j x^j + O(x^{2k_p}), so d(p^j) = j log p · r_j **exactly (linear)**. Here r_j = b_{p^j} − b_{p^{j−1}} ∈ {−1,0,1},
and the steps alternate in sign starting with −1, because b moves along a {0,1} path that starts at 1.
In the coordinates δ'(q) = d(q)/log q:

- **Admitted moves (ε fixed).** These are products over primes of alternating paths. Each path has Δ = ½(∏_p(1+Σ_{j: r_j≠0} p^{−j}) − 1) ≤ ε.
- **Generators of cone(S_ε−Λ).** The first kind is −e_q (delete level q) for q ∈ 𝒬 with 1/(2q) ≤ ε. The second kind is e_{q'} − e_q
  (b drops at q = p^i and returns at q' = p^{i'}, i < i', both in 𝒬) when ½(p^{−i}+p^{−i'}) ≤ ε. Longer alternating paths are
  sums of these. Products over different primes are sums when they are admitted.
- **Dual cone.** cone(S_ε−Λ)* = {y : y(q) ≥ 0 for admitted q; y(p^i) ≥ y(p^{i'}) for admitted pairs}.
- **Farkas condition.** cone(S_ε−Λ) ⊆ {⟨·,w_T⟩ ≤ 0} holds iff g ∈ cone(S_ε−Λ)*. Written out, it is
  (F1) c_{F⋆}(log q) ≥ 0 for every admitted q ∈ 𝒬, and
  (F2) log(p^i)c(log p^i)/p^{i/2} ≥ log(p^{i'})c(log p^{i'})/p^{i'/2} for each admitted pair of levels of the same p.
  (F2) is non-empty only when p < √N has two levels in 𝒬. The first instance is p = 2 with {4, 8} at T ∈ (½log8, log4].
- **Inhomogeneous form.** This is what S_ε ⊆ H_T actually needs: g(q) ≥ −λ_A(T) on generators, and g(q) − g(q') ≥ −λ_A on pairs.
  Since λ_A ≤ 3.1·10⁻¹² past ½log5 (P47 App. num), it is (F1)–(F2) up to 10⁻¹².
This matches the X3(b) divisor-cone dual restricted to 𝒬. The audit's correction is built in: (F2) is exactly the face that
the counterexample R_2 = 1−x^k+x^{k+1} creates.

## 2. The signs
**Analytic (PROVED, from X4).** If F⋆ is even and has no zero in (T−δ, T), then (F1) holds for q ∈ (Ne^{−δ}, N). Nothing
analytic reaches the bulk of 𝒬. Theorem X / W-lin say every first-order quantity is a functional of h*, and that applies here.

**NUMÉRICO (Legendre Galerkin, M = 40/56/72/80, P47 eq:Aform):**

| T | 𝒬 | sector of F⋆ | c_{F⋆}(log q), q ∈ 𝒬 | (F1) |
|---|---|---|---|---|
| ½log3 | {2} | even | +0.151 | holds |
| log2 | {2,3} | even | +0.074, +0.012 | holds |
| 0.75 | {3,4} | even | +0.017, +4.6e-6 | holds |
| ½log5+0.01 | {3,4,5} | even (gap 2.3e-10, stable in M) | +2.27e-2, +3.5e-5, +1.0e-11 | **holds** |
| 0.9, 1.0, log3, ½log11−0.01 | … | **unresolved** | signs change with M | undecided |

For T ≥ 0.9 the Galerkin bottom is λ_A ≈ 10⁻¹⁴, below double precision. The two parity sectors are degenerate to within
10⁻¹⁴, and the eigenvector, and with it every c(log q), changes with M. Fixing the signs would need a parity-resolved
computation in multiprecision. **That is unnecessary, because of §3.**

## 3. The decision family fails: deletion falsifiers inside the class (NUMÉRICO; NO-GO for the class)
The class decides T only if WP_T(Λ_Q) holds for every admitted Λ_Q (X3(d)). Galerkin values are upper bounds for the
bottom, so a negative value means WP_T(Λ_Q) fails:

| T | q (cost 1/(2q)) | λ_A(T; Λ − q) Galerkin, M=40 → 72/80 |
|---|---|---|
| log2 | 3 (1/6) | −0.0828 → −0.0828 |
| 0.75 | 3, 4 | −0.244, −0.0606 |
| ½log5 − 10⁻⁴ | 3, 4 | −0.371, −0.0995 |
| ½log5 + 0.01 | 3, 4, 5 | −0.395, −0.102, −2…−3·10⁻⁴ |
| 0.9 | 3, 4, 5 | −0.594, −0.268, −0.215 |
| 1.0 | 3, 4, 5, 7 | −0.632, −0.330, −0.383, −0.129 |
| log3 | 3, 4, 5, 7, 8 | −0.634, −0.343, −0.587, −0.318, −0.107 |
| ½log11 − 0.01 | 4, 5, 7, 8, 9 | −0.346, −0.707, −0.501, −0.172, −0.184 |

All multi-deletions Λ_Q and the two-level path −e_4+e_8 are also negative (−0.1 to −0.84; see the script output).
Sanity check: at ½log3, deleting 2 gives +0.0825, which is the empty comb.
**Independent check:** I took an explicit polynomial F ∈ P_T, re-imposed the Tate moments exactly in mpmath, and evaluated
P47 eq:Aform directly at 30 digits. The Rayleigh quotients are −0.232424618789 (T = 0.75, q = 3) and −0.385182962856
(T = ½log5+0.01, q = 3), −0.0401656414828 (T = 1, q = 7), −0.0179270129691 (T = log3, q = 8; M=14 test vectors). All four agree with Galerkin to 10⁻¹¹. A certificate in ball arithmetic of one test function per
window (margin ≥ 0.017 with M=14 vectors) is routine but has not been done. **Label NUMÉRICO.**

**Theorem Y1 (structure PROVED; the inputs λ_A(T;Λ_q) < 0 are NUMÉRICO).** Fix T in the tested set. For the class 𝓘_{01}
with defect ε there are three cases:
(a) If ε < 1/(2 max𝒬), then π_N S_ε = {Λ}. This is pinning, REF-D.
(b) If ε ≥ 1/(2q) for some q ∈ 𝒬 with λ_A(T;Λ_q) < 0, then S_ε ⊄ K_T and the method is unsound at T: **NO-GO**. In the
tables, every q ∈ 𝒬 qualifies, so (b) covers all non-pinning ε.
(c) There is no third case. The Farkas condition (F1) **holds** at ½log5+0.01 and still (b) applies. So (F1)–(F2) is
necessary for S_ε ⊆ H_T, but it is irrelevant to S_ε ⊆ K_T. H_T is only the supporting half-space at Λ, and admitted moves
are O(1) in v (k log p·2/√q ≈ 0.4–1.3), far outside the region where the first-order tangent applies. The concave μ_T falls
from about 10⁻¹² to about −0.1…−0.7 along every deletion.

**Consequence.** Residue (ii) closes. The sign of c_{F⋆}(log q) does not decide anything for this class. Wherever it can be
read (even sector, T ≤ ½log5+0.01) it has the good sign, and the class is falsified anyway. That includes windows
T ≤ ½log5, where WP_T(Λ) is certified, so the defect is in the method and not in the window.
**ℤ-specific? No.** The mechanism is that in a near-critical window, removing an O(1) top contact is an O(1) indefinite
perturbation of 𝔞_T. That is the cor:void / thm:finmod mechanism, here at the scale of a single atom and fixed T. It uses
only λ_A ≈ 0 and v_q = O(1), not integrality or ℤ. Integrality matters only in that it makes the admitted moves O(1)
rather than infinitesimal, which is why the class lands on falsifiers. **NO-GO 𝒦_Y^{01}**: "a {0,1}-majorization (b ≤ b(ζ))
Euler class with any FE defect ε ≥ 1/(2 max𝒬)" is falsified at every tested T ∈ [log2, ½log11) by its own single deletions.

## 4. Status
§1 Farkas dual: PROVED. (F1) at ½log3, log2, 0.75, ½log5+0.01: NUMÉRICO, holds. (F1)/(F2) at T ≥ 0.9: undecided in double
precision, and moot. Y1: structure PROVED, inputs NUMÉRICO (mp check of 4 cases; arb certificate OPEN, routine). NO-GO
𝒦_Y^{01}. What would survive needs a class whose admitted moves are infinitesimal at Λ (so lem:degen/first order governs),
and that is a cone premise, which is BARRIER_001 Thm 3 → REF-D⁺. No sign. Row D: OPEN.
