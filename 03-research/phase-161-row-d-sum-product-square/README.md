# Phase 161 — Row D: the sum×product square

Status: **OPEN — PRODUCT-HARDY PORT CONSTRUCTED; REVERSE MARKOV PULLBACK REMAINS**.

This phase develops `O-D4.1` of phase 160: use the exact multiplicative identity
`Lambda * 1 = log` and additive Poisson/Fourier in the same quadratic construction.

Files:

- `R161_000_BLUEPRINT.md`: objective, gates and success criteria.
- `R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md`: the finite Poisson–Chebyshev anomaly identity.
- `R161_002_SQUARE_VERDICT_AND_NEXT_LEMMA.md`: the canonical square, its sign-blindness, and the residual target.
- `R161_003_POLAR_RENORMALIZATION.md`: why raw truncation cannot work and the renormalized next object.
- `R161_004_CORPUS_COLLISION_AND_STOP_GATES.md`: matches the scalar and positive-fibre continuations to prior no-go
  results and retires scalar `L161.2`.
- `R161_005_FIRST_CONTACT_POISSON_PORT.md`: specialises the anomaly to first contact and isolates the remaining
  oriented exterior port.
- `R161_006_EXTERIOR_PORT_KERNEL.md`: gives the exact one-sided lattice-minus-continuum kernel of that port and
  separates its opposite-tail contribution into the two Tate directions.
- `R161_007_CHEBYSHEV_CRITICAL_JET.md`: multiplies the oriented Euler current by the Poisson factor and proves that
  its regularised value at a simple zero is `-zeta'(rho)K_F(rho-1/2)`.
- `R161_008_PRODUCT_HARDY_SEPARATION.md`: uses the first-contact `H^s`, `s>1/4`, regularity to place the product-
  regularised orientations in opposite Hardy spaces after a polar correction that preserves critical values.
- `R161_009_POLAR_COEFFICIENT_MATCH.md`: identifies those polar coefficients with the already proved crossed Tate
  collar currents; only the vector graph decomposition remains.
- `R161_010_FIRST_CONTACT_CLOSURE.md`: records the attempted graph decomposition and its conditional consequence;
  its claimed proof is retracted by the typed scattering audit.
- `R161_011_TYPED_SCATTERING_AUDIT.md`: restores the missing cosine/reflection scattering and reduces closure to
  trivial intersection of the arithmetic product-port range with the appropriate Sonin eigenspace.
- `R161_012_PRODUCT_RANGE_AND_FIRST_COLLAR.md`: restates the remaining arithmetic condition as physical division by
  zeta and computes the exact `n=2,3,4` product-port germ immediately above `T=0.8`.
- `R161_013_FIRST_COLLAR_TRANSMISSION.md`: proves the inner/outer `2,3,4` transmission law, shows that the bare
  differentiated co-Poisson equation is not independent, and isolates `C Q C` as the surviving cross-place term.
- `R161_014_SONIN_GAMMA_COERCIVITY.md`: proves strict Gamma coercivity on the product-port Sonin sector and reduces
  closure to one explicit upper/null balance for the sum--product excess energy.
- `R161_015_CANONICAL_HARDY_GAUGE_AND_NORM_SLOPE.md`: fixes the polar-vector gauge by the Hardy reproducing kernel and
  identifies the excess energy with minus the exact contour derivative of the endpoint-normalized port norm.
- `R161_016_MARKOV_PULLBACK_AND_ARROW_AUDIT.md`: proves that the direct Markov pullback has the automatic, non-closing
  norm direction; identifies the required reverse physical typing and separates the finite `2,3,4` collar route
  from the necessarily infinite, Tate-centred global norm route.
- `R161_017_EXACT_SCATTERING_DEFECT.md`: computes the exact functional-equation defect of the two product ports;
  identifies its interior value with the Tate forcing and proves that completing the physical cosine scattering
  would reduce first contact to the still-open homogeneous zero-mode problem.
- `R161_018_PC_GRAPH_COMPARISON_NO_GO.md`: compares that defect with the `(PC-ren)` graph limit and proves that every
  linear completion collapses to the already known zero commutator; new sign information must remain quadratic and
  finite-parameter until after the physical ports are connected.
- `R161_019_GAMMA_POLE_LATTICE_RIGIDITY.md`: proves that exact physical scattering forces an infinite complete
  lattice of exponential moments through the positive odd Gamma poles; hence the explicit product-range/Sonin
  intersection is trivial and the missing upper balance follows with equality.
- `R161_020_COMPRESSED_SCATTERING_AND_LEAKAGE_SQUARE.md`: reduces full physical scattering to a one-sided compressed
  cosine equation and isolates its failure as an explicit nonnegative Hardy leakage square, the new finite `(PC)`
  matching target.
- `R161_021_EXTREMAL_CROSS_CORRELATION.md`: weakens the terminal target again: one oriented scalar cross-correlation,
  equivalently half the full cosine-scattering defect square, suffices. It states the exact radical-polarization
  acceptance test for a finite `(PC-ren)` conjugate test.
- `R161_022_CANONICAL_CONJUGATE_TEST_AND_BOUNDARY_RECIPROCITY.md`: constructs the conjugate test canonically as
  `Pi_T P_T Z* g` and decomposes the extremal correlation into one crossed-Tate term and two exterior pairings. The
  terminal theorem is reduced to an explicit exterior Green reciprocity for the finite `(PC-ren)` boundary layer.
- `R161_023_CONJUGATE_TEST_COLLAPSE_AND_TRUE_RECIPROCITY_GATE.md`: performs the Tate projection calculation and proves
  that the direct conjugate test recombines tautologically into `(PC-ren)`. It rejects treating the indefinite
  crossed Tate matrix as the positive Gram and isolates the need for an independent antisymmetric boundary law.
- `R161_024_POLE_REMOVABILITY_IS_ENOUGH.md`: weakens the terminal theorem drastically: it is enough that the explicit
  scattering defect be removable at `s=3,5,7,...`. This alone forces the complete Gamma moment lattice and `F=0`;
  the new finite target is residue cancellation in the safe half-plane, without global scattering.
- `R161_025_EXACT_GAMMA_RESIDUE_ENERGY.md`: computes the exact residues, rejects the merely linear safe-half-plane
  passage, and packages the complete residue lattice into a finite faithful positive energy. The surviving target
  is a finite quadratic `(PC-ren)` realization which vanishes on first contact.
- `R161_026_GAMMA_POLE_ENERGY_IS_A_HANKEL_BOUNDARY_DERIVATIVE.md`: identifies that residue energy exactly with the
  negative displacement derivative of a positive Hankel form built from the positive-odd Gamma tail. This supplies
  a canonical reflected boundary square and reduces closure to its reverse first-contact displacement inequality.
- `R161_027_METHOD_OF_IMAGES_AND_PRIME_FORCE_AUDIT.md`: realizes the Gamma-Hankel form as interaction with a
  separated reflected copy and its pole energy as the gap force. It proves that raw prime contacts have no sign and
  formulates the exact surviving target: `(PC-ren)` must complete the combined image force into a same-sign Poisson
  boundary square.
- `R161_028_POLAR_LAYER_IS_THE_EXTERIOR_IMAGE.md`: proves that at `log N=2(T+delta)` the Euler--Maclaurin polar layer
  has exactly the image support and its cutoff derivative is the reflected image on a parity source. This embeds
  the Gamma-pole force directly into the moving `S_a-C_a` discrepancy and identifies its continuous and jump parts.
- `R161_029_MOVING_DISCREPANCY_SIGN_AUDIT.md`: computes the exact continuous derivative and integer-birth jumps of
  the canonical discrepancy norm. Both contain indefinite cross terms; after primitive centering the required
  same-sign completion is exactly the reverse-Markov gate already isolated in `R161_016`.
- `scripts/161_01_hyperbola_defect.py`: exact finite checks of the hyperbola coefficients and falsifier defects.
- `scripts/161_02_poisson_defect_probe.py`: diagnostic of the non-monotone raw Poisson-defect energy.
- `scripts/161_03_gamma_hankel_identity.py`: numerical falsifier for the moment/Hankel identity, its displacement
  derivative, and the normalization relating `R161_025` to `R161_026`.

Current verdict:

1. A genuinely joint additive–multiplicative operator identity was constructed.
2. The naive positive square is rigorously sign-blind: it contains the square of the truncated Weil operator.
3. Raw partial sums are the wrong approximation at the critical half-density; the corrected object is the explicit
   polar-renormalized Muntz operator.
4. The scalar Stieltjes completion and positive divisor-fibre lift are prior closed routes. Product regularisation
   instead constructs oriented Hardy ports and preserves their critical jets.
5. The scalar commutator identifies the orientations through cosine/reflection scattering. For parity sources the
   port therefore lies in a Sonin eigenspace; support separation alone does not kill it.
6. The canonical port excess is minus its endpoint-normalized norm slope. A direct Euler--Gamma Markov contraction
   gives only the already known decreasing-norm inequality. Closure requires a source-labelled Poisson/Fourier
   scattering which reverses the physical input/output typing. The global balance still uses infinitely many
   exterior prime powers; the finite `2,3,4` reduction applies only to the alternative zero-collar route.
7. The two-port cosine defect is exactly `zeta(s)W_epsilon^0`; its inverse restricts to the first-contact Tate
   forcing on the window. Thus physical scattering is not automatic from parity: if proved, it kills that forcing
   and leaves precisely the homogeneous zero-mode/range-intersection problem.
8. Comparing this defect with the linear `(PC-ren)` limit yields only the tautology
   `[zeta,D_Gamma]=0`. The separated exterior port cannot be made zero by a linear graph split; the remaining route
   must retain the reverse quadratic Markov defect before taking the completed limit.
9. Once physical scattering is available, the poles of `d_Gamma` at `s=3,5,7,...` force
   `K_F(5/2)=K_F(9/2)=...=0`; polynomial density after `x=e^(-2t)` gives `F=0` for every finite window. Therefore the
   only remaining terminal gate is deriving that scattering from the finite quadratic `(PC)` construction.
10. By unitary-compression rigidity it suffices to prove the right-exterior equation
    `P_+C_log g=sigma g`. Its obstruction is the positive leakage
    `||(I-P_+)C_log g||^2`; the next exact task is to obtain this square as the projected boundary-layer limit of the
    finite renormalized Poisson defect and show its first-contact value is zero.
11. It is enough to annihilate the single oriented correlation
    `X_T=||g||^2+epsilon<g,C_log g>=(1/2)||(I+epsilon C_log)g||^2`. In Mellin coordinates this is exactly
    `Re<G_+^0,zeta W_epsilon^0>`. The sharp remaining task is to realize this scalar as a finite `(PC-ren)`
    polarization `a_T(F,H_(M,N,T)F)`, which vanishes on the first-contact radical.
12. The canonical test is `H_F=Pi_T P_T Z*g`. Writing `w=(W_epsilon^0)^vee`, `d=w-AF`, and
    `y=Z*g`, one has `P_Td=0` and the exact decomposition
    `X_T=Re[<r,Tau_TP_Ty>+<ell_T(F),(I-P_T)y>+<d,y>]`. The crossed Tate match controls the first term; the last two
    define the precise exterior Green reciprocity still to be obtained from finite `(PC-ren)`.
13. The exact projection calculation gives
    `<r,(I-Pi_T)P_T(S_N^ren)*g_N>=<S_N^ren r,g_N>`. Together with the exterior Weil leakage this is merely the
    mixed `(PC-ren)` pairing; adding `d` reconstructs `X_T`. Hence the direct conjugate-test route is tautological.
    The surviving target L161.6 is an independent antisymmetric boundary concomitant before the two causal
    orientations are recombined.
14. Full or compressed scattering is sufficient but not necessary. Holomorphy of `W_epsilon^0` merely at the
    positive odd Gamma poles already forces all moments `K_F(2m+1/2)` to vanish and hence `F=0`. The minimal target
    L161.7 is to derive those removable singularities directly from the two-orientation finite `(PC-ren)` germs in
    `Re s>1`.
15. The residue is exactly `zeta(2m+1)K_F(2m+1/2)`. Linear finite holomorphy cannot kill it: Laurent-coefficient
    convergence is already the missing theorem, and the linear graph limit is tautological by `R161_018`. The
    normalized weighted sum of the residue squares defines a finite faithful energy `D_T^pole`; L161.8 asks for its
    noncircular finite `(PC-ren)` realization and equality-state vanishing.
16. The pole energy is a literal Gamma-Hankel boundary derivative. For every `delta>0`,
    `D_(T,delta)^Gamma=-(1/2)partial_delta B_(T,delta)^Gamma`, with kernel
    `-(c_Gamma-e^(-v/2))'(2T+2delta+t+u)`. It is a bounded faithful square. L161.9 asks `(PC-ren)` to prove the
    reverse displacement sign at first contact; the direct sign is automatic.
17. Equivalently, this is the Gamma interaction with a reflected copy of `F` across a gap `2delta`; its derivative
    is a strictly positive force. Individual prime-power image forces are signed autocorrelation derivatives, so
    `Lambda>=0` is insufficient. L161.10 asks the joint `Lambda*1=log` plus Poisson identity to turn the combined
    prime force into a second nonnegative boundary square with the same sign.
18. The image is intrinsic to `(PC-ren)`: with `a=log N=2(T+delta)`, one has
    `partial_a C_aF=epsilon e^(a/2)M_(T,delta)F`, and `supp C_aF` is exactly the exterior image interval. Between
    integer births the discrepancy velocity is `-e^(a/2)tau_a`; at a birth its jump is
    `n^(-1/2)tau_(log n)`. L161.11 asks the differentiated-and-jumped finite `(PC-ren)` pairing to complete these
    into the same-sign Poisson square.
19. The ordinary moving norm does not supply that square:
    `partial_a||Z_af||^2=-2e^(a/2)Re<Z_af,tau_af>`, and every integer birth has an equally indefinite cross term.
    Primitive projection merely rewrites radicality. Hence L161.11 and the reverse Tate-centred Markov pullback are
    the same terminal sign theorem, now with the Gamma component explicitly identified.
20. The missing algebraic completion is a two-level variance taken before scalar synthesis. On each product fibre
    `de=k`, retain both Poisson/Fourier orientations and only then average with `Lambda(d)/log k`. The resulting
    identity is the sum of an orientation square and a divisor-seam square. Unlike the old divisor variance, its
    orientation term survives on prime fibres, so the phase-121 root-diagonal obstruction is removed. The terminal
    source match is to realize its saturated left side from finite crossed-Tate `(PC-ren)`.
21. The pathwise vectors are canonical. For every `de=k`, the two product orientations are
    `k^(-1/2)Jtau_(log k)f` and `k^(-1/2)tau_(log k)Fcal f`; they are independent of `d`. Hence the divisor seam
    vanishes exactly and the gate leaves the direct-sum Poisson square
    `(1/4)sum_(k<=N)(log k)^2/k||tau_(log k)Fcal f-Jtau_(log k)f||^2`. As corrected in item 23, realizing this
    labelled diagonal from the coherent source norm remains part of the unsolved source match.
22. The crossed Tate block has the required sign after parity is imposed. If `C` exchanges the two Tate characters
    and the forcing vector satisfies `Cv=epsilon v`, then
    `epsilon<v,G_TCv>=<v,G_Tv>=||r||^2`. Thus the endpoint term is not an indefinite remainder on the relevant
    branch; with the same `epsilon` as the scattering square it is a positive Tate energy. The remaining theorem is
    the finite Green bookkeeping identity assembling this term with the Poisson and Gamma squares.
23. A noncircularity audit finds a missing Gram step: `(PC-ren)` contains the coherent sum over `k`, whereas the
    oriented variance uses a direct-sum second moment. Source labels alone do not delete cross-`k` interference.
    Closure therefore requires either an explicit Parseval/Naimark dilation or an exact Green identity in which the
    polar/Gamma and parity-Tate boundary terms compensate the cross Gram. The parity sign lemma remains valid, but
    occurrence of its concomitant with that sign is still to be derived.
24. Mellin diagonalization shows that the missing cross Gram is exactly the phase-106 product--ratio split:
    equal orientations depend on `k/l`, opposite orientations on `kl`. Therefore it cannot be cancelled in the
    translation-invariant full-line algebra by a rank-two Tate term. The surviving new object is the coherent
    compressed leakage `||(I-P_T)sum_k(log k)d_kP_TF||^2`, whose expansion retains the full ratio/product Gram but
    localizes it to the boundary. Its polar-renormalized identification with scattering leakage is the terminal
    target.
25. The direct-sum lift is unnecessary. The proof of `(PC-ren)` already gives two global coherent orientations
    `U_N=K_N^ren Fcal`, `V_N=JK_N^ren`, and the exact source mean
    `U_N+V_N=S_N^ren M Fcal-{X,E_N^ren}`. Their physical-space parallelogram is
    `(1/4)||(U_N-V_N)f||^2>=0` and retains the complete product/ratio Gram. The terminal gate is the polar/Tate
    first-contact saturation of this two-state second-moment equality.
26. Mellin differentiation identifies the coherent difference with the completed zeta jet. If
    `e_N=Z_N(s)u(s)-Z_N(1-s)`, then
    `U_N+V_N=-e_N'+Z_Nu'` and `U_N-V_N=-Z_N'u+Z_N'(1-s)`. Under differentiated graph convergence the latter tends
    to `-2zeta'u-zeta u'`, hence at a simple critical zero it is `-2zeta'(rho)u(rho)`. Saturation therefore kills
    the faithful critical conormal observation directly.
27. Strong differentiated graph convergence is not needed. If coherent saturation gives
    `||(U_N^ren-V_N^ren)F||_2->0`, Plancherel supplies an a.e.-zero subsequence, while pointwise differentiated
    Euler--Maclaurin fixes its limit as `(-2zeta'u-zeta u')Fhat`. This meromorphic multiplier is nonzero almost
    everywhere, so `F=0`. The polar/crossed-Tate saturation is therefore the sole remaining gate.
28. Saturation is not a formal consequence of `(PC)` plus radicality. An exact `2x2` model satisfies all algebraic
    identities, has `A=0`, includes both parity lines, but has `D^coh(f)=||f||^2`. Therefore the remaining step must
    use genuine physical compression, the additive-Fourier kernel, and polar/Tate collar geometry; another formal
    rearrangement of the linear anomaly cannot prove it.
29. The terminal ledger identifies coherent saturation as the missing uniqueness theorem itself. The same blocker
    has persisted through scattering leakage, reverse Gamma displacement, divisor variance and coherent variance.
    A continuation requires a genuinely new compressed Green identity whose expansion produces the polar layer and
    the oriented Tate term; no such identity is present in the corpus.
30. On retry, the physical property absent from the formal countermodel is identified: for
    `Z_N=S_N^ren`, Poisson gives `Z_NFcal=Z_N*J+E_N^ren`. Hence on a parity source
    `(I-P)Z_NFcal f-epsilon(I-P)Z_N*f=(I-P)E_N^renf`. This is the exact annular transport between the two causal
    histories that phase 121 could not derive from Real symmetry. Differentiating its positive exterior norm is the
    new concrete route to the coherent jet plus Gamma/polar/Tate energies.
31. Orientation audit corrects that last derivative: the Poisson difference
    `E_N=Z_NFcal-JZ_N` differentiates covariantly to `U_N+V_N`, while the desired jet `U_N-V_N` is the derivative
    of the complementary sum `C_N=Z_NFcal+JZ_N`:
    `U_N-V_N=Z_NM Fcal-{X,C_N}`. Hence the next object must be a mixed compressed `E_N`--`C_N` Green pairing;
    differentiating `||E_N||^2` alone has the wrong orientation.
32. The mixed pairing has an exact Green cancellation. For `a=Z_NFcal f`, `d=JZ_Nf`,
    `Re<a-d,X(a+d)>=<a,Xa>-<d,Xd>`. After right/left exterior compression this becomes the sum of two positive
    distance-to-boundary moments, the two-sided Sonin--Gamma excess. The remaining half of `{X,C_N}` is `C_NXf`;
    decomposing `PXf` into primitive and Tate parts localizes the unresolved concomitant to the crossed Tate block.
33. In that source-derivative ordering the Tate block actually vanishes by parity. Since `JX=-XJ`, a parity
    `epsilon` source has `Tau_TPXf` in parity `-epsilon`, while the forcing vector and collar current have parity
    `epsilon`. Their pairings are zero. The same-parity positive Tate identity remains valid elsewhere but cannot
    be inserted into this term. The live remainder is therefore primitive plus exterior, not a Tate sign problem.
34. The primitive `Xf` component is the derivative at zero of the Tate-corrected horizontal modulation family and
    is therefore the phase-121 radicality tautology. Moving the finite synthesis so as to identify the mixed term
    with that primitive pairing creates the exterior Hankel commutator. Hence all genuinely new content has again
    been reduced to the antisymmetric exterior reciprocity of `R161_023(5.3)`; its scalar consequence
    `Re<g,P_+C_log g+epsilon g>=0` is sufficient for exact scattering.
35. Brown--Halmos gives the desired rank-one positive self-commutator for every local Euler factor, but phase 122
    proves that globalizing it requires a metrized Euler--Gamma determinant anomaly/trivialization. Poisson
    identifies the undifferentiated histories; differentiating that relation has the wrong orientation for the
    critical jet. Hence the local Hankel square does not prove the remaining antisymmetric exterior reciprocity.
# Backward audit update

[R161_061](R161_061_POISSON_TATE_LAGRANGIAN_BOUNDARY_IDENTITY.md) proposes a new source identity: the crossed Tate matrix is treated as a symmetric boundary response, whose graph is Lagrangian for the Green form. The target is to lift PC-ren to an isotropic graph in the full Poisson--Tate boundary carrier; its canonical conjugate pairing would be the extremal scattering correlation.

[R161_062](R161_062_HERMITIAN_BOUNDARY_POWER_IDENTITY.md) corrects that proposal: an alternating Green form has identically zero diagonal and cannot yield the quadratic scattering gate. The relevant object is the complementary Hermitian boundary-power form. It proves the exact compressed anticommutator identity, retains rather than cancels the crossed Tate power, and formulates the finite Poisson--Tate power balance whose `E/C`-oriented graph limit is the required extremal correlation.

[R161_063](R161_063_NESTED_COMPRESSION_POWER_DECOMPOSITION.md) performs the exact nested `Pi_T + Tate + exterior` expansion and then audits its typing. The diagonal anticommutator identity is valid, but its Tate block contains `RZ_Nf`, whereas the proved crossed collar is `Tau_TP_TZ_N^*g(f)`. The attempted diagonal identification is therefore withdrawn. With the correctly typed mixed pair one recovers exactly the already known canonical-pullback decomposition, so a new vanishing still has to act on the complete mixed exterior power.

[R161_064](R161_064_MIXED_POWER_TYPING_AND_SUPPORT_CONCOMITANT.md) introduces the finite support concomitant made of the off-diagonal compression blocks and audits the collar typing. Its suggested positive `E_N/C_N` expansion is retained there only as an open candidate and is subsequently withdrawn by R161_065.

[R161_065](R161_065_SUPPORT_CONCOMITANT_COLLISION_AND_FINAL_AUDIT.md) proves that the R161_064 candidate is exactly `<g,[P_T,Z_N]w>`, hence the support commutator already audited in R161_042--R161_044 and R161_057. Its proposed positive expansion is withdrawn: the primitive term is tautological, the derivative Tate term has opposite parity, and literal PC-ren substitution reconstructs rather than annihilates the exterior correlation. This exhausts the R161_061--R161_064 Lagrangian/Hermitian variants without closing D.

[R161_066](R161_066_NEW_ARITHMETIC_INPUT_SELECTION.md) restarts the construction at the genuinely missing arithmetic level. It selects the positive-odd Gamma Laurent coefficient as the smallest target, realizes the faithful pole energy as a weighted sum of separated contour observations, and formulates the noncircular finite oriented-annihilation law OAL that must be constructed before the two PC orientations recombine.

[R161_067](R161_067_ORIENTED_LAURENT_DICHOTOMY.md) audits OAL and withdraws it as an annihilation mechanism. A finite germ without the Gamma factor has zero residue but cannot converge across the pole without already proving the desired moment vanishing; with the Gamma factor its residue is exactly the target moment at every finite stage. A genuinely new input must therefore be a quadratic comparison law with the Gamma-pole energy as a computed remainder, not another linear contour limit.

[R161_068](R161_068_GAMMA_EULER_OBSERVABILITY_IDENTITY.md) constructs a new faithful quadratic arithmetic observable: the positive-odd Gamma observation diagonalizes every additive translation, and the von Mangoldt generator acts there by the strictly positive scalars `-zeta'(2m+1)/zeta(2m+1)`. Its naive radical pullback is then rejected: radicality inserts `A_infinity` into the observed vector, and removing it would require a circular inverse. A closure would require a new division-free factorization of the observation through the compressed first-contact operator.

[R161_069](R161_069_FAITHFUL_OBSERVATION_FACTORING_NO_GO.md) proves that such a formal factorization already has the full force of injectivity: a faithful positive observation `C=AK` vanishes on `ker A` and therefore kills the kernel. Thus the Gamma--Euler detector is genuinely arithmetic but does not supply its own equality-state annihilation law.

[R161_060](R161_060_LITERAL_PC_SUBSTITUTION_IN_THE_DOUBLE_COMMUTATOR.md) completes the literal substitution of PC-ren into the positive radical double commutator. After the primitive and Tate reductions it reconstructs the same exterior extremal correlation; it supplies no additional zero or sign.

[R161_059](R161_059_COMPRESSED_COMMUTATOR_EXACT_BLOCK_FORM.md) expands the compression of a globally commuting pair: `[PAP,PZP]=Ybar*X-X*Y`. Radicality, reflection and Tate correction leave these crossed exterior products; they do not turn the double commutator into a negative square.

[R161_058](R161_058_DOUBLE_COMMUTATOR_POSITIVITY_AND_RECIPROCITY_TEST.md) identifies the remaining quadratic reciprocity with a positive radical double commutator. Reflection makes the two causal energies equal, not zero. Closure requires PC-ren to supply a genuine negative Gamma/polar balance for this positive quantity.

[R161_057](R161_057_FOUR_BLOCK_MIXED_GREEN_IDENTITY.md) expands the mixed Green identity into the correctly oriented exterior energy, the wrong-side exterior energy, the norm flux and the interior first-moment flux. After the known primitive and Tate reductions, the only remaining term is the quadratic reciprocity between the wrong-side energy and the two one-sided integer-minus-continuum discrepancies.

[R161_056](R161_056_UNITARY_PHASE_HAS_THE_WRONG_TANGENT.md) corrects the colligation route: the unimodular quotient is valid, but its logarithmic derivative observes the Poisson difference and hence `U_N+V_N`. The closing jet `U_N-V_N` differentiates the complementary sum and is not a unitary phase tangent.

[R161_055](R161_055_DIAGONAL_GRAPH_CENTRAL_METRIC_EQUALITY.md) proves, by a compatible smooth/cutoff diagonal in the common graph, that the two undifferentiated Poisson histories have equal central metrics in the limit. The equality is stable under the canonical finite-rank polar/Tate correction. The differentiated boundary-layer metric remains open.

[R161_054](R161_054_TWO_CAUSAL_ORIENTATIONS_SQUEEZE_LEMMA.md) proves the conservative three-block flux identity and the abstract two-orientation squeeze. Poisson identifies the histories and PC identifies their tangent; closure now requires the finite central metric equality after the canonical crossed Tate correction and the common-port graph limit.

[R161_053](R161_053_CANONICAL_SOURCE_LIFT_AND_COVARIANT_TANGENT.md) fixes the finite colligation vector from the two actual Poisson histories. Covariant differentiation cancels source motion and retains exactly the two Chebyshev orientations plus the Gamma connection. The remaining equality is the compressed PC-Gamma-Tate quadratic balance.

[R161_052](R161_052_FINITE_UNIMODULAR_POISSON_COLLIGATION.md) constructs the finite unitary colligation hidden in the two renormalized Poisson orientations. Its Toeplitz defect is an exact exterior leakage square, while its division-free phase derivative combines the coherent Chebyshev orientations and the Gamma connection. First-contact extremality with the crossed Tate endpoint remains to be derived.

[R161_051](R161_051_TERMINAL_EQUIVALENCE_AFTER_THREE_BLOCK_AUDIT.md) records that every surviving arithmetic gate has the full force of excluding first contact and hence of D itself. The current corpus proves all downstream implications but not the equality-state arithmetic transfer.

[R161_050](R161_050_THREE_BLOCK_UNITARY_COUNTERMODEL_AND_REQUIRED_ARITHMETIC_INPUT.md) gives an exact three-dimensional unitary countermodel: central cancellation, scattering parity and unitarity do not imply the right compressed gate. Any closure must use the arithmetic product-range, Gamma-pole, Euler-ideal or PC boundary data load-bearingly.

[R161_049](R161_049_THREE_BLOCK_SCATTERING_AUDIT.md) separates the central compression already killed by the completed incoming theorem from the right-exterior compression required by unitary rigidity. It records the exact three-block norm identities and isolates the remaining arithmetic transfer.

[R161_048](R161_048_INTERIOR_CUTOFF_STABILIZATION_AND_RETRY_LEDGER.md) proves exact stabilization of the interior synthesis above the window cutoff, including the continuum subtraction. The exterior Fourier block remains unresolved; the resumed closure attempt has not proved D.

The fixed-pole calculation and exact translated collar are in [R161_047](R161_047_FIXED_POLE_COMPRESSION_AND_EXACT_COLLAR.md). The residue belongs to the exterior remainder; restricting the first-contact equation to the window does not annihilate it.

See [R161_046](R161_046_BACKWARD_CHAIN_AND_FINITE_RADICAL_DETECTION.md): the abstract countermodel does not establish independence from the full physical hypotheses. At each fixed first-contact window, finitely many Gamma-pole moments detect the finite-dimensional radical. Their annihilation from finite PC data remains to be proved.

[R161_070](R161_070_TYPED_FINITE_GAMMA_EULER_COLLAR.md) corrects the observation-domain and global/compressed-kernel errors in R161_068–069. It constructs the bounded detector R*D_N R and its exact finite collar identity, with trace-norm convergence and an explicit inactive-prime remainder. The primitive Weil comparison remains open; the earlier global factorization argument does not establish a no-go for it.

[R161_071](R161_071_PARITY_TEST_AND_EXACT_GAMMA_EULER_BALANCE.md) constructs the finite primitive test Pi(G_L+JG_LJ)f and obtains an exact equality-state balance 0=2c_(N,L)+Q_(N,L). The remainder explicitly includes the backward Euler moments, forward collar, Gamma form and Tate forcing. Its required sign remains unproved; the balance does not yet close D.

[R161_072](R161_072_BALANCE_RECOMBINATION_AND_COEFFICIENT_TEST.md) expands that remainder back to the original window equation. It also proves that the detector/collar construction works for arbitrary nonnegative coefficients, even a single shift. Thus neither detector faithfulness nor this test exploits the divisor relation in a way that forces annihilation. Inactive-tail increments change Q by exactly minus twice the detector increment. No new equality-state sign is obtained.

[R161_073](R161_073_STABILIZED_MOMENT_INVERSE.md) constructs the legitimate stabilized inverse S^(-1), S=H_T+R*R, for a finite Gamma observation detecting ker H_T. It proves an exact square identity for I-RS^(-1)R* and an isomorphism of its kernel with the first-contact kernel. A strict arithmetic estimate for this finite matrix, including control of the full inverse, remains open.

[R161_074](R161_074_RESIDUAL_UPPER_CERTIFICATE.md) proves M=M_0+E*S^(-1)E for approximate stabilized solves and the upper certificate M<=M_0+alpha^(-1)E*E. An exact two-dimensional example shows why a strict Galerkin margin alone can miss a real zero mode. Quantitative arithmetic coercivity and full residual bounds remain unproved.

[R161_075](R161_075_MULTIPLIER_DOMAIN_AUDIT.md) audits the blanket linear-limit exclusion in R161_018. Injective L2 zeta multiplication, distributional zero-supported data and the meromorphically zero Gamma–Euler symbol have different meanings. The identification of the physical Weil limit with the zero commutator is unproved as written; a compatible carrier and graph-limit theorem remain to be constructed.

[R161_076](R161_076_LOCAL_WEIL_LIMIT_AND_POISSON_DOMAIN.md) constructs A_loc f by exact local stabilization and proves global exponentially weighted convergence for compact smooth f. It gives the moving cutoff M>=N exp(K+T) for raw Poisson composition and shows why this topology does not control the continuum left tail. The combined renormalized product requires a separate tail-cancellation estimate.

[R161_077](R161_077_CONTINUUM_MODULO_TATE.md) computes the finite arithmetic continuum via the compact primitive cumulative J_f. It proves that changing the lower integration anchor adds only a Tate vector, so the primitive projected continuum action and the fixed-N projected Weil–Poisson limit are well-defined on compact smooth sources. Uniform N control and the full exterior representative remain open.

[R161_078](R161_078_SMOOTH_RENORMALIZED_TAIL_CONVERGENCE.md) uses a stated unconditional PNT remainder to prove locally uniform N convergence of the anchored sum-minus-continuum action on A_loc f for compact smooth primitive f. The derivative-dependent estimates do not yet extend to first-contact radicals, and the value of the limit is not shown to vanish.

[R161_079](R161_079_WEAK_RENORMALIZATION_ON_PRIMITIVE_L2.md) extends this renormalization to compact primitive L2 sources in the distribution topology by transferring derivatives to compact tests. It constructs the continuum modulo Tate via a distributional primitive and gives a source-L2 tail bound with test seminorms. This admits first-contact vectors to the weak construction, but does not preserve radicality under smoothing, supply Hilbert graph transport, or annihilate the exterior remainder.

[R161_080](R161_080_POLE_ESCAPE_AND_TWO_SCALE_OBSERVATION.md) tests the new limit against Gamma-residue extraction. An explicit escaping exterior tail retains its residue while tending to zero even in every fixed Sobolev norm. It gives exact noncommuting Abel limits, the two spatial scales required to detect the escaping coefficient, and a conditional extraction estimate with its weighted remainder hypothesis exposed. The weak-limit construction alone cannot annihilate the residue.

[R161_081](R161_081_SIGN_TEST_ON_WEIL_EIGENVECTORS.md) tests the proposed direct sign proof. With a canonical Tate forcing away from the kernel, the exact remainder on a parity eigenvector Hf=lambda f is Q=-2 sum_m(d_(m,N)+lambda)|(R_L f)_m|^2. Hence Q cannot have a nonnegative-square representation valid throughout the primitive space, even when H is nonnegative. A radical-specific arithmetic proof or a genuinely different comparison is still required.
