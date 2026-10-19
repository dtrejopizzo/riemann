# R161_029 — Sign audit of the moving discrepancy: L161.11 is the reverse-Markov gate

## 0. Verdict

`R161_028` proves a genuine operator bridge: the exterior image is the velocity of the Euler--Maclaurin polar
layer. It does not, by itself, supply the sign requested in L161.11. The most canonical quadratic discrepancy has
an indefinite continuous derivative and indefinite jumps. After Tate centering, obtaining the opposite sign is
exactly the reverse physical typing left open in `R161_016`.

Thus the polar-image insight localizes the terminal theorem but does not prove it. Any claim that monotonicity of
the ordinary discrepancy norm closes D would be false.

## 1. Canonical moving discrepancy

Use the notation of `R161_028`:

```
Z_a=S_a-C_a,                                                     (1.1)
```

where `S_a` is the integer comb up to `exp(a)` and `C_a` is its continuum polar term. For a fixed vector `f` in the
common core define

```
N_f(a)=||Z_af||^2.                                               (1.2)
```

This is the most direct positive quantity built from the moving Poisson defect before inserting the Chebyshev
operator.

## 2. Continuous derivative between births

On an interval containing no `log n`, `S_a` is constant and

```
partial_a Z_a=-exp(a/2)tau_a.                                   (2.1)
```

Therefore

```
boxed: N_f'(a)
 =-2exp(a/2)Re<Z_af,tau_af>.                                    (2.2)
```

The right side has no fixed sign. It is a cross-correlation, not a squared norm. The polar-image identity tells us
where the second vector lives; it does not orient its phase relative to `Z_af`.

## 3. Exact jump at an integer birth

At `a_n=log n`, write `Z_-` and `Z_+` for the two one-sided values. Since

```
Z_+=Z_-+v_n,
v_n=n^(-1/2)tau_(log n),                                        (3.1)
```

one has

```
boxed: N_f(a_n+)-N_f(a_n-)
 =2n^(-1/2)Re<Z_-f,tau_(log n)f>+n^(-1)||f||^2.                 (3.2)
```

The final term is positive, but the cross term is indefinite and can dominate. The oscillating raw energies in
`161_02_poisson_defect_probe.py` are a numerical falsifier for any universal monotonicity claim.

Multiplying or summing the jumps with positive Chebyshev coefficients does not remove this issue: the terminal
hyperbola jump supplies orientation, but its pairing with the existing discrepancy is still the cross term whose
sign is sought.

## 4. Primitive radical pairing

Let `Pi=Pi_T`, `P=P_T`, and define

```
H_a=Pi P Z_a*Z_a P Pi>=0.                                       (4.1)
```

If `F` is a first-contact radical, then `H_aF` is a primitive test and hence

```
a_T(F,H_aF)=0                                                    (4.2)
```

for every `a`. Differentiating (4.2), where legitimate, is still radicality evaluated on another primitive test.
It does not set (2.2) or (3.2) to zero separately. Expanding the projection introduces exactly the moving Tate and
exterior boundary terms isolated in phase 121.

This is the moving-discrepancy version of the collapse proved in `R161_023`.

## 5. Identification with the previous terminal gate

The direct causal/Markov construction of `R161_016` gives the decreasing-norm direction. In the present notation,
it controls the sign obtained from the ordinary lattice-minus-continuum discrepancy and its positive innovations.
Closure requires the reverse port typing, which would turn the cross terms in (2.2)--(3.2) into a same-sign defect.

Consequently:

```
L161.11 (same-sign moving discrepancy)
   = reverse Tate-centred Markov pullback of R161_016
```

at the level of the remaining sign theorem. `R161_028` supplies a new exact coordinate for its Gamma component,
but not an independent proof of the reverse arrow.

## 6. Exact remaining statement

The terminal theorem remains:

> Construct before scalar synthesis a source-defined two-orientation quadratic form whose expansion replaces the
> indefinite cross terms (2.2)--(3.2) by
>
> ```
> 2D_(T,delta)^Gamma(F)+D_a^Poisson(F),
> D_a^Poisson(F)>=0,                                             (6.1)
> ```
>
> and prove that the form vanishes on a first-contact state.

Neither the norm `N_f`, the primitive family `H_a`, nor first-contact shape minimality proves (6.1).

## 7. Status

- exact continuous derivative of the moving discrepancy norm: **PROVED / INDEFINITE**;
- exact birth jump: **PROVED / INDEFINITE**;
- ordinary discrepancy monotonicity: **FALSE**;
- primitive radical differentiation as new information: **REJECTED AS TAUTOLOGICAL**;
- equivalence of the remaining sign with the reverse-Markov gate: **IDENTIFIED**;
- reverse source-defined two-orientation square: **OPEN / TERMINAL**;
- row D: **OPEN**.
