# P123.027 — the direct integral-to-analytic map lands in modules

Date: 2026-09-05. Status: PROVED for the algebraic functor and its
bimodule typing obstruction below. No completed realization is claimed.

## 1. An actual coefficient map

Fix a chart S containing a finite prime and a nonidentity positive
S-unit q. Let A=A_S^u be the enlarged unital rapid algebra of P123.019.
Because U_q is an invertible element, there is a unital ring map

    i_q: R=Z[T,T^-1] -> A,  T -> U_q.

It is injective: distinct powers of q have distinct crossed-product
labels, and finite Laurent sums have unique coefficients. Regarding A
as a left A, right R bimodule gives the algebraic derived functor

    A tensor_R^L - : Perf(R) -> Perf(A).

Here Perf(A) means algebraic perfect left modules over the underlying
ring. A bounded finite projective R model becomes a bounded finite
projective A model; flatness of A over R is not needed for this derived
construction. All finite free differential matrices are continuous on
the corresponding finite products of A, but this alone asserts no
completed derived descent theorem.

The image of V_n is the two-term left-module complex

    [A --right multiplication by Phi_n(U_q)--> A].

The exact triangles of P123.025–026 are transported as module triangles.
This is a concrete realization of their algebraic maps, with the scope
of its target explicitly limited.

## 2. Why this is not yet a correspondence realization

For the regular A-bimodule, right multiplication by a is a bimodule
endomorphism if and only if a is central: right linearity at 1 says
ba=ab for every b. The element Phi_n(U_q) is not central.

Indeed set d=degree Phi_n, which is positive for n>1. Its leading
coefficient is 1. Choose f in C_c(X_S) with alpha_(q^d)(f) != f;
such an f exists because q^d acts nontrivially on the real coordinate.
In the commutator with f, the coefficient at label q^d is
alpha_(q^d)(f)-f, up to the choice of commutator order, and is nonzero.
Other polynomial terms have different labels and cannot cancel it.

Thus the displayed complex is not a complex of regular A-bimodules.
Neither its module triangle nor its matrix continuity proves that it
belongs to Corr_A. Introducing different twisted terms would require
new bimodule maps and proofs of composition and diagonal-shadow
compatibility; it is not supplied by extension of scalars above.

## 3. The central scalar alternative

The ring map T -> 1 is central and does give complexes of regular
A-bimodules. For V_n its differential is the nonzero scalar Phi_n(1),
which is invertible in the complex algebra A. The complex is therefore
contractible, with contracting homotopy multiplication by its reciprocal.
This alternative loses the nonzero integral contact object.

An integral lattice together with metric/determinant comparison could
retain an arithmetic degree despite analytic acyclicity. No such
comparison is implied by contractibility, and no impossibility of that
more structured realization is claimed here.

## 4. Resulting obligation

The missing bridge must do more than give a coefficient homomorphism:
it needs an integral correspondence category and a realization on its
bimodule/kernel morphisms, plus a comparison of shadows retaining the
required arithmetic determinant. The two direct maps above distinguish
the existing module-level construction from that outstanding theorem.
This is consistent with P123.022's additive torsion obstruction and
does not extend it to all possible integral-to-analytic realizations.
