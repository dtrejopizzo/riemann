# E73.016 - Finite local action certificate

## 1. Correction to E73.015

E73.015 proposed a strict triangular rule:

```text
r -> r,r+1.
```

E73.016 falsifies this as an exact finite rule.  The lower rational block, especially
`r=0`, still has a visible component outside source orders `0,1`.

The surviving statement is finite-width rather than triangular:

```text
r -> 0,1,2,3 plus endpoint terms.
```

This is the correct analytic target.

## 2. Local spaces

For critical nodes `gamma in K_L` and off-line test nodes `beta in O_L`, define

```text
DD_gamma(d)=DD_L(-gamma,d).
```

The primitive class is

```text
P_{O,K}
= span{ DD_gamma(d)/(d^2+beta^2)^r : r=0,1,2 }
  + span{ d^2 DD_gamma(d) }.
```

The finite source class is

```text
S_{O,K}^{fin}
= span{ DD_gamma(d)/(d^2+beta^2)^r : r=0,1,2,3 }
  + span{ d^2 DD_gamma(d), d^4 DD_gamma(d) }.
```

## 3. Certificate statement

The finite local action certificate is:

```text
LOCAL-FIN:
(C_E-mu I)P_{O,K} subset S_{O,K}^{fin} + R_{72},
```

where `R_72` belongs to the already isolated Phase 72 residual classes:

```text
parity-cancelled finite Fourier tail,
zero-node absorbed tail,
outside-natural-height second-variation tail.
```

Equivalently, for each primitive generator `Y` there are coefficients `a_j`, `b_1`,
`b_2` such that

```text
(C_E-mu I)Y(d)
= sum_{gamma,beta,j<=3} a_{gamma,beta,j}
   DD_gamma(d)/(d^2+beta^2)^j
 + sum_gamma b_{gamma,1} d^2 DD_gamma(d)
 + sum_gamma b_{gamma,2} d^4 DD_gamma(d)
 + R_72(d).
```

## 4. Why this is progress

The dangerous alternative was an infinite local pole tower:

```text
r=0,1,2,... without a uniform cutoff.
```

That would merely rename NAT-PROJ.  E73.016 instead identifies a finite action envelope.
The proof now has a precise finite algebraic form: derive the six source families above
from the coupled `W02-WR-Prime` operator and bound the remaining `R_72` by the already
closed tail estimates.

## 5. Load-bearing chain

The current chain is:

```text
LOCAL-FIN
 + NAT-SRC residual pairing bound
=> NAT-PROJ
=> off-line Schur suppression
=> scalar WRL
=> Omega_7.
```

Thus the next analytic lemma is not strict triangularity.  It is the finite-width action
identity `LOCAL-FIN`.
