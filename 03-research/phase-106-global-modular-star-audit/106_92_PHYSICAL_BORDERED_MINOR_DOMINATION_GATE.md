# 106.92 — The physical bordered-minor domination gate

## Purpose and conclusion

Documents 106.89--106.91 reduce one negative staircase row, after the
finite radical has been anti-shorted, to the strict comparison

\[
 G_J>\delta_J.
\]

This note puts the comparison into one source-balanced determinant before
any estimate is made.  If

\[
 \tau_{d+1}(Y)=\det\mathbb C_{J,Y},
 \qquad
 \tau_d(Y)=\det\mathbb C_{J,Y}^{-},
\]

then the exact finite crossing condition is

\[
 \boxed{\tau_{d+1}(Y)>\delta_J\tau_d(Y).}          \tag{1}
\]

Inserting the physical source identity turns (1) into

\[
\boxed{
\begin{aligned}
 \tau_{d+1}(Y)
 &+\left[
 \mathscr E_\Gamma(\widetilde q_J^*)
 +\sum_{p^k\le X}\frac{\log p}{p^{k/2}}
  \mathcal J_{k\log p}(\widetilde q_J^*,\widetilde q_J^*)
 \right]\tau_d(Y)\\
 &>\frac12\|\widetilde q_J^*\|_{\mu_K}^{\,2}\tau_d(Y).
\end{aligned}}                                                   \tag{2}
\]

Thus the force-bearing new statement is a physical domination of squared
minors: omitted ordinary-prime minors together with the Gamma and retained
ordinary-prime source energy must dominate the polar-threshold minors.
This statement keeps all terms coupled and has a finite witness whenever
it is strict.

The note also gives an exact rational countermodel.  It has a connected
full-rank omitted tail, a threshold radical, nontrivial old-mode
adaptation, a positive Gamma/head split, literal von Mangoldt weights, and
a theta-sized envelope, but (1) fails.  Consequently no generic
electrical-network, effective-resistance, determinant-monotonicity, or
positive-weight argument proves (2).  A successful proof must use the
literal theta-translation geometry and the mean-periodic constraint of
the Riemann system.

## 1. The bordered physical determinant

Use the notation of 106.91.  In the ordered affine basis

\[
 \mathcal B_J=(e_1,\ldots,e_{M-1},r_1,\ldots,r_J;q_J^*)
\]

write

\[
 \mathbb C_{J,Y}
 =\begin{pmatrix}B_Y&b_Y\\ b_Y^*&h_Y\end{pmatrix}\succ0,
 \qquad
 d=M-1+J.                                         \tag{3}
\]

Its last Schur complement is

\[
 \mathfrak C_J(Y)=h_Y-b_Y^*B_Y^{-1}b_Y
 =\frac{\tau_{d+1}(Y)}{\tau_d(Y)}.               \tag{4}
\]

Let \(e_*\) be the last coordinate vector and define the physical
bordered matrix

\[
 \boxed{\mathbb P_{J,Y}
 :=\mathbb C_{J,Y}-\delta_Je_*e_*^*.}             \tag{5}
\]

### Theorem 1 — Exact source-balanced determinant

For every finite nonempty omitted block,

\[
\boxed{
\begin{aligned}
 \det\mathbb P_{J,Y}
 &=\tau_d(Y)\{\mathfrak C_J(Y)-\delta_J\}\\
 &=\tau_{d+1}(Y)-\delta_J\tau_d(Y).
\end{aligned}}                                                   \tag{6}
\]

Consequently,

\[
 \boxed{
 \det\mathbb P_{J,Y}>0
 \quad\Longleftrightarrow\quad
 \mathfrak C_J(Y)>\delta_J.}                   \tag{7}
\]

#### Proof

Take the Schur complement of \(B_Y\succ0\) in (5).  Only the last
diagonal entry changes, so its Schur complement is

\[
 h_Y-\delta_J-b_Y^*B_Y^{-1}b_Y
 =\mathfrak C_J(Y)-\delta_J.
\]

Multiplication by \(\det B_Y=\tau_d(Y)\) proves (6).  Since
\(\tau_d(Y)>0\), (7) follows. \(\square\)

The effective-resistance notation does not add a sign.  Indeed,

\[
 R_{\mathrm{eff}}(Y)
 :=e_*^*\mathbb C_{J,Y}^{-1}e_*
 =\frac1{\mathfrak C_J(Y)},                       \tag{8}
\]

and the matrix determinant lemma rewrites (6) as

\[
 \det\mathbb P_{J,Y}
 =\det\mathbb C_{J,Y}
  \{1-\delta_JR_{\mathrm{eff}}(Y)\}.             \tag{9}
\]

Thus \(\delta_JR_{\mathrm{eff}}(Y)<1\) is exactly (7), not a new
estimate.

## 2. Inserting Gamma, the retained primes, and the threshold

The joint saddle residual of 106.89 satisfies

\[
 \mathcal A_X(\widetilde q_J^*,\widetilde q_J^*)=-\delta_J.
                                                               \tag{10}
\]

The literal finite-head formula therefore gives

\[
\boxed{
\begin{aligned}
 \delta_J
 ={}&\frac12\|\widetilde q_J^*\|_{\mu_K}^{\,2}
 -\mathscr E_\Gamma(\widetilde q_J^*)\\
 &-\sum_{p^k\le X}\frac{\log p}{p^{k/2}}
 \mathcal J_{k\log p}(\widetilde q_J^*,\widetilde q_J^*).
\end{aligned}}                                                   \tag{11}
\]

Substitution of (11) into the second line of (6) proves that
\(\det\mathbb P_{J,Y}>0\) is exactly (2).  No term has been bounded or
separated in this substitution.

There is also an exact raw-response audit.  Put

\[
 R_J=\|\Pi_JVq_J^*\|^2
 =\mathcal T_X(\widetilde q_J^*,\widetilde q_J^*).               \tag{12}
\]

Since \(\mathcal A_\infty=\mathcal A_X+\mathcal T_X\), (10) gives

\[
 \boxed{R_J-\delta_J
 =\mathcal A_\infty(\widetilde q_J^*,\widetilde q_J^*).}       \tag{13}
\]

The exact adaptive decomposition of 106.89 is

\[
 R_J=G_J+\mathcal L_J,
 \qquad
 \mathcal L_J
 =\|a_\infty-\widehat a\|_{A_\infty}^{\,2}\ge0.               \tag{14}
\]

Hence

\[
 \boxed{
 G_J-\delta_J
 =\mathcal A_\infty(\widetilde q_J^*,\widetilde q_J^*)
 -\mathcal L_J.}                                                 \tag{15}
\]

This identity fixes the exact meaning of “the negative residual retains
enough directional energy.”  Raw energy \(R_J>\delta_J\) is not enough:
the surplus must also pay the common old-mode adaptation loss
\(\mathcal L_J\).  Conversely, (15) contains no artificial loss; its
strict positivity is the desired completed pivot.

## 3. The squared-minor form

Realize the positive old-mode matrix \(\widehat A\) as a finite Gram
feature and adjoin it to the ordinary-prime observation space.  Denote the
resulting positive observation space at cutoff \(Y\) by
\(\Omega_{J,Y}\), and let

\[
 F_1,\ldots,F_d,F_*
\]

be the feature columns of the \(d\) nuisance vectors and of \(q_J^*\).
The Gram--Andreief formula gives

\[
\boxed{
 \tau_{d+1}(Y)
 =\frac1{(d+1)!}
 \int_{\Omega_{J,Y}^{d+1}}
 \left|\det[F_j(\omega_i)]_{{i=1,\ldots,d+1}
 \atop{j=1,\ldots,d,*}}\right|^2
 \prod_{i=1}^{d+1}d\nu_Y(\omega_i),}             \tag{16}
\]

and

\[
\boxed{
 \tau_d(Y)
 =\frac1{d!}
 \int_{\Omega_{J,Y}^{d}}
 \left|\det[F_j(\omega_i)]_{i,j=1}^{d}\right|^2
 \prod_{i=1}^{d}d\nu_Y(\omega_i).}              \tag{17}
\]

Every ordinary-prime-power term in these integrals carries a product of
literal positive factors

\[
 \prod_i\frac{\Lambda(n_i)}{\sqrt{n_i}}.         \tag{18}
\]

Equations (2), (16), and (17) show exactly what a new proof must provide.
It must charge the polar-threshold configurations contributing to

\[
 \frac12\|\widetilde q_J^*\|_{\mu_K}^{\,2}\tau_d(Y)            \tag{19}
\]

into the union of

* captured omitted-prime \((d+1)\)-minors in \(\tau_{d+1}(Y)\);
* Gamma energy times the nuisance \(d\)-minors; and
* retained ordinary-prime energy times the same nuisance minors,

with a strict residual mass.  The same radical correction and the same
old-mode configuration must be retained throughout.  Termwise
minimization, separate radical shorting, or replacing the joint minors by
atomwise floors loses precisely this compatibility.

### Proposition 2 — Finite capture after a strict minor surplus

If the strict version of (2) holds in the cofinal limit \(Y=\infty\),
then it holds for some finite \(Y\).

#### Proof

By 106.91,

\[
 \mathfrak C_J(Y)\nearrow G_J,
 \qquad
 0\le G_J-\mathfrak C_J(Y)\le C Q(Y)e^{-cY}.      \tag{20}
\]

A strict limiting surplus has some margin \(\eta>0\).  Choose \(Y\) so
that the right side of (20) is smaller than \(\eta\).  Then
\(\mathfrak C_J(Y)>\delta_J\), and Theorem 1 gives (2) at that finite
cutoff. \(\square\)

Thus theta decay does not obstruct finite selection after the strict
source-balanced surplus is known.  It also does not produce that surplus.

## 4. A full-rank rational falsifier of generic network arguments

Work on \(\mathbb R^4\), and put

\[
\begin{aligned}
 u&=\tfrac12(1,1,-1,-1)^T,\\
 v&=\tfrac12(1,-1,1,-1)^T,\\
 r&=\tfrac12(1,-1,-1,1)^T.
\end{aligned}                                                     \tag{21}
\]

These vectors are orthonormal and centered.  Define the graph Laplacian

\[
 L=\frac45uu^*+\frac25vv^*+\frac12rr^*.          \tag{22}
\]

Its six edge weights are

\[
 w_{12}=w_{34}=\frac1{40},\qquad
 w_{13}=w_{24}=\frac9{40},\qquad
 w_{14}=w_{23}=\frac7{40},                        \tag{23}
\]

so \(L\) is a positive connected graph generator.  Let \(P\) be the
orthogonal projection onto the centered space.  The completed threshold
form is

\[
 H_\infty=L-\frac12P,
\]

with eigenvalues

\[
 H_\infty u=\frac3{10}u,qquad
 H_\infty v=-\frac1{10}v,qquad
 H_\infty r=0.                                    \tag{24}
\]

Thus \(r\) is an exact threshold radical and \(v\) is a complementary
bound state.

Take the connected star tail

\[
 \boxed{
 T=\frac1{50}\sum_{j=2}^{4}
 (e_1-e_j)(e_1-e_j)^*.}                           \tag{25}
\]

It is strictly positive on the entire centered space.  In the ordered
basis \((u,v,r)\),

\[
 T=
 \begin{pmatrix}
 1/25&1/50&1/50\\
 1/50&1/25&1/50\\
 1/50&1/50&1/25
 \end{pmatrix}.                                   \tag{26}
\]

The current finite-head form is \(H_X=H_\infty-T\).  Maximizing out the
radical coordinate gives

\[
 \widehat H_X=
 \begin{pmatrix}
 27/100&-1/100\\
 -1/100&-13/100
 \end{pmatrix}.                                   \tag{27}
\]

Its old block is positive, its regression coefficient is nonzero,

\[
 \widehat a=-\frac1{27},                          \tag{28}
\]

and its new-mode pivot is

\[
 \widehat\sigma_X
 =-\delta=-\frac{88}{675}.                        \tag{29}
\]

Restoring the full tail \(T\) produces the completed pivot \(-1/10\).
Therefore the exact adaptive gain is

\[
 G=-\frac1{10}+\frac{88}{675}
 =\frac{41}{1350}<\frac{88}{675}=\delta,
 \qquad
 \frac G\delta=\frac{41}{176}.                   \tag{30}
\]

In the stationary old/residual coordinates, the positive augmented gain
matrix is

\[
 \mathbb C=
 \begin{pmatrix}
 3/10&1/90\\
 1/90&187/6075
 \end{pmatrix}.                                   \tag{31}
\]

Direct calculation gives

\[
 \mathfrak C=\frac{41}{1350},\qquad
 R_{\mathrm{eff}}=\frac{1350}{41},\qquad
 \delta R_{\mathrm{eff}}=\frac{176}{41},         \tag{32}
\]

and

\[
 \boxed{\det(\mathbb C-\delta e_*e_*^*)=-\frac3{100}<0.}      \tag{33}
\]

All fractions in (21)--(33) are exact.

The remaining positive graph \(L-T\) may be split, for example equally,
into a Gamma channel and a retained-prime channel.  The tail itself can
be atomized over the ordinary prime powers with the literal weights

\[
 w_n=\frac{\Lambda(n)}{\sqrt n}.
\]

Indeed, choose positive numbers

\[
 \alpha_n
 =\frac{w_ne^{-2\pi n}}
        {\sum_{m=p^k}w_me^{-2\pi m}},
 \qquad
 D_n=\sqrt{\frac{\alpha_n}{w_n}}\,T^{1/2}.        \tag{34}
\]

Then

\[
 \sum_{n=p^k}w_nD_n^*D_n=T,                      \tag{35}
\]

every atom has a theta-sized envelope, and the complete tail remains
strictly positive on the centered space.  Nevertheless the bordered
determinant is negative by (33).

This model does not have the literal maps

\[
 q\longmapsto
 \sqrt{K(x)K(x-\log n)}\{q(x)-q(x-\log n)\}
\]

or the Riemann mean-periodic equation.  That is exactly its purpose: it
proves that those two specific structures, rather than generic network
positivity, must supply any proof of (2).

## 5. Ledger conclusion

The following statements are now exact.

1.  The cumulative block-gain condition
    \(\sum_j\Delta_{\mathcal B_j}>-\sigma_{M,X_0}\), the bordered
    determinant sign (7), and the effective-resistance condition
    \(\delta_JR_{\mathrm{eff}}<1\) are the same condition.
2.  The physical source identity converts that condition into the
    coupled squared-minor inequality (2).
3.  A strict cofinal minor surplus always has a finite ordinary-prime
    witness before the theta envelope disappears.
4.  Positive literal weights, full-rank tail observability, graph
    structure, Gamma/head positivity, an exact threshold radical,
    determinant monotonicity, adaptation, and theta-scale summability do
    not force the sign.

The surviving arithmetic theorem is therefore the following: prove (2)
for the literal theta displacements and the ordinary values
\(\Lambda(p^k)=\log p\), using the Riemann mean-periodic constraint, with
one common old-mode/radical correction.  This theorem has not been proved
here; it is the precise source-balanced minor-domination gate.
