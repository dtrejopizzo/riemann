# P123.003 — the dagger-complete rational kernel algebra

## Status

`PROVED-IN-REPOSITORY` for the algebra, its nuclear Frechet topology,
dagger, faithful scaling representation and distributional kernel
composition.

`OPEN` for strict localization of this completion in the semilocal
crossed-product sheaf and for comparison with the periodic mixed
Riemann--Roch determinant.

## 1. The defect in the one-sided coefficient algebra

The nuclear Dirichlet algebra `C_R` on `N^x` is closed under composition,
but not under the geometric transpose of scaling.  On
`L^2(R_+^x,d^*x)`, with

```text
(U_q f)(x)=f(qx),
```

one has

```text
U_q^*=U_(q^-1).
```

Thus a source-defined Rosati/dagger operation forces the coefficient
semigroup to be enlarged from `N^x` to `Q_+^x`.  Adding formal inverses
without a topology is insufficient: A requires a complete algebra on which
composition and dagger are continuous.

## 2. Symmetric arithmetic height

Write every `q in Q_+^x` uniquely as `q=a/b` with coprime positive
integers `a,b`, and define

```text
H(q)=max(a,b).
```

Then

```text
H(1)=1,
H(q^-1)=H(q),
H(qr)<=H(q)H(r).                                      (2.1)
```

The last inequality follows before cancellation by multiplying the two
reduced numerator/denominator pairs; reduction can only decrease their
maximum.

For `k>=0` put

```text
p_k(c)=sum_(q in Q_+^x) |c_q| H(q)^k
```

and define

```text
C_Q={c=(c_q):p_k(c)<infinity for every k>=0},          (2.2)
```

with group convolution

```text
(c*d)_q=sum_(rs=q)c_r d_s.                            (2.3)
```

## 3. Nuclear dagger algebra theorem

### Theorem 3.1

`C_Q` is a complete commutative unital nuclear Frechet algebra.  Its point
masses satisfy

```text
delta_q*delta_r=delta_(qr).
```

The formula

```text
(c^dagger)_q=conjugate(c_(q^-1))                      (3.1)
```

defines an isometric continuous involution for every seminorm and obeys

```text
(c*d)^dagger=d^dagger*c^dagger.                       (3.2)
```

Extension by zero gives a closed continuous algebra embedding

```text
C_R -> C_Q                                             (3.3)
```

from the original rapidly decreasing Dirichlet algebra on positive
integers.  On that subalgebra the seminorms are exactly the original ones.

### Proof

Submultiplicativity in (2.1), Tonelli and (2.3) give

```text
p_k(c*d)<=p_k(c)p_k(d).
```

The space (2.2) is the projective limit of the Banach spaces
`l^1(Q_+^x,H^k)`, so it is complete and Frechet.  The point mass at `1` is
the unit.

For nuclearity, consider the bonding inclusion from weight `k+4` to weight
`k`.  After conjugating both weighted `l^1` spaces to ordinary `l^1`, it is
the diagonal map with entries `H(q)^-4`.  The number of reduced positive
rationals of height exactly `N>1` is at most `2N`; hence

```text
sum_q H(q)^-4 <= 1+2 sum_(N>=2) N^-3 < infinity.
```

The diagonal bonding map is nuclear.  The standard projective-limit
criterion for countably normed spaces therefore makes `C_Q` nuclear.

Inversion permutes the rational labels and preserves `H`, proving that
(3.1) is isometric.  Formula (3.2) follows by replacing `rs=q` with
`s^-1 r^-1=q^-1`; commutativity is not needed for the anti-multiplicative
identity.  Finally, on integers `n/1`, `H(n)=n`.  Support on the closed
subset of integer coordinates defines (3.3), and convolution preserves
that support.  QED.

## 4. Faithful scaling-kernel realization

Use multiplicative Haar measure on the positive line and let

```text
H_scal=L^2(R_+^x,d^*x).
```

Every `U_q` is unitary.  Since `p_0(c)<infinity`, the series

```text
pi(c)=sum_q c_q U_q                                    (4.1)
```

converges absolutely in operator norm and

```text
||pi(c)||<=p_0(c),
pi(c*d)=pi(c)pi(d),
pi(c^dagger)=pi(c)^*.                                 (4.2)
```

### Proposition 4.1

The representation `pi:C_Q->B(H_scal)` is faithful.

### Proof

Under the logarithm and Fourier transform, `U_q` becomes multiplication by
`exp(i tau log q)` up to the fixed Fourier-sign convention.  Thus `pi(c)`
is multiplication by the continuous Fourier--Stieltjes transform of the
finite measure

```text
mu_c=sum_q c_q delta_(log q).
```

If `pi(c)=0`, that transform vanishes almost everywhere and hence
everywhere by continuity.  Uniqueness of the Fourier transform of finite
complex Borel measures gives `mu_c=0`.  The points `log q` are distinct,
so every `c_q=0`.  QED.

Equivalently, (4.1) has the distributional Schwartz kernel

```text
K_c(x,y)=sum_q c_q delta^x_(qx)(y),                    (4.3)
```

where `delta^x_z` is the Dirac mass normalized against multiplicative Haar
measure `d^*y`, so that integrating it against `f(y)d^*y` gives `f(z)`.

Composition of kernels with respect to `d^*x` gives

```text
K_c circle K_d=K_(c*d),
K_c^dagger=K_(c^dagger).                              (4.4)
```

The sums in (4.3) are interpreted through the bounded operator (4.1), not
as a locally finite point distribution: rational dilation labels are dense.

## 5. Consequence for row A

The algebra `C_Q` supplies a dagger-complete mixed coefficient and
distributional-kernel sector before B selects any arithmetic family.  Its
identity is `delta_1`, its composition is geometric scaling composition,
and its dagger is forced by Haar adjunction.  This discharges the global
algebraic part of A.2--A.4 more strongly than the one-sided corner of
P123.001.

It does not yet discharge the sheaf-theoretic part.  The imported
semilocal crossed-product sheaf has algebraic, finite group-label support;
(2.2) is an infinite nuclear completion.  Completion need not commute with
sheaf equalizers, so strict topological descent must be proved rather than
asserted.

## 6. Interfaces reserved for B and C

Row B has the canonical one-sided embedding

```text
delta_n |-> delta_n in C_Q,
Gamma_n |-> U_n.
```

The transpose is now already available:

```text
Gamma_n^dagger |-> U_(1/n).
```

Row C may apply an arithmetic trace distribution to admissible test
combinations.  No such scalar distribution, no `Lambda`, and no explicit
formula is used in the construction or proof above.
