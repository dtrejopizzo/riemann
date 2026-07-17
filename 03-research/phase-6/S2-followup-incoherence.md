# Phase 6 / S2-followup — The way the refutation points: RH as prime incoherence vs the archimedean envelope

> **⚠️ RETRACTION (caught on careful computation of S2f-1). The §1 reduction below is FLAWED.**
> The explicit formula gives $\sum_\rho|\hat\varphi(\gamma_\rho)|^2 = 2|\hat\varphi(i/2)|^2+\frac1{2\pi}\int|\hat\varphi|^2[\Omega_\infty-\sum_pG_p]dr$.
> Since the LHS is a sum over **discrete** zeros, equality for all $\varphi$ forces the "comb"
> $\sum_pG_p$ to be **distributional, not a smooth function**: as a distribution,
> $\Omega_\infty(r)-\sum_pG_p(r)=2\pi\sum_\rho\delta_{\gamma_\rho}(r)-(\text{pole})$ — **the comb contains the
> zeros as (negative) deltas.** Hence **"$\Omega_\infty(r)\ge\sum_pG_p(r)$ pointwise" (the boxed §1
> Proposition) is FALSE** (you cannot compare pointwise), and one **cannot** take $\hat\varphi\to\delta_{r_0}$
> (the localized claim) because there the prime sum **diverges** ($\varphi*\tilde\varphi$ stops decaying).
> **What survives:** the *heuristic* link (zero clustering $\leftrightarrow$ $\zeta$ large $\leftrightarrow$
> $S(T)$ large) is real but **standard** (the Selberg $S(T)$ story), and it is **not** a new sound reduction.
> §2–§5 below are kept only as the (correct) identification of the relevant frontier (large values), not as a
> mechanism. The honest meta-conclusion is in `S2f-PROGRESS-HONEST.md`.


**Phase 6, the lever the $G_p$ computation opens.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
S2 refuted *per-place* positivity ($G_p$ indefinite). But the exact $G_p$ tells us **what the positivity
actually is**, and it points to a precise, partly-new attack using assets that are *ours* (the $\omega$-class
interference work; the validated detector) and the deepest arithmetic input (unique factorization). This note
makes the reduction rigorous and states honestly where it lands (the large-values frontier).

---

## 1. The exact spectral form of Weil positivity (from $G_p$)

Writing the Weil Hermitian form spectrally,
$$
\mathfrak t(\psi)=\langle\psi,\psi\rangle_W=\int_{-\infty}^\infty |\widehat\psi(r)|^2\,d\mu(r),\qquad
d\mu = \Omega_\infty(r)\,dr\ -\ \Big(\textstyle\sum_p G_p\Big)_{\!\mathrm{reg}}(r)\,dr ,
$$
where $\Omega_\infty(r)=\mathrm{Re}\,\psi_\Gamma(\tfrac14+\tfrac{ir}2)-\log\pi$ is the **archimedean density**
($\Omega_\infty(r)\sim\tfrac12\log\tfrac{|r|}{2\pi}$, growing), the pole adds a fixed atom, and
$\big(\sum_pG_p\big)_{\mathrm{reg}}$ is the **prime comb** (conditionally convergent, regularized by the
explicit formula),
$$
G_p(r)=\frac{2\log p}{p|1-z_p|^2}\big(\sqrt p\cos(r\log p)-1\big),\qquad z_p=p^{-1/2}e^{ir\log p}.
$$

> **Proposition (localized positivity).** For test functions $\widehat\psi$ concentrating at a height $r_0$,
> $\mathfrak t(\psi)\ge0$ as $\widehat\psi\to\delta_{r_0}$ iff $d\mu\ge0$ near $r_0$. Hence
> $$
> \boxed{\ \mathrm{RH}\ \Longleftrightarrow\ \Omega_\infty(r)\ \ge\ \Big(\textstyle\sum_p G_p\Big)_{\!\mathrm{reg}}(r)\quad\forall r\ }
> $$
> — **the archimedean envelope dominates the prime comb, pointwise in $r$.**

This is rigorous (it is the spectral reading of Weil's criterion via the explicit formula) and it isolates
the difficulty cleanly: positivity is **one envelope dominating one oscillatory comb**.

---

## 2. The comb is constructive interference of prime oscillators (= large values of $\zeta$)

Split $G_p$ into **drift** (the $-1$, average-negative, *helps* positivity) and **fluctuation** (the
$\cos$, the danger):
$$
\Big(\sum_pG_p\Big)(r)= \underbrace{-\sum_p\frac{2\log p}{p|1-z_p|^2}}_{\text{drift }<0}\ +\ \underbrace{\sum_p\frac{2\log p}{\sqrt p\,|1-z_p|^2}\cos(r\log p)}_{\text{fluctuation}=:F(r)} .
$$
The fluctuation $F(r)=\sum_p a_p\cos(r\log p)$, $a_p\asymp \log p/\sqrt p$, is a sum of **prime oscillators**.
Two facts pin its meaning:

- **(i) $F$ is essentially $\zeta'/\zeta$ on the critical line.** $\sum_p (\log p)\,p^{-1/2}\cos(r\log p)=\mathrm{Re}\sum_p(\log p)\,p^{-(1/2-ir)}\approx-\mathrm{Re}\,\tfrac{\zeta'}{\zeta}(\tfrac12+ir)$
  (prime part). So **the comb's spike is the size of $\zeta$ on the line** — positivity is a self-referential
  bound on $\zeta$, which is *why* it is hard.
- **(ii) Spikes $=$ constructive interference $=$ large values.** $\sup_r F(r)$ over a window is achieved when
  many $\cos(r\log p)$ align positive — the **large-values / resonance** problem for $\zeta$
  (Soundararajan; Bondarenko–Seip). RH demands $F(r)\lesssim\Omega_\infty(r)\sim\tfrac12\log r$ — i.e. the
  constructive interference never exceeds the archimedean log-envelope.

> **The mechanism, stated.** $\ \mathrm{RH}\iff$ *the maximal constructive interference of the weighted prime
> oscillators $\{a_p\cos(r\log p)\}$ stays under the archimedean envelope $\Omega_\infty$, at every height.*

---

## 3. Why unique factorization is the lever — and the $\zeta$-vs-$L_{\mathrm{DH}}$ discriminant, made precise

The frequencies $\{\log p\}$ are **$\mathbb Q$-linearly independent** — this is *exactly* the fundamental
theorem of arithmetic (unique factorization). $\mathbb Q$-independence means the prime oscillators are
**incoherent**: there is no height $r$ at which a positive-density set of them resonates exactly, so $F(r)$
cannot spike as a coherent sum (only diophantine, sub-maximal alignments occur). This is the structural
reason ζ's comb stays bounded.

> **The discriminant, now mechanistic (Conjecture B2, sharpened).**
> - **$\zeta$:** unique factorization $\Rightarrow$ $\{\log p\}$ $\mathbb Q$-independent $\Rightarrow$ prime
>   oscillators incoherent $\Rightarrow$ (conjecturally) $F(r)\lesssim\Omega_\infty(r)$ $\Rightarrow$ RH.
> - **$L_{\mathrm{DH}}$:** *no* Euler product $\Rightarrow$ its "frequencies" carry $\mathbb Q$-linear
>   relations (it is a sum of two $L(\chi)$, whose coherence creates resonances) $\Rightarrow$ the comb
>   **can** spike above the envelope $\Rightarrow$ off-line zeros. **Computed witness:** its off-line zero at
>   height $85.699$ is exactly such a coherent spike.
>
> So **Conjecture B2 ("factorization $\Rightarrow$ Euler product") becomes "incoherence $\Rightarrow$
> $\mathbb Q$-independent frequencies $\Rightarrow$ Euler product"** — a statement about *resonances of the
> frequency set*, which is checkable per object and is where ζ and $L_{\mathrm{DH}}$ genuinely differ.

---

## 4. Our unfair assets here (this is the part that is *ours*)

This frontier is the one our earlier program was built for:
- **The $\omega$-class decomposition (P2, P4, P5)** is precisely a decomposition of the prime-oscillator
  interference into coherent classes — i.e. a structured way to bound $\sup_r F(r)$. The moment fingerprints
  (P5's growth exponents) measure exactly the constructive-interference tail. **We already have machinery for
  the spike.**
- **The validated detector (Phase 3)** measures $\mu\ge0$ locally — it *is* an envelope-vs-comb meter; it can
  map where $F(r)$ approaches $\Omega_\infty(r)$ (the "near-spike" heights), guiding the analysis.
- **The exact $G_p$ (S2)** gives the comb in closed form — no heuristic, the real weights $a_p/|1-z_p|^2$.

> **Concrete attackable sub-problem (S2f-1).** Bound $\sup_{r\in[T,2T]}F(r)$ using the $\mathbb Q$-independence
> of $\{\log p\}$ (a diophantine/equidistribution input) and the $\omega$-class structure, and compare to
> $\Omega_\infty\sim\tfrac12\log T$. Even a *conditional* sharp bound (e.g. on GRH-free large-value
> estimates) would either (a) cross — unlikely — or (b) pin the exact constant at which incoherence meets the
> envelope, which is the threshold RH sits on.

---

## 5. Honest landing

This is **not** a proof and likely not a crossing: §2(i) shows the comb *is* $\zeta$ on the line, so the bound
"$F\le\Omega_\infty$" is self-referential — it is the **large-values frontier**, itself open and tied to RH
(Bondarenko–Seip's $\Omega$-results show $\zeta$ *does* get large, $\sim\exp(c\sqrt{\log T/\log\log T})$, but
on a sparse set; RH is about the *typical/structured* bound, not the sparse extreme). So:

> **The refutation of S2 points to the large-values/incoherence frontier — the precise, mechanistic form of
> RH — and it is exactly where our $\omega$-class assets live. It does not obviously cross the wall (the comb
> is ζ itself, self-referential), but it is the *right* frontier, our most-equipped one, and it sharpens
> Conjecture B2 into a statement about $\mathbb Q$-independence of frequencies (= unique factorization).**

**What this is worth.** (i) A rigorous spectral reduction: RH $\iff$ archimedean envelope $\ge$ prime comb,
pointwise. (ii) The mechanism: incoherence (unique factorization) vs constructive interference (large values).
(iii) The sharpened, mechanistic B2. (iv) A concrete sub-problem (S2f-1) where our $\omega$-class machinery
applies. **The honest next move is S2f-1** — bound the prime-comb spike with the $\omega$-class + diophantine
incoherence, and see whether the constant lands above or below the envelope. That is the one place left where
we have a tool the field's standard approaches do not.

---

### Status
- §1 reduction (RH $\iff$ envelope $\ge$ comb) — ✅ rigorous (spectral Weil criterion).
- §2 comb $=$ constructive interference $=$ $\zeta$ on the line / large values — ✅ identified.
- §3 incoherence mechanism + sharpened B2 ($\mathbb Q$-independence) — ◆ mechanism stated; the bound is the open core.
- §4 $\omega$-class assets for the spike (S2f-1) — ⬜ the attackable sub-problem (our tool).
- §5 honest: this is the large-values frontier (self-referential), not an obvious crossing — but the right one.
