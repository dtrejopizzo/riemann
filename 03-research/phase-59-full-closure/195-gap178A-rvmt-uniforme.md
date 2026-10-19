# Document 195 — Closure of GAP-178.A: the Riemann–von Mangoldt count in unit windows is uniform in $t\in[0,1]$ for the arithmetic $H_t$ (full theorem via Jensen with vertical convolution)

**Program:** Riemann Hypothesis — Phase 59 (full closure)
**Mandate:** prove [GAP-178.A] = [BRIDGE 178.5] (Doc 178 §2.6): the hypothesis (RvM-t), the only pending technical input of the dynamic half of Tower 2 (Thms 178.4/178.4′/178.7/178.10).
**Contract:** [THEOREM]/[LEMMA] only with full proof; deaths documented; backward-only citations (de Bruijn 1950; Ki–Kim–Lee 2009; Polymath 15, 2019; Titchmarsh, *Theory of the Riemann Zeta-Function*, for classical RvM, Stirling, and convexity).

---

## 0. Conventions and exact statement

Polymath 15 chart as in Doc 167 §0.1 / Doc 178 §0: $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}$, with $\partial_tH_t=-\,\partial_z^2H_t$ and $H_0=\tfrac18\,\Xi(\cdot/2)$, i.e. $H_0(z)=\tfrac18\,\xi\!\bigl(s(z)\bigr)$, $s(z):=\tfrac12+\tfrac{iz}2$. The zeros of $\zeta$ in the strip $0<\sigma<1$ correspond to zeros of $H_0$ in the band $|\mathrm{Im}\,z|<1$; "height $\gamma$" = $\mathrm{Re}\,z\asymp\gamma$ (fixed rescaling from Doc 178, irrelevant to absolute constants). $L:=\log\gamma$, $\rho:=L/4\pi$.

**[TARGET STATEMENT (RvM-t), verbatim from Doc 178 §2.3].** *There exists an absolute $C_0$ such that for every $t\in[0,1]$ and every interval $J\subset\mathbb R$ with $|J|\le1$ centered at large height $\gamma$: $\#\{x\in Z_t\cap J\}\le\rho(\gamma)|J|+C_0\log\gamma$* (real zeros of $H_t$, with multiplicity). We will prove something stronger: the count of **all** zeros (real or not) of $H_t$ in the box $J\times[-1,1]$ is $\le C_0\log\gamma$, uniform in $t\in[0,1]$.

**Sign check (mandated).** The mandate writes "forward $\partial_tH=\partial_z^2H$, Gaussian convolution over REAL $w$." In Doc 178's chart the sign is the **opposite** one ($e^{tu^2}$ in Fourier: de Bruijn 1950), and therefore the correct integral representation is the **vertical** convolution:

**[LEMMA 195.0] (vertical representation).** For $t>0$ and every $z\in\mathbb C$,
$$H_t(z)\;=\;\frac1{\sqrt{4\pi t}}\int_{\mathbb R}H_0(z+iw)\,e^{-w^2/4t}\,dw .$$
*Proof.* For $H_0=\cos(\lambda z)$: $\cos(\lambda(z+iw))=\tfrac12(e^{i\lambda z-\lambda w}+e^{-i\lambda z+\lambda w})$ and $\frac1{\sqrt{4\pi t}}\int e^{\pm\lambda w-w^2/4t}dw=e^{t\lambda^2}$, so the average is $e^{t\lambda^2}\cos(\lambda z)$ — exactly the chart's $e^{tu^2}$ factor. The general case follows by superposition: $H_0(z+iw)=\int_0^\infty\Phi(u)\cos((z+iw)u)du$ with $\Phi$ of super-exponential decay, Fubini applies ($\int\int\Phi(u)e^{|w|u-w^2/4t}<\infty$ since $u^2$ loses against $w^2/4t$… more precisely $\int e^{|w|u-w^2/4t}dw=O(e^{tu^2})$ and $\int\Phi e^{u^2}<\infty$). $\square$

This sign correction is not pedantic: it is **the reason route 1 closes over all of $[0,1]$** (Remark 195.6).

Arithmetic–archimedean factorization: for $\sigma=\mathrm{Re}\,s>1$, $\xi(s)=\mathfrak G(s)\,\zeta(s)$ with $\mathfrak G(s):=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)$, and $\zeta(s)=\sum n^{-s}$ absolutely convergent. We write $\mathfrak g(z):=\mathfrak G(s(z))$ (holomorphic and zero-free in $\mathrm{Re}\,z>0$, $\mathrm{Im}\,z<-1$, the region where we use it).

---

## 1. The two size lemmas (Stirling)

Let $\gamma$ be large and $z_0:=\hat\gamma-iB$ with $\hat\gamma:=\gamma+\tfrac12$ (center of the window) and $B\ge6$ even and fixed (to be chosen absolute in §3). Then $s(z_0)=\tfrac12+\tfrac B2+\tfrac{i\hat\gamma}2$, with $\sigma_0=\tfrac12+\tfrac B2\ge\tfrac72$.

**[LEMMA 195.1] (local envelope of $H_0$ in a strip).** There exist absolute $A,C>0$ such that for $x\ge2$, $|y|\le 4B+8$:
$$|H_0(x+iy)|\;\le\;C\,(1+x)^{A}\,|\mathfrak g(x)|\;e^{\varphi(x)\,|y|},\qquad \varphi(x):=\tfrac14\log\tfrac{x}{4\pi}.$$
*Proof.* By the functional equation $\xi(s)=\xi(1-s)$ it suffices to take $\mathrm{Im}\,z\le0$, i.e. $\sigma\ge\tfrac12$. Uniform Stirling in $\sigma\in[\tfrac12,\,2B+5]$, $|s|\asymp x$: $\log|\mathfrak G(\sigma+i\tau)|=\log|\mathfrak G(\tfrac12+i\tau)|+(\sigma-\tfrac12)\cdot\tfrac12\log\tfrac{|\tau|}{2\pi}+O(\log(2+|\tau|))$; with $\tau=x/2$, $\sigma-\tfrac12=|y|/2$, the increment is $\varphi(x)|y|+O(\log x)$. For $\zeta$: for $\sigma\ge2$, $|\zeta|\le\zeta(2)$; for $\tfrac12\le\sigma\le2$, $|\zeta(s)|\le C|s|$ (crude convexity bound, [Titchmarsh §5]). The factors $O(\log x)$ and $|s|$ are absorbed into $(1+x)^A$. $\square$

**[LEMMA 195.2] (exact first-order expansion of $\mathfrak g$ along the vertical).** Let $\psi:=-\frac{d}{dw}\log\mathfrak g(z_0+iw)\big|_{w=0}$. Then $\psi=\varphi(\hat\gamma)+\tfrac{i\pi}8+O(\hat\gamma^{-1})$ and, for $-\gamma/2\le w\le B-4$,
$$\mathfrak g(z_0+iw)\;=\;\mathfrak g(z_0)\,e^{-\psi w+R(w)},\qquad |R(w)|\le C\,w^2/\gamma .$$
*Proof.* $\frac{d}{dw}\log\mathfrak g(z_0+iw)=i\cdot\frac{i}{2}\frac{d}{ds}\log\mathfrak G=-\tfrac12\bigl[\tfrac12\log\tfrac{s}{2\pi}+O(|s|^{-1})\bigr]$; with $s\approx i\hat\gamma/2$, $\log\tfrac{s}{2\pi}=\log\tfrac{\hat\gamma}{4\pi}+\tfrac{i\pi}2+O(\hat\gamma^{-1})$, which gives $\psi$. On the indicated segment $\sigma\in[\tfrac52,\tfrac\gamma4+B]$ and $|s|\asymp\gamma$, hence $\bigl|\tfrac{d^2}{dw^2}\log\mathfrak g\bigr|=\tfrac14\bigl|\tfrac{d}{ds}\log\tfrac{s}{2\pi}+\dots\bigr|\le C/\gamma$; Taylor with integral remainder gives $R$. $\square$

(Note: $\varphi=\pi\rho+O(1)$: the "phase front" of $\xi$ is the RvM density — internal coherence.)

---

## 2. The pointwise lower bound, uniform in $t\in[0,1]$

**[THEOREM 195.3] (quantitative non-vanishing at $z_0$).** There exist absolute $B$ (even), $c>0$, $A'>0$ such that for every $t\in[0,1]$ and $\gamma\ge\gamma_0$:
$$|H_t(z_0)|\;\ge\;c\,\gamma^{-A'}\,|\mathfrak g(\hat\gamma)|\;e^{B\varphi+t\varphi^2},\qquad \varphi=\varphi(\hat\gamma).$$
*Proof.* Case $t=0$: $|H_0(z_0)|=\tfrac18|\mathfrak g(z_0)||\zeta(s_0)|\ge\tfrac18|\mathfrak g(z_0)|(2-\zeta(\sigma_0))\ge c|\mathfrak g(\hat\gamma)|e^{B\varphi}\gamma^{-A'}$ (Lemma 195.2 to compare $|\mathfrak g(z_0)|$ with $|\mathfrak g(\hat\gamma)|e^{B\varphi}$ modulo $\gamma^{O(1/\gamma)}$ and polynomials; $\zeta(\sigma_0)<2$ since $\sigma_0\ge\tfrac72$). Let $t\in(0,1]$. By Lemma 195.0, $8H_t(z_0)=(4\pi t)^{-1/2}\int\xi(s(z_0+iw))e^{-w^2/4t}dw$. Split $\mathbb R=G\cup G^c$, $G:=(-\gamma/2,\,w_c]$, $w_c:=B-4$ (on $G$, $\sigma(w)=\tfrac12+\tfrac{B-w}2\ge\tfrac52$: factorization range).

**(i) Main term.** On $G$: $\xi=\mathfrak g\cdot(1+(\zeta-1))$. The term with the $1$:
$$\frac{\mathfrak g(z_0)}{\sqrt{4\pi t}}\int_G e^{-\psi w+R(w)}e^{-w^2/4t}dw .$$
The full Gaussian without $R$: $(4\pi t)^{-1/2}\int_{\mathbb R}e^{-\psi w-w^2/4t}dw=e^{t\psi^2}$ (exact, completed square; $\psi$ complex, no contour shifting), with $|e^{t\psi^2}|=e^{t(\varphi^2-\pi^2/64)+O(t\varphi/\gamma)}\ge0.85\,e^{t\varphi^2}$ for $\gamma$ large. Errors: (a) tails — for $w>w_c$, $|e^{-\psi w}|=e^{-\varphi w}$ and $e^{-w^2/4t}\le1$ give a relative mass $\le e^{-\varphi w_c-w_c^2/4t-t\varphi^2}\cdot e^{t\varphi^2}\!\big/e^{t\varphi^2}$; since $\tfrac{w_c^2}{4t}+t\varphi^2\ge\varphi w_c$ (AM–GM), the tail relative to the main term is $\le e^{-2\varphi w_c}\cdot O(\sqrt{1+t}\,(1+\varphi\sqrt t))=O(\gamma^{-w_c/2+\epsilon})$; for $w<-\gamma/2$, $e^{\varphi\gamma/2-\gamma^2/16t}\le e^{-\gamma^2/32}$ for $t\le1$, negligible compared to everything present. (b) curvature — $|e^{R}-1|\le C\tfrac{w^2}\gamma e^{Cw^2/\gamma}$ and the effective mass of $e^{-\varphi w-w^2/4t}$ lives in $|w|\le2t\varphi+C\sqrt t\le C L$: relative contribution $O(L^2/\gamma)$. Total: main term $=\mathfrak g(z_0)e^{t\psi^2}(1+O(\gamma^{-1/2}))$, of modulus $\ge0.8\,|\mathfrak g(z_0)|e^{t\varphi^2}$.

**(ii) Arithmetic error on $G$.** $|\zeta(s(w))-1|\le\zeta(\sigma(w))-1\le\zeta(\tfrac52)-1<0.342$ pointwise on $G$; by the triangle inequality and the same Laplace computation on $|\mathfrak g(z_0+iw)|=|\mathfrak g(z_0)|e^{-\varphi w+\mathrm{Re}\,R}$:
$$\Bigl|\frac1{\sqrt{4\pi t}}\int_G\mathfrak g\,(\zeta-1)\,e^{-w^2/4t}dw\Bigr|\;\le\;0.342\,|\mathfrak g(z_0)|\,e^{t\varphi^2}\,(1+O(\gamma^{-1/2})).$$
Margin: $0.8-0.342>0.45$. *(This is the only fine-tuning point: the main term's deficit $e^{-t\pi^2/64}\ge0.85$ must exceed $\zeta(\sigma_0')-1$ in the good range; $\sigma\ge\tfrac52$ is more than enough. No cancellation is needed: only absolute convergence of the Dirichlet series.)*

**(iii) Remainder $w\in(w_c,\infty)$** (the vertical crosses the zero band and exits above; there is no factorization there, only Lemma 195.1 with $|y(w)|=|w-B|$):
$$\le\;C\gamma^{A}|\mathfrak g(\hat\gamma)|\,\frac1{\sqrt{4\pi t}}\int_{w_c}^\infty e^{\varphi|w-B|-w^2/4t}dw\;\le\;C\gamma^{A}|\mathfrak g(\hat\gamma)|\,e^{t\varphi^2}\,e^{-2\varphi w_c}\,,$$
using again $\varphi w+\tfrac{w^2}{4t}+t\varphi^2\ge2\varphi w\ge2\varphi w_c$ on the branch $w\le B$ and $\varphi(w-B)-\tfrac{w^2}{4t}\le t\varphi^2-2B\varphi$ on the branch $w>B$. Since $|\mathfrak g(z_0)|\ge c\gamma^{-A}|\mathfrak g(\hat\gamma)|e^{B\varphi}$, the remainder relative to the main term is $\le C\gamma^{2A}e^{-2\varphi w_c-B\varphi}=C\gamma^{2A-(w_c/2)-(B/4)}\cdot(4\pi)^{O(B)}$. **Absolute choice:** $B:=8A+16$ (hence $w_c=8A+12$): the exponent is $\le-2$. Summing (i)–(iii): $|8H_t(z_0)|\ge0.4\,|\mathfrak g(z_0)|e^{t\varphi^2}$, and Lemma 195.2 translates $|\mathfrak g(z_0)|\ge c\gamma^{-A'}|\mathfrak g(\hat\gamma)|e^{B\varphi}$. $\square$

**Structural reading.** The chart's flow ($e^{tu^2}$) **amplifies** the archimedean mode: $e^{+t\varphi^2}$. The amplification will appear identically in the upper bound and cancels in the Jensen ratio. The dominant term is the $n=1$ term of the Dirichlet series over the *whole* range $t\in[0,1]$ because the saddle point of the vertical integral is at $w^*\approx-2t\varphi$ (depth $\asymp tL$, i.e. increasing $\sigma\asymp tL$): **the flow pushes the effective evaluation toward the region of absolute convergence**, where $\zeta\to1$. The larger $t$, the more dominant $n=1$.

---

## 3. The local upper bound and Jensen

**[LEMMA 195.4] (local upper bound, uniform in $t$).** For $|z-z_0|\le 2B+4$ and $t\in[0,1]$:
$$|H_t(z)|\;\le\;C\,\gamma^{A}\,|\mathfrak g(\hat\gamma)|\,e^{(3B+4)\varphi+t\varphi^2}.$$
*Proof.* Triangle inequality in Lemma 195.0 + Lemma 195.1 (with $|y|\le|\mathrm{Im}\,z|+|w|\le 3B+4+|w|$ where for large $|w|$ one uses the global order-$1$ bound of $\xi$, $\log|H_0(x+iy)|\le C(1+|y|)\log(2+|x|+|y|)$, crushed by $e^{-w^2/4t}$ with $t\le1$):
$(4\pi t)^{-1/2}\int e^{\varphi|w|-w^2/4t}dw\le 2e^{t\varphi^2}+O(1)$; the horizontal variation of $|\mathfrak g(x)|$ for $|x-\hat\gamma|\le2B+4$ is $\gamma^{O(1)}$, absorbed into $\gamma^A$ (relabeling $A$). $\square$

**[THEOREM 195.5] (= (RvM-t); GAP-178.A closed).** There exists an absolute $C_0$ such that for every $t\in[0,1]$ and every $\gamma\ge2$, the number of zeros of $H_t$ (with multiplicity) in the box $[\gamma,\gamma+1]\times[-1,1]$ is $\le C_0\log\gamma$. In particular the statement (RvM-t) of Doc 178 §2.3 holds.
*Proof.* For $\gamma\ge\gamma_0$: the box is contained in $D(z_0,r_1)$, $r_1:=B+2$ (distance from the center $z_0=\hat\gamma-iB$ to any point of the box $\le\sqrt{\tfrac14+(B+1)^2}<B+2$). Jensen with $r_2=2r_1$:
$$N\;\le\;\frac{1}{\log2}\Bigl[\log\max_{|z-z_0|\le 2r_1}|H_t|-\log|H_t(z_0)|\Bigr]\;\le\;\frac{1}{\log 2}\Bigl[(2B+4)\varphi+(A+A')\log\gamma+C\Bigr]\;\le\;C_0\log\gamma,$$
by Theorems 195.3 and Lemma 195.4: **the $t\varphi^2$ terms cancel exactly** and what remains is linear in $\log\gamma$ with absolute constants, uniform in $t\in[0,1]$ (the case $t=0$ is the classical one, [Titchmarsh §9.2], or the limit $t\to0^+$ of the above). For $2\le\gamma\le\gamma_0$: $(t,z)\mapsto H_t(z)$ is continuous, $H_t\not\equiv0$ (its Fourier transform $e^{tu^2}\Phi$ is not zero), and by Hurwitz + compactness of $[0,1]$ the count on the fixed compact set $[0,\gamma_0+1]\times[-1,1]$ is bounded uniformly in $t$; it is absorbed into $C_0$. $\square$

---

## 4. Deaths and remarks

**[REMARK 195.6] (why the sign decides; death of the "forward" reading).** With the mandate's sign ($\partial_tH=+\partial_z^2H$, **horizontal** Gaussian convolution) the same strategy dies for $t\gtrsim1/\log\gamma$: the local archimedean mode has complex frequency $-\tfrac\pi8\pm i\varphi$ and the forward heat flow damps it by $e^{-t\varphi^2}$, sinking the value at $z_0$ below the $n\asymp\sqrt{\gamma}$ terms of the central range of the approximate functional equation (whose pointwise lower bound is a non-vanishing problem for short sums, out of reach); the Jensen cost would be $t\log^2\gamma$. We therefore checked the convention of Doc 178 §0 line by line: it is de Bruijn's ($e^{tu^2}$), backward in $z$, and then the amplification $e^{+t\varphi^2}$ is **common** to both the maximum and the center and cancels. The mandate's sentence "the convolution is over the real line (de Bruijn §2)" is incorrect in this chart; the correct version is Lemma 195.0. This correction is the proof.

**[REMARK 195.7] (route 2 unnecessary; its death).** Transfer via flux (count at $t=0$ + net flux through the boundary) is circular in its natural form: the velocity of the zeros is bounded using the count (Lemma 178.6 already needs it) and the boundary flux requires a lower bound on $|H_t|$ at the boundary — the same problem route 1 solves directly. Not executed: route 1 closed.

**[REMARK 195.8] (route 3 unnecessary).** No effective statement of [P15] nor the asymptotics of [KKL 2009] is invoked: the proof uses only Stirling, the Dirichlet series in $\sigma\ge\tfrac52$, crude convexity of $\zeta$ in a fixed strip, and de Bruijn's integral representation. Bridge 178.5's [literature gap] is replaced by a self-contained proof.

**[REMARK 195.9] (what is stronger than requested).** (a) The entire complex box is counted, not just real zeros; (b) uniformity holds over all $t\in[0,1]$ (and the proof gives the same for $t\in[0,T_0]$ with $C_0(T_0)$ for any fixed $T_0$), while Thms 178.4/178.4′ only use it for $t\le C'L^{-2}$; (c) byproduct: $H_t(\hat\gamma-iB)\ne0$ with an explicit lower bound — a "quantitative zero-free region" below the axis, uniform in the flow, consistent with de Bruijn 1950 (the zero band does not grow) but independent of it.

**Anti-circularity test.** Inputs: Stirling ($\Gamma$), absolute convergence of $\sum n^{-s}$ for $\sigma>1$, $|\zeta|\le C|s|$ for $\tfrac12\le\sigma\le2$ (convexity, no zero-free regions), functional equation of $\xi$, de Bruijn's representation. **Not** used: any information about the location of zeros of $\zeta$ or of $H_t$, any RH/density-type hypothesis, any result from Docs 167–190 (only the statement to be proved from Doc 178 is *cited*). The completed count does not re-enter any input. No circularity.

---

## 5. Verdict

**[GAP-178.A] CLOSED: (RvM-t) is a [THEOREM] (195.5), unconditional and uniform in $t\in[0,1]$, with a complete, self-contained proof.** Immediate consequences for Tower 2 (dynamic half):

1. **[Thm 178.4/178.4′]** loses the condition "(RvM-t)": it remains conditional **only** on local reality (R) in $[t/2,t]$ — which is a declared structural hypothesis, not technical debt. Tower 2's dynamic half rests **on theorems**.
2. **[Lemma 178.3]** (short compressed blocks) is now unconditional.
3. **[Thm 178.7]** and **[Thm 178.10]** (177.B ⟺ confinement) lose the "(RvM-t)" module; what remains irreducible is still 178.C/confinement at $t=0$, exactly as Doc 178 diagnosed — the quasi-RH-hard calibration of 177.B does not change.

**Residual GAPs of this document:**
- **[GAP-195.A] (minor, cosmetic):** the constants $A,B,C_0$ are not numerically optimized (the contract excludes numerics); any future use needing an explicit $C_0$ must redo §1–§3 with explicit Stirling — routine, no wall.
- No mathematical GAP remains open on (RvM-t).

**State of Tower 2 after this document:** static pincer $178.\mathrm C\wedge\mathrm{LP}\text{-}134^\infty\Rightarrow m<\infty$ (Cor 178.11, certified in Phase 58) + dynamic half 178.4′ now free of technical debt. The remaining hard objects are the usual ones: 178.C and LP-134∞.
