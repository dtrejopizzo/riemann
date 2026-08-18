# D.172 — Exact contracted total-Gram reduction

## Verdict

The infinite Legendre tail in the endpoint Feshbach problem need not be
summed.  For each of the five already-contracted polynomial columns, the
pointwise Gamma formula of D.150 reduces the full physical Gram

\[
 H_{ab}=\int_{-T}^{T}(A_TX_a)(t)(A_TX_b)(t)\,dt
\]

to finite polynomial integrals and absolutely convergent scalar series with
explicit tails.  This is the correctly conditioned directed target: the raw
high/low Hurwitz matrix forms enormous terms before cancellation, whereas the
series below evaluate the contracted columns first.

This note proves the reduction.  It does not yet enclose the fifteen resulting
numbers.

## 1. Contract before summing the oscillators

Put (L=2T), (b_j=2j+\tfrac12), and

\[
 H_s(x)=\sum_{j\ge0}\frac{e^{-b_jx}}{b_j^s}.
\]

For a polynomial (F), define the two contracted endpoint symbols

\[
 q_F^-(b)=\sum_{r=0}^{\deg F}\frac{(-1)^rF^{(r)}(-T)}{b^{r+1}},
 \qquad
 q_F^+(b)=\sum_{r=0}^{\deg F}\frac{F^{(r)}(T)}{b^{r+1}}.             \tag{1.1}
\]

D.150 gives, with (x=t+T),

\[
 (A_TF)(t)=U_F(t)+B_F^-(x)+B_F^+(L-x),                            \tag{1.2}
\]

where (U_F) is an explicit piecewise polynomial containing the interior
Gamma term, the constant mass and the three contacts (2,3,4), and

\[
 B_F^\pm(x)=\sum_{j\ge0}e^{-b_jx}q_F^\pm(b_j).                    \tag{1.3}
\]

Equations (1.1)--(1.3) retain all cancellations belonging to (F) before
any high-degree endpoint quantities are combined.

## 2. Polynomial--boundary integrals

On a polynomial cell write (U(x)=\sum_{m=0}^d c_mx^m), after the affine
change from (t) to (x).  If

\[
 E_m(z)=\sum_{r=0}^m\frac{z^r}{r!},
\]

then direct integration gives

\[
 \int_\alpha^\beta x^m e^{-bx}\,dx
 =\frac{m!}{b^{m+1}}
 \left(e^{-b\alpha}E_m(b\alpha)
       -e^{-b\beta}E_m(b\beta)\right).              \tag{2.1}
\]

Therefore every (U\)-(B) cross term is a single absolutely convergent
sum obtained by multiplying (2.1) by (q_F^\pm(b_j)).  The contact break
points are exactly (T\pm\log n), (n=2,3,4); hence there are only finitely
many polynomial cells.  The (U\)-(U) term is integrated exactly on those
same cells.

## 3. Boundary--boundary kernels

For two boundary layers on the same side, Tonelli first for absolute values
and then termwise integration give

\[
 \begin{aligned}
 \int_0^L B_F^\sigma(x)B_G^\sigma(x)\,dx
  =\sum_{j,k\ge0}q_F^\sigma(b_j)q_G^\sigma(b_k)
  \frac{1-e^{-(b_j+b_k)L}}{b_j+b_k}.                 \tag{3.1}
 \end{aligned}
\]

For opposite sides,

\[
 \int_0^L B_F^-(x)B_G^+(L-x)\,dx
 =\sum_{j,k\ge0}q_F^-(b_j)q_G^+(b_k)K_{jk}(L),       \tag{3.2}
\]

where

\[
 K_{jk}(L)=
 \begin{cases}
 L e^{-b_jL},&j=k,\\[1mm]
 \dfrac{e^{-b_kL}-e^{-b_jL}}{b_j-b_k},&j\ne k.
 \end{cases}                                         \tag{3.3}
\]

The quotient in (3.3) is positive.  It is evaluated by `expm1` or its Arb
power series when (j\) and (k) are close; no subtractive floating-point
evaluation is required.

## 4. Explicit same-side tail

For a directed cutoff (J), evaluate (q_F^\pm(b_j)) by Horner arithmetic
for (j<J).  For (b\ge b_J), (1.1) gives the computable bound

\[
 |bq_F^\pm(b)|
 \le |F(\pm T)|+
 \sum_{r=1}^{d}\frac{|F^{(r)}(\pm T)|}{b_J^r}
 =:C_{F,J}^\pm.                                      \tag{4.1}
\]

Enlarge (C_{F,J}^\pm), if necessary, by the finitely many directed values
(|b_jq_F^\pm(b_j)|), (j<J).  It then bounds every (j\ge0).

With (a=\tfrac14), grouping (j+k=\ell) yields the exact identity

\[
 \sum_{j=0}^{\ell}\frac1{b_jb_{\ell-j}(b_j+b_{\ell-j})}
 =\frac{1}{4(\ell+2a)^2}
   \sum_{j=0}^{\ell}\frac1{j+a}.                    \tag{4.2}
\]

Consequently the part of (3.1) with (j+k\ge J) is bounded in absolute
value by

\[
 C_{F,J}^\sigma C_{G,J}^\sigma
 \sum_{\ell\ge J}
 \frac{4+\log(4\ell+1)}{4(\ell+1/2)^2},             \tag{4.3}
\]

and the last sum has an elementary integral upper bound of order
((1+\log J)/J).  Formula (3.3) gives an exponentially smaller analogous
bound for the opposite-side tail.  Equation (2.1) gives polynomial--boundary
tails by ordinary Hurwitz-zeta tails.

Thus all truncation errors are explicit Arb expressions.  In particular, no
claim about decay of uncomputed Legendre coefficients is needed.

## 5. The finite endpoint gate

Let (K_{\rm final}) be the directed five-dimensional Schur complement of
D.166 and let (H) be the total Gram obtained above.  Since the graph columns
are (A_T)-orthogonal to the eliminated finite safe directions, and D.152
gives the full primitive-complement gap (0.218), the sufficient endpoint
test is

\[
 \boxed{K_{\rm final}-0.218^{-1}H>0.}                \tag{5.1}
\]

The nondirected D.169 evaluation places the smallest eigenvalue of (5.1) near
(2.78\cdot10^{-12}).  D.172 turns its remaining proof into fifteen scalar
enclosures plus a five-by-five directed congruence.
