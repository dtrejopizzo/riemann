# E72.231 - Minimum-mode Fourier profile

## Purpose

E72.230 showed that raw phase candidates are insufficient. This probe lifts the minimum eigenvector
of `A_1` back to the full even Fourier side:

```text
f_min = B_Q v_min.
```

## Diagnostic

Script:

```text
E72_231_minmode_fourier_profile_probe.py
```

Output:

```text
E72.231 min-mode Fourier profile probe
High block minimum eigenvector lifted as f=bq vmin; reports dominant |m| modes
lam minEig top_abs_modes
 12 -2.226316e-01 0:0.323:-0.57 1:0.206:-0.45 30:0.034:-0.18 32:0.026:+0.16 31:0.011:-0.10 19:0.006:-0.08 4:0.006:-0.08 17:0.006:-0.08
 16 -2.186781e-01 1:0.269:+0.52 0:0.219:+0.47 39:0.106:+0.32 40:0.008:-0.09 4:0.001:+0.03 15:0.001:-0.03 12:0.001:-0.03 18:0.001:-0.03
 20 -2.243125e-01 0:0.487:-0.70 1:0.171:-0.41 47:0.044:-0.21 46:0.006:+0.08 2:0.005:+0.07 48:0.005:+0.07 45:0.004:+0.06 8:0.002:+0.04
 24 -2.542393e-01 0:0.477:-0.69 1:0.254:-0.50 2:0.001:-0.03 48:0.000:+0.02 43:0.000:-0.02 4:0.000:-0.02 56:0.000:-0.02 21:0.000:+0.02
 28 -2.409324e-01 1:0.301:-0.55 0:0.249:-0.50 63:0.063:+0.25 3:0.002:+0.04 6:0.002:-0.04 14:0.001:-0.03 5:0.001:+0.03 9:0.001:-0.03
 32 -1.368453e-01 0:0.292:+0.54 72:0.190:+0.44 1:0.080:+0.28 15:0.014:-0.12 16:0.008:-0.09 70:0.008:-0.09 27:0.006:-0.08 9:0.004:-0.08
```

## Reading

The minimum mode is dominated by low even frequencies:

```text
|m|=0,1.
```

Some windows show a small truncation-edge component near `|m|=N`, but the core is the two-dimensional
low block. This gives an explicit candidate subspace for min-max.
