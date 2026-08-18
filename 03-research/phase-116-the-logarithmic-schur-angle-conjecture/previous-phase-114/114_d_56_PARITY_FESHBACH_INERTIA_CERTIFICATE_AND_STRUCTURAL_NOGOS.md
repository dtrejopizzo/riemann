# D.56 — Parity--Feshbach inertia certificate and structural no-go results

## 1. Purpose

D.55 isolates every possible positive direction of `B_nuc` in an explicit
finite prolate Schur core.  This note uses the exact reflection symmetry to
split that core into even and odd channels and derives a finite certificate
which, if verified, proves simultaneously

\[
 n_+(B_T)=1,
 \qquad
 \operatorname{In}(M_TB_T^{-1}M_T^*)=(1,1,0).             \tag{1.1}
\]

The certificate includes all prime powers and the complete Gamma term
through the multiplier and Schur complement of D.55.  It is suitable for
rigorous interval verification, including an explicit error contribution
from the eliminated high modes.

Two tempting purely structural shortcuts are disproved exactly first:
being `mass minus a connected Gram energy` does not force index one, and
index one alone does not force a hyperbolic boundary Green matrix.

No RH, Weil positivity or screw positivity is assumed.  The certificate is
not claimed to have been verified for every `T`.

## 2. Exact reflection splitting

Let `J F(t)=F(-t)`.  Every source term commutes with `J`:

1. the Gamma multiplier is even in frequency;
2. each finite-place term occurs as `S_a+S_(-a)`;
3. the prolate concentration kernel depends only on `t-s` and is even.

Consequently the D.55 core `E_T`, its complement `Q_T`, the high inverse and
the Schur matrix all split:

\[
 E_T=E_{T,e}\oplus E_{T,o},qquad
 S_T=S_{T,e}\oplus S_{T,o}.                               \tag{2.1}
\]

The two normalized ruling vectors split in the same way:

\[
 u_e\sim e^{t/2}+e^{-t/2}=2\cosh(t/2),
 \qquad
 u_o\sim e^{t/2}-e^{-t/2}=2\sinh(t/2).                    \tag{2.2}
\]

Thus the boundary Green matrix is diagonal in parity.  There is no
off-channel term to estimate.

## 3. Why the global Gram factorization is insufficient

The complete source operator has the exact form

\[
 B_T=m_TI-\mathcal D_T^*\mathcal D_T,                     \tag{3.1}
\]

where `mathcal D_T` contains every weighted graph difference
`sqrt(c_(p,k))(I-S_(k log p))` and every Gamma feature
`a_j^(-1/2)R_j`.  This is useful, but it does not imply index one.

An exact three-vertex counterexample is the connected path incidence
matrix.  Its Gram Laplacian is

\[
 L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},
 \qquad \operatorname{spec}(L)=\{0,1,3\}.                 \tag{3.2}
\]

For `m=2`,

\[
 \operatorname{spec}(2I-L)=\{2,1,-1\},                   \tag{3.3}
\]

so the positive index is two despite positivity of the energy, connected
interaction graph and a simple ground state.  Hence a proof must establish
a quantitative second singular-value bound for the *arithmetic* feature
map; connectivity and Perron--Frobenius simplicity are not enough.

## 4. Why index one is insufficient for the jets

Let

\[
 B_e=\operatorname{diag}(1,-1),\quad u_e=(0,1),
 \qquad B_o=(-2),\quad u_o=1.                              \tag{4.1}
\]

Then the total operator has exactly one positive eigenvalue, but

\[
 \langle u_e,B_e^{-1}u_e\rangle=-1,
 \qquad
 \langle u_o,B_o^{-1}u_o\rangle=-1/2.                     \tag{4.2}
\]

The boundary Green matrix is negative definite, not hyperbolic.  The
example is parity diagonal and shows the exact persistent-eigenvalue
obstruction: the unique positive mode may fail to couple to the even jet.
Thus the jet signature needs an independent coupling estimate.

## 5. The finite parity inertia certificate

In each parity channel `epsilon in {e,o}`, write the D.55 decomposition as

\[
 B_\epsilon=
 \begin{pmatrix}A_\epsilon&C_\epsilon\\
 C_\epsilon^*&D_\epsilon\end{pmatrix},
 \qquad D_\epsilon\leq-\eta/2,                            \tag{5.1}
\]

and put

\[
 S_\epsilon=A_\epsilon-C_\epsilon
 D_\epsilon^{-1}C_\epsilon^*.                             \tag{5.2}
\]

The odd certificate is simply

\[
 \boxed{S_o<0.}                                            \tag{5.3}
\]

For the even core, choose a normalized, source-defined anchor `v`—the
normalized core projection of `cosh(t/2)` is the canonical choice—and let
`P_v=|v><v|`, `Q_v=I-P_v`.  Define

\[
 a=\langle v,S_ev\rangle,
 \quad b=Q_vS_ev,
 \quad D_v=Q_vS_eQ_v.                                     \tag{5.4}
\]

The even certificate is

\[
 \boxed{D_v<0,qquad
 \sigma_e:=a-\langle b,D_v^{-1}b\rangle>0.}               \tag{5.5}
\]

Gaussian elimination gives

\[
 S_e\sim \sigma_e\oplus D_v.                              \tag{5.6}
\]

Therefore (5.3)--(5.5) imply

\[
 n_+(B_o)=0,qquad n_+(B_e)=1,qquad n_+(B_T)=1.           \tag{5.7}
\]

Equivalently, (5.5) supplies the desired `rank one minus positive`
factorization after the displayed congruence.  Unlike an assumed global
factorization, every term in (5.5) is a finite matrix or a certified high
Schur correction.

## 6. Exact jet formula after eliminating high modes

Decompose the parity jet as

\[
 u_\epsilon=p_\epsilon\oplus q_\epsilon
 \in E_{T,\epsilon}\oplus Q_{T,\epsilon}.                 \tag{6.1}
\]

The block inverse formula gives

\[
 \boxed{
 g_\epsilon:=\langle u_\epsilon,B_\epsilon^{-1}u_\epsilon\rangle
 =\langle\widetilde p_\epsilon,
 S_\epsilon^{-1}\widetilde p_\epsilon\rangle
 +\langle q_\epsilon,D_\epsilon^{-1}q_\epsilon\rangle,}  \tag{6.2}
\]

where

\[
 \widetilde p_\epsilon
 =p_\epsilon-C_\epsilon D_\epsilon^{-1}q_\epsilon.       \tag{6.3}
\]

If (5.3) holds, both terms in (6.2) are strictly negative for the odd
channel unless the odd jet vanishes, which it does not.  Hence

\[
 g_o<0.                                                     \tag{6.4}
\]

For the even channel the high contribution is negative but explicitly
bounded:

\[
 -{2\over\eta}\|q_e\|^2
 \leq\langle q_e,D_e^{-1}q_e\rangle<0.                    \tag{6.5}
\]

It is therefore enough to certify the finite inequality

\[
 \boxed{
 \langle\widetilde p_e,S_e^{-1}\widetilde p_e\rangle
 >{2\over\eta}\|q_e\|^2.}                                \tag{6.6}
\]

Then `g_e>0>g_o`, so the ruling Green matrix has signature `(1,1)`.
Equations (5.3), (5.5) and (6.6) are a complete finite certificate for the
direct D.47 gate at a fixed window.

## 7. Determinant and LDL versions

For exact or interval arithmetic, matrix inversion in (5.5) is optional.
Choose a parity-adapted ordered basis beginning with `v`.  A symmetric
`LDL^*` factorization of `S_e` and `S_o` proves the same statements:

1. every odd pivot is negative;
2. exactly one even pivot is positive and all remaining even pivots are
   negative;
3. no pivot interval contains zero.

Equivalently, after a fixed symmetric pivot order, the signs of the ratios
of successive principal determinants give the inertia.  Symmetric pivoting
is essential: the arithmetic shift matrices are dense and have no fixed
Jacobi sign pattern, so unpivoted leading minors are not intrinsically
ordered.

The D.55 residual estimate

\[
 \|D_\epsilon^{-1}r\|\leq2\|r\|/\eta                     \tag{7.1}
\]

gives interval enclosures for all Feshbach entries.  The same estimate
controls the effective jets (6.3).  Thus (5.3), (5.5) and (6.6) can be
machine-certified without truncating any prime power or Gamma tail.

## 8. Oscillation audit

A classical discrete Sturm proof would require a tridiagonal Jacobi matrix
with sign-definite nearest-neighbor entries.  The actual core does not have
that structure:

* every displacement `k log p` contributes a different dense compressed
  shift matrix;
* the Gamma multiplier gives another dense parity block;
* D.53 exhibits both crossing signs for a single symmetrized displacement.

Therefore ordinary nodal interlacing cannot be invoked.  A new oscillation
theorem would have to apply to the complete arithmetic feature matrix and
prove exactly the second singular-value gap encoded by (5.5).  Calling the
matrix oscillatory without proving the relevant minors would simply assume
the missing sign.

## 9. Remaining global task

The finite certificate genuinely attacks the two requested inertias and
separates their logically independent parts:

\[
 \begin{array}{c|c}
 \text{required fact}&\text{finite source certificate}\\ \hline
 n_+(B_o)=0&S_o<0\\
 n_+(B_e)=1&D_v<0,\ \sigma_e>0\\
 g_o<0&\text{automatic from }S_o<0\\
 g_e>0&\text{inequality (6.6)}
 \end{array}                                               \tag{9.1}
\]

What remains is to verify these inequalities for every `T`, with interval
control through the discrete prime-power thresholds and uniform control on
compact `T`-ranges.  D.55 proves that this is finite at each stage and that
no uncontrolled ultraviolet mode is omitted.  D.56 does not prove the
required signs uniformly in `T`; declaring them from Weil positivity would
be circular.

## 10. Verdict

Neither the global Gram representation nor ground-state simplicity forces
the desired inertia, and index one does not force the jet signature.  The
exact surviving structure is parity plus Feshbach elimination.  It reduces
row D at each window to three explicit finite inequalities, (5.3), (5.5)
and (6.6), containing all prime powers and the complete Gamma contribution
with certified tail errors.

