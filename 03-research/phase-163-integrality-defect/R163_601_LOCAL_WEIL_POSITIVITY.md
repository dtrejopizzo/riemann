# R163_601 — Local Weil positivity $P_{\rm loc}(\gamma,T)$: exact localisation, margin inheritance, twisted prime sums

* Pure mathematics; no numerics. Nothing outside this file was edited. No label of record moves.*
*Inputs: R163_401 (status table, §3–§4, $(\star_{\rm cell})$, Rem 4.8a), R163_402 (Thm 4, Landau ceiling), R163_490,
Paper 48 (walls W1–W12, codes, Condition S1–S12, Theorem M).*
*Corpus check (rule ).* Localised Weil forms already occur in the record: Paper 07 (localised Weil
detector; `prop:dichotomy`: a *uniform* transfer of $\lambda_{\min}$ from localisations to the full form ⟺ RH);
R160_S1_SURVEY l.52 (" $A_\Phi-P_F$ is $\mathfrak a_T$ on a height-localised subspace"); and, written in parallel,
R163_602 (localisation formula for $g\cos\gamma u$, trivial range $4.16e^T\le\log(\gamma/2\pi)-O(1)$, NO-GOs for
Selberg/sieve/Levinson–Conrey). This memo **does not repeat** R163_602; it cites it. What is new here: the
*exact* multiplier partition (Theorem 1: zero cross terms), the sandwich $D_{T+\varepsilon}\Rightarrow P_{\rm loc}\Rightarrow D_T$
(Cor 2), the smoothed cell identity replacing §4.7 of R163_401 (Cor 3), margin inheritance (Prop 4, the
answer to "is it Theorem M?"), and the falsifier analysis (§5).

**Labels.** PROVED (full proof here); PROVED-CITED (reference given; *record* = project file, not re-audited);
ARGUED (argument given, the unproved step named); OPEN.

## Outcome first

| # | statement | label |
|---|---|---|
| L0 | $\mathfrak a_T$ on complex $F$ splits as $\mathfrak a_T(\mathrm{Re}F)+\mathfrak a_T(\mathrm{Im}F)$; primitivity splits too | PROVED |
| Def | localiser $\psi$, class $\mathrm{Loc}_{T'}(\gamma)$, statement $P_{\rm loc}(\gamma,T')$ — no reference to $W$, nodes or witnesses | definition |
| Thm 1 | **exact localisation**: $\mathfrak a_T(F)=\sum_{k\in\mathbb Z}\mathfrak a_{T+\varepsilon}(\psi_k*F)$, $\|F\|^2=\sum_k\|\psi_k*F\|^2$, $\psi_k*F\in\mathrm{Loc}_{T+\varepsilon}(kL)$, whenever $\varepsilon L<\pi$; **no cross terms** | PROVED |
| Cor 2 | sandwich $D_{T+\varepsilon}\Rightarrow P_{\rm loc}(L\mathbb Z,T+\varepsilon)\Rightarrow D_T$; hence $\{P_{\rm loc}\}\Leftrightarrow$ D $\Leftrightarrow$ RH | PROVED |
| Cor 3 | smoothed cell identity at the witness; $P_{\rm loc}\Rightarrow$ smoothed $(\star_{\rm cell})$ in the form $P_k\ge N_k$; strictness only past the contact | PROVED |
| Rem 3a | why frequency localisation is exact and the node cells of R163_401 §4.7 are not values of the form | PROVED |
| Prop 4 | **margin inheritance**: $\inf_k\lambda_{\rm loc}(kL,T+\varepsilon)\le\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon')T})$ | PROVED (Thm M(b) record) |
| Prop 5 | $P_{\rm loc}$ unconditional (i) for $T'\le\frac12\log5$, (ii) on concentrated tests in the double-log range | PROVED / PROVED-CITED (R163_602 §2.1) |
| 3.x | three regimes (trivial / sub-Landau / supra-Landau); supra-Landau = Montgomery–Vaughan diagonal range exceeded = $\alpha>1$ in pair correlation | PROVED (exponent bookkeeping); comparison ARGUED |
| §4 | explicit formula for $\mathrm{Loc}$; exact arithmetic statement $(\mathrm H_{\rm loc})\Leftrightarrow P_{\rm loc}$ | PROVED |
| §4.3 | literature comparison (MV, Selberg density, Goldston–Gonek, Montgomery, Goldston–Montgomery) | citations FROM MEMORY, flagged |
| §5 | DH, Epstein, $M_m$, $\Xi_a$: $P_{\rm loc}$ **fails** (Thm 1 is class-level + their own Weil criterion) | PROVED for $M_m$; PROVED-CITED/ARGUED for DH, Epstein |
| §5 | Beurling–DMV, $\zeta_\theta$: Thm 1 holds for the ½-centred multiplier form; failure of $P_{\rm loc}$ there | ARGUED |
| $P_{\rm loc}$ for ζ, all $(\gamma,T)$ | | **OPEN** (⟺ RH) |
| Row D | | **OPEN** |

**Verdict in one paragraph.** The circularity of $(\star_{\rm cell})$ *at the witness* is escaped: $P_{\rm loc}(\gamma,T')$ is
a positivity statement on an explicit infinite-dimensional subspace of tests defined by a frequency localiser,
true unconditionally in two ranges, and Theorem 1 reassembles it into D **with zero cross terms**. But the escape is
only from E1-at-the-witness to E1-as-a-family: the family $\{P_{\rm loc}(kL,T')\}_{k,T'}$ is *equivalent* to D (Cor 2;
the W1 clause "per-window law quantified over all $T$"), and Prop 4 shows that it inherits Theorem M: the local
bottoms are doubly-exponentially small somewhere on the lattice, so no proof with slack uniform in $\gamma$ exists
(code M). The arithmetic input that would prove it (§4.2) is pointwise control of *long* twisted prime sums,
length $e^{2T'}\ge\gamma$, which is past the Montgomery–Vaughan diagonal range and, through the explicit formula,
is the local zero sum itself (W12). Row D stays OPEN.

---

## §1 Definitions

Notation of R163_401 §1.1: $\widehat F(z)=\int F(t)e^{izt}dt$, $\mathfrak a_T(F)=\frac1{2\pi}\int\sigma_T|\widehat F|^2$,
$\sigma_T=m-\sum_{\log n<2T}v_n\cos(\tau\log n)$, $v_n=2\Lambda(n)n^{-1/2}$, $A(F)=\widehat F(-i/2)$, $B(F)=\widehat F(i/2)$,
$\mathcal P_T=\{A=B=0\}\subset L^2(I_T)$, $\mathcal D_T$ the form domain, $\|F\|^2=\int|F|^2=\frac1{2\pi}\int|\widehat F|^2$.
Row D: $\forall T$, $\mathfrak a_T\ge0$ on $\mathcal P_T\cap\mathcal D_T$ (R163_401 Def 1.1, equivalent form).

**Lemma 0 (complex tests). PROVED.** For $F=u+iv$, $u,v$ real: $\mathfrak a_T(F)=\mathfrak a_T(u)+\mathfrak a_T(v)$, and
$F\in\mathcal P_T\iff u,v\in\mathcal P_T$.
*Proof.* $|\widehat F|^2=|\widehat u|^2+|\widehat v|^2+2\,\mathrm{Im}(\widehat u\,\overline{\widehat v})$. Since $u,v$ are real,
$\widehat u(-\tau)=\overline{\widehat u(\tau)}$, so $\mathrm{Im}(\widehat u\overline{\widehat v})$ is odd, while $\sigma_T$ is even:
the cross integral vanishes. $A(u),A(v),B(u),B(v)$ are real, so $A(F)=0\iff A(u)=A(v)=0$; same for $B$. ∎
So row D may be tested on complex primitive tests.

**Localiser.** Fix $\varepsilon>0$, $L>0$ with $\varepsilon L<\pi$, and $\psi\in C_c^\infty(-\varepsilon,\varepsilon)$ with
$\|\psi\|_2^2=L/2\pi$. Put $\psi_\gamma(t)=\psi(t)e^{-i\gamma t}$, so $\widehat{\psi_\gamma}(z)=\widehat\psi(z-\gamma)$, an entire
function with $|\widehat\psi(x+iy)|\le C_N e^{\varepsilon|y|}(1+|x|)^{-N}$ for every $N$ (Paley–Wiener–Schwartz).

**Definition (local class and local positivity).** For $T'>\varepsilon$ and $\gamma\in\mathbb R$,
$$
\mathrm{Loc}_{T'}(\gamma)=\mathrm{Loc}_{T'}(\gamma;\psi):=\{\psi_\gamma*H:\ H\in\mathcal P_{T'-\varepsilon}\cap\mathcal D_{T'-\varepsilon}\},
\qquad
P_{\rm loc}(\gamma,T'):\quad \mathfrak a_{T'}(F)\ge0\ \ \forall F\in\mathrm{Loc}_{T'}(\gamma).
$$
- *Concentration (quantitative).* $\widehat F=\widehat\psi(\cdot-\gamma)\widehat H$, so for $F\in\mathrm{Loc}_{T'}(\gamma)$ and $R>0$,
  $\frac1{2\pi}\int_{|\tau-\gamma|>R}|\widehat F|^2\le s_\psi(R)^2\|H\|^2$, $s_\psi(R):=\sup_{|s|>R}|\widehat\psi(s)|\le C_N(1+R)^{-N}$;
  and $|\widehat F(\tau)|\le\sqrt{2(T'-\varepsilon)}\,\|H\|\,|\widehat\psi(\tau-\gamma)|$. The spectral mass of $F$ sits in a cell of
  length $\asymp1/\varepsilon$ around $\gamma$; with $\varepsilon=\theta T'$, the cell length is $\asymp1/T'$ and $L<\pi/(\theta T')$.
- $\mathrm{Loc}_{T'}(\gamma)\subset\mathcal P_{T'}\cap\mathcal D_{T'}$: support adds, $\widehat F(\pm i/2)=\widehat\psi(\pm i/2-\gamma)\widehat H(\pm i/2)=0$,
  and $|\widehat F|\le\|\widehat\psi\|_\infty|\widehat H|$ on $\mathbb R$.
- The definition involves neither $W$, nor nodes, nor a witness, nor ζ: it is a named class (requirement of the
  boxed gap in R163_401). It is an infinite-dimensional closed-range subspace (image of an injective bounded map;
  injective because $\widehat\psi\not\equiv0$ is entire), not a cone of minimisers.

---

## §2 Exact localisation (task item 1)

**Theorem 1 (exact localisation, no cross terms). PROVED.** Let $\varepsilon L<\pi$ and $\psi$ as above; put
$F_k:=\psi_{kL}*F$. For every $F\in\mathcal P_T\cap\mathcal D_T$:
$$
\text{(a)}\ \ \sum_{k\in\mathbb Z}|\widehat\psi(z-kL)\,|^{2}_{\#}:=\sum_k\widehat\psi(z-kL)\widehat\psi^{\#}(z-kL)\equiv1\ \ (z\in\mathbb C);\qquad
\text{(b)}\ \ \|F\|^2=\sum_k\|F_k\|^2;\qquad
\text{(c)}\ \ \mathfrak a_T(F)=\sum_{k\in\mathbb Z}\mathfrak a_{T+\varepsilon}(F_k),
$$
with $F_k\in\mathrm{Loc}_{T+\varepsilon}(kL)$, the series converging absolutely.

*Proof.*
1. *Partition on $\mathbb R$.* $h:=|\widehat\psi|^2=\widehat{\psi*\tilde\psi}$ with $\tilde\psi(t)=\overline{\psi(-t)}$, and
   $\mathrm{supp}(\psi*\tilde\psi)\subset[-2\varepsilon,2\varepsilon]$. Poisson summation:
   $\sum_kh(\tau-kL)=\frac{2\pi}{L}\sum_m(\psi*\tilde\psi)(2\pi m/L)e^{2\pi im\tau/L}$. Since $2\varepsilon<2\pi/L$, only $m=0$ survives,
   giving $\frac{2\pi}L\|\psi\|^2=1$.
2. *Extension to $\mathbb C$.* $\Sigma(z):=\sum_k\widehat\psi(z-kL)\widehat\psi^\#(z-kL)$ converges locally uniformly by the
   Paley–Wiener–Schwartz bound, so it is entire; on $\mathbb R$ it equals $\sum_kh(\tau-kL)=1$. By the identity theorem
   $\Sigma\equiv1$. This is (a).
3. (b): Plancherel and step 1, with Tonelli ($h\ge0$).
4. (c): $F_k$ has support in $I_{T+\varepsilon}$ and $\widehat F_k=\widehat F\,\widehat\psi(\cdot-kL)$. For $2T\le\log n<2T+2\varepsilon$,
   $\frac1{2\pi}\int|\widehat F|^2\cos(\tau\log n)\,d\tau=\mathrm{Re}\,c_F(\log n)=0$ because $\mathrm{supp}\,c_F\subset[-2T,2T]$; hence
   $\int\sigma_{T+\varepsilon}|\widehat F|^2=\int\sigma_T|\widehat F|^2$. Now $|\sigma_{T+\varepsilon}(\tau)|\le\log(2+|\tau|)+C_{T,\varepsilon}$, so
   $\sigma_{T+\varepsilon}|\widehat F|^2\in L^1$; the partial sums of $\sum_kh(\tau-kL)$ lie in $[0,1]$; dominated convergence gives
   $\sum_k\frac1{2\pi}\int\sigma_{T+\varepsilon}|\widehat F|^2h(\cdot-kL)=\mathfrak a_T(F)$, i.e. $\sum_k\mathfrak a_{T+\varepsilon}(F_k)=\mathfrak a_T(F)$.
   Absolute convergence: $\sum_k|\mathfrak a_{T+\varepsilon}(F_k)|\le\frac1{2\pi}\int|\sigma_{T+\varepsilon}||\widehat F|^2<\infty$.
5. $F_k\in\mathrm{Loc}_{T+\varepsilon}(kL)$ with $H=F$ (§1). ∎

**Corollary 2 (sandwich). PROVED.** For every $T>0$ and $\varepsilon L<\pi$:
$$
\big[\mathfrak a_{T+\varepsilon}\ge0\text{ on }\mathcal P_{T+\varepsilon}\big]\ \Longrightarrow\ \big[P_{\rm loc}(kL,T+\varepsilon)\ \forall k\in\mathbb Z\big]\ \Longrightarrow\ \big[\mathfrak a_T\ge0\text{ on }\mathcal P_T\big].
$$
Hence (with Lemma 0 and R163_401 Thm 1.2) **D ⟺ RH ⟺ $P_{\rm loc}(kL,T')$ for all $k$ and all $T'>\varepsilon$**, for any one fixed admissible
$(\varepsilon,L,\psi)$; also with $\varepsilon=\theta T'$, $L=\pi(1-\eta)/(\theta T')$ chosen per window.
*Proof.* Left arrow: $\mathrm{Loc}_{T+\varepsilon}(kL)\subset\mathcal P_{T+\varepsilon}$. Right arrow: Theorem 1(c), each summand $\ge0$. ∎
In particular $P_{\rm loc}$ on the lattice of heights $L\mathbb Z$ at window $T+\varepsilon$ implies $(\star_{\rm cell})$ at
any witness *vacuously* (via RH, no witness). The *direct* relation is Cor 3.

**Corollary 3 (smoothed cell identity at the witness; relation to $(\star_{\rm cell})$). PROVED.** Let $F$ be a real-rooted
primitive witness at the primitive contact $T_*$ (R163_401 §2.3–2.4, $\mathfrak a_{T_*}(F)=0$), $G$ as in R163_401 §3. Put
$\Psi_k(z):=\widehat\psi(z-kL)\widehat\psi^\#(z-kL)$ (entire, $\ge0$ on $\mathbb R$, $\sum_k\Psi_k\equiv1$ on $\mathbb C$). Then, at window $T_*+\varepsilon$,
$$
0=\sum_k\mathfrak a_{T_*+\varepsilon}(F_k),\qquad
\mathfrak a_{T_*+\varepsilon}(F_k)=\underbrace{\sum_{\rho\ \rm on}G(\gamma_\rho)^2\Psi_k(\gamma_\rho)}_{P_k\ \ge0}\;-\;\underbrace{\Big(-\!\!\sum_{\rho\ \rm off}G(t_\rho)^2\Psi_k(t_\rho)\Big)}_{N_k\in\mathbb R}.
$$
$P_{\rm loc}(kL,T_*+\varepsilon)$ is exactly $P_k\ge N_k$: a smoothed $(\star_{\rm cell})$ with **non-strict** inequality.
*Proof.* Theorem 1(c) and R163_401 (1.1) applied to $F_k$ (which is primitive, so $W=\mathfrak a$): $\widehat F_k\widehat F_k^\#=G^2\Psi_k$
(R163_401 Lemma 3.1(b) and multiplicativity of $\#$). Each $\mathfrak a(F_k)$ is real, so $N_k$ is real (sum of the
quartet terms). Absolute convergence: Lemma 3.0 of R163_401 applied to $\widehat F_k$. ∎
*Consequences.* (i) Unlike R163_401 §4.7, every piece $P_k-N_k$ is the value of the form on a *test* in a named class,
so its positivity is a class statement and not a statement about the witness. (ii) At the witness window itself the
non-strict inequalities are *consistent* with $\sum(P_k-N_k)=0$ (all pieces $0$); a contradiction needs a window
$T'>T_*$ where $\lambda^{\rm A}_{T'}<0$. So $P_{\rm loc}$ proves D directly (Cor 2), and the witness is not needed;
this is the honest content of "stronger than $(\star_{\rm cell})$".

**Remark 3a (why the cross terms vanish). PROVED.** $\mathfrak a_T$ is a Fourier multiplier (diagonal in $\tau$); the
only non-diagonal part of $W_T$ is the rank-two polar term $2\mathrm{Re}A\bar B$, and multiplication of $\widehat F$ by an
entire $\widehat\psi$ preserves $A=B=0$. A *quadratic* partition $\sum|\widehat\psi_k|^2=1$ then splits the form exactly;
the price is the window loss $\varepsilon$ with $\varepsilon L<\pi$ (uncertainty: cells of length $\sim1/T'$ cost a fixed
fraction of the window). Localisation in $t$, or with sharp cells $C_j$ (R163_401 §4.7), is not available: sharp
cutoffs $\mathbf 1_{C_j}\widehat F$ are not Paley–Wiener, and the pieces $P_j-N_j$ of §4.7 are sums of zero terms that
are not values of any form. (Paper 07's detector localises with Gaussians, also exactly diagonal, but its claim
is a *uniform* limit, which `prop:dichotomy` there shows to be RH-equivalent; Theorem 1 needs no limit.)

---

## §3 Strength, and Theorem M (task item 2)

**(2a) Not only witnesses.** $\mathrm{Loc}_{T'}(\gamma)$ is an infinite-dimensional subspace containing, e.g., every
$\psi_\gamma*H$ with $H$ an arbitrary primitive test of window $T'-\varepsilon$. It contains a witness only if a witness
happens to be divisible by $\widehat\psi(\cdot-\gamma)$, which (zeros of $\widehat\psi$ being non-real generically) is
non-generic. Individual instances are *proved*:

**Proposition 5 (unconditional instances).**
- (i) PROVED-CITED: $P_{\rm loc}(\gamma,T')$ holds for all $\gamma$ when $T'\le\frac12\log5$ (Paper 47 `thm:log5A`, certified; record),
  since $\mathrm{Loc}_{T'}\subset\mathcal P_{T'}$.
- (ii) PROVED-CITED (R163_602 §2.1, re-checked): pointwise $\sigma_{T'}\ge m-V_{T'}$, $V_{T'}\le4.16e^{T'}$ (Rosser–Schoenfeld
  $\psi(x)<1.04x$, FROM MEMORY, + partial summation), and $m$ is even and increasing in $|\tau|$ with $m(0)=\psi(\frac14)-\log\pi=-\gamma_E-\frac\pi2-3\log2-\log\pi\approx-5.37$
  (PROVED: $\mathrm{Re}\,\psi(x+iy)=\psi(x)+\sum_n y^2/((n+x)((n+x)^2+y^2))$). Hence for $F\in\mathrm{Loc}_{T'}(\gamma)$ whose mass
  fraction $\vartheta$ in $\{|\tau|<\tau_0\}$ satisfies $(1-\vartheta)(m(\tau_0)-V_{T'})\ge\vartheta(V_{T'}+5.37)$, $\mathfrak a_{T'}(F)\ge0$. For $\gamma$ with
  $m(\gamma/2)>4.16e^{T'}+1$ and $s_\psi(\gamma/2)$ small this covers the concentrated part of $\mathrm{Loc}_{T'}(\gamma)$:
  the double-log range $T'\le\log\log\gamma-O(1)$.
  *Gap:* the concentration estimate of §1 is relative to $\|H\|$, not $\|F\|$; elements of $\mathrm{Loc}$ with
  $\widehat H$ small near $\gamma$ are not covered. So (ii) is $P_{\rm loc}$ on a θ-concentrated cone, not on all of $\mathrm{Loc}$.

**(2b) Is it a per-window margin? (Theorem M check.)** $P_{\rm loc}$ asks for $\ge0$, not $\ge c(T)$, so as a
*statement* it is not code M. But proofs are constrained:

**Proposition 4 (margin inheritance). PROVED** (modulo Paper 48 Theorem M(b), record). Let
$\lambda_{\rm loc}(\gamma,T'):=\inf\{\mathfrak a_{T'}(F)/\|F\|^2:\,0\ne F\in\mathrm{Loc}_{T'}(\gamma)\}$. Then for all $T$,
$$
\inf_{k\in\mathbb Z}\lambda_{\rm loc}(kL,T+\varepsilon)\ \le\ \lambda^{\rm A}_T,\qquad\text{so}\qquad \inf_k\lambda_{\rm loc}(kL,T+\varepsilon)\le\exp\!\big(-e^{(2-\varepsilon')T}\big)\ (T\ge T_0(\varepsilon')).
$$
*Proof.* If $\lambda_{\rm loc}(kL,T+\varepsilon)\ge c$ for all $k$, Theorem 1(b),(c) give $\mathfrak a_T(F)=\sum\mathfrak a(F_k)\ge c\sum\|F_k\|^2=c\|F\|^2$
for every $F\in\mathcal P_T$ (terms with $F_k=0$ drop), so $\lambda^{\rm A}_T\ge c$. ∎
*Reading.* Any proof of $P_{\rm loc}$ with slack uniform over the lattice of heights is killed by Theorem M (code M,
S12). Slack depending on $\gamma$ is not excluded: for fixed $T'$ and $\gamma\to\infty$ the concentrated part has bottom
$\gtrsim\log\gamma-4.16e^{T'}$ (Prop 5(ii)). The doubly-exponential smallness must therefore sit at heights where
$\log\gamma$ is not large compared with $e^{T'}$ — ARGUED, more precisely at $\log\gamma\lesssim2T'$ (below).

**(2c) Three regimes. PROVED as bookkeeping; the reading is ARGUED.** For the cell at height $\gamma$, window $T'$:
- *trivial*: $4.16e^{T'}<\log(\gamma/2\pi)-O(1)$; Prop 5(ii), unconditional.
- *sub-Landau*: $T'<\frac12\log(\gamma/2\pi)$, i.e. the prime sums have length $X=e^{2T'}<\gamma/2\pi$. The local on-line ordinates
  have density $\rho=\frac1{2\pi}\log\frac\gamma{2\pi}>T'/\pi$: on the zero side the on-line terms form, in the lattice model, a
  sampling set for $PW_{T'}$ (R163_402 Thm 4: Poisson aliasing vanishes), and $\mathrm{Loc}_{T'}(\gamma)$ with $\varepsilon\asymp T'$
  is effectively $O(1)$-dimensional (Slepian count $\approx 2T'\cdot(\text{cell length})/\pi=O(1)$).
- *supra-Landau*: $T'\ge\frac12\log(\gamma/2\pi)$. $\widehat H$ can vanish at all on-line ordinates of the cell; the local zero
  side can be annihilated and the sign is decided by off-line zeros and by the $\widehat\psi$-tails of remote zeros.
  This is where the small-δ contacts sit (R163_402 §2–3, HEURISTIC) and where R163_401 (I1-T) fails.

---

## §4 The explicit formula for localised tests (task item 3)

**4.1 Identity. PROVED.** Let $F=\psi_\gamma*H\in\mathrm{Loc}_{T'}(\gamma)$ and write $F(t)=e^{-i\gamma t}g(t)$, i.e.
$g=\psi*(e^{i\gamma\cdot}H)$, $\widehat g(s)=\widehat\psi(s)\widehat H(s+\gamma)$. Put $k:=g*\tilde g$ (so $\widehat k=|\widehat g|^2\ge0$, $k(0)=\|g\|^2$,
$\mathrm{supp}\,k\subset[-2T',2T']$, $k(-u)=\overline{k(u)}$). Then $c_F(u)=e^{-i\gamma u}k(u)$ and
$$
\underbrace{\frac1{2\pi}\int m(\gamma+s)\,|\widehat g(s)|^2ds\;-\;2\,\mathrm{Re}\!\!\sum_{n<e^{2T'}}\!\!\Lambda(n)\,n^{-1/2-i\gamma}\,k(\log n)}_{\text{prime/archimedean side}}
\;=\;\mathfrak a_{T'}(F)\;=\;\underbrace{\sum_\rho \widehat k^{\,\flat}(t_\rho-\gamma)}_{\text{zero side}},
$$
where $\widehat k^{\,\flat}:=\widehat g\,\widehat g^{\#}$ (entire; $=|\widehat g|^2$ on $\mathbb R$), $t_\rho=\gamma_\rho-i\delta_\rho$, absolutely convergent.
*Proof.* Left: $\frac1{2\pi}\int\cos(\tau\log n)|\widehat F|^2=\mathrm{Re}\,c_F(\log n)$ and $v_n\mathrm{Re}(n^{-i\gamma}k(\log n))=2\mathrm{Re}(\Lambda(n)n^{-1/2-i\gamma}k(\log n))$;
$|\widehat F(\tau)|^2=|\widehat g(\tau-\gamma)|^2$. Right: R163_401 (1.1) for the primitive $F$, with
$\widehat F\widehat F^\#(z)=\widehat g(z-\gamma)\widehat g^\#(z-\gamma)$; Lemma 3.0 there. ∎
- Zero side: local. $|\widehat k^\flat(t_\rho-\gamma)|\le e^{2\varepsilon\delta_\rho}\cdot$(rapid decay in $|\gamma_\rho-\gamma|\varepsilon$)$\cdot\sup|\widehat H|^2$-type
  bounds (Paley–Wiener–Schwartz for $\widehat\psi$, Lemma 3.2 of R163_401 for $\widehat H$); on-line terms are $\ge0$.
  The mirror ordinates $-\gamma_\rho$ enter at distance $\approx2\gamma$ and are negligible.
- Prime side: a twisted, short-*range* (in $\log n$: $|\log n|<2T'$) prime sum with a positive-definite weight $k$.
  Archimedean side: $\frac1{2\pi}\int m(\gamma+s)|\widehat g|^2=(\log\frac\gamma{2\pi})k(0)\,(1+o(1))$ for concentrated $g$ (Stirling).
  So the trivial balance is $\log(\gamma/2\pi)$ against $2|\sum\Lambda(n)n^{-1/2-i\gamma}k(\log n)|/k(0)$.

**4.2 The exact arithmetic input. PROVED (equivalence).** $P_{\rm loc}(\gamma,T')$ is equivalent to:
$$
(\mathrm H_{\rm loc}(\gamma,T'))\qquad 2\,\mathrm{Re}\sum_{n<e^{2T'}}\Lambda(n)n^{-1/2-i\gamma}k(\log n)\ \le\ \frac1{2\pi}\int m(\gamma+s)\widehat k(s)\,ds
\quad\text{for all }k=g*\tilde g,\ \widehat g=\widehat\psi\cdot\widehat H(\cdot+\gamma),\ H\in\mathcal P_{T'-\varepsilon}.
$$
By Cor 2, $(\mathrm H_{\rm loc})$ on the lattice for all $T'$ ⟺ RH. What a proof needs, by regime:
- trivial range: $\sum\Lambda(n)/\sqrt n\le2.08\sqrt X$ suffices (Prop 5(ii));
- sub-Landau ($X=e^{2T'}<\gamma$): a bound $|\sum_{n<X}\Lambda(n)n^{-1/2-i\gamma}k(\log n)|\le(\frac12-\eta)\log(\gamma/2\pi)k(0)$ **for every
  $\gamma$** and every $k$ in the $O(1)$-dimensional local cone — i.e. pointwise square-root-type cancellation of
  Dirichlet polynomials of length $X<\gamma$ at the single point $\gamma$, with $\eta$ allowed to depend on $\gamma$ (Prop 4);
- supra-Landau ($X\ge\gamma$): the same with $X\ge\gamma$, *no* uniform slack (Prop 4), and by 4.1 the inequality is
  literally the positivity of the local zero sum (W12: identity without sign).

**4.3 Comparison with known results. (All citations FROM MEMORY, flagged; statements ARGUED as comparisons.)**
- *Montgomery–Vaughan mean value theorem* (J. London Math. Soc. 1974, "Hilbert's inequality"): $\int_0^{H}|\sum_{n\le X}a_nn^{-it}|^2dt=\sum|a_n|^2(H+O(n))$.
  With $a_n=\Lambda(n)n^{-1/2}k(\log n)$ the diagonal dominates iff $X\ll H$, i.e. $2T'<\log\gamma$: **the MV diagonal range is
  exactly the sub-Landau range** (PROVED as exponent bookkeeping). It gives the mean square $\asymp\int_0^{2T'}u|k(u)|^2du\le2T'^2k(0)^2$,
  so $(\mathrm H_{\rm loc})$ holds *on average* in $\gamma\in[H,2H]$ when $T'=o(\log H)$, with an exceptional set; higher moments
  (powers of the polynomial, length $X^j\le H$) shrink the exceptional set to measure $\ll H\exp(-c\log^2H/T'^2)$ (ARGUED, standard
  Selberg-type moment method). **Not every $\gamma$**: this is the non-localisation (I1-a) of R163_401 in arithmetic form.
- *Selberg's zero-density estimate* (Titchmarsh 9.19(C)): $N(\sigma,H)\ll H^{1-\frac14(\sigma-\frac12)}\log H$. It bounds the *number*
  of cells where $P_{\rm loc}$ can fail via an off-line zero with $\delta\ge\delta_0$ by $\ll H^{1-\delta_0/4}\log H$ out of $\asymp HT'$ cells.
  $P_{\rm loc}$ needs zero exceptions; density theorems are averages (same as R163_401 §4.2).
- *Goldston–Gonek* (Bull. LMS 2007): under RH, $|S(t)|\le(\frac12+o(1))\log t/\log\log t$. This would give the local frame
  (on-line sampling at cell scale) needed in sub-Landau cells — but assumes RH. Unconditionally only $S(t)=O(\log t)$
  (Backlund/Littlewood) and Selberg's moments of $S$.
- *Montgomery's pair correlation* (Proc. Symp. Pure Math. 24, 1973): under RH, $F(\alpha)$ is computed for $|\alpha|\le1$ from the
  explicit formula with Dirichlet polynomials $\sum\Lambda(n)n^{-1/2-it}$ of length $H^\alpha$, by the MV mean value. Length
  $X=e^{2T'}=\gamma^\alpha$ gives $\alpha=2T'/\log\gamma$: **the Landau ceiling $T'=\frac12\log\gamma$ is $\alpha=1$**, the barrier of
  Montgomery's theorem. The supra-Landau regime is $\alpha>1$, where $F(\alpha)=1$ is conjectural and, by
  *Goldston–Montgomery* (1987, Proc. Conf. Analytic Number Theory, Birkhäuser), equivalent under RH to the variance of primes in
  short intervals. So even the *averaged* version of $(\mathrm H_{\rm loc})$ in the supra-Landau range is beyond known
  methods, and all of them assume RH.
- Conclusion (ARGUED): known unconditional inputs reach $P_{\rm loc}$ only in the trivial range pointwise, and in the
  sub-Landau range on average with exceptions; the supra-Landau range, where Prop 4 places the collapse, needs
  pointwise control of long twisted sums, which by 4.1 is the local zero sum. Consistent with R163_602 §2.2–(c).

---

## §5 Falsifier lines (task item 4)

**Principle. PROVED.** Theorem 1, Cor 2, Cor 3 and Prop 4 use only: the form is a Fourier multiplier $\frac1{2\pi}\int\sigma|\widehat F|^2$
on $L^2(I_T)$ with an even symbol whose prime part has spectrum in $[-2T,2T]$, plus a polar part killed by $\widehat F(\pm i/2)=0$
(or by the model's own polar points). Every model below with a Weil form centred at ½ has this. Hence for each such
model $Z$: $P^Z_{\rm loc}$ (all lattice heights, all $T'$) ⟺ $D^Z$. So $P_{\rm loc}$ **fails** for $Z$ exactly when $D^Z$ fails —
it is never "accidentally true" for a falsifier. The burden of S4 falls on the *proof* of $P_{\rm loc}$, not on the statement.

| model | $P_{\rm loc}$ fails? | where / why | what a proof of $P_{\rm loc}$ must avoid |
|---|---|---|---|
| $M_m$ | **yes, PROVED**: $M_m$ has a first contact and $\lambda^{\rm A}<0$ beyond it (Paper 48 Tab. 1, record), so by Cor 2 some $P^{M_m}_{\rm loc}(kL,T'+\varepsilon)$ fails | by 4.1, $\mathfrak a^{M_m}(F)=\mathfrak a^\zeta(F)+\sum_{q\le m}(\text{quartet terms }\widehat k^\flat(t_q-\gamma))$; the extra terms are local at $\gamma_q$; on the prime side they are non-atomic exponentials $e^{\pm\delta_qu}\cos\gamma_qu$ | any bound on the twisted sums that uses only the on-line zeros, positions of off-line zeros and $\delta<\frac12$ (same as R163_401 §6); must use that ζ's prime side is purely atomic. Caveat: the $\tilde\Lambda$ model (Paper 48 Tab.) shows atomicity + positivity alone do not suffice |
| Davenport–Heilbronn | **yes**, PROVED-CITED modulo Weil's criterion for DH (explicit formula + an off-line zero ⇒ some window negative; Bombieri's argument uses only the explicit formula and the Hadamard product; transfer to DH ARGUED) | ARGUED location: near $\gamma\approx85.70$ ($\delta\approx0.3085$); local density $\rho=\frac1{2\pi}\log\frac{5\gamma}{2\pi}\approx0.67$, $\pi\rho\approx2.1$; δ below the self-consistency threshold $2.45/\log(5\gamma/2\pi)\approx0.58$, so density-limited branch, $T'\approx2.1+\Delta$ (HEURISTIC) | DH's −L′/L coefficients are not supported on prime powers and grow ($\sigma_a>1$); its trivial range is $T'\lesssim(\log\log\gamma)/(2\sigma_a-1)$ — a trivial-range argument is harmless (holds for DH too, and DH fails elsewhere). Any argument in the sub/supra-Landau range must use the Euler product (T2, F3:DH) |
| Epstein ($h>1$) | **yes**, same status as DH | off-line zeros in $\frac12<\sigma<1$ | same; T2: A1–A6 insufficient |
| $\Xi_a$ | **yes**, same mechanism (all zeros off the line) | every cell | functional equation + finite Tate compression insufficient |
| Beurling–DMV | ARGUED: define the ½-centred multiplier form with ζ's $m$ and atoms $v_B$ at $\log n_B$; Thm 1 holds verbatim, so $P^B_{\rm loc}\Leftrightarrow D^B$. There is no zero-side identity (no functional equation about ½), so failure is read on the prime side: near an off-line DMV zero $\beta_B+i\gamma_B$, $\sum\Lambda_B(n)n^{-1/2-i\gamma}k(\log n)$ carries the term $\approx X^{\beta_B-1/2}\widehat k$-weighted, which beats $\log\gamma$ for large $T'$ | the twisted-sum bound must use $\mathcal N\subset\mathbb Z$ (S4); any argument using only $\Lambda_B*1=\log$, $a\ge0$, Chebyshev bounds is F3:DMV |
| $\zeta_\theta$ (Broucke) | ARGUED: zeros on $\mathrm{Re}\,s=\frac{1+\theta}2$, i.e. $\delta=\theta/2$ relative to ½; the ½-centred twisted sums grow like $X^{\theta/2}$ near its ordinates, so $P_{\rm loc}$ fails for $T'$ beyond $\approx\theta^{-1}\log\log\gamma$ | separated only by integer prime multiplicities (Paper 48); every analytic obstruction (Prop `analyticnogo`) is blind |

**Verdict of the battery.** $P_{\rm loc}$ is correctly *false* for every falsifier with a Weil form (PROVED for $M_m$
via Cor 2; via Weil's criterion for DH, Epstein, $\Xi_a$). Nothing in §§1–3 separates ζ: Theorem 1 and Prop 4 are
class-level (as structure statements should be). The proved instances (Prop 5) hold for the falsifiers too in
their own trivial ranges, which is harmless. The separating input must enter in $(\mathrm H_{\rm loc})$ in the
sub/supra-Landau range and must use integrality and the Euler product (S4, T2); none is offered.

---

## §6 Ledger and specification check

| step | label |
|---|---|
| Lemma 0 complex splitting | PROVED |
| Def of $\mathrm{Loc}_{T'}(\gamma)$, $P_{\rm loc}$; inclusion in $\mathcal P_{T'}$; concentration bound | PROVED |
| Thm 1 exact localisation, partition $\sum\Psi_k\equiv1$ on $\mathbb C$ | PROVED |
| Cor 2 sandwich; $\{P_{\rm loc}\}\Leftrightarrow$ D ⟺ RH | PROVED (Thm 1.2 of R163_401 PROVED-CITED) |
| Cor 3 smoothed cell identity; $P_{\rm loc}\Rightarrow P_k\ge N_k$ (non-strict) | PROVED |
| Rem 3a cross terms vanish exactly; sharp/node cells are not form values | PROVED |
| Prop 4 margin inheritance | PROVED (Theorem M(b) record) |
| Prop 5 (i) $T'\le\frac12\log5$; (ii) double-log range on concentrated cone | PROVED-CITED (Paper 47; R163_602 §2.1) |
| §3(2c) regimes; MV range = sub-Landau; Landau ceiling = $\alpha=1$ | PROVED (bookkeeping); readings ARGUED |
| 4.1 localised explicit formula; 4.2 $(\mathrm H_{\rm loc})\Leftrightarrow P_{\rm loc}$ | PROVED |
| 4.3 literature comparison | ARGUED; citations FROM MEMORY |
| §5 $M_m$ fails $P_{\rm loc}$ | PROVED (record: $M_m$ first contact) |
| §5 DH, Epstein, $\Xi_a$ fail $P_{\rm loc}$ | PROVED-CITED modulo Weil criterion for those functions (ARGUED transfer) |
| §5 DMV, $\zeta_\theta$ | ARGUED |
| $P_{\rm loc}(\gamma,T')$ for ζ in sub-/supra-Landau range | **OPEN** |
| Row D | **OPEN** |

**Paper 48 specification.** S1 (λ=0 non-perturbative): $P_{\rm loc}$ does not use the contact at all — neutral. S5:
each $P_{\rm loc}(\gamma,T')$ is per-window without gap (allowed), but the family "for all $T'$" is a per-window law
quantified over all $T$ (W1/E1) — **violated as a closing statement**; acceptable only as an intermediate if some
*single-height* or *finite-range* instance is proved that is strictly weaker than RH and still implies something new.
S11: an instance $P_{\rm loc}(\gamma,T')$ couples primes and archimedean place at one height; Prop 5 shows the coupling is
unconditional only in the trivial range. S12: Prop 4 forbids uniform numerical slack. S4: not met (§5).

**New, reusable:** Theorem 1 (exact, cross-term-free frequency localisation of the primitive Weil form, with the
uncertainty constraint $\varepsilon L<\pi$), Cor 2 (sandwich $D_{T+\varepsilon}\Rightarrow P_{\rm loc}\Rightarrow D_T$), Cor 3 (a smoothed cell
identity whose pieces are form values — the repair of R163_401 Rem 4.7a/4.8a's "no named class"), Prop 4 (the local
family inherits Theorem M), and the identification Landau ceiling = MV diagonal limit = pair-correlation $\alpha=1$.
**Open target, sharpened:** prove $P_{\rm loc}(\gamma,T')$ for *every* $\gamma$ in the sub-Landau range $T'<\frac12\log(\gamma/2\pi)-C$
(pointwise twisted-sum control at one height, slack allowed to depend on γ), and separately decide whether the
supra-Landau range can be reached by any statement that is not the local zero sum.
