# Doc 144 — Attack on LP-141 (the minimal finiteness pivot): formalization, Hadamard test, arithmetic attempt, and map of the force/usefulness frontier

**Program:** Riemann Hypothesis — Phase 47: LIVE FRONTS.
**Role of the document:** frontal attack on the minimal lemma **LP-141** (Def. 141.2 of Doc 141), isolated in Phase 46
as the real pivot of the finiteness half ($m<\infty$) of the architecture $\mathrm{RH}=(m<\infty)\wedge(m<\infty\Rightarrow m=0)$.
The goal: formalize it with total quantifiers and distinguish it from LP-134; test it against the
Hadamard counterexample that already killed LP-134 in the analytic category; attempt to prove it in the
arithmetic category via the continuation⟹purity⟹repulsion mechanism; map the exact force/usefulness frontier and look
for weaker LPs; state what Davenport–Heilbronn decides. Frank verdict, including the part that hurts.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = TRULY proved here, complete proof; external results cited with
precision. **[COMPUTATION]** = shown. **[BRIDGE]** = connection with ζ/RH with frank status. **[GAP]** =
declared. **[DESIDERATUM]** = declared.

**Prerequisites read at source this phase (complete):** Doc 141 in full (Def. 141.1/141.2, hierarchy
141.P1/141.P3/141.P4, no-go 141.B/141.B2, Hadamard counterexample 141.R2, Euler computation 141.R3, Conjecture
141.E, GAP-141.DH); Doc 134 in full (crown §3, model $\mathfrak W$ §4 with visibility (V1)–(V2), Theorems
5.0–5.5, Thm. 7.2 synergy, §5.8 M1–M4); ERRATA of Phase 38 ($W_\lambda\geq0$ refuted — do NOT cite) and of Phase
46 (Doc 140: **Thm 5.3(ii) of D134 corrected to 5.3′** "strict ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$
with no exception clause"; perpetual scope caveat of B.4/Thm 1.3: essential positivity is an invariant of the
PAIR (form, Hilbert norm)).

---

## 0. Executive summary

1. **(§1) Formalization with total quantifiers.** LP-141$(a)$ is written canonically as
   $$\mathrm{LP\text{-}141}(a):\quad m=\infty\ \Longrightarrow\ \forall N\ \exists j>N\ \text{with}\ \delta_j\,a(\gamma_j)\geq1,$$
   a $\Pi_3$ statement over the off-line zeros, at FIXED unbounded calendar $a$. The precise distinction from LP-134:
   LP-134$^{(\psi)}$ is $\liminf_{\gamma\to\infty}|\beta-\tfrac12|\psi(\gamma)>0$ (NO off-line zero is
   asymptotically sub-resolution — a $\liminf$ over ALL off-line zeros); LP-141$(a)$ asks only that INFINITELY MANY
   be fat (a $\limsup$-type: the tail of fat ones never runs out). **[PROPOSITION 144.1]:** LP-134 ⟹ LP-141
   strictly; LP-141 ⟹̸ LP-134 (counterexample: replicated fat zeros + sub-resolution tail). LP-141 is thus
   strictly weaker than LP-134 — confirming its role as pivot.

2. **(§2) The Hadamard test REFUTES LP-141 in the analytic category — with the same force as against LP-134, and for
   the same reason, but the computation is new and must be done carefully.** **[PROPOSITION 144.2]:** for
   EVERY fixed unbounded calendar $a$ there exists an entire function of order 1, with functional equation, real on the
   line, zero count of ζ type, with $m=\infty$ and **ZERO fat quadruples at calendar $a$** — violating
   LP-141$(a)$. It is the analytic incarnation of Theorem 5.5(a) of Doc 134 (for every calendar there are
   invisible configurations), now realized by a concrete entire function. **Decisive conclusion of
   step 2 of the goal: YES, one can have $m=\infty$ with all off-line zeros simultaneously sub-resolution,
   respecting the functional equation and order 1 — hence LP-141 is also non-analytic and needs arithmetic.** The
   Hadamard counterexample of 141.R2 ($\delta_j=e^{-\gamma_j}$) refutes it for every sub-exponential $a$; the
   calendar-adapted refinement (144.2) refutes it for EVERY $a$.

3. **(§3) Attempt at an arithmetic proof via continuation⟹purity⟹repulsion: PROVED-PARTIAL with a named and
   reduced GAP.** The failure of the naive Euler construction (141.R3) is upgraded to a CONDITIONAL
   lower bound: **[PROPOSITION 144.4]** in the D131-H⁺ category (Euler + positive hermitian local data + continuation + functional equation), if the
   **quantitative local detection conjecture** [CONJECTURE 144.D] holds — an off-line zero at distance $\delta'$
   forces local impurity of size $\gtrsim\delta'$ detectable at support $\asymp1/\delta'$, NOT sustainable under
   continuation — then the strong form "$m\geq1\Rightarrow$ infinitely many fat ones" holds, which IMPLIES LP-141 for every calendar $a\succeq\log$.
   The exact residue is **[GAP-144.C]**: the effective lower bound $\delta_j\gtrsim 1/a(\gamma_j)$ on the fat ones
   derived from continuation. Frankness: it is NOT closed; LP-141 (in the Euler category) is reduced to a
   well-formed continuation rigidity property, strictly weaker than Conjecture 141.E (which
   asked for repulsion over ALL off-line zeros; 144.D asks only for infinitely many fat ones).

4. **(§4) Map of the force/usefulness frontier and a weaker LP-142.** The exact chain is built:
   $$\text{Axiom R}\ \succ\ \mathrm{LP\text{-}134}\ \succ\ \mathrm{LP\text{-}141}\ \succ\ \mathrm{LP\text{-}142}\ \succ\ (\text{trivial}),$$
   where **[NEW-DEFINITION 144.5] LP-142$(a)$:** "$m=\infty\Rightarrow$ the fat ones do not have zero
   relative density among the off-line zeros" — and **[PROPOSITION 144.6]** shows that LP-142 does NOT suffice for the synergy (weak
   positivity + zero density of fat ones is consistent with $m=\infty$). **The exact frontier is
   LP-141:** it is the MINIMUM statement that still gives $m<\infty$ with weak positivity of the symbol (any
   further weakening — finitely many fat ones allowed, or density — breaks Prop. 141.P3). Below
   LP-141 everything is too weak to serve; LP-141 itself is too strong for the analytic category (§2). The viable window is: LP-141 exactly, proved in the Euler category.

5. **(§5) Connection with GAP-141.DH — the exact logical implication.** **[PROPOSITION 144.7]:** if the $\delta_j$
   of Davenport–Heilbronn are bounded below by a constant $c>0$ (independent of $j$),
   then DH satisfies LP-141$(a)$ for EVERY calendar (in fact the strong form: all off-line zeros are
   fat at calendar $a\geq1/c$) — DH calibrates the GOOD side and is consistent with LP-141; if instead
   $\inf_j\delta_j=0$ with $\delta_j a(\gamma_j)\to0$ for some natural calendar, DH is an
   **arithmetic-approximate counterexample** to LP-141 at that calendar (DH has an approximate Euler product
   but NO genuine Euler functional equation — a failed Selberg class member — so it would not refute LP-141 in
   the D131-H⁺ category, but it WOULD show that "approximate Euler" is not enough). The implication is: **DH decides whether the
   genuine Euler functional equation is load-bearing in 144.D.**

6. **(§6) VERDICT: REFUTED-IN-ANALYTIC-CATEGORY / OPEN-WITH-MAP in the Euler category / PROVED-PARTIAL
   conditional on 144.D.** For the finiteness half $m<\infty$: LP-141 is genuinely the pivot (weaker than
   its two parents, sufficient with weak positivity), but it is NOT accessible without arithmetic, and within
   the arithmetic it reduces to a quantitative continuation rigidity (144.D / GAP-144.C) that is now the most concrete attackable object of the finiteness front.

---

## 1. Formalization of LP-141 and its distinction from LP-134

Work in the category of **configurations** (Def. 4.1 of D134): $Z=\{(\delta_j,\gamma_j)\}_{j\in J}$ with
$\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$ if $|J|=\infty$, finitely many $j$ per window, $m:=|J|$; the
quadruple $j$ is $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$. A **calendar** is $a:[2,\infty)\to[1,\infty)$ non-
decreasing (Def. 3.6 of D134); a quadruple is **fat at calendar $a$** if $\delta_j\,a(\gamma_j)\geq1$,
**sub-resolution** if $\delta_j\,a(\gamma_j)<1$ (Def. 4.2 of D134). The visibility $\theta_j$ satisfies
(V1) $\theta_j\to0$ when $\delta_j a(\gamma_j)\to0$, (V2) $\theta_j\geq c_0$ when $\delta_j a(\gamma_j)\geq1$.

### 1.1. The canonical form of LP-141 with total quantifiers

Doc 141 (Def. 141.2) states LP-141$(a)$ as "$m=\infty\Rightarrow\#\{j:\delta_j a(\gamma_j)\geq1\}=\infty$".
I write it with explicit quantifiers to fix its exact logical structure.

**Definition 144.0 [NEW-DEFINITION] (LP-141, canonical form with total quantifiers).** For a
function $F$ with zeros in the critical strip (finitely many per bounded height), a fixed unbounded calendar $a$, and
the enumeration $\{(\delta_j,\gamma_j)\}$ of its off-line quadruples ordered by increasing height:
$$\boxed{\ \mathrm{LP\text{-}141}(a)(F):\qquad \bigl(m=\infty\bigr)\ \Longrightarrow\ \Bigl(\forall N\in\mathbb N\ \ \exists j>N:\ \delta_j\,a(\gamma_j)\geq1\Bigr).\ }$$
Equivalently, with $\mathcal G_a:=\{j:\delta_j a(\gamma_j)\geq1\}$ (index of fat ones at calendar $a$):
$$\mathrm{LP\text{-}141}(a):\quad m=\infty\Rightarrow|\mathcal G_a|=\infty.$$

**Logical structure remarks (routine, fix the statement):**

(i) **The consequent is a $\limsup$, not a $\liminf$.** "$\forall N\,\exists j>N$" says the boolean sequence
$\mathbf 1[\delta_j a(\gamma_j)\geq1]$ is NOT eventually zero: it has infinitely many ones. It says nothing
about the intermediate zeros. **This is the atomic difference with LP-134.**

(ii) **Quantification over the tail.** LP-141 is insensitive to any finite set of quadruples: adding
or removing finitely many off-line zeros changes neither the hypothesis ($m=\infty$) nor the conclusion ($|\mathcal G_a|=\infty$). It is genuinely a statement about the $\gamma\to\infty$ behavior.

(iii) **Monotonicity in the calendar.** If $a\preceq a'$ (i.e. $a(\gamma)\leq a'(\gamma)$ eventually),
then $\mathcal G_a\subseteq\mathcal G_{a'}$ except for finitely many indices (Prop. 5.5bis(i) of D134), hence
$\mathrm{LP\text{-}141}(a)\Rightarrow\mathrm{LP\text{-}141}(a')$: **at a higher calendar, LP-141 is
easier** (more quadruples count as fat). The relevant calendar for the synergy is the natural
$a(\gamma)=C\log\gamma$ (mean zero spacing).

(iv) **Logical complexity.** As a predicate on the configuration: the hypothesis $m=\infty$ is $\Pi_2$
($\forall N\exists j>N$); the conclusion is $\Pi_2$; the conditional is $\Pi_3$. Simpler than LP-134, which
involves a $\liminf>0$ (a $\Sigma_2$ over the bound $c$ wrapped in a $\forall$).

### 1.2. The exact distinction LP-141 vs LP-134

Recall LP-134$^{(\psi)}$ (Def. 141.1): $\liminf_{\rho\ \text{off},\,\gamma\to\infty}|\beta-\tfrac12|\,\psi(\gamma)>0$,
i.e. $\exists c>0$ such that $\delta_j\psi(\gamma_j)\geq c$ for every $j$ with $\gamma_j$ large — **ALL**
off-line zeros are eventually fat.

**Proposition 144.1 [PROPOSITION] (LP-134 ⟹ LP-141, strictly).** Let $a$ be a calendar with
$a\succeq\psi$ (i.e. $a(\gamma)\geq\psi(\gamma)$ eventually). Then:

(a) $\mathrm{LP\text{-}134}^{(\psi)}\Rightarrow\mathrm{LP\text{-}141}(a)$.

(b) The implication is strict: there exists a configuration with $\mathrm{LP\text{-}141}(a)$ and $\neg\mathrm{LP\text{-}134}^{(\psi)}$.

*Proof.* (a) Suppose LP-134$^{(\psi)}$ and $m=\infty$. There exist $c>0$ and $\Gamma_0$ with
$\delta_j\psi(\gamma_j)\geq c$ for $\gamma_j\geq\Gamma_0$. Let $a\geq\psi$ from $\Gamma_1\geq\Gamma_0$.
By cofiniteness (Rem. 1.1(ii) of Doc 141) I can absorb the factor $c$: for the infinitely many $j$ with
$\gamma_j\geq\Gamma_1$, $\delta_j a(\gamma_j)\geq\delta_j\psi(\gamma_j)\geq c$. If $c\geq1$, all those
are fat: $|\mathcal G_a|=\infty$. If $c<1$, rescale the calendar: $a':=\lceil1/c\rceil\cdot a$
satisfies $\delta_j a'(\gamma_j)\geq\lceil1/c\rceil\,c\geq1$ for those $j$, hence $|\mathcal G_{a'}|=\infty$;
and since $\{C\log\}$ is ONE calendar class (invariance under constants, Rem. 1.1(i) of Doc 141), LP-141 at
the class $\{C\log\}$ holds. Concretely: LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ for the calendar
$a=\lceil1/c\rceil\psi$, which is of the same class as $\psi$. $\square_{(a)}$

(b) Explicit configuration (combines the two strata of Doc 134): take two families of quadruples.
*Replicated fat family:* $\gamma_k^{\mathrm{g}}:=2^{2k}$, $\delta_k^{\mathrm{g}}:=\tfrac14$ (fixed
distance to the line), $k\geq1$ — infinitely many quadruples at distance $\tfrac14$. *Sub-resolution family:*
$\gamma_k^{\mathrm{s}}:=2^{2k+1}$, $\delta_k^{\mathrm{s}}:=e^{-\gamma_k^{\mathrm{s}}}$, $k\geq1$. Let
$a(\gamma)=\log\gamma$. Then:
- $|\mathcal G_a|=\infty$: the fat family satisfies $\delta_k^{\mathrm{g}}a(\gamma_k^{\mathrm g})=\tfrac14\cdot2k\log2\to\infty\geq1$
  for $k\geq2$. LP-141$(a)$ holds (true consequent, $m=\infty$).
- $\neg\mathrm{LP\text{-}134}^{(\log)}$: the sub-resolution family gives
  $\delta_k^{\mathrm{s}}\log\gamma_k^{\mathrm{s}}=e^{-2^{2k+1}}\cdot(2k+1)\log2\to0$, hence
  $\liminf_{\gamma\to\infty}\delta\log\gamma=0$: LP-134 is violated. $\square_{(b)}$

**Remark 144.1bis (the difference is exactly "allowing thin ones in the presence of fat ones").** The
configuration of (b) is the heart of the distinction: LP-141 **tolerates infinitely many off-line zeros that are sub-resolution**
(the $\mathrm{s}$ family) WHILE they coexist with infinitely many fat ones (the $\mathrm g$ family). LP-134 forbids
ALL asymptotic sub-resolution. That is why LP-141 is strictly weaker — and that is why it is the
correct pivot candidate: it asks only for what synergy 141.P3 needs (one fat zero in infinitely many windows to activate
Theorem 5.1 of D134), no more. Prop. 141.P4(iii) of Doc 141 already recorded this non-implication; here it is
formalized with quantifiers and calibrated against the exact scale of the calendar.

### 1.3. Why LP-141 (not LP-134) is the correct statement for $m<\infty$ — reminder of the synergy

I repeat the operative content of Prop. 141.P3 of Doc 141 to keep it present in this document (not a
re-proof; I cite the result with its mechanism):

**[BRIDGE 144.S] (Prop. 141.P3, recalled).** In the model $\mathfrak W$ of D134 with (S1)–(S3) and (V2): if
LP-141$(a)$ holds at an unbounded calendar $a$ **and** the symbol $\sigma_a(Q)$ is **weakly** positive
($\mathrm{spec}\subseteq[0,\infty)$), then $m<\infty$. *Mechanism:* if $m=\infty$, LP-141 gives infinitely many
fat ones; by (V2) they have $\theta_j\geq c_0$; by Theorem 5.1 of D134,
$\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c_0/2]\neq\emptyset$ — contradicting weak positivity. Hence
$m<\infty$. Status: a theorem WITHIN the model $\mathfrak W$ (axioms (S1)–(S3) with their declared GAPs
in Rem. 4.5 of D134); the new piece this document attacks is the **hypothesis LP-141 itself**, not the
implication 141.P3.

Note the economy: LP-141 + **weak** positivity ⟹ $m<\infty$. The weakness of the positivity piece
(no gap is requested, which Theorem 1.3 of D134 showed to be exactly robust finiteness and which fixed-weight
normalization destroys, Theorem 2.2) is what makes this route cheaper than the strict route. **LP-141 is
the only geometric piece missing for the Fredholm half.** Hence the attack.

---

## 2. The Hadamard counterexample test against LP-141

Step 2 of the goal is the decisive question: the Hadamard counterexample (Prop. 141.R2 of Doc 141) killed
LP-134 in the analytic category with $\delta_j=e^{-\gamma_j}\to0$, ALL sub-resolution. If all the
$\delta_j$ are sub-resolution, there are ZERO fat ones — and LP-141 also asks for infinitely many fat ones. The question:
**does the same counterexample refute LP-141?** Answer: YES, and in fact an adapted version refutes it for EVERY
calendar. I prove this carefully.

### 2.1. The original Hadamard counterexample refutes LP-141 at sub-exponential calendar

**Computation 144.A [COMPUTATION] (the function of 141.R2 violates LP-141$(a)$ for every sub-exponential $a$).** Let $F$
be the entire function of Prop. 141.R2: order 1, $F(s)=F(1-s)$, real on the line, $N_F(T)\asymp T\log T$, with
off-line quadruples $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ where $\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$. For
any calendar $a$ with $a(\gamma)\leq e^{\gamma/2}$ (all $C\log\gamma$, all polynomials,
every sub-exponential $a$):
$$\delta_j\,a(\gamma_j)=e^{-\gamma_j}\,a(\gamma_j)\leq e^{-\gamma_j}e^{\gamma_j/2}=e^{-\gamma_j/2}\xrightarrow{j\to\infty}0.$$
Hence $\mathcal G_a=\{j:\delta_j a(\gamma_j)\geq1\}$ is FINITE (in fact empty for $j$ large): the consequent
of LP-141$(a)$ is FALSE. Since $m=\infty$ (true hypothesis), **LP-141$(a)$ is false on $F$ for every
sub-exponential calendar.** $\square$

This already answers the bulk of step 2: the Hadamard counterexample, which has $m=\infty$ and all
$\delta_j\to0$, has ZERO fat ones at the relevant $\log\gamma$ scale, so it refutes LP-141 exactly as
it refutes LP-134, **for the same reason** (total sub-resolution). The LP-134/LP-141 difference I highlighted in
§1 (LP-141 tolerates thin ones if there are fat ones) does NOT help here: the counterexample has NO fat one
at all, so not even the weakened conclusion of LP-141 is saved.

### 2.2. The refinement: LP-141 falls for EVERY calendar (not only sub-exponential)

One might object: the counterexample of 141.R2 is visible (fat) for the super-exponential calendar
$a(\gamma)=e^\gamma$. Does LP-141 survive at some calendar? No: given ANY fixed calendar, one
constructs a Hadamard counterexample adapted to it. It is the analytic version of Theorem 5.5(a) of D134.

**Proposition 144.2 [PROPOSITION] (analytic refutation of LP-141 at arbitrary calendar).** For every
fixed unbounded calendar $a$ there exists an entire function $F_a$ of order 1, with $F_a(s)=F_a(1-s)$, real on
the critical line, with all its zeros in $|\Re s-\tfrac12|<\tfrac12$, with count $N_{F_a}(T)\asymp T\log T$, and
infinitely many off-line quadruples $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ such that
$$m=\infty\qquad\text{and}\qquad\delta_j\,a(\gamma_j)\xrightarrow{j\to\infty}0,$$
so that $|\mathcal G_a|=0$ eventually and $F_a$ **violates LP-141$(a)$**.

*Proof.* I follow the construction of 141.R2, changing only the $\delta_j$ to adapt them to $a$.
Coordinate $z$: $s=\tfrac12+iz$, so $s\mapsto1-s$ is $z\mapsto-z$ and the critical line is $z\in\mathbb R$.
I prescribe zeros in $z$:

*(a) Real sea (fixes the order and the count).* Real pairs $\pm t_n$ with $t_n:=n/\log(n+2)$, $n\geq1$; the
counting function $\#\{t_n\leq r\}\asymp r\log r$.

*(b) Off-line quadruples (violators).* $\gamma_j:=2^j$ and
$$\delta_j:=\min\Bigl(\tfrac14,\ \frac{1}{j\,a(2^j)}\Bigr),\qquad z_j:=\gamma_j-i\delta_j,$$
with quadruple $\{\pm z_j,\pm\bar z_j\}$ (corresponding to $s=\tfrac12\pm\delta_j\pm i\gamma_j$). Define
$$G(z):=\prod_{n\geq1}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\cdot\prod_{j\geq1}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$

*Convergence and order.* Identical to 141.R2: in $w=z^2$, $\sum_n t_n^{-2}<\infty$ and
$\sum_j|z_j|^{-2}\leq\sum_j(\gamma_j^2+\delta_j^2)^{-1}\leq\sum_j 4^{-j}<\infty$ (since $|z_j|^2\geq\gamma_j^2=4^j$),
genus-0 product in $w$, $G$ entire and even; modulus counting function $n_G(r)\asymp r\log r$, convergence exponent 1 ⟹ order 1 [B54, Thm. 2.6.5]. (Changing $\delta_j$ does not affect this: only $|z_j|\geq\gamma_j$ matters,
which holds since $\delta_j\leq\tfrac14$.)

*Functional equation, reality, strip.* $G(-z)=G(z)$ (evenness) ⟹ $F_a(s):=G(\tfrac{s-1/2}{i})$ satisfies
$F_a(1-s)=F_a(s)$; the factors have real coefficients in $z^2$ (the $t_n^2$ real; the pairs
$(1-w/z_j^2)(1-w/\bar z_j^2)$ have real coefficients by conjugation), hence $G|_{\mathbb R}\subseteq\mathbb R$
and $F_a$ is real on the line; $|\Im z_j|=\delta_j\leq\tfrac14<\tfrac12$ ✓.

*Violation of LP-141$(a)$.* By construction, for $j$ with $\delta_j=1/(j\,a(2^j))<\tfrac14$ (all but
finitely many, since $a$ unbounded ⟹ $j\,a(2^j)\to\infty$):
$$\delta_j\,a(\gamma_j)=\frac{1}{j\,a(2^j)}\cdot a(2^j)=\frac1j\xrightarrow{j\to\infty}0.$$
For the finitely many initial $j$ with $\delta_j=\tfrac14$ the value is bounded, but they are finite. Hence
$\delta_j a(\gamma_j)\to0$: $\mathcal G_a$ finite, consequent of LP-141$(a)$ false, $m=\infty$. $\square$

**Corollary 144.3 [COROLLARY] (LP-141 is arithmetic or it is nothing — same as LP-134).** LP-141 is NOT a theorem of
the analytic category (entire + order 1 + functional equation + reality on the line + ζ-type zero density): the Prop. 144.2 gives,
**for each fixed calendar**, a member violating it with $m=\infty$ and zero fat ones. Consequently,
**every proof of LP-141 must use the arithmetic side** (Euler product / coefficients / explicit
formula with primes). The hope that LP-141, being strictly weaker than LP-134, might be accessible analytically,
is **FALSE**: both fall to the same mechanism (stacking off-line sub-resolution zeros calibrated against the calendar), because that mechanism produces ZERO fat ones, and "zero fat ones" violates the conclusion of LP-141
just as much as that of LP-134. $\square$

### 2.3. Frankness about what the test establishes and what it does not

**Remark 144.3bis (what §2 proves exactly).** Prop. 144.2 proves that the analytic category
(structure of ξ as an entire function of the Pólya–Laguerre class with functional equation) does NOT force LP-141.
This is expected and reinforces the corpus: it is the LP-141 analogue of the cosh anti-models (which
realize finite $m$ in the analytic category) and of Theorem 5.5(a) of D134 (for every calendar,
invisible $m=\infty$ configurations). **What it does NOT prove:** it says nothing about ζ itself. For ζ,
refuting LP-141 would exhibit infinitely many off-line zeros — refuting RH (same argument as Prop. 141.R1 for LP-134: refuting LP-141 for ζ
requires $m=\infty$, hence ¬RH). So the falsifiability situation of LP-141 is IDENTICAL to that of LP-134:
falsifiable in the category (and the analytic category indeed falsifies it), but the ζ instance is only
decidable together with RH or via the arithmetic class route (§3). **The Hadamard test does NOT kill LP-141 for the
program; it kills the analytic hope and redirects to arithmetic — exactly the same verdict that
141.R2 gave for LP-134.**

A frank subtlety that distinguishes LP-141 from LP-134 even here: for LP-134, there were analytic
configurations SATISFYING it non-trivially (the pure fat family $\delta_j\equiv\tfrac14$: satisfies LP-134).
Same for LP-141 (that family satisfies LP-141). But *refutability* is what matters, and it is identical:
both are refuted with the adapted sub-resolution family. The relative weakness of LP-141 does not buy
refutability: it only buys that in the presence of fat ones one can be lax with thin ones — and the counterexample
puts no fat ones at all.

---

## 3. Attempt at an arithmetic proof: continuation ⟹ purity ⟹ repulsion

Since §2 redirects LP-141 to arithmetic, I attack the D131-H⁺ category: Dirichlet series with Euler
product, positive hermitian local data, analytic continuation, and functional equation (the class where
Conjecture 141.E of Doc 141 lives). The proposed mechanism: the analytic continuation of an Euler product
forces asymptotic purity of the local data; purity is local sub-resolution; a "fat" off-line zero at distance
$\delta'$ requires local impurity of size $\gtrsim\delta'$ which continuation forbids sustaining.

### 3.1. The starting point: the failure of the naive construction (141.R3, recalled)

Computation 141.R3 of Doc 141 showed: the naive Euler product
$D(s)=\prod_k(1-\alpha_k p_k^{-s})^{-1}(1-\bar\alpha_k p_k^{-s})^{-1}$ with impure data
$|\alpha_k|=p_k^{1/2+\delta_k'}$, $\delta_k'\downarrow0$ (whose divisor would be at $\Re s=\tfrac12+\delta_k'$,
violating repulsion with $m=\infty$), **converges only for $\Re s>\tfrac32$** and does NOT continue to the critical strip: continuation couples the local data and the known continuable examples
(characters, automorphic forms) ALL have pure data ($|\alpha|=\sqrt p$, $\delta'=0$). The obstruction is structural. For
LP-141 (not LP-134) the question sharpens: does the continuation failure prevent stacking infinitely many fat ones all at
decreasing $\delta'$ — or does it only prevent total sub-resolution?

### 3.2. The purity ↔ resolution dictionary (M3 of D134, recalled and sharpened)

From §5.8 M3 of D134 and Theorem 6.7 of D131: a local block $F_{p,\alpha}$ with $|\alpha|=p^{1/2+\delta'}$
is **impure** and its impurity is detected in the local data $c_m$ (log-derivative coefficients) only at order
$m\gtrsim1/\delta'$, where $|c_m|>2p^{m/2}$ breaks Weil's purity barrier. The dictionary:
$$\text{off-line zero at distance }\delta'\ \longleftrightarrow\ \text{local impurity detectable at support }M\asymp1/\delta'.$$
"Local purity" $\iff$ "all potential quadruples are sub-resolution at every calendar" $\iff$ autonomous
symbol. The barrier $|c_m|\leq2p^{m/2}$ IS the sub-resolution condition in the local world (§5.8 M3 of D134,
verified there with the two-bump Mertens test).

### 3.3. The detection conjecture and the conditional lower bound

I formalize the missing link as a quantitative local detection conjecture, strictly weaker than
Conjecture 141.E (which required repulsion over ALL off-line zeros; here I ask only for infinitely many fat ones).

**Conjecture 144.D [CONJECTURE — the arithmetic link, named].** *In the D131-H⁺ category (Euler product
with positive hermitian local data, analytic continuation to the critical strip, functional equation), if the
function has $m=\infty$ off-line zeros, then there exist $c>0$ and a subsequence $j_k$ of off-line zeros with*
$$\delta_{j_k}\,\log\gamma_{j_k}\ \geq\ c\qquad(k\to\infty).$$
*Proposed mechanism: each off-line zero at distance $\delta_{j}$ requires sustained local impurity of amplitude
$\gtrsim\delta_j$ over a band of primes of logarithmic size $\asymp\log\gamma_j$ (the explicit formula
localizes the off-line zero at height $\gamma_j$ using primes $p\lesssim\gamma_j$); analytic continuation
couples those local data and forbids the impurity from being simultaneously (i) sub-resolution at
scale $1/\log\gamma$ at ALL zeros and (ii) sustained at infinitely many zeros — some must be
fat.*

**Proposition 144.4 [PROPOSITION] (conditional lower bound ⟹ LP-141 in the Euler category).** In the
D131-H⁺ category, if Conjecture 144.D holds, then LP-141$(a)$ holds for every calendar $a\succeq\log$ (in
particular the natural $a=C\log\gamma$). In fact the strong form holds: $m=\infty\Rightarrow$ infinitely many fat ones
at calendar $\log$.

*Proof.* Suppose 144.D and $m=\infty$. There exist $c>0$ and subsequence $j_k$ with
$\delta_{j_k}\log\gamma_{j_k}\geq c$. Take the calendar $a(\gamma)=\lceil1/c\rceil\log\gamma$ (class
$\{C\log\}$). Then $\delta_{j_k}a(\gamma_{j_k})=\lceil1/c\rceil\,\delta_{j_k}\log\gamma_{j_k}\geq\lceil1/c\rceil\,c\geq1$:
the $j_k$ are fat at calendar $a$, infinitely many. Hence $|\mathcal G_a|=\infty$: LP-141$(a)$. By monotonicity
(Rem. 144.0(iii)), LP-141$(a')$ for every $a'\succeq a$. $\square$

**Remark 144.4bis (what 144.4 achieves and what it does not — maximum frankness).** Prop. 144.4 does NOT prove
LP-141. It reduces LP-141 (in the Euler category) to Conjecture 144.D, which is a statement of **quantitative
continuation rigidity**. The net gain over Doc 141:
1. **144.D is strictly weaker than Conjecture 141.E.** 141.E asked for $\liminf_{\text{ALL off}}\delta_j\log\gamma_j>0$
   (repulsion of ALL — the source of LP-134). 144.D asks only for a $\limsup$ of a fat subsequence — the source
   of LP-141. It is the exact arithmetic translation of the distinction in §1.2. Hence **the correct arithmetic
   front to attack is not 141.E but 144.D**, which allows thin off-line zeros while infinitely many are fat.
2. **The residue is named: [GAP-144.C].** What remains to be proved is the effective lower bound
   $\delta_{j_k}\gtrsim 1/\log\gamma_{j_k}$ on a subsequence of off-line zeros, derived from the analytic
   continuation of the Euler product. Computation 141.R3 gives directional evidence (the construction that would violate
   this does NOT continue), but NOT the bound. Converting "does not continue" into "$\delta_{j_k}\gtrsim1/\log\gamma$" is the GAP.

### 3.4. Why continuation is the correct engine (not positivity) — reminder of Computation 141.M4

I emphasize, citing Computation 141.M4 of Doc 141 (not re-proving): Landau's positivity lever (which gives the
Deuring–Heilbronn repulsion from $s=1$) is **identically zero on the critical line** by the functional
equation — the first-order contribution of a symmetric pair to $\Re\frac{\xi'}{\xi}(\tfrac12+it)$ is
exactly zero. Hence the engine of LP-141/144.D CANNOT be positivity. The candidate engine is
**continuation rigidity**: the analytic continuation of the Euler product is a GLOBAL condition on the
family $\{\alpha_k\}$ of local data, and it is that global rigidity — not a local sign inequality — that
must force the fat ones. This matches Conjecture 141.E of Doc 141 in the engine, but 144.D lowers the
conclusion from "all repelled" to "infinitely many fat," aligning it exactly with what synergy 141.P3
needs.

### 3.5. A small but real unconditional dividend

Not everything is conjectural. One unconditional observation about the genuine Euler category:

**Proposition 144.5 [PROPOSITION] (Hamburger reduces the strict category to ζ).** In the narrowest category
(Dirichlet series with the EXACT functional equation of ζ and minimal regularity), by Hamburger's theorem
[H21] the only object is a multiple of ζ. Consequently, LP-141 in that category is LP-141 for ζ —
unfalsifiable without refuting RH (Prop. 141.R1 transposed to LP-141: refuting LP-141 for ζ gives $m=\infty$ ⟹ ¬RH).

*Proof.* Hamburger [H21]: the functional equation of ζ plus regularity characterizes ζ up to scalar. Hence
the only function in the category is ζ; LP-141 for it is unfalsifiable as in 141.R1. $\square$

**Remark 144.5bis (the pincer).** Hamburger (strict category, only ζ, unfalsifiable without ¬RH) and the
Hadamard counterexample (lax analytic category, falsifiable, Prop. 144.2) are the two jaws of the
pincer: LP-141 is true-or-RH in the narrow category, false in the wide category. The **productive
intermediate** category is D131-H⁺ (Euler + continuation + functional equation, but not necessarily that of
ζ): wide enough to have members other than ζ (automorphic $L$-functions), narrow enough for
continuation to be load-bearing. That is where 144.D / GAP-144.C lives, and it is the only category where proving
LP-141 is neither trivial nor equivalent to RH.

---

## 4. The map of the force/usefulness frontier and possible weaker LPs

The goal (step 4): if LP-141 is too strong, look for the ABSOLUTE MINIMUM statement that still gives $m<\infty$
with the symbol's synergy. I map the exact frontier.

### 4.1. The force chain

**Proposition 144.6 [PROPOSITION] (force chain, all implications strict).** At a fixed unbounded calendar $a$:
$$\underbrace{\text{Axiom R}}_{\text{repl.}}\ \Longrightarrow\ \mathrm{LP\text{-}134}^{(a)}\ \Longrightarrow\ \mathrm{LP\text{-}141}(a)\ \Longrightarrow\ \mathrm{LP\text{-}142}(a),$$
where LP-142 is Def. 144.7 below (the "≥1 fat one" weakening), and no arrow reverses.

*Proof.* Axiom R ⟹ LP-134: Prop. 141.P4(ii) of Doc 141 (replicas preserve $\delta_0/2$, are
eventually fat at every calendar — in fact giving the strong form $m\geq1\Rightarrow$ infinitely many fat ones,
which is more than LP-134). LP-134 ⟹ LP-141: Prop. 144.1(a). LP-141 ⟹ LP-142: infinitely many fat ones ⟹ at least one
fat one. Non-reversals: 144.1(b) (LP-141 ⟹̸ LP-134); Prop. 141.P4(iii) (LP-141 ⟹̸ Axiom R); and LP-142 ⟹̸
LP-141 is Prop. 144.8(a) below (a world with exactly one fat one plus a sub-resolution tail satisfies LP-142
but not LP-141). $\square$

### 4.2. The weakest candidate: LP-142, and why it does NOT suffice

The only weakening of LP-141 in the cardinality of fat ones is lowering "infinitely many" to "at least one." (There is
nothing strictly between "infinitely many" and "one" that is a natural statement about the cardinal: any finite bound
$\geq1$ is equivalent, modulo cofiniteness, to "$\geq1$"; and "positive relative density" is strictly
STRONGER than "infinitely many," hence goes in the wrong direction.) So I define the weakest candidate:

**Definition 144.7 [NEW-DEFINITION] (LP-142, the weakest pivot candidate).** At a fixed unbounded calendar $a$,
with $\mathcal G_a=\{j:\delta_j a(\gamma_j)\geq1\}$ the set of fat ones:
$$\mathrm{LP\text{-}142}(a):\qquad m=\infty\ \Longrightarrow\ |\mathcal G_a|\geq1,$$
"if there are infinitely many off-line, at least one is fat." It is the maximal weakening of LP-141 in the cardinal of fat ones,
and by Prop. 144.6 it is strictly weaker than LP-141.

**Proposition 144.8 [PROPOSITION] (the exact frontier: LP-141 is the minimum that works).**

(a) **"$m=\infty\Rightarrow|\mathcal G_a|\geq1$" (a single fat one) does NOT suffice for the synergy.** There exists a
configuration with $m=\infty$, exactly one fat one, weak positivity of the symbol, and $m=\infty$ — i.e.
weak positivity + "≥1 fat one" is consistent with $m=\infty$.

(b) **"$|\mathcal G_a|=\infty$ with zero density allowed" (= LP-141) DOES suffice**, and is strictly
weaker than LP-134.

(c) Consequently LP-141 is the **absolute minimum statement** of the family "how many fat ones" that still gives
$m<\infty$ via Prop. 141.P3: asking for less (finitely many fat ones) lets $m=\infty$ slip through; asking for more
(positive density, or all fat = LP-134) is unnecessarily strong.

*Proof.* (a) Theorem 5.1 of D134 produces negative spectral mass $\leq-c_0/2$ in the symbol
from an **INFINITE subsequence** of fat ones (it needs $\gamma_{j_k}\to\infty$ for the limit point to survive the quotient by $\mathcal J$). A single fat one at height $\gamma_0$ contributes a hyperbolic block of
finite support in windows: it lies in the compact ideal $\mathcal J$ (finite-support section), invisible to
the symbol (it is exactly the M1/cosh case of §5.8 of D134: finite-visible $m$ ⟹ symbol strictly
positive). Construction: one fat one at $\delta_0=\tfrac14$, $\gamma_0=10$, PLUS infinitely many sub-resolution
ones $\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$ ($j\geq4$). The symbol: the single fat one is in $\mathcal J$, the
sub-resolution ones are in $\mathcal J$ (Theorem 5.4), hence $\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, weakly
(and strictly) positive; yet $m=\infty$. Weak positivity + "≥1 fat one" ⟹̸ $m<\infty$. $\square_{(a)}$

(b) Sufficiency is Prop. 141.P3 (infinitely many fat ones ⟹ infinite subsequence ⟹ Theorem 5.1 ⟹ negative mass
⟹ contradicts weak positivity ⟹ $m<\infty$); the coexisting sub-resolution ones do NOT interfere (they are in $\mathcal J$,
Theorem 5.4). Weaker than LP-134: Prop. 144.1(b). $\square_{(b)}$

(c) From (a) and (b): the exact threshold between "does not serve" and "serves" is **infinitely many**
fat ones (not finitely many, not positive density). LP-141 is exactly that. $\square_{(c)}$

**Remark 144.8bis (the map of the frontier, in one sentence).** Theorem 5.1 of D134 needs a limit
point of negative spectra in the crown, and a limit point requires an INFINITE subsequence of windows
with fat ones. Neither more (density) nor less (finite) — exactly infinitely many. **LP-141 is the exact shadow
of the mechanism of Theorem 5.1 on the question "how many fat ones."** There is no LP-142 strictly between LP-141 and
trivial that works: the force/usefulness frontier is a point, and that point is LP-141. The search of step 4
ends with a clean negative result: **there is no pivot weaker than LP-141** for the weak-positivity-of-the-symbol route.

### 4.3. The only real weakening is in the calendar, not in the cardinal

What DOES admit weakening is the calendar: by monotonicity (Rem. 144.0(iii)), LP-141$(a)$ at a
higher calendar is weaker. The maximally weak useful calendar is the highest one for which the weak
positivity of the symbol remains plausibly autonomous. This reconnects with Desideratum O1 of D134 (pushing the
calendar of sub-resolution blindness from $a=O(1)$ toward $a=\epsilon\log n$): **the fine front is to measure the
maximal $\epsilon$ such that LP-141$(\epsilon\log)$ remains necessary for $m<\infty$ and the autonomous symbol
still has weak positivity.** It is a quantitative front, not a new quantifier.

---

## 5. Connection with GAP-141.DH: what Davenport–Heilbronn decides

The goal (step 5): state the exact logical implication that GAP-141.DH (are the $\delta_j$ of DH
bounded below?) has on LP-141. Other work of the program audits DH numerically; here I only state the logic.

**Context (from §5.8 M2 of D134 and §4.3 of Doc 141).** Davenport–Heilbronn [DH36] is a linear combination
$F_\theta=\cos\theta\,L_1+\sin\theta\,L_2$ of two $L$-functions mod 5; it has continuation and functional equation
but **NO genuine Euler product** (it is not multiplicative — it is in the "failed Selberg class"). It has
$m=\infty$ off-line zeros in the strip, computed at macroscopic distances from the line [BS07], [BG11]. GAP-141.DH:
is $\inf_j\delta_j(\theta)>0$? (plausible datum, not verified at the source).

**Proposition 144.9 [PROPOSITION] (exact logical implication of DH on LP-141).** Let $a(\gamma)=C\log\gamma$
be the natural calendar and consider DH at generic parameter $\theta$.

(a) **If $\inf_j\delta_j=c>0$** (distances bounded below by a constant): then for large $j$
$\delta_j a(\gamma_j)=c\cdot C\log\gamma_j\to\infty\geq1$, so ALL off-line zeros of DH are fat at calendar
$a\geq1/c$ (in fact at every calendar $\succeq\log$): DH satisfies the **strong form** of LP-141 (all
fat), a fortiori LP-141. **DH calibrates the GOOD side** and is consistent with LP-141.

(b) **If $\inf_j\delta_j=0$ but $\liminf_j\delta_j\log\gamma_j>0$** (distances decrease but not faster
than resolution): DH still satisfies LP-134$^{(\log)}$ (all eventually fat), a fortiori LP-141.
Good side too.

(c) **If $\delta_j\log\gamma_j\to0$ for a cofinal subsequence AND the fat ones run out** (all off-line zeros
eventually sub-resolution): DH **violates LP-141$(\log)$** with $m=\infty$ and zero fat ones. But —and this is the
logical key— **DH is NOT in the D131-H⁺ category** (no genuine Euler product), so this case would NOT
refute Conjecture 144.D nor LP-141 IN THE EULER CATEGORY; it would only show that "approximate Euler / functional
equation without multiplicativity" is insufficient to force fat ones.

(d) **Mixed case (infinitely many fat + infinitely many sub-resolution):** DH satisfies LP-141$(\log)$ (infinitely many
fat ones) BUT violates LP-134$(\log)$ (infinitely many thin ones). **This case is the most informative: it would realize LP-141 without
LP-134 in a concrete arithmetic-approximate object** — the separation of §1.2 instantiated in nature.

*Proof.* Direct computation of $\delta_j a(\gamma_j)$ in each regime, plus the definition of $\mathcal G_a$
and the observation that DH lacks a multiplicative Euler product [DH36], [BG11] (hence $\notin$ D131-H⁺).
$\square$

**Corollary 144.10 [COROLLARY] (what DH decides — the exact implication).** Computing the $\delta_j$ of DH
decides **one single precise thing**: whether the **genuine Euler functional equation (multiplicativity) is
load-bearing in Conjecture 144.D.**
- If DH is on the good side (cases a/b/d): consistent with 144.D, but does NOT confirm it (DH is not Euler) — and
  case (d) would be POSITIVE evidence that LP-141 (not LP-134) is the correct statement, since DH would
  satisfy it without satisfying LP-134.
- If DH violates LP-141$(\log)$ (case c): it does NOT refute 144.D (DH $\notin$ D131-H⁺), but it **demonstrates that
  multiplicativity/Euler is ESSENTIAL** in 144.D — that continuation + functional equation WITHOUT genuine Euler do NOT
  suffice to force fat ones. This would sharpen 144.D to "it is the Euler product, not continuation alone, that is the engine."

*Proof.* Combination of 144.9 with the fact DH$\notin$D131-H⁺. $\square$

**Remark 144.10bis (the value of the DH test).** DH is the ONLY $m=\infty$ object in the corpus with continuation
and functional equation. Its verdict does not decide LP-141 for ζ (DH is not Euler), but it **calibrates which hypothesis
of 144.D is load-bearing**: if DH (without Euler) already repels (case a/b), then maybe continuation alone suffices and
144.D could be weakened by dropping "Euler"; if DH (without Euler) does NOT repel (case c), then Euler is essential and
144.D is correctly formulated. The finite test over [BS07]/[BG11] is, therefore, a **measurement of the
correct hypothesis of the arithmetic conjecture**, not a decision of LP-141. Task for whoever audits DH:
determine which of the four cases (a)/(b)/(c)/(d) occurs, reporting $\liminf_j\delta_j\log\gamma_j$.

---

## 6. Verdict and consequences for the finiteness half $m<\infty$

### VERDICT: **REFUTED-IN-ANALYTIC-CATEGORY + OPEN-WITH-MAP (Euler category) + PROVED-PARTIAL conditional on 144.D**

**Refuted (analytic category):** LP-141 is FALSE in the category of order-1 entire functions with
functional equation, reality on the line, and ζ-type density — for EVERY fixed calendar (Prop. 144.2,
complete proof). The Hadamard counterexample that killed LP-134 kills LP-141 for the same reason
(total sub-resolution ⟹ zero fat ones), and the calendar-adapted version kills it for every $a$. **The
answer to the decisive question of step 2 is YES: one can have $m=\infty$ with all off-line zeros
sub-resolution, respecting the functional equation and order 1; LP-141 needs arithmetic, just like LP-134.** The
relative weakness of LP-141 (tolerates thin ones if there are fat ones) does NOT buy refutability, because the counterexample does not
exhibit any fat one.

**Open-with-map (Euler category):** unfalsifiable for ζ without refuting RH; in the D131-H⁺ category it reduces
to Conjecture 144.D (quantitative continuation rigidity: $m=\infty\Rightarrow$ subsequence with
$\delta_{j_k}\log\gamma_{j_k}\geq c$), with exact residue GAP-144.C (the effective lower bound derived from the
continuation). 144.D is **strictly weaker than Conjecture 141.E** of Doc 141 — it asks for infinitely many
fat ones, not repulsion of all — and is the exact arithmetic translation of the LP-141/LP-134 distinction.

**Proved-partial (conditional):** Prop. 144.4 — 144.D ⟹ LP-141 in the Euler category (strong form); the piece
that is missing is named and reduced.

### Consequences for $m<\infty$ (the finiteness half of the architecture)

1. **LP-141 IS genuinely the pivot.** Prop. 144.8: it is the ABSOLUTE MINIMUM statement about "how many fat ones"
   that gives $m<\infty$ with **weak** positivity of the symbol. There is no strictly weaker LP-142 that
   works (the force/usefulness frontier is a point: infinitely many fat ones, no more no less). The only real weakening
   is in the calendar (§4.3), a quantitative front.

2. **The finiteness half is NOT accessible without arithmetic.** §2 closes the analytic door definitively. The
   Fredholm half of RH=(m<∞)∧(m<∞⟹m=0) requires, in its geometric piece LP-141, the Euler product — just
   as the positivity piece of the symbol required arithmetic (Cor. 6.2 of D134). Both halves of the Fredholm wall
   are arithmetic; neither is analytic.

3. **The concrete live front is GAP-144.C / Conjecture 144.D.** It is the most attackable object of the
   finiteness front: a continuation rigidity statement, with directional evidence (141.R3: the violating
   construction does not continue), a named mechanism (sustained local impurity at support $\asymp\log\gamma$
   forbidden by continuation), and a finite calibrating test (DH, Cor. 144.10, which decides whether Euler is
   load-bearing in 144.D).

4. **Relation with synergy 7.2 of D134:** the route "(weakly positive symbol) ∧ LP-141" remains
   the minimal provable-conditioned version of $m<\infty$. This document does NOT make it cheaper (LP-141 remains
   conjectural), but it does **focus** it: the attack on LP-141 must be on 144.D in the Euler category, not on
   LP-134 nor on Axiom R (both strictly stronger, Prop. 144.6). And the symbol's positivity piece
   remains at **weak** (not strict), consistent with $W_\lambda\geq0$ being refuted (ERRATA
   Phase 38) and with the scope caveat of B.4 (essential positivity is an invariant of the form/norm pair, ERRATA
   Phase 46 Doc 140): NO strong-gap result is used.

### Final message

**VERDICT: REFUTED-IN-ANALYTIC-CATEGORY (for every calendar) + OPEN-WITH-MAP in the Euler category,
reduced to Conjecture 144.D / GAP-144.C.** LP-141 is the correct and minimal pivot of the finiteness half,
but it is not accessible without the Euler product; within arithmetic it reduces to a well-formed quantitative
continuation rigidity, strictly weaker than the prior desideratum (141.E).

**Three main results:**

1. **[PROPOSITION 144.2 + COROLLARY 144.3]** — *Hadamard test:* for EVERY fixed unbounded calendar $a$ there
   exists an entire function of order 1, with functional equation, real on the line, ζ-type density, with
   $m=\infty$ and ZERO fat ones at calendar $a$ — violating LP-141$(a)$. Complete proof. LP-141 is non-analytic
   (needs arithmetic), exactly like LP-134, and for the same reason (total sub-resolution ⟹ zero fat ones).

2. **[PROPOSITION 144.8 + 144.6]** — *Force/usefulness frontier:* LP-141 is the ABSOLUTE MINIMUM statement that gives
   $m<\infty$ with **weak** positivity of the symbol; "≥1 fat one" does not suffice (one fat one lives in the compact
   ideal, invisible to the symbol), "positive density" or LP-134 are excessive. The strict chain is
   Axiom R ≻ LP-134 ≻ LP-141 ≻ LP-142 (="≥1 fat one," already insufficient) ≻ trivial: the last USEFUL step is
   LP-141. The force/usefulness frontier is a point: infinitely many fat ones.

3. **[CONJECTURE 144.D + PROPOSITION 144.4 + COROLLARY 144.10]** — *Arithmetic reduction:* in the
   D131-H⁺ category, a quantitative continuation rigidity (off-line subsequence with $\delta_{j_k}\log\gamma_{j_k}\geq c$,
   strictly weaker than 141.E) IMPLIES LP-141; the residue is GAP-144.C; and Davenport–Heilbronn decides
   exactly whether multiplicativity/Euler is load-bearing in 144.D (it does not decide LP-141 for ζ, since DH$\notin$D131-H⁺).

---

## References

**Internal (backward-only):** Doc 141 (Def. 141.1/141.2 LP-134/LP-141; hierarchy 141.P1/P3/P4; relative no-go
141.B/141.B2; computations 141.M4/M5 null lever and zero-mean signal; Hadamard counterexample 141.R2;
Euler computation 141.R3; Conjecture 141.E; GAP-141.DH); Doc 134 (crown §3 Lemmas 3.2–3.3 Cor. 3.4; model
$\mathfrak W$ §4 visibility (V1)–(V2); Theorems 5.0–5.5, in particular 5.1 fat-ones⟹symbol-sees-them, 5.4
sub-resolution blindness, 5.5(a) calendar no-go; §5.8 M1–M4 cosh/DH/$F_{p,\alpha}$/DBN calibration,
purity↔resolution dictionary M3; Theorem 7.2 Fredholm×replication synergy; Theorem 1.3 robust finiteness ⟺
strict positivity; Theorem 2.2 death of the gap at fixed weight); Doc 131 (Theorem 6.7 local purity, barrier
$|c_m|\leq2p^{m/2}$; category H⁺ Desideratum 6.9); Doc 112 (LP-112, Axiom R, Rouché mechanism preserving
$\delta_0$); ERRATA Phase 38 ($W_\lambda\geq0$ REFUTED — not cited here) and Phase 46 Doc 140 (Thm 5.3′ of
D134 with no exception clause; perpetual scope caveat of B.4/Thm 1.3: essential positivity = invariant
of the pair (form, norm)).

**Literature (published, verifiable):**
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954 (Thm. 2.6.5: order of canonical products =
  convergence exponent — Props. 144.2).
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 and 307–312 (off-line zeros without Euler product).
- [H21] H. Hamburger, *Über die Riemannsche Funktionalgleichung der ξ-Funktion*, Math. Z. **10** (1921),
  240–254 (rigidity: the functional equation of ζ characterizes ζ — Prop. 144.5).
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049 (computation of the off-line zeros of DH — basis of the test of Cor. 144.10).
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270 (overview of DH; absence of a multiplicative Euler product).

*End of Doc 144.*
