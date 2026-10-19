# R161_072 — Exact recombination of the new balance and its coefficient test

## 1. The remainder is a reformulated equation, not an independent estimate

In the notation of R161_071 let

    u=Re<Bf,G_L f>, v=Re<B*f,G_L f>,
    c=<R_L f,D_(N,L)R_L f>, e=Re<R_L f,E_(N,L)f>.

R161_070 gives u=c-e. Reflection gives

    Re<(B+B*)f,S_L f>=2(u+v).

Consequently, even before the first-contact equation is used, R161_071's remainder obeys

    Q=2v-2e-Re m_T(f,S_L f)+Re<r,S_L f>
     =-2c-Re a_T(f,S_L f)+Re<r,S_L f>.          (1.1)

Here a_T denotes the full window form in the middle expression; its primitive restriction has the same notation elsewhere. At first contact a_T(f,S_L f)=<r,S_L f>, so Q=-2c exactly. The balance has no additional inequality beyond the input equation.

This does not make a separate proof of Q>=0 circular. It establishes that the test construction itself supplies no such proof. The earlier presentation of a newly constructed balance should be read as an exact expansion with an unproved sign, not as progress toward that sign.

## 2. Finite coefficient substitution

Replace Lambda(n) by arbitrary real numbers w_n>=0 for 2<=n<=N and set

    L_N^w=sum w_n n^(-1/2)V_(log n),
    d_(m,N)^w=sum w_n n^(-(a_m+1/2)).

Changing variables in the finite sums gives, verbatim,

    R_L B_N^w=D_(N,L)^w R_L-E_(N,L)^w.

The exterior integrals are the ones in R161_070, with w_n replacing Lambda(n). The positive detector is R*D_N^w R. If at least one w_n is positive, every diagonal entry of D_N^w is positive, and this detector is faithful by the same moment-completeness proof. No divisor identity was used. In particular one can take only w_2>0.

Thus positivity and faithfulness of the detector do not distinguish the actual von Mangoldt comb. The infinite identity c_m=-zeta'(2m+1)/zeta(2m+1) identifies its arithmetic weights, but the positivity proof never needs that identification. The construction contains arithmetic values without yet using the arithmetic relation that might force annihilation.

This substitution test is not a counterexample on actual first-contact states and does not establish independence from the complete physical hypotheses.

## 3. Dependence on inactive coefficients is exactly balanced

For N'>=N>=exp(2T), B_N is unchanged, while

    Delta e=Delta c,
    Delta Q=-2 Delta c.

This follows from R161_070(3.1), with M, f and r fixed. Increasing the inactive arithmetic tail increases the positive detector and decreases the candidate remainder by exactly the same amount. There is no improvement of the remainder sign from positivity of those added coefficients alone.

## 4. Consequence for the research step

The finite detector and collar formulas remain valid. The specific primitive test Pi(G_L+JG_LJ)f supplies an exact reformulation, with no new equality-state constraint. A successful comparison still needs a bound derived from the actual Gamma kernel together with the arithmetic coefficient relations, or another argument beyond this observation identity. Merely increasing N or L, applying parity, or recognizing the Dirichlet series does not provide it.

No new annihilation theorem is proved here. D remains open. This audit rejects only the inference that R161_070–071 already supply the missing arithmetic input; it is not a universal no-go theorem.
