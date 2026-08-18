# 106.95 — Cauchy--Binet charging audit for the physical minor gate

## Purpose and verdict

Document 106.92 reduces the remaining finite crossing to

\[
 \tau_{d+1}(Y)>\delta_J\tau_d(Y).                 \tag{1}
\]

The most direct proposed proof is to expand both determinants by
Gram--Andreief and charge every polar-threshold \(d\)-minor into an
omitted-prime \((d+1)\)-minor or into a Gamma/retained-prime source
minor, preserving the literal factors \(\Lambda(n)/\sqrt n\).

This note carries that proposal to its exact endpoint.  There are three
conclusions.

1.  Cauchy--Binet introduces no new inequality.  In exterior-power
    coordinates, existence of an abstract contractive charging map is
    equivalent to (1).
2.  A positive endpoint-local charge defined before the radical quotient
    is impossible.  Radical saturation forces such a charge to preserve
    every edge endpoint, while the ordinary-prime source has positive
    singular mass on the prime lines and the polar demand is absolutely
    continuous.  This is the measure-capacity obstruction of 106.65,
    now expressed at the minor level.
3.  The only surviving version is a row-dependent, globally nonlocal
    charge after the complete radical anti-short.  Constructing it with
    norm strictly smaller than one is exactly the source-balanced minor
    inequality, equivalently the negative-channel absorption theorem of
    106.37.  It cannot be obtained from positivity of the minor measures
    alone.

Thus no weight-preserving positive injection closes (1).  The
Riemann-specific statement still missing is a quantitative projected
Pluecker-frame bound for the literal theta translations on the
mean-periodic quotient.

## 1. Semantic audit

The following earlier results are directly relevant.

* Paper 36, H7, uses Andreief/Vandermonde squares for a two-node scalar
  determinant.  Its band closure does not give a uniform all-mode
  estimate.
* 106.65 constructs the full latent theta edge measure and proves that no
  positive conditional expectation can map its gradient to the polar
  gradient while preserving the complete radical equality family.
* 106.76 and 106.80 prove the exact Gram--Andreief formulas and finite
  observability for the literal prime atoms.  They do not compare the
  resulting determinant ratio with the negative pivot.
* 106.89--106.92 put the old-mode adaptation and finite radical correction
  inside one augmented determinant.  The remaining comparison is (1).

Therefore the exterior-power calculation below is an audit of the new
source-balanced comparison, not a new use of Cauchy--Binet.

## 2. Exterior-power form of the two sides

Let \(\mathcal H_{J,Y}\) be the positive observation Hilbert space which
contains the old positive feature \(\widehat A^{1/2}\), the projected
ordinary-prime observations up to \(Y\), and the common radical
correction.  In the ordered affine basis of 106.92, let

\[
 f_1,\ldots,f_d,f_*\in\mathcal H_{J,Y}              \tag{2}
\]

be the nuisance columns and the new residual column.  Put

\[
 a=f_1\wedge\cdots\wedge f_d,
 \qquad v=a\wedge f_*.                               \tag{3}
\]

Then

\[
 \|a\|^2=\tau_d(Y),
 \qquad \|v\|^2=\tau_{d+1}(Y).                     \tag{4}
\]

Introduce a one-dimensional threshold space with unit vector \(e_0\),
and put

\[
 u=\sqrt{\delta_J}\,e_0\otimes a.                  \tag{5}
\]

Thus

\[
 \|u\|^2=\delta_J\tau_d(Y).                        \tag{6}
\]

### Theorem 1 — Abstract charging is exactly the desired inequality

The following are equivalent.

\[
\begin{aligned}
 &\tau_{d+1}(Y)\geq\delta_J\tau_d(Y);              \tag{7a}\\
 &\text{there is a contraction }C:
   \operatorname {span}\{v\}\longrightarrow
   \operatorname {span}\{u\}
   \text{ such that }Cv=u.                         \tag{7b}
\end{aligned}
\]

Moreover, when \(v\ne0\), the smallest possible norm is

\[
 \boxed{\inf_{Cv=u}\|C\|
 =\frac{\|u\|}{\|v\|}
 =\left\{\frac{\delta_J\tau_d(Y)}
                 {\tau_{d+1}(Y)}\right\}^{1/2}.}  \tag{8}
\]

Consequently strict inequality in (1) is equivalent to the existence of
such a charge with \(\|C\|<1\).

#### Proof

If \(C\) is a contraction and \(Cv=u\), then

\[
 \|u\|=\|Cv\|\leq\|v\|,
\]

which is (7a) by (4) and (6).  Conversely, if \(\|u\|\leq\|v\|\), define

\[
 C(\alpha v)=\alpha u.
\]

Its norm is \(\|u\|/\|v\|\leq1\), and it sends \(v\) to \(u\).
The same computation proves (8). \(\square\)

The theorem is deliberately elementary.  It shows that a charging map
defined only after the two exterior vectors have been assembled cannot be
the missing argument: its contractivity is precisely (1).

## 3. What the Andreief expansion does and does not add

Choose a coordinate realization

\[
 \mathcal H_{J,Y}=L^2(\Omega_{J,Y},\nu_{J,Y}).       \tag{9}
\]

Then Gram--Andreief gives

\[
 \tau_{d+1}(Y)
 =\frac1{(d+1)!}\int_{\Omega_{J,Y}^{d+1}}
  |D_{d+1}(\boldsymbol\omega)|^2
  \,d\nu_{J,Y}^{d+1}(\boldsymbol\omega),          \tag{10}
\]

and

\[
 \tau_d(Y)
 =\frac1{d!}\int_{\Omega_{J,Y}^{d}}
  |D_d(\boldsymbol\omega)|^2
  \,d\nu_{J,Y}^{d}(\boldsymbol\omega).            \tag{11}
\]

On ordinary-prime rows the measures in (10)--(11) contain exactly the
products

\[
 \prod_i\frac{\Lambda(n_i)}{\sqrt{n_i}}.           \tag{12}
\]

A weight-preserving injection from configurations in (11) to
configurations in (10), with the Gamma and retained-prime source terms
adjoined, would construct the contraction in Theorem 1 by sending the
corresponding orthogonal coordinate wedges.  Its norm estimate would be
the required comparison of total charged mass.  Conversely, (10)--(11)
do not give that comparison: they only express both norms in a positive
coordinate basis.

The Laplace expansion

\[
 D_{d+1}(\omega_0,\ldots,\omega_d)
 =\sum_{i=0}^d(-1)^{i+d}F_*(\omega_i)
   D_d(\omega_0,\ldots,\widehat\omega_i,\ldots,\omega_d)       \tag{13}
\]

also supplies no termwise lower bound.  The terms on the right have
physical phases and can cancel.  Replacing the square of their sum by a
sum of squares discards exactly the cross-atom interference retained by
the augmented determinant.

## 4. Positive endpoint-local charging is impossible

Before the radical quotient, the complete theta source admits the positive
edge measure \(\Omega_\Theta\) of 106.65.  The polar threshold is the edge
measure

\[
 d\rho(t,s)=8h(t)h(s)K(t)K(s)\,dt\,ds,
 \qquad t>s>0,                                      \tag{14}
\]

for which

\[
 \|\nabla_0r\|_{L^2(\rho)}^2
 =\frac12\operatorname {Var}_{\mu_K}(r).            \tag{15}
\]

A positive endpoint-local minor charge, specialized to exterior degree
zero, gives a positive substochastic coupling \(Q\) from source edges to
polar edges.  Its conditional-expectation operator would satisfy

\[
 C_Q\nabla_\Theta r=\nabla_0r                       \tag{16}
\]

on the form core, while Jensen gives its contraction norm.

For the exact radical family

\[
 r_j=K^{(2j)}/K,
\]

the source and polar norms are equal.  Hence (16) forces equality in
conditional Jensen for every \(r_j\).  The edge-separation lemma of
106.65 then forces

\[
 \partial E=Z\qquad Q\text{-almost surely};          \tag{17}
\]

the charge must preserve both endpoints.

This is impossible for the literal ordinary-prime source.  Its endpoint
measure has positive singular mass on

\[
 \mathcal L_p=
 \bigcup_{\Lambda(n)>0}\{t-s=\log n\}
 \ \cup\!
 \bigcup_{\Lambda(n)>0}\{t+s=\log n\},             \tag{18}
\]

whereas \(\rho(\mathcal L_p)=0\).  Endpoint preservation therefore
requires the charge to discard all prime-line mass.  Radical norm equality
forbids that discard, because \(|\nabla_\Theta r_1|^2\) has strictly
positive integral on those lines.  This is a contradiction.

### Theorem 2 — No universal positive minor injection

There is no positive, endpoint-local, weight-preserving configuration
injection which simultaneously

1. charges the complete polar threshold into the Gamma and ordinary-prime
   theta source;
2. is contractive by Jensen or a Markov/substochastic mass comparison;
3. preserves the exact radical equality family.

#### Proof

Such an injection in exterior degree zero induces the coupling \(Q\)
above.  Equations (16)--(18) give the contradiction just proved.  \(\square\)

The theorem rules out a universal positive charging construction across
the exterior hierarchy, because that hierarchy includes degree zero.  It
does not by itself rule out a row-specific nonlocal charge constructed
only after a fixed nonzero nuisance wedge and the complete radical
anti-short; that is the surviving case treated next.

## 5. The surviving projected Pluecker statement

Theorem 2 does not rule out a map which is constructed only after the
complete radical anti-short and which is nonlocal in all configuration
variables.  Such a map must depend on the particular row \((M,J,X)\) and
must preserve the common old-mode regression.  In invariant form its
required estimate is exactly

\[
 \boxed{
 \|f_1\wedge\cdots\wedge f_d\wedge f_*\|^2
 >\delta_J\,
   \|f_1\wedge\cdots\wedge f_d\|^2.}              \tag{19}
\]

By Theorem 1, merely naming this map or defining it from the two vectors
in (19) is circular.  A proof must construct it before (19), directly
from the literal theta translations and the ordinary coefficients, and
then prove a strict norm bound.

In the mean-periodic coordinate \(F=hq\), this is a quantitative stable
sampling statement on

\[
 F*K=0.                                             \tag{20}
\]

It is stronger than analytic injectivity.  The local Christoffel results
prove that every individual displacement detects every finite affine
mode row, but they give no uniform lower frame bound at the scale
\(\delta_J\).  The missing Riemann-specific estimate is precisely that
the complete projected theta observation has enough Pluecker volume,
after one common regression, to dominate the polar threshold.

Equivalently, in the signed evaluation factorization of 106.37 it is the
absorption inequality

\[
 \|T_-f\|^2
 \leq\|T_0f\|^2+\|T_+f\|^2                       \tag{21}
\]

on the corresponding completed quotient.  An off-line orbit creates an
accessible negative channel and violates (21).  Therefore a proof of
(19) for the cofinal family of rows excludes every off-line zero; this is
the force-bearing arithmetic content, not a missing determinant identity.

## 6. Ledger conclusion

The Cauchy--Binet attack has a definitive outcome.

* The determinant and squared-minor identities are exact.
* An abstract charging contraction exists if and only if the desired
  inequality already holds.
* Every positive endpoint-local, weight-preserving charge is excluded by
  radical saturation and the ordinary-prime singular lines.
* A row-dependent nonlocal projected charge remains logically possible,
  but proving its norm is the original strict surplus
  \(G_J>\delta_J\), equivalently the negative-channel absorption theorem.

Thus the next admissible attack cannot be a positive configuration
injection.  It must be a globally signed projected Pluecker identity or
inequality which uses the theta scaling relations before squaring the
minors and keeps Gamma, retained primes, omitted primes, the pole, and the
common regression coupled.
