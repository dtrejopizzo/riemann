# Doc 137 — Adversarial audit of the Local Purity Theorem (Doc 131, Theorem 6.7)

**Program:** Riemann Hypothesis — Phase 46: audit and attacks.
**Audited object:** Theorem 6.7 of `phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md`, with its whole support chain (Def. 2.1, Def. 2.7, Prop. 2.8, Prop. 4.2, Theorem 4.4, Prop. 6.2, Theorem 6.6, Def./Prop. 6.6').
**Mandate:** destroy. Full 5-step protocol executed, only closed-form symbolic computation.

---

## 0. One-line verdict

**SURVIVES WITH ERRATA.** The mathematical content of Theorem 6.7 (H ⟺ |α|=√p ⟺ |c_m|≤2p^{m/2}) is correct in both directions — re-derived from scratch, symbol by symbol — but its formal support chain has **one false proposition (Prop. 2.8(b), conjugation error in the discrete block)** and **one type error (F_{p,α} with α∉ℝ is not "hermitian" under Def. 2.7, so Def. 6.1 and Prop. 6.2 do not apply to it as written)**. Both defects are repairable without touching any computation; the repair is in §4.

---

## 1. Independent re-derivation (without copying the document's proof)

### 1.1. The object, from scratch

Data: prime $p$, $L=\log p$, $\alpha\in\mathbb{C}^\times$ with $1<|\alpha|<p$. Weights
$c_m := \alpha^m + (p/\bar\alpha)^m$, functional
$$W_F(f) = L\sum_{m\in\mathbb{Z}} c_m f(p^m),\qquad f\in C_c^\infty(G),\ G=\mathbb{R}_+^*.$$

**Mirror identity (re-derived).** $c_{-m} = \alpha^{-m} + \bar\alpha^m p^{-m}$ and
$\bar c_m p^{-m} = \bar\alpha^m p^{-m} + (p/\alpha)^m p^{-m} = \bar\alpha^m p^{-m} + \alpha^{-m}$.
**Equal.** ✓ This identity carries all of the hermiticity of the object (see §4, E1–E2).

**Consistency with Def. 2.1.** With $a(p^m)=-Lc_m$ ($m\ge1$), $c=0$, $\omega\equiv-2L$:
- $-P_a(f) = L\sum_{m\ge1}[c_m f(p^m) + \bar c_m p^{-m} f(p^{-m})]$; by the mirror identity $\bar c_m p^{-m} = c_{-m}$, this is $L\sum_{m\ne0} c_m f(p^m)$. ✓
- $-A_\omega(f) = \frac{2L}{2\pi}\int\hat f(\tfrac12+it)\,dt = 2L f(1) = Lc_0 f(p^0)$ (Mellin inversion at $x=1$ on $\mathrm{Re}=\tfrac12$; absolute convergence by Paley–Wiener). ✓
- Design note (not an error): the atom $m=0$ admits two realizations — $\omega\equiv-2L$ or $a(1)=-L$ — i.e. the data→functional map **is not injective**. Harmless here.

**Analytic dictionary (verification of the "Euler" label).** For the Dirichlet polynomial $D(s)=(1-\alpha p^{-s})(1-(p/\bar\alpha)p^{-s})$: $\log D = -\sum_{m\ge1}c_m p^{-ms}/m$, so $-D'/D \leftrightarrow$ coefficient $-Lc_m$ at $p^m$ — exactly the $a$ of the object, supported on $p^{\mathbb N}$: it has an Euler product in the sense of Theorem 1.9. ✓ The zeros of $D$ are $Z(\alpha)\sqcup Z(p/\bar\alpha)$. ✓

### 1.2. Poisson (Theorem 6.6), re-derived

$\alpha=p^\beta e^{i\phi}$, $\rho_k=\beta+i(\phi+2\pi k)/L$; check: $p^{\rho_k}=p^\beta e^{i(\phi+2\pi k)}=\alpha$. ✓
With $F(t):=f(e^t)e^{\beta t}e^{i\phi t/L}\in C_c^\infty(\mathbb{R})$:
$\hat f(\rho_k)=\int F(t)e^{2\pi ikt/L}dt$. Classical Poisson on the lattice $L\mathbb{Z}$ (finite, $C^\infty$ periodization — no convergence subtleties):
$\sum_k\widehat F(2\pi k/L) = L\sum_m F(mL) = L\sum_m \alpha^m f(p^m)$. ✓ The sign of the Fourier convention only relabels $k\mapsto-k$; the bilateral sum is invariant. **Theorem 6.6 correct.**

Spectral pairing: $\sigma Z(\alpha)=Z(p/\bar\alpha)$ because $p^{1-\bar\rho}=p/\overline{p^\rho}=p/\bar\alpha$. ✓ Linear density $N_Z(T)\asymp T$. ✓

### 1.3. Direction ⟸ (purity ⟹ H), closed-form computation

$|\alpha|=\sqrt p \Rightarrow p/\bar\alpha = \alpha$: the two progressions **coincide** — the divisor is $Z(\alpha)$ with multiplicity 2, all on $\mathrm{Re}=\tfrac12$, and $c_m=2\alpha^m$. For $g=f\star\tilde f$ (which lies in $C_c^\infty(G)$):
$$Q_F(f,f)=W_F(g)=2\sum_{\rho\in Z(\alpha)}\hat g(\rho)
=2\sum_{\rho}\hat f(\rho)\,\overline{\hat f(1-\bar\rho)}
=2\sum_{\rho}|\hat f(\rho)|^2\;\ge\;0,$$
using $\widehat{f\star\tilde f}(s)=\hat f(s)\overline{\hat f(1-\bar s)}$ and $1-\bar\rho=\rho$ on the line. Absolute convergence: Paley–Wiener ($|\hat f(\tfrac12+it)|\ll_N(1+|t|)^{-N}$) against linear density. ✓
**Critical point of the audit:** this computation uses ONLY (i) the explicit formula (Poisson, proved) and (ii) $Z\subset\{\mathrm{Re}=\tfrac12\}$. **It does not use at any step that $a$ is real** — relevant for erratum E2: the proof survives even though Prop. 6.2's "hermitian" hypothesis, as typed, fails.

### 1.4. Direction ⟹ (impurity ⟹ ¬H), re-derived

WLOG $\delta'>0$ where $|\alpha|=p^{1/2+\delta'}$ (the swap $\alpha\leftrightarrow p/\bar\alpha$ leaves $c_m$ invariant: verified, $p/\overline{(p/\bar\alpha)}=\alpha$). Test $f=u+\theta\,u(\cdot/p^M)$, $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$, $\chi$ even, $\mathrm{supp}\,\chi\subset[-1,1]$, $\int\chi^2=1$, $\epsilon<L/4$, $\theta\in\mathbb{C}$.

- $g(x)=(f\star\tilde f)(x)=\int f(y)\overline{f(y/x)}(y/x)\,d^*y$: re-derived from $\tilde f(z)=\overline{f(1/z)}z^{-1}$, $\tilde f(x/y)=\overline{f(y/x)}(y/x)$. ✓ (matches the document).
- Support: $g(x)\ne0\Rightarrow\log x\in\{0,\pm ML\}+[-2\epsilon,2\epsilon]$; the only powers $p^m$ reached are $m\in\{0,\pm M\}$ because $2\epsilon<L/2<L$. **No term at $\pm2M$** (the differences of centers of the two bumps are $\{0,\pm ML\}$). ✓
- $g(1)=\int|f|^2y\,d^*y$: disjoint supports ⟹ no cross terms; $\int u^2y\,d^*y=\int e^{\epsilon s}\chi(s)^2ds=1+O(\epsilon)$ and the translated bump gives $|\theta|^2p^M(1+O(\epsilon))$. ✓
- $g(p^M)=\theta\int u(y/p^M)^2(y/p^M)d^*y=\theta(1+O(\epsilon))$ (only overlap: $y\approx p^M$). ✓
- Hermiticity of $g$: from $\tilde g=g$ we get $g(1/x)=x\,\overline{g(x)}$, so $g(p^{-M})=p^M\bar\theta(1+O(\epsilon))$. ✓ (re-derived; matches).
- Assembly, with $c_{-M}g(p^{-M}) = \bar c_M p^{-M}\cdot p^M\bar\theta(1+O(\epsilon)) = \overline{c_M\theta}(1+O(\epsilon))$:
  $$Q_F(f,f)/L = \bigl[\,2(1+|\theta|^2p^M)+2\,\mathrm{Re}(c_M\theta)\,\bigr](1+O(\epsilon)).$$ ✓
- Adversarial phase $\theta=-(\bar c_M/|c_M|)t$, $t>0$: quadratic $2+2p^Mt^2-2|c_M|t$, minimum at $t^*=|c_M|/(2p^M)$:
  $$2+\frac{|c_M|^2}{2p^M}-\frac{|c_M|^2}{p^M}=2-\frac{|c_M|^2}{2p^M}<0\iff|c_M|>2p^{M/2}.$$ ✓ (re-derived term by term; matches).
- Growth: $|c_M|\ge p^{M(1/2+\delta')}-p^{M(1/2-\delta')}=p^{M/2}\cdot2\sinh(M\delta' L)\to\infty\cdot p^{M/2}$ (reverse triangle inequality). ✓
- Order of quantifiers: $M$ is fixed first (fixed negative margin), $\epsilon$ afterward; the constants in $O(\epsilon)$ depend on $M,\theta$ already fixed. **No circularity.** ✓
- **Admissibility of the test:** sum of two $C^\infty$ compactly supported bumps with a complex coefficient — it lies in $C_c^\infty(G;\mathbb{C})$, the exact class of Def. 2.1/6.1 (the class is complex: the involution $\tilde f$ conjugates). ✓ The impurity-detecting test **is indeed in the admissible class**. (Note: if the class were real-valued functions, real $\theta$ would only extract $\mathrm{Re}(c_M)$ and the proof would need equidistribution of $M\phi$; the complex class avoids that gap. Verified that the document uses the complex class throughout.)
- Reality of $Q_F(f,f)$ (needed for "$\ge0$" to make sense): pairing $\pm m$, $c_mg(p^m)+c_{-m}g(p^{-m})=2\,\mathrm{Re}(c_mg(p^m))$ via the mirror identity + $g(1/x)=x\overline{g(x)}$; and $g(1)=\int|f|^2y\,d^*y$ real. **$Q_F(f,f)\in\mathbb{R}$ for every $f$ and every $\alpha$ (even impure and non-real).** ✓

### 1.5. Third leg of the equivalence

$|\alpha|=\sqrt p\Rightarrow|c_m|=2p^{m/2}$ exactly. $|\alpha|=p^{1/2+\delta'}$, $\delta'\ne0$ ⟹ $|c_m|>2p^{m/2}$ as soon as $\sinh(m|\delta'|L)>1$ (large m): the clause "$\forall m\ge1$" fails. ✓ Equivalence correct within the stated domain $1<|\alpha|<p$.

---

## 2. Proof-step-vs-verification table

| # | Step of the document (Theorem 6.7 and support) | Independent verification | Status |
|---|---|---|---|
| 1 | Mirror identity $c_{-m}=\bar c_m p^{-m}$ (6.6') | Re-derived, exact | ✓ |
| 2 | Realization of the atom $m=0$ as $\omega\equiv-2L$ | Inverse Mellin on $\mathrm{Re}=\tfrac12$; PW convergence | ✓ |
| 3 | "$F_{p,\alpha}$ is hermitian" (6.6') | **FALSE under Def. 2.7** for $\alpha\notin\mathbb{R}$: $\bar a\ne a$. True only as σ-symmetry of the functional: $\overline{W_F(\tilde f)}=W_F(f)$ (re-derived via the mirror identity) | ✗ label / ✓ content (E2) |
| 4 | Prop. 2.8(b): $W_{\sigma X}(f)=\overline{W_X(\tilde f)}$ | **FALSE in the discrete block** for non-real $a$: the document's own computation gives $\overline{P_a(\tilde f)}=P_a(f)$, and the document inserts "with $a\mapsto\bar a$" without justification (closed-form counterexample in §4, E1) | ✗ (E1) |
| 5 | One-factor Poisson (Theorem 6.6) | Re-derived with periodization; convention signs harmless | ✓ |
| 6 | Spectral pair $(F_{p,\alpha},Z_F)$, σ-stability of the divisor | $p^{1-\bar\rho}=p/\bar\alpha$; linear density; absolute convergence | ✓ |
| 7 | ⟸ via Prop. 6.2/Theorem 4.4(a) | The computation only uses spectrality + $Z\subset$ line; **the "hermitian" hypothesis of 6.2/4.4 is neither used nor literally satisfied** — survives with the weakened hypothesis | ✓ with typing erratum |
| 8 | Multiplicity 2 in the pure case ($Z(\alpha)=Z(p/\bar\alpha)$) | Counted correctly: factor 2 in the sum of squares | ✓ |
| 9 | $\delta'>0$ WLOG (swap $\alpha\leftrightarrow p/\bar\alpha$) | Same object: $c_m$ invariant | ✓ |
| 10 | Support of the test: $g(p^m)=0$ except $m\in\{0,\pm M\}$ | $2\epsilon<L$; no term at $\pm2M$ | ✓ |
| 11 | Values $g(1),g(p^M),g(p^{-M})$ | Re-derived; weights $y$ and $p^M$ correct | ✓ |
| 12 | Assembly $Q/L=2(1+|\theta|^2p^M)+2\mathrm{Re}(c_M\theta)$ | Matches; the mirror gives exactly the conjugate, no double counting | ✓ |
| 13 | Minimization: $2-|c_M|^2/(2p^M)<0\iff|c_M|>2p^{M/2}$ | Arithmetic redone | ✓ |
| 14 | Growth of $|c_M|$ and order $M\to\epsilon$ | $\sinh$; quantifiers in correct order | ✓ |
| 15 | Test in the admissible class | $C_c^\infty(G;\mathbb{C})$, yes | ✓ |
| 16 | Reality of $Q(f,f)$ for impure objects (implicit in "¬H") | Proved via the mirror; the document does not state it but uses it | ✓ (minor gap, see E4) |
| 17 | Corollary "Euler ⇏ H" | Follows from the theorem + Theorem 1.9 (support of $a$ on $p^{\mathbb N}$, verified via $D(s)$) | ✓ |

**Specific search for the type of error that killed W_λ** (sign / boundary / Abel summation swap): the only sum exchange is Poisson over finite $C^\infty$ periodization (harmless) and the reordering $\sum_\rho$ absolutely convergent (PW + linear density). The only boundary is the atom $m=0$, counted ONCE (as $\omega$, not as $a(1)$ — no double counting, verified in step 2/12). The only sign error found is in the **conjugation** of Prop. 2.8(b) (E1) — and it is not load-bearing for 6.7.

---

## 3. Edge cases

- **$\alpha=0$:** outside the domain ($|\alpha|>1$); also $p/\bar\alpha$ is undefined — the object does not exist. The statement is well bounded.
- **$|\alpha|=1$ (boundary):** excluded from the statement. Boundary audit: the object is defined, $\delta'=-\tfrac12$; the swap gives $\delta'=+\tfrac12$ and $|c_M|\ge p^M-1>2p^{M/2}$ for $M\ge2$: the test kills H there too. The restriction $1<|\alpha|<p$ is a scope choice, not concealment of a pathological case. ✓
- **non-real $\alpha$:** the central case (genuine Ramanujan). This is exactly where E1/E2 surface (the object is not Def-2.7-hermitian). The content survives: $Q$ is hermitian and the equivalence holds, via the repair of §4. In ⟹, the adversarial phase $\theta=-\bar c_M t/|c_M|$ is what makes the test robust against complex $c_M$. ✓
- **$\alpha=\pm\sqrt p$ (real pure):** $c_m=2(\pm\sqrt p)^m$, hermitian even under Def. 2.7; everything consistent. ✓
- **Multiplicities:** pure case = one progression with multiplicity 2; Theorem 4.4 allows multiplicities and the factor 2 is counted correctly. ✓
- **$p=2$:** $L=\log2$, $\epsilon<L/4\approx0.173>0$: the test fits; nothing degenerates. ✓
- **Minimal-support tests:** a single bump ($\theta=0$) gives $Q/L=2(1+O(\epsilon))>0$ — a single bump never detects impurity (consistent with §6.3: the two-frequency Mertens mechanism is needed). The two-bump test is minimal and sufficient. ✓
- **Both directions in each case:** verified; no case in the domain breaks either direction.

---

## 4. Errata found and proposed repair

### E1 (real erratum, false proposition): Prop. 2.8(b)

**Document statement:** $W_{\sigma X}(f)=\overline{W_X(\tilde f)}$ with $\sigma X=(\bar a,\sigma c,\omega)$.
**The error:** in the discrete block, the document's own computation reaches $\sum_n[a(n)f(n)+\bar a(n)n^{-1}f(1/n)]$ — which is **$P_a(f)$, literally** — and then claims "with $a\mapsto\bar a$ — exactly $P_{\bar a}(f)$" **without any line of the computation producing that conjugation**. The correct identity is
$$\overline{P_a(\tilde f)} = P_a(f)\qquad\text{for EVERY }a\ (\text{not }P_{\bar a}(f)),$$
because the mirror term $\bar a(n)n^{-1}f(1/n)$ of Def. 2.1 already hardcodes the σ-symmetry of the discrete block.
**Closed-form counterexample:** $a$ supported at $n_0=2$ with $a(2)=i$. Then $P_a(\tilde f)=\tfrac i2\overline{f(1/2)}-i\overline{f(2)}$, so $\overline{P_a(\tilde f)}=if(2)-\tfrac i2 f(1/2)=P_a(f)$; while $P_{\bar a}(f)=-if(2)+\tfrac i2f(1/2)=-P_a(f)\ne P_a(f)$ for generic $f$. Prop. 2.8(b) is false whenever $a\ne\bar a$.
**Repair:** $\overline{W_X(\tilde f)} = W_{X'}(f)$ with $X'=(a,\,\sigma c,\,\bar\omega)$ — **only the polar block and $\omega$ transform; the discrete one is σ-invariant by construction.** For real $a$ (all σ-fixed objects of Def. 2.7, including $\zeta_{\mathrm{ob}}$ with $a=\Lambda$) the original statement is correct: that is why the erratum went unnoticed.

### E2 (type error): "hermitian" in 6.6'/6.1/6.2 vs Def. 2.7

Def. 2.7 requires $\sigma X=X$, i.e. **$a$ real**. For $\alpha\notin\mathbb{R}$ (and $\alpha\ne$ real case), $a(p^m)=-Lc_m$ is complex: $F_{p,\alpha}$ **is not hermitian under Def. 2.7**, even though 6.6' declares it to be. Formal consequence: Def. 6.1 (Axiom H, defined "for hermitian objects") and Prop. 6.2/Theorem 4.4, invoked in direction ⟸, **do not literally apply to the object of Theorem 6.7** in its generic case.
**Why it does not kill the theorem:** (i) $Q_F(f,f)$ is real for every $f$ (proved in §1.4 via the mirror identity), so H is well posed; (ii) the proof of 4.4(a) only uses spectrality + σ-stability of $Z$, never real $a$; (iii) by polarization, $Q_X$ is hermitian for **every** $a$ as soon as $c$ is σ-stable with conjugate weights and $\omega$ is real — a direct consequence of the identity corrected in E1.
**Repair (the natural one):** weaken "hermitian" to **σ-symmetry of the functional**: $X$ is hermitian if $\overline{W_X(\tilde f)}=W_X(f)$ for every $f$ — equivalently (with E1 corrected): $c$ σ-stable with conjugate weights and $\omega$ real, **with no condition on $a$**. With this definition: Prop. 2.8(c) holds with weaker hypotheses (same proof), $F_{p,\alpha}$ is hermitian for every $\alpha$, and Theorems 4.4, 6.2, 6.3, 6.7 are correctly typed without changing a single line of their proofs. Note that **P48 already uses exactly this definition** (its "hermitian" Lemma: $\overline{W(\tilde f)}=W(f)$, proved via the mirror identity) — the paper self-repaired without stating so.

### E3 (minor carry-over): Prop. 4.2(b)

Inherits E1: what is provable is that $(\,(a,\sigma c,\omega),\,\sigma Z\,)$ is spectral (same $a$, not $\bar a$). For the catalog's objects (real $a$ or $F_{p,\alpha}$, where the symmetry is given by the mirror identity) the consequences used do not change.

### E4 (cosmetic)

(i) In the proof of 6.7 there remains a truncated draft sentence: "$c_m=2p^{m/2}e^{im\phi}\cos(0)$… more precisely". (ii) The reality of $Q_X(f,f)$ for impure objects (needed for "¬H" to mean "there exists $f$ with $Q<0$" and not "Q is not real") is used without being stated; it deserves one line (the one in §1.4 of this audit).

### What was sought and NOT found

No sign error in the computations of 6.6/6.6'/6.7; no illegitimate sum exchange; no double counting of the diagonal atom; no omitted support term ($\pm2M$ verified); the adversarial test is in the admissible class; the quantifiers $M\to\epsilon$ are in correct order. Direction ⟸ was closed with the explicit form $Q=2\sum|\hat f(\rho)|^2$ and ⟹ with the exact minimum $2-|c_M|^2/(2p^M)$. Unlike the W_λ case, here the positivity of the pure case is not a cancellation miracle but a manifest sum of squares with exact Cauchy–Schwarz at the boundary.

---

## 5. Consequences for P48 (`06-papers/P48-weil-positivity-finite-primes/`)

1. **P48's base theorem is confirmed.** P48 §"Local purity" re-proves 6.7 in a self-contained way; every step matches the re-derivation of §1 of this audit. The $n$-prime theorem (H ⟺ purity of all factors) rests on the one-prime case + additivity $Q_{X_1\star X_2}=Q_{X_1}+Q_{X_2}$, and the local link is solid.
2. **P48 does NOT inherit E1/E2.** Its "hermitian" Lemma defines hermiticity as $\overline{W(\tilde f)}=W(f)$ and proves it via $\bar c_{-m}p^m=c_m$ — exactly the repaired notion of E2. It does not cite Prop. 2.8(b) of Doc 131. No correction to P48 is needed as a result of this audit.
3. **Recommended action (not urgent):** (i) fix Prop. 2.8(b) and Def. 2.7 in Doc 131 per §4 (and log it in `06-papers/ERRATA.md`, alongside the Phase 38 errata); (ii) in P48, if extra robustness is desired, add the explicit reality line for $Q(f,f)$ for impure factors (E4.ii) — it is a three-line computation already done here.
4. **Stability of the structural corollary.** "Euler ⇏ H; the discriminator is purity" remains intact and, with E2 repaired, is better founded: the class where H is well posed is strictly larger than that of Def. 2.7, and the complex impure counterexamples legitimately live within it.

---

## References

**Internal (backward-only):** Doc 131 (audited object); Doc 107 (test class, Paley–Wiener, thickened kernel); Doc 110 (class ℱ); `06-papers/P48-weil-positivity-finite-primes/main.tex` (hermitian Lemma, local purity Theorem); Phase 38 (W_λ≥0 precedent, ERRATA.md).
**Literature [DATA]:** A. Weil, Comm. Sém. Math. Lund (1952); E. Bombieri, Rend. Mat. Acc. Lincei (9) 11 (2000) (Weil's criterion); H. Montgomery, R. Vaughan, *Multiplicative Number Theory I*, 2007 (Mertens mechanism); E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §3.

*End of Document 137.*
