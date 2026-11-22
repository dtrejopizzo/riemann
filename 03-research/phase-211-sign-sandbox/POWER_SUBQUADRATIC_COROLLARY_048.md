# POWER_SUBQUADRATIC_COROLLARY_048 — Extraction of a sign region from the bounds 017

Status: **PROVED as a corollary of the audited inequalities 017; independent review APPROVED in POWER_SUBQUADRATIC_AUDIT_048.md and derivation reviewed.** It is not a new arithmetic inequality nor a global closure. Papers untouched.

## 1. Prior consultation and exact difference

Read the project rules, STATEMENT_001, ROUTES-TRIED-INDEX/README, master grid and CROSSWORD-TO-D; reviewed SCALAR_BRIDGE017, QUADRATIC017, QUADRATIC_EXPLICIT017, DESCENT016, TABLE_DESCENT018, RECURRENCE_BOUNDARY036 and the states 046/047. The specific search for `subquadr`, `sub.quadr`, `loglog`, `log log N` and `log\\log N` in the index, grid, crossword and POWER files found no region of this form already made explicit.

The tool is entirely QUADRATIC017: no other proof of the band estimate is retried, nor is that route given another name. A quantitative consequence is extracted by letting its parameter c depend on N and tend to zero. The precise reason that allows this extraction is that STRIP, PRIME, ARCH and POL are inequalities valid for EACH c>0, N>=2 and k>=max(cN²,4N), with explicit constants; the eventual statement with N0(c) is not used without controlling its dependence.

The explicit result 017 had fixed c; QUADRATIC_EXPLICIT017 covers k>=10000N² from N=2. Here the frontier is 2N²/log log N. For each fixed positive c, this frontier lies below cN² for N large enough. It is new explicit coverage of the table, obtained from existing bounds. No new method is declared, nor is control of the full interior claimed.

## 2. Candidate and result

Fix u=63/2. For integers N>=exp(1000000) and

    k >= 2N²/log log N,

let f_(N,k) be the causal function with transform s^k/(s+u)^(N+k). Then, for the COMPLETE real form of 017,

    W[f_(N,k)] > (2/5) log N · ||f_(N,k)||².             (SUBQUADRATIC)

The statement covers ALL orders of that unbounded region and ALL k above its frontier. No order N or contact has been evaluated numerically. The threshold is deliberately conservative.

## 3. Four exact bounds imported from 017

For any c>0 under N>=2 and k>=max(cN²,4N), QUADRATIC017 proves

    C(c)=1+2[exp(4/(25c))+exp(1/c)],
    |Comb[f]|/||f||² < 14C(c),
    ARCH[f]/||f||² >= (1/2)log N + log[u sqrt(c)/(2pi)] - 5,
    |Polar[f]|/||f||² < 400^(-k).

The Comb bound sums the complete INFINITE comb using the shift of the joint rational DENSITY; it does not separate two time norms. The polar is the complete real one and is kept even when its sign is unfavourable. The four inequalities are finite and uniform in the indicated region. Neither the Gaussian approximation of 017 nor passing a limit through an arithmetic sum is needed.

## 4. Variable choice and check of all hypotheses

Write L=log N>=1000000 and choose

    c_N = 2/log L > 0.

The condition of the theorem is exactly k>=c_N N². Also c_N N²>=4N: it suffices that N>=2log L, and

    N=exp L >= L²/2 >= 2L >= 2log L

for L>=1000000. The first inequality uses only one positive term of the exponential series. Therefore ALL hypotheses of the bounds 017 hold with this choice c_N, without invoking any c-dependent N0.

Now

    exp(1/c_N)=sqrt L,
    exp(4/(25c_N))=L^(2/25)<=sqrt L,
    C(c_N)<=1+4sqrt L.

Moreover u sqrt(2)/(2pi)>1, using u=63/2 and pi<4. Thus

    ARCH[f]/||f||²
      > (1/2)L - (1/2)log log L - 5.

For L>=1000000 one has log log L<=log L<=sqrt L. The second inequality holds from L=16: at 16 it uses log16<4, and the derivative of sqrt L-log L is nonnegative for L>=4. The first follows from log L<=L and monotonicity of the logarithm.

## 5. Complete balance and margin

The polar bound is less than 1. The previous estimates give

    W[f]/||f||²
      > (1/2)L - (113/2)sqrt L - 20.

Set y=sqrt L>=1000. Then

    (1/10)y²-(113/2)y-20
      >=(87/2)y-20 > 0,

since y²/10>=100y. Therefore the last lower bound is strictly greater than (2/5)L. This proves SUBQUADRATIC with all constants symbolic and without a numerical campaign.

## 6. Scope relative to 036 and 046

This extraction does not prove the uniform -o(1) hypothesis over the WHOLE pending band of 046. What remains is k<2N²/log log N and N not covered by other results.

Nor is RECURRENCE_BOUNDARY036 cancelled. Its conclusion refers to the energy of the fixed cone k'>=10000N'²; enlarging the sign region here does not automatically convert the complement of a diagonal frontier into vanishing energy. No estimate of that new complement has been proved, nor is it eliminated by a mass count. The complete table and the global sign remain **OPEN**; there is no new certified window T of Paper 46.
