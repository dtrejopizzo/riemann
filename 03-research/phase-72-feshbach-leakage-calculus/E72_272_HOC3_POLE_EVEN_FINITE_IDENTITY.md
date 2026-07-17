# E72.272 -- HOC3 pole-even finite identity

**Purpose.** State the corrected HOC3/K1 mechanism as a finite algebraic certificate rather than a
spectral diagnostic.

In the corrected pole-even geometry, let `A=A_1` be the Hermitian high-block plus-current and let:

```text
P = span{even Fourier modes 0,1},
R = P^perp.
```

Write:

```text
A = [[B,C],
     [C^*,D]]
```

relative to `P + R`.

## Exact identity

The cubic trace decomposes exactly as:

```text
Tr(A^3)
= Tr(B^3)+Tr(D^3)+3Tr(BCC^*)+3Tr(DC^*C).
```

Since `B` is `2x2`, if

```text
t = Tr(B),        s = Tr(B^2),
```

then:

```text
Tr(B^3) = (3ts-t^3)/2.
```

Therefore:

```text
Tr(A^3)
= (3ts-t^3)/2 + 3Tr(BCC^*) + Tr(D^3)+3Tr(DC^*C).
```

## Finite sufficient certificate

Define:

```text
LOW := -[(3ts-t^3)/2 + 3Tr(BCC^*)],
TAIL_full := ||D||_op (Tr(D^2)+3||C||_HS^2).
```

Then:

```text
LOW >= TAIL_full        =>        Tr(A^3) <= 0.
```

Indeed,

```text
Tr(D^3)+3Tr(DC^*C)
<= ||D||_op Tr(D^2)+3||D||_op ||C||_HS^2
= TAIL_full.
```

Thus `LOW >= TAIL_full` forces the total cubic trace non-positive.

## K1 sign

The low trace is:

```text
t = Tr(B).
```

In the corrected pole-even tests, `t<0`. This is the same `K1` sign mechanism as before, but now with
`P` equal to the literal first two even Fourier modes.

## Corrected numerical status

E72.269 reports:

```text
lambda=16: LOW=1.856039e-02, TAIL_full=6.268496e-03, margin=1.229189e-02, t=-2.438979e-01
lambda=20: LOW=1.777702e-02, TAIL_full=5.471611e-03, margin=1.230541e-02, t=-2.408511e-01
lambda=24: LOW=1.722240e-02, TAIL_full=4.450967e-03, margin=1.277143e-02, t=-2.408753e-01
```

## Proof-facing target

The corrected HOC3/K1 theorem is now:

```text
HOC3-pole-even:
t<0
and
LOW >= TAIL_full
```

for the corrected pole-even high block.

This is a finite statement in traces, Hilbert-Schmidt norms, and one operator norm of the explicit
compressed matrices `B,C,D`.

## Status

The algebraic identity is proved. The remaining theorem is the uniform inequality
`LOW >= TAIL_full` plus `t<0` in the stable pole-even regime, preferably via the `K1` average and
Schatten tail bounds.
