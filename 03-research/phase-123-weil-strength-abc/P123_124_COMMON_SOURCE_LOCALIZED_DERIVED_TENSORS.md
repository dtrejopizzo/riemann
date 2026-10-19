# P123.124 — Localized derived tensors in the common smooth source

Status: PROVED-IN-REPOSITORY for coordinate-nonzero
opens and the linearly split exact structure of P123.122. This realizes
a geometrically localized sector with its actual derived composition.
It does not assert localization for every open or the full mixed RR.

## 1. Actual invariant open supports and their ideals

Fix P and A=A_sm^u(P). For J contained in P let

    U_J={x: x_p!=0 for every p in J},
    I_J=Rapid_(Gamma_P)(E_R tensorhat
                    tensor_(p in J) F_p tensorhat
                    tensor_(p notin J) E_p).             (1)

The realizations in P123.121 identify I_J as an actual closed two-sided
ideal of A supported on U_J. All Gamma actions preserve these opens.
Here I_empty is the nonunitized coefficient ideal A_sm(P), not the unit
A; the scalar lattice sector has not been silently identified with it.
The finite coordinate splittings E_p=C chi_p+F_p, together with the
linear scalar-lattice splitting, give a continuous linear projection
A->I_J. Thus 0->I_J->A->A/I_J->0 is admissible in P123.122.

We prove that every I_J is relatively projective as a module on either
individual A side. This is stronger than assuming approximate units
bounded in the rapid seminorms; no such boundedness is asserted.

## 2. Partitions adapted to the coefficient topology

On the real line choose a smooth nonnegative partition psi_n, n in Z,
with uniformly bounded derivatives, sum psi_n=1, and support in a fixed
translate of a compact interval. Choose smooth compact e_n=1 on
support psi_n, with the same uniform derivative bounds.

For p in J use the valuation-shell idempotents 1_(v_p=j), j in Z.
For p notin J use instead chi_p=1_(v_p>=0), including its value at 0,
together with the shell idempotents for j<0. These latter functions
partition all Q_p, while the former partition Q_p^*. All are in their
respective E_p or F_p factor and have trivial unit Fourier character.

Take their tensor products with e_n and psi_n. Denote the resulting
coefficient functions by e_i and rho_i, placed at identity lattice label.
They belong to I_J and satisfy

    e_i rho_i=rho_i,
    sum_i rho_i=1 on U_J.                                (2)

The sum is locally finite on U_J. The chi_p option is essential:
one must not decompose a nonzero value at x_p=0 into infinitely many
flat positive-valuation shells.

For every pair of seminorms alpha,beta on I_J there are a stronger
seminorm nu on A restricted to I_J and a constant such that

    sum_i alpha(e_i) beta(rho_i a)<=C nu(a),   a in I_J.   (3)

Here is the convergence argument. Real translates of the cutoffs grow
only as exp(l|n|) in a weighted derivative seminorm; a shell cutoff
grows as p^(l|j|). All their real derivatives are uniformly bounded
before these weights, and their unit conductor is 1. Applying a
stronger real weight and stronger shell weights to a leaves an arbitrary
geometric decay factor exp(-R|n|) product p^(-R|j|) after multiplying
by both output weights. Derivatives of rho_i a are handled by the finite
Leibniz sum. The unit Fourier and Gamma sums retain their original
weights, since rho_i has identity label and trivial unit character.
For the chi_p option the positive shells and value at zero remain in
one E_p seminorm. Summing the geometric bounds over the remaining
indices proves (3). This is precisely where rapid decay at the
specified nonzero-coordinate boundaries is used.

These estimates also prove sum_i rho_i a=a in every seminorm, by
weighted tail convergence. They do not assert convergence of sum rho_i
to an element equal to 1 inside the nonunital ideal.

## 3. A continuous module splitting of multiplication

Define

    h_J(a)=sum_i e_i tensor rho_i a.                      (4)

Estimate (3) gives absolute convergence in the unbalanced completed
projective tensor I_J tensorhat I_J and continuity. The multiplication
map satisfies m h_J=identity by (2). Moreover (4), regarded as a map
into I_J tensorhat A, is right A-linear: associativity gives
rho_i(ab)=(rho_i a)b. Its multiplication retraction is also right
A-linear. Thus I_J is a continuous right-module retract of the free
right module (underlying Frechet I_J) tensorhat A. Such free modules
lift through any admissible right-module surjection, by its underlying
continuous linear section. Hence I_J is relatively projective on the
right. Applying the source involution and reversing factors gives the
same assertion on the left.

In particular I_J tensorhat_A - preserves admissible exact sequences.
For free modules this follows by tensoring the explicit linear splitting;
for their retracts, apply the retract to the resulting split exact
complex. If its contraction is h and the commuting chain projection is
p, the contraction on the retract is p h p. This also proves continuous
split exactness on the image, rather than only algebraic injectivity.
The same observation gives the one-sided relative flatness needed for
the derived tensors below.

There is an additional explicit consequence: inserting (4) at the first
factor contracts the nonunital multiplication bar of I_J. Its first
boundary term is a, and its other terms cancel the insertion after the
bar boundary by right-linearity. Thus the ideal bar itself is linearly
contractible in the stated topology; no bounded-approximate-unit
excision assertion is substituted for this construction.

## 4. Intersection is the actual derived tensor product

For J,K contained in P, multiplication induces an isomorphism

    I_J tensorhat_A I_K ~= I_(J union K).                 (5)

To prove injectivity, tensor the admissibly split sequence
0->I_K->A->A/I_K->0 on the left by the relatively projective I_J.
This embeds I_J tensorhat_A I_K as a closed subspace of
I_J tensorhat_A A=I_J; its embedding is multiplication. Its image is
contained in I_(J union K): support of a crossed product is contained
in U_J intersect U_K, since the lattice preserves U_K.

For surjectivity use (4) on I_(J union K). Each first factor lies in
I_J and each second in I_K, so h_(J union K) followed by the balanced
quotient is a continuous right inverse to multiplication onto that
ideal. Together with injectivity this proves (5) as a topological
isomorphism, including the inverse's continuity.

Because I_J is relatively projective on the right, the corresponding
relative derived tensor has no higher terms in homology. Therefore

    I_J tensorhat_A^L I_K ~= I_(J union K)[0].             (6)

This uses the exact structure actually specified in P123.122. It is
not a claim about a different algebraic or C*-module tensor product.

## 5. Localized twists and stable composition

An external dilation beta preserves every coordinate-nonzero open and
acts continuously on A and its I_J by P123.121. Put
I_(J,beta)={}_1(I_J)_beta, whose right action is twisted by beta.
Untwisting is an exact equivalence of module categories, so these
modules retain the left and right relative projectivity just proved.
The original coefficient formula and (6) give

    I_(J,beta) tensorhat_A^L I_(K,eta)
           ~= I_(J union K,beta eta),
    u tensor v -> u beta(v).                             (7)

The graph support is the original one from the source action: a label
gamma in a coefficient contributes the graph with target
beta^-1 gamma^-1 x, with x restricted to U_J. Thus the ideals provide
actual localization of those graph kernels, not a selection based on a
future scalar trace. Their operators and support maps use the same
multiplication as (7).

Finite sums, retracts, bounded complexes and cones of these localized
twists, together with the unit and unlocalized twists of A, form a
specified stable sector in D_rel^-(A-A). Its terms are K-flat on either
side, so ordinary total tensors compute their relative derived
composition. Equation (7) proves closure under that composition; its
associativity is the one already constructed in P123.122. This is an
actual localized extension beyond the old twist-only sector.

## 6. New lattice covariance is constructed for this sector

In the notation of P123.123, work first over C with the full new
coefficients and old lattice. The same coordinate ideals and splittings
exist there. The new lattice action alpha_g preserves them, is tempered,
and commutes with the extended external dilation beta. Consequently

    rho_g(u)=alpha_g(u)

is a defined tempered semilinear action on each localized twist over C.
It meets the hypotheses of the invertible derived crossed comparison
P123.123 (11). Thus transport through the new lattice is now constructed
for these objects and for their equivariant maps and complexes.
It is not assigned to every old morphism: a differential or map must
commute with the specified rho to belong to that equivariant domain.
Nor is this a coefficient lift for every old correspondence across
A->C. Those broader extension and descent obligations remain.

## 7. Remaining full A requirements

This constructs localized source modules, proves their one-sided
projectivity and exact completed derived intersections, and supplies
the new-lattice actions on an explicit stable sector. It joins actual
geometric supports to the common derived composition; bounded cutoff
norms, algebraic exactness or density are not used as substitutes.

The coordinate-open graph sector is not declared the entire admissible
mixed category on the noncollapsed square. Full geometric descent,
contravariant duality, the trace-class determinant domain, numerical and
effectivity comparisons, and the intrinsic mixed RR metric identity
remain necessary. No full row A or global sign theorem is claimed.
