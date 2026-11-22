# State039 — Sign of the full arithmetic inverses on a wider tail

Status: PROVED and audited. Replaces STATE038 as working summary. Goal active, global sign OPEN, papers untouched.

## Signed infinite product: uniform result

POWER_INFINITE_SHOULDER_039 proves, at u=63/2, for ALL N>=4,000,000:

    h_N(x)>0 and K_N(x)>0 for ALL x>=exp(T_N),
    T_N=2(N−1)v_N/(u²−v_N²), v_N=1/2+1000/sqrt(N).

These are the FULL arithmetic inverses, with all Möbius integers. It is not a certificate of finite groups. The cutoff satisfies

    T_N=(N−1)/992+(1985·1000/992²)sqrt(N)+O(1)<(N−1)/330.

It improves the earlier cutoff026 for the SAME K_N; h_N is treated explicitly separately. T_N is here the logarithm of an x coordinate of the kernel, NOT the window T of Paper46.

## Mechanism and quantitative control

The gamma profile is tilted by v>1/2 and centred at t_v=2(N−1)v/(u²−v²). At sigma=v+1/2>1, the infinite Euler product, its moments and the sums used converge absolutely. Its signed multiplier in Fourier is kept, as in038, but now no outer coprime sum remains unestimated.

An elementary proof of psi_Lambda(x)<=2x gives A_sigma<=5/(sigma−1), B_sigma<=5/(sigma−1)² in the range. The Fourier normaliser is uniform for both profiles c=1/2 and3/2 and for v<=2; its mode is compared with the centre via Riccati. The translated profile stays on its positive physical side. For v between v_N and2, both ratios h/H and K/G lie between .9U_sigma and1.1U_sigma, where U_sigma=prod(1−p^−sigma)>=(sigma−1)/sigma>0.

Monotonicity of t_v covers a whole interval. From t_2 to infinity, a dilation bound m^−2 controls the absolute remainder and gives ratios greater than1/4. The WHOLE tail is thus obtained, without a campaign over indices nor arithmetic truncation.

## Evidence and remaining obligation

POWER_SHOULDER_AUDIT_039 approves the full proof and constants. Fourier, normaliser, elementary moments, Fubini for the infinite product, physical translated argument and union of tails were checked in three independent reviews. Exact verifier reproduced twice: PASS. It evaluates no new W values nor lists of primes.

The improvement relative to038 is control of the real infinite inverse in the declared region. It does not prove the sign of those kernels in the interior, nor compare their contribution with the adverse interior part and the archimedean term of W. The critical centre sigma=1 is not included either. No new row of W, arbitrary combination or window of Paper46 has been proved.

The coverage035 is kept: atoms of rows1..17, any k>=0, at u31.5 with W>norm²/40, in addition to the earlier regions and the atom211,1. Global closure requires an additional signed interior balance. The goal is declared neither complete nor blocked.
