# R170_301 — Coherent coupling of primes and Gamma via paths

**Unconditional construction of the coupling; global
sign OPEN.** No external literature was consulted. No novelty is claimed
for the resolvent method or the contraction criterion.

## 1. What is built and what is not

R170_201 separated the prime towers and left a negative remainder. Here
a common operator is built that includes the prime jumps, Gamma, and the
positive polar part. Its inverse has a convergent expansion that
preserves all interactions between primes. The construction and its
convergence do not require W_T≥0.

The target form becomes a single defect energy on that space of sources.
The sign of the defect remains a pending condition; it is not defined
as an inner product before being proved.

We work in H_T=L²(−T,T), extended by zero. All the unbounded operators
below are defined through their closed forms on 𝒟_T. The translations
S_u are taken in L²(ℝ); P_T denotes compression to H_T. We fix the inner
product to be linear in the first argument.

## 2. A positive operator built without the sign of W

Define

$$k(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad
m_0=m(0)=-\gamma_{\!E}-\frac\pi2-3\log2-\log\pi<0.$$

The digamma series, with the τ=0 value subtracted, gives

$$m(\tau)-m_0=2\int_0^\infty k(u)(1-\cos\tau u)\,du\ge0.$$

By Plancherel and Tonelli, the shifted archimedean form is

$$\Gamma_T(F)=\frac1{2\pi}\int (m(\tau)-m_0)|\widehat F(\tau)|^2d\tau
=\int_0^\infty k(u)\|F-S_uF\|_{L^2(\mathbb R)}^2du.\tag{1}$$

For u≥2T the supports are disjoint. Hence

$$\Gamma_T\ge\alpha_TI,\qquad
\alpha_T=2\int_{2T}^\infty k(u)du
=2[\operatorname{artanh}(e^{-T})+\arctan(e^{-T})]>0.\tag{2}$$

The last integral is computed with v=e^{-u/2}. This coercivity belongs
to the auxiliary operator Γ_T, not to a positive bound for W_T.

Let

$$a_n=\Lambda(n)/\sqrt n,\quad
A_T=\sum_{2\le n<e^{2T}}a_n,\quad
J_T=\sum_{2\le n<e^{2T}}a_nP_T(S_{\log n}+S_{\log n}^*)P_T.$$

Then J_T is self-adjoint and ‖J_T‖≤2A_T. With c(t)=cosh(t/2),
s(t)=sinh(t/2), we use |c⟩⟨c| for the operator F↦⟨F,c⟩c. Define

$$\boxed{E_T=\Gamma_T+2A_TI-J_T+2|c\rangle\langle c|,}\tag{3}$$
$$C_T=b_TI+2|s\rangle\langle s|,\qquad b_T=2A_T-m_0>0.\tag{4}$$

The form (3) is an explicit positive sum:

$$\langle E_TF,F\rangle=\Gamma_T(F)
+\sum_n a_n\|F-S_{\log n}F\|^2+2|\langle F,c\rangle|^2
\ge\alpha_T\|F\|^2.\tag{5}$$

Also, since 2Re(A(F)overline{B(F)})=2|⟨F,c⟩|²−2|⟨F,s⟩|²,

$$\boxed{W_T(F)=\langle E_TF,F\rangle-\langle C_TF,F\rangle.}\tag{6}$$

The diagonal cost appears on both sides of (6). The difference from
R170_201 is that we do not try to prove the sign of a separate
remainder: we build the common transfer E_T⁻¹ that mixes all the sources.

## 3. The inverse has convergent arithmetic paths

Set

$$B_T=\Gamma_T+2A_TI+2|c\rangle\langle c|,\quad
R_T=B_T^{-1/2}J_TB_T^{-1/2},\quad
\beta_T=2A_T+\alpha_T.$$

**Theorem 1.** Without assuming RH or W_T≥0,

$$\|R_T\|\le r_T:=\frac{2A_T}{2A_T+\alpha_T}<1,$$
$$\boxed{E_T^{-1}=B_T^{-1/2}\sum_{j=0}^\infty R_T^jB_T^{-1/2}.}\tag{7}$$

For the truncation after j=L,

$$\left\|E_T^{-1}-B_T^{-1/2}\sum_{j=0}^L R_T^jB_T^{-1/2}\right\|
\le\frac{r_T^{L+1}}{\alpha_T}.\tag{8}$$

**Proof.** B_T≥β_TI and ‖J_T‖≤2A_T. Hence ‖R_T‖≤r_T<1 and
E_T=B_T^{1/2}(I−R_T)B_T^{1/2} in the sense of forms. The Neumann series
and β_T(1−r_T)=α_T give (7)–(8). If A_T=0, R_T=0 and the inverse is
B_T⁻¹. ∎

Convergence holds for each T, with an explicit error formula. It is not
a contraction with a margin uniform in T: r_T approaches 1 as T grows.
The global sign quantifier is not obtained from this.

Writing J_T=Σ_nJ_n, the second-order terms include

$$\sum_{n,m}B_T^{-1}J_nB_T^{-1}J_mB_T^{-1}.\tag{9}$$

For n=p^k, m=q^l, p≠q, (9) preserves the coupling between primes.
Between each pair of jumps the same archimedean/polar inverse B_T⁻¹ acts,
with the support conditions. It is not replaced by a scalar weight, nor
is the interaction declared to be zero. The higher orders preserve all
the sequences of active primes and powers.

This avoids the attempt to directly identify V*V with Gamma:
the ratios are not erased; they form part of a series of coupled
operators. This does not imply that their contributions have the
desired final sign.

## 4. A single defect energy with all channels

Let 𝒢_T be the source operator whose components are

$$\sqrt{k(u)}(F-S_uF),\quad
(\sqrt{a_n}(F-S_{\log n}F))_n,\quad\sqrt2\langle F,c\rangle.$$

Its target space is the Hilbert sum of the continuous channel in (u,t),
the discrete channels in t, and a scalar. By (5), 𝒢_T*𝒢_T=E_T.
If 𝒢_T=U_TE_T^{1/2} is its polar decomposition, U_T is an isometry
from H_T onto the closed range of 𝒢_T. Define there

$$\mathcal T_T=C_T^{1/2}E_T^{-1/2}U_T^*.$$

It is bounded, ‖𝒯_T‖²≤‖C_T‖/α_T, and satisfies exactly

$$\mathcal T_T\mathcal G_TF=C_T^{1/2}F.$$

So,

$$\boxed{W_T(F)=\langle\mathcal G_TF,
(I-\mathcal T_T^*\mathcal T_T)\mathcal G_TF\rangle.}\tag{10}$$

In particular, the right-hand side of (10) has not been called a "norm".
Its metric is positive only if the pending contraction is proved.

Equivalently, and computable from (7), define

$$K_T=C_T^{1/2}E_T^{-1}C_T^{1/2}.$$

**Theorem 2.**

$$W_T\ge0\quad\Longleftrightarrow\quad K_T\le I
\quad\Longleftrightarrow\quad\|\mathcal T_T\|\le1.\tag{11}$$

**Proof.** In (6), changing variable to E_T^{1/2}F gives
I−E_T⁻¹ᐟ²C_TE_T⁻¹ᐟ². The norm of that positive product is
‖C_T¹ᐟ²E_T⁻¹ᐟ²‖²=‖K_T‖. The same norm is ‖𝒯_T‖². ∎

## 5. Positive grouping of the paths and explicit error

Although the odd powers of R_T may carry a sign, the orders 2j and 2j+1
can be grouped with no loss of any interaction. With
Y_T=B_T⁻¹ᐟ²C_T¹ᐟ² and

$$L_{j,T}=(I+R_T)^{1/2}R_T^jY_T,$$

one has the positive identity, convergent in norm,

$$\boxed{K_T=\sum_{j=0}^\infty L_{j,T}^*L_{j,T}.}\tag{12}$$

This follows from R_T self-adjoint, ‖R_T‖<1 and
Σ_jR_T^{2j}(I+R_T)=(I−R_T)⁻¹. The truncations
K_T^{[M]}=Σ_{j=0}^M L_{j,T}*L_{j,T} satisfy

$$0\le K_T-K_T^{[M]}\le
\frac{\|C_T\|}{\alpha_T}r_T^{2M+2}I,\qquad
\|C_T\|=b_T+2(\sinh T-T).\tag{13}$$

Here ‖s‖²=sinh T−T. Hence a certification of
K_T^{[M]}≤(1−ε)I, with ε at least the error of (13), would suffice
for that window. The operators remain infinite-dimensional; a
discretization adds another error that (13) does not control.

The pending global inequality is now written exactly as

$$\forall T>0\ \forall x\in H_T:\quad
\sum_{j\ge0}\|L_{j,T}x\|^2\le\|x\|^2.\tag{14}$$

The positivity of each summand of (12) does not give the upper bound
(14). Confusing those orientations would produce a false proof.

## 6. Non-circularity and arithmetic audit

E_T≥α_T and the series (7) are proved before the sign of W. W is not
inverted, nor is a hypothetical first contact assumed invertible. At
that contact K_T may have eigenvalue 1 with no effect on the
construction.

However, the whole construction above also works for arbitrary
nonnegative weights on a finite set of jumps. For example, fix
T>½log 2 and a smooth real test F with c_F(log 2)>0. Replacing the
single weight a_2 by a>0 gives

$$W^{(a)}_T(F)=\mathfrak a_\infty(F)+P(F)-2a\,c_F(\log2)<0$$

for a sufficiently large. E_T remains positive, its series still
converges, but ‖K_T‖>1. Hence **the coupling and its convergence do
not force the contraction**. The exact weights of Λ are present in (9),
but an identity exclusive to ℤ has not yet been used to prove (14).

A falsifier can be fixed with no computation of zeros or quadrature:
T=1, F=1_(−1,1)/√2 and a=100. This F belongs to 𝒟_1. Then
c_F(log2)=1−log2/2>1/2. By (1),

$$\Gamma_1(F)=\int_0^2u\,k(u)du+2\int_2^\infty k(u)du<3+2=5.$$

For the first term we use k(u)≤1+1/(2u); for the second, (2) and
e⁻¹<2/5, artanh(2/5)<1/2, arctan(2/5)<1/2. The polar term is
16sinh²(1/2)<16, and m₀<0. Consequently

$$W^{(100)}_1(F)<5+16-100=-79.\tag{15}$$

This system is not Λ: it only falsifies the claim that the construction
and convergence identities alone could imply (14).

## 7. Relation to the corpus and result

Phase 106.105 already establishes that an exact transfer has a norm
fixed by the spectral threshold. R161_073 builds a stabilized inverse
at first contact; R166_405 P11 collects contraction criteria.
This note does not claim to overcome those obstructions: it implements
the coupling in the original variables with an explicit coercivity,
a convergent path series with no RH, and the remainder (13).

**Solved here:** building the coupling without separating the primes
nor peeling off Gamma as a remainder assumed positive on its own.

**Not solved:** proving (14) for the weights Λ and all T. By (11),
claiming that (10) is already a positive energy would amount to
asserting the global goal without having proved it. The construction
is not yet the requested sign mechanism.

## 8. Reproducible verification

`verify_coherent_paths.py` implements normalized cell indicators on
(−T,T). It integrates the kernel k of (1) to obtain the Gamma matrix,
uses exact interval intersections for the jumps, and hyperbolic moments
for the pole. It checks:

- E−C=W computed separately from the three original terms;
- evaluation of the constant indicator, independent of the partition;
- the auxiliary coercivity and the bound on ‖R‖;
- the resolvent identity, positivity of the pairs, and bound (13);
- a nonzero mixed path between primes 2 and 3;
- the loss of contraction in the falsifier a₂=100.

The results are in `coherent_paths_diagnostics.json`. T=1/2, (log5)/2,
1 and 3/2 were tested with 24 and 48 cells. These are Galerkin
diagnostics with floating-point quadrature, **not new positivity
certificates**. Positive matrices on a subspace do not control their
complement; bound (13) controls path truncation, not Galerkin error.
Inverting a compressed matrix is also not the same as compressing the
inverse of the continuum.
</content>
