# Common architecture of the failed global-square mechanisms

## 1. The common normal form

After all local contacts have been assembled and the D.247 conservation law
has eliminated the redundant ports, every phase-120 construction reaches
the same source-defined difference

```
q_T(F)=-B_nuc,T(F,F)=||X_TF||^2-||Y_TF||^2,         (1.1)
```

on the two-Tate primitive source `P_T`.  The names of the two banks change,
but their content does not:

```
X_T = Gamma bulk + free/place input + positive tangent port,
Y_T = polar load + coherent degree + opposite tangent port. (1.2)
```

The zero-residual Green theorem gives a second exact coordinate

```
q_T(F)=<K_TE_TF,QK_TE_TF>-<E_TF,QE_TF>.             (1.3)
```

Equations (1.1)--(1.3) preserve the complete arithmetic information.  They
do not have a sign.

## 2. Positive-lift theorem

### Theorem 2.1

For bounded source maps `X:H->K_X` and `Y:H->K_Y`, the following are
equivalent:

1. `||XF||^2-||YF||^2>=0` for every `F in H`;
2. there is a contraction `Theta:closure(Ran X)->K_Y` satisfying
   `Y=Theta X`;
3. there is a Hilbert space `K_D` and an operator `D:H->K_D` satisfying
   `D^*D=X^*X-Y^*Y`.

The equivalence of 1 and 2 is Douglas factorization, and 2 gives 3 through
`D=(1-Theta^*Theta)^(1/2)X`.  Statement 3 gives 1 immediately.

Consequently every **linear positive lift** of the already identified form
is in the same logical equivalence class.  Changing the ambient category or
the name of `Theta` does not create a new sign theorem.

## 3. Dictionary of the repeated terminal morphism

| language | positive object constructed for free | terminal morphism which remained |
|---|---|---|
| Hilbert/Schur | two positive feature banks | contractive factor `Y=Theta X` |
| scattering/de Branges | bilateral unitary Green multiplier | one-sided innerness/intertwining |
| causal systems/KYP | passive local Gamma and prime cells | global storage transmission with the oriented sign |
| Hodge/Rosati | local rank-one contact metrics | primitive global polarization |
| Higgs/quiver | moment-map ports and coordinate stability | stability of every mixed source line |
| homological/Morse/bar | exact differentials and local cancellations | vanishing/injectivity on critical mixed homology |
| determinant geometry | exact Green connection | positive curvature with the same connection |
| Fock/CAR | positive free vacuum | bounded arithmetic descent/reflection on the commutative quotient |
| modular entropy | positive local Hessians | global modular inclusion/mixed tangent |
| cofinal operator theory | positive finite shifts or quotient forms | persistence of the unshifted sign in the limit |

In each row the positive object is genuine.  The final morphism is not a
technical afterthought: after the exact comparisons it is Theorem 2.1 in
that language.

## 4. What all candidates were trying to obtain

They were all seeking a **free local-to-global positivity transport**:

```
positive rank-one data at each place
 + positive quarter-Gamma reservoir
 + functional equation / Real involution
 + two Tate boundary conditions
          |
          v
positive form on every mixed primitive test.          (4.1)
```

The hoped-for principle was that coherence, causality, duality, stability,
curvature or entropy would make the vertical arrow in (4.1) automatic.
The audits show that it is not automatic.

The local inputs control the diagonal/placewise directions.  Row (d) is a
statement about arbitrary **mixed** source lines.  The exact Green coupling
between those lines is global and signed.  No local positive package orders
it.

## 5. The locality--phase--sign trilemma

Every failed construction chooses two of the following three properties:

1. **Local positivity:** each place or reservoir is a positive Hilbert
   object.
2. **Exact global phase:** cross-place Green interference and all `p^j`
   coefficients are retained.
3. **Positive primitive descent:** the object descends contractively to the
   common two-Tate source.

The observed alternatives are:

* orthogonalize places: obtain 1 and 3, lose 2;
* use the common causal/scattering carrier: obtain 1 and 2, but the descent
  is signed;
* demand a positive quotient, stable object, inner transfer, modular
  inclusion or positive trace: obtain 2 and 3 only by assuming the terminal
  morphism of Theorem 2.1.

This is why the residue repeatedly changed names while its mathematical
type did not change.

## 6. Exact identities conserve the missing inertia

The phase constructed many useful equalities:

* Frobenius and Gamma state equations;
* D.247 boundary conservation;
* Poisson resummation of every prime tower;
* quarter-determinant scattering;
* zero-residual Green formula;
* Bergman--Hardy filling;
* local modular-Hessian identities.

An exact invertible change of coordinates, a unitary dilation or a
conservation law cannot remove a negative direction; it transports the
inertia.  A compression or quotient can remove one, but proving that the
physical primitive compression removes all negative directions is exactly
the desired sign theorem.  Thus further equalities of the same kind can
simplify the operator but cannot by themselves finish row (d).

## 7. The repeated information loss

There are four recurrent ways a candidate became positive:

1. **Diagonalization:** mixed prime phases were discarded.
2. **Averaging/symmetrization:** distinct prime words collapsed and produced
   factorial or rank defects.
3. **Projection:** the two Tate constraints were enforced, but the sign of
   the resulting compression was assumed.
4. **Positive completion:** a metric, state, curvature or harmonic object
   was chosen whose comparison with the physical form was the missing
   intertwining.

Conversely, every construction which retained all the information -- the
bilateral Green unitary, the supertrace, the Krein/CAR covariance, the
relative modular Hamiltonian -- retained the sign difference as well.

## 8. What the failures say about a successor

A successor cannot merely construct another positive ambient object and
ask it to descend.  The whole linear-positive-lift family is covered by
Theorem 2.1.

The structurally different problem is the **negative-witness problem**:

> Assume a mixed primitive `F` with `q_T(F)<0`.  Derive, from an exact
> Euler-specific rigidity law, an object forbidden by rows (a)--(c), unique
> factorization, or the functional equation.

This reverses the quantifiers.  It does not try to manufacture a norm for
all tests.  It tries to prove that a hypothetical negative state cannot be
compatible with the exact arithmetic dynamics.

Such a rigidity law must satisfy all of the following:

* act on mixed source lines, not placewise coefficients;
* retain the exact prime phases and the coherent degree port;
* preserve both Tate conditions without projection by the target form;
* fail for Davenport--Heilbronn and the shifted rank-two pair for a reason
  visible before spectral comparison;
* not be a tensor amplification, recurrence argument, commutator estimate
  or positive-lift construction already covered by the corpus.

No such rigidity law is constructed here.  The point of the classification
is that it changes the search space: the failed programme was looking for a
canonical **certificate of positivity**; a genuinely different programme
must look for an arithmetic **impossibility of negativity**.

## 9. Verdict

What all failed cases shared was not merely positivity language.  They all
sought the same vertical arrow (4.1), and every successful local
construction stopped at the same mixed descent.  Their common hidden hope
was that local positive provenance plus exact gluing would force the global
sign.  The phase proves that provenance and gluing determine the form, but
do not polarize it.

The next conceptual move, if the programme continues, should therefore not
be another square.  It should be a source-side rigidity theorem for a
hypothetical negative mixed line.
