# POWER_CELL_BALANCE_024 — Local budget of negative K and exterior cells

Status: **PROVED** uniform per-cell inequality tolerating negative K; **PROVED** strictly positive tail of cells for every N. The targeted interior cell N129 is certified separately in POWER_CELL_TEST_024.md. No sign of all cells nor of W is claimed. Papers untouched.

## 1. Corpus and precise difference

Read the project rules, SIGNED_MEAN019 (PAIR), INVERSE_KERNEL020 (OUTER), CUMULATIVE_INVERSE022§§3,7 and CUMULATIVE_TEST023. Consulted the index (Euler/Möbius/summation by intervals), the master grid and CROSSWORD-TO-D.md, with state023 recording the COMPLETE refutation K129(1)<0.

The difference from the previous criterion is to measure how much NEGATIVE K ONE cell can tolerate, with an explicit buffer J(n) and an exact integrated constant. Universal pointwise positivity is not assumed again, nor is the sign of a sum inferred from a prefix. The auxiliary identities are used to prove that one-sided inequality and the localization of every possible lesion to a finite number of cells per N. The exterior consequence expressly uses the already known theorem020; it is not presented as a new global arithmetic mechanism.

## 2. Cell and notation

Keep u=63/2, J_N(x)=int_x^infty h_N, K_N=J_N+xh_N=J_N−xJ_N'. The Möbius sums are COMPLETE and their uniform/absolute convergence is proved022. For n>=2 define

    S_N(n)=H_(n−1)int_(n−1)^n J_N(x)dx−logn J_N(n),
    b_n=H_(n−1)(1−1/(2n))−logn,
    a=3/4−log2>0.

The slopes−H_(n−1) and jumps logn of the SAME B give

    sum_(n>=2)S_N(n)=−F_N/2.

This identity by itself proves no sign. Lemma022 gives b_n>=a for all n>=2 and H_(n−1)/(2n)<=1/4.

## 3. One-sided inequality keeping negative K

**Theorem.** For all N,n>=2, with no hypothesis on the sign of K or J,

    S_N(n)=b_n J_N(n)
       +(H_(n−1)/2)int_(n−1)^n [1−(n−1)²/t²]K_N(t)dt.       (LOCAL)

In particular, if M_N(n)=sup_(n−1<=t<=n)K_N^−(t),

    S_N(n)>=b_nJ_N(n)−[H_(n−1)/(2n)]M_N(n).                (BUFFER)

Proof. The exact differential identity gives, for n−1<=x<=n,

    J_N(x)=xJ_N(n)/n+x int_x^n K_N(t)/t²dt.

Integrating and swapping over the FINITE triangle (x,t) produces LOCAL. Discarding only the positive part of K gives the bound, because the weight is nonnegative and

    int_(n−1)^n [1−(n−1)²/t²]dt=1/n.

Neither the jump logn is lost nor K replaced by its modulus in a sign identity. QED.

**Sufficient integrated criterion.** If J_N(n)>=0 and M_N(n)<=4a J_N(n), then S_N(n)>=0. Indeed BUFFER>=aJ_N(n)−M_N(n)/4. The criterion allows K<0 in the cell; it is distinct from the universal hypothesis K>=0 refuted023. It is not claimed that its two hypotheses are proved for every real cell.

A finer variant keeps the integral of K^- in LOCAL instead of using the supremum. BUFFER quantifies a margin, but does not by itself constitute an arithmetic bound on M_N(n).

## 4. All exterior cells are favorable, for EVERY N

Let X_N=exp((N−1)/30). By OUTER020, h_N(x)>=H_N(x)/4>0 for x>=X_N. Hence, on EVERY n with n−1>=X_N,

    J_N(n)>=w_N(n)/4>0,
    J_N(x)>=J_N(n) for n−1<=x<=n.

In particular K_N>=0 there by022, and LOCAL proves the quantitative bound

    S_N(n)>=b_n J_N(n)>=a w_N(n)/4>0.                    (OUT-CELL)

In fact the preceding monotonicity also gives the stronger bound (H_(n−1)−logn)w_N(n)/4; it is not needed for the conclusion. Thus for each N any possible adverse cell lies among the FINITELY many cells whose left endpoint is less than X_N. This does not prove that an adverse one exists nor that the total sum is positive; it keeps an explicit favorable tail.

## 5. Targeted interior test and coordination

The only authorized interior point is the first cell of the SAME N129 that refuted K>=0. Its certificate and complete Möbius tail belong to the companion memo024; no other sweep is carried out here nor is anything extrapolated from that case.

To reproduce an integral without quadrature, write w_N=x^(−32)P_N(logx) and Q_N positive solving31Q_N−Q_N'=P_N:

    q_d=p_d/31,
    q_j=[p_j+(j+1)q_(j+1)]/31,
    T_N(x)=int_x^infty w_N(y)dy=x^(−31)Q_N(logx).

Then, with COMPLETE Möbius,

    int_1^2 J_N(x)dx
      =sum_(m>=1)mu(m)m^(−32)[Q_N(logm)−2^(−31)Q_N(log(2m))],
    J_N(2)=2^(−32)sum_(m>=1)mu(m)m^(−32)P_N(log(2m)).

These are exact identities with absolute tails controllable by the same positive polynomials and gamma integrals022. They are included here as a computational interface, not as an interior sign proof.

## 6. What is missing for the complete form

Even proving S_N(n)>=0 for ALL cells would only give F_N<=0. The correct formula is

    W[g_N]/C_N(0)=ARCH_sharp[g_N]/C_N(0)+2sum_(n>=2)S_N(n).

If ARCH_sharp is negative, the quantitative bound sum S_N(n)>=−ARCH_sharp/[2C_N(0)] is missing. OUT-CELL does not automatically control the interior cells nor that deficit. BUFFER may allow an integrated certificate surviving K129(1)<0, but it needs genuine estimates of its terms with the real arithmetic kernel. Writing LOCAL or summing Euler identities is not declared to fulfil that obligation.


## 7. Approved continuation025

POWER_INVERSE_LOGCONCAVITY_025.md proves K129(x)>0 for ALL x>=2 via specific log-concavity of D129 and a rational cutoff. Hence all cells n>=3 are favorable. Combined with S129(2)>33/100 from CELL_TEST024, one obtains COMPLETE ERR129<−33/50. The comparison with ARCH_sharp remains pending. This continuation does not assume K>=0 on[1,2] and keeps falsifier023. Independent audit025 approved.
