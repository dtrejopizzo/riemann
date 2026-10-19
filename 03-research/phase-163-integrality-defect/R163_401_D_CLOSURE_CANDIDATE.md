# R163_401 — Candidate closure of row D through the light cone of a real-rooted first contact

* Candidate closure proposal for review. Pure mathematics; no numerics were run for this memo. Nothing
outside this file was edited. No label of record moves.*

*Revision v3: fixes D1–D11 of R163_590 applied; v2 backed up as R163_401_v2.md. Errata added to R163_490 §1/§3 and R163_402 (D1); R163_501 citation and FC(iii) row corrected (D2, D10).*

*Revision v5: §4.11 added (negative results R163_801, R163_802, R163_901, R163_601/701/702); boxed gap and status table extended accordingly; v4 backed up as R163_401_v4.md. No label of the proved chain moves.*

*Revision v6: audit R163_991 of R163_901 integrated into §4.11(c), the boxed gap, the status table, §6 and the ledger: the $(\star_{\rm cell})$ clause stands given witness existence (ARGUED); the (A-loc) clause is ARGUED only (balance of $f_t$ OPEN); "Hamburger is the only separator" withdrawn in favour of a list of candidate separators; $f_t$ added to the §6 falsifier table. v5 backed up as R163_401_v5.md. No label of the proved chain moves.*

*Revision v7 (editor of phase 164, line L3): on-line abundance and Riemann–Siegel structure removed as candidate separators in the boxed gap, §4.11(c) and the §4.11 summary (on-line abundance: Bombieri–Hejhal, R163_602 F2; Riemann–Siegel/AFE: functional-equation-only, shared by $f_\chi$, R163_603 L2.1, R163_1001); §4.11(e) added for R163_1001 (Thm O, $f_\chi$, W3′); tail formulation (TC) referred to R164_000. v6 backed up as R163_401_v6.md. No label of the proved chain moves.*

*Revision v9 (editor of phase 164, rounds 3–4): §4.11(f) extended with Thm SA, Prop 4, the drop-term principle and "spectral invariants are window data" (labels from R164_190 rounds 3–4); v8 backed up as R163_401_v8.md. No label of the proved chain moves; $(\star_{\rm cell})$ stays OPEN.*

*Revision v10 (editor of phase 165): §4.11(g) added (Det+ and the $T_c$ bracket, Det− negative, exact phase identity with sign variable $\omega(E)$, interlacing refuted, real-rootedness at every simple $T$; labels from R165_190); status-table row §4.11(g). v9 backed up as R163_401_v9.md. No label of the proved chain moves; $(\star_{\rm cell})$ stays OPEN.*

*Revision v12 (editor of phases 166–167): §4.11(i) added (families P/Q survey; Thm A (iii) ⟹ (ii); θ = 0 tools; circularity theorem and (N′); exact target (WS\*) and its status: unreachable by sieves, scale-uniform ⟺ zero-free, single-scale = explicit formula; labels from R166_190, R167_190); status-table row §4.11(i). v11 backed up as R163_401_v11.md. No label of the proved chain moves; $(\star_{\rm cell})$ stays OPEN.*
*Revision v11 (editor of phase 166): §4.11(h) added (jet hierarchy theorem: $\mathrm{Re}\,G(t_q)^2$ is the jet $k=-1$; rough-zeta split of the tail; five new mechanisms DEAD; requirements (i)–(iii) for any proof of $(\star_{\rm cell})$; labels from R166_190); status-table row §4.11(h). v10 backed up as R163_401_v10.md. No label of the proved chain moves; $(\star_{\rm cell})$ stays OPEN.*

*Revision v8 (editor of phase 164, round 2): §4.11(f) added (R164_101 (KZ) = E1; positive tail DEAD; Thm R of R164_401; identification theorem of R164_190); the boxed gap's "Candidate separators" line replaced by the identification statement; status table and summary updated. v7 backed up as R163_401_v7.md. No label of the proved chain moves; $(\star_{\rm cell})$ stays OPEN.*

**Labels.** Every statement carries one of four labels.
- **PROVED**: the proof is given here, in full.
- **PROVED-CITED**: a reference is given. A *record* reference is a project file or paper whose proof was not re-audited
  here; this is said each time.
- **ARGUED**: part of the closing attempt. The argument is given in full, and the inequality it rests on is named.
- **HEURISTIC**: a plausibility statement with no proof; never load-bearing.

## Status table (final, after R163_490, R163_501, R163_502, R163_590)

| # | statement | final label |
|---|---|---|
| Thm 1.2 | D ⟺ RH (Weil criterion) | PROVED-CITED (⇒: Paper 45 Thms 11.3, 8.4; ⇐: Thm 1.3 + Lemma 3.0; Bombieri) |
| Thm 1.3 | zero-side identity (1.1) | PROVED-CITED (Paper 47 `lem:roughEF`) + Lemma 3.0 |
| 2.1 | positivity for $T\le\frac12\log5$ | PROVED-CITED (Paper 47, certified) |
| 2.2 | monotonicity, continuity, attainment | PROVED-CITED (Paper 47; Bombieri) |
| 2.3 | first contact $T_c>0.8047$ under ¬RH | PROVED |
| 2.4(i)–(iii) | full support, real-rooted witness, Gauss nodes $w_x=d_x/\lvert\widehat F'\rvert^2$ (simple nodes; block version 2.4(iii′) for multiple nodes), Q0 | PROVED (R163_501, R(d) after repair; R163_502 Q0; 2.4(iii′) here) |
| 2.4(iv) | node identity | PROVED-CITED (R162_2202, record) |
| (Q) | density of node span in $\mathcal D$ | OPEN (RH-neutral; unused) |
| 2.5 | Type I/II split | PROVED-CITED (R162_1701); unused |
| Rem 2.5a | FC(iii) full support at $T_*$ | UNPROVED as stated (fails if $\lambda^{\rm A}$ vanishes on an interval; not excluded; repaired at $T_\flat$); unused |
| Lemma 3.0 | absolute convergence | PROVED |
| Lemma 3.1 | factorisation, (3.1) | PROVED |
| Lemma 3.2 | Poisson majorant | PROVED-CITED (Koosis; Levin) |
| Lemma 3.3 | exact phase | PROVED |
| Lemma 3.4 | light cone; (e) with $M_2\le T^2e^{Tr}\lVert G\rVert_\infty$ | PROVED (corrected) |
| Prop 4.0 | CL ⟺ RH | PROVED (R163_501) |
| 4.1, Cor 4.1 | balance $N_-=P_+>0$ | PROVED (simple-zero proportion) |
| 4.2 | $\delta<\frac12$; density; $\sum\delta^2\ll R/\log R$; verification height | PROVED-CITED (R163_502 Δ) |
| 4.3 | Poisson bound on $N_-$ | PROVED |
| 4.4 | node tests absorb the cone (δ-blind) | PROVED under $M_2r<2(\sqrt2-1)\lvert G'(x_0)\rvert$; Consequence paragraph HEURISTIC |
| 4.5 | quadrature on $\overline N^{\mathcal D}$ | PROVED (R163_502 Q0; simple nodes, block form 2.4(iii′) otherwise); band reading conditional on (Q) |
| 4.6 | prime-side kernel equation; finite-vector reduction (`eq:symbol`, Möbius inversion) | PROVED |
| 4.7 | cell identity | PROVED |
| Rem 4.7a | linearised lower bound vacuous at cell scale | HEURISTIC |
| (I0) | counting heuristic | HEURISTIC; REFUTED in lattice model |
| (I1), (I1-T) | local on-line excess; window bound | ARGUED, not established; (I1) generically void at cell scale (Rem 4.7a), so $(\star_{\rm cell})$ must be attacked in the exact form $P_j=\sum_{C_j}G(\gamma)^2$; (I1-T) necessary, not sufficient |
| 4.8 $(\star_{\rm cell})$ | per-cell compensation | ARGUED, not established; ⟺ RH at the witness (Rem 4.8a, circular) |
| Rem 4.8a | $(\star_{\rm cell})$ circular at witness | PROVED (circularity identity only); margin bound PROVED-CITED (Paper 48 `thm:M`(b), $T\ge T_0(\varepsilon)$, record) |
| Lemma 4.10 | lattice-model threshold $S(T,\delta)>\pi\rho$; $T^*\le(\frac34L/\delta^2)^{1/3}$, self-consistent iff $\delta L>y_0\approx2.1773$ | PROVED-CITED (R163_402 Thm 4, Cor 5) + PROVED here (corrected per R163_590 D1) |
| Cor 4.10a | $(\star_{\rm cell})$ fails in model; (I0) refuted a fortiori; regime (α) empty | PROVED (in the model; reason corrected per R163_590 D1) |
| 4.9 | (I1-T) from arithmetic | ARGUED; fails (W2) |
| §5 | $(\star_{\rm cell})\Rightarrow$ RH ⟹ D | PROVED conditional on 4.8 |
| §6 | falsifier lines | PROVED-CITED (record, Paper 48 `tab:falsifiers`); numerical entries uncertified as marked; DH/Epstein **not separated** (earlier claim withdrawn) |
| §4.11(a) | node-pair system collapses to $\mathrm{diag}(d)$ (Loewner matrix of one function on $X$); interpolation identity (3.1) of R163_801 with tail $G^2\mathcal T_T$; off-line residues carried only by $\sum_{\log n\ge2T}\Lambda(n)n^{-1/2+ix}$ | PROVED-CITED (R163_801 Thm 1, Prop 4; Thm 3 PROVED for $C^1_c$, ARGUED at the witness; record) |
| §4.11(b) | Selberg-map invariant regions $K\subset\bigcap_T\mathcal P_T$: Lemma D (one-sided perturbations leave $\bigcap\mathcal P_T$), Thm U (rigidity in the summable class, under RH); no Beurling-regularity condition defines such a $K$ | PROVED-CITED (R163_802; record); route NO-GO |
| §4.11(c) | $f_t=\zeta+tg$ family: ζ's completed functional equation with $\Gamma_{\mathbb R}$ and pole, real coefficients, integer multiplicities, atomic prime side on a discrete semigroup (not on $\log\mathbb N$), $W^{f_t}_T=W^\zeta_T$ for $T\le\frac12\log\lambda_1$ ($\supset\lvert u\rvert<\log N_0$), off-line zeros, finite contact; Row D not provable from the listed inputs (unconditional); $(\star_{\rm cell})$ fails at its witness given witness existence; (A-loc) clause needs balance of $f_t$ | Thm F PROVED-CITED (R163_901 v2, audited R163_991: correct with fixes applied); $(\star_{\rm cell})$ clause CORRECT given witness existence (ARGUED); (A-loc) clause ARGUED, balance OPEN |
| §4.11(d) | local Weil positivity: exact cell decomposition (no cross terms); $\{P_{\rm loc}(kL,T')\}\Leftrightarrow$ D; sub-Landau $P_{\rm loc}$ ⇒ near-RH ($\beta-\tfrac12\lesssim\log\log\gamma/\log\gamma$ for dominant zeros); supra-Landau: on $K_H$ the form equals the unverified tail | Thm 1, Cor 2 PROVED-CITED (R163_601); Thm B (R163_701) core PROVED, tail ARGUED; Thm B (R163_702) PROVED-CITED (record) |
| §4.11(e) | global integrality of frequencies: $f_\chi$ (even cubic mod 7, $\Gamma(s/2)$, integer frequencies, off-line zeros); Thm O (identification at $q=1$, sign-blind at $q>1$); wall W3′ | PROVED-CITED (R163_1001, given its Lemma 1.2, PROVED-CITED with page-level caveat; record) |
| §4.11(f) | phase 164: (KZ) of the hybrid Euler–Hadamard cut is E1 (R164_101 Thm E1); positive tail without FE is zero-blind (R164_102 Thm A); Thm R: positive-off-ℕ measure + gap $(1,X)$ + ζ's FE and poles ⟹ $f=\zeta$, so O164.101 ⟺ ¬RH; identification theorem (every global property separating ζ from all falsifiers identifies ζ) | Thm E1, Thm A PROVED (R164_190); Thm R PROVED (R164_401, review audit R164_190; novelty to be verified); identification theorem PROVED as a synthesis of the cited statements (R164_190) |
| §4.11(g) | phase 165: Det+ bracket $0.8047<T_c\le\min_\rho\tau(\rho)$, $\tau\le T_L(\gamma)+\frac12\log(\pi/2)+o(1)$; Det− false for large $\delta\Lambda$ (contact = $\min_\rho T_{\rm det}$); exact phase identity, sign variable $\omega(E)$ (= Rem 4.8a); interlacing ⇏ quartet out of cone; real-rootedness at every simple $T$ | Det+ PROVED with clustering caveat (R165_101); Det− negative PROVED given cited zero count (R165_102); Thm 2/Cor 2.2 and Thm 3(a) PROVED (R165_201); flow tools PROVED, E1 (R165_202); all per R165_190 |
| §4.11(h) | phase 166: jet hierarchy (quartet term of $S^{(k)}(x_0)$ is $2k!\,\lvert Q(t_q)\rvert^2r^{1-k}\cos(2E+(k-1)\psi)$; $\mathrm{Re}\,G(t_q)^2$ = jet $k=-1$); no pole singularity at nodes; rough-zeta split $\mathcal T_X=\mathcal T^{\rm det}+\mathcal T^{\rm new}$; falsifier $P_{a,c}$; parity identity; five mechanisms DEAD; requirements (i)–(iii) | Thm 1.3, Cor 1.4, Prop 2.2 PROVED (R166_201); Thm 2.1 PROVED (R166_101); B1–B2, G1 PROVED (R166_103); Thm 3 PROVED, O202.1 OPEN (R166_202); exchange flow DEAD, lower bound ARGUED (R166_102); all per R166_190 |
| §4.11(i) | phases 166 (rounds 9–12) and 167: families P/Q (no (i)–(iii) mechanism; {i,iii} empty); Thm A (iii) ⟹ (ii); θ = 0 tools T3/T4; 7C DEAD; circularity theorem, requirement (N′); exact target (WS\*) | Thm A, B(5) PROVED (R166_501); T3/T4 PROVED, C1/C2 OPEN (R166_701); circularity PROVED for single tests/power families, ARGUED in general (R166_802); Thm A, Lemma Q, Thm C, Prop W PROVED, Thm B given (Dom$_\theta$) OPEN (R167_101); Thm B/B′, Theorem S PROVED, Thm D ARGUED (R167_102/103); (WS\*) unreachable by sieves, circular with zeros; all per R166_190, R167_190 |
| Row D | | **OPEN** |

> **Remaining gap (boxed).**
> $$\boxed{\begin{array}{c}\text{Find an identity-level mechanism, using the atomic arithmetic of }\zeta\text{ (absent in }M_m\text{, DH, Epstein),}\\ \text{that forces }P_j>N_j\text{ in every cell of a real-rooted first-contact witness containing an off-line ordinate.}\\ \text{At the witness this is equivalent to RH }(\textstyle\sum_j(P_j-N_j)=0)\text{, so it must be proved for a strictly larger,}\\ \text{named class of }G\text{; the lattice model (Lemma 4.10) shows on-line counting alone cannot supply it.}\\[4pt] \text{Moreover }(\star_{\rm cell})\text{ cannot be proved from: }\zeta\text{'s FE with }\Gamma_{\mathbb R}\text{ and pole, real coefficients, integer zero multiplicities,}\\ \text{the zero-side identity, and the prime side on }|u|<2T_0\text{ (R163\_901, audited R163\_991) — given witness existence for }f_t\text{ (ARGUED).}\\ \text{By the identification theorem (R164\_190), no class property separates: }(\star_{\rm cell})\text{ must be proved for }\zeta\text{ individually}\\ \text{from the comb/explicit formula at all heights; equivalently (TC). See §4.11(c), (e), (f).}\end{array}}$$
>
> *Removed (v7):* on-line abundance — Bombieri–Hejhal: DH-type combinations have 100 % of their zeros on the line (conditionally on GRH and pair independence) yet infinitely many off it (R163_602 F2); Riemann–Siegel/AFE structure — it uses only the functional equation and is shared by $f_\chi$ (R163_603 L2.1, R163_1001).

---

**Summary of the outcome, stated first so that no step is hidden.** §§1–3 and §4.1–§4.7 are PROVED or PROVED-CITED (after the fixes of R163_490 and the audits R163_501, R163_502).
The closing lemma (CL) of §4 is **not proved**: CL is PROVED to be *equivalent* to RH (Proposition 4.0), and the
attempt in §4.7–§4.9 reduces it to one per-cell compensation inequality $(\star_{\rm cell})$, which is ARGUED and is itself equivalent to
RH at the witness (Remark 4.8a; circular). The
falsifier $M_m$ shows (§6, Rem 4.8a) that $(\star_{\rm cell})$ cannot hold for a reason that uses only the on-line zeros,
the positions of the off-line zeros and the bound $\delta<\tfrac12$; the reason must also involve the window $T_*$
itself; the gap is $(\star_{\rm cell})$ in its exact form (§4.8, Rem 4.7a, Cor 4.10a; (I1) is only one possible route). §5 therefore gives a *conditional*
deduction: D ⟸ CL ⟸ $(\star_{\rm cell})$. Row D stays OPEN.

---

## §1 Setup and statement

### 1.1 Forms (Paper 47, `eq:symbol`, `eq:form`, `eq:W`)

For $T>0$ write $I_T=(-T,T)$. For $F\in L^2(I_T)$, extended by zero, put
$\widehat F(z)=\int F(t)e^{izt}\,dt$ (an entire function) and $\widehat F^{\#}(z):=\overline{\widehat F(\bar z)}$.
Write $c_F(u)=\int F(t)\overline{F(t-u)}\,dt$, and define

$$
\sigma_T(\tau)=m(\tau)-\sum_{n\in\mathcal N_T}v_n\cos(\tau\log n),\qquad
m(\tau)=\mathrm{Re}\,\psi\!\big(\tfrac14+\tfrac{i\tau}2\big)-\log\pi,\qquad v_n=\frac{2\Lambda(n)}{\sqrt n},
$$

where $\mathcal N_T=\{n\ge2:\log n<2T\}$. Then

$$
\mathfrak a_T(F)=\frac1{2\pi}\int_{\mathbb R}\sigma_T|\widehat F|^2\,d\tau,\qquad
W_T(F)=\mathfrak a_T(F)+2\,\mathrm{Re}\big(A(F)\overline{B(F)}\big),
$$

with $A(F)=\widehat F(-i/2)=\int Fe^{t/2}$ and $B(F)=\widehat F(i/2)=\int Fe^{-t/2}$. Both forms live on the form
domain $\mathcal D_T=\{F:\int\log(2+|\tau|)|\widehat F|^2<\infty\}$. The primitive space is
$\mathcal P_T=\{A=B=0\}$. Write $\lambda^{\rm W}_T$ and $\lambda^{\rm A}_T$ for the bottoms of $W_T$ on $L^2(I_T)$
and of $\mathfrak a_T$ on $\mathcal P_T$.

Put $\Phi_F(s)=\widehat F(-i(s-\tfrac12))$. For a nontrivial zero $\rho$ of $\zeta$ write
$t_\rho:=-i(\rho-\tfrac12)$, so that $\rho=\tfrac12+\delta+i\gamma$ gives $t_\rho=\gamma-i\delta$, and
$1-\bar\rho\mapsto\bar t_\rho$.

### 1.2 Row D and the statement

**Definition 1.1 (row D).** Row D is the statement $\forall T>0:\ W_T\ge0$ on $\mathcal D_T$. Equivalently,
$\forall T:\ \mathfrak a_T\ge0$ on $\mathcal P_T\cap\mathcal D_T$.

**Theorem 1.2 (D ⟺ RH). PROVED-CITED.** (Stated here; its (⇐) direction uses Theorem 1.3 below, forward reference.)
(⇒ D implies RH): $C_c^\infty(I_T)\subset\mathcal D_T$, then Paper 45 Thm 11.3 with Thm 8.4.
(⇐): under RH, Thm 1.3 (Paper 47 `lem:roughEF`, Lemma 3.0) gives $W_T(F)=\sum_\gamma\lvert\widehat F(\gamma)\rvert^2\ge0$
on $\mathcal D_T$. See also Bombieri 2000, Thm 1. Primitive tests suffice. *Paper 45 is a record reference; not re-audited here.*

**Theorem 1.3 (zero-side identity). PROVED-CITED** (Paper 47, `lem:roughEF`, together with Lemma 3.0 below for the
absolute convergence it needs). For $F\in\mathcal D_T$,

$$
W_T(F)=\sum_\rho \widehat F(t_\rho)\,\overline{\widehat F(\bar t_\rho)}=\sum_\rho(\widehat F\widehat F^{\#})(t_\rho),
\tag{1.1}
$$

with multiplicity and absolute convergence.

`lem:roughEF` is stated for real $F$. Lemma 3.0 below supplies its hypothesis (b) for every $F\in\mathcal D_T$. The
complex case follows by polarisation: (1.1) is the hermitian form whose real-test restriction is `lem:roughEF`.

**Target.** This memo tries to prove D by excluding a first contact (§2). The argument is by contradiction: assume
¬RH and derive a contradiction from the structure of the first-contact witness.

---

## §2 The proved chain

**2.1 Positivity up to $\tfrac12\log5$. PROVED-CITED** (Paper 47, `thm:log5W`, `thm:log5A`; a certified computation in
ball arithmetic, Legendre basis, Schur/Haynsworth inertia; record, with the scripts in the paper's data). For every
$0<T\le\tfrac12\log5=0.804718\ldots$, $\lambda^{\rm W}_T\ge10^{-18}$ and $\lambda^{\rm A}_T\ge2.5\cdot10^{-12}$.
Earlier results: Zhu 2026 to $0.8$ (CITED, as stated there); Yoshida 1992 and Bombieri 2000 to $\tfrac12\log2$.

**2.2 Monotonicity and continuity. PROVED-CITED** (Paper 47, `lem:monoT`, `lem:contT`, `lem:contA`; record. For the
complete form this is also Bombieri 2000, Thm 5). The maps $T\mapsto\lambda^{\rm W}_T$ and $T\mapsto\lambda^{\rm A}_T$
are nonincreasing and continuous on $(0,\infty)$. Both bottoms are attained, because the forms have compact
resolvent (Paper 47, proof of `thm:O`; Bombieri 2000, Thm 3).

**2.3 Existence of a first contact under ¬RH. PROVED** (from 1.2, 2.1 and 2.2).
Assume ¬RH. By Theorem 1.2 there is $T_0$ with $\lambda^{\rm W}_{T_0}<0$. Put
$T_c:=\inf\{T:\lambda^{\rm W}_T\le0\}$.
- By 2.1, $\lambda^{\rm W}\ge10^{-18}$ on $(0,\tfrac12\log5]$. By continuity this stays positive on a neighbourhood
  of $\tfrac12\log5$, so $T_c>\tfrac12\log5>0.8047$.
- By monotonicity, $\lambda^{\rm W}_T>0$ for $T<T_c$.
- By continuity, $\lambda^{\rm W}_{T_c}=0$, and the value is attained. So $W_{T_c}\ge0$ and
  $E_c:=\ker W_{T_c}\neq\{0\}$.
- $E_c$ is finite-dimensional (compact resolvent).

The same argument with `lem:contA` and `lem:firstcontact` (Paper 47) gives a primitive first contact
$T_*\ge T_c$ (since $\lambda^{\rm W}\le\lambda^{\rm A}$) with $\ker H_{T_*}\ne0$. From here on we work at the complete
contact $T_c$, because (1.1) applies there directly.

**2.4 Structure of the witness. PROVED** (audited and repaired in R163_501: Thm B, R(a)–(c),(e), FC0(ii), FC(i)–(ii),
G PROVED; R(d) PROVED AFTER REPAIR via R(d′) for the complex kernel $E_c$; original source R160_X_C1, Paper 48
`prop:witness`; the node identity (iv) remains PROVED-CITED, R162_2202, record).
- (i) Every $F\in E_c\setminus0$ has convex support $[-T_c,T_c]$. Its transform has exponential type $T_c$, and its
  zeros have density $T_c/\pi$ on each half-plane (on each half-line once real-rooted; R163_501).
- (ii) Each nonzero parity part of $E_c$ contains a real, parity-definite **witness** $F$ such that $\widehat F$ has
  only real zeros. The proof uses Blaschke invariance (moving a zero $w\mapsto\bar w$ preserves $\|F\|$, the support
  and $W$) and the parity-crossing count of the bottom eigenspace.
- (iii) **Gauss nodes.** Let $X$ be the zero set of $\widehat F$ (the *nodes*), and put $\widehat H_x=\widehat F/(z-x)$
  for $x\in X$. Then $W(H_x,H_y)=0$ for $x\ne y$, and on $\mathrm{span}\{H_x\}$
  $$
  W_{T_c}(G)=\sum_{x\in X}w_x|\widehat G(x)|^2,\qquad w_x=d_x/|\widehat F'(x)|^2=W(H_x)/|\widehat F'(x)|^2\ge0 .
  $$
  (The modulus is essential: for odd real $F$, $\widehat F'(x)^2<0$; R163_501 §4, R163_490 fix 4.)
  **Q0 (R163_502, PROVED, unconditional):** this holds on the $\mathcal D$-closure $\overline N^{\mathcal D}$ of
  $N=\mathbb C\widehat F+\mathrm{span}\{\widehat H_x\}$, where it also equals the zero sum (1.1).
  *Remark.* Whether $\overline N^{\mathcal D}\oplus\mathbb CF=\mathcal D$ (hypothesis (Q), OS-3) is OPEN and
  RH-neutral; R163_502 reduces it to Q1 and proves it in $L^2$ under (LB) (Q2). It is not used.
  (Stated for simple nodes; at a node of multiplicity $k$ add $\widehat F/(z-x)^j$, $j\le k$; the quadrature then has a
  $k\times k$ block at $x$ involving $\widehat G^{(i)}(x)$, and is no longer diagonal. See 2.4(iii′).)
- (iii′) **Block version for multiple nodes. PROVED.** Let $x\in X$ have multiplicity $k_x$, and put
  $\widehat H_{x,j}=\widehat F/(z-x)^j$, $1\le j\le k_x$; these lie in $\mathcal D_T$ (entire, same type, faster decay).
  - *Cross-node orthogonality.* For real $x\ne y$, $i\le k_x$, $j\le k_y$: $\widehat H_{x,i}\widehat H_{y,j}^\#=\widehat F\cdot\widehat K^\#$
    with $\widehat K=\widehat F/((z-x)^i(z-y)^j)$, which is entire because $\widehat F$ vanishes to order $\ge i$ at $x$ and
    $\ge j$ at $y$, and $K\in\mathcal D_T$. Hence $W(H_{y,j},H_{x,i})=W(K,F)=0$, since $F\in E_c=\ker W_{T_c}$ (§4.6:
    $W(F,\cdot)=0$; the hermitian form depends on $\widehat\Phi\widehat\Psi^\#$ only, by (1.1) or by `eq:form`).
  - *Node block.* The same identity with $y=x$ gives $W(H_{x,j},H_{x,i})=W(K_{i+j},F)$ with $\widehat K_{i+j}=\widehat F/(z-x)^{i+j}$,
    which is $0$ whenever $i+j\le k_x$. So the Gram matrix $B_x:=(W(H_{x,j},H_{x,i}))_{i,j\le k_x}$ is Hankel and
    vanishes above the anti-diagonal; it is $\succeq0$ because $W_{T_c}\ge0$.
  - *Quadrature.* For $\widehat G=c\widehat F+\sum_x\sum_{j\le k_x}a_{x,j}\widehat H_{x,j}$ (finite sum),
    $W(G)=\sum_x a_x^*B_xa_x$ (the $\widehat F$ term drops out, $W(F,\cdot)=0$). The vector $a_x$ is the principal part of
    $\widehat G/\widehat F$ at $x$; writing $\widehat F=(z-x)^{k_x}u_x$, $u_x(x)\ne0$, it is obtained from
    $(\widehat G^{(i)}(x))_{i<k_x}$ by an invertible triangular map (Taylor coefficients of $\widehat G/u_x$). Hence
    $W(G)=\sum_x\mathbf g_x^*\widetilde B_x\mathbf g_x$ with $\mathbf g_x=(\widehat G^{(i)}(x))_{i<k_x}$ and $\widetilde B_x\succeq0$
    a $k_x\times k_x$ block. For $k_x=1$ this is $w_x|\widehat G(x)|^2$ with $w_x=W(H_x)/|\widehat F'(x)|^2$, i.e. 2.4(iii).
    The extension to $\overline N^{\mathcal D}$ is the Q0 argument of R163_502 verbatim (continuity of the finitely many
    derivative evaluations at each node in $\mathcal D$). ∎
- (iv) **Node identity** (R162_2202, Theorem NI; record). For even $F$ and a simple node $x$,
  $$
  w_x\widehat F'(x)=\mathfrak A_F(x)+\sum_{n<e^{T_c}}v_n\,k_F(x,\log n)-\frac{2A(F)x}{x^2+\frac14},
  $$
  where $k_F(x,u)=\int_u^{T_c}F(s)\sin(x(s-u))\,ds$ and $\mathfrak A_F(x)=\frac1{2\pi}\int m(\tau)\widehat F(\tau)/(\tau-x)\,d\tau$.

**2.5 Type I / Type II. PROVED-CITED** (R162_1701, Theorem 1; record). $T_c\le T_*$, and RH ⟸ R-C.a ∧ R-C.b:
- R-C.a: there is no polar contact before $T_*$;
- R-C.b: there is no Type I primitive contact.

This split is not used below.

**Remark 2.5a (primitive contact; R163_501 §3.4).** The full-support claim FC(iii) at the primitive contact
$T_*=\inf\{\lambda^{\rm A}<0\}$ is UNPROVED as stated (it fails if $\lambda^{\rm A}$ vanishes on an interval $[T_1,T_*]$, which is not excluded;
repaired at $T_\flat$); real-rootedness there is PROVED. The repair
works at $T_\flat:=\sup\{T:\lambda^{\rm A}_T>0\}$. Nothing in this memo uses FC(iii). The argument works at $T_c$ and covers both types at once, because it never uses the
primitive space.

---

## §3 The geometric picture: the light cone

Throughout §3, $F$ is a witness at $T:=T_c$: real, parity-definite and real-rooted, with $W_T(F)=0$. Define
$G:=\widehat F$ if $F$ is even, and $G:=-i\widehat F$ if $F$ is odd.

**Lemma 3.0 (absolute convergence). PROVED.** For $f\in PW_T$ with $\int\log(2+|\tau|)|f|^2<\infty$ and
$|\delta_\rho|<\tfrac12$ (the sum runs over all $\rho$, and $1-\rho$ has $\delta<0$),
$$
\sum_\rho|f(\gamma_\rho-i\delta_\rho)|^2\le C_T\int\log(2+|\tau|)\,|f(\tau)|^2\,d\tau<\infty .
$$

*Proof.* By Lemma 3.2 below, $|f(x+iy)|^2\le e^{2T|y|}(P_{|y|}*|f|^2)(x)$. By subharmonicity of $|f|^2$ on the disc
$D(t_\rho,1)$,
$$
|f(t_\rho)|^2\le\frac1\pi\int_{D(t_\rho,1)}|f|^2\,dA\le\frac{e^{3T}}{\pi}\int_{\mathbb R}|f(\tau)|^2K(\tau-\gamma_\rho)\,d\tau,
$$
where $K(u)=\int_{-3/2}^{3/2}\int_{-1}^1P_{|y|}(u-s)\,ds\,dy\ll(1+u^2)^{-1}$; the case $y=0$ is the boundary value.
Now sum over $\rho$. By Titchmarsh, Thm 9.6(A) (CITED), $\sum_\rho(1+(\tau-\gamma_\rho)^2)^{-1}\ll\log(2+|\tau|)$. ∎

**Lemma 3.1 (factorisation and zero-side form). PROVED.**
- (a) $G$ is real on $\mathbb R$ and has parity. It factors as $G(z)=c\,z^{m}\prod_{x\in X_+}(1-z^2/x^2)$, with
  $c\in\mathbb R\setminus0$, $X_+$ the positive nodes (with multiplicity), and $\sum_{X_+}x^{-2}<\infty$.
- (b) $(\widehat F\widehat F^{\#})(t)=G(t)^2$ for all $t\in\mathbb C$.
- (c) Hence
  $$
  0=W_T(F)=\underbrace{\sum_{\rho\ \text{on-line}}G(\gamma_\rho)^2}_{=:P_+}\;+\;4\sum_{q}\mathrm{Re}\,G(\gamma_q-i\delta_q)^2,
  \tag{3.1}
  $$
  where $q$ runs over the off-line quartets $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$, with $\rho=\tfrac12+\delta_q+i\gamma_q$,
  $\delta_q>0$ and $\gamma_q>0$. Everything is counted with multiplicity and converges absolutely.

*Proof.*
- (a) $F$ is real, so $\widehat F^\#(z)=\widehat F(-z)$.
  - If $F$ is even, $\widehat F$ is even and $\widehat F^\#=\widehat F$, so $G$ is real on $\mathbb R$.
  - If $F$ is odd, $\widehat F$ is odd with $\widehat F^\#=-\widehat F$, so $G=-i\widehat F$ is odd and real on
    $\mathbb R$.
  - $G$ has order $\le1$ (exponential type). Hadamard gives $G=z^me^{a+bz}\prod_x E_1(z/x)$. The zero set is
    symmetric, so the factors pair as $E_1(z/x)E_1(-z/x)=1-z^2/x^2$, and $\sum x^{-2}<\infty$.
  - The parity of $G$ forces $e^{bz}=e^{-bz}$, so $b=0$. $c$ is real because $G$ is real on $\mathbb R$.
- (b) In the even case, $\widehat F\widehat F^\#=\widehat F^2=G^2$. In the odd case,
  $\widehat F\widehat F^\#=(iG)(-iG)=G^2$.
- (c) Apply (1.1) and Lemma 3.0. An on-line zero gives $G(\gamma)^2\ge0$. A quartet maps to
  $\{t,\bar t,-t,-\bar t\}$ with $t=\gamma-i\delta$. Since $G(-z)^2=G(z)^2$ and $G(\bar z)=\overline{G(z)}$, the four
  terms sum to $2G(t)^2+2\overline{G(t)^2}=4\,\mathrm{Re}\,G(t)^2$. ∎

**Lemma 3.2 (Poisson majorant). PROVED-CITED** (Koosis, *The Logarithmic Integral I*, §III.G; Levin, *Lectures on
Entire Functions*, Lecture 16). If $f\in PW_T$, then $f$ is bounded on $\mathbb R$, and for $y\ne0$
$$
\log|f(x+iy)|\le T|y|+(P_{|y|}*\log|f|)(x),\qquad\text{hence}\qquad |f(x+iy)|^2\le e^{2T|y|}(P_{|y|}*|f|^2)(x),
$$
where $P_\delta(u)=\delta/(\pi(u^2+\delta^2))$. The second inequality follows from the first by Jensen's inequality.

**Lemma 3.3 (exact phase). PROVED.** Let $\delta>0$ and $\gamma\in\mathbb R$. Then
$G(\gamma-i\delta)=\pm|G(\gamma-i\delta)|\,e^{i\Theta}$, where
$$
\Theta(\gamma,\delta)=\sum_{x\in X}\arctan\frac{\delta}{x-\gamma}
$$
(with multiplicity; $m$ copies of $x=0$; when $x=\gamma$, set $\arctan(\delta/0):=\pi/2$). The sum converges when $\pm x$ are paired.
Consequently
$$
\mathrm{Re}\,G(\gamma-i\delta)^2=|G(\gamma-i\delta)|^2\cos2\Theta .
$$

*Proof.*
- Write $z=\gamma-i\delta$. Then $1-z/x=(x-\gamma+i\delta)/x$, and $\arg(x-\gamma+i\delta)\in(0,\pi)$. This argument
  differs from $\arctan(\delta/(x-\gamma))$ by $0$ or $\pi$.
- Division by $x<0$ adds $\pi$, and the factor $z^m$ is handled the same way. So every factor has argument
  $\equiv\arctan(\delta/(x-\gamma))\pmod\pi$.
- The paired terms satisfy $\arctan\frac\delta{x-\gamma}+\arctan\frac\delta{-x-\gamma}=O(\delta(1+|\gamma|)x^{-2})$.
  This is summable, so $\Theta$ converges, and the product of the finitely many unpaired $\pi$-shifts is a sign.
- Squaring removes the sign. ∎

**Lemma 3.4 (light cone, with explicit errors). PROVED.** Let $t=\gamma-i\delta$ with $\delta>0$. Let $x_0\in X$ be a
node nearest to $\gamma$, and split
$$
\Theta=\varphi_0+E,\qquad \varphi_0:=\arctan\frac{\delta}{x_0-\gamma}\in(-\tfrac\pi2,\tfrac\pi2],\qquad
E:=\sum_{x\in X\setminus\{x_0\}}\arctan\frac{\delta}{x-\gamma},
$$
removing one copy of $x_0$.
- (a) $\mathrm{Re}\,G(t)^2<0$ if and only if $\cos2(\varphi_0+E)<0$.
- (b) Suppose $|E|<\pi/4$. Then
  $$
  |x_0-\gamma|<\delta\cot(\tfrac\pi4+|E|)\ \Longrightarrow\ \mathrm{Re}\,G(t)^2<0\ \Longrightarrow\ |x_0-\gamma|<\delta\cot(\tfrac\pi4-|E|).
  $$
  When $E=0$ both radii equal $\delta$. This is the **light cone** $\{|\gamma-x_0|<\delta\}$ of the node $x_0$.
- (c) $E=\delta S_0+R$, where
  $$
  S_0=\sum_{x\ne x_0}\frac1{x-\gamma}=-\frac{G'(\gamma)}{G(\gamma)}-\frac1{x_0-\gamma}
  $$
  (taken as the limit $-G''(x_0)/(2G'(x_0))$ when $\gamma=x_0$ is a simple node), and
  $|R|\le\frac{\delta^3}3\sum_{x\ne x_0}|x-\gamma|^{-3}$.
- (d) If $|x-\gamma|\ge g$ for all $x\ne x_0$, and $\#\{x\ne x_0:|x-\gamma|<r\}\le\kappa r$ for $r\ge g$, then
  $|R|\le\kappa\delta^3/(2g^2)$.
- (e) **Lorentzian form.** Put $r:=|t-x_0|$ and $M_2:=\sup_{|z-x_0|\le r}|G''|$. Then
  $$
  \mathrm{Re}\,G(t)^2=G'(x_0)^2\big[(\gamma-x_0)^2-\delta^2\big]+\mathcal E,\qquad |\mathcal E|\le r^2\big(|G'(x_0)|M_2r+\tfrac14M_2^2r^2\big),
  $$
  and $M_2\le T^2e^{Tr}\|G\|_{L^\infty(\mathbb R)}$ (the disc $|z-x_0|\le r$ reaches $|y|=r\ge\delta$; corrected per R163_490 fix 1).

*Proof.*
- (a) Immediate from Lemma 3.3.
- (b) $\cos2\Theta<0$ if and only if $\mathrm{dist}(\Theta,\pi\mathbb Z)\in(\pi/4,\pi/2]$.
  - Since $|\varphi_0|\le\pi/2$ and $|E|<\pi/4$, we have $|\Theta|<3\pi/4$. So the condition reads
    $\pi/4<|\varphi_0+E|<3\pi/4$.
  - This implies $|\varphi_0|>\pi/4-|E|$, i.e. $\delta/|x_0-\gamma|>\tan(\pi/4-|E|)$.
  - Conversely, $|\varphi_0|>\pi/4+|E|$ gives $\pi/4<|\varphi_0+E|\le\pi/2+|E|<3\pi/4$.
- (c) Use $|\arctan u-u|\le|u|^3/3$ for real $u$, and $G'/G(\gamma)=\sum_x(\gamma-x)^{-1}$ (symmetric summation; from
  Lemma 3.1(a)).
- (d) Abel summation: $\sum|x-\gamma|^{-3}\le\int_g^\infty3r^{-4}\kappa r\,dr=3\kappa/(2g^2)$.
- (e) Write $G(z)=G'(x_0)(z-x_0)+\eta(z)$ with $|\eta|\le\frac12M_2|z-x_0|^2$. Square, and use
  $\mathrm{Re}\,(t-x_0)^2=(\gamma-x_0)^2-\delta^2$. The bound on $M_2$ is Bernstein's inequality for functions of
  exponential type $T$ bounded on $\mathbb R$, $|G''(x+iy)|\le T^2e^{T|y|}\|G\|_\infty$ (CITED: Boas, *Entire
  Functions*, 11.1.2). ∎

**Reading.** To first order, an off-line quartet at $\gamma-i\delta$ contributes $4G'(x_0)^2[(\gamma-x_0)^2-\delta^2]$
to (3.1). This is a Minkowski interval, with the node $x_0$ as vertex and $\delta$ as time: it is negative exactly when
the zero lies inside the light cone of a node. An on-line zero is the case $\delta=0$, which is never inside a cone.
For $\zeta$, $0<\delta<\tfrac12$ (Lemma 4.2 below), while the mean node spacing is $\pi/T_c<\pi/0.8047<3.91$; so the
cone regime $\delta\ll$ spacing is the relevant one at moderate $T_c$.

---

## §4 The closing lemma

### 4.0 Statement

**Closing Lemma (CL).** Let $T>\tfrac12\log5$, and let $F\in\mathcal D_T$ be real, parity-definite and real-rooted,
with $W_T\ge0$ on $\mathcal D_T$ and $W_T(F)=0$. Then $F=0$.

In words: no configuration of nodes can place an off-line zero of $\zeta$ inside a light cone with enough weight to
balance all the on-line zeros in (3.1), at a window where $W_T\ge0$.

**Proposition 4.0 (CL ⟺ RH). PROVED** [(⇒) audited in R163_501 §5: uses only FC0(ii)+R(c) at $T_c$; (⇐) repaired per R163_501 FC0(i)].
- (⇐) Assume RH. Then (3.1) reads $\sum_\gamma G(\gamma)^2=0$, so $G$ vanishes at every ordinate. A positive proportion of
  zeros are simple (Levinson 1974; Conrey 1989; CITED), so there are $\gg R\log R$ *distinct* ordinates in $(0,R)$
  (Riemann–von Mangoldt alone counts with multiplicity and does not suffice; R163_501 FC0(i)), while a nonzero entire function of exponential type has $O(R)$
  zeros in $|z|<R$ (Jensen). So $F=0$. This direction does not even use $W_T\ge0$. The argument proves the general fact: *under RH,
  $W_T(F)=0$ with $F\in\mathcal D_T$ arbitrary (complex) implies $F=0$*, since $W_T(F)=\sum_\gamma|\widehat F(\gamma)|^2$ forces
  $\widehat F$ to vanish at every ordinate; reality, parity and real-rootedness are not used.
- (⇒) Assume ¬RH. Then §2.3–2.4 produce a nonzero witness at $T=T_c>\tfrac12\log5$ that satisfies every
  hypothesis of CL. The real-rootedness is load-bearing: Blaschke flips $w\mapsto\bar w$ leave
  $\widehat F\widehat F^\#$, hence $W$ via (1.1), unchanged (sound), but they do not make zeros real. That step is
  the eigenspace/parity-crossing argument of R160_X_C1 Thm R, now audited: PROVED in R163_501 (R(c); R(d) after
  repair). ∎

**Consequence for the logic.** Any proof of CL is a proof of RH. By wall W1 (Paper 48), a sign step that is equivalent
to RH is either a reformulation or the proof itself. The attempt below is therefore written to isolate exactly one
non-restating inequality, and to label it.

### 4.1 Balance. PROVED

Under ¬RH, at the witness: $N_-:=-4\sum_q\mathrm{Re}\,G(t_q)^2=P_+>0$.

*Proof.* (3.1) gives $N_-=P_+$. For positivity, the *distinct* on-line ordinates number $\gg R\log R$ in $(0,R)$ (positive
proportion of simple zeros on the line: Levinson 1974, Conrey 1989; CITED; R163_501 FC0(i)), while $G\ne0$ has $O(R)$ zeros there. So $G(\gamma)\ne0$ for some on-line $\gamma$, and $P_+>0$. ∎

**Corollary 4.1.** At least one quartet has $\cos2\Theta_q<0$. Whenever $|E_q|<\pi/4$, it lies in the corrected light
cone $|\gamma_q-x_0|<\delta_q\cot(\pi/4-|E_q|)$ of its nearest node (Lemma 3.4(b)). PROVED.

### 4.2 Euler-product input on δ. PROVED-CITED

Every nontrivial zero satisfies $\delta<\tfrac12-c/\log(\gamma+2)$ (de la Vallée Poussin; Titchmarsh Thm 3.8).
Moreover:
- $N(\sigma,R)=o(R)$ for every $\sigma>\tfrac12$ (Carlson 1920; Ingham; Selberg, Titchmarsh 9.19(C));
- $\sum_{\gamma\le R}\delta^2\ll R/\log R$ and $\sum_{\gamma\le R}\delta\ll R$ (R163_502 Thm Δ, PROVED-CITED from Selberg's density theorem, Titchmarsh 9.19(C)). This supersedes the record bound of R163_115. It is not load-bearing anywhere below;
- RH holds for $0<\gamma\le3\cdot10^{12}$ (Platt–Trudgian 2021; CITED), so every $\gamma_q>3\cdot10^{12}$.

This is the only place where the Euler product enters the sign analysis directly. Remark 4.8 records where else it
enters.

### 4.3 Poisson bound on the negative mass. PROVED

$$
N_-\le\int_{\mathbb R}G(\tau)^2\,m_{\rm off}(\tau)\,d\tau,\qquad m_{\rm off}(\tau):=4\sum_q e^{2T\delta_q}P_{\delta_q}(\tau-\gamma_q)\ \mathbf 1\{\cos2\Theta_q<0\}.
$$

*Proof.* $-\mathrm{Re}\,G(t_q)^2\le|G(t_q)|^2\mathbf 1\{\cos2\Theta_q<0\}$. Then apply Lemma 3.2. ∎

On the other side, $P_+=\int G^2\,dN_0$, where $dN_0$ is the on-line counting measure. So (3.1) says
$\int G^2\,dN_0=N_-\le\int G^2m_{\rm off}$.

### 4.4 Node tests absorb the cone. PROVED

Let $x_0$ be a simple node and $q$ a quartet with $r=|t_q-x_0|$ small. By (1.1) and Lemma 3.1(b),
$$
w_{x_0}G'(x_0)^2=w_{x_0}|\widehat F'(x_0)|^2=W(H_{x_0})=\sum_\rho\frac{G(t_\rho)^2}{(t_\rho-x_0)^2},
$$
with $w_x:=W(H_x)/|\widehat F'(x)|^2$ in both parities. (In the odd case $\widehat F'(x)^2=-G'(x)^2$, so dividing by
$\widehat F'(x)^2$ would give $w_x\le0$; with $|\widehat F'(x)|^2=G'(x)^2$ the identity holds with no sign
convention: $\widehat H_x=iG/(z-x)$, and $\widehat H_x\widehat H_x^\#=G^2/(z-x)^2$ by Lemma 3.1(b). Corrected per
R163_490 fix 4.) The quartet's terms near $x_0$ are
$2\,\mathrm{Re}\big[G(t_q)^2/(t_q-x_0)^2\big]=2G'(x_0)^2\,\mathrm{Re}(1+u)^2$ with $|u|\le M_2r/(2|G'(x_0)|)$, which is
**positive** provided $M_2r<2(\sqrt2-1)|G'(x_0)|$ (then $|u|<\sqrt2-1$ and $\mathrm{Re}(1+u)^2\ge1-2|u|-|u|^2>0$). Each on-line
$\gamma$ in the node cell contributes $G(\gamma)^2/(\gamma-x_0)^2=G'(x_0)^2(1+O(\cdot))$, also positive.

*Proof.* By Lemma 3.4(e), $G(t)/(t-x_0)=G'(x_0)(1+u)$ with $|u|\le M_2r/(2|G'(x_0)|)$. Square it. ∎

**Remark (HEURISTIC; cf. R160_X_C1 Thm Q, W3).** To first order the node weight $w_{x_0}$ counts the zeros in the cell of $x_0$, on-line and off-line
alike, all with sign $+$. This agrees with Remark G.1 of R160_X_C1: the weighted node density matches
Riemann–von Mangoldt. **The node quadrature is blind to $\delta$ to first order.** The sign of an off-line zero is
visible only in the test $F$ itself, whose transform vanishes at the vertex of the cone, and in tests built from it. So
no inequality on the weights $w_x$, including the prime-side formula 2.4(iv), can yield the contradiction alone. This is
the node-level form of Theorem Q of R160_X_C1 (Blaschke-invariant forms are blind) and of W3.

### 4.5 Quadrature on the node closure. PROVED (R163_502 Q0); band reading is a remark conditional on (Q)

(Stated for simple nodes; at a node of multiplicity $k$ add $\widehat F/(z-x)^j$, $j\le k$; the quadrature then has a
$k\times k$ block at $x$ involving $\widehat G^{(i)}(x)$, and is no longer diagonal; 2.4(iii′).)

For every $\Psi=\widehat G\widehat H^\#$ with $G,H\in\overline N^{\mathcal D}$,
$$
\sum_\rho\Psi(t_\rho)=\sum_{x\in X}w_x\Psi(x)
$$
(R163_502 Q0; R160_X_C1 Thm G(d)). *Remark (conditional on (Q), OPEN, RH-neutral):* if the products span a dense set of the band, then $\widehat{\nu_X}$ and the Weil distribution agree on $(-2T,2T)$,
where $\nu_X=\sum_xw_x\delta_x\ge0$. That Weil distribution has the atoms $-\frac{\Lambda(n)}{\sqrt n}(\delta_{\log n}+\delta_{-\log n})$
at the integers $n<e^{2T}$. The measure $\nu_X$ is a positive solution of KEP($T_c$) (`thm:KEP2` gives the converse direction); whether it is the unique one is
not claimed.

**What it gives.** Integrality of the comb (atoms exactly at $\log n$, $n\in\mathbb N$) enters (4.5) only as the
Fourier data of a positive measure on a band. It carries no sign (W12): the positive extension exists by the first
contact itself.

### 4.6 The prime side of the kernel equation. PROVED

$F\in E_c$ if and only if, for every $H\in\mathcal D_T$,
$$
\frac1{2\pi}\int\Big(m(\tau)-\sum_{n<e^{2T}}v_n\cos(\tau\log n)\Big)\widehat F(\tau)\overline{\widehat H(\tau)}\,d\tau+A(F)\overline{B(H)}+B(F)\overline{A(H)}=0 .
$$

*Proof.* $W_T\ge0$ and $W_T(F)=0$ give $W_T(F,\cdot)=0$ by Cauchy–Schwarz for nonnegative forms. Expand with
`eq:symbol` and `eq:W`. ∎

By `eq:symbol` the comb of $W_T$ involves only $n\in\mathcal N_T$, so any coefficient vector agreeing with
$(\Lambda(n))_{n<e^{2T}}$ gives the same $W_T$. The vector is determined by $a*1=\log$ on $n<e^{2T}$ (Möbius
inversion). Hence **at a fixed window, "the arithmetic of $\zeta$" is exactly this finite vector.**

### 4.7 Cell decomposition. PROVED

Let $X=\{x_j\}$ be the nodes in increasing order, and let $C_j=[\xi_{j-1},\xi_j)$ be the cell of $x_j$, where
$\xi_j=\frac12(x_j+x_{j+1})$. Split (3.1) by cells, assigning each zero to the cell containing its ordinate:
$$
0=\sum_j\Big(\underbrace{\sum_{\gamma\in C_j\ \text{on}}G(\gamma)^2}_{P_j}+\underbrace{4\sum_{q:\gamma_q\in C_j}\mathrm{Re}\,G(t_q)^2}_{-N_j}\Big).
$$
By Lemma 3.4(e), with $h_j:=|C_j|$ and every point of $C_j$ within distance $h_j$ of $x_j$,
$$
P_j\ge G'(x_j)^2\sum_{\gamma\in C_j}(\gamma-x_j)^2\,(1-\epsilon_j)_+^2,\qquad
N_j\le4G'(x_j)^2\sum_{q\in C_j}\big[\delta_q^2-(\gamma_q-x_j)^2\big]_++\mathcal E_j,
$$
with $\epsilon_j=M_2h_j/(2|G'(x_j)|)$, $M_2:=\sup_{|z-x_j|\le h_j+\frac12}|G''|$, and $\mathcal E_j$ bounded by Lemma 3.4(e) with $r\le h_j+\tfrac12$. ∎

**Remark 4.7a (vacuity at cell scale; R163_490 fix 2). HEURISTIC.** The cell identity $0=\sum_j(P_j-N_j)$ with
$P_j=\sum_{C_j}G(\gamma)^2$ is exact. The *lower bound* on $P_j$, however, is generically empty. By Bernstein,
$|G'|\lesssim T\|G\|$ and generically $M_2\asymp T^2\|G\|$, so with $h_j\asymp\pi/T$ one gets
$\epsilon_j\gtrsim\pi/2>1$ and $(1-\epsilon_j)_+=0$ for typical cells. The Lorentzian linearisation of Lemma 3.4(e) is
valid only on scale $r\ll1/T$, not on a cell of length $\pi/T$. Below, $P_j$ is used only in its exact form. When $\epsilon_j\ge1$ the side condition of (I1) cannot hold, so (I1) is
generically **void as formulated**; $(\star_{\rm cell})$ must be attacked in the exact form $P_j=\sum_{C_j}G(\gamma)^2$.

### 4.8 The compensation inequality. ARGUED

$$
(\star_{\rm cell})\qquad\text{for every cell }C_j\text{ that contains an off-line ordinate:}\quad P_j>N_j .
$$

Summing over $j$ (all other cells have $N_j=0$ and $P_j\ge0$) gives $W_T(F)>0$. This contradicts $W_T(F)=0$, so CL
follows, and with it RH (§5).

**The argument for $(\star_{\rm cell})$.** It rests on three inputs.
- **(I2) [PROVED-CITED, §4.2]:** $\delta_q<\tfrac12$. Then $N_j\le4G'(x_j)^2\cdot\#\{q\in C_j\}\cdot\tfrac14+\mathcal E_j=G'(x_j)^2n^{\rm off}_j+\mathcal E_j$.
- **(I1) [ARGUED; not proved]: local on-line excess.** For every cell $C_j$ that contains an off-line ordinate,
  $$
  \sum_{\gamma\in C_j\ \text{on}}(\gamma-x_j)^2\ \ge\ (1+\eta)\,n^{\rm off}_j\cdot\tfrac14\qquad\text{for some }\eta>0\text{ with }(1+\eta)(1-\epsilon_j)^2>1+\mathcal E_j/(G'(x_j)^2 n^{\rm off}_j).
  $$
- **(I0) [HEURISTIC; refuted in the lattice model by Lemma 4.10 below].** The cell $C_j$ has length about $\pi/T$, the node density being $T/\pi$ (2.4(i)), while
  the on-line ordinates near height $\gamma$ have mean density $\frac1{2\pi}\log\frac\gamma{2\pi}$ (Riemann–von
  Mangoldt with §4.2). So the *average* number of on-line zeros per cell near $\gamma_q$ is
  $\bar n_j\approx\frac{1}{2T}\log\frac{\gamma_q}{2\pi}$. With $\gamma_q>3\cdot10^{12}$ (§4.2), this is
  $\bar n_j>13.4/T$ (since $\tfrac12\log(3\cdot10^{12}/2\pi)\approx13.4$).

  If the on-line ordinates in $C_j$ were spread over the cell, then $\sum(\gamma-x_j)^2\approx\bar n_jh_j^2/12$, about
  $\frac{\log(\gamma_q/2\pi)}{2T}\cdot\frac{\pi^2}{12T^2}$. This exceeds $n^{\rm off}_j/4$ by a large factor as long as
  $T^3\ll\frac{\pi^2}{6}\log\frac{\gamma_q}{2\pi}$, *provided* $n^{\rm off}_j$ is bounded. Nothing localises this:
  the density bounds of §4.2 are averages, and any cell that contains a quartet has $n^{\rm off}_j\ge1$ (R163_490
  fix 6; the same non-localisation as (I1-a)). Moreover the computation uses the linearisation outside its range
  (Remark 4.7a).

**Where the argument is not a proof (stated exactly).** (I1) is a statement about the on-line zeros *in one specific
cell*, and two things are unproved.
- **(I1-a) Local distribution of on-line zeros.** Unconditionally, on-line zeros are known in every interval
  $[R,R+R^{27/82+\varepsilon}]$ (Karatsuba; CITED). They are not known in intervals of length $O(1)$ near a given
  height, and their clustering near a point is not controlled (Montgomery's small gaps go the wrong way). The density
  bounds of §4.2 are averages and do not localise to a single cell.
- **(I1-b) The window is free.** $F$ is a minimiser and may put its nodes at on-line zeros. $G$ has $T/\pi$ zeros per
  unit length against $\frac1{2\pi}\log\frac{\gamma}{2\pi}$ ordinates, so it can annihilate a fraction
  $\min(1,2T/\log\frac{\gamma}{2\pi})$ of the on-line ordinates near $\gamma_q$. Hence (I1) **can hold only if**
  $$
  T_c<\tfrac12\log\frac{\gamma_q}{2\pi}-C\qquad\text{for the off-line ordinate }\gamma_q\text{ inside a cone.}
  \tag{I1-T}
  $$
  Nothing in §§2–4.7 bounds $T_c$ from above in terms of the heights of the off-line zeros. The only lower bound known
  is $T_c>0.8047$.

So the precise inequality the attempt relies on is **(I1)**, and its necessary part is **(I1-T)**: *the first contact
occurs before the window at which the witness can absorb the on-line zeros adjacent to the cone.*

**Remark 4.8a ($(\star_{\rm cell})$ is RH at the witness; circular, E1). PROVED** (the circularity identity; the margin
sentence is labelled separately). Under ¬RH the witness satisfies the
exact identity $\sum_j(P_j-N_j)=0$ (§4.7 is an identity). So "$(\star_{\rm cell})$ at the witness" is literally the
negation of the existence of the witness, i.e. (Prop 4.0) $(\star_{\rm cell})\Leftrightarrow\mathrm{RH}$. It is
*not* a non-restating inequality unless proved for a class of $G$ strictly larger than witnesses, using data that $M_m$
lacks; no such class is named. Likewise (I1) with a fixed margin $\eta>0$ is a per-window margin, and at a true witness
no margin exists: at the witness the bottom is exactly $0$, so no fixed margin $\eta$ exists at $T_c$ (PROVED); for
$T\ge T_0(\varepsilon)$, moreover, $\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon)T})$ (Paper 48 `thm:M`(b), PROVED-CITED,
record). Any proof through
estimates with slack is code M. Only an identity-level mechanism could work, and none is offered.

**Lemma 4.10 (lattice-model detection threshold). PROVED-CITED** (R163_402 Thm 4 and Cor 5; re-derived in R163_490 §1).
Model: (M1) localisation $\widehat F(z)=G(z-\gamma)\pm G(-z-\gamma)$ with cross terms dropped; (M2) on-line ordinates
an exact lattice $\gamma+(n+\alpha)/\rho$, $\rho=\frac1{2\pi}\log\frac\gamma{2\pi}$. If $T<\pi\rho$, then
$$
\inf_G\Big[\sum_nG\big(\tfrac{n+\alpha}\rho\big)^2+2\,\mathrm{Re}\,G(-i\delta)^2\Big]<0\iff
S(T,\delta)=\frac{\sinh2\delta T}{2\delta}-T>\pi\rho,
$$
with extremal $b=\sinh\delta u$, $G$ odd, node exactly at $\gamma$ (the cone vertex). Write $L:=\log(\gamma/2\pi)=2\pi\rho$.
Hence $T^*$ is the root of $\sinh(2\delta T)-2\delta T=\delta L$. It satisfies $T^*\le(\tfrac34L/\delta^2)^{1/3}$,
with equality asymptotically only as $\delta T^*\to0$, and $T^*\sim\log(2\delta L)/(2\delta)$ as $\delta L\to\infty$.
It is self-consistent ($T^*<\pi\rho$) iff $\delta L>y_0=2.1773\ldots$ ($\sinh y_0=2y_0$).
*(Proof of the corrections, PROVED: $S(T)>\pi\rho\iff\sinh(2\delta T)-2\delta T>\delta L$; $\sinh y-y\ge y^3/6$ gives
$S\ge\frac23\delta^2T^3$, hence the upper bound; $\sinh y\sim e^y/2$ gives the asymptotic; $T^*<L/2\iff S(L/2)>L/2\iff
\sinh(\delta L)>2\delta L\iff\delta L>y_0$, as $\sinh y-2y$ is negative on $(0,y_0)$ and increasing beyond. The earlier
cubic law "$(1+o(1))$" and threshold $2.45$ were wrong: in the self-consistent regime $\delta T^*$ is not small.)* *(The density-limited branch $T^*\approx\pi\rho+\Delta(\delta)$ for small δ is
HEURISTIC, R163_402 §2–3, and is not part of this lemma.)*

**Corollary 4.10a (the model refutes (I0), and (I1-T) is not sufficient). PROVED** (in the model). At the contact
$T^*$ the extremal is a witness with $\sum_j(P_j-N_j)=0$; all cells $j\ne0$ have $N_j=0$, $P_j\ge0$, so
$P_0-N_0\le0$ and $(\star_{\rm cell})$ fails in the quartet's cell. The refutation of (I0) does not depend on where $T^*$ lies relative to the range of (I0). The model witness exists for
every $\delta\in(y_0/L,\tfrac12)$ and $(\star_{\rm cell})$ fails in its cell. For fixed $\delta$ and large $L$ the
contact lies **inside** that range ($T^{*3}=O(\log^3L)$), where (I0) predicted success. So (I0) is refuted a
fortiori. (I1-T) holds at the contact ($T^*<\pi\rho$), so (I1-T) is necessary but not sufficient, and regime (α) of
§4.9 is empty in the model.

### 4.9 An attempt at (I1-T) from the arithmetic. ARGUED; it fails at the step named

The idea is that a first contact caused by an off-line zero at height $\gamma_q$ should occur only once the window can
resolve that zero, i.e. at $T\gtrsim\frac{1}{2\delta_q}\log\log\gamma_q$. This is the heuristic scale on which
$e^{2T\delta_q}$ (Lemma 3.2) overtakes the local on-line density $\log\gamma_q$. If that held, the contact would come
**after** the scale $\tfrac12\log\gamma_q$ only when $\frac1{\delta_q}\log\log\gamma_q>\log\gamma_q$, that is, for
$\delta_q<\log\log\gamma_q/\log\gamma_q$. These are exactly the zeros closest to the line, which the zero-free region
does not exclude. In that regime (I1-T) fails, and the light-cone negativity is uncompensated in its own cell. The
argument therefore splits:
- (α) zeros with $\delta_q\ge\log\log\gamma_q/\log\gamma_q$, where (I1-T) is heuristically consistent; but (I1-a)
  remains unproved, and in the lattice model this regime is **empty** (Cor 4.10a);
- (β) zeros with $\delta_q<\log\log\gamma_q/\log\gamma_q$, where (I1-T) is heuristically *false*, so
  $(\star_{\rm cell})$ cannot be the mechanism.

Every step from "should occur only once" onward is a heuristic about where $\lambda^{\rm W}_T$ first vanishes. No
inequality of §§2–4.7 controls it. This is W2: the margin $\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon)T})$ for $T\ge T_0(\varepsilon)$ (Paper
48, `thm:M`(b), PROVED-CITED, record) leaves no quantitative room in which to locate $T_c$ by estimates. **This is the step at which the closure
fails.**

**Remark 4.8 (where integrality and the Euler product entered).** Integrality of $\log\mathbb N$ and the exact $\Lambda$
entered through (1.1) (the explicit formula), 4.5 and 4.6, all of which are identities. The Euler product entered
through $\delta<\tfrac12$ and the zero-density bounds (§4.2). It entered nowhere in the step $(\star_{\rm cell})$ that would carry the
sign. So the chain violates specification S4 of Paper 48 exactly at $(\star_{\rm cell})$. This is the precise location of the gap.

### 4.11 What the closing step cannot use. Negative results of record (R163_801, R163_802, R163_901, R163_601/701/702, R163_1001, R164)

This section records, with labels, the inputs that a proof of $(\star_{\rm cell})$ is now known **not** to be able to rest on.
All references are to project files (record); the proofs there were not re-audited here except where said. Nothing below
changes the label of any line of §§1–4.10.

**(a) The node-pair system carries no new information (R163_801).**
- *Collapse.* **PROVED-CITED** (R163_801 Thm 1). The matrix $[W(H_a,H_b)]_{a,b\in X}$ of the node tests $\widehat H_x=G/(z-x)$ is the Loewner
  (divided-difference) matrix of the single function $\Omega(x)=W(F,G/(z-x))$, with $\Omega|_X\equiv0$ and $\Omega'|_X=d$. Hence
  $[W(H_a,H_b)]=\mathrm{diag}(d_x)$: every rank or positivity property of the system is a property of the node-weight vector $d$,
  which is $\delta$-blind to first order (§4.4). The system is the kernel equation (§4.6) tested on $\{H_x\}$ and nothing more.
- *Interpolation identity.* **PROVED-CITED** for $F\in C^1_c(I_T)$, **ARGUED** at the witness (R163_801 Thm 3; the approximation
  step is that of Lemma 3.0). For $\mathrm{Im}\,x>\tfrac12$,
  $$\sum_\rho\frac{G(t_\rho)^2}{t_\rho-x}=C_T(x)-i\,G(x)^2\,\mathcal T_T(x),\qquad \mathcal T_T(x)=\sum_{\log n\ge2T}\Lambda(n)\,n^{-\frac12+ix},$$
  with $C_T$ the Cauchy transform of $\sigma_TG^2$ plus the polar pair. $C_T$ is holomorphic off $\mathbb R$ (except at $\tfrac i2$), so
  **every off-line residue $G(t_q)^2$ is carried by the tail** $G^2\mathcal T_T$, i.e. by $\Lambda(n)$ with $n\ge e^{2T}$; on $X$ the tail
  vanishes identically (R163_801 Cor 3.1). Consequently no evaluation of the system on the node set reaches $\mathrm{Re}\,G(t_q)^2$.
- *Loewner split.* **PROVED-CITED** (R163_801 Prop 4). $L_{\rm on}+L_{\rm off}=\mathrm{diag}(d)$ on $X$ with $L_{\rm on}\succ0$ on finite sets;
  this is the quadrature 2.4(iii) rewritten and yields no sign on any quartet. Rank/finite-span arguments do not separate $M_m$
  (Prop 4.1 there), whose prime side differs from ζ's exactly by the non-atomic density $\beta_m(u)=\sum_j4\cos(\gamma_ju)\cosh(\delta_ju)$
  on $(-2T,2T)$ (Thm 5 there). The only atomic consequence (Prop 5.1 there, a local count with budget $V_T$) carries no sign.

*What this excludes:* any closing step phrased as rank, positivity, or finite-span of Gram/Hankel data on the Gauss nodes, and any
evaluation of (3.1) on $X$.

**(b) Selberg-map invariant regions (R163_802). NO-GO.**
- **Lemma D (one-sided perturbations). PROVED-CITED**, unconditional. If $\nu\ge0$ is nonzero with $\sum\nu(n)n^{-1/2}<\infty$, then
  $\Lambda\pm\nu\notin\bigcap_T\mathcal P_T$ (the window form acquires an almost-periodic absolutely continuous spectral part of mean zero,
  of either sign, which a localised test detects).
- **Theorem U (rigidity in the summable class). PROVED-CITED**, under RH. If $a=\Lambda+d$ with $\sum|d(n)|n^{-1/2}<\infty$ and
  $a\in\bigcap_T\mathcal P_T$, then $d=0$.
- *Consequence.* Every $K\subset\bigcap_T\mathcal P_T$ satisfies $K\cap(\Lambda+\ell^1(n^{-1/2}))=\{\Lambda\}$. Since $\zeta\cdot\exp(G)$ with $G$ an
  absolutely convergent Dirichlet series at $\sigma\ge\tfrac12$ (no constant term) has $N=e^{G(1)}x+O(1)$, **no Beurling-regularity condition
  $N_b=\rho x+O(x^\theta)$, for any $\theta\ge0$ and any $\rho$, and no order condition $b\lessgtr1$, defines a Selberg-invariant $K\subset\bigcap_T\mathcal P_T$**
  (R163_802 §3; order cones collapse to $\{\Lambda\}$ by the exact sign flip, Prop O there). The Selberg fixed point attracts every closed
  invariant region (Fact 3 there), so the route restates "C ⇒ $b\equiv1$ up to non-summable junk", which is RH-strength.

*What this excludes:* any convex/invariant-region certificate for $(\star_{\rm cell})$ built from Selberg's identity together with
integer-count regularity or order conditions on $b=\exp_*(a/\log)$.

**(c) Window and local data cannot prove $(\star_{\rm cell})$ (R163_901 v2; audit R163_991: correct with fixes, applied).**
- **Prop 1.1 (window locality). PROVED-CITED.** Witness, nodes and first contact of any configuration depend only on its window
  functional on $PW_{T_0}$-products. **Prop 1.2. PROVED-CITED** for *balanced* integer configurations ($\gg R\log R$ distinct on-line
  ordinates, §4.1; the audit found that T5.1 uses balance, so the hypothesis was added). **Thm 1.3 (collapse). PROVED-CITED.** The R163_801 §6
  question ("integer configuration with ζ's window functional and an (A-loc)-violating witness") is equivalent to ¬RH at window scale, with ζ
  itself the realiser (balance holds for ζ by Levinson/Conrey); integrality does no work in it.
- **Theorem F (window-agreeing integer falsifier).** For every $N_0$ there is $f_t=\zeta+t\,g$, $g(s)=\sum_{m>R}c(m)(m/\sqrt M)^{-s}$ built
  from a self-dual lattice measure with a spectral and spatial hole at $0$ (Lemma 2.1 there, **PROVED-CITED**; a finite-lattice instance of
  the classical infinite-dimensionality of the FE solution space over non-integral frequencies: Bochner 1951, Kahane–Mandelbrojt 1958,
  Hecke), such that $\pi^{-s/2}\Gamma(\tfrac s2)f_t(s)$ satisfies ζ's exact functional equation with ζ's pole and real coefficients, the zeros
  of $f_t$ have positive integer multiplicities with the symmetry $\rho\mapsto1-\bar\rho$ (trivially: it is a genuine zero set), the prime side
  $-f_t'/f_t$ is atomic **on a discrete semigroup with irrational generators — not on $\log\mathbb N$, not on prime powers** — and
  $W^{f_t}_T=W^\zeta_T$ exactly for $T\le\tfrac12\log\lambda_1$ ($\lambda_1=m_1/\sqrt M>N_0$ the first new frequency), and for $|t|$ large
  $f_t$ has an off-line zero and a finite first contact $T_c(f_t)\le\tfrac12\log\lambda_1+\varepsilon$. Items 1–4 of Thm F are **PROVED-CITED**
  (Riemann's theta argument on the self-dual measure; the Weil/Barner explicit formula, which uses no Euler product; frequency list and $A=0$
  case fixed per R163_991). Variant F′ (prime side on logs of integers — not prime powers — up to the contact) is **ARGUED** (dimension count;
  coefficient formula valid at the minimal $n_0$ only).
- **Cor F, $(\star_{\rm cell})$ clause. CORRECT given witness existence (ARGUED).** If $f_t$ has a first-contact witness, then $(\star_{\rm cell})$ fails
  there (Rem 4.8a identity plus one off-line ordinate; no balance). Witness existence for $f_t$ transfers the argument of R163_501 (compact
  resolvent, monotonicity, continuity, real-rootedness; Lemma 3.0 adapted to a disc containing zeros with $\sigma>1$): **ARGUED**, not re-proved.
- **Cor F, (A-loc) clause. ARGUED, with an open balance gap.** The failure of (A-loc) at $f_t$'s witness goes through Prop 1.2, hence through
  balance: $f_t$ must have more distinct on-line zeros in $(-R,R)$ than the witness's density $\tfrac{2T_c}{\pi}R+o(R)$ allows $G$ to absorb.
  For a generalised Dirichlet series without Euler product no on-line abundance result is on record (for DH/Epstein only $\gg R$). **OPEN.**
- **§3 meta-statement, three clauses.** Over the inputs: integer multiplicities, the zero-side identity, ζ's $\Gamma$-factor, polar term and
  functional equation, atomicity of the prime side, real coefficients, the prime side on $|u|<2T_0$ with $T_0<T_c$, and every structure of
  R163_401/603/801 except balance —
  (i) **no such argument proves Row D** ($W_T\succeq0$ for all $T$): **PROVED-CITED, unconditional** (Thm F.4 alone);
  (ii) **no such argument proves $(\star_{\rm cell})$ at the witness**: **CORRECT given witness existence for $f_t$ (ARGUED)**;
  (iii) no such argument proves (A-loc) at the witness: **NOT PROVED** (ARGUED; needs balance of $f_t$, which is moreover itself an input of §4.1/T5.1).
- **Separators.** Hamburger rigidity (R163_113) is the only separator of ζ from $\{f_t\}$ *among the listed inputs*, not the only one. Not listed,
  and separating: (a) the Euler product / prime-power support of $-\zeta'/\zeta$ ($\log\mathbb N$-support is the weak form; R163_114: equivalent to RH
  for the exchange; F′ has it only below the contact, generically); in tail form, the Euler product of $-\zeta'/\zeta$ above the window, $\mathcal T_X$, $X=e^{2T_c}$ (R163_801 Cor 3.1; (TC) in R164_000);
  (b) BF$_\theta^{\rm disc}$ for $\theta\le\frac13$ (R163_803, R163_1001 Thm O.4). Both are global (neither is a window statement).
  *Removed in v7:* on-line abundance (Levinson/Conrey) — not a separator: Bombieri–Hejhal (Duke 1995; R163_602 F2, PROVED-CITED) gives DH-type
  combinations with 100 % of zeros on the line (conditionally) and infinitely many off it; it is still an input of balance (§4.1), not a separator.
  Riemann–Siegel / approximate-functional-equation structure of $Z(t)$ (R163_603 §2) — not a separator: it is functional-equation-only data, and
  $f_\chi$ has its own real Hardy function and AFE (R163_603 L2.1, R163_1001).

*Status of (c).* Audited (R163_991). Its use in this memo is as a constraint on the shape of a proof: $(\star_{\rm cell})$ cannot be proved from the
inputs listed in the boxed gap, given witness existence for $f_t$ (ARGUED); any proof must bring in one of the candidate separators (a)–(b) above
(Hamburger rigidity enters only as identification, §4.11(e)), each a property of ζ at every level. The caveat of R163_991 §4 applies: the phase-163 integrality-defect programme (R163_102,
R163_803) hypothesises integrality *together with* $\log\mathbb N$-support (R163_114), which $f_t$ lacks; (c) excludes only its atomic abstraction.

**(d) Local Weil positivity (R163_601, R163_701, R163_702).**
- **Exact cell decomposition. PROVED-CITED** (R163_601 Thm 1; also re-derived in outline here). With a frequency localiser $\psi$ and
  $\varepsilon L<\pi$: $\mathfrak a_T(F)=\sum_{k\in\mathbb Z}\mathfrak a_{T+\varepsilon}(\psi_k*F)$, $\|F\|^2=\sum_k\|\psi_k*F\|^2$, each $\psi_k*F\in\mathrm{Loc}_{T+\varepsilon}(kL)$,
  **with no cross terms**. This replaces the node cells of §4.7 (which are not values of the form, Rem 3a there) by cells that are.
- **$P_{\rm loc}$ family ⟺ D. PROVED-CITED** (R163_601 Cor 2). $D_{T+\varepsilon}\Rightarrow P_{\rm loc}(L\mathbb Z,T+\varepsilon)\Rightarrow D_T$; hence
  $\{P_{\rm loc}(kL,T')\}_{k,T'}\Leftrightarrow\mathrm D\Leftrightarrow\mathrm{RH}$, and $P_{\rm loc}$ at the witness is the smoothed, non-strict
  $(\star_{\rm cell})$ ($P_k\ge N_k$, Cor 3 there). Margin inheritance (Prop 4 there, via Theorem M(b), record): the local bottoms are doubly
  exponentially small somewhere on the lattice, so no proof with slack uniform in $\gamma$ exists (code M).
- **Sub-Landau ⇒ near-RH. Core inequality PROVED-CITED, tail bookkeeping ARGUED** (R163_701 Thm B). If $P_{\rm loc}(\gamma,T')$ holds for all
  $\gamma$ and all $T'\le\tfrac12\log(\gamma/2\pi)-C'$, then every locally dominant zero has $\beta-\tfrac12\le(1+o(1))\log\log\gamma/\log\gamma$.
  Conversely (Thm A there, conditional on a local lower frame) a zero-free region of width $\eta\lesssim1/\log\gamma$ gives sub-Landau $P_{\rm loc}$.
  So the sub-Landau half of $P_{\rm loc}$ is already quasi-RH strength and is not a soft input.
- **Supra-Landau: the $K_H$ obstruction. PROVED-CITED** (R163_702 Thm B). For every $\gamma$, $T'$, $H$, the subspace
  $K_H\subset\mathrm{Loc}_{T'}(\gamma)$ of tests with $\widehat F=0$ at all verified ordinates $|\gamma_\rho|\le H$ has finite codimension, and on $K_H$ the
  form **equals the tail** $\sum_{|\gamma_\rho|>H}$. Hence verification $\mathrm V(H)$ plus tail decay and counting never give exact $P_{\rm loc}$ in a
  supra-Landau cell; at $T\approx T_1(H)=\tfrac12\log\tfrac H{2\pi}-C-\varepsilon$ ($\approx13.45-C$ at $H=3\cdot10^{12}$) every verified cell is
  supra-Landau (Thm C there). Upward induction in $T$ is killed by $M_m$ (§3 there).

*What this excludes:* any closing step that proves $(\star_{\rm cell})$ cell by cell with uniform slack; any reduction of the supra-Landau cells
to numerical verification; and any use of sub-Landau positivity as a cheap hypothesis.

**(e) Global integrality of frequencies (R163_1001).** PROVED given Lemma 1.2 there (off-line zeros of $f_\chi$, PROVED-CITED:
Kaczorowski–Kulas 2007, Saias–Weingartner 2009, page-level caveat).
- **Falsifier $f_\chi$** (Lemma 1.1 there, PROVED): $f_\chi=\alpha L(s,\chi)+\bar\alpha L(s,\bar\chi)$, $\chi$ the even cubic character mod 7,
  $\alpha^2=\bar\varepsilon_\chi$: integer frequencies, real 7-periodic coefficients, ζ's $\Gamma(s/2)$, exact FE at conductor 7, entire of order 1,
  2-periodic modular theta; off-line zeros.
- **Theorem O.** At conductor 1, $\{\mathrm{Fr}\subset\mathbb N\}\cap\{\zeta\text{'s FE}\}=\{c\zeta\}$ (Hamburger); for $q>1$ the class contains $f_\chi$.
  So every statement "global integrality + data shared with $f_t$ or $f_\chi$ ⟹ $(\star_{\rm cell})$" is false or has $\{c\zeta\}$ as its only model;
  integrality enters only as identification, after which the sign must come from the values $\Lambda(n)$. With Euler at $q>1$: degree-one
  Dirichlet $L$-functions, a mechanism would be GRH in degree one uniform in χ.
- **Wall W3′** (integer-frequency blindness; grid §3): integrality is identification or sign-blind. Deformation $f_t\to\zeta$ (Thm A.3, E1),
  theta periodicity (Prop B.2/Thm B.3) and a window Hamburger theorem (Thm C.1–C.3) are NO-GO.
- **Tail formulation.** What is left is the Euler product above the window: the tail theorem (TC) of R164_000 (phase 164), built on R163_801 Thm 3/Cor 3.1.
  (TC) at the witness is RH (Rem 4.8a); phase 164 does not claim it is weaker, only that its hypothesis is the one not excluded.

**(f) Phase 164: the tail and the identification theorem (R164_101, R164_102, R164_401, R164_190).**
- **(KZ) is E1** (R164_101 Thm E1, PROVED): the hybrid Euler–Hadamard cut at the window edge turns the kernel equation into a pairing of
  $\theta'_{X}$ against $PW_T$-products that depends on the zero multiset alone; row D ⟺ the Toeplitz compression of $-\theta'_{X(T)}$ to
  $PW_T$ is $\succeq0$ for every $T$, which is RH. Prop D (PROVED): the deletion has literally ζ's $Z_X$ and a negative window form.
- **Positive tail DEAD** (R164_102 Thm A, PROVED): with ζ's window and a positive tail measure there are members with a zero at any
  $\beta+i\gamma$ (paid by a double pole, so no FE). Thm L (Landau–Pringsheim): positivity is zero-blind and pole-sensitive.
- **Thm R** (R164_401, PROVED; review audit R164_190): if $f=\int\lambda^{-s}dN$, $N=N_\zeta$ on $[1,X)$ for some $X>1$, $N\ge0$ off $\mathbb N$,
  and $\pi^{-s/2}\Gamma(s/2)f$ has ζ's FE with its two simple poles and finite order, then $f=\zeta$ (sinc annihilation of the self-dual
  theta measure). Hence the witness class of O164.101 is $\{\zeta\}$ and O164.101 ⟺ ¬RH (Cor R.2); $f_t$ has negative coefficients
  off $\mathbb N$ for every $t\ne0$ (Cor R.3).
- **Identification theorem** (R164_190, synthesis of the cited statements): every global property that separates ζ from all falsifiers
  (Hamburger, Thm O, Thm R) identifies ζ; the others (on-line abundance, Riemann–Siegel, families, positive tail without FE,
  integrality without FE above $\theta=\frac13$) do not separate. So $(\star_{\rm cell})$ must be proved for ζ individually from the comb /
  explicit formula at all heights, equivalently (TC). The only remaining non-identification content is BF$_\theta^{\rm disc}$, $\theta\le\frac13$,
  off the Witt lattice (O164.201a, ARGUED that it must be off-lattice; R164_201 Theorem L, R164_291).
- **Rounds 3–4 of phase 164** (labels from R164_190 rounds 3–4):
  - **Thm SA** (R164_501, PROVED): every test $\ge0$ on $\mathbb R$ annihilated by the kernel equation is $\hat H\hat H^\#$ with $H\in E_c$
    (finite-dimensional cone); the nodes have critical density $T_c/\pi$, so the sinc step of Thm R has no room at the witness; output
    = Rem 4.8a (E1). Cor SA.1 (polynomial ladder) PROVED, via the direct route $W(z\hat\Phi)=W(\Phi,z^2\Phi)=0$ (R164_491 F5).
  - **Prop 4** (R164_501, PROVED): $\Psi_y=G^2\,y/(z^2+y^2)\ge0$, $\sum_\rho\Psi_y(t_\rho)=\mathfrak A_y-G(iy)^2\mathcal T(iy)$,
    $\mathcal T(iy)=\sum_{\log n\ge2T}\Lambda(n)n^{-1/2-y}>0$: Λ at all heights enters with a sign, but as an identity with off-line weight
    $y/\gamma_q^2$; fails for $f_t$, $f_\chi$; the windowed $M_m$ satisfies the tail-sign inequality.
  - **Drop-term principle** (R164_601 Thm 3.1, CONFIRMED): any inequality obtained by discarding the signed tail holds for ζ's true zeros
    whatever they are; it excludes a quartet only with an independent lower bound, which is $(\star_{\rm cell})$ weighted by $K$
    (Thm 3.2; O164.601.1 OPEN). O164.501.1 CLOSED (test exists: dlVP on $G^2$, Prop 2.1); Thm 3.3: W2/M cap $\frac12-\delta_q\le c/\log\gamma_q$.
    The review's uncertainty reading is refuted (Prop 1.2).
  - **Spectral invariants = window data** (R164_502 L1, CONFIRMED): $A_T$ depends only on $\check\sigma$ on $(-2T,2T)$; determinant, heat
    trace and moments DEAD (L3 ARGUED; L4, L5, L6 PROVED). R164_503: the positive direction of BF$_\theta^{\rm disc}$ below $\frac13$ is
    ≥ RH + quadratic GRH; prime-side rounding capped at $x^{1/2}$ (ARGUED). **Every route returns to $(\star_{\rm cell})$.**

**(g) Phase 165 (critical interlacing; labels from R165_190, review audit ).**
- **Det+ and the $T_c$ bracket** (R165_101, PROVED with the clustering caveat; constants not rederived by the review): if ¬RH at
  $\rho^*$, then $\lambda^W_T<0$ for all $T\ge\tau(\rho^*)$, with $\tau(\rho^*)\le T_L(\gamma^*)+\tfrac12\log(\pi/2)+o(1)$,
  $\tfrac12\log(\pi/2)=0.2258$. Proof idea: $h=\Xi\cdot R/Q^k$ ($\Xi$ divided by its quartet factor $Q$, $R=z^2-c$ with $c$ chosen for the phase);
  $F$ = inverse transform of $h$ (the Riemann–Pólya kernel $\Phi$, decay $\exp(-\pi e^{2|u|})$) truncated to $[-T,T]$. Hence
  $$0.8047<T_c\le\min_\rho\tau(\rho).$$
  Caveat (Obstruction O.1): the bound uses the reduced coefficient $|\Xi^{(k)}|$ at $\rho^*$, which enters log-log; other off-line zeros may cluster there.
- **Det− negative** (R165_102, PROVED given the cited zero count): uniform-in-γ (Det−) is false when $\delta^*\Lambda^*$ is large (Thm 1:
  sub-Landau detection $T_{\rm det}$ for a dominant zero); by Cor 2(c) the contact is decided by $\min_\rho T_{\rm det}(\rho)$ over all off-line
  zeros, not by the lowest one; false also for $M_m$. Residues O102.1, O102.2, O701.1–3. Route to $(\star_{\rm cell})$ DEAD.
- **Exact phase identity** (R165_201 Thm 2, Cor 2.2, CONFIRMED): $\arg G\equiv\arg Z_{\rm on}+\pi[\omega(E^+)-\omega(E^-)]+\Psi_{\rm out}$ and
  $4\,\mathrm{Re}\,G(t_q)^2=4|G(t_q)|^2\cos2(\Phi_Z\pm\pi\omega(E)+\Psi_{\rm out})$, ω the harmonic measure at $\gamma+i\delta$. The sign variable
  is $\omega(E)$, the position of each node within its cell at first contact; at the witness this is Rem 4.8a.
  Interlacing does **not** push the quartet out of the cone (Thm 3(a), PROVED: $G=\sin\pi\rho z$, $Z=\cos\pi\rho z$ interlace at critical
  density, $G(x_0-i\delta)^2=-\sinh^2\pi\rho\delta<0$); "contact forces (EC)" is false (R165_202). D.16-γ answered negatively.
- **Node flow** (R165_202, CONFIRMED; E1): no jumps in $T$; the witness background is real-rooted at every $T$ where $\lambda_T$ is simple;
  quadrature with $w_x\ge0$ and the Cauchy identity at every $T$; consecutive nodes are separated by a charged on-line zero. Node
  monotonicity and parity simplicity OPEN.

**(h) Phase 166 (ω-closure, rounds 6–7; labels from R166_190, review audit ).** Base: the wall dichotomy (R166_190 §0) —
zero side alone is killed by $M_m$, the prime window alone by $f_t$, class properties identify ζ; the only datum proper to ζ is the exact
duality $Z_\zeta\leftrightarrow$ atomic $\Lambda$ on $\log\mathbb N$ at all heights.
- **Jet hierarchy** (R166_201 Thm 1.1, Thm 1.3, Cor 1.4, PROVED): with $Q=G/(z-x_0)$, $t_q-x_0=re^{-i\psi}$ and $E$ the phase of the other
  nodes, the quartet term of $S^{(k)}(x_0)$ is $2k!\,|Q(t_q)|^2r^{1-k}\cos(2E+(k-1)\psi)$. The node weights $d=S'$ are $k=1$ and blind to
  $\psi$; the kernel equation is $k=0$ (window and zero data at once); $\mathrm{Re}\,G(t_q)^2=|Q|^2r^2\cos(2E-2\psi)$ is the formal level
  $k=-1$, below every node jet, so no polynomial function of node data reads its sign. This is the exact form of the δ-blindness of §4.4.
  Prop 2.2: at the lattice extremal the sine channel $-\mathrm{Im}\,G(t_q)^2/\delta$ is $O(\delta^2)$ (dormant). ω(E) is thus a **global
  phase** of $G$ at $t_q$ (harmonic measure of the node set, R165_201 Thm 2), not a local node datum.
- **No pole singularity at nodes** (R166_101 Thm 2.1, PROVED): $|G(t)/(t-x_0)|\le e^{T|\delta|}\|G'\|_\infty$; the quartet weighs in $d_x$
  like two on-line zeros; δ enters only at second order. Mechanism DEAD (E1).
- **Rough-zeta split** (R166_103 B1–B2, PROVED; tool): $\mathcal T_X=\mathcal T^{\rm det}_X+\mathcal T^{\rm new}_X$, $\mathcal T^{\rm det}_X$ a
  finite window sum holomorphic in $\mathrm{Im}\,x>-\frac12$, $\mathcal T^{\rm new}_X=-\zeta_{\ge X}'/\zeta_{\ge X}$ with $\zeta_{\ge X}$ the zeta
  of the $X$-rough integers; it carries every off-line residue and separates $f_t,f_\chi,M_m$. Its positivity is zero-blind without FE
  (Thm A), identification with FE (Cor R.1), one-sided = Landau (E1). Falsifier $P_{a,c}=\zeta\,[1+c\cosh((s-\frac12)\log a)]$ (θ−1>0,
  exact FE, off-line zeros) kills moments of θ−1 (G1–G2).
- **Five mechanisms DEAD with proof:** node-weight singularity (R166_101, E1); exchange flow in $s$ (R166_102, W2/M; bounds of the same
  order $\frac12\log\log(1/s)$, lower bound ARGUED); free mechanism α/β/γ (R166_103: $f_t$/$M_m$; Thm A/Cor R.1/Landau; $P_{a,c}$);
  sine–cosine coupling and T-flow (R166_201, E1); parity coupling (R166_202, vacuous/E1; Thm 3 $W_T(F^{\rm ev})+W_T(F^{\rm odd})=4W_{T/2}(\Phi)$;
  OS-2 closed negative; residue O202.1: $T_e=T_o$ OPEN).
- **Requirements for any proof of $(\star_{\rm cell})$** (R166_190, Cierre): it must (i) be global in the node set $X$ (not local in jets),
  (ii) couple $X$ with the atomic prime side beyond the window, and (iii) not reduce to (1.1) on a test. No mechanism of record meets (i)–(iii).

**(i) Phases 166 (rounds 9–12) and 167 (labels from R166_190 rounds 9–12 and R167_190 after the  R167_291, review audits ).**
- **Survey of families P/Q** (R166_400–405, ≈230 mechanisms of phases 0–166): no mechanism meets (i)–(iii). The 2-of-3 mechanisms split into
  family P = {i,ii} (15; quadratic in $F$, linear in Λ, the two faces of the explicit formula; all fall by E1) and family Q = {ii,iii} (30;
  degree zero in $F$, non-linear in Λ); {i,iii} is empty. The three P↔Q joins are decided: P7+Q25 is a repeat of E70_11/12 (R166_502; new
  lemma: the non-integer comb of $V*V$ is the cross part $\sum_{p\ne q}V_p*V_q$), P1/P5+Q1 is tautological/E1 (R166_601: the rough-zeta
  identity is equivalent to $\zeta(\rho^*)=0$; Legendre's Φ is zero-blind), and "Q + global phase" is excluded by Thm A.
- **Theorem A (R166_501, PROVED): (iii) alone ⟹ (ii).** A mechanism is $(H,S)$ with ζ ∈ H proved without RH and $H\Rightarrow S$; (iii) means
  $f_t\notin H$ and $M_m\notin H$. Since $f_t$ shares everything inside the window (Lem A.1) and $M_m$ shares the on-line zeros and the atomic
  side, $H$ must use Λ beyond the window. Requirement (i) is not used, so "{i,iii} empty" is a theorem. Every functional of $(X,\Gamma_{\rm on})$,
  the phase of R165_201 Thm 2 included, is also satisfied by $M_m$ with its own witness. Transport of Thm R to $\eta=Z-Q_X$: gap by Q0 (PROVED),
  no room at type $2T_c$ without hypothesis (Q), and the exact obstruction B(5) (PROVED). Non-linearity in Λ: ARGUED (O166.501.1).
  Requirements become **(G)** $S$ a non-constant invariant of the witness, global in $X$ (degree 0 allowed), and **(N)** $H$ uses Λ beyond the window.
- **Beurling frontier** (R166_701, R166_702): θ = 0 rigidity T3/T4 PROVED (adding a prime $q$ keeps θ = 0 iff $R$ is a bounded coboundary for
  $x\mapsto x/q$; ℕ plus any real $q>1$ is never θ = 0; novelty to be checked against Hilberdink 2012); C1/C2 OPEN; position-tuned systems
  DEAD (Lemma PT, exponent ≥ (1−θ)/2 ≥ 1/3 ARGUED). As routes to D both fail (N): the count $N$ is blind to zeros.
- **Cell 7C** (R166_801): the second moment over translates is Parseval of the first moment; $M_m$ passes with its witness; DEAD (E1/$f_t$).
- **Circularity theorem** (R166_802, PROVED for single tests and power-size families; ARGUED for arbitrary non-linear $B$, O166.802.1): for one
  test the witness only imposes ${\rm Tail}_K\le\mathfrak A_K-Q_K+S$; excluding it needs the lower bound, which by the true identity is
  ${\rm OnLine}_K<0$, false. The Λ-sum twisted by $n^{i\gamma_q}$ has exponent exactly $\Theta-\frac12$ at every fixed frequency (Landau, MV 15.3);
  zero-free sieve bounds give only $\Theta\le1$. No inequality on Λ true for ζ excludes the witness unless it controls the Λ-sum at frequency
  $\gamma_q$ beyond $X$ with the exact strength of the absence of the zero. (N) sharpens to **(N′)**: Λ beyond the window with zero-localisation strength (= localized RH).
- **The exact target (WS\*)** (R167_101, Thm A identity, Lemma Q, Thm B given (Dom$_\theta$), Thm C, Prop W): with $w=(e^{-i\gamma_q\cdot}g)*\check k$,
  $$\mathrm{Re}\sum_{n\le Y}\Lambda(n)n^{-\frac12+i\gamma_q}w(\log n)<(1-\theta)\,c_\Theta|G(t_q)|^2|k(-i\delta_q)|-E_K/4,$$
  the sum over all of $[1,Y]$ (not only the tail), given (Dom$_\theta$) (O167.101.1; small-$y$ regime O167.101.2). At the witness it is a
  polylogarithmic bound at a single scale, of RH quality. **Status (R167_190 after R167_291):** unreachable by the sieve class (Thm B′: the
  cos-modulated $b_\theta$ with $0\le b_\theta\le\Lambda$ obeys every sieve upper bound and reaches $X^{1/2}$; Theorem S: the same tools hold in
  discrete Beurling systems, where DMV/Zhang falsify RH); its scale-uniform form is equivalent to a zero-free statement (Thm C, Landau); at a
  single scale it is an evaluation of the explicit formula (Thm E). Lemma K (Kronecker resonance) is demoted to an observation; (WS\*) is not
  "false uniformly". **Final requirements: (G) + (N′).** $(\star_{\rm cell})$ stays OPEN.

**Summary of §4.11.** The closing step cannot use: Gram/Hankel/rank data on the nodes (a); Selberg-invariant convex regions defined by
integer-count regularity (b); any finite window of the prime side together with the structural properties listed in (c) — audited
R163_991, given witness existence for $f_t$; cell-wise positivity with uniform slack, or verification in supra-Landau cells (d). Global integrality of frequencies is identification or sign-blind (e). By (f), every class property that separates ζ identifies it (R164_190): what remains is a proof of $(\star_{\rm cell})$ for $\zeta$
individually, from the comb / explicit formula at all heights (equivalently (TC)), which is the boxed gap; BF$_\theta^{\rm disc}$ with $\theta\le\frac13$
off the Witt lattice (O164.201a) is the only non-identification residue. On-line abundance (Bombieri–Hejhal,
R163_602 F2) and Riemann–Siegel structure (FE-only, shared by $f_\chi$) are no longer on the list (v7).

---

## §5 Consequences: the deduction if §4 holds

Assume $(\star_{\rm cell})$ for every cell containing an off-line ordinate (for instance via (I1)+(I2), Rem 4.7a notwithstanding). Then:
1. **No witness.** Suppose ¬RH. §2.3 gives $T_c>0.8047$, and §2.4(ii) gives a nonzero real, parity-definite,
   real-rooted $F\in E_c$. §4.7 and $(\star_{\rm cell})$ give $W_{T_c}(F)=\sum_j(P_j-N_j)>0$, contradicting
   $F\in E_c$. So ¬RH is false. (PROVED, given $(\star_{\rm cell})$.)
2. **RH.** Hence RH holds. Equivalently: CL holds (Proposition 4.0), so there is no first contact, so $T_c=\infty$, so
   $\lambda^{\rm W}_T>0$ for every $T$.
3. **Row D.** Theorem 1.2 gives $W_T\ge0$ for all $T$, i.e. D. Paper 47 `lem:contA` and Proposition 4.0 also give
   $\mathfrak a_T\ge0$ on $\mathcal P_T$ for every $T$, the primitive form of D. In fact the bottom is strictly
   positive at every window: under RH, $W_T(F)=0$ with $F\in\mathcal D_T$ arbitrary (complex) implies $F=0$
   (the general fact proved in Proposition 4.0, ⇐), so $\ker W_T=0$, and the bottom is attained.
4. **The A–C carrier.** Rows A–C are closed on the declared carrier (record). With D, the four-row programme is
   complete on that carrier.

The chain is: $(\star_{\rm cell})\Rightarrow\mathrm{CL}\Leftrightarrow\mathrm{RH}\Leftrightarrow\mathrm D$. The
implications ⇒ and ⇔ are PROVED. $(\star_{\rm cell})$ is ARGUED and not established (§4.8–4.9).

---

## §6 Falsifier checks. PROVED-CITED (record, Paper 48 `tab:falsifiers`); numerical entries uncertified as marked

For each model the table gives what it shares and the first line of §§3–4 that fails for it. A line marked "holds" is
class-level; this is why §§3–4.7 alone cannot give the sign.

| model | (1.1) zero-side identity | 3.1–3.4 cone geometry | 4.1 balance | 4.2 $\delta<\frac12$ | 4.4–4.7 | first failing line |
|---|---|---|---|---|---|---|
| Davenport–Heilbronn | holds (own Γ, own coefficients) | holds | holds | fails globally (zeros in $\sigma>1$), but DH also has zeros with $\tfrac12<\beta<1$, e.g. $\rho\approx0.8085+85.699i$ (Spira 1994; Balanzario–Sánchez-Ortiz 2007; cited), $\delta\approx0.31<\tfrac12$ | hold | **none identified.** In a cell containing such a quartet every line of §§3–4.8, including (I2), holds verbatim; whether $(\star_{\rm cell})$ holds there is the same open question. **Not separated** (F3:DH, W3) |
| Epstein ($h>1$) | holds | holds | holds | fails globally, but off-line zeros with $\tfrac12<\sigma<1$ exist | hold | **none identified**; same as DH. Not separated (T2: no axiom beyond A1–A6 at the sign step) |
| Beurling–DMV, Broucke $\zeta_\theta$ | **fails**: no functional equation about $\frac12$, so no Weil form centred at $\frac12$ with a zero-side identity; $\zeta_\theta$ has a continuous prime measure | — | — | (for $\zeta_\theta$: $\delta=\theta/2$ relative to its own line) | — | **§1 / (1.1)**. Caveat: this separation comes from the functional equation, not from integrality. Since (I1) does not use integrality, nothing in the chain reproduces the DMV/$\zeta_\theta$ separation by integer multiplicities (Remark 4.8) |
| two-atom Type I curve ($s_2^c\approx0.99977$; uncertified) | **fails**: the detuned form is $W^\zeta_T+(s_2-1)v_2\,\mathrm{Re}\,c_F(\log2)$, not the zero sum of any function | — | — | — | — | **§4.6**: the coefficient vector differs from $(\Lambda(n))$ at $n=2$ (Selberg Lemma S at $N=2$). The contacts at $T\approx0.55$–$0.61<\frac12\log5$ are below the range of CL |
| deletion $\Lambda\mathbf 1_{n\ge5}$ | **fails**: $\zeta_a$ has the zeros of $\zeta$ but its window form is $W_T+\sum_{n<5}v_n\mathrm{Re}\,c_F(\log n)$, not a zero sum | — | — | — | — | **(1.1) / §4.6**. Its first contact in $[0.4608,0.60]$ (record) is invisible to the cone picture, which needs (1.1) |
| $M_m$ ($\xi$ times $m$ rational off-line quartets) | holds | holds | holds | can hold (choose $\delta<\frac12$) | hold | **§4.8 (I1)**. $M_m$ has the on-line zeros of $\zeta$ and finitely many quartets, and it has a first contact with a witness (Paper 48 `tab:falsifiers`); by the argument of Rem 4.8a, $(\star_{\rm cell})$ fails in some cell of that witness. So **(I1) cannot follow from the on-line zero set, the off-line positions and $\delta<\frac12$ alone**. Any proof of (I1) must use the atomic arithmetic side, which $M_m$ lacks |
| $f_t=\zeta+tg$ (R163_901 v2, audited R163_991) | holds (ζ's Γ_R, pole, real coefficients; genuine integer zero set) | holds | **OPEN** for $f_t$ (no on-line abundance result for a non-Euler generalised Dirichlet series) | can fail (zeros with $\sigma>1$ not excluded) but an off-line zero with finite contact exists | hold | **§4.8 $(\star_{\rm cell})$**, given witness existence (ARGUED). Prime side atomic and equal to ζ's for $T\le\frac12\log\lambda_1$, any prescribed length, but on a semigroup with irrational generators (not $\log\mathbb N$). Strictly better falsifier than DH (own Γ, own coefficients) and $M_m$ (non-atomic). Separated from ζ only by global properties: Hamburger rigidity, $\log\mathbb N$/prime-power support (R163_114), on-line abundance, Riemann–Siegel structure |
| $\Lambda\chi_2$ (ζ's Γ and pole, χ₂ comb) | **fails** (hybrid: no matching zero side) | — | — | — | — | (1.1). Its contact $T_c\le0.38$ (record) is below CL's range |
| $\kappa$-models | fail (1.1) | — | — | — | — | (1.1) / §4.6 |

**Verdict of the battery.**
- §§3–4.7 pass every model in the precise sense that they *hold* for each model with a zero-side identity, as a
  structure statement should.
- The sign step $(\star_{\rm cell})$ is **not** separated from DH or Epstein. (An earlier version claimed separation
  by (I2); that claim was false and is withdrawn, R163_490 §4: both have off-line zeros with $\delta<\tfrac12$, and
  their zeros in $\sigma>1$ are irrelevant to such cells.) Beurling–DMV/$\zeta_\theta$ are excluded only by the
  functional equation, not by integrality (S4 violated).
- From $M_m$, (I1) is **not** separated. So the closing argument is incomplete exactly at $(\star_{\rm cell})$, and §6 confirms that
  this is the location of the gap rather than a defect of the falsifiers.
- From $f_t$ (given witness existence, ARGUED), $(\star_{\rm cell})$ is not separated by ζ's FE, pole, real coefficients, integer multiplicities,
  atomicity and any finite window of the prime side; the balance line (4.1) is OPEN for $f_t$, so the (A-loc) version of this statement is ARGUED only.

---

## §7 Ledger

| step | label |
|---|---|
| Thm 1.2 (D ⟺ RH), Thm 1.3 (zero-side identity) | PROVED-CITED (⇒: Paper 45 Thms 11.3, 8.4; ⇐: Thm 1.3 = Paper 47 `lem:roughEF` + Lemma 3.0) |
| 2.1 positivity on $T\le\frac12\log5$ | PROVED-CITED (Paper 47 `thm:log5W`/`thm:log5A`, certified computation) |
| 2.2 monotonicity, continuity, attainment | PROVED-CITED (Paper 47 `lem:monoT`, `lem:contT`, `lem:contA`; Bombieri Thms 3, 5) |
| 2.3 existence of a first contact $T_c>0.8047$ under ¬RH | PROVED |
| 2.4 real-rooted witness, Gauss nodes | PROVED (R163_501; R(d) after repair; $w_x=d_x/\lvert\widehat F'\rvert^2$); node identity 2.4(iv) PROVED-CITED (R162_2202, record); Q0 PROVED (R163_502); block version 2.4(iii′) PROVED; (Q) OPEN, unused |
| 2.5 Type I/II split | PROVED-CITED (R162_1701 Thm 1); not used |
| Lemma 3.0 absolute convergence | PROVED |
| Lemma 3.1 factorisation; $W=P_++4\sum\mathrm{Re}\,G(t_q)^2$ | PROVED |
| Lemma 3.2 Poisson majorant | PROVED-CITED (Koosis; Levin) |
| Lemma 3.3 exact phase; Lemma 3.4 light cone with errors $E=\delta S_0+R$, Lorentzian form | PROVED |
| Prop 4.0 CL ⟺ RH | PROVED (⇒ audited R163_501; ⇐ via simple-zero proportion) |
| 4.1 balance, Cor 4.1 | PROVED |
| 4.2 $\delta<\frac12$, density bounds, $\sum\delta^2\ll R/\log R$ (R163_502 Δ), verification height | PROVED-CITED |
| 4.3 Poisson bound on $N_-$ | PROVED |
| 4.4 node tests absorb the cone | PROVED under $M_2r<2(\sqrt2-1)\lvert G'(x_0)\rvert$; δ-blindness remark HEURISTIC |
| 4.5 quadrature on $\overline N^{\mathcal D}$ | PROVED (R163_502 Q0); band reading conditional on (Q) |
| 4.6 prime-side kernel equation; finite-vector reduction | PROVED |
| 4.7 cell decomposition (identity) | PROVED |
| Rem 4.7a lower bound on $P_j$ vacuous at cell scale; (I1) generically void | HEURISTIC |
| Rem 4.8a $(\star_{\rm cell})\Leftrightarrow$ RH at witness | PROVED (circularity identity, E1); margin sentence PROVED-CITED (Paper 48 `thm:M`(b), $T\ge T_0(\varepsilon)$, record) |
| (I0) counting heuristic | HEURISTIC; REFUTED in lattice model (Cor 4.10a) |
| Lemma 4.10 lattice detection threshold | PROVED-CITED (R163_402 Thm 4, Cor 5; re-derived R163_490); asymptotics and threshold $y_0$ corrected and PROVED here (R163_590 D1) |
| Cor 4.10a $(\star_{\rm cell})$ fails in model; (I1-T) not sufficient | PROVED (in the model) |
| 4.8 $(\star_{\rm cell})$, possible route: (I1) [and (I1-T)] | **ARGUED: not established** |
| 4.9 derivation of (I1-T) from the arithmetic | **ARGUED: fails (W2; regime β)** |
| §5 deduction $(\star_{\rm cell})\Rightarrow$ RH ⟹ D | PROVED (conditional on 4.8) |
| §6 falsifier lines | PROVED-CITED (record, Paper 48 `tab:falsifiers`; numerical entries uncertified); DH/Epstein separation claim WITHDRAWN (not separated) |
| §4.11(a) node-pair collapse, interpolation identity, tail carries off-line residues | PROVED-CITED (R163_801; Thm 3 ARGUED at the witness) |
| §4.11(b) Selberg-invariant regions: Lemma D, Thm U, NO-GO | PROVED-CITED (R163_802) |
| §4.11(c) $f_t$ family, Thm F; window data cannot prove Row D (unconditional) nor $(\star_{\rm cell})$ at the witness (given witness existence) | Thm F PROVED-CITED (R163_901 v2, audited R163_991); $(\star_{\rm cell})$ clause CORRECT given witness existence (ARGUED); (A-loc) clause ARGUED, balance of $f_t$ OPEN |
| §4.11(d) exact cell decomposition; $P_{\rm loc}$ family ⟺ D; sub-Landau ⇒ near-RH; $K_H$ obstruction | PROVED-CITED (R163_601, R163_702); R163_701 Thm B tail ARGUED |
| §4.11(e) $f_\chi$, Thm O, W3′ (integrality = identification or sign-blind) | PROVED-CITED (R163_1001, given Lemma 1.2 there) |

**Status of row D: OPEN.** New in this memo: the light-cone lemma (3.3–3.4) with explicit errors and its Lorentzian
form; the absolute-convergence lemma 3.0 for (1.1) on $\mathcal D_T$; the δ-blindness of node tests (4.4); the cell
decomposition (4.7); and the identification of $(\star_{\rm cell})$ as the exact missing step ((I1-T) is necessary but not sufficient, Cor 4.10a), with $M_m$ as the falsifier showing that it needs the atomic arithmetic side.
