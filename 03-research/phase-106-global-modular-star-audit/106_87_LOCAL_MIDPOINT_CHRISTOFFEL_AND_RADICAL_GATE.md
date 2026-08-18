# 106.87 — Local midpoint Christoffel bounds and the radical gate

## Purpose and conclusion

The stable finite-head transitions suggest that the adaptive negative
residual is detected near the midpoint of the first omitted literal
prime-power atom.  This note determines exactly what can be proved from
that localization picture.

Let

\[
 V_{M-1}\subset V_M
 =\operatorname {span}\{\phi_1,\ldots,\phi_M\}     \tag{1}
\]

be a finite elementary even zero-mode space, including any prescribed
confluent jets.  For every displacement \(u>0\) and every aperture radius
\(W>0\), the midpoint-restricted literal feature is injective on \(V_M\).
Consequently every affine residual

\[
 q^*=\phi_M+v,\qquad v\in V_{M-1},                \tag{2}
\]

obeys the exact local Christoffel bound

\[
 \boxed{
 \mathcal J_{u,W}(q^*)\ge
 \kappa_M(u,W)
 =\frac{\det G_M(u,W)}{\det G_{M-1}(u,W)}>0.}      \tag{3}
\]

For the first omitted atom \(n=p^k\), \(u=\log n\), this gives the rigorous
Kalman lower bound

\[
 \boxed{
 \Delta_n\ge
 \frac{\Lambda(n)}{\sqrt n}\,\kappa_M(\log n,W).} \tag{4}
\]

Thus the observed midpoint detection has an exact finite-dimensional
theorem behind it.  The theorem does not, however, compare (4) with the
negative Schur deficit \(\delta=-\sigma_0\).

There is an exact counterexample inside the literal Riemann
\(K\)-displacement geometry.  If \(r\ne0\) belongs to the completed
radical, then every proper finite head has the adaptive one-dimensional
pivot

\[
 \sigma_X=-\mathcal T_X(r,r)<0,                  \tag{5}
\]

while every proper finite block of omitted atoms gains strictly less than
\(\mathcal T_X(r,r)\).  It never crosses.  As the head moves out, the
midpoint of the first omitted atom tends to infinity and the local spatial
mass of the fixed vector \(r\) there tends to zero.

This counterexample is removed by the radical anti-short and therefore
does not refute a theorem on the completed complement.  It proves that
106.47 tail localization, 106.74 one-atom carrier coercivity, the adaptive
source equation, and a Christoffel bound do not by themselves produce the
needed comparison.  A valid closure theorem must quantitatively use the
condition \(q^*\in\mathcal R^\perp\), or the equivalent maximal radical
anti-short, before comparing the first omitted gain with \(\delta\).

## 1. The midpoint-restricted literal feature

Put

\[
 t=\frac u2,\qquad
 a_u(y)=K(t+y)K(t-y)>0.                           \tag{6}
\]

For \(W>0\), define

\[
 \boxed{
 \mathcal J_{u,W}(q,s)
 :=\int_{-W}^{W}a_u(y)
 \{q(t+y)-q(t-y)\}
 \overline{\{s(t+y)-s(t-y)\}}\,dy.}              \tag{7}
\]

The evenness of \(q\) turns the literal displacement difference at
\(x=t+y\) into the difference in (7):

\[
 q(x)-q(x-u)=q(t+y)-q(y-t)=q(t+y)-q(t-y).        \tag{8}
\]

Therefore

\[
 0\le\mathcal J_{u,W}(q,q)\le\mathcal J_u(q,q).  \tag{9}
\]

### Lemma 1 — Local midpoint injectivity

For every \(u,W>0\),

\[
 \boxed{
 q\in V_M,\quad \mathcal J_{u,W}(q,q)=0
 \quad\Longrightarrow\quad q=0.}                 \tag{10}
\]

#### Proof

Strict positivity of \(a_u\) and (7) give

\[
 q(t+y)=q(t-y)                                    \tag{11}
\]

for almost every \(y\in(-W,W)\).  Every vector in \(V_M\) is real
analytic on the real axis, so (11) holds first throughout that interval
and then, by analytic continuation, for every real \(y\).  Thus \(q\) is
invariant under reflection about \(t\).  It is also even, hence invariant
under reflection about \(0\).  The composition of these two reflections
is translation by \(2t=u\), so

\[
 q(x+u)=q(x)                                      \tag{12}
\]

for every real \(x\).

Every elementary mode and every finite jet in the open strip has a
polynomial times exponentially decaying envelope.  Hence \(q(x)\to0\) as
\(x\to+\infty\).  Iterating (12) gives

\[
 q(x)=q(x+ju)\longrightarrow0,
\]

so \(q=0\).  \(\square\)

This argument is local: any nonempty open midpoint aperture already sees
the whole finite analytic mode space.

## 2. The local Christoffel determinant

Let

\[
 G_M(u,W)
 =\bigl[\mathcal J_{u,W}(\phi_i,\phi_j)\bigr]_{i,j\le M}.
                                                               \tag{13}
\]

Lemma 1 gives

\[
 G_M(u,W)\succ0,\qquad G_{M-1}(u,W)\succ0.        \tag{14}
\]

Write

\[
 G_M(u,W)=
 \begin{pmatrix}
 G_{M-1}&g\\g^*&h
 \end{pmatrix}.                                  \tag{15}
\]

### Theorem 2 — Affine midpoint Christoffel bound

For every \(q=\phi_M+\sum_{j<M}c_j\phi_j\),

\[
 \boxed{
 \mathcal J_{u,W}(q,q)
 \ge h-g^*G_{M-1}^{-1}g
 =\frac{\det G_M(u,W)}{\det G_{M-1}(u,W)}
 =:\kappa_M(u,W)>0.}                             \tag{16}
\]

#### Proof

Expanding (15) gives

\[
 \mathcal J_{u,W}(q,q)
 =c^*G_{M-1}c+2\operatorname {Re}(c^*g)+h.
                                                               \tag{17}
\]

Its minimum over \(c\in\mathbb C^{M-1}\) is attained at
\(c=-G_{M-1}^{-1}g\) and equals the Schur complement in (16).
The determinant identity is the block determinant formula, and strict
positivity follows from (14).  \(\square\)

The number \(\kappa_M(u,W)\) is the local aperture analogue of a
Christoffel function.  It is finite and computable by interval quadrature
for a specified mode block.  It is invariant under changes of the old
basis and scales in the expected way when the new mode is rescaled.

### Corollary 3 — First omitted atom gain

Let \(A\succ0\) be the preceding signed block, let \(q^*\) be its adaptive
residual, and let \(n=p^k\) be the first omitted prime power.  Set

\[
 w_n=\frac{\Lambda(n)}{\sqrt n},\qquad u_n=\log n. \tag{18}
\]

Then the exact one-atom Kalman gain satisfies (4).

#### Proof

The variational form of the update is

\[
 \Delta_n
 =\min_{v\in V_{M-1}}
 \{\mathcal A_0(v,v)+w_n\mathcal J_{u_n}(q^*+v)\}. \tag{19}
\]

In coefficient coordinates the first term is nonnegative because
\(A\succ0\).  Restricting the literal integral to \(|y|\le W\), dropping
that first term, and then minimizing over the larger affine class gives

\[
\begin{aligned}
 \Delta_n
 &\ge w_n\min_{v\in V_{M-1}}
       \mathcal J_{u_n,W}(q^*+v)\\
 &=w_n\kappa_M(u_n,W).
\end{aligned}                                    \tag{20}
\]

The last equality uses the fact that \(q^*\) has coefficient one on
\(\phi_M\).  \(\square\)

Equation (20) proves spatial detection at the exact midpoint of the first
omitted atom.  It is the localized version of the pure conditional
distance in 106.80.  As the diagnostics there show, it can be much smaller
than the full augmented gain because it discards the component whose
regression is priced by \(A\).

## 3. Why the adaptive source equation does not set the scale

The adaptive equation is

\[
 H_0x_*=-\delta e_M,\qquad
 x_*=\binom{-A^{-1}c}{1}.                        \tag{21}
\]

It selects one direction, but its algebra alone does not relate that
direction's observation energy to \(\delta\).  This can be seen before
using any asymptotics.

### Lemma 4 — The source algebra has a free deficit coordinate

Fix \(A\succ0\), \(c\), and any literal observation block \(S=[\,U\ v\,]\).
For

\[
 H(h)=\begin{pmatrix}A&c\\c^*&h\end{pmatrix},    \tag{22}
\]

the adaptive vector \(x_*=(-A^{-1}c,1)^T\) and its observation
\(Sx_*=v-UA^{-1}c\) are independent of \(h\), whereas

\[
 \delta(h)=c^*A^{-1}c-h                           \tag{23}
\]

can be increased arbitrarily by decreasing \(h\).

#### Proof

All assertions follow directly from multiplication of (22) by \(x_*\).
\(\square\)

Lemma 4 is an algebraic falsifier, not a modification of the physical
Riemann form.  Its role is precise: no estimate comparing (20) with
\(\delta\) can follow from the source equation and observation geometry
alone.  The physical relation tying \(h\) to Gamma, the threshold, the
ordinary primes, and the radical quotient must be used.

## 4. Exact literal counterexample from the completed radical

Let \(0\ne r\in\mathcal R_J\) be a finite completed radical vector.  The
complete identity is

\[
 \mathcal A_\infty(r,r)=0.                       \tag{24}
\]

For a finite prime-power head \(X\), write

\[
 \mathcal T_X(r,r)
 =\sum_{p^k>X}\frac{\log p}{p^{k/2}}
   \mathcal J_{k\log p}(r,r).                    \tag{25}
\]

Since
\(\mathcal A_X=\mathcal A_\infty-\mathcal T_X\),

\[
 \boxed{
 \mathcal A_X(r,r)=-\mathcal T_X(r,r)<0.}         \tag{26}
\]

Take the one-dimensional ordered space \(V_1=\operatorname {span}\{r\}\).
After fixing the scale of its basis vector, the adaptive residual is
literally \(q^*=r\), and its Schur deficit is

\[
 \delta_X=\mathcal T_X(r,r).                     \tag{27}
\]

### Theorem 5 — No proper omitted block crosses a radical pivot

For every finite nonempty set

\[
 \mathcal B\subset\{p^k:p^k>X\},
\]

the exact gain is

\[
 \Delta_{\mathcal B}
 =\sum_{n\in\mathcal B}\frac{\Lambda(n)}{\sqrt n}
   \mathcal J_{\log n}(r,r)
 <\delta_X.                                      \tag{28}
\]

In particular, the first omitted atom has strictly positive gain but
cannot cross the pivot.

#### Proof

There are no old coordinates in the one-dimensional problem, so the
Kalman gain is exactly the sum in (28).  Every summand in (25) is strictly
positive.  Indeed, vanishing of one displacement energy would make \(r\)
\(\log n\)-periodic, whereas a nonzero finite radical combination has the
nonperiodic theta asymptotic used in 106.75.  Since \(\mathcal B\) is
finite, at least one strictly positive omitted term remains.  Subtracting
that remainder from (25) proves (28).  \(\square\)

This counterexample uses the actual Riemann theta kernel, the literal
weights \(\Lambda(n)/\sqrt n\), the exact displacement atoms, and the
adaptive Schur update.  It is not a generic graph model.

There is also no uniform moving-midpoint mass consequence.  Let \(n_X\)
be the first prime power above \(X\).  Then
\(\tfrac12\log n_X\to\infty\).  Since \(r\in L^2(\mu_K)\), for every
fixed \(W>0\),

\[
 \int_{\left|x-\frac12\log n_X\right|\le W}
 |r(x)|^2\,d\mu_K(x)\longrightarrow0.            \tag{29}
\]

Moreover,

\[
 \frac{\Lambda(n_X)}{\sqrt {n_X}}
 \mathcal J_{\log n_X}(r,r)
 \le\mathcal T_X(r,r)\longrightarrow0.           \tag{30}
\]

Thus negative finite pivots can coexist with midpoint mass and midpoint
gain tending to zero.

## 5. Relation to the tail floor and the carrier floor

The counterexample clarifies the roles of 106.47 and 106.74.

1. The tail-floor theorem of 106.47 is a statement about the **completed**
   operator.  It makes any completed eigenstate below \(1/2\) spatially
   localized and turns such spectrum into isolated bound states.  It does
   not say that a negative vector of a proper finite head must follow the
   midpoint of its first omitted atom.  On the radical, the missing tail
   is exactly what creates the finite negative pivot.
2. The one-atom carrier theorem of 106.74 gives a strictly positive floor
   on every fixed finite translated carrier cluster.  In (28), every atom
   is indeed strictly positive.  Positivity is insufficient because the
   deficit is the sum of that atom and all later positive atoms.
3. If a completed subthreshold state existed in
   \(\mathcal R^\perp\), 106.47 would make it centrally localized.  Every
   finite head would remain negative, and even the complete omitted tail
   would leave its fixed subthreshold deficit.  Consequently central
   localization is compatible with the obstruction; excluding the state
   is the sign theorem itself.

The logical distinction is therefore

\[
 \text{local midpoint observability}
 \quad\ne\quad
 \text{gain larger than the signed deficit}.     \tag{31}
\]

The first statement is Theorem 2.  The second must use the completed
complement quantitatively.

## 6. Diagnostic Shannon alignment

The stable numerical transitions have a simple time--frequency alignment.
For the \(M\)-th critical-line ordinate \(\gamma_M\) and a prime-power
displacement \(u=\log n\), define the Shannon count

\[
 \mathsf S(M,n)=\frac{\gamma_M\log n}{2\pi}.      \tag{32}
\]

Using the ordinates in "06-grafico/zeros_10000.txt" gives

\[
\begin{array}{c|c|c|c|c}
M&n&\gamma_M&\mathsf S(M,n)&\mathsf S(M,n)/M\\ \hline
4&2&30.424876126&3.356405&0.839101\\
7&3&40.918719012&7.154621&1.022089\\
12&4&56.446247697&12.454052&1.037838\\
16&5&67.079810529&17.182493&1.073906
\end{array}                                      \tag{33}
\]

Equivalently, solving \(\mathsf S(M,n_*(M))=M\) gives

\[
 n_*(M)=\exp\!\left(\frac{2\pi M}{\gamma_M}\right), \tag{34}
\]

whose values for the four rows are

\[
 2.2843,\qquad2.9296,\qquad3.8029,\qquad4.4758.  \tag{35}
\]

The Riemann--von Mangoldt main term predicts

\[
 n_*(M)\sim\frac{\gamma_M}{2\pi e}.               \tag{36}
\]

Equations (32)--(36) are a diagnostic, not a theorem about the staircase
frontier.  They suggest that the first successful atom appears when its
logarithmic displacement has approximately one Shannon degree of freedom
per admitted zero mode.  They do not prove a Christoffel lower bound or
compare it with \(\delta\).

## 7. Surviving target

Theorem 2 supplies the strongest general midpoint statement implied by
finite analyticity and the coefficient flag.  Theorem 5 proves why it
cannot be promoted to a deficit comparison without excluding the
threshold radical.

A viable next theorem must have the form

\[
 \boxed{
 q^*\in\mathcal R^\perp,\quad
 \mathcal A_X(q^*,q^*)=-\delta<0
 \quad\Longrightarrow\quad
 \Delta_{\mathcal B}>\delta}                     \tag{37}
\]

for a finite block selected at the Shannon scale, with all radical
cross-terms shorted before the comparison.  Equivalently, it must prove a
positive lower bound for the completed complement innovation.  Neither
the local determinant \(\kappa_M(u,W)\), the source equation, nor the
tail-floor theorem gives that bound separately.
