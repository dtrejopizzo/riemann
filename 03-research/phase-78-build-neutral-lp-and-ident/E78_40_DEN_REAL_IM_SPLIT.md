# E78.40 - Denominator quotient skew splits into real floor plus imaginary part

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.39 reduced the denominator side to the raw quotient

```text
q_b,N := (1-theta_N+2)/(1-theta_N),                       (DRI-1)
```

with phase rigidity equivalent to small skew

```text
Im(q_b,N) / Re(q_b,N).                                    (DRI-2)
```

This note splits that condition into its two elementary ingredients:

```text
positive real floor  +  small imaginary part.            (DRI-3)
```

## 2. Exact elementary bound

Whenever `Re(q_b,N) > 0`,

```text
|Delta phi_b,N|
 = |arctan(Im(q_b,N)/Re(q_b,N))|
 <= |Im(q_b,N)| / Re(q_b,N).                             (DRI-4)
```

So if `Re(q_b,N)` admits any positive lower floor `c_N > 0`, then

```text
|Delta phi_b,N|
 <= |Im(q_b,N)| / c_N.                                   (DRI-5)
```

In particular, on any branch where `Re(q_b,N) >= c_* > 0`,

```text
small |Im(q_b,N)|
=> DEN-QUOTIENT-SKEW-SMALLNESS
=> DEN-PHASE-RIGIDITY.                                   (DRI-6)
```

## 3. Probe audit

Companion:

```text
E78_40_den_real_im_split_probe.py
E78_40_den_real_im_split_results.json
```

The probe records the actual real floor and imaginary part on the audited ladder.

### Zeta

Across the audited zeta rows:

```text
min Re(q_b,N)    = 0.4942228848151406
max |Im(q_b,N)|  = 0.00460174785080823.                  (DRI-7)
```

Representative rows:

```text
sigma=1.0, N=10->12:
  q = 0.4942228848 + 0.0009740449 i
  |phase| <= 0.0009740449 / 0.4942228848 = 0.0019708615

sigma=3.0, N=12->14:
  q = 0.6180742111 - 0.0046017479 i
  |phase| <= 0.0046017479 / 0.6180742111 = 0.0074452999. (DRI-8)
```

So on the audited zeta ladder the real part is safely bounded away from `0`, and
phase rigidity is already equivalent to small imaginary part at a fixed real
scale.

### Planted build

The planted build does not fail by loss of real positivity on the audited rows;
it fails because the imaginary part is too large relative to the same scale.

Representative rows:

```text
sigma=1.0, N=10->12:
  q = 7.4534770 + 2.2988077 i

sigma=3.0, N=12->14:
  q = 0.5187196 + 0.2603806 i.                           (DRI-9)
```

So the bad mechanism is not sign loss of `Re(q_b,N)` but large imaginary shell
drift.

## 4. Consequence

This gives the smallest denominator target so far on the audited zeta branch:

```text
DEN-IMAG-SMALLNESS:
  prove that Im(q_b,N) stays small cofinally,
  together with a positive real floor for Re(q_b,N).      (DRI-10)
```

Then

```text
positive real floor
+ small imaginary part
=> small quotient skew
=> phase rigidity
=> small DENDIR_N.                                       (DRI-11)
```

This is a genuine reduction because the live content is now pushed onto the
imaginary part of one explicit shell quotient, with the real scale separated out.

## 5. Honest reading

This note does not yet prove a theorem-grade real floor or imaginary bound
cofinally. What it does prove is that on the audited zeta ladder the denominator
phase front has reduced to the simplest possible real-imag decomposition of
`q_b,N`.

That is a useful endpoint because it shows exactly what a shell update law would
have to control.

## 6. Status

```text
proved:
  small denominator phase follows from small imaginary part of q_b,N once
  Re(q_b,N) has a positive floor;

observed:
  on the audited zeta ladder Re(q_b,N) stays in [0.4942, 0.7383] while
  |Im(q_b,N)| stays below 0.00461;

observed:
  the planted build fails through large imaginary part rather than through
  negative real part;

reduced:
  DEN-QUOTIENT-SKEW-SMALLNESS to DEN-IMAG-SMALLNESS plus a positive real floor;

next:
  search for an exact shell law governing the imaginary part of
  (1-theta_N+2)/(1-theta_N).
```
