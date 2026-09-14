# P121 -- backward/forward design of second-order Euler contact

## Status

This note does not claim row (d), the global Weil square, or a new positivity
theorem.  It reconstructs the remaining problem simultaneously backward from
the desired conclusion and forward from the source objects already built.

The new exact object is the **critical conormal class** of the compact source.
Its norm is the faithful critical square constructed in phase 121.  The only
unproved assertion is an equality-state-only second-order contact law.  By
the proved first-contact reduction and exact nesting, that assertion is
**equivalent in force to the global square**; it is not an intermediate
lemma whose formulation constitutes progress toward the sign.  Requiring
the corresponding Euler ideal to be invariant on every source is forbidden:
that is the phase-91 flat-descent defect in new notation.

## 1. Backward reconstruction

Fix a window `T`, let `F in P_T`, and write

\[
 K_F(z)=\int_{-T}^{T}F(t)e^{-zt}\,dt,
 \qquad E(z)=\xi(1/2+z),
 \qquad H_F(z)=E(z)K_F(z).                          \tag{1.1}
\]

Let `Sigma_simp` be the set of simple critical zeros `z_gamma=i gamma` of
`E`.  The desired contradiction chain is

```text
global Weil sign
 <- no nonzero first-contact state
 <- K_F(i gamma)=0 for every gamma in Sigma_simp
 <- H_F has second-order contact with (E=0) at every z_gamma
 <- the critical conormal class of H_F vanishes
 <- an equality-state source law kills that class.
```

The last arrow is new mathematics still to be proved.  Once the already
proved first-contact and nesting theorems are included, proving that arrow
is precisely proving the global square.

## 2. Exact local conormal algebra

Fix `lambda in Sigma_simp`.  Let `O_lambda` be the local ring of holomorphic
germs and `I_lambda=(E)`.  Since the zero is simple, `E'(lambda)` is a unit
in the residue field and multiplication by `E` gives an isomorphism

\[
 O_\lambda/I_\lambda\longrightarrow I_\lambda/I_\lambda^2,
 \qquad [a]\longmapsto[aE].                        \tag{2.1}
\]

### Proposition 2.1 -- second-order contact dictionary

For `H_F=EK_F`, the following statements are equivalent:

\[
\begin{aligned}
 &(a)\quad K_F(\lambda)=0,\\
 &(b)\quad H_F\in I_\lambda^2,\\
 &(c)\quad H_F'(\lambda)=0,\\
 &(d)\quad [H_F]=0\quad\hbox{in }I_\lambda/I_\lambda^2.
\end{aligned}                                      \tag{2.2}
\]

Moreover, under (2.1),

\[
 [H_F]=K_F(\lambda)[E],
 \qquad
 {H_F'(\lambda)\over E'(\lambda)}=K_F(\lambda).  \tag{2.3}
\]

#### Proof

The first formula in (2.3) follows from `H_F=EK_F`.  Differentiation gives
`H_F'=E'K_F+EK_F'`, and evaluation at `lambda` gives the second formula.
Since `E'(lambda)` is nonzero, (a) and (c) are equivalent.  Isomorphism
(2.1) gives the equivalence with (b) and (d).  QED.

Thus the missing condition is not global division by zeta.  It is the
vanishing of one first-order normal coefficient at each reduced critical
point.

## 3. The conormal norm is exactly the antisymmetric defect

Define the reduced conormal sampling map

\[
 \nu_T(F)
 :=\left({H_F'(i\gamma)\over E'(i\gamma)}\right)_
       {i\gamma\in\Sigma_{\rm simp}}
 =\bigl(K_F(i\gamma)\bigr)_
       {i\gamma\in\Sigma_{\rm simp}}.              \tag{3.1}
\]

On a compact ordinate window `J`, give this finite vector the norm

\[
 \|\nu_{T,J}(F)\|_{\rm cn}^2
 :=8\pi\sum_{\substack{i\gamma\in\Sigma_{\rm simp}\\\gamma\in J}}
 |K_F(i\gamma)|^2.                                 \tag{3.2}
\]

The negative-half residue theorem proves, without using row (d),

\[
 \|\nu_{T,J}(F)\|_{\rm cn}^2
 =\lim_{\sigma\downarrow0}{
  \|\chi_J(\mathscr A_+-\mathscr A_-)
       (\sigma+i\,\cdot)\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}.                             \tag{3.3}
\]

Exhausting the line gives

\[
 \|\nu_T(F)\|_{\rm cn}^2
 :=\sup_J\|\nu_{T,J}(F)\|_{\rm cn}^2
 =\mathfrak D_T^{\rm crit}(F)\in[0,+\infty].       \tag{3.4}
\]

### Proposition 3.1 -- faithfulness

\[
 \nu_T(F)=0\quad\Longleftrightarrow\quad F=0.       \tag{3.5}
\]

#### Proof

The simple critical set has superlinear counting function, while a nonzero
Cartwright function of fixed exponential type has only linearly many zeros.
Thus `nu_T(F)=0` forces `K_F=0`; Laplace injectivity gives `F=0`.  QED.

Equations (2.3) and (3.3) are the backward identification: the positive
critical defect is the norm of the first infinitesimal failure of `H_F` to
meet the Euler divisor twice.

## 4. Forward reconstruction from first contact

At a first contact one knows

\[
 F\in\mathcal P_T,
 \qquad P_T\mathscr A_TF=0,                         \tag{4.1}
\]

or `mathscr A_TF` is a two-Tate forcing.  Rows (a)--(c) and phase 121 already
supply:

1. the completed Euler determinant `E`;
2. its logarithmic contact character;
3. the compact-source section `H_F=EK_F`;
4. the two unsupertraced causal currents;
5. a well-defined graph-renormalized symmetric boundary;
6. the conormal observation `nu_T(F)` in (3.1).

The source equation determines only the sum of the two causal currents.
Their conormal coefficients are opposite.  Therefore ordinary Real symmetry
or scalar conservation kills their sum and leaves `nu_T(F)` untouched.

## 5. The equality-state second-order contact theorem

The terminal theorem can now be stated without a norm estimate or an
operator factorization.

### ESOC -- equality-state second-order Euler contact

For every compact-window primitive first-contact state,

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 H_F\in I_{i\gamma}^2
 \quad(i\gamma\in\Sigma_{\rm simp}).               \tag{5.1}
\]

Equivalently,

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \nu_T(F)=0.                                       \tag{5.2}
\]

By Proposition 3.1, ESOC immediately excludes first contact.  Exact nesting
then gives the global finite-window sign and the already proved cofinal
theorem gives row (d).

ESOC is strictly equality-state-only.  The statement that `(E)` is preserved
by the degree derivation on every source is not ESOC and is rejected by the
phase-91 Euler-derivation defect.

## 6. Decomposition of the genuinely new arrow

To prove ESOC forward, one must construct three pieces in this order.

### F1. Unsupertraced first-jet lift

Work first over the dual-number algebra
`D=C[epsilon]/(epsilon^2)` and freeze the compact source while displacing
only the completed Euler determinant.  Define

\[
 \mathbf J_T^\pm(F;z)
 :=E(z\pm\epsilon)K_F(z)
 =E(z)K_F(z)\pm\epsilon E'(z)K_F(z).                \tag{6.1}
\]

This construction takes place before the two orientations are added.
For the local factor of `zeta`, namely the dual of the inverse-Euler
determinant line constructed by the local conormal intersection,

\[
 z_p(s)=(1-p^{-s})^{-1},
\]

one has

\[
 z_p(s\pm\epsilon)
 =z_p(s)\left(1\mp\epsilon
 { (\log p)p^{-s}\over1-p^{-s}}\right).            \tag{6.2}
\]

The Leibniz rule on the product gives `zeta'/zeta`; changing the orientation
gives the physical `-zeta'/zeta` contact.  The completed Gamma determinant
supplies its archimedean derivative.  Thus (6.1) is source-defined from the
same local determinant data as rows (a)--(c), after the already constructed
determinant-line dualization, and no critical-zero location is used.

### Theorem 6.1 -- frozen-source dual Euler jet

The pair (6.1) defines an unsupertraced first-jet lift

\[
 \mathbf j_T(F)=(j_+(F),j_-(F))                    \tag{6.3}
\]

whose reduced conormal symbols at every simple critical zero are

\[
 \operatorname{Nor}(j_+(F))=-\nu_T(F),
 \qquad
 \operatorname{Nor}(j_-(F))=+\nu_T(F),             \tag{6.4}
\]

after choosing the signs to agree with the two causal residue orientations.
Their scalar sum has zero normal symbol and their difference has symbol
`-2 nu_T(F)`.

#### Proof

Equations (6.1)--(6.2) construct the jet over `D`.  At a simple zero
`lambda`, reduction modulo `(E)` kills the order-zero term and leaves
`+/- E'(lambda)K_F(lambda)`.  Division by the nonzero conormal generator
`E'(lambda)` gives `+/- K_F(lambda)`.  Reversing the label on the positive
causal port gives the convention in (6.4), identical to the residues of the
two currents.  Addition and subtraction prove the last assertion.  QED.

Thus F1 is closed.  The construction realizes the normal symbols of the
physical ports; it does not identify their complete Hardy boundary values.

### F2. Equality-locus causal matching

Construct a source relation `M_T` defined only on solutions of (4.1), not on
the whole test space, such that

\[
 M_T\mathbf j_T(F)=0
 \quad\Longrightarrow\quad
 j_+(F)=j_-(F)                                      \tag{6.5}
\]

in the reduced conormal quotient.  Together with the already proved scalar
law `j_++j_-=0`, equation (6.5) gives both jets zero.

The load-bearing requirement is that `M_T` be computed from the Euler source
and the two Tate constraints before evaluating `A_T(F,F)`.  It may depend on
the particular solution `F`, but it may not use `A_T^{-1}`, a square root,
critical-zero locations, or a fitted Green parameter.

### F3. Descent and faithfulness

Apply `Nor` to (6.5), use (6.4), and obtain `nu_T(F)=0`.  Proposition 3.1
then gives `F=0`.  This piece is closed.

Hence F2 is the unique construction problem.  F1 and F3 are proved.  F2 is
not a weaker gate: on the first-contact branch it is the global sign theorem
itself, expressed before supertrace.

## 7. Backward specification of the matching law

The matching law cannot be another equality of scalar boundary values.  It
must distinguish the two copies before supertrace and then identify them on
the equality locus.  Its minimal algebraic type is a relation

\[
 M_T:\ker(P_T\mathscr A_T)\longrightarrow
 \operatorname{Eq}(\mathcal J_{T,+},\mathcal J_{T,-}), \tag{7.1}
\]

where `Eq` is the equalizer of the two conormal projections.  The map must
factor through the rank-one local Euler incidence, because the rank-two
shifted pair must not possess (7.1).

This gives four nonnegotiable tests:

1. **Equality-locus only:** extending `M_T` to every source must not be
   needed.
2. **Before supertrace:** after adding the two orientations, their normal
   data cancel and cannot be recovered.
3. **Rank-one consumption:** at a prime, the matching uses the single local
   Frobenius conormal line; a doubled local factor has two unmatched lines.
4. **No derivative-flatness assumption:** `M_T` cannot assert that the full
   Euler principal ideal is stable under the degree derivation.

## 8. Corpus collision audit

The words `conormal` and `I/I^2` occur in phases 107 and 114 for local prime
self-intersections, Kunneth diagonal trace domains and Haran contacts.  Those
objects recover `1-p^{-s}`, `Lambda(p^j)` or a positive transverse trace
norm.  They do not contain `H_F=EK_F`, the critical divisor of `E`, or the
second-order contact condition (2.2).

The nearest genuine collision is phase 91: global stability of the Euler
ideal under the degree derivation leaves the exact derivation defect and is
not available.  ESOC avoids claiming that global stability, but it is not
proved merely by restricting the old false statement to a kernel.  F2 must
be an independently constructed equality-locus matching law.

### 8.1 Why the tempting cubic separator is not promoted

There is a correct algebraic observation.  In a complex line, if

\[
 x+y=0,
 \qquad x^{\otimes3}=y^{\otimes3},                  \tag{8.1}
\]

then `x=y=0`: substitution gives `2x^(tensor 3)=0`, and a nonzero vector has
nonzero tensor cube.  Thus a cubic matching of the two jets would prove F2.

The corpus contains faithful cubic and odd-moment operations on the row-(a)
bio targets.  Those constructions provide the operation `x -> x^3`; they do
not provide the equality of the two expressions in (8.1) for a first-contact
state.  After `j_-=-j_+` is known, that equality is itself equivalent to
`j_+=0`.  It is therefore a possible *type* for `M_T`, not an independent
source law, and is not recorded as progress toward ESOC.

## 9. Honest closure state

```text
critical conormal coefficient             PROVED
coefficient = antisymmetric residue        PROVED
critical conormal norm                     PROVED
faithfulness of the norm                   PROVED
source realization of the two jets         PROVED (F1)
equality-locus causal matching              OPEN (F2 = global-square core)
descent from matching to F=0                PROVED (F3)
global Weil square                          OPEN
```

This is not a new name for a sequence of future inequalities.  It is a
backward/forward specification of one source relation, with its domain,
codomain, normal symbol and forbidden circular realizations fixed in
advance.
