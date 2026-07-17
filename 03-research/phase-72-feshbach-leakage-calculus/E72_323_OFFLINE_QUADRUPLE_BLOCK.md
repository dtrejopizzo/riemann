# E72.323 -- Off-line quadruple block in the zero-node system

**Purpose.** Analyze the leading block of the zero-node system E72.322 for one off-line quadruple.
The correct forcing is not scalar diagonal dominance; it is a `2 x 2` block on the pair
`{a, conjugate(a)}` after the `+-` symmetry has already been quotiented out.

## 1. Setup

Let

```text
a=alpha+i gamma,        b=conjugate(a)=alpha-i gamma,
alpha>0,                gamma != 0.
```

The shifted zero quadruple is

```text
{a,-a,b,-b}.
```

After E72.321, representatives are `{a,b}`.

Write

```text
E_a=e^(aL),        E_b=e^(bL).
```

The zero-node system from E72.322 is

```text
D_aG(a)-K_abG(b)=Err_a,
D_bG(b)-K_baG(a)=Err_b.
```

## 2. Leading coefficients

The diagonal coefficient is

```text
D_a=mu+e_pole-2kappa_L-L-sinh(aL)/a.
```

For `alpha>0`, the exponential part is

```text
D_a^lead=-E_a/(2a),
D_b^lead=-E_b/(2b).
```

The off-diagonal coefficient from E72.322 is

```text
K_ab
= [ b(1+E_a)(1-E_b^(-1))
     + a(1-E_a)(1+E_b^(-1)) ]/(b^2-a^2).
```

Its leading part is

```text
K_ab^lead=E_a/(a+b),
K_ba^lead=E_b/(a+b).
```

Thus the leading block is

```text
[ E_a  0  ] [ -1/(2a)   -1/(a+b) ] [G(a)]
[ 0    E_b] [ -1/(a+b)  -1/(2b)  ] [G(b)].
```

## 3. Invertibility of the quadruple block

The reduced `2 x 2` matrix

```text
M(a,b)= [ -1/(2a)   -1/(a+b) ]
       [ -1/(a+b)  -1/(2b)  ]
```

has determinant

```text
det M(a,b)
= 1/(4ab)-1/(a+b)^2
= (a-b)^2/[4ab(a+b)^2].                              (1)
```

Since `gamma != 0`, `a != b`, so

```text
det M(a,b) != 0.
```

Therefore the off-line quadruple block is invertible at leading exponential scale.

## 4. Consequence

Suppose this quadruple is isolated among zeros with real part `alpha` in the fixed window, and all
couplings to zeros with smaller real part are `O(e^((alpha-delta)L))`. Suppose also

```text
Err_a, Err_b = O(L^B).
```

Then the system gives

```text
G(a),G(b)=O(e^(-alpha L)L^B),
```

after absorbing the lower-exponent couplings.

This is exactly the nodal suppression required by `PW-Cauchy` at the off-line zero nodes.

## 5. What remains for the global theorem

The scalar diagonal target `ZND` from E72.322 should be replaced by a block theorem:

```text
ZNB:
for each maximal-real-part off-line cluster in a fixed height window, the leading exponential
zero-node block is invertible, and all lower-real-part couplings are perturbative.
```

For a simple quadruple, E72.323 proves the leading invertibility.

The remaining cases are:

```text
1. multiple zeros with the same real part alpha;
2. real shifted zeros with gamma=0, if such a case is not excluded separately;
3. uniform control of the finite Fourier tail and the lower-real-part error.
```

## 6. Status

```text
proved: a single off-line quadruple gives an invertible leading 2 x 2 block;
reduced: nodal suppression for isolated maximal quadruples to polynomial error/tail control;
open:   prove cluster invertibility and global tail/error bounds.
```

This is the first analytic forcing mechanism in Phase 72 that is not a positivity statement and not a
finite numerical certificate.

E72.324 proves the simple-cluster version of the open cluster-invertibility item: the maximal-real-part
leading block is the Cauchy matrix `1/(a_j+a_k)`, hence invertible by the Cauchy determinant formula.
