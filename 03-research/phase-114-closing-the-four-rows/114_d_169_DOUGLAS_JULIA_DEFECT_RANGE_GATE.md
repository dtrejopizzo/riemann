# D.169 — Douglas--Julia defect-range gate

## Verdict

The factorization suggested by the integer-cell orthogonality,

\[
 z_N=(I-K_N)^{1/2}w_N,qquad
 \|w_N\|^2\le c_N,                                   \tag{0.1}
\]

is exactly the right theorem for D.168.  It is also exactly equivalent to
positivity of the enlarged boundary Schur block.  Consequently it cannot
be inferred merely from the existence of the Julia colligation of the old
contraction; an explicit Witt--Poisson formula for (w_N) and a proof of
(0.1) are required.

Let

\[
 D_N=I-K_N\ge0,qquad
 z_N=\Gamma_N^{-1/2}\mathcal B_N:E_N\longrightarrow H_N.            \tag{0.2}
\]

For (c_N\ge0), the following are equivalent:

\[
\begin{array}{ll}
\text{(i)}&z_N=D_N^{1/2}w_N\quad\hbox{for some }
             \|w_N\|^2\le c_N;\\
\text{(ii)}&z_Nz_N^*\le c_ND_N;\\
\text{(iii)}&
 \begin{pmatrix}c_NI_{E_N}&z_N^*\\z_N&D_N\end{pmatrix}\ge0;\\
\text{(iv)}&\operatorname {Ran}z_N\subseteq\operatorname {Ran}D_N^{1/2}
 \quad\hbox{and}\quad z_N^*D_N^\dagger z_N\le c_NI_{E_N}.
\end{array}                                                    \tag{0.3}
\]

Taking (c_N) to be the Gamma boundary capacity minus the diagonal Tate
and collision terms, (iii) is the congruent form of positivity of the new
integer cell.  This proves both the usefulness and the logical status of
(0.1).

## 1. Douglas factorization

The Douglas range lemma says that, for bounded operators (S,T),

\[
 SS^*\le cTT^*
 \quad\Longleftrightarrow\quad
 S=TW\quad\hbox{with }\|W\|^2\le c.                  \tag{1.1}
\]

Apply it with (S=z_N) and (T=D_N^{1/2}).  This proves
(i) (Longleftrightarrow) (ii), including the range condition when
(D_N) has a kernel.

Shorting the lower-right corner of the block in (iii) gives

\[
 c_NI-z_N^*D_N^\dagger z_N,                          \tag{1.2}
\]

again with (operatorname {Ran}z_N\subseteq
\operatorname {Ran}D_N^{1/2}).  The generalized Schur theorem proves
(iii) (Longleftrightarrow) (iv).  Applying the same theorem after
shorting the upper-left scalar corner gives (ii).  Hence all four
statements are equivalent.

The spectral estimate (0.5) of D.168 follows immediately from (i): for
the spectral projection (E_D([0,\epsilon])),

\[
 \|E_D([0,\epsilon])z_Ne\|^2
 =\|E_D([0,\epsilon])D_N^{1/2}w_Ne\|^2
 \le\epsilon c_N\|e\|^2.                            \tag{1.3}
\]

## 2. What the Julia operator does and does not supply

If (C_N) is an old comparison contraction and
(D_N=I-C_N^*C_N), its Julia operator is

\[
 \mathcal J(C_N)=
 \begin{pmatrix}
 C_N&(I-C_NC_N^*)^{1/2}\\
 (I-C_N^*C_N)^{1/2}&-C_N^*
 \end{pmatrix}.                                      \tag{2.1}
\]

It is unitary and therefore constructs the universal defect channel
(D_N^{1/2}).  However, (2.1) contains no map from the newly born boundary
space (E_N) into that channel.  Such a map is precisely (w_N) in
(0.1).  Assigning

\[
 w_N=D_N^{\dagger/2}z_N                              \tag{2.2}
\]

does not prove anything: (2.2) exists and is bounded exactly when the
range and norm statements in (iv) already hold.

Thus a Julia/Sz.-Nagy vocabulary alone cannot close D.  It becomes a proof
only if the A--B--C data construct (w_N) before inverting the defect and
verify

\[
 D_N^{1/2}w_N=\Gamma_N^{-1/2}\mathcal B_N            \tag{2.3}
\]

with the required norm.

## 3. Audit of the Witt--Poisson candidates

For each (n=p^k), the Hadamard rotation

\[
 \binom{J_{n,+}F}{J_{n,-}F}
 ={1\over\sqrt2}
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}
 \binom{S_{\log n}F}{F}                              \tag{3.1}
\]

is unitary before restriction to the overlap.  On an integer cell, the
restricted translates are orthogonal except for (nm=N), which gives
the exact scalar (H_N).  Therefore (3.1) explains (V_N\pm H_N) and
provides the ambient isometry needed in D.164.

What it does not do is identify the ambient antisymmetric channel with
the defect channel of the **already shorted** comparison (C_N).  Their
difference is the centered atomic measure

\[
 d\psi(x)-dx+{\beta\over2}\delta_1,                  \tag{3.2}
\]

or, in Fourier variables, (E_N=W_N-M_N).  The continuous part of
(3.2) is removed by the two Tate moments (D.137 and D.167), but the atomic
remainder is exactly the unresolved defect alignment of D.168.

Consequently the raw candidate obtained by sending each (J_+) channel
to its (J_-) partner verifies (2.3) only in the ambient Gamma--Poisson
dilation.  After old-core shorting it leaves the residual

\[
 \mathfrak r_N
 =z_N-D_N^{1/2}w_N^{\rm amb}.                         \tag{3.3}
\]

Proving (mathfrak r_N=0), or absorbing it by a second defect channel
with a summable norm budget, is equivalent to the centered Dirichlet
Carleson estimate (3.3) of D.168.  Integer-cell orthogonality bounds the
ambient norm of (3.3), but not its component in
(ker D_N) or the small-defect spectral layers.

## 4. Noncircular target

The next admissible construction must therefore provide one of:

1. an explicit (w_N=w_N^{\rm Witt}\oplus w_N^{\Gamma}) assembled from
   the old Julia channel and the centered Poisson remainder, satisfying
   (2.3) as an identity; or
2. a residual factorization

   \[
   \mathfrak r_N=D_N^{1/2}\widetilde w_N,qquad
   \|w_N^{\rm amb}\oplus\widetilde w_N\|^2\le c_N.   \tag{4.1}
   \]

The second formulation is compatible with the directed Feshbach data:
the finite endpoint-flat graph approximates (w_N^{\rm amb}), while the
safe-complement estimate must factor (mathfrak r_N), not merely bound it
in the ambient (L^2) norm.

The ancillary `114_d_169_douglas_julia_verify.py` checks all equivalences
in (0.3), the Julia unitarity (2.1), and the fact that a fixed ambient Gram
does not control the defect factor norm.
