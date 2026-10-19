# R170_892 — Boundary-augmented KKT and virtual work of the Tate defect

## 0. Result audited twice

The physical product `sigma(F)Delta(F)` has an exact interpretation:
it is the cross work of the normal residual `Delta b` against the normal
velocity of the primitive constraint. However, it is not a Schur complement
of the physical minimality and does not receive its sign.

The first derivation was independent; the second review recomputed the
signs, factors, and an explicit moving counterexample. The delegated
neutral audit could not be run because of a tool usage limit; it was not
replaced by an automatic acceptance.

## 1. First-contact KKT system

In a real parity sector and a fixed-window gauge, use

\[
 \mathscr L_s(F,\alpha,\beta)
 ={1\over2}(F,A_sF)+\alpha(F,b_s)
 +{\beta\over2}(\|F\|^2-1).                              \tag{1.1}
\]

At contact,

\[
 A F=\rho b,\qquad (F,b)=0,\qquad \|F\|=1,\qquad
 \alpha=-\rho,quad\beta=-\lambda=0.                    \tag{1.2}
\]

The linearization is

\[
\boxed{
 \begin{pmatrix}
 A&b&F\\ b^*&0&0\\ F^*&0&0
 \end{pmatrix}
 \begin{pmatrix}\dot F\\\dot\alpha\\\dot\beta\end{pmatrix}
 =
 \begin{pmatrix}
 -\dot A F+\rho\dot b\\ \sigma/2\\0
 \end{pmatrix}.}                                        \tag{1.3}
\]

Indeed `dot alpha=-dot rho`, `dot beta=-nu`, and

\[
 (b,\dot F)=-(\dot b,F)={\sigma(F)\over2}.               \tag{1.4}
\]

With a moving window, (1.3) is written with covariant derivatives and
the first row incorporates `dot P A F`; it is the same connection as
R170_887.

## 2. The defect as virtual work

Suppose a symmetric carrier `W` has Tate port

\[
 R_TWF=(\rho+\Delta)b.                                   \tag{2.1}
\]

The connection of its compression produces exactly

\[
\boxed{
 2\operatorname{Re}(\dot\Pi F,\Delta b)
 =\sigma(F)\Delta(F).}                                   \tag{2.2}
\]

One leg gives

\[
 (\dot F,\Delta b)={\sigma\Delta\over2};                 \tag{2.3}
\]

the two Hermitian legs produce (2.2). In the coordinates
`(sigma,Delta)`, the block is

\[
 \begin{pmatrix}0&1/2\\1/2&0\end{pmatrix},              \tag{2.4}
\]

of signature `(1,1)`. It is a hyperbolic block, not a positive energy.

## 3. Physical Schur complement

Set `mathcal T={F,b}^perp` and decompose

\[
 \dot F=x+{\sigma\over2g}b,\qquad x\in\mathcal T.         \tag{3.1}
\]

If contact is simple and
`H_mathcalT=Q_mathcalT A Q_mathcalT` is invertible and positive on
`mathcal T`, projecting the first row of (1.3) gives

\[
 H_{\mathcal T}x=-y,                                     \tag{3.2}
\]

\[
 y=Q_{\mathcal T}\left[
 \dot A F-\rho\dot b+{\sigma\over2g}Ab\right].           \tag{3.3}
\]

Hence

\[
 x=-H_{\mathcal T}^{-1}y,
 \qquad
 \text{Schur}=-\,(y,H_{\mathcal T}^{-1}y).              \tag{3.4}
\]

Neither `Delta` nor `Omega_EM` appears. Kato's second variation has the
same structure:

\[
 \ddot\lambda=(F,\ddot H F)
 -2(Q\dot H F,RQ\dot H F).                               \tag{3.5}
\]

Inserting the EM defect into (3.4) would require a new operator
identity; doing so would also produce squared and cross terms. Adding a
row `Delta` to the KKT matrix only rewrites the port and does not prove
positivity. The bordered matrix (1.3) is already indefinite because it contains
`2 alpha(b,x)`.

## 4. Counterexample with a moving constraint

In `R^2`, let `(f,b)` be an orthonormal basis and define

\[
 b_s={b+s\kappa f\over\sqrt{1+\kappa^2s^2}},\qquad
 F_s={f-s\kappa b\over\sqrt{1+\kappa^2s^2}}.             \tag{4.1}
\]

In the moving basis, take the self-adjoint operator

\[
 A_sF_s=-sF_s+\rho b_s,\qquad
 A_sb_s=\rho F_s+c b_s.                                  \tag{4.2}
\]

The primitive compression has

\[
 \lambda_s=-s\ge0\quad(s<0),\qquad A_0f=\rho b,          \tag{4.3}
\]

and

\[
 \sigma=2(\dot\Pi f,b)=-2\kappa.                        \tag{4.4}
\]

Choose any symmetric carrier `W_s` with

\[
 R_sW_sF_s=(\rho+\delta)b_s.                             \tag{4.5}
\]

Then `Delta=delta` and

\[
 \sigma\Delta=-2\kappa\delta,                           \tag{4.6}
\]

which can have any sign while `A_s`, its KKT, `lambda_s`, and
minimality remain fixed. The example refutes an abstract inference from
KKT; it does not refute a specific identity of the integers that fixes
`delta`.

## 5. Exact relation to EM

R170_852 proves (2.2) for the Tate defect of the combined carrier. To
write it as

\[
 {\sigma(F)\over g}\Omega_{\rm EM,cov}(F)                \tag{5.1}
\]

one must first prove

\[
 \Omega_{\rm EM,cov}=g\Delta_{\rm tot}.                  \tag{5.2}
\]

R170_885 gives the frozen Wronskian and R170_887 its connections, but
(5.2) for the total ledger remains part of the open law. It is not
derived from KKT.

If (5.2) is granted, `Delta_tot` keeps `U_N`, `R_M`, the continuous
polar incidence, and the branch connections. KKT only multiplies that
scalar by `sigma`; it cancels no tail. Moreover the physical KKT
stabilizes while the auxiliary ports depend on `N`, so an independent
stabilization law is needed before identifying them.

At thresholds the finite collar system with the birth term must be
used; (1.3) does not authorize a derivative that does not exist.

## 6. Status

```text
linearized KKT system                                       PROVED
sigma*Delta as virtual work                                  PROVED
hyperbolic signature of the block                             PROVED
physical Schur complement                                     PROVED UNDER SIMPLE/REG
KKT signs sigma*Delta                                         REFUTED BY COUNTEREXAMPLE
Omega_EM,cov = g Delta_tot                                     OPEN
stabilization in N of all ports                                OPEN
VIR--LB / D                                                     OPEN
```
