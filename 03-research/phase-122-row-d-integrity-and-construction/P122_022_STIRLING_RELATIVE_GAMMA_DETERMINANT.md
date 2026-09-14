# P122 -- the Stirling-relative Gamma determinant class

## Status

`IMPORTED ASYMPTOTICS/RESTRICTED FRAMEWORK + PROVED SPECIALIZATION`.
Stirling--Lerch asymptotics and the Hardy `H^(1/2)` restrictedness criterion
are classical; the specific residual factor and its type audit are derived
here.  This note constructs a restricted archimedean determinant datum
**relative to** its universal Stirling chirp.  It
does not construct the Gamma--Euler transmission or prove either gate of
P122.020.

## 1. The full Gamma scattering is not restricted

Put `a=1/4` and

\[
 b_\infty(\tau)=\pi^{-i\tau}
 {\Gamma(a+i\tau/2)\over\Gamma(a-i\tau/2)}
 =e^{i\phi_\infty(\tau)},
 \qquad \phi_\infty(0)=0.                         \tag{1.1}
\]

The phase is odd and

\[
 \phi_\infty'(\tau)
 =\operatorname {Re}\psi(a+i\tau/2)-\log\pi.     \tag{1.2}
\]

Stirling expansion, with one differentiated remainder, gives

\[
 \begin{aligned}
 \phi_\infty(\tau)
  &={\tau}\log{|\tau|\over2\pi}-\tau
    -{\pi\over4}\operatorname {sgn}\tau
    +O(|\tau|^{-1}),\\
 \phi_\infty'(\tau)
  &=\log{|\tau|\over2\pi}+O(|\tau|^{-2}).        \tag{1.3}
 \end{aligned}
\]

The first correction is in fact `1/(24 tau)+O(tau^(-3))`; its value is not
needed below.

### Proposition 1.1 -- ordinary restrictedness fails

Let `P_+` be the Hardy projection on `L^2(R)`.  Then

\[
                         [P_+,M_{b_\infty}]       \tag{1.4}
\]

is not Hilbert--Schmidt.

#### Proof

The Hilbert--Schmidt seminorm is, up to a fixed positive normalization, the
homogeneous Gagliardo integral

\[
 \iint_{\mathbb R^2}{|b_\infty(x)-b_\infty(y)|^2\over|x-y|^2},dx\,dy.
                                                               \tag{1.5}
\]

For large `x`, (1.3) makes the phase derivative positive and comparable to
`log x`, with relative variation tending to zero on intervals of length
`O(1/log x)`.  Choose constants `0<c<C` so that for

\[
 {c\over\log x}<y-x<{C\over\log x}                \tag{1.6}
\]

the phase difference stays in a compact subinterval of `(0,pi)`.  The
numerator in (1.5) is then bounded below, while integration in `y` over
(1.6) contributes a constant times `log x`.  Integrating this lower bound
over all sufficiently large `x` diverges.  QED.

Thus the phrase “quarter-Gamma determinant line” needs a relative
polarization; the full phase is not an element of the ordinary restricted
unitary group.

## 2. Extraction of the universal chirp

Choose once and for all an even smooth cutoff `chi` which is zero on
`[-1,1]` and one outside `[-2,2]`.  Define the odd smooth reference phase

\[
 \phi_{\rm St}(\tau)=\chi(\tau)
 \left(
 \tau\log{|\tau|\over2\pi}-\tau
 -{\pi\over4}\operatorname {sgn}\tau
 \right)                                           \tag{2.1}
\]

and the residual unitary

\[
 q_\infty(\tau)
 :=b_\infty(\tau)e^{-i\phi_{\rm St}(\tau)}
 =e^{i\rho_\infty(\tau)}.                         \tag{2.2}
\]

Different admissible cutoffs change `phi_St` by a compactly supported
smooth odd function.  Hence they give the same restricted-polarization
class, with a canonical restricted transition between representatives.

### Theorem 2.1 -- the residual Gamma phase is restricted

One has

\[
 q_\infty-1\in H^1(\mathbb R)
 \subset H^{1/2}(\mathbb R),
 \qquad [P_+,M_{q_\infty}]\in\mathcal S_2.        \tag{2.3}
\]

#### Proof

Equations (1.3) and (2.1) give

\[
 \rho_\infty(\tau)=O(|\tau|^{-1}),
 \qquad \rho_\infty'(\tau)=O(|\tau|^{-2})        \tag{2.4}
\]

outside a compact set.  On the compact transition region both functions
are smooth.  Since `|e^(ix)-1|<=|x|`, (2.4) implies

\[
 q_\infty-1\in L^2,
 \qquad q_\infty'=i\rho_\infty'q_\infty\in L^2. \tag{2.5}
\]

This proves the first inclusion in (2.3); the second is the elementary
Fourier inequality `|xi|<=1+xi^2`.  Finally, the standard Hardy kernel
calculation identifies the squared Hilbert--Schmidt norm of the commutator
with a constant multiple of the homogeneous `H^(1/2)` seminorm, proving
the last assertion.  QED.

## 3. The constructed archimedean object

The theorem defines an honest relative restricted-Grassmannian point and
determinant line

\[
 D^{\rm rel}_\infty
 =\bigl(P_+,q_\infty P_+q_\infty^*,
        L^{\rm det}_\infty,\phi_{\rm St}\bigr).    \tag{3.1}
\]

Here `phi_St` is retained as background polarization data rather than
discarded.  The exact Gamma connection splits as

\[
 \phi_\infty'
 =\phi_{\rm St}'+\rho_\infty'.                    \tag{3.2}
\]

The residual term is an ordinary restricted determinant connection.  The
background term carries the logarithmic high-energy density and must be
realized by the already constructed quarter-oscillator/Bergman bulk.  If it
were simply subtracted from the comparison, the exact Gamma multiplier
would be lost.

This improves the type statement in P122.016:

```text
full b_infinity in ordinary GL_res                 FALSE
Stirling-relative q_infinity in ordinary GL_res    PROVED
universal high-energy chirp retained separately    CONSTRUCTED DATUM
exact Gamma connection recovered by their sum      PROVED
```

## 4. Compatibility and remaining no-go

Both `phi_St` and `rho_infinity` are odd; their derivatives are even.
Therefore the Real-symmetric mixed cocycle of either part with every Euler
phase still vanishes by the parity proof of P122.018.  The relative
factorization repairs restrictedness but does not manufacture a mixed
Gamma--Euler anomaly.

Nor does (2.3) imply Gate R.  P122.021 proves that sharp-window causal
translation can take a smooth function out of the physical `H^(1/2)`
class.  The required map is still a transmission across the cut, not the
mere membership of `q_infinity` in a restricted group.

The new finite-plus-infinite determinant skeleton is therefore

\[
 D^{\rm skel}_{T}
 =\bigl(D^{\rm fin}_{T,{\rm sf}},
        D^{\rm rel}_\infty,
        \text{quarter-oscillator background}\bigr).       \tag{4.1}
\]

It contains exact determinant objects on both sides and the full Gamma
normalization.  What it still lacks is a correspondence morphism joining
their boundary traces and proving Gates R and S.

## 5. Falsifiability boundary

The construction uses only the universal Gamma factor and therefore also
exists for non-Euler models having that factor.  It is not by itself the
Davenport--Heilbronn or shifted-pair falsifier.  Arithmetic specificity
must enter through the missing transmission to the Frobenius-coherent Bohr
module.

No positivity of the Weil form, no zero divisor of `xi`, and no spectral
subspace of `Delta_T` is used in (1.1)--(4.1).
