# 108.28 — Div is already logarithmic; 108_27 §4's proposed fix was misconceived

## 0. Answer to the open question of 108_27 §4

> **Open question (108_27 §4).** Is there a logarithmic divisor operator on
> the DC potentials, compatible with 107_237's defining relation?

> **Yes, trivially: it is $\mathrm{Div}$ itself.** $\mathrm{Div}$
> already has both hallmarks of a classical logarithmic divisor operator —
> it forgets units and it obeys the power rule — once "logarithmic" is read
> correctly, in the additive (tropical) language 107_237 already works in.
> No new operator exists to be found, and 108_27 §4's proposed diagnostic
> ($D_{\log}(U):=(\log U)''$) could not have supplied one even in principle:
> it is shown below to be blind to the weight $s$ entirely.

This corrects 108_27 §4, not its Theorem 2.1: that theorem (weight $s=0$
forced by literal Frobenius-invariance) is untouched and remains correct.
What changes is the diagnosis of *why* — and, consequently, where the
search for a fix should go next (108_29, 108_31: the definition of
"principal", not the operator $\mathrm{Div}$).

No zero of $\xi$ is used anywhere.

## 1. The additive/multiplicative dictionary 107_237 already commits to

107_237 defines $U_f$ as a solution of $u_f''(r)=f(r)/r$ (its (2.3)), unique
modulo affine functions (its Theorem 2.1, cited here, not re-derived). This
is an **additive** construction: it is built by solving a *linear* ODE in
$f$. Classical divisor theory, by contrast, is stated **multiplicatively**:
for a rational function $\varphi$ on a variety $X$,

\[
 \mathrm{div}(\varphi\psi)=\mathrm{div}(\varphi)+\mathrm{div}(\psi),
 \qquad
 \mathrm{div}(\varphi^{c})=c\,\mathrm{div}(\varphi)\ (c\in\mathbb Z),
 \qquad
 \mathrm{div}(u\varphi)=\mathrm{div}(\varphi)\ \text{for a unit }u .
 \tag{1.1}
\]

Passing from a multiplicative theory to an additive one is exactly what a
logarithm does: $\log(\varphi\psi)=\log\varphi+\log\psi$,
$\log(\varphi^c)=c\log\varphi$, $\log(u\varphi)=\log u+\log\varphi$ (a
*constant* additive shift, since $u$ is a unit, i.e. locally constant in
the relevant sense). **107_237's potentials $U_f$ are already the additive
(logarithmic) objects** — this is the entire point of building them from a
linear ODE rather than from a product formula. The question is only whether
$\mathrm{Div}$, read in *this* additive language, reproduces (1.1)
correctly. It does, term by term.

## 2. Div reproduces all three classical laws, correctly translated

### Proposition 2.1 (the sum law: $\mathrm{Div}$ is additive over sums of potentials)

For test data $f,g$ with potentials $U_f,U_g$ (107_237 Theorem 2.1),

\[
 \mathrm{Div}(U_f+U_g)=\mathrm{Div}(U_f)+\mathrm{Div}(U_g).
 \tag{2.1}
\]

**Proof.** $(u_f+u_g)''=u_f''+u_g''=f(r)/r+g(r)/r=(f+g)(r)/r$, so $U_f+U_g$
solves the defining ODE for $f+g$; by uniqueness mod affine (107_237
Theorem 2.1), $U_f+U_g$ *is* a potential of $f+g$, hence
$\mathrm{Div}(U_f+U_g)=(f+g)(r)\,d^*r=\mathrm{Div}(U_f)+\mathrm{Div}(U_g)$
by Definition 5.1 of 108_03. $\square$

This is the exact translation, into the additive picture, of the first law
of (1.1): $\mathrm{div}(\varphi\psi)=\mathrm{div}(\varphi)+\mathrm{div}(\psi)$
becomes "$\mathrm{Div}$ of a **sum** of potentials is the sum of the
$\mathrm{Div}$s" precisely because sums of potentials play the role
products of functions play classically.

### Proposition 2.2 (the power law: $\mathrm{Div}(cU)=c\mathrm{Div}(U)$ is correct, not a defect)

This is 108_27 fact (a), cited, not re-derived: $u_{cf}''=c\,u_f''$, so
$\mathrm{Div}(cU)=c\mathrm{Div}(U)$ for every real $c$.

Under the dictionary of §1, $cU$ (scalar multiple of a potential) is the
additive avatar of $\varphi^c$ (raising the underlying multiplicative
object to the $c$-th power): $\log(\varphi^c)=c\log\varphi$. The classical
law $\mathrm{div}(\varphi^c)=c\mathrm{div}(\varphi)$ is a
**standard, unremarkable, expected scaling law** — divisors of powers scale
by the power. $\mathrm{Div}(cU)=c\mathrm{Div}(U)$ is exactly
this law, correctly transplanted. It is not the departure from "logarithmic"
behaviour that 108_27 §3 suggested; it is a confirmation of it.

### Proposition 2.3 (the unit law: $\mathrm{Div}$ already forgets units — via *affine* shift, not scalar multiplication)

107_237 Theorem 2.1, cited: $U_f$ is unique modulo **affine** functions of
$(x,y)$, and $\mathrm{Div}(U+\text{affine})=\mathrm{Div}(U)$
(this is 108_27 fact (b), re-verified in the verifier below at two further
weights for completeness).

Under the dictionary of §1, multiplying $\varphi$ by a nonvanishing
constant unit $u$ corresponds, additively, to *adding* the constant
$\log u$ — **not** to scalar-multiplying $\log\varphi$. The classical law
$\mathrm{div}(u\varphi)=\mathrm{div}(\varphi)$ therefore
translates to "$\mathrm{Div}$ is insensitive to *additive* (affine)
shifts of the potential" — which is exactly what 107_237 Theorem 2.1
already supplies. This is the correct, and already-present, "divisor
forgets units" clause; it was never missing.

### Corollary 2.4 (the three laws (1.1) are all already present, correctly matched)

$\mathrm{Div}$ satisfies the additive avatar of each of the three
classical laws (1.1): the sum law (Prop. 2.1), the power law (Prop. 2.2),
and the unit law (Prop. 2.3, via affine shift rather than scalar
multiplication). There is no fourth classical law it is missing.

**In particular:** $\mathrm{Div}(cU)=\mathrm{Div}(U)$ for
scalar $c\ne1$ — the property 108_27 §4 asked a "fix" to supply — is
**not** one of the classical laws (1.1) at all. It would assert
$\mathrm{div}(\varphi^c)=\mathrm{div}(\varphi)$, which is false
classically for $c\ne1$ (e.g. $\mathrm{div}(x^2)=2\mathrm{div}(x)\ne\mathrm{div}(x)$
on $\mathbb A^1$, for $\mathrm{div}(x)\ne0$). Seeking an operator with
that property was seeking something with **no classical counterpart**;
108_27 Theorem 2.1's conclusion (only $s=0$ is literally
Frobenius-invariant) is exactly what a correctly-behaved logarithmic
operator should produce once the Frobenius action is recognised as acting
by *raising to a (real) power* $n^s$ rather than by *multiplying by a unit*.

## 3. Why the §3 diagnostic $D_{\log}$ could never have worked, independent of the sign issue

108_27 §3 exhibited $D_{\log}(U):=(\log U)''$ as a model with
$D_{\log}(cU)=D_{\log}(U)$, and flagged (§4, candidly) that $U_f$ changes
sign so $\log U_f$ is not globally defined. That objection is sufficient by
itself, but there is a second, independent reason $D_{\log}$ was never a
candidate fix, visible even where $\log U$ *is* defined:

### Proposition 3.1

Wherever $U>0$, $D_{\log}(cU)=D_{\log}(U)$ for every $c>0$, **for every
$U$**, regardless of which weight $s$ (if any) $U$ belongs to, and
regardless of the character $\chi_s(m,n)$ entirely.

**Proof.** $\log(cU)=\log c+\log U$ with $\log c$ constant in $r$, so
$(\log(cU))''=(\log U)''$ identically — this uses only that $\log c$ does
not depend on $r$, never the value of $s$. $\square$

**Consequence.** $D_{\log}$ cannot distinguish weights at all: it is
invariant under *every* positive rescaling of *every* potential,
independent of $s$. Even setting aside that $\log U_f$ is ill-defined on
sign changes, $D_{\log}$ could not have been sharpened into a tool that
picks out a favourable set of weights (e.g. all of them, or $(0,1)$) as
"principal" in any sense responsive to the Frobenius character
$\chi_s(m,n)=n^{1+s}m^{-s}$ — it is blind to $\chi_s$ by construction. The
§3 model was a check of a general principle (constants drop out under
$\log$), not a step toward a working construction, for a reason beyond the
one 108_27 itself already gave.

## 4. What this settles, and what it leaves open

$\mathrm{Div}$ is not defective and needs no replacement: it already
implements a logarithmic (valuation-type) divisor operator, correctly, in
the additive language 107_237 is built in. 108_27 Theorem 2.1 stands as a
*correct* instance of the power law (Prop. 2.2), not as a symptom to be
cured.

This closes 108_27 §4's open question in the negative-for-the-search,
positive-for-the-diagnosis sense: no new operator is needed or wanted. It
throws the entire weight of unforcing $s=0$ onto the definition of
"principal" itself (108_03 Definition 6.1) — precisely the object 108_29
and 108_31 examine next. Nothing here decides whether that definition
should be revised; it only establishes that $\mathrm{Div}$ is not
the place to look.

## 5. Scope

Proved here:

* Proposition 2.1: $\mathrm{Div}$ is additive over sums of potentials
  of different test data (new; not stated in 108_03/108_27);
* Proposition 3.1: $D_{\log}$'s constant-invariance is independent of $s$
  and of $\chi_s$, a second, independent reason it cannot serve as a
  weight-sensitive fix.

Read from source, not re-derived: 107_237 (2.3) and Theorem 2.1 (unique mod
affine); 108_27 facts (a)-(c) and Theorem 2.1; 108_03 Definition 5.1.

Not established, and explicitly not claimed:

* any revision to the definition of "principal" (108_03 Definition 6.1) —
  that is 108_29/108_31's task, not this note's;
* anything about complex $s$;
* any relation to $\xi$, RH, or `ROW_A_STATUS`.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 6. Verifier

`108_28_div_is_already_logarithmic.py` checks: Proposition 2.1 (additivity
of $\mathrm{Div}$ across two different weights, by finite
differences, avoiding cancellation by testing the ODE residual directly);
Proposition 2.2 is cited from 108_27 and re-confirmed at one further weight
pair; Proposition 2.3 (affine-insensitivity) re-confirmed at two further
weights beyond 108_27's; Proposition 3.1 ($D_{\log}$'s $s$-independence,
verified across six weights and three positive constants, showing the
diagnostic's invariance value never depends on $s$).
