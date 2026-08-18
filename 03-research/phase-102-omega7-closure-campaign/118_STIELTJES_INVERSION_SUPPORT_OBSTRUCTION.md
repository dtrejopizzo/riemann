# Stieltjes inversion and the support obstruction

## Purpose

The positive boundary measure target asks for a positive measure supported on
the critical line in the line coordinate. A natural idea is to construct a
positive measure by Stieltjes or Poisson inversion from \(\xi\). This document
records exactly what that construction gives and why it is not yet A1.

## Riesz measure of the completed function

The function
\[
  u(z)=\log\left|\xi\left({1\over2}+z\right)\right|
\]
is subharmonic. Its Riesz measure is positive:
\[
  {1\over2\pi}\Delta u
  =
  \sum_{\rho}m_\rho\,\delta_{\rho-1/2},
\]
with the usual paired interpretation at multiplicities.

Thus positivity of a measure is not the problem. The Riesz measure is always
positive. The problem is its support.

## Required support collapse

The positive boundary measure target needs this positive measure to live on
the imaginary axis:
\[
  \mathrm{supp}\,\Delta u\subset i\mathbb R.
\]

That support statement is exactly the critical-line statement. If it is
proved, then the Li sum-of-squares follows. If it is assumed, the proof is
circular.

## Why ordinary inversion does not close A1

Poisson or Stieltjes inversion can recover the divisor measure from boundary
data where the function is known. But it recovers the full two-dimensional
divisor in the line coordinate, not a one-dimensional positive measure on
the imaginary axis.

An off-line zero produces a positive atom away from the imaginary axis. There
is no sign contradiction in the Riesz measure itself. The contradiction only
appears after applying the Li transform, where the corresponding
\[
  \left|1-{1\over\rho}\right|>1
\]
mode gives a geometric negative subsequence.

## Eliminated class

The following class does not close A1:
\[
  \hbox{construct the positive Riesz measure of }\log|\xi|
  \hbox{ and call it the boundary measure}.
\]

That measure is positive but not known to be supported on the critical line.
It is a divisor measure, not the required boundary Herglotz measure.

## Live theorem

The missing theorem can be stated as a support-collapse theorem:

The Euler--Gamma data force
\[
  \mathrm{supp}\,\Delta\log\left|\xi\left({1\over2}+z\right)\right|
  \subset i\mathbb R.
\]

This theorem is equivalent in strength to the positive boundary measure
target and would close A1.

## Status

Stieltjes/Riesz inversion gives positivity but not support. The support
collapse remains open and is another exact formulation of the A1 force-RH
core.
