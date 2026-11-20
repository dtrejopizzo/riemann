# The two dominant frequencies of the majorant at the positive saddle

**Status: PROVED, with independent review of the normalization, the variance and the uniform exclusion of distant frequencies.**

Let β and H be the positive saddle and exponent of 395, Y=(4+κ/b)z at fixed κ. Denote by B the majorant obtained by integrating at β the modulus of the signed integrand, including 1/(2π). Then, unconditionally,

    log(B/A)=−(π² V/2+o(1))L/b³,
    V=4−2(log 4)²>0.

Set μ=2log 4−2, t₀=π/(b+μ). For each fixed ε>0, the part of B outside the two intervals |t∓t₀|<ε/b² is ≤B exp(−c_ε L/b³). This localizes the majorant; in the signed integral the two intervals are conjugate and there may still be oscillation inside them.

**Measure of the logarithms.** For a_p=p^(−β), M=Σa_p∼L/b by the saddle equation (log p=b+O(1); the squares cost O(1)). With weights a_p/M, the values v_p=log(p/z) converge in distribution on [0,log 4] to the density exp(v/2)/2 by the PNT and β→1/2. The integral of the density is one; its mean and variance are μ and V by integration. Bounded support gives convergence of both moments.

**Loss near an odd phase.** For |t|≤K/b with fixed K consider

    D(t)=Σ log((1+a_p)/|1−a_p exp(−it log p)|).

Uniformly D(t)=Σ a_p(1+cos(t log p))+O(Σa_p²), with Σa_p²=O(1), negligible relative to M/b². If tb=ℓπ+h/b for fixed odd ℓ and bounded h, Taylor gives

    b²D(t)/M = [(h+ℓπ μ)²+(ℓπ)² V]/2 + o(1).

If b dist(tb,π+2πℤ)→∞ with |tb|≤K, then b²D(t)/M→∞: the perturbations tv_p are O_K(1/b) and 1+cos is bounded below by a constant times the squared angular distance to the nearest odd multiple. By sequential compactness, the normalized minimum on this range is π²V/2+o(1) for K>π. Only ℓ=±1 and h→−ℓπμ attain it; outside the two stated bands there is a fixed margin (depending on ε).

**Excluding distant frequencies and integrating.** For K/b≤|t|≤2√L, the phase estimate in 396 gives D(t)≫(L/b)min(t²,1), with an absolute constant independent of K. Choose K fixed large enough to exceed the normalized minimum by a margin. Beyond 2√L the Gaussian tail suffices. These ceilings lose at most O(log L) in logarithm when integrating and normalizing by A∼exp(H(β))/√(2πH''(β)). For the floor of B use |t−t₀|≤b^(−3): in that whole band h=−πμ+o(1), the minimum is preserved up to o(1) and the logarithm of the width is negligible. This gives the equivalent and the exterior exponential saving. A terminal weight in [0,1] changes the logarithms of the products by O(1/L) on the vertical, so the claims persist.

**Review record.** For q=log4, the density exp(v/2)/2 on[0,q] integrates to1; its moments are2q−2 and2q²−8q+8. Subtracting the square of the mean gives exactly V=4−2q²>0, which is also positive by non-degeneracy of the density. The saddle equation gives M∼L/b, so M/b²∼L/b³ without an additional factor2. At tb=ℓπ+h/b, the angular deviation is(h+ℓπv_p)/b+O(b^(−2)), which fixes the constantπ²V/2 and the centers±π/(b+μ) to error o(b^(−2)). The uniform error O(Σa_p²)=O(1) is o(M/b²).

For K/b≤|t|≤1, the lemma of396 gives D(t)≥cK²L/b³; for1≤|t|≤2sqrt L it gives D(t)≥cL/b, with the same absolute constant. Thus K can be fixed large once to separate all those frequencies from the minimum; the phase Taylor expansion is not extrapolated to growing frequencies. On the remaining compact range, extracting subsequences distinguishes bounded h from b·dist(tb,π+2πℤ)→∞ and gives the uniform margin outside the bands of radiusε/b². The lower band of width b^(−3) and the prefactors only cost O(log L), less than L/b³; this allows converting the margins in the exponent into the relative concentration ofB. Weighting the last factor alters its log-modulus by O(1/L) uniformly in t, since its radius is O(1/L)<1, so it does not create an additional frequency of comparable magnitude either.

The constant is that of the majorant on this vertical. Obtaining the phase of the pulse requires studying the sum of the two complex integrals and comparing it with the exterior error before attributing a sign to it.
