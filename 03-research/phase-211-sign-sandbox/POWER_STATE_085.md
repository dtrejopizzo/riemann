# POWER_STATE_085 — Four arbitrary admissible powers

Status: **PROVED**, run 61911 exit0/FULL PASS 16384 panels for NR and NS; mathematical and code audit approved. Independent reproduction 29132 exit0/FULL PASS of both numerators on the 16384 panels, with matching hash. Paper 46 global **OPEN**; papers untouched.

## Complete result

For any real exponents ai>1, W is positive on the span of up to FOUR corresponding powers, except for the zero function. For distinct nodes the full kernel Kij=[L(ai)+L(aj)]/(ai+aj−1) is PD. If there are repeated exponents, coefficients are grouped and the redundant matrix is PSD. ARCH, polar and ALL contacts are kept via CONE001.

Chain: 073/080 prove the minors up to 3 and the derivatives of R=u/M, S=uM; 084 identifies TR/TS and proves their global sufficiency via Rolle, in addition to the exterior A>=128; 085 certifies simultaneously NR,NS>0 on [.5,127.5]; 083 factors detK4 into the product PfR·PfS/productR. This proves all nodes, not a list of matrices.

Sources: `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md`, `POWER_FOUR_TURAN_084.md`, `POWER_FOUR_TURAN_AUDIT_084.md`, `POWER_RECIPROCAL_PFAFFIANS_083.md`, `POWER_STATE_080.md`.

Code: `tools/power_four_turan_compact_085_verify.py`.
Hash:

    4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46

Fixed continuous certificate: 16384 dyadic panels, 512 bits/cap 45, Taylor 40, discs r 1/32, analytic majorant 10^20 and rational remainder 10^20(127/1024)^41/(1−127/1024)<10^−16. Only exact central jets with rigorous errors and global Cauchy remainder; no sign sampling.

## Scope

New coverage of four small or mixed exponents; rates all >=31.5 were already contained in 053. Five generators, all orders and a new window T are not proved. The abstract appendix 083 does not by itself supply the higher signs. 081 only rules out literal BASE inheritance, not a broader recursion. Global continuation active.
