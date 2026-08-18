# E77.7au - Alignment defect coordinate identity

**Run:** 2026-07-18.

## 1. Purpose

E77.7at reduced the live shell-side object to the explicit scalar

```text
ALIGNMENT-DEFECT
  = r_even . (sqrt(c), -sgn(b) sqrt(a)),
```

where `r_even` is the even residual in the 2x2 locked block

```text
S_even = [[a,b],[b,c]].
```

This note shows that the defect is not a new formal object.  It is exactly a
linear combination of the two shell residual amplitudes already present in the
original 4-node coordinates.

## 2. Exact coordinate identity

Write the shell residual on the symmetric 4-node shell as

```text
(-m,-n,n,m) residual = (r_out, r_in, r_in, r_out).
```

Then the even coordinates are exactly

```text
r_even = (sqrt(2) r_in, sqrt(2) r_out).                (AU-1)
```

This is not asymptotic; it is the orthonormal even-basis change used in
`E77_7aq_even_odd_shell_probe.py`.

Substituting `(AU-1)` into the E77.7at defect gives

```text
ALIGNMENT-DEFECT
 = sqrt(2) (r_in sqrt(c) - sgn(b) r_out sqrt(a)).      (AU-2)
```

So the live shell-side scalar is simply the signed mismatch between the inner
and outer residual amplitudes after weighting by the locked block scales
`sqrt(c)` and `sqrt(a)`.

Equivalently, the large-branch alignment law becomes the original-coordinate
ratio law

```text
r_out / r_in ~= sgn(b) sqrt(c/a),                      (AU-3)
```

with defect `(AU-2)`.

## 3. Probe check

Using

```text
E77_7aq_even_odd_shell_results.json
E77_7aq_even_odd_shell_plant_16_18.json
E77_7h_geometric_shell_residual_results.json
```

the computed original-coordinate combination

```text
r_out sqrt(a) - sgn(b) r_in sqrt(c)
```

tracks the even-basis defect up to the exact `sqrt(2)` normalization factor
and the inner/outer ordering convention:

### Zeta `16 -> 18`

```text
alignment defect (even basis)      = -2.85877e-42
original-coordinate combo          = -2.02145e-42
ratio defect/combo                 = 1.41421356...
```

### Zeta `18 -> 20`

```text
alignment defect (even basis)      = -6.14691e-45
original-coordinate combo          =  4.34652e-45
|defect|/|combo|                   = 1.41421356...
```

### Planted `16 -> 18`

```text
alignment defect (even basis)      =  2.35922e-1
original-coordinate combo          =  1.66822e-1
ratio defect/combo                 = 1.41421356...
```

So the exact shell-facing object can be written directly in the original
residual amplitudes without any spectral decomposition.

## 4. Consequence

This is another admissible reduction:

```text
ALIGNMENT-DEFECT
=> SMALL-MODE-ALIGNMENT-LAW
=> SMALL-MODE-SUPPRESSION
=> ... => BTG-DIV-L.
```

But now the defect is no longer stated in eigenvector language.  The smallest
currently visible shell-side object is the explicit weighted amplitude
mismatch

```text
WEIGHTED-INNER-OUTER-MISMATCH:
  r_in sqrt(c) - sgn(b) r_out sqrt(a).                 (AU-4)
```

This is strictly smaller and more useful because it lives entirely in the
already certified shell residual coordinates.

## 5. Status

```text
proved:
  the alignment defect is exactly a weighted linear combination of the two
  symmetric shell residual amplitudes;
  no new spectral formalism is needed to state the live shell-side object.

reduced:
  ALIGNMENT-DEFECT
  -> WEIGHTED-INNER-OUTER-MISMATCH.

live object:
  theorem-grade proof that the weighted inner/outer mismatch is higher order
  on the zeta shell ladder.
```
