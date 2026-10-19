# R166_403 — Survey 2-of-3 (part C): mechanisms of phases 0–110 against criteria (i)/(ii)/(iii)

Scope:** `03-research/phase-0-foundations` … `phase-110-principal-xi-divisibility`.
**Index used:** master grid `phase-162-…/grid/R162_2300_MASTER_grid.json` (all routes whose id names a phase ≤ 110, ~320 rows, collapsed to 58 mechanisms), surveys `R160_S1…S3`, `MAP_*`. Original files were opened only to confirm the borderline ones (phase-12-meta-obstruction-moment-problem verdict, phase-27-adelic-rigidity verdict, phase-67 E67_15, phase-70 E70_10).

**Criteria (from R166_190 §0 and closure):**
- **(i) GLOBAL** in the node set X / whole witness (Hadamard product, phase, harmonic measure, Wiener–Hopf), not finitely many node jets / finite truncation.
- **(ii) ATOMIC PRIME COUPLING beyond the window**: uses Λ(n) for n ≥ e^{2T_c}, Λ ≥ 0, multiplicativity, all heights, **non-linearly** (a linear functional of Λ = explicit formula = fails).
- **(iii) NOT a reduction** to E1 (explicit formula / zero-side identity on one test), nor window-only (f_t), nor zero-set-only (M_m).

**Strict reading.** Any route whose grid killer is E1 (or whose note says "iff RH" / "restatement") fails (iii). Any route that is a statement about the zero set / dBN / Hadamard data only fails (ii) and (iii) (M_m). Any route on a finite truncation, finite S, per-prime or fixed window fails (i) and is killed by f_t on (iii). "log ζ" and ζ′/ζ are **linear** in Λ: they do not give (ii). ✓ = met, ✗ = not met, ~ = met only in a degenerate/formal sense (not counted).

## Table (sorted by number of criteria met)

| # | Mechanism | Phases / files | Grid ids | (i) | (ii) | (iii) | Wall (killer) | Residue | Why (one line) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dirichlet-shift square / Wiener–Hopf Euler–Γ factor A−T_Λ = D\*D | 70 (E70_9, E70_10, E70_7) | R160_S2 F54 phase-70/E70_10; phase-70 | ✓ | ✓ | ~ | F2 (Euler ratio-comb manufactured) | Grading/quotient cancelling the Euler square (E70_10 end) | Wiener–Hopf factorization of the whole form; V\*V contains Λ(m)Λ(n) at all log(n/m) — genuinely quadratic in atomic Λ; target is full Weil positivity, not one test, but the square adds Σ c_r S_{log r} that A cannot absorb |
| 2 | Lee–Yang / DQPT for dBN + Euler–Möbius connection (AHM) | 70 (E70_4, E70_7, E70_11) | phase-70 (4E) | ✓ | ✓ | ✗ | F2; per-prime local positivity insufficient | "Global cross-prime cancellation" requirement (E70_7) | Lee–Yang is global in the zero set and Möbius/Euler connection is multiplicative; but AHM reduces to Weil (E70_4) ⇒ E1 |
| 3 | Multiplicative chaos / freezing (S(T) log-correlated) | 12 (M12-VERDICT, M12.8–9) | phase-12-meta-obstruction-moment-problem/M12.1-9 | ✗ | ✓ | ✓ | OTHER: probabilistic–deterministic gap | Moment problem for freezing (M12.9) | Uses ζ = exp(Σ prime sums), a non-linear (exponential) functional of primes at all heights; not an explicit formula; but statistical over heights, never global in X of one witness |
| 4 | Adelic local–global (Hasse–Minkowski) Q = Q_∞ + Σ Q_p | 27 (02-C, 03-verdict) | phase-27-adelic-rigidity; R160_S1 §2.1#4 phase-27-adelic-rigidity | ✗ | ✓ | ✓ | OTHER: MW-3 walls A/B (= CC arithmetic site) | Wall A/B open | Uses all primes with multiplicative local structure; not a single-test identity; but no node-set globality — factorization over places, and sum over places is linear |
| 5 | Sign of \|ζ\|²−\|ζ_on\|², dν, relative entropy | 33 (83, 86, 89) | phase-33/83,86,89; R160_S1 §2.4#22 | ✓ | ✓ | ✗ | OTHER: uses zero positions; E1 | — | Harmonic-measure-type global object built from \|ζ\|² (quadratic in Euler product); every divergence "vanishes iff RH" |
| 6 | Bagchi strong recurrence / Voronin universality | 35 (102), LP-112 | phase-35/102; R160_S1 §2.6#42 | ✗ | ✓ | ✗ | E1 | LP-112 open | Universality uses Euler product non-linearly at all heights; strong recurrence ⟺ RH |
| 7 | Epstein test (geometry vs Euler product) | 8 (PLAN) | phase-8-heat-flow-monotonicity/PLAN (Epstein) | ✗ | ✓ | ✓ | F3: Epstein | — (falsifier, not a mechanism) | Shows multiplicativity is required; delivers no sign — recorded as the ancestor of (ii) |
| 8 | Two-variable Weil form W₂, Λ\*Λ block | 36/107 | phase-36/107; R160_S1 §5 I7 | ✗ | ✓ | ~ | superseded by R162_2702a | Lemma 5.2 analytic realization | Prime×prime block Λ\*Λ is bilinear in Λ; but it is a two-variable explicit formula on a test, no node globality |
| 9 | Green–Littlewood energy / Cesàro double integral of log\|ζ\| | 55/173, 176 | phase-55/173+176 | ✓ | ✗ | ✗ | E1 | — | Global harmonic quantity; log\|ζ\| is linear in Λ; RH iff value = −π/8 (zero-side identity) |
| 10 | de Branges / Hermite–Biehler / Pontryagin H(E_ξ) | 0 (0A3), 5 (B3.2), 16 (07-09), 29 (50) | phase-0/0A3, phase-5/B3.2, phase-16-surf-witness-variety/07-09, phase-29-zeta-spectral-triples/50 | ✓ | ✗ | ✗ | E1; Conrey–Li | — | Global phase of E; criterion ⟺ RH; prime data absent |
| 11 | Kreĭn angular operator E\*JE, ‖K‖≤1, Kreĭn–Langer | 4 (B3-KREIN, PAPER-A Thm C), 25, 34/91–96 | phase-4/B3-KREIN, phase-4/PAPER-A Thm C, phase-34/91,94,96 | ✓ | ✗ | ✗ | E1 | Conjecture C_B (finite off-zeros) | Global operator on whole space; ‖K‖≤1 ⟺ RH; depths enter only through t |
| 12 | Herglotz / half-plane Re ξ′/ξ ≥ 0, Pick passivity | 64 (Pick), 102 (115–116, 174–175) | phase-64/Pick, phase-102/115,116, phase-102/174,175 | ✓ | ✗ | ✗ | E1 | Schur for ω>½ | Global analytic positivity; ξ′/ξ linear in Λ |
| 13 | Nyman–Beurling density (variational) | 33 (82, 85) | phase-33/82,85 | ✓ | ✗ | ✗ | E1 | — | Global approximation; δ_λ=0 ∀λ ⟺ RH |
| 14 | Li / Keiper coefficients, A0 tail, A1 Laguerre | 33/75, 102, 103, 104, 105 | phase-102/README+139, phase-103/*, phase-104/*, phase-105/105_02 | ✓ | ✗ | ✗ | E1; envelope/stop-gates | A1 (n≥8) open | λ_n = sum over all zeros (global) but arithmetic side is ψ(x)−x, linear in Λ; "sign must come from signed global compensation" |
| 15 | dBN flow / Λ=0 / balance law / monotone functionals | 8 (GATE-B), 9 (N6), 25, 28/01, 30/57, 33/88, 54/167, 37/109 | phase-8-heat-flow-monotonicity/GATE-B, phase-9-unconditional-universality/M9.1, phase-33/88, phase-54/167-168, phase-30-langlands-bridge-c-infinity/57 | ✓ | ✗ | ✗ | E1; N5/N6; M_m | Conj A.15 | Hadamard-product flow, global in zeros; arithmetic-blind (zero-only ⇒ M_m) |
| 16 | Laguerre–Pólya / Jensen hyperbolicity / t-concavity | 11, 28 (07-08) | phase-11-hyperbolicity-total-positivity/M11.2-5, phase-28-four-fronts/07-08 | ✓ | ✗ | ✗ | E1; preserver arithmetic-blind | — | Global hyperbolicity of the whole function; zero-only |
| 17 | Poisson / Cauchy rigidity, C_∞(γ_n)=0, deficit measure | 29 (42–54), 31/58 | phase-29-zeta-spectral-triples/42-48, phase-29-zeta-spectral-triples/53-54, R160_S1 §2.7#44 | ✓ | ✗ | ✗ | E1 (MW-7 Hadamard barrier) | — | Global Poisson transform; every formulation is zero location |
| 18 | Moment-problem rigidity (Carleman, Jacobi m-function, CCM triples) | 29 (00–28, 26), 38/118, 34/92 | phase-29-zeta-spectral-triples/00-28, phase-29-zeta-spectral-triples/26, phase-38/118, phase-34/92 | ✓ | ✗ | ✗ | E1; Carleman fails | Determinacy unavailable | Global spectral measure; equalities are zero-side input |
| 19 | Fourier interpolation / frames {e^{iγs}} | 35/101 | phase-35/101 | ✓ | ✗ | ✗ | OTHER: weight-independent refutation | — | Global in zero set; no prime input |
| 20 | Parity / exclusion principle (all on-line or ∞ off) | 21 | phase-21-negative-directions-geometry/01-02 | ✓ | ✗ | ✗ | (open conjecture) — M_m kills it | — | Statement about the zero set only; M_m has finitely many quartets, so exclusion alone is zero-only |
| 21 | LP-112 / LP-134 / LP-141 dichotomy and repulsion; Stepanov | 37/112–113, 38/115–116, 46/141, 47/144, 55/175, 56/181 | phase-55/175+56/181, R160_S2 F49-F51, phase-46/141+47/144+56/179 | ✓ | ✗ | ✗ | F3: adapted Hadamard countermodel | LP-134∞ conjectural | Global zero-set dynamics; every calendar has a non-arithmetic countermodel |
| 22 | Montgomery pair correlation / exchange rate T9 / sine kernel | 7 (P7b), 9 (T9A, T9cal) | phase-9-unconditional-universality/T9A, phase-9-unconditional-universality/T9cal, phase-7-weil-carleson-sine-kernel/P7b | ✗ | ✗ | ✗ | wrong sign; E1 | full Montgomery | Linear in Λ via explicit formula, statistical |
| 23 | Rodgers–Tao coupled heat flow | 8 (RT-coupled), 70 | phase-8-heat-flow-monotonicity/RT-coupled; R160_S2 F46 | ✓ | ✗ | ✗ | E1 / upper pair correlation | — | Global flow, zero-side only |
| 24 | E(T)=Σ(β−½)² ≪ T/log T, density towers | 54/170, 55, 56 | phase-54/170, phase-55/174-176, R160_S2 F43 | ✗ | ✗ | ✗ | F3: all worlds (MV identity) | Tower 1 (Lindelöf-hard) | Average, linear MV identity |
| 25 | Hadamard depression / b_j lower bounds / 15 classical mechanisms | 23/24, 25/01, 25/111 | phase-23-two-scale-defect-structure/24, phase-25-lower-bounds-bj-audit/01, R160_S1 §2.6#40-41 | ✗ | ✗ | ✗ | OTHER: compatible with GMC tails | — | Local jets of the Hadamard product |
| 26 | Weil form semibounded realization / faithful compression / λ_min | 0 (0A1, 0A2), 3, 4 (B-2) | phase-0/0A1, phase-0/0A2, phase-3/phase3-plan, phase-4/B2-THEOREM | ~ | ✗ | ✗ | E1 | Galerkin pollution (R160_S1 I18) | The Weil form itself; linear in Λ |
| 27 | CCM spectral triples A_λ, ε₀≥0, trace positivity CTP, Cesàro in λ | 32, 33/70–79, 60, 61/O10, 62, 64 TASK-A, 71 | phase-60/REDUCCION-RH-CCM, phase-61/O10, phase-32/59-64, phase-62/C1, phase-64/TASK-A, phase-71 | ✗ | ✗ | ✗ | E1; window (finite λ) | gap uniformity | Finite-λ = window; limit is RH |
| 28 | Connes–Consani / Connes trace / Sonin, prolate (archimedean & p-adic) | 4 (RH-ENDGAME), 5 (B3.1, B2-semilocal), 15/M8, 61/O8, 60 | phase-4/RH-ENDGAME, phase-5/B3.1, phase-61/O8, R160_S2 F22 | ✗ | ✗ | ✗ | E1; p-adic Sonin rank 1 | — | Local/semilocal; no place carries zeros |
| 29 | Semilocal finite-S positivity, two-prime theorem, per-prime OS reflection | 5 (T3), 6 (M-OS-2), 45/135, 46/142, 47/145, 48/152 | phase-6-osterwalder-schrader-reflection/M-OS-2, phase-45/135, phase-46/142+47/145, R160_S2 F34, F36 | ✗ | ~ | ✗ | OTHER: G_p indefinite; Thm B low-frequency failure; impurity collective | GAP-135.A | Per-prime/finite-S is window-like; sign "irreducibly collective" — names (ii) but does not supply it |
| 30 | Incommensurable frames / Q-linear independence of log p | 47/148, 7 (N3), 50/158 | phase-47/148, phase-7-weil-carleson-sine-kernel/P7-OPEN-CORE, R160_S2 F41 | ✗ | ~ | ✗ | E1 (phase→inertia bridge = explicit formula); C=1 saturated | Open frame problem (148) | Uses arithmetic of log p but only as Bohr-torus coordinates, linear |
| 31 | Multiplicativity controls Weil sign (NG-F1) | 60 | R160_S2 F37 | ✗ | ~ | ✗ | F3: smooth non-multiplicative controls | — | Test was numerical; separation was smoothness |
| 32 | Hodge index / Arakelov / Castelnuovo–Severi / Faltings–Hriljac | 15 (M1–M3, M10), 33/80, 40/124 | phase-15-arithmetic-hodge-index/M3, phase-15-arithmetic-hodge-index/M10, phase-33/80, phase-40/124 | ~ | ✗ | ✗ | E1; heights not zeros | Witness variety X (M10) | Global intersection form, but M3 = RH; no Λ coupling |
| 33 | Deninger foliation / Forni dynamical Hodge / Morishita | 42/127–128, 43/129–130 | phase-42/127, phase-42/128, phase-43/129-130, R160_S2 F6/F7 | ~ | ✗ | ✗ | E1; MW-5 object absent | Kähler–Riemann foliation existence | Scaling-flow trace = prime side of explicit formula (linear) |
| 34 | Lefschetz / J-linear Frobenius / Kähler sl₂ / tropical AHK | 15 (M4–M5), 41/125–126, 63, 107 | phase-15-arithmetic-hodge-index/M4-M5, phase-41/125-126, phase-63/R1-R3, phase-107/107_00 | ✗ | ✗ | ✗ | F3 function-field; T1; LI | — | No global object over ℤ; Lefschetz = explicit formula |
| 35 | CC cohomology / Serre duality / square cohomology / D₀ self-pairing | 39/119–121, 40/122–123 | phase-39/119-121, phase-40/122, phase-40/123 | ✗ | ✗ | ✗ | structural gap | D₀ self-pairing (I14) | Object without positivity |
| 36 | Inertia functors / KK metric / homotopy inertia / quantum Stone | 51, 52, 53 | phase-51/160-161, phase-52/162-163, phase-53/164-165 | ✗ | ✗ | ✗ | E1 (Thm 161.9); MW-5 | — | Partition function is ζ (linear trace) |
| 37 | K-theory [H_C], APS η-invariant, Kreĭn↔Connes V.2 | 26, 28 (02, 03) | phase-26-krein-connes-bridge, phase-28-four-fronts/02, phase-28-four-fronts/03 | ✗ | ✗ | ✗ | E1 (tautological) | η(T0)=0 open | Index invariants ⟺ RH |
| 38 | Function-field transfer / Deligne / Poincaré duality in MM | 30/56, 33/74, 29/49 | phase-33/74, phase-30-langlands-bridge-c-infinity/56, phase-29-zeta-spectral-triples/49,52 | ✗ | ✗ | ✗ | F3 function-field; W8; E1 | — | Uses geometry absent over ℤ |
| 39 | Modular surface / Eisenstein resonance / Maass–Selberg | 16 (01–05) | phase-16-surf-witness-variety/01-05 | ✗ | ✗ | ✗ | CAP; definite (F3 all configurations) | — | Pairing definite for every configuration |
| 40 | Langlands / Selberg class / Kaczorowski–Perelli / Motohashi | 14 (M14), 30/55, 48/153 | phase-30-langlands-bridge-c-infinity/55, phase-14-off-diagonal-anchor-asymmetry/M14.1-3, phase-48/153 | ✗ | ✗ | ✗ | E1; self-referential | — | Transfers return RH for ζ |
| 41 | Prismatic / Sen / Hodge–Tate grading | 15/M6 | phase-15-arithmetic-hodge-index/M6 | ✗ | ✗ | ✗ | wrong side (local Satake) | — | Local data |
| 42 | Quantum q-index / q-Shapovalov / Bost–Connes / compact quantum group | 67 | phase-67; R160_S2 F23 | ✗ | ✗ | ✗ | Bost–Connes ansatz; Haar kills interference | — | Acts on finite truncation D_N (E67_15: finite q-trace forcing tautological) |
| 43 | GLT / Widom symbol / Toeplitz symbol positivity | 68 | phase-68; R160_S2 F24 | ✗ | ✗ | ✗ | object not GLT | symbol-depth detector | Finite-window symbol |
| 44 | Nevanlinna / Cayley exact signed index, inertia readers, Maslov | 35/100, 37/110, 49, 69 | phase-69, phase-37/110, phase-49/154-157, phase-35/100 | ✗ | ✗ | ✗ | Weil wall (E1) | Cayley signed index (named, not built) | Index counts ⟺ zero location |
| 45 | Feshbach / Schur / signature continuity / rank-one escape (Ω₇) | 64, 65, 66, 71–74 | phase-65/RH-PROOF, phase-66/Omega7, phase-72..74 | ✗ | ✗ | ✗ | E1; attribution gate E72.16 | critical endpoint | Finite windows; detectors not forcers |
| 46 | RDI / bordered anchor / Kato current / cofactor–adjugate chain | 75–101 | phase-80, phase-93/E93_002, phase-94..100, phase-91/E91_004, phase-92 | ~ | ✗ | ✗ | E1; exact identities, no sign | CA-1 convergence | Determinant identities transport DIRECT-BORD; certified to 1e-96, signless |
| 47 | Γ–Euler coboundary / intertwiner / semigroup deformation | 83, 87 | phase-83/E83_003, E83_008, phase-87 | ✗ | ✗ | ✗ | domain obstruction (ker X={0}) | — | Γ and Euler independent |
| 48 | Self-adjoint perturbation determinant = Euler product | 64/106 | phase-106/106_00; R160_S2 F17-F18 | ✗ | ✗ | ✗ | zero-free off ℝ | — | Cannot vanish at Euler zeros |
| 49 | Tate canonical system / Lax–Phillips angle / colligation | 61/O8, 64 | R160_S2 §5b5 phase-64, F21, §3.2 phase-61 O8 | ✗ | ✗ | ✗ | E1; passivity collective divergence | (superseded by R162_2701) | Finite-S product diverges at critical value |
| 50 | Tensor-power amplification (⊠, superadditive κ) | 36/106, 38/117, 44/45 | phase-36/106+38/117; R160_S2 F47 | ✗ | ✗ | ✗ | dilution σ₀=0 both worlds | R-FIN sublinear bound | Window indices binary |
| 51 | Diophantine / Liouville of ξ discriminant | 50/158–159 | phase-50/158-159 | ✗ | ✗ | ✗ | destructor 159 | GAP-179.B | No tool |
| 52 | Tauberian crossing (Wiener–Ikehara, Pitt, Karamata) | 49/157 | R160_S2 F40 | ✗ | ✗ | ✗ | E1 | GAP-157.A non-local with LI | Frequency-local ⟺ RH; linear in Λ |
| 53 | Sieve-to-index bridge | 36/108 | phase-36/108 | ✗ | ✗ | ✗ | E1 | Sub-resolution blindness (I6) | Average over windows |
| 54 | Mollifier / Farmer floor / boundary flux at σ=½ | 58, 59 | phase-58/188+59/191, phase-58/189+59/194 | ✗ | ✗ | ✗ | Thm 197.B / Littlewood first moment | GAP-189.1 ζ-correlated weights | Linear moment pipeline |
| 55 | Class-𝔄 detectors / non-collapsibility (Thm 198.2) | 55/59, 58/190 | phase-58/190+59/198, R160_S2 F44-F45 | ✗ | ✗ | ✗ | S1/S2/S3 disjunction | GAP-198.1 cross-coin | Detectors pay microscopic correlations |
| 56 | Theta kernel / Pólya-type positive kernels / Stieltjes / heat compactification | 101, 103/15–30, 106 | phase-103/103_15…, phase-103/103_30, phase-101/E101_024, E101_033 | ✗ | ✗ | ✗ | F3: positive kernels with off-axis zeros | — | Class property ⇒ identification wall |
| 57 | Corner Tate pairing / one-sided Λ pairing / prime-power pairings | 108, 109 | phase-108/108_17…, phase-109/109_99, R160_S3 §2.2#12 | ✗ | ~ | ✗ | radical prime-power-determined (zero-blind) | Stage 7 scaling compatibility (open) | Uses atomic prime powers but pairing is zero-blind (sin πx witness) |
| 58 | ξ-divisibility on compact support | 110 | phase-110/110_99; R160_S3 §2.2#13 | ✗ | ✗ | ✗ | Γ growth vacuity | — | Empty space |

(Rows 15, 26–58 additionally absorb minor grid rows of the same device: e.g. phase-17-surf-2-design SURF/real structure → 37/symmetry; phase-18-negative-directions-portrait negative directions, phase-22-pontryagin-finite-defect Pontryagin defect → 26; phase-13-omega-class-multiplicative-chaos/19 ω-class → 24 (RH-independent); phase-101 Loewner/jet compressions, phase-105 Sturm/Bregman → 14; phase-106 heat flow/mean-periodic/Birman–Schwinger → 56; phase-107 local sources/Néron → 34.)

## Counts

- 3 of 3: **none** (row 1 is the only one with (iii) arguable; counted as 2).
- 2 of 3: **7** (rows 1–5, 7, 8).
- 1 of 3: row 6 ((ii) only) and rows 9–21 ((i) only: global zero-side objects killed by E1 or M_m).
- 0 of 3: rows 22–58 (marks "~" not counted).

## Grouped by pair

**{i, ii}** (global + non-linear atomic primes; all fail (iii) by E1 or by an extra term)
- Dirichlet-shift square / Wiener–Hopf Euler–Γ factor (phase 70, E70_10; R160_S2 F54) — (iii) arguable; killer F2. **The strongest candidate in 0–110.**
- Lee–Yang / Euler–Möbius connection (phase 70, E70_4/E70_7/E70_11) — E1 via AHM→Weil.
- Sign of |ζ|²−|ζ_on|², dν, relative entropy (phase 33/83,86,89) — E1.

**{ii, iii}** (non-linear atomic primes, not a reduction; no node-set globality)
- Multiplicative chaos / freezing (phase 12) — probabilistic–deterministic gap.
- Adelic local–global Hasse–Minkowski (phase 27) — MW-3 walls A/B.
- Epstein test (phase 8) — a falsifier, not a mechanism.
- Two-variable Weil form W₂, Λ\*Λ block (phase 36/107) — (iii) only "~", superseded by R162_2702a.

**{i, iii}**: none. (Every global object in 0–110 is either zero-only ⇒ M_m, or an explicit-formula identity ⇒ E1.)

Note: Bagchi/Voronin (row 6, phase 35/102) meets (ii) only (killed by E1); it sits in the top block of the table only because of sorting by (ii)-content.

## Reading

The only device in phases 0–110 that is simultaneously global (Wiener–Hopf) and non-linear in atomic Λ is the **phase-70 Dirichlet square** (I−V)\*(I−V), V = Σ Λ(n)n^{−1/2}S_{log n}. Its documented obstruction is precisely the ratio comb Σ_{r∈ℚ} c_r S_{log r} with c_r = Σ Λ(bj)Λ(aj)… — the multiplicative (ii)-content appears and is exactly what the archimedean operator cannot absorb. Residue: a grading/quotient cancelling the Euler square (E70_10 final section; R160_S2 F54 "viable factor needs grading/quotient"). Recommended cross-check against phases 161 (sum-product square) and 166 R166_301 (Wiener–Hopf 2×2 symbol, killed W-TK) before reopening.
