# Doc 140 — Adversarial audit: the Weil–Toeplitz algebra, the visibility trichotomy, and the Fredholm theorem

**Program:** Riemann Hypothesis — Phase 46: AUDIT AND ATTACKS.
**Role of the document:** purely adversarial. Mandate: destroy. Audited objects: Doc 134 (symbol/compact,
trichotomy, Thm 1.3), Doc 132 (B.4, Theorem D, Witt), and the operator-theoretic sections of P47
(`06-papers/P47-weil-toeplitz-logistic/main.tex`, §§2–4 and thm:exact/thm:strict/thm:thin/thm:blind/thm:nogo).
**Method:** line-by-line re-derivation of every proof, search for degenerate cases, explicit
counterexamples in closed form. No numerics. Backward-only citations (corpus + Kato, Reed–Simon, Murphy,
Bognár, Iohvidov–Kreĭn–Langer, Böttcher–Silbermann, Rabinovich–Roch–Silbermann).

---

## 0. VERDICT PER PIECE

| piece | object | verdict |
|---|---|---|
| **(a)** | Thm 1.3 (D134) / thm:exact (P47): $\delta(G+K)<\infty\ \forall K$ compact ⟺ strict essential positivity | **SURVIVES.** Correct proof in all three directions, including the limiting case $\mu=0$. One cosmetic erratum (the $n_0=4$ is unnecessarily conservative; $n_0=1$ holds). Scope: $G=G^*$ **bounded** — the restriction is load-bearing and is stated (Def. 2.4 D132), but see §2 below: the application to $Z_\zeta$ is outside the proved scope. |
| **(b)** | B.4 (D132): essential positivity ⟹ $\delta<\infty$, stable under compacts | **SURVIVES** as a theorem over Hilbert-type $G$. **SURVIVES WITH WARNING** as a tool of the program: essential positivity is NOT an invariant of the Weil form — it is an invariant of the pair (form, Hilbert norm), and Doc 134 itself (Theorem 2.2) proves that in the natural normalization the statement is vacuous. The document knows this; the risk is that future citations will forget it. |
| **(c)** | $\mathcal W$, $\mathcal J$, corona, symbol; Lemmas 3.2–3.3; **Thm 5.2 / trichotomy** | The C\* skeleton **SURVIVES** intact (§1). Thm 5.2 **SURVIVES WITH ERRATA** (clause (iv) of D134 fails in the degenerate case and the proof itself admits it; P47 already removed it). **Thm 5.3 DIES IN ITS NOISY CLAUSE**: the exception "$\vartheta_n\le\omega_n$ eventually" is FALSE — counterexample in §4.2; the corrected version (without exception) is cleaner and everything downstream survives. The phrase "the zeros live on the boundary" is a **THEOREM-IN-MODEL for pure strata, METAPHOR as a global statement about ζ** (the fat/thin/sub-resolution classes are relative to the schedule; Thm 5.5 itself says so). Thm 5.4 is a **near-axiom disguised as a theorem** inside $\mathfrak W$ (§4.3). |
| **(d)** | $\delta=1$ forbidden (Theorem D.4, D132) | **SURVIVES WITH SCOPE CAVEAT.** The proof is correct. But the hypothesis $z^2\notin\mathbb R$ is load-bearing and excludes exactly the cases the protocol asks about: real spectrum (Siegel type) and the fixed point $z=0$ ($s=\tfrac12$). The slogan "the functional symmetry forces parity" is false without that hypothesis (counterexample §5.2). For ζ it is harmless (ζ has no real zeros in $(0,1)$); for the general category it is NOT. |
| **(e)** | $\mathcal K_{\mathrm{off}}$ Witt-trivial (D132 §8.2(b)) | **SURVIVES for $m<\infty$; slippage for $m=\infty$.** The chain D.1→D.2→D.4→E.2 is correct in finite dimension. The phrase "lives in the absorbing ideal" uses finite-dimensional Witt theory (E.2); under $\neg$RH with $m=\infty$ the signature $(\infty,\infty)$ is not covered by E.2 and the statement must be read by truncation. It also depends on the nondegeneracy of $Q|_{\mathcal K_{\mathrm{off}}}$, inherited from the model. |

**No error that topples the architecture was found.** Found: one repairable false statement
(noisy Thm 5.3), one admitted-and-failing clause (5.2(iv)), two language slippages ("continuous
field", "the zeros live on the boundary" as global), and two scope boundaries the corpus must
respect in perpetuity ($G$ bounded; $z^2\notin\mathbb R$).

---

## 1. C\* verification of $\mathcal W$ (protocol 1)

### 1.1. Is $\mathcal W$ genuinely a C\*-algebra? — YES

$\mathcal W=\prod^b_n\mathcal B(H_n)$ with $\|A\|=\sup_n\|A_n\|$ and pointwise operations is the
**$\ell^\infty$-product of C\*-algebras**: completeness (uniform limit of sections bounded
componentwise), $\|A^*A\|=\sup_n\|A_n^*A_n\|=\sup_n\|A_n\|^2=\|A\|^2$ (the C\* identity passes to the sup
because it holds in each component and the sup of squares is the square of the sup for nonnegatives).
Standard [Murphy, *C\*-Algebras and Operator Theory*, §1; Dixmier, *C\*-algèbres*, §1.9]. No objection.

### 1.2. Is $\mathcal J$ a closed two-sided ideal? — YES

$\mathcal J=\{A:\|A_n\|\to0\}$: (i) closed subspace — if $A^{(k)}\to A$ in sup-norm with
$\|A^{(k)}_n\|\to_n0$, then $\limsup_n\|A_n\|\leq\|A-A^{(k)}\|\to_k0$; (ii) two-sided —
$\|B_nA_n\|,\|A_nB_n\|\leq\|B\|\,\|A_n\|\to0$. It is the $c_0$ direct sum,
$\bigoplus_{c_0}\mathcal B(H_n)$. No objection.

### 1.3. Is the symbol a well-defined \*-homomorphism? — YES, trivially

$\sigma:\mathcal W\to\mathcal C=\mathcal W/\mathcal J$ is the canonical C\* quotient: a surjective
\*-homomorphism of norm 1. There is nothing to check beyond 1.1–1.2. The identification with the Calkin
algebra: $\bigoplus_nA_n$ is compact on $\bigoplus_nH_n$ ⟺ $\|A_n\|\to0$ (each block is finite-dimensional,
hence compact; the tail dominates the distance to finite ranks) — correct. And the inclusion
$\mathcal W/\mathcal J\hookrightarrow$ Calkin$(\bigoplus H_n)$ is a unital \*-monomorphism
($\ker=\mathcal W\cap\mathcal K=\mathcal J$), hence **isometric and spectrally permanent**
[Murphy, Thm. 2.1.11, Thm. 3.1.5]: $\mathrm{spec}_{\mathcal C}(\sigma(A))=\mathrm{spec_{ess}}(\bigoplus A_n)$.
This validates the phrase "essential spectrum of the family" with total precision. No objection.

### 1.4. "Continuous field" in Dixmier's sense? — NO, and it is a (minor) language slippage

A Dixmier continuous field requires a topological base and continuity conditions on $n\mapsto\|A_n\|$.
Here the base is **discrete** $\mathbb N$: every bounded section is vacuously "continuous". Doc 134 §3
defines the object precisely and does not claim Dixmier structure; but **P47's abstract** says
"continuous field of finite-dimensional Hilbert spaces" — technically true and mathematically vacuous
over a discrete base. **Declared slippage:** the word "continuous" carries no content; it should say
"$\ell^\infty$-product" or "field over $\mathbb N$". It does not affect any theorem (no proof uses
continuity).

### 1.5. Lemmas 3.2–3.3 re-derived — CORRECT

**Lemma 3.2** ($\|\sigma(A)\|=\limsup\|A_n\|$): both inequalities verified; it is the diagonal case of
computing the essential norm by truncation. Correct. (It is also the classical fact
$\ell^\infty/c_0$-norm = $\limsup$.)

**Lemma 3.3** (spectrum of the symbol = limit set of the window spectra): re-derived. The
($\supseteq$ by contrapositive) direction correctly uses that for self-adjoint operators
$\|(A_n-\lambda)^{-1}\|=\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)^{-1}$; the ($\subseteq$)
direction constructs the inverse by windows with a uniformly bounded tail and a finite-support remainder. Correct.
Fine point verified: the left and right invertibility of $(A_n-\lambda)B_n$,
$B_n(A_n-\lambda)$ for large $n$ does give invertibility of $A_n-\lambda$ (right inverse + left
inverse ⟹ invertible). It is the diagonal-trivial case of RRS's limit-operator theory, as the
document frankly states. **Corollary 3.4 is correct** and the identification uniform-quantifier =
strict positivity of the symbol is exact (no metaphor): verified by reading 3.3 twice, with the fine
point that "weak" ⟺ $\liminf_n\lambda_{\min}(A_n)\geq0$ (a bounded sequence with
$\lambda_{\min}(A_{n_k})\leq-\varepsilon$ infinitely often produces a limit point $\leq-\varepsilon$).

**Verdict §1: the C\*-algebraic skeleton is impeccable.** What is NOT a theorem is the Weil instance of the
field (Def. 3.6): the boundedness $\sup_n\|Q_n\|<\infty$ is GAP-134.R, declared. Correctly labeled.

---

## 2. Re-derivation of B.4, with the domain/boundedness issue made explicit (protocol 2)

### 2.1. The theorem as stated — CORRECT

D132 Def. 2.4 restricts to objects **of Hilbert type**: $Q_C(x,y)=\langle Gx,y\rangle$ with
$G=G^*\in\mathcal B(H)$ **bounded**. Under that hypothesis:

1. **Lemma 4.1** ($\delta=\dim\mathrm{ran}\,E_G(-\infty,0)$): re-derived; the injectivity of
   $E_G(-\infty,0)|_N$ for $N$ negative is correct. ✓
2. **B.4:** $\mathrm{spec_{ess}}(G)\subseteq(0,\infty)$ with $G$ bounded ⟹ $\mathrm{spec_{ess}}$ is
   **compact** nonempty ⟹ automatically $\subseteq[c,\infty)$ with $c>0$ (Obs. 1.2 of D134 — the document
   detected this point itself). Then $\mathrm{spec}(G)\cap(-\infty,0]$ is compact, discrete (accumulation
   points would go to the essential spectrum), finite, of finite multiplicities: $\delta(G)<\infty$.
   Weyl [Kato, Thm. IV.5.35] gives stability under compact $K$. ✓ No error.

### 2.2. The point the protocol flagged as most likely to fail — and how the documents dodge it (and where they do NOT)

**The argument "infinite-rank negative part ⟹ negative essential spectrum" requires three things:**
an operator (not just a form), self-adjoint, **bounded** (or at least semibounded with a closed form domain).
For unbounded quadratic forms the chain breaks in two places: (i) without an operator representation
(KLMN requires semiboundedness + relative closability) not even $E_G$ exists; (ii) for unbounded $G$
with $\mathrm{spec_{ess}}\subseteq(0,\infty)$, the essential spectrum is closed but **not compact**, and
$\subseteq(0,\infty)$ no longer implies a gap (e.g.: essential spectrum $\{1/n\}_n\cup[1,\infty)$… it is not
closed; but $\overline{\{1/n\}}\ni0$ — the point is that without compactness Obs. 1.2 fails and weak/strict
must be distinguished by hand). **The documents do NOT make this error**: all B theorems are under Def. 2.4
(G bounded). The Pontryagin issue: in a Pontryagin space $\Pi_\kappa$ with a Hilbert majorant, the
Gram $J$ of the form is bounded and invertible [Bognár, *Indefinite Inner Product Spaces*, Ch. V;
Iohvidov–Kreĭn–Langer, §1], so instance (I1) is of Hilbert type **if** the P35 realization
delivers the majorant — which is exactly the declared bridge conjecture P35.

**Where the slippage DOES threaten:** DESIDERATUM 8.D1 ("prove that the Gram of the Weil form is
essentially positive") is phrased as if "the Gram of the Weil form" were a single object. It is
not: **essential positivity is an invariant of the pair (form, Hilbert inner product), not of the
form**. Doc 134 itself proves this in the hardest possible way: Theorem 2.2 (in fixed weight the gap
dies unconditionally, empty certificate) versus §3–5 (in window normalization the sea has gap
$1-r$ but the certificate loses completeness). My re-derivation of Theorem 2.2 via Lemma 1.5: correct
(the gap detector by orthonormal sequences is Weyl's criterion in quadratic form; the proof with
$E$ of finite rank and $u_n\rightharpoonup0$ is standard and flawless). **Adversarial conclusion:** B.4
survives as a theorem; "essential positivity of the Weil Gram" as a program objective is an
**incomplete statement until the realization is fixed**, and the two honest known realizations either
fail or remain conditional (Thm 2.2 / GAP-134.R). This is not an error of the documents — it is their
central finding — but it is logged as a **mandatory citation rule**: no future invocation of B.4/8.D1
without specifying the norm.

### 2.3. Delimiting counterexample re-verified

$G=\mathrm{diag}(-1/n)$: $\mathrm{spec_{ess}}=\{0\}$, weakly positive, $\delta=\infty$. Correct, and
by Thm 1.3 it is the generic case. ✓

---

## 3. Thm 1.3 / thm:exact, both directions (protocol 3)

### 3.1. (i)⟹(ii) and (iii)⟺(i) — CORRECT

(i)⟹(ii) is B.4 (§2.1). (iii)⟺(i): $\delta(G-\varepsilon I)=\dim\mathrm{ran}\,E_G(-\infty,\varepsilon)$
(translation of the spectral measure, exact); finiteness ⟺ $\mathrm{spec}(G)\cap(-\infty,\varepsilon)$
finite with finite multiplicities ⟺ $\mathrm{spec_{ess}}\subseteq[\varepsilon,\infty)$. ✓

### 3.2. (ii)⟹(i), the new direction — CORRECT, re-derived step by step

Let $\mu\in\mathrm{spec_{ess}}(G)$, $\mu\leq0$ (the negation of strictness for bounded $G$ is exactly
this, by compactness of $\mathrm{spec_{ess}}$).

- **Step 1.** $\dim\mathrm{ran}\,E_G(\mu-\epsilon,\mu+\epsilon)=\infty$ for every $\epsilon>0$: this is the
  characterization of the essential spectrum of self-adjoint operators [Reed–Simon IV, §XIII.4]. The
  inductive orthonormal choice with $\|(G-\mu)e_n\|\leq8^{-n}$: correct (the spectral integral estimate is exact). ✓
- **Step 2.** $|\langle Ge_n,e_m\rangle|\leq8^{-\max(n,m)}$ for $n\neq m$: verified via both routes
  (self-adjointness gives the two bounds $8^{-n}$ and $8^{-m}$). Diagonal:
  $\langle Ge_n,e_n\rangle=\mu+\langle(G-\mu)e_n,e_n\rangle\leq\mu+8^{-n}\leq8^{-n}$ using $\mu\leq0$. ✓
- **Step 3.** $K=-\sum2^{-n}\langle\cdot,e_n\rangle e_n$ compact self-adjoint. Bound on the cross term
  via row-wise Schur: $r_n\leq(n+1)8^{-n}$ — re-derived, correct (and valid for full $\ell^2$
  vectors, not just finite support, so the negativity extends to the closed span; for
  $\delta=\infty$ the algebraic span suffices). Final coefficient $(n+2)8^{-n}-2^{-n}<0$ ⟺ $n+2<4^n$, which
  holds for **every $n\geq1$** — the document's $n_0=4$ is unnecessary (cosmetic erratum, not an error). ✓

**The protocol's question** ("what happens if $0\in\mathrm{spec_{ess}}$ but there is no essential
negative part?"): this is exactly the case $\mu=0$, and the construction covers it without modification — the
diagonal remains $\leq8^{-n}$ and the perturbation $-2^{-n}$ dominates. It is the attack "diag$(+1/n)$ plus
a compact that sinks it." **The document anticipated and resolved the most likely failure point.** The
equivalence is genuinely exact and the "for every compact" quantifier is necessary (without it, (ii) with
$K=0$ does not imply (i): diag$(-1/n)$ has… no: diag$(-1/n)$ already has $\delta=\infty$ with $K=0$; the
correct example is diag$(+1/n)$: $\delta(G)=0$ but $\delta(G+K)=\infty$ for the $K$ of Step 3 — non-robust
finiteness does exist, the quantifier is not decorative). ✓

**Verdict: (a) SURVIVES.** It is, together with Lemmas 3.2–3.3, the most solid piece of the package.

---

## 4. The trichotomy (protocol 4)

### 4.1. Are "fat/thin/sub-resolution" defined without reference to RH? — YES, but NOT without reference to the schedule

The classes are defined by $\delta_j\,a(\gamma_j)$ — data of the configuration $Z$ and of the schedule $a$,
zero reference to RH or to primes. ✓ But **they are not intrinsic to the zeros**: the same quadruple is fat
for one schedule and sub-resolution for another (Thm 5.5(b): every quadruple is fat for some $a$). The
document itself turns this into a theorem (5.5: $m=\sup_a m_a$, resolution quantifier). Therefore the
headline phrase **"the zeros live on the symbol/compact boundary" is:**

- **A THEOREM within $\mathfrak W$ for pure-stratum thin-visible configurations** (Thm 5.2(i)–(iii),
  verified below): the negatives accumulate at $0\in\mathrm{spec}(\sigma(Q))$;
- **A METAPHOR as a global statement about the zeros of ζ**: (1) the strata are relative to $a$; (2) the
  fat ones do NOT live on the boundary (they live in the negative interior of the symbol, 5.1) and the
  sub-resolution ones do NOT live on the boundary (they live in the ideal, 5.4) — the exact phrase would be
  "the intermediate stratum lives on the boundary"; (3) the Weil instance of axioms (S1)–(S3),(V2) is
  mixed/GAP (table Obs. 4.5, declared). Observation 5.6 of Doc 134 is frank (per-stratum table); the headline
  of the summary and of P47 (Remark rem:trichotomy: "off-critical zeros live exactly on the symbol/compact
  boundary") **elevates the intermediate stratum to global**. A declared rhetorical slippage; there is no
  mathematical error behind it because the formal statements are indeed stratified.

### 4.2. THE MAIN FINDING: Theorem 5.3 (noisy case) is FALSE as stated

**Audited statement** (D134 Thm 5.3(ii); P47 thm:strict, parenthetical): with noise $\omega_n\to0$, strict
positivity of the symbol is equivalent to the visible windows eventually ending, *except at most windows
whose maximal visibility satisfies $\vartheta_n\to0$ and $\vartheta_n\leq\omega_n$ eventually* — i.e.,
the statement claims that infinitely many populated windows "below the noise" **are compatible with**
strict positivity of the symbol.

**Refutation (closed form).** Suppose $J_n^{\mathrm{vis}}\neq\emptyset$ for infinitely many $n$, with
$\vartheta_n>0$ arbitrary (in particular $\vartheta_n\leq\omega_n$). In $\mathfrak W$, the matrix
$Q_n-C_n$ has the exact eigenvalue $-\vartheta_n$ (hyperbolic block). By finite-dimensional Weyl
[Bhatia], $Q_n$ has an eigenvalue $\mu_n\in[-\vartheta_n-\omega_n,\,-\vartheta_n+\omega_n]$. The sequence
$(\mu_n)$ over the populated windows is bounded; let $\ell$ be any accumulation point. Then
$$\ell\;\leq\;\limsup_n\,(-\vartheta_n+\omega_n)\;\leq\;\limsup_n\,\omega_n\;=\;0 .$$
By Lemma 3.3, $\ell\in\mathrm{spec}(\sigma(Q))\cap(-\infty,0]$: **strict positivity FAILS,
whenever there are infinitely many visible windows, regardless of the comparison $\vartheta_n$ vs $\omega_n$.**
Explicit instance satisfying the exception clause and refuting the equivalence: $\omega_n=1/n$,
a population at every even $n$ with $\vartheta_n=1/(2n)$; the block's perturbed eigenvalues lie in
$[-3/(2n),\,1/(2n)]\to0$, so $0\in\mathrm{spec}(\sigma(Q))$ and there is no gap — but the theorem's
clause declares this compatible with strictness. Contradiction.

**Diagnosis.** The error is in the last line of D134's proof ("eigenvalues reabsorbed to the positive
side"): that the eigenvalue may be $\geq0$ window by window does not prevent it from tending to $0$, and
$0$ as a limit point already kills strictness (Lemma 3.3). The correct intuition being pursued is "below
the noise the block should not be in the model" — a legitimate modeling defense, but then the statement
must modify **Definition 4.4** ($J_n^{\mathrm{vis}}$ with threshold $\theta_j>\omega$), not
add a false exception to the theorem.

**Repair (and it is an improvement).** The correct statement, proved by the argument above plus the
clean direction ($J_n^{\mathrm{vis}}=\emptyset$ eventually ⟹
$\mathrm{spec}(Q_n)\subseteq[1-r-\omega_n,1+r+\omega_n]$ ⟹ $\Lambda(Q)\subseteq[1-r,1+r]$):

> **Thm 5.3′ (corrected, noisy case included).** Strict positivity of the symbol ⟺
> $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$. No exception clause.

The corrected equivalence is **stronger and cleaner**; Cor. 5.3bis (quantitative bound
$m_a^{\mathrm{vis}}\ll N_0\log N_0$), the LP-134 route (which uses 5.1+5.3 with the gap (V2) $\theta\geq c_0$,
a regime where the clause was never invoked) and Thm 7.2 survive unchanged. **Erratum to propagate:
D134 Thm 5.3(ii) and P47 thm:strict (parenthetical) — add to 06-papers/ERRATA.md.**

### 4.3. Thm 5.2 — SURVIVES WITH ERRATA (clause (iv))

(i)–(iii) re-derived: correct within $\mathfrak W$ (with the fine point that (i) requires
$\vartheta_n>\omega_n$ on infinitely many windows for the limiting eigenvalues to be *genuinely
negative*; otherwise $0\in\Lambda$ holds just the same as a limit of eigenvalues of uncontrolled sign — the
accumulation at $0$ and the failure of strictness (iii) hold in all cases; the phrase "attained as a
limit of negative eigenvalues" requires the sub-hypothesis). **(iv)** ($\delta=\infty$ in the field's
direct sum): D134's own proof admits midway that "in that degenerate case per-window negativity may be
lost" and redirects to the level of the full form — i.e., **statement (iv) as formulated is not proved in
the degenerate case** $\vartheta_n\leq\omega_n$ a.e. P47 removed (iv) from thm:thin: the correction has
already been carried out in the paper. For D134: restrict (iv) to
"$\vartheta_n>\omega_n$ on infinitely many populated windows, or read $\delta$ at the level of the full form."

### 4.4. Thm 5.4 — TRUE but with mostly axiomatic content; it should be labeled accordingly

In $\mathfrak W(Z)$, Definition 4.4 stipulates that quadruples with $\theta_j=0$ "do not appear in
$H_n$: their entire effect is absorbed into $R_n/C_n$." With that stipulation,
$Q_n-Q_n^{\mathrm{aut}}=C_n$ (both sections share $I+R_n$), and $\|C_n\|\leq\omega_n\to0$:
$Q-Q^{\mathrm{aut}}\in\mathcal J$ **by construction of the model**. D134's proof also invokes a
perturbation bound $\sum_j\varphi(\delta_ja(\gamma_j))$ that is NOT any of the axioms (S1)–(S3) as
written — it is a "perturbation form of (V1)", an implicit extension of the model whose real content is
CALCULATION 4.3 (Paley–Wiener) plus Theorem 3.3 of Doc 108 (declared status).
**Verdict:** the statement is true (in the stipulated version it is trivial; in the version with the bound it
is a declarable extension of the model), but the [THEOREM] label oversells it: sub-resolution blindness
is essentially the absorption axiom, and the only non-axiomatic anchor is D108 Thm. 3.3. The no-go 5.5 and
Prop. 5.5bis (re-derived: explicit construction $\delta_j=\min(\tfrac14,1/(ja(\gamma_j)))$,
monotonicity, cofinality) are correct — and are the frank, hard part of the document: the master
quantifier reappears as a resolution quantifier, said by the documents themselves.

### 4.5. Lemma 5.0, Thm 5.1, Thm 7.2, Theorem 6.1/6.1bis, Prop. 6.3/7.4 — CORRECT

All re-derived. Minor notes: (1) P47 lem:window-spec has the typographical chain
"$\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n\geq\lambda_{\min}$" — it should be
"$\lambda_{\min}\leq\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n$" (typographical erratum, correct
content). (2) Thm 6.1bis uses $\mathrm{dist}_H(\mathrm{spec}A,\mathrm{spec}B)\leq\|A-B\|$ for
self-adjoint elements in a C\*-algebra — correct (standard spectral perturbation; holds in any
C\*-algebra via a faithful representation). (3) Prop. 7.4: the bound $\mathrm{tr}(BA)\geq-\varepsilon\,\mathrm{tr}(A)$
for $B\geq-\varepsilon I$, $0\leq A\leq I$ is correct; the average with bad-window density
$\to0$ and Banach limit: correct.

---

## 5. Parity and Witt (protocol 5)

### 5.1. Re-derivation of D.1–D.4 — proofs CORRECT

- **D.1** (radical orthogonality, $w\neq\bar z$): the induction on $p+q$ with
  $(z-\bar w)Q(u,v)=Q(u,v')-Q(u',v)$ is correct (sesquilinearity verified: $Q(u,Av)$ with
  $A$ $Q$-symmetric and eigenvalue $w$ in the second variable produces $\bar w$). ✓
- **D.2** (hyperbolic pairing): isotropy of $H[z]$ for $z\notin\mathbb R$ via D.1 with $w=z$
  ($\bar z\neq z$); the nondegenerate pairing $H[\bar z]\cong H[z]^*$ and the signature $(d_z,d_z)$
  via SVD of the block $\begin{psmallmatrix}0&B\\B^*&0\end{psmallmatrix}$: correct. ✓
- **D.3** ($\delta=\sum d_z$): additivity A.1(ii) over the $Q$-orthogonal decomposition. ✓
- **D.4** (parity): $SH[z]=H[-z]$ (induction on the nilpotent index, correct); the four points
  $z,\bar z,-z,-\bar z$ are distinct **precisely because** $z\notin\mathbb R\cup i\mathbb R$;
  $\delta=2\sum d_z$ even. ✓ The proof does not use $\epsilon_S$: correct, it only needs $S$ bijective
  conjugating as $SAS^{-1}=-A$.

### 5.2. The parity error the protocol asked to look for — does not exist within scope, but the SCOPE is the trap

**Zeros ON the critical line (even or odd multiplicity):** $z=\rho-\tfrac12\in i\mathbb R$ ⟹
$z^2\in\mathbb R$ ⟹ **excluded from $P$ by definition**. The theorem says nothing about them; in the
Weil form they contribute mass $\geq0$ and do not touch $\delta$. No error. **The fixed point $s=\tfrac12$:**
$z=0$, likewise excluded. No error.

**But — real spectrum ($z\in\mathbb R\setminus\{0\}$, i.e. real $\rho\neq\tfrac12$): here parity
is FALSE and the hypothesis $z^2\notin\mathbb R$ is the only wall.** Closed-form counterexample within
the category: $H=P=\mathbb Cu\oplus\mathbb Cv$, $A=\mathrm{diag}(t,-t)$ with $t\in\mathbb R\setminus\{0\}$,
$Su=v$, $Sv=u$ (then $SAS^{-1}=-A$ ✓, $S^2=1$ ✓), and $Q=-I$ (negative definite; $Q(Sx,Sy)=Q(x,y)$ ✓;
$A$ is $Q$-symmetric since $Q(Ax,y)=-\langle Ax,y\rangle$ and $A$ is… take $A$ real diagonal, symmetric
for $-\langle\cdot,\cdot\rangle$ ✓). Spectral object with full functional symmetry and
$\delta=2$ — fine; now take the sub-object $H=P=\mathbb Cu\oplus\mathbb Cv$ with
$Q=\mathrm{diag}(-1,+1)$: $Q(Sx,Sy)=\epsilon_SQ$ with $\epsilon_S=-1$ ✓ and $\delta=1$ **odd, with
functional symmetry** — possible only because the spectrum is real. Arithmetic translation: a **Siegel–Landau
type zero** ($\beta\in(\tfrac12,1)$ real; $z=\beta-\tfrac12\in\mathbb R$) falls outside D.4: the
pair $\{z,-z\}$ given by the functional equation does NOT force a hyperbolic plane (D.1 does not apply:
$\bar z=z$), and $Q|_{H[z]}$ can be definite of odd dimension. **For ζ it is harmless** (ζ has no
real zeros in $(0,1)$: $\zeta(s)<0$ there — classical), but the categorical slogan "every spectral object with
functional symmetry has even defect" (Obs. 6.1 D132) **is false without the explicit caveat $z^2\notin\mathbb R$
in every citation**, and the category 𝒫ol_δ is meant to house general Dirichlet objects
(D131, $F_{p,\alpha}$, DH), where real zeros are not excluded a priori. **Verdict: SURVIVES WITH MANDATORY
SCOPE CAVEAT**; D.4's formulation is correct because the hypothesis is in the definition of
"spectral object", but every paraphrase without the hypothesis is false.

### 5.3. $\mathcal K_{\mathrm{off}}$ Witt-trivial — re-derived

For $m<\infty$: D.2+D.4 give signature $(2m,2m)$ on $\mathcal K_{\mathrm{off}}$; E.2 ("$\sigma=0$ ⟺
hyperbolic", via the real-segment argument for the isotropic vector + definite anisotropic part
[Scharlau]): re-derived, correct. $\theta=\tfrac12$ is in the absorbing ideal E.2: correct. **Two
minor slippages:** (1) under $\neg$RH with $m=\infty$, the signature is $(\infty,\infty)$ and E.2 (a
finite-dimensional theorem) does not apply literally — the statement holds by truncation/exhaustion and
should be said that way; (2) the nondegeneracy of $Q|_{\mathcal K_{\mathrm{off}}}$ (needed for D.2) is
inherited from the quadruple model (D96/D106), not verified here — low risk, declarable. The
structural consequence (invisible to every multiplicative invariant; A.4 re-derived via the ring
$\mathbb Z[\varepsilon]/(\varepsilon^2-1)$, correct with the observation that it also requires an integral
domain **of characteristic 0 or $\neq2$** for $u=\pm1$ distinct — in characteristic 2 the two
characters collapse; irrelevant to the use) stands.

---

## 6. Consequences for P47

1. **thm:exact (= Thm 1.3): intact.** It is publishable as is; it is the paper's best piece.
2. **thm:strict: MANDATORY ERRATUM.** The parenthetical "(With noise $\omega_n\to0$, the same equivalence
   holds up to windows whose maximal visibility satisfies $\vartheta_n\to0$ and
   $\vartheta_n\leq\omega_n$ eventually.)" is false (§4.2). Replace with: "With noise
   $\omega_n\to0$ the equivalence holds verbatim: strict symbol positivity iff
   $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$." The correction **strengthens** the theorem and does
   not touch cor:gap-quant, conj:lp134, thm:synergy or rem:trichotomy.
3. **thm:thin: already corrected** with respect to D134 (clause (iv) was removed); optionally add the
   sub-hypothesis $\vartheta_n>\omega_n$ i.o. for the phrase "attained as a limit of *negative*
   $\lambda_{\min}$"; (ii)–(iii) do not need it.
4. **lem:window-spec:** typographical erratum in the chain of inequalities (§4.5).
5. **Abstract/intro:** replace "continuous field" with "$\ell^\infty$-product field over $\mathbb N$"
   or state the discrete base (§1.4).
6. **rem:trichotomy:** the phrase "off-critical zeros live exactly on the symbol/compact boundary" should
   say "the *thin-visible stratum* lives on the boundary; fat strata in the symbol, sub-resolution in
   the ideal" — the body of the paper already says this correctly; the global remark over-condenses it.
7. **D134 itself:** fix Thm 5.3(ii), restrict Thm 5.2(iv), re-label Thm 5.4 as
   "[THEOREM-in-extended-model; non-axiomatic content = D108 Thm. 3.3]". Add the three entries to
   `06-papers/ERRATA.md`.
8. **Future citation rule (the two scope walls):** (i) B.4/Thm 1.3 never without "G bounded in the
   specified Hilbert realization" (essential positivity is not an invariant of the form — Thm 2.2
   proves it); (ii) D.4/parity/Witt never without "$z^2\notin\mathbb R$" (Siegel-type real zeros break
   parity; harmless for ζ, not for the category).
9. **What this audit does NOT touch:** P47's logistic section (thm:logistic, thm:realiz, thm:main) was
   not part of mandate (a)–(e); its declared dependencies (rem:deps) are frank. It remains a natural
   target for a separate audit (in particular Step 3 of thm:realiz: the tail budget via
   lem:tail, and the claim "the caveat was an artifact" of rem:key, which de-conditions
   Hypothesis D of P40 — exactly the kind of de-conditioning that has died under audit
   before in this program).

---

## References

**Internal:** Doc 134 (main object); Doc 132 (main object); Doc 108 (Thm. 3.3, Lemma 2.4,
§5.2); Doc 112 (LP-112, Prop. 2.6); Doc 98/95 (CCM); P35; P43; P47 main.tex; 06-papers/ERRATA.md
(destination for the errata).

**Literature:** G. J. Murphy, *C\*-Algebras and Operator Theory*, Academic Press, 1990 (Thm. 2.1.11
spectral permanence; Thm. 3.1.5 isometric monomorphisms). J. Dixmier, *Les C\*-algèbres et leurs
représentations*, Gauthier-Villars, 1969 (§1.9 products; §10 continuous fields — the notion that
P47's abstract invokes vacuously). T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed.,
Springer, 1976 (Thm. IV.5.35). M. Reed, B. Simon, *Methods of Modern Mathematical Physics IV*, Academic
Press, 1978 (§XIII.4, Weyl's criterion). J. Bognár, *Indefinite Inner Product Spaces*, Springer, 1974
(Hilbert majorants, bounded Gram in $\Pi_\kappa$). I. S. Iohvidov, M. G. Kreĭn, H. Langer,
*Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*, Akademie-Verlag,
1982. W. Scharlau, *Quadratic and Hermitian Forms*, Springer, 1985 (Witt). R. Bhatia, *Matrix Analysis*,
Springer, 1997 (finite-dimensional Weyl). A. Böttcher, B. Silbermann, *Analysis of Toeplitz Operators*,
2nd ed., Springer, 2006. V. Rabinovich, S. Roch, B. Silbermann, *Limit Operators and Their Applications
in Operator Theory*, Birkhäuser, 2004. I. C. Gohberg, M. G. Kreĭn, *Introduction to the Theory of Linear
Nonselfadjoint Operators*, AMS, 1969 (Fredholm/index context; no audited proof requires it).

*End of Doc 140.*
