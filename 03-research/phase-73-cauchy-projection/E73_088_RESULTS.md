# E73.088 results - Local root-locking probe

## 1. Purpose

E73.087 defines the canonical local zero window `Z_loc(A,L)`.  The next analytic question is why
`H_0(w)` should be small on that window without simply measuring it.

E73.088 tests the finite root-locking mechanism:

```text
if -gamma is near a root r of C(t)=sum_n xi_n/(t-d_n),
then |C(-gamma)| <= |-gamma-r| sup_[r,-gamma] |C'(t)|.
```

Since

```text
H_0(i gamma) = -i C(-gamma),
```

this gives a non-spectral, finite Cauchy explanation for local nodal smallness.

## 2. Representative output

```text
 lam     L tau  gamma      distB     derB  boundB  actualB   ratio
  18   5.781   14.13   14.13   -19.358    2.614  -16.744  -16.871    0.800
  18   5.781   14.13   21.02   -18.963    0.305  -18.658  -18.989    0.560
  18   5.781   14.13   25.01     0.789    0.507    1.296  -14.272    0.000

  24   6.356   21.02   21.02      -inf   -0.120  -18.796  -19.079    0.592
  24   6.356   21.02   25.01   -17.240   -0.938  -18.179  -19.792    0.051
  24   6.356   21.02   14.13   -16.583   -0.927  -17.509  -18.860    0.082
```

Here `distB`, `derB`, `boundB`, `actualB` mean powers of `L`.

## 3. Diagnosis

The bound:

```text
|C(-gamma)| <= dist(-gamma,Div(C)) sup |C'|
```

holds in the tested local window.

Two regimes appear:

```text
root-locked nodes: distance is around L^-16 to L^-19;
companion nodes:  distance can be macroscopic in small data, but C(-gamma) remains small by
                  additional cancellation.
```

Thus the local HWIN proof should not claim that every companion node is root-locked.  It should
split:

```text
Z_loc(A,L) = Z_lock(A,L) union Z_comp(A,L).
```

## 4. Consequence

The finite calculus part is proved:

```text
ROOT-PROX + DERIVATIVE-BOUND => local H_0 smallness.
```

The remaining uniform theorem is:

```text
LOCAL-LOCK:
for the root-locked part, critical nodes in Z_lock(A,L) remain polynomially/exponentially close
to finite Cauchy roots with derivative growth below the available HWIN margin.
```

and:

```text
COMP-RES:
the finite companion nodes have a separate residual bound strong enough for LOCAL-HWIN-5.
```

## 5. Status

```text
proved finite lemma: root proximity bounds H_0 by derivative times distance;
observed: root-locked part has very large slack;
observed: companion nodes need a separate analytic residual mechanism;
next: state LOCAL-HWIN as LOCK + COMP sufficient theorem.
```
