# 107.212 -- Arithmetic degree converts the localized prime class into the finite Green term

## 1. Why ordinary coherent support is insufficient

On \(\mathrm{Spec}\,\mathbb Z\), the prime torsion sheaf has the
resolution

\[
 0\longrightarrow\mathbb Z\xrightarrow{\ p\ }\mathbb Z
 \longrightarrow\mathbb F_p\longrightarrow0.
 \tag{1.1}
\]

Consequently

\[
 [\mathbb F_p]=0\quad\text{in }G_0(\mathrm{Spec}\,\mathbb Z).
 \tag{1.2}
\]

Thus ordinary coherent \(K\)-theory forgets the finite-prime weight.
On the Arakelov compactification, however, the arithmetic divisor

\[
 \widehat{[p]}=([p],0)
 \tag{1.3}
\]

has

\[
 \widehat{\deg}\,\widehat{[p]}=\log p.
 \tag{1.4}
\]

The metric anomaly in (1.1), equivalently the product formula for the
principal arithmetic divisor of \(p\), is exactly what distinguishes
(1.4) from (1.2).

## 2. Localized equivariant arithmetic class

For each prime let

\[
 R_{T,p}^{\mathrm{loc}}
 =\mathbb Z[\chi_p,\chi_p^{-1},(1-\chi_p)^{-1}].
 \tag{2.1}
\]

For every prime define the finite-support class

\[
 \widehat\gamma_p
 =\widehat{[p]}\otimes{\chi_p\over1-\chi_p}
 \in
 \widehat{\mathrm{CH}}^1(\overline{\mathrm{Spec}\,\mathbb Z})
 \otimes R_{T,p}^{\mathrm{loc}}.
 \tag{2.2}
\]

The factor \(\chi_p/(1-\chi_p)\) is the nontrivial-return part of the
localized graph--diagonal class.  It is also

\[
 {\chi_p\over1-\chi_p}=\sum_{e\ge1}\chi_p^e,
 \tag{2.3}
\]

so all positive returns of the prime orbit are encoded before any zero
of zeta is used.

It is canonically derived from the proper numerator of 107_211:

\[
 -\chi_p{\partial\over\partial\chi_p}\log(1-\chi_p)
 ={\chi_p\over1-\chi_p}.
 \tag{2.4}
\]

Thus no localized coefficient is selected after inspecting zeta; it is
the logarithmic character of the pushed Euler numerator.  Evaluating
the scale character at \(\chi_p=p^{-s}\), \(\Re s>1\), gives

\[
 \boxed{
 \widehat{\deg}\,\widehat\gamma_p\big|_{\chi_p=p^{-s}}
 =\log p\,{p^{-s}\over1-p^{-s}}.}
 \tag{2.5}
\]

This is exactly the \(p\)-summand of the finite Green character.

## 3. Comparison with the determinant route

The proper Euler numerator of 107_211 satisfies

\[
 {d\over ds}\log(1-p^{-s})
 =\log p\,{p^{-s}\over1-p^{-s}}.
 \tag{3.1}
\]

Equations (2.5) and (3.1) prove that the two constructions agree:

1. the determinant route obtains \(\log p\) by differentiating the
   character \(p^{-s}\);
2. the arithmetic-intersection route obtains it as
   \(\widehat{\deg}[p]\).

These are two realizations of the same scalar, not two factors to be
multiplied.  Hence no \((\log p)^2\) term occurs.

### Theorem 3.1 (finite-place arithmetic degree realization)

For every finite set \(S\) of primes, use the finite tensor-product
coefficient ring

\[
 R_S=\bigotimes_{p\in S}R_{T,p}^{\mathrm{loc}}.
 \tag{3.2}
\]

Then the class

\[
 \widehat\gamma_S=\sum_{p\in S}\widehat\gamma_p
 \tag{3.3}
\]

is a genuine finite-support localized arithmetic divisor class, and

\[
 \widehat{\deg}\,\widehat\gamma_S\big|_{\chi_p=p^{-s}}
 =\sum_{p\in S}\log p\,{p^{-s}\over1-p^{-s}}.
 \tag{3.4}
\]

Thus the finite-prime Green character is an arithmetic degree on every
fixed finite support.

## 4. Relation to published arithmetic fixed-point theory

Arithmetic Lefschetz fixed-point and Lefschetz--Riemann--Roch theorems
of Koehler--Roessler and Tang construct equivariant arithmetic direct
images for regular projective arithmetic schemes under stated group
and smoothness hypotheses.  The present finite-support class is of the
same localized fixed-point form, but Phase 107 has not verified those
hypotheses for its infinite scaling action or nuclear prime assembly.
No applicability promotion is made here.

## 5. Exact remaining boundary

The infinite sum over all primes is not a finite arithmetic divisor.
107_210 constructs it only as a nuclear trace on \(\Re s>1\), and
Meyer supplies its continuation in a Frechet quotient.  What remains
unproved is a single arithmetic-geometric object whose direct image
simultaneously:

1. contains every finite class (3.3) functorially;
2. realizes the nuclear limit;
3. includes Gamma and pole terms;
4. carries a bilinear primitive intersection pairing and Hodge sign.

Moreover the coefficient \((1-\chi)^{-1}\) still has no ordinary
augmentation at \(\chi=1\), exactly as in 107_179.  The result is a
localized arithmetic degree, not an ordinary Arakelov divisor after
forgetting equivariance.

## 6. Falsifier

107_212_arithmetic_degree_of_localized_prime_class.py tests 9,592
actual primes, exact prime-power expansions, the determinant derivative
comparison, and explicit omitted-tail bounds.  It also rejects ordinary
\(G_0\) and unweighted mutations.
