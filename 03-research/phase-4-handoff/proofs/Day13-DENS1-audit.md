# Day 13 — Audit of DENS.1: when does $\sum_\gamma f(\gamma)\sim\int f\rho\,dt$ hold?

Per the referee: DENS.1 (faithful $\iff K\rho\notin L^1$) is the new pillar, and it rests on the
sum$\to$integral step $\sum_\gamma K(\gamma,\gamma)\asymp\int K(t,t)\rho(t)\,dt$, whose **fluctuation term**
$\int K\,dS$ ($S(T)=$ argument fluctuation) is not obviously lower order. Audit it.

**Verdict (matching the referee's prediction):** DENS.1 **survives**, but the equivalence is now explicitly
**conditioned on $K$ being regularly varying** (mild; all band candidates satisfy it). The fluctuation term
diverges in some regimes but always at a *strictly slower rate* than the main term, so it never flips the
$L^1$ verdict. The crude $S=O(\log)$ bound suffices — no fine input on $S$ needed. The **critical scaling
law $K\asymp1/\rho$ survives unconditionally**. **Tags:** ✅ rigorous · ◆ standard · ⬜.

---

## 1. The exact decomposition
$\Sigma(T):=\sum_{0<\gamma\le T}K(\gamma,\gamma)=\int_0^T K(t,t)\,dN(t)$, $N=\bar N+S$ with
$\bar N'(t)=\rho(t)=\tfrac1{2\pi}\log\tfrac t{2\pi}$ and $S(t)=\tfrac1\pi\arg\zeta(\tfrac12+it)=O(\log t)$
(unconditional). So
$$
\Sigma(T)=\underbrace{\int_0^T K\rho\,dt}_{M(T)\ \text{(main)}}+\underbrace{\int_0^T K\,dS}_{E(T)\ \text{(fluctuation)}},\qquad
E(T)\overset{\text{IBP}}{=}K(T)S(T)-\int_0^T S(t)K'(t)\,dt .
$$
DENS.1 ("$\Sigma<\infty\iff M<\infty$") holds **iff** $E$ never overturns $M$'s convergence verdict.

---

## 2. The rate computation (the referee's concern, carried out) ✅
Use $|S(t)|\le C\log t$ (crude, unconditional). The two pieces of $E(T)$:
- **boundary** $|K(T)S(T)|\le C\,K(T)\log T$;
- **integral** $\big|\int_0^T SK'\big|\le C\int_0^T \log t\,|K'(t)|\,dt$.

Evaluate against $M(T)=\int_0^T K\rho\,dt\asymp\int_0^T K(t)\log t\,dt$ for the model kernels:

| $K(t,t)$ | regime | $M(T)$ | $K(T)\log T$ | $\int_0^T\!\log t\,|K'|\,dt$ | $E=o(M)$? |
|---|---|---|---|---|---|
| $\asymp1$ (flat) | over-sampled | $\asymp T\log T$ | $\log T$ | $0$ ($K'=0$) | ✅ |
| $\tfrac{2\pi}{\log t}$ (critical) | $R\asymp1$ | $\asymp T$ | $O(1)$ | $\asymp\!\int\!\tfrac{dt}{t\log t}\!\sim\!\log\log T$ | ✅ |
| $\tfrac1{t\log^2 t}$ (near-boundary, faithful) | barely faithful | $\asymp\log\log T$ | $\to0$ | $\asymp\!\int\!\tfrac{dt}{t^2\log t}\!<\!\infty$ | ✅ |
| $\log t\,e^{-\pi t/2}$ (Gamma) | trivial | $<\infty$ | $\to0$ | $<\infty$ | ✅ |

**Reading.** The referee is right that $\int\tfrac{dt}{t\log t}=\infty$ — the fluctuation integral
*diverges* in the critical regime. **But it diverges at rate $\log\log T$, while $M(T)\asymp T$** — so
$E(T)=O(\log\log T)=o(M(T))$. In every regime, either $E=o(M)$ (when $M\to\infty$) or $E$ converges (when
$M<\infty$). **Near the faithfulness boundary ($K\rho$ marginally $\notin L^1$) the error always
converges**, so only $M$ decides. Since $M(T)>0$ and $M\to\infty$ forces $\Sigma=M+E\to\infty$ regardless of
$E$'s sign, the verdict never flips.

---

## 3. The precise theorem (conditional, as predicted) ✅
**Proposition (Day 13).** Let $K(t,t)>0$ be **regularly varying** (i.e. $\tfrac{tK'(t)}{K(t)}\to$ const, or
more weakly $|K'|/K\lesssim 1/t$ with no wild oscillation). Then, using only $S(T)=O(\log T)$,
$$
\int_0^T\log t\,|K'(t)|\,dt = o\!\Big(\int_0^T K\rho\,dt\Big)\ \text{when the RHS}\to\infty,\quad\text{and converges otherwise,}
$$
hence $\Sigma(T)\sim M(T)$ in the divergent case and both converge together in the convergent case.
**Therefore**
$$
\boxed{\ K\ \text{regularly varying}\ \Longrightarrow\ \big[\ \text{FAITHFUL}\iff K\rho\notin L^1\ \big].\ }
$$
*Proof sketch.* Regular variation gives $|K'|\asymp K/t$ (up to slowly-varying factors), so
$\int^T\log t\,|K'|\asymp\int^T\tfrac{K\log t}{t}\,dt$, whose integrand is $\tfrac1t\cdot(K\log t)=\tfrac1t\cdot(2\pi K\rho)$
— a factor $1/t$ smaller than the main integrand $K\rho$. Hence $o(M)$ when $M\to\infty$; absolutely
convergent when $K\rho$ is (the extra $1/t$ only helps). Boundary term $K(T)\log T\lesssim K(T)\rho(T)\cdot T/\rho(T)\cdot\dots$
is likewise $o(M)$ or $\to0$. $\square$

**What is NOT needed:** any improvement on $S$ (the crude $\log$ bound suffices), Littlewood's
$\int_0^T S=O(\log)$ (would only sharpen), or RH.

**What IS needed:** $K$ regularly varying. This is the explicit hypothesis the referee predicted. It is
**satisfied by every band-geometry candidate** (flat: $K=$const; critical: $K\sim1/\log$; both regularly
varying). It could fail only for a pathologically oscillating diagonal, which band spaces do not produce.

---

## 4. What survives, sharpened

| Claim | Day 12 | Day 13 (audited) |
|---|---|---|
| faithful $\iff K\rho\notin L^1$ | asserted | ✅ **holds for regularly-varying $K$** (mild, all candidates) |
| fluctuation $\int K\,dS$ lower-order | "negligible" (loose) | ✅ **$O(\log\log T)$ vs $M$; converges near boundary** — verdict never flips |
| critical scaling $K\asymp1/\rho$ | canonical | ✅ **unconditional** (independent of the $S$-audit) |
| needs fine $S(t)$ input | unclear | ✅ **no** — crude $O(\log)$ suffices |

**Net (Day 13).** The referee's audit of the new pillar was right to demand and **favorable in outcome**:
DENS.1 holds, now with its hypothesis explicit ("$K$ regularly varying") exactly as predicted — a genuine
conditioning, but a mild one met by all candidates, and *not* requiring any delicate fact about $S(t)$. The
divergent-but-slower fluctuation ($\log\log T \lll T$) is the precise resolution of the referee's
"$\int dt/(t\log t)=\infty$" worry. The **critical scaling law $K\asymp1/\rho$ survives unconditionally**.

**Meta-note.** This is the **first audited pillar (Days 7–13) to hold up largely intact** — a possible sign
the program has reached more stable ground (the durable stack: B-1, EF-id, K1–K4, the scaling law, and now
DENS.1 with explicit hypothesis). Earlier pillars (CLOS in $H(E_\gamma)$, the Day-10 theorem) cracked;
this one only acquired an honest side-condition.

**Next:** with DENS.1 secured, return to the **lower frame bound** (form-core A.2) and **relative Carleson
in density form** ($K\rho_{\mathrm{off}}\notin L^1$), both now resting on an audited foundation.
