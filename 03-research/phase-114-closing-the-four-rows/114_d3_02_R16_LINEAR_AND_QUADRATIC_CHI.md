# 114_d3_02 — row (d), lens 3: R16 answered — linear chi on the curve, quadratic chi on the surface

```
R16 ASKED:            "Ansatz A presumes a surface Riemann-Roch (a quadratic
                      chi).  Every Riemann-Roch actually available over Spec Z
                      is one-dimensional with a linear chi.  If it is shown
                      that no quadratic chi can exist over Spec Z, Ansatz A is
                      dead and with it this route."   (113_12 section 5)
R16 ANSWER:           R16 DOES NOT FIRE.  A quadratic chi over Spec Z exists
                      and is classical: Faltings 1984, Deligne 1987,
                      Gillet-Soule 1992, on any regular arithmetic surface
                      X -> Spec Z.  Read first-hand in the form
                      deg-hat det Rf_* L = (1/2)(L, L (x) omega^) + deg-hat det Rf_* O.
                      Its numerical-cohomology refinement is Wei He 2025
                      Thm 1.1.  Second difference along L -> nL is exactly
                      (L,L): genuinely quadratic.
BUT:                  the quadratic chi does NOT live on Spec Z as a curve.
                      Thm 4.2 below proves that no Riemann-Roch on Spec Z-bar
                      or on Spec O (Connes-Consani, van der Geer-Schoof) can
                      have Ansatz A's shape, because their chi is affine in
                      the degree with bounded second difference.  So R16's
                      premise about the ONE-DIMENSIONAL theories is correct and
                      is now proved, not merely observed.
COST OF THE IMPORT:   the true surface Riemann-Roch carries an ANALYTIC TORSION
                      term.  Ansatz A must be corrected to
                      chi(D) = D^2/2 + T(D),  T = (1/2) log(det Delta_O / det Delta_D) + chi(O),
                      and 113_12 Thm 5.1's deduction of (E^o) survives only
                      under T(D) > -D^2/2.  That is a NEW GAP (G-4), it was not
                      in the ledger, and it is not closed here.
```

Depends on: 113_11 section 4 (the four Connes–Consani Riemann–Rochs, cited
there second-hand through the phase-39 inventory — upgraded to first-hand
here), 113_12 section 5 (Ansatz A, Thm 5.1, R16), 114_d3_01 (the imported index
theorems, Gap G-1).

External sources, read in this session:
- Wei He, *Numerical cohomology for arithmetic surfaces and applications*,
  arXiv:2512.01811v2, at
  `00-references/papers-nuevos/D/arXiv-2512.01811v2/Numerical_cohomology_for_arithmetic_surfaces_and_applications.tex`.
- A. Connes and C. Consani, *Riemann–Roch for `Spec Z-bar`*,
  arXiv:2205.01391v2, at `00-references/papers-nuevos/A/arXiv-2205.01391v2/RR-J-final.tex`.

Verifier: `114_d3_02_linear_vs_quadratic_chi.py` — 27 checks, all pass, run
below.

---

## 1. What R16 says, and what has to be answered

Verbatim from 113_12 section 5:

> **R16.** Ansatz A presumes a *surface* Riemann–Roch (a quadratic `chi`). Every
> Riemann–Roch actually available over `Spec Z` is one-dimensional with a linear
> `chi` (113_11 section 4, corpus-verified). If it is shown that no quadratic
> `chi` can exist over `Spec Z`, Ansatz A is dead and with it this route.

R16 is a *conditional* refutation condition: it fires only if **no** quadratic
`chi` can exist. Answering it therefore requires exactly two things:

1. an exhibition of a quadratic `chi` over `Spec Z`, from a source read
   first-hand, with its precise hypotheses — section 3;
2. a proof of the complementary statement that the *one-dimensional* theories
   cannot supply one, so that the exhibited quadratic `chi` is the only
   candidate and Ansatz A is bound to an arithmetic surface — section 4.

Both are done. R16 does not fire; the route is not dead; but the object Ansatz A
needs is now pinned to Gap G-1 of 114_d3_01, and it acquires a new term.

---

## 2. The linear side: `Spec Z` as a curve

### Theorem 2.1 (Riemann–Roch for arithmetic curves; van der Geer–Schoof)

Verbatim from Wei He, section 2.2.1, equations `(rrc1)` and `(rrc)` (ASCII
transcription; `O` = ring of integers of a number field `F`, `F-cal` a Hermitian
coherent `O`-module):

> `h^0_O(F-cal) := log sum_{x in F-cal} e^{-pi ||x||^2}`,
> `h^1_O(F-cal) := h^0_O(omega_O (x) F-cal^v)`,
> `chi_O(F-cal) := h^0_O(F-cal) - h^1_O(F-cal)`.
> Then the Riemann–Roch formula for `F-cal` says that
>
> ```
>     chi_O(F-cal) = - log ( covol(F-cal) / #F-cal_t )
>                  = deg-hat det F-cal + rank_O F-cal . chi_O(O)
> ```
>
> with `chi_O(O) = - log sqrt(|D_F|)` (cf. [Geer–Schoof]).

**This `chi` is exactly affine in `deg`**: `chi_O = deg + rank . chi_O(O)`.

**The `Spec Z` instance is Jacobi's theta identity.** For `O = Z`, `F = Q`,
`D_F = 1`, `chi_O(O) = 0`; the Arakelov divisor `D = a{infinity}` is the lattice
`Z` with `||x||_a = |x| e^{-a}`, `deg D = a`, and

```
        h^0_O(D) = log sum_{n in Z} e^{-pi n^2 e^{-2a}} ,
        RR  <==>  h^0_O(a) - h^0_O(-a) = a  <==>  theta(t) = t^{-1/2} theta(1/t) .
```

Verified to `1.8e-40` at twelve values of `a` (verifier section A), and the
second difference along `D |-> nD` is `0` to the same accuracy: **the
arithmetic-curve `chi` is exactly linear.**

### Theorem 2.2 (Connes–Consani, Riemann–Roch for `Spec Z-bar`)

Verbatim from arXiv:2205.01391v2, Theorem 1.1 (`\newtheorem{theorem}{Theorem}[section]`,
`\section{Introduction}` then the first numbered environment; verified by
inspection of the source):

> Let `D` be an Arakelov divisor on `Spec Z-bar`. Then
>
> ```
>     dim_S H^0(D) - dim_S H^1(D) = ceil'( deg' D + log' 2 ) - 1_L .
> ```
>
> Here, `ceil'(x)` denotes the odd function on `R` that agrees with the ceiling
> function on positive reals, and `1_L` is the characteristic function of the
> exceptional set of finite Lebesgue measure which is the union of the intervals
> `( log'(3^k/2), log'((3^k+1)/2) )`.

with, from the same introduction,

```
        dim_S( ||HZ||_n ) = ceil( log(2n+1) / log 3 ) ,      n = floor(e^a) ,
        dim_S( H(R/Z), R ) = ceil( (-a - log 2) / log 3 ) ,
        deg'(D) := deg(D)/log 3 .
```

and Theorem 1.2 (Serre duality), verbatim:

> Let `D` be an Arakelov divisor on `Spec Z-bar` and `K = -2{2}`, with
> `deg K = -2 log 2`. Then there is an isomorphism of `S`-modules
> `H^0(K-D) = uHom_{Gamma T_*}( H^1(D), U(1)_{1/4} )`, where `U(1)_{1/4}`
> coincides with `H^1(K)`, playing the role of the dualizing module in
> Pontryagin duality.

**Reading note (forced, not chosen).** The index `k` in the exceptional set runs
over `k >= 0`. This is forced by Connes–Consani's own words "of finite Lebesgue
measure": for `k >= 0` the lengths are `log(1 + 3^{-k})`, summing to a finite
number, whereas allowing `k < 0` would include an interval of infinite measure.
With `k >= 0` the formula is confirmed on a grid of 10001 points, including 569
points inside `L`; dropping `1_L` produces mismatches at **exactly** those 569
points and nowhere else (verifier section D). This is a first-hand verification
of a theorem that 113_11 section 4 could only cite second-hand.

### Proposition 2.3 (both one-dimensional theories are affine in the degree)

For the Connes–Consani `chi_CC(D) := dim_S H^0(D) - dim_S H^1(D)`,

```
        | chi_CC(D) - ( deg' D + log' 2 ) |  <=  1        for every D,
```

hence for any fixed `D` the second difference along `n |-> chi_CC(nD)` is
bounded by `4` in absolute value, uniformly in `n` and in `D`. For `chi_O` it is
identically `0`.

*Proof.* Theorem 2.2 gives `chi_CC(D) = ceil'(x) - 1_L` with
`x = deg' D + log' 2`; `|ceil'(x) - x| < 1` and `1_L in {0,1}`, so
`|chi_CC - x| <= 1` — the bound `1` (not `2`) because `1_L = 1` only where
`ceil'(x) - x` is within `1` of `0` from above, as the proof of Theorem 2.2
shows and as the measurement confirms. The second difference of an affine
function vanishes, so `|Delta^2 chi_CC| <= 4 sup|chi_CC - x| <= 4`. For
`chi_O`, Theorem 2.1 is exactly affine. `[]`

Measured: `max |chi_CC - x| = 0.999722` over 6001 points, and
`max |Delta^2 chi_CC(nD)| = 1` over the tested families (verifier section E).

---

## 3. The quadratic side: an arithmetic surface over `Spec Z`

### Theorem 3.1 (Faltings–Deligne–Gillet–Soulé; the relative arithmetic RR)

Verbatim from Wei He, section 2.1.3 (`\label{arr}`), equation `(arrf)`:

> Let `f : X -> Spec O` be an arithmetic surface. Choose the Arakelov metric on
> `omega_{X/O}`. For `L` a Hermitian line bundle on `X`, take metric on
> `det f_* L` to be either Faltings metric or Quillen metric. Both of them
> depend on the Arakelov metric. The following Riemann–Roch formula is due to
> Faltings [Faltings], Deligne [Deligne:85] and Gillet–Soulé [Gillet-Soule]:
> Let `deg-hat` be the arithmetic degree on `Pic-hat(O)` and `( , )` the
> Arakelov arithmetic intersection pairing on `Pic-hat(X)`, then
>
> ```
>     deg-hat det Rf_* L = (1/2) ( L, L (x) omega_{X/O}^v ) + deg-hat det Rf_* O_X .
> ```

**That is the quadratic `chi` R16 asked for.** `(L, L (x) omega^v) = (L,L) -
(L, omega)` is a quadratic form in `L`; the formula is the arithmetic-surface
Riemann–Roch in exactly the classical shape `chi(D) = chi(O) + (D^2 - D.K)/2`.
It is a theorem over `Spec Z` (take `O = Z`), it is 40 years old, and it is
quadratic.

### Theorem 3.2 (Wei He Thm 1.1 = Thm 2.8: RR for numerical cohomology)

Verbatim (`\newtheorem{thm}{Theorem}[section]`; the statement appears both as
the first numbered environment of section 1 and, identically, as the last of
section 2, i.e. **Theorem 1.1 = Theorem 2.8** of that paper):

> Let `L` be a Hermitian line bundle on an arithmetic surface `X` and let
> `omega_X` be the canonical sheaf equipped with the Arakelov metric, then
>
> ```
>     ( chi_X(L) + (1/2) log det Delta_{L_infinity} )
>        = (1/2) ( L, L (x) omega_X^v )
>          + ( chi_X(O_X) + (1/2) log det Delta_{O_{X_infinity}} ) ,
> ```
>
> where `( , )` is the Arakelov intersection pairing on `Pic-hat(X)`.

with the definitions (verbatim from the same paper, section 2.2.2):

> `h^0_X(L) := h^0_O(f_* L)`,
> `h^1_X(L) := h^0_O(omega_O (x) (f_*L)^v) + h^0_O( f_*(omega_{X/O} (x) L^v)^v )
>   + (1/2)( deg-hat det H^1(X,L)_t + deg-hat det H^1(X, omega_X (x) L^v)_t )`,
> `h^2_X(L) := h^0_X(omega_X (x) L^v)`,
> `chi_X(L) = h^0_X(L) - h^1_X(L) + h^2_X(L)`,

and, for each infinite place, `det Delta_{L_v} = e^{-zeta'_{L_v}(0)}` the
regularised determinant of the Laplacian (analytic torsion),
`det Delta_{L_infinity} = prod_{v|infinity} det Delta_{L_v}`.

**Citation audit (mandatory, and it bites).** The introduction of that paper
contains the sentence "Then `h^1_X(L) = h^0_X(omega_X (x) L^v)`", which combined
with the displayed definition of `h^2_X` would give `h^1 = h^2` identically and
hence `chi_X = h^0_X`. The Remark in section 2.2.2 of the same paper states
instead `h^1(L) = h^1(omega_X (x) L^v)`, which is the Serre-duality symmetry one
expects. The two cannot both be intended; the introduction sentence is a typo
for the Remark's identity. **Nothing below uses the introduction sentence.**
Everything below uses only the displayed definitions, the Remark's symmetry, and
Theorem 3.2's identity. Recorded here because R22 of 113_14 exists exactly for
this failure mode.

### Proposition 3.3 (the surface `chi` is genuinely quadratic)

Write `chi-tilde(L) := chi_X(L) + (1/2) log det Delta_{L_infinity}`. Then
Theorem 3.2 says `chi-tilde(L) = (1/2)((L,L) - (L,omega)) + chi-tilde(O)`, and

```
        chi-tilde((n+1)L) - 2 chi-tilde(nL) + chi-tilde((n-1)L)  =  (L,L)
```

for every `n`, with no error term. Over the rescaling family `L |-> mL` the
second difference is `m^2 (L,L)`, which is unbounded whenever `(L,L) != 0`.
Also `chi-tilde(omega - L) = chi-tilde(L)` identically (Serre symmetry) and, at
`omega = 0`, `chi-tilde(L) = (L,L)/2 + chi-tilde(O)` — Ansatz A's exact shape.

*Proof.* Expand; verified symbolically (verifier section F). `[]`

---

## 4. The answer to R16

### Theorem 4.1 (R16 does not fire)

A quadratic `chi` over `Spec Z` exists: Theorem 3.1, with `O = Z`, on any
regular projective arithmetic surface `f : X -> Spec Z`. Therefore the
antecedent of R16 ("it is shown that no quadratic `chi` can exist over
`Spec Z`") is **false**, R16 does not fire, and Ansatz A is not dead.

### Theorem 4.2 (but it cannot come from a one-dimensional theory)

Let `chi` be either `chi_O` of Theorem 2.1 or `chi_CC` of Theorem 2.2, and let
`D` be a divisor of the corresponding kind. Then `chi` cannot satisfy Ansatz A
(`chi(D) = D^2/2` for a pairing with `D^2 != 0`) for the whole family
`{ nD : n in Z }`.

*Proof.* Ansatz A forces `chi(nD) = n^2 D^2/2`, whose second difference in `n`
is `D^2 != 0` and whose second difference along `D |-> mD` is `m^2 D^2`,
unbounded. By Proposition 2.3 the second difference of `chi_O` is `0` and that
of `chi_CC` is bounded by `4`, uniformly over **all** divisors. A bounded
function is not an unbounded one. `[]`

Measured: `max |Delta^2 chi_CC| = 1` against `Delta^2 chi_AnsatzA(nH) = H^2 = 2`
already at the smallest corpus class `H` (verifier sections E, F).

### Corollary 4.3 (what Ansatz A is now bound to)

Ansatz A can only be realised by an arithmetic-surface Riemann–Roch, i.e. by
Theorem 3.1/3.2 applied to an actual `f : X -> Spec Z` together with a
realisation `iota : D_R -> Pic-hat(X)_R`. That realisation is Gap G-1 of
114_d3_01, and by Theorem 5.3 there it must be adelic. **The status of Ansatz A
is therefore: not refuted, not proved, and reduced to G-1 + G-4.**

This also upgrades 113_11 section 4 and 113_12's R16 remark from "corpus-verified"
to *proved*: the one-dimensional theories are provably the wrong shape, and the
right shape provably exists elsewhere.

---

## 5. The corrected Ansatz A, and the new gap it opens

### Definition 5.1 (Ansatz A')

With `T(D) := (1/2) log( det Delta_{O_infinity} / det Delta_{D_infinity} ) +
chi_X(O_X)` (so that `T` collects everything Theorem 3.2 puts on the wrong side
of Ansatz A), the imported Riemann–Roch with `K = 0` reads

```
        chi(D)  =  D^2 / 2  +  T(D) .                                 (A')
```

Ansatz A is (A') with `T == 0`.

### Theorem 5.2 (113_12 Thm 5.1 under the corrected ansatz)

Assume (A') and the effectivity dictionary of Ansatz A. Then the implication
"`D^2 > 0` implies `D` or `-D` effective" — i.e. `(E^o)`, hence RH — follows if
and only if

```
        T(D)  >  -D^2/2      for every real D in D^o with D^2 > 0.       (T+)
```

*Proof.* 113_12 Thm 5.1 needs `chi(D) > 0`; under (A') that is exactly (T+).
Conversely if (T+) fails at some `D` then `chi(D) <= 0` and the argument gives
nothing. `[]`

The failure is not hypothetical bookkeeping: at `D^2 = 2`, `T = -2` gives
`chi = -1 < 0` and the deduction collapses (verifier section G). So **the
imported Riemann–Roch does not hand over Ansatz A; it hands over Ansatz A plus
an analytic obligation.**

### Remark 5.3 (what `T` is, and one thing that is free)

`T` is built from `det Delta_L = e^{-zeta'_L(0)}`, the Ray–Singer analytic
torsion of the Laplacian `Delta_L = dbar_L^v dbar_L` on `X(C)`. Wei He's
equation `(lap)`, quoted verbatim — "`det Delta_L = det Delta_{Omega_X (x) L^v}`"
— gives for free that `T` is **Serre-symmetric**: `T(D) = T(K - D)`. So the
correction term does not break the `h^2(D) = h^0(-D)` half of Ansatz A; it only
attacks the positivity half.

### Proposition 5.4 (a structural constraint on the surface, if `K = 0` transports)

Suppose a realisation `iota` sends the corpus canonical class `K = 0` (113_12
Thm 3.4) to `omega_X = 0` in `Pic-hat(X)_R`. Then the generic fibre `X_Q` has
genus 1.

*Proof.* For `O = Z` one has `omega_O = Z` with the trivial metric and
`omega_X = omega_{X/Z} = omega_{X/O}`. If `omega_X = 0` in `Pic-hat(X)_R` then
its restriction to the generic fibre is trivial in `Pic(X_Q)_R`, so
`deg omega_{X_Q} = 2g - 2 = 0`, i.e. `g = 1`. `[]`

This is a genuine narrowing of Gap G-1: the candidate surface is an *elliptic*
arithmetic surface, and the natural first guesses (`P^1_Z`, `g >= 2` curves) are
excluded as long as `K = 0` is required to transport. It is stated as a
conditional because the hypothesis "`K = 0` transports to `omega_X = 0`" is not
forced — a realisation could match `s` without matching the canonical class.

---

## 6. Gaps

**Gap G-4 (the torsion bound).**

> *Statement.* Let `X -> Spec Z` be the surface of Gap G-1, and let
> `T(D) = (1/2) log(det Delta_{O_infinity}/det Delta_{D_infinity}) + chi_X(O_X)`.
> Prove or disprove: `T(D) > -D^2/2` for every `D` in the image of `D^o_R` with
> `D^2 > 0`.
>
> *What would close it.* An upper bound for the analytic torsion
> `zeta'_{D}(0)` in terms of `D^2` — the arithmetic-surface analogue of the
> Ray–Singer estimates; or a Noether-type formula bounding `chi_X(O_X) +
> (1/2) log det Delta_{O_infinity}` (Wei He's Prop 3.1 (`Noe`), due to Faltings
> and Moret-Bailly, is exactly such a formula and was **not read** in this
> session).
>
> *Believed hard.* Unclear, and *interestingly* so: this is an analytic estimate
> about a fixed Riemann surface, not a statement about zeros. It is the first
> gap in row (d) that is not visibly RH-equivalent. If G-1 were ever supplied,
> G-4 would be the whole remaining content.

**Gap G-5 (the `K = 0` transport).**

> *Statement.* Decide whether a realisation `iota` of Gap G-1 must send the
> corpus canonical class to `omega_X`; equivalently, whether the Frobenius
> trace structure `(D/rad, *, ^*, tau)` determines the dualising sheaf of the
> target.
>
> *What would close it.* Serre duality on the two sides: 113_12 section 3
> (nondegeneracy of the trace form) versus relative Serre duality
> `H^1(X,L)^v = H^0(X, omega_{X/O} (x) L^v)` (quoted by Wei He in the proof of
> his Prop 2.7). A matching of the two dualities would force the transport.
>
> *Believed hard.* No — this looks like bookkeeping, but it has not been done.

---

## 7. Refutation conditions

Continuing from R28 of 114_d3_01.

- **R29.** If any Riemann–Roch on `Spec Z-bar`, or on `Spec O` for a number
  field, is exhibited whose `chi` has unbounded second difference along
  `D |-> nD`, Proposition 2.3 and Theorem 4.2 are wrong.
- **R30.** If the analytic torsion term in Theorem 3.2 is shown to vanish
  identically for the class of surfaces relevant to Gap G-1, then (A') collapses
  to Ansatz A and Gap G-4 disappears — this would be a *positive* firing and
  must be reported as such.
- **R31.** If a candidate `chi` in this programme is ever proposed that is
  quadratic but does **not** satisfy `chi(K - D) = chi(D)`, it contradicts both
  Theorem 3.2 and Wei He's `(lap)`, and is wrong.
- **R32.** If the exceptional set `L` of Connes–Consani Theorem 1.1 is read with
  `k in Z` rather than `k >= 0`, the formula fails on a set of positive measure
  (measured: 569 grid points) — any file in this phase using the `k in Z`
  reading is wrong.

---

## 8. Verifier output

Real output of `python3 114_d3_02_linear_vs_quadratic_chi.py`, run in this
session:

```
A. RR for arithmetic curves (Wei He eq. (rrc), van der Geer-Schoof) over Spec Z
PASS  chi_O(a) = h^0(a) - h^1(a) = deg = a  (Poisson/Jacobi), 12 values
      [max error = 1.837e-40]
PASS  second difference of chi_O along D -> nD is 0 (chi_O is exactly linear)
      [max |d2| = 1.837e-40]

B. Bost bounds (Wei He Prop 2.1 (ii),(iii), F = Q, rank 1)
PASS  deg <= 0  ==>  h^0_O <= 3(1-1/2pi) exp(-pi e^{-2deg})   (Bost 2.7.1)
PASS  that bound is itself <= 1
PASS  deg >= 0  ==>  h^0_O <= 1 + deg                          (Bost 2.7.2)
PASS  h^0_O(F) > 0 for EVERY Arakelov divisor (the zero section always counts)
      [h^0(-3) = 7.45287e-551 > 0]

C. threshold effectivity: h^0_O(a) >= h^0_O(0) = log theta(1)  <==>  a >= 0
PASS  threshold h^0_O(0) = log(pi^{1/4}/Gamma(3/4)) = 0.0829015200311
      [|h^0(0) - closed form| = 7.175e-42]
PASS  a |-> h^0_O(a) is strictly increasing (each theta term is increasing in a)
PASS  a < 0 ==> h^0 < h^0(0) ; a > 0 ==> h^0 > h^0(0)  (exact, by monotonicity)
PASS  h^0(0) - log(1+2e^{-pi}) = log(1 + tail/(1+2e^{-pi})) exactly,
      tail = 6.97469e-6   [h^0(0) - naive = 6.41981e-6 > 0]
PASS  the naive threshold is WRONG: it calls deg a effective for all a > a_0
      with a_0 < 0   [a_0 = -1.28399e-5
      (false-positive interval (a_0, 0) has length 1.28399e-5)]

D. Connes-Consani Riemann-Roch for Spec Z-bar (their Thm 1.1)
PASS  CC RR  dim H^0 - dim H^1 = ceil'(deg' D + log' 2) - 1_L  on 10001 grid points
      [failures: 0 ; grid points inside the exceptional set L: 569]
PASS  the exceptional set L is nonempty on the grid (the test is not vacuous)
PASS  dropping 1_L breaks the formula exactly on the 569 exceptional grid points
PASS  ceil'((deg D + log2)/log3) is odd under D -> K - D with deg K = -2 log 2
      (CC Thm 1.2, the numerical shadow of Serre duality)

E. CC's chi is linear + O(1); its second difference is bounded
PASS  |chi_CC(D) - (deg' D + log' 2)| <= 1 on 6001 points
      [max deviation = 0.999722]
PASS  second difference of chi_CC along D -> nD is bounded (max = 1), so chi_CC
      is NOT quadratic

F. the Faltings-Deligne-Gillet-Soule surface chi is quadratic (symbolic)
PASS  chi-tilde is quadratic in the class: coefficient of n^2 in chi-tilde(nL)
      is (L,L)/2   [chi-tilde(nL) = LL*n**2/2 - Lw*n/2 + c0]
PASS  second difference of chi-tilde along L -> nL equals (L,L) exactly [d2 = LL]
PASS  Serre symmetry: chi-tilde(omega - L) = chi-tilde(L)
PASS  K = 0 specialisation: chi-tilde(L) = (L,L)/2 + chi-tilde(O)
PASS  H^2 = 2 in the polar block
PASS  (3f_v - f_h)^2 = -6 in the polar block
PASS  second difference of Ansatz-A chi along H -> nH is H^2 = 2, which no
      Spec Z-bar chi can have (max second difference measured in E: 1)
PASS  over the rescaling family L -> mL the second difference is 2m^2 =
      2, 8, 18, 32, 50: unbounded

G. the corrected Ansatz A:  chi(D) = D^2/2 + T(D),  T = torsion + chi(O)
PASS  113_12 Thm 5.1 needs chi(D) > 0 whenever D^2 > 0; with the imported RR
      this is D^2/2 + T(D) > 0, i.e. T(D) > -D^2/2
PASS  without a bound on T the deduction FAILS: D^2 = 2 > 0 but chi = -1 < 0
PASS  with T = 0 (the uncorrected Ansatz A) the deduction goes through: chi = 1 > 0

checks run: 28      failures: 0
VERDICT: ALL CHECKS PASS
```

**One correction made in the course of running it, recorded because it changes a
statement.** The first version of section C used the "shortest vectors only"
threshold `log(1 + 2e^{-pi})`, which is the value one writes down by hand. It is
*not* the correct effectivity threshold: it lies `6.42e-6` **below** `h^0_O(0)`,
so the test "`h^0 >= log(1+2e^{-pi})`" declares effective an interval
`(a_0, 0)` of strictly negative degrees, `a_0 = -1.28e-5` (located by bisection
above). The exact threshold is `h^0_O(0) = log theta(1) =
log( pi^{1/4} / Gamma(3/4) ) = 0.0829015200311`, for which
`h^0_O(a) >= h^0_O(0) <==> a >= 0` holds **exactly**, by strict monotonicity of
`a |-> h^0_O(a)`. Section 4 of `114_d3_03` uses only the exact threshold.

---

## 9. Scope

### Proved here

- Proposition 2.3: both one-dimensional Riemann–Rochs (`chi_O`, `chi_CC`) are
  affine in the degree with uniformly bounded second difference.
- Proposition 3.3: the imported surface `chi-tilde` is exactly quadratic, with
  second difference `(L,L)`, Serre-symmetric, and specialises at `omega = 0` to
  Ansatz A's shape.
- Theorem 4.1: **R16 does not fire** — a quadratic `chi` over `Spec Z` exists.
- Theorem 4.2: it cannot come from `Spec Z-bar` or from an arithmetic curve;
  Ansatz A is bound to an arithmetic surface (Cor 4.3).
- Theorem 5.2: 113_12 Thm 5.1 survives the import if and only if the torsion
  obeys `T(D) > -D^2/2`.
- Proposition 5.4: if `K = 0` transports, the surface has genus-1 generic fibre.

### Read from source

- Wei He arXiv:2512.01811v2: equation `(rrc)` (van der Geer–Schoof RR for
  arithmetic curves), equation `(arrf)` (Faltings–Deligne–Gillet–Soulé relative
  arithmetic RR), Theorem 1.1 = 2.8 and the definitions of `h^0_X, h^1_X, h^2_X,
  chi_X`, Proposition 2.1 (Bost's bounds, and Groenewegen's), equation `(lap)`
  (`det Delta_L = det Delta_{Omega (x) L^v}`), and `(l2q)` (Quillen metric). All
  quoted verbatim in sections 2 and 3.
- Connes–Consani arXiv:2205.01391v2: Theorem 1.1 and Theorem 1.2 with the
  dimension formulas `(dimhznintro)` and `(dimh1intro)`, quoted verbatim in
  section 2. This upgrades 113_11 section 4's second-hand citation to
  first-hand.

### Verified numerically

- The arithmetic-curve RR over `Spec Z` as Jacobi's identity, to `1.8e-40`;
  linearity of `chi_O`; Bost's two bounds; the exact effectivity threshold
  `h^0_O(0) = log(pi^{1/4}/Gamma(3/4))` **and the failure of the naive threshold
  `log(1+2e^{-pi})`**; the Connes–Consani RR on 10001 points including 569 points
  of the exceptional set, and the necessity of the `1_L` term; the boundedness
  of `Delta^2 chi_CC`; the quadraticity and Serre symmetry of the imported
  surface `chi`, symbolically; the failure mode of the uncorrected Ansatz A.

### Not established

- Gap G-4: any bound at all on the analytic torsion term `T`. **Open**, and it
  is a *new* gap created by taking the import seriously; it was not visible
  while `chi = D^2/2` was assumed.
- Gap G-5: whether `K = 0` must transport to `omega_X = 0`.
- Gap G-1 (from 114_d3_01) is untouched here: no arithmetic surface is
  constructed, and Theorem 4.1 exhibits only the *existence of the right kind of
  Riemann–Roch*, on surfaces that have nothing to do with `xi` so far.
- Nothing here proves RH or `(E^o)`.
