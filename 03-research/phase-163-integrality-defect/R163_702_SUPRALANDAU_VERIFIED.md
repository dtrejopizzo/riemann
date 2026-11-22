# R163_702 — Supra-Landau cells and the verified height: what verification gives, and what it cannot give

* Pure mathematics; no numerics run. Nothing outside this file was edited. No label of record moves.*
*Inputs: R163_601 (§1 definitions, Thm 1, Cor 2, Prop 4, Prop 5, §4.1), R163_401 (status, boxed gap, (1.1), Lemma 3.0,
Lemma 3.2), R163_402 (Thm 4, Landau ceiling).*
*Corpus check (rule ).* Verification height already enters the record in R163_401 §4.2 / R163_502 (Δ, as a
bound on where a quartet can sit). This memo adds the effect of verification on $P_{\rm loc}$.

**Labels.** PROVED (proof here); PROVED-CITED (reference; FROM MEMORY when flagged); ARGUED; HEURISTIC; OPEN.

## Outcome first

| # | statement | label |
|---|---|---|
| V | verification input $\mathrm V(H)$, $H=3\cdot10^{12}$ (Platt–Trudgian) | PROVED-CITED (FROM MEMORY, flagged) |
| Thm A | **margin form**: under $\mathrm V(H)$, for $F=\psi_\gamma*H_0\in\mathrm{Loc}_{T'}(\gamma)$, $\gamma\le H-\Delta$: $\mathfrak a_{T'}(F)\ge\sum_{\lvert\gamma_\rho\rvert\le H}\lvert\widehat F(\gamma_\rho)\rvert^2-E_H(\gamma,T')\lVert H_0\rVert^2$, explicit $E_H$ | PROVED (counting input PROVED-CITED) |
| Cor A | $P_{\rm loc}(\gamma,T')$ holds on the verified-sampling cone $\{\sum_{\rm verified}\ge E_H\lVert H_0\rVert^2\}$ | PROVED |
| Thm B | **obstruction**: for every $\gamma$, $T'>\varepsilon$, $H$, the subspace $K_H\subset\mathrm{Loc}_{T'}(\gamma)$ where $\widehat F$ vanishes at all verified ordinates is of finite codimension (so infinite-dimensional), and on $K_H$ the form **equals the tail** $\sum_{\lvert\gamma_\rho\rvert>H}$. Hence $\mathrm V(H)$ reduces $P_{\rm loc}(\gamma,T')$ only to $P_{\rm loc}$ on $K_H$, i.e. to the unverified zeros. Task item (1) as stated (exact $P_{\rm loc}$ from $\mathrm V(H)$ + tail decay) is **impossible** | PROVED |
| Rem B′ | non-locality of $\mathrm{Loc}$: its normalised elements may carry their mass at any height | PROVED (inclusion); consequence ARGUED |
| Thm C | the conditional theorem of task item (2) cannot be obtained from Thm 1 + $\mathrm V(H)$: at $T\approx T_1(H)$ **every** verified cell is supra-Landau and needs exact $P_{\rm loc}$ there; what Thm 1 does give is the split statement Thm C′ | PROVED (bookkeeping + Thm B) |
| Thm C′ | $\mathrm V(H)$ ∧ [sub-Landau $P_{\rm loc}$ above $H-\Delta$] ∧ [$P_{\rm loc}$ on $K_H$-parts of verified cells] ⇒ $D_T$ for $T\le T_1(H)$; $T_1(H)=\tfrac12\log\tfrac{H}{2\pi}-C-\varepsilon$, $\approx13.45-C-\varepsilon$ at $H=3\cdot10^{12}$ | PROVED (conditional) |
| §3 | upward induction in $T$ is impossible without arithmetic ($M_m$); monotonicity runs downward; raising $H$ moves $T_1$ by $\tfrac12\log$ only and does not touch Thm B | PROVED / ARGUED as marked |
| $P_{\rm loc}$ at supra-Landau verified cells | | **OPEN** (not reducible to verification) |
| Row D | | **OPEN** |

**One-line verdict.** Verification to height $H$ controls the *verified* zero terms but not the cells: because
$\mathrm{Loc}_{T'}(\gamma)$ is infinite-dimensional and $P_{\rm loc}$ is non-strict, one can always annihilate all
$\sim10^{13}$ verified terms by finitely many linear conditions, after which $\mathfrak a_{T'}$ *is* the unverified
tail. So verification gives $P_{\rm loc}$ with an explicit, polynomially small (in $\Delta$) error relative to the verified
sum (Thm A), never exact $P_{\rm loc}$ (Thm B). The requested reduction "sub-Landau above $H$ ⇒ $D_T$, $T\le T_1(H)$" fails
exactly at the supra-Landau verified cells, which at $T\approx T_1(H)$ are all of them.

---

## §0 Input

**(V) Verification. PROVED-CITED (FROM MEMORY, flagged).** D. Platt, T. Trudgian, *The Riemann hypothesis is true up to
$3\cdot10^{12}$*, Bull. London Math. Soc. **53** (2021), 792–797: every zero $\rho=\beta+i\gamma$ of $\zeta$ with
$0<\gamma\le3\cdot10^{12}$ has $\beta=\tfrac12$ (and is simple). By $\rho\mapsto\bar\rho$ the same holds for
$\lvert\gamma\rvert\le H:=3\cdot10^{12}$. Write $\mathrm V(H)$ for this statement for a general $H$.

**(N) Zero counting. PROVED-CITED (FROM MEMORY, flagged).** For $t\ge e$,
$\lvert N(t)-\tfrac{t}{2\pi}\log\tfrac{t}{2\pi e}-\tfrac78\rvert\le R(t):=0.11\log t+0.29\log\log t+2.29$
(Platt–Trudgian, *An improved explicit bound on $\lvert\zeta(\tfrac12+it)\rvert$*-companion paper on $S(T)$, 2021;
Trudgian 2014 has $0.112,0.278,2.51$, which also suffices). Only the consequence used is:
$N(t+1)-N(t)\le\tfrac1{2\pi}\log t+2R(t+1)\le\log t$ for $t\ge10^3$.
Also needed: $\delta_\rho:=\beta-\tfrac12\in(-\tfrac12,\tfrac12)$ (classical zero-free line $\beta<1$).

Notation of R163_601 §1: $F=\psi_\gamma*H_0$, $H_0\in\mathcal P_{T_0}\cap\mathcal D_{T_0}$, $T_0=T'-\varepsilon$,
$\widehat F(z)=\widehat\psi(z-\gamma)\widehat H_0(z)$, $\mathfrak a_{T'}(F)=\sum_\rho(\widehat F\widehat F^\#)(t_\rho)$ by R163_401 (1.1)
(PROVED-CITED there, absolute convergence Lemma 3.0). The localiser $\psi\in C_c^\infty(-\varepsilon,\varepsilon)$, and for
$N\ge1$, $c_N(\psi):=\lVert\psi^{(N)}\rVert_{L^1}$.

## §1 Verified cells (task item 1)

**Lemma 1 (pointwise bounds). PROVED.** For $\lvert y\rvert\le\tfrac12$:
(a) $\lvert\widehat H_0(x+iy)\rvert\le\sqrt{2T_0}\,e^{T_0\lvert y\rvert}\lVert H_0\rVert$;
(b) $\lvert\widehat\psi(x+iy)\rvert\le e^{\varepsilon\lvert y\rvert}c_N(\psi)\lvert x\rvert^{-N}$ ($x\ne0$).
*Proof.* (a) Cauchy–Schwarz on $\int_{-T_0}^{T_0}H_0(t)e^{ixt}e^{-yt}dt$, with $\int e^{-2yt}\le2T_0e^{2T_0\lvert y\rvert}$.
(b) $N$ integrations by parts in $\int\psi(t)e^{i(x+iy)t}dt$; $\lvert e^{-yt}\rvert\le e^{\varepsilon\lvert y\rvert}$ on $\mathrm{supp}\,\psi$. ∎

**Theorem A (margin form). PROVED** (given (V), (N)). Assume $\mathrm V(H)$, $H\ge10^3$, $0\le\gamma\le H-\Delta$,
$1\le\Delta\le H$, $N\ge1$. Then for every $F=\psi_\gamma*H_0\in\mathrm{Loc}_{T'}(\gamma)$,
$$
\mathfrak a_{T'}(F)\ \ge\ \sum_{\lvert\gamma_\rho\rvert\le H}\lvert\widehat F(\gamma_\rho)\rvert^2\;-\;E_H(\gamma,T')\,\lVert H_0\rVert^2,\qquad
E_H\le 8\,T_0\,e^{T_0+\varepsilon}\,c_N(\psi)^2\,\log H\;\Big(\frac{2\Delta^{1-2N}}{2N-1}+\Delta^{-2N}\Big).
$$
*Proof.* Split (1.1) into $\lvert\gamma_\rho\rvert\le H$ and $>H$. Below $H$, $t_\rho=\gamma_\rho$ is real and
$(\widehat F\widehat F^\#)(\gamma_\rho)=\lvert\widehat F(\gamma_\rho)\rvert^2$ (V). Above $H$, each term is bounded by
$\lvert\widehat F(t_\rho)\rvert\lvert\widehat F(\bar t_\rho)\rvert$; by Lemma 1 with $\lvert\delta_\rho\rvert<\tfrac12$,
$\lvert\widehat F(t_\rho)\rvert\lvert\widehat F(\bar t_\rho)\rvert\le 2T_0e^{T_0}e^{\varepsilon}c_N^2\lvert\gamma_\rho-\gamma\rvert^{-2N}\lVert H_0\rVert^2$.
For $\gamma_\rho>H$: $\gamma_\rho-\gamma\ge\gamma_\rho-H+\Delta$. Group zeros in unit intervals $[H+j,H+j+1)$, $j\ge0$,
each holding $\le\log(H+j+1)\le\log H+\log(j+2)$ zeros by (N); then
$\sum_{\gamma_\rho>H}(\gamma_\rho-\gamma)^{-2N}\le\sum_{j\ge0}(\log H+\log(j+2))(\Delta+j)^{-2N}
\le2\log H\big(\Delta^{-2N}+\int_\Delta^\infty u^{-2N}du\big)$ for $\Delta\le H$, $N\ge1$ (the $\log(j+2)$ term is absorbed since
$\log(j+2)\le\log H$ for $j\le H$, and the range $j>H$ contributes $O(H^{-2N+2})$, absorbed by the factor 2 for $H\ge10^3$).
Zeros with $\gamma_\rho<-H$ are at distance $\ge H+\gamma\ge\Delta$ and give at most the same bound. Total factor
$2\cdot2T_0e^{T_0+\varepsilon}c_N^2\cdot2\log H(\Delta^{-2N}+\Delta^{1-2N}/(2N-1))$. ∎

**Explicit Δ.** Given a tolerance $\eta>0$, with $N=2$:
$\Delta(T',\eta)=\big(32\,T_0e^{T_0+\varepsilon}c_2(\psi)^2\log H/\eta\big)^{1/3}$ suffices ($\Delta\ge1$). With the per-window
scaling $\varepsilon=\theta T'$ one has $c_2(\psi)^2\asymp\varepsilon^{-5}$ for $\psi=\varepsilon^{-1/2}\psi_1(\cdot/\varepsilon)\sqrt{L/2\pi}$, so
$\Delta\asymp(e^{T'}\log H/(\eta\,T'^{4}))^{1/3}$: for every $T'\le13.5$ and $\eta\ge10^{-6}$, $\Delta\le10^{4}$, negligible against $H$.

**Corollary A (verified-sampling cone). PROVED.** Under $\mathrm V(H)$, $P_{\rm loc}(\gamma,T')$ holds for every
$F\in\mathrm{Loc}_{T'}(\gamma)$, $\gamma\le H-\Delta$, with $\sum_{\lvert\gamma_\rho\rvert\le H}\lvert\widehat F(\gamma_\rho)\rvert^2\ge E_H\lVert H_0\rVert^2$. ∎
*Reading.* In a sub-Landau verified cell a sampling inequality for the verified ordinates (a frame bound at density
$\rho>T'/\pi$, which needs gap data of the verified zeros — not cited here) would put most of the concentrated cone in
this set; in a supra-Landau cell there is no such inequality (R163_601 §3(2c)). Even the sub-Landau case leaves the
non-concentrated part (R163_601 Prop 5 gap, relative to $\lVert H_0\rVert$).

**Theorem B (verification cannot give exact $P_{\rm loc}$). PROVED.** Fix $\gamma$, $T'>\varepsilon$, $H$ and assume $\mathrm V(H)$.
Let $Z_H=\{\gamma_\rho:\lvert\gamma_\rho\rvert\le H\}$ (finite, $\#Z_H=2N(H)$) and
$K_H:=\{F\in\mathrm{Loc}_{T'}(\gamma):\widehat F(x)=0\ \forall x\in Z_H\}$ (with multiplicity, if any). Then
(i) $K_H$ has codimension $\le2N(H)$ in $\mathrm{Loc}_{T'}(\gamma)$, hence is infinite-dimensional;
(ii) for $F\in K_H$, $\mathfrak a_{T'}(F)=\sum_{\lvert\gamma_\rho\rvert>H}(\widehat F\widehat F^\#)(t_\rho)$;
(iii) $P_{\rm loc}(\gamma,T')\iff[\mathfrak a_{T'}\ge0$ on $K_H]$ ∧ [the verified-sum-dominates statement on a complement],
and the first conjunct involves no verified zero at all.
*Proof.* (i) $K_H$ is the kernel of the linear map $F\mapsto(\widehat F(x))_{x\in Z_H}$ into $\mathbb C^{2N(H)}$ (continuous on
$\mathrm{Loc}$, Lemma 1(a)); $\mathrm{Loc}$ is infinite-dimensional (R163_601 §1). (ii) (1.1) with the verified terms
$\lvert\widehat F(\gamma_\rho)\rvert^2=0$. (iii) restriction plus (ii). ∎
*Consequence.* No argument of the form "verified part $\ge$ (tail bound)" proves exact $P_{\rm loc}$: on $K_H$ the verified
part is $0$ and the tail is, in general, a non-zero quantity whose sign is the unverified RH content. Concentration of
$\widehat\psi$ makes $\lvert$tail$\rvert\le E_H\lVert H_0\rVert^2$ but not zero ($\widehat\psi\not\equiv0$ is entire, so its zero set is discrete and
it does not kill the tail; $\widehat H_0$ is free modulo finitely many conditions).
Task item (1) is therefore answered in the margin form (Thm A); the exact form is **not** a consequence of $\mathrm V(H)$
plus decay plus counting. This is the cell-level form of the obvious global fact that $\mathrm V(H)$ does not imply
$D_T$ by tail estimates (an $M_m$ model with an extra quartet above $H$ satisfies all inputs of Thm A; §3).

**Remark B′ (Loc is not local in normalised form). PROVED (inclusion); ARGUED (consequence).** For $T'>2\varepsilon$,
$\psi_{\gamma'}*K\in\mathcal P_{T'-\varepsilon}$ for $K\in\mathcal P_{T'-2\varepsilon}$, so
$\mathrm{Loc}_{T'}(\gamma)\supset\{\widehat\psi(\cdot-\gamma)\widehat\psi(\cdot-\gamma')\widehat K\}$ for every $\gamma'$. After normalisation these tests
carry their mass near $\gamma'$, with weight $\lvert\widehat\psi(\cdot-\gamma)\rvert^2$ slowly varying at cell scale when
$\widehat\psi$ is of Gevrey type (ARGUED). Hence $P_{\rm loc}(\gamma,T')$ at a verified height $\gamma$ already contains
positivity of near-localised tests at *unverified* heights $\gamma'>H$: the cell's "height" is a weighting, not a
support. This is the structural reason for Thm B.

## §2 Combination with Theorem 1 (task item 2)

**Bookkeeping. PROVED.** Cell at $\gamma=kL$, window $T'=T+\varepsilon$: sub-Landau iff $T'\le\tfrac12\log\tfrac{\gamma}{2\pi}-C$,
supra-Landau iff $\gamma<2\pi e^{2T'+2C}$. All cells with $\lvert kL\rvert>H-\Delta$ are sub-Landau iff
$$T\le T_1(H):=\tfrac12\log\tfrac{H-\Delta}{2\pi}-C-\varepsilon .$$
At $H=3\cdot10^{12}$: $\log(H/2\pi)=\log(4.775\cdot10^{11})=26.89$, so $T_1\approx13.45-C-\varepsilon$ ($\Delta$ negligible).
At $T=T_1(H)$ the supra-Landau region is $\lvert\gamma\rvert<2\pi e^{2T_1+2\varepsilon+2C}=H-\Delta$: **every verified cell is
supra-Landau**. For $T<T_1$, the verified cells split into supra-Landau ($\lvert\gamma\rvert<2\pi e^{2T+2\varepsilon+2C}$) and
sub-Landau verified ones.

**Theorem C (the requested reduction fails as stated). PROVED.** The implication
"[sub-Landau $P_{\rm loc}$ at all cells $\lvert\gamma\rvert>H$] ⇒ $D_T$ for all $T\le T_1(H)$" cannot be derived from
Thm 1 / Cor 2 together with $\mathrm V(H)$, Lemma 1 and (N).
*Proof.* Cor 2 requires $P_{\rm loc}(kL,T+\varepsilon)$ at *every* $k$; for $\lvert kL\rvert\le H-\Delta$ the available inputs give
only Thm A, and by Thm B the instances on $K_H$ are not touched by them; for $T>\tfrac12\log5$ these instances are
not covered by any certified range (R163_601 Prop 5(i)). Since Thm 1(c) is an identity, a deficit in a single cell
cannot be compensated by the hypothesis on other cells unless positivity of the sum is proved — which is $D_T$ itself. ∎

**Theorem C′ (what Thm 1 does give: the honest conditional). PROVED.** Assume $\mathrm V(H)$ and fix $(\varepsilon,L,\psi)$
with $\varepsilon L<\pi$. Let $T\le T_1(H)$. If
- (S) $P_{\rm loc}(kL,T+\varepsilon)$ for all $\lvert kL\rvert>H-\Delta$ (sub-Landau cells above the verified height), and
- (K) $\mathfrak a_{T+\varepsilon}\ge0$ on $\mathrm{Loc}_{T+\varepsilon}(kL)$ for $\lvert kL\rvert\le H-\Delta$ — equivalently (Thm B(iii), Cor A) on the part of
  each verified cell where the verified sum is $<E_H\lVert H_0\rVert^2$,

then $D_T$. *Proof.* Cor 2, with Cor A covering the remaining part of (K)'s cells. ∎
(K) for supra-Landau verified cells is, by Thm B(ii), a statement about the unverified zeros only. Thus the gap
**does not move to heights $>H$ in the sub-Landau sense**: it stays at supra-Landau cells, now phrased on $K_H$.

**Corollary C″ (an implication that does hold, trivially). PROVED.** $\mathrm V(H)$ ∧ [all zeros with $\lvert\gamma\rvert>H$ on the
line] ⇒ D. (Tail terms are then $\lvert\widehat F(\gamma_\rho)\rvert^2\ge0$.) Any weaker hypothesis on heights $>H$ that is to imply
$D_T$ must control the signs of the tail on $K_H$; sub-Landau $P_{\rm loc}$ above $H$ does not, because small-δ quartets are
seen only beyond the Landau ceiling (R163_402 §2, HEURISTIC; Thm 4 exact in the lattice model).

## §3 What remains for $T>T_1(H)$, and can it be pushed? (task item 3)

1. **The gap is not at $T>T_1(H)$; it is at supra-Landau cells for every $T>\tfrac12\log5$.** By §2 the obstruction (Thm B)
   is already present at $T\le T_1(H)$. For $T>T_1(H)$ there are additionally supra-Landau cells *above* $H$, where
   neither verification nor sub-Landau arithmetic applies. PROVED (bookkeeping).
2. **More verification (numerics).** Raising $H$ to $H'$ moves $T_1$ by $\tfrac12\log(H'/H)$; e.g. $H'=10^{20}$ gives
   $T_1\approx22.6-C-\varepsilon$. It does not touch Thm B, which holds for every finite $H$. So numerics cannot close any
   window beyond the certified range in the exact sense; they only shrink the error $E_H$ in Thm A (polynomially in
   $\Delta$). PROVED.
3. **Monotone/induction in $T$.** $\lambda^{\rm A}_T$ is non-increasing in $T$ (nested $\mathcal P_T$; Paper 46, record), and
   Cor 2 runs downward ($D_{T+\varepsilon}\Rightarrow P_{\rm loc}\Rightarrow D_T$). An upward step "$D_T\Rightarrow D_{T+\varepsilon}$" or
   "$D_T\Rightarrow P_{\rm loc}(\cdot,T+2\varepsilon)$" valid for every $T$ would prove D from $D_{\frac12\log5}$; any such step using
   only the multiplier structure, (1.1), $\mathrm V(H)$-type data and zero counting also applies to $M_m$ (ζ plus an off-line
   quartet above $H$: same verified zeros, same counting up to $O(1)$, Thm 1 verbatim, R163_601 §5), which has $D_T$ for
   $T<T_c(M_m)$ and fails it after (record). So the step is false at $T_c(M_m)$ for $M_m$: it must use the atomic prime side
   of ζ (S4/T2). PROVED (modulo record: $M_m$ first contact). By Prop 4 of R163_601 the step also cannot carry uniform
   slack (code M). PROVED-CITED (Theorem M(b), record).
4. **Margin bootstrapping.** Thm A would give exact positivity on a verified cell if the cell bottom (over the
   non-$K_H$ part) exceeded $E_H$. But Thm B shows $K_H$ is always present, and on it there is no verified mass to
   compare with; under RH its bottom is $\inf_{K_H}\sum_{\lvert\gamma_\rho\rvert>H}\lvert\widehat F(\gamma_\rho)\rvert^2/\lVert F\rVert^2$, which is not
   bounded below by any verified quantity. ARGUED.
5. **What a genuine push needs.** A statement on $K_H$ (tests silent at all verified ordinates) that forces the tail
   sign — via the prime side of R163_601 §4.1 at height $\gamma$ with length $e^{2T'}\ge\gamma$, i.e. pair-correlation
   $\alpha>1$ — which is the boxed gap of R163_401 in its supra-Landau form. OPEN.

## §4 Ledger

| step | label |
|---|---|
| (V) Platt–Trudgian $3\cdot10^{12}$; (N) explicit $N(T)$ | PROVED-CITED (FROM MEMORY, flagged) |
| Lemma 1 pointwise bounds | PROVED |
| Thm A margin form, explicit $E_H$, explicit Δ | PROVED (given V, N) |
| Cor A verified-sampling cone | PROVED |
| Thm B finite-codim silent subspace; form = tail on it; exact $P_{\rm loc}$ not derivable from V+decay+counting | PROVED |
| Rem B′ non-locality of Loc | PROVED (inclusion); ARGUED (reading) |
| §2 bookkeeping, $T_1(H)=\frac12\log\frac{H-\Delta}{2\pi}-C-\varepsilon\approx13.45-C-\varepsilon$ | PROVED |
| Thm C requested reduction not derivable; Thm C′ honest conditional; Cor C″ | PROVED |
| §3.2 numerics move $T_1$ only logarithmically, never remove Thm B | PROVED |
| §3.3 upward induction killed by $M_m$; no uniform slack | PROVED (record: $M_m$ contact; Theorem M(b)) |
| §3.4 margin bootstrapping | ARGUED |
| $P_{\rm loc}$ at supra-Landau cells (verified or not), i.e. on $K_H$ | **OPEN** |
| Row D | **OPEN** |
