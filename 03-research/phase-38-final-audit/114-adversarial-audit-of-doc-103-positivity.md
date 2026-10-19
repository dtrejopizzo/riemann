# Document 114 — Adversarial audit of Doc 103 (positivity of $W_\lambda$ and sharpening of P39)

**Program:** Riemann Hypothesis — Phase 38 (final audit)
**Objects audited:** Doc 103 (Lemma 2.1, Theorem 2.2, Theorem 3.1), Doc 63 §3 and §7, Doc 76 §4, Doc 83 §1, P39 (`06-papers/P39-ccm-trace-criterion/main.tex`, Def. `def:Wlambda`, Thm. `thm:Wpos`, Thm. `thm:main`)

---

## Anticipated verdict

**REFUTED.** The kernel $W_\lambda$ actually defined in Doc 63 §5.2 / P39 Def. `def:Wlambda`,
$$W_\lambda(s) = \sum_{n\,:\,\gamma_n\leq\lambda} (a_n^\infty)^2\bigl(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2\bigr),$$
**is not non-negative**: it takes strictly negative values on open regions of $\mathbb{R}$, for every $\lambda$. The "summed by parts" form of Doc 63 §7.1 / Doc 103 eq. (1) / P39 eq. `eq:abel`,
$$\sum_{n=1}^{N} n\,|\mathcal{P}_n|^2 + (a_N^\infty)^2|\mathcal{P}_{N+1}|^2,$$
**is not equal to $W_\lambda$**: the Abel sum has the sign of the interior term flipped and the lower boundary term omitted, and moreover the coefficient "$n$" is miscomputed (the correct value of the difference of squares is $2n+\tfrac12$, not $n$). Theorem 2.2 of Doc 103 is true *for the polynomial of eq. (1)*, but that polynomial is not $W_\lambda$; applied to the true $W_\lambda$ it is **false**. Theorem 3.1 (sharpening of P39 to a single $\lambda_0$) is left **without support**, and —worse— the direction $(ii)\Rightarrow(i)$ of P39's own main theorem (Thm. `thm:main`), which relies on Thm. `thm:Wpos`, is left **without proof**.

The only statement that survives is Lemma 2.1 (non-simultaneous vanishing of $\mathcal{P}_n,\mathcal{P}_{n+1}$), which is correct classical theory (Szegő). But it shields a theorem about the wrong kernel.

---

## §1. The one-line proof: $W_\lambda$ has zero $dm_\infty$ mean

Before any Abel-sum algebra, there is a structural argument that settles the question. The $\{\mathcal{P}_n\}$ are **orthonormal** with respect to $dm_\infty$: $\int |\mathcal{P}_n|^2\,dm_\infty = 1$ for every $n$. Integrating the definition of $W_\lambda$ term by term:
$$\int_\mathbb{R} W_\lambda(s)\,dm_\infty(s) \;=\; \sum_{n\,:\,\gamma_n\leq\lambda} (a_n^\infty)^2\,\bigl(\,\underbrace{\|\mathcal{P}_{n+1}\|^2_{L^2(dm_\infty)}}_{=1} - \underbrace{\|\mathcal{P}_n\|^2_{L^2(dm_\infty)}}_{=1}\,\bigr) \;=\; 0.$$
**Exactly zero, for every $\lambda$.** A continuous kernel, not identically zero, with zero integral against a measure of support $\mathbb{R}$, **cannot be non-negative**. This refutes in one blow:

- Doc 63, Cor. 7.2 ("$W_\lambda \geq 0$"): **false**.
- P39, Thm. `thm:Wpos` ("$W_\lambda(s)\geq 0$ for every $\lambda,s$"): **false**.
- Doc 103, Theorem 2.2 ("$W_\lambda > 0$ on all of $\mathbb{R}$"): **false** for the true $W_\lambda$.

Note that this very integral is computed in **Doc 76, Prop. 4.1**, which obtains $\widehat{W_\lambda dm_\infty}(0) = \frac{N(N+1)}{2}+(a_N^\infty)^2 > 0$ using the summed-by-parts form. The contradiction $0 \neq \frac{N(N+1)}{2}+(a_N^\infty)^2$ is the internal proof, with the program's own documents, that **the summed-by-parts form is not equal to the definition**. (The entire Doc 76 Fourier series inherits the error.)

---

## §2. Line of attack 1: the identity $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ is arithmetically false

With $a_k^\infty = \tfrac12\sqrt{(2k+1)(2k+2)}$ (the definition used consistently in Doc 63 Prop. 7.1, Doc 103 §1, P39 lines 48, 128, 296):
$$(a_k^\infty)^2 = \frac{(2k+1)(2k+2)}{4} = \frac{4k^2+6k+2}{4}.$$
Then
$$(a_n^\infty)^2-(a_{n-1}^\infty)^2 = \frac{(4n^2+6n+2)-(4n^2-2n)}{4} = \frac{8n+2}{4} = 2n+\tfrac12 \;\neq\; n.$$
- Doc 63, Prop. 7.1 (line 146): claims the difference "$= n$". **False**: it is $2n+\tfrac12$.
- Doc 103, eq. (1) and §1: copies "$(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ (direct computation)". **False**, same error.
- P39, proof of `thm:Wpos` (line 519) and the Remark after: claims $(a_{n+1}^\infty)^2-(a_n^\infty)^2 = n+1$ and that "the differences of its square are exactly the positive integers". **False**: $(a_{n+1}^\infty)^2-(a_n^\infty)^2 = \frac{(4n^2+14n+12)-(4n^2+6n+2)}{4} = \frac{8n+10}{4} = 2n+\tfrac52$.

By itself, this error would be benign ($2n+\tfrac12 > 0$ just as $n > 0$: "miscopied formula, theorem survives"). The sequence that would actually satisfy "differences $=n$" would be $(a_n)^2 = n(n+1)/2$, which is not the CCM. The fatal error is the following.

## §3. Line of attack 2: the Abel sum has the interior sign flipped and omits the lower boundary

Correct Abel summation, with $u_n=(a_n^\infty)^2$, $v_n=|\mathcal{P}_n(s)|^2$, consecutive indices $n_0,\dots,N$:
$$\sum_{n=n_0}^{N} u_n(v_{n+1}-v_n) \;=\; u_N v_{N+1} \;-\; u_{n_0}v_{n_0} \;-\; \sum_{n=n_0+1}^{N}(u_n-u_{n-1})\,v_n.$$
The interior coefficients enter with a **minus sign** (since $u_n$ is increasing, $u_n-u_{n-1}=2n+\tfrac12>0$), and there is a lower boundary term $-u_{n_0}v_{n_0}$ that **is not negligible** ($v_{n_0}=|\mathcal{P}_{n_0}(s)|^2$, and for $n_0=0$, $v_0\equiv 1$).

**Explicit verification with $N=2$** (sum over $n=0,1,2$; $c_n:=u_n$, $b_n:=v_n$):
$$c_0(b_1-b_0)+c_1(b_2-b_1)+c_2(b_3-b_2) = c_2 b_3 - c_0 b_0 + (c_0-c_1)b_1 + (c_1-c_2)b_2,$$
with $(c_0-c_1)<0$, $(c_1-c_2)<0$. The form claimed by Doc 63 §7.1 / Doc 103 (1) is
$$ (c_1-c_0)b_1 + (c_2-c_1)b_2 + c_2 b_3,$$
that is, **the opposite sign in both interior coefficients, and the lower boundary term $-c_0b_0$ removed**. No re-indexing or sign convention for $\kappa_n$ reconciles the two expressions (I tested both orientations $\kappa_n = \pm(a_n)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$: neither produces positive interior coefficients *and* a positive upper boundary at once).

**Doc 63 itself contains the correct version.** Doc 63's Prop. 3.2 (line 60) writes the Abel sum correctly:
$$\sum_{n=0}^N(a_n^\infty)^2\!\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = (a_N^\infty)^2\!\int|\mathcal{P}_{N+1}|^2 - (a_0^\infty)^2\!\int|\mathcal{P}_0|^2 + \sum_{n=0}^{N-1}\bigl[(a_n^\infty)^2-(a_{n+1}^\infty)^2\bigr]\!\int|\mathcal{P}_{n+1}|^2,$$
with interior coefficients $(a_n)^2-(a_{n+1})^2 = -(2n+\tfrac52) < 0$ and boundary
$-(a_0)^2\int|\mathcal{P}_0|^2$. **Doc 63 §7.1 contradicts Doc 63 §3.2.** §3.2 is correct.

**Mechanism of the error in P39.** The proof of `thm:Wpos` (lines 514–525) states the Abel sum with boundary "$-u_{-1}v_0$" (it should be $-u_0v_0$; the trick "$u_{-1}:=0$" illegitimately erases the boundary) and then, when passing to eq. `eq:abel`, transcribes the interior term "$-\sum(u_{n+1}-u_n)v_{n+1}$" as "$+\sum(n+1)|\mathcal{P}_{n+1}|^2$": **two sign/boundary errors plus the arithmetic error of §2, all three in five lines**. This is exactly the pattern of the program's historical errors (Doc 93: sign; Doc 70: sign; Doc 71: omitted block).

**The correct form** (indices $0\dots N$) is:
$$W_\lambda(s) = (a_N^\infty)^2|\mathcal{P}_{N+1}(s)|^2 \;-\; (a_0^\infty)^2 \;-\; \sum_{n=0}^{N-1}\Bigl(2n+\tfrac52\Bigr)|\mathcal{P}_{n+1}(s)|^2.$$

## §4. Explicit counterexample ($N=1$): $W_\lambda$ is negative on a macroscopic interval

With $a_0^\infty=\tfrac{\sqrt2}{2}$, $a_1^\infty=\sqrt3$, $\mathcal{P}_0\equiv1$, $\mathcal{P}_1(s)=\sqrt2\,s$ (recurrence: $s\mathcal{P}_0=a_0\mathcal{P}_1$), $\mathcal{P}_2(s)=\frac{s\mathcal{P}_1-a_0\mathcal{P}_0}{a_1}=\sqrt{\tfrac23}\,(s^2-\tfrac12)$. The definition gives, summing $n=0,1$:
$$W = \tfrac12(2s^2-1) + 3\Bigl(\tfrac23(s^2-\tfrac12)^2 - 2s^2\Bigr) = 2s^4-7s^2 = s^2(2s^2-7).$$
**$W(s)<0$ for every $0<|s|<\sqrt{7/2}\approx 1.87$**; e.g. $W(1)=-5$. Doc 103's form eq. (1) would instead give $1\cdot 2s^2 + 3\cdot\tfrac23(s^2-\tfrac12)^2 = 2s^2+2(s^2-\tfrac12)^2 \geq 0$; at $s=1$ it equals $+\tfrac52$. The two expressions are different polynomials. (Cross-check with the correct form of §3: $3\cdot\tfrac23(s^2-\tfrac12)^2 - \tfrac12 - \tfrac52\cdot 2s^2 = 2s^4-7s^2$ ✓.)

More generally: at any zero $s_0$ of $\mathcal{P}_{N+1}$ (there are $N+1$, all real and simple: Szegő, *Orthogonal Polynomials*, AMS Colloq. Publ. 23, Thm. 3.3.1), the correct form gives
$$W_\lambda(s_0) = -(a_0^\infty)^2 - \sum_{n=0}^{N-1}\Bigl(2n+\tfrac52\Bigr)|\mathcal{P}_{n+1}(s_0)|^2 \;\leq\; -\tfrac12 \;<\;0,$$
with the strict inequality reinforced because $\mathcal{P}_N(s_0)\neq0$ (interlacing). The set $\{W_\lambda<0\}$ is open and nonempty for **every** $N\geq 0$.

## §5. Line of attack 3: the chain of definitions Doc 63 → Doc 76 → P39 → Doc 103

- Doc 63 §5.2 (Prop. 5.2) and P39 Def. `def:Wlambda` define $W_\lambda$ as the sum of $\kappa_n$: **they agree**, and this is the binding definition, because it is the only one for which the integral representation $T_\lambda = \int W_\lambda\,d\nu$ holds (P39 Prop. `prop:integral`), which is what everything else uses. There is no escape by redefining $W_\lambda$ as the positive form: the identity with $T_\lambda$ would be lost.
- Doc 63 §7.1, Doc 76 §4.1 (line 244, with coefficients "$k$") and Doc 103 eq. (1) use the spurious summed-by-parts form: **they agree with one another** (modulo the $n$ vs $n+1$ shift in P39's `eq:abel`, another sign of carelessness), and **all of them differ from the definition**. The error is born in Doc 63 §7.1 and propagated by copying to Doc 76, P39 and Doc 103 without anyone redoing the sum with $N=2$.
- Indexing: P39 sums "$n\geq 0,\ \gamma_n\leq\lambda$" while Doc 63 §7.1 produces the top term $(a_{N(\lambda)})^2|\mathcal{P}_{N(\lambda)+1}|^2$ with $N(\lambda)=\#\{n:\gamma_n\leq\lambda\}$; if the zeros are indexed from $n=0$ the top term should be $(a_{N-1})^2|\mathcal{P}_N|^2$, if from $n=1$ it matches. An off-by-one ambiguity never fixed; irrelevant to the refutation (any consecutive range gives negative interior coefficients), but it must be fixed in the correction.
- On whether this $W_\lambda$ is "the Abel kernel of CCM" (Connes–Consani–Moscovici): I could not verify this against the external source in this offline audit; the name is internal to the program (the weights $(a_n^\infty)^2$ are not Abel weights $e^{-\lambda k}$ nor Cesàro weights $(1-k/N)$). I recommend not attributing the form to CCM in P39 without a specific citation.

## §6. Lines of attack 4 and 7: Lemma 2.1 survives (it is classical)

The measure $dm_\infty$ is even (symmetric under $s\mapsto -s$; cf. Doc 83 §2, parity of $|\zeta(1/2+is)|^2$ and of the $\Gamma$ factor), hence $b_n=0$ and recurrence (2) of Doc 103 is the correct convention. The $\mathcal{P}_n$ have real coefficients, so $|\mathcal{P}_n(s)|^2=\mathcal{P}_n(s)^2$ on $\mathbb{R}$: no problem. The descent argument of Lemma 2.1 is valid as is **for $s_0\in\mathbb{C}$ too** (it only uses the algebraic recurrence and $a_k>0$, $\mathcal{P}_0\equiv1$); the final step uses the recurrence at index $1$ ($s_0\mathcal{P}_1 = a_1\mathcal{P}_2+a_0\mathcal{P}_0$), without needing $\mathcal{P}_{-1}$. Multiplicity is irrelevant (only vanishing is used). This is a standard fact: the zeros of $\mathcal{P}_n$ and $\mathcal{P}_{n+1}$ strictly interlace and in particular do not coincide (Szegő, op. cit., Thm. 3.3.2; also B. Simon, *Szegő's Theorem and Its Descendants*, Princeton, 2011, §1.2, via the Christoffel–Darboux Wronskian $a_n(\mathcal{P}_{n+1}'\mathcal{P}_n-\mathcal{P}_n'\mathcal{P}_{n+1})=\sum_{k\leq n}\mathcal{P}_k^2>0$). **No counterexample is possible** to this lemma for any measure with finite moments: it is structural. Lemma 2.1: **SURVIVES INTACT** — but it is the lock on a door that opens into the wrong room.

## §7. Lines of attack 5 and 6: Doc 83, Doc 89 and convergence (correct but now insufficient)

- **Doc 83, Cor. 1.2**: $|\zeta|^2\geq|\zeta_{on}|^2$ pointwise and unconditional, via the Hadamard-product ratio $\prod_j(1+\delta_j^2/(u-\gamma_j)^2)^{\,\cdot}\geq 1$. The mechanism is sound (each factor $\geq1$; convergence by $\sum\delta_j^2/\gamma_j^2<\infty$); it does not require a normalization that presupposes the zeros. I grant $d\nu\geq0$.
- $|\zeta_{on}|^2>0$ except at isolated zeros: legitimate (a discrete, $dm_\infty$-null set).
- $d\nu=0\iff$RH (Doc 89, cond. 2): legitimate ($R\equiv1$ a.e. forces every $\delta_j=0$ by continuity of the factors).
- Convergence of $T_{\lambda_0}=\int W_{\lambda_0}\,d\nu$: $W_\lambda$ grows polynomially (degree $2N+2$), $dm_\infty$ decays like $e^{-\pi|s|/2}$ (the $\Gamma$ factor) and $|\zeta(1/2+is)|^2$ grows polynomially; the integral converges absolutely. No objection.

But all of this is now insufficient: with $W_{\lambda_0}$ **sign-indefinite**, $T_{\lambda_0}=0$ (and even $T_\lambda=0$ for every $\lambda$) is a priori compatible with $d\nu\neq0$ by cancellation between the regions $\{W>0\}$ and $\{W<0\}$. The step "non-negative integrand $\Rightarrow$ null a.e." of Theorem 3.1 ($\Leftarrow$) loses its hypothesis. **Theorem 3.1: REFUTED in its proof; the statement remains an open conjecture.**

## §8. Collateral damage in P39 and downstream results

1. **P39, Thm. `thm:Wpos`**: false (§1, §4). Must be withdrawn.
2. **P39, Thm. `thm:main`, direction (ii)$\Rightarrow$(iii)**: the proof invokes `thm:Wpos`; it remains invalid. I observe that from $T_\lambda=0\ \forall\lambda$ one does deduce $\Delta_n^{full}=\Delta_n^{full,on}$ term by term (consecutive differences of $T_\lambda$ at the jumps $\lambda=\gamma_n$), that is $\int\kappa_n\,d\nu=0\ \forall n$, i.e. $\int|\mathcal{P}_n|^2 d\nu$ constant in $n$. But **this does not imply $d\nu=0$** without a new argument (a positive measure whose density with respect to $dm_\infty$ is orthogonal to all the $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ is not automatically zero). The criterion RH$\iff T_\lambda=0\ \forall\lambda$ **is not proved** in the direction that matters. The direction RH$\Rightarrow T_\lambda=0$ survives (trivial: $d\nu=0$).
3. **Doc 63, entire §7** (Prop. 7.1, Cor. 7.2, Thm. 7.3, Cor. 7.5): refuted. Caution: Doc 63 §6 (line 122) claims $\Delta_n^{full}-\Delta_n^{full,on}\geq0$ for each $n$ via a sum of Poisson kernels, which contradicts the same document's Obs. 2.2 ("$\kappa_n$ has indefinite sign" + $d\nu\geq0$ ⟹ sign a priori indefinite). That alternative route, if correct, might rescue $T_\lambda\geq0$ without going through $W_\lambda$; **it requires an independent and urgent audit** — it is now the only conceivable support for the criterion.
4. **Doc 76** (Fourier transform of $W_\lambda dm_\infty$): the entire series uses the spurious form; in particular Prop. 4.1 ($\widehat{W_\lambda dm_\infty}(0)>0$) contradicts the exact value $0$ (§1). Refuted as a block; it must be recomputed with the correct form of §3 (where, incidentally, $\widehat{\,\cdot\,}(0)=0$ will come out automatically).
5. **The entirety of Doc 103** except Lemma 2.1; Obs. 2.4 ($N=0$: "$W=(a_0)^2|\mathcal{P}_1|^2$") is also false: the real value is $(a_0)^2(|\mathcal{P}_1|^2-1)=s^2-\tfrac12$, negative near $0$.
6. **P41**: any use of the "collapse of the family $\{T_\lambda\}$ to a point" (Doc 103 §4, Cor. 3.2) must be withdrawn.

## §9. What is salvageable

- $T_\lambda=\int W_\lambda\,d\nu$ with $d\nu\geq0$ (Doc 83) and the correct Abel formula of §3: all of this is solid as an *identity*.
- $\int W_\lambda\,dm_\infty=0$: a new exact identity, free, that any reconstruction must respect.
- Lemma 2.1 / interlacing (Szegő 3.3.1–3.3.2): available for future legitimate uses.
- Possible repair route: prove $T_\lambda>0$ under ¬RH directly from Doc 63 §6 (Poisson), or find weights $w_n>0$ such that $\sum w_n\kappa_n$ is indeed a sum of squares (this would require **decreasing** $w_n$, e.g. of genuine Abel type $w_n=e^{-\lambda n}$: with $u_n$ decreasing the summation by parts gives positive interior coefficients $+(u_{n-1}-u_n)$, a lower boundary $-u_{n_0}v_{n_0}$ still negative — it would need to be absorbed; not trivial but the correct direction if one wants a genuinely positive kernel).

## §10. Table of verdicts

| Statement | Verdict |
|---|---|
| $(a_n^\infty)^2-(a_{n-1}^\infty)^2=n$ (D63 7.1, D103 §1, P39) | **FALSE**: $=2n+\tfrac12$ (and $2n+\tfrac52$ in P39's variant) |
| Summed-by-parts form $=W_\lambda$ (D63 §7.1, D76 §4.1, D103 (1), P39 eq:abel) | **FALSE**: interior sign flipped + boundary $-(a_0)^2|\mathcal{P}_0|^2$ omitted; counterexample $N=1$: $W=s^2(2s^2-7)$ |
| $W_\lambda\geq0$ (D63 Cor 7.2, P39 thm:Wpos) | **REFUTED**: $\int W_\lambda dm_\infty=0$ exact; $W_\lambda<0$ on open sets |
| Lemma 2.1 (D103) | **SURVIVES** (classical: Szegő Thm 3.3.2; descent valid in $\mathbb{C}$) |
| Theorem 2.2 (D103) | **REFUTED** for the true $W_\lambda$ (true only for the spurious kernel) |
| Theorem 3.1 / Cor. 3.2 (D103), sharpened to a single $\lambda_0$ | **REFUTED** (without proof; plausibly false by cancellation) |
| P39 thm:main, (ii)$\Rightarrow$(i) | **WITHOUT PROOF** (real gap: $\int\kappa_n d\nu=0\ \forall n \not\Rightarrow d\nu=0$ without a new argument) |
| $d\nu\geq0$ (D83), $d\nu=0\iff$RH (D89), convergence of $T_{\lambda_0}$ | No objection |

**FINAL VERDICT: REFUTED** — in Doc 63 §7.1 (origin), propagated to Doc 76, P39 (`thm:Wpos` and the key direction of `thm:main`) and Doc 103 (Theorems 2.2 and 3.1). The error is of the same type as those of Docs 70/93/95/97: flipped sign in a summation by parts plus an omitted boundary term, confirmed by a miscomputed arithmetic identity. Internal detection was available: Doc 63 §3.2 already contained the correct Abel sum, and $\int W_\lambda\,dm_\infty=0$ was verifiable in one line.

---

*End of Document 114.*