# P123.053 — Unital integrable source and completed external bimodules

Status: PROVED for the fixed two-prime domain of
P123.051. This resolves its unital bimodule formulation; semilocal and
integral-contact comparisons remain open.

## 1. Adjoin the full rapid label algebra

Let D be the scalar rapid Gamma algebra of P123.019, with seminorms
d_k(c)=sum_gamma |c_gamma| H(gamma)^k. Put

    A_int^u = A_int direct_sum D,

interpreting c in D as the multiplier sum c_gamma U_gamma. This is
coefficient unitization with all rapid labels, not just adjoining a
single scalar unit to the crossed product. The product is

    (a,c)(b,d)=(ab+c b+a d,cd),
    (a,c)*=(a*,c*).

The multiplier actions are well-defined and continuous. More explicitly,
P123.051–052 imply, for each graph seminorm A_kd, constants C and indices
k',d' and an exponent N such that

    A_kd(U_gamma a)+A_kd(a U_gamma)
         <= C H(gamma)^N A_k'd'(a).

The label shift costs H(gamma)^k, the real moments a polynomial in
log H(gamma), and the section defect a further linear log H(gamma)
factor. These are precisely the terms in that bound. Consequently

    A_kd(c a)+A_kd(a c) <= C d_N(c) A_k'd'(a),

and the multiplier sums converge absolutely in every defining seminorm.
Thus A_int^u is a complete unital Fréchet star algebra. Associativity
holds first for finite label sums and extends by these estimates.

Its embedding into the original coefficient-unitized rapid algebra is
injective: each coefficient has the unique decomposition into a C_0
function and a constant. It has actual elements U_gamma, with
U_gamma U_delta=U_(gamma delta) and U_gamma*=U_(gamma^-1).
The kernel of the continuous projection A_int^u -> D is exactly A_int.

## 2. External action and gauge maps extend

Extend beta_h by fixing every element of D. P123.052 proves that this
is a continuous star automorphism on A_int; it respects the D multiplier
actions because external dilation commutes with Gamma dilation. Hence
it is a continuous star automorphism of A_int^u, with

    beta_(gamma h)=Ad(U_gamma) beta_h,
    beta_h(U_delta)=U_delta.

The original integrable ideal remains invariant. No trace on the added
label constants is inferred: the boundary traces retain the domain I_int
and the quotient trace retains B_int, as previously constructed.

## 3. Completed tensor law on this specific algebra

For beta an external automorphism of A=A_int^u, let E_beta be A with
its usual left multiplication and right action x.c=x beta(c). In the
Hausdorff completed projective balanced tensor, define

    E_beta tensor_A E_eta -> E_(beta eta),
    x tensor y -> x beta(y).

It is continuous by the multiplication estimates and balanced by direct
substitution. Its inverse is z -> [z tensor 1], since balancing gives
[x tensor y]=[x beta(y) tensor 1]. The inverse identities extend from
elementary tensors to the completion. In particular this is a topological
bimodule isomorphism on the new integrable unital source itself.

Triple compositions both give x beta(y) beta eta(z), establishing
associativity coherence. E_id is the tensor unit. The operation

    j_beta(x)=beta^-1(x*)

identifies the dagger with E_(beta^-1), reverses composition and squares
to identity in the same way as the explicit calculation of P123.019.
This is a star-bimodule structure, not a positivity theorem.

For a change of lift beta'=Ad(U_gamma) beta, the map

    E_beta' -> E_beta,  x -> x U_gamma

is a continuous bimodule isomorphism with inverse multiplication by
U_(gamma^-1). The right module identity follows from
beta'(c) U_gamma=U_gamma beta(c). Multiplication of the U_gamma proves
coherence of successive lift changes; beta fixing all U_delta proves
compatibility with the tensor law. All these maps preserve A_int as a
subspace, because it is a two-sided invariant ideal.

## 4. Exact scope for A/B/C

The trace-bearing integrable domain now sits as an ideal in a specific
unital source with the completed external bimodule tensor law, dagger
and coherent lift changes. The nonunital gap identified in P123.052 is
therefore resolved at fixed S_f={p,q} without putting nonexistent units
inside the original ideal.

This does not identify balanced tensors of the nonunital ideal alone,
assert full-Hom semilocal functoriality, or prove that integral contacts
are the diagonal shadow of these bimodules. The comparison between source
traces and the external relative character also remains necessary. Full
A/B/C closure cannot be inferred from this fixed-S tensor result.
