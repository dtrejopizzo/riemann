# POWER_STATE_089 — Global R4 transport and real Turán

Status: **PROVED**, run 40406 exit0/FULL PASS 1024 origin + 8192 remainder and math/code audit approved. Independent reproduction 87911 exit0/FULL PASS 1024+8192 and matching hash. Paper 47 global OPEN; papers untouched.

## Structural results

1. Wt(1,A,B,C)<0 for ALL t>0: certificate 089 two complete branches plus analytic exterior 088.
2. In the order [1,B,A,C] the previous Wronskians 086 and the fourth give global Chebyshev; the determinant of the densities rho4 is negative for ALL its nodes.
3. Without TP4/confluent Andreief, this sign is transferred to −(Z'/u)^4T_R<0. Therefore T_R=2R'R'''−3R''²>0 at ALL x=u²>0.
4. 090 applies globally: h=1/b strictly concave. With 086 g_*=xb strictly concave, 078 proves all pairs of the remainder Gp strictly PD for ALL p>0.

Sources: `POWER_THETA_DENSITY_COMPACT_089.md`, `POWER_THETA_DENSITY_COMPACT_AUDIT_089.md`, `POWER_THETA_DENSITY_TRANSPORT_089.md`, `POWER_RECIPROCAL_SECANT_CONCAVITY_090.md`, 086/088.
Code: `tools/power_theta_density_compact_089_verify.py`.
Hash:

    995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa

## Certificate and scope

Origin lambda [0,1/256]: 1024 panels, 1024 bits/cap 23, Taylor 16, B 1e48. Remainder t [1/16,1]: 8192 panels, 512 bits/cap 47, Taylor 40, B 1e60. Each central jet includes 16 theta modes and ALL the complete tail via coefficient errors before differentiating. Partial parity at the origin forced via the average ±sqrt lambda. Uniform Cauchy remainder of the determinant pays for the whole panel. Parameters fixed/audited before the run; no FAIL/adjustments.

No new W coverage relative to 085 (four exponents ai>1 already PROVED). No global S4 transport, five/all orders or new T. The remainder Gp does not inherit BASE 081 nor its Turán inequalities; the second reciprocal curvature and the iteration remain OPEN. Continuation active.

## Audited extension 090

The lemma anchored at P, proved in both orientations, applies to g=xb=aR−1, since T_g=a²T_R>0. Therefore S_G has strictly negative second derivative for ALL p,x>0. The other curvature, R_G, requires global T_h>0: it remains OPEN and corresponds to the next anchored jet made explicit in 090. There is no automatic inheritance nor new closure of W.

The explicit global counterexample of 090§9 refutes the generic inheritance T_f⇒T_H: with w=(5−e^−x)/4, T_f>0 globally but T_H(0)=−1/192. It does not decide T_h of Phi nor the specific iteration.
