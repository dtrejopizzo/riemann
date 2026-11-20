# POWER_FULL_TRANSFER_PLAN_050 — MULTI scope and contacts needed for the tail comparison

Status: EXPLORATION SUPERSEDED by POWER_FULL_TWELVE_050. The computations of this plan remain valid, but the obligation E_(2,3) proposed as the next step was avoided via the reinforced margin0.02 and transport through thirteen poles with zero numerator. Do not treat NEXT as the current obligation. Papers untouched.

## Antecedents and difference

Consulted ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D and COMMON_TRANSFER010§6, GEOMETRIC_TRANSFER015§6, ARITHMETIC_BLOCK007 and R12_TRANSPORT049. The multiple filter with positive weights is earlier; the consequence that can now be applied is that049 and007 have proved their ENTIRE E2 orbit positive. A universal ordering of contacts is not retried, nor is contact3 assumed to have a favorable sign. The next possible construction must keep it exactly in matrices, and pay only the tail from4.

## MULTI corollary already obtained

Let u=63/2 and F0=P(s)/(s+u)^12, degreeP<12. The base007 and049 prove, with c=1/2500,

    E2[Q^jF0]>c||Q^jF0||², ALL j≥0.

For arbitrary finite rates v1,...,v12≥u, let F=P/∏(s+vi). MULTI015 proves

    E2[F]=Σw_j E2[Q^jF0],
    ||F||²=Σw_j||Q^jF0||²,
    Σw_j z^j=∏[ri/(1−(1−ri)z)], ri=u²/vi².

The weights are nonnegative and sum to1. Absolute convergence is preserved for E2 by the same continuity used in049. Thus

    E2[F] > ||F||²/2500, ALL twelve poles≥u.         (MULTI-E2)

There is no need to iterate R12 on intermediate bases. This consequence is for ARCH+POLAR+contact2, not for the full W.

## Preliminary tail computation, before another finite certificate

COMMON_TRANSFER010§6 proves uniformly on those twelve poles, with α=2/3 and σ=21,

    ||exp(21y)f||² ≤ B ||f||²,
    B=Σ_(j=0)^11 Σ_(k=0)^j binom(j,k)²(2/3)^(2k)/(1/3)^(2j+1)
     =1282776893780652,
    sqrt(B)<35815875.

By Cauchy, |c_f(logn)|≤sqrt(B)n^−21||f||². For every integer M≥3 and bounds L≥logM, s≤sqrt(M),

    |Σ_(n≥M)2Λ(n)n^−1/2 c_f(logn)|/||f||²
      ≤ (2·35815875/s)M^−21[L+ML/20+M/400].             (TAIL-M)

Indeed n^−21.5≤n^−21/s, Λ(n)≤logn and logx·x^−21 is decreasing from3. The comparison by first term plus integral gives exactly the indicated bracket. No prime or prime power in the range is removed.

Only the three adjacent cuts are evaluated, corresponding to keeping contacts2, then2,3, then2,3,4:

| Tail | L | s | TAIL-M majorant |
|---|---|---|---|
| n≥3 | 11/10 | 17/10 | <0.005126 |
| n≥4 | 7/5 | 2 | <0.000013763 |
| n≥5 | 17/10 | 11/5 | <0.000000146 |

The first computed bound is larger than c=0.0004; it does not allow concluding W from MULTI-E2. This is an insufficiency of THAT majorant, not a lower bound for the real tail nor an absolute necessity of keeping3 under any method. The second is less than c. Hence the minimal initial set of contacts that this comparison justifies attempting is{2,3}: if one proves

    E_(2,3)[Q^jF0]≥||Q^jF0||²/2500, ALL j≥0,F0∈V12, (NEXT)

MULTI and TAIL-4 would give W[F]>(1/2500−0.000013763)||F||² for all twelve poles. It would not be necessary to include4 for that margin. NEXT remains OPEN here; it requires a new analytic highpass cut and the exhaustive segment it determines. Contact3 has not been separated by absolute value in those blocks nor assumed favorable. No campaign was run to choose indices or contacts.
