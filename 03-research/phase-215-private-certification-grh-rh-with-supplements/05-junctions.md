# Junctions between the papers

**Current update:** the deep review replaces the historical pending items of this table in the cases individualised by [JUNCTIONS-MATRIX](deep-review/JUNCTIONS-MATRIX.md). That matrix distinguishes textual coincidence, hypotheses and range, proof of the input, logical cycles and propagation of the character failure of P53. In particular, the earlier (c) verdicts for mere lack of reading of P55/P56 are no longer current; the local chain was reconstructed, while the IM branch of z=1 depends on the defective exchange. What is not individualised remains without certification.

The table of inputs at the end of the automorphic section of paper 46 (5055–5095) is covered by the matrix below and the specific checks linked. **The whole network of transitive imports is not certified.** The concordance of the imported statement is distinguished from the proof of the statement and from the fulfilment of its hypotheses in each application. A mutual citation does not prove circularity; textual coincidence does not prove its absence either.

## Inputs listed by paper 46

| Input | Origin | Concordance checked | Verdict of global validity |
|---|---|---|---|
| `au:seesaw` | 49 | The scalar is independent of the twist; the chain datum may depend on it. | (c), the whole transfer and integration remain to be certified. |
| `au:divis` | 49, 50 | Level exception, truncation and loss of colength are maintained; invariance of the ramified subspace under each Hecke operator is not asserted. | (c); algebraic argument of 50 reviewed separately. |
| `au:count` | 49 | The nested columns and the additional deduction at the ramified prime are kept. | (c), normal form of the kernel and assembly. |
| `au:kernel` | 49 | Every conjugate and the exponential bound with `rs_j/2`. | (c), exact CM normalisation and reciprocity. |
| `au:restrict` | 49 | Squared norm, loss `x^70` and level term. | (c), integral branching pending. |
| `au:expansion` | 49 | Integrality outside the level and conductor; size bound for trivial twist. | (c), gluing and count. |
| `au:equiv` | 49 | Tame character and right translation kept. | (c), local integrality of the translation. |
| `au:shortbasis` | 49 | Basis over E, not necessarily an integral basis; constant `6c_0(fn)^2`. | (a) for the geometry of numbers lemma under its hypotheses. |
| `au:moment` | 51, 52 | Three bounds and constant `1+9b^-4` coincide. | (c), complete local estimates and uniformity pending. |
| `au:mult` | 51 | The assumptions of separation and projection are present; `pm:rem-full` covers inert places. | (c), orbital identity and global justification of the trace. |
| `au:inj` | 53, 54 | Triangle and first lift identified; no complete literal comparison of all its inputs was made. | (c), automorphic realisation; abstract triangle correct. |
| `au:factor` | 53, 54, 51 | m-fold twists and powers are kept; depends on the same comparison of multiplicities. | (c), exchange, factors and all the substitutions. |
| `au:aux` | 53 | Origin identified in `pc:twistreduct`; complete comparison of hypotheses pending. | (c). |
| `au:regular` | 55, 56, 54 | R1–R3, factors `log ℓ`, denominators and false lifts collated. | (c), Selmer, integral exponents and odd classes. |
| `au:onelift` | 54, 53 | Compressed determinant, power `d_j` and twist-independent factors coincide. | (c), `po:glue` and its antecedents. |
| `au:hecke` | 54, 53 | `3x^35` already propagated, not the old version; rest of the applications of CL pending. | (c), integral test and comparison of norms. |

The details and locators are in [theta and Hecke](02-theta-hecke-covolume.md), [spanning](03-spanning.md) and [Selmer and Hodge](04-selmer-hodge.md).

## Junctions that require special care

**Range of 50 towards 49.** The equality of the cited statement includes the exceptional fraction and the term `θj`. A truncated colength cannot be replaced by a uniform bound for all the elementary divisors. The numerical substitutions were verified; the arithmetic realisation of all the data remains (c).

**Lattices 49 and 51.** They are not literally the same lattice. The manuscript acknowledges this and provides adelic transport and unitary conjugation (`pb:lattice` of 51, 1027–1110; `au:two-lattices` of 46). The invariance of Hilbert–Schmidt norms under that transport is correct. Checking it does not by itself certify all the data of the original construction of 49.

**52 towards 51.** The range includes `ρ≥10^8` and conditions H0–H5. The weaker condition `n≥100` would not be sufficient, but the current version mentions and verifies the larger size in the data. (R), (F), (S) use the same measures, masses and weights; the complete audit of H1–H5 and of their proofs remains (c).

**56 towards 55.** The text carefully distinguishes annihilating exponent from length of the defect: in a generic case only the second is obtained. The duals, changes of weights and inversion `K(s^-1)` of tame types are present. NM is verified from `λ<h^3` in the application examined. The loss of hypotheses that reading only the title "without Fontaine–Laffaille restriction" would suggest was not found.

**43–45 towards 46.** The explicit formula and the primitive criterion do coincide, according to [the review of the Weil framework](07-rows-a-b-c.md). Those inputs are used to interpret the form and the converse of the criterion; they do not supply the positivity that the automorphic chain aims to prove.

## Reproducible inventory and limits

`evidence/audit_sources.py` generates:

- `sources.json`: SHA-256 hashes, paths and number of lines of the fourteen sources 43–46, 49–58, excluding 47–48.
- `shared_statements.json`: text and locator of environments with shared labels.
- `textual_junctions.tsv`: equality after removing labels and normalising spaces.
- `internal_citations.tsv`: explicit bibliographic references with keys P43–P56 or Paper43–Paper56, excluding 47–48. It does not detect keys with alternative names such as `Companion`.

The coincidence of labels is only a navigation aid: generic labels may name different results. The macros may also change meaning between files. For that reason a `True` in the TSV **is not a verdict (a)**, and a `False` is not a mathematical failure. The differences of the main automorphic inputs between 46 and 58 were inspected: those observed are substitutions of external citations by internal references, not demonstrated changes of constant or range.

**Status of all the junctions not individualised in the tables:** (c), not verified. What is pending is to compare the complete statement, its transitive definitions and the verification of hypotheses at the place of application. The inventory does not replace that work. I do not claim to have reviewed semantically each of the thousands of references of these manuscripts.

To close the network a note is needed per import with origin, destination, correspondence of symbols, measures, lattices, range and proof of the hypotheses of application. The notes above cover the central inputs that 46 lists; they are not enough to certify the conclusion GRH.
