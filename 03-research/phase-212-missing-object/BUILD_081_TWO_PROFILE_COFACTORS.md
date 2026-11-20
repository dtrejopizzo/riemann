# Construction 081 — Two-profile cancellation by cofactors

Status: explicit design, pending review; global sign OPEN.

Let g0=Q(1_I M), g1=Q(1_I M′), explicit primitive profiles. Let l0=0,l1=log2,l2=log3 and U_l the compressed causal shifts. Define

    D F(t)=det [[g0(t),g1(t),F(t)],
               [U_l1 g0(t),U_l1 g1(t),U_l1 F(t)],
               [U_l2 g0(t),U_l2 g1(t),U_l2 F(t)]].

The determinant is linear in F. Expanding along the last column,

    D F=c0 F+c1 U_l1 F+c2 U_l2 F,
    c0=(U_l1 g0)(U_l2 g1)−(U_l2 g0)(U_l1 g1),
    c1=(U_l2 g0)g1−g0(U_l2 g1),
    c2=g0(U_l1 g1)−(U_l1 g0)g1.

One has Dg0=Dg1=0 exactly, even at nodes and degeneracies of the determinant. No minor is divided by.

Define C=Σ_{j=0}²||c_j||∞, α=1/[2(1+C)], W=α Q D Q, V=JW. Then ||W||<1/2 and Wg0=Wg1=0. The profiles and coefficients are compactly supported BV; for F in the smooth core, WF belongs to the logarithmic domain of J.

For Z_jF=Q(c_j U_lj F), the square and the residue are

    ||VF||²=α²Σ_{i,j=0}² b(Z_iF,Z_jF),
    ρ(F)=Arch(F)−2Re<F,LF>−α²Σ_{i,j=0}²b(Z_iF,Z_jF).

No cross terms are discarded. The identity a_T=||V||²+ρ is exact on the core; ρ≥0 is not claimed.

## Arithmetic and degeneration risk

The delays 2 and 3 take part together, but the values of Λ do not appear in D. Multiplying each row by an arithmetic weight only multiplies D by the product of the weights. This is not a coupling that explains the sign, nor does it separate the rescaling of Λ. It is an explicit limitation of this design.

If a delay puts its whole row outside I, the row is zero and the determinant vanishes. In particular for 2T≤log3 the operator D is zero. A zero extraction is not interpreted as positivity of the residue.

The design is tested to check whether annihilating two profiles resolves the excess extraction seen in BUILD080. Annihilating a finite family does not by itself constitute a global proof.

## Review and test

The formulas, cofactor signs, annihilation and domain were checked independently. It was made precise that supp(DF)⊂(-T+log3,T). The final projection Q may extend the support, but it does not change the annihilation of the profiles.

NUMERICAL: the saved even test T=0.8 gives ||WF||²=9.4765538142759e−5 (Gauss64), 9.4765538142757e−5 (Gauss96). The sum of cofactor suprema was sampled: C≈1698.39301. Neither these suprema nor the saved value of the form were certified. Since the latter is ≈5.2943e−12, the first channel is still excessive. The two-profile cancellation does not improve this diagnosis compared with the one-profile corrector.

It is not proposed to resolve this by mechanically increasing the number of profiles. The lesson of the test is that annihilating explicit profiles separately does not necessarily reproduce the cancellations of the near-null vector. A coherent sum over pairs of delays would keep cross terms between pairs, unlike summing their norms, but a choice of coefficients that signs the residue has not yet been written.
