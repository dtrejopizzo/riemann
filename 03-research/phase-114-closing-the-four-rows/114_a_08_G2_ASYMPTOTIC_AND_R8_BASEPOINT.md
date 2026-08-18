# 114.a.08 — G-2 solved: the `l1` gauge has an `m log m` term; R8 baseline fixed

```
+--------------------------------------------------------------------------+
| G-2          CLOSED.  For r=mk+1 and R=floor(exp(ma)),                   |
|              log |I_r(R)| = r log(2R) - log(r!) + O(r^2/R).             |
|              Hence the next term is -km log m, not a linear RR term.     |
|                                                                          |
| CONSEQUENCE  The quadratic coefficient is gauge-robust, but subleading   |
|              terms are not: l1 has -km log m; box and theta have         |
|              different linear terms.  No missing saddle point can turn  |
|              the l1 count into the exact theta RR formula.               |
|                                                                          |
| R8           The acceptance-test repair is canonical at the basepoint:   |
|              Eff_thr(L) iff h0_theta(L)>h0_theta(O).  It sends the image  |
|              of every radical element to the boundary, not the interior. |
|              This repairs R8 as a predicate, not the full dictionary.    |
|                                                                          |
| G-1          Still open, elementary and unnecessary for a4: it asks for  |
|              the exact leading constant of CC's minimal generator count. |
| G-3          Delimited in a_13: additive form RH-equivalent; bare         |
|              non-additive domination vacuous; structured version open.  |
+--------------------------------------------------------------------------+
```

## 1. Exact count of the cross-polytope lattice points

For integers `r,R>=0`, let

```
I_r(R)={c in Z^r : |c_1|+...+|c_r|<=R}.
```

The exact count is

```
|I_r(R)| = sum_{j=0}^{min(r,R)} 2^j binom(r,j) binom(R,j).    (1.1)
```

Indeed, choose the `j` nonzero coordinates, their signs, and a composition of
an integer at most `R` into `j` positive parts.

Write `T_j=2^j binom(r,j)binom(R,j)`.  For `1<=j<=r<=R`,

```
T_(j-1)/T_j = j^2/[2(r-j+1)(R-j+1)].                        (1.2)
```

In particular, if

```
q=r^2/[2(R-r+1)]<1,
```

then every downward ratio is at most `q`, and

```
T_r <= |I_r(R)| <= T_r/(1-q).
```

### Theorem 1.1 (uniform large-radius asymptotic)

If `r^2/R -> 0`, then

```
log |I_r(R)| = r log 2 + log binom(R,r) + O(r^2/R)
             = r log(2R) - log(r!) + O(r^2/R).               (1.3)
```

*Proof.* The geometric bound above gives
`log(|I|/T_r)=O(q)=O(r^2/R)`.  Also

```
log binom(R,r)=r log R-log(r!)+sum_{j=0}^{r-1}log(1-j/R)
              =r log R-log(r!)+O(r^2/R).
```

`[]`

## 2. G-2 has a negative answer in the proposed form

Take

```
r_m=mk+1,       R_m=floor(exp(ma)),       k,a>0.
```

Then `r_m^2/R_m` is exponentially small.  By Theorem 1.1 and Stirling,

```
log |I_(r_m)(R_m)|
 = r_m log(2R_m) - (r_m+1/2)log r_m + r_m
   - (1/2)log(2pi) + O(1/r_m)
 = ka m^2 - km log m
   + m[a-k log k+k(1+log 2)]
   - (3/2)log m + O(1).                                     (2.1)
```

The displayed second line uses `r_m=mk+1`; changing floor conventions only
changes an exponentially small term.

Thus the old G-2 request for a `Theta(m)` coefficient after the quadratic term
was based on a false asymptotic shape.  The correction is structural:

- `l1` ball: `ka m^2-km log m+O(m)`;
- coefficient box: `ka m^2 + m(a+k log 2)+O(1)`;
- theta lattice: `ka m^2+am+o(1)`.

All three have the same quadratic leading term, as `114_a_02` proved, but
their subleading terms differ.  Therefore gauge robustness holds at arithmetic
volume/self-intersection level and fails at exact Riemann--Roch level.

> **G-2 is closed:** there is no missing linear coefficient for the `l1`
> count; an unavoidable `-km log m` term comes first.

## 3. G-1 was isolated here and is now closed

G-1 asks for the exact limit of the Connes--Consani minimal signed-generator
dimension in the coupled regime `r~m`, `log R~m`.  The entropy and binary-digit
bounds leave constants `1/log 3` and `1/log 2`.  Neither Theorem 1.1 nor toric
intersection determines that minimisation problem.

This gap is now cleanly isolated:

- it does not affect the theta invariant;
- it does not affect the toric self-intersection derived in `114_a_07`;
- it does not affect the existence of quadratic growth;
- resolving it cannot supply the missing I7 kernel pairing.

`114_a_11` closes it: counting the entire saturated positive boundary gives
the matching binary lower bound and the exact coupled constant `1/log 2`.
It remains non-load-bearing for a4 and independent of the I7 pairing.

## 4. R8: the only canonical baseline repair

Let `h_theta(L)` denote the raw theta invariant of the normed lattice
`H^0(X,L)`.  Its theta sum contains the zero vector, so

```
h_theta(O_X)=log sum_{n in Z} exp(-pi n^2)=log theta(1)>0.
```

This is not a defect in theta cohomology.  It means that source effectivity
cannot be transported using the raw predicate `h_theta>0`, because that
predicate treats every nonzero lattice as positive and, in particular, treats
the trivial target class as positive.

### Definition 4.1 (strict/basepoint effectivity)

Define only the predicate

```
Eff_thr(L)  <=>  h_theta(L)>h_theta(O_X).                     (4.1)
```

Equivalently set `h_thr=h_theta-h_theta(O_X)` for purposes of the sign test.
Do **not** replace the cohomological theta invariant by `h_thr` inside a quoted
Riemann--Roch theorem unless all other terms are renormalized consistently.

### Proposition 4.2 (R8 acceptance test repaired)

If a realisation `iota` has `ker(iota)=rad`, then every `w in rad` maps to
`O_X`, and hence

```
h_thr(iota(w))=0.
```

No nonzero radical element is declared strictly effective.  Thus R8 passes
for the threshold predicate.

The threshold is forced among constant thresholds if the trivial class is to
lie exactly on the boundary: it must equal `h_theta(O_X)`.

### What remains open

R8 is an acceptance test, not the whole effectivity dictionary.  Still needed
is a construction of `iota` and a proof that source-effective classes map
precisely to `Eff_thr`.  That problem is part of G-3/G-effectivity and cannot be
deduced from the baseline normalization.

## 5. Updated status

| gate | status |
|---|---|
| G-0 metric/intersection realisation | CLOSED by `114_a_07` |
| G-1 exact CC dimension constant | **CLOSED by `a_11`: `1/log 2`** |
| G-2 counting-gauge subleading term | **CLOSED here**, formula (2.1) |
| G-3 comparison/realisation | FULLY DELIMITED through `a_60`: meaningful additive, polarized or effectivity-compatible versions are RH-equivalent; unstructured version vacuous |
| R8 raw theta predicate | FAILS |
| R8 threshold predicate | **REPAIRED here** |
| full source/target effectivity dictionary | OPEN |

## 6. Verifier and refutation conditions

`114_a_08_g2_r8_verify.py` checks the exact formula (1.1), dominance of `T_r`,
the asymptotic expansion against exact integer counts, the three distinct
subleading laws, and the exact R8 basepoint cancellation.

- **R46.** G-2 reopens if (1.1) or the dominance estimate is false.
- **R47.** The asymptotic (2.1) is false if its error against exact counts is
  not `O(1)` after the displayed logarithmic terms are retained.
- **R48.** The R8 repair is only a predicate normalization.  A future use of
  `h_thr` as raw cohomology without adjusting RR fires this condition.
