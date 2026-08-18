# D.177 — Audit of the collision-only reduction

## Verdict

The centered old--born cross (q) of D.175 does **not** reduce to the
single collision (nm=N).  The scalar

\[
 H_N={1\over\sqrt N}(\Lambda*\Lambda)(N)             \tag{0.1}
\]

is only the off-diagonal entry of the **two-sided synthesis Gram**.  It
appears after the left and right boundary synthesis operators have been
multiplied.  It is not a linear summand of either synthesis operator or of
the cross (q).

After exact Tate centering the complete discrepancy

\[
 E_N(\tau)=
 \sum_{n\le N}{\Lambda(n)\over\sqrt n}e^{-i\tau\log n}
 -{N^{1/2-i\tau}-1\over1/2-i\tau}                   \tag{0.2}
\]

remains.  It is nonzero for every (N\ge2), including prime (N), whereas
(H_N=0) for prime (N).  Hence no collision-only factorization can equal
the exact centered cross.

The valid gain from D.164 is instead:

\[
 \mathcal B_N^*\mathcal B_N=
 \begin{pmatrix}V_N&H_N\\H_N&V_N\end{pmatrix}\otimes I, \tag{0.3}
\]

with exact diagonal square-sum (V_N) and only one exceptional
left--right overlap (H_N).  This is essential for an unweighted or
pure-Gamma large-sieve estimate, but it does not make
(q^*D^\dagger q) finite-dimensional.

## 1. What the integer-cell orthogonality actually proves

With the notation of D.164,

\[
 \mathcal B_N(f_L,f_R)
 =\sum_{n\le N}w_n(U_n^Lf_L+U_n^Rf_R),
 \qquad w_n={\Lambda(n)\over\sqrt n}.                \tag{1.1}
\]

The exact support relations are

\[
 (U_n^L)^*U_m^L=\delta_{nm}I,qquad
 (U_n^R)^*U_m^R=\delta_{nm}I,qquad
 (U_n^L)^*U_m^R=\mathbf1_{nm=N}I.                   \tag{1.2}
\]

Thus (H_N) occurs only in the product
((\mathcal B_N^L)^*\mathcal B_N^R).  The one-sided products are

\[
 (\mathcal B_N^L)^*\mathcal B_N^L
 =(\mathcal B_N^R)^*\mathcal B_N^R=V_NI,             \tag{1.3}
\]

and remain nonzero whether or not any collision exists.

In particular, when (N) is prime there are no integers (n,m\ge2) with
(nm=N), so

\[
 H_N=0,                                               \tag{1.4}
\]

but both one-sided synthesis operators in (1.1) contain every active
prime power (p^j\le N) and have squared norm (V_N>0).

## 2. Exact nonvanishing of the Tate-centered discrepancy

Write (L=\log N).  Formula (0.2) is the Fourier transform of the finite
signed measure on ([0,L])

\[
 d\nu_N(u)=
 \sum_{n\le N}{\Lambda(n)\over\sqrt n}\delta_{\log n}(u)
 -e^{u/2}\,du.                                       \tag{2.1}
\]

The measure (d\nu_N) is not zero: its first part is atomic and its second
part is nonzero and absolutely continuous.  Uniqueness of the Fourier
transform of finite measures therefore gives

\[
 \boxed{E_N\not\equiv0.}                             \tag{2.2}

This argument is exact and does not use a prime-number estimate.

For a more elementary prime-cell witness, let (N=p) be prime.  Then
(H_p=0), whereas

\[
 E_p(0)=\sum_{n\le p}{\Lambda(n)\over\sqrt n}
        -2(\sqrt p-1).                               \tag{2.3}

Even if (2.3) accidentally vanished at an isolated (p), (2.2) would
still rule out (E_p\equiv0).  At the first prime cells, (2.3) is already
nonzero directly.

## 3. Why the two Tate moments do not change this conclusion

The two Tate conditions replace the continuous Chebyshev main term by
the bounded reflected exponential and shift the Gamma index from
(1/4) to (5/4).  Equivalently, they replace (W_N) by the centered
measure (d\nu_N) in the born synthesis, together with the exact endpoint
Volterra pieces.

They do not identify the atomic measure in (2.1) with Lebesgue measure.
Nor can a codimension-two projection annihilate the full one-sided
boundary synthesis: on a boundary space (L^2(0,\ell)), (1.1) has
infinite rank whenever one (w_n\ne0), and subtracting two Tate directions
changes its rank by at most two.

Thus the post-centering decomposition is

\[
 q=q_{E_N}+q_{\rm end},                              \tag{3.1}
\]

where (q_{E_N}) is the genuine centered atomic-continuous discrepancy
and (q_{\rm end}) contains the finite-width Volterra endpoints.  There is
no further exact reduction

\[
 q_{E_N}=q_{H_N}.                                    \tag{3.2}

Indeed (H_N) is quadratic in the synthesis coefficients, while (q) and
(E_N) are linear in them.

## 4. Consequence for the return estimate

D.175--D.176 reduce the non-telescoping capacity to

\[
 q^*D^\dagger q
 =\sum_{k\ge0}q^*T^kq.                               \tag{4.1}

Equation (0.3) can be used at every occurrence of the boundary synthesis
to control diagonal words by (V_N) and the sole left--right collision by
(H_N).  But the complete centered channel (q_{E_N}) must remain in
(4.1).  A legitimate next estimate has the form

\[
 q_{E_N}^*T^kq_{E_N}
 \le a_k(N),qquad \sum_{k\ge0}a_k(N)<\infty,         \tag{4.2}

with the endpoint pieces treated separately.  Replacing (q_{E_N}) by a
rank-two collision channel would discard the diagonal (V_N) contribution
and would already fail on every prime threshold.

The accompanying verifier checks the exact collision ledger, exhibits
prime cells with (H_N=0) but (E_N(0)\ne0), and verifies that removing two
Tate target directions cannot collapse a discretized one-sided synthesis
to rank two.
