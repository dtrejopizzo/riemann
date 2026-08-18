# 107.43 -- Paper C audit coverage matrix

## 1. Purpose

Paper C had accumulated substantial forward construction, but without a
clean line separating exact local audits from still-globalized theorem
targets.  This note records that boundary explicitly so later progress
cannot silently promote unresolved geometry.

The status labels used here match `107_14`:

1. `exact-audited` means a claim is checked by a finite verifier already
   present in the workspace;
2. `formalized` means the claim is theorem-level or blueprint-level but
   not exact-audited;
3. `partial` means some local subclaims are exact-audited, while the
   full paper output is not.

## 2. Coverage table

| Part | File | Load-bearing claim | Status | Audit artifact |
| --- | --- | --- | --- | --- |
| III-Pre | `107_10` | universal finite-model target and structural exclusions | `partial` | `107_63` and `107_86` exact-audit the finite exclusion and assembled finite-support realization shadows |
| III-PreB | `107_11` | Picard/Jacobian realization target and exact radical control | `partial` | `107_48`, `107_49`, `107_78`, `107_82`, `107_87`, and `107_89` exact-audit the finite kernel, pairing-transport, degree-zero/covariance, candidate-target assembly, point-spectrum retention, and divisor-sensitivity shadows |
| III-A | `107_15` | first candidate model \(\mathcal X_T^{(1)}\) | `partial` | `107_62` and `107_79` exact-audit the finite visible incidence and candidate-envelope coherence shadows |
| III-B | `107_16` | compactified framed square and boundary line | `partial` | `107_61` exact-audits the finite common-corner receiver shadow |
| III-C | `107_17` | local chart atlas and finite-type criterion | `partial` | `107_60` exact-audits the finite local-atlas and finite-type shadow |
| III-D | `107_18` | visible rooted/cyclotomic packet coordinate | `partial` | `107_59` exact-audits the finite visible framing-coordinate shadow |
| III-E | `107_19` | packetwise bridge to determinant lines | `partial` | `107_58` exact-audits the finite packet-to-cyclotomic bridge shadow |
| III-F | `107_20` | local packet line splits as cyclotomic line times norm-one rooted unit | `partial` | `107_42` exact-audits the local finite algebra model |
| III-G | `107_21` | global descent of local packet lines on \(\mathcal X_T^{(1)}\) | `partial` | `107_44` and `107_72` exact-audit the finite cocycle and glued-line-object shadows |
| III-H | `107_22` | candidate adelic metrized realization | `partial` | `107_57` and `107_73` exact-audit the finite packaging and intrinsic-adelic-class shadows |
| III-I | `107_23` | chartwise adelic integrability criterion | `partial` | `107_45` and `107_74` exact-audit the finite logarithmic and intrinsic integrability-profile shadows |
| III-J | `107_24` | primitive degree-zero reduction | `partial` | `107_46` exact-audits the finite primitive degree-zero shadow |
| III-K | `107_25` | first polarization intersection identities | `partial` | `107_46` and `107_47` exact-audit the finite denominator bookkeeping shadow |
| III-L | `107_26` | exceptional-correction control | `partial` | `107_47` exact-audits the finite correction-sum architecture |
| III-M | `107_27` | local exceptional-center audit | `partial` | `107_46` and `107_47` exact-audit the finite center-channel shadow |

## 3. Exact content now secured

At the Paper C level, the current exact audit layer is still narrow but
real.

1. `107_63` and `107_86` exact-audit the finite `107_10` shadows:
   base truncation loses prime channels, genus-zero envelopes lose the
   degree-one carrier, ruling collapse destroys visible
   diagonal/transpose structure, and absolutely continuous completions
   erase the point/resonance classes needed later in Part III; moreover,
   the same full-base, degree-one, two-ruling, discrete architecture is
   now exact-audited as one assembled finite-support realization shadow
   carrying the coherent candidate envelope and target-side package.
2. `107_48`, `107_49`, `107_78`, `107_82`, `107_87`, and `107_89` exact-audit the finite realization
   shadows behind `107_11`: radical modes may die only through the
   explicit Weil radical after realification, non-radical witnesses
   survive, the visible pairing-transport logic is bilinear and radical
   compatible in one finite model, and primitive correction lands the
   visible realization shadow in exact degree zero with finite critical
   scaling preserving that status; moreover, the visible candidate
   target package can assemble that realization together with one
   intrinsic receiver channel and one metric profile on one common
   cover, and the resulting intrinsic package retains visible
   point/resonance classes instead of collapsing them into a continuous
   completion shadow, while still remaining sensitive to genuine
   moved-divisor positions modulo the explicit radical shadow.
3. `107_62` and `107_79` exact-audit the finite candidate-model
   shadows behind `107_15`: the visible incidence locus really contains
   the diagonal, both rulings, and the graph generators without
   collapsing them, and those visible components fit one coherent
   candidate envelope with one common corner receiver and one finite
   regularization-center list.
4. `107_61` exact-audits the finite compactified-square shadow behind
   `107_16`: the common corner is a real shared receiver for boundary,
   diagonal, and graph data in the visible model.
5. `107_60` exact-audits the finite local-atlas shadow behind `107_17`:
   the visible chart transitions, diagonal equations, graph equations,
   chartwise finite-type reduction, and corner generator all remain
   symbolically consistent.
6. `107_59` exact-audits the finite framing-coordinate shadow behind
   `107_18`: the visible rooted dual really factors through finite
   order-dividing character packets and supports finite combinatorial
   graph equations.
7. `107_58` exact-audits the finite bridge shadow behind `107_19`:
   rooted packet labels leave both the prime-power support law and the
   off-diagonal cyclotomic norm unchanged in the visible window, while
   the diagonal still remains in excess-intersection territory.
8. `107_42` exact-audits the finite local algebra behind `107_20`:
   rooted labels act as rank-one norm-one packet factors and preserve
   the cyclotomic resultant norm off the diagonal.
9. The same verifier also exact-audits that packet refinement leaves the
   diagonal in vanishing/excess-intersection territory rather than
   creating a fake finite scalar.
10. `107_44` and `107_72` exact-audit the finite descent shadow behind
   `107_21`:
   the rooted transition system forms a connected groupoid over each
   off-diagonal order pair, satisfies the cocycle condition on all
   composable triples in the visible window, yields a route-independent
   descended section, remains compatible with the visible finite
   action \(\mu_r\), and defines a representative-independent glued
   quotient line object stable under visible gauge re-trivialization.
11. `107_45` and `107_74` exact-audit the finite `107_23` shadows: the
   logarithmic local template is stable under the chart transitions of
   `107_17`, remains additive under tensor packaging, introduces no
   stronger-than-log singular support in the normal-crossings model,
   and the visible chart/root presentations determine one intrinsic
   integrability profile on the divisor slots
   \((B_{\rm v}, B_{\rm h}, \Delta)\).
12. `107_57` and `107_73` exact-audit the finite `107_22` shadows:
   the candidate realized object is additive in generator coefficients,
   uses one archimedean receiver channel, ignores rooted refinements at
   the packaging level, remains compatible with the primitive
   correction protocol, and its visible chart/root presentations define
   one intrinsic quotient-class shadow rather than several local
   packages.
13. `107_69` and `107_90` exact-audit the finite load-bearing shadows
   behind the same candidate package: fixed finite-rank algebraic
   storage creates non-radical collisions, sufficiently rich Green-side
   data separate them, and the current intrinsic finite-support package
   retains its visible faithfulness only while those separating Green
   channels remain available.
14. `107_46` exact-audits the finite symbolic shadow behind `107_24`:
   the primitive coefficient is the unique linear degree-zero
   correction once \(h_T\neq0\), the denominator bookkeeping of
   `107_25` is algebraically consistent, and the visible
   corner-preserving center types of `107_27` act only through the
   exceptional correction channels.
15. `107_47` exact-audits the finite quantitative shadow behind
   `107_25`--`107_27`: the correction package aggregates additively over
   the finite center list, boundary-only centers do not alter the corner
   term directly, and cancellation of \(-2c_T\) is a genuinely signed
   numerical equality rather than a structural consequence of the center
   types.

## 4. What remains unaudited

The following transitions remain theorem-level only.

1. Finite cocycle/glued-line-object shadows \(\rightarrow\) actual global
   line object on \(\mathcal X_T^{(1)}\).
2. Finite universal-model exclusions and assembled realization shadows
   \(\rightarrow\) true existence of a universal finite model.
3. Finite kernel/pairing-transport/degree-zero/assembly shadows \(\rightarrow\) true
   Picard/Jacobian or adelic realization with exact kernel
   \(\ker=\mathfrak R_W\).
4. Global line object \(\rightarrow\) genuine Deligne pairing or adelic
   analogue.
5. Finite candidate-model incidence/envelope shadows \(\rightarrow\)
   true regular proper candidate surface.
6. Finite compactified-square receiver logic \(\rightarrow\) true
   boundary metric descent and global compactification.
7. Finite local-atlas equations \(\rightarrow\) true algebraic gluing of the
   compactified square.
8. Finite visible framing coordinate \(\rightarrow\) true global chart
   gluing on \(\overline{\mathfrak P}_{\rm fr}\).
9. Finite packet-to-cyclotomic bridge \(\rightarrow\) true packet
   intersection line and global comparison morphism.
10. Finite packaging/intrinsic-class shadows \(\rightarrow\) true
   adelic Picard class.
11. Finite logarithmic/integrability-profile shadows \(\rightarrow\)
   actual analytic coefficients and globally integrable metric.
12. Finite primitive degree-zero bookkeeping \(\rightarrow\) actual
   geometric nonvanishing and numerical generator-vs-polarization
   intersections.
13. Finite correction-sum architecture \(\rightarrow\) actual geometric
   signs and magnitudes of the exceptional correction package.
14. Candidate metrized class \(\rightarrow\) faithful Picard/Jacobian
   realization with exact kernel control.
15. Candidate polarization identities \(\rightarrow\) terminal identity
   of `107_13`.

## 5. Promotion rule

No later forward paper in Part III may by itself promote `107_20`,
`107_21`, or any of `107_22`--`107_27` beyond the statuses recorded
here.  Any future promotion must come from a new audit artifact that can
fail on a specific finite shadow or arithmetic witness, not from
additional forward construction alone.
