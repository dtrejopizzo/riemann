# P76.029 - Weak exponential closure theorem

Let `g_{L,N}` be the exact normalized boundary density of P76.026, extended
by zero outside `[-L/2,L/2]`, so that

```text
Phi_{L,N}(z)=int_R exp(izx) g_{L,N}(x) dx.
```

Fix `a>1/2`.  Along a path with `N(L)/L -> infinity`, assume:

### BCF-TV

```text
sup_L int_R exp(a|x|)|g_{L,N(L)}(x)| dx < infinity.   (WE-1)
```

### BCF-EULER-MOMENT

For every `sigma` in a nonempty open interval `I subset (1/2,a)`, locally
uniformly in `sigma`,

```text
int_R exp(sigma*x)g_{L,N(L)}(x) dx
 -> Xi(1/2+sigma)/Xi(1/2).                           (WE-2)
```

Then `Phi_{L,N(L)}` converges locally uniformly to normalized `Xi` on
`|Im z|<a`, and Omega7 follows from P76.023 and Hurwitz.

## Proof

For every compact `K` in `|Im z|<a`, choose `a_K<a` with
`|Im z|<=a_K` on `K`.  Equation `(WE-1)` gives

```text
|Phi_{L,N}(z)|
 <=int exp(a_K|x|)|g_{L,N}(x)|dx
 <=int exp(a|x|)|g_{L,N}(x)|dx,
```

uniformly on `K`.  Hence the family is normal.  Equation `(WE-2)` identifies
every subsequential limit with normalized `Xi` on the open segment
`z=-i sigma`, `sigma in I`; the identity theorem identifies it throughout
the connected strip.  Every subsequence has the same limit, so the full
family converges.  Finite real-rootedness and Hurwitz give Omega7.

## Exact finite formulas

Neither hypothesis requires inversion of a Fourier transform:

```text
int exp(sigma*x)g_{L,N}(x)dx = Phi_{L,N}(-i sigma),
```

and `Phi` is the normalized Schur/Cauchy determinant ratio `(BCF-1)`.
Therefore `(WE-2)` is an arithmetic statement entirely in the Euler-safe
half-plane.  `(WE-1)` is a stability bound for the same canonically
normalized Schur null vector.

This is strictly weaker than `BF-WL1`: oscillatory densities may converge
weakly while retaining nonvanishing absolute `L1` distance.

## Remaining endpoint

The proof burden is now exactly:

```text
WE-STABILITY: prove (WE-1) without an inverse-gap bound;
WE-EULER: evaluate the finite Schur moment in Re(s)>1 and prove (WE-2).
```

The rank-two displacement identity must be used before absolute values in
`WE-STABILITY`; P76.016 shows that termwise estimates lose the cancellation.
