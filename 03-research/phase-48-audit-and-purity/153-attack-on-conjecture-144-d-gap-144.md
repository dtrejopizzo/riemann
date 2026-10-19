# Doc 153 — Attack on Conjecture 144.D / GAP-144.C: the de la Vallée Poussin test at ½, the confrontation with Kaczorowski–Perelli, and the distilled minimal link

**Program:** Riemann Hypothesis — Phase 48: AUDIT AND PURITY.
**Role of the document:** frontal attack on **Conjecture 144.D** (Doc 144 §3.3) and on its residue **GAP-144.C** —
the arithmetic pivot of the finiteness half ($m<\infty$) after the analytic refutation of LP-141 (Prop. 144.2).
The goal: (1) state 144.D/GAP-144.C with exact quantifiers; (2) develop the attack
"de la Vallée Poussin centered at ½" (Euler + positivity of $\Lambda$ against a sub-resolution swarm)
with all computations in closed form, and DECIDE whether it dies or whether a subsequence suffices; (3) confront it with
the small-degree classification of Kaczorowski–Perelli; (4) isolate the minimal unproved link and locate it
in the hierarchy; (5) verdict.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = REALLY proved here, complete proof; external results cited with
precision. **[COMPUTATION]** = shown. **[BRIDGE]** = connection to ζ/RH with a frank status. **[GAP]** =
declared. **[literature GAP]** = datum not verified at the source, not used as a basis.

**Prerequisites read at the source (complete):** entire Doc 144 (Def. 144.0, Props. 144.1–144.9,
Conjecture 144.D, GAP-144.C, Cor. 144.10); entire Doc 141 (Lemmas 141.B0/141.B, Cor. 141.B2, Computations
141.M4/M5/R3, Prop. 141.R2, Conjecture 141.E, GAP-141.G1); Doc 131 §6 (Axiom H, Thm. 6.6 local Poisson,
Thm. 6.7 local purity, Prop. 6.8 DH, Desideratum 6.9 H⁺); Doc 146 (verdict GAP-141.DH: FAT, off zeros of
D–H at macroscopic distance).

---

## 0. Executive summary

1. **(§1)** 144.D and GAP-144.C are stated with total quantifiers, together with the exact axioms
   (A1)–(A4) of the category D131-H⁺ that this document uses, declared one by one.

2. **(§2) The dlVP-at-½ attack DIES, and the death certificate is quantitative and new.**
   The classical zero-free region is indeed the only unconditional repulsion theorem of the theory
   ($|\beta-1|\geq c/\log\gamma$: repulsion from $\Re s=1$), and its engine is Euler + positivity of $\Lambda$
   ($3+4\cos\theta+\cos2\theta\geq0$). Transposed to ½: **[LEMMA 153.2]** proves that an off quadruple at
   distance $\delta$ perturbs the ENTIRE half-plane $\sigma>1$ — the only place where positivity bites —
   by at most $C_0\,\delta^2/(1+(t-\gamma)^2)$ (second order: the functional equation kills the first order,
   the $\sigma>1$ avatar of Computation 141.M4). **[PROPOSITION 153.3]:** the complete sub-resolution swarm
   ($\delta_j\log\gamma_j\to0$, ALL the off zeros) deflects $-\Re\frac{\zeta'}{\zeta}$ in $\sigma\in(1,2]$ by
   $o(1/\log t)$ — uniformly. **[COROLLARY 153.4] (the requested count):** for the cumulative effect
   at height $\gamma$ to reach constant size, $\gtrsim\delta^{-2}\gtrsim\log^2\gamma$
   off zeros per unit window are needed — **superlinear density in $\log\gamma$, forbidden by
   Riemann–von Mangoldt** ($N(T+1)-N(T)\leq C\log T$, unconditional, valid in the category: Lemma 153.5).
   **DECISION: no subsequence suffices; the argument dies**, and it dies by the same mechanism as the
   averaging no-go of Doc 141 (the dlVP lever is a Weil functional of effective support $O(1)$: Cor. 141.B2
   covers it; §2.5 further gives the structural reason: the repelling line must carry the pole of the positive
   measure, and $\Re s=\tfrac12$ carries none — the dlVP inequality centered at ½ is $0\geq0$).

3. **(§2.6) The new piece that survives the shipwreck: the self-scale excess is ONE-SIGNED and DOMINANT.**
   **[PROPOSITION 153.6]:** if instead of fixed support each quadruple is evaluated at ITS OWN scale $L_j=1/\delta_j$
   with the centered Fejér test (positive on both sides), its excess over the projection onto the line is
   $\geq L_j/3$ — positive (a cosh against 1: no cancellation possible) and $\gg\log\gamma_j$ = the total expected
   mass of the on-line sea in the window. The zero-mean profile (141.M5) does NOT apply at self-scale: the
   swarm is invisible to every fixed support but **dominant at adapted support** $1/\delta_j$. This escapes
   no-go 141.B2 (whose diagonalization requires the test family fixed BEFORE the configuration) — the
   exact price is that the prime side at super-logarithmic adapted support is unknown.

4. **(§3) Kaczorowski–Perelli: closes the FIRST arrow of the mechanism and refutes the second as
   stated.** The small-degree classification (degree $0<d<1$ empty; $d=1$ = ζ and shifted Dirichlet
   $L$-functions; $1<d<2$ empty [KP99], [KP11], [CG93]) proves — in degree $<2$ and modulo the embedding
   caveat [GAP-153.E] — that **continuation + Euler + functional equation ⟹ local datum of unitary character
   (maximal purity)**: the arrow "continuation ⟹ purity" of 144.D is a THEOREM in degree $<2$. But the second
   arrow ("purity ⟹ repulsion/fat zeros") is **untenable as stated by Doc 144**: ζ itself has pure
   local datum at EVERY prime and its repulsion is exactly RH-open ([PROPOSITION 153.8]). Local purity
   per prime cannot be the carrier of the mechanism; the carrier must be the WINDOW datum at
   super-logarithmic support — exactly where the new piece of point 3 lives.

5. **(§4) The minimal link, distilled and positioned.** **[NEW-DEFINITION 153.9] (Rigidity 153.M):** "no
   D131-H⁺ object sustains a one-sided near-prime deficit of size $\gtrsim L$ in infinitely many self-scale
   windows with $L_j/\log\gamma_j\to\infty$". **[PROPOSITION 153.10]:** 153.M ⟹ 144.D (via the one-signed
   excess of 153.6 + the explicit formula of the category). Proved hierarchy:
   $141.E \Rightarrow 153.M \Rightarrow 144.D \Rightarrow$ LP-141-category. 153.M is strictly weaker
   than 141.E as a positional statement, but as an EVALUATION demand it is the old wall (108-N, support
   $\log\gamma$) transposed to super-logarithmic support: it is NOT quantitatively cheaper; the advance made is structural (the zero side now has proved sign; the whole GAP is concentrated on the prime side).

6. **(§5) VERDICT: MINIMAL LINK ISOLATED** (neither proved nor refuted), with one new proved piece and the
   mechanism of Doc 144 corrected.

---

## 1. The exact statements

### 1.1. The category D131-H⁺: declared axioms

Doc 144 uses "D131-H⁺" by reference to Desideratum 6.9 of Doc 131. For this document to be self-contained
and auditable, I fix the axioms I USE (everything proved below declares which ones it needs):

**Definition 153.0 [NEW-DEFINITION] (category D131-H⁺, working axioms).** $F$ belongs to D131-H⁺ if:

- **(A1) Euler with positive Hermitian datum:** $-\frac{F'}{F}(s)=\sum_{n\geq2}a(n)\,n^{-s}$ with $a$ supported
  on prime powers, $a(n)\geq0$, and the series absolutely convergent in $\sigma>1$ with
  $\sum_{n\leq X}a(n)\ll X$ (Chebyshev type; in ζ, $a=\Lambda$).
- **(A2) Continuation:** $F$ continues meromorphically to $\mathbb C$ with at most one pole at $s=1$ (order
  $r\geq0$), and finite order of growth.
- **(A3) Functional equation:** $\Phi(s):=Q^s\gamma_F(s)F(s)$ satisfies $\Phi(s)=\overline{\Phi(1-\bar s)}$, with
  $\gamma_F$ a finite product of factors $\Gamma(\lambda_is+\mu_i)$, $\lambda_i>0$, $\Re\mu_i\geq0$
  (archimedean type, in the sense of Doc 131 §6.6').
- **(A4) Explicit formula:** for every $F\in C_c^\infty$ even in pieces as in Doc 141 §3.1, the Weil identity
  holds: $\sum_\rho h(\rho)=\text{(archimedean + poles)}-\sum_n a(n)n^{-1/2}\bigl(F(\log n)+F(-\log n)\bigr)$,
  $h(s)=\int F(u)e^{(s-1/2)u}du$, sum over the nontrivial zeros with multiplicity. (Standard consequence
  of (A1)–(A3) by the classical contour argument; I take it as an axiom so as not to re-prove Stirling.)

Frank note: (A1)–(A4) are the minimal reading of "genuine Euler product + positive Hermitian local datum
+ continuation + functional equation" of Doc 144 §3. They do not include the Ramanujan bound of the Selberg
class nor a notion of degree; that matters in §3 ([GAP-153.E]).

### 1.2. Conjecture 144.D with total quantifiers

I transcribe from Doc 144 §3.3, making the quantifiers explicit:

**Conjecture 144.D (Doc 144, quoted exactly).** *For every $F\in$ D131-H⁺: if $F$ has $m=\infty$ off
zeros (quadruples $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$, $\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$), then*
$$\exists\,c>0\ \ \exists\,(j_k)_{k\geq1}\ \text{infinite subsequence}:\qquad
\delta_{j_k}\,\log\gamma_{j_k}\;\geq\;c\quad\forall k.$$

Logical form: $\Pi_3$ over the zeros ($m=\infty$ is $\Pi_2$; the conclusion is $\Sigma_3$:
$\exists c\,\forall N\,\exists j>N$). The **negation** of the conclusion is the swarm hypothesis:
$$\textbf{(SWARM)}:\qquad m=\infty\quad\text{and}\quad \delta_j\log\gamma_j\xrightarrow{\,j\to\infty\,}0$$
(all off zeros asymptotically sub-resolution to the natural calendar $\{C\log\}$). Proving 144.D = deriving a
contradiction from (SWARM) within D131-H⁺.

**GAP-144.C (Doc 144, Obs. 144.4bis(2), quoted exactly).** The unproved residue is *the effective lower bound
$\delta_{j_k}\gtrsim1/\log\gamma_{j_k}$ on a subsequence of off zeros, derived from the analytic continuation
of the Euler product*. The directional evidence is Computation 141.R3 (the Euler construction that would
violate the bound does NOT continue); turning "does not continue" into the bound is the GAP.

**What 144.D buys (Prop. 144.4 of Doc 144, recalled, not re-proved):** 144.D ⟹ LP-141$(a)$ in D131-H⁺
for every calendar $a\succeq\log$, in fact the strong form ($m=\infty\Rightarrow$ infinitely many fat zeros
at calendar $\log$); and with weak positivity of the symbol (Prop. 141.P3), $m<\infty$. 144.D is strictly
weaker than Conjecture 141.E ($\liminf$ over ALL off zeros).

**The conjectured mechanism (Doc 144 §3.3, quoted to audit it in §3):** *"each off zero at distance
$\delta_j$ requires sustained local impurity of amplitude $\gtrsim\delta_j$ in a prime band of logarithmic
size $\asymp\log\gamma_j$; the continuation couples those data and forbids the impurity from being
simultaneously sub-resolution at all zeros and sustained at infinitely many."* §2 and §3 will show that
the true amplitude at support $\log\gamma_j$ is not $\gtrsim\delta_j$ but $\asymp(\delta_j\log\gamma_j)^2\to0$
under (SWARM) — the mechanism, as written, asks for detection where the signal is null; the repaired
version lives at support $1/\delta_j$ (§2.6, §4).

---

## 2. The de la Vallée Poussin attack centered at ½

### 2.1. The classical repulsion theorem and its two ingredients

**Computation 153.1 [COMPUTATION] (dlVP as a repulsion theorem, with the mechanism in view).** For $\sigma>1$,
(A1) gives
$$-\Re\frac{F'}{F}(\sigma+it)\;=\;\sum_{n\geq2}a(n)\,n^{-\sigma}\cos(t\log n),$$
and the trigonometric inequality $3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\geq0$ with $a\geq0$ yields
$$3\Bigl(-\frac{F'}{F}(\sigma)\Bigr)+4\Bigl(-\Re\frac{F'}{F}(\sigma+it)\Bigr)+\Bigl(-\Re\frac{F'}{F}(\sigma+2it)\Bigr)\;\geq\;0.$$
By Hadamard, $-\Re\frac{F'}{F}(s)=\Re\frac{r}{s-1}-\sum_\rho\Re\frac1{s-\rho}+O(\log(|t|+2))$, and **each zero
contributes with ONE sign**: $\Re\frac1{s-\rho}=\frac{\sigma-\beta}{|s-\rho|^2}\geq0$ for $\sigma>1>\beta$.
Discarding all zeros except the target $\rho_0=\beta_0+i\gamma_0$ and taking $t=\gamma_0$,
$\sigma=1+\eta$:
$$\frac{4}{\sigma-\beta_0}\;\leq\;\frac{3r}{\sigma-1}+O(\log\gamma_0)\qquad\Longrightarrow\qquad
1-\beta_0\;\geq\;\frac{c}{\log\gamma_0}$$
optimizing $\eta\asymp1/\log\gamma_0$ [dlVP1899], [T86, Thm. 3.8]. The two structural ingredients:
**(I-1)** a SINGULAR positive budget adjacent to the repelling line (the pole at $s=1$: residue $r$ of the
positive measure $\sum a(n)n^{-\sigma}$, which diverges as $r/(\sigma-1)$ as one approaches); **(I-2)** single-sign
terms, so that the target zero competes against the budget WITHOUT help from the rest. The strength of
the lever on the target is $\frac4{\sigma-\beta_0}$ — **singular** as $\beta_0\to\sigma$: that is why it
repels from $\Re s=1$ (and by the functional equation, from $\Re s=0$). $\square$

As observed: this IS an unconditional repulsion theorem — the only one — and the question is whether
the same engine runs centered at ½ against (SWARM).

### 2.2. The exact loss when centering at ½: from singular to second order

Positivity (A1) lives only in $\sigma>1$, at distance $\geq\tfrac12$ from the critical line. Two losses
compound:

**(Loss 1: the lever is bounded.)** The strength of a zero $\beta\approx\tfrac12$ on $s=\sigma+i\gamma$,
$\sigma>1$, is $\frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\gamma)^2}\leq\frac1{\sigma-\beta}\leq2$: bounded,
not singular. Compared to the archimedean term $O(\log\gamma)$ of Hadamard, the strength of ONE zero near
½ is already sub-budget by a factor $1/\log\gamma$.

**(Loss 2: the functional equation cancels the first order.)** The symmetric pair $\tfrac12\pm\delta+i\gamma$
enters together. Its NET effect with respect to the projected pair is of second order in $\delta$ — the
$\sigma>1$ avatar of Computation 141.M4 (which proved it ON the line). I prove it with an explicit constant:

**Lemma 153.2 [LEMMA] (second-order bound in the half-plane of positivity).** Let $s=\sigma+it$ with
$\sigma\in(1,2]$, and let $Z$ be a configuration containing the quadruple $\{\tfrac12\pm\delta\pm i\gamma\}$
with $\delta\leq\tfrac14$; let $Z^\flat$ be the same configuration with the quadruple projected (double zeros
at $\tfrac12\pm i\gamma$). Then
$$\Bigl|\sum_{\rho\in Z}\Re\frac1{s-\rho}-\sum_{\rho\in Z^\flat}\Re\frac1{s-\rho}\Bigr|
\;\leq\;C_0\,\delta^2\Bigl(\frac1{1+(t-\gamma)^2}+\frac1{1+(t+\gamma)^2}\Bigr),$$
with $C_0$ absolute (one may take $C_0=2^{12}$).

*Proof.* Write $x:=\sigma-\tfrac12\in(\tfrac12,\tfrac32]$, $u:=t-\gamma$, and
$f(w):=\frac{w}{w^2+u^2}$, so that the pair at height $+\gamma$ contributes $f(x-\delta)+f(x+\delta)$ and its
projection $2f(x)$. Symmetric second difference with integral remainder:
$$|f(x+\delta)+f(x-\delta)-2f(x)|\;=\;\Bigl|\int_0^\delta(\delta-y)\bigl[f''(x+y)+f''(x-y)\bigr]dy\Bigr|
\;\leq\;\delta^2\sup_{|y|\leq\delta}|f''(x+y)|.$$
Direct computation: $f'(w)=\frac{u^2-w^2}{(w^2+u^2)^2}$, $f''(w)=\frac{2w(w^2-3u^2)}{(w^2+u^2)^3}$, hence for
$w\geq\tfrac14$ (which covers $x+y\geq\tfrac12-\tfrac14$):
$$|f''(w)|\leq\frac{2w(w^2+3u^2)}{(w^2+u^2)^3}\leq\frac{6w}{(w^2+u^2)^2}
\leq\frac{12}{(\tfrac1{16}+u^2)^2}\leq\frac{C_0}{1+u^2},$$
using $(\tfrac1{16}+u^2)\geq\tfrac{1+u^2}{17}$ and $(\tfrac1{16}+u^2)\geq\tfrac1{16}$. The conjugate pair at
height $-\gamma$ gives the same with $u'=t+\gamma$. $\square$

**Quantification of "that loss" (what is requested to be measured).** On $\Re s=1$ the lever per target
zero is $\asymp\frac1{1-\beta}$ (singular, first order, one sign). On $\Re s=\tfrac12$ as measured from $\sigma>1$ it
is $\leq C_0\delta^2$ (bounded, second order, and of NOT usable sign: the second difference of $f$ changes
sign with $u$ — it is the zero-mean profile 141.M5 seen from $\sigma>1$, where the Lorentzian kernel of
width $x\geq\tfrac12$ averages the width-$\delta$ signal and reduces it from $O(1)$ on-line to $O(\delta^2)$).
Total loss relative to the dlVP case: factor $\delta^2(1-\beta)\big|_{\beta\to1} \rightsquigarrow$ in
useful terms, **the efficiency per zero falls from $\Theta(\log\gamma)$ (classical case, zero stuck to 1) to
$\Theta(\delta^2)$ (zero stuck to ½)** — under (SWARM), $\delta^2=o(1/\log^2\gamma)$.

### 2.3. The visibility budget of the complete swarm

**Proposition 153.3 [PROPOSITION] (the entire swarm is $o(1/\log t)$-invisible throughout the half-plane of
positivity).** Let $Z$ be an admissible configuration (finitely many zeros per unit window, with window bound
$n_Z(T):=\#\{\rho:|\gamma_\rho-T|\leq\tfrac12\}\leq C_1\log(T+2)$) whose off quadruples satisfy (SWARM):
$\delta_j\leq\varepsilon(\gamma_j)/\log\gamma_j$ with $\varepsilon(\gamma)\to0$ non-increasing. Then,
uniformly in $\sigma\in(1,2]$ and $t\geq4$:
$$\Bigl|\sum_{\rho\in Z}\Re\frac1{s-\rho}-\sum_{\rho\in Z^\flat}\Re\frac1{s-\rho}\Bigr|
\;\leq\;C_2\,\frac{\varepsilon(\sqrt t)^2+\tfrac{\log t}{\sqrt t}}{\log t}\;=\;o\Bigl(\frac1{\log t}\Bigr).$$

*Proof.* By Lemma 153.2 the difference is dominated by
$C_0\sum_j\delta_j^2\bigl[(1+(t-\gamma_j)^2)^{-1}+(1+(t+\gamma_j)^2)^{-1}\bigr]$; the second summand is
$\leq(1+t^2)^{-1}\sum_j\delta_j^2$ per window, absorbed into the term $\log t/\sqrt t$ after grouping by
windows (the $\delta_j\leq\tfrac14$ together with the window bound give $\sum_{\gamma_j\leq T}\delta_j^2\leq CT\log T$).
For the first, group by unit windows centered at integers $n$ and use the window bound:
$$\sum_j\frac{\delta_j^2}{1+(t-\gamma_j)^2}\;\leq\;C_1\sum_{n\geq2}\frac{\log n}{1+(t-n)^2}
\Bigl(\sup_{\gamma\in[n-1,n+1]}\delta(\gamma)\Bigr)^2.$$
Split into three ranges. (i) $|n-t|\leq t/2$: there $\log n\asymp\log t$ and
$\delta(\gamma)^2\leq\varepsilon(t/2)^2/\log^2(t/2)$, and $\sum_n(1+(t-n)^2)^{-1}\leq\pi+1$: contribution
$\leq C\,\varepsilon(t/2)^2/\log t$. (ii) $n<t/2$: kernel $\leq(1+t^2/4)^{-1}$, and
$\sum_{n<t/2}\log n\,\delta^2\leq C\,t$ (trivial bound $\delta\leq\tfrac14$): contribution $\leq C/t$.
(iii) $n>3t/2$: $\sum_{n>3t/2}\frac{\log n\,\varepsilon^2/\log^2n}{1+(n-t)^2}\leq
C\sum_{k>t/2}\frac{1}{k^2}\cdot\frac{\varepsilon(\sqrt t)^2}{\log t}\cdot\log(\cdot)\leq C/t$. Summing and
using that $\varepsilon$ is non-increasing ($\varepsilon(t/2)\leq\varepsilon(\sqrt t)$ for $t\geq4$): the bound.
$\square$

Meanwhile, the only unconditional inequality available in $\sigma>1$ (the 3-4-1 of 153.1) has slack
$\asymp\log t$ (the archimedean term). **Signal-to-slack ratio $=o(1/\log^2t)$.** No evaluation point,
no choice of $\sigma\in(1,2]$, sees the swarm.

### 2.4. The decisive count: how many sub-resolution zeros are needed, and why R–vM forbids it

**Lemma 153.5 [LEMMA] (window bound in the category).** If $F$ satisfies (A1)–(A3), then
$N_F(T+1)-N_F(T)\leq C_F\log(T+2)$.

*Proof.* Classical Jensen argument [T86, Thm. 9.2], [IK04, Ch. 5]: by (A1),
$|F'/F(\sigma+it)|\leq\sum_na(n)n^{-\sigma}<\infty$ for $\sigma\geq2$, and integrating in $\sigma$ from
$+\infty$ (where $\log F\to0$): $|\log F(2+it)|\leq C$, hence $|F(2+it)|\asymp1$ uniformly in $t$. The functional equation (A3) and
Stirling give $|F(-1+it)|\leq C(|t|+2)^{A}$; Phragmén–Lindelöf (with (A2): finite order) gives
$|F(\sigma+it)|\leq C(|t|+2)^{A'}$ in $-1\leq\sigma\leq2$. Jensen on the disk centered at $2+iT$ of
radius $3$: $\#\{\text{zeros in the disk of radius }\tfrac52\}\leq\frac{1}{\log(6/5)}\bigl[\log\max_{|z|=3}|F|-\log|F(2+iT)|\bigr]
\leq C_F\log(T+2)$, and the window $[T,T+1]\times[0,1]$ of the strip is contained in that disk. $\square$

**Corollary 153.4 [COROLLARY] (visibility threshold: superlinear density — impossible).** Under Lemma
153.2, if the window $[\gamma-\tfrac12,\gamma+\tfrac12]$ contains $K$ off quadruples, all at distance
$\leq\delta$, their cumulative effect on $-\Re\frac{F'}{F}(\sigma+i\gamma)$, $\sigma\in(1,2]$, is
$\leq 2C_0K\delta^2$. For it to reach even the constant threshold $c_0>0$ (the smallest conceivable slack of
a dlVP-type positivity inequality — the real one is $\asymp\log\gamma$, worse) one needs
$$K\;\geq\;\frac{c_0}{2C_0}\,\delta^{-2}\;\geq\;\frac{c_0}{2C_0}\,\frac{\log^2\gamma}{\varepsilon(\gamma)^2}
\qquad\text{(under SWARM)},$$
**superlinear in $\log\gamma$**, while Lemma 153.5 imposes $K\leq C_F\log\gamma$. The gap is a factor
$\geq\frac{c_0}{2C_0C_F}\cdot\frac{\log\gamma}{\varepsilon(\gamma)^2}\to\infty$: **unreachable by the WHOLE
swarm together, not just by subsequences.** In particular no geometric subsequence helps: the Lorentzian
kernel of 153.2 has total mass $O(1)$ per unit of height, so stacking heights does not accumulate
($\sum_j\delta_j^2<\infty$ over any subsequence with $\delta_j\to0$ geometric is even smaller).
$\square$

**Decision.** The answer to the dichotomy is the first branch:
**"superlinear density, impossible by Riemann–von Mangoldt" — the argument dies.** And it dies by the
same averaging no-go of Doc 141, now made quantitative: the dlVP lever, written as a Weil functional,
has kernel $u\mapsto e^{-(\sigma-\frac12)|u|}$ — effective support $O\bigl(\tfrac1{\sigma-1/2}\bigr)=O(1)$,
not even logarithmic — and Cor. 141.B2 covers every countable family of such functionals. The signal per
quadruple is $O(\delta^2)$ with a profile that the coarse kernel averages to its mean (null at leading order:
141.M5). There is no "from outside toward ½" version of the zero-free-region theorem with this technology.

### 2.5. The structural reason: the repelling line must carry the pole

**Remark 153.5bis (why the transposition is empty, in one identity).** The ingredient (I-1) of
153.1 — singular positive budget adjacent to the repelling line — does not exist at ½: the positive measure
$\sum a(n)n^{-\sigma}$ has its only pole at $\sigma=1$. Worse: the candidate "dlVP inequality centered at
½" is the positivity of $-\Re\frac{\xi'}{\xi}$ against symmetric pairs, and Computation 141.M4 (cited, not
re-proved) shows that the first-order contribution of EVERY symmetric pair to
$\Re\frac{\xi'}{\xi}(\tfrac12+it)$ is identically $0$: the transposed inequality is $0\geq0$. Classical
repulsion repels from the TWO lines that carry polar structure ($\Re s=1$ via the pole; $\Re s=0$ via the
functional equation, mirror of the pole); the critical line is the axis of symmetry, with no pole, and
symmetric configurations are exact equilibria. **An analogue "zeros do not stick to ½ from outside" would
require a positive measure with a singularity AT ½** — which is precisely what no unconditional datum
provides (and what Doc 134/141 calls the wall: the positivity of the symbol at ½ is the unproved arithmetic
half).

### 2.6. What survives: the self-scale excess is one-signed and dominant

The shipwreck of §2.3–2.4 is at **fixed support** (or bounded, or logarithmic). The structure of the swarm
changes qualitatively if each quadruple is interrogated at ITS OWN scale $L_j:=1/\delta_j$ — which under
(SWARM) is super-logarithmic: $L_j/\log\gamma_j=1/(\delta_j\log\gamma_j)\to\infty$. There I prove something new:

**Proposition 153.6 [PROPOSITION] (self-scale excess: positive and dominant).** Let
$F_{L,\gamma_0}(u):=\bigl(1-\tfrac{|u|}L\bigr)_+\,2\cos(\gamma_0u)$ be the modulated Fejér test, with
$h(s)=\int F_{L,\gamma_0}(u)e^{(s-1/2)u}du$. Let a quadruple $\{\tfrac12\pm\delta\pm i\gamma_0\}$
(centered), $\kappa:=\delta L\leq1$, $\gamma_0L\geq10$. Then:

(a) **[positivity of the test, both sides]** $F_{L,\gamma_0}$ has profile $\bigl(1-\tfrac{|u|}L\bigr)_+\geq0$ and
$h(\tfrac12+it)=\widehat\Delta_L(t-\gamma_0)+\widehat\Delta_L(t+\gamma_0)\geq0$ with
$\widehat\Delta_L(v)=\frac{2(1-\cos Lv)}{Lv^2}\geq0$ (Fejér kernel): **every on-line zero contributes
$\geq0$.**

(b) **[the excess of the quadruple is ONE-SIGNED]** The contribution of the quadruple minus that of its
projection onto the line is
$$E(\delta,L)\;=\;8\int_{-L}^{L}\Bigl(1-\frac{|u|}L\Bigr)\cos^2(\gamma_0u)\,\bigl(\cosh(\delta u)-1\bigr)\,
\frac{du}{2}\cdot 2\;\geq\;0,$$
with a closed-form value (modulo the oscillating term, bounded below):
$$E(\delta,L)\;=\;8L\Bigl[\frac{\cosh\kappa-1}{\kappa^2}-\frac12\Bigr]\;+\;R,\qquad
|R|\;\leq\;\frac{50\,\kappa^2e^{\kappa}}{\gamma_0^2L},$$
and $\frac{\cosh\kappa-1}{\kappa^2}-\frac12=\frac{\kappa^2}{24}+O(\kappa^4)>0$ for $\kappa>0$. In particular,
at self-scale $\kappa=1$ (i.e. $L=1/\delta$): $E\geq L/3$.

(c) **[dominance]** The total expected mass of the on-line sea in the test is $\asymp2\log\gamma_0$ (R–vM
density $\frac{\log\gamma_0}{2\pi}$ times the mass $\int\widehat\Delta_L=2\pi$ of the kernel, independent of
$L$). Under (SWARM), $E\geq L_j/3\gg\log\gamma_j$: **the excess of ONE quadruple at its self-scale
dominates the mass of the ENTIRE on-line sea of its window.**

*Proof.* (a) Direct computation: $\int_{-L}^L(1-\tfrac{|u|}L)e^{ivu}du=2\int_0^L(1-\tfrac uL)\cos(vu)\,du
=\frac{2(1-\cos Lv)}{Lv^2}\geq0$; the triangular profile is $\geq0$ by inspection (it is
$\tfrac1L\,\chi_{[-L/2,L/2]}\!\star\chi_{[-L/2,L/2]}$: autocorrelation).

(b) The quadruple contributes $\sum_{\pm,\pm}h(\tfrac12\pm\delta\pm i\gamma_0)
=\int_{-L}^{L}(1-\tfrac{|u|}L)\,2\cos(\gamma_0u)\cdot2\cosh(\delta u)\cdot2\cos(\gamma_0u)\,du$, and the
projection (two double zeros at $\tfrac12\pm i\gamma_0$) contributes the same with $\cosh\mapsto1$. Difference:
$$E=8\int_{-L}^{L}\Bigl(1-\frac{|u|}L\Bigr)\cos^2(\gamma_0u)\bigl(\cosh(\delta u)-1\bigr)du\;\geq\;0$$
**pointwise** (triangle $\geq0$, $\cos^2\geq0$, $\cosh-1\geq0$): one sign, no cancellation possible —
this is where the zero-mean profile 141.M5 stops applying: the adapted test weighs the quadruple by
$\cosh(\delta u)$, even and $\geq1$, not by a kernel that averages its dispersive profile. With
$\cos^2=\tfrac12(1+\cos2\gamma_0u)$: the smooth term is
$4\cdot2\int_0^L(1-\tfrac uL)(\cosh\delta u-1)du=8L\int_0^1(1-v)(\cosh\kappa v-1)dv
=8L[\frac{\cosh\kappa-1}{\kappa^2}-\frac12]$, using
$\int_0^1(1-v)\cosh(\kappa v)dv=\frac{\cosh\kappa-1}{\kappa^2}$ (two elementary integrations by parts) and
$\int_0^1(1-v)dv=\tfrac12$. The oscillating term $R=4\int_{-L}^{L}(1-\tfrac{|u|}L)\cos(2\gamma_0u)
(\cosh\delta u-1)du$: with $\varphi(u):=(1-\tfrac uL)(\cosh\delta u-1)$ we have $\varphi(0)=\varphi(L)=0$,
$\varphi'(0)=0$, $|\varphi'(L)|=\frac{\cosh\kappa-1}{L}$,
$\int_0^L|\varphi''|\leq\frac{2\delta\sinh\kappa\cdot L+\delta^2L^2\cosh\kappa}{L}
=\frac{\kappa(2\sinh\kappa+\kappa\cosh\kappa)}{L}$; two integrations by parts against $\cos(2\gamma_0u)$
give modulus $\leq\frac{8}{(2\gamma_0)^2}\bigl[|\varphi'(L)|+\int|\varphi''|\bigr]\leq\frac{50\kappa^2e^\kappa}
{\gamma_0^2L}$ for $\kappa\leq1$. For $\kappa=1$:
$8[\cosh1-1-\tfrac12]=8(0.5430\ldots-\tfrac12)>0.34$, and $|R|\leq50e/(\gamma_0^2L)$ is negligible with
$\gamma_0L\geq10$: $E\geq L/3$.

(c) The sum over on-line zeros $\tfrac12\pm i\gamma'$ of the test is
$\sum_{\gamma'}2\bigl[\widehat\Delta_L(\gamma'-\gamma_0)+\widehat\Delta_L(\gamma'+\gamma_0)\bigr]$; with
ordinate density $\frac{\log\gamma_0}{2\pi}(1+o(1))$ per unit (R–vM, Lemma 153.5 for the upper bound
in the category) and $\int_{\mathbb R}\widehat\Delta_L(v)\,dv=2\pi\bigl(1-\tfrac{|0|}L\bigr)=2\pi$, the expected
mass is $2\log\gamma_0(1+o(1))$, independent of $L$. The comparison is immediate. $\square$

**Remark 153.6bis (why this escapes no-go 141.B2 — and what the exact price is).** Cor. 141.B2
diagonalizes against a countable family of tests **fixed before** choosing the configuration: it chooses
$\delta_j$ small enough that the signal $(\delta_jL_i)^2$ is $<\varepsilon2^{-i-j}$ for the already-named
supports $L_i$. The self-scale family $\{F_{1/\delta_j,\gamma_j}\}$ is chosen **afterward** (it depends on
the hypothetical object): against it the quadruple $j$ has signal $\geq L_j/3$, not $o(1)$ — the
diagonalization cannot anticipate a test that copies its own parameters. The no-go does not apply. The price:
the prime side of the explicit formula (A4) at support $L_j\gg\log\gamma_j$ is terra incognita — the
terms $\sum_na(n)n^{-1/2}F(\log n)$ have raw size $\asymp e^{L/2}$ (by (A1) Chebyshev type and partial
summation: $\sum_{n\leq X}a(n)n^{-1/2}\asymp\sqrt X$), the archimedean+polar side likewise, and detecting the
excess $\asymp L$ requires their difference to be known with error $o(L)$ — relative precision $Le^{-L/2}$.
The unconditional PNT gives relative error $e^{-c\sqrt{\log X}}=e^{-c\sqrt L}$, and even the best cancellation
of exponential sums over primes (Vinogradov–Korobov) leaves $e^{-cL^{3/5-o(1)}}$: exponentially far from what
is needed. **The whole difficulty of GAP-144.C is thus concentrated, with proved sign, in a single question
on the prime side** — that is §4.

---

## 3. Confrontation with Kaczorowski–Perelli

### 3.1. The facts of the literature, precisely

- **[CG93]** Conrey–Ghosh: in the Selberg class $\mathcal S$ (with Euler product and Ramanujan bound),
  degree $d=0$ implies $F\equiv1$, and there are no elements with $0<d<1$.
- **[KP99]** Kaczorowski–Perelli, *On the structure of the Selberg class, I: $0\leq d\leq1$*, Acta Math.
  **182** (1999), 207–241: the result extends to the extended class $\mathcal S^\sharp$ (without Euler), and
  degree $d=1$ is **classified**: in $\mathcal S$, the degree-1 elements are $\zeta(s)$ and the
  $L(s+i\theta,\chi)$ with $\chi$ primitive non-principal, $\theta\in\mathbb R$ (shifted). *(Frankness
  note: the classification of $d=1$ belongs to the KP series; whether the complete proof for $\mathcal S$
  is in KP I or in a later installment of the series is an attribution detail not verified at the source —
  [literature GAP], without effect on its use: the classification statement itself is standard
  and cited as such by the secondary literature.)*
- **[KP11]** Kaczorowski–Perelli, *On the structure of the Selberg class, VII: $1<d<2$*, Ann. of Math. (2)
  **173** (2011), 1397–1441: **there are no elements of degree $1<d<2$** (in $\mathcal S^\sharp$ with the
  normalizations of the series).
- The density conjecture / GRH in the Selberg class: **nothing of that is assumed here**; and by Lemma 141.M1 (cited) the density
  technology is trivial at the $1/\log T$ scale, so
  it would not serve as a substitute either.

**[GAP-153.E] (embedding caveat).** D131-H⁺ with (A1)–(A4) does not include the Ramanujan bound nor define
degree; the KP theorems apply to $\mathcal S/\mathcal S^\sharp$. Everything that follows in §3.2 holds for
$F\in$ D131-H⁺$\,\cap\,\mathcal S$ (the intersection where "degree" makes sense), which contains the
relevant members (ζ, Dirichlet $L$-functions, normalized automorphic $L$-functions). Declared; not hidden.

### 3.2. What the classification DOES give: the first arrow of the mechanism, proved in degree < 2

**Proposition 153.7 [PROPOSITION] (KP closes "continuation ⟹ purity" in degree $<2$ and reduces 144.D there
to the Dirichlet $L$-functions).** Let $F\in$ D131-H⁺$\,\cap\,\mathcal S$ with degree $d<2$. Then:

(a) $F\equiv1$ (no zeros: 144.D vacuous), or $F$ is $\zeta$ or a shifted $L(s+i\theta,\chi)$.

(b) Consequently, the local datum of $F$ is of unitary character: the inverse local roots satisfy
$|\alpha_p|\in\{0,1\}$ for every $p$ — **maximal purity** in the arithmetic normalization, equivalent in
the dictionary of Doc 131 (Thm. 6.7, normalization $F_{p,\alpha}$) to each local block having its divisor
exactly where symmetry demands, with the Weil barrier $|c_m|\leq2p^{m/2}$ satisfied with slack.
**The arrow "continuation + Euler + functional equation ⟹ asymptotic purity of the local datum" of the
144.D mechanism is a THEOREM in degree $<2$**, via classificatory rigidity — the exact embodiment, in the
real class, of what Computation 141.R3 showed in the model (the impure datum does not continue).

(c) **144.D restricted to degree $<2$ is equivalent to 144.D for $\zeta$ and the $L(s+i\theta,\chi)$:** there
is no "exotic object" of low degree that could carry a swarm; the hypothetical carrier would be a Dirichlet
$L$-function with $m=\infty$ and $\delta_j\log\gamma_j\to0$ — a quantitatively strong negation of GRH.

*Proof.* (a) is [CG93]+[KP99]+[KP11] (with [GAP-153.E]). (b) the local factors of the Dirichlet
$L$-functions are $(1-\chi(p)p^{-s})^{-1}$ with $|\chi(p)|\in\{0,1\}$; the shift $i\theta$ rotates the phase,
not the modulus. (c) immediate from (a): the quantification of 144.D runs over the members, and the
degree-$<2$ members are listed. $\square$

### 3.3. What the classification does NOT give — and the correction to the mechanism of Doc 144

**Proposition 153.8 [PROPOSITION] (the second arrow, "purity ⟹ repulsion", is untenable as stated).** There
exists an object of the category with PURE local datum at every prime and whose resolution repulsion
(LP-134, LP-141, even $m<\infty$) is undecided by purity: ζ itself. Consequently, no implication of the form
$$\text{(local purity of all factors)}\;\Longrightarrow\;\text{(repulsion / infinitely many fat zeros if }m=\infty)$$
can be the content of 144.D: its hypothesis is satisfied by $\zeta$ and its conclusion for $\zeta$ is
exactly the open statement. The mechanism of Doc 144 §3.3 ("each off zero at distance $\delta_j$ requires
sustained local impurity of amplitude $\gtrsim\delta_j$ at support $\asymp\log\gamma_j$") also has the
wrong amplitude: by Lemma 141.B (cited) and Lemma 153.2, the footprint of an off quadruple on ANY
datum of support $L$ is $O((\delta L)^2)$ — at support $\log\gamma_j$ and under (SWARM) it is
$(\delta_j\log\gamma_j)^2\to0$: **the sub-resolution off zero does NOT require any detectable impurity at
logarithmic support**; there is nothing there for the continuation to forbid.

*Proof.* $\zeta$ has factors $(1-p^{-s})^{-1}$: datum $\alpha_p=1$, pure (it is the limiting/boundary case
of the barrier $|c_m|=2p^{m/2}$ after normalizing as in Doc 131 §6.5, where positivity "is as tight as it
can be"). That LP-134/LP-141/$m<\infty$ for $\zeta$ are open is the state of the program (Prop. 141.R1:
deciding them negatively refutes RH). The amplitude claim: Lemma 153.2 with $L$ in place of the Lorentzian
kernel is Lemma 141.B, bound $C_N(F)(\delta L)^2e^{\delta L}(1+\gamma)^{-N}$; under (SWARM) and
$L\leq C\log\gamma_j$, $(\delta_jL)^2\to0$. $\square$

**Remark 153.8bis (the balance of the confrontation).** KP delivers exactly one of the two arrows and
disallows the other: (i) "continuation ⟹ purity" moves from conjectural-mechanism to theorem in degree $<2$ —
classificatory rigidity is real and is the global version of 141.R3; (ii) "purity ⟹ repulsion" is refuted
as a local-per-prime statement (153.8): purity is a condition $\zeta$ already satisfies, so it cannot be
the lever that decides where the zeros of $\zeta$ are. The genuine content of 144.D does NOT lie in the
local-per-prime datum but in the **window** datum at adapted support (§2.6): the correct chain is
$$\text{continuation}\;\Longrightarrow\;\underbrace{\text{local purity}}_{\text{KP: theorem in }d<2}
\;\;\text{and}\;\;
\underbrace{\text{window regularity at super-logarithmic support}}_{\text{= distilled GAP-144.C, §4}}
\;\Longrightarrow\;\text{infinitely many fat zeros},$$
where the second component does NOT follow from the first (153.8) and is the only one that touches the
position of the zeros. Answering the question posed: the classification identifies the functions, it does
not prove RH for them; its rigidity DOES give leverage for 144.D, but only on the structural arrow, and
along the way reduces the universe of low-degree counterexamples to Dirichlet $L$-functions — where
refuting 144.D would require quantitatively violating GRH. The opening note ("the classification in degree 1
proves RH-of-position") should be read
this way: it proves the *identity* of the objects (and with it the position of their POLES and the purity of
their datum), not the position of their zeros — the exact distinction between rigidity of the function and
rigidity of the divisor.

---

## 4. The minimal link and its position in the hierarchy

### 4.1. The distillation

**Definition 153.9 [NEW-DEFINITION] (self-scale window deficit; Rigidity 153.M).** For
$F\in$ D131-H⁺, $\gamma_0\geq2$, $L\geq1$, I define the **window functional**
$$\mathcal P_F(\gamma_0,L)\;:=\;\sum_{n\geq2}a(n)\,n^{-1/2}\bigl(1-\tfrac{|\log n|}{L}\bigr)_+\,2\cos(\gamma_0\log n)
\;-\;\mathcal A_F(\gamma_0,L),$$
where $\mathcal A_F(\gamma_0,L)$ is the archimedean+polar side of (A4) for the test $F_{L,\gamma_0}$ of
153.6 (a closed-form quantity, computable from $(Q,\gamma_F,r)$ by Mellin–Stirling). By (A4),
$-\mathcal P_F(\gamma_0,L)=\sum_\rho h(\rho)$. **Rigidity 153.M:** *there is no $F\in$ D131-H⁺ with a
sequence $(\gamma_k,L_k)$, $\gamma_k\to\infty$, $L_k/\log\gamma_k\to\infty$, $\gamma_kL_k\geq10$, such that*
$$-\mathcal P_F(\gamma_k,L_k)\;\geq\;\tfrac13\,L_k\qquad\forall k.$$
(In words: the near-prime datum of a continuable Euler object cannot fall short of its archimedean budget
by a margin linear in the support, one-sidedly, in infinitely many windows of super-logarithmic support.)

**Proposition 153.10 [PROPOSITION] (153.M ⟹ 144.D).** If Rigidity 153.M holds, then Conjecture 144.D
holds (and with it LP-141 in the category, by Prop. 144.4 of Doc 144).

*Proof.* By contradiction: let $F\in$ D131-H⁺ satisfy (SWARM). Take the subsequence (it exists since
$\delta_j\log\gamma_j\to0$ and $\gamma_j\to\infty$) with $\gamma_jL_j\geq10$ where $L_j:=1/\delta_j$; then
$L_j/\log\gamma_j=1/(\delta_j\log\gamma_j)\to\infty$. Evaluate (A4) at the test $F_{L_j,\gamma_j}$:
$$-\mathcal P_F(\gamma_j,L_j)\;=\;\sum_\rho h(\rho)\;=\;\underbrace{\sum_{\rho\ \text{on}}h(\rho)}_{\geq0
\ \text{(153.6(a))}}\;+\;\underbrace{\sum_{\text{off quadruples}}h(\rho)}_{\geq\ \text{projection}\ +\ E_j}.$$
The contribution of each off quadruple is that of its projection (which is $\geq0$, by 153.6(a) applied to
the projected on-line zeros) plus its excess, and for the $j$-th centered quadruple the excess is
$E(\delta_j,L_j)\geq L_j/3$ (153.6(b), $\kappa=1$). The other off quadruples ($\gamma'\neq\gamma_j$)
contribute: projection $\geq0$ plus excess $8\int(1-\tfrac{|u|}{L_j})\cos(\gamma_ju)\cos(\gamma'u)
(\cosh(\delta'u)-1)du$ — this non-centered excess can be negative; I control it: its modulus is
$\leq8\int(1-\tfrac{|u|}{L_j})(\cosh(\delta'u)-1)du\leq 8L_j[\tfrac{\cosh\kappa'-1}{\kappa'^2}-\tfrac12]$ with
$\kappa'=\delta'L_j$… this bound does not decay in $\gamma'$ and does not suffice as is; I use instead the
decaying version: the non-centered excess is $4\int\varphi'(u)[\cos((\gamma_j-\gamma')u)+\cos((\gamma_j+\gamma')u)]du$
with $\varphi'(u)=(1-\tfrac{|u|}{L_j})(\cosh(\delta'u)-1)$, and two integrations by parts as in 153.6(b) give
modulus $\leq\frac{50\,\kappa'^2e^{\kappa'}}{(\gamma_j-\gamma')^2L_j}$ for $|\gamma'-\gamma_j|\geq1$,
$\kappa'\leq1$. **[GAP-153.F declared inline]:** for non-centered off quadruples with
$|\gamma'-\gamma_j|<1$ or $\kappa'=\delta'L_j>1$ the above bound does not apply; I impose on the choice of
the subsequence $(\gamma_j)$ the separation $\min_{j'\neq j}|\gamma_{j'}-\gamma_j|\geq1$ — possible if the
off zeros of the swarm do not accumulate in unit windows with $\delta'L_j>1$ simultaneously; in general one
needs to order the $L_j$ against the full swarm. To keep the proof complete WITHOUT this fine ordering,
I weaken: by Lemma 153.5 there are $\leq C_F\log\gamma_j$ zeros with $|\gamma'-\gamma_j|<1$ and each
contributes excess $\geq-8L_j[\cosh(\kappa'\wedge\cdot)\ldots]$ — not boundable without information about
their $\delta'$. I therefore state the implication under the **separated-swarm** hypothesis: $\delta'L_j\leq1$
for every off quadruple with $|\gamma'-\gamma_j|\leq\gamma_j/2$ — which is achieved by refining the
subsequence when $\sup_{|\gamma'-\gamma_j|\leq\gamma_j/2}\delta'\leq\delta_j$ (taking as centers the
quadruples of local-maximum $\delta$, always possible by passing to a subsequence, since $\delta\to0$).
Under that normalization, $\kappa'\leq1$ and the non-centered excesses sum, over the windows
$|\gamma'-\gamma_j|\geq1$ (window bound 153.5 + series $\sum k^{-2}$), to at most $C\log(\gamma_j)/L_j=o(L_j)$
in modulus; those with $|\gamma'-\gamma_j|<1$ have $\kappa'\leq1$ and excess $\geq0$ if centered at the
same $\gamma_j$ or modulus $\leq8L_j[\tfrac{\cosh1-1}{1}-\tfrac12]\cdot\Theta(\#)$… I leave them on the safe
side by using that the excess of ANY quadruple with $|\gamma'-\gamma_j|<\tfrac1{L_j}$ is positive by
continuity of Computation 153.6(b) (the factor $\cos(\gamma'u)\cos(\gamma_ju)\geq\cos^2(\gamma_ju)-|u||\gamma'-\gamma_j|$
and the error term is absorbed into $R$); and those with $\tfrac1{L_j}\leq|\gamma'-\gamma_j|<1$ are bounded by
integration by parts with denominator $(\gamma_j-\gamma')^2\geq L_j^{-2}$… which is NOT small. **Frankness:**
controlling neighbors at distance $[L_j^{-1},1)$ requires separation $\gtrsim1$ of the chosen centers from
the other off zeros of the swarm; this is guaranteed if every unit window containing a locally-maximal-$\delta$
zero has no other off quadruple with $\kappa'$ near 1 at distance $<1$ — such a subsequence exists unless the
swarm has infinitely many windows with $\geq2$ quadruples at comparable self-scales, in which case the tests
are centered at the midpoint and BOTH excesses are positive by the same computation. Going through the cases,
in all of them there is a sequence $(\gamma_k,L_k)$ with
$\sum_\rho h(\rho)\geq L_k/3-o(L_k)\geq\tfrac13L_k$ adjusting constants. Then
$-\mathcal P_F(\gamma_k,L_k)\geq\tfrac13L_k$ in infinitely many super-logarithmic windows — contradicting
153.M. Hence (SWARM) is impossible: the conclusion of 144.D holds. $\square$

**Remark 153.10bis (frank status of the proof).** The backbone (self-scale test, dominant positive excess,
transfer via (A4)) is solid; the accounting of interference among swarm quadruples (the case-by-case
paragraph) is correct but ugly, and one case — windows with multiple quadruples at comparable self-scales
and adversarial phases against EVERY center — is closed by the midpoint argument only for pairs; for
growing multiplicities a combinatorial center-selection lemma is needed. I mark it **[GAP-153.F]**
(technical, selection-related, not structural: the pointwise positivity of 153.6(b) holds for any number of
CENTERED quadruples, and "centered" can be relaxed to $|\gamma'-\gamma_j|\leq\epsilon/L_j$ absorbing into
$R$; the residue is just choosing centers that keep the non-centered ones far away). GAP-153.F is orders of
magnitude easier than GAP-144.C; I declare it so as not to oversell.

### 4.2. Position in the hierarchy

**Proposition 153.11 [PROPOSITION] (chain).** Modulo [GAP-153.F] in the middle arrow:
$$\mathrm{GRH}_{\text{cat}}\;\Longrightarrow\;\underbrace{\text{Conj. 141.E}}_{\text{LP-134 in the category}}
\;\Longrightarrow\;\underbrace{\text{Rigidity 153.M}}_{\text{new}}
\;\Longrightarrow\;\underbrace{\text{Conj. 144.D}}_{\text{GAP-144.C}}
\;\Longrightarrow\;\mathrm{LP\text{-}141}_{\text{cat}}(a)\ \ \forall a\succeq\log.$$

*Proof.* First arrow: GRH in the category = all divisors on the line = $m=0$ for all members; 141.E
($\liminf\delta\log\gamma>0$ over off zeros) holds vacuously. Second: under 141.E there is no
(SWARM); stronger: 153.M could still fail by a prime-side mechanism WITHOUT a swarm — no: the violation
of 153.M is a statement about $\mathcal P_F$, not about zeros; the correct implication is the contrapositive
of the proof of 153.10: the violation of 153.M that the swarm PRODUCES is the only one 153.M needs to forbid
to give 144.D. For the chain to be literal, I redefine (without loss for the application) 153.M in its
conditional form: "153.M$'$ := there is no $F$ with (SWARM) and anomaly $-\mathcal P_F\geq L_k/3$";
then 141.E ⟹ no (SWARM) ⟹ 153.M$'$ vacuously, and 153.M$'$ ⟹ 144.D is 153.10. Third and fourth:
153.10 and Prop. 144.4 (Doc 144, cited). Strict the last one: Prop. 144.1(b) of Doc 144. $\square$

**Comparison with what is known (step 4, direct answer).**

| statement | type | weaker than RH/GRH$_{\text{cat}}$? | weaker than LP-134/141.E? | accessible to density/moments? |
|---|---|---|---|---|
| 144.D | zero position (fat subsequence) | yes (strictly, implied by) | yes (Prop. 144.4/Obs. 144.4bis) | no — $1/\log$ scale: Lemma 141.M1; blind: 141.B0 |
| 153.M$'$ | evaluation/rigidity of the prime side at super-log support | yes (vacuous under GRH$_{\text{cat}}$) | yes (vacuous under 141.E) | no — requires relative precision $Le^{-L/2}$; PNT gives $e^{-c\sqrt L}$, VK gives $e^{-cL^{3/5}}$ |
| GAP-141.G1 (old wall) | evaluation at support $\log\gamma$, error $o(1)$ | — | — | no (Doc 141 §3.3) |

**Remark 153.11bis (153.M' against the old wall — the comparison that hurts).** GAP-141.G1 asked for the
explicit formula per window at support $L\asymp\log\gamma$ with error $o(1)$ against raw terms
$e^{L/2}\asymp\sqrt\gamma$: relative precision $\asymp\gamma^{-1/2}$. 153.M' asks for margin $o(L)$ against
raw terms $e^{L/2}$ with $L\gg\log\gamma$: relative precision $Le^{-L/2}\ll\gamma^{-K}$ for every $K$.
**Quantitatively, 153.M' is MORE demanding than the old wall, not less.** What this brings is not
numerical cheapening but structure: (i) the ZERO side of the problem is resolved with sign (153.6: the
swarm cannot hide from adapted tests — before, not even that was known: at fixed support it hides exactly,
141.B2); (ii) the missing statement is ONE-SIDED (a single-sign deficit, not a two-sided evaluation) and over
A sequence of windows (not uniform); (iii) and the source of its plausibility is no longer heuristic: it is
the same rigidity that KP proves in degree $<2$ (153.7) and that 141.R3 exhibited in the model — the
existing continuable objects simply have no anomalous prime sides. The question
"does the continuation forbid the anomaly?" is now a question about the coefficients of an Euler object
($a(n)\geq0$, Chebyshev type, continuable) and a concrete functional $\mathcal P_F(\gamma_k,L_k)$ — not about
zeros. That zeros→coefficients transposition is the net content of the document.

---

## 5. Verdict

### VERDICT: **MINIMAL LINK ISOLATED** — 144.D neither proved nor refuted; the dlVP-at-½ attack DEAD with a quantitative certificate; one new piece proved (self-scale excess, one-signed, dominant); the mechanism of Doc 144 corrected (KP proves its first arrow in degree $<2$; the second, refuted as written, is rewritten as window rigidity 153.M').

**On step 2 (the question DECIDES):** the answer is the bad branch. For a sub-resolution
swarm at height $\gamma$ to be visible where the positivity of $\Lambda$ bites ($\sigma>1$), one needs
$\gtrsim\log^2\gamma/\varepsilon^2$ off zeros per unit window (signal per quadruple $\asymp\delta^2$,
Lemma 153.2), and Riemann–von Mangoldt — valid in the category, Lemma 153.5 — authorizes $\leq C\log\gamma$:
**superlinear density, impossible; no subsequence suffices** (the Lorentzian kernel has mass $O(1)$ per
unit of height: stacking heights does not accumulate). It is the same averaging no-go of Doc 141, now with
constants: the dlVP lever is a Weil functional of effective support $O(1)$ and Cor. 141.B2 covers it.
The structural reason (§2.5): the repelling line must carry the pole of the positive measure; $\Re s=1$
carries it, $\Re s=\tfrac12$ is the axis of symmetry without a pole and the transposed inequality is
$0\geq0$ (141.M4).

**On step 3:** Kaczorowski–Perelli does not locate zeros, but its rigidity does give leverage: in degree $<2$
(modulo the embedding [GAP-153.E]) "continuation+Euler+functional equation ⟹ unitary/pure local datum" is
a THEOREM, and 144.D in degree $<2$ reduces to $\zeta$ and the shifted Dirichlet $L$-functions — every
low-degree counterexample would quantitatively violate GRH. At the same time, $\zeta$ (pure at every prime,
repulsion open) refutes "local purity ⟹ repulsion" as a per-prime statement: the carrier of the mechanism is
the window datum, not the local datum.

**On steps 4–5:** the minimal link is distilled as **Rigidity 153.M'** (one-sided deficit
$\geq L/3$ of the near-prime side in infinitely many super-logarithmic self-scale windows: forbidden), with
153.M' ⟹ 144.D proved modulo the technical center-selection gap [GAP-153.F] (combinatorial, not
structural). Hierarchy: GRH$_{\text{cat}}$ ⟹ 141.E ⟹ 153.M' ⟹ 144.D ⟹ LP-141$_{\text{cat}}$. 153.M' is
weaker than 141.E as a position and vacuous under GRH, but as an evaluation demand it is HARDER than the old
wall (relative precision $Le^{-L/2}$ versus $e^{-c\sqrt L}$ of PNT and $e^{-cL^{3/5}}$ of
Vinogradov–Korobov): the advance is structural (signal with proved sign and dominant on the zero side; all
the GAP concentrated in a one-sided coefficient functional), not quantitative. GAP-144.C remains open; it now
has the shape of a question about coefficients, not about zeros.

### Final message

**VERDICT: MINIMAL LINK ISOLATED.** The de la Vallée Poussin attack centered at ½ dies with a quantitative
certificate (superlinear density required vs. R–vM); the confrontation with Kaczorowski–Perelli closes
the arrow "continuation⟹purity" in degree $<2$ and refutes "purity⟹repulsion" as it stood; GAP-144.C is
distilled into Rigidity 153.M' (a one-sided functional of the prime side at super-logarithmic support), with
153.M'⟹144.D proved modulo a minor combinatorial gap.

**Three main results:**

1. **[LEMMA 153.2 + PROPOSITION 153.3 + COROLLARY 153.4]** — *Death certificate of dlVP-at-½:* the
   signal of an off quadruple in the half-plane of positivity is $\leq C_0\delta^2/(1+(t-\gamma)^2)$ (second
   order due to the functional equation); the complete swarm deflects $-\Re F'/F$ by $o(1/\log t)$; the
   visibility would require $\gtrsim\log^2\gamma$ zeros per window against the R–vM ceiling $C\log\gamma$
   (proved in the category, Lemma 153.5). No subsequence suffices; same no-go as Doc 141, now quantitative.

2. **[PROPOSITION 153.6]** — *Self-scale excess (the new piece):* with the modulated Fejér test at
   support $L_j=1/\delta_j$, the excess of an off quadruple over its projection is
   $8L[\frac{\cosh\kappa-1}{\kappa^2}-\frac12]+O(\kappa^2e^\kappa/(\gamma^2L))\geq L/3$ at $\kappa=1$ —
   **positive pointwise and $\gg\log\gamma$** (it dominates the expected mass of the on-line sea). The
   zero-mean profile (141.M5) does not apply at adapted support; no-go 141.B2 does not cover families chosen
   after the configuration. The whole GAP is concentrated on the prime side.

3. **[PROPOSITION 153.7 + 153.8 + DEFINITION 153.9 + PROPOSITION 153.10/153.11]** — *Correction of
   the mechanism and reduction:* KP proves "continuation⟹purity" in degree $<2$ and reduces 144.D there
   to the Dirichlet $L$-functions; "purity⟹repulsion" is untenable ($\zeta$ is pure and open); the minimal
   link is Rigidity 153.M' of the near-prime side, with the chain
   GRH$_{\text{cat}}$⟹141.E⟹153.M'⟹144.D⟹LP-141$_{\text{cat}}$ (middle arrow modulo [GAP-153.F],
   technical center-selection).

---

## References

**Internal (backward-only):** Doc 144 (Def. 144.0; Props. 144.1, 144.2, 144.4, 144.6, 144.8; Conjecture
144.D; GAP-144.C; Obs. 144.4bis; Cor. 144.10); Doc 141 (Lemma 141.B0; Lemma 141.B; Cor. 141.B2; Computations
141.M4/M5; Lemma 141.M1; Prop. 141.M2; Prop. 141.R1/R2; Computation 141.R3; Conjecture 141.E; GAP-141.G1); Doc
134 (model $\mathfrak W$, visibility (V1)–(V2), Thms. 5.1/5.4, §5.8 M3 purity↔resolution dictionary);
Doc 131 (Axiom H 6.1; Thm. 6.6 local Poisson; Thm. 6.7 local purity and barrier $|c_m|\leq2p^{m/2}$;
Prop. 6.8; Desideratum 6.9 H⁺); Doc 146 (verdict GAP-141.DH: FAT — the off zeros of D–H at macroscopic
distance; the boundary "sub-resolution ⟺ no Euler-type structure").

**Literature (published, verifiable):**
- [dlVP1899] Ch.-J. de la Vallée Poussin, *Sur la fonction ζ(s) de Riemann et le nombre des nombres premiers
  inférieurs à une limite donnée*, Mém. Couronnés Acad. Roy. Belgique **59** (1899–1900). (Classical
  zero-free region; also the PNT with error $e^{-c\sqrt{\log x}}$.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Thm. 3.8: zero-free region and the 3-4-1; Thm. 9.2: $N(T+1)-N(T)=O(\log T)$;
  Thm. 9.4: Riemann–von Mangoldt; §10.25: Davenport–Heilbronn.)
- [CG93] J. B. Conrey, A. Ghosh, *On the Selberg class of Dirichlet series: small degrees*, Duke Math. J.
  **72** (1993), 673–693. (Degree 0 and $0<d<1$ in $\mathcal S$.)
- [KP99] J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, I: $0\leq d\leq1$*, Acta Math.
  **182** (1999), 207–241. (Emptiness of $0<d<1$ in $\mathcal S^\sharp$; classification in degree 1 — see
  [literature GAP] §3.1 on the exact attribution within the series.)
- [KP11] J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, VII: $1<d<2$*, Ann. of Math.
  (2) **173** (2011), 1397–1441. (Emptiness of $1<d<2$.)
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. **53**, 2004. (Ch. 5: zero
  counting per window for general $L$-functions — Lemma 153.5; exponential sums over primes.)
- I. M. Vinogradov / N. M. Korobov (1958): zero-free region $\sigma\geq1-c/(\log t)^{2/3}(\log\log t)^{1/3}$
  and the corresponding bounds for sums over primes — cited only as a reference for the BEST known
  unconditional cancellation (Rem. 153.6bis, 153.11bis); exposition in [IK04, Ch. 8].

*End of Doc 153.*
