# P121 -- opposite-parity rigidity of the causal Tate port

## Status

This note proves a new finite-window rigidity lemma.  The one-sided causal
Euler observation of a nonzero Tate forcing cannot have the parity opposite
to that forcing.  The proof is exact on the prime-free collar and on the
integer activation cells of the reflected collar.

Combined with `P121_GRAPH_RENORMALIZED_INCOMING_CURRENT.md`, it shows that
any genuine cross-port matching which produces opposite parity forces the
Tate multiplier, and hence the completed incoming current, to vanish.
`P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT.md` proves that ordinary Real
covariance alone does **not** produce that matching: it relates two distinct
causal currents.

This does not yet prove that the physical cross-port matching holds, nor
does it exclude a homogeneous primitive zero mode after the Tate multiplier
has vanished.  The global square remains open.

## 1. Causal Tate images

Fix `T>log 2`, put `I_T=(-T,T)`, and let

\[
 r_\varepsilon(t)
 =c\bigl(e^{t/2}+\varepsilon e^{-t/2}\bigr),
 \qquad \varepsilon\in\{+1,-1\}.                  \tag{1.1}
\]

Thus `r_epsilon(-t)=epsilon r_epsilon(t)`; normalization of `cosh` and
`sinh` is absorbed in `c`.  Extend `r_epsilon` by zero outside `I_T` and
write

\[
 k_\varepsilon
 :=\mathcal Z_{T,+}r_\varepsilon,
 \qquad
 (\mathcal Z_{T,+}f)(t)
 =\sum_{n\ge1}n^{-1/2}E_Tf(t-\log n).              \tag{1.2}
\]

The sum is finite at every `t in I_T`.

## 2. Collar formula

For `x in (T-log 2,T)`, away from the finite set of activation points
`x=log m-T`, put

\[
 M(x):=\#\{n\in\mathbb N:n<e^{x+T}\},
 \qquad H_M:=\sum_{n=1}^{M}{1\over n}.             \tag{2.1}
\]

Then

\[
 \boxed{
 \begin{aligned}
 k_\varepsilon(-x)
   &=c\bigl(\varepsilon e^{x/2}+e^{-x/2}\bigr),\\
 k_\varepsilon(x)
   &=c\bigl(e^{x/2}H_{M(x)}
          +\varepsilon e^{-x/2}M(x)\bigr).
 \end{aligned}}                                    \tag{2.2}
\]

Indeed, at `-x in (-T,-T+log 2)` every delay `log n>=log 2` exits the
window, so only `n=1` remains.  At `x`, a summand is active exactly when
`n<e^(x+T)`, and

\[
 n^{-1/2}r_\varepsilon(x-\log n)
 =c\bigl(e^{x/2}n^{-1}
       +\varepsilon e^{-x/2}\bigr).                \tag{2.3}
\]

Summation gives (2.2).

## 3. Opposite-parity exclusion

### Theorem 3.1 -- causal Tate port has a nonzero same-parity component

For `T>log 2`,

\[
 \boxed{
 \mathcal Rk_\varepsilon=-\varepsilon k_\varepsilon
 \quad\Longrightarrow\quad c=0.}                  \tag{3.1}
\]

Equivalently, for every nonzero Tate forcing,

\[
 P_\varepsilon\mathcal Z_{T,+}r_\varepsilon\ne0,
 \qquad P_\varepsilon={1\over2}(I+\varepsilon\mathcal R).
                                                               \tag{3.2}
\]

#### Proof

Opposite parity says, for almost every `x in (T-log 2,T)`,

\[
 k_\varepsilon(x)+\varepsilon k_\varepsilon(-x)=0. \tag{3.3}
\]

Substitution of (2.2) gives

\[
 c\left[
 e^{x/2}(H_{M(x)}+1)
 +\varepsilon e^{-x/2}(M(x)+1)
 \right]=0.                                         \tag{3.4}
\]

If `epsilon=+1`, the bracket is strictly positive, so `c=0`.

Suppose `epsilon=-1` and `c` is nonzero.  Equation (3.4) becomes

\[
 e^x={M(x)+1\over H_{M(x)}+1}                       \tag{3.5}
\]

for almost every `x` in the collar.  The activation points form a finite
set there, and their complement is a nonempty union of open intervals.  On
each such interval `M(x)` is constant, so the right side of (3.5) is
constant while the left side is strictly increasing.  Equality cannot hold
almost everywhere on any one of these intervals.  This contradiction proves
`c=0`.  QED.

### Corollary 3.2 -- a cross-port matching kills the Tate current

Let `F` be a parity first-contact state and let

\[
 \mathcal L^{\rm gr}_{T,-}(F)
 =-\mathcal Z_{T,+}r_\varepsilon                  \tag{3.6}
\]

be its graph-renormalized incoming current.  If an independently constructed
physical cross-port law implies

\[
 \mathcal R\mathcal Z_{T,+}r_\varepsilon
 =-\varepsilon\mathcal Z_{T,+}r_\varepsilon,       \tag{3.7}
\]

then

\[
 r_\varepsilon=0,
 \qquad \mathcal L^{\rm gr}_{T,-}(F)=0.            \tag{3.8}
\]

#### Proof

Theorem 3.1 gives `c=0` in (1.1), hence both conclusions.  QED.

## 4. Exact scope

Equation (3.7) is not inferred from scalar conservation or ordinary Real
covariance.  The latter gives only the relation between the distinct plus
and minus currents written in
`P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT.md` (1.3).  Equation (3.7) would
require an additional physical identification before scalar supertrace.

The gain is a sharp falsifiable consequence: any future matching which does
imply (3.7) has its Tate component annihilated automatically.  This note is
not evidence that such a matching exists.  The remaining homogeneous problem is

\[
 F\in\mathcal P_T,\qquad P_T\mathcal A_\infty F=0,
 \qquad \mathcal L^{\rm gr}_{T,-}(F)=0
 \quad\Longrightarrow?\quad F=0.                  \tag{4.1}
\]

That implication is not proved here.  In particular, killing the finite
Tate terminal must not be reported as annular vanishing of
`h=mathcal Z_(T,+)F`.
