# 106.101 — Relative-heat spectral shift and the exact source deficit

## 1. Purpose

Document 106.100 constructs the positive relative heat observable

\[
 \Theta_V(t)=\operatorname {Tr}\{e^{-tS}-e^{-t(S+V)}\},
 \qquad S=A+\frac12I,
 \tag{1}
\]

where \(A=L|_{(\mathbf1\oplus\mathcal R)^\perp}\), and proves that its
logarithmic decay detects the physical floor.  This note determines the
leading coefficient under the subthreshold counterfactual.

If

\[
 \alpha=\inf\sigma(A)<\frac12
 \tag{2}
\]

has multiplicity \(m_\alpha\), then for every positive injective trace-class
boost \(V\),

\[
 \boxed{
 \Theta_V(t)\sim m_\alpha e^{-t(\alpha+1/2)}.}
 \tag{3}
\]

Consequently the literal ordinary-prime--Gamma source has the exact
heat-weighted deficit

\[
 \boxed{
 \frac12A_V(t)-E_V(t)
 \sim
 \left(\frac12-\alpha\right)
 \frac{m_\alpha}{t}e^{-t(\alpha+1/2)}.}
 \tag{4}
\]

Thus positive source atoms, Tonelli positivity, heat regularization and an
injective boost are all compatible with a strictly positive threshold
deficit.  They detect a subthreshold mode with integer leading weight; they
do not exclude it.

## 2. The relative spectral measure

For \(s\in[0,1]\), put \(S_s=S+sV\), and define the finite positive measure

\[
 d\eta_V(\lambda)
 =\int_0^1\operatorname {Tr}
 \bigl(V^{1/2}E_{S_s}(d\lambda)V^{1/2}\bigr)\,ds.
 \tag{5}
\]

The Duhamel identity of 106.100 gives

\[
 \boxed{
 \frac{\Theta_V(t)}t
 =A_V(t)
 =\int_{\mathbb R}e^{-t\lambda}\,d\eta_V(\lambda).}
 \tag{6}
\]

No trace-class assumption on either heat semigroup is used.  The measure in
(5) is finite because

\[
 \eta_V(\mathbb R)=\int_0^1\operatorname {Tr}V\,ds=\|V\|_1.
 \tag{7}
\]

## 3. Local spectral-shift mass at an isolated ground cluster

Let

\[
 \lambda_0=\alpha+\frac12.
 \tag{8}
\]

The proved essential threshold makes \(\lambda_0\) an isolated eigenvalue of
\(S\), of finite multiplicity \(m_\alpha\).  Choose \(\varepsilon_0>0\) so
that

\[
 \sigma(S)\cap(\lambda_0,\lambda_0+3\varepsilon_0)=\varnothing.
 \tag{9}
\]

Because \(V\ge0\), every eigenvalue in the ground cluster of \(S_s\) is
nondecreasing in \(s\).  Injectivity of \(V\) and finite dimensionality of
the ground eigenspace imply that the cluster moves strictly to the right.
After reducing \(s_0>0\), the cluster remains isolated for
\(0\le s\le s_0\), and its eigenvalue branches may be denoted

\[
 \lambda_j(s),\qquad 1\le j\le m_\alpha,
 \tag{10}
\]

with multiplicity.  They are absolutely continuous, satisfy

\[
 \lambda_j(0)=\lambda_0,
 \qquad
 \lambda_j'(s)=\operatorname {Tr}(VP_j(s))
 \quad\text{for a.e. }s,
 \tag{11}
\]

after resolving crossings into the corresponding spectral subclusters.
Here \(P_j(s)\) is the spectral projection of that branch.  Formula (11) is
the trace form of the Hellmann--Feynman identity; summing it over a crossing
cluster is independent of the choice of branches.

For every continuous function \(\varphi\) supported in
\((\lambda_0,\lambda_0+\varepsilon_0)\), functional calculus and (11) give

\[
\begin{aligned}
 \int\varphi(\lambda)\,d\eta_V(\lambda)
 &=\sum_{j=1}^{m_\alpha}\int_0^{s_0}
     \varphi(\lambda_j(s))\lambda_j'(s)\,ds \\
 &=\sum_{j=1}^{m_\alpha}
   \int_{\lambda_0}^{\lambda_j(s_0)}\varphi(\lambda)\,d\lambda.
\end{aligned}
\tag{12}
\]

All spectral components outside this cluster lie above
\(\lambda_0+2\varepsilon_0\) after possibly decreasing \(s_0\).  Since
every \(\lambda_j(s_0)>\lambda_0\), (12) proves the exact local density

\[
 \boxed{
 d\eta_V(\lambda)=m_\alpha\,d\lambda
 \quad\text{on }(\lambda_0,\lambda_0+\varepsilon_V)}
 \tag{13}
\]

for some \(\varepsilon_V>0\).  Notice that the density is independent of the
size and orientation of \(V\).  The branch velocity in (11) is exactly
cancelled by the change of variables in (12).  The interval can be chosen
below \(\min_j\lambda_j(s_0)\); form monotonicity
\(S_s\ge S_{s_0}\) for \(s\ge s_0\) then shows that the omitted part of the
\(s\)-integral contributes no additional mass there.

## 4. Exact large-time coefficient

Split (6) at \(\lambda_0+\varepsilon_V\).  Equation (13) gives

\[
 \int_{\lambda_0}^{\lambda_0+\varepsilon_V}
 e^{-t\lambda}\,d\eta_V(\lambda)
 =\frac{m_\alpha}{t}e^{-t\lambda_0}
   \{1-e^{-t\varepsilon_V}\}.
 \tag{14}
\]

The remaining finite positive measure contributes
\(O(e^{-t(\lambda_0+\varepsilon_V)})\).  Hence

\[
 A_V(t)\sim\frac{m_\alpha}{t}e^{-t\lambda_0},
 \qquad
 \Theta_V(t)=tA_V(t)\sim m_\alpha e^{-t\lambda_0},
 \tag{15}
\]

which proves (3).

## 5. The literal source deficit

Use the notation of 106.100:

\[
 E_V(t)=\int_0^1\operatorname {Tr}(L\Gamma_{s,t})\,ds,
 \qquad
 B_V(t)=\int_0^1s\operatorname {Tr}(V\Gamma_{s,t})\,ds.
 \tag{16}
\]

The exact source identity there is

\[
 -\partial_t\log\Theta_V(t)
 =-\frac1t+\frac12+\frac{E_V(t)}{A_V(t)}
                    +\frac{B_V(t)}{A_V(t)},
 \qquad
 0\le\frac{B_V(t)}{A_V(t)}\le\frac1t.
 \tag{17}
\]

Differentiating the two Laplace integrals obtained by splitting (6) at
\(\lambda_0+\varepsilon_V\), and using (13), yields

\[
 \frac{E_V(t)}{A_V(t)}\longrightarrow\alpha.
 \tag{18}
\]

Combining (15) and (18) proves (4).  Each \(E_V(t)\) in this formula is the
literal nonnegative source sum

\[
\begin{aligned}
 E_V(t)={}&\int_0^1\int_0^\infty
 \frac{e^{-u/2}}{1-e^{-2u}}
 \mathcal J_u[\Gamma_{s,t}]\,du\,ds\\
 &+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \int_0^1\mathcal J_{\log n}[\Gamma_{s,t}]\,ds.
\end{aligned}
\tag{19}
\]

Thus (4) does not arise by separating or changing any physical source.

## 6. Consequence for a source-rate proof

The desired estimate is

\[
 \liminf_{t\to\infty}\frac{E_V(t)}{A_V(t)}\ge\frac12.
 \tag{20}
\]

Equations (4) and (18) give the exact adversarial alternative:

\[
 \alpha<\frac12
 \quad\Longrightarrow\quad
 \frac{E_V(t)}{A_V(t)}\to\alpha<\frac12
 \tag{21}
\]

while every term in (19), every raw heat moment, and \(\Theta_V(t)\) itself
remain nonnegative.  Therefore none of the following inputs can imply
(20) without an additional signed estimate:

* positivity of the ordinary coefficients \(\Lambda(n)\);
* positivity of the Gamma channel;
* Tonelli interchange of the complete source;
* heat regularization and trace-class relative summability;
* positivity of all unshifted heat moments.

The required new statement must control the compensated source

\[
 E_V(t)-\frac12A_V(t)
 \tag{22}
\]

itself.  Under the subthreshold counterfactual, (4) proves that (22) has a
negative main term with explicit exponent, coefficient and sign.  Hence a
proof of its nonnegativity is exactly a bound-state exclusion theorem for
the literal ordinary-prime--Gamma operator, not a consequence of the
positive heat representation.

## 7. Status

Proved here:

* the finite relative spectral measure (5);
* the local integer density (13) at an isolated ground cluster;
* the boost-independent asymptotic (3);
* the exact literal-source deficit (4).

Not proved here:

\[
 \liminf_{t\to\infty}\frac{E_V(t)}{A_V(t)}\ge\frac12.
\]

The note sharpens the heat falsifier: a hypothetical subthreshold physical
mode survives every positive heat/source identity with a nonzero integer
leading coefficient.
