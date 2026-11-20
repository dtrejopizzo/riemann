# Counter-test for decorrelation based only on the carriers

There exists a fixed sequence f with values 0,±1 that coincides with μ on all numbers with up to three distinct prime factors, has exactly the same squarefree support and can coincide on any prescribed initial table. It preserves the cell distribution bounds used in 350 and all the sign reserves of 351. However, for each δ=1/j, j≥16, sufficiently large dyadic X and H=X^(1−δ), its two residues on p,2p and 3p,6p satisfy

    ∫_[X,2X] R_1(x)R_3(x) dx/x ≫ H² exp(−2√log X).

Thus the separation of the carriers and their exact signs allow a correlation of order H^(2−o(1)). The test sequence is not multiplicative.

**Sparse perturbation.** Fix Q=3·5·7·11. In each [N,2N), N a power of two above the initial table, there are ≫N squarefree multiples of Q, by the count of coprime squarefree integers applied to n/Q. Among them one of the signs of μ occupies ≫N points. Successively choose the smallest available point of that sign and leave a gap of at least D_N=⌈exp(√log N)⌉. One obtains K≫N/D_N points and at most O(1+N/D_N). In that block compare two choices: keep μ or invert it at the K points. The sums differ in modulus by 2K; choose the option with larger sum in absolute value, fixing the tie-break. In this way |Σ_[N,2N) f|≥K without presupposing anything about the real size of the Möbius sum on that block. The decisions define a single f, independent of the windows. All the carriers of 351 have at most three distinct primes, so none has been modified. Multiplicativity together with the prime signs and the squarefree support would fix all coefficients, so that hypothesis cannot be attributed to the modified model; if some choice left f=μ on all blocks, the lower bounds themselves would already apply to μ. To guarantee a discrepancy by construction without resorting to that dichotomy, on a single finite block after the initial table compulsorily invert one squarefree multiple of Q. This does not affect any asymptotic statement.

**What the cells preserve.** In any subinterval of length L inside [X/2,3X] there are O(1+L exp(−c√log X)) coefficients different from μ, since only a bounded number of dyadic blocks are crossed. The change in all partial sums within a cell of 350 is therefore O_A(J/log^A X) for each fixed A. The construction of 351 applies with the same two types of carriers, the same signs and the same uniform bound |R_i−S_f|≪1+J²/H=o(√H). The subcollections actually chosen may differ from those corresponding to μ.

**Correlation.** For X=N, integrate the full pulse of f in dx/x. Each interior n whose translate fits entirely contributes h∫η times f(n); only O(H+1) integers at the edges have incomplete weight or come from outside. Thus

    ∫ S_f dx/x = h(∫η) Σ_[X,2X) f + O_η(h(H+1)).

Since H=o(X/D_X) for fixed δ, its modulus is ≫H/D_X. Cauchy–Schwarz gives ∫ S_f² dx/x ≫H²/D_X². The L² norm of each R_i−S_f is o(√H), negligible relative to H/D_X. Expanding the cross product gives the announced bound.

**Comparison and decision.** In 330 multiplicativity and signs were preserved but prime magnitudes were changed. Here magnitudes, support and exact values on both prime families are preserved, at the cost of modifying the multiplicative law. An estimate of 351 founded exclusively on the availability of primes, disjointness and the distribution bounds used to select the residues would be false. The point requiring additional information is the selection decisions coming from the exact μ.
