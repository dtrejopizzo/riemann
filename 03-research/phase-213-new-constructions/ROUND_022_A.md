# Variance of the arithmetic crossing that the global sign would tolerate

Prior independent cross-check with 213-019/020/021, P46 (band, oneprofile, AM), L2_BUILD_019, R186_005 and P2_SCHUR_001. Selecting a test vector by projection is classical. The specific application measures simultaneously the residues of all cells after removing two moments. The cross-check did not locate this condition in those antecedents.

Fix C>1. For large integer K use the full cells with indices J=[K,floor(CK))∩ℤ. We use exactly M, A, h and q of BUILD084 (3)-(4). Let p=(log(3/2),−log 2) on cells 1,2 and d=log(4/3). For j∈J write

    s_j = Σ_{i=1,2} p_i Σ_{ni≤j<n(i+1), n≥2} Λ(n)/n,
    r_j = Σ_{i=1,2} p_i A_ij,     l_j=log(1+1/j).

Let H be the matrix with rows 1 and K l. Define b=Hᵀ(HHᵀ)⁻¹(d,0)ᵀ, v=s−Hᵀ(HHᵀ)⁻¹Hs, D=max(1,max_{i∈J} Σ_{j∈J}|M_ij|). With at least two cells H has rank two. The tail x=b+v/D makes p+x primitive, since Σp_i=−d, the inverse moment of p is zero and Hv=0. The vectors b and v are orthogonal and ⟨s,v⟩=||v||². The exact matrix formula of BUILD084 and the row-sum bound for the symmetric matrix give

    a(U(p+x)) ≤ q(0)+D||b||²−2⟨s,b⟩+2⟨r,x⟩−||v||²/D.       (1)

Hence a strictly negative right-hand side for any K with J separated from the head (K≥4) and at least two cells provides a full counterexample. The proof uses only an upper bound on the tail energy.

For fixed C, HHᵀ/K converges by Riemann sums to the Gram of 1,1/u on [1,C], positive definite. Thus ||b||₂=O_C(K⁻¹ᐟ²) and ||b||₁=O_C(1). By PNT and partial summation the two inner sums in s_j tend respectively to log 2 and log(3/2), uniformly for j≥K; hence ||s||∞=o(1) and ||v||₂=o_C(√K). Moreover ||r||₂=O_C(K⁻¹ᐟ²) by (3) of BUILD084. In the tail matrix the diagonal costs O_C(log K), the off-diagonal archimedean sum costs O_C(log K) by h(0)=2log2 and h(m)≤1/m for m≥1. For each n with contact in J one has n≤C. In a row there are at most n upper columns and one lower for that n, so the whole sum of arithmetic weights is O_C(1). Hence D=O_C(log K).

Consequently (1) has the form q(0)−||v||²/D+o_C(1). If the global sign holds, necessarily

    limsup_{K→∞} ||v||²/D ≤ q(0),    ||v||²=O_C(log K).

The first bound is an asymptotic threshold with computable normalization. The finite decision uses (1) with all its terms. Satisfying the condition leaves open the energy of other tails, even within the same band. No violation has been verified for the von Mangoldt weights. PROVED for the necessary condition and the finite criterion after independent mathematical audit.

## Finite evaluation of the criterion

With C=2 the internal comb is exactly zero, since j<2K≤2i throughout the band. W(m)=Σ_{n≤m}Λ(n)/n was accumulated by a prime-power sieve and s_j=log(3/2)[W(j)−W(⌊j/2⌋)]−log(2)[W(⌊j/2⌋)−W(⌊j/3⌋)] was used. The projection by QR, D by absolute row sums and the energy by the exact matrix of BUILD084 were computed. Results in double precision, rounded; they are not interval certificates.

| K | D | Projected loss | Bound (1) | Test energy |
|---:|---:|---:|---:|---:|
| 16 | 5.030073 | 0.015720 | 0.822007 | 0.183973 |
| 64 | 7.819384 | 0.014822 | 0.407719 | 0.149002 |
| 256 | 10.595623 | 0.010248 | 0.239676 | 0.146535 |
| 1024 | 13.369113 | 0.007644 | 0.185880 | 0.152829 |

The head energy is approximately 0.167101. In the last three bands the tail reduces that energy; the four tests stay above zero. The table concerns a single tail selected per band.

### Minimum with the head p fixed

Prior cross-check. BUILD084 (16)–(18), 212-59/75, 212 ROUND_001_B, P46 prop:schur and the Schur entry in P48 already contain the elimination. It is used only to decide whether the choice of tail hid a negative energy in the four examples.

For Z with orthonormal columns spanning ker H, write x=b+Zu, B=ZᵀAZ and g=Zᵀ(Ab+r−s), where A is the tail block. If B is positive definite the minimum is attained at u=−B⁻¹g. Z was built by SVD, the smallest eigenvalue of B was checked and the system was solved by Cholesky. The largest Euclidean stationarity residue was 2.1×10⁻¹⁵. Diagnosis in double precision.

| K | Smallest eigenvalue of B | Minimal energy with fixed head |
|---:|---:|---:|
| 16 | 0.606024 | 0.156323 |
| 64 | 0.553454 | 0.116346 |
| 256 | 0.547662 | 0.107085 |
| 1024 | 0.547097 | 0.101826 |

It includes all cellwise constant tails in each band with both moments imposed and that head. The table does not control several bands simultaneously nor establish a bound uniform in K. The sweep is closed here.
