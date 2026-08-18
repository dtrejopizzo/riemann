# 114.a.06 — Category audit of a4-weak: what the theta calculation actually constructs

> **Resolved by 114.a.07.** The category gap isolated here is real in the
> smooth-only formulation but is closed positively in the established category
> of semipositive adelic toric metrics.  The canonical metric on `O(1)` has
> Haar Chern measure, and the toric roof-function height formula derives the
> hyperbolic pairing.  See `114_a_07_TORIC_REALISATION_OF_THE_HAAR_QUADRIC.md`.

```
+--------------------------------------------------------------------------+
| OBJECT       P^1_Z is a genuine regular projective arithmetic surface.   |
| VALID DATA   For every (k,a), Haar integration on |z|=1 gives a genuine  |
|              Euclidean norm on H^0(P^1_Z,O(k)) = Z^{k+1}.                |
| VALID RESULT The theta invariant is exactly                              |
|              (k+1)(a + log theta(e^{2a})); quadratic on (mk,ma).         |
| CATEGORY GAP The construction specifies a norm on global sections, not   |
|              a smooth Hermitian line bundle on all P^1(C).               |
| PAIRING GAP  <(k,a),(k',a')>=ka'+k'a is declared, not derived from an    |
|              arithmetic Chow/intersection product for the stated data.  |
| VERDICT      a4-weak is closed as a gauged lattice-growth model.  Its     |
|              stronger Arakelov-geometric reading is OPEN.                |
+--------------------------------------------------------------------------+
```

## 1. Three levels that must be kept separate

`114_a_02` combines three structures which are individually meaningful but
whose compatibility was not proved.

1. **The scheme.** `X=P^1_Z` is regular, projective and flat over `Spec Z`, of
   relative dimension one.  This is an arithmetic surface in the usual
   scheme-theoretic sense.
2. **Normed section lattices.** For `k>=0`, restriction to the unit circle and
   Haar integration gives

   ```
   ||sum c_j z^j||_2^2 = integral_0^1 |sum c_j e^{2 pi ijt}|^2 dt
                       = sum |c_j|^2.
   ```

   Thus `H^0(X,O(k))` is the standard Euclidean lattice `Z^{k+1}`.  Scaling
   its norm by `e^{-a}` gives a perfectly valid Hermitian lattice and hence a
   theta invariant.
3. **Arithmetic intersection theory.** A smooth Hermitian line bundle in
   classical Arakelov geometry requires pointwise fiber norms over all of
   `X(C)` (with the usual conjugation compatibility); an `L^2` norm is then
   obtained using a volume form on the complex fiber.  A measure supported on
   the equatorial circle supplies neither datum by itself.

The passage from level 2 to level 3 is the missing construction.

## 2. The exact theorem that survives unchanged

Let `Lambda_{k,a}` be `Z^{k+1}` with squared norm

```
||(c_0,...,c_k)||_{k,a}^2 = e^{-2a} sum_j c_j^2.
```

Define its theta dimension by

```
h^0_theta(k,a) = log sum_{c in Z^{k+1}}
                         exp(-pi ||c||_{k,a}^2).
```

### Theorem 2.1 (normed-lattice Riemann--Roch identity)

For all `k>=0` and real `a`,

```
h^0_theta(k,a)
 = (k+1) log theta(e^{-2a})
 = (k+1)(a + log theta(e^{2a})).
```

In particular, for `k>0,a>0`,

```
h^0_theta(mk,ma) = ka m^2 + a m + o(1).
```

*Proof.* The theta series factors into `k+1` copies of the rank-one series.
The second equality is Jacobi's functional equation.  The final formula uses
`theta(e^{2ma})=1+O(exp(-pi e^{2ma}))`. `[]`

This is the exact mathematical content verified by
`114_a_02_the_absolute_quadric.py`.  Calling the polynomial on the right
`(1/2)D.(D-K)` is valid notation after defining the hyperbolic form, but it
does not prove that this form is the Gillet--Soulé intersection of a smooth
Hermitian line bundle.

## 3. Why the distinction matters

The arithmetic Hodge index and arithmetic Riemann--Roch are compatibility
theorems between metrics, arithmetic Chow classes, curvature/Green data and
cohomology.  One cannot invoke them from an arbitrary family of Euclidean
norms on the groups of global sections.

In particular, the following implications in the earlier wording are not yet
available:

```
Haar section norm  =>  canonical Green function,
theta identity     =>  arithmetic RR for the claimed divisor group,
stipulated U-form  =>  geometric arithmetic intersection.
```

The failure is not in the numerical identity; it is a missing functorial
realisation of all the displayed data in one category.

## 4. Corrected meanings of G-1, G-2 and G-3

- **G-1 (absolute-dimension constant)** is closed by `114_a_11`: its coupled
  constant is `1/log 2`.  It is not needed for Theorem 2.1, whose theta
  leading constant is exactly one.
- **G-2 (subleading term for counts)** is closed by `114_a_08`: the `l1`
  count has an unavoidable `-km log m` term.  This does not by itself supply
  a smooth Hermitian line bundle or an arithmetic intersection product.
- **G-3 (comparison with the phase-113 trace space)** is delimited by
  `114_d3_03` Theorem 6.5 and `114_a_13`: additive Lorentzian domination is
  RH-equivalent, while unstructured non-additive domination is automatic and
  vacuous. `114_a_59` further proves that non-additive two-point
  polarization/Kunneth domination is RH-equivalent. `114_a_60` proves the
  exact effectivity branch G3-EFF is RH-equivalent too. Thus meaningful G-3
  is the RH step itself and must not be used to validate the category gap.

There is therefore a new preliminary gate before the old G-3:

> **G-0 (metric/intersection realisation).** Construct smooth or explicitly
> admissible singular Hermitian metrics `||.||_k` on `O(k)` and a volume theory
> on `P^1(C)` whose induced section norms are the Haar norms used above, and
> derive the form `ka'+k'a` from the corresponding arithmetic intersection;
> or prove that exact simultaneous realisation is impossible.

**Updated status:** CLOSED POSITIVELY by `114_a_07`, using the canonical
semipositive toric metric.  Smoothness is replaced by uniform approximability
by smooth semipositive metrics, exactly the admissible hypothesis of the cited
toric intersection theory.

An admissible singular toric metric may be the natural category, but it must
be named and its intersection theory cited/proved.  The circle measure is a
plausible equilibrium/Monge--Ampère measure; plausibility is not the missing
compatibility theorem.

## 5. Updated verdict

The following remains fully established and useful:

> There is a family of integral section lattices living on `P^1_Z`, with rank
> and logarithmic radius both linear along divisor rays, whose theta dimension
> is quadratic with exact leading coefficient `ka`.

This closes the growth obstruction O1 in the **gauged-lattice** sense and
answers the weak question “can quadratic theta cohomology occur over
`Spec Z`?” positively.

It does not yet construct the literal `F_1` square, the I7 kernel pairing, or a
single classical Arakelov divisor theory having every structure asserted in
the original box.  Hence it is not a completed point A by itself.

## 6. Refutation conditions

- **R39.** This audit is wrong if Haar integration on the circle, without any
  additional definition, is already a smooth pointwise Hermitian metric on
  `O(k)` over all `P^1(C)`.
- **R40.** The pairing gap is closed if the form `ka'+k'a` is derived from an
  explicitly specified arithmetic Chow product for the same metrics that
  induce the section norms.
- **R41.** G-0 is closed positively if an admissible singular-metric theorem
  supplies that derivation and its hypotheses are checked for the circle
  measure.
