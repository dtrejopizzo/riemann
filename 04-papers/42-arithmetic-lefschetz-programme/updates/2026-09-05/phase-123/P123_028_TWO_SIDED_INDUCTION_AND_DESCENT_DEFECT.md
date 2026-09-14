# P123.028 — two-sided induction and the diagonal descent defect

Date: 2026-09-05. Status: PROVED for the algebraic bimodule induction,
its failure to preserve the diagonal via multiplication, and the ordinary
relative coring below. Completed derived descent and shadow comparison
remain OPEN.

## 1. Repair the morphism target

Keep R=Z[T,T^-1] -> A=A_S^u, T -> U_q, from P123.027. For an
R-bimodule complex E define

    F(E)=A tensor_R^L E tensor_R^L A.

The outer actions make this an actual A-bimodule complex. Derived
extension in both variables is an exact functor on the derived bimodule
categories. Central R-modules in P123.025–026 can be regarded as
R-bimodules, and their triangles are transported to this target.
We do not assert that every image is perfect over A's enveloping algebra,
nor that the algebraic functor extends to the required topological category.

Here the unqualified algebraic bimodules are over underlying rings.
For bimodules whose two complex scalar actions agree, first set
R_C=C[T,T^-1], E_C=C tensor_Z E, and use
A tensor_(R_C)^L E_C tensor_(R_C)^L A. This imposes the complex scalar
balance but annihilates finite integral torsion. The diagonal defect
proved below persists for this version as well: L is also R_C-balanced.

This repairs the immediate typing failure of one-sided induction.
It has an additional, independently testable requirement: the image
of the source diagonal R is

    F(R)=A tensor_R^L A,

with a canonical multiplication map to the desired diagonal A.

## 2. Multiplication does not identify that image with the diagonal

There are two continuous characters on A, defined using the additive
origin 0 in X_S and the added coefficient point infinity:

    chi_0(a)=sum_g b_g(0),
    chi_inf(a)=sum_g b_g(infinity),  a=(b_g).

Both points are fixed by all dilations. Absolute convergence and the
crossed-product formula therefore prove multiplicativity. Also
|chi_0(a)|, |chi_inf(a)| <= p_0(a). Both characters send U_q to 1,
so their restrictions to R agree with evaluation T=1.

Choose f in C_c(X_S) with f(0)=1. As a coefficient of A it has
chi_0(f)=1 and chi_inf(f)=0. In the ordinary balanced tensor put

    z=f tensor 1 - 1 tensor f.

Multiplication sends z to zero. However the balanced functional

    L(a tensor b)=chi_0(a) chi_inf(b)

sends z to 1. It is R-balanced because the characters agree on R.
Thus z is nonzero and multiplication A tensor_R A -> A is not injective.
The same functional extends to the Hausdorff completed projective
balanced tensor, so completion alone does not kill this defect.

For the derived tensor, H^0(A tensor_R^L A)=A tensor_R A.
Consequently its canonical multiplication to A cannot be a
quasi-isomorphism either. This refutes the proposed unit comparison,
without assuming flatness, nuclearity or a faithful Hilbert realization.
It does not assert that every conceivable object-level isomorphism is
impossible; the canonical comparison required by this induction fails.

## 3. Composition retains a middle coefficient factor

Associativity of derived tensor gives

    F(E) tensor_A^L F(H)
      ~= A tensor_R^L E tensor_R^L A tensor_R^L H tensor_R^L A.

The extra middle A is absent from F(E tensor_R^L H). Inserting
R -> A gives a natural map from the latter to the former, not an
automatic isomorphism. Together with F(R) -> A, these are the canonical
colax structure maps. Their coherence follows from the unit identity
and tensor associativity. Section 2 already prevents this structure
from being a strong unital monoidal realization.

Therefore genuine bimodule maps are now available, but preservation of
correspondence composition and diagonal is a separate descent theorem.
The statement is restricted to this induction and its canonical maps.

## 4. A concrete descent object to retain

At the ordinary algebraic level K=A tensor_R A is the relative coring:

    counit:      a tensor b -> ab,
    coproduct:   a tensor b -> a tensor 1 tensor b
                 in K tensor_A K ~= A tensor_R A tensor_R A.

These maps are well-defined on balanced tensors. For example moving
r across a tensor b becomes moving r successively through the two
adjacent R-balanced slots. Multiplication proves both counit identities;
inserting two units in either order proves coassociativity.

Thus the excess is structured descent data, not an unexplained scalar
error. The element z of section 2 gives an explicit nonzero counit
kernel. A candidate using this route must treat K and its coherent
descent, and prove how the resulting diagonal shadow compares with the
integral contact triangle. Declaring K equal to A is invalid.

This elementary coring construction is not a new common arithmetic
carrier. Effectivity, analytic trace, integral determinant retention and
mixed RR have not been obtained. It does, however, identify both an
actual bimodule-valued functor and the precise canonical comparison
that still fails after repairing P123.027's morphism typing.
