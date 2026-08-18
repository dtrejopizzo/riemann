# D.172 — Directed closure of the first endpoint

## Theorem

At

\[
 T={1\over2}\log5,
\]

the complete primitive endpoint operator is strictly positive.  The proof is
a directed Feshbach certificate; no ambient moment identity of order two or
higher is used.

## Inputs already certified

1. D.152 proves that the primitive complement has lower bound
   (delta>0.218), including the rank-two Tate defect.
2. D.166 proves the directed finite hierarchy
   (V_{200}=D_5\oplus S_{163}\oplus Y_{30}).  Its final five-dimensional
   Schur matrix (K_{m final}) is strictly positive.
3. D.171 proves the exact endpoint decomposition

   \[
   AF(t)=-\frac12F(t)\log(T^2-t^2)+U_F(t),
   \]

   with (U_F) analytic on each contact cell, and gives every polynomial
   log and log-square moment in closed beta/digamma form.

## Directed continuum Gram

Let (X=(X_1,\ldots,X_5)) be the exact post-Schur graph from D.166.  D.172
uses the cancellation-free D.156 formula

\[
 q(z)=zK(z)={ze^{z/2}\over2\sinh z},\qquad
 R_1(x)=H_1(x)+\frac12\log x.
\]

Writing (q(z)=\sum c_nz^n), the truncation at (n<140) makes every
(U_{X_a}) a polynomial on each of the seven contact cells.  The coefficients
are exact Arb balls.  Polynomial products are performed by FLINT polynomial
arithmetic, and all integrations are finite Arb sums of the moments in D.171.

The Taylor tail is rigorous.  On the circle (|z|=R=2.5<\pi), the Bernoulli
majorant for

\[
 q(z)=\frac12{2z\over e^{2z}-1}e^{3z/2}
\]

gives

\[
 M_R\le {e^{3R/2}\over2}
 \left(1+R+2\zeta(2){(R/\pi)^2\over1-(R/\pi)^2}\right).
\]

Thus, for (L=log5),

\[
 \left|q(z)-\sum_{n<140}c_nz^n\right|
 \le {M_R(L/R)^{140}\over1-L/R}qquad(0\le z\le L).
\]

The same bound divided by 140 controls the tail of (R_1), since its
nonconstant coefficients are (-c_n/n).  The resulting uniform action errors
for the five columns are between (2.14\cdot10^{-22}) and
(5.54\cdot10^{-21}).

The binary serialization radii of the graph coefficients are not expanded
into ill-conditioned monomial balls.  They are propagated in the normalized
Legendre basis using

\[
 |P_n|le1,qquad |P_n'|le {n(n+1)\over2},qquad qle2,qquad R_1le2
\]

on the real interval.  Here (qle e^{L/2}/2<2) follows from
(sinh z\ge z), while (R_1le R_1(0)=\log2+\pi/4<2).  The resulting
directed action errors are

\[
 (1.61,1.95,2.06,3.38,5.08)\,10^{-8}.
\]

After adding both error sources, the diagonal of the directed continuum Gram
(H_X\ge (QAX)^*(QAX)) has centres

\[
 (7.1893\,10^{-14}, 2.3892\,10^{-11}, 5.9552\,10^{-9},
   7.3205\,10^{-7}, 2.4836\,10^{-5}).
\]

## Final Feshbach congruence

The directed matrix

\[
 K_{m final}-{1\over0.218}H_X
\]

has centre eigenvalues

\[
 2.7805\,10^{-12},\quad5.4715\,10^{-10},\quad
 2.8783\,10^{-7},\quad2.7890\,10^{-5},\quad1.9903\,10^{-3}.
\]

A frozen Cholesky preconditioner followed by Arb Gershgorin gives the explicit
lower endpoints

\[
 0.9497247499,quad0.9891485575,quad0.9741473730,quad
 0.9360164888,quad0.7940881021.
\]

All are strictly positive.  Since the complementary block is at least
(0.218I), the Feshbach inequality proves positivity of the complete
primitive operator at this endpoint.

## Reproduction

```bash
PYTHONPATH=/tmp/d61-flint D172_DPS=900 D172_M=140 \
python3 114_d_172_directed_contracted_gram.py
```

The successful run is preserved at `/tmp/d172_full140.log`.  It exits with
code zero and prints

```text
D172 DIRECTED CONTRACTED CONTINUUM GRAM AND FINAL SCHUR: PASS
```

## Scope

This closes the local first-endpoint obligation at (T=\frac12\log5).  It
does not by itself prove the global row-D inequality away from this endpoint;
that requires the separate global propagation argument.
