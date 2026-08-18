# 107.222 -- The rooted normalization needs a relative codifferent dualizer

## 1. Base canonical data versus relative ramification

Connes--Consani's canonical divisor on the arithmetic base is

\[
 K_{\mathrm{CC}}=-2\{2\}.
 \tag{1.1}
\]

For a normalized rooted component

\[
 \pi_n:\mathrm{Spec}\,O_n
 =\mathrm{Spec}\,\mathbb Z[\zeta_n]
 \longrightarrow\mathrm{Spec}\,\mathbb Z,
\]

the trace-dualizing module is

\[
 \omega_{n/\mathbb Z}
 =\mathrm{Hom}_{\mathbb Z}(O_n,\mathbb Z)
 =\mathfrak D_n^{-1}.
 \tag{1.2}
\]

Its finite divisor is supported at every rational prime ramified in the
cyclotomic field, equivalently at primes dividing \(n\).

## 2. Pullback-only no-go

### Theorem 2.1

There is no identification of all componentwise dualizers
\(\mathfrak D_n^{-1}\) with the pullback of the single base divisor
\(K_{\mathrm{CC}}\).

### Proof

The pullback of (1.1) is supported only above 2.  For \(n=5\), the
different has norm

\[
 |\mathrm{disc}\,\mathbb Q(\zeta_5)|=5^3,
\]

and is supported above 5.  For \(n=9\), its norm is

\[
 |\mathrm{disc}\,\mathbb Q(\zeta_9)|=3^9,
\]

and is supported above 3.  These nonzero odd-prime divisors cannot be
the pullback of a divisor supported at 2.  \(\square\)

This is a support obstruction, not merely a degree mismatch.

## 3. Correct finite rooted dualizer

At level \(L\), define

\[
 \omega^{\mathrm{rel}}_L
 =\coprod_{n\mid L}\mathfrak D_n^{-1}
 \quad\text{on}\quad
 \mathcal R_L=\coprod_{n\mid L}\mathrm{Spec}\,O_n.
 \tag{3.1}
\]

Since \(\mathcal R_L\hookrightarrow\mathcal R_{L'}\) is open and closed
for \(L\mid L'\), every old summand of (3.1) is retained literally.
Thus \(\omega_L^{\mathrm{rel}}\) forms a strict directed dualizing system.

On each component, tensoring the Koszul complex by (3.1) gives exactly
the perfect duality of 107_221.  Therefore the finite rooted canonical
package is not a pullback but a relative formula:

\[
 \boxed{
 \omega_{\mathrm{rooted}}
 =\pi^*(\omega_{\mathrm{base}})
 \otimes\omega^{\mathrm{rel}}.}
 \tag{3.2}
\]

Equation (3.2) states the required architecture.  The relative factor
is constructed algebraically.  The tensor product with the tolerant
\(\mathbb S[\pm1]\)-dualizer \(H^1(K_{\mathrm{CC}})\), and a theorem that
it gives global Serre duality on the absolute square, remain open.

## 4. Consequence

The componentwise \(H^1\) route survives, but any RR formula that uses
only \(-2\{2\}\) after passing to cyclotomic covers omits the relative
different and is false.  Ramification terms at odd primes are forced
before any archimedean correction or Hodge argument.

## 5. Falsifier

`107_222_relative_codifferent_dualizer_on_rooted_normalization.sage`
computes actual cyclotomic differents, discriminants and ramified prime
supports at six fixed conductors.  It rejects the base-support-only
model whenever odd ramification occurs and verifies that unchanged
components retain identical codifferent ideals at larger rooted levels.

