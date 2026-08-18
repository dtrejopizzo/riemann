# 115.14 — Point 4: the mechanism is proved, the sign is NOT resolved

> **Read §6bis before §3–§5.**  The favourable-sign claim of §3–§5 is withdrawn
> there; the two derivations conflict and the splitting has an obstruction.
> Propositions 1 and 3 stand.

`115_13` derived the mechanism of the semilocal Sonin trace but left the sign
open, and with the sign as written there the route was useless.  **The sign is
now resolved, by two independent routes, and it is the favourable one.**  This
note also identifies exactly why `115_13` Proposition 1 is incomplete, and what
single statement remains.

Scripts: `scripts/115_14_p4_sign_resolution.py` (+`.out`),
`scripts/115_13_p4_phase_derivative_identity.py` (+`.out`).

## 1. The calibration `115_13` got wrong

`115_13` wrote \(\varphi=-\arg E\).  The archimedean case fixes the convention.
With \(E_\infty(s)=L_\infty(\tfrac12+is)=\pi^{-\frac14-\frac{is}2}\Gamma(\tfrac14+\tfrac{is}2)\),

\[
 \arg E_\infty(s)=-\tfrac s2\log\pi+\arg\Gamma(\tfrac14+\tfrac{is}2)=\theta(s),
\]

the Riemann–Siegel theta function, and \(\theta'(s)\sim\tfrac12\log\tfrac{s}{2\pi}>0\)
for large \(s\).  A de Branges phase must be **increasing**, so
\(\varphi=+\arg E\).

Verified: \(\theta'(s)\) against \(\tfrac12\log\tfrac{s}{2\pi}\) agrees to 4–5
digits at \(s=14,30,100\).

## 2. The archimedean phase is the archimedean multiplier

> **Proposition 1.**  \(\varphi_\infty'(s)=\theta'(s)=-\tfrac12m_\infty(s)\),
> with \(m_\infty\) the multiplier of `eq:archmultiplier`.
>
> *Proof.*  \(\tfrac{d}{ds}\Im\log\Gamma(\tfrac14+\tfrac{is}2)
> =\Im\bigl[\tfrac i2\psi(\tfrac14+\tfrac{is}2)\bigr]
> =\tfrac12\Re\psi(\tfrac14+\tfrac{is}2)\), so
> \(\theta'(s)=\tfrac12\Re\psi(\tfrac14+\tfrac{is}2)-\tfrac12\log\pi
> =-\tfrac12m_\infty(s)\). \(\square\)

> **Corollary 2.**  For positive-definite \(f\),
> \(\frac1\pi\int\widehat f\,\varphi_\infty'\,ds=-G_\infty(f,f)=W_\infty^{CC}(f)\).

A striking cross-check falls out.  \(\theta'\) changes sign exactly where
\(m_\infty\) does, at

\[
 \tau^{*}=6.28983598884\ldots
\]

the constant already isolated in `main.tex` after `eq:archenergy` (there noted
as \(\approx2\pi=6.28318\ldots\), and indeed distinct from it in the third
digit).  Numerically \(\theta'(2)=-0.5808\), \(\theta'(6)=-0.0236\),
\(\theta'(14)=+0.4005\).

## 3. The finite places enter with a minus

> **Proposition 3.**
> \[
>  \frac{d}{ds}\arg\!\!\prod_{p\in S\setminus\{\infty\}}\!\!L_p(\tfrac12+is)
>  \;=\;-\sum_{n\ S\text{-smooth}}\frac{\Lambda(n)}{\sqrt n}\cos(s\log n).
> \]

*Proof.*  \(L_p(\tfrac12+is)^{-1}=1-p^{-\frac12-is}\) and
\(\arg(1-p^{-\frac12-is})=\sum_{k\ge1}\frac{p^{-k/2}}{k}\sin(ks\log p)\); the
\(1/k\) cancels against the \(k\) on differentiating, and
\(\arg L_p=-\arg(1-p^{-\frac12-is})\). \(\square\)

**Verified** at \(P\in\{3,7,19,53\}\), \(s\in\{0.4,1.7,5.0,13.9\}\): agreement
\(10^{-11}\)–\(10^{-9}\), residue being the finite-difference step.

**Independent confirmation.**  This is the Riemann–von Mangoldt density:
\(N(T)=\tfrac1\pi\theta(T)+1+S(T)\) with \(S(T)=\tfrac1\pi\arg\zeta(\tfrac12+iT)\)
and \(\zeta=\prod_pL_p\); the oscillating prime terms enter the zero density
with a minus.  Two independent derivations, same sign.

> **Corollary 4.**  \(\displaystyle\frac1\pi\int\widehat f\,\varphi_S'\,ds
> =-G_\infty(f)-K_S(f)=-B^S_{\rm nuc}(f).\)

**The phase of \(E_S\) delivers exactly the Weil functional, with the sign row (d)
needs.**  `115_13` §4's obstruction is removed.

## 4. Why `115_13` Proposition 1 is nevertheless incomplete

Corollary 4 at \(S=\{\infty\}\) would give
\(\mathrm{Tr}(\vartheta(f)\mathbf S)=-G_\infty(f)=W_\infty^{CC}(f)\), i.e.
\(E=0\) — contradicting CC's Theorem 3, where \(E\ne0\).  So the identification
of the structure function used there is wrong, and §2 shows exactly how:

**\(E_\infty\) cannot be a structure function at all**, because \(\varphi_\infty'=-\tfrac12m_\infty<0\)
for \(s<\tau^{*}\), while a de Branges phase is increasing.  The true structure
function is Burnol's \(\lambda\)-dependent \(\mathscr E_\lambda\), which satisfies
\(|\mathscr E_\lambda(\tfrac12+is)|=|E_\infty(s)|\) but has a **different,
increasing phase** \(\varphi_\lambda\).

> **The discrepancy \(\varphi_\lambda-\theta\) is precisely what produces CC's
> correction \(\epsilon\), i.e. their \(E\).**

That is a satisfying identification rather than a defect: it says CC's \(E\) is
the \(\lambda\)-dependent (Sonin-cutoff) part of the phase, and nothing else.

## 5. What remains, stated exactly

By `propbb` of CCM, \(\mathcal B_\lambda\) is **the same space for every \(S\)**;
only the norm changes, and it changes by exactly
\(\prod_{p\in S}|1-p^{-\frac12-is}|^{2}\) (`115_12` Proposition 1).  The
\(\lambda\)-dependent correction is therefore **\(S\)-independent**.

> **Remaining statement (the splitting).**  The phase of the structure function
> of \(\mathcal B^S_\lambda\) splits as
> \[
>  \varphi^S_\lambda=\varphi_\lambda+\arg\!\!\prod_{p\in S\setminus\{\infty\}}\!\!L_p(\tfrac12+is),
> \]
> i.e. the \(\lambda\)-correction and the Euler phase do not interact.

Granting the splitting, Propositions 1–3 give

\[
 \boxed{\;\mathrm{Tr}\,\bigl(\vartheta(f)\mathbf S_S\bigr)
  =-B^S_{\rm nuc}(f)+E(f),\qquad E\ \text{the archimedean correction, }S\text{-independent}.\;}
\]

which is **exactly hypothesis (H) of `115_09`**, with \(E_S=E\) not growing with
\(S\).  Hence, since \(\mathcal S_S\ge0\) by construction,

\[
 -B^S_{\rm nuc}(g,g)=\mathcal S_S(g)-E(g\star g^\vee)\ \ge\ -E(g\star g^\vee),
\]

and **row (d) on \(S\) follows from \(E\le0\) on positive-definite functions.**

## 6. What this buys, measured against the no-go

`115_08` Corollary 7 proved no single-place construction closes row (d): every
archimedean lower bound costs a slack equal to what is missing.  The present
reduction escapes it, because \(\mathcal S_S\) is built from a cutoff on
\(\mathbb A_S\) and carries arithmetic.

The gain is not that the difficulty vanished but that it changed type:

| before | after |
|---|---|
| archimedean reservoir must **dominate** the arithmetic \(K\) | \(K_S\) is **absorbed exactly** into the phase |
| blocked by Corollary 7 for any single-place \(\mathcal A\) | remaining statement \(E\le0\) is purely archimedean with **nothing arithmetic to dominate** |

And \(E\le0\) is not virgin territory: CC §5 prove \(E\circ Q=-2\epsilon'(1^{+})(\mathrm{Id}-K)\)
with \(K\) compact Hilbert–Schmidt, so \(E\le0\) holds on every compact interval
**up to finite codimension**, with \(\epsilon'(1^{+})\approx22.9965\).  The
outstanding work is uniform control of those finitely many directions as the
interval grows — which is what their §6 does by Toeplitz analysis on
\([2^{-1/2},2^{1/2}]\).

## 6bis. CORRECTION — the sign is NOT resolved, and §5's splitting has an obstruction

The claim in §3–§5 that the sign is favourable is **withdrawn**.  Carrying out
the computation named in §8 reverses it, and the two derivations conflict.

\(1-p^{-\frac12-is}\), as a function of \(s\), is analytic and zero-free in the
**lower** half-plane (there \(|p^{-\frac12-is}|=p^{-\frac12+\tau}<1\)) and has its
zeros on \(\Im s=\tfrac12\), i.e. in \(\mathbb C^{+}\).  So
\(\log(1-p^{-\frac12-is})\) is the boundary value of a function analytic in
\(\mathbb C^{-}\), where the conjugate relation carries the opposite sign to
\(\mathbb C^{+}\).  Hence

\[
 \mathcal H^{+}\bigl[\log|L_p|\bigr]=+\arg\bigl(1-p^{-\frac12-is}\bigr)=-\arg L_p .
\]

> **Proposition 5.**  The outer function in \(\mathbb C^{+}\) with modulus
> \(|L_p|\) has phase \(-\arg L_p\), not \(+\arg L_p\); on the line it is
> \(\overline{L_p}\).  With that phase the finite term re-enters as \(+K_S\),
> the adverse sign of `115_13`.

So the sign has now been derived twice, with opposite answers:

| factorisation | phase | sign of \(K_S\) |
|---|---|---|
| \(\varphi_S=\arg E_S\), \(E_S=\prod_vL_v\) (CCM's notation) | \(\arg\prod L_p\) | \(-K_S\), favourable |
| outer function of modulus \(|E_S|\) (HB-admissible) | \(-\arg\prod L_p\) | \(+K_S\), adverse |

The two are complex conjugates on the line.  **The modulus does not determine
the structure function**: two Hermite–Biehler functions with the same modulus
differ by an inner factor and generate different spaces, and CCM fix only
\(|\mathscr E^S|=|E_S|\).

Worse, **neither candidate is admissible**.  A structure function must be
*entire* with zeros confined to \(\mathbb C^{-}\).  \(\prod_pL_p\) has poles in
\(\mathbb C^{+}\); and \(\mathscr E_\lambda/\prod_p(1-p^{-\frac12+is})\), which
would carry the right modulus, has poles as well.  Therefore
\(\mathcal B^S_\lambda\) has **no** structure function of the form
(archimedean)\(\times\)(Euler factor), and the splitting posited in §5 is not
merely unverified — there is a concrete obstruction against it.

What survives §6bis untouched: Proposition 1
(\(\varphi_\infty'=-\tfrac12m_\infty\)) and Proposition 3 (the phase derivative
of the Euler factor is \(\mp\) the von Mangoldt sum, closed form, verified to
\(10^{-9}\)).  The mechanism is real; which of the two signs the space realises
is not settled.

## 7. Status

* \(\varphi=+\arg E\) calibration: **PROVED** (\(\theta'>0\) asymptotically) and
  verified.
* Proposition 1, \(\varphi_\infty'=-\tfrac12m_\infty\): **PROVED**; sign change at
  \(\tau^{*}=6.28983598884\), the constant of `eq:archenergy`.
* Proposition 3, Euler phase derivative \(=-\)von Mangoldt: **PROVED** in closed
  form, **verified** to \(10^{-9}\), and independently confirmed by
  Riemann–von Mangoldt.
* Corollary 4, \(\frac1\pi\int\widehat f\varphi_S'=-B^S_{\rm nuc}\): **holds only for the
  first factorisation of §6bis**; the sign is not determined.
* `115_13` §4's adverse sign: **re-derived in §6bis** from the outer function;
  it conflicts with §3.  Neither sign is established.
* `115_13` Proposition 1 as stated: **INCOMPLETE**; \(E_\infty\) is not a
  structure function (\(\varphi_\infty'<0\) below \(\tau^{*}\)), and the
  \(\lambda\)-dependent part is exactly CC's \(E\) (§4).
* The splitting of §5: **obstructed** — \(\mathcal B^S_\lambda\) has no structure
  function of the form (archimedean)×(Euler factor); see §6bis.
* (H) with \(E_S=E\): **NOT established**.
* Row (d) on \(S\) \(\Longleftarrow\) \(E\le0\): holds **given (H)**, which is not
  established.
* \(E\le0\) without support restriction: **OPEN** — this is CC's own §5/§6, known
  up to finite codimension on every compact interval.
* Row (d): **OPEN**.

## 8. Next

The splitting of §5, which is a statement about Hermite–Biehler factorisation:
does the outer factor of modulus \(\prod_p|1-p^{-\frac12-is}|^{-1}\) contribute
its own argument additively to the phase, with no interaction with the
\(\lambda\)-cutoff?  Note \(1-p^{-\frac12-is}\) is zero-free in the **lower**
half-plane and has zeros on \(\Im s=\tfrac12\), so neither \(\prod L_p\) nor
\(\prod(1-p^{-\frac12-is})\) is itself Hermite–Biehler; the admissible factor is
the outer function with that modulus, whose phase is the conjugate function of
\(\log\prod|1-p^{-\frac12-is}|\).  Checking that this conjugate function is
\(\arg\prod L_p\) is the concrete remaining computation.
