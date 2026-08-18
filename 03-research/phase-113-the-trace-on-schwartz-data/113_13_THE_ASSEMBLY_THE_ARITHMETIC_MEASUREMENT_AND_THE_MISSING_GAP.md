# 113_13 — d5: the assembly, the form measured from primes, and why there is no gap

```
THE ASSEMBLY (d5):   d0-d4 chain stated and checked; row (d) = Ansatz A.
s(f,f) ON D^o FROM   MEASURED.  Prime side minus archimedean equals the zero
PRIMES:              side to ~1e-15 at four probes; every value is <= 0.
                     First arithmetic measurement of the index form on D^o.
NO-GAP THEOREM:      sup s(f,f)/||f||^2 = 0 over D^o \ rad, NOT attained.
                     Measured: ratio falls to 1e-176 while a control grows.
OBSTRUCTION O2:      the correspondence lattice cannot be paired -- s is
                     INFINITE on delta masses.  PROVED.
OBSTRUCTION O3:      no coercive proof of row (d) can exist.  PROVED.
CONVERGENT VERDICT:  O1, O2, O3 are three independent proofs of one thing --
                     there is no lattice.  That is the whole remaining gap.
```

Depends on: 113_06 (Def 2.1 for `A(h)`, Thm 2.2 the explicit formula), 113_09,
113_10, 113_11 (O1), 113_12 (`tau`, Thm 4.1, Ansatz A).

Verifier: `113_13_the_assembly_and_the_missing_gap.py`

---

## 1. The assembly (d5)

The backward map is now complete as a chain of proved implications. Writing
`V = D / rad` and `V^o = D^o / rad`:

| step | statement | status |
|---|---|---|
| d0 | `deg(f) = s(f,H) = f^(0)+f^(1) = int f(u)(1+u) d^x u`; `deg(rad) = 0` | **proved**, 113_10 Thm 1.2–1.3 |
| d1 | `rad I_d = (s(s-1) xi)`; the rulings `f_v, f_h, H, w` exist in `D` | **proved**, 113_09 Thm 2.2, 3.1 |
| d2 | `V` is a ring; `f_v, f_h` are its minimal polar idempotents; `H` their sum | **proved**, 113_11 Thm 1.1–1.2 |
| d3 | a section functor `h^0` | **blocked**, 113_11 Thm 3.3 (and 4.1) |
| d4 | `s(x,y) = tau(x*y^*)`; `s` Hermitian, nondegenerate; `K = 0` | **proved**, 113_12 §1–3 (mod (SEP)) |
| d5 | Hodge index on `V` | **= RH**, 113_12 Thm 4.1 |

and the one statement that would close everything:

> **Ansatz A** (113_12 §5): `h^0 - h^1 + h^2 = D^2/2`, with `h^2(D) = h^0(-D)`
> and `h^0(D) >= 1` iff `D` is effective or `D = 0`.
>
> Ansatz A `=>` `(E^o)` `=>` RH (113_12 Thm 5.1, 113_10 Thm 4.2), and Ansatz A
> passes every pre-registered test the programme has produced: R7, R8, R9.

So d5 is not a separate task: given d0–d4, the assembly is Theorem 4.1 of 113_12,
and it says row (d) *is* RH. What remains is d3, i.e. Ansatz A. The rest of this
file is about what stands in its way, and it produces two new obstructions and
one new measurement.

---

## 2. The intersection form measured from primes, on `D^o`

Until now the form was measured from arithmetic only on the ruling classes
(113_09 Thm 4.1: `H^2 = 2`, `(F_v - F_h)^2 = -2`). Those live in the polar block,
where the zero sum drops out. The interesting block — the one row (d) is about —
is `D^o`, and it had never been measured from primes.

**Setup.** Take the balanced profile `F(x) = e^{-x^2/(2 sigma^2)}(cos(bx) - c)`
with `c` chosen so that `F^(±1/2) = 0`, i.e. `f` lies in `D^o`. Put
`h := f * f^*`, so `s(f,f) = tau(h)` by 113_12 Thm 1.3. Three quantities:

```
  prime side   P(h) = sum_{n>=2} Lambda(n) [ h(n) + h(1/n)/n ]
                    = sum_{n>=2} Lambda(n) . 2 n^{-1/2} H(log n)
  archimedean  A(h) = (1/pi) int [ (1/2)Re psi(1/4 + it/2) - (1/2)log pi ]
                              |F^(it)|^2 dt              (113_06 Def 2.1)
  zero side    Z    = - sum_rho m_rho |F^(i gamma_rho)|^2
```

with the autocorrelation `H(x) = int F(x+y) F(y) dy` in closed form,

```
  H(x) = sqrt(pi) e^{-x^2/4} [ (e^{-b^2} + cos(bx))/2
                               - 2c e^{-b^2/4} cos(bx/2) + c^2 ] ,
  F^(it) = sigma sqrt(2pi) { [e^{-sigma^2(t-b)^2/2} + e^{-sigma^2(t+b)^2/2}]/2
                             - c e^{-sigma^2 t^2/2} } .
```

**Measurement** (`sigma = 1`, primes and prime powers to `2 x 10^5`, 20 zeros;
the zeros enter only the right-hand column, which is a verification of an
identity, never a definition):

| `b` | `P(h)` | `A(h)` | `tau(h) = P - A` | zero side `Z` | `|tau - Z|` |
|---|---|---|---|---|---|
| 14 | `-2.3763816862725` | `0.70870273490994` | `-3.0850844211824` | `-3.0850844211824` | `2.7e-15` |
| 10 | `0.40922855105741` | `0.40922866921789` | `-1.1816047908e-7` | `-1.1816048291e-7` | `3.8e-15` |
| 25 | `-1.9177586182303` | `1.2234641256125` | `-3.1412227438428` | `-3.1412227438428` | `4.0e-16` |
| 6 | `-0.048237528080248` | `-0.048237528080247` | `-1.35e-15` | `-5.73e-29` | `1.3e-15` |

**Theorem 2.1 (what was measured).** At all four probes,
`s(f,f) = tau(f * f^*) <= 0`, computed from `Lambda(n)` and the digamma kernel
alone, and agreeing with the spectral side to the resolution of the computation.
This is Weil positivity, evaluated arithmetically, on the block where row (d)
lives.

Three things are worth extracting, and the third is the subject of section 3.

1. **The identity is a real test.** At `b = 10` and `b = 6` the prime side and
   the archimedean side agree to 7 and 15 digits *with each other*, and their
   difference — the quantity of interest — is 7 to 15 orders of magnitude
   smaller than either. Nothing about the computation is arranged to make that
   happen.
2. **The arithmetic side has finite resolution.** At `b = 6` the true value is
   `-5.7 x 10^-29` and the prime computation returns `-1.3 x 10^-15`: the
   truncation floor. So the arithmetic side can *confirm* negativity but cannot
   certify it below its own noise. Any numerical programme aiming at row (d)
   from primes inherits this floor.
3. **The values collapse toward zero when `b` avoids the zeros.** `b = 14` and
   `b = 25` sit near ordinates (`14.13`, `25.01`) and give `s(f,f) ~ -3`;
   `b = 10` and `b = 6` sit in gaps and give `-10^-7` and `-10^-29`. The form is
   negative, but it is nowhere near uniformly negative.

---

## 3. The no-gap theorem

**Theorem 3.1.** There is a sequence `f_k` in `D^o`, none in `rad I_d`, with
`||f_k||_{L^2} = 1` and `s(f_k, f_k) -> 0`. Equivalently

```
        sup { s(f,f) / ||f||^2  :  f in D^o real, f not in rad I_d }  =  0 ,
```

and the supremum is not attained.

*Proof.* For `f` in `D^o`, `s(f,f) = -sum_rho m_rho f^(rho) conj(f^(rho'))`,
which under RH is `-sum_rho m_rho |F^(i gamma)|^2`. Fix `b` strictly between two
consecutive ordinates, at distance `delta > 0` from the nearest, and take
`F_sigma(x) = e^{-x^2/(2 sigma^2)}(cos(bx) - c_sigma)` normalised in `L^2`. Then
`|F^_sigma(i gamma)|^2` carries a factor `e^{-sigma^2 (gamma - b)^2}` and hence
`e^{-sigma^2 delta^2}` uniformly, while `||F_sigma||^2` grows only like `sigma`.
The zero-counting function is `O(T log T)`, so the sum converges and is
`O(sigma^{-1} e^{-sigma^2 delta^2} . polylog)`, which tends to `0`. Not attained:
if `f` is not in `rad` then `f^(rho_0) != 0` for some `rho_0` (113_09 Thm 2.2),
so `s(f,f) <= -m_{rho_0}|f^(rho_0)|^2 < 0`. `[]`

**Measured** (`b = 17.5`, in the gap `(14.134, 21.022)`; ratio is
`s(f,f)/||f||^2`):

```
  sigma    s(f,f)                   ||f||^2       ratio
  1        -5.078557256e-5          0.88622693    -5.7305382e-5
  2        -2.699509571e-19         1.7724539     -1.5230352e-19
  3        -1.533418955e-43         2.6588856     -5.7671489e-44
  4        -1.015288545e-77         3.5978127     -2.8219605e-78
  5        -8.60303686e-122         4.2064607     -2.0451961e-122
  6        -9.781861575e-176        5.7281483     -1.707683e-176
```

and the control, with `b` placed **on** the first ordinate `14.1347...`, where
the ratio must not collapse:

```
  sigma    s(f,f)         ||f||^2      ratio
  1        -3.141592654   0.88622693   -3.5449077
  2        -12.56637061   1.7724539    -7.0898154
  4        -50.26548246   3.5480142    -14.167216
  6        -113.0973355   5.1283532    -22.053344
```

The two columns are produced by the same function with one argument changed.
Off a zero the ratio falls by 170 orders of magnitude; on a zero it grows.

**Obstruction O3 (no coercive proof).** Row (d) holds — under RH — with no
margin whatsoever. Consequently:

- Any argument that would establish `s(f,f) <= -epsilon ||f||^2` for some fixed
  `epsilon > 0` on `D^o` is **false**, not merely unavailable. Theorem 3.1
  refutes it outright.
- Any argument routed through a spectral gap, a coercivity estimate, a uniformly
  positive-definite kernel, or compactness of the unit ball of `V^o` is
  therefore dead on arrival.
- What is *not* ruled out: arguments giving `s(f,f) <= 0` with no margin — which
  is exactly the shape a Riemann–Roch inequality has (`chi(D) > 0` forces a
  section, with no quantitative content). Ansatz A survives O3. This is a point
  in its favour, and one of the few available.

**Remark 3.2 (a third reading of "no lattice").** On an algebraic surface, the
Néron–Severi group is a *lattice* of finite rank; a negative-definite form on a
lattice has a gap — `-1` is the largest nonzero value of `-sum x_i^2` on
`Z^n \ {0}`. Theorem 3.1 says our negative part has no gap, which is the
statement that `V^o` contains no such lattice. That is the same conclusion O1
reached from scaling (113_10 §5) and O2 reaches below from divergence, by three
unrelated routes.

---

## 4. Obstruction O2: the correspondence lattice cannot be paired

113_11 §5 identified where the missing `Z`-structure ought to be: the index set
of the `Lambda`-sum, i.e. the free abelian group on the prime powers, which is
the arithmetic analogue of Weil's group of correspondences. The natural way to
give it an intersection form is to embed it into (a completion of) `D` by
`n |-> delta_n`, the unit mass at `u = n`, and restrict `s`. This section shows
that fails, quantitatively.

**Theorem 4.1.** With `delta_n^(s) = n^s`,

```
        s(delta_n, delta_m)  =  m + n  -  m . sum_rho m_rho (n/m)^rho ,
```

and the series diverges for every `n != m`, `n, m > 0`.

*Proof.* Substitute `x^(0) = 1`, `x^(1) = n`, `x^(rho) = n^rho` and
`conj(y^(rho')) = conj(m^{1 - conj(rho)}) = m^{1 - rho}` into the definition of
`s`; the zero term is `sum_rho m_rho n^rho m^{1-rho} = m sum_rho m_rho (n/m)^rho`.
Divergence: `|(n/m)^rho| = (n/m)^{Re rho}`, which lies between
`min(1, n/m)` and `max(1, n/m)` and is bounded away from `0`. The terms of a
convergent series tend to `0`; these do not. `[]`

Measured at `n/m = 3/2`, where every term has modulus `sqrt(3/2) = 1.2247...`:
the symmetric partial sums over `|gamma| < T` are

```
  K=5: 2.8305   K=10: 2.3678   K=20: 2.0270   K=40: 1.0671   K=59: 1.2144
```

— wandering, with no sign of a limit, exactly as a distribution should.

**Obstruction O2.** The intersection form is a *distribution*, not a function, on
the correspondence lattice: it takes no finite value on the very generators that
carry the integrality. Smoothing `delta_n` into an element of `D` restores
finiteness but replaces the integer coefficient by a real one, destroying the
lattice. So the `Z`-structure and the pairing are incompatible for a second,
independent reason — 113_11 Thm 3.1 said they live on different objects; O2 says
that even where they meet, the pairing is infinite.

This also explains, in one line, why Arakelov-style finiteness (lattice points
in a ball — the mechanism behind CC's integer `dim H^0`, as recorded in
`phase-39/120-inventario-CC-fuente.md`: divisors `sum n_i x_i` with
`sum |n_i| <= e^a`) cannot be transplanted here. The ball is fine; it is the
form on the lattice that is infinite.

---

## 5. Verdict on row (d)

**Row (d) is not closed.** It is reduced, exactly, to Ansatz A, and Ansatz A
implies RH (113_12 Thm 5.1). The programme has therefore converted "prove the
Riemann Hypothesis" into "prove one specified Riemann–Roch theorem of surface
type over `Spec Z`" — which is a genuine reduction in the sense that the
remaining statement is single, precise, and falsifiable, and *not* a reduction
in the sense of making anything easier.

What this phase established about the obstacle, which is the part that is new:

> The obstacle is the absence of a lattice, and it has been proved three
> independent times.
>
> - **O1** (113_10 §5, 113_11 Thm 3.3) — the divisor group is a complex vector
>   space; the effective cone is scaling-stable; `h^0(nD) = h^0(D)`, measured
>   exactly at `n = 2, 5, 100`.
> - **O2** (Thm 4.1 here) — the natural integral generators, the correspondences
>   `delta_n`, have infinite self- and mutual intersection.
> - **O3** (Thm 3.1 here) — the negative part has no spectral gap, which a
>   negative-definite lattice always has. Measured: `10^-176` against a control
>   that grows.
>
> Each rules out a different escape: O1 kills asymptotic (`n -> infinity`)
> arguments, O2 kills discretising the correspondence side, O3 kills coercive or
> compactness arguments. What survives all three is precisely a
> non-quantitative, `n = 1`, section-existence statement — Ansatz A — and no
> Riemann–Roch theorem of that shape is known over `Spec Z`. Connes and Consani
> identify the same object as their open problem (`1805.10501`; corpus:
> *"Nadie ha cruzado todavía 'RR absoluto' con 'cuadrado'"*).

Pre-registered refutation conditions:

- **R17.** If any `f` in `D^o` is exhibited with `s(f,f) > 0`, RH is false and
  §2's measurement was wrong. The measurement is cheap to rerun at new probes;
  this is the one test in the phase that could in principle *disprove* RH.
- **R18.** If a coercive bound `s(f,f) <= -epsilon ||f||^2` is ever claimed,
  Theorem 3.1 refutes it. The `b = 17.5, sigma = 6` datum is the counterexample.
- **R19.** If someone gives the correspondence lattice a finite pairing that
  restricts to `s` on `D`, Theorem 4.1 says the embedding cannot be
  `n |-> delta_n`; the burden is to say what it is instead.
- **R20.** §2 assumes RH only in the *right-hand* column (the zero side, where
  computed zeros are used to verify an identity). The prime side and `A(h)` are
  computed unconditionally. If the two columns are ever found to disagree beyond
  the truncation floor, the error is in this file, not in the literature.

---

## 6. Scope

**Proved here:**

- Thm 3.1 — no gap: `sup s(f,f)/||f||^2 = 0` on `D^o \ rad`, not attained.
  (Under RH for the clean form; the *construction* of the sequence and the
  measured collapse are unconditional.)
- Thm 4.1 — `s(delta_n, delta_m) = m + n - m sum_rho m_rho (n/m)^rho`, and the
  series diverges. Unconditional.
- O2, O3 as stated, and Remark 3.2 relating them to O1.
- §1 — the d0–d5 assembly table, each entry with its source.

**Read from source (quoted, not re-derived):**

- `A(h)` — 113_06 Def 2.1, verbatim.
- The explicit formula (2.2) — 113_06 Thm 2.2.
- `s = tau(x * y^*)`, `K = 0`, Hodge index `<=>` RH, Ansatz A and Thm 5.1 —
  113_12.
- `rad = (s(s-1)xi)` — 113_09 Thm 2.2.
- CC's open problem — via the phase-39 inventory, a second-hand source, flagged
  as such in 113_11 §7.

**Verified numerically:**

- The closed forms for `F^(it)` and for the autocorrelation `H`, against
  quadrature, to 15 digits.
- §2's three-way identity at four probes: `|P - A - Z| <= 4e-15`, with all four
  `tau` values `<= 0`.
- Thm 3.1: the ratio at `b = 17.5` for `sigma = 1..6`, and the on-zero control.
- Thm 4.1: partial sums at `n/m = 3/2`, and `|(3/2)^rho| = sqrt(3/2)` for every
  `rho`.
- Negative controls: an on-zero probe (ratio grows, not collapses); a
  `sigma`-independent claim (refuted); the `b = 6` resolution floor, reported
  rather than hidden.

**Not established:**

- Ansatz A, in any part. RH-hard.
- `(E^o)`, hence row (d).
- (SEP), carried over from 113_12.
- Rows (a) and (b): unchanged, and untouched by this file.
- **RH.** Nothing in phase 113 proves RH. Sections 2–4 constrain how it could be
  proved in this framework and rule out three families of attempt; they do not
  prove it, and Theorem 4.1 of 113_12 shows that anything that did would be a
  proof of RH itself.

---

## 7. Verifier

`113_13_the_assembly_and_the_missing_gap.py` — **33 checks, 33 pass, exit 0.**
Sections A (closed forms vs quadrature), B (§2's three-way measurement, four
probes), C (Thm 3.1 and the on-zero control), D (Thm 4.1 and divergence),
E (the assembly table's numerical entries).

**A control that failed first, and the diagnosis.** The obvious negative control
on `A(h)` is 113_06's own: replace the kernel by its complex version, dropping
the `Re`, which 113_06 reports fails by 27%–97%. Here it **did not fail** — the
identity still closed to `2.7e-15`. The reason is not an error in either file.
113_06's discriminating probes include an *odd* profile
(`h~(x) = x e^{-100 x^2}`); every profile in 113_13 is **even**, so `F^(it)^2`
is even, `Im psi(1/4 + it/2)` is odd, and the imaginary part integrates to
exactly zero. This probe family is structurally blind to the `Re`.

The control was replaced by two that this family *can* see, and both fire:

```
  [PASS] diagnosis: for EVEN profiles the Re in the kernel is invisible
         |tau_noRe - Z| = 2.660e-15 -- so this family cannot test the Re
  [PASS] negative control: dropping the -(1/2)log pi term breaks the identity
         |tau_bad - Z| = 1.09939
  [PASS] negative control: the 1/pi prefactor is not free -- 1/(2pi) breaks it
         |tau_bad - Z| = 0.354351
  [PASS] negative control: truncating the prime sum at n <= 100 breaks it
         |tau_short - Z| = 0.00890833
```

The point is general and worth carrying forward: **a negative control inherited
from another file is only valid if the new probe family can see the feature it
perturbs.** The `Re` in 113_06 Def 2.1 is genuinely necessary; it is simply not
testable against real even data, and §2's agreement is therefore not evidence
for it either way.
