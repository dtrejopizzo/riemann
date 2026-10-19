# CA_A_002 — Candidate (a): Lewis–Zagier period functions / Mayer transfer operator as sign carrier

Phase 193. Pen and paper.

## 0. Corpus / index check
06_OPEN_RESIDUES "Lewis–Zagier route" OPEN (never attempted); P152 (R152_001/002): Dolgopyat–Mayer branch series,
abscissa ½, DEAD as overstated; G1H-152 P152.1 (Dolgopyat bound via Lewis–Zagier) OPEN-RESIDUE, no method. This memo is the
first attempt.

## 1. Data (CITED: Mayer 1991; Lewis–Zagier, Ann. Math. 2001)
Mayer: (L_s f)(z)=Σ_{n≥1}(z+n)^{−2s} f(1/(z+n)) on holomorphic functions on the disc |z−1|<3/2; nuclear for Re s>½,
meromorphic continuation; Z_Selberg(s)=det(1−L_s)det(1+L_s). Lewis equation ψ(z)=ψ(z+1)+(z+1)^{−2s}ψ(z/(z+1)) ↔
period functions of Maass forms with spectral parameter s; for E(·,s) the period function is
ψ_s(z)=ζ(2s)(1+z^{−2s})+Σ_{m,n≥1}(mz+n)^{−2s} (+ explicit correction; Lewis–Zagier §IV, CITED, form to be checked).
Zeros of Z_Selberg: s=½+ir_j (cusp forms), s=ρ/2 (scattering, from φ), trivial ones.

## 2. Pre-screen
| clause | verdict | reason |
|---|---|---|
| spectral parameter ↔ ζ line | NO | same line doubling as CA_A_001 Lemma 1: ζ(2s) ⇒ ζ(½+iτ) at Re s=¼ |
| positivity available | only real s>½ | L_s positive (Ruelle–Perron–Frobenius) only for real s; at Re s=¼ no positive cone is preserved (CA_A_001 Lemma 2 for invariant forms; for cones: L_s with complex weights (z+n)^{−2s} does not preserve any proper cone of real functions — ARGUED) |
| (4) zero side | NO | ζ enters det(1∓L_s) only via resonances s=ρ/2 ([zeros]) |
| (3) non-linear in Λ | NO-content | Λ does not enter at all: L_s is built from ℤ (continued fractions) only; ζ(2s) appears through Σ_n n^{−2s}, i.e. the coefficients 1, never Λ except through log det |
| (11) ζ-specific | partly YES | DH has no transfer operator (index note); but ζ_K (Hilbert modular / Bianchi transfer operators exist, CITED in outline) ⇒ O12 survives |
| (8) near-coincidence | nominal YES | Σ(mz+n)^{−2s} sums over ℤ² near the line n≈−mz — but at z>0 there is no cancellation, all terms positive; the "near-coincidence" is only realised at z<0, outside the Mayer disc |

## 3. What was built (PROVED, elementary)
**Prop 1.** For real z>0 and real s>½, every term of L_s and of Σ_{m,n}(mz+n)^{−2s} is positive; for s=¼+iτ/2,
(mz+n)^{−2s}=(mz+n)^{−½}e^{−iτlog(mz+n)}, and the period function's ζ-dependent part is the 2-dimensional Dirichlet series
Σ_{m,n}(mz+n)^{−½−iτ}, which at z=1 equals Σ_N (N−1)N^{−½−iτ} = ζ(−½+iτ)−ζ(½+iτ) (formal; continuation).
*Proof.* Counting pairs m+n=N. ∎
So at z=1 the period-function data are linear combinations of ζ at shifted points — no quadratic form, no sign; at
general z they are Epstein-like values of the indefinite-free form (mz+n) — Hurwitz/Barnes double zeta, which survive
every comb modification because Λ is absent (lem:shape-ident applies trivially: the object does not depend on the comb).

## 4. Result
**NO-GO for (a) as sign carrier (ARGUED overall; Prop 1 and the line-doubling step PROVED).** The Lewis–Zagier/Mayer
structure encodes ℤ-integrality and FE, but (i) it sees ζ through ζ(2s) (line doubling), (ii) it sees Λ only through
log det, i.e. through zeros (clause 4), (iii) positivity (Perron–Frobenius) lives only on real s. The index entry
"Lewis–Zagier route" moves from OPEN (never attempted) to NO-GO (ARGUED, this memo), with the precise reason
"positivity only at real s; ζ on the critical line sits at Re s=¼; Λ enters only via det = zeros".
Residue: P152.1 (Dolgopyat bound) unaffected — it is an estimate, already outside (11) by (B′).

## 5. Self-review
- One could use the even/odd split det(1−L_s)det(1+L_s) and the sign of the factor ζ-part; still zero side.
- One could use L_s at real s and a Mellin transform in s to reach the line: that is an integral over s of positive
  operators against a non-positive kernel — positivity lost; estimate with remainder → (B′).
- Verdict stands. No negative value for ζ.
