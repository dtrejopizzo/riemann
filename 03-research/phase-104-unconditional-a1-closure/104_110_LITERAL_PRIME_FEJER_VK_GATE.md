# 104_110 — Literal prime Fejér kernel and the exterior-ray VK gate

**Question.** Can the uniform bound surviving in `104_108`,

\[
 \sup_{\phi\in\mathbb R}
 \left|\mathcal B^{\triangle}_{2L,L,1}(\phi)\right|
 \le \exp(o(L)),                                           \tag{1}
\]

be proved by directly inserting the effective Vinogradov–Korobov PNT
into the prime–Laguerre form, without separating the pole, the primes,
and the prime powers?

**Result.** The literal prime form does admit a closed finite kernel and
contour. If

\[
 \alpha_{L,k}={L-|k|\over L^2}\quad (|k|<L),
 \qquad q=e^{-i\phi},
\]

one defines

\[
 \begin{aligned}
 P_{L,\phi}(u)
   &:=\sum_{|k|<L}\alpha_{L,k}q^k
           L_{2L+k-1}^{(1)}(u),\\
 Q_{L,\phi}(u)
   &:=\sum_{|k|<L}\alpha_{L,k}q^k
           L_{2L+k-1}^{(2)}(u),
 \end{aligned}                                             \tag{2}
\]

then, with \(E(x)=\psi(x)-x\),

\[
 \boxed{
 \mathcal B^{\triangle}_{2L,L,1}(\phi)
 =P_{L,\phi}(0)+
   \int_0^\infty E(e^u)e^{-u}Q_{L,\phi}(u)\,du.}           \tag{3}
\]

The identity jointly preserves the continuous polar mass and all the
atoms \(p^j\), with their real weight \(\Lambda(p^j)=\log p\).

However, (1) **does not** follow from the VK envelope. At the exact
frequency \(\phi=\pi\), every summand of \(Q_{L,\pi}\) has the same sign
on the exterior ray. If

\[
 \eta(u)=c u^{3/5}(\log u)^{-1/5},\qquad
 U_L=L^{5/3}(\log L)^{1/3},                               \tag{4}
\]

then the majorant resulting from

\[
 |E(e^u)|\le C e^u e^{-\eta(u)}                            \tag{5}
\]

satisfies

\[
 \boxed{
 \int_0^\infty e^{-\eta(u)}|Q_{L,\pi}(u)|\,du
 \ge
 \exp\!\left\{
 {4\over3}L\log L+{2\over3}L\log\log L-O(L)
 \right\}.}                                               \tag{6}
\]

Thus the triangular smoothing and the modulation that reduce the phase
cost at \(a\ge4\) to \(O(1)\) do not reduce the absolute VK cost at
\(a=1\): frequency \(\pi\) aligns the entire exterior ray. The deficit
relative to (1) is \(\exp((4/3+o(1))L\log L)\), not a lost constant.

This is a no-go for **PNT/VK + modulus after the prime–pole coupling**.
It is not a lower bound for the real arithmetic expression (3). The
specific signed cancellation of the literal weights \(\Lambda(m)\)
remains exactly the missing theorem. This document does not prove (1),
A1, or RH.

---

## 1. Prime–pole form before removing the regulator

Keep the definition of `104_41`. For \(a>1\), absolute convergence allows
summing first over the degree:

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{2L,L,a}(\phi)
 =a\int_{1^-}^{\infty}y^{-a}
 P_{L,\phi}(a\log y)\,d\{\psi(y)-y\}.                    \tag{7}
 \end{aligned}
\]

The Stieltjes notation in (7) is not cosmetic:

\[
 d\psi(y)=\sum_{m\ge2}\Lambda(m)\,\delta_m,
 \qquad d y=\hbox{continuous polar channel}.                  \tag{8}
\]

Hence (7) contains, before any estimate, the pole, all the primes, and
all the prime powers. Equivalently,

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{2L,L,a}(\phi)
 =a\sum_{m\ge2}{\Lambda(m)\over m^a}
       P_{L,\phi}(a\log m)
 -a\int_1^\infty y^{-a}P_{L,\phi}(a\log y)\,dy.          \tag{9}
 \end{aligned}
\]

No separate meaning will be assigned to the two terms of (9) at
\(a=1\). It is their combination that continues.

## 2. Exact generating function and finite contour

Write

\[
 K_L(z)=\sum_{|k|<L}\alpha_{L,k}z^k
 ={(1-z^L)(1-z^{-L})\over
       L^2(1-z)(1-z^{-1})}.                               \tag{10}
\]

The ordinary generating functions

\[
 \sum_{d\ge0}L_d^{(1)}(u)z^d
 ={e^{-uz/(1-z)}\over(1-z)^2},
 \qquad
 \sum_{d\ge0}L_d^{(2)}(u)z^d
 ={e^{-uz/(1-z)}\over(1-z)^3}                             \tag{11}
\]

give, for a small circle around zero,

\[
 \boxed{
 P_{L,\phi}(u)
 ={1\over2\pi i}\oint
 {e^{-uz/(1-z)}\over(1-z)^2z^{2L}}
 K_L(q/z)\,dz,}                                          \tag{12}
\]

and

\[
 \boxed{
 Q_{L,\phi}(u)
 ={1\over2\pi i}\oint
 {e^{-uz/(1-z)}\over(1-z)^3z^{2L}}
 K_L(q/z)\,dz.}                                          \tag{13}
\]

Here \(K_L(q/z)\) is a finite Laurent polynomial; no two-sided series or
new region of convergence has been introduced.

There is also a direct closed contour for the observable. Let

\[
 M_\Lambda(s)={1\over s-1}+{\zeta'(s)\over\zeta(s)}.
\]

Equation (8) of `104_41`, differentiated in the generating variable,
gives

\[
 \sum_{n\ge1}B_nz^{n-1}
 =-{1\over(1-z)^2}
 M_\Lambda\!\left({1\over1-z}\right).                   \tag{14}
\]

Consequently,

\[
 \boxed{
 \mathcal B^{\triangle}_{2L,L,1}(\phi)
 =-{1\over2\pi i}\oint
 {M_\Lambda((1-z)^{-1})\over
   (1-z)^2z^{2L}}K_L(q/z)\,dz.}                           \tag{15}
\]

The function \(M_\Lambda=F'/F\), with \(F(s)=(s-1)\zeta(s)\), is regular
at \(s=1\). Hence (15) is a legitimate local contour, not a deformation
across zeros.

## 3. Joint removal of the regulator

For each fixed \(L\), VK makes the boundary term at infinity vanish when
integrating (7) by parts and lowering \(a\) down to \(1\). At the lower
boundary \(E(1)=-1\). Since

\[
 {d\over du}L_d^{(1)}(u)=-L_{d-1}^{(2)}(u),
 \qquad
 L_d^{(2)}(u)=L_d^{(1)}(u)+L_{d-1}^{(2)}(u),              \tag{16}
\]

one has exactly

\[
 P_{L,\phi}(u)-P'_{L,\phi}(u)=Q_{L,\phi}(u).             \tag{17}
\]

Hence,

\[
 \begin{aligned}
 \int_{1^-}^{\infty}y^{-1}P_{L,\phi}(\log y)\,dE(y)
 &=P_{L,\phi}(0)
   +\int_1^\infty {E(y)\over y^2}
       Q_{L,\phi}(\log y)\,dy,
 \end{aligned}                                           \tag{18}
\]

which, via \(y=e^u\), proves (3). For a single degree, (18) is the known
identity

\[
 B_n=n+\int_0^\infty E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.   \tag{19}
\]

The boundary term \(n\) of (19) has not been discarded; averaging it
produces exactly \(P_{L,\phi}(0)\).

## 4. Frequency \(\pi\) aligns the entire exterior ray

We need an elementary bound for the Laguerre zeros. The zeros of
\(L_d^{(\alpha)}\) are the eigenvalues of the \(d\times d\) truncation of
the Jacobi matrix with diagonal \(2j+\alpha+1\) and off-diagonal
\(\sqrt{(j+1)(j+\alpha+1)}\). Gershgorin and

\[
 \sqrt{j(j+\alpha)}\le j+{\alpha\over2}
\]

give

\[
 0<x_{d,j}<4d+2\alpha+2.                                 \tag{20}
\]

In (2), the degrees \(d=2L+k-1\) satisfy \(d\le3L-2\). For
\(u\ge24L\), (20) with \(\alpha=2\) gives \(x_{d,j}<u/2\). Since the
leading coefficient of \(L_d^{(2)}\) is \((-1)^d/d!\),

\[
 (-1)^dL_d^{(2)}(u)
 ={1\over d!}\prod_{j=1}^d(u-x_{d,j})
 \ge{(u/2)^d\over d!}.                                   \tag{21}
\]

Now take \(\phi=\pi\), so that \(q^k=(-1)^k\). Since

\[
 (-1)^k(-1)^{2L+k-1}=-1,                                 \tag{22}
\]

**every** summand of \(Q_{L,\pi}(u)\) is negative for \(u\ge24L\). There
is no cancellation between degrees. Keeping only \(k=0\), whose weight is
\(1/L\),

\[
 \boxed{
 |Q_{L,\pi}(u)|
 \ge {1\over L}{(u/2)^{2L-1}\over(2L-1)!}
 \qquad(u\ge24L).}                                      \tag{23}
\]

This exact alignment is the prime–Laguerre counterpart of the residue
resonance of `104_108`, but it uses no zeros of \(\zeta\).

## 5. Scale gap for VK

For \(U_L\) from (4), one has \(U_L\ge24L\) for \(L\) large, and

\[
 \eta(U_L+1)=O(L).                                       \tag{24}
\]

The function \(\eta\) is increasing in that range. From (23), over
\([U_L,U_L+1]\),

\[
 \begin{aligned}
 \log\!\int_0^\infty e^{-\eta(u)}|Q_{L,\pi}(u)|\,du
 &\ge
 (2L-1)\log(U_L/2)-\log(2L-1)!\\
 &\quad-\log L-\eta(U_L+1).                              \tag{25}
 \end{aligned}
\]

The elementary bound

\[
 \log d!\le d\log d-d+O(\log d)
\]

turns (25) into (6). In particular, not even a bound
\(e^{cL}\) can be obtained by taking moduli after (3), let alone the
barrier \(e^{\sqrt L}\) of `104_108`.

The same computation has an operator-theoretic reading: the norm of the
functional \(E\mapsto\int E(e^u)e^{-u}Q_{L,\pi}(u)du\) over the VK
weighted ball is at least the right-hand side of (6). The real arithmetic
may be very far from an extremal of that ball; VK alone does not
quantify that distance.

## 6. Monotonicity does not repair the majorant either

The previous point does not depend on allowing arbitrarily oscillatory
errors. Fix a smooth function \(0\le\chi_L\le1\), supported on
\([U_L,U_L+1]\), equal to one on
\([U_L+1/4,U_L+3/4]\), with \(|\chi_L'|\le5\). Set

\[
 E_L(e^u)=-1-{1\over2}e^u e^{-\eta(U_L+1)}\chi_L(u),
 \qquad \Psi_L(y)=y+E_L(y).                              \tag{26}
\]

For \(L\) large,

\[
 \Psi_L'(y)
 =1-{1\over2}e^{-\eta(U_L+1)}
   \{\chi_L(\log y)+\chi_L'(\log y)\}
 \ge0.                                                    \tag{27}
\]

Moreover, by monotonicity of \(\eta\),

\[
 |E_L(e^u)|\le e^u e^{-\eta(u)}                         \tag{28}
\]

for every sufficiently large \(u\); on an initial compact set the
envelope constant can be adjusted. The constant part \(-1\) of
\(E_L\) exactly cancels the boundary term:

\[
 P_{L,\pi}(0)-\int_0^\infty e^{-u}Q_{L,\pi}(u)\,du=0.    \tag{28a}
\]

Moreover,

\[
 |P_{L,\pi}(0)|
 \le\sum_{|k|<L}\alpha_{L,k}(2L+k)
 \le3L.                                                   \tag{28b}
\]

Since the remainder of \(E_L\) and \(Q_{L,\pi}\) are both negative
throughout the support, (23) shows that the version of (3) associated
with \(\Psi_L\) has size

\[
 \exp\!\left\{
 {4\over3}L\log L+{2\over3}L\log\log L-O(L)
 \right\}.                                                \tag{29}
\]

Hence VK plus monotonicity of the accumulating function also fails to
force (1). This comparator is continuous and has no support on prime
powers. It is not a counterexample for the ordinary \(\Lambda(m)\); it
identifies exactly the additional information an arithmetic proof would
have to use.

## 7. Audit against earlier phases

- `103_56` already proves that the modulus of a single Laguerre kernel
  under VK has the wrong scale. Here the new case left open by
  `104_108` is closed: a triangular block of length comparable to the
  degree with uniform modulation. Identity (22) shows why that smoothing
  does not help at frequency \(\pi\).
- `103_70`–`103_71` rule out separate Hardy norms after a Vaughan
  decomposition. Here \(\Lambda\) is not decomposed: (7), (15),
  and (18) keep the full observable.
- `104_41` and `104_107` prove bounds \(O(L)\) and \(O(1)\), respectively,
  at \(a\ge4\). Equation (6) quantifies why VK does not transport those
  bounds down to \(a=1\).
- `104_53` classifies additive polynomial moment identities. The present
  argument introduces neither moments nor cumulants.
- `104_65` deals with fixed local filters. The triangular filter here
  depends on \(L\), has width \(2L-1\), and is therefore not covered by
  that theorem.

## 8. Verdict

**Proved:** the literal prime form (7)–(9), the closed kernels
(12)–(13), the complete contour (15), the joint removal (3), the exact
alignment of the exterior ray (22)–(23), and the VK gap (6).

**Ruled out:** obtaining the uniform bound of `104_108` using only
PNT/VK, even keeping the prime–pole coupling through the integration by
parts and even adding monotonicity of the accumulating function.

**Remains:** proving, for the literal weights \(\Lambda(m)\), a signed
cancellation that makes (3) small uniformly in \(\phi\). It must use
information not contained in the VK size nor in monotonicity; by
`104_108`, a subexponential barrier of that type would prove RH.

**Not proved:** that literal cancellation, (1), A1, or RH.

## 9. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 literal_prime_fejer_vk_gate_check.py
```

The checker uses `Fraction`. It verifies the finite generating-function
identities, \(P-P'=Q\), the sign alignment, and the exterior bound (23)
on exact families. The asymptotic estimate (25) is proved in the text
and is not replaced by sampling.
</content>
