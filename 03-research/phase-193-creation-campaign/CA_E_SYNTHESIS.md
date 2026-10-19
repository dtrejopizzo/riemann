# CA_E_SYNTHESIS — Front E (quantum mathematics and operator algebras), phase 193

Pen and paper; no numerics. **No sign contact. No negative value for ζ.
No clause of (R) moved.** Memos: CA_E_000_SEEDS.md (12 seeds, pre-screen), CA_E_001_COMMUTATIVE_COLLAPSE.md (development of E4/E5).

## Why the area is exhausted: the commutative collapse (CA_E_001, PROVED)
By thm:oneprofile and prop:AM the target is the positive definiteness of φ(q) = 𝖡(log q) on the **abelian** group ℚ_{>0}^×. Hence:
- **Thm 1 (separability).** Positivity on Euler-product (product, "separable") Dirichlet test vectors is equivalent to the target. No
  growth assumption is needed. Cor 1.1 gives a Fejér-point form: Fejér means of φ on divisor boxes, twisted by any unimodular completely
  multiplicative y in the solenoid Ĝ, must be ≥ 0.
- **Cor 1.2.** Positive = completely positive = block positive for the Schur multiplier of φ. Entanglement, decomposability, Choi rank
  and NC hierarchies distinguish nothing here.
- **Thm 2 (Schur NO-GO).** φ ≠ g·b for PD g, b with g a product kernel having an atomless local factor (GCD/Smith, Haagerup,
  Gaussian, ITPFI/primon kernels), or with g Haar-absolutely-continuous. Reason: the Bochner measure of φ is carried by the Kronecker
  line ι(ℝ), and μ_g * μ_b gives every translate of the line measure 0.
Both theorems are comb-generic ((B″)) and Thm 1 is a restatement (REF-D), so neither is a sign step. Together they say this: the
non-commutative leverage of quantum information is void for the global target. At a fixed window the only non-commutativity is the
compression (time limit + Tate jets), which is the closed Sonin/prolate/Wiener–Hopf territory (ARGUED).

## Subareas tried and killing clauses
| subarea | seed | killing clause |
|---|---|---|
| KMS / phase transitions beyond BC (Laca–Raeburn ℕ⋊ℕ^×, Cuntz–Li) | E1 | KMS positivity only at real β; O11 (semigroup density); (R)(2) no Γ; retry 114_d_116 |
| Tomita–Takesaki, Connes RN cocycle criterion | E2 | summands not weights (split = REF-D); commutative ⇒ pointwise symbol, false at τ = 0; (R)(5) |
| Subfactors, Jones index, TL positivity | E3 | no object; Hecke-pair indices = (I)+semigroup, O6 survives, (R)(2); integer-invariant collapse (CA_A_008) |
| CP maps, Choi, entanglement witnesses, decomposability | E4 | commutative collapse: REF-D, B″ (CA_E_001 Thm 1, Cor 1.2) |
| Schur multipliers / GCD / Haagerup product kernels | E5 | NO-GO PROVED (CA_E_001 Thm 2) |
| CCR/CAR quasi-free states, Robertson, second quantization, Fock | E6 | retry (114_d_92, 114_d_142, 114_d_195, R178); the state's positivity is the global square (R)(3) |
| ITPFI / Araki–Woods type, Kakutani at β = ½ | E7 | O11/O15 (density only), (R)(7); Thm U; CA_E_001 Thm 2 |
| Golden–Thompson, Peierls–Bogoliubov, Gibbs variational | E8 | (B′) estimate; summands commute before compression |
| Kadison–Singer / MSS interlacing, real stability, Lee–Yang | E9 | retry (phase 11, PF walls, DBN/N5); (B′); class argument; (R)(4) |
| Araki relative entropy, data processing, Petz | E10 | retry (phase-120 P3, R177); monotonicity points the wrong way (lem:monoT) |
| Operator systems, spectral truncations, Arveson extension | E11 | REF-D (Kreĭn extension, thm:KEPdich); P45-1 |
| NC-SOS / DPS / quantum de Finetti hierarchies | E12 | (R)(3) class (D); reduces to classical SOS by the collapse |
| free probability; CQG prime current; OS/reflection positivity | — | excluded by the coordinator (CA_C_006; NG-67; CA_A_007) |

## Tools left for other fronts
- CA_E_001 Thm 1 / Cor 1.1: a proof or a falsifier may be sought among Euler-product tests and Fejér points y ∈ Ĝ, including points
  off the Kronecker line, which the campaign never used. Low priority. Running it would be NUMÉRICO (a falsifier search only), and it is
  not strictly necessary.
- CA_E_001 Thm 2: closes Schur/Hadamard factorizations through product-state kernels in one stroke. What survives is the convolution
  factorization of the profile measure, a zero-side statement ((R)(4), ARGUED).

## Proposed YES→NO moves (pending review)
- "Quantum-information positivity (CP, Choi, entanglement witnesses, decomposability, operator-system or NC-SOS hierarchies) carries
  the sign" → NO (PROVED: commutative collapse).
- "The Euler product enters as a product-state / GCD Schur factor of the Gram kernel" → NO (PROVED, Thm 2).
- "KMS / modular / ITPFI type data at β = ½ carry the sign" → NO (real β only; density-level, O11).

Front E stops here: every subarea listed in the brief has been tried, and each has a killing clause.
