# 104_00 — Bibliography gate

**Objective:** blocking. No Phase 104 mechanism proceeds without a verdict here.

**Replaces** `03-research/phase-102-omega7-closure-campaign/102_BIBLIOGRAPHIC_GATE.md`, which has 54 lines and
itself states: *"A full external literature audit should compare this exact theorem by formula
and mechanism before any paper-level novelty claim is made."* That audit had not been done.

**Mandatory convention.** Every imported statement carries the label `[UNCOND]` (unconditional) or
`[COND: RH]` / `[COND: GRH]`. Confusing them is the error this gate exists to prevent.

---

## 1. Main finding of the gate

### Lagarias, *Li coefficients for automorphic L-functions*, `math/0404394` (Ann. Inst. Fourier 57 (2007) 1689)

Definition (eq. 1.14), **incomplete Li coefficient**:
\[
\lambda_n(T,\pi)=\sum_{\substack{\rho\in Z(\pi)\\ |\Im\rho|<T}}\Bigl[1-\Bigl(1-\frac1\rho\Bigr)^{n}\Bigr].
\]

Theorem 1.1, eq. (1.17), **as printed**:
\[
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)\,n-\lambda_n(\sqrt n,\pi)+O(\sqrt n\log n).
\]

Eq. (1.18) — **`[COND: RH for L(s,π)]`**:
\[
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)\,n+O(\sqrt n\log n).
\]

Eq. (1.13): \(C_1(\pi)=\frac N2(\gamma-1-\log 2\pi)+\frac12\log Q(\pi)\).
For \(\zeta\) (\(\pi\) trivial, \(N=1\), \(Q=1\)): \(C_1=\frac12(\gamma-1-\log 2\pi)\).

Eq. (1.15), as printed:
\(S_f(n,\pi)=+\lambda_n(\sqrt n,\pi^\vee)+O(\sqrt n\log n)\).

### Binding sign erratum

The two formulas above cannot be imported as theorems in that form. At the point
\(s_0=\rho-1\), the integrand in the proof of Theorem 6.1 satisfies

\[
\mathop{\mathrm{Res}}_{s=s_0}
k_n(s)\left(-\frac{L'}L(s+1,\pi)\right)
=-m_\rho k_n(\rho-1),
\qquad
k_n(s)=\left(1+\frac1s\right)^n-1.
\]

The minus sign comes from \(-L'/L\). When expanding the small counterclockwise contour to the
large rectangle, the printed proof uses the opposite sign. With the zero symmetry that the
article uses to obtain (6.7), set

\[
\widehat I_2(n):={1\over2\pi i}\int_{C_2}F_n(s)\,ds.
\]

The source defines \(I_2\) without the \((2\pi i)^{-1}\) factor, but later uses it as if it were
normalized. With the unambiguous notation above, the corrected computation gives

\[
\widehat I_2(n)=S_f(n,\pi)+\lambda_n(T,\pi^\vee)+O(1),
\]

and the contour conclusion is repaired as follows. The printed choice
\(T=\sqrt n+\varepsilon_n\) does not justify the geometric decay of (6.12):
its available ratio is \(e/2>1\). Taking instead
\(T=2\sqrt n+\varepsilon_n\), the exact identity

\[
 {k_n(s+1)+1\over k_n(s)+1}
 =\left(1-{1\over(s+1)^2}\right)^n
\]

gives the ratio \(e^{1/4}/2<1\) against the absolute majorant of the Dirichlet
series of \(L'/L\). Thus
\(\widehat I_2(n)=O_\pi(\sqrt n\log n)\). The band
\(\sqrt n\le|\gamma|\le2\sqrt n+1\) contains
\(O_\pi(\sqrt n\log n)\) zeros and each Li summand has modulus
\(\le1+e^{1/2}\), so one returns to the \(\sqrt n\) cutoff with the same
order of error. This yields

\[
\boxed{
S_f(n,\pi)=-\lambda_n(\sqrt n,\pi^\vee)+O_\pi(\sqrt n\log n).}
\tag{1.15c}
\]

By the exact arithmetic formula
\(\lambda_n=S_\infty-S_f+\delta\), the corrected version of (1.17) is

\[
\boxed{
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)n
+\lambda_n(\sqrt n,\pi)+O_\pi(\sqrt n\log n).}
\tag{1.17c}
\]

The conditional formula (1.18) is unchanged. The full audit of orientation, residue, and
symmetry is in `104_02` §1. The search carried out on 25-Jul-2026 on the arXiv record, the
Numdam record, and the results linked from them **found no corrigendum**; (1.15c)–(1.17c)
are therefore an internal erratum, not an official correction attributed to the author.

**Implied constant — critical datum.** In (1.15), (1.17), and (1.18), Lagarias repeats:
*"where the implied constant in the O-notation depends on \(\pi\)"*. **There is no effective
constant.** For \(\zeta\) it is a fixed absolute but unknown constant. It blocks any
certified numerical range. Making it effective is not RH-strength, but it is **deferred**: it
does not contribute to closure for all \(n\), which is the goal of the phase.

**Range with verified RH — Lagarias's own statement**, immediately after (1.16).
**Note: the two versions differ by a factor of 2 and must not be merged.**

- **Published version** (Ann. Inst. Fourier **57** (2007) 1689, p. 1694), checked against the PDF:
  > *"Furthermore if the Riemann hypothesis holds up to height \(T\), then a bound of shape
  > (1.16) holds for all \(n\leqslant T^2/2(\log T)^2\), with the implied \(O\)-constant
  > depending on \(\pi\)."*
- **arXiv TeX source** `math/0404394`: same paragraph with \(T^2/4(\log T)^2\).

The published version is recorded as the main text and the arXiv source as a variant. The
corrected discussion of what a verified height allows is in `104_02` §5.

The final statement uses the truncation at **exactly \(\sqrt n\)**. The earlier factor
of \(2\) is only the auxiliary contour that repairs the horizontal segment;
it is eliminated by the band estimate.

**Blow-up without RH — the needed reference.** After (1.18), p. 1694:
> *"If the Riemann hypothesis does not hold for \(L(s,\pi)\) then the incomplete Li coefficient
> term \(\lambda_n(\sqrt n,\pi)\) will sometimes be very large, of size exponential in \(n\).
> This fact was already observed for the Riemann zeta function in [4, Theorem 1 (c)]."*

[4] = **Bombieri–Lagarias**. This is the statement cited in §7; it is not redone by hand.

**Corrected consequence for our normalization.** Our archimedean block satisfies
(`main.tex:6856`)
\[
A_n=\frac n2(\log n+\gamma-1-\log 2\pi)+O(\log n),
\]
which matches \(\frac12 n\log n+C_1 n\) for \(\zeta\), up to \(O(\log n)\). Defining

\[
\widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n),
\]

(1.17c) implies

\[
\boxed{\ A_n-\lambda_n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n,\quad
|\widetilde\varepsilon_n|\le C_*\sqrt n\log n\qquad[\mathrm{UNCOND}]\ }
\tag{G1c}
\]

and since our exact identity gives \(\lambda_n=A_n-n-\mathcal J_n\) with
\(\mathcal J_n=\int_0^\infty E\,K_n\), one obtains

\[
\boxed{\ \mathcal J_n+n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n
\qquad[\mathrm{UNCOND}]\ }
\tag{G2c}
\]

The earlier quantity
\(\varepsilon_n^-=A_n-\lambda_n-\lambda_n(\sqrt n)\) satisfies
\(\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n)\). Hence the unconditional
bound \(|\varepsilon_n^-|\ll\sqrt n\log n\) is **withdrawn**: it is not a matter of making a
constant effective. The corrected exact form of A1 is

\[
\boxed{
\mathrm{A1}_\theta\iff
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\theta))
\le(1-\theta)A_n.}
\tag{G3c}
\]

Consequently, the incomplete block requires a **lower** bound, not an upper one.

Here it is recorded only that **collective control of zeros of height \(\gg\sqrt n\) is already
resolved in the literature**, and that the remaining obstacle lives entirely in the incomplete
block.

**Consistency check.** Under RH,
\(0\le\lambda_n(\sqrt n)\le4N(\sqrt n)\). The side that now matters in (G3c) is non-negativity.
If RH fails, Bombieri–Lagarias shows that the incomplete block has exponential excursions; a
uniform lower bound of the required size is still RH-strength.

**Verdict:** `does-not-duplicate` for A1, **`duplicates`** for the localization of the tail **and
also for the finite range with verified height**.

Before this gate was incorporated, phases 1–103 had **zero occurrences** of "incomplete Li"
(search over `*.md`, `*.tex`, `*.py`), and `rmk:height-range` (`main.tex:6516`) posed the
collective control of \(\gamma>H\) as open, requesting "a zero-density input" — an input that
the corrected version (1.17c) does not need. And the range \(\approx10^{25}\) of
`main.tex:6531` is obtained by **single-zero analysis**, not collective analysis: that is the
real defect. Lagarias states, since 2007, a smaller range for a bound of form (1.16)
—\(T^2/2(\log T)^2\approx5.5\times10^{21}\) in the published version—, but **the correct value
remains open**: the direct count from \(\sqrt n\le H\) does reach \(n\le H^2\) for the trivial
bound, and there is also an editorial discrepancy (recorded in `104_02` §5).

**Consequence for the plan:** the finite range with verified height is mostly bibliographic
ground and **is not the front**. The front is (G3c), with the corrected sign.

---

## 2. Saddle-point / Nörlund–Rice route

### Mazhouda, *The saddle-point method and the Li coefficients*, `1506.01755` (Canad. Math. Bull.)

Abstract, verbatim: *"for any function F in the Selberg class S and **under the Generalized
Riemann Hypothesis**, we have λ_F(n)=…"*. Method: saddle point + Nörlund–Rice integrals
over the generalized \(\lambda_F(n)\) of Omar–Mazhouda.

- Label: **`[COND: GRH]`**. There is no unconditional version in the statement.
- **Overlap with `104_03`:** the contour representation
  \(S_n=\frac1{2\pi i}\oint R(t)(1+t)^n t^{-(n+1)}dt\) is of the same family (binomial transform
  ↔ Nörlund–Rice). `104_03` must explicitly delineate which part of the contour is
  unconditional in our case and which part, there, relies on GRH.
- **Verdict:** `adjacent`. The technique is published; what is missing is an unconditional
  conclusion. `104_03` is declared an audit, not a contribution.

---

## 3. Voros series

| ref | content | label |
|---|---|---|
| `1602.03292` — *Simplifications of the Keiper/Li approach to the RH* | simplifications of the scheme | — |
| `1703.02844` — *Discretized Keiper/Li approach to the RH* | deforms \(\{\lambda_n\}\) into explicit sequences, computed up to \(n=5\cdot10^5\) (Misguich); tests that "selectively react to zeros off the critical line", validated against Davenport–Heilbronn | **gives no unconditional result**; it is a computational test framework |
| `2204.01036` — *From asymptotic to closed forms…* | new sequence in elementary closed form that retains the asymptotic sensitivity to RH; flags violating zeros via DH | **no unconditional claims in the abstract**; it does not prove a new criterion equivalent to RH, it reformulates Li's |

**Point that corrects gate 102.** `102_BIBLIOGRAPHIC_GATE.md` warns: *"Claims proving only
the asymptotic size of `lambda_n` do not close Omega7."* This is imprecise. A subexponential
**upper** bound on \(\lambda_n\) does imply RH: an off-line quartet contributes
\(4-4\cosh(n\alpha)\cos(n\theta)\) with \(\alpha>0\), of exponential amplitude in \(n\)
(`103_28`, `103_69`). What closes nothing is a bound that is **asymptotic in the "order of
magnitude" sense** without uniformity or side. The correct warning is about **uniformity and
side**, not about "asymptotic."

Here the normalization is that of the Li coefficient. In a Weil-form/autocorrelation
normalization \(2\mathrm{Re}\,\lambda_n\), the same quartet contributes
\(8-8\cosh(n\alpha)\cos(n\theta)\).

**Verdict:** `adjacent`. Voros's conclusions **do not transfer automatically to
A1**: his sequences are deformations, not ours, and his proved value is diagnostic.

---

## 4. Coffey

| ref | content | risk |
|---|---|---|
| `math/0402168` — *Effective method of computing Li's coefficients and their properties* | effective computation of \(\lambda_n\) | low |
| `math/0406312` — *An Explicit Formula Relating Stieltjes Constants and Li's Numbers* | explicit relation Stieltjes constants ↔ Li numbers | **high** for the scalar form of `103_66` |

The scalar form of `103_66` eq. (8) is
\(\sum_{j=0}^n\binom nj\frac{R^{(j)}(0)}{j!}\le\frac12\Delta A_n\), where
\(R^{(j)}(0)/j!\) are explicit polynomials in the Stieltjes constants. **This is exactly the
type of object in `math/0406312`.**

**Verdict:** `likely duplication` of the *coordinate*, not necessarily of the inequality.
Operational consequence: the lcm/Stieltjes form is **downgraded to audit**, it is not a front
(consistent with the plan's decision).

---

## 5. Model space / de Branges / Clark measures

### Suzuki, *On the Hilbert space derived from the Weil distribution*, `2301.00421`, Canad. J. Math., online 3-Nov-2025, DOI 10.4153/S0008414X25101739

Completes \(C_c^\infty(\mathbb R)\) with respect to the Hermitian form of the Weil
distribution **under RH**, and proves that this Hilbert space is isomorphic to a **de Branges
space** via Fourier composed with a simple map; deduces new conditions equivalent to RH.

- Label: **`[COND: RH]`** for the construction of the space.
- **Eliminates the novelty** that had been attributed to the model-space/de Branges route: the
  bridge Weil ↔ model space ↔ de Branges is published.

**On Aleksandrov–Clark measures.** The search returns no Clark ↔ RH connection, and the repo
has zero occurrences of "Clark measure". But that is **not enough to declare it promising**:
the Clark measure of \(\theta_n(s)=((s-1)/s)^n\) depends **only on \(\theta_n\)**, not on
\(\zeta\), so it is universal and by itself contains no arithmetic whatsoever; moreover one of
the nodes may appear as a point mass at infinity.

**Verdict:** `discarded as a front`. It is taken up again only if a concrete arithmetic entry
point appears, and in that case the delineation from Suzuki is mandatory.

---

## 6. Verified height

### Platt–Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, `2004.09765`

RH verified for \(|\gamma|\le H=3\times10^{12}\).

- Label: **`[UNCOND]`** (it is a computer-assisted theorem, not conditional).
- **Admissible use in Phase 104: verification, finite corollary, or consistency check only**
  (`104_02` §5). The uniform proof of A1 for all \(n\ge150\) cannot depend on it.
- **Scale: open, not corrected.** \(H^2\) (direct count from \(\sqrt n\le H\),
  for the trivial bound \(\lambda_n(\sqrt n)\le4N(\sqrt n)\)), \(H^2/2(\log H)^2\) (Lagarias
  published), and \(H^2/4(\log H)^2\) (arXiv) coexist. What is actually wrong in
  `rmk:height-range` (`main.tex:6531`) is the **argument**, which is of isolated-zero type. See
  `104_02` §5.

---

## 7. Admissible sources, and the "competitor" on the same route

### Source policy (binding for the whole phase)

**Admissible as a source for a result:** arXiv, Zenodo, institutional repositories, and
peer-reviewed journals.
**Not admissible as a source for a result:** ResearchGate, Academia.edu, viXra, and similar
aggregators — they host preprints with no review or version control, and their error rate on
this specific topic (claimed proofs of RH) is high. Consequently **no lemma is imported from
them**.

**A necessary distinction: admissibility ≠ priority.** A source inadmissible as support for a
theorem **still counts as a possible priority antecedent**: if someone published an idea first,
that fact does not depend on where it was hosted. Therefore inadmissible texts **are recorded,
dated, and compared mechanism by mechanism**; the only thing not done is citing them to justify
a step.

### The text in question

**"On the Asymptotics of Li coefficients and Proof of the Riemann Hypothesis"**, Feb-2026,
hosted **only on ResearchGate** (publication 400430678). No arXiv, Zenodo, or
preprints.org version; no peer review. **Inadmissible source** under the policy above.

This entry is kept for a single reason: it attacks via **our exact route** (explicit
formula for \(\psi\) + Laguerre polynomials) and claims:
\[
\lambda_n=\frac n2(\log n-1+\gamma-\log 2\pi)+o(n)\quad(n\to\infty)
\ \Longrightarrow\ \text{RH by a theorem of Voros}.
\]

In the normalization of (G1c)–(G2c) this amounts to claiming \(\lambda_n(\sqrt n)=o(n)\)
**unconditionally** — precisely the incomplete block that is open here.

**Access status:** `BLOCKED` (HTTP 403 on anonymous fetch) **and inadmissible source**. Only
the statement, via indexing, is available.

**What can be established without the text.** Its claim, translated via (G1c), is
\[
\lambda_n(\sqrt n)=o(n)\qquad\text{unconditionally.}
\]

**Proposition (dichotomy).** *The preprint's claim is equivalent to RH; it is not an
intermediate step toward it.*

*Proof.* (\(\Leftarrow\)) Under RH, each pair \(\{\rho,\bar\rho\}\) with \(|\gamma|<\sqrt n\)
contributes \(2-2\cos(n\theta_\rho)\in[0,4]\), so
\(\lambda_n(\sqrt n)\le4N(\sqrt n)=O(\sqrt n\log n)=o(n)\).

(\(\Rightarrow\)) **Bombieri–Lagarias is cited**, Thm 1(c), which is exactly the statement
needed: if RH fails, \(\lambda_n(\sqrt n)\) is *sometimes* of exponential size in \(n\).
Lagarias himself notes this after (1.18):

> *"If the Riemann hypothesis does not hold for \(L(s,\pi)\) then the incomplete Li coefficient
> term \(\lambda_n(\sqrt n,\pi)\) will sometimes be very large, of size exponential in \(n\).
> This fact was already observed for the Riemann zeta function in [4, Theorem 1 (c)]."*
> — `math/0404394`, p. 1694; [4] = Bombieri–Lagarias.

Hence \(\lambda_n(\sqrt n)\ne o(n)\), contradicting the claim. \(\square\)

> **Binding correction.** An earlier version of this proof argued direction
> (\(\Rightarrow\)) by saying that "the other zeros are finite in number and of fixed
> frequencies \(\theta\)," so they cannot cancel the offending quartet. **That argument is
> insufficient:** the truncation \(\sqrt n\) **grows with \(n\)**, so the set of participating
> zeros is not fixed — new zeros enter indefinitely. Controlling the cancellation among a
> growing set of exponential terms is precisely the content of Bombieri–Lagarias, and it must be
> cited, not redone by hand.

**Operational consequence.** The preprint either contains RH or contains an error; there is no
third option, and no part of it can be imported as a lemma. **Its value to us is exclusively
diagnostic:** knowing at exactly which line the natural argument via the
\(\psi\)-explicit-formula + Laguerre route — which is *our* route — breaks down saves time in
`104_10`.

**Hypotheses about the breaking point**, in order of likelihood, to be checked once the PDF is
obtained:
1. Illegitimate interchange of the limit \(n\to\infty\) with the sum over zeros (or with the
   regulator \(\varepsilon\downarrow0\)): this is exactly where an exponential excursion of
   \(\lambda_n(\sqrt n)\) can disappear.
2. **Pointwise** bound on \(\psi(y)-y\) where phase is needed — the \(\Theta(n)\) deficit of
   `rmk:pointwise-insufficient`.
3. Using the printed sign of (1.15)/(1.17) without recomputing the residue of \(-L'/L\), or
   importing (1.18) (`[COND: RH]`) as if it were an unconditional estimate.

**Reclassification — CLOSED.** This item was marked **blocking for `104_10`**. It is closed for
two independent reasons: (a) the source is inadmissible under this section's policy, so it
cannot serve as an antecedent or a novelty delineation; (b) the Proposition above already fixes,
unambiguously and without needing the text, what any argument along this route must prove —
which is exactly the wall of `104_02` §4. **`104_10` is unblocked.**
If a version appears on arXiv or Zenodo, it is reopened only as diagnostic.

This is recorded as a scope change relative to the approved plan, which listed it as
blocking.

---

## 8. Verdict table

| Phase 104 mechanism | compared source | verdict |
|---|---|---|
| Reduction of A1 to the incomplete block (`104_02`) | Lagarias `math/0404394`, §6, with internal sign erratum | **duplicates the tail localization**, but the printed equations (1.15)/(1.17) are unusable without the correction |
| Binomial contour \(R(t)\) (`104_03`) | Mazhouda `1506.01755` `[COND: GRH]` | `adjacent` — audit, not contribution |
| lcm / Stieltjes form (`103_66`) | Coffey `math/0406312` | `likely duplication` of the coordinate → **downgraded to audit** |
| Model space / Clark | Suzuki `2301.00421` `[COND: RH]` | `discarded as a front` |
| \(C_n^\theta\) family (`104_01`) | — | **does-not-duplicate** — the A0/A1 split with free \(\theta\) does not appear in the consulted literature |
| M1, collective kernel \(w_{\max(i,j)}\) (`104_10`) | — | **does-not-duplicate** — the identity is from `103_67` (internal); the monotone/PSD decomposition appears neither in the repo nor in the consulted literature |

---

## 9. What this gate changes in the plan

1. **`104_02` fixes the erratum and the exact corrected target**:
   \[
   -\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\theta))
   \le(1-\theta)A_n.
   \]
   The front is a lower bound of the incomplete block. The former Theorem A/A′ and B1/B2
   are withdrawn.
2. **`rmk:height-range` in `main.tex` needs correction**: the collective
   control of \(\gamma>H\) does not require a density input, it is given by the §6 proof with
   the corrected sign (1.17c); and its range
   \(\approx10^{25}\) comes from a **single-zero analysis**, which is the real defect. The
   published range has an editorial discrepancy, recorded in `104_02` §5.
3. **`102_BIBLIOGRAPHIC_GATE.md` §Warning needs correction**: the problem with an asymptotic
   bound is not that it is asymptotic, but its side and its uniformity.
4. Two routes are closed before spending further effort: the lcm/Stieltjes form (Coffey) and the
   model space/de Branges route (Suzuki).

**Blocking status of `104_10`: UNBLOCKED.** The preprint item (§7) is closed there by source
inadmissibility plus the dichotomy via Bombieri–Lagarias, and is kept on record as a possible
priority antecedent. *(An earlier version of this section declared it blocking; this
contradicted §7 and is withdrawn.)*
</content>
