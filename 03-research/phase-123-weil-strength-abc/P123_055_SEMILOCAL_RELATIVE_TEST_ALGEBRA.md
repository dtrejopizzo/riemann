# P123.055 — Semilocal assembly of the relative test algebras

Status: CONSTRUCTED with continuous crossed product,
involution and coherent injective chart maps. Faithfulness of its map
to the original coefficient completion is a separate requirement.

## 1. Coefficient algebra and its topology

Let E_p be the local Banach algebra of P123.054, retaining its original
norm nu_p so nu_p(chi_p)=1. Its multiplication is bounded with constant
at most 4. Let E_infinity be the completion of C_c^infinity(R) for

    m_d(g)=||g||_infinity+integral (1+|t|)^d |g(t)|dt,
    d=0,1,2,... .

It is a Fréchet algebra under pointwise multiplication, and translation
by s has bound (1+|s|)^d in m_d. Integration and the first moment are
continuous functionals. For finite S_f form the completed projective
tensor algebra

    E_S=E_infinity tensor_pi product_(p in S_f) E_p.

Write pi_d for the projective seminorm formed from m_d and all nu_p.
The tensor product multiplication extends continuously with bound
pi_d(fg)<=4^|S_f| pi_d(f)pi_d(g); conjugation is continuous. These follow
first on tensor decompositions and then by taking the projective infimum.

There is a continuous coefficient realization E_S -> C_0(X_S^+) obtained
by multiplying tensor factors. We do not infer injectivity of this
completed projective realization from injectivity of its individual
factors. All assertions below are on the specified completed tensor
algebra, where its norms and functional maps are defined independently.

## 2. Gamma action and rapid crossed convolution

Gamma_S acts on E_S by its real translation and local dilations. From
P123.054, for gamma in Gamma_S,

    pi_d(alpha_gamma f)
      <= (1+|log gamma|)^d
            product_(p in S_f)(1+|v_p(gamma)|) pi_d(f)
      <= C_(S,d) H(gamma)^(d+|S_f|+1) pi_d(f).   (2.1)

Define the rapid crossed algebra T_S as label sequences with

    P_kd(b)=sum_gamma H(gamma)^k pi_d(b_gamma)<infinity
                            for every k,d>=0.

Using the usual crossed product, (2.1) gives, with N=d+|S_f|+1,

    P_kd(bc)<=C'_(S,d) P_(k+N),d(b) P_kd(c).

The same dilation estimate proves continuity of involution, with a
possible increase of the rapid index. Completeness follows from the
complete coefficient space and the countable weighted l¹ seminorms.
Thus T_S is a Fréchet star algebra. The group action is not isometric
in the relative norms; its controlled growth is explicitly included.

## 3. Adding a prime is a split injective coefficient map

For S contained in T define

    j_ST(f)=f tensor product_(ell in T_f\S_f) chi_ell.

Each chi_ell is idempotent, so this is multiplicative and respects star.
Its projective seminorm is at most the old one. Evaluation at zero in
the added coordinates is a contractive left inverse, since
ev_ell(chi_ell)=1 and evaluation is bounded by nu_ell. Therefore

    pi_d(j_ST f)=pi_d(f).                        (3.1)

In particular this is injective on the completion, independently of the
unsettled faithfulness of the coefficient realization in section 1.
Evaluation at zero is also an algebra homomorphism on each added factor.

Every old Gamma_S element is a unit at a new prime. It preserves chi_ell,
so j_ST intertwines the old Gamma action. Extend j_ST coefficientwise
on old labels and use zero coefficients on new labels. Crossed products
then agree, and (3.1) gives

    P_kd(j_ST b)=P_kd(b).

Tensor associativity gives j_TU j_ST=j_SU on chart triples. No projection
discarding new labels is claimed to be an algebra retraction of the
whole crossed algebra: products of opposite new labels preclude that.

## 4. External action and relative components

Normalized external elements act by real translations and finite units,
so preserve the local relative norms up to the real moment factor.
Their action is strongly continuous, first on tensor tests and then by
density and locally uniform bounds. It extends to T_S. The normalized
lift adding unit 1 at new places intertwines j_ST; so does any added
unit, since chi_ell is unit-invariant. This recovers the required
coefficient intertwining for the normalized chart data.

For every choice of either R_p or ev_p in each finite coordinate, their
tensor product with real integration or its first moment defines a
continuous functional on E_S. P123.054 gives their dilation law exactly,
including all evaluation defect terms. Under j_ST a new evaluation
factor retains the old functional, whereas a new R_ell factor gives
zero. These identities compose on triples because the tensor operations
in different coordinates commute.

Such coefficient functionals are not automatically traces on T_S:
their dilation defects must be included in the cyclic comparison. This
construction supplies their common domain and exact covariance, rather
than assuming cyclicity from the tensor notation.

## 5. Scope and next comparison

The relative local blocks now form a single semilocal family of complete
crossed algebras with coherent injective chart maps and controlled gauge
growth. This resolves their algebraic/topological assembly, which was
left open in P123.054. It does not yet identify T_S faithfully with a
subalgebra of the earlier rapid C_0 source or with the two-prime domain
of P123.051. Those realization comparisons must be proved, as must the
cyclic shadow and its match to the external Fourier trace. Integral
contact transport and the D sign remain unresolved.
