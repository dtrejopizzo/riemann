# P121 -- two-port Wronskian and Real-matching audit

## Status

This note audits two tempting continuations of the graph-renormalized
current construction:

1. identify the two reflected causal currents using Real symmetry;
2. use a Wronskian of the two Euler orientations as a new nonlinear
   equality law.

Both calculations are exact.  Neither supplies the missing physical
matching.  The first confuses covariance of two different ports with
opposite parity of one port.  The second is the already known differentiated
meromorphic observation multiplied by a common scalar factor.

## 1. Correct Real covariance of the causal ports

Let

\[
 \mathcal Z_{T,-}:=\mathcal R\mathcal Z_{T,+}\mathcal R,
 \qquad \mathcal RF=\varepsilon F,
 \qquad \mathcal Rr_\varepsilon=\varepsilon r_\varepsilon. \tag{1.1}
\]

The plus and minus graph-renormalized currents are

\[
 \mathcal L^{+,\rm gr}_{T,-}=-\mathcal Z_{T,+}r_\varepsilon,
 \qquad
 \mathcal L^{-,\rm gr}_{T,+}=-\mathcal Z_{T,-}r_\varepsilon. \tag{1.2}
\]

Reflection gives the exact covariance

\[
 \boxed{
 \mathcal L^{-,\rm gr}_{T,+}
 =\varepsilon\mathcal R\mathcal L^{+,\rm gr}_{T,-}.}       \tag{1.3}
\]

Indeed,

\[
 \mathcal Z_{T,-}r_\varepsilon
 =\mathcal R\mathcal Z_{T,+}\mathcal Rr_\varepsilon
 =\varepsilon\mathcal R\mathcal Z_{T,+}r_\varepsilon.
\]

Equation (1.3) relates two different causal boundary values.  It does not
say

\[
 \mathcal R\mathcal Z_{T,+}r_\varepsilon
 =-\varepsilon\mathcal Z_{T,+}r_\varepsilon.        \tag{1.4}
\]

Thus Real covariance alone does not activate the opposite-parity theorem in
`P121_TATE_PORT_OPPOSITE_PARITY_RIGIDITY.md`.  Condition (1.4) would require
an additional physical identification of the two unsupertraced ports.

## 2. Exact two-port Wronskian

Let `G` be an entire compact-source Mellin transform and put

\[
 H_+(s)=\zeta(s)G(s),\qquad
 H_-(s)=\zeta(1-s)G(s).                              \tag{2.1}
\]

Their Wronskian is

\[
 \begin{aligned}
 W(H_+,H_-)(s)
 &: =H_+'(s)H_-(s)-H_+(s)H_-'(s)\\
 &=\zeta(s)\zeta(1-s)G(s)^2
 \left(
   {\zeta'\over\zeta}(s)
  +{\zeta'\over\zeta}(1-s)
 \right).                                           \tag{2.2}
 \end{aligned}
\]

The derivative `G'` cancels exactly.  This is the attractive part of the
construction.

### Proposition 2.1 -- normalized Wronskian contains no witness data

Where the quotient is defined,

\[
 \boxed{
 {W(H_+,H_-)\over H_+H_-}
 ={\zeta'\over\zeta}(s)
  +{\zeta'\over\zeta}(1-s).}                       \tag{2.3}
\]

Hence the normalized Wronskian is independent of `G`.  After Gamma
completion, (2.3) is exactly the differentiated functional equation.

The unnormalized expression (2.2) is the meromorphic differentiated
observation v94 (321) multiplied by the common factor
`zeta(s)zeta(1-s)G(s)`.  It therefore has the same unresolved distinction
between a common meromorphic germ and the two physical boundary values.

#### Proof

Differentiate (2.1).  The two terms containing `G G'` occur with opposite
signs and cancel, leaving (2.2).  Division gives (2.3).  V94 (321) has
multiplier

\[
 -\left({\zeta'\over\zeta}(s)
        +{\zeta'\over\zeta}(1-s)\right)G(s),
\]

so multiplication by `-zeta(s)zeta(1-s)G(s)` gives (2.2).  QED.

## 3. Consequence

Neither mechanism is the missing equality law:

* Real symmetry transports the plus current to a distinct minus current;
  identifying them is additional information, not covariance.
* The two-port Wronskian cancels the source derivative, but after
  normalization it cancels the source itself.  Without normalization it
  merely rescales the already audited meromorphic identity.

Accordingly the remaining source theorem must distinguish the two physical
boundary representatives while retaining nontrivial dependence on the
first-contact witness.  A scalar determinant, Wronskian, normalized ratio,
or reflected covariance cannot do both jobs.

