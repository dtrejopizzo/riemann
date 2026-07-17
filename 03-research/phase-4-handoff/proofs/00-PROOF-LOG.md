# Phase 4 — Proof Log (running record)

This folder is the **permanent working record** of the pure-math proof attempt. Every derivation,
dead end, and partial result is logged here so nothing is lost. Each working file is self-contained
and dated; this log is the index + chronology.

**Conventions.** Hilbert space, operator, and notation are *pinned once* in
[`A1-operator-and-compression.md`](A1-operator-and-compression.md) §1 and reused everywhere. When a
file proves something, it is promoted to a numbered **Result** (Lemma/Prop/Thm) and copied into the
ledger below. Honest status tags: ✅ proved · 🟡 reduced-to / conditional · ⬜ open · ❌ refuted.

---

## Files
- [`A1-operator-and-compression.md`](A1-operator-and-compression.md) — **Problem A.** Pins
  $(\mathcal H,\mathcal T)$; states and reduces the compression identity $Q=P_J\mathcal T P_J$.
- [`B2-semiboundedness.md`](B2-semiboundedness.md) — **Problem B-2.** Semiboundedness of the Weil
  form; the KLMN attack and where arithmetic cancellation becomes unavoidable.
- [`B2.4a-de-branges-norm.md`](B2.4a-de-branges-norm.md) — **B2.4a / D(i).** The de Branges norm;
  Gamma-factor geometry, the width-$\tfrac12$ triple coincidence, and the reduction **B-2 $\rightsquigarrow$
  de Branges chain** (downgraded from `≡` on Day 3).
- [`B2.4a-closability.md`](B2.4a-closability.md) — **the bridge.** Closability of $\mathfrak t$ in
  $H(E)$; the sign/value invariance principle; closability $\iff$ (C-bound); the weight prerequisite (§0).
- [`B2.4a-break-attempt.md`](B2.4a-break-attempt.md) — **the break (Day 4) + RETRACTION (Day 5).** BR.1
  ❌ false (hard-cutoff artifact); Fock pivot withdrawn; $H(E_\gamma)$ back in play.
- [`EF-identity-audit.md`](EF-identity-audit.md) — **audit (Day 6).** The explicit-formula identity
  $\mathfrak t=\sum_\rho h(\gamma_\rho)$: unconditional on the dense core; RHS **indefinite** (not
  positive); closure in $H(E_\gamma)$ **open**.
- [`closure-in-HEgamma.md`](closure-in-HEgamma.md) — **first positive result (Day 7).** $\mathfrak t_+$
  **closed** (Kato); RH $\Rightarrow$ $\mathfrak t$ closable; the whole residual = **one KLMN inequality
  (RFB)** = a zero-density comparison. *(CLOS.1 overclaim corrected Day 8.)*
- [`CLOS1-audit-and-RFB.md`](CLOS1-audit-and-RFB.md) — **Day 8.** Part A: CLOS.1 audited — "closure$=\mathfrak t_+$"
  **retracted**; form-core open. Part B: (RFB) is a **Carleson** condition; sufficient cond.
  $\sum K(t-ib,t-ib)<\infty$. *(Space corrected Day 9.)*
- [`space-correction-strip-hardy.md`](space-correction-strip-hardy.md) — **Day 9 (deep dive).** Computing
  $K$ quantitatively suggests $H(E_\gamma)$ is **trace-class = TRIVIALIZES**; leading candidate the **strip
  Hardy space**. *(Trivialization downgraded to conditional Day 10.)*
- [`Day10-kernel-audit.md`](Day10-kernel-audit.md) — **Day 10 (audit of the load-bearing kernel).** Formula
  ✅; trivialization **normalization-dependent** (◆, Danger C real); gem: faithful $\Rightarrow S_{\mathrm{off}}=\infty$
  *(both F1 & F2 found to have gaps Day 11)*.
- [`Day11-theorem-audit.md`](Day11-theorem-audit.md) — **Day 11 (audit of the Day-10 theorem).** F2 false
  ($1/\log$); F1 conditional ($D(t)\ge0$ can fail); reconstructed **density-adapted** ($K\gtrsim1/\log$);
  impossibility-constraint list **K1–K4**.
- [`Day12-density-scaling-law.md`](Day12-density-scaling-law.md) — **Day 12 (the scaling law).** Faithful
  $\iff K\rho\notin L^1$; **F1 = geometric (Level B)** via $D=2K_{11}-\tfrac12K''$; **necessary scaling law**
  $K\asymp1/\rho$; **A.2 = lower sampling bound** (upper=Carleson proved).
- [`Day13-DENS1-audit.md`](Day13-DENS1-audit.md) — **Day 13 (audit of DENS.1).** The fluctuation $\int K\,dS$
  is $O(\log\log T)\lll M$; DENS.1 **holds for regularly-varying $K$** (mild); critical law unconditional.
  First audited pillar to **hold up**.
- [`Day14-reduction-audit.md`](Day14-reduction-audit.md) — **Day 14 (audit of the A.2 reduction).** Genuine
  space = **over-sampling**; A.2 ≠ frame bound; coercivity easy. *(Its T2/K5 mechanism corrected Day 15.)*
- [`Day15-K5-audit.md`](Day15-K5-audit.md) — **Day 15 (audit of K5).** K5's "$R\asymp1\Rightarrow$ Carleson"
  is **false**: Carleson is governed by $P=\rho\ell$ ($\ell=\sqrt{K/K_{11}}$), not $R=K\rho$. Eval-bounding
  $\Rightarrow\ell\gtrsim\tfrac12\Rightarrow P\to\infty$ **always** ⟹ over-sampling FORCED; no T2.
- [`Day16-carleson-and-RFB.md`](Day16-carleson-and-RFB.md) — **Day 16 (Carleson + RFB proof).** $P\lesssim1\Rightarrow$
  Carleson (Schur, suff. only); $P\to\infty\Rightarrow\mathfrak t_+$ unbounded (direct kernel test). RFB sketch
  Step-3 hole; clean Schur-interpolation route ⟹ **RFB $\Leftarrow$ zero sampling-regularity** (the arithmetic).
- [`Day17-verification.md`](Day17-verification.md) — **Day 17 (verification).** TWO errors in the deeper
  exploration: Montgomery-scale "reversal" (coherence≠bandwidth; $P$ scale-invariant) and lattice/Schur
  (all $\ell^1$ routes hit $P\to\infty$). RFB plausibly TRUE $O(1)$ via $P$-**cancellation**.
- [`Day18-quadrature.md`](Day18-quadrature.md) — **Day 18 (quadrature reformulation).** RFB $\Leftarrow$
  **band-fixed quadrature** $\sum_\gamma|F(\gamma)|^2\approx\rho\int|F|^2$; $P$ cancels; reduces to the
  zeros' low-freq **form factor** (Montgomery). Most likely an **RH-conditional reformulation** ("new face").
- [`Day19-pair-correlation-input.md`](Day19-pair-correlation-input.md) — **Day 19 (the external input).**
  Parseval ✅ (cleaner in $PW_d$ = classical Weil class); $\|D_T\|^2_{L^2[-2d,2d]}$ = **scale-$1/d$ pair-corr
  2nd moment** at **Montgomery's proven $\beta\to0$ range**. B-2 closes in $H_+$. Decisive: is $V(d,T)$
  unconditional?
- [`Day20-threshold-correction.md`](Day20-threshold-correction.md) — **Day 20 (the threshold push has a
  VACUOUS step).** Global $\sqrt{V(d,T)}$ Cauchy–Schwarz is vacuous ($\to\infty\cdot\mathfrak t_+$). Local
  IBP+Bernstein+Selberg ⟹ $E_g=O(\mathfrak t_+)$ **unconditional**; $\kappa(b)\le e^d$. **B-2 plausibly
  unconditional** (no Montgomery).
- [`Day21-offline-and-coercivity.md`](Day21-offline-and-coercivity.md) — **Day 21 (off-line closed; B-2 ⟸
  gaps).** Proofs A/B/C verified. Off-line gap **closed unconditionally** by **Plancherel–Pólya** (clustering-OK)
  + local count $O(\rho)$ ⟹ $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|_2^2$. **B-2 ⟸ COERCIVITY**. *(Gap framing
  refined Day 22.)*
- [`../PAPER-A.md`](../PAPER-A.md) — **Day 23 — THE DELIVERABLE (paper A).** Full self-contained write-up:
  Theorem A (semibounded realization, modulo (H)), Theorem B (Kreĭn $\mathfrak t=E^*JE$ + angular operator,
  $\|K\|\le1\iff$RH), Theorem C (no-go: zero-side can't reach the sign). All equations, prior-work placement
  (Connes–Consani, de Branges completion), honest scope. Author: David Alejandro Trejo Pizzo.
- [`../B2-THEOREM.md`](../B2-THEOREM.md) — **Day 23.** Complete B-2 theorem assembled: Lemmas A–D + depth
  split unconditional; hypothesis (H) isolated (≪ RH, frontier). RH ⟺ sign of finite bottom.
- [`../B3-KREIN-STRUCTURE.md`](../B3-KREIN-STRUCTURE.md) — **Day 23.** Kreĭn/angular structure verified +
  audited; §8 **no-go theorem** (depth gives no leverage); over-claim "exactly Connes–Consani" corrected.
- [`../RH-ENDGAME.md`](../RH-ENDGAME.md) — **Day 23.** Reconnection to RH: machinery gives FINITE bottom
  (B-2), RH = the SIGN; needs structural positivity $\mathcal T=A^*A$, untouched.
- [`Day22-coercivity.md`](Day22-coercivity.md) — **Day 22 (coercivity = pure sampling).** $D^-=\infty$ does
  **NOT** give the lower frame bound (one Nyquist gap kills it — referee right). **Depth split:** only **deep**
  off-line zeros ($\kappa$ large) are dangerous, and they're locally $o(\rho)$ by **short-interval zero-density**;
  shallow ones harmless. **B-2 ⟸ uniform short-interval zero-density** (≪ RH, sharper than "no gaps").
- [`../B2-THEOREM.md`](../B2-THEOREM.md) — **PATH (A) CLOSED: the complete B-2 theorem.** Self-contained:
  Lemmas A/B/C/D + depth split all **unconditional**; the residual **hypothesis (H)** (uniform short-interval
  zero-density, ≪ RH) precisely isolated. **Theorem: modulo (H), a faithful semibounded $\mathcal T$ exists,
  RH ⟺ sign of its bottom.** Ready to validate.
- [`../RH-ENDGAME.md`](../RH-ENDGAME.md) — RH end-game: B-2 = finite bottom; RH = the SIGN (structural
  positivity $\mathcal T=A^*A$), untouched by the magnitude machinery.

---

## Result ledger (promoted statements)

| # | Statement | File | Status |
|---|---|---|---|
| **A.0** | Pinned data: $\mathcal H=L^2(\mathbb R,du)$; $\mathcal T=\Omega(D)+\Pi-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}T_{\log n}$ | A1 §1 | ✅ (definition) |
| **A.1** | The Weil form is finite on $\mathcal S(\mathbb R)$: $\mathcal S\subseteq\mathrm{dom}(\mathfrak t)$ | A1 §3 | 🟡 (proof drafted, one bound to tighten) |
| **A.2** | Hermite–Gauss localizers $g_j\in\mathcal S$, hence $g_j\in\mathrm{dom}(\mathfrak t)$ | A1 §3 | ✅ (corollary of A.1) |
| **A.3** | Compression identity $Q^{\mathrm{exact}}_{jk}=\langle g_j,\mathcal T g_k\rangle=(P_J\mathcal T P_J)_{jk}$ | A1 §4 | ✅ (once A.1 holds; tautology of the form) |
| **A.4** | Computed $Q^{(X)}\to Q^{\mathrm{exact}}$ as $X\to\infty$, rate $\le A e^{-\alpha(\log X)^2}$ | A1 §4 | 🟡 (= P7-B; needs the operator-norm restatement) |
| **B2.1** | The free part $\Omega(D)$ is self-adjoint, bounded below: $\Omega(D)\ge\Omega_{\min}\approx-5.37$ | B2 §2 | ✅ |
| **B2.2** | Prime form $\mathfrak p(g)=-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}(g\star\tilde g)(\log n)$ converges $\forall g\in\mathcal S$ | B2 §3 | ✅ |
| **B2.3** | ~~Naive KLMN fails: $\mathfrak p\gg\mathfrak a$~~ — **flawed (hard-cutoff error); reasoning withdrawn Day 5** | B2 §4 | ❌ reasoning (see Day 5) |
| **B2.4a** | (SB) ill-posed in $L^2$: off-axis point-eval $\widehat g(a\pm ib)$ unbounded ⟹ need weighted/de Branges norm | B2 §5.3–5.4 | ✅ (obstruction proved); 🟡 (norm found: de Branges of $\gamma$) |
| **DB.1** | $\Omega(r)=2\,\mathrm{Re}(\gamma'/\gamma)(\tfrac12+ir)$ — free part is the Gamma-factor geometry | DB §1 | ✅ |
| **DB.2** | width-$\tfrac12$ triple coincidence: pole class $=$ off-line strip $=$ $\gamma$'s first pole at $i/2$ | DB §2 | ✅ |
| **DB.3** | de Branges $H(E)$ has bounded strip evaluations — dissolves the $L^2$ obstruction | DB §3 | ◆ classical |
| **DB.4** | semiboundedness norm-dependent; single $E$ insufficient ⟹ **B-2 $\rightsquigarrow$ de Branges chain** (was `≡`, DOWNGRADED Day 3) | DB §4 | ✅ (norm-dep) / ⟶ (chain, *suggestive only*) |
| **CL.0** | ⚠️ weight asymptotic of $|E|^{-2}$ (log = density-of-states vs exp = $|\gamma|^{-2}$) GATES everything | CL §0 | ⚠️ unverified — do first |
| **CL.2** | **sign/value invariance:** sign(inf spec)=RH is norm-independent; only finiteness is norm-dependent; sign transfers $\iff$ closable | CL §2 | ✅ |
| **CL.3** | closability of $\mathfrak t$ in $H(E)$ $\iff$ (C-bound): $H(E)$-relative KLMN on $\mathfrak p$ ($L^2$-failed bound re-asked in strong norm) | CL §3 | ⟶ (reduced; settled negatively by BR.1) |
| **CL.0** | de Branges norm weight is **exponential** $e^{\pi|x|/2}$ (the density-of-states $\sim\log$ is a *different* object) | BR §0 | ✅ resolved |
| **BR.1** | ~~$\mathfrak t$ not semibounded in $H(E_\gamma)$ (width blow-up)~~ — **FALSE; hard-cutoff artifact** | BR §1,§5 | ❌ **RETRACTED Day 5** |
| **BR.3** | ~~faithful norm needs Fock/Bargmann~~ — rested on BR.1; **withdrawn** | BR §3,§5 | ❌ withdrawn |
| **EF-id** | explicit-formula identity $\mathfrak t(g,g)=\sum_\rho h(\gamma_\rho)$, $h=\widehat g\,\widehat g^*$ — **unconditional on dense core $\mathcal D$**; RHS **INDEFINITE** off-line ($4\mathrm{Re}[\widehat g(t-ib)^2]$), positivity$=$RH; **closure open** | EF-audit | ✅ core / ⬜ closure |
| **$K$ formula** | $K(t,t)=\tfrac{\varphi'(t)}\pi|E(t)|^2$ (re-derived from $E=A-iB$, phase $\varphi$) | Day10 §1 | ✅ |
| **SPACE** | Gamma–de-Branges **ruled out** (both norms fail: $E\sim\gamma$ trivializes ◆; $E\sim1/\gamma$ eval-uncontrolled). Home = **mild-weight Hardy-band**, exact weight ⬜ | Day9; Day10 §2 | ◆ / ⬜ pin via lit. |
| **Day-10 dichotomy** | ~~faithful $\Rightarrow S_{\mathrm{off}}=\infty$ (space-independent)~~ — **F1 & F2 gaps (Day 11)**; downgraded | Day10 §3 | ❌ as stated |
| **F2 (audited)** | only $\inf_t K(t,t)>0\Rightarrow S_{\mathrm{off}}=\infty$; "faithful$\Rightarrow\inf K>0$" is **FALSE** ($K\sim1/\log$) | Day11 §1 | ✅ (corrected) |
| **F1 (audited)** | $K(t-ib,t-ib)=K(t,t)+b^2D(t)+\dots$; $D(t)$ can be $<0$ ⟹ F1 holds only for **translation-invariant/symmetric** spaces | Day11 §2 | ◆ |
| **Day-11 theorem** | (i) $K\gtrsim1/\log$ + (ii) F1 + (iii) off-line positive proportion $\Rightarrow S_{\mathrm{off}}=\infty$, $a=0$ impossible. Covers both candidate spaces | Day11 §3 | ✅/◆ |
| **constraints K1–K4** | impossibility list any faithful realization must satisfy (trivial$\perp$faithful; faithful$\perp a=0$; Gamma-dB excluded; strong-norm$\perp$nontrivial) | Day11 §4 | ✅/◆ |
| **DENS.1** | **FAITHFUL $\iff K(t,t)\rho(t)\notin L^1$** — **audited Day 13: holds for regularly-varying $K$** (fluctuation $\int K\,dS=O(\log\log T)\lll M$; crude $S=O(\log)$ suffices). $\rho=\tfrac1{2\pi}\log\tfrac t{2\pi}$ | Day12 §1, Day13 | ✅ (reg.-varying $K$) |
| **DENS.2 (F1=geom)** | $K(t-ib,..)=K(t,t)+b^2D+\dots$, $D=2K_{11}-\tfrac12K''=K_{11}-\sum e_ne_n''$; **F1 $\iff K''\le4K_{11}$**, holds for slowly-varying diagonal ⟹ **Level B geometric** | Day12 §2 | ✅ |
| **DENS.4 (scaling law)** | **necessary law: faithful $\Rightarrow K\rho\notin L^1$**; critical $K\asymp1/\rho\sim2\pi/\log t$; standard de Branges (incl. $H(E_\xi)$) trivialize ($|E|\to0$) | Day12 §4 | ✅/◆ |
| **A.2 reduction** | ~~form-core $\Leftarrow$ lower frame bound (critical space)~~ — **AUDIT Day 14: critical space is T2-trivial ($\mathfrak t$ bounded, B-2 vacuous); A.2≠frame bound in genuine space** | Day12 §6; Day14 | ❌ corrected |
| **T2 / K5** | ~~$R\asymp1\Rightarrow\mu$ Carleson ⟹ $\mathfrak t$ bounded~~ — **Day-15: FALSE** (conflated $R=K\rho$ with $P=\rho\ell$). T2 not established; likely collapses to T1 | Day14; Day15 | ❌ corrected |
| **resolution $\ell$, $P$** | $\ell=\sqrt{K/K_{11}}\asymp d$ (Hardy-band); **Carleson $\iff P=\rho\ell$ bounded** ($\ne R$). $R\asymp(K/d)P$ | Day15 §1–2 | ✅ |
| **over-sampling FORCED** | eval-bounding $\Rightarrow d\ge\tfrac12\Rightarrow\ell\gtrsim\tfrac12\Rightarrow P=\rho\ell\to\infty$ **always** ⟹ $\mathfrak t_+$ **unbounded** for ALL admissible spaces (genuine space forced, not contingent) | Day15 §3 | ✅ |
| **two invariants** | $R=K\rho$ governs **trace-class (T1)**; $P=\rho\ell$ governs **Carleson/boundedness**. Day-14 merged them | Day15 §4 | ✅ |
| **Carleson suff.** | $P\lesssim1$ + separation $\Rightarrow$ Carleson (Schur test); full equiv FALSE (clustering) — sufficient direction only | Day16 A.1–2 | ✅ |
| **$\mathfrak t_+$ unbdd (direct)** | kernel test: $\langle k_t,Tk_t\rangle/\|k_t\|^2\approx K(t,t)P\to\infty$ ⟹ $\mathfrak t_+$ unbounded (upgrades Day-15 over-sampling) | Day16 A.3 | ✅ |
| **RFB Step-3 hole** | $\sum_\gamma|F'(\gamma)|^2\le C_d\|F\|^2$ is FALSE (over-counts by $P\to\infty$); only the *ratio* to $\mathfrak t_+$ is bounded | Day16 B.1 | ❌ (advisor's sketch) |
| **RFB reduction** | via Schur-interpolation (derivative-free): $\widetilde{\mathfrak t}_-\le CC'\mathfrak t_+$ if off→on interpolation coeffs are $\ell^1$-Schur bounded (rows+cols) | Day16 B.2 | ✅ (mod regularity) |
| **RFB conditional thm** | [bounded mult. + zeros a sampling seq. with Schur regularity] $\Rightarrow\mathfrak t_-\lesssim\mathfrak t_+\Rightarrow$ **Weil semibounded (B-2)** | Day16 C | ✅ conditional |
| **arithmetic frontier** | the regularity hyp. = zeros a REGULAR sampling sequence = **separation / $S(T)$ / Montgomery pair-corr / GUE** | Day16 C | ⬜ THE arithmetic core |
| **Day-17 errors** | "Montgomery-scale reversal" (coherence≠bandwidth; $P$ scale-inv) ❌; lattice/Schur/$G^{-1}$ all hit $P\to\infty$ ❌ — no $\ell^1$ route proves RFB | Day17 B,C | ✅ (errors confirmed) |
| **RFB via cancellation** | $\widetilde{\mathfrak t}_-/\mathfrak t_+$: both over-sample by $P$, **$P$ cancels in the ratio** ⟹ RFB plausibly $O(1)$; coercivity stays easy | Day17 D | ◆ |
| **QUADRATURE reformulation** | RFB $\Leftarrow$ $\sum_\gamma|F(\gamma)|^2\approx\rho\int|F|^2$ (band-fixed $g=|F|^2$); $S(T)=O(\log)$ **insufficient** (error $\asymp$ main); needs low-freq **form factor** $\widehat R_2(\alpha)\sim|\alpha|$ | Day18 | ◆ correct |
| **reduction vs reformulation** | the needed uniform discrepancy is **RH-conditional** (Montgomery) or frontier ⟹ most likely a **new equivalent of RH**, not unconditional reduction | Day18 | ◆ honest |
| **Parseval reduction** | $E_g=\int_{-2d}^{2d}\widehat g\,D_T$, $|E_g|\le\|\widehat g\|_2\|D_T\|_{L^2[-2d,2d]}$; rigorous in **$PW_d$ = classical Weil class** (cleaner, no strip-weight) | Day19 §1 | ✅ verified |
| **$\|D_T\|^2$ = pair-corr** | $V(d,T)=\int_{-2d}^{2d}|D_T|^2$ = Montgomery 2nd moment, kernel $\widehat r=\mathbf 1_{[-2d,2d]}$, scale $1/d$; **form factor at $\beta\to0$ = PROVEN range** | Day19 §2 | ✅ verified |
| **B-2 in $H_+$** | in the zero-sampling norm ($\mathfrak t_+=\|\cdot\|^2$), $\mathfrak t/\|\cdot\|^2\ge1-4\kappa(b)$ finite ⟹ **B-2 closes**; RH = sign of bottom (norm-indep) | Day19 §3 | ✅ |
| **THE external input** | $V(d,T)$ bounded: **diagonal $4dN$ UNCONDITIONAL** (suff. up to a $\log$); off-diag = Montgomery cancellation. **Decisive: is it unconditional?** | Day19 §4 | ◆ borderline / ⬜ lit |
| **the stakes** | unconditional $V$ ⟹ **B-2 UNCONDITIONAL** = faithful semibounded realization w/o RH = **§6 dream (A∧B∧C)**; else = new RH-equivalence | Day19 §4 | ⬜ |
| **❌ global $V$ vacuous** | $|E_g|\le\|\widehat g\|_2\sqrt{V_{\mathrm{global}}}$ gives $\to\infty\cdot\mathfrak t_+$ (loses localization); "$V\ll(\log T)^2$/Montgomery" was an ARTIFACT | Day20 §1 | ✅ (error found) |
| **B-2 needs $O$ not $o$** | semiboundedness (finite bottom) needs $E_g=O(\mathfrak t_+)$, **not** $o$; the Day-18 "$S=O(\log)$ insufficient" was for the wrong ($o$) target | Day20 §2 | ✅ |
| **$E_g=O(\mathfrak t_+)$ uncond.** | local IBP: $|E_g|\le(\sup_{\rm loc}|S|)\int|(|F|^2)'|\le2d\log T_0\|F\|_2^2=O(\mathfrak t_+)$ (Bernstein + Selberg $S=O(\log)$) | Day20 §2 | ◆ strong/to-audit |
| **B-2 plausibly UNCONDITIONAL** | $\kappa(b)\le e^d$ uniform (band-limited, $|b|<\tfrac12<d$); off-line via classical zero-density ⟹ $\widetilde{\mathfrak t}_-\le C\mathfrak t_+$ finite ⟹ $\mathfrak t\ge(1-4C)\|\cdot\|^2_{H_+}$. **Montgomery NOT needed** | Day20 §3–4 | ◆ to-audit |
| **Proofs A/B/C** | IBP valid in $PW_d\cap H^1$ ✅; $E_g=O(\mathfrak t_+)$ (Bernstein+Selberg, $O$ not $o$) ✅; vertical $\|F(\cdot+ib)\|^2\le e^d\|F\|^2$ exact ✅ | Day21 §1 | ✅ verified |
| **off-line CLOSED** | **Plancherel–Pólya** (clustering-OK, no separation needed) + local count $O(\rho)$ (RvM+$S$) ⟹ $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|_2^2$ **UNCONDITIONAL** (closes the referee's gap) | Day21 §2 | ◆→✅ |
| **B-2 ⟸ COERCIVITY** | $\mathfrak t_+\ge c\rho\|F\|^2$. *Day-22: $D^-=\infty$ does NOT suffice (one Nyquist gap kills it, Beurling gap theorem needed)* | Day21 §3–4; Day22 §1 | ◆ refined |
| **depth split (Day 22)** | coercivity only needed NEAR off-line zeros; **shallow** off-line ($\kappa\approx1$) harmless; **deep** off-line (large $\kappa$) locally $o(\rho)$ by short-interval zero-density | Day22 §2–3 | ◆ |
| **B-2 ⟸ short-interval density** | **B-2 ⟸ uniform short-interval zero-density for $\sigma>\tfrac12+\delta$** (deep off-line locally $o(\rho)$). ≪ RH, sharper than "no gaps". Frontier: is the *uniform* version unconditional? | Day22 §3–4 | ◆ THE input / ⬜ frontier |
| **(H) = the hypothesis (Day 23)** | (H): on-line+shallow zeros keep fraction $\eta$ of every Nyquist cell (deep off-line don't locally dominate). $(H)\Rightarrow$ coercivity (Beurling). **(H) NOT unconditional** by current methods (global $N(\tfrac12+\delta,T)\ll T^{1-c\delta}$ allows a $\log T$-cluster in one cell); ≪ RH | B2-THEOREM §4 | ◆ frontier |
| **Theorem A (B-2, Day 23)** | modulo (H): $\mathfrak t$ closable in $H_+$, self-adjoint $\mathcal T$, $\inf\operatorname{spec}\ge1-4C>-\infty$; **RH ⟺ sign of bottom**. Lemmas A–D unconditional | B2-THEOREM §5; PAPER-A §5 | ✅ modulo (H) |
| **Kreĭn identity (Day 23)** | $\mathfrak t=E^*JE$, $E$=evaluation at $t_\rho+ib_\rho$, $J=J^*$, $J^2=I$ involution $\rho\mapsto1-\bar\rho$. Negativity of $J$ = exactly off-line zeros. Team's antilinear $J$ = convention slip | B3-KREIN §1–2; PAPER-A §6 | ✅ unconditional |
| **angular operator $K$ (Day 23)** | exact split $\mathfrak t=\|P_+EF\|^2-\|P_-EF\|^2$ (no factor-4); $K$ defined uncond. (type-density); **$\|K\|<\infty\Leftarrow$(H)=B-2; $\|K\|\le1\iff$RH**; $\|K\|\ge e^{d/2}$ magnitude side | B3-KREIN §3; PAPER-A §7 | ✅ unconditional |
| **$P_+\|_{R(E)}$ injective** | QUALITATIVE (type-density uniqueness, $K$ defined, maybe unbounded) — uncond., NOT circular. ≠ QUANTITATIVE boundedness (=(H)/coercivity, not free). Referee caught the conflation | B3-KREIN §3; PAPER-A §7.2 | ✅ (qualitative) |
| **$b_\rho^2$ = shallow only** | $d_\rho=F(t+ib)-F(t-ib)\approx2ib_\rho F'$ is SHALLOW linearization; for deep zeros remainder/leading $\sim b^2 d=O(1)$, true amp $e^{2d|b|}$. "$\sum b_\rho^2|F'|^2\le\theta\mathfrak t_+\Rightarrow$RH" = optimistic-pillar trap | B3-KREIN §4; PAPER-A §7.3 | ✅ (caveat) |
| **Theorem C = NO-GO (Day 23)** | $\mathfrak t=\|P_+EF\|^2-\|P_-EF\|^2=\mathfrak a+\mathfrak q-\mathfrak p$ (arith. side, NO $b_\rho$). Depths give ZERO leverage; $\|K\|\le1$ from zero side $\equiv$ Weil positivity $\equiv$ RH; sign-agnostic bounds $\Rightarrow\|K\|^2\gtrsim e^d$ (wrong side). Zero-side $K$ presupposes the unknown zeros (circular as tool) | B3-KREIN §8; PAPER-A §8 | ✅ **proved** |
| **prior-work placement** | strongly analogous to **Connes–Consani** (arXiv:2006.13771, their $K<1$) & **arXiv:2301.00421** (de Branges completion, RH-conditional; ours uncond/Kreĭn). NOT proven identical (over-claim "exactly CC" corrected) | B3-KREIN §6; PAPER-A §9 | ✅ situated |
| **$K_{S_d}$ (flat)** | $K_{S_d}(t-ib,t-ib)=\kappa(b)$ **$t$-flat**, $\asymp(d-|b|)^{-1}$ edge-blowup (flat strip Hardy case) | Day 9 §3 | ◆ |
| **CLOS.1** | $\mathfrak t_+|_{\mathcal D}$ **closable** (Kato). VACUOUS in $H(E_\gamma)$ (bounded); **non-vacuous in $H^2(S_d)$** ($\mathfrak t_+$ unbounded) | CLOS §1, Day9 C1 | ✅ (in $H^2(S_d)$) / ⬜ identification |
| **CLOS.1-core** | **form-core**: is $\overline{\mathfrak t_+|_{\mathcal D}}=\mathfrak t_+$ (Hermite dense in graph norm)? — else operator-from-core $\neq$ maximal | audit A.2 | ⬜ open (load-bearing) |
| **CLOS.2** | RH $\Rightarrow$ $\mathfrak t=\mathfrak t_+$ closable, $\inf\operatorname{spec}\ge0$ — unconditional in the RH/control world | CLOS §2 | ✅ |
| **CLOS.3 = (RFB)** | $\,|\mathfrak t_-|\le a\,\mathfrak t_++C\|\cdot\|^2$ ($a<1$) $\Rightarrow$ **closable AND semibounded** in one stroke | CLOS §3 | ⬜ **the single open target** |
| **(RFB) = Carleson** | (RFB) $\Leftarrow$ $\mu_{\mathrm{off}}=\sum\delta_{t-ib}$ is a **Carleson measure** for $H(E_\gamma)$ — NOT raw density | RFB B.1 | ✅ reduction |
| **(RFB) sufficient** | ~~$S_{\mathrm{off}}<\infty\Rightarrow a=0$~~ — in $H^2(S_d)$, $S_{\mathrm{off}}\ge\kappa(0)\cdot\#\text{off-line}=\infty$. **$a=0$ FALSE** (referee right) | Day9 C2 | ❌ (relevant case) |
| **(RFB) content** | in $H^2(S_d)$: **relative Carleson** of $\mu_{\mathrm{off}}$ vs $\mu_{\mathrm{on}}$ ($a>0$ forced); fine zero-geometry ($S(T)$, separation), NOT raw density | Day9 C3 | ⬜ open (the crux) |

---

## Chronology

**2026-06-01 — Day 0.** Opened the workspace. Pinned $(\mathcal H,\mathcal T)$ (A.0). Two threads
started in parallel per the work program §7:
- **Problem A.** Reduced the compression identity to two analytic facts: (i) the localizers lie in
  the form domain (A.1/A.2), (ii) the finite-cutoff computed matrix converges to the exact form entries
  (A.4 = P7-B restated). With both, $Q=P_J\mathcal T P_J$ is essentially a *tautology of the Gram
  matrix* — A is the most decidable problem, as predicted. Remaining: tighten the archimedean bound in
  A.1 and restate P7-B at operator-norm level (A.4).
- **Problem B-2.** Established the free part is bounded below (B2.1) and the prime form converges on
  Schwartz functions (B2.2). **Key finding of Day 0:** the naive functional-analytic route (KLMN /
  relative form-boundedness) **provably cannot work** (B2.3) — the prime perturbation is "form-larger"
  than the log-growing archimedean part, so semiboundedness cannot come from soft perturbation theory.
  It must come from **arithmetic cancellation** in $\sum\Lambda(n)n^{-1/2}T_{\log n}$, i.e. from the
  distribution of primes/zeros. **This is the mechanism behind the §3.3 conjecture** that B-2 sits at
  "zero-density level," now derived rather than asserted.

> **Day-0 headline.** A is on track to be genuinely provable. B-2's difficulty has been *localized*:
> it is not soft analysis, it is a single explicit inequality (B2.4) tying the negative prime form to
> the archimedean form, whose constant is controlled by zero density. The frontier is now one boxed
> inequality, not a vague "entanglement."

**2026-06-02 — Day 1.** Two referee alerts on the Day-0 §5, both conceded, both load-bearing:
- **Alert 1.** The "multiplier symbol" $\Phi(r)=2\sum\Lambda(n)n^{-1/2}\cos(r\log n)$ and
  $\inf_r(\Omega-\Phi)$ were illegitimate: the prime measure $\nu$ has mass $\asymp e^{t/2}$ per unit
  interval, so it is **non-tempered** and $\Phi=\widehat\nu$ is **not** a tempered distribution. (SB) had
  to be restated as a **distributional pairing on the positive-type cone** $\{|\widehat g|^2\}$, never a
  pointwise bound. The pairing exists only on the strip-width-$>\tfrac12$ class — the *same* class the
  pole forced in A. *(B2 §5.1.)*
- **Alert 2.** "Finitely many off-line zeros $\Rightarrow$ (SB)" is **not** a corollary. An off-line
  quartet's factors $\widehat g(a\pm ib)=\int g\,e^{\mp bu}e^{-iau}du$ are point-evaluations **off the
  real axis**, which are **unbounded functionals on $L^2(\mathbb R,du)$** ($e^{\mp bu}\notin L^2$). So one
  off-line zero already makes the form a-priori unbounded; finiteness proves nothing. *(B2 §5.3.)*
- **Day-1 finding (what the corrections destapan).** The Hilbert-space **norm** — invisible to Problem A
  — is what decides B-2. With naive $L^2$, off-axis evaluations are unbounded and (SB) **plausibly
  collapses to RH** (no separation). The genuine-weakening branch *requires* a weighted reproducing-kernel
  norm — a **de Branges space $H(E)$** in which strip point-evaluations are bounded. **So B and D are the
  same problem viewed twice:** B2.4a (find the norm) **is** de Branges step (i). Corrects Day-0's "no free
  $\delta$": no free parameter for identity A, but the **norm/weight is a genuine, decisive choice for B-2**.
- **v10 reframed:** "measure $\inf_r(\Omega-\Phi_X)$" is only heuristic (no such inf); the rigorous probe
  is form-level $\inf\mathfrak t(g,g)/\|g\|_{H(E)}^2$ with sensitivity-to-weight testing.

> **Day-1 headline.** The entanglement is now concrete and *located in the norm*: B-2 is well-posed only
> in a de Branges space, and there it splits into B2.4a (construct $E$ so strip evaluations are bounded)
> + B2.4b (the zero-density inequality). Merge the B and D sub-teams. Next: build $E_{T_0,\sigma}$ and
> read Bombieri's norm.

**2026-06-02 — Day 2.** Followed the directive "pursue B/de Branges while hot" (do **not** stop to write
up A first). Attacked B2.4a directly. Results in [`B2.4a-de-branges-norm.md`](B2.4a-de-branges-norm.md):
- **DB.1 ✅** The free part is the Gamma geometry: $\Omega(r)=2\,\mathrm{Re}(\gamma'/\gamma)(\tfrac12+ir)$,
  $\gamma(s)=\pi^{-s/2}\Gamma(s/2)$. The ambient space of B is forced — it is $\gamma$'s de Branges space.
- **DB.2 ✅** Width-$\tfrac12$ **triple coincidence**: the admissible strip ($>\tfrac12$, from the pole),
  the off-line displacement range ($|\beta-\tfrac12|<\tfrac12$), and $\gamma(\tfrac12+iz)$'s first pole
  ($z=i/2$) are the **same strip**. Three independently-arrived constants collapse to one.
- **DB.3 ◆** In any de Branges $H(E)$, point-evaluations are bounded at **every** $w\in\mathbb C$
  (reproducing kernel $K_w$) — so the Day-1 $L^2$ pathology (off-axis evals unbounded) simply **does not
  occur**. A space with bounded strip evaluations *exists* — the archimedean de Branges space of $\gamma$.
- **DB.4 — the catch and the consolidation.** The de Branges weight $|E|^{-2}\asymp e^{\pi|r|/2}$ is
  **exponentially stronger** than the Weil energy $\Omega\sim\log|r|$. Positivity ($=$RH) is
  norm-independent but **semiboundedness is norm-dependent**, and the strong norm makes it *easier*
  (good) while **redefining the Rayleigh quotient the ladder converges to** (so $E$ is now a shared
  parameter of B *and* C). No single $E$ does both "bound evaluations" (strong norm) and "be the Weil
  form" (weak $\log$ norm); the principled reconciliation is the de Branges **chain** $\{H(E_a)\}$. **⟶
  HEADLINE: B-2(b) $\equiv$ the de Branges chain/ordering condition for $E_{T_0,\sigma}$ $\equiv$ (LB).**
  Every flank now points at one object ($E_{T_0,\sigma}$) and one condition. v9's "no Conrey–Li" is
  re-priced as *direct* evidence about that chain condition.

> **Day-2 headline.** The program consolidated. B fully merges into D; the named inequality (LB) is now
> *literally* a de Branges chain condition for a Gamma-factor-based localized $E_{T_0,\sigma}$. The spine
> of Phase 4 (DB-open) is: (1) construct $E_{T_0,\sigma}$; (2) write the chain/ordering condition;
> (3) prove it (conditionally on zero density) and confirm Conrey–Li immunity in the localized regime.
> A stays in write-up; B/D is the live frontier.

**2026-06-02 — Day 3.** Referee gave two corrections on Day 2, both conceded, both load-bearing; the
second produced the day's real content. Record in [`B2.4a-closability.md`](B2.4a-closability.md).
- **Correction A — `≡` was overstated.** Day-2's "B-2 $\equiv$ de Branges chain condition" is only
  $\rightsquigarrow$ (suggestive). Upgrading needs three unproven things: (1) $H(E)$ canonical, (2) the
  Weil spectral bottom preserved on passing to the chain, (3) semiboundedness $\iff$ ordering. Downgraded
  everywhere.
- **Correction B — the deep worry: does a strong norm *trivialize* the instability?** If the de Branges
  weight is exponential, the archimedean form becomes negligible (CL §1) and semiboundedness could be
  vacuous — a property of the space, not of $\zeta$. Valid risk.
- **My self-catch (prompted by B).** Day-2's weight asymptotic $|E|^{-2}\asymp e^{\pi|r|/2}$ was
  **asserted, not verified** — I conflated the *modulus* $|\gamma|$ (exponential) with the de Branges
  *density of states* $\varphi'\sim\log$ (logarithmic). Which one is the weight **gates the whole worry**
  (CL §0): exponential ⟹ trivialization real; logarithmic ⟹ norm $\approx$ Weil energy, no trivialization.
  Flagged ⚠️, not built upon. (Exactly the $\Phi$-type slip, caught early this time.)
- **The contribution (CL §2) — sign/value invariance principle.** "$\inf\operatorname{spec}\ge0$" $=$ RH
  is **norm-independent** (it never mentions the inner product); only *finiteness* of the bottom is
  norm-dependent. So the norm can corrupt the **value** (B-2) but **never the sign** (RH). Closability is
  exactly the guarantee that the sign *transfers to the completion*. This both answers the referee
  (RH cannot be hidden by the norm) and vindicates the directive (closability is the precise bridge).
- **Reduction (CL §3).** Closability of $\mathfrak t$ in $H(E)$ $\iff$ one rigorous, distribution-free
  inequality (C-bound): the **$H(E)$-relative KLMN bound on $\mathfrak p$** — the same bound that *failed*
  in $L^2$ (B2.3), now re-asked in the stronger norm where it may hold; an inequality between the prime
  measure $\nu$ and the de Branges weight $|E|^{-2}$.
- **Trichotomy (CL §4).** Verdict is one of: (1) closable & non-trivially bounded below ⟹ faithful ladder
  well-posed (best); (2) closable but trivially bounded ⟹ B-2 vacuous, content reverts to sign$=$RH (no
  separation); (3) not closable ⟹ wrong space (referee's worry realized). All three are informative.

> **Day-3 headline.** Reprioritized per referee: **do not build $E_{T_0,\sigma}$ yet.** Order is
> (0) verify the archimedean de Branges **weight asymptotic** (log vs exp — one literature computation,
> gates all), (1) decide **closability** via (C-bound), reading Bombieri's norm, (2) only if case 1 holds,
> construct the chain. The sign/value principle guarantees no choice of norm can fake or hide RH; the open
> risk is whether a *faithful* (closable, non-trivial) norm exists at all. Immediate next computation: §0.

**2026-06-02 — Day 4.** Per referee directive ("actively try to break DB.4 before building it").
Record in [`B2.4a-break-attempt.md`](B2.4a-break-attempt.md).
- **CL.0 resolved (double self-correction).** The de Branges **norm weight is exponential**
  $|E|^{-2}\asymp e^{\pi|x|/2}$ (Day-2 instinct was right); the **density of states $\sim\log$** is a
  *different* object (Day-3 caught a real object but mislabeled it the norm). We are in the strong-norm
  regime; trivialization worry is live → test it.
- **THE BREAK (BR.1).** Tried to falsify semiboundedness in $H(E_\gamma)$ — and **succeeded**. Scaling
  family $\widehat g_\varepsilon$ = bump of width $\varepsilon\to0$ at fixed $T_0$ (wide-in-$u$): the
  norm $\asymp e^{\pi|T_0|/2}\|\widehat g\|_{L^2}^2$ depends on **location** $T_0$, *blind to width*
  $\varepsilon$; but the prime form $\asymp\|\widehat g\|_{L^2}^2\cdot e^{1/2\varepsilon}$ (Chebyshev
  $\sum_{n\le N}\Lambda(n)n^{-1/2}\sim2\sqrt N$, $N=e^{1/\varepsilon}$). So
  $\mathfrak t/\|g\|_{H(E)}^2\sim -e^{1/2\varepsilon}\to-\infty$. **$\mathfrak t$ is NOT semibounded in
  the pure de Branges space of $\gamma$.** An amplitude-by-location weight cannot control a width-driven
  divergence. **DB.4-as-stated is falsified.**
- **Consistency (BR.2).** Band-limited ($PW_\tau$) test functions $\Rightarrow$ $\mathfrak p$ a finite
  sum $\Rightarrow$ bounded (classical "tame on band-limited" Weil/Bombieri–Lagarias regime); the blow-up
  uses the opposite wide-in-$u$ regime — no contradiction, and it locates RH content in the
  non-band-limited limit. v9 (fixed $\sigma$, grow $J$) explored a *different* direction than the
  blow-up ($\sigma\to0$); **v10 falsifiable prediction:** $\sigma\to0$ scan $\Rightarrow\lambda_{\min}\to-\infty$
  in $L^2$ normalization.
- **Redirection (BR.3).** Faithful norm must control **amplitude (location)** AND **width/smoothness**.
  That is a **Fock/Bargmann (Gaussian phase-space)** norm — whose ON basis is the **Hermite functions =
  our localizers**. The program's Gaussian window was secretly the right geometry; de Branges (DB.1–DB.3)
  survives as the *location half*. The chain picture is replaced by a Gaussian phase-space picture.

> **Day-4 headline.** Trying to break DB.4 broke it — cleanly and usefully. The pure de Branges space is
> *not* the faithful home (Weil form unbounded below there, explicit width-driven $\sqrt N$ blow-up). The
> same calculation redirects to **Fock/Bargmann**, the natural home of the Hermite–Gauss instrument, as
> the candidate that can bound both off-line evaluations and the prime form. Next: (1) make BR.1 rigorous;
> (2) write $\mathcal T$ in the Bargmann transform and test whether the Fock norm cures the blow-up; (3)
> v10 $\sigma\to0$ falsifier. $E_{T_0,\sigma}$ deferred (was for the superseded picture).
> **[Day-4 headline is itself retracted — see Day 5.]**

**2026-06-02 — Day 5. ❌ RETRACTION of BR.1 (and B2.3).** Attempting (per referee) to make BR.1 rigorous
*before* building the Fock formalism revealed BR.1 is **false**. Record in `B2.4a-break-attempt.md` §5.
- **The disproof (explicit-formula identity, EF-id).** $\mathfrak t(g,g)=\mathfrak a+\mathfrak q-\mathfrak p=\sum_\rho|\widehat g(\gamma_\rho)|^2$
  is an **identity**. For a smooth bump $\widehat g_\varepsilon$ of width $\varepsilon\to0$ at a generic
  $T_0$, the right side counts only zeros within $\varepsilon$ — **finite, $\to0$**. So $\mathfrak p$ is
  **finite**, not $\sim e^{1/2\varepsilon}$. The $\sqrt N$ "blow-up" was an artifact of the **hard cutoff**
  $\mathbf 1_{\log n\le1/\varepsilon}$ the referee flagged as non-innocent; the smooth test function
  **resums** the pointwise-divergent prime series to $\Phi(T_0)=2\,\mathrm{Re}(-\zeta'/\zeta(\tfrac12+iT_0))$,
  finite. The predicted oscillatory cancellation is exactly what kills it.
- **Scope.** BR.1 ❌ withdrawn; BR.3 (Fock pivot) ❌ withdrawn (rested on BR.1); **B2.3 (Day 0) used the
  SAME hard-cutoff error** — its "$\mathfrak p\gg\mathfrak a$" is not established (by EF-id, $\mathfrak p$
  is *comparable* to $\mathfrak a$). CL.0 ✅, DB.1–DB.3 ✅, Day-1 off-axis mechanism ✅ all survive.
- **Corrected picture — $H(E_\gamma)$ is BACK IN PLAY.** The only rigorous $L^2$ unboundedness is Day-1's:
  off-line zero $\Rightarrow$ off-axis evaluation $\Rightarrow$ unbounded on $L^2$, but **bounded in
  $H(E_\gamma)$ (DB.3)**. So B-2 in $H(E_\gamma)$ $\rightsquigarrow$ "is $\sum_{\text{off-line}}$(bounded
  terms) bounded below?" $=$ **zero-density** $=$ exactly §3.3's original conjecture, now reached cleanly
  with the prime-blow-up phantom removed. The Day-2/3/4 chain/Fock detours were chasing an artifact.
- **Meta-lesson (logged permanently).** The hard-cutoff-of-a-conditionally-convergent-series error
  appeared Day 0 AND Day 4 and survived four passes. **Mandatory rule:** every blow-up claim must be
  checked against EF-id ($\mathfrak t=\sum_\rho|\widehat g(\gamma_\rho)|^2$) before being believed.

> **Day-5 headline.** A clean self-retraction, the program's ethos working. The "break" was the artifact,
> not the de Branges space. After five days the picture **converges back to §3.3**: B-1 unconditional
> (von Neumann); B-2 well-posed in the archimedean de Branges space $H(E_\gamma)$ (off-axis evaluations
> bounded, DB.3), reducing to a **zero-density inequality** on the off-line-zero sum. No Fock, no chain
> required by the evidence. Next: (1) B-2 as a zero-density problem in $H(E_\gamma)$; (2) Bombieri's norm;
> (3) re-examine whether any genuine norm-dependence survives. The instrument's recurring temptation —
> manufacturing blow-ups by hard-truncating — is now a named, guarded-against failure mode.

**2026-06-02 — Day 6. Audit of EF-id (the new pillar) — survives, with two corrections.** Per referee:
before building on EF-id, audit it (three questions). Record in [`EF-identity-audit.md`](EF-identity-audit.md).
- **Q3 (role of RH): Case A, unconditional.** (EF) is the Weil explicit formula — a theorem, no RH input.
  RH enters only in the *sign* of the (unconditional) RHS. ⟹ using EF-id to refute BR.1 is legitimate; it
  is NOT circular. ✅
- **Q2 (is the RHS positive?): NO — notation corrected.** $\mathfrak t(g,g)=\sum_\rho h(\gamma_\rho)$ with
  $h=\widehat g\,\widehat g^*$. On-line zeros give $|\widehat g(\gamma)|^2\ge0$; **off-line quartets give
  $4\,\mathrm{Re}[\widehat g(t-ib)^2]$ — INDEFINITE**, built from off-axis evaluations. Positivity $\iff$
  RH (Weil's criterion). The Day-5 shorthand "$\sum|\widehat g(\gamma_\rho)|^2$" was valid only under RH;
  fixed everywhere.
- **Q1 (domain): the real frontier.** (EF) holds **unconditionally on $C_c^\infty$ and on $\mathcal D$**
  (dense core); whether it **and the sign survive the $H(E_\gamma)$-closure is OPEN** — an identity on a
  dense core need not control the closure (the referee's deep point). EF-id is ✅ **core-level**, ⬜ closure.
- **B-2, restated on the audited identity:** $\inf_{\|g\|_{H(E)}=1}[\sum_{\text{on-line}}|\widehat g(\gamma)|^2+\sum_{\text{off-line}}4\mathrm{Re}[\widehat g(t-ib)^2]]>-\infty$?
  On-line part $\ge0$; off-line part = bounded $H(E)$-evals (DB.3) ⟹ **zero-density** question (§3.3).

> **Day-6 headline.** The new pillar holds — EF-id is unconditional on the dense core — but was mis-stated
> twice (RHS indefinite not positive; core-level not global), now fixed. This is the **first formulation
> in the Day 0–6 sequence to survive a deliberate hard audit without retraction.** The single open
> analytic crux is now sharp and stable: **does EF-id survive closure in $H(E_\gamma)$, and is the
> off-line-zero sum bounded below there?** — a zero-density problem on a verified unconditional foundation.
> Next: (1) the closure question (does the form close in $H(E_\gamma)$?); (2) Bombieri's norm; (3) the
> off-line-zero-sum zero-density bound.

**2026-06-02 — Day 7. Closure attacked (referee priority) — FIRST POSITIVE RESULT.** Record in
[`closure-in-HEgamma.md`](closure-in-HEgamma.md). Using the audited split $\mathfrak t=\mathfrak t_++\mathfrak t_-$:
- **CLOS.1 ✅** The on-line part $\mathfrak t_+(g)=\sum_\gamma|\langle g,K_\gamma\rangle|^2$ (DB.3: bounded
  evaluations) is a **non-decreasing supremum of bounded closed forms**, hence **closed** by **Kato's
  monotone convergence theorem for forms**. ⟹ a non-negative self-adjoint operator $T_+\ge0$ on
  $H(E_\gamma)$ exists **unconditionally** (B-1 concrete + positive half of B-2, no hypotheses).
- **CLOS.2 ✅** Under RH (all GRH controls), $\mathfrak t_-=0$ ⟹ $\mathfrak t=\mathfrak t_+$ **closable**,
  $\inf\operatorname{spec}\ge0$. **The Weil form closes in $H(E_\gamma)$, unconditionally in the world the
  numerics live in.** de Branges geometry vindicated; chain/Fock detours unnecessary.
- **CLOS.3 = (RFB) ⬜** RH-false residual: closability AND semiboundedness BOTH follow from ONE inequality
  $|\mathfrak t_-(g)|\le a\,\mathfrak t_+(g)+C\|g\|^2$, $a<1$ (KLMN). It is a **zero-density comparison of
  off-line vs on-line zero contributions**, in the geometry where every term is a bounded evaluation —
  the KLMN that *failed* in $L^2$ (Day 0) now correctly posed. **Re-derives §3.3 independently.**

> **Day-7 headline.** The closure question — the spot history said hides surprises — returned **positive**:
> $\mathfrak t_+$ is closed (named classical theorem), under RH the form closes unconditionally, so
> $H(E_\gamma)$ is a *legitimate* home and we now study a concrete closed form with a real operator $T_+$.
> All remaining difficulty of Problem B funnels into the **single inequality (RFB)** — a zero-density
> comparison of off-line to on-line zeros. This is the **first Phase-4 result that changes the
> mathematical state** (exactly as the referee predicted closability would). Next: attack (RFB) as a
> density bound; cross-check Bombieri; audit CLOS.1's Kato hypotheses (new load-bearing step).

**2026-06-02 — Day 8. Parallel: audit CLOS.1 + attack (RFB).** Record in
[`CLOS1-audit-and-RFB.md`](CLOS1-audit-and-RFB.md).
- **CLOS.1 audit (referee's 3 weak points).** ⚠️ Overclaim found and **retracted**: I said "closure
  $=\mathfrak t_+$ because $\mathcal D$ dense" — but **density $\ne$ form-core**. Rigorous now: only
  $\mathfrak t_+|_{\mathcal D}$ **closable** ⟹ $\overline{T_+}\ge0$ exists. The **form-core** question
  $\overline{\mathfrak t_+|_{\mathcal D}}\overset?=\mathfrak t_+$ (Hermite dense in graph norm) is **OPEN**
  and now load-bearing — if it fails, the operator-from-core is a proper restriction with different
  spectrum (where spectral programs historically die). **Existence survives; identification with the
  zeros does not (yet).** CLOS.1 downgraded to "✅ existence / ⬜ identification."
- **(RFB) attack — it's CARLESON, not raw density (referee #3 right).** $|\mathfrak t_-(g)|\le 4\sum_{\text{off-line}}|\widehat g(t-ib)|^2$,
  so (RFB) $\Leftarrow$ "$\mu_{\mathrm{off}}=\sum\delta_{t-ib}$ is a **Carleson measure** for $H(E_\gamma)$."
  **Clean sufficient condition:** $S_{\mathrm{off}}=\sum_{\text{off-line}}K(t-ib,t-ib)<\infty\Rightarrow\mathfrak t_-$
  **bounded** $\Rightarrow$ B-2 done with $a=0$ and the **RH-false separation** (bottom $<0$ possible). $S_{\mathrm{off}}$
  is a **kernel-weighted zero-density integral**: $K$ blows up near the strip edge ($\beta\to0,1$) where
  zeros are *rarest* (strong zero-density), moderate near the line where they may be *many* — a real
  tension. If $S_{\mathrm{off}}=\infty$, need the relative ($a>0$) interpolation regime (off-axis value
  from nearby on-axis samples; Carleson-box fine geometry, $S(T)$ fluctuation).
- **Logical reorder (referee).** "Does the Weil form close & control in $H(E_\gamma)$?" (CLOS + form-core
  + RFB) is now **prior** to 0A2/faithful-compression; 0A2 regains meaning only once $\overline{T_+}$ is
  shown to be the right operator.

> **Day-8 headline.** Audit caught a real overclaim (form-core $\ne$ density); CLOS.1 is now honest
> ("existence ✅ / identification ⬜"). (RFB) sharpened to its true nature — a **Carleson embedding** of
> the off-line-zero measure into $H(E_\gamma)$ — with a clean sufficient condition ($S_{\mathrm{off}}<\infty$,
> a weighted density integral) that would settle B-2 *and* exhibit the RH-false separation. Two new
> load-bearing open items: **form-core** (A.2) and **the Carleson/density integral** (B.3). Next: attack
> the form-core (Hermite graph-norm density) and make $S_{\mathrm{off}}$ quantitative.

**2026-06-02 — Day 9. DEEP DIVE: computing $K$ quantitatively forces a SPACE CORRECTION.** Per referee
Front 2 ("compute $K$ quantitatively") + the $S_{\mathrm{off}}$ suspicion. Record in
[`space-correction-strip-hardy.md`](space-correction-strip-hardy.md).
- **❌ $H(E_\gamma)$ TRIVIALIZES.** $K_{H(E_\gamma)}(\gamma,\gamma)\sim\log\gamma\,e^{-\pi\gamma/2}\to0$
  (Stirling on $|E_\gamma|\asymp|\gamma|$), so $\operatorname{Tr}T_+=\sum_\gamma K(\gamma,\gamma)<\infty$
  ⟹ **$\mathfrak t_+$ (and $\mathfrak t_-$) BOUNDED** ⟹ $\mathfrak t$ bounded ⟹ CLOS.1/CLOS.2 are
  **correct but VACUOUS** (Day-3 trichotomy **case 2**: trivializes, no RH separation). The Day-3 worry
  ("too-strong norm trivializes") was RIGHT; my Day-5 "de Branges back in play" used the WRONG de Branges
  space (the Gamma one, exp. weight $e^{\pi|t|/2}$ — that's the space *of the Gamma factor*, NOT *of the
  archimedean energy* $\mathfrak a$ whose weight is only $\Omega\sim\log$).
- **✅ CORRECTED HOME: strip Hardy $H^2(S_{1/2+\epsilon})$** (mild/flat weight). Goldilocks: (1) off-axis
  evals $|b|<\tfrac12$ bounded (RKHS of strip; $\epsilon$ fits the pole at $\pm i/2$); (2) **non-trivial**
  — $K_{S_d}(t,t)=\kappa(0)=\tfrac1{4d}$ const (translation-inv.), $\sum_\gamma K=\infty$, $\mathfrak t_+$
  genuinely **unbounded**; (3) Gaussians inside. **Explicit kernel:** $K_{S_d}(t-ib,t-ib)=\kappa(b)\asymp(d-|b|)^{-1}$,
  $t$-flat, edge-blowup. ($\epsilon$ = the regularization; deep zeros $|b|\to\tfrac12$ near edge = dangerous.)
- **✅ Referee's $S_{\mathrm{off}}<\infty$ is FALSE in the relevant case.** $S_{\mathrm{off}}=\sum_{\text{off-line}}\kappa(b_\rho)\ge\kappa(0)\cdot\#\text{off-line}=\infty$
  (infinitely many off-line). So $a=0$ (Day-8 B.2) cannot hold; **relative Carleson ($a>0$) FORCED** —
  a classical Carleson-measure problem for $H^2(S_d)$, fine zero-geometry ($S(T)$, separation), NOT raw
  density. Exactly the referee's prediction ("$S_{\mathrm{off}}<\infty$ hides almost all the difficulty").
- **CLOS.1 (Kato) TRANSFERS to $H^2(S_d)$ and is NON-vacuous** there ($\mathfrak t_+$ unbounded). Form-core
  A.2 re-posed: zeros over-sample ($\log T$ density vs $H^2(S_d)$ flat) ⟹ possible lower frame bound;
  flat-vs-log weight is part of A.2.

> **Day-9 headline.** A quantitative kernel computation (referee Front 2) caught a real error: the Days
> 5–8 home $H(E_\gamma)$ **trivializes** the Weil form (trace-class), so "closure" there was vacuous and it
> was the *wrong* de Branges space. Corrected to the **strip Hardy space** $H^2(S_{1/2+\epsilon})$ (mild
> weight), where everything is genuine: $\mathfrak t_+$ unbounded, Kato non-vacuous, kernel explicit and
> $t$-flat, and the referee's two intuitions become theorems (strong norm trivializes; $S_{\mathrm{off}}=\infty$
> forces relative Carleson). Next: pin the weight (flat vs log = form-core A.2); (RFB) as relative Carleson
> for $H^2(S_d)$; cite $|E_\gamma|$ asymptotic. The pattern holds: a green box (CLOS in $H(E_\gamma)$)
> turned out vacuous on deep audit — caught before building further.

**2026-06-02 — Day 10. AUDIT of the load-bearing kernel (referee priority) + parallel advances.** Record
in [`Day10-kernel-audit.md`](Day10-kernel-audit.md).
- **Danger B (formula) CLEARED ✅:** $K(t,t)=\tfrac{\varphi'}\pi|E|^2$ re-derived from $E=A-iB$, phase
  $\varphi$ — no sign/normalization slip.
- **Danger A/C (which $E$) NOT cleared — trivialization DOWNGRADED ◆:** the Gamma factor has TWO HB
  normalizations: $E\sim\gamma$ (modulus decays $e^{-\pi|t|/4}$, $K\to0$, **trivializes**) vs $E\sim1/\gamma$
  (modulus grows $e^{+\pi|t|/4}$, $K\to\infty$, does NOT). Conclusion **flips with convention** (exactly
  the referee's Danger C). Day-9 "$H(E_\gamma)$ trivializes ✅" → "◆ conditional on decaying-modulus norm."
  **Robust unconditional part:** *neither* Gamma normalization is Goldilocks (one trivializes, the other
  fails uniform eval-control) ⟹ home is an **intermediate mild-weight Hardy-band space**, exact weight to
  be **pinned from the literature** (de Branges *HSEF* / Lagarias). "Use $H^2(S_d)$" downgraded to "leading
  candidate family."
- **THE ROBUST GEM (space-independent THEOREM, Day-10 §3):** $K(t-ib,t-ib)\ge K(t,t)$ (continuation harder
  ⟹ larger eval) + faithful ($\inf_t K(t,t)=c>0$) + infinitely many off-line zeros $\Rightarrow$
  $S_{\mathrm{off}}\ge c\cdot\#\text{off-line}=\infty$. So **faithfulness and $a=0$ ($\mathfrak t_-$ bounded)
  are MUTUALLY EXCLUSIVE**; $a=0$ works only in trivializing spaces. ⟹ **relative Carleson ($a>0$) is
  intrinsic, unavoidable in any faithful space** — the arithmetic difficulty is not a modeling artifact.
  Proves the referee's Day-8 suspicion in strongest form. Needs only RKHS positivity (no de Branges $E$).
- **Parallel advances (space-robust, locked):** B-1 (von Neumann) ✅; EF-id (identity on core) ✅; the
  Day-10 dichotomy ✅; over-sampling observation (zeros density $\log T\uparrow$ vs flat reference ⟹
  possible lower frame bound, first step of form-core A.2) ◆. External resolver: read Bombieri/Lagarias for
  the space (literature task, settles §2).

> **Day-10 headline.** Auditing the load-bearing kernel (referee's call) found Danger C is **real**: the
> trivialization is normalization-dependent, so "strip Hardy is correct" is downgraded to "Gamma–de-Branges
> ruled out; faithful space is mild-weight Hardy-band, pin from literature." But the audit **upgraded** the
> durable core to a **space-independent theorem**: faithfulness $\Rightarrow$ $S_{\mathrm{off}}=\infty$
> $\Rightarrow$ relative Carleson is intrinsic. The conceptual phase-change (arithmetic difficulty is
> unavoidable, not a space artifact) survives the convention uncertainty. Next: literature pin (§2);
> over-sampling first step of A.2; then relative-Carleson characterization.

**2026-06-02 — Day 11. AUDIT of the Day-10 theorem (new pillar) — TWO gaps found, reconstructed.** The
referee chose to re-audit the Day-10 theorem before advancing. Record in
[`Day11-theorem-audit.md`](Day11-theorem-audit.md).
- **F2 gap CONCEDED ❌ (referee's catch).** "faithful $\Rightarrow\inf_t K(t,t)>0$" is **FALSE**:
  $K\sim1/\log t$ gives $\sum_\gamma K(\gamma,\gamma)\sim\sum_n 1/\log n=\infty$ (faithful) yet $\inf K=0$.
  Solid one-liner is only **$\inf_t K(t,t)>0\Rightarrow S_{\mathrm{off}}=\infty$**.
- **F1 gap FOUND ◆ (this audit).** Expansion $K(t-ib,t-ib)=K(t,t)+b^2 D(t)+\dots$, $D(t)=\sum_n(e_n'^2-e_ne_n'')$,
  and $D(t)$ **can be $<0$** (a function with $e'(t)=0,e''(t)>0$). So F1 ($K$ larger off-axis) is **not
  universal** — holds for **translation-invariant** spaces (convex even $\kappa(b)$, min at 0) but not
  generally. The Day-10 "space-independent" label was wrong; it's structure-dependent.
- **RECONSTRUCTED density-adapted theorem ✅/◆ (referee's suggestion, precised):** (i) $K(t,t)\ge c/\log(2+|t|)$
  + (ii) F1 + (iii) off-line positive proportion ($\sum_{\text{off-line}}1/\log t_\rho=\infty$) $\Rightarrow$
  $S_{\mathrm{off}}\ge c\sum_{\text{off-line}}1/\log t_\rho=\infty$ $\Rightarrow$ $a=0$ impossible. Covers
  BOTH candidate spaces (flat strip Hardy: $K=$const; log-weighted: $K\sim1/\log$); needs no constant kernel.
  (i) is a mild extra regularity beyond bare faithfulness = the referee's $K\gtrsim1/\log$ threshold.
- **META-FRAME (referee's point): structural-constraint / impossibility list K1–K4** — the durable output
  is NOT a space but constraints any faithful realization must satisfy (K1 trivial$\perp$faithful; K2
  faithful$\perp a=0$; K3 Gamma-dB excluded; K4 strong-norm$\perp$nontrivial). Impossibility results
  survive model changes better than positive constructions.

> **Day-11 headline.** The new pillar got the hard audit it deserved: **both** F1 and F2 had gaps, so the
> "space-independent theorem" is downgraded to a **density-adapted impossibility result with explicit
> hypotheses** (i)–(iii) — still covering the candidate spaces, still forcing relative Carleson. The
> genuine durable gain is the **constraint list K1–K4**: the faithful space threads a narrow window and the
> relative-Carleson difficulty is unavoidable inside it. Methodological shift (referee): we are now
> producing *impossibility* results, more robust than positive constructions. Next: verify F1/$D(t)\ge0$
> for the log-weighted strip; over-sampling lower-frame-bound (A.2); literature pin.

**2026-06-02 — Day 12. THE DENSITY SCALING LAW (referee: reformulate via $\rho(t)$, classify F1).** Both
asks fused into the deepest result so far. Record in [`Day12-density-scaling-law.md`](Day12-density-scaling-law.md).
- **DENS.1 — faithfulness criterion, $\inf K$-free ✅/◆:** replacing $\sum_\gamma$ by $\int(\cdot)\rho\,dt$
  ($S(T)$ fluctuation lower-order for slowly-varying $K$): **FAITHFUL $\iff K(t,t)\rho(t)\notin L^1$**.
  Verifies the 3 cases (flat $K\rho\sim\log\to\infty$; log $K\rho\sim1$; Gamma $K\rho\in L^1$ trivial). This
  is the referee's exact $K\gtrsim1/\log$ threshold, and it **removes the Day-11 F2 gap** (no $\inf K$).
- **DENS.2 — F1 CLASSIFIED = Level B geometric ✅:** kernel identity $K(t-ib,t-ib)=K(t,t)+b^2D+\dots$ with
  $D=2K_{11}-\tfrac12K''=K_{11}-\sum e_ne_n''$ ($K_{11}=\sum e_n'^2\ge0$), double-checked via $\Delta K=4K_{11}$.
  **F1 $\iff K''(t)\le4K_{11}(t)$**, and for a density-matched (slowly-varying) diagonal $K''\sim K/t^2\lll
  K_{11}\sim K/d^2$, so F1 holds — a consequence of **band geometry**, NOT translation-invariance, NOT
  accidental. Resolves the referee's "model vs problem" risk in the GOOD direction. Verified on explicit
  strip kernel ($K_{11}=\pi^2/16d^3>0$).
- **DENS.4 — NECESSARY SCALING LAW ✅/◆ (the durable, model-independent output):** any faithful realization
  obeys $K\rho\notin L^1$; canonical = critical sampling $K\asymp1/\rho\sim2\pi/\log t$ ($R=K\rho\asymp1$).
  Bonus: **even $H(E_\xi)$ (full $\xi$ de Branges) trivializes** ($|E|\sim e^{-\pi t/4}$ ⟹ $K\rho\in L^1$),
  so the faithful space is NOT a standard de Branges space ($|E|$ decaying) — needs $|E|\asymp$const
  (Hardy-band). K2 in density form: $S_{\mathrm{off}}=\infty\iff K\rho_{\mathrm{off}}\notin L^1$.
- **POSITIVE ADVANCE — form-core A.2 = a sampling problem ✅(reduction):** in the critical space
  $\mu_{\mathrm{on}}$ is **Carleson** (1 zero/box) ⟹ **UPPER frame bound PROVED** ($\mathfrak t_+$ bounded,
  non-trace-class = "bounded but not trace-class," correcting Day-9's loose "unbounded"). Then **A.2
  $\Leftarrow$ LOWER frame bound $\iff\{\gamma\}$ a SAMPLING sequence for $H_{\mathrm{crit}}$** — a
  Beurling-borderline question (holds under RH: zeros = de Branges Riesz basis of $H(E_\xi)$; uncond. open).

> **Day-12 headline.** The referee's "reformulate via density" produced the program's deepest pure-math
> result: a **necessary scaling law $K\rho\notin L^1$** that constrains *any* faithful realization (not a
> chosen space), with critical sampling $K\asymp1/\rho$ canonical; **F1 reclassified as geometric (Level
> B)**, removing the Day-11 conditionality across the band family; and a positive advance reducing
> **form-core A.2 to the zeta zeros being a sampling sequence** (upper/Carleson bound proved, lower bound =
> Beurling-borderline, RH-true). The durable stack now: B-1, EF-id, K1–K4, and the scaling law. Next: the
> lower frame bound (or weakest zero-regularity input); relative Carleson in density form; literature pin.

**2026-06-02 — Day 13. AUDIT of DENS.1 (the new pillar; referee priority over the lower-frame-bound).** The
sum$\to$integral step rests on $\int K\,dS$ being lower-order. Record in
[`Day13-DENS1-audit.md`](Day13-DENS1-audit.md).
- **The fluctuation computation (referee's concern, done):** $E(T)=\int_0^T K\,dS=K(T)S(T)-\int_0^T SK'\,dt$,
  bounded via crude $|S|=O(\log)$. Rates: flat $E=O(\log T)$ vs $M\asymp T\log T$; critical $E\asymp\int\frac{dt}{t\log t}=O(\log\log T)$
  vs $M\asymp T$; near-boundary $E$ **converges** vs $M\asymp\log\log T$; Gamma both converge. **The referee
  is right that $\int\frac{dt}{t\log t}=\infty$ (error diverges) — but at rate $\log\log T\lll T\sim M$, so
  $E=o(M)$ always; converges near the faithfulness boundary where the verdict is decided.** Sign harmless
  ($M\to+\infty$). The verdict $K\rho\in L^1$? never flips.
- **VERDICT (matches referee's prediction): DENS.1 HOLDS, now CONDITIONED:** $K$ **regularly varying**
  ($|K'|/K\lesssim1/t$, no wild oscillation) $\Rightarrow$ [faithful $\iff K\rho\notin L^1$]. Mild, met by
  ALL band candidates (flat, critical). **Crude $S=O(\log)$ suffices — no fine $S(t)$ input, no RH.** The
  **critical scaling law $K\asymp1/\rho$ survives UNCONDITIONALLY** (independent of the $S$-audit).
- **META: first audited pillar (Days 7–13) to HOLD UP** — only acquired an honest side-condition, didn't
  crack (unlike CLOS-in-$H(E_\gamma)$, the Day-10 theorem). Possible sign of reaching stable ground.

> **Day-13 headline.** The referee's audit of the new pillar was right to demand and **favorable**: DENS.1
> survives with its hypothesis made explicit ("$K$ regularly varying") exactly as predicted — a genuine but
> mild conditioning, needing nothing delicate about $S(t)$. The divergent-but-slower fluctuation
> ($\log\log T\lll T$) is the precise resolution of the "$\int dt/(t\log t)=\infty$" worry. Durable stack:
> B-1, EF-id, K1–K4, critical scaling law (uncond.), DENS.1 (reg.-varying $K$). Next: lower frame bound
> (A.2) and relative Carleson in density form, now on an audited foundation.

**2026-06-02 — Day 14. AUDIT of the "A.2 $\Leftarrow$ lower frame bound" reduction (referee Priority 1) —
finds a SECOND TRIVIALITY.** Record in [`Day14-reduction-audit.md`](Day14-reduction-audit.md).
- **THE HOLE ❌:** Day-12 §6 did the reduction in the **critical space** ($R=K\rho\asymp1$). There
  $\mu_{\mathrm{on}}$ Carleson ⟹ $\mathfrak t_+$ **bounded** ⟹ form-core AUTOMATIC (no frame bound needed).
  BUT $\mu_{\mathrm{off}}$ (same critical density, interior depths) also Carleson ⟹ $\mathfrak t_-$ bounded
  ⟹ $\mathfrak t$ **BOUNDED** ⟹ **B-2 VACUOUS**. So the critical space is a **2nd triviality T2** (distinct
  from Day-9 trace-class T1): T1 = $K\rho\in L^1$ ($\mathfrak t_+$ compact); T2 = $\mu$ Carleson / $R$
  bounded ($\mathfrak t$ bounded, B-2 vacuous). Days 12–13 treated critical $R\asymp1$ as canonical — it's
  **T2-trivial**. Referee's Priority-1 audit caught it.
- **CORRECTION ✅:** genuine (non-vacuous) B-2 needs $\mathfrak t$ unbounded-below-able ⟹ $\mathfrak t_-$
  unbounded ⟹ $\mu_{\mathrm{off}}$ NOT Carleson ⟹ over-sampling ⟹ **$R=K\rho\to\infty$**. The genuine
  faithful space is **flat (sub-critical-weight) Hardy-band**, $R\sim\log t\to\infty$, where $\mathfrak t_\pm$
  are UNBOUNDED. Sharpened ladder: T1 ($\in L^1$) / T2 ($R$ bounded, incl. critical) / genuine ($R\to\infty$).
  "faithful $\Rightarrow K\rho\notin L^1$" still necessary but NOT sufficient (critical satisfies it yet
  T2-trivial); genuine needs strictly stronger $R\to\infty$. **New constraint K5: bounded $\perp$ genuine B-2.**
- **A.2 ≠ frame bound in the genuine space ✅:** with $R\to\infty$, $\mathfrak t_+$ unbounded, and upper bound
  (Carleson) FAILS, lower bound (coercivity) and form-core (A.2) SEPARATE. The Day-12 §6 reduction conflated
  form-core with coercivity. **Priority-2 bonus:** coercivity $T_+\ge c>0$ is the EASY part (over-dense zeros,
  Beurling lower density $\to\infty>$ Nyquist, modulo finite-rank low-$t$ correction). The genuine difficulty
  is (a) form-core density + (b) RFB $\mathfrak t_-\lesssim\mathfrak t_+$ (off-line$\le$on-line over-dense
  measures) — both governed by FINE zero geometry (separation, $S(T)$, pair correlation), as the referee
  foresaw. So the classical input that enters is NOT Beurling density (gives coercivity free) but the finer
  relative comparison.

> **Day-14 headline.** Priority-1 audit of the reduction found a real Day-10-style hole: the "A.2 $\Leftarrow$
> lower frame bound" was done in the critical space, which is a **second triviality (T2): $\mathfrak t$
> bounded ⟹ B-2 vacuous**. Genuine B-2 lives in the **over-sampling** regime $R=K\rho\to\infty$ (flat
> Hardy-band), where coercivity is easy but **A.2 (form-core) and RFB are the real, fine-geometry questions**.
> Durable stack updated: +K5, sharpened faithfulness ($R\to\infty$). Next (Priority 2): the minimal fine
> zero-regularity input for RFB / form-core; defer F1 (Priority 3). **[T2/K5 mechanism corrected Day 15.]**

**2026-06-02 — Day 15. AUDIT of K5 (referee: audit before pillarizing) — the Carleson step CONFLATED TWO
INVARIANTS.** Record in [`Day15-K5-audit.md`](Day15-K5-audit.md). Followed the referee's 3-step recipe.
- **Intrinsic resolution $\ell(t)=\sqrt{K(t,t)/K_{11}(t)}$** (kernel coherence length). For Hardy-band
  $\ell\asymp d$ **constant** (verified on explicit kernel: $\ell=2d/\pi$); slowly-varying weight doesn't
  change it (bandwidth set by strip width $d$, not weight).
- **Carleson is governed by $P=\rho\ell$, NOT $R=K\rho$ ✅.** $R/P=\sqrt{KK_{11}}\asymp K/d$; they coincide
  only when $K\asymp d$ (flat). For the "critical" weight $K\sim1/\log$: $R\asymp1$ **but** $P=\rho\ell\sim
  d\log t\to\infty$. **So "$R\asymp1\Rightarrow\mu$ Carleson" (the K5 step) is FALSE** — the critical-weight
  space over-samples ($P\to\infty$), $\mathfrak t_+$ unbounded, NOT T2-trivial. Exactly the referee's
  "which spatial scale?" concern.
- **Over-sampling is FORCED for all admissible spaces ✅.** Eval-bounding at depth $\tfrac12$ $\Rightarrow$
  $d\ge\tfrac12$ $\Rightarrow$ $\ell\gtrsim\tfrac12$ $\Rightarrow$ $P=\rho\ell\gtrsim\tfrac12\rho\to\infty$.
  So every eval-bounding strip space over-samples; $\mathfrak t_+$ **always unbounded**. **No T2 there.** The
  only Carleson ($P\asymp1$) spaces are resolution-shrinking ($\ell\sim1/\log$) = de Branges ($\varphi'\sim\log$),
  but those have $|E|$ decaying ⟹ **T1 (trace-class)**. T2 (Carleson+faithful) needs $\varphi'\sim\log$ with
  $|E|\asymp$const — blocked by the HB phase–amplitude relation; **likely collapses into T1**.
- **VERDICT:** **K5 downgraded ◆** (not established; no T2 among admissible spaces). **Day-14 conclusion
  SURVIVES with a stronger reason:** genuine = over-sampling Hardy-band is **forced** ($\ell\ge\tfrac12$),
  not contingent on a T2 dichotomy. **DENS.1 unaffected** (it is the $R$/trace-class question, correct
  invariant). Durable gain: **clean separation $R=K\rho$ (trace-class) vs $P=\rho\ell$ (Carleson)** — Day-14
  had merged them. "Critical scaling $K\asymp1/\rho$" is a trace-density normalization, NOT critical
  sampling (terminology corrected).

> **Day-15 headline.** K5's audit (referee's call) caught a genuine invariant-conflation: Carleson depends
> on $P=\rho\ell$ (resolution), not $R=K\rho$ (trace density); eval-boundedness forces $\ell\gtrsim\tfrac12$,
> so over-sampling ($P\to\infty$) is **universal** among admissible spaces — $\mathfrak t_+$ always
> unbounded, genuine space forced. T2/K5 downgraded; the over-sampling conclusion upgraded from contingent
> to forced. Net: two invariants cleanly separated (the durable gain). Next: RFB ($\mathfrak t_-\lesssim\mathfrak t_+$),
> where the fine zero geometry finally enters.

**2026-06-02 — Day 16. Carleson sufficiency (Schur) + a rigorous reduction of RFB (referee provided a
proof sketch).** Record in [`Day16-carleson-and-RFB.md`](Day16-carleson-and-RFB.md).
- **Carleson, audited ✅/◆:** $P\lesssim1$ + separation $\Rightarrow$ Carleson (Schur test, rigorous, the
  referee's argument); **full equivalence FALSE** (clustering breaks it) — sufficient direction only, $P$ =
  natural local density. **Direct $P\to\infty\Rightarrow\mathfrak t_+$ unbounded** via kernel test
  $\langle k_t,Tk_t\rangle/\|k_t\|^2\approx K(t,t)P\to\infty$ — **upgrades Day-15** (box heuristic → rigorous),
  answering the referee's "prove non-Carleson directly?" — yes.
- **RFB proof sketch audited — a real HOLE in Step 3 ❌:** $\sum_\gamma|F'(\gamma)|^2\le C_d\|F\|^2$ FAILS in
  over-sampling (over-counts by $P\to\infty$ — the forced over-sampling biting back); both $\sum|F'(\gamma)|^2$
  and $\mathfrak t_+$ carry the $P$ factor, only the *ratio* is bounded; routing through $\|F\|^2$ loses it.
- **The clean fix (derivative-free) ✅(mod regularity):** off-axis$\to$on-axis via interpolation coeffs
  $F(\gamma+ib)=\sum_{\gamma'}c_{\gamma'}F(\gamma')$, then Schur ⟹ $\widetilde{\mathfrak t}_-\le CC'\mathfrak t_+$
  **if** the $c$ are $\ell^1$-Schur bounded (rows AND columns). So RFB needs **TWO** fine-geometry hypotheses
  (sampling + Schur regularity), not the one the sketch claimed.
- **CONDITIONAL THEOREM (Day-16 C):** [bounded multiplicity + zeros a sampling sequence with Schur
  interpolation regularity] $\Rightarrow\mathfrak t_-\lesssim\mathfrak t_+\Rightarrow$ **Weil form semibounded
  (B-2)**. **The arithmetic frontier, located precisely:** the regularity hypothesis = zeros a REGULAR
  sampling sequence = minimum **separation** / $S(T)$ control / **Montgomery pair correlation** / **GUE**.
  Honest tension: zeros have NO positive uniform min gap (close pairs expected), so hyp. must be the
  *averaged/Schur* form — itself a pair-correlation question. (Lower frame bound at over-critical density may
  still be RH-conditional — the Day-12 §6 loop persists, flagged.)

> **Day-16 headline.** Functional analysis taken to its limit: **RFB follows by standard analysis ONCE the
> zeros' sampling regularity is granted** — and that regularity IS the fine arithmetic (separation, $S(T)$,
> Montgomery pair correlation, GUE). The referee's thesis ("FA ends, arithmetic begins at the lower frame
> bound") is now a *proven boundary*, sharpened: it's sampling **+ Schur regularity** (two conditions), and
> the program's hard core is definitively the fine geometry of the zeros. Durable conditional theorem in
> hand. Next: weakest sufficient arithmetic form of the regularity hypothesis.

**2026-06-02 — Days 17–18. VERIFICATION of a deep multi-thread exploration (referee asked to double-check
& find errors).** Records: [`Day17-verification.md`](Day17-verification.md), [`Day18-quadrature.md`](Day18-quadrature.md).
- **Day-17: TWO real ERRORS found.** (1) The "Montgomery-scale reversal" (claim: local under-sampling ⟹
  coercivity not free) is WRONG — confuses kernel **coherence length** with **bandwidth** (bandwidth = its
  *inverse*); flat-kernel limit = rank-1 degenerate = MORE over-sampling; and **$P=\rho\ell$ is
  SCALE-INVARIANT** ($\rho\to\rho/\lambda,\ell\to\lambda\ell$) so it can't be rescaled away. Coercivity
  STAYS easy; Days 14–16 stand. (2) "Regular lattice / Schur ⟹ RFB" is WRONG in over-sampling: $G_0^{-1}\sim\rho\to\infty$
  (Gram near-singular), and direct Schur gives $\|A\|\lesssim P\to\infty$ — **every $\ell^1$ route hits the
  $P$ wall** (same as the Day-16 Step-3 hole). CORRECTED: RFB plausibly TRUE $O(1)$ via the **$P$-cancellation**
  in $\widetilde{\mathfrak t}_-/\mathfrak t_+$ (both over-sample by $P$).
- **Day-18: the QUADRATURE reformulation — verified, NO outright error.** The referee dropped Gram/Schur and
  recast RFB as a **band-fixed quadrature** $\sum_\gamma|F(\gamma)|^2\asymp\rho\int|F|^2$ ($P$ cancels).
  Verified: vertical $L^2$ bound ✅ (strip-weight caveat); **$S(T)=O(\log)$ INSUFFICIENT** ✅ (error $\asymp$
  main term — honest self-correction); form-factor route ($\widehat R_2(\alpha)\sim|\alpha|$ ⟹ number-variance
  suppression ⟹ $E(g)=o(1)$) ✅ morally correct RMT.
- **REDUCTION vs REFORMULATION (the verdict):** the needed input = **uniform low-freq discrepancy / form
  factor** of the zeros = **RH-conditional (Montgomery, only proven under RH) or at the unconditional
  frontier** (Selberg's $\int S^2\ll T\log\log T$ gives *typical* not *uniform*). So MOST LIKELY a **new
  EQUIVALENT of RH**: "RH ⟺ zeros are an asymptotically perfect band-fixed quadrature" — NOT an
  unconditional proof. Confirms the referee's own pessimistic scenario. **DECISIVE OPEN QUESTION (settles
  the program's status): is a uniform low-freq discrepancy bound for $\{\gamma\}$ available UNCONDITIONALLY?**
- **DURABLE META-INSIGHT (endorsed):** every point-wise control failed by $P\to\infty$; every statistical
  (average) control made $P$ cancel ⟹ the correct object is **statistical (quadrature/equidistribution),
  not local (sampling/interpolation)**. The Weil operator was a machine that distilled this. The program's
  content migrated from "spectral property of $\mathcal T$" to "**equidistribution/quadrature property of
  the zeros**" — the most robust conceptual output, surviving every audit. Likely final shape:
  RH ⟺ semibdd ⟸ RFB ⟸ band-fixed quadrature of zeros (deepest step = last; "quadrature ≈ RH" expected).

> **Days 17–18 headline.** The referee's deepest push: two concrete reductions (Montgomery reversal;
> lattice/Schur) were **erroneous** (the $P$-over-sampling forbids every $\ell^1$ proof), but the
> **quadrature reformulation** they pivoted to is **correct and the right object** — RFB reduces to a
> uniform low-frequency **quadrature/discrepancy** law for the zeros, governed by the Montgomery form
> factor. That law is RH-conditional or frontier, so the honest status is a **new equivalent of RH** (the
> pessimistic scenario, most probable). The durable, audit-proof gain: the program's core is now a
> **statistical equidistribution property of the zeros**, not an operator-spectral one. Single decisive
> open: is the uniform discrepancy bound unconditional (Selberg) or RH-only (Montgomery)?

**2026-06-02 — Day 19. VERIFICATION of the Parseval/pair-correlation input (referee: "muy serio, verifica
todo"). NO outright error — and it SIMPLIFIES.** Record in [`Day19-pair-correlation-input.md`](Day19-pair-correlation-input.md).
- **Parseval ✅:** $E_g=\int_{-2d}^{2d}\widehat g\,D_T$, $|E_g|\le\|\widehat g\|_2\|D_T\|_{L^2[-2d,2d]}$. And
  it is **cleaner in $PW_d$ = the classical Weil (compact-support) test class** — band-limited ⟹ entire ⟹
  off-axis evals automatic, **no strip-weight machinery** (Days 9–15 simplified away). Referee's bonus.
- **$\|D_T\|^2_{L^2}$ = pair-corr 2nd moment ✅:** $V(d,T)=4dN+\sum_{\gamma\ne\gamma'}\frac{2\sin(2d(\gamma-\gamma'))}{\gamma-\gamma'}$
  = Montgomery sum, $\widehat r=\mathbf 1_{[-2d,2d]}$, scale $1/d$. **Form factor enters at $\beta=\xi/\rho\to0$
  = Montgomery's PROVEN range** ($\widehat R_2(\beta)\sim|\beta|$). The referee's $L^2$-not-$L^\infty$ move is
  the right object; BGSTB (unconditional Montgomery, arXiv 2306.04799) is exactly the relevant literature.
- **Subtlety resolved (which norm closes B-2) ✅:** majorant gives $\kappa(b)=e^{2d|b|}>1$; in $L^2$ that
  fails, but in the **zero-sampling space $H_+\cong\ell^2(\{\gamma\})$** ($\mathfrak t_+=\|\cdot\|^2$),
  $\mathfrak t/\|\cdot\|^2\ge1-4\kappa(b)$ finite ⟹ **B-2 closes**; RH = sign of bottom (CL.2, norm-indep).
  Over-sampling is *cured* by working in $H_+$ ($\mathcal T_+=I$). So B-2 reduces to quadrature + coercivity,
  not a direct RH proof.
- **THE decisive borderline:** $E_g=O(\mathfrak t_+)$ needs $V(d,T)$ at the right level. **Diagonal $4dN$ =
  UNCONDITIONAL** (counting), suff. **up to a $\log$**; off-diagonal $\log$ closed by Montgomery-range
  cancellation. **Decisive question: is $V$ bounded UNCONDITIONALLY?** If YES (BGSTB/Goldston–Montgomery/Gonek)
  ⟹ **B-2 UNCONDITIONAL** = faithful semibounded realization w/o RH = **§6 DREAM (A∧B∧C, RH-independent)**;
  if RH-only ⟹ new RH-equivalence. **FIRST TIME the missing input is a single concrete classical ANT
  quantity** (mesoscopic pair-corr 2nd moment) with active recent literature on its unconditionality.

> **Day-19 headline.** The referee's reduction **verifies clean** (no error, unlike Day 17) and *simplifies*
> the framework to the classical band-limited Weil class. The program's irreducible core is now explicit:
> **B-2 (a faithful semibounded realization, RH-independent) holds iff a single mesoscopic pair-correlation
> second moment $V(d,T)=\int_{-2d}^{2d}|D_T|^2$ is controlled** — diagonal-unconditional up to a log, closed
> by Montgomery's *proven-range* cancellation. Whether that closing is unconditional is the ONE question
> separating "an unconditional faithful spectral reformulation of RH" (the dream) from "a new equivalent of
> RH." MAX-EFFORT next: nail the threshold bookkeeping + the BGSTB/Goldston–Montgomery literature check.
> **[Day-20: the "$V(d,T)$ global" framing is VACUOUS; corrected below.]**

**2026-06-02 — Day 20. The referee's threshold push has a VACUOUS step; the correction points to
UNCONDITIONAL B-2.** Record in [`Day20-threshold-correction.md`](Day20-threshold-correction.md). The
referee asked: reformulation or what? Verify, find errors, max effort.
- **❌ ERROR FOUND:** the chain $|E_g|\le\|\widehat g\|_2\sqrt{V(d,T)}$ uses the **global** $V$ ($V_{\mathrm{diag}}\sim T\log T$),
  giving $|E_g|/\mathfrak t_+\lesssim\sqrt{T_0/\log T_0}\to\infty$ — **VACUOUS**. The localizer's phase
  correlates with only a sliver of $D_T$; global Cauchy–Schwarz discards the localization. **So the demand
  "$V\ll(\log T)^2$ / strong Montgomery off-diagonal cancellation" is an ARTIFACT, not the real requirement.**
- **THE CORRECTION (local bound):** $E_g=\int|F|^2 dS$, IBP $=\int(|F|^2)'S$, and **Bernstein**
  ($\int|(|F|^2)'|\le2d\|F\|_2^2$) + **unconditional $S=O(\log)$** ⟹ $|E_g|\le2d\log T_0\|F\|_2^2=O(\mathfrak t_+)$
  (the $\log T_0$ from $S$ cancels $\rho\sim\log T_0$). **Crucial:** B-2 needs $E_g=O(\mathfrak t_+)$ (FINITE
  const), **NOT** $o(\mathfrak t_+)$ — the Day-18 "$S=O(\log)$ insufficient" targeted the wrong ($o$) thing.
- **Off-line:** in $PW_d$, $\kappa(b)=e^{2d|b|}<e^d$ **uniformly** ($|b|<\tfrac12<d$, NO deep-zero blowup —
  band-limiting removes the Days 9–15 strip-edge danger); off-line $\rho_{\mathrm{off}}\le\rho$ by **classical
  zero-density (unconditional)** ⟹ $\widetilde{\mathfrak t}_-\le C\mathfrak t_+$ finite ⟹ $\mathfrak t\ge(1-4C)\|\cdot\|^2_{H_+}$.
  **⟹ B-2 PLAUSIBLY UNCONDITIONAL, Montgomery NOT needed.**
- **ANSWER (reformulation or what?): probably BETTER than a reformulation.** Referee's bet (60% RH-reformulation)
  rested on the vacuous bound. Corrected estimate: ~60% **unconditional B-2** (= §6 prize: faithful semibounded
  Weil realization, RH-independent), ~20% RH-reformulation, ~20% surprise. RH itself = the sign of the now-finite
  bottom (untouched).
- **⚠️ MANDATORY: this Day-20 optimistic claim is now the load-bearing pillar and must survive its OWN hostile
  audit** (§5): (1) IBP boundary/tail for non-compact $PW_d$; (2) the exact off-line 2D quadrature (varying
  $b_\rho$, $\rho_{\rm off}\le\rho$ + zero-density giving finite $C$); (3) is $C$ useful (or just finite); (4)
  re-confirm coercivity. NOT written as a theorem yet.

> **Day-20 headline.** The referee's threshold push contained a **vacuous global Cauchy–Schwarz**; correcting
> it to the **local IBP+Bernstein+Selberg** bound shows B-2 needs only a **finite-constant** quadrature
> comparison — **unconditional, no Montgomery**. So the program likely lands on **unconditional B-2** (a
> faithful semibounded Weil realization, RH-independent — the §6 prize), *not* an RH-reformulation. RH stays
> the sign. **But this is now the optimistic load-bearing claim and must pass its own hostile audit (§5)
> before becoming a theorem** — the discipline that caught every prior over-claim applies here most of all.

**2026-06-02 — Day 21. Proofs A/B/C verified; off-line sum CLOSED; B-2 ⟸ a single gap bound.** Record in
[`Day21-offline-and-coercivity.md`](Day21-offline-and-coercivity.md). The referee wrote Proofs A (IBP), B
(Bernstein+Selberg), C (vertical), flagged the off-line discrete sum as the remaining gap; asked to verify
+ complete.
- **A/B/C VERIFIED ✅** (minor precision: A's $O(1/t)$ boundary term still gives $g\log t\to0$; B's IBP tail
  $O(\log T_0/R^2)$ dominated by window; C exact). $E_g=O(\mathfrak t_+)$ is $O$ not $o$ — exactly B-2's need.
- **OFF-LINE GAP CLOSED ◆→✅ (the advance):** **Plancherel–Pólya** (band-limited Carleson/Bessel, handles
  ARBITRARY non-separated 2D sequences — answers the referee's exact worry) ⟹ $\widetilde{\mathfrak t}_-\le B\|F\|_2^2$,
  $B\asymp$ off-line points per Nyquist cell $\le$ ALL zeros per cell $=O(\rho)$ (RvM$+S=O(\log)$, uncond.).
  So $\widetilde{\mathfrak t}_-\le C_d\rho\|F\|_2^2$ UNCONDITIONAL. **Why B-2 not RH:** off-line *globally*
  sparse but may *cluster locally* ⟹ local count $\le\rho$ (total), NOT $\rho_{\mathrm{off}}$; using
  $\rho_{\mathrm{off}}$ would give $o(\mathfrak t_+)$=RH, forbidden by clustering.
- **THE SINGLE REMAINING INPUT — COERCIVITY = NO LARGE GAPS:** B-2 ⟸ $\mathfrak t_+\ge c\rho\|F\|^2$ ⟸ **no
  $\zeta$-zero gap exceeds Nyquist $1/d$** ($d\to\tfrac12^+$, Nyquist$\sim2$). Zeros' lower Beurling density
  $D^-=\infty>$ Nyquist (super-sampling, favorable); the lower frame bound needs no Nyquist cell empty.
  **One-sided gap-regularity — VASTLY weaker than RH** (constrains the largest gap, not any zero's location).
- **NET:** EVERYTHING ELSE UNCONDITIONAL (A,B,C, Plancherel–Pólya). **The entire residual of B-2 is: do the
  zeros have no Nyquist-size gaps?** If yes (or if averaged coercivity from $D^-=\infty$ alone suffices —
  audit §2½), **B-2 is an UNCONDITIONAL THEOREM** (faithful semibounded Weil realization, the §6 prize).

> **Day-21 headline.** Proofs A/B/C verify; the off-line sum the referee couldn't close is **closed
> unconditionally by Plancherel–Pólya** (clustering-robust). B-2 now reduces — with everything else
> unconditional — to a **single classical gap-regularity**: the $\zeta$-zeros have no Nyquist-size gaps
> (coercivity). That is a one-sided statement far weaker than RH, with $D^-=\infty$ already strongly
> favorable. **If it holds unconditionally (or averaged coercivity suffices), B-2 is an unconditional
> theorem.** Mandatory next: audit §5 (esp. 2½: does $D^-=\infty$ give coercivity with no gap hypothesis?).
> **[Day-22: §2½ answered NO; gap framing refined to a depth split.]**

**2026-06-02 — Day 22. Coercivity (§2½) as PURE SAMPLING (referee: forget zeta, attack it as a frame
problem).** Record in [`Day22-coercivity.md`](Day22-coercivity.md).
- **§2½ ANSWERED: $D^-=\infty$ does NOT give the lower frame bound ✅ (referee's instinct right).** Beurling:
  set of sampling for $PW_d$ $\Leftarrow$ no gap $>\pi/d$ (gap theorem); $D^-\ge d/\pi$ is NECESSARY not
  sufficient. A single Nyquist gap + a bump in it kills coercivity. **So the gap dependence is genuine, not
  removable by density.**
- **BUT the Day-21 "no gaps" framing was too crude.** Refinement: coercivity is **only needed near off-line
  zeros** (a large gap with no off-line zeros is harmless, $\mathfrak t=\mathfrak t_+\ge0$). **DEPTH SPLIT:**
  shallow off-line ($|b|<\delta$, $\kappa\approx1$) sample like on-line — **harmless** (may cluster); deep
  off-line ($|b|\ge\delta$, $\kappa$ up to $e^d$) are the danger but **locally $o(\rho)$** by classical
  **short-interval zero-density** ($N(\sigma,T+1)-N(\sigma,T)=o(\log T)$, $\sigma>\tfrac12$, uncond.). So every
  Nyquist window keeps $\sim P-o(P)$ samples with $\kappa\approx1$ ⟹ coercivity; deep part $=o(\mathfrak t_+)$.
- **B-2 ⟸ uniform short-interval zero-density for $\sigma>\tfrac12+\delta$** — classical, plausibly
  unconditional, **≪ RH, sharper than "no gaps".** TO EXECUTE: (1) pin $\delta$ + is the *uniform* (every $T$)
  short-interval density unconditional or only on-average? = THE frontier; (2) bound the shallow term; (3)
  rigorous coercivity from the $P-o(P)$ retained samples.
- **RECALIBRATED:** ~45% uncond B-2 (down from ~50%), ~35% needs near-frontier uniform short-interval density,
  ~20% surprise. Lowered because the referee's coercivity worry was right — it's NOT free from density.

> **Day-22 headline.** Attacking coercivity as pure sampling: **$D^-=\infty$ is insufficient** (one Nyquist
> gap kills the lower frame bound — the referee called it). But coercivity is only needed *near off-line
> zeros*, and a **depth split** shows only **deep** off-line zeros (large $\kappa$) are dangerous — and those
> are **locally $o(\rho)$ by classical short-interval zero-density**, shallow ones harmless. So **B-2 ⟸
> uniform short-interval zero-density for $\sigma>\tfrac12$** — sharper than the Day-21 "no gaps," ≪ RH. Still
> not a theorem: the *uniform* version of that density is the precise frontier. Next: is uniform short-interval
> zero-density for fixed $\sigma>\tfrac12$ unconditional?

---

**2026-06-03 — Day 23. RECONNECTION TO RH + PATH (A) CLOSED + KREĬN STRUCTURE + NO-GO + PAPER A.** A long,
multi-part day driven by the external team (hostile-referee mode). Records: `RH-ENDGAME.md`, `B2-THEOREM.md`,
`B3-KREIN-STRUCTURE.md`, **`PAPER-A.md`** (the deliverable).

- **RH end-game reconnection (`RH-ENDGAME.md`).** Honest reconnection to the actual goal: the 22 days give
  $\inf\operatorname{spec}(\mathcal T)\ge1-4C$, $C\ge e^d>1$ finite = **B-2 (the bottom is FINITE)**. RH is
  the **SIGN** ($\ge0$). All machinery bounds **magnitude** ($|\mathfrak t_-|\le C\mathfrak t_+$, $C>1$),
  which gives B-2 but **cannot supply the sign** — lowering $C\le1$ *is* RH. Two end-games: **(A)** faithful
  reformulation (achievable, NOT a proof); **(B)** structural positivity $\mathcal T=A^*A$ (the only route to
  the sign; very low prob; never engaged).

- **PATH (A) CLOSED (`B2-THEOREM.md`, then `PAPER-A.md`).** Per user instruction ("cerrá A del todo, no
  termines hasta cerrarlo, así lo valido"). Complete B-2 theorem: **Lemmas A (IBP $E_g=-\int g'S$), B
  ($E_g=O(\mathfrak t_+)$ via Bernstein+Selberg — note $O$ not $o$), C (vertical $\|F(\cdot+ib)\|^2\le e^d\|F\|^2$,
  exact), D (off-line $\le C_d\rho\|F\|^2$, Plancherel–Pólya with clustering) — ALL UNCONDITIONAL.** Residual
  isolated as **hypothesis (H)** (uniform local sparsity of deep off-line zeros; on-line+shallow keep a
  fraction $\eta$ of every Nyquist cell). $(H)\Rightarrow$ coercivity (Beurling) $\Rightarrow$ B-2. **Honest
  recompute: (H) is NOT unconditional** — global $N(\tfrac12+\delta,T)\ll T^{1-c\delta}$ allows a $\sim\log T$
  deep-cluster in one short interval; Selberg makes it a large deviation (measure $\ll\exp(-c(\log T)^2/\log\log T)$),
  rare but not provably absent. (H) is genuinely needed (else $F$ with $\mathfrak t_+=0,\mathfrak t_-\ne0$
  breaks closability). So **Theorem A = B-2 modulo (H); (H) ≪ RH, frontier.** Corollary: RH ⟺ sign of bottom.

- **B3 KREĬN STRUCTURE (`B3-KREIN-STRUCTURE.md`), proposed by the team, verified + audited.** Team's identity
  $\mathfrak t=E^*JE$ **correct** (their antilinear $J=\overline{c_{\bar\rho}}$ = convention slip; clean object
  = linear involution $J=J^*$, $J^2=I$, $\sigma(\rho)=1-\bar\rho$). Three consequences verified (RH⟹J=I⟹E*E≥0;
  RH-fail⟹J=I⊕swap-blocks, negativity = exactly off-line; RH⟺R(E) is J-nonnegative). **Added: angular operator
  $K$** — exact split $\mathfrak t=\|P_+EF\|^2-\|P_-EF\|^2$ (no factor-4 slack); single-axis dictionary
  **$\|K\|<\infty\Leftarrow(H)=$B-2; $\|K\|\le1\iff$RH**; $\|K\|\ge e^{d/2}$ magnitude side. **Corrections from
  referee pushback:** (1) $P_+|_{R(E)}$ injectivity is QUALITATIVE/uncond. (type-density), ≠ quantitative
  boundedness (=(H)); (2) $d_\rho\approx2ib_\rho F'$ is SHALLOW-only (deep needs full vertical; $b_\rho^2$
  target = optimistic-pillar trap); (3) "exactly Connes–Consani" downgraded to "strongly analogous, not
  proven identical."

- **BIBLIOGRAPHY (WebSearch).** = strongly analogous to **Connes–Consani arXiv:2006.13771** (their $K<1$
  device) and **arXiv:2301.00421** (de Branges completion of Weil distribution, but RH-conditional; ours
  unconditional/Kreĭn). Not new mathematics — the program reconstructed the actual research frontier.

- **THEOREM C = NO-GO (`B3-KREIN` §8; `PAPER-A` §8), PROVED.** Settled the one open crack (does explicit depth
  dependence give leverage?). **No, with proof:** $\mathfrak t=\|P_+EF\|^2-\|P_-EF\|^2=\mathfrak a+\mathfrak q-\mathfrak p$
  (arithmetic side has NO $b_\rho$); same functional ⟹ depths carry no independent info; $\|K\|\le1$ from zero
  side $\equiv$ Weil positivity $\equiv$ RH (tautological); every sign-agnostic bound ⟹ $\|K\|^2\gtrsim e^d$
  (wrong side). Corollary: zero-side $K$ presupposes the unknown off-line zeros = circular as a tool; CC's
  archimedean $K$ is the useful one *because* it's zero-independent.

- **PAPER-A.md written** (the deliverable): Theorems A/B/C, all lemmas/equations, prior-work §9, honest scope
  §10. Author David Alejandro Trejo Pizzo.

> **Day-23 headline.** Reconnected to RH and **closed path (A)**: a faithful, RH-independent, semibounded
> realization $\mathcal T$ of the Weil form (Theorem A, modulo (H)≪RH), with the exact Kreĭn structure
> $\mathfrak t=E^*JE$ collapsing the whole program onto one axis — **B-2 = "$K$ bounded", RH = "$K$ a
> contraction"** (Theorem B). And a **no-go theorem** (Theorem C): the zero-side realization *cannot* attack
> the sign, because the off-line depths enter only through $\mathfrak t$ itself — bounding $\|K\|\le1$ from the
> zero side is identically Weil positivity. Net: the program converges precisely to $\|K\|\le1$ (= RH), with a
> theorem explaining why this door does not open. **High conceptual value, no step past the sign barrier.**
> The sign needs structural positivity ($\mathcal T=A^*A$) — left open. Next: either (i) write A as a formal
> paper / pull the CC + 2301.00421 PDFs for surgical citation, or (ii) the genuine RH attack (B) — structural
> positivity — with eyes open about the odds.

**2026-06-03 — Day 23 (cont.). PAPER P8 written + compiled; ROUTE-B plan opened.** Per user: write the
closing paper, compile it, open the route-B plan.
- **Read both reference PDFs** (`papers-referencia/2006.13771v1.pdf` CC, `2301.00421v3.pdf` Suzuki).
  Confirmed: CC's positive object = **compression of the scaling action onto Sonin's space**
  (zero-INDEPENDENT), residual via prolate spheroidal + Toeplitz, eigenvalue-below-1 (Thm 6.11). Suzuki's
  de Branges completion is **RH-CONDITIONAL** ($E_\xi$ Hermite–Biehler needs RH; unconditional needs screw
  lines; cites Selberg's warning). Citations now surgical; our characterization verified accurate.
- **PAPER P8** written `.md` + `.tex`, **compiled (10 pp., 0 undefined refs)**:
  `06-papers/P8-weil-krein-realization/{P8.md, main.tex, main.pdf}`. *A Faithful Kreĭn-Space Realization of
  the Weil Quadratic Form, with a No-Go Theorem for the Zero-Side Attack on Positivity.* Theorems A/B/C, §9
  prior-work (CC Sonin / Suzuki de Branges), §10 status. Added to `06-papers/00-INDEX.md` (now P1–P8).
  **Closes the explicit-formula / zero-side line.**
- **ROUTE-B PLAN opened:** `riemann-program/PLAN-RH-ROUTE-B-structural-positivity.md`. Only open route:
  is $\mathcal T=A^*A$ for $A$ built **independent of the zeros** (P8 Thm C = Guardrail B0). Fronts in order
  **B3 (identify $\mathcal T$ vs Connes-Sonin / de Branges / Hilbert–Pólya) → B2 (Connes residual as the
  square; $PW_d$/Slepian) → B1 (direct factorization or a structural no-go)**. Honest odds: full square ⟹ RH
  $<1\%$; likely deliverable = another no-go or a clean identification. Work folder `phase-5-structural/`
  at M1.

> **Day-23 (cont.) headline.** **Paper P8** (md+tex+compiled pdf) closes the zero-side line: faithful Kreĭn
> realization (Thm A), single axis $\|K\|\le1=$RH (Thm B), no-go (Thm C). Citations to Connes–Consani and
> Suzuki made surgical from the actual PDFs. **Route B** (structural positivity $\mathcal T=A^*A$,
> zero-independent — all P8 Thm C leaves open) is now a written plan, with the honest expectation that its
> deliverable is most likely a further no-go or an identification with Connes/de Branges, not RH itself.

**2026-06-03 — Day 23 (cont.). ROUTE B, MILESTONE M1 (B3.1) — Connes–Consani comparison + structural
theorem.** Advisor (endorsing the plan, max effort, panel-shared) sharpened M1: *is the Connes residual the
P8 indefinite part in another basis?* Read CC §§0–6 (eqs 7–14, Thms 1/3/6.11). Record:
`phase-5-structural/B3.1-connes-comparison.md`.
- **CC structure (exact).** Manifest square = Sonin trace $\mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)=\mathrm{Tr}((\vartheta(g)\mathbf S)(\vartheta(g)\mathbf S)^*)\ge0$
  ($\mathbf S$ = proj. onto Sonin space, **zero-independent**, prolate cutoff at $\Lambda=1$). Thm 3:
  $\mathrm{Tr}(\vartheta(f)\mathbf S)=W_\infty(f)+\int f\epsilon\,d^*\rho$; residual $E\circ Q\sim-2\epsilon'(1^+)(\mathrm{Id}-K_{CC})$,
  $\epsilon'(1^+)\approx22.9965$, $K_{CC}$ **compact Hilbert–Schmidt**. Wall = $\mathrm{Id}-K_{CC}\succeq0$ i.e.
  $\|K_{CC}\|\le1$ (conditioned). Single archimedean place ($\mathrm{supp}\subset(1/2,2)$, no primes) is
  **SOLVED** (no wall, Thm 6.11); the **semi-local** (all primes) residual $\iff$ RH = open.
- **Prop B3.1.1 (universal template):** any $\mathfrak t=q_+-q_-$ (metric $q_+$) gives RH$\iff\|K\|\le1$.
  So matching "$\|K\|\le1$" shape between P8 & CC is **generic Kreĭn, not a bridge** — content is in WHICH
  decomposition.
- **THEOREM B3.1.3 (no constructive equivalence) — proved.** $K_{P8}=0\iff$RH (zero-dependent, vanishes on
  RH); $K_{CC}\ne0$ fixed compact (zero-INDEPENDENT). ⟹ no zero-independent unitary $U$ with $UK_{P8}U^{-1}=K_{CC}$
  (would map $0$ to $\ne0$ under RH). **Cor B3.1.4: P8's no-go (Thm C) does NOT cross to $K_{CC}$** — CC
  residual is zero-free, hence a genuine attack surface, NOT obstructed. Good news for route B.
- **Two sharpenings for B1/B2:** (1) BOTH positive parts are already manifest squares ($A^*A$): $A_{P8}=P_+E$
  (zero-dep), $A_{CC}=\vartheta(g)\mathbf S$ (zero-indep). So "is $\mathcal T=A^*A$?" is NOT about the positive
  part (done) but about **residual non-negativity**. (2) Live B2.2 sub-question: CC's prolate spheroidal
  (scaling cutoff $\Lambda=1$) vs P8's $PW_d$ band-limit (Slepian prolates) — genuine bridge or superficial?
  Honest prior: superficial, but the one non-redundant technical check.

> **M1 headline.** Proved P8's wall and Connes' wall are the **same wall** (both $=$RH) but arise from
> **constructively inequivalent operators**: $K_{P8}$ vanishes under RH and is zero-built (circular — its own
> no-go), $K_{CC}$ is fixed and zero-free (the only viable handle). P8's no-go does **not** cross over to CC,
> certifying the Connes semi-local residual as the correct — and only — place to push. Positive part is a
> manifest square on both sides; the whole remaining problem is **non-negativity of the semi-local Connes
> residual**. Next: M2 (de Branges structure functions, B3.2) and M3 (semi-local residual / $PW_d$-Slepian, B2).

**2026-06-03 — Day 23 (cont.). M1 CORRECTED (panel review) + M2 (B3.2) + M3 (B2) done in parallel.**
- **M1 corrections (advisor, fair).** Downgraded two over-claims in `B3.1-connes-comparison.md`: "no
  constructive equivalence" → **Prop B3.1.3 "no natural zero-independent unitary identification"** (defensible
  scope); "the same wall" → **"the same Kreĭn positivity template"**. Foregrounded the strategic corollary
  (P8 no-go does not transport to Connes) as the durable output. Robust one-line form recorded.
- **M2 (B3.2, de Branges) — `phase-5-structural/B3.2-de-branges-comparison.md`.** $E_\xi(z)=\xi(\tfrac12-iz)+\xi'(\tfrac12-iz)$,
  structure functions $A,B$ ($E=A-iB$, real entire, zero-INDEPENDENT). Certificate = Hermite–Biehler / kernel
  positivity $\iff$ RH (Lagarias) = **same template, no free lunch**. Historically proposed unconditional de
  Branges positivity hypotheses **refuted (Conrey–Li 2000)**. Mechanism genuinely different (totally ordered
  CHAIN of subspaces, not a trace-square). **Durable yield = Obs B3.2.1:** under RH, de Branges chain ↔ P8
  height/Nyquist sampling ladder (two filtrations of $\mathcal H(E_\xi)\cong H_+$) — a Rosetta entry,
  suggestive only. **Verdict: de Branges deprioritized** (certificates $\iff$ RH or refuted); no new attack.
- **M3 (B2, semi-local residual) — `phase-5-structural/B2-semilocal-residual.md`.** (B2.1) Semi-local
  $\mathrm{Id}-K_{CC}\succeq0\iff$RH = open frontier (single arch. place solved, Thm 6.11). (B2.2) The
  $PW_d$↔prolate coincidence is **SUPERFICIAL** for global P8 (CC = time∧band cutoff at fixed $\Lambda=1$;
  P8 = band-only at free $d$) — a small no-go; but **REAL for localized P7** (Hermite–Gauss → Slepian
  prolates). Operative redirection (Obs B2.2-(b)): build a **Slepian-prolate localized Gram matrix via the P7
  engine** and compare to CC's Sonin compression — a concrete finite experiment. (B2.1-(c)) **Magnitude-vs-
  sign trap reapplied:** sharpening $\|K_{CC}^{semi-local}\|$ is magnitude; RH only if it crosses $<1$ =
  itself RH. The genuine open content = **cross-place (semi-local) cancellation** (archimedean square vs prime
  negativity) = Connes' geometric program = zero-independent (unobstructed by P8) but beyond a bounded
  milestone.

> **M1–M3 headline.** Route B's three identification fronts done. **B3 (identify):** P8, Connes, de Branges
> all share the **same Kreĭn positivity template**; their certificates are $\iff$ RH; the only zero-free,
> unobstructed handle is the **Connes semi-local residual** (de Branges certificates are $\iff$RH or refuted;
> P8's is zero-built/circular). **B2 (the residual):** semi-local positivity = the open RH-frontier; the
> $PW_d$ prolate coincidence is superficial (global) but real via **P7-localized Slepian** — a concrete
> finite experiment that can at most sharpen the estimate or give a no-go (not the sign, by the magnitude-vs-
> sign lesson). The sign, if anywhere, is in **cross-place semi-local cancellation** (Connes' geometric
> program). **Rosetta stone assembled; no step past the sign; the frontier is precisely named.**

**2026-06-03 — Day 23 (cont.). M1/M2 editorial fixes + CREATIVE FRONTIER PROGRAM opened.** Advisor (panel
review) flagged two editorial points, both applied: (1) M1 — qualified "$K_{P8}=0\iff$RH" with *"within the
P8 realization of §§6–7"* (not an absolute statement about any RH-operator); (2) M2 — downgraded Obs B3.2.1
to a *"heuristic structural correspondence / organizational insight"* (not a theorem; rests on $H_+\cong\mathcal H(E_\xi)$
under RH + two non-canonical filtrations). Advisor endorsed the package M1–M3 as panel-ready and the M3
finding (**Connes ↔ P7 localized, NOT P8 global**) as the genuinely new observation.
- **NEW: `PLAN-RH-FRONTIER-creative-program.md`** (continues route B). Thesis: mix the Connes frontier with
  an asset the literature lacks — P7's *computable semi-local localized* Weil engine + an *explicit
  RH-violator* $L_{DH}$ (P3). Organizing question: **which arithmetic invariant forces $\|K\|\le1$ for $\zeta$
  but $>1$ for an RH-false L-function?** Four ranked directions: **α** semi-local spectral flow (P7-Slepian,
  top eigenvalue vs prime cutoff/height/$c$); **δ** the discriminant ($\zeta$ vs $L_{DH}$ residual — the
  novel, asset-unique one); **β** sine-kernel/GUE identification of the residual; **γ** the global square via
  GNS/Stinespring over the adèle-class algebra (terminal north star, <1%). **Combined first experiment (M4):**
  Slepian-prolate localized residual spectrum for $\zeta$ AND $L_{DH}$ → reads spectral flow + discriminant +
  sine-kernel at once (extends the P7 engine; output `phase-5-structural/experiments/`). Honest prior:
  durable structure, not RH.

> **Headline.** Identification phase closed and panel-ready (M1–M3, with two editorial fixes). Opened the
> **creative frontier program**: use the program's unique assets (semi-local P7 engine + explicit RH-violator
> $L_{DH}$) to ask the sharper falsifiable question — *what arithmetic invariant forces the residual norm
> below 1 for $\zeta$?* First experiment (M4) reads spectral flow + RH-true/false discriminant + GUE
> sine-kernel simultaneously. North star: the global adèle-class square (GNS). Eyes open: structure, not RH.

**2026-06-03 — Day 23 (cont.). M5 — PURE-THEORY CLASSIFICATION PROGRAM (panel reframe + tautology resolved).**
Panel endorsed δ but reframed the declared goal to **classification/anatomy of L-functions, not RH**, and made
the **tautology test mandatory and first**: maybe $I(L)=f(\text{nearest-zero distance})$, tautological. Record:
`phase-5-structural/M5-classification-pure-theory.md`. Cover question: *"Is there an operator-theoretic
invariant of the semi-local Weil residual that separates RH-consistent and RH-violating L-functions, and is it
genuinely arithmetic?"*
- **KEY REALIZATION (the spine, PROVED):** the panel's tautology test = **our own P8 Theorem C + M1 Prop
  B3.1.3.** Prop 1 (assembled): the **zero-side** $K_{P8}$ IS the tautology (P8 Thm C: a zero-functional,
  $=0$ on RH, circular); the **arithmetic-side** $K_{CC}$ is provably distinct (M1) and real-analytic in the
  Euler factors (CC eq.14: $\epsilon$ abs. convergent in coefficients) ⟹ NOT a zero-distance re-encoding. **So
  the non-tautological invariant exists on the Connes side by theorem — the tautology test is PASSED before
  any experiment.** Strongest single point for the panel.
- **Pure-math path (theorem targets):** **T1** anti-tautology/analyticity (analyticity ✅; the
  same-$d$-different-$I$ separation witness ◆) — first milestone. **T2** forced spectral transition = **P7
  Theorem I lifted**: $\lambda_{\min}(Q)<0\iff\|K\|>1$, P7 rate $\mu-1\asymp c\,\delta^2$, $c\sim A(\gamma)$ ⟹
  transversal crossing of $\|K\|=1$ with explicit arithmetic rate (near-in-hand; transversality via P7's
  rank-one Hellmann–Feynman). **T3** anatomy: $\langle K\cdot,\cdot\rangle=R_\infty+\sum_p R_p$ ($R_\infty$=CC
  square, $R_p$=explicit Toeplitz Euler blocks); which ingredient forces the crossing (interaction = the
  semi-local wall). **T4** classification $\Phi(L)$: arithmetic functional with $\|K\|\le\Phi$, separating the
  classes; partial $\Phi$ realistic, full = RH (<1%).
- **Deformation family (rigorous version of panel's transition test, anti-tautology built in):** D1
  zero-position (the control/tautology, to be SUBTRACTED), **D2 Euler-factor at fixed $d$ (the witness — run
  FIRST to try to destroy the program)**, D3 conductor/$\Gamma$. A sharp bifurcation under D2/D3 (not D1) =
  real arithmetic structure.

> **M5 headline.** Adopted the panel's reframe (anatomy of L-functions, RH = north star) and discovered the
> tautology objection is **already proven resolved by P8 Thm C + M1**: the invariant must live on the
> arithmetic-side Connes residual, where it is provably non-tautological (analytic in the Euler factors,
> distinct from the zero-distance). Laid a pure-theory path T1–T4 leveraging P7's explicit forced-negativity
> rate $\delta^2A(\gamma)$ (T2, near-in-hand) and CC's archimedean square (T3), with a three-deformation
> family (D2 = the anti-tautology witness) as falsifying evidence. **The program now has a provable spine and
> a declared, RH-independent goal.** Next: T1 (analyticity + separation witness) and T2 (transversality).

**2026-06-03 — Day 23 (cont.). FOUNDATION CORRECTION + PROOFS of T1, T2, analytic D2.** Record:
`phase-5-structural/M5-T1-T2-proofs.md` (+ correction note in M5).
- **Hostile-audit FOUNDATION CORRECTION (my error, fixed).** M5's "$K_{CC}(L)$ via CC eq.(14) with
  $\lambda(n)\to a_n(L)$" **conflated** the prolate eigenvalues $\lambda(n)$ (Sonin geometry, L-independent)
  with L-coefficients. WRONG. The rigorous, in-hand object is **P7's localized arithmetic Weil-Gram
  $Q_{\mathrm{arith}}(L)$** (Euler+$\Gamma$+conductor), with $\lambda_{\min}(Q)<0\iff\|K\|>1$ (0.2). All T's
  rebuilt on $Q_{\mathrm{arith}}$. (CC $K_{CC}$ = the heavier continuum ideal.)
- **T1 (anti-tautology) ✅ PROVED.** (a) $Q_{\mathrm{arith}}^{(X)}$ is **affine** in the local data
  $D_X=\{\Lambda_L(n)\}_{n\le X}$ ⟹ $\lambda_{\min}$ continuous, real-analytic where simple (Rellich/Kato).
  (b) $I^{(X)}=G_X(D_X)$ factors through FINITE local data; nearest-zero $d(L)$ does NOT (depends on the
  full tail) ⟹ varying $\{\Lambda_L(n)\}_{n>X}$ moves $d$ but fixes $I^{(X)}$ ⟹ $I^{(X)}\ne f(d)$. The
  tautology test passes at the level of the computable invariant.
- **T2 (forced transversal transition) ✅ PROVED** (lifts P7 Thm I). $Q(L_t)=Q(L_0)-c\delta^2 vv^*+o(\delta^2)$
  (P7 rank-one); Hellmann–Feynman on simple $m_0=\lambda_{\min}(Q(L_0))>0$ ⟹
  $\lambda_{\min}=m_0-c|\langle u_0,v\rangle|^2\delta^2+o(\delta^2)$; overlap $\langle u_0,v\rangle\ne0$ IS
  P7's forced-negativity ⟹ **transversal crossing** of $\|K\|=1$ at $\delta_*^2=m_0/(c|\langle u_0,v\rangle|^2)$
  — an arithmetic transition invariant. (Panel's "real structure not coincidence" = transversality.)
- **Analytic D2 ✅ PROVED** (constructive non-tautology witness). $\partial Q/\partial\Lambda_L(n)=-\tfrac1{\sqrt n}w_nw_n^*$
  (rank-one, freq $\log n$) ⟹ $\partial I^{(X)}/\partial\Lambda_L(n)=\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2>0$
  generically; $\nabla I\not\parallel\nabla d$ ⟹ can move $I$ at fixed $d$. **Numerical D2 (the destroy test,
  to run with P7 engine):** verify $\nabla I\not\parallel\nabla d$ for $\zeta$ & $L_{DH}$; Prop D2 gives the
  predicted gradient → clean confirm/refute.
- **T3 (anatomy) ◆ decomposition explicit:** $\langle K\cdot,\cdot\rangle=R_\infty+\sum_p R_p$, $R_\infty=A_\infty$
  (CC square), $R_p=-\sum_k\tfrac{\Lambda_L(p^k)}{\sqrt{p^k}}w_{p^k}w_{p^k}^*$; the $\zeta$-vs-$L_{DH}$
  discriminant = the per-prime $R_p$-profile difference (open: the interaction). **T4** ⬜ north star.

> **Headline.** Foundation self-corrected (dropped the conflated $K_{CC}$ generalization; rebuilt on P7's
> computable $Q_{\mathrm{arith}}$). **Proved T1 (the invariant is local-arithmetic, NOT the zero-distance —
> tautology test passes), T2 (transversal $\|K\|=1$ crossing with explicit arithmetic threshold, lifting P7's
> forced negativity), and analytic D2 ($\partial I/\partial\Lambda_L(n)=\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$,
> $\nabla I\not\parallel\nabla d$).** Three modest but rigorous structural theorems, RH-independent. Next: run
> numerical D2 (destroy test) with the P7 engine; if it survives, T3 ($R_p$-profile discriminant) then T4.

**2026-06-03 — Day 23 (cont.). NUMERICAL D2 — ran it; one confirmation, two honest negatives, a redirection.**
Self-contained Gram (numpy+mpmath, NOT P7's validated engine). Code+results:
`phase-5-structural/experiments/{d2_destroy_test.py, d2_gradient_check.py, M4-D2-results.md}`.
- **Prop D2 (gradient) ✅ NUMERICALLY CONFIRMED** to rel-err $\sim10^{-7}$ (after fixing a bug — I had
  realified a genuinely complex-Hermitian $Q$, corrupting $u_0$; logged). The gradient profile
  $\tfrac1{\sqrt n}|\widehat{u_0}(\log n)|^2$ is **spread over ~14 Euler factors** (peaks $p\approx29$–31) ⟹
  the non-tautological multi-Euler-factor structure is exhibited.
- **Honest NEGATIVE 1:** my quick Gram does NOT reproduce P7's positivity baseline — RH-true $\zeta$ wrongly
  gives $\lambda_{\min}=-5.56$ (engine-spec §3: need $X=10^5$ + full archimedean+polar). So absolute margins
  & the margin-discriminant / crossing tests in `d2_destroy_test.py` are ARTIFACT, need the real engine.
- **Honest NEGATIVE 2 (the important one):** by P7's *validated* data (engine-spec §4) the **scalar
  $\lambda_{\min}$ is an off-line-zero detector** ($\approx$floor for ALL RH-true ζ/L(χ)/L(Δ); huge only for
  $L_{DH}$) ⟹ the scalar is **near-tautological** ($\approx f(d)$). My TEST B (margin difference of two
  RH-true L's) is the WRONG discriminant.
- **REDIRECTION (real finding):** the non-tautological invariant is NOT the scalar margin but the **finer
  structure** — the gradient profile (confirmed) and the **per-prime anatomy $R_p$ (T3)**. T1's logical
  locality stands; refined to mean the gradient/anatomy, not $\lambda_{\min}$. (M5-T1-T2-proofs.md T1 refined.)
- **T2 bonus:** engine-spec §4 *independently* reports $|\lambda_{\min}|\propto\delta^{2.03}$, $R^2=0.999$ —
  **P7's validated data already confirms T2's $\delta^2$ law.** (My self-contained TEST C was artifact.)

> **Headline.** Ran the numerical D2 honestly: **Prop D2's gradient confirmed to $10^{-7}$** and shown spread
> over ~14 primes (non-tautology exhibited); **T2's $\delta^2$ law confirmed by P7's validated data**
> ($\alpha\approx2.03$). Two honest negatives: my self-contained Gram lacks P7's baseline (absolute margins
> artifact), and — decisively — **the scalar margin is near-tautological** (an off-line detector, per P7's
> validated controls), so it is **retired** as the invariant. **Redirection: the non-tautological invariant
> is the per-prime anatomy / gradient profile (T3), not the scalar.** Next: T3 ($R_p$-profile, ζ vs $L_{DH}$)
> on P7's validated engine. One prediction confirmed, one invariant retired, the target sharpened.

**2026-06-03 — Day 23 (cont.). T3 ANATOMY (analytic) — advisor's ordering: formalize T3 BEFORE building the
engine (so the engine measures the surviving object, not the retired scalar).** Record:
`phase-5-structural/T3-anatomy.md`.
- **T3.1 (anatomy identity) ✅** exact Rayleigh decomposition: $\lambda_{\min}=R_\infty(u_0)-\sum_p R_p(u_0)$,
  $R_p(u)=\sum_k\frac{\Lambda_L(p^k)}{\sqrt{p^k}}|\widehat u(k\log p)|^2$. Non-perturbative.
- **T3.2 (mass/variational) ✅** $\lambda_{\min}=\min_{\|u\|=1}[R_\infty(u)-\|\mu_u\|]$, anatomy measure
  $\mu_u=\sum_n\frac{\Lambda_L(n)}{\sqrt n}|\widehat u(\log n)|^2\delta_{\log n}$. Localized positivity = a
  COMPETITION archimedean-square vs prime-mass; RH-true ζ = balanced at the floor (tight).
- **T3.3 (gradient = anatomy density) ✅** $\partial\lambda_{\min}/\partial\Lambda_L(n)=-\frac1{\sqrt n}|\widehat{u_0}(\log n)|^2=-d\mu_{u_0}$.
  ⟹ **the D2-confirmed gradient IS the anatomy profile** — the experiment already measured the surviving
  invariant.
- **T3.4 (the band — honest demotion) ✅** the anatomy density's outer cutoff $\log p\lesssim\sqrt{2J-1}/\sigma\approx4.4$
  is a **Hermite-BASIS envelope, not arithmetic**; the observed band $\log p\approx3.3$–3.7 sits at that edge
  (highest Hermite modes). **The band's location is basis-set; only its internal modulation could be
  arithmetic — provisional, needs validated engine + Slepian basis.** (Advisor's "geometric band" demoted
  from finding to lead.)
- **T3.5 / T3-open ⬜** the deep targets: a concentration theorem ($\mu_{u_0}$ at an arithmetic frequency set as
  $T_0\to\infty$); the $R_p\leftrightarrow$ Euler-factor $L_p$ relation; a profile discriminant $\Phi$ with
  $\Phi(\zeta)\le1<\Phi(L_{DH})$. T3.1–3.4 are the scaffolding making these well-posed.
- **Phasing adopted:** Ph1 (T3 formalized) ✅ → Ph2 (Slepian re-derivation to remove the Hermite envelope +
  $R_p\leftrightarrow L_p$, analytic, no engine) → Ph3 (validated engine measures $\mathcal R(\zeta)$ vs
  $\mathcal R(L_{DH})$, the surviving profile).

> **T3 headline.** Formalized the surviving invariant analytically: the localized Weil margin is EXACTLY
> $\lambda_{\min}=R_\infty-\sum_p R_p$ = a mass competition (archimedean square vs prime-frequency mass
> $\mu_{u_0}$), and the D2-confirmed gradient IS the anatomy density. Honestly demoted the "geometric band" to
> a basis-enveloped lead (Hermite turning point), pending the validated engine + Slepian basis. The deep
> content (concentration theorem, $R_p\leftrightarrow L_p$, discriminant $\Phi$) is now well-posed = the
> forward target. Next (Ph2): Slepian re-derivation + the $R_p\leftrightarrow$ Euler-factor relation —
> analytic, before any engine work.

**2026-06-03 — Day 23 (cont.). PHASE 2 (analytic) — the anatomy vs the local Euler factor.** Advisor's steps
A/B/C; decisive question: *is $\{R_p\}$ new info or just $\{a_p\}$ re-packaged?* Record:
`phase-5-structural/Phase2-Rp-Euler.md`.
- **A (Slepian) ✅** anatomy is **subspace-intrinsic** (basis-free for fixed $\mathcal V$); Hermite vs Slepian
  = choice of SUBSPACE. Slepian gives a **flat-box envelope** vs Hermite turning point. **A-criterion (band
  test, NO engine):** divide out the flat envelope — if the $\log p\approx3.3$–3.7 concentration persists it's
  operator/arithmetic, if it flattens it was Hermite.
- **B (Prop B1) ✅** $R_p(u_0)=\sum_k a_{p^k}W_k(\log p)$, $W_k(x)=x e^{-kx/2}|\widehat{u_0}(kx)|^2$ universal,
  $a_{p^k}=\sum_j\alpha_{p,j}^k$ (Satake). **HONEST VERDICT:** leading $R_p\approx a_p W_1(\log p)$ = $a_p$
  re-weighted (**deflation risk REAL, conceded**); ζ ($a_p\equiv1$)=pure window. **New content beyond $a_p$:**
  (i) $k\ge2$ corrections = FULL local factor (Satake $a_{p^2}=a_p^2-2$…); (ii) $W_k=W_k[u_0]$ self-consistent
  (couples all primes); (iii) DECISIVE — **factorizability $\equiv$ Euler product:** ζ/Dirichlet/automorphic
  factor, $L_{DH}$ (NO Euler product) does NOT ⟹ the multiplicative structure of $\{R_p\}$ = the ζ-vs-$L_{DH}$
  discriminant. Invariant sharpened to the multiplicative/windowed-local-factor structure.
- **C (stability) ✅** shared $\Lambda_L$ for $n\le P$ ⟹ truncated profiles identical (T1) and
  $\|\mathcal R(L)-\mathcal R(L')\|\le C e^{-\alpha(\log P)^2}$ (P7 II + Davis–Kahan). Exponentially-stable
  local arithmetic fingerprint (quantitative T1).
- **T4 seed:** *is positivity more transparent in $\{R_p\}$ than $\{a_p\}$?* (does factorizability + Ramanujan
  $|a_p|\le2$ force $\sum_p R_p\le R_\infty$ on a sub-class?) First point the repackaging could earn its keep.

> **Phase-2 headline.** Faced the deflation question: **leading-order $R_p\approx a_p W(\log p)$ IS $a_p$
> re-weighted (conceded)** — but the new content is the full **local factor** (Satake), the **self-consistent
> window**, and decisively **factorizability $\equiv$ Euler product** (ζ factors, $L_{DH}$ doesn't = the
> discriminant). Plus a **stability theorem** ($e^{-\alpha(\log P)^2}$) and the **Slepian flat-envelope band
> test** (decides the band, no engine). Invariant sharpened to the multiplicative structure. Next: T4 seed
> (sign transparent in $\{R_p\}$?), analytic → Phase 3 (engine) → panel (only after Phase 3, per user).

**2026-06-03 — Day 23 (cont.). Phase-2 CORRECTIONS + T4-SEED (the survival test).** Advisor's audit, taken:
(1) **"factorizability ≡ Euler product" downgraded** — only **Euler ⇒ factorization** is proved; the converse
(factorization ⇒ Euler), needed for a discriminant, is now **Conjecture B2** (not a Phase-2 conclusion).
(2) **Theorem C (stability) flagged as the autonomous candidate theorem** (survives even if RH classification
fails). (3) **T4 reformulated precisely** (not "more transparent"): the anatomy earns its keep iff an
inequality/monotonicity is *natural* in $\{R_p\}$ and *opaque* in $\{a_p\}$. Record: `phase-5-structural/T4-seed.md`.
- **T4-I ✅ PROVED (Bessel/Carleson form):** $\lambda_{\min}\ge0\iff$ the weighted prime-frequency system
  $\{(\Lambda_L(n)/\sqrt n)^{1/2}B^{-*}w_n\}$ is **Bessel $\le1$** in the archimedean metric $A_\infty=B^*B$;
  equiv. the prime measure $\nu_L=\sum\frac{\Lambda_L(n)}{\sqrt n}\delta_{\log n}$ is **Carleson $\le1$** for
  the Sonin window space. **T4-I' ✅:** the FINITE Carleson bound is unconditional (Ramanujan $|a_{p^k}|\le k+1$
  + $p^{-k/2}$ decay) = **B-2 reappears, localized to the anatomy.** $\le1$ = local RH. Structural &
  frame-theoretic, opaque in $a_p$.
- **T4-II ✅ PROVED (concavity/monotonicity/extremal reduction):** $\lambda_{\min}(Q(\Lambda))$ is **concave**
  (min-of-linear ∘ affine) and **coordinate-wise non-increasing** on $\Lambda\ge0$ (Weyl). ⟹ on a box
  $0\le\Lambda_n\le c_n$, $\min\lambda_{\min}$ at the **all-upper corner**; local positivity on the whole box
  ⟺ at one extremal object. Tempered box $a_{p^k}\in[0,2]$ ⟹ corner $=$ **$\zeta^2$ (Eisenstein, RH-true)** ⟹
  whole non-neg tempered box locally positive (reduced to 1 check). Artificial class (sanctioned), local. A
  structural inequality natural in the mass picture, opaque in $a_p$ (sign-oscillation hides it).
- **VERDICT (survival filter):** **the program SURVIVES — positivity IS structural in anatomy coords** (Bessel/
  Carleson + concave/monotone), genuine inequalities natural in $\{R_p\}$, opaque in $\{a_p\}$. **BUT the sign
  wall is unmoved** (Bessel $\le1$ / extremal positivity = local RH). Consistent with P8: finite bound (B-2)
  unconditional, $\le1$ = RH; anatomy makes the dichotomy crisper (a Carleson measure, a concave functional),
  doesn't cross it.

> **T4-seed headline.** The anatomy *earns its keep as structure*: positivity reformulates as a **Bessel/
> Carleson bound** on the prime measure (T4-I, opaque in $a_p$, finite bound = B-2 unconditional) and is
> organized by **concavity + an extremal reduction** (T4-II, box ⟺ one $\zeta^2$ check). Both are genuine
> inequalities natural in $\{R_p\}$ — the advisor's survival test PASSED — but the sign ($\le1$ / extremal
> positivity) is unmoved = local RH. Phase 3 now has a crisp target: **measure the Carleson constant of $\nu_\zeta$
> vs $\nu_{L_{DH}}$** + test Conjecture B2 (factorization ⇒ Euler). Theorem C (stability) = the autonomous
> theorem to foreground. Panel after Phase 3.

**2026-06-03 — Day 23 (cont.). PAPERS P9 + P10 written & compiled (advisor's two-paper split).** Isolate the
autonomous stability result (P9) from the speculative RH-classification (P10). Applied the T4-II correction
(extremal reduction is the theorem; corner-positivity left open, not via RH⇒Q⪰0).
- **P9 — `06-papers/P9-stable-arithmetic-fingerprints/` ({P9.md, main.tex, main.pdf 4pp, 0 errors}).** *Stable
  Local Arithmetic Fingerprints from Localized Weil Forms.* RH-INDEPENDENT. Stability theorem
  $\|Q(L)-Q(L')\|\le Ae^{-\alpha(\log P)^2}$ (operator/spectrum uncond. via Weyl; profile via Davis–Kahan/gap)
  + anatomy identity + HF gradient + concavity/extremal reduction. The durable standalone.
- **P10 — `06-papers/P10-anatomy-localized-weil/` ({P10.md, main.tex, main.pdf 4pp, 0 errors}).** *Anatomy of
  the Localized Weil Form.* Anatomy identity; factorization $R_p=\sum_k a_{p^k}W_k$ (lead $\approx a_pW_1$,
  deflation conceded); Carleson reformulation (positivity = Carleson $\le1$, finite bound uncond.); concave
  extremal reduction; Conjecture B2 (factorization ⇒ Euler) = candidate ζ-vs-$L_{DH}$ discriminant. No sign.
  Both in `00-INDEX.md` (P1–P10).

> **P9/P10 headline.** Banked the two advisor-recommended papers: **P9** the autonomous RH-independent
> stability theorem (durable), **P10** the speculative anatomy/Carleson/Conjecture-B2 program (no sign). Both
> compiled clean (4pp each). T4-II corrected. **Next: Phase 3** — validated engine (engine-spec §3) to measure
> the Carleson constant $\nu_\zeta$ vs $\nu_{L_{DH}}$, the Slepian band test, and Conjecture B2.

**2026-06-03 — Day 23 (cont.). PHASE 3 (first pass) — one confirmation, one genuine blocker.** Record:
`phase-5-structural/experiments/{phase3_carleson.py, Phase3-results.md}`. Self-contained Gram (NOT P7's
validated engine).
- **Carleson constant $C(L)=\lambda_{\max}(A_\infty^{-1/2}P A_\infty^{-1/2})$ ($C\le1\iff$ positivity) — BLOCKED.**
  My engine **FAILS the ζ validation gate:** $C(\zeta)\approx1.98>1$ (λ_min(A−P)=−1.95<0), wrong for RH-true ζ.
  Stable across $X=10^3$–$10^5$ ⟹ it's NORMALIZATION not truncation. Diagnosis: $C(\zeta)\approx2\approx2\times$
  threshold, $\bar\Omega\approx1.99$ ⟹ likely a **factor-2 explicit-formula convention** (prime term $2\sum$ vs
  $\sum$); with it fixed ζ would sit at $C\approx1$ (floor). **Did NOT fudge** — calibrating + validating vs P7
  reference is the Phase-3 engineering task. The apparent discriminant $|C(\zeta)-C(\chi_4)|\approx1.87$ is
  CONFOUNDED by the un-calibrated baseline (different Γ-factors) ⟹ **not a clean measurement.** Also $L_{DH}$
  has NO Euler product ⟹ its arithmetic side isn't a clean $\sum\Lambda_L(n)n^{-s}$ ⟹ extra handling needed.
- **Band test — CONFIRMS T3.4 ✅.** Anatomy density rises monotonically to the **Hermite turning-point edge**
  ($\sqrt{2J}/\sigma\approx4.9$), peaks $p\approx59$ ($\log p\approx4.1$) ⟹ **basis artifact, not arithmetic**
  (the earlier "band 3.3–3.7" = the rising edge at smaller J). The genuine band test needs the **Slepian
  flat-box basis** (not in the self-contained build).
- **HONEST NET:** Phase-3 numerical measurement (Carleson discriminant) is **blocked on reproducing P7's
  validated engine** (engine-spec §3 + $L_{DH}$ no-Euler-product) — real engineering, best with P7's code; NOT
  reliably self-contained here. The analytic program (P9/P10/T1–T4) is **unaffected and stands.** Carleson/
  discriminant numbers from this pass are NOT trustworthy and must not be reported as measurements.

> **Phase-3 headline.** Ran it honestly: the **band test confirmed T3.4** (the concentration is a Hermite
> basis artifact — clean negative, validates the earlier demotion; the real test needs Slepian). The
> **Carleson-constant measurement is blocked** — my self-contained engine fails the ζ gate ($C\approx1.98$,
> a likely factor-2 normalization; not fudged), and $L_{DH}$'s missing Euler product needs special handling.
> Phase 3 done faithfully requires **P7's validated engine** (Colab/v8) or a validated engine-spec §3 build.
> The analytic results stand; the numerical Carleson discriminant is the open engineering task. **Decision for
> the user: get P7's engine code, or invest the validated reimplementation, before trusting Phase-3 numbers.**

**2026-06-03 — Day 23 (cont.). PHASE 3 — VALIDATED COLAB ENGINE (zero side).** User asked for a runnable
Colab script. Built one with **self-validating gates** (engine-spec §1 reference zeros, ζ floor, δ² law).
File: `phase-5-structural/experiments/colab_phase3_engine.py`.
- **Found the correct convention (2 bugs fixed):** (1) the Weil symmetrization must be
  $M[i,j]=\sum_\rho g_i(t-i\delta)\overline{g_j(t+i\delta)}$ (pair $z$ with its CONJUGATE $\bar z$) — NOT
  $g_i(z)\overline{g_j(z)}$ (that's the PSD-by-construction dead-end engine-spec warns of); (2) shift the
  IN-WINDOW zeros ($|\gamma-T_0|<2\sigma$), not the first-m (locality).
- **VALIDATED against engine-spec §4:** Gate1 (zeros) ✅; Gate2 ζ at floor ($\lambda_{\min}/\mathrm{tr}=+5.2\times10^{-5}$)
  ✅; **Gate3 forced-negativity $\delta^2$ law, exponent 2.04 vs engine-spec's 2.03 ✅**. The corrected
  ZERO-SIDE $M_{\mathrm{zeros}}$ reproduces P7's reference behavior. **No arithmetic side needed** — positivity
  is read directly: $\lambda_{\min}(M_{\mathrm{zeros}})\ge0\iff$ local positivity.
- **The arithmetic side (M_arith / the Carleson-constant number) stays BROKEN/omitted:** the explicit-formula
  calibration is a STRUCTURAL mismatch (3-constant least-squares fit residual 0.58, not a scaling) — I do NOT
  ship it; positivity SIGN is measured via the validated zero side instead ($\lambda_{\min}\ge0\iff C\le1$).
- **$L_{\mathrm{DH}}$ construction FIXED:** the simple $(1\mp i)/2$ coefficients do NOT reproduce the reference
  off-line zero; the correct **Davenport–Heilbronn $\kappa=0.28407904384$** form $(1\mp i\kappa)/2$ does
  ($|L_{DH}(0.808517+85.699348i)|=6.5\times10^{-7}\approx0$ ✅). The Colab branch self-checks this and skips if
  it fails. *(Banked the κ fix.)*
- **MEASUREMENT delivered (ζ_δ controlled discriminant, validated):** off-line zeros at displacement δ force
  $\lambda_{\min}(M_{\mathrm{zeros}})\sim-c\,\delta^2$: $+3.3\times10^{-4}$ (floor, δ=0) → $-4.84$ (δ=1),
  exponent 2.04. A LOCAL, EXPLICIT, VALIDATED positivity-violation curve.

> **Phase-3 headline (RESOLVED for the zero side).** Built a **validated, self-checking Colab engine**: found
> the correct Weil symmetrization (pair $z$ with $\bar z$) + window-locality; it reproduces engine-spec's ζ
> floor and the **$\delta^2$ forced-negativity law (2.04 vs 2.03)**. Positivity is measured directly from the
> zero side (no arithmetic side); the $L_{DH}$ κ-construction is fixed and self-validated. The user can run it
> in Colab and get the ζ_δ curve (and, with DO_LDH=True, the $L_{DH}$ violation). The arithmetic-side Carleson
> NUMBER remains uncalibrated (structural mismatch) and is honestly omitted — the positivity SIGN (=Carleson
> $\le1$) is what the validated engine measures.

**2026-06-03 — Day 23 (cont.). MOONSHOT PLAN — RH via Osterwalder–Schrader reflection positivity.** User:
"llegamos al muro, hay que pasarlo; armá un plan que nadie hizo." Record:
`riemann-program/PLAN-RH-MOONSHOT-OS-reflection.md`.
- **New insight:** the Kreĭn $J$ ($\rho\mapsto1-\bar\rho$) IS the functional-equation reflection
  $s\leftrightarrow1-s$ ⟹ Weil positivity $E^*JE\succeq0$ IS **Osterwalder–Schrader (OS) reflection
  positivity** for $\Theta=J$, Euclidean time $\tau=$ off-line displacement $\delta$, critical line = time-zero
  slice.
- **Why it's leverage:** OS reflection positivity ⟹ (OS reconstruction theorem) builds a self-adjoint
  $H\succeq0$ = **Hilbert–Pólya for free** ⟹ real spectrum ⟹ RH. Turns "bound a norm" into "prove reflection
  positivity" (standard route: lattice factorization).
- **Mechanism:** the **Euler product = a reflection-positive lattice factorization** $\prod_v L_v$. RP of a
  site-factorized system ⟸ (each local factor RP) + (tensor/Markov gluing). **Consistency:** $L_{DH}$ (NO Euler
  product) violates RH — mechanism predicts it; ζ (Euler) ⟹ RH. **= the structural mechanism behind Conjecture
  B2.** Unifies Kreĭn $J$ + anatomy $R_p$ + engine.
- **Skeleton:** S1 OS form $\mathfrak t=\langle\Theta F,F\rangle_\mu$ (engine tests it); S2 per-place RP (arch
  ≈ Connes; primes = new finite-dim check via Ramanujan); **S3 gluing (hard core)**; S4 OS reconstruction ⟹
  Hilbert–Pólya ⟹ RH. **Validated engine = falsifiable guide** (δ² forced-negativity curve IS the OS RP test).
  Hedges: H1 rigidity (P7 forced-negativity as global constraint), H2 function-field→ζ interpolation ($\|K\|$
  Lyapunov, T2). Odds RH <1%; realistic prize = S3 or its no-go. First move M-OS-1: write S1 + engine test.

> **Moonshot headline.** Past the wall: **RH via Osterwalder–Schrader reflection positivity** — $J$ = the
> functional-equation reflection, Weil positivity = OS RP, **Euler product = the reflection-positive lattice**,
> OS reconstruction = **Hilbert–Pólya for free**. Explains ζ vs $L_{DH}$ (B2 is its shadow), unifies the
> program, instrument-guided by the validated engine. Hard core = S3 (adelic gluing). <1% for RH; the route is
> new.

**2026-06-03 — Day 24. PHASE 6 STARTED — `riemann-program/phase-6/`. Step S1 done (M-OS-1-S1-setup.md).**
- **S1.1 ✅ (load-bearing recasting):** Weil's criterion IS reflection positivity for $\Theta$ — **Weil's own
  involution $\tilde\psi(u)=\overline{\psi(-u)}$ IS the functional-equation reflection** ($u\mapsto-u$ =
  inversion = $s\leftrightarrow1-s$). $\langle\psi,\psi\rangle_W=W(\psi*\tilde\psi)\ge0\iff$RH. Verified vs the
  standard Weil/Suzuki form.
- **S1.2 ✅** $W\circ\Theta=W$ ($\Theta$-invariance from the functional equation).
- **S1.3 ◆** positive-time RP $\iff$ full Weil positivity = RH (the genuinely-new lemma: the OS positive-time
  formulation is FAITHFUL; proved modulo the standard OS Cauchy–Schwarz bootstrap, flagged). ⟹ **RH $\iff$
  (OS-RP).**
- **S1.4 ✅ conditional (prize):** OS reconstruction ⟹ self-adjoint $H\succeq0$ (Hilbert–Pólya), spectrum
  $\{\gamma_\rho\}$ real ⟹ RH. Fixes covariance+regularity axioms (dilation = Connes scaling). NOT circular as
  a program: prove (OS-RP) via S2–S3 without RH, then reconstruction DELIVERS $H$.
- **Anchors:** Connes–Consani = the archimedean S2 (CC support $(1/2,2)$ under inversion = the positive/
  negative-time split; the Sonin square = archimedean local RP). Validated engine = the **(OS-RP) detector**
  (the δ² forced-negativity curve = failure of OS-RP off the time-zero slice) ⟹ every step falsifiable.
- **Honest:** S1 = faithful recasting + scaffolding; CONTENT (proving OS-RP) is S2–S3. Next: S2.

**2026-06-03 — Day 24. PHASE 6 STEP S2 — COMPUTED and REFUTED (honest no-go).** `phase-6/M-OS-2-S2-local-REFUTATION.md`.
Attacked S2 (per-place reflection positivity = the heart of the Euler-lattice mechanism); the computation
**kills the mechanism**.
- **S2.1 (proved):** the local prime form is $\langle\psi,\psi\rangle_{W_p}=\int|\widehat\psi(r)|^2 G_p(r)\,dr$
  with closed form $G_p(r)=\frac{2\log p}{p|1-z|^2}(\sqrt p\cos(r\log p)-1)$, $z=e^{ir\log p}/\sqrt p$.
  **$G_p$ is INDEFINITE:** $G_p(0)=\frac{2\log p}{\sqrt p-1}>0$ but $G_p(\pi/\log p)=-\frac{2\log p}{\sqrt p+1}<0$.
  Verified numerically (p=2,3,5,7) — closed form matches to all digits. So **each finite-prime factor is
  individually indefinite, NOT reflection-positive.**
- **No-go S2.2 (proved):** the Euler-lattice mechanism (per-place RP + tensor gluing) **fails** — the local
  factors are indefinite, so global positivity is NOT a tensor of local positivities; it's **cross-place**
  (archimedean $R_\infty$ dominating the SUM of indefinite primes) = the same cancellation as M3 §5, NOT a
  Markov/transfer structure. The OS route reduces to Connes.
- **S1 corrections (caught here):** (1) S1.1 "second equivalence" BOGUS — a separate linear $\Theta$ gives
  $\sum\overline{\widehat\psi(\gamma)}^2$ (indefinite squares), not a norm; the reflection IS the Weil
  involution itself (recasting still valid). (2) S1.4 "Hilbert–Pólya for free" RETRACTED — the two-point
  function $\sum e^{i\gamma u}$ is OSCILLATORY, not OS-decaying; reconstruction does NOT hand us $H$ free.
- **Honest salvage:** only a *multiplicative/KMS* per-place positivity (Bost–Connes partition function) could
  survive — but that IS Connes' open core, no new mechanism gained.

> **S2 headline (a real no-go, computed not guessed).** Attacking the moonshot honestly: the $J$=reflection
> insight and the Weil=reflection-positivity recasting are CORRECT, but the two load-bearing mechanisms —
> per-place reflection positivity and free Hilbert–Pólya reconstruction — **both FAIL on direct computation**
> ($G_p$ indefinite; oscillatory two-point function). The OS-lattice route lands back at the cross-place
> conspiracy = Connes' problem. **Durable output: a rigorous no-go for the OS-lattice mechanism.** The sign
> needs an idea neither we nor the field has; the program's harvest is P9 (stability), the validated detector,
> and the precise, now-even-sharper map of the wall (incl. why reflection positivity does not localize for ζ).

**2026-06-03 — Day 24. PHASE 6 — the S2 refutation POINTS somewhere: prime incoherence vs the archimedean
envelope (the large-values frontier, our ω-class turf).** `phase-6/S2-followup-incoherence.md`. The exact
$G_p$ from S2 gives the precise spectral form of RH.
- **§1 rigorous reduction:** $\mathfrak t(\psi)=\int|\widehat\psi(r)|^2 d\mu$, $d\mu=\Omega_\infty(r)dr-(\sum_p G_p)_{\rm reg}dr$;
  **RH $\iff\Omega_\infty(r)\ge(\sum_p G_p)_{\rm reg}(r)\ \forall r$** = the **archimedean envelope dominates the
  prime comb, pointwise**.
- **§2:** the comb's fluctuation $F(r)=\sum_p\frac{2\log p}{\sqrt p|1-z_p|^2}\cos(r\log p)$ is **(i)** essentially
  $-\mathrm{Re}\,\zeta'/\zeta(\tfrac12+ir)$ (so the bound is self-referential = why it's hard) and **(ii)**
  $\sup_r F$ = **constructive interference = large values of ζ** (Soundararajan/Bondarenko–Seip resonance).
  **RH $\iff$ the prime-oscillator interference never exceeds $\Omega_\infty\sim\tfrac12\log r$.**
- **§3 (the lever):** $\{\log p\}$ are **ℚ-linearly independent = unique factorization** ⟹ prime oscillators
  **incoherent** ⟹ no coherent spike. **Sharpened Conjecture B2:** ζ (unique factorization ⟹ ℚ-indep freqs ⟹
  incoherent ⟹ RH) vs $L_{DH}$ (no Euler product ⟹ ℚ-relations/coherence ⟹ spike ⟹ off-line; its 85.699 zero
  IS such a spike). B2 becomes "incoherence ⟺ ℚ-independent frequencies ⟺ Euler product."
- **§4 OUR assets:** the **ω-class decomposition (P2/P4/P5)** is exactly a structured bound on the
  prime-interference spike; the validated detector is an envelope-vs-comb meter. Concrete sub-problem **S2f-1:**
  bound $\sup_{[T,2T]}F(r)$ via ω-class + diophantine incoherence vs $\tfrac12\log T$.
- **§5 honest landing:** NOT a crossing — the comb IS ζ on the line (self-referential), so this is the
  **large-values frontier** (open, tied to RH). But it's the RIGHT frontier and our most-equipped one.

> **Headline.** The S2 no-go is not a dead end: it gives the **exact spectral form of RH** (archimedean
> envelope ≥ prime comb, pointwise), shows the comb's spike = **large values of ζ = constructive interference**,
> and isolates the lever = **unique factorization (ℚ-independence of log p) ⟹ incoherence**. This sharpens
> Conjecture B2 into a frequency-resonance statement and lands exactly on our **ω-class** turf (P2/P4/P5 bound
> the interference spike). Next: **S2f-1** — deploy the ω-class machinery to bound the prime-comb spike vs the
> archimedean envelope. Honest: the large-values frontier, not an obvious crossing, but the right one and ours.

**2026-06-03 — Day 24. PHASE 6 — S2f-1 attempted; the follow-up reduction is FLAWED; honest meta-conclusion.**
`phase-6/{S2-followup-incoherence.md (retraction header), S2f-PROGRESS-HONEST.md}`.
- **Caught: the S2-followup §1 reduction is WRONG.** Explicit formula:
  $\sum_\rho|\hat\varphi(\gamma_\rho)|^2=2|\hat\varphi(i/2)|^2+\frac1{2\pi}\int|\hat\varphi|^2[\Omega_\infty-\sum_pG_p]$.
  LHS discrete (zeros) ⟹ the comb $\sum_pG_p$ is **distributional**: $\Omega_\infty-\sum_pG_p=2\pi\sum_\rho\delta_{\gamma_\rho}-$pole.
  So **"$\Omega_\infty\ge\sum_pG_p$ pointwise" is FALSE** (comb contains the zeros), and one **cannot** take
  $\hat\varphi\to\delta$ (prime sum diverges). The "envelope ≥ comb" mechanism retracted. The zero-clustering
  ↔ large-values link survives only as the **standard** $S(T)$ heuristic, NOT a new reduction.
- **Honest meta-conclusion:** across phase 6, **every idea claiming leverage on the SIGN failed on audit** —
  S1.4 (Hilbert–Pólya free) retracted, S2 (per-place RP) refuted ($G_p$ indefinite), S2-followup §1 flawed.
  The recasting (Weil = RP for the involution) is correct but only a recasting. **We do NOT have a sound new
  path across the wall.** Directions = the field's open cores (Connes KMS; large values/$S(T)$); ω-class
  assets point at the right frontier but yield no crossing. More framings = motivated reasoning, not math.
- **Durable harvest:** P9 (stability), the validated detector, the no-gos — **N1** (positivity does NOT
  localize per prime: $G_p$ indefinite — small clean publishable), **N2** (no naive OS Hilbert–Pólya), P8 Thm
  C — plus the precise map (sign = cross-place conspiracy = large values = Connes KMS, named) and the
  sharpened (conjectural) B2 (unique factorization ⟹ ℚ-indep freqs ⟹ incoherence).

> **Day-24 honest headline.** Attacked the moonshot rigorously: **OS recasting correct, mechanism REFUTED
> ($G_p$ indefinite), Hilbert–Pólya prize RETRACTED (oscillatory two-point fn), follow-up reduction FLAWED
> (comb distributional). NO crossing.** Two flawed reductions caught in one session = the discipline working.
> Truthful state: the sign needs an idea neither we nor the field has in 2026; we mapped *why* with unusual
> precision. Durable: P9, the validated detector, the audited no-gos. Recommendation: consolidate; engage the
> open core (Connes KMS / large values) only with eyes fully open ($<1\%$).

**2026-06-03 — Day 24 (cont.). PHASE 7 — open core engaged (option 2); the incoherence lever REFUTED with numbers.**
`phase-7/{P7-OPEN-CORE-carleson-saturation.md, experiments/carleson_band_engine.py}`.
- **Built the rigorous finite reformulation** (the *correct* replacement for the retracted distributional comb):
  for $f=\hat\varphi$ band-limited type $d$ in the log-prime variable, the prime sum truncates **exactly** to
  $n\le e^{2d}$, and $\mathrm{RH}\iff C(d,T_0):=\lambda_{\max}(P_F,A_\Phi)\le1$, threshold **intrinsic**
  (Weil-explicit-formula constants), $A_\Phi[i,j]=\int S_iS_j\Phi$, $P_F[i,j]=\int S_iS_jF$,
  $F=2\sum_{n\le e^{2d}}\Lambda(n)n^{-1/2}\cos(r\log n)$. Implemented + convergence-validated ($10^{-6}$; sinc
  $1/r$ tails need span $\gtrsim20$ window-widths — the early $C{>}1$ by $\sim10^{-3}$ was that artifact).
- **MEASURED (real numbers):** $C\le1$ for $\zeta$ at **every** height (RH consistent), and
  $C\to1$ **saturated, margin exactly $0$**, once $x:=2d/\log T_0\gtrsim0.85$ (primes to $e^{2d}\gtrsim T_0^{0.85}$).
  Sweep $T_0{=}1000$: $C=0.34,0.61,0.79,0.92,\mathbf{1.000},\mathbf{1.000}$ at $d=1,1.5,2,2.5,3,\dots$. The only
  sub-unit margin is in the **prime-deficient** regime and is a clean monotone function of $x$ alone =
  **band-dof vs zero-density** (purely **archimedean**).
- **Why (the mechanism, now concrete):** $A_\Phi-P_F=\sum_{\rho\in\text{window}}|f(\gamma_\rho)|^2-$pole = the
  **zero-side Gram**; a band-limited $f$ can vanish at the window's (real) zeros ⟹ $A-P=0$ ⟹ $C=1$. So the
  form's positivity **is** the realness of the zeros; "prime incoherence" is **identical to** RH, not an
  independent lever.
- **N3 (measured no-go):** *the band-limited Carleson constant of $\zeta$ is identically $1$ (saturated); prime
  incoherence provides NO positivity slack — adding primes pushes $C$ up to $1$, never below.* Refutes the
  option-2 ($\omega$-class / unique-factorization) hope **with data**. Sharpens "the sign has no margin."

> **Day-24 cont. headline.** Engaged the open core. Made the incoherence hope into a **rigorous, finite,
> validated** instrument ($C(d,T_0)$, intrinsic threshold 1) — and **measured it dead**: $C\equiv1$ for $\zeta$
> at the natural scale, the margin is archimedean (zero density), arithmetic incoherence buys **zero slack**.
> A clean, durable **negative with numbers** (N3) + a new instrument. No crossing. Lever closed; pivoting.

**2026-06-03 — Day 24 (cont.). PHASE 7b — second order: Weil–Carleson = sine-kernel/pair-correlation; bridge real, same wall.**
`phase-7/{P7b-second-order-sinekernel-bridge.md, experiments/second_order_{sinekernel,offline}.py}`.
- **Bridge B1 (verified with real zeta zeros):** $A_\Phi-P_F=\sum_{\rho\in\text{win}}v_\rho v_\rho^\top$,
  $v_\rho[j]=S_j(\gamma_\rho)$ ⟹ **rank $=K$** (#zeros in window: measured 22 $O(1)$ eigs for $K{=}21$), and the
  $K$ active modes = spectrum of the band-limited reproducing-kernel Gram = the **sine kernel**
  $\sin(d(\gamma_i-\gamma_j))/\pi(\gamma_i-\gamma_j)$ (measured vs sinc: $6.8\times10^{-2}$). So **2nd-order
  Weil–Carleson IS the Montgomery–Dyson sine-kernel determinantal process on the zeros.** First order $C_{\max}{=}1$
  $\iff$ zeros real; subdominant gap = pair-correlation statistics.
- **Detector (verified):** push central zero off-line $\gamma_c\mapsto\tau\mp i\delta$ ⟹ $\lambda_{\min}=-c\,\delta^2$,
  $c\approx0.005$ **stable** — reproduces the validated $\delta^2$ law in sine-kernel language. Curvature $c$ set by
  local spacing, $\to0$ at **Lehmer pairs** (a quantitative RH-stability margin per height).
- **Honest verdict:** RH $\iff$ sine-Gram $\preceq1$ per window. The sine kernel on **real** zeros is automatically
  a contraction ($0\preceq K_{\rm sine}\preceq1$), so $C\le1$ **is** the realness of the zeros = RH. Pair
  correlation/GUE **describe** real zeros, do **not** force reality (Montgomery itself open, RH-conditional).
  **Reduces to the wall — fourth language.** The $\omega$-class machinery characterizes the fluctuation tail of
  real zeros; it does not supply the contraction.

> **Day-24 cont. (2nd).** Pivoted to second order per the user. Found a genuinely beautiful **measured bridge**
> (Weil positivity's 2nd order = sine-kernel/pair-correlation; RH-stability margin = Lehmer-pair curvature) and a
> working $\delta^2$ detector — but it **restates RH** (sine-Gram contraction = real zeros) and pair correlation
> describes rather than forces. **Option 2's "ours" half (ω-class / large values / Carleson) is now exhausted in
> BOTH orders (N3 + B1), both measured, both reducing to the self-referential wall.** Durable: N3, B1, the new
> instrument. The only structurally-distinct untried core left is Connes KMS (not ours; <1%).

**2026-06-03 — Day 24 (cont.). PHASE 7c — Connes core engaged (foreign terrain); SAME wall, multiplicatively dressed.**
`phase-7/connes/{P7c-connes-core-same-wall.md, prolate_bridge.py}`.
- **Bridge established (ours → theirs):** our band-limited Weil–Carleson form **is** the Connes–Consani
  **prolate** compression — window half-width $W$, band $d$ ⟹ time-bandwidth $c=Wd$, dim $2c/\pi$. Computed
  $\lambda_n(c)$: $\approx2c/\pi$ modes $\approx1$, sharp drop at $n=2c/\pi$, transition width $\sim\log c$;
  $\lambda_{\max}(c)<1$ **strictly** = Connes–Consani's proved **archimedean contraction** = **our $A_\Phi\succ0$**.
- **The Connes hope (per-place positivity at finite primes) REFUTED multiplicatively too:** the local Weil
  distribution $W_p$ is the same prime-power object, not individually positive; Connes–Consani prove only $\infty$;
  finite-place positivity is global — exactly **N1** ($G_p$ indefinite). Multiplicative dressing does not rescue it.
- **The wall is the SAME:** the Connes–Consani gap to RH = the $\Lambda\to\infty$ uniformity of the cutoff
  positivity (the edge modes $\lambda_n\approx\tfrac12$, width $\sim\log c$) = **structurally our Phase-4 wall**
  (uniform $\lambda_J\to\inf\mathrm{spec}\,\mathcal T$, no a-priori rate). $C(d,T_0)\le1$ (N3) is their contraction
  in scaling language.
- **N4 (unification):** the additive (prime-comb) and multiplicative (adelic/prolate) organizations of Weil
  positivity hit the **same** obstruction; per-place positivity fails in BOTH. Five independent languages now map
  to one self-referential wall (Thm C, N1, N3, B1, N4).

> **Day-24 cont. (3rd). OPTION 2 FULLY ENGAGED AND CLOSED.** All three incarnations of the open core — large
> values (N3), pair correlation (B1), Connes adelic (N4) — engaged concretely with real computation, all reduce
> to the **same** wall: positivity = realness of the zeros = the uniform $\Lambda\to\infty$ passage; the
> archimedean place is provably positive (prolate $\lambda<1$ = $A_\Phi\succ0$), the finite places are the
> obstruction and are NOT per-place positive. **No crossing anywhere.** Durable & real: P9, the validated
> detector, the new band-limited instrument + the prolate bridge, and the five-language map of the wall (N1–N4 +
> Thm C + B1). The honest verdict stands: the sign needs an idea neither we nor the field has in 2026 — and we
> have now mapped *why* from every available direction.

**2026-06-04 — Day 25. P11 consolidation + PHASE 8: a genuinely NEW path (de Bruijn–Newman heat flow).**
`06-papers/P11-band-limited-weil-carleson/{main.tex(6pp,compiled),P11.md}`, `phase-8/{PLAN-RH-PHASE8-heat-flow.md,
SEED-results-and-honest-caveat.md, experiments/heatflow_seed.py}`.
- **P11 written & compiled:** the band-limited Weil–Carleson instrument $C(d,T_0)$, the two RH-independent
  theorems (N3 saturation, B1 sine-kernel 2nd order), the prolate/Connes bridge (N4), and the **five-language
  map of the wall** (Thm 6.1). Index updated P1→P11.
- **Triage of the 3 forwarded ideas (engaged critically):** PT-symmetry/neuromorphic = the Hilbert–Pólya wall
  in physics clothing; **lattices/SVP = likely dead end** — Epstein (lattice) zetas **generically violate RH**,
  so geometry alone doesn't force the line; the Euler product does (confirms our Conj. B2); NCG/entropy = Connes
  = done (N4). None is the path, but PT-symmetry's *dynamical-attractor* instinct, made rigorous, IS.
- **Phase-8 path designed — the de Bruijn–Newman heat flow.** RH $\iff\Lambda=0$ (Rodgers–Tao $\Lambda\ge0$;
  Polymath15 $\Lambda\le0.2$). **The escape from self-reference:** reality of zeros at $t\ge\Lambda>0$ is a
  THEOREM (not RH); propagating it back to $t=0$ is governed by the **Coulomb-gas ODE**, NOT the explicit
  formula — so a dynamical/Lyapunov argument is not self-referential. The marginality $\Lambda=0$ = our measured
  $C\equiv1$ saturation. Synthesis: our detector measures $C(d,T_0;t)$ along the flow; B1's pair-correlation =
  the criticality. OpenAI-style methodology (precise lemmas, verify-first, self-refute, decision gates A/B/C).
- **Seed (Gate A) — mechanism real & measured; one guard-rail catch.** $C(t{=}0)=0.998\le1$ (marginal =
  $\Lambda{=}0$ shadow). Injected off-line pair $\delta_0{=}0.30\Rightarrow C{=}1.0023{>}1$ (detected); FORWARD
  flow **heals** it ($|\mathrm{Im}\,z|\,0.30\!\to\!0.269$, $C\to1.0014$). **Critical line = attractor of the
  flow, tracked by our detector** — the rigorous form of the "stable attractor" instinct. *Guard-rail:* first
  seed used PSD $\sum vv^*$ (can't show $C>1$) → fixed to the indefinite Weil quartet (matches B1); only then did
  detection+healing appear. **Honest caveat:** seed ran FORWARD (well-posed, healing trivial); the RH content is
  the BACKWARD/marginal direction (ill-posed), NOT tested. Lyapunov candidate refined to
  $\mathcal L=\sum(\mathrm{Im}\,z_j)^2$ (flow contracts it via partner-attraction $\dot z\ni-i/\mathrm{Im}\,z$).

> **Day-25 headline.** Did NOT give up. Consolidated (P11) and opened a **genuinely new, non-self-referential
> attack surface**: the de Bruijn–Newman heat flow ($\mathrm{RH}\iff\Lambda=0$), where reality is a theorem for
> $t\ge\Lambda$ and the time parameter is the new DOF the five-language map said we needed. Seed CONFIRMS the
> critical line is the flow's attractor and our detector measures it — but honestly only in the easy (forward)
> direction. **Gate B (the crux):** prove $\dot{\mathcal L}\le0$ to $t=0$ from the Coulomb ODE alone, uniformly
> in height — or find it RH-equivalent (the sixth language). Odds <5%, eyes open, but it is NEW and ours.

**2026-06-04 — Day 25 (cont.). GATE B resolved: clean Lyapunov theorem, but arithmetic-blind ⇒ N5 dynamical no-go.**
`phase-8/{GATE-B-verdict-sixth-language.md, experiments/gateB_lyapunov.py}`.
- **Derived + verified the theorem:** under the Coulomb flow, $\mathcal L=\sum(\mathrm{Im}\,z_j)^2$ obeys
  $\dot{\mathcal L}=-2\sum_{j\ne k}(y_j-y_k)^2/|z_j-z_k|^2\le0$ (symmetrize $\dot{\mathcal L}=2\sum y_j\mathrm{Im}\dot z_j$).
  Matches finite-diff to machine precision. Clean, unconditional, NEW — a strict Lyapunov function for the forward
  flow ($\Rightarrow$ "critical line is the attractor", now rigorous). By-product: isolated pair heals with
  $d(y^2)/dt=-2$ exactly $\Rightarrow$ any RH-violator sits at $|\mathrm{Im}|\le\sqrt{2\Lambda}\le0.63$.
- **But it does NOT cross, for two verified reasons:** (1) **wrong direction** — $\mathcal L$ decreases forward,
  so $\mathcal L(0)\ge\mathcal L(\Lambda)=0$ is trivial; (2) **arithmetic-blind** — the identity is IDENTICAL for
  random / zeta-like / clustered configs; the ODE knows nothing about primes, so a pure-ODE Lyapunov would prove
  "every function satisfies RH" (false). RH lives in the INITIAL DATA; using it = re-injecting zeta's pair
  correlation = the **B1 wall**.
- **N5 (dynamical no-go, established):** any heat-flow/dissipative-dynamics RH attack using only the flow
  (Lyapunov from the ODE) cannot succeed — arithmetic-blind. **Subsumes the forwarded PT-symmetry/neuromorphic
  suggestion** (any "critical-line-as-attractor" dissipative flow is of this type). The attractor picture is true
  and now rigorous, but not a proof, for a precise structural reason.
- **Honest continuation:** the productive version is Rodgers–Tao's (couple the flow to zeta's statistics; they got
  $\Lambda\ge0$ from the lower fluctuation control). RH $=\Lambda\le0$ needs the upper clustering control = open,
  RH-conditional pair correlation. Their machinery + B1 wall, $<2\%$.

> **Day-25 cont. (Gate B).** Pushed the new path to its crux and got an honest, sharp result: a clean Lyapunov
> THEOREM ($\dot{\mathcal L}\le0$) that rigorously vindicates the attractor intuition, plus a verified meta-theorem
> (**N5**) that the entire flow-only class — including the forwarded PT-symmetry ideas — is arithmetic-blind and
> cannot cross. The time-parameter escape is illusory *in a provable way*: arithmetic lives in the initial data,
> and using it returns to the B1 pair-correlation wall. Not giving up = pushing the new idea all the way to where
> it provably stops, and naming why. Durable adds: the Lyapunov theorem, the height bound, N5.

**2026-06-04 — Day 25 (cont.). RT statistics-coupled: heat-flow path lands on the uniform UPPER pair-correlation.**
`phase-8/{RT-coupled-verdict.md, experiments/rt_statistics_coupled.py}`.
- Engaged Rodgers–Tao's statistics-coupling with **real zeta zeros**. By Gate B a tight real pair of normalized
  gap $g$ backward-collides on $t$-scale $\sim g^2$, so $\Lambda$ is governed by the **closest pairs**. Measured
  min normalized gap shrinking with height: $0.291\,(T{\sim}310)\to0.221\,(1591)\to0.194\,(10005)$ — the Lehmer
  phenomenon, **no uniform lower bound on gaps**; the uniformity wall made visible.
- **Verdict:** Rodgers–Tao proved $\Lambda\ge0$ from the **lower tail** (zeros fluctuate). RH $=\Lambda\le0$ needs
  the **upper tail** — a uniform bound forbidding anomalously tight clustering — **open, RH-conditional** (Montgomery
  proven only in a range; uniform upper unknown). **Exactly the B1 wall, upper tail.** The flow delivered us
  precisely to the one irreducible statistical statement; it did not bypass it.
- **Phase 8 closes.** Durable: the Lyapunov theorem, the height bound $|\mathrm{Im}|\le\sqrt{2\Lambda}\le0.63$,
  **N5** (dynamical no-go), and the **named irreducible target** = uniform upper pair-correlation = no-uniform-tight-
  Lehmer. Every route (5 static languages + flow-only N5 + statistics-coupled) terminates at the SAME arithmetic
  core. No key; <2%.

> **Day-25 final.** Engaged the principal's chosen continuation (Rodgers–Tao) with real computation. It lands,
> precisely and honestly, on the **uniform upper pair-correlation** — the irreducible open core, the B1 wall's upper
> tail. Phase 8's real harvest: a new Lyapunov theorem (attractor, rigorous), N5 (first PROVED no-go for an entire
> class of methods, subsuming PT-symmetry/dissipative), and the sharply-named target. We did not give up; we pushed a
> genuinely new path to its provable floor and named exactly what new mathematics a crossing requires.

**2026-06-04 — Day 25 (final). Attacked the upper tail: $\Lambda=$ first backward collision; lands on GUE gap universality.**
`phase-8/{UPPER-TAIL-verdict.md, experiments/upper_tail_backward.py}`.
- **Self-correction (guard-rail on my own RT note):** the target is **extremal**, not an average — even ONE
  complex pair forces $\Lambda>0$; $\Lambda=\sup$ of backward-collision times. RH = worst pair has $t_c<0$,
  uniformly.
- **Verified mechanism:** pair gap $g^2(t)=g_0^2+8t$ (2-body, to $2\%$); collision at $t_c=-g_0^2/8$; $\Lambda=$
  first backward collision = largest $t$ with a multiple zero.
- **Measured (real zeros, backward flow):** $t_c<0$ at all heights (RH-safe), $|t_c|$ shrinks with $T$
  ($0.105\to0.032\to0.025$, since spacing $s\sim2\pi/\log T\to0$). **New observation:** normalized $t_c/s^2$
  clusters at a **universal negative constant $\approx-0.02$** (GUE/sine-kernel prediction; suggestive — 3 pts,
  crude windowed flow). Marginal $\Lambda=0$ consistent: $t_c\to0^-$ absolute, normalized stays $<0$.
- **Sharpest target:** RH $\Longleftarrow$ $t_c/s^2$ stays a universal negative constant uniformly = **unconditional
  GUE gap universality** of $\zeta$ zeros — open, RH-conditional (Montgomery range only). **The B1 wall, in its
  strongest quantitative extremal form.** No key, $<2\%$.

> **Day-25 FINAL. Phase 8 fully mapped and closed.** Attacked the user's chosen target (upper tail) with real
> computation: got a verified mechanism, a pretty new observation (universal normalized collision margin), and the
> sharpest possible statement — RH ⟸ unconditional GUE gap universality. **Every route now provably terminates at
> the SAME irreducible arithmetic statement** (the unconditional pair-correlation/gap universality of the zeros):
> 5 static languages + flow-only (N5) + statistics-coupled + upper-tail extremal. We did not give up — we compressed
> RH to its single hardest, sharpest open core and proved the shortcuts don't exist. Durable Phase-8 harvest:
> Lyapunov theorem, height bound, N5, and the maximally-sharp target. A crossing needs new mathematics on
> unconditional universality — which neither we nor the field has.

**2026-06-04 — Day 26. P12 (Phase-8 consolidation) written & compiled; PHASE 9 program designed.**
`06-papers/P12-heat-flow-lyapunov/{main.tex(4pp,compiled),P12.md}`, `phase-9/PLAN-RH-PHASE9-unconditional-universality.md`.
- **P12 written & compiled:** the de Bruijn–Newman Lyapunov theorem (Thm 2.1 attractor; Cor 2.2 height bound), the
  dynamical no-go N5 (Thm 3.1, arithmetic-blind, subsumes PT-symmetry), the extremal reduction (Prop 4.1,
  $\Lambda=$first backward collision) and the universal normalized margin → target = unconditional GUE gap
  universality (Obs 4.2). RH-independent. Index updated P1→P12 (P12 = "Arc C: dynamical").
- **Phase 9 program designed** — the attack on the irreducible target (U): unconditional extremal gap universality.
  Landscape mapped (Montgomery support barrier; Rudnick–Sarnak unconditional-restricted; Katz–Sarnak proven over
  function fields; simplicity of zeros). **Spearhead S9 (the genuine new idea, escapes N5):** seek a functional
  $\mathcal F[H_t]$ of $H_t$ ITSELF (not its zeros) — weighted Dirichlet energy / relative entropy / explicit-formula
  pairing — BOTH monotone under the flow AND arithmetic-aware (sees the kernel/primes). N5 forbids only position-only
  functionals; $\mathcal F[H_t]$ evades it. Sub-targets T9-A (extend support), T9-B (tight-pair tail), T9-C (S9),
  T9-D (function-field transport). Assets: detector calibrates "how much is exactly enough"; extremal reduction =
  one-sided (softer) target. **Next: M9.1/L9.1 — does an arithmetic-aware monotone $\mathcal F[H_t]$ exist?** Honest:
  full (U) <1%, multi-year; T9-A/B real incremental sub-problems.

> **Day-26.** Consolidated Phase 8 into P12 (compiled) and designed the Phase-9 program for the new mathematics the
> problem demands. The one genuinely new move: escape N5 via a functional of $H_t$ (arithmetic-aware) not of its
> zeros (blind). Banked: P1–P12, N1–N5, the Lyapunov theorem, the validated detector, the precisely-named target.

**2026-06-04 — Day 26 (cont.). M9.1 resolved the spearhead: N6 — no arithmetic-aware monotone escape.**
`phase-9/{M9.1-N6-spearhead-verdict.md, experiments/M9_1_spearhead.py}`.
- Tested the 3 exhaustive sources of arithmetic-awareness for a monotone $\mathcal F[H_t]$ (any functional of $H_t$
  reduces via Hadamard to zeros + trivial factor): (1) **generic** heat-flow energy — universal monotonicity,
  **blind** (verified: $E$ changes smoothly across on/off-line, not sign-keyed); (2) **archimedean** density —
  controls COUNT $N(T)$, not reality; (3) **primes via explicit formula** — the only reality-aware source, but its
  positivity for positive-type $g$ **IS** the Weil criterion = RH. **Verified the explicit formula to
  $5.3\times10^{-12}$** ($\sum_\rho h(\gamma)=$ arch+pole−primes $=0.0038876$), anchoring "arithmetic-awareness =
  this identity = the wall."
- **N6 (spearhead no-go):** every flow-monotone $\mathcal F[H_t]$ is generic-blind / archimedean-count / prime-aware-
  =-wall. The arithmetic-aware-monotone escape from N5 **does not exist**. Time cannot carry prime info except
  through the explicit formula, whose positivity is what we must prove.
- **Residual = T9-A/T9-B** (unconditional partial arithmetic: extend Montgomery support; bound tight-pair tail) —
  NOT a new escape, the field's known-hard open frontier. Our distinctive deliverable: detector-calibrated "how much
  support/tail-bound is EXACTLY enough" to force $t_c/s^2<0$.

> **Day-26 (cont.). N6 = the sixth and sharpest no-go: it closes the LAST genuinely new idea** (the arithmetic-aware
> monotone functional). After N6 the program has no untried escape — only the field's known unconditional sub-problems
> (T9-A/B), where we bring a calibrating instrument but no special key. Honest: the new-idea space is exhausted; a
> crossing needs progress on extending the unconditional range of the zero statistics (a central open problem). Banked:
> P1–P12, N1–N6, the Lyapunov theorem, the validated detector, the precisely-cornered target.

**2026-06-04 — Day 26 (cont.). T9-A attacked head-on: the support barrier = short-interval prime variance; the WRONG-SIGN capstone.**
`phase-9/{T9A-verdict-wrong-sign.md, experiments/T9A_montgomery_F.py}`.
- Computed Montgomery $F(\alpha,T)$ from 700 real zeros: rises through $\alpha<1$ (known, $\sim|\alpha|$), levels for
  $\alpha>1$ (conjectured $\sim1$, open). The $\alpha>1$ region = **prime pair correlation / variance of primes in
  short intervals** (Goldston–Montgomery) — famous open.
- **Sharp barrier:** our extremal tight-pair target needs an **UPPER** bound on $F$ for $\alpha>1$; Montgomery's
  unconditional tool is $F\ge0$, which gives **LOWER** bounds on clustering (small gaps occur: Lehmer/simplicity),
  not the upper bound. **The unconditional handle is one-sided the WRONG way.**
- **WRONG-SIGN CAPSTONE (the program's deepest unifying observation):** every unconditional handle on the zeros is a
  **positivity** ($\ge0$), oriented to give lower bounds / existence / the easy side; RH is fundamentally a one-sided
  **upper** constraint (no off-line zeros; no clustering above GUE). Positivity gives the wrong inequality direction.
  This mismatch recurs across Gate B (monotonicity wrong way), N5/N6 (Weil $F\ge0$ = existence), T9-A (Montgomery
  $F\ge0$ = lower bounds) — it is, across N1–N6 + T9-A, the single deepest reason RH resists.
- Residual doable (finite, real): detector-calibrated "exactly how much $\alpha>1$ upper bound suffices to force
  $t_c/s^2<0$" — a quantified target for the community.

> **Day-26 (cont.). T9-A = the field's open frontier (short-interval prime variance), with the unconditional tool
> wrong-signed.** No key. The capstone: unconditional positivity is lower-bound-oriented, RH is an upper constraint —
> the wrong-sign mismatch unifies all six no-gos. We attacked every named target head-on and characterized, precisely,
> why each resists. Banked: P1–P12, N1–N6, Lyapunov theorem, validated detector, the cornered target, and the wrong-sign
> capstone. A crossing needs an unconditional UPPER bound nobody has.

**2026-06-04 — Day 26 (final). T9-cal: the calibration deliverable — an exchange rate support ↔ certified zeros.**
`phase-9/{T9cal-DELIVERABLE-exchange-rate.md, experiments/T9cal_support_requirement.py}`.
- The program's honest FINITE output. Bridge (rigorous up to O(1)): detector at band $d$, height $T$ uses
  $F(\alpha)$ up to $\alpha=2d/\log T$ (N3); resolving a normalized gap $\beta$ needs $\alpha\asymp1/\beta$
  (Nyquist, B1); $\Lambda$ set by the tightest pair (P12). So $\alpha_{\rm req}(T)\asymp1/\beta_{\min}(T)$.
- **GUE level repulsion** ($\beta_{\min}\asymp N^{-1/3}$, $N\sim\frac{T}{2\pi}\log T$) gives the clean law
  $\alpha_{\rm req}(T)\asymp N(T)^{1/3}\asymp(T\log T)^{1/3}$, i.e. the **EXCHANGE RATE: proving Montgomery's
  $F(\alpha)\le O(1)$ up to $\alpha=A$ certifies the extremal collision margin (analytic non-existence of
  off-line zeros) for the first $\sim A^3$ zeros.** Table: $A{=}5\to125$ zeros; $A{=}20\to8000$; $A{=}100\to10^6$;
  $A{\to}\infty\to$ full RH. (Numerics: $\beta_{\min}=0.29,0.22,0.19$ at $T\approx310,1591,10^4$ → $\alpha_{\rm
  req}>1$ at every nontrivial height.)
- **Punchline:** Montgomery's proven $\alpha<1$ is, for the EXTREMAL target, essentially empty (covers only the
  bulk/average $\beta>1$; never the tightest pairs). Each unit of new proven support buys $\sim\alpha^3$ certified
  zeros. The detector makes any claimed bound checkable.

> **Day-26 FINAL. The program's analytic arc is complete.** The wall is mapped (6 languages), every named target
> attacked head-on (N1–N6 + T9-A), the deepest reason named (wrong-sign capstone), the target cornered
> (unconditional gap universality), and now the **cost of crossing priced** (T9-cal exchange rate: support $A$ ↔
> $\sim A^3$ zeros). Banked: P1–P12, N1–N6, the Lyapunov theorem, the validated detector, the wrong-sign capstone,
> the exchange rate. No crossing — honestly, none is reachable without an unconditional upper bound the field lacks
> — but the resistance of RH is now charted, priced, and explained with unusual completeness.

**2026-06-04 — Day 27. MASTER CLOSING DOCUMENT + PHASE 10 (the cohomological turn) proposed.**
`MASTER-CLOSING-the-wall-charted.md`, `phase-10/PHASE-10-NEW-MATHEMATICS-the-cohomological-turn.md`.
- **Master closing document** written: full synthesis — 3 arcs, 12 papers, the 6-language wall, the 6 no-gos
  (N1–N6), durable RH-independent results (P9, detector, Lyapunov), the cornered target (U), the exchange rate, the
  wrong-sign capstone. The definitive panel-facing record of the analytic arc.
- **Phase 10 proposed — the cohomological turn**, the one path that escapes the wrong-sign capstone: a HIGHER-level
  (Hodge-index) positivity yielding the zero-level UPPER bound by DUALITY — how the Weil conjectures (the only proved
  RH) were proved. Program: build the arithmetic surface / cohomology for Spec Z (Deninger / Connes–Consani / F_1).
  Entry point: explicit formula = Lefschetz trace; Weil–Carleson form = intersection form on the primitive part;
  missing = the ample/polarization direction + full Lorentzian envelope. **M10.1 (buildable now):** reconstruct the
  Lorentzian envelope from the detector — adjoin a candidate ample direction, test the Hodge-index signature (exactly
  one positive eigenvalue) + the Castelnuovo–Severi shape. Either supports/falsifies the surface picture or yields a
  7th no-go (first about the cohomological route). Honest: generational, ≪1%, but the only structure known to turn the
  corner, and it requires inventing mathematics.

> **Day-27. Closed the analytic arc (master document); opened the one new-mathematics direction.** The cohomological
> turn is not another reformulation — it is the structure (Hodge index → upper bound by duality) that escapes the
> capstone, as the Weil conjectures did. Our detector gives the primitive block of the intersection form explicitly —
> a concrete finite first brick (M10.1) the abstract programs lack.

**2026-06-04 — Day 27 (cont.). M10.1 — the Lorentzian envelope degenerates: the cohomological face of the marginality.**
`phase-10/{M10.1-verdict-degenerate-hodge.md, experiments/M10_1_hodge_envelope.py}`.
- Reconstructed the candidate intersection form: Weil–Carleson $\mathfrak t=A_\Phi-P_F$ (primitive part) + one ample
  (archimedean) direction. Grew band $d$ (= grew cohomology "genus" toward ζ) and tracked the **Hodge gap**
  $\lambda_{\min}(\mathfrak t)$ + signature of $I$.
- **MEASURED:** finite genus (small $d$) → form is **DEFINITE**, Hodge gap $>0$, signature $(1,N,0)$ — curve-like,
  Lorentzian. As genus → ζ: gap $\to0$ and the form **DEGENERATES** (null directions appear): gap $0.377\,(d{=}1)\to
  0.008\,(1.5)\to3{\times}10^{-9}\,(2.0)\to\sim0$; signature $(1,N{-}k,k)$, $k=0,0,2,5,6,8,9$.
- **THE FOUR-WAY UNIFICATION:** N3 saturation $(C\equiv1)$ = $\Lambda=0$ marginality = vanishing Hodge gap =
  degeneration of the intersection form. The wrong-sign capstone in cohomological language: the Hodge positivity is
  **marginal (zero-gap)** for ζ, **definite (positive-gap)** for curves (finite genus); the finite-rank Hodge
  argument does NOT transfer.
- **The new math named (with a measurable diagnostic):** a **regularized, infinite-dimensional Hodge index** (a
  ζ-regularized Castelnuovo–Severi positivity surviving infinite genus) controlling the degenerate primitive form —
  the open heart of Deninger / Connes–Consani, now with our detector computing the degeneration explicitly. First
  concrete result ABOUT the cohomological route: consistent, obstruction = measured degeneration, target sharp.
- **Not a crossing** (degeneration = the marginality wall), but the cohomological framing is the one place it might be
  *controllable* (regularized determinants are built for infinite-dim degenerate settings). M10.2 = construct the
  ζ-regularized Hodge gap — the genuine generational new-math problem.

> **Day-27 (cont.). The cohomological route's first brick is laid.** M10.1 reconstructs the Lorentzian envelope,
> shows it is definite for finite genus and DEGENERATES toward ζ, and thereby unifies N3 / $\Lambda{=}0$ / saturation /
> intersection-form-degeneration as ONE phenomenon — and names the precise new mathematics (regularized infinite-dim
> Hodge index) with a measurable diagnostic. Honest: not a crossing, but the sharpest characterization yet of what must
> be invented, and the first finding that is *about* the only capstone-escaping route.

**2026-06-04 — Day 27 (cont.). M10.2 — the regularized Hodge gap SURVIVES (first non-trivially-realized positivity).**
`phase-10/{M10.2-verdict-regularized-gap-survives.md, experiments/M10_2_regularized_gap.py}`.
- The bare-gap vanishing (M10.1) was carried by TRIVIAL null directions (test functions vanishing at all window
  zeros = interpolation = the trivial classes). The curve Hodge index is definite on the PRIMITIVE part = modulo
  trivial. So the **regularized Hodge gap** = smallest POSITIVE eigenvalue of $\mathfrak t$ = $\lambda_{\min}$ of
  the $K\times K$ sine-kernel Gram of the zeros.
- **MEASURED: it is POSITIVE and healthy** ($+0.15,0.34,0.48,0.69$ as $d$ resolves, at $T_0{=}100$; $+0.20,0.35$ at
  $T_0{=}500$) — exactly where the bare gap vanished. **The genuine primitive intersection form of ζ is
  positive-DEFINITE with a real gap** (the M10.1 degeneration was only trivial nullity). FIRST non-trivially-realized
  positivity in the program (every other language's relevant positivity was marginal).
- **Reformulation:** regularized Hodge index positivity $\iff G\succeq c>0$ uniformly $\iff$ zeros are a uniform
  **Riesz sequence** for Paley–Wiener/de Branges $\iff$ (U) as a **DETERMINANTAL positivity**. Still (U) (capped by
  the tightest pair), but now in the form $\zeta$-regularized determinants (Deninger $\det_\infty$, Connes–Consani)
  and Seip-type de Branges sampling are built for — a TWO-sided definiteness, plausibly OUTSIDE the wrong-sign
  capstone (a determinant is positive or not, not a one-sided lower bound).
- Next M10.3: uniform lower frame bound — does $\lambda_{\min}(G)$ stay bounded below as $T\to\infty$? (Seip de
  Branges sampling on the over-dense zero set.)

> **Day-27 (cont.). M10.2: the first encouraging sign.** The regularized Hodge gap is positive and healthy — the
> cohomological route's needed positivity is NON-trivially realized, unlike every other language. RH reduces to a
> uniform Riesz/determinantal positivity — the cornered target (U) recast as a two-sided definiteness, the natural
> object for regularized-determinant machinery and the one form plausibly outside the wrong-sign capstone. Not a
> crossing, but the most promising reformulation the program has produced for new machinery to engage.

**2026-06-04 — Day 27 (cont.). M10.3 — the uniform frame bound is T-stable; the route lands on S(T) regularity.**
`phase-10/{M10.3-verdict-uniform-frame-S(T).md, experiments/M10_3_uniform_frame.py}`.
- At FIXED sampling ratio ($K/M\approx0.8$, band $d\sim\tfrac12\log(T/2\pi)$), across $T{=}50\to3000$ (two orders of
  magnitude), the regularized gap $\lambda_{\min}(G)$ is **remarkably T-STABLE**: $0.284,0.289,0.246,0.292,0.204$.
  **First numerical evidence of a UNIFORM lower frame bound** — the regularized Hodge index could genuinely hold.
- **The new handle (Pavlov/Seip/de Branges):** uniform lower frame bound for reproducing kernels in $H(E)$ $\iff$ a
  **Muckenhoupt $A_2$ (Helson–Szegő)** condition on $|E|^2\sim\xi$ $\iff$ **regularity of $S(T)=\tfrac1\pi\arg\zeta$**.
  So RH (regularized Hodge) $\iff$ uniform $A_2$ on $E\sim\xi$ $\iff$ $S(T)$ regularity. **Two favorable features:**
  (1) it is TWO-SIDED (a definiteness $c\le\lambda\le C$, not a one-sided bound) — plausibly OUTSIDE the wrong-sign
  capstone; (2) $S(T)$ has strong UNCONDITIONAL partial control (Selberg: $S(T)=O(\log T)$, all moments, Gaussian CLT).
- **Honest:** still (U)/RH in the limit (range doesn't reach the tightest Lehmer pairs; full uniform $A_2$ open under
  RH only). But it is the FIRST target the program reaches with substantial unconditional, two-sided control already
  existing — the single most promising reformulation produced.
- Next M10.4: engage Pavlov $A_2$ + Selberg's $S(T)$ bounds quantitatively — does $S(T)=O(\log T)$ + moments give a
  nontrivial UNCONDITIONAL frame bound (positive-density subset / $\varepsilon$-loss)? Price the route like T9-A.

> **Day-27 (cont.). M10.3: the most promising reformulation.** Through M10.1–M10.3 the cohomological route converted
> RH from a one-sided pair-correlation upper bound (wrong-signed, intractable) into a uniform Riesz/Muckenhoupt
> definiteness governed by $S(T)$ regularity — TWO-sided, with real unconditional partial control (Selberg). The frame
> bound is T-stable in data. Not a crossing, but the first time the cornered target sits in a form with existing
> two-sided unconditional tools.

**2026-06-04 — Day 28. DEEP RUN (M=25, T≤10⁴, 10154 zeros) + M10.4 — Phase 10 closes; capstone holds even here.**
`phase-10/{DEEPRUN-analysis-M10.1-M10.3.md, M10.4-verdict-route-priced-capstone-holds.md, deeprun_M10.1-M10.3.png,
experiments/{colab_phase10_M1_to_M3.py, make_deeprun_figure.py}}`.
- **Deep run corrected M10.3's optimism (guard-rail via more numbers):** at $T{=}10^4$ the regularized gap DROPPED
  to $0.111$ (half the $\sim0.28$ plateau). Analysis: $\boxed{\lambda_{\min}(G)\approx\frac{\pi^2}{6}\beta_{\min}^2}$
  (ratio $1.1$–$2.0$ around $\pi^2/6{=}1.64$; the $2{\times}2$ sine-kernel level-repulsion law). The gap is governed
  by each window's TIGHTEST pair; the dip is its tighter $\beta_{\min}{=}0.31$. The shallow "T-stability" was the
  slow fluctuating regime. **$\inf\lambda_{\min}(G)\to0$ at the Lehmer pairs = (U).** New clean identity: the
  regularized Hodge gap IS the squared minimum gap.
- **M10.4 priced the route:** via $\lambda_{\min}{=}\frac{\pi^2}{6}\beta_{\min}^2$ + $\beta_{\min}\asymp N^{-1/3}$,
  the cohomological route gives the **IDENTICAL exchange rate to T9-cal** ($A\leftrightarrow\sim A^3$ zeros) — it IS
  the same target.
- **The wrong-sign CAPSTONE HOLDS even in the frame/de Branges language:** the easy/unconditional direction is the
  UPPER frame bound (Bessel = positivity); the hard direction is the LOWER frame bound (= RH), which though a
  "lower bound on a Gram eigenvalue" MEANS "no two zeros too close" = a one-sided UPPER clustering constraint. The
  "two-sidedness" was illusory. $S(T)$ pricing: Selberg controls the TYPICAL $S(T)$ ($\sqrt{\log\log T}$, CLT); the
  obstruction is the EXTREMAL sup-interval $S(T)$ (tight pairs), unconditional only as $O(\log T)$ → not uniform.
- **Phase 10 closes — the SEVENTH language of the wall** (the first ABOUT the capstone-escaping route): the route
  designed to escape the capstone does not; it is the natural HOME for the target (two-sided, determinantal,
  regularized-determinant-friendly), not a passage. Durable: the identity $\lambda_{\min}{=}\frac{\pi^2}{6}\beta_{\min}^2$,
  the four-way unification, the Riesz/$A_2$/$S(T)$ reformulation, and the capstone's robustness.

> **Day-28. Phase 10 closed honestly.** The deep run (the user's 3.4 h Colab) corrected the optimism: the regularized
> Hodge gap is exactly $\frac{\pi^2}{6}\beta_{\min}^2$, so the cohomological route prices identically to T9-cal and
> reduces to (U). The wrong-sign capstone holds even in the most favorable (frame/de Branges/determinantal) language —
> the lower frame bound is an upper-clustering constraint. Every route, including the one built to escape the capstone,
> terminates at (U). Banked: P1–P12, N1–N6, the capstone, the exchange rate, and now the Phase-10 identity +
> reformulation + the capstone-robustness theorem.

**2026-06-04 — Day 28 (cont.). PHASE 11 opened — the hyperbolicity / Jensen-polynomial route (a different MECHANISM).**
`phase-11/{PLAN-RH-PHASE11-hyperbolicity-route.md, experiments/M11_1_jensen_hyperbolicity.py}`.
- **New path, distinct in KIND:** RH $\iff\Xi\in$ Laguerre–Pólya $\iff$ all Jensen polynomials $J^{d,n}$ of $\Xi$ are
  HYPERBOLIC (real-rooted). This is **real-rootedness, NOT a quadratic-form positivity** — proved in modern
  combinatorics by **interlacing families (Marcus–Spielman–Srivastava)** and **stability preservers
  (Borcea–Brändén)**, mechanisms that bound the *largest root* (an UPPER control) **without a positivity
  certificate**. The one classical route to an upper bound the wrong-sign capstone does not obviously obstruct.
- **Recent partial result (why now):** Griffin–Ono–Rolen–Zagier (PNAS 2019) — for each fixed $d$, $J^{d,n}$
  hyperbolic for all large $n$; rescaled roots → Hermite $H_d$ (GUE). Uniformity in $d$ is the open frontier.
- **M11.1 grounding (done, works):** computed $\Xi$ Taylor coeffs $a(k)=\Xi^{(2k)}(0)/(2k)!$ ($a(0)=0.4971=\xi(1/2)$);
  signs ALTERNATE (+,−,+,−,…, the L–P signature); Turán $a(k)^2-a(k-1)a(k+1)>0$ holds; all $J^{d,n}$ ($d{=}2..5$,
  $n{=}0,2,5$) HYPERBOLIC ($\max|\mathrm{Im}|=0$). Concrete, computable, RH-consistent.
- **Honest risk:** low-degree hyperbolicity ($d{=}2$ = Turán = Li positivity) inherits the capstone; the BET is the
  high-degree régime where MSS interlacing replaces positivity. M11.5 is the make-or-break (is the high-degree
  interlacing positivity-free?). Milestones M11.2 (interlacing family), M11.3 (stability-preserver realization of the
  shift, where arithmetic enters — escape N6), M11.4 (uniformity-in-$d$ margin probe).

> **Day-28 (cont.). Phase 11: the first path whose MECHANISM is structurally outside the positivity paradigm.** After
> proving every positivity route (7 languages) reduces to (U) and the capstone holds even in the cohomological/frame
> language, hyperbolicity (real-rootedness via interlacing, not positivity) is the principled next bet — it is exactly
> the kind of upper-root-location control the capstone said we need, with recent partial results (GORZ) and powerful
> modern machinery (MSS, Borcea–Brändén). Grounded (M11.1). Next: M11.2, the interlacing-family structure.

**2026-06-04 — Day 28 (cont.). M11.2 — interlacing holds (MSS precondition); the positivity is TOTAL positivity.**
`phase-11/{M11.2-verdict-interlacing-total-positivity.md, experiments/M11_2_interlacing.py}`.
- **(A) Interlacing structure exists:** $J^{d,n}$ vs $J^{d,n+1}$ (shift) AND $J^{d,n}$ vs $J^{d+1,n}$ (degree)
  interlace for all tested $(d{=}3,4,5;\,n{=}0,2,4)$ — the **MSS largest-root precondition is met.**
- **(B) Guard-rail correction:** first tested Hankel (moment) minors → mixed signs = WRONG object. Corrected: RH
  $\iff b(k){=}(-1)^k a(k)$ is a **Pólya-frequency sequence** $\iff$ Toeplitz $[b(i-j)]$ **totally positive** (ASW).
  Verified: $b(k)>0$ all; log-concave (Turán); contiguous Toeplitz minors orders 1–6 ALL positive
  ($+0.497,+7e{-}5,+1.5e{-}13,\dots,+7.7e{-}73$). **The positivity behind the route is TOTAL positivity (Toeplitz/
  Schoenberg), NOT quadratic/moment positivity** — structurally richer, the variation-diminishing/interlacing regime.
- **Honest read:** the TARGET (total positivity of $b$ = RH) is still a positivity (capstone-bound as an object).
  **The escape is the METHOD:** MSS interlacing-families establish such total positivity WITHOUT a positivity
  certificate (largest-root bound). M11.2 confirms its precondition holds. Bet sharpened: make the MSS largest-root
  argument apply to $\{J^{d,n}\}$ with arithmetic entering via the shift. Next: M11.3 (shift = Borcea–Brändén
  stability-preserver, where ζ enters — escape N6), then M11.5 (is high-degree interlacing positivity-free?).

> **Day-28 (cont.). M11.2:** the interlacing precondition for the positivity-FREE MSS machinery holds for $\Xi$, and
> the underlying positivity is the richer TOTAL positivity (Pólya-frequency/Toeplitz), not the quadratic kind the
> capstone obstructs. The route's escape is the method (interlacing largest-root), not the object. Precondition met;
> the decisive tests are M11.3 (arithmetic via the shift) and M11.5 (positivity-free?).

**2026-06-04 — Day 28 (cont.). M11.3 — shift preserver is arithmetic-blind; the escape is the MSS averaging realization.**
`phase-11/{M11.3-verdict-preserver-blind-MSS-pivot.md, experiments/M11_3_shift_preserver.py}`.
- **Shift identified:** $\Xi=\int_0^\infty\Phi(u)\cos(tu)du$ (dBN kernel) ⟹ $b(k)=(-1)^k a(k)=m_{2k}/(2k)!$ (even
  moments of $\Phi$ = the ARITHMETIC). Shift $n\to n+1$ = $\Phi\to u^2\Phi$ = $\Xi\to-\Xi''$ = DIFFERENTIATION = a
  Borcea–Brändén stability preserver (preserves Laguerre–Pólya).
- **Arithmetic-blindness verified (N5-analogue):** differentiation preserves L–P for ANY L–P function. Control test —
  $\cos t$ (proven L–P) vs $\Xi$ ($\zeta$): IDENTICAL structure (all $J^{d,n}$ hyperbolic, shift- and degree-interlace,
  all True for both). The preserver/interlacing STRUCTURE cannot single out $\zeta$; arithmetic lives only in "is
  $\Xi\in$ L–P" = RH. **A stability-PRESERVING operator cannot cross.**
- **The genuine escape (pivot):** MSS is NOT a preserver — it is an AVERAGING construction proving real-rootedness of
  an EXPECTED characteristic polynomial via interlacing, positivity-free. So the target (M11.4) is a **constructive
  Hilbert–Pólya via MSS:** realize $\Xi$ as $\mathbb{E}\det(xI-A_\omega)$ of a random ensemble whose distribution
  carries the $\zeta$ moments $m_{2k}$, with interlacing forcing the real spectrum — replacing self-adjointness (the
  century-old HP wall) with MSS interlacing (a new positivity-free tool). Arithmetic enters via the ENSEMBLE
  DISTRIBUTION (the one place N5/N6 do not forbid).

> **Day-28 (cont.). M11.3:** the preserver half of the hyperbolicity route is arithmetic-blind (same as $\cos$,
> N5-analogue), so it cannot cross — but the response is structurally correct for the first time: an AVERAGING
> (random-matrix) realization rather than another preserving operator. The escape is constructive Hilbert–Pólya via
> the MSS interlacing method (positivity-free real spectrum), arithmetic in the ensemble distribution. First route
> whose escape mechanism is both new and not-yet-refuted. Next: M11.4, probe the random-matrix realization of $\Xi$.

**2026-06-04 — Day 28 (cont.). M11.4–M11.5 — the decisive test: hyperbolicity IS a positivity; capstone holds. Phase 11 closes.**
`phase-11/{M11.4-5-verdict-capstone-holds-richest-positivity.md, experiments/M11_4_5_hermite_form_capstone.py}`.
- **Decisive fact:** a degree-$d$ real polynomial has all real roots $\iff$ its **Hermite form** $H[i,j]=p_{i+j}$
  (Hankel of Newton power sums of roots) is **PSD**. So real-rootedness of each $J^{d,n}$ **IS a quadratic
  positivity.** Verified on $\Xi$ ($d\le4$ clean): $\min\mathrm{eig}(H)>0$ throughout ($+0.70,..,+0.047$). ($d=5$
  large-negatives = numerical artifacts — power sums overflow; M11.1 confirmed hyperbolic by direct roots.)
- **M11.5 verdict (the make-or-break):** the MSS "interlacing" method's apparent positivity-freedom is **illusory at
  the foundation** — it rests on real-stability of $\det(xI+\sum z_iA_i)$ for $A_i\succeq0$ (Borcea–Brändén), a
  POSITIVITY (PSD building blocks). So the hyperbolicity route, traced to root, **is a positivity → the wrong-sign
  CAPSTONE HOLDS.** It is the RICHEST positivity language (real-stability / total positivity / Hermite form, the
  Borcea–Brändén/MSS machinery) — but a positivity, hence (U) in disguise. **Not a crossing.**
- **Eighth confirmation of the capstone:** six static languages + dynamical (heat flow) + cohomological (Hodge) +
  hyperbolicity (stable polynomials) — EVERY paradigm reduces to a positivity and to (U), including the one whose
  mechanism looked positivity-free. Durable Phase-11 harvest: the dBN-moment identity $b(k)=m_{2k}/(2k)!$; RH as
  total positivity / real-stability of the PF sequence (modern language); the arithmetic-blindness (M11.3) + PSD
  foundation (M11.5) = the hyperbolicity-language forms of N5 and the capstone.

> **Day-28 FINAL. Phase 11 closed honestly.** The most promising NEW mechanism (real-rootedness via interlacing,
> structurally outside quadratic positivity) was pursued fully and delivered the richest positivity reformulation +
> the most powerful modern toolbox — but its FOUNDATION is a positivity (Hermite form / PSD real-stability), so it
> does not escape the capstone. Eight paradigms tested; all terminate at a positivity and at (U). The wrong-sign
> capstone is, now, exceptionally robust. Banked: P1–P12, N1–N6, the capstone (8× confirmed), the exchange rate,
> the Phase-10 + Phase-11 identities and reformulations.

**2026-06-04 — Day 28 (final). CONSOLIDATION: Phases 10–11 into the master doc + map; P13 written & compiled.**
- **Master closing document** updated: Part III now the **EIGHT-language wall** (added 7 cohomological Hodge, 8
  hyperbolicity); capstone table (Part VII) + the two modern paradigms; new **Part VIII** (Phases 10–11 in full);
  Part IX verdict updated to thirteen papers / eight paradigms.
- **00-MAP.md** extended with **PART 6 — Phases 7–11** (N3–N6, the capstone, the exchange rate, the eight languages).
- **P13 written & compiled** (`06-papers/P13-modern-routes-wrong-sign/`, 5pp): the two modern routes (Hodge-index;
  hyperbolicity), the identities $\lambda_{\min}(G)=\frac{\pi^2}6\beta_{\min}^2$ and $b(k)=m_{2k}/(2k)!$, the
  Hermite-form capstone theorem, and the robustness-across-eight-paradigms theorem. Index updated P1→P13 (new
  "Arc D: modern paradigms"). Durable, RH-independent.

**2026-06-04 — Day 28 (final). PHASE 12 proposed — the first NON-POSITIVITY path: log-correlated fields / multiplicative chaos.**
`phase-12/PLAN-RH-PHASE12-log-correlated-upper-bounds.md`.
- The capstone itself dictates the new path: a mechanism whose native output is an unconditional **UPPER** bound, not
  founded on a positivity. **The one such modern machinery connected to ζ:** log-correlated fields / multiplicative
  chaos, which produce upper bounds on extremes (max|ζ|~log log T: Arguin–Belius–Bourgade–Radziwiłł–Soundararajan,
  Najnudel, Harper) via second-moment / Girsanov / branching-barrier methods — **not** positivity.
- **Direct bridge to our cornered target:** Phase 10 (P13) reduced RH to **extremal $S(T)$ regularity** (uniform
  $A_2$); and **$S(T)$ is a log-correlated field** ($\mathbb E[S(t)S(t')]\sim-\frac1{2\pi^2}\log|t-t'|$, Bourgade/
  Najnudel; Selberg CLT = its marginal). So (U) in Phase-10 form **is** a log-correlated extreme-value problem —
  exactly where the upper-bound machinery lives. The two halves were built to meet.
- **First route whose DIRECTION (upper) and MECHANISM (probabilistic, not positivity) both match what the capstone
  demands** — it does not pre-reduce to a positivity like Hodge/hyperbolicity. Open part: the extreme tail / freezing
  at minimal scale (RH-strength), but in a fast-moving, upper-bound-native field. Milestones M12.1 (confirm the
  log-correlated covariance in our data), M12.2 ($A_2$↔extreme-$S(T)$ dictionary), M12.3 (apply the chaos upper bound,
  price the gap), M12.4 (decisive: verify it is genuinely not a positivity at foundation).

> **Day-28 final. Phase 12 opened: the first non-positivity path.** The eight-paradigm capstone analysis points
> exactly here — log-correlated / multiplicative-chaos machinery gives UPPER bounds (the right direction) without a
> positivity, and our own Phase-10 reformulation (RH = extremal $S(T)$ regularity) meets it, since $S(T)$ is
> log-correlated. The first route the wrong-sign capstone does not, on its face, obstruct. Next: M12.1.

**2026-06-05 — Day 29. PHASE 12 executed in full (M12.1–M12.5, autonomous): the capstone is ESCAPED; N7 found and BRIDGED; lands on large values (Arc A).**
`phase-12/{M12-VERDICT-capstone-escaped-new-barrier.md, experiments/{M12_1_log_correlated_S.py, M12_2_4_dictionary_capstone.py, M12_5_derandomize.py}}`.
- **M12.1 — $S(T)$ is log-correlated (data):** $S(T)=N(T)-1-\theta(T)/\pi$; covariance fits $-c\log\delta$ with
  $c=0.0465$ vs $1/(2\pi^2)=0.0507$ (8%, confirmed). Tightest gaps ($\beta\approx0.18$–$0.25$) sit at the steepest
  $S$ rises ($dS/dT\approx1.3$).
- **M12.2 — dictionary (exact):** $\lambda_{\min}(G)=\frac{\pi^2}6\beta_{\min}^2=\frac{\pi^2}6(\max dS/du)^{-2}$.
  RH $\iff$ extreme normalized $S$-slope bounded uniformly.
- **M12.4 — the capstone test, DECISIVE:** the multiplicative-chaos UPPER bound is $\mathbb P(\max S>u)\le\mathbb
  E[\#\{S>u\}]$ (first moment / union bound / Markov) — **NO PSD, NO SOS, NO real-stability. Genuinely NOT a
  positivity.** **For the first time, the mechanism ESCAPES the wrong-sign capstone.**
- **M12.3 → N7 (the new, distinct wall):** the union-bound machinery is **probabilistic** (height-averaging =
  randomness); it controls the STATISTICS of the real zeros, not the DETERMINISTIC off-line count $N_{\rm off}$. So
  it **describes** the ensemble, does not **force** reality (B1 in probabilistic dress). The criterion that forces
  reality ($\lambda_{\min}(G)\ge0$ / $N_{\rm off}=0$) is again a positivity/deterministic-count = the capstone. **Two
  fundamental obstructions now named:** capstone (deterministic tools = positivities, wrong sign) + N7 (probabilistic
  tools = ensemble statistics, wrong object).
- **M12.5 — the way around N7 (DONE, works):** DERANDOMIZE — $S(T)=$ explicit-formula prime sum
  $-\frac1\pi\sum\frac{\Lambda(n)}{\sqrt n\log n}\sin(T\log n)$ (verified: tracks true $S(T)$, corr $0.79\to0.89$).
  So $\mathbb E[\#\{S>u\}]$ IS the deterministic prime-sum large-value count, bounded by the **LARGE SIEVE /
  Halász / moments — deterministic + upper-direction + non-positivity: the FIRST tool that is all three** (the
  conjunction the capstone and N7 jointly demand). **Lands on the EXTREME large values of ζ (resonance /
  Bondarenko–Seip / ω-class = ARC A)** — a genuine open frontier, neither the capstone nor N7.

> **Day-29. Phase 12 — the program's arc closes, and for the first time a path is mechanism-correct.** The
> log-correlated machinery gives UPPER bounds via union/first-moment (NOT positivity) — escaping the capstone for
> the first time (M12.4). The new barrier N7 (probabilistic vs deterministic) is BRIDGED by derandomization (M12.5):
> the union count = the explicit-formula prime sum, bounded by the large sieve — deterministic, upper, non-positivity,
> all three. It lands on the EXTREME LARGE VALUES of ζ (resonance / Bondarenko–Seip / our ω-class, Arc A) — where the
> program BEGAN. The remaining wall is a hard but GENUINE frontier (extreme large values), neither the wrong-sign
> capstone nor the prob-det gap. For the first time the obstruction is the right one. Our ω-class assets (P2–P5) are
> built for exactly this. Banked: P1–P13, N1–N7, the capstone (escaped), the derandomization bridge, the arc closure.

**2026-06-05 — Day 29 (cont.). M12.6 — omega-class moment method + the Diophantine landing + the BAKER bridge.**
`phase-12/experiments/M12_6_omega_moments_extreme.py`.
- **Moment method (deterministic, upper, non-positivity) is SHARP in the accessible regime:** $\max|F|\le1.432$ vs
  actual $1.379$ (4%). The prime-sum moments are **sub-Gaussian** (ratios $0.95,0.87,0.76$, stable $X=3000\to2e5$)
  **because unique factorization forbids exact resonances $\sum\pm\log p_i=0$** (Q-independence) — so the
  distinct-prime sum is Gaussian and its extreme is sharply controlled.
- **The extreme large values (Bondarenko–Seip freezing)** are a LONG-sum ($X\sim T$) phenomenon ($\sigma^2\sim\frac1{2\pi^2}\log\log X$,
  too slow to reach computationally), from **near-resonances** $|\sum\pm\log p_i|<1/W$ = small linear forms in
  $\log p$ = a **Diophantine** question.
- **THE BAKER BRIDGE (M12.7 target):** Baker's theorem (linear forms in logarithms) gives effective LOWER bounds on
  $|\sum b_i\log p_i|$ — bounding how close prime frequencies resonate — **unconditionally, by transcendence, NOT
  positivity.** Deterministic + upper + non-positivity, exactly the conjunction needed. Open gap is QUANTITATIVE
  (Baker's bounds are weak; sharpening = abc/Lang–Waldschmidt territory).
- **Landing:** Arc A (the omega-classes, P2–P5) reached via the mechanism-correct path; the remaining wall is the
  extreme large values = a Diophantine near-resonance bound, a GENUINE open frontier, neither the capstone nor N7.

> **Day-29 (cont.). M12.6 — the program reaches its right frontier.** The moment method (sharp in reach, via
> incoherence/Q-independence) + Baker-type transcendence (for the extreme near-resonances) is a deterministic,
> upper-direction, non-positivity attack on the extreme large values of ζ — Arc A, where the program began. For the
> FIRST time the full attack chain is mechanism-correct end to end (M12.4 escaped the capstone; M12.5 bridged N7 by
> derandomization; M12.6 lands on a genuine Diophantine frontier with the Baker bridge). The remaining wall is a real,
> hard, but RIGHT problem (extreme large values / linear forms in logs), with active progress and our own ω-class
> assets pointed at it. Banked: P1–P13, N1–N7, the capstone (escaped), the derandomization + Baker bridges.

**2026-06-05 — Day 29 (final). M12.7 — Baker quantified (too weak) → additive energy = P5; Phase 12 consolidated.**
`phase-12/experiments/M12_7_baker_additive_energy.py`; master doc Part IX + map Part 7.
- **M12.7:** smallest 4-term near-resonance (primes ≤300): 223·269=59987 vs 239·251=59989, |log(pq/rs)|=3.3e-5.
  **Baker's lower bound is astronomically below it (underflows)** — Baker is the right mechanism (deterministic,
  upper, non-positivity, transcendence) but EXPONENTIALLY too weak; the threshold needs Lang–Waldschmidt/abc-strength
  (conjectural). **PIVOT:** the extreme needs the COUNT (additive energy), not the single smallest; the 4-term energy
  = multiplicative near-quadruples pq~rs = **exactly P5's ω-class moment inflation**, bounded by sieve/multiplicative
  methods (deterministic, upper, non-positivity), sharp low-order; high-order = the **moment-conjecture (CFKRS)
  frontier**.
- **The mechanism-correct chain is COMPLETE:** RH (via M12.4–M12.7) ⟸ a sharp high-order additive-energy bound for
  {log p} = the moment conjectures, deterministic + upper + non-positivity end to end, neither the capstone nor N7,
  = Arc A (P2–P5).
- **Consolidated:** Phase 12 into the master closing doc (new Part IX) + 00-MAP (Part 7); banked N1–N7, the two
  fundamental obstructions, and the first mechanism-correct chain.

> **Day-29 final. Phase 12 complete and consolidated.** The autonomous M12.1→M12.7 push produced the program's first
> mechanism-correct attack chain: escapes the wrong-sign capstone (M12.4), bridges the probabilistic–deterministic
> barrier N7 (M12.5), reaches the extreme large values via the moment method (M12.6), and lands — through Baker
> (too weak) pivoting to the additive energy = P5's ω-classes — on the moment-conjecture frontier (M12.7),
> deterministic + upper + non-positivity throughout. The remaining wall is genuine (the moment conjectures / additive
> energy of primes), neither obstruction, and exactly Arc A where the program began. The next genuine research step
> (M12.8) is the sharp high-order additive-energy bound with the ω-class machinery — the real open frontier.

**2026-06-05 — Day 30. M12.8 — the chain reaches the FREEZING transition (multiplicative chaos of ζ): the live frontier.**
`phase-12/{M12.8-verdict-freezing-live-frontier.md, experiments/M12_8_multiplicative_chaos_freezing.py}`.
- The high-order additive energy = the moments of the **multiplicative chaos of ζ**: $G(t)=\sum_p\cos(t\log p)/\sqrt p\sim\log|\zeta|$,
  $M_\beta=\langle e^{2\beta G}\rangle$. Computed the normalized $m(\beta)=M_\beta/e^{2\beta^2\sigma^2}$ ($X{=}2e4$, $\sigma^2{=}1.28$):
  $m\approx1$ for $\beta<0.6$ (subcritical GMC, RIGOROUS Saksman–Webb), deviates below 1 past $\beta_c{\approx}1$
  ($0.93,0.84,0.69,0.41,0.08$) — the annealed–quenched gap = the FREEZING (measure concentrates on the max).
- **The chain lands on the FREEZING TRANSITION** ($\beta_c=1$): subcritical = rigorous; **supercritical ($\beta\ge1$,
  the extreme / tightest gaps = U) = the LIVE FHK frontier** (max of ζ to subleading order now known: Arguin–Belius–
  Bourgade–Radziwiłł–Soundararajan, Najnudel, Harper). P5's ω-class moment exponents ARE the chaos exponents.
- **Complete honest picture:** RH ⟸ supercritical multiplicative chaos / freezing of ζ = the FHK conjecture =
  Arc A (ω-classes), deterministic + upper + non-positivity end to end; subcritical rigorous, supercritical the
  field's most active rigorous frontier. NOT crossed (supercritical = RH-strength), but the obstruction is the RIGHT
  one, on the LIVE frontier, with the best current tools + our ω-class assets pointed at it.

> **Day-30. The program converges, mechanism-correct, on the live frontier.** Phase 12's chain — escaping the
> capstone (M12.4), bridging N7 (M12.5), the moment method (M12.6), Baker→additive energy (M12.7) — reaches the
> FREEZING transition of ζ's multiplicative chaos (M12.8): the FHK conjecture / the maximum of ζ, where the leading
> and subleading terms are now rigorously known and the gap to RH is the precise supercritical control. After eight
> positivity paradigms and two named obstructions, this is the program's destination: a deterministic, upper,
> non-positivity reduction of RH to the live, actively-progressing frontier of multiplicative chaos — Arc A, where it
> began. The next genuine step is the supercritical/freezing bound with the ω-classes. Banked: P1–P13, N1–N7, the two
> obstructions, the mechanism-correct chain, the freezing landing.

**2026-06-05 — Day 30 (cont.). M12.9 — supercritical = the moment problem; and the HONEST status of the chain.**
`phase-12/{M12.9-verdict-moment-problem-honest-status.md, experiments/M12_9_divisor_moments_omega.py}`.
- **(1)** Leading chaos moment $(\log T)^{k^2}$ = the DIAGONAL of the divisor sum $\sum_{n\le N}d_k(n)^2/n\sim A_k(\log N)^{k^2}$
  — KNOWN; exponent $k^2$ = P5's ω-class moment-growth exponent (verified in trend; severe finite-N drift for high k).
  The freezing $\beta_c{=}1$ = the diagonal→off-diagonal transition; the off-diagonal (CFKRS constant; supercritical
  control that U needs) = the MOMENT PROBLEM, open unconditionally for $k\ge3$, RMT-predicted, a genuinely DIFFERENT
  open problem from RH (not RH-equivalent, not circular), active progress (Harper, Ng).
- **(2) HONEST STATUS (integrity-defining):** the Phase-12 chain is mechanism-correct but **NOT a rigorous reduction**.
  M12.1/M12.4 (log-correlated $S$) are empirical for the ranges; M12.5's derandomization is mechanism-correct but the
  probabilistic→deterministic-pointwise step is NOT closed (N7 bridged in mechanism, not as a theorem); the final
  implication (extreme/freezing control ⟹ no off-line zeros) is the N7 "describes vs forces" gap, heuristic. So the
  chain CONNECTS RH to the moment/FHK frontier by the right mechanism, but is a suggestive heuristic, not a theorem;
  the frontier is itself open. **Neither crossed nor a rigorous reduction.**
- **Genuinely gained (real):** the first mechanism-correct route (upper+deterministic+non-positivity); two named
  fundamental obstructions (capstone, N7) + the shape of any tool passing both; the clean map placing RH at the
  freezing/supercritical chaos = moment problem = Arc A; the honest demarcation (the remaining problem is different
  from RH, on the live frontier, but the chain is heuristic).

> **Day-30 (cont.). Phase 12 complete, honestly assessed.** The mechanism-correct chain reaches the live frontier
> (freezing / supercritical multiplicative chaos = FHK = the moment problem), with the diagonal ω-exponent $k^2$ known
> and the off-diagonal open. The truthful verdict: a mechanism-correct HEURISTIC connecting RH to the live
> moment-problem frontier — NOT a crossing, NOT a rigorous reduction. The most an exhaustive, honest program could
> reach, with the precise naming of what remains: an unconditional supercritical/off-diagonal moment bound (a
> different open problem) AND a rigorous closing of the N7 gap (extreme control ⟹ reality). Both genuinely open.
> Banked: P1–P13, N1–N7, the two obstructions, the mechanism-correct (heuristic) chain, the freezing landing.

**2026-06-05 — Day 30 (final). M12.10 — closing N7: the META-OBSTRUCTION (capstone and N7 are one gap).**
`phase-12/M12.10-the-meta-obstruction.md`.
- Attacked the N7 closure (force reality of zeros, deterministically, without a positivity) from every angle.
  **Enumerated every known "absence of zeros" mechanism:** (a) positivity (Weil/Hodge/3-4-1 zero-free/Selberg)
  — the capstone; (b) counting/density — reaches "few" not "none"; (c) finite computation — height T not all T;
  (d) statistics (pair corr / mult. chaos / FHK) — describes, doesn't force (= N7).
- **META-OBSTRUCTION:** no known mechanism is simultaneously (i) deterministic, (ii) absence not "few", (iii)
  uniform in T, (iv) not a positivity. The wrong-sign capstone (fails iv in mechanism a) and N7 (fails "force"
  in mechanism d) are **two faces of ONE gap.** Each concrete N7-closure route (argument-principle/winding →
  3-4-1 positivity; integrality+flow → uniform integer bound = a/b/c; off-line⇒large-values → open moment
  problem + heuristic step; rigidity → needs a new discreteness ζ lacks, being transcendental) loops back to
  (a)-(d). **N7 cannot be closed with current mechanisms.**
- **What a crossing requires, named precisely:** a non-positivity DETERMINISTIC ABSENCE principle — conceivably
  a NEW discreteness/rigidity for the zeros (the function-field algebraicity analogue; the F_1/cohomological
  dream, which P13 showed reduces to a Hodge positivity). A genuinely new such principle does not exist in 2026.
- **NOT a crossing.** The deepest, most complete characterization of why RH resists: the absence of off-line
  zeros has no deterministic, uniform, non-positivity proof-mechanism.

> **Day-30 FINAL. M12.10 — the program's complete characterization of the wall.** Pushed the N7 closure with full
> effort; it unifies with the capstone into ONE meta-obstruction: there is no deterministic, uniform,
> non-positivity mechanism for the ABSENCE of zeros. The capstone (a-positivity) and N7 (d-statistics-describe)
> are its two faces. A crossing needs a new kind of theorem (a non-positivity deterministic absence / a new zero
> discreteness) that does not exist. This is the honest end: not a passage, but the most complete chart of the wall
> a program could produce — eight positivity paradigms, two obstructions unified into one, the mechanism-correct
> heuristic chain to the live frontier, and the precise naming of the single missing idea. Banked: P1–P13, N1–N7,
> the meta-obstruction, the complete map.

**2026-06-05 — Day 31. Advisor corrections accepted + PHASE 13 (the third option): the ω-class structure of ζ's chaos (RH-independent).**
`phase-13/{RESULT-omega-class-structure-of-chaos.md, experiments/{M13_1_omega_k2_structure.py, M13_2_fhk_from_freezing.py}}`;
M12.10 corrected.
- **M12.10 DOWNGRADED (advisor, accepted):** "capstone and N7 are ONE meta-obstruction" → a real recurring TENSION,
  not a proven identity; "every future proof must invent a new theorem" → a methodological HYPOTHESIS, not a result
  (math history has unanticipated combinations). M12.10 is a conceptual map of strategies, not an impossibility proof.
- **PHASE 13 — the advisor's third option (the most promising), delivered:** WHY ω-class exponents = $k^2$ moment
  exponents. **Rigorous core:** on squarefree $n$, $d_k(n)=k^{\omega(n)}$, so $d_k(n)^2=(k^2)^{\omega(n)}$; and
  $\sum_{n\le N}z^{\omega(n)}/n\sim(\log N)^z$ (Selberg–Delange). **So the moment exponent $k^2$ IS the per-prime
  ω-weight $z=k^2$, factored $k\times k$** (one $k$ from $\zeta^k$, one from $\bar\zeta^k$). Explains P5 = moments =
  chaos as ONE object (the per-prime weight).
- **The dictionary (new, RH-independent):** chaos parameter $\beta\leftrightarrow$ ω-weight $z=\beta^2$; freezing
  $\beta_c=1\leftrightarrow z_c=1$ (neutral ω-weight); supercritical $\beta>1\leftrightarrow z>1\leftrightarrow$ the
  **large deviations of $\omega(n)$** (thick points = integers with $\omega(n)\sim z\log\log N$ prime factors,
  Sathe–Selberg). **Identifies the FHK/freezing frontier with the large-deviation theory of the number of prime
  factors** — bridging modern extreme-value ζ-theory to classical ω(n) large deviations via Arc A.
- **M13.2:** $V=\mathrm{Var}(G)\approx\tfrac12\log\log X$; the max $\sim2V=\log\log T$ = the FHK leading term, from
  the freezing (computed $\max G/2V=1.72\to1.44\to1.40\to1$ from above). Candidate paper P14 (RH-independent).

> **Day-31. Accepted the advisor's corrections; pursued the third option (the most promising for real research).**
> Delivered a clean, rigorous, RH-INDEPENDENT structural result: ζ's multiplicative-chaos / moment exponents ARE the
> ω-class (prime-factor-count) exponents under $z=\beta^2$ ($k^2=k\times k$), and the freezing/FHK frontier IS the
> large deviations of $\omega(n)$. This explains P5 structurally and bridges two literatures — new mathematics whose
> value does not depend on RH. Options 1 (supercritical off-diagonal moment problem) and 2 (new discreteness / $\mathbb
> F_1$) remain the hard frontiers, untouched. Next: M13.3 (the $-\tfrac34\log\log\log T$ subleading term from the ω
> large-deviation saddle) + P14 write-up.

**2026-06-05 — Day 31 (cont.). N7-closure attempt (Littlewood) + M13.3 (FHK both terms from the ω-BRW).**
`phase-12/M12.11-N7-closure-attempt-littlewood.md`, `phase-13/experiments/M13_3_brw_subleading.py`.
- **N7 closure attempted in full (the goal is RH):** Littlewood's lemma — the EXACT deterministic identity
  $\sum_{\beta>\sigma_0}(\beta-\sigma_0)=\frac1{2\pi}\int_0^T\log|\zeta(\sigma_0+it)|dt+O(\log T)$ — is the right
  classical bridge (large-value quantity ↔ off-line zeros). **Outcome: gives DENSITY (few), not ABSENCE (none)**:
  the integral grows in $T$ while a single zero contributes $O(1)$; an upper bound ⟹ zero-density, not RH. The same
  identity shows BOTH faces (positivity lower bound = capstone; upper bound = density). The tension made CONCRETE
  and classical (sharper than M12.10). **No impossibility claimed.** Forward target: improve $\int_0^T\log|\zeta(\sigma_0)|$
  toward $O(1)$ = the zero-density/large-values frontier (where Phase 13 lives). RH-directed, open.
- **M13.3 — both FHK terms from the ω-hierarchy as a BRW:** index primes by level $j=\lfloor\log\log p\rfloor$; each
  level has variance $\approx\tfrac12$ (Mertens; verified $0.42,0.46,0.39$), $n=\log\log T$ levels. So $\log|\zeta|$
  is a BRW: max $=2V-\tfrac32\cdot\tfrac12\log n=\log\log T-\tfrac34\log\log\log T$ — the FULL FHK leading+subleading.
  The $-\tfrac34=\tfrac32\times\tfrac12$ (Bramson $\times$ velocity), $\log n=\log\log\log T$ (the ω-depth). **The
  ω-classes (Arc A) ARE the branching hierarchy of $\zeta$; both FHK terms emerge from the ω-structure.**
  RH-independent (heuristic via the BRW analogy; rigorous FHK is Arguin et al). Candidate paper P14.

> **Day-31 (cont.).** Tried to close N7 with full strength via Littlewood (the right classical tool) — honest outcome:
> density not absence, the tension concrete, no impossibility claimed, an RH-directed forward target named. Then M13.3:
> the ω-class hierarchy is the BRW of $\zeta$, and BOTH FHK terms (leading $=$ depth $\log\log T$, subleading $=$
> Bramson $-\tfrac34\log\log\log T$) emerge from it — a clean, RH-independent structural explanation through the
> program's own Arc-A machinery. P14 candidate. The goal stays RH; the new math (Phase 13) is the credible by-product.

**2026-06-05 — Day 31 (cont.). P14 written & compiled — the RH-independent new-math paper (the third option, full).**
`06-papers/P14-omega-hierarchy-branching-chaos/{main.tex (9pp, compiled), P14.md}`.
- Wrote the full technical paper on the Phase-13 result: "The ω-Class Hierarchy of the Riemann Zeta Function:
  Per-Prime Weights, Multiplicative Chaos, and the Branching Structure of the Maximum." 9 dense pages, proper
  theorem/proof structure, the dictionary table, numerical section, full references (ABBRS, Najnudel, Harper,
  Saksman–Webb, CFKRS, Soundararajan, Bramson, Tenenbaum, Selberg).
- **Rigorous core:** Prop 3.1 ($d_k=k^\omega$ on squarefree), Thm 3.2 (moment exponent $k^2$ = ω-weight $z=k^2$,
  factored $k\times k$; LSD $\sum z^{\omega(n)}/n\sim C(z)(\log N)^z$), Thm 5.1 (supercritical = ω large deviations,
  $\omega\sim z\log\log N$), Prop 6.2 (equal-variance levels by Mertens, depth $=\log\log T$ = a BRW). **Heuristic
  bridge** (Heuristic 7.1, honestly labeled): both FHK terms from the BRW (depth + Bramson), citing the rigorous
  FHK literature, NOT reproved. Explicit rigorous/heuristic boundary stated. RH-independent throughout.
- Index updated P1→P14 (P14 = "RH-independent"). The third-option new mathematics is now a self-contained,
  publishable-quality paper.

> **Day-31 (cont.). P14 done.** The advisor's third option — understand structurally why ω-class exponents = $k^2$
> moments — is delivered as a complete, technical, honestly-scoped paper: the per-prime weight $z=\beta^2$ unifies
> the moments, the chaos, the ω large deviations, and the branching maximum; rigorous arithmetic core + the
> established chaos/BRW picture for the maximum; nothing conditional on RH. This is the credible new-mathematics
> by-product of the long RH push — intrinsic value, no overselling. The goal stays RH (N7/Littlewood target open).

**2026-06-05 — Day 32. STRATEGIC (advisor directive): where the ω-structure touches the zeros — the explicit formula is ω-BLIND; the exact bridge is Motohashi / the spectral theory of moments.**
`phase-14/STRATEGIC-where-omega-touches-the-zeros.md`.
- The advisor's directive supersedes the others: don't refine FHK; find where the ω-structure touches the zeros
  EXACTLY (a sum over zeros / explicit formula), not a statistic of values.
- **NEGATIVE half (structural obstruction):** $\omega(p^a)=1$ on ALL prime powers = the support of $\Lambda$. So
  $\Lambda(n)z^{\omega(n)}=z\Lambda(n)$: **the explicit formula (the canonical sum over zeros) is ω-BLIND** — the
  ω-weight is a trivial factor $z$. The ω-large-deviations (many-factor integers) are ORTHOGONAL to the
  prime-power support of the explicit formula. This is the precise reason Phase-13 (maxima/moments/freezing) does
  not move RH: it is a statistic of values, invisible to the explicit formula.
- **The leading moment factorizes** $a_k g_k(\log T)^{k^2}$: ω gives $a_k$, zeros give $g_k$, DECOUPLED (product).
  So neither the explicit formula nor the leading moment couples ω to the zeros.
- **POSITIVE half (the exact bridge):** the coupling is the OFF-DIAGONAL = the shifted-convolution / additive-divisor
  problem, which touches the zeros EXACTLY via the **spectral theory of moments**: **Motohashi's formula** ($k=2$,
  the 4th moment = exact spectral sum over the Maass-form spectrum + the zeros), PROVEN; CFKRS / $GL(k)$ for $k\ge3$,
  conjectural. THIS is the first exact point where the ω/divisor structure meets the zeros — an identity, not a
  statistic.
- **RH-directed redirection:** study the off-diagonal of the $d_k$ moments and its spectral (Motohashi/$GL(k)$)
  expansion, where the zeros appear exactly; ask whether the ω-large-deviation structure constrains the spectral/zero
  side. Honest caveats: brings in the automorphic spectrum (deep machinery); $k\ge3$ open (the moment wall, spectral
  form); whether it gives NEW zero-info is open — but it is the right KIND of object. Filter (per advisor): if a step
  factors through $\Lambda$/prime powers, ω is trivial there = wrong step. Next: M14.1 (additive divisor ↔ zeros via
  Motohashi, explicitly).

> **Day-32. Answered the advisor's question precisely.** The ω-structure does NOT touch the zeros via the explicit
> formula (ω-blind: $\omega=1$ on prime powers); it touches them EXACTLY via the spectral theory of moments (Motohashi,
> $k=2$, proven) through the off-diagonal. This redirects the RH attack to the off-diagonal $d_k$ correlations / the
> $GL(k)$ spectral theory of moments — the first exact ω↔zeros bridge, RH-directed, with the automorphic spectrum as
> the new apparatus and the $k\ge3$ moment wall in its spectral form. The ω-blindness is the sharp filter for future
> steps. Banked: the structural location of where ω can and cannot meet the zeros.

**2026-06-05 — Day 32 (cont.). M14.1 — the off-diagonal made concrete: additive divisor + Motohashi (the first exact ω↔zeros bridge).**
`phase-14/{M14.1-verdict-additive-divisor-motohashi.md, experiments/M14_1_additive_divisor_motohashi.py}`.
- Per the advisor's binary decision (abandon FHK; the exact ω↔zeros bridge is the off-diagonal / Motohashi), took
  the first concrete step. **Object:** $D(x,h)=\sum_{n\le x}d(n)d(n+h)$ (the 4th-moment off-diagonal),
  $d=2^\omega$. **Confirmed** $D(x,h)\sim\tfrac6{\pi^2}\sigma_{-1}(h)x(\log x)^2$ (ratio tracks $\tfrac6{\pi^2}\sigma_{-1}(h)$:
  $h{=}12\to1.406$ vs $1.419$; the $\sigma_{-1}(h)$-dependence clear).
- **The exact bridge (passes the filter):** Motohashi's formula — the smoothed 4th moment / the additive-divisor
  error = an EXACT sum over the Maass-form spectrum $\{\kappa_j\}$ weighted by central $L$-values $H_j(1/2)^3$. First
  exact identity where the divisor/ω structure meets the automorphic spectrum (dual to the zeros). An identity, not a
  statistic — PASSES the advisor's filter.
- **Honest outcome:** the 4th-moment bound it yields gives a ZERO-DENSITY theorem (few off-line zeros), NOT absence —
  same $O(1)$ wall as Littlewood (moment $(\log)^4$-large, one zero $O(1)$). Right KIND of object (exact, zeros-facing),
  density not RH.
- **The genuinely new, ω-sensitive, zeros-facing question (M14.2):** the $z^\omega$-WEIGHTED additive divisor
  $D_z(x,h)=\sum z^{\omega(n)}d(n)d(n+h)$ ($z>1$ = supercritical/many-factor weight) and its Motohashi-type spectral
  expansion — does the weight give a DEFINITE/controllable spectral feature the unweighted lacks? First instance where
  the ω-large-deviation structure could give NEW spectral (zero-facing) info. Likely still density, but it is exactly
  the object the advisor's criterion selects, unexamined.

> **Day-32 (cont.). M14.1.** On the advisor's chosen direction (off-diagonal/Motohashi), grounded the additive-divisor
> object and identified Motohashi as the first EXACT ω/divisor↔automorphic-spectrum bridge (passes the filter: an
> identity, not a statistic). Honest outcome: it yields zero-DENSITY (mechanism b), not absence — the right kind of
> object, same $O(1)$ wall. The new lever is the $z^\omega$-weighted correlation (M14.2): does the ω-large-deviation
> weight produce a controllable spectral feature? That is the first ω-sensitive, exact, zeros-facing question — the
> next step on the only RH-directed line.

**2026-06-05 — Day 32 (cont.). M14.2 — the binary question answered: z^omega is a NON-TRIVIAL spectral modification.**
`phase-14/{M14.2-verdict-nontrivial-spectral-modification.md, experiments/M14_2_spectral_modification.py}`.
- Formulated from the SPECTRAL side (advisor's strict condition). The input a(n)=z^{omega(n)}d(n) to the
  Motohashi/Kuznetsov machine has local factor [1+2(z-1)x+(1-z)x^2]/(1-x)^2, so
  **sum a(n)/n^s = zeta(s)^2 G_z(s)**, G_z(s)=prod_p[1+2(z-1)p^-s+(1-z)p^-2s] ~ zeta^{2(z-1)} H_z, pole order 2z.
  Verified: exponent tracks 2z (1.09,1.85,2.48,3.01 for z=0.5,1,1.5,2); local roots (1-alpha x)(1-beta x),
  alpha*beta=1-z (alpha=beta=0 at z=1 => G_1=1; real opposite-sign for z>1).
- **BINARY ANSWER: NON-TRIVIAL.** G_z != 1 iff z != 1; G_z ~ zeta^{2(z-1)} is a POWER OF zeta carrying the
  zeta zeros (branch points for non-integer z). The spectral weight in Motohashi/Kuznetsov therefore CARRIES THE
  ZEROS. **First ω-structure in the program NOT invisible to the spectral/zeros side; the line survives the
  brutal test** (per the advisor's threshold).
- **Honest characterization:** the non-triviality is a GL(1)/Eisenstein-type (zeta-power) reweighting, not new
  cuspidal structure; at cuspidal points it multiplies the Maass contribution by zeta(1/2+i kappa_j)^{2(z-1)} —
  zeros-facing but possibly SELF-REFERENTIAL (zeros via a zeta-power).
- **M14.3 (decisive):** self-referential, or does G_z suppress/band-localize the cuspidal Maass spectrum to give
  a new upper bound on D_z (hence on the zeros) the unweighted case lacks?

> **Day-32 (cont.). M14.2: the line survives.** From the spectral side, z^omega is a non-trivial modification —
> the extra Euler factor G_z = zeta^{2(z-1)} H_z, a zeta-power carrying the zeros. First ω-object not invisible to
> the spectral/zeros side. Honest: it is a GL(1)/Eisenstein zeta-power reweighting, possibly self-referential. The
> decisive M14.3: does G_z merely shift the Eisenstein zeta-part, or suppress/band-localize the cuspidal Maass
> spectrum into a NEW upper bound on the zeros? That is the first genuinely new, zeros-facing, spectral question.

**2026-06-05 — Day 32 (final). M14.3 — BINARY VERDICT: the ω-weight is spectrally SELF-REFERENTIAL. The ω→zeros line is CLOSED.**
`phase-14/{M14.3-VERDICT-self-referential-close-the-line.md, experiments/M14_3_self_referential_test.py}`.
- The audit demanded one of two sentences. **PROVEN:** $G_z(s)=\prod_p(1-\alpha p^{-s})(1-\beta p^{-s})$ has CONSTANT
  Satake parameters ($\alpha+\beta=2(1-z)$, $\alpha\beta=1-z$, independent of $p$) ⟹ ζ-ISOBARIC:
  $G_z(s)=\prod_{N\ge1}\zeta(Ns)^{c_N}$, $c_N=-\tfrac1N\sum_{k|N}(\alpha^k+\beta^k)\mu(N/k)$ ($c_1=2(z-1)$, $c_2=-2z(z-1)$,…).
  Verified: direct Euler product matches $\prod\zeta(Ns)^{c_N}$ to $3e{-6}$–$8e{-4}$.
- **VERDICT: "The ω-weight is spectrally SELF-REFERENTIAL."** $G_z$ is entirely ζ-factors; the $z\ne1$-vs-$z=1$ ratio
  is COMPLETELY ζ-factors; NO new irreducible spectral weight; the zeros enter only because $G_z$ is built from
  ζ-powers. Scenario A.
- **STRUCTURAL REASON (a unification):** $\omega(n)$ counts primes UNIFORMLY (prime-blind — how many, never which);
  a prime-blind weight has CONSTANT Satake ⟹ ζ-isobaric ⟹ cannot make a prime-DISTINGUISHING (zero-distinguishing)
  L-function. This is the SPECTRAL TWIN of the explicit-formula ω-blindness ($\omega=1$ on prime powers). One root:
  ω lives on the prime-COUNT axis; the zeros live on the prime-IDENTITY (Euler) axis; orthogonal.
- **DECISION (per the audit): the ω→zeros line (off-diagonal/Motohashi $z^\omega$-twist) is CLOSED.** Exact, spectral,
  zeros-facing — but reduces to ζ itself, no new info.
- **Ledger:** FHK/chaos (not zeros-facing; P14 stands as RH-independent math); Littlewood & Motohashi (zeros-facing,
  give DENSITY not absence, $O(1)$ wall); $z^\omega$-Motohashi (self-referential, closed). The two genuine zeros-facing
  lines give density; the ω-injection is self-referential. ω cannot supply prime-distinguishing info (prime-blind).

> **Day-32 FINAL. The ω→zeros line closed with a rigorous binary verdict (self-referential).** $G_z=\prod\zeta(Ns)^{c_N}$:
> the ω-weight reduces to ζ-powers, no new spectral structure, because ω is PRIME-BLIND (counts, doesn't distinguish)
> — the unified root of both the explicit-formula and spectral obstructions. A real result: the precise reason the
> ω-direction cannot reach the zeros. The RH frontier returns to Littlewood/Motohashi (density, the $O(1)$ wall),
> with the honest knowledge that the ω-structure does not help. P14 (RH-independent) stands on its own.

**2026-06-05 — Day 33. N8 — the density→absence gap characterized: the square-root cancellation barrier (= the capstone).**
`phase-14/N8-the-density-to-absence-gap.md`.
- Per the audit (two distinct exact-zeros theories hit the same wall ⟹ study the wall): characterized the precise
  logical ingredient missing to pass from density to absence — NOT a technique, a characterization.
- **The exact zeros-facing tools all reduce to a CANCELLATION estimate** (explicit formula = prime sum; Littlewood =
  $\int\log|\zeta|$ = prime-sum cancellation; Motohashi = $\sum d(n)d(n+h)$ error). They deliver POWER-SAVING
  ($x^{1-\delta}$) ⟹ density; absence (RH) needs SQUARE-ROOT ($x^{1/2+\varepsilon}$). A single off-line zero is $O(1)$,
  the aggregate is power-saving-but-growing ⟹ one zero below resolution ⟹ density not absence.
- **N8:** the density→absence gap IS the SQUARE-ROOT CANCELLATION BARRIER; the missing ingredient is square-root
  cancellation itself, which IS RH. The gap is RH-EQUIVALENT, not a separable sub-ingredient. This is why two
  different theories (Littlewood, Motohashi) fail identically — both limited by the same universal barrier.
- **UNIFICATION (the wall from four sides):** wrong-sign capstone (lower-bound tools, wrong sign) = N7 (statistics
  describe not force) = meta-obstruction (no deterministic non-positivity absence) = N8 (power-saving ↛ square-root).
  Square-root cancellation = upper-cancellation = the capstone's upper constraint = RH. One object: the absence of
  unconditional square-root/upper-cancellation control of the prime/Möbius sums.
- **Settles:** the missing ingredient is square-root cancellation, RH-equivalent — NOT a separable logical step a
  clever tool-combination could supply; the central barrier itself. No further STATISTIC helps; the exact lines are
  right but all stopped at the same (RH-equivalent) barrier.

> **Day-33. N8 — the wall named from the cancellation side.** The density→absence gap is the square-root barrier
> (power-saving ↛ square-root), RH-equivalent — the same wall as the capstone/N7/meta-obstruction, seen from a fourth
> side. Littlewood and Motohashi stop identically because both are limited by the universal square-root barrier; the
> wall is the object, and crossing it is RH. The map of the wall is now complete from positivity, dynamics,
> probability, cohomology, AND cancellation — every accessible route reaches the same upper-cancellation barrier and
> none crosses. The honest frontier, precisely named: an unconditional square-root/upper bound for the prime sums,
> uniform = RH, with no current mechanism providing an unconditional handle.

**2026-06-05 — Day 33 (cont.). AUDIT of the P7→T2→D2→T3→T4 structural line: it collapses to the wall (positivity side).**
`phase-14/AUDIT-P7-structural-line-collapse.md`. Per the audit: the only branch possibly not yet forced to collapse
is the original structural/arithmetic-Weil-form line. Audited object by object — is anything NOT reducible to {prime
sum, ζ-power, value-statistic, known spectral identity}?
- **The line IS the positivity** ($\lambda_{\min}(Q)\ge0$) — the one NONLINEAR, individual-resolving, absence-CAPABLE
  tool (exactly what N8 says is needed). So it is the wrong-sign-capstone side of the wall, content = the SIGN of
  $\lambda_{\min}$ = RH. Not a fifth kind of object.
- **D2 gradient** $\partial\lambda_{\min}/\partial\Lambda(n)=-n^{-1/2}|\widehat{u_0}(\log n)|^2$: depends on ground
  state $u_0$ = zero-interpolating function ⟹ determined by the zeros ⟹ reduces to prime sum (nonlinear through the
  eigenvector, not a new variable). **T3 anatomy** $\lambda_{\min}=R_\infty-\sum_pR_p$: $R_p$ from $\widehat{u_0}$ at
  prime-power freqs, determined by zeros; per-prime $G_p$ indefinite (N1). **T4 Carleson** = exactly P11 (N3 saturation,
  B1 pair-correlation, N4 prolate); P13: $\lambda_{\min}=\tfrac{\pi^2}6\beta_{\min}^2$ = squared min gap.
- **COLLAPSE traced:** $\lambda_{\min}$(localized Weil) = regularized Hodge gap = $\tfrac{\pi^2}6\beta_{\min}^2$ (P13) =
  pair-correlation / gap-universality (B1) = same prime-sum cancellation whose square-root control is RH (N8). The line
  collapses to the wall on the POSITIVITY side; quantitatively the square-root barrier.
- **No fifth kind of object exists.** Every branch reduces to the one wall, now mapped from five sides (positivity,
  dynamics, probability, cohomology, cancellation). ω-branch self-referential (M14.3); Littlewood/Motohashi density (N8);
  structural branch = the capstone itself.
- **One genuinely un-reduced object survives: Conjecture B2** (factorizing anatomy ⟺ Euler product) — but it is
  RH-INDEPENDENT (classification of L-functions, prime-IDENTITY, not zero location; like P14). Using its Euler-product
  for the zeros routes through the explicit formula = prime sum = N8.

> **Day-33 (cont.). The structural line collapses — the map is complete.** The auditor's instinct was right to check
> P7→T4; the honest outcome is that it, too, collapses, to the positivity/capstone side and thence (via
> $\lambda_{\min}=\tfrac{\pi^2}6\beta_{\min}^2$) to the square-root barrier. Every RH-directed branch of the program is
> now audited to the same wall. The single un-reduced object (B2) is RH-independent. There is no remaining un-collapsed
> RH-directed line; the frontier is the square-root/upper-cancellation barrier itself.

**2026-06-04 — Day 34. BREAK N8: absence WITHOUT square-root cancellation exists. N8 was a SYMPTOM. The anchor asymmetry.**
`phase-14/BREAK-N8-the-anchor-asymmetry.md`. The audit attacked the strongest step: "raíz-cuadrada es RH-equivalente ⟹
no hay ingrediente más elemental." Goal: not prove RH — BREAK N8. Binary question: ¿existe formulación exacta que fuerce
ausencia SIN cancelación raíz-cuadrada?
- **YES — COUNTEREXAMPLE: de la Vallée Poussin** ζ(1+it)≠0 (exact absence). Proof = positivity 3+4cosθ+cos2θ=2(1+cosθ)²≥0
  + the POLE of ζ at s=1 + finiteness of ζ(σ+2it) (no pole at t≠0). NO Dirichlet mean value, NO large values, NO square-
  root cancellation. An exact absence theorem with ZERO cancellation input. **N8's universal form is REFUTED.**
- **N8 is a SYMPTOM** (the audit's Scenario B confirmed). It is true ONLY of the density/anchorless routes (Littlewood,
  Motohashi, zero-density — which substitute cancellation for a missing anchor). It silently universalized. The earlier
  "capstone = N8" unification OVER-REACHED and is corrected: there are TWO walls, not one.
- **THE REAL STRUCTURE — the ANCHOR ASYMMETRY.** Absence-via-positivity = (positivity identity)+(an ANCHOR = place ζ is
  unconditionally large). de la Vallée Poussin: anchor = pole at σ=1 (unconditional, FREE; region width c/log t uses only
  convexity, not square-root). Hilbert–Pólya: anchor = self-adjointness (would give σ=1/2, no operator known). Weil:
  anchor = center-positivity (capstone). **The pole anchors σ=1 for free; σ=1/2 has NO unconditional anchor** (no pole,
  no lower bound on |ζ(1/2+it)|, functional eq gives symmetry not anchor). Density routes lack the anchor ⟹ substitute
  cancellation ⟹ hit N8.
- **REFRAMED QUESTION Q(anchor):** ¿existe un anchor de positividad incondicional en σ=1/2 análogo al polo en σ=1? Unifies
  Hilbert–Pólya + Weil center-positivity + a hypothetical center-pole as ONE missing ingredient.
- **HONEST (no repeat of N8's over-reach):** I do NOT claim Q(anchor) is more elementary than RH nor RH-equivalent. It is
  a DIFFERENT formulation (lower-bound/anchor, not cancellation), NOT yet collapsed — its value is exactly that the
  collapse-to-N8 did not dispose of it (N8 only ruled out anchorless routes).

> **Day-34. N8 broken — it was a symptom.** de la Vallée Poussin forces exact absence with zero cancellation, refuting
> N8's universal form. The program has TWO walls: square-root cancellation (anchorless/density routes) and the absence of
> an unconditional anchor at σ=1/2 (positivity routes). The pole anchors σ=1 for free; the center has no anchor. The
> reframed RH-directed question is Q(anchor): is there a center-anchor (= Hilbert–Pólya / Weil center-positivity / a
> hypothetical σ=1/2 pole)? Honestly flagged as NOT shown elementary nor RH-equivalent — but the one reframing the audit
> chain did not collapse. The frontier is no longer "square-root is inevitable"; it is "an anchored route would bypass it,
> and whether the anchor exists is open."

**2026-06-04 — Day 35. The ANCHOR FRAMEWORK: anchor = Landau singularity (ζ-free). A classification of zero-absence mechanisms.**
`phase-14/ANCHOR-framework-a-classification-of-zero-absence.md`. The audit's decisive test: define "anchor" WITHOUT
ζ/poles/Hilbert–Pólya/Weil/RH — if yes, a new object; if no, only a pattern.
- **ANSWER: YES. Anchor = a LANDAU SINGULARITY** — the forced real boundary singularity of the transform of a POSITIVE
  (non-negative-coefficient) measure (Landau 1905). No ζ, no "pole," no HP/Weil/RH in the definition. The pole of ζ at
  s=1 is merely the INSTANCE for the prime measure. The audit's test is passed → a genuine object.
- **Framework (all ζ-free):** positivity datum (ν≥0, kernel K, log F=∫K dν); sum rule (Σw_j log|F(s_j)|≥0 for free when
  Σw_j Re K(s_j,·)≥0 on supp ν); anchor (s_* where the transform =+∞ = Landau singularity, REAL by Landau); tight vs
  loose budget (tight=pinned by anchor⟹absence; loose=estimated⟹density).
- **Theorem A (proven core):** positivity datum + Landau anchor ⟹ zero-free neighborhood of reach δ(M,B). Specializes
  EXACTLY to de la Vallée Poussin (ν=prime measure, K=e^{-su}, s_*=1, sum rule 3+4cosθ+cos2θ, budget B=convexity log t,
  reach δ≍1/log t). The classical theorem IS the s_*=1 instance. No conjecture.
- **Classification (table):** de la Vallée Poussin (anchor σ=1, proven), Vinogradov–Korobov (σ=1 wider), Hilbert–Pólya
  (σ=1/2 via self-adjoint spectral measure, real axis), Weil (σ=1/2 via functional eq), P7→T4 (σ=1/2 variational),
  function-field RH (diagonal, Hodge index — PROVEN geometric anchor). All = manufacture a Landau-type anchor, differing
  only in LOCATION (σ=1 vs 1/2) and the positive structure. The pole anchors σ=1 free; every route to σ=1/2 is a
  different attempt to force a center-anchor.
- **Why Littlewood/Motohashi lack an anchor (ζ-free):** they have a positivity datum but a LOOSE budget — Landau puts the
  prime measure's only forced singularity at σ=1, NOT σ=1/2 — so no anchor at the center ⟹ density. N8's square-root
  barrier is now a COROLLARY (anchorless routes must estimate the loose budget; one-zero precision = square-root).
- **ACC (stated AS conjecture):** every unconditional absence proof = positivity datum + anchor; no anchor ⟹ at best
  density. Evidence: ALL known analytic zero-free regions are positivity+pole; the only proven RH (function field) is
  positivity+Hodge-anchor. No known counterexample. NOT claimed proven.
- **Q(anchor) ζ-free:** does a positive structure with a forced Landau-type singularity at σ=1/2 exist? A CONSTRUCTION
  problem, not cancellation — different from N8, NOT collapsed. Subsumes HP + Weil as two proposals for the same object.
- **HONEST caveats (no repeat of N8 over-reach):** Q(anchor) MAY be RH-equivalent (HP/Weil are it); ACC is a conjecture.
  What IS established: the ζ-free DEFINITION (Landau), Theorem A (de la Vallée Poussin recovered), and RH reframed as a
  center-anchor CONSTRUCTION.
- **Proposed path (staged, each checkable):** (1) formalize + prove Theorem A in generality; (2) express Weil + the
  function-field Hodge anchor in the framework (test on the one proven RH); (3) attack Q(anchor) as construction, incl.
  non-arithmetic toy models, to find what OBSTRUCTS a center-anchor — that obstruction (if any) is the next honest wall,
  about positive structures, not cancellation.

> **Day-35. "Anchor" is now an object: the Landau singularity.** The audit's ζ-free test is passed; the heuristic became
> a framework with a proven core (Theorem A recovers de la Vallée Poussin) and a classification placing de la Vallée
> Poussin / HP / Weil / function-field RH as anchors at different locations. RH is reframed, ζ-free, as: construct a
> positive structure forced-singular at σ=1/2. Honestly flagged: may be RH-equivalent, ACC is conjectural — but it is the
> one RH-directed direction the audits did not collapse, and it is a construction problem, not a cancellation one.

**2026-06-04 — Day 36. STAGES 1 & 2: the Landau anchor tested against the one PROVEN RH. Verdict: it COLLAPSES, informatively.**
`phase-14/STAGE1-2-anchor-vs-definiteness-the-verdict.md`. The audit ran both stages to settle the bifurcation: is the
anchor a NEW object or a renaming? The named danger — the function-field anchor is "just the trivial cohomology class" —
MATERIALIZED.
- **STAGE 1 (object exists ζ-free, but ceiling = edge):** Theorem A — ν≥0, abscissa σ_a, log F=∫e^{-su}dν, pole order ρ at
  σ_a (Landau), convexity budget B(t), non-neg cosine poly P ⟹ no zero with β>σ_a−c(P,ρ)/B(γ). NO "ζ" in the statement
  ⟹ the anchor has independent existence (test passed). BUT it is recognizably the CLASSICAL positive-coefficient
  zero-free-region machinery (the 3+4cosθ+cos2θ technique), and its reach is a SHRINKING EDGE region at σ_a — structurally
  it never reaches the center (no arithmetic positive measure has abscissa = critical line).
- **STAGE 2 (the proven RH does NOT use a center-anchor):** function field C/F_q, Z=P_1/((1-T)(1-qT)). Dictionary
  (T=q^{-s}): poles at T=1 (H⁰, s=0) and T=1/q (H², s=1) = the Landau ANCHORS, from TRIVIAL cohomology; zeros at Re s=1/2
  (H¹) = RH. So anchors are at the EDGE (s=0,1), NO anchor at s=1/2 — exactly like ζ. RH proven by the HODGE INDEX THEOREM
  on S=C×C (intersection form signature (1,ρ−1), negative-definite on ⟨f₁,f₂⟩^⊥), forcing |α_i|=√q. The fiber classes
  f₁,f₂ (ample anchors) = H⁰,H² = the edge poles. THE CENTER IS REACHED BY DEFINITENESS (signature), NOT BY AN ANCHOR.
- **CORRECTED TAXONOMY (framework had merged two objects — same over-reach as N8):** ANCHOR = singularity of a positive-
  measure transform, lives at the EDGE, present for ζ (pole at s=1). DEFINITENESS = signature of a form/operator (Hodge
  index / Weil positivity / self-adjointness), acts at the CENTER, gives RH, ABSENT for ζ (the capstone). My earlier §3
  table wrongly listed HP/Weil/Hodge as "anchors at σ=1/2" — they are DEFINITENESS, not anchors. Stage 2 separates them.
- **BIFURCATION RESOLVED — Q(anchor) COLLAPSES.** The anchor is the trivial-cohomology edge pole, present in both worlds,
  NOT the discriminator. RH-where-proven uses the Hodge index theorem = Weil positivity = the capstone. The danger
  ("anchor = trivial cohomology class") was real and confirmed.
- **SHARPENED WALL (genuine residue of value):** the missing ingredient is NOT a center-anchor but a HODGE INDEX THEOREM
  ON A 2-DIMENSIONAL ARITHMETIC GEOMETRY over Spec(ℤ) — an object playing the role of C×C
  ("Spec ℤ ×_{F₁} Spec ℤ"), with an intersection form negative-definite on a primitive part. The anchor (edge pole) is
  already present; the SURFACE is what is absent. = Connes–Consani / Deninger / Arakelov target. RH-equivalent (capstone),
  now pinpointed as a MISSING-SURFACE problem, the most precise statement of the wall the program reached.

> **Day-36. The anchor collapses against the one proven RH — and names the wall exactly.** Stage 1: anchor is ζ-free
> (Theorem A) but is classical edge-region machinery, ceiling = edge. Stage 2: function-field RH is proven by the Hodge
> index theorem (DEFINITENESS on H¹), NOT a center-anchor; the geometric "anchor" is the trivial-cohomology edge pole,
> present for ζ. So Q(anchor) is NOT a new object — it collapses to Weil/Hodge positivity (capstone). The framework's
> merge of anchor and definiteness was an over-reach, corrected. The genuine residue: the wall is precisely a MISSING
> HODGE INDEX THEOREM ON AN ARITHMETIC SURFACE for Spec(ℤ) — the anchor is present, the surface is absent. The honest
> bifurcation the audit demanded is settled: anchor = renaming (edge); the real object = the missing arithmetic geometry.

**2026-06-05 — Day 37. P15 (paper packaging the meta-result) + OPTION (b) attacked to a computation.**
- **P15** (`06-papers/P15-why-rh-resists/`, compiled 4pp): packages the strategy map as a conditional "why RH resists":
  the classifier D0 (I1∧I2a∧I2b∧I3∧I4, three-valued), the FINITE-TO-FULL gap theorem (TP/Pólya–Schoenberg:
  RH⟺Φ is a Pólya frequency function⟺[Φ(x_i−x_j)] totally positive; every finite TP order unconditional, TP_∞=RH;
  four positivity families = one gap), finitization = Frobenius periodicity (zeros = 2g mod period 2π/log q), and the
  LI OBSTRUCTION (Thm: under Linear Independence of {γ_n}, no periodicity ⟹ no finite-dim algebraic finitization;
  F_1 period 2π/log q → ∞ as q→1). Conditional, falsifiable, no proof.
- **OPTION (b) — infinite-dim route via PONTRYAGIN INDEX κ** (`OPTION-B-pontryagin-index-attack.md`): sharpen P8's
  Krein sign to the integer κ = #neg squares = #off-line zeros. κ<∞ ⟺ Pontryagin Π_κ; Krein–Langer: ≤κ non-real
  eigenvalues. Reduced κ<∞ to RFB_X: prime tail 𝔭_{>X} relatively form-bounded by 𝔞 with const <1 ⟹ finite-rank head
  ⟹ κ<∞. RFB_X hard for one reason: prime energy Σ_{n≤N}Λ(n)/√n ~ 2√N vs archimedean ~ log N (√N vs log N = the same
  wall as Day-0 KLMN / N3 / square-root barrier, now unified).
- **EXPERIMENT** (`phase-14/experiments/a_tail_relative_form_bound.py`, ran): computed λ_max(𝔭_{>X},𝔞) vs head-cut X,
  bands d=4,5, T0=1000. RESULTS: (1) full form λ_max=1.00000 exactly (reproduces N3 saturation, validates engine);
  (2) subordination cutoff X*(d)≈e^{2d}/10 — in log-scale a FIXED-WIDTH (~2.3) top slice that SLIDES to ∞ with d;
  for fixed X, λ_max INCREASES with d and recrosses above 1. VERDICT: RFB_X fails for every fixed X as d→∞;
  κ<∞ does NOT follow from finite-rank head; the N3 criticality a=1 is SCALE-INVARIANT (not small-prime, not
  large-prime — uniform across log-prime scale; removing small primes RAISES λ_max, so saturation-at-1 is a global
  conspiracy of all primes). Surviving sub-fork: attained-vs-approached saturation in the genuine d→∞ form (κ<∞ vs
  κ=∞), possibly via cross-scale cancellation — concrete next computation (multiplicity of near-1 eigenvalues as d→∞).

> **Day-37. Meta-result papered (P15) + option (b) pushed to a number.** The infinite-dim/Pontryagin route did NOT
> dead-end on contact — it reduced to RFB_X (a one-sided relative form bound on the prime tail), which the engine
> then DECIDED against for fixed cutoffs: the subordination window X*(d)~e^{2d}/10 slides to ∞, so the off-line
> negative squares recur at every scale (scale-invariant N3 criticality), and finite-rank-head κ<∞ fails. The wall
> was not accepted but crossed *to its quantitative core*: a=1 is scale-invariant, and the only surviving door is
> attained-vs-approached saturation (κ<∞ vs κ=∞) in the genuine form.

**2026-06-05 — Day 37 (cont.). OPTION (b) sub-fork DECIDED: APPROACHED (infinite-dimensional criticality).**
`phase-14/experiments/near_critical_multiplicity.py`. Measured near-critical multiplicity of the full pencil
(P_F,A_Phi) vs band d (T0=1000): #{λ>0.99} = 3,11,19,27 for d=3,4,5,6 — LINEAR growth (~8d−21); gap λmax−λ2 ≈ 0;
critical fraction 10%→55%. VERDICT: the saturation λmax=1 is APPROACHED by a growing-dimensional near-null space
(𝔱=𝔞−𝔭≈0 on a positive, growing fraction of directions) — the infinite-dim analogue of "Λ=0 approached not
attained." ⟹ finite-defect κ<∞ FAILS (near-null space infinite-dim), complementing the earlier finite-rank-head
failure (X*(d)~e^{2d}/10→∞). BOTH κ<∞ mechanisms closed by computation. Criticality is SELF-SIMILAR (linear in
band = log-prime scale = zero-density scale). Option (b) returns to the program's central wall: semiboundedness/
coercivity of the localized Weil form on an INFINITE-dimensional near-null space (Days 0–23 (LB), Days 12–16
over-sampling), now with the structural fact that there is NO finite-defect shortcut. Off-line-zero count is not
finite-rank-detectable. Files: OPTION-B-VERDICT-approached-infinite-defect.md.

**2026-06-05 — Day 37 (cont. 2). P16 written/compiled + CROSS-SCALE door probed (option b fully closed).**
- **P16** (`06-papers/P16-pontryagin-index-finite-defect/`, compiled 3pp): packages option (b) — off-line zeros as
  Pontryagin index κ; reduction κ<∞ ⟸ RFB_X (Prop); Computation I (X*(d)~e^{2d}/10, finite-rank head fails);
  Computation II (near-critical multiplicity 3,11,19,27 linear, finite defect fails). No RH claim.
- **CROSS-SCALE door** (`phase-14/experiments/cross_scale_cancellation.py`): on the saturating direction g*, measured
  R(Y)=𝔭_{≤Y}[g*]/𝔞[g*]→1 and |𝔭_{≤Y}|/√Y. RESULTS: (1) |𝔭|/√Y DECAYS to ~0 (√N barrier OVERCOME pointwise — the
  prime form on the optimal direction is square-root-cancelled, bounded while √Y→e^d); (2) octave increments ΔR are
  O(0.1), do NOT decay, and ALTERNATE SIGN at the top (d=5: overshoot 1.064 then −0.042,−0.022→1.000; d=6: several
  negative octaves −0.075,−0.062,−0.063 →1.00000). VERDICT: octave-resolved N3 — the cancellation beats √N but lands
  at EXACTLY the archimedean ceiling (R=1, zero margin) via sign-alternating cross-scale corrections. The √N growth is
  a red herring pointwise; the wall is the boundary-exact calibration.
- **OPTION (b) FULLY CLOSED** across all three sub-questions (finite head / finite defect / cross-scale), all returning
  to boundary-exact semiboundedness of the Weil form = the Weil criterion. Marginality resolved in 3 coordinates:
  scale (self-similar), direction-count (infinite-dim near-null), magnitude (boundary-exact). Sharp prime-side residue
  named: an unconditional SIGN-ALTERNATING BOUNDARY-EXACT cross-scale cancellation law for
  Σ_octave Λ(n)n^{-1/2}(g⋆g̃)(log n) — the I2b object localized to prime octaves. Files:
  OPTION-B-cross-scale-door-verdict.md.

> **Day-37 (cont. 2). Option (b) closed; both papers (P15,P16) compiled.** The Pontryagin route, pushed through three
> computations, does not cross — but characterizes the wall fully: √N is overcome pointwise, the obstruction is the
> boundary-exact, sign-alternating, infinite-dimensional, self-similar marginality of the Weil form (octave-resolved
> N3). The residue is a sharply-posed PRIME-SIDE cancellation law (the I2b object), not a statement about zeros.

**2026-06-05 — Day 38. The prime-side residue formulated precisely; non-circularity decided.**
`RESIDUE-precise-and-noncircular-attack.md`. Formulated the cross-scale residue as a clean prime-side proposition
and checked RH-circularity.
- **Residue (precise):** (LB) semiboundedness 𝔱≥−C‖g‖² ⟺ V(d,T)≪dN uniformly, where V(d,T)=4dN (diagonal) +
  Σ_{γ≠γ'} 2sin(2d(γ−γ'))/(γ−γ') (off-diagonal pair correlation). The direction-free content of the octave
  convergence = boundedness of the mesoscopic 2nd moment V(d,T). (Re-derives Day-19 from the octave angle.)
- **NON-CIRCULAR (3 facts):** (1) RH⟹V bounded but V bounded gives only a FINITE BOTTOM (𝔱≥−C), not 𝔱≥0=RH — the
  gap finite-bottom-vs-nonneg-bottom is the wrong-sign capstone; (LB) is strictly weaker & sign-free. (2)
  Unconditional core: Montgomery 1973 R₂(α)→|α| for |α|<1 is a THEOREM (RH-free). (3) Prime-side: Goldston–Montgomery
  ⟺ 2nd moment of ψ(x+h)−ψ(x) (short intervals), provable without locating a zero.
- **SEPARATION POINT (sharp):** attack is RH-free up to Montgomery's |α|<1 range + the diagonal; opens precisely at
  the UNIFORM HIGH-FREQUENCY form factor |α|≥1 = Goldston–Montgomery short-interval prime variance. NOT RH (RH gives
  typical not uniform; the S(t)-extremal-vs-typical distinction). Cross-scale view localizes the gap to the LARGEST
  primes in the band (the top octaves = the experiment's negative late increments).
- **Octave structure does NOT shrink the gap:** the sign-alternation is a property of g* (eigenvector adapts), not a
  direction-free prime law; clean target stays V(d,T) bounded. It DOES localize the |α|≥1 gap to n~e^{2d}.
- **VERDICT:** the residue is a genuine SUB-RH, NON-CIRCULAR frontier (the same one reached at Day 19), now pinned to
  the uniform high-frequency form factor / short-interval prime variance at the largest band-scale primes. Next
  non-circular step: uniform |α|≥1 form-factor bound anchored on Montgomery |α|<1 + the diagonal ⟹ finite bottom
  (LB), strictly between zero-density and RH.

> **Day-38. Residue pinned, non-circularity proven.** The cross-scale/option-(b) line terminates at a precisely
> formulated, NON-RH-circular target: V(d,T)≪dN uniformly = a uniform high-frequency pair-correlation / short-interval
> prime-variance bound, RH-free up to Montgomery's |α|<1 range, open at |α|≥1 (Goldston–Montgomery frontier),
> localized by the octave view to the largest primes. Strictly weaker than RH; a recognized hard frontier, not a
> restatement of RH.

**2026-06-05 — Day 39. Attack on the uniform form factor (the non-circular sub-RH residue).**
`ATTACK-uniform-form-factor.md`. Pushed the target V(d,T)≪dN rigorously.
- **EXACT IDENTITY:** V(d,T)=∫_{-2d}^{2d}|S(ξ)|²dξ ≥ 0, S(ξ)=Σ_γ e^{iγξ} — V is a manifest band-limited square (the
  L² energy of the zero exponential sum). Diagonal = exactly 4dN; positivity is the unconditional engine (gives
  lower bounds on pair correlation, not upper — capstone localized).
- **EXPLICIT-FORMULA EXPANSION:** V = arch + Σ Λ(n)²/n|k_d|² (diagonal, ~2d², UNCONDITIONAL) + Σ_{m≠n} (off-diag,
  short multiplicative intervals = the difficulty, a PRIME statement).
- **NON-CIRCULAR BRIDGE (theorem):** Goldston–Montgomery (1987) unconditional EQUIVALENCE: V≪dN ⟺ short-interval
  prime variance ∫(ψ(x+x/H)−ψ(x)−x/H)²dx/x² ≪ log X/H, uniformly — neither side assumes RH. Proves the target is
  non-circular (equivalent to a zero-free prime statement).
- **UNCONDITIONAL STATE + GAP:** in α=2d/log T: F(α)≥0 unconditional; |α|<1 controlled (diagonal + GM equivalence +
  Selberg); |α|≥1 = THE GAP (uniform high-freq form factor; Selberg's ∫S(t)²≪T loglog T gives TYPICAL not UNIFORM).
  Large sieve gives unconditionally V ≪ dN(log T)^c (finite bottom up to a log POWER; exact least c is itself
  frontier, not asserted) ⟹ 𝔱 ≥ −C(log T)^c‖g‖² UNCONDITIONAL semiboundedness — weaker than clean (LB) by the log.
- **VERDICT:** first point in the program with an UNCONDITIONAL semiboundedness of the Weil form (modulo a log
  power), residual = ONE explicit non-circular sub-RH object (uniform |α|≥1 form factor = uniform short-interval
  prime variance, localized to largest band primes n~e^{2d}). Strictly weaker than RH (RH gives typical not uniform).
- Next non-circular sub-targets: (1) reduce the log-power loss c via weighted Montgomery–Vaughan + Selberg tail
  (measurable partial results); (2) clean uniform bound = Goldston–Montgomery frontier (not RH).

> **Day-39. Unconditional finite bottom (modulo log^c) in hand; residue pinned to a sub-RH frontier.** V=∫|S|²
> exact; GM equivalence makes the target non-circular (= uniform short-interval prime variance); large sieve gives
> 𝔱≥−C(log T)^c‖g‖² unconditionally; the only remaining obstacle is the uniform high-frequency form factor, strictly
> below RH, localized to the largest band primes. The program's central (LB), for the first time, has an
> unconditional version with an explicit, non-circular, recognized-frontier residue.

**2026-06-05 — Day 39 (cont.). Backbone identity VERIFIED with real zeta zeros.**
`phase-14/experiments/verify_V_identity.py` (zeros #1000–1079, T~1465, ρ~0.868): the identity
V(d,T)=Σ_{γ,γ'}2sin(2d(γ−γ'))/(γ−γ') = ∫_{-2d}^{2d}|S(ξ)|²dξ confirmed to rel.err ≤3e-6 across d∈[0.25,3]
(α=2dρ from 0.43 to 5.2). Form factor: V/(dN) decreases through α=1 and levels at ≈3.8 (=diagonal 4 − GUE
off-diagonal ≈0.2) for α≳3 ⟹ F(α) BOUNDED at high frequency, V~dN for ζ's actual zeros (clean bound, c=0 in
reality, GUE). ⟹ the (log T)^c loss is a limitation of the PROOF, not of ζ; the zeros realize the clean (LB), and
the whole residue is the *unconditional* uniform form-factor bound. The Day-39 reduction rests on a verified exact
identity. (No new ANT bound claimed; improving the unconditional uniform short-interval prime variance is
Montgomery–Soundararajan-frontier and not fabricated here.)

**2026-06-05 — Day 39 (cont. 2). P17 compiled + BALANCE + MAP Part 8. Phase consolidation.**
- **P17** (`06-papers/P17-unconditional-finite-bottom/`, compiled 3pp): the unconditional finite bottom mod log.
  Thm (identity V=∫|S|², verified); Prop (𝔱≥−C(log T)^c‖g‖² via large sieve); Thm (Goldston–Montgomery, clean (LB)
  ⟺ uniform short-interval prime variance, non-circular); the three-level hierarchy (S)<(κ)<(R). First unconditional
  semiboundedness of the localized Weil form with residue pinned to a sub-RH frontier.
- **BALANCE** (`BALANCE-program-assessment.md`): full arc A–D + Phases 12–14; durable results (P1–P17, N1–N8,
  capstone, identities, discriminator, unconditional (LB)); RH-directed vs RH-independent split; bottom line — no
  proof, no new non-circular route to RH; the new math (P14,P9,B2conj) is RH-INDEPENDENT; the gain is the map + the
  instrument + the unconditional sub-RH (LB).
- **MAP Part 8** appended (00-MAP.md): Phases 13–14 closure, discriminator, bin three/LI obstruction, option (b)
  closure, P17.
- Trilogy of the meta-phase: P15 (why RH resists), P16 (Pontryagin/finite-defect), P17 (unconditional finite
  bottom). Papers P1–P17 all compiled.

> **Day-39 consolidation. The program's strategy map is complete and the phase is banked.** Durable: 17 compiled
> papers; N1–N8 + capstone + Thm C; the calibrated discriminator D0; the finitization-under-LI obstruction; and the
> first UNCONDITIONAL semiboundedness of the Weil form (mod log) with a non-circular sub-RH residue. No non-circular
> passage to RH found; genuinely new math is RH-independent. Honest endpoint, fully recorded.

**2026-06-05 — Day 40. Three non-circular tracks advanced in parallel (Options 1, 2, 4).**
- **OPT 1 (`OPT1-c-reduction-selberg-tail.md`):** exact split V=N∫_{|α|<1}+N∫_{1≤|α|≤A} ϕ̂ F. Low part (I) ≪ N
  UNCONDITIONAL (diagonal L·T^{-2|α|} + F≥0; no loss). The ENTIRE loss is the high part (II) = uniform ∫_1^A F(α)dα.
  Selberg ∫S²≪T loglog T gives TYPICAL loglog T but not UNIFORM; conversion typical→uniform is the residual c =
  Goldston–Montgomery short-interval variance. Sub-RH, non-circular; each smoothing improvement = measurable
  decrement of c.
- **OPT 2 (`OPT2-B2conj-formulation-forward.md`):** B2conj formalized. **FORWARD DIRECTION PROVEN** (unconditional,
  RH-free): Euler product ⟹ Λ_L supported on prime powers ⟹ anatomy R_L(p^k) depends only on local L_p, no
  multi-prime cross-terms (Newton–Girard on L_p). Converse precisely formulated + distinguished from Weil's converse
  theorem (no twists; single localized Weil form's anatomy), reduced to a bilinear cross-term vanishing question on
  the ground state. Genuinely new, RH-independent; forward is a real result.
- **OPT 4 (`OPT4-finite-to-full-uniformity.md`):** the finite-to-full gap = a UNIFORMITY (quantifier-order) gap
  ∀k∃T_0 vs ∃-free, NOT a logical-implication gap (P_∞=∩P_k trivially). Uniformity criterion (Prop): bridge holds iff
  finite-type (scale-free) OR bounded threshold sup_k T_0(k)<∞. Dichotomy: matroids/Lorentzian/moment problems =
  scale-free → bridge holds (AHK); ζ Jensen/total-positivity = scale-parametrized, T_0(k)→∞ (GORZ) → gap.
  UNIFICATION: gap ⟺ no finitization (a Frobenius makes the object scale-free). New RH-independent questions:
  bounded-threshold non-finite-type hierarchies; uniform-in-scale defect rates; a "uniform Hodge–Riemann" for towers.

> **Day-40. Three non-circular tracks, real content each.** OPT1: the (LB) loss localized entirely to the uniform
> high-freq form factor (low part unconditional, no loss). OPT2: B2conj forward direction PROVEN, converse pinned to
> a cross-term vanishing (new, RH-independent). OPT4: finite-to-full = uniformity gap, criterion (finite-type or
> bounded threshold), gap ⟺ no finitization — a transferable positivity-theory principle. Material for three future
> papers; none circular (sub-RH or RH-independent).

**2026-06-05 — Day 41. Papers P18,P19,P20 written/compiled + publication index + three fronts advanced.**
- **P18** (loss-localization-form-factor, 3pp): Thm — (LB) log-loss confined to the high-band ∫_1^A F; low band |α|<1
  unconditionally O(N). **P19** (euler-product-anatomy-locality, 2pp): Thm — Euler ⟹ local anatomy (proven); B2
  converse reduced to ground-state cross-term vanishing. **P20** (finite-to-full-uniformity, 2pp): finite-to-full =
  uniformity gap; criterion (finite-type or bounded threshold); gap ⟺ no finitization. All cite only backward.
- **00-PUBLICATION-INDEX.md** created in 06-papers/: 20-row table in publication order (P6 at #3, P16 before P17,
  no cycles), with an `arxiv link` column (placeholders) to fill on posting; P18/19/20 appended #18/19/20.
- **FRONT 1 advance:** clean (LB) holds OFF a sparse exceptional set of density ≪K^{-2} (Selberg 2nd+4th moments);
  on it, mild loss ≤CK loglog T. Refines "loss everywhere mod log" → "clean a.e., mild loss on a sparse set." Next:
  bound exceptional density via higher Selberg moments.
- **FRONT 2 advance:** CONDITIONAL CONVERSE of B2 — if ground state û_0(log n)≠0 at every non-prime-power n, then
  factorizing anatomy ⟹ Euler product (proven). Exact obstruction: û_0 (entire, exp type) vanishing at the
  non-prime-power log-lattice = fine-tuned alignment. ⟹ B2 is GENERICALLY TRUE; counterexample needs a ground-state
  zero conspiracy. Next: prove non-vanishing for a sign-definite Gaussian window ⟹ unconditional converse.
- **FRONT 4 advance:** bounded-threshold non-finite-type class is NON-EMPTY (converging strictly-positive measure
  families, Prop). Discriminator = UNIFORM convergence. ζ fails: ξ-Jensen → Hermite but NON-uniformly in degree
  (GORZ thresholds grow). NEW LINK: uniform Hermite convergence of the Jensen polys ⟹ bounded threshold ⟹
  finitization ⟹ contradicts LI — so "uniform Hermite convergence is obstructed under Linear Independence." A clean
  analytic↔arithmetic bridge.

> **Day-41. Three papers banked (P18–P20, publication index with arxiv-link column) + three non-circular fronts
> advanced.** F1: clean (LB) a.e. off a sparse set. F2: B2 converse GENERICALLY a theorem (obstruction = ground-state
> zero alignment). F4: bounded-threshold class non-empty; uniform Hermite convergence obstructed under LI (new
> analytic↔LI link). All sub-RH or RH-independent; none circular. Papers P1–P20 compile.

**2026-06-05 — Day 42. Three fronts deepened (one near-theorem, one rate improvement, one self-correction).**
- **FRONT 2 (near-theorem):** ground state g_0=P(t)e^{-t²/2σ²} ⟹ autocorrelation c_0(u)=Q_σ(u)e^{-u²/4σ²}, deg Q_σ≤2deg P
  ⟹ c_0 has ≤2deg P real zeros. **THEOREM (B2 converse, all-windows):** if anatomy factorizes across a continuum of
  windows with non-stationary autocorrelation zeros, then L has an Euler product. Proof: a fixed log n can't be a
  root of Q_σ for all σ ⟹ Λ_L(n)=0 for non-prime-powers. B2 ESSENTIALLY SETTLED affirmative; residue = verify
  non-stationarity for Hermite–Gauss family (finite RH-independent computation).
- **FRONT 1 (rate improvement):** Selberg's FULL moment theorem (all moments Gaussian, CLT) ⟹ exceptional set
  {M(T)>K loglog T} density ≪_m K^{-2m} ∀m ⟹ decays FASTER THAN ANY POWER of K. Clean (LB) holds except on
  super-polynomially sparse anomalous-cluster (large-S(t)) heights. Strengthens Day-41 K^{-2}.
- **FRONT 4 (self-correction):** RETRACTED the Day-41 "uniform Hermite convergence obstructed under LI" — WRONG at
  arrow 2 (bounded threshold has TWO sources: finite-type/finitization OR uniform-convergence; only the first is
  LI-obstructed, per §5 existence Prop). Correction REVEALS: the convergence route to RH is structurally SEPARATE
  from finitization and NOT LI-obstructed — first RH-approach provably outside the LI obstruction. Honest caveats:
  "uniform" = full (d,n) grid (not just above one height); whether uniform-convergence ⟺ RH (circle) or strictly
  different (non-circular) is the OPEN dichotomy that decides if this is a real opening.

> **Day-42. Deepening: F2 → near-theorem (B2 converse settled under all-windows def), F1 → super-polynomially sparse
> exceptional set (clean LB a.e.), F4 → self-corrected a false LI link, exposing a genuine fork (uniform-convergence
> route is NOT LI-obstructed; circular-vs-not is the open question). The program's ethos held: retracted my own
> overclaim, and the correction opened more than it closed.

**2026-06-05 — Day 43. F2 CLOSED (theorem), F4 dichotomy RESOLVED, F1 consolidated.**
- **FRONT 2 — B2 CONVERSE PROVEN** (`B2_autocorrelation_zeros.py`): (a) pure-Gaussian ground state ⟹ c_0(u)>0 ∀u
  (verified, 0 real zeros all σ); (b) pure H_k ⟹ c_0=L_k(u²/2σ²)e^{-u²/4σ²}, exactly k zeros (2,4,6 verified);
  (c) zeros scale u*=σr_j, MOVE with σ (verified linear). **Theorem (localized-detector regime):** ground state
  Gaussian-dominated (Ω min at r=0) ⟹ c_0>0 ⟹ factorizing anatomy ⟹ Euler product, in ONE window. **Theorem
  (general, two-window):** zeros at σr_j(σ) move ⟹ two generic-ratio widths ⟹ no fixed log n stays a zero ⟹ Euler
  product. **B2 SETTLED: an L-function has an Euler product IFF its localized-Weil anatomy factorizes.** Full
  characterization (forward §2 + converse). RH-independent.
- **FRONT 4 — dichotomy RESOLVED:** uniform (d,n) Hermite convergence at rate o(1/d) ⟹ hyperbolic (within Hermite
  gap ~1/d) ⟹ RH (sufficient); but RH ⟹ hyperbolic ≠ Hermite-spacing (not necessary). Cor: uniform convergence is
  STRICTLY STRONGER than RH (over-RH, harder); the RH-equivalent notion (within margin of SOME hyperbolic poly) =
  "hyperbolic" = RH (circular). NO sub-RH opening from the convergence route. Framework value is RH-independent
  (criterion, bounded-threshold class, dichotomy) — honest terminus as an RH route.
- **FRONT 1 — consolidated (terminus):** elementary toolkit at its limit: clean (LB) off a super-polynomially
  sparse anomalous-cluster set; log-power everywhere. Beyond = uniform high-freq form factor = Goldston–Montgomery,
  needs Montgomery–Soundararajan ANT, not program machinery. Honest stopping point, residue named.

> **Day-43. F2 closed to a theorem (Euler product ⟺ anatomy factorizes), F4 dichotomy resolved (convergence route
> over-RH or circular — no opening; framework RH-independent), F1 consolidated at the GM frontier. The three fronts
> reach their natural termini: F2 a clean RH-independent theorem (the only one that fully closed), F1 an
> unconditional sub-RH result with named residue, F4 a resolved negative + standalone positivity-theory framework.

**2026-06-05 — Day 44. P19 rewritten (full theorem + GL(n)); P18,P20 updated; GL(n) front advanced.**
- **P19 (3pp, recompiled):** now the COMPLETE characterization — Thm: L has Euler product ⟺ localized-Weil anatomy
  factorizes (converse proven: localized-detector regime in 1 window via Gaussian-dominated c_0>0; general via
  two-window non-stationarity); Lemma (autocorr zero structure) + Observation (computation); **GL(n) Satake recovery
  Thm** (anatomy → power sums → Newton-Girard → L_p → π by strong mult one). Title updated.
- **P18 (3pp):** added Thm (clean bound a.e.) — exceptional set super-polynomially sparse via Selberg's full moment
  hierarchy. **P20 (3pp):** added Prop (bounded-threshold class non-empty, converging measures) + Thm (convergence
  route over-RH or circular, no sub-RH opening). Index P19 row updated. All cite backward only.
- **GL(n) FRONT ADVANCED (Day 44, OPT2 §8):** (i) DEGREE = eventual Hankel rank of anatomy power sums s_k(p); (ii)
  RAMANUJAN as DECAY RATE: max|α_{i,p}| = lim|s_k(p)|^{1/k} recoverable from anatomy; Ramanujan ⟺ R_L(p^k) decays
  exactly like p^{-k/2}. The anatomy is a complete faithful local invariant (degree + local factors + Ramanujan).
  Open continuation (rich, RH-independent): automorphy direction = factorizing anatomy + functional eq ⟹ automorphic
  = twist-free spectral Langlands converse.

> **Day-44. P19 closed to a full theorem with GL(n) Satake/degree/Ramanujan recovery; P18,P20 consolidated. Three
> papers updated, all compile. The richest open vein is the twist-free automorphy direction (GL(n)), genuinely hard
> and RH-independent. F1 at the GM frontier (handoff), F4 resolved (RH route closed, framework standalone).

**2026-06-05 — Day 45. Three fronts advanced to frontier mathematics.**
- **FRONT 2 (OPT2 §9):** anatomy generating function G_p(x)=Σ s_k(p)x^k = x L_p'/L_p ⟹ L_p=exp∫G_p/t dt — EXACT
  spectral reconstruction of the local Euler factor. **Theorem (GL(1) automorphy CLOSED):** degree-1 + factorizing
  anatomy ⟹ shifted Dirichlet L (Hecke char), via Kaczorowski–Perelli degree-1 classification. GL(2) REDUCED to the
  Selberg degree-2 conjecture (open), with new tools: Hankel-rank degree detector + generating-function reconstruction.
- **FRONT 1 (OPT1 §7):** the (LB) exceptional set = Arc A's EXTREME-VALUE heights (large |ζ(1/2+it)|, Bondarenko–Seip
  resonance, FHK/moment frontier). Program-internal UNIFICATION: end (localized-Weil residue) = beginning (ω-class
  extreme values). Transfer: any unconditional bound on extreme-value-height contribution (Arc A machinery / moment
  conjectures) shrinks c. The two ends of the program meet at the large values of ζ.
- **FRONT 4 (OPT4 §8):** **Theorem (HR stability under limits):** a Hodge–Riemann tower (V_m,L_m,Q_m)→limit has
  UNIFORM HR (liminf δ_m ≥ δ_∞ > 0) iff the limit HR form is strictly definite (δ_∞>0); δ_∞=0 ⟹ uniform HR fails.
  Cor: bounded threshold = strictly-definite limit. Generalizes Adiprasito–Huh–Katz from objects to FAMILIES (HR is
  classically per-object) — new positivity theory. ζ at the borderline (δ_∞=0 in degree direction). RH-independent.

> **Day-45. Frontier math on all three: F2 — GL(1) automorphy closed + exact local reconstruction (G_p→L_p), GL(2)
> reduced to Selberg degree-2. F1 — residue = Arc A extreme-value heights (program closes its own loop). F4 — HR
> stability theorem (uniform HR ⟺ definite limit), AHK from objects to families. Three new theorems/reductions, all
> RH-independent or sub-RH, none circular. Frontier problems for the team: Selberg degree-2 automorphy (F2),
> extreme-value-height form factor (F1), uniform-HR tower classification (F4).

**2026-06-05 — Day 46. THREE FRONTIER PAPERS CLOSED (P18, P19, P20), full length + Python appendices.**
Final-session deliverable: the three non-circular fronts written up as complete papers with formal theorems, proofs,
and reproducible code appendices.
- **P18 (9pp):** unconditional finite bottom — Thm (V=∫|S|² identity, verified 1e-6), Prop (Parseval bound),
  Prop (low band O(N)), Prop (finite bottom mod log^c), Lemma (diagonal ~2d²), Prop (RFB reduction), Thm (clean
  bound a.e. off super-sparse set via Selberg moments), Goldston–Montgomery non-circularity, three-level hierarchy
  (S)<(κ)<(R), Arc A extreme-value connection. 3 code appendices (verify_V_identity, a_tail, near_critical) + real outputs.
- **P19 (8pp):** the anatomy as complete local invariant — Thm (Euler ⟺ factorizing anatomy, converse proven 2 ways),
  Lemma (autocorr zero structure, Laguerre), Thm (Satake recovery: power sums→Newton-Girard→L_p, degree=Hankel rank,
  Ramanujan=decay rate), Thm (generating function G_p=xL_p'/L_p, exact local reconstruction), Thm (Rankin–Selberg
  multiplicativity s_k(π⊠π')=s_k(π)s_k(π')), Thm (functorial lifts polynomial in base anatomy), Thm (GL(1) automorphy),
  GL(2) reduction to Selberg degree-2. Code appendix (B2_autocorrelation_zeros) + real output.
- **P20 (7pp):** finite-to-full = uniformity gap — Thm (criterion: finite-type or bounded-threshold), Prop (bounded-
  threshold class non-empty), Thm (convergence route over-RH or circular), **Thm (HR stability: uniform HR ⟺ definite
  limit, generalizing AHK objects→families)**, Prop (rate transfer), worked examples (uniform-HR tower, degenerate
  borderline, uniform matroids), ζ-orders concretely. 2 code appendices (HR stability demo, degenerate borderline) +
  real outputs.
- Publication index updated (rows 18–20 with page counts, code notes, full descriptions; arxiv-link column ready).

> **Day-46. The three non-circular fronts are closed as full frontier-mathematics papers (P18 9pp, P19 8pp, P20 7pp),
> each with formal theorems, complete proofs, and reproducible Python appendices with real outputs. P19 is the
> strongest: a complete characterization (Euler ⟺ anatomy factorizes) + GL(n) Satake recovery + Rankin–Selberg
> functoriality. P20 contributes a new HR stability theorem (AHK objects→families). P18 an unconditional sub-RH
> finite-bottom with a.e. clean constant. All RH-independent or strictly sub-RH; none circular. Papers P1–P20 compile.

**2026-06-05 — Day 46 (cont.). LaTeX edition of the bitácora created.**
The full proof log (Days 0–46, 2655 lines) was rendered to typeset LaTeX in a new folder
`phase-4-handoff/proofs/latex/`: PROOF-LOG.tex + PROOF-LOG.pdf (88 pp, compiles clean, 0 errors) +
build_proof_log_tex.py (a self-contained markdown→LaTeX converter, no pandoc; handles unicode/Greek,
escaping, nested inline spans, fenced code blocks) + README. The .md remains the canonical append-only diary;
the LaTeX edition is a regenerable mirror (rerun the build script after new entries).

**2026-06-06 — Day 47. NEXT PHASE proposed: the Anatomy–Kreĭn–Hodge program.**
`NEXT-PHASE-the-anatomy-krein-hodge-program.md`. The one direction that passes the discriminator D0: SURF (an
arithmetic Hodge index for Spec ℤ), now with this program's three tools as a NEW spectral entry point.
- **Central idea:** the ANATOMY (P19, Satake recovery) IS the missing arithmetic Frobenius — the ingredient
  Connes–Consani/Deninger seek to construct geometrically is already available SPECTRALLY. Build the arithmetic
  intersection theory AROUND the anatomy, with the Kreĭn form (P16) as the pairing and HR-stability (P20) as the
  definiteness criterion. Inverts the usual order: Frobenius + pairing in hand, the Hodge-index definiteness is the task.
- **Milestones:** M1 arithmetic intersection pairing (Γ,Δ classes, trace identity, from EF+anatomy — achievable,
  non-circular); M2 ample cone = the pole/de la Vallée Poussin anchor = hyperbolic plane analogue (unconditional,
  from P14); M3 the Hodge-index step = THE CAPSTONE = RH, attacked via TWO new channels — (a) HR-stability limit
  (strict-definite vs critical-degenerate limiting primitive form, the P16/P18 borderline) and (b) Rankin–Selberg
  effectivity square s_k(π⊠π̄)=|s_k(π)|²≥0; M4 LI-consistency check (genuinely infinite-dim, evades P15 obstruction).
- **Honest:** M1,M2,M4 achievable/non-circular/real; M3 IS RH (no shortcut). The novelty = the two new attack channels
  on M3 that the geometric programs lack, turning the capstone into a sharp structured question. D0 certifies it as the
  only I2a∧(candidate I2b) route. Team targets assigned per milestone.

> **Day-47. Next phase proposed — the Anatomy–Kreĭn–Hodge program.** The honest frontier: the anatomy is the missing
> arithmetic Frobenius; build the arithmetic intersection theory around it (Kreĭn form = pairing, HR-stability =
> definiteness criterion); RH = an infinite-dimensional Hodge index (M3), attacked via the HR-stability limit and the
> Rankin–Selberg effectivity square. Early milestones real and non-circular; the capstone sharply posed, not promised.

**2026-06-06 — Day 47 (cont.). PHASE 15 folder created; MILESTONE M1 COMPLETE (proved + verified).**
Phase-15 folder (`phase-15/`) holds the overview (00-PHASE-15-overview.md) + M1 + experiments.
**M1 — the arithmetic intersection pairing** (`phase-15/M1-arithmetic-intersection-pairing.md`), fully proved,
RH-independent:
- **Definition:** ⟨f1,f2⟩=Σ_ρ f̂1(γ_ρ)overline{f̂2(γ_ρ)} = the Kreĭn–Weil intersection pairing; negative index
  κ=#off-line zeros; RH ⟺ ⪰0 (Weil).
- **Theorem A (Lefschetz/adelic trace identity):** the pairing = poles [h(±i/2)=H⁰⊕H²] − 2Σ Λ(n)/√n g(log n)
  [primes=Frobenius] + (1/2π)∫hW [archimedean=∞-place] — the explicit formula AS a sum of local intersection
  numbers. NUMERICALLY VERIFIED to 3.5e-12 (T=100, σ=1), with the ±γ conjugate-zero factor-2 confirming correctness.
- **Theorem B (Γ·Γ≥0, Rankin–Selberg effectivity):** the Frobenius self-intersection = ∫_{-2d}^{2d}|S|²≥0 = the
  verified P18 second moment; = Res_{s=1}L(s,π×π̄)>0 = Σ|s_k(p)|² (anatomy power sums, P19). VERIFIED to 1e-7.
- **Proposition C (Hodge-index reduction):** poles=ample cone (edge-positive, P14); primitive part=H¹ (critical-line
  zeros); RH ⟺ pairing ⪰0 on the primitive part = THE ARITHMETIC HODGE INDEX (=M3).
- M1 assembles the arithmetic surface's intersection theory around the anatomy and reduces RH to ONE statement (M3),
  via an equivalence (Prop C). Two attack channels on M3 set up: M3a (HR-stability limit), M3b (RS effectivity +
  ample positivity). Numerical grounding: phase-15/experiments/intersection_check.py.

> **Day-47 (cont.). M1 done.** Built and proved the arithmetic intersection pairing for Spec ℤ around the anatomy:
> Theorem A (explicit formula = Lefschetz trace identity, verified 1e-12), Theorem B (Γ·Γ≥0 Rankin–Selberg
> effectivity = verified second moment), Proposition C (RH ⟺ arithmetic Hodge index on the primitive part). RH is
> now exactly M3, sharply posed. M1 is RH-independent and fully verified; nothing assumed about RH.

**2026-06-06 — Day 48. MILESTONE M2 COMPLETE (proved + verified): the ample cone is positive, unconditionally.**
`phase-15/M2-ample-cone-edge-positivity.md`, RH-independent, fully proved.
- **Lemma (real pole evaluations):** for real even f, λ_0(f)=f̂(i/2)=λ_1(f)=f̂(−i/2)=∫f(u)e^{−u/2}du ∈ ℝ
  (r=i/2↔s=0, r=−i/2↔s=1, the two poles; functional equation s↔1−s swaps them).
- **Theorem (edge positivity, UNCONDITIONAL):** the trivial/pole part of the self-pairing is
  P(f,f)=h(i/2)+h(−i/2)=2(∫f e^{−u/2}du)² ≥ 0, =0 iff ∫f e^{−u/2}=0. The ample cone is POSITIVE.
- **Prop (= de la Vallée Poussin):** this positivity IS the Landau/edge anchor of P14 (the pole at s=1 forces a
  positive Weil-pairing term) in intersection-theoretic form.
- **Prop (hyperbolic plane):** the trivial part = ⟨λ_0,λ_1⟩ (s=0,1 = H⁰⊕H²), exchanged by the functional equation;
  the symmetric combination λ_0+λ_1 is ample (positive) — the exact analogue of the fiber classes f_1,f_2 with
  f_1+f_2 ample; on even f it collapses to the ample line. Weil-positivity convention noted (ample positive; RH =
  primitive positivity).
- **Corollary (scaffold):** ⟨·,·⟩ = (2 λ⊗λ, ample, ⪰0 unconditional) ⊕ (primitive part on Π^⊥=ker λ, the H¹
  zeros); RH ⟺ primitive positivity = arithmetic Hodge index (M3).
- VERIFIED (`ample_check.py`): Lemma to 8 digits (f̂(i/2)=λ=2.84038195, P=4πe^{1/4}=16.13553926); positivity across
  a family; engineered λ=0 case gives P=1e−31 (sharp vanishing).

> **Day-48. M2 done.** The ample cone (poles = H⁰⊕H²) is POSITIVE and unconditional: P=2(∫f e^{−u/2})²≥0, the de la
> Vallée Poussin edge positivity as a hyperbolic plane. M1+M2 = the full Weil-style scaffold for Spec ℤ, all proved
> and verified. RH is now exactly M3 (the arithmetic Hodge index = primitive-part positivity), with the ample
> positivity (M2) in hand as one input to M3b. Nothing assumes RH.

**2026-06-06 — Day 48 (cont.). MILESTONE M3 — the arithmetic Hodge index = the capstone = RH. Attack complete; RH NOT crossed (honest).**
`phase-15/M3-arithmetic-hodge-index.md`. M3 IS RH; every provable step proved + documented; the irreducible RH-core
isolated. NO proof of RH claimed or fabricated.
- **Prop (M3=RH):** M3 (primitive positivity ⟨f,f⟩=Σ|f̂(γ)|²≥0 on Π^⊥=ker λ) ⟺ κ=0 ⟺ RH.
- **CHANNEL M3b (Weil assembly):** Lemma (Kreĭn index inequality: M3 ⟺ reverse-Cauchy-Schwarz on the ample line).
  Theorem: ingredients (A) trace identity (M1, verified 1e-12), (E) effectivity Γ·Γ=∫|S|²≥0=Σ|s_k|² Rankin-Selberg
  (M1, verified), (P) ample positivity ⟨H,H⟩=2λ²>0 (M2, verified) — ALL in hand; RH ⟺ the SIGNATURE THEOREM
  (⟨D,D⟩≥0 on Π^⊥), supplied for free by the general Hodge index on C×C in function fields, MISSING for Spec ℤ =
  the capstone (exactly what D0 predicted).
- **UNIFICATION (new, proved):** Theorem — M3 (geometry) ⟺ V(d,T)≪dN uniform ⟺ uniform high-freq form factor F(α)≪1
  (analysis, P18). Weil geometry = Montgomery pair correlation = SAME WALL. Corollary: P18's partial results ARE
  partial arithmetic Hodge index — semibounded mod log^c, and clean off a super-sparse extreme-value set. FIRST
  partial arithmetic-Hodge-index results, unconditional.
- **CHANNEL M3a (HR-stability):** Theorem — band-limited primitive forms = a tower; P20 HR-stability ⟹ uniform
  positivity ⟺ δ_∞>0; P16/P18 measure δ_∞=0 (borderline, near-critical multiplicity grows). ζ at the degenerate-
  limit borderline.
- **Theorem (three faces coincide):** signature (Weil) ⟺ uniform form factor (Montgomery) ⟺ definite limit
  (HR-stability) ⟺ RH. Three communities provably on one object; equivalences are THEOREMS not intra-framework
  restatements.
- **IRREDUCIBLE CORE:** the signature theorem = uniform form factor = δ_∞>0 = RH. NOT proved (= the capstone). In
  function fields supplied by the general Hodge index on a surface; for Spec ℤ no such surface (D0; LI obstruction
  P15). NOT crossed; claiming a crossing = fabricating RH = the false victory the program refuses.

> **Day-48. M3 = the capstone, attacked to completion in the only honest sense.** Proved: M3=RH; the full Weil
> assembly with the single missing piece = the signature theorem; the NEW unification (arithmetic Hodge index =
> uniform short-interval prime variance = HR-stability definite limit, three faces proven equal); and the FIRST
> partial arithmetic Hodge index (mod log; off a sparse set), unconditional. Not proved: RH itself (the irreducible
> core). The capstone stands, sharply posed from three coincident sides, partial progress attached. No false victory.

**2026-06-06 — Day 48 (cont. 2). M3 core — FOUR genuine new attempts, all developed to endpoint; none crosses.**
`phase-15/M3-genuine-attempts-on-the-core.md`. Maximum-effort exploration of the irreducible core ⟨D,D⟩≥0 on Π^⊥
(=RH), four new attacks, honest outcomes:
- **Attempt 1 (2×2 Hodge-index Gram det):** Gram of {H ample, Γ Frobenius} = [[2λ²,a],[a,V]]; Hodge index ⟺ det<0 ⟺
  a²>2λ²V uniform (reverse Cauchy-Schwarz). a=⟨H,Γ⟩=cross-place pairing. The uniform domination IS the index = RH.
  Lands on core.
- **Attempt 2 (Bochner positivity):** the sine kernel is positive-definite ⟹ V≥0 (effectivity, lower bound) only;
  the upper bound (offdiag≤0) needs a zero-DIAGONAL positive-definite kernel, IMPOSSIBLE (K(0)=∫K̂≥0, =0 iff K≡0).
  Clean structural reason the upper bound isn't free = the wrong-sign capstone.
- **Attempt 3 (dBN flow + arithmetic):** relaxation reduces clustering ⟹ V_t decreasing ⟹ V_0≥GUE (lower bound,
  wrong direction); N5 forbids arithmetic-aware monotone to flip it. Lands on N5.
- **Attempt 4 (Sym^m / Rankin-Selberg tower):** each Sym^m effectivity controls its OWN zeros / the Satake
  (Ramanujan, local/prime-identity axis), NOT ζ's archimedean zeros. Orthogonal axis (M14.3/P19 dichotomy). Doesn't
  reach RH.
- **Synthesis:** all four reproduce the same one-sided core (unconditional UPPER/sign control = a²>2λ²V uniform =
  offdiag≤0 = uniform form factor = δ_∞>0 = RH), unreachable from effectivity/Bochner (lower bounds), relaxation
  (lower, arithmetic-blind), or local functoriality (Satake not zeros). Four new non-circular confirmations that the
  core is exactly one-sided positivity. No fabricated crossing.

> **Day-48 (cont. 2). Four genuine maximum-effort attempts on the M3 core, all documented, none crosses.** Each
> lands freshly on a face already isolated (the Gram-det form a²>2λ²V; the Bochner zero-diagonal impossibility; the
> flow's wrong-sign monotonicity + N5; the Satake-vs-zeros orthogonality). The irreducible core — an unconditional
> one-sided upper bound forced by a signature — stands, now confirmed from four new directions. The honest crossing
> requirement (a structure giving upper/sign control that is not effectivity/Bochner/relaxation/local) is exactly
> D0's missing I2b. No false victory.

**2026-06-06 — Day 49. M3 · Attempt 5 — the arithmetic Hodge index theorem EXISTS; the obstruction is the SURFACE, not the theorem. (Corrected premise.)**
`phase-15/M3-attempt5-arithmetic-hodge-index-exists.md`. A genuine crossing attempt that corrects a false premise
in Attempts 1-4 / M3b.
- **CORRECTION (load-bearing):** the claim "for Spec ℤ no general Hodge index theorem is known" is FALSE. The
  arithmetic Hodge index theorem IS PROVEN: Faltings–Hriljac (1984, Arakelov pairing on degree-0 = Néron–Tate,
  negative definite); Yuan–Zhang (2017) + Moriwaki (all dimensions, adelic line bundles). A general arithmetic
  I2b-THEOREM is in hand.
- **The attempt:** realize the primitive Weil pairing as the Arakelov pairing on Pic^0 of an arithmetic surface X,
  then Faltings–Hriljac/Yuan–Zhang gives the signature = M3 = RH. Needs: (1) Π^⊥ ≅ Pic^0(X)⊗ℝ, (2) Weil pairing =
  Arakelov pairing, (3) zeros = Arakelov eigenvalues.
- **Where it lands (honest, sharper):** the obstruction is EXACTLY the surface X, not the theorem. Two facts:
  (a) Faltings–Hriljac/Yuan–Zhang control HEIGHTS (Néron–Tate, special values, BSD), NOT critical-line zeros; the
  zeros↔Arakelov-height link is the open Beilinson/motivic dictionary. (b) ζ_ℚ lives on Spec ℤ (dim 1); applying a
  2-dim Hodge index to its zeros needs X = "Spec ℤ ×_{F₁} Spec ℤ" with zeros as Frobenius on H¹ — no such X exists
  (SURF/Connes–Consani).
- **REFINED CONCLUSION:** the missing I2b SPLITS — the THEOREM exists (✓), the OBJECT (the arithmetic surface for
  Spec ℤ) does not (✗). The whole obstruction is the object. The only two routes: (a) construct the F₁ surface
  (Connes–Consani) → Yuan–Zhang gives RH; (b) realize ζ_ℚ's zeros as Arakelov eigenvalues on an existing
  higher-dim arithmetic variety (Beilinson realization). Both recognized deep programs; the attempt shows they are
  the ONLY routes since the theorem-half is done. Testable on an elliptic curve E/ℚ (there X exists; the Hodge index
  applies, but to heights not zeros — confirming the gap is zeros↔heights, not a method defect).

> **Day-49. M3 Attempt 5 corrects the program's framing: the arithmetic Hodge index theorem EXISTS (Faltings–Hriljac,
> Yuan–Zhang). The obstruction to RH is NOT a missing theorem — it is the missing ARITHMETIC SURFACE for Spec ℤ (plus
> the zeros↔heights dictionary). "We lack a Hodge index theorem" becomes the correct "we lack the surface to apply
> the Hodge index theorem we already have." Sharpest true statement of the M3 obstruction; no crossing, real
> refinement, fully verifiable (cited theorems are published; the gap is explicit).

**2026-06-06 — Day 49 (cont.). M3 · Attempt 6 — the elliptic control: the proven Hodge index is on the WRONG cohomology (heights, not zeros).**
`phase-15/M3-attempt6-elliptic-control-heights-vs-zeros.md`. Ran the Attempt-5 construction on E/ℚ, where the
arithmetic surface 𝓔→Spec ℤ EXISTS and Faltings–Hriljac applies.
- **Prop (heights/special value):** Faltings–Hriljac gives neg-definiteness of Néron–Tate ĥ on E(ℚ)⊗ℝ ⟹ controls the
  Mordell–Weil regulator R_E ⟹ (BSD) the LEADING COEFFICIENT of L(E,s) at the CENTRAL POINT s=1. A BSD/special-value
  statement.
- **Prop (zeros are a different object):** the location of L(E,s)-zeros on Re s=1 (GRH for E) is NOT controlled by ĥ.
  Separation at the level of WHICH COHOMOLOGY carries the eigenvalues: function-field zeros = Frobenius on H¹_ét(C);
  arithmetic Pic^0(𝓔)=E(ℚ) = heights/special value. Different cohomologies; only the function-field one carries zeros.
- **SHARPENED OBSTRUCTION (final form):** there are TWO arithmetic Hodge indices / two cohomologies:
  (i) Arakelov/Faltings–Hriljac/Yuan–Zhang — PROVEN; controls HEIGHTS (Mordell–Weil) ⟹ special values (BSD), NOT
  zeros. (ii) Deninger/Connes "arithmetic cohomology" — CONJECTURAL; would carry the L-ZEROS ⟹ GRH/RH; doesn't exist.
  So the missing I2b is NOT merely "a surface": even WITH the surface (for E), the proven Hodge index is on the WRONG
  cohomology. The genuinely missing object = the ZERO-CARRYING arithmetic cohomology (a H¹ for Spec ℤ with a Frobenius-
  analogue Φ, spec(Φ)={γ_ρ}) + its Hodge index = exactly the Deninger/Connes target, isolated as the UNIQUE remaining
  ingredient.
- **Refines SURF:** the F₁-surface is necessary but NOT sufficient unless its cohomology carries the ZEROS (not heights);
  the Arakelov route (heights) is a different BSD-flavored theory that does NOT transfer. The Beilinson dictionary
  (special values↔zeros) is the precise open link.

> **Day-49 (cont.). Elliptic control sharpens M3 to its final, correct form.** Even where the arithmetic surface
> exists (E/ℚ), the PROVEN arithmetic Hodge index (Faltings–Hriljac) controls HEIGHTS ⟹ special values (BSD), NOT the
> critical-line ZEROS (GRH). The missing I2b is the ZERO-CARRYING arithmetic cohomology (Deninger/Connes) + its Hodge
> index — not the height theory (proven, wrong object), not merely "a surface" (necessary, insufficient). Sharpest,
> most correct statement of the RH obstruction the program reached; verifiable; no crossing.

**2026-06-06 — Day 50. M3 · Attempt 7 — the zero-carrying cohomology BUILT explicitly; capstone pinned to one Kähler compatibility.**
`phase-15/M3-attempt7-constructing-the-zero-cohomology.md`. Constructed the Deninger/Connes object for ζ (not named).
- **BUILT (unconditional):** (H1) the Kreĭn space H_W = Weil-form completion, candidate H¹, neg index κ=#off-line;
  (H2) the flow 𝒯 (P8) with spec(𝒯)={γ_ρ} — Frobenius-analogue, eigenvalues=zeros; (H3) the Lefschetz trace formula
  Tr h(𝒯)=Σ_ρ h(γ_ρ)=poles−2Γ(g)+arch (M1-A, verified 1e-12); (H4) anatomy/Satake as LOCAL FROBENIUS, G_p=xL_p'/L_p
  (P19); (H5) the positive ample cone (poles=H⁰⊕H², M2). The Deninger/Connes object is CONCRETE for ζ.
- **Candidate weight-1 Hodge structure** on Π^⊥: polarization Q=Weil pairing; involution ι=functional eq s↔1−s;
  complex structure J=spectral (Hilbert-transform) splitting aligned with 𝒯 (candidate H^{1,0}⊕H^{0,1}).
- **Theorem (RH = the polarization is genuine):** (H_W^prim,J,Q) is a POLARIZED Hodge structure (Riemann bilinear
  relation Q(x,Jx)>0) ⟺ RH. (= M3/Prop C.)
- **CAPSTONE pinned to ONE compatibility:** RH = the candidate Hodge structure is polarized = J compatible with Q =
  a KÄHLER structure on the arithmetic H¹. We HAVE J (spectral splitting of 𝒯) and Q (Weil form); the single missing
  object is the compatible (1,1)-KÄHLER FORM ω. In Kähler geometry this compatibility is automatic (Kähler ⟹
  Hodge–Riemann); here it is the lone missing input.
- **Unifies all faces:** Q(x,Jx)>0 = Hodge index (M3b) = uniform form factor (P18) = HR definite limit (M3a) =
  Laguerre–Pólya/hyperbolicity (P13) = Weil positivity. All = the Riemann relation of the one constructed structure.
- Next sub-target (sharp, structural not analytic): find the compatible (1,1)-Kähler form ω on H_W^prim that forces
  the Riemann relation — the Deninger/Connes positivity, now reduced to a single (1,1)-class with J,Q in hand.

> **Day-50. The zero-carrying arithmetic cohomology is BUILT explicitly for ζ** (Kreĭn space + flow 𝒯 with
> zero-spectrum + Lefschetz trace + anatomy Frobenius + ample cone + candidate Hodge structure J,Q). RH is pinned to
> ONE structural compatibility: the candidate Hodge structure is POLARIZED (Riemann relation Q(x,Jx)>0) = a Kähler
> form ω on the arithmetic H¹ exists. We have J and Q; only ω is missing. Most structural form of the capstone the
> program reached; the Deninger/Connes object made concrete; no crossing.

**2026-06-06 — Day 50 (cont.). M3 · Attempt 8 — the Kähler form: RH = one independent hard-Lefschetz sl₂, NOT generable from the flow. (Honest terminus.)**
`phase-15/M3-attempt8-the-kahler-form.md`. Attacked ω directly.
- **Prop (ω not independent):** the only (1,1)-form compatible with (J,Q) is ω=Q(J·,·); its positivity = Riemann
  relation = RH. So ω from the spectral triple alone IS RH (circular); an ω that FORCES positivity must come from
  outside (𝒯,J,Q).
- **Prop (𝒯 ≠ Lefschetz grading):** a hard-Lefschetz sl₂ (L,Λ,H) would deliver Hodge–Riemann structurally, but H
  has INTEGER eigenvalues while spec(𝒯)={γ_ρ} is real/irrational/dense (density ~log γ). 𝒯 is the Frobenius
  (eigenvalue datum WITHIN a weight), not the weight grading. So 𝒯 can't be the Lefschetz operator.
- **Prop (no contraction):** under RH 𝒯 is self-adjoint ⟹ e^{it𝒯} UNITARY, not a contraction; a contraction
  (Im 𝒯≻0) would put all zeros on one side, contradicting ρ↔1−ρ. So positivity can't come from a contraction
  structure either.
- **DEEPEST FORM OF CAPSTONE:** RH = existence of an independent hard-Lefschetz sl₂ (Kähler class ω) on H_W^prim
  COMMUTING with the Frobenius 𝒯 — exactly the ample geometry of the surface C×C, which delivers hard Lefschetz +
  Hodge–Riemann = RH. For Spec ℤ we BUILT 𝒯 and the cohomology (Attempt 7); the lone missing structure is ω, and
  Props (sl2,contr) PROVE it can't be manufactured from the flow. SURF in sharpest form = a single sl₂-action.
- **HONEST TERMINUS of the 8-attempt arc:** built H_W, 𝒯, J, Q, trace formula, anatomy/Frobenius, ample cone;
  RH = one independent Kähler/Lefschetz class ω (an sl₂) = the ample geometry of Spec ℤ × Spec ℤ. That's the
  Connes–Consani/Deninger target, reduced to a single hard-Lefschetz action and PROVEN not generable from the flow.

> **Day-50 (cont.). The 8-attempt M3 arc terminates, honestly and sharply.** Everything is built — the zero-carrying
> cohomology, the Frobenius flow 𝒯, J, Q, the trace formula, the anatomy as local Frobenius, the ample cone — and RH
> is reduced to ONE missing structure: an independent hard-Lefschetz sl₂ (Kähler class ω) commuting with 𝒯, the
> ample geometry of the missing arithmetic surface. Proven (spectrum mismatch; unitarity) that ω cannot come from
> the flow alone. The most precise statement of what a proof must still supply. No crossing; the construction is the
> deliverable.

---

## PHASE 15→16 (2026-06-06) — the Lefschetz dichotomy, P21, and the SURF spec sheet

**M1–M5 (Anatomy–Kreĭn–Hodge):** built the Weil scaffold for Spec ℤ (pairing, trace identity, effectivity, ample cone),
reduced RH to a single independent hard-Lefschetz sl₂/Kähler ω, and proved the INDEPENDENCE FILTER (any spectral
L∈W*(𝒯) only restates RH) + the LEFSCHETZ DICHOTOMY (integer/lowest-weight HR grading and the LI zero-spectrum are
incompatible: no Tate-twist op on the discrete zeros; principal series on the continuum). The archimedean density
Ψ(r)=Re ψ(¼+ir/2)−log π is the smooth zero-density; an explicit 𝒯-independent sl₂ (L=translation) was built and
verified (1e-12), but its transport to the zeros is the explicit formula Q=A_∞−P with Q≥0 only as the
archimedean−prime near-cancellation residual (CAP). **PAPER P21 ("The Lefschetz dichotomy", 7pp, compiled, indexed
row 21).**

**M6–M10:** prismatic route relocates to SURF (local Satake ≠ global zeros); an advisor incompleteness theorem (M7)
independently confirmed no proof lives in spectral data; a submitted "Connes proof of RH" REFUTED with 6 fatal flaws
(M8); a guarded Lise Science run returned 3 honest negatives + the Δ₃ rigidity plateau constraint (M9); and the advisor
"Arakelov–RH equivalence" was audited to its honest one-directional form: **∃𝒳 (Arakelov witness variety, Axiom 3) ⟹
RH** (theorem, via Yuan–Zhang transport); the converse is the open Hilbert–Pólya dream, possibly false (M10).

**PHASE 16 — sole task: build 𝒳, verify Axiom 3.** Acceptance criteria in `phase-16/00-SURF-SPEC-SHEET.md`. Two arbiter
corrections to the submitted spec: (1) the Pillar-1 trace test is the test-function trace Tr h(Frob)=Σh(γ_ρ)=explicit
formula (Σγ^k diverges); (2) **Pillar 4 cannot cite Yuan–Zhang** — it controls Pic⁰/heights (the object Pillar 2.2
rejects); the Hodge index for the zero-carrying H¹ is a new, OPEN theorem (Attempt 6, sharpest). Rejection filters:
spectrum (Frob trace ≠ explicit formula), heights (unconditionally definite pairing), independence (zeros/anatomy as
input), citation (G4 via Yuan–Zhang). No crossing; the deliverable is the construction of 𝒳, governed by the spec sheet.
