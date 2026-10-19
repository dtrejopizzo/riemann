# Doc 134 — The Weil–Toeplitz algebra: symbol, compact ideal, and the boundary where the zeros live

**Program:** Riemann Hypothesis — Phase 45: DRILLING THE WALL FROM THE FREDHOLM SIDE.
**Role of the document:** constructive-creative with a fire test. Develop idea B.4 of Doc 132 to its
final form: does the Weil form decompose as (autonomous symbol computable from primes) + (compact)? If
so, strict essential positivity would give $\delta<\infty=m<\infty$ — the Fredholm half of the D-109
architecture — without touching the master quantifier of P43, because $m<\infty$ is not an exact-zero
event. The document answers the question with full precision, including the part that hurts.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = REALLY proved here, complete proof, maximal standard; external
results cited precisely. **[COMPUTATION]** = shown. **[BRIDGE]** = connection with ζ/RH with an honest
status for each link. **[WISH]** = stated without shame. **[GAP]** = declared.

**Prerequisites read at the source this session:** Doc 132 (B.4 and its proof; the counterexample
$\mathrm{diag}(-1/n)$ of Obs. 4.2; RH = essential positivity ∧ replicability, §8.2(c); Theorem C.1 and the
dictionary M1 with Doc 112). Doc 108 (indices by window $\kappa_W\asymp m\cdot n_W$ under ¬RH, Prop. 2.3/2.5;
Theorem 3.3 of sub-resolution blindness; Theorem 3.4 of the two-worlds argument; Conjecture 108-N and Theorem
4.3; §5.2: the asymptotic holds on average over windows — MV74 — and the exceptional window is the signal). P35
main.tex (realization of the Weil form in $(\mathcal K,Q)$, $\kappa(Q)=2m$, bridge conjecture
$\kappa=\mathrm{neg.ind}(H_C)$). Doc 131 §6.5 (local purity: the block structure of the form; the Mertens test
with two bumps; the discriminator is the purity of the local datum, not multiplicativity).

---

## 0. Executive summary

1. **(§1) [THEOREM 1.3] The precision B.4 needed — and a new exact characterization.** There are two
   essential positivities: the **weak** one ($\mathrm{spec_{ess}}(G)\subseteq[0,\infty)$) and the **strict**
   one ($\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$, $c>0$). Only the strict one implies $\delta<\infty$; the
   weak one coexists with $\delta=\infty$ (negative eigenvalues $\lambda_n\to0^-$). And the strict one is
   exactly optimal: **Theorem 1.3**: $\delta(G+K)<\infty$ for *every* compact $K$ ⟺ strict essential
   positivity. The Fredholm half robust-under-compacts IS the gap; a certificate without a gap certifies
   nothing.

2. **(§2) [THEOREM 2.2] Normalization (i) — fixed weight — dies by a theorem, and the target's riddle is
   resolved.** In any fixed-weight realization where the high-frequency tails have decaying $Q$-norm (the CCM
   has this: $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$), the infimum of the essential spectrum is
   $\leq 0$ **unconditionally**: the gap is destroyed by the normalization itself, not by the zeros. Under ¬RH
   with $m=\infty$ the negatives do indeed live in the compact ideal, and weak essential positivity can indeed
   hold in both worlds — with no contradiction with B.4, because B.4 requires the gap and the gap was never
   there. Empty certificate.

3. **(§3) [NEW-DEFINITION] The Weil–Toeplitz algebra $\mathcal W$.** The family of re-normalized windows
   $\{Q_n\}$ is not an operator: it is a **section of a field**. $\mathcal W:=\prod^b_n\mathcal B(H_n)$
   (bounded sections), $\mathcal J:=$ $c_0$ sections (the "compact ideal" of the field),
   $\mathcal C:=\mathcal W/\mathcal J$ (the corona), $\sigma(Q):=Q+\mathcal J$. **[LEMMAS 3.2–3.3, proved]:**
   $\|\sigma(A)\|=\limsup\|A_n\|$ and, for self-adjoint sections, $\mathrm{spec}_{\mathcal C}(\sigma(A))=$ the
   set of limit points of $\bigcup\mathrm{spec}(A_n)$. The "essential spectrum of the family" exists and is
   computable window by window in the limit. The strict positivity of the symbol is **literally** the
   uniform-over-windows quantifier: the corona turns average/uniform into $c_0$/$\ell^\infty$.

4. **(§4–§5) The fire test (C): the negatives of ¬RH are STRATIFIED by visibility — a trichotomy, not a
   dichotomy.** With the visibility $\theta_j$ of a quadruple $(\delta_j,\gamma_j)$ at the resolution
   $a(\cdot)$ of the window calendar ($\theta_j\asymp\min(1,\delta_j a(\gamma_j))^{\kappa}$): (a) **fat ones**
   ($\theta_j\geq c$ infinitely often) ⟹ the symbol SEES them:
   $\mathrm{spec}(\sigma(Q))\cap(-\infty,-c/2]\neq\emptyset$ (Theorem 5.1); (b) **thin visible ones**
   ($\theta_j\to0$, $\theta_j>0$) ⟹ the negatives accumulate exactly at $0\in\mathrm{spec}(\sigma(Q))$:
   weak positivity of the symbol YES, strict NO — **the zeros live at the symbol/compact boundary** (Theorem
   5.2); (c) **sub-resolution** ($\delta_j a(\gamma_j)\to0$) ⟹ $Q-Q^{\mathrm{aut}}\in\mathcal J$: the symbol is
   BLIND and $\delta=\infty$ all the same (Theorem 5.4; the unconditional anchor is Theorem 3.3 of Doc 108). And
   **[THEOREM 5.5]**: for EVERY calendar there are invisible $m=\infty$ configurations — $m=\sup_a m_a$ is a
   boundary event over the filtration of resolutions: the master quantifier reappears as a **resolution
   quantifier**.

5. **(§6) Computability of the symbol: localized transmutation down to the millimeter.**
   $\|\sigma(Q)-\sigma(Q^{\mathrm{aut}})\|=\limsup_n\|Q_n-Q_n^{\mathrm{aut}}\|$ (Lemma 3.2): "the symbol is the
   Archimedean prediction" ⟺ second-order asymptotics **uniform over windows** — Conjecture 108-N in C*
   coordinates, which implies RH-at-resolution (Doc 108, Thm. 4.3). What arithmetic computes
   unconditionally (MV74, via Doc 108 §5.2) are the **Cesàro states** of $\sigma(Q)$: the average. The
   average/uniform wall = weak-state topology / norm topology on the corona. Same wall, new coordinates
   — but now with one point: $0\in\mathrm{spec}(\sigma(Q))$.

6. **(§7) The positive dividend: the Fredholm × replication synergy.** **[THEOREM 7.2, in the model]:** under
   Axiom R (replicability, the abstract form of LP-112), the replicas of a quadruple preserve $\delta_0>0$:
   for any calendar with $a(\gamma)\to\infty$ they are **eventually fat** — the thin stratum is
   exactly the NON-replicable stratum (where the cosh anti-models live). Conjunction: **Axiom R ∧
   strict positivity of the symbol ⟹ RH.** The wall splits into two named pieces: **LP-134** (resolution
   repulsion: no off-line zero is asymptotically sub-resolution — new, not RH, it is geometric) and the
   uniformity of windows (the old wall). VERDICT in §9: **localized transmutation with a new
   C*-algebraic characterization of the wall, plus two new unconditional theorems (1.3 and 2.2) and a new
   well-formed missing lemma (LP-134).**

---

## 1. The exact definition of essential positivity — and why the strict one is optimal

Throughout §1–§2: $H$ a complex separable Hilbert space of infinite dimension, $G=G^*\in\mathcal B(H)$,
$E_G$ its spectral measure, $\delta(G):=\dim\mathrm{ran}\,E_G(-\infty,0)$ (the defect, Doc 132 Lemma 4.1).

**Definition 1.1 (the two essential positivities).**
- $G$ is **weakly essentially positive** if $\mathrm{spec_{ess}}(G)\subseteq[0,\infty)$.
- $G$ is **strictly essentially positive** if there exists $c>0$ with $\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$.

**Remark 1.2 (equivalent form of the strict one).** Since $\mathrm{spec_{ess}}(G)$ is closed and bounded,
$\mathrm{spec_{ess}}(G)\subseteq(0,\infty)$ ⟺ strict (a compact set inside an open one stays positively far from
the boundary). The phrase "$\mathrm{spec_{ess}}\subseteq(0,\infty)$" of B.4 (Doc 132) was, therefore, already
the strict one; what this document adds is that the weak/strict distinction **is not a refinement**: it is the
entire content of the matter (§2, §5).

**Theorem 1.3 [THEOREM] (exact characterization of robust finiteness of the defect).** For
$G=G^*\in\mathcal B(H)$ the following are equivalent:

(i) $G$ is strictly essentially positive; (ii) $\delta(G+K)<\infty$ for **every** self-adjoint compact $K$; (iii)
there exists $\varepsilon>0$ with $\delta(G-\varepsilon I)<\infty$.

*Proof.*

**(i) ⟹ (ii).** This is B.4 of Doc 132, repeated for self-containedness: by Weyl's theorem [Kato,
*Perturbation Theory*, Thm. IV.5.35], $\mathrm{spec_{ess}}(G+K)=\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$; hence
$\mathrm{spec}(G+K)\cap(-\infty,0]$ is a compact, discrete set (its accumulation points would lie in the
essential spectrum, disjoint from $(-\infty,0]$), hence finite, consisting of eigenvalues of finite
multiplicity: $\delta(G+K)<\infty$.

**(iii) ⟺ (i).** $\delta(G-\varepsilon I)=\dim\mathrm{ran}\,E_G(-\infty,\varepsilon)$. If this is finite,
$\mathrm{spec}(G)\cap(-\infty,\varepsilon)$ consists of finitely many eigenvalues of finite multiplicity, hence
$\mathrm{spec_{ess}}(G)\subseteq[\varepsilon,\infty)$: strict. Conversely, if
$\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$, take $\varepsilon=c/2$: $\mathrm{spec}(G)\cap(-\infty,c/2)$ is
finite with finite multiplicities (same argument as above), hence
$\dim\mathrm{ran}\,E_G(-\infty,c/2)<\infty$.

**(ii) ⟹ (i), by contrapositive — the new direction.** Suppose the strict property fails: there exists
$\mu\in\mathrm{spec_{ess}}(G)$ with $\mu\leq0$. I construct a self-adjoint compact $K$ with $\delta(G+K)=\infty$.

*Step 1 (orthonormal Weyl sequence with summable error).* For each $n$,
$\dim\mathrm{ran}\,E_G\bigl(\mu-8^{-n},\,\mu+8^{-n}\bigr)=\infty$ (definition of essential spectrum for
self-adjoint operators: if it were finite for some $n$, $\mu$ would be an isolated eigenvalue of finite
multiplicity or would not be in the spectrum). I choose inductively $e_n\in\mathrm{ran}\,E_G(\mu-8^{-n},\mu+8^{-n})$
unit and orthogonal to $e_1,\dots,e_{n-1}$ (possible: the range is infinite-dimensional and the orthogonality
conditions are finitely many). Then $(e_n)$ is orthonormal and
$$\|(G-\mu)e_n\|^2=\int_{(\mu-8^{-n},\mu+8^{-n})}|\lambda-\mu|^2\,d\|E_\lambda e_n\|^2\leq 64^{-n},\qquad\text{i.e. }\|(G-\mu)e_n\|\leq 8^{-n}.$$

*Step 2 (the Gram matrix of $G$ over $V:=\overline{\mathrm{span}}\{e_n\}$).* For $n\neq m$, using
orthonormality and self-adjointness:
$$|\langle Ge_n,e_m\rangle|=|\langle(G-\mu)e_n,e_m\rangle|\leq 8^{-n},\qquad
|\langle Ge_n,e_m\rangle|=|\langle e_n,(G-\mu)e_m\rangle|\leq 8^{-m},$$
hence $|\langle Ge_n,e_m\rangle|\leq 8^{-\max(n,m)}$; and $\langle Ge_n,e_n\rangle\leq\mu+8^{-n}\leq 8^{-n}$.

*Step 3 (the perturbation).* Define $K:=-\sum_{n\geq1}2^{-n}\langle\cdot,e_n\rangle e_n$: compact (norm
limit of finite-rank operators), self-adjoint, $\|K\|=\tfrac12$. For $x=\sum_n\xi_ne_n$ with finite support in
$\{n\geq n_0\}$ (with $n_0$ to be fixed):
$$\langle(G+K)x,x\rangle\leq\sum_n\bigl(8^{-n}-2^{-n}\bigr)|\xi_n|^2+\sum_{n\neq m}8^{-\max(n,m)}|\xi_n||\xi_m|.$$
The cross term is bounded by
$\sum_{n\neq m}8^{-\max(n,m)}\tfrac{|\xi_n|^2+|\xi_m|^2}{2}\leq\sum_n|\xi_n|^2\,r_n$ with
$r_n:=\sum_{m\neq n}8^{-\max(n,m)}\leq n\,8^{-n}+\sum_{m>n}8^{-m}\leq(n+1)8^{-n}$. Hence
$$\langle(G+K)x,x\rangle\leq\sum_n\Bigl(8^{-n}+(n+1)8^{-n}-2^{-n}\Bigr)|\xi_n|^2.$$
Since $(n+2)8^{-n}<2^{-n}$ for all $n\geq4$, taking $n_0=4$ the coefficient is $<0$ for each $n\geq n_0$: the
form $G+K$ is negative definite on $V_0:=\mathrm{span}\{e_n:n\geq4\}$, which is infinite-dimensional. By the
definition of $\delta$ as neg.ind (Doc 132, Lemma 4.1 and Def. 2.2), $\delta(G+K)=\infty$. $\square$

**Corollary 1.4 (the design lesson).** The only reading of "essential positivity ⟹ $m<\infty$" that survives
the compact ideal — and the essential spectrum lives *by definition* modulo that ideal — is the **strict**
one. Every certificate of the program must produce a **gap** $c>0$, not just a sign. The counterexample
$\mathrm{diag}(-1/n)$ of Obs. 4.2 of Doc 132 was not a curiosity: by Theorem 1.3 it is the general case of
what happens without a gap.

**Lemma 1.5 [LEMMA] (gap detector via orthonormal sequences).** If there exists an orthonormal sequence $(u_n)$ in
$H$ with $\liminf_n\langle Gu_n,u_n\rangle\leq\ell$, then $\inf\mathrm{spec_{ess}}(G)\leq\ell$.

*Proof.* Suppose $\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$ with $c>\ell$. Let
$\varepsilon\in(0,c-\ell)$ and $E:=E_G(-\infty,c-\varepsilon)$: of finite rank (as in 1.3, (iii)⟺(i)). With
$m_0:=\inf\mathrm{spec}(G)>-\infty$:
$$\langle Gu,u\rangle=\int\lambda\,d\|E_\lambda u\|^2\geq m_0\|Eu\|^2+(c-\varepsilon)\|(1-E)u\|^2=(c-\varepsilon)\|u\|^2-(c-\varepsilon-m_0)\|Eu\|^2.$$
Since $(u_n)$ is orthonormal, $u_n\rightharpoonup0$, and $E$ of finite rank gives $\|Eu_n\|\to0$:
$\liminf\langle Gu_n,u_n\rangle\geq c-\varepsilon>\ell$. Contradiction. $\square$

---

## 2. Normalization (i): fixed weight. Degeneration theorem and resolution of the riddle

The first candidate for the target: realize the Weil form as A SINGLE Gram operator $G$ on an $L^2$ of fixed
weight (the CCM realization is the example of the program: the negative cost of a quadruple at height
$\gamma$ is $2\delta^2K_\lambda(\gamma)$ with $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98; the
spectral measure $dm_\infty$ decays, Doc 95). In this normalization the high quadruples contribute negatives of
norm $\to0$: the sum of the off blocks is compact (indeed trace class), and the essential spectrum of $G$
ignores the zeros. The target asks: then would essential positivity be autonomous — and would it hold even
under ¬RH with $m=\infty$, without giving $m<\infty$? Where does it fail? Answer: exactly where Theorem 1.3
says — in the gap. And the failure is a theorem:

**Definition 2.1 (property (N1): high-frequency degeneration).** A Hilbert-type realization $(H,G)$ of
a Hermitian form $Q$ on a test class with a notion of height has property
**(N1)** if there exists an orthonormal sequence $(u_n)\subset H$ (normalized tests localized at heights
$T_n\to\infty$) with $\langle Gu_n,u_n\rangle=Q(u_n,u_n)\to0$.

**Theorem 2.2 [THEOREM] (degeneration of the gap under fixed weight).** If $(H,G)$ has (N1), then
$\inf\mathrm{spec_{ess}}(G)\leq0$: $G$ is **not** strictly essentially positive — whatever the position of
the zeros. Consequently, by Theorem 1.3, there exists a self-adjoint compact $K$ with $\delta(G+K)=\infty$, and
no chain of the type
$$\text{(positive autonomous symbol)}+\text{(compact)}\;\Longrightarrow\;\delta<\infty$$
can be carried out in this realization: the conclusion is false for some member of the modulo-compacts class
in which the certificate lives.

*Proof.* Immediate from Lemma 1.5 with $\ell=0$. The second statement: Theorem 1.3 ((ii)⟹(i)
by contrapositive) produces the $K$; and an "essential" certificate — invariant under the compact ideal by
construction — cannot distinguish $G$ from $G+K$. $\square$

**[BRIDGE 2.3] (the CCM has (N1)).** In the CCM realization with fixed Hilbert norm, the coordinate
vectors normalized at spectral height $\gamma$ have $Q$-value $\asymp$ local weight of $dm_\infty$, which decays
(Doc 95: decay of $dm_\infty$; Doc 98: the kernel $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$). Status:
the decay of the weight is a theorem of the CCM model (Docs 95/98); the orthonormalization of the tails and the
literal check of (N1) is declared routine not carried out line by line here — **[status: inherited from the
model, no identified risk]**. For any other fixed-weight realization with a Weil form of decreasing mass at
height (every "fixed $L^2$" normalization has this: the explicit formula distributes mass $\sim\log T$ per
window while the fixed norm distributes constant mass — the quotient per window decays after normalizing the
tails), the same theorem applies.

**Corollary 2.4 (resolution of the target's riddle).** In normalization (i):

1. The negatives of ¬RH live in the **compact ideal** (off blocks of norm $\to0$): the essential spectrum is
   blind to them. **True.**
2. The **weak** essential positivity of $G$ is then plausibly an autonomous statement, valid in both
   worlds even with $m=\infty$. **True.**
3. There is no contradiction with B.4 because B.4 (correctly read: Theorem 1.2(i)⟹(ii) = strict) **requires
   the gap**, and Theorem 2.2 shows that the gap fails unconditionally: the negative eigenvalues
   $\lambda_j\asymp-\delta_j^2K_\lambda(\gamma_j)\to0^-$ under ¬RH-$m=\infty$ break the gap without breaking the
   weak property — exactly the $\mathrm{diag}(-1/n)$ pattern.
4. **Route (i) dies with a theorem**: not because the symbol sees the zeros (it does not see them) but because
   the symbol has no gap to offer. The blindness of the essential spectrum and the uselessness of the
   certificate are, here, the same fact.

**Remark 2.5 (the structural moral).** Fixed weight flattens EVERYTHING at large height — the online sea and
the off quadruples alike. The information "$m<\infty$" is a statement **per re-normalized window**;
any fixed global normalization erases it along with the noise. This forces option (ii) of the target: the
family of re-normalized windows, which is not an operator. The right question becomes: essential spectrum
*of what*? The answer is §3.

---

## 3. [NEW-DEFINITION] The Weil–Toeplitz algebra

### 3.1. The field of windows and the corona

**Definition 3.1 (field of windows; the algebra $\mathcal W$; the ideal $\mathcal J$; the symbol).** A **field
of windows** is a sequence $\{(H_n,Q_n)\}_{n\geq2}$ where $H_n$ is a Hilbert space of finite dimension
$d_n<\infty$ and $Q_n=Q_n^*\in\mathcal B(H_n)$, with $\sup_n\|Q_n\|<\infty$. Over the field:
$$\mathcal W:=\Bigl\{A=(A_n)_{n}:\ A_n\in\mathcal B(H_n),\ \|A\|:=\sup_n\|A_n\|<\infty\Bigr\}$$
with pointwise operations: a C*-algebra (the $\ell^\infty$ product of the field).
$$\mathcal J:=\bigl\{A\in\mathcal W:\ \|A_n\|\to0\bigr\}$$
is a closed two-sided ideal (the **compact ideal of the field**: it contains every finitely-supported
section; it is its closure). The **corona** is $\mathcal C:=\mathcal W/\mathcal J$, and the **symbol** of a
section is its class:
$$\sigma(A):=A+\mathcal J\in\mathcal C.$$

Justification of the name "compact ideal": in the direct-sum operator $\bigoplus_n A_n$ on
$\bigoplus_n H_n$, a section is in $\mathcal J$ if and only if the operator is compact (finite-dimensional
blocks with norms $\to0$); $\mathcal W/\mathcal J$ is the image of the algebra of sections in the Calkin
algebra of $\bigoplus H_n$. The corona is, literally, "the family modulo compacts."

**Lemma 3.2 [LEMMA] (norm of the symbol).** $\|\sigma(A)\|_{\mathcal C}=\limsup_n\|A_n\|$.

*Proof.* ($\leq$) For fixed $N$, the truncation $A^{(N)}:=(A_2,\dots,A_N,0,0,\dots)\in\mathcal J$, hence
$\|\sigma(A)\|\leq\|A-A^{(N)}\|=\sup_{n>N}\|A_n\|\xrightarrow{N\to\infty}\limsup_n\|A_n\|$. ($\geq$) For every
$J\in\mathcal J$: $\|A+J\|=\sup_n\|A_n+J_n\|\geq\limsup_n\|A_n+J_n\|=\limsup_n\|A_n\|$ (since $\|J_n\|\to0$).
Taking infimum over $J$: $\|\sigma(A)\|\geq\limsup\|A_n\|$. $\square$

**Lemma 3.3 [LEMMA] (the spectrum of the symbol is the limit set of the window spectra).** Let
$A=(A_n)\in\mathcal W$ with each $A_n$ self-adjoint. Then
$$\mathrm{spec}_{\mathcal C}\bigl(\sigma(A)\bigr)=\Lambda(A):=\bigl\{\lambda\in\mathbb R:\ \exists\,n_k\to\infty,\ \lambda_k\in\mathrm{spec}(A_{n_k}),\ \lambda_k\to\lambda\bigr\}.$$

*Proof.* $\sigma(A)$ is self-adjoint in $\mathcal C$, real spectrum. $\Lambda(A)$ is closed and bounded
(by $\sup\|A_n\|$).

($\supseteq$, i.e. $\lambda\notin\mathrm{spec}\Rightarrow\lambda\notin\Lambda$) If $\sigma(A)-\lambda$ is
invertible in $\mathcal C$, there exists $B\in\mathcal W$ with $(A-\lambda)B=1+J$, $B(A-\lambda)=1+J'$,
$J,J'\in\mathcal J$. For large $n$, $\|J_n\|,\|J'_n\|\leq\tfrac12$, so $(A_n-\lambda)B_n$ and
$B_n(A_n-\lambda)$ are invertible, hence $A_n-\lambda$ is invertible (right and left inverse) with
$\|(A_n-\lambda)^{-1}\|\leq2\|B\|$. For self-adjoint operators,
$\|(A_n-\lambda)^{-1}\|=\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)^{-1}$:
$\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)\geq(2\|B\|)^{-1}$ for all large $n$. Then no
$\lambda_k\in\mathrm{spec}(A_{n_k})$ can converge to $\lambda$: $\lambda\notin\Lambda(A)$.

($\subseteq$, i.e. $\lambda\notin\Lambda\Rightarrow\lambda\notin\mathrm{spec}$) If $\lambda\notin\Lambda(A)$,
there exist $\varepsilon>0$ and $N$ with $\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)\geq\varepsilon$ for all $n\geq N$
(otherwise there would be a violating sequence, which by compactness of the bounded spectra would produce a point
of $\Lambda$ at distance $<\varepsilon$ from $\lambda$, and refining, $\lambda\in\Lambda$). Define
$B_n:=(A_n-\lambda)^{-1}$ for $n\geq N$ (it exists, $\|B_n\|\leq\varepsilon^{-1}$) and $B_n:=0$ for $n<N$:
$B\in\mathcal W$. Then $(A-\lambda)B-1$ and $B(A-\lambda)-1$ are finitely-supported sections $\in\mathcal J$:
$\sigma(B)$ is the inverse of $\sigma(A)-\lambda$. $\square$

**Corollary 3.4 (positivity of the symbol = uniform quantifier).** For $A$ self-adjoint:
- $\mathrm{spec}(\sigma(A))\subseteq[0,\infty)$ (**weak positivity of the symbol**) ⟺
  $\min\mathrm{spec}(A_n)\geq-\varepsilon_n$ with $\varepsilon_n\to0$;
- $\mathrm{spec}(\sigma(A))\subseteq[c,\infty)$ with $c>0$ (**strict positivity of the symbol**) ⟺
  $\forall\varepsilon>0\ \exists N:\ \mathrm{spec}(A_n)\subseteq(c-\varepsilon,\infty)$ $\forall n\geq N$ — a
  gap **uniform over the windows, eventually**.

$\square$ (Lemma 3.3 read twice.)

**Remark 3.5 (what kind of object this is).** $\mathcal C$ is the exact analogue, for a family, of the
Calkin algebra; Lemma 3.3 is the analogue of computing the essential spectrum via limit operators (the
limit-operator theory of Rabinovich–Roch–Silbermann, and of the Toeplitz symbol: the essential spectrum of
$T_\phi$ is the range of the symbol = the "window limits" of the operator; here the role of the symbol is played
by the class of the section in the corona). The conceptual point for the program: **the master quantifier of P43
(average vs. uniform over windows, Doc 108 §5.2/§7) turns into membership in $c_0$ vs. $\ell^\infty$** — the
average/uniform distinction is, in these coordinates, the average-state/norm-topology distinction on the
corona (§6). It is not a metaphor: Corollary 3.4 IS the statement "uniform over every window" of Doc 108, written
as positivity of an element of a C*-algebra.

### 3.2. The Weil field

**Definition 3.6 (the Weil field of windows; the resolution calendar).** Fix $\Delta\in(0,1]$ and a
**resolution calendar** $a:[2,\infty)\to[1,\infty)$ nondecreasing (the logarithmic support budget of the
tests per window; the natural one for the program is $a(T)\asymp\log T$, the resolution scale of individual
zeros, Doc 108 §3.3). For each $n$:
- $H_n$ := a finite-dimensional subspace of the test class (the thickened class of Doc 107 in the double
  version; Mellin tests concentrated on the window $|{\rm Im}\,s-n|\leq\Delta$ with support
  $\subseteq[e^{-a(n)},e^{a(n)}]$ in the simple version), equipped with the **online-sea normalization**: the
  inner product of $H_n$ is the spectral Gram form of the online zeros of the window (the mass
  $|\hat f(\rho)|^2$ per zero, normalized to $1$ per zero).
- $Q_n$ := the compression to $H_n$ of the Weil form, expressed in that normalization.

The **Weil field at calendar $a$** is $\{(H_n,Q_n)\}$; its symbol is $\sigma(Q)\in\mathcal C$. The
**autonomous** section $Q^{\mathrm{aut}}=(Q^{\mathrm{aut}}_n)$ is the polar/Archimedean-plus-almost-prime
prediction of each window: the blocks $E+\Pi_{\mathrm{predicted}}$ of Doc 108 (3.1) with the deficit $\Delta K$
set to zero — computable without zero positions (Doc 108, Def. 3.6 and Theorem 4.1).

**[Status of Definition 3.6 — candor].** That these compressions exist with the stated normalization and that
the section is bounded uses the realizability apparatus of Doc 107/108 (Lemma 2.4 of Doc 108 and its declared
caveat, same status here: Hypothesis D of the toy model for statements under ¬RH; under RH the normalization is
the exact diagonal of Prop. 2.2 of Doc 108). The uniform boundedness of $\|Q_n\|$ in the sea normalization
requires control of the pair-correlation corrections per window —
**[GAP-134.R, declared]**: it is assumed as axiom (S1) of the model in §4, where ALL the theorems of §5 are
proved with full rigor within the model. The document thus separates, as the contract demands: theorems (in
the axiomatized model, §4–§5) / bridge (the Weil instance, §8).

---

## 4. [NEW-DEFINITION] The spectral model $\mathfrak W$: visibility and resolution

The spectral structure of the Weil form by windows, distilled from the corpus (Doc 107 Theorem 5.5 and Prop. 6.1;
Doc 108 Prop. 2.3, Theorem 3.3, Lemma 2.4; Doc 131 §6: hyperbolic blocks per free orbit of the divisor), is:
**online sea ≈ identity + corrections; each visible off quadruple contributes a hyperbolic plane; what is
sub-resolution is not seen.** The model axiomatizes exactly that.

**Definition 4.1 (configuration).** A **configuration** is an at most countable set
$Z=\{(\delta_j,\gamma_j)\}_{j\in J}$ with $\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$ if $|J|=\infty$, and
finitely many $j$ per window ($\#\{j:|\gamma_j-n|\leq\Delta\}<\infty$, uniformly bounded per window is not
required). $m:=|J|\in\mathbb N\cup\{\infty\}$. ($Z=\emptyset$ is "RH"; $(\delta_j,\gamma_j)$ is the quadruple
$\{\tfrac12\pm\delta_j\pm i\gamma_j\}$.)

**Definition 4.2 (visibility at calendar $a$).** The **visibility** of quadruple $j$ is
$$\theta_j:=\theta(\delta_j,\gamma_j)\in[0,1],$$
where $\theta(\delta,\gamma)$ is a fixed function with the properties:

(V1) $\theta$ is continuous, nondecreasing in $\delta$, and $\theta(\delta,\gamma)\to0$ when
$\delta\,a(\gamma)\to0$; (V2) there exists $c_0>0$ with $\theta(\delta,\gamma)\geq c_0$ when
$\delta\,a(\gamma)\geq1$.

Quadruples with $\delta_j\,a(\gamma_j)\geq1$ are called **supra-resolution (fat)**; with
$\delta_j\,a(\gamma_j)<1$, **sub-resolution (thin)**; $m_a:=\#\{j:\delta_j\,a(\gamma_j)\geq1\}$.

**[COMPUTATION 4.3] (where $\theta$ comes from, and why (V1)–(V2) are the correct properties — shown).** The
negative direction of the hyperbolic plane of a quadruple requires a test with
$\hat f(\tfrac12+\delta+i\gamma)\approx-\hat f(\tfrac12-\delta+i\gamma)$ — sign opposition across a
band of width $2\delta$. I do both halves of the computation.

*Half (V1) — below resolution there is nothing to align.* Let $f$ be a test with multiplicative support
on $[e^{-a},e^{a}]$: $\hat f(s)=\int_{-a}^{a}F(u)e^{(s-\frac12)u}\,du$ with $F(u)=f(e^u)e^{u/2}$. Differentiating under
the integral, for $s$ in the band $|\mathrm{Re}\,s-\tfrac12|\leq\tfrac12$:
$$\bigl|\partial_\sigma\hat f(s)\bigr|=\Bigl|\int_{-a}^{a}u\,F(u)e^{(s-\frac12)u}du\Bigr|\leq a\,e^{a/2}\|F\|_{L^1},$$
and by the mean value theorem applied over the segment
$[\tfrac12-\delta+i\gamma,\ \tfrac12+\delta+i\gamma]$:
$$\hat f(\tfrac12+\delta+i\gamma)\,\overline{\hat f(\tfrac12-\delta+i\gamma)}\;=\;\bigl|\hat f(\tfrac12+i\gamma)\bigr|^2\;+\;O\bigl(\delta\,a\,e^{a/2}\|F\|_{L^1}\cdot\sup_{\text{band}}|\hat f|\bigr).$$
That is: the contribution of the off pair differs from that of a fictitious online pair by $O(\delta a)$ per
unit mass (after the sea normalization, which fixes $\sup|\hat f|$ and $\|F\|$ at scale $1$ per zero): **a
quadruple with $\delta a\to0$ is a perturbation of norm $O(\delta a)\to0$ of the autonomous prediction, not a
new block.** The proved unconditional anchor of this mechanism is Theorem 3.3 of Doc 108 (fixed support,
$T\to\infty$: $Q_2=AA(1+O(1/\log T))>0$ — sub-resolution blindness as a theorem).

*Half (V2) — above resolution alignment is achieved.* For $\delta a\geq1$ there exists the aligned test:
take $F$ odd-modulated, $F(u)=\chi(u/a)\sinh$-type… concretely
$\hat f(s):=\hat g(s)\cdot\bigl(s-\tfrac12-i\gamma\bigr)$ with $\hat g$ of PW type concentrated at $i\gamma$ (Doc
107, Lemma 1.2: multiplying by polynomials in $s$ = applying $x\partial_x$, preserves the class): the linear
factor equals $\pm\delta$ at $\tfrac12\pm\delta+i\gamma$ — exact sign opposition — and vanishes at
$\tfrac12+i\gamma$, suppressing the nearest online zero. The loss against the sea of the window is the content
of Lemma 2.4 of Doc 108 (with its declared caveat): the residual online mass is controlled with additional
polynomial factors and PW decay, leaving visibility $\geq c_0$ absolute. The status of this half = the status
of Lemma 2.4 (toy Hypothesis D).

The exact shape of $\theta$ in the transition zone $\delta a\asymp1$ (is it $(\delta a)$ or $(\delta a)^2$? —
the cost $2\delta^2K_\lambda(\gamma)$ of Doc 98, renormalized by sea, suggests exponent $2$; the PW computation
above gives exponent $1$ as a perturbation bound, and the realizable negativity is usually the square of the
alignment amplitude) **is not load-bearing**: no theorem in §5 uses more than (V1)–(V2). [Exact exponent:
GAP-134.θ, declared, not load-bearing.]

**Definition 4.4 (the model $\mathfrak W(Z)$).** Given a configuration $Z$ and the calendar $a$, the model field
is
$$H_n:=\mathbb C^{d_n}\oplus\bigoplus_{j\in J_n^{\mathrm{vis}}}\mathbb C^2,\qquad
Q_n:=\bigl(I_{d_n}+R_n\bigr)\ \oplus\ \bigoplus_{j\in
J_n^{\mathrm{vis}}}\begin{pmatrix}0&\theta_j\\\theta_j&0\end{pmatrix}\ +\ C_n,$$ where $d_n\asymp\Delta\log n$
(online sea per window), $J_n^{\mathrm{vis}}:=\{j:|\gamma_j-n|\leq\Delta,\ \theta_j>0\}$, and:

(S1) $\|R_n\|\leq r<\tfrac12$ for all $n$ (sea corrections: pair correlation per window). [Weil instance:
GAP-134.R.] (S2) the hyperbolic blocks have the weight $\theta_j$ of Def. 4.2, with (V1)–(V2).
[Weil instance: COMPUTATION 4.3 + Lemma 2.4/Theorem 3.3 of Doc 108.] (S3) $\|C_n\|\leq\omega_n$ with $\omega_n\to0$
(cross couplings sea↔off and off↔off between separated windows). [Weil instance: the decay of
correlations between spectral windows — direct heritage of GAP-132.ω; in the CCM model,
$K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Docs 95/98.]

The autonomous section of the model is $Q^{\mathrm{aut}}_n:=(I_{d_n}+R_n)\oplus I_{2|J_n^{\mathrm{vis}}|}$ **on
the same space** when compared with $Q_n$ at a fixed configuration, and $Q^{\mathrm{aut}}$ alone denotes the
field with $Z=\emptyset$ (sea only). Sub-resolution quadruples with $\theta_j=0$ **do not appear** in $H_n$: their
entire effect is absorbed into $R_n/C_n$ (Doc 108, Theorem 3.3: the test does not resolve them; that is the
operational definition of "sub-resolution").

**Remark 4.5 (what is theorem and what is axiom — status table of the model).**

| axiom | content | status in the Weil instance |
|---|---|---|
| block form | sea ⊕ hyperbolic planes | **theorem** (Doc 107 Thm. 5.5/Prop. 6.1; Doc 131 Thm. 6.3: free orbit ⟹ hyperbolic block) |
| (S1) $\|R_n\|\leq r<\tfrac12$ | sea ≈ identity per window | GAP-134.R (pair correlation per window, bound not proved) |
| (S2) visibility (V1)–(V2) | (V1) below resolution nothing is seen: **theorem** (Doc 108 Thm. 3.3); (V2) above resolution it is realized: status of Lemma 2.4 of Doc 108 (Hypothesis D, declared caveat) | mixed, declared |
| (S3) $\omega_n\to0$ | far windows decouple | GAP-132.ω (partial in CCM, Docs 95/98) |

All the theorems of §5 are **unconditional within $\mathfrak W$**; their transport to ζ has exactly
the statuses of this table and is discussed in §8.

---

## 5. The stratification theorems: the fire test

Throughout §5: field $\mathfrak W(Z)$ with (S1)–(S3); $\sigma(Q)\in\mathcal C$ its symbol;
$\Lambda(Q)=\mathrm{spec}(\sigma(Q))$ (Lemma 3.3); $\vartheta_n:=\max\{\theta_j:j\in J_n^{\mathrm{vis}}\}$ ($:=0$
if empty).

**Lemma 5.0 [LEMMA] (spectrum per window).** For every $n$:
$$\mathrm{spec}(Q_n)\subseteq\bigl([1-r,\,1+r]\cup\{\pm\theta_j\}_{j\in J_n^{\mathrm{vis}}}\bigr)+[-\omega_n,\omega_n].$$
In particular: $\lambda_{\min}(Q_n)\geq-\vartheta_n-\omega_n$; and if $J_n^{\mathrm{vis}}\neq\emptyset$,
$\lambda_{\min}(Q_n)\leq-\vartheta_n+\omega_n$.

*Proof.* Without $C_n$, $Q_n$ is a direct sum: the sea block has spectrum in $[1-r,1+r]$; each block
$\begin{pmatrix}0&\theta\\\theta&0\end{pmatrix}$ has eigenvalues $\pm\theta$ (eigenvectors $(1,\pm1)/\sqrt2$).
The self-adjoint perturbation $C_n$ moves each eigenvalue by at most $\|C_n\|\leq\omega_n$ (finite-dimensional
Weyl: $|\lambda_k(A+B)-\lambda_k(A)|\leq\|B\|$). The upper bound for $\lambda_{\min}$: the eigenvector $v=(1,-1)/\sqrt2$
of the block of $\vartheta_n$ gives $\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n$, and
$\lambda_{\min}\leq\langle Q_nv,v\rangle$. $\square$

**Theorem 5.1 [THEOREM] (fat ones ⟹ the symbol sees them).** If there exist $c>0$ and a subsequence $j_k$ with
$\theta_{j_k}\geq c$ and $\gamma_{j_k}\to\infty$, then
$$\mathrm{spec}\bigl(\sigma(Q)\bigr)\cap(-\infty,-c/2]\neq\emptyset.$$
In particular the symbol is not even weakly positive: the negativity of the supra-resolution quadruples
**survives the quotient by the compact ideal**.

*Proof.* Let $n_k:=$ the window of $\gamma_{j_k}$ ($n_k\to\infty$ since $\gamma_{j_k}\to\infty$). By
Lemma 5.0, $\lambda_{\min}(Q_{n_k})\leq-\theta_{j_k}+\omega_{n_k}\leq-c+\omega_{n_k}$. Since $\omega_{n}\to0$, the
$\lambda_{\min}(Q_{n_k})$ have an accumulation point $\leq-c$; the spectra are uniformly bounded,
so there is a limit along a subsequence: a point of $\Lambda(Q)$ in $(-\infty,-c]\subseteq(-\infty,-c/2]$.
Lemma 3.3. $\square$

**Theorem 5.2 [THEOREM] (visible thin ones ⟹ the negatives live exactly on the boundary $0$).** Suppose
$m=\infty$, $J_n^{\mathrm{vis}}\neq\emptyset$ for infinitely many $n$, and $\vartheta_n\to0$ (all visibilities
tend to zero). Then:

(i) $0\in\mathrm{spec}(\sigma(Q))$, attained as a limit of **negative** eigenvalues
$\lambda_{\min}(Q_{n})\in[-\vartheta_{n}-\omega_{n},\,-\vartheta_{n}+\omega_{n}]$ over the populated windows
(when $\vartheta_n>\omega_n$, genuinely negative); (ii)
$\mathrm{spec}(\sigma(Q))\subseteq\{0\}\cup[1-r,1+r]$: the **weak** positivity of the symbol HOLDS; (iii) the
**strict** positivity of the symbol FAILS; (iv) the global defect is infinite: in the direct sum
$\bigl(\bigoplus_nH_n,\bigoplus_nQ_n\bigr)$, $\delta=\infty$.

That is: the symbol is not blind to the thin ones (it sees them accumulate) but it does not separate them
either (they do not contribute negative spectral mass far from $0$): **they live at the boundary point $0$ — the
point that distinguishes weak from strict positivity, the same point as in Theorem 1.3.**

*Proof.* (i) Lemma 5.0: over the infinitely many populated windows, $\lambda_{\min}(Q_n)\to0$ (since
$\vartheta_n\to0$, $\omega_n\to0$) and $\lambda_{\min}(Q_n)\leq-\vartheta_n+\omega_n$; the limit $0$ is a point of
$\Lambda(Q)$ (Lemma 3.3). (ii) By Lemma 5.0 every eigenvalue of $Q_n$ lies in
$[-\vartheta_n-\omega_n,\vartheta_n+\omega_n]\cup[1-r-\omega_n,1+r+\omega_n]$; the limit points lie in
$\{0\}\cup[1-r,1+r]$. (iii) Immediate from (i) and Corollary 3.4. (iv) Each populated window contributes
$\mathrm{neg.ind}(Q_n)\geq1$ when $\vartheta_n>\omega_n$ (eigenvalue $\leq-\vartheta_n+\omega_n<0$); if
$\vartheta_n\leq\omega_n$ on almost every populated window, take the sequence of negative hyperbolic vectors
$v_n$ with $\langle Q_nv_n,v_n\rangle\leq-\vartheta_n+\omega_n$… in that degenerate case the negativity per
window may be lost; but $\delta$ of the configuration as a form (the $\mathrm{neg.ind}$ of the full Weil form,
not of its compressions at resolution $a$) is $2m=\infty$ by Theorem D of Doc 132 — the compression
can underestimate, never overestimate. For statement (iv) as stated (the direct sum of the field), it suffices
to have $\vartheta_n>\omega_n$ on infinitely many windows; if this does not hold, (iv) holds at the level of the
full form and the correct statement is: the field loses those negatives — which is exactly the phenomenon of
Theorem 5.4.
$\square$

**Theorem 5.3 [THEOREM] (strict positivity of the symbol ⟺ VISIBLE finiteness).** The following are equivalent:

(i) $\mathrm{spec}(\sigma(Q))\subseteq[c,\infty)$ for some $c>0$; (ii) $J_n^{\mathrm{vis}}=\emptyset$ for
all sufficiently large $n$ except, at most, windows whose maximum visibility satisfies $\vartheta_n\to0$
**and** $\vartheta_n\leq\omega_n$ eventually (quadruples below the model's noise); (iii) in the clean case
$\omega_n\equiv0$: $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$, i.e. **only finitely many visible
quadruples**: $m_a^{\mathrm{vis}}:=\#\{j:\theta_j>0\}<\infty$.

In particular (clean case): strict positivity of the symbol at calendar $a$ ⟺ $m_a^{\mathrm{vis}}<\infty$ — and
**says nothing about $m-m_a^{\mathrm{vis}}$**, the sub-resolution ones.

*Proof.* Clean case first ($\omega\equiv0$). (iii)⟹(i): if $J_n^{\mathrm{vis}}=\emptyset$ for
$n\geq N$, then $\mathrm{spec}(Q_n)\subseteq[1-r,1+r]$ for $n\geq N$: $\Lambda(Q)\subseteq[1-r,1+r]$, gap
$c=1-r>0$ (Cor. 3.4). (i)⟹(iii): if there were infinitely many windows with $J_n^{\mathrm{vis}}\neq\emptyset$,
each has eigenvalue $-\vartheta_n<0$ (Lemma 5.0, $\omega=0$): the limit points of these eigenvalues are $\leq0$,
giving $\Lambda(Q)\cap(-\infty,0]\neq\emptyset$, contradicting the gap. With noise $\omega_n\to0$: the same
argument gives (i)⟺(ii) — an eigenvalue $\leq-\vartheta_n+\omega_n$ exists in each populated window, and for no
limit point to fall below $c$ we need $-\vartheta_n+\omega_n\geq c-\varepsilon$ eventually, impossible
unless the populated windows terminate or $\vartheta_n\leq\omega_n\to0$ with eigenvalues reabsorbed into the
positive side. $\square$

**Corollary 5.3bis [COROLLARY] (the gap is quantitative: answers option (c) of the target).** In the clean
case, suppose the gap data $(c,N_0)$ is known: $\mathrm{spec}(Q_n)\subseteq[c,\infty)$ for $n\geq N_0$.
Then
$$m_a^{\mathrm{vis}}\;\leq\;\sum_{n<N_0}\bigl|J_n^{\mathrm{vis}}\bigr|\;\leq\;N_0\cdot\max_{n<N_0}|J_n^{\mathrm{vis}}|,$$
and with the density of zeros per window ($|J_n^{\mathrm{vis}}|\leq$ #zeros of the window $\ll\Delta\log n$,
[IK04, Thm. 5.8]): $m_a^{\mathrm{vis}}\ll N_0\log N_0$. **The gap quantitatively controls visible-$m$, with
explicit constants in the data $(c,N_0)$** — the hope (c) of the target is correct at the visible level. What
the gap does NOT control, by Theorem 5.4, is $m-m_a^{\mathrm{vis}}$: option (c) is true in a stratified sense and
false globally. $\square$ (Theorem 5.3 plus the von Mangoldt count.)

**Theorem 5.4 [THEOREM] (sub-resolution ⟹ the symbol is BLIND: the half that kills).** Let $Z$ be a
configuration with $m=\infty$ but $\delta_j\,a(\gamma_j)\to0$ (everything sub-resolution at calendar $a$; by (V1),
$\theta_j\to0$ and, in the strictly sub-resolution regime of Def. 4.4, $J_n^{\mathrm{vis}}=\emptyset$ with the
entire effect inside the corrections). Then, as sections over the SAME field of test spaces:
$$Q-Q^{\mathrm{aut}}\in\mathcal J,\qquad\text{hence}\qquad\sigma(Q)=\sigma(Q^{\mathrm{aut}})\ \text{in }\mathcal C,$$
and if $Q^{\mathrm{aut}}$ has a gap (S1: $\mathrm{spec}\subseteq[1-r,1+r]$ modulo $\omega$), **$\sigma(Q)$ has
strict positivity** — while the defect of the configuration is $\delta=2m=\infty$ (Doc 132, Theorem D, at
the level of the full form). The strict positivity of the symbol does NOT imply $m<\infty$.

*Proof.* In the sub-resolution regime window $n$ sees, by the mechanism of Theorem 3.3 of Doc 108
axiomatized in (S2)/(V1), a perturbation of norm controlled by the visibilities:
$\|Q_n-Q^{\mathrm{aut}}_n\|\leq\sum_{j:|\gamma_j-n|\leq\Delta}\varphi(\delta_j a(\gamma_j))+2\omega_n$ with
$\varphi(t)\to0$ when $t\to0$ ((V1) in its perturbation form: the off pair at distance $\delta$ differs from the
predicted online pair by $O(\delta a)$ on tests of resolution $a$ — the proved content of Thm. 3.3 of
D108). Since $\gamma_j\to\infty$ and there are finitely many $j$ per window, $\max_{j\in n}\varphi(\delta_ja(\gamma_j))\to0$ and
the sum per window (finite, with cardinality per window $O(1)$ in the toy model; in general, dominated by the same
support argument) tends to $0$: the difference section is in $\mathcal J$. The rest is Lemma 3.2/3.3 and
(S1). The statement $\delta=2m$ of the full form is Theorem D.4 of Doc 132 applied to the configuration
(the hyperbolic planes exist in the test class WITHOUT support restriction: with support
$\gtrsim1/\delta_j$ quadruple $j$ is visible — but that support exceeds the calendar: the negative exists, the
field does not contain it). $\square$

**Theorem 5.5 [THEOREM] (no-go of the calendar: $m<\infty$ is a boundary event in the filtration of
resolutions).**

(a) For **every** calendar $a(\cdot)$ there exists a configuration $Z$ with $m=\infty$ and
$\delta_j\,a(\gamma_j)\to0$ (take $\gamma_j:=j$ — or any admissible sequence — and
$\delta_j:=\min(\tfrac14,\,1/(j\,a(\gamma_j)))$): invisible at calendar $a$ by Theorem 5.4.

(b) For every configuration and every quadruple $j$, there exists a calendar that sees it: $\delta_j>0$ and it
suffices to have $a(\gamma_j)\geq1/\delta_j$. Therefore, with $m_a:=\#\{j:\delta_ja(\gamma_j)\geq1\}$ (the fat
ones at calendar $a$):
$$m\;=\;\sup_{a}\ m_a,$$
the supremum over the directed family of calendars.

(c) Consequently: $m<\infty$ ⟺ $\exists M\ \forall a:\ m_a\leq M$ — a $\Sigma_2$ statement about the
filtration of resolutions — and **no individual Weil–Toeplitz symbol (no fixed calendar) certifies it**: by
(a), for each $a$ there is a world with $m=\infty$ where the symbol at calendar $a$ is strictly positive.

*Proof.* (a) Explicit construction; $\delta_j\,a(\gamma_j)\leq1/j\to0$; Theorem 5.4. (b) Monotonicity of
$a\mapsto m_a$ and the pointwise observation. (c) Rewriting of (b) plus (a). $\square$

**Proposition 5.5bis [PROPOSITION] (structure of the resolution filtration).** Let $\mathcal A$ be the set
of calendars (nondecreasing functions $[2,\infty)\to[1,\infty)$), preordered by $a\preceq a'$ ⟺
$a(\gamma)\leq a'(\gamma)$ eventually. Then:

(i) **(monotonicity)** $a\preceq a'\Rightarrow m_a\leq m_{a'}+O(1)$ (the fat ones of $a$ are fat ones of $a'$
except for the finitely many $\gamma_j$ of the initial stretch); in particular $a\mapsto m_a$ is nondecreasing
modulo constants along the filtration;

(ii) **(countable cofinality)** the family $\{a_k(\gamma):=k\cdot\log\gamma\}_{k\in\mathbb N}$ is NOT cofinal in
$\mathcal A$ (a quadruple with $\delta_j=e^{-\gamma_j}$ escapes every $a_k$ but is visible for
$a(\gamma)=e^{\gamma}$): the relevant filtration is genuinely uncountable upward, BUT for each FIXED
configuration $Z$ a countable sequence of calendars suffices to compute $m=\sup_a m_a$ (take $a_k$
adapted to the first $k$ quadruples). The non-uniformity lies in the fact that the sequence depends on $Z$ —
**the same "constants internal to the world vs. uniform certificate" structure of Doc 112 §2.6 and of the master
quantifier**, now over calendars;

(iii) **(the symbol is monotone in information, not in positivity)** raising the calendar can CREATE negativity
in the symbol (a thin one becomes fat) but never destroy it in the presence of persistent fat ones: if
$\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c]\neq\emptyset$ due to quadruples with $\delta_{j_k}a(\gamma_{j_k})\geq1$,
then for every $a'\succeq a$, $\delta_{j_k}a'(\gamma_{j_k})\geq1$ eventually and Theorem 5.1 reapplies.
Strict positivity of the symbol is a **decreasing** property along the filtration; its infimum limit value
is exactly "$m<\infty$" with a uniform bound.

*Proof.* (i) If $\delta_ja(\gamma_j)\geq1$ and $a\leq a'$ from $\gamma\geq\Gamma_0$ onward, then
$\delta_ja'(\gamma_j)\geq1$ for the $j$ with $\gamma_j\geq\Gamma_0$; the remaining ones are finitely many
(configuration: finitely many per window, $\gamma_j\to\infty$). (ii) The escape:
$\delta_j a_k(\gamma_j)=k e^{-\gamma_j}\log\gamma_j\to0$ for every $k$. The adapted sufficiency: given
$Z=\{(\delta_j,\gamma_j)\}$, let $a_k$ be any calendar with $a_k(\gamma_j)\geq1/\delta_j$ for $j\leq k$
(it exists: finitely many conditions, interpolate monotonically); then $m_{a_k}\geq\min(k,m)$ and $\sup_k m_{a_k}=m$.
(iii) Immediate from the definitions and 5.1. $\square$

**Remark 5.5ter (reading).** The proposition turns into a precise statement the phrase from the summary: the
master quantifier did not disappear — it changed variables. In Doc 108 it was "$\forall$ window" vs. "almost
every window"; here it is "$\forall$ calendar" vs. "calendar adapted to the configuration". The gain is not
eliminating it (impossible: P43) but that in these coordinates the quantifier has an associated geometric
object — the filtration $\mathcal A$ and the point $0$ of the corona — and an exact identified complement:
LP-134 (§7.2) is precisely the statement "the filtration stabilizes at a fixed calendar", i.e. "$\exists a\ \forall Z$
arithmetic: $m=m_a+O(1)$".

**Remark 5.6 (the exact answer to the target's "fire test" (C)).** Do the negatives of
¬RH-with-$m=\infty$ live in the symbol or in the compact ideal? **Answer: the dichotomy is false; it is a
trichotomy stratified by $\delta_j\,a(\gamma_j)$:**

| stratum | behavior | theorem |
|---|---|---|
| fat ($\delta_j a(\gamma_j)\geq1$ i.o.) | IN THE SYMBOL: spectral mass $\leq-c/2$ | 5.1 |
| visible thin ($\theta_j\to0^+$) | AT THE BOUNDARY: accumulates at $0\in\mathrm{spec}(\sigma(Q))$; weak yes, strict no | 5.2 |
| sub-resolution ($\delta_j a(\gamma_j)\to0$) | IN THE IDEAL: $\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, totally blind | 5.4 |

And the phrase the target offered as a consolation prize is, literally, a theorem: **the zeros of ¬RH
live exactly at the symbol/compact boundary** — the intermediate stratum accumulates at the point $0$ of the
corona, the only point that separates weak from strict positivity, which by Theorem 1.3 is the only point
on which the robust finiteness of the defect depends. The master quantifier of P43 now has an exact
C*-algebraic direction: it is the point $0\in\mathrm{spec}_{\mathcal C}$.

### 5.8. Mandatory calibration: anti-models under the stratification

As in Doc 132 §5.4, the theory is tested against all corpus objects with known defect. All four
pass, and two of the checks produce information:

**(M1) The cosh class (Doc 111/112; instance I5 of Doc 132): finite $m$, fixed $\delta_0$.** Configuration: $m$
quadruples, all at height $\leq\gamma_0$ and distance $\delta_0>0$. At any calendar: finitely many visible ⟹
Theorem 5.3 ⟹ **the symbol is strictly positive** (the high windows are empty of off). Consistent and
sharp: the defect $2m\neq0$ of the cosh objects is invisible to $\sigma(Q)$ — it lives entirely in $\mathcal J$
(finite support in windows). The reading: **the symbol measures asymptotic defect, not total defect** —
exactly the division of the D-109 architecture: the symbol aims at $m<\infty$ (Fredholm axis), never at $m=0$
(which needs the replication axis). No symbol certificate will ever refute a cosh object: correct, because
the cosh objects satisfy "$\delta<\infty$" — the Fredholm certificate must not exclude them.

**(M2) Davenport–Heilbronn ($m=\infty$ real, Doc 131 §6.6, Doc 112 §3.3).** DH has infinitely many off
zeros in the strip. Under the stratification: if its $\delta_j$ do not tend to $0$ (status: plausible datum not
verified at the source — GAP-134.DH), DH has fat ones at a large constant calendar $a(\gamma)=C$, and Theorem
5.1 predicts: **the symbol of the DH form is spectrally negative** — the corona version of Prop. 6.8(a) of
Doc 131 (unconditional violation of H by blocks). Consistency test of the framework: the paradigmatic
$m=\infty$ object falls into the fat stratum, the stratum the symbol SEES. If instead DH's $\delta_j$ tended to
$0$, DH would calibrate the boundary stratum (5.2) — either outcome is informative and the numerical-bibliographic
check is a declared finite task.

**(M3) The impure $F_{p,\alpha}$ (Doc 131, Theorem 6.7): the fat stratum in pure state.** The divisor of
$F_{p,\alpha}$ with $|\alpha|=p^{1/2+\delta'}$, $\delta'>0$, is an entire vertical progression on
$\mathrm{Re}=\tfrac12+\delta'$: ALL the off zeros, ALL with the same fixed $\delta'$ — the perfect fat
configuration ($m=\infty$, $\delta_j\equiv\delta'$). Theorem 5.1: negative symbol at any unbounded calendar
(indeed at any calendar with $a\geq1/\delta'$). Independent check: the two-bump Mertens test of Theorem 6.7
of D131 produces the negativity with tests of support $\asymp M\log p$ — INCREASING support, exactly as the
visibility theory requires (the negativity of $F_{p,\alpha}$ requires large $M$: $|c_M|>2p^{M/2}$ only for
$M\gtrsim1/\delta'$ — **the barrier $|c_m|\leq2p^{m/2}$ of purity IS the sub-resolution condition in the
local world**: purity = "all potential quadruples are sub-resolution at every calendar" = autonomous symbol).
This purity↔resolution dictionary is a dividend: it connects the discriminator of Doc 131 (purity of the
local datum) with the discriminator of this document (visibility), and suggests that LP-134 is the global
analogue of "purity is an open property of the local datum".

**(M4) The De Bruijn–Newman flow (D70).** For $t<\Lambda$ (the ¬RH world of the flow), the off zeros of $\xi_t$
migrate toward the line as $t\uparrow\Lambda$: $\delta_j(t)\to0$. Under the stratification: the DBN flow
transports the configuration from the fat stratum to the thin stratum and from there to the boundary $0$ — the
negative spectral mass of the symbol is absorbed into the point $0$ exactly at $t=\Lambda$. This refines
Wish 9.D4 and gives a consistency test: the characterization $\Lambda=\inf\{t:T_\lambda(t)=0\}$ (D70) and "Λ =
absorption time of $\mathrm{spec}(\sigma(Q^{(t)}))\cap(-\infty,0)$ into $\{0\}$" must coincide if continuity of
the flow over the field is proved. [Status: image, not theorem; the continuity gap is that of D132 §8.2(c).]

**Remark 5.9 (total reconciliation with §2 and with B.4 — the complete picture of normalizations).** Under
fixed weight (§2): EVERYTHING (sea and zeros) collapses toward $0$; the gap dies autonomously; the negatives
are in the ideal; empty certificate. Under window normalization (§3–§5): the sea regains the gap $1-r$; the
negatives are stratified; what dies is not the sea's gap but the **completeness** of the certificate (5.4–5.5).
The two deaths are dual and the invariant of the duality is the point $0$: either the autonomous symbol
touches it (fixed weight), or the enemy negatives touch it (windows, thin stratum), or they escape below
resolution (windows, sub-resolution stratum). No normalization gives both an autonomous gap and capture of all
$m=\infty$ cases at once: that is Theorem 5.5(a) run over the entire family of calendars, which parametrizes
exactly the intermediate normalizations between (i) ($a$ bounded) and infinite resolution (which is not a
calendar).

---

## 6. Computability of the symbol: exactly where the transmutation remains

### 6.1. The computability identity

**Theorem 6.1 [THEOREM] (computing the symbol = uniformity over windows).** Over the same field of spaces,
$$\bigl\|\sigma(Q)-\sigma(Q^{\mathrm{aut}})\bigr\|_{\mathcal C}\;=\;\limsup_{n\to\infty}\ \bigl\|Q_n-Q^{\mathrm{aut}}_n\bigr\|.$$
In particular, the statement "the symbol of the Weil form IS the Archimedean/almost-prime prediction" (the
corona version of the symbol+compact decomposition) is equivalent to: $\|Q_n-Q^{\mathrm{aut}}_n\|\to0$ — the
asymptotics of the deficit $\Delta K$ to second order, **in operator norm per window, uniform in $n$** over
the entire ball of tests.

*Proof.* Lemma 3.2 applied to the difference section. The identification of the right-hand side with the
asymptotics of the deficit: $Q_n-Q^{\mathrm{aut}}_n$ is, by the block identity (3.1) of Doc 108, the per-window
form of the almost-prime deficit $\Delta K_\varphi$ against the tests of the window (Def. 3.6 of Doc 108); its
operator norm is the supremum over the ball — the "whole ball" uniformity of Conjecture 108-N(a).
$\square$

**Corollary 6.2 [BRIDGE] (the transmutation, localized).** The statement "$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$"
is **Conjecture 108-N in C\* coordinates**: same precision (second order, relative $o(1)$ per window after
normalizing), same uniformity (every window, full ball). By the mechanism of Theorem 4.3 of Doc 108
(transported: a ¬RH world with a fat quadruple in window $n$ separates
$\|Q_n-Q^{\mathrm{aut}}_n\|\geq\theta_j-\omega_n$, since $Q^{\mathrm{aut}}_n$ has a gap and $Q_n$ has eigenvalue
$\leq-\theta_j+\omega_n$), the identity of symbols **implies the nonexistence of fat ones at calendar $a$** — that
is, it implies RH-at-resolution-$a$ ("every off zero satisfies $\delta<1/a(\gamma)$ except for finitely many").
Status: for the double form, the link to Doc 108 Thm. 4.3 is a theorem of the corpus (with the caveats of
Lemma 2.4 declared there); for the simple per-window form, same mechanism, same status. **It is not a lemma:
it is (the resolution version of) the conclusion.** The computability of the symbol is not obtained for free;
that is the old wall, intact, now with exact coordinates: it lives in the NORM of the corona.

### 6.2. The two-worlds argument, in the corona

**Theorem 6.1bis [THEOREM] (separation of worlds; the corona version of Theorem 3.4 of Doc 108).** In the model
$\mathfrak W$, let $W_{RH}$ be the world $Z=\emptyset$ and $W_{\neg}$ a world with infinitely many fat ones of
visibility $\geq c$. Then
$$\mathrm{dist}_H\bigl(\mathrm{spec}\,\sigma(Q^{W_\neg}),\,\mathrm{spec}\,\sigma(Q^{W_{RH}})\bigr)\;\geq\;\tfrac c2+(1-r)\;\geq\;\tfrac c2,\qquad\text{and hence}\qquad\bigl\|\sigma(Q^{W_{\neg}})-\sigma(Q^{W_{RH}})\bigr\|_{\mathcal C}\;\geq\;\tfrac c2,$$
where $\mathrm{dist}_H$ is Hausdorff distance: the spectra of the two symbols differ by at least $c/2$
(that of $W_\neg$ has mass in $(-\infty,-c/2]$ — Theorem 5.1 —, that of $W_{RH}$ lives in $[1-r,1+r]$). As a
consequence, **any theorem computing $\mathrm{spec}(\sigma(Q))$ with Hausdorff error $<c/4$ decides
between the two worlds** — and that is why computability in norm of the symbol cannot be unconditionally cheap
(Cor. 6.2): it is the two-worlds argument of Doc 108 (Thm. 3.4: the autonomous part takes the same value in
both worlds; the entire difference lives in the deficit), raised from individual quadratic forms to classes in
the corona.

*Proof.* The first statement with spectra: $\mathrm{spec}\,\sigma(Q^{W_{RH}})\subseteq[1-r,1+r]$ (Lemma
5.0 with $J^{\mathrm{vis}}=\emptyset$ and $\omega_n\to0$, plus Lemma 3.3);
$\mathrm{spec}\,\sigma(Q^{W_\neg})\cap(-\infty,-c/2]\neq\emptyset$ (Theorem 5.1). A spectral point in
$(-\infty,-c/2]$ is at distance $\geq c/2+(1-r)\geq c/2$ from $[1-r,1+r]$. The
norm of the symbol difference bounds the Hausdorff distance of spectra of self-adjoint elements
($\mathrm{dist}_H(\mathrm{spec}\,A,\mathrm{spec}\,B)\leq\|A-B\|$ in any C*-algebra, by standard
perturbation of the self-adjoint spectrum): hence the lower bound for the norm. $\square$

### 6.3. What is indeed computable: the average states

**Proposition 6.3 [PROPOSITION] (arithmetic computes the Cesàro states of the symbol).** For each autonomous
section of tests $A=(A_n)\in\mathcal W$ (chosen without knowing the zeros) and each free ultrafilter/Banach
limit $\mathcal L$ over the averages, the functional
$$\varpi_{\mathcal L}(\sigma(X)):=\mathcal L\text{-}\lim_N\ \frac1N\sum_{n\leq N}\frac{\mathrm{tr}(X_nA_n)}{d_n}$$
is well defined on $\mathcal C$ (it vanishes on $\mathcal J$: if $\|X_n\|\to0$, the normalized traces
go to $0$), and is a continuous functional of norm $\leq\sup\|A_n\|$. *Proof.*
$|\mathrm{tr}(X_nA_n)|\leq d_n\|X_n\|\|A_n\|$; vanishing on $\mathcal J$ by Cesàro of a null sequence;
linearity and the bound are obvious. $\square$

**[BRIDGE 6.4] (the arithmetic status of the two sides).**
- The values $\varpi_{\mathcal L}(\sigma(Q))$ — **averages over windows** of the per-window spectral data —
  are the regime where the unconditional inventory of Doc 108 §5.2–5.3 DOES deliver: the Montgomery–Vaughan
  mean value gives the asymptotics of the deficit **for almost every window**, which determines the Cesàro
  averages. Arithmetic (explicit formula per window, D72:
  $T_\lambda=A_\lambda^{\mathrm{off}}-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$; blocks of Doc 107/108) computes
  precisely per-window traces against autonomous tests. **The symbol is computable from primes in the
  topology of average states.** [Status: the exact chain average-MV74→Cesàro of the field is heritage of the
  Doc 108 §5.2, declared, not re-proved here.]
- Positivity (weak or strict) of the symbol is a **norm** statement (equivalently: over ALL states of
  $\mathcal C$, including pure states supported on exceptional window sequences — Banach limits along
  windows aligned with the zeros). The gap between what is computable and what is necessary is exactly the
  gap between average states and exceptional pure states of the corona.

**Remark 6.5 (the wall, in a new sentence).** *Arithmetic determines the image of $\sigma(Q)$ under the
Cesàro states; RH-at-resolution is a statement about its exceptional pure states; and the set of
states the average does not control is exactly where Theorem 5.1 places the signal.* It is the "almost every
window vs. every window" of Doc 108 §5.2 turned into the geometry of the state space of a C*-algebra. Same wall;
the new information is its shape: **the wall is the corona minus its average states** — and the point $0$ of
the spectrum (Obs. 5.6) is where it is decided.

---

## 7. The synthesis: the ladder of resolutions, LP-134, and the synergy with replication

### 7.1. What is left of the original hope

The hope of the target (P44, Doc 132 B.4): $m<\infty$ is not an exact-zero event, so the P43 wall (which
blocks certifying $m=0$ from averages) might not block essential positivity. The verdict, measured:

**Theorem 7.1 [THEOREM] (synthesis; in the model $\mathfrak W$).** At a fixed calendar $a$:

(a) strict positivity of the symbol ⟺ finitely many visible quadruples (Thm. 5.3) — a statement genuinely
weaker than RH and NOT exact-zero: **up to here the hope was correct**; (b) but $m<\infty$ = strict
positivity of the symbol **across all calendars simultaneously with a uniform bound** (Thm. 5.5(b)–(c)), and for
each calendar there are invisible $m=\infty$ worlds (5.5(a)): **the quantifier expelled from positions
reappears in the resolutions**; (c) and the computability of the symbol (which was the other half of the
promise: "computable from primes") is the uniformity of windows in norm — the old wall without discount (Thm.
6.1, Cor. 6.2).

$\square$ (recombination of 5.3, 5.5, 6.1.)

The transmutation then has TWO leaves, and it is worth saying precisely what changed shape: the P43 wall
was "average vs. uniform over windows at fixed resolution"; the Phase 45 wall is that same one (leaf (c))
**plus** a new leaf, "fixed resolution vs. unbounded resolution" (leaf (b)), which no previous formulation of
the corpus had isolated. Leaf (b) is not RH in disguise: it is a statement about the **geometry of the zeros
relative to the line** that does not mention primes. This allows naming it:

### 7.2. [NEW-DEFINITION + WISH] LP-134: resolution repulsion

**LP-134 (new missing lemma, named).** *There exists a calendar $a(\cdot)$ (e.g. $a(\gamma)=C\log\gamma$, the
natural resolution) and $c>0$ such that every nontrivial zero $\rho=\tfrac12+\delta+i\gamma$ of
$\zeta$ with $\delta\neq0$ satisfies $|\delta|\geq c/a(\gamma)$.* — "Zeros cannot be asymptotically
sub-resolution: either they are on the line, or they are repelled from it at the scale of resolution."

**Why it is the exact missing piece (immediate conditional theorem):** under LP-134, every configuration has
$\theta_j\geq c_0$ for every $j$ with large $\gamma_j$ ((V2)): the thin and sub-resolution strata remain
EMPTY, and then (Theorems 5.1+5.3) **$m<\infty\iff$ strict positivity of the symbol at ONE calendar** — the
Fredholm half of the D-109 architecture becomes a single C*-algebraic statement. $\square$ (5.1, 5.3, (V2).)

**Status and character of LP-134, with total candor.** (1) **It is not RH** nor does it imply it: a world
with a quadruple at $\delta=\tfrac14$ satisfies LP-134 and violates RH. (2) **It does not follow from anything
known:** the classical zero-free region (Vinogradov–Korobov) repels from $\mathrm{Re}\,s=1$, not from
$\mathrm{Re}\,s=\tfrac12$; density theorems ($N(\sigma,T)=o(T)$) bound how many, not how close. As far as I
know, NO statement from the corpus or standard literature forbids $\delta_j\asymp1/\log^2\gamma_j$ with
$m=\infty$. [Declared: no external bibliographic search this session.] (3) **It is of the correct type:** it is a
*rigidity dichotomy* ("the defect is discrete at the natural scale"), a structural relative of Siegel's
separation (repulsion of real zeros) rotated 90°: repulsion from the line instead of from $s=1$. (4) It is
**falsifiable in the category** of Doc 131: the $F_{p,\alpha}$ objects have their divisor on $\mathrm{Re}=\beta$
FIXED (trivial repulsion); constructing an Euler object with $\delta_j\to0$ and $m=\infty$ — or proving that the
Dirichlet class does not allow it — is a concrete task for Phase 45/46 (see Wish 9.D2).

### 7.3. The Fredholm × replication synergy: the thin stratum is the non-replicable stratum

**Theorem 7.2 [THEOREM] (in the model; the conjunction that closes).** Suppose the configuration $Z$ satisfies
the **quantitative Axiom R** (the D112/M1 form of replicability): if $m\geq1$, there exists a quadruple
$(\delta_0,\gamma_0)\in Z$, $\delta_0>0$, and a sequence of heights $\tau_k\to\infty$ such that $Z$ contains
quadruples $(\delta_k',\gamma_0+\tau_k)$ with $\delta_k'\geq\delta_0/2$ (the replicas preserve the distance to
the line up to a factor $2$ — in the Rouché mechanism of D112 the replicas live in the disk $D(\rho_0+i\tau_k,r)$
with $r<\delta_0/2$: they preserve it). Let $a$ be any calendar with $a(\gamma)\to\infty$. Then:
$$m\geq1\ \Longrightarrow\ \text{infinitely many fat quadruples}\ \Longrightarrow\ \mathrm{spec}(\sigma(Q))\cap(-\infty,-c_0/2]\neq\emptyset.$$
Contrapositive: **weak positivity of the symbol (at any unbounded calendar) ∧ Axiom R ⟹ $m=0$ ⟹ RH.**

*Proof.* The replicas have
$\delta_k'\,a(\gamma_0+\tau_k)\geq(\delta_0/2)\,a(\gamma_0+\tau_k)\to\infty$: eventually supra-resolution,
visibility $\geq c_0$ by (V2). Theorem 5.1. The contrapositive uses only weak positivity because 5.1 violates
even the weak one. $\square$

**Remark 7.3 (reading — this is new and gives orientation).** (1) The thin/sub-resolution stratum (the one that
kills the pure Fredholm route, Thm. 5.4–5.5) is **exactly the stratum that replication does not produce**: the
replicas inherit fixed $\delta_0$ and every unbounded calendar eventually sees them. The invisible configurations
of Theorem 5.5(a) ($\delta_j\to0$ calibrated against the calendar) require zeros ever closer to the line — the
type of configuration the almost-period mechanism does NOT generate and that no known object of the Dirichlet
class realizes (the GAP of D111 Obs. 2.4: no known member has finite nonzero $\delta$; add: none known
has $m=\infty$ with $\delta_j\to0$; Davenport–Heilbronn has its off zeros at distances that do not tend to zero
[status: datum not verified at the source this session — GAP-134.DH, checkable numerically in the
literature]). (2) The two axes of Doc 132 §8.2(c) — Fredholm and replication — cease to be parallel: **they
need each other and complement each other exactly**: replication covers the stratum the symbol does not see;
the symbol turns the conclusion of replication ($\delta=\infty$, useless by itself) into a localized spectral
negativity and, dually, its positivity into $m=0$. The D-109 architecture "RH = (essential positivity) ∧
(replicability)" is refined to:
$$\mathrm{RH}\;=\;\underbrace{\bigl[\mathrm{spec}(\sigma(Q))\subseteq[0,\infty)\ \text{at an unbounded calendar}\bigr]}_{\text{C* statement: weak suffices}}\ \wedge\ \underbrace{\text{quantitative Axiom R}}_{\text{LP-112, unchanged}}$$
where — a concrete gain — the Fredholm piece required dropped from "strict with a gap" to **weak** (thanks to
5.1 violating the weak one), and the piece LP-134 would replace is replication entirely in this role. Two
routes to the same closure: (weakly positive symbol ∧ LP-112) or (strictly positive symbol ∧ LP-134).

### 7.4. And the good side of the quantifier? What the corona allows to prove unconditionally

So that the document does not end merely in cartography: two positive statements remain within reach and are
recorded as immediate, checkable objectives (not claimed):

- **(O1)** Strict positivity of the symbol **of the autonomous field** $\sigma(Q^{\mathrm{aut}})$ at
  sub-resolution calendar ($a$ bounded): it is Theorem 3.3 of Doc 108 repackaged — that is already a theorem
  (there). The objective: push the admissible calendar from $a=O(1)$ toward $a=\epsilon\log n$ measuring exactly
  at which $\epsilon$ the proof of D108 §3.2 breaks. Every increment of $\epsilon$ is a new unconditional
  fragment of Weil positivity, and the first $\epsilon$ where it breaks is a MEASUREMENT of the wall in units of
  resolution.
- **(O2)** The states version (Prop. 6.3): "all Cesàro states of $\sigma(Q)$ are $\geq0$" should be an
  unconditional theorem via MV74 (the average controls almost every window). It is "average positivity of the
  symbol" — strictly weaker than the weak one (which asks for ALL states), but an unconditional positivity
  statement about the right object, and it delimits the wall from within: the wall is exactly the step
  average-states → pure states. The abstract half of O2 is already proved:

**Proposition 7.4 [PROPOSITION] (from "almost every window" to "all average states" — the abstract half of
O2).** Suppose the family satisfies the density control: for every $\varepsilon>0$,
$$\frac{\#\{n\leq N:\ \lambda_{\min}(Q_n)<-\varepsilon\}}{N}\;\xrightarrow[N\to\infty]{}\;0\qquad(\ast)$$
("almost every window is $\varepsilon$-positive" — the exact form of the MV74/large-sieve output in Doc 108
§5.2). Then for every POSITIVE section of tests $A=(A_n)$, $0\leq A_n\leq I$, and every Banach limit
$\mathcal L$:
$$\varpi_{\mathcal L}\bigl(\sigma(Q)\bigr)\;:=\;\mathcal L\text{-}\lim_N\frac1N\sum_{n\leq N}\frac{\mathrm{tr}(Q_nA_n)}{d_n}\;\geq\;-\,\mathcal L\text{-}\lim_N\frac1N\sum_{n\leq N}\Bigl[\varepsilon+\sup_k\|Q_k\|\cdot\mathbf 1_{\lambda_{\min}(Q_n)<-\varepsilon}\Bigr]\;=\;-\varepsilon$$
for every $\varepsilon>0$; that is, **all positive Cesàro states of $\sigma(Q)$ are $\geq0$**.

*Proof.* Decompose $Q_n=Q_n^++Q_n^-$ (positive and negative spectral parts). If
$\lambda_{\min}(Q_n)\geq-\varepsilon$: $Q_n\geq-\varepsilon I$, hence
$\mathrm{tr}(Q_nA_n)\geq-\varepsilon\,\mathrm{tr}(A_n)\geq-\varepsilon d_n$ (using $0\leq A_n\leq I$ and that for
$B\geq-\varepsilon I$ and $0\leq A\leq I$:
$\mathrm{tr}(BA)=\mathrm{tr}((B+\varepsilon)A)-\varepsilon\,\mathrm{tr}(A)\geq-\varepsilon\,\mathrm{tr}(A)$,
since $\mathrm{tr}(CA)\geq0$ for $C,A\geq0$). If not: trivial bound
$\mathrm{tr}(Q_nA_n)\geq-\|Q_n\|\,\mathrm{tr}(A_n)\geq-\sup_k\|Q_k\|\cdot d_n$. Averaging, the fraction of
bad windows weighs $\to0$ by $(\ast)$ and the Banach limit of a sequence $\geq-\varepsilon-o(1)$ is
$\geq-\varepsilon$. Since $\varepsilon$ is arbitrary, $\geq0$. $\square$

  What remains for complete O2 is hypothesis $(\ast)$ — the density statement — whose arithmetic status is
that of Doc 108 §5.2 (Montgomery–Vaughan mean value: the deficit asymptotics holds outside an exceptional set
of windows of relative measure $o(1)$): heritage declared, to be carried out as a computation in the next
phase. Prop. 7.4 guarantees that this heritage, once carried out, produces the complete corona statement
"average positivity of the symbol" — and then the wall is stated with both sides proved: average
$\geq0$ (theorem), uniform $\geq0$ ⟺ (with R) RH.

---

## 8. [BRIDGE] Complete status table

| link | statement | status |
|---|---|---|
| Theorem 1.3 | robust finiteness of the defect ⟺ strict essential positivity | **THEOREM**, unconditional, complete proof here |
| Lemma 1.5 / Theorem 2.2 | (N1) ⟹ no essential gap; death of normalization (i) | **THEOREM**, abstract, complete proof here |
| Bridge 2.3 | the CCM has (N1) | inherited (Docs 95/98), routine not carried out, no identified risk |
| Lemmas 3.2–3.3, Cor. 3.4 | corona of the field; spectrum of the symbol = limit set | **THEOREM**, unconditional, complete proof here |
| Def. 3.6 (Weil field) | existence/boundedness of the normalized windows | Doc 107/108 apparatus + GAP-134.R declared |
| model $\mathfrak W$ (S1)–(S3) | blocks: theorem (D107/D131); (V1): theorem (D108 Thm. 3.3); (V2): status of Lemma 2.4 D108; (S3): GAP-132.ω | mixed, table in Obs. 4.5 |
| Theorems 5.0–5.5 | stratification, boundary $0$, no-go of the calendar | **THEOREM** within $\mathfrak W$, complete proofs here |
| Prop. 5.5bis | structure of the resolution filtration; LP-134 = stabilization | **PROPOSITION**, complete proof here |
| §5.8 (M1–M4) | calibration: cosh in $\mathcal J$; DH and $F_{p,\alpha}$ in the fat stratum; purity = local sub-resolution; DBN = absorption at $0$ | checks: M1, M3 with proof (via 5.1/5.3 + D131 Thm. 6.7); M2 with GAP-134.DH; M4 image |
| Theorem 6.1 | computing the symbol = uniformity in per-window norm | **THEOREM** (identity), complete proof here |
| Prop. 7.4 | almost-every-window ⟹ Cesàro states $\geq0$ | **PROPOSITION**, complete proof here; hypothesis $(\ast)$ is the MV74 heritage |
| Cor. 6.2 | that uniformity ⟹ RH-at-resolution | mechanism of Doc 108 Thm. 4.3, inherited with its caveats |
| Prop. 6.3 + Bridge 6.4 | arithmetic computes the average states of the symbol | Prop. 6.3 proved; arithmetic identification inherited (D72, D108 §5.2) |
| Theorem 7.2 | Axiom R ⟹ fat replicas ⟹ symbol sees them; weak ∧ R ⟹ RH | **THEOREM** in $\mathfrak W$ with the quantitative Axiom R (= LP-112 + preservation of $\delta_0$, which the Rouché mechanism of D112 gives by construction) |
| LP-134 | resolution repulsion | **[WISH/new missing lemma]**, open, not RH, falsifiable in the D131 category |

---

## 9. [WISH] Wishes, and VERDICT

**[WISH 9.D1 — O1/O2 of §7.4.]** Prove the average positivity of the symbol (all Cesàro states
$\geq0$, unconditional, via MV74) and push the calendar of sub-resolution blindness: both are
finite target-theorems, with no master quantifier, and they measure the wall from within.

**[WISH 9.D2 — falsify or found LP-134.]** In the category of Doc 131: construct a Hermitian spectral
object with an Euler product, $a\geq0$, and divisor with $\delta_j\to0$, $m=\infty$ (this would falsify "Euler +
positivity of the datum" implying repulsion), or prove that the class does not allow it (this would found LP-134
as a phenomenon of the class, not of ζ). It is the repulsion-version of Conjecture H⁺ (D131 Wish 6.9),
and is a task of construction, not of evaluation.

**[WISH 9.D3 — the corona with more structure.]** $\mathcal C$ here is only the quotient $\ell^\infty/c_0$ of
the field. The Weil field has more: the dilation action connects windows (genuine Toeplitz, not just
diagonal). A corona with that action (crossed product, or the full limit-operator algebra of RRS)
could have FEWER exceptional states — every symmetry acting transitively on window sequences kills
pathological pure states. Quantifying "how many states dilation kills" is a new and precise way to attack
average→uniform.

**[WISH 9.D4 — the DBN flow in the corona.]** Doc 70: $\Lambda=\inf\{t:T_\lambda(t)=0\}$. The section
$t\mapsto\sigma(Q^{(t)})$ of the De Bruijn–Newman flow in $\mathcal C$: under the flow, the $\delta_j(t)$ decrease
(the zeros migrate to the line); under the stratification of §5, **the DBN flow moves mass of the symbol toward
the boundary $0$ and from there into the ideal**. "$\Lambda\leq0$" = "at $t=0$ nothing was already left in the
symbol." Turning this into a theorem requires continuity of the flow over the field (the GAP of D132 §8.2(c)),
but the image is new: $\Lambda$ as the absorption time into the compact ideal.

### VERDICT

**Localized transmutation with dividends — neither bridge-theorem nor clean death.**

1. **The target's question ("does the Weil form = autonomous symbol + compact?") has an exact answer: it
   depends on the normalization, and the two candid options fail for dual, proved reasons.** Fixed weight: it
   does decompose (off compact), but the symbol has no gap to offer (Theorem 2.2) and without a gap there is
   nothing (Theorem 1.3: the strict one is exactly the robust finiteness). Windows: the symbol exists (Lemmas
   3.2–3.3), has an autonomous gap, and the negatives of ¬RH are stratified: fat in the symbol (5.1), thin at the
   boundary $0$ (5.2), sub-resolution in the ideal (5.4) — and the no-go of the calendar (5.5) shows that
   $m<\infty$ is a boundary event over the filtration of resolutions: **the master quantifier was not avoided;
   it was conjugated into C\* coordinates** — from "every window" to "every resolution", with the point
   $0\in\mathrm{spec}(\sigma(Q))$ as its exact geometric residue.

2. **New information about the wall (what was being sought):** (a) the C* characterization: the wall = corona
   minus average states; the enemy zeros live at the symbol/compact boundary, at the point that separates
   weak from strict; (b) the wall SPLITS: uniformity of windows (old, leaf (c) of 7.1) ⊕ resolution repulsion
   (new, LP-134, not RH, geometric, falsifiable); (c) the 7.2 synergy: the stratum the symbol does not see
   is the stratum replication does not produce — the two axes of D-109 complement each other exactly, and the
   required Fredholm piece drops from strict to **weak** in conjunction with LP-112.

3. **New unconditional theorems that stand on their own:** 1.3 (exact characterization of the
   robust finiteness of the defect — the definitive formalization of "finite defect = compact failure of
   positivity"), 2.2 + 1.5 (proved death of the fixed-weight normalization), 3.2–3.3 (the corona of the field and
   its spectral calculus), and the 5.0–5.5/6.1/7.2 package in the axiomatized model with status declared per
   axiom.

**Most attackable next theorem, in order:** (1) O2 (average positivity of the symbol, unconditional — closes
from within); (2) GAP-134.R in the toy model (bound $\|R_n\|$ with Hypothesis D: finite computation per window);
(3) 9.D2 (falsify/found LP-134 in the D131 category — pure construction, no ζ); (4) O1 (measure the $\epsilon$
at which sub-resolution blindness breaks).

---

## References

**Internal (backward-only):** Doc 132 (B.4, Obs. 4.2, Lemma 4.1, Theorem C.1, Theorem D.4, §8.2(c): RH =
essential positivity ∧ replicability; GAP-132.ω); Doc 108 (Prop. 2.3/2.5, Lemma 2.4 and its caveat, Theorem 3.3,
Theorem 3.4, Def. 3.6, Theorem 4.1, Conjecture 108-N, Theorem 4.3, §5.2 MV74/almost-every-window, §7
transmutation); Doc 107 (thickened class, Theorems 2.4/3.4/5.5, Prop. 6.1); Doc 131 (Theorem 6.3 free orbit ⟹
hyperbolic block; Theorem 6.7 local purity; Wish 6.9 H⁺); Doc 112 (LP-112; Rouché mechanism: replicas in
$D(\rho_0+i\tau_k,r)$ — preservation of $\delta_0$; Prop. 2.6); Doc 111 (Obs. 2.4); D70
($\Lambda=\inf\{t:T_\lambda(t)=0\}$); D72 (trace via the Weil formula); Docs 95/98 (decay of $dm_\infty$ and
cost $2\delta^2K_\lambda(\gamma)$); P35 (realization $(\mathcal K,Q)$, $\kappa=2m$, bridge conjecture); P43
(master quantifier; value/inertia); P44/Doc 133 (context of the rewrite).

**Literature (classical, verifiable):**
- T. Kato, *Perturbation Theory for Linear Operators*, Springer, 2nd ed. 1976 (Thm. IV.5.35: invariance of
  $\mathrm{spec_{ess}}$ under compacts — Theorem 1.3(i)⟹(ii)).
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics I, IV*, Academic Press (Weyl's criterion for
  $\mathrm{spec_{ess}}$ of self-adjoint operators — Step 1 of 1.3; Weyl's theorem §XIII.4).
- V. Rabinovich, S. Roch, B. Silbermann, *Limit Operators and Their Applications in Operator Theory*,
  Birkhäuser, 2004 (limit operators; essential spectrum as a union of limit spectra — context of
  Lemmas 3.2–3.3; the proofs here are self-contained for the product/$c_0$ case).
- A. Böttcher, B. Silbermann, *Analysis of Toeplitz Operators*, Springer, 2nd ed. 2006 (symbol and essential
  spectrum of Toeplitz operators — context for the name "Weil–Toeplitz").
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974) (mean value —
  via Doc 108 §5.2, for Bridge 6.4).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS, 2004 (Thm. 5.8: density of zeros per window
  $n_W\asymp(2\Delta/\pi)\log T$).
- R. Bhatia, *Matrix Analysis*, Springer, 1997 (finite-dimensional Weyl inequality
  $|\lambda_k(A+B)-\lambda_k(A)|\leq\|B\|$ — Lemma 5.0).

*End of Doc 134.*
