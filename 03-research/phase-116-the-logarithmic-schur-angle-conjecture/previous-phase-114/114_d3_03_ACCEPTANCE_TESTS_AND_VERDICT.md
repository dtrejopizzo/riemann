# 114_d3_03 — row (d), lens 3: R7, R8, R9 run against the imported `h^0`, and the verdict

```
R7  (h^0(H) != 0)          PASSED, and NOT vacuously.  For the imported theta
                           h^0 one has h^0_X(L) = 0 exactly when f_*L = 0, so R7
                           is the sharp demand that the realisation send H to a
                           class with a global section.  It becomes a condition
                           ON THE REALISATION, i.e. part of Gap G-1.
R8  (rad not effective)    ***FIRES***, unconditionally, against the RAW import:
                           h^0_X(O_X) = log theta(1) = 0.0829015 > 0, so the
                           imported h^0 declares the zero class - the class of
                           every element of rad - effective, contradicting
                           113_10 Cor 2.3.  REPAIRABLE, and the repair is
                           forced: subtract the threshold.
R9  (h^1(3f_v-f_h) >       PASSED with an explicit margin of 4, which is exactly
     h^1(H))               ((H,H) - (D2,D2))/2.  R9 is passed BY THE SELF-
                           INTERSECTION, not by the degree (both degrees are 2).
                           Conditional only on |T(H) - T(3f_v - f_h)| < 4.
OBSTRUCTION O1             DEFEATED by the import.  113_10 Prop 5.1 said the
                           corpus effective cone is scale-stable so "let n grow"
                           is empty; the imported h^0 restores the growth on the
                           target and Prop 5.1 transports the conclusion back.
                           This is the mechanism row (d) has been missing.
VERDICT ON THE LENS        The import is REAL and the mechanism WORKS, but the
                           transport is CIRCULAR:  Theorem 6.5 below proves that
                           the existence of ANY additive map iota from D^o into
                           ANY Lorentzian space with (iota c, iota c) >= s(c,c)
                           is EQUIVALENT to RH.  Not merely isometric maps -
                           merely DOMINATING ones.  Every arithmetic surface is
                           Lorentzian (arithmetic Hodge index).  So no linear
                           import can close row (d) without assuming RH.
                           Row (d) is NOT closed.  R16 does not fire.
```

Depends on: `114_d3_01` (imported index theorems; Thm 2.5, Thm 4.5, Gaps G-1..G-3),
`114_d3_02` (R16; the quadratic `chi` and the torsion term `T`, Gaps G-4, G-5),
`113_10` (Def 2.1 effectivity, Thm 2.2, Cor 2.3, Cor 2.4, Thm 3.2, Prop 5.1 and
Obstruction O1, R7, R8), `113_11` (Thm 3.4 and R9), `113_12` (Thm 4.1, Ansatz A,
Thm 5.1), `107_241` (Thm 3.1 blockwise signature).

Verifier: `114_d3_03_acceptance_tests.py` — 43 checks, all pass, run in section 8.

---

## 1. The three tests, quoted exactly

From 113_10 section 5:

> - **R7.** If a proposed `h^0` gives `h^0(H) = 0`, it is wrong: Theorem 3.2 proves
>   `H` is effective, explicitly and unconditionally. This is a real, cheap,
>   non-vacuous acceptance test — the first one row (d3) has ever had.
> - **R8.** If a proposed `h^0` makes some nonzero element of `rad I_d` effective,
>   it is wrong by Corollary 2.3.

From 113_11 section 3:

> - **R9.** A candidate `h^1` must satisfy `h^1([3f_v - f_h]) > h^1([H])`, since the
>   two classes have equal degree and only the first fails to be effective.

The objects they test are fixed by 113_10 Def 2.1 (`h^0(c) > 0` iff `c` has a
nonnegative nonzero representative), 113_10 Cor 2.3 (`rad I_d ∩ {f >= 0} = {0}`)
and 113_10 Thm 3.2 (`H` is represented by `2 Phi > 0`).

---

## 2. The object under test

**Definition 2.1 (the imported `h^0`).** For a Hermitian coherent `O`-module
`F` over `O = Z`,

```
        h^0_O(F) = log sum_{x in F} e^{-pi ||x||^2} ,
```

and for a Hermitian line bundle `L` on an arithmetic surface `f : X -> Spec Z`,
`h^0_X(L) = h^0_O(f_* L)` (Wei He section 2.2.2, quoted verbatim in
`114_d3_02` section 3). `h^1_X`, `h^2_X`, `chi_X` are as quoted there.

**Standing hypotheses used in this file, all named.**

- **(H0)** `X` is a regular projective arithmetic surface over `Spec Z` with
  `H^0(X, O_X) = Z` (the standard normalisation for a surface with geometrically
  connected generic fibre).
- **(H3)** `omega_X = O_X` in `Pic-hat(X)` (the `K = 0` transport; Gap G-5).
- **(Hι)** a realisation `iota` of Gap G-1 exists, additive and positively
  homogeneous.

Nothing in sections 3–5 uses **(Hι)** beyond additivity; section 6 uses it
explicitly and then destroys it.

**Circularity of Definition 2.1: CLEAN.** `h^0_O` is built from a lattice and a
metric. It does not mention `xi`, any zero, `s(f,f)`, or any positive part of a
Weil form. It also **passes R6** (113_10) and **passes R5**: it is *not* a
function on a complex vector space with a scale-stable effective set — see
section 6.1 — which is exactly the property Obstruction O1 demands.

---

## 3. R7

**Theorem 3.1 (R7 is passed, and is not vacuous).** For a Hermitian coherent
`Z`-module `F`,

```
        h^0_O(F) = 0    <==>    F = 0  as a lattice,
        h^0_O(F) > 0    for every F of positive rank or with torsion.
```

Consequently, for a Hermitian line bundle `L` on `X`,

```
        h^0_X(L) = 0    <==>    f_* L = 0    <==>    H^0(X, L) = 0 .
```

*Proof.* The theta sum always contains the term `x = 0`, contributing `1`; every
other term is strictly positive. So the sum is `>= 1` with equality iff the
underlying set is `{0}`. Take `log`. `[]`

So R7 is **not** automatically satisfied by the import — it is exactly the
demand

```
        H^0(X, iota(H)) != 0 ,
```

i.e. *the realisation must send the polarisation class to a line bundle with an
candid global section*. That is a nontrivial, checkable condition on `iota`, and
it is the correct arithmetic transport of 113_10 Thm 3.2 (`H` is represented by
the strictly positive function `2 Phi`).

**Corollary 3.2 (threshold form).** After the repair forced in section 4, R7
strengthens to `h^0_X(iota H) > h^0_X(O_X) = log theta(1) = 0.0829015200311...`,
which in the rank-1 model (`f_* iota(H)` a Hermitian line bundle over `Z` of
arithmetic degree `a`) is **exactly** `a > 0`, by strict monotonicity of
`a |-> h^0_Z(a)`.

**Verdict on R7: PASSED, conditionally on Gap G-1, non-vacuously.**

---

## 4. R8 — this one fires

**Theorem 4.1 (R8 fires against the raw import).** Assume (H0). Every element
of `rad I_d` has class `0` in `D / rad I_d`, and every additive realisation
sends it to the trivial Hermitian line bundle `O_X`. Then

```
        h^0_X(O_X) = h^0_O(Z) = log theta(1) = 0.0829015200311... > 0 ,
```

whereas 113_10 Cor 2.3 requires `h^0` to vanish there. Hence the raw imported
`h^0` **violates R8**, for every realisation and every surface.

*Proof.* By (H0), `f_* O_X = O_Z`, the rank-1 lattice `Z` with `||1|| = 1` for a
normalised measure; `h^0_O(Z) = log sum_n e^{-pi n^2} = log theta(1) > 0`.
Changing the normalisation of the measure shifts `deg-hat f_* O_X` by a
constant, and `h^0_Z` is a strictly increasing **strictly positive** function of
that degree (Theorem 3.1), so the value stays `> 0` for *every* normalisation —
only its size changes. 113_10 Cor 2.3 says no nonzero element of `rad I_d` is
nonnegative, so `h^0([0]) = 0` in 113_10's own sense. `[]`

Two readings of R8 are possible and both give the same verdict: read at the
level of classes (as above), the zero class is wrongly declared effective; read
at the level of functions, the import assigns a positive value to the class
containing the radical generator `w = Phi'' - Phi/4`, which changes sign
(`-16.95` at `0`, `+6.78` at `0.5`, 113_10 verifier).

**Proposition 4.2 (the repair, and it is forced).** Define

```
        h^0_thr(L) := h^0_X(L) - h^0_X(O_X) ,
        L effective  :<==>  h^0_thr(L) > 0 .
```

Then `h^0_thr(O_X) = 0` exactly, R8 is passed, and R7 becomes Corollary 3.2.
The threshold is *pinned*, not chosen: R8 forces any admissible threshold `t` to
satisfy `t >= h^0_X(O_X)` (otherwise the zero class is effective), while
exactness of the degree test at the boundary — `h^0_thr > 0` iff
`deg-hat f_* L > 0`, Corollary 3.2 — forces `t <= h^0_Z(0) = h^0_X(O_X)`.
Hence `t = h^0_X(O_X)`.

**Remark 4.3 (a real, if small, scalp).** In `114_d3_02` I had first used the
hand-written threshold `log(1 + 2e^{-pi})`, the "two shortest vectors" value.
That is **wrong**: it lies `6.42e-6` below `h^0_Z(0)` and declares effective an
interval `(-1.28e-5, 0)` of strictly negative degrees. The only threshold for
which the dictionary is exact is `h^0_X(O_X)` itself. Both files now use it.

**Verdict on R8: FIRED against the raw import; PASSED after the forced
thresholding.** This is the first time in the corpus that a pre-registered
refutation condition has actually fired against an imported object, and the
repair it forces is the reason section 5 and 6 are stated with a threshold.

---

## 5. R9

**Theorem 5.1 (the imported `h^1` passes R9 with margin `4`).** Assume (H0),
(H3), (Hι), and write `D2 = 3 f_v - f_h`, `T(L) = chi_X(O_X) +
(1/2) log(det Delta_{O_infinity} / det Delta_{L_infinity})` as in `114_d3_02`
Def 5.1. Then

```
   h^1_X(iota D2) - h^1_X(iota H)  =  ( (H,H) - (D2,D2) ) / 2  +  ( T(H) - T(D2) )  +  E
                                   =  4  +  ( T(H) - T(D2) )  +  E ,
   E := h^0_X(iota D2) + h^0_X(-iota D2) - h^0_X(iota H) - h^0_X(-iota H) .
```

In particular R9 holds whenever

```
        h^0_X(iota H) + h^0_X(-iota H)  <  4 + T(H) - T(D2) .              (R9-suf)
```

*Proof.* `chi_X = h^0 - h^1 + h^2` gives `h^1 = h^0 + h^2 - chi`. By (H3),
`h^2_X(L) = h^0_X(omega_X (x) L^v) = h^0_X(-L)`. By the imported Riemann–Roch
(`114_d3_02` Thm 3.2) with `omega_X = 0`, `chi_X(L) = (L,L)/2 + T(L)`. Subtract
the two expressions at `iota D2` and `iota H`, and use the isometry on these two
classes: `(iota H, iota H) = s(H,H) = 2` and `(iota D2, iota D2) = s(D2,D2) =
-6` (both re-derived in the verifier from `s(f_v,f_h) = 1`,
`s(f_v,f_v) = s(f_h,f_h) = 0`). For (R9-suf) drop the two nonnegative terms
`h^0_X(iota D2), h^0_X(-iota D2) >= 0`. `[]`

**Corollary 5.2 (the rank-1 model).** If `f_* iota(H)` and `f_*(-iota(H))` are
Hermitian line bundles over `Z` and `deg-hat f_* iota(H) in [0,2]`, then
`h^0_X(iota H) + h^0_X(-iota H) <= 2.0000...` (Bost's bound at `deg = -2` is
`8.1e-75`), so R9 holds whenever `T(H) - T(D2) > -2`; and the exact criterion is
`T(H) - T(D2) > -4` up to `1e-74`.

**Remark 5.3 (why this is the *right* pass).** The margin is
`((H,H) - (D2,D2))/2`, purely a self-intersection difference; the two degrees are
equal (`deg H = deg D2 = 2`), exactly as 113_11 Thm 3.4 demands. So the imported
`h^1` separates `[H]` from `[3f_v - f_h]` for the same reason the corpus does:
the second class is far from the light cone on the wrong side. This is a genuine
structural agreement, not a coincidence of normalisations.

**Remark 5.4 (what R9 does and does not constrain).** `h^1(D2) - h^1(H)` is
invariant under `T -> T + const`. So **R9 constrains only the variation of the
analytic torsion**, while Gap G-4 constrains its absolute value. They are
independent conditions, and R9 is by far the cheaper one.

**Verdict on R9: PASSED, conditionally on `|T(H) - T(D2)| < 4` (Gap G-6).**

---

## 6. Obstruction O1, the mechanism, and the circularity that kills it

### 6.1 O1 is defeated

113_10 Prop 5.1: `[nf]` is effective iff `[f]` is, for every real `n > 0`; hence
`h^0_corpus(nD) = h^0_corpus(D)` and "let `n` grow" has no content inside `D`.
Obstruction O1 asks for "a divisor group with a genuine discrete (lattice)
component, so that `n` large has content — this is what Arakelov theory does".

**Lemma 6.1 (`h^1_X >= 0`).** From Wei He's definition, `h^1_X(L)` is the sum of
two theta invariants `h^0_O(...) >= 0` and of `(1/2)(deg-hat det H^1(X,L)_t +
deg-hat det H^1(X, omega_X (x) L^v)_t)`, each of which is `log #T >= 0` for a
finite module `T` under the standard convention that makes `deg-hat` additive in
short exact sequences. Hence `h^1_X >= 0`. `[]`

**Theorem 6.2 (the transport mechanism).** Assume (H0), (H3), and let
`c in D^o` be such that

- **(H4')** there is `L in Pic-hat(X)` with `(L, L) = s(c,c) > 0`;
- **(H5)** `T(nL) >= -n^2 (L,L)/4 - C` for some constant `C` and all `n >= 1`;
- **(H1)** for every `n >= 1`: `h^0_X(nL) > h^0_X(O_X)` implies `nc` effective,
  and `h^0_X(-nL) > h^0_X(O_X)` implies `-nc` effective.

Then `c` or `-c` is effective in `D / rad I_d`.

*Proof.* `chi_X(nL) = n^2 (L,L)/2 + T(nL) >= n^2 (L,L)/4 - C -> +infinity`. By
Lemma 6.1 and `chi = h^0 - h^1 + h^2`, `h^0_X(nL) + h^2_X(nL) >= chi_X(nL)`;
by (H3) `h^2_X(nL) = h^0_X(-nL)`. So `max(h^0_X(nL), h^0_X(-nL)) >=
chi_X(nL)/2 -> infinity`, and for `n` large one of them exceeds the fixed number
`h^0_X(O_X)`. By (H1), `nc` or `-nc` is effective. By 113_10 Prop 5.1, `c` or
`-c` is effective. `[]`

**Corollary 6.3.** If (H4'), (H5), (H1) hold for every `c in D^o` with
`s(c,c) > 0`, then (E^o) holds, and hence RH by the 113_12 chain.

That is a complete proof of RH from four labelled hypotheses, and it shows O1 is
**defeated**: the discrete/continuous mismatch the import supplies is exactly
what "let `n` grow" needed, and Prop 5.1 — previously an obstruction — becomes
the *transport* that carries the conclusion back to `n = 1`.

### 6.2 And then it collapses

**Theorem 6.4 (the conclusion of (H1) is always false).** By 113_10 Cor 2.4, no
class in `D^o` is effective, and `D^o` is a linear subspace, so `-c in D^o` too.
Hence the conclusion of (H1) is false for every `c in D^o`, and (H1) is
*equivalent* to the statement

```
        h^0_X(n iota c) <= h^0_X(O_X)  and  h^0_X(-n iota c) <= h^0_X(O_X)
        for every c in D^o and every n >= 1.                              (NOEFF)
```

(NOEFF) is a genuine, non-vacuous constraint on `iota`: its quantifier is not
emptied by RH.

*Proof.* Immediate from 113_10 Cor 2.4 and the linearity of `D^o`. `[]`

So the mechanism, read correctly, is: **(NOEFF) + a positive self-intersection
somewhere in `D^o` + the torsion bound = contradiction.** The route to RH is to
establish (NOEFF) and the torsion bound and then conclude `s(c,c) <= 0` on
`D^o`, which is Weil positivity. The engine that converts `s(c,c) > 0` into
`(iota c, iota c) > 0` is the only remaining link, and it is where everything
dies:

**Theorem 6.5 (the domination obstruction — the main theorem of this lens).**
Let `(V, q)` be any real quadratic space with `n_+(q) <= 1`. Let
`iota : D^o_R -> V` be additive and `Q`-homogeneous with

```
        q(iota c)  >=  s(c,c)      for every c in D^o_R .                 (DOM)
```

Then `n_+(s|_{D^o_R}) <= 1`. Since `n_+(s|_{D^o_R}) = 2b` where `b` is the number
of off-line zero quadruples (`114_d3_01` Thm 2.5 with the polar block removed by
`f^(0) = f^(1) = 0`), and `2b <= 1` forces `b = 0`, **(DOM) implies RH**.
Conversely, under RH, `s|_{D^o_R} <= 0` and `iota = 0` satisfies (DOM).
Therefore:

```
        the existence of an additive dominating map from (D^o_R, s) into any
        Lorentzian space  <==>  RH.
```

*Proof.* Suppose `n_+(s|_{D^o_R}) >= 2` and choose a real basis `u,v` of a
2-dimensional subspace `W` on which `s` is positive definite. Put
`x=iota(u)`, `y=iota(v)`. Additivity and `Q`-homogeneity give, for rational
`a,b`,

```
q(a x+b y) = q(iota(a u+b v)) >= s(a u+b v,a u+b v).       (6.5.1)
```

First, `x,y` are real-linearly independent. Otherwise take a nonzero real
pair `(a,b)` with `a x+b y=0` and rational pairs `(a_j,b_j)->(a,b)`. The left
side of (6.5.1) tends to zero, while the right side tends to the strictly
positive number `s(a u+b v,a u+b v)`, a contradiction. Next approximate an
arbitrary real pair by rational pairs in (6.5.1). Continuity of the two
quadratic forms gives

```
q(a x+b y) >= s(a u+b v,a u+b v) > 0
```

for every nonzero real `(a,b)`. Thus `q` is positive definite on the real
2-plane `span_R{x,y}`, so `n_+(q)>=2`, contra. (This rational-density argument
is necessary: injectivity of a merely `Q`-linear map alone would not imply
that its image is a real 2-plane.)

Evenness of `n_+(s|_{D^o_R})`: the polar block `span(f_v, f_h)` of inertia
`(1,1)` is not in `D^o`; each mirror 2-cycle `{rho, rho'}` with `Re rho != 1/2`
contributes a hyperbolic Hermitian plane of inertia `(1,1)`, and such cycles come
in conjugate pairs, so they contribute `(2,2)` per quadruple; on-line zeros
contribute negative-definite blocks. Hence `n_+ = 2b`. The converse: under RH
`b = 0` and `s|_{D^o_R}` is negative semidefinite, so `0 >= s(c,c)` and `iota=0`
works. `[]`

**Corollary 6.6 (no linear import closes row (d)).** Every regular arithmetic
surface has `n_+ = 1` for its arithmetic intersection pairing (Yuan–Zhang
Thm 1.1/1.3 = Faltings–Hriljac–Moriwaki, quoted verbatim in `114_d3_01` §1;
Prop 1.5 there). Therefore hypothesis (H4') of Theorem 6.2, even in its weakest
useful form — an *inequality*, at *one* class at a time but uniformly over
`D^o` — cannot be established without already knowing RH. **Row (d) is not
closed by the import.**

**Remark 6.7 (this strictly strengthens `114_d3_01` Thm 4.5).** That theorem
showed *isometric* realisations are RH-equivalent. Theorem 6.5 shows the same
for *dominating* ones: no rigidity, no exactness, no signature preservation is
needed — only the one inequality that the growth mechanism actually consumes.
And it needs neither the archimedean-block argument nor the finite-support
argument of `114_d3_01` Thm 5.3; it is pure inertia.

**Remark 6.8 (the two escapes, and their cost).**

1. **Non-additive `iota`.** Theorem 6.5 uses additivity only on 2-dimensional
   subspaces. A realisation that is not additive on *any* 2-plane where `s > 0`
   escapes — but then Theorem 6.2's `iota(nc) = n iota(c)` must be re-supplied by
   hand, and the growth mechanism needs precisely that. No such object is known.
2. **A non-Lorentzian target.** Then it is not an arithmetic surface, and by
   Yuan–Zhang Thm 1.3 it is not an adelic-line-bundle limit of one either. This
   is Gap G-3 of `114_d3_01` with a sharper edge: the adelic escape must also
   break the Lorentzian bound, which Yuan–Zhang's theorem says it does not.

**Circularity audit of every hypothesis used in section 6.**

| hypothesis | status | why |
|---|---|---|
| (H0) `H^0(X,O_X) = Z` | CLEAN | standard normalisation, no zeros |
| (H3) `omega_X = 0` | CLEAN, open (G-5) | a statement about `X`, not about `xi` |
| (H5) torsion bound | CLEAN, open (G-4) | an analytic estimate on a Riemann surface |
| (H1) = (NOEFF) | CLEAN, open (G-7) | quantifier not emptied by RH (Thm 6.4) |
| (H4') isometry at one class | CLEAN in isolation | no signature obstruction for a single class |
| (H4') uniformly over `D^o` | **CIRCULAR** | Theorem 6.5: equivalent to RH |
| (DOM) domination | **CIRCULAR** | Theorem 6.5 |
| Lemma 6.1, Thms 3.1, 4.1, 5.1 | CLEAN | no zeros, no `sign(Q)`, no Weil positivity |

---

## 7. Gaps

**Gap G-6 (the R9 torsion variation).**

> *Statement.* With `T` as in `114_d3_02` Def 5.1, prove
> `|T(iota H) - T(iota(3f_v - f_h))| < 4`.
>
> *What would close it.* Any two-sided estimate for `log det Delta_L` across two
> classes of equal degree on a fixed arithmetic surface. Strictly weaker than
> Gap G-4: it is a difference, so it is insensitive to the additive constant
> `chi_X(O_X) + (1/2) log det Delta_{O_infinity}`.
>
> *Believed hard.* No. This is an analytic comparison on one fixed Riemann
> surface. It is the *cheapest* open item in row (d).

**Gap G-7 (the effectivity dictionary (NOEFF)).**

> *Statement.* Exhibit an additive, positively homogeneous
> `iota : D^o -> Pic-hat(X)` for some regular arithmetic surface `X` such that
> for all `c in D^o` and all `n >= 1`,
> `h^0_X(n iota c) <= h^0_X(O_X)` and `h^0_X(-n iota c) <= h^0_X(O_X)`.
>
> *What would close it.* A construction of `iota` from the trace `tau`, plus an
> effectivity criterion on `X` (e.g. via Bost's bounds and the successive minima
> of `f_*(n iota c)`) — Groenewegen's bound (Wei He Prop 2.1(i)) is the natural
> tool since it bounds `h^0` by `n h^0_Z(Z) + sum log max{1, gamma_i/lambda}`.
>
> *Believed hard.* Unknown, and **not** obviously RH-equivalent: by Theorem 6.4
> its quantifier is not emptied by RH. But it is useless alone: it delivers RH
> only in combination with (H4'), which is RH-equivalent by Theorem 6.5. So G-7
> is *clean but currently inert*.

**Gap G-8 (a meaningful non-additive transport).**

> *Corrected statement.* Pointwise domination plus positive homogeneity is
> vacuous: `114_a_13` constructs it on one positive ray for every quadratic
> space. Construct instead a source-defined map
> `iota:D^o->Pic-hat(X)_R` which also transports enough two-point, section or
> effectivity structure to run Theorem 6.2, or prove that those extra
> requirements force additivity on a positive 2-plane.
>
> *What would close it.* A polarization law, an effectivity-compatible
> Kunneth law, or another explicit two-point condition strong enough to prevent
> the one-ray collapse of `114_a_13`.
>
> *Status.* The old formulation is closed trivially and has no RH content. The
> strengthened formulation is open.

Still open from the earlier files of this lens: **G-1** (the arithmetic surface
and the realisation — now known to be RH-equivalent in every linear form),
**G-2**, **G-3** (the adelic escape), **G-4** (absolute torsion bound), **G-5**
(the `K = 0` transport).

---

## 8. Refutation conditions

Continuing from R32 of `114_d3_02`.

- **R33.** If any candidate `h^0` imported into row (d) is not thresholded at
  `h^0_X(O_X)`, R8 fires against it by Theorem 4.1 and it is wrong. This applies
  to every future file in this programme.
- **R34.** If a future file exhibits an additive `iota : D^o -> Pic-hat(X)_R`
  with `(iota c, iota c) >= s(c,c)` for all `c in D^o` and claims it is proved
  unconditionally, it has proved RH or it has an error; by Theorem 6.5 there is
  no third possibility.
- **R35.** If the analytic torsion difference `|T(H) - T(D2)|` is shown to
  exceed `4`, R9 fires against the imported `h^1` and the import is dead even
  as a formal analogy.
- **R36.** If an arithmetic intersection pairing with `n_+ >= 2` is exhibited on
  a regular arithmetic surface over `Spec Z`, then Yuan–Zhang Thm 1.1 is
  contradicted and `114_d3_01` Prop 1.5, Theorem 6.5 and Corollary 6.6 here are
  all wrong.

---

## 9. Verifier output

Real output of `python3 114_d3_03_acceptance_tests.py`, run in this session
(exit code 0):

```
A. R7 (113_10): a candidate h^0 must not give h^0(H) = 0
PASS  imported h^0 of the ZERO module is exactly 0 (the theta sum is the one term x=0)
PASS  so R7 is NOT vacuous for the import: h^0_X(L) = 0  <==>  f_*L = 0, i.e. L has no global section
PASS  but on any module of rank >= 1 the imported h^0 is STRICTLY positive
      [h^0(-40) = 8.5383e-75594941668333063763836237404867871 > 0]
PASS  hence R7 fires against the import EXACTLY when the realisation sends H to a class with no section
PASS  threshold form of R7:  h^0_Z(a) > h^0_Z(0)  <==>  a > 0  (exact, by strict monotonicity)
      [threshold h^0_Z(0) = 0.0829015200311]
PASS  so under the threshold reading R7 becomes: deg-hat f_*iota(H) > 0

B. R8 (113_10 Cor 2.3): no nonzero element of rad may be effective
PASS  imported h^0 of the TRIVIAL class O_X equals h^0_Z(Z) = log theta(1) = 0.0829015200311
PASS  R8 FIRES against the raw imported h^0: it declares the zero class (= the class of every
      element of rad) effective   [h^0_X(O_X) = 0.08290152 > 0, but 113_10 Cor 2.3 forces h^0 = 0 there]
PASS  the repair h^0_thr := h^0_X(.) - h^0_X(O_X) gives h^0_thr(O_X) = 0 exactly, so R8 passes
      after thresholding
PASS  the repair is not free: it turns R7 into the strictly stronger demand
      h^0_X(iota H) > log theta(1) = 0.08290152
PASS  the repair is consistent: R7-threshold and R8-threshold can hold simultaneously
      (a > 0 for H, a = 0 for rad)

C. R9 (113_11): h^1([3f_v - f_h]) > h^1([H]) for the imported h^1
PASS  re-derived: (H,H) = 2
PASS  re-derived: (3f_v - f_h)^2 = -6
PASS  re-derived: deg(H) = s(H,H) = 2 = deg(3f_v - f_h) = s(D2,H)
PASS  symbolic: h^1(D2) - h^1(H) = 4 + (T(H) - T(D2)) + E, E = h0D + h0mD - h0H - h0mH
      [margin = -TD + TH + h0D - h0H + h0mD - h0mH + 4]
PASS  the margin 4 is exactly ((H,H) - (D2,D2))/2, i.e. R9 is passed by the SELF-INTERSECTION,
      not by the degree (both degrees are 2)
PASS  sufficient condition for R9:  h^0_X(H) + h^0_X(-H) < 4 + T(H) - T(D2)  (uses only h^0 >= 0 at D2)
PASS  rank-1 model: for deg-hat f_*iota(H) in [0,2], h^0(H)+h^0(-H) <= 2.0 < 4, so R9 holds
      whenever T(H) - T(D2) > -2
PASS  Bost (ii) at deg = -2 makes the correction invisible: h^0 <= 8.11731e-75
PASS  so in the rank-1 model R9  <==>  T(H) - T(3f_v - f_h) > -4 (up to 1e-74)
PASS  R9 constrains only the VARIATION of T (it is invariant under T -> T + const);
      Gap G-4 constrains its absolute value

D. Obstruction O1 (113_10 Prop 5.1) against the imported h^0
PASS  corpus side: the effective cone is scale-stable, so h^0_corpus(nc) = h^0_corpus(c)
      for every real n > 0 (113_10 Prop 5.1) - no growth
PASS  imported side: h^0_Z(n a) - h^0_Z(0) grows without bound
      (n = 1..7: 0.9171, 1.917, 2.917, 3.917, 4.917, 5.917, 6.917)
PASS  imported side: h^0_Z(a) - h^0_Z(-a) = a exactly, so the growth is LINEAR in the degree
      and QUADRATIC in the class via chi
PASS  structural: every summand of Wei He's h^1_X is >= 0 (two theta invariants and two
      log #torsion), hence h^1_X >= 0
PASS  mechanism: with the weak torsion bound T(nL) >= -n^2 (L,L)/4 - C for ANY constant C,
      chi(nL) -> infinity   [at C = 1000 the threshold is first crossed at n = 45]
PASS  h^1 >= 0 and chi = h^0 - h^1 + h^2  ==>  h^0(nL) + h^2(nL) >= chi(nL) -> infinity,
      so one of +-nL is effective for n large
PASS  and 113_10 Prop 5.1 transports that back: nc effective <==> c effective.
      O1 is DEFEATED by the import, not confirmed by it

E. circularity: the signature an isometric realisation forces
PASS  inertia with 3 on-line zeros and 0 off-line quadruples: (n_+, n_-) = (1, 7)
      [predicted (1+2b, 1+2a+2b) = (1, 7)]
PASS  inertia with 5 on-line zeros and 0 off-line quadruples: (n_+, n_-) = (1, 11)
      [predicted (1+2b, 1+2a+2b) = (1, 11)]
PASS  inertia with 3 on-line zeros and 1 off-line quadruples: (n_+, n_-) = (3, 9)
      [predicted (1+2b, 1+2a+2b) = (3, 9)]
PASS  inertia with 3 on-line zeros and 2 off-line quadruples: (n_+, n_-) = (5, 11)
      [predicted (1+2b, 1+2a+2b) = (5, 11)]
PASS  inertia with 0 on-line zeros and 3 off-line quadruples: (n_+, n_-) = (7, 7)
      [predicted (1+2b, 1+2a+2b) = (7, 7)]
PASS  the arithmetic Hodge index theorem forces n_+ = 1 on the target, so an ISOMETRIC
      realisation exists only if b = 0, i.e. only under RH: that hypothesis is CIRCULAR
PASS  a SINGLE-CLASS realisation (one c, one surface, (L,L) = s(c,c)) carries no signature
      obstruction and is NOT circular; the whole burden then falls on the effectivity dictionary
PASS  on D^o (polar block removed) with 3 on-line zeros and 0 off-line quadruples: n_+ = 0 = 2b,
      EVEN   [n_+ = 0, so n_+ <= 1 forces b = 0, i.e. RH]
PASS  on D^o (polar block removed) with 6 on-line zeros and 0 off-line quadruples: n_+ = 0 = 2b,
      EVEN   [n_+ = 0, so n_+ <= 1 forces b = 0, i.e. RH]
PASS  on D^o (polar block removed) with 3 on-line zeros and 1 off-line quadruples: n_+ = 2 = 2b,
      EVEN   [n_+ = 2, so n_+ <= 1 forces b = 0, i.e. RH]
PASS  on D^o (polar block removed) with 3 on-line zeros and 2 off-line quadruples: n_+ = 4 = 2b,
      EVEN   [n_+ = 4, so n_+ <= 1 forces b = 0, i.e. RH]
PASS  on D^o (polar block removed) with 1 on-line zeros and 4 off-line quadruples: n_+ = 8 = 2b,
      EVEN   [n_+ = 8, so n_+ <= 1 forces b = 0, i.e. RH]

F. the domination obstruction: q(iota c) >= s(c,c) forces n_+(s) <= n_+(q)
PASS  400 random instances: q Lorentzian (n_+ = 1), iota linear, p psd, s = q(iota .) - p
      ==>  n_+(s) <= 1   [max n_+(s) observed = 1 over 400 trials]
PASS  consequence: a linear iota into ANY Lorentzian target with (iota c, iota c) >= s(c,c)
      on D^o forces n_+(s|_{D^o}) <= 1; since that index is 2b, it forces b = 0 = RH.
      The transport is CIRCULAR.
PASS  converse: under RH (b = 0), s|_{D^o} is negative definite, so iota = 0 dominates and the
      hypothesis is satisfiable - hence EQUIVALENT to RH, not merely implied by it
      [max eigenvalue of s|_{D^o} at b = 0 is -1.000 < 0]

checks run: 43      failures: 0
VERDICT: ALL CHECKS PASS
```

---

## 10. Scope

### Proved here

- Theorem 3.1: `h^0_X(L) = 0` iff `f_*L = 0`; R7 is a non-vacuous condition on
  the realisation.
- Theorem 4.1: **R8 fires** against the raw imported `h^0`, unconditionally;
  Prop 4.2: the threshold repair, and its uniqueness.
- Lemma 6.1: `h^1_X >= 0` from Wei He's definition.
- Theorem 5.1 and Cor 5.2: the imported `h^1` passes R9 with margin
  `((H,H)-(D2,D2))/2 = 4`, conditionally on the torsion *variation*.
- Theorem 6.2 and Cor 6.3: the growth mechanism; Obstruction O1 is defeated and
  113_10 Prop 5.1 becomes the transport.
- Theorem 6.4: the conclusion of the dictionary is always false on `D^o`, so the
  dictionary is (NOEFF) and is *not* emptied by RH.
- **Theorem 6.5 and Corollary 6.6**: the existence of an additive **dominating**
  map from `(D^o, s)` into any Lorentzian space is **equivalent to RH**. Hence no
  linear import of an arithmetic index theorem can close row (d). This
  strengthens `114_d3_01` Thm 4.5 from isometries to inequalities.

### Read from source

- Wei He arXiv:2512.01811v2: the definitions of `h^0_X, h^1_X, h^2_X, chi_X`,
  Theorem 1.1 = 2.8, Prop 2.1(i) (Groenewegen) and (ii),(iii) (Bost) — quoted
  verbatim in `114_d3_02` §3 and used here.
- Yuan–Zhang arXiv:1304.3538v1 Thm 1.1 and Thm 1.3 (the Lorentzian conclusion) —
  quoted verbatim in `114_d3_01` §1.
- Repo, re-read and checked against the use made of them: 113_10 Def 2.1,
  Thm 2.2, Cor 2.3, Cor 2.4, Thm 3.2, Prop 5.1, R7, R8; 113_11 Thm 3.4, R9;
  107_241 Thm 3.1.

### Verified numerically

43 checks, all passing: the vanishing locus of the theta `h^0`; the exact
threshold `log theta(1) = 0.0829015200311`; R8's firing; the R9 margin
symbolically and the Bost bound `8.1e-75` at `deg = -2`; the unbounded growth of
`h^0_Z(na)`; the crossing index `n = 45` at torsion deficit `C = 1000`; the
inertia `(1+2b, 1+2a+2b)` on the full space and `2b` on `D^o` for five
configurations; and the domination lemma on 400 random Lorentzian instances.

### Not established

- Gaps G-1 through G-8. In particular **nothing here proves RH**, and Theorem
  6.5 says that the linear version of this route *cannot*.
- The single class where the import could still bite — a non-additive transport
  (G-8) — is not constructed and not excluded.
- The torsion terms `T` are not bounded, absolutely (G-4) or in variation (G-6).

---

## 11. Verdict on lens 3 of row (d)

**R16 does not fire.** The quadratic `chi` R16 doubted is classical and was read
first-hand (`114_d3_02` Thm 3.1, Thm 4.1).

**The import is real and it works on its own terms.** It supplies exactly what
Obstruction O1 asked for; it passes R5, R6, R7, R9; it fails R8 only through a
normalisation that is forced and harmless.

**And it cannot be attached to `D` without assuming RH.** Theorem 6.5 is the
sharp statement: every additive map that merely *dominates* `s` on `D^o`, into
any space where the intersection form has `n_+ <= 1` — which is every arithmetic
surface, by the arithmetic Hodge index theorem — exists if and only if RH holds.
The obstruction is not the effective cone, not the torsion, not Serre duality
and not the choice of `h^0`: it is one integer, the positive inertia index, `1`
on the geometric side and `2b` on the arithmetic side.

Row (d) lens 3: **NOT CLOSED, and now known to be unclosable by any linear
transport.** The candid next move is Gap G-8 — prove that homogeneity forces
additivity on a positive 2-plane, which would close row (d) negatively and
finally.
