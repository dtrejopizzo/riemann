# 114_d3_01 — row (d), lens 3 (external index): the imported index theorems

```
IMPORTED, READ FIRST-HAND: Faltings-Hriljac-Moriwaki arithmetic Hodge index
                      theorem and the Yuan-Zhang adelic version, from
                      00-references/papers-nuevos/D/arXiv-1304.3538v1.
                      Both are LORENTZIAN: n_+ = 1, exactly.
THE CHEAP TEST:       PASSED, and the brief's worry was based on a MISREADING
                      of 107_241 Thm 3.1.  In that theorem P is the set of
                      OFF-LINE MIRROR 2-CYCLES OF ZEROS, not the set of places.
                      n_+ = 1 on every truncation under RH; measured to
                      dimension 122 from 60 genuine zeros.  The lens is NOT
                      closed negatively.
COMPARISON OBJECT:    the REAL form (D_R, s), not its realification.  The
                      realification has n_+ = 2 and would falsely refute the
                      import.  Stated as Prop 2.4 so it cannot be walked into.
VACUITY THEOREM:      "there exists an isometric realisation of (D/rad, s) in
                      an arithmetic Hodge-index space" is EQUIVALENT to RH
                      (Thm 4.5).  So the bare embedding is a CIRCULAR target
                      and no import of that shape can prove anything.
NO-GO:                there is NO place-wise realisation on a fixed regular
                      arithmetic surface (Thm 5.3): the finite part of an
                      arithmetic intersection number is supported on finitely
                      many primes, while tau(f * f^*) has a nonzero p-part at
                      EVERY prime, for an explicit f in D.
WHAT SURVIVES:        one non-vacuous target only -- a place-wise realisation
                      by ADELIC line bundles in the sense of Zhang/Yuan-Zhang.
                      That is Gap G-3.  It is not closed here.
```

Depends on: 107_241 (corner pairing, Thm 3.1 and its Cor 3.3), 113_08 (the
coordinate model (2.2)), 113_09 (`rad = (chi)`, `s(H,H) = 2`), 113_10 (degree,
`(E^o)`, R7, R8), 113_12 (Thm 1.3 `s = tau(x * y^*)`, Thm 4.1 Hodge index
`<=>` RH), 113_14 (the two analytic gaps), 113_15 (the four-row ledger, R16).
External: Yuan–Zhang, *The arithmetic Hodge index theorem for adelic line
bundles I*, arXiv:1304.3538v1 — read in this session at
`00-references/papers-nuevos/D/arXiv-1304.3538v1`.

Verifier: `114_d3_01_imported_index_theorems.py` — 43 checks, all pass, run
below.

---

## 0. What this file is, and one correction to the brief

Row (d) of the ledger asks for an index theorem. Lens 3 is instructed to try to
**import one from arithmetic geometry** rather than build one. This file does
three things:

1. states the two importable theorems **verbatim from a source read in this
   session**, with the exact quantifiers (section 1);
2. settles the cheap decisive test the brief posed — *does the positive index
   of `s` grow with the size of the truncation?* — and corrects the misreading
   on which the worry rested (sections 2, 3);
3. determines exactly what an import can and cannot buy, by proving that the
   *bare* form of the import is RH-equivalent (section 4) and that the
   *place-wise* form is impossible on a fixed arithmetic surface (section 5).

**Correction to the brief.** The brief states that 107_241 Thm 3.1 gives
`n_+ = 1 + #P` and that this "suggests the positive index GROWS with the number
of places". The brief also instructs: *verify this reading against the actual
files and correct it if it is wrong.* It is wrong. 107_241, section 3, first
sentence, reads verbatim:

> Write `L` for the set of distinct zeros with `Re rho = 1/2` and `P` for the
> set of mirror 2-cycles `{rho, rho'}`, `Re rho != 1/2`.

`P` is a set of **2-cycles of off-line zeros of xi**, not a set of places. The
same file's Cor 3.2 makes this explicit: `n_+ - 1 = #P = (1/2) #{distinct
off-line zeros}`, and Cor 3.3 concludes `RH <=> n_+ = 1`. So the positive index
does **not** grow with the number of places, and under RH it does not grow at
all: it is 1 on every truncation. Section 3 below proves this and measures it.

---

## 1. The two imported theorems, verbatim

Source: `00-references/papers-nuevos/D/arXiv-1304.3538v1`, Xinyi Yuan and
Shou-Wu Zhang, *The arithmetic Hodge index theorem for adelic line bundles I:
number fields* (2013). Theorem numbering in that source: `\newtheorem{thm}{Theorem}[section]`
with all environments sharing the counter, `\section{Introduction}`, then
`\begin{thm}\label{hodge0}`, `\begin{defn}\label{def-positivity}`,
`\begin{thm}\label{hodge}` — i.e. **Theorem 1.1**, **Definition 1.2**,
**Theorem 1.3**. Verified by direct inspection of the source file.

### Theorem 1.1 (Yuan–Zhang Thm 1.1, attributed there to [Fal], [Hr], [Mo1])

Quoted verbatim from the source (LaTeX transcribed to ASCII):

> Let `K` be a number field, and `pi : X -> Spec O_K` be a regular arithmetic
> variety, geometrically connected of relative dimension `n >= 1`. Let `M-bar`
> be a Hermitian line bundle on `X`, and `L-bar` be an ample Hermitian line
> bundle on `X`. Assume that `M_K . L_K^{n-1} = 0` on the generic fibre `X_K`.
> Then the arithmetic intersection number
>
> ```
>         M-bar^2 . L-bar^{n-1}  <=  0 .
> ```
>
> Moreover, if `L` is ample on `X` and the metric of `L-bar` is strictly
> positive, then the equality holds if and only if `M-bar = pi^* M-bar_0` for
> some Hermitian line bundle `M-bar_0` on `Spec O_K`.

The source adds: "The result was due to Faltings [Fal] and Hriljac [Hr] for
`n = 1`, and due to Moriwaki [Mo1] for general `n`." This is the
**Faltings–Hriljac form** the brief asked for, in the exact shape in which
Yuan–Zhang use it. Note the quantifiers, which matter below:

- the *space* is `Pic-hat(X)` (Hermitian line bundles on a regular arithmetic
  variety), not an abstract quadratic space;
- the *pairing* is `(M-bar, N-bar) |-> M-bar . N-bar . L-bar^{n-1}`;
- the *subspace of definiteness* is cut out by a condition **on the generic
  fibre**: `M_K . L_K^{n-1} = 0`;
- the *sign* is `<= 0`, and equality is *exactly* the pullbacks from the base.

For `n = 1` (an arithmetic surface) the generic-fibre condition reads
`deg(M_K) = 0`.

### Definition 1.2 (Yuan–Zhang Def 1.2: positivity)

Verbatim:

> Let `K` be a number field. Let `X` be a projective variety over `K`, and
> `L-bar`, `M-bar` be adelic line bundles on `X`.
> (1) We say that `L-bar` is *nef* if the adelic metric of `L` is a uniform
> limit of metrics induced by nef Hermitian line bundles on integral models of
> `X`.
> (2) We say that `L-bar` is *integrable* if it is the difference of two nef
> adelic line bundles on `X`.
> (3) We say that `L-bar` is *ample* if `L` is ample, `L-bar` is nef, and
> `(L-bar|_Y)^{dim Y + 1} > 0` for any closed subvariety `Y` of `X`.
> (4) We say that `M-bar` is *`L-bar`-bounded* if there is an integer `m > 0`
> such that both `m L-bar + M-bar` and `m L-bar - M-bar` are nef.

### Theorem 1.3 (Yuan–Zhang Thm 1.3: the adelic arithmetic Hodge index theorem)

Verbatim:

> Let `K` be a number field, and `pi : X -> Spec K` be a normal and
> geometrically connected projective variety of dimension `n >= 1`. Let `M-bar`
> be an integrable adelic line bundle on `X`, and `L-bar_1, ..., L-bar_{n-1}`
> be `n-1` nef line bundles on `X` where each `L_i` is big on `X`. Assume
> `M . L_1 ... L_{n-1} = 0` on `X`. Then
>
> ```
>         M-bar^2 . L-bar_1 ... L-bar_{n-1}  <=  0 .
> ```
>
> Moreover, `L-bar_i` is ample and `M-bar` is `L-bar_i`-bounded for each `i`,
> then the equality holds if and only if `r M-bar = pi^* M-bar_0` for some
> adelic line bundle `M-bar_0` on `Spec K` and some integer `r > 0`.

### Statement 1.4 (Yuan–Zhang, the signature paragraph following Thm 1.3)

Verbatim:

> As in the classical case, the theorem explains the signature of the
> intersection pairing on certain space of adelic line bundles. Let `W` denote
> the subspace of `Pic-hat(X)_int (x) Q` consisting of elements which are
> represented by `Q`-linear combinations of integrable adelic line bundles on
> `X` which are `L-bar_i`-bounded for all `i`. Define a pairing on `W` by
> `<M-bar_1, M-bar_2> = M-bar_1 . M-bar_2 . L-bar_1 ... L-bar_{n-1}`. Denote
> `V = pi^* Pic-hat(K) (x) Q`, viewed as a subspace of `W`. Then the theorem
> implies that the pairing on `V^perp` is negative semi-definite, that `V` is a
> maximal isotropic subspace of `V^perp`, and that `V^perp / V` is negative
> definite.

### Proposition 1.5 (the imported forms are Lorentzian: `n_+ = 1`)

Let `(W, <,>)` be as in Statement 1.4, with `V = pi^* Pic-hat(K)_Q` and suppose
`W != V^perp` (equivalently: some class of `W` pairs nontrivially with `V`).
Then

```
        n_+(W)  =  1 ,     rad(W) = V ,     and  <,>  is negative definite
                                                 on V^perp / V .
```

*Proof.* `V^perp` is by definition the kernel of the linear map
`phi : W -> V^*`, `M-bar |-> <M-bar, ->|_V`. `V` is one-dimensional over `Q`
(`Pic-hat(K)_Q = Q` by the arithmetic degree, for `K` a number field), so
`dim V^* = 1` and `codim V^perp <= 1`; the hypothesis `W != V^perp` forces
`codim V^perp = 1`. By Statement 1.4, `<,>` is negative semi-definite on
`V^perp` with radical `V` (that is what "`V` maximal isotropic in `V^perp`" and
"`V^perp/V` negative definite" say together). Hence `n_+(V^perp) = 0` and, by
Sylvester's law applied to a codimension-1 extension, `n_+(W) <= 1`. It is `>= 1`
because if `n_+(W) = 0` then `<,>` would be negative semi-definite on all of
`W`, forcing `V` (which is isotropic and pairs nontrivially with something in
`W`) to violate Cauchy–Schwarz for semi-definite forms. So `n_+(W) = 1`. `[]`

This is the "arithmetic surface intersection forms are Lorentzian" fact the
brief asked for, now derived from a statement read at the source rather than
recalled. **It is the exact shape of `s` under RH** (113_12 Thm 4.1); see
section 4.

### Proposition 1.6 (the archimedean block is a negative definite Dirichlet form)

Let `X -> Spec Z` be a regular projective arithmetic surface (relative
dimension 1) carrying an ample `L` with strictly positive metric. Let
`G := ker( Ch-hat^1(X) -> Pic(X) )`, the classes of the form `(0, g)` with `g` a
real `F_infinity`-invariant function on `X(C)`. Then the arithmetic
self-intersection is negative semi-definite on `G`, and its radical is exactly
the constants.

*Proof.* Apply Theorem 1.1 with `n = 1`, `M-bar = (O_X, g)`. The generic fibre
condition is `deg(M_K) = deg(O_{X_K}) = 0`, which holds. Hence
`M-bar^2 . L-bar^0 = M-bar^2 <= 0`. The equality clause of Theorem 1.1 gives
`M-bar^2 = 0` iff `M-bar = pi^* M-bar_0`, and for `X -> Spec Z` the pullbacks
of Hermitian line bundles on `Spec Z` that are trivial as line bundles are
exactly the `(0, c)` with `c` constant. `[]`

**Consequence used later.** `G / (constants)` has dimension `2^{aleph_0}` as a
real vector space (it contains `C^infinity(X(C))_R` modulo constants, and
`|C^infinity(X(C))| = 2^{aleph_0}`), and the form is negative *definite* on it.
So an arithmetic surface supplies a negative definite block of the largest
possible dimension — **and it supplies it analytically, from Green functions,
not from algebraic cycles.**

---

## 2. The comparison object: the real form, not the realification

The imported pairing is a **real symmetric** form. The corpus form `s` is
**Hermitian** on a complex space. Comparing the wrong real object to the
imported one produces a spurious refutation. This section fixes the comparison.

**Definition 2.1.** `D_R := { f in D : f(u) in R for all u > 0 }`, and
`V_R := D_R / (rad ∩ D_R)`.

**Lemma 2.2 (`s` is real on `D_R`).** For `x, y in D_R`, `s(x,y) in R`.

*Proof.* For real `f`, `f^(conj s) = conj(f^(s))`; so `f^(0), f^(1)` are real
and the polar part `x^(0) y^(1) + x^(1) y^(0)` is real. For the zero sum, pair
`rho` with `conj rho` (a zero of the same multiplicity, since `xi` is real on
`R`). Writing `rho' = 1 - conj rho`, the `conj rho` term is
`x^(conj rho) conj( y^((conj rho)') ) = conj(x^(rho)) . conj( conj( y^(rho') ) )
= conj( x^(rho) conj(y^(rho')) )`, the complex conjugate of the `rho` term.
Summing over conjugate pairs gives a real number. `[]`

**Lemma 2.3 (a real form has the inertia of its Hermitian extension).** Let `h`
be a Hermitian form on `V = V_R (x)_R C` which is real-valued on `V_R`. Then the
inertia of `h|_{V_R}` (as a real symmetric form) equals the inertia of `h`.

*Proof.* Diagonalise `h|_{V_R}` over `R`: a basis `e_1, ..., e_n` of `V_R` with
`h(e_i, e_j) = 0` for `i != j` and `h(e_i,e_i) in {+1,-1,0}` after scaling. The
same basis is a `C`-basis of `V` and diagonalises `h` with the same values. `[]`

**Proposition 2.4 (the doubling trap).** Let `h` be Hermitian of inertia `(p,q)`
on a complex space `V`. The *realification* — the real symmetric form
`Re h` on the underlying real space of `V`, of twice the real dimension — has
inertia `(2p, 2q)`.

*Proof.* Diagonalise; each complex coordinate with sign `e` contributes
`e(x^2+y^2)`. `[]`

**This is a trap, not a curiosity.** `s` has `n_+ = 1` under RH; its
realification has `n_+ = 2`; an arithmetic Hodge index space has `n_+ = 1`
(Prop 1.5). An import that compares the *realification* to the imported form
would conclude "`2 != 1`, the import is impossible" — falsely. Verifier check E
exhibits all three numbers side by side: Hermitian `(1,9)`, real form `(1,9)`,
realification `(2,18)`.

**Theorem 2.5 (blockwise signature of the real form).** Let a truncation of the
zero set consist of `a` conjugate pairs of on-line zeros and `b` off-line
quadruples `{rho, conj rho, rho', conj rho'}` (all multiplicities 1). Then on
the real form

```
        n_+  =  1 + 2b ,        n_-  =  1 + 2a + 2b ,
```

so `n_+ = 1` iff there are no off-line zeros in the truncation.

*Proof.* Real coordinates: `alpha = f^(0)`, `beta = f^(1)` in `R`, and for each
zero `rho` in the **upper** half plane a complex coordinate `z_rho = f^(rho)`
(the lower zero carries `conj z_rho`, not an independent coordinate).

*Polar block:* `2 alpha beta`, inertia `(1,1)`.

*On-line conjugate pair `{rho, conj rho}`, `rho' = rho`:* the two terms are
`-m|z_rho|^2` and `-m|conj z_rho|^2`, together `-2m(u^2+v^2)` for
`z_rho = u+iv`: inertia `(0,2)`.

*Off-line quadruple:* put `z = f^(rho)`, `w = f^(rho')`, both free in `C`; the
four terms of `- sum_rho m_rho f^(rho) conj(f^(rho'))` over the quadruple are
`z conj w`, `w conj z`, `conj z . w`, `conj w . z`, total
`-2m( z conj w + conj z w ) = -4m Re(z conj w) = -4m (x_1x_2 + y_1y_2)`, two
copies of `-4m` times a hyperbolic plane: inertia `(2,2)`.

Blocks are pairwise orthogonal (a coordinate pairs only with its mirror), so
inertias add. `[]`

Theorem 2.5 agrees with the Hermitian count of 107_241 Thm 3.1, as Lemma 2.3
requires: an off-line quadruple is **two** mirror 2-cycles, so `#P = 2b` and
`n_+ = 1 + #P = 1 + 2b`; an on-line conjugate pair is **two** elements of `L`,
so `#L = 2a` and `n_- = 1 + #L + #P = 1 + 2a + 2b`.

---

## 3. The cheap decisive test, resolved

**Theorem 3.1.** For every finite truncation `Z_0` of the zero set that is
stable under `rho |-> conj rho` and `rho |-> rho' = 1 - conj rho`, the
positive index of `s` restricted to the corresponding coordinate block is
`1 + 2b(Z_0)`, where `b(Z_0)` is the number of off-line quadruples in `Z_0`. In
particular, **under RH the positive index equals 1 for every truncation, of
every size**; it does not grow with the truncation, with the number of zeros,
or with anything else.

*Proof.* Theorem 2.5, plus: under RH `b(Z_0) = 0`. `[]`

**Corollary 3.2 (the test does not close the lens).** The apparent conflict
between "arithmetic intersection forms are Lorentzian" and "107_241 gives
`n_+ = 1 + #P`" is not a conflict: `#P` counts off-line zeros, which RH says
there are none of. The two statements agree exactly, and the negative closure of
the lens that the brief pre-authorised does **not** occur.

**Measured** (verifier, section B): with 60 genuine zeros from
`mpmath.zetazero`, at truncation sizes `N = 1,2,3,5,8,13,21,34,55,60`, the real
form has inertia exactly `(1, 0, 1+2N)` — dimension 122 at `N = 60` with
`n_+ = 1`. The Hermitian model gives the same numbers. With `k` planted
off-line quadruples, `n_+ = 1 + 2k` for `k = 1,2,3`, so the test is not blind:
it detects the failure it is designed to detect. Section D reproduces 113_12's
two measured signatures `(1,7)` and `(3,5)` exactly.

**Section F of the verifier does the same test one level lower**, on genuine
elements of `D`: real functions with balanced profiles `x^j e^{-x^2}`,
`j = 0..7` (113_07 Def 1.3 and the remark after Lemma 1.4 certify that these lie
in `D_theta` for every `theta`), Mellin-evaluated at genuine zeros in 60-digit
precision, giving a real symmetric `8 x 8` Gram matrix with entries of size
`10^0` to `10^2` and eigenvalues spanning 44 orders of magnitude. Inertia
`(1, 4, 3)`: `n_+ = 1`. With one off-line quadruple planted, `(3, 3, 2)`:
`n_+ = 3`.

---

## 4. What an import can buy, and the vacuity theorem

**Definition 4.1 (isometric realisation).** An *isometric realisation* of
`(V_R, s)` is a real vector space `W` with a symmetric bilinear form `<,>`
arising as an arithmetic Hodge index space (Statement 1.4 / Prop 1.5), together
with an `R`-linear map `iota : V_R -> W` with `s(x,y) = <iota x, iota y>` for
all `x,y`, and `ker iota = rad(s)`.

**Definition 4.2 (place-wise realisation).** An isometric realisation is
*place-wise* if in addition, for every `x, y in D_R` and every prime `p`, the
`p`-local component of the arithmetic intersection number `<iota x, iota y>`
equals

```
        c_p(x,y)  :=  log p . sum_{k>=1} [ z(p^k) + z(1/p^k)/p^k ] ,
                      z := x * y^* ,
```

the `p`-part of the trace `tau` of 113_12 Def 1.1, and the archimedean local
component equals `-A(z)`.

Definition 4.2 is the only version with arithmetic content: it says the
primes of `Spec Z` are the primes of the realisation. Definition 4.1 says
nothing about primes at all. The next two theorems show precisely how much that
distinction costs.

**Theorem 4.3 (transfer: a realisation implies RH).** If an isometric
realisation exists, then RH holds.

*Proof.* By Prop 1.5, `n_+(W) = 1`. An isometry with kernel exactly the radical
preserves the positive index, so `n_+(s) = n_+(V_R, s) <= 1`. By 113_12 Thm 4.1
(equivalently 107_241 Cor 3.3), `n_+(s) = 1` iff RH; and `n_+(s) >= 1` since
`s(H,H) = 2 > 0` (113_09 Thm 4.1). Hence `n_+(s) = 1` and RH holds. `[]`

**Theorem 4.4 (converse: RH implies a realisation).** Assume RH. Then an
isometric realisation exists; one may take `W = Ch-hat^1(X)_R` for any regular
projective arithmetic surface `X -> Spec Z` with `X(C) != empty` and with a
section, e.g. `X = P^1_Z`.

*Proof.* Assume RH. By 113_12 Thm 4.1, `s(H,H) = 2 > 0` and `s` is negative
definite on `H^perp` modulo the radical; hence

```
        V_R / rad   is isometric to   <2>  ⊥  (-1)^{(+)kappa}
```

for some cardinal `kappa <= 2^{aleph_0}` (a negative definite real quadratic
space of dimension `kappa` is isometric to `(-1)^{(+)kappa}` by transfinite
Gram–Schmidt: scale each vector by `|q(v)|^{-1/2}`, extend a maximal orthonormal
set by Zorn). The bound `kappa <= 2^{aleph_0}` holds because `D_R` is a set of
functions on `(0, infinity)`, so `|D_R| <= 2^{aleph_0}`.

In the target: choose a horizontal `C` with `deg C_Q = 1` and adjust the metric
of `O(C)` by `C-bar |-> C-bar + pi^*(t)`, which changes `C-bar^2` by
`2t deg C_Q = 2t`; choose `t` with `C-bar^2 = 2`. Let
`K := { g in C^infinity(X(C))^{F_infinity}_R : ((0,g) . C-bar) = 0 }`, a
subspace of codimension 1, hence of dimension `2^{aleph_0}`, and orthogonal to
`C-bar`. The constants are not in `K` (by the projection formula
`(pi^* a-bar . C-bar) = deg(a-bar) deg(C_Q) = deg(a-bar) != 0`), so Prop 1.6
makes `<,>` negative definite on `K`. Therefore
`W ⊇ <2> ⊥ (-1)^{(+)2^{aleph_0}}`, which receives `V_R/rad` isometrically since
`kappa <= 2^{aleph_0}`. `[]`

**Theorem 4.5 (VACUITY).**

```
        ( there exists an isometric realisation of (V_R, s) )   <==>   RH .
```

*Proof.* Theorems 4.3 and 4.4. `[]`

**Circularity verdict.** Definition 4.1 is a **circular** target in the exact
sense fixed by the brief: the statement "an isometric realisation exists" is
RH-equivalent. Proving it is proving RH; assuming it is assuming RH. No import
whose only output is an abstract isometry can therefore contribute anything —
not because the import is false, but because the *hypothesis* of the import is
the conclusion. This retires the naive form of row (d)'s lens 3, and it is the
same disease 113_10 Thm 4.3 has ((E^o) made vacuous by RH), diagnosed one level
up.

Note what Theorem 4.5 does **not** say. It does not say the import is useless:
Theorem 4.3 remains a genuine implication, and it is the only implication in
this corpus that would derive RH from a *finitely* stated arithmetic-geometric
input. It says that the input must be produced by construction, and that the
construction must see the primes. That is Definition 4.2.

---

## 5. The finite-support no-go for place-wise realisations

**Lemma 5.1 (finite support).** Let `X` be a regular projective arithmetic
surface over `Spec Z` and let `D-bar, E-bar in Ch-hat^1(X)_R`. Then the set of
primes `p` at which the `p`-local component of `(D-bar . E-bar)` is nonzero is
**finite**.

*Proof.* Each of `D, E` is, by definition, a finite `R`-linear combination of
prime divisors. After moving `D` by a principal divisor so that `D` and `E`
share no component (possible on the finitely many components involved), the
intersection `|D| ∩ |E|` is a closed subscheme of the Noetherian scheme `X` of
dimension `0`, hence has finitely many irreducible components, hence is a finite
set of closed points; each such point lies over a single prime. The `p`-local
components vanish for all other `p`. Moving `D` by `div(f)` changes the local
components by `- v_p(f) . log p . deg(...)`, again nonzero for only finitely
many `p` since `f` has finitely many zeros and poles. `[]`

**Lemma 5.2 (an explicit witness with all primes present).** Let

```
        f(u) := u^{-1/2} exp( - (log u)^2 )       (balanced profile F(x) = e^{-x^2}),
```

so `f in D_theta` for every `theta > 0` (113_07, remark after Lemma 1.4, which
exhibits exactly this function with `f^(s) = sqrt(pi) e^{(s-1/2)^2/4}`). Then

1. `f^* = f`;
2. `z := f * f^*` has balanced profile `(F * F)(x) = sqrt(pi/2) e^{-x^2/2}`, so
   `z(u) = u^{-1/2} sqrt(pi/2) e^{-(log u)^2/2} > 0` for all `u > 0`;
3. for every prime `p`,
   `c_p(f,f) = 2 log p sqrt(pi/2) sum_{k>=1} p^{-k/2} e^{-(k log p)^2/2} > 0`;
4. `sum_p c_p(f,f) < infinity`.

*Proof.* (1) `f^*(u) = conj(f(1/u))/u = u^{-1} . u^{1/2} e^{-(log u)^2} = f(u)`.
(2) Additive convolution of `e^{-x^2}` with itself is `sqrt(pi/2) e^{-x^2/2}`;
113_07 Lemma 1.2(2) says `*` on `D` is additive convolution of profiles.
(3) `z(1/p^k)/p^k = p^{k/2} sqrt(pi/2) e^{-(k log p)^2/2} / p^k = z(p^k)`, so
the bracket doubles the `k`-th term; every term is positive.
(4) `c_p <= 2 log p sqrt(pi/2) p^{-1/2} e^{-(log p)^2/2} / (1 - p^{-1/2})` and
`e^{-(log p)^2/2} = p^{-(log p)/2}` decays faster than any power of `p`. `[]`

Verifier section H checks (1)–(4) numerically: `f^* = f` to 25 digits, the
closed form of `z` against numerical Mellin convolution to 20 digits,
`c_p > 0` for **all 1229 primes below 10^4**, and a tail
`sum_{p in last 100} c_p = 1.4e-17`.

**Theorem 5.3 (no place-wise realisation on a fixed arithmetic surface).** There
is no place-wise realisation (Def 4.2) of `(D_R, s, tau)` in `Ch-hat^1(X)_R` for
a fixed regular projective arithmetic surface `X` over `Spec Z`.

*Proof.* Take `x = y = f` of Lemma 5.2. Place-wise compatibility demands that
the `p`-local component of `(iota f . iota f)` equal `c_p(f,f) != 0` for every
prime `p` (Lemma 5.2(3)) — infinitely many nonzero local components. Lemma 5.1
says there are finitely many. `[]`

**Remark 5.4 (where the escape is, and only there).** Theorem 5.3 uses
*finiteness of the divisor support*, which is exactly what Zhang's adelic line
bundles and Yuan–Zhang's `Pic-hat(X)_int` give up: an adelic metric is a uniform
limit of model metrics (Def 1.2(1)), and a limit may differ from the trivial
metric at infinitely many finite places, with local heights forming a
convergent, infinitely supported sum. Lemma 5.2(4) says the required sum
`sum_p c_p` converges. So the adelic framework is not merely a convenience here:
it is the **unique** known category in which Definition 4.2 is not immediately
contradictory. That is the content of Gap G-3.

**Remark 5.5 (109_04 does not block this).** 109_04 Thm 1.1 shows that any
bilinear form `B_K(f,g) = sum_{n,m} K(n,m) f(n) g(m)` built from a kernel
supported on prime powers has `{f : f(p^k) = 0 for all p,k}` inside its radical,
so the *coefficient side is blind*. That theorem does **not** apply to `tau(x *
y^*)`: the arithmetic side of the explicit formula evaluates the prime powers of
the **convolution** `x * y^*`, not of `x` and `y` separately, and
`(x * y^*)(p^k)` depends on all of `x` and `y`. Verifier section H is an
explicit instance: `f` vanishes at no point at all, and `z = f * f^*` is
strictly positive at every prime power. So the blindness theorem leaves
Definition 4.2 open; it is Lemma 5.1 that kills the non-adelic version.

---

## 6. Gaps

**Gap G-1 (the canonical arithmetic surface).**

> *Statement.* There exist a regular projective arithmetic surface (or an
> adelic-line-bundle space in the sense of Yuan–Zhang Def 1.2 over a finitely
> generated field) `X`, an ample `L-bar`, and an `R`-linear
> `iota : D_R -> Pic-hat(X)_{int,R}` with `ker iota = rad(s)` such that
> `s(x,y) = <iota x, iota y> = iota x . iota y . L-bar^{n-1}` for all
> `x, y in D_R`, **and** `iota` is place-wise compatible in the sense of
> Definition 4.2.
>
> *What would close it.* A construction. By Theorem 5.3 it must be adelic; by
> Lemma 5.2 the target local heights are prescribed real numbers
> `c_p(x,y)` at every prime, so the construction must produce a metric at every
> finite place whose local height reproduces `log p . sum_k [z(p^k) +
> z(p^{-k})/p^k]`. Nothing in this corpus or in the read sources supplies such a
> metric.
>
> *Believed hard.* Yes. This is "Spec Z x_{F_1} Spec Z" in the form in which
> Deninger and Connes have posed it, restricted to what row (d) actually needs.
> It is *not* obviously RH-equivalent — Theorem 4.5 shows the *bare* existence
> statement is, but the place-wise version is a strictly stronger, and therefore
> possibly falsifiable, statement.
>
> **Amendment (added after `114_d3_03` Thm 6.5).** The RH-equivalence is much
> worse than Theorem 4.5 indicates. `114_d3_03` Theorem 6.5 shows that the mere
> existence of an *additive* map `iota : D^o_R -> V` into any `V` with
> `n_+ <= 1` satisfying the one-sided inequality `q(iota c) >= s(c,c)` is already
> equivalent to RH. So **every linear form of G-1 — isometric, place-wise,
> adelic, or merely dominating — is RH-equivalent.** What survives is only a
> non-additive transport (Gap G-8 there).

**Gap G-2 (finite-rank obstruction, not resolved either way).**

> *Statement.* For a fixed regular projective arithmetic surface `X/Spec Z`,
> `Pic(X)` is a finitely generated abelian group, so the image of any `iota` in
> the *algebraic* part has finite rank and the entire infinite-dimensional
> negative definite block of `s` must be carried by metrics/Green functions.
> Determine whether that is compatible with place-wise compatibility.
>
> *What would close it.* Either a proof that Green-function data cannot carry
> prescribed local heights at infinitely many finite places (which would close
> G-1 negatively and end row (d)), or a construction (which is G-1).
>
> *Believed hard.* The finite generation itself is standard (Mordell–Weil plus
> finiteness of bad fibres) and is **not proved here**; the compatibility
> question is open. Flagged as a gap and not used in any theorem above.

**Gap G-3 (the adelic version of Theorem 5.3).**

> *Statement.* Decide whether Definition 4.2 can be satisfied in
> `Pic-hat(X)_int` for adelic line bundles: i.e. whether there is an adelic
> metric whose local heights at the finite places realise `(c_p(x,y))_p` for all
> `x,y in D_R` simultaneously and bilinearly.
>
> *What would close it.* Yuan–Zhang's local decomposition of `M-bar_1 . M-bar_2
> . L-bar^{n-1}` into local heights, applied to the specific system
> `(c_p)_p`. This requires reading Yuan–Zhang I section 3 and Yuan–Zhang II
> (`arXiv-1304.3539v2`, present locally, **not read**), which is the next
> concrete step for this lens.
>
> *Believed hard.* Unknown. This is the one place where a finite amount of
> reading might produce a decisive answer, in either direction.

---

## 7. Refutation conditions

Numbered continuing the ledger of 113_15, whose last entry is R23.

- **R24.** If any truncation of `s` built from genuine zeros, of any size, is
  found with `n_+ != 1 + 2b` (`b` = number of off-line quadruples in the
  truncation), Theorem 2.5 is wrong and section 3 collapses.
- **R25.** If an isometric realisation (Def 4.1) is ever exhibited *without*
  place-wise compatibility and is claimed to prove RH, it must be rejected: by
  Theorem 4.5 its existence is RH-equivalent, so the claim is circular. Any file
  in this phase that does so fires R25.
- **R26.** If a place-wise realisation is exhibited on a **fixed** regular
  arithmetic surface (not adelic), Theorem 5.3 is wrong: either Lemma 5.1 fails
  or the witness of Lemma 5.2 is not in `D`.
- **R27.** If `c_p(f,f) = 0` for some prime `p` and the witness `f` of
  Lemma 5.2, Theorem 5.3's proof fails. (Checked for all `p < 10^4`.)
- **R28.** If the realification of `s` (rather than the real form `D_R`) is ever
  used as the comparison object in an import argument, the argument is wrong by
  Prop 2.4, whatever it concludes.

---

## 8. Verifier output

Real output of `python3 114_d3_01_imported_index_theorems.py`, run in this
session (43 checks; abbreviated — full listing reproduced by re-running):

```
A. ruling arithmetic (113_09 Thm 4.1, 113_10 Thm 1.2)
PASS  s(H,H) = 2                                   [2.0]
PASS  s(f_v,f_h) = 1                               [1.0]
PASS  s(f_v-f_h, f_v-f_h) = -2                     [-2.0]
PASS  polar block is Lorentzian (1,1)

B. inertia on increasing truncations, GENUINE zeros of zeta
computing 60 genuine zeta zeros with mpmath.zetazero ...
gamma_1 = 14.134725142 ... gamma_60 = 163.030709687
PASS  real form,  1 on-line zeros: (n_+,n_0,n_-) = (1,0,3), predicted (1,0,3)
   ...
PASS  real form, 60 on-line zeros: (n_+,n_0,n_-) = (1,0,121), predicted (1,0,121)
PASS  n_+ does NOT grow with the truncation (positive index stays 1)
      [tested up to 60 zeros = dimension 122]
PASS  Hermitian n_+ also stays 1 (107_241 Thm 3.1 with #P = 0)

C. planted off-line zeros:  n_+ = 1 + 2 * (# off-line quadruples)
PASS  real form, 1 off-line quadruple(s): n_+ = 3, predicted 3
PASS  real form, 2 off-line quadruple(s): n_+ = 5, predicted 5
PASS  real form, 3 off-line quadruple(s): n_+ = 7, predicted 7
PASS  Hermitian, 1 off-line quadruple(s) = 2 mirror 2-cycles: n_+ = 3, predicted 3
PASS  Hermitian, 2 off-line quadruple(s) = 4 mirror 2-cycles: n_+ = 5, predicted 5

D. reproduction of the two signatures reported in 113_12 section 4
PASS  113_12's on-line model: (n_+,n_-) = (1,7), reported (1,7)
PASS  113_12's off-line model: (n_+,n_-) = (3,5), reported (3,5)

E. the doubling trap
PASS  Hermitian inertia (1,9)
PASS  real form inertia (1,9) EQUALS the Hermitian inertia
PASS  realification inertia (2,18) = (2p,2q) -- the trap
PASS  realification is NOT Lorentzian (n_+ = 2): comparing it to an arithmetic
      surface form would falsely refute the import

F. Gram matrix of s on actual functions in D (high precision)
Gram entries range: |G_00| = 7.11978, |G_77| = 97.5605
PASS  real Gaussian-Hermite basis (8 functions, 3 genuine zeros): inertia (1,4,3)
      [n_+ = 1 as predicted for a Lorentzian form under RH]
PASS  same basis, one off-line quadruple planted: inertia (3,3,2), n_+ > 1

G. Yuan-Zhang shape (arXiv:1304.3538v1, paragraph after Thm 1.3) => n_+ = 1
PASS  V isotropic + <V,L> != 0 + V^perp/V negative definite ==> inertia (1,0,n-1)
      in 200 random instances
PASS  polar hyperbolic + negative definite + 1-dim radical ==> (1,1,n-2): the
      shape of s under RH, in 200 random instances

H. witness  f(u) = u^{-1/2} exp(-(log u)^2)  and z = f * f^*
PASS  f^* = f (the witness is self-adjoint)
PASS  z(0.5) = (f * f)(0.5) matches the closed form  [num=1.39394580739 closed=1.39394580739]
PASS  z(2.0) = (f * f)(2.0) matches the closed form
PASS  z(7.0) = (f * f)(7.0) matches the closed form
PASS  c_p != 0 for every one of the 1229 primes below 10^4
      [min c_p = 8.9941e-20 at p = 9973]
PASS  c_p is strictly positive (so the support of the prime decomposition of
      tau(f * f^*) is ALL primes, an infinite set)
PASS  sum_p c_p converges (tail over the last 100 primes < 1e-8) [tail = 1.42293e-17]

checks run: 43      failures: 0
VERDICT: ALL CHECKS PASS
```

---

## 9. Scope

### Proved here

- Prop 1.5: the Yuan–Zhang signature statement forces `n_+ = 1` (Lorentzian),
  with radical `V = pi^* Pic-hat(K)_Q`.
- Prop 1.6: on an arithmetic surface the archimedean block `(0,g)` is negative
  semi-definite with radical the constants — derived from Theorem 1.1, not
  assumed.
- Lemma 2.2, Lemma 2.3, Prop 2.4: the real form of `s` is the correct
  comparison object; the realification doubles the inertia.
- Theorem 2.5 and Theorem 3.1: the blockwise real signature, and `n_+ = 1` on
  every truncation under RH. This resolves the brief's cheap decisive test in
  the *negative for the worry*, i.e. the lens is not closed.
- Theorem 4.3 (a realisation implies RH), Theorem 4.4 (RH implies a
  realisation), Theorem 4.5 (so bare realisation is RH-equivalent, hence a
  circular target).
- Lemma 5.1 (finite support of arithmetic local intersection), Lemma 5.2 (an
  explicit `f in D` with `c_p(f,f) > 0` for every `p`), Theorem 5.3 (no
  place-wise realisation on a fixed arithmetic surface).

### Read from source

- Yuan–Zhang, arXiv:1304.3538v1, Theorem 1.1 (= Faltings–Hriljac–Moriwaki),
  Definition 1.2, Theorem 1.3, and the signature paragraph following Theorem
  1.3 — quoted verbatim in section 1, read in full at
  `00-references/papers-nuevos/D/arXiv-1304.3538v1` lines 339–395.
- 107_241 section 3: the definitions of `L` and `P`, Theorem 3.1, Corollaries
  3.2 and 3.3 — read in full; the brief's paraphrase corrected in section 0.
- 113_12 Theorem 4.1 (Hodge index `<=>` RH) with its proof; 113_12 Def 1.1 and
  Thm 1.3 (the trace); 113_09 `s(H,H) = 2`; 113_07 Def 1.3 and the remark after
  Lemma 1.4 (the Gaussian witness lies in `D_theta` for every `theta`, with
  `f^(s) = sqrt(pi) e^{(s-1/2)^2/4}`); 109_04 Thm 1.1 (coefficient-side
  blindness).

### Verified numerically

- `n_+ = 1` on truncations of dimension up to 122 built from 60 genuine zeta
  zeros; `n_+ = 1 + 2b` with planted off-line quadruples; the two signatures
  `(1,7)`, `(3,5)` of 113_12; the doubling trap `(1,9) / (1,9) / (2,18)`; the
  function-level Gram matrix at 60 digits; the Yuan–Zhang signature shape on 400
  random instances; the witness `f`, `z = f * f^*`, and `c_p > 0` for all
  1229 primes below `10^4`.

### Not established

- Gap G-1: the canonical place-wise realisation. **Not constructed.**
- Gap G-2: whether the finite rank of `Pic(X)` obstructs place-wise
  compatibility. The finite generation of `Pic(X)` is asserted as standard and
  **not proved here**, and is used nowhere above.
- Gap G-3: whether the adelic category evades Theorem 5.3. **Not decided**;
  requires Yuan–Zhang I section 3 and II, present locally and not read.
- Nothing in this file proves RH, and by Theorem 4.5 nothing of the shape
  "import an abstract index theorem" can.
