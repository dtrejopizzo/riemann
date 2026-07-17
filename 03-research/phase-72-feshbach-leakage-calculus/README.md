# Phase 72 -- Pole-relative Feshbach leakage calculus

**Opened:** 2026-07-07.

Phase 71 reduced the CCM stable-divisor problem to the convergence of the finite Weil ground state
`theta_x` to the prolate model state `k_lambda`. The first reduction asked for the strong global
estimate

```text
||H_x-H_x^0|| = o(g_x).
```

Phase 65 already showed why estimates of this global strong-resolvent kind are exactly where the
Connes route stalls. Phase 72 therefore changes the missing tool.

The new target is not global operator convergence. The first sufficient replacement was **ground-state
leakage**:

```text
||Q_x^0 (H_x-H_x^0) P_x^0|| = o(g_x),
```

after the pole-relative/Feshbach shorting has removed the definite rank-one pole mode.

Here `P_x^0` is the rank-one prolate ground-state projection, `Q_x^0=1-P_x^0`, and `g_x` is the prolate
spectral gap. E72.3 then sharpens this further: the actual quantity that moves the eigenvector is the
**reduced leakage**

```text
||C_x^{-1}Q_x^0 (H_x-H_x^0) k_lambda|| -> 0.
```

The diagonal part merely shifts the ground energy; the high-energy block can be large; even high-mode
leakage is harmless if it is killed by the compressed complement inverse.

## Documents

- **[E72.1](E72_1_FESHBACH_LEAKAGE_THEOREM.md)** -- proves the leakage theorem: a small off-diagonal
  Feshbach coupling, plus a lower bound on the compressed complement, implies
  `theta_x -> k_lambda` and therefore closes the Phase 71 stable-divisor bridge. The remaining new
  arithmetic estimate is the leakage bound itself.

- **[E72.2](E72_2_PRIOR_SONIN_FAILURE_AUDIT.md)** -- reads the earlier Sonin/prolate attempts
  (Phase 32, Doc 100, Docs 120/124, Phase 4/60 context) and records the constraints: no PCN/local
  Christoffel kernel, no `1/log gamma` scale, no spectral positivity rebranded as Hodge, and no
  unproved semilocal uniformity. Phase 72 must be a projected leakage estimate, not a locality theorem.

- **[E72.3](E72_3_REDUCED_LEAKAGE_THEOREM.md)** -- improves the target again: the ground vector is
  controlled by the reduced leakage `C_x^{-1}Q_x(H_x-H_x^0)k_lambda`, not by the raw leakage divided by
  the gap. This permits harmless high-mode excitation and turns the arithmetic target into a projected
  coboundary formula.

- **[E72.4](E72_4_DUAL_VARIATIONAL_LEAKAGE.md)** -- rewrites reduced leakage exactly as a dual
  first-variation norm:
  `sup |<v,(H_x-H_x^0)k_lambda>|/||C_xv||`. This is the clean load-bearing identity for a future
  Feshbach-Sonin integration-by-parts proof.

- **[E72.5](E72_5_PRIOR_FESHBACH_FAILURE_AUDIT.md)** -- audits prior Feshbach/Schur uses. It records
  what is safe (shorting, Haynsworth, actual compressed complement) and what is forbidden (subtraction,
  additive Green assembly, sourced Euler products, endpoint identification from scalar determinants).

- **[E72.6](E72_6_LOW_HIGH_REDUCED_LEAKAGE_CRITERION.md)** -- splits reduced leakage into a finite
  low-channel cancellation problem plus a uniform reduced-tail/tightness estimate, using the spectrum of
  the actual compressed complement `C_x`.

- **[E72.7](E72_7_NONCIRCULAR_VARIATIONAL_GATE.md)** -- adds the no-self-deception gate: the coboundary
  primitive `u_x` must be constructed from Sonin/prolate boundary calculus, not by applying `C_x^{-1}` to
  the residual or by importing the endpoint resolvent.

- **[E72.8](E72_8_CORRECTOR_EQUATION_ATTEMPT.md)** -- develops the boundary-corrector equation. It proves
  that a non-circular trace/mismatch/corrector triple implies reduced leakage, and isolates the exact
  missing lemmas: graph trace, vanishing actual/model boundary mismatch, and reduced bulk tightness.

- **[E72.9](E72_9_MODEL_COMPLEMENT_PRIMITIVE_PSC.md)** -- integrates the parallel audit/proof attempt.
  It introduces the allowed model primitive `u_x^0=(C_x^0)^{-1}b_x`, proves the model-primitive
  criterion, and isolates **PSC**, the one-vector pole-relative Prolate-Sonin coboundary lemma, as the
  first exact missing theorem.

- **[E72.10](E72_10_MODEL_COMMUTATOR_COBORDISM.md)** -- sharpens PSC into a commutator mechanism.
  If `Q_xR_xk_x = Q_x[C_x^0,A_x]k_x + e_x` with a small model transport primitive
  `Q_xA_xk_x`, then PSC follows. The next object is an explicit pole-relative prolate boundary transport
  `A_x`.

- **[E72.11](E72_11_DOOB_POISSON_TRANSPORT.md)** -- computes the commutator in Doob coordinates. It
  shows that MCC is equivalent to a one-source Doob-Poisson smoothing statement for
  `F_x/k_x`, where `F_x=Q_x(H_x-H_x^0)k_x`.

- **[E72.12](E72_12_ONE_DIMENSIONAL_POISSON_FORMULA.md)** -- solves the Doob-Poisson equation explicitly
  in one dimension. The primitive is controlled by the weighted cumulative residual force
  `G_x(theta)=int_a^theta k_x F_x`, giving the concrete cumulative-cancellation target CC.

- **[E72.13](E72_13_CENTERED_CUMULATIVE_KERNELS.md)** -- expands the cumulative residual force exactly
  as a coherent sum of centered cumulative cell kernels. The proof target becomes the centered
  cumulative Gram cancellation `omega_x^*M_xomega_x=o(lambda_{x,1}^D)`.

- **[E72.14](E72_14_ABEL_CCG_REDUCTION.md)** -- applies Abel summation to the centered cumulative
  kernels. After model-main matching, CCG reduces to a Hilbert-valued Chebyshev discrepancy estimate
  against `partial_u K_x(u)`.

- **[E72.15](E72_15_ACD_RESONANCE_BARRIER.md)** -- expands the Abel-Chebyshev vector by the explicit
  formula. It proves that ACD is equivalent to annihilating the Hilbert-valued zero-resonance vectors
  `R_x(rho)`. Any non-annihilated off-line zero violates ACD, so PNT-scale estimates cannot close the
  route.

- **[E72.16](E72_16_ZERO_FILTER_GATE.md)** -- proves the zero-filter gate: any scalar Mellin-limit proof
  of `R_x(rho)->0` produces an analytic function whose divisor contains the off-critical zeta divisor.
  If that filter is `Xi` in disguise, the proof is circular. The remaining plausible path is vector
  cancellation among maximal zero resonances forced by finite CCM symmetry.

- **[E72.17](E72_17_MAXIMAL_RESONANCE_BLOCK.md)** -- proves that the functional equation and real
  conjugation do not automatically cancel the maximal off-line resonance block. ACD can survive an
  off-line zero only through a new null-vector identity in the resonance Gram matrix.

- **[E72.18](E72_18_FINITE_RESIDUE_COBORDISM.md)** -- introduces the finite residue cobordism: the
  finite CCM real-zero divisor has zero off-real residue current. If the finite relative current
  converges to the global `Xi` relative current against `R_x(s)/s`, the maximal resonance block cancels.
  This turns the missing identity into relative Cartwright current convergence.

- **[E72.19](E72_19_REAL_SUPPORT_CURRENT_CLOSURE.md)** -- proves the closure principle:
  distributional convergence of finite CCM divisor currents, all supported on the real axis, to the
  `Xi` divisor current implies RH. This isolates the exact non-circular theorem still needed:
  divisor-current convergence.

- **[E72.20](E72_20_POINCARE_LELONG_CURRENT_CRITERION.md)** -- proves the Poincare-Lelong criterion:
  relative potential convergence `log|F_x/G_x| -> log|Xi/G|` in `L^1_loc` implies finite divisor-current
  convergence, hence RH. This replaces zero tracking by a Cartwright potential theorem.

- **[E72.21](E72_21_BLASCHKE_DEFECT_OBSTRUCTION.md)** -- proves that real-axis modulus convergence
  cannot imply the potential/current convergence needed in E72.20: off-real Blaschke factors are
  invisible on the boundary. The missing theorem must control phase/current or exclude inner defects.

- **[E72.22](E72_22_TWO_HEIGHT_CURRENT_RIGIDITY.md)** -- proves a new rigidity criterion: convergence
  of finite real-divisor Cauchy transforms on two interior horizontal lines, plus local Hardy/normal
  bounds in the slab, rules out hidden Blaschke defects. This reduces Schur-free convergence to
  two-height log-current convergence with compactness.

- **[E72.23](E72_23_WEYL_LOG_CURRENT_FORMULA.md)** -- writes the finite divisor current directly from
  the CCM Weyl data:
  `P_x'/P_x=m_x'/m_x+Q_x'/Q_x`, with `m_x=sum xi_k/(s-d_k)`. The remaining theorem is Weyl two-height
  current convergence from the finite eigenvector equation.

- **[E72.24](E72_24_WEYL_RICCATI_TRANSPORT.md)** -- derives the Riccati mechanism: if
  `(A_x-eps_x)r_x(s)` lies in the span of `r_x(s)` and `partial_s r_x(s)` plus a Weyl-invisible error,
  then `m_x'/m_x` is forced, yielding WTCC and Schur-free current convergence.

- **[E72.25](E72_25_TWO_JET_TRANSPORT_FALSIFIER.md)** -- tests the direct two-jet vector transport and
  falsifies it numerically. The full residual is large, and the eigenvector channel is tautologically
  zero. The surviving target is current-level/commutator transport, not vector-level transport.

- **[E72.26](E72_26_BORDERED_PENCIL_CURRENT.md)** -- gives the exact finite current identity:
  `P_x(s)=-det[[0,xi_x^T],[1_x,sI-D_x]]`. Therefore the finite divisor current is the trace current of
  a bordered linear pencil. Schur-free convergence becomes bordered Fredholm convergence.

- **[E72.27](E72_27_RELATIVE_BORDERED_FREDHOLM_THEOREM.md)** -- proves the functional-analytic closure:
  trace-norm convergence of the relative bordered perturbations, plus determinant identification,
  gives locally uniform convergence of finite real-rooted spectral functions to `Xi`, hence RH.

- **[E72.28](E72_28_DETERMINANT_IDENTIFICATION_AUDIT.md)** -- audits the Fredholm theorem. Determinant
  identification alone is the Phase 71 convergence problem renamed. The genuinely new target is the
  bordered trace estimate `(BTE)`: trace-closeness of actual finite CCM bordered pencils to the prolate
  bordered pencils.

- **[E72.29](E72_29_RANK_ONE_BORDER_ESTIMATE.md)** -- computes the bordered perturbation when actual
  and model pencils share the pole mesh. Full trace BTE follows from vector convergence and may be too
  strong; the scalar current factor reduces to Weyl-weak convergence of `xi_x-k_x`.

- **[E72.30](E72_30_WEYL_WEAK_FESHBACH_THEOREM.md)** -- proves the weakest current-level Feshbach
  closure: Weyl-reduced leakage, tested only against Cauchy resolvent functionals and one derivative,
  implies Schur-free current convergence and hence RH.

- **[E72.31](E72_31_SCALAR_WRL_ABEL_FORM.md)** -- expands Weyl-reduced leakage into a scalar
  Abel-Chebyshev formula. The minimal arithmetic target is scalar WRL resonance annihilation for the
  single Weyl-Feshbach kernel `L_x(s;u)`.

- **[E72.32](E72_32_SCALAR_WRL_COBORDER_ATTEMPT.md)** -- attacks scalar WRL annihilation directly.
  It proves that ordinary coborders, smoothing estimates, and zero-independent Mellin symbols either
  fail or become zero-filters. The remaining possible proof must be a finite arithmetic spectral
  coborder for the scalar kernel.

- **[E72.33](E72_33_MELLIN_SPECTRAL_DIVISIBILITY.md)** -- identifies the only algebraic mechanism that
  can prove scalar WRL annihilation: Mellin spectral divisibility
  `M_x(s;z)=P_x(z)A_x(s;z)+E_x(s;z)`. It proves this would imply annihilation once the finite spectral
  polynomials converge, and shows that annihilation without divisibility creates a zero-filter.

- **[E72.34](E72_34_MELLIN_COFACTOR_CRITERION.md)** -- turns Mellin spectral divisibility into an exact
  finite cofactor criterion for the bordered pencil `B_x(z)`. A root-free proof must construct a
  factorized `B_x`-coboundary identity
  `M_x=a_x^TB_xb_x` with `B_xb_x=P_xc_x`.

- **[E72.35](E72_35_BORDERED_COHOMOLOGY_EQUATION.md)** -- derives the actual bordered cohomology
  equation and removes the adjugate tautology. It shows the proof must construct a finite concomitant
  identity making `M_x(s;z)` a multiple of the Weyl function `m_x(z)=P_x(z)/Q_x(z)` up to regular
  mesh cancellation.

- **[E72.36](E72_36_NAIVE_DISCRETE_DIVISIBILITY_FALSIFIER.md)** -- tests the raw discrete finite-cell
  Mellin scalar and falsifies exact divisibility by `P_x`. Any valid divisibility must be
  Abel-renormalized/model-subtracted, not a direct `sum n^z T_n` identity.

- **[E72.37](E72_37_NORMALIZED_MELLIN_PROBE.md)** -- tests the Abel-normalized scalar transform
  `sum (n/x)^z<v_s,T_nk>`. Unlike the raw transform, it is small at finite Weyl roots and decreases in
  the tested windows. This suggests endpoint Weyl-Feshbach tightness as the next estimate.

- **[E72.38](E72_38_ENDPOINT_TAPER_ESTIMATE.md)** -- proves the endpoint taper
  `|q_mn(y)|<=2(L-y)/L` for the finite CCM cells. This gives a real mechanism for the normalized
  Mellin smallness, conditional on a compressed channel bound for `v_{x,s}`.

- **[E72.39](E72_39_COMPRESSED_CHANNEL_BOUND.md)** -- converts endpoint taper into a sufficient theorem:
  post-main endpoint mass times the compressed channel bound implies normalized scalar WRL
  annihilation. It isolates two zero-free estimates to prove.

- **[E72.40](E72_40_POST_MAIN_ENDPOINT_MASS.md)** -- estimates the post-main Chebyshev discrepancy with
  endpoint taper. PNT gives `o(sqrt(x))`; therefore scalar WRL closes if the compressed channel supplies
  the missing `o(x^-1/2)` factor.

- **[E72.41](E72_41_WEIGHTED_CHANNEL_REFINEMENT.md)** -- tests the channel size and corrects the target:
  a uniform half-power bound is too strong, but the endpoint-weighted coherent channel sum is small.
  The remaining estimate is weighted endpoint Weyl-Feshbach cancellation.

- **[E72.42](E72_42_ENDPOINT_OPERATOR_PROBE.md)** -- tests the endpoint-weighted operator
  `S_x(z)=sum(n/x)^zT_n`. Operator norm is not the right target; the viable estimate is scalar endpoint
  orthogonality against the compressed Cauchy vector.

- **[E72.43](E72_43_ENDPOINT_COBORDER_LEMMA.md)** -- gives the endpoint coborder lemma: if
  `Q_xS_x(z)k_x=C_xw_x+e_x` with Weyl-small primitive and error, then scalar WRL annihilation follows.
  This is the renormalized Feshbach/Sonin target in the minimal current channel.

- **[E72.44](E72_44_ADJOINT_GREEN_PAIRING.md)** -- proves the adjoint Green pairing:
  `<Q_xr_s,w_z>` equals the mixed cumulative-energy integral
  `int G_{H_s}G_{F_z}/rho`. Endpoint Doob-Weyl smallness follows from bounded Weyl-test energy and
  endpoint cumulative-energy decay.

- **[E72.45](E72_45_ENDPOINT_CUMULATIVE_ENERGY_TARGET.md)** -- rewrites endpoint cumulative-energy
  decay as a Gram estimate for endpoint-weighted centered cumulative cells. A quadratic endpoint taper
  of the cumulative cells would prove the needed decay.

- **[E72.46](E72_46_CONTINUOUS_ENDPOINT_OPERATOR.md)** -- replaces the heuristic quadratic taper by a
  rigorous continuous endpoint-operator split. The endpoint layer gives entrywise
  `x^-1/2/L` smallness; the remaining tasks are Fourier/Bessel summation and scalar-compressed
  Chebyshev-discrepancy control.

- **[E72.47](E72_47_FOURIER_OVERLAP_BOUND.md)** -- proves the Fourier overlap bound
  `||Q_x(y)||<=2(1-y/L)`, eliminating the dimension-loss obstruction. Consequently the continuous
  endpoint operator has norm `O(x^-1/2/L)` on compact subsets of `Re z>1/2`.

- **[E72.48](E72_48_SCALAR_ENDPOINT_DISCREPANCY.md)** -- isolates the remaining arithmetic estimate:
  scalar endpoint discrepancy cancellation for
  `a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>`. All model/geometric endpoint pieces have been reduced to this
  one scalar compressed channel.

- **[E72.49](E72_49_BANDLIMITED_PNT_ENDPOINT_THEOREM.md)** -- tests the finite-bandwidth PNT route and
  corrects its scaling: classical PNT plus `N_x=O(L)` still leaves a half-power gap. The missing gain
  must come from the compressed scalar channel, not from bandwidth alone.

- **[E72.50](E72_50_HALF_POWER_WCB_PROBE.md)** -- measures the actual scalar endpoint channel and finds
  half-power-scale smallness in `sqrt(x)|<v_s,S_x(z)k>|`. The smallness is scalar, not a norm bound on
  `v_s`.

- **[E72.51](E72_51_FINITE_FREQUENCY_EXPANSION.md)** -- expands the scalar endpoint channel into
  finitely many Fourier modes. Classical PNT reduces the remaining discrepancy to an `l1`
  half-power bound on the compressed channel coefficients.

- **[E72.52](E72_52_HILBERT_COEFFICIENT_FORMULA.md)** -- expresses those coefficients as discrete
  Hilbert-transform combinations of `v_{x,s}` and `k_x`. Generic Hilbert bounds are insufficient, so
  the half-power must come from the Feshbach equation for `v`.

- **[E72.53](E72_53_AFFINE_FREQUENCY_CORRECTION.md)** -- corrects the finite-frequency expansion:
  the diagonal cell has an affine endpoint factor `(1-y/L)`. This adds exponent derivatives/log
  factors but preserves the finite-frequency strategy and splits the coefficient target into
  off-diagonal Hilbert and diagonal overlap pieces.

- **[E72.54](E72_54_LOEWNER_COMMUTATOR_IDENTITY.md)** -- proves the exact Loewner identity
  `Q_x(y)=2cos(yD)-(2/L)Lo_y`, with `[D,Lo_y]=[sin(yD),J]`. This turns the Hilbert coefficient
  obstruction into a finite commutator/Fréchet-derivative identity.

- **[E72.55](E72_55_LOEWNER_CANCELLATION_PROBE.md)** -- tests the Loewner split and finds that the
  weighted scalar channel is often one to two orders of magnitude smaller than the separate cosine and
  Loewner pieces. The missing proof must use their cancellation as a whole.

- **[E72.56](E72_56_ENDPOINT_RANK_ONE_EXPANSION.md)** -- derives the endpoint Taylor expansion
  `Q_x(L-r)=(2r/L)J+higher`. The Loewner cancellation collapses the endpoint cell to a rank-one leading
  term, so the next target is suppression of `<v_{x,s},1><1,k_x>`.

- **[E72.57](E72_57_LAMBDA_WEIGHTING_CORRECTION.md)** -- corrects the endpoint probes: the scalar WRL
  operator is `Lambda`-weighted. Unweighted support probes are structural only; all closure targets must
  use `S_x^Lambda(z)=sum Lambda(n)(n/x)^zT_n`.

- **[E72.58](E72_58_RANK_ONE_SUPPRESSION_FALSIFIER.md)** -- falsifies literal rank-one endpoint
  suppression: `<v,1><1,k>` is not small. The rank-one endpoint layer must be absorbed by the continuous
  model main term; the correct object is the prime-minus-continuous scalar endpoint discrepancy.

- **[E72.59](E72_59_PNT_MEASURE_CORRECTION.md)** -- corrects the PNT main measure in the endpoint
  operator: the continuous main uses `du`, hence `exp(y/2)dy`, and has size `O(sqrt(x)/L)`. Only the
  post-main Chebyshev-discrepancy channel is expected to be small.

- **[E72.60](E72_60_POST_MAIN_DISCREPANCY_PROBE.md)** -- measures the corrected post-main scalar
  endpoint discrepancy. The `prime-continuous` error is small in the finite harness; this becomes the
  LFDC target.

- **[E72.61](E72_61_ENDPOINT_REFLECTION_IDENTITY.md)** -- proves the exact endpoint reflection
  `Q_x(L-r)=(2/L)Lo_r` and rewrites LFDC as a reflected Loewner-Stieltjes pairing against the endpoint
  Chebyshev discrepancy. The remaining estimate is the Endpoint Reflected Inequality `(ERI)`.

- **[E72.62](E72_62_INTEGRATED_LOEWNER_COMMUTATOR.md)** -- integrates the Loewner commutator against
  the endpoint Chebyshev discrepancy. The LFDC operator `K_x^E(z)` satisfies
  `[D,K_x^E]=[Sigma_x^E,J]`, reducing the scalar estimate to the finite Cauchy-Hilbert coefficient
  identity `(ECHC)`.

- **[E72.63](E72_63_LOW_HIGH_CAUCHY_HILBERT_CLOSURE.md)** -- proves a low-high closure theorem:
  high endpoint exponential control plus low Feshbach current cancellation imply LFDC with one
  derivative, hence scalar WRL resonance annihilation through E72.30--E72.31.

- **[E72.64](E72_64_LOW_BLOCK_RESIDUE_IDENTITY.md)** -- identifies the low-frequency block with the
  Mellin residue functionals of the scalar WRL kernel. Low cancellation must therefore be proved by
  finite spectral divisibility, not by estimating endpoint transforms one by one.

- **[E72.65](E72_65_SPECTRAL_VARIABLE_ALIGNMENT.md)** -- corrects the variable alignment:
  Mellin exponent `rho` and CCM height `tau` are related by `rho=1/2+i tau`. Divisibility is by
  `P_x(tau)` for the height transform `widehat M_x(s;tau)`, not by `P_x` in the raw exponent variable.

- **[E72.66](E72_66_ENDPOINT_ONLY_DIVISIBILITY_FALSIFIER.md)** -- falsifies the shortcut that the
  endpoint post-main discrepancy alone is divisible by `P_x(tau)`. The spectral divisibility, if true,
  must belong to the full Abel-WRL boundary-minus-bulk concomitant.

- **[E72.67](E72_67_CELL_ABEL_DIVISIBILITY_FALSIFIER.md)** -- falsifies the next shortcut: the
  unnormalized continuous Abel transform of the overlap cell alone is not divisible by `P_x`. E72.68
  corrects the missing half-power factor.

- **[E72.68](E72_68_HALF_POWER_ABEL_CONCOMITANT.md)** -- writes the correct half-power Abel concomitant
  `A_x(tau)=Q_x(0)+(1/2+i tau)int exp(i tau y)Q_x(y)dy`, gives closed finite entries, and reduces scalar
  WRL annihilation to asymptotic divisibility of
  `<C_x^(-1)Q_x(sI-D_x)^(-1)1,A_x(tau)k_x>` by `P_x(tau)`.

- **[E72.69](E72_69_RESOLVENT_ALGEBRA_CERTIFICATE.md)** -- clears the mesh poles in the half-power
  concomitant and expresses divisibility as the explicit finite certificate `(CERT)`:
  an exponential-polynomial residual evaluated at finite roots of `P_x`, plus a normal quotient bound.
  The companion script **[E72_69_hpac_certificate_probe.py](E72_69_hpac_certificate_probe.py)** computes
  this finite-root residual in the Phase 71 harness.

- **[E72.70](E72_70_ABEL_GENERATOR_IDENTITY.md)** -- removes the HPAC boundary term by integration by
  parts and proves
  `A_x(tau)=int exp(i tau y)((1/2)Q_x(y)-Q_x'(y))dy`. Divisibility becomes the finite
  generator-root identity `(GEN-root)`.

- **[E72.71](E72_71_TWO_RESOLVENT_HPAC_IDENTITY.md)** -- identifies `Q_x(y)` as a symmetrized
  one-sided translation overlap and proves the closed HPAC formula:
  two diagonal resolvents `(tau I+-D)^(-1)` plus two rank-one terms. The finite certificate is now the
  scalar two-resolvent cancellation `(2R-CERT)`.

- **[E72.72](E72_72_WEYL_NULL_SPLIT.md)** -- uses the finite-root relation
  `<xi_x,(tau_jI-D)^(-1)1>=0` to split the HPAC residual into an actual-divisor core and a
  model/actual displacement term. Numerically the core is much smaller; the remaining estimate is an
  HPAC displacement norm, not full vector convergence.

- **[E72.73](E72_73_PARITY_CORE_REDUCTION.md)** -- uses parity to show that, at finite roots, both
  `<xi_x,r_->` and `<xi_x,r_+>` vanish. The actual-divisor core collapses to the even-sector pairing
  `<v_even,2tau(tau^2-D^2)^(-1)xi_x>`.

- **[E72.74](E72_74_EVEN_SECTOR_HPAC_CERTIFICATE.md)** -- collapses the full HPAC scalar, not just the
  core, to the even sector:
  `F_x/alpha=i<v_even,S_tau k>-(E_tau-1)L^(-1)<v_even,S_tau1><r_-,k>`. At finite roots the last factor
  is `<r_-,k_x-xi_x>`.

- **[E72.75](E72_75_EVEN_COBORDER_CERTIFICATE.md)** -- rewrites `EV-CERT` as an exact shorted coborder:
  `F_x/alpha=<Q r_s^even,C_even^(-1)QW_j>`. The raw source `QW_j` need not be small; the target is Weyl
  invisibility after Feshbach shorting. The companion script
  **[E72_75_even_coborder_probe.py](E72_75_even_coborder_probe.py)** measures the raw, shorted, and
  Weyl-paired sizes.

- **[E72.76](E72_76_CORE_DISPLACEMENT_SPLIT.md)** -- splits the even coborder source into
  `W_j^core=iS_jxi_x` and a rank-one-corrected displacement source involving `h_x=k_x-xi_x`. The core
  is numerically tiny after shorting; the remaining hard estimate is the displacement certificate. The
  companion script **[E72_76_core_displacement_probe.py](E72_76_core_displacement_probe.py)** measures
  the two pieces separately.

- **[E72.77](E72_77_DISPLACEMENT_HPAC_GATE.md)** -- identifies the displacement certificate as
  `HPAC_x[h_x]` at finite roots and records the non-circularity gate: it cannot be closed by assuming
  `k_x->xi_x`; it must be proved directly in the even shorted Weyl-Feshbach norm.

- **[E72.78](E72_78_CORE_CAUCHY_ROOT_IDENTITY.md)** -- proves the unshorted core identity
  `<r_s^even,S_jxi_x> = -2tau_j m_x(conjugate(s))/(conjugate(s)^2-tau_j^2)`. This explains the core
  cancellation and isolates the remaining content as Feshbach shorting. The companion script
  **[E72_78_core_cauchy_identity_probe.py](E72_78_core_cauchy_identity_probe.py)** checks the Hermitian
  formula.

- **[E72.79](E72_79_SHORTED_BORDERED_MINOR_CERTIFICATE.md)** -- removes the last opaque inverse from
  the even Feshbach certificate. In an orthonormal basis of the even `Q_x`-space,
  `<Q r_s^even,C_even^(-1)QW_j>` is exactly
  `-det[[C_E,b_j],[a_s^*,0]]/det(C_E)`. The companion script
  **[E72_79_bordered_minor_probe.py](E72_79_bordered_minor_probe.py)** verifies the determinant formula
  against the direct solve to roundoff for core, displacement, and total sources.

- **[E72.80](E72_80_ROOT_REMAINDER_CERTIFICATE.md)** -- replaces informal divisibility by the exact
  finite root-remainder statement. Since the bordered minor is rational-exponential in `tau`, the
  correct certificate is the interpolation remainder of `N_x(s;tau)/det(C_E)` on the finite Weyl roots.
  The companion script **[E72_80_root_remainder_probe.py](E72_80_root_remainder_probe.py)** checks that
  the finite remainder reproduces the root residuals to roundoff.

- **[E72.81](E72_81_DUAL_COFACTOR_TRANSPORT.md)** -- factors the bordered-minor residual through the
  dual cofactor vector `g_{x,s}=B_xC_E^(-1)B_x^*r_s^even`. The residual becomes the scalar transport
  identity
  `iC_{g,k}(tau)-(exp(i tau L)-1)L^(-1)C_{g,1}(tau)M_k(tau)` at finite Weyl roots. The companion script
  **[E72_81_dual_cofactor_transport_probe.py](E72_81_dual_cofactor_transport_probe.py)** verifies the
  factorization and the finite-root replacement `M_h=M_k` to roundoff.

- **[E72.82](E72_82_MESH_COTANGENT_SHORTCUT_AUDIT.md)** -- tests the tempting shortcut that the HPAC
  boundary factor and the uniform mesh Cauchy sum alone give
  `(exp(i tau L)-1)L^(-1)M_1(tau) approx i`. The test fails in the active finite windows, so the current
  minimal theorem remains the full dual cofactor transport identity, not a universal mesh cotangent
  cancellation. The companion script **[E72_82_mesh_cotangent_probe.py](E72_82_mesh_cotangent_probe.py)**
  records the numerical falsifier.

- **[E72.83](E72_83_DUAL_COFACTOR_BANDLIMIT.md)** -- identifies a positive compactness mechanism:
  for fixed `s`, the dual cofactor vector `g_{x,s}` is not low rank but is sharply fixed-band tight in
  the finite harness. E72.84 corrects the invariant formulation: the stable cutoff is physical height
  `|d_n|`, not fixed index `|n|`. The companion script
  **[E72_83_dual_cofactor_bandlimit_probe.py](E72_83_dual_cofactor_bandlimit_probe.py)** records the
  original frequency concentration.

- **[E72.84](E72_84_PHYSICAL_HEIGHT_COFACTOR_TIGHTNESS.md)** -- replaces fixed-index tightness by
  physical-height tightness `(PDCT)`. For several `s` values, the cofactor mass concentrates below a
  physical cutoff just above the height of `s`. The companion script
  **[E72_84_dual_cofactor_physical_tightness_probe.py](E72_84_dual_cofactor_physical_tightness_probe.py)**
  verifies the corrected formulation.

- **[E72.85](E72_85_HIGH_LOW_BLOCK_CRITERION.md)** -- derives the exact high/low graph identity
  `g_H=C_HH^(-1)a_H-C_HH^(-1)C_HLg_L`. The block coupling is small in the harness, but not visibly
  decaying, so the two-block operator estimate is too coarse to prove `(PDCT)`. The companion script
  **[E72_85_high_low_block_probe.py](E72_85_high_low_block_probe.py)** records the block sizes.

- **[E72.86](E72_86_BUFFERED_GREEN_DECAY_AUDIT.md)** -- tests the stronger buffered operator-norm
  route `||T_HC_E^(-1)S_R|| -> 0`. The norms are small but do not decisively decay with the buffer, so
  the proof must use the specific Cauchy source rather than every source in a physical band. The
  companion script **[E72_86_buffered_green_decay_probe.py](E72_86_buffered_green_decay_probe.py)**
  records the audit.

- **[E72.87](E72_87_CCGD_QUADRATIC_CERTIFICATE.md)** -- turns the surviving Cauchy-channel Green decay
  `(CCGD)` into an exact finite quadratic inequality:
  `a^*C_E^(-1)K_HC_E^(-1)a / a^*C_E^(-2)a -> 0`. The companion script
  **[E72_87_ccgd_certificate_probe.py](E72_87_ccgd_certificate_probe.py)** verifies the quadratic
  certificate against direct tail computation to roundoff.

- **[E72.88](E72_88_FINITE_BAND_TRANSPORT_REDUCTION.md)** -- checks that physical cofactor tightness
  transfers to the actual transport residual. Once the cutoff `H` is above the Cauchy height of `s`,
  the finite-band residual tracks the full residual to `1e-5--1e-4` in the tested windows. The companion
  script **[E72_88_finite_band_transport_probe.py](E72_88_finite_band_transport_probe.py)** records the
  full/band/tail comparison.

- **[E72.89](E72_89_FINITE_BAND_ROOT_REMAINDER.md)** -- states the current minimal finite identity:
  after `(CCGD-QR)`, scalar WRL is reduced to the vanishing of the interpolation remainder of the
  finite-band transport residual `R_{x,H}(s;tau)` on the finite Weyl roots. This gives the clean split:
  a finite quadratic inequality in `s`, plus a finite root-remainder identity in `tau`.

- **[E72.90](E72_90_FINITE_BAND_TRANSPORT_SCALING.md)** -- tests whether the finite-band residual
  visibly decays once the Cauchy tail is small. It does not show clean monotone decay; changing `H`
  barely changes the value after the tail is removed. The companion script
  **[E72_90_fbrt_scaling_probe.py](E72_90_fbrt_scaling_probe.py)** records the scaling audit.

- **[E72.91](E72_91_LOW_BAND_COFACTOR_IDENTITY.md)** -- factors finite-band transport through a single
  transported cofactor vector
  `phi_{x,H,tau}=B_xC_E^(-1)B_x^*P_HZ_x(tau)`, giving
  `R_{x,H}(s;tau)=<r_s^even,phi_{x,H,tau}>`. The companion script
  **[E72_91_low_band_cofactor_probe.py](E72_91_low_band_cofactor_probe.py)** verifies the identity to
  roundoff.

- **[E72.92](E72_92_PHI_INVISIBILITY_AUDIT.md)** -- tests whether `phi` is norm-small. It is not small
  enough uniformly; some Cauchy pairings are a large fraction of `||phi||`. The proof must be Cauchy
  invisibility, not a Hilbert norm estimate. The companion script
  **[E72_92_phi_invisibility_probe.py](E72_92_phi_invisibility_probe.py)** records the audit.

- **[E72.93](E72_93_FINITE_BAND_STIELTJES_MOMENT_CRITERION.md)** -- converts finite-band Cauchy
  invisibility into the Stieltjes transform and moment criterion for `phi`. The companion script
  **[E72_93_moment_probe.py](E72_93_moment_probe.py)** measures low-moment coherences.

- **[E72.94](E72_94_MOMENT_SHORTCUT_AUDIT.md)** -- shows that a few low moments do not explain the
  cancellation: many normalized moment coherences are close to `1`. The remaining identity is
  root-specific, not generic low-moment decay.

- **[E72.95](E72_95_LOW_RANK_ALIGNMENT_AUDIT.md)** -- tests whether `phi` lies near
  `span{xi_x,k_x-xi_x,1}`. It does not; residuals are typically `0.7--0.99`. The companion script
  **[E72_95_phi_alignment_probe.py](E72_95_phi_alignment_probe.py)** records the low-rank falsifier.

- **[E72.96](E72_96_UNIFIED_FINITE_CERTIFICATE.md)** -- packages the current reduction into two finite
  defects: `D1`, the Cauchy-channel physical tail, and `D2`, the finite-band root-specific Stieltjes
  defect. The companion script
  **[E72_96_unified_certificate_probe.py](E72_96_unified_certificate_probe.py)** computes both defects
  from the same finite data and verifies the quadratic tail formula to roundoff.

- **[E72.97](E72_97_FBRT_BORDERED_MINOR.md)** -- rewrites the `D2` Stieltjes defect as a single bordered
  determinant ratio
  `-det[[C_E,c_{x,H}(tau_j)],[a_x(s)^*,0]]/det(C_E)`. The companion script
  **[E72_97_fbrt_bordered_minor_probe.py](E72_97_fbrt_bordered_minor_probe.py)** verifies the formula
  against direct solves to relative error around `1e-15`.

- **[E72.98](E72_98_FINITE_ENDPOINT_THEOREM.md)** -- states the finite endpoint theorem: if the two
  explicit defects `D1` and `D2` vanish in the stated asymptotic regimes, scalar WRL resonance
  annihilation follows, hence the Phase 72 route closes Ω7. This is a finite explicit reduction, not a
  proof of the required asymptotic vanishing.

- **[E72.99](E72_99_WEYL_ROOT_STRUCTURE_AUDIT.md)** -- tests whether the finite-root condition
  `M_xi(tau_j)=0` already makes `Z_x(tau_j)` orthogonal to simple directions such as `xi_x`, `k_x`, or
  `1`. It does not; the root factor is not a pre-shorting vector orthogonality. The companion script
  **[E72_99_weyl_derivative_probe.py](E72_99_weyl_derivative_probe.py)** records the audit.

- **[E72.100](E72_100_DERIVATIVE_NORMALIZATION_AUDIT.md)** -- tests whether `D2` is explained by the
  scalar derivative normalization `M'_xi(tau_j)`. The normalized values are not stable enough to give a
  scalar root-derivative theorem, so `D2` remains a full shorted bordered determinant. The companion
  script **[E72_100_derivative_normalization_probe.py](E72_100_derivative_normalization_probe.py)**
  records the falsifier.

- **[E72.101](E72_101_MODEL_VS_ACTUAL_D2_AUDIT.md)** -- compares `D2` computed with the actual
  complement against `D2` computed with the prolate/model complement. The model defect is the same
  order as the actual defect, so `D2` is not primarily a PNT-small arithmetic perturbation. The
  companion script **[E72_101_model_vs_actual_d2_probe.py](E72_101_model_vs_actual_d2_probe.py)**
  records the model/actual split.

- **[E72.102](E72_102_MATCHED_ROOTS_AUDIT.md)** -- tests whether the model defect disappears when the
  model complement is evaluated at model roots instead of actual roots. It does not; root mismatch is
  not the explanation. The companion script
  **[E72_102_matched_roots_probe.py](E72_102_matched_roots_probe.py)** records the matched-root audit.

- **[E72.103](E72_103_RELATIVE_ROOT_CURRENT_AUDIT.md)** -- tests the next correction: subtract model
  root currents from actual root currents instead of requiring pointwise `D2` vanishing. The unweighted
  relative current shows sporadic cancellation but is not robust. The companion script
  **[E72_103_relative_root_current_probe.py](E72_103_relative_root_current_probe.py)** records the
  relative-current audit.

- **[E72.104](E72_104_DERIVATIVE_WEIGHTED_CURRENT_AUDIT.md)** -- tests the derivative/residue-weighted
  relative current using `1/M'(tau_j)`. This also fails to produce stable cancellation, so the correct
  HPAC background gauge is subtler than local derivative normalization. The companion script
  **[E72_104_weighted_relative_current_probe.py](E72_104_weighted_relative_current_probe.py)** records
  the weighted-current audit.

## Why this is not Phase 65 again

Phase 65 asked for renormalization-stable strong-resolvent convergence of the whole primitive tower.
Phase 72 asks for a one-vector, pole-relative Schur complement estimate. This is strictly weaker and
better targeted:

- global modes not coupled to `k_lambda` are irrelevant;
- diagonal energy renormalization is harmless;
- the prime arithmetic appears only in the reduced leakage vector `C_x^{-1}Q R k_lambda`;
- Davenport-Heilbronn/planted controls should fail by producing non-vanishing leakage.

The open problem is now microscopic:

```text
prove pole-relative reduced arithmetic leakage:
||C_x^{-1}Q_x(H_x-H_x^0)k_lambda|| -> 0.
```

Equivalently:

```text
sup_v |<v,(H_x-H_x^0)k_lambda>| / ||C_x v|| -> 0.
```

Operationally this is now split into:

```text
for every fixed M, low reduced channels vanish;
the high reduced tail is uniformly tight.
```

The next required object is an explicit non-circular coboundary primitive:

```text
Q_x(H_x-H_x^0)k_lambda = C_x u_x + r_x,
u_x -> 0,
C_x^{-1}r_x -> 0,
```

with `u_x` built before solving the Feshbach inverse equation.

The first concrete missing construction is the boundary-corrector triple:

```text
Tr_x, m_x, u_x
```

for the actual compressed complement `C_x`.

The sharpened missing lemma is PSC:

```text
<v,b_x> = <C_x^0 v,w_x> + eps_x(v),
||w_x|| -> 0,
||eps_x||_{(C_x^0)^*} -> 0,
||C_x^{-1}(C_x-C_x^0)w_x|| -> 0.
```

The sharper commutator target is:

```text
Q_xR_xk_x = Q_x[C_x^0,A_x]k_x + e_x,
||Q_xA_xk_x|| -> 0,
||(C_x^0)^{-1}e_x|| -> 0.
```

In Doob variables this becomes:

```text
h_x = D_x^+(F_x/k_x),
||h_x||_{L^2(k_x^2dtheta)} -> 0,
||C_x^{-1}(C_x-C_x^0)(k_xh_x)|| -> 0.
```

The explicit one-dimensional target is:

```text
G_x(theta)=int_a^theta k_x(t)Q_x(H_x-H_x^0)k_x(t)dt,
int |G_x(theta)|^2/(p_x(theta)k_x(theta)^2)dtheta -> 0,
```

plus the one-vector actual/model replacement.

Equivalently, with centered cumulative cell kernels:

```text
G_x(theta)=sum_c omega_c K_x[B_{x,c}](theta),
||G_x||_{rho^{-1}}^2 = omega_x^*M_xomega_x.
```

After Abel summation:

```text
G_x = -E(x)K_x(x) + int_1^x E(u)partial_uK_x(u)du + M_x^{err},
E(u)=Psi(u)-u.
```

The explicit-formula resonance expansion is:

```text
T_x = -sum_rho R_x(rho)/rho + lower-order archimedean/cutoff terms,
R_x(s)=x^sK_x(x)-int_1^x u^s partial_uK_x(u)du.
```

So the remaining proof cannot be a PNT-size estimate. It must prove intrinsic annihilation of the
off-critical resonance vectors `R_x(rho)` for the actual one-vector centered cumulative kernels.

The zero-filter gate says a scalar Mellin proof of that annihilation would have to manufacture an
analytic filter containing the off-critical zeta divisor. The non-circular remaining target is therefore
not scalar decay, but finite-dimensional vector cancellation of the maximal resonance block.

E72.17 shows that ordinary symmetries do not provide that cancellation: the functional-equation partner
has lower real part, and conjugation only creates a real oscillatory pair. The only possible remaining
statement is an intrinsic null-vector identity in the finite CCM/prolate resonance Gram matrix.

E72.18 formulates the new possible mechanism: finite CCM real-zero divisors have zero off-real residue
current. The maximal resonance block is therefore a boundary-loss term in the passage from the finite
relative residue current to the global `Xi` relative current.

E72.19 proves the stronger closure theorem: if the finite real-supported divisor currents converge to
the `Xi` divisor current in the strip, the support of the limit remains real and RH follows.

E72.20 lowers the target from divisor convergence to potential convergence: it is enough to prove
`log|F_x/G_x| -> log|Xi/G|` in local `L^1`.

E72.21 shows why boundary modulus is insufficient: Blaschke factors can carry off-real divisor mass
with unit modulus on the real line. The required convergence must be Schur-free current convergence,
not merely real-axis amplitude convergence.

E72.22 gives the first concrete way to force that: prove log-derivative convergence on two interior
horizontal lines together with local normal bounds in the slab. Hidden off-real divisor mass would
create a pole in the slab, impossible as a compact normal limit of finite real-supported Cauchy
currents with those traces.

E72.23 makes that target computable from finite CCM data without root tracking:
`P_x'/P_x=-S_{2,x}/S_{1,x}+Q_x'/Q_x`.

E72.24 shows how to prove that current convergence from the finite eigenvector equation: compute
`(A_x-eps_x)r_x(s)` and prove a two-jet transport identity.

E72.25 corrects this: the naive full-vector two-jet identity is false. The next object must transport
the log-current itself, or a canonical finite-rank current projection, not the whole resolvent vector.

E72.26 supplies that object: the Weyl numerator is exactly a bordered determinant, so the current is a
finite trace of the inverse bordered pencil.

E72.27 gives the precise Fredholm theorem needed to close the route: prove trace-norm convergence of
the relative bordered pencils and identify the Fredholm determinant with the prolate/CCM `Xi` limit.

E72.28 sharpens the non-circular burden: the model determinant may come from Connes's prolate limit,
but the actual work is the bordered trace estimate
`||(B_x-B_x^0)(B_x^0)^(-1)||_1 -> 0`.

E72.29 shows full trace norm may be too strong. The current-level scalar factor only asks for
`(xi_x-k_x)^T(sI-D_x)^(-1)1_x -> 0` on interior heights, a Weyl-weak ground convergence estimate.

E72.30 translates that into the minimal remaining arithmetic estimate: the Feshbach leakage only has
to vanish after testing against the Weyl Cauchy functional, not in full norm.

E72.31 expands that estimate: it is a scalar Abel-Chebyshev cancellation against a single kernel
`L_x(s;u)`, with the same explicit zero-resonance obstruction but in the smallest possible channel.

E72.32 shows that this scalar annihilation cannot come from generic smoothing or integration by parts.
It must come from an intrinsic finite spectral coborder in the CCM data.

E72.33 sharpens that coborder into Mellin spectral divisibility by the finite CCM Weyl numerator
`P_x(z)`.

E72.34 gives the finite algebraic target behind that divisibility: prove the Mellin scalar current is a
factorized bordered-pencil coboundary carrying an explicit `P_x` factor.

E72.35 sharpens this further: the non-tautological identity must express `M_x` through the finite Weyl
factor `m_x=P_x/Q_x` via an intrinsic bilinear concomitant.

E72.36 shows the raw discrete Mellin version is false numerically. The remaining target is the
renormalized Abel resonance, not the unrenormalized finite-cell sum.

E72.37 gives the first positive numerical signal for that renormalized target: endpoint-normalized
Mellin values are small and decreasing.

E72.38 explains the signal: the Fejer cell kernels vanish linearly at the endpoint, and the normalized
Mellin character weights the endpoint.

E72.39 turns that mechanism into an explicit sufficient bound: endpoint mass after model-main
subtraction times the compressed Cauchy channel must tend to zero.

E72.40 quantifies the arithmetic side: PNT leaves an `o(sqrt(x))` mass, so the remaining operator
estimate is a half-power compressed channel bound.

E72.41 refines that statement: the needed bound is not pointwise in cells but the coherent
endpoint-weighted dual norm actually appearing in scalar WRL.

E72.42 confirms this numerically: endpoint damping is visible, but the operator norm is too strong.
The proof must use scalar orthogonality in the compressed channel.

E72.43 formulates the needed scalar coborder: endpoint-weighted sources must have a Doob primitive that
is small only against Weyl Cauchy tests.

E72.44 converts that Weyl pairing into an exact mixed cumulative-energy identity.

E72.45 isolates the next estimate: centered cumulative endpoint cells should gain a second taper
factor, enough to make the endpoint energy vanish.

E72.46 corrects that expectation: the safe route is continuous endpoint operator smallness plus a
separate endpoint discrepancy estimate.

E72.47 proves the continuous endpoint operator smallness using the overlap/translation structure of the
CCM cells.

E72.48 isolates the last arithmetic estimate in scalar form: endpoint-tapered Chebyshev discrepancy
against the compressed Weyl-Feshbach channel.

E72.49 shows finite bandwidth helps organize the discrepancy but does not by itself beat the
`x^(1/2)` barrier from PNT. The half-power gain remains a compressed-channel estimate.

E72.50 gives numerical evidence that the missing half-power is present in the weighted scalar endpoint
channel itself.

E72.51 identifies the exact finite-dimensional estimate behind that evidence: an `l1` Fourier
coefficient half-power bound for `a_{x,s}(y)=<v_s,Q_x(y)k_x>`.

E72.52 opens that coefficient: it is a Hilbert-transform expression in the compressed Cauchy vector and
the prolate ground vector.

E72.53 corrects the basis: the scalar channel is affine-frequency, so the prime sums include a harmless
endpoint derivative in the exponent.

E72.54 exposes the finite commutator behind those coefficients, giving a concrete algebraic target for
the missing half-power cancellation.

E72.55 confirms numerically that this finite commutator is carrying the scalar smallness.

E72.56 identifies the leading endpoint structure produced by that commutator: a rank-one overlap term.

E72.57 fixes the normalization of the endpoint channel: the true arithmetic operator carries the
von Mangoldt weight.

E72.58 corrects the endpoint rank-one interpretation: the leading rank-one term is model-main, not
self-suppressed.

E72.59 corrects the endpoint main normalization: continuous endpoint smallness was a false
`du/u` artifact; the route must work entirely after model-main subtraction.

E72.60 verifies the corrected post-main object numerically and names the finite target:
Loewner-Feshbach Discrepancy Cancellation.

E72.61 sharpens LFDC into an exact endpoint-reflected identity:
`D_x(s;z)=(2/(L sqrt(x)))int exp(-(z-1/2)r)<v,Lo_rk>dE_x^leftarrow(r)`. The open estimate is now the
Endpoint Reflected Inequality for the derivative of this single Loewner-Feshbach test family.

E72.62 integrates the Loewner commutator and rewrites the reflected discrepancy as the finite
Cauchy-Hilbert coefficient identity `(ECHC)`. This exposes the exact place where the Feshbach equation
must kill the incoherent half-power barrier.

E72.63 splits `(ECHC)` into high oscillatory endpoint sums and low Feshbach current cancellation. The
closure theorem is proved; the two estimates `(HF)` and `(LF)` are now the remaining mathematical
targets.

E72.64 shows that the low part is exactly where off-critical residues would live. Closing it requires a
finite algebraic divisibility identity by the CCM spectral polynomial `P_x`, before evaluating at any
zero.

E72.65 fixes the variable alignment for that divisibility: the determinant ideal lives in the CCM
height variable `tau`, with Mellin exponent `rho=1/2+i tau`.

E72.66 falsifies endpoint-only divisibility. The endpoint reflection is useful for LFDC estimates, but
the algebraic divisor must be constructed for the full Abel-WRL concomitant.

E72.67 falsifies only the unnormalized cell-Abel shortcut. E72.68 corrects the half-power normalization
and identifies the finite concomitant that now carries the divisibility target.

E72.69 makes that target directly finite and verifiable: after clearing mesh denominators, the residual
is `G_x^{(0)}(tau_j)+exp(i tau_jL)G_x^{(1)}(tau_j)` at finite CCM roots `tau_j`.

E72.70 gives the cleanest form of the same target: the residual is the Fourier transform at finite roots
of the single generator `(1/2)Q_x-Q_x'`.

E72.71 collapses that Fourier transform further: the HPAC matrix is exactly two diagonal resolvents plus
two rank-one terms. At finite roots, one rank-one vector is the Weyl null vector `r_-(tau_j)`.

E72.72 splits the finite-root certificate using that Weyl-null relation. The route now separates into a
small actual-divisor core and a reduced displacement term for `k_x-xi_x`.

E72.73 reduces the core further: it only tests the even part of the Cauchy-Feshbach vector after the
ground line has been projected out.

E72.74 gives the smallest current certificate so far: a single even-sector scalar identity `(EV-CERT)`.

E72.75 turns that scalar identity into a vector coborder certificate `(EVC)`, matching the reduced
Feshbach norm philosophy of E72.3--E72.4.

E72.76 splits `(EVC)` into a small actual-divisor core and a rank-one-corrected model/actual
displacement term.

E72.77 names the remaining displacement statement as HPAC-displacement invisibility and blocks the
circular shortcut through full model/actual convergence.

E72.78 proves the exact Cauchy divided-difference identity behind the actual-divisor core. The core
problem is now specifically the shorted version of that identity.

E72.79 identifies the shorted core certificate with an exact bordered minor. This exposes the inverse
inside the Feshbach complement instead of hiding it in an informal divisibility claim.

E72.80 rewrites finite-root vanishing as a root-remainder condition. The target is now a finite
interpolation remainder on the roots of the CCM spectral polynomial.

E72.81 transports the dual cofactor explicitly and reduces the root residual to two model Cauchy
channels plus the exact HPAC boundary factor.

E72.82 audits and rejects the mesh cotangent shortcut. The finite mesh identity is not enough to kill
the residual.

E72.83 records the fixed-index bandlimit signal, then E72.84 corrects it: the stable tightness is in
physical height `|d_n|`, not in the raw index.

E72.85 and E72.86 reject the too-strong full operator-norm Green decay. The only viable estimate is
Cauchy-channel-specific.

E72.87 gives an exact finite quadratic certificate for the Cauchy-channel Green tail, and E72.88 shows
finite physical-band transport tracks the full residual once the Cauchy tail is removed.

E72.89--E72.92 isolate the finite-band obstruction: the transported vector is not norm-small, so the
remaining cancellation must be Stieltjes/Cauchy invisibility, not vector invisibility.

E72.93 formulates the finite-band moment criterion. E72.94 and E72.95 reject the low-moment and
low-rank shortcuts.

E72.96 unifies the finite certificate, and E72.97 rewrites the finite-band root transport defect as a
bordered determinant.

E72.98 states the finite endpoint theorem: Cauchy-channel tail `D1 -> 0` plus finite-band root
transport `D2 -> 0` implies scalar WRL resonance annihilation. It is a valid sufficient theorem, not a
proof of the asymptotic estimates.

E72.99 and E72.100 audit two local root-normalization hopes and reject them: neither Weyl-root
pre-orthogonality nor derivative normalization removes the finite-band defect.

E72.101 and E72.102 compare actual and prolate/model complements. The key discovery is that the
finite-band defect is already present in the model background and persists even when model roots are
used.

E72.103 and E72.104 test natural relative-current gauges, unweighted and derivative-weighted. Both
fail to reveal stable cancellation, showing that subtracting the model after root evaluation is too
late.

E72.105 corrects the endpoint target. Absolute `D2` remains a sufficient but over-strong condition;
the scalar WRL route needs a post-main HPAC gauge built from
`dE_x^leftarrow=dPsi_x^leftarrow-xe^(-r)dr` before shorting and before root evaluation. The remaining
identity is post-main finite-band root transport, equivalently integrated Loewner-Feshbach discrepancy
cancellation.

E72.106 constructs that post-main source explicitly:
`Z_x^{pm}(tau)=(2/(L sqrt(x)))K_x^E(tau)k_x`, where
`K_x^E(tau)=int exp(-i tau r)Lo_r dE_x^leftarrow(r)`. It proves the closed divided-difference entry
formula, the integrated commutator `[D,K_x^E]=[Sigma_x^E,11^T]`, and the exact bordered determinant
for `D2_x^{pm}`. The numerical identity check agrees to roundoff.

E72.107 proves a spectral divergence gate: if the post-main finite-band cofactor is a discrete
spectral divergence with `h||Psi||_1=o(1)`, then its Cauchy pairing vanishes by summation by parts.
The first probe shows decreasing `D2pm`, mass, and flux, but also shows exact zero mass is too strict.

E72.108 corrects this by splitting every cofactor exactly into a mass channel plus a centered spectral
divergence. The current minimal finite theorem is now: prove `MASS -> 0` and
`h||centered flux||_1 -> 0` for the post-main cofactor at finite CCM roots.

E72.109 converts that target into a positive quadratic certificate. Since a fixed physical band has
`M_H~HL/(2*pi)` points, `h||Psi||_1 <= O(L^(-1/2))||Psi||_2`. Thus it is enough to prove
`Mass_x(H,tau_j)->0` and a uniform bound on the centered cumulative flux energy. The first diagnostic
shows bounded/decreasing quadratic flux in the tested windows.

E72.110 opens the quadratic certificate as exact arithmetic integrals. The mass is a single integral
against `dE_x^leftarrow`; the flux is a positive double discrepancy energy with kernel
`G_{x,H}(r,r')=<Lo_rk_x,A_{x,H}Lo_{r'}k_x>`. The remaining theorem is now the structured
Loewner-Feshbach discrepancy energy bound `(MASS-INT)+(ENERGY-INT)`.

E72.111 rewrites the post-main source as a finite pushforward of the Chebyshev Fourier packet
`Y_x(tau)=(Ehat_x(tau±d_n),Ehat'_x(tau±d_n))`. The gain diagnostic shows that the raw source is not
small, but physical projection, Feshbach shorting, and endpoint centering produce a small cofactor.

E72.112 isolates the shorted pushforward operator `R_{x,H,tau}`. The operator split
`||R_{x,H,tau_j}||||Y_x(tau_j)||=O(1)` is a sufficient finite criterion for the quadratic energy bound,
and the probe verifies the factorization to roundoff.

E72.113 packages the current endpoint: `CCGD + MOP + ROP` implies scalar WRL resonance annihilation.
The remaining open content is now exactly the finite estimates `MOP` and `ROP/DQF`, plus the physical
Cauchy-tail tightness.

E72.114 sharpens `ROP/DQF` using the SVD of the shorted pushforward. The direct energy is exactly
`sum sigma_l^2 |<Y,v_l>|^2`; hence it suffices to control finitely many bad singular projections and
the singular tail. Numerically the pushforward is almost low-rank and the first three modes carry
more than `99%` of the tested energy.

E72.115 isolates the mass channel as a single projection condition
`Mass=||m||<Y,e_m>`. The product `||m||||Y||` is bounded in the tested windows, while the actual mass
is smaller by an alignment factor; so `MOP` should be proved as mass-projection orthogonality rather
than by a raw norm bound.

E72.116 combines the mass direction and the first `q` right singular directions into one bad subspace
`B_{x,H,q}`. The final finite gate becomes `CCGD + BNORM + BORTH`, where `BORTH` is a finite family of
explicit endpoint discrepancy tests against `dE_x^leftarrow`. For `q=3`, the measured projection of
`Y_x(tau_j)` onto the bad subspace decreases across the tested windows.

E72.117 converts `BORTH` into a Gram determinant saturation:
`det(G_x[Y_j])/(det(G_x)||Y_j||^2)->1`. This is a finite determinant identity in the endpoint
discrepancy transforms. The QR, Gram-inverse, and determinant computations agree numerically, and the
measured determinant saturation improves toward `1`.

E72.118 isolates `BNORM` as three scalar finite bounds:
`||m||||Y||`, `sigma_1(R)||Y||`, and `sigma_{q+1}(R)||Y||`. For `q=3`, all three are bounded in the
tested windows. The final non-tail package is now `BNORM + GBORTH`.

E72.119 packages the current endpoint as one finite checklist:
`C-FIN + N-FIN + S-FIN`, namely one Cauchy-tail quadratic ratio, three scalar norm bounds, and one Gram
determinant saturation. This single certificate implies scalar WRL resonance annihilation through the
Phase 72 chain.

E72.120 reduces `C-FIN` to a graph-energy bound:
`Graph_x(s)=||Dg_{x,s}||^2/||g_{x,s}||^2=O_K(1)`, since
`CCGD_x(H,s)<=H^{-2}Graph_x(s)`. This replaces the physical-tail piece by a finite quadratic rational
inequality.

E72.121 audits the natural height normalization `Graph/(1+|s|^2)`. It works sharply at higher physical
heights, while low-height windows require the compact-window constant `C_K`; this calibrates `CGE`
without overstating a universal height law.

E72.122 splits `N-FIN` into arithmetic packet size and shorted geometric decay. The diagnostic suggests
`||Y||=O(sqrt(x)L)` and the mass/singular maps decay like `O(1/(sqrt(x)L))`, leaving the three N-FIN
products bounded.

E72.123 splits `S-FIN` into a lower bound and an upper bound:
`||Y||>=c sqrt(x)L` and `||P_BY||=O(sqrt(x))`. This gives
`||P_BY||/||Y||=O(1/L)` and hence Gram determinant saturation.

E72.124 identifies the lower bound as a finite packet frame bound `PFLB`: the sine packet and its
logarithmic derivative carry energy `>= c^2 xL^2` against the endpoint discrepancy. Numerically both
packet components are active, and the discrepancy/continuous ratio is comparable rather than a
background artefact. Thus `S-FIN` is now reduced to `PFLB + BUP`, with `BUP` the remaining bad-subspace
upper bound `||P_BY||=O(sqrt(x))`.

E72.125 turns `BUP` into the invariant finite square bound `BTB`:
`sum_a |int exp(-i tau_j r)T_{a,x}(r)dE_x^leftarrow(r)|^2 <= Cx`, where the scalar tests `T_{a,x}`
come from an orthonormal basis of the shorted bad subspace. The diagnostic shows `BTB/x` bounded and
decreasing in the tested windows, so the remaining proof target is a shorted-root orthogonality
identity for these finitely many tests, not a general explicit-formula discrepancy bound.

E72.126 identifies the missing logarithm in that proof target. Bounded shorted flux alone gives only
`|<Y,v_l>|=O(sqrt(x)L)`. The needed statement is the top-mode flux gain
`||Sigma_{<=q}V_{<=q}^*Y||=O(1/L)`, plus the analogous mass gain. Numerically `L` times the retained
flux is stable and small, isolating the exact finite root/shorting identity still to be proved.

E72.127 compresses the endpoint using the centered spectral-divergence theorem: top-mode annihilation
is not needed for scalar WRL. Bounded flux `ROP` already vanishes after the mesh summation-by-parts
gain `h||Psi||_1<=C_HL^{-1/2}||RY||_2`. The minimal route is now
`CGE-K + ROP + MG`, where `MG` is the single scalar mass estimate `m_xY_x(tau_j)->0`.

E72.128 isolates `MG` as the mass of the shorted post-main cofactor
`1_H^TW_HB_xC_E^(-1)B_x^*P_HZ_x^{pm}(tau_j)`. The scale probe shows `L*mass` decreasing and
`L^2*mass` roughly bounded in the tested windows, so the likely theorem is a logarithmic mass gain
coming from the finite CCM root/Feshbach equation.

E72.129 rejects a purely scalar root-factor explanation for `MG`: ratios involving `M_k`, `M'_k`, and
`M'_xi` are not uniformly stable. E72.130 then locates the gain: raw and complement-projected masses
are O(1), while the shorted mass is smaller by a decreasing factor. Thus `MG` is now a shorting
damping theorem for the mass functional of `C_E^(-1)`.

E72.131 measures that damping directly. The mass vector satisfies
`||C_E^(-1)b_H||/||b_H||=O(1/L)`, and in the tested windows the whole shorted complement has
`minEig(C_E)>=cL`. This moves the final scalar mass estimate to a complement-coercivity theorem for
`C_E`, plus a bounded post-main source size.

E72.132 proves the mass channel from those two finite estimates:
`COER: C_E>=c_HLI` and `MSB: ||b_H||||c_H^{pm}(tau_j)||=O(1)` imply
`|b_H^*C_E^{-1}c_H^{pm}(tau_j)|=O(1/L)`. The source-bound probe supports `MSB`, leaving complement
coercivity as the main structural estimate.

E72.133 shows crude operator-norm perturbation is too strong: the arithmetic perturbation is large in
norm even though the actual complement is coercive. E72.134 replaces it with the correct relative form
bound `C_actual>=theta_H C_model`; generalized eigenvalues stay above `0.42` in the tested windows.
Thus `COER` reduces to model coercivity `C_model>=a_HLI` plus relative coercivity.

E72.135 packages the sharp finite route:
`CGE-K + ROP + MCOER + RCOER + MSB => scalar WRL annihilation`. This is now the minimal post-Phase-72
proof obligation: Cauchy tail, bounded shorted flux, model complement coercivity, relative
actual/model coercivity, and bounded post-main source product.

E72.136 audits `MCOER` by Gershgorin and finds a positive entrywise lower bound in every tested
window. E72.137 proves the corresponding theorem: `GCOER` implies `MCOER`, hence
`CGE-K + ROP + GCOER + RCOER + MSB => scalar WRL`. Model coercivity is now an explicit row-wise
inequality for `C_model`.

E72.138 rewrites `RCOER` as the relative arithmetic form bound `RFBD`:
`(-<v,Delta_arith v>)_+ <= eta <v,C_model v>` with `eta<1`. This avoids the failed operator-norm
Weyl bound and targets only the negative arithmetic part. The current sharp route is
`CGE-K + ROP + GCOER + RFBD + MSB => scalar WRL`.

E72.139 opens the relative negative spectrum of the arithmetic perturbation. The negative rank grows,
so the obstruction is not a few-mode correction, but the negative Frobenius norm stays below `1`.
E72.140 turns this into the scalar certificate `NHS: ||K_rel^-||_HS<1`, which implies `RFBD`. The
sharpest current route is now `CGE-K + ROP + GCOER + NHS + MSB => scalar WRL`.

E72.141 tests the stronger unsigned shortcut `Tr(K_rel^2)<1` and rejects it: total Hilbert-Schmidt
norm is above `1` because positive directions contribute. This validates why the signed/negative
certificate `NHS` is the right finite target.

E72.142 removes the spectral-projection language from `NHS`: `||K_rel^-||_HS` is exactly the Frobenius
distance from `K_rel` to the PSD cone. Thus `NHS` is equivalent to the finite SDP certificate
`exists P>=0 with Tr((K_rel-P)^2)<1`. The route can be stated as
`CGE-K + ROP + GCOER + PSD-DIST + MSB => scalar WRL`.

E72.143 tests the tempting diagonal PSD certificate and rejects it: the diagonal distance remains
above `1`. Therefore `PSD-DIST` genuinely uses off-diagonal structure; the next useful target is an
explicit structured PSD approximant, not a purely entrywise diagonal bound.

E72.144 tests low-rank PSD approximants. Two or three positive relative modes already make the
distance to `K_rel` less than `1`, so `PSD-DIST` can be sharpened to a low-rank positive certificate
plus a Frobenius tail estimate. The diagonal route is dead, but the rank-3 route is alive.

E72.145 tests whether those positive modes are simple mass/moment/edge directions and rejects that
shortcut: correlations are low. The rank-3 PSD certificate, if made explicit, must be built from the
arithmetic kernel rather than from elementary physical moments.

E72.146 packages the current endpoint as one finite semialgebraic certificate:
`GCOER + PSD-DIST + MSB + ROP + CGE-K => scalar WRL`. This is the sharpest finite reduction so far:
Gershgorin rows for the model complement, one PSD-distance inequality for the relative arithmetic
perturbation, one mass-source product, one flux bound, and one graph-energy tail.

E72.147 evaluates all five certificate quantities in one table. In the tested windows, `GCOER/L` and
`PSDmargin` are positive, `MSB` and `ROP` remain bounded, and `GraphN` stays close to `1`. This is the
current executable certificate dashboard for the Phase 72 route.

E72.148 stress-tests the relative arithmetic gap behind `RFBD`. Through `lambda=30`, the generalized
coercivity floor `theta_H` stays in `[0.4218,0.6633]`; it does not show visible decay toward zero. The
absolute perturbation norm remains too large, so this supports the signed relative/PSD route rather
than the rejected Weyl-norm route.

E72.149 splits `MSB` into two scale estimates:
`||b_H||=O(sqrt(L))` and `sup||c_H^{pm}(tau_j)||=O(1/sqrt(L))`. The probe supports both, with the
source factor apparently smaller than the required scale. Thus `MSB` is no longer a black-box product;
it is two explicit norm-growth estimates.

E72.150 tests whether the source estimate follows from the operator norm of `B^*P_HLK`; it does not.
The operator norm is O(1), so `CPM-scale` is another alignment/cancellation estimate for the finite
root packet `Y_x(tau_j)`, not a crude norm estimate.

E72.151 measures that alignment directly:
`||M_xY||/(||M_x||||Y||)=O(1/L)` for `M_x=B^*P_HLK`. This reduces `CPM-scale` to a finite singular
orthogonality statement `CPM-ORTH`, while `B-scale` supplies `||b_H||=O(sqrt(L))`.

E72.152 refines the final certificate by replacing `MSB` with structural estimates:
`B-scale + Y-scale + OPM + CPM-ORTH => MSB`. The two genuinely signed/cancellation gates left are now
`PSD-DIST` and `CPM-ORTH`; the rest are size or coercivity bounds.

E72.153 rewrites `CPM-ORTH` as the positive quadratic Rayleigh certificate `CPM-Q`:
`Y^*M^*MY/(||M||^2||Y||^2)=O(L^{-2})`. The probe gives `L^2Q_CPM<0.12` in tested windows, so the
source cancellation is now a single finite quadratic inequality.

E72.154 shows the geometric reason for `CPM-Q`: finite root packets lie within `O(1/L)` of
`ker(M_x)` for `M_x=B^*P_HLK`. Thus `CPM-Q` is reduced to the kernel-saturation statement
`KERN-ORTH`, another finite subspace orthogonality gate.

E72.155 tests whether `KERN-ORTH` is specific to actual roots and finds it is not: model roots and
generic grid heights have comparable `L*dist` values. This suggests `KERN-ORTH` may be upgraded to a
uniform tau-window geometric packet estimate, not a delicate actual-root cancellation.

E72.156 confirms that upgrade numerically: on a dense tau grid in `[0.25,6]`,
`sup_tau ||P_Row(M)Y(tau)||/||Y(tau)||=O(1/L)`. The maximum occurs at the window edge in the tested
runs. Thus `CPM-Q` no longer needs a root-specific argument; it reduces to the uniform geometric packet
estimate `UKERN`.

E72.157 updates the route: `UKERN => CPM-ORTH => CPM-Q => CPM-scale`, so the CPM side of `MSB` is now
a uniform geometric kernel estimate. The remaining signed arithmetic gate is `PSD-DIST`; the other
pieces are size, coercivity, graph-tail, or geometric packet bounds.

E72.158 tests whether the low-rank PSD certificate for `PSD-DIST` comes from the largest individual
prime-power cells. It does not: the distance remains above `1`. The PSD approximant is global over the
arithmetic perturbation, not local over a few dominant prime cells.

E72.159 tests coherent prime-position blocks. Two coarse blocks nearly certify `PSD-DIST` and succeed
for the larger small windows, while finer blocks get worse. This suggests the positive approximant is
coherent over broad endpoint regions.

E72.160 adds two scalar weights to the two-block PSD approximant and succeeds in every tested window:
`||K_rel-aP_0-bP_1||_HS<1`. E72.161 packages this as `2B-PSD`, a constructive replacement for the
abstract `PSD-DIST`. The signed arithmetic gate is now a two-block weighted distance inequality.

E72.162 tests universal weights and finds that fixed `(a,b)=(0.70,0.60)` certify all tested windows.
E72.163 packages this as `F2B-PSD`, removing window-dependent optimization from the arithmetic PSD
gate.

E72.164 optimizes the block cut for those fixed weights. Moving the cut from `0.50L` to `0.60L`
improves the worst distance from `0.996` to `0.967`, giving margin `0.065`. The current fixed
arithmetic certificate is therefore `cut=0.60`, `a=0.70`, `b=0.60`.

E72.165 stress-tests that fixed certificate through `lambda=20` without refitting any parameter. The
worst case remains `lambda=8` with distance `0.967`; the new larger windows stay lower
(`0.863,0.833,0.843`). Thus the current arithmetic gate is the explicit fixed statement
`F2B-PSD(0.60;0.70,0.60)`, not a window-by-window optimization.

E72.166 decomposes the fixed residual into four signed spectral pieces:
`(1-a)K_0^+ + K_0^- + (1-b)K_1^+ + K_1^-`. From `lambda=10` onward the diagonal sign energy is already
below `1`, so the asymptotic proof of `F2B-PSD` can be attacked as a one-sided Hilbert-Schmidt norm
bound plus a finite small-window check, rather than as a delicate cancellation theorem.

E72.167 names that one-sided estimate `BSE` (block sign energy). The tested rows give
`BSE<=0.898` from `lambda=12` onward, with a stable descent toward `0.74`. The exact remaining
asymptotic target is `BSE + cross_+ <= 1-epsilon`; the cross term is now a small correction, not the
main cancellation mechanism.

E72.168 rewrites `BSE` as a trace asymmetry functional:
`E_a(K)=c_a||K||_HS^2-d_a Tr(K|K|)`. The block roles separate: `K0` is larger but
positive-asymmetric, while `K1` is more negative but smaller. The sharp proof target is now two direct
trace-functional bounds for `K0,K1` plus a small `cross_+` bound.

E72.169 tests the naive PNT-continuum replacement
`K_I^cont=-int_I exp(y/2)Q(y)dy` after the same whitening. It is qualitatively related but too far
from the exact prime block to close `BSE`; the discrepancy remains large. Thus the exact discrete
von Mangoldt measure must stay inside the main trace-functional estimate.

E72.170 tests the first trace-polynomial idea, a cubic majorant for the split quadratic. It is valid
but too loose: the cubic sums stay above `1`, so it cannot close `F2B-PSD`.

E72.171 replaces the cubic by fixed degree-10 polynomial majorants on the intervals
`K0 in [-0.9,0.9]`, `K1 in [-0.6,0.6]`. The resulting trace bound is below `0.92` throughout the
stable tested range. E72.172 certifies the polynomial majorants by checking critical points, not just
the LP grid. This produces the current sharp arithmetic gate `PTC`: norm bounds, one trace-polynomial
bound, and a small `cross_+` bound imply `F2B-PSD`.

E72.173 combines `PTC` into one executable verifier. It shows the correct regime split:
`lambda=6,8,10` are handled by direct `F2B-PSD`, while `lambda>=12` is handled by `PTC`. In the stable
range, `PTCsum` stays below `0.917`, hence below the `1` threshold with room.

E72.174 expands the trace polynomial gate as a finite prime-power cycle identity:
`Tr(K_j^r)=sum Tr(A_{n1}...A_{nr})`. Thus `PTC-trace` is now a finite explicit sum over exact
von Mangoldt cells up to degree 10. The only remaining non-cycle correction in stable `PTC` is the
small `cross_+` term.

E72.175 removes that `cross_+` correction by approximating the signed residual function
`f_a(t)=t` for `t<0`, `(1-a)t` for `t>=0` with degree-28 polynomials. E72.176 certifies the uniform
errors by critical-point checks. The resulting `SRP` gate proves the full residual bound directly:
`||g0(K0)+g1(K1)||_HS + sqrt(d)(eps0+eps1) < 1`, passing all tested stable windows with worst
certified bound `0.984`.

E72.177 expands `SRP` as a mixed cycle identity. Since
`||g0(K0)+g1(K1)||_HS^2` is a finite sum of traces `Tr(K0^rK1^s)`, and each mixed trace expands into
prime-power cell cycles, the stable gate is now a finite explicit inequality over von Mangoldt cycles
of length at most `56`, plus certified uniform polynomial errors.

E72.178 packages the endpoint as a reduction theorem, now corrected by E72.179:
`Finite-F2B + Adaptive-Stable-SRP => uniform F2B-PSD => PSD-DIST => scalar WRL`, assuming the already
isolated non-arithmetic gates. The exact remaining arithmetic theorem is `Adaptive-Stable-SRP`: two
operator-norm intervals and one mixed cycle inequality for `Tr(G_{x,D_x}^2)`.

E72.179 audits a subtle uniformity issue: fixed degree `28` gives fixed polynomial error, so the
term `sqrt(d_x)(eps0+eps1)` cannot be uniform if `d_x` grows. The corrected gate is
`Adaptive-Stable-SRP`, with degree schedule `D_x` chosen so
`sqrt(d_x)(eps0(D_x)+eps1(D_x))` stays below a margin. The finite identity remains explicit, but cycle
length grows to `2D_x`.

E72.180 gives a concrete approximation schedule by writing
`f_a(t)=(1-a/2)t-(a/2)|t|`. Any constructive polynomial approximant to `|t|` with
`delta_D<=C_abs D^{-1/2}` yields a valid schedule `D_x=O(d_x)`. The final open arithmetic target is
therefore the adaptive mixed cycle inequality for `Tr(G_{x,D_x}^2)`, with cycle length `O(d_x)`.

E72.181 improves the schedule using the exact Chebyshev expansion of `|u|`. The tail bound
`2/(pi(2N+1))` gives `D_x=O(sqrt(d_x))` and cycle length `O(sqrt(d_x))`. The explicit Chebyshev
certificate passes the tested stable windows through `lambda=28`; the worst bound is still at
`lambda=12` and decreases from `0.985` at degree `28` to `0.931` at degree `160`.

E72.182 instantiates the adaptive schedule with concrete margin `m_*=0.05`. The automatic degree
condition is `D_x+1 >= 0.99 sqrt(d_x)/(0.05 pi)`, and the remaining cycle inequality is
`Tr(G_{x,D_x}^2)<0.9025`. In tested windows through `lambda=28`, the approximation error is below
`0.05`, the cycle norm is below `0.95`, and the worst total bound is `0.970`.

E72.183 removes the remaining operator-norm language from Adaptive-SRP: `||K0||<0.90` and
`||K1||<0.60` follow from the trace-power certificates
`Tr((K0/0.90)^16)<1` and `Tr((K1/0.60)^16)<1`. These are fixed cycle inequalities of length `16` and
pass all tested stable windows with large margin.

E72.184 consolidates the arithmetic gate into one executable certificate:
pre-stable windows use direct `F2B`, while stable windows use `NTC-8 + ASRP-0.05`. The unified stress
passes through `lambda=32`; the worst value is still `lambda=12` with final bound `0.970`. The exact
open theorem is now the three stable cycle inequalities listed in E72.184.

E72.185 extends the ASRP stress through `lambda=36`. The certificate still passes, with worst stable
value at `lambda=12`. The norm-trace certificate is not the bottleneck; the hard term is
`Tr(G_{x,D_x}^2)`.

E72.186 decomposes `Tr(G^2)` into `Tr(G0^2)+Tr(G1^2)+2Tr(G0G1)`. The mixed term is consistently small
and negative in the tested stable windows; the pure diagonal sum is already below `0.9025`. This
suggests the sharper target `D-ASRP + XNEG`, separating one-block energy estimates from a mixed sign
lemma.

E72.187 tests `XNEG` under cut perturbations `0.55,0.60,0.65`. The mixed term remains negative for all
tested cuts and stable windows through `lambda=32`, suggesting it is not a one-cut tuning artifact.

E72.188 audits the ASRP margin. Reducing the approximation margin from `0.05` to `0.03` raises the
degree schedule but relaxes the cycle target from `0.9025` to `0.9409`. The recommended proof target
is now `m_*=0.03`, with `D_x+1 >= 0.99 sqrt(d_x)/(0.03 pi)`, because it gives much better inequality
margin while keeping cycle length `O(sqrt(d_x))`.

E72.189 studies the pure D-ASRP energy for `m_*=0.03`. The worst tested value is
`Tr(G0^2)+Tr(G1^2)=0.898` at `lambda=12`, below the target `0.9409`. The block roles remain stable:
`K0` is larger and positive-asymmetric, while `K1` is smaller and negative-asymmetric.

E72.190 identifies `D-ASRP` with the earlier `BSE` up to tiny polynomial approximation error. The gain
of the adaptive SRP construction is not a new energy, but a sign-projection-free cycle realization of
the same block sign energy.

E72.191 searches for low-moment envelopes for `BSE`. Degree `8` succeeds where degrees `4` and `6`
fail. E72.192 certifies the degree-8 envelopes on the full interval by critical-point checks.
E72.193 packages this as `LM8-ASRP`: a fixed degree-8 trace/cycle inequality implying
`D-ASRP-0.03`. This is a strong diagnostic envelope, but E72.247 later shows that its constant term
cannot be the final uniform proof target.

E72.194 tests the degree needed for `XNEG`. Degrees `2,4,8,16` are insufficient in the tested stable
range, but fixed degree `32` makes the mixed term negative through `lambda=36`. The current target can
therefore be stated entirely with fixed finite cycle degrees: `NTC-8`, `LM8-ASRP`, and `XNEG-32`.

E72.195 combines the three gates into one fixed-degree stable certificate and stress-tests it through
`lambda=36`. Every tested stable window passes:
`Tr((K0/0.90)^16)<1`, `Tr((K1/0.60)^16)<1`, the degree-8 low-moment envelope stays below `0.9409`,
and the degree-32 mixed term is non-positive. The worst values are `LM8=0.937` at `lambda=12` and
`XNEG32=-0.003` at `lambda=32`. After E72.247--E72.250 this should be read as a stress diagnostic, not
as the final uniform theorem: the LM8 majorant has dimensional constant drift, and fixed
signed-polynomial errors still carry the `sqrt(dim)` issue unless replaced by a homogeneous or
adaptive/exact mechanism.

E72.196 rewrites those fixed inequalities in the exact Green-cycle form. The correct cycles are not
bare products of the translation overlaps `Q_y`; the exact whitening inserts the model Green operator
`C_model^{-1}` between every prime-power cell. The final arithmetic theorem is therefore the uniform
proof of `GC-NTC`, `GC-LM8`, and `GC-XNEG32` for these Green-cycles. The next possible simplification
is to expand `Q_y=U_y+U_y^*` inside the Green-cycles, producing signed one-sided translation words
with Green insertions.

E72.197 performs exactly that expansion. Each relative cell splits as `A_n=A_n^+ + A_n^-`, where the
two pieces use `U_y` and `U_y^*` after the exact Green whitening. The probe verifies the signed-word
identity for sample Green-cycles to roundoff. The remaining inequalities are now finite signed
Green-word inequalities; proving them by absolute values would lose the phase cancellation and return
to the incoherent ceiling.

E72.198 measures that loss directly. In low moments, absolute summation over signed Green-words is
already worse by factors from about `1.2` to `20`, with the high block showing the largest cancellation.
The next proof invariant should group words by signed displacement
`Delta=sum eps_i log n_i`, separating multiplicative resonances from oscillatory non-resonant words.

E72.199 performs that grouping by the exact rational product `prod n_i^eps_i`. Even moments have a
large resonant component, but the high-block odd moment has zero resonant contribution and still has a
stable negative sign. Therefore the proof cannot keep only multiplicative resonances and bound all
non-resonances absolutely. The next target is a coherent estimate for signed non-resonant Green-word
class sums.

E72.200 inspects the dominant non-resonant classes in the high-block cubic moment. They occur in
reciprocal pairs `R,1/R` with matching signs, and many dominant classes are single-displacement classes
`R=p` or `R=1/p`. This points to an even displacement kernel in `log R` multiplied by a finite
multiplicative von Mangoldt correlation. The next theorem should be a displacement-kernel inequality,
not an individual-word estimate.

E72.201 tests the stronger scalar factorization suggested by E72.200. It fails: after stripping the
positive von Mangoldt weights, words with the same displacement `R` still have large internal Green
kernel spread. Therefore the proof cannot collapse to a scalar function `W(log R)`. The surviving exact
object is the full weighted signed Green-word class sum.

E72.202 formulates that object as an operator-valued finite group-algebra certificate. For each block,
`mathcal A_j=sum(A_n^+ delta_n + A_n^- delta_{n^{-1}})`, and `epsilon(mathcal A_j)=K_j`. The fixed
certificate `NTC-8 + LM8-ASRP + XNEG-32` becomes a finite set of trace inequalities for augmented
powers and mixed polynomial coefficients of `mathcal A_0,mathcal A_1`. This keeps multiplicativity,
translation phases, and exact Feshbach Green whitening simultaneously.
The companion probe verifies the coefficient identity
`Tr(epsilon(mathcal A_j)^r)=sum_R Tr coeff_R(mathcal A_j^r)` to roundoff for `r=2,3`.

E72.203 audits a possible C*-style proof by taking the supremum over unitary characters
`chi_t(n)=exp(it log n)`. It fails with the fixed constants: for `lambda=12`, block `K1`,
`sup_t ||A_1(t)|| ~= 0.620 > 0.60`, while the augmentation norm is only `0.445`. Therefore the proof
must be augmentation-sensitive; the fixed certificate is not a consequence of a uniform torus norm
bound with the same margins.

E72.204 audits the underlying path geometry of one-sided translation words. The simple path-range
formula `Tr prod U_a ~= ell(a)D_N(sum a)/L` is asymptotically informative but not an exact finite
identity; finite Fourier projections create diffraction corrections. Thus the exact proof target is
path-sensitive: multiplicative displacement, partial-sum range, finite-section diffraction, and model
Green insertions all have to remain visible.

E72.205 studies the local character jet at the augmentation. For
`A(t)=sum exp(it log n)A_n^+ + exp(-it log n)A_n^-`, the extreme eigenvalue derivatives satisfy
`lambda'_extreme(0)=0`, while `lambda_min''(0)>0` and `lambda_max''(0)<0` in the tested stable windows.
So `chi=1` is locally favorable even though the global torus norm route fails. The proof should exploit
augmentation-local adjoint-pair evenness rather than uniform control over all characters.

E72.206 computes the trace character jets `F_{j,r}(t)=Tr(A_j(t)^r)`. The trace moments are locally even:
odd derivatives vanish at the augmentation. Even trace energies have negative second derivative, and
the high-block cubic negative moment has positive second derivative. This identifies the next exact
finite identities: displacement-square weighted Green-word sums such as
`F''_{j,r}(0)=-sum (sum eps_i log n_i)^2 Tr(word)`.

E72.207 verifies and records that identity. The second character derivative is exactly the negative of
the displacement-square weighted signed Green-word sum. This turns augmentation-local rigidity into a
finite displacement-moment problem: prove sign and size relations between the `q=0` certificate moments
and the `q=1` displacement-square moments.

E72.208 tests a Poincare-type bridge from displacement-square moments back to augmentation moments. It
works conceptually for the high-block cubic channel, where the resonant part is zero and the effective
gap is large. It is not a universal proof for even moments, because resonant even energy is large and
the smallest nonzero displacement can be tiny. The proof target splits into resonant even energy,
non-resonant displacement Poincare, and high-block odd sign.

E72.209 isolates the base resonant even identity at degree `2`:
`Res_2=2 sum_n ||A_n^+||_HS^2`. This positive local cell energy accounts for about `55%--80%` of the
quadratic block moment in the tested stable windows. Thus even energy should be bounded by local
cell-energy estimates, while the high-block odd sign remains the genuinely non-resonant cancellation
problem.

E72.210 factors that local cell energy exactly:
`2||A_n^+||_HS^2 = 2(Lambda(n)^2/n) Geom_x(log n)`, where
`Geom_x(y)=||C_x^{-1/2}B_x^*U_yB_xC_x^{-1/2}||_HS^2`. The resonant pair energy becomes a weighted
prime-square sum against a purely Feshbach-geometric envelope. Numerically the top cell fraction drops
with `lambda`, and the average geometric factor decreases enough to balance the growth of
`sum Lambda(n)^2/n`.

E72.211 probes the continuous geometric factor. On prime-power support `y>=log 2`, the data are
consistent with `Geom_x(y)=O(L^{-2})` with a decreasing profile in `y/L`; the integral in `u=y/L` also
scales like `L^{-2}`. Thus the resonant-pair sublemma reduces to proving a model-complement geometric
envelope and summing `Lambda(n)^2/n` against a monotone weight.

E72.212 checks the elementary coercive bound
`Geom_x(y)<=||B_x^*U_yB_x||_HS^2/lambda_min(C_x)^2`. It loses only a factor about `1.4--1.8` in tested
windows, so the resonant geometric envelope plausibly reduces to two model estimates:
`lambda_min(C_x)>=cL^2` and `||B_x^*U_yB_x||_HS^2<=CL^2 Phi(y/L)`.

E72.213 audits the first of those model estimates. The data show
`lambda_min(C_model)/L^2 >= 0.20` from `lambda=6` onward, improving with window size, while the
condition number stays around `2--3`. Thus `MCOER2`, the quadratic model coercivity lemma, is a
plausible archimedean/model lemma rather than an arithmetic obstruction.

E72.214 audits the second model estimate, the raw truncated-translation HS bound. The scale is stable:
`||B_x^*U_yB_x||_HS^2/L^2` stays below about `0.72` on the tested grid and has a decreasing profile in
`y/L`. Combined with quadratic model coercivity, this gives the correct `Geom_x(y)=O(L^{-2})` scale;
sharp constants require using the stable-window coercivity, not only the weakest pre-stable bound.

E72.215 measures the resonant-pair budget. The profiled coercive bound is close, losing only
`1.36--1.71` against the actual resonant energy. A flat envelope `K/L^2` is too coarse for the high
block because it ignores that `Geom_x(y)` is much smaller for `y/L>0.60`. The resonant proof must keep
a decreasing profile `Phi(y/L)`.

E72.216 tests explicit profiles for the raw HS envelope. The simple bound
`||B_x^*U_{uL}B_x||_HS^2 <= 0.75 L^2 sqrt(1-u)` has no violations on the tested grid. Combined with
quadratic model coercivity, this yields the explicit resonant bound
`Res_2 <= (1.5/c_C^2)L^{-2} sum (Lambda(n)^2/n)sqrt(1-log n/L)`.

E72.217 evaluates the remaining profiled prime-square sum. For both blocks,
`Sphi/L^2` is stable around `0.12--0.127` through `lambda=96`, so the arithmetic coefficient
`1.5*Sphi/L^2` is about `0.18--0.19`. The limiting issue is not the prime-square sum but the strength
of the model coercivity constant and the sharpness of the raw HS profile.

E72.218 audits whether the convenient `0.75 sqrt(1-u)` profile is sharp enough when combined with the
observed coercivity constant. It is not: the resulting bound loses factors about `1.9--2.6` in the low
block and `3.2--4.9` in the high block. The resonant proof must use a near-sharp profiled coercive sum,
not the soft square-root envelope alone.

E72.219 measures that near-sharp sum:
`Rraw_j=sum_{n in S_j}(Lambda(n)^2/n)||B_x^*U_{log n}B_x||_HS^2`. The scales are stable:
`Rraw_0/L^4 ~= 0.056--0.067` and `Rraw_1/L^4 ~= 0.030--0.040`. Combined with quadratic coercivity,
this gives a resonant bound losing only `1.36--1.71` against the exact resonant energy. The resonant
pair theorem is now a pair of explicit model/Fourier inequalities for `Rraw_j` and `lambda_min(C_x)`.

E72.220 removes the SVD basis from the raw HS term:
`||B_x^*U_yB_x||_HS^2 = Tr(PU_y^*PU_yP)`, where `P=E-kk^*` is the even-sector projection with the
model ground line removed. Hence it is bounded by the full-even overlap `||EU_yE||_HS^2`.

E72.221 audits that full-even overlap. Its leading profile is
`(dim_even/2)(1-y/L)`, with finite-section diffraction corrections. This gives a basis-free route to
the raw HS bound: prove a finite Fourier overlap estimate for `EU_yE`, then subtracting the ground
line can only improve it.

E72.222 tests the resulting simple bound for `Rraw_j`:
`Rraw_j <= (dim_even/2) sum_{S_j}(Lambda(n)^2/n)(1-log n/L)`. It is near-sharp, losing only
`1.04--1.14` against the exact `Rraw`. Thus the resonant degree-2 theorem reduces to a full-even
overlap estimate, quadratic model coercivity, and an elementary prime-square weighted sum.

E72.223 combines the even-leading raw bound with model coercivity to bound the exact resonant pair
energy. The resulting `R2-ELR` bound loses only `1.4--2.0`, improving with window size, and depends
only on `dim_even`, `lambda_min(C_x)`, and
`sum_{S_j}(Lambda(n)^2/n)(1-log n/L)`. This gives the cleanest current proof target for the resonant
degree-2 channel.

E72.224 simplifies the high-block cubic sign. If `A_j=sum_{n in S_j}A_n^+` and `K_j=A_j+A_j^*`, then
the tested blocks satisfy `Tr(K_j^3)=8 Re Tr(A_j^3)`. The sign flips by block:
`Re Tr(A_0^3)>0`, `Re Tr(A_1^3)<0`. Thus the odd high-block sublemma reduces to the finite
plus-current phase inequality `Re Tr(A_1^3)<=0`.

E72.225--E72.226 remove the complex phase ambiguity. The compressed plus-current is Hermitian to
roundoff after the model-relative even compression, so the high-block target is the real cubic moment
inequality `Tr(A_1^3)<=0`. The high block is indefinite, so there is no Loewner shortcut; the correct
statement is third-moment domination of the negative spectrum.

E72.227--E72.229 falsify the cellwise route and locate the mechanism. Individual cells do not have the
right cubic sign; the sign is created by coherent triple cross terms. Spectrally, the negative cubic
budget is mostly carried by a leading negative mode, while the positive cubic budget is smaller.

E72.230--E72.235 identify the leading negative mode as an explicit two-dimensional low block. With
`P=span_Q{0,1}`, `R=P^\perp`, and `A_1=[[B,C],[C^*,D]]`, the exact identity
`Tr(A_1^3)=Tr(B^3)+Tr(D^3)+3Tr(BCC^*)+3Tr(DC^*C)` shows that the sign is driven by `Tr(B^3)<0`,
with the tail small.

E72.236--E72.240 give the finite HOC3 certificate. For the `2x2` block `B`, with `t=Tr(B)` and
`s=Tr(B^2)`, `Tr(B^3)=(3ts-t^3)/2`. The tail is bounded by
`Tr(D_+^3)+3||D_+||op||C||_HS^2`. The certificate
`t<0`, `3s-t^2>0`, and
`-[(3ts-t^3)/2+3Tr(BCC^*)] >= Tr(D_+^3)+3||D_+||op||C||_HS^2`
passes for `lambda=12,16,20,24,28,32,36`, including the delicate `lambda=32` window. This turns the
odd high-block sublemma into scalar finite estimates for the low `2x2` block and a Schatten/operator
tail bound.

E72.241--E72.242 test and package a hybrid HOC3 certificate. The fully nonspectral tail bound
`||D||op(Tr(D^2)+3||C||_HS^2)` passes in the tested stable windows but fails at the delicate
`lambda=32` dip. The hybrid certificate uses the nonspectral bound in stable windows and the sharp
`D_+` certificate at `lambda=32`; it passes through `lambda=36`. This is the most proof-friendly form:
asymptotic norm estimates plus finite sharp exceptions.

E72.243--E72.244 express the low `2x2` invariants as kernel sums. With
`A_1=-sum beta_n M_{u_n}` and `G(u)=PM_uP`,
`t_B=-sum beta_n Tr(G(u_n))` and
`s_B=sum beta_m beta_n Tr(G(u_m)G(u_n))`. The condition `3s_B-t_B^2>0` is automatic from the
dimension-two inequality `t_B^2<=2s_B`. Thus the stable low proof reduces to a positive average of the
scalar kernel `K1(u)=Tr(G(u))` against the high prime-power measure, plus a quantitative tail estimate.

E72.245--E72.246 show that the `K1` average is geometric. The continuous high-window average of `K1`
is positive, and the prime-power weighted average tracks it closely. The actual discrepancy is small
relative to total variation, while `lambda=32` again appears as a finite delicate window. The LOW1
proof template is now:
`average(K1)>0`, `TV(K1)` controlled, and a prime-power discrepancy estimate strong enough to preserve
positivity, with finite exceptional windows handled by the sharp certificate.

E72.247 audits the fixed LM8 majorant and confirms the dimensional-drift issue: the current degree-8
majorants have `P_j(0)>0`, so their trace contains an `O(dim)` constant term. At `lambda=12`, this
constant cost is larger than the reported LM8 slack. Therefore the old LM8 fixed envelope is demoted
to diagnostic status.

E72.248--E72.249 repair the majorant architecture with homogeneous envelopes `P_j(u)=u^2R_j(u)`, so
`P_j(0)=P_j'(0)=0`. A homogeneous `P` degree 10 envelope passes from `lambda=16` onward, and the
finite `lambda=12` exception is recovered by homogeneous `P` degree 12 or higher. A final version still
needs rational/SOS interval certificates.

E72.250 records the corrected fixed-degree audit: fixed signed-residual approximation errors still
carry a `sqrt(dim)` factor unless made adaptive or replaced by an exact mechanism; fixed LM8 is
acceptable only in homogeneous form. Thus E72.195 is a stress diagnostic, not the final uniform theorem
statement.

E72.251 freezes the current normalizations. In the model-relative complement normalization used from
E72.210 onward, `lambda_min(C_model)` scales like `L^2`, not `L`. The low HOC3 margin is governed by
the `K1` kernel average and finite arithmetic dips, while the nonspectral tail is smoother and
compatible with a stronger decay. Future statements should use the `C_model >= c L^2` normalization
for these objects.

E72.252 extends the homogeneous LM8 stress to `lambda=56`, `dim=120`, using the same fixed
homogeneous `P` degree 10 coefficients from E72.248 and no refit. The certificate passes throughout
the extended range, with worst value still at `lambda=16`. This supports the claim that the
homogeneous redesign removed the dimensional drift seen in E72.247.

E72.253 extends the HOC3/K1 stress to `lambda=56`, `dim=120`. The nonspectral tail bound still fails
only at the known delicate `lambda=32` window; beyond it, the low/tail margin is positive and the
prime-power `K1` average remains positive. This supports the hybrid HOC3 package: sharp finite
exception plus stable nonspectral tail.

E72.254--E72.257 turn the homogeneous LM8 envelope into an interval-certified majorant. E72.254 shows
that checking `P(u)-target(u)` near the double zero is not enough; E72.256 checks the correct
`R`-inequalities directly and adds the strict homogeneous buffer `1.5e-3 u^2`. This preserves
`P(0)=P'(0)=0`, avoids dimensional drift, and passes the interval check. E72.257 verifies that the
strict buffer still leaves large LM8 slack through `lambda=56`, `dim=120`. The remaining paper-level
step is rational/SOS certification of the buffered univariate inequalities.

E72.258--E72.259 complete that rational univariate certification for the strict homogeneous LM8
envelope. E72.258 rounds the buffered degree-8 `R` coefficients to six-decimal rationals and verifies
that the selected extended stress windows still pass without refit. E72.259 then proves, by exact
rational Bernstein subdivision, the four inequalities
`R0>=1` on `[-1,0]`, `R0>=0.09` on `[0,1]`, `R1>=1` on `[-1,0]`, and `R1>=0.16` on `[0,1]`.
Thus the LM8 majorant algebra is now homogeneous, rational, and interval-certified; the remaining
LM8 work is the uniform Green/model moment bound for `K0,K1`, not the polynomial envelope.

E72.260 starts that Green/model proof. It proves the uniform even-overlap bound
`||E_+U_uE_+||_HS^2 <= (N+1)(1-u)+H_N/(2pi)` by reflection decomposition and Parseval. This is a
zero-free, model-only estimate: it converts the resonant degree-two overlap into positive
prime-power sums after the quadratic coercivity bound for `C_model`. The logarithmic reflected term is
the explicit price of even-sector diffraction near the interval boundary.

E72.261 finds and isolates a setup bug in the old RFBD helper: the global model ground is odd, so
symmetrizing it produces a near-zero vector and normalizing it removes an arbitrary even line. The pure
even-ground complement has only `O(1)` gap, not `L^2`, so it is not the pole-relative complement.
E72.262 repairs the geometry: subtract the global odd pole energy `e_pole`, but keep the full physical
even sector. This corrected pole-even complement restores `L^2` coercivity without the accidental
line removal. It also shows that the old LM8 envelope must be refit in the corrected geometry: exact
BSE is below target from `lambda=16`, while the old rational envelope is too loose at `lambda=16` and
passes again from `lambda=20` in the tested windows.

E72.263 performs that first pole-even LM8 refit. Homogeneous envelopes `P_j(u)=u^2R_j(u)` certify the
stable corrected windows from `lambda=20` onward in the tested range, but no tested degree through
`R=12` certifies the tight transition window `lambda=16` despite exact BSE passing there. The corrected
proof architecture should therefore use a stable homogeneous LM8 certificate for `lambda>=20` plus a
separate sharp finite certificate for `lambda=16`; windows below that are below the chosen asymptotic
threshold.

E72.264--E72.265 rationalize and exactly certify the stable pole-even LM8 envelope. Adding a homogeneous
buffer `0.002u^2` to the E72.263 degree-8 `R` polynomials and rounding to six decimals still leaves
stable stress margins at `lambda=20,24`. E72.265 proves the four required `R` inequalities by exact
rational Bernstein subdivision. Thus the stable pole-even LM8 majorant algebra is closed; what remains
is the uniform model/arithmetical moment bound plus a sharp finite certificate for the `lambda=16`
transition window.

E72.266 computes that transition window sharply in the corrected geometry. At `lambda=16`,
`BSE=0.9235401277444217`, giving slack `0.0173598722555782` below the target `0.9409`. The budget is
dominated by a few negative eigenmodes, especially the leading high-block mode, so the window should be
certified by interval eigenvalue/Sturm or low-mode-plus-tail methods rather than by the stable LM8
polynomial envelope.

E72.267 proves the exact pole-even coercivity identity:
`lambda_min(C_model)=lambda_0(H_model|even)-lambda_0(H_model|odd)`. Thus MCOER2 in the corrected
geometry is precisely an odd/even gap theorem for the archimedean model:
`lambda_0^even-lambda_0^odd >= c_C L^2`. This removes another layer of matrix opacity from the route:
the model coercivity input is now a parity-gap lower bound, independent of primes and zeros.

E72.268 consolidates the corrected RFBD package. The current proof-facing split is:
`MCOER2-pole-even(0.30,lambda>=16)`, stable rational LM8 for `lambda>=20`, a sharp finite BSE
certificate target at `lambda=16`, and a required recheck of HOC3/K1/mixed terms in the corrected
pole-even geometry. This explicitly marks which parts are closed and which still carry the real
mathematics before scalar WRL/Mellin divisibility can be claimed.

E72.269 performs the corrected pole-even HOC3/K1 recheck. With the full even sector and
`P=span{even modes 0,1}`, the high-block cubic sign survives: `Tr(A_1^3)<0`, `t_B<0`, and both sharp
and nonspectral full tails are dominated by the low margin for `lambda=16,20,24`. Thus the HOC3/K1
low-mode mechanism was not an artifact of the old accidental even-line removal.

E72.270 rechecks the mixed-block `XNEG` sign in the corrected geometry. The sign survives for
sufficient signed-polynomial degree: `D16`, `D32`, and adaptive degree give negative
`2Tr(G_0G_1)` for cuts `0.55,0.60,0.65` across `lambda=16,20,24`. Degree `D8` is too crude for the
lower cuts, so the corrected proof target should be `XNEG-pole-even-D16` or higher, not the old
degree-8 shorthand.

E72.271 expands `XNEG-pole-even-D16` as a finite mixed trace polynomial:
`2 sum a_r b_s Tr(K_0^rK_1^s)` with `r,s in {0,1,2,4,6,8,10,12,14,16}`. The expansion matches the
Chebyshev matrix evaluation to roundoff. This converts the mixed sign target into a finite list of
trace/cycle moments in the corrected pole-even blocks.

E72.272 states the corrected HOC3/K1 mechanism as an exact finite block identity. With
`A=[[B,C],[C^*,D]]` relative to `P=span{even modes 0,1}`, the sufficient certificate is
`t=Tr(B)<0` and
`LOW=-[(3ts-t^3)/2+3Tr(BCC^*)] >= ||D||op(Tr(D^2)+3||C||HS^2)`. This is a finite trace/norm
inequality in the corrected pole-even high block.

E72.273 repairs the bordered-minor endpoint in the corrected pole-even geometry. The Schur-complement
identity `<a,C_E^{-1}b>=-det[[C_E,b],[a^*,0]]/det(C_E)` survives unchanged with
`C_E=B_even^T(H_actual-e_pole I)B_even`. However, the old E72.79 HPAC source vector used the invalid
`Q=I-kk^*` and `h=k-xi`; the source must be rederived directly in the full pole-even sector before
claiming scalar WRL divisibility.

E72.274 performs the first corrected HPAC source probe in that full pole-even sector. It tests
`b_tau=B_even^T A_x(tau)xi_x`, with no old accidental projection and no `k-xi` displacement source.
For the first four finite roots at `lambda=16,20,24`, the bordered-minor formula agrees with the direct
solve at `1e-14` relative error and the scalar size remains small (`max|F|` about `1.9e-2`, `1.8e-2`,
`8.3e-3`). This repairs the endpoint object; it does not yet prove that this source is the exact
load-bearing scalar WRL source or that the finite-root decay is uniform.

E72.275 finds the corrected HPAC gauge. At finite roots, Weyl-nullity and parity give the exact
simplification `A_x(tau_j)xi_x=2xi_x+i(1/2+i tau_j)S_tau_jxi_x`. The dominant `2xi_x` term is not the
resonant HPAC channel; it is removed by the left actual-ground gauge
`a_s^perp=a_s-xi_x<xi_x,a_s>/<xi_x,xi_x>`, because `C_E^{-1}xi_x` is parallel to `xi_x`. This avoids the
old invalid `Q=I-kk^*` projection. After gauging, the tested residual drops from `~1e-2` to the
`2e-3--3e-3` resonant scale, and the finite-root simplification holds to `1e-12`.

E72.276 tests that corrected resonant residual on all finite roots in the fixed compact height window
`0<tau<=8`. The maximum of
`|<a_s^perp,C_E^{-1}i(1/2+i tau_j)S_tau_jxi_x>|` decreases from `2.57e-2` at `lambda=16` to `2.10e-3`
at `lambda=32`. This supports the compact-root decay theorem with the correct quantifier order. A
higher-height tail estimate is still separate; exploratory `H=12` already shows a larger finite-window
spike at `lambda=16`.

E72.277 proves the exact inverse-collapse identity
`<a,C_E^{-1}Sxi>=mu^{-1}<a,Sxi>-mu^{-1}<a,C_E^{-1}[C_E,S]xi>`, where `C_E xi=mu xi`.
For `S=S_tau_j` and the gauged Cauchy vector, the measured compact-root residual is entirely carried by
the diagonal term `mu^{-1}<a_s^perp,S_tau_jxi_x>`; the commutator correction is at numerical roundoff
in the tested windows. This replaces a crude and too-large gap bound by two sharper proof targets:
diagonal Cauchy-resolvent orthogonality plus commutator invisibility.

E72.278 factors the diagonal target explicitly. At finite roots, Weyl-nullity and parity give
`sum xi_n/(tau_j^2-d_n^2)=0`, and partial fractions yield
`<a_s^perp,S_tau_jxi_x>=z M_x(z)[-2tau_j/(z^2-tau_j^2)-V_x(tau_j)]`, with
`z=conjugate(s)`, `M_x(z)=sum xi_n/(z^2-d_n^2)`, and
`V_x(tau)=sum xi_n^2 2tau/(tau^2-d_n^2)`. The identity matches the matrix pairing to numerical
roundoff over `0<tau<=8`. Thus the compact-root diagonal proof is reduced to Cauchy-mass decay,
bounded variance bracket, and the separate commutator invisibility term.

E72.279 proves the Cauchy-mass decay component. By Cauchy-Schwarz,
`|M_x(z)| <= (sum |z^2-d_n^2|^{-2})^{1/2}` because `||xi_x||_2=1`. For `z` in a fixed compact subset
of `C\R`, the mesh sum is `O_K(L)`, hence `|M_x(z)|=O_K(L^{1/2})`. Combined with the pole-even gap
`mu_x>=cL^2`, this gives `|M_x(z)|/mu_x=O_K(L^{-3/2})`. This closes the Cauchy-mass part of the
diagonal HPAC compact-root estimate, conditional only on the already isolated pole-even gap.

E72.280 isolates the correct bracket condition. The operator norm of `S_tau` is not usable: it can
explode when a finite root lies extremely close to the mesh (`||S_tau||op ~ 4.6e6` at `lambda=32` in
the probe). But the vector channel `||S_tau xi_x||` stays small. Since
`|V_x(tau)|=|<xi_x,S_tau xi_x>| <= ||S_tau xi_x||`, the diagonal term is closed if
`sup_{tau_j<=H}||S_tau_jxi_x||=O_H(L^beta)` for any `beta<3/2`. This becomes the variance-bracket gate
`VBG`; the numerics suggest the stronger `O_H(1)` version.

E72.281 rewrites VBG as a positive squared-Stieltjes estimate. With
`W_x(t)=sum xi_n^2/(t-d_n)`, one has exactly
`V_x(tau)=W_x(tau)-W_x(-tau)` and
`||S_tau xi_x||^2=-W_x'(tau)-W_x'(-tau)+V_x(tau)/tau`. The identities check to roundoff. Thus the
remaining VBG theorem is no longer an operator-norm statement near poles; it is a root estimate for the
Stieltjes transform of the positive squared-ground measure.

E72.282 proves VBG with exponent `beta=1`. At a finite Weyl root,
`sum xi_n/(tau_j-d_n)=0`; the closest-pole term is therefore controlled by the sum of all other mesh
terms, and Cauchy-Schwarz plus the reciprocal-square mesh sum gives `E_-(tau_j)=O_H(L^2)`. By evenness,
the same holds for `E_+(tau_j)`. Hence
`||S_tau_jxi_x||<=sqrt(E_-)+sqrt(E_+)=O_H(L)`, which is enough because E72.279 supplies the
`L^{-3/2}` Cauchy-mass/gap factor. This closes the diagonal compact-root term, conditional on the
pole-even gap.

E72.283 closes the compact-root commutator term under the natural upper complement bound
`||C_E||=O(L^2)`. The crude estimate
`|K_x| <= mu^{-1}||a_s^perp||||C_E^{-1}||||[C_E,S_tau]xi||`, together with
`||[C_E,S_tau]xi|| <= (||C_E||+mu)||S_tau xi||`, gives `O(L^{-1/2})` using
`mu>=cL^2`, `||a_s^perp||=O_K(L^{1/2})`, and VBG. Thus the compact-root HPAC theorem is now reduced to
the pole-even lower gap, the upper complement bound, and the corrected source/gauge identities.

E72.284 splits the upper complement bound as
`C_actual=C_model+Delta_arith` and
`||C_actual||<=||C_model||+lambda_max(Delta_arith)_+`. This avoids charging the negative arithmetic
directions against an upper bound. The observed scales are `||C_model||/L^2 ~ 1.0--1.3` and
`lambda_max(Delta_arith)_+/L^2 ~ 0.13--0.16`. Thus the upper complement input is reduced to `MUCB`
(`||C_model||=O(L^2)`) plus `APCB` (positive-part arithmetic ceiling).

E72.285 rewrites `APCB` as the exact finite autocorrelation inequality
`Delta_arith=-sum Lambda(n)n^{-1/2}Q_{log n}` with
`<v,Q_yv>=2Re int_0^{L-y} f_v(t+y)conj(f_v(t))dt`. The probe reconstructs `Delta_arith` from these
cells to roundoff. The absolute incoherent ceiling is far larger than the positive part, so `APCB` must
be proved as a coherent autocorrelation estimate, not by termwise absolute values.

E72.286 reduces `MUCB` to the upper endpoint of the pure archimedean model. Since
`C_model=H_model|even-lambda_0(H_model|odd)I`, one has
`||C_model||=lambda_max(H_model|even)-lambda_0(H_model|odd)`. Thus the model upper complement bound is
the upper partner of the lower odd/even gap theorem, with no arithmetic input.

E72.287 gives a sufficient scalar route for `APCB`. The arithmetic autocorrelation operator is a finite
compression of the translation convolution with Dirichlet symbol
`P_L(omega)=sum_{n<=e^L}Lambda(n)n^{-1/2}e^{i omega log n}`. Therefore
`lambda_max(Delta_arith)_+ <= -2 inf_omega Re P_L(omega)`. The tested symbol floor is looser than APCB
but remains on the `L^2` scale. Thus APCB follows from the scalar Dirichlet-polynomial floor
`-2inf Re P_L=O(L^2)`.

E72.288 audits that scalar floor. Since `P_L` is the cutoff version of `-zeta'/zeta` on the critical
line, an off-critical zero would naturally generate excursions of size `e^{(beta-1/2)L}` near its
height. Therefore `DSF-O2` should be treated as RH-strength, not as a routine PNT estimate. The safer
proof target is the compressed APCB inequality itself, which is numerically much smaller than the
full-line symbol floor.

E72.289 probes the compression mechanism. The top positive eigenvector of `Delta_arith` has almost all
its mesh-frequency mass in `|d|>=8`, while the full-line Dirichlet symbol is worst near
`omega~=0.5--0.7`. Thus the compressed APCB constant is small because the finite even compression avoids
the bad low-frequency symbol directions. This points to an `APCB-band` proof: low band small, high band
`O(L^2)`, cross terms controlled separately.

E72.290 turns that diagnostic into a block split. For a mesh-frequency cutoff `D0`, write
`Delta_arith=[[A,B],[B^*,D]]` on low/high bands; then
`lambda_max(Delta)_+ <= lambda_max(A)_+ + lambda_max(D)_+ + ||B||`. The probe shows `D0=4` gives a
small low budget and a smaller cross term than `D0=2`, while the high block carries the top positive
mode. The remaining APCB target is therefore a high-band compressed autocorrelation ceiling, plus
low/cross budgets.

E72.291 reduces the high-band ceiling to a Gershgorin row-sum estimate. For the `|d|>=4` high block,
`lambda_max(H)<=max_i sum_j|H_ij|`; the observed row-sum ceiling is stable at about `0.34--0.37 L^2`,
while the top eigenvalue is `0.13--0.16 L^2`. Thus high-band APCB can be attacked by explicit row sums
using the closed formula for `Q_y(m,n)`.

E72.292 completes the APCB-band budget. With cutoff `|d|<4`, the low block has tiny finite rank and
positive ceiling about `0.05--0.06 L^2`; the cross block is controlled by Frobenius/Schur at about
`0.02--0.04 L^2`; the high block is governed by H-GERSH. APCB is now reduced to three non-spectral
estimates: LOW-FIN, H-GERSH, and CROSS-HS.

E72.293 stops the diagnostic loop and rewrites the current endpoint as an analytic lemma stack. It
proves, from previously established identities, that
`GAP + UCB + corrected source/gauge => fixed-height compact-root HPAC decay`, and it records the
then-current attempt to obtain `UCB` from `MUCB + APCB`. E72.295 later retires that global branch.

E72.294 corrects that last sentence. The absolute row-sum target H-GERSH is not the right asymptotic
proof mechanism: it destroys the sign of the PNT main term, whose natural unsigned mass is exponential
in `L` because of the `n^{-1/2}` weight. The correct high-band target is signed:
`Delta_arith=Delta_main+Delta_rem`, with
`Delta_main=-int_0^L e^(y/2)Q_y dy`. On the exact Fourier mesh the full-translation symbol has
`Re int_0^L e^(y/2)e^(i omega_m y)dy>0`, hence the main contribution to `Delta_arith` is
non-positive. APCB should therefore be attacked as `LOW-FIN + H-SIGNED + CROSS-HS`, where H-SIGNED
controls only the positive part of the compressed arithmetic remainder plus a pure boundary cost.

E72.295 goes further and proves the decisive high-mode obstruction. For the actual one-sided diagonal
cell `Q_y(m,m)=2(1-y/L)cos(omega_m y)`, direct integration gives
`int_0^L e^((1/2+iomega)y)(1-y/L)dy=-1/a+(e^(L/2)-1)/(La^2)`, `a=1/2+iomega`. For fixed
`|omega|>1/2`, this makes the diagonal Rayleigh quotient of `Delta_arith` positive of size
`e^(L/2)/L`, up to a smaller classical PNT error. Therefore global APCB, and hence the global
upper-complement route, is false asymptotically.

E72.296 replaces the false global bound with the source-local estimate actually needed by the
inverse-collapse identity. The new target is the directional commutator bound
`DCB: sup_{tau_j<=H}||[C_E,S_tau_j]xi||=O_H(L^alpha)`, `alpha<7/2`. The exact formula
`([Q_y,S_tau]xi)_m=sum_j Q_y(m,j)(s_j-s_m)xi_j` contains the smoothing factor `s_j-s_m`, which cancels
the dangerous `1/(j-m)` denominator after the commutator is inserted. The compact-root route is now
`GAP + corrected source/gauge + VBG + DCB => fixed-height HPAC decay`.

E72.297 gives the sharper spectral identity behind DCB. Since `xi` is the actual ground vector in the
pole-even complement, `C_E xi=mu xi`, hence
`[C_E,S_tau]xi=(C_E-mu I)S_tau xi`. Therefore DCB is a second spectral moment of the single vector
`S_tau xi`, not a global complement norm. A sufficient package is
`FORM-DCB: <S_tau xi,C_E S_tau xi>=O_H(L^4)` plus `EFF-SUP: the effective C_E support of S_tau xi is
O_H(L^2)`, which gives `||[C_E,S_tau]xi||=O_H(L^3)` and closes the compact-root commutator contribution.

E72.298 converts `FORM-DCB` into the exact double-commutator identity
`<S_tau xi,(C_E-mu I)S_tau xi>=-1/2 sum_{m,n}xi_mxi_n(s_m-s_n)^2C_E(m,n)`. This kills every diagonal
term, including the high-mode obstruction of E72.295, and also kills the scalar pole shift. It also
records the direct square identity
`||[C_E,S_tau]xi||^2=sum_m|sum_n C_E(m,n)(s_n-s_m)xi_n|^2`. The next proof target is therefore the
finite inequality `DCB-square <= C_H L^6`, or the weaker double-commutator `FORM-DCB <= C_H L^4` plus
an effective support bound.

E72.299 Abelizes the arithmetic part of `FORM-DCB`. It defines the scalar kernel
`F_tau(y)=sum_{m,n}xi_mxi_n(s_m-s_n)^2Q_y(m,n)`. The diagonal is absent and
`F_tau(0)=F_tau(L)=0`, so partial summation gives an exact no-boundary identity:
`FORM_arith=(1/2)int e^(y/2)F_tau(y)dy -(1/2)int E(e^y)e^(-y/2)(F_tau'-F_tau/2)dy`. Thus the next
arithmetic target is `MAIN-FORM + REM-FORM`, both for one explicit commutator-smoothed scalar kernel.

E72.300 corrects the load-bearing use of E72.299. The standalone arithmetic `MAIN-FORM` contains an
`e^(L/2)/L` divided-difference factor, so it should not be bounded alone. In the actual operator,
`C_E=W02-WR-Prime-e_pole I`, and the scalar pole shift vanishes in the double commutator. Combining
`W02` with the Abel formula for `Prime`, the full `e^(y/2)` main cancels exactly:
`FORM_actual=-(1/2)int e^(-y/2)F_tau +(1/2)WR(F_tau)
-(1/2)int E(e^y)e^(-y/2)(F_tau'-F_tau/2)`. The corrected target is
`LOWEXP-FORM + WR-FORM + PNTERR-FORM`.

E72.301 collapses the two archimedean pieces of E72.300. Since `F_tau(0)=0`, the `WR` functional has no
constant or logarithmic endpoint terms, and
`1/2 WR(F_tau)-1/2 int e^(-y/2)F_tau = 1/2 int e^(-5y/2)/(1-e^(-2y))F_tau`. The remaining FORM target is
therefore `ARCH-FORM + PNTERR-FORM`.

E72.302 rewrites `PNTERR-FORM` by the explicit formula. With
`A_tau=e^(-y/2)F_tau` and `A_tau(0)=A_tau(L)=0`, each zero contribution cancels the factor `1/rho` and
becomes `M_tau(rho-1/2)=int_0^L e^((rho-1/2)y)F_tau(y)dy`. The transform has the closed finite formula
`M_tau(z)=(1-e^(zL)) sum_{m!=n}xi_mxi_n(s_m-s_n)^2[Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)]`,
`Phi_z(d)=d/(z^2+d^2)`. Thus the remaining arithmetic content is the Mellin spectral divisibility
target `MSD-FORM`.

E72.303 packages the compact-root theorem:
`GAP + VBG + ARCH-FORM + MSD-FORM + (EFF-SUP or DCB-square) => fixed-height compact-root HPAC decay`.
It also marks what remains outside the compact-root theorem: the source theorem, high-root tail,
transport gates, and bordered-minor divisibility to scalar WRL.

E72.304 unifies the archimedean residual and spectral error. Since
`e^(-5y/2)/(1-e^(-2y))=sum_{k>=0}e^(-(5/2+2k)y)`, one gets
`ARCH_tau=1/2 sum_{k>=0}M_tau(-(5/2+2k))`. These points are exactly `rho-1/2` for the trivial zeros
`rho=-2,-4,...`. Thus the next target is not two independent estimates but one unified shifted
explicit-formula divisor identity `UMSD-FORM` for `M_tau`.

E72.305 completes the explicit-formula bookkeeping. In `PNTERR_tau`, the constant `-log(2pi)` vanishes
because `A_tau(0)=A_tau(L)=0`, and the trivial-zero term
`-(1/2)log(1-e^(-2y))` contributes exactly `2ARCH_tau`. Therefore
`FORM_actual(tau)=-(1/2)sum_rho M_tau(rho-1/2)`, with only nontrivial zeros remaining. The compact
Mellin target is now `NZ-MSD-FORM`, and the compact-root theorem sharpens to
`GAP + VBG + NZ-MSD-FORM + (EFF-SUP or DCB-square) => fixed-height compact-root HPAC decay`.

E72.306 normalizes `M_tau(z)=(1-e^(zL))N_tau(z)`. The apparent poles of the divided-difference formula
at the Fourier mesh are removable, so there is no finite mesh-residue shortcut. In normalized form the
target is `sum_rho(1-e^((rho-1/2)L))N_tau(rho-1/2)=O_H(L^4)`. For an off-line shifted zero
`z=rho-1/2` with `Re z>0`, this requires exponential annihilation of `N_tau(z)` or a packet symmetry
cancellation.

E72.307 rewrites `N_tau` as a finite Loewner double commutator:
`N_tau(z)=(2/L)<xi,[S_tau,[L_z,S_tau]]xi>`, where `L_z` is the Loewner matrix of
`Phi_z(d)=d/(z^2+d^2)`. Thus the normalized divisor target is now a zero-weighted family of finite
commutator quadratic forms.

E72.308 factors the Loewner kernel:
`[Phi_z(a)-Phi_z(b)]/(a-b)=(z^2-ab)/((z^2+a^2)(z^2+b^2))`. By the even parity of `xi` and odd parity
of `d_m,s_m`, this gives the rank-two scalar normal form
`N_tau(z)=-(4/L)(z^2U_0(z)U_2(z)+V_1(z)^2)`. The compact MSD target is now a resolvent moment identity,
not a matrix identity.

E72.309 uses the finite Weyl root equation
`sum_m xi_m/(tau^2-d_m^2)=0` to cancel the rank-two expression down to rank one:
`N_tau(z)= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau`, where
`R_tau=sum_m xi_m/(tau^2-d_m^2)^2`. Thus the compact Mellin obstruction is now carried by the single
Stieltjes moment `U_0(z)=sum_m xi_m/(z^2+d_m^2)`.

E72.310 rewrites `U_0` as the finite Cauchy transform of the same ground vector:
`U_0(z)=iC_x(iz)/z`, `C_x(w)=sum_m xi_m/(w-d_m)`. The compact target becomes `MC-NZ`: a Mellin-weighted
sum of `C_x(i(rho-1/2))`, while the same Cauchy transform vanishes at the finite Weyl roots `tau`.

E72.311 removes the remaining matrix language from `MC-NZ`. Writing
`C_x(w)=P_x(w)/D_x(w)`, where `P_x` is the finite Cauchy numerator, the compact target is exactly a
rotated numerator bound at `w=i(rho-1/2)`. The real-root divisor `P_x(tau_j)=0` is necessary but not
sufficient: by itself it does not force exponential suppression at off-line rotated points. The new
analytic target is `RNS`, a scalar residue/contour theorem for the quotient
`p_x(-z^2)/Delta_x(z)`.

E72.312 converts `RNS` into a contour-residue lemma. For
`F_{tau,L}(s)=(1-e^((s-1/2)L))((s-1/2)tau^2)/(tau^2+(s-1/2)^2)Q_x(s-1/2)`, the zero sum is exactly the
contour integral of `F_{tau,L} Xi'/Xi` minus the finite-pole residues. Thus the remaining proof splits
cleanly into `REM` (mesh and kinematic poles are removable by finite algebra) plus `CB` (horizontal
decay and vertical contour bounds).

E72.313 proves `REM` in the unreduced Cauchy form. Mesh poles of `C_x(iz)` occur at
`z=-id_m=-2pi i m/L` and are killed by the simple zero of `1-e^(zL)`. The kinematic poles
`z=+-i tau` are killed by the finite Weyl equation `C_x(tau)=0` and oddness `C_x(-tau)=-C_x(tau)`.
Therefore the compact contour identity has no finite-pole residue term; only `CB` remains.

E72.314 identifies the analytic estimate needed for `CB`: the sine-quotient bound `SQB`,
`|(1-e^(zL))C_x(iz)| <= A L^B(1+|Im z|)^B` in fixed shifted strips. This is the exact place where the
off-line exponential factor must be neutralized. `SQB + LOG + TAIL` implies `CB`, hence the compact
root branch. The remaining new theorem is therefore a finite sine-quotient/product bound for the CCM
Cauchy numerator.

E72.315 separates the denominator from the numerator in `SQB`. The factor `1-e^(zL)` is exactly the
canonical sine product for the Fourier mesh, so `(1-e^(zL))/D_x(iz)` is explicit after finite product
normalization. The nonstandard theorem is now `NUM-GROW`: polynomial strip growth of the normalized
Cauchy numerator, equivalently regularity of the residue vector `xi_m` under the pole-even CCM
ground-vector equation.

E72.316 audits `NUM-GROW`. Ordinary `l^1`, `l^2`, bounded-variation, or Sobolev control of `xi_m` gives
only polynomial bounds for `C_x(iz)`, whereas `SQB` requires `C_x(iz)=O(e^{-Re(z)L})` in the right
shifted strip. Thus the remaining theorem is a one-sided Paley-Wiener Cauchy identity `PW-Cauchy`
derived from the actual finite equation `C_E xi=mu xi`, not from generic residue regularity.

E72.317 writes that remaining theorem as an exact transformed eigenvector equation. With
`G_x(z)=(1-e^(zL))C_x(iz)`, multiplying `C_E xi=mu xi` by `(1-e^(zL))/(iz-d_m)` and summing gives
`(mu+e_pole)G_x=T_W02[xi]-T_WR[xi]-T_Prime[xi]`. Thus `PW-Cauchy` follows from `TPW`: polynomial strip
growth of the combined transformed kernel, without estimating the three terms separately by absolute
values.

E72.318 computes the transformed cell kernel. The complete Fourier mesh identity
`(1-e^(zL))sum_m e^(id_m r)/(iz-d_m)=iL e^(z(L-r))` gives
`KQ_z(y;n)=i[z+i d_n]^{-1}(e^(z(L-y))-e^(i d_n y)+e^(zL)e^(-i d_n y)-e^(zy))`, with an explicit finite
tail for the truncated CCM mesh. Therefore `TPW` is a shifted Cauchy-packet Abel identity plus finite
tail control, not a generic matrix bound.

E72.319 applies Abel summation and the explicit formula to that packet without dropping endpoint
terms. For a general packet `B`, the combined functional is
`Lcal(B)=sum_rho M_B(rho-1/2)+Arch_0(B)`. In the old FORM channel `B(0)=0`, so `Arch_0` vanished; for
the transformed packet, `B_z(0)=2G_x(z)`, hence `Arch_0(B_z)=2kappa_LG_x(z)` and is absorbed into the
left coefficient. The remaining `TPW` target is now a packet-zero bound plus a finite Fourier-tail
bound.

E72.320 computes the packet Mellin transform. The complete-mesh main collapses to
`M_z(w)=[((w+z)+e^(zL)(w-z))G_x(w)-2wG_x(z)]/(w^2-z^2)`. Thus the endpoint-renormalized `TPW` is a
scalar interpolation equation for `G_x` at `z` and at the shifted nontrivial-zero parameters
`w=rho-1/2`, plus the finite mesh tail.

E72.321 uses the even shifted divisor of `Xi` and the pole-even identity
`G_x(-w)=e^(-wL)G_x(w)`. The zero-sum part proportional to `G_x(z)` cancels exactly by pairs `{w,-w}`.
The complete-mesh zero pressure is now the paired interpolation sum `PAIR-Z`, plus the finite tail.

E72.322 evaluates the paired equation at zero nodes. The self-pair has the removable limit
`Pair_a(a)=(L+sinh(aL)/a)G_x(a)`, so the nodal values satisfy an explicit linear system
`[mu+e_pole-2kappa_L-L-sinh(aL)/a]G_x(a)-sum_{w!=a}K_{a,w}G_x(w)=Err_a`. For an off-line zero
`Re a>0`, the diagonal contains exponential forcing. The remaining theorem is zero-node dominance
`ZND` plus finite-tail control.

E72.323 corrects the naive diagonal-dominance reading. For an off-line quadruple
`{a,-a,conj(a),-conj(a)}`, the off-diagonal coupling between `a` and `conj(a)` is also exponential.
The correct leading object is a `2 x 2` block with determinant
`(a-conj(a))^2/[4a conj(a)(a+conj(a))^2]`, nonzero when `Im a != 0`. Thus an isolated maximal
off-line quadruple is forced by block invertibility, provided the tail/error is polynomial and
lower-real-part couplings are perturbative.

E72.324 generalizes this to any simple maximal-real-part cluster. The leading cluster matrix is
`C_A(j,k)=1/(a_j+a_k)`, a symmetric Cauchy matrix with determinant
`prod_{j<k}(a_k-a_j)^2/prod_{j,k}(a_j+a_k)`, nonzero because `Re(a_j+a_k)>0`. Thus simple cluster
invertibility is closed; the remaining nodal theorem is finite-tail/outside-window control plus
confluent bookkeeping for multiple zeros.

E72.325 closes the multiplicity bookkeeping. Multiple zeros give the confluent Cauchy matrix
`(p!q!)^{-1}partial_x^p partial_y^q(1/(x+y))|_{x=a_j,y=a_k}`. A partial-fraction nullspace argument
proves it is invertible whenever `Re a_j>0`. Therefore maximal-cluster invertibility is closed,
including multiplicities; the remaining transformed-route issues are finite Fourier tail,
outside-window zero contribution, and nodal-to-strip propagation.

E72.326 proves the nodal-to-strip propagation lemma. In the paired scalar equation, exponential factors
attached to off-line zero nodes are cancelled by the nodal suppression from the Cauchy-block theorem;
critical-line nodes need only polynomial control. Thus `OFF-NODAL + CRIT-POLY + OUT-POLY + TAIL-POLY`
imply `PW-Cauchy` on fixed compact shifted strips, up to the polynomial lower bound for
`mu+e_pole-2kappa_L`.

E72.327 closes `CRIT-POLY`. On the shifted critical line `z=i gamma`, the cancelled Cauchy multiplier is
`(1-e^{-iuL})/(u-d_m)`, with `u=-gamma`, a divided difference of the Fourier exponential against the
mesh value `e^{-id_mL}=1`. Hence it is bounded by `L`, and
`|G_x(i gamma)| <= L ||xi||_1 <= L N_L^{1/2}`, polynomial in fixed active windows.

E72.328 isolates the remaining left coefficient
`Lambda_L=mu+e_pole-2kappa_L`. The transformed route only needs a polynomial lower bound. This follows
from the pole-even gap `mu>=cL^2` once the explicit endpoint scalar
`kappa_L=Arch_0(1)` is shown to be subquadratic, expected logarithmic from the WR finite-part
normalization. This is a zero-free elementary normalization gate.

E72.330 closes that normalization gate. Splitting
`Ren int e^(y/2)/(2sinh y)` into `(e^(y/2)-1)/(2sinh y)` plus the finite part of `1/(2sinh y)`, the
entire `L`-dependence cancels against the `1/2 log(tanh(L/2))` term in `WR(1)`. Hence
`kappa_L=kappa_*` is a fixed finite-part constant, and `Lambda_L` inherits the pole-even gap scale.

E72.329 consolidates the transformed route. The structural pieces `REM`, transformed cell, Abel packet,
pair cancellation, Cauchy-block cluster invertibility, multiplicity, critical-line polynomial control,
and nodal-to-strip propagation are now organized into one theorem. The remaining transformed gates are
`TAIL-POLY` and `OUT-POLY`; proving them gives `PW-Cauchy`, hence `SQB => CB => RNS =>
MC-NZ => NZ-MSD`, and then the compact-root HPAC decay needed by the Phase 72 scalar WRL chain.

E72.331 audits `TAIL-POLY`. A pointwise finite Fourier tail bound is false at polynomial cutoff in
right shifted strips because the cancelled Cauchy coefficients have size `e^(sigma L)/m`. Therefore the
tail must be controlled only after applying the combined functional `Lcal`. The correct target is the
explicit signed coefficient identity
`sum_{|m|>M}(1-e^(zL))/(iz-d_m)Lcal(b_m)=O_K(L^B)`, called `TAIL-COEFF/TAIL-ABEL`.

E72.333 computes those coefficients. Since tail indices satisfy `m != n`, the endpoint values vanish
and `Lcal(b_m)` is only the nontrivial-zero transform:
`sum_rho(1-e^(w_rhoL))sum_n xi_n[Phi_{w_rho}(d_m)-Phi_{w_rho}(d_n)]/[pi(n-m)]`. Thus `TAIL-POLY` is
now the explicit spectral identity `TAIL-SPEC`, tied to the same Cauchy moments as `MC-NZ`.

E72.332 audits `OUT-POLY`. Absolute zero-counting is insufficient because the paired kernel has a
large-`w` leading scale like `G_x(w)/w`. The correct target is the contour estimate `OUT-CONTOUR`:
integrate the paired kernel against `Z'(w)/Z(w)` on zero-avoiding outside rectangles and prove the
tail is polynomial. This reduces the outside-zero gate to high-frequency decay of the paired cancelled
Cauchy kernel.

E72.334 unifies the two tail gates. The actual finite packet is
`B_z^M=B_z^infty-B_z^tail`, so after choosing a zero window the only true remainder is
`Rem_T^M(z)=sum_{w notin W_T}(M_z^M(w)+M_z^M(-w))`. The earlier `TAIL-SPEC` and `OUT-CONTOUR` are just
pieces of this same finite contour remainder. The transformed route now has one tail gate:
`UREM-POLY`, polynomial boundedness of that finite packet contour.

E72.335 identifies the endpoint decay behind `UREM-POLY`. Since `B_z^M(0)=2G_x(z)` and `B_z^M(L)=0`,
the pair `M_z^M(w)+M_z^M(-w)` cancels the leading `1/w` endpoint term. A second integration by parts
reduces `UREM-POLY` to `PACK-SMOOTH`: polynomial bounds for endpoint derivatives and
`int |(B_z^M)''|`.

E72.336 starts `PACK-SMOOTH`. The first derivative of the overlap kernel has the exact identity
`Q'_0(m,n)=Q'_L(m,n)=-2/L` for all active `m,n`, so endpoint derivatives collapse to
`-(2/L)(sum_m(1-e^(zL))/(iz-d_m))(sum_n xi_n)`. The endpoint part is therefore rank-one; the remaining
smoothness gate is the oscillatory bulk second-derivative estimate `BULK-SMOOTH`.

E72.337 rewrites `BULK-SMOOTH` in packet form. With
`A_z(r)=sum_m(1-e^(zL))/(iz-d_m)e^(id_mr)` and `X(r)=sum_nxi_ne^(id_nr)`, the finite packet is an
integral of `A_z(t+y)conj(X(t))` plus its reflected partner. The key identity
`A_z'=-zA_z-i(1-e^(zL))D_M` converts dangerous `d_m` powers into the finite Dirichlet kernel. Thus
`BULK-SMOOTH` reduces to Dirichlet-Cauchy packet bounds, not raw `Q''` estimates.

E72.338 audits this and corrects the gate. Absolute `PACK-SMOOTH` is too strong: in the complete mesh,
`A_z(r)=iLe^(z(L-r))`, whose `L^1` norm is exponential for `Re z>0`. The valid target must keep the
pairing before absolute values. The replacement is `POSC`, a paired oscillatory contour estimate
obtained from `M_z^M(w)+M_z^M(-w)`.
