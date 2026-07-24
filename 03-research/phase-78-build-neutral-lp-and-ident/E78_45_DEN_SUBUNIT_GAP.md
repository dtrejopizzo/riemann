# E78.45 - Centered denominator horizontality is a subunit real-gap condition

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.44 showed that the denominator direction law is governed by the centered
quotient

```text
w_N := Delta d_N / d_N = q_N - 1,                        (DSG-1)
```

where

```text
q_N := (1-theta_N+2)/(1-theta_N).                        (DSG-2)
```

This note isolates the only genuinely new ingredient contributed by that
re-centering: the **subunit real gap**

```text
1 - Re(q_N).                                             (DSG-3)
```

## 2. Exact affine identities

Since `w_N = q_N - 1`, we have immediately

```text
-Re(w_N) = 1 - Re(q_N),                                  (DSG-4)
Im(w_N)  = Im(q_N).                                      (DSG-5)
```

Therefore, whenever `Re(q_N) < 1`,

```text
|Im(w_N)| / (-Re(w_N))
 = |Im(q_N)| / (1 - Re(q_N)).                            (DSG-6)
```

Combining E78.44 with `(DSG-6)` yields the exact left-half-plane skew control

```text
|DIRINC_N|
 = |Im(w_N)| / |w_N|
 <= |Im(w_N)| / (-Re(w_N))
 = |Im(q_N)| / (1 - Re(q_N)).                            (DSG-7)
```

Thus denominator horizontality reduces to two elementary shell conditions:

```text
SUBUNIT-GAP:     1 - Re(q_N) >= c_* > 0,
IMAG-SMALLNESS:  |Im(q_N)| is small.                     (DSG-8)
```

## 3. What is genuinely new here

E78.40 had already reduced the denominator side to

```text
positive real floor for Re(q_N) + small |Im(q_N)|.       (DSG-9)
```

E78.44 did **not** create a new imaginary term: by `(DSG-5)` it is the same
`Im(q_N)`.

So the only new theorem-grade content in the centered picture is the upper real
barrier

```text
Re(q_N) <= 1 - c_* < 1,                                  (DSG-10)
```

equivalently the positive centered real floor `-Re(w_N) >= c_*`.

That is the honest reduction.

## 4. Probe audit

Companion:

```text
E78_45_den_subunit_gap_probe.py
E78_45_den_subunit_gap_results.json
```

The probe imports the certified E78.40 and E78.44 results and verifies
`(DSG-4)`-`(DSG-7)` to roundoff.

### Zeta

Across the audited zeta ladder:

```text
min (1 - Re(q_N)) = 0.26173631001735664
median            = 0.30723536116528977
max |Im(q_N)|/(1-Re(q_N)) = 0.012048801060316614.        (DSG-11)
```

Representative rows:

```text
sigma=1.0, N=10->12:
  q_N = 0.4942228848 + 0.0009740449 i
  1-Re(q_N) = 0.5057771152
  |Im(q_N)|/(1-Re(q_N)) = 0.0019258381

sigma=3.0, N=12->14:
  q_N = 0.6180742111 - 0.0046017479 i
  1-Re(q_N) = 0.3819257889
  |Im(q_N)|/(1-Re(q_N)) = 0.0120488011.                 (DSG-12)
```

So on the audited zeta ladder the denominator shell quotient is not merely in
the right half-plane; it stays quantitatively below `1` in real part, and the
horizontal skew against that subunit gap is tiny.

### Planted build

The planted build fails already at the subunit-gap level on the early steps:

```text
sigma=1.0, N=10->12:
  q_N = 7.4534770235 + 2.2988076646 i
  1-Re(q_N) = -6.4534770235

sigma=3.0, N=10->12:
  q_N = 7.2386795739 + 2.2817795781 i
  1-Re(q_N) = -6.2386795739.                             (DSG-13)
```

Even when the plant re-enters the subunit region later, the skew remains much
larger than on zeta:

```text
sigma=3.0, N=12->14:
  |Im(q_N)|/(1-Re(q_N)) = 0.5410163741.                 (DSG-14)
```

## 5. Consequence

This yields the honest denominator endpoint after E78.44:

```text
DEN-SUBUNIT-HORIZONTALITY:
  prove cofinally that Re(q_N) <= 1-c_* < 1
  and |Im(q_N)| is small on the safe ladder.             (DSG-15)
```

Then `(DSG-7)` gives denominator direction control and feeds back into the
E78.37-E78.44 chain.

## 6. Honest reading

This is partly a reduction and partly an autopsy.

Reduction:
the new centered picture really does isolate one additional scalar barrier,
namely the positive gap `1-Re(q_N)`.

Autopsy:
apart from that barrier, E78.44 does not move the imaginary content beyond
E78.40; it repackages the same `Im(q_N)` in centered coordinates.

That is useful because it tells us exactly what the next proof burden is and
prevents a fake spiral of equivalent quotient normalizations.

## 7. Status

```text
proved:
  the centered real floor from E78.44 is exactly the subunit real gap
  1-Re(q_N);

proved:
  under Re(q_N)<1, denominator directional defect is bounded by
  |Im(q_N)|/(1-Re(q_N));

observed:
  zeta keeps a healthy audited subunit gap, with minimum about 0.2617;

observed:
  the planted build fails the subunit barrier at the early breaking steps and
  remains much more skewed afterwards;

reduced:
  DEN-CENTERED-QUOTIENT-HORIZONTALITY to DEN-SUBUNIT-HORIZONTALITY;

next:
  either derive a finite shell law forcing the subunit gap and small imaginary
  part for q_N, or autopsy one of those two scalar conditions into a smaller
  exact update residual.
```
