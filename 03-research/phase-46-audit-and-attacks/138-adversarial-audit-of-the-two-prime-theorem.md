# Doc 138 — Adversarial audit of the two-prime theorem (Doc 135 / P48)

**Program:** Riemann Hypothesis — Phase 46: audit and attacks.
**Audited object:** Doc 135 (`phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md`) and paper P48
(`06-papers/P48-weil-positivity-finite-primes/main.tex`).
**Protocol:** closed-form re-derivation of all central identities, no
numerics; active search for sign errors, implicit hypotheses, degenerate cases
and false novelty. Precedent motivating the strictness: W_λ≥0 survived for months until
the sign error of Doc 63 §7.1 (Phase 38).

---

## 0. One-line verdict

**SURVIVES WITH ERRATA — the proofs are correct, but the core (Theorems A/B and the
additivity) IS NOT NEW in substance: it is the trivial direction of Weil's criterion
applied to a divisor placed on the critical line BY HYPOTHESIS, plus the additivity of
the logarithmic derivative of a product (classical). The only potentially new
substance is the fine structure (§5: kernel threshold, GAP-135.A), which the paper
itself leaves open.**

Breakdown: no sign error found; no fatal implicit hypothesis; four
errata located (§5 below); one internal *framing* contradiction (Obs. 2.2 vs.
Obs. 3.2) that deflates the document's own novelty justification.

---

## 1. Re-derivation of the cross-term identity $L(F\star G)=L(F)+L(G)$

### 1.1. The identity, verified from scratch

Exact definitions of the paper (Def. 2.1 / Lemma 2.2 of P48; Doc 131 Lemma 1.7,
verified to exist as cited): $\mathcal D=\{a:\mathbb Z_{\ge1}\to\mathbb C\}$
with $(a\star b)(n)=\sum_{de=n}a(d)b(e)$; $(Da)(n)=a(n)\log n$; for a normalized unit
$F$ ($F(1)=1$), $L(F)=F^{-1}\star DF$.

**Derivation.** $D(a\star b)(n)=\log n\sum_{de=n}a(d)b(e)
=\sum_{de=n}(\log d+\log e)a(d)b(e)=(Da\star b)(n)+(a\star Db)(n)$ — uses only
$\log(de)=\log d+\log e$. With commutativity and $(F\star G)^{-1}=F^{-1}\star G^{-1}$:
$L(F\star G)=F^{-1}\star G^{-1}\star(DF\star G+F\star DG)=L(F)+L(G)$. **Correct.**
The identity is pure algebra; no disguised Diophantine cancellation.

### 1.2. The three degenerate cases required by the protocol

- **$n=1$.** $DF(1)=F(1)\log 1=0$, so $L(F)(1)=F^{-1}(1)\,DF(1)=0$ always. The
  discrete datum $a$ **has no mass at $n=1$**; the diagonal atom $c_0L_p+c'_0L_q=2\log(pq)$
  lives in the $\omega$ slot (Def. 1.5 of Doc 135), which is trivially additive
  ($\omega_1+\omega_2=-2\log p-2\log q$). There is no double counting: in the boxed
  formula of Def. 1.5, the $m=0$ term of the $p$ block contributes $2L_pf(1)$ and the $n=0$
  term of the $q$ block contributes $2L_qf(1)$; the sum IS the $\omega$ atom counted once.
  **Consistent.**
- **Powers $p^aq^b$ with $a$ or $b=0$.** These are pure powers $p^a$ or $q^b$; carried
  by the corresponding $a_i$, with no collision ($p^a=q^b$ with $a,b\ge1$ is impossible
  by unique factorization; $a=b=0$ is the $n=1$ case already treated). **Correct.**
- **Was the diagonal/archimedean term omitted?** It was not omitted: it was handled
  (constant $\omega$ slot, additive). But it must be stated plainly: **these objects
  have no gamma factor nor polar block** — their "archimedean term" is a negative
  constant realizing the diagonal atom and nothing more. That is internally
  consistent (the explicit formula of a Dirichlet polynomial is pure Poisson, no
  contour), and the paper admits it in B1/B3. It is not an error; it is the reason
  the theorem is easy (see §4).

### 1.3. Disjoint support and where the content really is

If $F$ is supported on $p^{\mathbb N}$, the triangular recursion of $F^{-1}$ only
involves divisors, so $F^{-1}$ and $DF$ and hence $L(F)$ live on
$p^{\mathbb N}$. Then $a_1+a_2$ lives on $p^{\mathbb N_{\ge1}}\sqcup
q^{\mathbb N_{\ge1}}$, disjoint by unique factorization: the Weil mass on
$\{p^aq^b:a,b\ge1\}$ is exactly zero. **Correct.** But note what was proved: that
the logarithmic derivative of a product is the sum of the logarithmic derivatives — i.e.
that the explicit formula of $E_1E_2$ is the sum of the explicit formulas. This is the
standard mechanism by which the explicit formula of $\zeta=\prod_p(1-p^{-s})^{-1}$
is a sum over primes. **There is no cancellation miracle: there is linearity.**
Doc 135 admits it ("trivial but structural", Prop. 1.2) while simultaneously selling it
as "the fear of cross terms, dissolved" — it is the latter that is excessive.

**Side checks performed and approved:** the Poisson Lemma (lem:poisson):
with $F(t)=f(e^t)e^{bt}e^{i\phi t/L_p}$, $\hat f(\rho_k)=\hat F(2\pi k/L_p)$ and classical
Poisson gives $\sum_k\hat F(2\pi k/L_p)=L_p\sum_mF(mL_p)=L_p\sum_m\beta^mf(p^m)$ ✓.
The mirror relation: $c_{-m}=\alpha^{-m}+(\bar\alpha/p)^m=\bar c_mp^{-m}$ ✓ (holds for
every $\alpha$, without purity). Hermiticity (Lemma 1.6 / lem:herm): the change $m\mapsto-m$
and $\bar c_{-m}p^m=c_m$ close ✓. Under purity $|\alpha|^2=p\Rightarrow
p/\bar\alpha=\alpha$, $c_m=2\alpha^m$, divisor with multiplicity 2 on
$\mathrm{Re}=\tfrac12$, and each term of $Q$ is $2|\hat F(\xi)|^2$ ✓.

---

## 2. Re-computation of the $p=2$, $q=3$ toy example, in closed form

All re-derived by hand from $g=f\star\tilde f$, $g(x)=\int f(xz)\overline{f(z)}\,z\,d^*z$.

### 2.1. The values of $g$ (taking nothing from the document)

With $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$: $\|u\|_w^2=1+O(\epsilon)$;
$\|u(\cdot/p^M)\|_w^2=p^M(1+O(\epsilon))$ (substitution $x=p^My$). For
$f=u-t_1u(\cdot/2^M)-t_2u(\cdot/3^N)$:
$g(1)=\|f\|_w^2=1+t_1^22^M+t_2^23^N$, $g(2^M)=-t_1$, $g(3^N)=-t_2$,
$g(2^{-M})=-t_12^M$, $g(3^{-N})=-t_23^N$ (all $\times(1+O(\epsilon))$). ✓ Matches.

### 2.2. The functional and the mirrors

$W_X(g)$: diagonal $2(\log2+\log3)g(1)=2\log6\,g(1)$. Terms $m=\pm M$:
$L_2[c_Mg(2^M)+c_{-M}g(2^{-M})]=L_2(-t_1)[2\cdot2^{M/2}+2\cdot2^{-M/2}\cdot2^M]
=-4\log2\cdot2^{M/2}t_1$. Same for $q$. Hence
$$\tfrac12Q_X=\log6\,(1+2^Mt_1^2+3^Nt_2^2)-2\log2\cdot2^{M/2}t_1-2\log3\cdot3^{N/2}t_2.$$
✓ Identical to 6.3 of the document and §4.3(3) of the paper.

### 2.3. The minima

- $t_1^*=\tfrac{\log2}{\log6}2^{-M/2}$, $t_2^*=\tfrac{\log3}{\log6}3^{-N/2}$ ✓
  (independent of $M,N$ in value).
- Single test (6.1): $\log6-(\log2)^2/\log6=1.52361\ldots$ ✓ (recomputed:
  $1.791759-0.480453/1.791759$).
- Double test (6.3): $\log6-\tfrac{(\log2)^2+(\log3)^2}{\log6}
  =\tfrac{(\log6)^2-(\log2)^2-(\log3)^2}{\log6}=\tfrac{2\log2\log3}{\log6}$, hence
  $\min Q_X=\tfrac{4\log2\log3}{\log2+\log3}=1.70005\ldots$ ✓. Twice the harmonic
  mean ✓. Identity $(\sum L_i)^2-\sum L_i^2=2\sum_{i<j}L_iL_j$ ✓; the single-prime
  check gives margin $0$ = perfect square $Q_{F_2}=2\log2(1-2^{M/2}t)^2$ ✓
  (re-derived: $\log2[2(1+2^Mt^2)-4\cdot2^{M/2}t]$).
- Rescue of the critical direction (6.2): at $t=2^{-M/2}$, $Q_{F_3}=2\log3\cdot
  g(1)\cdot c_0'/2\cdot\ldots$ — clean: $L_3c'_0g(1)=\log3\cdot2\cdot2=4\log3$ ✓.
- Mixed adversary (6.4): $2^3\cdot3^{-2}=8/9$, $\log(8/9)=-0.1178$ ✓; no $2^m,3^n$
  ($m,n\ne0$) falls in $\{0,\pm\log(8/9)\}+[-2\epsilon,2\epsilon]$ for
  $\epsilon<\tfrac14|\log(8/9)|$ ✓.

### 2.4. ATTACK: is that minimum "the minimum", and is it uniform?

Two observations that a hasty reader may misread, even though the text does not lie:

1. **The 1.700 is NOT a spectral gap.** It is the minimum over the 2-parameter Mertens
   family with normalization "first bump = 1" — not with
   $\|f\|_w=1$. The infimum of $Q_X$ over $\|f\|_w=1$ on long windows is **zero**
   (infinite-dimensional kernel, Theorem 5.4(b) of the document itself). In the
   normalization $\|f\|_w=1$, the value at the optimum is $Q/\|f\|_w^2=1.700/1.5256=1.114$, and
   taking the family with $M,N$ such that the window exceeds $\log6$ it can be pushed
   toward $0$ with other tests. P48's abstract says "adversarial Mertens test;
   minimum $\approx1.700$" — defensible, but the sentence in Doc 135 §0 ("the margin is
   twice the harmonic mean…, uniform in the heights") invites reading a gap that does not
   exist. Recommendation: an explicit sentence "minimum over the Mertens family, not a
   gap in the $\|\cdot\|_w$ norm" next to the boxed result.
2. **Uniformity in $M,N$ is real, but $\epsilon$ is not uniform:** the separation
   $\min_{n}||n|L_3-ML_2|$ decreases polynomially in $M$ (Baker), so
   $\epsilon=\epsilon(M,N)$ must shrink. Since $\epsilon$ is chosen per test and the
   limiting value does not depend on $\epsilon$, the bound is correct as an infimum; no
   error, but the dependence $\epsilon(M,N)$ should be stated (it is stated in §4 of the
   document; in §6 it is tacitly inherited).

**The class of tests is correct** (complex $C_c^\infty(G)$, form
$Q(f,f)=W(f\star\tilde f)$, hermitian by Lemma 1.6): it matches that of the standard
Weil criterion. No class trick.

---

## 3. Audit of additivity (Theorem 7.1)

### 3.1. Consecutive pairs or all pairs?

There is no induction to audit in (a): $Q_{X_S}=\sum_iQ_{F_{p_i}}$ is **linear $n$-ary**
(iterated Prop. 1.2; $\star$ associative by construction on the slots
$(a,c,\omega)$, and the additivity of $L$ holds for arbitrary finite products). The
cross terms of **each** pair are zero by the same support argument (the supports
$p_i^{\mathbb N_{\ge1}}$ are pairwise disjoint by unique factorization). No order and
no step $n\to n+1$ is used. **Correct** — and the document itself underlines it
("the step $n\to n+1$ uses nothing about $n$"), which is the key admission for §4.

### 3.2. Does the test class shrink as primes are added?

In (a), no: positivity holds over all of $C_c^\infty(G)$, for every $n$. In (b)
(the converse), the test depends on $n$ only via $\epsilon$: the separation
"$p_i^m\ne$ product of powers of the others" involves finitely many candidates and the
bound $|c_M^{(i)}|>2p_i^{M/2}(\sum_jL_{p_j})/L_{p_i}$ is exceeded because the Ramanujan
violation grows geometrically in $M$ while the barrier is constant in $M$.
Re-derived from the two-prime case (recomputed in §1.3: minimum
$(L_p+L_q)-L_p^2|c_M|^2/(4(L_p+L_q)p^M)<0\iff|c_M|>2p^{M/2}(1+L_q/L_p)$ ✓; the
generalization replaces $L_p+L_q\rightsquigarrow\sum_jL_{p_j}$ ✓). **Correct.**

### 3.3. (c) and (d), verified

(c) The Jensen argument: exponential type $\le T$ + zeros in $n$ progressions of
total density $(\sum L_i)/\pi$ forces $\sum L_i\le2T$ — constant
$\tfrac1{2\pi}\int_0^{2\pi}|\sin\vartheta|d\vartheta=\tfrac2\pi$ ✓, count per
progression $\ge rL_i/\pi-2$ ✓, overlap $\le$ one point per pair (Lemma 1.7) — for
$n$ progressions the total overlap is $O_n(1)$, absorbed in $C_0$ ✓. The
construction of the kernel $F=D_{p_1}\cdots D_{p_n}g$: support
$|\mathrm{supp}\,g|+\sum L_i\le2T$ ✓, $F\ne0$ because the extreme translate
$g(\cdot-\sum L_i)$ is at distance $\ge\min_iL_i$ > width of $g$ from its neighbors ✓.
(d) is §2.3 with $n$ summands ✓.

**Conclusion of front 3: additivity is unassailable precisely because it asserts
nothing nonlinear.** The $n$-prime theorem is $n$ copies of the one-prime theorem
(Doc 131, Thm. 6.7) glued by linearity. This shifts the entire weight onto the
question of novelty.

---

## 4. Novelty vs. literature: the attack that does connect

### 4.1. What Theorem A really is

Stripped of the $\mathcal Arith$ category: let
$E_S(s)=\prod_{i}(1-\alpha_ip_i^{-s})(1-(p_i/\bar\alpha_i)p_i^{-s})$, a finite
**Dirichlet polynomial**. Its explicit formula (Poisson, no analytic continuation, no
contour, no gamma) says $\sum_{\rho:E_S(\rho)=0}\hat f(\rho)=W_{X_S}(f)$. Theorem A
says: if all zeros of $E_S$ are on $\mathrm{Re}=\tfrac12$ (which is EXACTLY the purity
hypothesis $|\alpha_i|=\sqrt{p_i}$ — purity is not a deep arithmetic condition here: it is
placing the zeros on the line by fiat), then
$Q(f,f)=\sum_\rho|\hat f(\rho)|^2\ge0$.

This is the **trivial direction of Weil's criterion**: "zeros on the line $\Rightarrow$
term-by-term positivity" — the mechanism is in Weil 1952 and explicit in
Bombieri 2000 (the form $\sum_\rho m_\rho\hat f(\rho)\overline{\hat f(1-\bar\rho)}$ is a
sum of squared moduli when $\mathrm{Re}\,\rho=\tfrac12$; cf. also Doc 131,
Prop. 6.2, which is the same observation in categorical form, and which Theorem 3.1
**cites as its final step**). The only other piece is §1: the explicit formula of a
product is the sum of the explicit formulas — the additivity of
$-\tfrac{d}{ds}\log$, classical since Euler.

### 4.2. The known case in disguise

A pure factor $(1-\alpha p^{-s})(1-\bar\alpha p^{-s})$ with $|\alpha|=\sqrt p$ and
$\alpha+\bar\alpha\in\mathbb Z$ is the numerator of the zeta function of an elliptic
curve over $\mathbb F_p$ (in general, weight-1 Frobenius factors where local RH
**is** Hasse–Weil). The positivity of the explicit formula for zeta functions
of function fields — where RH is a theorem — is exactly the setting of Weil's own
1952 paper (which treats the function-field case alongside the number-field one). The
"$n$-prime object" is a product of such factors for distinct primes, and its
positivity is the sum of the local positivities. **Nobody published
"Weil positivity for finite systems of primes" as a theorem because it is a corollary of
one line of the explicit formula for Dirichlet polynomials with zeros on the
line.** The frank comparison:

- *vs. positivity for finite-degree L-functions with known RH* (function
  fields, Weil 1952): it is that result, restricted to products of local
  factors, repackaged.
- *vs. truncated explicit formulas / Bombieri 2000*: Bombieri analyzes the Weil
  quadratic form of $\zeta$ (destructive regime, $a=\Lambda\ge0$, with polar and
  gamma); P48 lives in the constructive regime without polar or gamma — the regime
  where there is nothing to prove once the zeros are on the line. P48 admits this in B3.
- *vs. Bombieri–Lagarias / Li / Coffey*: does not directly apply (Li's criterion =
  positivity of $\lambda_n$ for $\zeta$; here there is no $\zeta$); no overlap,
  but no novelty rescue from that side either.
- *vs. Fejér / trigonometric positivity*: Theorem B's Mertens test is
  literally the mechanism $3+4\cos\theta+\cos2\theta$ (the paper cites it, MV 2007);
  the converse "impure $\Rightarrow\neg H$" is the local version of the classical
  argument that positivity fails with zeros off the line, already present as
  Theorem 6.7 of Doc 131 for one prime. The only new piece of Theorem B is the barrier
  shift $2p^{M/2}\to2p^{M/2}(1+L_q/L_p)$: correct, elementary, and of minor interest.

### 4.3. The internal framing contradiction (this must be corrected)

Observation 2.2 of Doc 135 justifies novelty thus: "it is not a lattice… neither
Theorem 4.4(c) nor 6.7 decide H. **That is why this theorem is new**." But
Observation 3.2 (and Remark 2.7 of the paper) confesses: "the incommensurability of
$\log p$ and $\log q$ **is not used** in Theorem 3.1 (it holds just the same for $q=p$!)".
Both cannot support the same thesis: if positivity is linear in the divisor and
term by term, the "non-lattice territory" is never actually entered for the sign — the
difficulty invoked by Obs. 2.2 as a source of novelty is exactly the one the
proof evades by linearity. The abstract's claim ("the first unconditional
Weil-positivity theorem… genuinely off the lattice") inherits this problem: the theorem
does not overcome the non-periodic regime; it goes around it. **The priority
claim must be withdrawn or downgraded to "first explicit formulation in this category".**

### 4.4. What does have substance (and remains open or is standard-adjacent)

- **Theorem 5.4 (kernel threshold $\log(p_1\cdots p_n)$):** correct (re-derived).
  But it is, in harmonic-analysis language, the completeness/sampling
  statement for the union of $n$ arithmetic progressions in
  $L^2$ of an interval: Beurling density > type $\Rightarrow$ uniqueness — standard
  technique (Boas/Levinson; the document cites Boas 1954 correctly). The arithmetic
  formulation ("the threshold is the logarithm of the naive conductor") is elegant and
  possibly the citable observation of the paper.
- **GAP-135.A (lower frame bound for
  $\{e^{i\xi t}\}_{\xi\in\Lambda_p\cup\Lambda_q}$, intermediate region):** this is the
  only genuinely hard question of the document, and it is **declared open**.
  Adversarial note: unions of incommensurable progressions and their frame/sampling
  properties are actively studied territory (Seip; Olevskii–Ulanovskii,
  universal sampling; Lyubarskii–Seip on complete interpolating sequences); before
  investing in GAP-135.A, review that literature — it is plausible that the answer (or
  a counterexample with generic phases) already exists in the form of a frame theorem.
- **B1–B4:** well stated and frank; B2 (positivity passes to the limit,
  spectrality does not) and B3 (the factors of $\zeta$ are maximally impure:
  $c_m=1+p^m$; the symmetry of $\zeta$ is global) are correct and are precisely the
  admission that the finite theorem lives in the regime where there is no obstacle. B1–B4
  do not hide triviality: **they expose it** — the problem is that the title and abstract
  do not expose it with the same clarity.

### 4.5. On "H ⟺ bilateral purity" (Cor. 4.2)

Correct and verified, but it must be stated what it is: purity IS "zeros on the
line" for these objects, so the corollary says "the Weil form of the object is
PSD ⟺ its zeros are on the line" — the Weil equivalence for objects where both
directions are elementary. The nontrivial direction of the Weil equivalence for
$\zeta$ (positivity $\Rightarrow$ RH) requires the contour and the continuation; here the
converse is done with a two-bump test because the object is a polynomial.
Decidability ≠ depth.

---

## 5. Errata and corrections required in P48 / Doc 135

No substantive mathematical error. Errata and scope corrections, in order of
importance:

1. **[P48, §6 (B3) — out-of-scope citation]** B3 claims "each factor of $\zeta$ …
   violates $H$ (Theorem~\ref{thm:local})", with $\alpha=1$, $|\alpha|=1$. But
   thm:local is stated for $1<|\alpha|<p$; $|\alpha|=1$ is **outside the range**
   (same as $|\alpha|=p$, its mirror). The Mertens test proof extends without
   changes to $|c_M|=1+p^M>2p^{M/2}\cdot(\text{barrier})$, but as written
   the citation is invalid. Minimal correction: extend thm:local/Theorem 4.1 to
   $1\le|\alpha|\le p$ (the proof already covers it with $\delta'=\pm\tfrac12$) or add a
   line in B3. The same applies to Doc 135 §7.2 B3 (cites Doc 131 Thm. 6.7, same range).
2. **[Doc 135, Theorem 5.4(b) — corrupted width condition]** "bump of width
   $0<\,2T-\log pq\,<\min(2T-\log pq,\,L_p)$" is incoherent (a number cannot be less
   than the minimum of itself). It should read: width $w$ with $0<w<\min(2T-\log pq,\,L_p)$.
   The paper (thm:thresh(b)) already has it right; fix the document.
3. **[Doc 135, §6.1 — garbled line]** "only gives $\tfrac12Q=\log2\,(1-2^{M/2}t)^2\cdot
   \tfrac{2}{2}$ — more precisely…": the factor $\cdot\tfrac22$ is typographical noise;
   the final formula $Q_{F_2}=2\log2(1-2^{M/2}t)^2$ is correct (re-verified).
   Delete the first half of the sentence.
4. **[P48, Lemma 3.4 (lem:herm) — garbled algebraic chain]** The line
   "$\bar c_{-m}p^m=\overline{(\bar c_m p^{-m})}\,p^m\cdot p^{-m}\cdot p^{m}=c_m$"
   contains spurious factors $p^{-m}\cdot p^m$. The correct chain:
   $c_{-m}=\bar c_mp^{-m}\Rightarrow\bar c_{-m}=c_mp^{-m}\Rightarrow\bar c_{-m}p^m=c_m$.
   The result is correct; the display is not.
5. **[Framing, P48 abstract + Doc 135 Obs. 2.2 — novelty claim]** Withdraw or
   downgrade "the first unconditional Weil-positivity theorem for a finite system of
   distinct primes with incommensurable periods": (i) it contradicts the document's own
   Obs. 3.2/Remark 2.7 (incommensurability is not used in the positivity); (ii) the
   content is the trivial direction of Weil's criterion for Dirichlet polynomials
   with zeros on the line + additivity of logarithmic derivatives, both classical
   (Weil 1952; Bombieri 2000); (iii) the "local purity" version for one prime was
   already Doc 131 Thm. 6.7, and the step to $n$ primes is linear. Suggested
   reformulation: "an explicit categorical formulation, with quantitative fine
   structure (kernel threshold, short-window gap) that we did not find stated in the
   literature" — defensible; "first positivity theorem" is not.
6. **[Doc 135 §0.6 / §6.3 — label of the minimum]** Add next to the boxed result:
   "minimum over the Mertens family (first-bump normalization), not a spectral
   gap; the infimum of $Q_X$ at $\|f\|_w=1$ over long windows is $0$
   (Thm. 5.4(b))". Avoids the gap-misreading that the W_λ≥0 precedent teaches to fear.
7. **[Minor, document/paper consistency]** Doc 135 proves H₂ (Theorem 3.1, via Doc 131
   Thm. 4.9); the paper omits H₂ entirely. A legitimate decision (self-containment), but
   the program's summary should not cite "P48 proves H and H₂": H₂ is only in the
   document, conditional on Doc 131.

**No findings:** signs (all re-derived: mirrors $c_{-m}=\bar c_mp^{-m}$,
Mertens barrier, toy minima, Parseval of the periodization with its constant
$L_r$, Jensen count with $\tfrac2\pi$); document/paper normalizations (identical:
$\hat f(\tfrac12+i\xi)=\hat F(\xi)$, $\|f\|_w^2=\|F\|_2^2$, $W$ and $c_m$ match);
test class (standard, no shrinkage); convergences (Paley–Wiener vs linear
density, correct).

---

## 6. Conclusion

The theorem survives as mathematics: the sign error sought was not found, and the
search followed the trail the precedent (Doc 63 §7.1) teaches to follow — mirrors, Abel
summations implicit in the weights $c_{-m}p^m$, double counts of the diagonal atom. No such
error exists: the structure is too linear to hide one. That same linearity is the
verdict on novelty: **the theorem is correct because it asserts nothing beyond
the sum of local positivities term by term over a divisor placed on the
line by hypothesis.** The document's real value lies in what it declares it does not know
(GAP-135.A, GAP-135.B/Doc 136) and in the frankness of B1–B4 — which should be promoted
from "scope section" to the paper's thesis, with the priority claim withdrawn.

*End of Document 138.*
