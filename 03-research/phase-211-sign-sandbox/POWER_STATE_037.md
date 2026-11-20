# State037 — Signed grouping with explicit error and limit of the absolute remainder

Status: PROVED and audited. Replaces STATE036 as working summary; keeps the positive coverage035. Goal active, global sign OPEN, papers untouched.

## Result on the real arithmetic

POWER_ENERGY_GROUP_037 studies H_N(x)=−d[x^(-1/2)rho_N(logx)]/dx, at x_N=exp((N−1)/992), asymptotic centre of the polar energy. At fixed rate63/2, M_N=u²/(2N−3), it proves for all m>=1:

    exp(−M_N[log(m)/1985+log²(m)/2])/m
       <= m H_N(mx_N)/H_N(x_N) <= (1+M_N log(m))/m.

The critical behaviour is1/m. An elementary count of squarefree integers and these bounds prove that the absolute sum of the non-principal Möbius terms exceeds1 for ALL N>=2^16. This refutes absolute contraction at the real energy centre, unlike the region m^(-2) of033. It does not determine the sign of the signed sum.

## Concrete gain from keeping signs before the error

For Q a finite product of primes, the grouped kernel K_(N,Q)(m) keeps exactly as principal term U_Q/m, U_Q=prod(1−1/p). An explicit error is proved through the two moments of log(b) under the weights1/b of its divisors. A uniform condition guarantees K_(N,Q)(m) between U_Q/(2m) and3U_Q/(2m) in a window logm of order sqrtN for fixed Q. It is the sign of an auxiliary grouped kernel, not the sign of W.

The growing choice Q=prod_(p<=floor(N^(1/8)))p allows, for ALL N>=2^80, relative error<.01 on the whole window m<=exp(3N^(1/4)). However a proof by inclusion–exclusion and square counting shows that the sum of moduli of the grouped remainder exceeds1.48, while the principal group is<.505. Hence this choice does not close the problem through absolute domination of the remainder either. The outer sum with its signs remains open.

## Scope and evidence

POWER_GROUP_AUDIT_037 approves the kernel and the growing extension. Both were reviewed and the extended exact verifier reproduced: PASS; an independent run also PASS. The use of integer counting was corrected via discrete Abel summation. The uniform theorems are analytic; no new W data were evaluated and no campaigns of primes or Möbius were enumerated.

The novelty relative to018/030/031 is not another formal cancellation of the principal term: it is a quantitative inequality of the real profile and of its finite grouping. Even so, the error majorant of order log²(m)/m cannot be summed to infinity. Control of the signed arithmetic complement and its integral is missing. It is not claimed that other groupings are impossible.

There is no new positive coverage of W nor window T. Rows1..17, any k>=0, at u31.5 with W>norm²/40, the earlier regions and the atom211,1 are kept. The global objective remains open. The continuation must supply new signed control of the complement; improving only constants of the same absolute bounds does not resolve the obligation.
