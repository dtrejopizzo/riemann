# Doc 150 — Adversarial audit of Docs 144 and 146 (LP-141 / GAP-141.DH)

**Program:** Riemann Hypothesis — Phase 48: AUDIT AND PURITY.
**Role of the document:** audit with a kill mandate on the load-bearing pieces of Doc 144
(Hadamard counterexample 144.2/144.3; boundary 144.8; reduction 144.4/144.D; strength chain 144.6)
and of Doc 146 (GORDOS verdict of GAP-141.DH; implication for LP-141; "cheap repulsion / lacking purity").
Prerequisites read in full at the source: Doc 144, Doc 146, Doc 141 entire, Doc 134
(§3 algebra/ideal/crown, §4 model $\mathfrak W$, §5 Theorems 5.0–5.5 and 5.5bis, §5.8 M1–M4),
ERRATA E46.4 (Thm 5.3′ corrected: strict ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$,
WITHOUT exception clause; erratum of the degenerate case of 5.2(iv); caveat B.4).

**Contract:** [VERIFIED] = re-derived and sound. [REFUTED] = counterexample or logical error exhibited, with
proof. [OVERCLAIMED] = the support proves a statement strictly weaker than the statement. [REPAIRABLE] = a concrete
correction given. [literature GAP] = datum not verifiable at page level, declared and NOT used as the basis of any verdict.

---

## 0. Verdict per piece

| piece | verdict | detail |
|---|---|---|
| **Prop. 144.2 + Cor. 144.3** (adapted Hadamard refutes LP-141 ∀ calendar) | **[VERIFIED]** | order exactly 1 ✓; no $e^{A+Bs}$ factor (parity forces it to 0) ✓; functional equation and reality ✓; density $\asymp T\log T$ (not $\sim$, see §1.3 — harmless) ✓; quantifier $\forall a\,\exists F_a$ correct and the only one possible ✓ |
| **Prop. 144.8** ("≥1 fat one" is not enough; LP-141 is the minimum) | **[VERIFIED]** against the errata | uses corrected 5.3′/5.4, not the old version; nuance declared in §2.3 about the parenthetical "(and strictly)" — the load-bearing piece only needs the weak version and survives |
| **Prop. 144.1(a)** (LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ ∀$a\succeq\psi$) | **[REFUTED as stated]** [REPAIRABLE] | closed counterexample (§3.2): $\delta_j=1/(2\psi(\gamma_j))$ satisfies LP-134$^{(\psi)}$ and violates LP-141$(\psi)$; invariance under constants of the class $\{C\log\}$ holds for LP-134 (liminf) but **NOT for LP-141** (threshold $\geq1$); correct form: LP-134$^{(\psi)}\Rightarrow\exists C:\mathrm{LP\text{-}141}(C\psi)$ |
| **Prop. 144.4** (144.D ⟹ LP-141 ∀$a\succeq\log$, "strong form at the log calendar") | **[OVERCLAIMED]** [REPAIRABLE] | same failure: 144.D with constant $c<1$ gives LP-141 only at calendar $\lceil1/c\rceil\log$, with $c=c(F)$ **internal to the function** — the constant internal to the world of 141.A/P43 reappears (§3.3); the repaired implication is valid at the class level |
| **Conjecture 144.D** (well-posedness) | **[VERIFIED]** with a remark | well formed, not circular as a conjecture; but it is almost tautological with respect to LP-141 (it is LP-141 with explicit scale); the real content ("continuation rigidity") remains a named mechanism, not an independent hypothesis (§3.4) |
| **Chain 144.6** (Axiom R ≻ LP-134 ≻ LP-141 ≻ LP-142, all strict) | **[OVERCLAIMED]** [REPAIRABLE] | the separator for Axiom R ≻ LP-134 is **misquoted** (141.P4(iii) gives LP-141⟹̸AxR, which does not separate that link); correct trivial separator given in §3.5; the link LP-134 ⟹ LP-141 inherits the failure of 144.1(a); LP-141 ≻ LP-142 ✓ intact |
| **Doc 146, strong "GORDOS" verdict** ($\liminf_{\rho\,\mathrm{off}}\delta_\rho>0$, "not even modulo $\log\gamma$") | **[REFUTED]** | liminf/limsup logical error in the use of Fact 146.6 (§4.2) + the very universality invoked in §3.2 of Doc 146 forces $\liminf\delta_\rho=0$ (Prop. 150.2, proof via joint universality + Rouché, §4.3); D–H does **NOT** satisfy band separation nor the "strongest form of LP-134" |
| **Doc 146, weak statement** (∃ infinitely many fat ones = LP-141 for D–H) | **[VERIFIED]** | solid and unconditional: infinitely many zeros with $\beta>1$ [DH36] ⟹ $\delta_j\geq\tfrac12$ in an infinite subsequence ⟹ LP-141$(a)$ for every unbounded calendar (§4.5) |
| **Doc 146, LP-134$^{(\log)}$ for D–H** (case (b) vs (d) of 144.9) | **OPEN** | the question that Cor. 144.10 actually commissioned ($\liminf\delta_j\log\gamma_j$) is NOT decided by the qualitative literature (§4.6); Doc 146 answered a different (stronger) question, and answered it wrong |
| **Consistency 144↔146 and "cheap repulsion"** | consistent on LP-141; **the "repulsion" rhetoric must be corrected** | what is cheap is *abundant fatness* (LP-141), NOT *repulsion* (LP-134): the quasi-Euler of D–H produces infinitely many fat ones AND zeros arbitrarily close to the line (§5) |

---

## 1. Re-derivation of the Hadamard counterexample (Prop. 144.2)

### 1.1. Convergence, order and genus — [VERIFIED]

Data: in coordinate $z$ ($s=\tfrac12+iz$), real sea $\pm t_n$, $t_n=n/\log(n+2)$; quadruples
$\{\pm z_j,\pm\bar z_j\}$, $z_j=\gamma_j-i\delta_j$, $\gamma_j=2^j$,
$\delta_j=\min(\tfrac14,\,1/(j\,a(2^j)))$;
$$G(z)=\prod_{n}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\prod_{j}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$

*Convergence.* In $w=z^2$ the zeros are $w_n=t_n^2$ and $w_j^{\pm}=z_j^2,\bar z_j^2$. Recount:
$\sum_n t_n^{-2}=\sum_n\log^2(n+2)/n^2<\infty$ ✓; $|z_j|^2\geq\gamma_j^2=4^j$ ⟹
$\sum_j 2|z_j|^{-2}\leq2\sum_j4^{-j}<\infty$ ✓. The product in $w$ is **canonical of genus 0**
($\sum|w_k|^{-1}<\infty$): converges absolutely and locally uniformly. ✓

*Order exactly 1 (not just $\leq1$).* Counting function in $w$: $n_w(r)=\#\{t_n\leq\sqrt r\}+O(\log r)
\asymp\sqrt r\log r$; convergence exponent in $w$ $=\tfrac12$ (at $\tfrac12$ exactly:
$\sum t_n^{-2\lambda}$ converges ⟺ $\lambda>\tfrac12$... more precisely $\sum_n(\log(n+2)/n)^{2\lambda}$
converges ⟺ $2\lambda>1$). By Boas [B54, Thm. 2.6.5] (the order of a canonical product = the convergence
exponent of its zeros), $P(w)$ has order $\tfrac12$ in $w$, exactly. Hence $G(z)=P(z^2)$ has order
**exactly $1$** in $z$. ✓ The lower bound is also seen directly in $z$: $\sum_n t_n^{-1}=
\sum\log(n+2)/n=\infty$ ⟹ convergence exponent $\geq1$ in $z$ ⟹ order $\geq1$. ✓
The off quadruples contribute counting function $O(\log r)$: irrelevant for the order. ✓

*Genus.* The phrase in Doc 144 "genus-0 product in $w$" is correct. In $z$, the Hadamard genus
would be 1 (since $\sum1/|a_k|=\infty$), but the symmetric pairing $(1-z/t)(1+z/t)=(1-z^2/t^2)$ identically
cancels the exponential factors $E_1$: the product in $w$ IS the factorization, with no genus-1 primary
factors. There is no error.

### 1.2. The functional equation and the factor $e^{A+Bs}$ — [VERIFIED]

The potential objection was: Hadamard's theorem for order 1 gives $G(z)=e^{A+Bz}\prod E_1(z/a_k)$ — can
$B$ be chosen compatible with $G(-z)=G(z)$ AND with reality on the line? **The objection does not bite because
the construction does not represent a given function: it DEFINES it as the even product.** $G$ is even by
construction (every factor depends on $z^2$), so $F_a(s):=G(\frac{s-1/2}{i})$ satisfies $F_a(1-s)=F_a(s)$
exactly, with no exponential factor ($B=0$ forced by parity: if $G$ is even and $G=e^{A+Bz}\Pi$ with $\Pi$ the
even product, then $e^{Bz}$ even ⟹ $B=0$). Reality on the line: each factor has real coefficients
in $w$ — those of the sea trivially; those of the quadruples,
$(1-w/z_j^2)(1-w/\bar z_j^2)=1-2w\,\Re(z_j^2)/|z_j|^4\cdot|z_j|^4/|z_j|^4\,\dots$ — explicitly
$1-w\bigl(\tfrac1{z_j^2}+\tfrac1{\bar z_j^2}\bigr)+\tfrac{w^2}{|z_j|^4}$ with
$\tfrac1{z_j^2}+\tfrac1{\bar z_j^2}=2\Re(z_j^2)/|z_j|^4\in\mathbb R$ ✓. Hence $G(\bar z)=\overline{G(z)}$,
$G|_{\mathbb R}\subseteq\mathbb R$, $F_a$ real on $\tfrac12+i\mathbb R$. ✓ Band:
$|\Im z_j|=\delta_j\leq\tfrac14<\tfrac12$ ✓. The multiset of zeros is invariant under $z\mapsto-z$ and
under conjugation ✓: the symmetry of the multiset TOGETHER WITH the definition-as-product resolve question (ii)
of the protocol with no residue left.

### 1.3. "Zeta-type density" — [VERIFIED with a non-load-bearing nuance]

$t_n\leq T\iff n\lesssim T\log T$: $N_{F_a}(T)\asymp T\log T$, the same ORDER as Riemann–von Mangoldt but
with constant $1$, not $\tfrac1{2\pi}$. Prop. 144.2 states $\asymp$, and that is exactly what it proves: **there is no
formal overclaim**. If some future piece needed the exact asymptotic
$N(T)\sim\frac{T}{2\pi}\log\frac T{2\pi}$, it suffices to rescale the sea ($t_n$ defined implicitly by
$\#\{t_m\leq r\}=\lfloor\frac r{2\pi}\log\frac r{2\pi}\rfloor$; the convergence series do not change).
Nuance recorded: "zeta-type density" should be read as $\asymp$, not $\sim$.

### 1.4. The calibration $\delta_j=\min(\tfrac14,1/(j\,a(2^j)))$ and the order of quantifiers — [VERIFIED]

*Sub-resolution.* For the $j$ with $j\,a(2^j)>4$ (all but finitely many: $j\,a(2^j)\geq j\to\infty$ even
with $a$ bounded): $\delta_j a(\gamma_j)=1/j\to0$ ✓. The finitely many initial $j$ with $\delta_j=\tfrac14$
can be fat ($a(2^j)/4\geq1$ possible) — but they are **finite**, and LP-141 requires **infinitely many**
fat ones: $|\mathcal G_a|<\infty$ with $m=\infty$ violates LP-141$(a)$. ✓ (The document's phrase "$|\mathcal G_a|=0$
eventually" is slightly clumsy — the correct statement is "$\mathcal G_a$ finite" — with no consequence.)

*Quantifiers.* The proposition is $\forall a\ \exists F_a$: the calendar is fixed FIRST and $\delta_j$
uses only the values $a(2^j)$ of the already-fixed calendar. That is exactly the order needed to refute
LP-141 in the category, because LP-141$(a)$ is a statement at a fixed calendar and Cor. 144.3 concludes
**for each fixed calendar**. The reverse order ($\exists F\ \forall a$: a single function with zero fat
quadruples at EVERY calendar) is **impossible** — Theorem 141.A constructs the adapted calendar $a_Z$ that
makes every quadruple of any configuration fat — and Doc 144 does NOT claim it (it states this correctly in
§2.2 and in 144.3: "for each fixed calendar, a member that violates it"). ✓ The refinement over 141.R2
(which only covered sub-exponential calendars) is genuine and the calculation $\delta_j a(\gamma_j)=1/j$
is exact.

**Verdict §1: Prop. 144.2 and Cor. 144.3 SURVIVE the audit intact.** The only weak point of
all of §2 of Doc 144 is not in 144.2 but in what is concluded afterward with the class $\{C\log\}$ (§3 below).

---

## 2. Prop. 144.8 against the errata (E46.4) — [VERIFIED with a nuance]

### 2.1. Does it use the old (false) version of Thm 5.3?

No. The proof of 144.8(a) rests on: (1) an isolated fat one = a finite-support section in windows
$\in\mathcal J$ (Def. 3.1 of D134: $\mathcal J$ contains every finite-support section) — this is
ideal algebra, independent of 5.3; (2) the tail $\delta_j=e^{-\gamma_j}$ is strictly
sub-resolution ⟹ Theorem 5.4 (absorption: $Q-Q^{\mathrm{aut}}\in\mathcal J$); (3)
$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, positive. None of the three steps invokes the false exception clause
of the old 5.3(ii). Against the corrected 5.3′ (strict ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$)
the construction is CONSISTENT: in the strictly sub-resolution regime of Def. 4.4, the quadruples
with $\theta_j=0$ do not populate $J_n^{\mathrm{vis}}$, so there is only ONE visible window (that of the
fat one $\gamma_0=10$): finitely many ⟹ 5.3′ gives strict. ✓

### 2.2. "An infinite subsequence is needed" against 5.1/5.2 post-errata

Theorem 5.1 of D134 (re-read at the source) requires a subsequence $j_k$ with $\theta_{j_k}\geq c$ **and
$\gamma_{j_k}\to\infty$**: the limit point of Lemma 3.3 needs $n_k\to\infty$; a single fat one (or finitely many)
gives a negative eigenvalue only in finitely many windows, which the truncation $A^{(N)}\in\mathcal J$ erases
(Lemma 3.2). The claim of 144.8 is exactly the mechanism of 5.1 read at the contrapositive, and it coincides
with calibration M1 (cosh: $m$ finite ⟹ strictly positive symbol). Erratum 2 of E46.4 (degenerate
case of 5.2(iv), $\vartheta_n\leq\omega_n$) is NOT invoked by 144.8. ✓

### 2.3. The honest nuance (non-load-bearing)

The parenthetical in 144.8(a) "$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, weakly **(and strictly)** positive"
depends on modeling the tail $e^{-\gamma_j}$ as strictly sub-resolution ($\theta_j=0$, absorbed in
$R_n/C_n$). If instead it were modeled as "visible fine ones" ($\theta_j>0$, $\theta_j\to0$), Theorem 5.2 +
corrected 5.3′ give: weak YES, **strict NO** ($0\in\mathrm{spec}$, infinitely many visible windows). The
load-bearing statement of 144.8(a) — "**weak** positivity + ≥1 fat one is consistent with $m=\infty$" —
survives under BOTH readings, because synergy 141.P3 only uses the weak version. Cosmetic recommendation:
delete the parenthetical "(and strictly)" or condition it explicitly on $\theta_j=0$. With that, **144.8(a), (b)
and (c) are VERIFIED** and the boundary "infinitely many fat ones, no more no less" (Obs. 144.8bis) is the
faithful shadow of Theorem 5.1.

---

## 3. The reduction 144.4 / Conjecture 144.D — the central finding about Doc 144

### 3.1. Well-posedness and non-circularity of 144.D

As a conjecture, 144.D is well formed: it is a statement about the multiset of zeros of the members of
a category (D131-H⁺), of the same logical type as LP-134/LP-141. There is no **logical** circularity (a
conjecture may mention the zeros). But one must say what it is: **144.D is not an independent "continuation
rigidity property" that implies LP-141; it IS LP-141 with the scale $\log$ made explicit and in subsequence-liminf
form, restricted to the Euler category.** "Quantitative continuation rigidity" is the *proposed mechanism*
(the italicized paragraph of 144.D), not a separate mathematical hypothesis. Prop. 144.4 is, accordingly, an
almost tautological reformulation (its proof is a one-line rescaling), and the value of §3 of Doc 144 is
taxonomic (144.D ≺ 141.E, the correct front), not deductive. The document itself admits this (144.4bis), so
this is emphasis, not an erratum. What follows IS an erratum.

### 3.2. [REFUTED] Prop. 144.1(a) is false as stated

**Counterexample 150.1 [COUNTEREXAMPLE].** Let $\psi(\gamma)=\log(\gamma+3)$ and the configuration
$Z^*:=\{(\delta_j,\gamma_j)\}_{j\geq1}$ with $\gamma_j=2^j$, $\delta_j:=\dfrac1{2\,\psi(\gamma_j)}$
(admissible: $\delta_j\in(0,\tfrac12)$, finitely many per window, $m=\infty$). Then:
- $\delta_j\,\psi(\gamma_j)=\tfrac12$ for all $j$: $\liminf=\tfrac12>0$ ⟹ **LP-134$^{(\psi)}$ holds**.
- $\mathcal G_\psi=\{j:\delta_j\psi(\gamma_j)\geq1\}=\emptyset$ and $m=\infty$ ⟹ **LP-141$(\psi)$ is FALSE**
  in $Z^*$.

And $a=\psi$ satisfies the hypothesis "$a\succeq\psi$" of 144.1(a). Hence the statement
"LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ for every $a\succeq\psi$" is **false** with $a=\psi$. $\square$

*Where the proof of Doc 144 breaks down:* the proof of 144.1(a) itself detects the problem ("If $c<1$,
rescale the calendar: $a':=\lceil1/c\rceil a$") and then buries it with the phrase "since $\{C\log\}$ is ONE
calendar class (invariance under constants, Obs. 1.1(i) of Doc 141), LP-141 holds for the class $\{C\log\}$."
But Obs. 1.1(i) of Doc 141 proves invariance under constants **for LP-134** (the liminf absorbs $C$ into $c$),
and that invariance **is FALSE for LP-141**: the threshold "$\delta_j a(\gamma_j)\geq1$" does not absorb
constants. Counterexample 150.1 separates LP-141$(\psi)$ from LP-141$(2\psi)$ (in $Z^*$ with
$\delta_j=1/(2\psi)$: at calendar $2\psi$ every quadruple is fat; at calendar $\psi$, none is):
**LP-141$(C\log)$ is a family of genuinely distinct statements in $C$, monotonically decreasing in
strength** (Obs. 144.0(iii)), not a class.

**Correct form and repair [REPAIRABLE]:**
$$\mathrm{LP\text{-}134}^{(\psi)}\ \Longrightarrow\ \mathrm{LP\text{-}141}(a)\quad\text{for every }a\text{ with }a/\psi\to\infty,
\qquad\text{and}\qquad \mathrm{LP\text{-}134}^{(\psi)}\ \Longrightarrow\ \exists C>0:\ \mathrm{LP\text{-}141}(C\psi),$$
where $C=\lceil1/c\rceil$ and $c$ is the liminf constant — **internal to the configuration/function**. The
implication at a FIXED calendar of the same class does not hold.

### 3.3. Propagation to Prop. 144.4 — [OVERCLAIMED]

Prop. 144.4 states: "if 144.D holds, then LP-141$(a)$ holds for every calendar $a\succeq\log$...
In fact the strong form holds: $m=\infty\Rightarrow$ infinitely many fat ones at calendar $\log$." Its proof
constructs $a=\lceil1/c\rceil\log$ and applies monotonicity for $a'\succeq a$. That establishes LP-141$(a')$ only
for $a'\succeq\lceil1/c\rceil\log$ — **not** for every $a'\succeq\log$ (e.g. not for $a'=\log$ itself if
$c<1$), and the "strong form at calendar $\log$" **is not proved**: with $c<1$, 144.D is consistent with
zero fat ones at calendar $\log$ (configuration 150.1 with subsequence $\liminf=c=\tfrac12$). Repaired
statement:
$$\textbf{144.4′}:\quad \text{144.D}\ \Longrightarrow\ \exists C=C(F)>0:\ \mathrm{LP\text{-}141}(C\log)\ \ \text{and}\ \ \mathrm{LP\text{-}141}(a)\ \forall a\ \text{with } a/\log\to\infty.$$

**Why this is NOT cosmetic.** Synergy 141.P3 needs LP-141$(a)$ and weak positivity of the symbol
$\sigma_a(Q)$ **at the same calendar $a$**. With 144.4′, the calendar at which the fat ones are obtained is
$C(F)\log$ with $C(F)$ internal to the function: closing $m<\infty$ would require weak positivity of the
symbol at calendar $C(F)\log$ — or, uniformly, **for the whole family $\{C\log\}_{C\in\mathbb N}$** (which
by Prop. 5.5bis(iii) of D134 is a decreasing condition: positivity at higher calendars is MORE
demanding). That is: the failure of invariance reintroduces exactly the **constant internal to the world**
that Theorem 141.A diagnosed as the trivialization of the free calendar, now in miniature (a constant
factor, not an arbitrary calendar). It does not kill the route — a constant factor over the class $\log$ is
infinitely more benign than the adapted calendar $a_Z$ of 141.A — but it **must be declared**: the honest
version of the route is
$$m<\infty\ \Longleftarrow\ \bigl[\sigma_{C\log}(Q)\geq0\ \text{weakly }\forall C\in\mathbb N\bigr]\ \wedge\ \text{144.D}.$$
The same correction applies to Prop. 144.9(b) of Doc 144 ("DH satisfies LP-134$^{(\log)}$... a fortiori
LP-141" — a fortiori LP-141$(C\log)$ for some $C$, not LP-141$(\log)$), and retroactively applies to Prop.
141.P4(i) of Doc 141, which contains the same rescaling step with the same gap ("rescaling $a$ they are
fat" — rescaling $a$ changes the statement).

### 3.4. Does 144.4 hide an "almost everywhere"?

No. Modulo the calendar repair of §3.3, the implication 144.D ⟹ LP-141$(C\log)$ is exact, with no
density steps nor "almost everywhere" steps: an infinite subsequence with $\delta_{j_k}\log\gamma_{j_k}\geq c$
literally becomes an infinite subsequence of fat ones at calendar $\lceil1/c\rceil\log$. The
implication is complete (and precisely for that reason, thin: all the work lies in 144.D).

### 3.5. The strength chain 144.6 — misquoted separator [REPAIRABLE]

The chain Axiom R ⟹ LP-134 ⟹ LP-141 ⟹ LP-142 with "no arrow reverses" cites three separators:
144.1(b) (LP-141⟹̸LP-134 ✓ correct), **Prop. 141.P4(iii) (LP-141⟹̸Axiom R)** and 144.8(a)
(LP-142⟹̸LP-141 ✓ correct). The second does NOT separate the link it is supposed to separate: the strictness of
"Axiom R ≻ LP-134" requires **LP-134 ⟹̸ Axiom R**, and "LP-141⟹̸AxR" does not imply it (LP-134 is stronger
than LP-141: it could imply AxR even if LP-141 does not). As cited, the strictness of the FIRST
link remains unproved.

**Correct separator (trivial) [PROPOSITION 150.3].** The single-quadruple configuration
$Z_1=\{(\tfrac14,\gamma_0)\}$ (the cosh anti-model, M1 of D134) satisfies LP-134$^{(\psi)}$ for every scale
(finite off set ⟹ $\liminf:=+\infty$, convention of Def. 141.1) and **violates Axiom R**
quantitatively, whose recorded consequence in 141.P4(ii) is "$m\geq1\Rightarrow$ infinitely many fat ones":
here $m=1\geq1$ and the fat ones are finitely many. $\square$

Moreover the link LP-134 ⟹ LP-141 of the chain inherits the failure of 144.1(a) (§3.2): at a fixed calendar
it is false; the chain holds **at the class level** ($\exists C$). Final state of the chain after repairs:
$$\text{Axiom R}\ \succ\ \mathrm{LP\text{-}134}^{(\psi)}\ \succ\ \bigl[\exists C:\mathrm{LP\text{-}141}(C\psi)\bigr]\ \succ\ \bigl[\exists C:\mathrm{LP\text{-}142}(C\psi)\bigr],$$
all strict with separators: 150.3, 144.1(b), 144.8(a). The structural conclusion of Doc 144 (LP-141
is the minimal pivot; "≥1 fat one" is not enough) **survives intact** — only it lives in the class, not at
the individual calendar.

---

## 4. Doc 146: the critical point — $\liminf\delta_\rho>0$ or just $\exists\infty$ fat ones?

### 4.1. The two statements, separated precisely

On the off zeros $\rho_j=\beta_j+i\gamma_j$ of D–H, $\delta_j=|\beta_j-\tfrac12|$:

- **(STRONG)** $\liminf_j\delta_j\geq c>0$: ALL off zeros are eventually at distance $\geq c$
  (band separation; the $\psi\asymp1$ form of LP-134, "not even modulo $\log\gamma$"). This is what
  Doc 146 claims in the box of §4.1 and in the summary (point 1).
- **(WEAK)** $\#\{j:\delta_j\geq c\}=\infty$ for some $c>0$: infinitely many fat ones. This is ALL that
  LP-141 needs (and more: fat at a constant, not only at a calendar).

The support of Doc 146 — [DH36] (infinitely many zeros with $\beta>1$), the witness [BS07]
($\delta\approx0.31$ at $\gamma\approx85.7$), and Fact 146.6 (density $\gg T$ in ONE fixed strip
$(\sigma_1,\sigma_2)$, $\sigma_1>\tfrac12$) — proves the WEAK statement with room to spare. **None of the three proves the
STRONG one**, and the step of Doc 146 that claims to deduce it is a pure logical error:

> (Doc 146, §2.3) "Fact 146.6 exhibits infinitely many zeros with $\delta_j\geq\sigma_1-\tfrac12$ constant.
> Hence $\liminf_{\rho\ \text{off}}\delta_\rho\geq\sigma_1-\tfrac12>0$."

A liminf over ALL off zeros is not bounded below by exhibiting a distant SUBFAMILY: that bounds the
**limsup**. For the liminf one must exclude zeros close to the line — about which Fact 146.6 is
silent. It is exactly the liminf/limsup confusion that Doc 144 §1.1(i) erects as "the atomic
difference between LP-134 and LP-141" — committed by the sister document of the same phase.

### 4.2. The STRONG statement is not merely unsupported: it is FALSE (modulo joint universality, a published theorem)

**Proposition 150.2 [PROPOSITION] (the off zeros of D–H approach the line: $\liminf_j\delta_j=0$,
with density $\gg T$ at every distance).** Let $f=\frac{\sec\theta}2(e^{-i\theta}L_1+e^{i\theta}L_2)$ be the
D–H function (Def. 146.2; $L_1=L(s,\chi)$, $L_2=L(s,\bar\chi)$, $\chi$ a primitive complex character mod 5).
Then for every $\varepsilon\in(0,\tfrac18)$ there exist infinitely many zeros $\rho$ of $f$ with
$\delta_\rho\in[\tfrac\varepsilon2,\tfrac{3\varepsilon}2]$; in fact $\gg_\varepsilon T$ of them with
$0<\gamma\leq T$. Consequently $\liminf_{\rho\ \mathrm{off}}\delta_\rho=0$ and D–H **does not** satisfy
any band separation.

*Proof.* Let $\sigma_0:=\tfrac12+\varepsilon$, $r:=\tfrac\varepsilon2$, and the disk
$\overline D:=\{|s-\sigma_0|\leq r\}\subset\{\tfrac12<\Re s<1\}$. Define the targets
$$g_2(s):\equiv1,\qquad g_1(s):=-e^{2i\theta}\exp\Bigl(\frac{s-\sigma_0}{r}\Bigr),$$
continuous and **zero-free** on $\overline D$, holomorphic in its interior. The target combination is
$$h(s):=e^{-i\theta}g_1(s)+e^{i\theta}g_2(s)=e^{i\theta}\Bigl(1-\exp\Bigl(\tfrac{s-\sigma_0}{r}\Bigr)\Bigr),$$
which has in $\overline D$ a single, simple zero, at $s=\sigma_0$ (the other zeros of $1-e^w$ lie in
$w\in2\pi i\mathbb Z\setminus\{0\}$, outside $|w|\leq1$). On the circle $|s-\sigma_0|=r/2$
(i.e. $|w|=\tfrac12$): $|h|=|1-e^w|\geq m_0>0$ with $m_0:=\min_{|w|=1/2}|1-e^w|$ (an absolute constant;
$m_0\geq1-e^{-1/2}>0.39\cdot e^{-1/2}$... it suffices that $m_0>0$, which holds because $1-e^w$ does not
vanish on $|w|=\tfrac12$ and the minimum of a positive continuous modulus on a compact set is positive).

By Voronin's **joint universality theorem** for Dirichlet $L$-functions of inequivalent characters
($\chi\neq\bar\chi$ mod 5; [V75-joint], textbook form in [KV92] and [St07, Thm. 1.10]): the set
$$\mathcal T:=\Bigl\{\tau>0:\ \max_{j=1,2}\ \sup_{|s-\sigma_0|\leq r/2}\bigl|L_j(s+i\tau)-g_j(s)\bigr|<\tfrac{m_0}3\Bigr\}$$
has positive lower density in $[0,T]$. For $\tau\in\mathcal T$, on $|s-\sigma_0|=r/2$:
$$\bigl|\,\bigl(e^{-i\theta}L_1+e^{i\theta}L_2\bigr)(s+i\tau)-h(s)\bigr|\leq|L_1(s+i\tau)-g_1(s)|+|L_2(s+i\tau)-g_2(s)|<\tfrac{2m_0}3<|h(s)|,$$
and by Rouché $e^{-i\theta}L_1+e^{i\theta}L_2$ — hence $f$, which differs by the nonzero factor
$\tfrac{\sec\theta}2$ — has a zero $\rho$ with $|\rho-(\sigma_0+i\tau)|<r/2$, i.e.
$\delta_\rho=|\beta_\rho-\tfrac12|\in(\varepsilon-\tfrac\varepsilon4,\,\varepsilon+\tfrac\varepsilon4)
\subset[\tfrac\varepsilon2,\tfrac{3\varepsilon}2]$. Taking $\tau$'s from $\mathcal T$ separated by
$\geq r=\tfrac\varepsilon2$ (still a set of cardinality $\gg_\varepsilon T$ in $[0,T]$ by the
positive lower density), the resulting zeros are distinct: $\gg_\varepsilon T$ zeros with
$\delta_\rho\asymp\varepsilon$ and $0<\gamma\leq T$. Since $\varepsilon$ is arbitrary,
$\liminf\delta_\rho=0$. $\square$

*Status of the citations.* The joint universality of $L(s,\chi_1),\dots,L(s,\chi_k)$ for pairwise
inequivalent characters, on compact sets $K$ in the strip $\tfrac12<\Re s<1$ with connected complement and
continuous zero-free targets on $K$, holomorphic in the interior, with positive lower density of the set of
$\tau$'s, is a PUBLISHED theorem of Voronin (1975, thesis and papers; textbook treatment:
Karatsuba–Voronin, *The Riemann Zeta-Function*, De Gruyter 1992; Steuding, *Value-Distribution of
L-Functions*, Springer LNM 1877, 2007). The universality+Rouché argument to produce $\gg T$ zeros of
linear combinations in any sub-strip is likewise standard and published: it is recorded by
Kaczorowski–Kulas (combinations of $L$-functions, zeros off the critical line) and, with a two-sided
bound $\asymp T$ for Dirichlet series with periodic coefficients without an Euler product,
**Saias–Weingartner, Acta Arith. 140 (2009)**: for such $f$, the number of zeros with
$\beta\in(\sigma_1,\sigma_2)$, $0<\gamma\leq T$ is $\asymp T$ **for every** $\tfrac12<\sigma_1<\sigma_2\leq1$
— in particular with $\sigma_1$ arbitrarily close to $\tfrac12$. [literature GAP: the exact statements
of Kaczorowski–Kulas and the precise page of Saias–Weingartner were not verified at page level;
Prop. 150.2 does NOT depend on them — it depends only on Voronin's joint universality, which is
textbook material. They are cited as independent corroboration.]

*Decisive internal remark:* Doc 146 §3.2 itself invokes "Voronin universality holds on the whole right
critical strip $\tfrac12<\sigma<1$" to justify the strip regime — without noticing that THAT VERY SAME
universality, applied with $\sigma_1\downarrow\tfrac12$, produces Prop. 150.2 and destroys its own box.
The argument of §3.2 of Doc 146 ("that would require $L_1/L_2\to-e^{2i\theta}$ FORCEDLY on approaching
the line, and there is no such forcing — the line is not special for the quotient") confuses "not all
zeros collapse onto the line" (true, and compatible with infinitely many fat ones) with "no zero approaches
the line" (false: since the line is not special for the quotient, the phase condition is realized ALSO
arbitrarily close to it — that is exactly what universality gives).

### 4.3. Secondary errors in §3 of Doc 146 (recorded)

1. **Calculation 146.A:** invokes "universality (Voronin) in any strip $1<\sigma_1<\sigma<\sigma_2$" —
   Voronin universality lives in $\tfrac12<\sigma<1$, NOT in $\sigma>1$. In $\sigma>1$ the correct
   mechanism is Bohr almost-periodicity / Kronecker–Weyl density of $(p^{-it})_p$ on the torus:
   the quotient $L_1/L_2$ on a vertical $\sigma_0>1$ has image with closure determined by the
   Euler factors, and the phase condition is realized only for $\sigma_0$ in a bounded range
   ($1<\sigma_0<\sigma^*$): for $\sigma$ large, $|f-1|<1$ dominant term) and there are NO zeros — "any
   strip $1<\sigma_1<\sigma_2$" is false for large $\sigma_1$. The conclusion the document needs
   (infinitely many zeros with $\beta>1$) is genuine [DH36] and is not affected.
2. **Summary point 3:** "the image $\{f(s):\sigma>1\}$ is dense" — false ($|f|$ is bounded on
   $\sigma\geq\sigma_1>1$); the correct statement is "$0$ belongs to the closure of the image of the verticals
   $1<\sigma_0<\sigma^*$" (Bohr).
3. **§4.1/summary:** "the off zeros cluster near fixed verticals, not near the line" — the
   first half is true FOR A SUBFAMILY; the second half is false (Prop. 150.2: they also cluster,
   with density $\gg T$, near the line — at EVERY distance $\varepsilon$).

### 4.4. What Doc 146 actually proved, and the corrected verdict

**[CORRECTED GAP-141.DH VERDICT].**
- **Proved (unconditional, [DH36]):** D–H has infinitely many off zeros with $\delta_j\geq\tfrac12$ ($\beta>1$).
  Consequently, for every unbounded calendar $a$: $\delta_j a(\gamma_j)\geq\tfrac12 a(\gamma_j)\to\infty$
  on that subsequence ⟹ infinitely many fat ones ⟹ **D–H satisfies LP-141$(a)$ for every unbounded calendar**
  (without the constant failure of §3.2: here $\delta_j$ is bounded below by the absolute constant
  $\tfrac12$, so the threshold $\geq1$ is reached as soon as $a\geq2$, eventually for every unbounded $a$).
  This is what the program needed and it stands.
- **Refuted (Prop. 150.2):** $\liminf_j\delta_j>0$. D–H does **NOT** satisfy band separation
  ($\psi\asymp1$), nor "all off zeros are fat", nor the box of §4.1 of Doc 146. The clause
  "$\liminf|\beta-\tfrac12|\psi(\gamma)=+\infty$ for every scale $\psi\to\infty$" of the box is
  likewise false as quantified (the liminf runs over all off zeros, including those of
  Prop. 150.2).
- **Open:** LP-134$^{(\log)}$ for D–H, i.e. $\liminf_j\delta_j\log\gamma_j>0$ — the question that
  Cor. 144.10 of Doc 144 actually commissioned (to distinguish case (b) from case (d) of 144.9). Prop. 150.2 gives
  zeros with $\delta\asymp\varepsilon$ at heights of positive density FOR EACH FIXED $\varepsilon$, but
  violating LP-134$^{(\log)}$ would require $\delta_\rho=o(1/\log\gamma_\rho)$ along a sequence —
  a regime $\varepsilon=\varepsilon(T)\to0$ requiring EFFECTIVE universality (control of the size of the
  first admissible $\tau$ as a function of $\varepsilon$), not available in the qualitative literature.
  [literature GAP: I know of no effective results on the approach $\delta$ vs. height for D–H; I claim none.]

In the taxonomy of Prop. 144.9 of Doc 144: cases (a) ($\inf\delta_j>0$) and (c) (total
sub-resolution) are **excluded** (150.2 kills (a); [DH36] kills (c)); D–H is in (b) or (d), **undecided**.
Note that (b) and (d) are both "good side" for Cor. 144.10, so the logical implication of Doc 144
("DH is consistent with 144.D; it does not confirm it; case (d) would be evidence that LP-141 —not LP-134—
is the correct statement") remains alive and with no change of sign. What can already be said: **D–H realizes
"infinitely many fat ones WITHOUT band separation"** — the $\psi\asymp1$ version of the LP-141/LP-134
separation instantiated in nature. If (d) were further confirmed ($\delta\log\gamma\to0$ along a subsequence),
D–H would realize the separation at the $\log$ scale itself, the "most informative case" of 144.9.

---

## 5. Consistency 144↔146 and the final status of "cheap repulsion / lacking purity"

### 5.1. Are "does not decide LP-141 for ζ" (144) and "confirms LP-141 as a quasi-model" (146) consistent?

Yes, they are logically consistent: Doc 144 speaks of **decision** (DH$\notin$D131-H⁺ ⟹ no verdict
about DH refutes nor proves 144.D/LP-141 in the Euler category nor for ζ) and Doc 146 speaks of **case
evidence** (an $m=\infty$ object with quasi-Euler structure that satisfies LP-141). There is no formal
contradiction. Two real frictions remain:

1. **Doc 146 answered a different question from the one commissioned.** Cor. 144.10 explicitly asked
   "determine which of the four cases (a)/(b)/(c)/(d) occurs, reporting $\liminf_j\delta_j\log\gamma_j$".
   Doc 146 reported (a) — and in fact something stronger — with support that only gives "not-(c)". After
   correction: the real deliverable is "not-(a), not-(c), (b)∨(d) open".
2. **The rhetoric of §5 of Doc 146 overgeneralizes:** "the front shifts from 'is there repulsion?'
   (**resolved in favor in the quasi-Euler category**)..." — a single case does not resolve a category (Doc
   146 itself acknowledges this in 4.2.3 and then contradicts it in §5), and after Prop. 150.2 the content is
   the OPPOSITE: in the quasi-Euler category repulsion-of-all is FALSE (the zeros of D–H approach the
   line); what the D–H case gives is abundance of fat ones.

### 5.2. "Cheap repulsion / lacking purity" — corrected

The separation of §4.3 of Doc 146 survives, but with corrected wording, and corrected in a direction
that FAVORS Doc 144:

- **What quasi-Euler buys cheaply is NOT "repulsion" but "abundant fatness":** infinitely many off zeros at
  macroscopic distance (the $\beta>1$ of [DH36]). That is exactly the input of LP-141, and only that.
- **What quasi-Euler does NOT buy is LP-134 repulsion:** D–H has, alongside the fat ones, zeros
  arbitrarily close to the line (Prop. 150.2). Clause (a) of §4.3 of Doc 146 ("D–H shows that
  resolution repulsion does not require genuine Euler... the '⟹ fat ones' part of 141.E is cheaper than
  conjectured") must be rewritten: *D–H shows that "infinitely many fat ones" (LP-141) does not require genuine
  Euler; and it shows at the same time that quasi-Euler does NOT give "all repelled" (LP-134-band is false in
  D–H). If 141.E is true, genuine multiplicativity is load-bearing precisely for the half that quasi-Euler
  loses.* This **reinforces** the central thesis of Doc 144 (LP-141, not LP-134, is the correct pivot, and
  144.D —which only asks for the fat subsequence— is the correct front): nature provides an object that
  separates the two notions in the predicted direction, at least at scale $\psi\asymp1$.
- **The "lacking purity" half remains intact:** D–H has fat ones and $m=\infty$; what is exclusive to genuine
  Euler remains the collapse $m\to0$ (purity), not fatness. No change.
- **The table in §3.3 of Doc 146** (row D–H: "position of the off zeros: $\delta_j\geq\sigma_1-\tfrac12>0$,
  fixed strip") must be corrected to: "infinite subfamily with $\delta_j\geq\tfrac12$ ($\beta>1$) + zeros with
  arbitrarily small $\delta$ (density $\gg T$ at every distance $\varepsilon$); verdict:
  **LP-141 yes; band separation no; LP-134$^{(\log)}$ open**". The moral "the sub-resolution/fat
  boundary coincides with the no-structure/with-structure boundary" degrades to: *structure (even
  approximate) guarantees the presence of infinitely many fat ones; it does not prevent approach to the
  line.*

### 5.3. Net effect on the program

1. The minimal Fredholm-half route stands, in its honest form:
   $$m<\infty\ \Longleftarrow\ \bigl[\sigma_{C\log}(Q)\ \text{weakly positive}\ \forall C\in\mathbb N\bigr]\ \wedge\ \text{144.D},$$
   with the quantifier on $C$ explicit (a consequence of §3.2–3.3; previously hidden).
2. GAP-141.DH is reopened on its fine half: the pending datum is $\liminf_j\delta_j\log\gamma_j$ for D–H
   (case (b) vs (d)), which requires either effective universality, or targeted computation like [BS07] at
   growing heights in strips $\delta\asymp1/\log\gamma$. The coarse half (LP-141 for D–H) is
   CLOSED in the affirmative, unconditionally.
3. No result of this audit touches Prop. 144.2/144.3 (the analytic door remains closed for
   LP-141) nor Prop. 144.8 (the "infinitely many fat ones" boundary remains the pivot).

---

## Final message

**Verdicts.**
- **Doc 144:** Prop. 144.2 + Cor. 144.3 **[VERIFIED]** (exact order 1 via a canonical product in $w=z^2$ and
  Boas 2.6.5; $e^{A+Bs}$ nonexistent by parity; density $\asymp$, not $\sim$ — declared; quantifier
  $\forall a\,\exists F_a$ correct and the only one possible). Prop. 144.8 **[VERIFIED]** against E46.4 (uses
  corrected 5.3′/5.4; non-load-bearing nuance in "(and strictly)"). Prop. 144.1(a) **[REFUTED as
  stated]** and Prop. 144.4 **[OVERCLAIMED]** — both repairable at the class level $\{C\log\}$ with
  internal constant $C(F)$. Chain 144.6 **[REPAIRABLE]**: separator of the first link misquoted;
  correct trivial separator (150.3). Conjecture 144.D well formed but almost tautological with respect to
  LP-141; the reduction is complete, with no hidden "almost everywhere".
- **Doc 146:** the strong "GORDOS ($\liminf\delta>0$, not even modulo $\log\gamma$)" verdict
  **[REFUTED]** (liminf/limsup error + Prop. 150.2 via Voronin joint universality + Rouché, with
  Saias–Weingartner corroboration). The weak statement survives **[VERIFIED]**: D–H satisfies LP-141 at every
  unbounded calendar (infinitely many $\beta>1$, [DH36]). The question commissioned by 144.10
  ($\liminf\delta\log\gamma$: case (b) vs (d)) remains **OPEN**.
- **Consistency 144↔146:** no formal contradiction; Doc 146 answered a stronger question than the
  one commissioned and answered it wrong; "cheap repulsion" must be rewritten as "cheap fatness, no
  repulsion" — a correction that reinforces the thesis of Doc 144 (LP-141 is the pivot, not LP-134).

**Three main findings.**

1. **[REFUTATION — Doc 146] The strong verdict of GAP-141.DH is false.** The step "infinitely many zeros in
   a fixed strip ⟹ $\liminf_{\text{all off zeros}}\delta\geq\sigma_1-\tfrac12$" bounds a liminf with a
   subfamily (liminf/limsup confusion — the same atomic distinction LP-134/LP-141 that Doc 144
   formalizes). And it is not merely lack of support: Voronin's joint universality (which Doc 146
   §3.2 itself invokes) + Rouché give, for each $\varepsilon$, $\gg_\varepsilon T$ zeros of D–H with
   $\delta_\rho\asymp\varepsilon$ (Prop. 150.2, closed proof): $\liminf\delta_\rho=0$. What remains standing is
   what LP-141 needs: infinitely many fat ones ($\beta>1$, [DH36]) — D–H satisfies LP-141, not band
   separation; LP-134$^{(\log)}$ for D–H remains open (the (b)-vs-(d) datum that 144.10 requested is not
   decided).
2. **[COUNTEREXAMPLE — Doc 144] Invariance under constants of the class $\{C\log\}$ is false for LP-141,
   and with it the literal statements of 144.1(a) and of the "strong form" of 144.4 fall.** The configuration
   $\delta_j=1/(2\psi(\gamma_j))$ satisfies LP-134$^{(\psi)}$ and violates LP-141$(\psi)$ (Counterexample 150.1): the
   liminf absorbs constants, the threshold "$\geq1$" does not. Repair: LP-134$^{(\psi)}\Rightarrow\exists C:
   \mathrm{LP\text{-}141}(C\psi)$, and 144.D $\Rightarrow\mathrm{LP\text{-}141}(C(F)\log)$ with $C(F)$ internal
   to the function — the constant internal to the world of 141.A/P43 reappears (in miniature) inside the very
   pivot, and the honest synergy requires weak positivity of the symbol over the entire family
   $\{C\log\}_{C\in\mathbb N}$, not over a single calendar.
3. **[REPAIR — Doc 144] The strength chain 144.6 has its first separator misquoted** (141.P4(iii)
   gives LP-141⟹̸Axiom R, which does not separate Axiom R ≻ LP-134); the correct separator is trivial and is
   proved here (Prop. 150.3: the single-quadruple cosh configuration satisfies LP-134 by the finiteness
   convention and violates "$m\geq1\Rightarrow\infty$ fat ones"). With 150.1+150.3 the chain is
   strict with complete separators — at the calendar-class level. The two structural pieces of Doc 144 that
   the program carries (144.2/144.3: LP-141 is non-analytic for every calendar; 144.8: "≥1 fat one" is not
   enough, the minimal pivot is "infinitely many fat ones") survive the audit intact.

---

## References

**Internal (backward-only):** Doc 144 (Props. 144.1/144.2/144.4/144.6/144.8/144.9, Cor. 144.3/144.10,
Conjecture 144.D, GAP-144.C); Doc 146 (Defs. 146.1/146.2, Facts 146.3–146.7, Calculation 146.A, verdict
§4.1); Doc 141 (Theorem 141.A, Def. 141.1/141.2, Props. 141.P1/P3/P4, 141.R1/R2, Calculation 141.R3, Conjecture
141.E, GAP-141.DH); Doc 134 (Defs. 3.1/3.6/4.1/4.2/4.4, Lemmas 3.2/3.3/5.0, Theorems 5.1–5.5, Prop. 5.5bis,
§5.8 M1–M2); ERRATA 06-papers/ERRATA.md E46.4 (Thm 5.3′; degenerate case 5.2(iv); caveat B.4).

**Literature (published, verifiable):**
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954. (Thm. 2.6.5: order of a canonical product =
  convergence exponent — used in §1.1.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* I, II, J. London Math.
  Soc. **11** (1936), 181–185 and 307–312. (Infinitely many zeros with $\beta>1$ — support of the weak statement.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath-Brown), Oxford,
  1986, §10.25. (The D–H function, its functional equation, its off zeros.)
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math.
  Comp. **76** (2007), 2045–2049. (Witness $\rho^*\approx0.8085+i\,85.699$.)
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270. (Overview; distribution of zeros in $\sigma\geq1$.)
- [V75-joint] S. M. Voronin, universality (1975) and joint universality of Dirichlet $L$-functions
  for inequivalent characters; textbook treatment in [KV92] and [St07]. (Engine of Prop. 150.2.)
- [KV92] A. A. Karatsuba, S. M. Voronin, *The Riemann Zeta-Function*, De Gruyter, 1992. (Chapter on
  universality; cited form of the joint theorem.)
- [St07] J. Steuding, *Value-Distribution of L-Functions*, Springer Lecture Notes in Math. **1877**, 2007.
  (Thm. 1.10 joint universality; universality+Rouché method for zeros of combinations.)
- [SW09] E. Saias, A. Weingartner, *Zeros of Dirichlet series with periodic coefficients*, Acta Arith.
  **140** (2009), 335–344. (Zeros $\asymp T$ in every strip $\tfrac12<\sigma_1<\sigma_2\leq1$ for periodic
  series without Euler product — independent corroboration of Prop. 150.2. [Statement cited from memory;
  page-level verification pending — Prop. 150.2 does not depend on it.])
- J. Kaczorowski, M. Kulas, on zeros off the critical line of linear combinations of
  $L$-functions (Monatsh. Math., ca. 2007). [literature GAP: exact reference not verified; cited only as
  corroboration, not as a basis.]

*End of Doc 150.*
