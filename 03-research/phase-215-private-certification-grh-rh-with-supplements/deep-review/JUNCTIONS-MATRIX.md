> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# Junctions matrix: identity, hypotheses and dependencies

Status: 28-11-2026. This matrix updates the historical pending items of `../05-junctions.md`. Sources: local `main.tex` files, inventory `../evidence/shared_statements.json` and deep ledgers. "Junction (a)" means that the transfer of the result and its hypotheses were checked; **it does not turn a defective proof of the imported result into a correct one**. The errors of P53 propagate as lack of justification of the route, not as demonstrated falsity of each descendant conclusion.

## What the textual inventory measures

The JSON records environments with the **same label**; not all the imports keep the label. For example, `au:regular` appears there at 46:4921 and 58:4911, but its mathematical source in 55 is `pg:main` (55:440), `pg:sums` (493) and the deduction 535–545. Hence there is no automatic comparison 46↔55 that would authorise saying "identical".

The following automatic differences were inspected: `pg:III` 55:648/58:22611; `pki:data` 56:486/58:58602; `pki:data-sizes` 56:500/58:58616; `pki:align` 56:638/58:58754; `pll:status` 55:3511/58:25471. They are substitutions of external references by internal references; they do not change the formulas or hypotheses of those environments. By contrast, `pg:main`, `pg:I`, `pg:II`, `pg:loss`, `pg:odd`, `pll:exponent`, `pki:generic`, `pki:tame`, `pki:crys` and `pkw:G4` are equal after normalisation in the pairs 55/58 or 56/58. That fact only certifies the copy of the statement, not all the definitions of its macros nor its applications.

## Junctions 54–56 and return to 46: direct inspection

| Origin → destination | Identity of the imported content | Hypotheses and range checked | Status and obligation that remains |
|---|---|---|---|
| 55 `pg:main` + `pg:sums` → 46 `au:regular` | Deduction, not literal equality. R1=(a), R2=(b), R3=(c),(d). | 55:535–545: θ_ι=τ, both signs and all powers 1≤j≤m. β(ℓ)=(β_ℓ+v_ℓ(h₁))logℓ; false lifts and test forms are preserved. | **(a) the conditional junction.** The integral input is not closed: it depends on IM54 and multiplicities, and requires correcting the sentences of P55 described in SELMER §§6,11. |
| 54 `pex:IM`/`pex:IM1` → 55 `pg:poly`, `pg:stick`, `pg:II` | The finite expansion in characters, integrality at ι and ι∘c, quotient of values and omitted Euler factors are preserved. | SELMER §13: n_p may depend on the critical pair, but not on θ,Q; v₀ cancels. Includes ℓ=d, all j≤m and enlargements of the modulus. Q is prime to ℓ. | **(a) transfer and deduction of II under IM.** For z≥2 norm and expansion were reconstructed; z=1 uses the exchange of 53 and is affected by its defective proof. Do not arbitrarily reduce II to the range z≥2. |
| 55 M2/G4 → 56 `pki:data`/`pkw:G4` | Weights, crystalline/tame classes and parameters identified, not a mere copy of names. | η=h²+1,W=4t,δ_j=jΔ+h−2t; duals −u−1; K(s⁻¹); q_s depends on s. Polynomials of degrees ≤N,≤N,≤N² and e₀≤ℓ^(r²). | **(a) conditional junction**, HODGE §6 and SELMER §§6,12. In P55 there are incorrect sentences on norms of fields and orders; the corrections do not increase the bounds. The correct polynomial of P56 does NOT repeat the error of a fixed polynomial for all s. |
| 56 `pki:crys`, tame, data → 55 `pll:exponent` | Same four cases and constants; exponent is not confused with length in case (d). | HODGE §§1–6: all ℓ by means of the authorised alternatives; NM for λ<h³, cut λ≥h³, duals and lattices. SELMER §14 verifies the passage to D_ℓ and the sum over places. | **(a) junction and local segment** under the declared data of P46 and the classes M2/G4. Fontaine–Laffaille is not needed as a hidden input. |
| 55 `pll:ribet`, `pll:dual` → classes used in 56 and return to `pri:loss` | The class of cocycles is the one produced by lattices u_x and the length is normalised by [O:Z_ℓ]. | One does not average integrally by dividing by the order of the group; crystalline exactness is used rationally where appropriate. The rank of Z_f only multiplies the exponent cases. | **(a)**, SELMER §§1–4 and HODGE §§5–6. It is not an omitted residual irreducibility hypothesis. |
| 53 lattice/Gram → 55 pairing and Higman | Restriction of the standard tensor form, not an undetermined scale. | COVOLUME, "Junction 53→55"; SELMER §11: integral dual e_T and G=H_μF_μ⁻¹. Stabilisers eliminated by N_ch. | **(a) this algebraic junction**, independent of the exchange of 53. To apply denominators in e_c, make base level precise and use a construction preserving e_c; explicit repair in SELMER §11.2, not incorporated into the paper. |
| 55 `pg:odd` and sums → regular budget of 46 | Same C_odd,e_ℓ,e′_ℓ,β_ℓ and logℓ. | Odd classes for ℓ=2 included; Σλ_ℓlogℓ≤3b log b and Σb v_ℓ(M)logℓ≤22b log b. | **(a) assembly** SELMER §§7,14. Its correctness does not resolve the exchange/multiplicities inputs. |

## Mutual citations: bibliographic cycle versus logical cycle

**55↔56: no logical cycle was identified in the reconstructed segment.** P56 receives definitions of lattices, weights and classes from P55, whose construction M2/G4 precedes the loss bound. It produces the local exponents; P55 afterwards applies duality and sum. In particular the mention of `pll:main` in `pki:data` is used to identify L_c and C_v, not to assume the conclusion δ_v≤D_ℓ which P56 has to prove. This was checked in HODGE §6 and SELMER §§6,12,14; it is not merely a declaration of the author.

**53↔54: bibliographic reciprocity is not enough to assert circularity either.** The inner product formula `pc:SW/pc:rallis` of P53 used in P54 was reconstructed in THETA SW01 independently of exchange; it returns to P53 by means of the explicit formula for a lift. The exchange of 53, by contrast, enters in addition in z=1 of IM54. The audited branch exhibits a **failure of an identity**, not a demonstrated logical cycle. The bounded descent of tower and all the transitive imports are not certified by this analysis of order.

**46↔55/56:** the admissible data and sizes of 46 are received before concluding regularity. Regularity is not used in the local checks of those sizes. This rules out the supposed cycle at that particular junction, but does not certify the global existence of the data nor all the dependencies of 46; see its analytic audit.

## Propagation of the character error of P53

The failure **(b)** is in `pcu:product`, 53:3351–3360; α(det g)α(det y)β(det l) is missing. In `pcu:period` β(det u) appears inside the integral. The modulus one does not allow it to be removed. See [complete computation](ERROR-53-CHARACTERS.md).

| Branch | Impact proved | What does not follow |
|---|---|---|
| product→period→coeff→P-top→P-std→exchange `pcx:X` | That written route does not prove the exchange. The period and its non-vanishing must be recomputed and L_* preserved. | It is not a counterexample to the exchange statement. |
| exchange→54 z=1→IM1→55 II→regular 46 | The justification of that branch receives the unproved input. The collation of the hypotheses of IM and its use remains valid conditionally. | It has not been proved that all the pairs actually used can exclude z=1. |
| exchange→53 factorisation/covolume→46 | The chain is not certified by this proof. | It does not imply that each descendant equality is false. |
| 53 inner product SW/Rallis→54 z≥2 | The review SW01 finds an independent route; the doubling uses tensor with the conjugate and cancels the characters. | The closure is not extended to all non-compact sources nor to the whole tower. |
| 53 Gram→55; local theory of 56 | They do not use the defective identity. Their local closures remain. | They do not by themselves reconstruct regularity or GRH. |

The other failures of 53 have a different scope: P=∅ is corrected by requiring non-empty, already satisfied in exchange by m≠(1); pointwise evaluation is not Hilbert-bounded and needs the moment/Schwartz norms. They must not be grouped with the character error as if one and the same repair resolved all three.

## Remaining branches and limits of this matrix

The theta review confirmed the following statuses, collated with THETA; this matrix does not repeat that independent inspection:

| Junction | Verdict reported and exact obligation |
|---|---|
| 49→50→49 | Abstract application reconstructed in HE01: root/count/av and applicable range. There is no new pending item on range identified at this junction. |
| 49→54 | Kernels, CS/CM constant and divisibility reconstructed in CM01/KI01/LN01/BR01/AS01. The strong formula for δ_g is not proved literally, but the properties used are derived independently; the two assertions must not be confused. |
| 53 SW/Rallis→54 Prop.3.4→53 CL | SW01 reconstructs z≥2 without exchange or CL. Thus this route is not circular. The complete closure of CL requires in addition its other steps; see COVOLUME. |
| 54→55 | IM for z≥2 and the deduction from IM are reconstructed; z=1 continues to depend on the defective exchange of 53. |

 For 52→51 and multiplicities 51→46/53/55, see SPANNING and MULTIPLICITIES: a closed local bound does not certify the global trace. For 43–45→46, see the report on the rows and COMPLETION-FORM-43/HOCHSCHILD-43; their interpretation does not replace the positivity of 46.

**Status of a junction not individualised or not traversed in the ledgers: (c).** Exact general pending item: identify the complete source statement and the definitions of its symbols, check measures/lattices/constants/ranges in the instance and trace that its proof does not presuppose the destination conclusion. The TSV performs none of those three tasks. Neither the complete network nor a universal absence of circularity is declared closed.

## Exhaustive collations added

[JUNCTIONS-THETA](JUNCTIONS-THETA.md) identifies 275 reproductions of the appendices 49/50/53/54, with collation of bodies, transitive macros and TeX references. [JUNCTIONS-SPANNING](JUNCTIONS-SPANNING.md) identifies 51 reproductions of 51/52, with complete inspection of their 21 differences of format/references. The fidelity status of a copy is kept separate from the status of its application and from the correctness of the source proof. The inputs H/Hc/F of the chain of 53 were reconstructed subsequently in [CHAIN-53§6](CHAIN-53.md); RS/T1 retains the dependence on the defective exchange.
