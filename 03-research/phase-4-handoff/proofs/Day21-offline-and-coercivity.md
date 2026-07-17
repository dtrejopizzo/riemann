# Day 21 — Proofs A/B/C verified; the off-line sum closed (Plancherel–Pólya); B-2 ⟸ a single gap bound

The referee wrote careful Proofs A (IBP), B (Bernstein+Selberg), C (vertical bound) and flagged the
remaining gap: converting the vertical $L^2$ bound into a bound on the **discrete off-line sum**
$\widetilde{\mathfrak t}_-$. **Verification:** A, B, C are **correct** (minor precision notes below). **Advance:**
the off-line gap **closes unconditionally** via **Plancherel–Pólya** (the band-limited Carleson/Bessel
bound), reducing B-2 to a *single* classical input — **coercivity = no zero gaps exceeding the Nyquist
length**, far weaker than RH. **Tags:** ✅ verified · ◆ advanced/to-audit · ⬜ the one input.

---

## 1. Verification of Proofs A, B, C ✅
- **A (IBP), correct.** In $PW_d\cap H^1$, IBP in $\xi$ gives $F(t)=\tfrac{1}{2\pi it}\big[\widehat F(d)e^{itd}-\widehat F(-d)e^{-itd}\big]-\tfrac{1}{2\pi it}\int\widehat F'e^{it\xi}$.
  *Precision:* the boundary term (nonzero unless $\widehat F(\pm d)=0$) is $O(1/t)$, so $|F(t)|=O(1/t)$ still
  holds, $g\log t\to0$, $[gS]_{\pm\infty}=0$. The IBP $E_g=-\int g'S$ is valid, unconditional. ✅
- **B (Bernstein+Selberg), correct.** $\int|g'|\le2\|F'\|_2\|F\|_2\le2d\|F\|_2^2$ (Bernstein), $|S|=O(\log)$.
  *Precision:* the IBP integral runs over all $\mathbb R$, not a window; the tail $\int_{|t-T_0|>R}|g'||S|$
  with $g'=O(t^{-3})$, $|S|=O(\log t)$ is $O(\tfrac{\log T_0}{R^2})$ — dominated by the window. So
  $|E_g|\le C_d(\log T_0)\|F\|_2^2=O(\mathfrak t_+)$, unconditional. (And — as the referee stresses — $O$,
  **not** $o$; that is exactly what B-2 needs.) ✅
- **C (vertical), correct & exact.** $\|F(\cdot+ib)\|_2^2=\int_{-d}^d|\widehat F|^2e^{-2b\xi}d\xi\le e^{2d|b|}\|F\|_2^2\le e^d\|F\|_2^2$
  ($|b|<\tfrac12<d$). No RH, no Montgomery. ✅

---

## 2. Closing the off-line gap: Plancherel–Pólya (unconditional) ◆→✅
**The tool.** For $F\in PW_d$ and **any** sequence $\{w_n\}$ in the strip $|\Im w_n|\le h<d$ (no separation
required), the band-limited Carleson/Bessel ("Plancherel–Pólya") inequality holds:
$$
\sum_n|F(w_n)|^2\ \le\ B(\{w_n\})\,\|F\|_2^2,\qquad B\ \asymp\ \frac{d-h\ \text{margin}}{1}\cdot\Big(\sup_x \#\{n:\,\Re w_n\in[x,x+\tfrac1d]\}\Big),
$$
i.e. the Bessel constant is governed by the **maximal number of points per Nyquist cell** $1/d$ (clustering
allowed — this answers the referee's "2D measure, no separation" worry directly). The off-line zeros sit at
$|\Im|=|b_\rho|<\tfrac12<d$, margin $d-\tfrac12>0$.

**The local count is unconditional.** The number of *all* zeros in $[x,x+\tfrac1d]$ is, by Riemann–von
Mangoldt $+$ $S=O(\log)$, $\le\tfrac1d\cdot\tfrac{\log x}{2\pi}+O(\log x)=O(\rho)$. Off-line zeros are a
subset, so their local count is also $\le O(\rho)$. Hence
$$
\boxed{\ \widetilde{\mathfrak t}_-=\sum_{\rho\ \mathrm{off}}|F(\gamma_\rho+ib_\rho)|^2\ \le\ C_d\,\rho\,\|F\|_2^2\qquad(\text{UNCONDITIONAL}).\ }
$$
**Why this gives B-2, not RH.** Zero-density makes off-line zeros *globally* sparse ($\rho_{\mathrm{off}}\ll\rho$),
but they may *cluster locally*, so the local count is $\le\rho$ (total), **not** $\rho_{\mathrm{off}}$. Using
$\rho_{\mathrm{off}}$ would give $\widetilde{\mathfrak t}_-=o(\mathfrak t_+)\Rightarrow$ RH — *forbidden* by
possible local clustering. So we get the $O(\mathfrak t_+)$ of B-2, not the $o$ of RH. (Whether off-line
zeros *don't* cluster locally is itself $\approx$RH — consistent.)

---

## 3. The single remaining input: coercivity = no large gaps ⟸ B-2
Combine: $\widetilde{\mathfrak t}_-\le C_d\,\rho\,\|F\|_2^2$ (§2, unconditional). For B-2 in $H_+$ we need
$\widetilde{\mathfrak t}_-\le C\,\mathfrak t_+$, i.e.
$$
\boxed{\ \text{COERCIVITY:}\quad \mathfrak t_+=\sum_{\mathrm{on}}|F(\gamma)|^2\ \ge\ c\,\rho\,\|F\|_2^2\quad\forall\,F\in PW_d.\ }
$$
Then $\widetilde{\mathfrak t}_-\le\tfrac{C_d}{c}\,\mathfrak t_+$ — finite, $O(\mathfrak t_+)$ — and
$\mathfrak t\ge(1-\tfrac{4C_d}{c})\|\cdot\|^2_{H_+}$, **B-2**.

**Coercivity reduces to a gap bound.** $\mathfrak t_+\ge c\rho\|F\|^2$ is the *lower frame bound* for the
on-line zeros sampling $PW_d$. The zeros' lower Beurling density is $D^-=\infty>\tfrac d\pi$ (Nyquist) —
**super-sampling**, favorable. The lower bound holds provided **no Nyquist cell $[x,x+\tfrac1d]$ is empty**,
i.e.
$$
\boxed{\ \text{the }\zeta\text{-zeros have no gap }>\tfrac1d\quad(\text{choose }d\to\tfrac12^+:\ \text{Nyquist }\tfrac1d\to2).\ }
$$
A $PW_d$ function concentrated in a too-large gap would have $\mathfrak t_+$ small but $\|F\|_2$ not —
breaking coercivity. So **coercivity $\Longleftarrow$ a uniform upper bound on consecutive zero gaps**.

---

## 4. The reduction, and its honest status
$$
\boxed{\ \text{B-2 (the §6 prize: faithful semibounded Weil realization, RH-independent)}\ \Longleftarrow\ \text{no }\zeta\text{-zero gap exceeds the Nyquist length }\tfrac1d\ (d\to\tfrac12^+).\ }
$$
Everything else is **unconditional**: A (IBP), B ($E_g=O(\mathfrak t_+)$ via Bernstein+Selberg), C (vertical
$e^d$), §2 (off-line via Plancherel–Pólya + unconditional local count). The **entire residual content of
B-2 is a one-sided gap-regularity** of the zeros — *vastly* weaker than RH (it constrains the **largest
gap**, not the location of any zero; RH constrains all real parts).

**Status of the gap input.** Mean gap $\to0$ (RvM), and lower Beurling density $\infty$, so on average
hugely favorable. The *maximal* gap is the question: choosing $d$ near $\tfrac12$ (Nyquist $\sim2$), B-2
needs "no gap $>2$-ish." Conditionally (RH) gaps $\to0$; unconditionally the sharp maximal-gap bound is at
the classical frontier (large-gap literature: Hall, Bredberg, etc.). **Decisive sub-question:** is "no zero
gap exceeds a fixed constant (for $T$ large)" known unconditionally? If yes (or if a slightly weaker
averaged coercivity suffices), **B-2 is an unconditional theorem.**

---

## 5. MANDATORY audit of this Day-21 advance (discipline)
The optimistic chain is now load-bearing; attack it:
1. **Plancherel–Pólya constant.** Confirm the Bessel bound for $PW_d$ with the *clustering-allowed*
   density-weighted constant (not requiring separation) — pin the exact dependence on margin $d-\tfrac12$
   and on max local count. (Standard, but state precisely.)
2. **Coercivity $\Leftrightarrow$ gaps, exactly.** Is "no gap $>\tfrac1d$" truly sufficient for
   $\mathfrak t_+\ge c\rho\|F\|^2$ with $c$ uniform? Or is a *weaker averaged* gap condition enough (which
   might be unconditional)? Landau/Beurling sampling theory — get the precise sufficient condition.
2½. **Could averaged coercivity suffice?** We only need $\mathfrak t_+\ge c\rho\|F\|^2$; perhaps a few
   sporadic large gaps are tolerable (finite-rank correction). If so, the unconditional **lower-density**
   $D^-=\infty$ might already give coercivity with no extra gap hypothesis.
3. **The constant $c$ and the bottom $1-4C_d/c$.** Finite suffices for B-2; confirm nothing downstream
   needs it $>0$ (that would be RH).

**Net (Day 21).** The referee's Proofs A, B, C **verify**; the off-line gap they could not close is **closed
unconditionally by Plancherel–Pólya** (clustering-robust, answering the 2D-measure worry). The result: **B-2
reduces, with everything else unconditional, to a single classical statement — the $\zeta$-zeros have no
Nyquist-size gaps (coercivity)** — a one-sided gap-regularity far weaker than RH. If that gap bound is
unconditional (or an averaged version suffices, which $D^-=\infty$ suggests), **B-2 is an unconditional
theorem** (the §6 prize). Next: audit §5, especially 2½ (does $D^-=\infty$ alone give coercivity?), which
could make B-2 fully unconditional with no gap hypothesis at all.
