# P123.019 — a multiplier-containing rapid algebra and local bimodule repair


## Status and scope

`PROVED-IN-REPOSITORY` below for a specified **larger unital Frechet algebra**,
its closed old kernel ideal, and the local twisted-bimodule calculus,
including continuous lift-change maps. This repairs the particular typing
failure in P123.018 §1 by changing the algebra explicitly.

This is not a proof for the minimal unitization formerly used in P123.014.
It does not assert nuclearity of the new ambient algebra, a trace on it,
a perfect integral contact, effective geometric descent, or row-A closure.
The alternative essential nonunital tensor theorem is not needed for this
repair and is not asserted here.

## 1. The coefficient enlargement

Fix finite S containing infinity and use positive S-units

    Gamma_S^+ = {product_(p in S_f) p^e_p : e_p in Z}.

Set X_S=A_S, B_S=C_0(X_S), and

    B_S^+ = C_0(X_S) + C1 = C(X_S^+),

where X_S^+ is the one-point compactification. Give it its supremum norm.
The decomposition b=f+c1 is unique; |c|<=||b|| and ||f||<=2||b||.
Every dilation alpha_a(b)(x)=b(a^-1 x) fixes 1 and extends to the added
point at infinity, so is an isometric unital star automorphism of B_S^+.

For H(q)=max(numerator(q),denominator(q)), define

    A_S^u = { (b_q) : b_q in B_S^+,
                p_k(b)=sum_q ||b_q|| H(q)^k < infinity, all k>=0 }.

Use the crossed-product multiplication and involution

    (bc)_t = sum_(qr=t) b_q alpha_q(c_r),
    (b*)_q = alpha_q(conjugate(b_(q^-1))).

Since H(qr)<=H(q)H(r) and H(q^-1)=H(q),

    p_k(bc)<=p_k(b)p_k(c),    p_k(b*)=p_k(b).

The common weighted-l1 projective limit is complete and metrizable.
Thus A_S^u is a unital Frechet star algebra. The identity has coefficient
1 at label 1, and U_q has coefficient 1 at label q. In particular

    U_q in A_S^u,   U_q U_r=U_qr,   U_q*=U_(q^-1).

This is the rapid crossed product of the **coefficient unitization**,
not the unitization of the old crossed product.

## 2. The old ideal survives with its topology

Let C_S^rapid be the scalar rapid label algebra. Evaluation at the added
coefficient point defines a continuous split star homomorphism

    epsilon_infinity : A_S^u -> C_S^rapid,
    (f_q+c_q) |-> (c_q).

Its continuous section is (c_q) |-> (c_q 1). Its kernel is exactly the
K_S^rapid of P123.006. Consequently

    0 -> K_S^rapid -> A_S^u -> C_S^rapid -> 0

is split exact as a sequence of topological vector spaces and algebras.
The splitting is a semidirect algebra structure, not a direct product:
label constants act on the kernel ideal. The embedding of K is isometric
for every p_k; products by A_S^u preserve K.

The continuous projection to the old ideal has seminorm bound 2. Since
C_0(X_S) is recovered as a complemented coefficient subspace, the ambient
algebra is not claimed nuclear. No new trace is defined on the added label
constants. Existing trace assertions may only be used on a domain already
proved to lie in the old ideal or on a separately constructed represented
trace sector.

## 3. External automorphisms and topology

For a in A_S^times put

    beta_a(sum_q b_q U_q)=sum_q alpha_a(b_q)U_q.

These are p_k-isometries, beta_a beta_b=beta_ab, and commute with star.
They fix every U_q. For gamma in Gamma_S^+,

    beta_(gamma a)=Ad(U_gamma) beta_a.

The action is jointly continuous. For a finite label sum it follows from
strong continuity of dilations on C_0 of a locally compact product of
local fields (approximate by compactly supported continuous functions),
and constants are fixed. Uniform isometry and label-tail truncation extend
the assertion to each p_k. Smoothness of all coefficient vectors is not
claimed; the smooth-section problem remains separate.

## 4. The completed balanced tensor theorem

For a continuous automorphism beta of A=A_S^u, let E_beta be A with
left action by multiplication and right action x.c=x beta(c). Define its
balanced completed tensor with E_eta as the Hausdorff quotient of the
completed projective tensor by the closed span of balancing relations.

The continuous map

    mu_(beta,eta)(x tensor y)=x beta(y)

is balanced, since x beta(c) beta(y)=x beta(cy). Its target is E_(beta eta).
The inverse is the continuous map z |-> [z tensor 1]. Indeed in the
balanced quotient

    [x tensor y]=[x beta(y) tensor 1].

This proves both inverse identities on elementary tensors, hence by
density on the completed quotient. The source is therefore complete and
isomorphic to A; no completion or closed-range claim is inferred merely
from an algebraic bijection.

The two parenthesizations of a triple tensor both send it to
x beta(y) beta eta(z). This proves associativity coherence on elementary
tensors and then on completion. E_id is the tensor unit. Define the
contravariant star operation through

    j_beta(x)=beta^-1(x*) in E_(beta^-1).

It is conjugate-linear, exchanges left/right actions with star, and squares
to the identity after replacing beta by beta^-1. Direct substitution gives
j_(beta eta)(mu(x,y))=mu_(eta^-1,beta^-1)(j_eta(y),j_beta(x)).
Thus E_beta^dagger identifies with E_(beta^-1), and composition reverses.
This is a star-bimodule operation, not an unproved Hilbert positivity claim.

## 5. Lift independence, now with the correct codomain

For a'=gamma a define

    Phi_gamma : E_(beta_a') -> E_(beta_a),
    Phi_gamma(x)=x U_gamma.

U_gamma is now an actual invertible element of A. Both Phi and its inverse
are continuous, with p_k(x U_gamma)<=H(gamma)^k p_k(x). For the right action,

    x beta_a'(c) U_gamma = x U_gamma beta_a(c).

Left linearity is immediate. If a''=delta gamma a, successive maps
multiply on the right by U_delta U_gamma=U_(delta gamma), proving coherence.
Tensor compatibility follows, for lift changes gamma and delta, from

    (x U_gamma) beta_a(y U_delta)
       =x beta_(gamma a)(y) U_(gamma delta).

All identities take place inside A_S^u and its completed bimodules.
Therefore the action groupoid of lifts has a coherent realization by
invertible bimodules, and isomorphism classes depend only on the idele class.
This does not claim that different idele classes always give nonisomorphic
bimodules; faithfulness requires an independent theorem.

## 6. Sign convention and next obligations

The above uses Gamma_S^+. If all S-units are required, replace the group
by {+1,-1} times Gamma_S^+ and set H(-q)=H(q). Every proof is unchanged.
The positive-unit quotient retains a real sign component; the full-unit
quotient identifies it with the corresponding finite-place sign action.
Do not interchange the two quotients silently.

The local typing repair is complete in A_S^u. It remains to prove genuine
chart transitions, a suitable smooth trace sector and its representation,
integral arithmetic contact and all numerical/RR comparisons. In
particular this enlargement does not transport a torsion complex over Z
into existence in a C-linear category.
