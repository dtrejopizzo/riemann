# 106.82 — Finite-response inertia falsifier and the adaptive residual

## Purpose

The directional target isolated in 106.81 concerns one particular vector:
the signed Schur residual \(q^*\) selected by the preceding positive block.
It is important not to replace this target by the stronger assertion that
every negative finite spectral vector has a uniformly large response in a
fixed block of prime-midpoint channels.  The latter assertion is false for
an exact dimension reason.

This note proves the falsifier, states the exact equation which distinguishes
the adaptive residual, and records a local diagnostic using the literal
midpoint samples of 106.73.  It does not prove the directional estimate of
106.81.

### Prior-route audit

The generic Gram-distance identity was already used in Phase 72,
E72.117, and the scalar Schur innovation was isolated again in Phase 102.
Within the present phase, 106.73 derives the midpoint functional \(A_p\),
106.74 explains why qualitative phase separation has no uniform lower
constant, 106.76 proves exact finite-block observability, and 106.80--106.81
derive the pure and augmented conditional determinants.  None of those
notes tests the intersection of a finite response kernel with the negative
subspace of the preceding signed head.  The theorem below is elementary
inertia algebra; its role is to prevent the existing observability theorem
from being upgraded to an invalid arbitrary-vector quantitative bound.

## 1. A response-kernel inertia theorem

Let \(V\) be a finite-dimensional complex vector space, let \(H\) be a
Hermitian form on \(V\), and let

\[
 T:V\longrightarrow \mathbb C^K                         \tag{1}
\]

be any collection of \(K\) linear observations.  Denote the negative index
of \(H\) by \(\nu_-(H)\).

### Theorem 1 — Inertia survives too few observations

If

\[
 \nu_-(H)>\mathrm{rank}\,T,                         \tag{2}
\]

then there is a nonzero \(q\in\ker T\) such that

\[
 \boxed{H(q,q)<0,\qquad Tq=0.}                           \tag{3}
\]

More precisely, the restriction of \(H\) to \(\ker T\) has negative index
at least

\[
 \boxed{
 \nu_-(H|_{\ker T})\ge
 \nu_-(H)-\mathrm{rank}\,T.}                        \tag{4}
\]

#### Proof

Choose a maximal negative subspace \(N\subset V\), so
\(\dim N=\nu_-(H)\) and \(H(q,q)<0\) for every nonzero \(q\in N\).  Since

\[
 \mathrm{codim}\,\ker T=\mathrm{rank}\,T,
\]

the dimension formula gives

\[
 \dim(N\cap\ker T)
 \ge \dim N-\mathrm{rank}\,T.
\]

The restriction of \(H\) to this intersection is negative definite.  This
proves (4), and (3) follows from (2).  \(\square\)

### Corollary 2 — No arbitrary-vector response floor

Under (2), no constant \(c>0\) can satisfy

\[
 \|Tq\|^2\ge c\{-H(q,q)\}                         \tag{5}
\]

for every \(H\)-negative vector \(q\in V\).  In particular, taking

\[
 T_Kq=(A_{p_1}(q),\ldots,A_{p_K}(q))                       \tag{6}
\]

shows that finitely many prime-midpoint samples cannot control an arbitrary
negative subspace whose dimension exceeds their rank.

This is independent of the positions of the primes, the theta attenuation,
or arithmetic independence of their logarithms.  It is an exact
finite-dimensional obstruction.

## 2. Why the adaptive Schur residual is different

The staircase row of 106.80 begins with

\[
 H_0=
 \begin{pmatrix}A&c\\c^*&h\end{pmatrix},
 \qquad A\succ0,                                          \tag{7}
\]

and defines

\[
 a=A^{-1}c,
 \qquad
 q^*=\phi_M-\sum_{j<M}a_j\phi_j,
 \qquad
 \sigma_0=H_0(q^*,q^*)=h-c^*A^{-1}c.                    \tag{8}
\]

If \(\sigma_0<0\), Sylvester inertia gives

\[
 \nu_-(H_0)=1.                                           \tag{9}
\]

Thus the dimension obstruction of Theorem 1 disappears as soon as one
nonzero observation is applied.  It neither proves nor disproves that the
observation sees the unique adaptive direction.

Write the response matrix in the same ordered basis as

\[
 T_K=[B\;b],
 \qquad
 B\in\mathbb C^{K\times(M-1)},\quad b\in\mathbb C^K.   \tag{10}
\]

Then the exact adaptive response is

\[
 \boxed{T_Kq^*=b-BA^{-1}c.}                              \tag{11}
\]

Consequently

\[
 T_Kq^*=0
 \quad\Longleftrightarrow\quad
 b=BA^{-1}c.                                             \tag{12}
\]

No inertia identity forbids the interpolation equation (12).  Conversely,
full column rank of \([B\;b]\) excludes exact vanishing but supplies no
quantitative lower bound at the theta-weighted scale required by 106.81.

The weighted midpoint energy in the notation of that document is exactly

\[
 \sum_{p\in\mathcal P}\beta_p
 |A_p(q^*)+\rho_p(q^*)|^2
 =\|W_{\mathcal P}^{1/2}
       (b-BA^{-1}c+\rho(q^*))\|^2.                       \tag{13}
\]

Therefore the surviving theorem must estimate the specific regression
residual in (11), including the physical weights and aperture errors.  A
frame bound for arbitrary \(q\) is both unnecessary and, in the range of
Theorem 1, impossible.

### Remark — Adaptivity without a fixed exhaustion is not enough

Even a one-negative-direction form admits an abstract counterexample.  Let

\[
 H=I_{M-1}\oplus[-1],\qquad
 T(y,t)=T_0y,                                            \tag{14}
\]

so the negative basis vector is invisible.  Ordered after the positive
coordinates it is exactly the Schur residual \(q^*\), with pivot \(-1\).
Hence the force-bearing information is not the word *adaptive* alone; it is
the literal relation among the Riemann head \(H_0\), its prescribed mode
exhaustion, and the ordinary-prime response rows.

## 3. Literal finite-head diagnostic

The script

```text
python3 tools/finite_midpoint_response_inertia.py \
  --dx 0.0005 --span 24 --max-k 15
```

uses the weighted-orthonormal first 24 real zero modes, the literal
Gamma-only Gram, and

\[
 A_p(z)=2z\sin(z\log p/2)
 +\tanh(\log p/4)\cos(z\log p/2).                       \tag{15}
\]

The calculation is floating point and is not an interval certificate.  Its
stable rows at meshes \(1.5\cdot10^{-3},10^{-3},5\cdot10^{-4}\) are

\[
\begin{array}{c|c|c|c}
K&\mathrm{rank}\,T_K&\dim\ker T_K&
\lambda_{\min}(H_\Gamma|_{\ker T_K})\\ \hline
10&10&14&-0.22488917\ldots\\
12&12&12&-0.06385456\ldots\\
13&13&11&-0.05564949\ldots\\
14&14&10&-0.05385060\ldots\\
15&15&9& \phantom{-}0.10135891\ldots
\end{array}                                             \tag{16}
\]

The computed Gamma defect has negative index \(12\).  Theorem 1 guarantees
negative kernel vectors for \(K<12\); the additional negative rows at
\(K=12,13,14\) are system-specific numerical observations.  For the
computed witnesses, the relative response residual is below
\(1.4\cdot10^{-16}\).

By contrast, the natural adaptive residuals at the four stable transitions
used in 106.81 have nonzero first available prime-midpoint responses in the
same diagnostic.  This distinction is evidence that (11), rather than an
arbitrary-vector frame floor, is the appropriate target.  It is not a proof
of the required cofinal lower bound.

## 4. Consequence for the next attack

The admissible statement has to retain all three dependencies

\[
 \boxed{
 q^*=q^*(H_0,V_{M-1}),\qquad
 \sigma_0=\sigma_0(H_0,V_{M-1}),\qquad
 T_{\mathcal P}=T_{\mathcal P}(\Lambda,K).}              \tag{17}
\]

A valid crossing theorem may use the exact normal equation

\[
 H_0(q^*,v)=0\qquad(v\in V_{M-1})                        \tag{18}
\]

to compare the negative pivot with the response residual (11).  A theorem
which drops (18) and estimates every finite spectral \(q\) is falsified by
Theorem 1 before theta decay enters.

The remaining scalar target is unchanged:

\[
 \sum_{p\in\mathcal P}\beta_p
 |A_p(q^*)+\rho_p(q^*)|^2
 >(-\sigma_0)
 \left(1+\frac{\|S_0\|^2}{\lambda_{\min}(A)}\right).     \tag{19}
\]

The new restriction is decisive: (19) must be derived from the adaptive
orthogonality equation (18) and the literal prime--Gamma structure, not
from finite-dimensional observability alone.
