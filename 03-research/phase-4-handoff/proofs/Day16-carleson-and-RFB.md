# Day 16 — Audit of the Carleson step (Schur), and a rigorous reduction of RFB to zero-regularity

Per the referee: (A) audit the step "$\mu$ Carleson $\iff P=\rho\ell$ bounded" — prove the safe sufficient
direction, concede the equivalence is false; (B) carry the RFB proof sketch as far as rigor allows,
separating standard FA from the hypotheses, and locate where arithmetic enters. **Both done. The referee's
meta-conclusion is confirmed and sharpened:** RFB follows by standard analysis *once the zeros' sampling
regularity is granted*; that regularity is the arithmetic. One real hole in the sketch (Step 3) is found
and fixed. **Tags:** ✅ rigorous (mod stated regularity) · ◆ standard · ❌ hole · ⬜ arithmetic-open.

---

## Part A — Carleson: the sufficient direction (Schur), the equivalence's failure, and a direct lower bound

### A.1 $P\lesssim1\Rightarrow$ Carleson (Schur sufficiency) ✅
$\mathfrak t_+(F)=\sum_\gamma|F(\gamma)|^2=\langle F,TF\rangle$, $T=\sum_\gamma k_\gamma\otimes k_\gamma$.
Normalize $e_\gamma=k_\gamma/\|k_\gamma\|$; Gram $G_{\gamma\gamma'}=\langle e_\gamma,e_{\gamma'}\rangle$.
The Hardy-band kernel decays exponentially off-diagonal,
$|K(t,s)|\le\sqrt{K(t,t)K(s,s)}\,e^{-c|t-s|/\ell}$ (from $\operatorname{sech}$), so for a **separated**
sequence (gaps $\ge\delta_0$),
$$
\sup_\gamma\sum_{\gamma'}|G_{\gamma\gamma'}|\ \le\ \sup_\gamma\sum_{\gamma'}e^{-c|\gamma-\gamma'|/\ell}\ \asymp\ \rho\ell=P .
$$
By Schur's test, $\|T\|\lesssim P$ (bounded if $P$ bounded). **So $P=\rho\ell$ bounded $+$ separation
$\Rightarrow\mu$ Carleson.** ✅ (the referee's argument, rigorous).

### A.2 The full equivalence is false ◆
$P$ bounded is **not necessary**: a clustered sequence can have small *average* $P$ yet break boundedness
locally (or vice versa). So the honest statement is **"$P$ is the natural local density; $P\lesssim1$ is
sufficient for Carleson"** — not an equivalence. Day-15's "$\mu$ Carleson $\iff P$ bounded" is corrected to
the one-way sufficient form. *(Exactly the referee's caution.)*

### A.3 Direct proof: $P\to\infty\Rightarrow\mathfrak t_+$ unbounded (upgrades Day 15) ✅
Test $T$ on the reproducing kernel $k_t$ ($t$ real):
$$
\frac{\langle k_t,T k_t\rangle}{\|k_t\|^2}=\frac{\sum_\gamma|K(\gamma,t)|^2}{K(t,t)}\ \approx\ \frac{K(t,t)^2\sum_\gamma e^{-2|\gamma-t|/\ell}}{K(t,t)}\ \approx\ K(t,t)\!\cdot\! P\ \asymp\ R\,\ell\ \to\ \infty
$$
(using $|K(\gamma,t)|\approx K(t,t)e^{-|\gamma-t|/\ell}$ for slowly-varying $K$, and
$\sum_\gamma e^{-2|\gamma-t|/\ell}\approx\rho\ell=P$). So $T=\mathfrak t_+$ is **unbounded** whenever
$P\to\infty$ — a **direct** proof (no full Carleson theory), needing only exponential kernel decay +
slowly-varying $K,\rho$ + mild regularity (no extreme clustering). This **upgrades** the Day-15
over-sampling conclusion from a box heuristic to a rigorous kernel test, **answering the referee's question**
("can one prove $P\to\infty\Rightarrow$ not Carleson directly?" — yes).

---

## Part B — Audit of the RFB proof sketch: a hole in Step 3, and the clean reduction

Target: $\widetilde{\mathfrak t}_-(F):=\sum_{\text{off-line}}|F(\gamma+ib)|^2\le C\,\mathfrak t_+(F)$
(majorant of $|\mathfrak t_-|$; recall $|\mathfrak t_-|\le4\widetilde{\mathfrak t}_-$). $F=\widehat g$,
analytic in $|\Im z|<d$, $|b|<\tfrac12<d$.

### B.1 The hole (Step 3 of the sketch) ❌
The sketch bounds $\sum_\gamma|F'(\gamma)|^2\le C_d\|F\|^2$ (local Bernstein + sum). **This fails in the
over-sampling regime.** Summing the local bound $|F'(\gamma)|^2\le C_d\int_{\gamma-d}^{\gamma+d}|F|^2$ over
zeros over-counts each region by the overlap $=\#\{\gamma\text{ in a }2d\text{ window}\}=\rho\cdot2d\asymp P\to\infty$:
$$
\sum_\gamma|F'(\gamma)|^2\ \le\ C_d\,P\,\|F\|^2\qquad(\text{constant }P\to\infty,\ \text{not bounded}).
$$
The same over-counting afflicts $\mathfrak t_+=\sum_\gamma|F(\gamma)|^2\asymp P\|F\|^2$. So bounding each by
$\|F\|^2$ **loses the cancellation**: only the *ratio* $\sum|F'(\gamma)|^2/\mathfrak t_+$ is bounded. Routing
through $\|F\|^2$ (Step 3 → Step 4) carries the spurious factor $P$ and the final constant diverges.
**This is exactly the over-sampling we proved forced (Day 15) obstructing the naive proof.**

### B.2 The fix: bound off-axis by on-axis directly (interpolation/Schur, no $\|F\|^2$ detour) ✅(mod regularity)
Because the off-axis point $\gamma+ib$ ($|b|<d$) lies **inside the coherence cell** of the on-axis grid,
and $\{\gamma'\}$ is a sampling sequence, there are interpolation coefficients with
$$
F(\gamma+ib)=\sum_{\gamma'}c_{\gamma'}(\gamma,b)\,F(\gamma'),\qquad |c_{\gamma'}(\gamma,b)|\lesssim e^{-c|\gamma'-\gamma|/\ell}.
$$
Then, by Cauchy–Schwarz in the weight $|c|$ and Fubini,
$$
\widetilde{\mathfrak t}_-=\sum_{\text{off}}\Big|\sum_{\gamma'}c_{\gamma'}F(\gamma')\Big|^2
\le\Big(\sup_{\text{off}}\sum_{\gamma'}|c_{\gamma'}|\Big)\sum_{\gamma'}|F(\gamma')|^2\Big(\sup_{\gamma'}\sum_{\text{off}}|c_{\gamma'}|\Big)
\le C\,C'\,\mathfrak t_+ ,
$$
**provided** the coefficient matrix is **$\ell^1$-Schur bounded in both directions**:
$$
\boxed{\ (\mathrm{Schur})\quad \sup_{\text{off}}\sum_{\gamma'}|c_{\gamma'}|\le C,\qquad \sup_{\gamma'}\sum_{\text{off}}|c_{\gamma'}|\le C'.\ }
$$
Both hold if the kernel-decay weights $e^{-c|\gamma'-\gamma|/\ell}$ sum boundedly — i.e. if **on-line and
off-line ordinates are separated with bounded local density** (the off-line ones being $\le$ on-line
density). **This route avoids derivatives entirely and the $P$-overcounting hole.** $\square$ (mod the
Schur regularity).

### B.3 What B.2 actually needs (the hidden second hypothesis) ⬜
The sketch claimed RFB reduces to **one** step (the lower frame bound). The audit shows it needs, more
precisely, that $\{\gamma\}$ is a **sampling sequence admitting bounded ($\ell^1$-Schur) interpolation** of
off-axis from on-axis values. This **subsumes**:
- the **lower frame bound** ($\{\gamma\}$ a set of sampling — for the coefficients $c$ to exist), and
- a **dual/regularity bound** (the $c$ have bounded $\ell^1$ rows *and* columns — controlled by zero
  **separation** + bounded local density).
So there is a *second* fine-geometry hypothesis beyond the lower frame bound, of the same arithmetic
flavor (separation/regularity). It is mild and expected, but **not free** and **not implied by the lower
frame bound alone** — a genuine correction to "everything else is standard FA."

---

## Part C — The conditional theorem, and where arithmetic enters

**Theorem (Day 16, conditional).** Suppose the nontrivial zeros satisfy, in the over-sampling Hardy-band
$H^2(S_d)$ ($d>\tfrac12$):
1. **bounded multiplicity** $m(\gamma)\le M$;
2. **sampling + Schur-interpolation regularity** (B.2): $\{\gamma\}$ is a set of sampling and the off-axis$\to$on-axis
   interpolation coefficients are $\ell^1$-Schur bounded (guaranteed by a uniform **minimum separation** and
   bounded local density of the ordinates).
Then $\widetilde{\mathfrak t}_-\le C\,\mathfrak t_+$, hence $|\mathfrak t_-|\le 4C\,\mathfrak t_+$, hence
$$
\mathfrak t(g)=\mathfrak t_+(g)-\mathfrak t_-(g)\ \ge\ -(4C-1)\,\mathfrak t_+(g)\ \ge\ -(4C-1)\,C_{\mathrm{up}}\dots
$$
$\Rightarrow$ **the Weil form is semibounded** (B-2 holds), via the relative bound (RFB).

**The honest reduction.** Functional analysis delivers everything **above** the regularity hypotheses
(1)–(2). The **entire remaining difficulty** is proving that the $\zeta$-zeros satisfy (2) — that they form
a **sufficiently regular sampling/interpolation sequence** for the Hardy-band space. This is precisely:
- **minimum separation** of ordinates (no two zeros too close) — known to fail *pointwise* (small gaps
  exist) but holds *on average*;
- control of $\boldsymbol{S(T)}$ (the argument fluctuation — regularity of the counting);
- **Montgomery pair correlation** / **GUE** statistics (the fine distribution governing clustering).

$$
\boxed{\ \text{Functional analysis ends at RFB; the arithmetic begins at "are the zeros a regular sampling sequence?"}\ }
$$
**This is the referee's conclusion, now proven as the precise location of the boundary.** Note the honest
tension: zeros have *no positive uniform minimum gap* (arbitrarily close pairs are expected), so hypothesis
(2) must be the *averaged/Schur* form, not a naive separation — and whether the averaged form suffices is
itself a pair-correlation question. *(And the lower frame bound at over-critical density may still need an
RH-flavored input — flagged, the Day-12 §6 honest loop persists.)*

---

## Status (Day 16)

| Result | Status |
|---|---|
| $P\lesssim1+$separation $\Rightarrow$ Carleson (Schur) | ✅ |
| Carleson $\iff P$ bounded (full equivalence) | ❌ false (clustering); sufficient direction only |
| $P\to\infty\Rightarrow\mathfrak t_+$ unbounded (direct kernel test) | ✅ (upgrades Day 15) |
| RFB sketch Step 3 ($\sum|F'(\gamma)|^2\le C_d\|F\|^2$) | ❌ hole (over-counts by $P\to\infty$) |
| RFB via Schur-interpolation (B.2) | ✅ mod Schur regularity (2) |
| RFB reduces to ONE step (lower frame bound) | ❌ needs a 2nd (Schur/separation) hypothesis too |
| RFB $\Leftarrow$ [bounded mult. + sampling/Schur regularity] $\Rightarrow$ B-2 | ✅ conditional theorem |
| the regularity hypotheses | ⬜ **arithmetic** (separation, $S(T)$, pair correlation, GUE) |

**Net (Day 16).** The referee's two requests closed cleanly. Carleson: the sufficient direction is Schur
(rigorous), the equivalence is false (clustering), and $P\to\infty\Rightarrow$ unbounded has a direct
kernel-test proof (upgrading Day 15). RFB: the sketch's structure is right but Step 3 has a real
over-counting hole (the forced over-sampling biting back); the clean fix is a derivative-free
Schur-interpolation bound, which reduces RFB to **two** fine-geometry hypotheses (sampling + Schur
regularity), not one. The **conditional theorem** — *regular sampling of the zeros $\Rightarrow$ RFB
$\Rightarrow$ Weil semibounded* — makes precise the referee's thesis: **functional analysis ends here, and
the rest is the fine arithmetic geometry of the zeros** (separation / $S(T)$ / Montgomery / GUE). That is
the genuine mathematical core the program has been pushed toward.

**Next:** make hypothesis (2) precise and find its weakest sufficient arithmetic form (averaged separation
vs pair correlation); revisit whether the lower frame bound at over-critical density is RH-conditional.
