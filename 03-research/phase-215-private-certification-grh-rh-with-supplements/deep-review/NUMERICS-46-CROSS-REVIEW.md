# Independent cross-review of the certificate at T₅

`rebuild_matrix_46.py`, `verify_inertias_46.py` and `verify_remainders_46.py` were reviewed, collating them with P46:1630–1782. The cut-off values T are taken as fixed; this audit deals with the certified bounds and does not look for other cut-offs.

## Normalisation and boxes

The matrix integrates over [0,240] with factor 2T/π. The node map is `τ=panel/2+(node+1)/4`; hence the weight carries 1/4, and 480 panels cover the interval exactly. The documentation of the python-flint installation was consulted: `legendre_p_root(46,k,weight=True)` returns the 46 zeros, in decreasing order, with the Gauss weights for (−1,1). The order does not affect the sum.

The scale `sqrt(2n+1)(−1)^floor(n/2)` reproduces the sign `(-1)^((l−i)/2)` when i,l have the same parity. The 165×140 matrices correspond to degrees<330 against degrees<280, separately in each parity. The Bessel resets replace two consecutive values by Arb evaluations and preserve the recurrence; no node is 0, so the divisions by x are legitimate. The sum and the product of matrices are of balls, and the 210-digit serialisation retains an explicit radius.

The vector χ uses `i_n(T/2)=sqrt(π/(2x)) I_(n+1/2)(x)`, x=T/2. Its total norms are exactly `sinhT+T` in the even case and `sinhT−T` in the odd case. The indices of the sum 140:165 are precisely the stretch 280≤degree<330. The boxes of the Gram tails are `tail²` and those of the cross terms `tail·||χ_tail||`, by Cauchy–Schwarz. The exclusive replacement of the final entry by `c−upper(||P_Yχ||²/q_Y)` does indeed produce R'≤R; an arbitrary entry-by-entry subtraction is not interpreted as an order of forms.

An expository precision: P46:1765 writes `c_*=193.13`, which is a rounding down of 240T=193.132549… . 193.13 must not be used as an upper bound in the tails. The scripts use 240T as a ball and their predicates preserve the bounds 4.5e−20 and 3.9e−70.

## Analytic remainder

The integral identity for j_n and `∫_{−1}^1 P_n²=2/(2n+1)` give
`sqrt(2n+1)|j_n(z)|≤exp|Imz|` by Cauchy–Schwarz. This normalised version is the one that controls the matrix entries without introducing factors growing in n.

For a panel of length 1/2 and ρ=3.2 the half-height is `(ρ−ρ^-1)/8=.3609375`, smaller than the distance 1/2 to the poles of digamma. In the recurrence to w+8 one has Re(w)>0 and Re(w+8)>8. The bounds on the eight inverses, the shifted digamma part, logπ and the cosines give |g|<34. The normalised Bessel product is <2, so M=70 is valid.

Gauss 46 is exact up to degree 91. The Chebyshev coefficients satisfy |a_k|≤2Mρ^-k, the difference between integral and quadrature of T_k has modulus ≤4 and is 0 for odd k. Hence the remainder per standard panel is ≤`8Mρ^-92/(1−ρ^-2)`. Multiplying by 480, 1/4 and 2T/π gives a remainder <2e−42 per entry. This does not reproduce the finer figure 1.5e−43 of the manuscript; it does certify the conservative box 2e−42 actually added by the script.

Ran `verify_remainders_46.py`: remainder 1.28151474598754e−42, Λ280≤4.40516113423683e−20, Λ330≤3.86274619398775e−70. All the Arb predicates pass.

## Inertia: first run and pending obligation

The first independent run of `verify_inertias_46.py` passed the two primitive cases and the complete odd case. The complete even case, μ=1e−18,c=−1/2, was not certified: in the Schur complement of the fixed block the interval elimination reached pivot 83 with ball [±2.48]. This is **(c) for that implementation**, not a counterexample to the sign of the form. The other minimal pivots were 0.00846658, 0.02026832 and 8.14424e−14.

The result was reported to the main front; a preconditioning by midpoint LDL followed by an Arb check of the congruent form is being reconstructed there. Success of the four certificates must not be communicated on the basis of the first run. The subsequent review of that repair will be added here when there is executed evidence.

## Subsequent closure: four inertias certified

The corrected version with `preconditioned_positive` was read and run independently. The four cases pass. In the complete even case the invertibility of the Householder congruence is first certified by means of `||HᵀH−I||∞<1`; the binary block has determinant<0. The direct interval elimination still runs out at index 83, but it is no longer used as a certificate.

The new preconditioning takes **point** entries of an approximate factorisation: L is unitriangular with exact dyadic entries and D has strictly positive point diagonals. It is not presupposed that M=LDLᵀ exactly. The invertible matrix `P=D^-1/2 L^-1` is defined, a ball for `PMPᵀ` is computed using the complete M with its radii and positive diagonal dominance is checked by Gershgorin. This proof is valid for the enclosed exact matrix; its independence of the exactness of the approximate factorisation avoids the problem of interval dependency.

The cross run obtained, in the complete even case:

- binary determinant≈−0.0425472158049231;
- minimal pivot of the approximate factorisation≈0.000447307564344;
- certified Gershgorin margin>0.999999999999999999999969;
- `ok:true` in the four cases.

**Final verdict of this reconstruction: (a)** for the bounds requested at T₅ and their extension to smaller windows by means of the declared monotonicity. The remainder 2e−42, the tails and the normalisations were checked above. The reconstructed certificate uses preconditioning and Gershgorin for the complete even case: it must not be described as a successful literal reproduction of the simple interval Cholesky elimination. The finer remainder figure 1.5e−43 and the columns "fails at" of the table are not certified by this work; they are not necessary for the lower bounds that were indeed proved.
