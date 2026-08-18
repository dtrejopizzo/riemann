# E78.121 - `MODE2-CAUCHY-AMPLITUDE(z)` reduces to the Cauchy overlap with `v_2`

**Scope:** front B only, live object `MODE2-CAUCHY-AMPLITUDE(z)`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the mode-2 Cauchy
amplitude is not an opaque resolvent quantity. It is exactly the Cauchy overlap
`<v_2,r_z>` divided by the eigenvalue `nu_2`.

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
P76.061: respected. The reduction remains at the paired/modal level before any
         further estimate.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.120 reduced the live object to

```text
MODE2-CAUCHY-AMPLITUDE(z)
  := |gamma_2(z)| / ||g_z||,                                (O-1)
```

where

```text
g_z = (I-P0)A^-1 r_z
    = sum_{j>=1} gamma_j(z) v_j.                            (O-2)
```

The next candid question is whether `gamma_2(z)` itself can be written without
carrying the full resolvent vector `g_z`.

## 2. Exact identity

Because `v_2` is orthogonal to `v_0`,

```text
gamma_2(z)
 = <v_2,g_z>
 = <v_2, A^-1 r_z>
 = <A^-1 v_2, r_z>.                                         (O-3)
```

Since `A v_2 = nu_2 v_2`,

```text
A^-1 v_2 = nu_2^(-1) v_2,                                   (O-4)
```

and therefore

```text
gamma_2(z) = <v_2,r_z> / nu_2.                              (O-5)
```

So the predecessor `(O-1)` reduces to the normalized overlap package

```text
MODE2-OVERLAP(z):
  |<v_2,r_z>| / (|nu_2| ||g_z||).                           (O-6)
```

This is strictly less information than carrying `gamma_2(z)` as a modal
coordinate of the full resolvent vector.

## 3. Probe

Companion files:

```text
E78_121_mode2_overlap_probe.py
E78_121_mode2_overlap_results.json
```

The audited safe sweep gives:

```text
BUILD zeta
N=8,12 and z in {i0.6,i1.0,i2.0}:
  relative identity error = 3e-30 to 5e-19.                (O-7)

BUILD plant
N=8,12 and z in {i0.6,i1.0,i2.0}:
  relative identity error = 2e-32 to 1e-23.                (O-8)
```

So `(O-5)` is exact to roundoff on both builds.

## 4. Why this is a genuine reduction

The predecessor `MODE2-CAUCHY-AMPLITUDE(z)` still referred to the modal
coefficient extracted from the resolvent vector `g_z`.

After `(O-5)`, the object is seen directly as an overlap of the raw safe Cauchy
row with the single eigenvector `v_2`.

That removes the need to carry the whole vector `g_z` in the live object.

So this is a genuine reduction:

```text
MODE2-OVERLAP(z)
=> MODE2-CAUCHY-AMPLITUDE(z).                               (O-9)
```

## 5. Consequence

The remaining arithmetic content of this branch is now concentrated in the
single overlap

```text
<v_2,r_z>.                                                  (O-10)
```

up to the already explicit eigenvalue factor `nu_2`.

This is the sharpest finite spectral object reached so far on the front-B safe
pairing branch.

The next admissible question is whether `<v_2,r_z>` can be identified in the
finite coupled-generator package, or whether that bridge fails for a named
reason.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact identity gamma_2(z)=<v_2,r_z>/nu_2;

reduced:
  MODE2-CAUCHY-AMPLITUDE(z) to the overlap package
  MODE2-OVERLAP(z);

next:
  identify <v_2,r_z> inside the coupled-generator package, or autopsy the exact
  reason that identification cannot hold.
```
