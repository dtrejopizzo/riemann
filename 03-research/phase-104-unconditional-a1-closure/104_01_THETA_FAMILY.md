# 104_01 — The family \(C_n^\theta\)

**Objective:** normalization. First exact theorem of the phase. It contains no new mathematics
with respect to RH; it fixes the object on which `104_02` and `104_10` work, and **resolves with
a sign** the question of whether the A0/A1 split frozen at \(\theta=\frac14\) can be improved.

Notation from `main.tex:6718`–6729:
\[
A_n:=\lambda_n^{\rm arch},\quad
E(u):=\psi(e^u)-e^u,\quad
K_n(u):=e^{-u}L^{(2)}_{n-1}(u),\quad a:=\log 2,
\]
\[
R_n(T):=-\int_T^\infty E(u)K_n(u)\,du .
\]
The integrals are understood via the paired pole–prime Abel regularization; for every finite
\(T\) the first one is an ordinary integral of the Chebyshev discrepancy.

---

## Theorem 1 (exact identity, every \(\theta\))

For every \(n\ge1\), every \(\theta\in\mathbb R\), and every admissible cutoff \(T\), let
\[
C_n^\theta(T):=(1-\theta)A_n-n-\int_0^T E(u)K_n(u)\,du .
\]
Then
\[
\boxed{\;C_n^\theta(T)=\lambda_n-\theta A_n-R_n(T).\;}
\tag{1}
\]

**Proof.** The corrected Stieltjes integration by parts
(`main.tex:6743`–6748, with the boundary term \(-n\) **kept**, binding erratum) gives
\[
\lambda_n^{\rm prime}=-n-\int_0^\infty E(u)K_n(u)\,du,
\]
and \(\lambda_n=A_n+\lambda_n^{\rm prime}\), so
\(\int_0^\infty EK_n=-n-\lambda_n+A_n\). Since \(\int_T^\infty EK_n=-R_n(T)\),
\[
\int_0^T EK_n=\int_0^\infty EK_n-\int_T^\infty EK_n=(-n-\lambda_n+A_n)+R_n(T).
\]
Substituting into the definition,
\[
C_n^\theta(T)=(1-\theta)A_n-n+n+\lambda_n-A_n-R_n(T)=\lambda_n-\theta A_n-R_n(T).\qquad\square
\]

\(\theta=\frac14\) recovers `prop:li-compact-tail` (`main.tex:6734`). There is no exchange of
limits nor an unpaired divergent term.

**Corollary 1.1.** If \(A_n>0\), \(|R_n(T_n)|\le\theta A_n\), and \(C_n^\theta(T_n)\ge0\),
then \(\lambda_n\ge0\).
*Proof:* \(\lambda_n=C_n^\theta(T_n)+\theta A_n+R_n(T_n)\ge C_n^\theta(T_n)\ge0\). \(\square\)

---

## Theorem 2 (collapse and reserve)

For every \(n\ge1\), every \(\theta\), and every admissible cutoff \(T\ge a\),
\[
C_n^\theta(T)\ge0
\iff
\boxed{\;\int_{a}^{T} E(u)K_n(u)\,du\ \le\ q_{n,\theta},\qquad
q_{n,\theta}:=(1-\theta)A_n+1-L_n^{(1)}(\log 2).\;}
\tag{2}
\]

**Proof.** For \(0\le u<a\) there are no prime powers, so \(\psi(e^u)=0\) and
\(E(u)=-e^u\), whence \(E K_n=-L^{(2)}_{n-1}\). Since \((L_n^{(1)})'=-L^{(2)}_{n-1}\) and
\(L_n^{(1)}(0)=n+1\),
\[
\int_0^a E K_n=-\int_0^a L^{(2)}_{n-1}(u)\,du=-(n+1)+L_n^{(1)}(a).
\]
Substituting into the definition of \(C_n^\theta\),
\[
C_n^\theta(T)=(1-\theta)A_n-n+(n+1)-L_n^{(1)}(a)-\int_a^T EK_n
=q_{n,\theta}-\int_a^T EK_n.\qquad\square
\]

No base reserve, pole term, or exponential boundary contribution survives in (2):
the cancellation \(-n+(n+1)=+1\) is exact.

**Scale.** With \(A_n=\frac n2(\log n+\gamma-1-\log2\pi)+O(\log n)\) and
\(L_n^{(1)}(a)=O_a(n^{1/4})\) (`main.tex:6856`),
\[
q_{n,\theta}=(1-\theta)\frac n2(\log n+\gamma-1-\log 2\pi)+O(n^{1/4}+\log n).
\]
**Every argument uses the exact \(q_{n,\theta}\), never this asymptotic** (rule 3).

---

## Theorem 3 (A0 with free \(\theta\) and effective \(T_n(\theta)\))

Let an explicit Vinogradov–Korobov-type PNT estimate be given,
\[
|\psi(y)-y|\le A\,y\,e^{-\eta(\log y)}\quad(y\ge e^{U_0}),\qquad
\frac{\eta(u)}{\log(1+u)}\to\infty ,
\]
with \(A,U_0,\eta\) **fixed once and for all** (a single declared choice, not optimized
case-by-case). If \(T\ge U_0\) satisfies
\[
\eta(u)\ \ge\ (n+1)\log(1+u)+\log\frac{3An^2}{\theta A_n}
\qquad(u\ge T),
\tag{B$_\theta$}
\]
then \(|R_n(T)|\le\theta A_n\).

**Proof.** Same as `thm:a0-tail-direct` (`main.tex:6786`–6804): the finite Laguerre expansion
gives \(|f'_{n,\varepsilon}(y)|\le 3n^2y^{-2}(1+\log y)^{n-1}\) for \(0\le\varepsilon\le1\),
so
\[
|R_n(T)|\le 3An^2\int_T^\infty(1+u)^{n-1}e^{-\eta(u)}\,du .
\]
(B\(_\theta\)) is equivalent to \(e^{\eta(u)}\ge\frac{3An^2}{\theta A_n}(1+u)^{n+1}\), so the
integrand is majorized by \(\theta A_n(1+u)^{-2}\) and
\(|R_n(T)|\le\theta A_n\int_T^\infty(1+u)^{-2}du\le\theta A_n\). \(\square\)

**Fixed explicit PNT triple (declared once, not optimized).** Johnston–Yang,
Theorem 1.4 (`2204.01980v2`), prove for every \(x\ge23\)
\[
 |\psi(x)-x|\le 0.026x(\log x)^{1.801}
 \exp\!\left(-0.1853{(\log x)^{3/5}\over(\log\log x)^{1/5}}\right).
\]
We therefore adopt the weaker triple that is directly compatible with Theorem 3:
\[
A=1,\qquad U_0=1000,\qquad
\eta(u)=0.1853\,u^{3/5}(\log u)^{-1/5}-1.801\log u.
\]
The factor \(0.026\le1\) is favorably discarded. For \(u\ge1000\), direct differentiation
gives
\[
 u\eta'(u)=0.1853\,u^{3/5}(\log u)^{-1/5}
 \left({3\over5}-{1\over5\log u}\right)-1.801>0,
\]
and the first term is increasing; moreover \(\eta(u)/\log(1+u)\to\infty\).
**The whole phase uses this triple and no other.** Any document that changes it must say so
in its header and redo \(T_n(\theta)\).

**Definition.** \(T_n(\theta):=\min\{T\ge U_0:\ \text{(B}_\theta)\ \text{holds for every }u\ge T\}\).

**Lemma 3.1 (monotonicity).** For \(0<\theta\le\theta'\) we have \(T_n(\theta)\ge T_n(\theta')\).

*Proof.* Let \(\Phi_\theta(u):=(n+1)\log(1+u)+\log\frac{3An^2}{\theta A_n}\) be the right-hand
side of (B\(_\theta\)). From \(\theta\le\theta'\) we get \(\log(1/\theta)\ge\log(1/\theta')\),
so \(\Phi_\theta\ge\Phi_{\theta'}\) pointwise. Let
\(S_\theta:=\{T\ge U_0:\eta(u)\ge\Phi_\theta(u)\ \forall u\ge T\}\). If \(T\in S_\theta\)
then \(\eta(u)\ge\Phi_\theta(u)\ge\Phi_{\theta'}(u)\) for every \(u\ge T\), i.e.
\(T\in S_{\theta'}\). Hence \(S_\theta\subseteq S_{\theta'}\) and
\(\min S_\theta\ge\min S_{\theta'}\). \(\square\)

*(The minimum exists: \(\eta(u)/\log(1+u)\to\infty\) guarantees \(S_\theta\ne\emptyset\), and
\(S_\theta\) is a closed ray by its own definition.)*

In particular \(T_n(\theta)\ge T_n(\tfrac14)\) for \(\theta\le\tfrac14\), which is what
Proposition 4 uses. Moreover \(|R_n(T)|\le\theta A_n\) **for every** \(T\ge T_n(\theta)\), not
only at \(T_n(\theta)\): (B\(_\theta\)) was required for every \(u\ge T\).

**Dependence on \(\theta\).** \(\theta\) enters (B\(_\theta\)) **only** through the additive
term \(\log(1/\theta)\). With \(\eta(u)\asymp c\,u^{3/5}(\log u)^{-1/5}\), the defining
equation is
\(c\,T^{3/5}(\log T)^{-1/5}=(n+1)\log(1+T)+O(\log T)+
\log\frac{3An^2}{\theta A_n}\), with \(c=0.1853\), whence
\[
T_n(\theta)-T_n(\tfrac14)\ \approx\ \frac{5}{3c}\,T^{2/5}(\log T)^{1/5}\,\log\frac{1}{4\theta},
\qquad T\asymp T_n(\tfrac14).
\]
The cutoff grows **logarithmically in \(1/\theta\)**; the reserve grows linearly in
\((\tfrac14-\theta)\). That is what makes the question nontrivial, and what is resolved below.

---

## Proposition 4 (signed transport and exact balance)

For \(0<\theta\le\frac14\) define the **signed transport**
\[
\boxed{\;\Delta_{n,\theta}:=-\int_{T_n(1/4)}^{T_n(\theta)}E(u)K_n(u)\,du
\;=\;R_n\bigl(T_n(\tfrac14)\bigr)-R_n\bigl(T_n(\theta)\bigr).\;}
\tag{3}
\]
(The second equality is immediate from \(R_n(T)=-\int_T^\infty EK_n\).)
Then target (2) at \(\theta\) and at \(\frac14\) differ exactly by

\[
\Bigl[q_{n,\theta}-\int_a^{T_n(\theta)}EK_n\Bigr]
-\Bigl[q_{n,1/4}-\int_a^{T_n(1/4)}EK_n\Bigr]
=\underbrace{(\tfrac14-\theta)A_n}_{\text{reserve gain}}
+\underbrace{\Delta_{n,\theta}}_{\text{cutoff cost, signed}} .
\tag{4}
\]

Call \(\mathcal N_n(\theta):=(\tfrac14-\theta)A_n+\Delta_{n,\theta}\) the **net improvement**.

**Unconditional bounds.** By Theorem 3, \(|R_n(T_n(\tfrac14))|\le\tfrac14A_n\) and
\(|R_n(T_n(\theta))|\le\theta A_n\), so \(|\Delta_{n,\theta}|\le(\tfrac14+\theta)A_n\) and
\[
\boxed{\;-2\theta A_n\ \le\ \mathcal N_n(\theta)\ \le\ \tfrac12 A_n .\;}
\tag{5}
\]

**Correct reading of (5).**

1. **There is no free gain.** The sign of \(\mathcal N_n(\theta)\) **is not determined** by
   A0: it depends on the sign of the transport \(\Delta_{n,\theta}\), i.e. on the correlation of
   \(E\) with \(K_n\) in the window \([T_n(\tfrac14),T_n(\theta)]\). Claiming that "\(\theta\to0\)
   gives a free \(4/3\)" is **false**: it is a redistribution of the RH content between reserve
   and block.
2. **But the loss is controllable and tends to zero.** For every \(\varepsilon>0\), choosing
   \(\theta\le\varepsilon/2\) gives \(\mathcal N_n(\theta)\ge-\varepsilon A_n\): lowering
   \(\theta\) **can cost no more than \(\varepsilon A_n\)**, uniformly in \(n\).
3. **The possible gain is real and bounded:** at most \(\tfrac12A_n\approx\tfrac14 n\log n\),
   against \(q_{n,1/4}\approx\tfrac38n\log n\).
4. **Operational conclusion: \(\theta=\tfrac14\) is fixed.** Taking \(\theta_n\downarrow0\) is
   *admissible* (its cost is bounded by \(2\theta_nA_n=o(A_n)\)) but **provides no sign** and
   complicates the cutoff: it moves \(T_n\) outward and enlarges the transport window without
   buying anything provable. **`104_10` (M1) works with \(\theta=\tfrac14\)**, i.e. with the
   normalization inherited from phases 102–103, \(q_{n,1/4}=\tfrac34A_n+1-L_n^{(1)}(\log2)\).
   The \(\theta\) family remains available, not in use.

**What would be needed to turn (5) into a gain.** A sign for \(\Delta_{n,\theta}\), namely
\(\int_{T_n(1/4)}^{T_n(\theta)}EK_n\le0\). In that window \(u\ge T_n(\tfrac14)\) the kernel
\(K_n\) is **past all its zeros** and has fixed sign \((-1)^{n-1}\)
(`103_08` correction 5; note that `103_03` said "always positive," which is false), but
\(E\) has no unconditional one-sided sign (Littlewood: \(E=\Omega_\pm(\sqrt x\log\log\log x)\)).
Therefore **the sign of \(\Delta_{n,\theta}\) is exactly the type of information that A1
needs** and cannot be obtained here without circularity. It is recorded as such and not pursued.

---

## VK diagnostic (not part of the proof)

\[
\mathrm{Cost}_n(\theta):=\int_{T_n(1/4)}^{T_n(\theta)}|E(u)K_n(u)|\,du
\]
is computed **only** to see the order of magnitude of the trade-off against the VK envelope.

> **No choice of \(\theta\) can be justified by citing \(\mathrm{Cost}_n\), and
> \(\mathrm{Cost}_n\) appears in no statement.** It is a diagnostic, not a conclusive
> optimization: replacing \(\Delta_{n,\theta}\) by \(\mathrm{Cost}_n(\theta)\) is exactly
> the absolute-value step forbidden by rule 2, and reproduces the \(\Theta(n)\) deficit
> of `rmk:pointwise-insufficient`.

---

## Parameters that are **not** free

**Laguerre index \(\alpha\).** \(\alpha=2\) is fixed by the exact integration-by-parts
identity \((L_n^{(1)})'=-L^{(2)}_{n-1}\), which is what produces the cancellation
\(-n+(n+1)=+1\) in Theorem 2. The kernel \(\alpha=3\) of
`phase-103-direct-a1-closure/tools/raised_kernel.py` is auxiliary (used in the by-parts
estimate of `103_58`); replacing it in the identity **requires rederiving all boundary terms**,
including the analogue of \(L_n^{(1)}(0)=n+1\). It is not touched in this phase.

**Generalized Li base point.** Omar–Mazhouda's \(\lambda_F(n,a)\) may be admissible, but:
- they must remain **fixed** — if \(a=a(n)\), the equivalence with RH is not automatic;
- they require rebuilding A0, A1, the archimedean formula, and the full criterion.
This is recorded as an option with a cost, not as an adjustment. See `104_00` §2 for the
delineation from `1506.01755`.

---

## Verification

| Item | Test |
|---|---|
| Theorem 1 | Evaluate \(C_n^\theta(T)+\theta A_n+R_n(T)-\lambda_n\) against the rational certificates of `103_51` for \(n\le149\) and several \(\theta\); it must vanish within the interval |
| Theorem 2 | \(q_{n,\theta}\) reconstructed from \(A_n\) and \(L_n^{(1)}(\log2)\); compare against \(q_{n,1/4}\) from `103_02` |
| Theorem 3 | \(T_n(\theta)\) generated from the **declared** explicit PNT triple; numerically verify (B\(_\theta\)) at \(u=T_n(\theta)\) and the monotonicity \(T_n(\theta)\ge T_n(1/4)\) |
| Prop. 4 | Verify (5) by reconstructing \(\Delta_{n,\theta}\) via both routes of (3) |

Diagnostic tool: `tools/theta_family_check.py`. It uses floating point to tabulate the
cutoffs; the identities and the monotonicity are proved in the text and do not depend on that
table.

---

## Result of the document, in one line

The family \(C_n^\theta\) is exact for every \(\theta\), the reserve is
\(q_{n,\theta}=(1-\theta)A_n+1-L_n^{(1)}(\log2)\), and **lowering \(\theta\) gives nothing for
free**: the net improvement \(\mathcal N_n(\theta)=(\tfrac14-\theta)A_n+\Delta_{n,\theta}\) has
indeterminate sign, unconditionally bounded by \(-2\theta A_n\le\mathcal N_n\le\tfrac12A_n\).
**\(\theta=\tfrac14\) is fixed** for the rest of the phase.

## Status

- **Closed algebraically:** Theorems 1–3, Lemma 3.1, and Proposition 4.
- **Closed effectively:** the Johnston–Yang PNT triple is published and declared, so
  \(T_n(\theta)\) is computable.
- **Diagnostic executed:** `tools/theta_family_check.py`; it does not replace the exact proofs.
</content>
