# R161_073 — A legitimate stabilized inverse and finite kernel test

## Assumptions and scope

Work on the primitive window Hilbert space. Assume the imported first-contact facts: H=H_T is selfadjoint, nonnegative, and has compact resolvent. Choose a finite weighted Gamma-moment observation R: H_space -> C^L that is injective on ker H. Such an L exists by R161_046, but that existence does not give an effective bound for L. All adjoints below are on this primitive space.

The following is an operator reduction, not a claim of a new general spectral theorem or a proof of D.

## 1. Stabilization does not assume absence of a zero mode

Define S=H+R*R by bounded form perturbation. Then S is strictly positive and has a bounded inverse.

Proof: its form is nonnegative, and a zero vector for this form belongs to ker H intersect ker R, which is zero. Bounded perturbation preserves compact resolvent. A nonnegative operator with compact resolvent and no zero eigenvector has strictly positive bottom eigenvalue. Thus S>=alpha I for some alpha>0. This does not require H to be invertible.

Define the finite Hermitian matrix

    M=R S^(-1) R*.

It is a positive contraction. Indeed ||R S^(-1/2)||<=1, since R*R<=S as forms.

## 2. Exact square identity

For y in C^L put u=S^(-1)R*y. Then Ru=My and

    <y,(I-M)y>=||y-Ru||^2+||H^(1/2)u||^2.       (2.1)

To verify, expand the right side and use

    ||H^(1/2)u||^2+||Ru||^2=<u,Su>=<u,R*y>.

The last scalar equals <y,My> and is real. This proves (2.1) with no unknown boundary remainder. The full Gamma, prime and Tate operators are retained in H and in the primitive-space adjoint R*.

## 3. Exact correspondence of kernels

The maps

    f -> Rf,                 y -> S^(-1)R*y

are inverse isomorphisms between ker H and ker(I-M).

For Hf=0, Sf=R*Rf, so S^(-1)R*Rf=f and MRf=Rf; injectivity of R on ker H prevents loss of a nonzero vector. Conversely, My=y implies by (2.1) that Hu=0 and Ru=y. Thus

    ker H={0} iff lambda_max(M)<1.              (3.1)

This repairs the earlier blanket objection to inverses: S^(-1) is legitimate at a hypothetical first contact, whereas H^(-1) is not available there.

## 4. What must be estimated

The exact identity (2.1) proves only M<=I. It does not prove the strict bound in (3.1). If f is a hypothetical zero mode and y=Rf, both squares in (2.1) are zero. The decisive arithmetic task is therefore a strict estimate for this explicitly defined matrix, valid at every hypothetical first-contact window.

For fixed T and a chosen finite observation, one possible rigorous method would enclose S^(-1) on the finitely many primitive exponential right-hand sides R*e_j, including a certified bound for the omitted infinite-dimensional part. A Galerkin computation without that bound is insufficient. No such enclosure or global estimate is supplied here.

The finite matrix still encodes the full inverse S^(-1); the reduction has not made the infinite-dimensional arithmetic problem finite at no cost. Nor does the existential choice of L give an algorithmic uniform bound in T.

## Status

Proved under the imported first-contact hypotheses: existence of the stabilized inverse; positive contraction M; square identity (2.1); exact kernel correspondence. Open: a strict arithmetic bound lambda_max(M)<1 sufficient to exclude first contact. D remains open.
