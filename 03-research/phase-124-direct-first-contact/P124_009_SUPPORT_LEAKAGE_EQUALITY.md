# P124.009 -- support leakage equality and the first-contact gap

Status: `FINITE-DIMENSIONAL COUNTERMODEL / ABSTRACT LEAKAGE DATA INSUFFICIENT`.

This note tests the extra information returned by the variation front:

\[
        \mathfrak D_{T,\sigma}=B_{\theta,\sigma}^*C_{\eta,\sigma},
        \qquad
        \dot{\mathfrak D}_T
        =\dot B_\theta^*C_\eta+B_\theta^*\dot C_\eta,
        \tag{0.1}
\]

with constant-one Cauchy leakage, and the rank-two Tate crossblock bound
coming from `A_P(I-A_P)`.  The question is whether these identities, plus
first contact on primitive vectors, force the Tate collar current to vanish.
They do not.  The obstruction is already finite-dimensional and typed at
the support-anomaly level.

Throughout, the Hilbert pairing is linear in the first variable, as in
D.240.

## 1. What the leakage identity actually bounds

Let `P` be the support projection and `N=I-P`.  From the dual Euler identity

\[
        \theta_\sigma^*\eta_\sigma=I
        \tag{1.1}
\]

one gets the exact support anomaly

\[
        \mathfrak D_\sigma
        =P\theta_\sigma^*N\eta_\sigma P
        =B_{\theta,\sigma}^*C_{\eta,\sigma},        \tag{1.2}
\]

where

\[
        B_{\theta,\sigma}=N\theta_\sigma P,
        \qquad C_{\eta,\sigma}=N\eta_\sigma P .    \tag{1.3}
\]

Differentiating at the critical parameter gives

\[
        \dot{\mathfrak D}
        =\dot B_\theta^*C_\eta+B_\theta^*\dot C_\eta . \tag{1.4}
\]

For a primitive vector `F` and a Tate vector `tau`, the collar functional
has the form

\[
\boxed{
        J_\tau(F)
        :=\langle\dot{\mathfrak D}F,\tau\rangle
        =\langle C_\eta F,\dot B_\theta\tau\rangle
         +\langle\dot C_\eta F,B_\theta\tau\rangle .}
        \tag{1.5}
\]

Hence Cauchy gives the exact leakage estimate

\[
        |J_\tau(F)|
        \le
        \|C_\eta F\|\,\|\dot B_\theta\tau\|
        +\|\dot C_\eta F\|\,\|B_\theta\tau\|.       \tag{1.6}
\]

Equivalently,

\[
        |J_\tau(F)|^2
        \le E_\tau\,E_{\rm leak}(F),                \tag{1.7}
\]

with, for instance,

\[
        E_\tau=\|B_\theta\tau\|^2+\|\dot B_\theta\tau\|^2,
        \qquad
        E_{\rm leak}(F)=\|C_\eta F\|^2+\|\dot C_\eta F\|^2 .
\]

This is a bound by exterior leakage energy.  It is not a bound by the
first-contact quadratic form `q_T` unless one adds a further theorem
controlling `E_leak(F)` by `q_T(F,F)` on primitive vectors.  At first
contact `q_T>=0` and `L_TF=0` imply only `q_T(F,F)=0`; they do not, by
(1.5), set either exterior vector `C_eta F` or `dot C_eta F` to zero.

The equality condition in (1.6) is also the wrong kind of information.  It
requires the exterior vectors in the two Cauchy pairings to be collinear,
with phases aligned.  That collinearity can make the collar pairing large;
it does not force it to vanish.

## 2. A typed finite-dimensional countermodel

Let

\[
        H=P H\oplus N H,
        \qquad
        P H=\operatorname{span}\{\tau,f\},
        \qquad
        N H=\operatorname{span}\{e\},
\]

with the standard real inner product.  The vector `tau` is the Tate line
and `f` is the primitive first-contact line.  Put `a=1/2` and define

\[
        \eta_\sigma=M_\sigma,
        \qquad
        \theta_\sigma=(M_\sigma^{-1})^*,
\]

where, in the ordered basis `(tau,f,e)`,

\[
        M_\sigma=
        \begin{pmatrix}
        1&0&a\\
        0&1&0\\
        0&\sigma&1
        \end{pmatrix},
        \qquad
        M_\sigma^{-1}=
        \begin{pmatrix}
        1&a\sigma&-a\\
        0&1&0\\
        0&-\sigma&1
        \end{pmatrix}.                              \tag{2.1}
\]

Therefore

\[
        \theta_\sigma^*\eta_\sigma
        =M_\sigma^{-1}M_\sigma=I                    \tag{2.2}
\]

exactly.  The support anomaly is

\[
        \mathfrak D_\sigma
        =P M_\sigma^{-1}N M_\sigma P
        =
        \begin{pmatrix}
        0&-a\sigma\\
        0&0
        \end{pmatrix}_{(\tau,f)} .                  \tag{2.3}
\]

It has the required factorization.  Indeed

\[
        B_{\theta,\sigma}=N\theta_\sigma P=(-a,0),
        \qquad
        C_{\eta,\sigma}=N\eta_\sigma P=(0,\sigma),  \tag{2.4}
\]

so `mathfrak D_sigma=B_theta^* C_eta`.  Differentiating at `sigma=0`,

\[
        \dot{\mathfrak D}=B_\theta^*\dot C_\eta
        =
        \begin{pmatrix}
        0&-a\\
        0&0
        \end{pmatrix}.                              \tag{2.5}
\]

Thus the Tate collar functional on the primitive vector is nonzero:

\[
\boxed{
        J_\tau(f)=\langle\dot{\mathfrak D}f,\tau\rangle=-a=-\frac12.}
        \tag{2.6}
\]

The Cauchy bound is sharp here, not defective:

\[
        B_\theta\tau=-a e,
        \qquad \dot C_\eta f=e,
        \qquad
        |J_\tau(f)|=\|B_\theta\tau\|\,\|\dot C_\eta f\|=a. \tag{2.7}
\]

So the equality condition in the leakage Cauchy estimate is satisfied and
still the collar is nonzero.

Now impose the first-contact primitive score.  Let `Pi` be the projection
from `P H` onto the primitive line `span{f}`.  The localized dual-pairing
derivative seen on `P H` is `-dot{mathfrak D}`; take its Hermitian part

\[
        S={-\dot{\mathfrak D}-\dot{\mathfrak D}^{*}\over2}.
\]

The compressed primitive operator is

\[
        L:=\Pi S\Pi=0.                              \tag{2.8}
\]

Hence `L>=0`, `Lf=0`, and `q(f,f)=<Lf,f>=0`, exactly the abstract
first-contact condition on primitives.  Nevertheless (2.6) gives a
nonzero Tate collar current.

The announced rank-two Tate bound is also respected.  The collar crossblock
`f -> tau` has norm `a=1/2`.  This is the extremal value of
`||sqrt(A_P(I-A_P))||` for a one-dimensional Tate projection with
`A_P=1/2`; adding a second unused Tate line only increases the allowed rank,
not the conclusion.  Thus the finite-rank Tate contractivity information is
compatible with a nonzero collar.

## 3. Consequence for the real phase-124 route

The model proves only a logical no-go for the abstract data just listed. It
does not falsify the arithmetic operator.  What it shows is sharper:

\[
        \theta^*\eta=I,
        \quad
        \mathfrak D=B_\theta^*C_\eta,
        \quad
        \dot{\mathfrak D}=\dot B_\theta^*C_\eta+B_\theta^*\dot C_\eta,
        \quad
        q_T\ge0,
        \quad
        L_TF=0,
\]

plus the rank-two Tate crossblock norm bound, do not imply
`J_tau(F)=0` on primitive first-contact vectors.  A bound of the form

\[
        |J_\tau(F)|^2\le C_T q_T(F,F)               \tag{3.1}
\]

would be an additional range/shorting theorem, not a consequence of the
D.240 duality and Cauchy equality cases.  In the countermodel the right
side of (3.1) is zero while the left side is `1/4`.

Thus the leakage energy from (1.7) is related to `q_T` only through a
missing support-to-primitive estimate.  The D.190 full block
`B_E-X^*A_O^\dagger X` is exactly the kind of larger positive shorting datum
that could supply such control.  The rank-two Tate block cannot replace it:
it can saturate its own norm bound while leaving the primitive collar
current free.
