# R161_012 — Product range certificate and the finite first-collar equation

## 0. Purpose

The scattering audit reduces the route to more than abstract Sonin membership.  The phase-161 port has the explicit
Mellin numerator

```
G_(+,T)(z)=-zeta'(1/2+z)K_F(z)-zeta(1/2+z)Q_(+,T)(z),             (0.1)
```

after the canonical polar correction.  Its oriented quotient is

```
G_(+,T)(z)/zeta(1/2+z)
=-(zeta'/zeta)(1/2+z)K_F(z)-Q_(+,T)(z).                           (0.2)
```

Thus the missing arithmetic restriction on the Sonin port is a physical range certificate for division by zeta,
not a new choice of norm.

## 1. Exact range criterion

Let `G_(+,T)^0` denote the corrected `H2(C_+)` numerator of `R161_008`--`R161_009`.  Define the causal physical
co-Poisson range by

```
Ran_phys(Z_+)
 ={G in H2(C_+) : G/zeta(1/2+.) is the boundary transform
                    of a causal physical source}.                 (1.1)
```

This is a definition of a graph range, not meromorphic divisibility.  The phase-121 pole-rigidity theorem and
`R161_007` give:

**Proposition 1.1 (range certificate closes first contact; PROVED CONDITIONALLY).** If a primitive first-contact
state satisfies

```
G_(+,T)^0 in Ran_phys(Z_+),                                        (1.2)
```

then `F=0`.

*Proof.* Physical range membership makes the quotient in (0.2) holomorphic across every simple critical zero. Its
residue there is `-K_F(i gamma)`. Hence `K_F(i gamma)=0` on the unconditional superlinear family of simple critical
zeros. Cartwright zero counting makes `K_F` identically zero, and Laplace injectivity gives `F=0`.  The polar
correction is a zeta multiple and changes neither the quotient residue nor the critical numerator value. ∎

The word “physical” is indispensable.  Every `G_(+,T)^0` is formally a zeta multiple of the meromorphic quotient
(0.2); accepting that formal factorisation would assume the desired zero cancellation.

## 2. Relation with the Sonin intersection

The correctly typed cosine/reflection graph puts `G_(+,T)^0` in the parity Sonin eigenspace described in
`R161_011`.  Therefore either of the following independently sufficient statements closes D:

```
(A) G_(+,T)^0 in Ran_phys(Z_+);                                    (2.1)
(B) Ran(P_T^PC | radical) intersect Son_T^epsilon={0}.             (2.2)
```

Statement (A) uses the arithmetic zeros of the co-Poisson range; statement (B) kills the entire port geometrically.
They must not be conflated.  Burnol's range audit shows that generic Sonin membership does not imply (A): the missing
zero cancellations are exactly the obstruction to the co-Poisson range.

The new information of phase 161 is that the numerator in (A) is already an ordinary `H2` function.  Only the
quotient graph remains singular.

## 3. Literal first collar in the chamber above `0.8`

Put

```
delta_T=min(log 2, log 5-2T)>0,
0.8<T<(log 5)/2.                                                  (3.1)
```

Choose the harmless polar profile `theta_T` with support strictly to the right of `T+delta`, where
`0<delta<delta_T`.  On `T<t<T+delta`:

1. the outer zeta convolution contributing to `G_+^0` has only its `m=1` term, because `t-log m<T` for every
   `m>=2`;
2. the oriented prime tail has only `n=2,3,4`, because `t-log n<-T` for every `n>=5`;
3. the polar correction vanishes by the chosen support of `theta_T`.

Consequently the product port has the exact, non-asymptotic boundary germ

```
g_(+,T)^0(t)
 = (log 2)/sqrt(2) F(t-log 2)
  +(log 3)/sqrt(3) F(t-log 3)
  +(log 2)/2       F(t-log 4),
          T<t<T+delta.                                           (3.2)
```

**Proof.** Before continuation, the inverse Laplace transform of `G_+` is `Z_+(1_[T,infinity)Y_+)`.  On the stated
collar local finiteness makes this literal.  The first inequality in (3.1) removes all outer shifts `m>=2`; the
second removes all prime powers `n>=5`.  Since `Lambda(4)=log 2`, the three remaining coefficients are those in
(3.2).  The two sides are `L2` boundary representatives of the same holomorphic germ, so the identity persists for
the corrected port on this collar. ∎

This is the first place where the simultaneous sum--product construction yields a finite physical equation rather
than a scalar continuation.

## 4. What (3.2) can and cannot prove

If the whole product port vanished, (3.2) would give a three-delay recurrence and Proposition 1.1 would already
give the stronger global conclusion.  Sonin membership alone, however, does not make the left side vanish on its
first collar.  Therefore (3.2) is not yet the phase-121 boundary-germ implication.

The next lemma must use the first-contact equation in addition to the cosine eigenrelation and prove one of:

```
g_(+,T)^0=0 on a nonempty collar;                                  (4.1)
G_(+,T)^0 in Ran_phys(Z_+);                                       (4.2)
```

or directly that the three-delay germ (3.2) has zero source trace.  A proof based only on the two Tate moments,
parity or scalar commutation is excluded by the phase-121 countermodels.

## 5. Falsifiable next calculation

On the same collar, substitute the three-delay expression (3.2) into the differentiated co-Poisson identity

```
[Q,Z_+]F=Z_+B_+F.                                                  (5.1)
```

Retain the cosine/reflection component instead of supertracing it.  The target is an explicit two-equation system
for the three translates in (3.2), with the Gamma affine term and the two crossed Tate scalars included.  The test
is decisive:

- if the second equation is independent of (3.2), eliminate the three translates and propagate a zero collar;
- if it is only the cosine transform of (3.2), the construction has returned to the Sonin equivalence and no
  closure is claimed.

`R161_013` performs this test.  The differentiated identity is only the same three-delay equation, so the second
row is not independent.  The surviving new equation is the inner/outer transmission through the nonlocal Gamma
term `C Q C`.

## 6. Status

- explicit `H2` numerator and critical jet: **PROVED**;
- physical co-Poisson range implication: **PROVED CONDITIONALLY / range membership OPEN**;
- finite first-collar formula (3.2): **PROVED**;
- independent differentiated collar equation: **REJECTED; it repeats (3.2)**;
- unsupertraced Gamma collar transmission: **PROVED in `R161_013`; rigidity consequence OPEN**;
- row D: **OPEN**.
