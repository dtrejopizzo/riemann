# 114.a.07 — Toric realisation of the Haar quadric: G-0 closed positively

```
+--------------------------------------------------------------------------+
| CATEGORY     Semipositive adelic toric metrics (uniform limits of smooth  |
|              semipositive metrics), not only smooth Gillet--Soulé data.   |
|                                                                          |
| METRIC       On O(k), ||P([z0:z1])||can = |P(z0,z1)|/max(|z0|,|z1|)^k.  |
|              Put ||.||k,a = e^{-a}||.||can.                             |
|                                                                          |
| MEASURE      c1(O(1),||.||can) is Haar probability measure on |z|=1.    |
|              Hence the induced L2 lattice is exactly Z^{k+1} with the    |
|              scaled Euclidean norm used in 114_a_02.                     |
|                                                                          |
| INTERSECTION The global roof function is the constant a on [0,k].        |
|              Toric height = 2! int_[0,k] a dx = 2ka.  Polarisation gives |
|              <(k,a),(k',a')> = ka' + k'a.                               |
|                                                                          |
| RESULT       The norm and hyperbolic form of a4-weak are now realised in  |
|              one established Arakelov category.  G-0 is CLOSED.          |
|                                                                          |
| LIMIT        This does not construct the F_1 square or the I7 kernel      |
|              pairing.  It upgrades a4-weak, not a4-strong.               |
+--------------------------------------------------------------------------+
```

## 1. Sources and conventions

The primary source is Burgos Gil--Philippon--Sombra, *Arithmetic geometry of
toric varieties. Metrics, measures and heights*, arXiv:1105.5584, especially:

- Chapter 4, the canonical toric metric and the correspondence between
  semipositive toric metrics and concave functions;
- Theorem 4.8.1: semipositive toric metrics are described by concave functions
  and are uniform limits of semipositive algebraic/smooth metrics;
- Theorem 5.1.6 and Theorem 5.2.5: local/global height equals the integral of
  the roof function;
- the canonical toric height is zero.

The later paper Burgos Gil--Moriwaki--Philippon--Sombra, *Arithmetic positivity
on toric varieties*, arXiv:1210.7692v2, §4--§5, uses the same category and
states

```
h_D(X) = (n+1)! integral_Delta theta_D(x) dx
```

for a semipositive toric metrized divisor on an `n`-dimensional toric variety.

Our norm convention is that replacing `||.||` by `e^{-a}||.||` enlarges the
unit ball by `e^a`.  This matches `114_a_02`.

## 2. The canonical toric metric and its measure

Let `X=P^1_Z`, with homogeneous coordinates `[z0:z1]`, and let `L=O(1)`.
For a homogeneous section `P` of degree `k`, define

```
||P([z0:z1])||can = |P(z0,z1)| / max(|z0|,|z1|)^k.             (2.1)
```

This is independent of the homogeneous representative and is the canonical
toric metric on `O(k)`.  It is continuous and semipositive in the admissible
toric sense; it need not be smooth along `|z0|=|z1|`.

### Proposition 2.1 (the Chern measure is Haar)

On the affine chart `z=z1/z0`, the canonical potential is

```
g(z)=log max(1,|z|).
```

Its distributional Laplacian is the normalized Haar measure on the unit
circle.  Equivalently,

```
c1(O(1),||.||can) = dtheta/(2 pi) supported on |z|=1.          (2.2)
```

*Proof.* The function `g` is harmonic on `|z|<1` and on `|z|>1`; its radial
normal derivative jumps by one at radius one.  Green's formula therefore
places the full unit mass uniformly on the circle.  This is also the standard
measure associated with the canonical metric in the cited toric theory. `[]`

Thus the measure introduced in `114_a_02` was not an arbitrary measure looking
for a metric: it is the Chern/Monge--Ampère measure of (2.1).

## 3. Exact recovery of the section lattice

For `D=(k,a)` put

```
L_D = (O(k), ||.||k,a),       ||.||k,a = e^{-a}||.||can.       (3.1)
```

### Proposition 3.1 (the Haar `L2` norm is the old norm)

For `P(z)=sum_{j=0}^k c_j z^j`,

```
||P||L2(D)^2
 = integral_|z|=1 ||P(z)||k,a^2 dtheta/(2pi)
 = e^{-2a} sum_{j=0}^k |c_j|^2.                              (3.2)
```

*Proof.* On the unit circle the denominator in (2.1) is one.  The characters
`1,z,...,z^k` are an orthonormal family for Haar measure. `[]`

Consequently the theta series, its exact Jacobi identity, and every lattice
calculation in `114_a_02` remain unchanged.

## 4. The arithmetic intersection is the hyperbolic form

The toric divisor `O(k)` has polytope

```
Delta_k=[0,k].
```

For the canonical metric the metric function is the support function and the
roof function is zero.  Multiplying the metric by `e^{-a}` subtracts `a` from
the logarithmic metric function, hence adds `a` to its Legendre--Fenchel dual.
Therefore

```
theta_(k,a)(x)=a,       x in [0,k].                            (4.1)
```

### Theorem 4.1 (derived self-intersection)

In the semipositive adelic toric intersection theory,

```
L_D^2 = h_{L_D}(P^1) = 2! integral_0^k a dx = 2ka.            (4.2)
```

*Proof.* Apply the toric height formula in dimension one to (4.1).  At every
finite place the canonical model metric has zero roof, so there are no omitted
finite terms. `[]`

### Corollary 4.2 (derived mixed intersection)

For `D=(k,a)` and `D'=(k',a')`,

```
<D,D'> = (1/2)((D+D')^2-D^2-D'^2) = ka' + k'a.                (4.3)
```

In particular `(1,0)^2=(0,1)^2=0` and `(1,0).(0,1)=1`.  The
hyperbolic plane of `114_a_02` is therefore not an imposed analogy: it is the
polarisation of a genuine toric adelic arithmetic self-intersection.

### Corollary 4.3 (degree and canonical class)

With `H=(1,1)`,

```
deg_H(k,a)=<D,H>=k+a,     H^2=2.
```

The underlying canonical divisor of `P^1` is `O(-2)`.  Equipping it with the
dual canonical toric metric gives `K=(-2,0)`, so

```
(1/2)D.(D-K)=ka+a.                                           (4.4)
```

Combined with Proposition 3.1 and Jacobi,

```
h0_theta(D)=(1/2)D.(D-K)+(k+1)log theta(e^{2a}).              (4.5)
```

Equation (4.5) is an exact identity for the theta invariant of the normed
section lattice.  It is compatible with the toric intersection just derived.
It is not being identified with a full analytic-torsion arithmetic
Riemann--Roch theorem beyond this explicitly computed invariant.

## 5. What this closes

`114_a_06` introduced G-0 because `114_a_02` had specified only the Haar
section norm and had stipulated the pairing.  Propositions 2.1 and 3.1 plus
Theorem 4.1 supply the missing common category and derivation.

> **G-0 is closed positively:** the canonical semipositive toric metric
> simultaneously produces the Haar measure, the Euclidean section lattices,
> and the hyperbolic arithmetic intersection form.

This restores the strong reading of **a4-weak**:

> A genuine arithmetic surface over `Spec Z` carries a semipositive adelic
> toric divisor family whose theta dimension has quadratic leading term equal
> to one half of its arithmetic self-intersection.

The qualifier “weak” remains essential.  The object is `P^1_Z`, not
`Spec Z x_{F1} Spec Z`, and Corollary 4.2 says nothing about the explicit
infinite-rank kernel of `114_a_05`.

## 6. Relation to I7

The canonical metric depends only on the degree/polytope coordinate and its
constant rescaling.  Cyclotomic divisors of equal degree and Mahler measure
still have identical image in this rank-two sector.  Hence Theorem 2.1 of
`114_a_05` remains binding:

```
beta(Phi_3)=beta(Phi_6)=(2,0),
I_fin(Phi_3,Delta)=log 3 != 0=I_fin(Phi_6,Delta).
```

The toric construction closes the diagonal and metric for the rank-two
quotient; it cannot descend backwards to recover information discarded by
`beta`.  I7-C still requires a metric/intersection on the kernel itself.

## 7. Verifier and refutation conditions

`114_a_07_toric_realisation_verify.py` checks the metric's homogeneity,
orthogonality of the Haar monomial basis, the constant-roof height formula,
polarisation, the canonical class identity, and the `(3,6)` I7 control.

- **R42.** G-0 reopens if (2.2) is not the Chern current of (2.1).
- **R43.** G-0 reopens if the toric height formula does not apply to the
  canonical semipositive metric or if its roof is not zero before rescaling.
- **R44.** The exact pairing convention is wrong if rescaling by `e^{-a}` does
  not shift the roof by `+a` under the cited definitions.
- **R45.** Nothing here closes I7-C; any such claim must define a nondegenerate
  or proper kernel gauge and a finite diagonal compatible with resultants.

