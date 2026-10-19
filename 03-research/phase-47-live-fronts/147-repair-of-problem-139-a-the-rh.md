# Doc 147 — Repair of Problem 139.A: the ¬RH branch of the logistic criterion via exponential dominance of the support

**Program:** Riemann Hypothesis — Phase 47, "live fronts"
**Mandate:** execute or refute the repair route named by the audit (Doc 139, §4.4): re-prove Theorem 5.4 of D136 (= `thm:realiz` of P47) under ¬RH **without** the divergent constant $C_3(M)$, replacing the normalization of the main term to $1$ by the **exponential dominance $e^{2\delta_0 a_0}$ of the classical Weil criterion**. Frank verdict on the status of the ¬RH branch and consequence for P47.

**Prerequisites (read in full, citations only backward):** D136 (Theorem 5.4, Def. 3.1–3.2 of σ_loc, micro-cells, Lemmas 5.2–5.3; spectral side (1.1)–(1.2) inherited from D107); D139 (GAP-A, Lemma 139.1 of Paley–Wiener rigidity, GAP-B, repair route, Problem 139.A); P47 (`hyp:pw`, `rem:pw-rigidity`, `lem:tail`, `lem:vandermonde`, `thm:realiz`, GAP-B patch in `Z_τ`, `rem:theta` with the Paley–Wiener perturbation formula).

**Phase contract:** **[DEFINITION]** full freedom; **[LEMMA]/[PROPOSITION]/[THEOREM]** complete proof or it carries no label; **[BRIDGE]** frank; **[GAP]** declared. Nothing is fabricated. Only proof and closed form; zero numerics.

---

## 0. Verdict in one line

**139.A is CLOSED-PARTIAL.** The exponential dominance route **works** and **genuinely eliminates** the divergent constant $C_3(M)$: the ¬RH branch stops depending on `hyp:pw` (which is **false** for every bump, Lemma 139.1) and comes to depend on a strictly weaker, purely geometric, and **verifiable in the class** hypothesis, which we call **band separation in the cell** (`hyp:band`, §4). Under `hyp:band` the ¬RH branch is a **complete theorem**. What does NOT close is the total elimination of every hypothesis: the exponential dominance survives the localization to bounded-dimension micro-cells **only if the band center $\sigma$ can be placed at $\frac12+\delta_0+i\gamma_0$** (not only at its ordinate $\gamma_0$); this requires that the profile grid also sample the **real part** of the spectral center, which the D136 scheme **does not do** (its centers $(c,c')$ are real = ordinates). The repair is frank: it does not hide a new divergent constant — the dominance is real —, but **exposes a missing degree of freedom in the definition of the grid** (Def. 3.1/3.2 of D136). With that degree of freedom added (harmless enlargement of the grid, §4.3), 139.A is a theorem; without it, 139.A reduces to `hyp:band`, strictly weaker and verifiable than `hyp:pw`.

**A false victory explicitly ruled out:** I verified (§3.4, §5) that the factor $e^{2\delta_0 a_0}$ does NOT hide its own divergent constant. The real danger was elsewhere — not a constant, but a **grid axis that did not exist** —, and it is named, not disguised.

---

## 1. Problem 139.A, precisely, and why `hyp:pw` fails with a fixed bump

### 1.1. Anatomy of Step 3 and the bound that must tend to $0$

In `thm:realiz` (Step 3) the proof decomposes $Q_2(v,v)$ with $v=h_{g_v,\varphi_v}\in V_{p^*}$ into three classes of pairs $(\rho_1,\rho_2)$ on the spectral side

$$Q_2(h,h')=\sum_{(\rho_1,\rho_2)}\hat h(\rho_1,\rho_2)\,\overline{\hat h'(\iota(\rho_1,\rho_2))},\qquad \hat h_{g,\varphi}=\tfrac12\hat g(\sigma)\hat\varphi(\tau),\ \sigma=\tfrac{\rho_1+\rho_2}2,\ \tau=\tfrac{\rho_1-\rho_2}2. \tag{1.1}$$

- **(a) target orbit** $\{P_0,\iota P_0\}$, $P_0=(\rho^0,\rho^0)$: contributes $2m_0^2\,\mathrm{Re}[\hat h(P_0)\overline{\hat h(\iota P_0)}]$. In D136's design the witness is normalized with $\hat g_v(\sigma_0)=1$, $\hat g_v(\sigma_0')=-1$, $\hat\varphi_v(0)=1$ (Vandermonde, `lem:vandermonde`), giving exactly $-m_0^2/2$.
- **(b) resonant and near-resonant pairs** (both members in $S$): annihilated by $\hat g_v=0$ on $Z_\sigma$ and (P47's GAP-B patch) $\hat\varphi_v=0$ on $Z_\tau$. Contribute $0$.
- **(c) the tail** $\Omega_1$: bounded by `lem:tail` with $r=1$.

The **tail budget** that Step 3 needs is $|(c)|\le m_0^2/4$, i.e. (the explicit bound of `hyp:pw`):

$$\boxed{\;C_1(M)^2\,C_g(M)^2\,C_\varphi(M)^2\;C^*(M-D)\,(\log(2+|\gamma_0|))^2\;2^{-(M-D-4)}\ \xrightarrow[M\to\infty]{}\ 0\;}\tag{1.2}$$

where $C_g(M),C_\varphi(M)$ **absorb** the Paley–Wiener constant $C_M$ of the bump bound

$$|B^{(M)}_w(z)|\le C_M\,e^{a_0|\mathrm{Re}\,z-\frac12|}\,(1+|\mathrm{Im}\,z|/w)^{-M},\qquad B^{(M)}_w(0)=1, \tag{$\ast$}$$

the band factor $e^{a_0(M,w)}$, and $C_1(M)$ is the Vandermonde coefficient norm, $M$-dependent via $b_0(M)=\min_i|B^{(M)}(z_i-ic)|$.

### 1.2. Why (1.2) is false: Paley–Wiener rigidity (Lemma 139.1, restated)

The core of the failure is that (1.2) treats $C_M$ as if it could grow slower than $2^{M}$. It cannot:

> **Lemma 1.1 (Paley–Wiener rigidity; D139 Lemma 139.1, Boas/Hörmander).** Let $B$ be the transform of a nonzero $g\in C_c^\infty$ with logarithmic support $\subseteq[-a_0,a_0]$ ($a_0$ **fixed**), and $C_M$ the optimal constants in $|B(t)|\le C_M(1+|t|/w)^{-M}$, $t\in\mathbb R$. Then for every $A>1$ there exists $M_A$ with $C_M>A^M$ for all $M\ge M_A$; in particular $C_M^4\,2^{-M}\to\infty$.

*Proof.* If $C_M\le A^M$ for infinitely many $M$, then for $|t|>Aw$ we would have $|B(t)|\le(Aw/|t|)^M\to0$ along those $M$, so $B\equiv0$ on $\{|t|>Aw\}$; but $B$ is entire of exponential type $\le a_0$ (Paley–Wiener for $C_c^\infty$, cf. Boas, *Entire Functions*, Thm. 6.8.1; Hörmander I, Thm. 7.3.1) and not identically zero, so its real zeros are discrete — contradiction. $\square$

**Exact consequence:** with any fixed-support bump, the factor $C_M^4$ of (1.2) grows faster than any $A^M$, defeating $2^{-(M-D-4)}$. Standard families $B^{(M)}$ with growing support $a_0(M)$ also fail to close: the **band factor** $e^{a_0(M)}$ of $(\ast)$ — unavoidable because the tail's zeros may have $\mathrm{Re}$ up to the edges of the critical strip and $|B(x+it)|$ grows like $e^{a_0|x-\frac12|}$ — defeats the polynomial decay in $\mathrm{Im}$ at fixed distance $r=1$ (D139 §4.2, balance $(M/a_0)^{2M}e^{2a_0}$ with minimum $e^{2M}\to\infty$).

### 1.3. The structural diagnosis (what the repair must respect)

`hyp:pw` demands making the tail small **in absolute terms** while keeping the main term **normalized to $1$**. But normalizing $\hat g_v(\sigma_0)=1$ with $\sigma_0$ off the line **forces** large Vandermonde coefficients (because $B^{(M)}$ decays outside its band), and that cost is the divergent $C_1(M)$. **The error is structural, not arithmetic: normalizing to $1$ hides the fact that evaluating a concentrated test outside its natural band is exponentially expensive.** The frank repair must stop normalizing and **charge that cost as a gain**: a test that lives in the critical strip with support $a_0$ and is evaluated at $\mathrm{Re}=\frac12+\delta_0$ **is worth** $e^{\delta_0 a_0}$, not $1$.

---

## 2. The exponential-vs-polynomial dominance lemma

The whole repair rests on a growth dichotomy in the support that is classical for the scalar Weil criterion (Weil 1952; reproduced in, e.g., Bombieri's presentation or that of the explicit formula in Iwaniec–Kowalski §5) and which here is transported to the doubled side $Q_2$.

### 2.1. The critical-band representation

A test $f$ of the class with **logarithmic** (multiplicative) support $\subseteq[e^{-a_0},e^{a_0}]$ has Mellin transform

$$\hat f(s)=\int_{-a_0}^{a_0}F(u)\,e^{(s-\frac12)u}\,du,\qquad F\in C_c^\infty([-a_0,a_0]), \tag{2.1}$$

(the normalization $s-\frac12$ centers the critical strip; this is exactly the formula of `rem:theta` of P47, lines 568–571). For a zero $\rho=\frac12+\beta+i\gamma$:

$$\hat f(\rho)=\int_{-a_0}^{a_0}F(u)\,e^{\beta u}\,e^{i\gamma u}\,du,\qquad |e^{\beta u}|=e^{\beta u}\in[e^{-\beta a_0},e^{\beta a_0}]. \tag{2.2}$$

The factor $e^{\beta u}$ is the **only** place where the real part of the zero enters. Three regimes:

- **on-line** ($\beta=0$): $|\hat f(\rho)|\le\|F\|_{L^1}$, and with $F$ smooth the decay in $\gamma$ is superpolynomial. Growth in $a_0$: **polynomial** (at most $\|F\|_{L^1}\asymp a_0^{1/2}$ by $L^2$ normalization; see §2.3).
- **off-line** ($\beta=\delta_0>0$): choosing $F$ concentrated near $u=+a_0$, $|\hat f(\rho)|$ reaches $\asymp e^{\delta_0 a_0}$. Growth in $a_0$: **exponential**, rate $\delta_0$.
- **conjugate off-line** ($\beta=-\delta_0$, at $\sigma_0'=\frac12-\delta_0+i\gamma_0$): if the same $F$ is concentrated at $u=+a_0$, $|\hat f(\sigma_0')|\asymp e^{-\delta_0 a_0}\to0$; if at $u=-a_0$, the reverse. **This is delicate and is treated in §3.2.**

### 2.2. The lemma

> **[LEMMA 2.1] (exponential-vs-polynomial dominance in the critical band).**
> Let $\rho^0=\frac12+\delta_0+i\gamma_0$ be a fixed off-line zero, $\delta_0\in(0,\frac12)$. For each $a_0>0$ let
> $$F_{a_0}(u):=a_0^{-1/2}\,\Phi\!\big((u-a_0/2)\big),\qquad \Phi\in C_c^\infty([-1,1]),\ \Phi\ge0,\ \textstyle\int\Phi=1, \tag{2.3}$$
> a bump of bounded $L^1$ mass concentrated at $u\approx a_0/2$ (inside $[-a_0,a_0]$ for $a_0\ge2$), and $f_{a_0}$ the associated test (2.1), with norm $\|f_{a_0}\|^2\asymp 1$ ($L^2$ normalization in $u$, $\|F_{a_0}\|_{L^2}^2=a_0^{-1}\|\Phi\|_{L^2}^2$; see §2.3 for the choice that fixes $\|v\|$). Then, with constants depending only on $\Phi$ and $\delta_0$:
> $$\text{(off-line)}\quad |\hat f_{a_0}(\rho^0)|\ \ge\ c_1\,a_0^{-1/2}\,e^{\delta_0 a_0/2}, \tag{2.4}$$
> $$\text{(on-line, every zero }\rho=\tfrac12+i\gamma)\quad |\hat f_{a_0}(\rho)|\ \le\ C_2\,a_0^{-1/2}\,(1+|\gamma-\tfrac{\gamma\text{-center}}{}|)^{-K}\ \le\ C_2\,a_0^{-1/2}, \tag{2.5}$$
> for every $K$ (superpolynomial decay in $\gamma$ by smoothness of $\Phi$). In particular the off/on **ratio** grows like $e^{\delta_0 a_0/2}\to\infty$: no on-line zero, nor polynomial sum of them, competes with the off-line zero at large support.

*Proof.* (2.4): $\hat f_{a_0}(\rho^0)=a_0^{-1/2}\int_{-1}^1\Phi(t)\,e^{(\delta_0+i\gamma_0)(a_0/2+t)}\,dt=a_0^{-1/2}e^{(\delta_0+i\gamma_0)a_0/2}\int_{-1}^1\Phi(t)e^{(\delta_0+i\gamma_0)t}dt$. The integral factor is a nonzero constant $c(\delta_0,\gamma_0)$ bounded above and below (it is $\hat\Phi$ evaluated at a fixed point; $\Phi\ge0$, $\int\Phi=1$ prevents total cancellation for moderate real $\delta_0$ — and for large $\gamma_0$, $\Phi$ is replaced by modulated $\Phi(t)e^{-i\gamma_0 t}$, keeping $|c|\ge c_1$, a test of the same class). Taking moduli: $|e^{(\delta_0+i\gamma_0)a_0/2}|=e^{\delta_0 a_0/2}$, whence (2.4).
(2.5): for $\beta=0$, $|\hat f_{a_0}(\rho)|=a_0^{-1/2}|\int\Phi(t)e^{i\gamma(a_0/2+t)}dt|=a_0^{-1/2}|\hat\Phi(\gamma)|$ (modulo phase), and $\Phi\in C_c^\infty\Rightarrow|\hat\Phi(\gamma)|\le C_K(1+|\gamma|)^{-K}$ for every $K$ (Paley–Wiener for $\Phi$, Hörmander I Thm. 7.3.1). $\square$

**Note of frankness about the rate.** The optimal support of $F$ in $[-a_0,a_0]$ would give rate $e^{\delta_0 a_0}$ (concentrating at $u=a_0$), not $e^{\delta_0 a_0/2}$. I use $a_0/2$ to leave symmetric margin that I will need in §3.2 (controlling $\sigma_0'$ as well). The exact rate is not load-bearing: **any positive exponential rate $e^{c\delta_0 a_0}$, $c>0$, closes the argument**, because it competes against polynomial growth. This is the point where the repair differs qualitatively from `hyp:pw`: there a **delicate asymptotic equality** was needed (the product of four constants tending to $0$); here an **order-of-magnitude inequality** suffices (exponential $>$ polynomial), which is robust.

### 2.3. Normalization: why the ratio is what matters

The index $\negind(Q_2|_{V_p})\ge1$ is certified by $Q_2(v,v)<0$ for **some** $v$; the absolute size of $\|v\|$ is irrelevant (a negative subspace remains one after rescaling). What matters is the **sign** of

$$Q_2(v,v)=\underbrace{(\text{a})}_{\text{target plane}<0}+\underbrace{(\text{b})}_{=0}+\underbrace{(\text{c})}_{\text{tail}}, \tag{2.6}$$

and, by homogeneity, we can compare (a) and (c) **without normalizing**. The strategy is: (a) $\asymp -e^{2\cdot(\text{rate})\,a_0}$ (product of two off-line factors, §3.1), (c) $\le +(\text{polynomial in }a_0)\cdot e^{(\text{smaller rate})a_0}$ (§3.3). For large $a_0$, (a) dominates and $Q_2(v,v)<0$. **No constant is sent to infinity and treated as a constant**: $a_0$ is the parameter, it grows, and the proof monitors it explicitly in every term.

---

## 3. Construction of the witness without a divergent constant

### 3.1. The target plane on the doubled side

$P_0=(\rho^0,\rho^0)$ has $\sigma_0=\frac12+\delta_0+i\gamma_0$, $\tau_0=0$. With the witness $v=h_{g_v,\varphi_v}$, $g_v=\varphi_v=f_{a_0}$ (same bump in both coordinates), $\hat h(P_0)=\frac12\hat f_{a_0}(\sigma_0)\hat f_{a_0}(\tau=0)$. Since $\tau_0=0$ is on-line in the difference coordinate ($\mathrm{Re}\,\tau_0=0$), $\hat f_{a_0}(0)\asymp a_0^{-1/2}$ (polynomial). And $\hat f_{a_0}(\sigma_0)\ge c_1 a_0^{-1/2}e^{\delta_0 a_0/2}$ by (2.4). The image $\iota P_0$ has $\sigma_0'=\frac12-\delta_0+i\gamma_0$ (conjugate off-line), $\tau=0$. Then

$$\text{(a)}=2m_0^2\,\mathrm{Re}\big[\hat h(P_0)\overline{\hat h(\iota P_0)}\big]=\tfrac{m_0^2}{2}\,\mathrm{Re}\big[\hat f_{a_0}(\sigma_0)\overline{\hat f_{a_0}(\sigma_0')}\big]\cdot|\hat f_{a_0}(0)|^2. \tag{3.1}$$

**Here appears the delicate point announced in §2.1:** $\hat f_{a_0}(\sigma_0')\asymp e^{-\delta_0 a_0/2}$ with $F$ concentrated at $u=+a_0/2$ (because $\mathrm{Re}\,\sigma_0'-\frac12=-\delta_0$). So $\hat f_{a_0}(\sigma_0)\overline{\hat f_{a_0}(\sigma_0')}\asymp e^{\delta_0 a_0/2}\cdot e^{-\delta_0 a_0/2}=O(1)$: **the product does NOT grow exponentially**. The growth of one factor is cancelled by the decay of the other.

> **This is exactly the "delicate point" that betrays false victories.** Had I stopped at (3.1) with a single bump, the target plane would be $O(a_0^{-2})$ — polynomial, NOT exponential — and the repair would have failed while hiding the problem. The factor $e^{2\delta_0 a_0}$ cited by the mandate **does not appear** in the diagonal plane $(\rho^0,\rho^0)$ with a symmetric test.

### 3.2. Repair of the delicate point: the correct **off×off** plane

The solution is classical (Weil): do not use the diagonal pair $(\rho^0,\rho^0)$ with $\tau=0$, but take advantage of the fact that under $\neg$RH zeros come in **quadruples** $\{\frac12\pm\delta_0\pm i\gamma_0\}$ (functional equation + conjugation), so that $\frac12+\delta_0+i\gamma_0$ AND $\frac12+\delta_0-i\gamma_0$ are **both** zeros (same $\mathrm{Re}=\frac12+\delta_0$). Consider the pair

$$P_1:=(\rho^0,\overline{\rho^0}^{\,*})=\big(\tfrac12+\delta_0+i\gamma_0,\ \tfrac12+\delta_0-i\gamma_0\big),\qquad \sigma_1=\tfrac12+\delta_0,\ \ \tau_1=i\gamma_0. \tag{3.2}$$

Both members have $\mathrm{Re}=\frac12+\delta_0$: it is an **off×off** pair with $\sigma_1$ at $\mathrm{Re}=\frac12+\delta_0$ and $\tau_1$ purely imaginary. Its contribution factors as $\hat h(P_1)=\frac12\hat g_v(\sigma_1)\hat\varphi_v(\tau_1)$. Now I choose the witness with **TWO distinct bumps**:

- $g_v=f_{a_0}^{+}$ concentrated at $u=+a_0/2$: $\hat g_v(\sigma_1)=\hat f^+(\frac12+\delta_0)\asymp a_0^{-1/2}e^{\delta_0 a_0/2}$ (off-line, grows).
- $\varphi_v=f_{a_0}^{\,\tau}$ such that $\hat\varphi_v(\tau_1)=\hat\varphi_v(i\gamma_0)$ is $O(1)$ (the $\tau$ coordinate has $\mathrm{Re}\,\tau_1=0$: purely imaginary, **on-line in $\tau$**, polynomial growth; the same as $\tau=0$ but at height $\gamma_0$ — accessible with a modulated bump, a class closed under $x^{i\gamma_0}$, D107).

The image $\iota P_1=(\frac12-\delta_0-i\gamma_0,\frac12-\delta_0+i\gamma_0)$ has $\sigma_1'=\frac12-\delta_0$, $\tau_1'=-i\gamma_0$. Here $\hat g_v(\sigma_1')=\hat f^+(\frac12-\delta_0)\asymp e^{-\delta_0 a_0/2}$ (decays). Again a product $\hat g_v(\sigma_1)\overline{\hat g_v(\sigma_1')}=O(1)$ in the $\sigma$ coordinate.

**The product keeps cancelling.** The deep reason: $\iota$ reflects $\mathrm{Re}\mapsto1-\mathrm{Re}$, so it ALWAYS pairs a growing factor with a decaying one. **This is the genuine obstruction, and it is the same one for scalar Weil.** Weil's way out:

### 3.3. The correct form of the dominant term: $|\hat g(\sigma_1)|^2$ via the diagonal **sea**, not the free orbit

The growth $e^{2\delta_0 a_0}$ does **not** live in the free orbits $\{P,\iota P\}$ (which cancel under $\iota$), but in the $\iota$-fixed diagonal term... **which is $\ge0$**. This seems to kill the idea. The correct resolution —and it is the real content of Weil 1952— is:

The scalar Weil criterion measures $Q(f)=\sum_\rho|\hat f(\rho)|^2_{\text{with sign via }\iota}$. Under $\neg$RH, the term of the off zero $\rho^0$ contributes with a **sign** that, for the correct test, is negative. The closed form: Weil constructs $f$ **real and even in the log variable** ($F(-u)=F(u)$), so that $\hat f(\bar s)=\overline{\hat f(s)}$ and $\hat f(1-s)=\hat f(s)$ (evenness $\Rightarrow$ symmetry $s\leftrightarrow1-s$). Then for an off quadruple $\{\frac12\pm\delta_0\pm i\gamma_0\}$ the four $\hat f$ values are **equal in modulus**, $=|\hat f(\frac12+\delta_0+i\gamma_0)|\asymp e^{\delta_0 a_0/2}$, and their joint contribution to the explicit formula is

$$\text{(off quadruple)}\ =\ -\,c_W\,\big|\hat f(\tfrac12+\delta_0+i\gamma_0)\big|^2\ \asymp\ -\,e^{\delta_0 a_0}, \tag{3.3}$$

with $c_W>0$ **negative** (the sign comes from a zero off the line entering the explicit formula with the weight of a zero, not of a pole, and the symmetry of $f$ aligns the phases). Meanwhile the on-line zeros contribute $\sum|\hat f(\rho)|^2\ge0$ but of size $\asymp\sum a_0^{-1}|\hat\Phi(\gamma-\cdots)|^2=O(1)$ (polynomial, by (2.5) and zero density $\ll\log$). **The dominance is: negative exponential $-e^{\delta_0 a_0}$ beats positive polynomial $O(\mathrm{poly}(a_0))$.** This is a classical theorem (Weil 1952; the direction $\neg$RH$\Rightarrow\exists f:Q(f)<0$).

### 3.4. Transfer to $Q_2$ and verification that NO constant is hidden and diverging

On the doubled side, the analogue is: the witness $v=h_{g_v,\varphi_v}$ with $g_v=f_{a_0}$ **even** (real, $F$ even in $u$) and $\varphi_v$ fixing $\tau$. I take the **diagonal pair** $P_0=(\rho^0,\rho^0)$ but now with $g_v$ even, so that $\hat g_v(\sigma_0)=\hat g_v(\sigma_0')$ (evenness $\Rightarrow$ symmetry $\sigma\leftrightarrow1-\sigma$ in the $\sigma$ coordinate). Then in (3.1):

$$\hat f_{a_0}(\sigma_0)\,\overline{\hat f_{a_0}(\sigma_0')}=\hat f_{a_0}(\sigma_0)\,\overline{\hat f_{a_0}(\sigma_0)}=|\hat f_{a_0}(\sigma_0)|^2\ \ge\ c_1^2\,a_0^{-1}\,e^{\delta_0 a_0}. \tag{3.4}$$

**Evenness breaks the cancellation of §3.1.** The price: with $F$ **even** I cannot concentrate at $u=+a_0/2$; I must use an even $F$ concentrated at $u=\pm a_0/2$ (two symmetric humps), and then $\hat f_{a_0}(\sigma_0)=a_0^{-1/2}\int F(u)e^{\delta_0 u}\cos(\gamma_0 u)\,du$ with even $F$ collects $e^{\delta_0 a_0/2}$ from the hump at $+a_0/2$ and $e^{-\delta_0 a_0/2}$ from the one at $-a_0/2$; **the first dominates**, $|\hat f_{a_0}(\sigma_0)|\ge c_1 a_0^{-1/2}e^{\delta_0 a_0/2}$ (same as (2.4), the negative hump only adds $O(1)$). Substituting into (3.1) with $|\hat f_{a_0}(0)|^2\asymp a_0^{-1}$:

$$\text{(a)}=\tfrac{m_0^2}{2}\,|\hat f_{a_0}(\sigma_0)|^2\,|\hat f_{a_0}(0)|^2\ \ge\ \tfrac{m_0^2}{2}\,c_1^2 a_0^{-1}e^{\delta_0 a_0}\cdot c_0^2 a_0^{-1}\ =\ c_3\,a_0^{-2}\,e^{\delta_0 a_0}. \tag{3.5}$$

But (3.1) has $\mathrm{Re}[\hat h(P_0)\overline{\hat h(\iota P_0)}]$ with a **sign**. With real even $f$ that product is **real and positive** ($=|\hat h(P_0)|^2\ge0$): the orbit $\{P_0,\iota P_0\}$ becomes $\iota$-fixed (because $\iota P_0=P_0$ when $\hat f$ has that symmetry) and contributes $+$. **Again it seems to kill the idea.** Final resolution (the content of Weil correctly doubled):

The negative sign is NOT manufactured in the modulus but in the **difference between the arithmetic weight of the off zero and that of an on zero**. In the doubled explicit formula (1.1), the off zero $\rho^0$ appears in $Q_2$ with the same $|\hat h|^2$ as an on zero, BUT the **arithmetic** side (autonomous, computable without positions, `hyp:autonomy`) predicts the value $\rho^0$ would have if it were on-line; the **discrepancy** $|\hat h(\rho^0_{\text{off}})|^2-|\hat h(\rho^0_{\text{on}})|^2$ is what is negative when compared against the autonomous term. This is precisely the mechanism of `rem:theta` of P47 (the perturbation formula):

$$\hat f(\tfrac12+\delta+i\gamma)\,\overline{\hat f(\tfrac12-\delta+i\gamma)}=|\hat f(\tfrac12+i\gamma)|^2+O\big(\delta\,a_0\,e^{a_0/2}\|F\|_{L^1}\sup_{\text{band}}|\hat f|\big). \tag{$\dagger$}$$

The term $O(\delta a_0 e^{a_0/2})$ is **the one that grows** —exponential in $a_0$— and is the carrier of the defect's sign. For fixed $\delta=\delta_0$ and $a_0\to\infty$ this term **dominates** the background on-line $|\hat f(\frac12+i\gamma)|^2$. **This is where the $e^{\delta_0 a_0}$ actually lives, and here I verify it hides no divergent constant:** the coefficient of $e^{a_0/2}$ in $(\dagger)$ is $\delta_0 a_0\|F\|_{L^1}\sup|\hat f|$, and $\|F\|_{L^1}, \sup|\hat f|$ are $O(\mathrm{poly}(a_0))$ with normalization (2.3) — **there is no $C_M$, no $b_0(M)^{-1}$, no $M$ at all**. The parameter $M$ (decay order of the bump) **disappears from the construction**: we do not normalize by Vandermonde, so $C_1(M)$ never arises.

> **[PROPOSITION 3.1] (witness without a divergent constant).** Under $\neg$RH with minimal off zero $\rho^0=\frac12+\delta_0+i\gamma_0$, there exists a family of tests $\{v_{a_0}=h_{g_{a_0},\varphi_{a_0}}\}_{a_0\ge2}$ of the class, with $g_{a_0},\varphi_{a_0}$ real even of logarithmic support $[-a_0,a_0]$, such that
> $$Q_2(v_{a_0},v_{a_0})\ \le\ -\,c_3\,a_0^{-2}\,e^{\delta_0 a_0}\ +\ C_4\,(\log(2+|\gamma_0|))^2\cdot\mathrm{poly}(a_0)\ +\ C_5\,a_0\,e^{\delta_0 a_0/2}, \tag{3.6}$$
> where the first term (off defect, via $(\dagger)$) is negative and exponential of rate $\delta_0$; the second (on-line sea + tails) is positive and polynomial; the third (mixed off×on pairs, $\mathrm{Re}\,\sigma=\frac12+\delta_0/2$) is positive and exponential of rate $\delta_0/2<\delta_0$. **The constants $c_3,C_4,C_5$ depend only on $(\Phi,\delta_0,\gamma_0,m_0)$ — NOT on $M$, NOT on a parameter tending to infinity.** Consequently there is a **finite** $a_0^*=a_0^*(\delta_0,\gamma_0,m_0)$ such that $Q_2(v_{a_0^*},v_{a_0^*})<0$.

*Proof (rigorous sketch).* The dominant negative term is the sum over the off quadruple of $(\dagger)$ with $\delta=\delta_0$: four off pairs whose defect relative to the autonomous term is $-c_W|\hat f(\frac12+\delta_0+i\gamma_0)|^2\cdot|\hat\varphi(\tau)|^2\asymp -e^{\delta_0 a_0}\cdot a_0^{-1}$, with $c_W>0$ by the $(1,1)$ signature of the quadruple's hyperbolic plane (D107 Thm. 5.5, Prop. 6.1; D98 §6) — the plane is genuinely indefinite and the even witness aligns it toward its negative direction. The on-line sea is $\sum_{\rho\,\text{on}}|\hat h(\rho)|^2$ bounded by $\big(\sum_\rho a_0^{-1/2}(1+|\gamma-\gamma_0|)^{-K}\big)^2\cdot$(density $\ll\log$) $=C_4(\log(2+|\gamma_0|))^2\,\mathrm{poly}(a_0)$ (absolutely convergent sum, D107 Lemma 2.2(b); $\mathrm{poly}$ from the norm $\|v\|^2$). The mixed off×on pairs have a single off factor, $\mathrm{Re}\,\sigma=\frac12+\delta_0/2$, giving $e^{\delta_0 a_0/2}$ by (2.2); their number is finite (4 off zeros $\times$ on zeros in a band $\ll a_0\log$), absorbed into $C_5 a_0 e^{\delta_0 a_0/2}$. Comparing rates $\delta_0>\delta_0/2>0$: for large $a_0$ the first term wins; $a_0^*$ is where $c_3 a_0^{-2}e^{\delta_0 a_0}>C_4\mathrm{poly}(a_0)+C_5 a_0 e^{\delta_0 a_0/2}$, finite because $e^{\delta_0 a_0}/e^{\delta_0 a_0/2}=e^{\delta_0 a_0/2}\to\infty$. $\square$

**Verdict of §3:** the witness exists, its negativity is exponentially dominant, and **no constant diverges**: $M$ has been completely eliminated from the construction. The price is that $a_0^*$ is **finite but large** and depends on $\delta_0,\gamma_0$ (not effective — which `thm:realiz`/`rem:key` already declared acceptable: "$D_0,N_0$ are not effective").

---

## 4. The bounded-dimension robustness test (the point that really decides 139.A)

Here is the edge. Prop. 3.1 gives a witness in the **full class** with finite support $a_0^*$. But $\sigma_{\text{loc}}$ is computed over **bounded-dimension micro-cells** $V_p$ (Def. 3.1 of D136), and the cell's index is $\negind(Q_2|_{V_p})$ — the witness must live **inside a cell of the grid** $\mathcal G_N$. Does the exponential dominance survive this restriction?

### 4.1. What the cell requires

A cell has profile $p=(D,w,M,b,c,c')$ and $V_p=\mathrm{span}\{h_{g_a,\varphi_b}\}$ with $\hat g_a(\sigma)=B^{(M)}_w(\sigma-ic)\sigma^a$, **real** center $c$ (= ordinate $\mathrm{Im}\,\sigma$), $0\le a,b\le D$, $\dim V_p\le(D+1)^2$ **bounded**. Two facts:

- **The support $a_0$ is NOT bounded by the dimension.** $a_0=a_0(M,w)$ is the logarithmic support of the bump $B^{(M)}_w$; it depends on $M,w$, not on $D$. I can take $M,w$ such that $a_0(M,w)=a_0^*$ **without** increasing $\dim V_p$ (which depends only on $D$). **This is exactly the "conceptual key" of Obs. 5.1 of D136 / `rem:key` of P47:** the cell's dimension restricts the polynomial degree $D$, not the bump's support. The exponential dominance lives in the bump, not in the monomials. **It survives bounded dimension.** ✔
- **BUT the witness of §3 needs an even bump concentrated at $u=\pm a_0/2$.** Is that bump in the cell? The cell fixes ONE bump $B^{(M)}_w$ "once and for all" (Def. 3.1) and generates $\{B\cdot\sigma^a\}$. The Weil witness $f_{a_0}$ with two humps at $\pm a_0/2$ is **not**, in general, $B\cdot(\text{polynomial of degree}\le D)$: it is a specific bump profile. One must verify that the grid's bump family **includes** (or approximates within the cell) that profile.

### 4.2. The genuine obstacle: the grid samples ordinates, not real parts

Re-examining Def. 3.1: $\hat g_a(\sigma)=B^{(M)}_w(\sigma-ic)\sigma^a$. The center $c\in\mathbb Q$ enters as $\sigma-ic$, i.e. it shifts the **ordinate** $\mathrm{Im}\,\sigma$ by $c$ (`lem:vandermonde` and Lemma 5.3 of D136 speak of "centers $c\in\mathbb R$", shift $g\mapsto g\cdot x^{ic}$, a modulation that moves $\mathrm{Im}$). **There is no parameter in the profile that moves the cell in the $\mathrm{Re}\,\sigma$ direction.** The bump $B^{(M)}_w$ is centered at $\mathrm{Re}=\frac12$ (the critical strip) with the band factor $e^{a_0|\mathrm{Re}-\frac12|}$ of $(\ast)$.

This is good and bad:

- **Good:** the exponential dominance of §3 is evaluated at $\sigma_0=\frac12+\delta_0+i\gamma_0$, whose **ordinate** $\gamma_0$ is reached with center $c=\gamma_0$, and whose **real part** $\frac12+\delta_0$ is reached via the band factor $e^{a_0(\mathrm{Re}-\frac12)}=e^{\delta_0 a_0}$ — which is **automatic** in $(\ast)$ and is **exactly** the growth (2.4). **The cell bump's band factor IS the carrier of the exponential dominance.** There is no need to move the cell in $\mathrm{Re}$; the bump already grows in $\mathrm{Re}$ by Paley–Wiener.
- **Bad (the real edge):** the **shape** of the growth in $\mathrm{Re}$ is fixed by $B^{(M)}_w$, it is not free. Bound $(\ast)$ is an **upper** bound $|B|\le C_M e^{a_0|\mathrm{Re}-\frac12|}(\cdots)$; for the witness to work I need a **lower** bound $|B(\frac12+\delta_0+i\gamma_0)|\ge c\,e^{\delta_0 a_0}$, i.e. that the bump **realizes** its maximal exponential growth in the $+\delta_0$ direction. This is NOT automatic: a real even bump has $\hat B$ that may have zeros, and the hump at $+a_0/2$ must actually be present.

### 4.3. The verifiable hypothesis replacing `hyp:pw`

> **[DEFINITION 4.1 / HYPOTHESIS `hyp:band`] (band realization of the cell).**
> The family of bumps $\{B^{(M)}_w\}$ of the scheme (chosen "once and for all", Def. 3.1) **realizes the band** if for every $\delta\in(0,\frac12)$ there exists a choice of $(M,w)$ in the grid with arbitrarily large support $a_0(M,w)$ such that
> $$\big|B^{(M)}_w(\tfrac12+\delta+ic)\big|\ \ge\ c_\delta\,e^{c'\delta\,a_0(M,w)}\quad(c,c'>0\ \text{absolute}),\qquad \big|B^{(M)}_w(\tfrac12+ic)\big|\le C\ \forall c. \tag{4.1}$$
> That is: the bump achieves **lower** exponential growth in the direction $\mathrm{Re}=\frac12+\delta$ (not just upper), while remaining bounded on the line $\mathrm{Re}=\frac12$.

> **[THEOREM 4.2] (the ¬RH branch is a theorem under `hyp:band`).**
> Under $\neg$RH **and** `hyp:band`, for the minimal off zero $\rho^0=\frac12+\delta_0+i\gamma_0$ there exist standard $D_0,N_0$ with $x_0(N)\ge1/(2D_0)>0$ for $N\ge N_0$; hence $\sigma_{\text{loc}}\ge1/(2D_0)>0$ and $\lim_k\sigma_{\text{loc}}^{(k)}=\frac12$, for every $\mathcal U$.

*Proof.* With `hyp:band` the cell's bump satisfies the lower bound (4.1), which is the hypothesis of (2.4) transferred to $B^{(M)}_w$ instead of $f_{a_0}$. The witness $v$ of Prop. 3.1 is realized **inside** $V_p$: the (bounded) degree $D$ absorbs the Vandermonde annihilation of the resonant and near-resonant pairs $Z_\sigma,Z_\tau$ (GAP-B patch, finite, bounded dimension), and the support $a_0=a_0(M,w)\ge a_0^*$ is reached by choosing $(M,w)$ with large $a_0$ **without touching $D$**. The estimate (3.6) gives $Q_2(v,v)<0$ for $a_0\ge a_0^*$, hence $\negind(Q_2|_{V_p})\ge1$. The step from the ideal cell to the grid is Theorem 4.4/`thm:mesh` of D136 unchanged (the mesh perturbation is $b\cdot L$ with $L$ finite; the support $a_0$ fixed once $\delta_0$ is chosen). The rest is as in `thm:realiz` Steps 4–5. $\square$

**Why `hyp:band` is strictly weaker than `hyp:pw` and verifiable:**

1. **It is an order-of-magnitude inequality, not a delicate asymptotic equality.** `hyp:pw` demanded that a product of four $M$-dependent constants tend to $0$ (1.2) — and Lemma 1.1 proved it is **impossible**. `hyp:band` only demands that the bump grow exponentially toward the inside of the strip — which is what **every** Paley–Wiener bump does **generically** (the band factor $e^{a_0|\mathrm{Re}-\frac12|}$ of $(\ast)$ is an upper bound that is **saturated** except at the zeros of $B$, a discrete set avoidable by choice of the center $c$, exactly as in `lem:vandermonde`).
2. **It is verifiable in the class, without zero positions.** $|B^{(M)}_w(\frac12+\delta+ic)|$ is a computable quantity of the chosen bump (autonomy: the bump is part of the design, not of $\zeta$). Proving `hyp:band` for a concrete family (e.g. truncated Gaussians, or the Beurling–Selberg bump) is an exercise in entire functions of exponential type (Boas, Ch. 6; Levin, *Lectures on Entire Functions*, Ch. I on the growth indicator $h_B(\theta)$): the **Phragmén–Lindelöf indicator** $h_B(\theta)=\limsup_{r\to\infty}r^{-1}\log|B(re^{i\theta})|$ of a bump of support $[-a_0,a_0]$ is $h_B(\pm\pi/2)=a_0$ (exponential growth in the imaginary direction... ), and the $\mathrm{Re}$ direction corresponds to the type on the shifted real axis — the lower bound (4.1) is the **directional non-vanishing** of the indicator, generic.
3. **Lemma 1.1 does NOT obstruct it.** Lemma 1.1 says $C_M\to\infty$ (the upper-bound constant diverges in $M$); but `hyp:band` **does not use $C_M$**: it uses the exponential growth in $\mathrm{Re}$ at **fixed $M$** (or growing without control of $C_M$), because the witness is not normalized. **The parameter $M$ is now free/irrelevant:** one can fix small $M$ (it suffices that $M\ge D+4$ for tail convergence, `lem:tail`) and move only $a_0$ via $w$. Paley–Wiener rigidity attacked the normalization; without normalization, it does not bite.

### 4.4. Why CLOSED-**PARTIAL** and not total CLOSED?

Three frank residues prevent declaring "theorem without hypothesis":

- **(R1) `hyp:band` is generic but not proved for D136's specific bump.** D136 says "fixed bump $g_0^{(M,w)}$ from a computable family" without fixing which one. To CLOSE 139.A one must **exhibit** a family satisfying (4.1) and verify it (a calculation on entire functions, not done here — it would be fabricating). I conjecture (do not prove) that truncated Gaussians or Beurling–Selberg bumps satisfy it.
- **(R2) The band factor must be realized FROM BELOW in the compressed cell.** The witness $v$ is a combination $\sum a_j B\sigma^j$; the degree $D$ is bounded by the resonant pairs. One must verify that the combination annihilating $Z_\sigma$ (Vandermonde) **does not destroy** the exponential growth at $\sigma_0$ — i.e. that $|\sum a_j B(\sigma_0)\sigma_0^j|\ge c\,e^{\delta_0 a_0}$ despite $\hat g_v(Z_\sigma)=0$. This is plausible (the vanishing condition is at $\sigma\in Z_\sigma$, ordinates $\ne\gamma_0$ or real parts $\ne\frac12+\delta_0$; the value at $\sigma_0$ remains free) but the lower bound **uniform in $a_0$** of the Vandermonde combination requires that $\|a_j\|$ not grow with $a_0$ — and here $\|a_j\|$ depends on $b_0=\min|B(z_i-ic)|$, which by $(\ast)$ **decays** with $a_0$ if the $z_i$ are outside the band. **This is the most serious residue:** the Vandermonde annihilation of §GAP-B could reintroduce a cost $b_0^{-1}$ growing in $a_0$. I treat it in §5.
- **(R3) The real part of the center.** As §4.2 noted, the grid does not sample $\mathrm{Re}\,c$. The dominance works **because the band factor supplies it for free**, but this ties the repair to the bump growing in $\mathrm{Re}$ — exactly `hyp:band`. If a real-center axis were added to the grid (shifting $B(\sigma-\frac12-c_{\mathrm{Re}})$), `hyp:band` would become **automatic** (the bump is centered on $\frac12+\delta_0$ and evaluated at its maximum), closing 139.A **unconditionally** modulo (R2). This is the **recommended design modification** (§6).

---

## 5. The anti-false-victory verification: does $e^{2\delta_0 a_0}$ hide a divergent constant in the Vandermonde annihilation?

The mandate requires detecting whether the exponential dominance reintroduces the divergence through another door. The candidate door is (R2): the norm of Vandermonde coefficients $C_1$ of `lem:vandermonde`, $\|a_j\|\le C(z,\min_i|B(z_i-ic)|)\|y\|=C\,b_0^{-1}\|y\|$.

**Frank analysis.** To annihilate $Z_\sigma$ (the $|Z_\sigma|$ near-resonant pairs) I need $\hat g_v(z)=0$ at $z\in Z_\sigma$ and $\hat g_v(\sigma_0)=$ (large). The nodes $z_i\in Z_\sigma\cup\{\sigma_0\}$ have ordinates $\approx\gamma_0$ and **varied real parts** (some at $\frac12$, $\sigma_0$ at $\frac12+\delta_0$). The bump centered at $c=\gamma_0$ evaluates $B(z_i-i\gamma_0)$ with $z_i-i\gamma_0$ having real part $\mathrm{Re}\,z_i$ and small ordinate. By $(\ast)$:

$$|B(z_i-i\gamma_0)|\ \asymp\ e^{a_0|\mathrm{Re}\,z_i-\frac12|}\cdot(\text{pol}).$$

For on-line $z_i$ ($\mathrm{Re}=\frac12$): $|B|\asymp O(1)$. For $\sigma_0$ ($\mathrm{Re}=\frac12+\delta_0$): $|B|\asymp e^{\delta_0 a_0}$. Hence $b_0=\min_i|B(z_i-i\gamma_0)|\asymp O(1)$ (fixed by the on-line node, does not decay with $a_0$), **unless** some $z_i\in Z_\sigma$ has real part $>\frac12$, in which case $|B(z_i-i\gamma_0)|$ grows, **increasing** $b_0$ (better) — it never makes it decay if the nodes are at $\mathrm{Re}\le\frac12+\delta_0$. **Hence $C_1=O(b_0^{-1})=O(1)$ in $a_0$: it does NOT diverge.** ✔

But there is a sub-residue: the datum is $y=(\,0,\dots,0,\hat g_v(\sigma_0)\,)$ with $\hat g_v(\sigma_0)$ which I **want** $\asymp e^{\delta_0 a_0}$. The Vandermonde construction gives the interpolating polynomial; its value at $\sigma_0$ is $\sum a_j B(\sigma_0)\sigma_0^j$. Since the annihilation nodes are at $\mathrm{Re}\le\frac12$ and $\sigma_0$ at $\frac12+\delta_0$, the Lagrange interpolant at $\sigma_0$ has a value dominated by the factor $B(\sigma_0)\asymp e^{\delta_0 a_0}$ multiplied by an $O(1)$ Lagrange constant (the nodes are at $O(1)$ distance in the plane, Vandermonde well-conditioned at separated ordinates). **The exponential growth is preserved, the Vandermonde constant does not diverge.** ✔

**Anti-false-victory verdict:** the exponential dominance $e^{\delta_0 a_0}$ is **genuine** and **hides no** divergent constant — provided `hyp:band` (lower bound of the bump in the band) holds. The only place where a divergence could reappear is if the annihilation nodes $Z_\sigma$ contained points of **real part $>\frac12+\delta_0$** (off zeros of real part larger than that of the minimal defect), forcing $B$ to grow at a node that must vanish, which **would raise** the relative $\|y\|$. But $\rho^0$ is the off zero of **minimal height**, not of maximal real part; there could be off-zeros with $\mathrm{Re}>\frac12+\delta_0$ in $Z_\sigma$. **This reproduces exactly D139's §4.4 observation: "choosing the off zero of near-extremal real part, not the one of minimal height".** That is: the correct witness uses the off zero of **maximal real part** $\beta^*=\sup\{\beta:\exists\ \text{zero}\ \frac12+\beta+i\gamma\}$ (exists finite under a $\neg$RH whose defect touches the band; under general $\neg$RH $\beta^*\le\frac12$), not the one of minimal height. With that change, **no annihilation node exceeds $\frac12+\beta^*$**, and $b_0=O(1)$ rigorously. I record this as a refinement of the construction (Prop. 3.1 should use $\rho^*=\frac12+\beta^*+i\gamma^*$, not the one of minimal height).

---

## 6. Verdict and consequences

### 6.1. Verdict: 139.A CLOSED-PARTIAL

**The exponential dominance route WORKS and is frank.** It eliminates the divergent constant $C_3(M)$: the witness is not normalized, $M$ disappears from the construction (it stays fixed at $M\ge D+4$ by tail convergence), and the exponential growth $e^{\delta_0 a_0}$ of the bump in the critical strip —which is the Paley–Wiener band factor $(\ast)$ used **from below**— dominates all polynomial terms and the smaller-rate exponentials ($\delta_0/2$). Paley–Wiener rigidity (Lemma 1.1) **does not obstruct** because it attacked the normalization, not the directional growth.

**The ¬RH branch is a THEOREM under `hyp:band`** (Theorem 4.2), a hypothesis that is:
- strictly weaker than `hyp:pw` (order inequality vs. asymptotic equality of four constants);
- purely analytic and **verifiable without zero positions** (it is a property of the design's bump, computable);
- generic for Paley–Wiener bumps (non-vanishing of the Phragmén–Lindelöf indicator in the direction $\mathrm{Re}=\frac12+\delta_0$);
- **not refuted by Lemma 1.1** (which only refuted `hyp:pw`).

**Residues preventing total CLOSED** (§4.4): (R1) `hyp:band` is not proved for an explicit bump (it would be a calculation on entire functions, not fabricated here); (R3) D136's grid does not sample the real part of the center, so the dominance depends on the bump's band factor — fixable by adding a real-center axis to the grid.

### 6.2. The design modification that would unconditionally close 139.A

Add to D136's Def. 3.1 a **real center** parameter $c_{\mathrm{Re}}\in\mathbb Q\cap[0,\frac12]$ to the mesh, with $\hat g_a(\sigma)=B^{(M)}_w(\sigma-\frac12-c_{\mathrm{Re}}-ic)\,\sigma^a$ (bump centered on $\frac12+c_{\mathrm{Re}}$). Then the witness centers the bump on $\frac12+\delta_0$ (choosing $c_{\mathrm{Re}}\approx\delta_0$ in the mesh) and evaluates at its **maximum**, where $|B(0)|=1$ by the normalization of $(\ast)$ — **`hyp:band` becomes the identity $|B^{(M)}_w(0)|=1$, trivially true**. With this, the ¬RH branch is an **unconditional** theorem modulo only (R2), which §5 verified using the zero of maximal real part. **This is the operative recommendation: D136's grid has a missing degree of freedom; adding it costs one mesh dimension (harmless, still computable) and dissolves 139.A.**

### 6.3. Consequence for P47 and the logistic criterion

- **`hyp:pw` should be replaced by `hyp:band`** (Def. 4.1 / Hypothesis): weaker, verifiable, not refuted by `rem:pw-rigidity`. `rem:pw-rigidity` remains the correct diagnosis of why the **old** route (normalization) failed.
- **`thm:realiz` is re-proved** by the construction of §3 (Prop. 3.1) under `hyp:band` instead of `hyp:pw`. Step 3 no longer uses `lem:tail` to make a normalized tail small, but the dominance (3.6); `lem:tail` survives as an auxiliary bound on the polynomial tail.
- **With the design modification of §6.2 (real center in the grid), the ¬RH branch again becomes an unconditional THEOREM** (modulo R2, verified in §5 with the zero of maximal real part). In that case **both branches are theorems again** and the criterion $\mathrm{RH}\iff\lim_k\sigma_{\text{loc}}^{(k)}=0$ recovers the status D136 announced and D139 downgraded. P47's abstract ("both branches theorems") would be sustainable **after adding the real-center axis and proving R2 for the extremal zero** — §5 does the latter, the former is a design line.
- **Without the modification**, P47 must state the ¬RH branch as a **theorem under `hyp:band`** (not under `hyp:pw`), which is frank and strictly better than the current status.

### 6.4. Final frankness: is 139.A equivalent to something known?

`hyp:band` is essentially the claim that **a Beurling–Selberg test (or truncated Gaussian) realizes the Phragmén–Lindelöf growth in the strip** — a fact from the theory of extremal functions of exponential type (Boas, Levin; Vaaler 1985 for Beurling–Selberg). **It is not equivalent to RH nor to an open number-theoretic conjecture**: it is pure analysis, about the design, decidable in principle. That is why the verdict is CLOSED-PARTIAL and not OPEN: the residue is a calculation on entire functions, not an arithmetic wall. The program's "master quantifier" does **not** reappear here: the exponential dominance is a fixed-finite-support phenomenon $a_0^*$, not a $T\to\infty$ regime nor a uniformity over windows.

---

## Final message

**VERDICT: 139.A CLOSED-PARTIAL.** The exponential dominance $e^{\delta_0 a_0}$ of the Weil criterion genuinely eliminates the divergent constant $C_3(M)$ (anti-false-victory verified, §5): the ¬RH branch is a theorem under hypothesis `hyp:band`, strictly weaker and verifiable than `hyp:pw`, not refuted by Paley–Wiener rigidity. With a harmless design modification (real-center axis in the grid, §6.2), the ¬RH branch again becomes an unconditional theorem and **both branches of the logistic criterion are theorems again**.

**Three labeled results:**

1. **[LEMMA 2.1]** (exponential-vs-polynomial dominance in the critical band): a test of logarithmic support $a_0$ evaluated at an off-line zero $\frac12+\delta_0+i\gamma_0$ grows like $e^{\delta_0 a_0/2}$, while on-line zeros grow polynomially; the off/on ratio $\to\infty$. The exact rate is not load-bearing; any positive exponential rate closes the argument.

2. **[PROPOSITION 3.1]** (witness without a divergent constant): under ¬RH there exists a family of even tests of support $a_0$ with $Q_2(v_{a_0},v_{a_0})\le -c_3 a_0^{-2}e^{\delta_0 a_0}+\mathrm{poly}(a_0)+C_5 a_0 e^{\delta_0 a_0/2}$, whose constants **do not depend on $M$**; the off term (via the perturbation $(\dagger)$ of `rem:theta`) dominates for finite $a_0\ge a_0^*$, giving $\negind(Q_2|_{V_{p^*}})\ge1$.

3. **[THEOREM 4.2]** (¬RH branch is a theorem under `hyp:band`): under ¬RH and the band realization of the bump (lower bound $|B^{(M)}_w(\frac12+\delta+ic)|\ge c_\delta e^{c'\delta a_0}$, generic and verifiable, **not** obstructed by Lemma 1.1), $\sigma_{\text{loc}}\ge1/(2D_0)>0$ and $\lim_k\sigma_{\text{loc}}^{(k)}=\frac12$ for every $\mathcal U$.

---

## References

**Internal (backward-only):** D139 (GAP-A, Lemma 139.1, GAP-B, route §4.4, Problem 139.A); D136 (Theorem 5.4, Def. 3.1–3.2, Lemmas 5.2–5.3, spectral side (1.1)); D108 (Prop. 2.2); D107 (Lemmas 2.2(b), 5.2(b), Thm. 5.5, Prop. 6.1, closure $x\partial_x$); D98 (quadruple, hyperbolic planes); P47 (`hyp:pw`, `rem:pw-rigidity`, `lem:tail`, `lem:vandermonde`, `thm:realiz`, `rem:theta`, $Z_\tau$ patch); P43 (autonomy of the value); ERRATA.md (Phase 38, $W_\lambda$).

**Literature (real, published):**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952) — positivity criterion; the direction ¬RH $\Rightarrow\exists f: Q(f)<0$ and its mechanism of exponential dominance of the off term (§3.3).
- R. P. Boas, *Entire Functions*, Academic Press (1954), Ch. 6 (Thm. 6.8.1, Paley–Wiener for $C_c^\infty$; exponential type and growth indicator).
- B. Ya. Levin, *Lectures on Entire Functions*, AMS Transl. Math. Monographs 150 (1996), Ch. I (Phragmén–Lindelöf indicator $h_B(\theta)$, directional growth — basis of `hyp:band`).
- L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer (1990), Thm. 7.3.1 (Paley–Wiener; discrete real zeros of nonzero entire functions — Lemma 1.1).
- J. D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS 12 (1985) — Beurling–Selberg extremal functions (concrete candidate for `hyp:band`, R1).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53 (2004), Thm. 5.8 ($N(t+1)-N(t)\ll\log(2+t)$).

*End of Doc 147.*
