# P123.029 — one-prime algebraic faithfully flat descent

Status: PROVED for the single-prime, underlying
algebraic module statements below. Topological descent, bimodule
composition/shadow comparison and integral descent remain OPEN.

## 1. Exact setting

Take S={infinity,p}, positive gauge group p^Z, and the algebra A=A_S^u
of P123.019. Write a=sum_j b_j U_p^j. Its seminorms are

    p_k(a)=sum_j ||b_j|| p^(k|j|),  k>=0.

Set R_C=C[T,T^-1], with T mapped to U_p. Then A is faithfully flat
both as a left and as a right R_C-module, in the algebraic sense.
No multi-prime or completed tensor assertion is included in this theorem.

## 2. Torsion freeness on both sides

For right multiplication by a Laurent polynomial P(U_p), coefficient
sequences undergo ordinary finite convolution. Associate to a the
Banach-valued Laurent function

    F_a(z)=sum_j b_j z^j,  z in C^*.

On each compact annulus, a sufficiently large seminorm p_k bounds this
series and its differentiated series, giving locally uniform convergence
and holomorphy. If a P(U_p)=0, then F_a(z) P(z)=0. For nonzero P this
forces F_a=0 off its finite zero set and hence everywhere. Laurent
coefficient uniqueness (or the coefficient contour integrals) gives a=0.

For left multiplication, replace b_j by c_j=alpha_(p^-j)(b_j).
This coefficient change is an isometry for every p_k. The coefficient
of P(U_p)a at j is sum_l P_l alpha_(p^l)(b_(j-l)); after applying
alpha_(p^-j), it becomes sum_l P_l c_(j-l). The same Laurent argument
therefore proves left torsion freeness.

R_C is a PID: it is the localization of the Euclidean ring C[T] at T.
Each finitely generated submodule of a torsion-free R_C-module is free,
and the whole module is the directed union of these submodules.
Tensoring a directed union of free modules preserves injections, since
filtered direct limits of modules preserve exactness. Thus torsion
freeness proves flatness on both sides without a topological flatness
assumption.

## 3. Faithfulness

For every lambda in C^*, define

    chi_lambda(a)=sum_j b_j(infinity) lambda^j.

The rapid seminorms give absolute convergence and continuity. Evaluation
at infinity is invariant under the gauge action, so crossed-product
multiplication and absolute convergence prove that chi_lambda is a
unital algebra character. Its restriction to R_C is evaluation at lambda.

Every nonzero proper ideal I of R_C has a generator with a zero lambda
in C^*. Hence chi_lambda kills both IA and AI and proves that the
corresponding quotients of A are nonzero. For I=0 nonvanishing is clear.
If an R_C-module N is nonzero, any nonzero element supplies an injection
R_C/I -> N for a proper ideal I. Flatness preserves this injection
after extension of scalars, and the source remains nonzero by the
preceding character test. This proves faithfulness on either side.

In particular A tensor_(R_C) (R_C/(Phi_n)) is nonzero for n>1.
The analytic module realization of the cyclotomic component itself
is not acyclic; a primitive root character detects it. This must not
be confused with the unit-contact torsion complex, which becomes
acyclic after complexification.

## 4. An actual algebraic descent resolution

For every left R_C-module N the augmented Amitsur complex is exact:

    0 -> N -> A tensor_R_C N
      -> A tensor_R_C A tensor_R_C N -> ... .

The augmentation inserts 1. In degree r, the differential is the
alternating sum of inserting 1 in each of the r+2 available positions
among the A factors. The usual cancellation of pairs of insertions
proves d^2=0. All maps are R_C-linear even though R_C is not central in A.

To prove exactness, tensor once more on the left with the faithfully
flat right R_C-module A. The resulting complex is contractible: its
homotopy multiplies the extra first A factor with the following A
factor. The first insertion contributes the identity and the remaining
insertions cancel against the differential followed by that homotopy.
This proves dh+hd=id, including the augmented term. Flatness identifies
the homology after tensoring with the tensor of the original homology;
faithfulness then forces every original homology module to vanish.

This establishes a concrete algebraic resolution using the relative
coring of P123.028. It neither makes A tensor_R_C A equal to A nor
proves a completed categorical or monoidal equivalence. In particular
no diagonal shadow or arithmetic determinant comparison follows from
this module resolution alone.

## 5. Integral boundary and next gate

The original R_Z=Z[T,T^-1] -> A is not faithfully flat: for any rational
prime ell the nonzero module R_Z/(ell) is annihilated by extension to A,
since ell is invertible in A. Thus the theorem above cannot be used to
recover the integral contact or component-gluing torsion of P123.025–026.
It supplies a viable algebraic complex descent component, while an
integral model and its determinant comparison still have to be retained
separately and related by a theorem.

The next gate for this route is to equip the descent resolution with the
required completed domains and the integral/analytic shadow comparison.
The proofs here do not assert those gates, classical effectivity, RR or D.
