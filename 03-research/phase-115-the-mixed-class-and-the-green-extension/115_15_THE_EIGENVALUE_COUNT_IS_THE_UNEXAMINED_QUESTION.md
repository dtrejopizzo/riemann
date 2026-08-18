# 115.15 — Point 5: what \(E\le0\) actually costs, and the one question nobody has asked

Point 5 of the attack order.  \(E\le0\) without support restriction is
Connes–Consani's own open problem; this note records its exact state, and
identifies a concrete, unexamined computation that would decide it.

All statements below are from arXiv:2006.13771 (Selecta Math 27 (2021) no. 4,
paper 77) with the numbering of that paper, or from the 2020–2026 literature.

## 1. Theorem 3 is unrestricted; the restriction is entirely in the sign of \(E\)

**Theorem 4.7** (= Theorem 3 of the introduction), eq. (83): for **all**
\(f\in C_c^\infty(\mathbb R_+^*)\),

\[
 \operatorname{Tr}\bigl(\vartheta(f)\mathbf S\bigr)=W_\infty(f)+\int f(\rho^{-1})\epsilon(\rho)\,d^*\rho,
\]

with \(\epsilon(\rho^{-1})=\epsilon(\rho)\) and, for \(\rho\ge1\) (eq. (84)),
\(\epsilon(\rho)=\sum_n\frac{\lambda(n)}{\sqrt{1-\lambda(n)^2}}\langle\xi_n\mid\vartheta(\rho^{-1})\zeta_n\rangle\).

So `115_09`/`115_14`'s use of Theorem 3 with no support hypothesis is correct.
Everything difficult sits in the sign of \(E(f)=\int f(\rho^{-1})\epsilon\,d^*\rho\).

## 2. The negativity of \(E\circ Q\), and its length bound

**Proposition 5.5.**  *Let \(I\subset[-\log2,\log2]\) be an interval of length
\(\le\log2\).*  Then \(N_I=-2\epsilon'(1^{+})(\mathrm{Id}-K_I)\) with \(K_I\)
compact (Hilbert–Schmidt), kernel (104) built from \((Q\epsilon)(e^{|v|})\).

Two things matter here and were not appreciated in `115_09`.

* The bound \(|I|\le\log2\) is **used in the proof**, not decorative: it is what
  makes \(f(v)=\int\eta(x)\xi(x+v)dx\) vanish outside \([-\log2,\log2]\) so that
  (102) collapses to (104).  **For \(|I|>\log2\) the operator \(N_I\) is not even
  defined by that formula.**  Extending requires redoing (102)→(104) with the
  tail of \((Q\epsilon)(e^{|v|})\) beyond \(\log2\), which the paper never does.
* \(\epsilon'(1^{+})\approx22.9965\) (Lemma 5.4) is a **numerical** sum
  \(\sum_n\frac{\lambda(n)^2}{1-\lambda(n)^2}\xi_n(1)^2\), terms
  \(11.9719,\ 8.77574,\ 2.20528,\ 0.0433983,\ 1.25\times10^{-4},\dots\); no
  closed form.  It is the jump of \(\epsilon'\) at \(\rho=1\).

## 3. The mechanism at the one interval where it is done

At \(I=[2^{-1/2},2^{1/2}]\), §6 establishes:

* **exactly one** eigenvalue of \(K_I\) exceeds 1:
  \(\lambda_{\max}\approx1.05158\), with the rigorous separation
  \(\lambda_2\le0.772216\) (Lemma 6.8(iii)) and \(\|K_I-T\|\le0.00122\)
  (Fact 6.1, \(m=1732\));
* the single bad eigenvector \(\zeta\) is **nearly parallel to the constant
  function** \(\xi_0\): \(\langle\zeta\mid\xi_0\rangle\approx0.94865\)
  (Fact 6.5), and \(\langle\xi_0\mid\xi\rangle\) is, up to a factor,
  \(\widehat g(0)\);
* hence Lemma 6.10 gives \(\langle\xi\mid N_I\xi\rangle\le\gamma|\langle\xi_0\mid\xi\rangle|^2\),
  \(\gamma\approx2.94355\), and **Theorem 6.11**: for
  \(g\in C_c^\infty([2^{-1/2},2^{1/2}])\) with \(\widehat g(-i/2)=0\),
  \[
   W_\infty(g*g^*)\ \ge\ \operatorname{Tr}\bigl(\vartheta(g)\mathbf S\vartheta(g)^*\bigr)-c\,|\widehat g(0)|^2,
   \qquad c=4\gamma/\log2,\ \ 13<c<17 .
  \]

> **The finite codimension is one, and the one condition is the character
> condition \(\widehat g(0)=0\).**  That is why it is harmless: it is already
> part of the definition of the test space, not an extra imposition.

This is a much sharper mechanism than `115_09` assumed, and it is the reason the
whole approach is not vacuous.

## 4. The unexamined question

> **How does the number of eigenvalues of \(K_I\) exceeding 1 grow with \(|I|\)?**

**Nobody has asked.**  The word "codimension" appears twice in the entire paper,
both times qualitative.  Figure 11 plots \(\lambda_{\max}\) only for
\(a\in[0,\log2]\) at \(q=e^{10^{-3}}\); the paper does not even record where it
crosses 1.  A full citation sweep of arXiv:2006.13771 (16 citing works,
2020–2026, including Connes' Feb 2026 survey arXiv:2602.04022, CCM
arXiv:2511.22755, Connes–van Suijlekom arXiv:2511.23257, Suzuki
arXiv:2606.09096, Groskin arXiv:2605.20224 and arXiv:2607.02828, Kim et al.
arXiv:2607.24830) turns up **no bound, no numerical experiment, and no
conjecture** on this count.  Six years, and it appears never to have been
examined.

**Why it is decisive.**  If the count stays at 1 as \(|I|\) grows, and the bad
direction stays nearly parallel to \(\xi_0\), then Theorem 6.11's argument
extends verbatim to every window, and \(E\le0\) holds on the test space
(where \(\widehat g(0)=0\) already).  That is exactly what row (d) needs.  If the
count grows, the mechanism fails and the route closes.

**One structural fact pointing the right way, which CC state but do not use.**
**Remark 5.6**: \((Q\epsilon)(1)=0\), so the integral of the diagonal values of
the \(\epsilon\)-side kernel is **zero independently of \(|I|\)** — whereas for the
\(\delta\)-side kernel of Theorem 3.6 the trace is proportional to \(|I|\)
(Figure 8 shows \(Q_+\delta(e^x)\approx15\) at \(x=0\)).  So
\(\operatorname{tr}K_I=0\) for every \(I\), and any eigenvalue above 1 must be
compensated by negative ones.  This is the only statement in the paper about how
\(K_I\) degrades with \(|I|\), and it is not turned into a count.

*It does not by itself bound the count.*  The trivial consequence
\(\#\{\lambda_j>1\}\le\|K_I\|_{HS}^2\approx|I|\int|\chi|^2\) grows linearly and
proves nothing.  Recorded here so it is not mistaken for evidence.

## 5. The contrast with the \(\delta\)-functional, which is genuinely dead

For \(D\) (their §3) the picture is worse and settled:

* **Theorem 3.6**: \(D\circ Q(\xi*\xi^*)=-2\|\xi\|^2+\langle\xi\mid K_I\xi\rangle\),
  \(K_I\) Hilbert–Schmidt, for any bounded symmetric \(I\).
* **Corollary 3.8**: \(D\circ Q\le0\) on \(I=[u^{-1},u]\), \(u=1.10246\);
  **Remark 3.9(i)** improves to \(u=1.15077\) via Boas–Kac.
* **Remark 3.9(ii)**: \(D\circ Q\) is **not** negative on \([2^{-1},2]\).  The
  counterexample is explicit: \(g_\epsilon=\phi_\epsilon*\mathbf 1_{[\epsilon,\log2-\epsilon]}\),
  \(f_\epsilon=g_\epsilon*g_\epsilon^*\), whose \(\epsilon\to0\) limit is the
  triangle (Fejér) kernel of half-width \(\log2\), with
  \(\lim_{\epsilon\to0}D_+(Q_+f_\epsilon)\approx+2.98699>0\).

This confirms `115_11`'s record: the \(-D\ge K\) route is closed by
counterexample.  The \(\epsilon\) route is **not** in the same position — the
whole difference is Remark 5.6's \(\operatorname{tr}K_I=0\).

Separately, at the top of §3 there is a counterexample showing the support
condition is needed for \(W_\infty\) itself: \(\widehat g(t)=(1+4t^2)e^{-t^2/4}\)
satisfies the vanishing conditions but has \(W_\infty(f)\approx-28.8971<0\).
Its support is **unbounded**, so it does not bear on compactly supported test
functions.

## 6. Status

* Theorem 3 unrestricted: **CONFIRMED**; `115_14`'s use is legitimate.
* Prop. 5.5 restricted to \(|I|\le\log2\), the bound used in the proof:
  **CONFIRMED**; \(N_I\) is undefined by that formula beyond.
* Codimension at \(I=[2^{-1/2},2^{1/2}]\) is **one**, and the one condition is
  \(\widehat g(0)=0\): **PROVED by CC** (Fact 6.5, Lemmas 6.9–6.10, Thm 6.11).
* Growth of the count with \(|I|\): **NOT EXAMINED BY ANYONE**, 2020–2026.
* \(\operatorname{tr}K_I=0\) for all \(I\) (Remark 5.6): **stated by CC, unused**.
* \(E\le0\) without support restriction: **OPEN**.
* Row (d): **OPEN**.

## 7. The experiment

Compute \(\#\{\lambda_j(K_I)>1\}\) and \(\langle\zeta\mid\xi_0\rangle\) for
\(|I|>\log2\).  Requires: (i) extending (102)→(104) with the tail of
\((Q\epsilon)(e^{|v|})\) beyond \(\log2\) — CC's Lemma F.1(ii) bounds the prolate
truncation only on \(\rho\in[1,2]\), so the tail bound has to be redone;
(ii) the Toeplitz discretisation of §6.1, which is straightforward once the
kernel is available.

This is the first thing in this phase that is both **unexamined in the
literature** and **decidable by computation** rather than by a new theorem.
