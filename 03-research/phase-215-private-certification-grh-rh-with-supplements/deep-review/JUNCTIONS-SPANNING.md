# Individualised junctions of 51 and 52

The two appendices were read in full and their 51 reproduced statements were extracted (29 in 51, 22 in 52). They were collated with the source environments in 46, 49, 51, 52. 30 coincide after removing labels, references and spaces; the 21 remaining differences were inspected one by one. They are migrations of internal references to external citations, equation numbering or formatting. **No modification of a formula, hypothesis or range was found in the bodies of these 51 citations.**

Evidence: `evidence/compare_appendices_spanning.py`, `junctions_spanning_copies.json`, `junctions_spanning_diffs.txt` and `number_map_spanning.json`. The extractor serves only for collation: it does not prove the validity of the theorems nor the semantic correctness of an application. The check of the numerical locators is recorded separately from the equality of bodies.

## Hypotheses and main applications

- **46→51/52, data and sizes:** D1–D8 and S1–S7 remain complete. The two-sided window of logN is not replaced by a mere existence of N. S7 supplies n≥100, k≥512000n⁹, f≤b/1000, N≤b^(60n), separation Δ, norms of κ and the volume and dimension bounds used. Its independent construction is in ANALYTIC; its local consumption was traced in SPANNING.
- **49→51, real coefficient and formal degree:** it keeps h≥n²+1 and the measure compatible with volume 1 on the compact, without renormalising one per place after multiplying. The FJ proof requires the documented order repair; fidelity of the statement does not remove that defect of proof.
- **52→51, real system:** H0–H5 remain explicit; the mass is (1+b⁻¹⁰)/deg_τ, not an absolute constant. The two statements of the upper form (global Gram and at fixed head) are kept. SPANNING reconstructs the hypotheses in the instances used.
- **52→51, finite system:** T is finite, stable under conjugation and contains MN; for Siegel it moreover contains the places where B is not a unit. The same Z(A,d) is kept between the upper form and the Siegel step, and the mass (1+b⁻⁶)b^(−6k#A). The family of quadruples must be distinct and satisfy |τ(t_j)|>N. These conditions are not replaced by a simple count without multiplicities.
- **51→52, Bessel:** B1–B5′ include compact support modulo U, not only modulo R. The step uses that the real H is compact. The scalar c_W and the norm of the period have the same formal degree; B6 and B7 come from the construction before the local systems are invoked.
- **51→52, sieve and constants:** the inverse transformation is w↦w⁻¹ at the real places and w↦M⁻¹w⁻¹ at the finite place. The product ∏c_a and the error b^(2403n⁹f) are maintained. The L2 return receives the same three inputs R/F/S and the size inequalities; it does not already presuppose the final second moment.
- **51↔52, Siegel and fibres:** the source theorem requires explicit measures and normalisation and absolute convergence of the z integral. The wrong direction of the cutoff in an auxiliary proof still requires the repair indicated in CORRECTIONS-INVENTORY. The citations do not change that statement nor by themselves repair its proof.

The imports that reproduce Spanning, moment, spreading or local systems in the paper that develops their inputs are return/context statements: they are not automatically taken as independent premises. The actual sequence audited is data and Bessel → systems/fibres → sieve and L2 → moment → spreading; the mutual citations do not by themselves prove a cycle.

## Inventory of fidelity of the statements

In the last column **(a) copy** means agreement of the body and hypotheses with the source inspected; the validity of the application is assessed in the preceding notes and in SPANNING/MULTIPLICITIES. It is not equivalent to approving each line of the source proof. The numerical locators are not taken as good merely because they were deleted on normalising.

| Destination and line | Source | Label / line | Collation |
|---|---|---|---|
| 51:10753 | 46 13.3 | `an:def-data` / 2954 | (a) copy; equal after normalisation |
| 51:10787 | 46 13.4 | `an:lem-sizes` / 2989 | (a) copy; differences of references/formatting inspected |
| 51:10825 | 46 14.5 | `au:free` / 3598 | (a) copy; equal after normalisation |
| 51:10830 | 46 14.14 | `thm:srcB` / 4012 | (a) copy; equal after normalisation |
| 51:10838 | 46 14.29 | `au:ramcount` / 4619 | (a) copy; equal after normalisation |
| 51:10842 | 46 14.30 | `au:onetranslate` / 4637 | (a) copy; equal after normalisation |
| 51:10854 | 46 14.31 | `au:few` / 4666 | (a) copy; equal after normalisation |
| 51:10868 | 46 14.32 | `au:moment` / 4692 | (a) copy; equal after normalisation |
| 51:10882 | 46 14.34 | `au:spread` / 4778 | (a) copy; equal after normalisation |
| 51:10887 | 46 14.36 | `au:mult` / 4812 | (a) copy; differences of references/formatting inspected |
| 51:10899 | 49 2.19 | `pwf:haar` / 1137 | (a) copy; differences of references/formatting inspected |
| 51:10908 | 49 3.17 | `pco:FJ` / 1876 | (a) copy; differences of references/formatting inspected |
| 51:10912 | 49 3.18 | `pco:minors` / 1898 | (a) copy; equal after normalisation |
| 51:10927 | 49 3.19 | `pco:equiv` / 1938 | (a) copy; equal after normalisation |
| 51:10941 | 49 3.21 | `pco:indep` / 2029 | (a) copy; equal after normalisation |
| 51:10947 | 49 3.23 | `pco:K` / 2097 | (a) copy; differences of references/formatting inspected |
| 51:10959 | 49 3.25 | `pco:decay` / 2148 | (a) copy; equal after normalisation |
| 51:10964 | 49 8.1 | `pz:def-type` / 7759 | (a) copy; equal after normalisation |
| 51:10978 | 49 8.4 | `pz:types` / 8021 | (a) copy; differences of references/formatting inspected |
| 51:11000 | 52 2.17 | `pfr:R` / 926 | (a) copy; differences of references/formatting inspected |
| 51:11017 | 52 2.19 | `pfr:haar` / 1001 | (a) copy; equal after normalisation |
| 51:11024 | 52 2.41 | `pfr:rearr` / 1472 | (a) copy; equal after normalisation |
| 51:11028 | 52 4.1 | `prp:heis` / 2665 | (a) copy; equal after normalisation |
| 51:11036 | 52 5.12 | `pff:massK` / 3725 | (a) copy; equal after normalisation |
| 51:11041 | 52 5.13 | `pff:L1` / 3741 | (a) copy; equal after normalisation |
| 51:11046 | 52 5.24 | `pff:fixed` / 4104 | (a) copy; equal after normalisation |
| 51:11058 | 52 5.28 | `pff:F` / 4192 | (a) copy; differences of references/formatting inspected |
| 51:11073 | 52 5.29 | `pff:S` / 4223 | (a) copy; differences of references/formatting inspected |
| 51:11090 | 52 6.35 | `pfg:siegel` / 5462 | (a) copy; differences of references/formatting inspected |
| 52:5524 | 46 13.4 | `an:lem-sizes` / 2989 | (a) copy; differences of references/formatting inspected |
| 52:5562 | 46 14.5 | `au:free` / 3598 | (a) copy; equal after normalisation |
| 52:5567 | 51 2.1 | `pb:KR` / 554 | (a) copy; equal after normalisation |
| 52:5573 | 51 2.16 | `pb:bessel` / 1152 | (a) copy; differences of references/formatting inspected |
| 52:5610 | 51 2.21 | `pb:massratio` / 1336 | (a) copy; equal after normalisation |
| 52:5621 | 51 3.6 | `pbv:haar` / 1777 | (a) copy; differences of references/formatting inspected |
| 52:5627 | 51 3.16 | `pbe:ds` / 2331 | (a) copy; equal after normalisation |
| 52:5647 | 51 3.18 | `pbe:local` / 2376 | (a) copy; differences of references/formatting inspected |
| 52:5678 | 51 3.22 | `pbe:bessel` / 2622 | (a) copy; differences of references/formatting inspected |
| 52:5700 | 51 3.33 | `pbm:pos` / 3168 | (a) copy; differences of references/formatting inspected |
| 52:5712 | 51 3.39 | `pbm:E4` / 3396 | (a) copy; differences of references/formatting inspected |
| 52:5718 | 51 3.41 | `pbm:cell` / 3450 | (a) copy; equal after normalisation |
| 52:5730 | 51 3.42 | `pbm:orbit` / 3525 | (a) copy; equal after normalisation |
| 52:5740 | 51 3.44 | `pbm:system` / 3617 | (a) copy; equal after normalisation |
| 52:5759 | 51 3.50 | `pbm:sieve` / 3813 | (a) copy; differences of references/formatting inspected |
| 52:5773 | 51 3.51 | `pbm:inputs` / 3890 | (a) copy; differences of references/formatting inspected |
| 52:5806 | 51 3.52 | `pbm:const` / 3928 | (a) copy; equal after normalisation |
| 52:5818 | 51 3.53 | `pbm:L2` / 3994 | (a) copy; differences of references/formatting inspected |
| 52:5828 | 51 7.2 | `pbp:main` / 6801 | (a) copy; equal after normalisation |
| 52:5837 | 51 7.12 | `pbp:tb-witt` / 7062 | (a) copy; equal after normalisation |
| 52:5846 | 51 8.80 | `pbo:GF` / 10235 | (a) copy; equal after normalisation |
| 52:5854 | 51 8.81 | `pbo:append` / 10280 | (a) copy; differences of references/formatting inspected |

## Check of references and macros completed

The theta review reused its verifier on these 51 rows: all the numerical references were resolved against the LaTeX auxiliary files of the sources, with no discrepancies. The comparison of macros, including their transitive closure, found no differences either. Evidence: `collation_51_spanning_refs.json`, `collation_51_spanning_macros.json` and `check_spanning_aux_macros.py`. This completes the semantic fidelity of the reproductions, without making correct the defective lines of the source proofs.
