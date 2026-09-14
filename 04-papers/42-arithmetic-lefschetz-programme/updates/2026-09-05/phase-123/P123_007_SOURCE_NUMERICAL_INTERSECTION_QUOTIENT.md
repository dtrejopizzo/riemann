# P123.007 — source numerical intersection and its radical quotient

## Status

`PROVED-IN-REPOSITORY`, relative to the imported semilocal trace theorem
with its hypotheses checked in P123.004, for:

* a source-defined Hermitian intersection pairing on the compactly
  supported mixed test algebra;
* closed numerical equivalence;
* stability of the numerical radical under convolution and dagger;
* the separated numerical quotient and its nondegenerate pairing;
* existence and nuclearity of the ambient completion.

`OPEN` for identifying this quotient with the numerical realization of the
periodic Deligne/ruling sector and for a Riemann--Roch theorem on the joined
category.

No zero of zeta, no von Mangoldt coefficient and no sign assertion is used
in the construction or in the proofs below.

## 1. The trace-class mixed algebra

Put

```text
D = C_c^infinity(R_+^times)
```

with its usual complete nuclear LF topology, multiplicative convolution

```text
(f star g)(x)=integral f(y)g(y^-1 x) d^times y,        (1.1)
```

and the half-density involution

```text
f^dagger(x)=x^-1 conjugate(f(x^-1)).                  (1.2)
```

Thus `(f star g)^dagger=g^dagger star f^dagger`.  Under the logarithmic
coordinate this is the standard compactly supported smooth convolution
algebra, with the modular weight dictated by the normalization of the
scaling representation.  In the Mellin convention

```text
M(f)(s)=integral f(x)x^s d^times x
```

one has

```text
M(f^dagger)(s)=conjugate(M(f)(1-conjugate(s))).        (1.3)
```

The algebra `D` is the scalar trace-class ray inside the dense
Bruhat--Schwartz core of P123.006.  It is not the whole ambient crossed
product and it does not contain its multiplier identity.

## 2. Source trace, before the explicit formula

For a finite set of places `S` containing infinity, use the semilocal
scaling representation and phase-space cutoff of P123.004/107.239:

```text
T_S(h)=lim_(Lambda -> infinity)
       (Tr(theta(h) R_Lambda)-2h(1)log Lambda).        (2.1)
```

The imported semilocal trace theorem proves existence on `D` and identifies
it with the sum of the local fixed-point distributions

```text
T_S(h)=sum_(v in S) integral' h(u^-1)/|1-u|_v d^*u.   (2.2)
```

For compact support the set of contributing finite places stabilizes.
Denote the stabilized distribution by `T`.  Definition (2.1), rather than
the global explicit formula, is the definition used here.

### Lemma 2.1 — star reality

```text
T(h^dagger)=conjugate(T(h)).                           (2.3)
```

### Proof

It is enough to verify the identity in every local summand of (2.2).
Conjugate the local integral and substitute `u -> u^-1`.  Multiplicative
Haar measure is invariant and

```text
|1-u^-1|_v=|u|_v^-1 |1-u|_v.
```

The extra factor `|u|_v` is exactly the modular factor in (1.2).  The same
change of variables is valid for Tate's finite-part normalization at the
singular point.  Summing and then stabilizing proves (2.3).  This proof uses
only local fixed-point geometry.  QED.

The right side of (2.2) also proves that `T` is a continuous distribution
on each fixed-support Frechet step, hence on the nuclear LF space `D`.

## 3. Intersection and numerical equivalence

Define

```text
I_A(f,g)=T(f star g^dagger).                           (3.1)
```

This is linear in `f`, conjugate-linear in `g`, jointly continuous and
Hermitian.  Indeed, commutativity of multiplicative convolution and (2.3)
give

```text
conjugate(I_A(g,f))
 =T((g star f^dagger)^dagger)
 =T(f star g^dagger).
```

Define the source numerical radical

```text
R_A={f in D : I_A(f,g)=0 for every g in D}.            (3.2)
```

and write `N_A^c=D/R_A`.

### Theorem 3.1 — the radical is a closed dagger ideal

`R_A` is a closed two-sided convolution ideal and
`R_A^dagger=R_A`.

### Proof

It is closed because it is the intersection, over all `g`, of the kernels
of the continuous linear maps `f -> I_A(f,g)`.  If `f in R_A`, then for
arbitrary `a,g in D`,

```text
I_A(a star f,g)
 =T(f star a star g^dagger)
 =I_A(f,a^dagger star g)=0.                           (3.3)
```

Commutativity gives both ideal sides.  Further,

```text
I_A(f^dagger,g)
 =T(f^dagger star g^dagger)
 =conjugate(T(g star f))
 =conjugate(I_A(f,g^dagger))=0.                       (3.4)
```

Thus `f^dagger in R_A`; involutivity gives equality.  QED.

Consequently convolution, dagger and the pairing descend to the Hausdorff
locally convex quotient `N_A^c`.  The descended pairing is nondegenerate by
construction: if a quotient class pairs to zero with every class, any
representative lies in (3.2).

## 4. Completion

Let

```text
N_A^mix = completion(N_A^c).                           (4.1)
```

The quotient topology is Hausdorff and nuclear, because nuclearity is
stable under Hausdorff quotients; its completion is therefore a complete
nuclear locally convex space.  Continuous convolution, dagger and `I_A`
extend uniquely to the completion.  Formula (3.3) remains valid by
density, so the completion is a complete nuclear dagger algebra equipped
with a continuous pairing.

Nondegeneracy is proved on `N_A^c`; it is **not** automatically inherited
by an arbitrary locally convex completion.  Let

```text
R_boundary={x in completion(N_A^c):
            I_A(x,y)=0 for every y in completion(N_A^c)}.             (4.2)
```

This is a closed dagger ideal by the same proof as Theorem 3.1.  The
Hausdorff quotient by `R_boundary` is separated, but its completeness after
quotient is not asserted here.  Thus P123.007 constructs the complete
ambient numerical sector and identifies the exact possible boundary
defect; eliminating that defect, or choosing a proved perfect-pairing
topology, remains part of the A.6 comparison gate.  No Hilbert-space
positivity or reflexivity is asserted.

The external idele-class dilations act on `D` by translation.  Equation
(3.3) shows that every such action preserving `D` preserves `R_A`, hence
acts on `N_A^mix`.  P123.013 proves that these external actions must not be
identified with the internal rational gauge multipliers of P123.006; row B
must lift into the external bimodules before using this conclusion.

## 5. Non-vacuity without arithmetic labels

The pairing is not identically zero.  Already on a single semilocal chart,
the off-identity fixed-point calculation of P123.006 gives, for `q != 1`,

```text
Tr_dist,S(f U_q)
 =|q|_S^(1/2) f(0)/|q-1|_S.                           (5.1)
```

Choose a Bruhat--Schwartz coefficient with `f(0) != 0`.  Then (5.1) is a
nonzero source trace.  No preferred integer, prime tower or weight is used.
Equivalently, (2.2) has a nonzero local fixed-point distribution.  Hence
the trace-class mixed sector and its numerical quotient are non-vacuous.

## 6. What this closes in A.6

This note proves the difficult algebraic part of numerical equivalence:

```text
source trace
   -> Hermitian mixed intersection
   -> closed dagger ideal R_A
   -> nondegenerate Hausdorff nuclear quotient N_A^c
   -> complete nuclear ambient N_A^mix, with boundary radical isolated.
```

It does **not** identify `N_A^mix` with the existing ruling plane.  At
present there are two rigorously constructed pieces,

```text
H_rul = span(F_v,F_h),      matrix [[0,1],[1,0]],
N_A^mix,                    pairing induced by (3.1),
```

and the comparison functor that places both inside one determinant/RR
theory is open.  Their direct sum may be written as a bookkeeping object,
but it is not accepted as the sought geometric join.  This prevents a
formal direct-sum declaration from falsely closing A.6 or A.8.

## 7. Independence audit

The definitions (1.1), (1.2), (2.1), (3.1) and (3.2) use only:

1. the semilocal scaling action;
2. its adjoint/modular normalization;
3. the phase-space cutoff and generic-orbit subtraction;
4. convolution and local fixed-point trace.

The optional later identity of `T` with Weil's global distribution is not
used.  Evaluation at zeta zeros, the coefficients `Lambda(n)`, the
distinguished objects `Gamma_n`, RH and every positivity assertion are all
absent.  The construction therefore satisfies the independence half of
A.10.

## 8. Exact remaining gate

The live arrow is now

```text
(K_S^rapid, N_A^mix, T)
          |
          | OPEN: determinant/cohomology realization Phi_det
          v
(periodic Deligne ruling category, lambda_per)
```

It must transport the diagonal multiplier, dagger and trace, and extend
the ruling determinant to mixed kernels.  Only such a theorem can turn the
source numerical pairing above into the intersection product entering
mixed Riemann--Roch.
