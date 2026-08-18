# 114.a.10 — Completion audit of row (a): unified metrized closure in a144

```
+--------------------------------------------------------------------------+
| a1  DIV/PRIN     CLOSED on the valued supportwise Haran square.            |
| a2  PRIN-INVAR   CLOSED: determinant pairings live on metrized Pic_A.      |
| a3  CURVE DIM    CLOSED by the fixed-rank ruling restrictions.             |
| a4  QUADRATIC    CLOSED: normalized bounded-section determinants.          |
| a5  GRADED PAIR  CLOSED: RR = contact tensor Green on the same kernels.    |
|                                                                          |
| VERDICT          a144 constructs one metrized bivariant object satisfying |
|                  a1--a5. ROW A IS CLOSED; this is not an RH claim.        |
+--------------------------------------------------------------------------+
```

## 1. Authoritative requirements

The row-(a) contract is the table in `113_15_THE_FOUR_ROW_LEDGER.md`:

| item | requirement |
|---|---|
| a1 | a divisor group `Div` and principal subgroup `Prin'` |
| a2 | `Prin'`-invariance of the pairing |
| a3 | curve-like absolute dimension `Theta(deg D)` in fixed rank |
| a4 | a product structure with quadratic dimension growth |
| a5 | a working pairing on the graded side |

Completion means that one compatible construction satisfies all five.  It is
not enough to source a1, a4 and a5 from unrelated objects.

## 2. Evidence audit item by item

### a1 — divisor/principal structure

The phase-108 graded candidate supplies a formal divisor group and a principal
subgroup. Haran 2017 §11 separately supplies completed bundles, section
sheaves and rank-one isomorphism classes for general pro-objects. `a_63`
corrects `a_12`: projection pullback of completed bundles is not automatic,
because their trivializers live in a regular-denominator fraction sheaf.
The external Picard map and its kernel reduction are conditional on
H7-PB-REG; for prime bundles this is H7-PRIME-REG.

What is missing is the anti-diagonal injectivity, an identification with the
analytic construction, and a computation of the full `Pic` and `Prin`.
Therefore:

```
a1 as an isolated analytic item: HAVE.
a1 inside the desired unified square: OPEN.
```

### a2 — principal invariance

The old graded pairing fails principal invariance by `108_38` Theorem 3.1.
`114_a_09` explains why the cyclotomic workaround cannot repair this:

```
Z_3-Z_6=div(Phi_3/Phi_6)
```

is principal, so a global Picard pairing must give equal intersections of
`Z_3` and `Z_6` with `Delta`; their raw finite resultants are `log 3` and `0`.

The toric adelic intersection of `114_a_07` is principal-invariant, but the
product formula completes/cancels those local resultant contributions.  Thus
it does not supply the requested Lambda pairing.

```
a2 for raw resultant/Lambda values as a global Picard pairing: IMPOSSIBLE on P1.
a2 for the completed toric global pairing: HAVE, but Lambda is lost.
a2 on nonprincipal cycles of Haran's square: OPEN.
```

### a3 — fixed-rank absolute dimension

The fixed-rank Connes--Consani result remains available.  `114_a_01` correctly
separates it from a4: holding rank fixed gives linear growth and says nothing
about the coupled rank/radius surface regime.

```
a3: HAVE, non-load-bearing for a4-strong.
```

### a4 — quadratic product

The chain `114_a_02`, corrected by `114_a_06` and completed by `114_a_07`, now
establishes in one standard category:

1. `P^1_Z` is a genuine arithmetic surface;
2. the canonical semipositive toric metric on `O(1)` has Haar Chern measure;
3. the Haar `L2` section lattice is exactly `Z^{k+1}` with norm scaled by
   `e^{-a}`;
4. its roof function is constant `a` on `[0,k]`;
5. its arithmetic self-intersection is `2ka` and its mixed form is
   `ka'+k'a`;
6. its theta invariant is `ka+a` plus the explicit Jacobi remainder.

This is stronger than the original a4-weak claim because the pairing is now
derived rather than stipulated.

It is not the literal square.  Haran's square exists, and 2017 §11 gives a
bundle/section formalism, but neither the read 2017 source nor Haran's later
arXiv:2209.08536 and arXiv:2402.04456 supplies/computes a two-directional
degree, a proper section gauge, an intersection product or Riemann--Roch on
that square.

```
a4-weak: CLOSED POSITIVELY and strengthened.
a4-strong: OPEN at Haran G-7.
```

### a5 — graded pairing

The phase-108 no-go results remain binding.  The toric rank-two form is a valid
pairing on its own divisor family, but `114_a_05` proves that no form on that
quotient can reproduce the cyclotomic Lambda data, and `114_a_09` proves why
principal invariance prevents doing so globally on `P^1`.

```
a5 in the original graded route: CLOSED NEGATIVELY.
a5 on a future Haran/nonprincipal cycle theory: OPEN.
```

## 3. Numbered gaps after the audit

| gap | rigorous status | evidence |
|---|---|---|
| I7 algebraic kernel lattice | CLOSED POSITIVELY | `a_05` Thm 1.1 |
| I7 descent to `(r,m)` | CLOSED NEGATIVELY | `a_05` Thm 2.1 |
| I7 positive weight-one kernel gauge | CLOSED NEGATIVELY | `a_09` Thm 2.1 |
| I7 global principal pairing retaining raw resultants | CLOSED NEGATIVELY on `P1` | `a_09` Thm 3.1 |
| I7 geometric prime-incidence carriers on Haran square | CLOSED POSITIVELY | `a_17`: `Delta cap V_p = Spec F_p`, local mass `log p` |
| I7 nonprincipal prime Picard lifts | ABSTRACT CLOSED / COMPLETED REGULAR ROUTE FALSE AT 2 | `a_66`: unit-torsor pullback exists and diagonal detects nontriviality. `a_108` proves the image of `2` is a zero divisor on the square, so the Section-11 completed regular-denominator lift cannot include `L_2` by this route |
| I7 Frobenius/correspondence algebra | CLOSED OPERATORIALLY AND AS DECORATED SPANS / UNDECORATED OPEN | `a_36`: faithful Witt operators. `a_70`: diagonal spans decorated by `T_n` compose as `Gamma_m Gamma_n=Gamma_mn` and have monoidal contact `P_n`; forgetting decoration collapses every carrier to `Delta` |
| I7 exact Lambda diagonal mass | CLOSED OPERATORIALLY | `a_36`: `log|tr(lambda_1(V_n phi_1))|=log|Phi_n(1)|=Lambda(n)`; equality with geometric intersection is H7-I7-REAL |
| I7 literal Witt Frobenius graphs | CLOSED ON WITT PRO-SCHEME | `a_37`: every `F_m` preserves `W_N`, and its graphs compose as `G_m o G_n=G_mn` compatibly in `N` |
| I7 Witt graph space as arithmetic surface | CLOSED NEGATIVELY | `a_37`: `W_N` and `W_N tensor_Z W_N` are finite over `Z`, hence dimension one; H7-WBASE/H7-WLEF must transport to Haran's two-ruling square |
| I7 ordinary scalar transport Witt -> Haran | CLOSED NEGATIVELY | `a_38`: the two unital `Z -> W_N` maps coincide, so `Z tensor_F Z -> G(W_N)` factors through the fold and lands on the diagonal |
| H7 twisted-field scalar/bio targets | CLOSED POSITIVELY | `a_39` gives the two field laws; `a_40` constructs the universal involutive bio; `a_49` proves its unary real monoid embeds |
| H7 unary embedding H7-UEMB | CLOSED POSITIVELY FOR ALL `u>0` | `a_49`: simultaneous homogeneous regular representations into `B x B^op`; evaluation at `1` separates scalars |
| I7 ordinary Witt graph/diagonal intersection | CLOSED NEGATIVELY | `a_41`: on `W_{p^a}`, the fixed ring of `F_p` is exactly `Z`; the intersection has horizontal excess, not finite degree `log p` |
| I7 reduced Witt Lefschetz formula | OPEN, EXACTLY DELIMITED | `a_41`: H7-WLEF-red must remove the common `F_0` direction by a derived/excess complex and recover `Lambda` from its determinant |
| I7 standard reduced fixed cone | CLOSED NEGATIVELY | `a_42`: after quotienting `Z phi_1`, `F_p` is nilpotent and `det(1-F_p)=1`; the standard cone has degree zero |
| I7 cyclotomic excess determinant | OPEN WITH FORCED TARGET | `a_42`: the required determinant is `Norm(1-zeta_n)=Phi_n(1)`, so H7-WLEF-cyc must geometrize the primitive cyclotomic conormal factor |
| I7 prime Witt node intersection | CLOSED POSITIVELY | `a_43`: `W_p ~= Z x_{F_p} Z`; its `F_0` and trace branches meet in `Spec F_p` with degree `log p=Lambda(p)` |
| I7 local Witt-node/Haran-incidence comparison | DATA MATCH CLOSED, FUNCTOR OPEN | `a_43`: the Witt node and `Delta cap V_p` of `a_17` have identical residue diagram/mass; H7-WNODE asks for compatible transport and composition |
| I7 prime-power contact mass | CLOSED LOCALLY | `a_44`: adjacent Witt characters meet in `Spec Z/p^k`; the primitive layer `p^{k-1}Z/p^k` is `F_p` with degree `Lambda(p^k)=log p` |
| I7 prime-power/multi-prime composition transport | OPEN | `a_44`: H7-WNODE-COMP must transport primitive layers under `V_{p^k}=V_p^k` and prove cancellation when `n` has multiple primes |
| I7 global primitive contact system | CLOSED ALGEBRAICALLY | `a_45`: `P_n=tensor_{p^k||n} F_p` has `log #P_n=Lambda(n)` and canonical `P_m tensor P_n ~= P_mn`; multi-prime cancellation is literal tensor zero |
| I7 contact sheaves on Haran square | CLOSED POSITIVELY | `a_46`: `M_p=(i_p)_*F_p` and `M_n=tensor_{p|n}M_p` satisfy `M_m tensor M_n ~= M_mn` and `log #Gamma(Y,M_n)=Lambda(n)` |
| I7 faithfulness of contact sheaves | CLOSED NEGATIVELY | `a_47`: `M_{p^a}=M_{p^b}` and every multi-prime label has zero shadow; the cycles must retain information erased by `LDelta^*` |
| I7 composition of prime rulings as spans | CLOSED NEGATIVELY | `a_48`: for `p!=q`, mixed composition either vanishes (not faithful) or remembers the left endpoint (`R_p R_q != R_q R_p`) |
| I7 arithmetic-site Frobenius model | CLOSED IN ITS OWN TOPOS, NO BRIDGE | `a_48`: Connes--Consani `Psi(m)Psi(n)=Psi(mn)` exactly for integers, but no functor/intersection map to Haran's square is supplied |
| I7 undecorated lift from contact sheaves to cycles | OPEN, EXACTLY DELIMITED | H7-CYCLE-LIFT must construct distinct undecorated cycles `Gamma_n`, their composition and `LDelta^*Gamma_n ~= M_n`; `a_70` closes the decorated-span replacement |
| I7 faithful Picard label lift | CLOSED IN `Pic_tor` / COMPLETED REGULAR ROUTE FALSE AT 2 | `a_61`/`a_66`: `T_n` exists as a unit torsor, is faithful and monoidal. `a_108`: the required regular denominator `2` is a zero divisor, so the conditional completed-lattice promotion fails |
| I7 principal Cartier-act diagonal contact | CLOSED CONDITIONAL ON PRIME-REG | `a_67`: `V_p=D_Y(p)`, `pO_Y` is an invertible principal right act, and its ordinary diagonal layers are `F_p`; no global conormal Ab-module/`Tor` is claimed |
| I7 global derived conormal/contact | CONTACT RETRACT CLOSED / EXCESS OPEN | `a_68` constructs `L Omega_{O_Vp/O_Y}`; `a_69` uses `Delta^#p_1^#=id` to split `F_p[1]` canonically from its pulled complex. H7-LCI-DELTA is exactly vanishing of the complementary excess |
| I7 prime regularity on Haran tree charts | **CLOSED NEGATIVELY AT p=2** | `a_108`: `kappa=(1,-1)_1 o (1,1)_2^t` is nonzero, detected by the universal differential class `tau`, while a middle-wire swap gives `kappa=-kappa`; hence `2kappa=0` already in scalar arity. H7-PRIME-REG, H7-AUG-FLAT and 2-root-closure are false. Odd-prime regularity remains a separate optional question, not enough for the all-prime completed lattice |
| I7 universal regular repair | CLOSED SUPPORTWISE | `a_109` constructs `P^reg` on the dense finite-finite plane. `a_131` retracts the uniform real-chart construction; `a_132` repairs it by imposing only the finite-support scalars actually present and gluing on cofinal `(T,N)` tails, producing `Y^locreg` |
| I7 repaired prime Cartier subgroup and contact degree | CLOSED ON EVERY DISTINCT TWO-PRIME SUBGROUP | `a_111`: for `p!=q`, the actual regular Cartier-act data `V^reg_(p,1),V^reg_(q,2)` generate a free `Z^2` inside the completed Picard group; diagonal incidence gives the injective contact degree `m log p+n log q`. This is not yet a global bilinear intersection product |
| I7 all-prime Cartier presentation and partial intersection | POSSIBLE KERNEL EXACTLY ARCHIMEDEAN | `a_112` confines every relation to the anti-diagonal. `a_128` proves `p_2/p_1` cancels only finite valuations and fails as a real local-unit trivializer; `a_129` identifies the remaining kernel exactly with H7-ARCH-BDRY |
| I7 same-ruling prime intersections | CLOSED OFF THE DIAGONAL | `a_113`: quotient pushout plus Bézout gives `V_(p,i) x_Yreg V_(q,i)=empty` for `p!=q`, hence the forced intersection entry is zero. H7-REG-MIXDEG is reduced to opposite-ruling products and self-intersections |
| I7 opposite-ruling prime intersections | REDUCED BLOCK CLOSED / EXCESS OPEN | `a_114`: for equal primes the cross quotient has a split ordinary `F_p` retract; for distinct primes no nonzero finite scalar bio can have both characteristics. Tensoring the canonical contact retracts gives the bilinear reduced block `I_red(V_(p,1),V_(q,2))=delta_(p,q) log p`. Full generalized excess and self-intersections remain |
| I7 contact versus RR intersection | CLOSED NEGATIVELY AS AN IDENTIFICATION | `a_115`: the reduced value `delta_(p,q)log p` differs for every prime pair from the H7-RR0-forced value `(log p log q)/(2 log 3)`. A full theory must keep Lambda contact local and supply complementary excess/Green degree `(log p log q)/(2 log 3)-delta_(p,q)log p` |
| G-7 RR degree-product form and anti-diagonal | EXACT CRITERION / ARCHIMEDEAN GATE OPEN | `a_116` gives the exact descent criterion. `a_128` rejects finite principalization at the real ball, and `a_129` reduces faithfulness to independence of residual boundary classes H7-ARCH-BDRY |
| G-7 calibrated selective quotient | SATURATED BLOCK CLOSED; SUPERSEDED GLOBALLY BY `a_120` | `a_117` closes the original obstructing blocks. `a_120` replaces their special degree ratio by a generalized-Vandermonde construction on every positive effective ray. Sheaf exactness remains |
| G-7 denominator transitions | ACCUMULATED TARGET IMPOSSIBLE / DEGREEWISE BYPASS CLOSED | `a_57` forbids retaining old residue characteristics. `a_118` reevaluates both factors in the fresh block for `D+E`; `a_125` proves target transitions cannot be the exactness mechanism. Only sourcewise H7-FRESH-RESTR remains |
| G-7 characteristic-zero common moment bio | ALGEBRAIC DEN-TRANS CLOSED / FINITE DIMENSION OPEN | `a_119`: an ultraproduct of primes `p_j=2 mod M_j` has characteristic zero and every fixed odd power is bijective. One full bio target supports all rational denominators, odd moments and truncations. It is infinite; genuine-section Loeb/height dimension and exactness remain H7-PF-DIM |
| G-7 all-positive-ray calibrated interpolation | SHARP NUMERICAL RR COEFFICIENT CLOSED ON EVERY POSITIVE RAY | `a_120`: powers `1,3,9,...`, small integer nodes and a fresh prime avoiding the generalized Vandermonde give a bounded surjection onto `F_p^m` inside every `t(p_1^*A+p_2^*B)`. The canonical projection has exact dimension `t^2 deg(A)deg(B)/(2log3)+O(t)`. Restriction/cohomology exactness and geometric Green RR remain open |
| G-7 section/Picard descent | EXACTLY H7-ARCH-BDRY | `a_121` gives the equivalence with anti-faithfulness; `a_129` identifies that kernel with the residual mixed real-boundary kernel |
| G-7 reflected anti-diagonal route | FINITE PART CLOSED / ARCHIMEDEAN PART OPEN | `a_128`: `p_2/p_1` cancels finite valuations but its corrections are not units in the real ball. H7-RULING-PF is reduced to H7-ARCH-BDRY, not refuted |
| G-7 global numerical Green excess | FULL PRIME MATRIX CLOSED / BOUNDARY DESCENT OPEN | `a_123` determines `G_num=B_RR-C_Lambda`; `a_129` localizes its descent gate at H7-ARCH-BDRY. A sheaf-level realization is still open |
| G-7 metrized numerical Green gauge | CLOSED ON PRESENTATION / BOUNDARY DESCENT OPEN | `a_124` constructs the symmetric metrized biextension and gauge. Its geometric descent requires an independently constructed archimedean boundary degree plus Cartier/Deligne comparison |
| G-7 fresh exactness typing | TARGET-SHEAF VERSION CLOSED NEGATIVELY / SOURCE RESTRICTION OPEN | `a_125`: different fresh characteristics admit no unital target transitions, and Haran (11.7) gives right acts rather than abelian modules, so a target sheaf/long exact sequence is impossible or ill-typed. H7-FRESH-RESTR instead asks for one common reevaluation of each source restriction diagram and a direct fiber/cardinality theorem |
| G-7 fresh restriction | OPEN CLOSED / COMMON-TARGET CARTIER CLOSED NEGATIVELY | `a_126`: open localization and evaluation commute exactly. `a_127`: an inverse generic chart makes the Cartier prime a unit while its residue quotient kills it, so one nonzero unital target cannot evaluate both. The replacement is H7-TWO-TARGET-DELIGNE |
| G-7 canonical pre-Picard divisor target | SOURCE OBJECT CLOSED / BOUNDARY DEGREE OPEN | `a_129`: Haran's `D_1/Bun_1` and its global-fraction action give the exact principal/Picard sequence. The anti-class equals a finite principal part plus a residual archimedean boundary class; independence of those classes is H7-ARCH-BDRY |
| G-7 mixed archimedean boundary detector | OBJECTS/RESTRICTION FORMULAS CLOSED / PULLBACK FAITHFULNESS OPEN | `a_130`, corrected by `a_135`: define `B_i^locreg` levelwise using the rational-sphere residue point and supportwise inverse image. The prime anti-class restricts to `pi_2^*L_p^(-1)` and `pi_1^*L_p`; injectivity of either pullback implies H7-ARCH-BDRY. `a_136` rules out proving it by a base retraction |
| G-7 global reflection type audit | OLD UNIFORM VERSION CLOSED NEGATIVELY / REPAIRED | `a_131`: the real charts lack scalar `2`, so uniform `Reg_Z(A_alpha)` is undefined. `a_132` closes H7-LOCAL-REG-GLUE supportwise and restores the downstream finite-support statements on `Y^locreg` |
| G-7 supportwise local regular gluing | CLOSED POSITIVELY | `a_132`: index by finite prime supports `T` and levels `N` divisible by `prod T`; impose regularity only for actual local scalar sections. Those primes are units on every finite/real overlap, so relative reflections glue and form `Y^locreg`. Every finite-support prime lattice exists on a cofinal tail |
| I7 undecorated diagonal Chow cycles | CLOSED NEGATIVELY | `a_133`: if `Gamma_n=k(n)Delta`, convolution forces completely multiplicative `k`, while bilinear intersection gives `k(n)Delta^2`; this cannot equal `Lambda(p)=Lambda(p^2)` for all primes. The live undecorated route is H7-DYNAMIC-THICKENING or moving support |
| I7 torsor-to-derived-module route | EXACT FIVE-PART GATE / OPEN | `a_134`: Section 6 supplies an abelian module category, scalar extension and cotangent complexes, but not the asserted free rank-one `A^[1]`, torsor descent, tensor/convolution, faithfulness or contact comparison. These are isolated as H7-TOR-LIN; no derived kernel is claimed yet |
| I7 decorated dynamics versus unified geometry | DYNAMICS/CONTACT CLOSED; INTEGRATION OPEN | `a_139`: the authoritative a1--a5 contract does not mandate ordinary Chow representatives. `a_70` closes faithful decorated composition and monoidal `Lambda` contact. The live gate is H7-DYN-INTEGRATE: place those kernels in the same G-7 divisor/intersection theory and prove contact is geometric diagonal pullback |
| I7 contact-framed arithmetic kernels | DYNAMIC/DERIVED-CONTACT INTEGRATION CLOSED | `a_140`: combine each faithful torsor `T_n` with the canonical `H_1` cotangent retracts of `a_69` and the geometric contact sheaf `M_n`. These typed kernels compose under multiplication and have geometric reduced contact mass `Lambda(n)`. The remaining fifth integration clause is H7-FRAMED-RR |
| G-7 contact determinant line | CONTACT HALF OF TWO-TARGET DELIGNE CLOSED | `a_141`: the reduced `F_p` contact is represented by `[Z --p--> Z]`; its torsion determinant norm is `p^{-1}`. Virtual tensor powers/duals give a biexact line with logarithmic norm `C_Lambda`, isometric to `E_C` of `a_124`. The generic determinant line H7-RR-DET and boundary descent H7-RSPH-UNIT remain open |
| G-7 asymptotic RR determinant | CLOSED ON THE PRESENTATION | `a_142`: normalize the torsion determinant of the genuine calibrated image `F_(p_t)^(k_t)` by `t^(-2)`. The `O(t)` floor error becomes `O(1/t)`, and the metric limit polarizes exactly to `B_RR` |
| G-7 valued mixed-boundary Picard norm | CLOSED FOR METRIZED DESCENT | `a_143`: retain the Euclidean valuation before rational-sphere reduction. Isometric Cech frame changes have norm one, while `q_a=prod p^(a_p)` has norm `q_a`; unique factorization proves boundary faithfulness and survives supportwise reflection. Bare H7-RSPH-UNIT remains optional |
| Row-A unified object | CLOSED | `a_144`: the valued `Y^locreg`, actual metrized Div/Prin quotient, bounded-section RR determinant, torsion contact determinant, Green quotient and contact-framed `Gamma_n` form one bivariant object satisfying a1--a5 |
| G-7 real reduced point / mixed base change | TYPED POSITIVELY / CONSERVATIVITY OPEN | `a_135`: the real limit local object is `Q intersection Z_R`; its residue `kappa_infty` is the rational sphere object, neither `Z_R` nor full `F_R`. The mixed boundary is levelwise base change along `F{+-1}->kappa_infty` followed by supportwise inverse image. H7-RSPH-CONS is the exact remaining faithfulness theorem |
| G-7 rational-sphere base section | CLOSED NEGATIVELY | `a_136`: a retraction `kappa_infty->F{+-1}` would have to send `(3/5,4/5)` to a nonzero signed coordinate while preserving its zero residue contractions with both coordinate axes, impossible. Boundary faithfulness now requires genuine descent or a Picard norm |
| G-7 rational-sphere Cech units | EXACT EQUIVALENCE / UNIT NORMAL FORM OPEN | `a_138`: on the Haran two-chart cover, a prime word `q_a` dies after base change exactly when it belongs to the endpoint coboundary image `G_U G_V^(-1)` in the overlap. H7-RSPH-UNIT is the equality `Q_T intersect G_U G_V^(-1)={1}` plus invariance under supportwise reflection |
| I7 residual coefficient obstruction | OPEN, SHARPENED TO ANNIHILATION | `a_99`--`a_100` reduce nonextractable parity to outer coefficients after finite-set retractions. `a_101` closes every correctly oriented split coefficient and proves nonsplitness alone is insufficient; H7-COEFF-ANN must exhibit an ambiently separable pair killed by a genuinely nonsplit two-sided context, or be excluded |
| I7 scalar augmentation flatness | OPEN, EXACTLY EQUIVALENT TO SCALAR SATURATION | `a_102`: the first-ruling scalar ring splits additively as `Z direct-sum K`, `K=ker(nabla)`. Scalar `p`-regularity is `K[p]=Tor_1^Z(K,Z/p)=0`; all-prime regularity is exactly torsion-freeness/ordinary `Z`-flatness of `K`. The split fold alone is insufficient |
| I7 first tameness obstruction | **CLOSED NEGATIVELY: PLANE NONTAME** | `a_103` identifies the sandwich-blind mixed defect; `a_104` maps the full signed plane to Haran's commutative infinitesimal extension `F(Z) Pi N`, where centre minus grid has nine independent primitive-direction coordinates. Thus H7-XDEF-12 survives and H7-TAME-PLANE is false. This kills tame promotion but does not decide PRIME-REG |
| I7 explicit N-jet prime regularity | **CLOSED POSITIVELY / SUPERSEDED BY UNIVERSAL RATIONAL JET** | `a_105`: both ordered derivation maps land in `F(Z) Pi N`, prime-regular in every arity. `a_106` proves that Haran's omitted injectivity `C Omega -> N` is actually false, so these jets are not universal |
| I7 universal rational first jet | **CLOSED POSITIVELY / COMMON RATIONAL-JET KERNEL OPEN** | `a_106`: the exact entropy cocycle sends `[1,1|1]` to `-2e_2` but its image in `N` is zero. Rationalizing the universal module gives `H_Q=F(Z) Pi (C Omega tensor Q)`, prime-regular in every arity. Any source p-collision is invisible to both ordered universal rational jets. Integral torsion in `C Omega` and nonlinear/higher-order differences remain |
| I7 Picard-to-dynamic promotion | DECORATED VERSION CLOSED / UNDECORATED OPEN | `a_70` constructs the Picard-decorated span category and faithful diagonal kernels; `a_48` still forbids using prime rulings themselves as faithful commutative undecorated spans |
| I7 global nonprincipal intersection inducing local masses | OPEN | `a_17` constructs incidence, not an intersection product |
| G-0 toric metric/intersection realisation | CLOSED POSITIVELY | `a_07` |
| G-1 exact CC minimal-generator constant | CLOSED | `a_11`: positive-boundary entropy gives `1/log 2` |
| G-2 `l1` subleading asymptotic | CLOSED | `a_08` Thm 1.1, formula (2.1) |
| G-3 additive Lorentzian comparison | DELIMITED: RH-equivalent | `114_d3_03` Thm 6.5, proof repaired in `a_13` |
| G-3 pointwise non-additive domination | CLOSED AS VACUOUS | `a_13`: universal one-ray collapse |
| G-3 non-additive two-point polarization/Kunneth | DELIMITED: RH-equivalent | `a_59`: G3-POL creates a positive target two-plane without assuming additivity |
| G-3 effectivity-compatible non-additive realization | DELIMITED: RH-equivalent | `a_60`: target property (E) gives the forward implication; under RH the spatial-ray map gives the converse |
| G-7 external Picard sector | AXES CLOSED / ANTI-KERNEL REDUCED TO REAL BOUNDARY | `a_128` rules out the naive finite principalization; `a_129` proves the exact boundary-kernel formula. Rank two is equivalent to H7-ARCH-BDRY |
| G-7 discrete rank-two bigrade | CLOSED IN COMPLETED PICARD ON `Y^locreg` | `a_111` realizes every distinct-prime rank-two lattice by regular Cartier-act data and completed lattices; `a_112`, transported by `a_132`, extends this to arbitrary disjoint prime supports on cofinal tails |
| G-7 prime-axis sections and mixed grid | ABSTRACT CLOSED / BOUNDED COMPLETION OPEN | `a_20`: exact curve count and abstract `(m+1)(n+1)` grid; full completed bounded interpretation requires H7-PB-REG |
| G-7 diagonal-only quadratic growth | CLOSED NEGATIVELY | `a_20`: at most `2p^m q^n+1`, so log-size `O(m+n)` |
| G-7 generic off-diagonal entropy | CLOSED POSITIVELY | `a_21`: `2^N` distinct block defects in one fold fiber |
| G-7 one-output typing of generic entropy | CLOSED POSITIVELY | `a_22`: `2^N` operations in arity `[2N]->[1]` |
| G-7 variable-arity quadratic shortcut | CLOSED NEGATIVELY | `a_23`: arity choice manufactures arbitrary entropy |
| G-7 intrinsic rank / boundedness / upper count | CLOSED SECTORIALLY WITH NORMALIZED GAUGE | H7-R in `a_24`, boundedness in `a_30`, injectivity in `a_49`, finite-moment upper count in `a_33` |
| G-7 intrinsic rank and scalar mixed map | PARTIAL POSITIVE | `a_24`: exact `r_m`, `Theta(mn)` domain and collapsed mass |
| G-7 mixed-map injectivity / genuine boundary / upper count | CLOSED ON LAURENT SECTOR, GLOBAL DIMENSION OPEN | `a_28`/`a_30` give boundary membership; `a_49` gives injectivity; `a_33` gives normalized upper count |
| G-7 conditional mixed injectivity | CLOSED AS CRITERION | `a_25`: power evaluations imply injectivity |
| G-7 power-evaluation source lemma | CLOSED POSITIVELY | `a_49`: every positive power character factors through the non-total bio target |
| G-7 Laurent normal form for evaluations | CLOSED POSITIVELY | `a_26` joint-evaluation criterion + `a_49` factorization prove `J_Har=0` |
| G-7 genuine real-boundary membership | CLOSED FOR CROSS FAMILY | `a_28`: typed cross-contraction has both Euclidean vectors in the unit ball; its H7-XI is open |
| G-7 one-family Kunneth compatibility | CLOSED SECTORIALLY, GLOBAL PROMOTION OPEN | `a_30` bounded family + `a_49` injectivity + `a_33` normalized dimension; H7-FMD-ALL/RR remain |
| G-7 bounded Laurent one-family route | CLOSED FOR LOWER/SECTORIAL NORMALIZED COUNT | `a_30` gives the family, `a_49` faithfulness, `a_33` normalized count; `a_31` excludes only raw-cardinality H7-U |
| G-7 full-Laurent scalar route | CLOSED NEGATIVELY AS A PACKAGE | `a_31`: H7-LNF implies `log h0 >= Omega(2^d)` at bidegree `(2d,d)`, contradicting H7-U |
| G-7 selective quotient / normalized dimension | SHARP ON PRESENTATION RAYS / BOUNDARY DESCENT OPEN | `a_120` constructs the calibrated quotient on every positive presentation ray; `a_121` gives its descent criterion and `a_129` reduces that criterion to H7-ARCH-BDRY |
| G-7 H7-SEL multiplication acceptance | OPEN, EXACTLY DELIMITED | `a_32`: balanced dimension is quadratic, but the code is not multiplicatively closed; coefficient-additivity collapses it to diagonal growth |
| G-7 finite-moment normalized dimension | UNCONDITIONAL SECTORIAL POSITIVE | `a_33` gives matching `Theta(mn)` size in `A_12`; `a_49` closes descent; `a_50` closes compatible degree transitions on fixed rays |
| G-7 cofinal moment functoriality | CLOSED ON EVERY FIXED EFFECTIVE RAY | `a_50`: nested moduli `M_j|M_{j+1}`, exact reduction/truncation maps and `Theta(T_j^2)` target size |
| G-7 all-tree finite dimension H7-FMD-ALL | CLOSED ON EVERY FIXED EFFECTIVE RAY | `a_51`: finite twisted bios define odd moments on every scalar tree; odd Vandermonde gives the lower bound and Linnik gives the quadratic upper size |
| G-7 global finite-effective dimension | RETRACTED | `a_57`: every retained characteristic `p` eventually becomes an allowed denominator, so the accumulated target of `a_52` cannot evaluate the whole cone |
| G-7 denominator-compatible global transitions | FINITE ACCUMULATION IMPOSSIBLE; TWO BYPASSES | `a_118` gives degreewise fresh-target reevaluation without transitions. `a_119` gives one characteristic-zero pseudofinite bio supporting every denominator and odd moment. `a_125` retracts target-sheaf exactness; sourcewise H7-FRESH-RESTR and pseudofinite height H7-PF-DIM remain |
| G-7 ordinary/derived/Witt denominator transitions | CLOSED NEGATIVELY | `a_58`: distinct residue fields have no nonzero common unital apex and zero derived intersection; inverting `p` in a Witt lift destroys reduction mod `p` |
| G-7 Picard/principal scalar dimension | CODE-LEVEL ONLY | `a_53` standard representatives and odd-sign invariance survive; its global `h_FM` is retracted with `a_52` by `a_57` |
| G-7 real-degree code coefficient | CLOSED AT CODE LEVEL | `a_53`: continuous formal coefficient `d_1d_2/(2log3)`; realization by actual square Picard degrees additionally requires H7-PB-REG |
| G-7 unfiltered moment algebra | CLOSED NEGATIVELY | `a_54`: one separating moment vector and Lagrange interpolation generate the whole finite product, so raw target cardinality cannot be the sharp RR dimension |
| G-7 bounded moment-image RR candidate | CLOSED NEGATIVELY | `a_55`: one bounded cross-contraction lifts every vector of a full moment block in linear bidegree, exceeding the code coefficient by `Theta(t^2)` |
| G-7 multiplicative selective moment quotient | REDUCED TO AN EXACT FINITE INVARIANT | `a_56`: every ring/bio quotient is a coordinate projection; its minimum separating size is the difference-support hitting number `kappa(r,Q;p)` |
| G-7 selective sheaf dimension and sharp RR | COEFFICIENT CLOSED ON ALL POSITIVE RAYS / SOURCE RESTRICTION OPEN | `a_120` proves the sharp coefficient for every positive ray. Principal/sign invariance and output-degree multiplication are degreewise closed. `a_125` replaces ill-typed target exactness by sourcewise H7-FRESH-RESTR; geometric comparison remains |
| G-7 optimal rank / RR leading coefficient | CLOSED FOR THE CODE, GLOBAL PROMOTION OPEN | `a_34`: ternary rank is information-theoretically maximal and forces `h_code ~ log(2)log(q)Mn/(2log(3))`; `a_55` refutes promotion via the present complete-bounded `h_FM` |
| G-7 prime/arity independence of coefficient | CLOSED FOR EFFECTIVE RAYS | `a_35`: general `k`-ary contractions give the universal code coefficient `deg(D1)deg(D2)/(2log(3))`, independent of prime factorization and arity |
| G-7 pure external sections for quadratic growth | CLOSED NEGATIVELY | `a_14` Thm 1.1 |
| G-7 gauge/Kunneth/intersection/RR | OPEN | `a_12` exact remaining gates |
| R8 raw theta predicate | FAILS | `h_theta(O)>0` |
| R8 acceptance test | CLOSED | `a_08` Def 4.1 and `a_137`: the unique constant threshold placing `O_X` on the boundary is `h_theta(O_X)`; radical classes are not strictly effective |
| full effectivity dictionary | OPEN SEPARATE GATE | requires realisation; `a_137` proves this is G3-EFF/G-7, not an unfinished clause of R8 |

## 4. Why row (a) cannot candidly be marked complete

At least two required compatibility statements are absent:

1. a divisor/cycle theory on the literal square in which Frobenius cycles are
   nonprincipal and retain the local `Lambda` intersections;
2. a degree/gauge/intersection package on that same theory with quadratic
   section growth.

The classical toric surface provides item 2 but fails item 1.  The Haran square
is the candidate carrier for item 1 but has not yet been equipped with item 2.
The Witt/cyclotomic bridge cannot identify them because its quotient loses the
arithmetic and its kernel is killed by weight-one Frobenius gauges.

This is a genuine mathematical obstruction diagram, not a lack of numerical
testing:

```
W_rat kernel --(r,m)--> toric rank 2
     |                       |
     | retains labels        | has degree, metric, RR
     | no positive F-weight1 | loses Lambda(3) vs Lambda(6)
     v                       v
local resultants        global principal-invariant intersection
```

## 5. The next construction gate

Further work should not modify the toric quotient or search for another
weight-one scalar gauge.  Both routes are decided.  The surviving gate is:

> **H7-I7.** On Haran's pro-square, use the injective two-prime bigrade of
> `a_19` (or, for the full continuous Picard plane, close the anti-diagonal),
> realize the faithful Witt operator algebra and exact `Lambda` functional
> of `a_36` as divisorial correspondences extending the prime-incidence
> carriers of `a_17` (or construct genuine pro-scheme Frobenius maps),
> define an archimedean proper gauge, and prove a
> Künneth/Hilbert--Samuel lower and upper bound giving quadratic section
> growth.  The local resultant must appear as a place-wise component, with
> the global principal relation stated separately.

The correspondence clause is no longer algebraically unspecified. `a_36`
constructs the faithful operator algebra
`Gamma_m^op Gamma_n^op=Gamma_mn^op` and derives its diagonal functional
`Lambda(n)` from the Witt lambda-trace. Its realization as cycles on the
literal pro-square, with composition and intersection preserved, is the
gate H7-I7-REAL. `a_37` constructs compatible literal graphs on the Witt
pro-scheme, but proves their relative square is only one-dimensional. Thus
H7-I7-REAL splits into transport H7-WBASE and the trace/intersection formula
H7-WLEF; the Witt graph space cannot substitute for Haran's surface. `a_38`
also proves that ordinary scalar transport factors through the diagonal
fold. H7-WBASE must use a non-total bimodule/kernel or a new two-ruling Witt
enhancement. `a_39` supplies a concrete non-total scalar shadow: conjugated
field additions realize exactly the power characters needed for H7-LNF.
`a_40` constructs their universal commutative involutive bio lift. `a_49`
maps it to the involutive double of the homogeneous endomorphism bio and
proves its unary real monoid injective by evaluation at `1`. This closes
H7-UEMB, H7-TBIO, H7-LNF and the finite-moment descent to `A_12`.
On the trace side, `a_41` proves that naive graph/diagonal intersection is
not merely uncomputed: its fixed ring is `Z`, a horizontal excess component.
The surviving formula is H7-WLEF-red, a derived/excess determinant after
removing the common `F_0` direction. `a_42` then rules out the standard
reduced cone as well: its determinant is one. The exact surviving target is
H7-WLEF-cyc, realizing the primitive cyclotomic conormal determinant
`Norm(1-zeta_n)=Phi_n(1)`. `a_43` supplies its exact prime-local geometry:
`W_p=Z x_{F_p} Z`, and the two character branches meet in `Spec F_p` with
degree `log p`, matching `a_17`. H7-WNODE now asks only for the functorial
transport of this node and compatibility with prime powers/composition.
`a_44` computes those prime-power contacts: the full thickness is `Z/p^k`,
while its primitive new layer is one `F_p` and therefore exactly
`Lambda(p^k)`. H7-WNODE-COMP retains transport/composition and multi-prime
cancellation as the unresolved clauses at that stage. `a_45` closes both
arithmetic clauses in finite contact modules: `P_m tensor P_n=P_mn` and
`log #P_n=Lambda(n)` for all labels. `a_46` then realizes those modules as
literal contact sheaves `M_n` on Haran's square, preserving tensor
composition and the complete `Lambda` mass. The remaining step is no longer
transport of the contact shadow: H7-CYCLE-LIFT must construct the cycles
`Gamma_n`, correspondence composition and the derived identity
`LDelta^*Gamma_n=M_n`.
`a_47` proves that this lift cannot take `Gamma_n=M_n`: the contact functor
necessarily identifies all powers of a fixed prime and all multi-prime
labels. Thus the required cycles must be faithful before diagonal pullback
while having exactly this prescribed nonfaithful shadow.
`a_48` eliminates the next literal shortcut: the prime rulings themselves do
not represent the commutative label monoid under span composition. Mixed
composition either vanishes, losing faithfulness, or retains an oriented
endpoint and fails to commute. Connes--Consani's `Psi(n)` supplies the exact
dynamic law in the arithmetic-site topos, but no bridge from that to Haran's
square or to `M_n` is presently constructed. H7-CYCLE-LIFT is therefore
sharpened to H7-DYNAMIC-LIFT: the cycles need a new transverse/dynamic datum.

The Künneth clause has advanced beyond a generic request. `114_a_24` supplies
an intrinsic rank, a fixed-scalar mixed map and an `exp(Theta(mn))` domain;
`114_a_25` proves its injectivity from a typed power-evaluation family. The
algebraic lower-bound injectivity of that Laurent family is reduced by
`a_27` to H7-DFLAT; `a_49` now closes it independently through simultaneous
homogeneous bio representations. Separately, `a_28` proves genuine real-boundary
membership for a cross-contraction family. `a_29` proves that these families
have different outer labels and may not be spliced. `a_30` then constructs a
dyadic binary tree inside the Laurent family itself and proves its genuine
real membership, closing H7-WV without interchange. `a_31` then proves that
full H7-DFLAT/LNF would separate exponentially many bounded leaf multisets
and contradict H7-U. Thus the surviving raw-cardinality route requires
H7-SEL, a selective quotient separating the balanced code while collapsing
the operadic closure; alternatively one must define a normalized dimension
or change the gauge. `a_32` clarifies that the lower-bound witnesses need not
themselves form a section ring. `a_33` then supplies a finite-moment
normalized dimension with matching quadratic lower and upper size in the
Laurent sector on every positive ray. Its finite descent H7-FMD is now
unconditional by `a_49`. Extension to all scalar trees, global
presentation-independent degree functoriality, intrinsic divisor height and
intersection/RR remain. `a_34` proves that the
ternary signed rank is optimal and isolates the forced sectorial RR
coefficient. `a_35` removes its apparent dependence on the primes and binary
arity: for arbitrary effective divisor rays it is universally
`deg(D1)deg(D2)/(2log(3))`. This remains the coefficient of the explicit
code, not of the complete bounded moment image: `a_55` proves that the
latter is quadratically larger on a positive ray. Global promotion therefore
requires the new H7-SEL-RR/EXACT object.
`a_50` repairs degree functoriality on each fixed effective ray without
losing the quadratic bound: dyadic cofinal scales accumulate separating
prime factors in nested moduli, and reduction/truncation gives exact
transition maps. What remains of H7-FMD-ALL is all-tree cofinality and a
presentation-independent system for arbitrary divisors at the `a_50` stage.
`a_51` closes the all-tree clause: controlled primes make all required odd
power maps multiplicative permutations of finite fields, so `a_49` supplies
full bio evaluations. Odd Vandermonde separation and Linnik's prime bound
give matching quadratic lower/upper size. The remaining global clause is
renamed H7-FMD-GLOB: presentation and principal-divisor invariance.
At the `a_52` stage uniform blocks were claimed to close the complete finite
effective cone, and `a_53` standardized Picard representatives. `a_57`
retracts the global claim: every retained characteristic `p_i` eventually
occurs as the allowed denominator `p_i`, where its inverse cannot be reduced
modulo `p_i`. Individual bounded-height blocks, fixed-support rays, standard
representatives and the sign-invariant code coefficient survive. Global
dimension now additionally requires H7-DEN-TRANS.
`a_58` closes the three immediate repairs negatively. Distinct residue
characteristics admit neither a common nonzero unital ring nor a nonempty
derived intersection over `Z`; same-prime `Tor_1` records only local excess.
Witt lifting retains reduction until `p` is inverted, at which point no map
back to the finite block exists. Any global transition must therefore be
nonunital/additive, determinant-trace based, or use a new characteristic-zero
adelic dimension rather than transport finite moment values.
`a_59` sharpens G-3 independently: every non-additive transport whose
two-point polarization controls all linear combinations is already
RH-equivalent by the Lorentzian inertia bound. The one-ray collapse is
vacuous, and the polarization/Kunneth escape is circular. The only remaining
structured branch is G3-EFF, an exact effectivity/section biconditional that
distinguishes both signs without imposing two-point linearization.
`a_60` closes that final logical branch as RH-equivalent. Since `D^o` has no
strictly effective class and the a4-weak target makes one sign of every
positive-square class effective, G3-EFF forces `s<=0`. Under RH the map
`sqrt(-s/2)(1,-1)` supplies the converse. Thus G-3 is fully delimited; the
full effectivity dictionary outside `D^o` remains open separately.
`a_66` corrects the type boundary in `a_65`: Haran (11.7) is a right-action
subsheaf, not a Section-6 abelian module. Unit-torsor pullbacks nevertheless
exist unconditionally, so `a_61` still supplies a faithful monoidal family in
`Pic_tor`. H7-PRIME-REG is needed for the completed generator `1/p`; a
separate typed comparison was needed. `a_67` now constructs the principal
quotient/right act and identifies its **ordinary diagonal** layers with
`M_n`. `a_68` constructs the global cotangent conormal and `a_69` splits its
ordinary `F_p[1]` contact as a canonical retract; only the complementary
derived excess remains open. Dynamic convolution remains separately open.
`a_54` proves that the unfiltered moment algebra cannot supply the sharp
comparison: a single separating moment vector generates the entire finite
product by Lagrange interpolation. `a_55` strengthens this to a decisive
bounded no-go: centered Vandermonde lifts placed in one genuine cross-
contraction already surject onto a full block at bidegrees
`(log(m(p-1)),m log2)`. Their excess over the code coefficient is
`Theta(m^2)`, so the sharp comparison for the existing complete-bounded
`h_FM` is false. The surviving H7-SEL-RR/EXACT gate must construct a new
canonical selective quotient or filtration, exclude this explicit family,
and prove multiplication, principal invariance, restriction exactness and
the intersection identity.
`a_56` completely classifies the quotient-based option at each finite block:
ideals of `F_p^m` only discard coordinates. A selected set separates the
code exactly when it hits the coordinate-difference support of every code
pair. Thus its optimal cardinality is `p^kappa`, and the sharp coefficient
is equivalent to the single asymptotic H7-SEL-MOM condition
`kappa log p-log #I=o(t^2)`. Finite examples show that `kappa` can strictly
exceed the information bound, so the asymptotic is not automatic.
The arity-inflation audit of `a_23` is now an actual obstruction, not only an
acceptance warning.

The full anti-diagonal clause can be closed by `114_a_16` Theorem 3.1: compute
partial-diagonal detection of units on `X^[3]` and prove effective descent of
completed line bundles along `X->S` (or bypass both with an absolute-point
slice/direct cocycle computation).  It is no longer a prerequisite for the
minimal rank-two program: `114_a_19` proves that the kernel cannot meet the
two-prime lattice except at zero.

The bigrade, prime carriers, local `log p` incidence, intrinsic mixed domain
and conditional injectivity criterion now exist.  The remaining nouns above
are still absent or uncomputed; none may be replaced by its toric analogue
without an explicit functor.

## 6. Verification status

`114_a_15_full_row_a_verify.py` enumerates the complete 52-script suite. The
following component verifiers cover the new or corrected claims:

- `114_a_05_i7_kernel_verify.py` — kernel and quotient collision;
- `114_a_07_toric_realisation_verify.py` — Haar norm and derived U-form;
- `114_a_08_g2_r8_verify.py` — exact count/asymptotic and R8 threshold;
- `114_a_09_i7_no_go_verify.py` — Frobenius fixed points and principal no-go.
- `114_a_11_g1_binary_constant_verify.py` — positive-boundary entropy and
  exact coupled constant.
- `114_a_12_haran_source_and_picard_verify.py` — source types and external
  Picard anti-diagonal reduction.
- `114_a_13_g3_boundary_verify.py` — universal non-additive domination and
  its failure of additivity/sign separation.
- `114_a_14_h7_kunneth_verify.py` — pure-product no-go and mixed quadratic
  acceptance test.
- `114_a_16_h7_descent_source_verify.py` — descent source anchors and the
  normalized unit-defect criterion.
- `114_a_17_h7_prime_incidence_verify.py` — literal prime/diagonal pullback
  and its `log #F_p=Lambda(p^k)` local mass.
- `114_a_18_h7_prime_picard_verify.py` — idelic curve-prime degree and
  unconditional abstract square nontriviality.
- `114_a_19_h7_discrete_bigrade_verify.py` — unconditional abstract
  two-prime rank-two lattice; completed refinement remains separate.
- `114_a_20_h7_axis_sections_verify.py` — curve-axis and abstract mixed grid;
  the completed bounded ceiling remains conditional on H7-PB-REG.
- `114_a_21_h7_off_diagonal_entropy_verify.py` — generic two-addition defect
  and its exact `2^N` block amplification inside one diagonal fiber.
- `114_a_22_h7_scalarization_verify.py` — one-output bit recovery and the
  collapsed real norm of the scaled quadratic family.
- `114_a_23_h7_arity_inflation_verify.py` — exact no-go against manufacturing
  quadratic growth by choosing a variable input arity.
- `114_a_24_h7_intrinsic_rank_verify.py` — exact axis-derived rank, canonical
  scalar mixed map, quadratic domain entropy and collapsed mass.
- `114_a_25_h7_power_evaluation_verify.py` — balanced-base proof that a typed
  power-evaluation family would make the scalar mixed map injective.
- `114_a_26_h7_laurent_gate_verify.py` — Laurent encoding and separation by
  all positive power characters.
- `114_a_27_h7_differential_injectivity_verify.py` — arithmetic prime
  differential, localization and the conditional minimal-degree descent.
- `114_a_28_h7_real_boundary_verify.py` — exact Euclidean bounds, finite
  trivialization and quadratic domain entropy for the cross family.
- `114_a_30_h7_bounded_laurent_tree_verify.py` — dyadic node contraction,
  ternary leaf capacity, exact finite valuation and quadratic Laurent-domain
  entropy.
- `114_a_31_h7_lnf_upper_nogo_verify.py` — full-Laurent leaf-multiset
  inflation and its contradiction with a quadratic upper bound.
- `114_a_32_h7_selective_acceptance_verify.py` — multiplication-support
  obstruction, diagonal collapse and the exact H7-SEL acceptance boundary.
- `114_a_33_h7_finite_moment_verify.py` — exhaustive finite-moment
  separation, Vandermonde determinants and quadratic finite-image bounds.
- `114_a_34_h7_optimal_rank_rr_verify.py` — sharp signed leaf capacity,
  optimal ternary rank and convergence to the candidate RR coefficient.
- `114_a_35_h7_general_arity_verify.py` — general Euclidean contractions,
  divisor valuations and universality under prime/arity regrouping.
- `114_a_36_i7_witt_operator_verify.py` — faithful Verschiebung composition,
  cyclic-vector separation and the exact cyclotomic `Lambda` mass.
- `114_a_37_i7_witt_graph_verify.py` — Frobenius-stable finite Witt stages,
  literal graph composition and finite-free relative-square ranks.
- `114_a_38_i7_scalar_transport_nogo_verify.py` — uniqueness of the two
  integer maps, fold factorization and loss of the ruling label.
- `114_a_39_h7_twisted_field_verify.py` — transported field laws, exact
  power-character integers and failure of total interchange.
- `114_a_40_h7_universal_twisted_bio_verify.py` — categorical source
  anchors, common unary multiplication and the conditional non-total witness.
- `114_a_41_i7_witt_excess_verify.py` — unit-minor fixed-ring computation,
  torsion-free horizontal excess and the `F_0` retraction.
- `114_a_42_i7_standard_cone_nogo_verify.py` — nilpotent reduced Frobenius,
  determinant-one cone and the forced cyclotomic norm replacement.
- `114_a_43_i7_witt_prime_node_verify.py` — the exact fiber-product
  presentation `W_p=Z x_{F_p} Z` and its `log p` branch intersection.
- `114_a_44_i7_prime_power_contact_verify.py` — adjacent character contact
  ideals, primitive `F_p` layers and the prime-power order index.
- `114_a_45_i7_global_contact_verify.py` — tensor-gcd composition,
  multi-prime annihilation and exact `Lambda(n)` contact masses.
- `114_a_46_i7_geometric_contact_sheaf_verify.py` — stalkwise contact-sheaf
  composition on Haran's square and exact global `Lambda(n)` mass.
- `114_a_47_i7_contact_shadow_verify.py` — complete shadow classification,
  monoidal law and the unavoidable prime-power/multi-prime collisions.
- `114_a_48_i7_ruling_span_nogo_verify.py` — finite span-composition shadow,
  endpoint support and the ruling commutativity/faithfulness obstruction.
- `114_a_49_h7_homogeneous_endobio_verify.py` — two transported field laws,
  homogeneous bio commutativity and unary scalar separation.
- `114_a_50_h7_cofinal_moment_verify.py` — nested composite moduli, exact
  degree transitions, code separation and cofinal quadratic size.
- `114_a_51_h7_full_tree_bio_moment_verify.py` — controlled primes,
  transported finite fields, full-tree homogeneity and odd moments.
- `114_a_52_h7_global_finite_effective_verify.py` — uniform per-height
  blocks and the later-characteristic collision exposed by `a_57`.
- `114_a_53_h7_picard_normalization_verify.py` — standard representatives,
  residual signs/metrics and real-degree code coefficient; not global `h_FM`.
- `114_a_54_h7_moment_saturation_verify.py` — Lagrange idempotents and
  saturation of the unfiltered finite moment algebra.
- `114_a_55_h7_bounded_cross_interpolation_verify.py` — exact Vandermonde
  lifts, contraction norms, bounded block surjectivity and RR coefficient gap.
- `114_a_56_h7_selective_moment_quotient_verify.py` — coordinate-ideal
  classification, exact hitting numbers and selective quotient cardinality.
- `114_a_57_h7_global_denominator_nogo_verify.py` — later collision of every
  retained characteristic with its own allowed divisor denominator.
- `114_a_58_h7_den_trans_span_derived_witt_verify.py` — Bezout collapse,
  cross-prime derived vanishing and the Witt inversion/reduction dichotomy.
- `114_a_59_g3_two_point_polarization_verify.py` — two-point Gram domination,
  Lorentzian inertia and the sign loss of the one-ray collapse.
- `114_a_60_g3_effectivity_equivalence_verify.py` — target property (E),
  spatial-ray converse and the positive-square effectivity contradiction.
- `114_a_61_i7_faithful_picard_lift_verify.py` — faithful prime-valuation
  torsor labels and the separate finite contact algebra.
- `114_a_62_i7_cartier_prime_regularity_verify.py` — curve-side prime
  anchors, all-arity denominator regularity and the operation/module type
  distinction.
- `114_a_63_h7_fraction_pullback_admissibility_verify.py` — Section-11
  denominator quantifiers and failure of regularity preservation even for a
  split map.
- `114_a_64_h7_prime_regularity_saturation_verify.py` — exact equivalence
  between prime regularity and tree-congruence saturation, plus the residual
  characteristic sufficient criterion.
- `114_a_65_h7_abstract_picard_pullback_verify.py` — compatibility wrapper
  recording the `Pic_qc` retraction and corrected torsor verdict.
- `114_a_66_h7_type_audit_verify.py` — source distinction between abelian
  modules and right-action lattices, plus unconditional unit-torsor pullback.
- `114_a_67_h7_typed_cartier_act_verify.py` — principal equivalence-ideal
  quotient/right act and exact ordinary diagonal contact algebra.
- `114_a_68_h7_cotangent_lci_gate_verify.py` — global cotangent conormal
  typing, ordinary `L_{F_p/Z}=F_p[1]`, and the exact LCI base-change gate.
- `114_a_69_h7_split_cotangent_verify.py` — split derived comparison,
  canonical `F_p[1]` retract and reduced `Lambda(n)` contact law.
- `114_a_70_i7_decorated_diagonal_verify.py` — faithful decorated-span
  composition, unit/zero distinction and monoidal contact shadow.
- `114_a_71_h7_fold_fiber_verify.py` — exact fold-fiber cancellation
  criterion, strictly weaker residual target, localization lemma and the
  absence of a source-level unique-normal-form theorem.
- `114_a_72_h7_all_arity_block_regular_verify.py` — full-bio cubic
  separation and prime cancellation on all block-extractable same-fold
  families, uniformly in their arity.
- `114_a_73_h7_depth_two_regular_verify.py` — Boolean pair reconstruction
  and prime cancellation for every depth-two read-once partition tree.
- `114_a_74_h7_read_once_hessian_verify.py` — exact mixed-Hessian identity,
  recursive root/partition reconstruction and all-depth unsigned read-once
  prime cancellation.
- `114_a_75_h7_signed_read_once_verify.py` — leaf-sign recovery, orthant
  reduction and Hessian-support invariance for signed read-once trees.
- `114_a_76_h7_cancellation_purity_verify.py` — corrected long-source audit,
  exact colon-congruence criterion and non-pure quotient warning; the
  bilateral cancellation-purity theorem remains open.
- `114_a_77_h7_cut_and_local_bundle_verify.py` — order-ideal connectivity of
  all cuts on a fixed DAG and prime purity of isolated signed parallel
  bundles; topology-changing core confluence remains open.
- `114_a_78_h7_single_site_confluence_verify.py` — joint confluence of unary
  and alternating tree reductions plus unique one-site topology change.
- `114_a_79_h7_core_critical_pairs_verify.py` — termination and all local
  critical-pair identities for the fixed-incidence signed-network subsystem;
  it is not presentation-complete.
- `114_a_80_h7_odd_prime_and_sign_orbit_verify.py` — conditional signed-
  incidence/Smith criterion and the explicit `Z/3` warning; unconditional
  base odd-prime regularity is retracted.
- `114_a_81_h7_k22_two_torsion_verify.py` — sign-fixed `K2,2` candidate,
  absence of local redexes and its exact identification as a contextual
  image of `x_0`, hence zero rather than nonzero 2-torsion.
- `114_a_82_h7_rectangular_macro_smith_verify.py` — exact incidence Smith
  forms for all rectangular macro contexts and safe vertex quotients.
- `114_a_83_h7_aggregated_fiber_smith_verify.py` — exact `Z/n` obstruction
  from cycle Laplacians, including odd torsion in the bipartite `C_6` model.
- `114_a_84_h7_tame_scalar_reduction_verify.py` — tame sandwich theorem
  reducing all-arity regularity to scalar regularity, with both hypotheses
  explicitly open for the arithmetic plane.
- `114_a_85_h7_macro_context_graph_verify.py` — exact sandwich-context graph,
  component-injectivity criterion and the p-CONVEX/DIVPATH decomposition.
- `114_a_86_h7_p_convex_boundary_verify.py` — graph-theoretic equivalence
  between p-CONVEX and the one-boundary attachment condition, with exhaustive
  finite controls through five vertices.
- `114_a_87_h7_characteristic_zero_residual_verify.py` — simultaneous
  all-prime cancellation from a faithful characteristic-zero scalar residual
  map, followed by tame sandwich promotion to every arity.
- `114_a_88_h7_real_bio_marginal_blindness_verify.py` — exact factorization
  of unary homogeneous-bio evaluations through signed left/right marginals
  and a minimal three-leaf pairing ambiguity.
- `114_a_89_h7_two_level_marginal_verify.py` — corrected complete relation
  lattice for a fixed two-level grid: both ruling contrasts reduce the
  quotient to total signed mass `Z`, with all-prime saturation.
- `114_a_90_h7_laminar_nested_verify.py` — all-depth laminar/no-reuse cut
  gluing as direct sums of oriented incidence matrices, hence saturated at
  every prime.
- `114_a_91_h7_binary_matching_verify.py` — Hall decomposition of every
  regular binary copy-mixing interface and the minimal ternary even-parity
  hypergraph obstruction to matching decomposition.
- `114_a_92_h7_parity_fiber_verify.py` — typed realization of that parity
  hypergraph by the finite-set maps `i`, `j`, `i+j`, with all pair projections
  bijective.
- `114_a_93_h7_parity_smith_verify.py` — exact Smith factors `1,1,1,2`, the
  explicit order-two incidence class and its destruction by any odd edge;
  macro endpoint realization remains open.
- `114_a_94_h7_fold_zero_parity_verify.py` — fold-preserving even differences
  still have Smith `1,1,2` and the explicit half-integral witness.
- `114_a_95_h7_parity_swap_verify.py` — any internal undecorated coordinate
  swap kills that factor two, so the bare parity candidate is rejected.
- `114_a_96_h7_parity_rigid_verify.py` — intrinsic same-fold bit decorations
  remove the swap automorphisms at the typed-tree level.
- `114_a_97_h7_positive_rigid_no_go_verify.py` — the three even moves force
  all positive scalar decoration ratios to one; scalar-visible
  rigidification cannot realize the parity collision.
- `114_a_98_h7_scalar_invisible_full_bio_verify.py` — scalar-invisible
  labelled pair partitions are separated by Boolean full-bio probes, so
  block-extractable rigidification also cannot realize the even moves.
- `114_a_99_h7_tame_retract_dichotomy_verify.py` — nonextractable rigidity
  splits exactly into an ambient nontameness witness or a failure of the
  outer context to transmit scalar sandwiches.
- `114_a_100_h7_finite_set_retract_verify.py` — arbitrary finite-set
  multiplication/contraction reuse has coordinate retractions; only
  nonsplit outer operation coefficients remain.
- `114_a_101_h7_split_coefficient_retract_verify.py` — typed one-sided
  splittings transmit every scalar sandwich exactly; the matrix shadow is
  the unit-ideal criterion, and nonsplitness without annihilation is shown
  insufficient.
- `114_a_102_h7_augmentation_flatness_verify.py` — scalar prime regularity
  is exactly vanishing of the prime torsion/Tor in the off-diagonal
  augmentation ideal; a split but nonflat ring prevents using the fold as a
  shortcut.
- `114_a_103_h7_cross_defect_tameness_verify.py` — every surviving
  centre-versus-grid cross defect has identical complete sandwich signature
  and hence explicitly refutes tameness; the signed mixed-generator equality
  is decided by `a_104`.
- `114_a_104_h7_signed_plane_nontame_verify.py` — Haran's `N` normal form
  gives nine independent coordinates for centre minus grid, while its
  ordinary matrix image is zero; H7-XDEF-12 survives and the plane is not
  tame.
- `114_a_105_h7_first_jet_prime_regular_verify.py` — the normal form for
  `N` is free abelian in every arity, the two ordered jet targets are
  prime-regular, and every possible source collision is confined to their
  common equality kernel.
- `114_a_106_h7_universal_rational_jet_verify.py` — an exact
  prime-valuation entropy cocycle disproves `C Omega -> N` injectivity; the
  rationalized universal first-jet target cancels every prime in all
  arities.
- `114_a_107_h7_scalar_differential_z2_verify.py` — the scalar universal
  differential is exactly two free prime copies plus one shared `Z/2` sign
  anomaly.
- `114_a_108_h7_explicit_scalar_two_torsion_verify.py` — the anomaly
  integrates to `kappa=(1,-1)_1 o (1,1)_2^t`; wire transposition proves
  `2kappa=0`, while the universal jet proves `kappa!=0`.
- `114_a_109_h7_z_regular_reflection_verify.py` — the minimal quotient seen
  by all simultaneous Z-regular targets kills `kappa` but retains both axes,
  the non-total cross defect and every `F_p` diagonal contact.
- `114_a_110_h7_regular_pro_square_verify.py` — regular reflection is
  functorial, glues reflected affine charts through central localizations,
  and restores the faithful prime-generated completed lattice on the new
  pro-square.

The meta-verifier establishes consistency of the executable claims; it does
not turn the explicitly open H7-I7 constructions into theorems.

The complete integrated 62-component suite through corrective `a_63`
(including the three imported row-D acceptance controls) passed on
2026-08-05 in `459.16s`. The run checks the narrowed `a_52`/`a_53` verdicts
and the corrected completed-lattice scopes of `a_12`, `a_18`--`a_20` and
`a_61`, rather than their retracted strong claims. The `a_64` and `a_65`
verifiers then passed separately. After the type correction `a_66`, the
fresh integrated suite of all 65 components passed on 2026-08-05 in
`460.31s`. The integrated 72-component suite through `a_73` then passed on
2026-08-05 in `472.35s`. After integrating `a_74`--`a_76`, the complete
75-component suite passed on 2026-08-05 in `484.86s`.  The `a_77` verifier
then passed separately, followed by the targeted `a_78`--`a_88` runs.  After
integrating all corrections and scope guards through `a_88`, the complete
87-component suite passed on 2026-08-05 in `521.68s`.  After the targeted
`a_89`--`a_100` runs, the complete integrated suite of all 99 then-existing
components passed on 2026-08-05 in `550.40s`.  The new `a_101` verifier
passed separately (6,380 coefficient systems and 29,504 exact scalar
retractions).  The new `a_102` verifier also passed separately (8,640 finite
abelian Tor controls plus split nonflat ring controls).  The new `a_103`
verifier passed separately (1,794 blind-signature systems).  The `a_104`
exact normal-form verifier then passed (324 scaling-transfer controls and a
nine-coordinate nonzero defect).  The `a_105` all-arity jet verifier passed
with 5,054 scalar-transfer controls.  The `a_106` verifier then passed 1,331
cocycle triples, 1,331 homogeneity identities and 2,450 coupling controls.
The `a_107` classification verifier passed 14,641 sign-cocycle and 6,561
coupling controls; the symbolic `a_108` verifier then passed the explicit
nonzero two-torsion theorem.  The `a_109` reflection and `a_110` pro/lattice
verifiers passed separately (including 14,400 valuation tensor laws), and
`a_111` passed its rank-two Cartier/contact controls. That 110-component
single-process run passed on 2026-08-05 in 552.00 seconds. The meta-verifier
The 119-component single-process suite through `a_120` passed on 2026-08-05
in 558.02 seconds.  A fresh 137-component snapshot through `a_138` then
passed on 2026-08-05 in 569.19 seconds. The meta-verifier now enumerates 143
components. The fresh full 143-component suite through `a_144` passed on
2026-08-05 in 566.97 seconds, including the three imported row-D
non-circularity controls.

These verifiers cover their stated finite/algebraic claims. They do not prove
RH or certify the open anti-diagonal, one-family Kunneth, H7-U and
intersection parts of Haran G-7. G-3 is classified as an RH-equivalent
boundary, not constructed unconditionally.

## 7. Final verdict for this audit

> **Current verdict (`a_144`): Point A is closed in the metrized bivariant
> category stated by the authoritative a1--a5 contract.** The object is the
> valued supportwise Haran square with its actual metrized Div/Prin quotient,
> normalized RR determinant, torsion contact determinant, Green quotient and
> contact-framed dynamic kernels. This closes A only and does not prove RH.

The following paragraph is the historical verdict before `a_142`--`a_144`,
retained as provenance for the obstruction campaign:

> **Historical verdict through `a_141`: Point A was materially advanced but
> not complete.** a4-weak is now a
> rigorous semipositive toric Arakelov construction; G-1, G-2 and the R8 test
> are settled. I7 has faithful Witt composition, exact cyclotomic mass and a
> monoidal contact-sheaf realization on Haran's literal square. `a_66`
> restores the faithful square-Picard labels as unit torsors; H7-PRIME-REG
> remains necessary for their completed lattice/gauge. `a_67` supplies a
> typed principal Cartier-act and its exact ordinary diagonal contact;
> `a_68`--`a_69` construct the global cotangent conormal and split that contact
> from its possible excess. `a_70` closes the faithful dynamic lift in the
> Picard-decorated span category; the stronger undecorated lift is open.
> `a_71` reduces prime regularity to same-fold fiber cancellation and shows
> that localization introduces no new collision; `a_72` proves cancellation
> on every block-extractable arbitrary-arity fiber, and `a_73` on every
> depth-two read-once fiber. `a_74` closes every depth and arity in the
> unsigned read-once sector, and `a_75` includes all leaf signs. `a_76`
> corrects the source audit and identifies the residual bilateral theorem as
> `(E_cancel:p)=E_cancel`, equivalent here to H7-RF-BICUT. `a_77` proves
> that all cuts of a fixed network are connected and every
> isolated signed parallel bundle is prime-pure, leaving only the
> topology-changing overlaps H7-CORE-CONFLUENCE. `a_78` closes joint tree
> reduction and one-site topology change, and `a_79` every visible finite
> cascade, only in the fixed-incidence subsystem. `a_81` shows this is not
> presentation-complete: its locally irreducible `K2,2` is a macro context
> image of `x_0` and is zero.  The full remaining gates are
> H7-MACRO-CONTEXT-NF/SAT and boundary transport. `a_82` closes every
> rectangular macro grid; `a_83` reduces the first
> nonseparable danger to H7-FIBER-RETENTION via exact cycle-Laplacian Smith
> obstructions. `a_84` gives the alternative sufficient route
> H7-TAME-PLANE plus H7-SCALAR-SAT. `a_85` closes the macro edge presentation
> itself and reduces saturation to
> p-CONVEX plus p-DIVPATH on the sandwich-context graph. `a_86` sharpens the
> first gate: p-CONVEX is exactly H7-p-ONE-BOUNDARY, so a failure is one
> connected nondivisible region attached to two distinct divisible components.
> H7-p-ONE-BOUNDARY and p-DIVPATH remain open. `a_87` gives the alternative
> simultaneous route H7-REAL-RES plus H7-TAME-PLANE: a faithful product of
> real scalar evaluations cancels every prime at once, and tameness promotes
> this to all arities. `a_88` proves that the unary targets currently built
> forget bilateral leaf-pair correlations, so the residual route additionally
> needs H7-MARGINAL-COMPLETE or an enriched correlation-sensitive target.
> Corrected `a_89` closes prime saturation on every fixed two-level grid:
> both ruling context families reduce the quotient to total mass `Z`. Its
> first row/column-margin formulation is retracted using the `a81` K2,2
> regression. The remaining gate is H7-NESTED-CONTEXT-SAT across cut-changing
> overlapping grids. `a_90` closes every laminar no-reuse nesting by
> fiberwise incidence; the remaining shape is H7-NONLAMINAR-FIBER, requiring
> contraction/reuse or aggregation across incomparable blocks. `a_91`
> removes every isolated binary interface and reduces the first matching
> danger to H7-TERNARY-OVERLAP. `a_92` realizes its typed finite-set skeleton;
> `a_93` finds exact `Z/2` in the skeleton's incidence cokernel, but not yet
> in the Haran quotient. `a_94` retains the factor after imposing fold-zero
> differences, but `a_95` shows an undecorated child swap kills it.  The bare
> candidate is rejected; H7-PARITY-RIGID or a different nonlaminar shape
> remains. `a_96` supplies same-fold rigid decorations, but `a_97` proves
> their positive scalar separation forbids the required even moves. Only
> scalar-invisible rigidification seemed possible; `a_98` constructs one but
> shows full-bio block probes still kill the moves. Only
> H7-NONEXTRACTABLE-RIGID or a different nonlaminar shape survives, and no
> Haran torsion class is claimed. `a_99` splits this into nontameness or a
> nonretractable context; `a_100` eliminates finite-set reuse itself, leaving
> only nonsplit outer labels. `a_101` closes the split-label sector and shows
> that nonsplitness alone is not an obstruction: the exact residual branch is
> H7-COEFF-ANN, requiring an ambiently separable pair killed by a two-sided
> nonsplit context. `a_102` identifies the simultaneous scalar theorem as
> H7-AUG-FLAT, torsion-freeness of the fold augmentation ideal. `a_103`
> gives the canonical tameness test H7-XDEF-12, and `a_104` closes it
> negatively: a commutative infinitesimal target separates centre from grid,
> so H7-TAME-PLANE is false.  The conditional tame promotion is therefore
> dead; H7-AUG-FLAT alone is only scalar, and the live all-arity route is
> direct p-CONVEX/p-DIVPATH or componentwise cancellation purity. `a_105`
> closes the explicit `N`-detected part of that route: both ordered infinitesimal
> targets are prime-regular in every arity, so any collision lies in their
> common `N`-jet kernel H7-JET1-KERNEL-PURE. The universal differential
> kernel does contain additional first-order information: `a_106` constructs
> an infinite-order entropy class killed by `N`.  Its universal rational
> first-jet target is nevertheless prime-regular in every arity, so any
> collision lies in the common rational-jet kernel. `a_107` computes the
> scalar integral differential as two free prime copies plus one `Z/2`, and
> `a_108` integrates that anomaly to a nonzero scalar `kappa` with
> `2kappa=0`. Hence H7-AUG-FLAT and H7-PRIME-REG are false, and the
> Section-11 completed regular-denominator route fails at `2`. The live
> repair must be torsion-aware and retain the literal `Lambda(2)` contact.
> `a_109` constructs the universal Z-regular reflected base, killing exactly
> the forced obstruction while retaining both axes, non-totality and all
> prime contacts. `a_110` glues its affine reflections into a modified
> pro-square and restores every prime-generated completed lattice. `a_111`
> closes every distinct-prime rank-two subgroup, and `a_112` extends the
> result to all axes and disjoint supports while isolating the anti-diagonal
> as the only possible Picard kernel. `a_113`--`a_115` compute the forced
> local intersection blocks and prove that reduced `Lambda` contact is not
> the global RR intersection. `a_116` constructs the hyperbolic RR form and
> proves that its descent is equivalent to anti-diagonal faithfulness.
> `a_117` obtains the sharp RR coefficient on each saturated block; `a_118`
> closes fresh degreewise evaluation and principal invariance; `a_119`
> supplies a common characteristic-zero algebraic bio for all denominators;
> `a_120` upgrades the calibrated bounded-section asymptotic to every
> positive effective ray, with exact leading term and `O(t)` error.
> `a_121` proves that descent of this invariant and descent of the `a_116`
> RR form are the same anti-diagonal faithfulness problem. `a_122` isolates
> the required ruling product formula; `a_128` proves the finite candidate
> `p_2/p_1` leaves a real-boundary defect, and `a_129` identifies that defect
> as the exact remaining kernel H7-ARCH-BDRY.
> `a_123` closes the complete numerical Green counterterm on the prime
> presentation; only its geometric metric/excess realization remains.
> `a_124` realizes that counterterm as a canonical metrized biextension and
> quadratic gauge; comparison with actual repaired Cartier sheaves remains.
> `a_129` then uses Haran's pre-Picard divisor object and global-fraction
> action to derive the exact residual boundary-kernel formula.
> `a_130` realizes that residual geometrically on the two repaired mixed
> boundaries and reduces faithfulness to one explicit base-change map on the
> already known prime curve Picard lattice.
> `a_131` then retracts the claimed global construction underlying those
> statements: the finite `Reg_Z` functor cannot be applied unchanged to the
> real charts. `a_132` supplies the corrected supportwise relative reflection
> and proves H7-LOCAL-REG-GLUE, restoring the pro-square and every
> finite-support prime lattice on cofinal tails.
> `a_133` closes the undecorated diagonal-multiplicity alternative
> negatively and leaves only genuine thickenings/derived or moving supports.
> `a_134` audits the derived-module alternative: Haran's Section 6 makes it
> meaningful but does not provide the required rank-one, descent,
> tensor/convolution, faithfulness and contact comparisons.  Their exact
> conjunction is H7-TOR-LIN, not a completed kernel construction.
> `a_135` corrects the mixed real edge itself: the base is the rational
> sphere residue `kappa_infty`, and boundary faithfulness is the explicit
> conservative-base-change statement H7-RSPH-CONS.  No flatness or norm
> theorem proving it occurs in the audited source.
> `a_136` then rules out the easiest missing theorem: the rational sphere
> extension has no `S`-algebra retraction. Hence a section cannot prove
> boundary Picard injectivity; H7-RSPH-DESC/NORM is the surviving route.
> `a_137` closes R8 as the acceptance test actually stated: its basepoint
> threshold is forced and unconditional. The full effectivity dictionary is
> retained separately under G3-EFF/G-7 rather than misreported as open R8.
> `a_138` rewrites the surviving boundary problem as the exact Cech unit
> intersection H7-RSPH-UNIT. Thus the next proof obligation is a unary-unit
> normal form for three explicit tensor-product charts, not an unspecified
> Picard-descent assertion.
> `a_139` corrects I7's scope: decorated dynamics and exact monoidal contact
> are already closed. What row A still needs is H7-DYN-INTEGRATE, their
> comparison with the unified G-7 divisor/intersection theory. An ordinary
> undecorated Chow lift is optional unless imposed as an extra convention.
> `a_140` closes the dynamic/contact part of that integration in one typed
> contact-framed kernel monoid. It deliberately composes the canonical
> `H_1` retracts, not the shifted ambient complexes. Only H7-FRAMED-RR now
> remains from H7-DYN-INTEGRATE.
> `a_141` constructs the contact half of the required two-target determinant
> comparison and identifies it isometrically with `E_C`. Its generic half
> is the exact remaining gate H7-RR-DET; the `O(t)` asymptotic of `a_120`
> alone does not supply it.
> Thus finite accumulated DEN-TRANS is no longer the live route.
> `a_142` subsequently closes the normalized RR determinant on the
> presentation. `a_143` constructs the non-circular Picard norm from the
> pre-residue Euclidean valuation, so bare H7-RSPH-UNIT is no longer needed
> for metrized descent. `a_144` then assembles the single a1--a5 object.
