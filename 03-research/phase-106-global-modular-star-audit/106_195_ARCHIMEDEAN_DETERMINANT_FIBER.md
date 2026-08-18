# 106.195 — The archimedean determinant fiber

## 1. Purpose

The finite root tower of 106.194 produces the complete coefficient
\(\Lambda(p^k)p^{-k/2}\) from positive cycle Laplacians and relative
determinants.  The archimedean page of 106.160 already realizes the Gamma
density as the trace of a positive semigroup, but its determinant line was
not computed.  This note performs that computation in the centered
coordinate

\[
 z=s-\frac12.                                               \tag{1}
\]

The result is an exact determinant realization of the full Gamma--polar
factor

\[
 A_\infty(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),                     \tag{2}
\]

with no use of the zeros of \(\zeta\) or of the Weil sign.

## 2. Zeta determinant of the Gamma spin operator

On \(\mathcal H_\Gamma=\ell^2(\mathbb N_0)\), retain the positive
operator of 106.160,

\[
 N_\Gamma e_m=\left(2m+\frac12\right)e_m.                  \tag{3}
\]

For \(\Re z>-1/2\), the spectral zeta function of \(N_\Gamma+z\) is

\[
 \begin{aligned}
 Z_\Gamma(w;z)
 &=\mathrm{Tr}(N_\Gamma+z)^{-w}\\
 &=\sum_{m\ge0}(2m+1/2+z)^{-w}\\
 &=2^{-w}\zeta_H\!\left(w,\frac{s}{2}\right),             \tag{4}
 \end{aligned}
\]

initially for \(\Re w>1\), and meromorphically elsewhere.  Here
\(\zeta_H\) is the Hurwitz zeta function and (1) was used in the last
line.  Define

\[
 \det_\zeta(N_\Gamma+z)
 :=\exp\bigl(-\partial_wZ_\Gamma(0;z)\bigr).               \tag{5}
\]

### Theorem 2.1 — Exact Gamma determinant

For \(\Re s>0\),

\[
 \boxed{
 \det_\zeta(N_\Gamma+s-1/2)
 =\frac{\sqrt{2\pi}\,2^{,1/2-s/2}}{\Gamma(s/2)}.}        \tag{6}
\]

Both sides extend meromorphically with the same identity.

#### Proof

Set \(a=s/2\).  The classical values

\[
 \zeta_H(0,a)=\frac12-a,
 \qquad
 \zeta_H'(0,a)=\log\Gamma(a)-\frac12\log(2\pi)            \tag{7}
\]

and (4) give

\[
 \begin{aligned}
 -\partial_w Z_\Gamma(0;z)
 &=\left(\frac12-a\right)\log2
   -\log\Gamma(a)+\frac12\log(2\pi).
 \end{aligned}                                             \tag{8}
\]

Exponentiating (8) proves (6). \(\square\)

The heat trace underlying (4) is exactly the previously constructed
Gamma spin page:

\[
 \mathrm{Tr}\,e^{-uN_\Gamma}
 =\frac{e^{-u/2}}{1-e^{-2u}}.                              \tag{9}
\]

Thus (6) is not a determinant prescribed from \(\Gamma\); it is the zeta
determinant of the source-defined positive operator whose heat trace was
already fixed independently.

## 3. The polar determinant

Let \(\mathcal H^{\rm triv}=\mathbb C e_0\oplus\mathbb C e_2\) and

\[
 N_{\rm triv}e_0=-\frac12e_0,
 \qquad
 N_{\rm triv}e_2=\frac12e_2.                               \tag{10}
\]

This is the \(H^0/H^2\) plane of 106.160.  In the centered coordinate,

\[
 \boxed{
 \det(zI-N_{\rm triv})
 =(z+1/2)(z-1/2)=s(s-1).}                                 \tag{11}
\]

The same plane has heat trace

\[
 \mathrm{Tr}\,e^{-uN_{\rm triv}}=2\cosh(u/2),        \tag{12}
\]

so the determinant and fixed-point descriptions are two realizations of
the same polar boundary page.

## 4. Exact Gamma--polar determinant identity

### Theorem 4.1 — Archimedean relative determinant

The completed archimedean factor (2) satisfies

\[
 \boxed{
 A_\infty(s)
 =\sqrt\pi\,(2\pi)^{-s/2}
   \frac{\det((s-1/2)I-N_{\rm triv})}
        {\det_\zeta(N_\Gamma+s-1/2)}.}                    \tag{13}
\]

#### Proof

Insert (6) and (11) into the right side of (13).  The scalar factor is

\[
 \frac{\sqrt\pi(2\pi)^{-s/2}}
      {\sqrt{2\pi},2^{1/2-s/2}}
 =\frac12\pi^{-s/2}.                                      \tag{14}
\]

The remaining factors are \(s(s-1)\Gamma(s/2)\), which gives (2).
\(\square\)

The affine exponential \(\sqrt\pi(2\pi)^{-s/2}\) is fixed by the
normalization in (3); it is not a free finite counterterm.  Its logarithm
is affine in \(s\), so it changes neither the determinant divisor nor any
second logarithmic variation.

For two regular points \(s,s_0\), (6) also gives the relative form

\[
 \frac{\pi^{-s/2}\Gamma(s/2)}
      {\pi^{-s_0/2}\Gamma(s_0/2)}
 =(2\pi)^{-(s-s_0)/2}
  \frac{\det_\zeta(N_\Gamma+s_0-1/2)}
       {\det_\zeta(N_\Gamma+s-1/2)}.                     \tag{15}
\]

This is the archimedean relative determinant needed to accompany the
finite root-covering determinant ratios of 106.194.

## 5. Positive degree-one page and cohomological parity

On the real doubled form domain of \(N_\Gamma^{1/2}\), define

\[
 \begin{aligned}
 g_\Gamma((x,y),(u,v))
 &=\langle N_\Gamma^{1/2}x,N_\Gamma^{1/2}u\rangle
  +\langle N_\Gamma^{1/2}y,N_\Gamma^{1/2}v\rangle,\\
 J_\Gamma(x,y)&=(-y,x),\\
 \Omega_\Gamma(a,b)&=-g_\Gamma(a,J_\Gamma b).             \tag{16}
 \end{aligned}
\]

Then \(g_\Gamma\) is positive, \(J_\Gamma^2=-I\), and
\(\Omega_\Gamma\) is alternating and nondegenerate.  This is the
archimedean positive degree-one page.  The finite-dimensional factor
(10) is not added to that positive metric: it remains the hyperbolic
trivial cohomology whose determinant occurs in the numerator of (13).
This separation preserves the Lefschetz parity

\[
 H^0-H^1+H^2                                             \tag{17}
\]

rather than converting all local fixed-point terms into an orthogonal
positive direct sum.

## 6. What has and has not been closed

Together, 106.194 and the present note now provide:

* functorial positive finite-root polarizations;
* exact finite relative torsion \(\log p\);
* exact incidence coefficient \(p^{-k/2}\);
* the literal product \(\Lambda(p^k)p^{-k/2}\);
* a positive archimedean spin page;
* the exact Gamma determinant and polar \(H^0/H^2\) determinant;
* the complete archimedean factor (13), including its normalization.

These are source constructions and use no zero of \(\zeta\).

They do **not** yet prove that the finite-root and archimedean pages form
the desired global degree one.  The remaining theorem is a relative
descent statement: construct the common boundary pushout, prove that its
source norm is faithful on separated CCM degree one, and verify bounded
weak nondegeneracy plus uniform boundedness of normalized scaling.  Once
those properties hold, 106.191 and 106.190 produce the compatible positive
complex structure.

## 7. Status

Proved:

* the archimedean determinant fiber in the same relative-determinant
  language as the finite root tower;
* exact agreement with Gamma, the polar polynomial, and their heat traces;
* positivity of the degree-one Gamma page before global descent.

Still required:

* the prime--Gamma--polar boundary pushout;
* its faithful descent to separated CCM degree one;
* the three analytic hypotheses of Corollary 4.2 in 106.191.
