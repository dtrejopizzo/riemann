# D.154 — Preconditioned Feshbach graph certificate

## Verdict

At the first endpoint (T=\frac12\log 5), the exact pullback of the
two Tate jets gives the two primitive moments of A--B--C, and the primitive
operator contains, in one self-adjoint form, every finite contact
(p^k\le e^{2T}) and the complete Gamma contribution.  The ordinary
estimate

\[
 B-\delta^{-1}C^*C\ge0
\]

is rigorous but too wasteful: it destroys the cancellation between the
finite contacts and Gamma before the high-frequency inverse is applied.
The correct certificate is the preconditioned graph identity below.  It
keeps that cancellation exact and leaves only a squared *preconditioned*
residual.

The numerical Lanczos audit selects a positive target near
(3.07629\times10^{-12}).  This number is not used as proof.  The remaining
directed task is to enclose the finite graph and its residual by intervals.
No statement in the paper is changed by this note.

## 1. Exact graph identity

Let (A) be the self-adjoint primitive operator and decompose the primitive
Hilbert space as (H=W\oplus W^\perp).  In this decomposition write

\[
 A=\begin{pmatrix}B&C^*\\ C&D\end{pmatrix},
 \qquad D\ge\delta I,
 \qquad \delta>0.                                      \tag{1.1}
\]

For any bounded trial graph (X:W\to W^\perp), put

\[
 R=C-DX.                                                \tag{1.2}
\]

Since (C=DX+R), direct expansion gives the exact identity

\[
 C^*D^{-1}C
 =X^*C+C^*X-X^*DX+R^*D^{-1}R.                         \tag{1.3}
\]

Consequently the exact Schur complement satisfies

\[
\begin{aligned}
 B-C^*D^{-1}C
 &=B-X^*C-C^*X+X^*DX-R^*D^{-1}R\\
 &\ge B-X^*C-C^*X+X^*DX-\delta^{-1}R^*R.              \tag{1.4}
\end{aligned}
\]

Thus the following directed inequalities imply (A\ge0):

\[
 D\ge\delta I,
 \qquad
 B-X^*C-C^*X+X^*DX-\delta^{-1}\widetilde R\ge0,
 \qquad
 \widetilde R\ge R^*R.                               \tag{1.5}
\]

Unlike the unpreconditioned estimate, (1.5) becomes exact when
(X=D^{-1}C).  This is the mechanism needed at the (10^{-12}) margin.

## 2. A finite auxiliary graph

Let (S:\mathbb C^n\to W) synthesize the directed low frame and let
(Y:\mathbb C^m\to W^\perp) synthesize an auxiliary high frame.  Write

\[
 G_Y=Y^*Y,
 \quad D_Y=Y^*AY,
 \quad C_Y=Y^*AS.                                     \tag{2.1}
\]

After orthonormalizing (Y), the Galerkin graph is

\[
 X_Y=Y D_Y^{-1}C_Y.                                    \tag{2.2}
\]

All entries in (2.1) are evaluations of the same complete primitive form.
They therefore include the contacts (p^k) and Gamma *before* any norm or
absolute value is taken.  The finite part of (1.4) is a directed congruence.
Only

\[
 R_Y=(I-YY^*)\bigl(AS-AYD_Y^{-1}C_Y\bigr)              \tag{2.3}
\]

must be bounded outside the auxiliary graph.  Increasing the Krylov or
nested Legendre graph reduces (2.3), rather than merely adding an
unweighted tail estimate.

For a nonorthogonal auxiliary frame, replace (YY^*) by
(Y G_Y^{-1}Y^*) throughout.  This change is algebraic and does not alter
(1.3).

## 3. Why the coarse residual is not decisive

For the lowest (N=170) Ritz vector, a high-resolution Fourier stress test
of the full multiplier gives approximately

\[
 \langle Av,v\rangle=3.11434\times10^{-12},
 \qquad \|Av\|^2=2.827135696445\times10^{-1}.           \tag{3.1}
\]

The large second number is compatible with positivity: most of the residual
lies at high multiplier values and is strongly suppressed by (D^{-1}).
Replacing (D^{-1}) by the scalar (\delta^{-1}) loses precisely this
suppression.  Hence failure of the coarse bound is not evidence of a
negative direction.

A fully reorthogonalized Lanczos calculation for the same complete
multiplier and the exact two-moment projection gives the successive lowest
Ritz values

\[
\begin{array}{c|c}
\text{steps}&\text{lowest Ritz value}\\ \hline
10&3.07712738\times10^{-12}\\
30&3.07683375\times10^{-12}\\
60&3.07629211\times10^{-12}\\
90&3.07629211\times10^{-12}.
\end{array}                                            \tag{3.2}
\]

This stable positive value selects the interval target and shows that a
small graph already captures the relevant resolvent correction.  Because
the computation in (3.2) is floating point, it is an audit only.

## 4. Directed endpoint certificate still required

The first endpoint is closed once the following finite data are enclosed:

1. a directed interval basis for (W_{170}=P_TL_{170});
2. a directed auxiliary graph (X_Y) assembled from the joint
   finite-contact--Gamma operator;
3. an interval lower bound for the graph matrix in (1.5);
4. an interval upper bound for (R_Y^*R_Y) below that margin.

D.147 supplies the full Gamma matrix, D.148 the finite contact matrix,
D.151--D.152 absorb the rank-two Tate defect, and D.150 supplies the exact
pointwise Gamma action needed for the residual.  Formula (1.5) is therefore
the exact remaining bridge from those certified ingredients to positivity
of the complete primitive operator.

## 5. Algebraic verifier

`114_d_154_preconditioned_feshbach_verify.py` verifies (1.3), the directed
inequality in (1.4), and positivity of a nontrivial random example.  It is a
certificate of the algebraic reduction, not of the endpoint interval data.
