# 108.27 — Weight zero is forced, and the reason is that Div is linear

## 0. Answer to the open question of 108_26 §4.1

> **Does $\mathcal G$ admit a principal witness of weight strictly inside
> $0<s<1$?**
>
> **No.**  Weight $s=0$ is forced.

But the proof localises the obstruction somewhere unexpected and actionable:
not in the family $\mathcal G$, and not in the analysis, but in the fact that
$\mathrm{Div}$ as defined in 107_237 is **linear** in $f$ rather than
**logarithmic**.  §4 states what would unforce it.

No zero of $\xi$ is used anywhere.

## 1. The three inputs

**(a) $\mathrm{Div}$ is linear.**  107_237 (2.3) defines the potential
by $u_f''(r)=f(r)/r$, so $u_{cf}''=c\,u_f''$ and

\[
 \mathrm{Div}(cU)=c\mathrm{Div}(U).
 \tag{1.1}
\]

Verified to $2\times10^{-7}$ relative error over three weights and three
constants.

**(b) $\mathrm{Div}$ forgives *additive* affine shifts.**  107_237
Theorem 2.1: $U_f$ is unique modulo affine functions, and affine functions
have vanishing second derivative.  Verified in two pieces to avoid
catastrophic cancellation: the second difference of an affine function is
$0$ (worst case $4.4\times10^{-10}$, including coefficients of size $10^3$),
and the second-difference operator is linear.

**(c) The Frobenius action is *multiplicative* on potentials.**  108_02
Theorem 4.1: $f_s(r/n)=\chi(n)f_s(r)$ with $\chi(n)=n^{s}$ a character.
Verified exactly (error $0$).

## 2. The theorem

> ### Theorem 2.1
> Let $U$ be a nonzero element of $\mathcal G$ of weight $s$.  Then
> $\mathrm{Div}(U)$ is invariant under the Frobenius action if and only
> if $s=0$.

**Proof.**  By (c) the action sends $f_s$ to $\chi(n)f_s$, hence by (a)
sends $\mathrm{Div}(U)$ to $\chi(n)\mathrm{Div}(U)$.  Invariance
therefore requires $\chi(n)\mathrm{Div}(U)=\mathrm{Div}(U)$ for
every $n\in\mathbb N^\times$, i.e. either $\mathrm{Div}(U)=0$ — which
forces $f_s\equiv0$ by 107_237 Theorem 2.1, excluded — or $\chi(n)=1$ for
every $n$.  Since $\chi(n)=n^{s}$, that holds for all $n$ iff $s=0$. $\square$

Verified: $\chi(n)=n^{s}$ is trivial for all $n\in\{2,3,5,7,11,101\}$ exactly
when $s=0$, tested at $s=0,10^{-3},0.1,0.5,0.9,1$.

> ### Corollary 2.2
> $\mathrm{Prin}(\mathcal G)$ of 108_03 Definition 6.1 is the **only**
> principal subspace available in $\mathcal G$.  By 108_26 it lies on the
> excluded boundary, at an accumulation point of the singular set.
> **Stage 1 is terminally obstructed on this route.**

## 3. Where the obstruction actually sits

The proof turns on a mismatch that is worth isolating:

> $\mathrm{Div}$ forgives **addition** of a constant but not
> **multiplication** by one, while the Frobenius action acts by
> **multiplication**.

Verified directly: for $s=\tfrac12$ at $r=2$, replacing $U$ by $U+3.1r+0.7$
leaves $\mathrm{Div}$ unchanged; replacing $U$ by $2U$ does not.

This is a departure from classical divisor theory, where $\mathrm{div}$
is **logarithmic**, $\mathrm{div}(c\varphi)=\mathrm{div}(\varphi)$
for every nonzero constant $c$, which is precisely why principal divisors
form a group and $\mathrm{Pic}=\mathrm{Div}/\mathrm{Prin}$
is well behaved.

Verified: a logarithmic model $D_{\log}(U):=(\log U)''$ satisfies
$D_{\log}(cU)=D_{\log}(U)$ for $c=2,5,0.3$.

> **So the obstruction is not the graded family, and not the analysis.  It is
> that 107_237's $\mathrm{Div}$ is linear where the classical one is
> logarithmic.**

## 4. What would unforce it

Under a logarithmic divisor, $\chi(n)$ would drop out of Theorem 2.1's proof
and **every** weight $s$ would be principal — in particular weights strictly
inside $0<s<1$, where 108_24's pairing already exists.  Stage 1 would then
close with no further analytic work.

This is a concrete and bounded question about the foundations of the DC
construction:

> **Open question.**  Is there a logarithmic divisor operator on the DC
> potentials, compatible with 107_237's defining relation and with 107_238's
> vanishing interior density?

It is **not** answered here, and it is not obvious: $U_f$ takes both signs
(it is a difference of convex functions, 107_237 §2), so $\log U_f$ is not
globally defined, and the model $D_{\log}$ used in §3 is a check of the
principle, not a construction.

## 5. Scope

Proved here:

* Theorem 2.1: invariance of $\mathrm{Div}$ forces $s=0$;
* Corollary 2.2: no principal witness exists inside the open strip, so
  Stage 1 is terminally obstructed on the present route;
* §3: the obstruction is the linearity of $\mathrm{Div}$, isolated by
  the additive/multiplicative mismatch.

Verified numerically: linearity (1.1); affine-insensitivity in two pieces;
exactness of the character relation; triviality of $\chi$ exactly at $s=0$;
the additive/multiplicative asymmetry; invariance of a logarithmic model.

Read from source, not re-derived: 107_237 (2.3) and Theorem 2.1; 108_02
Theorem 4.1; 108_03 Definition 6.1; 108_24 Theorem 2.1; 108_26.

Not established, and explicitly not claimed:

* that a logarithmic divisor operator exists on DC potentials (§4) — the
  §3 model is a principle check, not a construction, and $U_f$ changes sign;
* any repair of Stage 1 along the present route, which Corollary 2.2 closes;
* anything about complex $s$.

`ROW_A_STATUS` remains `partial`.  Nothing here bears on RH.

## 6. Verifier

`108_27_weight_zero_forced_by_linear_div.py` checks: linearity of
$\mathrm{Div}$; vanishing of the second difference of affine functions
and linearity of that operator, composing to affine-insensitivity; exactness
of $f_s(r/n)=\chi(n)f_s(r)$; that $\chi$ is trivial on six primes exactly
when $s=0$; the additive-yes / multiplicative-no asymmetry at $s=\tfrac12$;
and invariance of the logarithmic model under three constant multiples.
