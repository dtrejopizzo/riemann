# State 015 — full mixture and eventual positivity

Status: PROVED partial results; global sign OPEN. Goal active. Papers untouched. Replaces POWER_STATE_014 as the current summary.

## Consolidated results

W[f]>||f||²/1000 still holds for all spaces of eight real poles >=63/2, with repetitions, numerator of degree less than eight and all arithmetic contacts. Rational certificate and audit in POWER_SIGNED_TRANSFER_014 and POWER_SIGNED_AUDIT_014.

The bridge POWER_CONFLUENT_BRIDGE_014 shows that nonnegativity of all confluent blocks of a single rate suffices. It does not require a uniform margin in dimension. All sizes remain open.

## New general result

POWER_HIGHPASS_015, fully reviewed in POWER_HIGHPASS_AUDIT_015: fixing u>1 and N, there exists K_N such that the FULL form is positive on all subspaces Q^k V_N for k>=K_N, where Q(s)=s/(s+u) and V_N has transforms P(s)/(s+u)^N, deg P<N. Uniformity includes all numerators, even ones depending on k.

The normalised archimedean part is >=(log k)/2-C_N; the full comb and the normalised polar tend uniformly to zero. The proof uses convergence of rescaled Gram matrices, not only the leading term of a fixed polynomial. K_N is not yet effective nor uniform in N.

## Exact mixture

POWER_GEOMETRIC_TRANSFER_015, reviewed in POWER_MIXTURE_AUDIT_015 and POWER_HIGHPASS_AUDIT_015, expresses pole transport through a positive mixture of the energies W[Q^k f_base]. It includes the polar and all contacts, converges absolutely and has Rayleigh weights correctly normalised by the norms. The finite identity keeps the remainder on the target function.

The novelty relative to the pointwise deficit013 is keeping the full signed correction and its spectral structure. Relative to014, the expansion and its uniform tail are now proved. These identities do not by themselves prove the arithmetic sign.

## Pending obligation

For each fixed N a sufficient transport condition remains on a finite segment of initial blocks. Its effective endpoint and its sign for all N are not known here. Eventual positivity does not allow inferring positivity of those initial terms nor of every mixture. There is no global proof nor counterexample of the full form.

Next work: look for a mechanism to control the initial segment and its dependence on N, checking it first against the index and the high-order falsifiers007–008. Do not repeat a campaign of finite certificates as a substitute for that mechanism.
