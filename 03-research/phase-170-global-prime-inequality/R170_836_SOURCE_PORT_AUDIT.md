# R170_836 — Audit of the canonical port and the quadratic map

Audited documents: R170_834–835. Verdict:
the typing and finite-rank obstructions are valid; the column map and its
Gram matrix are exact. The mixed form of R170_835 §6 is a specification
of the next theorem, not a construction nor evidence of its sign.

## 1. Exterior Tate port

R161_009 and R161_015 canonically fix the polar correction of the Hardy
port produced by a source. This does not define a functional on every
exterior tail. The comparison in R170_834 between character continuation
and Hardy evaluation proves non-uniqueness: for the Gamma columns the
lines

\[
 \kappa_m^-={b_me^{-(a_m+1/2)T}\over a_m+1/2},\qquad
 \kappa_m^+={b_me^{-(a_m-1/2)T}\over a_m-1/2},
\]

appear, and \(\kappa_m^+/\kappa_m^-\) depends on \(m\). A fixed Tate
matrix does not identify both lines when \(L\ge2\). The exterior
perturbation of R170_834 §3 also verifies that reflection and parity do
not cancel the freedom.

Compression to \(Z_0=\ker\mathcal A\) removes the ambiguity because there
\(r_F=0\). It is a correct reduction, but it does not control the
remaining Tate directions.

## 2. Column map and Gram matrix

With

\[
 \mathcal J_+=(I-D)^{1/2}R_L,\qquad
 \mathcal K_+=\iota_+(I-D)^{1/2},
\]

one obtains exactly

\[
 \mathcal K_+\mathcal J_+F=\iota_+(I-D)R_LF.
\]

The integral

\[
 2\int_T^\infty(t-T)e^{-(a_m+a_n)t}\,dt
 ={2e^{-(a_m+a_n)T}\over(a_m+a_n)^2}
\]

confirms the Gram matrix

\[
 G^{\rm col}_{mn}
 ={2b_mb_ne^{-(a_m+a_n)T}\over(a_m+a_n)^2}.
\]

The residual identities of R170_835 §3 and §5 are then exact sums and
differences. They do not assign a sign to the matrices.

## 3. Finite-rank obstruction

If the Hardy product germ factored universally through \(R_L\), its
evaluation at a simple critical zero would turn every functional
\(F\mapsto K_F(i\gamma)\) into a combination of
\(F\mapsto K_F(a_m)\). By duality this would imply

\[
 e^{-i\gamma t}\in\operatorname{span}\{e^{-a_1t},\ldots,e^{-a_Lt}\},
\]

which contradicts the independence of exponentials with distinct
exponents. The argument excludes a universal finite factorization
preserving the critical jet. It does not exclude an infinite map, a
source-dependent factorization, nor an identity valid only on the
radical.

The factorization on the radical via
\((R_L|_Z)^{-1}\) is algebraically legitimate, but depends on the object
one wishes to exclude and is not uniform in \(T\). It does not constitute
the missing arithmetic law.

## 4. Real entry of the arithmetic

In the finite PC identity, for \(M\ge N\), the absence of interior
coefficients of \(H_{M,N}\) uses exactly

\[
 \sum_{d\mid k}\Lambda(d)=\log k,\qquad k\le N.
\]

Substituting \(\Lambda\) by \(a\) brings back the defect
\(\delta_a(k)=\sum_{d\mid k}a(d)-\log k\). The column Gram matrix does not
contain this defect and survives for arbitrary positive weights. Hence no
sign obtained only from that Gram can close D.

## 5. Scope of the next piece

R170_835 §6 specifies a finite mixed form
\(\mathfrak B_{M,N,L}^{\varepsilon}\) with two desired expansions. It does
not yet prove that such a form exists with the same residual in both
expansions. It also does not yet incorporate the window derivative that
distinguishes the first contact from any positive eigenvector.

For the next piece to be accepted it must:

1. be written directly from the two finite PC identities;
2. preserve the hyperbola, collar, polar, and Tate terms before taking
   limits;
3. show algebraically the cancellation of \(\delta_\Lambda\);
4. produce the same residual in the Gamma–Euler and Hardy readings;
5. contain a one-sided variation in \(T\) or an equivalent minimality
   term.

R170_834–835 pass the audit at this scope. D remains open.
