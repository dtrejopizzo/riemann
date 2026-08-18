# Row (d): falsification test for the continuous-reference remainder

## Question

The strict continuous Castelnuovo--Severi form

\[
 Q_0(F)=\iint e^{|t-s|/2}F(t)\overline{F(s)}\,dt\,ds\le0
\]

suggests writing

\[
 B_{\rm nuc}=Q_0+R_{\rm ar}.
\]

The sufficient condition `R_ar <= 0` would close row (d).  It is stronger
than the required inequality and therefore must be tested before it is used
as a construction target.

## Probe

The executable

`114_d_11_continuous_remainder_probe.py`

uses compactly supported `C-infinity` windowed cosine spaces.  It imposes
the two exponential ruling moments by an SVD nullspace and computes the
finite-prime contact, the Fourier--gamma multiplier and `Q_0`.  It then
finds the extremal generalized eigenvalues relative to the `L^2` Gram
matrix.

Zero-padding factors 8, 16 and 32 give identical displayed results on the
radius-two trial space:

```
T=2  max(R_ar)=+0.354343194  min(R_ar)=-4.11242396
T=3  max(R_ar)=+0.819015830  min(R_ar)=-5.49906524
T=4  max(R_ar)=+1.37693814   min(R_ar)=-0.697716578
```

The discrete ruling-moment residuals are below `8e-16`.  The computed
largest eigenvalue of `B_nuc` is only `1e-5`--`3e-4`; that small wrong-sign
value must be treated as quadrature/interpolation error, not as arithmetic
evidence.  In contrast, the positive eigenvalues of `R_ar` are three to
four orders of magnitude larger and stable under Fourier zero-padding.

## Verdict

This is strong falsification evidence that `R_ar <= 0` is false.  The
continuous reference form remains a correct strict Hodge model, but its
arithmetic discrepancy is indefinite.  It cannot be used as a separately
negative Green correction.

This numerical result is not a mathematical counterexample until one trial
vector is exported and both signs are enclosed with rigorous quadrature
error bounds.  The appropriate next step is an interval certificate for
one positive `R_ar` vector.  Irrespective of that certificate, no claim in
the paper may use `R_ar <= 0`.

The surviving target is the sharp combined inequality

\[
 B_{\rm nuc}(f,f)=Q_0(F)+R_{\rm ar}(F)\le0,
\]

not a termwise sign for `R_ar`.
