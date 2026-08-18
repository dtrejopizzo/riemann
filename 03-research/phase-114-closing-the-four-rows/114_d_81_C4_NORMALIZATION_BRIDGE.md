# D.81 — Normalization bridge: the `c=4` cutoff-free matrix and `QW_{log 2}`

This note fixes the sign and normalization before the D.80 finite-band
certificate is used.  It does not extend that certificate to the full
support space.

Let `T=log(2)`, `L=2T=log(4)`, and translate `[-T,T]` to an interval of
length `L`.  For a trigonometric polynomial with symmetric Fourier
coefficient vector `u`, Groskin's cutoff-free matrix is, entry by entry,

```
Q_infty = W_(0,2) - W_R - W_p.                         (1)
```

This is Lemma 2.1 of arXiv:2607.02828v1, proved there from the closed
digamma/trigamma archimedean entries and the finite prime-power source.
The identification is independent of the paper's later zero-sum
dictionary.

The independent symbolic audit
`114_d_81_normalization_bridge_verify.py` checks on modes `-3,...,3` the
polar matrix as the crossed product of the two boundary moments, every
prime entry as the divided difference of its sine source, exact vanishing
of the `q=4` boundary contact, and
`log(pi)-psi(1/4)=log(pi)+EulerGamma+pi/2+3log(2)`.  The nonconstant
digamma/trigamma entry identity itself is cited to the primary Lemma 2.1;
the audit does not pretend to reprove that lemma.

In the phase-114 convention D.49/D.52 give on the same compact window

```
QW_T = M_T^* C M_T - B_nuc,T,                           (2)
```

and the explicit-formula definition is exactly
`W_(0,2)-W_R-W_p`.  Therefore translation of the interval and the
isometric symmetric Fourier embedding give

```
<u,Q_infty u> = QW_(log 2)(F_u,F_u).                    (3)
```

There is no sign reversal: on primitive vectors `M_T F_u=0`, D.52 gives
`QW_T=-B_nuc,T`, which is precisely the desired Hodge sign.  At `c=4` the
prime-power list is `2,3,4`; the `q=4` contribution lies at translation
length `L=2T` and hence has null `L^2` overlap, consistently with D.79.

Consequently D.80 rigorously proves positivity of `QW_(log 2)` on its
401-dimensional symmetric Fourier Galerkin band.  Equation (3) does not
identify this Fourier band with the prolate core of D.55 and supplies no
bound on the Schur coupling to its orthogonal complement.  That remaining
bridge must be certified separately.
