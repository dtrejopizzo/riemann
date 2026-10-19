# P123.034 — Fourier normalization fixes the finite-place unit counterterm

Status: PROVED for the local distribution identity
below. This identifies P123.033's normalization with the specified
self-dual p-adic Fourier convention, not with the yet-unconstructed
common-carrier shadow or an unverified cutoff theorem.

## 1. Define the local distribution

Choose an additive character psi of Q_p trivial on Z_p and nontrivial
on p^-1 Z_p. Normalize additive Haar measure dx by vol(Z_p)=1; it is
self-dual for this conductor. Let F be its additive Fourier transform.
The locally integrable function log|x|_p defines a distribution on
Bruhat tests. Set

    T_p = -F(log|x|_p),
    C_p = log p/(1-p^-1).

There is no free delta coefficient in this definition. The logarithm
at x=0 is interpreted by local integrability, not by a pointwise value.
Fourier signs do not affect the calculations, since the distribution
and the relevant radial weights are invariant under x -> -x.

## 2. Compute off the origin

Take y_0 in Z_p^* and m>=1. The Fourier transform of
1_(y_0+p^m Z_p) is

    p^-m psi(y_0 x) 1_(p^-m Z_p)(x),

up to the immaterial Fourier sign. The integral of log|x|_p against
this function can be evaluated by shells. On x in Z_p,

    integral log|x|_p dx
      =-(log p)(1-p^-1) sum_(k>=0) k p^-k
      =-log p/(p-1).

On the shell p^-1 Z_p minus Z_p, the additive character integral is
-1 and log|x|_p=log p, giving -log p. On every larger shell the two
ball character integrals are both zero. Hence

    <F(log|x|_p),1_(y_0+p^m Z_p)> = -C_p p^-m.

Scaling gives the density -C_p/|y|_p on every ball avoiding zero.
Indeed scaling log|x|_p adds a constant, whose Fourier transform is
supported at zero; away from zero only the Jacobian factor remains.
Such balls span the tests supported away from zero. Therefore

    T_p(y)=C_p/|y|_p,  y!=0,                         (2.1)

as a distributional restriction.

## 3. Fix the unit contribution

Because F(1_Zp)=1_Zp, the preceding elementary logarithmic integral gives

    <T_p,1_Zp>=log p/(p-1).

The ball 1+p Z_p avoids zero, so (2.1) gives

    <T_p,1_(1+p Z_p)>=C_p/p=log p/(p-1).

But 1_(Z_p^*)(1-y)=1_Zp(y)-1_(1+p Z_p)(y). Consequently

    <T_p(y),1_(Z_p^*)(1-y)>=0.                      (3.1)

Thus translating the Fourier-normalized distribution to the singular
point x=1 yields exactly the zero-on-constant-units normalization.
For any locally constant g on Z_p^*, subtract g(1) and use (2.1) on
the resulting test, which vanishes near y=0. Equation (3.1) implies

    <T_p(y),1_(Z_p^*)(1-y) g(1-y)>
       = C_p integral_(Z_p^*) [g(x)-g(1)]/|1-x|_p dx.

Since probability Haar on Z_p^* is dx/(1-p^-1), this is precisely
P123.033's unit functional, including its log p factor.

## 4. Match the whole finite-place packet

For f as in P123.032 define the local Bruhat function

    G_f(x)=|x|_p^-1/2 f(j_p(x)), x!=0,
    G_f(0)=0.

Compact logarithmic support bounds the valuation of x in both
directions; finite unit level gives local constancy. Thus G_f is
compactly supported and zero near x=0, so G_f(1-y) is a valid additive
Bruhat test. Define

    W_p^Fourier(f)=<T_p(y),G_f(1-y)>.

Decompose into unit and nonunit x. On the nonunit region y=1-x never
vanishes, so (2.1) and

    d^*x=C_p dx/|x|_p,  vol_(d^*)(Z_p^*)=log p,

give exactly the half-density integral of P123.032. On units,
section 3 gives exactly P123.033. Therefore

    W_p^Fourier(f)=L_p^off(f)+L_p^unit(f).           (4.1)

This proves the Fourier normalization of the finite-place scalar
packet; no arbitrary coefficient times f(1) remains under this
specified additive-character and Haar convention. Its conductor
values and compact-step stabilization follow from P123.032–033.

## 5. Scope of the remaining theorem

The additive character has been fixed to conductor Z_p. Changing the
Fourier normalization can alter a delta term and must be tracked if a
different imported convention is used. The common-carrier trace and
its cutoff operators have not been realized by T_p here. Their equality
with (4.1), and the archimedean/Tate comparison, remain requirements of C.
This note removes the previously free local unit normalization within
the stated Fourier model; it does not prove RR or D.
