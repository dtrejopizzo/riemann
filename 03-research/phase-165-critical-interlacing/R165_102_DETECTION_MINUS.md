# R165_102 — (Det−): can the lowest off-line quartet make contact below the Landau window?

* Task A2 of phase 165 (R165_000 §1, §4). Pure mathematics; no numerics were run (the three numbers
in §2.4 are hand arithmetic on closed formulas). No file outside this one was edited. No label of record moves.*
*Inputs: R165_000 §1; R163_401 §1–§4 (eq. (1.1), Lemma 3.1, Lemma 3.2, §4.8, Rem 4.8a, Lemma 4.10, Cor 4.10a, §4.9); R163_402
Thm 4 and erratum D1; R163_701 (L1, L3, Thm A, Thm B, Rem B.1–B.2, O701.1–3); R163_702 (V), (N), Thm B ($K_H$).*
*Corpus check (rule ).* This memo makes three changes to existing work. (i) R163_701 Thm B is a *local* statement
($P_{\rm loc}$, Gevrey localiser of width $\asymp\log\gamma$, tail ARGUED). Here it is re-proved as a *global* statement about
$\lambda^{\rm W}_T$, with an un-modulated complex test and the far tail PROVED. (ii) The constants are explicit, which gives an explicit
threshold at the verified height. (iii) The result is read against (Det−). Neither R163_402 nor R163_401 says anything about (Det−) for ζ:
R163_402 §2 calls the "density-limited branch" HEURISTIC.

**Labels.** PROVED, PROVED-CITED (FROM MEMORY when flagged), ARGUED, OPEN.

---

## Outcome first

**Verdict.** (Det−) in the form asked, with $C'$ depending only on $\delta^*$ and not on $\gamma^*$, is **false in the large-δ regime**. It
is **δ\*-dependent**, with three regimes in $y:=\delta^*\Lambda^*$, where $\Lambda^*:=\log(\gamma^*/2\pi)=2T_L(\gamma^*)$:

| regime | lattice model (Lemma 4.10) | ζ (this memo) |
|---|---|---|
| $y\le y_0(2\delta^*C')$ (≈ $y_0=2.1773$ when $\delta^*C'\ll1$) | (Det−)[$C'$] **true** (Prop 3) | OPEN: needs a sub-Landau lower frame (O701.2) and control of all higher quartets (Cor 2(c)) |
| $y_0<y<\log\Lambda^*+\log\log\Lambda^*+O(1)$ | (Det−) **false** (contact below $T_L$) | OPEN (the gap is the L3 loss; O701.3) |
| $y\ge\log\Lambda^*+\log\log\Lambda^*+K$, with dominance (Dom) | (Det−) false | **(Det−) FALSE, PROVED** (Thm 1): $T_c<T_{\rm det}<T_L(\gamma^*)-C'$ |

Answers to the questions of the task.
- **(a) Obstruction.** Sampling inequalities cannot beat $e^{2\delta^*T}$. Every lower or upper frame constant for $PW_T$ at the on-line
  ordinates is at most $2\pi M(1+2T)=O(\Lambda T)$ (L3). It is $\Lambda$ in the lattice. The quartet can extract $2S(T,\delta)\|g\|^2$ with
  $S\asymp e^{2\delta T}/\delta$. So the sampling obstruction holds exactly while $S(T,\delta^*)\lesssim$ frame constant, and it is lost once
  $2\delta^*T>\log(\delta^*\Lambda^*T)+O(1)$, well below $T_L$ when $y$ is large (Prop 4). The premise "node density $<$ zero density ⇒ the
  quartet cannot win" is wrong: sub-Landau contact does **not** make the nearby on-line zeros invisible. It **outweighs** them, by
  amplification and not by annihilation (§3).
- **Reconciliation with Lemma 4.10.** In the lattice model, replacing L3's constant $2\pi M(1+2T)$ by the exact Poisson constant $\Lambda$
  turns Thm 1's criterion into $S(T,\delta)>\Lambda/2$, which is Lemma 4.10 verbatim. The test of Thm 1 is the model extremal (odd, node at
  the cone vertex) smoothed by a Gevrey bump. Thm 1 is therefore the model mechanism transported to the real zero set. The only loss is the
  factor $\asymp\Lambda$, which costs $\log\Lambda$ in the threshold (Rem 1.3).
- **(b) The sub-Landau witness.** At a sub-Landau contact, the quartet's cell (length $\pi/T_c$) contains about $\Lambda^*/(2T_c)$ on-line
  ordinates. At $T_c\approx T_{\rm det}$ that is $\asymp y/\log(y\Lambda^*)$, which is greater than 1. $(\star_{\rm cell})$ fails in that cell
  (Cor 4.10a mechanism). The on-line mass $P_0$ is of the same order as $\Lambda T\|g\|^2$, not small. R163_701 Thm B is a one-cell
  construction, so its contrapositive applies to the lowest quartet alone: $P_{\rm loc}(\gamma^*,\tfrac12\Lambda^*-C')$ forces
  $\delta^*\le(\log\Lambda^*+\log\log\Lambda^*+O(1))/\Lambda^*$ when $\rho^*$ is dominant. The present Cor 2 shows that the global (Det−)
  forces the same bound.
- **What (Det−) really is.** (Det−)[$C'$] is a **zero-location statement**: it implies the strip bound $Z(C')$ (Cor 2) for the lowest zero, and
  a uniform bound for every dominant off-line zero at every height. No known region gives this: dlVP and VK are regions near $\beta=1$. So
  (Det−) cannot be proved without proving new zero-free information. It is false for $M_m$ with one quartet of large $\delta$, so the proof
  must use the arithmetic (§5). It is not RH-strength in the way the *uniform-in-γ* sub-Landau $P_{\rm loc}$ is (R163_701 Thm B), but it is a
  quasi-RH statement in a bounded range.
- **Consequence for phase 165.** The relation $T_c=T_L(\gamma^*)+O(1)$ (R165_000 §1) cannot hold in general. Contact is governed by
  $\min_\rho T_{\rm det}(\rho)$ over off-line zeros, not by the lowest one (Cor 2(c)). The critical interlacing (EC) of R165_000 §2 can be the
  geometry at $T_c$ only in the regime $y=O(1)$, i.e. off-line zeros within $O(1/\log\gamma)$ of the line.

## Status table

| # | statement | label |
|---|---|---|
| Thm 1 | global detection: for a (Dom)-dominant off-line zero $\rho_0$, $\lambda^{\rm W}_T<0$ at $T=T_{\rm det}(\rho_0)\le\tfrac12\Lambda_0$, with explicit $T_{\rm det}$ | PROVED (counting input PROVED-CITED, FROM MEMORY; Gevrey bump PROVED-CITED) |
| Rem 1.3 | lattice substitution gives exactly Lemma 4.10 | PROVED |
| Cor 2(a) | no $C'(\delta)$ uniform in $\gamma^*$: (Det−) fails for $\delta^*\Lambda^*\ge\log\Lambda^*+\log\log\Lambda^*+K(C')$ under (Dom) | PROVED |
| Cor 2(b) | (Det−)[$C'$] ⇒ $Z(C')$ for $\rho^*$ (if dominant): $\delta^*\Lambda^*<\log\Lambda^*+\log\log\Lambda^*+O(1+C')$ | PROVED |
| Cor 2(c) | (Det−)[$C'$] ⇒ $T_{\rm det}(\rho)\ge T_L(\gamma^*)-C'$ for **every** dominant off-line ρ (all heights); the lowest quartet is not the one that decides contact | PROVED |
| §2.4 | at $\gamma_0\approx H=3\cdot10^{12}$: Thm 1 detects sub-Landau iff $\delta_0\gtrsim0.37$ | PROVED (hand arithmetic on Thm 1) |
| Prop 3 | lattice model: (Det−)[$C'$] ⟺ $\sinh(y-s)\le2y-s$, $s=2\delta C'$; uniform in Λ only for $y=O(1)$ | PROVED (in the model) |
| Prop 4 | sampling trade-off: no frame inequality gives (Det−) once $2S(T,\delta^*)>B_T$ | PROVED |
| Prop 5 | conditional positive direction (ZFR at width $c/T$ + local frame at all heights ⇒ (Det−)) | PROVED-CITED (R163_701 Thm A + R163_601 Thm 1, record); hypotheses OPEN |
| §5 | $M_m$ falsifier: (Det−) false for $M_m$ with one quartet in regime 3 | PROVED (given $M_m$'s explicit formula, record) |
| removal of (Dom) | clusters of near-equal δ | OPEN (= O701.1) |
| middle regime $y_0<y<\log\Lambda+\log\log\Lambda$ for ζ | | OPEN (= O701.3) |
| (Det−) for ζ | | **OPEN**: false in regime 3 given (Dom), and implies the unknown $Z(C')$ |
| $(\star_{\rm cell})$, Row D | | **OPEN** |

---

## §0 Setting

Notation of R163_401 §1. For $F\in L^2(I_T)$ (complex), $\widehat F(z)=\int Fe^{izt}dt$, and by (1.1) (PROVED-CITED, Paper 46
`lem:roughEF` + R163_401 Lemma 3.0, complex case by polarisation)
$$
W_T(F)=\sum_\rho\widehat F(t_\rho)\,\overline{\widehat F(\bar t_\rho)},\qquad t_\rho=\gamma_\rho-i\delta_\rho . \tag{0.1}
$$
$\lambda^{\rm W}_T$ is the bottom of the hermitian form $W_T$ on $L^2(I_T)$ (complex). Write $\Lambda(\gamma):=\log(\gamma/2\pi)$,
$T_L(\gamma)=\frac12\Lambda(\gamma)$.

**Counting input (N). PROVED-CITED (FROM MEMORY, flagged; R163_702 (N)).** Ordinates are counted with multiplicity. For $t\ge10^3$,
$N(t+1)-N(t)\le\log t$. For every real $t$, $\#\{\rho:\gamma_\rho\in[t,t+1]\}\le\log(|t|+10^3)$. For $|t|<10^3$ this needs only the
table of low zeros, where at most 3 ordinates lie in any unit interval (FROM MEMORY).

**(V). PROVED-CITED (FROM MEMORY, flagged; Platt–Trudgian 2021).** All zeros with $|\gamma|\le H=3\cdot10^{12}$ are on the line and simple.
So $\gamma^*>H$ and $\Lambda^*>\log(3\cdot10^{12}/2\pi)=26.89$, i.e. $T_L(\gamma^*)>13.44$.

**Gevrey bump. PROVED-CITED** (Hörmander, *ALPDO I*, Thm 1.3.5 and the Denjoy–Carleman construction; Rodino, *Linear PDO in Gevrey
spaces*, §1.4). Fix $s\in(1,2)$. There is an even $\psi\ge0$ with $\mathrm{supp}\,\psi\subset[-1,1]$, $\int\psi=1$, and
$$
|\widehat\psi(x+iy)|\le C_\psi\,e^{|y|}\exp(-c_\psi|x|^{1/s})\qquad(x,y\in\mathbb R). \tag{0.2}
$$

**Lemma L1 (pair identity; R163_701). PROVED there.** For $g\in L^2(-T,T)$ put $\Phi=\widehat g\widehat g^\#$. Then
$\mathrm{Re}\,\Phi(x-i\delta)=|\widehat{g\cosh\delta u}(x)|^2-|\widehat{g\sinh\delta u}(x)|^2$.

**Lemma L3 (upper sampling; R163_701). PROVED there.** Let $X$ be a multiset of reals with at most $M$ points in every unit interval
meeting its convex hull. Then for $g\in L^2(-T,T)$, $\sum_{x\in X}|\widehat g(x)|^2\le2\pi M(1+2T)\|g\|^2$.

## §1 Theorem 1 (global sub-Landau detection)

**Data.** Let $\rho_0=\frac12+\delta_0+i\gamma_0$ be a zero with $0<\delta_0<\frac12$ and $\gamma_0\ge10^4$, of multiplicity $m_0\ge1$. Put
$\Lambda_0=\Lambda(\gamma_0)$, $M_0:=\log(2\gamma_0)$, and fix ψ, $s$, $C_\psi$, $c_\psi$ as in (0.2). Define
$$
R_0:=1+\Big(\frac{3\log\gamma_0}{c_\psi}\Big)^{s},\qquad
T_{\rm det}(\rho_0):=1+\frac1{2\delta_0}\max\Big\{3,\ \log\Big(\tfrac{32\pi}{3}\,\delta_0\,(1+\Lambda_0)\,M_0\Big)\Big\},
$$
$$
\kappa(T):=\tfrac12\log\big(256\,e^2(R_0+1)M_0T^2\big).
$$
**(Dom) at $T$:** every zero $\rho\ne\rho_0$ with $|\gamma_\rho-\gamma_0|\le R_0$ has $|\delta_\rho|\le\delta_0-\kappa(T)/T$.

**Theorem 1. PROVED** (given (N), (0.2), (0.1)). There is $\gamma_1(\psi)$, effectively computable from $C_\psi,c_\psi,s$, such that the
following holds. Let $\gamma_0\ge\gamma_1(\psi)$ and $T\in[T_{\rm det}(\rho_0),\frac12\Lambda_0]$, and assume (Dom) at $T$. Then
$\lambda^{\rm W}_T<0$. Consequently $T_c<T_{\rm det}(\rho_0)$ whenever $T_{\rm det}(\rho_0)\le\frac12\Lambda_0$ and (Dom) holds at
$T_{\rm det}(\rho_0)$. (If $\lambda^{\rm W}_T<0$ then $T_c<T$ by continuity, R163_401 2.2–2.3.)

*Test.* Put $T''=T-1$, $b_0:=\mathbf 1_{[-T'',T'']}(u)\sinh(\delta_0u)$ (real, odd), $g:=i\,(\psi*b_0)$ (supported in $[-T,T]$, $i\times$ real
odd), and $F(t):=e^{-i\gamma_0t}g(t)\in L^2(I_T)$. Then $\widehat F(z)=\widehat g(z-\gamma_0)$, and $\widehat g=\widehat\psi\,\widehat{ib_0}$ decays
by (0.2), so $F\in\mathcal D_T$ and (0.1) applies. Write $x_\rho:=\gamma_\rho-\gamma_0$. Group $\rho$ with $1-\bar\rho$, so that
$t_{1-\bar\rho}=\bar t_\rho$. A pair with $\delta_\rho>0$ contributes $2\mathrm{Re}\,\Phi(x_\rho-i\delta_\rho)$, and an on-line zero contributes
$|\widehat g(x_\rho)|^2$. Put
$$
S_0:=\int b_0\sinh(\delta_0u)\,du=\int_{-T''}^{T''}\sinh^2(\delta_0u)\,du=\frac{\sinh(2\delta_0T'')}{2\delta_0}-T''=\|b_0\|^2 .
$$
Since $T\ge T_{\rm det}$, $y'':=2\delta_0T''\ge3$, and so (because $e^{y}/4\ge y+e^{-y}/2$ for $y\ge3$)
$$
S_0\ \ge\ \frac{e^{2\delta_0T''}}{8\delta_0}\ \ge\ \frac{e^3}{4}>5,\qquad S_0^2\ge\frac{e^{4\delta_0T}e^{-4\delta_0}}{64\delta_0^2}\ge\frac{e^{4\delta_0T}}{16e^2}. \tag{1.1}
$$

*Step 1 (the detecting pair). PROVED.* At $\rho_0$ we have $x=0$ and $\delta=\delta_0$. First, $\psi*b_0$ is odd (ψ even, $b_0$ odd), so
$\widehat{g\cosh\delta_0u}(0)=i\int(\psi*b_0)\cosh\delta_0u=0$. Second,
$\int(\psi*b_0)(u)\sinh(\delta_0u)du=\int b_0(v)\int\psi(w)\sinh(\delta_0(v+w))\,dw\,dv=k\,S_0$ with $k=\int\psi\cosh(\delta_0w)\ge1$; the
$\cosh(\delta_0 v)\sinh(\delta_0w)$ part vanishes because ψ is even. By L1 the pair $\{\rho_0,1-\bar\rho_0\}$ contributes
$-2m_0k^2S_0^2\le-2S_0^2$.

*Step 2 (near on-line zeros, $|x_\rho|\le R_0$). PROVED.* Every unit interval within distance $R_0+1\le\gamma_0/2$ of $\gamma_0$ carries
at most $\log(\frac32\gamma_0+10^3)\le M_0$ ordinates (N). By L3 and Young's inequality ($\|g\|\le\|\psi\|_1\|b_0\|$), their contribution
is at most $2\pi M_0(1+2T)S_0$.

*Step 3 (near off-line pairs other than $\rho_0$). PROVED.* For such a pair, $2\mathrm{Re}\,\Phi\le2|\widehat{g\cosh\delta_\rho u}(x_\rho)|^2$
(drop the sinh part). Next, $|g(u)|\le\sinh(\delta_0T)\le\frac12e^{\delta_0T}$ and
$\int_{-T}^T\cosh(\delta_\rho u)du\le2Te^{\delta_\rho T}$. So each pair contributes at most $2T^2e^{2(\delta_0+\delta_\rho)T}$. Under (Dom),
$e^{2\delta_\rho T}\le e^{2\delta_0T-2\kappa}$. There are at most $(2R_0+2)M_0$ such pairs. With (1.1) the total is
$\le4(R_0+1)M_0T^2e^{4\delta_0T}e^{-2\kappa}\le64e^2(R_0+1)M_0T^2e^{-2\kappa}S_0^2=\frac14S_0^2$, by the choice of $\kappa$.

*Step 4 (far zeros, $|x_\rho|>R_0$, including $\gamma_\rho<0$ and the low zeros). PROVED.* For $|y|\le\frac12$:
$|\widehat{ib_0}(x+iy)|\le\int_{-T}^T|\sinh\delta_0u|e^{|u|/2}du\le Te^{(\delta_0+\frac12)T}$, so by (0.2)
$|\widehat g(x+iy)|\le C_\psi e^{1/2}Te^{(\delta_0+\frac12)T}\exp(-c_\psi|x|^{1/s})$. Each zero in (0.1) contributes at most
$\sup_{|y|\le1/2}|\widehat g(x_\rho+iy)|^2$. For $\gamma_0\ge10^4$, (N) gives at most $M_0(1+\log(1+n))$ ordinates in each of the two
unit intervals at distance $n$ from $\gamma_0$. Using $e^{-2c|x|^{1/s}}\le e^{-c(R_0-1)^{1/s}}e^{-c n^{1/s}}$ for $|x|\ge n\ge R_0-1$, the far
part is
$$
\le 2eC_\psi^2T^2e^{(2\delta_0+1)T}M_0\,\Sigma_\psi\,e^{-c_\psi(R_0-1)^{1/s}},\qquad \Sigma_\psi:=\sum_{n\ge0}(1+\log(1+n))e^{-c_\psi n^{1/s}}<\infty .
$$
By the choice of $R_0$, $e^{-c_\psi(R_0-1)^{1/s}}=\gamma_0^{-3}$. Since $T\le\frac12\Lambda_0$ and $\delta_0<\frac12$,
$e^{(2\delta_0+1)T}\le e^{2T}\le\gamma_0/2\pi$. So the far part is $\le eC_\psi^2\Sigma_\psi\Lambda_0^2M_0\gamma_0^{-2}/(4\pi)$. This is
$\le\frac14\cdot25<\frac14S_0^2$ once $\gamma_0\ge\gamma_1(\psi)$ (polylog against $\gamma_0^2$).

*Step 5 (conclusion).* Adding Steps 1–4,
$$
W_T(F)\le-2S_0^2+\tfrac12S_0^2+2\pi M_0(1+2T)S_0=-\tfrac32S_0\Big(S_0-\tfrac{4\pi}3M_0(1+2T)\Big).
$$
By (1.1) and $1+2T\le1+\Lambda_0$, the bracket is positive when $e^{2\delta_0(T-1)}>\frac{32\pi}3\delta_0(1+\Lambda_0)M_0$. That holds for
$T\ge T_{\rm det}$. So $W_T(F)<0$ with $F\ne0$, and $\lambda^{\rm W}_T<0$. ∎

**Remark 1.1 (what was used).** Only (0.1), the pairing $\rho\leftrightarrow1-\bar\rho$, (N), and a compactly supported Gevrey bump. No
primitivity correction is needed, because (0.1) is the complete form $W_T$, poles included. This is a **detector**. It is class-blind and
carries no sign (W3), exactly as R163_701 Rem B.3 says of its local version.

**Remark 1.2 (comparison with R163_701 Thm B).** There the localiser has width $\varepsilon\asymp\log\gamma$ and dominance window
$(\log\gamma)^{1/2}$, and the tail is ARGUED. Here the width is 1, the window is $R_0\asymp(\log\gamma_0)^s$, and the tail is PROVED. The
threshold has the same shape: $T_{\rm det}\le\frac12\Lambda_0-C'$ reads
$$
y_0:=\delta_0\Lambda_0\ \ge\ \log(y_0\Lambda_0)+\log\tfrac{32\pi}{3}+\log\tfrac{M_0}{\Lambda_0}+2\delta_0(1+C')+o(1)
\iff y_0\ge\log\Lambda_0+\log\log\Lambda_0+O(1+C').
$$

**Remark 1.3 (lattice substitution = Lemma 4.10). PROVED.** Under (M1)–(M2) of R163_402, the on-line sum in Step 2 is exactly
$\Lambda\|g\|^2$ (Poisson, for type $2T<\Lambda$) instead of $\le2\pi M(1+2T)\|g\|^2$. The off-line part is a single quartet, and no
smoothing is needed (ψ = δ-mass, $T''=T$). Step 5 becomes $-2S^2+\Lambda S<0\iff S(T,\delta)>\Lambda/2=\pi\rho$, which is R163_402 Thm 4 /
Lemma 4.10 together with its extremal (odd, node at the vertex). The factor $2\pi M(1+2T)/\Lambda\asymp\Lambda$ is the whole difference
between the lattice threshold $y>y_0=2.1773$ and the ζ threshold $y>\log\Lambda+\log\log\Lambda+O(1)$ (cf. R163_701 Rem B.1).

## §2 Consequences for (Det−)

**(Det−)[$C'$]** (R165_000 §1): $\lambda^{\rm W}_T>0$ for all $T\le T_L(\gamma^*)-C'$.

**Corollary 2. PROVED** (from Thm 1 and monotonicity of $\lambda^{\rm W}$, R163_401 2.2).
- (a) *No $\gamma$-uniform constant.* Fix $\delta\in(0,\frac12)$ and $C'\ge0$. There is $\gamma_2(\delta,C',\psi)$ such that, if
  $\rho^*$ satisfies $\delta^*\ge\delta$, $\gamma^*\ge\gamma_2$ and (Dom) at $T_{\rm det}(\rho^*)$, then (Det−)[$C'$] fails. In fact
  $T_c<T_{\rm det}(\rho^*)=\frac{\log\Lambda^*}{\delta^*}(1+o(1))\ll T_L(\gamma^*)-C'$, and $T_L-T_c\to\infty$. So no $C'(\delta^*)$ works
  uniformly in $\gamma^*$ in this regime.
- (b) *(Det−) is a zero-location statement for $\rho^*$.* If (Det−)[$C'$] holds and $\rho^*$ satisfies (Dom) at $T_{\rm det}(\rho^*)$, then
  $T_{\rm det}(\rho^*)>T_L(\gamma^*)-C'$, i.e.
  $$
  Z(C'):\qquad \delta^*\Lambda^*<\max\Big\{3+2\delta^*(1+C'),\ \log\big(\tfrac{32\pi}3\delta^*(1+\Lambda^*)\log(2\gamma^*)\big)+2\delta^*(1+C')\Big\}
  =\log\Lambda^*+\log\log\Lambda^*+O(1+C').
  $$
- (c) *The lowest quartet does not decide contact.* If (Det−)[$C'$] holds, then **every** off-line zero ρ (at any height
  $\gamma\ge\gamma^*$, with $\gamma\ge\gamma_1$) that satisfies (Dom) at $T_{\rm det}(\rho)$ has $T_{\rm det}(\rho)\ge T_L(\gamma^*)-C'$. (Since
  $\gamma\ge\gamma^*$, $T_L(\gamma^*)-C'\le\frac12\Lambda(\gamma)$, so Thm 1 applies.) Equivalently, every dominant off-line zero obeys the
  uniform strip
  $$
  \delta_\rho\le\frac{\log\big(\frac{32\pi}{3}\delta_\rho(1+\Lambda(\gamma_\rho))\log(2\gamma_\rho)\big)}{\Lambda^*-2C'-2}\quad\Big(=O\Big(\frac{\log\log\gamma_\rho}{\Lambda^*}\Big)\Big),
  $$
  which is nontrivial (below ½) for $\log\log\gamma_\rho\lesssim\Lambda^*/4$. A zero *above* $\gamma^*$ with larger δ makes contact before the
  lowest quartet whenever its $T_{\rm det}$ is smaller.

*Proof.* (a) $T_{\rm det}(\rho^*)-1\le\frac{1}{2\delta}\max\{3,\log(C\Lambda^{*2})\}$, which is $o(\Lambda^*)$. Apply Thm 1 at
$T=T_{\rm det}$, then monotonicity. (b) Contrapositive of Thm 1 at $T=T_{\rm det}(\rho^*)$, combined with $\lambda^{\rm W}>0$ on
$(0,T_L-C']$. (c) The same argument for ρ, using that $\lambda^{\rm W}_T$ is a single global quantity. ∎

**2.4 At the verified height. PROVED** (hand arithmetic). Take $\gamma_0=3\cdot10^{12}$, so $\Lambda_0=26.89$, $M_0=29.42$ and
$T_L=13.44$. Then $\frac{32\pi}3\delta_0(1+\Lambda_0)M_0$ equals $\approx1.10\cdot10^4$ at $\delta_0=0.40$ ($T_{\rm det}=12.6<T_L$),
$\approx1.05\cdot10^4$ at $0.38$ ($T_{\rm det}=13.2<T_L$), and $\approx9.6\cdot10^3$ at $0.35$ ($T_{\rm det}=14.1>T_L$). So, at heights
just above $H$, Thm 1 places a contact below the Landau window iff $\delta_0\gtrsim0.37$, given (Dom) and $\gamma_0\ge\gamma_1(\psi)$. The
constant $\gamma_1(\psi)$ is not evaluated, so whether $H\ge\gamma_1(\psi)$ is OPEN, though it is only a polylog-versus-$\gamma^2$ condition.
As γ grows the threshold falls like $(\log\Lambda+\log\log\Lambda)/\Lambda$.

**Prop 3 (lattice model, exact δ-threshold with $C'$). PROVED** (from Lemma 4.10 / R163_402 Thm 4). Under (M1)–(M2) with one quartet,
$T\mapsto\inf$ is nonincreasing. Hence (Det−)[$C'$], read as nonnegativity on $(0,T_L-C']$ with the boundary case allowed, holds iff
$S(T_L-C',\delta)\le\Lambda/2$. With $y=\delta\Lambda$ and $s=2\delta C'<C'$, that is
$$
\sinh(y-s)\le2y-s .
$$
For $s=0$ this is $y\le y_0=2.1773$, which is Lemma 4.10. For fixed $C'$ and δ, it fails once $y$ exceeds the root $y_0(s)$, which is finite.
So in the model, (Det−) with $C'$ independent of γ holds **iff $\delta\Lambda=O(1)$**: true for $\delta^*\le y_0(s)/\Lambda^*$, false above.
The model therefore says "δ\*-dependent, true iff $\delta^*L\le y_0$-type threshold", exactly as anticipated in the task. Thm 1 shows the
same failure is real for ζ, at the larger threshold $\log\Lambda+\log\log\Lambda$. ∎

## §3 (a) Why sampling cannot give the obstruction beyond $y=O(\log\Lambda)$

**Prop 4 (sampling trade-off). PROVED.** Let $T<T_L(\gamma^*)$, and let $A_T\le B_T$ be any constants with
$A_T\|w\|^2\le\sum_{\rm on,\,|x|\le R}|\widehat w(x_\rho)|^2\le B_T\|w\|^2$ for $w\in L^2(-T,T)$ (a local frame; B is finite by L3, with
$B_T\le2\pi M(1+2T)$; A may be 0). Then:
- (i) For the test $g$ of Thm 1, the ratio of the quartet's negative part to the on-line part is at least
  $2S_0^2/(B_TS_0)=2S_0/B_T$. So **no** inequality of the form "on-line mass ≥ $A_T\|F\|^2$" yields $W_T>0$ once $2S(T-1,\delta^*)>B_T$.
- (ii) Conversely, under (Dom) and a ZFR as in R163_701 Thm A, positivity holds while $(\sqrt{A_T}-\sqrt{B_T}(\cosh\eta T-1))^2>2B_T\sinh^2\eta T$
  (R163_701 (A.2)). For the quartet itself this requires $\eta T\lesssim\sqrt{A_T/B_T}$, i.e. $\delta^*T=O(1)$.

So the obstruction holds where $e^{2\delta^*T}/\delta^*\lesssim B_T$ and is lost where $e^{2\delta^*T}/\delta^*\gtrsim B_T$. The fact that
node density is below zero density gives at most a frame constant of order Λ (Landau's necessary density concerns the *existence* of $A_T>0$,
not its size). It never gives an exponential in $T$.
*Proof.* (i) Steps 1–2 of Thm 1 give an on-line part $\le B_T\|g\|^2\le B_TS_0$ and a quartet part $\le-2S_0^2$. (ii) Cited. ∎

**Reconciliation, stated exactly.** The task's picture "below $T_L$ the nodes cannot vanish at all nearby on-line zeros, hence a lower
bound" is right but **irrelevant to the sign**. The test of Thm 1 vanishes at only one point, $\gamma_0$, the cone vertex, and leaves
$\asymp\Lambda/(2T)$ on-line zeros per cell fully visible. Their total weight $\le2\pi M(1+2T)S_0$ is linear in $S_0$, while the quartet's
gain is quadratic in $S_0\asymp e^{2\delta T}/\delta$. Contact sub-Landau happens by **amplification** (the $e^{\delta|u|}$ weight of an
off-line evaluation), not by **annihilation** (node absorption, which is the supra-Landau mechanism of (Det+)/R163_702 $K_H$).

**Prop 5 (conditional positive direction). PROVED-CITED** (R163_701 Thm A; R163_601 Thm 1, cell decomposition $\{P_{\rm loc}\}\Leftrightarrow$
D, record). (Det−)[$C'$] holds if, for every height γ and every $T'\le T_L(\gamma^*)-C'$, the local frame (A.1) of R163_701 holds with
$A/B$ bounded below and all zeros near γ satisfy $\delta\le c\sqrt{A/B}/T'$. Both hypotheses are OPEN (O701.2; and a ZFR of width
$1/\Lambda^*$ at all heights is beyond any known region). A *global* frame is not available even in principle: the upper frame constant
grows like $\log\gamma$ with height, which is why the positive direction must go through localisation.

## §4 (b) The sub-Landau witness, and what R163_701 says about the lowest quartet

- **Cell count. PROVED** (from (N) on average; the pointwise count is only $O(\log\gamma)$). At contact $T_c$, the cell has length $\pi/T_c$
  and on average $\Lambda^*/(2T_c)$ on-line ordinates. In regime 3, $T_c<T_{\rm det}\approx\log(y\Lambda^*)/(2\delta^*)$, so the average is
  $\ge y/\log(y\Lambda^*)>1$. Pointwise, the count is between 0 and $O(\log\gamma^*)$, since (I1-a) is not localisable.
- **$(\star_{\rm cell})$ at a sub-Landau contact. PROVED** (Rem 4.8a identity + Cor 4.10a argument). If the contact is caused by ρ\* (all
  other cells have $N_j=0$), then $P_0\le N_0$ in its cell, while $P_0$ is not small. In the Thm 1 test, $P_0\le2\pi M(1+2T)\|g\|^2$ and
  $N_0\ge2\|g\|^4$, with $\|g\|^2\asymp S_0$. The "invisible on-line zeros" scenario does not occur. The failure of $(\star_{\rm cell})$ is
  a pure size effect.
- **R163_701 on the lowest quartet. PROVED** (reading of Thm B). Steps 1, 2 and 4 of Thm B use one localised test at $\gamma_0$ and the
  hypothesis $P_{\rm loc}(\gamma_0,T')$ at that single $\gamma_0$. So the one-zero contrapositive holds: $P_{\rm loc}(\gamma^*,\frac12\Lambda^*-C')$
  together with (Dom) at ρ\* gives $\delta^*\le(\log\Lambda^*+\log\log\Lambda^*+O(1))/\Lambda^*$ (tail ARGUED there, PROVED here in global form).
  Thm B's "RH-strength" refers to the uniform-in-γ hypothesis. For the lowest quartet alone the conclusion is $Z(C')$: a single-zero
  near-line bound, not known for any zero and not RH.
- **Non-dominant case. OPEN (O701.1).** If several zeros within $R_0$ of $\gamma^*$ have δ within $\kappa/T$ of each other, Step 3 fails.
  Phases $e^{ix_\rho u}$ could cancel the cluster's sinh-parts, and nothing above excludes a cluster for which (Det−) holds at larger δ.

## §5 Falsifier tests

| test | outcome | consistent? |
|---|---|---|
| lattice model (R163_402 (M1)–(M2)) | Rem 1.3: Thm 1 reduces to Lemma 4.10 exactly; Prop 3: (Det−) true iff $\sinh(y-s)\le2y-s$ | yes, agrees with Lemma 4.10 and Cor 4.10a |
| $M_m$ (ξ × rational, $m$ quartets) | its explicit formula is (0.1) with its own zeros (Paper 48 `tab:falsifiers`, record); counting (N) holds with $M_0+4m$; one isolated quartet is dominant. So for $\delta^*\Lambda^*\ge\log\Lambda^*+\log\log\Lambda^*+K$, (Det−) is **false for $M_m$** (PROVED, given the record). Any proof of (Det−) for ζ must therefore use arithmetic, and through it must prove $Z(C')$ | yes: (Det−) is not a zero-set theorem |
| $f_t$, $f_\chi$, DH | Thm 1 is class-blind (Rem 1.1) and applies to each with its own $N$ | yes (W3: detector, no sign) |
| verified zeros $\gamma^*>H$ | gives $\Lambda^*>26.89$ only; at that height regime 3 starts near $\delta^*\approx0.37$ (§2.4); nothing in (V) restricts $\delta^*$ | (V) cannot prove (Det−) (cf. R163_702 Thm B: the test of Thm 1 has its mass above H) |

## §6 Grid cells (append to R162_2300_MASTER_GRID)

- **7A** (zeros × one window form) — R165_102 Thm 1: global sub-Landau detection with tail PROVED and explicit constants. PROVED-TOOL.
  (Det−) for the lowest quartet: DEAD as a route to $(\star_{\rm cell})$, because it is a zero-location statement ($Z(C')$, Cor 2(b)) and is
  false for $M_m$ (W3 + E1-type: positivity below Landau ⇔ near-line zeros). Item 25 (D.16-γ, cone cut by the zero data) is now attacked:
  the cut is a size effect (amplification), not a node effect.
- **7D** (zeros × spectrum) — Cor 2(c): first contact is governed by $\min_\rho T_{\rm det}(\rho)$, not by the lowest quartet. So
  "$T_c=T_L(\gamma^*)+O(1)$" (R165_000 §1) is false in regime 3, and the critical interlacing (EC) can be the geometry at $T_c$ only for
  $\delta\Lambda=O(1)$. PARTIAL.
- **2A** (positivity/support × one window) — Prop 4: sampling or frame inequalities (Beurling–Landau, MZ, Gallagher) cannot carry
  positivity past $2\delta T\approx\log(\delta\Lambda T)$. DEAD [W2-type: frame constants polynomial, gain exponential].

## Ledger

| step | label |
|---|---|
| (0.1) complete-form zero identity, complex tests | PROVED-CITED (Paper 46 `lem:roughEF`, R163_401 Lemma 3.0; record) |
| (N) counting; (V) verification | PROVED-CITED, FROM MEMORY (flagged) |
| (0.2) Gevrey bump | PROVED-CITED (Hörmander Thm 1.3.5; standard) |
| L1, L3 | PROVED (R163_701) |
| Thm 1 Steps 1–5 | PROVED |
| $\gamma_1(\psi)$ numerical value; whether $H\ge\gamma_1$ | OPEN (not computed) |
| Rem 1.3 lattice substitution = Lemma 4.10 | PROVED |
| Cor 2(a)–(c) | PROVED |
| §2.4 threshold ≈0.37 at $H$ | PROVED (arithmetic on Thm 1; conditional on $H\ge\gamma_1(\psi)$ and (Dom)) |
| Prop 3 (model, with $C'$) | PROVED in the model |
| Prop 4 sampling trade-off | PROVED |
| Prop 5 conditional positive direction | PROVED-CITED; hypotheses OPEN |
| §4 cell count (average), $(\star_{\rm cell})$ failure at sub-Landau contact, R163_701 single-zero reading | PROVED |
| (Dom) removal | OPEN (O701.1) |
| middle regime $y_0<\delta\Lambda<\log\Lambda+\log\log\Lambda$ for ζ | OPEN (O701.3: cell-scale upper frame $O(\Lambda)$ would close it to $O(1)$) |
| (Det−) for ζ | **OPEN**; false in regime 3 under (Dom); implies $Z(C')$ |
| Row D | **OPEN** |

**Open items.** (O102.1) Evaluate $\gamma_1(\psi)$ for an explicit Gevrey ψ, and decide whether $H=3\cdot10^{12}$ suffices. (O102.2)
(Det−) restricted to configurations with $\delta^*\Lambda^*\le y_0$, i.e. the only regime where (EC) can be the contact geometry: this
needs O701.2 at height $\gamma^*$ and Cor 2(c) for all higher zeros.
