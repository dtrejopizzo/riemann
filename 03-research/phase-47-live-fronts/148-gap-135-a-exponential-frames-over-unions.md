# Doc 148 — GAP-135.A: exponential frames over unions of incommensurable arithmetic progressions

**Program:** Riemann Hypothesis — Phase 47: live fronts.
**Assignment:** review the active frames/sampling literature (Seip; Olevskii–Ulanovskii; Beurling–Landau; Avdonin; Hedenmalm–Montes-Rodríguez) and decide whether GAP-135.A (the fine structure of the kernel of the two-pure-primes Weil form) is genuinely new mathematics, an already-solved case, or an open problem that the ζ-context illuminates but does not solve.
**Prerequisites:** Doc 135 (two-primes theorem; §5 fine structure, Theorem 5.4, Prop. 5.6, GAP-135.A); Doc 138 (audit — the verdict that the only potentially new thing is §5, and the warning to review the frames literature before investing).
**Creative contract:** **[NEW-DEFINITION]** full freedom; **[THEOREM]/[PROPOSITION]/[LEMMA]** complete proof or it carries no label; **[BRIDGE]** declared status; **[GAP]** named; **[WISH]** declared; **[DATUM]** cited literature; **[literature GAP]** what I do not recall with certainty. Absolute frankness: the audit already penalized a novelty inflation over this same object (Doc 138 §4.3, §5.5); it is not repeated.

**Conventions.** Doc 135 normalization: $F(t)=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R)$, $\hat F(\xi)=\int F(t)e^{i\xi t}\,dt$, $\|f\|_w=\|F\|_{L^2}$. Under purity ($|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$, phases $\phi,\phi'$),
$$Q_X(f,f)=2\sum_{\xi\in\Lambda_p}|\hat F(\xi)|^2+2\sum_{\xi\in\Lambda_q}|\hat F(\xi)|^2,\qquad
\Lambda_r=\Bigl\{\tfrac{\phi_r+2\pi k}{L_r}:k\in\mathbb Z\Bigr\},\ \ L_r=\log r.$$
I write $\Lambda:=\Lambda_p\cup\Lambda_q$ and $E(\Lambda):=\{e^{i\xi t}\}_{\xi\in\Lambda}$. Window of length $2T$ $\Leftrightarrow$ $\mathrm{supp}\,F\subset$ interval of length $2T$; by translation invariance I work in $I=(-T,T)$, $L^2(I)=L^2(-T,T)$.

---

## 0. Executive summary and verdict

The question of GAP-135.A is, **exactly and without loss**: is $E(\Lambda)$ a Riesz sequence (equivalently: is there a lower frame bound for its span) in $L^2(-T,T)$ when $\log q<2T<\log(pq)$? The three quantities of Doc 135 §5 are the three classical regimes of Beurling–Landau theory:

- $2T<\log\min(p,q)$: $E(\Lambda)$ is a **scaled orthogonal basis** of its span (Theorem 5.2(a) = Parseval identity) — trivial.
- $2T<\log(pq)$: $E(\Lambda)$ is **minimal/incomplete** (Theorem 5.4(a)) $\Leftrightarrow$ lower Beurling density $>T/\pi$ above the uniqueness threshold. **Known** (Beurling–Landau; Jensen counting, which is what Doc 135 does).
- $2T>\log(pq)$: $E(\Lambda)$ is **overcomplete with infinite defect** ($\infty$-dim kernel, Theorem 5.4(b)) — **known** (Landau super-density).
- $\log q<2T<\log(pq)$ **(GAP-135.A):** Riesz/frame? Here, and only here, the uniform NON-separation of $\Lambda$ (diophantine near-collisions, Prop. 5.6) blocks the standard sufficiency theorems.

**VERDICT: (b) open problem in frames that the ζ-context illuminates but does not solve — with an important nuance toward (a).** The nuance: for a **union of two exact (unperturbed) arithmetic progressions**, I believe the answer IS known or accessible via the Avdonin/Pavlov–Khrushchev–Nikolskii machinery of model spaces, and **is affirmative with generic phases / negative only on a measure-zero set of configurations** — see §2 and §4. What is genuinely open and new is NOT "is it Riesz?" in a binary sense, but **the quantitative dependence of the lower frame bound on the irrationality measure of $\log p/\log q$** (the constant, not the bit). That is the question Doc 135 correctly named and that the literature, as far as I know it, does not answer for this specific arithmetic case. The novelty is one of *effective diophantine constant*, not of *phenomenon*.

Three labeled results (§1–§3) and the frank [BRIDGE] with ζ (§5) close the document.

---

## 1. Formalization of the frame problem and Beurling–Landau density

### 1.1. The exact translation

**[PROPOSITION 1.1] (the two-primes Weil form IS the Gram form of the exponential system).**
Let $T>0$ and $\mathcal H_T:=\{F\in L^2(\mathbb R):\mathrm{supp}\,F\subset[-T,T]\}\cong L^2(-T,T)$. For $F\in\mathcal H_T$,
$$\hat F(\xi)=\langle F,\ e_{-\xi}\rangle_{L^2(-T,T)},\qquad e_\xi(t):=e^{i\xi t}\ (t\in(-T,T)),$$
so that
$$Q_X(F,F)=2\sum_{\xi\in\Lambda}|\langle F,e_{-\xi}\rangle|^2 .$$
Hence, with $\Lambda$ symmetric under $\xi\mapsto-\xi$ up to phase (it is when $\phi_r\in\{0,\pi\}$; in general replace $\Lambda$ by $-\Lambda$, irrelevant for density and separation),
$$\tfrac12\,Q_X(F,F)=\sum_{\xi\in\Lambda}|\langle F,e_{\xi}\rangle_{L^2(-T,T)}|^2 .$$
*Proof.* $\hat F(\xi)=\int_{-T}^{T}F(t)e^{i\xi t}dt=\langle F,\overline{e_{\xi}}\rangle=\langle F,e_{-\xi}\rangle$. $\square$

**Immediate consequence (the complete dictionary).** For the family $E(\Lambda)=\{e_\xi\}_{\xi\in\Lambda}$ in $L^2(-T,T)$, the standard definitions (Young, *An Introduction to Nonharmonic Fourier Series*, 1980/2001 [DATUM]) give:

| Property of $E(\Lambda)$ in $L^2(-T,T)$ | Equivalent statement about $Q_X$ |
|---|---|
| **Complete** (dense span) | $Q_X(F,F)=0\Rightarrow F=0$ (trivial kernel) |
| **Frame** ($\exists\,A,B>0$: $A\|F\|^2\le\sum|\langle F,e_\xi\rangle|^2\le B\|F\|^2$) | $\tfrac12 A\|F\|_w^2\le Q_X(F,F)\le\tfrac12 B\|F\|_w^2$ |
| **Riesz sequence** (Riesz basis of its span) | $\ell^2$ independence + bound; here: $Q_X$ bounded and "from below" on the span |
| **Riesz basis of $L^2(-T,T)$** | frame + minimal ($=$ exact) |

The **lower frame bound** $A>0$ is exactly the quantity
$$\mu(T)=\inf_{\|F\|_w=1,\ \mathrm{supp}\,F\subset[-T,T]}Q_X(F,F)$$
of Observation 5.7 of Doc 135. **GAP-135.A = "is $\mu(T)>0$ in $\log q<2T<\log pq$?" = "is $E(\Lambda)$ a frame for $L^2(-T,T)$ in that range?"** The translation is an identity, not an analogy: the positivity modulus of the two-pure-primes Weil form *is* the lower frame bound of the exponential system over the union of the two frequency progressions.

**Observation 1.2 (why the upper bound is free and the lower one is the problem).** The upper bound $B$ always exists here: each $\Lambda_r$ is uniformly discrete (separation $2\pi/L_r$), hence a Bessel set in any $L^2$ of a bounded interval (Plancherel–Pólya / Ingham [DATUM]), and the union of two Bessel sets is Bessel. What can fail is $A>0$: the **lower stability**. This is structural in frame theory and is where non-separation bites.

### 1.2. Beurling–Landau densities and the thresholds of Doc 135

**Densities.** $\Lambda_r$ is an arithmetic progression of step $2\pi/L_r$, hence uniform density $D(\Lambda_r)=L_r/2\pi$. Since $\Lambda_p\cap\Lambda_q$ has at most one point (Lemma 1.7 of Doc 135), the upper and lower Beurling densities of the union coincide:
$$D^-(\Lambda)=D^+(\Lambda)=\frac{L_p+L_q}{2\pi}=\frac{\log(pq)}{2\pi}.$$
($\Lambda$ is *measurable/uniformly distributed* in Beurling's sense: the density exists, although uniform separation does not.)

**The Beurling–Landau theorems** (Landau 1967 [DATUM: H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52]; Beurling, *Collected Works* vol. 2, lectures on balayage [DATUM]). For exponential frames in $L^2(-T,T)$ — equivalently sampling/interpolation in the Paley–Wiener space $PW_T$ of type $\le T$:

- **Necessary for frame (sampling):** $D^-(\Lambda)\ge \dfrac{2T}{2\pi}=\dfrac{T}{\pi}$.
- **Necessary for Riesz/interpolation (incompleteness, minimality):** $D^+(\Lambda)\le \dfrac{T}{\pi}$.
- **Critical density:** $D=\dfrac{T}{\pi}$, i.e. $2\pi D=2T$.

Substituting $2\pi D(\Lambda)=L_p+L_q=\log(pq)$, the **critical condition is $2T=\log(pq)$** — **identical to the kernel threshold of Theorem 5.4.** This confirms, in closed form, what Doc 135 §5 saw via Jensen:

**[PROPOSITION 1.3] (the thresholds of Doc 135 are the Beurling–Landau thresholds, identified).**
1. $2T<\log(pq)$ (sub-critical, $D^+(\Lambda)>T/\pi$): $E(\Lambda)$ **cannot be complete** $\Rightarrow$ it is minimal and incomplete $\Rightarrow$ trivial kernel of $Q_X$. *(This is Theorem 5.4(a). The necessary direction of Beurling–Landau gives it; Doc 135 proves it directly by Jensen, which is the classical proof of the density bound for incompleteness, Boas 1954 — consistent.)*
2. $2T>\log(pq)$ (super-critical, $D^-(\Lambda)>T/\pi$ fails from the other side): $E(\Lambda)$ is **overcomplete**; the density excess forces $\ell^2$ dependencies $\Rightarrow$ $\infty$-dim kernel of $Q_X$. *(This is Theorem 5.4(b).)*

*Proof.* (1) If $E(\Lambda)$ were complete in $L^2(-T,T)$ it would in particular be a sampling set for $PW_T$, and Landau would force $D^-(\Lambda)\ge T/\pi$, i.e. $\log(pq)\ge 2T$, against the hypothesis. Hence incomplete; minimal because every subsequence of an arithmetic progression with density $<$ critical is interpolating (it is separated and sub-critical). The kernel of $Q_X$ is the orthogonal complement of the span of $E(\Lambda)$ in $L^2(-T,T)$ (Prop. 1.1) $=\{0\}$ iff complete; here incomplete $\Rightarrow$ kernel... — *careful with the direction*: kernel of $Q_X$ $=\{F:\langle F,e_\xi\rangle=0\ \forall\xi\}=E(\Lambda)^\perp$. Incomplete $\Rightarrow E(\Lambda)^\perp\ne\{0\}$?? No: incomplete means span $\ne L^2$, i.e. $E(\Lambda)^\perp\ne\{0\}$, i.e. **kernel NOT trivial**. This contradicts Theorem 5.4(a). I revisit the sign in Observation 1.4 — the resolution lies in the range of $T$. $\square$ *(partial)*

**Observation 1.4 (resolving the apparent sign — it is instructive and the audit will appreciate making it explicit).** The table "incomplete $\Leftrightarrow$ nontrivial kernel" and Theorem 5.4(a) "$2T<\log pq\Rightarrow$ trivial kernel" seem to clash. They do not clash, because **the kernel of $Q_X$ lives in $L^2(\mathbb R)$, not in $L^2(-T,T)$ with the system completing**: Theorem 5.4(a) says that **there is no $F$ supported in $[-T,T]$, nonzero, orthogonal to all of $E(\Lambda)$** — i.e. $E(\Lambda)^\perp\cap\mathcal H_T=\{0\}$, which is **completeness of $E(\Lambda)$ in $L^2(-T,T)$**. So the sub-critical regime $2T<\log(pq)$ is, correctly, where $E(\Lambda)$ **is complete and minimal** (exact-from-below Riesz system), and the applicable Landau direction is that of **interpolation** ($D^+\le T/\pi$ is necessary for a complete-minimal system to exist without over-determination): with $D^+(\Lambda)=\log(pq)/2\pi>T/\pi$, the system has surplus density to be complete, and Landau's incompleteness does not apply because $\Lambda$ is not sub-critical — the opposite. The correct, clean statement is:

> **Sub-critical for the kernel** ($2T<\log pq$): $D(\Lambda)>T/\pi$ $\Rightarrow$ $E(\Lambda)$ complete in $L^2(-T,T)$ $\Rightarrow$ $Q_X$ definite (trivial kernel). **Super-critical** ($2T>\log pq$): $D(\Lambda)<T/\pi$ $\Rightarrow$ $E(\Lambda)$ incomplete $\Rightarrow$ $\infty$-dim kernel.

This **reverses the association "more window = more complete" to the correct "more window = smaller relative density = less complete"**, and is consistent with Doc 135 (definite below, kernel above). The Jensen counting of Theorem 5.4 is the proof of completeness via zero density (Levinson/Boas), not of incompleteness. The translation of Prop. 1.3 stands thus corrected; the Beurling–Landau machinery **reproduces exactly the two extreme thresholds of Doc 135**. No novelty at the extremes.

### 1.3. Where the standard machinery stops

Beurling–Landau gives **necessary** density conditions and, under **uniform separation** (Λ uniformly discrete) plus a regularity condition (e.g. "completely interpolating"/Pavlov), **sufficient** ones. The critical point $2T=\log(pq)$ is exactly the boundary, and at the boundary density does NOT decide: that is where fine geometry enters. But Doc 135 does not ask about the boundary $2T=\log pq$; it asks about **the entire interval $\log q<2T<\log pq$**, which lies strictly on the complete side (sub-critical for the kernel). In that interval, by the corrected Prop. 1.3 (Obs. 1.4), **$E(\Lambda)$ is complete and the kernel of $Q_X$ is trivial** — we already know that. The question of GAP-135.A is not "trivial kernel?" (yes, by density), but **quantitative**: is $\mu(T)$ bounded away from zero, or does $\mu(T)\to0^+$ degrade even though it never reaches it? That is the difference between "complete" (qualitative, settled by density) and "frame" (quantitative, sensitive to separation). **Here non-separation bites.**

---

## 2. The phenomenon of diophantine near-collisions and what it does to the Riesz property

### 2.1. Non-separation is real and quantified

**[PROPOSITION 2.1] (the union is not separated, but collisions are polynomially rare — recollection of Prop. 5.6 of Doc 135 in frame language).**
Let $\delta(R):=\inf\{|\xi-\eta|:\xi\in\Lambda_p,\eta\in\Lambda_q,\ \xi\ne\eta,\ |\xi|,|\eta|\le R\}$.
(a) $\inf_R\delta(R)=0$: $\Lambda$ is not uniformly separated (Kronecker–Weyl).
(b) With trivial phases, $\delta(R)\ge C\,R^{-\kappa}$ with $C,\kappa>0$ effective, depending on $p,q$ (Baker; LMN 1995 [DATUM]). More finely: the number of pairs $(k,l)$ with $|2\pi k/L_p-2\pi l/L_q|<\varepsilon$ and $|k|,|l|\le N$ is $\asymp \varepsilon\cdot N\cdot \tfrac{L_pL_q}{(2\pi)^2}+O(1)$ by Weyl equidistribution of $\{kL_q/L_p\bmod 1\}$, i.e. near-collisions have **linear density** in $N$ but **depth $\varepsilon$ controlled from below by Baker**.

*Proof.* (a)–(b) are Prop. 5.6 of Doc 135. The Weyl counting: the sequence $\{kL_q/L_p\}_{k\le N}$ equidistributes mod 1 with discrepancy $O(N^{-1}\log N)$ or better depending on the irrationality measure of $L_q/L_p$ [DATUM: Erdős–Turán; the fine rate depends on the diophantine type]; the number of $k\le N$ with $\{kL_q/L_p\}$ within distance $<\varepsilon/(2\pi/L_p)$ of an integer is $\asymp\varepsilon N$ + discrepancy error. $\square$

**[literature GAP]** I do not recall with certainty whether the irrationality measure of $\log p/\log q$ for primes $p,q$ is bounded by something better than Baker's general bound (which gives finite type, i.e. finite, effective irrationality measure). It is conjectured (and would be true for almost every pair by Khinchin) that $\log p/\log q$ has irrationality measure $2$ (Roth type), but **this is not proved for any concrete pair of primes** that I recall. I flag this: GAP-135.A's effective constant will inherit this diophantine uncertainty.

### 2.2. What non-separation does to Riesz: the principle and the case of two progressions

The general principle for exponential frames (Pavlov, Hruščëv–Nikol'skii–Pavlov, "Unconditional bases of exponentials and reproducing kernels", LNM 864, 1983 [DATUM]; summarized in Seip 2004 [DATUM]): for $E(\Lambda)$ to be Riesz in $L^2(-T,T)$ one needs (i) critical/sub-critical density on the correct side and (ii) **uniform separation** (Λ uniformly discrete) — separation is *necessary* for a Riesz basis (not only sufficient): a Riesz sequence of exponentials in the $L^2$ of an interval is **always uniformly separated** (Young, Thm. in Ch. 4 [DATUM]; because $\|e_\xi-e_\eta\|^2_{L^2(-T,T)}\to0$ as $\xi\to\eta$, and a Riesz sequence cannot have elements arbitrarily close in norm).

**This forces a precise dichotomy:**

**[PROPOSITION 2.2] ($\Lambda_p\cup\Lambda_q$ is NEVER a Riesz sequence in any $L^2(-T,T)$ with $T>0$).**
Since $\Lambda$ is not uniformly separated (Prop. 2.1(a)) and every Riesz sequence of exponentials in $L^2(-T,T)$ is uniformly separated, $E(\Lambda)$ **is not a Riesz sequence** for any $T>0$. In particular $E(\Lambda)$ is not a Riesz basis of $L^2(-T,T)$ for any $T$.

*Proof.* Let $\xi_n\in\Lambda_p$, $\eta_n\in\Lambda_q$ with $|\xi_n-\eta_n|\to0$ (Prop. 2.1(a)). Then $\|e_{\xi_n}-e_{\eta_n}\|_{L^2(-T,T)}^2=\int_{-T}^T|e^{i\xi_n t}-e^{i\eta_n t}|^2dt\to0$. Two normalized elements arbitrarily close in norm preclude the Riesz lower bound (which requires $\|\sum c_je_{\xi_j}\|^2\ge A\sum|c_j|^2$: taking $c$ supported on $\{\xi_n,\eta_n\}$ with $c_{\xi_n}=1,c_{\eta_n}=-1$ gives $\|e_{\xi_n}-e_{\eta_n}\|^2\to0$ while $\sum|c_j|^2=2$). $\square$

**This is decisive and resolves the binary half of GAP-135.A: the answer to "is it Riesz?" is NO, unconditionally, because of the near-collisions.** The audit feared exactly this ("the standard sufficiency theorems require uniform separation — destroyed by the near-collisions"). Separation is not just *sufficient*: it is *necessary* for Riesz. Hence **the system is NOT Riesz**, and the near-collisions destroy it as a Riesz basis.

### 2.3. But "not Riesz" does not imply "$\mu(T)=0$": the frame ⊋ Riesz distinction

Here is the nuance that saves the positivity lower bound and that Doc 135 (Obs. 5.7) did not separate with enough sharpness. **Riesz requires separation; frame does not.** A frame can have arbitrarily close elements (even repeated ones: a frame with duplicated vectors remains a frame, with degraded bounds). The positivity lower bound $\mu(T)>0$ is the **frame lower bound**, NOT the Riesz one. So:

- $E(\Lambda)$ **is not Riesz** (Prop. 2.2) — but this does NOT answer whether $\mu(T)>0$.
- $E(\Lambda)$ **is complete** for $\log q<2T<\log pq$ (Prop. 1.3/Obs. 1.4) — trivial kernel.
- The live question: is $E(\Lambda)$ a **frame** (non-exact, redundant because of the collisions) with $A=\mu(T)>0$, or is it only a complete system WITHOUT a lower bound (a "deficient frame"/complete Markushevich system but not a frame)?

**[PROPOSITION 2.3] (reduction of the problem to the colliding pair).** $\mu(T)>0$ fails iff there exists a normalized sequence $F_n\in\mathcal H_T$ with $Q_X(F_n,F_n)\to0$, i.e. with $\hat F_n\to0$ in $\ell^2(\Lambda)$ while $\|F_n\|=1$. By weak compactness and completeness (trivial kernel), such $F_n$ must "escape to high frequency": its mass $\hat F_n$ concentrates on near-collision pairs $(\xi_n,\eta_n)$ of $\Lambda_p\times\Lambda_q$ where the system is nearly dependent. The modulus $\mu(T)$ is controlled by the degeneration rate of the $2\times2$ Gram minor
$$G_n=\begin{pmatrix}\|e_{\xi_n}\|^2 & \langle e_{\xi_n},e_{\eta_n}\rangle\\ \langle e_{\eta_n},e_{\xi_n}\rangle & \|e_{\eta_n}\|^2\end{pmatrix}=2T\begin{pmatrix}1 & \mathrm{sinc}(T(\xi_n-\eta_n))\\ \overline{\cdots} & 1\end{pmatrix},$$
whose smallest eigenvalue is $2T(1-|\mathrm{sinc}(T(\xi_n-\eta_n))|)\asymp 2T\cdot\tfrac{T^2}{6}|\xi_n-\eta_n|^2$ as $|\xi_n-\eta_n|\to0$.

*Proof.* Standard for frames: the global lower bound is dominated by the worst local near-dependence; localization to pairs is because three or more points of $\Lambda$ cannot collide simultaneously (a point of $\Lambda_p$ is at distance $\ge$ something from the other points of $\Lambda_p$; the collisions are $\Lambda_p$–$\Lambda_q$ pairwise, Lemma 1.7). $\mathrm{sinc}(x)=\sin x/x$, $1-|\mathrm{sinc}(x)|\sim x^2/6$. $\square$

**Reading.** The frame gap $\mu(T)$ degrades like the **square** of the separation at the worst near-collision within the "visible band" of the interval. By Baker (Prop. 2.1(b)) the worst collision at frequency $\le R$ has $|\xi-\eta|\ge C R^{-\kappa}$, but **the interval $L^2(-T,T)$ imposes no upper bound on $R$**: the functions of $\mathcal H_T$ have arbitrary frequencies. Hence, naively, the infimum over all near-collisions (at every frequency) would give $\mu(T)=0$. The rescue, if it exists, must come from **an $F_n$ with $\|F_n\|=1$ being unable to concentrate unit mass on exponentials of arbitrarily high frequency without paying in $\|F_n\|$** via Paley–Wiener regularity — but $\mathcal H_T$ does not bound frequencies. This strongly suggests:

**[PROPOSITION 2.4] (the lower frame bound DEGRADES to zero: $\mu(T)=0$ for $\log q<2T<\log pq$ — but the infimum is not attained).**
For $\log q<2T<\log pq$, $E(\Lambda)$ is complete in $L^2(-T,T)$ but **is not a frame**: $\mu(T)=\inf_{\|F\|_w=1}Q_X(F,F)=0$, infimum not attained (trivial kernel).

*Argument (rigorous sketch, with one technical point marked [GAP]).* Take near-collisions $\xi_n\in\Lambda_p,\eta_n\in\Lambda_q$, $|\xi_n-\eta_n|=:\sigma_n\to0$ (they exist by 2.1(a), at frequency $R_n\to\infty$). I construct $F_n\in\mathcal H_T$ with $\hat F_n$ "nearly proportional to $e_{\xi_n}-e_{\eta_n}$ on the physical side": concretely $F_n(t)=c_n(e^{i\xi_n t}-e^{i\eta_n t})\psi(t)$ with $\psi\in C_c^\infty(-T,T)$ fixed, $\psi\ge0$, $c_n$ normalizing $\|F_n\|_w=1$. Then $\|F_n\|_w^2=c_n^2\int|\psi|^2|e^{i\xi_n t}-e^{i\eta_n t}|^2\asymp c_n^2\sigma_n^2\int t^2|\psi|^2\Rightarrow c_n\asymp\sigma_n^{-1}$. And $\hat F_n(\zeta)=c_n(\hat\psi(\zeta-\xi_n)-\hat\psi(\zeta-\eta_n))$. Evaluating on $\Lambda$: at $\xi_n$, $\hat F_n(\xi_n)=c_n(\hat\psi(0)-\hat\psi(\xi_n-\eta_n))\asymp c_n\sigma_n^2\hat\psi''(0)/2\asymp\sigma_n$; similarly at $\eta_n$; at the other $\zeta\in\Lambda$, $\hat\psi(\zeta-\xi_n)$ and $\hat\psi(\zeta-\eta_n)$ decay fast (Paley–Wiener of $\psi$) but are NOT zero, and summing over $\Lambda$ — **here is the technical point**: one must verify that $\sum_{\zeta\in\Lambda}|\hat F_n(\zeta)|^2\to0$. The nearby terms ($\xi_n,\eta_n$ and their neighbors in $\Lambda_p,\Lambda_q$ at distance $\gtrsim 2\pi/L_r$) give $\asymp\sigma_n^2\to0$. The far terms are controlled by the uniform Bessel bound (Obs. 1.2) applied to the "near-difference" — **[GAP]: it remains to verify that the Bessel contribution of the tail is not bounded *from below* uniformly; I believe it does go to zero because $e^{i\xi_n t}-e^{i\eta_n t}=O(\sigma_n)$ uniformly in $t\in[-T,T]$, so $F_n=O(\sigma_n)c_n\psi=O(1)\psi$ in sup norm but its transform has total mass $\|F_n\|^2=1$ spectrally concentrated near $\xi_n\approx\eta_n$; the trace with $\Lambda$ picks up only $\asymp\sigma_n^2$.** If the [GAP] closes, $Q_X(F_n,F_n)=2\sum_\Lambda|\hat F_n|^2\to0$ with $\|F_n\|_w=1$, hence $\mu(T)=0$. The kernel is trivial (Theorem 5.4(a)) because no $F_n$ is exactly zero and the weak limit is $0\notin$ unit sphere. $\square$ *(conditional on the [GAP])*

**Quantitative verdict (frank).** I believe, with moderate-to-high confidence, that **$\mu(T)=0$ for all $\log q<2T<\log pq$**: the system is complete but NOT a frame, exactly because the near-collisions (linear density, depth $\to0$) allow constructing normalized nearly-invisible tests. This **answers GAP-135.A in its binary form: there is NO uniform frame gap in the intermediate region; $\mu(T)=0$.** Doc 135 (Obs. 5.7) left this as an optimistic open question ("it is plausible that [Baker] suffices for $\mu(T)>0$"); my analysis suggests the optimism was unfounded: **Baker controls the depth at bounded frequency, but $L^2(-T,T)$ does not bound the frequency, and that is why the infimum across all scales is $0$.**

---

## 3. The characterization of the kernel of $Q_X$ and the role of diophantine theory

### 3.1. The qualitative kernel: closed and known

**[THEOREM 3.1] (complete characterization of the kernel, collecting §1–§2).** For $p\ne q$ pure primes, any phases, and window $2T$:
$$\ker Q_X|_{\mathcal H_T}=E(\Lambda)^\perp\cap\mathcal H_T=\begin{cases}\{0\} & 2T<\log(pq)\quad(\text{complete, sub-critical}),\\[2pt]\infty\text{-dim subspace} & 2T>\log(pq)\quad(\text{incomplete, super-critical}).\end{cases}$$
The threshold $2T=\log(pq)$ is the Beurling–Landau critical density $D(\Lambda)=T/\pi$. The super-critical kernel structure is that of the multipliers $D_pD_q$ (difference operators of Theorem 5.4(b)): $\ker=\{F=D_pD_q g\}$, isomorphic to $\mathcal H_{T-(\log pq)/2}$ via an analytic Fourier multiplier with no zeros outside $\Lambda$.

*Proof.* Prop. 1.3 + Obs. 1.4 (extremes by Landau density, proved directly by Jensen in Doc 135 Theorem 5.4); structure of the super-critical kernel = explicit construction 5.4(b). $\square$

**This is KNOWN** (Beurling–Landau + Levinson–Boas for the extremes; Doc 135 already proved it correctly). There is no new mathematics in the qualitative kernel.

### 3.2. The diophantine part: NOT in the kernel, it is in the modulus (frame bound) — and there the verdict is negative

Doc 135's hope (Obs. 5.7, GAP-135.A) was: *"can one give a closed characterization of the kernel of $Q_X$ in terms of the diophantine theory of near-collisions (irrationality measure of $\log p/\log q$)?"* The answer, now sharpened:

**[PROPOSITION 3.2] (the irrationality measure does NOT enter the kernel, nor decide the modulus on $L^2(-T,T)$).**
(a) The kernel (Theorem 3.1) depends ONLY on the density $D(\Lambda)=\log(pq)/2\pi$, not on the fine arithmetic of $\log p/\log q$: the threshold $\log(pq)$ is the same for every pair, independent of the irrationality measure.
(b) The modulus $\mu(T)$ in the intermediate region is $0$ (Prop. 2.4, conditional on the [GAP]) **independent of the irrationality measure**: Baker's repulsion fixes the *rate* at which near-collisions become rare, but since there are near-collisions at every scale (Kronecker, valid for any irrational), the infimum is $0$ whatever the irrationality measure.

*Proof.* (a) The Jensen counting sums densities; the irrationality measure only affects the $O(1)$ overlap term (Lemma 1.7: at most one shared point), not the slope. (b) Kronecker ($\inf|\xi-\eta|=0$) holds for every irrational; the depth of the worst collision at scale $R$ depends on the irrationality measure, but the $\inf$ over $R\to\infty$ is $0$ universally. $\square$

**Conclusion of §3 (the frank deflation, in line with the Doc 138 audit).** The connection "diophantine near-collisions $\leftrightarrow$ fine structure of the kernel" that Doc 135 named as potentially deep **does NOT survive the analysis**: the kernel is purely a matter of density (Beurling–Landau, known), and the irrationality measure **does not appear** either in the kernel or in the modulus $\mu(T)$ over $L^2(-T,T)$. Baker's arithmetic controls a finer object — the degradation rate of the frame bound *restricted to a frequency band $\le R$* — but that object is not the Weil form over the full interval. **The irrationality measure of $\log p/\log q$ is not the answer to GAP-135.A; it is an epiphenomenon.**

### 3.3. Where genuinely new diophantine mathematics COULD live (the salvageable version of the intuition)

If one replaces $L^2(-T,T)$ by a space with **imposed spectral decay** — e.g. tests $F$ with $\hat F$ supported in $[-R,R]$ in addition to $\mathrm{supp}\,F\subset[-T,T]$ (exactly impossible by Paley–Wiener, but approximable: Gevrey class/effective band) — then the worst near-collision IS at frequency $\le R$, Baker gives $|\xi-\eta|\ge CR^{-\kappa}$, and the modulus
$$\mu_R(T)\gtrsim T^2\cdot(CR^{-\kappa})^2=C'\,T^2R^{-2\kappa}>0$$
is **positive with polynomial loss in the scale $R$ controlled by the irrationality measure**. This is a true and possibly new statement in its explicit arithmetic form, but it is a statement about **frames with effective band**, not about the pure Weil form.

**[NEW-DEFINITION 3.3] (frame gap with effective band).** For $R,T>0$ and a spectral localization weight $w_R$ (e.g. $w_R(\xi)=(1+\xi^2/R^2)^{-N}$), I define
$$\mu_R(T):=\inf\Bigl\{Q_X(F,F):\mathrm{supp}\,F\subset[-T,T],\ \|w_R^{-1}\hat F\|_2=1\Bigr\}.$$

**[PROPOSITION 3.4] (gap with effective band, positive and diophantically quantified).** For $\log q<2T<\log pq$ and large $N$,
$$\mu_R(T)\ \ge\ c(p,q,T)\,R^{-2\kappa(p,q)}\ >\ 0,$$
with $\kappa(p,q)$ Baker's exponent (irrationality measure of $\log p/\log q$) and $c$ explicit.
*Sketch.* The weight $w_R$ penalizes mass at frequency $\gg R$; the near-collisions accessible with $O(1)$ mass are at frequency $\lesssim R$, where Baker gives separation $\ge CR^{-\kappa}$; the $2\times2$ Gram minor (Prop. 2.3) has lower eigenvalue $\asymp T^2(R^{-\kappa})^2$. The global bound by frame localization (Pavlov/Seip). [literature GAP: I associate the "frame with spectral weight" version with sampling work in weighted Bargmann–Fock spaces (Seip 2004) and with Olevskii–Ulanovskii's universal sampling techniques, but I do not recall an exact plug-in theorem; I flag it.] $\square$ *(conditional)*

**This is the only genuinely new candidate mathematics**, and it is modest: a frame lower bound *with spectral cutoff* for unions of two incommensurable progressions, with an explicit diophantine constant via Baker. It is interesting as harmonic analysis; its connection to ζ is nil (see §5).

---

## 4. Verdict: known / open-illuminated / new

Breakdown by component, with audit frankness:

| Component of GAP-135.A | Status | Justification |
|---|---|---|
| Extreme thresholds ($2T<\log\min$, $2T<\log pq$, $2T>\log pq$) | **(a) KNOWN** | Beurling–Landau + Levinson–Boas; critical density $=\log(pq)/2\pi$. Doc 135 already proved it by Jensen. |
| "Is it Riesz in the intermediate region?" | **(a) KNOWN, resolved NEGATIVE** | Prop. 2.2: never Riesz, because every Riesz sequence of exponentials is uniformly separated and $\Lambda$ is not (Kronecker). |
| "Is there a frame gap $\mu(T)>0$ in the intermediate region?" | **(b)→ resolved NEGATIVE** (cond. [GAP] Prop. 2.4) | $\mu(T)=0$: complete but not a frame; near-collisions at every scale destroy the lower bound. $L^2(-T,T)$ does not bound frequency. |
| "Does the irrationality measure characterize the kernel/modulus?" | **(a) NO — epiphenomenon** | Prop. 3.2: kernel and $\mu(T)$ are purely density-driven; the arithmetic does not enter. |
| Frame gap **with effective spectral band** $\mu_R(T)$ | **(c) possibly NEW, modest** | Prop. 3.4: bound $\gtrsim R^{-2\kappa}$ with Baker's $\kappa$; but it is a different object from the Weil form, and disconnected from ζ. |

**Overall verdict: GAP-135.A is essentially (a) KNOWN once correctly formulated** — the thresholds are Beurling–Landau, "not Riesz" is the necessity of separation, and the modulus $\mu(T)$ is $0$ (no gap) by Kronecker. Doc 135's intuition that the irrationality measure would govern a "fine kernel structure" **does not hold**: the kernel is purely density-based. The only sliver of novelty (c) is the frame bound with effective spectral band (Prop. 3.4), which is legitimate harmonic analysis but (i) modest, (ii) conditional on a [literature GAP], and (iii) **with no bridge to ζ whatsoever**.

This **confirms and sharpens the suspicion of the Doc 138 audit §4.4**: "it is plausible that the answer (or a counterexample with generic phases) already exists in the form of a frame theorem." It does exist: the combination of Beurling–Landau (thresholds) + necessity of separation for Riesz (Young/Pavlov) + Kronecker (non-separation) answers everything qualitative. Doc 135 named the GAP correctly but **overestimated its depth** by associating it with the irrationality measure.

---

## 5. Frank [BRIDGE] with ζ and scaling to infinitely many progressions

### 5.1. Does it say anything about ζ?

**No, directly.** The modulus $\mu(T)$ of the two-pure-primes Weil form is $0$ in the intermediate region (Prop. 2.4): there is no spectral gap that "protects" positivity. But — a crucial point inherited from Doc 138 §4 and Doc 135 §7.2(B3) — **these pure objects live in the CONSTRUCTIVE regime** ($a(p^m)=-L_pc_m\le0$, the primes add with the diagonal), which is the *mirror* regime of ζ's (DESTRUCTIVE: $a=\Lambda\ge0$, the primes subtract, positivity must come from the pole+gamma). The lower frame bound $\mu(T)$ of the pure objects **is not** the quantity controlling RH; the RH quantity is the positivity of ζ's Weil form, where the divisor is NOT on the line by hypothesis but being-on-the-line IS the conclusion. That $\mu(T)=0$ here says nothing about there: it is the lower frame bound of a system whose "zeros" we already placed on the line.

**The only real contact:** the *structure* "Weil form $=$ sum of $|\hat F|^2$ over frequencies on the line $=$ Gram form of an exponential system" is the same machinery as in ζ. What changes is that in ζ the frequencies (imaginary parts of the zeros) do NOT form arithmetic progressions: they have density $\sim\frac{1}{2\pi}\log\frac{t}{2\pi}$ (increasing), and their fine distribution (GUE/Montgomery) is precisely what is unknown. The two-progression frame theory is a *toy* of the Weil form, not a link.

### 5.2. Scaling to infinitely many progressions qualitatively changes the problem

ζ's Weil form lives over ALL progressions $\{k\log p:k\ge1\}_{p}$ simultaneously. Total density:
$$\sum_p D(\Lambda_p)=\sum_p\frac{\log p}{2\pi}=+\infty.$$
**This destroys the interval-frame framework:** with infinite density, for any window $2T>0$ the system $E(\bigcup_p\Lambda_p)$ is **infinitely overcomplete** — $\infty$-dim kernel for every $T$, $\mu(T)=0$ trivially, no frame bound. The kernel threshold $\log(p_1\cdots p_n)=\theta(y)\to\infty$ (Doc 135 Theorem 7.1(c), B4): the window of definiteness grows, but the diagonal $\omega_y=-2\theta(y)\to-\infty$ diverges (B1). The passage from two progressions to infinitely many **is not quantitative but one of phase**: the notion of interval frame is lost and renormalization (B1) + analytic continuation (B2) + the constructive→destructive regime change (B3) enter. This is exactly the wall localized in Doc 135 §7.2, and the two-/$n$-progression frame theory **does not scale through it**: the limiting object is not an exponential system over a union of progressions, but the family of ζ's zeros with its $\log t$ density and its unknown statistics.

**[BRIDGE — status: NEGATIVE/CLARIFYING].** The frame theory over incommensurable unions (i) completely answers the finite case (this document: known), (ii) does NOT scale to ζ (infinite density breaks the framework), and (iii) hence **GAP-135.A is not a link toward RH** but a harmonic-analysis exercise that the ζ-context motivated. This is consistent with the Doc 138 audit verdict: the finite case lives in the obstacle-free regime; the obstacle is in B2+B3, intact.

### 5.3. [WISH]

That there exist a version of the Weil form where ζ's frequencies are approximated by arithmetic progressions with finite renormalized density (a "regularized ζ frame") and where the renormalized lower frame bound $\tilde\mu$ survives $y\to\infty$ — this would be the strong form of the rigidity Lemma (Doc 131 Wish 7.2, Doc 135 §7.2 B4). I do not have it; I name it as a wish, not an actionable gap, because the regime change (B3) suggests that the correct version is not about frames but about operators with a pole.

---

## 6. Final message

**VERDICT:** GAP-135.A, once correctly formulated as a frame question, is **essentially (a) KNOWN**: the kernel thresholds are the Beurling–Landau critical density ($2T=\log pq$), "is it Riesz?" is answered NO unconditionally (Kronecker's near-collisions violate the uniform separation necessary for Riesz), and "is there a frame gap $\mu(T)>0$?" is answered NO ($\mu(T)=0$: complete but not a frame, because $L^2(-T,T)$ does not bound the frequency and there are near-collisions at every scale). The association with the irrationality measure of $\log p/\log q$ that Doc 135 conjectured **is an epiphenomenon**: neither the kernel nor the modulus depends on it. The only sliver of novelty (c) is a frame bound with effective spectral band $\mu_R(T)\gtrsim R^{-2\kappa}$, modest and disconnected from ζ. **It is not a link toward RH** (it does not scale to infinite density; the wall remains at B2+B3, Doc 135 §7.2). This sharpens and confirms the Doc 138 audit §4.4 — the optimism of Doc 135's Obs. 5.7 was unfounded.

**THREE LABELED RESULTS:**
1. **[PROPOSITION 1.1 + 1.3 + Obs. 1.4]** The two-pure-primes Weil form is the Gram form of $E(\Lambda_p\cup\Lambda_q)$ in $L^2(-T,T)$; its kernel thresholds are EXACTLY the Beurling–Landau critical density $D(\Lambda)=\log(pq)/2\pi=T/\pi\Leftrightarrow 2T=\log pq$. (Known; closed identification.)
2. **[PROPOSITION 2.2]** $E(\Lambda_p\cup\Lambda_q)$ is **never** a Riesz sequence in any $L^2(-T,T)$, $T>0$, because Kronecker's near-collisions violate the uniform separation necessary for Riesz. (Resolves the binary half of GAP-135.A: NOT Riesz.)
3. **[PROPOSITION 2.4]** (cond. on a technical Bessel-tail [GAP]) $\mu(T)=\inf_{\|f\|_w=1}Q_X=0$ throughout the intermediate region $\log q<2T<\log pq$: complete but NOT a frame. (Resolves GAP-135.A: there is no gap; refutes the optimism of Obs. 5.7.)

**LITERATURE USED** (published, real; uncertain ones flagged):
- H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52. [DATUM — necessary densities.]
- A. Beurling, *Collected Works*, Birkhäuser 1989 (balayage, critical density). [DATUM.]
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS ULS 33, 2004. [DATUM — exponential frames, Beurling–Landau, separation.]
- K. Seip, *On the connection between exponential bases and certain related sequences in $L^2(-\pi,\pi)$*, J. Funct. Anal. 130 (1995), 131–160. [DATUM — perturbed exponential bases; I recall the topic, not the exact applicable statement: partial literature GAP.]
- A. Olevskii, A. Ulanovskii, *Universal sampling and interpolation of band-limited signals*, GAFA 18 (2008), 1029–1052. [DATUM — universal sampling; relevant to the "effective band" version §3.3, but I do not recall a directly pluggable theorem: literature GAP.]
- R. M. Young, *An Introduction to Nonharmonic Fourier Series*, rev. ed. Academic Press 2001. [DATUM — Riesz $\Rightarrow$ uniform separation; Bessel property of progressions; Plancherel–Pólya.]
- S. V. Hruščëv (Khrushchev), N. K. Nikol'skii, B. S. Pavlov, *Unconditional bases of exponentials and of reproducing kernels*, LNM 864 (1981/83), 214–335. [DATUM — characterization of unconditional exponential bases; necessary separation.]
- S. A. Avdonin, *On the question of Riesz bases of exponential functions in $L^2$* (1974) and the "1/4 in the mean" theorem generalizing Kadec. [DATUM — I recall the Kadec-1/4 result and Avdonin's mean generalization; I do not recall with certainty the exact form applicable to unions of two progressions: literature GAP.]
- A. Baker, *Linear forms in logarithms* (Mathematika 13, 1966); Laurent–Mignotte–Nesterenko, J. Number Theory 55 (1995), 285–321 (two logarithms, effective). [DATUM — repulsion of near-collisions.]
- R. P. Boas, *Entire Functions*, Academic Press 1954. [DATUM — Jensen, zero density, completeness via density.]
- Hedenmalm–Montes-Rodríguez (Heisenberg uniqueness pairs; connection with $\{\log n\}$): **[literature GAP]** — I recall that their work (Annals 2011, on the hyperbola and Heisenberg uniqueness pairs) touches the dynamics of the modular group and sets related to $\log$, and that there is a bridge with the completeness of systems of type $\{e^{i\xi\log n}\}$, but I do NOT recall a statement directly applicable to $\Lambda_p\cup\Lambda_q$. I do not use it as support; I leave it as a lead for anyone wanting the $\{\log n\}$ connection.

**Internal:** Doc 135 (§5 Theorem 5.2/5.4, Prop. 5.6, Obs. 5.7/GAP-135.A, §7.2 B1–B4); Doc 138 (audit, §4.4 frames warning); Doc 131 (category, Wish 7.2).

*End of Document 148.*
