# P124.013 -- the entire-function form, and the shielding dichotomy for Gate R

Status: `PROVED-IN-REPOSITORY` for Sections 1--4 (a dictionary and a
dichotomy).  `OPEN` for the sign itself.  No zero of zeta, no positivity of
`B_nuc` and no row-(d) statement is used in any proof below.

This note replaces the coordinate in which Gate R has been attacked since
P124.005.  Gate R has been carried as a statement about an **unknown**
first-contact minimizer: `<rho_{+,T},F_*>=0`.  The theorem below shows it is
equivalent to a statement with **no unknown vector in it at all**: survival of
the *unconstrained* Weil form at the first contact of the *constrained* one.

## 1. The dictionary

For real `F in C_c^infty(R)` put

\[
        \Phi_F(s)=\int_{\mathbb R}F(t)e^{(s-1/2)t}\,dt .   \tag{1.1}
\]

`Phi_F` is entire, `Phi_F(\bar s)=\overline{\Phi_F(s)}`, and by Paley--Wiener
`supp F\subset[-T,T]` iff `Phi_F` has exponential type `<=T` in `s-1/2`.
The two Tate moments of the corpus are values of `Phi_F`:

\[
        M_+(F)=\int e^{t/2}F=\Phi_F(1),
        \qquad
        M_-(F)=\int e^{-t/2}F=\Phi_F(0).                   \tag{1.2}
\]

Hence the primitive space is a **two-point interpolation condition**:

\[
\boxed{
        F\in\mathcal P_T
        \quad\Longleftrightarrow\quad
        \Phi_F(0)=\Phi_F(1)=0 .}                            \tag{1.3}
\]

Let `rho` run over the nontrivial zeros of `zeta` with multiplicity.  Weil's
explicit formula in the normalization of P123.036 (1.1) and of paper 42
`eq:localizedprimitiveoperator` reads, for real `F` supported in `I_T`,

\[
\boxed{
        \mathcal W(F):=\sum_\rho \Phi_F(\rho)\Phi_F(1-\rho)
        =2\,\Phi_F(0)\Phi_F(1)+\langle\mathscr A F,F\rangle ,}
        \tag{1.4}
\]

with

\[
 \mathscr A=g_\Gamma(D)-m_0I
   -\sum_{n\ge2}{\Lambda(n)\over\sqrt n}(S_{\log n}+S_{-\log n}),
 \qquad
 g_\Gamma(\tau)-m_0=\operatorname{Re}\psi(\tfrac14+\tfrac{i\tau}2)-\log\pi .
\]

The sum in (1.4) is taken in the symmetric order `|\Im\rho|\le X`,
`X\to\infty`; the zero multiset is stable under `rho\mapsto1-\rho` and
`rho\mapsto\bar\rho`, so `\mathcal W(F)` is real.

Two immediate consequences fix the bookkeeping used below.

**Lemma 1.1 (exact truncation).**  For `supp F\subset[-T,T]` and
`\log n\ge2T` one has `\langle S_{\log n}F,F\rangle=0`, and moreover
`(S_{\pm\log n}F)|_{I_T}=0`.  Hence `\mathscr A F|_{I_T}=\mathscr A_TF|_{I_T}`
with the finite operator `\mathscr A_T` of P124.005 (1.1), both as a form and
pointwise on the window.  *Proof:* `S_{\log n}F` is supported in
`[-T+\log n,T+\log n]`, which meets `I_T` only if `\log n<2T`.  QED

**Lemma 1.2 (window independence and nesting).**  `\mathcal W(F)` and
`q(F):=\langle\mathscr A F,F\rangle` depend on `F` alone, not on the window
used to compute them; and by (1.3) the primitive condition is
window-independent, so

\[
 S\le T\ \Longrightarrow\
 \mathcal P_S\subset\mathcal P_T,\quad \mathcal Q_S\subset\mathcal Q_T .
\]

Consequently the two positivity sets

\[
 \{T:\ q\ge0\text{ on }\mathcal P_T\cap\mathcal Q_T\},
 \qquad
 \{T:\ \mathcal W\ge0\text{ on }\mathcal Q_T\}
\]

are intervals.  Write `T_q` and `T_{\mathcal W}` for their suprema.  Since the
second test class contains the first, `T_{\mathcal W}\le T_q`. QED

Both `T_q=\infty` and `T_{\mathcal W}=\infty` are equivalent to RH: the first
is the row-(d) target, the second is Weil's criterion in its unconstrained
form.

## 2. The Weil form as a two-by-two bordered form

Fix `T>\log2`.  In `L^2(I_T)` write `phi_\pm(t)=e^{\pm t/2}\mathbf 1_{I_T}`;
these are the Riesz representers of `M_\pm`, so

\[
 L^2(I_T)=\mathcal P_T\oplus\mathcal T_T,
 \qquad \mathcal T_T=\operatorname{span}\{\phi_+,\phi_-\},
\]

and the same splitting holds on the closed form domain `\mathcal Q_T` (both
`phi_\pm` lie in the logarithmic Gamma form domain).  Relative to it,
`\mathcal W` has the block matrix

\[
\boxed{
 \mathcal W\ \simeq\
 \begin{pmatrix} L_T & X_T\\ X_T^{*} & B_T\end{pmatrix},}
 \tag{2.1}
\]

whose entries are computed from (1.4) as follows.

**(1,1) block.** For `F_0,G_0\in\mathcal P_T` the polar term of (1.4) vanishes
by (1.3), so it is `\langle\mathscr A F_0,G_0\rangle=\langle L_TF_0,G_0\rangle`
with `L_T=P_T\mathscr A_TP_T`: the row-(d) operator itself.

**Crossblock.** For `F_0\in\mathcal P_T` the polar term again vanishes, and

\[
 (X_T)_\sigma(F_0)=\mathcal W(F_0,\phi_\sigma)
 =\langle\mathscr A F_0,\phi_\sigma\rangle
 =M_\sigma(\mathscr A_TF_0)=J_\sigma(F_0)
 =\langle\rho_{\sigma,T},F_0\rangle .                      \tag{2.2}
\]

So the crossblock **is** the Tate collar of P124.005 (3.4), with
`rho_{+,T}=P_T(e^{t/2}\Phi_{+,T})`.  This identifies the D.190 crossblock of
P124.011 (4.3) as the border of the unconstrained Weil form; it is not an
analogy.

**Tate block.** `(B_T)_{\sigma\tau}
 =\langle\mathscr A\phi_\sigma,\phi_\tau\rangle
  +\Phi_{\phi_\sigma}(0)\Phi_{\phi_\tau}(1)
  +\Phi_{\phi_\sigma}(1)\Phi_{\phi_\tau}(0)`, with

\[
 \Phi_{\phi_+}(1)=\Phi_{\phi_-}(0)=2\sinh T,
 \qquad
 \Phi_{\phi_+}(0)=\Phi_{\phi_-}(1)=2T,                     \tag{2.3}
\]

the Gram matrix already used in P121_RESOLVED_TATE_COLLAR_INTEGRAL (4.2).

**Proposition 2.1 (Schur/Douglas for (2.1)).**
`\mathcal W\ge0` on `\mathcal Q_T` if and only if

\[
 L_T\ge0,\qquad
 \Pi_{\ker L_T}X_T=0,\qquad
 \Sigma(T):=B_T-X_T^{*}L_T^{\dagger}X_T\ \ge0 .            \tag{2.4}
\]

*Proof.*  This is the closed-form Schur complement recalled in P124.011
(3.2)--(3.4), applied to the two-dimensional border `\mathcal T_T` instead of
an abstract shell.  QED

Note what has changed relative to P124.011: there the augmented block (4.4)
was an *auxiliary* object with a free parameter `d`, and its positivity was
"not supplied by the positivity already proved".  Here `B_T` is not free.  It
is the Weil form's own Tate block, and (2.1) is not an enlargement of the
problem but the problem before the primitive constraint was imposed.

## 3. The shielding dichotomy

**Theorem 3.1.**  Let `T_*=T_q` be the first contact of the primitive form,
and let `K_{T_*}=\ker L_{T_*}\cap\mathcal P_{T_*}\ne\{0\}` be its radical
(P122.002).  Then exactly one of the following holds.

1. **(Gate R holds at `T_*`.)** `J_\sigma(F)=0` for every `F\in K_{T_*}` and
   `sigma=\pm`; equivalently `\Pi_{K_{T_*}}\rho_{\pm,T_*}=0`.
2. **(Shielding.)** `\mathcal W` is indefinite on `\mathcal Q_{T_*}`, i.e. the
   unconstrained Weil form has already lost its sign at the window where the
   constrained one is still nonnegative.

Moreover, in case 1 and with `\Sigma(T_*)\ge0`, `\mathcal W\ge0` on
`\mathcal Q_{T_*}`; in case 2, `T_{\mathcal W}\le T_q` with `\mathcal W`
failing at `T_q` itself.

*Proof.*  Suppose 1 fails: there are `F_0\in K_{T_*}` and `sigma` with
`J_\sigma(F_0)\ne0`.  Let `z\in\mathbb R^2` be the vector with components
`J_\pm(F_0)`, not zero, and for `eps\in\mathbb R` put
`F_eps=F_0+eps\,(z_+\phi_++z_-\phi_-)\in\mathcal Q_{T_*}`.  By (2.1), using
`L_{T_*}F_0=0`,

\[
 \mathcal W(F_\varepsilon)
 =\underbrace{\langle L_{T_*}F_0,F_0\rangle}_{=0}
  +2\varepsilon\,|z|^2
  +\varepsilon^2 B_{T_*}(z,z).                              \tag{3.1}
\]

The linear term is nonzero, so `\mathcal W(F_\varepsilon)<0` for small
`\varepsilon<0`, while `\mathcal W(F_{|\varepsilon|})>0` for small
`\varepsilon>0`; `\mathcal W` is indefinite.  This is case 2.  Conversely, if
1 holds then the range obstruction of (2.4) vanishes on the radical, and
Proposition 2.1 gives `\mathcal W\ge0` as soon as `\Sigma(T_*)\ge0`.  The two
cases are mutually exclusive because (3.1) with `z=0` gives no negative
direction of this form.  QED

**Corollary 3.2 (constraint-free form of Gate R).**

\[
\boxed{
 T_{\mathcal W}=T_q
 \quad\Longrightarrow\quad
 \text{Gate R holds at the first contact.}}
\]

Equivalently: if the unconstrained Weil form survives exactly as far as the
primitive one, the Tate collar of every first-contact radical vanishes.

**Corollary 3.3 (quantitative form).**  For `T<T_q` one has `L_T>0`, so
`\Sigma(T)=B_T-X_T^{*}L_T^{-1}X_T` is an honest `2\times2` real symmetric
matrix, continuous in `T`.  Gate R at `T_*` holds if and only if
`\liminf_{T\uparrow T_*}\lambda_{\min}\Sigma(T)>-\infty`.  In particular the
single scalar inequality

\[
\boxed{
 \Sigma(T)\ \ge\ 0\qquad\text{for every }T<T_q}            \tag{3.2}
\]

implies Gate R, and (3.2) refers only to the explicitly known data
`\rho_{\pm,T}` (P124.005 (2.2)--(3.3)), the Gram matrix (2.3) and the
resolvent of the strictly positive operator `L_T`.

**[phase 134 — note of record, from Paper 47 Finding 4.8 and
`R134_002` (M5).  It does not alter Corollary 3.3, and it corrects a
round-1 claim of Paper 47 that did.]**

1. *The criterion is invariant.*  `\liminf_{T\uparrow T_*}\lambda_{\min}\Sigma(T)
   > -\infty` at a **finite** `T_*` is unchanged by a change of basis of the
   border: a rebasing acts by `\Sigma \mapsto C(T)^{\mathsf T}\Sigma C(T)` with
   `C` continuous and nonsingular, and on a compact neighbourhood of a finite
   `T_*` the quantities `\|C\|` and `\|C^{-1}\|` are bounded, so boundedness
   below of `\lambda_{\min}` transfers.  Paper 47 round 1 claimed this
   criterion is "basis-dependent as stated"; **that claim is withdrawn**.
2. *The number is not invariant, and must not be quoted across bases or
   papers.*  In the named border basis `(\phi_+,\phi_-)` and in the
   Gram-orthonormalized basis used by `p124_lab.blocks`, the same form at the
   same `T` and the same resolution gives `\lambda_{\min}\Sigma = 2.35\cdot
   10^{-2}` and `2.77\cdot10^{-3}` at `T = 1.67`.  Both are correct; neither
   is a property of `\Sigma`.  The congruence relating them has condition
   number growing like `e^{T}` (`\|\phi_\sigma\|_{L^2}\sim e^{T/2}`).
3. *What to carry.*  The boxed target (3.2), `\Sigma(T)\ge 0`, and the inertia
   of `\Sigma(T)`, are congruence invariants (Sylvester).  Carry those.  Quote
   `\lambda_{\min}\Sigma(T)` only with its border normalization named.
4. *And a scope remark on all `\Sigma` numerics here.*  `\Sigma_T(z)
   = \inf\{\mathcal W(F+\phi_z) : F\in\mathcal P_T\}` is an **infimum**, so a
   piecewise-constant Galerkin computation of it is a variational **upper
   bound**.  See the `[phase 134]` note in P124.014 §3 and the phase README.

This is the exact gain of the reformulation.  Every earlier attack on Gate R
had to control `\rho_{+,T}` against a vector `F_*` that is not known in closed
form.  Statement (3.2) has no `F_*` in it: it is a bordered-positivity
inequality for a one-parameter family of explicit objects, on the range of
windows where the operator is strictly positive.

## 4. What the dichotomy does not prove

Theorem 3.1 is not a proof of Gate R, and Corollary 3.2 is not a cheap route
to it.  `T_{\mathcal W}=T_q` is itself equivalent to a genuine arithmetic
statement, and it is **false** for the shifted-pair falsifier: see
[P124.014](P124_014_FALSIFIER_GATE_SEPARATION.md), where the first contact of
the primitive form of `Xi_a(s)=xi(s+a)xi(s-a)` is located and the collar
`J_\sigma(F_*)` is found to be nonzero.  That computation instantiates case 2
of Theorem 3.1 in an actual model with zeros off the critical line.

Three consequences for the programme, all negative or restrictive:

1. **Gate R is not a structural theorem of the "functional equation plus
   rank-two Tate compression" class.**  The falsifier has both, and fails it.
   Any proof of Gate R must use an input that separates `zeta` from `Xi_a`
   before the spectral comparison, exactly as required by
   `P3_COMMON_FAILURE_ARCHITECTURE` section 8.  The visible difference is that
   the local weights of `Xi_a` are `p^{-1/2\pm a}`, i.e. its local roots are
   not unimodular.
2. **Gate R and Gate S are not independent obligations of different types.**
   Theorem 3.1 shows Gate R already carries the full unconstrained positivity
   at the contact window.  The two-gate factorization of P122.020 remains
   valid as a *sufficient* route, but the present note removes the hope that R
   could be discharged by soft analysis and S left as the only arithmetic
   step.
3. The reformulation supersedes nothing.  P124.005 (the collar kernel),
   P124.011 (the Schur reduction) and P124.012 (the storage surplus) are
   unchanged; (2.2) explains why P124.011's crossblock had to be exactly
   `\rho_{+,T}`, and Corollary 3.3 replaces its free budget `d` by the
   computed `B_T`.

## 5. Ledger

| statement | status |
|---|---|
| dictionary (1.1)--(1.4), `\mathcal P_T=\{\Phi(0)=\Phi(1)=0\}` | `PROVED-IN-REPOSITORY` |
| Lemma 1.1 exact truncation, Lemma 1.2 nesting, `T_{\mathcal W}\le T_q` | `PROVED-IN-REPOSITORY` |
| block identification (2.1)--(2.3); crossblock `=` Tate collar | `PROVED-IN-REPOSITORY` |
| Proposition 2.1 (Schur/Douglas) | `IMPORTED` (closed-form Schur complement), hypotheses checked |
| Theorem 3.1 dichotomy, Corollaries 3.2--3.3 | `PROVED-IN-REPOSITORY` |
| `\Sigma(T)\ge0` for all `T<T_q` (constraint-free Gate R) | `OPEN` -- the new target |
| Gate R itself; Gate S; row (d) | `OPEN`, unchanged |
| Gate R as a model-independent theorem | `REFUTED` by P124.014 |
| Corollary 3.3's `liminf` criterion | `PROVED`, and **invariant** at finite `T_*`; the *value* `lambda_min Sigma(T)` is **not** a congruence invariant — `[phase 134]` note above |

The [verification script](scripts/p124_013_schur_verify.py) checks two things
that are not proofs of the above but guard against transcription error: the
generalized assembly of `scripts/p124_lab.py` reproduces the audited
phase-118 `rowd_assembly` matrices for `zeta` exactly, and the finite
dimensional statements behind Proposition 2.1 and Theorem 3.1, including the
explicit negative witness (3.1), hold on random blocks.
