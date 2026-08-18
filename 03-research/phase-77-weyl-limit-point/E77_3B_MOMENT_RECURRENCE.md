# E77.3b - Moment recurrence and ratio reduction

**Run:** 2026-07-18.

## 1. Statement

Let

```text
A = H_inner - mu I,        A x = b,
D = diagonal mesh,         s = sine displacement symbol.
```

RDP-2 implies the exact finite recurrence

```text
A D^k x =
D^k b
+ (2/L) sum_{r=0}^{k-1} D^r
  (s <1,D^{k-1-r}x> - 1 <s,D^{k-1-r}x>).      (MR-1)
```

E77.3b tests whether this recurrence itself closes `GEN-ORTH-DIV`, or
whether it only names the next smaller obstruction.

## 2. Probe

Probe:

```text
E77_3b_moment_recurrence_probe.py
```

Command:

```bash
python3 E77_3b_moment_recurrence_probe.py \
  --lambdas 6,7,8 \
  --modes 12,16,18 \
  --kmax 6 \
  --dps 60
```

Output:

```text
E77_3b_moment_recurrence_results.json
```

The planted falsifier is the required `gamma=14.134725141734693790`,
`beta=0.30`, `strength=5.0`.  The planted run uses its own planted sine
symbol, so the identity is tested fairly.

## 3. Certification Table

`g/b` means `||generator package||/||boundary package||` in `(MR-1)`.

| case | S_N | max rel. residual | g/b k=2 | g/b k=4 | g/b k=6 | cancel k=6 |
|---|---:|---:|---:|---:|---:|---:|
| zeta L6 N12 | 1.682e21 | 1.06e-50 | 1.71 | 3.02 | 4.59 | 0.907 |
| plant L6 N12 | 2.799e2 | 2.75e-60 | 43.5 | 66.7 | 89.0 | 0.988 |
| zeta L6 N16 | 5.128e23 | 3.98e-50 | 0.396 | 0.676 | 0.995 | 0.936 |
| plant L6 N16 | 2.203e2 | 3.95e-60 | 14.9 | 10.7 | 8.48 | 0.865 |
| zeta L6 N18 | 9.213e27 | 2.01e-48 | 0.172 | 0.337 | 0.509 | 0.967 |
| plant L6 N18 | 2.721e2 | 2.29e-60 | 5.47 | 3.37 | 2.38 | 0.865 |
| zeta L7 N12 | 9.856e16 | 3.33e-53 | 0.791 | 1.89 | 3.42 | 0.962 |
| plant L7 N12 | 2.966e1 | 2.24e-60 | 6.05 | 8.10 | 8.34 | 0.937 |
| zeta L7 N16 | 1.081e24 | 2.03e-50 | 0.221 | 0.412 | 0.619 | 0.962 |
| plant L7 N16 | 2.750e2 | 3.13e-60 | 8.31 | 5.63 | 4.96 | 0.944 |
| zeta L7 N18 | 8.546e26 | 1.56e-48 | 0.385 | 0.727 | 1.12 | 0.947 |
| plant L7 N18 | 2.217e2 | 9.53e-60 | 17.0 | 10.6 | 8.92 | 0.878 |
| zeta L8 N12 | 2.549e16 | 2.19e-53 | 0.642 | 1.54 | 2.75 | 0.963 |
| plant L8 N12 | 3.133e1 | 8.35e-60 | 4.70 | 10.4 | 16.2 | 0.894 |
| zeta L8 N16 | 6.830e23 | 4.88e-50 | 0.510 | 0.875 | 1.25 | 0.904 |
| plant L8 N16 | 8.125e3 | 1.95e-59 | 126 | 145 | 117 | 0.994 |
| zeta L8 N18 | 1.800e26 | 7.34e-49 | 0.247 | 0.452 | 0.670 | 0.952 |
| plant L8 N18 | 2.565e2 | 1.15e-59 | 21.9 | 19.1 | 13.7 | 0.906 |

## 4. Proof Component

The recurrence `(MR-1)` is exact.  The probe verifies it with relative
residuals between `1e-48` and `1e-60` on all measured zeta and planted
cases.

Algebraically, this follows from

```text
A D - D A = (2/L)(s 1^T - 1 s^T),
```

and the commutator expansion

```text
A D^k - D^k A
= sum_{r=0}^{k-1} D^r (A D-D A) D^{k-1-r}.
```

Applying this to `Ax=b` gives `(MR-1)`.

## 5. Autopsy of the Naive Recurrence Closure

The identity itself is not the closure mechanism.  It is exact for the
planted falsifier as well.  Therefore:

```text
MR-1 alone is falsifier-neutral;
MR-1 alone cannot be the arithmetic discriminator;
GEN-ORTH-DIV does not follow merely from writing the recurrence.
```

This is not a stall.  The recurrence exposes the smaller object: the
relative size of the generator package compared with the boundary package.
For zeta, `g/b` at N=18 is already below or near one in all lambdas:

```text
L6: k=2 0.172, k=4 0.337, k=6 0.509
L7: k=2 0.385, k=4 0.727, k=6 1.12
L8: k=2 0.247, k=4 0.452, k=6 0.670
```

For the planted falsifier, `g/b` remains much larger:

```text
L6: k=2 5.47,  k=4 3.37,  k=6 2.38
L7: k=2 17.0,  k=4 10.6,  k=6 8.92
L8: k=2 21.9,  k=4 19.1,  k=6 13.7
```

This matches E77.3: zeta generator escape decays, while planted generator
mass remains visible.

## 6. Reduced Target

E77.3b reduces `GEN-ORTH-DIV` to a sharper finite inequality:

```text
MOM-RATIO:
For fixed k and safe lambda-growth regime, the zeta canonical response
satisfies

    ||G_k(x_N)|| <= C_k ||D^k b_N||

with a block/parity envelope strong enough to force escape_k(N)->0 and
S_N lower-envelope divergence.

FALSIFIER:
The planted off-line build violates the same estimate by a persistent
factor in the generator package.
```

Here `G_k(x_N)` is the generator package in `(MR-1)`.  This is strictly
smaller than LP and more concrete than IDENT: it is a finite comparison of
two named packages in the exact RDP-2 recurrence.

## 7. Next Step

Open E77.3c / E77.5 interface:

```text
derive MOM-RATIO from the safe Gamma-prime/cell formula, using only
absolute convergence in Re(s)>1, or autopsy that arithmetic insertion
and move to IDENT directly.
```

If MOM-RATIO can be proved, it supplies the quantitative LP envelope
needed by E77.1b and E77.3.  If it cannot, the difficulty has moved cleanly
into the IDENT arithmetic insertion.

## 8. Status

```text
proved:    exact finite recurrence MR-1;
proved:    MR-1 is falsifier-neutral and cannot close GEN-ORTH-DIV alone;
observed:  zeta g/b at N=18 is O(1) or smaller for k=2,4,6;
observed:  planted g/b at N=18 remains several-to-tens larger;
open:      MOM-RATIO theorem and its safe arithmetic source;
next:      E77.3c/E77.5 interface: Gamma-prime derivation of MOM-RATIO or
           autopsy into IDENT.
```
