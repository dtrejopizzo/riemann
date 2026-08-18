# D.181 — Self-contained certificate for the first endpoint

## Certified statement

Let

\[
 T=\frac12\log 5
\]

and let \(A_T\) be the complete primitive operator of the A--B--C
Lefschetz form.  Then

\[
 \boxed{\langle A_Tf,f\rangle>0\quad(0\ne f\in\mathcal P_T).}
\]

This is an infinite-dimensional operator statement.  It is not an
extrapolation from the eigenvalues of a Galerkin matrix.

## Logical dependencies

The certificate uses exactly the following previously directed results.

1. **D.152 (primitive complement).**  On
   \(\mathcal P_T\cap V_{170}^{\perp}\), including the two-dimensional
   Tate defect, one has \(A_T>0.218I\).  Since
   \(V_{170}\subset V_{200}\), the same bound holds on
   \(\mathcal P_T\cap V_{200}^{\perp}\).
2. **D.166 (finite nested Schur reduction).**  The directed decomposition
   \(V_{200}=D_5\oplus S_{163}\oplus Y_{30}\) eliminates the two safe
   blocks and leaves a five-dimensional Schur matrix \(K_{\rm final}\)
   and its exact post-Schur graph \(X=(X_1,\ldots,X_5)\).
3. **D.171 (endpoint logarithm).**  For every graph column,
   \[
     A_TX_a(t)=-\tfrac12X_a(t)\log(T^2-t^2)+U_{X_a}(t),
   \]
   where the remainder is analytic on each of the seven contact cells.
   D.171 also supplies exact beta/harmonic formulas for all polynomial,
   logarithmic and log-square moments.
4. **D.174 (Bernoulli enclosure).**  The common analytic kernel has Taylor
   radius \(\pi>\log5\), so its degree-139 Taylor polynomial and a directed
   Cauchy remainder enclose every \(U_{X_a}\).
5. **D.172 (contracted continuum Gram).**  Exact FLINT polynomial
   arithmetic and Arb moment arithmetic enclose the complete five-column
   Gram \(H_X\), including Taylor and serialized-coefficient errors.

No moment identity which omits the intervening Tate projection is used.

## Infinite-dimensional Feshbach step

Write \(P\) for the finite post-Schur graph subspace and \(Q=I-P\).  The
first dependency gives

\[
 QA_TQ\ge\delta Q,\qquad \delta=0.218.
\]

The directed Gram in D.172 is a majorant for the **complete** off-diagonal
operator:

\[
 (QA_TP)^*(QA_TP)\le H_X.
\]

Consequently the operator Feshbach complement is bounded below by

\[
 PA_TP-(PA_TQ)(QA_TQ)^{-1}(QA_TP)
 \ge K_{\rm final}-\delta^{-1}H_X.                 \tag{1}
\]

This is the point which makes the result an operator proof rather than a
Galerkin calculation: every vector in the infinite complement is absorbed
by the certified bound \(QA_TQ\ge\delta Q\), and its entire coupling to the
dangerous graph is controlled by \(H_X\).

## Directed numerical data

The definitive computation uses 900 decimal digits and Taylor truncation
\(M=140\).  Its analytic-tail action bounds are

\[
 (2.144,3.012,5.982,14.48,55.39)\,10^{-22},
\]

and its independent graph-coefficient-ball action bounds are

\[
 (1.6086834,1.9477040,2.0560371,3.3822491,5.0816822)\,10^{-8}.
\]

The diagonal centres of \(H_X\) are

\[
 (7.18929231\,10^{-14},2.38922565\,10^{-11},
 5.95515021\,10^{-9},7.32054138\,10^{-7},
 2.48364187\,10^{-5}).
\]

The centre eigenvalues of the matrix on the right of (1) are

\[
 2.78052720\,10^{-12},\ 5.47152465\,10^{-10},\
 2.87827286\,10^{-7},\ 2.78898083\,10^{-5},\
 1.99028729\,10^{-3}.
\]

These eigenvalues are diagnostics only.  The proof is the Arb interval
congruence followed by interval Gershgorin.  Its five lower endpoints are

\[
 0.9497247499281420,\quad0.9891485574603620,\quad
 0.9741473729524866,\quad0.9360164888157518,\quad
 0.7940881020622326.
\]

All are positive, hence (1) is positive definite.  Together with the
positive complement this proves the boxed operator statement.

## Reproduction and independent audit

From the repository root:

```bash
PYTHONPATH=/tmp/d61-flint D172_DPS=900 D172_M=140 \
D172_SAVE=/tmp/d172_directed_endpoint_certificate.npz \
python3 riemann/03-research/phase-114-closing-the-four-rows/\
114_d_172_directed_contracted_gram.py \
| tee /tmp/d172_full140_final.log

python3 riemann/03-research/phase-114-closing-the-four-rows/\
114_d_181_endpoint_certificate_verify.py
```

The first command recomputes the directed Gram and writes outward-enclosed
matrix centres/radii.  The lightweight verifier independently recomputes
both error budgets from the D.166 graph, checks the interval identity in
(1), and repeats the final fixed-congruence Gershgorin audit.  It does not
accept a textual PASS marker as evidence.

For the definitive run the SHA-256 digests were:

```text
a46a626df96286581b1da5caa3173a167b0ba1d9ac3a750e51c36b2ce5a05148  d166_nested200_directed_graph.npz
6e12f07346962d7ce78876103511217ea3485919238db6d82e91be7f03aa4640  d172_directed_endpoint_certificate.npz
e33e2fdcbcd057bce7654d3bb5366a1fc14aa46d8118cc1df2a4662bef75eb67  d172_full140_final.log
b1d98b7df9799dbe65c98d7c643eb32fc5214fc475fe9b9fe07f0f0dc1d4e43f  114_d_172_directed_contracted_gram.py
36e558fcfdfc55c21d6bd3b805c2fdff906a129200348d889b62fc33a1b9f5ba  114_d_181_endpoint_certificate_verify.py
```

## Scope

The theorem closes the complete operator at the single endpoint
\(T=\frac12\log5\).  It does not assert propagation through the next
threshold cell; that is a separate operator-continuity/compression theorem.
