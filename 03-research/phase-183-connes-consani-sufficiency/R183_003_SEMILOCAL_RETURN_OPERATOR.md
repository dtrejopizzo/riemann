# R183.003 — The semilocal return operator

> **Status corrected by R183.014–016.** Vector identity (1.2)
> is valid and does not require trace class. What is withdrawn is presenting a
> vector-by-vector contraction as an equivalent reduction of the conjecture:
> R183.016 proves that the sandwich is indefinite for every nonzero smooth
> test in the modulus sector. The trace does admit the regularized limit
> of R183.014–015. R183.004's source factorization is not proved.

## Verdict

The original candidate required building a contractive return operator.
This is a sufficient condition that is too strong, not an equivalent
reduction. The vector condition is refuted in R183.016's sector; this does
not refute Connes–Consani's trace inequality.

The sign follows from the contractivity of a **return between tails**. The
co-Poisson sum determines a finite recipe for that return. What remains is to
type it in the semilocal quotient and prove that it converges, after removing
the two Tate modes, to a contraction. This statement fixes the object before
asking about its sign.

## 1. Exact norm difference

Let \({\cal H}_S=L^2(X_S)\), let \(P\) be the half-line projector of the
quantized calculus, \(Q=1-P\), and let

\[
        u_S=I{\cal F}_S
\]

be Tate's scattering unitary in the scaling representation. For a test \(h\),
let \(M_h\) be its multiplicative convolution operator. Connes--Consani's
operator is

\[
 A_S=\frac12u_S^*[2P-1,u_S]=u_S^*Pu_S-P .          \tag{1.1}
\]

Hence, on every core where the expressions are defined,

\[
 \boxed{
 -\langle M_hf,A_SM_hf\rangle
 =\|Qu_SM_hf\|^2-\|QM_hf\|^2 .}                   \tag{1.2}
\]

The equality only uses \(P+Q=1\) and the unitarity of \(u_S\). Define

\[
 B_{q,h}=Qu_SM_h,\qquad C_{q,h}=QM_h .              \tag{1.3}
\]

Thus, Weil's inequality, with the article's sign conventions, is

\[
          B_{q,h}^*B_{q,h}-C_{q,h}^*C_{q,h}\geq0   \tag{1.4}
\]

on the vectors satisfying the two Tate moments.

## 2. Return sufficiency theorem

**Theorem 183.R (PROVED).** Suppose that, without using zeros of zeta, an operator

\[
 {\cal R}_{q,h}:\overline{\operatorname{Ran}B_{q,h}}
          \longrightarrow {\cal H}_S              \tag{2.1}
\]

is built satisfying

\[
 C_{q,h}={\cal R}_{q,h}B_{q,h},\qquad
 \|{\cal R}_{q,h}\|\leq1.                         \tag{2.2}
\]

Then

\[
 \boxed{
 -\langle M_hf,A_SM_hf\rangle
 =\|(1-{\cal R}_{q,h}^*{\cal R}_{q,h})^{1/2}
       B_{q,h}f\|^2\geq0 .}                        \tag{2.3}
\]

In particular, if (2.2) holds for \(S(q)=\{\infty\}\cup\{p:p<q\}\), for every \(h\) supported on \((q^{-1/2},q^{1/2})\) with both moments vanishing, Connes--Consani's Conjecture 4.1 is proved, and, by the semilocal trace theorem, so is Weil's inequality.

**Proof.** Substitute \(C={\cal R}B\) into (1.2):

\[
 \|Bf\|^2-\|Cf\|^2
 =\langle Bf,(1-{\cal R}^*{\cal R})Bf\rangle.
\]

The second hypothesis of (2.2) gives (2.3). \(\square\)

This only adds content if \({\cal R}_{q,h}\) is built via Poisson before knowing (1.4). Defining it as \(CB^\dagger\) would be circular and is excluded.

## 3. Arithmetic source of the candidate

Set

\[
 S_f(q)=\{p:p<q\},\qquad
 M_S=\{m\geq1:(m,\prod_{p<q}p)=1\}.
\]

Unique factorization gives the exact gap

\[
 m\in M_S,\ m>1\quad\Longrightarrow\quad m\geq q. \tag{3.1}
\]

For a finite arithmetic truncation \(R\), the central co-Poisson sum is

\[
 E_S^{[R]}=1+V_S^{[R]},\qquad
 V_S^{[R]}=\sum_{\substack{m\in M_S\\1<m\leq R}}
                    m^{-1/2}D_m,                   \tag{3.2}
\]

where \(D_m\) translates the logarithmic coordinate by \(\log m\). If \(T=\tfrac12\log q\), (3.1) implies

\[
             P_TV_S^{[R]}P_T=0.                    \tag{3.3}
\]

This is the precise use of the individual arithmetic of \(\mathbb Z\). The semilocal Poisson formula gives, for the full operator on its natural core, the central intertwining

\[
             E_S{\cal F}_S=I E_S,                  \tag{3.4}
\]

with the terms at zero and the integral removed by the two Tate functionals. Equations (3.3) and (3.4) are the arithmetic triangularity and the Poisson orientation. Neither alone produces a sign.

Fix a bounded scaling band \((-L,L)\). In each sector where the shifts point towards the same boundary, the compression of \(V_S^{[R]}\) is nilpotent, since each step advances by at least \(2T\). Its elimination then has the finite algebraic inverse

\[
 (1+V_S^{[R]})^{-1}
 =\sum_{j=0}^{J(L,T)}(-V_S^{[R]})^j .              \tag{3.5}
\]

The return recipe is: lift the tail via (3.5), apply additive Fourier and inversion as in (3.4), remove the co-Poisson sum again, and project onto the opposite tail and the kernel of the two Tate moments. At the finite level, once the quotient maps of \(X_S\) are written, we denote the result by

\[
                 {\cal R}_{q,h}^{[R,L]}.           \tag{3.6}
\]

The fully typed formula of (3.6) is not yet built. We do not use a deformation in \(\sigma\): the dual sum outside the region of convergence would require analytic continuation and could circularly introduce the sought datum.

## 4. Central theorem that would close the route

**Semilocal return theorem (OPEN).** For every \(q>1\) and every \(h\) with

\[
 \operatorname{supp}h\subset(q^{-1/2},q^{1/2}),\qquad
 \int h(x)x^{\pm1/2}d^*x=0,                       \tag{4.1}
\]

the finite operators (3.6) are well typed and the renormalized limit

\[
 {\cal R}_{q,h}=\lim_{L\to\infty}\lim_{R\to\infty}
                 {\cal R}_{q,h}^{[R,L]}            \tag{4.2}
\]

exists in \(L^2(X_{S(q)})\), is independent of the regularization, and satisfies

\[
 C_{q,h}={\cal R}_{q,h}B_{q,h},\qquad
 {\cal R}_{q,h}^*{\cal R}_{q,h}\leq1.             \tag{4.3}
\]

The stronger geometric version asks for a source realization

\[
 1-{\cal R}_{q,h}^*{\cal R}_{q,h}
       ={\cal Z}_{q,h}^*{\cal Z}_{q,h},            \tag{4.4}
\]

where \({\cal Z}_{q,h}\) is the flow that crosses the scaling boundary exactly once, and not a square root defined from the left-hand side.

By Theorem 183.R, (4.3) suffices to close D.

## 5. Logical status

* Exact norm difference (1.2): **PROVED**.
* Sufficiency Theorem 183.R: **PROVED**.
* Gap \(m\geq q\) and absence of interior return (3.3): **PROVED**.
* Poisson intertwining (3.4): **CITED/PROVED** in the semilocal framework, on its natural core.
* Finite triangular elimination (3.5): **PROVED** in each oriented sector and finite band.
* Explicit typing of (3.6) in the quotient: **OPEN**.
* Existence of the limit (4.2): **OPEN**.
* Contractivity (4.3): **OPEN**.
* Flow factorization (4.4): **OPEN**.
* Row D: **OPEN**.

The progress is to localize the sign in an operational statement: Poisson must transform one outgoing tail into the other via a contraction. The Euler product determines the returns and the gap (3.1) prevents interior returns; Poisson determines their orientation. What remains is to control the limit of a concrete triangular elimination on the quotient of the two Tate modes.
