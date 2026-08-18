# D.221 — A (0.7) safe-capacity allowance at (T=\frac12\log6)

## Verdict

The unpaid safe-tail correction in D.220 is controlled by one normalized
capacity.  In the notation of the exact three-block matrix

\[
 \mathcal A=
 \begin{pmatrix}
 K&0&C_G\\
 0&B&C_S\\
 C_G^*&C_S^*&A
 \end{pmatrix},
 \qquad A\ge\delta I,
\]

define

\[
 \rho:=\left\|A^{-1/2}C_S^*B^{-1/2}\right\|^2.     \tag{0.1}
\]

Then, for (0\leq\rho<1),

\[
 \boxed{
 K-{1\over\delta(1-\rho)}H_G>0
 \quad\Longrightarrow\quad
 \mathcal A>0,}                                     \tag{0.2}
\]

where (C_GC_G^*\le H_G).  This is a **PROVED OPERATOR
INEQUALITY**.

At (T=\frac12\log6), the native directed calculation certifies

\[
 \boxed{K-{1\over0.2199(1-0.7)}H_G>0.}              \tag{0.3}
\]

Consequently the full endpoint will follow from the single source-defined
estimate

\[
 \boxed{
 \left\|A_{QQ}^{-1/2}C_S^*B_{SS}^{-1/2}\right\|^2\le0.7.}       \tag{0.4}
\]

Equation (0.4) is not proved here.  It is now the exact minimal local target;
the graph-to-tail budget, the finite compression and the infinite gap have
already been paid with directed intervals.

## 1. Exact elimination of the tail

First assume all blocks are bounded and (A>0).  Put

\[
 U=A^{-1/2}C_G^*:G\longrightarrow Q,
 \qquad
 V=A^{-1/2}C_S^*:S\longrightarrow Q.                \tag{1.1}
\]

Shorting (A) gives

\[
 \begin{pmatrix}
 K-U^*U&-U^*V\\
 -V^*U&B-V^*V
 \end{pmatrix}.                                    \tag{1.2}
\]

Let (W=VB^{-1/2}).  The definition (0.1) says

\[
 W^*W\le\rho I_S.                                  \tag{1.3}
\]

Therefore

\[
 B-V^*V=B^{1/2}(I-W^*W)B^{1/2}>0                  \tag{1.4}
\]

when (\rho<1).  Shorting (1.4) in (1.2), the additional graph cost is

\[
 \begin{aligned}
 U^*V(B-V^*V)^{-1}V^*U
 &=U^*W(I-W^*W)^{-1}W^*U\\
 &\le {\rho\over1-\rho}U^*U.                       \tag{1.5}
 \end{aligned}
\]

Indeed the nonzero spectra of (WW^*) and (W^*W) agree, so

\[
 0\le W(I-W^*W)^{-1}W^*
 \le {\rho\over1-\rho}I_Q.                         \tag{1.6}
\]

The final graph Schur form is consequently bounded below by

\[
 K-{1\over1-\rho}U^*U.                              \tag{1.7}
\]

Since (A\ge\delta I),

\[
 U^*U=C_GA^{-1}C_G^*
 \le\delta^{-1}C_GC_G^*
 \le\delta^{-1}H_G.                                \tag{1.8}
\]

Equations (1.7)--(1.8) prove (0.2).

For closed forms, replace (A) and (B) by their positive resolvent
regularizations, apply the bounded argument and pass monotonically to the
form limit.  Finiteness of (0.1) supplies the supported-range conditions;
if it fails, the capacity is infinite and (0.4) is false rather than
silently defined by a pseudoinverse.

## 2. Directed numerical allowance

D.220 supplies native Arb balls for (K) and (H_G).  The complement gap
is used only through the strict rational lower bound

\[
 \delta=0.2199.
\]

For the conservative allowance (\rho=0.7), the denominator in (0.2) is

\[
 \delta(1-\rho)=0.06597.
\]

At (900) decimal digits, the cancellation-free D.172 evaluation gives
centre eigenvalues

\[
 8.69151333\,10^{-18},\qquad1.29694598\,10^{-14}
\]

for the matrix in (0.3).  A frozen Cholesky congruence followed by Arb
Gershgorin has lower endpoints

\[
 0.9999835909885916\ldots,
 \qquad
 0.9999886164946187\ldots,
\]

both strictly positive.  This is a **FINITE INTERVAL CERTIFICATE**, not a
numerical conjecture.

The reproduction command is

```bash
PYTHONPATH=/tmp/rowd-flint \
D172_DPS=900 D172_M=140 D172_K=2 D172_X=6 \
D172_DELTA=.06597 \
D172_GRAPH=/tmp/t6_v200_directed_graph2_native100.npz \
D172_SAVE=/tmp/t6_v200_totalgram2_rho07_d900.npz \
python3 114_d_172_directed_contracted_gram.py
```

It exits with code zero.  The output artifact has SHA-256

```text
ee9969a8c6992cb779aa29eadbe9d95ba38411daedfbcc4e5eab59ecd0982de1
```

## 3. Exact next task

The endpoint problem is no longer an unspecified three-block Feshbach
calculation.  It is (0.4).  By D.210, for any source-defined finite trial
space (W\subset Q), the capacity in (0.4) has the exact decomposition

\[
 C_SA^{-1}C_S^*=G_W+R_W^*\Sigma_W^{-1}R_W.          \tag{3.1}
\]

Thus the next certificate must:

1. retain (G_W) exactly;
2. bound only the corrected residual (R_W) by the final-tail gap;
3. prove that the largest generalized eigenvalue relative to (B) is at
   most (0.7).

This is strictly sharper than bounding the raw safe coupling by
(0.2199^{-1}C_SC_S^*), a route already refuted in D.209.

## 4. Classification

* operator implication (0.2): **PROVED**;
* directed allowance (0.3): **CERTIFIED BY INTERVALS**;
* reduction of the full endpoint to (0.4): **PROVED**;
* safe capacity bound (0.4): **OPEN**;
* full endpoint (T=\frac12\log6): **OPEN pending only (0.4)**;
* global row D: **OPEN**.
