# E72.285 -- APCB autocorrelation form

**Purpose.** State the arithmetic positive-part ceiling as an exact finite autocorrelation inequality.

E72.284 reduces the upper complement bound to:

```text
MUCB: ||C_model||=O(L^2),
APCB: lambda_max(Delta_arith)_+=O(L^2).
```

This note rewrites `APCB` without spectral hiding.

## Exact form

For Fourier coefficients `v=(v_n)` on the finite mesh, let

```text
f_v(t)=L^(-1/2) sum_n v_n exp(2pi i n t/L).
```

The CCM overlap cell satisfies

```text
<v,Q_yv>
= 2 Re int_0^(L-y) f_v(t+y) conjugate(f_v(t)) dt.             (AC)
```

The arithmetic perturbation is

```text
Delta_arith
= - sum_{p^k<=e^L} (log p)p^(-k/2) B_even^T Q_{k log p}B_even.
```

Thus `APCB` is exactly:

```text
sup_{||u||=1}
[- sum_{p^k<=e^L} (log p)p^(-k/2)
   2 Re int_0^(L-k log p)
     f_{B_even u}(t+k log p) conjugate(f_{B_even u}(t)) dt]_+
<= C L^2.                                                    (APCB-AC)
```

This is a finite, explicit, model-normalized arithmetic autocorrelation ceiling.

## Why absolute values are wrong

Since `||Q_y||<=2`, the incoherent ceiling is

```text
2 sum_{p^k<=e^L} (log p)p^(-k/2),
```

which is much larger than the observed positive part.  Therefore APCB must use coherent
autocorrelation, not termwise absolute values.

## Probe

Run:

```text
python3 E72_285_apcb_autocorrelation_probe.py
```

Output:

```text
E72.285 APCB autocorrelation probe
Delta_arith=-sum Lambda(n)n^-1/2 Q_log n; APCB asks lambda_max(Delta_arith)_+=O(L^2).
incoh=2 sum Lambda(n)n^-1/2 is the absolute autocorrelation ceiling.
lam L dim cells posDelta/L2 negDelta/L2 absDelta/L2 incoh/L2 rebuildRel
 16 5.545177  41    70 1.617975e-01 -5.841092e-01 5.841092e-01 1.895554e+00 5.168e-16
 20 5.991465  49    97 1.530683e-01 -6.240223e-01 6.240223e-01 2.077903e+00 6.938e-16
 24 6.356108  57   126 1.428683e-01 -6.624494e-01 6.624494e-01 2.231231e+00 7.924e-16
 28 6.664409  65   160 1.406409e-01 -6.999850e-01 6.999850e-01 2.396519e+00 6.682e-16
 32 6.931472  73   198 1.327397e-01 -7.356424e-01 7.356424e-01 2.555856e+00 7.891e-16
```

## Reading

The exact reconstruction error is at roundoff, so `(APCB-AC)` is the correct finite target.

The observed positive ceiling is about `0.13--0.16 L^2`, while the incoherent absolute ceiling is about
`1.9--2.6 L^2` in these windows and grows with the cutoff.  This confirms that APCB is a coherent
autocorrelation estimate, not a prime-cell absolute estimate.

The next proof-facing task is to prove `(APCB-AC)` uniformly.
