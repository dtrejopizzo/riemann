# 113_10 — The degree map, the effective cone, and the reduction of row (d) to a single statement

```
DEGREE MAP d0:        CONSTRUCTED EXPLICITLY, deg(f) = int f(u)(1+u) d^x u
deg(rad) = 0:         PROVED (so deg descends to D/rad)
REQUIREMENT (R):      PROVED  (was pre-registered open in 113_08 section 4)
POLARIZATION H:       PROVED EFFECTIVE, H = 2*Phi (Riemann's Phi-function)
ROW (d) REDUCED TO:   (E^o) alone -- and (E^o) is shown to be EQUIVALENT to RH
OBSTRUCTION O1:       the divisor group is a VECTOR SPACE; the classical
                      Riemann-Roch route to (E^o) is structurally unavailable
```

Depends on: 113_05 (conventions), 113_06 (Thm 2.2, the Weil decomposition),
113_07 (Prop 4.1, the criterion), 113_08 (the rulings, formula (2.2), the
pre-registration of (E) and (R)), 113_09 (rad I_d = the xi-ideal; the rulings
realised in D).

Verifier: `113_10_the_degree_map_and_the_effective_cone.py`

---

## 0. What this file is for

113_08 reduced row (d) — the Hodge-index / Castelnuovo–Severi row — to two
pre-registered requirements:

- **(E)** *effectivity*: `Q(f) > 0  ==>  h^0(D_f) > 0  or  h^0(-D_f) > 0`
- **(R)** *the rulings see effectivity*: `h^0(D) > 0, D != 0  ==>  s(D,F_v) != 0 or s(D,F_h) != 0`

Neither could be stated precisely at the time, because there was no degree map
and no definition of `h^0`. 113_09 supplied the missing analytic object (the
radical is the `s(s-1)xi(s)`-ideal, and the rulings `f_v`, `f_h` are candid
elements of `D`). This file supplies `d0`: the degree.

The outcome is sharper than expected in both directions. **(R) is proved
outright** — it costs three lines once the degree map exists. And the same
three lines show that **(E), restricted to the only place the argument uses
it, is logically equivalent to RH**. That is not a defeat: on an algebraic
surface (E) is likewise not free, it is exactly what Riemann–Roch buys you.
But it does mean row (d) is now one single statement, and section 5 records a
concrete structural obstruction to the classical way of proving it.

---

## 1. The degree map

Recall the standing conventions (113_05, 113_07). For `f` in the algebra `D`,

- `f^(s) = int_0^inf f(u) u^s d^x u`,   `d^x u = du/u`
- balanced profile `F(x) = e^{x/2} f(e^x)`, equivalently `f(u) = u^{-1/2} F(log u)`
- `f^(s) = F^(s - 1/2)` where `F^(z) = int_R F(x) e^{zx} dx`
- `D = union_{theta > 3/2} D_theta`, a commutative `*`-algebra
- `D^o = { f in D : f^(0) = f^(1) = 0 }`
- `rad I_d = { f in D : f^ / (s(s-1)xi(s)) is holomorphic on the strip }`   (113_09 Thm 2.2)
- the rulings `f^_v(s) = -2(s-1)xi(s)`, `f^_h(s) = 2 s xi(s)`, `H = f_v + f_h`,
  `H^(s) = 2 xi(s)`   (113_09 Thm 3.1)
- the pairing `s(x,y) = x^(0) conj(y^(1)) + x^(1) conj(y^(0)) - sum_rho m_rho x^(rho) conj(y^(rho'))`,
  `rho' = 1 - conj(rho)`   (113_08, 107_241)
- formula (2.2) of 113_08: `s(x, F_v) = x^(1)`, `s(x, F_h) = x^(0)`.

**Definition 1.1 (the degree).** For `f` in `D` set

```
        deg(f) := s(f, H).
```

**Theorem 1.2 (three closed forms).** For every `f` in `D`,

```
        deg(f)  =  f^(0) + f^(1)
                =  int_0^inf f(u) (1 + u) d^x u
                =  2 int_R F(x) cosh(x/2) dx .
```

*Proof.* `H^(0) = H^(1) = 2 xi(0) = 2 xi(1) = 1`, and `H` is real
(`H^(s)` is real for real `s`, and `conj(H^(conj s)) = H^(s)`), so by the
definition of `s`, and because `H` lies in the radical's complement with zero
`rho`-coordinates (`H^(rho) = 2 xi(rho) = 0` at every zero `rho`, with
multiplicity, since `H^ = 2 xi`), the zero sum drops out entirely and

```
        s(f, H) = f^(0) conj(H^(1)) + f^(1) conj(H^(0)) = f^(0) + f^(1).
```

For the second form, `f^(0) = int f d^x u` and `f^(1) = int f u d^x u`
(113_08 Thm 1.1), so the sum is `int f(u)(1+u) d^x u`. For the third,
substitute `f(u) = u^{-1/2}F(log u)`, `u = e^x`:
`f^(0) = int F(x) e^{-x/2} dx`, `f^(1) = int F(x) e^{x/2} dx`, and
`e^{x/2} + e^{-x/2} = 2 cosh(x/2)`. `[]`

The three forms are verified against each other to 18 significant digits in
section A of the verifier. (The middle form is the one to remember: **degree is
the total mass of `f` against the measure `(1+u) d^x u`.** It involves no zero,
no `xi`, and no transform.)

**Theorem 1.3 (deg kills the radical).** `deg(g) = 0` for every `g` in `rad I_d`,
so `deg` descends to a linear functional on `D / rad I_d`.

*Proof.* If `g` is in the radical then `g^(s) = s(s-1)xi(s) v(s)` with `v`
holomorphic on the strip (113_09 Thm 2.2). The factor `s(s-1)` vanishes at
`s = 0` and at `s = 1`, so `g^(0) = g^(1) = 0` and `deg(g) = 0`. `[]`

Equivalently: the radical pairs to zero with everything, and `H` is something.
Both readings are recorded, because the second is the one that generalises: `deg`
is *intersection with the polarization*, exactly as on a surface.

**Proposition 1.4 (the values on the geometric classes).**

| class | `f^` | `deg` |
|---|---|---|
| `H = f_v + f_h` | `2 xi(s)` | `2` |
| `f_v` | `-2(s-1) xi(s)` | `1` |
| `f_h` | `2 s xi(s)` | `1` |
| `f_v - f_h` | `-2(2s-1) xi(s)` | `0` |
| `w` (radical generator) | `s(s-1) xi(s)` | `0` |

*Proof.* Evaluate at `s = 0` and `s = 1` using `xi(0) = xi(1) = 1/2`. `[]`

These are the intersection numbers with `H` of 113_09 Thm 4.1 read again:
`deg H = H.H = 2`, `deg F_v = F_v.(F_v + F_h) = 0 + 1 = 1`. The degree map is
not new information; it is the `H`-column of the intersection table. What is
new is closed form two of Theorem 1.2, which turns that column into a
**positive integral**.

**Proposition 1.5 (`D^o` sits strictly inside the degree-zero part).**
`D^o` is contained in `ker(deg)`, and the containment is strict:
`f_v - f_h` has degree `0` but `(f_v - f_h)^(0) = 1 != 0`.

So there are two different "balanced" conditions in play, and they are not the
same. `D^o` (both polar coordinates vanish) is the one Connes' criterion uses;
`ker(deg)` (their sum vanishes) is the one geometry would call degree zero.
`D^o` is the smaller. This matters in section 4: the reduction needs only that
`D^o` is *inside* `ker deg`, which is the easy direction.

---

## 2. The effective cone

**Definition 2.1 (effective).** Call `f` in `D` *nonnegative*, written `f >= 0`,
if `f(u) >= 0` for almost every `u` in `(0, inf)` — equivalently `F(x) >= 0`
a.e. on `R`. Call a class `c` in `D / rad I_d` **effective**, written
`h^0(c) > 0`, if `c` has a nonnegative representative that is not the zero
function:

```
        h^0(c) > 0   <==>   there is f in c with f >= 0 and f not identically 0.
```

Write `Eff` for the set of effective classes.

Two remarks on why this is the right definition and not a convenience.

1. It is the only notion of positivity available on `D` that uses no zero, no
   `xi`, and no choice: it is the pointwise order of the underlying function
   algebra. It is manifestly compatible with the source rule.
2. It is *not* the `*`-algebra positivity `{ f * f~ }`. Those two cones differ,
   and the difference is the content of the whole problem: `f * f~` is the class
   on which `s(f*f~, ...)` is the Weil functional, while `f >= 0` is the class on
   which the degree is positive. Section 4 is exactly the statement that these
   two cones cannot overlap in `D^o`.

**Theorem 2.2 (effective classes have strictly positive degree).**
Let `f` in `D` satisfy `f >= 0` and `f` not identically `0`. Then

```
        f^(0) > 0,      f^(1) > 0,      deg(f) > 0 .
```

*Proof.* `f^(0) = int_0^inf f(u) d^x u` and `f^(1) = int_0^inf f(u) u d^x u`.
Both integrands are nonnegative and not a.e. zero, and the measures `d^x u` and
`u d^x u` have full support on `(0, inf)`; hence both integrals are strictly
positive. Their sum is `deg(f)`. `[]`

Nothing about `xi`, zeros, or the pairing enters. The statement is the
elementary fact that a nonnegative function has positive mass.

**Corollary 2.3 (no nonzero principal divisor is effective).**
`rad I_d` contains no nonnegative function other than `0`:

```
        rad I_d  intersect  { f >= 0 }  =  { 0 } .
```

*Proof.* If `g` is in the radical and `g >= 0` then `deg(g) = 0` by Theorem 1.3
and `deg(g) > 0` by Theorem 2.2 unless `g = 0` a.e. `[]`

This is the exact analogue of the function-field fact that the divisor of a
nonconstant rational function is never effective, and it is the first
structural check that the pair (`deg`, `rad`) behaves like (degree, principal
divisors) rather than being an accident of notation. The verifier confirms it
concretely: the radical generator `w` has profile `W = Phi'' - Phi/4`, which
takes the value `-16.95` at `x = 0` and `+6.78` at `x = 0.5` — it changes sign,
as Corollary 2.3 forces.

**Corollary 2.4 (`D^o` meets no effective class).**
`D^o intersect { f >= 0 } = { 0 }`, and no class in `D^o + rad` is effective.

*Proof.* `f` in `D^o` has `f^(0) = 0`, contradicting Theorem 2.2 unless
`f = 0`. For the class statement, `deg` is constant on classes and vanishes on
`D^o`. `[]`

Consistency check, not a proof, but worth recording: the standard `D^o` probe
used since 113_07 is `F(x) = exp(-a x^2) cos(b x)` with `a = b/2pi`, `b = 14`.
It is manifestly sign-changing — as Corollary 2.4 requires. Every element of
`D^o` must oscillate.

**Theorem 2.5 (requirement (R) is proved).**
Let `c` be an effective class, `c != 0`. Then `s(c, F_v) != 0` and
`s(c, F_h) != 0`. In particular the disjunction pre-registered as **(R)** in
113_08 section 4 holds, with both alternatives true rather than one.

*Proof.* Choose a nonnegative representative `f != 0`. By 113_08 formula (2.2),
`s(f, F_v) = f^(1)` and `s(f, F_h) = f^(0)`, both strictly positive by
Theorem 2.2. Pairings are constant on classes modulo `rad I_d`, since the
radical is the annihilator of the descended form (113_09 Thm 2.4(3)). `[]`

**(R) is therefore no longer a requirement.** It is a theorem, and an easy one.
This is not surprising in hindsight: on a surface, (R) is the statement that a
nonzero effective divisor has positive intersection with an ample class, which
is Nakai–Moishezon in its trivial direction. What the proof above shows is that
our `H` really does behave like an ample class: pairing against it is
integration against a strictly positive measure.

---

## 3. The polarization is effective: `H = 2 Phi`

Theorem 2.2 would be vacuous if the effective cone were empty or missed every
class we care about. It is not, and the polarization itself is in it —
via a classical object.

**Definition 3.1 (Riemann's `Phi`).** For real `u`, with `psi(y) = sum_{n>=1} e^{-pi n^2 y}`,

```
        Phi(u) = 2 pi sum_{n>=1} ( 2 pi n^4 e^{9u/2} - 3 n^2 e^{5u/2} ) exp(-pi n^2 e^{2u}).
```

Equivalently, with `y = e^{2u}`,  `Phi(u) = 4 y^{3/4} d/dy [ y^{3/2} psi'(y) ]`.

**Facts (classical, quoted).** `Phi` is even, real-analytic, strictly positive
on all of `R`, decays doubly exponentially (`Phi(u) = O(exp(-pi e^{2|u|}))`),
and

```
        Xi(t) = xi(1/2 + it) = int_R Phi(u) e^{iut} du .
```

Positivity and evenness are due to Pólya; they are the standing hypotheses of
the de Bruijn–Newman literature, where `Phi` is the kernel whose Fourier
transform is `Xi`. Both are proved from the theta functional equation, and
neither uses any information about the location of the zeros. The verifier
checks the identity `Xi = Fourier(Phi)` against an independent mpmath
evaluation of `xi` to `2e-12`, checks evenness of the series to 10 digits, and
checks strict positivity on a grid of 81 points in `[0,8]` — in mpmath, since
`Phi(4) ~ 1.8e-4058` underflows double precision.

**Theorem 3.2 (`H` is effective, explicitly).** The polarization class `H` is
represented by the strictly positive function

```
        f_H(u) = 2 u^{-1/2} Phi(log u) > 0     for all u in (0, inf),
```

that is, `F_H = 2 Phi`. Consequently `h^0(H) > 0`, and `deg(H) = 2` is the
total mass `4 int_R Phi(x) cosh(x/2) dx`.

*Proof.* `H^(s) = 2 xi(s)`, so `F^_H(it) = 2 Xi(t) = 2 int Phi(u) e^{iut} du`.
Fourier inversion in the convention of 113_05 gives `F_H = 2 Phi`. Positivity
is the quoted fact; membership in `D_theta` for every `theta > 0` is 113_09
Lemma 1.2 (or directly: `Phi` decays doubly exponentially, which beats every
`e^{-theta|x|}`). `[]`

Numerically (verifier section C, mpmath dps=30):

```
        int Phi dx            = 0.497120778188314   = xi(1/2)
        int Phi e^{+x/2} dx   = 0.500000000000000   = xi(1)
        int Phi e^{-x/2} dx   = 0.500000000000000   = xi(0)
        deg(H) = 4 int Phi cosh(x/2) dx = 2.000000000000000
```

**Proposition 3.3 (the rulings are *not* effective at these representatives).**
`F_v = Phi + 2 Phi'` and `F_h = Phi - 2 Phi'`, and both change sign:
`F_v(0) = +0.8934` while `F_v(0.2) = -4.178`. Hence neither `f_v` nor `f_h` is
nonnegative.

*Proof.* `f^_v(1/2 + it) = (1 - 2it) Xi(t)`; multiplication by `-2it` corresponds
to `+2 d/dx` in the convention of 113_05, giving `F_v = Phi + 2 Phi'`. The same
computation with `f^_h(1/2+it) = (1 + 2it) Xi(t)` gives `F_h = Phi - 2 Phi'`,
which is `F_v(-x)` since `Phi` is even — consistent with 113_09's finding that
the involution swaps `f_v` and `f_h`. Sign change: `Phi'(0) = 0` by evenness so
`F_v(0) = Phi(0) > 0`, while `Phi'/Phi -> -inf` as `x -> +inf` (doubly
exponential decay), so `F_v < 0` eventually. The numerical values are computed
in verifier section D. `[]`

This is a genuine open point, not a defect: effectivity is a property of the
*class*, and `f_v` might still be equivalent modulo `rad I_d` to a nonnegative
function. Theorem 2.5 does not care (it needs only that *if* the class is
effective *then* the pairings are nonzero, and `deg f_v = 1 > 0` is consistent
with effectivity). But it is worth recording that the two rulings of the
"quadric" are not visibly effective, while their sum is. On a genuine quadric
surface both rulings *are* effective. That asymmetry is data about how far the
analogy actually reaches, and 113_13 should return to it.

---

## 4. Row (d) is now one statement — and that statement is RH

**Definition 4.1.** Pre-register, as the sharpened form of (E):

> **(E^o)** For every real `f` in `D^o` with `s(f,f) > 0`, the class of `f` or
> the class of `-f` in `D / rad I_d` is effective.

This is (E) of 113_08 section 4 restricted to `D^o`, which is the only place
the index argument uses it.

**Theorem 4.2 (the reduction).** `(E^o) ==> RH`.

*Proof.* Suppose RH fails. By 113_07 Prop 4.1 — equivalently Connes' criterion
(17), whose side conditions are exactly `f^(0) = f^(1) = 0` by 113_08 Thm 1.1 —
there is a real `f` in `D^o` with `s(f,f) > 0`. By (E^o), `[f]` or `[-f]` is
effective, so by Theorem 2.2 its degree is strictly positive. But `f` is in
`D^o`, so `deg(f) = f^(0) + f^(1) = 0`, and `deg(-f) = 0`; degree is constant on
classes by Theorem 1.3. Contradiction. Hence no such `f` exists, i.e.
`s(f,f) <= 0` on `D^o`, which is RH. `[]`

**Theorem 4.3 (the candid converse).** `RH ==> (E^o)`. Hence
**`(E^o) <==> RH`**.

*Proof.* Under RH there is no real `f` in `D^o` with `s(f,f) > 0` (113_07 Prop
4.1 again), so (E^o) is vacuously true. `[]`

So (E^o) is not a weakening of RH; it is RH rewritten in the vocabulary of rows
(d3)–(d5). This must be said plainly, because the opposite reading is the
natural one and it is wrong: **proving (E^o) is not a step towards RH that is
easier than RH.** 113_08 reached the same verdict about Connes' Lemma 2.1 — the
lemma is arithmetically empty — and the same verdict holds here. The index
engine has now been assembled completely, and every screw in it turns freely.

What is *not* empty, and is the entire content of the programme's bet, is this:
**on an algebraic surface, (E) is a theorem, and its proof is Riemann–Roch.**
There, `D^2 > 0` implies `chi(nD) = chi(O) + (n^2 D^2 - n D.K)/2` grows without
bound, so `h^0(nD) + h^0(K - nD) -> inf`, and since `nD` and `K - nD` cannot
both be effective for large `n`, one of `±nD` is effective. That argument
converts a *numerical* hypothesis (`D^2 > 0`) into a *geometric* conclusion
(a section exists), and it is the only known mechanism that does so. Row (d)
is closed the moment that mechanism exists over `Spec Z`. That is why (d3) and
(d4) — `h^0` and Serre duality — are the bottleneck, and it is why they are
113_11 and 113_12.

The value of this file is that it removes everything else. Before it, row (d)
needed (E) and (R) and a degree map and a proof that the polarization was a
real class. Now:

```
        row (d)  <==>  (E^o)  <==>  build enough Riemann-Roch over Spec Z
                                    to convert  s(f,f) > 0  into a section.
```

---

## 5. Obstruction O1: the divisor group is a vector space

The Riemann–Roch mechanism quoted above has a load-bearing feature that our
setting does not have, and it should be registered now rather than discovered
in 113_13.

**Proposition 5.1.** For every real `n > 0` and every `f` in `D`, the class
`[n f]` is effective if and only if `[f]` is effective.

*Proof.* `rad I_d` is a linear subspace and `f >= 0 <==> n f >= 0`. If
`f + g >= 0` with `g` in the radical, then `n f + n g >= 0` with `n g` in the
radical, and conversely. `[]`

**Obstruction O1.** `D / rad I_d` is a complex vector space, and the effective
cone is a genuine cone (stable under positive scaling). Therefore
`h^0(nD) = h^0(D)` for all `n > 0`, and the classical route to (E) — *let `n`
grow until the quadratic term in `chi(nD)` dominates* — proves nothing here.
There is no `n` to grow into. Any construction of `h^0` over `Spec Z` that
recovers (E^o) must therefore either

- **(i)** produce a divisor group with a genuine discrete (lattice) component,
  so that "`n` large" has content — this is what Arakelov theory does, and it is
  what Connes–Consani's Riemann–Roch for `Spec Z` does in its own way, since
  there `deg` is real-valued while `dim H^0` is integer-valued (the minimum
  cardinality of a generating set); or
- **(ii)** prove effectivity at `n = 1` directly, which classical surface theory
  never does.

Route (i) is the one to try, and it is a positive reason to read Connes–Consani
2022 Thm 5.3 closely in 113_12: the integrality of their `dim H^0` against the
real-valuedness of their `deg` is precisely the discrete/continuous mismatch
that O1 says we need. Route (ii) should be treated as refuted until someone
exhibits a mechanism.

**Refutation conditions, pre-registered.**

- **R5.** If a proposed `h^0` on `D / rad` is again a function of the class in a
  complex vector space with a scaling-stable effective cone, then by
  Proposition 5.1 it cannot deliver (E^o) by any growth argument, and 113_11
  must report that rather than proceed.
- **R6.** If a proposed `h^0` is defined using `s(f,f)`, or using the zeros, or
  using a positive part of a Weil form, it is circular (this is R1 of 113_08,
  restated for the sharpened target).
- **R7.** If a proposed `h^0` gives `h^0(H) = 0`, it is wrong: Theorem 3.2 proves
  `H` is effective, explicitly and unconditionally. This is a real, cheap,
  non-vacuous acceptance test — the first one row (d3) has ever had.
- **R8.** If a proposed `h^0` makes some nonzero element of `rad I_d` effective,
  it is wrong by Corollary 2.3.

R7 and R8 are new and worth the file on their own: until now no candidate `h^0`
could be tested against anything.

---

## 6. Scope

**Proved here (unconditionally, no zeros used in any definition):**

- Thm 1.2 — the degree map `deg(f) = s(f,H) = f^(0)+f^(1) = int f(u)(1+u) d^x u
  = 2 int F cosh(x/2) dx`, three closed forms.
- Thm 1.3 — `deg(rad I_d) = 0`; `deg` descends to `D / rad I_d`.
- Prop 1.4 — `deg H = 2`, `deg f_v = deg f_h = 1`, `deg(f_v - f_h) = deg w = 0`.
- Prop 1.5 — `D^o` is strictly contained in `ker deg`.
- Thm 2.2 — `f >= 0`, `f != 0` implies `f^(0) > 0`, `f^(1) > 0`, `deg f > 0`.
- Cor 2.3 — `rad I_d` contains no nonzero nonnegative function.
- Cor 2.4 — `D^o` contains no nonzero nonnegative function; every element of
  `D^o` changes sign.
- **Thm 2.5 — requirement (R) of 113_08 section 4, proved.**
- Thm 3.2 — `H` is effective: `F_H = 2 Phi > 0`, `f_H(u) = 2u^{-1/2}Phi(log u)`.
- Prop 3.3 — `F_v = Phi + 2Phi'` and `F_h = Phi - 2Phi'` both change sign.
- Thm 4.2 — `(E^o) ==> RH`.
- Thm 4.3 — `RH ==> (E^o)`; so `(E^o) <==> RH`.
- Prop 5.1 / O1 — `h^0(nD) = h^0(D)`; the growth route to (E^o) is unavailable.

**Read from source (quoted, not re-proved):**

- `Phi` is even and strictly positive on `R` (Pólya; standard in the
  de Bruijn–Newman literature), and `Xi(t) = int Phi(u)e^{iut}du` (Titchmarsh
  §10.1). The Fourier identity and the evenness are re-verified numerically
  below; the positivity is checked on a grid but quoted as a theorem.
- `xi(0) = xi(1) = 1/2`, `xi(1-s) = xi(s)`, `xi` entire — 113_09 section A.
- Connes' criterion (17) and its identification with 113_07 Prop 4.1 — 113_08
  Thm 1.1 and Thm 1.2.

**Verified numerically:**

- The three closed forms of `deg` agree to 18 significant digits on three
  Gaussian probes (`a = 0.5, 1.0, 2.0`).
- `deg H = 2`, `deg f_v = deg f_h = 1`, `deg w = 0`, exactly.
- `Phi` against Fourier inversion of an independently computed `xi`: agreement
  to `2e-12` at `x = 0`, `3e-12` at `x = 0.2`, degrading to `1e-10` at `x = 0.6`
  only because `Phi(0.6) ~ 1.5e-2` and the quadrature noise floor is `~2e-12`.
- Evenness of the `Phi` series: 25 digits at `u = 1`, and at `u = 1.5` **8
  digits at dps=30 rising to 69 digits at dps=90**. The second is a measured
  confirmation of catastrophic cancellation, not of evenness: at `u = -1.5` the
  largest term of the series is `~8e-2` while the sum is `~1.3e-23`, so ~22
  digits are lost and dps=30 can retain only ~8. Both are recorded in the
  verifier so that the dps=30 number is not misread as a defect.
- The separate diagnosis that the raw series is unusable for `u < -1`:
  `exp(-pi n^2 e^{2u})` needs `n >~ e^{-u}` terms, so `u = -4` needs `n ~ 55`
  and `N = 60` returns `-1.334`, the wrong sign. The verifier evaluates at `|u|`
  and records this failure explicitly rather than silently avoiding it.
- `Phi > 0` at 81 points of `[0,8]` in mpmath (`Phi(4) = 1.8e-4058`,
  `Phi(8) = 1.4e-12123982`; both underflow float64).
- `int Phi = xi(1/2) = 0.497120778188314`; `int Phi e^{±x/2} = 1/2`;
  `deg H = 4 int Phi cosh(x/2) = 2.000000000000000`.
- `F_v` changes sign (`+0.893` at `0`, `-4.178` at `0.2`); `W = Phi'' - Phi/4`
  changes sign (`-16.95` at `0`, `+6.78` at `0.5`), as Cor 2.3 requires.
- Formula (2.2) of 113_08 re-checked in two coordinate models — all zeros on the
  line, and zeros off the line with multiplicities `2,3` — on 50 random vectors
  each, exact agreement: the zero block never contributes to `s(x,F_v)` or
  `s(x,F_h)`, so `deg` is independent of the zero data.
- Negative controls: (i) the wrong `x`-space weight `(1+e^x)` gives `4.0483`
  against the correct `3.7735`, so form three of Thm 1.2 has discriminating
  power; (ii) an off-line-zero model with a witness on a **mirrored** pair of
  slots gives `s(x,x) = +4` with `deg(x) = 0` — exactly the configuration Thm 4.2
  rules out — while the same witness with all zeros on the line gives
  `s(x,x) = -2`; (iii) `s(f_v,F_v) = 0` while `deg(f_v) = 1`, so `deg` is not the
  `F_v` pairing; (iv) `Phi > 0` also on a 10x finer grid.
- A control that failed first and was fixed: placing the witness on two
  *unrelated* zeros makes every term of the zero sum vanish and returns
  `s(x,x) = 0`, testing nothing. The verifier now selects the partner index from
  the mirror permutation rather than by hand.

**Not established:**

- **(E^o)** — and Theorem 4.3 shows it is exactly as hard as RH. Row (d) is
  reduced to it and to nothing else.
- Whether the ruling classes `[f_v]`, `[f_h]` are effective modulo `rad I_d`.
  Their representatives `Phi ± 2Phi'` are not nonnegative (Prop 3.3). On a
  quadric surface both rulings are effective; here it is open.
- Any construction of `h^0` as a *dimension* (a number, not a Boolean). This
  file only defines `h^0(c) > 0`. That suffices for (E^o) and (R), but not for
  Riemann–Roch, which needs `chi` and hence an actual integer. 113_11.
- Serre duality, `K`, and the trace map. 113_12.
- Whether `D / rad I_d` can be given the discrete component O1 says it needs.
  This is the single most important open question this file produces.
- Rows (a) and (b) remain where 113_09 section 5 left them: `P` is *defined* as
  the `xi`-ideal, with the burden moved onto the construction of the space and
  the correspondences. 108_38 Thm 3.1 and 108_50/52/53 are untouched.

---

## 7. Verifier

`113_10_the_degree_map_and_the_effective_cone.py` — sections:

- **A** the three closed forms of `deg`, on Gaussian probes, mpmath dps=30
- **B** `deg` on `H`, `f_v`, `f_h`, `f_v - f_h`, `w`; linearity; `deg(rad) = 0`
- **C** `Phi`: evenness, Fourier identity against `xi`, positivity, moments
- **D** `F_v = Phi + 2Phi'`, `F_h = Phi - 2Phi'`, `W = Phi'' - Phi/4`: sign changes
- **E** Thm 2.2 and Cors 2.3, 2.4 on explicit nonnegative and sign-changing data
- **F** Thm 2.5, requirement (R), in the coordinate model
- **G** Prop 5.1 (scaling invariance of effectivity) and negative controls

Status: **51 checks, 51 pass, exit 0, `VERDICT: ALL CHECKS PASS`.**
