# E72.203 - Character torus audit

## Purpose

E72.202 formulates the fixed certificate in the operator-valued group algebra of the multiplicative
lattice. A natural possible proof is to evaluate the group algebra on unitary characters

```text
chi_t(n)=exp(i t log n)
```

and prove a uniform torus norm bound. If this worked with the same constants, `NTC-8` would follow
from a stronger C*-type estimate.

## Diagnostic

Script:

```text
E72_203_character_torus_probe.py
```

It scans

```text
A_j(t)=sum_{n in S_j} exp(it log n)A_n^+ + exp(-it log n)A_n^-
```

for `t in [0,40]`. The point `t=0` is the augmentation, i.e. the actual block `K_j`.

Output:

```text
E72.203 character torus norm probe
scans chi_t(n)=exp(i t log n); t=0 is augmentation
lam block op_t0 maxOp t_at_max minEig maxEig passNTCbound
 12     0  0.439  0.528  25.700  -0.528  +0.348 YES
 12     1  0.445  0.620   2.700  -0.620  +0.284 NO
 16     0  0.399  0.449  34.200  -0.449  +0.313 YES
 16     1  0.437  0.597   3.600  -0.597  +0.405 YES
 20     0  0.356  0.407  29.000  -0.407  +0.266 YES
 20     1  0.449  0.563   6.000  -0.472  +0.563 YES
 24     0  0.349  0.379  21.000  -0.379  +0.276 YES
 24     1  0.508  0.582   2.100  -0.582  +0.313 YES
```

## Reading

The uniform torus norm route fails with the fixed `NTC-8` constants: at `lambda=12`, block `K1`,

```text
sup_t ||A_1(t)|| ~= 0.620 > 0.60,
```

even though the augmentation satisfies

```text
||A_1(0)|| ~= 0.445.
```

Thus the actual certificate is not a simple consequence of a stronger all-character C*-norm bound.
The augmentation point has extra cancellation that is destroyed by twisting the prime-power phases.

## Consequence

The group-algebra formulation survives, but the proof must be augmentation-sensitive:

```text
prove the fixed trace inequalities at chi=1,
not uniformly on the whole character torus with the same constants.
```

This matters because a torus-sup proof would be too coarse in exactly the same way as an absolute
signed-word ceiling, though less brutally.

## Status

Rejected as a direct proof route:

```text
uniform character-torus norm bound with constants 0.90, 0.60.
```

Kept:

```text
operator-valued group algebra at the augmentation character.
```
