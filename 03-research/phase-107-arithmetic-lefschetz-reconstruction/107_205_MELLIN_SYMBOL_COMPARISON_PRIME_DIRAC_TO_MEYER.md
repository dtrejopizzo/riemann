# 107.205 -- Mellin comparison identifies the prime Dirac determinant with Meyer's Zeta operator

## 1. Mellin diagonalization

Use Meyer's convention

\[
 \widehat f(s)=\int_0^\infty f(x)x^s\,{dx\over x}.
\]

For \(\Re s>1\), absolute convergence permits termwise integration:

\[
 \begin{aligned}
 \widehat{Zf}(s)
 &=\sum_{n\ge1}\int_0^\infty f(nx)x^s\,{dx\over x}\\
 &=\sum_{n\ge1}n^{-s}\widehat f(s)
 =\zeta(s)\widehat f(s).
 \end{aligned}
 \tag{1.1}
\]

Thus the Mellin transform diagonalizes Meyer's source operator \(Z\)
with multiplier \(\zeta(s)\).

## 2. Comparison theorem

The global balanced Dirac operator of 107_200 satisfies

\[
 \det{}_2(1-D_s)=\zeta(s)^{-1}.
\]

Combining with (1.1) gives the exact symbol identity

\[
 \boxed{
 \mathcal M Z\mathcal M^{-1}(s)
 =\det{}_2(1-D_s)^{-1}.
 }
 \tag{2.1}
\]

**Theorem.**  On \(\Re s>1\), the determinant line of the global
balanced prime Dirac operator and Meyer's Zeta-operator multiplier are
canonically identified by Mellin transform.

No zero data enters (2.1): the left side is the integer-dilation
operator and the right side is the prime-block determinant.

## 3. Logarithmic character

Differentiating (2.1) gives

\[
 -d\log\det{}_2(1-D_s)
 =d\log\zeta(s)
 =\frac{\zeta'(s)}{\zeta(s)}\,ds,
\]

or, in the Green sign convention of 107_200,

\[
 d\log\det{}_2(1-D_s)
 =-\frac{\zeta'(s)}{\zeta(s)}\,ds.
 \tag{3.1}
\]

This is precisely the finite-place term used in Meyer's nuclear
character computation.

## 4. Continuation interface

Meyer proves, via Poisson summation and the closed range of \(Z\), that
the quotient representation extends the character as a nuclear
distribution.  Equation (2.1) therefore supplies the missing
comparison interface:

\[
 \text{prime Dirac determinant on }\Re s>1
 \longrightarrow
 \text{Meyer nuclear quotient on the continued test space}.
\]

The continuation is not a cofinal Hilbert determinant limit, in
agreement with 107_203.  It is carried by the nuclear quotient.

## 5. Exact scope

This closes the **analytic determinant-to-nuclear-trace comparison** for
the finite prime sector.  It does not place the nuclear character on the
Connes--Consani square, construct a Green current there, or supply Hodge
positivity.

## 6. Falsifier

For \(f(x)=e^{-x}\),

\[
 Zf(x)=\sum_{n\ge1}e^{-nx}={1\over e^x-1},
 \qquad
 \widehat f(s)=\Gamma(s).
\]

The verifier numerically integrates both Mellin transforms at real and
complex points, checks their ratio against \(\zeta(s)\), and compares
with an independent finite prime-block determinant.  A mutated dilation
coefficient at \(n=2\) must break the identity.
