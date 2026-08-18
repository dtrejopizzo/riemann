# D.28 — Completion audit and exact blocker for row D

## Scope audited

Row D requires all of the following, in this order:

1. a mixed object constructed independently of the zero divisor;
2. a primitive Hodge--Castelnuovo--Severi inequality on that object;
3. a strict equality theorem;
4. an exact comparison with the B--C nuclear intersection;
5. deduction of Weil positivity and RH.

Items 4 and 5 are already reduced exactly.  Item 2 remains unproved.

## What is constructed

* The two ruling degrees are the moments at `+1/2` and `-1/2`.
* `D^2-1/4` is a bijection from compact potentials to the primitive test
  space.
* Every finite prime tower is an exact periodic Poisson section norm minus
  its torsor norm.
* The archimedean term is the exact Gamma oscillator boundary norm.
* Consequently the full nuclear form has the source-defined factorization

  ```text
  B_nuc(F,F)=||S F||^2-||B F||^2.
  ```

* The equality case, once the sign is known, is strict.
* The dynamic contact of B and the trace of C agree term by term with this
  factorization.

## Independent routes audited

### Subcritical Szego Hodge space

The finite Lorentzian theorem uses parameter `n^-1`.  C forces
`n^-1/2`.  At the required weight the controlling sum changes from

```text
sum_(p,k) p^(-2k)<1
```

to

```text
sum_(p,k) p^(-k)=infinity.
```

Hence no isometric comparison exists (D.27).

### Ordinary and charged Hilbert completions

They have absolutely continuous scale spectrum.  The CCM/Meyer quotient
has discrete resonant jets.  Every equivariant map kills those jets, so no
faithful Hilbert descent exists (D.25--D.26 and 106.205).

### Resonant Hardy quotient

It retains all jets without listing zeros, but normalized scaling acts on
the evaluation vector at `a` by `exp(t conjugate(a))`.  Making this action
unitary in any equivalent positive metric forces `Re(a)=0`.  Thus the
missing metric is precisely the critical-line assertion (106.206).

### Root-cover correspondences

One row satisfies a finite Castelnuovo--Severi inequality.  Cross
intersection in the common refinement is `gcd(m,n)`.  The primitive matrix
for `(m,n)=(2,3)` is

```text
[[-2,-4],[-4,-3]],
```

of signature `(1,1)`, so the multirow Hodge theorem fails (106.208--209).

### Green/current and total positivity

The Green inversion identifies the correct primitive space but leaves the
arithmetic residual.  Positivity of the resulting screw kernel is Weil
positivity itself.  Ordinary TP2 and the relevant Euler minor fail (D.16).

### Curvature

Positive von Mangoldt weights give the exact unconditional
`CD(0,infinity)` square.  The Doob transform removes the additive ground
energy.  The desired positive curvature/gap is the omitted scalar sign and
is equivalent to D; `CD(0,infinity)` cannot recover it.

## Exact remaining theorem

All successful constructions reduce the missing statement to either of
the equivalent forms

```text
||S F|| <= ||B F||
```

for every compactly supported `F` with the two ruling moments zero, or

```text
lambda_1(T;X) >= 2 A_X + m_0
```

for every finite window, or uniform boundedness of normalized scaling on
a faithful resonant positive completion.

Each statement implies Weil positivity and RH by the already proved B--C
comparison.  None is supplied by the current A--B--C axioms, local Hodge
planes, determinant lines, Euler positivity, Gamma oscillator, or known
completion functors.

## Status

Row D is **not constructed**.  The obstruction is not a missing
calculation or formalization: it is the global primitive sign.  Further
progress requires a new independent geometric/effectivity theorem whose
hypotheses can be verified for the mixed periodic object without invoking
the nuclear form, its spectral divisor, or an equivalent positivity
criterion.

