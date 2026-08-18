# Uniform Laguerre lobe geometry on \([T_8,T_n]\)

Work order step 4 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.

## Objects

\[
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u)=\omega_n'(u),
  \qquad
  \omega_n(u)=G_N(T_n)-G_N(u),\quad N=n-1 .
\]

Two partitions occur in the guide:

* the **value partition**, by the zeros of \(\omega_n\) (used for the
  coefficient sign in (3));
* the **derivative partition**, by the zeros of \(L_{n-1}^{(2)}\) (used for
  the correlation (9)).

Only the derivative partition is needed below, because
`103_01`/`103_02` removed the value partition entirely: the certificate was
reduced to the single correlation
\(\int_{\log2}^{T_n}E\,K_n\,du\le q(n)\).

## 1. Location of the zeros

\(L_{n-1}^{(2)}\) has exactly \(N=n-1\) simple positive zeros
\(0<\xi_{n,1}<\dots<\xi_{n,N}\), all contained in
\[
  \Bigl(0,\;4N+2\bigl(2N\bigr)^{1/3}+O(N^{-1/3})\Bigr),
\]
the classical Laguerre bound.  Consequently:

> **Fact 1 (corrected truncated geometry).**  For every admissible A0
> cutoff of the canonical VK policy,
> \(T_n\asymp n^{5/3}(\log n)^2\) (`208`, `221`).  The zeros at the hard
> edge lie below every fixed positive lower endpoint for large \(n\).  Put
\[
 r_n(T_8)=\#\{j:\xi_{n,j}\le T_8\}.
\]
> Then the derivative zeros which occur in the integration interval are
\[
 T_8<\xi_{n,r_n(T_8)+1}<\cdots<\xi_{n,N}<4n<T_n,
\]
> for all sufficiently large \(n\).  The hard-edge count is
\(r_n(T_8)=\frac2\pi\sqrt{NT_8}+O_{T_8}(1)\); a proof and the resulting
fixed-window collapse are recorded in
`103_12_HARD_EDGE_CORRECTION_AND_FIXED_WINDOW_COLLAPSE.md`.

Thus the *relevant truncated* oscillatory region is contained in
\((T_8,4n)\), while \((4n,T_n)\) carries no sign change.  This is the
structural reason why cutoff optimisation cannot help
(`119_A1_TRUNCATION_OPTIMIZATION_AUDIT.md`): moving \(T_n\) moves only the
sign-free tail.  The \(r_n(T_8)\) omitted hard-edge lobes are already part
of the fixed finite-data term in the exact reserve; they must not be
silently included in the moving lobe partition.

## 2. Zero density and lobe widths

With \(u=xN\), \(0<x<4\), the zero-counting density of \(L_N^{(2)}\) is the
Marchenko–Pastur density
\[
\boxed{\ \rho_N(u)={1\over2\pi}\sqrt{4N-u\over u}\,,
       \qquad
       \hbox{lobe width }\ w(u)={1\over\rho_N(u)}=2\pi\sqrt{u\over4N-u}\ }
\tag{1}
\]
so that at \(u=xN\),
\[
  w=2\pi\sqrt{x\over4-x}\qquad\hbox{(independent of }N).
\tag{2}
\]

Numerically verified (`103_06`, and `tools/laguerre_geometry.py`):

| \(x=u/N\) | predicted \(w\) | measured \(N=100\) | \(N=400\) | \(N=1600\) |
|---|---|---|---|---|
| 0.5 | 2.375 | 2.409 | 2.380 | 2.377 |
| 1.0 | 3.628 | 3.666 | 3.644 | — |
| 2.0 | 6.283 | 6.321 | 6.318 | — |
| 3.0 | 10.883 | 11.390 | 11.065 | — |

> **Fact 2 (the decisive geometric fact).**  In the bulk the lobe width is
> \(\Theta(1)\) — it does **not** shrink with \(n\).  It is bounded below by
> \(2\pi\sqrt{x/(4-x)}\ge2.37\) for \(x\ge1/2\).

Fact 2 is what makes the competitor construction of
`103_05_ADMISSIBLE_COMPETITOR_NO_GO.md` possible: a nondecreasing
prime-counting function has enough room *inside a single lobe* to traverse
the whole admissible envelope.  Had the lobes shrunk like \(n^{-1/2}\),
monotonicity alone would have constrained the adversary and the oriented
route would have had a chance.  It does not.

## 3. Amplitude envelope

The Plancherel–Rotach regime gives, for \(0<u<4N\),
\[
\boxed{\ |L_N^{(\alpha)}(u)|\le c_\alpha\,N^{\alpha/2-1/4}u^{-\alpha/2-1/4}e^{u/2},\ }
\tag{3}
\]
hence
\[
  |K_n(u)|\le c_2\,N^{3/4}u^{-5/4}e^{-u/2},
  \qquad
  |\omega_n'(u)|=|K_n(u)| .
\tag{4}
\]

Note the two competing factors in (4): amplitude \(N^{3/4}\) but
Gaussian-type decay \(e^{-u/2}\).

**Range of validity of (3).**  Measured (`103_06` §5,
`tools/raised_kernel.py`), the left/right ratio in (3) taken as a supremum
over the *whole* interval \(0<u\le4N\) is
\[
  \sup_u|L_N^{(\alpha)}(u)|u^{\alpha/2+1/4}e^{-u/2}N^{-\alpha/2+1/4}
  = 1.19,\,1.32,\,1.47,\,1.64,\,1.84
  \quad(\alpha=2,\ N=50,100,200,400,800),
\]
i.e. it grows like \(N^{0.157}\approx N^{1/6}\).  This is the soft-edge
(Airy) correction at \(u\approx4N\); (3) with a constant \(c_\alpha\) is
correct on any fixed range \(u\le U\), and correct up to \(N^{1/6}\) on the
full bulk.  Every estimate in this phase that needs the full range is
therefore stated as a **measured integral budget**, not as a pointwise sup.

## 4. Signed and absolute lobe budgets

Define, for a lobe \(J_{n,j}\) between consecutive zeros,
\[
  W_{n,j}=\int_{J_{n,j}}|K_n(u)|\,du,
  \qquad
  \sigma_{n,j}=\mathrm{sgn}\,K_n|_{J_{n,j}} .
\]

Three budgets control every estimate in the phase:

\[
\boxed{
\begin{aligned}
 \hbox{(a) kernel }L^1\hbox{ mass}\quad
   &\int_0^\infty e^{-u}|L_{n-1}^{(2)}(u)|\,du\ \asymp\ n,\\
 \hbox{(b) }I_2(u_0)=\!\!\int_{u_0}^{4N}\!\! e^{-u/2}|L_{n-1}^{(2)}|\,du
   &\ \le\ 1.3\,n^{0.80},\\
 \hbox{(b$'$) }I_3(u_0)=\!\!\int_{u_0}^{4N}\!\! e^{-u/2}|L_{n-1}^{(3)}|\,du
   &\ \le\ 0.52\,n^{5/4}u_0^{-3/4},\\
 \hbox{(c) unweighted bulk mass}\quad
   &\int_{aN}^{bN}|L_{n-1}^{(2)}(u)|\,du\ =\ e^{(b/2+o(1))N}.
\end{aligned}}
\tag{5}
\]

Measured values (`tools/laguerre_geometry.py`, `tools/raised_kernel.py`):

* (a) \(\int_0^\infty e^{-u}|L_N^{(2)}|\,du\) = 28.8, 76.0, 158.6, 329.9,
  685.7, 1506.8 for \(N=20,50,100,200,400,800\) — growth exponent
  \(1.07\), consistent with \(\asymp N\).
* (b) \(I_2(1)\) = 21.1, 37.0, 65.1, 111.8, 192.8 for
  \(N=50,100,200,400,800\); ratio to \(N^{3/4}\) is 1.12, 1.17, 1.22, 1.25,
  1.28 (slow \(N^{1/6}\)-type drift from the soft edge), and the fitted
  exponent is \(N^{0.798}\).  Hence the safe form \(I_2(1)\le1.3N^{0.80}\)
  on the tested range.
* (b\('\)) \(I_3(1)\) = 67.9, 159.1, 358.8, 859.8, 2026.3 for the same
  \(N\); fitted exponent \(N^{1.225}\) against the predicted \(N^{5/4}\),
  ratio \(I_3(1)/N^{5/4}\in[0.476,0.511]\).  The \(u_0\)-dependence is
  confirmed sharply: at \(N=400\), \(I_3(u_0)u_0^{3/4}\) = 859.8, 860.4,
  823.7 for \(u_0=1,10,100\).
* (c) \(\log_{10}\int_{2N}^{3N}|L_N^{(2)}|\,du\) = 11.6, 31.1, 63.6, 128.7,
  258.4 for \(N=20,50,100,200,400\); the fit is
  \(e^{1.49N}\), i.e. \(e^{3N/2}\), matching (5c) with \(b=3\).

Budget (b) is the one that matters for a proof; budget (c) is the one that
matters for a no-go.  Their ratio is \(e^{3N/2}/N^{3/4}\).

## 5. Pairing and the failure of independent lobe estimates

Adjacent lobes carry nearly equal absolute mass:
\[
  {W_{n,j+1}\over W_{n,j}}=1+O\!\left({1\over\sqrt{u(4N-u)}}\right)
\]
in the bulk, so the alternating series \(\sum_j\sigma_{n,j}W_{n,j}\) is
conditionally convergent with cancellation of relative size \(O(N^{-1/2})\)
per pair, whereas \(\sum_jW_{n,j}\asymp n\).  Compare with the *true* value
of the correlation, which is \(O(1)\) (`103_06`).  Hence:

> **Fact 3.**  Independent lobe estimates lose a factor of at least
> \(\asymp n\) even in the best case where each lobe is evaluated exactly in
> absolute value.  Against a VK envelope they lose \(e^{3n/2}\).  This is
> no-go 3 of the guide, now quantified.

## 6. What the geometry does and does not give

Delivered (step 4 items 1–5 of the work order):

1. zeros located: exactly the \(N-r_n(T_8)\) relevant zeros lie inside
   \((T_8,4n)\subset(T_8,T_n)\); the other \(r_n(T_8)\) hard-edge zeros
   lie at or below the fixed lower endpoint;
2. signs determined: strict alternation; on the last lobe
   \((\xi_{n,N},\infty)\), \(K_n\) has the constant sign
   \((-1)^{n-1}\), since
   \(L_{n-1}^{(2)}(u)\sim(-1)^{n-1}u^{n-1}/(n-1)!\).  Thus this ray is
   sign-definite (not always positive);
3. lobe widths uniformly \(\Theta(1)\) in the bulk, formula (2);
4. extrema and signed areas: envelope (4), budgets (5);
5. the initial truncated piece \((T_8,\xi_{n,r_n(T_8)+1})\) and the
   terminal ray \((\xi_{n,N},T_n)\) are explicitly separated; the terminal ray is
   sign-definite and is the only place where an absolute envelope is safe
   (`327`).

Not delivered, and provably not deliverable from geometry alone: any
orientation statement about where the prime powers sit relative to these
lobes.  That is the content of `103_05`.

## Status

Closed.  Step 4 of the work order is complete.
