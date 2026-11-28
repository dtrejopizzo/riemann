> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the other results are being consolidated.

# Junctions of the appendices of P55 and P56

Date: 28-11-2026. Object: **fidelity of all the statements reproduced in the appendices of P55/P56**, collated with their local sources. There are 45 entries (26 in 55, 19 in 56), corresponding to 43 distinct source statements: Definition 13.3 of 46 appears twice in 56 and Lemma 13.4 of 46 appears in both papers. Mere bibliographic mentions in prose are not counted as reproduced statements.

**Fidelity result: (a) in the 45 entries.** There are 23 coincidences after normalising spaces and removing labels/environment titles; the remaining 22 only replace internal references by external numbers —or conversely— and, in two cases, convert a numbered equation into an equation with an explicit label. These 22 differences were inspected by hand. None removes a hypothesis, or changes an inequality, a quantifier, a constant or a range. This does **not** grant (a) to the proof of each result nor to every later use.

Reproducible evidence: [complete pairs](../evidence/junctions_selmer_hodge.json), [extractor/comparator](../evidence/audit_appendices_selmer_hodge.py). The comparator does not by itself establish mathematical equivalence: here the differences were reviewed. The lines are those of `main.tex` in the local revision audited. “Exact” does not mean byte-for-byte identity: spaces and labels are normalised.

## Complete inventory

In all rows the verdict on the **copy** is (a). The differences indicated are exclusively of references/presentation. The conditions of application are separated below.

| Destination:line | Source:number (line) | Source label | Copy / difference inspected |
|---|---|---|---|
| 55:7739 | 46:13.4 (2989) | `an:lem-sizes` | Reference §14.3 of 46 |
| 55:7777 | 46:14.5 (3598) | `au:free` | Exact after normalisation |
| 55:7782 | 46:14.27 (4584) | `au:equiv` | Exact after normalisation |
| 55:7789 | 46:14.36 (4812) | `au:mult` | Exact after normalisation |
| 55:7801 | 46:14.37 (4850) | `au:factor` | Exact after normalisation |
| 55:7816 | 46:14.39 (4895) | `def:au-regular` | Exact after normalisation |
| 55:7837 | 46:14.40 (4921) | `au:regular` | Exact after normalisation |
| 55:7841 | 46:14.41 (4965) | `au:onelift` | Exact after normalisation |
| 55:7857 | 46:14.42 (4992) | `au:hecke` | Exact after normalisation |
| 55:7862 | 46:14.43 (5013) | `au:Zj` | Exact after normalisation |
| 55:7867 | 49:5.2 (3428) | `ps:weil` | References eq.62, Prop.2.17, §5.2.1 and Rem.7.18 of 49 |
| 55:7916 | 53:3.2 (1767) | `pcx:X` | Label/environment eq.12 and reference §2.3 of 53 |
| 55:7940 | 53:5.26 (9837) | `pgs:pairing` | Reference Lemma5.25 of 53 |
| 55:7958 | 54:2.2 (544) | `po:facts` | Reference eq.1 of 54 |
| 55:7971 | 54:3.6 (1827) | `pex:dint` | Exact after normalisation |
| 55:7978 | 54:3.8 (1898) | `pex:IM` | Exact after normalisation |
| 55:7992 | 54:3.12 (2038) | `pex:IM1` | Reference Lemma3.6 of 54 |
| 55:8001 | 56:2.4 (416) | `pki:def-reads` | Exact after normalisation |
| 55:8011 | 56:2.5 (436) | `pki:generic` | Exact after normalisation |
| 55:8023 | 56:2.10 (486) | `pki:data` | Prop.5.2 of 55 becomes an internal reference; Prop.2.8 of 56 |
| 55:8037 | 56:2.13 (552) | `pki:crys` | Reference Lemma2.12 of 56 |
| 55:8054 | 56:7.1 (5892) | `pkj:conv` | Two references Prop.2.9 of 56 |
| 55:8073 | 56:7.9 (6095) | `pkj:chart` | References Conv.7.1 and Def.2.4 of 56 |
| 55:8080 | 56:9.2 (7399) | `pkw:def-pcris` | Two references Lemma9.3(i) of 56 |
| 55:8090 | 56:9.9 (7594) | `pkw:T2` | References Defs.9.5 and 3.4 of 56 |
| 55:8098 | 56:9.23 (7937) | `pkw:G4` | Exact after normalisation |
| 56:8002 | 46:13.2 (2930) | `an:def-sparse` | Exact after normalisation |
| 56:8013 | 46:13.3 (2954) | `an:def-data` | Exact after normalisation |
| 56:8047 | 46:13.3 (2954) | `an:def-data` | Exact after normalisation |
| 56:8081 | 46:13.4 (2989) | `an:lem-sizes` | Reference §14.3 of 46 |
| 56:8119 | 55:2.5 (493) | `pg:sums` | Reference Prop.2.27 of 55 |
| 56:8128 | 55:2.6 (563) | `pg:def-summand` | Exact after normalisation |
| 56:8151 | 55:2.28 (1383) | `pg:loss` | References Thm.2.10, Prop.4.5, Thm.5.8(d), Rem.5.7 of 55 |
| 56:8165 | 55:4.5 (2223) | `pri:loss` | References Def.2.7, Props.2.28 and 4.6 of 55 |
| 56:8192 | 55:4.6 (2260) | `pri:BL` | Reference Def.8.42 of 55 |
| 56:8207 | 55:5.1 (3213) | `pll:def` | Exact after normalisation |
| 56:8243 | 55:5.2 (3268) | `pll:main` | Reference Prop.2.28, label/environment eq.9 and §2.1 of 55 |
| 56:8260 | 55:5.4 (3354) | `pll:dual` | Exact after normalisation |
| 56:8269 | 55:5.5 (3408) | `pll:ribet` | Exact after normalisation |
| 56:8280 | 55:5.6 (3448) | `pll:exp` | Exact after normalisation |
| 56:8286 | 55:5.8 (3487) | `pll:exponent` | Reference Prop.5.2 of 55 |
| 56:8304 | 55:5.10 (3528) | `pll:sum` | Reference eq.9 of 55 |
| 56:8309 | 55:6.4 (3763) | `pga:depth0` | Exact after normalisation |
| 56:8322 | 55:6.6 (3938) | `pga:G45` | References Prop.6.2 and Lemma6.4 of 55 |
| 56:8341 | 55:8.27 (7092) | `pay:eta` | References Props.6.11 and 4.6(c) of 55 |

## Fidelity versus validity and range of application

The numerical references of the table were collated with the source environments. The equation numbers are identified by the corresponding source labels (`pl:eq-w5`, `pcx` exchange, `po:eq-w5`, `pll:eq-place`); the changes of presentation do not change their terms. The definitions are not replaced by weaker versions in these copies. For the meaning of the parameters in the effective applications, the reading of the main sections recorded in the following ledgers was also used.

| Group of imports | Result of the review of hypotheses/range and limit of the conclusion |
|---|---|
|46 sizes/data/sparsity →55/56|Same admissible data and sizes. The identification of letters and windows of 56 with the data of 46 is reconstructed in [HODGE §6](HODGE.md). Reproducing `au:regular`, `au:factor`, `au:onelift` or `au:Zj` does not prove those theorems nor by itself constitute a use as a premise.|
|46 `au:regular` in 55|The copy coincides; the result that 55 must contribute is deduced from `pg:main` and `pg:sums`, not from assuming its copy. The step R1–R3 was verified for both signs and j≤m in [JUNCTIONS-MATRIX](JUNCTIONS-MATRIX.md). Its global truth still depends on the inputs indicated there.|
|49 `ps:weil` →55|The conditions W and normalisation references are kept. The properties actually used were reconstructed in [THETA](THETA.md); the strong formula for the phase δ_g must not be confused with the weaker properties used. The fidelity of the copy does not remove that distinction.|
|53 `pcx:X` →55|**Correct copy of a statement whose written proof was not established:** the failure `pcu:product` is detailed in [ERROR-53-CHARACTERS](ERROR-53-CHARACTERS.md). It is not a change of range of the citation nor a counterexample to the exchange statement.|
|53 `pgs:pairing` →55|Identification of lattice and tensor form verified, independent of exchange; see [COVOLUME](COVOLUME.md) and [SELMER §11](SELMER.md). The restriction to e_c requires the base level precision/repair recorded there; it is not remedied by copying the lemma.|
|54 `po:facts`, `pex:dint`, `pex:IM`, `pex:IM1` →55|In the deduction of II both embeddings, integrality, omitted factors and all the critical pairs are kept. Branch z≥2 reconstructed; z=1 of IM1 depends on exchange 53. It was not verified that z=1 can be excluded from all the uses. [SELMER §13](SELMER.md).|
|56 `pki:def-reads`, `generic`, `data`, `crys`, conventions/charts →55|The copies keep NM and windows: no NM hypothesis suppressed in the transcription was detected. The application to the system of weights and its alternative for λ≥h³ was checked in [HODGE §§5–6](HODGE.md). NM is sufficient in the relevant result; it is not necessary for each instance to have defect zero.|
|56 `pkw:def-pcris`, `T2`, `G4` →55|Tame orders, conductor and permitted classes are kept. The polynomial q_s may depend on s; this result is not equivalent to a fixed polynomial killing all the elements of inertia. Coverage of all ℓ/lattices according to [HODGE](HODGE.md), under its explicit hypotheses.|
|55 `pg:sums`, `pg:loss`, `pri:loss`, `pll:main`, `exponent`, `sum` →56|Statements of global application/accounting reproduced faithfully. Their loss conclusions must not be used as a premise of the local bound that proves them. The order of construction classes→local bound→duality/sum was reconstructed, without that cycle, in [HODGE §6](HODGE.md) and [SELMER §§12,14](SELMER.md).|
|55 `pg:def-summand`, `pll:def`, `dual`, `ribet`, `exp` →56|Same lattices, length normalisation and classes. The review of Ribet reconstructed the residual hypothesis M4 explicitly included; no non-existent residual irreducibility was added to the junction. See [SELMER §§1–4](SELMER.md).|
|55 `pri:BL` →56|**The appendix also copies faithfully the defective assertion about one and the same polynomial for all s.** The literal defect is not a copying discrepancy; the correct local application uses q_s. The base level/e_c scope and the repair not incorporated into the paper are separated in [SELMER §11](SELMER.md).|
|55 `pga:depth0`, `pga:G45`, `pay:eta` →56|The label/depth conditions and the same source statements are kept. The defective sentences about norms of extensions of finite fields and orders of roots, and the repairs that preserve bounds, are recorded in [SELMER §§6,12](SELMER.md). Fidelity does not certify the source proof without those corrections.|

## Mutual citations and exhaustive scope

The inventory is exhaustive for the **environments of statements reproduced in those two appendices**. It does not claim that each bibliographic reference in the proofs of 55/56 is one of these 45 environments nor that equality of the body automatically audits all the transitive conventions of all the papers. The conventions relevant to the local/automorphic applications pointed out above were verified separately in the ledgers; those not individualised receive no certification from this inventory.

The arrows 46→55→46 and 55→56→55 are not by themselves circles. In the stretches reconstructed, data, lattices and classes are fixed first; then 56 proves the local bound and 55 concludes regularity. The appendix copy of a global conclusion is not used as its own proof. The route z=1 of 54 does receive exchange 53, not proved by the written proof; that dependence remains even if all its copies are faithful. See [JUNCTIONS-MATRIX](JUNCTIONS-MATRIX.md) for the exact propagation.
