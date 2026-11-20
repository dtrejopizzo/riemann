# POWER TABLE AUDIT 018 — independent review

Status: APPROVED, with delimited scope. Date: 2026-11-05. Papers untouched.

## 1. Rows N=2 and N=3

Reviewed `POWER_TABLE_DESCENT_018.md` and ran its exact verifier `tools/power_table_descent_018_verify.py`: PASS. A second independent review agrees.

For all u≥63/2 and k≥0, both rows satisfy W[f_Nk]>||f_Nk||²/8. The normalization is f_Nk(s)=s^k/(s+u)^(N+k). The exact recurrence is a_Nk=a_N,k+1+u²a_N+1,k. Therefore the strict first and second differences of the row N=1 are certified; differences of higher orders are not deduced.

Checked: archimedean monotonicity in k by covariance; A20=d−ud′>2/5 and A30=d−ud′+u²d″/3>3/20; uniform weighted ratios R2=4641/11 and R3=15658881/1331 at the endpoint u=63/2, decreasing in u; costs of the complete comb less than .003 and 1/60; polar of N=2 in absolute value less than .26 and negative polar of N=3 less than .001. The resulting sums exceed 1/8. The parity of the polar of N=3 is essential and is used correctly.

## 2. Budget of the low row

Reviewed and approved `POWER_LOW_TABLE_018.md`. It does not supply a new sign: it quantifies exactly the absolute budget of the already existing route E0.

With E0(x)=ψΛ(x)−x+1, E0(1)=0 and C_N the positive decreasing autocorrelation, integration by parts gives

F_N=(2/C_N(0))∫₀∞ E0(eᵗ)e^(−t/2)(C_N(t)/2−C_N′(t))dt.

The term +1 and the endpoint x=1 are correct. Under the hypothesis |E0(x)|≤Ax^θ, 0≤θ<u+1/2, the exact budget is D_N(θ)=2+2θJ_N(θ−1/2), with J_N(b)=∫₀∞e^(bt)C_N(t)/C_N(0)dt. Verified: D_N(0)=2; the limit 1/(1/2−θ) if θ<1/2; growth of order √N if θ=1/2; and of order √N(1−(θ−1/2)²/u²)^(−N) if θ>1/2. The last regime uses the two-sided cosh bounds and requires θ−1/2<u. No signed control of the residue has been obtained.

## 3. Exact falsifier of the structural inference

This model is not the arithmetic form W. It shows that the recurrence, filter identities and the certified positive regions do not suffice, by themselves, to complete the table.

Fix u₀=63/2, ε=1/100 and the arcsine probability ν(dq)=dq/(π√(q(1−q))). Let μ=2ν−εδ₁/₂. The form on real causal rational functions is

V[f]=2||f||²−εu₀|F(iu₀)|².

With q=τ²/(u₀²+τ²) and F₁(s)=1/(s+u₀), it is equivalent to integrating |F/F₁|² against μ/(2u₀). For the table with pole u₀,

b_Nk=∫q^k(1−q)^(N−1)dμ,   a^V_Nk=b_Nk/(2u₀^(2N−1)).

The pointwise identity q+(1−q)=1 gives exactly the same Pascal recurrence and the complementary/binomial identities. The convergent geometric identities are also preserved. No gamma or von Mangoldt identity is postulated for V.

### 3.1. Margins of blocks and rows

In any rational space of m≤12 poles v_j≥u₀, including repeated poles, the Malmquist basis gives

Σ_j|φ̂_j(iu₀)|²=Σ_j 2v_j/(v_j²+u₀²)≤m/u₀.

Cauchy implies V[f]≥(2−εm)||f||²≥47||f||²/25. Thus it preserves, with a larger margin, all block certificates of up to twelve poles, including all their crossings and the eight arbitrary poles.

It also preserves the three complete rows for any pole v≥u₀. Write q_v=u₀²/(v²+u₀²)≤1/2. The ratio of the evaluated term to the norm is

[2u₀v/(v²+u₀²)] q_v^k(1−q_v)^(N−1)/(B(k+1/2,N−1/2)/π).

The first factor is ≤1. For N=1, c_k=binom(2k,k)/4^k≥2^(−k) gives ratio ≤1. For N=2 the maximum is ≤2: k=0 directly; for k≥1 the mode k/(k+1)≥1/2 allows maximizing at q=1/2. For N=3 the bound is 8/3: k=0 directly; k=1 gives 64/27<8/3; k≥2 again maximizes at 1/2. At q=1/2 the consecutive quotients are (k+N)/(2k+1), with maximum at k=N−1 or N. Hence the margins are respectively 1.99, 1.98 and 2−(8/3)ε, all larger than the real certificates. The corresponding difference inequalities are preserved.

### 3.2. Positive cone and eventual positivity

Let h(q)=q^k(1−q)^(N−1), d=h(1/2). Since ν≥dq/2,

∫h dν≥(1/2)∫h dq≥(1/2)(3/4)^k8^(−N),

integrating over q∈[3/4,7/8]. If k≥6N, (∫h dq)/d≥(3/2)^k/2^(2N+1)>1. Hence the ratio of the negative atom to the mass ν is ≤2 and V/||f||²≥2−2ε=1.98. In particular the whole cone N≥2, k≥10000N² and its margin 49/50 are preserved.

For each fixed order, the evaluated atom after Q^k decreases exponentially, while the norm decreases only as a power of k. The statement is uniform in any fixed finite-dimensional space of numerators. Therefore eventual positivity of each fixed row/space is also preserved. It is not claimed that V reproduces the precise logarithmic growth of W.

### 3.3. Explicit negative interior entry

Take N=n+1, k=n. Then

4^n b_Nk=2c_n−ε,   c_n=binom(2n,n)/4^n.

The induction c_n≤1/√(n+1) follows from c_(n+1)/c_n=(2n+1)/(2n+2): the required squared inequality has difference 3n+2>0. With n=201²=40401,

2c_n≤2/√40402<2/201<1/100.

Therefore b_40402,40401<0, and also a^V_40402,40401<0. This entry lies outside the finite blocks and the certified cone.

## 4. Scope conclusion

Rows 2 and 3: new effective positive sign of the whole row. LOW_TABLE: exact budget of a previous route, without additional sign. Model μ: logical obstruction to completing the table through only the identities and regions already proved; not a counterexample to W nor to the sought positivity. The pending distinction must use additional information about the concrete arithmetic form. None of these results by itself certifies a new window T.
