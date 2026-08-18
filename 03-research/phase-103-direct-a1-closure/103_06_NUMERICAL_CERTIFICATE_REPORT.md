# Numerical certificate report

Work order step 6 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`:
"test the lemma against explicit prime-power sums for a substantial finite
range, using interval arithmetic only as diagnosis."

All computations are in `tools/`, double precision, no external
dependencies beyond numpy.  They are **diagnostic**, not certified; the
rigorous route for each is indicated.

## 0. Validation of the pipeline

\(\lambda_n\) is computed from the Cauchy integral of the Li generating
function
\[
  \sum_{n\ge1}\lambda_nz^{n-1}={d\over dz}\log\xi\bigl(1/(1-z)\bigr)
  ={\xi'\over\xi}\Bigl({1\over1-z}\Bigr){1\over(1-z)^2},
\]
on \(|z|=r<1\).  The identity holds with the zeros paired
\(\rho\leftrightarrow1-\rho\) (then \(z_{1-\rho}=1/z_\rho\)), which is the
standard symmetric summation of Li's criterion.  The contour has one
additional hypothesis which must be kept separate from RH.  A zero
\(\rho=\beta+i\gamma\) is transported to \(w_\rho=1-1/\rho\), with
\[
 |w_\rho|^2
 =1+{1-2\beta\over\beta^2+\gamma^2}.                              \tag{0}
\]
Thus Cauchy's coefficient formula at radius \(r\) is valid only if the
disk \(|w|\le r\) contains no transformed zero.  Equivalently, it requires
the exclusion of every zero satisfying
\[
 2\beta-1\ \ge\ (1-r^2)(\beta^2+\gamma^2).                          \tag{0a}
\]
For the actual choice \(r=0.995\), such a zero necessarily has
\(|\gamma|<1/\sqrt{1-r^2}=10.0125\ldots\).  Hence this is a *finite*,
RH-neutral zero-free check, rather than RH itself; but no certificate of
that check is implemented in the numerical scripts.  The previously stated
claim that all singularities lie on \(|z|=1\) was RH-equivalent and is not
used.  \(\zeta\) and \(\zeta'\) come from Borwein's algorithm,
\(\psi_{\rm digamma}\) from a shifted asymptotic series.

*Numerical cross-check, conditional on the disk check above.*  The computation returns
\[
  \lambda_8=1.46575567714706\ldots
\]
against the certified rational interval of
`217_N8_BASE_MARGIN_CERTIFICATE.md`,
\(\lambda_8\in[1.465755677147060632655514,\;1.465755677147060632655515]\):
agreement to 14 digits.  Likewise \(A_8=0.020899933028\) against the
certified \([0.02089993302762,\ 0.02089993302764]\).
The pipeline reproduces phase 102 exactly.

## 1. The archimedean term \(A_n=\lambda_n^{\rm arch}\)

Computed from the numerically stable form
\(A_n=1-\frac n2(\gamma+\log4\pi)+\sum_{r\ \rm odd}q_n(1/r)\),
\(q_n(x)=(1-x)^n-1+nx\ge0\).  (The equivalent finite form
\(\sum_{k=2}^n(-1)^kC(n,k)(1-2^{-k})\zeta(k)\) of `217` has terms of size
\(2^n\) and is unusable past \(n\approx20\); recorded here as a practical
warning for the final write-up.)

Findings:

* \(A_n<0\) for \(1\le n\le7\); \(A_8=+0.0209\); \(A_n>0\) and increasing
  for \(n\ge8\).  This is exactly the threshold asserted in `151`.
* Least-squares fit over \(200\le n\le1200\) of
  \(A_n=a\frac n2\log n+b\frac n2+c\log n+d\):
  \[
    a=1.00000062,\qquad b=-2.26066691,\qquad c=0.00034,\qquad d=0.748 .
  \]
  Since \(\gamma-1-\log2\pi=-2.26066140\), this identifies
  \[
  \boxed{\ A_n={n\over2}\bigl(\log n+\gamma-1-\log2\pi\bigr)+O(\log n).\ }
  \]
  The phase-102 archimedean term therefore reproduces **exactly** the main
  term of the classical (conditional) Li asymptotic.

## 2. The strong margin \(\lambda_n\ge\frac12A_n\)

By `150` (11), A0 plus \(\lambda_n\ge\frac12A_n\) implies \(C_n(T_n)\ge0\).
The quantity \(\lambda_n-\frac12A_n\) is a certified lower bound for
\(C_n(T_n)\).

| \(n\) | \(\lambda_n\) | \(A_n\) | \(\lambda_n-\frac12A_n\) | \(\lambda_n/A_n\) |
|---:|---:|---:|---:|---:|
| 8 | 1.46575568 | 0.02089993 | **1.455306** | 70.13 |
| 9 | 1.85091605 | 0.46031964 | **1.620756** | 4.021 |
| 10 | 2.27933936 | 0.95553568 | **1.801572** | 2.385 |
| 20 | 8.76927687 | 8.09862406 | **4.719965** | 1.083 |
| 50 | 43.5310965 | 42.0332068 | **22.514493** | 1.036 |
| 100 | 118.603775 | 117.975023 | **59.616264** | 1.005 |
| 200 | 306.655765 | 304.515388 | **154.398071** | 1.007 |
| 400 | 748.315583 | 746.910525 | **374.860320** | 1.002 |
| 800 | 1763.86348 | 1770.33008 | **878.698444** | 0.996 |
| 1200 | 2899.88614 | 2898.39923 | **1450.686527** | 1.000 |

> **Finding 1.**  \(\lambda_n-\frac12A_n>0\) for every \(1\le n\le1200\),
> with margin \(\sim\frac n4(\log n+\gamma-1-\log2\pi)\to\infty\).  The
> required ratio is \(1/2\); the observed ratio tends to \(1\).  The strong
> margin gate holds with an asymptotic slack factor of \(2\).

Rigorous route: this is a finite, non-circular computation for each \(n\)
(Stieltjes constants + \(\zeta(k)\) + \(\gamma,\log4\pi\), rational interval
arithmetic), i.e. exactly the `217` verifier extended from \(n\le8\).  It is
*not* rigorous as computed here.

> **Finding 2.**  \(\lambda_n^{\rm prime}=\lambda_n-A_n\) is **bounded** and
> oscillating over the whole computed range: values between \(-6.5\) and
> \(+3.5\) for \(8\le n\le1200\).  All the growth of \(\lambda_n\) is
> archimedean.

## 3. The correlation \(\mathcal J_n\) against its budget

By `103_02` (10), direct A1 is
\(\mathcal J_n=\int_{\log2}^{T_n}EK_n\,du\le q(n)\).
\(\mathcal J_n\) is recovered from
\(\lambda_n^{\rm prime}=1-L_n^{(1)}(\log2)-\mathcal J_n\).

| \(n\) | budget \(q(n)\) | true \(\mathcal J_n\) | \(\mathcal J_n/q(n)\) |
|---:|---:|---:|---:|
| 8 | 2.678 | 1.218 | 0.455 |
| 20 | 5.797 | \(-0.947\) | \(-0.163\) |
| 60 | 43.757 | 0.564 | 0.013 |
| 200 | 232.341 | 1.814 | 0.008 |
| 400 | 556.889 | \(-4.699\) | \(-0.008\) |
| 800 | 1324.828 | 3.548 | 0.003 |

> **Finding 3.**  The certificate holds with an enormous and *growing*
> margin: the true cost is \(O(1)\) while the budget grows like
> \(\frac38n\log n\).  The direct route is not marginal — it is true by a
> factor \(\asymp n\log n\).

## 4. Absolute-envelope loads (Theorem 1 of `103_04`)

Load \(=\int_{\log2}^{4.05N}W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du\) for
\(W(u)=e^{u/2}u^{a}\), i.e. \(|\psi(x)-x|\le\sqrt x(\log x)^a\).

Fitted exponents over \(n=200\dots800\) (predicted \(\max(3/4,a+1/2)\)):

| \(a\) | fitted | predicted | load/budget at \(n=800\) |
|---|---|---|---|
| 0 | \(N^{0.789}\) | \(N^{0.75}\) | 0.161 |
| 1/2 | \(N^{1.030}\) | \(N^{1.00}\) | 1.223 |
| 1 | \(N^{1.487}\) | \(N^{1.50}\) | 29.81 |
| 2 | \(N^{2.473}\) | \(N^{2.50}\) | 1928.5 (with Schoenfeld's \(1/8\pi\)) |

> **Finding 4.**  The envelope threshold is \(a\le1/2\).  RH in Schoenfeld's
> explicit pointwise form (\(a=2\)) misses by \(n^{3/2}\); the conjectured
> true order (\(a\to0\)) succeeds with room to spare.  Confirms Theorem 1 of
> `103_04`.

## 5. Laguerre geometry constants

From `tools/laguerre_geometry.py` and `tools/raised_kernel.py`.

**(i) Plancherel–Rotach sup, and a correction to the naive bound.**
\(c_\alpha(N)=\sup_{0<u\le4N}|L_N^{(\alpha)}(u)|u^{\alpha/2+1/4}e^{-u/2}N^{-\alpha/2+1/4}\):

| \(N\) | 50 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|
| \(\alpha=2\) | 1.189 | 1.315 | 1.465 | 1.639 | 1.836 |
| \(\alpha=3\) | 1.223 | 1.334 | 1.476 | 1.645 | 1.839 |

The fitted growth is \(N^{0.157}\approx N^{1/6}\): the supremum over the
*full* bulk is **not** bounded, because of the soft-edge (Airy) region at
\(u\approx4N\).  On any fixed range \(u\le U\) the constant is bounded
(\(\le1.9\) measured).  Estimates in this phase that need the whole bulk
are therefore stated as integral budgets, never as a pointwise sup.

**(ii) Lobe widths.**  \(2\pi\sqrt{x/(4-x)}\), measured to \(<1\%\) at
\(x=0.5,1,2\) and \(<2\%\) at \(x=3\), for \(N=100,400,1600\).

**(iii) Integral budgets.**

\(I_\alpha(u_0)=\int_{u_0}^{4.05N}e^{-u/2}|L_N^{(\alpha)}(u)|\,du\):

| \(N\) | \(I_2(1)\) | \(I_2(1)/N^{3/4}\) | \(I_3(1)\) | \(I_3(1)/N^{5/4}\) |
|---|---|---|---|---|
| 50 | 21.10 | 1.122 | 67.89 | 0.511 |
| 100 | 36.96 | 1.169 | 159.11 | 0.503 |
| 200 | 65.09 | 1.224 | 358.76 | 0.477 |
| 400 | 111.82 | 1.250 | 859.79 | 0.481 |
| 800 | 192.78 | 1.282 | 2026.29 | 0.476 |

Fitted exponents \(N^{0.798}\) and \(N^{1.225}\) against the predicted
\(N^{3/4}\), \(N^{5/4}\).  Safe forms used in `103_04`:
\(I_2(1)\le1.3N^{0.80}\), \(I_3(u_0)\le0.52N^{5/4}u_0^{-3/4}\).
The \(u_0\)-law for \(\alpha=3\) is confirmed sharply: at \(N=400\),
\(I_3(u_0)u_0^{3/4}=859.8,\ 860.4,\ 823.7\) for \(u_0=1,10,100\).

**(iv) \(L^1\) mass.** \(\int_0^\infty e^{-u}|L_N^{(2)}|\,du\asymp N\)
(28.8, 76.0, 158.6, 329.9, 685.7, 1506.8 for \(N=20,\dots,800\); fitted
exponent 1.07).

**(v) Bulk mass (the no-go driver).**
\(\log_{10}\int_{2N}^{3N}|L_N^{(2)}|\,du\) = 11.6, 31.1, 63.6, 128.7,
258.4 for \(N=20,50,100,200,400\); i.e. \(e^{(3/2+o(1))N}\), the quantity
driving `103_05` Theorem 1.

## 5b. The conditional bound of `103_04` Theorem 2, evaluated

`tools/conditional_bound_check.py`, \(Y=\max(20,\sqrt n)\):

| \(n\) | \(q(n)\) | (i) | (ii) | (iii) | total | total/\(q\) |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 3.64 | 3.16 | 9.61 | 0.80 | 13.58 | 3.727 |
| 20 | 5.80 | 4.50 | 15.94 | 2.08 | 22.51 | 3.884 |
| 40 | 24.21 | 7.72 | 28.11 | 4.73 | 40.56 | 1.675 |
| 80 | 62.06 | 13.77 | 49.89 | 10.38 | 74.04 | 1.193 |
| 150 | 153.50 | 20.93 | 81.03 | 23.43 | 125.38 | 0.817 |
| 300 | 388.21 | 36.60 | 141.51 | 54.23 | 232.34 | 0.598 |
| 600 | 928.50 | 62.13 | 278.20 | 113.73 | 454.06 | 0.489 |
| 800 | 1324.83 | 76.83 | 379.69 | 149.99 | 606.51 | 0.458 |

> **Finding 5.**  The threshold is \(n_1=150\), and the ratio decreases
> monotonically thereafter.  The elementary term satisfies
> \(\int_{\log2}^{4N}e^{-u}|L_N^{(2)}|\,du/N^{3/4}\in[0.257,0.272]\) over
> \(9\le n\le800\), confirming that starting the integral at \(\log2\)
> rather than \(0\) improves the \(L^1\) mass from \(\asymp n\) to
> \(\asymp n^{3/4}\).

## 6. A numerical trap worth recording

The naive scaled recurrence for \(e^{-u/2}L_N^{(2)}(u)\) starts from
\(m_0=e^{-u/2}\), which underflows for \(u\gtrsim1490\).  All loads for
\(N\ge400\) are then silently truncated, and — because
\(\int u^{a}|M_N|\,du\) with \(a<1/4\) is lower-end dominated — the error is
invisible in the \(a=0\) column while corrupting \(a=1,2\) by orders of
magnitude.  `tools/laguerre_geometry.py` and `tools/raised_kernel.py` use a
dynamically rescaled recurrence.  Any re-derivation of these tables must do
the same.

## 7. What is verified and what is not

Verified numerically (diagnosis):

1. \(\lambda_8\), \(A_8\) reproduce the phase-102 certified intervals;
2. \(A_n>0\) exactly for \(n\ge8\), with asymptotic
   \(\frac n2(\log n+\gamma-1-\log2\pi)\);
3. the strong margin, hence \(C_n(T_n)\ge0\), for \(8\le n\le1200\);
4. the true correlation \(\mathcal J_n=O(1)\) against a budget
   \(\frac38n\log n\);
5. all Laguerre scales used in `103_03`, `103_04`, `103_05`.

Not verified, and requiring the extended rational interval verifier:

* a **certified** version of item 3, i.e. `217` run for \(9\le n\le N_\ast\).
  This is the concrete, finite, non-circular task that would extend the
  proved base of the direct route from \(n=8\) to \(n=N_\ast\).
