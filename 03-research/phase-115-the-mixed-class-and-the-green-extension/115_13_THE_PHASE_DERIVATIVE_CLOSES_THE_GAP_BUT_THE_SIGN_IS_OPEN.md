# 115.13 — The semilocal Sonin trace: the mechanism is found, and the sign decides everything

Point 4 of the attack order.  The gap measured in `115_12` — multiplicative
Möbius weight on the Sonin side versus additive von Mangoldt weight on the Weil
side, a logarithmic derivative apart — **closes by mechanism**: the trace of a
projection onto a de Branges space produces the derivative of the phase
function, and the derivative of the phase of an Euler factor *is* the von
Mangoldt sum.

The mechanism is derived and numerically verified.  The **sign** is not
established, and with the sign as derived the identity works against row (d)
rather than for it.  That is stated plainly in §4; it is the live question.

Script: `scripts/115_13_p4_phase_derivative_identity.py` (+`.out`).

## 1. The trace on the spectral side

On the spectral side the scaling action becomes multiplication:
\(\vartheta(f)\mapsto M_{\widehat f}\) with
\(\widehat f(s)=\int f(\rho)\rho^{-is}d^*\rho\), because
\(\mathcal U_S=\mathcal F_\mu\circ w_S\) is unitary and carries \(\vartheta(\rho)\)
to multiplication by \(\rho^{-is}\).

By `propbb` of CCM, \(\upsilon_S\) identifies
\(\mathfrak{Son}_\lambda(X_S,\alpha)\) with \(\mathcal B_\lambda\) inside
\(L^2\bigl(\mathbb R,\,ds/|E_S(s)|^2\bigr)\).  So \(\mathbf S_S\) becomes the
orthogonal projection \(P_S\) onto \(\mathcal B_\lambda\), a reproducing-kernel
space with kernel \(K_S\).  For such a projection,

\[
 \mathrm{Tr}\,\bigl(M_{\widehat f}P_S\bigr)
 =\int_{\mathbb R}\widehat f(s)\,K_S(s,s)\,\frac{ds}{|E_S(s)|^2},
\]

and for a de Branges space with structure function of phase \(\varphi_S\) the
diagonal kernel is \(K_S(s,s)=\varphi_S'(s)\,|E_S(s)|^2/\pi\).  **The weight
cancels:**

> **Proposition 1 (formal).**
> \[
>  \boxed{\;\mathrm{Tr}\,\bigl(\vartheta(f)\,\mathbf S_S\bigr)
>   =\frac1\pi\int_{\mathbb R}\widehat f(s)\,\varphi_S'(s)\,ds. \;}
> \]

Everything about \(S\) is now in one scalar function, \(\varphi_S'\).

## 2. The phase derivative of the Euler factor

With \(E_S(s)=\prod_{v\in S}L_v(\tfrac12+is)\) (CCM \eqref{ess}) and
\(L_p(\tfrac12+is)^{-1}=1-p^{-\frac12-is}\), write
\(u=p^{-\frac12-is}\).  From \(\log(1-u)=-\sum_{k\ge1}u^k/k\),

\[
 \arg\bigl(1-p^{-\frac12-is}\bigr)
 =\sum_{k\ge1}\frac{p^{-k/2}}{k}\,\sin(ks\log p),
\]

so \(\varphi_S=\varphi_\infty+\sum_{p\in S}\arg(1-p^{-\frac12-is})\) and,
differentiating, **the \(1/k\) cancels against the \(k\)**:

> **Proposition 2.**
> \[
>  \varphi_S'(s)-\varphi_\infty'(s)
>  =\sum_{p\in S}\sum_{k\ge1}\log p\;p^{-k/2}\cos(ks\log p)
>  =\sum_{\substack{n\ \ S\text{-smooth}}}\frac{\Lambda(n)}{\sqrt n}\cos(s\log n).
> \]

**Verified numerically.**  LHS by complex arithmetic and central differences
(no series), RHS as an explicit von Mangoldt sum, at \(P\in\{3,7,19,53\}\) and
\(s\in\{0.4,1.7,5.0,13.9\}\): agreement \(10^{-11}\)–\(10^{-9}\) across all 16
combinations, the residue being the finite-difference step, not the identity.

Combining with Fourier inversion \(\int\widehat f(s)\cos(s\log n)\,ds=\pi\bigl(f(n)+f(n^{-1})\bigr)\):

> **Corollary 3.**
> \[
>  \mathrm{Tr}\,\bigl(\vartheta(f)\mathbf S_S\bigr)
>  =\mathrm{Tr}\,\bigl(\vartheta(f)\mathbf S\bigr)
>  +\sum_{n\ S\text{-smooth}}\frac{\Lambda(n)}{\sqrt n}\bigl(f(n)+f(n^{-1})\bigr),
> \]
> the second term being exactly \(W_{\rm fin,S}\) of `eq:Ktest` in the
> \(\Delta^{1/2}\)-normalised form.

**This answers `115_12` Proposition 2.**  The conversion from the multiplicative
Euler weight to the additive von Mangoldt sum is performed by differentiating
the phase; no separate trace formula is needed.

## 3. What (H) becomes

With CC's Theorem 3, \(\mathrm{Tr}(\vartheta(f)\mathbf S)=W_\infty^{CC}(f)+E(f)=-G_\infty(f)+E(f)\),

\[
 \mathrm{Tr}\,\bigl(\vartheta(f)\mathbf S_S\bigr)
 =-G_\infty(f)+E(f)+K_S(f),
\]

so **(H) holds with \(E_S=E\) unchanged** — the correction term does not grow
with \(S\).  That is a strong and clean statement, and it is what `115_09`
hypothesis (H) asked for, except for one thing.

## 4. The sign, and why it is fatal as derived

`115_09` Proposition 1 needed
\(\mathcal S_S=-B^S_{\rm nuc}+E_S=-(K_S+G_\infty)+E_S\), i.e. \(K_S\) entering
with a **minus**.  §3 delivers a **plus**.  With the plus,

\[
 -B^S_{\rm nuc}=-K_S-G_\infty=\mathcal S_S-E-2K_S,
\]

so positivity of \(\mathcal S_S\) buys nothing: the finite term appears twice
and the conclusion is weaker than the starting point, not stronger.  The
semilocal route as set up in `115_09` **does not close row (d) with this sign**.

Where the sign is decided: Proposition 1 assumes \(\mathcal B^S_\lambda\) has a
structure function whose phase is \(\varphi_S=-\arg E_S\), i.e. that
\(\mathscr E^S_\lambda=\mathscr E^\infty_\lambda\prod_{p\in S}L_p\).  That is
**not established**, and there is a concrete obstruction to it: \(E_S=\prod_vL_v\)
has **poles** at the zeros of \(1-p^{-\frac12-is}\), so it is not a
Hermite–Biehler function and cannot itself be a structure function.  CCM state
only that \(\mathcal B^S_\lambda\) is de Branges *with the norm induced by the
embedding*; Burnol computed the structure function \(\mathscr E_\lambda\) only
for \(S=\{\infty\}\).

So the correct structure function for \(S\ne\{\infty\}\) is unknown, and its
phase may differ from \(-\arg E_S\) by exactly the sign at issue.

## 5. Candid status

* Proposition 1 (trace \(=\frac1\pi\int\widehat f\varphi_S'\)): **derived
  formally**.  Not rigorous: the trace is not trace-class without the
  regularisation CC use, and the de Branges diagonal-kernel formula presumes
  the structure function of §4.
* Proposition 2 (phase derivative \(=\) von Mangoldt): **PROVED** in closed
  form and **verified numerically** to \(10^{-9}\).  This part is independent of
  the structure-function question and stands on its own.
* Corollary 3 and (H) with \(E_S=E\): **conditional** on Proposition 1.
* The sign: **OPEN**, and decisive.  As derived it makes the semilocal route
  useless for row (d); the opposite sign would close `115_09` Proposition 1 and
  reduce row (d) to \(E\le0\), which is CC's own §5 statement.
* Row (d): **OPEN**.

## 6. Next

One question, and it is sharp: **what is the structure function of
\(\mathcal B^S_\lambda\)?**  Burnol has it for \(S=\{\infty\}\).  Since
\(\prod_vL_v\) has poles, the structure function is not that product, and
identifying it fixes \(\varphi_S\) and hence the sign in §4.  Everything else in
this note is settled.
