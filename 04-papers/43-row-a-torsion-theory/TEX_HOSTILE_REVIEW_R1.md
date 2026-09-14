# Hostile referee report, round 1 — `main.tex`

Paper: *A Correspondence Algebra with a Canonical Trace on the Idele Class
Group, its Tate Symbol and its Numerical Form*.
Files examined: `main.tex` (4107 lines), `main.md` (5473 lines),
`TEX_CONVERSION_NOTES.md`, `../42-arithmetic-lefschetz-programme/main.tex`.
`main.tex` was not modified.

---

## 0. Summary of the audit

* **Forbidden vocabulary: clean.** No genuine hit. See §1.
* **Compilation: clean.** No errors, no undefined refs/citations, 51 pages,
  4 overfull boxes. See §4.
* **Proof coverage: structurally complete.** Every one of the 62
  theorem/proposition/lemma/corollary environments is followed by a `proof`
  environment; the only unproved environments are the two that are declared as
  such (Hypothesis 3.1, Convention 6.10) and the definitions. See §2.
* **But**: several *displayed inputs and intermediate assertions inside those
  proofs* are neither proved nor citable to the literature. One block of them
  (§3.2) carries the whole excision section. This is the reason the verdict is
  not an accept.
* **One theorem that the Markdown proves is omitted from the tex on a factually
  false ground** (Theorem 8A.12 *does* exist in `main.md`). See §3.

---

## 1. Forbidden vocabulary (BLOCKING class — none found)

Grep over `main.tex` for `riemann hypothes`, `\bRH\b`, `critical line`,
`phase`, `row`, `round`, `builder`, `auditor`, `lead `, `label`, `honest`,
`candidly`, `PROVED`, `P1[0-9][0-9]`, `106_1`, `programme`, `corpus`,
`repositor`, `of record`, `ledger`, `withdrawn`, `acceptance`, `contract`,
`status`, `clause`, `verificat`, after excluding `\label{`/`\ref{}`:

* **F1.1 (no defect).** All surviving hits are genuine mathematics:
  `label` = the lattice/gauge label of an elementary tensor (ll. 592, 840,
  1076, 1097–1101, 2551–2552, 3093, 3133); `row` = *row measure* of a kernel
  (ll. 3086, 3100–3102, 3135); `contraction`/`contractible`/`contractivity`
  (ll. 828–1006, 3206); `proved` in ordinary mathematical prose
  (ll. 615, 1370, 1933, 2475, 3238, 3330, 3354, 3460).
* **F1.2 (no defect).** "Riemann" occurs only in *Riemann–Roch*,
  *Riemann–Lebesgue*, *Riemann–Stieltjes*, *Riemann–von Mangoldt* is absent.
  There is no occurrence of "hypothesis" other than the declared
  `Hypothesis 3.1` and ordinary "the hypothesis of (b)".
* **F1.3 (no defect).** Abstract, introduction, §14 and §15 read as
  mathematics throughout. No meta-commentary about the writing, no
  self-assessment, no AI-flavoured prose. The self-limiting remarks that
  remain (Remarks 14.2, 14.3, 14.4, 12.7, 8.19, 13.8, and the sentence after
  Theorem 11.4) are all *mathematical* scope statements of the kind a careful
  author writes, and they are appropriate.

Verdict on item 1: **pass, no findings.**

---

## 2. Completeness of proofs

### 2.1 BLOCKING

**B1. §3.2, lines 307–322: the entire excision section rests on four
displayed/asserted facts that are neither proved nor cited.**

> `Each $I_J$ is relatively projective on each side through the summable
> adapted partition $h_J(a)=\sum_i e_i\otimes\rho_i a$ built from shell
> idempotents … and
> $I_J\,\widehat\otimes^{\mathbf L}_U\,I_K\cong I_{J\cup K}[0]$.` (3.6)
> `Then $B_O$ has the finite Čech resolution with terms $P_O^{-n}=\dots$, and
> $I_{J_T}\widehat\otimes_U B_O=0$, $B_O\widehat\otimes^{\mathbf L}_U B_O\cong
> B_O$.` (3.7)

Nothing in the article proves (i) relative projectivity of $I_J$ on each side,
(ii) the summability of the adapted partition, (iii) the ideal product formula
(3.6), (iv) exactness of the Čech resolution and the two vanishings (3.7).
There is no citation attached to any of them. Theorem 3.5, Lemma 3.6 and
Theorem 3.7 (two-sided excision) are *all* derived from them — Lemma 3.6's
proof cites "(3.6) and the adapted partition" verbatim.

In `main.md` §4 (ll. 665–680) these four facts are attributed to internal notes
`P123.124 (2)–(7)` and `P123.125 (2)–(4)`, i.e. exactly the kind of source the
conversion was instructed not to rely on. The converter's notes do **not** list
this among the seven flagged items, so it was shipped silently.

*Effect.* Section 3 — advertised in the abstract ("we prove two-sided excision
for it") and as one of the four headline results — is not self-contained. An
outside reader cannot check Theorem 3.7.

*Concrete fix.* Either (a) write out the four facts as a lemma with proof
(they are elementary for the shell-idempotent partition: state $h_J$
explicitly, prove $b'h+hb'=\mathrm{id}$ with the seminorm estimate as in
Lemma 5.1, prove $I_J\cdot I_K=I_{J\cup K}$ with continuous splitting, and
deduce the Čech vanishing from $I_{J_a}B_O=0$), or (b) demote Theorem 3.7 to a
conditional statement listing (3.6)–(3.7) as hypotheses, as was correctly done
for Hypothesis 3.1. Option (a) is strongly preferred; the material is not deep,
and it is one page.

---

### 2.2 MAJOR

**M1. Theorem 5.8(a), lines 752–758: the collapse of the group factors is
asserted, not proved, and has no citation.**

> `On the piece with label $\gamma$, the standard collapse of the group
> factors onto one $U_{\gamma}$ leaves the coefficient complex twisted by
> $\gamma w$, tensored with the group homology of $\Gamma_S$ … The collapse is
> continuous because it is built from the crossed product comparison maps,
> which are finite signed sums of multiplications and gauge translations in
> each degree.`

Two distinct gaps. (i) The *existence* of the collapse — i.e. the
decomposition of the (twisted) Hochschild complex of a crossed product
$E_P\rtimes\Gamma_S$ over the conjugacy classes of $\Gamma_S$, with
coefficient complex $\otimes$ group homology — is a real theorem and is
nowhere proved here; the word "standard" is doing all the work. (ii) The
continuity step is explicitly asserted with a reason rather than proved (this
is the converter's flagged item 3, and the flag is accurate).

In `main.md` (l. 922) the continuity is `P123.123 (8)–(11)` and the collapse is
`P123.121` — repository notes. So *nothing citable backs either half*.
Theorem 5.8 is the whole content of §5, and Corollary 5.10 and Proposition
13.10 depend on it.

*Fix.* Cite the literature for the crossed-product Hochschild decomposition —
for a commutative algebra with a group acting, Brylinski, *A differential
complex for Poisson manifolds*; Nistor, *Group cohomology and the cyclic
cohomology of crossed products*, Invent. Math. 99 (1990); or Getzler–Jones,
*The cyclic homology of crossed product algebras*, J. reine angew. Math. 445
(1993) — and state precisely which continuity hypothesis carries it into the
complete-Fréchet setting, or prove the Koszul collapse by hand for
$\Gamma_S\cong\Z^{d}$ (it is a finite Koszul complex; this is feasible).

**M2. Lemma 5.6 and Theorem 5.8(c): the untwisted higher vanishing for a shell
algebra is asserted twice, with two different unproved phrasings, and used in
both directions.**

> l. 700: `The untwisted contraction, which proves $H_n(F)=0$ for $n\ge1$ for
> this algebra, is diagonal in the character basis`
> l. 772: `whose Hochschild homology vanishes in positive degrees by a
> continuous character-diagonal homotopy`

Neither passage exhibits the homotopy. `main.md` (l. 949) sources it to
`P123.118` ("the continuous homotopies of P123.118"), a repository note.

The statement is true and provable — $C(\Z_p^\times)$ with rapid conductor
weights is a topological inductive limit of the finite-dimensional separable
commutative algebras $C(\Z_p^\times/(1+p^N\Z_p))\cong\C^{M_N}$, and a
separable algebra has vanishing Hochschild homology in positive degrees — but
it must be written, with the seminorm control that makes the limit homotopy
continuous.

*Fix.* Add a lemma: "$F^{(j)}$ is the projective limit / inductive limit of
finite products of $\C$; the separability idempotent
$e=\sum_{\kappa}\,\ldots$ gives a continuous contracting homotopy in positive
degrees with the seminorm shift of \eqref{eq:seminorms}", with proof. Then
Lemma 5.6 and Theorem 5.8(c) both cite it rather than each other.

**M3. Lines 596–601: Wodzicki excision is invoked in a twisted, topological
form with no pinpoint citation and with the hard step waved through.**

> `By Wodzicki's excision theorem \cite{Wodzicki}, in its topological form for
> Fréchet algebras with continuous H-unitality \cite{MeyerCyclic,CuntzQuillen},
> there is a distinguished triangle … the twisted case is identical because the
> proof uses only the bar complex of the ideal.`

`\cite{Wodzicki}` is purely algebraic; the topological statement is attributed
to two book-length/40-page references with no section or theorem number; and
the extension to *twisted* coefficients is asserted in one clause. Theorem 5.3
(Künneth over places), hence all of §5, depends on this.

*Fix.* Give the pinpoint (Meyer, *Local and Analytic Cyclic Homology*, Thm.
and § number; Cuntz–Quillen 1997, Thm. numbers), and either prove the twisted
variant (the argument really is the bar-complex one, but write it) or state it
as the imported theorem it is, with its hypotheses checked against §2.2.

**M4. Line 390 and Proposition 4.1: $\Hom_{U\text{-}U}(U,N)=0$ is asserted
unconditionally, on the same input the paper declares unverified.**

> `A bimodule map out of $U$ is multiplication by a central element of $U$;
> the freeness of the lattice action on the open stratum kills all nonidentity
> labels, and an invariant identity coefficient must vanish by exponential
> decay along an orbit. Hence $\Hom_{U\text{-}U}(U,N)=0$ …`

This is a two-line sketch, not a proof; it uses "freeness of the lattice
action" — which §3.1 (ll. 219–221) explicitly says is *"the point we do not
verify"* for the coefficient algebra \eqref{eq:coeff}; and it is stated as a
fact in the running text, immediately before Proposition 4.1 whose statement
merely says what the vanishing *implies*. A reader will take the vanishing as
proved.

*Fix.* Either prove it (the argument through exponential decay of a
$\Gamma_S$-invariant coefficient is short and does not obviously need the
freeness claim that Hypothesis 3.1 needs — if so, say why), or make it part of
Hypothesis 3.1 and add it to the list of what the hypothesis supplies.

**M5. Lines 222–223: the claim that Hypothesis 3.1 "is used exactly twice" is
false.**

> `It is used exactly twice: in Proposition~\ref{prop:cat}(iv) and in
> Theorem~\ref{thm:daggerthm}.`

A third use is at line 412: `By \eqref{eq:homclass} the ideal $N$ is not an
object of $G$, so the obstruction does not apply to the category of
Definition~\ref{def:G}` — this is exactly how the paper disposes of the
self-duality obstruction, i.e. it is load-bearing for §4.

*Fix.* "It is used three times: Proposition 3.3(iv), the remark following
Proposition 4.1, and Theorem 4.3." (And re-examine M4 in the same sentence.)

**M6. Theorem 14.1(c): a Grothendieck-duality formula is asserted with no
proof and no pinpoint citation.**

> `On the classical side, for a finite morphism $f$ one has
> $D_h(\mathcal O_{\Gamma_f})=\sigma_{*}i_{f*}(h\otimes f^{*}h^{-1})$`

The only citation in the proof is a blanket `\cite{SGA6}` for "the standard
six-functor formalism" at the top. This displayed identity — which is the
entire content of part (c), one of the four claims of the comparison theorem —
is neither derived nor located.

*Fix.* Pinpoint the duality statement (SGA 6 or Conrad, *Grothendieck Duality
and Base Change*, with chapter/theorem), or derive it from
$f^{!}\mathcal O=\omega_f[\dim]$ for a finite flat morphism in two lines.

**M7. The archimedean closed form \eqref{eq:Winfclosed} is an import whose
citation is not precise enough for the quantitative use made of it.**

> l. 539: `The closed form \eqref{eq:Winfclosed} is the classical evaluation of
> the archimedean Weil distribution \cite{Weil1952,CCWeilArch}: the even part
> of \eqref{eq:Winfhat2} is, in Weil's normalization, the functional whose
> value on $e^{i\tau t}$ is $\log\pi-\Rel\,\psi(\tfrac14+\tfrac{i\tau}{2})$.`

Two references, no page, no equation, no theorem number, and the crucial
clause "in Weil's normalization" — i.e. the normalization match, which is
precisely where such comparisons go wrong — is asserted. This is honest about
being an import (the converter's flagged item 4 is accurate, and the
self-contained $-\log|\tau|+O(1)$ derivation above it is genuinely from
scratch and correct), but the closed form then carries:

* the explicit constant $\log\pi+\gamma+3\log2+\pi/2\approx5.372$ in
  Theorem 15.1(c) / \eqref{eq:mbound};
* the whole Mittag–Leffler expansion \eqref{eq:MLinf} of Theorem 7.4(b), hence
  7.4(c),(e) and \eqref{eq:residues}, hence Remark 13.5's second reason and
  the "forcing" narrative of Theorem 13.4.

So the paper's *quantitative* backbone at the archimedean place is imported on
a loose citation. Note also the unjustified monotonicity claim at l. 545,
`$\Rel\,\psi(\tfrac14+\tfrac{i\tau}{2})$ is increasing in $|\tau|$`, which is
what turns \eqref{eq:Winfclosed} into the *maximum* \eqref{eq:maxarch}.

*Fix.* Pinpoint the citation to the displayed formula (Connes–Consani,
Selecta Math. 27 (2021), §/eq. number is the right target), state the
normalization dictionary explicitly as a one-line lemma, and prove the
monotonicity (it is $\Rel\,\psi'(\tfrac14+\tfrac{i\tau}{2})\cdot$ sign, or
directly from the Gauss series already displayed in the proof of
Theorem 7.4(b) — that series makes it immediate, so the proof can simply be
reordered).

---

### 2.3 MINOR

**m1. Theorem 12.2(a), l. 3100–3103** — the converse uses `the
$\Gamma_S$-action being free there`. As written, a reader who has just read
§3.1's disclaimer about freeness will think this is the unverified input. It is
not: on the locus $x_\infty\ne0$, $\gamma x_\infty=x_\infty$ with
$\gamma\in\Q_{>0}$ forces $\gamma=1$, which is one line. *Fix:* add that line.
(The converter's flagged item 5 over-states the problem.)

**m2. Theorem 7.1, l. 361–364** — `a compactly supported smooth function on
$\R_{>0}$ may have prescribed Mellin values at two distinct points` is asserted.
One sentence on the linear independence of $t\mapsto e^{t/2}, e^{-t/2}$ as
functionals on $C_c^\infty$ would close it (the very argument is spelled out in
full in Theorem 13.9(c), l. 3593–3600 — cross-reference it).

**m3. Duplicate definition of $N$.** Lemma 8.12 \eqref{eq:Nsemi} and
Definition 10.1 \eqref{eq:trnorm} define the same functional twice, two
sections apart, with no cross-reference at the second. Merge, or say "with $N$
as in \eqref{eq:Nsemi}".

**m4. Theorem 13.7(f), l. 3405–3410.** The notation $L_S^{(q)}(F+G)$ is
undefined: $L_S^{(q)}$ was introduced as a *two-variable* line
$L_S^{(q)}(F,G)$. Also the proof's `The statement about the cross-effect is
the computation in (a)` is false — (a) contains no such computation. The
identity is correct ($B(F+G,F+G)-B(F,F)-B(G,G)=2\Rel B(F,G)$), but write it.

**m5. Theorem 15.2, Step 4, l. 3648.** The claim
`$|B(t)|\le C_{\psi}n^{-1}e^{-na}e^{-|t|}$` is stated for all $t$ but is only
valid for $t>0$; for $t<0$ the correct bound is
$|B(t)|\le C_{\psi}n^{-1}e^{-na}$. The two cases are then treated separately
and correctly, so no result is affected, but the display as written is wrong.
Also, $h'$ denotes *the profile of $H'$* while $(h')'$ denotes its derivative —
a needless collision; rename to $h_{\sharp}$ or $\eta$.

**m6. Theorem 13.9(c)** works with algebraic $\mathrm{Tor}$ and algebraic
$I^2$ over the topological algebra $\DA^{+}$. Correct as stated, but say so in
one clause, so that no reader assumes a completed tensor product.

**m7. Corollary 5.10** states a dichotomy ("constant … or undefined") whose
two cases are $v_p(w_p)\ne0$ and $w_p\in1+p\Z_p\setminus\{1\}$. Units outside
$1+p\Z_p$ are covered by neither, as Remark 5.7 itself observes. Add
"…and the remaining unit classes are not treated, by Remark 5.7."

**m8. Convention 6.10** says the value $c=0$ is used "namely in Theorem
13.7(f), Proposition 6.12 and Theorem 15.2". Proposition 6.12 states `Let
$c=0$` but its content — the identity
$\mathrm{rk}^{\mathrm{Haar}}\cdot w_p=\tau_p$ — is independent of $c$; only
the last display uses it. Harmless, but the list invites a reader to hunt for a
dependence that is not there.

**m9. Unused macros** `\Ltr`, `\dg`, `\Spec` are defined and never used; the
`example` environment is declared and never used. Cosmetic.

---

### 2.4 Items verified clean (no finding)

I checked the following from scratch and found them correct and complete as
written:

* **The densities $\tau_v$** — Lemma 6.2(i),(ii) and the cutoff-trace identity;
  Lemma 6.4 ($\tau_v(x^{-1})=\tau_v(x)$); the archimedean forms
  \eqref{eq:tauinf}; the folding factor $\tfrac12$ of \eqref{eq:archmeasure}
  and its consistency with \eqref{eq:Winf}. **Correct.**
* **The trace $T$** — Definition 6.5; Theorem 6.6 (absolute convergence off
  the identity, with all three counterterms shown to drop); Theorem 6.7
  (uniqueness, with the finite-order hypothesis stated where it is needed).
  **Correct and complete.**
* **The identity $c=0$** — Convention 6.10 is a *declaration*, correctly
  labelled as such, and the paper is explicit that all results hold for
  arbitrary $c$ except the three named. No circularity. **Correct.**
* **Proposition 6.8** carries the cutoff asymptotic \eqref{eq:cutoff} as an
  explicit hypothesis, and the sentence after it states that nothing depends on
  it. Flagged item 7 is handled correctly. **No defect.**
* **Theorem 6.11 (separation)** — the membership argument, the vanishing of
  $W_\infty$ and of $W_q$ ($q\ne p$) via the $\theta<q^{1/2}$ support
  condition, the constancy of $|1-w|_p^{-1}=p^{j}$ on the coset, and the
  equality of the Tate values. **Fully verified, correct, and regularization
  free.** This is the strongest piece of the paper.
* **The symbol, Theorem 7.2** — the shell sum
  $2\Rel(\zeta/(1-\zeta))$; the conductor identity \eqref{eq:conductor}
  (verified line by line, the telescoping $A_n-A_{n+1}$ and the collapse to
  $-1-(c-1)=-c$ are right); the evaluation $\pi/\cosh(\pi\tau)$ of the even
  $\mathrm{sech}$ transform; the $\mathrm{Cin}$ computation and the
  bookkeeping of the two factors $\tfrac12$ (they are *not* applied twice —
  I checked); part (d)'s termwise interchange with its three explicit
  dominations. **Correct**, modulo M7 for \eqref{eq:Winfclosed}.
* **Theorem 7.4 (Mittag–Leffler, Tate poles, contour identities)** — the
  two-exponential rewriting \eqref{eq:twoexp}; the $\coth$ expansion; the
  index bookkeeping $\tilde w-2\pi ik=iL(\tau-\tau_k^{+})$ and
  $w-2\pi ik=-iL(\tau-\tau_{-k}^{-})$ and the symmetric re-indexing; the Gauss
  series manipulation in (b); the rectangle-contour argument in (d) with the
  periodicity bound on the vertical sides and the Paley–Wiener decay; the
  Poisson step \eqref{eq:poisson}. **All correct.** Remark 7.5's restriction
  of (b),(d),(e) to the even component is stated, which is the right
  disclosure.
* **The Tate symbol $\widehat T$ and $\Nrad=0$ (Theorem 8.4)** — the density
  of $\{\widehat g:g\in C_c^\infty\}$ in Schwartz space, the tempered-product
  argument, and the isolated-zero step from Theorem 7.2(c). **Correct**, and
  the following Remark correctly identifies the three and only three
  properties used.
* **What exactly vanishes, and where.** Theorem 8.4 asserts $\Nrad=0$ *on
  $\DA$ at a fixed finite chart*; the sentence at l. 3395–3398 explicitly
  declines the colimit statement. This matches `main.md` (ll. 555, 5016–5017).
  **Correctly scoped.**
* **The Tate sequence and the rulings** — Theorem 8.8 (including the
  codimension-two/boundedness-on-translates argument for nondegeneracy on the
  kernel), Theorem 8.9(a) (on-axis vs off-axis, with the translation
  argument), Lemma 8.12, Theorem 8.13 (all of (a)–(e), the exact values
  $\lambda_+(F_n)=1$ and the bounds), Theorem 8.14 (canonical splitting, no
  choices), Theorem 8.15, Definition 8.16 and Theorem 8.17.
  **All verified correct.** Remarks 8.18 and 8.19 correctly forestall the two
  obvious objections (no extension of $I_A$ to the completion is claimed; no
  contradiction with 8.9(a)).
* **Effectivity §12** — Theorem 12.2, Proposition 12.3, Theorems 12.4, 12.5
  (the three-step argument through the positive quadrant and
  $\lVert F\rVert_{L^1}\le\tfrac12(\lambda_++\lambda_-)$ is clean), 12.6.
  **Correct.** The definitional treatment of the $E_F$ coefficients
  (converter's flagged item 6) is handled exactly as claimed: the coefficient
  statement is definitional in the fixed trivialization, and Proposition 9.3
  supplies a second, independent operator-theoretic proof of injectivity.
  **No defect.**
* **Riemann–Roch §13** — Lemma 13.2, Theorem 13.4, Theorem 13.7(a)–(g) and
  Theorem 13.9 base change (the $\mathrm{Tor}_1\cong I/I^2$ computation and
  the surjection onto $\C^2$ via the four independent functionals
  $e^{\pm t/2},te^{\pm t/2}$). **Correct.** Remark 13.8 is unusually candid
  about how much of Theorem 13.7(e) is definitional — this is a virtue, and it
  should be kept.
* **Signature, Theorem 15.1** — the concentration argument is the right one
  (the paper explicitly notes that $\widehat\varphi$ is never compactly
  supported, and builds the *weighted* tail estimate
  \eqref{eq:weightedtail} that the argument actually needs); the diagonal
  dominance bookkeeping with the inductive choice of $\delta_j$ is sound; (b)
  and (c) check out numerically. **Correct**, modulo M7 for the constant.
* **Mertens limit, Theorem 15.2** — Steps 0–3 verified in full, including the
  reduction to $\sum_N\Lambda(N)N^{-1}\phi_{n,m}(\log N)$, the partial
  summation with $-\int t\phi'=\int\phi=1$, and the exponentially small
  archimedean term. **Correct**, modulo m5. The theorem is correctly flagged
  at l. 3534–3536 as used nowhere else.
* **Hochschild computations the converter says it wrote out in full**:
  Lemma 5.1 (H-unitality), Theorem 5.2 (split augmented excision — the
  $P\oplus Q$ decomposition, the identification of $P_\bullet$ with $B'(I)$
  and of $\bar C$ with $\mathrm{Cone}(\phi)$, the degree-zero splitting, and
  the explicit cone-contraction inverse $(x,y)\mapsto y-\phi(hx)$), Theorem 5.3
  Step 1 (Eilenberg–Zilber/Alexander–Whitney with the continuity argument) and
  Step 2 (the filtration of $\widehat\bigotimes E_v^{+}$), Lemmas 5.4 and 5.5,
  and the $\HH_0$ half of Lemma 5.6 (including the lower bound
  $|1-\kappa(u)|\ge cp^{-(m-k)}$ that makes the division continuous).
  **These are genuinely written out and are correct.** The gaps are M2 (the
  positive-degree untwisted vanishing) and M3 (excision), not these.
* **Theorem 8A.12 dependence.** I confirmed by grep that no statement in the
  tex asserts closure of the correspondence category under the analytic
  completion: `E_H`, `\lambda(H)` and any "closed under the analytic
  completion" phrasing are absent, and §10 constructs $\Atr$ as a Banach
  algebra only. The *tex* is therefore internally safe on this point — but see
  D1 below.

---

## 3. Fidelity to `main.md`

**D1 (MAJOR). Theorem 8A.12 *is* stated and proved in `main.md`, and it is
omitted from the tex on a stated ground that is false.**

`TEX_CONVERSION_NOTES.md` §(b) and §(c) item 2 assert:

> **Theorem 8A.12 does not exist in the Markdown.** … no such theorem is
> stated or proved anywhere in `main.md` or `appendix.md`.

This is wrong. `main.md` lines **2096–2135** contain
*"**Theorem 8A.12 (the trace-class category over `𝓐_tr`; closure under
`‖·‖_tr`-limits).**"* with a bracketed note recording that the text "never
entered this document" in phase 130 and was *"Entered in phase 137 (record
repair), with the proof the audit accepted"* — followed by a full statement
(a)–(d) and a full proof (Young's inequality, faithfulness of the regular
representation of $L^1$ of a LCA group, the extension of $F\mapsto E_F$, and
closure of $\mathrm{Corr}^{tr,\mathcal A}_A$ under $\lVert\cdot\rVert_{tr}$
limits of presentations with $\Tr_A$ continuous).

So a theorem the Markdown proves has been dropped, and the notes' justification
is stale — the converter evidently read a pre-phase-137 copy of §8A.3quater.
Note that tex Proposition 9.3 (`prop:faithful`) is exactly part (b) of it,
restricted to $\DA$, with the same two proofs — further evidence that the
material was available.

*Fix.* Restore it as a proposition in §10 (right after Theorem 10.2), stating
(a)–(d) with the Markdown's proof, and delete the corresponding paragraphs from
`TEX_CONVERSION_NOTES.md` §(b) and §(c)2. This also strengthens the paper: it
gives $\Atr$ objects, not just a norm, and makes $\Tr_A$ continuous on
presentations.

**D2 (MINOR).** The conversion notes' flagged item 5 says Theorem 12.2(a)
"appeals to freeness of the lattice action … the same unproved input as in
item 1". It is not the same input (see m1); the notes over-report a defect.

**D3 (no finding). Exclusion list verified accurate** on the remaining six
points:

| Excluded | Markdown status | Verdict |
|---|---|---|
| §13.1–13.8 "what was tried and withdrawn" | `main.md` ll. 4761–4986, withdrawn routes and false intermediate statements | correctly excluded |
| Theorem 7.4 (isomorphic shadows) | `main.md` l. 987: "**Theorem 7.4 (withdrawn)**" | correctly excluded |
| Theorem 7.1(d) (real place) | `main.md` ll. 913–917, 985–986: rests on `P123.094/096/097/118/119`, `PROVED-IN-REPOSITORY` only | correctly excluded; nothing downstream uses it |
| Theorem 8A.7 / Fredholm display | imported cutoff theorem + undetermined constant; survives as Prop. 6.8 with the asymptotic as a hypothesis | correctly excluded |
| $\Nrad_\infty=0$, $\Nrad_\infty^{W}=0$, (3.10) | `main.md` ll. 5016–5017, 5117: explicitly *not* claimed | correctly excluded, and the tex records the non-claim at l. 3395 |
| $c_{\mathrm{cut}}$ | `main.md` l. 5118: undetermined | correctly retained only as the unnamed constant of Prop. 6.8 |

**D4 (no finding). Nothing in the tex is stronger than the Markdown.** Spot
checks on the headline results — Theorem 8.4 ($\Nrad=0$) vs md Theorem 9.8,
Theorem 15.1 (signature) vs md Theorem 14.1 including \eqref{eq:mbound},
Theorem 13.9 vs md Theorem 10.9/(10.13), Theorem 15.2 vs md Theorem 10.8b
(`CLASSICAL — Mertens`) — show the tex statements identical or weaker.
The two deliberate *weakenings* are correct and welcome: the Hom
classification, `PROVED modulo (Tr)` in the md (l. 429), is demoted to
Hypothesis 3.1; and the archimedean closed form, "quoting a repository
computation" in the md, is demoted to an import (subject to M7).

---

## 4. Compilation

`pdflatex -interaction=nonstopmode main.tex`, twice, in a clean directory:

* **Errors:** none.
* **Undefined references / citations:** none. All 13 bibliography entries are
  cited.
* **LaTeX warnings:** only `Label(s) may have changed. Rerun…` on the second
  pass, which is the normal two-pass notice (a third pass clears it, as the
  notes say).
* **pdfTeX / hyperref warnings:** none.
* **Pages:** 51. **Sections:** 15. Matches the notes.
* **Overfull boxes: 4**, all in displays or display-adjacent paragraphs:

| log line | source | width | judgement |
|---|---|---|---|
| 575 | ll. 1628–1636 (shell-part paragraph, Thm 7.2 proof) | 27.0pt | **fixable**: break the inline display after $\int_{\Z_p^\times}\kappa_p(w)dw$ |
| 592 | l. 2379 (display in Thm 8.15(b) proof) | 59.7pt | **fixable**: split the $N(G_m)\le\ldots$ display over two lines |
| 603 | ll. 2963–2966 (New places paragraph, Thm 11.3) | 72.3pt | **fixable**: the long inline parenthetical `($\ell^{-k}$ at $\infty$, …)` should be a display |
| 614 | l. 3977 (display in Thm 15.2 Step 4) | 45.2pt | **fixable**: break the $\sum_p|W_p(H')|$ chain |

All four are worth fixing; none is a correctness issue. (MINOR.)

---

## 5. Style

* **Preamble/macros vs Paper 42:** `diff` shows identical document class
  (`amsart`, 11pt), identical package list, identical geometry, hyperref,
  microtype, parskip and emergencystretch settings, identical theorem-style
  scaffolding. Differences are only the task-appropriate macro sets
  (`hypothesis`/`convention` here vs `problem`/`conjecture` there; `\Th`,
  `\DA`, `\Picb`, … here vs `\RH`, `\QW`, `\Div`, … there). **Consistent.**
* **Title** names what is constructed — a correspondence algebra, its
  canonical trace, its Tate symbol, its numerical form — with no claim and no
  programme word. **Good.**
* **No AI-flavoured or meta prose** anywhere. No "we now turn to", no
  "importantly", no summaries of the paper's own virtues. The register is that
  of a research monograph.
* **Section audit (filler / duplication):** none of the 15 sections is filler.
  The two candidates I examined closely both survive:
  * §14 (*The classical model*) is a single theorem plus three scope remarks;
    it is explicitly flagged as "a test of structural correctness rather than a
    construction used elsewhere", so it is not load-bearing, but it is short
    and it earns its place by fixing what the formalism is modelled on. Keep.
  * §15.2 (*Mertens*) is explicitly flagged as used nowhere else and deletable.
    It is the single most striking statement in the paper (the structure
    constant is the logarithmic density of prime powers). Keep, with the flag.
  * §9 (*Presented complexes…*) and §10 (*The trace Banach algebra*) look
    adjacent but are not duplicative: §9 fixes the domain and the target, §10
    the norm and the determinant germ. The only genuine overlap is the double
    definition of $N$ (m3).

---

## Verdict

**MAJOR REPAIRS NEEDED.**

The mathematics is of high quality and, where it is written out, it is written
out properly: I re-derived the local densities, the conductor identity
\eqref{eq:conductor}, the whole symbol computation, the Mittag–Leffler
expansions and their contour consequences, the vanishing of the radical, the
Tate sequence and the construction of the rulings in the completion, the
effectivity section, the base change, the signature and the Mertens limit, and
found no error of substance. The separation theorem (6.11) and the
Mittag–Leffler analysis (7.4) are genuinely good. The paper is also unusually
scrupulous about what it does *not* claim, and the vocabulary and style
constraints are met without exception.

It cannot be accepted in this state for two reasons, one structural and one of
record:

1. **B1** — §3's excision, one of the four advertised results, rests on four
   displayed facts that are neither proved nor cited, and this was not
   disclosed. Together with **M1**, **M2**, **M3** and **M6**, the article
   fails the contract "every theorem has a complete proof or a precise external
   citation" at five identified points, four of them in §§3 and 5.
2. **D1** — a theorem that `main.md` states and proves (8A.12) was dropped
   because the conversion notes recorded, incorrectly, that it does not exist
   there.

None of these requires new mathematics. B1, M2 and m1 are writing tasks; M1,
M3, M6 and M7 are citation tasks; D1 is a transcription task. A second round
that closes B1, M1–M7 and D1 should reach acceptance.

---
---

# Review R2 — confirmation round

Verified against the current `main.tex` (4617 lines, 58 pages), not against
`TEX_CONVERSION_NOTES.md`. Sources consulted directly:
`03-research/phase-123-weil-strength-abc/P123_121`, `P123_122`, `P123_123`,
`P123_124`, `P123_125`. `main.tex` was again not modified.

## Per-finding status

| # | Finding | Status |
|---|---|---|
| B1 | excision inputs unproved/uncited | **CLOSED** — see §R2.1 |
| M1 | crossed-product collapse | **CLOSED as a hypothesis** — see §R2.2 |
| M2 | positive-degree vanishing for a shell algebra | **CLOSED** — see §R2.3 |
| M3 | Wodzicki excision | **CLOSED** |
| M4 | `Hom(U,N)=0` asserted unconditionally | **CLOSED** |
| M5 | "used exactly twice" false | **CLOSED** |
| M6 | duality formula for a graph | **CLOSED** — see §R2.4 |
| M7 | archimedean closed form imported | **CLOSED** — see §R2.5 |
| D1 | Theorem 8A.12 dropped | **CLOSED** — see §R2.6 |
| m1–m9 | minor findings | **all nine CLOSED** — see §R2.7 |
| — | compilation, vocabulary, style | **CLEAN** — see §R2.8 |
| m10, m11 | two new one-line editorial residuals | **OPEN**, see §R2.9 |

### R2.1 B1 — closed, and the sources do contain the proofs

The four facts are now Lemmas 3.6–3.9 (ll. 685–893), preceded by the explicit
ideal definition \eqref{eq:UJ} and the finite coefficient decomposition
\eqref{eq:Ldecomp}. I checked each proof from scratch **and** against the
sources; nothing was invented.

* **Lemma 3.6 (partition + summability).** Construction matches `P123.124` §2
  exactly: smooth real partition $\psi_n$ with uniform derivative bounds and
  cutoffs $\varepsilon_n\equiv1$ on $\supp\psi_n$; shell idempotents at $p\in
  J$; `\chi_p` *plus* the negative shells at $p\notin J$, with the source's
  warning ("one must not decompose a nonzero value at $x_p=0$ into infinitely
  many flat positive-valuation shells") reproduced verbatim in substance.
  \eqref{eq:partition} = source (2); \eqref{eq:summable} = source (3). The tex
  **improves** on the source: it fixes the weights explicitly
  ($l_{\nu}>l_{\alpha}+l_{\beta}+1$ and likewise at each place), which the
  source leaves as "applying a stronger real weight and stronger shell
  weights". The Leibniz remark, the trivial-conductor/identity-label remark and
  the final "no claim that $\sum_i\rho_i$ converges inside the ideal" are all
  in the source. **Correct.**
* **Lemma 3.7 (relative projectivity + bar contractibility).** $h_J$ =
  source (4); right $U$-linearity from $\rho_i(ab)=(\rho_i a)b$; retract of the
  free module $I_J^{\flat}\widehat\otimes U$; lifting through admissible
  surjections; the $\pi h\pi$ argument for the retract; the bar contraction by
  insertion at the first factor. All four steps are in `P123.124` §3, in the
  same order and with the same justifications. **Correct.**
* **Lemma 3.8 ($I_J\widehat\otimes_UI_K\cong I_{J\cup K}$).** Injectivity by
  tensoring the admissible sequence with the relatively projective $I_J$ and
  the support containment $U_J\cap U_K=U_{J\cup K}$; surjectivity by $h_{J\cup
  K}$. = source (5), and \eqref{eq:idealprod} = source (6), with the same
  reason (no higher terms, by one-sided relative projectivity). **Correct.**
* **Lemma 3.9 (Čech resolution and the two vanishings).** (i) = `P123.125` §1
  including the observation that the scalar lattice summand is not in $I_O$;
  (ii) = §2, and the contraction argument is the source's — on a coefficient
  summand $C_L$ the complex is the augmented simplicial chain complex of the
  full simplex on $\mathcal A_L=\{a:J_a\subseteq L\}$, contracted by insertion
  of the least vertex, with the $\mathcal A_L=\emptyset$ case handled
  separately, the contractions combined by the continuous finite projections
  and explicitly *not* $U$-linear; (iii) = §3 (3), with the continuous
  splitting propagating the vanishing to the completed tensor; (iv) = §3 (4).
  **Correct.**

I re-checked the downstream: Lemma 3.11 (`lem:excvanish`) now cites Lemmas 3.6
and 3.8 rather than a bare display, and Lemma 5.1 (H-unitality) takes its
contraction from Lemma 3.7 instead of restating it. §3 is now self-contained.
**B1 is closed.**

### R2.2 M1 — the phase-123 finding, explicitly

**The coordinator's question: do `P123_121` and `P123_123` prove the
continuity of the crossed-product decomposition? They do not.**

* **`P123_121`** (*One smooth semilocal source containing the zero-stratum
  boundaries*) constructs the coefficient algebra, its finite coordinate
  decomposition, the dilation with its attaching correction, and the semilocal
  embeddings. Its six sections contain **no** Hochschild computation: grep for
  `Hochschild`, `Koszul`, `group homology`, `conjugacy`, `collapse` returns
  nothing in that file. It supplies temperedness and continuity of the
  $\Gamma$- and $\beta$-actions — i.e. the *hypotheses* of the decomposition,
  not the decomposition.
* **`P123_123`** (*Equivariant semilocal composition*) proves a **different**
  theorem. Its §1 shows the old induction fails the unit test; §3 sets up
  tempered equivariant modules; §4 proves an invertible composition comparison
  with its inverse; §5 proves that crossed bar resolutions remain resolutions
  with relatively flat terms, and its main result (11) is
  $(M\widehat\otimes^{\mathbf L}_CN)\rtimes G$ — a **derived monoidal transport
  of crossed products along a tensor product**, not a decomposition of
  $\HH_*(A\rtimes\Gamma)$ over group labels with a group-homology factor. The
  file does contain the continuity statements the Markdown was gesturing at
  ("Crossing a continuous underlying linear contraction preserves it
  coefficientwise; its seminorm bound is independent of the label", §5; the
  seminorm estimates for (7)–(10) in §4), but they are continuity statements
  **for (11)**, not for the label-$\gamma$ Koszul collapse.
* `P123_122` mentions Koszul signs only in the double-bar rotation for the
  shadow, which is unrelated.

**Conclusion (row-A record fact): the repository does not prove the continuous
crossed-product Hochschild decomposition, and Hypothesis 5.9 is the correct
disposition.** It should *not* be replaced by a proof on the strength of
`P123_121`/`P123_123`.

I then verified the dependency claim, since it is what makes the hypothesis
harmless:

* Hypothesis 5.9 (`hyp:crossed`, ll. 1333–1345) is stated abstractly with its
  hypotheses (unital complete Fréchet $A$, tempered $\Z^{d}$-action, continuous
  $\beta$ commuting with $\alpha$ and fixing the gauge unitaries) and its
  conclusion (admissible homotopy equivalence with
  $\mathrm{Tot}(\mathcal K_{\Gamma}(\alpha)\widehat\otimes C(A,A_{\gamma\beta}))$).
  The Koszul complex now carries the differentials $\alpha_{g_i}-1$, so no
  triviality of the lattice action is smuggled in — a genuine improvement over
  the R1 text, which wrote a plain tensor product.
* The algebraic statement is now cited precisely: Nistor [§§3–4],
  Getzler–Jones [§3], Brylinski, with the abelian-centralizer reduction spelled
  out. Exactly what M1 asked for.
* Theorem 5.10(a) is flagged *(under Hypothesis 5.9)* in its own statement;
  the proof opens "Assume Hypothesis 5.9". Parts (b) and (c) do not use it —
  (b) is Theorem 5.3, (c) is Lemmas 5.5/5.6 plus commutativity.
* **Dependents.** `thm:shadow` is referenced at ll. 158/161 (introduction),
  1421 (`cor:blind`) and 4059 (`prop:contactblind`), and nowhere else. The two
  further references to `cor:blind` (ll. 1663, 1768) are rhetorical contrasts
  ("the reason the analytic trace is usable where the additive ones are not"),
  not logical uses: Proposition 6.12's own proof runs through Lemmas 5.5 and
  5.6, both unconditional. **Confirmed: Corollary 5.12 and Proposition 13.10
  are the only dependents, and the trace, the symbol, the numerical theory, the
  Banach algebra, the charts, effectivity, Riemann–Roch proper, the classical
  model and the signature are all independent of Hypothesis 5.9.**

### R2.3 M2 — closed, conclusions intact

Lemma 5.6 now states only $\HH_0(F^{(j)},(F^{(j)})_{\sigma})\cong\C^{N_k}$ and
\eqref{eq:D2} as an $\HH_0$ statement. The two unproved assertions are gone.
Remark 5.7 (`rem:higherdegrees`) gives the precise reason the positive-degree
statement is withheld — the level-$N$ separability idempotent is a
separability idempotent for that level only and its size in
\eqref{eq:seminorms} is not uniform in $N$ — which is exactly right, and is a
better disclosure than R1 asked for.

I checked that every conclusion survives:

* **Theorem 5.10(c)**: the untwisted claim is weakened to
  $\HH_0(E_p,E_p)\cong E_p$ and now proved in one line by commutativity; the
  non-unit case is still the *full* complex $\simeq\C[0]$, which is legitimate
  because Lemma 5.5's twisted complex is contractible in all degrees and the
  contraction is exhibited — the proof says so explicitly; the unit case is
  $\HH_0$ of infinite dimension.
* **Corollary 5.12**: conclusion unchanged, and its proof now reads "a complex
  with infinite-dimensional $\HH_0$ has no finite rank, no Euler
  characteristic and no determinant line, **whatever its higher homology**" —
  which is the correct logic and is independent of the withheld statement.
* **Proposition 13.10**: same rephrasing, same conclusion.

Nothing was lost. **Closed.**

### R2.4 M6 — closed; I re-derived it

Theorem 14.1 now uses the *untwisted* $\Phi(E_\lambda)=\mathcal
O_{\Gamma_{\phi(\lambda)}}$, and (c) is the displayed
\eqref{eq:dualitygraph}. I recomputed the derivation independently:

* FLI \eqref{eq:fli} with $c=1$ and $N_{\Gamma_f}\cong T_C$ (via
  $\id\times f^{-1}$ carrying $\Gamma_f$ to $\Delta$) gives
  $\mathcal O_{\Gamma_f}^{\vee}\cong i_{f*}(T_C)[-1]$. ✓
* $\sigma\circ i_f=i_{f^{-1}}\circ f$ ✓, so
  $\sigma^{*}i_{f*}(G)\cong i_{f^{-1}*}((f^{-1})^{*}G)$ ✓; the shifts $[-1]$
  and $[1]$ cancel ✓.
* $i_{f^{-1}}^{*}H=h\otimes(f^{-1})^{*}h$ ✓ (since $p_1i_{f^{-1}}=\id$,
  $p_2i_{f^{-1}}=f^{-1}$), so by the projection formula
  $D_h(\mathcal O_{\Gamma_f})\cong i_{f^{-1}*}(h\otimes(f^{-1})^{*}(T_C\otimes
  h))$ ✓, and $T_C\otimes h\cong\omega_C^{-1}\otimes h\cong h^{-1}$ ✓.
* The right-hand side of \eqref{eq:dualitygraph} evaluates by the projection
  formula to the same thing ✓, and at $f=\id$ the twist is $\mathcal O_C$ ✓.

The **$0=-2$ computation** also checks out: for
$\Psi(E_\lambda)=i_{f*}(h^{a}\otimes f^{*}h^{b})$ the same chain gives
$D_h(\Psi)\cong i_{f^{-1}*}((f^{-1})^{*}h^{-a-1}\otimes h^{1-b})$ ✓ against
$\Psi(E_{\lambda^{-1}})=i_{f^{-1}*}(h^{a}\otimes(f^{-1})^{*}h^{b})$, forcing
$a=1-b$ and $b=-a-1$, whence $a=a+2$. *(Pedantic: substituting gives $0=2$,
not $0=-2$; the sign of the contradiction is immaterial and I do not count it
as a finding.)* The statement of (c) has been weakened to exactly what is
proved. **Closed.**

### R2.5 M7 — closed; I recomputed the whole derivation

\eqref{eq:Winfclosed} is no longer imported. I verified every step of the new
paragraph (ll. 1996–2035):

* $b(t)=e^{i\tau t}$, $b(-t)=e^{-i\tau t}$ in the log-modulus coordinate, so
  the bracket of \eqref{eq:Winf} is $2\cos\tau t-2e^{-t/2}$ ✓ (and this is the
  reading that makes $\Wh_\infty$ real, consistent with
  \eqref{eq:Winfhat2}).
* $u=2t$: $e^{-t/2}=e^{-u/4}$, $1-e^{-2t}=1-e^{-u}$, $dt=du/2$, and the factor
  $2$ in the bracket cancels the $\tfrac12$ — giving exactly
  $\mathcal J(\tau)=\int_0^\infty[e^{-u/4}\cos(\tau u/2)-e^{-u/2}](1-e^{-u})^{-1}du$ ✓,
  with $e^{-u/4}\cos(\tau u/2)=\tfrac12(e^{-\alpha u}+e^{-\bar\alpha u})$,
  $\alpha=\tfrac14+\tfrac{i\tau}2$ ✓.
* Subtracting Gauss's representation at $s$ and at $\tfrac12$ gives
  $\int_0^\infty(e^{-su}-e^{-u/2})(1-e^{-u})^{-1}du=\psi(\tfrac12)-\psi(s)$ ✓;
  averaging over $s=\alpha,\bar\alpha$ gives
  $\mathcal J=\psi(\tfrac12)-\Rel\,\psi(\alpha)$ ✓.
* $\psi(\tfrac12)=-\gamma-2\log2$ ✓, so
  $(\gamma+\log4\pi)-\gamma-2\log2=\log4+\log\pi-2\log2=\log\pi$ ✓.
  **The constant of Definition 6.5 produces $\log\pi$ exactly, as claimed.**
* **Monotonicity**: $\Rel(n+\tfrac14+\tfrac{i\tau}2)^{-1}=
  (n+\tfrac14)/((n+\tfrac14)^2+\tau^2/4)$ ✓, positive and decreasing in
  $|\tau|$, so each subtracted term decreases and the sum increases ✓; local
  uniform convergence of the Gauss series justifies the termwise conclusion ✓.
  \eqref{eq:maxarch} follows, with $\psi(\tfrac14)$ cited to DLMF §5.4(iii) and
  the integral representation to DLMF §5.9 — both pinpoint.

`\cite{Weil1952,CCWeilArch}` now appears only as an identification remark,
explicitly not relied upon ("the derivation above fixes the normalization, and
no comparison of conventions is required"). **The archimedean backbone —
including the constant $5.372$ of Theorem 15.1(c) and the Mittag–Leffler
expansion of Theorem 7.4(b) — is now self-contained. Closed.**

### R2.6 D1 — closed, and the closure statement is exactly what is proved

Theorem 10.3 (`thm:Atrcat`, ll. 3170–3241) reproduces `main.md`
Theorem 8A.12(a)–(d) (ll. 2096–2135) faithfully:

* (a) Young + \eqref{eq:trnormineq}, multiplicativity, $\lambda(H^\dagger)=
  \lambda(H)^{*}$ — same proof as the md;
* (b) faithfulness, correctly noted to use nothing beyond
  $\Atr\subseteq L^{1}(C_S)$, and cross-referenced to the second argument of
  Proposition 9.3 — which is retained over $\DA$ and now points forward;
* (c) the extension of $F\mapsto E_F$;
* (d) the category over $\Atr$, with the transported results listed, and —
  **critically — the closure statement carries the "common finite support"
  qualifier**, exactly as the md does ("all supported in one finite set of
  degrees"). The proof closes $d_{n+1}\star d_n=0$ under limits by
  submultiplicativity and gets $\Tr_A$ continuity from Theorem 10.2(c) plus
  finiteness of the common support. No over-claim.

Remark 10.4 (`rem:whichcompletion`) adds the two correct disclaimers: nothing
is claimed for limits without a common finite support, and $\NAd$ is a
numerical module that indexes no objects. The abstract (l. 312) and the
introduction record the addition. **Closed.**

### R2.7 Minor findings m1–m9

All nine verified in the current source: m1 the freeness line is added
(l. 3527, "$\gamma x_\infty=x_\infty$ … then $\gamma=1$"); m2 the Mellin
independence with the cross-reference; m3 the duplicate $N$ removed, both later
uses now pointing to \eqref{eq:Nsemi}; m4 $L^{(q)}(F):=L_S^{(q)}(F,F)$ defined
and the cross-effect exponent computed (ll. 3916–3926), correctly yielding
$2\Rel W_q$; m5 the two regimes of $B(t)$ split and the profile renamed $\eta$;
m6 the clause "the ring underlying $\DA^{+}$ — no completed tensor product is
used" (l. 3979); m7 the unit classes outside $1+p\Z_p$ recorded; m8
Convention 6.10's list corrected; m9 `\Ltr`, `\dg`, `\Spec` and the `example`
environment all removed (grep count 0). **All closed.**

### R2.8 Vocabulary, style, compilation

* **Vocabulary regrep** (including the new terms `referee`, `review`, `audit`,
  `repair`): every surviving hit is mathematics — `contractible`/`contraction`,
  *row measures*, lattice *labels*, `proved` in ordinary prose, and "does not
  repair the finite chart" (l. 4531) / "does not repair it" (l. 4220), both
  about cones and charts. **No forbidden vocabulary, and no meta prose about
  the writing, the review, or the repairs entered the article.**
* **Compilation from clean, three passes:** **0 errors, 0 LaTeX/pdfTeX/package
  warnings, 0 undefined references or citations, 0 overfull and 0 underfull
  boxes.** 58 pages, 15 sections. (The notes say 19 bibliography entries; the
  file has **17** — all cited, since the run is warning-free. Harmless
  bookkeeping slip in the notes, not in the paper.)
* **Style:** preamble unchanged and still aligned with Paper 42; the four new
  lemmas sit inside §3 rather than in a new section, so the section count is
  unchanged and no section is filler; the seven added pages are all proof.

### R2.9 Two residuals, both one-line and editorial (OPEN)

**m10 (MINOR).** Lemma 3.7, ll. 786–787:

> `applying the involution of Section~\ref{sec:dagger} and reversing the
> factors gives the statement on the left.`

There is no involution of $U$ in this article: §4 defines $\dagger$ on $G$ and
the Hilbert adjoint on graph operators, not an antiautomorphism of the source
algebra. (`P123.124` §3 says "the source involution", which that note has and
this paper does not.) The statement is true and the repair is one line:
replace the appeal by the mirrored partition
$h_J^{\mathrm{op}}(a):=\sum_i a\rho_i\otimes e_i$, which satisfies the same
estimate \eqref{eq:summable} and exhibits $I_J$ as a left-module retract.

**m11 (MINOR).** Line 1356–1357:

> `Only part (a) of the next theorem uses it, and through it only
> Corollary~\ref{cor:blind} and Proposition~\ref{prop:contactblind}; nothing in
> Sections~\ref{sec:trace}--\ref{sec:signature} depends on it.`

The second clause contradicts the first: Proposition 13.10
(`prop:contactblind`) *is* in Section 13, which lies in the named range
§6–§15. This is the same species of over-tidy scope claim as the original M5.
Fix: "…; no result of Sections 6–15 other than Proposition 13.10 — an aside in
§13.3 — depends on it."

Neither residual affects any proof, and neither requires new mathematics.

---

## Verdict R2

**ACCEPT** — subject to the two one-line editorial corrections m10 and m11.

Every blocking and major finding of R1 is genuinely closed in the source, not
merely in the notes. I re-verified the B1 lemmas against `P123_124` and
`P123_125` line by line and found no invention; I re-derived the M6 duality
identity, the M6 obstruction computation, and the whole M7 archimedean closed
form and its monotonicity independently; I confirmed the M2 rephrasing loses
no conclusion; and I confirmed the D1 restoration matches the Markdown
including the "common finite support" qualifier.

The paper now declares exactly two hypotheses and one import, all three labelled
in the text, all three with their dependents named, and — after m11 — named
correctly. The declared archimedean import is gone. The article is
self-contained apart from those three, which is the right state for a paper of
this kind.

**Row-A record fact requested by the coordinator (M1): `P123_121` and
`P123_123` do NOT prove the continuity of the crossed-product Hochschild
decomposition. `P123_121` supplies only the algebra and the temperedness of the
actions; `P123_123`'s theorem (11) is derived monoidal transport of crossed
products along a tensor product, a different statement. Hypothesis 5.9 must
stand. Its only dependents are Theorem 5.10(a), Corollary 5.12 and
Proposition 13.10; Sections 6–15 are otherwise independent of it, and the
trace, symbol, numerical theory, Banach algebra, charts, effectivity,
Riemann–Roch, classical model and signature are all unconditional on it.**
