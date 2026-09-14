# P122 -- the Stirling--Frobenius canonical relation does not glue the ports

## Status

`PROVED-IN-REPOSITORY` as a microlocal identification and a no-go theorem.
The Stirling chirp converts archimedean frequency scale into logarithmic
position, but its exact unitary commutes with every Euler translation.
Therefore stationary-phase sampling at `|tau|=2 pi n` is not the missing
Gamma--Euler transmission law.

## 1. The tempting canonical relation

Outside the compact smoothing region of P122.022, on the positive-frequency
branch,

\[
 \phi_{\rm St}(\tau)
 =\tau\log{\tau\over2\pi}-\tau-\frac\pi4,
 \qquad
 \phi_{\rm St}'(\tau)=\log{\tau\over2\pi},
 \qquad
 \phi_{\rm St}''(\tau)=\frac1\tau.                \tag{1.1}
\]

Multiplication by `exp(i phi_St)` in frequency is a Fourier integral
operator with canonical shear

\[
                  (t,\tau)\longmapsto
                  (t-\phi_{\rm St}'(\tau),\tau),  \tag{1.2}
\]

for the convention `Fourier(f)(tau)=integral exp(-it tau)f(t)dt`.

Consequently a shear of oriented length `-log n` occurs at

\[
 \phi_{\rm St}'(\tau)=\log n
 \quad\Longleftrightarrow\quad
 \tau=2\pi n.                                     \tag{1.3}
\]

The convolution kernel has phase `t tau+phi_St(tau)`; its positive
stationary point is `tau=2 pi e^(-t)`.  Thus the universal Gamma chirp
really does contain the classical exponential/logarithmic change of scale
behind Poisson--Tate analysis.

## 2. Exact commutation defeats the proposed gluing

Let

\[
 U_{\rm St}=\mathcal F^{-1}M_{e^{i\phi_{\rm St}}}\mathcal F,
 \qquad
 V_a=\mathcal F^{-1}M_{e^{-ia\tau}}\mathcal F.     \tag{2.1}
\]

Here `V_a` is translation by `a`; every Euler return is
`V_(log n)` multiplied by its half-density.

### Theorem 2.1 -- the global Stirling carrier has zero Euler commutator

For every real `a`,

\[
                 [U_{\rm St},V_a]=0.              \tag{2.2}
\]

The same is true with the exact Gamma scattering `b_infinity` or the
restricted residual `q_infinity` in place of the Stirling phase.

#### Proof

All three operators and `V_a` are Fourier multipliers.  Their symbols
commute pointwise.  QED.

Thus (1.3) is a canonical-relation coincidence, not an exact sampling
identity.  Stationary phase can approximate the kernel near a scale; it
cannot turn (2.2) into a nonzero seam, determinant anomaly or local-to-global
reciprocity law.

## 3. Compression produces only the known boundary anomaly

Let `P_T` denote restriction/extension for `I_T`.  Although the global
operators commute, their compressions need not:

\[
 [P_TU_{\rm St}P_T,P_TV_aP_T]
 \quad\text{is supported by paths crossing the boundary of }I_T. \tag{3.1}
\]

Algebraically every such term is built from commutators `[P_T,V_a]` and
`[P_T,U_St]`.  For `a=log n`, `[P_T,V_a]` is exactly the activation strip
of P122.021.  Summing the half-density returns gives the one-sided Euler
history identified in P122.018 and phase 121.

Therefore the chirp offers no third alternative:

```text
global Stirling/Gamma carrier      commutes with all Euler returns;
sharp-window compressed carrier   couples them only through boundary history.
```

Killing the second line is Gate R/S, not a consequence of the first.

## 4. Relation to the existing Poisson carrier

Composing `U_St` with a Fourier transform changes translations into
modulations, but this is a unitary change of coordinates.  It retains the
same commutation/intertwining data and is the microlocal skeleton already
present in the Fourier--Poisson/Meyer realization.  Without the exact
integer summation morphism it gives no arithmetic sampling theorem; with
that morphism its cokernel is the previously identified Meyer spectral
quotient.

Hence the next construction must use more than the canonical shear (1.2).
It needs an arithmetic transmission morphism which is sensitive to the
Frobenius factorization of the integer lattice and controls the sharp-window
boundary.  The asymptotic equality (1.3) cannot substitute for that
morphism.
