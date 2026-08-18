# D.200 — Correct three-block Feshbach algebra and the missing safe-tail term

## Verdict

The finite certificate D.199 is valid.  It cannot be joined to the
`V_200`-complement gap by computing only the continuum residual of the final
two-dimensional Schur graph.  A third block is present:

\[
 \mathcal P_T=D\oplus S\oplus Q,                       \tag{0.1}
\]

where `D` is the slow finite block, `S` the finite safe block and `Q` the
infinite primitive complement.  The coupling `S<->Q` must be shorted before
the final slow test.

This exposes a logical omission in the D.172/D.181 endpoint template: the
claimed implication

\[
 QAQ\ge\delta Q,quad K_D-\delta^{-1}H_D>0
 \quad\Longrightarrow\quad A>0                         \tag{0.2}
\]

is valid only if `Q` denotes the complement of the *entire finite block*, or
if the eliminated safe block is known to have zero coupling to the infinite
tail.  In D.181 the gap theorem applies to the complement of `V_200`, while
the later symbol `Q=I-P_D` also contains the 193 eliminated finite
directions.  Those are not the same projection.  No theorem there proves
the missing safe-tail condition.

The corrected criterion below is exact and supplies the next computation
for `T=log(6)/2`.  No paper file is modified.

## 1. Exact block algebra

Write the self-adjoint form as

\[
 A=\begin{pmatrix}
 A_{DD}&A_{DS}&A_{DQ}\\
 A_{SD}&A_{SS}&A_{SQ}\\
 A_{QD}&A_{QS}&A_{QQ}
 \end{pmatrix}.                                        \tag{1.1}
\]

Assume

\[
 A_{SS}>0,\qquad A_{QQ}\ge\delta I_Q.                 \tag{1.2}
\]

Short the safe block first.  Put

\[
 \begin{aligned}
 K_D&=A_{DD}-A_{DS}A_{SS}^{-1}A_{SD},\\
 C_D&=A_{DQ}-A_{DS}A_{SS}^{-1}A_{SQ},\\
 Q_S&=A_{QQ}-A_{QS}A_{SS}^{-1}A_{SQ}.                 \tag{1.3}
 \end{aligned}
\]

The exact congruence

\[
 \begin{pmatrix}I&-A_{DS}A_{SS}^{-1}&0\\0&I&0\\0&-A_{QS}A_{SS}^{-1}&I\end{pmatrix}
 A
 \begin{pmatrix}I&0&0\\-A_{SS}^{-1}A_{SD}&I&-A_{SS}^{-1}A_{SQ}\\0&0&I\end{pmatrix}
 =\begin{pmatrix}K_D&0&C_D\\0&A_{SS}&0\\C_D^*&0&Q_S\end{pmatrix}       \tag{1.4}
\]

shows that all three expressions in (1.3) are forced.  In particular the
post-safe slow vector has a `Q`-component in its image unless `A_SQ=0`.

Define

\[
 \kappa:=\|A_{QS}A_{SS}^{-1/2}\|^2.                  \tag{1.5}
\]

Then

\[
 A_{QS}A_{SS}^{-1}A_{SQ}\le\kappa I_Q,qquad
 Q_S\ge(\delta-\kappa)I_Q.                            \tag{1.6}
\]

Therefore the following is a sufficient directed certificate:

\[
 \boxed{
 A_{SS}>0,quad \kappa<\delta,quad
 K_D-(\delta-\kappa)^{-1}C_DC_D^*>0.}                 \tag{1.7}
\]

Equations (1.4)--(1.7) are also valid for closed forms by the standard
bounded-form Schur argument on the indicated finite ranges.

## 2. Simultaneous elimination form

Let `V=D direct-sum S` and

\[
 B=V^*AV,qquad R=(QAV)^*(QAV).                        \tag{2.1}
\]

From `QAQ>=delta Q`, completion of the square gives

\[
 A\ge0\quad\text{if}\quad B-\delta^{-1}R\ge0.         \tag{2.2}
\]

This is the safest computational version: it retains the full residual
Gram, including

\[
 R=\begin{pmatrix}R_{DD}&R_{DS}\\R_{SD}&R_{SS}\end{pmatrix}.       \tag{2.3}
\]

The missing `R_SS` and `R_DS` are exactly the safe-tail and corrected-cross
data absent from a slow-graph-only calculation.

If forming (2.3) densely is undesirable, a trace gate is sufficient.  For
`A_SS>0`,

\[
 \kappa\le
 \operatorname {tr}(A_{SS}^{-1}R_{SS}).               \tag{2.4}
\]

After proving the right side smaller than `delta`, compute `C_D C_D^*`
directly from the contracted columns in (1.3).  Formula (2.4) is the
correct use of the safe trace mechanism proposed in D.165.

## 3. Scalar counterexample to the shortcut

Take one-dimensional blocks and

\[
 A=\begin{pmatrix}1&0&0\\0&1&2\\0&2&1\end{pmatrix}.              \tag{3.1}
\]

The finite `D direct-sum S` compression is positive and the raw `Q` block
has gap `delta=1`.  Eliminating `S` inside the finite compression leaves
`K_D=1`.  The slow graph has zero coupling to `Q`, so the shortcut (0.2)
reports `1>0`.

Nevertheless the `S direct-sum Q` block has eigenvalues `3,-1`; hence (3.1)
is indefinite.  Here

\[
 \kappa=4>\delta,                                      \tag{3.2}
\]

and the correct test (1.7) rejects the example immediately.  This proves
that the omitted term is logically indispensable, not merely a sharper
numerical refinement.

## 4. Consequence for the former first-endpoint certificate

D.152 proves a gap on the primitive complement of `V_200`.  D.166 then
eliminates two finite safe blocks and retains a five-dimensional graph.
D.172 controls the continuum action only on those five graph columns.
Those facts do not prove a gap on the orthogonal complement of the
five-dimensional graph, because that complement also contains the finite
safe blocks.  The assertion in D.181 that the D.152 gap applies after this
change of projection is therefore unsupported.

Accordingly D.181 must be read as a finite-plus-slow-residual certificate,
not yet as a complete infinite-dimensional endpoint theorem, until either

1. the full residual Gram (2.3) is enclosed, or
2. the safe trace bound (2.4) and corrected cross of (1.3) are enclosed.

This correction does not affect D.199, which asserts positivity only on
`V_200` and explicitly leaves the infinite complement open.

## 5. Correct `T=log(6)/2` target

D.185 supplies

\[
 A_{QQ}>0.219 I_Q                                      \tag{5.1}
\]

for the primitive `V_200` complement.  D.199 supplies the exact finite
matrix.  A numerically stable split should place at least the first eight
finite Ritz directions in `D`; the next safe midpoint value is about
`0.5045`, whereas with only two slow directions the safe block starts at
`1.80e-11` and gives no useful safe-tail budget.

For `D_8 direct-sum S_190 direct-sum Q_200`, the remaining obligations are

\[
 \begin{aligned}
 \kappa_8
 &=\|A_{QS}A_{SS}^{-1/2}\|^2<0.219,\\
 C_8
 &=A_{DQ}-A_{DS}A_{SS}^{-1}A_{SQ},\\
 K_8-(0.219-\kappa_8)^{-1}C_8C_8^*&>0.                \tag{5.2}
 \end{aligned}
\]

All factors in (5.2) are source-defined and contain the complete Gamma term
and all active prime powers.  The cancellation-free endpoint-log action of
D.172 can evaluate the eight corrected columns.  The genuinely new item is
the relative safe action bound `kappa_8`; a rank or raw Hilbert--Schmidt norm
without the `A_SS^{-1/2}` weight does not prove (5.2).
