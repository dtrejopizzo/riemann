# POWER_FULL_THIRTEEN_053 — Full form positive on all thirteen real poles ≥63/2

Status: PROVED, exhaustive segment and constants PASS; independent review approved in POWER_FULL_THIRTEEN_AUDIT_053.md. Papers untouched.

**Theorem.** For any thirteen real rates v_i≥63/2, with multiplicities allowed, and every nonzero real polynomial P of degree<13,

    W[P/∏_(i=1)^13(s+v_i)] > ||P/∏(s+v_i)||²/4000.

The new gain is W>norm²/1000 on all fourteen poles≥63/2 with numerator vanishing at0. All arithmetic contacts and the polar are kept. Neither arbitrary dimension nor fourteen poles with general numerator is claimed.

## 1. Corpus and change relative to050/052

Consulted the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D, COMMON_TRANSFER010, FULLTEL014, MULTI015, CENTERED_CUTOFF049, FULL_TWELVE050 and CONFLUENT_THIRTEEN052.052 already proves W>norm²/4000 on confluent V13. The new piece is a FULL gain on fourteen poles with zero numerator, which transports that block to thirteen arbitrary poles. It is not assumed that positivity in codimension1 implies that of the whole block.

The first block E2[QV13] was certified rationally >norm²/125, with tools/power_zero_fourteen_endpoint_053_verify.py. The tail majorant from3 obtained with trace14 is0.0463807089, too large for that margin; even the term n=3 of THAT Cauchy majorant exceeds0.036. Hence keeping Λ exact only for n≥4 does not fix that particular comparison. This does not exclude another bound of the correlation operator.

So contact3 is kept exactly, in addition to2, and only the tail from4 is paid. No sequence of primes or dimensions was searched. The analytic cut J=96 and its audit were obtained BEFORE certifying the segment j=1,...,95.

## 2. Analytic highpass tail, already independently reviewed

CENTERED_MOMENT053 proves via a single rational moment matrix of dimension13, at j=96, that for EVERY nonzero F0∈V13,

    E_(Q^96F0)[tau^-2] <4/19845, Q(s)=s/(s+u), u=63/2.

Reweighting by q=|Q|² and the negative covariance with (1−q)/q propagate this bound to ALL j≥96 without checking additional matrices. The same memo, audited in CENTERED_MOMENT_AUDIT053, deduces

    ARCH[Q^jF0]>(12/5)||Q^jF0||².

The two contact coefficients satisfy v2+v3<137/60. The normalized polar on this orbit is less than3(169/992)^j<3/5^j<1/1000. Hence

    E23[Q^jF0]>(1/10)||Q^jF0||², ALL j≥96.           (TAIL-ORBIT)

E23 keeps ARCH, POLAR and contacts2,3. The arithmetic tail from4 is not yet included in TAIL-ORBIT.

## 3. Exact certificate of the exhaustive segment

The only remaining segment is j=1,...,95, with fixed margin c=1/500. The verifier tools/power_full_thirteen_053_verify.py builds108 Toeplitz bands E23. It uses rational intervals rounded outward with step10^−260; the logarithms use512 atanh terms and a positive geometric remainder.

The precision was fixed before execution: for direct log3, the remainder is less than2^−1022. The512 terms are evaluated with outward intervals in every sum, product and division; the remainder is added as a positive interval using r≤1/2. The accumulated error is not identified with a single rounding step: it is propagated in the endpoints and checked in the row-sum bound before the LDLs. This evaluation avoids huge intermediate denominators without changing the mathematical sum or the remainder. For degree≤107 and argument63log3<70, a coarse bound for the derivative of the polynomials involved is108·71^107<10^201. This bound explains the ample choice of precision; the final effective bound is verified directly from ALL interval endpoints, without assuming a number of digits preserved after cancellations. No floating-point precision is used to decide signs.

ARCH uses Hurwitz from16, exact sum up to CUT−1 with CUT=256, and Euler–Maclaurin with12 Bernoulli terms. The absolute periodic remainder is

    |B24|(p)_23 / [24!·256^(p+23)].

The bound of the periodic Bernoulli |B24({x})|≤|B24| is the same one used in ARCH_EXACT032, obtained from the absolutely convergent Fourier series of B24 and its value at0. Each rational coefficient of the band multiplies the EXACT Hurwitz endpoints BEFORE rounding them; thus a previous rounding is not amplified by u^r, as032 already warned. Gamma uses the same Euler enclosure with the remainder of007. The final centers have denominator10^24 and the sum of errors per row<ε=10^−12 is required BEFORE attempting the finite certificates.

The compression of Q^j is computed without a dense108 matrix. For the thirteen initial coordinates, Vandermonde gives exactly

    band_r(C_jᵀTC_j)=Σ_(d=−j)^j binom(2j,j+d)t_|r+d|,
    band_r(C_jᵀC_j)=binom(2j,j+r), 0≤r≤12,

with zero when r>j. The common factor4^−j is omitted. The operator error is paid as ε C_jᵀC_j. For each index of the segment a positive rational LDL is verified for

    C_jᵀTcC_j − (1/500+ε)C_jᵀC_j.

No index was chosen by floating eigenvalues; the full segment is determined by TAIL-ORBIT. The complete run finished exit0: PASS for108 bands, PASS for row error sum<10^−12 BEFORE the certificates, and95 PASS messages, one for each j=1,...,95. No threshold was relaxed. The earlier process was stopped only to replace a too-costly exact evaluation of the logarithms by the same series with per-term intervals; it had not produced a mathematical failure and its partial output was not used to choose indices.

## 4. Full transport and arithmetic tail

The95 positive LDLs and TAIL-ORBIT prove E23[Q^jF0]>norm²/500 for ALL j≥1. For any numerator D=sP of degree≤13, P of degree<13,

    G0=D/(s+u)^14=QF0.

MULTI015 with FOURTEEN factors expresses E23 and the norm of any G=D/∏_(i=1)^14(s+v_i), v_i≥u, as the same positive and absolutely convergent mixtures of Q^kG0. It follows that E23[G]>norm²/500 uniformly over all those restricted spaces.

The trace010 with n=14, α=1/2 is EXACTLY

    B_T14=947334302964<973312².

By Cauchy and Λ(n)≤logn, the full tail n≥4 satisfies

    ||tail||≤2·973312 Σ_(n≥4)(logn)n^−65/4.

Use n^−1/4≤5/7 for n≥4, log4<7/5 and first term plus integral of logx·x^−16, decreasing from4. The result is the rational

    L4=2·973312·(5/7)·4^−16
             [7/5+4(7/5)/15+4/225]
       =0.0005798513927...<1/1000.

Hence it is proved that

    W[G]>(1/500−L4)||G||²>||G||²/1000,
    ALL14poles≥u, D(0)=0.                            (ZERO14)

FULLTEL014 with n=13 keeps form, norm, polar and all contacts exactly. Its base052 has W>norm²/4000 and its corrections G_j belong to ZERO14, whose margin exceeds1/4000. One then obtains

    W[P/∏_(i=1)^13(s+v_i)]>norm²/4000,
    ALL13poles≥u, degreeP<13.                          (TARGET)

The FULLTEL identity used here is exact: with R0=∏u²/v_i²>0 and κ_j=(v_j²−u²)/u²·∏_(k<j)v_k²/u²≥0,

    W[F]−c||F||²=R0[(W[F0]−c||F0||²)
                         +Σ_jκ_j(W[G_j]−c||G_j||²)],
    G_j=sP/[(s+u)^(14−j)∏_(k≤j)(s+v_k)].

Each correction has fourteen poles and zero numerator; its ZERO14 margin exceeds c=1/4000. The same identity preserves the norm. The first base term052 is strictly positive, so TARGET is strict even when some rates coincide with u. Convergence of all prime series is absolute for these rational data with poles>1/2; no atom is omitted and the sign of the polar is not changed.

## 5. Scope

The fixed V13 of052 is extended to ALL thirteen real poles≥31.5 via a full arithmetic gain of fourteen poles with zero numerator. The moment bound and monotonicity replace all certificates j≥96, and the earlier segment was exhaustive and fixed analytically. Neither arbitrary dimension nor fourteen poles with general numerator is claimed, and no new T window of Paper47 is deduced here. The next case needs new verified hypotheses; the margins are not extrapolated by dimension. Papers untouched.
