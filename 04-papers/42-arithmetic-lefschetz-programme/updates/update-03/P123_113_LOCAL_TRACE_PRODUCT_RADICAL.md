# P123.113 — Exact radical and sign of the local trace-of-product pairing

Status: PROVED-IN-REPOSITORY on compact
multiplicative Bruhat tests on Q_q^*, with probability unit Haar.
This is a local calculation, not the global numerical theory of A.6.

## 1. Fourier decomposition of the test algebra

For a test f set a_(k,chi)=integral_U f(q^k u)chi(u)^-1 du and
p_(f,chi)(z)=sum_k a_(k,chi)z^k. Only finitely many characters and
valuation exponents occur. Conversely every such finite collection of
Laurent polynomials is a test, by finite unit Fourier inversion.

Convolution becomes componentwise Laurent multiplication, and star
becomes p(z)->conjugate(p(1/conjugate z)). Thus the test algebra is
the algebraic direct sum, over unit characters, of C[z,z^-1]. No
completion or extra spectral test functions are required for this fact.

Let r=q^-1/2. P123.107 gives the local relative trace in these coordinates:

    W_loc(f)=-sum_(chi!=1)c(chi) a_(0,chi)
                               +sum_(k!=0)r^|k| a_(k,1).  (1)

## 2. Spectral density in the trivial-character sector

The absolutely convergent geometric Fourier series gives

    P_r(theta)=sum_(k in Z)r^|k| exp(i k theta)
              =(1-r^2)/(1-2r cos theta+r^2).

Consequently for a Laurent polynomial p in the trivial unit sector,

    W_loc(p)=integral_0^(2pi) p(exp(i theta)) w_r(theta)
                                                   dtheta/(2pi),
    w_r=P_r-1=2r(cos theta-r)/(1-2r cos theta+r^2).          (2)

The sign changes at cos theta=r; the denominator is strictly positive.
The subtraction of one removes exactly the zero-valuation constant
coefficient from (1), rather than changing the prescribed trace.

For I_loc(f,g)=W_loc(f*g), formulas (1)–(2) give its Hermitian version

    I_loc(f,f^*)
       =-sum_(chi!=1)c(chi) integral |p_(f,chi)|^2 dtheta/(2pi)
         +integral |p_(f,1)|^2 w_r(theta) dtheta/(2pi).      (3)

## 3. The radical against all compact tests is zero

Suppose I_loc(f,g)=0 for every compact Bruhat test g. Tests supported
in one unit Fourier character isolate that summand. In a nontrivial
summand the functional is -c(chi) times the constant Laurent coefficient
of p_(f,chi)p_(g,chi). Taking all monomials for p_g extracts every
coefficient of p_f; since c(chi)>0, that polynomial must vanish.

In the trivial summand, taking all Laurent monomials implies that every
Fourier coefficient of the continuous function p_f(exp(i theta))w_r(theta)
vanishes. Uniform density of trigonometric polynomials, or convolution
with their elementary Fejer approximants, then makes that function zero.
Since w_r is nonzero except at two points, continuity forces p_f=0
on the entire circle, hence all its Laurent coefficients are zero.
Therefore

    rad I_loc={0}.                                        (4)

The same conclusion holds for the Hermitian pairing because star is
a bijection of the test algebra. This determines the whole radical on
the stated algebra; no restriction to a finite list of arithmetic tests
is used. In particular its ideal and star stability are exact here.

## 4. Explicit tests with opposite signs

Let e be the unit-supported constant test, and v the constant test on
qU. Both lie in the trivial unit sector, with polynomials 1 and z.
For f_+=e+v and f_-=e-v,

    I_loc(f_+,f_+^*)=2r>0,
    I_loc(f_-,f_-^*)=-2r<0.                                (5)

Indeed |1+z|^2=2+z+z^-1 and |1-z|^2=2-z-z^-1 on the circle; (1)
annihilates the constant term and evaluates z,z^-1 as r. Thus the
local form is nondegenerate and indefinite already on explicit compact
tests. Its isotropic vectors, for example e with self-value zero, need
not belong to its radical: I_loc(e,v)=r.

The Haar normalization used for the local Weil packet multiplies all
these values by log q and changes neither the radical nor the signs.

## 5. Scope for A and D

This completes the radical calculation for the local trace-product test
algebra and gives its exact spectral/sign description. It supplies a
nondegenerate local pairing compatible with the declared product, in
contrast to the anomaly radical in P123.112.

It does not show that this algebra is the full correspondence category,
identify the ruling plane or the required completed mixed numerical
sector, or prove a global sign. The global Weil form includes other
places and restrictions on the common tests; neither local sign in
(5) decides D. The geometric RR comparison and full row A remain open.
