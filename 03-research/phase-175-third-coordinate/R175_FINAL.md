# R175 — third coordinate: closure of rounds 0–3

**Verdict: NO-GO.** Rounds 1–3 neither build the required geometric triple
nor prove an impossibility or a classification. The result is more
precise: there are dynamical and Witt carriers with correct parts, but
none jointly delivers the spectral `H¹`, the geometric form `Q`, the
transfer map, and the full trace that identifies `ζ`'s explicit formula.
Row D remains open. Nothing in this round proves RH.

## 0. Primary sources and starting point

Álvarez López–Kordyukov–Leichtnam (AKL), [arXiv:2402.06671v2](https://arxiv.org/pdf/2402.06671v2), a 176-page PDF, and Deninger, [arXiv:1807.06400v4](https://arxiv.org/pdf/1807.06400v4), 119 pages, were read in full. Borger [arXiv:0906.3146](https://arxiv.org/html/0906.3146) and Connes–Consani [arXiv:1805.10501](https://arxiv.org/html/1805.10501) were also checked against them.

AKL define a generic system `(M,F,φ)` with no `ζ`. Theorem 1.3.10 (p. 8) proves a dynamical trace formula with preserved leaves and closed orbits: **PROVED**. It builds no specific arithmetic `π`, no `σ`, no relevant `Q`, and does not identify its distribution with `ζ`'s explicit formula. It declares the arithmetic framework pending: "once the appropriate framework ... will have been discovered" (p. 2). The dynamical equality is a theorem; the arithmetic identification is neither adopted as a hypothesis nor proved. [R158_001, §4](../phase-158-row-d-mw5-object/R158_001_SPEC_SHEET.md) records OT-2 as the first failure upon admitting the generic geometric carrier; under OT-1 applied to the required arithmetic object, that specific carrier is also missing.

Deninger defines the system `X_E` coming from rational Witt vectors without using `ζ`. An admissible class `E` is fixed, with `E_f⊆E⊆E_max` — for example `E=E_f`, of finite kernel, §4, pp. 28–29. Theorem 6.1 (p. 39), applied to `Spec Z`, gives the bijection between the nonempty canonical packages `Γ_p` and the closed points. Counting one package per prime and its iterations produces

\[
\pi=\sum_{p}\sum_{k\ge1}\log p\,\delta_{k\log p}
   =\sum_{n\ge2}\Lambda(n)\delta_{\log n}.
\]

This equality is **PROVED** as an R175 inference; it is not a trace formula published by Deninger and does not extend to unrestricted Witt points. Definition 10.1 (p. 63) formally defines all the degrees `H^•`; Theorem 10.2 (p. 64) computes `H⁰=R`. It does not compute an `H¹` with a zero spectrum, builds no `Q`, and proves no Lefschetz formula equal to `ζ`'s. The limitation is preserved in its own phrase: "the cohomological problem pointed out in [KS18] and which we recalled above persists" (p. 5). By OT-1: **NO-GO**.

The multiset `σ_an` is indeed built from `π`: the comb determines `−ζ′/ζ` for `Re s>1`; classical meromorphic continuation determines the zeros and their multiplicities. This reconstruction satisfies the literal output of `σ`, but builds neither `Q_X` nor its transfer. The cohomological identification is also unproved.

Borger, §1.1–§1.2, builds `W^*(Spec A)=colim_n Spec W_n(A)`; by contrast, `Spec Λ=W_*(A¹)` is the arithmetic jet space of the line, not the square `W^*(Spec Z)`. Here `Λ` denotes the ring of symmetric functions, not von Mangoldt. The warning about infinity is in the introduction: the theory "says nothing about the archimedean place". The required cohomological/intersectional object is missing (OT-1); so is the archimedean place (OT-12): **NO-GO**.

Connes–Consani locates the cohomological blockage: "null elements creates unwanted contributions". Grouping an idempotent monoid kills its generators, but this alone does not resolve any entire cohomological theory.

The application of [OT-1…OT-12 and their corrections](../phase-158-row-d-mw5-object/R158_003_AUDIT_SPEC.md) is recorded as follows; **NO-GO** means an unverified requirement for the triple, not a nonexistence theorem:

| Test | AKL / Deninger, as arithmetic triples |
|---|---|
| OT-1 | **NO-GO**: the required arithmetic cohomological object is missing; see the OT-2 convention for AKL above. |
| OT-2 | **NO-GO**: the full arithmetic trace is missing. |
| OT-3 | **PROVED**: definitional independence of the carriers. |
| OT-4, OT-5 | **NO-GO**: no proved separation of substitutes. |
| OT-5′, OT-6, OT-7, OT-8 | **NO-GO**: the exact global geometric positivity is missing. |
| OT-9 | **NO-GO** as a realization of the required Riemann–Roch route. |
| OT-10 | **NO-GO** for the uniform theorem; Deninger's carrier family does exist. |
| OT-11 | **NO-GO**: no full arithmetic form delivered. |
| OT-12 | **NO-GO**: the exact archimedean contribution is not realized. |

## 1. Round A: dynamics, cohomology, and renormalization

**A1 — NO-GO.** For an idempotent additive monoid `M`, in its
grouping `G(M)` one has `[a]+[a]=[a]`, hence `[a]=0`; so `G(M)=0`. This is **PROVED** and concerns only the naive additive grouping. It does not prove that every idempotent cohomology is trivial nor does it eliminate complexes, sheaves, or derived theories that bypass that naive grouping.

**A2 — NO-GO.** Directly applying AKL to the carrier `W_rat` lacks the geometric hypotheses and the required computation: closed manifold, regular foliation, conormal complexes, and flow operator within AKL's framework. Deninger does provide `π` in the sense above; the failure lies in manufacturing the geometric object to which the trace is applied, and in identifying it with `ζ`.

**A3 — NO-GO.** The finite part of the scalar model gives

\[
\int_\varepsilon^1(1-x/2)\,\frac{dx}{x}
=-\log\varepsilon-\frac12+\frac\varepsilon2,
\qquad \operatorname{FP}_{\varepsilon\downarrow0}=-\frac12,
\]

even though the density is positive on `(0,1]`. Thus, an inference from pre-renormalization positivity to positivity of the finite part is false: **PROVED**. The computation does not identify AKL's exact global `b`-calculus operator and does not refute its theorem.

**Pending Statement A — NO-GO.** Build, from `X_E`, or from an explicit functorial geometric replacement, a conormal complex with an archimedean contribution, its `H¹`, a Hermitian form `Q_X`, and a linear map `J:C_c^∞(R)→dom(Q_X)`, without defining them via `π`, `σ`, or `W`. Geometrically prove `Q_X≥0`; then identify the cohomological spectrum with all the multiplicities of `σ`; and prove `Q_X(JF,JF)=W(F)` for **every** `F∈C_c^∞(R)`, including Gamma and poles, with the extension to the form domain that the mandate requires. A finite-dimensional compactification of the published space is not presupposed. This is the construction missing in this route, not a proved existence.

## 2. Round B: Witt, squares, and bivariate theory

**B1 — NO-GO.** The assumption that the necklace carries a contact length and the assumption that the Euler differential produces the gamma factor are withdrawn. The formal-line identities do not satisfy clause 2 of [P47 §28.4](../../04-papers/47-intersection-frame-defect/archive/main.md).

**B2 — NO-GO.** `W^*(Spec Z)=Spec Λ` and the argument via truncated products are withdrawn: Adams operations do not preserve `Z[e₁,…,e_N]`. The notation supplies no arithmetic square.

**B3 — NO-GO.** `W_rat` and the Witt spaces are carriers. What is missing is a bivariate theory on the correct Witt square that builds correspondences and domains, controls the passage to the limit, incorporates the geometry at infinity, produces a genuine local polar residue, and derives the Hodge index plus the exact trace. It has not been proved that every route of this kind fails.

**Pending Statement B — NO-GO.** On Borger's square `W^*(Spec Z)`, build a real group of correspondences with product, transpose, and degrees, with specified domains and passage to the limit. Build its real contribution and its polar class from geometric localizations; prove the Hodge index on the classes of both degree zero. Also build the cohomology and the test map identifying that pairing with the full form `W` for every test, with exact spectral multiplicities. Positivity must precede that identification. The proof stopped before the global product and its real localization; not only at the sign. These conditions describe the attempted implementation, not a classification of every implementation.

[G1_B5_R3](../phase-159-row-d-two-front-construction/G1_B5_R3.md) treats the suspension of Witt data under its Hilbertian adjunction hypotheses. The Coulomb correction is in [R160_C4_R1, Theorems B–E](../phase-160-row-d-infinite-T/R160_C4_R1.md): it reproduces Weil terms without deriving their sign. Proposition C.4 there only excludes corrections depending on the norm quotient, not every archimedean construction.

## 3. Round C: recodings and residual candidate

**C1 — NO-GO.** The bouquet and `Sym` recode the monoid `N`. It is not proved that `Sym` is the only recoding, nor is cohomology, polarization, or a trace formula obtained.

**C2 — NO-GO.** The Eisenstein/scattering modular route was rejected before being built, due to the explicit prohibition in phase 174's mandate. Its claimed novelty and its claimed Morita inequivalence were not proved and were withdrawn.

**C3 — NO-GO.** No admissible candidate remains within the families examined. The criterion to reopen is a new `X` outside them, accompanied by geometric cohomology and `Q`, `π`, `σ`, and a `J` transferring the full form `W`. This is a delivery specification, not an existence theorem.

## 4. H1–H5 audit and the six clauses

| Gate | Status | Certificate |
|---|---|---|
| H1: `X` defined without `ζ` | **PROVED** for the cited carriers | This does not credit the geometric enrichments proposed in A/B. C delivers no admissible candidate. |
| H2: `σ` constructed, not postulated | **PROVED** for `σ_an` from `X_E`; **NO-GO** for the proposed cohomological realization | The literal analytic output is neither rejected nor confused with a sign proof. |
| H3: sign of `Q_X` without using `σ` | **NO-GO** | The required positive form was not built. A conditional norm does not verify this gate. |
| H4: exact transfer to `W` | **NO-GO** | There is no `Q` and `J` with `Q(JF)=W(F)`, including Gamma and poles. |
| H5: falsifiers | **NO-GO** | Simultaneous separation of `P_171`, Davenport–Heilbronn, `Ξ_a`, and `Ξ_Q` was not proved. These are pending proofs, not invented failures. `P_171` already has integer multiplicities: [R171_FINAL](../phase-171-discrete-beurling-frontier/R171_FINAL.md). |

P47 §28.4's six clauses remain **NO-GO** for the triple: square and positivity after twists; locally fixed polar divisor; holomorphic zeros to its left; phase reading; simultaneous use of sum and product; and uniformity across fields. The existence of a family of carriers does not prove clause 6, and the formal lines do not prove clause 2. Nor is that absence turned into a universal falsifier.

**Closure: NO-GO.** R175 delimits the missing object and corrects strong attributions. It does not prove that object is impossible, does not classify every carrier, and does not prove RH.
