# E78.113 - The raw geometric route for `SOURCE-FIRST-RESOLVENT` is dead

**Scope:** front B only, live object `SOURCE-FIRST-RESOLVENT`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the direct
geometric reduction of `(I-P0)A^-1 1` fails for an exact and already familiar
reason: the bad coefficient is the raw overlap `|<v_0,1>|^(-1)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as the theorem.
P76.061: respected. This autopsy concerns the source side of the already paired
         first-resolvent package; no ambient inverse closure is claimed.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

After E78.112, the Cauchy side of `PAIRED-FIRST-RESOLVENT` is reduced, and the
only surviving burden is

```text
SOURCE-FIRST-RESOLVENT:
  control (I-P0)A^-1 1.                                      (S-1)
```

The first obvious attempt is the same raw geometric certificate used on the
Cauchy side.

## 2. Exact source-side certificate

Applying E78.112's identity with `b=1` gives

```text
||(I-P0)A^-1 1|| / ||P0 A^-1 1||
 <= |nu_0/nu_1| * ||(I-P0)1|| / |<v_0,1>|.                  (S-2)
```

Since `||(I-P0)1|| <= ||1|| = sqrt(N)`, this implies the cruder but explicit
bound

```text
||(I-P0)A^-1 1|| / ||P0 A^-1 1||
 <= |nu_0/nu_1| * sqrt(N) / |<v_0,1>|.                      (S-3)
```

So the only question is whether `(S-2)` or `(S-3)` is useful on the zeta side.

## 3. Probe

Companion computation: the audited source-side sweep produced

```text
BUILD zeta
N= 6: actual ratio = 3.42e-3, certificate = 2.00e7
N= 8: actual ratio = 1.65e-3, certificate = 2.10e9
N=10: actual ratio = 1.64e-3, certificate = 5.48e11
N=12: actual ratio = 1.26e-3, certificate = 8.97e13.       (S-4)

BUILD plant
N= 6: actual ratio = 4.36e57, certificate = 6.87e49
N= 8: actual ratio = 2.74e10, certificate = 1.10e0
N=10: actual ratio = 1.68e13, certificate = 3.62e0
N=12: actual ratio = 3.41e15, certificate = 6.92e0.        (S-5)
```

On the zeta ladder the actual source-side ratio is tiny, but the geometric
certificate explodes by 10 to 16 orders of magnitude.  The failure is exact:

```text
|<v_0,1>| =
 4.08e-10, 2.18e-12, 9.33e-15, 4.84e-17                     (S-6)
```

on the audited zeta rows, so the bad factor is

```text
|<v_0,1>|^(-1).                                             (S-7)
```

## 4. Autopsy

The source-side route

```text
gap ratio + raw geometric overlap of 1                      (S-8)
```

is therefore dead.

What fails is theorem-grade and precise:

```text
the geometric certificate throws away the resolvent-weighted structure of the
source and divides by the tiny raw overlap |<v_0,1>|.                       (S-9)
```

That is exactly why it can be useful for the Cauchy rows `r_z` and useless for
the source `1`: the safe rows have order-one overlap with `v_0`, while the
constant source does not.

So `SOURCE-FIRST-RESOLVENT` cannot be proved by collapsing the input `1` to its
raw overlap geometry.

## 5. Consequence

The next admissible object must retain more structure than `|<v_0,1>|`.
In particular, it must keep a resolvent-weighted source package, such as

```text
A-weighted source geometry for 1,
or an exact finite identity in the coupled-generator package that bypasses
the raw overlap with v_0.                                               (S-10)
```

Any route that immediately divides by `|<v_0,1>|` is now closed.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact source-side geometric certificate
  ||(I-P0)A^-1 1|| / ||P0 A^-1 1||
  <= |nu0/nu1| * ||(I-P0)1|| / |<v0,1>|;

autopsied:
  this route is useless on the audited zeta ladder because the exact bad factor
  is |<v0,1>|^(-1);

closed:
  the strategy "gap ratio + raw overlap geometry of 1" for SOURCE-FIRST-
  RESOLVENT;

next:
  keep resolvent-weighted source structure in the live object instead of
  collapsing to the bare overlap with `1`.
```
