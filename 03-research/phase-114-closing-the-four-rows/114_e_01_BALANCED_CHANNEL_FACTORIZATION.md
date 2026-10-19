# E.01 — The balanced channel factorization and the single-step contract

*Mathematical week 1 of the row (d) closure plan.*

## SCOPE CORRECTION (read first)

The initial version of this file claimed that \(X_0,Y_0,X_E,Y_E,S_E,\mathcal H_{5/4}\)
"are not defined in any `.tex`". **That was misleading.** They are defined in the
research corpus: the feature maps in **D.137**, and the reference Cholesky transform
with \(H,\widetilde X_E,S_E,A_N,y_N\) in **D.170 (1.1)-(1.4)**. What is true and much
smaller: those definitions **were not transferred to the paper**, so a referee who
reads only `row-d-local-analysis.tex` cannot audit §5 of that section. It is an
editorial task, not a research gap.

The derivation of §3 was done independently and **matches** D.170:
*"the entries of \(X\) contain the complete Gamma screw and every \(J_{p^k,-}\); the
entries of \(Y\) contain the \(\beta\)-line, the resolvent and every \(J_{p^k,+}\)"*
(D.170 §0). Its value is cross-verification and publishable form, not new
content.

**Moreover, D.170 is ahead of this file on one substantive point:** the correct
defect is the **output** one \(D_{\rm out}=I-A_NA_N^*\), not the input one
\(D_{\rm in}=I-A_N^*A_N\); the push-through identity \(I+A_ND_{\rm in}^\dagger A_N^*
=D_{\rm out}^\dagger\) connects them, and the capacity is
\(y_N^*D_{\rm out}^\dagger y_N\le I\) (D.170 (0.4)). The \(\Theta\) of §5.2 is a
different normalization from the \(v_N\) of D.170 (0.5).

What this file does contribute: the numerical verification (§2-§4), the
quantification of the scalar deficit (§4), Theorem 5.0 (R1), and the `114_e_00`
harness.

## Verdict

The balanced factorization exists, is **unique given the codomain convention**, and
is derived from `eq:localizedprimitiveoperator` with no free choice:

\[
 A_T=\underbrace{G_{\Gamma,T}+\sum_{n}w_n\,\widehat J_{n,-}^*\widehat J_{n,-}}_{R_T}
     -\underbrace{\Bigl(m_0I+\sum_{n}w_n\,\widehat J_{n,+}^*\widehat J_{n,+}\Bigr)}_{L_T},
 \qquad w_n=\frac{\Lambda(n)}{\sqrt n},
\]

with \(\widehat J_{n,\pm}F=(\widetilde F(\cdot+\log n)\pm\widetilde F)/\sqrt2\) as
operators \(L^2(I_T)\to L^2(\mathbb R)\). Both channels receive **the same** boundary
energy under extension by zero, which is exactly the closing sentence of
`row-d-local-analysis.tex:464-465`. This identifies
\(\mathcal H_{5/4}=G_{\Gamma,T}\) and confirms the coefficient \(\Lambda(n)/\sqrt n\) of
`prop:shiftchaincoercivity`.

Quantitative consequence (§4): **the scalar comparison fails by a factor of exactly
4 in the limit**, and the failure is leading order, not a margin. Since
`prop:shiftchaincoercivity` already proves that \(\alpha_N\sim\sqrt N\) is *sharp*, no
improvement of the shift-chain constant can close the door. The deficit \(3\sqrt N\)
must be paid by the Gamma channel together with the non-scalar structure.

---

## 1. The window, the primitive space, the operator

In logarithmic coordinates \(F(t)=e^{t/2}f(e^t)\), let \(I_T=(-T,T)\) and \(\widetilde F\)
the extension of \(F\) by zero to \(\mathbb R\). The two Tate moments are

\[
 M_\mp F=\int_{-T}^{T}F(t)e^{\mp t/2}\,dt,
 \qquad
 \mathcal P_T=\ker M_-\cap\ker M_+ ,
\]

the pullbacks of \(\widehat f(0),\widehat f(1)\) in `eq:twoprimitive`. The compressed
shift is \(S_aF=\bigl(\widetilde F(\cdot+a)\bigr)\big|_{I_T}\), so that \(S_a^*=S_{-a}\)
on \(L^2(I_T)\), and

\[
 A_T=G_{\Gamma,T}-m_0I-\sum_{2\le n<e^{2T}}w_n\,(S_{\log n}+S_{-\log n}),
 \qquad
 m_0=\log\pi+\gamma+\tfrac\pi2+3\log2 ,
\]

where \(G_{\Gamma,T}\) is the compression under extension by zero of the multiplier
\(g_\Gamma(\tau)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{i\tau}2)-\psi(\tfrac14)\).

**Positivity of the Gamma channel.** \(g_\Gamma\ge0\), with equality only at \(\tau=0\). Indeed
`eq:archenergy` (`main.tex:1093-1098`) gives
\(m_\infty(\tau)-m_\infty(0)=-\sum_{k\ge0}\frac{(\tau/2)^2}{(k+\frac14)((k+\frac14)^2+(\tau/2)^2)}\le0\)
with \(m_\infty(\tau)=\log\pi-\mathrm{Re}\,\psi(\frac14+\frac{i\tau}2)\); that is,
\(\mathrm{Re}\,\psi(\frac14+\frac{i\tau}2)\ge\psi(\frac14)\). Hence
\(G_{\Gamma,T}\ge0\). Numerically \(m_0=5.3721834192\ldots\)

Since \(S_{\log n}+S_{-\log n}=2\mathrm{Re}\,S_{\log n}\), we write
\(\sigma_T=\sum_{2\le n<e^{2T}}w_n\).

---

## 2. The zero-extension channels

**Definition 2.1.** For \(a>0\) let
\(\widehat J_{a,\pm}:L^2(I_T)\to L^2(\mathbb R)\),

\[
 \widehat J_{a,\pm}F=\frac{\widetilde F(\cdot+a)\pm\widetilde F}{\sqrt2}.
\]

**The codomain is \(L^2(\mathbb R)\), not \(L^2(I_T)\).** This statement is
load-bearing: under the truncated reading Lemma 2.2 is false and the constant of
`prop:shiftchaincoercivity` changes from \(1-\cos\frac\pi{m+1}\) to \(1-\cos\frac\pi{2m+1}\).

**Lemma 2.2.** \(\widehat J_{a,\pm}^*\widehat J_{a,\pm}=I\pm\mathrm{Re}\,S_a\).
In particular

\[
 \boxed{\;
 \mathrm{Re}\,S_a
 =\tfrac12\bigl(\widehat J_{a,+}^*\widehat J_{a,+}-\widehat J_{a,-}^*\widehat J_{a,-}\bigr),
 \qquad
 S_a+S_{-a}
 =\widehat J_{a,+}^*\widehat J_{a,+}-\widehat J_{a,-}^*\widehat J_{a,-}. \;}
\]

*Proof.* Translation is an isometry of \(L^2(\mathbb R)\), so
\(\|\widetilde F(\cdot+a)\|_{L^2(\mathbb R)}=\|F\|\). Since \(\widetilde F\) vanishes outside
\(I_T\),

\[
 \langle\widetilde F(\cdot+a),\widetilde F\rangle_{L^2(\mathbb R)}
 =\int_{I_T}\widetilde F(t+a)\overline{F(t)}\,dt
 =\langle S_aF,F\rangle_{L^2(I_T)} .
\]

Therefore
\(\|\widehat J_{a,\pm}F\|^2_{L^2(\mathbb R)}
 =\tfrac12\bigl(2\|F\|^2\pm2\mathrm{Re}\,\langle S_aF,F\rangle\bigr)
 =\|F\|^2\pm\mathrm{Re}\,\langle S_aF,F\rangle\).
Subtracting the two identities and using \(S_a^*=S_{-a}\) gives the boxed statement. \(\square\)

**Observation 2.3 (why the codomain matters).** The chain vertex at \(t=r-a\) falls
outside \(I_T\), but the channel \(\widehat J_{a,\pm}F\) does **not** vanish there: it equals
\(\pm\widetilde F(r)/\sqrt2\). Discarding that cell replaces
\(\widehat J^*\widehat J\) by \(\tfrac12(I-U^*)(I-U)=I-\mathrm{Re}\,U-\tfrac12P_{e_0}\)
in the discrete chain model, which is **not** of the form
(diagonal) \(-\mathrm{Re}\,\)(compressed shift) and hence does not reproduce the shift
term of \(A_T\). With the codomain of Definition 2.1 the chain of \(m\) vertices
has \(m+1\) edges (Dirichlet wall at both ends) and the smallest eigenvalue is
\(1-\cos\frac{\pi}{m+1}\), exactly as `prop:shiftchaincoercivity` states.

---

## 3. The balanced factorization

**Theorem 3.1 (balanced channel factorization).** On \(L^2(I_T)\),

\[
 A_T=R_T-L_T,
 \qquad
 R_T=G_{\Gamma,T}+\sum_{2\le n<e^{2T}}w_n\,\widehat J_{n,-}^*\widehat J_{n,-},
 \qquad
 L_T=m_0I+\sum_{2\le n<e^{2T}}w_n\,\widehat J_{n,+}^*\widehat J_{n,+},
\]

with \(\widehat J_{n,\pm}=\widehat J_{\log n,\pm}\). Both summands are positive, and

\[
 R_T=X_T^*X_T,\qquad L_T=Y_T^*Y_T,
\]

\[
 X_TF=\Bigl(G_{\Gamma,T}^{1/2}F,\;\bigl(\sqrt{w_n}\,\widehat J_{n,-}F\bigr)_n\Bigr),
 \qquad
 Y_TF=\Bigl(\sqrt{m_0}\,F,\;\bigl(\sqrt{w_n}\,\widehat J_{n,+}F\bigr)_n\Bigr),
\]

as operators from \(L^2(I_T)\) into
\(L^2(I_T)\oplus\bigoplus_{n}L^2(\mathbb R)\).

*Proof.* By Lemma 2.2,
\(-w_n(S_{\log n}+S_{-\log n})
 =w_n\widehat J_{n,-}^*\widehat J_{n,-}-w_n\widehat J_{n,+}^*\widehat J_{n,+}\).
Sum over \(n\) and add \(G_{\Gamma,T}-m_0I\). The positivity of \(G_{\Gamma,T}\) is
§1. \(\square\)

**Corollary 3.2 (identification with the paper's notation).**
\(\widehat{\mathcal R}_T=R_T\) and \(\mathcal H_{5/4}=G_{\Gamma,T}\). The coefficient
\(\Lambda(n)/\sqrt n\) of `prop:shiftchaincoercivity` — and not \(2\Lambda(n)/\sqrt n\) — is
the correct one precisely because the split is balanced.

**Observation 3.3.** The factorization is unique given the codomain convention: any
other assignment of the term \(\mathrm{Re}\,S_a\) between the two signs breaks the
boundary-energy symmetry and hence the sentence `row-d-local-analysis.tex:464-465`.

---

## 4. The scalar deficit is leading order and equals exactly 4

**Proposition 4.1.** With \(N=e^{2T}\),

\[
 L_T\le(m_0+2\sigma_N)I,
 \qquad
 R_T\ge\alpha_NI
 \quad\text{(`prop:shiftchaincoercivity`, discarding }G_{\Gamma,T}),
\]

\[
 \sigma_N=\sum_{2\le n<N}\frac{\Lambda(n)}{\sqrt n}\sim2\sqrt N,
 \qquad
 \alpha_N\sim\sqrt N .
\]

Hence the scalar sandwich \(\alpha_N\ge m_0+2\sigma_N\) **fails**, with

\[
 \boxed{\;\lim_{N\to\infty}\frac{\alpha_N}{m_0+2\sigma_N}=\frac14 .\;}
\]

*Measurement* (`114_e_01_balanced_factorization_verify.py`):

| \(N\) | \(\sigma_N\) | \(\alpha_N\) | \(m_0+2\sigma_N\) | ratio | \(\sigma_N/\sqrt N\) | \(\alpha_N/\sqrt N\) |
|---|---|---|---|---|---|---|
| 5 | 1.4710 | 0.6340 | 8.3142 | 0.07625 | 0.65785 | 0.28353 |
| 200 | 26.1663 | 11.7300 | 57.7048 | 0.20328 | 1.85024 | 0.82943 |
| 5000 | 138.7319 | 65.5772 | 282.8359 | 0.23186 | 1.96196 | 0.92740 |
| 100000 | 629.9414 | 306.4512 | 1265.2549 | 0.24221 | 1.99205 | 0.96908 |

**Corollary 4.2 (no-go for the scalar route, unconditional).**
`prop:shiftchaincoercivity` further proves that \(\alpha_N\sim\sqrt N\) is **sharp** (the
upper bound matches, because every bracket is \(\le\frac12\) for \(n<N\)). Hence
no improvement of the shift-chain coercivity constant can close the door:
the deficit is \(3\sqrt N\), leading order. It must be paid by \(G_{\Gamma,T}\) together
with the non-scalar structure of the Schur complement.

This explains structurally — and not as a numerical accident — why
`114_d_207` shows that no internal split improves the scalar bound, and why
`114_d_209` observes 43 negative directions.

---

## 5. One step: defects, normalized cross, and \(\Theta\)

### 5.1 Parametrization by consecutive prime powers (R1)

The contact list of \(A_T\) changes only when \(e^{2T}\) crosses a prime power.
Let \(2=q_1<q_2<q_3<\cdots\) be the ordered sequence of prime powers and
\(\tau_j=\frac12\log q_j\). On \((\tau_j,\tau_{j+1})\) no contact is born. By the
nesting principle (`row-d-local-analysis.tex:233-240`) it suffices to prove positivity at the
right endpoint of each interval, so the step is
\(\mathcal P_{\tau_j}\to\mathcal P_{\tau_{j+1}}\).

**Theorem 5.0 (R1: the step is exact).** Let \(\mathcal E:\mathcal P_{\tau_j}\to
\mathcal P_{\tau_{j+1}}\) be the extension by zero and \(\mathcal C=\mathcal E(\mathcal P_{\tau_j})\).
Then:

1. the contact list is constant and equal to \(\{q_1,\dots,q_j\}\) throughout
   \((\tau_j,\tau_{j+1}]\);
2. **the birth is null on the core.** The incoming contact \(q_j\) has shift length
   \(\log q_j=2\tau_j\), which is *exactly* the width of the old window; hence
   for \(F\) supported on \(I_{\tau_j}\) the supports of \(\widetilde F(\cdot+\log q_j)\)
   and of \(F\) are disjoint and \(\langle(S_{\log q_j}+S_{-\log q_j})F,F\rangle=0\);
3. the Gamma channel is independent of the window on functions extended by zero,
   because \(\langle G_{\Gamma,T}F,F\rangle=\frac1{2\pi}\int g_\Gamma|\widehat{\widetilde F}|^2\)
   does not mention \(T\);
4. **consequently \(\mathcal E^*A_{\tau_{j+1}}\mathcal E=A_{\tau_j}\) exactly:** the
   old core block receives no correction from the newly born contact;
5. \(\mathcal A=\mathcal C^\perp\) within \(\mathcal P_{\tau_{j+1}}\) decomposes as
   \[
    \mathcal A=\bigl(\text{primitives supported on the ring}\bigr)\;\oplus\;
    \mathrm{span}\,\{e^{-t/2},e^{t/2}\}\big|_{I_{\tau_j}},
   \]
   that is, the ring **plus exactly two** directions, and those two are the Tate
   modes restricted to the core.

*Proof.* (1) the only \(n\in[q_j,q_{j+1})\) with \(\Lambda(n)\ne0\) is \(q_j\).
(2) the shift \(a=2\tau_j\) sends \(I_{\tau_j}=(-\tau_j,\tau_j)\) into \((-3\tau_j,-\tau_j)\),
disjoint from \(I_{\tau_j}\) except for one point. (3) by definition of the compression of the
multiplier. (4) subtracting the two forms, the difference is
\(-w_{q_j}\langle(S_{\log q_j}+S_{-\log q_j})F,F\rangle\), null by (2).
(5) \(F\in\mathcal A\) iff \(F|_{I_{\tau_j}}\perp\mathcal P_{\tau_j}\) in \(L^2(I_{\tau_j})\);
since \(\mathcal P_{\tau_j}\) is the kernel of two functionals, its orthogonal complement in
\(L^2(I_{\tau_j})\) is the span of the two restricted Tate vectors. \(\square\)

Verified in `114_e_02_r1_prime_power_step_verify.py` (15 checks; the dimension count
of (5) gives `extra = 2` in the four steps tested, with nesting residual
\(\sim5\times10^{-14}\)).

**Observation 5.0.1.** Point (5) is a direct input for route E1: the "two neutral
Tate channels" of the colligation are not a design choice — they are literally the
two dimensions the corona has above the ring.

### 5.2 The two defect operators

At the end of the step, \(\mathcal P_{\tau_{j+1}}=\mathcal C\oplus\mathcal A\) (transported
old core ⊕ nascent corona). In that decomposition the balanced form gives

\[
 A=\begin{pmatrix}A_{\rm old}&B\\B^*&A_{\rm new}\end{pmatrix},
 \qquad
 A_{\rm old}=R_0-L_0,
 \quad
 A_{\rm new}=S_E-L_E,
 \quad
 B=X_0^*X_E-Y_0^*Y_E,
\]

with \(R_0=X_0^*X_0\), \(L_0=Y_0^*Y_0\) (old channels) and \(S_E=X_E^*X_E\),
\(L_E=Y_E^*Y_E\) (corona channels). The **two** defect operators are

\[
 \boxed{\;
 D_0=I-T_0,\quad T_0=R_0^{\dagger/2}L_0R_0^{\dagger/2};
 \qquad
 \mathfrak D=I-T_E,\quad T_E=S_E^{\dagger/2}L_ES_E^{\dagger/2}. \;}
\]

Then \(A_{\rm old}=R_0^{1/2}D_0R_0^{1/2}\) and \(A_{\rm new}=S_E^{1/2}\mathfrak DS_E^{1/2}\)
on the respective supports; in particular the old-core hypothesis \(0\le T_0\le I\)
of the paper is exactly \(A_{\rm old}\ge0\).

The **normalized cross** and the **transfer** are

\[
 Q_c=R_0^{\dagger/2}\,B\,S_E^{\dagger/2},
 \qquad
 \boxed{\;\Theta=D_0^{\dagger/2}\,Q_c\,\mathfrak D^{\dagger/2}.\;}
\]

\(\Theta\) transports the corona's defect space to the old core's defect space;
it is normalized by **both** defects, which is what makes the goal
\(\|\Theta\|\le1\) a constant-one target rather than an unnormalized budget.

### 5.3 D1 — the single-step theorem, in regularized form

**Theorem 5.1 (D1).** Suppose \(A_{\rm old}\ge0\). For \(\varepsilon>0\) let

\[
 \mathcal C_\varepsilon
 =\mathfrak D-Q_c^*\bigl(D_0+\varepsilon I\bigr)^{-1}Q_c .
\]

Then:

1. \(\varepsilon\mapsto\mathcal C_\varepsilon\) is **decreasing** as \(\varepsilon\downarrow0\);
2. \(A\ge0\iff\mathcal C_\varepsilon\ge0\) for all \(\varepsilon>0\);
3. if (2) holds, the monotone limit
   \(\lim_{\varepsilon\downarrow0}Q_c^*(D_0+\varepsilon)^{-1}Q_c\) is bounded, which
   **forces** \(\mathrm{Ran}\,Q_c\subseteq\mathrm{Ran}\,D_0^{1/2}\), and the limit is
   \(Q_c^*D_0^\dagger Q_c\); consequently
   \(\mathfrak D-Q_c^*D_0^\dagger Q_c\ge0\) and \(\|\Theta\|\le1\).

*Proof.* (1) \(\varepsilon\mapsto(D_0+\varepsilon)^{-1}\) is decreasing in the operator
order, so \(Q_c^*(D_0+\varepsilon)^{-1}Q_c\) is decreasing and
\(\mathcal C_\varepsilon\) is increasing in \(\varepsilon\).

(2) For \(\varepsilon>0\) the block \(A_{\rm old}+\varepsilon\) is invertible on its
support, so by the Schur complement
\(\begin{psmallmatrix}A_{\rm old}+\varepsilon&B\\B^*&A_{\rm new}\end{psmallmatrix}\ge0
\iff A_{\rm new}-B^*(A_{\rm old}+\varepsilon)^{-1}B\ge0\).
Conjugating by \(S_E^{\dagger/2}\) and using
\(A_{\rm old}^{}=R_0^{1/2}D_0R_0^{1/2}\) gives
\(S_E^{\dagger/2}\bigl(A_{\rm new}-B^*(A_{\rm old}+\varepsilon)^{-1}B\bigr)S_E^{\dagger/2}
 =\mathcal C_{\varepsilon'}\) with the corresponding rescaling of \(\varepsilon\).
Finally \(A\ge0\iff A+\varepsilon(P_{\mathcal C}\oplus0)\ge0\) for all
\(\varepsilon>0\), by continuity of the quadratic form as \(\varepsilon\to0\).

(3) This is Douglas's criterion in its shorted-operator form: the monotone
supremum \(\sup_{\varepsilon>0}Q_c^*(D_0+\varepsilon)^{-1}Q_c\) is bounded if and only if
\(\mathrm{Ran}\,Q_c\subseteq\mathrm{Ran}\,D_0^{1/2}\), and then it coincides with
\(Q_c^*D_0^\dagger Q_c\). \(\square\)

**Observation 5.2.** The value of (3) is methodological: **the range inclusion
stops being an independent hypothesis** and becomes a consequence of the regularized
estimate. That is why every conservative identity (route E1) must first be proved in
the form

\[
 \mathcal C_\varepsilon
 =Z_\varepsilon^*Z_\varepsilon+E_\varepsilon,
 \qquad E_\varepsilon\ge0,
\]

and only afterward passed to the limit.

### 5.4 The normalized Schur kernel

If an analytic family \(\Theta(z)\) is built with \(\Theta(0)=\Theta\), the kernel is

\[
 K(z,w)=\frac{I-\Theta(z)^*\Theta(w)}{1-\bar zw},
\]

with \(I\) in the numerator — \(\Theta\) already carries \(\mathfrak D^{\dagger/2}\)
built in, so writing \(\mathfrak D-\Theta(z)^*\Theta(w)\) would mix an unnormalized
budget with a normalized transfer.

---

## 6. What remains of Week 1

- **Done:** §2 (Lemma 2.2), §3 (Theorem 3.1 + Cor 3.2), §4 (Prop 4.1 + Cor 4.2),
  §5.1 (Theorem 5.0 = R1), §5.2-5.4 (defects, \(\Theta\), D1 = Theorem 5.1, corrected
  kernel).
- **Pending:** extraction of the counterfactual harness → `114_e_00`.

**Week 1 gate:** \(\Theta\) is defined unambiguously (§5.2). **The gate
opens.**

### What Week 1 changes for D2

1. **The scalar route is closed for a structural reason** (Cor 4.2), not for lack
   of numerical effort: the deficit is \(3\sqrt N\), leading order, and the
   shift-chain coercivity is sharp.
2. **The step is exactly isolated** (Theorem 5.0): the old core block is
   literally \(A_{\tau_j}\), so induction does not accumulate error between steps.
3. **The two Tate channels are identified geometrically** (Theorem 5.0(5)): they are
   the two dimensions the corona has above the ring. The exact compression of
   those two channels in the colligation (step 3 of program E1) now has a
   concrete object to act on.
4. **The range inclusion stopped being a hypothesis** (Theorem 5.1(3)).

---

## Scope

**Proved here.** Lemma 2.2; Theorem 3.1 and Corollary 3.2; Proposition 4.1 (the bound
part; the asymptotic \(\alpha_N\sim\sqrt N\) is cited from `prop:shiftchaincoercivity`);
Corollary 4.2; Theorem 5.0 (R1); Theorem 5.1 (D1).

**Verified numerically.** Lemma 2.2 and Theorem 3.1 to \(2.9\times10^{-14}\) over six
configurations \((T,a)\); Observation 2.3 (the two spectral constants); the table of
§4 up to \(N=10^5\); D1 over 200 cases with \(D_0\) singular. See
`114_e_01_balanced_factorization_verify.py` (17 checks). Theorem 5.0 in
`114_e_02_r1_prime_power_step_verify.py` (15 checks).

**Read from source.** `row-d-local-analysis.tex`; `main.tex:1093-1098` (positivity of
\(g_\Gamma\)); `114_d_207`, `114_d_209`.

**Not established.** D2 (uniform contractivity), D3, D4. Whether \(G_{\Gamma,T}\) plus
the Schur structure suffices to pay the deficit \(3\sqrt N\) of §4 — that is exactly the
content of D2. **RH is not proved.**
