# D.79 supplement — one-mode Feshbach bound at a tangential endpoint

## Status

At a nearly tangent endpoint an operator-norm bound on the entire
`P--Q` cross block is too expensive.  The sign is controlled by one low
mode, so the relevant quantity is the residual of that mode.  This note
records the exact block lemma used for that reduction.

## Lemma

Let `A` be self-adjoint, let `v` be a unit vector, and decompose

\[
 H=\mathbb Cv\oplus v^\perp,
 \qquad
 A=\begin{pmatrix}\mu&r^*\\r&D\end{pmatrix}.            \tag{1}
\]

Assume

\[
 D\geq gI,qquad \|r\|\leq\varepsilon.                 \tag{2}
\]

Then

\[
 \boxed{
 A\geq\lambda_-I,qquad
 \lambda_-={\mu+g-
 \sqrt{(g-\mu)^2+4\varepsilon^2}\over2}.}              \tag{3}
\]

In particular, if `g>0`,

\[
 \lambda_-\geq \mu-{arepsilon^2\over g-\mu}
 \quad\hbox{whenever }\mu<g.                            \tag{4}
\]

The exact formula (3), rather than (4), should be evaluated by directed
interval arithmetic.

### Proof

For `lambda<g`, the Schur complement of `D-lambda` gives

\[
 A-\lambda I\geq0
 \quad\Longleftarrow\quad
 \mu-\lambda-{\varepsilon^2\over g-\lambda}\geq0.      \tag{5}
\]

Equality in (5) is

\[
 (\mu-\lambda)(g-\lambda)-\varepsilon^2=0,             \tag{6}
\]

whose smaller root is (3).  The scalar two-dimensional matrix with
off-diagonal `epsilon` shows sharpness.

## Residual interpretation

The cross vector in (1) is

\[
 r=(I-|v\rangle\langle v|)Av,
 \qquad \mu=\langle v,Av\rangle.                       \tag{7}
\]

Thus only the residual of the selected low vector is needed.  A uniform
bound on `||(I-P)AP||` controls every vector in a large Galerkin space and
can be many orders of magnitude larger than (7).

For the `T=log(2)` application, `v` must be stored as a rational or ball
vector; `mu`, `epsilon`, and the complementary gap `g` must all be bounded
outward.  A floating eigenvector may select `v` but has no evidentiary
role until enclosed.

The exact root and a sharp rational matrix example are checked in
`114_d_79_directed_one_mode_feshbach_verify.py`.

