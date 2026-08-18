# 106.191 — Amenable unitarization without an arithmetic surface

## 1. Purpose

The fixed-Rosati branch asks for an arithmetic intersection product and a
Hodge-index theorem.  An arithmetic surface
\(\operatorname {Spec}\mathbb Z\times_{\mathbb F_1}
\operatorname {Spec}\mathbb Z\) would provide such a source, but it is not
logically necessary.

This note gives a precise analytic replacement.  Exact unitarity of the
normalized scaling action need not be built into the initial norm.  It is
enough to construct an intrinsic faithful Hilbert completion on which that
action is uniformly bounded and the already constructed alternating form is
bounded and weakly nondegenerate.  Translation amenability then produces an
equivalent invariant metric, and the weak polar-completion theorem of
106.190 produces the positive compatible complex structure.

The result does not use the Rosati sign, the zeros of \(\xi\), or an
intersection theory.

## 2. Uniformly bounded scaling data

Let \((H_0,g_0)\) be a real Hilbert space and let
\(U:\mathbb R\to GL(H_0)\) be a strongly continuous group.  Assume

\[
 \boxed{\sup_{t\in\mathbb R}\|U_t\|_{g_0}\le M<\infty.}       \tag{1}
\]

Because \(U_{-t}=U_t^{-1}\), (1) also gives

\[
 M^{-1}\|u\|_{g_0}\le \|U_tu\|_{g_0}\le M\|u\|_{g_0}.        \tag{2}
\]

Let \(\Omega\) be a bounded alternating form on \(H_0\) satisfying

\[
 \Omega(U_tu,U_tv)=\Omega(u,v)                               \tag{3}
\]

and assume weak nondegeneracy:

\[
 \Omega(u,v)=0\ \text{for every }v\in H_0
 \quad\Longrightarrow\quad u=0.                             \tag{4}
\]

For the CCM action, \(U_t=e^{-t/2}\vartheta_t\); equation (3) is exactly
the normalized form of the weight-one covariance already proved for the
alternating residue pairing.

## 3. The invariant mean

### Lemma 3.1 — Translation-invariant mean on \(\mathbb R\)

There is a positive norm-one functional
\(m:L^\infty(\mathbb R)\to\mathbb R\) such that

\[
 m(1)=1,
 \qquad
 m(f(\,\cdot+s))=m(f)                                      \tag{5}
\]

for every \(s\in\mathbb R\).

#### Proof

For \(T>0\), put

\[
 m_T(f)=\frac1{2T}\int_{-T}^{T}f(t)\,dt.                    \tag{6}
\]

The \(m_T\) belong to the weak-star compact unit ball of
\((L^\infty)^*\).  Choose a weak-star cluster point \(m\) along
\(T\to\infty\).  Positivity, norm one, and \(m(1)=1\) pass to the limit.
For fixed \(s\),

\[
 |m_T(f(\,\cdot+s))-m_T(f)|
 \le \frac{|s|}{T}\|f\|_\infty,                            \tag{7}
\]

so the cluster point satisfies (5). \(\square\)

## 4. Unitarization theorem

### Theorem 4.1 — Uniform boundedness produces an equivariant polarization

Under (1)--(4), define

\[
 \boxed{
 \bar g(u,v)
 =m\!\left(t\longmapsto g_0(U_tu,U_tv)\right).}             \tag{8}
\]

Then \(\bar g\) is an inner product equivalent to \(g_0\),

\[
 M^{-2}g_0(u,u)\le \bar g(u,u)\le M^2g_0(u,u),              \tag{9}
\]

and every \(U_s\) is \(\bar g\)-unitary.  The form \(\Omega\) remains
bounded and weakly nondegenerate for \(\bar g\).  Consequently its Riesz
representative \(A\) in \(\bar g\) is bounded, skew-adjoint, and injective.
The polar part

\[
 J=A|A|^{-1}                                                \tag{10}
\]

is a unitary complex structure commuting with every \(U_t\), and

\[
 g_1(u,v)=\Omega(u,Jv)=\bar g(|A|u,v)                       \tag{11}
\]

is positive definite.  On the \(g_1\)-completion, \(U_t\) is a strongly
continuous unitary group and the original CCM action
\(\vartheta_t=e^{t/2}U_t\) is a polarized weight-one similitude.

#### Proof

The bounds (2), positivity of \(m\), and (8) give (9).  Hence \(\bar g\)
is definite and induces the same Hilbert topology as \(g_0\).  Translation
invariance of \(m\) gives

\[
 \bar g(U_su,U_sv)
 =m\!\left(t\mapsto g_0(U_{t+s}u,U_{t+s}v)\right)
 =\bar g(u,v).                                              \tag{12}
\]

Equivalence of the two norms preserves boundedness of \(\Omega\), and
(4) is algebraic, so it also persists.  Thus the Riesz representative is
bounded, skew-adjoint, and has zero kernel.  Theorem 3.1 of 106.190 gives
(10)--(11) and the positive weak polar completion.  Equation (3) together
with (12) implies \(U_t^*AU_t=A\); hence \(U_t\) commutes with \(A\),
\(|A|\), and \(J\).  Theorem 4.1 of 106.190 gives strong unitary extension
to the \(g_1\)-completion. \(\square\)

### Corollary 4.2 — Exact non-geometric substitute for the Hodge-index input

On the separated CCM degree one, it is sufficient to construct, directly
from the prime, Gamma, and polar source data, a Hilbert norm satisfying:

1. faithfulness on the separated nuclear CCM classes;
2. bounded weak nondegeneracy of the descended alternating form;
3. uniform boundedness of \(e^{-t/2}\vartheta_t\) for all real \(t\).

No arithmetic surface or a priori Rosati positivity is then required.

Conversely, every positive equivariant polarization supplies such a norm
with \(M=1\).  Thus this is the exact analytic alternative to an
intersection-theoretic construction, not an additional consequence of
the fixed Rosati form.

## 5. Why this is not the GNS factorization in disguise

The GNS map

\[
 \tau(f*g^\sharp)=\langle D[f],D[g]\rangle                 \tag{13}
\]

can be defined only after the Rosati form is known to be positive.  By
contrast, Theorem 4.1 starts from a positive norm \(g_0\) not defined by
\(\tau\).  The sign is obtained from the symplectic polar decomposition,
not inserted through (13).

This distinction imposes a strict admissibility test: the candidate
\(g_0\) must be defined before evaluating the Weil/Rosati quadratic form.
A norm built from \(|\tau|\), from a list of zeros, or from the positive
part of the Rosati operator would be circular.

## 6. Interaction with the existing obstructions

The theorem also identifies why the three positive constructions already
available do not yet finish the descent.

* The rooted-Jacobian metric of 106.164 is source-defined and positive,
  but Proposition 7.1 there proves that its continuous Hilbert quotient
  on the dense CCM range is zero.
* The nuclear Euler norm of 106.188 is faithful and retains the prime
  phases, but only the discrete subgroup
  \(\log\mathbb Q_+^\times\) acts naturally; the full real CCM action is
  not uniformly bounded in that topology.
* Free archimedean induction in 106.189 restores a real unitary action,
  but makes the Euler collapse coisometric and annihilates the desired
  cokernel.

Therefore the remaining construction must be intrinsic to the relative
torsion degree one and must couple Gamma, the pole, and the Euler row
before completion.  It cannot be the continuous quotient of the positive
root Hilbert space and cannot be a free archimedean tensor factor.

## 7. Status

Proved:

* literal construction of an arithmetic surface is not logically
  necessary for the polarization step;
* uniformly bounded normalized scaling can be unitarized by an invariant
  mean without using zeros or Rosati positivity;
* bounded weak nondegeneracy then yields the compatible positive complex
  structure through weak polar completion;
* the exact three-condition analytic substitute for the geometric
  Hodge-index input.

Still required:

* a source-defined non-free Gamma--Euler--polar relative Hilbert norm on
  separated CCM degree one satisfying the three conditions of Corollary
  4.2.
