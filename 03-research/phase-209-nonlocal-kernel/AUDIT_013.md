# AUDIT_013 — Universal scales of the Mellin–Gauss map011

2026-10-19. Independent check. Read LINK_013_NO_FIXED_SCALE and cross-checked P47 lem:testfam, thm:margin WITH ITS PROOF and cor:margin1.
**Verdict: PROVED the exclusion of every universal scale c>0 for U011, with the CITED input of the paper's bound on that explicit family. No exclusion of c(T), other maps or D.**

## 1. Corpus and change of class

Consulted: index/grid/crossword, margin families and entries011–012. The new reason is valid: 012 treated one scale in one window; 013 evaluates the SAME map on the concrete tests responsible for the margin as T→∞. There is no attempt to repeat the discarded equality nor is a small infimum turned into information about an arbitrary vector. The computation of M(F_T) is indispensable and has been carried out.

The CITED bound of P47 uses its certified data Z1/Z2 and the explicit formula. Here it only falsifies a domination of the auxiliary; it is not a source of positive sign for D nor is any external equivalence introduced.

## 2. Profile h and improper Riemann sums

The identity h=2y^(1/4)[z_cm(y)−Σ(d^(−1/2)−d^(−1))m(d²y)] is exact: the contribution of c cancels via Σv(d)/d=z_c. The series converge by the bounds already proved, without separating a divergent polar vector.

With N=y^(−1/2) and g(r)=r^(−1/2)m(r²), one checks exactly

    N^(−1/2)Σd^(−1/2)m((d/N)²)=(1/N)Σg(d/N).

The domination g≤min(r^(−1/2),r^(−3/2)) controls the sums near zero and at infinity by 2√ε+o(1) and 2/√R+o(1). On an interval [ε,R] the usual sum converges by continuity. An ordinary Riemann sum is not incorrectly invoked at a singular endpoint.

The integral of g is κ/2 via y=r², with correct factor 1/2. The term d^(−1) is O(1+logN) before the factor N^(−1/2); its tail is bounded via m((d/N)²)≤N/d. The term z_cm also vanishes. Thus h(−∞)=−κ. The original representation with τ proves h(+∞)=0 by Gaussian decay; local uniform convergence gives continuity. Together with the limits, h is bounded and h_ev→−κ/2 at both ends.

## 3. Spline, derivatives and escaping mass

For each fixed j, the Plancherel formula has prefactor k^(2j+1). On |v|≤1, |sincv|≤exp(−v²/7) yields an integral O(k^(−j−1/2)), so the product is O(k^(j+1/2)). The intervals [1,2] and [2,∞) give exponentially small contributions for large k using sin1<1 and v^(−2k). With exponent k and no weight one obtains ||ω_k||∞=O(√k). The arguments and orders are correct.

For k~T,

    ||G_T^(j)||₂=O(T^(3/4−j/2)).

Cauchy–Schwarz on a support of length 2T gives the two L¹ orders T^(1/4) and T^(−3/4), and ||F_T||²=O(T^(3/2)). No profile h is differentiated whose derivative integrability has not been proved.

G_T/T is a probability and its mass on |x|≤R is O_R(T^(−1/2)). Although G_T concentrates in x/T near zero, in the physical coordinate x its width grows: the mass escapes from every fixed compact set. With h bounded and h_ev→−κ/2 this proves ∫G_Th/T→−κ/2. A pointwise limit of G_T is not needed.

## 4. Response of the map and domain

P(D) coincides term by term with the polynomial of P47. The term −γ₁²G_T/4 gives the positive main part of M; the two derivatives contribute o(T). Thus

    M(F_T)/T→γ₁²κ/8,
    liminf ||U_TF_T||²/T²≥γ₁⁴κ³/64>0.

The sign and all powers of κ are correct.

To invoke the properties of the test it suffices to fix T≥1: k=ceil(21T/e)≥8, G has enough derivatives and F lies in H¹ with the required support and moments. It was flagged that this threshold should be made explicit in §3, since for very small T, k<5 and the lemma would not apply. This does not limit the asymptotic theorem: T_c can be raised to 1.

Parity and cancellation of both exponential moments come from the polynomial P(±1/2)=0 and from the vanishing derivatives at the boundary. Hence Q_T=a_T on these tests with no omitted polar term.

## 5. Bound for the ACTUAL family of P47

Step 6 of the proof of thm:margin bounds the ABSOLUTE SUM of zero contributions for the F of lem:testfam. Hence it also bounds |a_T(F)|, not only an infimum. Step 7 divides by the lower bound of ||F||². Cor:margin1 optimises precisely k=ceil(21T/e). Therefore it is valid to carry over from that proof, as CITED input,

    |Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T).

This claim is not obtained merely from the statement λ_A≤…; checking the proof avoids that invalid inference. The external certificates Z1/Z2 of the paper are not re-audited here.

With ||F_T||²=O(T^(3/2)) and the response of U≥const·T² one obtains

    |Q_T(F_T)|/||U_TF_T||²
      =O(T^(1/2)exp(−15.449T))→0.

It is valid to use the absolute value thanks to step 6; Q_T≥0 is not presupposed.

## 6. Quantifiers and core

The convergence of M/T and all the bounds hold for ALL sufficiently large T, not just a sequence, because k~T and the estimates are uniform for large k. Hence every fixed c>0 fails in all windows T≥T_c on the given family.

For each T with strict violation, approximating F_T in H¹ by even C_c∞ functions and correcting its cosh moment keeps the inequality by continuity of Q_T in H¹ and of U_T in L². A simultaneous uniform approximation over all windows is not needed.

A hypothetical domination with c(T)>0 would force c(T)≤O(T^(1/2)exp(−15.449T)) on these tests. That necessary condition proves neither existence nor impossibility of such scales. Nor does it rule out different maps or a link that genuinely changes class.

**Final result:** every positive universal scale of U011 ruled out, with a clearly delimited CITED source. −R and its identities remain valid. Full D remains OPEN and active; this result only closes that family of dominations of the concrete map.
