# Document 103 — Strict positivity of $W_\lambda$ and sharpening of P39

**Program:** Riemann Hypothesis — Phase 35 (micro verification)
**Prerequisites:** Doc 63 (Abel kernel and its positivity), 64/P39 (trace criterion), 83 ($d\nu\geq 0$).

---

## Summary

We prove that the Abel kernel $W_\lambda$ of the CCM program is **strictly positive at every point** of $\mathbb{R}$ (not merely almost everywhere), for every $\lambda$ with $N(\lambda)\geq 1$. This **sharpens Corollary 7.5 of Doc 63**, which left a finite exceptional set (the nodes of $\mathcal{P}_{N(\lambda)+1}$) and neutralized it by appealing to the absolute continuity of $d\nu$. We show here that this exceptional set is **empty**. As an immediate consequence, the universal quantifier "$\forall\lambda>0$" in the trace criterion P39 (Doc 64) is **redundant**: vanishing $T_\lambda=0$ for **a single** $\lambda$ (with $N(\lambda)\geq 1$) already is equivalent to RH. The one-parameter family $\{T_\lambda\}_{\lambda>0}$ ceases to be a family: a single member determines it.

---

## §1. Definition and the three-term recurrence

By Doc 63 (§7.1), with the truncation convention $N(\lambda)=\#\{n:\gamma_n\leq\lambda\}$, the Abel kernel admits the summation-by-parts form
$$
W_\lambda(s) \;=\; \sum_{n=1}^{N(\lambda)} \bigl[(a_n^\infty)^2-(a_{n-1}^\infty)^2\bigr]\,|\mathcal{P}_n(s)|^2 \;+\; (a_{N(\lambda)}^\infty)^2\,|\mathcal{P}_{N(\lambda)+1}(s)|^2,
$$
where $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ (direct computation with $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$, see Doc 63 Cor. 7.2). We write $N:=N(\lambda)$. Thus
$$
W_\lambda(s) \;=\; \sum_{n=1}^{N} n\,|\mathcal{P}_n(s)|^2 \;+\; (a_N^\infty)^2\,|\mathcal{P}_{N+1}(s)|^2. \tag{1}
$$
All coefficients are strictly positive.

The CCM orthonormal polynomials $\{\mathcal{P}_n\}$ with respect to $dm_\infty$ satisfy, by the parity of the measure ($b_n=0$, see Doc 92/P39), the three-term recurrence
$$
s\,\mathcal{P}_n(s) \;=\; a_n^\infty\,\mathcal{P}_{n+1}(s) + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s), \qquad a_k^\infty>0,\quad \mathcal{P}_0\equiv 1. \tag{2}
$$

---

## §2. The zero set of $W_\lambda$ is empty

**Lemma 2.1 (No simultaneous vanishing of consecutive polynomials).**
For every $n\geq 0$, the polynomials $\mathcal{P}_n$ and $\mathcal{P}_{n+1}$ have no common zero in $\mathbb{C}$.

*Proof.* Suppose $\mathcal{P}_{n+1}(s_0)=0$ and $\mathcal{P}_n(s_0)=0$ for some $s_0\in\mathbb{C}$. Substituting in (2) with index $n$:
$$
s_0\,\mathcal{P}_n(s_0) = a_n^\infty\,\mathcal{P}_{n+1}(s_0) + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s_0)
\;\Longrightarrow\; 0 = 0 + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s_0).
$$
Since $a_{n-1}^\infty>0$, it follows that $\mathcal{P}_{n-1}(s_0)=0$. Iterating the recurrence downward (indices $n-1,n-2,\dots,1$) gives $\mathcal{P}_{n-1}(s_0)=\mathcal{P}_{n-2}(s_0)=\cdots=\mathcal{P}_0(s_0)=0$. But $\mathcal{P}_0\equiv 1\neq 0$, a contradiction. $\square$

**Theorem 2.2 (Pointwise strict positivity of $W_\lambda$).**
For every $\lambda$ with $N(\lambda)\geq 1$,
$$
W_\lambda(s) \;>\; 0 \qquad \text{for every } s\in\mathbb{R}.
$$

*Proof.* By (1), $W_\lambda$ is a sum of non-negative terms with coefficients $>0$. If $W_\lambda(s_0)=0$ for some $s_0\in\mathbb{R}$, every term would vanish; in particular the term $n=N$, $N\,|\mathcal{P}_N(s_0)|^2$ (present because $N\geq 1$), would force $\mathcal{P}_N(s_0)=0$, and the final term would force $\mathcal{P}_{N+1}(s_0)=0$. This contradicts Lemma 2.1 (case $n=N$). Hence $W_\lambda(s)>0$ on all of $\mathbb{R}$. $\square$

**Remark 2.3 (Comparison with Doc 63).** Cor. 7.5 of Doc 63 asserted $W_\lambda>0$ *except on a finite set* (the nodes of $\mathcal{P}_{N+1}$), and closed the CTP argument by invoking the fact that $d\nu$ is absolutely continuous (Doc 83), so that the finite set has $d\nu$-measure zero. Theorem 2.2 shows that **this set is empty**: positivity is genuinely pointwise and requires no hypothesis on $d\nu$ whatsoever. The argument is purely structural (three-term recurrence with $a_k>0$).

**Remark 2.4 (Case $N(\lambda)=0$).** For $\lambda$ below the first node, $N(\lambda)=0$ and the sum in (1) is empty: $W_\lambda(s)=(a_0^\infty)^2|\mathcal{P}_1(s)|^2$, which vanishes at the single zero of $\mathcal{P}_1$ (this is $s=0$, since $\mathcal{P}_1(s)=\sqrt2\,s$). In this degenerate regime one exactly recovers the situation of Doc 63 (an isolated zero, neutralized by the absolute continuity of $d\nu$). Theorem 2.2 covers all other $\lambda$.

---

## §3. Consequence: a single $\lambda$ determines RH

**Theorem 3.1 (Sharpening of P39).**
Fix any $\lambda_0>0$ with $N(\lambda_0)\geq 1$. Then
$$
\mathrm{RH} \;\Longleftrightarrow\; T_{\lambda_0}=0.
$$
That is, the trace criterion of Doc 64 / P39 holds with a **single** value of the parameter; the quantifier "$\forall\lambda>0$" is redundant.

*Proof.* ($\Rightarrow$) Under RH, $dm_{\mathrm{full}}=dm_{\mathrm{full,on}}$, hence $d\nu=0$ and $T_{\lambda_0}=\int W_{\lambda_0}\,d\nu=0$ (Doc 64).

($\Leftarrow$) By Doc 83, $d\nu = dm_{\mathrm{full}}-dm_{\mathrm{full,on}}\geq 0$ is a non-negative measure (in fact $d\nu=(R-1)\,|\zeta_{\mathrm{on}}|^2\,dm_\infty$ with $R=|\zeta/\zeta_{\mathrm{on}}|^2\geq 1$). By Theorem 2.2, $W_{\lambda_0}(s)>0$ for every $s\in\mathbb{R}$. Then the integrand $W_{\lambda_0}\,\dfrac{d\nu}{dm_\infty}$ is non-negative and, if
$$
T_{\lambda_0}=\int_{\mathbb{R}} W_{\lambda_0}(s)\,\bigl(R(s)-1\bigr)\,|\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s)=0,
$$
non-negativity of the integrand forces $W_{\lambda_0}\,(R-1)\,|\zeta_{\mathrm{on}}|^2=0$ for $dm_\infty$-almost every point. Since $W_{\lambda_0}>0$ everywhere and $|\zeta_{\mathrm{on}}|^2>0$ except at the isolated zeros of $\zeta_{\mathrm{on}}$ (a set of measure zero), one concludes $R-1=0$ a.e., i.e. $d\nu=0$. By the equivalence $d\nu=0\iff$ RH (Doc 89, condition 2), RH is obtained. $\square$

**Corollary 3.2.** Condition 4 of the list of equivalences in Doc 89 ("$T_\lambda=0$ for every $\lambda>0$") can be replaced by "$T_{\lambda_0}=0$ for some (equivalently, any) $\lambda_0$ with $N(\lambda_0)\geq 1$".

---

## §4. Structural reading

This result is deliberately modest in difficulty but significant in structure. In the "meta-pattern" of the program (see P41, §2), RH repeatedly appears as the **boundary point** of a one-parameter family whose other members are unconditional theorems: De Bruijn–Newman time $t$, the approximation parameter $x$ of the spectral triples, the scale $\lambda$ of the Abel kernel. Theorem 3.1 shows that **at least one of these families collapses to a point**: $\{T_\lambda\}$ is not a one-parameter family of independent obstructions, but a single obstruction presented redundantly. This does not bring the proof of RH any closer —the difficulty remains concentrated in showing $d\nu=0$ without knowing the positions of the zeros (Hadamard barrier, MW-7)— but it cleans up the statement and removes a spurious degree of freedom from the map.

---

## §5. Results table

| Object | Result | Quality |
|---|---|---|
| $\mathcal{P}_n,\mathcal{P}_{n+1}$ with no common zero | YES (Lemma 2.1) | Rigorous |
| $W_\lambda(s)>0\ \forall s\in\mathbb{R}$, $N(\lambda)\geq 1$ | YES (Theorem 2.2) | Rigorous |
| Exceptional set of Doc 63 Cor. 7.5 is empty | YES (Remark 2.3) | Rigorous |
| RH $\iff T_{\lambda_0}=0$ for a single $\lambda_0$ | YES (Theorem 3.1) | Rigorous |

---

*End of Document 103.*
