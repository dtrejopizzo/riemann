# R163_502 — The density hypothesis (Q) and the Σδ² bound of R163_401 §4.2

*Pure mathematics; no numerics. Only this file was written. No label of record moves. Row D stays OPEN.*

**Final statuses (stated first).**

| item | status |
|---|---|
| U. Inventory of the uses of (Q) in R163_401 | PROVED (by inspection): no load-bearing step uses (Q) |
| Q0. Quadrature on the D-closure of the node span (unconditional replacement for 2.4(iii) and §4.5) | **PROVED** |
| Q1. Exact description of the L²-annihilator of the node span | **PROVED** |
| Q2. (Q) in L² under the lower bound (LB) on the witness | **PROVED** |
| (Q) in full: D-norm, no hypothesis on the witness | **OPEN** (RH-neutral; reduced to Q1) |
| Δ. Σ_{γ≤R} δ² ≪ R/log R, by Selberg's density theorem | **PROVED-CITED** (classical). This is stronger than R163_115 |
| Δ′. Σ_{γ≤R} δ ≪ R | PROVED-CITED (same proof) |

After the replacements in §4 below, **R163_401 no longer depends on an open hypothesis, apart from its own declared ARGUED
step (★_cell)/(I1)**. That step is unchanged, and R163_490 shows it is RH-equivalent at the witness (E1).

Notation is that of R163_401 §1 and R160_X_C1 §5. We write $T=T_c$. $E:=\widehat F$ is the transform of a real
witness. It lies in $PW_T$, has full type $T$, only real zeros $X$, and indicator $T|\sin\theta|$ (FC(i)). The node
tests are $\widehat H_x=E/(z-x)$, and
$$
N:=\mathbb CE+\mathrm{span}\{\widehat H_x:x\in X\}.
$$
For Q1 and Q2 the nodes are assumed simple. At a node of multiplicity $k$, add the tests $E/(z-x)^j$ for $j\le k$; the
proofs go through unchanged.

---

## 1. Where R163_401 uses (Q). PROVED by inspection

A grep of R163_401 for "(Q)", "OS-3", "quadrature" and "dense" finds four places.

1. **§2.4(iii), second half:** "Under (Q) this holds on all of $\mathcal D_{T_c}$ … positive quadrature, exact on
   products of type ≤ 2T_c."
2. **§4.5:** the whole subsection (band-$2T$ quadrature, $\widehat{\nu_X}$ = Weil distribution on $(-2T,2T)$, Kreĭn
   reading).
3. **§7 ledger:** the rows for 2.4 and 4.5.
4. **Remark 4.8:** it lists 4.5 among the places where integrality enters. This is descriptive only.

The other steps do not use (Q):
- **§4.4** uses $W(H_{x_0})=\sum_\rho G(t_\rho)^2/(t_\rho-x_0)^2$. This is (1.1) applied to the single test $H_{x_0}$,
  and it holds by Theorem G(a) and Lemma 3.0.
- **Prop. 4.0, §4.1–4.3, §4.6–4.9 and §5** use only (1.1), Lemmas 3.0–3.4, the cell identity and Theorem G(a)–(d) on
  the span.
- R163_490 §3 confirms this ("§4.5 … is not used in the sign step").

**Conclusion.** The weakest statement that serves every use is Q0 below. It is unconditional.

## 2. Q0: quadrature on the closure of the span. PROVED

Let $\overline N^{\mathcal D}$ be the closure of $\mathrm{span}\{H_x\}$ in the form-domain norm
$\|G\|_{\mathcal D}^2=\int\log(2+|\tau|)|\widehat G|^2$. Put $w_x:=W(H_x)/|E'(x)|^2$. Writing $|E'|^2$ settles the
odd-case sign (fix 4 of R163_490).

**Theorem Q0.** For $G,H\in\overline N^{\mathcal D}$:
$$
W_T(G,H)=\sum_{x\in X}w_x\,\widehat G(x)\overline{\widehat H(x)}=\sum_\rho(\widehat G\widehat H^\#)(t_\rho),
$$
and both sums converge absolutely.

*Proof.*
- $W$ is a bounded hermitian form on $\mathcal D$, since $|\sigma_T|\ll\log(2+|\tau|)$ and the point evaluations at
  $\pm i/2$ are $\mathcal D$-bounded by Lemma 3.2.
- On the span, $W(G)=\sum_xw_x|\widehat G(x)|^2$ (Theorem G(d)).
- Let $G_n\to G$ in $\mathcal D$ with $G_n$ in the span. Then $(G_n)$ is Cauchy for the seminorm $W^{1/2}$. So the
  vectors $(\sqrt{w_x}\widehat G_n(x))_x$ are Cauchy in $\ell^2(X)$, and converge to some $a\in\ell^2$.
- Point evaluation on $\mathbb R$ is $\mathcal D$-continuous, since $PW_T$ has a reproducing kernel. So
  $\widehat G_n(x)\to\widehat G(x)$ for every $x$, and $a_x=\sqrt{w_x}\widehat G(x)$.
- Hence $W(G)=\lim W(G_n)=\|a\|^2=\sum w_x|\widehat G(x)|^2$. Polarise.
- The zero side is (1.1) (Paper 46 `lem:roughEF` with Lemma 3.0), polarised. ∎

**Replacement texts.**
- **2.4(iii):** "on $\overline N^{\mathcal D}$, $W=\sum w_x|\widehat G(x)|^2$ (R163_502 Q0, PROVED). Whether
  $\overline N^{\mathcal D}\oplus\mathbb CF=\mathcal D$ is OS-3; it is not used."
- **§4.5:** "for $\Psi=\widehat G\widehat H^\#$ with $G,H\in\overline N^{\mathcal D}$,
  $\sum_\rho\Psi(t_\rho)=\sum_xw_x\Psi(x)$ (PROVED)." The Kreĭn/band reading ($\widehat{\nu_X}$ equals the Weil
  distribution on all of $(-2T,2T)$) needs the products to span a dense set of the band, so it stays conditional on
  (Q). It is marked as a remark, not a step.

## 3. Toward (Q) itself

### 3.1 Q1: the annihilator. PROVED

Let $V:=\{f\in PW_T:f|_X=0\}\ni E$ and $\mathcal M:=V/E=\{A\ \text{entire}:EA\in PW_T\}\ni1$. Every
$A\in\mathcal M$ is of zero exponential type: $E$ has completely regular growth with indicator $T|\sin\theta|$, the
quotient of Cartwright functions is Cartwright (Kreĭn), and $h_A=h_{EA}-h_E\le0$.

**Theorem Q1.** $g\in PW_T$ is $L^2$-orthogonal to $N$ if and only if
$$
g^\#=e^{iTz}A_0+e^{-iTz}B_0\quad\text{with }A_0,B_0\in\mathcal M,
$$
where $g^\#\in L^2(\mathbb R)$ and $\eta(0)=0$. Here
$\eta:=(Eg^\#)^\vee\in C_c([-2T,2T])$.

*Proof.*
- **The function $R$.** Put $H:=Eg^\#$; on $\mathbb R$, $H=E\bar g\in L^1$. Then $H(\tau)=\int\eta(u)e^{i\tau u}du$,
  with $\eta=F*\tilde g^\vee$ continuous. Put $H_\pm:=\int\eta\mathbf 1_{\pm u>0}e^{izu}du$. Since
  $\mathrm{p.v.}\!\int e^{i\tau u}(\tau-x)^{-1}d\tau=i\pi\,\mathrm{sgn}(u)e^{ixu}$,
  $$
  \langle\widehat H_x,g\rangle=\mathrm{p.v.}\!\int\frac{H(\tau)}{\tau-x}d\tau=i\pi(H_+-H_-)(x)\qquad(x\in X).
  $$
  The p.v. is harmless because $H(x)=0$.
- **The condition at the nodes.** Also $\langle E,g\rangle=\int H=2\pi\eta(0)$. So $g\perp N$ if and only if
  $\eta(0)=0$ and $H_+=H_-$ on $X$. Since $H_++H_-=H$ vanishes on $X$, this means $H_+|_X=H_-|_X=0$.
- **The forward direction.** $e^{-iTz}H_+$ has spectrum in $[-T,T]$ and $L^2$ density, so it lies in $PW_T$, and it
  vanishes on $X$. Hence $e^{-iTz}H_+=EA_0$ with $A_0\in\mathcal M$. Likewise $e^{iTz}H_-=EB_0$. So
  $g^\#=H/E=e^{iTz}A_0+e^{-iTz}B_0$.
- **The converse.** Given such $A_0,B_0$, the function $H=e^{iTz}EA_0+e^{-iTz}EB_0$ has $H_+=e^{iTz}EA_0$, because
  the spectra lie in $[0,2T]$ and $[-2T,0]$. Both $H_\pm$ vanish on $X$. ∎

**Reading.** (Q) in $L^2$ fails exactly when two zero-type multipliers of $E$, modulated by $e^{\pm iTz}$, cancel each
other to $L^2$ precision on $\mathbb R$. The model $E=\sin Tz/z$ has $\mathcal M=\mathbb C$. This recovers OS-3's model
case.

### 3.2 Q2: (Q) in $L^2$ under a lower bound. PROVED

**(LB)** There are $K,c>0$ with $|E(x\pm i)|\ge c(1+|x|)^{-K}$ for $x\in\mathbb R$. Because $E$ is real-rooted and
Cartwright, $\log|E(x+iy)|=T|y|+(P_{|y|}*\log|E|)(x)$ holds with equality (there are no zeros off $\mathbb R$). So
(LB) says that the Poisson average of $\log|E|$ at scale 1 is $\ge-K\log(2+|x|)-C$.

**Theorem Q2.** Under (LB), $N$ is dense in $PW_T$ for the $L^2$ norm.

*Proof.*
- **$\mathcal M$ is polynomial.** Let $A\in\mathcal M$. Then $|EA(x\pm i)|\le e^{T}\|EA\|_{PW}\cdot C$, so
  $|A(x\pm i)|\le C'(1+|x|)^K$.
  - $A$ has zero type, so on the strip $|y|\le1$ it is bounded by the same bound (Phragmén–Lindelöf in the strip).
  - On the half-planes $|y|\ge1$, $A(z)/(z\pm 2i)^K$ is bounded on the boundary and of zero type, hence bounded
    (Phragmén–Lindelöf).
  - So $A$ is a polynomial of degree $\le K$.
- **The annihilator is zero.** By Q1, an annihilator has $g^\#=e^{iTx}A_0+e^{-iTx}B_0$ with polynomials $A_0,B_0$.
  - Write $|g^\#|^2=|A_0|^2+|B_0|^2+2\mathrm{Re}(e^{2iTx}A_0\bar B_0)$.
  - Integrate over consecutive periods $\pi/T$. The cross term contributes $O(\int|(A_0\bar B_0)'|)$ per period,
    which is of lower degree.
  - So $\int|g^\#|^2=\infty$ unless $A_0=B_0=0$. Hence $g=0$. ∎

### 3.3 What remains open, exactly

- **(Q-a)** (LB) for the witness. Nothing in R160_X_C1 FC/G bounds $E$ from below. A witness whose transform is
  super-polynomially small on Poisson average would have $\mathcal M$ infinite-dimensional, and then Q1 is the exact
  test.
- **(Q-b)** Passage from $L^2$ to the $\mathcal D$ norm. The Q1 argument needs $g^\#$ entire. A $\mathcal D$-annihilator
  gives $\log(2+|\tau|)\bar g$, which is not entire. An entire weight $\Omega$ of small type with
  $|\Omega|^2\asymp\log(2+|x|)$ off a thin set would transfer Q1 and Q2. That transfer is not done here.
- Both points are RH-neutral: they concern a real-rooted $PW_T$ function, not $\zeta$.
- By §1, neither is needed by R163_401. (Q) is used load-bearingly only in R162_2301 Thm DC/Q, and only to extend
  from the span to all of $\mathcal D$. Thm Q's conclusion (no sign conflict) already holds on $\overline N^{\mathcal D}$
  by Q0.

## 4. The Σδ² bound. PROVED-CITED (classical)

For off-line zeros $\rho=\tfrac12+\delta+i\gamma$ ($\delta>0$, $\gamma>0$, one per quartet, with multiplicity), put
$N(\sigma,R)=\#\{\beta>\sigma,\ 0<\gamma\le R\}$.

**Input (Selberg 1946; Titchmarsh, 2nd ed., Thm 9.19(C)).** $N(\sigma,R)\ll R^{1-\frac14(\sigma-\frac12)}\log R$,
uniformly for $\tfrac12\le\sigma\le1$ and $R\ge2$.

**Theorem Δ.** $\displaystyle\sum_{0<\gamma\le R,\ \delta>0}\delta^2\ll\frac{R}{\log R}$ and
$\displaystyle\sum_{0<\gamma\le R,\ \delta>0}\delta\ll R$.

*Proof.* By the layer-cake formula, $\delta^2=\int_0^\delta2u\,du$. So
$$
\sum\delta^2=\int_0^{1/2}2u\,N(\tfrac12+u,R)\,du\ll R\log R\int_0^\infty2u\,e^{-\frac u4\log R}du=\frac{32\,R\log R}{\log^2R}.
$$
Similarly, $\sum\delta=\int_0^{1/2}N(\tfrac12+u,R)du\ll R\log R\cdot\frac4{\log R}$. Uniformity in $\sigma$ is what
allows the integration. ∎

**Remarks.**
- Theorem Δ improves R163_115's $R(\log\log R)^2/\log R$, which used Chourasiya–Simonič.
- It also improves the "standard" $\sum(\beta-\frac12)\ll R\log\log R$ quoted in R163_490 fix 5. That bound is
  Littlewood's lemma with Jensen applied to $\int\log|\zeta(\frac12+it)|dt\le\frac R2\log(\frac1R\int|\zeta|^2)$. The
  Jensen/Littlewood route alone gives only $\sum\delta^2\le\frac12\sum\delta\ll R\log\log R$, which is not $o(R)$.
  Selberg's mollified density theorem is needed for $o(R)$.
- The weaker $\sum\delta^2=o(R)$ also follows from Ingham/Bohr–Landau $N(\sigma,R)=o(R)$ for fixed $\sigma>\frac12$,
  with dominated convergence in $u$. This is also classical.

**Replacement text for R163_401 §4.2, second bullet.** "$\sum_{\gamma\le R}\delta^2\ll R/\log R$ and
$\sum_{\gamma\le R}\delta\ll R$ (Selberg's density theorem, Titchmarsh 9.19(C); R163_502 Thm Δ)."
- The bound is not load-bearing. It feeds only the heuristic (I0), which R163_490 §3 refutes as a mechanism.
- It does not make $n^{\rm off}_j$ small in any single cell (R163_490 fix 6), because it is an average.
- Also correct $13.1\to13.4$ in (I0), per R163_490.

## 5. Ledger

| item | label |
|---|---|
| §1 inventory: (Q) not load-bearing in R163_401 | PROVED |
| Q0 quadrature on $\overline N^{\mathcal D}$ | PROVED |
| Q1 annihilator = modulated pairs of zero-type multipliers | PROVED |
| Q2 (Q) in $L^2$ under (LB) | PROVED |
| (Q) in $\mathcal D$, unconditionally (OS-3) | OPEN, reduced to (Q-a)+(Q-b) |
| Thm Δ: $\sum\delta^2\ll R/\log R$, $\sum\delta\ll R$ | PROVED-CITED (Selberg; Titchmarsh 9.19(C)) |
| Row D | OPEN (gap = (★_cell)/(I1), RH-equivalent at the witness; R163_490) |
