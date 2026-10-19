# Document 193 — Adversarial audit of Document 191 (the universal floor of the mollified moment)

**Program:** Riemann Hypothesis — Phase 59 (full closure)
**Mandate:** decide whether [THEOREM 191.A] should be published. Full reconstruction from scratch BEFORE rereading the proof; attack on the normalization, the novelty, the uniformity range, and the satellite propositions. No numerics; backward-only.

---

## 0. Executive verdict

**CERTIFIED-PUBLISHABLE (with a bounded literature reservation and two repairable errata).**

- The proof of [THEOREM 191.A] **reconstructs cleanly**: the six steps (i)–(vi) close, with a drafting gap in (iv) (one must invoke the Montgomery–Vaughan generalized Hilbert inequality IN ITS WEIGHTED FORM, not the simple form; the declared final error is the correct one) — erratum E-193.3, repairable in five lines.
- **The normalization is the same as in [PROP 180.3]**: verified against the D180 text (hypothesis (M) uses $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt$, with no $\log T$ factor; D191's $c(\theta)$ in §Coordinates is exactly D180's mean$(0)$). The seal [COR 191.B] follows, BUT its sentence about the rate ("$a\le2(1-\theta)$ from below") is miscalibrated and the correct justification is different (erratum E-193.1, the corollary survives with a rewritten proof).
- **Consistency with known truth:** $1+\log\frac{1-\theta}\theta\le1+\frac1\theta$ always ($\log x<x$), trivial at $\theta=\tfrac12$, non-trivial at $\theta<\tfrac12$ — consistent as a strict lower bound of the BCHB/Farmer value. No contradiction.
- **Novelty:** the fine point of attack 3 resolves IN FAVOR of the document, with an important nuance (§3): the "folklore diagonal bound $c\ge1/\theta$" is **NOT immediate** — the naive path dies because the truncated $\zeta\varphi$ has length $TX>T$ and the mean value loses the main term; the BCHB+minimization path would give more but is not written for general coefficients (this is exactly [GAP-191.L1], which the document declares). The publishable contribution is **the bridge, not the rate**.
- **Impact on R1: barrier #2 becomes a THEOREM at $\theta<\tfrac12$** (after repairing E-193.1). The "hard-range" status on $[\tfrac12,1]$ is confirmed.

Errata: E-193.1 (substantive, Cor 191.B), E-193.2, E-193.3, E-193.4 (minor). No statement refuted.

---

## 1. Attack 1: independent reconstruction of the proof of 191.A

I reconstructed the proof before rereading §2.2, over the expected skeleton of the mandate. Step-by-step result:

### 1.1. The skeleton and where it could die

$F=\zeta\varphi(\tfrac12+it)$, $G=F-1$, test $D=\sum_{X<p\le Y}p^{-1/2-it}$ with $Y=T^{1-\theta-\eta}$. Three possible death points: (a) the Hardy–Littlewood approximation error contaminating the bilinear form; (b) the extraction of the diagonal in $\int F_0\overline D$ when $F_0$ has length $TX\gg T$; (c) the passage from $\int|G|^2$ to $\int|F|^2$ (first moment). I check all three.

**(a) Hardy–Littlewood correctors — CLOSES.** Titchmarsh Thm 4.11 with $x=T$: valid for $\sigma>0$, $|t|\le 2\pi x/C$ — the range $1\le t\le T$ is inside. $|F-F_0|\ll(T^{1/2}/t+T^{-1/2})|\varphi|$. Against $D$: $\int_1^T\frac{T^{1/2}}t\,X^{1/2+o(1)}\,Y^{1/2}\,dt\ll T^{1/2}X^{1/2}Y^{1/2}(\log T)^{B}=T^{(1+\theta+1-\theta-\eta)/2}(\log T)^B=T^{1-\eta/2}(\log T)^B$. Divided by $T$: $\ll T^{-\eta/2}(\log T)^B$, and with $\eta\ge C_0\frac{\log\log T}{\log T}$ this is $(\log T)^{B-C_0/2}=o(1)$ choosing $C_0>2B+2$. ✓ The segment $t\le1$: $|FD|\ll X^{1/2}Y^{1/2}(\log T)^{B}\ll T^{(1-\eta)/2}$, more than enough (the document's bound $T^{1/2+\theta}$ is another valid majorant but derived worse — E-193.2). ✓

**(b) The diagonal of the bilinear form — CLOSES, with MV's weighted form (E-193.3).** This was the candidate killer. $\int_0^TF_0\overline D\,dt$ with frequencies $\log N$ ($N\le TX$) against $\log p$ ($p\in(X,Y]$). The terms $N=p$ give EXACTLY $T\cdot\alpha_p/p$ (integrating $1$). The terms $N\ne k$: $\sum_{N\ne k}\frac{\alpha_N N^{-1/2}\,k^{-1/2}}{i\log(N/k)}(e^{i\cdot}-1)$-type; the minimum spacing of $\{\log N\}$ at $N\asymp M$ is $\asymp1/M$, so the simple Hilbert form (with a global $\delta^{-1}\asymp TX$) does NOT suffice. The one that closes is the **weighted generalized** inequality (Montgomery–Vaughan 1974, Cor. 2): $\big|\sum_{N\ne k}\frac{a_N\bar b_k}{\log(N/k)}\big|\ll\big(\sum_N|a_N|^2\delta_N^{-1}\big)^{1/2}\big(\sum_k|b_k|^2\delta_k^{-1}\big)^{1/2}$ with $\delta_N\asymp1/N$. With $a_N=\alpha_NN^{-1/2}$: $\sum|\alpha_N|^2N^{-1}\cdot N=\sum_{N\le TX}|\alpha_N|^2\ll TX(\log T)^{B_3}$ (divisor-bounded ✓, since $|\alpha_N|\le\sum_{n|N}|b_n|\le d_{\kappa+1}(N)(\log T)^{A_0}$ ✓). With $b_k=p^{-1/2}$: $\sum_p p^{-1}\cdot p=\pi(Y)\ll Y/\log Y$. Total error $\ll(TX)^{1/2}Y^{1/2}(\log T)^{B}=T^{1-\eta/2}(\log T)^B$ — **exactly the error the document declares in (iv)**. The proof is correct; the writing omits that the weighted form is needed (the citation "(1974)" covers it, but a referee will ask for it). The $-1$ term against $D$: frequency $0$ against $\log p\ge\log X$, large gap, contribution $\ll\sum_pp^{-1/2}/\log p\ll Y^{1/2}$, harmless. ✓
**Crucial:** $\alpha_p=\sum_{n|p,n\le X,p/n\le T}b_n=b_1=1$ for $X<p\le Y$ (the divisor $n=p$ exceeds the support; $p\le Y\le T$ ✓) — [LEMMA 191.1] applied to the truncated version is also correct, not only to the ideal $1*b$. ✓

**(c) From the square of $G$ to the moment — CLOSES.** $\frac1T\int|F|^2=1+\frac2T\mathrm{Re}\int G+\frac1T\int|G|^2$; the first moment: the sum $\frac1T\sum_{2\le N\le TX}|\alpha_N|N^{-1/2}/\log N\ll T^{-1}(TX)^{1/2}(\log T)^B=T^{(\theta-1)/2}(\log T)^B=o(1)$ with power saving for $\theta<1$ ✓ (here the sum of $|\alpha_N|N^{-1/2}$ is bounded by Cauchy–Schwarz against $\sum N^{-1}\cdot$length, same order). Correctors likewise. ✓

**(d) Denominator and assembly.** MV mean value: $\frac1T\int|D|^2=\sum_{X<p\le Y}\frac1p(1+O(p/T))$, and $\sup_p p/T\le Y/T=T^{-\theta-\eta}$ — the term $O(p/T)$ PER TERM (the mandate's concern) is uniformly $o(1)$, it does not even need to be summed carefully. ✓ Cauchy–Schwarz: $\frac1T\int|G|^2\ge\frac{(\mathcal P-O(T^{-\eta/2}(\log T)^B))^2}{\mathcal P(1+o(1))}=\mathcal P-o(1)$ as long as $\mathcal P\gg(\log T)^{-C_0/3}$ — guaranteed since $\mathcal P\ge2\delta\ge2C_0\frac{\log\log T}{\log T}$. ✓ Mertens: $\mathcal P=\log\frac{(1-\theta-\eta)}{\theta}+O(1/(\theta\log T))$, error absorbed in the declared range. ✓ The internal check "$\log\frac{1-\theta-\delta}\theta\ge2\delta$ for $\theta\le\tfrac12-\delta$": $(1-\theta-\delta)/\theta\ge\frac{1/2}{1/2-\delta}=\frac1{1-2\delta}$, $\log\frac1{1-2\delta}\ge2\delta$ ✓ correct.

**Conclusion of attack 1: the proof SURVIVES.** The step where it "could die" (the bilinear form with $F_0$ of length $TX>T$) is resolved precisely because the test $D$ is short and the shared diagonal lives only in the primes $(X,Y]$; the document handles the error of the approximate equation correctly. The choice $x=T$ (not the symmetric approximate functional equation) is the right one: it avoids the $\chi$ part entirely at the cost of length $TX$, which the weighted Hilbert form tolerates.

### 1.2. Can the composite diagonal compensate negatively?

Not applicable: the proof never uses the full diagonal $\sum|A_n|^2/n$ (which for length $TX>T$ does not even dominate the moment); it uses Cauchy–Schwarz, which is insensitive to the sign of the remainder. The restriction to primes is legitimate as a lower bound of $\int|G|^2\ge|\langle G,D\rangle|^2/\|D\|^2$ with no additional positivity hypothesis. ✓

---

## 2. Attack 2: normalization and the chain 191.A ⟹ 191.B ⟹ barrier

**Verified against the D180 §1.4 text.** [PROP 180.3] hypothesis (M): $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt\le1+(c-1)e^{-as\log T}$; conclusion $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}$. The $c$ of (M) at $s=0$ is $\frac1T\int|\zeta\varphi(\tfrac12+it)|^2dt$ — **identical to D191's $c(\theta)$ in §Coordinates**. No $\log T$ factor in either, no weight discrepancy. The comparison with the industry also matches: BCHB/Conrey/Farmer state $\frac1T\int|\zeta\psi|^2\sim1+\frac1\theta$ in that same normalization. ✓

**The real weak point is in [COR 191.B], not in the normalization — E-193.1 (substantive erratum).** The corollary claims that the shifted version of 191.A gives mean$(s)-1\ge\sum_{X<p\le Y}p^{-1-2s}-o(1)$ "which reproduces form (M) with rate $a\le2(1-\theta)$ from below." Two problems:

1. **The rate is misread.** $\sum_{X<p\le Y}p^{-1-2s}$ is dominated for large $s$ by the LOWER end $p\asymp X$: it decays like $X^{-2s}=e^{-2\theta s\log T}$, not like $e^{-2(1-\theta)s\log T}$. The correct restriction on any majorant (M) is $a\lesssim2\theta$ (stronger than the one stated; the stated one is a weak consequence for $\theta<\tfrac12$, hence it is not false, but the direct-substitution proof as written does not establish it, because…
2. **…the errors erode the restriction for large $s$.** The $-o(1)$ of the shifted version (size $(\log T)^{-C_0/3}$) exceeds $\sum p^{-1-2s}$ as soon as $s\gtrsim\frac{\log\log T}{\theta\log T}\cdot C$, so the floor only constrains (M) in a WINDOW $s\lesssim C'/\log T$-loglog-scale. **The corollary's conclusion survives via the correct argument, which is simpler:** at $s\asymp1/\log T$ the floor persists with value $\asymp\mathcal P\ge\delta$ (the errors are uniform and only improve for $s>0$, as the document correctly notes), hence (M) forces $(c-1)e^{-O(a)}\ge\delta$, i.e. $c-1\ge\delta e^{-O(a)}$, and therefore $\frac{c-1}{a}\gg\delta\cdot\frac{e^{-O(a)}}a\gg\delta$ for $a=O(1)$, while $a\gg1$ requires $c-1\ge\delta e^{ca}$ — the ratio $(c-1)/a$ grows. In both regimes $(c-1)/a\gg\delta$: **gaining a log is impossible for $\theta<\tfrac12$, q.e.d. for the corollary with the repaired proof.** The statement of 191.B stands as a THEOREM; the sentence about the rate must be rewritten (version ready in §7).

---

## 3. Attack 3: novelty — is the diagonal bound $1/\theta$ folklore?

This was the attack designed to downgrade the document to folklore. **It fails, and understanding why it fails pins down the exact contribution.**

**(a) The "naive diagonal" path does NOT exist.** The temptation: $\int_0^T|\zeta\varphi|^2\approx T\sum_n|(1*b)(n)|^2/n$ (diagonal), and the minimum of the diagonal form $\sum_{n\le T}((1*b)(n))^2/n$ with $b_1=1$, support $[1,T^\theta]$, is a classical dual-Selberg-sieve-type calculation (Iwaniec–Kowalski; completing the square via Möbius inversion) with answer $\asymp\log T/\log X=1/\theta$. **But the first step is false as an unconditional lower bound:** the truncated $\zeta\varphi$ frankly has length $TX>T$, and the mean value theorem gives $\sum|A_n|^2(T+O(n))$ where the term $O(n)$ for $n\asymp TX$ EXCEEDS $T$ and has no sign — the diagonal does not dominate, there is no free lower bound. The classical diagonal problem produces a heuristic, not a theorem. The missing piece is exactly what 191.A constructs: a functional (the short prime test) that extracts a forced portion of the diagonal unconditionally within the bilinear range $XY\le T^{1-\eta}$.

**(b) The "BCHB + minimization" path.** BCHB 1985 evaluate the moment for general divisor-bounded coefficients at $\theta<\tfrac12$; minimizing their explicit quadratic form over general coefficients would presumably give $1+\frac1\theta$ — a STRONGER bound than 191.A. **But:** (i) that minimization over ARBITRARY coefficients (not the smooth variational class) is not located anywhere in writing — it is precisely [GAP-191.L1], which the document candidly declares; (ii) even if it existed, it would require fixed $\theta\le\tfrac12-\varepsilon$ (BCHB's errors are not stated with uniformity up to $\tfrac12-C\frac{\log\log T}{\log T}$), whereas 191.A reaches the corner; (iii) the shifted version in $s$ (the one the barrier NEEDS via (M)) is also not in BCHB in the required form, and in 191.A it comes for free.

**Novelty verdict:** the RATE $\log\frac{1-\theta}\theta$ is suboptimal and no one should cite it as the true floor; the THEOREM (unconditional lower bound over the full divisor-bounded class, elementary, uniform up to the corner, with shifted version) **is not in the literature I know of** (Farmer 1993 does a variational calculation over its class, not universal lower bounds; Goldston–Gonek treat minima of forms with $\Lambda,\mu$ in sibling problems, not this moment; Bettin–Gonek treat consequences of $\theta=\infty$, not floors). The pre-publication obligation is the 191.L1 search as the document already mandates — the residual folklore risk concentrates on whether some expert wrote down observation (a)+(prime test); it is a two-page observation and could have appeared as an auxiliary lemma in the proportions literature. **Risk: moderate-low. The document's novelty claim is defensible as formulated (with its declared GAP).**

---

## 4. Attack 4: uniformity and the $o(1)$

All errors are explicit in the proof: $T^{-\eta/2}(\log T)^{B}$ (bilinear and correctors), $O(Y/T)$ (denominator), $O(1/(\theta\log T))$ (Mertens), $T^{(\theta-1)/2}(\log T)^B$ (first moment). With $\eta\ge C_0\frac{\log\log T}{\log T}$, the worst is $(\log T)^{B-C_0/2}$; $C_0(\kappa,A_0)>3B+3$ suffices and the dependence $B=B(\kappa,A_0)$ is traceable ($B_3$ comes from $\sum d_{\kappa+1}(N)^2\ll x(\log x)^{(\kappa+1)^2-1}$ plus $(\log T)^{2A_0}$). The statement "$e^{-\eta\log T/3}(\log T)^B$" of the theorem is consistent with the sum of the errors. The heading of §0 (and of the external summary) states "$1+\log\frac{1-\theta}\theta-o(1)$" suppressing $\eta$ — legitimate because $\eta$ can be taken as $C_0\frac{\log\log T}{\log T}=o(1)$, but the formal theorem should be stated with $\eta$ or in the form "$c(\theta)-1\ge\delta$" (E-193.4, cosmetic). **Uniformity: CORRECT and explicit.**

---

## 5. Attack 5: [PROP 191.C] and [PROP 191.D]

**[PROP 191.C] — CERTIFIED.** With $b_n=0$ on $(1,T^\alpha]$, [LEMMA 191.1] gives $A_p=1+b_p=1$ for ALL $p\le T^\alpha$ in addition to $p>X$. Test $D=\sum_{1<p\le T^\alpha}p^{-1/2-it}$: length $T^\alpha\le Y$, bilinear condition $XT^\alpha\le T^{\theta+\alpha}\le T^{1-\eta}$ ✓ (with $\alpha\le1-\theta-\eta$, which the range $\alpha<\theta<\tfrac12$ guarantees). $\mathcal P=\sum_{p\le T^\alpha}1/p=\log\log T^\alpha+O(1)=\log(\alpha\log T)+O(1)$ ✓. The error remains a small power of log, negligible against $\mathcal P\to\infty$. One nuance: for extremely small $\alpha$ ($T^\alpha$ bounded) $\mathcal P$ stops diverging — the statement implicitly assumes fixed $\alpha$ or $\alpha\log T\to\infty$; this should be stated (included in E-193.4). The reading ("every unmollified prime costs $1/p$") is exact.

**[PROP 191.D] — CERTIFIED as a trivial conditional.** Given (TW$_y$), the proof of 191.A repeats with $Y=T^{y-\varepsilon}$; the only step that used $XY\le T^{1-\eta}$ was (iv), replaced by the hypothesis. Correct. Auditor's remark: (TW$_y$) as stated already INCLUDES control of the Hardy–Littlewood correctors (it is stated for $\zeta\varphi$, not for $F_0$) — well formulated. The calibration of §3.2 (the frontier is one of range, not of arithmetic) is faithful to the proof's structure: correct, and it is the document's most valuable conceptual observation.

---

## 6. Errata

- **E-193.1 (substantive, [COR 191.B]).** The sentence "reproduces exactly form (M) with rate $a\le2(1-\theta)$ FROM BELOW" is doubly miscalibrated: the decay rate of the floor is $2\theta$ (endpoint $p\asymp X$), not $2(1-\theta)$; and direct substitution does not establish a restriction on $a$ for large $s$ because the error $o(1)$ exceeds the floor outside a window $s=O(\log\log T/\log T)$. **Repair (included here, §2):** use only the persistence of the floor at $s\asymp1/\log T$, which forces $(c-1)e^{-O(a)}\ge\delta$ and hence $(c-1)/a\gg\delta$ in all regimes of $a$. The CONCLUSION of the corollary (barrier = theorem at $\theta<\tfrac12$, impossible to gain a log) stands proved with this repair.
- **E-193.2 (minor, step (i)).** The bound on the segment $t\le1$ "$\ll T^{1/2+\theta}$ (convexity)": the natural bound is $\ll X^{1/2}Y^{1/2}(\log T)^B=T^{(1-\eta)/2}$; the written one is valid as a majorant only if $|D|\ll Y^{1/2}$ and $|\zeta|\ll1$ for $t\le1$ are justified, and even then the correct exponent is different. Harmless (both are absorbed).
- **E-193.3 (minor but mandatory for a referee, step (iv)).** The diagonal extraction requires the WEIGHTED generalized Hilbert inequality of MV 1974 (weights $\delta_N^{-1}\asymp N$ offset by the $N^{-1/2}$ of the coefficients); the document cites the correct paper but does not display the computation $\sum|\alpha_NN^{-1/2}|^2\delta_N^{-1}=\sum|\alpha_N|^2$. Five lines; the declared final error is already correct.
- **E-193.4 (cosmetic).** (a) The §0 headline omits $\eta$; state the formal theorem with $\eta$ or in the form "$\theta\le\tfrac12-\delta\Rightarrow c-1\ge\delta$". (b) 191.C: add the hypothesis $\alpha\log T\to\infty$. (c) In the statement of 191.A the range of $\eta$ appears with a broken sentence ("…more precisely"); formalize it.

---

## 7. Statement ready for the paper (auditor's version)

**Theorem.** *Let $\kappa\in\mathbb N$, $A_0>0$. There exists $C_0=C_0(\kappa,A_0)$ such that: for all large $T$, all $\delta$ with $C_0\frac{\log\log T}{\log T}\le\delta\le\tfrac12$, all $\theta\le\tfrac12-\delta$ and every Dirichlet polynomial $\varphi(s)=\sum_{n\le T^\theta}b_nn^{-s}$ with $b_1=1$ and $|b_n|\le d_\kappa(n)(\log T)^{A_0}$, one has*
$$\frac1T\int_0^T\big|\zeta\varphi(\tfrac12+it)\big|^2\,dt\;\ge\;1+\log\frac{1-\theta-\delta}{\theta}-\delta\;\ge\;1+\delta.$$
*More generally, for $0\le s\le\tfrac12$: $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt\ge1+\sum_{T^\theta<p\le T^{1-\theta-\delta}}p^{-1-2s}-\delta$. The bound requires no multiplicativity, sign, or any structure of $b$.*

Mechanism to highlight in the introduction: $(1*b)(p)=1$ for every prime outside the support (convolution rigidity) + short test on primes via Cauchy–Schwarz within the Montgomery–Vaughan bilinear range; explicitly point out that the rate $\log\frac{1-\theta}\theta$ is below the conjectural $\frac1\theta$ and why (the test only sees the tail primes). Mandatory citations and comparison: BCHB 1985 (evaluation, not a universal lower bound), Farmer 1993 (conjectural optimality), MV 1974 (weighted form). Prerequisite: close [GAP-191.L1] with a real literature search.

## 8. Impact on the architecture

1. **R1: barrier #2 ([PROP 180.3]) is a THEOREM at $\theta<\tfrac12$** over the divisor-bounded class (which exhausts the industry), with [COR 191.B] repaired by E-193.1. The conditional residue at $\theta\in[\tfrac12,1]$ (hard range, (TW$_y$)) remains as D191 calibrates it.
2. The sentence for P49/the program: *the mollifier conduit is closed by theorem in the short range; the only gap is the bilinear range beyond the square root.* The wall's live residue is once again a single one: [GAP-180.1] ($\mu_2=o(1)$).
3. Publication: standalone short note (≈4–6 pp.), conditioned on 191.L1 and on incorporating E-193.1–E-193.4. The value for the external reader is twofold: the universal bound and the exact localization of the frontier $\theta=\tfrac12$ as a RANGE frontier.

**Final verdict: CERTIFIED-PUBLISHABLE.** Exact contribution: the unconditional bridge (convolution rigidity + prime test) that converts the diagonal heuristic into a lower bound over the general class — not the rate, which is suboptimal and must be presented as such.
