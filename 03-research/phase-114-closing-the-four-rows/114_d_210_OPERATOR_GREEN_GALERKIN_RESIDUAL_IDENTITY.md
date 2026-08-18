# D.210 — Operator-valued Green by Galerkin residual shorting

## Verdict

The scalar-gap failure of D.209 does not require computing the entire
infinite Green operator.  There is an exact residual identity which retains
the Green geometry resolved by a finite intermediate space and applies the
remaining scalar gap only to the corrected residual.

Let (A=A^*>0) be the high/complement operator, let (W) be a finite or
closed trial subspace with projection (P), and put (Z=W^\perp), with
projection (Q).  Assume (A_{WW}=PAP) is invertible on (W).  Define

\[
S_W=A_{ZZ}-A_{ZW}A_{WW}^{-1}A_{WZ}.                 \tag{0.1}
\]

For a coupling (C:E\to W\oplus Z), write (C_W=PC), (C_Z=QC), and
define

\[
G_W=C_W^*A_{WW}^{-1}C_W,
\qquad
R_W=C_Z-A_{ZW}A_{WW}^{-1}C_W.                       \tag{0.2}
\]

Then

\[
\boxed{
C^*A^{-1}C=G_W+R_W^*S_W^{-1}R_W.
}                                                     \tag{0.3}
\]

Consequently, if (S_W\ge\delta_W I_Z),

\[
\boxed{
C^*A^{-1}C
\le G_W+\delta_W^{-1}R_W^*R_W.
}                                                     \tag{0.4}
\]

Formula (0.4) is always at least as informative as replacing all of (A)
by a scalar gap before elimination.  It is the correctly typed multilevel
Green certificate requested in D.207--D.209.

Equations (0.1)--(0.4) are **PROVED ALGEBRAIC/OPERATORIAL IDENTITIES** under
the displayed positivity hypotheses.  Their row-D application still
requires directed enclosures of (A_{WW}), (S_W), and (R_W); no
endpoint sign is asserted here.

## 1. Exact block factorization

Relative to (W\oplus Z), write

\[
A=
\begin{pmatrix}
A_{WW}&A_{WZ}\\
A_{ZW}&A_{ZZ}
\end{pmatrix}.
\]

The triangular congruence

\[
L=
\begin{pmatrix}
I&A_{WW}^{-1}A_{WZ}\\
0&I
\end{pmatrix}
\]

gives

\[
A=L^*
\begin{pmatrix}
A_{WW}&0\\0&S_W
\end{pmatrix}L.                                      \tag{1.1}
\]

Thus (A>0) if and only if (A_{WW}>0) and (S_W>0), and

\[
A^{-1}=L^{-1}
\begin{pmatrix}
A_{WW}^{-1}&0\\0&S_W^{-1}
\end{pmatrix}(L^*)^{-1}.                              \tag{1.2}
\]

Moreover

\[
(L^*)^{-1}C=
\binom{C_W}{C_Z-A_{ZW}A_{WW}^{-1}C_W}
=\binom{C_W}{R_W}.                                   \tag{1.3}
\]

Substitution of (1.3) into (1.2) proves (0.3).  Inversion reverses order,
so (S_W\ge\delta_WI) implies (S_W^{-1}\le\delta_W^{-1}I), proving
(0.4).

The same proof applies to closed coercive forms by first replacing each
block by its bounded resolvent regularization and passing monotonically to
the form limit.  The required range conditions are exactly those in the
generalized Schur theorem; no pseudoinverse is silently treated as an
ordinary inverse.

## 2. Galerkin interpretation

For (e\in E), let

\[
u_W=A_{WW}^{-1}C_We\in W,
\qquad
r_W=Ce-Au_W.
\]

The Galerkin equation (P(Au_W-Ce)=0) gives (Pr_W=0), and its (Z)
component is exactly (R_We).  Hence (0.3) reads

\[
\langle Ce,A^{-1}Ce\rangle
=\langle C_We,A_{WW}^{-1}C_We\rangle
\langle R_We,S_W^{-1}R_We\rangle.                    \tag{2.1}
\]

The first term is the energy captured by the trial space.  The second is
the exact energy of the corrected residual after the trial space has been
shorted.  Replacing it by (\delta_W^{-1}\|R_We\|^2) loses no information
already captured by (W).

By contrast, the scalar certificate of D.207/D.209 uses

\[
C^*A^{-1}C\le\delta^{-1}C^*C,                         \tag{2.2}
\]

which discards the Galerkin solution and charges the scalar worst case to
the entire coupling.  Formula (0.4) explains exactly why enlarging the
intermediate block can repair the proof route even though no internal split
can repair (2.2).

## 3. Nested monotonicity and exact increments

Let (W_1\subset W_2\subset\cdots) be a form-core exhaustion for (A),
and set

\[
G_j=C_{W_j}^*A_{W_jW_j}^{-1}C_{W_j}.
\]

Applying (0.3) inside (W_{j+1}=W_j\oplus
(W_{j+1}\ominus W_j)) gives

\[
0\le G_{j+1}-G_j
=R_{j\to j+1}^*S_{j\to j+1}^{-1}R_{j\to j+1}.       \tag{3.1}
\]

Thus (G_j) is monotone in Loewner order.  Standard Galerkin convergence
on a form core gives

\[
G_j\uparrow C^*A^{-1}C                              \tag{3.2}
\]

in quadratic forms.  This monotonicity supplies lower approximations; the
upper enclosure is obtained at a finite level from (0.4).  Therefore a
directed proof can squeeze the exact Green without ever forming an
infinite-dimensional pseudoinverse.

## 4. Exact endpoint obligation

At (T=\frac12\log6), take

\[
E=V_{200}\cap\mathcal P_T,qquad
W=(V_{600}\ominus V_{200})\cap\mathcal P_T,qquad
Z=V_{600}^\perp\cap\mathcal P_T.
\]

Here (A) is the complete primitive complement operator and (C) is the
complete finite-to-complement coupling.  The endpoint is proved if directed
arithmetic establishes

\[
B-
\left(G_W+\delta_W^{-1}R_W^*R_W\right)>0,            \tag{4.1}
\]

where (B) is the complete primitive (V_{200}) block and
(S_W\ge\delta_W I) is proved on the post-600 tail.  D.208 already supplies
a source-defined tail estimate on the endpoint-flat safe sector; the
remaining work is to build the complete directed (V_{600}) compression
and the residual (R_W) for all (198) primitive finite directions.

The same identity applies at (T=\frac12\log5), with the corresponding
finite filtration, and repairs the missing safe-block--tail term identified
in D.200.

## 5. Global threshold formulation

At a general prime-power birth, let (A_N^{\rm high}) be the true high
operator after the transported old core has been eliminated, and let
(C_N) be the born-to-high coupling.  Choose a source-defined nested form
core (W_{N,j}).  If for some finite (j=j(N)) one proves

\[
S_{N,j}\ge\delta_{N,j}I
\]

and the remaining born budget (B_N^{\rm born}) satisfies

\[
B_N^{\rm born}-
\left(G_{N,j}+\delta_{N,j}^{-1}R_{N,j}^*R_{N,j}\right)\ge0,
\tag{5.1}
\]

then the exact sharp Douglas capacity holds at that birth.  A uniform rule
for choosing (j(N)) and proving (5.1) for all sufficiently large (N)
would be the asymptotic theorem required for global propagation.

This reframes the next analytic task: not a uniform lower bound for the
whole high operator, but a uniform residual approximation theorem for the
specific born coupling in its Green metric.

## 6. Equality

If (0.4) is sharp on (e\), then equality requires simultaneously

\[
R_We\in\ker(S_W-\delta_WI)
\]

and equality in the final finite Schur form.  If the tail inequality is
strict on the range of (R_W), the equality kernel is already contained in
the finite Galerkin block.  This gives a concrete route to the row-D
equality analysis instead of postponing it until after positivity.

## 7. Classification

* (0.3), (2.1), and (3.1): **ALGEBRAIC/OPERATORIAL IDENTITIES**.
* (0.4): **PROVED SUFFICIENT INEQUALITY** under (S_W\ge\delta_WI).
* Existing endpoint-flat post-600 estimates: **CERTIFIED BY INTERVALS** only
  on their explicitly stated safe sector.
* Full endpoint inequality (4.1): **OPEN**.
* Uniform threshold theorem (5.1): **OPEN**.

