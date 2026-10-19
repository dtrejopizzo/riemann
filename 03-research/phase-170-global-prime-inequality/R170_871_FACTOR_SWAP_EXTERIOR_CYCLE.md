# R170_871 — Odd cycle from factor swap and exterior flow

> **Audit R170_872.** The multiplicative cycle and the flow formulas
> of this record are correct. The operator class of the flow is not
> new: it coincides with the support concomitant of R161_057 and R161_064
> after polarizing the two syntheses. The novelty is limited to realizing
> that concomitant as an observation of the `d<->m` cycle and to locating there
> the arithmetic oddness. The required Tate/exterior reciprocity remains
> exactly R161_064(4.2)--(4.3), now in route coordinates.

## 0. Result

R170_870 shows that the boundary-augmented class `beta_phys` is odd and cannot be
oriented by even minimality without an additional coupling. Integer
factorization supplies a canonical odd involution:

\[
 \iota(d,m)=(m,d).                                        \tag{0.1}
\]

On the full space, the two readings of the hyperbola coincide because
the causal translations commute:

\[
 L S=S L.                                                  \tag{0.2}

After inserting the window `P` and its exterior `Q=I-P`, the equality
decomposes into an exact flow law:

\[
\boxed{
 PLQSP-PSQLP
 =-\bigl(PLPSP-PSPLP\bigr).}                              \tag{0.3}
\]

The left-hand side is an oriented exterior flow; the right-hand side is the
commutator of the interior compressions. Both change sign under the
swap `L <-> S`.

The two-scale derivative of (0.3) produces the exterior version of the
Wronskian `dot L S-L dot S`. This explicitly realizes, via
factorization, the odd channel the corpus already knew as the support
concomitant.

The identity does not yet close the sign: the compressed commutator is
self-adjoint only after multiplying by `i`, and its real diagonal is
zero when the factors are self-adjoint, while `L,S` are causal and
not self-adjoint. The Tate/polar concomitants are still needed.
But (0.3) identifies a symmetry acting on the port, not only on
the coefficients.

## 1. Two oriented anchors

On the route space `(d,m)` define the two assignments

\[
 x^L_{d,m}={\Lambda(d)\over\sqrt{dm}},
 \qquad
 x^R_{d,m}={\Lambda(m)\over\sqrt{dm}}.                     \tag{1.1}
\]

On each fiber `k=dm`,

\[
 \sum_{dm=k}x^L_{d,m}
 =\sum_{d\mid k}{\Lambda(d)\over\sqrt k}
 ={\log k\over\sqrt k},                                   \tag{1.2}
\]

and, swapping `d` for `m`,

\[
 \sum_{dm=k}x^R_{d,m}={\log k\over\sqrt k}.               \tag{1.3}

Hence both orientations give the same Chebyshev column. Their
difference

\[
 \omega_\Lambda:=x^L-x^R                                 \tag{1.4}

is an incidence cycle:

\[
 \sum_{dm=k}(\omega_\Lambda)_{d,m}=0.                     \tag{1.5}

Moreover,

\[
 \iota\omega_\Lambda=-\omega_\Lambda.                    \tag{1.6}

This is a specifically arithmetic odd class. For a general sequence `a`,
the same cycle exists formally, but the coupling with the fixed
column `log` is zero at every cut only for `a=Lambda`, by R170_866.

## 2. The full observation kills the cycle

Associate to a route the operator

\[
 \tau_{\log d}\tau_{\log m}=\tau_{\log(dm)}.              \tag{2.1}

Summing (1.4),

\[
 \sum_{d,m}{\Lambda(d)-\Lambda(m)\over\sqrt{dm}}
 \tau_{\log(dm)}=0                                        \tag{2.2}

on every symmetric route cut. In comb language, (2.2) is
`LS-SL=0`.

Thus the observation that forgets the intermediate point of the factorization
kills the odd cycle. To detect it one must observe whether the trajectory
crosses the boundary after the first factor.

## 3. Observation through the cut

Let `P=P_T`, `Q=I-P`. Expand

\[
 P(L S-S L)P=0                                             \tag{3.1}

by inserting `I=P+Q` between the factors:

\[
\begin{aligned}
0={}&PLPSP+PLQSP\\
   &-PSPLP-PSQLP.                                          \tag{3.2}
\end{aligned}

Rearranging proves (0.3).

Define

\[
 \Phi_{\rm ext}(L,S):=PLQSP-PSQLP,                        \tag{3.3}
\]

\[
 \Phi_{\rm int}(L,S):=PLPSP-PSPLP.                        \tag{3.4}

Then

\[
 \boxed{\Phi_{\rm ext}+\Phi_{\rm int}=0,}                \tag{3.5}
\]

and

\[
 \Phi_\bullet(S,L)=-\Phi_\bullet(L,S).                   \tag{3.6}

The identity preserves the order of the routes and uses no adjunction through
`P`.

## 4. Antidiagonal derivative

Use the two scales of R170_847 and set

\[
 \mathcal W(r,q):=L(r)S(q).                                \tag{4.1}

Its antidiagonal derivative is

\[
 \partial_-\mathcal W(1,1)
 =\dot L S-L\dot S=\mathcal A^{\rm raw}.                  \tag{4.2}

The reading with the intermediate point observed is

\[
 \Phi_{\rm ext}(r,q):=PL(r)QS(q)P-PS(q)QL(r)P.            \tag{4.3}

Differentiating,

\[
\boxed{
\begin{aligned}
 \partial_-\Phi_{\rm ext}|_{1,1}
 ={}&P\dot LQSP-PLQ\dot SP\\
   &+P\dot SQLP-PSQ\dot LP.
\end{aligned}}                                             \tag{4.4}

The last two signs come from `-partial_q` applied to the second
orientation. Differentiating (3.5) gives

\[
 \partial_-\Phi_{\rm ext}
 =-\partial_-\Phi_{\rm int}.                              \tag{4.5}

On the other hand, inserting `P+Q` in `P mathcal A^{raw}P` separates exactly
the two routes of the first line of (4.4). The second line is the copy
with the factors swapped. Thus (4.4) is the odd polarization of the
Wronskian with respect to the intermediate point.

## 5. Relation to the boundary-augmented class

The exterior of R170_853 is encoded by

\[
 q=QS^*Ph,\qquad z=QAF-\rho q.                             \tag{5.1}

Its Wronskian

\[
 (\dot q,z)-(q,\dot z)                                    \tag{5.2}

is also odd under swapping the two orientations of the flow. The Green
law of R170_854 shows that (5.2) is the exterior part of the full
PC curvature.

Equation (4.4) provides the route representative that was missing in the
quotient decomposition of R170_869. To identify it exactly with
`beta_phys` one must still add:

* the reflected orientation `J`;
* the polar continuum;
* the primitive/Tate connection;
* the causal extraction `B_mu`.

R170_856 already gives the ledger of these pieces. What is new here is that
the main channel has an odd involution before recombination.

## 6. Why antisymmetry alone does not kill the flow

A quantity odd under `L <-> S` is not zero in the physical system, because
the system distinguishes the factors: `L` carries `Lambda` and `S` carries
`mathbf1`. The involution sends the system to its opposite orientation, it does
not leave it pointwise fixed.

To force vanishing one would need an additional identification between the
two orientations in the boundary-augmented port. Full commutativity gives that
identification after forgetting the intermediate point, but the cut
turns it exactly into (3.5), not into `Phi_ext=0`.

Likewise, (3.5) holds for many general weights and does not by itself use
`a=Lambda`. The specificity enters by requiring that both orientations
share the same Chebyshev column `log` at every cut.

## 7. Remaining minimal bilateral law

Define the full PC flow `Phi_PC` by adding to (4.4) the reflected, polar, and
Tate terms of the R170_856 ledger. The sought law can now be
formulated as

\[
 \boxed{
 \operatorname{Res}_{(\Lambda,1)}\Phi_{PC}(F)=0
 \quad(F\in\ker H_T),}                                    \tag{7.1}

where `Res_(Lambda,1)` is the quotient class of R170_869.

Equation (7.1) is exactly `beta_phys(F)=0`, but it adds structure:
its principal representative is the odd flow of the factor-swap
cycle. A new proof must show that the interior identification
(3.5), together with minimality, extends the involution to the Tate port.

No such extension is claimed here.

## 8. Status

```text
two oriented anchors share the log column                  PROVED
cycle omega_Lambda vanishes fiberwise and is odd under swap PROVED
full observation kills the cycle                            PROVED
P/Q cut produces exterior flow (0.3)                         PROVED
antidiagonal derivative of the flow, (4.4)                   PROVED
odd channel prior to recombination                           REALIZED / CLASS ALREADY IN R161
full identification with beta_phys                           PARTIAL / R170_856 LEDGER
minimality forces odd flow to vanish                         OPEN
VIR--LB / D                                                  OPEN
```
