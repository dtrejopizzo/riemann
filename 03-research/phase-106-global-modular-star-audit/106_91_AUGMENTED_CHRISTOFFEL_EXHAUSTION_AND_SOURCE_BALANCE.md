# 106.91 — Augmented Christoffel exhaustion and source balance

## Purpose and conclusion

Document 106.90 gives local Christoffel lower bounds for the
radical-conditioned adaptive gain \(G_J\). This note removes the
localization loss by retaining the old-mode penalty and the full literal
ordinary-prime displacement forms in one augmented determinant.

For every finite cutoff \(Y>X\), define

\[
\begin{aligned}
\mathfrak C_J(Y)
:=\inf_{d\in V_{M-1},\,r\in\mathcal R_J}
\bigg\{&
\widehat{\mathcal A}(d,d)\\
&+\sum_{\substack{n=p^k\\X<n\le Y}}
\frac{\Lambda(n)}{\sqrt n}\,
\mathcal J_{\log n}(q_J^*+d+r,q_J^*+d+r)
\bigg\}.
\end{aligned}                                                    \tag{1}
\]

The main theorem is

\[
\boxed{
0<\mathfrak C_J(Y)<G_J,\qquad
\mathfrak C_J(Y)\nearrow G_J.}                                  \tag{2}
\]

Moreover, \(\mathfrak C_J(Y)\) is the Schur determinant ratio of one
explicit finite matrix. If the current anti-shorted pivot is
\(-\delta_J\), then

\[
\boxed{
\sigma_\infty>0
\quad\Longleftrightarrow\quad
\mathfrak C_J(Y)>\delta_J
\text{ for some finite }Y.}                                    \tag{3}
\]

This does not prove the required sign. It shows that neither local
Christoffel loss, atomwise minimization, infinite-tail convergence, nor
finite selection remains in the sharp determinant formulation.

## 1. Setup

Use the notation of 106.89--106.90:

\[
V_M=V_{M-1}\oplus\operatorname{span}\{\phi_M\},
\qquad
\mathcal R_J=\operatorname{span}\{r_1,\ldots,r_J\}.              \tag{4}
\]

Assume the preceding block of the finite maximal-radical anti-short is
positive definite. Denote its form on \(V_{M-1}\) by
\(\widehat{\mathcal A}\), its adaptive residual by
\(q_J^*\in\phi_M+V_{M-1}\), and its new-mode pivot by

\[
\widehat\sigma_X=-\delta_J<0.                                   \tag{5}
\]

For every omitted prime power \(n=p^k>X\), put

\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
u_n=\log n,                                                     \tag{6}
\]

and define

\[
\mathcal J_u(q,s)
=\int_{\mathbb R}K(x)K(x-u)
\{q(x)-q(x-u)\}
\overline{\{s(x)-s(x-u)\}}\,dx.                                \tag{7}
\]

The exact radical-conditioned gain is

\[
\boxed{
G_J=\inf_{d\in V_{M-1},\,r\in\mathcal R_J}
\left\{
\widehat{\mathcal A}(d,d)
+\sum_{n>X}w_n\mathcal J_{u_n}(q_J^*+d+r,q_J^*+d+r)
\right\}.}                                                       \tag{8}
\]

Document 106.89 gives the completed source balance

\[
\boxed{\sigma_\infty=-\delta_J+G_J.}                            \tag{9}
\]

## 2. The augmented finite determinant

Choose a basis \(e_1,\ldots,e_{M-1}\) of \(V_{M-1}\) and use the ordered
affine basis

\[
\mathcal B_J=(e_1,\ldots,e_{M-1},r_1,\ldots,r_J;q_J^*).          \tag{10}
\]

Let \(\mathbb G_n\) be the Gram matrix of \(\mathcal J_{u_n}\) in this
basis. Embed the old positive matrix as

\[
\mathbb A_-=
\begin{pmatrix}
\widehat A&0&0\\
0&0_J&0\\
0&0&0
\end{pmatrix},                                                  \tag{11}
\]

and set

\[
\mathbb C_{J,Y}
=\mathbb A_-+
\sum_{\substack{n=p^k\\X<n\le Y}}w_n\mathbb G_n.                \tag{12}
\]

Let \(\mathbb C_{J,Y}^{-}\) be the principal block obtained by deleting
the last row and column.

### Theorem 1 — Determinant formula

If the sum in (12) is nonempty, then

\[
\mathbb C_{J,Y}\succ0,
\qquad
\mathbb C_{J,Y}^{-}\succ0,                                     \tag{13}
\]

and

\[
\boxed{
\mathfrak C_J(Y)
=\frac{\det\mathbb C_{J,Y}}
       {\det\mathbb C_{J,Y}^{-}}>0.}                            \tag{14}
\]

#### Proof

Suppose \(\mathcal J_u(q,q)=0\) for
\(q\in V_M\oplus\mathcal R_J\). Positivity of \(K(x)K(x-u)\) gives
\(q(x)=q(x-u)\) on the real axis. Real analyticity makes \(q\)
\(u\)-periodic.

Every zero-mode component in \(V_M\) decays at \(+\infty\). Every
nonzero finite radical component has a leading nonconstant polynomial in
\(e^{2x}\), supplied by the largest radical index. Their sum cannot be a
nonzero periodic function. Hence \(q=0\), so every one-displacement Gram
\(\mathbb G_n\) is positive definite on the finite space.

All \(w_n\) are positive. A nonempty sum in (12) is therefore positive
definite; adding \(\mathbb A_-\succeq0\) preserves strict positivity.
The principal block is also positive definite. Minimizing the quadratic
form of \(\mathbb C_{J,Y}\) over its first \(M-1+J\) coordinates gives
its last Schur complement. This is precisely (1), and the Schur
determinant identity gives (14). \(\square\)

The matrix \(\mathbb A_-\) is essential. Omitting it gives the joint
local determinant of 106.90, which is a valid lower bound but does not
generally exhaust the adaptive gain.

## 3. Monotone exhaustion

### Theorem 2 — Cofinal convergence

\[
\boxed{\mathfrak C_J(Y)\nearrow G_J\qquad(Y\to\infty).}          \tag{15}
\]

For every proper finite cutoff,

\[
\boxed{\mathfrak C_J(Y)<G_J.}                                   \tag{16}
\]

#### Proof

The objective in (1) increases pointwise with \(Y\). Hence its infimum
is nondecreasing and bounded above by (8). Write its limit as
\(L\le G_J\).

Fix \(Y_0\) containing at least one omitted prime power. By Theorem 1,
the objective \(F_{Y_0}(d,r)\) is a coercive positive quadratic
polynomial in the finite-dimensional variable \((d,r)\). If
\((d_Y,r_Y)\) minimizes \(F_Y\), then

\[
F_{Y_0}(d_Y,r_Y)
\le\mathfrak C_J(Y)\le G_J.                                    \tag{17}
\]

Thus the minimizers lie in a fixed compact set. Pass to a convergent
subsequence, with limit \((d_*,r_*)\). For every fixed \(Z\ge Y_0\),

\[
F_Z(d_Y,r_Y)\le F_Y(d_Y,r_Y)=\mathfrak C_J(Y)
\qquad(Y\ge Z).                                                  \tag{18}
\]

Taking the subsequential limit and then using monotone convergence of
the nonnegative ordinary-prime-power series gives

\[
F_\infty(d_*,r_*)\le L.                                         \tag{19}
\]

By (8), \(G_J\le F_\infty(d_*,r_*)\). Therefore
\(G_J\le L\le G_J\), proving (15).

For strictness, let \((d_\infty,r_\infty)\) minimize (8). The affine
vector

\[
q_\infty=q_J^*+d_\infty+r_\infty                               \tag{20}
\]

is nonzero because its \(\phi_M\)-coefficient is one. The injectivity
argument in Theorem 1 gives
\(\mathcal J_{u_n}(q_\infty,q_\infty)>0\) for every omitted prime
power. Hence a proper finite cutoff omits a strictly positive tail and

\[
\mathfrak C_J(Y)
\le F_Y(d_\infty,r_\infty)
<F_\infty(d_\infty,r_\infty)=G_J.                              \tag{21}
\]

This proves (16). \(\square\)

## 4. Exact source--capture identity

For any lower certificate \(C\le G_J\), define

\[
\mathfrak L(C)=G_J-C\ge0.                                       \tag{22}
\]

Combining this definition with (9) gives

\[
\boxed{
C-\delta_J=\sigma_\infty-\mathfrak L(C).}                       \tag{23}
\]

For the separate local sum of 106.90,

\[
C=S_{M,J,X}^{\mathrm{loc}},
\qquad
\mathfrak L(C)=G_J-S_{M,J,X}^{\mathrm{loc}}.                    \tag{24}
\]

Thus

\[
S_{M,J,X}^{\mathrm{loc}}>\delta_J
\quad\Longleftrightarrow\quad
\sigma_\infty>
G_J-S_{M,J,X}^{\mathrm{loc}}.                                  \tag{25}
\]

The right side asks the completed margin to pay the atomwise localization
and incompatible-minimizer loss. The source equation does not supply that
payment.

For the augmented determinant, put

\[
\mathfrak L_J(Y)=G_J-\mathfrak C_J(Y).                          \tag{26}
\]

Theorem 2 gives \(\mathfrak L_J(Y)\downarrow0\), and (23) becomes

\[
\boxed{
\mathfrak C_J(Y)-\delta_J
=\sigma_\infty-\mathfrak L_J(Y).}                              \tag{27}
\]

This proves (3). If \(\sigma_\infty>0\), a sufficiently large finite
\(Y\) makes \(\mathfrak L_J(Y)<\sigma_\infty\). Conversely, any finite
crossing implies \(G_J>\delta_J\), hence \(\sigma_\infty>0\). If
\(\sigma_\infty=0\), every proper finite augmented determinant remains
strictly below \(\delta_J\) and converges to it.

This last equality case is the sharp saturation obstruction: positivity,
discreteness, and strict detection by every individual ordinary-prime
atom do not by themselves produce a strict crossing.

## 5. Quantitative theta remainder

There are constants \(C,c>0\) and a fixed polynomial \(Q\), depending
on the finite spaces and on \(X\) but not on \(Y\), such that

\[
\boxed{
0\le G_J-\mathfrak C_J(Y)
\le C Q(Y)e^{-cY}.}                                              \tag{28}
\]

#### Proof

The coercivity estimate (17) bounds all finite minimizers in one compact
coordinate set. On the fixed finite space
\(V_M\oplus\mathcal R_J\), the established theta-overlap estimate gives

\[
\left\|
\sum_{n>Y}w_n\mathbb G_n
\right\|\le C_0Q(Y)e^{-cY}.                                    \tag{29}
\]

Evaluate the complete objective at a minimizer \((d_Y,r_Y)\) of the
finite objective. Then

\[
\begin{aligned}
G_J
&\le\mathfrak C_J(Y)\\
&\quad+\sum_{n>Y}w_n
\mathcal J_{u_n}(q_J^*+d_Y+r_Y,q_J^*+d_Y+r_Y).
\end{aligned}                                                    \tag{30}
\]

The uniform coordinate bound and (29) bound the last line by the
right side of (28). Monotonicity gives the lower bound. \(\square\)

Therefore a known positive completed margin satisfying

\[
\sigma_\infty>C Q(Y)e^{-cY}                                    \tag{31}
\]

would force the explicit determinant at \(Y\) to cross. This is a
cutoff rule after the sign is known, not a proof of the sign.

## 6. Elimination of the deficit symbol

Let \(\widetilde q_J^*\) be the joint old-mode/radical saddle residual
of 106.89. The finite source equation gives

\[
\mathcal A_X(\widetilde q_J^*,\widetilde q_J^*)=-\delta_J.       \tag{32}
\]

Using the literal finite-head form,

\[
\boxed{
\begin{aligned}
\delta_J
={}&\frac12\|\widetilde q_J^*\|_{\mu_K}^2
-\mathscr E_\Gamma(\widetilde q_J^*)\\
&-\sum_{p^k\le X}\frac{\log p}{p^{k/2}}
\mathcal J_{k\log p}(\widetilde q_J^*,\widetilde q_J^*).
\end{aligned}}                                                   \tag{33}
\]

Thus the finite determinant target is equivalently

\[
\boxed{
\begin{aligned}
\frac{\det\mathbb C_{J,Y}}
     {\det\mathbb C_{J,Y}^{-}}
&+\mathscr E_\Gamma(\widetilde q_J^*)\\
&+\sum_{p^k\le X}\frac{\log p}{p^{k/2}}
\mathcal J_{k\log p}(\widetilde q_J^*,\widetilde q_J^*)\\
&>\frac12\|\widetilde q_J^*\|_{\mu_K}^2.
\end{aligned}}                                                   \tag{34}
\]

Equation (34) is a completely finite compensated inequality. It keeps
Gamma, the threshold, every retained ordinary prime power, the finite
radical correction, old-mode adaptation, and one finite omitted
ordinary-prime block.

The source identity (33) evaluates \(\delta_J\) exactly, but it gives no
comparison with the determinant. Indeed, 106.87, Lemma 4 shows that the
source direction and all observation responses stay fixed when the new
diagonal source coordinate is varied, while the deficit varies freely.
The physical relation (33), not source algebra alone, is indispensable.

## 7. Determinant, inertia, and total-positivity audit

The augmented determinant does not acquire a sign merely because its
prime-power increments are positive.

### Proposition 3 — Exact physical-observation saturation model

Fix any nonzero even analytic decaying vector \(q\) for which the literal
theta displacement forms are finite, and put

\[
a_n=\frac{\Lambda(n)}{\sqrt n}\,
\mathcal J_{\log n}(q,q)>0,\qquad n=p^k>X.                        \tag{35}
\]

Then

\[
0<S:=\sum_{n>X}a_n<\infty.                                     \tag{36}
\]

On the one-dimensional row with no old mode and no radical coordinate,
choose the source pivot to be \(-\delta=-S\). Then

\[
\mathfrak C(Y)=\sum_{\substack{n=p^k\\X<n\le Y}}a_n<S=\delta
\quad\text{for every finite }Y,                                \tag{37}
\]

while

\[
\mathfrak C(Y)\nearrow\delta,\qquad \sigma_\infty=0.            \tag{38}
\]

#### Proof

One-displacement injectivity gives \(a_n>0\), and theta overlap gives
(36). In one dimension the augmented Schur determinant ratio is the
partial sum in (37). Every proper partial sum is strictly smaller than
the positive complete sum. The completed source balance (9) then gives
(38). \(\square\)

This model uses the actual \(K\), the actual translation lengths
\(\log p^k\), and the ordinary coefficients
\(\Lambda(p^k)=\log p\). It does not impose the physical Gamma diagonal:
that diagonal was deliberately chosen through the free scalar source
coordinate. Therefore it is not a counterexample to the Riemann
inequality. It is a sharp falsifier of any argument using only

* the source normal equation;
* positivity of the literal ordinary-prime increments;
* determinant monotonicity or inertia; and
* theta summability.

The full physical identity (33) is exactly the additional datum that such
an argument would have to exploit.

Total positivity does not repair the problem. The required signed family
contains the Gamma/threshold block, and 106.42 already shows that the
Gamma kernel is not TP2. On the arithmetic side, 104.21 gives a literal
prime-tower PF2 failure, while 106.60 shows that the most direct polarized
\(j_2\) lift is indefinite already on \(\{p,p^2\}\). Thus no previously
established total-positivity structure applies to the matrix path
\(\mathbb C_{J,Y}\).

Finally, a contradiction from permanent non-crossing is exactly the
completed sign:

\[
\boxed{
\mathfrak C_J(Y)\le\delta_J\ \text{for every finite }Y
\quad\Longleftrightarrow\quad
\sigma_\infty\le0.}                                               \tag{39}
\]

The forward implication follows by taking \(Y\to\infty\) in (15); the
reverse follows from
\(\mathfrak C_J(Y)<G_J=\delta_J+\sigma_\infty\).
Accordingly, inertia cannot turn non-crossing into a contradiction
without an additional theorem excluding the nonpositive completed
pivot. In the mean-periodic coordinate, 106.64 identifies precisely that
additional theorem as exclusion of the negative Krein evaluation
channel.

## 8. Ledger conclusion

The local Christoffel sum of 106.90 is a rigorous positive certificate,
but (23) proves that its comparison with the deficit contains the
completed sign plus a nonnegative localization loss.

The augmented determinant (12) removes that avoidable loss and converges
monotonically to the exact radical-conditioned gain. Its finite crossing
criterion (14), equivalently (34), is necessary and sufficient in the
cofinal sense. What remains unproved is that one such determinant has the
required strict sign on every relevant physical row. The present theorem
does not prove that arithmetic inequality and therefore does not close
the Riemann hypothesis.
