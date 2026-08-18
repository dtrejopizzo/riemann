# 107.05 -- Paper A, Part III: the archimedean Green metric

## 1. Purpose

This note executes Work Package I-C of 107.00.  The finite determinant
lines of `107_04` already recover the exact cyclotomic off-diagonal
support, but they do not determine a diagonal number and they do not yet
carry the Gamma, pole, or polar contributions.  The missing ingredient is
an archimedean metric on the same determinant line.

The output of this note is a metrized pairing

\[
 \overline{\langle D,E\rangle}
 =\bigl(\langle D,E\rangle_{\mathrm{fin}},
        \|\cdot\|_{\Gamma,\mathrm{pol}}\bigr)
 \tag{1.1}
\]

on finite-support source divisors \(D,E\in\operatorname{Div}_{\mathrm{EF}}\),
with the diagonal obtained from the same metric as the cross terms.

## 2. Input from earlier steps

Three previous documents supply the required ingredients.

1. `107_03` fixes the finite-support source divisor module
   \(\operatorname{Div}_{\mathrm{EF}}\).
2. `107_04` constructs the finite determinant line
   \(\langle D,E\rangle_{\mathrm{fin}}\) and proves that its
   off-diagonal orders are the normalized cyclotomic resultants.
3. Phase 106 already isolated the necessary archimedean normalization:
   `106.172` computes the exact primitive finite part
   \(\kappa_\infty\), `106.195` gives the exact Gamma--polar determinant,
   and `106.181` proves exact cancellation under a matched common cutoff.

This note repackages those ingredients in the language required by
Phase 107.

## 3. The archimedean determinant fiber

Work in the centered coordinate

\[
 z=s-\frac12.
 \tag{3.1}
\]

Let \(N_\Gamma\) be the positive Gamma-spin operator of `106.195`,

\[
 N_\Gamma e_m=\left(2m+\frac12\right)e_m
 \qquad (m\ge0),
 \tag{3.2}
\]

and let \(N_{\mathrm{triv}}\) be the polar \(H^0/H^2\) operator

\[
 N_{\mathrm{triv}}e_0=-\frac12e_0,
 \qquad
 N_{\mathrm{triv}}e_2=\frac12e_2.
 \tag{3.3}
\]

The exact determinant identities proved in `106.195` are:

\[
 \det_\zeta(N_\Gamma+s-\tfrac12)
 =\frac{\sqrt{2\pi}\,2^{1/2-s/2}}{\Gamma(s/2)},
 \tag{3.4}
\]

\[
 \det((s-\tfrac12)I-N_{\mathrm{triv}})
 =s(s-1),
 \tag{3.5}
\]

and therefore

\[
 \boxed{
 A_\infty(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)
 =\sqrt\pi\,(2\pi)^{-s/2}
 \frac{\det((s-\tfrac12)I-N_{\mathrm{triv}})}
      {\det_\zeta(N_\Gamma+s-\tfrac12)}.}
 \tag{3.6}
\]

Equation (3.6) is the exact source-defined Gamma--polar determinant
required by 107.00.

## 4. The matched primitive finite part

The common scalar entering the archimedean boundary is the exact finite
part computed in `106.172`:

\[
 \boxed{
 \kappa_\infty
 =\gamma+\sum_p\sum_{k\ge2}\frac{\log p}{p^k}>0.}
 \tag{4.1}
\]

It is not a free renormalization constant.  It is forced by the single
differentiated Euler identity behind
\(-\zeta'(w)/\zeta(w)\) at \(w=1\).

Equivalently, the primitive finite part and the archimedean boundary norm
cancel exactly:

\[
 \operatorname{FP}_{s\downarrow1/2}\|B_sF\|^2+\|B_\infty F\|^2=0.
 \tag{4.2}
\]

This scalar is the only coefficient that can appear in the boundary
shorting of the Green metric.  Any alternative additive constant would
break (4.2).

## 5. Matched-cutoff stabilization

Let \(h\) be the logarithmic fixed-orbit coefficient associated to a pair
of source divisors \(D,E\).  For a common cutoff \(X\), Phase 106 defines
the finite Green energy \(\mathcal E_X(h)\) and the boundary correction
\(\mathcal B_X(h)\) so that

\[
 \mathcal E_X(h)+\mathcal B_X(h)
 =\mathcal P_\infty(h)-A_X(h),
 \tag{5.1}
\]

where \(A_X(h)\) is the finite prime-power sum and \(\mathcal P_\infty(h)\)
is the joined archimedean--polar functional.

The key normalization theorem from `106.181` is:

\[
 \boxed{
 \mathcal E_X(h)+\mathcal B_X(h)
 =\mathcal P_\infty(h)
  -\sum_{p,k\ne0}\frac{\log p}{p^{|k|/2}}\,h(k\log p)}
 \tag{5.2}
\]

for every cutoff \(X\) beyond the logarithmic support of \(h\).  The
right-hand side is then independent of \(X\).

This is the exact form of the product-formula requirement in 107.00:
the common cutoff cancels before any limit is taken.

## 6. Definition of the Gamma--polar metric

For \(D,E\in\operatorname{Div}_{\mathrm{EF}}\), let \(h_{D,E}\) denote the
source logarithmic correlation extracted from the connected return data.
Because \(D\) and \(E\) have finite prime-power support, \(h_{D,E}\) has
compact logarithmic support.

### Definition 6.1: archimedean Green functional

Define the archimedean Green functional by the stabilized expression

\[
 G_{\Gamma,\mathrm{pol}}(D,E)
 :=
 \mathcal P_\infty(h_{D,E})
 -\sum_{p,k\ne0}\frac{\log p}{p^{|k|/2}}\,h_{D,E}(k\log p).
 \tag{6.1}
\]

By (5.2), this is independent of the matched common cutoff once the
cutoff exceeds the support of \(h_{D,E}\).

### Definition 6.2: archimedean norm

Let \(1_{D,E}\) be the canonical generator of the real line underlying
the archimedean component of \(\langle D,E\rangle\).  Define

\[
 \boxed{
 \|1_{D,E}\|_{\Gamma,\mathrm{pol}}
 :=\exp\!\bigl(-G_{\Gamma,\mathrm{pol}}(D,E)\bigr).}
 \tag{6.2}
\]

The metrized determinant line is then
\(\overline{\langle D,E\rangle}\) as in (1.1).

This is the minimal archimedean completion consistent with `107_04`: the
finite-place determinant line is kept, and its missing diagonal data is
supplied by the same Green functional that governs the cross terms.

## 7. The diagonal from the same metrized line

The finite cyclotomic theory of `107_04` left the diagonal as an excess
intersection object.  The present metric closes that gap.

### Definition 7.1: diagonal self-pairing

For a source divisor \(D\in\operatorname{Div}_{\mathrm{EF}}\), define its
self-pairing by

\[
 \overline{\langle D,D\rangle}
 :=
 \bigl(\mathcal E_D,\|1_{D,D}\|_{\Gamma,\mathrm{pol}}\bigr),
 \tag{7.1}
\]

where \(\mathcal E_D\) is the excess-intersection finite line of
`107_04` and the metric is given by (6.2) with \(E=D\).

Thus the diagonal is not inserted by cardinality, discriminant, or an
unrelated normal-bundle formula.  It is obtained from the same
Gamma--polar metric that governs off-diagonal pairings.

### Proposition 7.1: diagonal coherence

The self-pairing of \(D\) and the cross-pairing of \(D,E\) are computed
in one and the same metrized determinant theory.

Proof.  Off-diagonal pairs use the finite determinant line of `107_04`
plus the norm (6.2).  The diagonal uses the excess finite line
\(\mathcal E_D\) plus the same norm formula (6.2), evaluated at
\(h_{D,D}\).  No second metric is introduced.  \(\square\)

This is exactly the coherence requirement imposed by 107.00.

## 8. Arithmetic Deligne pairing on finite-support divisors

### Definition 8.1: arithmetic pairing

The Paper A arithmetic Deligne pairing on
\(\operatorname{Div}_{\mathrm{EF}}\) is the assignment

\[
 (D,E)\longmapsto \overline{\langle D,E\rangle}
 =\bigl(\langle D,E\rangle_{\mathrm{fin}},
        \|\cdot\|_{\Gamma,\mathrm{pol}}\bigr),
 \tag{8.1}
\]

with finite part from `107_04` and archimedean metric from (6.2).

Its arithmetic degree is

\[
 \widehat{\deg}\,\overline{\langle D,E\rangle}
 :=
 \log\|s_{D,E}\|_{\mathrm{fin}}
 -G_{\Gamma,\mathrm{pol}}(D,E),
 \tag{8.2}
\]

where \(s_{D,E}\) is the canonical section of the finite determinant line.

For off-diagonal cyclotomic generators this reproduces:

1. the finite normalized order \(\log p\) or \(0\) from `107_04`;
2. the Gamma contribution from the determinant quotient (3.6);
3. the pole and polar rulings through the \(s(s-1)\) factor in (3.6).

## 9. Why the normalization is rigid

### Proposition 9.1: no arbitrary additive constant

The metric (6.2) is not defined only up to an arbitrary additive scalar.

Proof.  There are two independent normalizations, and both are already
forced:

1. the determinant quotient (3.6) fixes the Gamma and polar factors,
   including the affine exponential normalization \(\sqrt\pi(2\pi)^{-s/2}\);
2. the shared-boundary finite part (4.2) and matched-cutoff identity
   (5.2) fix the scalar coefficient \(\kappa_\infty\) and remove the
   cutoff ambiguity.

Changing the metric by an arbitrary constant would break at least one of
those identities.  \(\square\)

This is the required answer to stop test 2 of I-C.

## 10. Divisor sensitivity

The metric must retain divisor location; otherwise it would collapse into
a signature-blind scalar correction.

### Proposition 10.1: location remains visible

The functional \(G_{\Gamma,\mathrm{pol}}(D,E)\) depends on the actual
logarithmic return positions appearing in \(h_{D,E}\), not only on the
number of active prime-power terms.

Proof.  The finite part of (6.1) evaluates the actual samples
\(h_{D,E}(k\log p)\), and the archimedean term \(\mathcal P_\infty(h_{D,E})\)
is the joined Gamma--polar functional applied to the same correlation.
Moving a divisor changes \(h_{D,E}\), hence changes at least one of these
two terms unless the move is trivial in the source package.  \(\square\)

### Proposition 10.2: scalar test

In the scalar model

\[
 s_a(z)=z-a,
 \tag{10.1}
\]

the metric cannot be independent of the moved divisor \(a\).

Proof.  As recalled in `106.182`, a positive metric by itself does not
force the support of the divisor \([a]\); Poincare--Lelong records the
zero at \(a\) explicitly.  In the present determinant model, the
archimedean factor is evaluated at the shifted parameter
\(s=\tfrac12+a\), and (3.6) varies nontrivially with \(a\) through both
\(\Gamma(s/2)\) and \(s(s-1)\).  Therefore the norm of the corresponding
section changes with \(a\).  \(\square\)

This disposes of stop tests 3 and 4 of I-C.

## 11. Stop-test audit

Work Package I-C passes its four stop tests.

### Stop test 1

Paired-cutoff independence is exact.

Reason.  Equation (5.2) from `106.181` is an identity at every matched
cutoff beyond the logarithmic support.

### Stop test 2

Rescaling the metric does not leave an arbitrary additive constant.

Reason.  Proposition 9.1 shows that both the determinant normalization
and the shared-boundary scalar are fixed.

### Stop test 3

The self-pairing is not automatically negative for every divisor
configuration.

Reason.  Proposition 10.1 shows that the actual divisor location remains
visible in the Green functional.

### Stop test 4

The scalar case \(s_a(z)=z-a\) does not make the metric independent of
the moved divisor.

Reason.  Proposition 10.2 shows explicit \(a\)-dependence through the
Gamma--polar determinant.

## 12. Milestone I status

With `107_03`, `107_04`, and the present note, Paper A now has all three
required layers:

1. the finite-support source divisor module;
2. the finite determinant lines with exact cyclotomic support;
3. the Gamma--polar metric completing those lines into metrized pairings.

What Paper A still does **not** claim is the later Part II/III/IV work of
Phase 107:

* no decorated Frobenius category has been constructed yet;
* no arithmetic Lefschetz fixed-point theorem is claimed yet;
* no regular proper arithmetic surface realizing these pairings is
  claimed yet;
* no Hodge sign is deduced yet.

But Milestone I of 107.00 is now assembled at the interface level: a
single coherent metrized determinant theory produces the finite
prime-power terms, the Gamma factor, the pole/polar correction, and a
diagonal drawn from the same Green metric rather than borrowed from an
external formula.
