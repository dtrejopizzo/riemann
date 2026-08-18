# 113.14 — The two residual analytic gaps, (SEP) and (INT), are both discharged

> **What this file does.** Phase 113 ended 113_13 with exactly two undischarged
> analytic lemmas, both recorded candidly at the time:
>
> - **(SEP)** — 113_12 section 3: the zero block of the intersection form was
>   proved nondegenerate only in the finite coordinate model, because "division
>   by `(s - rho')` is not an operation in the convolution algebra, and no
>   element of `D` realising it has been exhibited."
> - **(INT)** — 113_07 Proposition 4.1, the `(<=)` direction: "the
>   interpolation ... needs `D^o` to be rich enough to prescribe two values and
>   control the rest; that is a Paley–Wiener style statement about `D`, **and it
>   is not proved here**."
>
> Both are discharged here, by the same observation: `D` is defined by a
> **growth condition**, not by closure under any algebraic operation, so to
> exhibit an element one has only to exhibit a transform with the right decay.
> Multiplying by `xi` supplies that decay (113_09 Lemma 1.2); the content of
> this file is that *dividing* by a factor that `xi` already contains does not
> destroy it.
>
> (SEP) turns out to have been proved already, inside the proof of 113_09
> Theorem 2.2, and 113_12 simply failed to notice. (INT) is new, and its witness
> is written down in closed form.

```
LEMMA 1.1'   xi * (meromorphic v, poles cancelled by zeros of xi)  IS IN  D
THEOREM 2.1  (SEP) DISCHARGED -- d4 is unconditionally complete
THEOREM 3.3  (INT) DISCHARGED -- the real witness, in closed form
COROLLARY    113_07 Prop 4.1, 113_10 Thm 4.2/4.3, 113_12 Thm 4.1 are now
             unconditional statements about D, not about a coordinate model
STILL OPEN   Ansatz A; (E^o); row (d); RH
```

---

## 0. Why the gaps were there, and why they are cheap

Both gaps have the same shape. Something needs to be *in* `D`, and the natural
formula for it involves a division. In an algebra of functions closed under
convolution there is no division, so the formula looks illegitimate.

The answer is that nothing needs to be legitimate *as an operation*. `D` is

$$\mathcal D=\bigcup_{\theta>3/2}\mathcal D_\theta,\qquad
f\in\mathcal D_\theta\iff F(x)=e^{x/2}f(e^x)\in\mathcal S_\theta,$$

a class defined by decay of the balanced profile (113_07 Def 1.3). Membership
is checked by 113_09 Lemma 1.1, which asks only for a holomorphic transform
with rapid decay on vertical lines of a strip. A quotient is an element of `D`
as soon as it *is* a function with that decay — how one writes it is irrelevant.

The only thing to prove is that the quotient stays holomorphic, and that is
exactly what "the pole sits on a zero of `xi` of at least that order" means.

---

## 1. The membership lemma, in the form actually needed

113_09 Lemma 1.2 is stated for `Phi = p * xi * v` with `v` **holomorphic** and
polynomially bounded on the strip. Its own zero-slot argument then applies it to
`chi(s)/(s - rho_0)^{m}`, where the middle factor has a pole. The lemma as
stated does not cover that. It is a citation slip, not a mathematical one, and
the repaired statement is:

> ### Lemma 1.1′ (membership with cancelled poles)
> Let `theta' > 0`, let `E` be a finite subset of the closed strip
> `|Re s - 1/2| <= theta'`, and let `v` be meromorphic there with poles
> contained in `E` and polynomially bounded outside a fixed neighbourhood of
> `E`. Suppose the product `Phi := xi * v` extends holomorphically across `E`
> (i.e. `ord_rho v >= -m_rho` at each `rho` in `E`, and `v` has no pole off the
> zero set of `xi`). Then for every `theta > 0` there is `f` in `D_theta` with
> `f^ = Phi`; in particular `f` lies in `D`.

**Proof.** `Phi` is holomorphic on the closed strip by hypothesis. Fix a
vertical line `Re s = sigma` in the strip and split it at `|t| = T_0`, chosen so
that `E` lies in `|t| < T_0`. On the compact part `Phi` is continuous, hence
bounded. On `|t| >= T_0`, Stirling gives
`|xi(sigma + it)| = O(|t|^{A(sigma)} e^{-pi|t|/4})` (113_09 Lemma 1.2's
estimate, unchanged) and `|v(sigma + it)| = O(|t|^B)` by hypothesis, so
`|Phi| = O(|t|^{A+B} e^{-pi|t|/4})`. Hence
`\int |Phi(sigma+it)| (1+|t|)^N dt < oo` for every `N` and every `sigma` in the
strip, which is precisely the hypothesis of 113_09 Lemma 1.1. That lemma
returns `f` in `D_theta` with `f^ = Phi`, for the given `theta`; since
`theta'` was arbitrary, this holds for every `theta`. `[]`

**Numerically** (section A of the verifier): `xi` has a simple zero at the first
zero ordinate, `Phi = chi/(s - rho_1)` has the stable finite value
`rho(rho-1) xi'(rho) = -0.276600 i` there across `eps = 1e-6, 1e-10, 1e-14`
(spread below `1e-4`), while the control `chi(s)/(s - 1/2)` — a pole *not* on a
zero of `xi` — grows as `1.243e5, 1.243e9, 1.243e13`. The strip integrals
`\int |Phi| (1+|t|)^4 dt` converge on both edges of `|Re s - 1/2| <= 1.6`
(`= 1.733e5`), with the measured tail ratio matching `exp(-pi Delta t/4)`.

**Remark 1.2 (the source rule).** Lemma 1.1′ mentions the zeros of `xi` only
through "the poles of `v` sit where `xi` vanishes, to no greater order". It
never locates a zero, never uses `Re rho = 1/2`, and reads identically if RH is
false. This is 113_09 Remark 2.3's standard, applied again.

---

## 2. (SEP) is discharged, and d4 is unconditionally complete

> ### Theorem 2.1 (the separating family lives in `D`)
> For every zero `rho` of `xi`, with multiplicity `m_rho`, the function
> $$\widehat{y_\rho}(s):=\frac{s(s-1)\,\xi(s)}{(s-\rho)^{m_\rho}}$$
> is the Mellin transform of an element `y_rho` of `D`, and its coordinates on
> `S = {0, 1} u Z` are
> $$\widehat{y_\rho}(0)=\widehat{y_\rho}(1)=0,\qquad
> \widehat{y_\rho}(\sigma)=0\ (\sigma\in\mathcal Z,\ \sigma\ne\rho),\qquad
> \widehat{y_\rho}(\rho)=\frac{\rho(\rho-1)\,\xi^{(m_\rho)}(\rho)}{m_\rho!}\ne0.$$
> Consequently, for every `x` in `D`,
> $$\mathfrak s(x,\,y_{\rho'})=-m_\rho\,\widehat x(\rho)\,
> \overline{\widehat{y_{\rho'}}(\rho')},$$
> which is nonzero whenever `x^(rho) != 0`. **The zero block of `s` is
> nondegenerate inside `D`, unconditionally.**

**Proof.** Membership is Lemma 1.1′ with `v(s) = s(s-1)/(s-rho)^{m_rho}`: the
only pole is at `rho`, of order `m_rho`, exactly cancelled because `xi` vanishes
there to order `m_rho`; `v` is rational, hence polynomially bounded away from
its pole. The coordinate values are immediate — `xi(0), xi(1) = 1/2 != 0` so the
factor `s(s-1)` supplies the two polar zeros, and `xi` supplies a zero of order
`m_sigma >= 1` at every other `sigma`. The pairing formula then has a single
surviving term, since `s(x,y) = x^(0)conj(y^(1)) + x^(1)conj(y^(0)) - sum_sigma
m_sigma x^(sigma) conj(y^(sigma'))` and `y^(sigma') != 0` only for
`sigma' = rho'`, i.e. `sigma = rho`. `[]`

**This was already done.** The proof of 113_09 Theorem 2.2 constructs exactly
`g_{rho_0}(s) = s(s-1) xi(s) / (s - rho_0)^{m_{rho_0}}` and uses it for the same
purpose. 113_12 section 3 recorded (SEP) as open anyway. The record was wrong;
the correction is issued in section 5 below. What is genuinely new here is only
Lemma 1.1′, which is what makes 113_09's own citation of its Lemma 1.2 valid.

> ### Corollary 2.2 (d4 is complete without assuming RH)
> Serre duality in the Frobenius dictionary of 113_12 is nondegeneracy of the
> trace form. The polar block is nondegenerate by 113_12 Theorem 3.2
> (unconditional, via `s(x,F_v) = x^(1)`, `s(x,F_h) = x^(0)`); the zero block is
> nondegenerate by Theorem 2.1. Hence `rad(s) = rad I_d` on `D`, and 113_12
> Proposition 3.3 — which reached the same conclusion *from RH* — is no longer
> needed.

**Numerically** (section B): for the first three zeros, `y_k = chi/(s - rho_k)`
has exactly one nonzero coordinate on the truncated `S`, at `rho_k`, with
values `0.276600, 0.007849, 0.000792`; all 24 pairings `s(e_j, y_k)` are nonzero
exactly where predicted and zero elsewhere.

---

## 3. (INT) is discharged: the witness, in closed form

113_07 Proposition 4.1 needs: *if some zero lies off the critical line, there is
a **real** `f` in `D^o` with `s(f,f) > 0`.* The obstacle was interpolation —
prescribe two values at a mirror pair while controlling the infinitely many
other zeros. Theorem 2.1's construction solves the control problem for free:
divide `chi` by the whole orbit, and every other coordinate is *exactly* zero.
What is left is a two-real-parameter rotation, and that is Lemma 3.2.

Throughout, `u := s - 1/2`, `^*` is the involution `g^*(s) = conj(g(1 - conj s))`
of 113_12 Prop 2.1, and "real" means `f^(conj s) = conj(f^(s))`, i.e. `f` is a
real-valued function on `(0, oo)`.

> ### Lemma 3.1 (real and `*`-symmetric multipliers are the even ones)
> Let `P(s) = sum_k c_k u^k` be a polynomial. Then `P` is real iff every `c_k`
> is real, and `P^* = P` iff `c_k = 0` for every odd `k`. Hence `P` is both real
> and `*`-symmetric iff `P` is an **even polynomial in `u` with real
> coefficients**.

**Proof.** `P(conj s) = sum conj(c_k) conj(u)^k`, so reality is `c_k = conj(c_k)`.
For the involution, `1 - conj(s) - 1/2 = -conj(u)`, so
`P^*(s) = conj(sum c_k (-conj u)^k) = sum conj(c_k) (-1)^k u^k`; with real `c_k`
this is `P` iff the odd coefficients vanish. `[]`

> ### Lemma 3.2 (two real parameters suffice to rotate)
> Let `u_0` in `C` with `Im(u_0^2) != 0`, and let `A != 0` in `C`. Then there
> exist **real** `c_0, c_2` with `(c_0 + c_2 u_0^2) A = i`.

**Proof.** `Im(u_0^2) != 0` makes `{1, u_0^2}` an `R`-basis of `C`, so
`c_0 + c_2 u_0^2` ranges over all of `C` as `(c_0, c_2)` ranges over `R^2`;
take the preimage of `i/A`. Explicitly, with `z = i/A`,
`c_2 = Im z / Im(u_0^2)` and `c_0 = Re z - c_2 Re(u_0^2)`. `[]`

Note where the hypothesis bites: `u_0 = rho_0 - 1/2 = (sigma - 1/2) + it` has
`Im(u_0^2) = 2(sigma - 1/2)t`, which is nonzero **exactly when the zero is off
the critical line and not real**. On the line the span collapses to `R` and no
rotation is possible — that is not an accident of the method, it is RH.

> ### Theorem 3.3 ((INT), the real witness)
> Suppose `xi` has a zero `rho_0` with `Re rho_0 != 1/2`, of multiplicity `m`.
> Then there is a **real** `f` in `D^o = {f in D : f^(0) = f^(1) = 0}` with
> `s(f,f) > 0`.
>
> **Case 1 (`rho_0` not real).** Let `Q = {rho_1, rho_2, rho_3, rho_4} =
> {rho_0, conj rho_0, 1 - conj rho_0, 1 - rho_0}`, four distinct zeros each of
> multiplicity `m`. Put
> $$\widehat f(s)=\bigl(c_0+c_2\,(s-\tfrac12)^2\bigr)\,
> \frac{s(s-1)\,\xi(s)}{\prod_{j=1}^{4}(s-\rho_j)^{m}},$$
> with `c_0, c_2` the real constants of Lemma 3.2 applied to `u_0 = rho_0 - 1/2`
> and `A = A_1 :=` the value at `rho_1` of `s(s-1) xi(s) / prod_j (s-rho_j)^m`.
> Then `s(f,f) = 4m|a_1|^2 > 0`.
>
> **Case 2 (`rho_0` real, so `sigma != 1/2`, `t = 0`).** Use the pair
> `{rho_0, 1-rho_0}` in the denominator and `P = 1` or `P = u`, whichever makes
> `a_1 a_3 < 0`; one of the two always does.

**Proof.** *Membership.* The denominator's poles sit on zeros of `xi` of exactly
the stated orders (the four points are distinct: `rho_0 = conj rho_0` is case 2,
`rho_0 = 1 - conj rho_0` is `Re rho_0 = 1/2`, `rho_0 = 1 - rho_0` is
`rho_0 = 1/2`), so Lemma 1.1′ applies and `f` is in `D`. The multiplicities
agree around the orbit because `xi(1-s) = xi(s)` and `xi(conj s) = conj xi(s)`.

*`D^o` and degree.* `xi(0) = xi(1) = 1/2 != 0` and the denominator is nonzero at
`0, 1`, so the factor `s(s-1)` gives `f^(0) = f^(1) = 0`, hence `f` is in `D^o`
and `deg f = f^(0) + f^(1) = 0` (113_10 Thm 1.2).

*Reality.* `prod_j (s - rho_j)^m` has real coefficients, because `Q` is stable
under conjugation; `s(s-1) xi(s)` is real; `P` is real by Lemma 3.1. A quotient
of real functions is real.

*The coordinates.* `f^` vanishes at every zero outside `Q` (order `m_sigma >= 1`
from `xi`, denominator nonzero) and at `0, 1`. So the sum defining `s(f,f)` has
exactly four terms.

*The values.* Write `g^ = s(s-1) xi(s) / prod_j (s-rho_j)^m` and `A_j = g^(rho_j)`,
all nonzero. `Q` is `*`-stable, so `g^* = g^` and therefore
`A_3 = g^(1 - conj rho_1) = conj(A_1)`. With `P` real and even, Lemma 3.1 gives
`P^* = P`, and `rho_3 - 1/2 = -conj(u_0)` gives `P(rho_3) = conj(P(rho_1))`.
Hence `a_3 = conj(a_1)`, and by reality `a_2 = conj(a_1)`, `a_4 = conj(a_3) = a_1`.

*The sign.* The mirror `rho -> rho' = 1 - conj rho` pairs `rho_1 <-> rho_3` and
`rho_2 <-> rho_4`, so
$$\mathfrak s(f,f)=-m\bigl[a_1\overline{a_3}+a_3\overline{a_1}
+a_2\overline{a_4}+a_4\overline{a_2}\bigr]
=-4m\,\mathrm{Re}\bigl(a_1\overline{a_3}\bigr)=-4m\,\mathrm{Re}(a_1^2).$$
Lemma 3.2 makes `a_1 = P(rho_1) A_1 = i`, so `Re(a_1^2) = -1` and
`s(f,f) = 4m > 0`. Scaling `f` by `lambda > 0` scales this by `lambda^2`, so the
normalisation `a_1 = i` is free.

*Case 2.* Now `rho_0` and `1 - rho_0` are the only points of the orbit,
`rho_0' = 1 - rho_0`, and `s(f,f) = -2m Re(a_1 conj(a_3)) = -2m a_1 a_3` since
both values are real. `P = 1` gives `a_1 a_3 = A_1 A_3`; `P = u` gives
`a_1 a_3 = -(rho_0 - 1/2)^2 A_1 A_3`, the opposite sign. `A_1 A_3 != 0`, so one
of the two is negative and that `f` has `s(f,f) > 0`. (`P = u` is real and odd,
so `f` is still real; it is not `*`-symmetric, which is not required.) `[]`

**Numerically** (section C). Lemma 3.2 is verified on 200 deterministic
`(u_0, A)` pairs, `max |a_1 - i| = 2.03e-30`. The full construction is then run
end to end against a **surrogate**: `Xi_S(s) = prod_j (s - rho_j) * exp((s-1/2)^2)`
with the quadruple `0.8 +- 6i, 0.2 +- 6i` — an entire function that is real,
`*`-symmetric, Gaussian-decaying on vertical lines, and has its zeros off the
critical line, i.e. a legitimate stand-in for a `xi` violating RH. Measured:
`f^(0) = f^(1) = 0` exactly, reality to `0.0e0`, `a_1 = i`, `a_3 = -i`,
`s(f,f) = +4.000000000000` against the predicted `4m = 4`. Case 2 is verified on
the real pair `{0.8, 0.2}`: even `P` gives `-0.0613`, odd `P` gives `+0.0055` —
exactly one parity wins, as the proof says.

**The control that matters** (section C3): the *same* two-parameter family, run
against the **true** `xi` at its first zero, which is on the line, gives
`s(f,f) <= 0` for all 441 real `(c_0, c_2)` on a grid, with the maximum `0`
attained only at `c = 0`. The construction cannot manufacture positivity where
there is none; it converts an off-line zero into positivity and nothing else.

> ### Corollary 3.4 (what stops being conditional)
> 1. **113_07 Proposition 4.1** becomes a theorem of `D`:
>    `RH <=> s(f,f) <= 0 for all real f in D^o`. Both directions, no
>    interpolation hypothesis.
> 2. **113_10 Theorems 4.2 and 4.3** — `(E^o) <=> RH` — no longer quote an
>    unproved lemma. The witness has `deg = 0` and `s(f,f) > 0`, which is
>    exactly what the contradiction with 113_10 Theorem 2.2 needs.
> 3. **113_12 Theorem 4.1** — Hodge index `<=>` RH — now holds in `D` itself.
>    Previously the `(1) => (2)` direction was proved in the finite coordinate
>    model, with the `D`-level witness missing; it is Theorem 3.3.
> 4. **113_12 section 3** — d4 — is unconditionally complete, by Corollary 2.2.

---

## 4. What this does not do, stated as plainly as possible

The two gaps were the last analytic conditions in the phase. Closing them does
**not** move the programme closer to RH, and the reason is structural: every
statement they were blocking is an *equivalence* with RH, not an implication
towards it.

- Before: "Hodge index `<=>` RH, modulo an interpolation lemma."
- After: "Hodge index `<=>` RH."

The second is a cleaner sentence and an equally distant one. What the phase has
built is a complete, correct, zero-free dictionary in which Weil's row (d) is
*exactly* the Riemann Hypothesis — no side conditions, no renormalisation, no
undischarged trace assumption, no missing test functions. The remaining
statement, `(E^o)` / Ansatz A, is RH-hard by 113_10 Theorem 4.2, and the three
obstructions O1, O2, O3 of 113_10 and 113_13 say that no lattice, no
discretisation and no coercive estimate will supply it.

There is one candid gain beyond tidiness. Theorem 3.3 gives, for the first time
in the programme, an **explicit closed-form counterexample generator**: any
off-line zero produces, by a formula one can write on a line, a real Schwartz
datum violating Weil positivity. That is the object every "positivity implies
RH" argument needs and none of the earlier files had. It also gives R21 below a
sharp target.

### Pre-registered refutation conditions

- **R21.** If anyone exhibits a real `f` in `D^o` with `s(f,f) > 0` *without*
  assuming an off-line zero — i.e. computed from primes, as in 113_13 section 2
  — RH is false and the programme is over. 113_13 measured four such `f` and
  found `s(f,f) <= 0` in all four to `4e-15`.
- **R22.** If a future file claims a gap that is already proved elsewhere in the
  corpus (as 113_12 did with (SEP)), the citation audit in the verifier of that
  file must fail. Two textual audits are now run mechanically in section B.
- **R23.** If Theorem 3.3's witness is ever found to lie outside `D` — e.g. if
  the definition of `D` is later tightened beyond 113_07 Def 1.3 — Corollary 3.4
  reverts, and 113_07 Prop 4.1 `(<=)` returns to conditional status.

---

## 5. Correction ledger

| # | target | correction |
|---|---|---|
| 1 | 113_09, proof of Thm 2.2, zero slots | cites Lemma 1.2, which requires `v` holomorphic, for a `v` with a pole. The step is correct; the citation is not. Replace by Lemma 1.1′ of this file. |
| 2 | 113_12 section 3, "The gap (SEP)" | **wrong.** The element was exhibited in 113_09's proof of Thm 2.2. (SEP) was never open. Theorem 2.1 here states it properly. |
| 3 | 113_12 Prop 3.3 | still true, now redundant: nondegeneracy of the zero block does not need RH. |
| 4 | 113_07 Prop 4.1, `(<=)` | the interpolation hypothesis is discharged by Theorem 3.3; the proposition is a theorem. |
| 5 | 113_12 Thm 4.1, `(1) => (2)` | upgrade from "coordinate model" to "`D`", by Theorem 3.3. |

---

## 6. Scope

**Proved here.** Lemma 1.1′ (membership with cancelled poles); Theorem 2.1
((SEP), the separating family in `D`) and Corollary 2.2 (d4 unconditional);
Lemma 3.1 (real + `*`-symmetric = even real); Lemma 3.2 (the two-parameter
rotation); Theorem 3.3 ((INT), both cases) and Corollary 3.4.

**Read from source, not re-proved.** 113_07 Def 1.3 (`D_theta`, `D`), Lemma 1.4
(convolution `->` product), Prop 4.1; 113_09 Lemma 1.1 (the membership
criterion), Lemma 1.2 (the Stirling estimate for `xi` on vertical lines),
Thm 2.2, Remark 2.3; 113_10 Thm 1.2 (`deg`), Thm 2.2 (effective `=>` `deg > 0`),
Thm 4.2/4.3; 113_12 Prop 2.1 (the involution), Thm 3.2, Thm 4.1. Classical:
Stirling, the functional equation `xi(1-s) = xi(s)`, `xi(conj s) = conj xi(s)`,
`xi(0) = xi(1) = 1/2`.

**Verified numerically.** Simplicity of the first zero and the finite value of
`chi/(s-rho_1)` there; the strip integrals and the `exp(-pi|t|/4)` tail; the
coordinates of `y_1, y_2, y_3` and all 24 separating pairings; Lemma 3.2 on 200
data points; the whole of Theorem 3.3 case 1 against a surrogate with a
prescribed off-line quadruple, and case 2 against a real pair; the on-line
control over a 441-point grid; two textual citation audits.

**Not established.** That the surrogate `Xi_S` is `xi` — it is not, and no claim
is made that `xi` has an off-line zero. Theorem 3.3 is a conditional
construction and its numerical exercise is an exercise of the *algebra*, not
evidence about `xi`. Also not established, and unchanged by this file:
`(E^o)`, Ansatz A, `chi(O)`, row (d), RH.

**On the source rule.** No object of the programme is defined here using a zero
of `xi`. Sections A and B evaluate `xi` at computed zeros purely to *check*
statements proved without them (113_09 Remark 2.3's standard). Theorem 3.3
constructs from a *hypothesised* off-line zero inside a contrapositive; that is
how the direction `not RH => not positivity` must work, and it is the same use
113_07 Prop 4.1 already made. `xi` itself is used freely, as the rule permits.

---

## 7. Verifier

`113_14_the_two_analytic_gaps.py` — 38 checks, all passing, exit 0.
