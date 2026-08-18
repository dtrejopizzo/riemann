# E101.027 - Safe resolvent wall

## 1. Exact bordered numerator

Use the cofactor variables of E94.001:

```text
N(z)=C-q^T(zI-D)^(-1)y,                              (1.1)

C=det(M)-1^Tadj(M)b,
y=adj(M)b.                                           (1.2)
```

At `z=i sigma`,

```text
||(i sigma I-D)^(-1)||<=1/sigma.                    (1.3)
```

This suggests a far-right expansion, but its exact small parameter is

```text
eta_(L,N)(sigma)
 ={||q|| ||y||}/{sigma |C|}.                         (1.4)
```

## 2. Necessary projective condition

If `eta<1`, then

```text
N(z)=C[1-r(z)],
r(z)=q^T(zI-D)^(-1)y/C,                              (2.1)
```

and the logarithmic series for `N` is controlled.  Without a bound on (1.4),
the resolvent estimate (1.3) gives no uniform expansion.

For invertible `M`, put

```text
x=M^(-1)b,
c=1-1^Tx.                                           (2.2)
```

Then

```text
y=det(M)x,
C=det(M)c,                                           (2.3)
```

so the projective condition number is exactly

```text
eta_(L,N)(sigma)
 ={||q|| ||x||}/{sigma |c|}.                         (2.4)
```

The common determinant scale cancels; projective clearing does not improve
the ratio.

## 3. Collision with the determining-set requirement

A Neumann proof based only on (1.3) requires evaluation points satisfying

```text
sigma_(L,N)>>||q|| ||x||/|c|.                        (3.1)
```

The secular coefficient `c=1-1^Tx` is the small ceiling coefficient isolated
in the earlier IDENT analysis.  No cutoff-uniform lower bound for `|c|` is
available; finite zeta sections make it extremely small.

If the right side of (3.1) grows, the admissible evaluation point must drift
to infinity.  E101.026 proves that such a drifting regime cannot detect a
finite off-line quartet.  Hence the two requirements conflict:

```text
Neumann control from the raw resolvent:  sigma must drift;
Stieltjes uniqueness and discrimination: sigma must be fixed.       (3.2)
```

## 4. Degree-only bound is also insufficient

Finite real-rootedness gives

```text
g_core,(L,N)(x)
 =sum_j1/(x+kappa_j^2)
 <=deg(P_(L,N))/x.                                   (4.1)
```

The degree grows with the Fourier cutoff, so (4.1) supplies no cofinal mass
bound at fixed `x`.  Real-rootedness prevents a safe zero but does not control
the number of secular zeros in a bounded Stieltjes window.

## 5. Decision

Large fixed `sigma` may still be useful after a projective coefficient theorem
has been proved.  It cannot produce that theorem from the safe resolvent norm
alone.  A bound strong enough to make (1.4) uniform is part of the endpoint
identification problem, not free absolute-convergence input.

## 6. Status

```text
proved:
  exact projective small parameter for the safe-resolvent expansion;
  cancellation of the irrelevant determinant scale;
  incompatibility of a drifting Neumann regime with fixed-point
  discrimination;

closed as insufficient:
  a far-right proof using only ||(i sigma I-D)^(-1)||<=1/sigma;

open:
  fixed-point projective cofactor identification.
```

