# POWER_REFLECTION_TEST_044 — Reflection of densities does not preserve the real form

Status: **PROVED**, independent review approved in [POWER_REDUCTION_AUDIT_044.md](POWER_REDUCTION_AUDIT_044.md); exact verifier PASS. Fixed rate u=63/2. Papers untouched. Neither the sign of W nor every possible reduction to subfamilies is refuted.

## 1. Corpus and falsifiable proposal

Consulted ROUTES-TRIED-INDEX/README, master grid, CROSSWORD-TO-D and SCALAR_BRIDGE017; reread the limits DESCENT016, TABLE_AUDIT018, ROW_PATTERN029 and MOVING_BALANCE036. These antecedents prevent inferring density or sign from a union of positive families. Here there is no return to a mixture of large rates nor to an assumed positive recurrence.

The concrete proposal to prove/refute is to eliminate, by a REAL symmetry, the antisymmetric sectors of the rational densities, reducing the scalar target to a balanced diagonal. A STRICT inequality of the full form, with ALL contacts, is proved that refutes that symmetry. The difference concerns the given real functional, not only a density obstruction nor a generic model. The archimedean entry is reused from004; the full recurrence and the normalized archimedean monotonicity are already recorded in018. Those computations are not presented as a new technique. The new check is their exact application to the reflection hypothesis of the bridge017; it does not enlarge the known sign regions.

## 2. Why reflection appears

Use q=tau²/(u²+tau²), t=q(1−q). Every polynomial R(q) has a unique representation

    R(q)=A(t)+(2q−1)B(t).

Proof: decompose R into symmetric and antisymmetric parts for q↔1−q. The symmetric one is a polynomial in t, because q satisfies q²−q+t=0. The antisymmetric one is divisible by2q−1 and its quotient is symmetric.

The balanced atoms k=N−1 of017 have, relative to the common density |F1|², profiles t^(N−1). Two adjacent diagonals allow reconstructing the antisymmetric sector with SIGNED coefficients. This linear reconstruction does not preserve positivity. To DISCARD that sector via reflection the form would have to annihilate |F1|²(2q−1)B(t). Already B=1 fails for the real datum.

It is not claimed that every reduction to a strip must use this symmetry nor that the signed representation above is a positivity bridge.

## 3. Full inequality falsifying the symmetry

Take two real causal functions of L² norm one:

    g_Q(y)=sqrt(4u)(1−uy)e^(−uy),
    g_L(y)=sqrt(4u)uy e^(−uy), y>=0.

Their transforms are sqrt(4u)QF1 and sqrt(4u)LF1, with Q=s/(s+u), L=u/(s+u), F1=1/(s+u). The densities are interchanged by q↔1−q. We prove

    W[g_Q]−W[g_L]>3/2.                              (ASYMMETRY)

### Archimedean

The orthonormal Laguerre basis of CONFLUENT004 is

    phi0=sqrt(2u)e^(−uy),
    phi1=sqrt(2u)(1−2uy)e^(−uy).

Here g_Q=(phi0+phi1)/sqrt2, g_L=(phi0−phi1)/sqrt2. The mixed archimedean entry, already computed exactly there, is

    b=(u/2)psi'((u+1/2)/2)=(63/4)sum_(r>=16)r^(−2).

Integral comparison of the tail gives

    b>(63/4)[sum_(r=16)^31 r^(−2)+1/32]>1,

the last inequality purely rational. Hence the archimedean gap is2b>2.

### Exact polar

Evaluating the two transforms at s=±1/2 gives

    Polar[g_Q]−Polar[g_L]
      =−2u(1+4u²)/(u²−1/4)²>−1/2.

The polar contribution is not omitted nor is its sign inferred from the densities on the half-axis: the rational identity is evaluated exactly off it.

### Full comb, with favourable sign

Elementary integration of the normalized autocorrelations produces for all a>=0

    c_Q(a)=e^(−ua)(1−ua),
    c_L(a)=e^(−ua)(1+ua).

Thus, with the convention Comb[g]=−2sum_(n>=2)Lambda(n)n^(−1/2)c_g(logn),

    Comb[g_Q]−Comb[g_L]
      =4u sum_(n>=2)Lambda(n)log(n)n^(−u−1/2)>0.

The series is absolutely convergent and ALL its terms are nonnegative, with that of n2 strictly positive. No truncation nor numerical bound of the comb is used. Adding the three parts yields ASYMMETRY.

## 4. Scope

The antisymmetric sector of the densities is not invisible to the full form. In particular, the signed decomposition of §2 does not allow closing via only the balanced diagonal by eliminating the remaining sector through reflection. The obstacle comes from an inequality of the REAL datum and keeps its arithmetic, not from an auxiliary counterexample.

ASYMMETRY compares two positive W values already included in proved regions; it does not prove a negative W value nor exclude another unequal relation between strips. By itself it provides no new sufficient subfamily. A valid reduction would have to control the antisymmetric sector quantitatively, not cancel it by a nonexistent symmetry. There is no parameter campaign.
