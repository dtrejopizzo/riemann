# 104_87 — Finite Nyman section, `max` inversion, and Möbius tail

**Result.** The divisor inversion identity does give an exact cancellation
for the Nyman residual built with the Möbius coefficients: the residual
vanishes on the whole macroscopic interval \((1/N,1]\). Its full norm
remains concentrated on \((0,1/N]\), where it admits an exact positive
series. In the first block of that series there appears, without loss, a
centered increment of the Mertens function.

More precisely, if

\[
 g_N=\sum_{k\le N}{\mu(k)\over k},\qquad
 b_{k,N}=\mu(k)-Ng_N\mathbf 1_{\{k=N\}},                 \tag{1}
\]

then \(\sum_{k\le N}b_{k,N}/k=0\) and the residual

\[
 \mathcal R_N(x)=1+\sum_{k\le N}b_{k,N}
       \left\{{1\over kx}\right\}                       \tag{2}
\]

satisfies

\[
 \boxed{\mathcal R_N(x)=0\quad(1/N<x\le1).}             \tag{3}
\]

Setting

\[
 R_N(m)=1-\sum_{k\le N}b_{k,N}\left\lfloor{m\over k}\right\rfloor,
                                                                    \tag{4}
\]

we have the norm identity

\[
 \boxed{
 d_N^2:=\int_0^1|\mathcal R_N(x)|^2\,dx
 =\sum_{m=N}^{\infty}{R_N(m)^2\over m(m+1)}.}           \tag{5}
\]

In particular, if \(M(y)=\sum_{k\le y}\mu(k)\), then

\[
 \boxed{R_N(m)=M(m)-M(N)+Ng_N\quad(N\le m<2N)}          \tag{6}
\]

and therefore

\[
 \boxed{
 d_N^2\ge {1\over4N^2}\sum_{m=N}^{2N-1}
 \{M(m)-M(N)+Ng_N\}^2.}                                \tag{7}
\]

Thus, convergence of this explicit approximant would require the
necessary condition

\[
 \sum_{m=N}^{2N-1}\{M(m)-M(N)+Ng_N\}^2=o(N^2),         \tag{8}
\]

that is, mean-square size \(o(\sqrt N)\) in the first block.
PNT/Vinogradov--Korobov does not reach that scale. The tridiagonal
inversion of the kernel \(1/\max(m,n)\) does not improve (5): it is exactly
the operation that converts the coefficients of the Dirichlet residual
into the partial sums \(R_N(m)\).

The document does not claim that (8) is sufficient, nor that it fails for
the ordinary Möbius coefficients. It proves that divisor telescoping, by
itself, does not give the upper bound that would close Nyman. For
optimized coefficients, proving that the infimum of the norms tends to
zero remains the Nyman--Báez-Duarte criterion and hence RH. Neither
Deep-\(\Lambda\), A1, nor RH is proved.

---

## 1. Floor form for a Dirichlet polynomial

Let

\[
 A(s)=\sum_{k\le N}{a_k\over k^s},\qquad
 \sum_{k\le N}{a_k\over k}=0.                           \tag{9}
\]

The Hardy--Nyman residual is

\[
 f_A(s)={1-\zeta(s)A(s)\over s}.                        \tag{10}
\]

The Mellin transform of

\[
 \mathcal R_A(x)=1+\sum_{k\le N}a_k
       \left\{{1\over kx}\right\},\qquad 0<x<1,       \tag{11}
\]

is (10). Indeed, for \(\Re s>1\),

\[
 \int_0^1\left\{{1\over kx}\right\}x^{s-1}\,dx
 ={1\over k(s-1)}-{\zeta(s)\over sk^s},                \tag{12}
\]

and the first term cancels when summed by (9). The identity extends
to the Hardy space by continuity.

If \(m\le1/x<m+1\), (9) turns (11) into

\[
 \mathcal R_A(x)=R_A(m),\qquad
 R_A(m):=1-\sum_{k\le N}a_k\left\lfloor{m\over k}\right\rfloor.
                                                                    \tag{13}
\]

Consequently,

\[
 \boxed{
 \|f_A\|_{H^2}^2=\|\mathcal R_A\|_{L^2(0,1)}^2
 =\sum_{m\ge1}{|R_A(m)|^2\over m(m+1)}.}               \tag{14}
\]

The last equality uses only that
\((1/(m+1),1/m]\) has length \(1/[m(m+1)]\).

## 2. The Möbius choice and cancellation of the prefix

The choice (1) satisfies constraint (9). For \(m<N\), the corrector
at \(k=N\) does not contribute and Möbius inversion gives

\[
 \sum_{k\le N}b_{k,N}\left\lfloor{m\over k}\right\rfloor
 =\sum_{k\le m}\mu(k)\left\lfloor{m\over k}\right\rfloor
 =1.                                                     \tag{15}
\]

This proves (3). For \(m\ge N\), (4) is written

\[
 R_N(m)=1-\sum_{k\le N}\mu(k)\left\lfloor{m\over k}\right\rfloor
 +Ng_N\left\lfloor{m\over N}\right\rfloor.           \tag{16}
\]

If \(N\le m<2N\), the last floor equals one. Subtracting from the
complete identity

\[
 \sum_{k\le m}\mu(k)\left\lfloor{m\over k}\right\rfloor=1,        \tag{17}
\]

the terms with \(N<k\le m\) have floor one. Hence

\[
 R_N(m)=\sum_{N<k\le m}\mu(k)+Ng_N
       =M(m)-M(N)+Ng_N,                                 \tag{18}
\]

which proves (6). Since \(m(m+1)<4N^2\) in that block, (5) implies (7).

## 3. The `max` kernel and its exact inverse

Let \(r=(r_1,\ldots,r_M)^T\), \(S_j=\sum_{m\le j}r_m\), and

\[
 K_M(i,j)={1\over\max(i,j)}.                            \tag{19}
\]

Partitioning \((0,1]\) into reciprocal intervals gives

\[
 r^TK_Mr
 =\sum_{j=1}^{M-1}{S_j^2\over j(j+1)}+{S_M^2\over M}. \tag{20}
\]

In particular, \(K_M^{-1}\) is tridiagonal:

\[
 (K_M^{-1})_{j,j}=
 \begin{cases}2j^2,&j<M,\\ M^2,&j=M,\end{cases}
 \qquad
 (K_M^{-1})_{j,j+1}=(K_M^{-1})_{j+1,j}=-j(j+1),         \tag{21}
\]

and the remaining entries are zero. The inversion creates no reserve: (20)
shows that it only changes between the increments \(r_j\) and their
primitives \(S_j\).

For the residual of (10), the Dirichlet coefficients are

\[
 r_A(m)=\mathbf1_{\{m=1\}}-
        \sum_{\substack{k\le N\\k\mid m}}a_k,         \tag{22}
\]

and its partial sum is precisely (13). Thus, the limit of (20) is (14).
No boundary term is omitted by passing to the tridiagonal inverse.

## 4. Scale of the missing input

From PNT with a Vinogradov--Korobov-type zero-free region one obtains,
for some effective constant \(c>0\),

\[
 M(x),\;xg_x
 \ll x\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}.     \tag{23}
\]

Applying (23) term by term in (7) only produces the scale

\[
 N\exp\{-2c(\log N)^{3/5}(\log\log N)^{-1/5}\},        \tag{24}
\]

which does not tend to zero. This does not prove that the left-hand side
of (7) is large: it proves that the pointwise PNT input does not certify
(8).

For arbitrary coefficients subject to (9), a zero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), imposes, by Hardy evaluation,

\[
 \|f_A\|_{H^2}^2\ge {2\beta-1\over|\rho|^2}.           \tag{25}
\]

Hence a construction of coefficients with \(\liminf\|f_A\|=0\)
would exclude all right-hand zeros and prove RH. Equations
(3)--(8) are an exact localization of that problem for the truncated
Möbius case; they do not constitute such a construction.
