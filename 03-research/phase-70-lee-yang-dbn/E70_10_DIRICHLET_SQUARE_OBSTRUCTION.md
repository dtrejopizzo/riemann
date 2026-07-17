# E70.10 -- Dirichlet-square obstruction for the naive Euler-Gamma factor

**Date:** 2026-07-07.
**Role:** test the most direct Wiener-Hopf square after E70.9 and isolate the exact algebraic
obstruction.

## The tempting square

The Hardy-shift form of the remaining inequality is

```text
A - T_Lambda >= 0,
T_Lambda = sum_{n>=2} Lambda(n)n^{-1/2}(S_log n + S_log n^*),
```

where `S_a` is the unilateral shift on the additive Hardy model:

```text
(S_a f)(t) = 1_{t>=a} f(t-a),       a>=0.
```

The most direct attempt is to build a Dirichlet shift

```text
V = sum_{n>=2} b_n S_log n,
b_n = Lambda(n)n^{-1/2},
```

so that

```text
V + V^* = T_Lambda.
```

Then

```text
(I - V)^*(I - V) = I - T_Lambda + V^*V.
```

Thus this square would prove `A-T_Lambda>=0` only if the archimedean operator had the identity

```text
A = I + V^*V.
```

This is the first place where the construction can either become new mathematics or collapse into a
hidden Euler/KMS insertion.

## Shift algebra computation

For unilateral shifts on `L^2(R_+)`,

```text
S_a^* S_b =
  S_{b-a},     b>=a,
  S_{a-b}^*,   a>b.
```

Therefore, for any finite Dirichlet shift, and then formally for its Abel boundary family,

```text
V_epsilon = sum_{n>=2} Lambda(n)n^{-1/2-epsilon} S_log n,    epsilon>0,
```

one has

```text
V_epsilon^*V_epsilon
 = sum_{m,n>=2} b_m b_n S_log m^* S_log n
```

and hence the square contains shifts at all logarithmic ratios:

```text
log(n/m).
```

Equivalently, after grouping by rational ratios `r>1`,

```text
V_epsilon^*V_epsilon
 = c_1(epsilon) I
   + sum_{r>1, r in Q} c_r(epsilon) S_log r
   + sum_{r>1, r in Q} c_r(epsilon) S_log r^*,
```

where

```text
c_1(epsilon) = sum_{n>=2} Lambda(n)^2 n^{-1-2epsilon},
```

and, for `r=a/b` in lowest terms,

```text
c_r(epsilon)
 = sum_{j>=1}
     Lambda(aj)Lambda(bj) (ab)^(-1/2-epsilon) j^(-1-2epsilon),
```

with the convention that terms with `Lambda(aj)Lambda(bj)=0` vanish.

All coefficients are nonnegative. In particular, whenever both `aj` and `bj` contain prime-power
support for some `j`, the ratio channel `log(a/b)` is present.

## Consequence

The diagonal Euler square `V_epsilon^*V_epsilon` is not archimedean. It is an Euler pair-correlation
operator supported on the ratio comb

```text
{ log(n/m) : m,n >= 2 }.
```

The Gamma/polar operator `A` is canonical and zeta-free. It has no independent Euler ratio-comb data.
Thus the identity

```text
A = I + V_epsilon^*V_epsilon
```

cannot be a non-circular Gamma identity. To make it true, one would have to put Euler pair correlations
into the object called `A`, which is exactly the forbidden move: the archimedean side would no longer be
archimedean.

There is also a boundary obstruction. In the Abel family, as `epsilon -> 0+`,

```text
c_1(epsilon) = sum_{n>=2} Lambda(n)^2 n^{-1-2epsilon}
```

diverges. Thus the naive Euler square has a growing incoherent diagonal mass at the critical boundary,
the same type of mass that appeared as the `S_abs` ceiling in Phase 67 and E70.5-E70.7.

## Formal no-go

### Linear Dirichlet-Square Obstruction

Let `V_epsilon` be a nonzero finite-truncation or Abel-boundary Euler shift whose coefficients are
supported on `log n` and whose Hermitian part gives the prime-shift operator:

```text
V_epsilon + V_epsilon^*
 = sum_{n>=2} Lambda(n)n^{-1/2-epsilon}(S_log n + S_log n^*).
```

Then any ordinary Hilbert-square factorization of the form

```text
A_epsilon - (V_epsilon+V_epsilon^*) = (G_epsilon - V_epsilon)^*(G_epsilon - V_epsilon)
```

contains the positive Euler square `V_epsilon^*V_epsilon`. If `G_epsilon` is a genuine zeta-free
Gamma/polar factor, so that it does not already contain Euler ratio-comb channels, then these channels
cannot be absorbed into `A_epsilon`. Unless `V_epsilon^*V_epsilon` is cancelled by another
signed/graded sector, the right side contains Euler ratio-comb channels `log(n/m)` and critical
incoherent mass.

Therefore a non-circular proof cannot be the ordinary square of a linear Euler Dirichlet shift with a
pure archimedean factor.

## What remains possible

E70.9 said that the prime term must appear as a cross term. E70.10 sharpens this:

```text
cross term:       necessary,
ordinary square:  insufficient.
```

The remaining factorization, if it exists, must have one of the following stronger forms:

1. **Graded/supersymmetric cancellation.** A second sector cancels `V^*V` before positivity is taken
   on the physical quotient.
2. **Nilpotent or triangular Euler differential.** The Euler component is not an ordinary shift sum;
   its square vanishes or becomes purely archimedean by an algebraic relation independent of zeta.
3. **Nonlinear Euler-Gamma identity.** The prime operator is not represented by a linear Dirichlet
   shift, but by an object whose cross term is `T_Lambda` while its diagonal term is Gamma/polar.

The first two are the only shapes that still look structurally compatible with the previous no-go
results. A plain Wiener-Hopf square is now ruled out as another form of the incoherent ceiling.

## Updated target

The closure target is no longer just

```text
A - T_Lambda = D^*D.
```

It is the sharper identity

```text
A - T_Lambda = Q(D)^*Q(D)
```

where `Q` is a quotient or grading that removes the Euler ratio-square `V^*V` by algebraic necessity,
not by estimating it and not by inserting zeta.

In words:

```text
Omega_7 can only close by an Euler-Gamma cancellation identity whose off-diagonal part is prime
and whose diagonal Euler pair-correlations are exact boundaries/negligibles.
```

That is the next mathematical object to build.
