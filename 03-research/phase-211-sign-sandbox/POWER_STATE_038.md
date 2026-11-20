# State038 — Signed error via Fourier and enlarged grouping window

Status: PROVED and audited. Replaces STATE037 as working summary; keeps its W coverage. Goal active, global sign OPEN, papers untouched.

## New inequality on the same real profile

POWER_SIGNED_MOMENTS_038 keeps the finite Möbius product in Fourier. For the real gamma profile f_N of037 extended through even rho, it defines M_Q f=U_Q^(-1)sum_(b|Q)mu(b)f(ell+logb)/b, A_Q=sum logp/(p−1), B_Q=sum p(logp)²/(p−1)². For ALL real ell, N>=16 and B_Q<=N/1000:

    |M_Q f_N(ell)−f_N(ell−A_Q)|
      <=12000 B_Q/N +65 sqrt(N)(V_Q/U_Q+1)exp(−N/2000).

The difference relative to037 is substantial and quantitative: V_Q/U_Q disappears from the central error and remains only in an exponentially small tail. The principal term is an exact translation of the real profile, not a constant or a supposed positive average. The operator remains signed; Jensen is not applied to its weights.

The explicit gamma transform, a normaliser with positive auxiliary density and a Gaussian envelope allow inverting Fourier with controlled absolute errors. The extended profile may change sign; only the auxiliary density used for the normaliser is positive. The comparison between the mode and the central point is proved via Riccati, before using Chebyshev.

## Corollary for the same growing grouping037

For ALL N>=2^80, Q=prod_(p<=floor(N^(1/8)))p and

    A_Q <= logm <= A_Q+sqrt(N)/100,

one proves for the REAL grouped kernel

    (4/5)U_Q/m < K_(N,Q)(m) < (6/5)U_Q/m.

The translated profile is on its positive physical side, and each error is less than1/100. The certified logarithmic length goes from order N^(1/4) in037 to order sqrtN. These are validity windows of an auxiliary kernel: they are not windows T of Paper47. It is not claimed that the new interval contains m1 nor that its sign controls the outer sum with Möbius coefficients.

## Evidence and pending obligation

POWER_SIGNED_AUDIT_038 approves theorem and corollary. Fourier, normaliser, constants and scope were checked in three independent reviews. Exact constant verifier reproduced twice: PASS. No new W cases nor lists of Q were evaluated.

The local improvement does not yet control the infinite sum over m coprime to Q nor its integral in the polar−comb residue. The error B_Q/N does not by itself provide the precision needed against exponential components either. The next step must control that signed complement without summing a non-summable majorant nor turning positivity of groups into positivity of the whole sum.

No new positive coverage of W: rows1..17 for all k>=0 at u31.5 with W>norm²/40, the earlier regions and the atom211,1 are kept. No new arbitrary combinations nor extension of T. The global objective remains open.
