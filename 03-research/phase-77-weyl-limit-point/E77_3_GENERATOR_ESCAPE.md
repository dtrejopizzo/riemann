# E77.3 - Generator escape probe

**Run:** 2026-07-18.

## 1. Statement

E77.2 showed that raw RDP-1 cannot prove LP: the rank-two commutator is
blind on the codimension-two sector orthogonal to `1` and `s`.  E77.3
therefore tests the next finite object:

```text
GEN-ESC:
for the canonical boundary response x_N, measure whether D^k x_N escapes
or enters the generator sector spanned by 1 and s.
```

The probe computes, for `k=0,...,4`,

```text
escape_k(N)
 = sqrt( |<1,D^k x_N>|^2/(||1||^2||D^k x_N||^2)
        +|<s,D^k x_N>|^2/(||s||^2||D^k x_N||^2) ).
```

This is not an ambient inverse norm.  It is a paired directional diagnostic
on the selected canonical response.

## 2. Probe

Probe:

```text
E77_3_generator_escape_probe.py
```

Command:

```bash
python3 E77_3_generator_escape_probe.py \
  --lambdas 6,7,8 \
  --max-modes 18 \
  --dps 60
```

Output:

```text
E77_3_generator_escape_results.json
```

Cases: zeta and planted `beta=0.30`, `strength=5.0`,
`gamma=14.134725141734693790`.

## 3. Endpoint table

| case | S_18 | escape_0 | escape_2 | escape_4 | c(S_N) | c(escape_4) |
|---|---:|---:|---:|---:|---:|---:|
| zeta L6 | 9.213e27 | 1.783e-15 | 1.368e-13 | 3.237e-12 | 3.853 | -1.738 |
| plant L6 | 2.721e2 | 9.028e-2 | 3.829e-1 | 6.097e-1 | 0.691 | 0.018 |
| zeta L7 | 8.546e26 | 7.834e-15 | 5.554e-13 | 1.205e-11 | 3.850 | -1.763 |
| plant L7 | 2.217e2 | 3.295e-1 | 4.200e-2 | 3.832e-1 | 0.473 | -0.118 |
| zeta L8 | 1.800e26 | 1.278e-14 | 8.531e-13 | 1.734e-11 | 3.863 | -1.792 |
| plant L8 | 2.565e2 | 1.186e-1 | 5.192e-3 | 1.184e-1 | 0.548 | -0.226 |

## 4. Reading

The zeta canonical response becomes almost generator-orthogonal under
low displacement powers.  By N=18, `escape_4` is `3e-12`, `1e-11`, and
`2e-11` for lambdas 6,7,8.

The planted response does not share that behavior.  It keeps visible
generator mass:

```text
lambda 6: escape_4 = 0.610
lambda 7: escape_4 = 0.383
lambda 8: escape_4 = 0.118
```

This is a real falsifier separation, unlike raw RDP-1.  It says the
arithmetic difference appears in how the canonical response aligns with
the two displacement generators after mesh powers are applied.

## 5. What This Does Not Prove

This does not prove LP.  In fact, by itself it does not even prove
`S_N -> infinity`: a vector may be generator-orthogonal and still have
bounded energy.  The theorem still needs a recurrence/asymptotic statement
linking generator orthogonalization, boundary forcing, and lower-envelope
growth.

It also must be audited against the zero-filter gate before it can become
an arithmetic theorem.  The current measurement uses only the declared
plant as falsifier, but a proof of generator orthogonalization for zeta
must come from the allowed safe arithmetic package, not from hidden divisor
information.

## 6. Reduced Target

E77.3 reduces the next theorem target to:

```text
GEN-ORTH-DIV:
For the zeta CCM mesh, repeated displacement propagation forces
escape_k(N) -> 0 for fixed k, and the same finite recurrence implies
positive block/parity lower-envelope growth of S_N.

FALSIFIER:
The planted build fails GEN-ORTH-DIV at some fixed low k, or fails the
IDENT step that should explain GEN-ORTH-DIV through the safe Gamma-prime
formula.
```

This is smaller than LP and smaller than full IDENT: it is a finite
two-generator asymptotic for the selected canonical response.

## 7. Next Step

E77.4 should not be a generic direct-growth attempt yet.  The sharper move
is E77.3b:

```text
derive and test the finite recurrence for the moment vector
    (<1,D^k x_N>, <s,D^k x_N>)_{k<=K}
from RDP-2, including boundary forcing terms;
then prove or autopsy whether GEN-ORTH-DIV follows from that recurrence.
```

## 8. Status

```text
proved:    no theorem-level LP statement;
observed:  zeta generator escape decays to ~1e-11 for k=4 at N=18;
observed:  planted generator escape remains visible at k=4;
refuted:   raw commutator as discriminator, but not generator escape;
open:      finite recurrence GEN-ORTH-DIV and its non-circular arithmetic
           source;
next:      E77.3b moment-recurrence derivation/probe.
```
