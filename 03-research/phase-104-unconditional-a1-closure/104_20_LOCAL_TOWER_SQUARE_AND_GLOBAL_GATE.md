# 104_20 — Local tower square and the surviving global gate

**Role.** Exploit the special formula of
\(b_u=J_u*J_u\) to combine a complete prime tower with the three channels
of `104_19` **before** estimating. The result is an exact local
factorization. The square obtained is algebraic, not a norm square, and the
local blocks of the real arithmetic sequence have both signs. Hence the
"sign per tower and sum" strategy dies. The global inequality for the
complete cocycle remains alive and is the next front.

This document proves neither A1 nor RH.

## 1. Translation operators and the coupled polar channel

Let

\[
 N=-\partial_x,
 \qquad
 \mathsf A_\varepsilon f(x)
 :=\int_0^\infty e^{-r}f(x+r/\varepsilon)\,dr,
 \qquad
 \mathsf U_\ell f(x):=\int_0^\ell f(x+t)\,dt.       \tag{1}
\]

Since

\[
 (\varepsilon-\partial_x)^{-1}={1\over\varepsilon}
 \mathsf A_\varepsilon,
\]

the polar factor of a single cocycle acts on the Laguerre variable as

\[
 \mathsf P_{\varepsilon,c}
 :=I-u(\varepsilon-\partial_x)^{-1}
 =I-c\mathsf A_\varepsilon,
 \qquad u=c\varepsilon.                             \tag{2}
\]

Integration by parts in (1) gives

\[
 \mathsf A_\varepsilon N
 =\varepsilon(I-\mathsf A_\varepsilon),
\]

and hence the equivalent form

\[
 \boxed{
 \mathsf P_{\varepsilon,c}
 =(1-c)I+{c\over\varepsilon}\mathsf A_\varepsilon N.} \tag{3}
\]

All the operators of (1)–(3) are functions of translations and
derivatives; they commute on the polynomial space where they will be used.

## 2. Exact second difference on a prime tower

Fix a prime \(p\) and set

\[
 \ell=\log p,
 \qquad \rho=p^{-1-\varepsilon},
 \qquad Q=p^u,
 \qquad (E_\ell f)(x)=f(x+\ell).                   \tag{4}
\]

With the convention \(a_{-1}=a_{-2}=0\), let
\(\nabla^2a_k=a_k-2a_{k-1}+a_{k-2}\). The formula of `104_19` refines to

\[
 \boxed{
 b_u(p^k)=\nabla^2\bigl((k+1)Q^k\bigr),
 \qquad k\ge0.}                                     \tag{5}
\]

Consequently, for every polynomial \(f\),

\[
 \boxed{
 \sum_{k\ge0}b_u(p^k)\rho^k f(x+k\ell)
 =\sum_{k\ge0}(k+1)(Q\rho)^k
   (I-\rho E_\ell)^2f(x+k\ell).}                  \tag{6}
\]

The identity is an exact discrete summation: the factor
\((I-\rho E_\ell)^2\) is the operational image of the second difference of
(5). Both series converge absolutely because

\[
 Q\rho=p^{-1-(1-c)\varepsilon}<1.
\]

Moreover,

\[
 \boxed{
 I-\rho E_\ell=(1-\rho)I+\rho\mathsf U_\ell N,}   \tag{7}
\]

because \(\mathsf U_\ell N=I-E_\ell\).

## 3. Coupled local square theorem

Operators (3) and (7) commute. Define

\[
 \boxed{
 \mathsf C_{p,\varepsilon,c}
 :=\bigl((1-\rho)I+\rho\mathsf U_\ell N\bigr)
   \bigl((1-c)I+{c\over\varepsilon}
                   \mathsf A_\varepsilon N\bigr).} \tag{8}
\]

**Theorem.** A complete tower \(p^k\), including the three polar channels of
`104_19`, satisfies

\[
 \boxed{
 \sum_{k\ge0}b_u(p^k)\rho^k
       \mathsf P_{\varepsilon,c}^{2}f(x+k\ell)
 =\sum_{k\ge0}(k+1)(Q\rho)^k
       \mathsf C_{p,\varepsilon,c}^{2}f(x+k\ell).} \tag{9}
\]

*Proof.* Substituting (6), commuting
\(\mathsf P_{\varepsilon,c}^2\) through the translations, and using (7)
produces (9). None of the three channels is separated. \(\square\)

The signed measure of `104_19` has disappeared inside a square. But
\(\mathsf C^2\) is not \(\mathsf C^*\mathsf C\): it defines no norm and has
no sign on oscillatory polynomials.

## 4. Expansion in raised Laguerre functions

Write

\[
 \mathsf C=a_0+a_1N+a_2N^2,                        \tag{10}
\]

where

\[
\begin{aligned}
 a_0&=(1-\rho)(1-c)I,\\
 a_1&=(1-\rho){c\over\varepsilon}\mathsf A_\varepsilon
      +\rho(1-c)\mathsf U_\ell,\\
 a_2&={\rho c\over\varepsilon}
          \mathsf U_\ell\mathsf A_\varepsilon.
\end{aligned}                                      \tag{11}
\]

The \(a_j\) are positive combinations of translations and commute with one
another. Since

\[
 N^jL_n=L_{n-j}^{(j)},                              \tag{12}
\]

with the convention of a zero value for \(j>n\), one obtains

\[
\boxed{
\begin{aligned}
 \mathsf C^2L_n={}&a_0^2L_n
 +2a_0a_1L_{n-1}^{(1)}
 +(a_1^2+2a_0a_2)L_{n-2}^{(2)}\\
 &+2a_1a_2L_{n-3}^{(3)}
 +a_2^2L_{n-4}^{(4)}.
\end{aligned}}                                      \tag{13}
\]

All the operator weights in (13) are positive. Nevertheless, each raised
Laguerre function retains oscillations. The local square reorganizes the
cancellation, but does not turn it into positivity.

## 5. Exact witness on the real sequence \(b_u\)

The loss of sign is not merely formal. Consider a tower \(p^k\) over a
background \(m\) coprime to \(p\). After integrating the Beta measure of the
Gamma channel, the degree-\(n=1\) block is, up to the positive prefactor
\(b_u(m)m^{-1-\varepsilon}\),

\[
 \boxed{
 K_0M_p\left[
 (1-c)^2(1-\log m-\bar\eta-\ell\mu_p)
 +{2c(1-c)\over\varepsilon}\right],}               \tag{14}
\]

where

\[
\begin{aligned}
 K_0&=K_u(1+\varepsilon)>0,\\
 M_p&=\left({1-\rho\over1-Q\rho}\right)^2>0,\\
 \mu_p&={2\rho(Q-1)\over(1-\rho)(1-Q\rho)}>0,\\
 \bar\eta&={1\over2}\left[
 \psi\!\left({3+\varepsilon\over2}\right)
 -\psi\!\left({3+\varepsilon-u\over2}\right)
 \right]>0.
\end{aligned}                                      \tag{15}
\]

Here \(M_p=\sum_{k\ge0}b_u(p^k)\rho^k\),
\(\mu_p\) is the exact average of \(k\) under those normalized weights, and
\(\bar\eta\) is the average of \(-\frac12\log v\) under the normalized Beta
measure. Hence (14) changes sign exactly upon crossing

\[
 \boxed{
 \log m=1-\bar\eta-\ell\mu_p
       +{2c\over(1-c)\varepsilon}.}                 \tag{16}
\]

With \(p\) and \(c\in(0,1)\) fixed, there exists
\(\varepsilon_0(p,c)>0\) such that, for
\(0<\varepsilon<\varepsilon_0(p,c)\), the block \(m=1\) is on the positive
side and every sufficiently large coprime \(m\) is on the negative side. In
that regime both signs occur with the **real** arithmetic weights \(b_u\).

More generally, the leading coefficient in \(\log m\) of the degree-\(n\)
block is

\[
 \boxed{
 {K_0M_p(1-c)^2\over n!}(-1)^n.}                   \tag{17}
\]

So, for every even \(n\), including every even \(n\ge150\), there are
infinitely many coprime backgrounds whose canonical block is positive.
Hence the global sign cannot be closed by imposing a non-positive sign on
**each canonical block (14)**. This does not rule out a renormalization or
a global regrouping across backgrounds, including the global \(-1/u\) term
of (20) in `104_19`.

## 6. What does not die: the global gate

The witness above does **not** refute the sign of the complete sum. The
global identity of `104_19` remains

\[
 g_{n,\varepsilon,c}
 =[z^n]{\mathcal S_{c\varepsilon}(s_\varepsilon(z))-1
              \over c\varepsilon(1-z)},
 \qquad
 g_{n,\varepsilon,c}\longrightarrow-\Delta D_n.   \tag{18}
\]

Hence the statement, with its complete quantifiers,

\[
 \boxed{
 \exists c\in(0,1)\ \ \forall n\ge149:\quad
 \limsup_{\varepsilon\downarrow0}g_{n,\varepsilon,c}\le0} \tag{19}
\]

is, pointwise, equivalent to \(\Delta D_n\ge0\), because the limit in
(18) exists. The version with \(g_{n,\varepsilon,c}\le0\) for
\(0<\varepsilon<\varepsilon_0(n)\) suffices; a uniform
\(\varepsilon_0\) in \(n\) is not needed. Together with the finite
certificate, either of these forms would prove the strong margin and A1.

**Diagnostic, not a theorem.** A Cauchy/Borwein extraction in `float64`
found \(g_{n,\varepsilon,c}<0\) up to \(n=1200\) for

\[
 (\varepsilon,c)\in
 \{(10^{-3},1/2),(10^{-2},1/2),(10^{-1},1/2),(1,1/2),
   (10^{-1},9/10)\}.
\]

Reproduced with

```bash
python3 tools/global_cocycle_probe.py --nmax 1200 --samples 32768 \
  --r1 0.99 --r2 0.985
```

This is not a certified interval and enters no proof. Its only use is
directional: no counterexample to the global sum appeared, even though
(14)–(17) rigorously prove that its local summands have both signs.

## 7. Remaining exact global reformulation

Factorization (9) expresses the same global gate in a more structured
local coordinate, but **it does not demonstrate a reduction of difficulty
relative to \(\Delta D_n\ge0\)**. The unambiguous question is:

\[
 \boxed{
 \text{What global property of the multiplicative convolution of all
 towers turns the sum of }\mathsf C_p^2L_n
 \text{ into (19)?}}                                  \tag{20}
\]

A proof cannot use tower-by-tower sign, sign per background, or a norm of
\(\mathsf C\). It must preserve the multiplicative interactions between
distinct primes. That is now the narrowest active point of the mechanism.

`tools/local_tower_square_check.py` verifies with `Fraction` arithmetic
independent algebraic ingredients: (3), (5), (7),
\(\mathsf B^2\mathsf P^2=(\mathsf B\mathsf P)^2\) on test polynomials, and
the recomposition of the degree-one linear formula on both sides of its
threshold; it also checks the leading coefficient up to degree eight. It
does not verify the complete infinite series, (17) for every degree, (19),
A1, or RH.
</content>
