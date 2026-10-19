# CA_A_004 — Review

## Verdict
**EXCLUDED (object comb-independent ⇒ O1–O7, O15 survive; O12 survives in outline; (R)(1),(2),(8),(11)). Prop 1 CONFIRMED; Cor 2 CONFIRMED as a reduction (the exclusion via (B′) is ARGUED); Cor 3 ARGUED — FIX: thm:sos concerns squares of Dirichlet polynomials in the window calculus; squares of smeared L_D(½+2it) are not literally in its class. Addendum R1 accepted; R3 inherits the CA_B_005 non-sequitur — FIX.**

## 1. Claims
| claim | check | label |
|---|---|---|
| §0 DIT (2.24)–(2.25): b₀(Dm²,s) ∝ L_D(2s−½)/ζ(4s−1)·(finite); unitary axis Re s=½ (eigenvalue (s−¼)(¾−s) real ⇔ Re s=½) | at s=½+it: (s−¼)(¾−s)=(¼+it)(¼−it)=1/16+t² ✓; L_D(½+2it) ✓; constant term ζ(4s−2)/ζ(4s−1) = ζ(4it)/ζ(1+4it) ✓ | CITED (verified) |
| Prop 1: per-n kernel rank one | Parseval term |∫h g_n|² ✓ | CONFIRMED PROVED (trivial) |
| Cor 2: matching a multiplication operator needs a resolution σ_Tδ = Σg_n ḡ_n | ✓ as a necessary condition | CONFIRMED; "⇒ estimate (B′)" ARGUED (an exact Kuznetsov-type resolution is not excluded — memo §5 says so) |
| Remark 4 | |ζ|² vs Re ζ′/ζ: second-moment data, (S)/EI_002 | CONFIRMED, REF-D for that reading |
| Remark 5 (Waldspurger diagonal) | CITED in outline | CITED |

## 2. Modifications
No Λ in the object: O1–O7, O15 leave it unchanged ⇒ lem:shape-ident pattern ⇒ **EXCLUDED**. O12: Shimura-type half-integral Eisenstein over totally real K (CITED in outline) — survives. O11: no weight-½ binary analogue — destroyed (memo ✓), irrelevant given the above. O8 keeps everything — survives.

## 3. (R): (1),(2) (mixes every χ_D, conductor > 1),(3),(8),(11) not met; (4) met. Agree.
## 4. REF-D: the diagonal/second-moment reading is (S) (REF-D). Otherwise no sign.
## 5. Retry: G6B-R162_502 (Hecke equivariance), phase 192 EI_002; Salié/Kuznetsov variant new, OPEN-RESIDUE (low): exact trace formula valid for every spectrum on Γ₀(4) ⇒ comb-independent ⇒ (B″) unless a Salié-side inequality fails for a_P.
## 6. On Addendum R3
"An exact identity singling out Λ cannot be the sign carrier" (from openness) — not endorsed (see CA_B_005 review §2). The correct constraint is O8 + (B″): the property must couple to the form/minimizer. The next candidate (minimizer Dirichlet polynomial in a Rankin–Selberg integral) is the right direction; pre-flag: Petersson positivity of |Σb_mE|² is a norm ⇒ holds for every b (comb-generic in b) — must show what in it fails for O2/O8.
Endorsed: "metaplectic Parseval carries the σ_T-correlation inside P_T" → NO; "line doubling is a general barrier" → withdrawn ✓.
