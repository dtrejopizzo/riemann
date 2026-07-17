## Overview <output>
<conclusion>
The hypothesis is REFUTED for this target: LMFDB does not host a downloadable list of 5000 zeros for L(Δ, s); its public interfaces supply only the first 10 zeros (at ~33 decimal digits), so the proposed "download from LMFDB" strategy cannot deliver N=5000 and the de novo PARI/GP route — empirically scaling as t∝T^3.0 with an extrapolated runtime of ~1.7 h — remains the only feasible path, albeit at the edge of practicality.
</conclusion> <methods>
1. Queried the LMFDB programmatically for the L-function with LMFDB label 1.12.a.a (L-function label 2-1-1.1-c11-0-0, Ramanujan Δ, weight 12, level 1): - HTML page scrape of `/L/ModularForm/GL2/Q/holomorphic/1/12/a/a/` to discover download links. - `/L/download_zeros/2-1-1.1-c11-0-0` text/JSON endpoint. - `/api/lfunc_lfunctions/?label=2-1-1.1-c11-0-0` REST endpoint. - `/L/data/2-1-1.1-c11-0-0` data dump. - Tried query parameters `limit`, `n`, `N`, `count` to request more zeros.
2. Installed `cypari2` 2.2.4 (PARI/GP 2.17.2) in the Jupyter environment, set `allocatemem=1 GB`, `realprecision=50` (`dps=50`).
3. Built the Ramanujan Δ L-function in PARI via `lfunmf(mfinit([1,12,1],1), mfbasis(mfinit([1,12,1],1))[1])` and called `lfunzeros(Lram, T)` for T ∈ {30, 50, 100, 200, 400, 800}.
4. Compared the first 10 PARI zeros with the LMFDB positive_zeros using `mpmath` at `mp.dps=50` to compute absolute differences and digit-agreement.
5. Fit a power law t = c·T^α to the (T, time) measurements at T ∈ {200, 400, 800} on log-log axes (`numpy.polyfit`) and extrapolated to the T≈4075 corresponding to N=5000 zeros (estimated from the empirical density 982 zeros/T=800 ≈ 1.23/unit T, consistent with the asymptotic count T·log T/(2π) for degree-2 L-functions).
6. Cached the 10 LMFDB zeros plus validation metadata to `cache/L_delta_zeros_lmfdb.json` and produced a summary two-panel figure `L_delta_zeros_validation.png`.
</methods> <results>
LMFDB availability:
- `/L/download_zeros/2-1-1.1-c11-0-0` returns 10 positive zeros at accuracy=100 bits (≈33 decimal digits). All `limit/n/N/count` query parameters were ignored — output remained 10 zeros.
- `lfunc_lfunctions` API row exposes a `positive_zeros` array of length 10. The data dump `/L/data/2-1-1.1-c11-0-0` likewise contains exactly 10 high-precision values. No 5000-zero file is offered by LMFDB for this L-function. Validation (PARI vs LMFDB at dps=50):
- γ₁(LMFDB) = 9.222379399921102522243767192743263
- γ₁(PARI) = 9.2223793999211025222437671927434781355287706224320
- |Δγ₁| = 2.15×10⁻³¹ → agreement to 30.67 decimal digits (≫ 10 required).
- All 10 zeros agree to 30–31 decimal digits (panel A). The R2 validation gate is therefore passed with ample margin. PARI scaling (dps=50, single core):
- T=200 → 159 zeros in 0.78 s; T=400 → 404 zeros in 5.08 s; T=800 → 982 zeros in 49.39 s.
- Log-log fit: t ∝ T^3.00 (close to but milder than r6's reported ~T⁴, still steeply super-linear).
- Extrapolation: T≈4075 to reach ~5000 zeros → ~6082 s (~1.7 h), exceeding the 3600 s task budget. Cached artifact: `cache/L_delta_zeros_lmfdb.json` containing 10 validated zeros at ~33 dp plus full provenance and a written record that the N=5000 target was not met by LMFDB.
</results> <challenges>
- LMFDB does not host bulk pre-computed zeros for higher-degree L-functions; the public schema stores only 10 zeros per L-function entry. This directly contradicts the premise of the research objective.
- No documented API parameter on `/L/download_zeros/...` extends the count. We verified this by trial; without an internal LMFDB DB dump (not publicly served), more zeros are unavailable.
- The de novo alternative (PARI `lfunzeros`) is computationally bounded: empirically t ∝ T^3.0 here (Δ has degree 2 and conductor 1, so it is among the easiest cases; r6's T⁴ likely reflects different parameters or accuracy targets). Even the cubic scaling makes N=5000 infeasible within the agent's 3600 s runtime budget.
- `cypari2` was not preinstalled; required `pip install cypari2` (cysignals+cypari2 wheels were available).
- `lfunmf` initially required the two-argument `(mfinit, mfbasis-vector)` form, not a single-argument call.
</challenges> <discussion>
The hypothesis that LMFDB offers a fast, ready-made route to 5000 high-precision zeros for L(Δ, s) is empirically false: LMFDB curates only the leading ~10 zeros per L-function in its public dataset. This is a general structural property of LMFDB rather than an L(Δ, s)-specific gap, and it means the protocol's recommendation to "use pre-computed external tables" (Rule R8) — which works well for ζ via Odlyzko's tables — does not straightforwardly transfer to general automorphic L-functions. For the -v6 pipeline this is a meaningful constraint: the Ramanujan-Δ "control family" cannot reach the same N as ζ on equal computational footing. PARI's lfunzeros is still the most reliable de novo source; here its scaling exponent measured at α≈3.0 is gentler than r6's α≈4, but the prefactor and absolute cost make N=5000 a multi-hour single-core job. Parallelism is possible (independent windows in T or coarse Hardy-Z sign-change scans refined by `lfunzeros` on smaller intervals), and is the natural follow-up. The validation step — first-zero agreement of 30.7 decimal digits between LMFDB and PARI at dps=50 — confirms both sources are mutually consistent and clear the R2 gate, so any blend of the two can be safely used.
</discussion> <proposed-next-hypotheses>
1. Splitting the lfunzeros computation into K independent height-interval batches (Hardy-Z sign-change localisation per interval, then `lfunzeros` refinement) and running them on K cores will reduce wall-clock time for N=5000 by approximately a factor of K, bringing the dps=50 acquisition under 30 min on an 8-core box without loss of precision.
2. Among the five control families, only the ζ family will achieve N=20 000 at dps=50 within practical compute budgets using purely "external table" strategies, because LMFDB caps non-ζ L-functions at ~10 stored zeros; the other four families will be effectively limited by their respective de novo scaling exponents (PARI lfunzeros: α≈3 for Δ, similar for χ-mods; Hardy-Z scan ~1.5 s/zero for L_DH).
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>cache/L_delta_zeros_lmfdb.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON cache of the 10 high-precision (~33 decimal digits, 100-bit accuracy) positive zeros of the Ramanujan Δ L-function (LMFDB label 1.12.a.a / 2-1-1.1-c11-0-0), pulled from the LMFDB API endpoint `/api/lfunc_lfunctions/?label=2-1-1.1-c11-0-0`. Includes full provenance, the R2 validation record (γ₁ agreement of 30.67 decimal digits with an independent PARI/GP lfunzeros computation at dps=50), and a written notice that LMFDB does NOT supply 5000 zeros — only 10 — for this L-function.</artifact-description>
</artifact>
<artifact>
<file-name>L_delta_zeros_validation.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: per-zero agreement digits −log₁₀|γ_n^LMFDB − γ_n^PARI| for n=1..10, all ≈30–31 decimal digits, well above the R2 threshold of 10. Panel B: log-log scaling of PARI `lfunzeros(L,T)` wall-clock time vs height T at dps=50 with a fitted power law t ∝ T^3.00 and the extrapolated cost (~1.7 h) to reach N≈5000 zeros at T≈4075.</artifact-description>
</artifact>
</artifacts>
</output>
