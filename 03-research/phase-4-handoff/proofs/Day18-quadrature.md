# Day 18 — Verification of the quadrature reformulation, and the reduction-vs-reformulation verdict

The referee, after the Day-17 audit, abandoned Gram/Schur/interpolation and reformulated RFB as a
**band-fixed quadrature** statement (the $P$-cancellation made rigorous via averaging), then audited which
arithmetic input it needs. **Verification (double-checked):** unlike the Day-17 threads, **the quadrature
material contains no outright error** — it is the correct and cleanest formulation. But the input it
requires is **RH-conditional** (Montgomery) or at the known frontier, so this is *most likely a new
equivalent of RH*, not an unconditional reduction — exactly the referee's "pessimistic scenario."
**Tags:** ✅ verified · ◆ RH-conditional · ⬜ decisive-open.

---

## 1. Verified correct
- **Vertical $L^2$ bound (Step 8).** $\int|F(t+ib)|^2dt=\int|a(\xi)|^2e^{-2b\xi}d\xi$ (Plancherel). ✅ Rigorous.
  *Caveat:* for genuine $H^2(S_d)$ (not band-limited), the bound is $\le C\|F\|^2_{H^2(S_d)}$ via the strip
  weight $\cosh(2d\xi)$ ($|b|<d$), **not** $\le e^{2|b|\Lambda}\|F\|^2_{L^2}$ with a sharp $\Lambda$ — the
  "fixed bandwidth $\Lambda$" is a heuristic for the strip weight. The conclusion (bounded vertical
  amplification, $|b|<d$) holds.
- **Quadrature reformulation (Step 9).** RFB $\Leftarrow$ $\sum_\gamma|F(\gamma)|^2\asymp\rho\int|F|^2$, with
  $P=\rho\ell$ cancelling in the ratio $\widetilde{\mathfrak t}_-/\mathfrak t_+$. ✅ Correct and is the right
  object — statistical, $P$-free, immune to the Day-17 errors.
- **$S(T)=O(\log)$ is INSUFFICIENT (Step 10).** $\int g\,dS\overset{\text{IBP}}{=}-\int g'S$, $|{\le}|\,C\log T\!\int|g'|\le C\Lambda\log T\|F\|^2$,
  **same order** as the main term $\int g\rho\sim\log T\|F\|^2$. ✅ Correct — and an honest self-correction of
  the earlier "$S(T)$ suffices." The pointwise sup of $S$ does not beat the main term; **cancellation is
  required.**
- **Form-factor / pair-correlation route (Step 11).** $E(g)=\int\widehat g(\xi)\big(\widehat\mu(\xi)-\rho\delta_0\big)d\xi$;
  the fluctuation spectrum is the **GUE form factor** $\widehat R_2(\alpha)\sim|\alpha|$ ($|\alpha|<1$). For a
  band-fixed $g$ ($\widehat g$ in $[-2\Lambda,2\Lambda]$), in local units $\alpha=\xi/\rho\to0$, giving
  $\mathrm{Var}\,E(g)\lesssim\rho^{-1}\!\int|\xi||\widehat g|^2\lesssim(\Lambda/\rho)\|g\|^2$, so $E(g)=o(1)$.
  ✅ This is the standard RMT **number-variance suppression** — morally correct.

**No outright error found** in Steps 8–11 (contrast Day 17). The route is sound.

---

## 2. The decisive subtlety: reduction or reformulation? ◆
The quadrature law needs the **low-frequency form factor** $\widehat R_2(\alpha)\sim|\alpha|$ — i.e. a
**uniform $H^{-1/2}$-type discrepancy** bound on the zero-fluctuation measure $dS$, holding for **all**
band-fixed test functions. Two issues make this RH-conditional / frontier:
1. **Montgomery's pair-correlation theorem is conditional on RH** (and proven only for FT-support
   $(-1,1)$). The band-fixed regime sits at $\alpha\to0\subset(-1,1)$ — the *proven-under-RH* range — but
   still **assuming RH**. Using it to prove semiboundedness$\Rightarrow$RH would be **circular**.
2. **Unconditionally**, only $S(T)=O(\log T)$ and (Selberg) $\int_0^T S^2\ll T\log\log T$ are available; the
   latter gives the *typical* error but **not the uniform** ($\sup_F$) bound RFB needs — a single adversarial
   band-fixed $g$ correlating with $S$ is not excluded by a mean-square bound.

$$
\boxed{\ \text{The quadrature law} = \text{a uniform low-frequency discrepancy of the zeros} = \text{RH-conditional (Montgomery) or open.}\ }
$$
**Verdict:** most probably this is a **reformulation** — a *new equivalent of RH*:
$$
\text{RH}\ \Longleftrightarrow\ \text{the zeros are an asymptotically perfect band-fixed quadrature}\ \big(\sum_\gamma g(\gamma)=\rho\!\int g+o(\rho),\ \text{uniform, band-fixed }g\big),
$$
not an unconditional reduction. **This confirms the referee's own "pessimistic scenario."** It is still
valuable: a new face of RH in the **Montgomery/GUE lineage**, with the distinguishing feature that it
arose *forced* from the Weil-form/over-sampling analysis rather than posited.

**The one chance it is more than a reformulation** — the **decisive literature check**: is a *uniform*
(not just mean-square) low-frequency discrepancy bound for the zeros available **unconditionally** (e.g.
from Selberg's unconditional moment machinery, or Goldston–Montgomery-type equivalences)? If yes, the
quadrature route would be an unconditional *reduction* of B-2 to a known-unconditional input. If no
(only RH-conditional), it is a reformulation. **This is the single question that decides the program's
final status**, and it is concrete and checkable.

---

## 3. The durable meta-insight (endorsed)
Across Days 14–18 every **point-wise** control failed by the over-sampling factor $P\to\infty$
(Schur, Gram, Jaffard, interpolation), while every **statistical/average** control made $P$ cancel. That
asymmetry is a strong signal: **the correct object is statistical (quadrature/equidistribution), not local
(sampling/interpolation).** The Weil operator was a *machine that distilled this question*: the program's
content migrated from
$$
\text{“a spectral property of }\mathcal T\text{”}\quad\longrightarrow\quad\text{“an equidistribution/quadrature property of the zeros.”}
$$
This reformulation is the **most robust conceptual output of the entire Phase-4 sequence** — it survived
every audit that destroyed the others. The likely final shape, per the referee:
$$
\text{RH}\ \Longleftrightarrow\ \text{semiboundedness}\ \Longleftarrow\ \text{RFB}\ \Longleftarrow\ \text{band-fixed quadrature of the zeros},
$$
with the deepest step the last, and "quadrature $\approx$ RH" the honest expectation.

---

## 4. Net (Day 18)
The referee's quadrature reformulation **passes verification with no outright error** — a sharp contrast
with the Day-17 threads (two errors) and with most earlier "pillars." It correctly identifies that
**$P$ cancels under averaging**, reducing RFB to a **uniform low-frequency discrepancy / form-factor**
statement for the zeros. That statement is **RH-conditional (Montgomery) or at the unconditional frontier**,
so the most likely status is a **new equivalent of RH**, not a proof — the referee's pessimistic scenario,
which I concur is most probable. The **single decisive open question**: *is the needed uniform discrepancy
bound unconditional?* (Selberg moments vs Montgomery pair correlation.) The **durable gain** is conceptual
and real: the program's core is now a **statistical quadrature/equidistribution property of the zeros**,
the one formulation that survived every correction — a genuine, publishable reframing in the
Weil–Connes–de Branges–Montgomery lineage, independent of whether it ever yields an unconditional proof.

**Next (decisive):** the literature check — does an unconditional uniform low-frequency discrepancy bound
for $\{\gamma\}$ exist (Selberg/Goldston–Montgomery)? That single fact decides reduction vs reformulation.
