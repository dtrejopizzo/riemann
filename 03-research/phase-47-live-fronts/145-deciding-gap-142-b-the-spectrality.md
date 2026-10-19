# Doc 145 — Deciding GAP-142.B: the spectrality of the archimedean semilocal object

**Program:** Riemann Hypothesis — Phase 47: live fronts.
**Prerequisites:** Doc 142 (semilocal object $X_S^{\mathrm{ar}}$; weight $\Omega$; short-window Theorem A; failure Theorem B; transmission identity; trilemma §8; contrapositive $H^+\Rightarrow$ non-spectral; GAP-142.B); Doc 135 (two-prime theorem; "spectral" = sum of squares over vertical progressions; H⁺ in P48); Doc 131 §4–§6 (Def. 4.1 spectral object; Thm. 4.4 orbits; Thm. 6.3 H-by-blocks ⟺ on-line divisor; Def. 6.1 Axiom H; Conjecture H⁺ = Desideratum 6.9).
**Creative contract:** [NEW-DEFINITION] total freedom; [THEOREM]/[PROPOSITION]/[LEMMA] with complete proof or they carry no label; [BRIDGE] with declared status; [GAP]/[DESIDERATUM] named; [FACT] real literature. Absolute frankness. No numerics: closed form only (digamma/Gamma, integrals and series evaluable symbolically).

**Conventions (those of Doc 142, fixed once).** $G=\mathbb R_+^*$, $d^*x=dx/x$, $f\in C_c^\infty(G)$, $F(t)=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R)$, $\hat F(\xi)=\int_{\mathbb R}F(t)e^{i\xi t}dt$, $\hat f(\tfrac12+i\xi)=\hat F(\xi)$, $g=f\star\tilde f$, $\hat G(\xi)=|\hat F(\xi)|^2$, $\|f\|_w^2=\|F\|_{L^2}^2$. The archimedean weight (Doc 142, Def. 1.1):
$$\Omega(\xi)=\mathrm{Re}\,\psi\bigl(\tfrac14+\tfrac{i\xi}2\bigr)-\log\pi,\qquad \mathcal A(f)=\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi.$$
$\psi=\Gamma'/\Gamma$ digamma, $\gamma$ Euler. Recall $\Omega(0)=-\gamma-\tfrac\pi2-3\log2-\log\pi<0$ (Doc 142, Lemma 2.2) and $\Omega<0$ exactly on $(-\xi_*,\xi_*)$ (Lemma 2.3).

---

## 0. Executive summary

GAP-142.B asked to decide the trilemma of Conjecture H⁺: the counterexample of Doc 142 ($X_S^{\mathrm{ar}}$ violates H) verifies ALL the hypotheses of H⁺ except the **spectrality** of the semilocal object. Doc 142 left the contrapositive ($H^+\Rightarrow$ non-spectral) and named three branches: (1) spectral ⟹ H⁺ refuted; (2) non-spectral ⟹ H⁺ collapses onto RH; (3) undecidable. This document decides.

**Verdict: the semilocal object is NOT spectral in the program's sense (Doc 131, Def. 4.1, with on-line divisor on the critical line) — branch (2).** The obstruction is not heuristic: it is a **theorem** (Theorem 3.4 below). Its core is elementary and robust:

- "Spectral with on-line divisor" ⟹ $Q\ge0$ (sum of squares, Doc 131 Prop. 6.2). Theorem B of Doc 142 gives $Q_S(f_T)<0$. Hence **there is no on-line divisor**: the on-line-spectrality branch is unconditionally closed.
- The decisive piece, **new here**, is that non-spectrality already lives in the **archimedean core** $\mathcal A$ alone, before touching primes or the pole: $\mathcal A$ is a quadratic form whose **symbol $\Omega$ changes sign** (Lemma 2.3 of Doc 142). A form $\int|\hat F|^2\,\Omega$ is representable as a positive spectral measure $\sum_k|\langle F,e_k\rangle|^2$ (with $e_k$ exponentials/evaluations) **if and only if** $\Omega\ge0$ a.e. (Theorem 2.2 below, via Bochner). Since $\Omega(0)<0$, **this fails**. The $\zeta$-type archimedean term is intrinsically **one-sided with negative part**: it is NOT the transform of a positive measure, it is a Weil distribution with density of indefinite sign.

**Consequence for H⁺ (Theorem 4.1):** H⁺ is NOT weaker than RH. Its only nontrivial content is the spectrality hypothesis, and for objects with $\zeta$-type archimedean term, positive-spectrality is essentially RH (it forces the divisor onto the line, which for $\zeta_{\mathrm{ob}}$ IS RH). H⁺ truncated to finite $S$ is **emptied out** (its class is empty: no $X_S^{\mathrm{ar}}$ with finite $S$ is positive-spectral). GAP-135.B was ill-posed: the semilocal object was never in the class of H⁺. **Negative result: the illusory semilocal interpolation route is closed.**

**What survives unconditionally (§5):** Theorem A of Doc 142 (short-window positivity, $Q_S\ge\tfrac3{10}\|f\|_w^2$ for $2T\le\tfrac1{150}$, uniform in $S$, includes $\zeta$) and the transmission identity (Prop. 6.1 of Doc 142) **do not depend on the trilemma** — they are facts about the form $Q_S$, not about its representation. They stand and are restated.

---

## 1. [NEW-DEFINITION] "Spectral" with full precision

Doc 131 (Def. 4.1) and Doc 135 use "spectral" in ways that need to be sharply separated, because the trilemma is decided exactly in the difference between them.

**[NEW-DEFINITION 1.1] (EF-spectral: the broad sense of Doc 131, Def. 4.1).** A hermitian object $X$ is **EF-spectral** if there exists a countable multiset $Z\subset\mathbb C$ (the **divisor**), with bounded real parts and counting function $N_Z(T)=\#\{\rho\in Z:|\mathrm{Im}\,\rho|\le T\}\ll T^A$ for some $A<\infty$ (**polynomial density**), such that
$$\sum_{\rho\in Z}\hat f(\rho)\;=\;W_X(f)\qquad\forall f\in C_c^\infty(G),$$
with absolute convergence. (This is the object's explicit formula.)

**[NEW-DEFINITION 1.2] (positive-spectral: the strong sense, program/Doc 135).** An EF-spectral hermitian object $X$ with divisor $Z$ is **positive-spectral** if moreover $Z\subset\{\mathrm{Re}\,s=\tfrac12\}$ ($\sigma$-stable with $\sigma\rho=\rho$). Then, writing $\rho=\tfrac12+i\xi$ and multiplicities $m_\rho$,
$$Q_X(f)\;=\;\sum_{\rho\in Z}m_\rho\,\hat f(\rho)\,\overline{\hat f(\sigma\rho)}\;=\;\sum_{\rho\in Z}m_\rho\,\bigl|\hat F(\mathrm{Im}\,\rho)\bigr|^2\;\ge\;0$$
(Doc 131, Thm. 4.4(a) + Prop. 6.2). In the case of pure primes (Doc 135, Thm. 3.1) this is exactly $Q_X(f)=2\sum_{\Lambda_p}|\hat F|^2$: **sum of squares of evaluations of $\hat F$ over the vertical progressions** $\Lambda_p=\{\log p,2\log p,\dots\}$ read on the frequency axis. This is the representation that H⁺ asks for (P48, Conjecture 7.1: "$X$ spectral"); the operational content of "spectral" in the conjecture is **positive-spectral**.

**[REMARK 1.3] (why this is the correct reading for H⁺).** H⁺ concludes $Q_X\ge0$. If "spectral" meant only EF-spectral (divisor anywhere), then by Doc 131 Thm. 6.3, a divisor with a point off the line forces a hyperbolic block with a negative direction: the conclusion $Q_X\ge0$ would be false for such objects, and H⁺ would be trivially false for reasons unrelated to the semilocal object. The only reading under which H⁺ is a substantive conjecture (not trivially false) is: **"spectral" = positive-spectral = on-line divisor**. With that reading, "$X$ spectral $\Rightarrow$ $Q_X\ge0$" is a **theorem** (Prop. 6.2), and H⁺ says "the data $(a\ge0,\text{Euler},\text{polar},\Gamma)$ force the spectral lift to exist and fall on the line." We adopt this reading. It makes the contrapositive of Doc 142 (Thm. 8.1) a genuine theorem: if $Q_S<0$ for some $f$, then $X_S^{\mathrm{ar}}$ admits no on-line divisor, i.e. it is not positive-spectral.

**[REMARK 1.4] (the third reading, off-line, and why it does not save H⁺).** One might try "spectral with off-line divisor but positive by some other structure." But Doc 131 Thm. 4.4(a) is an identity: for ANY $\sigma$-stable divisor, $Q_X(f)=\sum_\rho m_\rho\hat f(\rho)\overline{\hat f(\sigma\rho)}$, and a point $\rho_0$ with $\mathrm{Re}\,\rho_0\ne\tfrac12$ contributes a hyperbolic plane of signature $(1,1)$ (Thm. 4.4(b)), realized as a negative direction by the evaluation Lemma 4.3. Hence **off-line divisor ⟹ $Q_X$ indefinite**. There is no "positive-spectral with off-line divisor": positive-spectral ⟺ on-line divisor, with no escape. This closes branch (3) of the trilemma of Doc 142 §8 (the "exotic divisor" sub-option) as a case of branch (1)/(2), not as a third way.

Summary of the framework: **"$X$ spectral" in H⁺ = positive-spectral = the Weil form $Q_X$ is represented as $\sum_k|\langle F,e_k\rangle|^2$ with $e_k(t)=e^{i\xi_k t}$, $\xi_k$ the heights of the on-line divisor.** Deciding GAP-142.B = deciding whether $Q_S$ (equivalently $\mathcal A$, see §3) admits such a representation.

---

## 2. The archimedean term is NOT the form of a positive spectral measure

Here lies the analytic heart. We isolate the representation question for the quadratic form $\mathcal A$, with no pole or primes, and decide it with a Bochner-type characterization.

**[NEW-DEFINITION 2.1] (form with spectral measure; representation by evaluations).** A quadratic form $\mathcal B(f)=\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,d\nu(\xi)$ on $C_c^\infty(G)$, given by an even temperate measure/distribution $\nu$, **admits a positive spectral representation** if there exists a **positive** Borel measure $\mu\ge0$ on $\mathbb R$, of polynomial growth, such that $\mathcal B(f)=\int_{\mathbb R}|\hat F(\xi)|^2\,d\mu(\xi)$ for every $f$. (When $\mu=\sum_k m_k\delta_{\xi_k}$ is atomic with polynomial density, this is exactly $\mathcal B(f)=\sum_k m_k|\hat F(\xi_k)|^2=\sum_k m_k|\langle F,e^{i\xi_k\cdot}\rangle|^2$: sum of squares of evaluations — the positive-spectral sense of Def. 1.2 with $e_k$ the exponentials of the divisor.)

**[THEOREM 2.2] (symbol positivity criterion).** Let $w\in L^1_{\mathrm{loc}}(\mathbb R)$ be even, real, of polynomial growth, and $\mathcal B_w(f)=\frac1{2\pi}\int|\hat F(\xi)|^2 w(\xi)\,d\xi$. Then:
$$\mathcal B_w\ \text{admits a positive spectral representation}\quad\Longleftrightarrow\quad w(\xi)\ge0\ \text{for almost every }\xi\in\mathbb R.$$
Moreover, $\mathcal B_w(f)\ge0$ for every $f\in C_c^\infty(G)$ ($\iff$ for every $F\in C_c^\infty(\mathbb R)$) $\iff w\ge0$ a.e.

*Proof.* ($\Leftarrow$) If $w\ge0$ a.e., $d\mu:=\tfrac1{2\pi}w(\xi)\,d\xi$ is a positive measure of polynomial growth and $\mathcal B_w(f)=\int|\hat F|^2\,d\mu$: a positive representation, and $\mathcal B_w(f)\ge0$ trivially.

($\Rightarrow$, positivity ⟹ $w\ge0$ a.e.) Suppose $\mathcal B_w(f)\ge0$ for every $F\in C_c^\infty(\mathbb R)$. Let $E:=\{\xi:w(\xi)<0\}$ and suppose $|E|>0$ (positive Lebesgue measure). By regularity there is a Lebesgue density point $\xi_0$ of $E$; by the evenness of $w$ we can take $\xi_0\ge0$, and if $\xi_0>0$ then also $-\xi_0\in E$. Choose a test whose spectral mass $|\hat F|^2$ concentrates near $\{\pm\xi_0\}$ inside $E$. Concretely: let $\phi\in C_c^\infty(\mathbb R)$ with $\hat\phi\in C_c^\infty$, $\hat\phi\ge0$, $\mathrm{supp}\,\hat\phi\subset[-1,1]$, $\hat\phi(0)>0$; for $\delta>0$ and $R>0$ set $\hat F_{\delta,R}(\xi):=\hat\phi\bigl(\tfrac{\xi-\xi_0}\delta\bigr)+\hat\phi\bigl(\tfrac{\xi+\xi_0}\delta\bigr)$ (even; corresponds to a real modulated $F$, $F_{\delta,R}\in\mathcal S$ and approximable in $C_c^\infty$). Then $|\hat F_{\delta,R}|^2$ is a bump of width $O(\delta)$ centered at $\pm\xi_0$ (the two terms have disjoint supports for $\delta<\xi_0$), total mass $\asymp\delta\|\hat\phi\|_2^2$ on each side, and
$$2\pi\,\mathcal B_w(F_{\delta,R})=\int|\hat F_{\delta,R}|^2 w=2\int\hat\phi\bigl(\tfrac{\xi-\xi_0}\delta\bigr)^2 w(\xi)\,d\xi=2\delta\int\hat\phi(u)^2\,w(\xi_0+\delta u)\,du.$$
Since $\xi_0$ is a density point of $E$ and $w$ is locally integrable, $\tfrac1{2H}\int_{\xi_0-H}^{\xi_0+H}w\to w$-average $<0$; more finely, since $\xi_0$ is a Lebesgue point of $w$ (a.e. point is) and $\xi_0\in E$ is a density point, the average $\int\hat\phi(u)^2 w(\xi_0+\delta u)\,du\to w(\xi_0)\int\hat\phi^2<0$ as $\delta\to0$ (choosing $\xi_0$ a Lebesgue point with $w(\xi_0)<0$, which occurs at a.e. point of $E$ since $|E|>0$). Hence $\mathcal B_w(F_{\delta,R})<0$ for small $\delta$: contradicting $\mathcal B_w\ge0$. Therefore $|E|=0$, i.e. $w\ge0$ a.e. The equivalence with positive representation follows from ($\Leftarrow$) (representation ⟹ positive trivially, and positive ⟹ $w\ge0$ ⟹ representation). The case $C_c^\infty(\mathbb R)$ vs $\mathcal S$: $C_c^\infty$ is dense and the form is continuous in the relevant topology, so it suffices to approximate $F_{\delta,R}$ by $C_c^\infty$ with arbitrarily small loss. $\square$

**[REMARK 2.3] (this is Bochner on the correct side).** Theorem 2.2 is the "symbol" version of Bochner's theorem [FACT: Bochner, *Lectures on Fourier integrals*, Princeton 1959; or Reed–Simon II, Thm IX.9]. The form $f\mapsto\int|\hat F|^2 d\nu$ is the quadratic form associated with the **Fourier multiplier** $w$; it is a functional of positive type in $F$ ⟺ its symbol $w$ is $\ge0$ ⟺ $\nu$ is a positive measure ⟺ a "positive spectral density" exists. The content is elementary but decisive: **the positivity of a form diagonal in Fourier is pointwise in the symbol**. There is no way to buy a negative symbol in one region with positive mass in another: the directions separate in frequency.

**[THEOREM 2.4] (the archimedean weight is not representable: the analytic decision).** The archimedean term $\mathcal A(f)=\frac1{2\pi}\int|\hat F|^2\Omega$ does **NOT** admit a positive spectral representation; equivalently, $\mathcal A$ **is not** a sum of squares of evaluations $\sum_k m_k|\hat F(\xi_k)|^2$ with weights $m_k\ge0$. The obstruction is exact and localized:
$$\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma-\tfrac\pi2-3\log2-\log\pi<0,\qquad \Omega<0\ \text{on }(-\xi_*,\xi_*),\ \xi_*>0.$$

*Proof.* By Theorem 2.2 with $w=\Omega$: $\mathcal A$ admits a positive spectral representation ⟺ $\Omega\ge0$ a.e. But $\Omega$ is continuous (Doc 142, Lemma 2.1) and $\Omega(0)<0$ (Lemma 2.2), hence $\Omega<0$ in a neighborhood of $0$ of positive measure — in fact exactly on $(-\xi_*,\xi_*)$ with $\xi_*>0$ by strict monotonicity (Lemma 2.3). By the contrapositive of Theorem 2.2, $\mathcal A$ is not representable and in fact $\mathcal A$ is **indefinite**: there exists $f$ with $\mathcal A(f)<0$ (take spectral mass concentrated in $(-\xi_*,\xi_*)$; this is the mechanism of Theorem B of Doc 142, slow and wide $\eta$). $\square$

**[REMARK 2.5] (the correct spectral reading of $\Omega$: trivial zeros, NEGATIVE multiplicity).** Does $\Omega$ have *any* spectral representation, even if not positive? Yes, and it is instructive. $\Omega$ is the contribution of the factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ to the Riemann–Weil formula. In the full explicit formula, the archimedean term is written (Weil 1952; Connes 1999) as
$$\mathcal A(f)=-\,g(1)\log\pi+\frac1{2\pi}\int_{\mathbb R}\hat F(\xi)\,\mathrm{Re}\,\psi\bigl(\tfrac14+\tfrac{i\xi}2\bigr)\,\overline{\hat F(\xi)}\,d\xi,$$
and Hadamard's identity for $\Gamma$ gives the expansion of $\Omega$ as a sum over the **poles of $\Gamma(s/2)$**, i.e. the **trivial zeros** of $\zeta$ at $s=-2,-4,-6,\dots$ These are NOT on the critical line; they enter the explicit formula with the sign that, in Doc 131's language, corresponds to **multiplicity/position producing indefinite signature**. Indeed: the "spectral density" of $\Omega$, as a Weil distribution, is $\Omega(\xi)$ itself, and its negative part $\Omega\mathbf 1_{(-\xi_*,\xi_*)}$ is exactly the "negative-sign spectral mass" that no positive measure can reproduce. The one-sidedness that Doc 142 §7 [GAP-142.B.2] pointed out — "the prime term is a half with mirror weight, not the bilateral Poisson sums of full vertical progressions" — is the same obstruction seen from the arithmetic side: **the divisor that would represent $X_S^{\mathrm{ar}}$ would have to include the trivial zeros (off-line, with their indefinite-sign contribution), and hence would NOT be an on-line divisor.** EF-spectral: possibly (with trivial zeros + whatever the pole contributes + the primes); **positive**-spectral: impossible. That is the decision.

**[REMARK 2.6] (contrast with the pure primes of Doc 135, where it DID work).** For a pure prime, the spectral weight of the Euler factor was $W_F(f)=L_p\sum_m c_m f(p^m)$ with $|c_m|=2p^{m/2}$ at the Ramanujan edge, and the divisor fell exactly on the line (purity), giving $Q=2\sum_{\Lambda_p}|\hat F|^2\ge0$: symbol "$\ge0$" because it was literally a sum of squares of evaluations. The pure Euler factor is a **weight of positive type** (positive atomic measure on the vertical progression). The $\Gamma$ factor, by contrast, has symbol $\Omega$ with a negative part: **it is not a factor of positive type**. The difference between Doc 135 (spectral, H holds) and Doc 142 (not positive-spectral, H fails) is exactly the difference between a symbol $\ge0$ and a symbol of indefinite sign. The "destructive" regime of Doc 142 IS the negativity of the archimedean symbol.

---

## 3. The complete form $Q_S$ inherits the symbol's non-positivity

The polar block and the primes do not change the verdict, and it is worth seeing this precisely because spectrality is a property of the whole object, not only of $\mathcal A$.

**[PROPOSITION 3.1] (the negativity survives the other blocks: already in Doc 142).** For every finite $S$ (including $\varnothing$) there exists $f$ with $Q_S(f)<0$. *(This is Theorem B of Doc 142, Thm. 5.1: the family $f_T$ with $\hat f_T(1)=0$ kills the polar term, the primes add $+B_S\|\eta\|^2$ with their worst sign, and $\mathcal A(f_T)\to\Omega(0)\|\eta\|^2<0$; total $(\Omega(0)-B_S)\|\eta\|^2<0$.)* $\square$

**[THEOREM 3.4] (GAP-142.B decided: $X_S^{\mathrm{ar}}$ is not positive-spectral).** For every finite $S$ (including $S=\varnothing$), the semilocal object $X_S^{\mathrm{ar}}$ **is not positive-spectral** (Def. 1.2): there is no divisor $Z\subset\{\mathrm{Re}=\tfrac12\}$ of polynomial density with $\sum_{\rho\in Z}\hat f(\rho)=W_{X_S^{\mathrm{ar}}}(f)$. Equivalently, $Q_S$ does **not** represent as $\sum_k m_k|\hat F(\xi_k)|^2$ with $m_k\ge0$.

*Proof.* Two independent proofs, both complete.

*(A) Via the complete form.* If $X_S^{\mathrm{ar}}$ were positive-spectral, by Doc 131 Prop. 6.2 (= Def. 1.2) we would have $Q_S(f)=\sum_{\rho\in Z}m_\rho|\hat F(\mathrm{Im}\,\rho)|^2\ge0$ for every $f$. This contradicts Proposition 3.1 ($Q_S(f_T)<0$). $\square_A$

*(B) Via the archimedean symbol, localizing the obstruction.* Even before invoking the full family $f_T$, the obstruction already lives in $\mathcal A$. Restrict to tests with polar and primes switched off exactly: take $f$ with $\mathrm{supp}\,F\subset(\,\tau,\ \tau+\ell\,)$ for $\ell<\log2$ and $\tau$ such that no $mL_p$ ($p\in S$) falls in $(-\ell,\ell)$ — automatic for $\ell<\log2\le mL_p$ — so that $P_S(f)=0$; and with $\hat f(1)=0$ to kill the polar term (a linear condition, possible without emptying $C_c^\infty$). For such a class, $Q_S(f)=\mathcal A(f)$ exactly. By Theorem 2.4, $\mathcal A$ is indefinite with negative directions concentrated on $(-\xi_*,\xi_*)$. Low-frequency spectral mass is obtained with wide tests; combining with $\hat f(1)=0$ (cost $e^{-T/8}$, Doc 142 Thm. 5.1 step 0) and $P_S=0$ (window avoiding the lags — alternatively the wide family $f_T$ whose primes add $+B_S$, which only reinforces negativity), one realizes $Q_S(f)<0$. But more important than the sign: **the positive-spectral representation is impossible for structural reasons, not for reasons of size.** If there existed a measure $\mu\ge0$ atomic on the line with $Q_S(f)=\int|\hat F|^2 d\mu$, then in particular for the tests with $P_S=0$ and dead polar we would have $\mathcal A(f)=\int|\hat F|^2 d\mu\ge0$ — i.e. $\mathcal A$ would admit a positive representation, contradicting Theorem 2.4 ($\Omega(0)<0$). $\square_B$

The two proofs agree in the verdict and localize it: the non-positive-spectrality of $X_S^{\mathrm{ar}}$ is **archimedean in origin** (the symbol $\Omega$ with negative part), inherited intact by the complete form. $\square$

**[REMARK 3.5] (the EF-spectral divisor does exist — it is truncated $\zeta$, off-line).** $X_S^{\mathrm{ar}}$ is not devoid of all spectral structure: it has an EF-spectral representation (Def. 1.1, divisor anywhere) in the weak sense, because its three blocks are Mellin evaluations and the truncated Riemann–Weil formula expresses it via the trivial zeros (of $\Gamma$), the pole ($\xi=-i/2$), and the zeros of the partial product $\prod_{p\in S}(1-p^{-s})^{-1}$ — but that divisor **lives off the line** (trivial zeros at $\mathrm{Re}=-2,-4,\dots$; poles of the Euler factors at $\mathrm{Re}=0$). Doc 131 Thm. 4.4(b)/6.3: a divisor with off-line points gives indefinite $Q$. Consistent with everything: $X_S^{\mathrm{ar}}$ is (at most) EF-spectral with off-line divisor, **never** positive-spectral. Branch (1) of the trilemma (positive-spectral ⟹ H⁺ refuted) is **vacuous in hypothesis**: the antecedent is never satisfied. The operating branch is (2).

---

## 4. Consequence for H⁺: it is not weaker than RH; it collapses

**[THEOREM 4.1] (verdict of the trilemma: branch (2) — H⁺ collapses onto RH).** Under the forced reading "spectral = positive-spectral" (Rem. 1.3, the only one making H⁺ non-trivially-false):

(a) **H⁺ survives as a statement** (it is not refuted): its only candidate counterexample, $X_S^{\mathrm{ar}}$, is NOT in its class, because it is not positive-spectral (Theorem 3.4). The contrapositive of Doc 142 (Thm. 8.1, $H^+\Rightarrow$ non-spectral) is realized as a **fact**: $X_S^{\mathrm{ar}}$ is indeed not spectral. There is no contradiction.

(b) **But H⁺ is NOT weaker than RH.** The positive-spectrality hypothesis carries 100% of the content: for a hermitian object with polar block $[0]+[1]$ and $\zeta$-type archimedean weight (symbol $\Omega$ with negative part), demanding an on-line divisor **forces** the negative archimedean deficit $\Omega\mathbf 1_{(-\xi_*,\xi_*)}$ to be compensated exactly from the divisor's side. The remaining hypotheses (hermitian + $a=\Lambda\ge0$ Euler + polar + $\Gamma$) are **consistent with violations of H of size $\ge|\Omega(0)|\approx5.37$** (Theorem 3.4 / Doc 142 Thm. 5.1). Hence they contribute no positivity. All the force is in "an on-line divisor exists," which for the complete data ($a=\Lambda$ on ALL primes) IS the statement that the zeros of $\zeta$ are on the line: **RH itself**.

(c) **H⁺ truncated to finite $S$ is empty** (Corollary 4.2 below): the class "positive-spectral objects with finite $S$ + $\Gamma$" contains no $X_S^{\mathrm{ar}}$. The only nonempty instance of the class of H⁺ with weight $\Gamma$ is the **complete** Euler product (all primes), i.e. $\zeta_{\mathrm{ob}}$, and there positive-spectral ⟺ RH. H⁺ is **RH in disguise for objects with an archimedean term**.

*Proof.* (a) Theorem 3.4. (b) The consistency of the hypotheses with $Q_S<0$ is Theorem 3.4 (B); that positive-spectrality implies on-line divisor is Def. 1.2; that for complete $a=\Lambda$ this is RH is Weil's criterion [FACT: Weil 1952; Bombieri 2000] and Doc 131 BRIDGE 7.1. (c) Corollary 4.2. $\square$

**[COROLLARY 4.2] (the semilocal class of H⁺ is empty; GAP-135.B was ill-posed).** There is no $X_S^{\mathrm{ar}}$ with finite $S$ that is simultaneously (hermitian + $a\ge0$ Euler + standard polar + $\Gamma$) AND positive-spectral. Hence the claim of Doc 135 §9 / GAP-135.B — that the two-prime semilocal object with archimedean term was "the first genuine case, weaker than RH, of H⁺" — is **false**: the object was never in the class of H⁺. *(Immediate from Theorem 3.4: $X_S^{\mathrm{ar}}$ is not positive-spectral for any finite $S$.)* $\square$

**[REMARK 4.3] (negative result, its value).** This closes an illusory route of the program, which is exactly what the objective asked to evaluate as a valuable finding. The hope of Doc 135/P48 was a **semilocal interpolation**: prove H⁺ for finite $S$ (easier than RH) and leave the limit $S\to\infty$ as a GAP. Theorem 3.4 shows that **there is no such intermediate step**: as soon as the weight $\Gamma$ is added (symbol with negative part), the only object in the class is complete $\zeta$ and the conjecture is RH. The wall of Doc 142 §8 ("there is no semilocal interpolation between the constructive two-prime theorem and RH; the first destructive step costs the full price") is **redrawn with precision**: the price is positive-spectrality with negative archimedean symbol, and that price is RH. Frank reformulation of the surviving conjecture (H⁺-complete, Doc 142 §8): *hermitian + positive-spectral + complete $a=\Lambda$ + polar + $\Gamma$ ⟹ H* — and here "positive-spectral" ⟺ "on-line divisor" ⟺ RH, so the conjecture is **RH ⟹ RH**, tautological. H⁺ offers no content below RH.

---

## 5. What survives unconditionally (independent of the trilemma)

The verdict of the trilemma is about the **representation** of $Q_S$. Two results of Doc 142 are about the **form** $Q_S$ itself and do not depend on how spectrality falls; we restate them as survivors.

**[THEOREM 5.1] (= Theorem A of Doc 142, reaffirmed).** For every $S$ (finite, infinite, or all primes, including $\zeta$) and every $f\in C_c^\infty(G)$ of window $2T\le\tfrac1{150}$:
$$Q_S(f)\;\ge\;\tfrac3{10}\,\|f\|_w^2.$$
**Status after GAP-142.B:** intact. The proof (Doc 142 §3) uses no spectral representation: it decomposes $Q_S$ into its three blocks and uses $\Omega(\xi)\sim\log|\xi|>0$ at high frequency (forced by uncertainty in a short window), $P_S=0$ (far lags), polar $=O(T)$. It is **direct positivity of the form**. It says, independent of the trilemma: **the data class of H⁺ satisfies H restricted to short windows, unconditionally and uniform in the data** (includes $\zeta$). It is the program's first Weil positivity with an archimedean term, and it survives entirely. *(The original objective's [DESIDERATUM] — archimedean domination up to support $\theta\log(p_1\cdots p_n)$ — remains false as stated: the threshold is absolute, $O(1)$, archimedean, it does not scale with the conductor; GAP-142.A.)* $\square$

**[PROPOSITION 5.2] (= transmission identity, Prop. 6.1 of Doc 142, reaffirmed).** For every $f$ and every finite $S$, unconditionally:
$$Q_S(f)\;=\;\underbrace{\sum_{\rho}\hat g(\rho)}_{Q_{\mathrm{full}}(f),\ \text{Riemann–Weil}}\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr].$$
**Status after GAP-142.B:** intact (it is algebra + Weil's explicit formula, [FACT: Weil 1952]). What it now says, in light of the verdict: the transmission deficit $D_S=B_S-\Omega(0)>0$ that measures the violation (Doc 142 Cor. 6.2, under RH) is **exactly** the negative spectral mass of the symbol $\Omega$ that no on-line divisor can absorb without the complete Euler product. The identity localizes where the limit $S\to$ all-primes stops commuting with positivity: in the transmission of the pole's custody ($\xi=-i/2$) to the real axis, which only the complete sum of primes achieves. This **redistributes** GAP-135.B onto spectrality — and §3–§4 decided it. $\square$

**[PROPOSITION 5.3] (= surviving cone, Prop. 7.2 of Doc 142, reaffirmed).** With dead polar and low spectral mass $\le\varepsilon_S\|f\|_w^2$ below $\bar\xi_S$ (defined by $\Omega(\bar\xi_S)=B_S+2$), one has $Q_S(f)\ge\|f\|_w^2$. **Status:** intact, for the same reason (direct positivity of the form, no representation). $\square$

**[REMARK 5.4] (what survives is positivity of FORM, not of representation).** The structural lesson of GAP-142.B: two questions that the program had fused must be distinguished. (i) *Is $Q_S\ge0$?* — a question of **form**; answer: not in general (Thm. B), yes on explicit cones (Theorems 5.1, 5.3). (ii) *Is $Q_S=\sum|\text{evaluations}|^2$?* — a question of **positive-spectral representation**; answer: no (Theorem 3.4), because the archimedean symbol has a negative part. Question (ii) is strictly stronger than (i): positive representation ⟹ positive form, not conversely. H⁺ asked for (ii), and that is why it was RH. The theorems that survive are all of type (i), in regions where the symbol's negative part is forced to have small mass.

---

## 6. The map

**Proved [THEOREM/PROPOSITION/LEMMA] with complete proof here:**
- **[THEOREM 2.2]:** symbol positivity criterion (Bochner on the multiplier side): $\int|\hat F|^2 w\ge0\ \forall F$ ⟺ $w\ge0$ a.e. ⟺ positive spectral representation.
- **[THEOREM 2.4]:** the archimedean weight $\Omega$ does NOT admit a positive spectral representation, because $\Omega(0)<0$ ($\Omega<0$ on $(-\xi_*,\xi_*)$). The $\Gamma$ term is one-sided with negative part: it is not the transform of a positive measure; its "spectral density" is the trivial zeros (off-line) with indefinite sign (Rem. 2.5).
- **[THEOREM 3.4]:** **GAP-142.B decided — $X_S^{\mathrm{ar}}$ is NOT positive-spectral, for every finite $S$** (two proofs: via the complete form and via the archimedean symbol). Branch (2) of the trilemma.
- **[THEOREM 4.1] + [COROLLARY 4.2]:** consequence for H⁺ — it is not weaker than RH; the semilocal class of H⁺ is **empty**; GAP-135.B was ill-posed; H⁺-complete is tautological (RH ⟹ RH). Negative result: semilocal interpolation route closed.
- **[THEOREM 5.1], [PROP. 5.2], [PROP. 5.3]:** Theorem A, transmission identity, and surviving cone of Doc 142 **unconditionally reaffirmed** — they are positivity/algebra of the form, independent of the trilemma.

**[BRIDGE] (declared status):** the decision of GAP-142.B turns the contrapositive $H^+\Rightarrow$ non-spectral (Doc 142 Thm. 8.1) into a verified fact, and redistributes ALL the content of H⁺ onto positive-spectrality, which for data with $\Gamma$ is RH. None of this proves or refutes RH; it **prunes a conjecture** (H⁺ as a route weaker than RH) by showing it was illusory.

**[GAP] inherited, not closed here:**
- **GAP-142.A:** the archimedean threshold $T_\square\in[\tfrac1{300},T_1]$ — sign of $\mu_\varnothing(T)$ in the intermediate region (a question of form, not of representation; orthogonal to GAP-142.B).

**Final message (the verdict, in three lines).**
1. **Verdict of the trilemma:** **branch (2)**. The semilocal object $X_S^{\mathrm{ar}}$ is **NOT spectral** (not positive-spectral, Theorem 3.4), because the symbol of the archimedean term $\Omega$ has a negative part ($\Omega(0)<0$) and hence is not the transform of a positive spectral measure (Theorems 2.2 + 2.4).
2. **What happens to H⁺:** **it collapses onto RH** (Theorem 4.1). H⁺ is not refuted, but it is also not weaker than RH: its only nonempty instance with weight $\Gamma$ is complete $\zeta$, where positive-spectral ⟺ RH. The finite-semilocal class of H⁺ is **empty** (Corollary 4.2); GAP-135.B was ill-posed. The semilocal interpolation route is **closed** (valuable negative result: it prunes a strategy).
3. **Three labeled results:** **[THEOREM 2.4]** $\Omega$ is not the transform of a positive measure (analytic decision, Bochner on the symbol); **[THEOREM 3.4]** $X_S^{\mathrm{ar}}$ is not positive-spectral (GAP-142.B decided); **[THEOREM 5.1]** the short-window Theorem A ($Q_S\ge\tfrac3{10}\|f\|_w^2$, $2T\le\tfrac1{150}$, uniform in $S$, includes $\zeta$) survives the trilemma unconditionally.

---

## References

**Internal (backward-only):** Doc 142 (`phase-46-audit-and-attacks/142-attack-on-gap-135-b-the-semilocal.md`: semilocal object, $\Omega$, Theorem A, Theorem B, transmission identity, trilemma §8, GAP-142.B); Doc 135 (`phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md`: "spectral" = sum of squares over progressions; H⁺ in P48); Doc 131 (`phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md`: Def. 4.1 spectral, Thm. 4.4 orbits, Thm. 6.3, Def. 6.1 Axiom H, Desideratum 6.9 Conjecture H⁺); P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjecture 7.1 = H⁺).

**Literature [FACT]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265. (Quadratic formula; criterion H ⟺ RH; archimedean term of the factor $\Gamma_{\mathbb R}$.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233. (Normalization of the functional; role of the archimedean term and of the polar block; the functional as a form of positive type ⟺ RH.)
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (Local terms of the explicit formula as distributions; the archimedean place and its sign; trivial zeros as poles of $\Gamma$.)
- S. Bochner, *Lectures on Fourier Integrals*, Annals of Mathematics Studies 42, Princeton 1959. (Bochner's theorem: a quadratic form diagonal in Fourier of positive type ⟺ symbol/spectral measure $\ge0$.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press 1975, Thm IX.9. (Characterization of distributions of positive type via positive measures; version used in Theorem 2.2.)
- J.-F. Burnol, *The explicit formula and the conductor operator*, arXiv:math/9902080 (1999); and *Sur les formules explicites I: analyse invariante*, C. R. Acad. Sci. Paris 331 (2000), 423–428. (The archimedean term $\mathrm{Re}\,\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi$ as conductor operator; its non-positive character / logarithmic part.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4th ed., CUP 1927, §12.3. (Gauss's digamma theorem; $\psi(\tfrac14)=-\gamma-\tfrac\pi2-3\log2$.)

*End of Document 145.*
