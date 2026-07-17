# E72.60 -- Post-main scalar endpoint discrepancy probe

**Date:** 2026-07-08.
**Role:** measure the corrected scalar endpoint object after subtracting the continuous PNT main term.

## 0. Correct object

After E72.59, the relevant scalar endpoint discrepancy is:

```text
D_x(s;z)
 = sum_{n<=x} Lambda(n)(n/x)^z n^(-1/2)a_{x,s}(log n)
   - int_0^L exp(z(y-L))exp(y/2)a_{x,s}(y)dy,
```

where:

```text
a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>.
```

This is the scalar channel of:

```text
S_x^{err}(z)
 = S_x^Lambda(z)-S_x^{cont}(z).
```

## 1. Numerical signal

Representative corrected values:

```text
z=6:
  x=36    |prime|=1.158e-2, |cont|=9.287e-3, |err|=3.088e-3, sqrt(x)|err|=1.853e-2
  x=64    |prime|=5.908e-3, |cont|=6.897e-3, |err|=1.112e-3, sqrt(x)|err|=8.897e-3
  x=144   |prime|=3.092e-3, |cont|=2.295e-3, |err|=7.971e-4, sqrt(x)|err|=9.566e-3

z=10:
  x=36    |err|=1.698e-3, sqrt(x)|err|=1.019e-2
  x=64    |err|=7.972e-4, sqrt(x)|err|=6.378e-3
  x=144   |err|=3.424e-4, sqrt(x)|err|=4.109e-3

z=14:
  x=36    |err|=1.385e-3, sqrt(x)|err|=8.309e-3
  x=64    |err|=5.252e-4, sqrt(x)|err|=4.202e-3
  x=144   |err|=1.794e-4, sqrt(x)|err|=2.153e-3
```

The relative error remains around `0.2-0.35` in these small windows, but the absolute corrected error
is small and the half-power-scaled error is also small.

## 2. Interpretation

This supports the corrected target:

```text
<v_{x,s},S_x^{err}(z)k_x> -> 0.
```

The smallness is not a property of:

```text
the raw prime endpoint sum,
the continuous endpoint main,
or the rank-one endpoint factor alone.
```

It is a post-main scalar discrepancy phenomenon in the compressed Loewner channel.

## 3. Current finite target

### LFDC -- Loewner-Feshbach Discrepancy Cancellation

For compact Cauchy-height and spectral windows:

```text
sup_{s,z}
|<C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
  [S_x^Lambda(z)-S_x^{cont}(z)]k_x>| -> 0.       (LFDC)
```

and the same estimate after one `s`-derivative.

## 4. Status

```text
observed: corrected post-main scalar discrepancy is small in the finite CCM harness;
open: prove LFDC from the Loewner commutator identity and Feshbach equation.
```

This is now the clean finite matrix statement to attack.
