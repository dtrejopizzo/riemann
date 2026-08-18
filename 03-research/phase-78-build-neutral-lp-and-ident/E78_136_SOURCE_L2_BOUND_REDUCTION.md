# E78.136 - `SAFE-Y-BOUND` reduces to a single `l2` source bound

**Scope:** front B only, current live derivative-specific clause `SAFE-Y-BOUND`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the three pieces
of `SAFE-Y-BOUND` are not independent quantities. On every safe compact they
are uniformly controlled by one and the same source norm `||y_b||_2`, with
constants depending only on the fixed mesh geometry. So the live derivative
burden shrinks from three transform clauses to a single cofinal `l2` bound on
`y_b`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       and no ambient inverse norm before paired reduction.
P76.061: respected. The reduction acts before any attempt to invert the full
         logarithmic quotient and keeps the source paired with its exact kernel.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Starting point

E78.104 isolated the remaining derivative-specific source clause:

```text
SAFE-Y-BOUND(L,K,eta):
  |Y_b(i sigma;mu)| + |Y_b^bd(mu)| + |Y_b'(i sigma;mu)|
  <= N_{L,K,eta}                                          (Y-1)
```

uniformly for `sigma in K`, `|mu|<=eta`, and all sufficiently large `N`.

Here

```text
Y_b(z;mu)   = sum_n y_b(n;mu)/(z-d_n),                    (Y-2)
Y_b^bd(mu)  = sum_n y_b(n;mu)/(d_n-d_b),                 (Y-3)
Y_b'(z;mu)  = -sum_n y_b(n;mu)/(z-d_n)^2.                (Y-4)
```

The question is whether `(Y-1)` really contains three new burdens, or only one.

## 2. Uniform mesh-kernel bounds

Fix `L`, a safe compact `K subset (0,infinity)`, and let

```text
sigma_- := inf K > 0,   sigma_+ := sup K.                 (Y-5)
```

The interior mesh is

```text
d_n = 2 pi n / L.                                         (Y-6)
```

For every finite section, define the coefficient vectors

```text
k_sigma(n)    := 1/(i sigma-d_n),
k_sigma'(n)   := -1/(i sigma-d_n)^2,
k_bd(n)       := 1/(d_n-d_b).                             (Y-7)
```

Since `|i sigma-d_n|^2 = sigma^2 + d_n^2`,

```text
||k_sigma||_2^2
 = sum_n 1/(sigma^2+d_n^2)
 <= sum_{m in Z} 1/(sigma_-^2+(2 pi m/L)^2)
 =: C_Y(L,K)^2 < infinity,                               (Y-8)
```

uniformly in the section depth `N`.

Likewise,

```text
||k_sigma'||_2^2
 = sum_n 1/(sigma^2+d_n^2)^2
 <= sum_{m in Z} 1/(sigma_-^2+(2 pi m/L)^2)^2
 =: C_{Y'}(L,K)^2 < infinity.                            (Y-9)
```

For the boundary coefficients, if the section boundary index is `b=N`, then

```text
|d_n-d_b| = (2 pi / L) |n-b|,                            (Y-10)
```

so

```text
||k_bd||_2^2
 = (L/2 pi)^2 sum_{n inner} 1/(n-b)^2
 <= (L/2 pi)^2 sum_{m>=1} 1/m^2
 = L^2/24
 =: C_bd(L)^2.                                           (Y-11)
```

Again this is uniform in the section depth.

## 3. Reduction to one source norm

Apply Cauchy-Schwarz to `(Y-2)`--`(Y-4)`:

```text
|Y_b(i sigma;mu)|
 <= ||k_sigma||_2 ||y_b(mu)||_2
 <= C_Y(L,K) ||y_b(mu)||_2,                              (Y-12)

|Y_b'(i sigma;mu)|
 <= ||k_sigma'||_2 ||y_b(mu)||_2
 <= C_{Y'}(L,K) ||y_b(mu)||_2,                           (Y-13)

|Y_b^bd(mu)|
 <= ||k_bd||_2 ||y_b(mu)||_2
 <= C_bd(L) ||y_b(mu)||_2.                               (Y-14)
```

Therefore, if

```text
SOURCE-L2-BOUND(L,eta):
  there exist B_{L,eta}, N_0 such that
  ||y_b(mu)||_2 <= B_{L,eta}
  for all N>=N_0 and |mu|<=eta,                          (Y-15)
```

then `(Y-12)`--`(Y-14)` imply

```text
SAFE-Y-BOUND(L,K,eta)                                    (Y-16)
```

with

```text
N_{L,K,eta}
 = (C_Y(L,K) + C_{Y'}(L,K) + C_bd(L)) B_{L,eta}.         (Y-17)
```

So:

```text
SOURCE-L2-BOUND => SAFE-Y-BOUND.                         (Y-18)
```

## 4. Why this is a genuine reduction

The predecessor clause carried three transform quantities:

```text
Y_b, Y_b^bd, Y_b'.                                        (Y-19)
```

The new clause asks only for one vector norm:

```text
||y_b||_2.                                                (Y-20)
```

That is strictly less information than controlling all three transforms
separately. It removes the safe-row parameter from the live object and keeps
only one sectionwise source norm.

So this is a genuine reduction, not a rephrasing.

## 5. Probe

Companion files:

```text
E78_136_source_l2_bound_probe.py
E78_136_source_l2_bound_results.json
```

Using the exact burden data already recorded in E78.104, the probe evaluates the ratios

```text
max_sigma |Y_b(i sigma)| / ||y_b||_2,
max_sigma |Y_b'(i sigma)| / ||y_b||_2,
                                                          (Y-21)
```

and compares them to the uniform constants from `(Y-8)`--`(Y-9)`.  It also
records the exact boundary-kernel constant `C_bd(L)` from `(Y-11)`.

Across the audited sections `N=6,8,10,12` for both zeta and planted builds,
the `Y` and `Y'` margins stay strictly positive, confirming numerically that the
derived kernel bounds dominate the observed transforms with comfortable slack.
The boundary term is covered directly by the exact coefficient-vector estimate
`(Y-14)` and its explicit constant `(Y-11)`, so it does not require a separate
heavy recomputation in the audit.

The probe is only an audit; the proof of `(Y-12)`--`(Y-14)` is the actual
reduction.

## 6. Consequence

Combining E78.135 with `(Y-18)`, the genuinely new derivative-specific burden
below `DMU-COUPLED-GENERATOR` now reduces to:

```text
SOURCE-L2-BOUND(L,eta).                                   (Y-22)
```

Everything else is either inherited from the fixed-`L` two-generator front or
follows from the exact Cauchy kernel geometry.

## 7. Status

```text
candidate closure - pending review

proved:
  uniform mesh-kernel l2 bounds imply SOURCE-L2-BOUND => SAFE-Y-BOUND;

reduced:
  the live derivative-specific clause from the triple transform
  (Y_b, Y_b^bd, Y_b') to the single cofinal source norm ||y_b||_2;

next:
  attack SOURCE-L2-BOUND directly from the inhomogeneous equation for y_b, or
  reduce that norm further by an exact cofinal implication.
```
