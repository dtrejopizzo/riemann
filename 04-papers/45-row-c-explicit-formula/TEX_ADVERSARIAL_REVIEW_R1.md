# Adversarial referee report R1 — `main.tex` (Paper 45)

Reviewed: `main.tex` (2442 lines), against `main.md` (2401 lines) and
`TEX_CONVERSION_NOTES.md`. Compiled twice with `pdflatex`; 31 pages.
No edit was made to `main.tex`.

---

## 1. Forbidden vocabulary — clean

`grep -n -i` over `main.tex` for: `Riemann hypothesis`, `\bRH\b`, `hypothesis
of Riemann`, `critical line`, `phase`, `row `, `round`, `construction`, `auditor`,
`label`, `honest`, `candidly`, `PROVED`, `P1[0-9][0-9]`, `106_1`,
`programme`, `corpus`, `repositor`, `of record`, `ledger`, `withdraw`,
`acceptance`, `contract`, `status`, `conjectur`.

Genuine hits: **none**. All matches are `\label{...}` commands, the ordinary
English verb "proved", `\newtheorem{conjecture}` (an unused preamble line
inherited from Paper 42), and `Riemann--von Mangoldt` / `Riemann
zeta-function` as proper mathematical names (lines 65, 222, 2298, 2317, 2421).
The word "conjecture" appears nowhere in the body; no statement of the form
"all zeros lie on ..." is asserted or named. Abstract, introduction (§1),
Remarks 9.5, 9.7, 9.8, 11.4 and both appendices were read in full: the paper
consistently phrases the relevant statements as "a zero off the line
`Re s = 1/2`" and never as a hypothesis or conjecture. Remark 11.4's
contrapositive ("then every zero of ξ lies on the line Re s = 1/2") is a
conclusion of a proved implication, not a named conjecture, and is admissible.

**Finding 1.1 — MINOR.** Line 21: `\newtheorem{conjecture}[theorem]{Conjecture}`
is declared and never used. Harmless, but a referee will read an unused
`conjecture` environment in a paper of this kind as a leftover. *Fix:* delete
line 21 (and line 20, `problem`, likewise unused).

**Finding 1.2 — MINOR (residual internal register).** Lines 459–460
("standing caution: no statement of the present paper asserts a sign"),
760–762 ("The negative half of the assertion is a statement about what is
*not* proved, and is recorded as strongly as the positive half"), 1495–1514
(Remark 9.5, "the normalisation is load-bearing"), 1862–1879 (Remark 10.8's
"deletion test"). These are not forbidden vocabulary, but they are audit
register rather than mathematics, and they read as answers to an unseen
referee. *Fix:* keep the mathematical content (that no positivity is claimed;
that (E8) is used only twice), delete the self-assessment clauses.

---

## 2. Completeness of proofs

Every `theorem`/`proposition`/`lemma`/`corollary` environment was enumerated
(`grep -n`) and matched against the following `proof` environment or its
bracketed citation. Result: **34 environments, 33 of which are either proved
in full or carry a bracketed citation to a numbered external statement.** The
single exception is Finding 2.1. Substantive gaps found in the proofs
themselves are Findings 2.2–2.8.

### 2.1 — MAJOR. A proposition with neither proof nor citation
*Location:* lines 980–992, `\begin{proposition}[where the isotropic directions
live]` (`prop:live`, Proposition 7.3).
*Quote:* "They exist in the completion $\mathcal N_A^{\mathrm{dist}}$, as
limits of spread Tate families, and the plane they span is exactly the scalar
radical there. In particular they are not radial classes: they are limits of
families whose $L^1$-mass escapes to $|w|_S\to\infty$."
*What is wrong:* the environment has no `\begin{proof}` and no bracketed
source. Its first clause is covered by the inline reference to
Proposition 2.6, but the second and third clauses (existence of the limits;
the escape of $L^1$-mass) are asserted with no reference at all. In `main.md`
the corresponding Proposition 8.3 carries "*Proof.* Citations, verbatim. ∎
`PROVED-IN-REPOSITORY` (Paper 43 Thms. 9.13, 9.14a–c′)" and the $L^1$-mass
clause cites Paper 43 Definition 9.14c0. The tex dropped both.
*Fix:* give the environment the bracketed header
`[\cite{P43}, Theorems 9.13(a), 9.14a--9.14c$'$, Definition 9.14c0]`, or
demote it to a remark; and add the one-line proof "Citations, verbatim."

### 2.2 — MAJOR. The load-bearing import of Theorem A is cited imprecisely
*Location:* lines 360–361 (`prop:symbol` header) and lines 381–390 (part (c));
used at lines 700–712 (proof of Lemma 4.2 = Theorem A) and at lines 2198–2212
(proof of Theorem 12.2 = Theorem G).
*Quote (line 360):* `\begin{proposition}[\cite{P43}, Theorem 9.7 and (9.11)]`
*Quote (lines 386–389):* "and the identity holds *place by place*,
$W_v(H)=\int\widehat H\,\widehat W_v\,d\chi$ for every $v\in S$, each integral
absolutely convergent."
*What is wrong:* the place-wise clause is *not* part of P43 Theorem 9.7 or of
(9.11). `main.md` (lines 612–617) is explicit: the place-wise identity "was
proved inside Paper 43 Theorem 9.7(d)'s termwise interchange but was not a
numbered assertion; it is now Paper 43 Theorem 9.7(d′)", i.e. (9.13′). The
converter's own notes (item (c)3) flag this as "the single load-bearing import
of Theorem A". As printed, the reader who goes to P43 Theorem 9.7 and (9.11)
will not find the statement on which Theorem A and Theorem G rest.
*Fix:* change the header to `[\cite{P43}, Theorem 9.7, (9.11), and Theorem
9.7(d$'$)/(9.13$'$)]`, and add after part (c) the sentence: "The place-wise
form is \cite{P43}, Theorem 9.7(d′), equation (9.13′); Lemma 4.2 and
Theorem 12.2 rest on it."

### 2.3 — MAJOR. "A has exactly two poles" is false as stated in the abstract
and in the introduction
*Location:* abstract, lines 79–80; introduction, Theorem E, lines 192–194;
section heading, line 1678.
*Quote (lines 79–80):* "the continued Euler-product symbol
$A(s)=\tfrac12\log\pi-\tfrac12\psi(s/2)-\zeta'/\zeta(s)$ has exactly two
poles, at $s=0$ and $s=1$, each of residue $1$".
*Quote (lines 192–194):* "Then $A$ has exactly two poles, at $s=0$ and $s=1$,
both simple and both of residue $1$".
*What is wrong:* $A=-\xi'/\xi+1/s+1/(s-1)$ (the paper's own
Theorem 10.3(i)), and $\xi'/\xi$ has a simple pole at **every zero of $\xi$**,
with residue the multiplicity. So $A$ has infinitely many poles; its poles are
$s=0$, $s=1$ and every nontrivial zero of $\zeta$ (the poles at $s=-2n$ do
cancel between $-\tfrac12\psi(s/2)$ and $-\zeta'/\zeta$, but the zeros do
not). The theorem body, line 1711, is correctly hedged — "$A$ has exactly two
poles **in $\{0,1\}$**" — and this matches `main.md` Theorem 9bis.2′(ii)
verbatim. The abstract and the introduction dropped the three-word
restriction and thereby assert a falsehood about the central object of §10;
they also state something strictly stronger than anything the Markdown marks
as proved (a fidelity defect, §3 below).
*Fix:* in the abstract and in Theorem E write "has exactly two poles in
$\{0,1\}$, both simple and both of residue $1$, and is regular at every other
point of $\Rel s\ge 0$ outside the zero set of $\xi$"; retitle §10.2 "The
continued symbol and its poles at $s=0$ and $s=1$".

### 2.4 — MAJOR. Step 2 of the sufficiency proof invokes the wrong case of
its own estimate
*Location:* line 2021, Step 2 of the proof of Theorem 11.3 (Theorem F) — one
of the two steps the converter rewrote.
*Quote:* "by repeated integration by parts. Using (11.6) with $M=0$, fix
$R>|x_0|+1$ such that no point of $\mathcal Z$ has $|\Rel z|=R$ and [(11.7):]
$\sup_{|\Rel z|\ge R,\ |\Iml z|\le1/2}|D(z)|/|D(z_0)|\le\tfrac12$."
*What is wrong:* (11.6) with $M=0$ asserts only that $D$ is **bounded** in the
strip; it does not give the smallness (11.7), which needs $|D(z)|\to0$ as
$|\Rel z|\to\infty$ in the strip, i.e. (11.6) with $M\ge1$. As written the
choice of $R$ is unjustified, and $R$ is used again in Step 8 through (11.7).
The repair is trivial — (11.6) is proved for every $M$ — but a referee is
entitled to treat the cited case as the claim.
*Fix:* replace "with $M=0$" by "with $M=1$, which gives
$|D(z)|\le C/(1+|\Rel z|)$ in the strip and hence $|D(z)|\to0$ as
$|\Rel z|\to\infty$ there".

### 2.5 — Verified correct (no defect), recorded because the instructions ask
for it
* **Theorem 8.4 (Theorem B) against the classical Weil formula.** Independent
  check with $h=F\star F^\dagger$, $F$ real: $\Phi_F(\tfrac12+i\gamma)=\hat
  F(-\gamma)$, so the spectral side is $\sum_\gamma|\hat F(\gamma)|^2$; the
  polar term is $\hat h(i/2)+\hat h(-i/2)=2\Phi_F(0)\Phi_F(1)$; the
  archimedean term $\frac1{2\pi}\int|\hat F|^2[\Rel\psi(\tfrac14+\tfrac{i\tau}
  2)-\log\pi]d\tau$ has the classical sign and normalisation; the prime term
  $-\sum\Lambda(n)n^{-1/2}[h(\log n)+h(-\log n)]$ is the classical
  $-2\sum\Lambda(n)n^{-1/2}g(\log n)$ with $g(u)=h(-u)$, $h$ even. All three
  constants ($2$, $1/2\pi$, $n^{-1/2}$) check out. The three internal factors
  $\frac1{\pi i}\int_{L_c}$ were recomputed independently in (a), (b), (c) and
  each is right; the cutoff $n<e^{2T}$ is correct since $\supp h\subseteq
  [-2T,2T]$ and $h(\pm 2T)=0$.
* **Theorem 9.3 (Theorem C).** $T_\infty(\Gamma_h)=-\mathcal W(F)$ (Lemma 9.2)
  combined with (9.2) gives (9.4) exactly; the sign of $\widehat W_\infty$
  relative to the Gamma term of the explicit formula is consistent.
* **Lemma 4.2 (Theorem A).** Correct, given Proposition 2.4(c); the divergence
  of $\int K(|t|)h(t)dt$ at $t=0$ and the reason the regularised value is the
  Plancherel one are stated honestly. Only the import is at issue (2.2).
* **Theorem 6.6, Proposition 5.1, Lemma 10.1, Theorem 10.3, Proposition 10.7.**
  Residue computations recomputed by hand: $\Res_{s=0}a=1$,
  $\Res_{s=0}f_p=1$, $\Res_{s=0}\zeta_p=c_p/\log p$, $\Res_{s=0}\zeta_\infty
  =1$, $\Res_{s=0}A_S=|S_f|+1$, $\Res_{s=1}A_S=0$, $\Res_{s=0}A=\Res_{s=1}A=1$;
  the $\tau$-transport residues $\mp i$; the Mertens comparison
  $\sum_{p\le x}\log p/(p-1)=\sum_{N\le x}\Lambda(N)/N+O(1)$. All correct.
  The archimedean constants (3.6) check: $\log\pi-\psi(\tfrac14)=\log\pi+
  \gamma+3\log2+\pi/2=5.3722$; $K(t)=\tfrac14[\operatorname{csch}(t/2)+
  \operatorname{sech}(t/2)]$; $K(\log n)=n^{3/2}/(n^2-1)$.
* **Theorem 11.3 (Theorem F), Steps 1–8.** Recomputed in full. $z_0=x_0+iy_0$
  with $x_0=\Iml\rho_0$, $y_0=\tfrac12-\Rel\rho_0$: correct. The quartet is
  distinct exactly when $x_0y_0\ne0$: correct, and $x_0\ne0$ is exactly where
  (E2)'s no-real-zero clause is used, as claimed. $Q(z)=P(z)P(-z)$: real,
  even, vanishing on $\mathcal Z_R\setminus\mathcal O_0$ to at least its
  multiplicity, nonzero at $\pm z_0$ — the converter's substitution for the
  cited note's $Z_R$ is sound and does avoid the parity-of-multiplicity-at-
  $z=0$ issue. The real-linear surjectivity (11.9) is equivalent to
  $\Iml(z_0^2)\ne0$: correct. The parity/reality bookkeeping in Step 5
  (even case $\overline{\mathfrak F(\bar z)}=\mathfrak F(z)=\mathfrak F(-z)$;
  odd case with $\mathfrak F=iR_N$) yields real even resp. real odd $F$:
  correct. Step 6: $4m_0\Rel(i^2)=-4m_0$ and $-4m_0\Rel(1^2)=-4m_0$:
  correct in both parities. Step 8's degree count $D_0=\deg E+3$ absorbs the
  primitivisation factor, and the tail bound works **because $D$ is even**, so
  $|D(z)D(-z)|=|D(z)|^2$ and (11.7) applies twice — the argument is correct
  but does not say that it uses the evenness of $D$ here (see 2.8).
* **Theorem 12.2 (Theorem G).** The Plancherel/density/analyticity argument is
  correct; $\hat h\in\mathcal S$, $\widehat T_S$ of logarithmic growth, $m$
  tempered, $\{\hat g\}$ dense in $\mathcal S$, zero set discrete,
  $\widehat T_S(\cz,0)>0$.

### 2.6 — MINOR. Corollary 8.5 invokes an estimate it does not have
*Location:* lines 1289–1307.
*Quote:* "$\Phi_h$ is entire and satisfies (8.1) with $C_N=\|h^{(N)}\|_{L^1}$
and $T$ replaced by $2T$ ... Lemmas 8.2 and 8.3 are unchanged, since they use
only that $g$ is entire, satisfies $g(1-s)=g(s)$ and obeys (8.2)."
*What is wrong:* here $g=\Phi_h$ is a **single** transform, so it does not obey
(8.2) as displayed (which reads $C_N^2\,e^{2T|\sigma-1/2|}|s-\tfrac12|^{-2N}$
and comes from a product of two transforms). What Lemma 8.2 actually needs is
$|g|=O(X^{-4})$ on the horizontal sides, which here is (8.1) with $N=4$, not
(8.2).
*Fix:* "…obeys the bound $|g(\sigma+i\tau)|\le C_4e^{2T|\sigma-1/2|}
|s-\tfrac12|^{-4}$, which is (8.1) with $N=4$; this is all that the horizontal
estimate of Lemma 8.2 uses."

### 2.7 — MINOR. Remark 8.6's bound is vacuous at $\rho=\tfrac12$
*Location:* lines 1310–1321.
*Quote:* "$|\Phi_h(\rho)|\le C_2e^{2T|\beta-\frac12|}|\rho-\tfrac12|^{-2}
=O(|\gamma_\rho|^{-2})$ uniformly for $\rho=\beta+i\gamma_\rho$ in the critical
strip".
*What is wrong:* (8.1) is stated only for $s\ne\tfrac12$, and the bound is
vacuous for $\rho$ with small $|\gamma_\rho|$ (and undefined if
$\rho=\tfrac12$). The conclusion survives trivially — $\Phi_h$ is entire, so
the finitely many zeros with $|\gamma_\rho|\le1$ contribute a finite amount —
but the display as written does not establish it.
*Fix:* "for $|\gamma_\rho|\ge1$; the finitely many zeros with
$|\gamma_\rho|<1$ contribute a finite amount, $\Phi_h$ being entire."

### 2.8 — MINOR. Two silent uses in Step 8 of Theorem 11.3
*Location:* lines 2131–2151.
*What is wrong:* (a) the step "$|\mathfrak F_{N,\pm}(z)\mathfrak
F_{N,\pm}(-z)|\le C_R^24^{-(N-N_0)}\Sigma_0$" uses $|D(-z)|=|D(z)|$, i.e. the
evenness of $D$ (true: $\varphi$ is even), but this is not said — as written
the reader must check that $\Sigma_0$, defined with the exponent $2N_0$ of
$|D(z)|/|D(z_0)|$, dominates the product $|D(z)D(-z)|^{N_0}$. (b) the
convergence parenthetical after (11.12) says the sum converges "because the
factor decays faster than any power of $|\Rel z|$" — which is (11.6) with $M$
large *and* $N_0\ge1$; the text says "fix $N_0$ so large that (11.12) holds",
which inverts the dependence (any $N_0\ge1$ works once $M$ is large).
*Fix:* insert "since $D$ is even, $|D(-z)|=|D(z)|$" before the display, and
replace "Fix $N_0$ so large that" by "Fix any $N_0\ge1$; by (11.6) with $M$
large and the zero count (E3d),".

### 2.9 — MINOR. Theorem 12.2's last clause is not proved
*Location:* line 2195, "and on which $M=(\lambda_-,\lambda_+)$ is defined and
surjective onto $\BT$"; proof line 2231, "The remaining assertions are
Proposition 3.2 and Proposition 2.5."
*What is wrong:* Proposition 2.5 gives surjectivity of $M$ on all of $\DA$,
not on the radial subalgebra $\DAr$. Surjectivity on $\DAr$ is true and easy —
$h\mapsto(\int he^{t/2},\int he^{-t/2})$ is onto $\C^2$ because the two
functionals are linearly independent on $C_c^\infty(\R)$ — but it is a
different statement, and the same slip is inherited from `main.md`.
*Fix:* add the one-line argument, or drop the clause.

### 2.10 — MINOR. A quoted proposition carries an embedded proof sketch that
a later proof leans on
*Location:* lines 602–650, Proposition 4.1 (`prop:primepacket`), header
`[\cite{P44}, Theorem 3bis.7]`, body: "The proof has two steps: (i) ... (ii)
...". Used at lines 685–694 in the proof of Lemma 4.2: "this is step (i) of
Proposition 4.1, which is where that proof uses radiality and *not* where it
uses $0\notin\supp h$ ... computed in step (ii) of the same proposition".
*What is wrong:* this is an appeal to the internals of somebody else's proof
rather than to a statement — the converter flags it as item (c)4 and the
appeal is in fact correct (step (i) uses radiality only, and the tex
re-derives it inline). Step (ii), however, is only referenced, not
re-derived; it rests on \cite{P43}, Lemma 8.2(i) and the volume
normalisation, both of which *are* cited.
*Fix:* make it self-contained: state the shell computation as a displayed
consequence of \cite{P43}, Lemma 8.2(i) and $\vol(p^k\Z_p^\times)=\log p$ in
the proof of Lemma 4.2, so that nothing is imported from inside a cited proof.

### 2.11 — MINOR. Appendix B misattributes one result
*Location:* lines 2377–2384; Theorem 6.5 (`thm:archsymbol`) is listed under
"Proved here". Its proof (lines 856–862) reads "Identity (6.2) is
Proposition~\ref{prop:symbol}(a)" — i.e. the substantive half is quoted from
\cite{P43}; only the constant reconciliation $\gamma+\log4\pi+\psi(\tfrac12)
=\log\pi$ is proved here.
*Fix:* move it to the "quoted" list with the note "the constant
reconciliation proved here", or restate the theorem as being about the
constant only.

No circular appeals were found: the explicit formula is proved from
(E1)–(E5) with no input from the companion papers, and the companion results
are used only for the algebra, the trace and its symbol. "It is easy to see"
does not occur. No reference to a non-existent "result above" was found; all
`\ref`s resolve (no undefined references in the log).

---

## 3. Fidelity to the proved set

Every included statement was matched to its Markdown origin using the
conversion table. The mapping is accurate; I re-derived it independently for
Lemma 5.1a → Lemma 4.2, Theorem 9.4 → Theorem 8.4, Theorem 9.6 → Theorem 9.3,
Corollary 9.6a → Corollary 9.4, Theorem 9.6′ → Theorem 9.6, Theorem 9bis.2′ →
Theorem 10.3, Theorem 10.4 → Theorem 11.3, Theorem 12.2 → Theorem 12.2. The
exclusions listed in §(b) of the notes are all either status machinery, the
withdrawal ledger, statements withdrawn there, or provenance; I checked the
ledger (`main.md` §13) and §14 and found nothing marked `PROVED` in its final
state that is silently dropped. In particular the excluded Lemma 10.3a and
Remark 10.3 are unused by the rewritten §11, and Remark 12.4a is correctly
excluded (it is a result of a different paper).

**(a) Anything in the tex not in the md's proved set?** One item:

**Finding 3.1 — see Finding 2.3 (MAJOR).** The abstract and Theorem E state
"$A$ has exactly two poles" where `main.md` Theorem 9bis.2′(ii) states
"exactly two poles **in $\{0,1\}$**". This is both a strengthening beyond the
proved set and (as a statement about $A$) false.

**Finding 3.2 — MINOR.** Proposition 2.4(d) is given under the header
"\cite{P43}, Theorem 9.7 and (9.11)", but the numerical lower bound
$\widehat T_S(\cz,0)\ge\log\pi-\psi(\tfrac14)$ is, per `main.md` §12, Paper 43
**(14.2)**, quoted there only "as a concrete witness". *Fix:* cite (14.2) for
part (d).

**(b) Anything marked PROVED and omitted without reason?** None found. The
dictionary-2 leg (S3), old Theorem 4.2/5.2/5.4, old §11, old §12.1–12.6 and
the Hodge-index reading of old Corollary 8.2 are all withdrawn or
notational, as the notes say; Corollary 8.4 and Theorem 9.14b's content
survive inside Proposition 7.3.

**The five items the converter flagged:**

1. *Sufficiency proof rewritten (§11, Steps 1–8).* The rewrite is
   mathematically sound and is a genuine improvement over the Markdown, which
   is a delta against an unpublished note and is not self-contained. Both
   presentational changes ($Q=P(z)P(-z)$; the explicit factor
   $\tfrac14+z^2$) are correct and do what the notes claim. One defect:
   Finding 2.4 (MAJOR), plus Finding 2.8 (MINOR). **After those two repairs
   the proof stands on its own and cites no repository note.** Note that
   `main.tex` correctly never cites `106_11`; consequently the paper must
   carry the whole construction, and with 2.4 unrepaired it does not.
2. *Mertens companion statement quoted, not proved.* Handled correctly.
   Remark 10.8 (lines 1862–1879) states it as a quotation with the precise
   reference \cite{P43}, Theorem 10.8b, says what it is used for, and gives a
   deletion test. I verified the deletion test by inspection: no proof in
   §§8–12 invokes Remark 10.8 or Proposition 10.7. (E8) appears in the
   appendix with the same restriction. **No theorem of this paper depends on
   it.** Acceptable as written.
3. *Place-wise Plancherel import.* **Not** handled correctly: Finding 2.2
   (MAJOR). The statement is correct as written; the citation is wrong/absent.
4. *Prime packet re-using a cited proof outside its hypothesis.* The argument
   is correct; Finding 2.10 (MINOR) is a presentation repair.
5. *The swap remark restated.* Handled correctly. Remark 7.2 (lines 960–979)
   makes no existence claim; the $\sigma$-invariance of $\beta_T$ is proved
   inline in one display, which I checked. The concluding sentence about which
   isotropic direction the spread families approximate is cited to \cite{P43},
   Theorem 9.14a. Acceptable.

---

## 4. Compile

`pdflatex -interaction=nonstopmode main.tex`, twice, in
`04-papers/45-row-c-explicit-formula/`.

* Errors: **0**.
* LaTeX warnings: **0**. No undefined references, no undefined citations, no
  rerun-needed warning after the second pass.
* Overfull/underfull boxes: **0**.
* Output: 31 pages.

**Finding 4.1 — MINOR.** `main.log` contains **97** instances of
`pdfTeX warning (ext4): destination with the same identifier
(name{equation.N.M}) has been already used, duplicate ignored`. Cause: the
paper numbers its displays by hand with `\tag{3.1}`, `\tag{6.1}`, `\tag{8.1}`,
… while the `equation` counter runs independently, so hyperref emits colliding
anchors. Consequence: some equation hyperlinks in `main.pdf` point at the
wrong display. *Fix:* either use `\tag*` / drop `\tag` in favour of real
`\label`ed equations, or add `\usepackage{hyperref}` option-level
`\renewcommand{\theequation}{\thesection.\arabic{equation}}` and let LaTeX
number the displays. Note that `TEX_CONVERSION_NOTES.md` line 5 claims "zero
errors, zero LaTeX warnings, zero overfull/underfull boxes" — true of LaTeX
warnings, but the notes do not mention these 97 pdfTeX warnings.

---

## 5. Style

Preamble, geometry, `microtype`, `booktabs`/`tabularx`, theorem environments
and the `\newcolumntype{Y}` definition are byte-identical to Paper 42 except
for the macro list, which is adapted to this paper's objects. Author line and
`\thanks` match Paper 42. The title names what is constructed ("An Explicit
Formula and a Comparison Theorem for the Canonical Trace on a Correspondence
Algebra of the Idele Class Group") and contains no internal vocabulary.
Sectioning, appendices and bibliography are in the house style; the ten
references are real and correctly formatted.

**Finding 5.1 — MINOR (AI-flavoured / meta prose).** Line 962: "It is worth
stating explicitly that $M(\Gamma_F)$ is the *swap* …"; line 1497:
"Corollary~\ref{cor:c-unique} should be read as saying two things at once";
lines 1594 and 2374: "For the reader's convenience we tabulate" / "For the
reader's orientation we record"; line 838 "Propositions 6.2 and 6.3 are
computations recorded for orientation"; line 795 "This is a consistency check
rather than a discovery". Each is an instruction to the reader about how to
read the paper rather than mathematics. *Fix:* delete the framing clauses and
keep the statements ("$M(\Gamma_F)=\sigma(\Phi_F(0),\Phi_F(1))$, the swap of
the pair …").

**Finding 5.2 — MINOR.** The table on lines 1596–1616 and the appendix cite
"Theorem~\ref{thm:EF}(b),(c)" as though (a)–(c) were parts of the theorem;
they are steps of its proof. *Fix:* "step (b) of the proof of
Theorem~\ref{thm:EF}".

---

## Summary of findings

| # | Severity | Location | Issue |
|---|---|---|---|
| 2.1 / 3.x | MAJOR | 980–992 | Proposition 7.3 has neither proof nor citation |
| 2.2 | MAJOR | 360, 386–389 | Place-wise Plancherel (the load-bearing import of Theorems A and G) cited to the wrong P43 number |
| 2.3 / 3.1 | MAJOR | 79–80, 192–194, 1678 | "$A$ has exactly two poles" — false, and stronger than the proved statement (which says "in $\{0,1\}$") |
| 2.4 | MAJOR | 2021 | Step 2 of Theorem F cites (11.6) with $M=0$, which gives boundedness, not the required smallness (11.7) |
| 1.1, 1.2, 2.6–2.11, 3.2, 4.1, 5.1, 5.2 | MINOR | various | see above |

No BLOCKING finding. No use of the Riemann hypothesis or of a zero-free
assumption anywhere; no circularity; the explicit formula, the comparison
theorem, the residue theorem, the sufficiency theorem and the radical theorem
are all correct as mathematics, subject to the four repairs above.

## Verdict

**MAJOR REPAIRS NEEDED.**

The mathematics is sound and the constants check against the classical Weil
formula by independent derivation. But the paper as printed contains a false
statement in its abstract and in its statement of Theorem E (2.3), one
proposition asserted with no proof and no source (2.1), one wrong citation for
the single import on which its Theorem A rests (2.2), and one unjustified step
inside the proof the converter rewrote and which therefore has no external
fallback (2.4). All four repairs are local — four sentences in total — but
each is a defect of the kind this paper's contract forbids, and none can be
left to the reader.

---

# Review R2 — confirmation round

Re-checked against the current `main.tex` (2465 lines) directly; the writer's
account in `TEX_CONVERSION_NOTES.md` §"Repairs after review R1" was not taken
on trust. Every repair was read in situ and, where it is a mathematical
statement, re-derived.

## Per-finding status

| # | Sev. | Status | Verification |
|---|---|---|---|
| **2.3 / 3.1** | MAJOR | **FIXED** | Abstract (l. 77–78) now reads "has exactly two poles in $\{0,1\}$, both simple and each of residue $1$". Theorem E (l. 190–193) reads "exactly two poles in $\{0,1\}$, both simple and both of residue $1$ --- its remaining poles are the zeros of $\xi$, contributed by $-\xi'/\xi$". The added clause is **correct**: $A=-\xi'/\xi+1/s+1/(s-1)$, $\xi$ entire, so the poles of $A$ are $s=0$, $s=1$ and the zeros of $\xi$ (the poles at $s=-2n$ cancel between $-\tfrac12\psi(s/2)$ and $-\zeta'/\zeta$). §10.2 is retitled "The continued symbol and its poles at $s=0$ and $s=1$" (l. 1694). Theorem 10.3(ii) (l. 1727) unchanged and still hedged. Abstract, introduction, section title and theorem body now agree with each other and with `main.md` Thm 9bis.2′(ii). |
| **2.1** | MAJOR | **FIXED** | Proposition 7.3 (l. 985–1003) now carries the header `[\cite{P43}, Theorems 9.13(a), 9.14a--9.14c′ and Definition 9.14c0]`, the $L^1$-mass clause cites Definition 9.14c0 in the text, and a proof environment was added attributing the three assertions in order to Thm 9.13(a), Thms 9.14a/9.14c, and Def. 9.14c0 + Thm 9.14c′. The attribution matches `main.md` Prop 8.3 and Rem 12.3. No dependency changed. |
| **2.2** | MAJOR | **FIXED** | Proposition 2.4's header (l. 359–360) is now `[\cite{P43}, Theorem 9.7, equation (9.11), Theorem 9.7(d′)/(9.13′), and (14.2)]`, and part (c) ends (l. 384–386) "The place-wise form is \cite{P43}, Theorem 9.7(d′), equation (9.13′); Lemma 4.2 and Theorem 12.2 rest on it." This is exactly the number `main.md` (l. 612–617) identifies, and the two dependent results are named. |
| **2.4** | MAJOR | **FIXED, and the bound checked** | Step 2 (l. 2037–2040) now reads "In particular (11.6) with $M=1$ gives $|D(z)|\le C_1/(1+|\Rel z|)$ in the strip $|\Iml z|\le\tfrac12$, so that $|D(z)|\to0$ as $|\Rel z|\to\infty$ there; fix $R>|x_0|+1$ such that …". This does deliver (11.7): $D(z_0)\ne0$ is fixed first, so $|D(z)|\to 0$ in the tail of the strip gives an $R$ with $\sup|D(z)|/|D(z_0)|\le\tfrac12$ for $|\Rel z|\ge R$, and the extra requirement that no zero have $|\Rel z|=R$ costs nothing. The "order matters" sentence is retained, correctly. |
| **Lemma 4.2 inline shell computation** (repair of 2.10) | — | **FIXED, and the computation checked** | l. 683–698. The unit-packet step is now derived inline with no reference to "step (i)" of a cited proof. The shell part is computed from three ingredients, each cited or immediate: $\tau_p\equiv p^{-|k|/2}$ on $p^k\Z_p^\times$ (\cite{P43}, Lemma 8.2(i)); $|j_p(p^ku)|_S=p^{-k}$ for $u\in\Z_p^\times$; $\vol_{d^*x}(p^k\Z_p^\times)=\log p$. The display $\sum_{k\ne0}(\log p)p^{-|k|/2}h(k\log p)=\sum_{k\ge1}(\log p)p^{-k/2}[h(k\log p)+h(-k\log p)]$ is correct (split $k>0$/$k<0$, $|k|=k$), agrees with (4.3), and the profile value $h(k\log p)$ is right since $\Gamma_h(w)=h(-\log|w|_S)$ and $-\log p^{-k}=k\log p$. The modulus $|j_p(p^ku)|_S=p^{-k}$ is the class computation under the splitting (2.1) (the archimedean coordinate of the $\ker\varphi$ representative after dividing by the $S$-unit $p^k$) and is consistent with the $k=0$ case $|j_p(u)|_S=1$ used three lines above; correct as written. The lemma now imports only *statements*. |
| 1.1 | MINOR | **FIXED** | `problem` and `conjecture` environments deleted from the preamble (l. 14–21). |
| 1.2 | MINOR | **FIXED** | "standing caution" (now l. 460–461), "recorded as strongly as the positive half" (l. 766–769), Remark 9.5's "two things at once" (l. 1512–1521), Remark 10.8's "deletion test" phrasing (l. 1888) all removed; the mathematical content is kept verbatim in each case. |
| 2.6 | MINOR | **FIXED** | Corollary 8.5 (l. 1316–1321) now invokes $|g|\le C_4e^{2T|\sigma-1/2|}|s-\tfrac12|^{-4}$, "(8.1) with $N=4$", and states explicitly that this replaces (8.2), "which was derived from a product of two transforms and is not available for a single one". Correct: $N=4$ is exactly what the horizontal estimate of Lemma 8.2 consumes. |
| 2.7 | MINOR | **FIXED** | Remark 8.6 (l. 1325–1334) restricts the decay bound to $|\gamma_\rho|\ge1$ and handles the finitely many zeros of smaller ordinate separately. |
| 2.8 | MINOR | **FIXED (math), new editorial defect (see NEW-1)** | "Fix any integer $N_0\ge1$" (l. 2145); "$|D(-z)|=|D(z)|$ because $\varphi$ is even, so that (11.7) applies to both factors" inserted before the tail display (l. 2157–2158). Both are correct and both were the missing links. |
| 2.9 | MINOR | **FIXED** | Theorem 12.2's clause (l. 2214–2215) is now "on which the restriction of $M$ is still surjective onto $\BT$", and the proof (l. 2257–2267) proves it: $M(\Gamma_h)=(\int he^{t/2},\int he^{-t/2})$, and $\alpha e^{t/2}+\beta e^{-t/2}\equiv0\Rightarrow\alpha=\beta=0$. It also records that Proposition 2.5 is a different statement. Correct. |
| 2.10 | MINOR | **FIXED** | See the Lemma 4.2 row above. |
| 2.11 | MINOR | **FIXED** | Appendix B (l. 2405–2426): Theorem 6.5 removed from "Proved here" and listed among the quoted results as "the symbol identity (6.2) of Theorem 6.5, of which only the constant reconciliation is proved here". |
| 3.2 | MINOR | **FIXED** | Proposition 2.4(d) (l. 389) now cites \cite{P43}, equation (14.2) for the lower bound. |
| 4.1 | MINOR | **FIXED** | `\usepackage[hypertexnames=false]{hyperref}` (l. 8). Clean rebuild (`rm` of all aux files, three passes): `grep -c "pdfTeX warning" main.log` = **0**. |
| 5.1 | MINOR | **FIXED** | "It is worth stating explicitly", "For the reader's convenience/orientation", "recorded for orientation" all removed. The retained "Since $N_\Gamma$ is defined by its spectrum, this is a consistency check on …" (l. 802) and Remark 10.9's "It is tempting to imagine" are statements about the mathematics, not about the writing; acceptable. |
| 5.2 | MINOR | **PARTLY FIXED** — see NEW-2 | The order-of-limits table (l. 1624) now reads "steps (b) and (c) of the proof of Theorem 8.4", and §10's opening says "step (a) of the proof of Theorem 8.4". But Appendix A still cites proof steps as if they were theorem parts at three places: l. 2308 "Theorem~\ref{thm:EF}(c)" in (E1), l. 2359 "\ref{thm:EF}(b)" in (E4), l. 2365 "Theorem~\ref{thm:EF}(c)" in (E5). |

## New issues introduced by the repairs

**NEW-1 — MINOR (editorial, visible in the PDF).** Lines 2145–2155, Step 8 of
the proof of Theorem 11.3. The justification of (11.12) is now given twice, and
the second copy is a sentence fragment beginning in lower case immediately
after a display that ends in a full stop:

> "Fix any integer $N_0\ge1$.  By the strip decay (11.6) with $M$ large
> together with the zero count … of (E3d), \[ \Sigma_0:=\dots<\infty. \]
> **the sum $\Sigma_0$ is finite:** the factor $(|D(z)|/|D(z_0)|)^{2N_0}$
> decays faster than any power of $|\Rel z|$ in the strip, since $N_0\ge1$ and
> (11.6) holds for every $M$, while the number of zeros with
> $|\Rel z|\in[X,X+1]$ is $O(\log X)$."

The mathematics is right (and the count $O(\log X)$ per unit interval is (E3b),
which is imported; the global $O(X\log X)$ of (E3d) would also suffice by
partial summation). *Fix:* delete the lead-in "By the strip decay (11.6) with
$M$ large together with the zero count … of (E3d)," and let the sentence after
the display carry the justification, capitalised: "The sum $\Sigma_0$ is
finite: the factor …".

**NEW-2 — MINOR (residue of finding 5.2).** Appendix A, lines 2308, 2359, 2365:
`Theorem~\ref{thm:EF}(c)`, `\ref{thm:EF}(b)`. Theorem 8.4 has no parts (b),
(c); these are steps of its proof. *Fix:* "step (c) of the proof of
Theorem~\ref{thm:EF}", etc., as already done in the table and in §10.

No other change introduced an error. I re-read every repaired passage in
context and re-derived the four mathematical repairs (2.4, 2.9, 2.10, and the
added clause of Theorem E); all four are correct. Nothing was strengthened
beyond the Markdown's proved set by the repairs, and no statement lost a
hypothesis.

## Forbidden vocabulary — re-checked on the repaired file

`grep -n -i -E "riemann hypothesis|\bRH\b|critical line|phase|row |round|
construction|auditor|honest|candidly|PROVED|P1[0-9][0-9]|106_|programme|corpus|
repositor|of record|ledger|withdraw|acceptance|contract|status|conjectur"`,
with `\label{...}` lines filtered out: the only matches are the ordinary
English verb "proved" (14 occurrences, all legitimate). The words "conjecture"
and "hypothesis" no longer occur anywhere in the file, the unused `conjecture`
environment having been deleted. The repairs introduced no new vocabulary
defect, and the new Theorem E clause names $\xi$ and its zeros, not any
conjecture about them.

## Compile from clean

All auxiliary files deleted, then three `pdflatex -interaction=nonstopmode`
passes:

* errors **0**
* LaTeX warnings **0** (no undefined references, no undefined citations, no
  rerun request)
* pdfTeX warnings **0** (the 97 duplicate-destination warnings are gone)
* overfull/underfull boxes **0**
* output 31 pages

## Verdict R2

**ACCEPT.**

All four MAJOR findings are fixed, correctly and without collateral damage; all
twelve MINOR findings are fixed except the three Appendix A cross-references of
5.2 (NEW-2). What remains is two purely editorial corrections with no
mathematical content — NEW-1 (a duplicated, lower-case-starting sentence in
Step 8 of §11) and NEW-2 (three "Theorem 8.4(b),(c)" that should read "step (b)
of the proof of Theorem 8.4") — which should be made at proof stage but do not
affect the correctness, the completeness of any proof, the fidelity to the
proved set, or the compile.
