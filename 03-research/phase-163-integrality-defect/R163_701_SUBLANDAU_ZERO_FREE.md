# R163_701 — The sub-Landau part of $P_{\rm loc}$ on actual ζ: zero-free regions in both directions

* Pure mathematics; no numerics. Nothing outside this file was edited. No label of record moves.*
*Inputs: R163_601 (Def of $\mathrm{Loc}_{T'}(\gamma)$, $P_{\rm loc}$; Thm 1; Cor 2; §4.1 localised explicit formula; §3(2c) regimes),
R163_602 (§2.1 trivial range, §2.3 lattice zero-free statement, open item O602.1 = this memo's target), R163_402 (Thm 4 sinh law,
Lemma 1 light cone, Erratum D1: exact lattice threshold $\delta L>y_0=2.1773\ldots$, $\sinh y_0=2y_0$).*
*Corpus check.* O602.1 asked for "a rigorous version of §2.3 for actual ζ zeros, without (M2)". R163_401 Lemma 4.10/Cor 4.10a
treat the lattice model only. Nothing in phase 163 handles the real zero set; this memo does.

**Labels.** PROVED; PROVED-CITED (reference given, FROM MEMORY where flagged); ARGUED (argument given, unproved step named); OPEN.

## Outcome first

The task conjectured: "sub-Landau $P_{\rm loc}$ ⟺ (up to constants) zero-free region $\beta<\frac12+c\,\log\log\gamma/\log\gamma$". What is
true is **asymmetric**. The $\log\log$ is the *unconditional loss in the on-line sampling constants*, not a feature of $P_{\rm loc}$.

| # | statement | label |
|---|---|---|
| L1 | pair identity: $2\,\mathrm{Re}\,\Phi(x-i\delta)=2|\widehat{g\cosh\delta u}(x)|^2-2|\widehat{g\sinh\delta u}(x)|^2$, $\Phi=\widehat g\widehat g^\#$ | PROVED |
| L2 | Taylor–Minkowski transfer: variable $\delta_\rho\le\eta$ costs at most $\sinh(\eta T')$, $\cosh(\eta T')-1$ in $\ell^2$ over zeros | PROVED |
| L3 | unconditional upper sampling at the zeros: $\sum_\rho|G(\gamma_\rho-\gamma)|^2\le C_0\log\gamma\,(1+2T')\|G\|^2$ (localised) | PROVED (from $N(t+1)-N(t)\ll\log t$) |
| Thm A (⇐) | zero-free region of width $\eta$ + a **local lower frame** $A$ at window $T'$ ⇒ $P_{\rm loc}(\gamma,T')$ whenever $\sinh(\eta T')+\sqrt{B/A}\,(\cosh\eta T'-1)<\sqrt{A/B}$-type condition (exact form (A.2)); for $T'\asymp\log\gamma$ this needs $\eta\le c\sqrt{A/B}/\log\gamma$ | PROVED (conditional on the frame) |
| Thm A′ | the frame hypothesis is unconditional only for $T'\le c\log\log\gamma$ (Littlewood gaps) — i.e. inside the already-trivial range | ARGUED (citations FROM MEMORY) |
| Thm B (⇒) | if $P_{\rm loc}(\gamma,T')$ holds for all $\gamma$ and all $T'\le\frac12\log(\gamma/2\pi)-C'$, then every **locally dominant** zero has $\beta-\frac12\le(1+o(1))\dfrac{\log\log\gamma}{\log\gamma}$ | core inequality PROVED; tail bookkeeping ARGUED |
| B′ | removal of the dominance hypothesis (clusters of off-line zeros with $\delta$ within $O(\log\log\gamma/\log\gamma)$ of each other) | **OPEN** (O701.1) |
| Cor C | under a lattice-strength frame ($A\asymp B\asymp\log\gamma$), both directions hold at the *same* width $\asymp1/\log\gamma$ (constants differ) — the true equivalence is with a $1/\log\gamma$ region, not $\log\log/\log$ | PROVED modulo the frame (A) and (Dom) (B) |
| §4 | comparison: dlVP/VK are regions at distance $\frac12-o(1)$ from the line; Thm B's output implies $\psi(x)=x+O(\sqrt x\log^{3}x)$, Lindelöf, density hypothesis | ARGUED (standard) |
| sub-Landau $P_{\rm loc}$ for ζ | | **OPEN** (⟹ quasi-RH; Thm B) |
| Row D | | **OPEN** |

**Verdict.** Sub-Landau $P_{\rm loc}$ is *not* a weak statement: by Thm B it already forces (for dominant zeros) a
$\frac12+(1+o(1))\log\log\gamma/\log\gamma$ zero-free region, which is of RH strength for every standard consequence up to
powers of $\log$. Conversely a zero-free region alone does **not** give it: (⇐) needs in addition a local frame (lower
sampling inequality for $PW_{T'}$ at the zero ordinates at cell scale), which is unknown in the sub-Landau range even under
RH, and with the frame the region needed is $1/\log\gamma$, a factor $\log\log\gamma$ thinner than what (⇒) delivers.
The task's "equivalence up to constants" is therefore false as stated on present knowledge; it holds at width $1/\log\gamma$
under a frame hypothesis (Cor C), which is the honest version of R163_602 §2.3 for actual ζ.

---

## §0 Setting and the zero side

Notation of R163_601. For $F=\psi_\gamma*H\in\mathrm{Loc}_{T'}(\gamma)$ write $F(t)=e^{-i\gamma t}g(t)$, $\mathrm{supp}\,g\subset[-T',T']$,
$\widehat g(s)=\widehat\psi(s)\widehat H(s+\gamma)$, $\Phi:=\widehat g\,\widehat g^\#$. By R163_601 §4.1 (PROVED),
$$
\mathfrak a_{T'}(F)=\sum_\rho\Phi(t_\rho-\gamma),\qquad t_\rho=\gamma_\rho-i\delta_\rho,\ \ \delta_\rho=\beta_\rho-\tfrac12\in(-\tfrac12,\tfrac12). \tag{0.1}
$$
By the functional equation zeros come in pairs $\rho,1-\bar\rho$, i.e. $t=x-i\delta$ and $x+i\delta$ (here $x=\gamma_\rho-\gamma$). Since
$\Phi^\#=\Phi$, $\Phi(x+i\delta)=\overline{\Phi(x-i\delta)}$, so a pair contributes $2\,\mathrm{Re}\,\Phi(x-i\delta)$; an on-line zero contributes
$\Phi(x)=|\widehat g(x)|^2\ge0$. Summing over *distinct ordinates with* $\delta_\rho\ge0$ (pairs counted once, weight 2 if $\delta>0$):
$$
\mathfrak a_{T'}(F)=\sum_{\delta_\rho=0}|\widehat g(x_\rho)|^2+\sum_{\delta_\rho>0}2\,\mathrm{Re}\,\Phi(x_\rho-i\delta_\rho). \tag{0.2}
$$
Notation: $\Lambda:=\log(\gamma/2\pi)$; Landau ceiling $\pi\rho=\Lambda/2$; sub-Landau: $T'\le\Lambda/2-C'$.
$\widehat{w}$ always means $\int w(u)e^{ixu}du$; $\|\cdot\|$ is $L^2(\mathbb R)$ in $u$, so $\|\widehat w\|^2_{L^2(dx)}=2\pi\|w\|^2$.

## §1 Three lemmas

**Lemma L1 (pair identity). PROVED.** For $g\in L^2(-T',T')$ (complex) and $\delta\in\mathbb R$, $x\in\mathbb R$,
$$
\mathrm{Re}\,\Phi(x-i\delta)=|\widehat{g_c}(x)|^2-|\widehat{g_s}(x)|^2,\qquad g_c:=g\cosh\delta u,\ \ g_s:=g\sinh\delta u .
$$
*Proof.* $\widehat g(x-i\delta)=\int g e^{\delta u}e^{ixu}=:a$, and $\widehat g^\#(x-i\delta)=\overline{\widehat g(x+i\delta)}=\overline{\int ge^{-\delta u}e^{ixu}}=:\bar b$.
$\mathrm{Re}(a\bar b)=\frac14(|a+b|^2-|a-b|^2)$ with $a+b=2\widehat{g_c}(x)$, $a-b=2\widehat{g_s}(x)$. ∎
This is the exact real-zero-set form of the sinh mechanism of R163_402 Thm 4: an off-line pair is a positive
"cosh-sample" minus a "sinh-sample" at the *same* ordinate.

**Lemma L2 (Taylor–Minkowski transfer). PROVED.** Let $\{x_\rho\}$ be a multiset, $0\le\delta_\rho\le\eta$, and suppose
$\sum_\rho|\widehat w(x_\rho)|^2\le B\|w\|^2$ for all $w\in L^2(-T',T')$. Then for every $g\in L^2(-T',T')$
$$
\Big(\sum_\rho|\widehat{g\sinh\delta_\rho u}(x_\rho)|^2\Big)^{1/2}\le\sqrt B\,\sinh(\eta T')\|g\|,\qquad
\Big(\sum_\rho|\widehat{g(\cosh\delta_\rho u-1)}(x_\rho)|^2\Big)^{1/2}\le\sqrt B\,(\cosh\eta T'-1)\|g\|.
$$
*Proof.* $\sinh(\delta_\rho u)=\sum_{k\ge0}\delta_\rho^{2k+1}u^{2k+1}/(2k+1)!$, so $\widehat{g\sinh\delta_\rho u}(x_\rho)=\sum_k\frac{\delta_\rho^{2k+1}}{(2k+1)!}\widehat{gu^{2k+1}}(x_\rho)$
(the series converges in $L^1(-T',T')$). Minkowski in $\ell^2_\rho$, then $|\delta_\rho|\le\eta$ and the hypothesis with $w=gu^{2k+1}$, $\|gu^{j}\|\le T'^{j}\|g\|$:
$\|\cdot\|_{\ell^2_\rho}\le\sum_k\frac{\eta^{2k+1}}{(2k+1)!}\sqrt B\,T'^{2k+1}\|g\|$. Same for $\cosh-1$ with even powers $k\ge1$. ∎

**Lemma L3 (unconditional upper sampling). PROVED.** Let $M(\gamma,R):=\max\{N(t+\tfrac12)-N(t-\tfrac12):|t-\gamma|\le R\}$ (ordinates counted
with multiplicity). For $G=\widehat w$, $w\in L^2(-T',T')$, and any set $X$ of ordinates in $[\gamma-R,\gamma+R]$,
$$
\sum_{\gamma_\rho\in X}|G(\gamma_\rho-\gamma)|^2\le M(\gamma,R)\,(1+2T')\,2\pi\|w\|^2 ,\qquad M(\gamma,R)\le C_0\log\gamma\ \ (R\le\gamma/2).
$$
*Proof.* Gallagher's inequality on a unit interval $I\ni y$: $|G(y)|^2\le\int_I|G|^2+\int_I|(G^2)'|\le\int_I|G|^2+2\int_I|G||G'|$.
Cover by unit intervals $I_j=[j-\frac12,j+\frac12]$; each $I_j$ carries $\le M$ points; sum and Cauchy–Schwarz:
$\sum|G|^2\le M(\|G\|^2_{L^2}+2\|G\|\|G'\|)$, and Bernstein $\|G'\|\le T'\|G\|$ ($G$ of type $T'$). The count bound is
$N(t+1)-N(t)=O(\log t)$ (Titchmarsh, *Theory of the Riemann zeta-function*, Thm 9.2; PROVED-CITED, FROM MEMORY as to numbering). ∎
*Comparison.* In the lattice model (M2) the exact constant is $2\pi\rho=\Lambda$ (Poisson, R163_402 Thm 4 step 1). L3 loses the
factor $(1+2T')\asymp\log\gamma$ in the sub-Landau range. **This factor is the origin of the $\log\log\gamma$** in §3. It is unavoidable
with present knowledge: $S(t)=O(\log t)$ is all that is known pointwise, so a cell of length $1/T'$ may carry $\asymp\log\gamma$
ordinates instead of $O(1)$.

## §2 Direction (⇐): zero-free region ⇒ $P_{\rm loc}$, and what else it needs

**Hypotheses.** (ZFR$_\eta$) $0\le\delta_\rho\le\eta$ for all zeros with $|\gamma_\rho-\gamma|\le R$, and $|\delta_\rho|\le\eta(\gamma_\rho)$ globally for
$\gamma_\rho\ge\gamma_1$, with $\eta(\cdot)$ decreasing. (Frame$_{A,B}$) for all $w\in L^2(-T',T')$ that arise as $g$ in $\mathrm{Loc}_{T'}(\gamma)$,
$$
A\|w\|^2\le\sum_{|\gamma_\rho-\gamma|\le R}|\widehat w(\gamma_\rho-\gamma)|^2\ \ (\text{ordinates, multiplicity, one per pair}),\qquad\text{and the upper bound with }B. \tag{A.1}
$$
$B$ is available unconditionally (L3: $B\le2\pi C_0\log\gamma(1+2T')$); $A$ is the lower frame.

**Theorem A (⇐). PROVED (conditional on (ZFR$_\eta$), (Frame$_{A,B}$)).** Under these hypotheses, for every $F\in\mathrm{Loc}_{T'}(\gamma)$,
$$
\mathfrak a_{T'}(F)\ \ge\ \Big[\big(\sqrt A-\sqrt B(\cosh\eta T'-1)\big)_+^2-2B\sinh^2(\eta T')\Big]\|g\|^2-\mathcal E_{\rm far}(F), \tag{A.2}
$$
where $\mathcal E_{\rm far}$ collects zeros with $|\gamma_\rho-\gamma|>R$ and is $\le C_N\,e^{2T'\eta^*}(1+R\varepsilon)^{-N}\gamma\log\gamma\,\|H\|^2$ with $\eta^*=\sup_{\rm far}\delta_\rho\le\frac12$.
Hence $P_{\rm loc}(\gamma,T')$ holds as soon as the bracket is positive and dominates $\mathcal E_{\rm far}$.
*Proof.* By (0.2) and L1, each zero (on-line: $\delta=0$, $g_c=g$, $g_s=0$) contributes $c_\rho(|\widehat{g_c}(x_\rho)|^2-|\widehat{g_s}(x_\rho)|^2)$,
$c_\rho\in\{1,2\}$. Lower-bound the positive part with $c_\rho\ge1$ and the reverse triangle inequality in $\ell^2_\rho$:
$(\sum|\widehat{g_c}(x_\rho)|^2)^{1/2}\ge(\sum|\widehat g(x_\rho)|^2)^{1/2}-(\sum|\widehat{g(\cosh\delta_\rho u-1)}(x_\rho)|^2)^{1/2}\ge(\sqrt A-\sqrt B(\cosh\eta T'-1))\|g\|$ (Frame + L2).
Upper-bound the negative part with $c_\rho\le2$ and L2. Far zeros: Paley–Wiener–Schwartz for $\widehat\psi$ (R163_601 §1),
$|\Phi(x-i\delta)|\le C_Ne^{2\varepsilon|\delta|}e^{2(T'-\varepsilon)|\delta|}(1+|x|\varepsilon)^{-2N}\cdot 2(T'-\varepsilon)\|H\|^2$, summed with $N(2\gamma)\ll\gamma\log\gamma$ and
the mirror ordinates at distance $\ge\gamma$. ∎

**Reading of (A.2).** With $\eta T'\le1$: bracket $=A-O(\sqrt{AB}\,\eta^2T'^2)-2B\eta^2T'^2(1+O(\eta^2T'^2))$. Positivity needs
$$
\eta\ \le\ c\,\sqrt{A/B}\;\frac1{T'}\qquad(c\text{ absolute}). \tag{A.3}
$$
At the top of the sub-Landau range, $T'\asymp\log\gamma$: **the region needed is $\eta\lesssim\sqrt{A/B}/\log\gamma$**, not
$\log\log\gamma/\log\gamma$. If $\eta T'\to\infty$ the bracket is negative for any frame ratio (the sinh term grows like $e^{2\eta T'}$, the
cosh term only enters the positive side with the factor $(\sqrt A-\sqrt B\cosh)$, which also goes negative). So (⇐) **cannot**
be obtained from a $\log\log\gamma/\log\gamma$ region by this argument, and §3 plus the lattice model (R163_402 Thm 4: a quartet with
$\delta\Lambda>y_0$ *is* detected sub-Landau when the ordinates are a lattice) show it is in fact false in the regular-spacing
picture: a zero at $\delta=\log\log\gamma/\log\gamma\gg y_0/\Lambda$ among lattice-like neighbours violates sub-Landau $P_{\rm loc}$. (ARGUED for ζ;
PROVED in the lattice model.)

**Theorem A′ (status of the frame). ARGUED; citations FROM MEMORY.**
- (i) *Unconditionally*, ordinates have gaps $\gamma_{n+1}-\gamma_n\ll1/\log\log\gamma_n$ (Littlewood 1924; Titchmarsh Thm 9.12). A set with
  maximal gap $h<\pi/T'$ is a weighted sampling set for $PW_{T'}$ with $\sum w_n|G(x_n)|^2\ge(1-hT'/\pi)^2\|G\|^2$, $w_n\le h$ (Gröchenig,
  Math. Comp. 1992), hence unweighted $A\ge h^{-1}(1-hT'/\pi)^2/2\pi$ (normalised as in (A.1)). Localised version: the test decays off its cell;
  ARGUED. So (Frame) holds unconditionally for $T'\le c_1\log\log\gamma$ with $A\gg\log\log\gamma$, $B\ll\log\gamma\log\log\gamma$. Then (A.3) asks
  $\eta\lesssim(\log\gamma)^{-1/2}$ — but in this range $P_{\rm loc}$ is already unconditional (R163_602 §2.1, $T'\le\log\log\gamma-1.43$). **No new content.**
- (ii) Under a region $\eta(t)\le c/\log\log t$ (much weaker than (ZFR) at width $1/\log t$), Selberg's method for $S(t)$ goes through
  (the zeros enter weighted by $x^{\delta}$ with $x=(\log t)^{2-\epsilon}$, and $x^{\eta}=O(1)$), giving $S(t)\ll\log t/\log\log t$ and so
  $N(t+h)-N(t)=\frac h{2\pi}\log\frac t{2\pi}+O(\log t/\log\log t)$, positive for $h\ge C/\log\log t$ (Titchmarsh §14.13 under RH; transfer ARGUED).
  A quantitative Beurling-type sampling theorem then gives (Frame) only for $T'\le\frac12\Lambda\,(1-C/(h_0\log\log\gamma))$ with spectral
  localisation at scale $h_0$, i.e. **up to $\frac12\Lambda-C\Lambda/\log\log\gamma$, not up to $\frac12\Lambda-C'$**. The last stretch of the
  sub-Landau range needs discrepancy control $N(t+h)-N(t)-\frac h{2\pi}\Lambda=O(1)$ at mesoscopic scales, which is false pointwise even
  under RH ($S(t)=\Omega_\pm((\log t/\log\log t)^{1/2})$, Montgomery 1977 under RH) — although a frame does not need pointwise
  discrepancy, only absence of $T'$-deficient stretches of length $\gg1/T'$, which is OPEN.
- Consequence: **(⇐) in the sub-Landau range is OPEN even granting RH-strength zero-counting**; under RH it is of course true
  (all $\delta_\rho=0$, (0.2) is a sum of squares), but not via any frame.

## §3 Direction (⇒): an off-line zero beyond the region gives $\mathfrak a_{T'}<0$ sub-Landau

**Dominance hypothesis (Dom$_\kappa$) at $\rho_0=\frac12+\delta_0+i\gamma_0$.** Every other zero with $|\gamma_\rho-\gamma_0|\le R_0:=(\log\gamma_0)^{1/2}$ has
$\delta_\rho\le\delta_0-\kappa/T'$, with $\kappa:=\log\log\gamma_0+K$ ($K$ a large absolute constant).

**Theorem B (⇒). Core inequality PROVED; tail bookkeeping ARGUED.** Assume $P_{\rm loc}(\gamma,T')$ for all $\gamma\ge\gamma_1$ and all
$T'\le\frac12\log(\gamma/2\pi)-C'$. Then every zero $\rho_0$ with $\gamma_0\ge\gamma_2(C')$ satisfying (Dom$_\kappa$) has
$$
\beta_0-\tfrac12=\delta_0\ \le\ \frac{\log\log\gamma_0+\log\log\log\gamma_0+O(1)}{\log\gamma_0}. \tag{B.1}
$$
*Construction.* Put $T'=\frac12\Lambda_0-C'$, $\Lambda_0=\log(\gamma_0/2\pi)$; $\varepsilon=\theta T'$ with fixed small θ; $T''=T'-\varepsilon$.
Choose $\psi$ even, $\ge0$, in a Gevrey class $G^{s}$, $1<s<\frac{3}{2}$ (compact support, $|\widehat\psi(x+iy)|\le Ce^{\varepsilon|y|}\exp(-c|\varepsilon x|^{1/s})$;
Denjoy–Carleman, FROM MEMORY; this replaces the $C^\infty$ localiser of R163_601 only to make far tails summable). Take
$h(u)=\chi(u)\sinh(\delta_0u)$ with $\chi$ a $G^s$ cutoff equal to 1 on $[-T''+1,T''-1]$, supported in $[-T'',T'']$; $H(t)=e^{i\gamma_0t}ih(t)$
corrected by a rank-two term of norm $O(e^{-c\gamma_0^{1/s}})$ to make $\widehat H(\pm i/2)=0$ (possible since $|\widehat{h}(\pm i/2+\gamma_0)|$ is that small).
So $F=\psi_{\gamma_0}*H\in\mathrm{Loc}_{T'}(\gamma_0)$, $g=\psi*(ih)$ (up to the correction), $g$ is $i\times$(real odd), and $\widehat g$ is real on $\mathbb R$.

*Step 1 (the detecting term). PROVED.* For $g=ib$, $b$ real odd, L1 gives at $x=0$, $\delta=\delta_0$: $\widehat{g_c}(0)=i\int b\cosh\delta_0u=0$ (odd), and
$|\widehat{g_s}(0)|^2=(\int b\sinh\delta_0u)^2=:\mathcal B^2$. So the pair of $\rho_0$ contributes exactly $-2\mathcal B^2$. With $b=\psi*h$ and $\psi\ge0$,
$\int b\sinh\delta_0u=\int h\,(\psi*\sinh\delta_0\cdot)=\widehat\psi(-i\delta_0)_{\rm even}\int h\sinh\delta_0u$, and $\int\psi\cosh(\delta_0 v)dv\ge\int\psi$, so
$$
\mathcal B\ \ge\ c_\psi\,S_0,\qquad S_0:=\int_{-T''+1}^{T''-1}\sinh^2(\delta_0u)\,du=\frac{\sinh(2\delta_0(T''-1))}{2\delta_0}-(T''-1).
$$
(This is the light-cone node of R163_402 Cor 2 placed exactly at $\gamma_0$: $\widehat g$ is odd, so it vanishes at $x=0$.)

*Step 2 (on-line and near off-line mass). PROVED.* $\|g\|^2\le\|\widehat\psi\|^2_\infty\|h\|^2\le C S_0'$ with $S_0'=\int_{-T''}^{T''}\sinh^2\le C S_0$ (for $\delta_0T'\ge1$).
On-line zeros, and the cosh-parts of off-line zeros with $|\gamma_\rho-\gamma_0|\le R_0$ other than $\rho_0$: by L1 they contribute at most
$2\sum|\widehat{g_c}(x_\rho)|^2$. For on-line zeros $g_c=g$; L3 gives $\le 2\cdot2\pi C_0\log\gamma_0(1+2T')\|g\|^2\le C_1\Lambda_0^2S_0$.
For off-line ones, $|\cosh(\delta_\rho u)|\le e^{\delta_\rho|u|}$ and $|g(u)|\lesssim e^{\delta_0|u|}$, so by L3 applied to $w=g\cosh\delta_\rho u$ with the variable-δ
handled as in L2 (Taylor in $\delta_\rho$, $\delta_\rho\le\delta_0-\kappa/T'$): contribution $\le C_1\Lambda_0^2\,e^{2(\delta_0-\kappa/T')T'}e^{2\delta_0T'}/\delta_0\ \le\ C_2\Lambda_0^2e^{-2\kappa}\,S_0^2\,\delta_0$.
(The negative sinh-parts of other zeros only help.)

*Step 3 (far zeros). ARGUED (routine; constants not tracked).* Zeros with $|\gamma_\rho-\gamma_0|>R_0$ have $|\delta_\rho|\le\frac12$ and contribute
$\le\sum|\Phi(x-i\delta)|\le C e^{T'}\cdot\sum_\rho\exp(-2c(\varepsilon|x_\rho|)^{1/s})\cdot\|h\|_1^2$. With $\varepsilon\asymp\log\gamma_0$, $|x|\ge R_0=(\log\gamma_0)^{1/2}$:
$(\varepsilon|x|)^{1/s}\ge(\log\gamma_0)^{3/(2s)}\gg\log\gamma_0$ for $s<\frac32$, beating $e^{T'}\le\gamma_0^{1/2}$, $\|h\|_1^2\le e^{2T'}$ and $N(2\gamma_0)\ll\gamma_0\log\gamma_0$; mirror
ordinates and low zeros are at distance $\asymp\gamma_0$. So $\mathcal E_{\rm far}=O(\gamma_0^{-10})$. The rank-two primitivity correction changes the form by
$O(e^{-c\gamma_0^{1/s}}e^{T'})$, same order.

*Step 4 (conclusion).* By (0.2), $\mathfrak a_{T'}(F)\le-2c_\psi^2S_0^2+C_1\Lambda_0^2S_0+C_2\Lambda_0^2e^{-2\kappa}\delta_0S_0^2+O(\gamma_0^{-10})$. With $\kappa=\log\log\gamma_0+K$ and
$\delta_0\le\frac12$ the third term is $\le\frac12c_\psi^2S_0^2$ for $K$ large. Hence $\mathfrak a_{T'}(F)<0$ as soon as
$$
S_0\ >\ C_3\Lambda_0^2,\qquad\text{i.e.}\qquad \frac{e^{2\delta_0T''}}{4\delta_0}\gtrsim C_3\Lambda_0^2 .
$$
With $2T''=(1-\theta)\Lambda_0-2C'$… — *correction*: to get the sharp constant 1 in (B.1) take θ→0 slowly ($\varepsilon=\theta T'$ with $\theta=1/\log\log\gamma_0$;
Gevrey decay at $|x|\ge R_0$ then still beats $\gamma_0^{1/2}$ with $R_0=(\log\gamma_0)^{1/2}$ since $(\varepsilon R_0)^{1/s}\gg\log\gamma_0$ for $s<\frac32$ and θ only $1/\log\log$).
Then $2\delta_0T''=\delta_0\Lambda_0(1-O(1/\log\log\gamma_0))-O(\delta_0)$, and negativity holds once
$\delta_0\Lambda_0>\log(4C_3\delta_0\Lambda_0^2)+O(\delta_0\Lambda_0/\log\log\gamma_0)$. With $\delta_0\Lambda_0=y$: $y(1-O(1/\log\log))>\log y+\log\Lambda_0+O(1)$, i.e.
$y>\log\Lambda_0+\log\log\Lambda_0+O(1)$. This contradicts $P_{\rm loc}(\gamma_0,T')$, so (B.1). ∎(modulo Step 3)

**Remark B.1 (where $\log\log$ comes from, and what it would be with a lattice).** Replace L3's constant $C\Lambda_0(1+2T')\asymp\Lambda_0^2$ by
the lattice value $2\pi\rho=\Lambda_0$ (R163_402 Thm 4): Step 4 becomes $e^{2\delta_0T'}/(4\delta_0)>\Lambda_0/2$, i.e. $\delta_0\Lambda_0>y_0$ — the
erratum threshold $y_0=2.1773$. The extra $\log\Lambda_0=\log\log\gamma$ is *exactly* the loss $(1+2T')$ in L3. Any improvement of the upper
frame at cell scale (from $O(\log\gamma)$ points per cell of length $1/T'$ to $O(1)$) improves (B.1) to $O(1/\log\gamma)$.

**Remark B.2 (dominance is a genuine hypothesis). OPEN (O701.1).** If several zeros near $\gamma_0$ have $\delta$ within $\kappa/T'$ of the
maximum, their sinh-parts at the shifted ordinates $x_\rho\ne0$ carry phases $e^{2ix_\rho T''}$ (Step 1 computed at $x=0$ only), and their
cosh-parts are not small: $\widehat{g_c}(x_\rho)\ne0$ for $x_\rho\ne0$. Cancellation within such a cluster is not excluded by anything above.
The classical tool is Turán's power-sum method (one-sided theorems of Knapowski–Turán, varying $T''$ in an interval), but its loss
$(cn)^{-n}$ with $n$ up to $\asymp\log\gamma$ ordinates per cell (S(t) = O(log t) again) is $\gamma^{-c}$, which swamps the gain $e^{2\delta_0T'}$ unless
$\delta_0\gg1$. So: **sub-Landau $P_{\rm loc}$ ⇒ zero-free region (B.1) for dominant zeros, PROVED-modulo-Step-3; for all zeros, OPEN.**
Note the logical form: the set of non-dominant off-line zeros above the region is a set where off-line zeros come in tight
$\delta$-clusters; a falsifier with such clusters (e.g. $M_m$ with repeated $\delta$) would have to be checked separately.

**Remark B.3 (falsifier sanity).** Theorem B uses only (0.1), the functional-equation pairing, $N(t+1)-N(t)\ll\log t$ and Gevrey
localisers. It holds verbatim for DH (zeros counted by its own $N$; $\Lambda$ replaced by $\log(5\gamma/2\pi)$): sub-Landau
$P^{\rm DH}_{\rm loc}$ fails at its dominant off-line zeros of fixed $\delta>0$, consistent with R163_601 §5. Theorem B is a
*detector*, class-level, and not a source of the sign. As it must be.

## §4 Comparison with known zero-free regions, and what sub-Landau $P_{\rm loc}$ would mean

**Corollary C (honest equivalence). PROVED modulo (Frame) for ⇐ and (Dom) for ⇒.** Suppose the ordinates near height γ satisfy a
lattice-strength frame at window $T'\le\frac12\Lambda-C'$: $A\ge a\Lambda$, $B\le b\Lambda$. Then for that γ-range:
- (ZFR) with $\eta\le c_-(a,b)/\Lambda$ ⇒ sub-Landau $P_{\rm loc}$ (Thm A with (A.3));
- sub-Landau $P_{\rm loc}$ ⇒ every dominant zero has $\delta\le c_+(b)/\Lambda$ (Thm B with $B\le b\Lambda$ in Step 2; Remark B.1).
So "sub-Landau $P_{\rm loc}$ ⟺ zero-free strip of width $\asymp1/\log\gamma$" **up to constants**, under a frame hypothesis. Without it,
what is unconditional is the one-sided (⇒) with width $(1+o(1))\log\log\gamma/\log\gamma$ (dominant zeros), and (⇐) is open.

**Known regions (PROVED-CITED, FROM MEMORY).**
- de la Vallée Poussin (1899): $\beta<1-c/\log\gamma$.
- Vinogradov–Korobov (1958): $\beta<1-c(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$; best constants Ford (2002).
- Both are regions **near β = 1**: their distance from the critical line is $\frac12-o(1)$. No region of the form $\beta<1-\epsilon$ for a fixed
  $\epsilon>0$ is known (that is the quasi-Riemann hypothesis). The region (B.1) sits at distance $O(\log\log\gamma/\log\gamma)$ *from ½*: it is
  of a different nature altogether, far beyond quasi-RH.
- The mechanism of dlVP/VK is the 3-4-1 positivity of Λ (R163_602 (b′)), i.e. lower bounds for prime sums, which is the *detection*
  side; it is structurally the same direction as Theorem B (a detector), never the direction of Theorem A.

**What sub-Landau $P_{\rm loc}$ would mean (ARGUED, standard explicit-formula consequences).** If all zeros (not only dominant ones; i.e.
granting O701.1) satisfy $\beta\le\frac12+K\log\log\gamma/\log\gamma$:
- $\psi(x)=x+O(\sqrt x\,(\log x)^{2+K})$: from the truncated explicit formula at height $x$, $x^{\beta}\le x^{1/2}\exp(K\log x\cdot\log\log x/\log x)=x^{1/2}(\log x)^K$.
  RH-strength up to a power of log.
- Lindelöf and $S(t)\ll\log t/\log\log t$, $\log\zeta(\frac12+it)\ll\log t/\log\log t$: Littlewood/Selberg arguments need only $\eta\le c/\log\log t$ (Thm A′(ii)).
- Density hypothesis $N(\sigma,T)\ll T^{2(1-\sigma)+\epsilon}$ trivially (no zeros for $\sigma>\frac12+o(1)$ at all).
- It would **not** be RH, and would not by itself close row D: the supra-Landau range (where R163_601 Prop 4 places the
  doubly-exponential collapse) and the strip of width $\log\log\gamma/\log\gamma$ remain. By Thm A the strip could only be closed from
  $P_{\rm loc}$ together with a frame, at width $1/\log\gamma$; and by R163_602 §2.2 the twisted-sum input for sub-Landau $P_{\rm loc}$
  is square-root cancellation at length up to $\gamma$, which no unconditional method approaches.

**Placement in the three regimes (R163_601 §3(2c)).**
| regime | $P_{\rm loc}$ status | zero-free content |
|---|---|---|
| trivial $T'\le\log\log\gamma-1.43$ | PROVED (R163_602 §2.1) | none (Thm A′(i): frame is unconditional here, region content empty) |
| sub-Landau $T'\le\frac12\Lambda-C'$ | OPEN | ⇒ region (B.1) for dominant zeros (Thm B); ⇐ needs region $1/\log\gamma$ + frame (Thm A) |
| supra-Landau | OPEN | ⟺ RH by R163_601 Cor 2 (family); local zero sum (W12) |

## §5 Ledger

| step | label |
|---|---|
| (0.1)–(0.2) zero side with pairing | PROVED (R163_601 §4.1 + functional equation) |
| L1 pair identity | PROVED |
| L2 Taylor–Minkowski | PROVED |
| L3 upper sampling via $N(t+1)-N(t)\ll\log t$ | PROVED (count PROVED-CITED, Titchmarsh 9.2, FROM MEMORY) |
| Thm A (⇐) conditional on ZFR + Frame; (A.3) | PROVED |
| Thm A′ frame status (Littlewood gaps, Gröchenig, Selberg S(t) transfer) | ARGUED; citations FROM MEMORY |
| Thm B (⇒) Steps 1, 2, 4 | PROVED |
| Thm B Step 3 (Gevrey tails, primitivity correction), sharp constant 1 via θ = 1/log log | ARGUED (routine; constants untracked) |
| Remark B.1 origin of log log = L3 loss | PROVED (bookkeeping) |
| O701.1 removal of (Dom) | **OPEN** |
| Cor C equivalence at width $1/\log\gamma$ under a lattice-strength frame | PROVED modulo Frame, Dom |
| task's conjecture "⟺ region $\frac12+c\log\log/\log$ up to constants" | **not established; (⇐) at that width fails in the lattice picture** (ARGUED for ζ, PROVED in the model) |
| §4 consequences, comparison dlVP/VK | ARGUED / PROVED-CITED FROM MEMORY |
| sub-Landau $P_{\rm loc}$ for ζ | **OPEN** |
| Row D | **OPEN** |

**Open items.** (O701.1) Dominance: detect a $\delta$-cluster of off-line zeros sub-Landau without Turán-type losses. (O701.2) A local
lower frame for $PW_{T'}$ at the zero ordinates, $T'\le\frac12\Lambda-C'$, under any hypothesis weaker than RH (it is not implied by
$S(t)\ll\log t/\log\log t$ via max-gap or block-count arguments, Thm A′(ii)). (O701.3) Improve L3 at cell scale (upper frame $O(\Lambda)$
instead of $O(\Lambda^2)$): this alone would sharpen (B.1) to $O(1/\log\gamma)$; it is a statement about clustering of ordinates in
intervals of length $1/\log\gamma$, implied on average by pair correlation but not known pointwise.
