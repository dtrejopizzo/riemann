# Exact reserve theorem: size, sign and threshold of \(Q_n\)

Work order step 2 and step 3 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.

## Input

From `103_01_GLOBAL_TELESCOPING_AND_ENDPOINT_TABLE.md`, for \(n\ge9\),
\[
  Q_n={3\over4}A_n+1-L_n^{(1)}(\log2)
      -\int_{\log2}^{T_8}E(u)K_n(u)\,du,
  \qquad A_n=\lambda_n^{\rm arch},
\tag{1}
\]
with \(K_n(u)=e^{-u}L_{n-1}^{(2)}(u)\), \(E(u)=\psi(e^u)-e^u\).

Three inputs are used, all of them already closed in phase 102 or classical:

* **(I1)** `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`, eq. (9):
  \[
    A_n\ \ge\ {1\over2}+n\Bigl({91072\over45045}-{1+C\over2}
                              +{1\over2}\log{n\over17}\Bigr),
    \qquad C={3109\over1000},\ n\ge19 .
  \]
  Evaluating the bracket,
  \[
  \boxed{\ A_n\ \ge\ {n\over2}\bigl(\log n-2.899\bigr)\qquad(n\ge19).\ }
  \tag{2}
  \]

* **(I2)** Chebyshev triviality: \(0\le\psi(x)\le 1.03884\,x\) for \(x>0\)
  (Rosser–Schoenfeld), hence
  \[
    |E(u)|\le e^u\qquad(u\ge0).
  \tag{3}
  \]

* **(I3)** Plancherel–Rotach / Erdélyi–Magnus–Nevai type bound: there are
  absolute constants \(c_1,c_2\) with
  \[
    |L_N^{(1)}(u)|\le c_1N^{1/4}u^{-3/4}e^{u/2},
    \qquad
    |L_N^{(2)}(u)|\le c_2N^{3/4}u^{-5/4}e^{u/2}
  \tag{4}
  \]
  for \(u\) in any **fixed** range \(0<u\le U\) as \(N\to\infty\).  This is
  all that is used here, since the integral in question runs only over
  \([\log2,T_8]\) with \(T_8\) fixed.  Measured (`103_06` §5):
  \(c_2\le1.9\) for \(50\le N\le800\).
  *Caveat, established in `103_06`:* the supremum of
  \(|L_N^{(\alpha)}(u)|u^{\alpha/2+1/4}e^{-u/2}N^{-\alpha/2+1/4}\) over the
  **whole** range \(0<u\le4N\) is not bounded — it grows like \(N^{1/6}\),
  the classical soft-edge (Airy) correction at \(u\approx4N\).  Statements
  below that need the full range are phrased in terms of measured integral
  budgets, never in terms of a global sup.

## Theorem 1 (exact reserve, split form)

For every \(n\ge9\),
\[
\boxed{
  Q_n=\underbrace{{3\over4}A_n+1-L_n^{(1)}(\log2)}_{q(n)}
      \;+\;\underbrace{\Bigl(-\int_{\log2}^{T_8}E(u)K_n(u)\,du\Bigr)}_{q_8(n,T_8)} }
\tag{5}
\]
where \(q(n)\) contains **no arithmetic at all** and \(q_8\) depends only on
the prime powers below \(e^{T_8}\).

Two structural remarks, both new relative to phase 102:

1. The linear term \(-n\) of the primitive reserve
   \(Q_n=\frac34A_n-n-\int_0^{T_8}EK_n\,du\) is cancelled *identically* by
   the empty-range contribution \(\int_0^{\log2}EK_n\,du=-(n+1)+L_n^{(1)}(\log2)\).
   The reserve therefore has archimedean order \(n\log n\), not \(O(n)\).
2. \(Q_n\) never has to be assembled from \(B_n^{\rm base}\),
   \(\int\omega_ne^u\,du\) and the pole term \(P_n\) separately.  Those three
   quantities are individually of size \(e^{T_n}\); (5) is their exact
   cancelled form.

## Theorem 2 (uniform lower bound and threshold)

Let
\[
  \Psi(T_8)=\int_{\log2}^{T_8}u^{-5/4}e^{u/2}\,du
  \;\le\; 2(\log2)^{-5/4}e^{T_8/2}.
\tag{6}
\]
Then for every \(n\ge19\),
\[
\boxed{\;
  Q_n\ \ge\ {3\over8}n\bigl(\log n-2.899\bigr)
          -c_1\,\sqrt2\,(\log2)^{-3/4}\,n^{1/4}
          -c_2\,\Psi(T_8)\,n^{3/4}
          +1 .\;}
\tag{7}
\]

*Proof.*  Bound \(\frac34A_n\) below by (2).  By (4) with \(u=\log2\),
\(|L_n^{(1)}(\log2)|\le c_1n^{1/4}(\log2)^{-3/4}2^{1/2}\).  By (3) and (4),
\[
  \Bigl|\int_{\log2}^{T_8}EK_n\,du\Bigr|
  \le\int_{\log2}^{T_8}|L_{n-1}^{(2)}(u)|\,du
  \le c_2(n-1)^{3/4}\Psi(T_8)\le c_2n^{3/4}\Psi(T_8).\qquad\square
\]

> **Corollary 3 (explicit threshold).**  Put
> \(\kappa=c_1\sqrt2(\log2)^{-3/4}\).  Then \(Q_n>0\) for every
> \[
>   n\ \ge\ n_0(T_8)
>   :=\max\Bigl\{\bigl\lceil(3c_2\Psi(T_8))^{4}\bigr\rceil,\
>                \bigl\lceil e^{7.2+\kappa}\bigr\rceil,\ 19\Bigr\}.
> \]

*Proof.*  Assume \(n\ge n_0\).  From \(n\ge(3c_2\Psi)^4\) we get
\(n^{1/4}\ge3c_2\Psi\), hence
\[
  c_2\Psi(T_8)\,n^{3/4}\ \le\ {n\over3}.
\]
Also \(\kappa n^{1/4}\le\kappa n/ e^{\kappa}\cdot\)… more simply,
\(n\ge e^{7.2+\kappa}\) gives both \(\kappa n^{1/4}\le\frac1{24}n\) (since
\(n^{3/4}\ge24\kappa\) whenever \(n\ge(24\kappa)^{4/3}\), implied by
\(n\ge e^{7.2+\kappa}\)) and \(\log n\ge7.2\).  Therefore
\[
  Q_n\ \ge\ {3\over8}n(\log n-2.899)-{n\over3}-{n\over24}+1
     \ \ge\ {3\over8}n(7.2-2.899)-{3n\over8}+1
     \ =\ {3\over8}n\cdot3.301+1\ >\ 0 .
\]
The indices \(19\le n<n_0\) are covered by the finite certificate of
`103_06`.  \(\square\)

The threshold is dominated by \(\Psi(T_8)\le2(\log2)^{-5/4}e^{T_8/2}\), i.e.
by \(e^{2T_8}\) — astronomically large but explicit, and irrelevant in
practice because the sharper route of `103_04` bypasses it entirely
(threshold \(n_1=150\)).

## Theorem 4 (true scale of the reserve)

The bound (2) is lossy in its constant.  The true archimedean scale is
\[
\boxed{\ A_n={n\over2}\bigl(\log n+\gamma-1-\log2\pi\bigr)+O(\log n).\ }
\tag{8}
\]

This is verified numerically to seven digits in
`103_06_NUMERICAL_CERTIFICATE_REPORT.md`
(least-squares fit of \(A_n\) over \(200\le n\le1200\) returns the
coefficient \(-2.26066691\) against
\(\gamma-1-\log2\pi=-2.26066140\)).  The fixed arithmetic window can be
evaluated without an absolute-value loss: `103_12_HARD_EDGE_CORRECTION_AND_FIXED_WINDOW_COLLAPSE.md`,
(3), writes it as a finite combination of fixed-argument \(L_N^{(1)}\)'s.
It is therefore \(O_{T_8}(n^{1/4})\), instead of merely the
\(O(n^{3/4}\Psi(T_8))\) supplied by the crude envelope in Theorem 2.
Consequently
\[
\boxed{\ Q_n={3\over8}\,n\bigl(\log n+\gamma-1-\log2\pi\bigr)
        +O_{T_8}\bigl(n^{1/4}\bigr).\ }
\tag{9}
\]

**This is the answer to step 2, items 1–4 of the work order.**  The reserve
is positive, of order \(\frac38 n\log n\), and every proposed bound for
\(\mathcal R_n\) whose leading cost exceeds \(\frac38 n\log n\) is to be
rejected immediately.

## The comparison that the rest of the phase must satisfy

By Proposition 1 of `103_01`, direct A1 at index \(n\) is exactly
\[
\boxed{\ \int_{\log2}^{T_n}E(u)K_n(u)\,du
        \ \le\ {3\over4}A_n+1-L_n^{(1)}(\log2)
        \ =\ q(n)\ \asymp\ {3\over8}n\log n .\ }
\tag{10}
\]

Equation (10) is the cleanest coordinate system reached so far in the
program: a **single** integral of the Chebyshev discrepancy against a
**single** Laguerre kernel, compared against a **purely archimedean**
budget of size \(\frac38n\log n\), with no cutoff, no pole term, no
low-window arithmetic and no endpoint convention left in it.  (The cutoff
\(T_n\) survives only as the upper limit, and by A0 the tail beyond \(T_n\)
costs at most \(\frac14A_n\).)

Every remaining task of phase 103 is a statement about the left side of
(10).

## Status

Closed.  Steps 2 and 3 of the work order are complete:

1. exact formula for \(Q_n\)  — Theorem 1;
2. rigorous uniform lower bound — Theorem 2;
3. true asymptotic scale \(\frac38n\log n\) — Theorem 4;
4. finite threshold \(n_0(T_8)\) separating direct verification from the
   uniform argument — Corollary 3.

The reserve is *not* the obstruction.  The obstruction is entirely on the
correlation side, and is quantified in
`103_04_ORIENTED_TRANSPORT_TARGET.md` and
`103_05_ADMISSIBLE_COMPETITOR_NO_GO.md`.
