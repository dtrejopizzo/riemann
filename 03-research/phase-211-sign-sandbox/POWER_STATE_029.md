# State029 — Uniform regions at all orders and limit of the positive bridge

Status: three results PROVED and audited. Replaces STATE028. Global sign OPEN; goal active; papers untouched.

## Real positivity of W in infinite regions

POWER_ROW_PATTERN_029 proves for ALL N>=2,k>=1,u²>=256N:

    W[f_(N,k,u)] > (7/10)||f_(N,k,u)||².

POWER_BOUNDARY_WEDGE_029 proves for ALL N>=1,k>=0,u²>=4096N:

    W[f_(N,k,u)] > (2/5)||f_(N,k,u)||².

Both keep the WHOLE arithmetic comb and the polar term. They are uniform theorems, without certifying individual dimensions. The second includes k0, where the inverse spectral moment used by the first diverges.

## Shared elementary mechanism

Cauchy–Schwarz with the two opposite weights keeps the product of their norms. Comparing coefficients of the WRN series with those of (1−rho)^−(2N−1) gives

    |c_f(t)|/norm² <= exp(−eta|t|)
       [(u²−eta²)/(u²−4eta²)]^(N−1/2), u>2eta.

The linear cost Neta/u of the one-sided estimate cancels. The remaining cost depends on Neta²/u². It does not contradict the obstruction016 to making the weights uniform with u fixed and N/u² growing.

For k>=1, a lower bound of digamma by Euler summation and the beta moments give ARCH>.9; the comb loses less than.16 and the adverse polar less than.001. For k0, the singular inverse moment is replaced by a maximal spectral density bound and the resolvent1/(tau²+.25): ARCH>.45 in the stronger region; comb<.0002 and adverse polar<.001. Monotonicity of ARCH in k extends that second proof to all k.

## What it does not contribute to the fixed-rate bridge

POWER_SCALE_BRIDGE_LIMIT_029 proves that the normalised densities of the domain u>=C sqrtN have height<=1/(C sqrtpi), even after mixing them with positive weights. On an interval of length C/4 their mass is<1/4. There are atoms of fixed rate u0=31.5 and large order with mass>3/4 on that interval; their L1 distance to that whole cone is>1/2.

Hence the cone of ALL atoms of the bridge017 cannot automatically be replaced by this region of increasing rates. It is a specific obstruction to positive approximation of densities, not a counterexample to W nor a no-go for any other bridge.

## Evidence and region still pending

POWER_SCALE_AUDIT_029 approves the three proofs; the texts were read and both exact verifiers reproduced: PASS. Uniformity belongs to the analytic proofs; the scripts only certify constants. The bridge limit uses an integral inequality, not a numerical proof.

At u31.5, region C16 reaches only N<=3 and C64 adds no orders. The coverage of the sufficient table at that rate remains: rows N1..5 for all k and cone k>=10000N². The eight arbitrary poles and fixed block12 also remain. N>=6,k<10000N² remains; no new window T nor the global sign has been certified.

The continuation must recover information at large N/u² and keep the arithmetic cancellations. Reducing constants of these regions may enlarge parameters, but does not by itself remove that obligation.
