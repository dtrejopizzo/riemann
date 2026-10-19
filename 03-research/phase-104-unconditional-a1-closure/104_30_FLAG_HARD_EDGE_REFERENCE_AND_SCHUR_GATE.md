# 104_30 — Positive flag reference and the hard-edge spectral gate

**Role.** Build the regulated prime–pole form missing from 104_28,
polarize it exactly in the Laguerre basis, and look for a positive
reference evaluating \(A_n\) on every ray \(g_n\), \(n\ge150\).

The construction exists. The positive reference is a diagonal flag form,
not the local archimedean channel. It produces an exact spectral ratio on
every finite section and allows running the spectral-mass diagnostic in
the correct gauge. The diagnostic is favorable up to \(N=500\), but it is
not a certificate. Direct Gershgorin–Schur bounds lose the cancellation
before that point and, analytically, require controlling precisely the
second differences of \(A_n-\lambda_n\).

This document proves neither A1 nor RH.

## 1. Regulated prime–pole form

Let

\[
 \phi_k(x)={\bf1}_{x\ge0}e^{-x/2}L_k(x),
 \qquad
 g_n=\sum_{k=0}^{n-1}\phi_k,
\]

and let

\[
 (S_a h)(x)={\bf1}_{x\ge a}h(x-a).
\]

We polarize the semigroup via

\[
 \mathsf B_a(g,h)
 ={1\over2}\left(
   \langle S_ag,h\rangle+\langle g,S_ah\rangle
 \right).                                                     \tag{1}
\]

For \(\varepsilon>0\), set
\(\alpha=\frac12-\varepsilon\) and define

\[
 \boxed{
 \mathsf Q_\varepsilon(g,h)
 =\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
       \mathsf B_{\log m}(g,h)
  -\int_0^\infty e^{\alpha a}\mathsf B_a(g,h)\,da.}            \tag{2}
\]

Combination (2), not its two terms after removing the regulator, is the
correct object. The identity of 104_28

\[
 \langle S_ag_n,g_n\rangle
 =e^{-a/2}L_{n-1}^{(1)}(a)                                    \tag{3}
\]

gives

\[
 \begin{aligned}
 \mathsf Q_\varepsilon[g_n]
 =P_{n,\varepsilon}
 :={}&\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_{n-1}^{(1)}(\log m)\\
 &-\int_0^\infty e^{-\varepsilon a}
       L_{n-1}^{(1)}(a)\,da .
 \end{aligned}                                                 \tag{4}
\]

The prime–Laguerre formula proves

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}P_{n,\varepsilon}
 =B_n:=A_n-\lambda_n.}                                        \tag{5}
\]

The second term of (4) is exactly

\[
 p_n(\varepsilon)
 =n\sum_{j=1}^n
   {n-1\choose j-1}{(-1)^{j-1}\over j\varepsilon^j}.           \tag{6}
\]

### 1.1 Closedness at fixed regulator

For

\[
 \mathcal H_\eta=L^2((0,\infty),e^{2\eta x}dx),
 \qquad
 \alpha<\eta<{1\over2},
\]

one has

\[
 |\mathsf B_a(g,h)|
 \le e^{-\eta a}\|g\|_\eta\|h\|_\eta.                          \tag{7}
\]

Writing

\[
 \delta=\eta-\alpha\in(0,\varepsilon),
\]

equation (7) proves that \(\mathsf Q_\varepsilon\) is a bounded, hence
closed, symmetric form, and

\[
 \|\mathsf Q_\varepsilon\|
 \le -{\zeta'\over\zeta}(1+\delta)+{1\over\delta}.              \tag{8}
\]

No uniform transfer is obtained from (8): the admissible interval for
\(\eta\) collapses as \(\varepsilon\downarrow0\). Moreover,
\(\|g_n\|_\eta^2\) has scale

\[
 \binom{2n-2}{n-1}
 [\,2(\varepsilon-\delta)\,]^{-(2n-1)},                        \tag{9}
\]

and optimizing (8)–(9) separately produces a loss of order
\(n\varepsilon^{-2n}\). This is another form of the Abel cancellation that
cannot be separated.

## 2. The regulated form is indefinite

The global positivity sought in 104_28 does not exist even before taking
the limit. Let

\[
 u_\delta=\delta^{-1/2}{\bf1}_{[0,\delta]},
 \qquad
 0<\delta<\log2.
\]

There is no prime overlap, and

\[
 \mathsf Q_\varepsilon[u_\delta]
 =-I_0,
 \qquad
 I_0={e^{\alpha\delta}-1-\alpha\delta
          \over\delta\alpha^2}>0,                              \tag{10}
\]

with the continuous value \(I_0=\delta/2\) when \(\alpha=0\).

Now let \(L=\log2\) and

\[
 v_\delta={u_\delta+S_Lu_\delta\over\sqrt2},
 \qquad
 \delta<\min(\log2,\log(3/2)).
\]

Only the atom \(m=2\) overlaps the two boxes, and

\[
 \mathsf Q_\varepsilon[v_\delta]
 ={\log2\over2^{3/2+\varepsilon}}-I_0-I_L,
 \qquad
 I_L={e^{\alpha L}\bigl(\cosh(\alpha\delta)-1\bigr)
          \over\delta\alpha^2}.                               \tag{11}
\]

Since \(I_0+I_L=O_\varepsilon(\delta)\), expression (11) is positive for
sufficiently small \(\delta\). Equations (10)–(11) prove that
\(\mathsf Q_\varepsilon\) is indefinite for every
\(\varepsilon>0\). This rules out a reference obtained by declaring the
prime–pole channel positive.

## 3. Exact Toeplitz matrix and algebraic limit

The Laguerre translation identity is

\[
 \langle S_a\phi_j,\phi_k\rangle
 =
 \begin{cases}
 e^{-a/2}L_{k-j}^{(-1)}(a),&k\ge j,\\
 0,&k<j.
 \end{cases}                                                   \tag{12}
\]

Hence (2) is Toeplitz on every finite section:

\[
 \mathsf Q_\varepsilon(\phi_j,\phi_k)
 =q_{|j-k|}(\varepsilon),                                     \tag{13}
\]

where

\[
 \boxed{
 q_0(\varepsilon)
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
   -{1\over\varepsilon}
 =-{\zeta'\over\zeta}(1+\varepsilon)-{1\over\varepsilon}}      \tag{14}
\]

and, for \(d\ge1\),

\[
 \boxed{
 q_d(\varepsilon)
 ={1\over2}\left[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_d^{(-1)}(\log m)-I_d(\varepsilon)
 \right],}                                                     \tag{15}
\]

\[
 \boxed{
 I_d(\varepsilon)
 =\int_0^\infty e^{-\varepsilon a}L_d^{(-1)}(a)\,da
 ={(-1)^d(1-\varepsilon)^{d-1}\over\varepsilon^{d+1}}.}        \tag{16}
\]

The generating function

\[
 \sum_{d\ge0}L_d^{(-1)}(a)t^d
 =\exp\left(-{at\over1-t}\right)
\]

proves (16). If \(F(s)=-\zeta'(s)/\zeta(s)\), the prime sum of
(15) can also be written, with no truncation, as

\[
 \sum_{j=1}^d
 {1\over j!}{d-1\choose j-1}F^{(j)}(1+\varepsilon).            \tag{17}
\]

The divergences of (16) and (17) cancel only in their difference.

From (4) and (13),

\[
 P_{n,\varepsilon}
 =nq_0(\varepsilon)
  +2\sum_{d=1}^{n-1}(n-d)q_d(\varepsilon).                    \tag{18}
\]

Let \(B_0=0\). Triangular inversion of (18) and (5) gives the
entry-by-entry limit

\[
 \boxed{
 q_0=B_1=-\gamma,
 \qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).}                \tag{19}
\]

Form \(\mathsf Q_0=[q_{|j-k|}]\) is thus defined on the algebraic space of
finitely supported sequences. It is not claimed to be closable in
\(L^2(0,\infty)\), nor that (8) survives the limit.

## 4. Positive reference evaluating \(A_n\)

Fix \(M=150\) and use the orthogonal, non-normalized basis

\[
 b_0=g_M,
 \qquad
 b_r=\phi_{M+r-1}\quad(r\ge1).                                \tag{20}
\]

For

\[
 v=a_0g_M+\sum_{k\ge M}a_k\phi_k
\]

define the diagonal flag form

\[
 \boxed{
 \mathsf A_{\rm flag}[v]
 =A_M|a_0|^2
  +\sum_{k\ge M}(A_{k+1}-A_k)|a_k|^2.}                        \tag{21}
\]

This form is positive and closed on its diagonal domain. Indeed,
\(A_M>0\), and if

\[
 \Delta A_n=A_{n+1}-A_n,
\]

then

\[
 \Delta^2 A_n
 :=A_{n+2}-2A_{n+1}+A_n
 =\sum_{\substack{r\ge1\\r\ {\rm odd}}}
   {(1-1/r)^n\over r^2}>0.                                   \tag{22}
\]

So \(\Delta A_n\) is increasing. The positive value at the finite
threshold implies \(\Delta A_k>0\) for \(k\ge M\).

Since

\[
 g_n=g_M+\sum_{k=M}^{n-1}\phi_k
 \qquad(n\ge M),                                               \tag{23}
\]

telescoping gives

\[
 \boxed{\mathsf A_{\rm flag}[g_n]=A_n.}                        \tag{24}
\]

Construction (21) resolves the type of problem found in 104_28, but must
be read with care: it is a nonlocal reference built from the sequence
\(A_n\). It does not identify the Gamma–pole channel with a positive form
and by itself produces no inequality for \(\mathsf Q_0\).

## 5. Exact matrix in the flag basis

On the section

\[
 \mathcal V_{M,N}
 =\mathrm{span}\,\{g_M,\phi_M,\ldots,\phi_{N-1}\},         \tag{25}
\]

the matrix of \(\mathsf A_{\rm flag}\) is

\[
 D_{M,N}
 =\mathrm{diag}
   (A_M,\Delta A_M,\ldots,\Delta A_{N-1})>0.                  \tag{26}
\]

The matrix of \(\mathsf Q_0\) is completely explicit. For
\(M\le k,l<N\),

\[
 \begin{aligned}
 \mathsf Q_0(g_M,g_M)&=B_M,\\
 \mathsf Q_0(\phi_k,\phi_l)&=q_{|k-l|},\\
 \mathsf Q_0(g_M,\phi_k)
 &=s_k:=\sum_{d=k-M+1}^{k}q_d\\
 &={1\over2}\left[
     (B_{k+1}-B_k)
     -(B_{k-M+1}-B_{k-M})
   \right].
 \end{aligned}                                                 \tag{27}
\]

**Index check for (27).** For \(k=M\), the sum is
\(\sum_{d=1}^{M}q_d\), and the second increment of the last line is
\(B_1-B_0\). For \(k=M+r\), the indices are
\(d=r+1,\ldots,M+r\). So the term \(q_0\) is neither missing nor
duplicated.

The same equations hold for \(\varepsilon>0\), replacing \(B_n\)
by \(P_{n,\varepsilon}\).

We define the whitened matrix

\[
 \boxed{
 K_{M,N}=D_{M,N}^{-1/2}Q_{M,N}D_{M,N}^{-1/2}.}                 \tag{28}
\]

If \(x_n=(1,\ldots,1,0,\ldots,0)\) are the coordinates of (23), the
correct unit vector is

\[
 u_n={D_{M,N}^{1/2}x_n\over\sqrt{A_n}},                        \tag{29}
\]

and

\[
 \boxed{
 \|u_n\|^2=1,
 \qquad
 \langle u_n,K_{M,N}u_n\rangle
 ={B_n\over A_n}
 =1-{\lambda_n\over A_n}.}                                    \tag{30}
\]

So \(\lambda_n\ge cA_n\) is equivalent to the specific spectral average of
\(u_n\) being at most \(1-c\). For the scale-free statement, any
\(c>1/4\) suffices. The choice \(c=501/2002\) of 104_26 requires the
exact ceiling

\[
 1-c={1501\over2002}=0.7497502497\ldots,
\]

slightly less than \(3/4\).

Controlling only the mass on \([3/4,\infty)\) is not enough without
control of the spectral tail: the relevant equality is the full first
moment of (30). The diagnostic therefore records mass, excess moment, and
expectation.

## 6. Reproducible diagnostic

The file **tools/flag_hard_edge_spectrum.py** uses
**lambda_arch** and two Cauchy/FFT extractions of **li_lambda**. It
verifies, for each \(M\le n\le N\), identities (24), (27), and (30),
diagonalizes (28), and computes the spectral mass of each \(u_n\) on
\([3/4,\infty)\). Reproduced with

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 flag_hard_edge_spectrum.py --nmax 500 \
      --sections 200 250 300 350 400 500

Double-precision, uncertified results:

| \(N\) | \(\lambda_{\min}(K)\) | \(\lambda_{\max}(K)\) | Gershgorin sup. | weighted Schur |
|---:|---:|---:|---:|---:|
| 200 | \(-0.363476\) | \(0.033546\) | \(0.118739\) | \(0.711902\) |
| 250 | \(-0.363476\) | \(0.066179\) | \(0.279405\) | \(0.763377\) |
| 300 | \(-0.363476\) | \(0.091360\) | \(0.497693\) | \(0.821868\) |
| 350 | \(-0.363476\) | \(0.108870\) | \(0.726895\) | \(0.898923\) |
| 400 | \(-0.363477\) | \(0.125661\) | \(0.924004\) | \(1.000074\) |
| 500 | \(-0.363479\) | \(0.166149\) | \(1.193387\) | \(1.207775\) |

At \(N=500\), the maximum discrepancy between radii \(0.985\) and
\(0.975\) in the \(\lambda_n\) was \(5.1\cdot10^{-9}\); the maximum
discrepancy between eigenvalues was \(4.2\cdot10^{-12}\).
No spectrum appeared in \([3/4,\infty)\), so the mass of every
\(u_n\) there was zero.

This is evidence that the fixed vector is not near the threshold in that
range. It is not asymptotic evidence and certifies no statement for every
\(n\): both radii share the Borwein evaluation, the FFT, and
**float64** arithmetic.

## 7. Gershgorin and Schur gate

With

\[
 a_0=A_M,
 \qquad
 a_k=\Delta A_k\quad(M\le k<N),
\]

the Gershgorin upper extremes are

\[
 \begin{aligned}
 G_0
 &={B_M\over A_M}
   +\sum_{k=M}^{N-1}{|s_k|\over\sqrt{A_M\Delta A_k}},\\
 G_k
 &={q_0\over\Delta A_k}
   +{|s_k|\over\sqrt{A_M\Delta A_k}}\\
 &\quad
   +\sum_{\substack{M\le l<N\\l\ne k}}
       {|q_{|k-l|}|\over\sqrt{\Delta A_k\Delta A_l}}.
 \end{aligned}                                                 \tag{31}
\]

**Index check for (31).** Index \(k\) labels row
\(\phi_k\), \(M\le k<N\). Its diagonal entry is
\(q_{|k-k|}/\Delta A_k=q_0/\Delta A_k\); the term \(s_k\) is the only
entry against \(g_M\); and the sum over \(l\ne k\) contains exactly the
remaining rows \(\phi_l\). There is no double counting.

With Schur weights \(w_i=\sqrt{a_i}\), the bound simplifies to

\[
 \begin{aligned}
 S_0
 &={|B_M|+\sum_{k=M}^{N-1}|s_k|\over A_M},\\
 S_k
 &={|s_k|+|q_0|
       +\sum_{\substack{M\le l<N\\l\ne k}}|q_{|k-l|}|
       \over\Delta A_k}.
 \end{aligned}                                                 \tag{32}
\]

To avoid an index ambiguity, define the centered second difference

\[
 \nabla_c^2 B_d:=B_{d+1}-2B_d+B_{d-1}\qquad(d\ge1).
\]

The exact arithmetic coefficient required by (31)–(32) is

\[
 \boxed{
 q_d={1\over2}\nabla_c^2(A-\lambda)_d
 ={1\over2}\nabla_c^2A_d
  -{1\over2}\nabla_c^2\lambda_d.}                              \tag{33}
\]

Hence a proof via (31) or (32) needs a signed or summable bound for the
centered second differences of \(\lambda_n\), or a direct estimate of the
prime–pole difference in (15). Replacing it with absolute values
eliminates the interference that A1 needs.

The diagnostic makes the loss visible: Gershgorin already exceeds
\(3/4\) between \(N=350\) and \(N=400\), and Schur does so even earlier,
while the observed top eigenvalue remains below \(0.13\). The row bound
does not capture the matrix cancellation even within the tested range.

## Status

* **Proved:** the closed regulated form for \(\varepsilon>0\), explicit
  indefiniteness, the Toeplitz matrix (14)–(18), the algebraic limit
  (19), the positive flag reference (21)–(24), and the exact whitened
  matrix (27)–(30).
* **Diagnostically verified:** all identities up to \(N=500\), stability
  between two radii, and absence of spectrum above
  \(3/4\) in those sections.
* **Ruled out as a direct estimate:** absolute Gershgorin–Schur row
  bounds; they lose the margin before \(N=400\).
* **Not proved:** uniform control of \(K_{M,N}\), uniform spectral
  non-alignment of \(u_n\), A1, and RH.
* **Minimal remaining coefficient:** a non-absolute estimate for
  \(q_d=\frac12\nabla_c^2(A-\lambda)_d\), keeping the joint cancellation
  of (15), or a direct estimate of the first moment (30) over the fixed
  family \(u_n\).
</content>
