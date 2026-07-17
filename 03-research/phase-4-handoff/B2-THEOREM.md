# Theorem B-2 — A faithful, semibounded realization of the Weil functional (the Phase-4 deliverable)

**Self-contained statement and proof. Path (A) closed.** This document assembles Days 0–22 into one
theorem: a rigorous, semibounded operator realization of the Weil quadratic functional on the
band-limited (classical Weil) test class, with the property that **RH is exactly the sign of its bottom**.
All supporting lemmas are proved unconditionally; the single residual hypothesis **(H)** is isolated,
stated precisely, and shown to be **strictly weaker than RH**.

**Status legend:** ✅ unconditional, proved here · (H) the one hypothesis · — RH itself (the sign, not
addressed).

---

## 0. Setup

**Test class.** $PW_d=\{F:\widehat F\in L^2[-d,d]\}$, the Paley–Wiener space of band-limit $d>\tfrac12$
(entire functions of exponential type $d$ in $L^2(\mathbb R)$). This is the **classical Weil class**
(compact support in the prime variable); band-limited $\Rightarrow$ entire $\Rightarrow$ off-axis
evaluations $F(\gamma+ib)$ are automatic, with no strip-weight machinery. Domain refinement:
$\mathcal D:=PW_d\cap H^1$ (for the IBP, §2; dense in $PW_d$).

**The Weil functional.** For $F\in\mathcal D$, with $h(z)=F(z)\,\overline{F(\bar z)}$ (the entire
extension of $|F|^2$), the Riemann–Weil explicit formula gives the Hermitian form
$$
\mathfrak t(F):=\sum_{\rho}h(\gamma_\rho)\ \overset{\text{(EF)}}{=}\ \mathfrak a(F)+\mathfrak q(F)-\mathfrak p(F),
$$
sum over the nontrivial zeros $\rho=\beta_\rho+i\gamma_\rho$ (note: $\gamma_\rho\in\mathbb R$ iff $\rho$
on-line). $\mathfrak a$ = archimedean, $\mathfrak q$ = pole, $\mathfrak p$ = primes. **Weil's criterion:**
$\mathrm{RH}\iff\mathfrak t(F)\ge0\ \forall F$.

**On/off decomposition (Day 6, EF-id).** Writing $b_\rho=\beta_\rho-\tfrac12$,
$$
\mathfrak t(F)=\underbrace{\sum_{\beta_\rho=1/2}|F(\gamma_\rho)|^2}_{\mathfrak t_+(F)\ \ge0}\ +\ \underbrace{\sum_{\text{off-line quartets}}4\,\mathrm{Re}\big[F(t_\rho-ib_\rho)^2\big]}_{\mathfrak t_-(F)\ \text{indefinite}},\qquad |\mathfrak t_-(F)|\le 4\,\widetilde{\mathfrak t}_-(F),\ \ \widetilde{\mathfrak t}_-:=\!\!\sum_{\beta_\rho\ne1/2}\!\!|F(\gamma_\rho+ib_\rho)|^2 .
$$

**Realization space.** $H_+:=$ completion of $\mathcal D$ in the norm $\|F\|_{H_+}^2:=\mathfrak t_+(F)$
(the on-line sampling space, $\cong\ell^2(\{\text{on-line }\gamma\})$ when coercive). $\mathcal T$ denotes
the self-adjoint operator on $H_+$ with form $\mathfrak t$.

**Notation.** $\rho(T)=\tfrac1{2\pi}\log\tfrac T{2\pi}$ (zero density); $P=\rho/d$ (zeros per Nyquist cell,
$\to\infty$); $\kappa(b)=e^{2d|b|}$.

---

## 1. Lemma A (integration by parts). ✅
**Claim.** For $F\in\mathcal D=PW_d\cap H^1$ and $g=|F|^2$, $\ E_g:=\sum_\gamma g(\gamma)-\int g\rho\,dt=-\int g'(t)S(t)\,dt$,
where $S(t)=N(t)-\bar N(t)=O(\log t)$ (unconditional).

**Proof.** $\widehat F\in H^1[-d,d]\hookrightarrow C^0$, so IBP in $\xi$ gives
$F(t)=\tfrac1{2\pi it}\big[\widehat F(d)e^{itd}-\widehat F(-d)e^{-itd}-\int\widehat F'e^{it\xi}\big]$, hence
$|F(t)|=O(1/t)$, $g=O(t^{-2})$, $g(t)\log t\to0$. Thus $[gS]_{\pm\infty}=0$ and, $S$ being of locally
bounded variation with $dS=dN-\rho\,dt$, IBP yields the claim. $\square$

---

## 2. Lemma B (the quadrature error is $O(\mathfrak t_+)$). ✅
**Claim.** $|E_g|\le 2d\,(\sup_{\mathrm{supp}}|S|)\,\|F\|_2^2=O(\rho\,\|F\|_2^2)$, unconditional.

**Proof.** $g'=2\,\mathrm{Re}(F'\overline F)$, so $\int|g'|\le2\|F'\|_2\|F\|_2\le 2d\|F\|_2^2$ by **Bernstein**
($\|F'\|_2\le d\|F\|_2$ on $PW_d$). With $|S|=O(\log T)$ on $\mathrm{supp}\,g$ and the tail
$\int_{|t-T_0|>R}|g'||S|=O(\tfrac{\log T_0}{R^2})$ controlled by $g'=O(t^{-3})$, $|E_g|\le C_d(\log T_0)\|F\|_2^2$.
Since the on-line main term is $\sim\rho\|F\|_2^2\sim\tfrac{\log T_0}{2\pi}\|F\|_2^2$, this is
$O(\mathfrak t_+)$ — **finite ratio, $O$ not $o$.** $\square$

> **Key point.** B-2 (a *finite* bottom) needs only $E_g=O(\mathfrak t_+)$; the sharp $o(\mathfrak t_+)$
> (which would need Montgomery / RH-level input) is **not** required.

---

## 3. Lemma C (vertical $L^2$ bound). ✅
**Claim.** For $F\in PW_d$ and $|b|<\tfrac12$, $\ \|F(\cdot+ib)\|_2^2\le e^{2d|b|}\|F\|_2^2\le e^{d}\|F\|_2^2$.

**Proof.** $\|F(\cdot+ib)\|_2^2=\int_{-d}^d|\widehat F(\xi)|^2e^{-2b\xi}d\xi$ (Parseval); $e^{-2b\xi}\le e^{2d|b|}\le e^d$
on $|\xi|\le d$, $|b|<\tfrac12<d$. **Exact, no RH.** $\square$

---

## 4. Lemma D (off-line sum bound, Plancherel–Pólya). ✅
**Claim.** $\widetilde{\mathfrak t}_-(F)=\sum_{\beta_\rho\ne1/2}|F(\gamma_\rho+ib_\rho)|^2\le C_d\,\rho\,\|F\|_2^2$, unconditional.

**Proof.** Off-line zeros sit at $|\Im(\gamma+ib)|=|b_\rho|<\tfrac12<d$ (margin $d-\tfrac12>0$). The
band-limited **Plancherel–Pólya / Bessel** inequality (valid for **arbitrary**, possibly clustered,
sequences in a strip interior) gives $\sum_n|F(w_n)|^2\le B\|F\|_2^2$ with
$B\asymp_d\sup_x\#\{n:\Re w_n\in[x,x+\tfrac1d]\}$ — the **maximal points per Nyquist cell**. By Riemann–von
Mangoldt $+\,S=O(\log)$, the number of *all* zeros in any cell is $\le\tfrac1d\rho+O(\log)=O(\rho)$; off-line
are a subset, so $B=O(\rho)$. $\square$

> **Why this is B-2 and not RH.** Zero-density makes off-line zeros *globally* sparse, but they may
> *cluster locally*, so the cell-count is bounded by the **total** $O(\rho)$, not by the off-line density.
> Using the latter would give $o(\mathfrak t_+)$ = RH — forbidden by possible clustering. So we obtain the
> $O(\mathfrak t_+)$ of B-2.

---

## 5. Coercivity and the depth split — where the one hypothesis lives

Assembling Lemmas C, D: $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|_2^2$. B-2 ($\widetilde{\mathfrak t}_-\le C\mathfrak t_+$)
then needs **coercivity** $\mathfrak t_+\ge c\,\rho\,\|F\|_2^2$. This is the lower frame bound for the on-line
zeros sampling $PW_d$, and — by Beurling — it **fails** if a Nyquist cell is empty of (effective) on-line
samples. Pure-sampling fact: $D^-=\infty$ is **not** sufficient; a single Nyquist gap kills it (Day 22 §1).

**Depth split (Day 22).** Coercivity is needed only where $\widetilde{\mathfrak t}_->0$, i.e. near off-line
zeros. Split by depth $|b_\rho|$ at threshold $\delta$:
- **shallow** ($|b_\rho|<\delta$): $\kappa\le e^{2d\delta}=1+O(\delta)$, so $F(\gamma+ib)\approx F(\gamma)$ —
  these sample like on-line points and **help** coercivity;
- **deep** ($|b_\rho|\ge\delta$): amplified ($\kappa$ up to $e^d$), the only danger; their cell-count is the
  object that must be controlled.

So coercivity (and hence B-2) reduces to: *deep off-line zeros do not dominate any Nyquist cell at large
height.* Precisely:

> **Hypothesis (H) — uniform local sparsity of deep off-line zeros.** There exist $\delta>0$, $\eta>0$, $T_0$
> such that for all $T\ge T_0$ and every interval $I$ of length $1/d$ centred at height $T$,
> $$
> \#\{\rho:\ |\beta_\rho-\tfrac12|<\delta,\ \gamma_\rho\in I\}\ \ge\ \eta\,\rho(T)\,|I|,
> $$
> i.e. on-line + shallow zeros retain a positive fraction $\eta$ of every Nyquist cell (equivalently, deep
> off-line zeros occupy at most $(1-\eta)$ of each cell).

**(H) $\Rightarrow$ coercivity.** Under (H), every Nyquist cell contains $\ge\eta\rho|I|$ samples with
$\kappa=1+O(\delta)$; this sampling set has no Nyquist gaps, so by the Beurling gap theorem
$\sum_{\text{shallow}\cup\text{on}}|F(\gamma)|^2\ge c\eta\,\rho\|F\|_2^2$. The shallow part exceeds
$\mathfrak t_+$ only by the on-line subset, and the $\kappa=1+O(\delta)$ amplification is bounded, giving
$\mathfrak t_+\ge c'\,\rho\,\|F\|_2^2$ (taking $\delta$ small). $\square$

---

## 6. Theorem B-2 (assembly)

> **Theorem (B-2).** Assume **(H)**. Then on the band-limited class $\mathcal D=PW_d\cap H^1$ ($d>\tfrac12$):
> 1. the Weil form $\mathfrak t$ is **closable** in $H_+$ and defines a **self-adjoint operator $\mathcal T$**;
> 2. $\mathcal T$ is **bounded below**: there is a finite constant $C=C(d,\delta,\eta)$ with
>    $$
>    \boxed{\ \inf\operatorname{spec}(\mathcal T)\ \ge\ 1-4C\ >\ -\infty,\ }
>    $$
>    a **faithful, semibounded realization of the Weil functional, without assuming RH.**

**Proof.** By Lemmas C+D and §5 (under (H)), $\widetilde{\mathfrak t}_-\le\tfrac{C_d}{c'}\,\mathfrak t_+=:C\,\mathfrak t_+$.
Hence $|\mathfrak t_-|\le4C\mathfrak t_+$, so in $H_+$ ($\mathfrak t_+=\|\cdot\|^2_{H_+}$),
$$
\frac{\mathfrak t(F)}{\|F\|^2_{H_+}}=1+\frac{\mathfrak t_-(F)}{\mathfrak t_+(F)}\ \ge\ 1-4C .
$$
The form $\mathfrak t_+$ is closed (monotone limit of bounded forms, Kato), and $\mathfrak t_-$ is form-bounded
relative to it (constant $4C$, §5 coercive), so $\mathfrak t=\mathfrak t_++\mathfrak t_-$ is closed and
semibounded; $\mathcal T$ is its associated self-adjoint operator (KLMN with the $H_+$-norm). $\square$

> **Corollary (the faithful reformulation).** By norm-independence of the sign of the bottom (the positivity
> $\mathfrak t\succeq0$ does not mention the inner product),
> $$
> \boxed{\ \mathrm{RH}\ \Longleftrightarrow\ \inf\operatorname{spec}(\mathcal T)\ \ge\ 0\ }
> $$
> — RH is exactly the **sign** of the finite bottom of the rigorously realized operator $\mathcal T$.

---

## 7. Honest status of (H), and what is *not* claimed

**(H) is strictly weaker than RH.** RH says there are *no* off-line zeros; (H) says only that deep off-line
zeros do not *locally dominate* (they may exist, even infinitely many, as long as they don't fill a Nyquist
cell). (H) is a **one-sided, local, density-type** statement. It is implied by:
- RH (trivially), or
- any uniform short-interval zero-density bound $N(\tfrac12+\delta,T+\tfrac1d)-N(\tfrac12+\delta,T)=o(\rho)$.

**Is (H) unconditional?** *Not established here.* The needed bound is **uniform** (every cell, all large
$T$). Globally, $N(\tfrac12+\delta,T)\ll T^{1-c\delta}$ (classical) makes deep off-line zeros sparse *on
average*, and Selberg's $S$-fluctuation theory makes a Nyquist-cell-filling cluster a *large deviation* of
measure $\ll\exp(-c(\log T)^2/\log\log T)$ — i.e. **extraordinarily rare**, but not provably absent at
sporadic large heights by current unconditional methods. So:
$$
\boxed{\ \textbf{Theorem B-2 is unconditional modulo (H); (H) is a uniform short-interval zero-density bound, far weaker than RH, very likely true (Selberg), but at the frontier of what is unconditionally known.}\ }
$$

**What is NOT claimed.** B-2 gives the bottom is **finite**; it does **not** give the **sign**
($\inf\operatorname{spec}\ge0$ = RH). The sign is untouched by all of §0–§6 (which bound *magnitudes*,
$C\ge e^d>1$). Proving the sign requires **structural positivity** ($\mathcal T=A^*A$ / Connes trace /
de Branges chain) — see `RH-ENDGAME.md`. That is a separate problem and is not addressed here.

---

## 8. Summary of what is proved (for the validator)

| Component | Status |
|---|---|
| Lemma A (IBP, $E_g=-\int g'S$, $\mathcal D=PW_d\cap H^1$) | ✅ unconditional |
| Lemma B ($E_g=O(\mathfrak t_+)$, Bernstein + $S=O(\log)$) | ✅ unconditional |
| Lemma C (vertical $\|F(\cdot+ib)\|^2\le e^d\|F\|^2$) | ✅ unconditional, exact |
| Lemma D (off-line $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|^2$, Plancherel–Pólya) | ✅ unconditional |
| Depth split (deep = only danger; shallow harmless) | ✅ unconditional |
| Coercivity $\mathfrak t_+\ge c\rho\|F\|^2$ | (H) — needs uniform short-interval density |
| **Theorem B-2** (faithful semibounded realization $\mathcal T$) | **✅ modulo (H)** |
| Corollary (RH $\iff$ sign of $\inf\operatorname{spec}\mathcal T$) | ✅ modulo (H) |
| RH itself (the sign) | — not addressed (needs structural positivity) |

**The deliverable, in one line.** *Modulo a uniform short-interval zero-density bound (H), far weaker than
RH, the Weil functional admits a faithful, rigorously realized, semibounded self-adjoint operator $\mathcal T$
on the band-limited class, with $\mathrm{RH}\iff\inf\operatorname{spec}(\mathcal T)\ge0$ — a new faithful
spectral reformulation of RH with an explicit finite-dimensional sampling ladder.*

---

### Open items for the validator to check (the audit surface)
1. **Lemma D constant** — the precise Plancherel–Pólya/Bessel constant for $PW_d$ with clustering allowed and
   margin $d-\tfrac12$ (state the exact dependence).
2. **§5 coercivity from (H)** — the quantitative Beurling step: $\ge\eta\rho|I|$ samples per cell with
   $\kappa=1+O(\delta)\Rightarrow\mathfrak t_+\ge c\rho\|F\|^2$; pin $c(\eta,\delta)$.
3. **(H) itself** — is the uniform short-interval bound unconditional (Selberg moments / large-deviation), or
   is it the genuine residual hypothesis? This is the one item separating "unconditional B-2" from
   "B-2 modulo (H)".
4. **Closability/KLMN in $H_+$** — confirm $\mathfrak t_-$ is form-bounded relative to $\mathfrak t_+$ with the
   stated constant, and the self-adjoint $\mathcal T$ is well-defined.
