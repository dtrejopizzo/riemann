# E78.123 - On the safe axis, `MODE2-OVERLAP` reduces to a real scalar amplitude

**Scope:** front B only, live object `MODE2-OVERLAP(z)`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** on the audited
safe axis `z=it`, the overlap `<v_2,r_z>` is purely imaginary to roundoff, so
the remaining live object is a single real scalar amplitude rather than a
complex-valued overlap.

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
P76.061: respected. The reduction stays on the paired safe axis already in use.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.121 reduced the live object to the interior overlap

```text
MODE2-OVERLAP(z) := <v_2,r_z>.                              (I-1)
```

The safe family used throughout this branch is the imaginary axis

```text
z = it,   t in {0.6, 1.0, 2.0}.                            (I-2)
```

So the next candid question is whether `(I-1)` still requires a full complex
value there, or whether symmetry collapses it further.

## 2. Symmetry observation

On the audited sections, the mode `v_2` is even to roundoff:

```text
max_j |v_2(j) - v_2(-j)| =
  2.08e-34, 4.75e-24   on zeta for N=8,12,
  1.39e-35, 2.37e-26   on plant for N=8,12.                (I-3)
```

By contrast the antisymmetry defect is order one, so this is a genuine parity
statement, not a near-zero vector artifact.

For an even vector and the symmetric mesh `d_{-j}=-d_j`, the Cauchy sum on the
imaginary axis pairs conjugate denominators and therefore should be purely
imaginary.

## 3. Probe

The audited overlaps give:

```text
BUILD zeta
N=8:
  <v_2,r_{0.6i}> = -4.99e-35 + 0.62080046 i
  <v_2,r_{1.0i}> = -3.82e-35 + 0.32253095 i
  <v_2,r_{2.0i}> = -1.46e-35 + 0.094719506 i

N=12:
  <v_2,r_{0.6i}> =  9.49e-25 - 0.56701099 i
  <v_2,r_{1.0i}> =  7.20e-25 - 0.28445242 i
  <v_2,r_{2.0i}> =  2.64e-25 - 0.074562503 i.              (I-4)

BUILD plant
N=8:
  real parts 1e-36, imaginary parts 0.83660348, 0.38614606, 0.075194439

N=12:
  real parts 1e-27, imaginary parts 0.79245353, 0.36316877, 0.068414606.   (I-5)
```

So on the audited safe axis the real part is annihilated to roundoff, and the
full overlap is already carried by its imaginary part.

## 4. Why this is a genuine reduction

The predecessor `MODE2-OVERLAP(z)` is complex-valued.

On the safe axis `(I-2)`, the present step reduces it to the real scalar
amplitude

```text
MODE2-SAFE-AMPLITUDE(t) := Im <v_2,r_{it}>.                (I-6)
```

That is strictly less information than carrying the full complex overlap.

So this is a genuine reduction on the safe family:

```text
MODE2-SAFE-AMPLITUDE
=> MODE2-OVERLAP(z)   for z=it on the safe axis.           (I-7)
```

## 5. Consequence

The remaining live object on this branch is now the real scalar function

```text
MODE2-SAFE-AMPLITUDE(t).                                   (I-8)
```

This is the sharpest safe-axis endpoint reached so far.

The next admissible question is whether `Im <v_2,r_{it}>` can be identified in
the finite coupled-generator package, or whether that bridge fails for a named
reason.

## 6. Status

```text
candidate closure - pending review

proved:
  on the audited safe axis, v_2 is even to roundoff and <v_2,r_{it}> is purely
  imaginary to roundoff;

reduced:
  MODE2-OVERLAP(z) on the safe axis to the real scalar
  MODE2-SAFE-AMPLITUDE(t);

next:
  identify MODE2-SAFE-AMPLITUDE(t) inside the finite coupled-generator package,
  or autopsy the exact reason that identification fails.
```
