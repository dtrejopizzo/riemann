# D.156 — General Gamma kernel and reduced graph data

## Verdict

The complete Gamma action needed by the range graph of D.155 has an exact
one-dimensional singular-kernel formula valid beyond polynomials.  Put

\[
 K(x)=\sum_{j\ge0}e^{-(2j+1/2)x}
 ={e^{-x/2}\over1-e^{-2x}},\qquad x>0,                 \tag{0.1}
\]

and

\[
 H_1(x)=\sum_{j\ge0}{e^{-(2j+1/2)x}\over2j+1/2}.       \tag{0.2}
\]

For every (C^1) function (g) on ([-T,T]),

\[
\boxed{
 (G_\Gamma g)(t)=
 \int_{-T}^T K(|t-s|)\bigl(g(t)-g(s)\bigr)\,ds
 +\bigl(H_1(t+T)+H_1(T-t)\bigr)g(t).}                 \tag{0.3}
\]

The apparent diagonal singularity is removable in the integral because
(K(x)=\frac1{2x}+O(1)).  Formula (0.3) also extends by form closure to the
logarithmic endpoint layers produced by D.150.

For a rank-(k) graph (Y=CR), only the following directed data are
needed:

\[
 C^*C,\qquad Y^*C,\qquad Y^*AY,\qquad (QAY)^*(QAY),
 \qquad C^*QAY.                                        \tag{0.4}
\]

Hence the full squared residual requires one application of (0.3) to the
(k) auxiliary columns, not the four dense moment matrices
(S^*A^jS\), (j\le4).  At the selected endpoint (k=60).

No paper file is modified.

## 1. Finite oscillator identity

Let (b_j=2j+\frac12) and

\[
 (G_Jg)(t)=\sum_{j=0}^{J}
 \left({2\over b_j}g(t)
 -\int_{-T}^Te^{-b_j|t-s|}g(s)\,ds\right).             \tag{1.1}
\]

For a fixed (b>0), add and subtract (g(t)) inside the integral.  Since

\[
 \int_{-T}^Te^{-b|t-s|}\,ds
 ={2-e^{-b(t+T)}-e^{-b(T-t)}\over b},                  \tag{1.2}
\]

one obtains

\[
\begin{aligned}
 {2\over b}g(t)-\int_{-T}^Te^{-b|t-s|}g(s)\,ds
 ={}&\int_{-T}^Te^{-b|t-s|}(g(t)-g(s))\,ds\\
 &+{e^{-b(t+T)}+e^{-b(T-t)}\over b}g(t).               \tag{1.3}
\end{aligned}
\]

Summing (1.3) for (0\le j\le J) gives (0.3) with the two series
truncated.  This is a finite algebraic identity.

## 2. Passage to the complete Gamma action

For (x>0), the two series (0.1)--(0.2) converge absolutely.  Near the
diagonal,

\[
 K(x)={1\over2x}+O(1).                                 \tag{2.1}
\]

If (g\in C^1[-T,T]), then

\[
 |g(t)-g(s)|\le\|g'\|_\infty|t-s|,                    \tag{2.2}
\]

so the first integrand in (0.3) is locally bounded.  Away from the
diagonal, monotone convergence of the positive kernel majorant applies.
The boundary functions (H_1(t+T)) and (H_1(T-t)) have only logarithmic
singularities and lie in (L^2).  Therefore the finite identities converge
in (L^2) to (0.3), which is exactly the oscillator definition of
(G_\Gamma).

For an input with logarithmic endpoint growth, truncate at distance
(\varepsilon), apply the (C^1) identity, and pass to the limit in the
closed Gamma form.  The difference quotient times (K) is locally
integrable and the boundary product is a product of logarithms, hence in
(L^2) on a bounded interval.  This proves the extension used for
(g=ASc).

## 3. Completed action

At (T=\frac12\log5), the complete primitive action is

\[
 Ag=P_T\left[
 G_\Gamma g-m_0g-
 \sum_{n\in\{2,3,4\}}{\Lambda(n)\over\sqrt n}
 \bigl(\widetilde g(\,\cdot+\log n)+
       \widetilde g(\,\cdot-\log n)\bigr)
 \right],                                             \tag{3.1}
\]

with (m_0=\log\pi-\psi(1/4)).  Thus (0.3), three explicit truncated
translations, and the rank-two projector give (Ag) pointwise.  Nothing in
(3.1) separates the finite and Gamma terms before their cancellation.

## 4. Reduced range-graph matrices

Let (C=QAS), freeze (R\in\mathbb R^{n\times k}), and put (Y=CR).
Define

\[
 D_Y=Y^*AY,\qquad C_Y=Y^*C,\qquad Z=D_Y^{-1}C_Y.       \tag{4.1}
\]

The graph shorting is

\[
 \mathcal S_Y=B-C_Y^*Z.                               \tag{4.2}
\]

Apply (3.1) to the (k) columns of (Y), set (E=QAY), and note that

\[
 \mathcal R=C-EZ.                                     \tag{4.3}
\]

Its exact Gram matrix is

\[
\boxed{
 \mathcal R^*\mathcal R
 =C^*C-C^*EZ-Z^*E^*C+Z^*E^*EZ.}                       \tag{4.4}
\]

Equations (4.1)--(4.4) require a (168\times168) Gram (C^*C), two
rectangular (168\times60) Grams, and two (60\times60) Grams.  This is
strictly smaller than enclosing (H_3,H_4) on all 168 low directions.

## 5. Directed quadrature structure

The only singularities in the spatial integrals are explicit:

* (K(x)(g(t)-g(s))) has a removable diagonal limit;
* (H_1(x)=-\frac12\log x+O(1)) at an endpoint;
* D.150's inputs have at most logarithmic endpoint layers.

Splitting off these logarithms leaves analytic functions on each contact
cell.  Gauss--Jacobi or tanh--sinh interval quadrature can therefore enclose
all data in (0.4), while contact translations are integrated on their exact
subintervals.  This is the concrete interval computation required next.

`114_d_156_general_gamma_kernel_verify.py` checks the finite oscillator
identity and convergence of the closed kernel on a nontrivial polynomial.
