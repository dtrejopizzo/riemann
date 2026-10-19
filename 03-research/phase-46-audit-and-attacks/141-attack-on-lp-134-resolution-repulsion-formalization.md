# Doc 141 — Attack on LP-134 (resolution repulsion): formalization, map, proof attempt, refutation attempt

**Program:** Riemann Hypothesis — Phase 46: AUDIT AND ATTACKS.
**Role of the document:** frontal attack on lemma LP-134 of Doc 134 §7.2 — the NEW half of the
uniformity wall. The goal: formalize it, map it against the literature, attempt to prove it unconditionally,
attempt to refute it, and give a verdict with exact consequences for D134's synergy.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = full freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = REALLY proved here, complete proof; external results cited with
precision. **[CALCULATION]** = shown. **[BRIDGE]** = connection with ζ/RH with honest status. **[GAP]** =
declared. **[DESIDERATUM]** = declared.

**Prerequisites read from source this session:** Doc 134 in full (in particular §4: visibility
$\theta_j\asymp\min(1,\delta_j a(\gamma_j))^\kappa$ and (V1)–(V2); §5: fat/thin/sub-resolution trichotomy,
Theorems 5.1–5.5, Prop. 5.5bis; §7.2: semi-formal statement of LP-134; §7.3: Theorem 7.2 and the two routes;
§5.8 M2–M3: DH and $F_{p,\alpha}$).

---

## 0. Executive summary

1. **(§1) The formalization uncovers a defect in the semi-formal statement: as written in D134
   §7.2 ("there exists a schedule $a$ and $c>0$..."), LP-134 is TRIVIALLY TRUE** for every
   admissible configuration — the schedule adapted to the zeros always exists ([THEOREM 141.A]). The entire
   content of the lemma lives in fixing the schedule IN ADVANCE within a definable class. The correct and
   canonical form is
   $$\textbf{LP-134}:\qquad \liminf_{\rho\ \mathrm{off}}\ \bigl|\beta_\rho-\tfrac12\bigr|\cdot\log\gamma_\rho\;>\;0$$
   (with $\liminf:=+\infty$ if there are finitely many off zeros). Proved hierarchy:
   $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}$, both arrows strict as
   implications between worlds: **LP-134 is the WEAKEST individual statement in the whole hierarchy of
   the program** — and yet, §3 shows it still lies behind the wall.

2. **(§2) Exact map against the literature.** (a) All density technology (Selberg 1946, Jutila)
   dies EXACTLY at the scale $\delta\asymp1/\log T$: non-triviality ⟺ $\delta\log T\to\infty$ ([LEMMA
   141.M1]). (b) Worse: what is unconditional proves the OPPOSITE of a repulsion — 100% of the zeros (in
   density) live INSIDE the resolution tube $|\beta-\tfrac12|\leq\psi(\gamma)/\log\gamma$, $\forall\psi\to\infty$
   ([PROPOSITION 141.M2], classical). (c) Vertical statistics ($S(t)$, Selberg moments,
   $N(T+h)-N(T)$, Littlewood gaps) are IDENTICALLY blind to LP-134: they depend only on the ordinates
   ([LEMMA 141.B0]). (d) Deuring–Heilbronn-type repulsion does not transpose: Landau's positivity
   lever is identically zero on the critical line by the functional equation ([CALCULATION 141.M4]), and the
   second-order signal of a quadruple is a profile of width $\delta$ with TOTAL INTEGRAL ZERO ([CALCULATION
   141.M5]): invisible exactly — not approximately — to any average coarser than $\delta$.

3. **(§3) Proof attempt: FAILS, and the failure is a relative theorem.** [LEMMA 141.B] (universal
   blindness of the explicit formula): a test of support $e^{\pm L}$ distinguishes a quadruple at distance $\delta$ from its
   projection onto the line by at most $O((\delta L)^2)$ per unit of mass. [COROLLARY 141.B2 — relative
   no-go]: no countable family of evaluations of functionals of polynomial support
   ($L\ll\log\gamma$) separates the LP-134 worlds from the ¬LP-134 worlds — the initial premise ("LP-134 is a
   statement of local average, on the good side of the master quantifier") is **FALSE**: LP-134 quantifies
   over individual zeros and is on the individual side of the wall. The exact residue: [GAP-141.G1]. What
   is indeed proved: the minimal form **LP-141** ("$m=\infty\Rightarrow$ infinitely many fat ones") suffices for the
   synergy ([PROPOSITION 141.P3]) and has TWO possible sources (repulsion or replication) — it is the real pivot.

4. **(§4) Refutation attempt.** For ζ: unconditionally impossible (refuting LP-134 exhibits infinitely many
   off zeros — refutes RH; [PROPOSITION 141.R1]); the violating worlds are consistent with everything known
   above the verification height. In the analytic category (entire, order 1, functional equation,
   real on the line): **LP-134 IS FALSE** — explicit Hadamard counterexample with $m=\infty$ and
   $\delta_j=e^{-\gamma_j}$ ([PROPOSITION 141.R2, complete proof]). In the category with Euler product:
   the naive construction (product of $F_{p_k,\alpha_k}$ with $\delta_k'\to0$) does NOT analytically continue
   ([CALCULATION 141.R3]) — the continuation of the Euler product emerges as the candidate MECHANISM for
   repulsion ([CONJECTURE 141.E]).

5. **(§5) VERDICT: OPEN-WITH-MAP.** LP-134 is not provable with averaging tools (relative no-go), is not
   refutable without refuting RH, is false without arithmetic, and its only positive evidence is the
   continuation rigidity of the Euler class. For D134's synergy: route 2 (strict ∧ LP-134) is NOT
   cheaper than route 1 (weak ∧ LP-112) — but the minimal pivot LP-141 reorganizes the board.

---

## 1. Formalization of LP-134

### 1.1. The semi-formal statement and its defect

Doc 134 §7.2 states: *"There exists a schedule $a(\cdot)$ (e.g. $a(\gamma)=C\log\gamma$, the natural
resolution) and $c>0$ such that every nontrivial zero $\rho=\tfrac12+\delta+i\gamma$ of $\zeta$ with $\delta\neq0$
satisfies $|\delta|\geq c/a(\gamma)$."*

With the quantifier $\exists a$ ranging over ALL schedules (non-decreasing functions
$[2,\infty)\to[1,\infty)$, Def. 3.6 of D134), this is trivially true:

**Theorem 141.A [THEOREM] (trivialization under a free schedule).** Let $Z=\{(\delta_j,\gamma_j)\}_{j\in J}$
be any admissible configuration (Def. 4.1 of D134: $\delta_j\in(0,\tfrac12)$, finitely many $j$ per window,
$\gamma_j\to\infty$ if $|J|=\infty$) — in particular, the set of off zeros of any function with
finitely many zeros per bounded height. Then there exists a schedule $a_Z$ (non-decreasing) with
$\delta_j\,a_Z(\gamma_j)\geq1$ for all $j$. Consequently, the statement of D134 §7.2, read with
free $\exists a$, holds for EVERY configuration — including all those that violate the purpose of the lemma — and
has no content.

*Proof.* For $n\geq2$ let $\varepsilon_n:=\min\{\delta_j:\ \gamma_j\leq n\}$ (minimum over a
finite set; $:=1$ if empty). The sequence $(\varepsilon_n)$ is non-increasing and strictly positive.
Define $a_Z(\gamma):=1/\varepsilon_{\lceil\gamma\rceil}$: non-decreasing. For each $j$, with
$n:=\lceil\gamma_j\rceil\geq\gamma_j$: $\delta_j\geq\varepsilon_n$ (since $\gamma_j\leq n$), so
$\delta_j\,a_Z(\gamma_j)=\delta_j/\varepsilon_n\geq1$. $\square$

**Observation 1.1 (why the triviality is fatal for the use).** D134 §7.2's conditional theorem
("under LP-134, strict positivity of the symbol at ONE schedule ⟺ $m<\infty$") needs the schedule
of the symbol and that of LP-134 to be THE SAME, and the positivity certificate to be producible without
knowing the zeros. The schedule $a_Z$ of 141.A depends on $Z$ — it is the "world-internal constant" of
P43/D112 §2.6, reappearing in the schedule quantifier, exactly as Prop. 5.5bis(ii) of D134 anticipated
("the sequence depends on $Z$"). What Prop. 5.5bis did not record is that this makes §7.2's literal
statement **true and empty at the same time**. The correct formalization MUST fix the schedule within a
definable class in advance.

### 1.2. The canonical form

**Definition 141.1 [NEW-DEFINITION] (LP-134, canonical form; and the generalized scale).** For a function
$F$ with zeros $\{\rho=\beta+i\gamma\}$ in the critical strip (finitely many per bounded height), and for a fixed
**resolution scale** $\psi:[2,\infty)\to[1,\infty)$ non-decreasing:
$$\mathbf{LP\text{-}134}^{(\psi)}(F):\qquad
\liminf_{\substack{\rho\ \text{zero of }F\\ \beta\neq1/2,\ \gamma\to\infty}}\ \bigl|\beta-\tfrac12\bigr|\cdot\psi(\gamma)\;>\;0,$$
with the convention $\liminf:=+\infty$ over finite or empty sets. **LP-134 plain** is
$\mathrm{LP\text{-}134}^{(\log)}$: $\psi(\gamma)=\log(\gamma+3)$, the natural resolution (mean zero
spacing $\asymp2\pi/\log\gamma$; support budget of the averaging technology, §2).

Three routine observations that fix the flexibility of the statement:

(i) **Invariance under constants:** $\mathrm{LP\text{-}134}^{(C\log)}=\mathrm{LP\text{-}134}^{(\log)}$ for
every $C>0$ (the $\liminf$ absorbs $C$ into $c$). The class $\{C\log\gamma\}$ is ONE statement.

(ii) **Free cofiniteness:** excepting finitely many zeros changes nothing: each off zero has $\delta>0$, so
a $\liminf>0$ over a tail extends to the whole set by lowering $c$ (this only uses finiteness per height).

(iii) **Monotonicity in the scale:** $\psi_1\leq\psi_2$ (eventually) $\Rightarrow$
$\mathrm{LP\text{-}134}^{(\psi_1)}\Rightarrow\mathrm{LP\text{-}134}^{(\psi_2)}$. In particular, the
bounded-scale version ($\psi\asymp1$) is the **uniform separation** ("there is a band
$0<|\beta-\tfrac12|<c$ free of zeros" — band-quasi-RH), the strongest of the family; the version
$\psi=\log$ is the one relevant to the synergy; versions $\psi\gg\log$ are weaker and feed symbols at
schedules where nothing is computable (§2 of the map).

### 1.3. Exact position in the program's hierarchy

**Proposition 141.P1 [PROPOSITION] (hierarchy).** As statements about a fixed configuration/function:
$$\mathrm{RH}\ (m=0)\;\Longrightarrow\;m<\infty\;\Longrightarrow\;\mathrm{LP\text{-}134}^{(\psi)}\ \text{for
every non-decreasing scale }\psi\geq1,$$
and no arrow reverses within the class of admissible configurations.

*Proof.* The first arrow is the definition of $m$ (number of off zeros). The second: if
$m<\infty$, the set of off zeros is finite and each $\delta_j>0$, so
$\liminf=+\infty$ by convention (or, with the $\exists c$ form: take
$c:=\min_j\delta_j\psi(\gamma_j)>0$). Non-reversal: (a) a configuration with a single quadruple at
$\delta=\tfrac14$ has $m=4\neq0$: violates RH, satisfies $m<\infty$; (b) the configuration
$\{(\tfrac14,\,2^j)\}_{j\geq1}$ has $m=\infty$ and
$\delta_j\psi(\gamma_j)=\tfrac14\psi(2^j)\geq\tfrac14$: satisfies $\mathrm{LP\text{-}134}^{(\psi)}$, violates
$m<\infty$. $\square$

**Observation 1.2 (the reading that orients the attack).** LP-134 is the **weakest statement in the whole
individual hierarchy of the program**: weaker than RH, weaker than $m<\infty$ (the Fredholm goal
itself!), weaker than uniform separation. If NOT EVEN this statement is accessible to averaging
tools (§3 will prove it is not, relative to a precise class of data), the measure of the wall is the
sharpest available: the wall does not begin at $m=0$, nor at $m<\infty$; it begins at the first
INDIVIDUAL statement about zeros, however weak its conclusion. And note the logical form: LP-134 is
$\forall\rho\,(\beta=\tfrac12\ \vee\ |\beta-\tfrac12|\geq c/\log\gamma)$ — an individual-$\forall$ with
disjunction, the SAME logical form as RH with a relaxed conclusion. The initial premise ("LP-134 is a
statement of LOCAL AVERAGE") is incorrect as such: there is no average in the quantifier. What is of
local average is the *evidence* one would want to use; the statement is individual. §3 turns this
observation into a relative no-go.

---

## 2. Exact map against what is known unconditionally

### 2.1. Zero density: dies exactly at the resolution scale

The relevant density theorem near the line is Selberg's [S46]:
$N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$ uniformly in $\tfrac12\leq\sigma\leq1$, where
$N(\sigma,T):=\#\{\rho:\beta\geq\sigma,\ 0<\gamma\leq T\}$. (Jutila [J77] and the density school improve
the exponents near $\sigma=1$ — irrelevant here: LP-134 lives glued to $\sigma=\tfrac12$.)

**Lemma 141.M1 [LEMMA] (exact non-triviality threshold).** Let $\delta(T)=\psi(T)/\log T$ with $\psi\geq0$.
Selberg's theorem gives $N(\tfrac12+\delta(T),T)=o(N(T))$ **if and only if** $\psi(T)\to\infty$; for
bounded $\psi$ the bound is $\gg T\log T\asymp N(T)$: trivial.

*Proof.* $T^{-\frac14\delta(T)}=e^{-\frac14\delta(T)\log T}=e^{-\psi(T)/4}$. Then
$N(\tfrac12+\delta(T),T)\ll e^{-\psi(T)/4}\,T\log T$ and $N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}$
(Riemann–von Mangoldt, [T86, Thm. 9.4]): the ratio is $\ll e^{-\psi(T)/4}$, which tends to $0$ exactly
when $\psi\to\infty$. If $\psi\leq C$: the bound is $\geq e^{-C/4}T\log T$, comparable to the total. $\square$

That is: **density technology becomes trivial exactly at the scale $1/\log T$ where LP-134 states its
repulsion.** It is not that the bounds are weak there: they say nothing at all. LP-134 lives exactly at
the point where the whole density school (Selberg, Ingham, Jutila, Huxley) turns off the light.

### 2.2. Worse than silence: the unconditional proves ACCUMULATION in the tube

**Proposition 141.M2 [PROPOSITION] (classical: 100% of the zeros live in the resolution tube).** For
every $\psi(T)\to\infty$, the proportion of zeros with $0<\gamma\leq T$ and
$|\beta-\tfrac12|>\psi(T)/\log T$ tends to $0$. Unconditionally, almost every zero (in density)
satisfies $|\beta-\tfrac12|\leq\psi(\gamma)/\log\gamma$.

*Proof.* Lemma 141.M1 plus the symmetry $\beta\leftrightarrow1-\beta$ of the zeros (functional equation).
It is Selberg's refinement of the Bohr–Landau theorem [BL14] (almost all zeros in
$|\beta-\tfrac12|<\epsilon$ fixed) to the scale $1/\log T$; see [T86, §9.15 and notes]. $\square$

The situation is thus the worst possible for a repulsion: the tube
$\{|\beta-\tfrac12|<\psi/\log\gamma\}$ — the region LP-134 declares free of off zeros — is where 100% of the
zeros pile up. LP-134 asserts that, within the tube where everything lives, the real part is
EXACTLY $\tfrac12$. The unconditional result proves piling toward the tube and is structurally mute
about its interior. LP-134 is not "between two known results": it is strictly beyond the edge
where every known result of σ type becomes trivial, and on the opposite side from the only proven
phenomenon (piling, not repulsion).

### 2.3. Vertical statistics are IDENTICALLY blind

**Lemma 141.B0 [LEMMA] (exact blindness of ordinate statistics).** Let $Z$ be a zero configuration
and $Z^\flat$ its **projection onto the line** (each zero $\beta+i\gamma$ replaced by $\tfrac12+i\gamma$, with
multiplicity). Then $N(t)$ is identical for $Z$ and $Z^\flat$ at every $t$ not a zero ordinate, and
by the Riemann–von Mangoldt formula ($N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+\frac78+S(t)+O(1/t)$,
[T86, Thm. 9.4], valid with $S$ defined by the argument variation and the same form in both worlds) the
function $S(t)$ differs between the two worlds by $O(1/t)$ away from the ordinates. Consequently: **all
moments of $S(t)$ (Selberg [S46]: $\int_0^T S^{2k}\sim c_k T(\log\log T)^k$), all variances of
$N(t+h)-N(t)$, and all ordinate-gap theorems (Littlewood [L24]:
$\gamma_{n+1}-\gamma_n\ll1/\log\log\log\gamma_n$) take exactly the same asymptotic values on $Z$ and
on $Z^\flat$** — they are functionals of the ordinates, blind to the coordinate $\beta$ by construction.

*Proof.* $N(t)$ counts zeros in the rectangle $0<\Im s<t$, $0<\Re s<1$, without reference to $\beta$
within the strip: the ordinates of $Z$ and $Z^\flat$ coincide as multisets by definition of the
projection, so $N$ coincides except at the jumps. The R–vM formula expresses $S(t)=N(t)-(\text{universal
smooth term})+O(1/t)$, with the smooth term depending only on the $\Gamma$ factor (identical). Every
statistic built on $S$ or on the ordinates inherits the coincidence. $\square$

This settles at once half of the toolbox proposed for step 3: **moments of $S(t)$ and
$N(T+h)-N(T)$ cannot prove LP-134 nor any weakened form of it** — not for lack of precision, but
by exact structural blindness. The tools with σ-sensitivity are only: density (dead at the
scale, §2.1), and the explicit formula with tests off the line (§2.4 and §3).

On pair correlation: Montgomery's theorem [M73] for $F(\alpha,T)$ at $|\alpha|<1$ is
**conditional on RH** (writing $\rho=\tfrac12+i\gamma$ is part of the proof); the unconditional
variants of the method (Goldston–Montgomery [GM87] and derivatives) weight each zero by terms of the type
$x^{\beta-1/2}$, $x\leq T^{O(1)}$: for a zero with $\delta\log T\to0$ the weight is
$x^{\delta}=e^{\delta\log x}\to1$ — the same sub-resolution blindness of §3, in its classical
incarnation. There is no unconditional pair repulsion with σ-sensitivity below $1/\log T$.

### 2.4. Why there is no Deuring–Heilbronn on the critical line: the null lever

The only genuinely proven zero repulsion in the theory is of Deuring–Heilbronn/Linnik type: an
exceptional zero (real, near $s=1$) repels the others. Its engine is **Landau's positivity
lever**: for $\sigma>1$ (and by extension near $1$),
$-\Re\frac{\zeta'}{\zeta}(\sigma+it)=\sum_{n}\Lambda(n)n^{-\sigma}\cos(t\log n)\ \text{bounded by the row
at }t=0$, and each zero contributes $\Re\frac1{s-\rho}=\frac{\sigma-\beta}{|s-\rho|^2}\geq0$: terms of ONE sign,
competing for a finite positive budget — hence the repulsion. Does it transpose to the line?

**Calculation 141.M4 [CALCULATION] (the first-order lever is identically zero on the line).** Let
$\frac{\xi'}{\xi}(s)=B+\sum_\rho\bigl(\frac1{s-\rho}+\frac1\rho\bigr)$ (Hadamard). Take $s=\tfrac12+it$ and
a pair of zeros symmetric under the functional equation, $\rho=\tfrac12+\delta+i\gamma$ and
$\rho'=1-\bar\rho|_{\text{same height}}=\tfrac12-\delta+i\gamma$. With $u:=t-\gamma$:
$$\Re\Bigl[\frac1{s-\rho}+\frac1{s-\rho'}\Bigr]
=\Re\Bigl[\frac1{-\delta+iu}+\frac1{\delta+iu}\Bigr]
=\frac{-\delta}{\delta^2+u^2}+\frac{\delta}{\delta^2+u^2}=0\qquad\text{for EVERY }t.$$
The first-order contribution of each symmetric pair to $\Re\frac{\xi'}{\xi}$ on the line is
exactly zero — consistent with $\Re\frac{\xi'}{\xi}(\tfrac12+it)\equiv0$ between zeros (ξ real on the
line). **There is no analogue at $\tfrac12$ of Landau's one-signed inequality at $1$: the functional
equation makes the line an axis of symmetry, and symmetric configurations are first-order equilibria.**
Any detection must be second order in $\delta$. $\square$

**Calculation 141.M5 [CALCULATION] (the second-order signal has total integral ZERO).** The second order is
$\partial_\sigma\Re\frac{\xi'}{\xi}(\sigma+it)\big|_{\sigma=1/2}=\Re\bigl(\tfrac{\xi'}{\xi}\bigr)'(\tfrac12+it)
=-\Re\sum_\rho\frac1{(s-\rho)^2}$. The contribution of the symmetric pair, with $u=t-\gamma$:
$$-\Re\Bigl[\frac1{(-\delta+iu)^2}+\frac1{(\delta+iu)^2}\Bigr]
=-\,\frac{2\delta^2-2u^2}{(u^2+\delta^2)^2}
=\frac{2(u^2-\delta^2)}{(u^2+\delta^2)^2}=:\,\Sigma_\delta(u).$$
The profile $\Sigma_\delta$ changes sign exactly at $|u|=\delta$ (signal width $=\delta$, the
distance of the zero from the line) and
$$\int_{-\infty}^{\infty}\Sigma_\delta(u)\,du
=2\Bigl[\frac{-u}{u^2+\delta^2}\Bigr]_{-\infty}^{\infty}=0$$
(exact antiderivative: $\frac{d}{du}\frac{-u}{u^2+\delta^2}=\frac{u^2-\delta^2}{(u^2+\delta^2)^2}$). **The
second-order signal of an off quadruple is a profile of exactly zero mean and width $\delta$:** any
average in $t$ at resolution $h\gg\delta$ does not attenuate it — it CANCELS it identically at the
leading order. Seeing it requires resolution $h\lesssim\delta$ in $t$, i.e. tests of support $e^{1/\delta}$:
super-polynomial in $\gamma$ when $\delta=o(1/\log\gamma)$. $\square$

This pair of calculations is the structural reason, in classical coordinates, why repulsion-from-$1$
exists and repulsion-from-$\tfrac12$ is not known how to prove: at $1$ there is a first-order lever with sign; at
$\tfrac12$ the first order is zero by symmetry and the second order has zero mean. It coincides exactly
with (V1) of D134 (Calculation 4.3) — and reinforces it: not only is the signal $O(\delta a)$ small; its
coarse average is ZERO.

### 2.5. Valiron–Landau: resolution repulsion is FREE in the wrong direction

**Lemma 141.M3 [LEMMA] (trivial horizontal repulsion — the contrast).** For every $T\geq2$ there exists
$\tau\in[T,T+1]$ with $\min_\rho|\tau-\gamma_\rho|\geq c/\log T$ ($c>0$ absolute).

*Proof.* $N(T+1)-N(T)\leq C\log T$ ([T86, Thm. 9.2], unconditional). The neighborhoods of radius
$r:=1/(4C\log T)$ around the $\leq C\log T$ ordinates in $[T,T+1]$ cover measure $\leq\tfrac12<1$:
there exists $\tau$ outside all of them. $\square$

This is the Landau/Valiron mechanism of horizontal-line selection (used in every proof of the
explicit formula; cf. [T86, §9.7]): **repulsion at scale $1/\log T$ with respect to a GENERIC
horizontal line is a trivial pigeonhole.** LP-134 asks for the same with respect to ONE fixed
vertical line — and there, there is no positive-measure family to average over: the critical line is
unique and maximally non-generic (Prop. 141.M2 says it carries 100% of the zeros). The contrast
locates LP-134's content: it is a statement of metric genericity for an object that is the least
generic in the whole strip.

### 2.6. Synthesis of the map

| tool | sensitivity to LP-134 | reason |
|---|---|---|
| moments of $S(t)$, $N(T+h)-N(T)$, Littlewood gaps | **exactly zero** | Lemma 141.B0: only ordinates |
| density (Selberg/Jutila/Ingham) | trivial at the scale | Lemma 141.M1: threshold $\delta\log T\to\infty$ |
| Bohr–Landau/Selberg (almost all near the line) | OPPOSITE sense | Prop. 141.M2: piling toward the tube |
| pair correlation | conditional on RH; unconditional blind | weights $x^{\beta-1/2}\to1$ sub-resolution |
| Deuring–Heilbronn / Linnik | does not transpose | Calculation 141.M4: null lever by the functional equation |
| Valiron–Landau (line selection) | wrong direction | Lemma 141.M3: pigeonhole only in $t$ |
| numerical verification (Platt–Trudgian [PT21]: RH up to $3\cdot10^{12}$) | finite | LP-134 only decided as $\gamma\to\infty$ |

**Conclusion of the map: LP-134 does not follow from anything known, is not "between" two known results, and
the whole of unconditional technology is either exactly blind, dies at the scale, or pushes in the
opposite direction.** It is a genuinely new statement — that confirms D134 — but §3 shows that its logical
form puts it on the individual side of the wall, against the initial hope.

---

## 3. Unconditional proof attempt

### 3.1. The plan and the first casualty

The plan: explicit formula with Fejér/Selberg tests, moments of $S(t)$, short counts
$N(T+h)-N(T)$ — local-averaging tools. The first casualty is immediate: by Lemma 141.B0, the
moments of $S$ and the short counts are identically blind. Only one family with σ-sensitivity remains: the
explicit formula evaluated off the line, i.e. the Weil functionals
$$W[f]\;:=\;\sum_\rho h_f(\rho)\;=\;\widehat{f}\,\text{(archimedean side)}\;-\;\sum_{p,k}\frac{\log p}{p^{k/2}}\bigl(f(p^k)+f(p^{-k})\bigr),
\qquad h_f(s)=\int_{-L}^{L}f(e^u)e^{(s-\frac12)u}e^{u/2}\,du,$$
with $\mathrm{supp}\,f\subseteq[e^{-L},e^{L}]$ (write $F(u):=f(e^u)e^{u/2}$). The parameter $L$ is the
support budget — D134's schedule in classical coordinates.

### 3.2. Universal blindness, with proof

**Lemma 141.B [LEMMA] (sub-resolution blindness of the explicit formula; classical version of D134 Thm. 5.4).**
Let $F\in C_c^\infty([-L,L])$ and $h=h_F$ as above. Let $Z$ be a configuration containing the quadruple
$\{\tfrac12\pm\delta\pm i\gamma\}$ and $Z^\flat$ the same configuration with that quadruple projected (two
double zeros at $\tfrac12\pm i\gamma$). Then, for every $N\geq0$,
$$\Bigl|\,\sum_{\rho\in Z}h(\rho)-\sum_{\rho\in Z^\flat}h(\rho)\Bigr|
\;\leq\;2\,\delta^2\sup_{|x|\leq\delta}\bigl(|h''(\tfrac12+x+i\gamma)|+|h''(\tfrac12+x-i\gamma)|\bigr)
\;\leq\;C_N(F)\,\frac{(\delta L)^2\,e^{\delta L}}{(1+\gamma)^N}.$$

*Proof.* The difference is $[g(\delta)+g(-\delta)-2g(0)]+[\tilde g(\delta)+\tilde g(-\delta)-2\tilde
g(0)]$ with $g(x):=h(\tfrac12+x+i\gamma)$, $\tilde g(x):=h(\tfrac12+x-i\gamma)$, holomorphic. By Taylor with
integral remainder, $|g(\delta)+g(-\delta)-2g(0)|=\bigl|\int_0^\delta(\delta-x)[g''(x)+g''(-x)]dx\bigr|\leq
\delta^2\sup_{|x|\leq\delta}|g''|$. For the second bound: $h''(s)=\int_{-L}^{L}u^2F(u)e^{(s-\frac12)u}du$;
integrating by parts $N$ times in $u$ (boundary terms vanish by compact support and smoothness),
$(s-\tfrac12)^Nh''(s)=(-1)^N\int(\partial_u)^N[u^2F(u)]\,e^{(s-\frac12)u}du$, so
$|h''(\tfrac12+x+i\gamma)|\leq e^{|x|L}\,\|(u^2F)^{(N)}\|_{L^1}\,(x^2+\gamma^2)^{-N/2}$. With $|x|\leq\delta$
and $\sup u^2\leq L^2$ absorbed into $C_N(F)$ (note $\|(u^2F)^{(N)}\|_1\leq C\,L^2$ modulo normalization
of $F$): the stated bound follows. $\square$

**Corollary 141.B2 [THEOREM] (relative no-go: LP-134 is not separable by polynomial-resolution data).**
Let $\mathcal F=\{F_i\}_{i\in\mathbb N}$ be any countable family of smooth tests, $F_i$ of support
$[-L_i,L_i]$, and let $\mathcal D(Z):=\bigl(\sum_{\rho\in Z}h_{F_i}(\rho)\bigr)_{i\in\mathbb N}$ be the Weil
datum of configuration $Z$, together with all vertical statistics (Lemma 141.B0) and the symbol
$\sigma_a(Q)$ at any fixed schedule $a$ with the property that each $F_i$ and $a$ are sub-linear
with respect to the sequence being constructed. Then for every $\varepsilon>0$ there exists a
configuration $Z_\varepsilon$ with:

(i) $Z_\varepsilon$ **violates** $\mathrm{LP\text{-}134}^{(\psi)}$ for every scale $\psi$ of growth at most
exponential fixed in advance, with $m=\infty$;
(ii) $|\mathcal D(Z_\varepsilon)_i-\mathcal D(\emptyset)_i|\leq\varepsilon\,2^{-i}$ for every $i$ (Weil
datum $\varepsilon$-indistinguishable from the RH world), vertical statistics identical to those of a world with
the same $\gamma$'s on the line, and $\sigma_a(Q^{Z_\varepsilon})=\sigma_a(Q^{\mathrm{aut}})$ in the
corona (D134, Thm. 5.4).

Consequently, **no argument whose input is (a) values of Weil functionals from a countable family of
supports fixed in advance, (b) ordinate statistics, (c) the symbol at a fixed schedule —
i.e., the totality of the "averaging tools" proposed for step 3 — can prove LP-134 nor
any weakening of it that excludes $Z_\varepsilon$:** any such argument, being valid over the class
of configurations with that data, would be valid on $Z_\varepsilon$, where the conclusion is false.

*Proof.* Construction by diagonalization. Choose $\gamma_j:=\max(2^j,\,j+\text{ordinate avoiding
collisions})$ and $\delta_j>0$ small enough that: (1) $\delta_j\,\psi(\gamma_j)\leq1/j$ for the fixed
scale $\psi$ (possible: $\psi(\gamma_j)$ is a number, $\delta_j$ free); (2) by Lemma 141.B, the
contribution of quadruple $j$ to functional $i$ is $\leq\varepsilon 2^{-i-j-1}$ for every $i\leq j$ (finitely
many conditions, each satisfied by small enough $\delta_j$ since the bound of 141.B is $O(\delta_j^2)$ with
constants depending only on $F_i,\gamma_j$); for $i>j$ use the bound with summable decay
$(1+\gamma_j)^{-N}$. Summing over $j$: the total discrepancy of datum $i$ is
$\leq\varepsilon2^{-i}$. (3) $\delta_j\,a(\gamma_j)\to0$, so D134 Thm. 5.4 applies and the symbol
matches the autonomous one. Violation of LP-134$^{(\psi)}$: $\liminf\delta_j\psi(\gamma_j)=0$ by (1), with
$m=\infty$. Vertical statistics: Lemma 141.B0. $\square$

**Observation 3.1 (what the no-go does and does not say — candor about its scope).** Corollary 141.B2 is
a no-go **relative to a class of data**, not an absolute unprovability theorem. It does not exclude: (a)
arguments using the REAL arithmetic of ζ at all supports simultaneously (the explicit formula's identity
is valid for every $L$; what does not exist is its unconditional *evaluation* with an error surpassing the
signal $(\delta L)^2$ — that is exactly [GAP-141.G1]); (b) global rigidity arguments (Hamburger type,
§4.3) using that the zeros are those of ONE function with an Euler product, not an abstract configuration.
What it does establish: **LP-134 is not a statement of local average.** The initial premise — "the whole
point of LP-134 is that it is a statement of LOCAL AVERAGE, on the good side of the master quantifier" — is
refuted: LP-134 quantifies individually over zeros, its per-zero signal has size $O((\delta L)^2)$ and
zero mean (Calculation 141.M5), and averages cancel it rather than accumulating it. The wall D134 split in
two did not leave LP-134 on the good side: it left it as the GEOMETRIC HALF of the same wall — weaker than
$m<\infty$ (Prop. 141.P1), not equivalent to RH (correct in D134), but on the same side of the quantifier.

### 3.3. [GAP] The exact residue

**[GAP-141.G1 — the missing estimate, named precisely].** To prove LP-134 by the analytic route one
would need: *an evaluation of the explicit formula in ONE individual window at height $\gamma$, with
tests of support $L=L(\gamma)$, whose error term (archimedean + primes + on-line sea) is
$o\bigl((\delta L)^2\bigr)$ uniformly for the $\delta$ one wants to exclude* — i.e., individual
(not average) control of the near-prime deficit per window. With $L\asymp\log\gamma$ and $\delta\asymp c/\log\gamma$ the
signal is $\asymp c^2$: ONE WOULD NEED the per-window individual deficit with error $o(1)$ — exactly
Conjecture 108-N / window uniformity, the old wall (D134 Thm. 6.1, Cor. 6.2). The circle closes:
**the new half of the wall, attacked with analysis, leads back to the old half.** There is no analytic
side door.

### 3.4. What is indeed proved: the minimal form LP-141 and the reorganization of the synergy

The proof attempt leaves a structural dividend: D134's synergy does not need the whole of LP-134.

**Definition 141.2 [NEW-DEFINITION] (LP-141, the minimal form).** At a fixed unbounded schedule $a$:
$$\mathbf{LP\text{-}141}(a):\qquad m=\infty\ \Longrightarrow\ \#\{j:\ \delta_j\,a(\gamma_j)\geq1\}=\infty$$
("if there are infinitely many off zeros, they cannot all be sub-resolution except finitely many: infinitely many are fat").

**Proposition 141.P3 [PROPOSITION] (LP-141 suffices for the Fredholm half; in D134's model $\mathfrak W$
with (S1)–(S3) and (V2)).** If LP-141$(a)$ holds and the symbol $\sigma_a(Q)$ is **weakly** positive
($\mathrm{spec}\subseteq[0,\infty)$), then $m<\infty$.

*Proof.* If $m=\infty$, LP-141 gives infinitely many fat zeros; by (V2) they have visibility $\theta_j\geq c_0$;
by D134 Theorem 5.1, $\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c_0/2]\neq\emptyset$ — contradicting
weak positivity. $\square$

**Proposition 141.P4 [PROPOSITION] (position of LP-141).**
(i) $\mathrm{LP\text{-}134}^{(\psi)}\Rightarrow\mathrm{LP\text{-}141}(a)$ for every schedule $a\succeq\psi$
(if every off zero satisfies $\delta_j\psi(\gamma_j)\geq c$, the infinitely many off zeros of a
world with $m=\infty$ satisfy $\delta_j a(\gamma_j)\geq c$ eventually, and after rescaling $a$ they are fat).
(ii) The quantitative Axiom R (D134 Thm. 7.2 = LP-112 with conservation of $\delta_0/2$) implies
$\mathrm{LP\text{-}141}(a)$ for every unbounded $a$ — it actually implies the stronger
"$m\geq1\Rightarrow$ infinitely many fat ones".
(iii) LP-141 does not imply LP-134 (configuration: one fat quadruple replicated at fixed $\delta$ PLUS a
sub-resolution sequence — satisfies LP-141, violates LP-134) nor does it imply Axiom R.

*Proof.* (i) and (iii): direct from the definitions, with the indicated configurations. (ii) is D134
Theorem 7.2, first half: the replicas have $\delta_k'\geq\delta_0/2$ and
$\delta_k'a(\gamma_0+\tau_k)\to\infty$. $\square$

**Observation 3.2 (the reorganization).** The real pivot of the synergy is LP-141, strictly weaker
than ITS TWO parents: repulsion (LP-134) and replication (LP-112/Axiom R). It has two
independent possible sources, and with it the Fredholm route becomes:
$$\text{WEAK positivity of the symbol at an unbounded schedule}\ \wedge\ \mathrm{LP\text{-}141}\ \Longrightarrow\ m<\infty,$$
with the positivity piece downgraded to weak (not strict: 5.1 violates even the weak one) and the geometric
piece downgraded from LP-134 to LP-141. It is the minimal provable-conditional version of D-109's Fredholm
half. No-go 141.B2 also applies to LP-141 (the configuration $Z_\varepsilon$ violates it and is
indistinguishable), so LP-141 is also not of average type — but having two sources, it attacks on two fronts:
any progress on LP-112 (dynamical front, D112) or on class repulsion (arithmetic front, §4.3) feeds it.

---

## 4. Refutation attempt

### 4.1. For ζ itself: refuting LP-134 is refuting RH

**Proposition 141.R1 [PROPOSITION].** Every unconditional refutation of LP-134 (for ζ) refutes RH. Every
unconditional proof of LP-134 is implied by a proof of RH (Prop. 141.P1) but does not imply it. In
particular LP-134 is **falsifiable only in ¬RH worlds**: its content is exclusively a statement about the
mode of failure of RH ("if RH fails, it fails visibly"), vacuous under RH.

*Proof.* Refuting LP-134 exhibits an infinite sequence of zeros with $\beta\neq\tfrac12$ — zeros off
the line: ¬RH. The second claim is 141.P1. $\square$

**Consistency of the violating world with everything known [frank discussion].** Are there configurations
compatible with everything proved/computed that violate LP-134? Yes, and the map of §2 certifies it
piece by piece: take the world $Z_\varepsilon$ of Corollary 141.B2 implanted above the numerical
verification height ($3\cdot10^{12}$, Platt–Trudgian [PT21]), with $\delta_j=1/\log^2\gamma_j$. Count
$N(T)$: identical (projection preserves ordinates). Density: the $\delta_j$ are below 141.M1's
threshold — no density bound sees it. Moments of $S$, gaps: blind (141.B0). Historically verified Weil
positivity: only tested with bounded supports — minuscule discrepancy $O((\delta_jL)^2)$
(141.B). Unconditional pair correlation: weights $\to1$. **Nothing known excludes the real world
being the violator.** And conversely, the heuristic at the boundary weighs AGAINST LP-134's plausibility: the
Rodgers–Tao theorem [RT20] ($\Lambda\geq0$: the de Bruijn–Newman constant is non-negative) says ζ is at
the exact boundary of the "barely real zeros" regime — "RH, if true, is barely true". RH's natural
failure mode is the "barely false" mode: quadruples with minuscule $\delta$ — exactly the stratum that
LP-134 forbids. Lehmer pairs (anomalously small local minima of $|Z(t)|$; Csordas–Smith–Varga
[CSV94] used them for lower bounds on $\Lambda$ pre-[RT20]) are the real numerical shadow of that
stratum: on-line configurations at distance $o(1)$ from becoming sub-resolution quadruples. LP-134 asserts that
that boundary, grazed infinitely often (Lehmer pairs occur), is never crossed, or is crossed with margin
$\geq c/\log\gamma$. I know of neither a mechanism nor evidence in its favor, apart from the class rigidity of §4.3.

### 4.2. In the analytic category: LP-134 IS FALSE (counterexample with proof)

**Proposition 141.R2 [PROPOSITION] (Hadamard counterexample).** There exists an entire function $F$ of order
$1$, with $F(s)=F(1-s)$, real on the critical line ($F(\tfrac12+it)\in\mathbb R$ for $t\in\mathbb R$), with
all its zeros in the strip $|\Re s-\tfrac12|<\tfrac12$, with zero count
$N_F(T)\asymp T\log T$, and with infinitely many off quadruples $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ where
$$\gamma_j=2^j,\qquad \delta_j=e^{-\gamma_j}:$$
$m=\infty$ and $\delta_j\,\psi(\gamma_j)\to0$ for EVERY scale $\psi(\gamma)\leq e^{\gamma/2}$ — $F$ violates
$\mathrm{LP\text{-}134}^{(\psi)}$ for every sub-exponential scale, in particular for the whole class
$\{C\log\gamma\}$ and every polynomial.

*Proof.* Coordinate $z$: $s=\tfrac12+iz$, so that the functional equation $s\mapsto1-s$ is
$z\mapsto-z$ and the critical line is $z\in\mathbb R$. Zeros prescribed in $z$: (a) real pairs $\pm t_n$ with
$t_n:=n/\log(n+2)$ ($n\geq1$), giving count $\#\{t_n\leq r\}\asymp r\log r$; (b) quadruples
$\{\pm z_j,\pm\bar z_j\}$ with $z_j:=\gamma_j-i\delta_j$ (corresponding to
$s=\tfrac12\pm\delta_j\pm i\gamma_j$). Define
$$G(z):=\prod_{n\geq1}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\ \cdot\ \prod_{j\geq1}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$
*Convergence:* in the variable $w=z^2$ the zeros are $w_n=t_n^2$ and $w_j=z_j^2,\bar z_j^2$;
$\sum_n t_n^{-2}=\sum_n\log^2(n+2)/n^2<\infty$ and $\sum_j|z_j|^{-2}\leq\sum_j4^{-j}<\infty$: the genus-$0$
product in $w$ converges absolutely and locally uniformly; $G$ is entire and even in $z$.
*Functional equation:* $G(-z)=G(z)$ by parity ⟹ $F(s):=G\bigl(\tfrac{s-1/2}{i}\bigr)$ satisfies $F(1-s)=F(s)$.
*Reality on the line:* the factors have real coefficients in $z^2$ ($t_n^2$ real; the quadruples
appear with $z_j^2$ and $\bar z_j^2$ paired: $(1-w/z_j^2)(1-w/\bar z_j^2)$ has real coefficients), so
$G(\bar z)=\overline{G(z)}$ and $G|_{\mathbb R}\subseteq\mathbb R$: $F$ is real on $\tfrac12+i\mathbb R$.
*Order:* the counting function of zero moduli in $z$ is $n_G(r)\asymp r\log r$, so the convergence
exponent is $1$ and, for canonical products, order $=$ convergence exponent $=1$ [B54, Thm. 2.6.5].
*Strip:* $|\Im z_j|=\delta_j<\tfrac12$ ✓. *Violation:* $\delta_j\psi(\gamma_j)=e^{-\gamma_j}\psi(\gamma_j)\to0$
if $\psi(\gamma)\leq e^{\gamma/2}$. $\square$

**Corollary 141.R2b [COROLLARY] (LP-134 is arithmetic or it is not).** LP-134 is not a theorem of the
analytic class (entire + order 1 + functional equation + reality on the line + zeta-type zero density):
141.R2 gives a member that violates it maximally. **Every proof of LP-134 must use the arithmetic side**
(Euler product / coefficients / explicit formula with primes), not just the structure of ξ as an entire
function of the Pólya class. (Compare: it is the LP-134 analogue of the cosh anti-models of D111/D112,
which realize finite $m$ in the analytic class. Here "$m=\infty$ sub-resolution" is realized.) $\square$

### 4.3. In the Euler category: the construction attempt FAILS, and the failure points to the mechanism

Following Desideratum 9.D2 of D134: can an object WITH Euler product be constructed that violates the
repulsion? The obvious candidate, with the blocks $F_{p,\alpha}$ of Doc 131 (Thm. 6.7: impure local datum
$|\alpha_k|=p_k^{1/2+\delta_k'}$ produces a divisor on $\Re s=\tfrac12+\delta_k'$):

**Calculation 141.R3 [CALCULATION] (the naive construction does not continue).** Take primes $p_1<p_2<\cdots$ and
impure data $\delta_k'\downarrow0$, and form the Euler product
$D(s):=\prod_k\bigl(1-\alpha_kp_k^{-s}\bigr)^{-1}\bigl(1-\bar\alpha_kp_k^{-s}\bigr)^{-1}$,
$|\alpha_k|=p_k^{1/2+\delta_k'}$. Factor $k$ has its poles/zeros on the vertical
$\Re s=\tfrac12+\delta_k'$: the aggregated divisor would violate LP-134 with $m=\infty$. But: (a) the
product converges only in $\Re s>\tfrac32$ (since $|\alpha_kp_k^{-s}|=p_k^{1/2+\delta_k'-\sigma}$ and
$\sum_kp_k^{1/2-\sigma}<\infty$ requires $\sigma>\tfrac32$); (b) the target verticals lie near
$\Re s\approx\tfrac12$, outside the convergence region: for the divisor to EXIST one needs
analytic continuation into the critical strip plus a functional equation, and nothing in the construction
provides it; (c) the reciprocal $\prod_k(1-\alpha_kp_k^{-s})$ does not either: converges on
$\sigma>\tfrac32$ and no further without a miracle. The obstruction is not technical but structural:
**analytic continuation couples the local data to each other** — it is a global condition on the
family $\{\alpha_k\}$, and all known continuable examples (characters, automorphic forms) have
PURE data ($|\alpha|=\sqrt p$: $\delta'=0$). $\square$

Two known rigidities delimit the phenomenon from above and below:

- **Hamburger [H21]:** a Dirichlet series with ζ's exact functional equation (and minimal regularity)
  IS a multiple of ζ. In the narrowest class there is NO object other than ζ: LP-134 there is
  exactly LP-134 for ζ — falsification in the strict category is as hard as ¬RH.
- **Davenport–Heilbronn [DH36]:** without an Euler product (linear combination of two $L$ mod 5), the
  continuation + functional equation are obtained and off zeros exist — infinitely many, even with
  $\beta>1$. Computations of their zeros in the strip ([BS07]; survey in [BG11]) show off zeros at
  macroscopic distances from the line; **if** their $\delta_j$ are bounded below (GAP-134.DH of the
  D134, inherited here as **[GAP-141.DH]**: plausible datum, not verified from source this session), DH
  satisfies LP-134 with genuine repulsion — the only $m=\infty$ object of the corpus would calibrate the GOOD
  side. Note moreover the deformation: DH is a point of a family $F_\theta=\cos\theta\,L_1+\sin\theta\,L_2$;
  at the values of $\theta$ where $F_\theta$ degenerates into a genuine $L$ (Selberg class), the off zeros
  must migrate to the line (Hurwitz), so $\inf_j\delta_j(\theta)\to0$ as $\theta\to\theta_0$ — the
  family realizes "repulsion with degenerating constant": LP-134 member by member with non-uniform
  $c(\theta)$. Again world-internal constants, now in a real family.

**Conjecture 141.E [DESIDERATUM/CONJECTURE — the mechanism, named].** *In category D131-H⁺ (Euler product
with positive hermitian local datum + continuation + functional equation; a fortiori in the Selberg class),
LP-134 holds; the mechanism is not positivity (the lever is null: Calculation 141.M4) but **continuation
rigidity**: the analytic continuation of an Euler product forces asymptotic purity of the local datum
(dictionary M3 of D134: purity = local sub-resolution at every schedule), and the impurity $\delta'$
needed for an off zero at distance $\delta'$ is detectable in the local datum at support $\asymp1/\delta'$
(D131 Thm. 6.7: $|c_m|>2p^{m/2}$ only at $m\gtrsim1/\delta'$) — a globally sub-resolution off zero
would require sustained sub-resolution local impurity, and continuation forbids it.* Status: conjecture;
evidence: the structural failure of 141.R3 (the only construction route dies exactly at the
continuation step), Hamburger, and the total absence of Selberg-class members with known off zeros.
Concrete task inherited and sharpened from 9.D2: prove that in category D131 continuation + Euler implies
$\liminf\delta_j\log\gamma_j>0$, OR construct the continuable counterexample. It is the program's first
statement where analytic continuation — not positivity — is the proposed engine of repulsion.

### 4.4. Verdict of the refutation attempt

LP-134 **survives** falsification: (a) for ζ it is unfalsifiable without refuting RH (141.R1); (b) in the
analytic category it falls (141.R2), but that does not refute it for ζ — it reclassifies it as an arithmetic
statement; (c) in the Euler category the counterexample attempt fails due to a structural obstruction
(141.R3) which is, in itself, the best evidence IN FAVOR of LP-134 produced this session. The falsifiability
situation is asymmetric and must be stated precisely: LP-134 is falsifiable WITHIN THE CATEGORY (and the
analytic category indeed falsifies it), but the ζ instance is only decidable together with RH or via the
class route 141.E.

---

## 5. Verdict and consequences for D134's synergy

### VERDICT: **OPEN-WITH-MAP** (with two PROVEN pieces and one initial premise REFUTED)

**Not proved:** LP-134 was not proved unconditionally — and Corollary 141.B2 shows it cannot be proved
with the tools proposed for step 3 (explicit formula at polynomial support, moments of $S$,
short counts): the premise "LP-134 is a statement of local average, on the good side of the master
quantifier" is **false**; LP-134 is $\forall$-individual over zeros, its per-zero signal is $O((\delta L)^2)$ and
of exactly zero mean, and the analytic attack leads back to window uniformity (GAP-141.G1 = the old
wall). **Not refuted:** unfalsifiable for ζ without refuting RH; the counterexample exists in the analytic
category (141.R2, proved) but the Euler category resists it via continuation rigidity (141.R3).

**Final position in the map:** $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}\Rightarrow
\mathrm{LP\text{-}141}$, all strict; vacuous under RH; content = "RH's failure is visible"; it lives
exactly at the point where density dies ($\delta\log T\asymp1$, Lemma 141.M1), in the sense opposite
to the only proven phenomenon (piling toward the tube, Prop. 141.M2), with no first-order lever (Calculation
141.M4) and with a second-order signal of zero mean (Calculation 141.M5); false without arithmetic (141.R2); open
with a named candidate mechanism in the Euler category (Conjecture 141.E).

**For D134's synergy (§7.3):** (1) Route 2 ("strict symbol ∧ LP-134") loses its expected advantage:
LP-134 is not cheaper than LP-112 in quantifier class — both are individual and no-go
141.B2 covers them equally. (2) The real gain is the minimal pivot **LP-141** (Def. 141.2): strictly
weaker than both LP-134 AND Axiom R, sufficient with **weak** positivity of the symbol for $m<\infty$
(Prop. 141.P3), and fed from two independent fronts (dynamical replication D112 or class repulsion
141.E). The refined D-109 architecture becomes:
$$m<\infty\ \Longleftarrow\ \bigl[\sigma_a(Q)\geq0\ \text{weak, $a$ unbounded}\bigr]\ \wedge\ \mathrm{LP\text{-}141}(a),
\qquad \mathrm{LP\text{-}141}\ \Longleftarrow\ \mathrm{LP\text{-}112}\ \ \text{or}\ \ \mathrm{LP\text{-}134}.$$
(3) The new front this session opens is not analytic but **algebraic-arithmetic**: Conjecture 141.E
(continuation of Euler products ⟹ resolution repulsion), with D134's task 9.D2 sharpened to a
concrete mechanism and a first finite test: deciding GAP-141.DH (are the $\delta_j$ of Davenport–Heilbronn
bounded below? — finite bibliographic/numerical check on [BS07]/[BG11]).

**The three main results of the session:**
1. **[THEOREM 141.A + Def. 141.1 + Prop. 141.P1]** — formalization: D134's semi-formal statement is
   trivially true with a free schedule; the form with content is
   $\liminf|\beta-\tfrac12|\log\gamma>0$ at a fixed scale; and LP-134 is the weakest individual statement of
   the hierarchy: $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}$, strict.
2. **[THEOREM 141.B2 (with Lemmas 141.B0/141.B and Calculations 141.M4/M5)]** — relative no-go: no
   countable family of polynomial-resolution data (explicit formula, vertical statistics, symbol at
   fixed schedule) separates LP-134 from its negation; the signal has exactly zero mean; LP-134 is on
   the individual side of the wall — the initial premise is refuted and the residue is GAP-141.G1 = the old
   wall.
3. **[PROPOSITION 141.R2 + CALCULATION 141.R3 + CONJECTURE 141.E]** — stratified refutation: LP-134 is FALSE
   in the analytic category (explicit Hadamard counterexample, complete proof), the Euler counterexample
   fails exactly at analytic continuation, and continuation rigidity is named as the only candidate
   mechanism of repulsion — the first non-positivity-based engine proposed in the program.

---

## References

**Internal (backward-only):** Doc 134 (§3 corona; §4 model $\mathfrak W$, visibility (V1)–(V2); Theorems
5.1–5.5, Prop. 5.5bis, Obs. 5.5ter; §6 computability; §7.2 semi-formal LP-134; Thm. 7.2; §5.8 M2–M3;
GAP-134.DH, Desideratum 9.D2); Doc 132 (Theorem D, defect $2m$; §8.2(c)); Doc 131 (Thm. 6.7 local purity,
barrier $|c_m|\leq2p^{m/2}$; Desideratum 6.9 H⁺); Doc 112 (LP-112, Rouché mechanism, §2.6 internal
constants); Doc 111 (Obs. 2.4, cosh anti-models); Doc 108 (Thm. 3.3 blindness; §5.2 MV74; Conjecture 108-N; Thm. 4.3);
D70 ($\Lambda$ as vanishing time); P43 (master quantifier).

**Literature (published, verifiable):**
- [BL14] H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die ζ-Funktion und die
  L-Funktionen*, Rend. Circ. Mat. Palermo **37** (1914), 269–272. (Almost all zeros near the line.)
- [L24] J. E. Littlewood, *On the zeros of the Riemann zeta-function*, Proc. Cambridge Philos. Soc. **22**
  (1924), 295–318. (Gaps between ordinates.)
- [H21] H. Hamburger, *Über die Riemannsche Funktionalgleichung der ξ-Funktion*, Math. Z. **10** (1921),
  240–254. (Rigidity: ζ's functional equation characterizes ζ.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 and 307–312. (Off zeros without an Euler product.)
- [S46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. **48**
  (1946), 89–155. (Density $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; moments of $S(t)$.)
- [M73] H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math.
  **24**, AMS (1973), 181–193. (Conditional on RH.)
- [J77] M. Jutila, *Zero-density estimates for L-functions*, Acta Arith. **32** (1977), 55–62.
- [GM87] D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, in
  Analytic Number Theory and Diophantine Problems, Birkhäuser (1987), 183–203.
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Thm. 9.2: $N(T+1)-N(T)=O(\log T)$; Thm. 9.4: Riemann–von Mangoldt; §9.7
  Valiron–Landau-type line selection; §9.15 density near the line.)
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954. (Order of canonical products, Thm. 2.6.5.)
- [CSV94] G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and
  the Riemann hypothesis*, Constr. Approx. **10** (1994), 107–129.
- [RT20] B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020),
  e6. (Λ ≥ 0: "RH, if true, is barely true".)
- [PT21] D. Platt, T. Trudgian, *The Riemann hypothesis is true up to* $3\cdot10^{12}$, Bull. London Math.
  Soc. **53** (2021), 792–797.
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049.
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. (Ch. 5: zeros per
  window; density context.)

*End of Doc 141.*
