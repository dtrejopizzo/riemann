# E72.355 - Node-blind CFIR closure is false

## 1. Purpose

E72.354 gives an exact finite Lambda-elimination certificate.  The numerical result shows that the
current partial residual fails this certificate on shifted control nodes.

This note records the analytic consequence: any CFIR closure which is blind to the special fact
`Xi(a)=0` must hold for arbitrary symmetric node windows.  Such a closure is falsified by the shifted
controls.  Therefore the remaining proof cannot be a universal kernel identity in the node variables
alone.

## 2. Node-blind residuals

Call a proposed residual construction node-blind if, for a finite symmetric window

```text
W={a_1,...,a_J} modulo a -> -a,
```

it builds

```text
R_W(L;Lambda)=Lambda K_W(L)+S_W(L)
```

from the finite operator data and universal kernels

```text
k_z,
K_L(z,w),
TailBasis_{z,n}^M(w),
```

but uses no additional relation satisfied only by zeros of `Xi`.

In particular, after the nodes are chosen, the same formula makes sense for arbitrary shifted windows
avoiding removable singularities.

## 3. Node-blind theorem test

Suppose a node-blind construction were a valid proof of the Xi-window row certificate for every
possible off-line contradiction window.  Since the proof would be an identity in the universal finite
kernels, it would continue to hold after replacing the zero nodes by nearby generic shifted nodes,
unless a special Xi-zero relation is used.

Thus a necessary condition for a node-blind CFIR theorem is:

```text
LAMBDA-ELIM holds for arbitrary shifted windows.
```

In the affine form of E72.354, this means:

```text
vec(S_W Adj(E)) and vec(K_W Adj(E)) are linearly dependent
```

for arbitrary `W`.

## 4. Falsification

E72.354 tests exactly this condition on generic shifted windows built from the finite-root heights:

```text
a_j = 0.5 + i tau_j.
```

The normalized 2x2 minor defect is:

```text
wedgeRel ~= 0.13 to 0.38.
```

Artificial compatible controls pass at roundoff:

```text
wedgeRel ~= 1e-16.
```

Therefore the failure is not numerical.  The current universal-kernel residual is not node-blindly
scalar-compatible.

## 5. Consequence

The remaining proof must use one of the following, and only one of them is acceptable:

```text
acceptable:
  a non-circular identity derived from the explicit formula which applies specifically to Xi-zero
  windows before any off-line suppression is assumed.

not acceptable:
  inserting G_x(a)=0, because Xi-zero nodes are not finite Weyl roots;

not acceptable:
  adding rowspace rows A(C_E-mu I), because E72.352 proves they are defect-invariant;

not acceptable:
  fitting Lambda_L after the fact, because E72.354 gives the exact compatibility minors.
```

Thus the next object cannot be another universal interpolation kernel.  It must be an Xi-divisor
compatibility identity.

## 6. The sharpened open statement

The Phase 72 endpoint is now:

```text
Xi-specific CFIR compatibility:

For every finite off-line Xi-zero contradiction window W_T,
the exact divisor-derived residual S_T^{Xi} satisfies

  vec(S_T^{Xi} Adj(E)) wedge vec(K_T Adj(E)) = O(L^B)

and the recovered scalar equals Lambda_L=mu+e_pole-2kappa_* up to polynomial error.
```

This statement is still finite and testable, but it is no longer node-blind.  The proof must expose
which zero-divisor identity supplies the missing collinearity.

## 7. Status

```text
proved: node-blind scalar CFIR closure would pass arbitrary shifted windows;
observed: arbitrary shifted windows fail the exact Lambda-elimination minors;
concluded: current universal-kernel residual is insufficient;
open: derive a non-circular Xi-divisor compatibility identity for S_T^{Xi}.
```
