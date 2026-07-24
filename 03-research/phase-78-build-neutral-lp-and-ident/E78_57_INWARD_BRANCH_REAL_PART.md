# E78.57 - The inward branch is exactly the sign of the centered real increment

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.54-E78.56 left the denominator front in the form

```text
branch condition   c_N < 0,
gap condition      GAP_N = 2 sqrt(1-s_N^2) - r_N > 0,    (IBR-1)
```

with

```text
w_N := Delta d_N / d_N,
r_N := |Delta d_N|/|d_N|,
s_N := DIRINC_N = sin(angle(Delta d_N,d_N)),
c_N := cos(angle(Delta d_N,d_N)).                         (IBR-2)
```

This note removes the separate branch variable: the inward branch is exactly the
sign of `Re(w_N)`.

## 2. Exact equivalence

Because

```text
Delta d_N = w_N d_N,                                      (IBR-3)
```

the angle between `Delta d_N` and `d_N` is exactly `arg(w_N)`. Therefore

```text
c_N = cos(angle(Delta d_N,d_N))
    = cos(arg(w_N))
    = Re(w_N)/|w_N|.                                      (IBR-4)
```

Since `|w_N| > 0` on the audited shell rows, we get the exact branch test

```text
INWARD-BRANCH
<=> c_N < 0
<=> Re(w_N) < 0.                                          (IBR-5)
```

So the branch condition is not a new geometric variable at all. It is exactly
the sign of the centered shell increment's real part.

## 3. Consequence for the denominator front

Substituting E78.57 into E78.56, the full denominator endpoint becomes:

```text
DEN-GAP-LOCK
<=> Re(w_N) < 0
    and
    2 sqrt(1-s_N^2) - r_N > 0.                            (IBR-6)
```

But `r_N = |w_N|`, so equivalently

```text
Re(w_N) < 0
and
|w_N| < 2 sqrt(1-s_N^2).                                  (IBR-7)
```

This is the cleanest mixed scalar form so far.

## 4. Audit

Certified data already available:

```text
E78_54_den_cone_lock_results.json
E78_44_den_centered_quotient_results.json
```

Direct comparison on the audited rows shows zero mismatches:

```text
branch mismatch count = 0 for both builds.               (IBR-8)
```

### Zeta

Every audited zeta row lies on the inward branch:

```text
Re(w_N) < 0 on 12/12 audited rows.                        (IBR-9)
```

Representative rows:

```text
sigma=1.0, N=10->12:
  c_N    = -0.9999981456
  Re(w_N)= -0.5057771152

sigma=3.0, N=12->14:
  c_N    = -0.9999274211
  Re(w_N)= -0.3819257889.                                 (IBR-10)
```

### Planted build

The planted build fails exactly where `Re(w_N)` changes sign:

```text
sigma=1.0, N=10->12:
  c_N    =  0.9420192582
  Re(w_N)=  6.4534770235

sigma=3.0, N=10->12:
  c_N    =  0.9391551088
  Re(w_N)=  6.2386795739.                                 (IBR-11)
```

Later planted rows can re-enter the inward branch precisely when `Re(w_N)` turns
negative again.

## 5. Honest reading

This is a real simplification.

It does not prove the branch cofinally, but it removes one layer of geometric
bookkeeping:

```text
to stay on the inward branch is exactly to keep Re(w_N) negative. (IBR-12)
```

So the denominator endpoint no longer needs a separate cosine variable. The live
content is now carried by the already-named centered increment `w_N`.

## 6. Status

```text
proved:
  the inward branch c_N<0 is exactly equivalent to Re(w_N)<0;

observed:
  all audited zeta rows satisfy Re(w_N)<0;

observed:
  the planted build fails exactly when Re(w_N) becomes positive;

reduced:
  the branch condition in DEN-GAP-LOCK to the sign of Re(w_N);

next:
  combine this with E78.56 to decide whether the scalar gap is now automatically
  positive from the already-audited regime, or isolate a separate shell law for
  Re(w_N) itself.
```
