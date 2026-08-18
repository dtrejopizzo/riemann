# 115.16 — Point 4 settled: the sign is favourable, the trace identity does not exist, and (H) is asymptotic rather than exact

Two results in opposite directions.  The sign question that blocked `115_14` is
**resolved favourably**, by three independent arguments.  But the trace identity
used to reach it is **not available at all**, and the correct intrinsic form
shows that (H) cannot be an exact identity at fixed \(\lambda\).

## 1. Correction to `115_14` §6bis — I mixed half-planes

`115_14` §6bis re-derived the adverse sign from the outer function and concluded
the two derivations conflict.  **That correction was itself wrong.**

CCM's half-plane is \(L^{+}=\{\Re w>\tfrac12\}\), which corresponds to the
**lower** \(s\)-half-plane.  There the increasing phase is
\(\Phi(s)=+\arg E(\tfrac12+is)\) — check on \(E(w)=e^{a(w-1/2)}\), \(a>0\),
Hermite–Biehler for \(L^{+}\), with \(\Phi(s)=as\) increasing — and in that same
half-plane the conjugate relation is

\[
 \arg F=-\mathcal H[\log|F|],\qquad\text{not }+\mathcal H .
\]

Verify on \(F=1-re^{-isL}\) (outer in \(\Im s<0\)):
\(\log|F|=-\sum_m\frac{r^m}{m}\cos(msL)\),
\(\arg F=+\sum_m\frac{r^m}{m}\sin(msL)\), so with \(\mathcal H[\cos]=\sin\) one
has \(\arg F=-\mathcal H[\log|F|]\).  The flip coming from the zero-free
half-plane is exactly cancelled by the flip in the phase convention.
**Routes (a) and (b) agree; there was never a conflict.**

## 2. The sign, fixed without any convention bookkeeping

> **Proposition 1 (parity argument).**  Both candidate contributions are **even**
> in \(s\): \(\theta'\) is even (\(\theta\) odd) and \(\cos(s\log n)\) is even.
> Reversing the orientation of the \(s\)-axis — which is the whole difference
> between the two conventions — therefore leaves the density unchanged.  The
> **relative** sign between archimedean and finite parts is convention
> independent, and the overall sign is pinned by positivity at large \(s\), where
> \(\theta'(s)\sim\tfrac12\log\tfrac{s}{2\pi}>0\).  Hence
> \[
>  \pi\rho(s)\ \simeq\ \theta'(s)\ -\!\!\sum_{n\ S\text{-smooth},\,n>1}\!\!\frac{\Lambda(n)}{\sqrt n}\cos(s\log n).
> \]

**MINUS** — the Riemann–von Mangoldt / Weil sign, i.e. option (a) of `115_14` §3.

**Independent confirmation, intrinsic.**  Since \(\upsilon_S=\beta_S\circ\mathcal U_S\)
with \(\beta_S\) multiplication by \(E_S\), and \(\mathcal B_\lambda\) is the same
set for every \(S\),
\(\mathcal V_S:=M_{E_S}^{-1}\mathcal B_\lambda=M_g\mathcal V_\infty\) inside
\(L^2(\mathbb R,ds)\), with \(g(\tfrac12+is)=\prod_{p\in S}(1-p^{-\frac12-is})\).
Multiplying a subspace by \(g\) reweights the diagonal of the orthogonal
projection by \(|g|^2\); where \(|g(s)|^2=1+p^{-1}-2p^{-1/2}\cos(s\log p)\) is
**minimal**, i.e. \(\cos(s\log p)=+1\), the density **decreases**.  That is the
\(-\cos\) sign.

So `115_14` §3–§5's favourable sign stands, and §6bis is **withdrawn**.

## 3. But the trace identity does not exist

> **Proposition 2.**  **No entire function has modulus \(|E_S(s)|\) on the
> critical line, for any \(S\ni\infty\), including \(S=\{\infty\}\).**
>
> *Proof.*  Suppose \(\mathscr E\) entire with
> \(|\mathscr E(\tfrac12+is)|=|E_S(s)|\).  Put
> \(g(w)=\prod_{p\in S,\,p<\infty}(1-p^{-w})\) (entire; \(g\equiv1\) if
> \(S=\{\infty\}\)) and
> \[
>  H(w):=\mathscr E(w)\,g(w)\,\pi^{w/2}/\Gamma(w/2).
> \]
> \(H\) is entire because \(1/\Gamma\) is entire, and \(|H|=1\) on
> \(L=\{\Re w=\tfrac12\}\) because
> \(E_S(w)=\pi^{-w/2}\Gamma(w/2)\,g(w)^{-1}\).  Then \(H^{\#}(w)=\overline{H(1-\bar w)}\)
> is entire and equals \(\overline H\) on \(L\), so \(HH^{\#}\equiv1\) and \(H\)
> has no zeros.  But \(H(0)=0\), since \(1/\Gamma(w/2)\) vanishes at
> \(w=0,-2,-4,\dots\) and neither \(\mathscr E\) nor \(g\) has a pole.
> Contradiction. \(\square\)

**Consequence.**  The step used throughout `115_13`–`115_14` — "\(|E_S|^2\)
cancels against \(K(s,s)=\varphi'|E|^2/\pi\)" — is **not available**.  The genuine
phase satisfies \(\varphi_S'=\pi K_S(s,s)/|\mathscr E^S_\lambda(\tfrac12+is)|^2\)
with a *different* denominator.  What is exactly true is the intrinsic form

\[
 \mathrm{Tr}\,\bigl(P_SM_{\widehat f}P_S\bigr)=\int_{\mathbb R}\widehat f(s)\,K_S(s,s)\,d\mu_S(s),
 \qquad d\mu_S=\frac{ds}{|E_S(s)|^2},
 \qquad \rho_S:=\frac{K_S(s,s)}{|E_S(s)|^2}\ \ge 0 .
\]

**Provenance note, and an error of mine.**  `115_14` quoted CCM's
\(|\mathscr E_\lambda(\tfrac12+is)|=|E_\infty(s)|\).  That sentence sits inside an
`\iffalse … \fi` block (lines 1074–1098 of `mainc2m24fine.tex`) — **suppressed**
— and is absent from the published version (Ann. Funct. Anal. 2024, §4.8.3),
which stops at "…is a de Branges space".  CCM withdrew it, correctly, since
Proposition 2 refutes it.  Burnol never claims it; his Théorème 1 (burnol-2)
says the *uncompleted* Mellin transform of a Sonine distribution is entire with
trivial zeros at \(w=-2n\), which is exactly what cancels the poles of
\(\Gamma(w/2)\).  I read the commented block as live text.

## 4. Why de Branges theory does not supply \(\mathscr E^S\)

* **Non-uniqueness (de Branges, *Hilbert Spaces of Entire Functions*, Thm 23).**
  Writing \(E=A-iB\), the complete list of structure functions giving the **same
  space with the same norm** is \(E_k=kA-ik^{-1}B\), \(k\in\mathbb R^*\), and
  \(|E_k|^2=k^2A^2+k^{-2}B^2\neq|E|^2\).  So identity of norms never forces
  identity of \(|E|\) — the premise of `115_14` §6bis ("same modulus, differ by
  an inner factor") points the wrong way.
* **The multiplication theorem** (\(M_g:B(E)\to B(gE)\) isometric when \(gE\) is
  Hermite–Biehler) **fails here**: \(g(w)=\prod_p(1-p^{-w})\) is not HB for
  \(\Re w>\tfrac12\).  With \(x=p^{-\sigma}\), \(y=p^{\sigma-1}\),
  \(\tau=t\log p\),
  \(|g(w)|^2-|g(w^{\#})|^2=(y-x)(2\cos\tau-(x+y))\), which changes sign for
  \(\sigma>\tfrac12\).
* CCM establish only that \(\mathcal B^S_\lambda\) satisfies the de Branges
  axioms, hence *some* \(\mathscr E^S_\lambda\) exists.  **The semilocal
  structure function has not been computed by anyone**, and no theorem in
  de Branges, Dym–McKean, Remling or Havin–Jericho determines it from
  \(\mathscr E^\infty\) and the weight.

Burnol's archimedean structure function does exist explicitly (burnol-2,
Théorème 8): with \(\psi^\lambda_\pm\) the entire even solutions of
\(\psi^\lambda_\pm(x)\pm\mathcal F(\psi^\lambda_\pm|_{(-\lambda,\lambda)})(x)=2\cos(2\pi\lambda x)\),
\[
 E_\lambda(w)=\pi^{-w/2}\Gamma(w/2)\Bigl[\lambda^{\frac12-w}
 +\tfrac{\sqrt\lambda}2\int_\lambda^\infty\bigl(\psi^\lambda_+(t)-\psi^\lambda_-(t)\bigr)t^{-w}dt\Bigr].
\]
No phase function is given, in this or any other Burnol paper; the only route to
it is the Dirac system of math/0302102, whose potential is a Fredholm
determinant of the Dirichlet kernel — no closed form.

## 5. (H) is asymptotic, not exact

Positivity \(\rho_S\ge0\) **rules out both signs as exact statements**:

* with \(-\): at \(s=0\) the additive correction is
  \(-\tfrac1\pi\sum_{p\in S}\frac{\log p}{\sqrt p-1}\to-\infty\) as \(S\) grows,
  while \(\rho_\infty\) is fixed;
* with \(+\): since
  \(\sum_m\Lambda(p^m)p^{-m/2}\cos(ms\log p)=(\log p)(\Re L_p(\tfrac12+is)-1)\ge-\frac{\log p}{\sqrt p+1}\),
  and the \(\log p\) are \(\mathbb Q\)-independent, Kronecker lets one put
  \(s\log p\approx\pi\pmod{2\pi}\) simultaneously for all \(p\in S\), giving
  \(-\tfrac1\pi\sum_{p\in S}\frac{\log p}{\sqrt p+1}\to-\infty\).

> **The exact \(S\)-deformation is multiplicative, not additive:**
> \(\mathcal V_S=M_g\mathcal V_\infty\), and in a rank-one model
> \(\rho_S=\rho_\infty\,|g|^2/\langle|g|^2\rangle\ge0\).  The additive
> \(-\sum_n\frac{\Lambda(n)}{\sqrt n}\cos(s\log n)\) is the **leading term in the
> high-density limit** — the regime of Connes' semilocal trace formula, with
> error \(o(1)\) as the cutoff \(\Lambda\to\infty\).

So hypothesis (H) of `115_09`, in the form
\(\mathrm{Tr}(\vartheta(f)\mathbf S_S)=-B^S_{\rm nuc}(f)+E(f)\), is **not an
exact identity at fixed \(\lambda\)**.  Whatever it delivers, it delivers
asymptotically, with \(\lambda\)-dependent corrections restoring positivity —
the same phenomenon already seen for \(\mathscr E_\infty\) in `115_14` §4.

## 6. Status

* `115_14` §6bis (adverse sign from the outer function): **WITHDRAWN**;
  half-planes were mixed (§1).
* The sign: **RESOLVED, favourable (minus)** — three independent arguments
  (parity, corrected conjugate relation, projection-diagonal reweighting).
* Proposition 2, no entire function of modulus \(|E_S|\): **PROVED**.  The trace
  identity of `115_13`–`115_14` is **not available**.
* CCM's \(|\mathscr E_\lambda|=|E_\infty|\): **false**, and **suppressed** by them
  in the arXiv source and the published version; quoted in error in `115_14`.
* The semilocal structure function: **not computed by anyone**; de Branges
  theory supplies no theorem determining it.
* (H) as an exact identity: **REFUTED** (§5).  (H) as an asymptotic statement in
  the high-density limit: **plausible, unproved**.
* Row (d): **OPEN**.
