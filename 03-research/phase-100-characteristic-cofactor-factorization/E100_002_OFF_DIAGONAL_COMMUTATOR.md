# E100.002 - Off-diagonal projection commutator

## 1. Algebraic split

Put

```text
Pi=Pi_t,
Q=I-Pi.                                              (1.1)
```

For every operator `Z`,

```text
[Z,Pi]=QZPi-PiZQ.                                    (1.2)
```

### Proof

Insert `I=Pi+Q` on both sides of `ZPi-PiZ`.  The two diagonal terms
`Pi Z Pi` cancel, while `QPi=Pi Q=0`. `QED`

Using E100.001,

```text
[Z,G_t]=-QZPi+PiZQ.                                  (1.3)
```

Thus the characteristic commutator contains only the Euler coupling between
the selected line and its orthogonal complement.

## 2. No gap denominator

Equation (1.3) is algebraic.  It contains no reduced resolvent and no inverse
spectral gap.  Estimating it by reconstructing `Pi` from a Riesz integral is
unnecessary.

## 3. Status

```text
proved:
  exact off-diagonal factorization of the characteristic commutator.
```

