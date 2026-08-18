# 106.15 — The signed prime--Gamma branch gate

## Purpose

Document 106.12 proves the exact moving co-Poisson identity

\[
 QW_\lambda(V_\lambda,G)=-QW(R_\lambda,G),
 \qquad
 QW_\lambda(V_\lambda,V_\lambda)=QW(R_\lambda,R_\lambda),
 \tag{1}
\]

and retains the pole, Gamma factor, primes and prime powers in the single
trace expression

\[
 W_{0,2}(H)+\log(TW)H(1)
 +\mathrm{Tr}\,\!\left(
   \vartheta(H)(1-P_T^S-\widehat P_W^S)\right)
 =-QW(R_\lambda,G),
 \quad H=V_\lambda^**G.
 \tag{2}
\]

The same construction gives the prolate angle levels

\[
 d_4\asymp\lambda^9e^{-4\pi\lambda^2},
 \qquad
 d_8\asymp\lambda^{17}e^{-4\pi\lambda^2}.
 \tag{3}
\]

This note determines exactly what (2)--(3) do and do not supply. There are
two conclusions.

1. The trace projection has two order-one branches even when the prolate
   leakage is exponentially small. Thus angle concentration determines the
   square of the trace branch, not its sign.
2. The branch residual is linear in the exterior leakage, whereas the
   Rayleigh identity in (1) is quadratic. Even a polynomial graph-norm
   estimate would miss the required residual scale by
   \(e^{2\pi\lambda^2}\).

The remaining theorem is therefore one explicit signed arithmetic estimate,
stated in Section 5. No assertion below proves that estimate or RH.

## 1. Principal-angle normal form

Let \(P,Q\) be two orthogonal projections and let \(e\in\mathrm{Ran}\,P\)
be a principal vector with

\[
 PQP e=\chi^2e,
 \qquad 0<\chi<1.
 \tag{4}
\]

Put \(s=(1-\chi^2)^{1/2}\). In the two-dimensional principal plane one may
choose an orthonormal basis in which

\[
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 Q=\begin{pmatrix}\chi^2&\chi s\\\chi s&s^2\end{pmatrix}.
 \tag{5}
\]

### Theorem 1 — The angle fixes the square, not the branch

For

\[
 B:=I-P-Q
 \tag{6}
\]

one has

\[
 \boxed{
 B=\begin{pmatrix}-\chi^2&-\chi s\\-\chi s&\chi^2\end{pmatrix},
 \qquad
 B^2=\chi^2I,
 \qquad
 \sigma(B)=\{-\chi,+\chi\}.}
 \tag{7}
\]

In particular, if the angle leakage is

\[
 d=1-\chi^2\longrightarrow0,
 \tag{8}
\]

then both branches of \(B\) converge in modulus to one. There is no
constant \(C\), independent of \(d\), for which

\[
 |B|\le Cd,
 \qquad B\ge cdI,
 \qquad\text{or}\qquad -B\ge cdI
 \tag{9}
\]

holds on the principal plane.

#### Proof

Substitution of (5) into (6) gives the displayed matrix in (7). Direct
multiplication gives \(B^2=\chi^2I\); its trace is zero, so its eigenvalues
are \(\pm\chi\). Equation (8) gives \(\chi\to1\), proving the last claim.
\(\square\)

### Corollary 2 — No geometric sign in the semilocal trace

Let \(A=\vartheta(V_\lambda)\) and \(C=\vartheta(G)\). The trace term in
(2) is

\[
 \mathrm{Tr}(A^*CB).
 \tag{10}
\]

For \(G=V_\lambda\), this is a weighted difference of the positive and
negative principal branches of \(B\). For a cross term it has no sign even
formally, since replacing \(G\) by \(-G\) reverses it. The generic bound is

\[
 \left|\mathrm{Tr}(A^*CB)\right|
 \le\|A\|_{\mathrm {HS}}\|C\|_{\mathrm {HS}},
 \tag{11}
\]

because \(\|B\|\le1\). The two-dimensional block (7) proves that the
constant in (11) does not acquire a factor \(d\) as the angle closes.

Thus the trace formula gives an exact coupled cancellation but not a free
choice of its fundamental branch. Any branch selector must show that the
ordinary-prime matrix coefficient \(A^*C\), together with the polar term,
has quantitatively biased mass between the two signs in (7).

## 2. Linear residual versus quadratic Rayleigh value

Normalize the first moving vector and its exterior remainder by

\[
 q_L=V_\lambda/\|V_\lambda\|,
 \qquad
 r_L=R_\lambda/\|V_\lambda\|.
 \tag{12}
\]

Let \(A_L\) be the semilocal Weil operator and set

\[
 R_L=\langle A_Lq_L,q_L\rangle,
 \qquad
 b_L=(1-|q_L\rangle\langle q_L|)A_Lq_L.
 \tag{13}
\]

### Theorem 3 — Exact first-variation identity

One has

\[
 \boxed{
 \|b_L\|
 =\sup_{\substack{g\perp q_L\\\|g\|=1}}
   |QW_\lambda(q_L,g)|
 =\sup_{\substack{g\perp q_L\\\|g\|=1}}
   |QW(r_L,g)|,}
 \tag{14}
\]

whereas

\[
 \boxed{R_L=QW(r_L,r_L).}
 \tag{15}
\]

#### Proof

The first equality in (14) is the Riesz representation of the projected
operator residual. The moving-radical identity (1), divided by
\(\|V_\lambda\|\), gives the second. The quadratic identity in (1), divided
by \(\|V_\lambda\|^2\), gives (15). \(\square\)

Equation (14) is linear in the exterior error; (15) is quadratic. The
prolate identity proves only

\[
 \|(1-P_\lambda)\widehat f_\lambda\|_2^2\asymp d_4.
 \tag{16}
\]

It supplies neither the form-dual norm in (14) nor a uniform logarithmic
Gamma graph norm. Therefore the proved inputs currently give no
quantitative decay rate for \(\|b_L\|\).

## 3. Scale of an absolute graph-norm estimate

The deficit persists even if one adds the natural missing regularity as an
assumption. Suppose, for some polynomially bounded \(P(\lambda)\), that the
exterior coordinate satisfies both an \(L^2\) bound of size \(d_4\) and

\[
 \int_{\mathbb R}\log^2(2+|t|)
       |\widehat r_L(t)|^2\,dt
 \le P(\lambda)^2d_4.
 \tag{17}
\]

The finite prime translations and polar block have norm \(O(\lambda)\),
while (17) controls the Gamma multiplier. Termwise estimation would then
give at best

\[
 \|b_L\|=O\!\left((\lambda+P(\lambda))\sqrt{d_4}\right).
 \tag{18}
\]

This is still exponentially larger than the branch scale required in
106.12:

\[
 \|b_L\|=o(\lambda^{-B}d_8),
 \qquad B<\tfrac12.
 \tag{19}
\]

Indeed,

\[
 \frac{(\lambda+P(\lambda))\sqrt{d_4}}
      {\lambda^{-B}d_8}
 \asymp
 (\lambda+P(\lambda))
 \lambda^{B-25/2}e^{2\pi\lambda^2}.
 \tag{20}
\]

No polynomial regularity estimate can make (20) tend to zero. Relative to
the natural linear leakage scale, the extra cancellation required by (19)
is

\[
 \boxed{
 \frac{\lambda^{-B}d_8}{\sqrt{d_4}}
 \asymp
 \lambda^{25/2-B}e^{-2\pi\lambda^2}.}
 \tag{21}
\]

Thus the desired selector must cancel the complete first variation in
(14); controlling the prime, Gamma and polar blocks separately cannot reach
the target.

## 4. The complementary branch

Define

\[
 \beta_L=inf_{\substack{g\perp q_L\\\|g\|=1}}
             QW_\lambda(g,g).
 \tag{22}
\]

If \(R_L<\beta_L\), the scalar Schur complement and min--max principle give

\[
 \lambda_2(A_L)\ge\beta_L,
 \qquad
 0\le R_L-\epsilon_{0,L}
 \le\frac{\|b_L\|^2}{\beta_L-R_L}.
 \tag{23}
\]

Hence the exact sufficient package is

\[
 R_L=O(d_4),qquad
 \beta_L\ge c d_8,qquad
 \lambda^B\frac{\|b_L\|}{\beta_L-R_L}\longrightarrow0
 \quad(B<\tfrac12).
 \tag{24}
\]

The first two fixed prolate angle levels do not prove (24): Theorem 1
shows that their common projection geometry contains both trace branches,
and Theorem 3 shows that their shared leakage cancels from a residual to
overlap quotient.

## 5. The remaining signed arithmetic theorem

The narrow source-side target can now be stated without separating any
local contribution.

### Gate SPG — Signed prime--Gamma branch selector

For the normalized first moving vector \(q_L\), uniformly for unit
\(g\perp q_L\), put \(H=q_L^**g\). Prove, for every \(B<1/2\),

\[
 \boxed{
 \left|
 W_{0,2}(H)+\log(TW)H(1)
 +\mathrm{Tr}\,\!\left(
   \vartheta(H)(1-P_T^S-\widehat P_W^S)\right)
 \right|
 =o(\lambda^{-B}d_8),}
 \tag{25}
\]

together with

\[
 \boxed{
 \inf_{\substack{g\perp q_L\\\|g\|=1}}
 \left[
 W_{0,2}(g^**g)+\log(TW)(g^**g)(1)
 +\mathrm{Tr}\,\!\left(
  \vartheta(g^**g)(1-P_T^S-\widehat P_W^S)\right)
 \right]
 \ge c d_8.}
 \tag{26}
\]

Equations (25)--(26) are exactly the cross and complementary estimates in
(24), written with primes, prime powers, Gamma and pole still coupled.
They are not consequences of the projection identity: the arithmetic
representation \(\vartheta(H)\) is essential.

### Theorem 4 — Conditional closure

Assume Gate SPG, \(R_L=O(d_4)\), and the model-transform identification in
Gate B of 106.07. Then the weighted curvature gate holds. Consequently RH
holds.

#### Proof

Equations (25)--(26) give the last two estimates in (24). Equation (23),
combined with \(d_4/d_8\asymp\lambda^{-8}\), gives the weighted
Rayleigh-excess/gap limit of Gate B. Document 106.07 converts that limit to
the normalized curvature convergence, and its divisor-contour theorem
implies RH. Equivalently, 106.08 and the bilateral fixed-negative-test
theorem 106.11 exclude either parity ground branch under failure of RH.
\(\square\)

## 6. Falsifier and verdict

For a divisor containing an off-line quartet, the same angle form and the
same two branches (7) remain available, but the Weil form has a fixed
negative test in both parity sectors by 106.11. Therefore a proof of
(25)--(26) based only on projection geometry, prolate concentration or
Poisson summation is invalid. It must use the actual ordinary-prime weights
inside the coupled trace coefficient.

The joint prime--Gamma cancellation requested at the start of this attack
is proved by (1)--(2). Quantitative selection of the fundamental branch is
not proved. It has been reduced to Gate SPG, and the scale audit shows that
Gate SPG requires cancellation of the entire linear leakage term, not a
sharper absolute estimate.
