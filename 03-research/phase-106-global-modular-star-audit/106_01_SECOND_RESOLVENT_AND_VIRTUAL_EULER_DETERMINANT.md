# 106.01 — Second resolvent and the virtual Euler determinant

## Result

The ordinary trace is not the correct regularity class for a zeta-zero
generator. The sharp possible determinant is a genus-one regularized
determinant, controlled by a trace-class **second resolvent**. If a source-built
operator \(\Theta\) satisfied

\[
\boxed{
\operatorname{Tr}(s-\Theta)^{-2}
=-\left(\frac{\xi'}{\xi}\right)'(s),
}
\tag{1}
\]

then its regularized determinant would equal \(e^{a+bs}\xi(s)\), with every
spectral multiplicity appearing linearly. The difficulty is not the
integration of (1); it is constructing \(\Theta\) and proving (1) from the
Euler--Gamma source.

The direct sum of local prime-orbit generators does not do this. It produces
the Euler product as a **virtual determinant in the denominator**, has
infinitely many zero modes, and has nonzero spectral points accumulating at
zero. Hence it has no compact resolvent and cannot be changed into the desired
operator by a trace-class resolvent perturbation.

## 1. The second-resolvent determinant theorem

### Theorem 1

Let \(\Theta\) be a closed operator with discrete spectrum
\(\{\lambda_j\}\), counted with algebraic multiplicity, whose exponent of
convergence is at most two. Suppose

\[
(s-\Theta)^{-2}\in\mathcal S_1
\]

off the spectrum. Let \(D_\Theta\) be its genus-one regularized determinant.
Then

\[
(\log D_\Theta)''(s)
=-\operatorname{Tr}(s-\Theta)^{-2}.
\tag{2}
\]

If (1) holds on any nonempty open subset of \(\Re s>1\), then

\[
D_\Theta(s)=e^{a+bs}\xi(s)
\tag{3}
\]

on the common analytic continuation domain, and hence globally after
continuation.

### Proof

The genus-one canonical factor is

\[
E_1(s/\lambda)=(1-s/\lambda)e^{s/\lambda}.
\]

Twice differentiating its logarithm gives

\[
\frac{d^2}{ds^2}\log E_1(s/\lambda)
=-\frac1{(s-\lambda)^2}.
\]

Trace-class convergence of the second resolvent permits summation over the
spectrum and proves (2). Combining (1) and (2) yields

\[
\left(\log D_\Theta-\log\xi\right)''=0.
\]

Thus the difference is \(a+bs\), which is (3). The identity theorem supplies
the continuation. \(\square\)

### Multiplicity check

Near an eigenvalue \(\lambda\) of algebraic multiplicity \(m\),

\[
\operatorname{Tr}(s-\Theta)^{-2}
=\frac{m}{(s-\lambda)^2}+O(1).
\]

Integrating twice gives \(m\log(s-\lambda)\), so (3) records multiplicity
\(m\), not \(m^2\). This avoids the two-trace multiplicity wall of Phase 101.

## 2. The source side of the required trace

For

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

direct differentiation gives, for \(\Re s>1\),

\[
-\left(\frac{\xi'}{\xi}\right)'(s)
=\frac1{s^2}+\frac1{(s-1)^2}
-\frac14\psi_1(s/2)
-\sum_{n\ge2}\Lambda(n)\log n\,n^{-s}.
\tag{4}
\]

Every term in (4) is explicit Euler--Gamma data. Formula (4), however, is a
scalar identity. Turning it into (1) requires one operator whose second
resolvent has exactly this trace. That operation is the missing global
cohomological projection; writing (4) does not construct it.

## 3. Why the first resolvent is unavailable

The Riemann--von Mangoldt law gives \(N(T)\asymp T\log T\). Consequently a
zero spectrum has

\[
\sum_{|\lambda_j|>1}|\lambda_j|^{-1}=\infty,
\qquad
\sum_{|\lambda_j|>1}|\lambda_j|^{-2}<\infty
\]

in the symmetric/regularized sense appropriate here. Thus the first
resolvent is not trace class, whereas the second resolvent can be. Ordinary
Fredholm determinants and ordinary traces are in the wrong Schatten class.

## 4. The local prime-orbit determinant

For a prime \(p\), put \(\ell_p=\log p\) and consider the translation
generator on a circle of length \(\ell_p\). Up to the conventional factor of
\(i\), its spectrum is

\[
\left\{\frac{2\pi i k}{\ell_p}:k\in\mathbb Z\right\},
\]

and its regularized determinant is, up to a zero-free exponential,

\[
\det_\infty(s-\Theta_p)=1-e^{-s\ell_p}=1-p^{-s}.
\tag{5}
\]

Therefore the finite-place part of the completed zeta function is not the
determinant of the direct sum itself but its inverse:

\[
\zeta(s)=\prod_p\det_\infty(s-\Theta_p)^{-1}.
\tag{6}
\]

Including pole and Gamma factors gives only the safe-half-plane **virtual
determinant**

\[
2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)
\left[\prod_p\det_\infty(s-\Theta_p)\right]^{-1}.
\tag{7}
\]

Equation (7) is a superdeterminant/Euler characteristic. It does not exhibit
\(\xi\) as the determinant of one positive \(H^1\) generator.

## 5. Essential accumulation at zero

For each prime, the first nonzero local frequency is

\[
\frac{2\pi}{\log p}\longrightarrow0
\qquad(p\to\infty).
\]

The direct sum \(\bigoplus_p\Theta_p\) therefore has nonzero spectral points
accumulating at zero, as well as one zero mode for every prime before any
reduction. Its resolvent is not compact. Since compact perturbations preserve
essential spectrum, a compact-resolvent reference operator cannot repair this
by a trace-class resolvent difference.

This is the precise obstruction to obtaining (1) by simply summing the local
orbit generators.

## 6. The exact new object required

A successful construction must supply a complex or quotient

\[
C^0\longrightarrow C^1\longrightarrow C^2
\]

with all of the following properties proved from source data:

1. the local prime orbit spaces occur virtually as in (7);
2. the differential cancels the infinite zero modes and the essential
   accumulation without inserting the zeta divisor;
3. the induced \(H^1\) generator has trace-class second resolvent;
4. its trace satisfies (1);
5. its metric is positive and its centered generator is skew-adjoint.

Items 1 and the scalar formula (4) are known. Items 2--5 are the missing
global cohomological projection. If they are established, Theorem 1 and
skew-adjointness prove RH immediately.

## Status

Proved: Theorem 1, the linear-multiplicity property, the explicit source
formula (4), and the local-orbit essential-spectrum obstruction.

Open: construction of the global \(H^1\) object and proof of (1) from the
Euler--Gamma source. No RH conclusion is claimed.
