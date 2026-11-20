# POWER_GAMMA_129_DECISION_061 — Complete decision of the pending interior case129,0

Status: PROVED, rational certificate PASS and independent review approved in POWER_GAMMA_129_AUDIT_061.md. A single historical atom; not a campaign of orders nor a uniform claim. Papers untouched.

## 1. Result and reason for this case

For u=63/2, N=129 and

    g_N(t)=t^(N−1)exp(−ut)/(N−1)! ·1_(t>0),
    G_N(s)=1/(s+u)^N,

it is proved, with ALL arithmetic contacts and the polar, that

    1.34·10^−10 < W[g129]/||g129||² <1.35·10^−10.       (DECISION)

This case was explicitly pending in025/026/027.025 proved ERR129<−0.66;026 showed that this coarse guarantee did not cover the ARCHsharp deficit;027 controlled only a joint tail. A search of the corpus, the index ROUTES-TRIED-INDEX, the grid R162_2300_MASTER_GRID and CROSSWORD-TO-D found no later decision in032/035/042. No new N was chosen: this round took up a concrete obligation already recorded within the authorized work.

The difference is to replace the separate coarse bounds by the stable ARCH of032, rational polar, sum of all contacts up to512 and a rigorous full tail. Neither the Euler–Maclaurin method nor the sharp identity018 is presented as new. A single preliminary evaluation only checked the feasibility of a small certificate; the final proof uses neither quadrature nor floating-point numbers.

## 2. Norm and stable archimedean formula

Set d=128. The original norm, WITHOUT additional renormalization, is

    c0=||g129||²=binom(256,128)/63^257.

Write the exact normalized autocorrelation

    ρ(t)=c_g129(t)/c0=exp(−ut)Σ_(r=0)^128 a_r t^r/r!,
    a_0=1,
    a_r/a_(r−1)=2u(d−r+1)/(2d−r+1).

All a_r are positive rationals. ARCH_EXACT032§2 proves

    ARCH/c0=ψ(16)−logπ−Σ_(r=1)^128(a_r/2^r)S_(r+1),
    S_p=Σ_(m=16)^∞m^−p.

The subtracted summands are positive; no alternating combination of huge derivatives is used. As in032, S_p is enclosed via direct summation16,...,31, Euler–Maclaurin with8 Bernoulli terms and absolute periodic remainder

    |B16|(p)_15/[16!·32^(p+15)].

The coefficients a_r/2^r multiply the rational endpoints BEFORE rounding them. Gamma, logπ and the logarithms come from the audited module power_fixed_grid_003.py. The final certified width of ARCH is<10^−18.

The normalized polar is the exact fraction

    POLAR/c0=2/[(u²−1/4)^129 c0].

## 3. Full arithmetic up to512 and adverse tail

All contacts of k0 are adverse: ρ(t)>0 for t≥0, by the positive gamma formula018. For each prime power q=p^m, the normalized magnitude is

    C_q=2logp ·q^−32 Σ_(r=0)^128 a_r(logq)^r/r!.

The power q^−32 is EXACT: it combines exp(−u logq) and q^−1/2, without approximating exponents or roots. The verifier tools/power_gamma_129_decision_061_verify.py generates all primes by deterministic integer division and all their powers up to512, including4,8,...,512. For a prime power Λ(q)=logp is used, not logq.

The polynomial is evaluated by Horner in divided powers, with all its coefficients positive. Division by q^32 is done first on the rational endpoints, as in032, avoiding premature rounding of a very small reciprocal.

Let q_N(t)=−ρ′(t)/ρ(t). ROOT026 and q_N′>0 give, for t≥log512>6,

    q_N(t)>16,

since the exact sufficient condition is

    u²>16²+2·128·16/6,

which is verified rationally. Hence for x≥512,

    ρ(logx)≤ρ(log512)(x/512)^−16.

The function logx·x^−33/2 decreases from512. Since the tail starts at513, no additional first term: the sum is bounded directly by the integral from512. Thus

    0≤Σ_(q>512)C_q
      ≤2ρ(log512)√512 [2log512/31+4/961]
      =2·512^−31 P(log512)[2log512/31+4/961],
    P(t)=Σa_rt^r/r!.

The last expression has only rational intervals: √512 cancels exactly with the exponent of ρ. Its certified value is<10^−24, with decimal evaluation of the majorant approximately1.9408294·10^−26. The tail is ADVERSE and is subtracted for the lower bound of W; it is not discarded by a nonexistent favorable sign.

## 4. Rational output and decision

The final run finished exit0 and PASS. Rounding outward, the normalized intervals are:

    ARCH/c0 ∈[−209403793025407910633,−209403793025407910630]/10^20,
    POLAR/c0 ∈[263311994766765745833,263311994766765745834]/10^20,
    Σ_(q≤512)C_q ∈[53908201727901151035,53908201727901151036]/10^20.

ARCH+POLAR−comb is summed and the majorant of the WHOLE tail is subtracted for the lower endpoint. The result is

    W[g129]/c0 ∈[13456684165,13456684168]/10^20,

which proves DECISION. The interval has a wide margin relative to the archimedean error and the tail; there was no need for massive precision nor for successively modifying cuts.

## 5. Exact compensation missing in025/026

The sharp resolvent is evaluated rationally:

    S=E[1/(τ²+1/4)]=2Σ_(r=0)^128 a_r/32^(r+1).

The identity is obtained from the kernel exp(−|t|/2), by Plancherel and the same autocorrelation. Thus

    ARCHsharp/c0=ARCH/c0+S,
    ERR=Σ_(q≥2)C_q−POLAR/c0+S,
    W/c0=ARCHsharp/c0−ERR.

The ERR is that of018/025, with E0(x)=ψ_Λ(x)−x+1 and endpoint E0(1)=0. No other term2 is added nor is the guarantee0.66 already included in that ERR added again.

The certificate obtains

    ARCHsharp/c0 ∈[−104219397018062543067,−104219397018062543064]/10^20,
    ERR ∈[−104219397031519227232,−104219397031519227231]/10^20.

The real benefit −ERR is approximately1.04219397031519, and the real deficit −ARCHsharp is approximately1.04219397018063. Their positive difference is only1.3456684·10^−10. The claim ERR<−0.66 was correct, but lost a substantial part of the benefit and all this cancellation precision.

There is also a quantified interior datum without recomputing another cell.024 already certified33/100<S129(2)<1/3, while025 identifies exactly −ERR=2Σ_(m≥2)S129(m). Hence the contribution of ALL other cells satisfies

    0.3755 <2Σ_(m≥3)S129(m)<0.3822.

These contributions are the same ones of the balance, not a benefit summable a second time. They show that the interior remainder, although favorable in025, contributes an essential amount to overcome the deficit; it is not enough to keep only the first cell nor the mere sign of ERR.

## 6. Scope and reproduction

An INTERIOR scalar case k0 that remained open is decided, with the full real Λ and the original archimedean constant. In particular K129(1)<0 of023 did not imply negativity of W: the full integrated balance is positive. This does not rehabilitate universal K≥0 nor presume that the pointwise kernel has the desired sign.

No row, propagation inequality in N, or result for130 or other orders is inferred. The datum that a future propagation must preserve is the signed balance with precision relative to the small residue, not only separate bounds of constant order. No new time window T nor global sign is deduced. Papers untouched.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_gamma_129_decision_061_verify.py
