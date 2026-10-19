# R161_046 — Backward closure audit and finite detection on the radical

## Scope correction

R161_038 refutes saturation from the listed abstract identities. It does not prove independence from the actual physical hypotheses. In particular, the previous conversational assertion that exterior reciprocity is a new axiom relative to the full physical construction was stronger than the evidence. Its status is unproved, not proved independent.

Likewise, the two expressions in R161_023 (5.3) agree by adjunction on their common domain. Merely reversing their order cannot generate a boundary term. A boundary term requires an explicitly different projection or domain; finite regularization must precede any unbounded limit.

## Backward dependency chain

The imported first-contact, nesting and cofinal results reduce D to exclusion of a nonzero primitive radical at any finite first-contact window. Their use remains conditional on those imported theorems with their precise domains.

For a fixed such window write N_T = ker Delta_T. Compact resolvent makes N_T finite dimensional (phase 121, P121_TATE_VOLterra_RADICAL_INVARIANCE_AUDIT, section 2). There are several sufficient routes:

1. Physical scattering implies vanishing of the Gamma residues and then F=0 (R161_019).
2. Removability at the positive odd Gamma poles suffices without full scattering (R161_024).
3. Vanishing of the positive pole energy suffices (R161_025).
4. On N_T only, finitely many pole moments suffice, as proved below.

These are sufficient conditions, not a proof that every possible closure must pass through global scattering or a determinant trivialization.

## Finite radical detection lemma

Fix T>0 and any finite-dimensional subspace N of L2(-T,T). Put

    a_m = 2m+1/2,
    ell_m(F) = integral F(t) exp(-a_m t) dt,
    N_M = N intersect ker ell_1 intersect ... intersect ker ell_M.

There is a finite M=M(N) for which N_M={0}.

Proof. The spaces N_M form a decreasing sequence of finite-dimensional spaces. There can be only finitely many strict dimension drops; consequently the sequence is eventually constant. Its eventual value is its intersection over all M. Moment completeness proved in R161_019 makes that intersection {0}. This proves the assertion. A plateau at one finite index alone does not prove eventual stabilization; a later moment may still reduce the dimension.

With positive weights b_m, there is therefore c_N>0 such that

    sum_(m=1)^M b_m |ell_m(F)|^2 >= c_N ||F||^2,   F in N.

Indeed the left side is continuous and strictly positive on the compact unit sphere of N. For N={0} the assertion is vacuous.

Applied to N_T, this proves that it would suffice to annihilate this finite observation on the radical. No bound for M in terms of dim N alone follows: the detecting indices can occur arbitrarily late for a general subspace. Nor does this construct N_T, prove any of its moments zero, or supply a uniform bound in T.

## What a finite source certificate must prove

For each m it would suffice to construct admissible primitive tests H_(m,n)F directly from finite PC data such that, for F in N_T,

    |ell_m(F)|^2 <= Re a_T(F,H_(m,n)F) + e_(m,n)(F),
    limsup_n e_(m,n)(F) <= 0.

Radicality kills the form term and proves ell_m(F)=0. Only finitely many instances are needed at a fixed radical, by the lemma. This is an acceptance criterion, not a constructed certificate. Defining H using an inverse of Delta_T or assuming the remainder sign would put the missing theorem into the hypothesis.

For the scattering route, the analogous target is merely X_T(F)<=0, since

    X_T(F)=||g||^2+epsilon<g,C_log g>
          =(1/2)||(I+epsilon C_log)g||^2 >=0.

This is equivalent to X_T=0 on these vectors; it changes the desired form of a proof, not its logical strength. R161_026 already uses the same sign-squeezing principle for Gamma displacement.

## Exact location of a compressed boundary term

Let P be the physical-window orthogonal projection, Q=I-P, and S a bounded finite synthesis. Whenever w,g belong to the Hilbert space,

    <g,Sw> = <PS*g,Pw> + <QS*g,Qw>.

If Pw=r is Tate forcing, the first term is <Tau PS*g,r>, where Tau is the orthogonal Tate projection inside the window. Neither term has an automatic sign. Their sum is exactly the original pairing. This is the literal block decomposition that a candidate reciprocity identity must control. The formula is asserted at bounded finite level; passage to a distributional w requires a separate convergence argument.

In particular, primitive radicality alone does not remove the second block. A proof must calculate that block from the integer translations, cosine kernel and polar corrections, or produce the finite moment certificates above.

## Status and next calculation

- Backward reduction to finite detection on each radical: proved, using imported compact resolvent and moment completeness.
- Independence from the complete physical hypotheses: not established; earlier stronger wording withdrawn.
- Finite PC certificate annihilating a detecting family: open.
- D: open.

The next calculation is a projected Laurent-coefficient pairing at one fixed positive odd Gamma pole, with the two blocks above retained. Its acceptance test is a derived remainder sign, not finite holomorphy, an adjoint reorder, or another identity defining X_T itself.
