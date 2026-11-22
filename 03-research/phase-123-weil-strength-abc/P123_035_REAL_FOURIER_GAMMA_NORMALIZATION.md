# P123.035 — real Fourier normalization, source coefficient audit and Gamma symbol

Status: PROVED for the Fourier-normalized scalar
distribution and its Gamma symbol below. The literal off-origin
coefficient in the cited Meyer computation fails the explicit Gaussian
check under its stated Fourier convention. This isolates a normalization
issue; it does not refute the existence of the nuclear representation
or assert a corrected common-carrier comparison theorem.

## 1. A normalization test that avoids principal values

Use ordinary Lebesgue measure and

    F phi(y)=integral_R phi(x) exp(2 pi i x y) dx.

This is the convention in Meyer's eq:def_Fourier. Let
phi(x)=x^2 exp(-pi x^2), so phi(0)=0. Differentiating the Gaussian gives

    F phi(y)=(1/(2 pi)-y^2) exp(-pi y^2)
            =(1/(2 pi)) d/dy [y exp(-pi y^2)].

Integration by parts, with y log|y| tending to zero at the origin,
gives the exact distribution pairing

    <F(log|x|),phi>=-1/(2 pi).

But integral_R phi(y)/|y| dy=1/pi. Therefore the off-origin coefficient
of F(log|x|) is -1/2, not -1. A delta term cannot change this test,
because phi(0)=0.

The local [Meyer source](../../00-references/papers-nuevos/foliated-dynamics/arXiv-math0412277v3),
end of section 5, explicitly obtains the coefficient c=-1 with that
Fourier definition. The [online version checked](https://arxiv.org/html/math/0412277v3)
also displays the unhalved archimedean kernel in equation (3). Those
literal normalizations must not be imported without reconciliation.
Evenness of phi does not remove the discrepancy: the Fourier transform
and distribution pairing above are both on the full real line as stated.
The prime-packet substitution in P123.033 is unaffected by this audit.

## 2. The Fourier-normalized real distribution

Define

    T_infinity=-F(log|x|).

For a Schwartz test phi define the finite part with unit-radius cutoff by

    Pf(phi)= integral_(|y|<=1) [phi(y)-phi(0)]/|y| dy
             +integral_(|y|>1) phi(y)/|y| dy.

Then

    T_infinity = (1/2) Pf + (gamma+log(2 pi)) delta_0. (2.1)

Here gamma is Euler's constant. To verify the coefficient and the delta
term together, Fourier transform |x|^s in the initial strip -1<Re(s)<0
using the cosine integral, then continue the tempered distributions
meromorphically to s=0:

    F(|x|^s)=c(s)|y|^(-1-s),
    c(s)=-2 Gamma(1+s) sin(pi s/2) (2 pi)^(-1-s).

Splitting the integral at |y|=1 and subtracting phi(0) yields

    |y|^(-1-s)=(-2/s) delta_0+Pf+O(s),
    c(s)=-(s/2)[1-(gamma+log(2 pi))s+O(s^2)].

Differentiation at zero proves (2.1). Subtraction also justifies the
continuation near zero; no singular integral is differentiated without
its delta contribution. The initial cosine integral is
[DLMF 5.9.6](https://dlmf.nist.gov/5.9.E6).

## 3. Translate and change to half-densities

For h in C_c^infinity(R), define the even function

    G_h(x)=|x|^-1/2 h(log|x|), x!=0,   G_h(0)=0.

It is smooth and supported in a compact annulus. Put

    W_infinity(h)=<T_infinity(y),G_h(1-y)>.

Away from the singularity, folding x and -x gives exactly one half
of the sum of the two real kernels. In logarithmic coordinates the
resulting even kernel for t>0 is

    K(t)=exp(-t/2)/(1-exp(-2t)).

The complete, convergent formula is

    W_infinity(h)=(gamma+log(4 pi)) h(0)
       +integral_0^infinity K(t)
          [h(t)+h(-t)-2h(0)exp(-t/2)] dt.           (3.1)

To check its constant, subtract h(0) times the reference function
h_ref(t)=exp(-|t|/2). Its associated G_ref equals 1 for |x|<=1 and
1/|x| for |x|>=1. Evaluate the explicit finite part (2.1) on
G_ref(1-y); its tail is integrable and its local cusp is Lipschitz,
so the same formula is well-defined. The positive-x part of the
finite-part integral is

    integral_1^2 (-1/x) dx + integral_2^infinity 1/[x(x-1)] dx=0.

The negative-x part is

    integral_0^1 1/(1+x) dx
      +integral_1^infinity 1/[x(1+x)] dx=2 log 2.

After the factor 1/2, W_infinity(h_ref)=gamma+log(4 pi).
The difference h-h(0)h_ref has zero value at the singular point and
gives the ordinary K integral, proving (3.1).

Near t=0 the bracket in (3.1) is O(t), while K(t)=O(1/t).
At infinity its remaining reference tail decays as exp(-t).
This proves convergence and continuity on each fixed smooth compact
support step, with a bound using h(0), sup norm and first derivative.
No cutoff operator or completed geometric trace is inferred.

## 4. Gamma multiplier and its sign convention

The formula extends to h(t)=exp(i tau t), since the subtracted bracket
still cancels at zero and K decays at infinity. Substituting u=2t and
using the digamma difference integral gives

    W_infinity(exp(i tau t))
      =gamma+log(4 pi)+psi(1/2)-Re psi(1/4+i tau/2)
      =log pi-Re psi(1/4+i tau/2).                  (4.1)

The identities used here are the integral representation
[DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16) and
[psi(1/2), DLMF 5.4.13](https://dlmf.nist.gov/5.4.E13).
Equivalently, for the logarithmic Fourier convention
h_hat(tau)=integral h(t) exp(-i tau t) dt,

    W_infinity(h)=(1/(2 pi)) integral_R h_hat(tau)
                      [log pi-Re psi(1/4+i tau/2)] dtau.

Interchange follows, for example, from the bound
|cos(tau t)-1|<=min(2,tau^2 t^2/2), the exponential tail of K,
and rapid decay of h_hat. The integral multiplier grows at most
logarithmically by splitting t at 1/(1+|tau|). The expression is the
archimedean distribution in the poles-minus-zeros convention. Reversing
the sign to form zeros-minus-poles reverses this multiplier too.

## 5. The two Tate moments under the same substitution

For g(x)=x^-1/2 h(log x), the Mellin test is

    g_hat(s)=integral_R h(t) exp((s-1/2)t) dt.

Thus the two pole characters at s=0,1 give

    g_hat(0)+g_hat(1)=integral_R 2 cosh(t/2) h(t) dt.

These are exactly the moments of the two half-density Tate characters.
This verifies their scalar normalization. It does not geometrically
embed the ruling plane or prove that a carrier trace subtracts them.

## 6. Remaining obligation

P123.032–035 now specify compatible scalar conventions for prime terms,
finite unit conductors, the real Fourier counterterm, Gamma multiplier
and Tate moments. Equality of that scalar distribution with the new
common-carrier shadow remains unproved. The mismatch in the literal
Meyer archimedean coefficient must be resolved at the precise imported
trace formula before citing it with these constants. Nothing here
establishes the sign needed for D or fills the mixed RR/effectivity gaps.

Numerical quadrature in the companion verifier is a normalization
regression, not a rigorous interval certificate; the analytic identities
above are the mathematical evidence.
