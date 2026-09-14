# P123.080 — Full two-fiber Tate excess and its determinant line

Date: 2026-09-06. Status: PROVED for the bar-defined Tate base-change
object in the strict derived category. Identification with the physical
ruling determinant or the global mixed RR metric remains open.

Let A -> D be the repaired split scalar quotient and I its ideal. For
any two continuous scalar augmentations lambda,mu, consider the full
two-sided bar for C_lambda tensor_A^(bar) C_mu. Projection to the
corresponding D bar has a continuous chain section, since both endpoint
actions factor through D. Its kernel consists of words with an I factor.

The proof of P123.079 applies with the full bar factors A=I direct_sum jD.
Filter by the number of D factors. Endpoint terms involving I vanish
because both augmentations kill I; endpoint terms involving D lower
the filtration. Likewise D-D and mixed products lower that count,
whereas I-I multiplication preserves it. The associated graded is
therefore the same collection of nonempty ideal-bar blocks, tensoring
with complete D factors. P123.078 supplies their exact fillings. The
finite filtration then proves strict acyclicity of the kernel, exactly
as in P123.079, without requiring lambda=mu.

Thus full-source two-fiber bars compare strictly with scalar two-fiber
bars for all lambda,mu. For distinct characters the scalar Koszul
complex of P123.076 has a nonzero constant differential coordinate and
is contractible. Hence the mixed full-source Tate terms vanish in the
strict derived category, not just after an unproved omission.

Put B=C_- direct_sum C_+ for lambda_i^-=p_i^-1/2 and
lambda_i^+=p_i^1/2, with r=|S_f|>=1 and V=C^r. The full bar-defined
base-change object and multiplication have the finite model

    B tensor_A^(bar) B ~= (exterior^* V)_- direct_sum (exterior^* V)_+,
    multiplication = identity in degree 0, zero in negative degrees.

Its cone E has two copies of exterior^k V in degree -k-1 for 1<=k<=r,
and zero differential. This determines a perfect complex in the stated
strict derived category. It is the full two-fiber version of the scalar
excess calculated earlier; no complementary ideal homology is left in
this particular bar comparison.

Fix the determinant convention det(E)=tensor_j det(E^j)^((-1)^j).
For one fiber, its determinant is

    tensor_(k=1)^r det(exterior^k V)^((-1)^(k+1)).

An invertible linear change g on V acts on this line by

    det(g)^e_r,
    e_r=sum_(k=1)^r (-1)^(k+1) binomial(r-1,k-1)
        =1 if r=1, and 0 if r>=2.

The exponent formula follows by counting the number of exterior basis
vectors containing each basis element; the final sum is the binomial
identity. Thus the full two-fiber determinant transforms by det(g)^(2e_r).
For r=1 its underlying line is (det V)^tensor 2. For r>=2 the alternating
exterior-basis construction supplies a basis-independent trivialization
of the underlying line, once the graded determinant ordering convention
is fixed. The total virtual rank of E is 2 for every r>=1; that grading
must still be retained even when the underlying line is trivialized.

This trivialization is not a computation of the required analytic norm.
A determinant line and a specified metric are different data, and a
globally prescribed Quillen or relative trace metric cannot be inserted
merely by choosing a basis. No conclusion about Gamma factors, arithmetic
degree or the Weil-form sign follows from the exponent cancellation.

The Tate base-change excess now has a complete finite model and explicit
determinant line at fixed S. Remaining tasks include identifying this
Tate functor with the physical ruling realization, proving the determinant
comparison for admissible mixed correspondences and their chart maps,
and supplying the required metric/equality in the trace target. These
are the remaining mixed RR requirements; the computed finite object
alone does not close A.8 or row A.
