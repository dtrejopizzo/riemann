# E83.007 - Endpoint resonance and failure of global smallness

## 1. The uncancelled left wedge

The kernel in E83.006 contains a region in which Mobius inversion has no
nontrivial divisor available.

### Proposition 1.1

If

```text
0<=t<log 2,
t<=L-y,                                               (1.1)
```

then

```text
(R_yf)(t)
 =sum_{exp(t)<k<=exp(t+y)}k^(-sigma)f(t+y-log k).      (1.2)
```

### Proof

Every divisor satisfying `d<=exp(t)<2` is `d=1`.  Hence

```text
D_k(t)=mu(1)=1                                        (1.3)
```

for every integer in the sum (3.1) of E83.006.  Substitution gives (1.2).
`QED`

There is no oscillatory arithmetic coefficient in (1.2).  The gauge is the
identity at the extreme left because no nontrivial multiplicative shift has
yet entered.

## 2. A uniform operator-norm obstruction

### Theorem 2.1

Choose `y_0` and `eta` such that

```text
log 2<y_0<min(log 3,L),
0<eta<min(log 2,L-y_0,log 3-y_0).                      (2.1)
```

Then

```text
(R_{y_0}f)(t)
 =2^(-sigma)f(t+y_0-log 2),
                         0<=t<=eta,                   (2.2)
```

and consequently

```text
norm(R_{y_0})>=2^(-sigma).                             (2.3)
```

### Proof

For `0<=t<=eta`, conditions (2.1) imply

```text
exp(t)<2<=exp(t+y_0)<3,
t<=L-y_0.                                             (2.4)
```

Thus the sum (1.2) contains exactly `k=2`, proving (2.2).  Take `f` supported
on

```text
[y_0-log 2,y_0-log 2+eta].                            (2.5)
```

Translation preserves its `L^2` norm and (2.2) gives

```text
norm(1_[0,eta]R_{y_0}f)_2=2^(-sigma)norm(f)_2.         (2.6)
```

The operator norm bound (2.3) follows. `QED`

The lower bound is independent of the outer interval once (2.1) is
available.  Hence the family `R_y` does not become small in global operator
norm as `L` grows.

## 3. What the obstruction does and does not prove

Theorem 2.1 rules out each of the following proposed shortcuts:

```text
R_y -> 0 in operator norm;
absolute summation of norm(R_y) over y;
uniform boundary smallness before insertion of the model vector;
Mobius cancellation alone as a proof of GE-2.          (3.1)
```

It does not rule out cancellation after all of the following have been kept:

```text
the actual Euler-generated vector;
the signed renormalized y-integral;
the bilateral safe Cauchy functional;
the finite Fourier compression correction.            (3.2)
```

These data can annihilate a fixed boundary translation even though its
operator norm is bounded below.

## 4. Minimal surviving theorem

Let

```text
B_L=M[H_L^A,Z]=integral_0^L a_L(y)R_y dy              (4.1)
```

on the common core, and let `w_L` be the explicit Euler-generated model
vector required in E83.002.  The surviving statement is the scalar theorem

```text
SAFE-BOUNDARY-PAIRING:
ell_{N,z}(P_N B_L w_L + FourierShell_{N,L})
has the correction limit prescribed by GE-2 and GE-3,
uniformly on every safe compact, together with one z derivative.   (4.2)
```

Neither `B_L` nor `R_y` may be replaced by its norm in (4.2).  This is the
smallest formulation not contradicted by Theorem 2.1.

## 5. Status

```text
proved:
  an exact positive-coefficient endpoint wedge;
  a nonvanishing operator-norm lower bound;

refuted:
  global smallness of the Mobius-gauged boundary commutator;
  proof of Gamma--Euler compatibility by operator norms;

localized:
  the remaining theorem to SAFE-BOUNDARY-PAIRING on one explicit vector;

next:
  identify w_L from the coupled source and compare (4.2) term by term with
  the scalar Weyl reduced-leakage statement.
```

