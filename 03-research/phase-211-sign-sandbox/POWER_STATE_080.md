# POWER_STATE_080 — Three arbitrary admissible powers

Status: **PROVED**, certificate FULL PASS and mathematical/code audit approved. Independent reproduction 92790 exit0/FULL PASS 4096 and matching hash. Global objective of Paper 46 **OPEN**; papers untouched.

## Complete result and sources

For any real exponents ai>1, the form W is positive on the span of up to THREE corresponding powers, except for the zero function. For three distinct nodes the full kernel Kij=[M(ui)+M(uj)]/(ui+uj), ui=ai−1/2, is positive definite; for repeated ones coefficients are grouped. It includes ARCH, polar and all contacts via the congruence CONE001.

Proof chain:

1. BASE073: M>0, M'>0, M''<0 and M/u strictly decreasing.
2. 079: under BASE, g(x)=a sqrt(x)/M(sqrt(x))−1 concave on an interval of squares is equivalent to all its triples being PSD; strict concavity gives distinct triples PD.
3. 078: g''<0 analytically for u>=63/2.
4. 080: continuous certificate g''<0 on ALL of [1/2,63/2], with 4096 fixed dyadic panels, central jets arb 256 bits/cap 20, Taylor degree 16 and uniform rational Cauchy remainder. Run 43260 exit0/FULL PASS.

Sources: `POWER_THETA_G_COMPACT_080.md` (full source read and audited), `POWER_THETA_G_COMPACT_AUDIT_080.md`, `POWER_THREE_SECANTS_079.md`, `POWER_THREE_SECANTS_AUDIT_079.md`, appendix 078 of `POWER_STATE_077.md`.

Code: `tools/power_theta_g_compact_080_verify.py`.
SHA256 checked:

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc

Exact Cauchy remainder:

    5285183618944392932503807265625/
    41901009533176678637026095660718210485846016 <10^−12.

## Novelty and limits

053 already covered up to thirteen arbitrary rates >=31.5. 080 adds ALL admissible triples, including small and mixed rates. It does not extend the number of generators nor certify a new time window. Four generators, all orders and the global sign remain OPEN. Neither concave h nor inheritance of BASE by the remainders G_p is used: 081 refutes that literal inheritance, 082 keeps a broader conditional reciprocal criterion.

The history of failed enclosures of the remainder is documented in audit 080. Mesh/interval/precision/margin 0 were kept; the final Cauchy-remainder representation is different and was audited before its run. No interval FAIL was promoted to a counterexample or to a proof.
