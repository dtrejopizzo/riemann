# POWER_ARCH_TRIPLE_004 — Dimension-three bound and exact limit of the method

Status: PROVED density bound; NUMERICAL diagnosis of its insufficiency; OPEN archimedean positivity for all triples of rates >=31.5. No falsifier of that positivity is obtained.

Difference from the exterior/Pick record: an uncertainty inequality is tried for a FIXED dimension equal to three, exploiting real poles with lower-bounded rates. Extrapolating finite cases is not proposed. Antecedents consulted in POWER_BRIDGE_002 and POWER_POLYNOMIAL_003; no paper is touched.

For rates u_j>=a, let V=span{exp(-u_j y)1_(y>0)} of dimension n<=3. The rational orthonormal Malmquist basis gives exactly the evaluation kernel on the Fourier line:

    Σ_j |phi_j(tau)|²=Σ_j 2u_j/(u_j²+tau²).

The preceding Blaschke factors have modulus one, whence the result by summation. Cauchy–Schwarz applied to the normalised coefficients gives

    |hhat(tau)|²/(2pi ||h||²) <= Σ_j u_j/[pi(u_j²+tau²)].

For |tau|<=a, u/(u²+tau²) decreases in u>=a. Thus the density is <=n a/[pi(a²+tau²)] on that interval. The inequality persists by continuity in the confluent limits, interpreted as y^k exp(-uy).

The symbol m(tau) is even and strictly increasing in |tau|; this follows from the digamma series (each real term has positive derivative for tau>0). The principle of filling from lower frequencies therefore gives

    arch[h]/||h||² >= (2n/pi)∫_0^R m(tau) a/(a²+tau²) dtau,
    R=a tan(pi/(2n)),

if R<=a, as happens for n=3. It suffices to observe that the candidate density saturates its cap on [-R,R] and has total mass one; outside, all mass pays m>=m(R), and inside the cap is used. No additional exterior bound is needed.

For a=31.5, n=3, a diagnostic quadrature of this integral with scipy gives R=18.186533479473212 and bound -0.05064542812409753. It is not presented as an exact certificate: it serves to decide that this bound does not give the required positivity. Improving discretisation or arithmetic would not resolve that loss. It is tighter than replacing the density by the constant n/(pi a), but it still forgets the impossibility of simultaneously saturating evaluators on a whole interval.

A numerical test limited to rates log-separated by >=.04 found the minimum at the end of small separations, with no negativity (approximate value .1932). This does not prove monotonicity nor cover confluent rates. A run without minimal separation produced a spurious negative due to ill-conditioning of the Cauchy Gram matrix; it was discarded and is NOT used as a falsifier.

Precise residue: obtain a collective inequality improving the scalar cap by at least .051 on the worst triple, or prove that the lowest archimedean eigenenergy increases when separating rates from the confluent limit. Neither statement has been proved here. The fixed-ladder certificate of degrees up to five is another task and does not imply that monotonicity.
