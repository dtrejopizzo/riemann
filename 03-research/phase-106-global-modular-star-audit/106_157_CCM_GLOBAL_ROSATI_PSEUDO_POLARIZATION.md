# 106.157 — The global Rosati pseudo-polarization on the actual CCM degree one

## 1. Purpose

Documents 106.154--106.156 construct positive coefficient and chain
polarizations. They do not by themselves put a form on the zero-carrying
CCM degree-one object. This document performs that descent at the
algebraic/topological level, using the cyclic cokernel, its trace pairing,
and the sharp involution.

The result is a canonical nondegenerate Hermitian pseudo-polarization on
the primitive CCM degree one. It has exact weight-one covariance, and its
imaginary part is an alternating form compatible with the ordinary complex
structure. No zero is used in its definition. The remaining statement is
the positivity of its real part.

## 2. The CCM quotient and its involution

Let

\[
 \mathcal Z=\mathbf S(C_{\mathbb Q})/\overline{\mathcal V},    \tag{1}
\]

where \(\mathcal V\) is the range of the adelic reduction/summation map and
the closure is taken in the CCM Schwartz/Meyer topology. Convolution on
\(C_{\mathbb Q}\) descends because \(\mathcal V\) is a convolution
submodule.

For \(f\in\mathbf S(C_{\mathbb Q})\), put

\[
 f^*(x)=\overline{f(x^{-1})},\qquad
 f^\sharp(x)=|x|^{-1}\overline{f(x^{-1})}.                    \tag{2}
\]

Then \(\sharp\) is a conjugate-linear involution and

\[
 (f*g)^\sharp=g^\sharp*f^\sharp.                              \tag{3}
\]

Let

\[
 \tau(f)=\operatorname{Tr}\!\left(
 \underline\vartheta_m(f)\mid H^1_{\rm CCM}\right)            \tag{4}
\]

be the CCM trace functional. Its real structure gives

\[
 \tau(f^\sharp)=\overline{\tau(f)},                            \tag{5}
\]

and the CCM vanishing lemma gives

\[
 \tau(v*f)=0\qquad(v\in\mathcal V).                            \tag{6}
\]

## 3. The Hermitian trace form

Define on \(\mathcal Z\)

\[
 \mathfrak h([f],[g])=\tau(f*g^\sharp).                        \tag{7}
\]

### Theorem 3.1 — Well-defined Hermitian descent

The form (7) is well defined, linear in its first variable,
conjugate-linear in its second, and Hermitian:

\[
 \boxed{\mathfrak h([g],[f])=
 \overline{\mathfrak h([f],[g])}.}                            \tag{8}
\]

#### Proof

If \(f\) is changed by \(v\in\mathcal V\), (6) makes the change in (7)
zero. If \(g\) is changed by \(v\), then \(v^\sharp\) belongs to the
sharp-stable closure of the adelic range; convolution commutativity and
(6) again give zero. Sesquilinearity is immediate. Finally, (3)--(5) give

\[
 \overline{\tau(f*g^\sharp)}
 =\tau((f*g^\sharp)^\sharp)
 =\tau(g*f^\sharp).
\]

This is (8). \(\square\)

Let

\[
 \mathcal N=\{z\in\mathcal Z:\mathfrak h(z,w)=0
                 \text{ for every }w\in\mathcal Z\}.         \tag{9}
\]

The primitive separated degree one is

\[
 H^1_{\rm Ros}:=\mathcal Z/\mathcal N.                        \tag{10}
\]

By construction, \(\mathfrak h\) is nondegenerate on
\(H^1_{\rm Ros}\). This quotient removes only the radical of the trace
pairing, not negative vectors.

## 4. Alternating form and compatible complex structure

Regard \(H^1_{\rm Ros}\) as a real vector space and let

\[
 Jz=iz.                                                        \tag{11}
\]

Put

\[
 g_{\rm Ros}(u,v)=\operatorname{Re}\mathfrak h(u,v),\qquad
 \Omega_{\rm Ros}(u,v)=-\operatorname{Im}\mathfrak h(u,v).    \tag{12}
\]

### Theorem 4.1 — Global pseudo-polarization

The form \(\Omega_{\rm Ros}\) is real bilinear and alternating. Together
with \(g_{\rm Ros}\), it is nondegenerate on the quotient, and

\[
 \boxed{
 J^2=-I,\qquad
 \Omega_{\rm Ros}(u,Jv)=g_{\rm Ros}(u,v).}                    \tag{13}
\]

#### Proof

Hermitian symmetry gives
\(\operatorname{Im}\mathfrak h(v,u)=-\operatorname{Im}\mathfrak h(u,v)\).
With the convention that \(\mathfrak h\) is conjugate-linear in the second
variable, \(\mathfrak h(u,iv)=-i\mathfrak h(u,v)\); hence

\[
 -\operatorname{Im}\mathfrak h(u,iv)
 =\operatorname{Re}\mathfrak h(u,v).
\]

If both real and imaginary parts pair \(u\) trivially with every \(v\),
then \(\mathfrak h(u,v)=0\) for every \(v\), and (10) gives \(u=0\).
\(\square\)

The adjective *pseudo* records only that \(g_{\rm Ros}(u,u)\) has not yet
been shown nonnegative.

## 5. Exact weight-one covariance

For \(a\in C_{\mathbb Q}\), let

\[
 (L_af)(x)=f(a^{-1}x).                                        \tag{14}
\]

Directly from (2),

\[
 (L_af)^\sharp=|a|L_{a^{-1}}(f^\sharp),                       \tag{15}
\]

and opposite translations cancel under convolution:

\[
 (L_af)*(L_{a^{-1}}g)=f*g.                                    \tag{16}
\]

### Theorem 5.1 — Polarized similitude law

The scaling action on \(H^1_{\rm Ros}\) satisfies

\[
 \boxed{
 \begin{aligned}
 \mathfrak h(L_au,L_av)&=|a|\mathfrak h(u,v),\\
 \Omega_{\rm Ros}(L_au,L_av)&=|a|\Omega_{\rm Ros}(u,v),\\
 g_{\rm Ros}(L_au,L_av)&=|a|g_{\rm Ros}(u,v),\\
 L_aJ&=JL_a.
 \end{aligned}}                                               \tag{17}
\]

Consequently \(U_a=|a|^{-1/2}L_a\) is pseudo-unitary. If \(\Theta\) is
the infinitesimal generator of positive-real scaling, then

\[
 \boxed{\Theta^\dagger+\Theta=I}                              \tag{18}
\]

with respect to \(\mathfrak h\).

#### Proof

Equations (15)--(16) give

\[
 \mathfrak h(L_a[f],L_a[g])
 =|a|\tau((L_af)*(L_{a^{-1}}g^\sharp))
 =|a|\mathfrak h([f],[g]).
\]

Taking real and imaginary parts proves (17), and scalar multiplication by
\(i\) commutes with translation. Differentiating at the identity gives
(18). \(\square\)

## 6. Relation with the positive chain construction

The Fourier--Weyl mixed complex of 106.156 carries a positive chain metric
\(g_{\rm FW}\), while (7) is the canonical form on the actual CCM degree
one. A polarization transfer would be a map

\[
 \mathfrak D:H^1_{\rm Ros}\longrightarrow
 H_1(\mathfrak C_{\rm FW,rel})                                \tag{19}
\]

satisfying

\[
 \boxed{
 \mathfrak h(u,v)=
 g_{\rm FW}(\mathfrak Du,\mathfrak Dv)
 +i\,\Omega_{\rm FW}(\mathfrak Du,\mathfrak Dv).}            \tag{20}
\]

If (20) holds and \(\mathfrak D\) is faithful, then
\(g_{\rm Ros}(u,u)=\|\mathfrak Du\|^2\ge0\), with equality only on the
removed radical. Thus (20) is the factorization form of the missing
Hodge/Rosati theorem.

The data in (20) are source-defined: the left side is the CCM trace pairing
and sharp involution; the right side is the Fourier--Weyl positive chain
metric; the prime coefficient modules descend through the single Cauchy
dilation and are jointly observable; and the scaling laws agree after the
degree-one Tate twist. No choice of zeros occurs in either side.

## 7. Positivity gate

The remaining claim is

\[
 \boxed{g_{\rm Ros}(u,u)=\tau(f*f^\sharp)\ge0
 \quad\text{for every }u=[f]\in H^1_{\rm Ros}.}               \tag{21}
\]

Equivalently, one must construct the faithful factorization (20). An
indefinite Hermitian form also satisfies (8), (13), (17), and (18), so
those identities alone do not imply (21). The arithmetic content is the
upgrade from pseudo-unitary to unitary.

## 8. Status

Proved without spectral input:

* a global Hermitian form on the actual CCM quotient;
* removal of its intrinsic radical;
* a global alternating form and compatible complex structure;
* the exact weight-one similitude and generator identity;
* the exact positive-factorization statement that would complete the
  polarization.

Still required:

* construct \(\mathfrak D\) and prove (20), or prove (21) by an equivalent
  source-side Hodge-index identity.

### Prior-work audit inside this project

The pseudo-polarization itself is not claimed as a new solution.  Phase 15
already constructed the corresponding Krein/Weil form and proved that its
positivity is the arithmetic Hodge-index gate.  It also closed the attempt
to obtain the missing sign by transporting the archimedean continuum
\(\mathfrak{sl}_2\): the transported form is the same prime--archimedean
near-cancellation residual.  The new content of 106.154--106.156 is the
source-defined Cauchy coefficient descent and the Fourier-dual cyclic chain
polarization.  Therefore (20) must be proved using those new structures;
reusing the continuum Lefschetz operator would repeat the closed Phase-15
route.

## 9. Primary source

The cokernel, trace pairing, sharp involution, vanishing on the adelic
range, and weight-one scaling action are from A. Connes, C. Consani, and
M. Marcolli,
[*The Weil proof and the geometry of the adeles class space*](https://arxiv.org/abs/math/0703392).
