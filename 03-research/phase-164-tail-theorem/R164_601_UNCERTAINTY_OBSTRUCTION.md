# R164_601 — O164.501.1: the uncertainty "obstruction" is false; the test exists and is de la Vallée Poussin at the witness

Memo, phase 164, round 6. Pure math, no numerics beyond cited constants. Inputs: R164_501 (Thm SA, Prop 4,
Prop 4.1, §6 Box), R164_190 §R164_501 (uncertainty remark), R163_401 (§1, §2.4, Lemma 3.1, Lemma 3.3, §4.8,
Rem 4.8a), R163_801 Thm 3. Notation as there: $G=\widehat F$ (or $-i\widehat F$) real-rooted of type $T=T_c$, parity
$(-1)^m$; $g:=(G^2)^\vee$, $\operatorname{supp}g\subset[-2T,2T]$; quartet point $t_q=\gamma_q-i\delta_q$,
$0<\delta_q<\tfrac12$, $\gamma_q>3\cdot10^{12}$; $P^{(s)}_a(z):=s/((z-a)^2+s^2)$, $\check P^{(s)}_a(u)=\tfrac12e^{-s|u|}e^{-iau}$.

## 0. Verdict and status table

**Verdict.** O164.501.1 as boxed in R164_501 §6 is **not** an obstruction: a test with (i)+(ii)+(iii) exists at
$T_c$ (Prop 2.1, PROVED), and it is precisely the de la Vallée Poussin (dlVP) test carried by $G^2$. The
reading "(ii)+(iii) is an uncertainty principle" is **REFUTED** as stated (Prop 1.2, Ex 2.2). What survives is a
different, *proved* no-go (Thm 3.1, the drop-term principle): every inequality obtained from the explicit formula by
discarding the tail with its sign is satisfied by $\zeta$'s true zero set, so it can exclude a quartet only together
with a lower bound on the *other* zero-side terms; for tests of the form $G^2K$ that lower bound is
$\operatorname{Re}[G^2K](t_{q'})\ge0$ at all other quartets, which fails in the light cones (Lemma 3.1/3.3 of
R163_401) and is (★_cell)-type. Without the $G^2$ factor (or when it is harmless), the inequality is classical dlVP and
excludes only $\tfrac12-\delta_q<c/\log\gamma_q$ (Thm 3.3, W2/M confirmed, loss computed). Residue returns to (★_cell).

| item | statement | status |
|---|---|---|
| Prop 1.1 | exact tail condition for $\Psi=G^2K$: sign of $g*\check K$ on $[2T,\infty)$; depends on $\check K|_{[0,\infty)}$ only | PROVED |
| Prop 1.2 | "tail sign $\iff\check K\ge0$" false both ways; $\check K\ge0$ on $[0,\infty)$ suffices iff $g\ge0$ | PROVED |
| Prop 1.3 | Bernstein class: $\check K|_{(0,\infty)}$ completely monotone $\Rightarrow$ tail sign $(-1)^m$, $K$ = Poisson superposition | PROVED |
| Prop 1.4 | trade-off inside the Bernstein class: (tail fraction)×(off-line/low-zero weight) $\lesssim \gamma_q^{-2}$ | PROVED (orders), constants ARGUED |
| Prop 2.1 | **construction**: $\Psi=G^2[w_0P^{(s)}_0+w_1(P^{(s)}_a+P^{(s)}_{-a})]$, $a=\gamma_q$, satisfies (i),(ii),(iii) | PROVED |
| Ex 2.2 | general class $\{\Psi\ge0,\ \check\Psi\ge0$ off $[-2T,2T]\}$ is not "essentially positive type"; $\check\Psi$ may be negative inside and $\Psi$ localized at $\gamma_q$ | PROVED |
| Thm 3.1 | drop-term principle: such inequalities are consistent with every zero configuration of $\zeta$ | PROVED (logic) |
| Thm 3.2 | at the witness, exclusion needs $\sum_{q'\ne q}\operatorname{Re}[G^2K](t_{q'})\ge -(\text{slack})$; fails in light cones | PROVED (reduction); closing it ⟺ (★_cell)-type, OPEN |
| Thm 3.3 | dlVP loss at $G^2K$: Fejér bound $w_1|G(a+is)|^2\le w_0|G(is)|^2\cos\frac{\pi}{N+2}$; archimedean term $\asymp w_1|G|^2\log\gamma_q$; excludes only $\tfrac12-\delta_q\le c/\log\gamma_q$ | PROVED (structure); constant PROVED-CITED |
| O164.501.1 | test with (i)+(ii)+(iii) | **CLOSED: exists (Prop 2.1)**; produces no new inequality (Thm 3.1–3.3) |
| O164.601.1 | lower bound on $\sum_{q'}\operatorname{Re}[G(t_{q'})^2K(t_{q'})]$ for a Poisson/trig $K$ localized at $\gamma_q$ | OPEN (= weighted (★_cell)) |

## 1. The natural class $\Psi=G^2K$

**Prop 1.1 (exact tail condition). PROVED.** Let $K$ be Weil-admissible, $\Psi=G^2K$. Then
$\check\Psi=g*\check K$ (convolution, $(1/2\pi)$-normalisation absorbed), and for $u\ge2T$
$$\check\Psi(u)=\int_{-2T}^{2T}g(v)\,\check K(u-v)\,dv,\qquad u-v\in[u-2T,u+2T]\subset[0,\infty).$$
So (ii) on $u\ge2T$ holds iff the window-convolution $g*\check K$ keeps one sign on $[2T,\infty)$, and this
involves only $\check K|_{[0,\infty)}$ (symmetrically for $u\le-2T$). Nothing is required of $\check K$ near $0$
beyond what $[0,4T]$ sees. *Proof:* support of $g$. ∎

**Prop 1.2 (the R164_190 equivalence is false). PROVED.**
- Not necessary: $\check K=\tfrac12e^{-s|u|}-\varepsilon\phi$, $\phi\ge0$ smooth, compactly supported in $(0,1)$: tail
  sign persists for small $\varepsilon$ (Prop 1.3 term dominates, $|g*\phi|\le\|g\|_1\|\phi\|_\infty$ and vanishes for
  $u>2T+1$), but $\check K<0$ somewhere.
- Sufficient iff $g\ge0$: if $g\ge0$, any $\check K\ge0$ on $[0,\infty)$ works. If $g(v_0)<0$ on a set of positive
  measure near $v_0$, take $\check K\ge0$ a narrow bump at $w_0=u_0-v_0\ge0$ with $u_0\ge2T$; then
  $\check\Psi(u_0)\approx g(v_0)\int\check K<0$ while $\check\Psi>0$ at other $u$ where $g>0$ is hit. (Whether $g$ of
  the witness changes sign is not used anywhere below.)
- "$\check K\ge0\Rightarrow|K|\le K(0)$ on $\mathbb R$" is true but obstructs nothing: (iii) is a *local*
  comparison at $\gamma_q$, and a positive-definite $K$ may have a bump at $\gamma_q$ as high as at $0$ (Ex 2.2). ∎

**Prop 1.3 (Bernstein class). PROVED.** If $\check K(w)=\int_{(0,\infty)}e^{-sw}\,d\mu(s)$ for $w>0$
($\mu\ge0$, completely monotone, even extension), then $K(z)=\int 2s/(s^2+z^2)\,d\mu(s)\ge0$ on $\mathbb R$ and for
$|u|\ge2T$
$$\check\Psi(u)=\int e^{-s|u|}\,G(is)^2\,d\mu(s)=(-1)^m\!\int e^{-s|u|}|G(is)|^2d\mu(s).$$
*Proof:* $\int g(v)e^{sv}dv=G^2(-is)=G(is)^2$ by parity, $G(is)^2=(-1)^m|G(is)|^2$ (Lemma 3.1(a)). Prop 4 of R164_501
is $\mu=\delta_y$. ∎

**Prop 1.4 (trade-off inside the Bernstein class). PROVED for orders.** Let $c_0:=\log n_0-2T>0$
($n_0$ the first prime power with $\log n_0\ge2T$). For $\mu=\delta_s$: tail fraction
$\eta(s)\asymp e^{-c_0 s}$ (Prop 4.1(iii) of R164_501), off-line weight $K(t_q)/K(\text{low})=s^2/(s^2+\gamma_q^2)\,(1+O(\delta_q/\gamma_q))$.
Hence $\eta(s)\cdot K(t_q)/K(0)\le \sup_s s^2e^{-c_0s}/\gamma_q^2=4/(e^2c_0^2\gamma_q^2)$; superposing $\mu$ does not
improve the sup. This is the true uncertainty statement — **but it is a statement about the Bernstein class only**
(sign generated by real exponentials). It is escaped by allowing complex exponentials with trigonometric positivity
(§2). ∎

## 2. Beyond the Bernstein class: the test exists

**Prop 2.1 (construction). PROVED.** Fix $s>\tfrac12$ (Weil-admissibility: $\Psi$ holomorphic in $|\operatorname{Im}z|<s$,
$O(|z|^{-2})$ times $G^2$, and $G^2$ type $2T$ with $\check\Psi$ decaying like $e^{-s|u|}$, so the prime sum
converges absolutely), $a=\gamma_q$, $w_1>0$, and $w_0$ with
$$w_0\,|G(is)|^2\ \ge\ 2\,w_1\,|G(a+is)|^2. \tag{2.1}$$
Put $K=w_0P_0^{(s)}+w_1(P_a^{(s)}+P_{-a}^{(s)})$, $\Psi=G^2K$.
- (i) $K>0$ on $\mathbb R$, $G$ real: $\Psi\ge0$.
- (ii) For $|u|\ge2T$, by the residue computation of R164_501 Prop 4 applied at $\pm a-is$:
  $$\check\Psi(u)=e^{-s|u|}\Big[\tfrac12w_0G(is)^2+w_1\operatorname{Re}\big(G(a+is)^2e^{-ia|u|}\big)\Big]
  =(-1)^m e^{-s|u|}\,p(a|u|),$$
  with $p(\theta)\ge\tfrac12w_0|G(is)|^2-w_1|G(a+is)|^2\ge0$ by (2.1). So the tail
  $\sum_{\log n\ge2T}\Lambda(n)n^{-1/2}\check\Psi(\log n)$ has sign $(-1)^m$, and its size relative to $\int|\check\Psi|$
  is $\asymp e^{-c_0s}$, non-negligible for $s=O(1)$.
- (iii) $\Psi(t_q)=G(t_q)^2\,[w_1 s/(s^2-\delta_q^2)+O(w_0/\gamma_q^2+w_1/\gamma_q^2)]$, while
  $\sup_{|\tau-\gamma_q|\le1}\Psi\asymp w_1 s^{-1}\sup_{|\tau-\gamma_q|\le1}G(\tau)^2$. By the real-rootedness,
  $|G(x+iy)|$ is nondecreasing in $|y|$ (each factor $|1-(x+iy)^2/x_k^2|$ is), so $|G(t_q)|\ge|G(\gamma_q)|$, and the
  ratio is bounded below by $|G(\gamma_q)|^2/\sup_{|\tau-\gamma_q|\le1}G^2$: a quantity of size $O(1)$, independent of
  $\gamma_q$ (no $\gamma_q^{-2}$ loss; it degenerates only if a node sits within $\ll1$ of $\gamma_q$, in which case
  shift $a$ by $O(1)$). ∎

So (i)+(ii)+(iii) hold simultaneously. The price is (2.1): $w_0/w_1\ge2|G(a+is)|^2/|G(is)|^2$, i.e. a large
low-height Poisson mass. This is exactly the dlVP structure $p(\theta)=p_0+p_1\cos\theta\ge0$.

**Ex 2.2 (no rigidity theorem for the general class). PROVED.** Let $h\in PW_T$ be real, $\Psi_1(\tau)=|h(\tau-a)|^2+|h(\tau+a)|^2$
(so $\check\Psi_1=2\cos(au)\,(\check h*\check h^\sim)$ is supported in $[-2T,2T]$ and sign-indefinite there), and
$B$ any positive-definite nonnegative Weil test (e.g. $P_0^{(s)}$). Then $\Psi=\Psi_1+\varepsilon B$ is $\ge0$ on
$\mathbb R$, has $\check\Psi>0$ on $|u|\ge2T$, $\check\Psi$ negative somewhere inside the window for small
$\varepsilon$, and is concentrated at $\pm a$. Hence the cone $\{\Psi\ge0,\ \check\Psi\ge0$ off $[-2T,2T]\}$ contains
$\{\Psi\ge0,\ \operatorname{supp}\check\Psi\subset[-2T,2T]\}+\{\text{positive definite}\}$ and has no
"essentially positive-type" structure; Kreĭn-type extension theory is not the relevant constraint. The rigidity, if
any, is on the **zero side off the real line** (§3), not in (i)+(ii). ∎

## 3. What the test gives at the witness

Write the explicit formula for $\Psi$ of §2 as $\sum_\rho\Psi(t_\rho)=\mathfrak A(\Psi)-\Pi_{\rm win}(\Psi)-\Pi_{\rm tail}(\Psi)$,
$\mathfrak A$ = archimedean + polar, $\Pi_{\rm win}$ = primes with $\log n<2T$, $(-1)^m\Pi_{\rm tail}\ge0$.

**Thm 3.1 (drop-term principle). PROVED.** The inequality $(-1)^m\sum_\rho\Psi(t_\rho)\le(-1)^m[\mathfrak A-\Pi_{\rm win}](\Psi)$
is equivalent, for the true zero set of $\zeta$, to $(-1)^m\Pi_{\rm tail}\ge0$; it holds whatever the zeros are. A
quartet is excluded by it only if, assuming the quartet, one has an *independent* lower bound
$(-1)^m\sum_{\rho\ne q}\Psi(t_\rho)\ge -S$ with $(-1)^m\,4\operatorname{Re}\Psi(t_q)>(-1)^m[\mathfrak A-\Pi_{\rm win}](\Psi)+S$.
*Proof:* subtract the identity. ∎ In particular Prop 2.1 alone, like Prop 4 of R164_501, yields **no** inequality on
the off-line part; this is the precise reason "the tail has a sign" never suffices.

**Thm 3.2 (where the witness bites). PROVED (reduction).** For $\Psi=G^2K$, $K$ as in Prop 2.1, on-line zeros give
$G(\gamma)^2K(\gamma)\ge0$ and can be dropped. Each other quartet contributes $4\operatorname{Re}[G(t_{q'})^2K(t_{q'})]$.
Since $K(t_{q'})\approx w_1s/(s^2-\delta_{q'}^2)+O(\gamma^{-2})>0$ near height $a$ and real to leading order,
its sign is that of $\operatorname{Re}G(t_{q'})^2$, which is negative exactly in the light cones (R163_401 Lemma 3.1/3.4:
phase $\Theta\in(\pi/4,3\pi/4)$ mod $\pi$). So the needed $S$ is a bound
$$\sum_{q'\ne q}\operatorname{Re}\big[G(t_{q'})^2K(t_{q'})\big]\ \ge\ -S,$$
a $K$-weighted version of the cell compensation (★_cell) of R163_401 §4.8 (O164.601.1, OPEN). The classical dlVP
argument drops these terms using $\operatorname{Re}K\ge0$ on the strip; the factor $G^2$ destroys that. ∎

**Thm 3.3 (the dlVP loss, exactly). PROVED (structure), constant PROVED-CITED.** Suppose the other-quartet terms are
granted $\ge0$ (best case). Then:
- target (quartet at $a=\gamma_q$): $4\operatorname{Re}[G(t_q)^2]\,w_1 s/(s^2-\delta_q^2)$, which is $\le0$ if $t_q$ is in
  its own light cone (then the inequality is automatically consistent) and at most $2w_1|G(t_q)|^2/(s-\delta_q)$;
- polar: $2\Psi(i/2)=2G(i/2)^2K(i/2)\approx(-1)^m w_0|G(i/2)|^2/(s-\tfrac12)$;
- archimedean: $\tfrac1{2\pi}\int\Psi\,\Omega\approx w_1\,\overline{G^2}_{\gamma_q}\log(\gamma_q/2\pi)$ (mean of $G^2$ near $\gamma_q$),
  plus $O(w_0)$.
Trigonometric positivity for degree $N$ (Fejér: $|p_1|\le2p_0\cos\frac{\pi}{N+2}$, CITED) caps
$w_1|G(a+is)|^2\le w_0|G(is)|^2\cos\frac\pi{N+2}$, and $|G(t_q)|\le|G(a+is)|$ (monotonicity in $|y|$, $\delta_q<s$).
Hence the target beats polar+archimedean only if
$$\frac{2\cos\frac{\pi}{N+2}}{s-\delta_q}\ \gtrsim\ \frac1{s-\frac12}\ +\ \kappa\log\gamma_q,\qquad
\kappa=\overline{G^2}_{\gamma_q}/|G(a+is)|^2\cdot\tfrac{|G(is)|^2}{|G(i/2)|^2}\cdots>0,$$
which, optimising $s-\tfrac12\asymp1/\log\gamma_q$, forces $\tfrac12-\delta_q\le c/\log\gamma_q$. For $\zeta$ without the
$G^2$ factor this is the classical region $1-\beta\ge1/(R_0\log\gamma)$, $R_0=5.5733$ (Mossinghoff–Trudgian 2015, CITED),
i.e. only $\delta_q>\tfrac12-0.0063$ at $\gamma_q\approx3\cdot10^{12}$ is excluded. The loss is the archimedean density
term $\asymp\log\gamma_q$ against a target of size $(\tfrac12-\delta_q)^{-1}$: **W2/M confirmed**. At the witness
there is no margin (Rem 4.8a; Paper 48 `thm:M`(b)), so no slack estimate of this type closes the cell. ∎

**Falsifiers.**
| step | uses Λ ≥ 0 beyond window | $f_t$ | $f_\chi$ | windowed $M_m$ | verdict |
|---|---|---|---|---|---|
| Prop 2.1 (test exists) | yes (tail sign) | sign fails | sign fails ($\Lambda\chi$ mixed) | sign holds | test is ζ-specific |
| Thm 3.1 inequality | yes | — | — | holds, $M_m$ has off-line zeros | no exclusion (identity-consistent) |
| Thm 3.3 dlVP region | yes | — | — | region near $\delta=\tfrac12$ only | W2/M |

The inequality exists for ζ only (good) but is satisfied by $M_m$, so it cannot exclude a first contact: **E1-type
consistency + W2/M**.

## 4. Conclusion

O164.501.1 is **settled negatively as an obstruction and positively as an existence question**: the (i)+(ii)+(iii)
test exists (Prop 2.1) and is dlVP at the witness. It is not an uncertainty principle; the only genuine uncertainty
(Prop 1.4) lives in the Bernstein class. The test gives a true inequality (Thm 3.1) whose exclusion power requires a
lower bound on the light-cone-negative terms $\operatorname{Re}G(t_{q'})^2$ (Thm 3.2, = weighted (★_cell),
O164.601.1), and even granting that, the archimedean cap leaves only the dlVP region (Thm 3.3). Wall: **W2/M**, with
the residue relocated to **(★_cell)**. (★_cell) is not proved here.

## 5. Ledger

- PROVED: Prop 1.1, 1.2, 1.3, 2.1, Ex 2.2, Thm 3.1, Thm 3.2 (reduction), structure of Thm 3.3; monotonicity of
  $|G(x+iy)|$ in $|y|$ for the witness.
- PROVED-CITED: Fejér bound on nonnegative cosine polynomials; Mossinghoff–Trudgian zero-free constant; RH to $3\cdot10^{12}$ (Platt–Trudgian).
- ARGUED: constants in Prop 1.4 and in $\kappa$ of Thm 3.3.
- RETRACTED/REFUTED: R164_190 remark "tail sign ⟺ $\check K\ge0$; hence no concentration at $\gamma_q$".
- OPEN: O164.601.1 (weighted cell compensation).

## 6. Grid cells

- **7F** (zero side × global transforms in T): O164.501.1 CLOSED (test exists, Prop 2.1). Route "positive-tail test
  with off-line weight": **DEAD [W2/M + drop-term principle Thm 3.1]**. New residue O164.601.1 (= (★_cell) weighted by
  Poisson/trig $K$). Symbol: no change (◧).
- **2A** (arithmetic positivity × one window): new PROVED-TOOL Prop 1.1/1.3 (exact tail-sign condition for $G^2K$,
  Bernstein class gives sign $(-1)^m$). The uncertainty reading is refuted (Prop 1.2, Ex 2.2). Symbol: no change.
- Walls used: W2/M (dlVP cap), E1-consistency (windowed $M_m$), light cone (R163_401 Lemma 3.1/3.4).
