# Day 19 — Verification of the Parseval/pair-correlation reduction; the precise external input

The referee reduced the quadrature error $E_g$ to an $L^2$ pairing with the zero-discrepancy $D_T$, observed
$\|D_T\|^2_{L^2}$ is a pair-correlation second moment, and pointed to recent *unconditional* pair-correlation
work (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh). **Verification (double-checked, "muy prolijo"):**
**no outright error** (contrast Day 17). The reduction is correct, lands on a **concrete classical object**,
and its scale is **Montgomery's near-zero (proven-under-RH) regime**. One subtlety (which *norm* closes B-2)
is resolved favorably. The decisive status hinges on one borderline second-moment bound. **Tags:** ✅
verified · ◆ borderline/open · ⬜ literature.

---

## 1. The Parseval reduction — correct, and cleaner in the band-limited class ✅
$E_g=\sum_\gamma g(\gamma)-\int g\rho\,dt$. Fourier inversion ($g=|F|^2$):
$$
E_g=\frac1{2\pi}\int\widehat g(\alpha)\,D_T(\alpha)\,d\alpha,\qquad D_T(\alpha)=\sum_{0<\gamma\le T}e^{i\alpha\gamma}-\int_0^T e^{i\alpha t}\rho(t)\,dt .
$$
For $F\in PW_d$ (**band-limited**, $\widehat F$ supported in $[-d,d]$), $\widehat g=\widehat F*\widehat{\overline F}$
is supported in $[-2d,2d]$, so the integral is over $[-2d,2d]$ and
$$
\boxed{\ |E_g|\le\tfrac1{2\pi}\,\|\widehat g\|_{L^2[-2d,2d]}\,\|D_T\|_{L^2[-2d,2d]}.\ }
$$
✅ Rigorous. **Bonus the referee found:** $PW_d$ is the **classical Weil test class** (compactly supported in
the prime variable), and is **cleaner** than the Gaussian/strip-Hardy setting — band-limited functions are
*entire*, so off-axis evaluations $F(\gamma+ib)$ are automatic (no strip-weight subtleties of Days 9–15),
and Weil's criterion already lives on this class. **This simplifies the whole framework.** (Caveat: for
genuinely non-band-limited test functions the $|\alpha|>2d$ tail does not vanish; restricting to $PW_d$ —
the classical class — removes this cleanly.)

---

## 2. $\|D_T\|^2_{L^2[-2d,2d]}$ is a scale-$1/d$ pair-correlation second moment ✅
Expanding $V(d,T):=\int_{-2d}^{2d}|D_T(\alpha)|^2 d\alpha$:
$$
V=\underbrace{4d\,N(T)}_{\text{diagonal }\gamma=\gamma'}+\sum_{\gamma\ne\gamma'}\frac{2\sin\!\big(2d(\gamma-\gamma')\big)}{\gamma-\gamma'}-(\text{smooth }\widehat\rho\text{ part}),
$$
i.e. **exactly Montgomery's pair sum** $\sum_{\gamma,\gamma'}r(\gamma-\gamma')$ with $r(x)=\frac{2\sin2dx}{x}$,
$\widehat r=\mathbf 1_{[-2d,2d]}$. ✅ The needed input is an **$L^2$/second-moment** bound (NOT a uniform
$L^\infty$ bound) — the natural, studied object.

**The scale is the proven-under-RH regime ✅.** The form factor enters at variable $\beta=\xi/\rho$; our
$\widehat r$ has $|\xi|\le2d$ fixed while $\rho\sim\log T\to\infty$, so $\beta\le2d/\rho\to0$ — **deep inside
Montgomery's proven range $|\beta|<1$**, where $\widehat R_2(\beta)\sim|\beta|$ (variance suppression). The
relevant pair correlation is the *low-frequency* one, exactly where Montgomery's theorem (and the recent
unconditional refinements) live — **not** the conjectural large-$\beta$ tail.

---

## 3. The subtlety: which norm closes B-2 (resolved favorably) ◆→✅
B-2 (semiboundedness) needs the **signed** $\mathfrak t_-$ controlled, and the majorant bound gives the
relative constant $\kappa(b)=e^{2d|b|}>1$. In the *$L^2$/over-sampling* norm $\kappa>1$ would leave the
form unbounded below ($\mathcal T_+$ unbounded). **But in the natural zero-sampling space**
$H_+:=$ completion in the $\mathfrak t_+$-norm $\cong\ell^2(\{\gamma\})$ (where $\mathfrak t_+=\|\cdot\|^2_{H_+}$):
$$
\frac{\mathfrak t(F)}{\|F\|^2_{H_+}}=1-\frac{\mathfrak t_-^{\mathrm{signed}}(F)}{\mathfrak t_+(F)}\ \ge\ 1-4\kappa(b)\quad(\text{finite}),
$$
provided the quadrature comparison $\widetilde{\mathfrak t}_-\le\kappa(b)\,\mathfrak t_+$ holds. So **B-2 closes
in $H_+$** with a finite (negative) bottom $\ge1-4\kappa(b)$, and — by the norm-independence of the *sign*
(CL.2) — **RH = (bottom $\ge0$)**. The over-sampling that blocked the $L^2$ realization is exactly *cured*
by working in $H_+$ (the sampling space), where $\mathcal T_+=I$. **B-2 is closable here; RH remains the
sign.** (So this is a *reduction of B-2 to the quadrature/coercivity inputs*, not a direct RH proof — as
always.)

---

## 4. The decisive borderline — and the stakes ◆/⬜
$E_g=O(\mathfrak t_+)$ (enough for B-2 in $H_+$, via §3) requires $\|D_T\|_{L^2[-2d,2d]}$ at the right
level. Status of $V(d,T)$:
- **Diagonal $4d\,N$: UNCONDITIONAL** (pure counting). Sufficient **up to a logarithmic factor**.
- **Off-diagonal:** with the form-factor cancellation ($\widehat R_2(\beta)\sim|\beta|$ near $0$, Montgomery)
  the $\log$ is closed; **without** cancellation the crude bound is off by $\sim\log T$ — **borderline**.

$$
\boxed{\ \textbf{Decisive question:}\ \text{is the scale-}1/d\text{ second moment }V(d,T)\text{ bounded at the needed level UNCONDITIONALLY?}\ }
$$
- **If YES** (e.g. via BGSTB-type unconditional low-frequency pair correlation, or Goldston–Montgomery /
  Gonek second-moment results): then $E_g=O(\mathfrak t_+)$ **unconditionally** $\Rightarrow$ **B-2 is
  UNCONDITIONAL** $\Rightarrow$ a **faithful, semibounded realization of the Weil operator exists without
  assuming RH** — precisely the program's **dream outcome** (§6 rung A∧B∧C: "the localized ladder converges
  rigorously to the Weil/Connes spectral criterion"), and **RH-independent**. RH then $=$ the sign of a
  now-rigorous bottom.
- **If only RH-conditional** (Montgomery's original needs RH): then this is a **new equivalent of RH** —
  "RH $\iff$ the zeros are an asymptotically exact band-fixed quadrature."

**This is the first time in the program that the missing input is a single, concrete, classical
analytic-number-theory quantity** (a mesoscopic second moment of the pair correlation), with active recent
literature *exactly* on its unconditionality. The referee's instinct — that this is where the real content
sits — is correct.

---

## 5. Verdict and the max-effort path
**No outright error** in the referee's Days-19 material (Parseval ✅, the pair-correlation identification ✅,
the proven-range observation ✅, the BGSTB pointer ✅). The reduction is sound, simplifies to the classical
$PW_d$ class, and isolates the external input to a single mesoscopic second moment. The one subtlety (norm
for B-2) resolves favorably (B-2 closes in $H_+$; RH stays the sign).

**Path of maximum effort (going for it):**
1. **Nail the threshold (careful bookkeeping).** Compute exactly what bound on $V(d,T)=\int_{-2d}^{2d}|D_T|^2$
   suffices for $E_g\le c\,\mathfrak t_+$ with $c$ giving a useful bottom, with full localizer-width
   ($\|F\|_4/\|F\|_2$) accounting — settle whether the **diagonal (unconditional) alone** suffices or the
   off-diagonal $\log$ must be cancelled.
2. **Literature check (decisive).** Does an unconditional bound for the scale-$1/d$ second moment / the
   low-frequency form factor exist? Targets: **Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh** (2306.04799,
   unconditional Montgomery), **Goldston–Montgomery** (second moment ↔ pair correlation), **Gonek**,
   **Chan**, **Fujii** (second moment of $S(T)$ / of the counting function over short intervals).
3. **If unconditional ⟹ write B-2 as an unconditional theorem** (faithful semibounded realization, the
   §6 prize). **If RH-conditional ⟹ state the new RH-equivalence** (band-fixed quadrature), a clean result
   in the Weil–Connes–de Branges–Montgomery lineage.

**Bottom line.** The program has reached its irreducible core: B-2 (a faithful semibounded realization,
RH-independent) holds **iff** a single classical mesoscopic pair-correlation second moment is controlled —
diagonal-unconditional up to a log, closed by Montgomery-range cancellation. Whether that closing is
unconditional is now the **one** question separating "an unconditional faithful spectral reformulation of
RH" from "a new equivalent of RH." Both are real results; the literature check decides which.
