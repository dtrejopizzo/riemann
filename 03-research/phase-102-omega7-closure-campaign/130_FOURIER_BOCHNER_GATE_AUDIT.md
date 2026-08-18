# Fourier-Bochner gate audit

## Purpose

The completed function
\[
  \Xi(t)=\xi\left({1\over2}+it\right)
\]
has a classical cosine-transform representation with a positive even kernel.
This is a tempting positivity route to A1.  This document separates what that
positivity proves from the stronger real-zero theorem actually needed.

## Cosine representation

In a standard theta-derived normalization,
\[
  \Xi(t)=\int_0^\infty \Phi(u)\cos(tu)\,du,
\]
where \(\Phi(u)>0\) for \(u\ge0\).  Equivalently, after even extension,
\[
  \Xi(t)=\int_{\mathbb R}e^{itu}\,d\mu(u)
\]
with \(d\mu(u)=\frac12\Phi(|u|)\,du\ge0\).

By Bochner positivity, the kernel
\[
  (x,y)\mapsto \Xi(x-y)
\]
is positive definite on the real line:
\[
  \sum_{j,k}c_j\overline{c_k}\,\Xi(x_j-x_k)\ge0.
\tag{1}
\]

## Why Bochner positivity is not A1

Positive definiteness on the real line does not force an entire function to
have only real zeros.  A simple counterexample is
\[
  F(z)=e^{-\sigma^2z^2/2}\left(1+\varepsilon\cos(az)\right),
  \qquad
  \sigma>0,\ a>0,\ 0<\varepsilon<1.
\tag{2}
\]

Indeed, \(F\) is the Fourier transform of the positive finite measure
\[
  e^{-\sigma^2z^2/2}
  \quad\hbox{times}\quad
  \delta_0+{\varepsilon\over2}\delta_a+{\varepsilon\over2}\delta_{-a}
\]
in transform notation, so \(F\) is positive definite.

But its zeros solve
\[
  1+\varepsilon\cos(az)=0.
\]
Since \(1/\varepsilon>1\), these zeros are non-real:
\[
  az=(2m+1)\pi\pm i\,\operatorname{arcosh}(1/\varepsilon),
  \qquad m\in\mathbb Z.
\]

Thus the implication
\[
  \hbox{positive Fourier measure}
  \Longrightarrow
  \hbox{all zeros real}
\]
is false.

Consequently the positive kernel \(\Phi\) for \(\Xi\) does not by itself
prove Omega7, A1, or RH.

## Correct stronger target

The Fourier route can close A1 only if it proves a substantially stronger
property, for example:

1. \(\Phi\) is a Pólya-frequency kernel of infinite order;
2. every Jensen polynomial associated to \(\Xi\) is hyperbolic, with a
   cofinal limiting theorem;
3. the de Branges/Hermite--Biehler kernel built from \(\Xi\) is positive by
   an Euler--Gamma construction;
4. the Fourier-side convolution operator has a total-positivity structure
   forcing the transform into the Laguerre--Pólya class.

Any of these would imply real zeros of \(\Xi\), hence Li positivity and A1
through the phase-102 assembly.  But each is a force-RH theorem, not a
consequence of ordinary Bochner positivity.

## Relation to existing gates

This Fourier gate refines the total-positivity and de Branges gates:

- `120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md` eliminates finite total
  positivity and identifies the needed infinite property.
- `119_DE_BRANGES_GATE_FOR_A1.md` eliminates divisor-built
  Hermite--Biehler constructions.
- The present document eliminates the weaker Fourier-positive route.

The surviving Fourier theorem is therefore:

\[
  \hbox{Euler--Gamma data prove a total-positive or Hermite--Biehler
  structure for }\Xi.
\]

If proved independently of zero locations, this closes A1.  Without the
stronger structure, Bochner positivity is only a consistency property.

## Off-line discriminator

An off-line control can still have a positive Fourier representation after
multiplying by a positive-definite factor of the kind in (2), while acquiring
non-real zeros.  Therefore a proof depending only on Fourier-measure
positivity would not distinguish the off-line mode required by the phase-102
discriminator.

The successful Fourier-side theorem must fail for such a control at the
level of total positivity, Hermite--Biehler interlacing, or cofinal
hyperbolicity, not merely at the final zero interpretation.

## Status

Closed as an audit of the Bochner route.  Positivity of the cosine-transform
kernel does not close A1.  The viable Fourier route is exactly the stronger
infinite total-positivity/de Branges gate already carrying the full A1 load.
