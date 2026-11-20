# POWER_ARITHMETIC_WITNESS_006 — An exterior test that needs the comb and is repaired by 2

Status: PROVED by exact rational arithmetic; §§1–3 independently reviewed in POWER_AUDIT_006. §4 added later, independently reviewed. No paper modified.

Antecedents: POWER_CONFLUENT_FOUR_005 shows that the polar term can rescue ARCH. Here a different frontier is crossed: ARCH+POLAR is negative and the arithmetic comb is necessary for the sign of this test. This object differs from the previously positive exterior regions; it is not a claim about generic graphs nor about positive theta. Index/grid/crossword and the project rules consulted in POWER_BRIDGE_002.

## 1. Test and concrete result

Let u=63/2, phi_j(y)=sqrt(63)e^-uy L_j(63y)1_(y>0), 0≤j≤11, and h=Σv_j phi_j, where

    v=(2521,−3701,3730,−3278,2158,−793,
       −793,2158,−3278,3730,−3701,2521),
    ||h||²=N=99993678.

The attached certificate proves the three claims

    −2/125 < (Arch[h]+Polar[h])/N < −1/100,                (A)
    each prime-power contact contributes strictly positively,
    term of n=2 divided by N >1/25.                  (B)

Therefore the full form satisfies W[h]>(1/25−2/125)N>(1/50)N. The comb is not a small irrelevant perturbation: without it, this test has negative sign. Contact 2 alone suffices to repair the deficit, and all additional contacts help on this concrete test.

## 2. Autocorrelation and sign of each contact

The integral of two shifted Laguerre functions gives

    c_h(t)=e^-ut Q(2ut), t>=0,
    Q(x)=Σ(i<=j)v_i v_j [L_(j-i)(x)−L_(j-i-1)(x)], L_-1=0.

This is verified by integrating polynomials against e^-63y, or by using the rational orthonormal basis and residues; the terms i>j vanish. The coefficients of Q in ascending order are

    [99993678,49185301,13821792,−7615697/2,59520419/12,
     −128178871/60,39362105/72,−4637517/56,7669309/1008,
     −3136561/7560,133613/10800,−6355441/39916800].

The exact expansion of Q(x+40) has ALL its coefficients strictly negative. Hence Q(x)<0 and Q'(x)<0 for x>=40. Since log2>2/3, for every integer n>=2 one has 63log n>42>40. Therefore

    −v_n c_h(log n)=−2Lambda(n)n^-32 Q(63log n)>=0,

strictly if Lambda(n)>0. "Each term" is understood as each nonzero prime-power contact. No tail needs to be estimated to obtain the lower bound for W.

For n=2, the monotonicity of −Q and log gives the sufficient rational bound

    −2log2·2^-32 Q(63log2)/N
      >−(4/3)2^-32 Q(42)/N >1/25.

The second comparison is verified exactly. No rounded values of log2 are used.

## 3. Rational certificate of negative ARCH+POLAR

The archimedean matrix of order twelve in this basis is Toeplitz. Its diagonal is d=psi16−log pi, and its bands, for k>=1, are

    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

Set C_k=Σ(i=0..11−k)v_i v_(i+k). Using psi^(r)(16)=(-1)^(r+1)r!Σ(m>=16)m^(-r-1), one obtains directly

    Arch[h]=N d+Σ(r=1..11) T_r Σ(m>=16)m^(-r-1),
    T_r=(-1)^(r+1)u^r Σ(k=r..11)C_k binom(k−1,r−1).

The T_r are rational. The bounds for d from POWER_CONFLUENT_FOUR_005 are applied and, for each r, the sums m16..255 plus integral tails between 1/[r·256^r] and 1/[r·255^r]. No large floating-point numbers are subtracted: the whole exact combination is kept as Fraction.

The moments are the same as in dimension four:

    Polar[h]=126 [Σv_j(−32)^j/31^(j+1)]
                   [Σv_j(−31)^j/32^(j+1)].

The verifier `tools/power_arithmetic_witness_006_verify.py` proves (A), the sign of all shifted coefficients and (B). The rational intervals obtained in (A) are approximately (-.01534,-.01054), but these decimals play no part in the proof.

## 4. Removing only contact 2 does change the sign

The WHOLE remainder can be bounded from above without computing other primes individually. Write Q(x)=Σq_k x^k and r=k+1. Since Lambda(n)≤log n,

    Σ(n>=3) |−2Lambda(n)n^-32 Q(63log n)|/N
      ≤ (2/N)Σ(k=0..11)|q_k|63^k S_(k+1),

where S_r=Σ(n>=3)(log n)^r n^-32. For r≤12, the function (log x)^r x^-32 decreases on x≥3. Using 1<log3<11/10, the integral comparison and an exact binomial expansion give

    S_r ≤3^-32(11/10)^r
          +3^-31 Σ(j=0..r)binom(r,j)(11/10)^(r-j)j!/31^(j+1).

The verifier proves rationally that the full majorant sum is <1/500. The bounds 1<log3<11/10 are obtained from the same J/E with argument 1/2; no decimal evaluation is presupposed. Since AP/N<−1/100,

    W_sin_contacto_2[h]/N <−1/100+1/500=−1/125.

Consequently this test genuinely distinguishes the weight of contact 2: with all contacts it has positive margin >1/50; removing only 2 and keeping ALL the others it has negative margin <−1/125. Its powers 4,8,... are not removed: those contributions are part of the bounded tail.

## 5. Scope

This test exhibits concrete arithmetic compensation outside the region where ARCH+POLAR is positive. It is neither a counterexample to the full sign nor a certificate on all vectors of order twelve. The sign change from removing 2 is proved for this explicit exterior test; no broader consequences are attributed without an additional construction.
