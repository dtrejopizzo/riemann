# CA_H_SYNTHESIS — Front H (the semiring (ℕ,+,·) as the source of the sign), phase 193

 Pen and paper; no numerics. **No sign contact. No negative value for ζ. No clause of (R) moved.**
Memos: CA_H_000 (10 seeds, full screens, fact H0), CA_H_001 (δ-structures: H1, H3, H8), CA_H_002 (semiring invariant and Kronecker
anatomy: H5, H6), CA_H_REVIEW.

## Verdicts
| seed | verdict | killing clause |
|---|---|---|
| H1 Buium δ_p, arithmetic Wronskian | developed; NO-GO | Cor 2.3 (archimedean height ×p, no degree drop); δ-log of ζ is monoid-functorial exponent deletion (Cor 3.4), split bounded/REF-D (Prop 3.5); δ-calculus on tests (B″) (Lem 4.1) |
| H2 Stepanov over ℤ | DISCARD | retry G1_B9 Lemma 3, Thm 3′ |
| H3 carries / Witt | DISCARD (folded in H1) | form carry-blind (001 §1.4); P44-1, G4H-159 |
| H4 sum-product (Erdős–Szemerédi, Solymosi, multiplication table) | DISCARD | real-set statements survive O11/O15, ignore weights, (B′), [crit] |
| H5 semiring invariant | developed; PROVED invariant, not a sign step | (S⁺) separates ζ from O1–O3, O5, O6, O8, O10–O12, O15; blind to O4, O7, O9, O14 ⇒ Cor 2.3 |
| H6 Kronecker line (front E) | developed; PROVED anatomy, REF-D | Near = ∫g d(ν₀ − Haar); anatomy is (additive weight) × (monoid coefficient), linear in Λ, (B″) |
| H7 integrality gap / Liouville | DISCARD (retry) | thm:ceiling one-sided; phase 163/164 |
| H8 polarized object from global Frobenius lifts (G-F bridge) | developed; NO-GO for class 𝒦_δ | genus ≥ 2: no Frobenius lift (degree argument); genus 1: none over ℤ; G_m/P¹: content-free (Γ_n·Δ = n+1, H¹ = 0) |
| H9 divisibility of N ≍ M by small n | DISCARD (retry) | SPEC_B Line 3; REF-D for η ≤ η₀ |
| H10 arithmetic derivative | DISCARD | G1 |

## PROVED facts (usable elsewhere)
H0. +/· test: monoid-only ⇒ O11/O12 survive; comb-only ⇒ O7 survives (PROVED); additive-only ⇒ FE-gen (ARGUED, per-property check needed: x²+5y² has conductor 20).
H-δ1. δ_p(n) = (n−n^p)/p is the unique p-derivation on ℤ; it lowers v_p by one and only at p; it multiplies the archimedean height by p.
H-δ2. W_p(a,b) = ab(a^{p−1}−b^{p−1})/p; the Mason identity fails exactly by the carry: W_p(a,a+b) − W_p(a,b) = a·C_p(a,b).
H-δ3. D_ℤ is a Λ-ring (φ_p f(s) = f(ps)); δ_pζ has coefficients (1[n=m^p] − d_p(n))/p; the δ-logarithmic derivative of ζ is the comb
      Λ·1[not a p-th power] = −ζ′/ζ(s) + ζ′/ζ(ps); every δ-operation on Euler products is monoid-functorial.
H-δ4. Class 𝒦_δ (global Frobenius-lift correspondences on curves over ℤ) has no member with H¹ ≠ 0; its members are content-free.
H-S.  (S⁺): a comb on prime powers has successor-continuous divisor sum iff a = cΛ (Erdős, CITED). Enters the form exactly on the
      collapse class (Prop 2.4) as a Riemann sum over consecutive integers; non-critical there.
H-K.  (extends CA_C_002 Prop 2 from boxes to Ĝ) Div = ∫g_s dHaar, Div + Near = ∫g_s dν₀ on Ĝ = (ℚ_{>0}^×)^; s^T𝔸_Ms = Σ_{q∈G}[α(log q)N_s(q) − c₀(log q)M_s(q)].
H-T.  The line measure's mass beyond the integer Nyquist frequency M is ≍ M^{−3} (proved); it matches [crit] (reading ARGUED).

## Proposed YES→NO moves (pending review)
- "Buium p-derivations / arithmetic Wronskian supply the derivation of the function-field proofs over ℤ" → NO (001 Cor 2.3, Lem 4.1).
- "a polarized object built from global Frobenius lifts closes G-F (a)+(c)" → NO-GO for 𝒦_δ (001 Cor 5.4); MW-5 by other correspondences untouched.
- "the semiring invariant of ℤ, used as a property of the comb, carries the sign" → NO (002 Cor 2.3: O7).
- "Kronecker/Bohr–Jessen structure of the line carries the sign as an exact identity" → NO: the only identity is Near = line − Haar, (B″),
  linear in Λ; its sign content is (K), REF-D (002 Cor 3.5).

## What remains (for the record, not a candidate)
The semiring interplay of the window form is fully described by Theorem 3.2: a pairing of additive-only weights at log q with
monoid-only coefficients at q ∈ G, linear in Λ. A +/· sign step therefore needs a non-linear input that is neither the minimizer
(REF-D) nor a property of the comb alone (O7). On the δ side, the archimedean place charges every p-derivative its Frobenius degree,
and no curve with H¹ carries global Frobenius lifts. No object in this area supplies the missing input. Area exhausted; front H stops.
