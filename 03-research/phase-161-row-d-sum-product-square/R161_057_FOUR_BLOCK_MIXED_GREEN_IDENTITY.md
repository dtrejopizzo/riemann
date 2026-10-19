# R161_057 — Exact four-block form of the mixed Green identity

## 1. Decomposition

Let P_L, P_0, P_R be the left exterior, physical-window and right exterior projections. They commute with X. For

    a=Z_N Fcal f,  d=JZ_Nf,
    e=a-d,           c=a+d,

write a_j=P_ja and d_j=P_jd. The global Green identity of R161_042 decomposes without cross terms:

    Re<e,Xc>
      =sum_(j=L,0,R) [<a_j,Xa_j>-<d_j,Xd_j>].          (1.1)

Define the correctly oriented and wrong-side exterior energies

    G_phys=
       ||(X-T)^(1/2)a_R||^2
       +||(-X-T)^(1/2)d_L||^2,                         (1.2)

    G_wrong=
       ||(-X-T)^(1/2)a_L||^2
       +||(X-T)^(1/2)d_R||^2.                          (1.3)

Both are nonnegative. Direct substitution gives

    Re<e,Xc>
      =G_phys-G_wrong+T Phi_ext+G_0,                    (1.4)

where

    Phi_ext=
       ||a_R||^2+||d_L||^2-||a_L||^2-||d_R||^2,        (1.5)

    G_0=<a_0,Xa_0>-<d_0,Xd_0>.                         (1.6)

Equation (1.4) is exact at every finite cutoff. It records all four exterior ports; no support or scattering assertion is hidden in it.

## 2. Meaning of the two residual scalars

`Phi_ext` is an oriented exterior norm flux. Equality of the two complete history norms gives only

    Phi_ext
      =2[||d_L||^2-||a_L||^2]
       -[||a_0||^2-||d_0||^2]                         (2.1)

whenever a and d are exactly the two input/output histories of that colligation with the same source normalization. Equivalently it can be written with the right blocks. Thus total unitarity plus central metric equality does not kill `Phi_ext`; it leaves the one-sided flux difference. In the actual finite notation a-d=E_Nf, and R161_055 controls the central bracket asymptotically along a compatible common-graph diagonal. The remaining left flux is part of the second causal-orientation theorem, not an order-zero consequence of unitarity.

`G_0` is the interior first-moment flux. Expanding a_0=d_0+P_0E_Nf gives

    G_0
      =2 Re<d_0,XP_0E_Nf>+<P_0E_Nf,XP_0E_Nf>.          (2.2)

The final formula is legitimate on a smooth finite core. Passing it to a first-contact vector requires the differentiated graph/boundary control which ordinary L2 convergence does not provide.

## 3. Insertion of the critical jet

The exact critical identity is

    B_Nf=(K_NFcal-JK_N)f=Z_NM Fcal f-{X,C_N}f.         (3.1)

Pairing it with E_Nf gives

    Re<E_Nf,B_Nf>
      =Re<E_Nf,Z_NM Fcal f>
       -Re<E_Nf,XC_Nf>
       -Re<E_Nf,C_NXf>.                                (3.2)

Substitute (1.4) into the middle term. The primitive interior part of the last term is the horizontal-modulation radical pairing of R161_044. Its literal Tate part vanishes by opposite parity, R161_043. What remains after those two reductions is precisely the finite support commutator generated when Z_N is moved across P_0.

Consequently the missing identity is no longer an unspecified Green law. It is the equality

    G_wrong
      = boundary_commutator_N(f)+o(1),                 (3.3)

with the convention in which the primitive radical term and the opposite-parity Tate term have already been removed. If the PC-ren expansion proves that the boundary commutator equals zero (or is absorbed by the polar image with the sign opposite to G_wrong), then (3.2) and first-contact radicality give

    0=G_phys+nonnegative Gamma/polar remainder,         (3.4)

and the closure follows.

## 4. Exact block form of the support commutator

For every bounded finite synthesis Z and P=P_0,

    PZ-ZP=PZQ-QZP,   Q=I-P.                            (4.1)

Pairing after moving Z across P produces only the two off-diagonal blocks

    PZQ,  QZP.                                         (4.2)

For Z_N=S_N^ren, R161_006 computes PZ_NQ as a one-sided integer-minus-continuum discrepancy plus a rank-one opposite-tail Tate scalar. Reflection computes the other block. R161_009 fixes exactly those two rank-one scalars from the crossed Tate system. Therefore (3.3) reduces to the two one-sided discrepancies Delta_(N,T)^R and Delta_(N,T)^L; all scalar endpoint freedom has already been removed.

The unresolved statement is their quadratic reciprocity with G_wrong. It cannot be replaced by full-space adjointness, because (4.1) is exactly what full-space adjointness omits after compression.

## 5. Status

- exact four-exterior-port identity (1.4): proved;
- separation of oriented mass flux and interior first moment: proved; total unitarity alone does not cancel the oriented flux;
- reduction of the interior primitive/Tate pieces: inherited from R161_043-R161_044;
- reduction of the support commutator to the two one-sided discrepancies after Tate matching: proved from R161_006 and R161_009;
- quadratic reciprocity of those discrepancies with G_wrong: open;
- D: open.
