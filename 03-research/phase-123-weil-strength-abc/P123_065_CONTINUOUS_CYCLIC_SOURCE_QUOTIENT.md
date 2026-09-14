# P123.065 — Continuous cyclic quotient of the repaired bimodule source

Date: 2026-09-06. Status: PROVED as a continuous underived shadow at
fixed source algebra. Derived excision and the required determinant or
nuclear target of A.5 remain separate obligations.

Let A be a repaired unital Fréchet algebra and M a complete Fréchet
A-bimodule. Define

    Q_A(M)=M / closure(span{a m-m a : a in A, m in M}).

This is a Hausdorff complete Fréchet quotient. Every continuous bimodule
map induces a continuous map of quotients. A continuous linear map from
M to a Hausdorff locally convex space that annihilates mixed commutators
factors uniquely through Q_A(M). Thus this construction is source-defined
and universal for continuous cyclic functionals on the declared domain.

For two bimodules M,N, form the Hausdorff completed balanced tensors.
There is a canonical continuous isomorphism

    Q_A(M tensor_A N) -> Q_A(N tensor_A M),
    [m tensor n] -> [n tensor m].

To prove that it exists after both quotients, start with the continuous
flip on the unbalanced completed projective tensor. The balancing
relation ma tensor n-m tensor an flips to n tensor ma-an tensor m.
Modulo balancing in the target this is (n tensor m)a-a(n tensor m),
which is killed by its cyclic quotient. Conversely the cyclic relation
am tensor n-m tensor na flips to n tensor am-na tensor m, which is a
target balancing relation. Continuity kills their closed linear spans
as well. Hence the flip descends. Its square is identity on elementary
tensors and therefore on the completion, proving the isomorphism.

For three factors, successive rotations send [m tensor n tensor l] to
[n tensor l tensor m] and then to [l tensor m tensor n]. Three rotations
are identity. All coherence identities follow on the dense elementary
tensors and extend continuously. The unit comparison with A agrees
with Q_A(M) through the usual balanced unit maps.

For a twisted rank-one module this is explicitly

    Q_A(E_beta)=A / closure(span{a x-x beta(a)}).

It uses the actual coefficient algebra and external action, rather than
a prescribed prime-weight functional. Finite sums commute with Q_A.
Applied degreewise to bounded complexes in P123.064, it gives a complex
because every differential is a bimodule map. Tensor rotation on
homogeneous elements uses the sign (-1)^(deg(m)deg(n)); substituting the
total differential proves that rotation is a chain map. Shifts and
mapping cones are preserved, since their terms are finite direct sums
and their differentials use the already functorial maps.

These cone identities do not assert preservation of arbitrary
quasi-isomorphisms. Degreewise underived coinvariants need not compute
derived Hochschild homology, and closure of commutators need not supply
topological derived excision. In particular this note does not identify
the quotient with a perfect determinant object or a nuclear trace space.

The continuous source boundary traces on I_int in P123.051 annihilate
[A_int,I_int], so factor through this quotient with A=A_int whenever
the indicated complete bimodule domain is used. The definition and flip
proof do not require a unit for this factorization statement. This links
the already constructed source traces to a common cyclic quotient,
without claiming an extension of those traces to added gauge constants.

The next required comparison must realize this source cyclic operation
in the target allowed by A.5, prove the necessary derived localization,
and recover the ruling determinant and mixed RR of A.8. A continuous
underived cyclic quotient alone does not meet those acceptance clauses.
