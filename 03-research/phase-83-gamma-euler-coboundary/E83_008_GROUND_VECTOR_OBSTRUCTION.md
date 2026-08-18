# E83.008 - Ground-vector obstruction in the physical module

## 1. The module derivation forced by the shift representation

On the operator algebra of E83.004, the scale derivation is

```text
delta(S_y)=[X,S_y]=yS_y,                              (1.1)
```

where `X` is multiplication by `t`.  The compatible derivation on the
physical vector module is therefore

```text
delta(f)=Xf.                                           (1.2)
```

Indeed,

```text
X(S_yf)=[X,S_y]f+S_y(Xf),                              (1.3)
```

which is precisely the module Leibniz rule used in E83.001.

## 2. There is no nonzero physical ground vector

### Proposition 2.1

On `L^2(0,L)`,

```text
ker X={0}.                                             (2.1)
```

### Proof

If `Xf=0`, then `t f(t)=0` for almost every `t`.  Since `t` is nonzero almost
everywhere on `(0,L)`, one has `f=0` almost everywhere. `QED`

Consequently the hypothesis

```text
delta k=0                                             (2.2)
```

in E83.002 forces `k=0`, and then

```text
w=(Z-I)k=0,
u=JZ^(-1)w=0.                                         (2.3)
```

Thus the nontrivial one-vector criterion of E83.002 cannot be instantiated
inside the physical Hilbert module as stated.

## 3. Exact formula without the ground assumption

The obstruction cannot be removed merely by dropping (2.2).  For an arbitrary
`k` in the common domain and `w=(Z-I)k`, the gauge identity gives

```text
Z^(-1)delta w
 =A k+(I-Z^(-1))delta k,                               (3.1)

A k
 =Z^(-1)delta w-(I-Z^(-1))delta k.                    (3.2)
```

The extra term in (3.2) is a new source defect.  Unless it is independently
controlled, the proposed coboundary has only moved the original source into
`(I-Z^(-1))delta k`.

## 4. The unique distributional repair

Let the vector module be enlarged to distributions on the closed interval.
The solutions of

```text
t T=0                                                 (4.1)
```

are exactly

```text
T=c delta_0.                                          (4.2)
```

### Proof

Equation (4.1) implies that the support of `T` is contained in `{0}`.  Every
distribution supported at one point is a finite linear combination of
derivatives of `delta_0`.  The identity

```text
t delta_0^(j)=-j delta_0^(j-1)                        (4.3)
```

then shows recursively that all derivative coefficients vanish except the
coefficient of `delta_0`. `QED`

Moreover the one-sided shifts satisfy, distributionally,

```text
S_y delta_0=delta_y.                                  (4.4)
```

Hence

```text
Z delta_0
 =sum_{n<=exp(L)}n^(-sigma)delta_{log n},              (4.5)

M[X,Z]delta_0
 =sum_{n<=exp(L)}Lambda(n)n^(-sigma)delta_{log n}.     (4.6)
```

Formula (4.6) is the exact prime-power current.  The desired ground vector
therefore exists canonically, but only in a rigged endpoint module, not in
`L^2(0,L)`.

## 5. Decision

The Hilbert-space version of `GAMMA-EULER-INTERTWINER` is closed as
inconsistent with its own ground hypothesis.  The admissible replacement is
a distributional endpoint theorem with three additional duties:

```text
1. define the Gamma and Euler actions on a common rigged module;
2. prove that finite Fourier projection produces the exact coupled source;
3. prove the safe paired limit without using an ambient distribution norm.
                                                                    (5.1)
```

The endpoint resonance of E83.007 is compatible with this conclusion: the
left boundary survives because the arithmetic ground state is concentrated
there.

## 6. Status

```text
proved:
  ker X={0} on the physical Hilbert module;
  exact correction formula when delta k is nonzero;
  uniqueness of delta_0 as a distributional ground vector;
  exact Euler orbit and prime current generated from delta_0;

closed:
  the nontrivial L^2 ground-vector implementation of E83.002;

opened:
  a rigged endpoint module based on delta_0.
```

