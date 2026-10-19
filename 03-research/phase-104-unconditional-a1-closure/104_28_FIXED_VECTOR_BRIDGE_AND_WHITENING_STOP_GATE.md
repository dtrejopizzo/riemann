# 104_28 — Fixed-vector bridge and the archimedean whitening stop-gate

**Role.** Audit the proposal to prove the proportional margin via
non-alignment of the Laguerre test with the near-extremal subspace of the
whitened prime operator. The fixed-vector bridge exists and is exact: the Li
test is the Dirichlet prefix in the orthonormal Laguerre basis of the
boundary. What does not exist in the record is a simultaneous bridge
identifying, on that same boundary, a positive archimedean metric whose
evaluation is \(A_n\). Hence the overlap with the top eigenvector of phases
62–69 is not today a quantity faithful to A1.

This document does not prove A1 or RH. It proves which part of the
proposal is exact, which part duplicates 103_24–103_26, and what new
mathematical obligation would have to be met before running a spectral
diagnostic.

## 1. The exact bridge to the Dirichlet prefix

Let

\[
 f_n(x)={\bf1}_{[0,\infty)}(x)L_{n-1}^{(1)}(x),
 \qquad g_n(x)=e^{-x/2}f_n(x),
\]

and

\[
 \phi_k(x)={\bf1}_{[0,\infty)}(x)e^{-x/2}L_k(x).
\]

Ordinary Laguerre orthogonality gives

\[
 \langle\phi_j,\phi_k\rangle_{L^2(0,\infty)}=\delta_{jk}.
\]

The summation identity

\[
 \boxed{L_{n-1}^{(1)}(x)=\sum_{k=0}^{n-1}L_k(x)}                 \tag{1}
\]

produces

\[
 \boxed{g_n=\sum_{k=0}^{n-1}\phi_k,
 \qquad [g_n]_{\{\phi_k\}}={\bf1}_n,
 \qquad \|g_n\|_2^2=n.}                                        \tag{2}
\]

So the test function is not an unknown vector: it is exactly the prefix
\((1,\ldots,1)\). Basis (2) is the Laguerre basis of parameter
\(y=1/2,t_0=0\); under \(s=1/2+iz\), it corresponds to the boundary point
\(s=1\). Moreover, since \(L_k(0)=1\),

\[
 L_{n-1}^{(1)}(x)=K_{n-1}^{\rm Lag}(x,0),
\]

so \(g_n/\sqrt n\) is the normalized state of the reproducing kernel at the
hard boundary \(x=0\), not a generic vector.

In the monomial jet basis, the same vector can be written as

\[
 \phi_j^{\rm mon}(x)={(-ix)^j\over j!}e^{-x/2},
 \qquad c_j^{(n)}=i^j{n\choose j+1}\quad(0\le j<n),              \tag{2a}
\]

with the convention \(F_c=\sum_j\overline{c_j}\phi_j^{\rm mon}\). Then
\(F_{c^{(n)}}=g_n\).

By 103_69, if \(h_n=f_n*f_n^\#\), then

\[
 \mathcal Lh_n(s)
 =\left(1-\left({s-1\over s}\right)^n\right)
  \left(1-\left({s\over s-1}\right)^n\right),
 \qquad
 \boxed{\mathcal W_\zeta(h_n)=2\lambda_n.}                     \tag{3}
\]

Equations (1)–(3) are the complete bridge for the **total** Weil form.

There is a further simplification. Since

\[
 F_n(s)F_n(1-s)=F_n(s)+F_n(1-s),
\]

uniqueness of the transform gives

\[
 \boxed{f_n*f_n^\#=f_n+f_n^\#,
 \qquad (g_n*\widetilde g_n)(a)=g_n(|a|).}                     \tag{3a}
\]

Hence, for the translation semigroup \(S_a\),

\[
 \boxed{\langle S_ag_n,g_n\rangle
 =e^{-a/2}L_{n-1}^{(1)}(a).}                                  \tag{3b}
\]

## 2. Exact Toeplitz polarization of the scalar datum

For any real sequence \(q_0=0,q_1,q_2,\ldots\), define

\[
 t_0(q)=q_1,
 \qquad
 t_m(q)={q_{m+1}-2q_m+q_{m-1}\over2}\quad(m\ge1),               \tag{4}
\]

and \(T_N(q)=[t_{|j-k|}(q)]_{0\le j,k<N}\). Two summations by
parts give, with no sign hypothesis,

\[
 \boxed{{\bf1}_n^*T_n(q){\bf1}_n=q_n.}                          \tag{5}
\]

In particular, taking \(q=2\lambda-A\), (5) is precisely the Fejér form
of 103_24–103_26. For the current margin, \(q=r_*\lambda-A\) may be
taken. Hence the observation "A1 only needs a fixed vector" is correct, but
its natural Toeplitz polarization was already on record: the fixed vector
is \({\bf1}_n\).

Identity (3b) also exactly recomposes the prime side. For
\(\varepsilon>0\), the expression

\[
 \mathfrak p_{\Lambda,\varepsilon}[g_n]
 :=\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
 \langle(S_{\log m}+S_{\log m}^*)g_n,g_n\rangle                \tag{6a}
\]

is a **form on the ray \(g_n\)** and satisfies

\[
 {1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                        \tag{6b}
\]

This must not be called a bounded operator obtained by summing in norm:
the overlap of \(g_n\) supplies the second factor \(m^{-1/2}\), essential
for convergence. If

\[
 p_n(\varepsilon)
 =n\sum_{k=1}^n{n-1\choose k-1}{(-1)^{k-1}\over k\varepsilon^k},
\]

the prime–Laguerre formula gives

\[
 A_n-\lambda_n
 =\lim_{\varepsilon\downarrow0}
 \left[{1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
       -p_n(\varepsilon)\right].                               \tag{6c}
\]

Thus, the rigorous version of the proposed ratio is the bound on **a
single renormalized ray**

\[
 \lambda_n\ge cA_n
 \iff
 \lim_{\varepsilon\downarrow0}
 \left[{1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
       -p_n(\varepsilon)\right]\le(1-c)A_n.                    \tag{6d}
\]

This is exactly the already-known prime–Laguerre formula, now expressed as
the diagonal coefficient of the reproducing kernel at the hard boundary.
There is not yet a closed renormalized operator built around that form.

## 3. Why there is no archimedean Rayleigh quotient

Condition

\[
 \lambda_n\ge cA_n                                              \tag{7}
\]

is a ratio of two **numbers** on vector (2). To turn it into a Rayleigh
quotient and speak of spectral projectors one needs a positive form
\(\mathsf A\) and a self-adjoint operator \(\mathsf P\) such that, with the
same normalization and uniformly in \(n\),

\[
 \langle g_n,\mathsf A g_n\rangle=A_n,
 \qquad
 \langle g_n,\mathsf P g_n\rangle=A_n-\lambda_n.                \tag{8}
\]

The existing forms do not simultaneously satisfy (8):

1. The operator of phases 62–69 is defined in an interior gauge
   \(y>1/2\), typically at large \(t_0\), and uses a different
   archimedean/prime split. Vector (2) lives exactly at
   \(y=1/2,t_0=0\), where the pole of \(\zeta\) requires Abel cancellation
   before separating the channels.
2. The Laguerre-elements proposition of the ledger for the interior gauge
   is a diagonalization of the Szegő leading term with an effective
   remainder; it is not an exact isometry that transports (7) to the
   boundary.
3. The natural Toeplitz polarization of \(A_n\) is not positive. Its
   diagonal is

   \[
    t_0(A)=A_1=1-\frac12(\gamma+\log4\pi)<0,                    \tag{9}
   \]

   since \(\gamma>0\) and \(\log(4\pi)>2\). So \(T_N(A)\) admits no
   \(T_N(A)^{-1/2}\), even though the scalar
   \({\bf1}_n^*T_n(A){\bf1}_n=A_n\) is positive for \(n\ge8\).
4. Whitening with the reference Gram matrix \(G_N>0\) is indeed possible,
   but then \(\langle g_n,G_Ng_n\rangle=n\), not \(A_n\asymp(n/2)\log n\).
   That ratio measures \(2\lambda_n/n\), whose threshold corresponding to
   (7) grows like \(c\log n\); it is not a fixed spectral layer near
   \(1\).

The negativity in (9) is the minimal version of the boundary stop-gate of
103_25: positivity on the prefixes does not extend to positivity of the
polarization, and the prefixes generate the whole space of polynomials.

## 4. The overlap diagnostic that is not licit to run

It is not faithful to compute

\[
 {|\langle g_n,v_{\max}(S\mathcal P_\Lambda S)\rangle|
  \over\|g_n\|}
\]

with the interior operator of phases 62–69 and read it as information
about \(\lambda_n/A_n\): neither \(g_n\), nor \(S\), nor the split of (8)
have been exactly transported to the same gauge.

Even after building such a transport, projecting only onto
\([1-\delta,1]\) would be insufficient without a prior spectral ceiling. An
off-line zero can create spectrum above \(1\); ignoring
\((1,\infty)\) would eliminate precisely the falsifier. The minimal
projector a proof should control is

\[
 P_{[1-\delta,\infty)},                                         \tag{10}
\]

with its spectral weight, and it must reproduce, for an off-line quartet,
the term

\[
 8-8\cosh(n\alpha)\cos(n\theta).                               \tag{11}
\]

## 5. Live successor

Non-alignment can only be reopened after proving a **boundary-transfer
theorem**:

* build, for \(\varepsilon>0\), a positive polarization
  \(\mathsf A_\varepsilon\), the coupled arithmetic operator, and the
  vector \(g_{n,\varepsilon}\);
* prove that its two forms converge, jointly and with constants uniform in
  \(n\), to the two scalars of (8);
* control the spectral mass of \(g_{n,\varepsilon}\) on
  \([1-\delta,\infty)\), not just one eigenvector;
* make the estimate fail for falsifier (11).

Without that theorem, "non-alignment" is not yet a mechanism: it is a
spectral reinterpretation of the sought proportional bound.

The heuristic claim that the prime/archimedean ratio of the real vector is
\(O(n^{-1/2})\) is justified only under RH (by the conditional asymptotics
of the Li coefficients). It cannot be used as an unconditional input to
validate the mechanism.

## Status

* **Proved:** the exact bridge \(g_n\leftrightarrow{\bf1}_n\), identities
  (3a)–(3b), the renormalized prime–pole form (6c), the Toeplitz identity
  (5), and the stop-gate (9) against the natural archimedean whitening.
* **Duplication identified:** the fixed vector is the Dirichlet–Fejér form
  already audited in 103_24–103_26.
* **Deliberately not run:** overlaps with the interior operator; they do
  not represent \(\lambda_n/A_n\).
* **Open:** a regulated positive polarization with uniform transfer to the
  boundary, or a direct scalar bound on the ray \(g_n\).
</content>
