# D.110 — Stratified residuation and the polar Frobenius Lefschetz operator

## Status

The ordered-frame depth map of D.109 can be replaced by a map genuinely
induced from the functional periodic section moduli.  The literal inclusion
of special modules is lifted by the canonical residuation coefficients.
On each differentiability stratum this gives a replication Jacobian
\(R_{N,M}\).  Its polar part

\[
 V_{N,M}=R_{N,M}(R_{N,M}^*R_{N,M})^{-1/2}
\]

is the unique metric isometry with the same range, and \(V_{N,M}^*\) is its
actual periodic adjoint.

On the canonical neutral-point chamber used to prove the dimension theorem,
the Jacobian and its polar part are explicit.  Iterating the adjacent
Frobenius polar maps gives, in the cofinal depth limit,

\[
 \langle V_{t+r,t+s}u_{t+r},u_{t+s}\rangle
 \longrightarrow p^{-|r-s|/2}.
\]

Thus the Jacobi/Szegő Green kernel of every prime-power orbit is induced by
residuation plus the row-A ordered-frame metric, not by an arbitrary
identification of labels.  This supplies a rigorous periodic
raising/lowering pair and is compatible with Künneth.

The archimedean quarter-shift oscillator can be adjoined as the real
boundary summand.  The resulting Krein pullback is exactly \(B_{\rm nuc}\)
with all \(p^k\) and Gamma.  The local Green operators, however, are not
ordered relative to the identity: their Poisson symbols cross one.  Hence
no local interlacing theorem proves the primitive global inequality.  The
remaining sharp Dirichlet comparison is exactly row D and is identified
explicitly below; it is not silently assumed.

No zero of zeta and no sign of \(B_{\rm nuc}\) is used.  The paper is not
modified.

## 1. The canonical stratified residuation lift

Write

\[
 P_{N,p}=\mathbb R^{N-p+1},\qquad
 \sigma_N(c)=\max_{0\leq i\leq N-p}(\phi_i^{(N)}+c_i). \tag{1.1}
\]

On the regular locus, every extremal is uniquely active somewhere and
residuation is inverse to \(\sigma_N\).  For \(N<M\), the defining boundary
inequality gives a literal inclusion of functional modules

\[
 \iota_{N,M}:\mathcal E_{N,p}\hookrightarrow\mathcal E_{M,p}.       \tag{1.2}
\]

Although \(\iota_{N,M}(\mathcal E_{N,p}^{\rm reg})\) lies on a lower
stratum of \(\mathcal E_{M,p}\), it has the canonical maximal coefficient
lift

\[
 \mathcal R_{N,M}(c)_j
 =\gamma_j^{(M)}(\sigma_N(c))
 =\inf_{x\in[1,p]}
   \bigl(\sigma_N(c)(x)-\phi_j^{(M)}(x)\bigr).          \tag{1.3}
\]

The reconstruction theorem for residuation proves

\[
 \sigma_M\mathcal R_{N,M}=\iota_{N,M}\sigma_N.         \tag{1.4}
\]

It also proves functoriality.  If \(N<M<L\), then both sides below are the
maximal \(L\)-coefficients of the same function:

\[
 \mathcal R_{M,L}\mathcal R_{N,M}=\mathcal R_{N,L}.     \tag{1.5}
\]

Each coordinate in (1.3) is a finite infimum envelope of max-affine
functions.  Therefore \(\mathcal R_{N,M}\) is continuous, one-Lipschitz in
the sup norm and piecewise affine.  On a stratum where the minimizing point
and the uniquely active old extremal are fixed, its Jacobian has the form

\[
 (R_{N,M})_{ji}=\begin{cases}
 1,&i=i(j),\\0,&i\ne i(j).
 \end{cases}                                             \tag{1.6}
\]

Thus every new coefficient is functorially pulled from an old active
coefficient.  This is the cotangent correspondence produced by the actual
section functor.

## 2. The neutral-point chamber

The dimension proof for \(\mathcal E_{N,p}\) uses the distinguished chamber
in which all extremals become active, in their slope order, in a common
right neighbourhood of the neutral point \(x=1\).  In that chamber the
coefficients satisfy the strict cumulative inequalities of the
Connes--Consani simplex.

For \(j\leq N-p\), the old and new extremals have the same left branch
\(-j(x-1)\).  Its activity witness therefore gives

\[
 \gamma_j^{(M)}(\sigma_N(c))=c_j.                       \tag{2.1}
\]

For \(j>N-p\), the new extremal has value zero at \(x=1\); the final old
extremal is uniquely active there and gives

\[
 \gamma_j^{(M)}(\sigma_N(c))=c_{N-p}.                   \tag{2.2}
\]

Put \(d=N-p+1\), \(D=M-p+1\), and \(m=D-d+1\).  Equations
(2.1)--(2.2) give the constant Jacobian

\[
 R_{N,M}e_i=\begin{cases}
 e_i,&0\leq i<d-1,\\
 \displaystyle\sum_{j=d-1}^{D-1}e_j,&i=d-1.
 \end{cases}                                             \tag{2.3}
\]

Consequently

\[
 R_{N,M}^*R_{N,M}=\mathrm{diag}(1,\ldots,1,m).    \tag{2.4}
\]

This calculation also shows why the zero-extension used provisionally in
D.109 was not the metric adjoint of residuation: the last coefficient is
replicated into all new boundary extremals.

## 3. Polar raising and lowering

Equip the coefficient cotangents with the row-A ordered-frame Euclidean
metric.  Since \(R_{N,M}\) is injective on the chamber, its polar part is

\[
 V_{N,M}=R_{N,M}(R_{N,M}^*R_{N,M})^{-1/2}.             \tag{3.1}
\]

It is characterized without a choice by

\[
 V_{N,M}^*V_{N,M}=I,qquad
 \mathrm{Ran}\,V_{N,M}=\mathrm{Ran}\,R_{N,M}.  \tag{3.2}
\]

Explicitly,

\[
 V_{N,M}e_i=\begin{cases}
 e_i,&i<d-1,\\
 m^{-1/2}\displaystyle\sum_{j=d-1}^{D-1}e_j,&i=d-1.
 \end{cases}                                             \tag{3.3}
\]

Define the periodic Lefschetz raising and lowering maps at adjacent
Frobenius depths by

\[
 L_r=V_{ap^r,ap^{r+1}},\qquad
 \Lambda_r=L_r^*.                                       \tag{3.4}
\]

Then \(\Lambda_rL_r=I\).  These are genuine adjoints for the periodic
metric.  For several depth steps use the functorial iteration

\[
 L_{r,s}=L_{s-1}\cdots L_r,qquad
 \Lambda_{s,r}=L_{r,s}^*.                               \tag{3.5}
\]

The polar part of a composite need not equal the composite of the polar
parts, so (3.5), rather than a false multiplicativity assertion for polar
decomposition, is the defined Frobenius-depth dynamics.

## 4. Cofinal Green kernel from the actual correspondence

Let

\[
 u_r=d_r^{-1/2}\sum_{i<d_r}e_i,qquad
 d_r=ap^r-p+1.                                          \tag{4.1}
\]

For one step, (3.3) gives

\[
 \langle L_ru_r,u_{r+1}\rangle
 ={d_r-1+\sqrt{m_r}\over\sqrt{d_rd_{r+1}}},qquad
 m_r=d_{r+1}-d_r+1.                                     \tag{4.2}
\]

Since \(d_{r+1}/d_r\to p\) and \(m_r=O(d_r)\),

\[
 \langle L_ru_r,u_{r+1}\rangle\longrightarrow p^{-1/2}. \tag{4.3}
\]

For a fixed number \(k\) of steps, the image of the first \(d_r-1\)
basis vectors remains unchanged.  Only the final vector is successively
spread over the new tails.  Its coordinate \(\ell^1\)-norm is
\(O(d_r^{1/2})\) for fixed \(k\).  Hence

\[
 \sum_i(L_{r,r+k}\sum_{j<d_r}e_j)_i=d_r+O(d_r^{1/2}).   \tag{4.4}
\]

Dividing by \(\sqrt{d_rd_{r+k}}\) proves

\[
 \boxed{
 \lim_{t\to\infty}
 \langle L_{t+r,t+s}u_{t+r},u_{t+s}\rangle
 =p^{-|r-s|/2}.}                                        \tag{4.5}
\]

Thus D.109's Jacobi Green kernel is induced by the stratified functional
correspondence and its metric polar normalization.  No label-only
zero-extension remains in (4.5).

For two factors, the residuation Jacobian is \(R_p\otimes R_q\).  Polar
decomposition respects tensor products of injective maps:

\[
 V_{R_p\otimes R_q}=V_{R_p}\otimes V_{R_q}.             \tag{4.6}
\]

Therefore the raising, lowering and Green kernels obey the row-A Künneth
rule.

## 5. Prime and Gamma assembly

The stationary cyclic representation of (4.5) is the Szegő vector

\[
 h_p(z)={\sqrt{1-p^{-1}}\over1-p^{-1/2}z},qquad
 \langle S^rh_p,S^sh_p\rangle=p^{-|r-s|/2}.             \tag{5.1}
\]

Together with the reduced contact length \(\log p\), it yields all
coefficients \(\Lambda(p^k)/p^{k/2}\).  On the logarithmic test
representation it gives

\[
 A_p=\sqrt{1-p^{-1}}(I-p^{-1/2}U_p)^{-1}.              \tag{5.2}
\]

Adjoin the independent real boundary module

\[
 A_\infty e_j=(j+\tfrac14)e_j,qquad
 \|\partial_\infty F\|^2
 =\int_0^\infty{e^{-r/2}\over1-e^{-2r}}
   \|F-S_rF\|^2,dr.                                    \tag{5.3}
\]

The exact assembled form is

\[
\begin{aligned}
 B_{\rm geom}(F,G)={}&
 \sum_p\log p\bigl(\langle A_pF,A_pG\rangle
                    -\langle F,G\rangle\bigr)\\
 &+m_0\langle F,G\rangle
   -\langle\partial_\infty F,\partial_\infty G\rangle,
 \qquad m_0=\log\pi-\psi(1/4).                         \tag{5.4}
\end{aligned}
\]

The periodic construction proves the finite Green factors in (5.4); the
oscillator heat trace proves the real factor.  Expansion and polarization
give

\[
 \boxed{B_{\rm geom}=B_{\rm nuc}}                       \tag{5.5}
\]

with every prime power and Gamma.

## 6. The interlacing/Dirichlet test

The positive Jacobi inverse by itself has no order relative to the
identity.  If \(\rho=p^{-1/2}\), its bilateral symbol is

\[
 P_\rho(e^{i\theta})
 ={1-\rho^2\over1-2\rho\cos\theta+\rho^2}.             \tag{6.1}
\]

At the two endpoints,

\[
 P_\rho(1)-1={2\rho\over1-\rho}>0,qquad
 P_\rho(-1)-1={-2\rho\over1+\rho}<0.                  \tag{6.2}
\]

Thus \(A_p^*A_p-I\) is indefinite at every prime.  There is no local
Dirichlet interlacing of a fixed sign to sum over the primes.

The exact global primitive claim is the sharp estimate

\[
 \sum_p\log p\,\|F\|^2+\|\partial_\infty F\|^2
 \ \geq\
 \sum_p\log p\,\|A_pF\|^2+m_0\|F\|^2                 \tag{6.3}
\]

for

\[
 M_-(F)=M_+(F)=0,                                      \tag{6.4}
\]

under the stabilized paired interpretation.  By (5.4), (6.3) is exactly

\[
 B_{\rm nuc}(F,F)\leq0.                                \tag{6.5}
\]

Hence any global interlacing theorem proving (6.3) would close row D, but
checking (6.3) from the already assembled operator is not a separate
argument.  The local polar/residuation construction proves the operator
identity and its adjointness; it does not prove the sharp comparison.

## 7. Outcome

The requested geometric comparison is now exact up to the genuine Hodge
inequality:

\[
 \begin{array}{c}
 \text{functional module inclusion}\\
 \downarrow\ \text{residuation}\\
 R_r\\
 \downarrow\ \text{metric polar part}\\
 (L_r,\Lambda_r=L_r^*)\\
 \downarrow\ \text{cofinal cyclic Gram}\\
 p^{-|r-s|/2}\\
 \downarrow\ \log p\text{ contact + Gamma oscillator}\\
 B_{\rm nuc}.
 \end{array}
\]

What remains is no longer the construction of the prime-power adjoint or
the Gamma term.  It is the global primitive Dirichlet inequality (6.3).
Any subsequent proof must derive that comparison from an additional
Hodge/duality principle on the completed stratified object, not rename
(6.5) as positivity.

