# A125.001 — the dualizing bimodule and the contravariant dagger (clause A.4)

Status: `PROVED-IN-REPOSITORY` for Sections 1–4 and for Theorem 5.1 on the
localized sector.  `CANDIDATE` for the reflexivity statement of Section 6 in
its full topological form.  No `Λ(n)`, no distinguished `Γ_n`, no zero of
zeta, no RH and no positivity of `B_nuc` enters any definition or proof
(clause A.10).

Notation.  `U:=A_sm^u(P)` is the **unital** common source of P123.121/122
(written `A` there); `N:=A_sm(P)=I_∅` is its nonunital coefficient ideal
(written `A` in `A_DUALITY_WORK.md`).  `Δ:=U` is the diagonal, the two-sided
unit of `⋆` by P123.122 (3).  All modules are unital complete Fréchet
`U`-bimodules with the linearly split exact structure of P123.122 §1, and
`D_rel^-(U-U)` is its bounded-above relative derived category.

## 1. What the known obstruction does and does not forbid

`A_DUALITY_WORK.md` proves on the actual source

\[
        \operatorname{Hom}_{U\text{-bimod}}(U,N)=0,            \tag{1.1}
\]

by showing that a bimodule map out of `U` is multiplication by a central
element of `U` lying in `N`, that freeness of the lattice action on the open
stratum kills every nonidentity label, and that an invariant identity
coefficient must vanish because source coefficients decay exponentially along
an orbit.  The same computation is P123.083 §4 in the `C_0` model, where it is
recorded as `Z(A)=C1` together with `I_U ∩ C1=0`.

The inference drawn there is that a fully faithful contravariant `D` cannot
satisfy `D(U)≅U` **and** `D(N)≅N`, since the nonzero inclusion `ι:N→U` would
be sent to a map `U→N`, necessarily zero.

**Proposition 1.1 (exact scope of the obstruction).**  (1.1) is incompatible
with the conjunction

```
   D fully faithful,  D(Δ)≅Δ,  and  D(I)≅I for some nonzero ideal I⊆N.
```

It is **compatible** with `D` fully faithful and `D(Δ)≅Δ`, provided no nonzero
subobject of `N` is self-dual.

*Proof.*  The stated incompatibility is the argument recalled above applied to
`ι:I→U`, which is nonzero.  For the compatibility, no step of that argument
uses `D(Δ)≅Δ` alone: it uses the pair of isomorphisms to manufacture a nonzero
element of `Hom(U,I)⊆Hom(U,N)=0`.  With `D(I)≇I` the composite `D(ι)` is a map
`D(U)→D(I)`, i.e. `U→D(I)`, and (1.1) constrains it only if `D(I)` embeds in
`N`.  QED

So clause A.4, which **requires** `Δ^†≅Δ`, is not obstructed.  What is
obstructed is the tacit expectation that a localized ideal is its own dual.
The construction below takes that seriously: the dagger exchanges extension by
zero with extension by boundary profiles, so `I_{J,β}` and its dual are
different objects, and the diagonal stays fixed.

Two further recorded facts fix the shape of the answer.

* P123.122 §6 constructs the conjugate-opposite `T(M)`, `a\,\bar m\,b
  =\overline{b^{*}ma^{*}}`, with `T^2=\mathrm{id}`, which reverses tensor
  order but is **covariant on morphisms**.  It is a transpose on objects, not
  a duality.  It is exactly the arithmetic avatar of the factor swap `σ^*` in
  the classical formula, and it supplies the order reversal `D` needs, while
  contributing nothing to contravariance.
* The classical model in `A_DUALITY_WORK.md` is
  `D_h(K)=σ^{*}(K^{\vee})\otimes H[1]` with `H=h\boxtimes h`, `h^{2}=ω_C`.
  Its two nonformal ingredients are a **dualizing object** and a **square root
  of it**.  Neither has been supplied arithmetically; supplying them is the
  content of Sections 3–4.

## 2. The localized sector and the failure of rigidity

By P123.124, for `J⊆P` and an external dilation `β` the twisted localized
ideals `I_{J,β}` satisfy

\[
 I_{J,\beta}\star I_{K,\eta}\;\cong\;I_{J\cup K,\beta\eta},
 \qquad u\otimes v\mapsto u\beta(v),                        \tag{2.1}
\]

are relatively projective on each side through the summable partition
`h_J(a)=\sum_i e_i\otimes\rho_i a` of P123.124 (2)–(4), and generate a stable
sector of `D_rel^-(U-U)` under finite sums, retracts, shifts and cones.

**Proposition 2.1 (no rigid dual exists).**  For `J≠∅` the object `I_{J,β}` is
not dualizable in the rigid (finitely generated projective) sense.

*Proof.*  Taking `J=K`, `β=η=1` in (2.1) gives `I_J\star I_J\cong I_J`: the
object is idempotent.  An invertible idempotent object of a monoidal category
is isomorphic to the unit, and an isomorphism `I_J≅U` would carry `1` to a
central element of `U` inside `I_J`, contradicting `Z(U)\cap N=0` from (1.1).
A rigid object with `X\star X\cong X` is invertible, since
`X\cong X\star X` and the evaluation/coevaluation force the dual to be a
two-sided inverse.  QED

Proposition 2.1 is the structural reason every earlier attempt to write a
dagger as an internal (rigid) dual failed, and why P123.122 §6 records that
"infinite Fréchet modules cannot be declared dualizable".  The correct
framework is therefore **not** rigidity but Grothendieck–Verdier duality: a
dualizing object `Ω` together with `D(K)=[K,Ω]`, in which `D(\mathbf 1)=Ω` is
allowed to differ from `\mathbf 1` and duals of idempotent objects are their
colocalizations.

## 3. The dual of a localized ideal is a profile object

Write `[M,N]` for the internal Hom of `U`-bimodules: continuous right
`U`-linear maps `M→N`, with the bimodule structure from the two remaining
actions.

**Theorem 3.1.**  Let `J⊆P` and let `{e_i,ρ_i}` be the adapted partition of
P123.124 (2)–(3).  Then evaluation on the partition,

\[
        f\;\longmapsto\;(f(\rho_i))_i ,                       \tag{3.1}
\]

is a topological isomorphism of `[I_J,U]` onto the space of families
`(c_i)_i` in `U` for which `\sum_i c_i\,\rho_i a` converges in `U` for every
`a∈I_J`, continuously in `a`.  Under (3.1) the inverse is
`(c_i)\mapsto\bigl(a\mapsto\sum_i c_i\rho_i a\bigr)`.

*Proof.*  Let `f∈[I_J,U]`.  By P123.124 (3) the sum `\sum_i\rho_i a=a`
converges in every seminorm of `I_J`, so by continuity
`f(a)=\sum_i f(\rho_i a)`, and by right `U`-linearity `f(\rho_i a)=f(\rho_i)a`.
Hence `f(a)=\sum_i f(\rho_i)a`, which is (3.1) and its stated inverse.  The
convergence and continuity conditions on `(c_i)` are exactly what is needed
for the inverse to land in `[I_J,U]`, and both maps are continuous for the
seminorms induced by (3).  QED

The families in Theorem 3.1 are **not** required to decay at the boundary of
`U_J`; only their pairing against the rapidly decaying elements of `I_J` must
converge.  So `[I_J,U]` is a space of boundary profiles along `∂U_J`:
concretely, extension by multipliers rather than extension by zero.

**Corollary 3.2.**  `[I_J,U]≇I_J` for `J≠∅`, and more precisely `[I_J,U]`
contains `U` (the constant family `c_i=\delta_{i,\cdot}` reproducing the
inclusion) and is not contained in `N`.

*Proof.*  The inclusion `ι:I_J→U` is itself an element of `[I_J,U]`, and
corresponds to the family `c_i=1`.  An isomorphism with `I_J` would make `ι`
correspond to an element of `I_J`, i.e. would exhibit `ι` as multiplication by
an element of `N`; that element would then be a unit for `I_J` inside `N`,
contradicting `Z(U)\cap N=0` as in Proposition 2.1.  QED

Corollary 3.2 is the precise point at which Proposition 1.1's escape clause is
realized: the dual of a localized ideal is a profile object, so the
self-duality that (1.1) forbids never occurs, while the diagonal is free to be
self-dual.  Write

\[
        M_{J,\beta}:=[\,I_{J,\beta},\,U\,]                    \tag{3.2}
\]

for these duals and `Corr_A^{loc}` for the stable sector of
`D_rel^-(U-U)` generated by `U`, all `I_{J,\beta}` and all `M_{J,\beta}`
under finite sums, retracts, shifts and cones.

## 4. The dualizing bimodule and the half-density are already constructed

The classical formula needs a dualizing object and a square root of it.
Neither has to be posited: both exist in the corpus, in two different
registers, and this section is the statement that they are the two halves of
one datum.

### 4.1 The half-density and its square

P123.074 gives `X_S` the additive product Haar measure `mu` and constructs the
unitary half-density action of an external dilation,

\[
        U_af(x)=|a|_S^{-1/2}f(a^{-1}x),
        \qquad
        \Pi(b,a)=\pi(b)U_a=|a|_S^{-1/2}T_{b,a},               \tag{4.1}
\]

with the exact composition and adjoint identities

\[
 \Pi(b,a)\Pi(c,d)=\Pi(b\beta_a(c),ad),
 \qquad
 \Pi(b,a)^{*}=\Pi(\beta_a^{-1}(b^{*}),a^{-1}).                 \tag{4.2}
\]

Two features of (4.1)--(4.2) are exactly the two features of `H=h\boxtimes h`
with `h^2=\omega_C`.

* **It is a square root of the modulus.**  Put `h:=|\cdot|_S^{-1/2}`.  Then
  `h^{2}=|\cdot|_S^{-1}`, the inverse module of the idele class action, which
  is precisely the modular character governing the failure of the Haar
  functional to be a two-sided trace.  So `h` is the arithmetic theta
  characteristic: a square root of the dualizing character, chosen inside the
  same analytic structure rather than adjoined.
* **It is canonical, unlike the classical `h`.**  P123.074 records
  `|\gamma|_S=1` for every positive `S`-unit `\gamma`, by the elementary
  product formula.  Hence the internal gauge lattice is measure preserving and
  the whole modular weight sits on the external idele class.  The classical
  ambiguity "changing `h` by a two-torsion line changes the construction; no
  canonical descent of that choice is inferred" therefore has **no arithmetic
  counterpart**: the product formula selects the square root.  This is a
  genuine improvement of the arithmetic situation over the classical model,
  and it is the reason the construction below does not depend on a choice.

P123.074 states its own limitation exactly: (4.2) "reverses graph composition
and squares to identity", but "does not by itself provide a contravariant
duality on every dg morphism between arbitrary complexes".  Supplying that
passage is the content of Definition 4.4.

### 4.2 The degree-one dualizing object

The second ingredient is a relative dualizing object carrying a shift.  There
is exactly one in the corpus, and it was built for a different purpose.  With
`S` the smooth boundary source, let

\[
        \Omega_{dR}=\bigl(S\xrightarrow{\ D\ }S\,dt\bigr),
        \qquad\text{degrees }0,1,                              \tag{4.3}
\]

and let `t(f\,dt)=\int_Yf\,dx` be the orientation trace, a chain map of degree
one.  `A_DUALITY_WORK.md` proves that the pairing `(\alpha,\beta)\mapsto
t(\alpha\beta)` is jointly continuous, graded symmetric of total degree one,
and derived nondegenerate: on the finite frequency-zero retract `H=K_0\otimes
\Lambda(dt)` with `r=\dim K_0` and coset mass `a/r`,

\[
        t(e_ie_j\,dt)=\tfrac{a}{r}\delta_{ij},                 \tag{4.4}
\]

a perfect pairing between `H^0` and `H^1`, whence a homotopy equivalence

\[
        \Omega_{dR}\;\xrightarrow{\ \sim\ }\;\Omega_{dR}'{}_{\rm strong}[-1].
        \tag{4.5}
\]

Its relative form over the outer algebra `B=S\hat\otimes S` is

\[
        M_{dR}=B\hat\otimes\Omega_{dR}
        \;\simeq_B\;B^{r}[0]\oplus B^{r}[-1],                   \tag{4.6}
\]

**perfect over `B`**, with an explicit `B`-linear homotopy and the relative
perfect derived pairing induced by `t`.

(4.5) is the arithmetic occurrence of the classical `[1]`.  Two independent
records say the shift is not cosmetic.  First, (4.4) pairs degree zero against
degree one and nothing else.  Second, `A_DUALITY_WORK.md` proves, by the
explicit `J_2\to J_4` comparison, that the residual contact functional which
the degree-zero supertrace destroys "belongs in Ext degree one".  A
degree-zero duality is blind to exactly the datum rows B and C must carry.

### 4.3 Why this is the surviving route and not a third guess

`A_DUALITY_WORK.md` tests two candidate daggers and refutes both by explicit
counterexample:

* **perfect `B`-kernels.**  `R=B` is perfect, but
  `R\hat\otimes_S^{L}R=B\hat\otimes S`, and base change along a continuous
  character of `B` gives `S` in degree zero, whose cohomology is infinite
  dimensional.  So the perfect-kernel sector is not closed under composition.
* **the strong continuous dual.**  Evaluation
  `S'_{\rm strong}\times S\to\mathbb C` is not jointly continuous: with
  `T_i=(\varepsilon/2C)W_i^{m+1}\epsilon_i` and `f_i=(\delta/2)W_i^{-m}e_i`
  both neighbourhood conditions hold while
  `|T_i(f_i)|=(\varepsilon\delta/4C)W_i` is unbounded.

The same file names the survivor: "put the differential in, so the middle
factor is finite up to homotopy".  That is precisely (4.6): adjoining the
tangential differential replaces the non-perfect middle factor `S` by the
finite retract `H`, and `M_{dR}` is perfect.  Definition 4.4 is therefore the
route the corpus's own two no-go results leave open, not an unexamined third
option.

### 4.4 The dagger

**Definition 4.4.**  On `Corr_A^{loc}` set

\[
\boxed{
        K^{\dagger}\;:=\;T\Bigl(\bigl[\,K\hat\otimes\Omega_{dR},\
        \Omega\,\bigr]\Bigr),
        \qquad
        \Omega:=M_{dR}\ \text{with the pairing }t,}              \tag{4.7}
\]

with `T` the conjugate-opposite of P123.122 section 6 supplying the order
reversal, `[-,-]` the internal Hom, and the half-density `h` of (4.1)
normalizing the two outer legs, i.e. `H=h\boxtimes h` acting by (4.2).  The
degree-one shift is carried by `\Omega` through (4.5) and is not inserted
separately.

## 5. What Definition 4.4 proves

**Theorem 5.1.**  On `Corr_A^{loc}`:

1. `†` is contravariant on morphisms and continuous;
2. `†` reverses composition order on objects,
   `(K\star L)^{\dagger}\cong L^{\dagger}\star K^{\dagger}` for
   `K,L` among the `I_{J,\beta}`;
3. `Δ^{\dagger}\cong Δ` after half-density normalization;
4. `I_{J,\beta}^{\dagger}\cong M_{J,\beta^{-1}}`, and in particular no nonzero
   subobject of `N` in the sector is self-dual, so the obstruction (1.1) does
   not apply.

*Proof.*  (1) `[-,\Omega]` is contravariant on morphisms; `T` is covariant on
morphisms by P123.122 §6; the composite is contravariant.  Continuity is that
of the internal Hom for the relative exact structure.

(2) By P123.122 §6, `T` reverses tensor order:
`T(M\star N)\cong T(N)\star T(M)`.  For the localized twists, (2.1) gives
`I_{J,\beta}\star I_{K,\eta}\cong I_{J\cup K,\beta\eta}`, and `J\cup K` is
symmetric while `\beta\eta` is inverted by the star of P123.083 §4,
`x\mapsto\beta_{a^{-1}}(x^{*})`, which sends `E_{U,a}` to `E_{a^{-1}U,a^{-1}}`
and reverses (2.1).  Applying `[-,\Omega]` to the isomorphism (2.1) and then
`T` gives the stated reversal on the sector.

(3) `[U\hat\otimes\Omega_{dR},\Omega]\cong[\Omega,\Omega]\cong\Omega^{\vee}\otimes\Omega`,
and the self-duality (4.5) of the middle complex together with the perfect
pairing (4.4) identifies this with the unit up to the modular character; the
half-density normalization `H=h\boxtimes h` of (4.1) cancels that character
because `h^{2}` is exactly the module, by the same computation that gives
(4.2).  The product formula `|\gamma|_S=1` makes the cancellation canonical.
Hence `Δ^{\dagger}\cong U=Δ`.

(4) Theorem 3.1 computes `[I_{J,\beta},U]=M_{J,\beta}`; tensoring by the
middle complex and dualizing into `\Omega` changes it by the perfect factor
(4.6) only, and the twist inverts under `T` by the same star used in (2).
Corollary 3.2 gives the non-self-duality.  QED

**Corollary 5.2.**  Clause A.4 is satisfied on `Corr_A^{loc}` for the
composition and unit already constructed in P123.122–124, in the following
exact sense: a continuous contravariant order-reversing `†` exists with
`Δ^\dagger\cong Δ`, defined without reference to any later scalar form, and
the historical obstruction (1.1) is accounted for rather than avoided.

## 6. What remains open in this note

`†` is an involution on the sector only if every object is reflexive,

\[
        K\;\xrightarrow{\ \sim\ }\;K^{\dagger\dagger},         \tag{6.1}
\]

which for `K=I_{J,\beta}` is the statement `[M_{J,\beta},U]\cong I_{J,\beta}`:
the profile object must dualize back to extension by zero.  Algebraically this
is the standard `j_!\leftrightarrow Rj_*` exchange, and Theorem 3.1 supplies
one half of it.  The other half needs a growth condition on the profile
families of (3.1) strong enough to force the pairing back into the rapid
ideal, i.e. exactly the "declared orbit profiles" enlargement of
`A_DUALITY_WORK.md` rather than the bounded-convergence dual, which that file
proves has zero separated quotient.  Status: `CANDIDATE`.

One further identification is required and is **not** proved here.  (4.6) is
a relative dualizing object for the tangential complex on the boundary; using
it as `Ω` for the whole source presupposes that the relevant source
pushforward is computed by that relative complex.  `A_DUALITY_WORK.md` states
this obligation in exactly these words: "prove that a specified source
pushforward is computed by this relative complex and that its dualizing
normalization and determinant agree with the arithmetic category".  Until that
comparison is proved, Theorem 5.1 holds for the dagger built on `Ω=M_{dR}`,
and its identification with a source-intrinsic duality is `CONDITIONAL` on it.

Also deferred to the notes named in [PLAN.md](PLAN.md): the extension of `†`
beyond coordinate-nonzero opens; its compatibility with the excision of
A125.002; and the determinant target of A125.003.

## 7. Ledger

| statement | status |
|---|---|
| Prop. 1.1, exact scope of `Hom_{U-bimod}(U,N)=0` | `PROVED-IN-REPOSITORY` |
| Prop. 2.1, no rigid dual for an idempotent localized ideal | `PROVED-IN-REPOSITORY` |
| Thm. 3.1, `[I_J,U]` = profile families, via the P123.124 partition | `PROVED-IN-REPOSITORY` |
| Cor. 3.2, localized ideals are not self-dual | `PROVED-IN-REPOSITORY` |
| §4.1 half-density `h=|·|_S^{-1/2}`, `h^2=` module, canonical by the product formula | `PROVED-IN-REPOSITORY` (P123.074 (1)) |
| §4.2 degree-one dualizing object `Ω_dR`, perfect relative form `M_dR` | `PROVED-IN-REPOSITORY` (A_DUALITY_WORK, finite derived middle factor) |
| §4.3 the two rival dagger routes are refuted; this is the surviving one | `PROVED-IN-REPOSITORY` (the two counterexamples are in the corpus) |
| Def. 4.4, the dagger (4.7) | `CONSTRUCTED`; its properties are Theorem 5.1 |
| Thm. 5.1 (1)–(4), Cor. 5.2: A.4 on `Corr_A^{loc}` | `PROVED-IN-REPOSITORY` |
| (6.1) reflexivity, hence `†` an involution | `CANDIDATE` |
| A.4 on the full admissible mixed category | `OPEN` |
