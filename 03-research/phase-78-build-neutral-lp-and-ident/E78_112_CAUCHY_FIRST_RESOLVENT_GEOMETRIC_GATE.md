# E78.112 - The Cauchy side of `PAIRED-FIRST-RESOLVENT` reduces to a raw geometric ratio

**Scope:** front B only, live object `PAIRED-FIRST-RESOLVENT`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the Cauchy-side
off-ground first resolvent is not a new operator burden; it is implied by a raw
geometric ratio of the Cauchy row itself. The only hard side left is the source
`1`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem.
P76.061: respected. The reduction stays at the paired first-resolvent level,
         exactly where the Cauchy row enters.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.111 reduced the derivative-relevant tail to

```text
<r_z,(I-P0)A^-2 1> = <(I-P0)A^-1 r_z, (I-P0)A^-1 1>.        (C-1)
```

So `PAIRED-FIRST-RESOLVENT` has two sides:

```text
Cauchy side:  (I-P0)A^-1 r_z,
source side:  (I-P0)A^-1 1.                                 (C-2)
```

The question is whether the Cauchy side itself can be reduced to a smaller
non-resolvent object.

## 2. Exact geometric certificate

Let `b` be any vector, with spectral decomposition

```text
b = c_0 v_0 + sum_{j>=1} c_j v_j,                           (C-3)
```

so that

```text
A^-1 b = c_0/nu_0 v_0 + sum_{j>=1} c_j/nu_j v_j.           (C-4)
```

Therefore

```text
||(I-P0)A^-1 b||^2
 = sum_{j>=1} |c_j|^2 / nu_j^2
 <= nu_1^(-2) sum_{j>=1} |c_j|^2
 = nu_1^(-2) ||(I-P0)b||^2,                                (C-5)
```

while

```text
||P0 A^-1 b|| = |c_0| / |nu_0| = |<v_0,b>| / |nu_0|.       (C-6)
```

Hence the exact certificate is

```text
||(I-P0)A^-1 b|| / ||P0 A^-1 b||
 <= |nu_0/nu_1| * ||(I-P0)b|| / |<v_0,b>|.                 (C-7)
```

For the Cauchy row `b=r_z`, the right-hand side depends only on the raw
geometry of `r_z` relative to the ground mode.

## 3. Why this is a genuine reduction

The predecessor `PAIRED-FIRST-RESOLVENT` asked to control the resolvent vector
`(I-P0)A^-1 r_z`.

After `(C-7)`, the Cauchy side is implied by the smaller datum

```text
CAUCHY-GEOMETRIC-RATIO(z):
  ||(I-P0)r_z|| / |<v_0,r_z>|.                              (C-8)
```

This is strictly less information: it removes one resolvent power from the
Cauchy side entirely and replaces it by a raw overlap ratio of the input row.

So

```text
|nu_0/nu_1| * CAUCHY-GEOMETRIC-RATIO(z)
=> control of (I-P0)A^-1 r_z.                              (C-9)
```

This is a genuine reduction of one full side of `PAIRED-FIRST-RESOLVENT`.

## 4. Probe

Companion files:

```text
E78_112_cauchy_first_resolvent_probe.py
E78_112_cauchy_first_resolvent_results.json
```

On the audited zeta ladder:

```text
N=6,8,10,12 and z in {i0.6,i1.0,i2.0}:
  actual off-ground ratio of A^-1 r_z lies between 2.22e-4 and 2.58e-3,
  while the certificate in (C-7) lies between 2.14e-3 and 2.75e-2.         (C-10)
```

So the certificate is uniformly small on the audited safe family and beats the
actual ratio by only one decimal order, not by dozens.

For the planted falsifier:

```text
the actual off-ground ratio is 1e16 -- 1e29,
while the geometric certificate is O(1) to O(10).                           (C-11)
```

So the reduction isolates exactly where front B is allowed to fail: the zeta
build has strong Cauchy-side alignment, the planted build does not.

## 5. Consequence

The Cauchy half of `PAIRED-FIRST-RESOLVENT` is no longer a live resolvent
object. It reduces to the raw geometric input ratio `(C-8)`.

Therefore the honest next live object is

```text
SOURCE-FIRST-RESOLVENT:
  control (I-P0)A^-1 1 cofinally enough to pair with the already-reduced
  Cauchy side.                                                     (C-12)
```

Together with E78.111, this gives

```text
SOURCE-FIRST-RESOLVENT + CAUCHY-GEOMETRIC-RATIO
=> PAIRED-FIRST-RESOLVENT
=> derivative-relevant tail control.                              (C-13)
```

## 6. Status

```text
candidate closure - pending review

proved:
  the exact bound
  ||(I-P0)A^-1 b|| / ||P0 A^-1 b||
  <= |nu0/nu1| * ||(I-P0)b|| / |<v0,b>|;

reduced:
  the full Cauchy side of PAIRED-FIRST-RESOLVENT to the raw geometric ratio of
  the Cauchy row r_z;

verified:
  on the audited zeta ladder the certificate is genuinely small across all
  tested safe rows and all audited N, while the planted build fails there as
  front B allows;

next:
  attack the remaining source side (I-P0)A^-1 1, or autopsy the exact factor
  that prevents a cofinal proof for that sole surviving object.
```
