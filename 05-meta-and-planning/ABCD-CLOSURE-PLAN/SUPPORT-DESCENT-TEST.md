# Support-descent test at first contact

**State:** the proposed implication does not constitute a weaker
intermediate lemma. In the presence of a first contact, it is equivalent to the vanishing
one wants to prove. The interference analogy does produce a useful lemma,
but it acts by enlarging the window, not by shrinking it.

## 1. The positive weights

For the ordinary von Mangoldt function,

\[
\Lambda(n)\ge0,
\qquad
d_{m,N}=\sum_{2\le n\le N}\Lambda(n)n^{-(2m+1)}>0.
\]

Hence

\[
\langle R_LF,D_{N,L}R_LF\rangle
=\sum_{m\le L}d_{m,N}|(R_LF)_m|^2\ge0,
\]

which vanishes exactly when `R_LF=0`. This gives no sign to the
cross terms of translation, collar, Gamma, and Tate.

## 2. No-descent theorem

Let `T_*` be a primitive first contact:

\[
H_{T_*}\ge0,
\qquad F\in\ker H_{T_*}.
\]

Then for every `T'<T_*` and every `G\in\mathcal P_{T'}`,

\[
\mathfrak a_{T'}(G,G)=\mathfrak a_{T_*}(EG,EG)\ge0,
\tag{1}
\]

where `E` is extension by zero. The equality is the extension
compatibility from Paper 47, `lem:monoT`; the inequality uses `H_{T_*}\ge0`.

Consequently, at a first contact the statement

\[
R_LF\ne0\Longrightarrow
\exists T'<T_*,\ G\in\mathcal P_{T'}:
\mathfrak a_{T'}(G,G)<0
\tag{2}
\]

cannot have a true consequent. Proving (2) is, in that
context, equivalent to proving that `R_LF\ne0` never occurs. It is not a reduction to
a weaker problem.

### Global equivalence

Choose, at each first contact, an `L<\infty` for which `R_L` is injective
on `\ker H_{T_*}`; Paper 47 proves that such an `L` exists. Then the following are
equivalent:

1. the primitive form is nonnegative for every window;
2. no counterexample to (2) exists;
3. (2) holds for every first-contact vector.

Indeed, if the form becomes negative, continuity and monotonicity produce
a first contact and an `F\ne0` in its radical. Injectivity gives
`R_LF\ne0`, while (1) blocks the consequent of (2): `F` is exactly
a counterexample. Conversely, if there is no global negativity, there is no
first contact and (2) holds vacuously. By the global equivalence of the
primitive form, these conditions are also equivalent to D/RH.

So constructing the requested arithmetic counterexample would prove D
false; excluding it would prove D. The test does settle the logic of the proposal,
but it does not lower the difficulty.

The phenomenon already appears in the scalar model

\[
q_T(x)=(T_*-T)|x|^2.
\]

There is positivity for `T<T_*`, an observed null vector at `T_*`, and
negativity for `T>T_*`; there is no negativity to the left. This model
does not falsify the arithmetic form: it shows that minimality and observation alone
are not enough.

## 3. Interference inside the window

For every `h` in the primitive domain at `T_*`, Cauchy–Schwarz for the
nonnegative form gives

\[
\mathfrak a_{T_*}(F,h)=0.
\]

Hence

\[
\mathfrak a_{T_*}(F+h,F+h)=\mathfrak a_{T_*}(h,h)\ge0.
\tag{3}
\]

In the language of interference, `F` is a dark state with respect to all
interior primitive variations. Trimming, dilating inward, or correcting
the two Tate moments does not create a negative linear term. This agrees with
R162_101, Proposition 3.

## 4. Where interference does act: the outer collar

Consider an abstract enlargement of the window and the block form

\[
\mathcal H=\mathcal H_{\rm int}\oplus\mathcal H_{\rm col},
\qquad
\widetilde H=
\begin{pmatrix}H&K^*\\ K&C\end{pmatrix}.
\]

**Coupling lemma.** If `H\ge0`, `HF=0`, and `KF\ne0`, then
`\widetilde H` has a negative direction, provided a collar vector
`y` with `\operatorname{Re}\langle KF,y\rangle\ne0` belongs to the domain of
the form.

Indeed,

\[
\widetilde q(F+ty)
=2t\operatorname{Re}\langle KF,y\rangle+t^2q_C(y).
\]

The sign of `t` is chosen so the linear term is negative, and then
`|t|` is taken small enough. This is the elementary mechanism of
interference or level repulsion.

In D's form, `KF` is the full outer residual

\[
\xi_F^\delta
=\mathcal MF-(B+B^*)F-r
\quad\hbox{on the new collar}.
\]

R162_405 proves the exact identity

\[
\lambda_\delta\langle F_\delta,F\rangle
=\langle\xi_F^\delta,F_\delta\rangle_{\rm collar}.
\]

The Gamma part of `\xi_F^\delta` is faithful, but it can interfere with the
Euler translations and with Tate. The nonvanishing of the residual produces
negativity to the right, something already part of the definition of first
contact; it produces no contradiction.

## 5. Reduced arithmetic target

Proving that the outer residual is nonzero does not close D: by the
coupling lemma it only proves again that the form acquires a negative
direction when the window is enlarged. That is already compatible with the first contact.

The interference question that does match the gate is interior:

> Can there exist a nonzero primitive dark state `F` for which Gamma,
> the ordinary-prime shifts, and Tate satisfy exactly
> the kernel's weak equation across the whole window?

The minimal statement that would close the gate is:

\[
\left.
\begin{array}{c}
H_T\ge0,\quad H_TF=0,\quad F\in\mathcal P_T,\\
\text{`T` is the first contact for the }\Lambda\text{ form}
\end{array}
\right\}
\Longrightarrow
K_F(2m+\tfrac12)=0\quad(m\ge1).
\tag{4}
\]

By the faithfulness of the Gamma moments, (4) implies `F=0`. In the language of
Paper 47, it would suffice to prove that the corrected product
`\zeta(s)W^0_\varepsilon(s)` is holomorphic at the positive odd integers:
its residue there is

\[
\zeta(2m+1)K_F(2m+\tfrac12).
\tag{5}
\]

The kernel equation only holds inside the window. Continuing it
outward brings in precisely the Euler collar, the Gamma tail, and Tate; that is why
the holomorphy of (5) does not follow from an automatic analytic continuation.
The new step would have to use `\Lambda*1=\log` to cancel those terms
without canceling or hiding their residues.

**Conclusion:** the attempt to obtain a negative function of smaller support
is ruled out by (1). The interference analogy leaves a simpler formulation
of the real obstacle: proving that the ordinary arithmetic system
admits no interior dark state at the first contact. That statement is still
the gate, not a proof of it.
