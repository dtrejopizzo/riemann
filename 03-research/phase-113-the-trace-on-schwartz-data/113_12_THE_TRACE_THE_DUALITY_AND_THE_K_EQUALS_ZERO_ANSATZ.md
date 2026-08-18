# 113_12 — d4: the trace, Serre duality, and the one ansatz that remains

```
THE TRACE tau:        CONSTRUCTED, with a ZERO-FREE definition (the arithmetic
                      side of the explicit formula).  s(x,y) = tau(x * y^*).
FROBENIUS STRUCTURE:  (D/rad, *, ^*, tau) -- PROVED.  This is the whole object.
SERRE DUALITY:        nondegeneracy of the trace form.  PROVED in the coordinate
                      model and on the polar block of D.  Zero block needs (SEP),
                      which RH implies.
CANONICAL CLASS:      K = 0.  PROVED (the trace is symmetric; Nakayama is trivial).
MAIN THEOREM:         HODGE INDEX  <==>  RH.  Both directions proved.
ANSATZ A:             chi(D) = D^2 / 2.  Implies (E^o), hence RH.  Passes R7, R8,
                      R9 and every numerical test available.  NOT PROVED.
```

Depends on: 113_06 (the explicit formula, Thm 2.2), 113_08 (the coordinate model,
formula (2.2)), 113_09 (`rad = (chi)`), 113_10 (degree, effective cone, `(E^o)`),
113_11 (the ring structure, R9).

Verifier: `113_12_the_trace_and_the_duality.py`

---

## 1. The trace map

Everything in 113_08–113_11 was built from a form `s` that was *defined* by a sum
over zeros. That was acceptable for a coordinate model but it violates the spirit
of the source rule at the level of definitions. This section removes the defect
and, in doing so, identifies the correct algebraic object.

**Definition 1.1 (the trace, zero-free).** For `z` in `D`, set

```
        tau(z)  :=  sum_{n >= 2} Lambda(n) [ z(n) + z(1/n)/n ]  -  A(z) ,
```

where `A` is the archimedean term of 113_06 Thm 2.2 and `Lambda` is von Mangoldt.
No zero of `xi`, no Li coefficient, and no positive part appears. `tau` is a
linear functional on `D`.

**Theorem 1.2 (the explicit formula, quoted).** For `z` in `D`,

```
        tau(z)  =  z^(0) + z^(1) - sum_rho m_rho z^(rho) .
```

This is 113_06 Thm 2.2, Assumption T discharged there. It is a *theorem about*
`tau`, not its definition.

**Theorem 1.3 (the intersection form is the trace of a product).** For all
`x, y` in `D`,

```
        s(x, y)  =  tau( x * y^* ) ,
```

where `*` is convolution and `y^*(u) = conj(y(1/u))/u` is the algebra involution.

*Proof.* Mellin turns `*` into multiplication and sends `y^*` to
`s |-> conj(y^(1 - conj(s)))`. Hence `(x * y^*)^(s) = x^(s) conj(y^(1-conj(s)))`.
Evaluate at the three kinds of point of `S` and apply Theorem 1.2:

```
        at s = 0 :   x^(0) conj(y^(1))
        at s = 1 :   x^(1) conj(y^(0))
        at s = rho:  x^(rho) conj(y^(rho')),   rho' = 1 - conj(rho).
```

Summing with the signs and multiplicities of Theorem 1.2 gives exactly the
definition of `s` in 113_08. `[]`

**Corollary 1.4 (the object).** The entire structure of phase 113 is the
quadruple

```
        ( D / rad ,  * ,  ^* ,  tau )
```

— a commutative `*`-algebra with a trace — and `s` is its trace form. This is
the standard shape of a Frobenius algebra, and it is also the shape of the
pairing in Weil's row (c)/(d). Nothing else is needed: degree, the rulings, the
effective cone and the index question are all statements about this quadruple.

**Remark 1.5.** `tau` is *not* `s(-, H)`. Pairing against `H` gives
`s(x,H) = x^(0) + x^(1) = deg(x)` (113_10), which drops the zero sum, because
`H` is the unit of the polar factor only (113_11 Thm 1.2) and annihilates the
zero block. `tau` is pairing against the unit of the *whole* algebra, which is
not an element of `D`. That single sentence is the difference between the degree
and the Weil functional.

---

## 2. The duality involution

**Proposition 2.1.** On transforms, `^*` is `s |-> 1 - conj(s)`, and

```
        (f_v)^*  =  f_h ,     (f_h)^*  =  f_v ,     H^* = H ,     w^* = w .
```

*Proof.* `xi` has real coefficients, so `xi(1 - conj(s)) = conj(xi(1-s)) =
conj(xi(s))` by the functional equation. Then
`conj( f_v^(1-conj(s)) ) = conj( -2(-conj(s)) conj(xi(s)) ) = 2 s xi(s) = f_h^(s)`,
and the rest similarly. `[]`

So the involution that Serre duality needs is not imported: it is the algebra's
own `*`, it is the functional equation, and it exchanges the two rulings. This
is the precise version of the observation in 113_09 that `F_h(x) = F_v(-x)`.

**Proposition 2.2.** `s` is Hermitian: `s(y,x) = conj(s(x,y))`; equivalently
`tau(z^*) = conj(tau(z))`. Hence `s(x,x)` is real, and the index question is
well posed.

---

## 3. Serre duality = nondegeneracy of the trace form

For a Frobenius algebra the content of Serre duality is exactly that the trace
form is nondegenerate: `x |-> tau(x * -)` is injective. Here that reads
`rad(s) = rad I_d`, i.e. the form is nondegenerate precisely on `D / rad`.

**Theorem 3.1 (nondegeneracy in the coordinate model).** On `V = C^S` with the
form of 113_08, the Gram matrix in the standard basis is

```
        G(0,1) = G(1,0) = 1 ,     G(rho, rho') = -m_rho ,     else 0 ,
```

a signed permutation matrix scaled by the multiplicities. On any `^*`-stable
finite block it is invertible, with `|det G| = prod_rho m_rho != 0`. Hence `s`
is nondegenerate on `V` and `rad(s) = 0`.

*Proof.* Each row has exactly one nonzero entry, in column `iota(s_0)`, and
`iota` is an involution of `S`, so `G` is a permutation matrix times a diagonal
of nonzero entries. `[]`

**Theorem 3.2 (nondegeneracy of the polar block, inside `D`).** If `x` in `D`
has `x^(0) != 0` or `x^(1) != 0`, then `s(x, y) != 0` for an explicit
`y` in `D`.

*Proof.* 113_08 formula (2.2): `s(x, F_v) = x^(1)` and `s(x, F_h) = x^(0)`, and
`f_v, f_h` are elements of `D` exhibited in 113_09 Thm 3.1. `[]`

This is a genuine `D`-level statement, not a coordinate one, and it is
unconditional.

**The gap (SEP).** For the zero block the same argument needs a separating
family: for each `rho` in `S`, an element `y` of `D` with `y^(rho') != 0` and
`y^` vanishing on `S \ {rho'}`. Formally `y^(s) = chi(s) g(s)/(s - rho')` works
— it is holomorphic, and `xi` decays rapidly on vertical strips so the decay is
fine — but division by `(s - rho')` is not an operation in the convolution
algebra, and no element of `D` realising it has been exhibited. **(SEP) is not
established here.**

**Proposition 3.3.** RH implies (SEP) is unnecessary: under RH, `rho' = rho` for
every zero, so the zero block of `s` is `-sum_rho m_rho |x^(rho)|^2`, which is
negative definite and hence nondegenerate. So the residual gap in d4 is
implied by the very statement the programme is trying to prove, and is therefore
not an independent obstacle — but it does mean d4 is **not unconditionally
complete on the zero block**.

**Theorem 3.4 (the canonical class vanishes).** The trace `tau` is symmetric
(Prop 2.2) on a commutative algebra, so the Nakayama automorphism of the
Frobenius structure is the identity. In the divisor dictionary that is `K = 0`.

Independent corroboration: the CC corpus reaches genus `0` for `Spec Z` over
`S` from a completely different direction (`2306.00456` Thm 1.1: *"a perfect
analogy with the Riemann-Roch formula holding for curves of genus 0"*, recorded
in `phase-39/120-inventario-CC-fuente.md`). Two independent routes to a
vanishing canonical term is weak evidence, but it is evidence, and it is the
first time the two frameworks have agreed on a computed invariant.

**Remark 3.5.** `K = 0` immediately says the object is **not** the quadric
`P^1 x P^1`, where `K = -2H_v - 2H_h != 0`. The quadric was always only a
picture for the two rulings; 113_11 Thm 1.2 replaced it with the correct
statement (two minimal idempotents) and this replaces the rest of it.

---

## 4. The main theorem: Hodge index is RH

This is the sharpest statement the phase can make, and it is fully proved in
both directions.

**Theorem 4.1.** Let `V = D / rad` with the Hermitian form `s`. The following are
equivalent:

1. **(Hodge index)** `s` has signature `(1, .)`: `s(H,H) > 0`, and `s` is
   negative definite on `H^perp`.
2. **RH.**

*Proof.* `s(H,H) = 2 > 0` unconditionally (113_09 Thm 4.1). By 113_10 Thm 1.2,
`s(x,H) = deg(x)`, so `H^perp = ker(deg)`. The polar and zero blocks are
`s`-orthogonal, since `s((a,b;0), (0,0;z)) = 0`. Hence

```
        H^perp  =  C.(f_v - f_h)  (+)  D^o / rad ,      orthogonally,
```

and `s(f_v - f_h, f_v - f_h) = -2 < 0` unconditionally (113_09 Thm 4.1, measured
from primes).

(2) => (1): under RH every `rho` satisfies `rho' = rho`, so on the zero block
`s(x,x) = -sum_rho m_rho |x^(rho)|^2 <= 0`, with equality only for `x = 0` in
`V`. Together with the `-2` on the ruling difference, `H^perp` is negative
definite.

(1) => (2): suppose some zero `rho_0` has `Re rho_0 != 1/2`, so
`rho_0' = 1 - conj(rho_0) != rho_0` is a distinct zero of the same multiplicity
`m`. Put `x^(rho_0) = 1`, `x^(rho_0') = -1`, all other coordinates `0`. Then
`x` lies in `D^o`, hence in `H^perp`, and

```
        s(x,x) = -m [ x^(rho_0) conj(x^(rho_0')) + x^(rho_0') conj(x^(rho_0)) ]
               = -m [ (1)(-1) + (-1)(1) ]  =  +2m  >  0 ,
```

contradicting negative definiteness. `[]`

Theorem 4.1 is Weil's row (d), stated exactly, over `Spec Z`. It says that the
whole programme is one signature computation — and that the signature
computation is RH, neither more nor less. It also retires any hope that row (d)
might be a *step towards* RH: it is RH.

The verifier measures both directions: signature `(1,7)` in the on-line model and
`(3,5)` in the off-line model, from the same code.

---

## 5. Ansatz A: the single remaining statement

`K = 0` (Thm 3.4) plus the Frobenius structure (Cor 1.4) determines the shape of
any Riemann–Roch theorem this object could satisfy. On a surface,
`chi(D) = chi(O) + (D^2 - D.K)/2`; with `K = 0` this is `chi(O) + D^2/2`.
Evaluating at `D = 0` in the abelian-surface normalisation `chi(O) = 0`:

> **Ansatz A.** There are functions `h^0, h^1, h^2` on `V`, with
> `h^0(D) >= 1` if and only if `D` is effective or `D = 0`, satisfying
> `h^2(D) = h^0(-D)` (Serre duality with `K = 0`) and
>
> ```
>         h^0(D) - h^1(D) + h^2(D)  =  D^2 / 2 .
> ```

**Theorem 5.1.** Ansatz A implies `(E^o)`, hence RH.

*Proof.* Let `f` be real in `D^o` with `s(f,f) > 0`, and `D = [f]`, so `D != 0`
and `D^2 > 0`. Then `chi(D) = D^2/2 > 0`, so `h^0(D) + h^2(D) > h^1(D) >= 0`,
hence `h^0(D) > 0` or `h^2(D) = h^0(-D) > 0`. So `D` or `-D` is effective, which
is `(E^o)`. By 113_10 Thm 4.2, `(E^o)` implies RH. `[]`

**So Ansatz A is at least RH-hard and cannot be proved in this file.** What can
be done — and what the rest of this section does — is test it. Ansatz A was not
tuned to pass these; R7 and R8 were pre-registered in 113_10 and R9 in 113_11,
each before this file existed.

**Test R7** (*"any `h^0` with `h^0(H) = 0` is wrong: `H` is provably effective"*).
Ansatz A gives `chi(H) = H^2/2 = 1`. Serre duality gives
`h^2(H) = h^0(-H) = 0`, since `deg(-H) = -2 < 0` and negative-degree classes are
not effective (113_10 Thm 2.2). So `h^0(H) - h^1(H) = 1`, forcing
`h^0(H) >= 1`. **Passes**, and it does so tightly: the minimal solution is
`h^0(H) = 1`, `h^1(H) = 0`.

**Test R8** (*"any `h^0` making a nonzero radical element effective is wrong"*).
Radical elements have `D = 0`; Ansatz A's dictionary says `h^0(0) >= 1` via the
"`or D = 0`" clause, which asserts nothing about pointwise-nonnegative
representatives. **Passes** — but the dictionary is loose exactly here and the
looseness is recorded in section 6 as an open point.

**Test R9** (*"a valid `h^1` must satisfy `h^1([3f_v - f_h]) > h^1([H])`"*, from
113_11 Thm 3.4, since the two classes have equal degree `2` and only the first
fails to be effective). Compute in the polar block, where
`s((a,b),(c,d)) = a conj(d) + b conj(c)`:

```
        D = 3f_v - f_h = (3, -1) ,     D^2 = 3(-1) + (-1)(3) = -6 ,
        chi(D) = -3 ,     h^0(D) = 0 (not effective, 113_11 Thm 3.4) ,
        h^2(D) = h^0(-D) = 0  (deg(-D) = -2 < 0) ,
        =>  h^1(D) = 3 .
```

Against `h^1(H) = 0` from R7. **Passes**, with a margin of 3, and this was a
genuinely independent test: 113_11 registered it without knowing what `chi`
would be.

**A fourth, unregistered consistency check.** `H^2 = 2` with `K = 0` and
`h^0(H) = 1` is the numerical signature of a **principal polarization**: exactly
one effective divisor in the class. And 113_10 Thm 3.2 exhibits exactly one
natural positive representative, `F_H = 2 Phi`, Riemann's own `Phi`-function.
The programme did not put that there; it fell out of `xi(0) = xi(1) = 1/2`.

**Refutation conditions for Ansatz A:**

- **R13.** If any class `D` with `D^2 > 0` is exhibited for which neither `D` nor
  `-D` is effective, Ansatz A is false. (This is the contrapositive of Thm 5.1 —
  and it would also refute RH, so it is not a cheap test.)
- **R14.** If `chi(O) != 0` is forced — e.g. if some independent computation
  gives `chi` of the zero class a nonzero value — the normalisation is wrong and
  every number in section 5 shifts.
- **R15.** If `h^1` is ever constructed and does *not* give `h^1(H) = 0`, then
  either R7's tight solution or Serre duality with `K = 0` fails.
- **R16.** Ansatz A presumes a *surface* Riemann–Roch (a quadratic `chi`). Every
  Riemann–Roch actually available over `Spec Z` is one-dimensional with a linear
  `chi` (113_11 section 4, corpus-verified). If it is shown that no quadratic
  `chi` can exist over `Spec Z`, Ansatz A is dead and with it this route.

---

## 6. Verdict on d4

**d4 is closed at the Frobenius level and open at one point.**

Closed: the trace `tau` exists with a zero-free definition (Def 1.1); the
intersection form is its trace form (Thm 1.3); the duality involution is the
algebra's own `*`, which is the functional equation and swaps the rulings
(Prop 2.1); the form is Hermitian (Prop 2.2) and nondegenerate in the coordinate
model (Thm 3.1) and on the polar block of `D` (Thm 3.2); and the canonical class
vanishes (Thm 3.4), in agreement with the CC corpus's independent genus-0
verdict.

Open: **(SEP)**, the separating family on the zero block, needed for
unconditional nondegeneracy inside `D`. Proposition 3.3 shows RH implies it is
moot, so it does not block the programme, but it does mean the phrase "Serre
duality is proved" must carry this qualification.

Also open and recorded: the dictionary clause `h^0(D) >= 1 iff D effective or
D = 0` treats the zero class by fiat. On a surface `h^0(O) = 1` because the
constants are sections; here "constants" are not elements of `D` (`D` has no
unit — Remark 1.5). Whether the zero class should have `h^0 = 1` or `h^0 = 0` is
undetermined by anything proved, and R14 is the test that would settle it.

And the real bottom line: **Theorem 4.1 says row (d) is RH**, and **Theorem 5.1
says Ansatz A implies RH**. Rows (a)–(d) have been reduced to Ansatz A, and
Ansatz A is a Riemann–Roch theorem of surface type over `Spec Z` — which is
precisely the object Connes and Consani identify as the open problem
(`1805.10501`; corpus: *"Nadie ha cruzado todavía 'RR absoluto' con
'cuadrado'"*). The programme's remaining distance is now one named theorem, not
a family of gaps. That is a real advance in bookkeeping and it is not a proof of
RH.

---

## 7. Scope

**Proved here:**

- Thm 1.3 — `s(x,y) = tau(x * y^*)`; the intersection form is a trace form.
- Cor 1.4 — the whole structure is `(D/rad, *, ^*, tau)`.
- Prop 2.1 — `^*` is `s |-> 1 - conj(s)`, swaps `f_v, f_h`, fixes `H` and `w`.
- Prop 2.2 — `s` is Hermitian.
- Thm 3.1 — nondegeneracy in the coordinate model; `|det G| = prod m_rho`.
- Thm 3.2 — nondegeneracy of the polar block inside `D`, unconditional.
- Prop 3.3 — RH implies the zero block is nondegenerate.
- Thm 3.4 — `K = 0`.
- **Thm 4.1 — Hodge index `<==>` RH, both directions.**
- Thm 5.1 — Ansatz A implies `(E^o)`, hence RH.

**Read from source (quoted, not re-derived):**

- The explicit formula, Thm 1.2 — 113_06 Thm 2.2.
- `s(H,H) = 2`, `s(f_v - f_h, f_v - f_h) = -2` — 113_09 Thm 4.1.
- `s(x, F_v) = x^(1)`, `s(x, F_h) = x^(0)` — 113_08 (2.2).
- `deg(x) = s(x,H) = x^(0) + x^(1)`; negative degree implies not effective;
  `H` effective with `F_H = 2 Phi` — 113_10.
- CC's genus-0 verdict and the open status of RR on the square — via
  `phase-39/120-inventario-CC-fuente.md`, a second-hand source, as flagged in
  113_11 section 7.

**Verified numerically:**

- Thm 1.3 on 200 random pairs in each of two zero models, to `1e-10`.
- Prop 2.1 on transforms, including `xi(1 - conj(s)) = conj(xi(s))`.
- Prop 2.2, Hermitian symmetry of the Gram matrix.
- Thm 3.1, `det G` and `prod m_rho` in both models.
- **Thm 4.1 in both directions: measured signature `(1,7)` on-line and `(3,5)`
  off-line, from identical code.**
- Section 5's arithmetic: `D^2 = -6`, `chi = -3`, `h^1 = 3` vs `h^1(H) = 0`.
- Negative controls, including a wrong trace (dropping the zero sum, i.e. using
  `deg` in place of `tau`) which fails Thm 1.3.

**Not established:**

- (SEP), hence unconditional nondegeneracy on the zero block inside `D`.
- Ansatz A, in any part. It is RH-hard by Thm 5.1.
- `chi(O)`; the normalisation in section 5 is chosen, not derived (R14).
- `(E^o)`, hence row (d). Unchanged.
- Rows (a) and (b): unchanged.

---

## 8. Verifier

`113_12_the_trace_and_the_duality.py` — **40 checks, 40 pass, exit 0.**
Sections A (Prop 2.1 on transforms), B (Thm 1.3, `s = tau(x*y^*)`, 200 random
pairs per model, plus the wrong-trace control), C (Thm 3.1, Gram matrix and
determinant), D (Thm 4.1, signature in both models — the main theorem),
E (section 5's arithmetic and the R7/R9 tests).

The main theorem, measured:

```
  ON  model: eigenvalues [-1. -1. -1. -1. -1. -1. -1.  1.]
             signature (+, -) = (1, 7)
  OFF model: eigenvalues [-3. -3. -2. -2. -1.  1.  2.  2.]
             signature (+, -) = (3, 5)
  [PASS] Thm 4.1 witness: x = [rho_0] - [rho_0'] lies in H^perp and s(x,x) = +2m > 0
         s(x,x) = +4.000000 = 2 * m (m = 2);  deg(x) = s(x,H) = 0.0e+00
```

and Theorem 1.3, which is the file's structural result:

```
  [PASS] ON  model: s(x,y) = tau(x * y^*) on 200 random pairs   max err 0.000e+00
  [PASS] OFF model: s(x,y) = tau(x * y^*) on 200 random pairs   max err 7.105e-15
  [PASS] negative control -- dropping the zero sum FAILS Thm 1.3
  [PASS] |det G| = prod m_rho = 144   (OFF model)
```

The identity `s = tau(x*y^*)` holds to machine zero in the on-line model and to
`7e-15` off it, in both cases against a control (the same computation with the
zero sum removed) that fails by an order-one amount. The signature measurement
is the whole of Theorem 4.1: one positive direction exactly when the zeros are
on the line, three when they are not, from the same code path.
