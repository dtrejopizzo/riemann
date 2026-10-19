# Doc 100 — Semilocal Maslov index: the first falsifiable step of $\mathbf{C}_D^B$

**Program:** Riemann Hypothesis — Phase 35, Five Fronts
**Prerequisites:** Docs 91, 94, 96, 98; Paper P35; Phase 27 (docs 00–03); Connes–Consani literature verified via web
**Absolute rule:** no proof is fabricated. Every step is either a proof, or a statement from the literature with a verified reference, or a precisely declared GAP. Statements from the literature that could not be verified against their source are marked [NOT VERIFIED].

---

## Executive summary

Doc 96 formulated Conjecture $\mathbf{C}_D$ (adelic Maslov index): $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p = 2\kappa$, with vanishing local contributions, as the only route of Direction B not clearly circular. Its declared obstacle was that it requires a local theory of $H_C$ over $\mathbb{Q}_p$ that does not exist. This document explores an alternative: **not** developing that local theory, but anchoring $\mathbf{C}_D^B$ in the only unconditional Weil positivity theorem that exists in the literature — the **semilocal/archimedean theorem of Connes–Consani** (Selecta Math. 2021) — and in its later semilocal infrastructure (Connes–Consani, J. Number Theory 2021; Connes–Consani–Moscovici, Ann. Funct. Anal. 2024).

**Results of the document:**

1. (§2) We state precisely, verified against the sources, what Connes–Consani prove: positivity of the **full Weil form** restricted to the subspace of test functions with support in $(1/2, 2)$ — a subspace on which the full form **coincides exactly** with the archimedean term $W_\infty$, because the support kills all the prime terms. It is not a truncated local positivity: the dichotomy of question (i) dissolves by exact coincidence in the window.

2. (§3) The semilocal Maslov index $\mu_S$ is rigorously defined as the negative index of the program's Weil form (Doc 91, Def. 1.2) restricted to the filtration of windows $\mathcal{D}_n$, with a **proved** exhaustion lemma: $\kappa(Q) = \lim_n \kappa(Q|_{\mathcal{D}_n})$. The interpretation as spectral flow (crossings of a path of forms) is given with its technical gaps declared.

3. (§4) $\mu_{\{\infty\}} = 0$ is an **unconditional theorem** (Yoshida 1992 by computation; Connes–Consani 2021 by operatorial mechanism). The trap of question (iii) is answered: as an index statement it is trivial given the positivity; the new content is the **mechanism** (compression to the Sonine space: positivity by construction + compact discrepancy), and that mechanism has a proved semilocal counterpart for every finite $S$ (CCM 2024).

4. (§5) The critical technical point of the proposal is **verified and refuted**: the space of test functions of CC does **not** shrink as $S$ grows — it grows (support in $[1/n, n]$, $n \to \infty$). The real obstruction to $S \to$ all places is something else, and it is **new** relative to MW-2/Phase 27: it is not the non-factorization of the zero side (irrelevant here, because the geometric side of the explicit formula is additive by places unconditionally), but the **non-uniformity in $n$ of the operatorial control of the Weil−Sonine discrepancy**, where the $\sqrt{n}$ vs $\log n$ barrier (Doc 91, Prop. 4.5) reappears window by window. It is formulated as Obstacle $\mathbf{O}_{SL}$ with three components.

5. (§6) Consequence for $\mathbf{C}_D^B$: the **additive** form of the conjecture ($\mu = \mu_\infty + \sum_p \mu_p$) is discarded as a formulation (the index is not additive and the local decomposition of the zero side was refuted in Phase 27); the correct form is by **filtration increments**, and its first case ($S = \{\infty\}$) is proved. What remains is the first falsifiable step: **Conjecture 100.A** ($\mu_{\{\infty,2\}} = 0$), an explicit inequality with a single prime term, open, with all the operatorial infrastructure already built in the literature.

6. (§7) **VERDICT: PARTIAL** — a route alive in its first stretch (small $S$, falsifiable, with a proven non-circular mechanism in the base case), with no known mechanism for the uniform stretch $n \to \infty$.

---

## §1. Framework: what this document takes from the program

### 1.1 The Weil form and the index $\kappa$

From Doc 91 (Defs. 1.1, 1.2, 1.5): for $f, g \in \mathcal{S}(\mathbb{R}^*_+)$, with $\hat f(s) = \int_0^\infty f(x) x^s \, dx/x$ (Mellin), $\tilde g(x) = \overline{g(1/x)}/x$, $(f \star g)(x) = \int_0^\infty f(y) g(x/y)\, dy/y$:

$$Q(f, g) = \mathcal{W}(f \star \tilde g), \qquad Q[f] = \mathcal{Z}[f] - \mathcal{P}[f] + \mathcal{A}[f],$$

where $\mathcal{Z}$ is the zero contribution, $\mathcal{P}$ the prime contribution, $\mathcal{A}$ the archimedean contribution (Doc 94, §1). The negative index is $\kappa(Q) = \sup\{\dim W : Q|_W < 0\}$; Weil's Theorem (1952) gives RH $\iff \kappa(Q) = 0$; under Hypothesis D with $m$ off-critical orbits, $\kappa(Q) = 2m$ (P35, kappa-2m Theorem, via P32–P33).

### 1.2 The state of Direction B

- Doc 91: conditions C1–C4, C6, C7 are equivalent to RH or circular; C5 (prime tail) is the only one not blocked and sits at the critical threshold $a_{\mathrm{tail}} = 1$.
- Doc 94: the gap $\kappa < \infty \to \kappa = 0$ (Conjecture $\mathbf{C}_B$) has no argument in the literature.
- Doc 96: Theorem 8.1 — under $\kappa < \infty$, the negative index is localized in $\mathcal{K}_{\mathrm{off}}$; Conjecture $\mathbf{C}_D$ (adelic Maslov index) with the explicit warning that point (iii) ($\mu_p = 0$ local) is the most questionable, and that the local theory of $H_C$ over $\mathbb{Q}_p$ is missing.
- Phase 27 (doc 02-C-wall-analysis): **the prime term of $Q$ DOES factor by places; the zero term does NOT factor** (Proposition 27-C.1, Wall A). Any decomposition $Q = Q_\infty + \sum_p Q_p$ of the spectral side requires the unfinished arithmetic site of Connes–Consani (MW-5).
- Doc 98 (§7): in the toy model of an off-critical quadruple, the spectral flow of the crossing $\delta: 0 \to \delta_0$ is $-2$ and $|\mu| = 2 = \kappa$, with declared regularity gaps. It is the program's only computed instance of the Maslov–Krein identity.

### 1.3 The relevant walls

MW-2 (the Euler product lives in $\mathrm{Re}(s) > 1$; the zeros are global); MW-3 (no Hasse–Minkowski in infinite dimension); MW-5 (factoring $Q$ by places requires nonexistent arithmetic cohomology); MW-4 / barrier $\sqrt{N}$ vs $\log N$ (Doc 91, Prop. 4.5): the prime term grows like $\sqrt{N}$ against $\log N$ for the archimedean one, and positivity requires oscillatory cancellation that is the content of RH.

The proposal of this document: the Connes–Consani semilocal framework is **the only known region where MW-4 has a proved exception**, and we must measure precisely what can be extracted from that exception for $\mathbf{C}_D^B$.

---

## §2. The semilocal theorem of Connes–Consani: verified statements

Everything that follows in this section was verified directly against the sources (arXiv:2006.13771, full text; arXiv:2310.18423 v2, full text of the introduction and §4; arXiv:2008.10974, abstract and publication data) in.

### 2.1 The Weil criterion in CC normalization

**Explicit formula (CC 2021, eq. (1)).** For a precise class of test functions $f$ on $\mathbb{R}^*_+$, with $\tilde f(s) := \int_0^\infty f(x) x^{s-1} dx$:
$$\tilde f(0) - \sum_{\rho \in Z} \tilde f(\rho) + \tilde f(1) = \sum_v \mathcal{W}_v(f),$$
where $Z$ is the multiset of nontrivial zeros of $\zeta$ and the right-hand sum runs over the places of $\mathbb{Q}$ ($v = \infty, 2, 3, 5, \ldots$). The right-hand side is the **geometric side**: $\mathcal{W}_p$ concentrates the terms $\log p \cdot p^{-k/2}[f(p^k) + f(p^{-k})]$ and $\mathcal{W}_\infty$ the gamma-factor term (principal value at $x = 1$).

**Criterion (CC 2021, eq. (2)).** For **any** finite set $F \subset \mathbb{C}$ with $F \supset \{0, 1\}$ and $F \cap Z = \emptyset$:
$$\mathrm{RH} \iff \sum_v \mathcal{W}_v(g * \tilde g^\sharp) \leq 0 \quad \forall g \in C_c^\infty(\mathbb{R}^*_+) \text{ with } \tilde g(z) = 0 \;\forall z \in F,$$
where $g^\sharp(x) = x^{-1} g(x^{-1})$, $\bar g(x) = \overline{g(x)}$. Two crucial observations, both textual in CC:

(a) The vanishing condition on $F$ is legitimate **only if it is known that $F$ contains no zeros** ($F \cap Z = \emptyset$). This will reappear in §5 as a component of the obstruction.

(b) *"The key point being that the right-hand side of the explicit formula, when evaluated on a test function $f$ with compact support, involves only finitely many primes"* (CC 2021, Introduction). RH, which concerns the asymptotic distribution of the primes, admits an equivalent formulation involving **finitely many primes at a time**.

**Lemma 2.0 (CC $\leftrightarrow$ program convention dictionary).** Let $g \in C_c^\infty(\mathbb{R}^*_+)$ with $\hat g(0) = \hat g(1) = 0$ (Mellin at the poles; in CC's multiplicative Fourier normalization, vanishing at $\pm i/2$ after the unitary shift $\Delta^{1/2}f(x) = x^{1/2}f(x)$). Then:
$$Q(g, g) \;=\; \sum_{\rho \in Z} \hat g(\rho)\, \overline{\hat g(1 - \bar\rho)} \;=\; -\sum_v \mathcal{W}_v(g * \tilde g^\sharp).$$

*Proof.* The Mellin transform of $h = g \star \tilde g$ is $\hat h(s) = \hat g(s) \overline{\hat g(1 - \bar s)}$ (Doc 91, Obs. 1.3, with the program's involution $\tilde g$, which coincides with CC's $\tilde g^\sharp = \bar g^\sharp$). The explicit formula in CC form (eq. (1)) applied to $h$ gives $\tilde h(0) - \sum_\rho \tilde h(\rho) + \tilde h(1) = \sum_v \mathcal{W}_v(h)$ with $\tilde h(s) = \hat h(s)$ in the variable translation; the conditions $\hat g(0) = \hat g(1) = 0$ kill $\tilde h(0)$ and $\tilde h(1)$, whence $\sum_\rho \hat h(\rho) = -\sum_v \mathcal{W}_v(h)$. The left-hand side is $\mathcal{Z}[g]$ in the notation of Doc 94, which on the subspace with pole conditions coincides with $Q(g,g)$ (the formula $Q = \mathcal{Z} - \mathcal{P} + \mathcal{A}$ of Doc 94 is precisely the explicit formula written on the spectral side; equating both expressions for $\mathcal{W}(h)$ produces the identity). $\square$

At the archimedean place CC write $W_\infty := -W_{\mathbb{R}}$, so that the Weil inequality takes the form $W_\infty(f) \geq 0$. **Convention for the whole document:** we use $Q \geq 0$ (program) and translate via Lemma 2.0 without further comment. Note that the lemma already exhibits the feature that the whole strategy exploits: under the pole conditions, $Q(g,g)$ — a spectral object (sum over zeros) — is **equal** to minus the geometric side, which is a sum of explicit local terms. Positivity can be attacked entirely from the geometric side, where additivity by places is a trivial fact and not an open problem (contrast with Phase 27, §5.3).

### 2.2 The semilocal framework and property $P(n)$

**Semilocal framework (Connes 1999, Selecta Math. 5; CCM 2024, §4).** For finite $S$ of places with $\infty \in S$: the semilocal adele ring is $\mathbb{A}_S = \prod_{v \in S} \mathbb{Q}_v$; the semilocal adele class space is $X_S = \mathbb{A}_S / \Gamma$, with $\Gamma = \{\pm p_1^{n_1} \cdots p_k^{n_k} : p_j \in S \setminus \{\infty\}, n_j \in \mathbb{Z}\} \subset \mathrm{GL}_1(\mathbb{A}_S)$; the semilocal idele class group $C_S = \mathrm{GL}_1(\mathbb{A}_S)/\Gamma$ acts on $X_S$. Connes' semilocal trace formula (1999) — which is a **theorem**, unlike the global one, which is equivalent to RH — computes the trace of the scaling action on $L^2(X_S)$ with cutoff and produces exactly $\sum_{v \in S} \mathcal{W}_v$.

**Property $P(n)$ (CCM 2024, Introduction, textual).** *"There exists a property $P(n)$, involving only the Euler factors for primes smaller than $n$, and whose validity for all $n$ is equivalent to RH. This is derived from Weil's positivity criterion which involves the quadratic form $Q_n$ defined using the Riemann–Weil explicit formula applied to test functions with support in the compact symmetric interval $[\frac{1}{n}, n]$."*

That is: the support restriction $\mathrm{supp}(f) \subset [1/n, n]$ kills $f(p^k)$ and $f(p^{-k})$ for every $p^k > n$, so that the **full** geometric side evaluated at $f$ coincides with the **semilocal** geometric side $\sum_{v \in S(n)} \mathcal{W}_v(f)$, where $S(n) = \{\infty\} \cup \{p : p \leq n\}$ (only the powers $p^k \leq n$ enter; CCM write "primes smaller than $n$"). In CC 2021 (Introduction) the same condition is written $\mathrm{Supp}(f) \subset (p^{-1}, p)$ for the set of places $\{\infty, 2, 3, \ldots, p\}$.

### 2.3 The archimedean theorem (the base case, proved)

**Archimedean Weil inequality (stated in CC 2021, p. 2; proved by Yoshida 1992).** *For every smooth, positive-definite $f$, with support in the interval $(1/2, 2)$ and whose (multiplicative) Fourier transform vanishes at $\pm i/2$, we have $W_\infty(f) \geq 0$, where $W_\infty := -W_{\mathbb{R}}$.*

CC attribute the first proof to H. Yoshida (*On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21 (1992), 281–325), "reducing it to an explicit computation." The vanishing at $\pm i/2$ of the multiplicative Fourier transform corresponds, in Mellin terms, to vanishing at the poles $s = 0, 1$; since $\zeta(s) \neq 0$ at $s = 0, 1$ within the relevant class, the condition is admissible in criterion (2).

**Theorem 1 of CC 2021 (textual).** *Let $g \in C_c^\infty(\mathbb{R}^*_+)$ with support in $[2^{-1/2}, 2^{1/2}]$ and Fourier transform vanishing at $i/2$ and at $0$. Then:*
$$W_\infty(g * g^*) \geq \mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*) \geq 0,$$
*where $\vartheta$ is the scaling action of $\mathbb{R}^*_+$ on $L^2(\mathbb{R})^{\mathrm{ev}}$ and $\mathbf{S}$ is the orthogonal projection onto the complement of the range of $\mathcal{P}_1 \vee \widehat{\mathcal{P}}_1$ (phase-space cutoff projections, parameter $\Lambda = 1$): the **Sonine** space (even functions which, together with their Fourier transform, vanish identically on $[-1, 1]$; Sonin 1880, Burnol 2002, de Branges).*

**Theorem 6.11 of CC 2021.** There is a finite constant $c$, with $13 < c < 17$, such that for every $g \in C_c^\infty([2^{-1/2}, 2^{1/2}])$ with $\hat g(i/2) = 0$:
$$W_\infty(g * g^*) \geq \mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*) - c\, |\hat g(0)|^2.$$

**Corollary 2 of CC 2021.** $c|\hat g(0)|^2 + \sum_{s \in Z} \hat g(s) \overline{\hat g(\bar s)} \geq \mathrm{Tr}(\vartheta(g) \mathbf{S} \vartheta(g)^*)$; in CC's words, the Sonine trace requires, besides the zeros of $\zeta$, an additional contribution (irrelevant for RH) on the critical line between the first two zeros $\sim 1/2 \pm 14.1347 i$, *"as if $\zeta(z)$ were multiplied by $(z - 1/2)^{17}$"*.

**Theorem 3 of CC 2021 (the discrepancy is an infinitesimal).** For every $f \in C_c^\infty(\mathbb{R}^*_+)$:
$$\mathrm{Tr}(\vartheta(f)\mathbf{S}) = W_\infty(f) + \int f(\rho)\, \epsilon(\rho)\, d^*\rho,$$
with $\epsilon(\rho) = \sum_n \frac{\lambda(n)}{\sqrt{1 - \lambda(n)^2}} \langle \xi_n \mid \vartheta(\rho^{-1}) \zeta_n \rangle$ expressed in prolate spheroidal functions ($\lambda(n)$ the prolate eigenvalues). The operator associated with the Weil−Sonine discrepancy is **compact** (an infinitesimal of the quantized calculus).

**Skeleton of the CC proof (verified in the Introduction and §§1–6 of the source; recorded here because it is the mold a proof of 100.A must replicate):**

1. *Geometrization (CC §1).* The local archimedean formula is written $W_\infty(f) = -\frac12 \mathrm{Tr}(\hat f\, u^* \,\textit{đ}u)$, with $u = u_\infty$ the unitary of the Fourier transform composed with the inversion (multiplication by $e^{2i\theta(s)}$, $\theta$ the Riemann–Siegel angular function) and $\textit{đ}u$ its quantized differential. The Schwartz kernel of the scaling action decomposes into two "squares" $\Delta$ (small) and $\Sigma$ (large) of the first quadrant.
2. *Isolation of the obstruction (CC §2).* The obstruction to local positivity is exactly the contribution of the small square $\Delta$; it is isolated in the "trace-remainder" function $\delta(\rho)$, explicitly given by $\delta(\rho) = 2\rho^{1/2}\big(\frac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)} + \frac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\big)$ for $\rho \geq 1$, and the functional $L(f) = D(f) + W_\infty(f)$ with $D(f) = \int f(\rho^{-1})\delta(\rho) d^*\rho$ turns out to be **positive without any support restriction** (CC, Prop. 2.2). All the difficulty is packed into the essential negativity of $D$.
3. *Pole conditions (CC §3).* Imposing $\hat f(\pm i/2) = 0$ amounts to replacing $\delta$ by $Q\delta$ with $Q = -(\rho\partial_\rho)^2 + \frac14$; the jump of $\delta'$ at $\rho = 1$ generates $-2\,\underline{\delta}_1$ and the operator associated with $D \circ Q$ in $L^2(\sqrt I, d^*\rho)$ decomposes as $-2\,\mathrm{Id} + K$ with $K$ compact of Hilbert–Schmidt class: $D$ is essentially negative on a fixed compact support, modulo finitely many linear conditions.
4. *Sonine compression (CC §4).* The identity $\delta(\rho) = \mathrm{Tr}(\vartheta_m(\rho^{-1}) \widehat{\mathcal{P}}_1 \mathcal{P}_1)$ ties the square $\Delta$ to the pair of cutoff projections; the decomposition into irreducible components of the representation of the infinite dihedral group $\mathbb{Z} \rtimes \mathbb{Z}/2$ generated by $(\mathcal{P}_1, \widehat{\mathcal{P}}_1)$ "moves" $\Delta$ into $\Sigma$, leaving as remainder exactly the Sonine space (where the representation is trivial) — hence Theorem 3.
5. *Toeplitz control (CC §§5–6).* The functional $E \circ Q$ associated with $\epsilon(\rho)$ decomposes as $-2\epsilon'(1^+)(\mathrm{Id} - K)$ with $K$ compact; in the window $I = [1/2, 2]$, $\mathbb{R}^*_+$ is discretized by $q^{\mathbb{Z}}$, $q \to 1^+$, $K_q$ is identified as a Toeplitz matrix, one checks that it has **a single eigenvalue $> 1$**, and one conditions on that single (nearest) direction to get $\mathrm{Id} - K > 0$ — hence Theorem 6.11 with $13 < c < 17$. CC note that the step $q \to 1^+$ is aligned with the $\mathbb{F}_q \to \mathbb{F}_1$ philosophy and with the Toeplitz technique used for RH over function fields (Hallouin–Perret 2019).

Step 5 is the **only** step of the proof that is specific to the window $[1/2, 2]$ and that has no analogue today for larger windows; steps 1–4 have a proved or structurally available semilocal counterpart (§2.5).

### 2.4 Answer to question (i): restricted full form or truncated local form?

**Proposition 2.1 (exact coincidence in the window).** Let $f$ have $\mathrm{supp}(f) \subset (1/2, 2)$. Then the full geometric side and the one truncated to the place $\infty$ coincide term by term:
$$\sum_v \mathcal{W}_v(f) = \mathcal{W}_\infty(f),$$
because $f(p^{\pm k}) = 0$ for every prime $p$ and every $k \geq 1$ (the smallest prime power is $2 \notin (1/2,2)$... more precisely $2 \geq 2 > \sup \mathrm{supp}(f)$ when the support is the open interval $(1/2,2)$). $\square$

**Consequence.** The dichotomy of question (i) — "positivity of the FULL Weil form restricted to a subspace, or positivity of a TRUNCATED LOCAL form?" — **dissolves**: in the window $(1/2, 2)$ both things are the same. Theorem 1 of CC is, simultaneously:

- positivity of the program's **full Weil form** $Q$ restricted to the subspace $\{g : \mathrm{supp}\, g \subset [2^{-1/2}, 2^{1/2}],\ \hat g(\text{poles}) = 0\}$ — a genuinely RH-relevant statement (it is the case $n = 2$ of the family $P(n)$ whose totality is equivalent to RH), and
- positivity of the local archimedean term $W_\infty$ on that subspace.

This is exactly what makes it valuable for $\mathbf{C}_D^B$: it is an **unconditional positivity of the global form** on a nontrivial subspace, with a **mechanism** (not an accidental computation): the positivity is the trace of an operator positive by construction ($\vartheta(g)\mathbf{S}\vartheta(g)^* \geq 0$), and everything separating $Q$ from that trace is a compact infinitesimal plus a bounded finite-rank defect ($c < 17$) in a certifiably nonzero direction ($s = 1/2$; $\zeta(1/2) \neq 0$).

### 2.5 The later semilocal infrastructure (verified)

**(a) Quasi-inner functions (CC, *Quasi-inner functions and local factors*, J. Number Theory 226 (2021), 139–167; arXiv:2008.10974).** The product of quotients of local factors over a finite set of places of $\mathbb{Q}$ (including $\infty$) is a function **quasi-inner** to the left of the critical line; the off-diagonal part of multiplication by such a function, in the decomposition $L^2(\text{critical line}) = H^2 \oplus (H^2)^\perp$, is a **compact** operator. CC present this explicitly as *"the analytic prerequisites for treating Weil positivity in the semilocal case"*.

**(b) Stability of the semilocal Sonine space (CCM, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024); arXiv:2310.18423).**

- *Theorem 1 (CCM §4):* for finite $S$ with $\infty \in S$, the canonical transform identifies $L^2(X_S)^{K_S}$ with $L^2(\mathbb{R}, dm_S)$, where the measure is $dm_S(s) = \big|\prod_{v \in S} L_v(\tfrac12 - is)\big|^2 ds$ ($L_v$ the local Euler factors); the dictionary with the archimedean place is multiplication by $\prod_{p \in S \setminus \{\infty\}} L_p(\tfrac12 - is)$.
- *Theorem 2 (CCM §4, textual):* *"Let $S$ be finite with $\infty \in S$ and $\lambda > 0$. Then the map $\theta_S$ induces a Hilbert isomorphism of the Sonine spaces $\theta_S : \mathbf{S}_\lambda(\mathbb{R}, e_\infty) \to \mathbf{S}_\lambda(X_S, \alpha)$."* That is: the positivity reservoir (the Sonine space) **is stable under growth of $S$** — it neither degenerates nor empties out when finite places are added.
- *Status of semilocal positivity in CCM 2024 (textual).* *"We expect that the use of such operatorial tools in the semilocal case opens a path to treating Weil positivity as in [CC 2021]. Indeed, the operatorial aspect of the present work provides a more precise strategy for addressing semilocal Weil positivity, comparing the trace functional associated with the operator — automatically positive for a self-adjoint operator — with the Weil functional."* — That is: for $|S| \geq 2$ the positivity is a **declared strategy, not a theorem**.

**(c) [NOT VERIFIED].** No publication by Connes–Consani(–Moscovici) or by third parties was found, in the searches performed, proving $P(n)$ for any $n > 2$ (that is, semilocal positivity with at least one finite place). It also could not be verified whether Yoshida's (1992) computation covers windows larger than $(1/2, 2)$. Both points are treated as open.

---

## §3. The semilocal Maslov index $\mu_S$: rigorous definition

### 3.1 The filtration of windows

**Definition 3.1 (windows and admissible subspaces).** For real $n \geq 2$:
$$\mathcal{D}_n := \{g \in C_c^\infty(\mathbb{R}^*_+) : \mathrm{supp}(g) \subset [n^{-1/2}, n^{1/2}]\}, \qquad \mathcal{D}_n^0 := \{g \in \mathcal{D}_n : \hat g(0) = \hat g(1) = 0\},$$
where $\hat g$ is the Mellin transform and the conditions $\hat g(0) = \hat g(1) = 0$ are the vanishings at the poles required by the Weil criterion (in CC normalization: vanishing of the multiplicative Fourier transform at $\pm i/2$). Note that $g \in \mathcal{D}_n \Rightarrow \mathrm{supp}(g \star \tilde g) \subset [1/n, n]$.

**Lemma 3.2 (finite arithmetic content of the window).** For $g \in \mathcal{D}_n$, the program's Weil form satisfies:
$$Q(g, g) = \mathcal{Z}[g] - \sum_{p^k \leq n} \frac{\log p}{p^{k/2}} \big[(g \star \tilde g)(p^k) + (g \star \tilde g)(p^{-k})\big] + \mathcal{A}[g],$$
i.e., the prime term involves only the prime powers $p^k \leq n$. In particular, on $\mathcal{D}_n^0$, $Q$ coincides with $-\sum_{v \in S(n)} \mathcal{W}_v(g * \tilde g^\sharp)$, where $S(n) = \{\infty\} \cup \{p : p \leq n\}$.

*Proof.* Immediate from the support: $(g \star \tilde g)(x) = 0$ for $x \notin [1/n, n]$, and the prime powers in $[1/n, n]$ are exactly $\{p^{\pm k} : p^k \leq n\}$. The identification with the semilocal geometric side is the explicit formula with the pole terms killed by the conditions in $\mathcal{D}_n^0$. $\square$

**Definition 3.3 (semilocal form and semilocal Maslov index).** The primary parameter is the window $n$, not the set of places (because different $n$ with the same set of visible primes give different forms — see Obs. 3.6). We define
$$Q_n := Q\big|_{\mathcal{D}_n^0}, \qquad \boxed{\mu(n) := \kappa(Q_n) = \sup\{\dim W : W \subset \mathcal{D}_n^0,\ Q|_W < 0\}}.$$
For finite $S$ of places with $\infty \in S$ of the form $S = S(n)$, we write $\mu_S := \mu(q_S^-) = \sup\{\mu(n) : S(n) = S\}$, where $q_S$ is the smallest prime power whose prime is not in $S$ or that exceeds the corresponding window; $\mu_S$ is a convenience notation for "the index just before the next arithmetic datum enters".

**Lemma 3.4 (monotonicity and exhaustion).** The function $n \mapsto \mu(n)$ is monotone non-decreasing, and
$$\kappa\big(Q|_{\{g \in C_c^\infty:\ \hat g(0) = \hat g(1) = 0\}}\big) = \lim_{n \to \infty} \mu(n) = \sup_n \mu(n).$$

*Proof.* Monotonicity: $\mathcal{D}_n^0 \subset \mathcal{D}_{n'}^0$ for $n \leq n'$, and the negative index of a restriction does not exceed that of the ambient form. Exhaustion: if $W \subset C_c^\infty$ is a finite-dimensional subspace of dimension $k$ with $Q|_W < 0$ and the pole conditions, take a basis $g_1, \ldots, g_k$; the union of their supports is compact in $\mathbb{R}^*_+$, hence contained in $[n^{-1/2}, n^{1/2}]$ for some finite $n$; then $W \subset \mathcal{D}_n^0$ and $\mu(n) \geq k$. Conversely each $\mu(n) \leq \kappa$. $\square$

**Remark 3.5 (the index with and without pole conditions).** The program's index $\kappa(Q)$ is defined on $\mathcal{S}(\mathbb{R}^*_+)$ without conditions (Doc 91, Def. 1.5). If $W$ is negative of dimension $k$ without conditions, $W \cap \{\hat g(0) = \hat g(1) = 0\}$ is negative of dimension $\geq k - 2$. Hence the index with conditions differs from that of $\kappa(Q)$ by at most 2, and under Hypothesis D both detect the same off-critical zeros: the chain RH $\iff \kappa(Q) = 0 \iff \mu(n) = 0\ \forall n$ is valid (the last equivalence is Lemma 3.4 plus CC's criterion (2), which is formulated exactly on the subspace with conditions). In particular:

$$\boxed{\mathrm{RH} \iff \mu(n) = 0 \text{ for every } n \geq 2 \iff \text{CCM's family } P(n) \text{ holds for every } n.}$$

**Remark 3.6 (densification within a fixed $S$).** Between two consecutive prime powers, $\mu(n)$ can in principle grow (the domain grows and the archimedean term sees the larger window) without new primes entering. The fine filtration is by continuous $n$; indexing by $S$ is the "by places" reading. This already shows that the arithmetic of the filtration is not purely "one prime per step": the powers $4 = 2^2, 8 = 2^3, 9 = 3^2, \ldots$ refine the steps of the same place.

### 3.2 Reading as spectral flow (path of forms and crossings)

**Construction 3.7 (the path of forms on a fixed space).** Let $V_\tau$, $\tau \geq 1$, be the Mellin rescaling $(V_\tau g)(x) := g(x^{1/\tau})$, satisfying $\widehat{V_\tau g}(s) = \tau\, \hat g(\tau s)$ and mapping $\mathcal{D}_2 \to \mathcal{D}_{2^\tau}$ bijectively. The pullback $Q^{(\tau)} := Q(V_\tau \cdot, V_\tau \cdot)$ is a path of Hermitian forms on the fixed space $\mathcal{D}_2$, with $\kappa(Q^{(\tau)}) = \mu(2^\tau)$ modulo the adjustment of the pole conditions (the vanishing $\hat g(1) = 0$ is not $V_\tau$-invariant: $\widehat{V_\tau g}(1) = \tau \hat g(\tau)$; the two conditions transport into two linear conditions that move with $\tau$). The **semilocal Maslov index as spectral flow** is the net crossing count at zero of the eigenvalues of the form operators associated with $Q^{(\tau)}$ along $\tau \in [1, T]$, in the sense of Robbin–Salamon (*The Maslov index for paths*, Topology 32 (1993), 827–844), applied to the symplectic realification of Construction 3.4 of Doc 96.

**Definition 3.7-bis (crossing form, Robbin–Salamon sense).** If $\tau_0$ is an instant with $N_{\tau_0} := \ker Q^{(\tau_0)} \neq 0$ (crossing), the **crossing form** is the Hermitian form on $N_{\tau_0}$:
$$\Gamma(\tau_0)[u] := \frac{d}{d\tau}\Big|_{\tau = \tau_0} Q^{(\tau)}(u, u), \qquad u \in N_{\tau_0}.$$
The crossing is **regular** if $\Gamma(\tau_0)$ is non-degenerate, and its contribution to the Maslov index of the path is $\mathrm{sign}\,\Gamma(\tau_0)$ (Robbin–Salamon 1993, Theorem 2.3 in the finite-dimensional case). In our context, the derivative $\frac{d}{d\tau} Q^{(\tau)}(u,u)$ has a concrete expression: differentiating the window produces (i) the archimedean boundary term (derivative of the principal value of $\mathcal{W}_\infty$ against the dilation, computable from the gamma factor) and (ii) arithmetic Dirac terms $-\frac{\log p}{p^{k/2}}\big[\delta(\text{entry of } p^k)\big]$ each time a prime power crosses the boundary $x = n^{\pm 1}$ of the window: **the derivative of the path of forms is exactly the sequential entry of the arithmetic data**. This is the precise version, within the program, of the intuition in Doc 96 (Obs. 3.11) that the Maslov index "might decompose by places": it is not the index that decomposes — it is the *derivative of the path*.

**GAP 3.8 (declared).** Construction 3.7 requires, to be a genuine spectral flow: (a) a reference Hilbert completion of $\mathcal{D}_2$ in which each $Q^{(\tau)}$ is representable by a bounded (or relatively bounded) self-adjoint operator — the natural candidate is $L^2(\sqrt{I}, d^*\rho)$ used by CC in their Toeplitz analysis, but the representability of the $\mathcal{Z}$ part is not established; (b) regularity of the path $\tau \mapsto Q^{(\tau)}$ (norm continuity of the forms; the Dirac terms of 3.7-bis break it at the arithmetic instants, where one would have to work with regularized jumps); (c) non-degeneracy of the crossing forms. None of the three points is established in general in the program; in the toy model of Doc 98 (§7), (a)–(c) were verified by hand for the crossing of the quadruple and the resulting flow was $= -2 = -\kappa$. **For this document, the operative definition of $\mu(n)$ is that of Definition 3.3 (index of the restriction), which is unconditionally rigorous; the spectral-flow reading is interpretive until GAP 3.8 is closed.**

**Table 3.9 (the first steps of the filtration).** Order of entry of the arithmetic data into the window $[1/n, n]$:

| range of $n$ | visible powers | $S(n)$ | weight of the entering term |
|---|---|---|---|
| $[1, 2)$ | none | $\{\infty\}$ | — (purely archimedean window) |
| $[2, 3)$ | $2$ | $\{\infty, 2\}$ | $\log 2 / \sqrt{2}$ |
| $[3, 4)$ | $2, 3$ | $\{\infty, 2, 3\}$ | $\log 3 / \sqrt{3}$ |
| $[4, 5)$ | $2, 3, 4$ | $\{\infty, 2, 3\}$ | $\log 2 / 2$ (power $2^2$, same place) |
| $[5, 7)$ | $2, 3, 4, 5$ | $\{\infty, 2, 3, 5\}$ | $\log 5 / \sqrt{5}$ |
| $[7, 8)$ | $\ldots, 7$ | $\{\infty, 2, 3, 5, 7\}$ | $\log 7 / \sqrt{7}$ |
| $[8, 9)$ | $\ldots, 8$ | same | $\log 2 / 2\sqrt{2}$ (power $2^3$) |

$\mu(2) = 0$ is Theorem 4.1; everything below that in the left column is open territory. The row $[2,3)$ is Conjecture 100.A (§6.2).

**Remark 3.10 (where an off-critical zero crosses).** If $\rho_0 = 1/2 + b + i\gamma$ is an off-critical zero, Lemma 3.4 guarantees that there is a finite threshold $n(\rho_0) := \min\{n : \mu(n) \geq 1\} < \infty$: the negative direction associated with $\rho_0$ (Doc 91, Prop. 1.6) **enters the filtration at finite scale**. The Maslov structure thus localizes the negation of RH into crossing events at finite scale. No effective upper bound for $n(\rho_0)$ in terms of $(b, \gamma)$ is known; we formulate it as a question:

**Question 100.Q1 (effective crossing threshold).** Is there an explicit function $N(b, \gamma)$ such that every off-critical zero $\rho = 1/2 + b + i\gamma$ forces $\mu(N(b,\gamma)) \geq 1$? An affirmative answer would turn every proved $P(n)$ into an **effective exclusion region** for off-critical zeros (analogous to the numerical verifications up to height $T$, but in the conjugate variable). Status: open; not even the qualitative shape of $N$ is known.

---

## §4. Does CC's positivity imply $\mu_S = 0$? (question iii)

### 4.1 The base case: theorem

**Theorem 4.1 ($\mu_{\{\infty\}} = 0$, unconditional).** $\mu(n) = 0$ for every $n \leq 2$. That is: the program's full Weil form is positive semidefinite on $\mathcal{D}_2^0$.

*Proof.* Let $g \in \mathcal{D}_2^0$. By Lemma 3.2 with $n = 2$ and support in the open set: if $\mathrm{supp}(g) \subset (2^{-1/2}, 2^{1/2})$, then $\mathrm{supp}(g \star \tilde g) \subset (1/2, 2)$ and there are no prime terms; $Q(g,g) = -\mathcal{W}_\infty(g * \tilde g^\sharp) = W_\infty(g * g^*) \geq 0$ by the archimedean Weil inequality (Yoshida 1992; statement verified in CC 2021, p. 2, with the vanishing conditions at $\pm i/2$ that are exactly those of $\mathcal{D}_2^0$). The closed-support case is obtained by approximation (the boundary evaluations $f(2), f(1/2)$ are controlled by continuity with cutoff functions; the boundary points have vanishing limit contribution for interior approximations). If there existed $W \subset \mathcal{D}_2^0$ with $Q|_W < 0$, any $g \in W \setminus \{0\}$ would violate the above. $\square$

**Remark 4.2 (what CC's mechanism proves and what Yoshida proves).** Yoshida's proof is an explicit computation; it covers all of $\mathcal{D}_2^0$. CC's operatorial proof (Theorem 1) additionally requires $\hat g(1/2) = 0$ (vanishing of the Fourier transform at $0$, i.e. Mellin at the center $s = 1/2$); without that condition, their Theorem 6.11 leaves the defect $-c|\hat g(0)|^2$ with $13 < c < 17$. By the codimension argument (as in Obs. 3.5), the CC mechanism alone gives $\mu(2) \leq 1$; combined with Yoshida, $\mu(2) = 0$. The point $s = 1/2$ is certifiably nonzero ($\zeta(1/2) \neq 0$, a known value), so the conditioning is legitimate in criterion (2).

### 4.2 The trap of question (iii), answered

**Yes, $\mu_{\{\infty\}} = 0$ follows trivially from positivity** (a subspace where the form is $\geq 0$ has negative index $0$; there is no additional logical content). The nontrivial content lies elsewhere, and it is worth separating it precisely:

**(a) Content of the theorem itself.** $P(2)$ is the first link in a family whose totality is RH. A single link bounds no zero (an off-critical zero of enormous imaginary part presumably has an enormous crossing threshold $n(\rho_0)$). Direct value for $\kappa$: nil. This must be said without euphemism.

**(b) Content of the mechanism (what matters for $\mathbf{C}_D^B$).** CC's structural identity:
$$Q_n(g,g) = \underbrace{\mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*)}_{\geq\, 0 \text{ by construction}} + \underbrace{\big(\text{discrepancy}\big)}_{\text{compact infinitesimal} + \text{conditionable finite rank}}$$
realizes positivity as the **trace of the scaling action compressed to the Sonine space** — an object defined without any reference to the zeros of $\zeta$. This is exactly the type of "local vanishing mechanism with a chance of propagating" that question (iii) asked for, for three verified reasons:

1. The Sonine compression exists **for every finite $S$** and is stable: CCM 2024, Theorem 2 ($\theta_S$ a Hilbert isomorphism of Sonine spaces). The positivity reservoir does not run out as places are added.
2. The semilocal spectral dictionary is canonical: the measure $dm_S = |\prod_{v \in S} L_v(\tfrac12 - is)|^2 ds$ (CCM 2024, Theorem 1) — the Euler factors of $S$ enter as a **spectral weight**, not as an infinite product; MW-2 is not invoked.
3. The analytic prerequisites for compactness with $|S| \geq 2$ are proved: CC's quasi-inner functions (JNT 2021) give that the off-diagonal obstruction of the local factors is compact — the semilocal analogue of "the discrepancy is an infinitesimal".

**(c) What the mechanism does NOT yet give.** The piece that closes the proof in the case $S = \{\infty\}$ — the quantitative Toeplitz control of the discrepancy, with its finite-rank defect $c < 17$ and its single conditioning direction — **has no proved analogue for any $S$ with a finite place** [NOT VERIFIED whether one exists; CCM 2024 declares it a strategy]. The by-construction positivity of the compressed trace is free in every $S$; the statement with content is that *Weil $\geq$ Sonine modulo legitimate finite conditioning*, and that is proved only in the window $(1/2, 2)$.

### 4.3 The CC mechanism against Obstacle $\mathbf{O}_D$ (Doc 96, §8.1)

Obstacle $\mathbf{O}_D$ states: any condition on $H_C$ implying $\kappa = 0$ requires information about the positions of the zeros, not derivable from functional equation + Euler product + growth. How does this coexist with Theorem 4.1, which proves a genuine positivity of $Q$ without any information about zeros?

**Analysis.** There is no contradiction, and the exact boundary is instructive:

1. Theorem 4.1 does not imply $\kappa = 0$: it implies $\mu(2) = 0$, and $\kappa = \sup_n \mu(n)$ (Lemma 3.4). $\mathbf{O}_D$ forbids the global conclusion, not the windowed one. The CC exception delimits the scope of $\mathbf{O}_D$ **from inside**: the boundary of the obstacle does not run between "global properties" and "zero positions," as the formulation of Doc 96 suggested, but between **windows with no prime mass** ($n \leq 2$: positivity provable by pure analysis) and **windows with prime mass** ($n > 2$: each step requires arithmetic cancellation). This reformulation of $\mathbf{O}_D$ is strictly more precise than that of Doc 96 and should replace it in the program's wall map.

2. The inputs of the CC mechanism are: harmonic analysis in $L^2(\mathbb{R})^{\mathrm{ev}}$, the pair of cutoff projections, prolate functions (Slepian–Pollak), Toeplitz theory, and the **certified non-vanishing of $\zeta$ at one point** ($s = 1/2$). None of these touches zero positions. But the output also scrupulously respects the limit of $\mathbf{O}_D$: CC's Corollary 2 says that the Sonine trace requires, besides the zeros, an extra contribution on the critical line ("as if $\zeta$ were multiplied by $(z - 1/2)^{17}$") — the mechanism "sees" the zeros only as a family of evaluations $\sum_{s \in Z} |\hat g(s)|^2$, never individually.

3. There is a genuinely new point relative to the diagnosis of Doc 96 (Conclusions, item on the Euler product): Lemma 2.8 of Doc 96 showed that positivity **does not** follow from the absence of zeros in the Euler region (subspace $\mathcal{H}_{>1}$, spectral support in $\mathrm{Re}(s) > 1$). Theorem 4.1 shows that it does follow in the dual subspace (**physical** support in the window $(1/2,2)$, with no spectral restriction). The asymmetry is exact: localizing in the Mellin variable (Doc 96, Angle 2) does not control the prime term, which is a sum of physical evaluations; localizing in the physical variable (CC) annihilates it. The retrospective lesson for the program: Angle 2 of Doc 96 chose the wrong side of the transform.

**Conclusion of §4.** CC's positivity implies $\mu_{\{\infty\}} = 0$ (trivially, Theorem 4.1); the new content for the program is not that vanishing index but (a) the **positive-trace + infinitesimal decomposition**, available as a proved skeleton at every level $S$ of the filtration and lacking only the quantitative estimator per level, and (b) the **redelimitation of Obstacle $\mathbf{O}_D$** (§4.3, point 1): the boundary of the obstacle is the prime mass of the window, not the global/local dichotomy. The program's question becomes: is the estimator uniformizable in $n$? That is the obstruction of §5.

---

## §5. The exact obstruction to $S \to$ all places (question iv)

### 5.1 Verification of the critical technical point: the space of test functions does NOT shrink

The proposal of this exploration conjectured that "CC's space of test functions shrinks as $S$ grows" as a possible obstruction. **Verification gives the opposite.** Textually:

- CC 2021 (Introduction): semilocal positivity is sought *"for functions $f$ satisfying the support condition $\mathrm{Supp}(f) \subset (p^{-1}, p)$"* for the set of places $\{\infty, 2, 3, \ldots, p\}$: the allowed support **grows** with $S$.
- CCM 2024 (Introduction): $Q_n$ is defined on functions *"with support in the compact symmetric interval $[\frac1n, n]$"*, and RH is equivalent to the validity of $P(n)$ **for all** $n$: the filtration is increasing and exhausts $C_c^\infty(\mathbb{R}^*_+)$ (our Lemma 3.4).

The direction of the statement is the opposite of the feared one, and it is the good one: if the space shrank, the family of semilocal positivities could not be equivalent to RH. That version of the obstacle is thereby refuted. The real obstruction has a different structure, which we now formulate.

### 5.2 Obstacle $\mathbf{O}_{SL}$

**Obstacle $\mathbf{O}_{SL}$ (three components).** Extending the CC theorem from $S = \{\infty\}$ to the full family $\{P(n) : n \geq 2\}$ faces exactly the following:

**$\mathbf{O}_{SL}$.1 (growing prime load in the window — MW-4 by windows).** On $\mathcal{D}_n^0$, the form is $Q_n = \mathcal{A}_n - \mathcal{P}_n$ (with no $\mathcal{Z}$ term on the geometric side). The gross size of the prime term in the window is quantified:

**Lemma 5.0 (prime mass of the window).** $\displaystyle M(n) := \sum_{p^k \leq n} \frac{\log p}{p^{k/2}} = (2 + o(1))\sqrt{n}, \qquad n \to \infty.$

*Proof.* $M(n) = \sum_{m \leq n} \Lambda(m) m^{-1/2}$ with $\Lambda$ the von Mangoldt function. By partial summation with $\psi(x) = \sum_{m \leq x} \Lambda(m)$:
$$M(n) = \frac{\psi(n)}{\sqrt n} + \frac{1}{2}\int_2^n \frac{\psi(t)}{t^{3/2}}\, dt,$$
and the prime number theorem $\psi(t) = (1 + o(1))t$ (in fact Chebyshev suffices for the order) gives $M(n) = (1 + o(1))\sqrt n + (1 + o(1))\int_2^n \tfrac{dt}{2\sqrt t} \cdot \ldots = (1+o(1))\sqrt n + (1 + o(1))(\sqrt n - \sqrt 2) = (2 + o(1))\sqrt n$. $\square$

Against this, the archimedean term on the same window grows like $\log n$ (the weight $\Omega(s) \sim \frac12 \log |s|$ of Doc 91, Prop. 4.4, integrated against band functions $\sim \log n$). The positivity of $Q_n$ for large $n$ therefore requires the oscillatory cancellation of the signs of $(g \star \tilde g)(p^k)$ to reduce the effective prime contribution from $\sqrt n$ to $O(\log n)$ — which is the arithmetic content of RH in the window. **The semilocal framework does not dissolve the $\sqrt{N}$ vs $\log N$ barrier (Doc 91, Prop. 4.5): it slices it.** Each $P(n)$ is a statement with finite arithmetic data (the $p^k \leq n$) plus the archimedean place; the full barrier reappears as divergence of the imbalance as one runs through the family. What changes — and it is not little — is the logical type of the problem: from a single global positivity to a countable sequence of positivities, each with finite arithmetic content. In the base case $n = 2$ one has $M(2) = \log 2/\sqrt 2$ but the open window excludes it: $M(2^-) = 0$ — the positivity proved by CC lives in the only window with **exactly zero** prime mass. This observation is the seed of the pessimistic scenario of §6.2.

**$\mathbf{O}_{SL}$.2 (non-uniformity of the discrepancy control — the heart of the obstacle).** CC's proof scheme at each level is: $Q_n = T_n + R_n$, with $T_n = \mathrm{Tr}(\vartheta(g)\mathbf{S}_n \vartheta(g)^*) \geq 0$ canonical (and $\mathbf{S}_n$ stable in $n$, CCM Theorem 2) and $R_n$ the discrepancy. At $n = 2$, $R_n$ was controlled with: (i) compactness (CC Theorem 3), (ii) Toeplitz analysis in the limit $q \to 1^+$, (iii) a finite-rank defect with constant $13 < c < 17$ and **one** conditioning direction. There is no analogue of (ii)–(iii) for any $n > 2$, and no principle controlling the growth in $n$ of:
$$c(n) := \text{optimal finite-rank defect}, \qquad d(n) := \text{number of conditioning directions needed}.$$
If $d(n)$ grows without control (for example, proportionally to the number of "visible" zeros at resolution $\log n$ of the window, which grows like $e^{c\sqrt{\cdot}}$... there is not even a quantitative conjecture in the literature), the method produces positivity only on subspaces of growing codimension, which does **not** imply $\mu(n) = 0$ but only $\mu(n) \leq d(n)$ — a bound that does not tend to $0$. The frank comparison: $\mu(n) \leq d(n)$ with $d(n) \to \infty$ would have exactly the same status as C5/$a_{\mathrm{tail}}$ of Doc 91: correct structure, constant stuck at the useless threshold.

**$\mathbf{O}_{SL}$.3 (arithmetic legitimacy of the conditioning).** CC's criterion (2) only allows imposing vanishings $\hat g|_F = 0$ with $F \cap Z = \emptyset$: each conditioning direction must be certified as a **non-zero of $\zeta$**. At $n = 2$ the direction is $s = 1/2$ and $\zeta(1/2) \neq 0$ is a verified fact. For general $n$, the conditioning directions are dictated by the spectrum of the limiting Toeplitz operator — an analytic datum not chosen by the prover — and there is no a priori guarantee that they correspond to certifiable points. However, this component is **structurally weaker** than the program's walls: the non-vanishing of $\zeta$ at a given point outside the zeros is verifiable (it is a strict inequality at a concrete value, decidable numerically with rigorous error), unlike the "positions of all the zeros" information that blocks routes C1–C4 (Doc 91). $\mathbf{O}_{SL}$.3 introduces a dependence on finite pointwise verifications per level — annoying, not fatal.

**Synthetic statement of the obstacle.** *The semilocal strategy reduces RH to the countable family $\{P(n)\}$ with $P(2)$ proved. The Sonine mechanism provides at each level a decomposition with a stable canonical positive part (CCM 2024) and compact discrepancy (CC JNT 2021), but the quantitative control of the discrepancy — the only step that decides positivity — is proved only at $n = 2$, is unknown for any $n > 2$, and no mechanism of uniformity in $n$ exists; the part of the discrepancy that grows with $n$ is exactly the prime term of amplitude $\sqrt{n}$ against $\log n$ for the archimedean one. The obstruction is of quantitative-uniform type (a sequence of constants to be controlled), not of structural-algebraic type (no object is missing).*

### 5.3 Is it the same obstruction as MW-2 / Phase 27? No — and the difference is informative

**Proposition 5.1 (the semilocal obstruction is disjoint from that of Phase 27).** The obstruction of Phase 27 (Proposition 27-C.1, Wall A) is: the **zero** term $\mathcal{Z}[f] = \sum_\rho \hat f(\rho)$ admits no decomposition $\sum_v \mathcal{Z}_v$ by places; factoring $Q$ on the spectral side requires the nonexistent arithmetic cohomology (MW-5). The semilocal strategy **never decomposes the zero side**: it works exclusively with the geometric side of the explicit formula, which is additive by places **unconditionally** (it is a sum $\sum_v \mathcal{W}_v$ term by term — the same fact that Phase 27 recorded as "the prime term DOES factor"), and localizes by **support of the test function**, not by factorization of the functional. Consequently:

- MW-2 (Euler product only in $\mathrm{Re}(s) > 1$) is not invoked: the Euler factors of $S$ enter as finite algebraic data (the weight $|\prod_{v \in S} L_v|^2$ on the critical line, CCM Theorem 1), with no infinite product or continuation.
- MW-3 (no infinite-dimensional Hasse–Minkowski) is not invoked: there is no local-to-global step of positivities; there is **exhaustion** (Lemma 3.4): global positivity is the supremum of the window positivities, not their product.
- MW-5 is not invoked: no factorization of $Q$ is postulated.

The price of avoiding the three walls is $\mathbf{O}_{SL}$.1–2: uniformity in the window. $\square$ (the proposition is a comparison of definitions; its content is the following table)

| | Phase 27 (factorization) | Semilocal (filtration) |
|---|---|---|
| Decomposed object | $Q$ as a whole (spectral side) | domain of $Q$ (support windows) |
| What factors | requires $\mathcal{Z} = \sum_v \mathcal{Z}_v$: **FALSE** (27-C.1) | geometric side $\sum_v \mathcal{W}_v$: **trivially true** |
| Critical step | local $\Rightarrow$ global (MW-3/MW-5) | uniformity in $n$ of constants ($\mathbf{O}_{SL}$.2) |
| Status of the base case | no base case | $P(2)$ **proved** (Yoshida/CC) |
| Type of obstruction | structural (object missing) | quantitative (bounds missing) |

**Remark 5.2 (what this teaches about $\mathbf{C}_D$).** Doc 96 (Conjecture $\mathbf{C}_D$, frank assessment) flagged point (iii) as most questionable: "the non-vanishing of the local factor does not imply that the local contribution to the Maslov index is zero." The semilocal analysis confirms and sharpens this: there is no "local contribution to the index" because the index is not additive by places (the negativity of $Q_n$ is an interference phenomenon between the archimedean term and **all** the primes of the window at once). What does exist, and is the correct substitute, are the **filtration increments** $\mu(n') - \mu(n) \geq 0$.

---

## §6. Consequences for $\mathbf{C}_D^B$ and the intermediate falsifiable statement (question v)

### 6.1 Reformulation of $\mathbf{C}_D^B$: from local sum to filtration

**What the semilocal case refutes in the original formulation.** $\mathbf{C}_D$ (Doc 96, §8.2) postulated $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p$ with $\mu_p = 0$ by the non-vanishing of the local factor. That additivity presupposes a decomposition by places of the object whose index is being measured, i.e., the factorization that Phase 27 refuted for the zero side. In the only rigorous realization available (the semilocal one), the index **does not decompose**: it is filtered.

**What the semilocal case confirms of the pattern.** The pattern "vanishing local contributions" survives in the form of increments: RH $\iff$ all increments of the filtration are zero, and the **base increment** (from the empty window to the window $(1/2,2)$, purely archimedean) **is zero by theorem**. It is the first component of $\mathbf{C}_D^B$ to move from conjecture to theorem, in the corrected formulation:

**Conjecture $\mathbf{C}_D^{SL}$ (filtered reformulation of $\mathbf{C}_D^B$).** For every $n \geq 2$: $\mu(n) = 0$. Equivalently (Lemma 3.4 + CC criterion): RH. Fine structure: $\mu(2) = 0$ [**THEOREM** — Theorem 4.1]; for each prime power $q$, the increment when the window passes $q$ is zero [OPEN for every $q \geq 2$].

Note the frankness of the equivalence: $\mathbf{C}_D^{SL}$ **is** RH, not a weaker statement. Its value is not logical but structural: it isolates the first unproved increment as a self-contained statement with all objects defined and a candidate proof mechanism (CC's) whose semilocal infrastructure already exists.

### 6.2 The first falsifiable step

**Conjecture 100.A ($\mu_{\{\infty, 2\}} = 0$; the case $P(n)$, $2 < n \leq 3$).** For every $g \in C_c^\infty(\mathbb{R}^*_+)$ with $\mathrm{supp}(g) \subset (3^{-1/2}, 3^{1/2})$ and $\hat g(0) = \hat g(1) = 0$ (Mellin at the poles), one has
$$W_\infty(g * g^*) \;\geq\; \frac{\log 2}{\sqrt{2}} \Big[ (g \star \tilde g)(2) + (g \star \tilde g)(1/2) \Big],$$
i.e. $Q(g, g) \geq 0$, where the right-hand side is the **only** prime term visible in the window $(1/3, 3)$ (the only prime power in $(1, 3)$ is $2$; note $4 = 2^2 > 3$ and $3 \notin (1/3,3)$ open). Conditioned admissible version (CC-style): the same inequality modulo additional vanishings $\hat g|_{F'} = 0$ with $F'$ an explicit finite set of certified non-zeros of $\zeta$.

**Status.** Open. [NOT VERIFIED that a published proof exists; CCM 2024 declares semilocal positivity a strategy.] It is the smallest falsifiable statement distinguishing the semilocal route from a repetition of the archimedean case:

- If it is **true and provable with the CC mechanism** (Sonine compression in $L^2(X_{\{\infty,2\}})$, measure $|L_2 L_\infty|^2 ds$, compact discrepancy via quasi-inner functions, Toeplitz control with finite defect): the pattern of $\mathbf{C}_D^{SL}$ is confirmed at the first increment with genuine arithmetic content (a real prime interfering with the archimedean term), and the question shifts to uniformity ($\mathbf{O}_{SL}$.2) with new data: the behavior of $c(n), d(n)$ at the first step.
- If it is **false**: $\zeta$ has an off-critical zero with crossing threshold $n(\rho) \leq 3$ — RH is false, with a detectable violation in the window $(1/3, 3)$. (No one expects this; the point is that the conjecture has immediate empirical content.)
- If it is **true but the CC mechanism does not reach it** (for example, if the conditioning defect already explodes with one prime): one learns that the archimedean exception to MW-4 was a prime-free-window phenomenon — i.e., that the positivity proved by CC lived precisely in the fact that in $(1/2,2)$ **there is no arithmetic** — and the semilocal route to $\mathbf{C}_D^B$ is severely degraded. This is the scenario the program must be able to detect: Conjecture 100.A is the experiment that decides it.

**Remark 6.1 (what canNOT be done numerically in this program).** The rule of the document excludes numerical exploration; but it is recorded that the third scenario is in principle decidable by pure operatorial methods: the analogue of CC's operator $K$ of §6 in the window $(1/3,3)$ is a concrete Toeplitz object whose norm decides the matter. Its analysis is the technical content of the "first step."

**Program 100.B (attack on Conjecture 100.A by the CC mold; steps with their unknowns).** Following the skeleton of §2.3 with $S = \{\infty, 2\}$:

- **(B1) Framework.** $X_S = (\mathbb{R} \times \mathbb{Q}_2)/2^{\mathbb{Z}}$ (with $\Gamma = \{\pm 2^k\}$), $L^2(X_S)^{K_S} \cong L^2(\mathbb{R}, dm_S)$ with $dm_S(s) = |L_2(\tfrac12 - is)|^2\, |L_\infty(\tfrac12 - is)|^2\, ds$, $L_2(z) = (1 - 2^{-z})^{-1}$, $L_\infty(z) = \pi^{-z/2}\Gamma(z/2)$ (CCM 2024, Theorem 1). *Proved.*
- **(B2) Reservoir.** Semilocal Sonine space $\mathbf{S}_\lambda(X_S, \alpha) \cong \mathbf{S}_\lambda(\mathbb{R}, e_\infty)$ (CCM 2024, Theorem 2): the compression $\mathrm{Tr}(\vartheta_S(g)\, \mathbf{S}_S\, \vartheta_S(g)^*) \geq 0$ exists and is positive by construction. *Proved.*
- **(B3) Discrepancy.** Define $\epsilon_S(\rho)$ by the identity $\mathrm{Tr}(\vartheta_S(f)\mathbf{S}_S) = (W_\infty + W_2)(f) + \int f \epsilon_S\, d^*\rho$ and prove that the associated operator is compact. Available input: the quasi-innerness of $L_2 \cdot L_\infty$ quotients with compact off-diagonal obstruction (CC JNT 2021). *Structurally available; the semilocal trace identity analogous to CC's Theorem 3 is not written in the literature.* GAP.
- **(B4) Poles and jump.** Analogue of $Q\delta$: the weight $|L_2|^2$ is smooth and periodic in $s$ (period $2\pi/\log 2$); the jump at $\rho = 1$ of the archimedean term should persist and the new arithmetic jumps appear at $\rho = 2^{\pm 1}$ — exactly the points where Table 3.9 records the entry of the datum $\log 2/\sqrt 2$. *Not written; it is a concrete principal-value computation.* GAP.
- **(B5) Toeplitz on $(1/3, 3)$.** The analogue of $K_q$ acquires, besides the archimedean symbol, a structural rank term coming from $W_2$ (a cosine in the variable $s \log 2$, from the periodicity of the local factor). Decisive questions: how many eigenvalues $> 1$? Do the conditioning directions correspond to certifiable non-zeros? *Completely open; it is the unknown $d(3)$ of Obstacle $\mathbf{O}_{SL}$.2.* Central GAP.

Program 100.B is not a proof nor a proof sketch: it is the exhaustive list of what is missing, separated into proved / available / GAP. If (B3)–(B5) are closed, Conjecture 100.A is proved and the pattern of $\mathbf{C}_D^{SL}$ is confirmed at its first arithmetic increment. If (B5) closes negatively (proliferation of non-certifiable directions), the third scenario of §6.2 is established.

### 6.3 By-products for the other pieces of Direction B

**(a) For Theorem 8.1 of Doc 96 (localization of the index in $\mathcal{K}_{\mathrm{off}}$).** The filtration $\mu(n)$ is compatible with the decomposition $\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}}$: under Hypothesis D, the negative directions live in $\mathcal{K}_{\mathrm{off}}$ (dimension $2m$) and each has a finite entry threshold in the filtration (Obs. 3.10). The pair (Theorem 8.1, Lemma 3.4) gives: $\kappa = \lim \mu(n)$ with all crossings produced by $\mathcal{K}_{\mathrm{off}}$ — the Maslov picture of Doc 96 (Conjecture 3.10) is partially realized: not as the conjectural identity $\mu = 2\kappa$ for a family of Lagrangians $\{L_\theta\}$, but as a **proved** identity of an index filtration (Lemma 3.4), which is poorer (it is not a topological invariant of a closed path) but unconditional.

**(b) For V.1 (P35).** In CCM's semilocal framework the scaling action is unitary on $L^2(X_S)$ and the semilocal trace formula is a theorem: the pathology of V.1 (does $Q(U_\lambda f, U_\lambda g) = Q(f,g)$?) does not appear **within a fixed window** because there $Q$ is computed by the explicit formula against the semilocal geometric side, and the scaling action moves the window ($U_\lambda \mathcal{D}_n \neq \mathcal{D}_n$). This suggests that the correct version of V.1 is *filtered*: invariance of the family $\{Q_n\}$ under the rescaling $V_\tau$ of Construction 3.7, not invariance of each $Q_n$ under $U_\lambda$. This is not developed here; it is recorded as a direction for closing V.1.

**(c) For C5/$a_{\mathrm{tail}}$ (Docs 91, 94).** The semilocal filtration and the prime tail are dual: C5 cuts the **large** primes off the global form; the semilocal window cuts the large primes **by support**. The decisive difference: the window cuts exactly (Lemma 3.2: zero contribution, not small), which is why the semilocal base case is a theorem while C5 remained stuck at the threshold $a_{\mathrm{tail}} = 1$. The cost is paid at the other end: C5 attempted a single global statement; the filtration needs infinitely many statements.

**(d) For Proposal 7.2 of Doc 96 (twisting by local factors).** Doc 96 (§7.2) proposed studying the local-factor quotients $\Theta_p(z) = (1 - p^{-1/2 - z})/(1 - p^{-1/2 + z})$, observed that $|\Theta_p(it)| = 1$ on the line but that $|\Theta_p(\sigma + it)|$ is not trivial for $\sigma \neq 0$, and left the computation unfinished (Lemma 7.3, marked "the computation gets complicated"). Verification against the literature closes that thread: the correct object is exactly the one CC study in *Quasi-inner functions and local factors* (JNT 2021) — the products of $\prod_{v \in S} L_v$-quotients are **quasi-inner to the left of the critical line**, and the part they lack to be inner (the obstruction to strict contractivity that Doc 96 sought for the dissipativity of Angle 1) is a **compact operator**. That is: twisting by local factors does not produce dissipativity (Doc 96, Corollary 1.13, still stands) but it does produce *compactness of the discrepancy*, which is precisely the input the semilocal mechanism needs. Proposal 7.2 of Doc 96 is thus absorbed — with improvement — by the route of this document.

**(e) On the final remark of Doc 96 (Obs. 7.4).** Doc 96 observed that $|\Theta| = 1$ globally is "a cancellation result among the local factors, not a property of each factor." The semilocal framework gives the correct quantitative version of that intuition: in CCM's measure $dm_S = |\prod_{v \in S} L_v(\tfrac12 - is)|^2 ds$, the local factors enter as a weight of the Hilbert space, and as $S$ grows the weight converges (formally) to $|\zeta_{\text{complete}}|^2$ on the line — global cancellation is the limit of well-defined semilocal weights. No convergence statement is used in this document (the limit is exactly what is out of reach, $\mathbf{O}_{SL}$.2); the structural coherence is recorded.

---

## §7. VERDICT

**PARTIAL.**

**Precise reason, in four clauses:**

1. **What is proved (alive).** The first link of the route is an unconditional theorem external to the program and verified in source: the full Weil form is positive on the window $(1/2, 2)$ ($\mu_{\{\infty\}} = 0$; Yoshida 1992, Connes–Consani mechanism, Selecta Math. 2021), and it constitutes the only proved exception to the MW-4 pattern known to the program. The infrastructure for the subsequent links exists and is proved: stability of the semilocal Sonine space for every finite $S$ (CCM, Ann. Funct. Anal. 2024, Theorem 2), spectral dictionary with weight $|\prod_{v\in S} L_v|^2$ (ibid., Theorem 1), compactness of the local-factor obstruction (CC, J. Number Theory 2021). The filtered reformulation $\mathbf{C}_D^{SL}$ corrects the additive formulation of Doc 96 (untenable after Phase 27) and leaves a first falsifiable, self-contained, well-posed step: Conjecture 100.A ($\mu_{\{\infty,2\}} = 0$, a single prime term against the archimedean one).

2. **What is refuted.** The feared technical point — that the space of test functions shrinks as $S$ grows — is false: the allowed support grows as $[1/n, n]$ and exhausts all of $C_c^\infty$ (verified textually in CC 2021 and CCM 2024; Lemma 3.4 of this document). Also discarded is the additive reading "$\mu = \mu_\infty + \sum_p \mu_p$ with local $\mu_p$": the index is not additive by places and need not be.

3. **What is open (the new obstruction).** The extension $S \to$ all places fails today at $\mathbf{O}_{SL}$: no $P(n)$ with $n > 2$ is proved, and there is no mechanism of uniformity in $n$ for the quantitative control of the Weil−Sonine discrepancy (defect $c(n)$, conditioning $d(n)$), where the program's $\sqrt{n}$ vs $\log n$ barrier reappears sliced by windows. It is a **quantitative** obstruction (bounds are missing), not a **structural** one (no object is missing), and it is disjoint from MW-2/MW-3/MW-5 and from the non-factorization of Phase 27 (Proposition 5.1). Being quantitative does not make it minor: it has exactly the shape of the obstructions on which the program has already run aground once (C5, threshold $a_{\mathrm{tail}} = 1$).

4. **Why PARTIAL and neither LIVE ROUTE nor CLOSED ROUTE.** It is not a CLOSED ROUTE: the base case is proved with a non-circular mechanism, the first new step (100.A) is falsifiable with already-built objects, and none of the three components of $\mathbf{O}_{SL}$ is an impossibility theorem. It is not a fully LIVE ROUTE: the complete route requires infinitely many links with non-uniformized constants, the simplest link $n > 2$ has been open since 2020 in the hands of the very authors of the mechanism, and if the archimedean positivity turned out to depend essentially on the absence of arithmetic in the base window (third scenario of §6.2), the contribution of the CC exception to $\mathbf{C}_D^B$ would be reduced to zero. The decision between these two destinies is concentrated in a single statement: Conjecture 100.A. Until it is resolved, the frank status is PARTIAL.

**Next action proposed for the program:** attack Conjecture 100.A by the CC scheme: (i) write the Sonine compression in $L^2(X_{\{\infty,2\}})$ with the measure $|L_2(\tfrac12 - is)|^2 |\Gamma_{\mathbb{R}}|^2 ds$; (ii) identify the discrepancy operator and its Toeplitz part in the window $(1/3,3)$; (iii) determine whether the conditioning defect remains finite and at certifiable points. Whichever of the three steps fails, fails informatively.

---

## Appendix A — Provenance of the verifications

To comply with the program's citation rule, what was verified and how is recorded here:

1. **arXiv:2006.13771** (CC, *Weil positivity and trace formula, the archimedean place*): full PDF downloaded and read on pages 1–8 (abstract, introduction, Theorem 1, Corollary 2, Theorem 3, outline of §§1–6) and 55–57 (full bibliography). The statements cited in §2.3 are direct transcriptions. Publication in Selecta Math. (N.S.) 27 (2021) was verified against the Springer page (DOI s00029-021-00689-4).
2. **arXiv:2310.18423 v2** (CCM, *Zeta zeros and prolate wave operators*): full PDF downloaded and read on pages 1–6 (abstract, full introduction, statements of Theorems 1 and 2 of §4, definition of $X_S$, $\Gamma$, $dm_S$). The textual quotes of §2.2 and §2.5(b) come from those pages. Publication in Ann. Funct. Anal. 15 (2024) verified by search.
3. **arXiv:2008.10974** (CC, *Quasi-inner functions and local factors*): verified by abstract and publication data (J. Number Theory 226 (2021), 139–167). The fine statement of its internal theorems was **not** read in source; the use made of it here (off-diagonal compactness, "analytic prerequisites for semilocal positivity") is limited to what is stated in the abstract and the author's publication page. Any finer use in future work of the program requires direct reading.
4. **Yoshida 1992**: cited through CC 2021 (reference [34] of its bibliography, verified on page 57 of the PDF: Adv. Stud. Pure Math. 21, 281–325). The primary source was not consulted; the exact scope of Yoshida's computation (only $(1/2,2)$ or larger windows?) remains [NOT VERIFIED].
5. **Negative searches**: web searches for proofs of semilocal positivity with finite places ($P(n)$, $n > 2$) turned up no publication. A negative search is not proof of nonexistence; the "open" status of 100.A is the best information available, not an established fact.
6. **Connes 1999** (Selecta Math. 5, semilocal trace formula): not re-read in source for this document; it is used through its reception in CC 2021/CCM 2024, which cite it as [11]/[7] respectively and reconstruct the full semilocal framework in the passages read.

---

## References

**External literature (verified in source):**

- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952), 252–265.
- N. Y. Sonin, *Recherches sur les fonctions cylindriques et le développement des fonctions continues en séries*, Math. Ann. 16 (1880), 1–80.
- H. Yoshida, *On Hermitian forms attached to zeta functions*, in: Zeta Functions in Geometry (Tokyo, 1990), Adv. Stud. Pure Math. 21, Kinokuniya, Tokyo (1992), 281–325. [Cited in CC 2021 as the first proof of the archimedean inequality in the window $(1/2,2)$.]
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. [Semilocal trace formula: theorem.]
- J.-F. Burnol, *Sur les espaces de Sonine associés par de Branges à la transformation de Fourier*, C. R. Acad. Sci. Paris, Ser. I 335 (2002), 689–692.
- A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. (N.S.) 27 (2021), art. 77; arXiv:2006.13771. [Theorem 1, Theorem 6.11, Corollary 2, Theorem 3, criterion (2), semilocal support condition: verified textually.]
- A. Connes, C. Consani, *Quasi-inner functions and local factors*, J. Number Theory 226 (2021), 139–167; arXiv:2008.10974. [Off-diagonal compactness of products of local-factor quotients over finite $S$.]
- A. Connes, C. Consani, *Spectral triples and ζ-cycles*, arXiv:2106.01715. [Context; not used in critical steps.]
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024), art. 70; arXiv:2310.18423 (v2, May 2024). [Property $P(n)$; framework $X_S$; Theorem 1 (measure $dm_S$); Theorem 2 (stability of the semilocal Sonine); status of semilocal positivity as a strategy: verified textually.]
- J. Robbin, D. Salamon, *The Maslov index for paths*, Topology 32 (1993), 827–844.
- M. G. Kreĭn, H. Langer; T. Ya. Azizov, I. S. Iokhvidov: as in Doc 91, Appendix A.

**Program documents:**

- Doc 91 — Pontryagin space $(\mathcal{K}, Q)$, index $\kappa$, conditions C1–C7, barrier $\sqrt{N}$ vs $\log N$ (Prop. 4.5).
- Doc 94 — Condition C5, prime tail, Conjecture $\mathbf{C}_B$.
- Doc 96 — Angle 3 (Maslov), Theorem 8.1 (localization in $\mathcal{K}_{\mathrm{off}}$), Conjecture $\mathbf{C}_D$, Obstacle $\mathbf{O}_D$.
- Doc 98 — Toy test: spectral flow $= -2 = -\kappa$ for an off-critical quadruple (§7).
- Phase 27, docs 00–03 — Proposition 27-C.1: the prime term factors, the zero term does not.
- Paper P35 — Bridge theorem $\kappa(Q) = \mathrm{neg.ind}(H_C)$, program V.1–V.4, Hypothesis D.

---

*End of Doc 100. Status: complete analysis of the semilocal front. Base case proved (external), first falsifiable step formulated (Conjecture 100.A), obstacle $\mathbf{O}_{SL}$ named with three components. Verdict: PARTIAL.*
