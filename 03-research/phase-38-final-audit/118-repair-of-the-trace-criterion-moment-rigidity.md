# Document 118 — Repair of the trace criterion: moment rigidity instead of kernel positivity

**Program:** Riemann Hypothesis — Phase 38 (final audit)
**Objective:** post-refutation repair — mandate: repair the central theorem of the CCM framework (P39, Thm. `thm:main`, direction $T_\lambda=0\ \forall\lambda \Rightarrow$ RH) after the refutation of Doc 114, or declare it irreparable with the exact gap.
**Prerequisites:** Doc 114 (refutation of $W_\lambda\geq0$), Doc 63, Doc 83 ($d\nu\geq0$), Doc 89, P39, P40, P43, D72.

---

## Anticipated verdict

**CRITERION REPAIRED** — in its per-index form (the family $\{\int\kappa_n\,d\nu=0\}_{n\geq0}$), with a complete, unconditional proof, and via a new route that **does not use** $W_\lambda\geq0$ nor any Christoffel asymptotic:

$$\boxed{\;\text{RH}\iff \int_{\mathbb{R}}\kappa_n(s)\,d\nu(s)=0\ \ \text{for all } n\geq 0\;}$$

where $\kappa_n=(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$ and $d\nu=dm_{\rm full}-dm_{\rm full,on}\geq0$. The mechanism of the proof is the **rigidity of the Hamburger moment problem**: the Carleman condition for $dm_\infty$ — the same property that *kills* Cor. 1.2 of Doc 63 ($K_n\to\pi/2$ is false) — is exactly what *repairs* the criterion. The only finite positive measure $\nu$ with $\int|\mathcal{P}_n|^2\,d\nu$ constant in $n$ is $\nu=c\,m_\infty$; and $c=0$ follows from Hardy's theorem (critical zeros exist) plus continuity of the densities.

Two caveats remain **declared** (not hidden):

1. **(Blocks)** The literal $\lambda$-form of P39 ("$T_\lambda=0\ \forall\lambda$") only recovers the per-index family when the ordinates $\{\gamma_n\}$ are pairwise distinct. Under ¬RH there are *automatic* coincidences (each pair $\beta+i\gamma,\,1-\beta+i\gamma$ shares an ordinate), so the $\lambda$-form only delivers per-block sums; the implication "$\lambda$-form $\Rightarrow$ RH" remains open (precise gap in §5.6). The per-index form is the correct formulation of the criterion and is the one the CCM chain (P39 item (iii), D72 per-$n$) actually produces.
2. **(Linearized vs. exact)** The repaired object is the *linearized* trace $T_\lambda:=\int W_\lambda\,d\nu$ (the definition that Doc 114 §5 declared binding). The version with exact Jacobi discrepancies, $\Delta_n^{\rm full}=\Delta_n^{\rm full,on}\ \forall n\iff$ RH, is also true — by determinacy of $m_{\rm full}$, and that part of P39 was already essentially correct (§5.7). What this document repairs is the link the audit left without proof: that the *linearized* family also characterizes RH.

---

## §0. What was broken and what is available

Doc 114 proved: $\int W_\lambda\,dm_\infty=0$ exactly, so $W_\lambda$ takes negative values on open sets (at the zeros of $\mathcal{P}_{N+1}$, $W_\lambda\leq-\tfrac12$), and the direction $T_\lambda=0\ \forall\lambda\Rightarrow$ RH of P39 was left without proof. What survives and will be used as input:

- **(I-1)** $d\nu=(|\zeta|^2-|\zeta_{\rm on}|^2)\,dm_\infty\geq0$, unconditional (Doc 83, Cor. 1.2–1.3; ratified by Doc 114 §7).
- **(I-2)** $d\nu=0\iff$ RH (Doc 89 cond. 2 / P39 Prop. `prop:full_measure`; ratified by Doc 114 §7).
- **(I-3)** The binding identity $T_\lambda=\int W_\lambda\,d\nu$ with $W_\lambda=\sum_{\gamma_n\leq\lambda}\kappa_n$ (Doc 114 §5: this is the definition that makes the integral representation valid; it is adopted here as the *definition* of $T_\lambda$).
- **(I-4)** The exact coefficients $a_n^\infty=\tfrac12\sqrt{(2n+1)(2n+2)}$ (CCM, imported axiom; P39 Def. 2.1).
- **(I-5)** The telescoping observation of Doc 114 §8.2: $T_\lambda=0\ \forall\lambda$ (with separated ordinates) $\Rightarrow\int\kappa_n\,d\nu=0\ \forall n\Rightarrow\Delta_n:=\int|\mathcal{P}_n|^2\,d\nu$ constant in $n$.

Fixed notation: $dm_\infty(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}{2})|^2\,ds=:w(s)\,ds$; $\{\mathcal{P}_n\}$ orthonormal with respect to $dm_\infty$ ($\int\mathcal{P}_m\mathcal{P}_n\,dm_\infty=\delta_{mn}$), positive leading coefficient; $\tilde g(s):=|\zeta(\tfrac12+is)|^2-|\zeta_{\rm on}(\tfrac12+is)|^2\geq0$, so that $d\nu=\tilde g\,dm_\infty=\tilde g\,w\,ds$.

---

## §1. Normalizations and a new exact identification

### 1.1. The total mass of $dm_\infty$ (correction to P39)

**Lemma 1.1.** $\displaystyle m_\infty(\mathbb{R})=\int_{\mathbb{R}}dm_\infty=\frac{1}{\sqrt{2\pi}}$, and hence $\mathcal{P}_0\equiv(2\pi)^{1/4}$ (not $\mathcal{P}_0\equiv1$).

*Proof.* Let $f(x)=e^{-e^x}e^{x/4}$. With $u=e^x$, $\widehat f(t)=\int_{\mathbb{R}}f(x)e^{-itx}\,dx=\int_0^\infty e^{-u}u^{1/4-it}\,\tfrac{du}{u}=\Gamma(\tfrac14-it)$. By Parseval ($\int|\widehat f|^2=2\pi\int|f|^2$):
$$\int_{\mathbb{R}}\bigl|\Gamma(\tfrac14+it)\bigr|^2dt=2\pi\int_0^\infty e^{-2u}u^{-1/2}\,du=2\pi\,\Gamma(\tfrac12)\,2^{-1/2}=\pi\sqrt{2\pi}.$$
With $t=s/2$: $m_\infty(\mathbb{R})=(2\pi)^{-2}\cdot 2\cdot\pi\sqrt{2\pi}=(2\pi)^{-1/2}$. Since $\int\mathcal{P}_0^2\,dm_\infty=1$ and $\mathcal{P}_0$ is constant, $\mathcal{P}_0=(2\pi)^{1/4}$. $\square$

**Consistency check.** The same method (Parseval with $f'=(\tfrac14-e^x)f$) gives $\int t^2|\Gamma(\tfrac14+it)|^2dt=2\pi\cdot\tfrac{\sqrt\pi}{8\sqrt2}$, whence $\mu_2/\mu_0=\int s^2dm_\infty/\int dm_\infty=\tfrac12=(a_0^\infty)^2=\tfrac{1\cdot2}{4}$ ✓. P39's claim ("a probability measure") is a harmless normalization error; it does **not** affect the $a_n^\infty$ (invariant under rescaling of the mass), but it does affect the constant in $\Delta_0$: with $\mathcal{P}_0^2=\sqrt{2\pi}$,
$$\Delta_0=\int\mathcal{P}_0^2\,d\nu=\sqrt{2\pi}\;\nu(\mathbb{R}).$$

### 1.2. The $\mathcal{P}_n$ are Meixner–Pollaczek polynomials

**Proposition 1.2 (exact identification).** Let $P_n^{(\lambda)}(x;\phi)$ be the Meixner–Pollaczek family [KLS, §9.7], orthogonal on $\mathbb{R}$ with respect to the weight $e^{(2\phi-\pi)x}|\Gamma(\lambda+ix)|^2$. Then the CCM orthonormals are exactly the Meixner–Pollaczek orthonormals with
$$\lambda=\tfrac14,\qquad \phi=\tfrac{\pi}{2},\qquad x=\tfrac{s}{2}.$$

*Proof.* For $\phi=\pi/2$ the weight is $|\Gamma(\tfrac14+ix)|^2=|\Gamma(\tfrac14+\tfrac{is}{2})|^2$ ✓ (same weight as $dm_\infty$, up to a constant). The Meixner–Pollaczek recurrence at $\phi=\pi/2$ is $(n+1)P_{n+1}=2xP_n-(n+2\lambda-1)P_{n-1}$ [KLS, eq. (9.7.3)]. Passing to the monic form ($k_n=2^n/n!$) gives $x\,\tilde p_n=\tilde p_{n+1}+\tfrac{n(n+2\lambda-1)}{4}\tilde p_{n-1}$, i.e., orthonormal Jacobi coefficients in $x$ coupling $n\leftrightarrow n+1$:
$$a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+2\lambda)}.$$
The CCM recurrence $s\,\mathcal{P}_n=a_n^\infty\mathcal{P}_{n+1}+a_{n-1}^\infty\mathcal{P}_{n-1}$ in the variable $x=s/2$ has coupling $a_n^\infty/2=\tfrac12\sqrt{(n+\tfrac12)(n+1)}$. Equating: $n+2\lambda=n+\tfrac12\iff\lambda=\tfrac14$ ✓, and both families have $b_n=0$ (even measures). Two positive measures with the same Jacobi coefficients and a **determinate** moment problem (Theorem 3.1 below) coincide up to normalization. $\square$

**Remark 1.3.** This identification is new in the program and has two uses: (a) it independently certifies the CCM $a_n^\infty$ against a classical table [KLS]; (b) it makes the asymptotic Meixner–Pollaczek literature available for any future quantitative refinement. It is **not** needed for the central theorem of this document.

---

## §2. Finiteness of $\nu$ and of all its moments

This was the first delicate point flagged in the objective: if $\nu(\mathbb{R})=\infty$, $\Delta_0=\infty$ and the whole scheme collapses. The answer is clean and does not require $N(\sigma,T)$:

**Proposition 2.1 (finiteness of all moments, unconditional).** For every $k\geq0$:
$$\mu_{2k}(\nu):=\int_{\mathbb{R}}s^{2k}\,d\nu(s)\;\leq\;\int_{\mathbb{R}}s^{2k}\,|\zeta(\tfrac12+is)|^2\,dm_\infty(s)\;<\;\infty.$$
In particular $\nu(\mathbb{R})<\infty$ and all integrals $\Delta_n=\int|\mathcal{P}_n|^2d\nu$ are finite.

*Proof.* The first inequality is $0\leq\tilde g\leq|\zeta|^2$ pointwise (Doc 83, Cor. 1.2: $|\zeta_{\rm on}|^2\leq|\zeta|^2$, hence $\tilde g=|\zeta|^2-|\zeta_{\rm on}|^2\leq|\zeta|^2$). For the second: by convexity $|\zeta(\tfrac12+it)|\ll(1+|t|)^{1/4+\varepsilon}$ [Ti86, chap. V] — any polynomial bound suffices — and by Stirling $|\Gamma(\tfrac14+\tfrac{is}{2})|^2\leq C(1+|s|)^{-1/2}e^{-\pi|s|/2}$ [Ti86, §4.42], so the integrand is dominated by $C\,s^{2k}(1+|s|)^{1/2+2\varepsilon}e^{-\pi|s|/2}$, integrable. $\square$

**Remark 2.2.** The argument completely sidesteps the discussion "is $\sum_j\delta_j^2K(\gamma_j)$ finite under ¬RH with infinitely many quadruples?": summing over zeros is unnecessary, because $\tilde g\leq|\zeta|^2$ gives global domination at once. The mass of $\nu$ is finite **regardless** of the configuration of off-critical zeros. (What is *not* finite in general is $\int\tilde g(s)\,ds$ — the mass *without* the weight $w$ —; see §4.3. This distinction is exactly what decides which analytic routes close and which do not.)

**Lemma 2.3 (moment growth and Carleman for the whole family).** With $\mu_{2k}(\sigma)$ the moments of any of the measures $\sigma\in\{m_\infty,\ m_{\rm full},\ m_{\rm full,on},\ \nu\}$:
$$\mu_{2k}(\sigma)\;\leq\;C_\varepsilon\int_0^\infty s^{2k+1/2+2\varepsilon}e^{-\pi s/2}\,ds\;\leq\;C'_\varepsilon\,\Gamma(2k+2)\Bigl(\tfrac{2}{\pi}\Bigr)^{2k},$$
whence $\mu_{2k}(\sigma)^{1/(2k)}\leq C''\,k$ and therefore $\sum_k\mu_{2k}(\sigma)^{-1/(2k)}=\infty$: **all** of these measures satisfy the Carleman condition and their Hamburger moment problems are determinate [Ak65, chap. 2; Si98, §1 and §4].

---

## §3. The Carleman-vs.-Doc-63-Cor.-1.2 tension — resolution

This is the conceptual heart of the matter. The objective flagged an apparent contradiction: Doc 63 Cor. 1.2 claims $K_n(\gamma_n,\gamma_n)\to\pi/2$ (the sum $\sum_k|\mathcal{P}_k(x)|^2$ would *converge*!), while moment theory says that for determinate measures without atoms that sum must diverge. Moment theory wins.

**Theorem 3.1 (determinacy, exact and unconditional).** The moment problem of $dm_\infty$ is determinate. Moreover the Carleman criterion holds in Jacobi form with the exact coefficients:
$$\sum_{n\geq0}\frac{1}{a_n^\infty}=\sum_{n\geq0}\frac{2}{\sqrt{(2n+1)(2n+2)}}\;\geq\;\sum_{n\geq0}\frac{1}{n+1}=\infty,$$
and $\sum 1/a_n=\infty$ implies that the Jacobi matrix is essentially self-adjoint and the problem is determinate [Ak65, chap. 1, Addenda; Si98, Cor. 3.3 and the discussion of the Carleman criterion; Be68].

**Theorem 3.2 ($K_n(x,x)\to\infty$ at every point).** For every fixed $x\in\mathbb{R}$:
$$K_n(x,x)=\sum_{k=0}^{n}\mathcal{P}_k(x)^2\;\longrightarrow\;\infty,\qquad \lambda_n(x)=\frac{1}{K_n(x,x)}\longrightarrow 0.$$

*Proof.* For determinate measures, the Christoffel function converges to the point mass: $\lim_n\lambda_n(x)=\mu(\{x\})$ for every $x\in\mathbb{R}$ [Ak65, chap. 2; Si98, §4: in the determinate case, $\sum_k\mathcal{P}_k(x)^2<\infty$ if and only if $x$ is an eigenvalue of the unique self-adjoint Jacobi operator, i.e. an atom of the spectral measure — and the mass of the atom is $(\sum_k\mathcal{P}_k(x)^2)^{-1}$]. The measure $dm_\infty=w\,ds$ is absolutely continuous, with no atoms; hence $\lambda_n(x)\to0$ and $K_n(x,x)\to\infty$ for **every** $x$. $\square$

**Corollary 3.3 (refutation of Doc 63, Cor. 1.2, and of P39, Prop. `prop:christoffel`).** The claims "$K_n(\gamma_n,\gamma_n)\to\pi/2$" and "$\lambda_n(\gamma_n)\to2/\pi$" are **false**. With them fall:
- P39, Prop. `prop:christoffel` (same statement).
- P39, Cor. `cor:T_positive` (its proof uses "$K_m(s,s)\approx\pi/2$ in the bulk" *and* the spurious `eq:abel` form; doubly invalid).
- The quantitative discussion of the C.P.-O. in Doc 63 §2, insofar as it uses the value $2/\pi$ as a scale (the qualitative conclusion "locality fails" still holds, now with even more reason).

**Diagnosis of the error.** Doc 63 §1 makes two independent errors:
1. It uses the arcsine density $\rho_n^{\rm eq}(s)=\tfrac{n}{\pi a_n\sqrt{1-(s/a_n)^2}}$, which is the equilibrium measure of the interval **with no external field** (the Chebyshev case, or the $\alpha\to\infty$ limit of Freud). For a weight with *linear* exponential decay ($Q(s)\asymp|s|$, "$\alpha=1$"), the correct limiting density is of Ullman type with a **logarithmic singularity at the origin**: for recurrence coefficients with linear growth $a_n\sim cn$, the contracted zero distribution of $\mathcal{P}_n$ is $\int_0^1\omega_{[-2ct,2ct]}\,dt$, whose density at $x$ diverges as $\tfrac{1}{2\pi c}\log\tfrac{1}{|x|}$ as $x\to0$ [KvA99; vA87]. There is no "density $\approx$ constant" in the bulk near the origin.
2. It omits the weight factor in the Christoffel asymptotic: in the regimes where the asymptotic holds, $\lambda_n(x)\approx w(x)/\rho_n(x)$, not $1/\rho_n(x)$ [LL01; Si11, chap. 3; To00].

With both corrected, the prediction consistent with the theory is
$$K_n(x,x)\;\asymp\;\frac{\log n}{w(x)}\cdot C(x)\qquad(x\ \text{fixed},\ n\to\infty),$$
*logarithmic* divergence — consistent with Carleman holding "just barely" ($\sum1/a_n\sim\sum1/n$, logarithmic divergence: the weight $e^{-\pi|s|/2}$ sits exactly at the boundary of determinacy, like $e^{-|x|}$). **[Status: the divergence $K_n\to\infty$ is a theorem (3.2); the $\log n$ rate is the prediction of equilibrium theory via [KvA99] and is not used anywhere below — it is flagged as NOT VERIFIED in the sense that no proof of the rate is given here.]**

**Conclusion of the tension.** There is no indeterminate measure here (that would occur with decay $e^{-|s|^\alpha}$, $\alpha<1$); this is the determinate-boundary case. Doc 63 Cor. 1.2 was the second structural error of that same document (audit 114 had already found that §7.1 contradicts §3.2). The technical irony: **determinacy, which destroys the "Christoffel scale $\pi/2$", is exactly the mechanism that repairs the criterion** (§5).

---

## §4. The analytic route "$\Delta_n\to0$": why it does NOT close as originally proposed

The objective proposed: prove $\Delta_n\to0$ for *any* finite non-negative measure $\nu$, and conclude from $\Delta_n=$ const that the constant is $0$. That route, literally, is **false**, and it is worth recording exactly why — because the way it fails points to the correct repair.

### 4.1. Counterexample to "$\Delta_n\to0$ for every finite measure"

**Observation 4.1.** Take $\nu=m_\infty$ (finite, non-negative, even, with all moments). Then $\Delta_n=\int|\mathcal{P}_n|^2\,dm_\infty=1$ for every $n$: constant and **not** tending to $0$. Hence no theorem of the form "$\nu$ finite $\Rightarrow\int|\mathcal{P}_n|^2d\nu\to0$" can be true, and no Plancherel–Rotach asymptotic can prove it. The mass of $\nu$ can travel together with the effective support of $\mathcal{P}_n$.

### 4.2. What analytic version would actually be true (and why it is not enough)

If the unweighted density $g:=\tilde g=d\nu/(w\,ds)$ were Lebesgue integrable, $g\in L^1(ds)$, and if the supremum bound $\|\mathcal{P}_n^2w\|_{L^\infty(\mathbb{R})}\to0$ held (for Freud weights with $a_n\asymp n$ the Airy-type edge prediction is $\asymp n^{-2/3}$; for the exact Meixner–Pollaczek weight this is plausible but **NOT VERIFIED** in the available literature), then
$$\Delta_n=\int\mathcal{P}_n^2\,w\,g\,ds\leq\|\mathcal{P}_n^2w\|_\infty\|g\|_{L^1}\to0,$$
and the criterion would close by this route *under these two hypotheses*. But:

**Proposition 4.2 ($g\in L^1(ds)$ is not unconditional).** $\int_{\mathbb{R}}\tilde g(s)\,ds<\infty$ holds if the number of off-critical zeros is finite (then, away from the finitely many ordinates, $R-1\asymp C/s^2$ and $\tilde g\ll s^{-3/2+\varepsilon}$), but under ¬RH with infinitely many quadruples the sum of local contributions $\sim\sum_j\delta_j^2\,|\zeta_{\rm on}'(\tfrac12+i\gamma_j)|^2$ is not controlled by any available unconditional bound ($\sum_j\delta_j^2/\gamma_j^2<\infty$ does not give it; nor do the zero densities: almost all zeros could be just barely off the line). In the adversarial scenario, $\int_{|s|\leq T}\tilde g\,ds$ can grow like $T\,{\rm polylog}\,T$.

So the analytic route only gives a **conditional** theorem ("finitely many off-critical zeros are excluded"), with an additional pending technical hypothesis. Recording it has value (§5.6 subsumes it), but it does not repair the criterion.

### 4.3. The clue that does work: the Cesàro identity is *exact*

The Cesàro version of constancy is not an asymptotic but an algebraic identity:
$$\int_{\mathbb{R}}K_n(s,s)\,d\nu(s)=\sum_{k=0}^{n}\Delta_k=(n+1)\,c\qquad\text{if }\Delta_k\equiv c.$$
Nothing needs to be estimated: the question is which measures can satisfy *all* these identities at once. That turns the analytic problem into a **moment** problem — and determinate moment problems have rigidity. This is the observation that closes everything, and it is purely algebraic:

---

## §5. The repaired theorem

### 5.1. Constancy of $\Delta_n$ (telescoping input)

**Lemma 5.1.** If $\int\kappa_n\,d\nu=0$ for every $n\geq0$, then $\Delta_n=\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})=:c$ for every $n$.

*Proof.* $\int\kappa_n\,d\nu=(a_n^\infty)^2(\Delta_{n+1}-\Delta_n)$ and $a_n^\infty>0$. Induction. All integrals are finite by Prop. 2.1. The value of $\Delta_0$ is Lemma 1.1. $\square$

### 5.2. The squares $\{\mathcal{P}_n^2\}$ are a triangular basis of the even polynomials

**Lemma 5.2.** For every $k\geq0$, $\;{\rm span}\{\mathcal{P}_0^2,\mathcal{P}_1^2,\dots,\mathcal{P}_k^2\}=\{\text{even polynomials of degree}\leq2k\}$.

*Proof.* Since $dm_\infty$ is even, $\mathcal{P}_n(-s)=(-1)^n\mathcal{P}_n(s)$ [Sz75, §2.3], so each $\mathcal{P}_n^2$ is an even polynomial, of degree exactly $2n$ (leading coefficient $\kappa_n^2>0$). The $k+1$ polynomials $\mathcal{P}_0^2,\dots,\mathcal{P}_k^2$ have distinct degrees $0,2,\dots,2k$: they are linearly independent in a space of dimension $k+1$, hence they span it, with a triangular change-of-basis matrix. $\square$

### 5.3. Rigidity: constancy identifies $\nu$ with $c\,m_\infty$

**Theorem 5.3 (moment rigidity).** Let $\nu$ be a non-negative, even Borel measure on $\mathbb{R}$, with all moments finite, such that
$$\int_{\mathbb{R}}\mathcal{P}_n(s)^2\,d\nu(s)=c\qquad\text{for every }n\geq0,$$
with $c=\sqrt{2\pi}\,\nu(\mathbb{R})$ as above (in general, $c=\Delta_0$). Then
$$\nu\;=\;c\cdot m_\infty\quad\text{as Borel measures.}$$

*Proof.* (i) *Equality over all polynomials.* By orthonormality, $\int\mathcal{P}_n^2\,dm_\infty=1$ for every $n$; by hypothesis, $\int\mathcal{P}_n^2\,d\nu=c=c\cdot1$. Hence the two measures $\nu$ and $c\,m_\infty$ assign the same integral to each $\mathcal{P}_n^2$, and by linearity and Lemma 5.2, to **every even polynomial**. For odd polynomials both integrals are $0$ (both measures are even; $\nu$ is even because $|\zeta(\tfrac12+is)|^2$ and $|\zeta_{\rm on}(\tfrac12+is)|^2$ are, by the functional equation, and $m_\infty$ is even too). Conclusion: $\mu_j(\nu)=c\,\mu_j(m_\infty)$ for every $j\geq0$.

(ii) *Determinacy.* If $c=0$: $\nu(\mathbb{R})=\mu_0(\nu)=0$, hence $\nu=0=c\,m_\infty$ and we are done. If $c>0$: the sequence $(c\,\mu_j(m_\infty))_j$ satisfies Carleman, since $(c\,\mu_{2k})^{-1/(2k)}=c^{-1/(2k)}\mu_{2k}^{-1/(2k)}$ and $c^{-1/(2k)}\to1$, so it inherits the divergence of $\sum\mu_{2k}^{-1/(2k)}$ (Lemma 2.3). A Carleman sequence is determinate [Ak65; Si98]: it admits a **unique** representing positive measure. Both $\nu$ and $c\,m_\infty$ are positive measures with that moment sequence; hence $\nu=c\,m_\infty$. $\square$

**Remark 5.4 (where the audit's objection gets answered).** Doc 114 §8.2 correctly objected: "a positive measure whose density is orthogonal to all the $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ is not automatically zero". Exactly: it is not zero — it is **proportional to $m_\infty$**. The missing new argument was rigidity 5.3. And note what does the work: the *determinacy* of $m_\infty$ (Carleman with the exact CCM $a_n^\infty$, metaplectic input (I-4)). The non-negativity of $\nu$ (Doc 83) enters in (ii): Carleman uniqueness is for *positive* measures; without $d\nu\geq0$ the step would fail (moment problems are not rigid for signed measures).

### 5.4. The constant is zero: critical zeros exist

**Lemma 5.5 ($c=0$).** If $\nu=c\,m_\infty$ with $\nu=\tilde g\,m_\infty$ and $\tilde g$ continuous, then $\tilde g\equiv c$ on $\mathbb{R}$, and $c=0$.

*Proof.* (i) $\tilde g$ is continuous: $|\zeta(\tfrac12+is)|^2$ is continuous; $\xi_{\rm on}$ is entire (canonical product of genus 1 over the projected zeros $\tfrac12\pm i\gamma_j$, convergent because $\sum_j(\tfrac14+\gamma_j^2)^{-1}<\infty$ [Ti86, §9.6]; cf. Doc 83 §1.1) and the gamma factor $\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)$ does not vanish on the critical line, so $|\zeta_{\rm on}(\tfrac12+is)|^2$ is continuous.

(ii) The two measures $\nu$ and $c\,m_\infty$ are absolutely continuous with continuous Lebesgue densities $\tilde g\,w$ and $c\,w$; equal as measures $\Rightarrow$ equal densities a.e. $\Rightarrow$ equal everywhere (continuity). Since $w(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}{2})|^2>0$ for **every** $s$ ($\Gamma$ has no zeros), it cancels: $\tilde g(s)=c$ for every $s\in\mathbb{R}$.

(iii) By Hardy's theorem [Ha14; Ti86, Thm. 10.2] there exist (infinitely many) zeros of $\zeta$ **on** the critical line; let $\gamma_*$ be the ordinate of one of them. Then $|\zeta(\tfrac12+i\gamma_*)|^2=0$, and also $|\zeta_{\rm on}(\tfrac12+i\gamma_*)|^2=0$ (critical zeros project onto themselves: they are zeros of $\xi_{\rm on}$ by construction). Hence $c=\tilde g(\gamma_*)=0-0=0$. $\square$

### 5.5. The repaired criterion

**Theorem 5.6 (trace criterion, repaired).** With $d\nu=dm_{\rm full}-dm_{\rm full,on}\geq0$ and $\kappa_n=(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$, the following are equivalent:

  (i) RH;
  (ii') $\displaystyle\int_{\mathbb{R}}\kappa_n\,d\nu=0$ for every $n\geq0$;
  (ii'') $\Delta_n=\int|\mathcal{P}_n|^2\,d\nu$ is constant in $n$.

*Proof.* (i)$\Rightarrow$(ii')$\,$: under RH, $\zeta_{\rm on}=\zeta$, $d\nu=0$ (input I-2), all integrals are $0$. (ii')$\iff$(ii''): Lemma 5.1 (and trivially in reverse, multiplying by $(a_n^\infty)^2$). (ii'')$\Rightarrow$(i): by Prop. 2.1 the moments of $\nu$ are finite; $\nu\geq0$ and even; by Theorem 5.3, $\nu=c\,m_\infty$; by Lemma 5.5, $c=0$, hence $\nu=0$; by input (I-2) (Doc 89 / Doc 83: $\tilde g\equiv0\Rightarrow R\equiv1\Rightarrow$ each factor $1+\delta_j^2/(u-\gamma_j)^2\equiv1\Rightarrow\delta_j=0\ \forall j$), RH. $\square$

**What the proof does NOT use.** Neither $W_\lambda\geq0$ (false), nor the spurious Abel form, nor the Christoffel scale (false), nor PPP (generically false), nor locality, nor any asymptotic of $\mathcal{P}_n$. It uses: orthonormality, parity, telescoping, Carleman, Hardy, and $d\nu\geq0$. All inputs are audited or classical.

**Comparison with the original conclusion.** P39 claimed RH $\iff T_\lambda=0\ \forall\lambda$. The repaired criterion has the **same conclusion with the per-index family**, which is the information the jumps of $\{T_\lambda\}_\lambda$ were meant to encode. The exact relation between the two forms is the next caveat.

### 5.6. Caveat 1: the $\lambda$-form and blocks of coincident ordinates

**Proposition 5.7.** Let $T_\lambda:=\int W_\lambda\,d\nu$ (binding definition, input I-3), with $W_\lambda=\sum_{\gamma_n\leq\lambda}\kappa_n$ and $\{\gamma_n\}$ the list of ordinates of the zeros of $\xi$ **with multiplicity**, in non-decreasing order.

(a) If the $\gamma_n$ are pairwise distinct, then $T_\lambda=0\ \forall\lambda\iff$ (ii') $\iff$ RH.

(b) Under ¬RH the $\gamma_n$ are **never** pairwise distinct: every off-critical zero $\rho=\beta+i\gamma$ comes paired with $1-\bar\rho=(1-\beta)+i\gamma$ having the **same** ordinate, so $\gamma$ appears (at least) twice in the list. In that case $T_\lambda=0\ \forall\lambda$ only delivers the block sums
$$\sum_{n\in B_i}(a_n^\infty)^2(\Delta_{n+1}-\Delta_n)=0\qquad\text{for each block }B_i\text{ of equal ordinates},$$
which do not force the constancy of $\Delta_n$ (one free parameter per block).

*Proof.* (a) The jumps of $\lambda\mapsto T_\lambda$ at the distinct points $\gamma$ recover each $\int\kappa_n\,d\nu$ individually; apply Theorem 5.6. (b) Inspection of the functional equation $\xi(s)=\xi(1-s)$ and of the definition of $W_\lambda$: when crossing $\lambda=\gamma$, *all* $n$ in the block enter the sum at once. $\square$

**Declared gap (G-118.1).** The implication "$T_\lambda=0\ \forall\lambda\Rightarrow$ RH" **in the literal $\lambda$-form** remains without proof when there are blocks, i.e., exactly in the ¬RH scenario one wants to exclude. What is obtained in that scenario is: $\Delta_n$ constant except for drifts across blocks, with $\Delta_{n+1}-\Delta_n$ linked within each block by the weights $(a_n^\infty)^2$. Rigidity 5.3 does not apply because the family of annihilated functionals no longer spans all even polynomials (as many dimensions are missing as there are blocks). **Normative recommendation:** state the program's criterion in the per-index form (ii')/(ii'') — which is also the form P39 already listed as item (iii) and the one D72 computes term by term — and treat the $\lambda$-form as a corollary valid under separation of ordinates. No arithmetic content is lost by this change.

### 5.7. Caveat 2: linearized vs. exact

This document repairs the criterion for the **linearized** trace $T_\lambda=\int W_\lambda\,d\nu$, i.e. the family $\int\kappa_n\,d\nu=L_n[\tilde g]$ (P39, Thm. `thm:CD`). The identification of $\int\kappa_n\,d\nu$ with the *exact* Jacobi discrepancy $\Delta_n^{\rm full}-\Delta_n^{\rm full,on}=(a_n^{\rm full})^2-(a_n^{\rm full,on})^2$ is a linearization (first order in the moment perturbation; Doc 63 §3 itself calls it "exact (first order)" — a contradiction in terms worth correcting). For the exact criterion, nothing in this document is needed:

**Remark 5.8 (the exact criterion was already correct).** RH $\iff(a_n^{\rm full})^2=(a_n^{\rm full,on})^2\ \forall n$: the $\Leftarrow$ direction is determinacy of $m_{\rm full}$ and $m_{\rm full,on}$ (both Carleman, Lemma 2.3: two determinate measures with the same Jacobi coefficients and the same mass coincide) plus the Hadamard argument of P39 ((iii)$\Rightarrow$(i), which the audit did not object to); the $\Rightarrow$ direction is trivial. Beware of one fine point: the Jacobi coefficients do not see the total mass; the equality of masses $m_{\rm full}(\mathbb{R})=m_{\rm full,on}(\mathbb{R})$ must be added as an $n=-1$ condition or else normalized — under ¬RH, in fact, $m_{\rm full}(\mathbb{R})>m_{\rm full,on}(\mathbb{R})$ by Doc 83, so the mass condition is already a detector. (This incidentally refutes Lemma 4.1 of Doc 63, which claimed "both measures have the same total mass by construction": false — it contradicts Cor. 1.3 of Doc 83 except under RH. Third internal inconsistency of Doc 63.)

---

## §6. What content the repaired criterion has (and what was spurious)

### 6.1. The trivial collapse the objective anticipated

With the Christoffel–Darboux kernel $K_N(s,s)=\sum_{k\leq N}|\mathcal{P}_k|^2\geq0$ one can define $\widetilde T_N:=\int K_N\,d\nu=\sum_{k\leq N}\Delta_k$. Since each $\Delta_k\geq0$ and $\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})$:
$$\widetilde T_N=0\ \text{for a single }N\iff\nu(\mathbb{R})=0\iff\text{RH}.$$
True — and **trivial**: it is the tautology "$\nu=0\iff$ RH" in disguise, available since Doc 83 with no polynomial at all. If the repair had ended there, the criterion would have died of vacuity. That is not the case:

### 6.2. The non-trivial content of the repaired criterion

1. **Rigidity (Theorem 5.3).** "The only finite positive measure with $\int\mathcal{P}_n^2\,d\nu$ constant is $c\,m_\infty$" is a genuine uniqueness theorem about the moment problem of the CCM measure, which essentially uses the metaplectic input (exact $a_n^\infty$ $\Rightarrow$ exact Carleman). It is not tautological: the family $\{\kappa_n\}$ has zero mean against $dm_\infty$ ($\int W_\lambda\,dm_\infty=0$, Doc 114 §1), so the criterion does not "see" the mass of $\nu$ via positivity — it sees it via **completeness** of the squares $\{\mathcal{P}_n^2\}$ together with determinacy. The indefinite kernel was not a fatal defect but the signal that the correct mechanism was never positivity.
2. **Arithmetic computability (D72).** Each $\int\kappa_n\,d\nu=L_n[\tilde g]$ admits the reading via Weil's explicit formula with test function $h_n=\kappa_n\,w/(a_n^\infty)^2$ (even, more than sufficient decay; the validity of the formula requires no sign of $h_n$). The repaired family is then a family of zero/prime arithmetic identities indexed by $n$ — the content the program was seeking. See §8.3.
3. **No single-index version.** The sharpening of Doc 103 ("a single $\lambda_0$ suffices") is dead and **cannot be revived** via this route: finitely many functionals $\int\kappa_n\,d\nu=0$ are finitely many linear conditions on $\nu$, which non-zero positive measures can satisfy (the $\kappa_n$ are indefinite). Universal quantification over $n$ is essential — consistent with the "master quantifier" of P43: the repaired criterion is once again a quantifier inversion (the whole family, not a finite average).

### 6.3. What was lost

- $T_\lambda\geq0$ and "$T_\lambda\to+\infty$ under ¬RH" (P39 Cor. `cor:T_positive`): lost. Under ¬RH, today only **not all** of the $\int\kappa_n\,d\nu$ are known to vanish; their individual sign is indefinite and there is no quantitative lower bound.
- Any reading of "detecting positivity" (CTP as *positivity*): the repaired invariant detects ¬RH by *non-vanishing*, not by sign.
- The Fourier chain of Doc 76 and the closed kernel of P40/P42 (ledger L6): they inherit the spurious form; they must be recomputed with the correct form of Doc 114 §3 (in particular $\widehat{W_\lambda dm_\infty}(0)=0$).

---

## §7. Audit of the "Poisson route" (Doc 63, §6)

Audit 114 left this route as the "only conceivable alternative support" of $T_\lambda\geq0$. Verdict: **IT FALLS**, for three independent reasons.

1. **Its premise is refuted.** Prop. 6.1 of Doc 63 derives $\Delta_n^{\rm full}-\Delta_n^{\rm full,on}\geq0$ *assuming PPP* ($F_n(z)=c_n/(z-\gamma_n)+R_n$, $c_n>0$). The program itself later proved (D68–D69; P39, Thm. `thm:wronskian` and Cor. `cor:ppp_exact`) that $F_n=-1/(a_n^\infty\mathcal{P}_n\mathcal{P}_{n+1}m_\infty)$ is **holomorphic** at $\gamma_n$ except for an exact coincidence of $\gamma_n$ with a Gauss node: exact PPP is generically false. Premise dead, conclusion unsupported.
2. **The "remainder" was never controlled.** Even granting an asymptotic form of PPP, Prop. 6.1 writes "$=c_n'\,C_\infty(\gamma_n)+\text{remainder}$" without any bound on the remainder; since $C_\infty(\gamma_n)$ can be arbitrarily small (distant off-critical zeros), no sign follows.
3. **Double internal contradiction.** (a) The conclusion "$\Delta_n^{\rm full}-\Delta_n^{\rm full,on}\geq0$ for every $n$" contradicts Obs. 2.2 of the same document ($\kappa_n$ indefinite + $d\nu\geq0$ $\Rightarrow$ term-by-term sign indefinite), as already pointed out by Doc 114 §8.3. (b) Lemma 4.1 of Doc 63 ("same total mass") contradicts Doc 83 (under ¬RH, $\nu(\mathbb{R})>0$): see Obs. 5.8. §6 of Doc 63 must be withdrawn in full.

With this, **no** path toward "$T_\lambda\geq0$" survives in the corpus — and none is needed: Theorem 5.6 replaces positivity with rigidity.

---

## §8. Impact

### 8.1. P39 (`06-papers/P39-ccm-trace-criterion/main.tex`)

| Item | Status post-118 |
|---|---|
| `prop:positivity`, `thm:rate`, `cor:mertens`, `thm:CD`, `rem:oscillation` | Survive (not touched by 114 or 118) |
| `prop:christoffel` ($\lambda_n(\gamma_n)\to2/\pi$, $K_n\to\pi/2$) | **WITHDRAW — FALSE** (Cor. 3.3; new damage detected by this document) |
| `thm:Wpos`, `eq:abel` | WITHDRAW (Doc 114) |
| `thm:main` | **Replace the proof**: (i)$\iff$(iii) via Obs. 5.8 (with the explicit mass condition); (i)$\iff$(ii',ii'') via Theorem 5.6; the $\lambda$-form (ii) only under separation of ordinates (Prop. 5.7, gap G-118.1) |
| `cor:T_positive` (growth $T_\lambda\gtrsim N(\lambda)$) | **WITHDRAW** (depends doubly on false statements) |
| `prop:no_exact_pcn`, `thm:wronskian`, `prop:Fn_closed`, `cor:ppp_exact` | Survive |
| Abstract and "Summary" section: items 5 ($2/\pi$ scale), 7, 8, 10 | Correct/withdraw; item 9 (the equivalence) is kept with the per-index statement and the new proof |
| "dm_∞ is a probability measure" | Correct: $m_\infty(\mathbb{R})=(2\pi)^{-1/2}$ (Lemma 1.1) |

### 8.2. P40 (`P40-three-paths-dnu`)

- **Path I**: $d\nu\geq0$ survives (Doc 83). The bound "$T_\lambda\geq2\sum_j\delta_j^2K_\lambda(\gamma_j)>0$" and every use of $W_\lambda>0$ (abstract; sec1-3 lines 31, 59–60, 82; sec6-7 synthesis theorem, equivalence (2)$\iff$(4) and lines 142–148, 177, 252–255, 485–490): **withdraw**; the equivalence (2)$\iff$(4) of the synthesis theorem can be re-proved with Theorem 5.6 substituting the per-index form for the $\lambda$-form.
- **Path II** (Jensen, $F(z)=\xi(z/(z-1))$): independent of $W_\lambda$; survives.
- **Path III**: the completeness "in $L^2(W_\lambda\,dm_\infty)$" is ill-posed ($W_\lambda\,dm_\infty$ is not a positive measure): reformulate with $|W_\lambda|\,dm_\infty$ or with $K_N\,dm_\infty$; the DBN part ($\Lambda\geq0$ [RT20], $\Lambda=0\iff$ RH) survives.
- The "Hadamard barrier" as a structural conclusion does not change: the repaired criterion still requires knowing $\nu$ (the positions of the zeros) to be evaluated.

### 8.3. D72 (arithmetic formula of the trace)

Weil's explicit formula with $h_\lambda=W_\lambda\,w/\pi$ is an **identity** valid as it stands: Weil's formula requires parity, analyticity in the strip and decay of the test function, **not** positivity. It survives with two changes of status: (a) every sign inference drawn from it is withdrawn; (b) the useful version is now per-index: $h_n=\kappa_n\,w/(a_n^\infty)^2$, an arithmetic identity for each $n$, whose simultaneous vanishing is RH (Theorem 5.6). D72 goes from "formula of a positive invariant" to "arithmetic side of the repaired criterion". Any passage of D72 that used the spurious Abel form of $W_\lambda$ to compute (instead of the definition) must be checked against the correct form of Doc 114 §3.

### 8.4. P43 — ledger L1–L8

- **L1** ($d\nu\geq0$): survives.
- **L2** (single-scale criterion, $W_\lambda>0$ $\Rightarrow$ a single $\lambda_0$ suffices): **DEAD** (Doc 114 + §6.2.3: not revivable). Replace with the repaired criterion: "RH $\iff\int\kappa_n\,d\nu=0\ \forall n$, by moment rigidity" — with an essential universal quantifier, which in fact *reinforces* P43's master-quantifier thesis.
- **L3, L4, L5** (tensor index, tensor-square realization, sub-resolution positivity): independent of $W_\lambda$; unaffected by 114/118 (L3 subject to its own audit, Doc 117).
- **L6** (closed kernel $B_{\lambda_0}$, sech$^{1/2}$): **recompute** — it was derived via the Fourier chain of Doc 76, refuted wholesale (Doc 114 §8.4). Not citable until recomputed.
- **L7** (eight reformulations of $d\nu$, Doc 89 + bridge P35): the reformulations based directly on $d\nu$ survive; those that go through "$T_\lambda=0$ with $W_\lambda>0$" must be referred to Theorem 5.6; P35 independent.
- **L8** (quadruple-density objective): independent; survives.

### 8.5. P44 and others

P44 (two-lemma architecture: $m<\infty$ + sequential LP-112 rigidity) does not use $W_\lambda$ nor $T_\lambda\geq0$: **unaffected**. Positive note for its ledger: Theorem 5.6 is a new unconditional result of the type P44 catalogs (a rigidity that turns a countable family of identities into RH). Doc 103: remains withdrawn in full (except Lemma 2.1). Doc 76: recompute. P41: the uses of the "collapse to a point" remain withdrawn (Doc 114 §8.6) and are not recoverable (§6.2.3).

---

## §9. Final verdict

**CRITERION REPAIRED.**

- The direction audit 114 left without proof is now proved, unconditionally, in the per-index form: $\int\kappa_n\,d\nu=0\ \forall n\Rightarrow\nu=c\,m_\infty$ (moment rigidity, Carleman with the exact CCM $a_n^\infty$) $\Rightarrow c=0$ (Hardy + continuity) $\Rightarrow\nu=0\Rightarrow$ RH. Same conclusion P39 was pursuing, via a new route, without $W_\lambda\geq0$.
- The Carleman-vs.-Doc-63-Cor.-1.2 tension is resolved **against** Doc 63: $dm_\infty$ is determinate ($\sum1/a_n^\infty=\infty$, exact), it is absolutely continuous, hence $K_n(x,x)\to\infty$ at every point; "$K_n(\gamma_n,\gamma_n)\to\pi/2$" is false (errors: arcsine density instead of Ullman-$\alpha{=}1$ with a logarithmic singularity, and the omitted weight). P39 `prop:christoffel` and `cor:T_positive` fall as well.
- The analytic route "$\Delta_n\to0$ for every finite measure" proposed in the objective is false as stated ($\nu=m_\infty$, $\Delta_n\equiv1$); its correct core was algebraic, not asymptotic.
- The Poisson route of Doc 63 §6 falls (PPP generically false + unbounded remainder + two internal contradictions, including the total mass of Lemma 4.1 against Doc 83).
- Declared gaps: **(G-118.1)** the literal $\lambda$-form ("$T_\lambda=0\ \forall\lambda$") only implies the per-index family under separation of ordinates, which ¬RH automatically violates (pairs $\beta,1-\beta$); the per-index form is the normative formulation of the criterion. **(G-118.2)** The repaired criterion is about the linearized trace $T_\lambda:=\int W_\lambda\,d\nu$; the version with exact Jacobi coefficients is a correct but distinct criterion (Obs. 5.8, via determinacy of $m_{\rm full}$, with the explicit mass condition).

The criterion remains a *reformulation* of RH, not a step toward its proof: evaluating $\int\kappa_n\,d\nu$ requires the positions of the zeros (Hadamard barrier intact, master quantifier intact: the universal quantifier over $n$ is irreducible). But the reformulation is once again **proved**, which is what was broken.

---

## §10. Table of verdicts

| Statement | Verdict |
|---|---|
| RH $\iff\int\kappa_n\,d\nu=0\ \forall n$ (per-index form) | **PROVED** (Theorem 5.6; moment rigidity + Hardy) |
| RH $\iff\Delta_n=\int\mathcal{P}_n^2\,d\nu$ constant in $n$ | **PROVED** (equivalent to the above) |
| RH $\iff T_\lambda=0\ \forall\lambda$ (literal $\lambda$-form) | Proved under separation of ordinates; **GAP G-118.1** in general (¬RH creates automatic blocks) |
| RH $\iff(a_n^{\rm full})^2=(a_n^{\rm full,on})^2\ \forall n$ + equality of masses (exact criterion) | **PROVED** (Obs. 5.8; already essentially in P39 (iii)$\Rightarrow$(i)) |
| $\nu(\mathbb{R})<\infty$ and all moments of $\nu$ finite | **PROVED**, unconditional (Prop. 2.1) |
| $dm_\infty$ determinate (Carleman, $\sum1/a_n^\infty=\infty$ exact) | **PROVED** (Theorem 3.1) |
| Doc 63 Cor. 1.2 / P39 `prop:christoffel` ($K_n(\gamma_n,\gamma_n)\to\pi/2$) | **REFUTED** ($K_n(x,x)\to\infty$ at every point, Theorem 3.2) |
| P39 `cor:T_positive` ($T_\lambda\gtrsim N(\lambda)$ under ¬RH) | **WITHDRAWN** (double dependence on false statements) |
| "$\Delta_n\to0$ for every finite measure $\nu\geq0$" (proposed route) | **FALSE** (counterexample $\nu=m_\infty$, Obs. 4.1) |
| Poisson route, Doc 63 §6 | **FALLS** (PPP premise refuted; unbounded remainder; 2 internal contradictions) |
| Doc 63 Lemma 4.1 ("same total mass") | **REFUTED** (contradicts Doc 83 under ¬RH) |
| $\mathcal{P}_n=$ Meixner–Pollaczek $(\lambda{=}\tfrac14,\phi{=}\tfrac\pi2)$, $x=s/2$ | **PROVED** (Prop. 1.2) |
| $m_\infty(\mathbb{R})=(2\pi)^{-1/2}$; $\mathcal{P}_0=(2\pi)^{1/4}$; $\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})$ | **PROVED** (Lemma 1.1; corrects P39's "probability measure") |
| Single-index/scale sharpening (Doc 103 §4) | **NOT REVIVABLE** via this route (§6.2.3) |
| D72 (Weil formula for the trace) | Survives as an identity; reinterpreted per-index (§8.3) |
| P43 ledger: L1, L3–L5, L7 (partial), L8 | Survive |
| P43 ledger: L2 | **DEAD**; replace with the repaired criterion |
| P43 ledger: L6 | **RECOMPUTE** (inherits Doc 76) |

---

## Appendix A. Sanity checks of Theorem 5.6

Audit 114 showed that the program's errors survive when nobody redoes the low-degree computations. The same standard is applied to the new theorem.

**A.1. Rigidity at low degree.** With $\mathcal{P}_0=(2\pi)^{1/4}$, $\mathcal{P}_1=(2\pi)^{1/4}\sqrt2\,s$, $\mathcal{P}_2=(2\pi)^{1/4}\sqrt{\tfrac23}(s^2-\tfrac12)$ (recurrence with $a_0=\tfrac{1}{\sqrt2}$, $a_1=\sqrt3$; those of Doc 114 §4 multiplied by the normalization of Lemma 1.1 — the common factor $(2\pi)^{1/4}$ does not alter any conclusion of the audit, which worked with $\mathcal{P}_0\equiv1$ under P39's unit-mass convention). Suppose $\Delta_0=\Delta_1=\Delta_2=c$ for an even measure $\nu\geq0$:
- $\Delta_0=c$: $\sqrt{2\pi}\,\mu_0(\nu)=c$;
- $\Delta_1=c$: $2\sqrt{2\pi}\,\mu_2(\nu)=c$, hence $\mu_2(\nu)=\tfrac12\mu_0(\nu)=c\,\mu_2(m_\infty)/\!\sqrt{2\pi}\cdot\sqrt{2\pi}$ — consistent with $\mu_2(m_\infty)/\mu_0(m_\infty)=\tfrac12$ (§1.1);
- $\Delta_2=c$: $\tfrac23\sqrt{2\pi}\,(\mu_4-\mu_2+\tfrac14\mu_0)(\nu)=c$, which with the two previous relations solves for $\mu_4(\nu)$ and reproduces $\mu_4(\nu)/\mu_0(\nu)=\mu_4(m_\infty)/\mu_0(m_\infty)$ (using $(a_0a_1)^2$-moments of the recurrence: $\mu_4/\mu_0=(a_0^2)(a_0^2+a_1^2)=\tfrac12\cdot\tfrac72=\tfrac74$).

The triangular pattern of Lemma 5.2 is visible: each new $\Delta_k=c$ solves exactly for the moment $\mu_{2k}(\nu)$ and equates it to $c\,\mu_{2k}(m_\infty)/\!\sqrt{2\pi}\cdot\sqrt{2\pi}$; no condition is redundant and none is superfluous.

**A.2. Why $\nu=m_\infty$ does not contradict the criterion.** The counterexample of Obs. 4.1 ($\nu=m_\infty$, $\Delta_n\equiv1$) satisfies (ii'') with $c=1\neq0$ — and Theorem 5.3 correctly gives $\nu=c\,m_\infty$ with $c\neq0$. The conclusion RH does **not** follow for that $\nu$, nor should it: $m_\infty$ is not of the form $\tilde g\,m_\infty$ with $\tilde g=|\zeta|^2-|\zeta_{\rm on}|^2$, because $\tilde g\equiv1$ would require $|\zeta(\tfrac12+i\gamma_*)|^2-|\zeta_{\rm on}(\tfrac12+i\gamma_*)|^2=1$ at a critical zero $\gamma_*$, where both terms vanish. Lemma 5.5 is exactly the link that uses the *arithmetic nature* of $\nu$ (that its density vanishes at the critical zeros), and it is the only place in the whole proof where $\zeta$ enters. The division of labor is clean: moment theory $\Rightarrow$ "$\nu$ is a multiple of $m_\infty$"; Hardy's theorem $\Rightarrow$ "the multiple is zero".

**A.3. Zero-mean check.** The repaired criterion respects the free identity of Doc 114 §1: $\int\kappa_n\,dm_\infty=0$, so the family (ii') vanishes identically when $\nu$ is replaced by $m_\infty$ — consistent with A.2: the family does not distinguish $\nu=0$ from $\nu=c\,m_\infty$; what distinguishes them is Hardy.

---

## Appendix B. The full dyadic bookkeeping of the analytic route (§4.2)

The computation is recorded that shows why no Plancherel–Rotach envelope bound can give $\Delta_n\to0$ without $g\in L^1(ds)$, so that the route is not retried without the hypothesis.

Partition into unit intervals $[m,m+1]$, $0\leq m\lesssim Cn$ (beyond $C n$ with $C$ large, the region outside the MRS interval contributes $O(e^{-cn})$: the polynomial grows like $e^{2n\,U(s/a_n)}$ but the remaining weight $w^{1/2}$ decays faster for $C$ large, and $\int w^{1/2}\tilde g\,ds<\infty$ by Prop. 2.1 with an $\varepsilon$-margin). In the bulk:

- expected envelope: $\sup_{[m,m+1]}\mathcal{P}_n^2\,w\;\lesssim\;\dfrac{1+\log(n/m)}{n}$ (Ullman-$\alpha{=}1$ density, §3), with edge peak $\asymp n^{-2/3}$ at $m\asymp a_n$;
- local unweighted mass of $\nu$: $\int_m^{m+1}\tilde g\,ds\leq\sup_{[m,m+1]}|\zeta|^2\leq e^{C\log m/\log\log m}=m^{o(1)}$ in the worst pointwise case, but with the only *accumulated* unconditional bound $\int_0^T\tilde g\,ds$ possibly $\asymp T\,{\rm polylog}\,T$ under adversarial ¬RH (almost all zeros just barely off-critical: $\sum\delta_j^2/\gamma_j^2<\infty$ allows this even with $\delta_j\asymp\tfrac12-\tfrac{c}{\log\gamma_j}$, since $\gamma_j\sim2\pi j/\log j$ makes $\sum\gamma_j^{-2}<\infty$).

Then $\Delta_n\lesssim\sum_{m\leq Cn}\tfrac{1+\log(n/m)}{n}\int_m^{m+1}\tilde g\,ds$, dominated by $m\asymp n$: $\asymp\tfrac1n\int_0^{Cn}\tilde g\,ds\asymp{\rm polylog}(n)$ in the worst case — a bound away from $0$ is not guaranteed, and $\to0$ only if $\int_0^T\tilde g\,ds=o(T)$. The factors $e^{\pm\pi m/2}$ of the weight cancel exactly (the envelope $\mathcal{P}_n^2w$ is flat in the bulk): there is no exponential decay to exploit. **Conclusion:** the obstruction of the analytic route is the possible linear Lebesgue mass of $\tilde g$, not a lack of asymptotics; that is why the repair had to be algebraic.

**Recoverable byproduct (conditional growth bound).** If in the future the standard Christoffel bound $\lambda_n(x)\leq C\,\tfrac{a_n}{n}\,w(x)$ for $|x|\leq\tfrac12 a_n$ is proved for the exact weight (this is the *easy* direction, via a test polynomial [LL01; To00]; it remains a technical task, **NOT VERIFIED** here for the Meixner–Pollaczek weight), then from (ii'') and the Cesàro identity of §4.3 it follows unconditionally that
$$\int_{|s|\leq T}\bigl(|\zeta|^2-|\zeta_{\rm on}|^2\bigr)(s)\,ds\;\leq\;C'\,c\,T\qquad\forall T>0,$$
a new linear restriction on the Lebesgue mass of the discrepancy under the hypothesis of the criterion. After Theorem 5.6 it is redundant for the criterion itself ($c=0$), but it is recorded because it would survive in the block variant (Appendix C), where the theorem does not close.

---

## Appendix C. The block scenario (gap G-118.1) in detail

Under ¬RH with quadruples $\{\beta_j\pm i\gamma_j,\,1-\beta_j\pm i\gamma_j\}$, the list of positive ordinates contains each $\gamma_j$ with multiplicity $\geq2$. Suppose $T_\lambda=0\ \forall\lambda$ ($\lambda$-form) and let $B=\{n_0,n_0+1\}$ be a block of size 2. With $u_n=(a_n^\infty)^2$ and $d_n=\Delta_{n+1}-\Delta_n$:
$$u_{n_0}d_{n_0}+u_{n_0+1}d_{n_0+1}=0,\qquad d_n=0\ \text{for }n\ \text{outside the blocks}.$$
The net drift of $\Delta$ across the block is
$$d_{n_0}+d_{n_0+1}=d_{n_0}\Bigl(1-\frac{u_{n_0}}{u_{n_0+1}}\Bigr)=d_{n_0}\cdot\frac{2n_0+\tfrac52}{(a_{n_0+1}^\infty)^2}\;\asymp\;\frac{2\,d_{n_0}}{n_0},$$
a free parameter per block. The partial constancies between blocks still hold, so $\nu$ is restricted to an affine subspace of codimension "number of distinct ordinates" within the moment space — exactly *one* free dimension per quadruple. What is missing to close it: either (a) an additional framework condition that fixes those dimensions (natural candidate: the $n=-1$ mass condition of Obs. 5.8, which gives one global equation, insufficient for infinitely many blocks but sufficient for **one** quadruple if moreover $d_{n_0}$ had known sign — it does not), or (b) proving that the arithmetic form of $\nu$ is incompatible with any non-zero choice of the drifts (an open problem, of the type "density of $\{\mathcal{P}_n^2\}_{n\notin B}$ in $L^1(\nu)$" — for determinate measures there are density results for polynomials in $L^p$ [Si98, §6] but the subspace here omits degrees, and the question is genuinely different). **Closed special case:** if all blocks have size 1 — i.e. if no ordinate repeats, which under ¬RH would require $\beta_j=1-\beta_j$, impossible with $\beta_j\neq\tfrac12$ — there is no gap; that is why the gap is exactly coextensive with ¬RH and the $\lambda$-form cannot be repaired this way without a new idea. The normative per-index formulation (Theorem 5.6) sidesteps it entirely.

Note also that the block gap does **not** infect the direction already valid: under RH there are no blocks that matter ($d\nu=0$ annihilates everything), and the equivalence of Theorem 5.6 is unconditional because its hypothesis (ii') is formulated per index, not per height.

---

## Appendix D. Detail of the monic conversion in Prop. 1.2

From $(n+1)P_{n+1}=2xP_n-(n+2\lambda-1)P_{n-1}$ [KLS (9.7.3) with $\phi=\pi/2$]: the leading coefficient satisfies $k_{n+1}=\tfrac{2}{n+1}k_n$, hence $k_n=2^n/n!$ and $\tilde p_n:=\tfrac{n!}{2^n}P_n$ is monic. Substituting,
$$x\,\tilde p_n=\frac{n!}{2^n}\,xP_n=\frac{n!}{2^n}\Bigl[\frac{n+1}{2}P_{n+1}+\frac{n+2\lambda-1}{2}P_{n-1}\Bigr]=\tilde p_{n+1}+\frac{n(n+2\lambda-1)}{4}\,\tilde p_{n-1},$$
whence the square of the orthonormal coefficient coupling $n-1\leftrightarrow n$ is $c_n=\tfrac{n(n+2\lambda-1)}{4}$, i.e. (coupling $n\leftrightarrow n+1$) $a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+2\lambda)}$, as used. For $\lambda=\tfrac14$: $a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+\tfrac12)}=a_n^\infty/2$ ✓ (exactly half, due to the change of variable $x=s/2$). The normalization integral $\int_{\mathbb{R}}|\Gamma(\tfrac14+ix)|^2dx=\pi\sqrt{2\pi}$ of Lemma 1.1 matches the norm formula of [KLS] at $n=0$, $\lambda=\tfrac14$, $\phi=\tfrac{\pi}{2}$.

---

## References

- [Ak65] N. I. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver & Boyd, 1965. (Determinacy; Carleman; $\lim\lambda_n(x)=\mu(\{x\})$ in the determinate case.)
- [Be68] Yu. M. Berezanskii, *Expansions in Eigenfunctions of Selfadjoint Operators*, AMS Transl. Math. Monogr. 17, 1968. (Criterion $\sum1/a_n=\infty\Rightarrow$ essential self-adjointness of the Jacobi matrix.)
- [Ha14] G. H. Hardy, *Sur les zéros de la fonction $\zeta(s)$ de Riemann*, C. R. Acad. Sci. Paris **158** (1914), 1012–1014.
- [KLS] R. Koekoek, P. A. Lesky, R. F. Swarttouw, *Hypergeometric Orthogonal Polynomials and Their $q$-Analogues*, Springer, 2010, §9.7 (Meixner–Pollaczek).
- [KvA99] A. B. J. Kuijlaars, W. Van Assche, *The asymptotic zero distribution of orthogonal polynomials with varying recurrence coefficients*, J. Approx. Theory **99** (1999), 167–197.
- [LL01] A. L. Levin, D. S. Lubinsky, *Orthogonal Polynomials for Exponential Weights*, Springer, 2001. (Christoffel functions for exponential weights; the factor $w(x)$ and the scale $a_n/n$.)
- [MS84] H. N. Mhaskar, E. B. Saff, *Extremal problems for polynomials with exponential weights*, Trans. Amer. Math. Soc. **285** (1984), 203–234.
- [RT20] B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020), e6.
- [Si98] B. Simon, *The classical moment problem as a self-adjoint finite difference operator*, Adv. Math. **137** (1998), 82–203.
- [Si11] B. Simon, *Szegő's Theorem and Its Descendants*, Princeton Univ. Press, 2011.
- [Sz75] G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloq. Publ. 23, 1975. (§2.3: parity; chap. 3: zeros, interlacing.)
- [Ti86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath-Brown), Oxford, 1986. (Chap. V: convexity; §4.42: Stirling; §9.6: $\sum\gamma^{-2}<\infty$; Thm. 10.2: Hardy.)
- [To00] V. Totik, *Asymptotics for Christoffel functions for general measures on the real line*, J. Anal. Math. **81** (2000), 283–303.
- [vA87] W. Van Assche, *Asymptotics for Orthogonal Polynomials*, Lecture Notes in Math. 1265, Springer, 1987. (Ullman-type zero distributions for linear growth of coefficients.)
- Internal documents: Doc 61–63, 68–72, 76, 83, 89, 103, 114; papers P35, P39–P44.

---

*End of Document 118.*
