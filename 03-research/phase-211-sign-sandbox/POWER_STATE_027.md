# State027 — Full exterior balance and interior gamma restriction

Status: partial results PROVED, independent audit approved; global sign OPEN. Replaces STATE026. Goal active, papers untouched.

## Joint exterior contribution

POWER_DISCRETE_BALANCE_027 gives an exact floor formula for the weight Omega and proves Omega(t)>=ell−(4logt+9)/t, ell=1+gamma/2−log(4pi)/2>1/50. In particular Omega>.009 for t>=4096 except for integrable logarithmic singularities. Combined with the uniform cutoff026 and the real gamma kernel, it proves positivity and magnitude bounds for the WHOLE joint tail int_T^infinito K_N Omega when T>=max(4096,exp(tau_N)).

For N129 one obtains 0<R=int_4096^infinito K129 Omega<10^-36. Hence W[g129]/norm²=int_1^4096 K129 Omega+R, with the first term still unsigned. The positive tail contributes no significant correction to the coarse budget026. The deficit .15 of that budget is not a proved real interior deficit.

The identities sum K(n)=3/2 and sum K(nx)=x^-32D_N(logx) are exact restrictions from inversion, not sign proofs by themselves. Uniform convergence of Omega to ell is not claimed: the logarithmic peaks prevent it.

## Real mixture and weight of the remainder

POWER_INTERIOR_CONSTRAINT_027 uses the known heat mixture018, rho_N(t)=E exp(−V_N t²), V_N=(u²/4)/G, G~Gamma(N−1/2,1). It keeps all pieces of W by Tonelli with finite magnitudes.

With m_N=EV_N, the specific positive weight L_N(a)=E(V_N−a)_+−(m_N−a)_+ gives exactly rho_N(t)−exp(−m_N t²)=t^4 int exp(−at²)L_N(a)da. For N>=3 its mass is Var(V_N)/2; at N2 the mass is infinite but the representation remains valid for t nonzero.

The comparison with the Gaussian of equal second moment has a strict UPPER sense for ARCH_sharp, by concavity. For the full form, Wgamma−Wgaussian(m_N)=int L_N(a)G_W''(a)da. The sign of that integral was not obtained. The premise of global convexity of the real Gaussian functional is false: G_W''(a)<0 for ALL a>=65536, via elementary bounds. This does not prove that W or the specific remainder is negative.

## Verification, coverage and continuation

POWER_JOINT_AUDIT_027 approves both memos, including normalisations, Fubini/Tonelli, singularities and the exception N2. The proofs were read and both exact verifiers reproduced: PASS. The scripts check constants; uniformity comes from the analytic arguments.

There is no new W coverage nor window T: rows N1,2,3 for all k, cone k>=10000N², eight arbitrary poles and fixed block12 remain. The scalar bridge017 still requires all N,k. A positive mixture with signed curvature is not enough, nor is another tiny favourable tail.

The next search prioritises an inequality for the real interior and a possible full row N4 via exact ARCH, improved autocorrelation weight and alternating polar, after consulting the corpus. The objective is not considered achieved and there is no external blockage.
