# D.167 — Tate-cancelled Dirichlet mean capacity

## Verdict

The exact prime-power boundary synthesis of D.164 has pure-Gamma dual
energy

\[
 \boxed{
 \|\Gamma_{T,N}^{-1/2}\mathcal B_N^{\rm prim}\|^2
 \le \left({1\over2}+o(1)\right)\log N.}             \tag{0.1}
\]

Here (Gamma_{T,N}) is the Gamma form on the old core with its support
uncertainty gap, and `prim` means that the continuous main terms are
removed by the two exact Tate moments of D.137.  The estimate is uniform
for the two boundary channels.  The only exact zero-frequency collision
between the left and right Dirichlet polynomials is (nm=N), and its
unweighted mass is the scalar

\[
 H_N={1\over\sqrt N}(\Lambda*\Lambda)(N)              \tag{0.2}
\]

already found in D.164.  In particular (H_N=o((\log N)^2)) and it does
not change the leading coefficient in (0.1).

Together with the pure-Gamma Dirichlet-to-Neumann estimate of D.166,
(0.1) leaves the formal leading boundary margin

\[
 (1-o(1))\log N-left({1\over2}+o(1)\right)\log N
 =\left({1\over2}-o(1)\right)\log N.                 \tag{0.3}
\]

This closes the **pure-Gamma resolvent comparison**, including every
prime power and both boundary channels.  It does not yet justify replacing
the Gamma inverse by the inverse of the previously shorted arithmetic
core.  That transfer is isolated in Section 5 and is the remaining
noncircular induction lemma.

## 1. Dirichlet polynomial and its exact norm

Put

\[
 W_N(\tau)=\sum_{n\le N}{\Lambda(n)\over\sqrt n}
                         e^{-i\tau\log n},\qquad
 V_N=\sum_{n\le N}{\Lambda(n)^2\over n}.             \tag{1.1}
\]

If (e) is supported on an interval of length
(ell\le\log(1+1/N)<1/N), translations by the numbers (log n),
(n\le N), have disjoint interiors.  Plancherel therefore gives the
exact identity

\[
 {1\over2\pi}\int_{\mathbb R}
 |\widehat e(\tau)|^2|W_N(\tau)|^2d\tau
 =V_N\|e\|_2^2.                                      \tag{1.2}
\]

For the two-sided synthesis the same computation gives the Gram matrix

\[
 \begin{pmatrix}V_N&H_N\\H_N&V_N\end{pmatrix},       \tag{1.3}
\]

because a positive and a reflected logarithmic frequency agree exactly
when (nm=N).  Thus the two-channel norm squared is (V_N+H_N), not
twice (V_N).

The prime number theorem and partial summation give

\[
 V_N={1\over2}(\log N)^2+O(\log N),\qquad H_N=O(\log N),             \tag{1.4}
\]

the latter deliberately coarse bound being enough below.  Formula (1.1)
contains all (p^k), since (Lambda(n)) vanishes off prime powers.

## 2. The two Tate main terms

The continuous comparison to (1.1) is

\[
 M_N(\tau)=\int_1^N x^{-1/2-i\tau}dx
 ={N^{1/2-i\tau}-1\over1/2-i\tau}.                  \tag{2.1}
\]

In logarithmic coordinates, multiplication by (M_N) is convolution
with

\[
 u\longmapsto e^{u/2}\mathbf1_{[0,\log N]}(u).        \tag{2.2}
\]

Pairing (2.2) with an old-core function produces, up to the two endpoint
pieces of length at most (ell), exactly one of

\[
 M_+(F)=\int e^{t/2}F(t)dt,qquad
 M_-(F)=\int e^{-t/2}F(t)dt.                          \tag{2.3}
\]

Both vanish on the primitive core by D.137.  The endpoint remainders in
(2.2) are Volterra operators between sets of length (ell); their norms
are (O(1)) after the central (N^{-1/2}) normalization.  They therefore
contribute (o(\log N)) to (0.1).

This is the point at which the jets/moments comparison is used
quantitatively: the coherent low-frequency part of (W_N) is not bounded
by absolute values; it is identified with the two A--B--C degree
characters and removed exactly.

## 3. Low frequencies after Tate cancellation

Let

\[
 E_N(\tau)=W_N(\tau)-M_N(\tau).                       \tag{3.1}
\]

The prime number theorem is equivalent, by partial summation, to

\[
 N^{-1/2}E_N(\tau)\longrightarrow0                  \tag{3.2}
\]

uniformly on every fixed compact (	au)-interval.  A diagonal choice
therefore gives numbers (R_0(N)\to\infty) and
(arepsilon_N\to0) such that

\[
 |E_N(\tau)|\le\varepsilon_N\sqrt N
 \quad(|\tau|\le R_0(N)).                            \tag{3.3}
\]

They may be chosen so slowly that

\[
 \log R_0=o(\log N).                                 \tag{3.4}
\]

Let (a_Tasymp(\log N)^{-2}) be the support gap of D.166 and put
(s_N=a_T\varepsilon_N^2).  For a boundary function of unit norm,
(|\widehat e|^2\le\ell\le1/N).  Since
(h_{5/4}(\tau)\asymp\tau^2) at zero, (3.3) gives

\[
 {1\over2\pi}\int_{|\tau|\le R_0}
 { |\widehat e(\tau)|^2|E_N(\tau)|^2
  \over h_{5/4}(\tau)+s_N},d\tau=o(\log N).         \tag{3.5}
\]

Indeed the singular part is
(O(\varepsilon_N^2s_N^{-1/2})=O(\varepsilon_N\log N)),
and (R_0) can be slowed further so that the remaining compact integral
is (o(\log N)).

The shift does not alter the leading dual norm.  From
(\mathcal H_{5/4}(f)\ge a_T\|f\|^2),

\[
 {1\over2\pi}\int(h_{5/4}+s_N)|\widehat f|^2
 \le(1+\varepsilon_N^2)\mathcal H_{5/4}(f).          \tag{3.6}
\]

Thus weighted Fourier Cauchy--Schwarz costs only (1+o(1)).

## 4. Mean-value estimate and the coefficient one half

The Montgomery--Vaughan Hilbert inequality for the separated frequencies
(log n) gives, uniformly for every real interval (I),

\[
 \int_I|W_N(\tau)|^2d\tau
 \le |I|V_N+C\sum_{n\le N}\Lambda(n)^2.              \tag{4.1}
\]

Here (C) is absolute; the nearest-neighbour gap
(log(n+1)-\log n\asymp n^{-1}) is precisely what changes the usual
error into (sum n|\Lambda(n)/\sqrt n|^2=sum\Lambda(n)^2).
The prime number theorem gives

\[
 \sum_{n\le N}\Lambda(n)^2=O(N\log N).              \tag{4.2}
\]

Choose (eta_N\downarrow0) with
(R_0<N^{1-\eta_N}) and
((\log R_0)^{-1}+\eta_N=o(1)), and also
(\eta_N\log N\to\infty).  On the middle band
(R_0\le|\tau|\le N^{1-\eta_N}), (4.1),
(|\widehat e|^2\le1/N), and monotonicity of (h_{5/4}) give

\[
 {1\over2\pi}\int_{m middle}
 { |\widehat e|^2|W_N|^2\over h_{5/4}+s_N}
 =o(\log N).                                         \tag{4.3}
\]

To see the coefficient rather than only the order, use (1.2) on the top
band.  Since

\[
 h_{5/4}(N^{1-\eta_N})
 =(1-\eta_N)\log N+O(1),                             \tag{4.4}
\]

we obtain

\[
\begin{aligned}
 {1\over2\pi}\int_{|\tau|\ge N^{1-\eta_N}}
 { |\widehat e|^2|W_N|^2\over h_{5/4}+s_N}
 &\le {V_N\over(1-\eta_N)\log N+O(1)}\|e\|^2\\
 &=\left({1\over2}+o(1)\right)\log N\,\|e\|^2.     \tag{4.5}
\end{aligned}
\]

The continuous term (M_N) is (O(\sqrt N/|\tau|)) on the middle and
top bands, so its weighted contribution there is (o(\log N)).  Using
(|E_N|^2\le(1+o(1))|W_N|^2+o(1)|M_N|^2), equations
(3.5), (4.3), and (4.5) prove (0.1) for one channel.

For two channels, apply the same separated-frequency inequality to the
union of the positive and reflected frequencies.  Its only zero gap is
the exact relation (nm=N), which is split off before applying Hilbert's
inequality and gives (0.2).  The remaining frequencies are separated and
the diagonal norm is the top eigenvalue (V_N+H_N) of (1.3).  Equations
(1.4) and (4.5) therefore retain the coefficient (1/2), rather than
introducing a spurious factor two.

## 5. The exact remaining transfer lemma

Let (A_N^{\rm core}) be the full primitive form on the old core after
Gamma, every preceding (p^k), the resolvent term and the Tate shorting
have been assembled.  The annular Schur complement needs

\[
 \mathcal B_N^*(A_N^{\rm core})^\dagger\mathcal B_N,  \tag{5.1}
\]

whereas (0.1) bounds the same expression with the pure-Gamma inverse.
Since old contacts lower the core form, operator monotonicity goes in the
wrong direction:

\[
 A_N^{\rm core}\le\Gamma_N
 \quad\Longrightarrow\quad
 (A_N^{\rm core})^\dagger\ge\Gamma_N^\dagger         \tag{5.2}
\]

on a common positive range.  Therefore (0.1) cannot simply be substituted
into (5.1).

The noncircular induction statement still required is the restricted
defect-resolvent estimate

\[
 \boxed{
 \mathcal B_N^*(A_N^{\rm core})^\dagger\mathcal B_N
 -\mathcal B_N^*\Gamma_N^\dagger\mathcal B_N
 =o(\log N)\,I.}                                     \tag{5.3}
\]

It is enough to prove (5.3) only on the two-channel range of
(mathcal B_N), not as an operator comparison on the entire old core.
The exact resolvent identity rewrites its left side as

\[
 \mathcal B_N^*\Gamma_N^\dagger
 (\Gamma_N-A_N^{\rm core})
 (A_N^{\rm core})^\dagger\mathcal B_N,               \tag{5.4}
\]

with the appropriate range projections.  Formula (5.4), together with
the Tate cancellation of Section 2, is the next directed target.  Proving
it closes the asymptotic integer-cell induction; the finitely many cells
below its effective threshold then remain for interval certification.

The ancillary `114_d_167_dirichlet_mean_verify.py` checks the exact
prime-power sums, the coefficient (1/2), the (nm=N) collision and the
finite-dimensional resolvent identity corresponding to (5.4).
