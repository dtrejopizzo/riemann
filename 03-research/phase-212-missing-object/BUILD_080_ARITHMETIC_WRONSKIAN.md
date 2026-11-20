# Construction 080 — Arithmetic corrector annihilating an explicit profile

Status: design and residue written, pending review; sign OPEN.

## Motivation and data

BUILD079 extracts too much even in its first channel. Removing by orthogonal projection the profile g=Q(1_I M), with M=−Φ″+Φ/4 explicit, numerically reduces ||WF||² on the saved test T=0.8 from 0.00829844628 to 0.000190522237; it still exceeds its form value 5.2943e−12. The computation is in build_079_data/check_extraction.py, orders 64/96 agreeing. It is not a certificate.

The normalization, irrelevant for that projection, is

    Φ(t)=Σ_{n≥1} e^(t/2)(4x_n²−6x_n)e^(−x_n), x_n=πn²e^(2t),
    M(t)=Σ_{n≥1} e^(t/2)(−16x_n⁴+112x_n³−164x_n²+36x_n)e^(−x_n).

It can be evaluated with t replaced by |t| by the parity of the profile. The diagnostic implementation truncates at n=12; it does not use the eigenvectors to define g. Q and K=R−I are exactly the operators of BUILD079.

## New operation within this design

Instead of removing a single component by inner product, cancellation is forced at each contact:

    D_g F = g·(KF)−(Kg)·F
          =Σ_n μ(n)/sqrt(n)[g(t)U_log n F(t)−U_log n g(t)F(t)].

This formula does not divide by g and is defined also at its zeros. In particular D_g g=0 exactly. No sign is attributed to g(t)g(t−log n): no ground-state transformation with positive rates is applied.

With S=Σ|μ(n)|/sqrt(n),

    ||D_g||≤2S||g||∞,
    α_g=1/[2(1+2S||g||∞)],
    W_g=α_g Q D_g Q,
    V_g F=J W_g F.

By construction ||W_g||<1/2 and W_g g=0, because Qg=g. The corrector uses arithmetic and the archimedean profile in each summand, with two constraints implemented by Q. These are facts of construction, not a sign proof.

## Complete square and residue

Put Z_n^g F=Q[g·U_log n F−(U_log n g)·F], for F∈P_T. Then

    ||V_g F||²=α_g² Σ_{m,n≥2} μ(m)μ(n)/sqrt(mn)
                           b(Z_m^g F,Z_n^g F),

    ρ_g(F)=Arch(F)−2Σ_n Λ(n)/sqrt(n) Re<F,U_log n F>
           −α_g²Σ_{m,n} μ(m)μ(n)/sqrt(mn)b(Z_m^g F,Z_n^g F).

Thus a_T(F)=||V_gF||²+ρ_g(F), with no omitted terms. For smooth F in the core, g and the resulting functions are compactly supported BV, so they belong to the domain of J. The identity is proposed first on that core; any extension requires continuity in the form norm.

The annihilation is preserved in the channel J W_g g. The order of J and W_g is not reversed here: W_gD_u g need not be zero. This is a concrete reason to abandon variant V3 of BUILD079.

## What is missing

Annihilating g does not automatically annihilate the derivatives of the profile nor the corrected vectors of the whole ladder. Nor does it sign ρ_g. The design must be submitted to the saved test and to the controls cΛ, deletion and Beurling. The algebraic annihilation D_g g=0 holds for any K; therefore it is not presented by itself as the step that separates falsifiers.

## Review and additional diagnosis

The formulas for D_g, its norm, the exact annihilation and the residue were checked independently on the declared core. The annihilation avoids the local-response failure of BUILD079 on the limit profile. It does not annihilate the whole ladder.

Correction of the scope of the commutator: now [D_u,M_g]=M_(g−g(·−u))τ_u introduces interior terms. The commutator is not localized exclusively at the endpoints and in Q, as happened in BUILD079.

NUMERICAL: with the same saved test T=0.8, the script computes ||W_gF||²=6.2306829896562e−5 at orders 64 and 96. The supremum of g was estimated on a mesh of 200001 points (16.9460810), giving α_g≈0.0112276223. Neither that supremum nor the saved value of a_T is certified. The first channel still exceeds the saved value 5.2943e−12 by roughly 1.18e7. It is evidence against domination on that test, even though D_g g=0 exactly.

## Correction of the choice of profile

To treat a complete explicit primitive test, instead of its hard projection, one can choose directly

    g_T=Mχ_T−a_T^corr u_T,
    a_T^corr=∫Mχ_T cosh(t/2)dt,
    ∫u_T cosh(t/2)dt=1,

with χ_T even smooth, compactly supported inside I, and u_T even smooth compactly supported in the interior. Both moments of g_T are then exactly zero. χ_T and u_T are chosen by bump formulas, independent of the target form. The same construction D_g annihilates this complete test, including its moment correction; not only Mχ_T.

If g=Q(Mχ_T) is kept, the exact relation with X_T=Mχ_T−a_T^corr u_T is W_gX_T=−a_T^corr W_gQu_T. That formula cannot be used without correcting the boundary term when χ_T differs from the cutoff of g.

The direct choice g_T=X_T exactly eliminates the first analytic test, but it does not change the obligation to control all other F. It is not presented as a solution of the previous numerical diagnosis, which used the hard profile Q(1_I M). The next proposed extension is a two-profile cancellation by cofactors, with separate review before attributing a larger scope to it.
