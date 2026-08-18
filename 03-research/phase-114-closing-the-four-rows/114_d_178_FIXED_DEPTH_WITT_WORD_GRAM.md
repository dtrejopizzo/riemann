# D.178 — Fixed-depth Witt-word Gram

## Verdict

Before inserting the noncommuting reference inverses, the (k)-fold Witt
word synthesis has an exact integer-cell Gram.  Put

\[
 \Lambda_k=\underbrace{\Lambda*\cdots*\Lambda}_{k\ {m times}},
 \qquad a_k(m)={\Lambda_k(m)\over\sqrt m}.            \tag{0.1}
\]

Then the depth-(k) left/right synthesis has Gram

\[
 \boxed{
 \begin{pmatrix}V_{N,k}&H_{N,k}\\H_{N,k}&V_{N,k}\end{pmatrix}
 \otimes I,}                                         \tag{0.2}
\]

where

\[
 V_{N,k}=\sum_{m\le N}{\Lambda_k(m)^2\over m},
 \qquad
 H_{N,k}={\Lambda_{2k}(N)\over\sqrt N}.              \tag{0.3}
\]

For every fixed (k), the squarefree (k)-prime words give the leading
asymptotic

\[
 \boxed{
 V_{N,k}\sim {k!\over(2k)!}(\log N)^{2k}.}           \tag{0.4}

In particular

\[
 V_{N,1}\sim\frac12(\log N)^2,qquad
 V_{N,2}\sim\frac1{12}(\log N)^4.                   \tag{0.5}

Relative to the (k)-th power of the depth-one main scale, the leading
constant is

\[
 \theta_k={2^kk!\over(2k)!}={1\over(2k-1)!!},        \tag{0.6}
\]

which is summable and in fact superfactorially decreasing.

This identifies a real combinatorial mechanism for summable returns:
ordered Frobenius words collapse to unordered products, and the logarithmic
simplex supplies ((2k)!) in the denominator.  However, the exact return
moment of D.176 is

\[
 q^*\left(R^{-1/2}LR^{-1/2}\right)^kq,               \tag{0.7}
\]

not the raw word Gram (0.2).  Each (R^{-1}) contains the full Gamma,
antisymmetric contacts and Tate shorting.  Therefore (0.4) is not yet a
bound for (0.7).  The remaining constructive theorem is a
**reference-resolvent word inequality** showing that insertion of the
exact (R^{-1}) preserves the simplex gain (0.6), up to a summable constant.

## 1. Exact word collapse

For an ordered word (\boldsymbol n=(n_1,\ldots,n_k)) of prime-power
labels, Witt composition gives

\[
 \Gamma_{n_1}\circ\cdots\circ\Gamma_{n_k}
 =\Gamma_{n_1\cdots n_k},                            \tag{1.1}
\]

and the central metric weights multiply:

\[
 \prod_{j=1}^k{\Lambda(n_j)\over\sqrt{n_j}}
 ={\prod_j\Lambda(n_j)\over\sqrt{n_1\cdots n_k}}.   \tag{1.2}
\]

Grouping all ordered words with product (m) gives precisely

\[
 {1\over\sqrt m}
 \sum_{n_1\cdots n_k=m}\prod_j\Lambda(n_j)
 ={\Lambda_k(m)\over\sqrt m}.                        \tag{1.3}
\]

This includes every prime-power depth and automatically vanishes when a
factor cannot be written as a product of (k) prime powers.

## 2. Integer-cell Gram at depth (k)

Let (U_m^L,U_m^R) be the exact placements of D.164.  Their support
relations depend only on the product label (m), not on its factorization.
Define

\[
 \mathcal B_{N,k}(f_L,f_R)
 =\sum_{m\le N}a_k(m)(U_m^Lf_L+U_m^Rf_R).             \tag{2.1}
\]

Then

\[
 (U_m^L)^*U_n^L=\delta_{mn}I,qquad
 (U_m^L)^*U_n^R=\mathbf1_{mn=N}I.                    \tag{2.2}
\]

The diagonal entry of (\mathcal B_{N,k}^*\mathcal B_{N,k}) is the first
formula in (0.3).  Its off-diagonal entry is

\[
 \sum_{mn=N}{\Lambda_k(m)\Lambda_k(n)\over\sqrt{mn}}
 ={(\Lambda_k*\Lambda_k)(N)\over\sqrt N}
 ={\Lambda_{2k}(N)\over\sqrt N},                    \tag{2.3}

which proves (0.2)--(0.3).

## 3. Leading fixed-depth asymptotic

The largest logarithmic degree in (V_{N,k}) comes from squarefree products
of exactly (k) distinct primes.  For
(m=p_1\cdots p_k),

\[
 \Lambda_k(m)=k!\prod_{j=1}^k\log p_j.              \tag{3.1}

After dividing unordered products by (k!), their contribution is

\[
 k!\sum_{p_1\cdots p_k\le N}^{\rm distinct}
       \prod_{j=1}^k{(\log p_j)^2\over p_j}.          \tag{3.2}

The prime number theorem and multivariable partial summation replace each
prime variable (u_j=\log p_j) by the measure (u_j\,du_j).  Hence the
leading integral is

\[
 k!\int_{\substack{u_j\ge0\\u_1+\cdots+u_k\le L}}
       u_1\cdots u_k\,du_1\cdots du_k,
 \qquad L=\log N.                                    \tag{3.3}

The Dirichlet simplex integral equals

\[
 \int_{\sum u_j\le L}\prod_j u_j\,du
 =L^{2k}{\Gamma(2)^k\over\Gamma(2k+1)}
 ={L^{2k}\over(2k)!}.                               \tag{3.4}

Words involving a repeated prime or a proper prime power have fewer than
(k) independent prime variables and contribute lower logarithmic degree.
Equations (3.2)--(3.4) prove (0.4) for fixed (k).

For (k=2), this can be seen directly.  If (p\ne q),

\[
 (\Lambda*\Lambda)(pq)=2\log p\log q,                \tag{3.5}

and the unordered two-prime simplex gives

\[
 2\int_{u+v\le L}uv\,du\,dv={L^4\over12}.          \tag{3.6}

## 4. The exact missing resolvent inequality

Let (\widetilde q) denote the unnormalized centered old--born cross and
write (C=R^{-1}L) on the primitive source.  A sufficient estimate with
the correct word constants would be

\[
 \boxed{
 \widetilde q^*C^kR^{-1}\widetilde q
 \le A_N\,{2^k k!\over(2k)!}+\varepsilon_{N,k},
 \qquad
 \sum_{k\ge0}\varepsilon_{N,k}<\infty.}             \tag{4.1}

After boundary normalization, summing (4.1) would close the centered
term (q^*D^\dagger q) of D.175.

D.164 proves the required orthogonality before the inverses.  D.166 proves
the leading Gamma cost of one inverse while allowing arbitrary old-core
extensions.  What is not yet proved is that repeated exact minimizers do
not realign the word channels and destroy (0.6).  This is precisely the
phase-defect alignment problem, now with an explicit target sequence
((2k-1)!!^{-1}) rather than an unspecified decay.

The accompanying verifier computes (V_{N,1}) and (V_{N,2}) by exact
Dirichlet convolution, checks (0.2)--(0.3) on finite cells, and confirms
the constants (1/2) and (1/12) numerically along growing cutoffs.
