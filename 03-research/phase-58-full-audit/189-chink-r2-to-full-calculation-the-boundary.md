# Document 189 — Chink R2 to full calculation: the boundary flux $\mathcal F_{1/2}$ is exactly the LP-134 currency, and it reabsorbs into barrier #3

**Program:** Riemann Hypothesis — Phase 58 (full audit)
**Mandate:** execute the full calculation of the boundary flux $\mathcal F_{1/2}(T)=-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt$, $u=\log|\zeta|$ — the only anisotropic channel of D183's Green geometry, dispatched there without calculation (E-188.4) and flagged by audit D188 as chink R2 — and decide: a new route to a bound on $E(T)$, or reabsorption into known barriers?
**Prerequisites (with errata E-188.x applied):** [THM 183.1] with corrected sign $c(\rho)=-2\pi h(\rho)$ (E-188.2); [183.4.b replaced] $\int_0^T(\partial_\sigma u)^2\,dt\asymp T\log^2T$ FINITE (E-188.6); [183.1.b downgraded] order of $\mathcal D_R$ undetermined between $T\log T\log\log T$ and $T\log^2T$ (E-188.3); [183.3.b refuted] $N_{\rm off}=o(N)$ is NOT unconditional (E-188.5); [PROP 180.4] (barrier #3, with E-188.1); [PROP 176.9] (barrier #1); [Thm 170.5] $E(T)\ll T/\log T$.
**Contract:** [THEOREM]/[PROP]/[LEMMA] only with complete proof; no numerics; backward-only; total candor.

**Coordinates.** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, one representative per quadruple; $E(T)=\sum_{\gamma\le T}b^2$; $J(T):=\sum_{\gamma\le T}b$ (first moment, Littlewood); **A** $\iff E(T)=O(1)$.

---

## 0. Executive summary and verdict

1. **R2 is SEALED, with structural spoils.** The full calculation was carried out. Central, exact result:
$$\boxed{\;\mathcal F_{1/2}(T)\;=\;\pi\sum_{\gamma\le T}b\,\log\frac{\gamma}{2\pi}\;+\;O(\log^2T)\;}$$
**The boundary flux IS, identically, the LP-134/178.C currency ($\sum b\log\gamma$) with constant $\pi$.** [THEOREM 189.2]. It is the first analytic embodiment (a Green flux) of that currency in the program.
2. **The flux's kernel is EXACTLY deterministic.** $\partial_\sigma u(\tfrac12+it)=\mathrm{Re}\,\tfrac{\zeta'}\zeta(\tfrac12+it)=\tfrac12\mathrm{Re}\,\tfrac{\chi'}\chi(\tfrac12+it)=-\tfrac12\log\tfrac t{2\pi}+O(t^{-2})$, **with no zero term whatsoever**, via the functional equation + Schwarz reflection — total confirmation of E-188.6, now as an identity rather than a term-by-term cancellation. [LEMMA 189.1]. All the flux's zero information lives in the factor $u$; the flux = a Littlewood integral with weight $\tfrac12\log\tfrac t{2\pi}$.
3. **Resulting unconditional bound:** $\sum_{\gamma\le T}b\log\gamma\le(\tfrac1{4\pi}+o(1))\,T\log T\log\log T$ [PROP 189.3] — but it is EXACTLY what partial summation over Littlewood 1924 gives ($J(T)\ll T\log\log T$). **The weight $\log t$ buys nothing**: it is deterministic and monotone, factorizes by dyadic blocks, and each block re-enters via Jensen + second moment, i.e. via Littlewood. There is no new bound.
4. **Exact reabsorption mechanism (barrier #2-bis, [PROP 189.4]):** the boundary anisotropy is **first order** in $b$; its full content is a weighted $J$; any bound on weighted $J$ passes through $\int_0^Tu(\tfrac12+it)\,dt$ **with sign**, and by Littlewood's bidirectionality ([180.4.b]: identity, no third term) bounding that signed integral IS counting zeros. The flux reabsorbs into barrier #3. Consistent with 141.B2 (first-order no-go): the flux escapes 141.B2's *premise* (it is not zero-integral — Littlewood is the classical exception, $\int u\ge-O(\log T)$) but not its *moral*: first-order positivity already has its known-optimal theorem (Littlewood) and the flux adds no information.
5. **Green's identity settles nothing:** the term $\sum c(\rho)$ (uncontrolled under $O(T\log^2T)$, E-188.3) drowns any attempt to extract $\mathcal F_{1/2}$ from the volume; and the flux is already better bounded directly (point 3) than anything Green could give. §4.
6. **Spoils:** (i) [THEOREM 189.2] as a permanent bookkeeping piece — the currency $\sum b\log\gamma$ has a flux representation, so any future progress on $\int_0^T\log t\cdot\log|\zeta(\tfrac12+it)|\,dt$ with sign transfers to LP-134∞ with an explicit constant; (ii) essential positivity $\mathcal F_{1/2}\ge-O(\log^2T)$; (iii) the wall is now written as ONE theorem-barrier + one principle (mandate of 188 fulfilled): the signal $\sum b^2$ is second-order transverse, and the object's only anisotropic channel in Green's geometry is first order.

---

## 1. The exact object: the flux kernel is blind to zeros

**[LEMMA 189.1] (determinism of $\partial_\sigma u$ on the line).** For every $t>0$ that is not the ordinate of a zero,
$$\partial_\sigma u(\tfrac12+it)\;=\;\mathrm{Re}\,\frac{\zeta'}\zeta(\tfrac12+it)\;=\;\frac12\,\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it)\;=\;-\frac12\log\frac t{2\pi}\;+\;O(t^{-2}),$$
an exact identity at the central step: **the real part of $\zeta'/\zeta$ on the critical line contains no zero term**.

*Proof.* (1) $\partial_\sigma u=\mathrm{Re}(\zeta'/\zeta)$ by Cauchy–Riemann ([183.1] §1.1, verified in D188). (2) Functional equation $\zeta(s)=\chi(s)\zeta(1-s)$, logarithmic derivative:
$$\frac{\zeta'}\zeta(s)\;=\;\frac{\chi'}\chi(s)\;-\;\frac{\zeta'}\zeta(1-s).$$
At $s=\tfrac12+it$: $1-s=\tfrac12-it=\bar s$. Since $\zeta(\bar s)=\overline{\zeta(s)}$ (real coefficients, Schwarz reflection), $\frac{\zeta'}\zeta(\tfrac12-it)=\overline{\frac{\zeta'}\zeta(\tfrac12+it)}$. Hence
$$\frac{\zeta'}\zeta(\tfrac12+it)+\overline{\frac{\zeta'}\zeta(\tfrac12+it)}\;=\;\frac{\chi'}\chi(\tfrac12+it)\quad\Longrightarrow\quad 2\,\mathrm{Re}\,\frac{\zeta'}\zeta(\tfrac12+it)=\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it).$$
(3) Stirling applied to $\chi(s)=2^s\pi^{s-1}\sin(\tfrac{\pi s}2)\Gamma(1-s)$ (Titchmarsh §4.12): $\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it)=-\log\tfrac t{2\pi}+O(t^{-2})$, $t\ge1$. $\square$

**Independent verification (the twin's cancellation, E-188.6's microscope).** By partial fractions, an on-line zero's term $\tfrac12+i\gamma'$ is $\mathrm{Re}\,\frac1{i(t-\gamma')}=0$; the off pair $(\tfrac12\pm b+i\gamma)$ contributes $\mathrm{Re}\big[\frac1{-b+i\tau}+\frac1{b+i\tau}\big]=\frac{-b}{b^2+\tau^2}+\frac{b}{b^2+\tau^2}=0$ ($\tau=t-\gamma$). The cancellation is **pointwise and exact**, not on average — the Lemma obtains it without conditionally convergent sums, via the functional equation, which is the globally rigorous form of the same fact. Also note: $\mathrm{Re}\,\zeta'/\zeta$ extends continuously across each ordinate (the singularity lives entirely in $\mathrm{Im}=-S'$), while $u\to-\infty$ logarithmically (integrable): $\mathcal F_{1/2}$ is an absolutely convergent integral, well defined with no principal value.

**Reading.** D183 feared poles in the kernel (false proof of 183.4.b); D188 disproved them. Here the stronger fact is made clean: the kernel not only has no poles — **it has no signal**. It is the deterministic function $-\tfrac12\log\tfrac t{2\pi}$. The flux's anisotropy cannot come from the kernel; it comes only from $u$.

## 2. The flux identity: $\mathcal F_{1/2}$ = Littlewood with a log weight

With D183's convention (§2): $\mathcal F_{1/2}(T)=-\int_0^Tu\,\partial_\sigma u\,dt$ (outward normal of $R_T$ at $\sigma=\tfrac12$ is $-\partial_\sigma$). By [LEMMA 189.1], writing $\omega(t):=\log\tfrac t{2\pi}$:
$$\mathcal F_{1/2}(T)\;=\;\frac12\int_0^T\omega(t)\,\log|\zeta(\tfrac12+it)|\,dt\;+\;O(1),$$
(the $O(t^{-2})$ against $u$ integrates to $O(1)$ by local integrability of $u$ and Selberg; the segment $t\le2\pi e$ is $O(1)$).

**[LEMMA 189.2.a] (Littlewood on the line, form used).** $\displaystyle\int_0^T\log|\zeta(\tfrac12+it)|\,dt=2\pi J(T)+O(\log T)$, with $J(T)=\sum_{\gamma\le T}b$ (one summand per quadruple: from the quadruple, only $\beta=\tfrac12+b$, $\gamma>0$ has $\beta>\tfrac12$). This is Littlewood's lemma at $\sigma_0=\tfrac12$ (Littlewood 1924; Titchmarsh §9.9; same normalization as [180.4.b]). In particular $\int_0^Tu\,dt\ge-O(\log T)$. *(Cited, not re-derived: it is the [180.4.b] certified result.)*

**[THEOREM 189.2] (the boundary flux is the LP-134 currency).**
$$\mathcal F_{1/2}(T)\;=\;\pi\sum_{\gamma\le T}b\,\log\frac\gamma{2\pi}\;+\;O(\log^2T).$$

*Proof.* Let $L(t):=\int_0^tu(\tfrac12+iv)\,dv=2\pi\tilde J(t)+\varepsilon(t)$, $\tilde J(t)=\sum_{\gamma\le t}b$, $|\varepsilon(t)|\ll\log(t+2)$ [LEMMA 189.2.a]. Integration by parts ($\omega'(t)=1/t$):
$$\int_0^T\omega\,dL=\omega(T)L(T)-\int_{2\pi}^T\frac{L(t)}t\,dt+O(1)=2\pi\Big[\omega(T)\tilde J(T)-\int_{2\pi}^T\frac{\tilde J(t)}t\,dt\Big]+O(\log^2T),$$
where the error uses $|\omega(T)\varepsilon(T)|\ll\log^2T$ and $\int^T\frac{|\varepsilon|}t\ll\log^2T$. Exchanging sum and integral (everything positive, Tonelli):
$$\omega(T)\tilde J(T)-\int_{2\pi}^T\frac{\tilde J(t)}t\,dt=\sum_{\gamma\le T}b\Big[\omega(T)-\int_{\max(\gamma,2\pi)}^T\frac{dt}t\Big]=\sum_{\gamma\le T}b\,\log\frac{\max(\gamma,2\pi)}{2\pi}=\sum_{\gamma\le T}b\,\log\frac\gamma{2\pi}+O(1)$$
(zeros with $\gamma<2\pi$: there are none — the first zero is at $\gamma\approx14$; the adjustment is vacuous). Multiply by $\tfrac12$. $\square$

**Contrast with the local calculation (cross sanity check with D188 §2.3).** The signature of a quadruple in $u$ on the line, relative to two on-line zeros at $\gamma$, is $\log\frac{\tau^2+b^2}{\tau^2}\ge0$, with mass $\int_{-\infty}^\infty\log\big(1+\tfrac{b^2}{\tau^2}\big)d\tau=2\pi b$ (classical: $\int\log(1+b^2/x^2)dx=2\pi b$ by parts + arctan), localized at $|\tau|\lesssim b$. Weighted by the kernel $\tfrac12\omega(t)\approx\tfrac12\omega(\gamma)$ (smooth at scale $b$): contribution $\pi b\log\tfrac\gamma{2\pi}$ per quadruple — **exactly the summand of 189.2**. D188's signal ("$\asymp b\log t$ per off zero") is confirmed and promoted to a global identity.

**[COR 189.2.b] (positivity and the RH case).** $\mathcal F_{1/2}(T)\ge-O(\log^2T)$ unconditionally; under RH, $\mathcal F_{1/2}(T)=O(\log^2T)$. And **A does not control $\mathcal F_{1/2}$**: by Cauchy–Schwarz $\sum b\log\gamma\le(\sum b^2)^{1/2}(\sum_{\rm off}\log^2\gamma)^{1/2}$, which even with $E=O(1)$ leaves $\ll(N_{\rm off}\log^2T)^{1/2}$ — the $J$-weighted currency and the $E$ currency are not comparable without population control (consistent with E-188.5).

## 3. The unconditional budget: the weight $\log t$ buys nothing

**[PROP 189.3] (unconditional bound on the flux and on the LP-134 currency).**
$$\mathcal F_{1/2}(T)\;\le\;\Big(\tfrac14+o(1)\Big)\,T\log T\log\log T,\qquad\text{equivalently}\qquad\sum_{\gamma\le T}b\log\gamma\;\le\;\Big(\tfrac1{4\pi}+o(1)\Big)\,T\log T\log\log T,$$
**and this bound coincides (order and method) with partial summation over classical Littlewood: it is not new.**

*Proof.* By dyadic blocks $[T_k/2,T_k]$, $T_k=T/2^k$: in each block $\omega(t)\le\log\tfrac{T_k}{2\pi}$, and by Jensen (concavity of $\log$) with the second moment $\int_{T_k/2}^{T_k}|\zeta(\tfrac12+it)|^2dt\sim\tfrac{T_k}2\log T_k$ (Hardy–Littlewood 1918):
$$\int_{T_k/2}^{T_k}u\,dt\le\frac{T_k}2\cdot\frac12\log\Big(\frac2{T_k}\int_{T_k/2}^{T_k}|\zeta|^2\Big)=\frac{T_k}4\log\log T_k+O(T_k).$$
Summing $\sum_k\log T_k\cdot\big[\tfrac{T_k}4\log\log T_k+O(T_k)\big]\le(\tfrac12+o(1))\cdot\tfrac{T}4\cdot\log T\log\log T\cdot 2=(\tfrac14+o(1))T\log T\log\log T$ (geometric series in $T_k$; the factor $\log T_k\le\log T$ and $\sum T_k\le2T$ give the constant with $o(1)$ after separating $k\le\log\log T$). The equivalence with the sum is 189.2. *Comparison:* classical Littlewood is the case $\omega\equiv1$ of the same argument ($J(T)\le(\tfrac1{4\pi}+o(1))T\log\log T$, Littlewood 1924 via Jensen + second moment), and dyadic Abel partial summation over $J$ gives exactly $\sum b\log\gamma\ll T\log T\log\log T$ with the same constant. $\square$

**Why the weight cannot buy anything.** The argument's only zeta-dependent input is, block by block, $\int u\,dt$ — and the weight $\omega$, being **deterministic and slowly varying** ($\omega'/\omega\asymp1/(t\log t)$, constant on each block up to error $O(1)$), commutes with the machinery: any functional $\int W(t)\,u\,dt$ with deterministic slowly varying $W>0$ decomposes dyadically into copies of Littlewood. For a weight to help it would have to **anti-correlate with $u$** — i.e., contain zero information — and [LEMMA 189.1] says the only weight Green's geometry offers (the kernel $\partial_nu$) is precisely deterministic. The chink closes on itself: *the same theorem that makes the flux computable (signal-free kernel) makes it sterile (signal-free weight).*

**Could Littlewood itself be improved?** That would reduce to bounding $\int_0^Tu\,dt$ (with sign) better than $T\log\log T$. By [180.4.b] (bidirectional identity, certified in D188) that IS bounding $J(T)$: there is no third term. Moments are blind to sign (barrier #3); Selberg's CLT says typical $|u|$ is $\asymp\sqrt{\log\log T}$, so Jensen's mean $\le\tfrac12\log\log T$ is only improvable by detecting the cancellation — which is the unknown. Clean circularity, not a technical defect. *(Best possible here: under the plausible Selberg symmetry, $\int u\,dt=o(T\sqrt{\log\log T})$ "should" hold; but proving it unconditionally would imply $J(T)=o(T\sqrt{\log\log T})$, an improvement over Littlewood that the literature does not have — a gauge of difficulty, not our [GAP].)*

## 4. Does Green's identity settle anything? No: balance of the three pieces

With the E-188.x corrections, Green's identity [183.1] at scale $R\asymp1/\log T$ is
$$\underbrace{\mathcal D_R(T)}_{\text{volume}}\;=\;\underbrace{2\pi N(T)\log\tfrac1R-2\pi\sum_\rho h(\rho)+O(RN\log\tfrac1R)}_{\text{atoms}}\;+\;\underbrace{\mathcal F_{1/2}(T)}_{\text{critical boundary}}\;+\;\underbrace{O(\log^2T)}_{\text{horizontal boundaries}, \sigma=X}.$$
Budget of each piece: volume $\in[c\,T\log T\log\log T,\;C\,T\log^2T]$ with exact order undetermined (E-188.3); atoms: main term $\asymp T\log T\log\log T$ known, but $\sum h(\rho)$ bounded only by $O(N\log T)=O(T\log^2T)$ **with no sign or proved cancellation**; boundary: $\mathcal F_{1/2}\ll T\log T\log\log T$ by [PROP 189.3], and $\ge-O(\log^2T)$ by [COR 189.2.b].

**Extraction is impossible:** to extract $\mathcal F_{1/2}$ (and with it $\sum b\log\gamma$) from Green one would need to know volume and $\sum h(\rho)$ with error $o(T\log T\log\log T)$; the unknown part of $\sum h(\rho)$ is $O(T\log^2T)$ — a factor $\log T/\log\log T$ ABOVE the flux's direct bound from 189.3. **Green gives, for the flux, a bound worse than the trivial one.** In the other direction, using 189.3 + atoms to bound $\mathcal D_R$ also adds nothing: it reproduces the framing of E-188.3. The system has one equation and two large unknowns ($\mathcal D_R$, $\sum h$); the flux is the small unknown and is already better measured from outside. Nothing to extract.

## 5. The barrier, stated: #2-bis (first-order anisotropy)

**[PROP 189.4] (sealing of R2 — reabsorption mechanism).** The anisotropic channel of the flat Green geometry on $\{\sigma>\tfrac12\}$ — the critical boundary flux — satisfies: (i) its kernel is deterministic ([LEMMA 189.1]); (ii) its zero content is exactly the weighted first moment $\pi\sum b\log\tfrac\gamma{2\pi}$ ([THEOREM 189.2]) — **first order in $b$, not second**; (iii) any unconditional upper bound on it via existing machineries factors, through dyadic decomposition of the deterministic weight, into Littlewood's problem $\int_0^Tu\,dt$ with sign, which by the identity [180.4.b] is equivalent to bounding $J(T)$ — barrier #3 territory; (iv) the resulting bound, $T\log T\log\log T$, coincides with partial summation of Littlewood's 1924 theorem and improves neither $E(T)\ll T/\log T$ nor $J(T)\ll T\log\log T$ nor the LP-134 currency.

*Proof.* (i)=189.1, (ii)=189.2, (iii)=§3 (slowly-varying-weight argument + bidirectionality 180.4.b), (iv)=189.3. $\square$

**Relation to 141.B2 and the wall.** 141.B2 (first-order no-go) rules out zero-integral linear functionals; Littlewood is the sign exception (positivity $\int u\ge-O(\log T)$) and that is why first order DOES have a theorem — but **only one**, the 1924 one, and the boundary flux turns out to be that theorem with an inert weight. The wall's taxonomy is thus (188's mandate fulfilled): **one theorem-barrier** (#1, densities, 176.9) **+ one unified structural principle**: *the signal $\sum b^2$ is a transverse second moment; unconditional functionals are isotropic (blind to direction: #1, #4-interior), signed (blind by cancellation: #3), line-saturated (#2, conditional-on-Farmer), or first-order anisotropic (this doc: exhausted by Littlewood).* The box "second-order anisotropic with definite sign" remains empty: it is GAP-183.1 = GAP-180.1 = genus 141.G1, intact.

## 6. Anti-circularity test

| Piece | ζ-free? | Unconditional? | Notes |
|---|---|---|---|
| [LEMMA 189.1] deterministic kernel | no (ζ's functional eq.) | yes (identity) | Schwarz reflection, no sums over zeros |
| [THEOREM 189.2] flux = currency | machinery yes (Abel) | yes | input: Littlewood 1924 (identity) |
| [PROP 189.3] bound | no | yes | inputs: Hardy–Littlewood 1918 + Jensen |
| [PROP 189.4] sealing | — | yes | uses certified 180.4.b; scope: dyadically-factorizable machineries (formal class in (iii), informal in the moral — same status as barrier #3) |

No step assumes RH, A, LP-112 or LP-134. No literature GAP is used as closed; [PROP 189.3] deliberately avoids GAP 180.L3/183.L1 (Tsang) by using only the second moment of $|\zeta|$, not the shifted one of $\log|\zeta|$.

## 7. Verdict

**R2: SEALED — outcome (b) with structural spoils (c-minor).** There is no new bound on $E(T)$, on $J(T)$, or on $\sum b\log\gamma$: the boundary flux is the LP-134 currency disguised as a flux, and its budget is Littlewood's with an inert weight. The reabsorption mechanism is proved, not asserted (the E-188.4 debt is settled with an exact identity).

**Proved:** [LEMMA 189.1] (deterministic kernel, identity); [THEOREM 189.2] ($\mathcal F_{1/2}=\pi\sum b\log\tfrac\gamma{2\pi}+O(\log^2T)$); [COR 189.2.b] (positivity; A does not control the flux); [PROP 189.3] ($\sum b\log\gamma\le(\tfrac1{4\pi}+o(1))T\log T\log\log T$, = Littlewood by parts, not new); [PROP 189.4] (barrier #2-bis, sealing of R2).

**Numbered GAPs:**
- **[GAP-189.1]** Does there exist a weight $W(t)>0$ that is NOT deterministic — built from unconditional ζ data (e.g. normalized $|\zeta|^2$, local moments) — such that $\int_0^TW\,u\,dt$ bounds weighted $J$ better than Littlewood without re-entering via the identity? The decomposition of §3 only covers deterministic slowly-varying weights; a randomly-correlated weight formally escapes [PROP 189.4.iii], but every candidate examined (weight $|\zeta|^2$: gives the moment $\int|\zeta|^2\log|\zeta|$, twisted-moment territory, same floor) re-enters. Status: third-generation formal chink, low priority.
- **[literature GAP 189.L1]** Is the bound $\sum_{\gamma\le T}(\beta-\tfrac12)\log\gamma\ll T\log T\log\log T$ — or an improvement — explicit in the literature ($S_1$, Fujii)? It is partial summation of Littlewood, hence "known-in-potential"; check whether anyone improved it (connect with 180.L4/188.L2, Fujii audit pending).

**Successor direction.** With R2 sealed and R1 (Farmer's floor, 188.L1) as the wall's only remaining formal chink, the front returns to where D188 §5 left it: the empty box "second-order anisotropic with sign" (GAP-183.1/180.1/141.G1) and the [BRIDGE 183 §4.2] spacetime bridge ($\mathcal D_{\sqrt t}\leftrightarrow\dot I=-2\kappa-D$, Phase 54), which is the program's only object living in that box. This document's usable byproduct for tower 2: **any future improvement of $\int\omega\,u\,dt$ converts into an improvement of the LP-134∞ currency with exact constant $\pi$** ([THEOREM 189.2]).

---

## References

- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Littlewood's lemma; $J(T)\ll T\log\log T$.]
- G. H. Hardy, J. E. Littlewood, "Contributions to the theory of the Riemann zeta-function...", *Acta Math.* 41 (1918). [Second moment $\sim T\log T$.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford 1986. §4.12 ($\chi$, Stirling); §9.9 (Littlewood, $S_1$).
- A. Selberg, "Contributions...", *Arch. Math. Naturvid.* 48 (1946). [CLT of $\log|\zeta|$ — only calibrational here.]
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985.

**Internal documents:** D170 (Thm 170.5); D173 (173.C); D176 (176.9); D180 (180.4 with E-188.1); D183 (183.1 with E-188.2/3, $\mathcal F_{1/2}$, with E-188.4/5/6); **D188 (audit that opened R2; all errata E-188.x applied)**; Phase 54 (balance law); D177/178 (currency $\sum b\log\gamma$, LP-134∞, confinement 178.C).
