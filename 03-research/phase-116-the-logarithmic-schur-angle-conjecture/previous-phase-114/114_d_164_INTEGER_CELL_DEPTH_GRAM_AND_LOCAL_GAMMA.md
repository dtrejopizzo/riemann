# D.164 — Integer-cell depth Gram and local Gamma capacity

## Verdict

Inside the single support cell

\[
 {1\over2}\log N\leq T\leq {1\over2}\log(N+1),       \tag{0.1}
\]

the boundary strips have a new exact arithmetic orthogonality which is
invisible in dyadic batching.  Put

\[
 \ell=2T-\log N\leq\log(1+1/N).                       \tag{0.2}
\]

All translates of a strip of length \(\ell\) by the distinct logarithms
\(\log n\), \(n\leq N\), are disjoint.  A left translate and a reflected
right translate can meet only when their integer labels multiply to
\(N\), and in that case the two intervals coincide exactly.

For the prime-power weights

\[
 w_n={\Lambda(n)\over\sqrt n},                         \tag{0.3}
\]

the complete boundary synthesis Gram is therefore the two-by-two scalar
matrix

\[
 \boxed{
 \mathsf G_N=
 \begin{pmatrix}V_N&H_N\\H_N&V_N\end{pmatrix}
 \otimes I_{L^2(0,\ell)},}                             \tag{0.4}
\]

where

\[
\begin{aligned}
 V_N&=\sum_{n\leq N}{\Lambda(n)^2\over n}
 =\sum_{p\leq N}{(\log p)^2\over p}
   {1-p^{-\lfloor\log N/\log p\rfloor}\over1-p^{-1}},\\
 H_N&={1\over\sqrt N}(\Lambda*\Lambda)(N).
\end{aligned}                                         \tag{0.5}
\]

Consequently the exact norm of the old-contact boundary synthesis is

\[
 \boxed{\|\mathcal B_N\|^2=V_N+H_N.}                  \tag{0.6}
\]

This is the desired square-sum gain on an individual threshold cell.  It
does not contradict D.122: a dyadic strip has fixed width, while the
integer-cell strip has width \(O(N^{-1})\), strictly below the logarithmic
separation of consecutive labels.  The exceptional off-diagonal term
\(H_N\) is exactly Dirichlet convolution, hence records Witt multiplication
and Frobenius depth rather than an uncontrolled overlap.

There is also an unconditional local Gamma lower bound.  If \(f\) is
supported on a set of measure at most \(2\ell\), then, for every
\(0<c<\pi/2\),

\[
 \boxed{
 \mathcal H_{5/4}(f)\geq
 \left(1-{2c\over\pi}\right)
 h_{5/4}(c/\ell)\|f\|_2^2.}                            \tag{0.7}
\]

Thus the boundary Gamma strength has leading size \(\log N\), whereas
the exact arithmetic synthesis has size
\(\sqrt{V_N+H_N}\sim2^{-1/2}\log N\).  This creates a real asymptotic
margin which the previous \(\ell^1\) estimates erased.

The result is a noncircular input to the annular capacity (D.163, (5.4)).
It does **not yet** prove its norm is at most one: the remaining operation
is to control the shorting through the transported old core.  In
particular no monotone Loewner update may be asserted; the new signed
contact is indefinite even on the two-Tate primitive smooth core.

## 1. Exact integer-cell separation

Let

\[
 A=[-T,-T+\ell],\qquad A^\vee=[T-\ell,T].              \tag{1.1}
\]

The centers of \(A+\log n\) and \(A+\log m\) differ by
\(|\log(n/m)|\).  For distinct \(m,n\leq N\),

\[
 |\log(n/m)|\geq\log{N\over N-1}
 >\log{N+1\over N}\geq\ell.                          \tag{1.2}
\]

Hence their interiors are disjoint.  The reflected family
\(A^\vee-\log m\) has the same property.

The centers of \(A+\log n\) and \(A^\vee-\log m\) differ by

\[
 |2T-\ell-\log n-\log m|
 =|\log N-\log(nm)|.                                  \tag{1.3}
\]

If \(nm<N\), this is at least \(\log(N/(N-1))>\ell\).  If
\(nm>N\), it is at least \(\log((N+1)/N)\geq\ell\).  If \(nm=N\),
the centers agree and the equal lengths make the intervals identical.
This proves the separation and collision assertions without a
prime-spacing estimate.

## 2. Exact synthesis Gram

Identify both boundary strips isometrically with \(L^2(0,\ell)\).  Let
\(U_n^L\) place a function on \(A+\log n\), and let \(U_n^R\) place it
on \(A^\vee-\log n\).  Define

\[
 \mathcal B_N(f_L,f_R)
 =\sum_{\substack{n\leq N\\\Lambda(n)>0}}
 w_n(U_n^Lf_L+U_n^Rf_R).                               \tag{2.1}
\]

Section 1 gives

\[
\begin{aligned}
 (U_n^L)^*U_m^L&=\delta_{nm}I,
 &(U_n^R)^*U_m^R&=\delta_{nm}I,\\
 (U_n^L)^*U_m^R&=\mathbf1_{nm=N}I.                    \tag{2.2}
\end{aligned}
\]

Therefore

\[
 \mathcal B_N^*\mathcal B_N=\mathsf G_N              \tag{2.3}
\]

with (0.4)--(0.5).  Its eigenchannels are the symmetric and antisymmetric
boundary combinations, with eigenvalues \(V_N+H_N\) and \(V_N-H_N\).
Positivity of the Gram itself proves \(0\leq H_N\leq V_N\), and (0.6)
follows.

The diagonal quantity has the finite-depth Euler expression in (0.5),
because

\[
 \sum_{k=1}^{K}{(\log p)^2\over p^k}
 ={(\log p)^2\over p}{1-p^{-K}\over1-p^{-1}}.         \tag{2.4}
\]

The collision term is

\[
 \sum_{nm=N}w_nw_m
 ={1\over\sqrt N}\sum_{nm=N}\Lambda(n)\Lambda(m).
                                                                    \tag{2.5}
\]

For a prime power \(N=p^k\), this specializes to

\[
 H_{p^k}={(k-1)(\log p)^2\over p^{k/2}}.              \tag{2.6}
\]

Thus the only same-prime collision counts the \(k-1\) internal cuts of
the Frobenius-depth word.

## 3. Local weighted-prolate Gamma lower bound

Let \(E\subset\mathbb R\) have measure \(|E|\leq2\ell\), and extend
\(f\in L^2(E)\) by zero.  Let \(K_{E,R}\) be the time--band
concentration operator for frequencies \([-R,R]\).  It is a positive
contraction with

\[
 \mathrm{Tr}\,K_{E,R}={|E|R\over\pi}
 \leq{2\ell R\over\pi}.                               \tag{3.1}
\]

Hence

\[
 {1\over2\pi}\int_{-R}^{R}|\widehat f(\tau)|^2d\tau
 \leq{2\ell R\over\pi}\|f\|_2^2.                   \tag{3.2}
\]

The function

\[
 h_{5/4}(\tau)=\mathrm{Re}\,\psi(5/4+i\tau/2)-\psi(5/4)
                                                                    \tag{3.3}
\]

is even, nonnegative and increasing on \([0,\infty)\).  Taking
\(R=c/\ell\) and discarding the low band in its positive multiplier form
gives (0.7).

For fixed \(c\),

\[
 h_{5/4}(c/\ell)=\log(1/\ell)+O_c(1)=\log N+O_c(1).   \tag{3.4}
\]

On the arithmetic side the prime number theorem and partial summation give

\[
 V_N={1\over2}(\log N)^2+O(\log N),\qquad
 H_N=o((\log N)^2).                                   \tag{3.5}
\]

Choosing \(c>0\) small enough that
\(1-2c/\pi>1/\sqrt2\), equations (0.7) and (3.5) yield

\[
 \left(1-{2c\over\pi}\right)h_{5/4}(c/\ell)
 -\sqrt{V_N+H_N}\longrightarrow+\infty.              \tag{3.6}
\]

This is an unconditional asymptotic margin.  It uses the actual integer
cell and the actual prime-power depth Gram, not a thickness fraction.

## 4. Why this is not a monotone first variation

At a prime-power birth \(N=p^k\), the exact update is

\[
 \Delta_N(F)=w_N\|J_{N,-}F\|^2-w_N\|J_{N,+}F\|^2
 =-2w_N\mathrm{Re}\,C_F(\log N).                 \tag{4.1}
\]

Two equal endpoint bumps make (4.1) negative, while reversing one bump
makes it positive.  The two Tate moments can be restored by two fixed
interior correctors of size \(O(\sqrt\ell)\), without changing the leading
endpoint value.  Consequently \(\Delta_N\) has both signs on the
primitive smooth core for every open cell.

Therefore neither

\[
 Q_N\geq Q_{N-1}\quad\text{nor}\quad Q_N\leq Q_{N-1}  \tag{4.2}
\]

holds in Loewner order.  This is the finite-cell version of the D.133
Hadamard no-go.  The useful monotone object is instead the positive Gram
\(\mathcal B_N^*\mathcal B_N\), whose norm is exactly (0.6), inside the
nonperturbative annular Schur complement.

## 5. Remaining core-shorting estimate

Let \(R_{N,T}\) and \(J_{N,+}\) be as in D.163.  The desired threshold
capacity is

\[
 \mathcal K_{N,T}^{\rm ann}
 =w_NJ_{N,+}R_{N,T}^\dagger J_{N,+}^*.                \tag{5.1}
\]

Equations (0.6)--(0.7) give exact directed bounds for the two ingredients
created at the boundary: arithmetic synthesis into the core and Gamma
coercivity on the born annulus.  What remains is a uniform estimate that
the Moore--Penrose shorting through the transported old core does not
consume the asymptotic margin (3.6).  This is strictly sharper than the
old generic target: the only exceptional overlaps have already collapsed
to the explicit convolution scalar \(H_N\).

