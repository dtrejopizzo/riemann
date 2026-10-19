# Audit of phases 51–75: from structural no-go results to the `ADJ-ARITH-LOCK` residue

## Executive verdict

This block contains no proof of RH. Its solid contribution is of two kinds: (i) abstract theorems,
finite identities, reductions, and correctly bounded no-go results; (ii) numerical diagnostics with
falsifiers. The pattern running through the block is stable: every condition forcing positivity,
divisor convergence, passivity/Herglotz, absence of a negative index, or `Omega7` at the limit object is
**EQUIVALENT-TO-RH** or has equivalent strength. The self-consistent finite objects do not transfer
that property to the limit without the missing arithmetic estimate.

The conceptual part 51–59 closes metric, inertia, Stone, and second-order detector routes; it keeps a
cartography of barriers, not a bridge to RH. Phase 60 experimentally refutes the thesis that the
localized form detects multiplicativity. Phases 62–64 show that window positivities and relative
determinants are marginal detectors. Phases 65–71 reduce the question to strong continuity/convergence
of positive objects toward `Xi`; that continuity is not available and has RH strength. Phases 72–75
carry out many exact reductions of the CCM/Feshbach/Cauchy chain, but their final endpoint remains an
unproved arithmetic divisibility/cancellation of all orders.

**Convention.** PROVED means an identity, implication, or theorem with explicit hypotheses that the
material itself supports. CONDITIONAL requires the indicated hypothesis. NUMERICAL is a reproducible
finite computation, not an asymptotic claim. CONJECTURAL is a prediction or mechanism without closure.
REFUTED includes negative controls, internal contradictions, or a withdrawn inference. EQUIVALENT-TO-RH
designates a reformulation whose closure already implies RH. INCOMPLETE designates a program with a gap
that has not become a theorem.

## Documentary coverage

The 25 phases and their mathematical, result, closure, audit, and status documents were indexed:
**1,207 Markdown files** and **644 implementations or probes**. Binaries and TeX sources of phase 60
were used as manuscript backup, without treating a PDF as additional proof. In 72 and 73, the hundreds
of entries are grouped by their `E72.*` and `E73.*` series; the final READMEs and ledgers make their
dependency explicit, so they are not counted as independent results.

| Phase | Substantive documents covered | Coverage verdict |
|---|---|---|
| 51 | `160-*`, `161-*` | 2/2 Markdown |
| 52 | `162-*`, `163-*` | 2/2 Markdown |
| 53 | `164-*`, `165-*` | 2/2 Markdown |
| 54 | `166-*`–`172-*` | 7/7 Markdown |
| 55 | `173-*`–`177-*` | 5/5 Markdown |
| 56 | `178-*`–`181-*` | 4/4 Markdown |
| 57 | `183-*` | 1/1 Markdown |
| 58 | `184-*`–`192-*` | 9/9 Markdown |
| 59 | `193-*`–`199-*` | 7/7 Markdown |
| 60 | `00-PLAN`, `RESULTS`, `RH-*`, audits, attacks, tribunal and 27 experiments | 54 Markdown, 27 Python, 9 TeX, 8 PDF |
| 61 | `OPEN-PROBLEMS`, `R9/R10`, responses, detector and closure material | 8 Markdown, 77 Python, 2 TeX, 7 PDF |
| 62 | `README`, `C1`, `CROSSING`, `E90`–`E96` and results | 6 Markdown, 6 Python |
| 63 | `README`, `R1/R3`, `E97`–`E99` and results | 6 Markdown, 3 Python |
| 64 | `README`, `RESULTS`, `THE-TARGET`, constructions, faces A/C, audits and reports | 33 Markdown, 10 Python |
| 65 | `README`, `D0`–`D12`, `M1`–`M3`, corrections and `RH-PROOF` | 31/31 Markdown |
| 66 | setup, calibration, `D1/D3`, results and `omega7` closures | 9 Markdown, 4 Python |
| 67 | `README`, map, manifesto, `E67.1`–`E67.20` and results | 23 Markdown, 15 Python |
| 68 | `README`, `E68.1`–`E68.6` and results | 6 Markdown, 6 Python |
| 69 | `README`, `E69.1`–`E69.2` and results | 3 Markdown, 3 Python |
| 70 | `README`, closure program, `E70.1`–`E70.12` | 14 Markdown, 4 Python |
| 71 | `README`, `E71.1`–`E71.17` and results | 26 Markdown, 10 Python |
| 72 | `README`; series `E72.1`–`E72.396`, certificates, audits and probes | 437 Markdown, 232 Python |
| 73 | `README`; series `E73.001`–`E73.305`, certificates, audits and probes | 463 Markdown, 225 Python |
| 74 | `README`, `E74.001`–`E74.027`, ledger and falsifiers | 37 Markdown, 19 Python |
| 75 | `README`, `P75.001`–`P75.016`, results and harnesses | 12 Markdown, 3 Python |

## Phase-by-phase reconstruction

| Phase | Goal and surviving result | Status, retraction, and inheritance |
|---|---|---|
| **51** | Build a phase→inertia transport from the Kronecker flow. `160` builds crossed-product/KMS candidates; `161` analyzes the KK metric. | **PROVED:** the formal constructions and the spectrum/partition no-go results. **REFUTED:** that phase ergodicity gives inertia positivity. `GAP-160.A` is missing: an RH-free inertia metric; the KMS alternative returns to the ζ partition. Inherits the diagnosis that transport without pairing does not control Weil's signature. |
| **52** | Lift inertia to a homotopy invariant (`162`) and attack it adversarially (`163`). | **CONDITIONAL PROVED:** the `e_ζ↔2m` link requires Fredholmness. **REFUTED:** pure homotopy closing the arithmetic arrow. `GAP-162.C/D` requires computing the bracket/Chern character without reconstructing zeros; `163` proves the available paths return to orientation, to the ζ partition, or to the nonexistent Connes–Deninger object. |
| **53** | Import Stone, unitarity, and quantum mechanics (`164`), followed by a destructor (`165`). | **PROVED:** Stone in Kreĭn space does not deliver a real spectrum; RH-free groups have the wrong spectrum and self-adjoint extensions encode ζ's boundary. **EQUIVALENT-TO-RH:** "genuine Hilbert + self-adjoint + emission". **REFUTED:** structural unitarity as an independent lever. Inheritance: three walls, metric, boundary condition, and absorption→emission. |
| **54** | Dynamize the metric and index κ (`166`, `167`) and audit the steps (`168`–`172`). | **PROVED:** finite metric geometry and algebraic conservation of inertia under its hypotheses; `170` gives a second-order bound, `E(T)\ll T/\log T`. **CONDITIONAL/EQUIVALENT-TO-RH:** reaching the discriminant minimum, Gram uniformity, and index concentration. **REFUTED:** the unconditional reading of `Cor. 2.4/2.5`; `168` detects a mix of normalizations and a gap when `I<∞, \kappa=∞`. Re-audit any citation to "minimal quantized takeoff". |
| **55** | Open the two arrows: representation of `I`, coercivity/backward, energy, and the Green–Littlewood attack (`173`–`177`). | **PROVED:** energy identities and reductions in their domains. **INCOMPLETE:** the necessary coercivity/repulsion. **REFUTED:** turning a Green–Littlewood identity or an energy law into sign control without fine phase information. Inherits the two conditional towers that are later calibrated. |
| **56** | Complete the two towers: polylog confinement, the Euler pivot, and LP separation (`178`–`181`). | **PROVED:** `LP-112` is false in the regime `0<I<∞`; gap 175.A dissolves. **CONJECTURAL:** 178.C and `LP-134∞`; they are pillars, not available lemmas. **INCOMPLETE:** 175.B. Inheritance: Tower 1 is rewritten as `RH \Leftarrow A∧Dic`, without LP-112. |
| **57** | Isolate the Dirichlet–Selberg identity (`183`). | **PROVED:** the identity/accounting within the declared scope. **INCOMPLETE:** its use for a second-order signal requires estimating terms the identity does not control. It is audit input for 58. |
| **58** | Comprehensive audit of `173`–`183` and detection of windows, boundaries, and rigidity (`184`–`192`). | **PROVED:** several negative audits, including that pair correlation plus `G1` does not beat the window scale. **CONDITIONAL:** RvM dynamics and the polylog DH test. **REFUTED:** strong equivalences that omitted local reality hypotheses or converted window data into a sign signal. Inherits `GAP-141.G1`, 178.C, 179.6, and the formalized DH tests. |
| **59** | Close and classify the remaining gaps (`193`–`199`). | **PROVED:** unconditional RvM-t, the mollified-pipeline barrier for `θ≥1/2`, an axiomatized no-go in class `𝔄`, and a dependency list. **CONDITIONAL:** `TW_y`, 178.C, `LP-134∞`, 179.6. **CONJECTURAL:** DH near-doubles of `GAP-196.A`. The ledger is the correct closure: two conditional towers and three prices S1/S2/S3, not RH. |
| **60** | Prove multiplicativity controls the Weil sign via a localized discriminant. | **REFUTED/NUMERICAL:** the control `E2b_kill_confound.py` reproduces `C(ζ)=1.9798`, but smooth non-multiplicative controls give `2.4391`, `2.1118`, and `2.2085`; the E2 separation was smoothness/coherence, not Euler structure. The zero side is blind to multiplicativity and using off-line zeros would be circular. **PROVED:** only the relative instrument and the methodological no-go; not a universal law for every Weil form. |
| **61** | Archive of open problems and explorations of the 2.3.F/Doob–Parter chain. | **INCOMPLETE:** it is an inventory and laboratory, not a closure. The E programs and the detector delimit candidates; they do not turn their outputs into theorems. Inherits O11 toward 62 and MW-5 toward 63. |
| **62** | Close 2.3.F by Cesàro averaging and explore quaternionic Hodge polarization. | **REFUTED:** Cesàro does not neutralize an off-line root: secular growth `λ^{2β-1}` appears. The `k(k+2)` ladder also fails to discriminate; DH reproduces it. **NUMERICAL:** PSD in `V₊` for ζ, indefiniteness in DH and controls; the cascade has no gap. **EQUIVALENT-TO-RH:** uniformly bounding the margin. Closes both levers as marginal detectors. |
| **63** | Realize the missing Lefschetz/Frobenius operator and contrast it with curves over finite fields. | **NUMERICAL/STRUCTURAL:** the window test obtains anticommutation with `J` and the `F_q` control commutes and is gapped. **REFUTED:** transferring the curve mechanism as is. The claim "a finite gap is needed" is diagnostic, not an impossibility theorem for every regularized realization. |
| **64** | Connes route: regularized positivity, canonical systems, and index continuity. | **PROVED:** `L1⇒RH` under the stated pole/non-vanishing theorem; HB/Herglotz/Kreĭn–Langer equivalences as criteria. **EQUIVALENT-TO-RH:** `L1`, limiting passivity, HB survival, or locally uniform `E_P→Xi`. **REFUTED:** the initial burial via `det Y≡1`; `AUDIT-structure-function-death` retracts it as a non sequitur. **INCOMPLETE:** signature continuity through rank-one renormalization. |
| **65** | Build a graded topology/determinant that preserves index across the pole. | **PROVED:** zero-index closure in the appropriate topology and reductions D0–D7/D9–D12. **CONDITIONAL:** `D8.5⇒RH`. **EQUIVALENT-TO-RH:** endpoint identification and renormalization convergence. **Critical inconsistency:** `RH-PROOF.md` is announced as QED, but `CORRECTIONS-CONNES-R2`, D8.5b, and D12 acknowledge D8.5 is the sole failure point and has RH strength; the correction must prevail. |
| **66** | Isolate `omega7`'s rank-one leak. | **PROVED:** HB closure under locally uniform convergence, positive shorting, and subcritical isolation. **CONDITIONAL/EQUIVALENT-TO-RH:** primitive Gram convergence at the endpoint. **INCONCLUSIVE NUMERICAL:** the faithful version of `K_P` was not stabilized. Inherits the split A,C→MW-2 and B→MW-5. |
| **67** | Force a quantum index `q` without circularity. | **REFUTED:** group-like/Bost–Connes generators and strict free products do not produce the required interference. **NUMERICAL:** index/symbol detectors separate controls. **INCOMPLETE:** a Haar state with off-diagonal coherence, domination, and a DH falsifier; the "forcing theorem" remains a condition, not a theorem. |
| **68** | Use a GLT/pseudodifferential symbol for the `Omega7` defect. | **REFUTED:** the assumed clean GLT sequence: the position symbol fails the distribution law and is fragile to gauge. **NUMERICAL:** marginal symbolic depth for ζ and negative on falsifiers. **EQUIVALENT-TO-RH:** `κ(x,θ)≥0` if used as a global forcer. Inheritance: abandon the symbol as a certificate. |
| **69** | Replace the symbol with an exact gauge-invariant index. | **PROVED:** for finite matrices, zero negative residue of the `q`-resolvent is equivalent to positivity. **EQUIVALENT-TO-RH:** `Im(-Xi'/Xi)≥0` on the half-plane or zero global negative index. **NUMERICAL:** correction of two bugs in `E69.1`; the mesh values only validate the detector. Inherits the clean Herglotz form, not a forcing. |
| **70** | Lee–Yang/de Bruijn–Newman forcing and arithmetic Herglotz majorization (AHM). | **PROVED:** the `q`-resolvent identity is a finite equivalence, not a new path. **EQUIVALENT-TO-RH:** AHM, `Λ≤0`, zero negative residue, or `Omega7`. **REFUTED:** treating the trace-residue as an independent identity; Euler/Gamma evaluation/fusion and global cancellation are missing. Inherits AHM as an explicit target. |
| **71** | Convergence of CCM triples to `Xi` via ground state/prolate. | **PROVED:** Hurwitz: entire approximants with real zeros converging locally to `Xi` imply RH; `E71.17` reduces this to ground-state approximation. **CONDITIONAL:** perturbation smaller than the gap. **EQUIVALENT-TO-RH:** the required stable divisor/resolvent convergence. **NUMERICAL:** window stability does not prove the limit. Inherits 72's reduced-leak goal. |
| **72** | Replace global convergence with a reduced Feshbach leak and turn it into current, Cauchy, and packet identities. | **PROVED:** numerous finite functional implications: sufficient reduced leak, current/Fredholm closures, and reductions to `PW-Cauchy`. **REFUTED:** two-jet transport, naive discrete divisibility, absolute tail bounds, and circular zero filters. **EQUIVALENT-TO-RH:** divisor-current convergence or the `PW-Cauchy` closure that suppresses off-line nodes. The README lists many closed doors; it does not prove the final arithmetic estimate. |
| **73** | Solve `NAT-PROJ` via Cauchy/Hermite interpolation, then via spectral distribution and the Hilbert product rule. | **PROVED:** finite equivalences and certificates, including the numerator divisor, Loewner normalization, and `HPR`. **REFUTED:** absolute geometry, universal Hermite moments, global quotient bounds, and purely geometric selection. **INCOMPLETE:** the signed cancellation `HPR-DIV`/`K-DIAGOFF`; the probes only show finite sizes. This phase does not establish the long chain to `Omega7`. |
| **74** | Prove Hilbert self-line cancellation and audit closure mechanisms. | **PROVED:** Schur transfer identities and equivalences of `CAUCHY-EIG-LOC`, `CRIT-NUM-DIV`, `CCM-ROOT-LOCK` under separation/Gram hypotheses. **REFUTED:** `QLIFT`, a single gap, jet bootstrap, generic coboundaries, and term-by-term Euler/Gamma tails. **NUMERICAL:** locking for ζ and failures on planted/DH data. **EQUIVALENT-TO-RH:** `HPR-DIV` given it leads to `Omega7`; the ledger declares the irreducible residue `EG_LOCK`. |
| **75** | Eliminate the self-line and prove divisibility of the finite numerator by the critical divisor. | **PROVED:** a bordered-determinant identity and an adjugate formula that turn the obstacle into a finite minor without a pseudoinverse. **REFUTED:** obtaining a new bound from the Euler/Gamma expansion, cutoff smoothing, or Schur conditioning. **NUMERICAL:** the harness keeps falsifiers, but is not a proof. **INCOMPLETE/EQUIVALENT-TO-RH:** `ADJ-ARITH-LOCK` is the same load as `TPW/scalar-WRL` under the already-isolated hypotheses; `Omega7` remains open. |

## Dependency chain and valid inheritance

```text
51–53: metric/inertia/Stone  ──> no-go: useful positivity or self-adjointness = RH
54–59: index and detectors   ──> partial theorems + conditional towers S1/S2/S3
60–63: localized window      ──> marginal detectors; Cesàro, Hodge, and Lefschetz do not cross over
64–71: Connes/CCM            ──> continuity or positive convergence toward Xi = RH-strength
72–75: Feshbach/Cauchy       ──> PW-Cauchy/HPR-DIV/EG_LOCK/ADJ-ARITH-LOCK
                                      └── unproved signed arithmetic estimate
```

Reusable inheritance must be limited to: finite algebraic identities, theorems with visible hypotheses,
precision controls, DH/planted/random falsifiers, and the no-go results that prevent reintroducing Weil
positivity, a zero filter, `-ζ'/ζ` as a partition function, or a pseudoinverse chosen to cancel the
residual. Not inherited as lemmas: window closures, root fits, double-precision margins, nor convergence
inferred from a few gauges.

## Critical findings requiring re-audit

1. **Phase 54, Cor. 2.4/2.5.** `168-adversarial-audit-of-doc-167-dynamics.md` identifies a mix of normalizations and the
   uncovered case `I<∞, κ=∞`. The unconditional versions must be withdrawn; only the conditioned form
   and `RH⇔I(0⁺)=0` with its hypotheses survive.
2. **Phase 60, scope of the no-go.** Running `E2b_kill_confound.py` confirms the numerical confound; it
   proves that observable does not detect multiplicativity under those controls, not that every possible
   localized form is blind. Any universal formulation must be downgraded.
3. **Phase 63, "exact" versus computation.** Anticommutation and the `F_q` contrast are presented with
   ratios and finite matrices. Without an independent symbolic proof, their correct classification is
   NUMERICAL/structural, not a general theorem over Spec ℤ.
4. **Phase 64, mandatory retraction.** The `det Y≡1` argument that buried HB convergence was retracted.
   It must not be cited either as no-go or as proof; the correct status is reduction to locally uniform
   convergence, of RH strength.
5. **Phase 65, editorial contradiction.** The QED label of `RH-PROOF.md` contradicts the later admission
   of D8.5b/D12. Re-auditing every `RH-PROOF` dependency and replacing its status with CONDITIONAL are
   mandatory before any reuse.
6. **Phases 67–70, finite equivalences.** `q`-indices, residues, and symbols are certificates or
   detectors. Their vanishing for ζ's data is not a forcing theorem; calling an equivalence a "forcer"
   without independent evaluation confuses goal and tool.
7. **Phases 71–75, chain inflation.** The numerous arrows are reductions; the only closure claim would
   be the leak/cancellation/divisibility bound. `E74.27` and `P75.016` acknowledge that `PW-Cauchy`,
   `HPR-DIV`, `EG_LOCK`, and `ADJ-ARITH-LOCK` are faces of the same missing piece, not four independent
   advances.
8. **External provenance.** Ledgers 59 and 65 keep citations and literature results with pages or
   verification pending; documents depending on D150, on the Bettin–Gonek/Farmer ranges, or on Connes
   references need external checking before promotion.

## Usable final status

**PROVED:** crossed-product/index identities within abstract scope, Stone–Kreĭn no-go, the bound
`E(T)\ll T/\log T`, barriers of class `𝔄`, finite determinant equivalences, shorting/Feshbach, and the
Cauchy/Hilbert/adjugate identities.

**CONDITIONAL:** both towers of 56–59, D8.5 of 65, the convergence closures of 64–72, and the transfers
of 74–75 that require separation, Gram, or a signed arithmetic estimate.

**NUMERICAL:** discriminants and controls of 60; PSD/window margins of 62–63; detectors of 64 and
67–71; locking, FAR selection, and falsifiers of 72–75. These are stress tests, not asymptotic proofs.

**REFUTED:** multiplicativity detected by the discriminant of 60; Cesàro as an escape in 62; clean GLT
in 68; the `q`-resolvent as an independent forcer in 70; quotient/gap/jet/absolute-bound mechanisms in
72–75; and the withdrawn inferences noted in 54, 64, and 65.

**EQUIVALENT-TO-RH:** Weil positivity/useful Hilbert–Pólya, `L1`, passivity or Herglotz of `Xi`,
signature continuity, locally uniform convergence of approximants with real zeros, `Omega7`, `HPR-DIV`
with its chain, and `ADJ-ARITH-LOCK` under the declared transfers.

The only next mathematical step that does not repeat a no-go is to prove an independent signed
arithmetic identity delivering `ADJ-ARITH-LOCK` — or, first, to prove that statement is formally
equivalent to RH without auxiliary hypotheses and record it as a closure by equivalence. Until then, the
overall classification is **INCOMPLETE**.
