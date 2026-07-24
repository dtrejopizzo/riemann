# E78.124 - `MODE2-SAFE-AMPLITUDE` reduces to a half-axis real kernel transform

**Scope:** front B only, live object `MODE2-SAFE-AMPLITUDE(t)`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** on the safe axis,
the surviving mode-2 amplitude is not merely an imaginary Cauchy overlap. It is
exactly a real kernel transform over the positive half of the interior mesh.

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
P76.061: respected. The reduction stays inside the already-selected safe-axis
         pairing.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.123 reduced the live object to the real scalar amplitude

```text
MODE2-SAFE-AMPLITUDE(t) := Im <v_2,r_{it}>.                (H-1)
```

The next honest question is whether `(H-1)` still needs the full symmetric
interior sum, or whether the parity of `v_2` collapses it to the positive half
of the mesh.

## 2. Exact half-axis formula

Write the interior mesh as `d_{-n}=-d_n`, and let `v_2` be even. Then

```text
<v_2,r_{it}>
 = sum_n v_2(n)/(it-d_n).                                  (H-2)
```

Pairing `n` with `-n` and isolating the zero mode gives

```text
Im <v_2,r_{it}>
 = -v_2(0)/t - 2t sum_{n>0} v_2(n)/(t^2+d_n^2).           (H-3)
```

So the safe-axis amplitude is exactly the real half-axis kernel transform

```text
HALF-AXIS-MODE2(t)
 := -v_2(0)/t - 2t sum_{n>0} v_2(n)/(t^2+d_n^2).          (H-4)
```

This is strictly less information than the full complex overlap `(H-1)`:
it removes the negative half of the mesh and the redundant real part.

## 3. Probe

The audited check gives roundoff agreement:

```text
BUILD zeta
N=8,12 and t in {0.6,1.0,2.0}:
  relative error = 2e-35 to 6e-25.                         (H-5)

BUILD plant
N=8,12 and t in {0.6,1.0,2.0}:
  relative error = 2e-36 to 3e-27.                         (H-6)
```

So `(H-3)` is exact to numerical precision on the audited safe family.

## 4. Why this is a genuine reduction

The predecessor `MODE2-SAFE-AMPLITUDE(t)` still carried the full symmetric
Cauchy overlap.

After `(H-3)`, the live object becomes the real transform `(H-4)` over the
positive half-axis only. This removes half the coordinates and fixes the kernel
explicitly.

So this is a genuine reduction:

```text
HALF-AXIS-MODE2(t) => MODE2-SAFE-AMPLITUDE(t).             (H-7)
```

## 5. Consequence

The remaining live object on this branch is now the real half-axis transform

```text
HALF-AXIS-MODE2(t).                                        (H-8)
```

This is the sharpest explicit scalar endpoint reached so far on the safe-axis
route.

The next admissible question is whether the coefficients `v_2(n)` for `n>=0`
can be identified or constrained through the finite coupled-generator package,
or whether that bridge fails for a named reason.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact half-axis formula
  Im <v_2,r_{it}> = -v_2(0)/t - 2t sum_{n>0} v_2(n)/(t^2+d_n^2);

reduced:
  MODE2-SAFE-AMPLITUDE(t) to the real half-axis transform HALF-AXIS-MODE2(t);

next:
  attack the half-axis coefficients of v_2, or identify a finite coupled object
  that carries the same transform.
```
