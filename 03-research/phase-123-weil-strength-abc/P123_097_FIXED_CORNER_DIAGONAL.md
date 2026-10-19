# P123.097 — The fixed corner diagonal in the continuous topology

Status: PROVED-IN-REPOSITORY for the completed
projective Hochschild chain complex of B=C(B_q). The equivalence is
strict quasi-isomorphism; a continuous linear contraction is not claimed.

## 1. A bounded approximate diagonal from characters

Write Y=B_q, a compact abelian group, and B=C(Y). Finite linear
combinations of its continuous characters are uniformly dense. In this
specific mapping torus this can be seen by first averaging over small
open subgroups of the compact unit factor: the resulting finite-level
quotients are compact abelian groups consisting of finitely many circles.
Their characters separate points and trigonometric polynomials are dense;
the averaging converges uniformly on continuous functions. The finite
levels separate points of Y, giving the asserted density.

For a finite set of characters, the subgroup they generate is finitely
generated abelian. Boxes in its free integer coordinates, times its
finite torsion subgroup, give finite sets F with
|eta F symmetric_difference F|/|F| as small as desired simultaneously
for every character eta in the prescribed finite set. Direct these
choices by finite sets and error tolerance. Define

    D_F=|F|^-1 sum_(chi in F) chi tensor chi^-1 in B tensorhat_pi B.

Then ||D_F||_pi<=1, multiplication mu(D_F)=1, and

    ||b.D_F-D_F.b||_pi ->0 for every b in B.                 (1)

For a character b=eta this follows by reindexing eta F; the norm is
bounded by its relative symmetric difference. Extend first to finite
linear combinations, and then to B using density and the uniform
bound ||b.D_F-D_F.b||_pi<=2||b||. This proves (1) directly.

## 2. Approximate chain fillings with a uniform bound

Use C_n=B^(tensorhat_pi(n+1)), with the untwisted boundary from
P123.096. For D_F=sum_j u_j tensor v_j (including its coefficients), set

    h_F(m tensor a_1 tensor ... tensor a_n)
        =sum_j u_j tensor v_j m tensor a_1 tensor ... tensor a_n.

The chosen character expression has sum_j ||u_j||||v_j||<=1, so
||h_F||<=1 in every degree. For n>=1, cancellation of adjacent products
and mu(D_F)=1 gives

    (d h_F+h_F d-1)(m tensor a_1 tensor ... tensor a_n)
      =(-1)^(n+1) sum_j
        (a_n u_j tensor v_j m-u_j tensor v_j m a_n)
                                  tensor a_1 ... tensor a_(n-1). (2)

Thus the norm of the remainder on an elementary tensor is at most
||a_n.D_F-D_F.a_n||_pi ||m|| product_(i<n)||a_i||. Its operator
norm is at most two, independently of F, so (1) and density extend
convergence of (2) to zero on every completed chain in positive degree.
In degree zero d_1=0 because B is commutative; no contraction there
is asserted.

## 3. Exact, rather than merely dense, boundaries

Let z be a cycle in positive degree n. Set r_0=z. Choose F_j so that
||r_j-d h_(F_j) r_j||<=||r_j||/2, using (2) and d r_j=0; if a residual
vanishes, stop. Define r_(j+1)=r_j-d h_(F_j)r_j. Each residual is a
cycle and ||r_j||<=2^-j||z||. Hence

    y=sum_(j>=0) h_(F_j)r_j

converges with ||y||<=2||z||. Continuity and telescoping give d y=z.
Therefore H_n(C_*)=0 for n>=1, for ordinary homology as well as reduced
homology. Every boundary image is the closed kernel of the next
boundary; the surjection onto that Banach kernel is open. The complex
is strictly exact in positive degrees. The choice of F_j depends on
the residual, so this proof does not supply a continuous linear section.

## 4. The precise perfect representative and its limits

The chain map C_*->B[0] is identity in degree zero and zero above it;
it has the degree-zero inclusion as a chain-map section. Its kernel is
the positive-degree complex just proved strictly acyclic. Consequently

    C_*(B,B) -> B[0]                                        (3)

is a strict quasi-isomorphism. All maps are B-linear for multiplication
on the first tensor factor; commutativity is essential here. Its kernel
is strictly exact on the underlying topological modules, not asserted
split as B-modules. Thus (3) gives a rank-one perfect B representative
in a derived category that inverts these strict quasi-isomorphisms.
It is not automatically an equivalence in the linearly split homotopy
framework of P123.066.

For an external parameter in K_q the corner automorphism is identity,
so this computes its tangential corner diagonal. Together with P123.096,
the fixed-parameter corner representatives are B[0] on K_q and zero
off K_q, with the exact-category qualifications stated in each result.
The determinant of the perfect representative B[0] is the trivial
line with virtual rank one. A trivial line does not provide the normal
regularized determinant or its prescribed metric.

This is a calculation for continuous functions with completed projective
tensors; it is not a calculation for a smooth differential algebra.
There is no parameter-uniform comparison across K_q, and no derived
Morita transport of the full source is supplied by this note. Normal
regularization, higher-stratum gluing and mixed RR remain obligations
for row A.
