# POWER_AUDIT_005 — Scope of pole movement when the polar term is kept

Status: PROVED exact identity and falsifier of the unrestricted extension; OPEN order-four comparison at rates >=31.5. Does not modify papers.

## 1. Audit of antecedents of the archimedean lemma

New targeted search in index, corpus, grid and crossword: pole movement, moving poles, movimiento de polos, covariance/covarianza, numerator fixed/numerador fijo and Rayleigh. The specific lemma of POWER_POLE_MOVEMENT_004 was not found before this round. E85_005_PATH_DECISION.md uses 'moving poles' for resolvents and parity complements, not for rational poles of test functions; E101_079 uses the phrase for possible moving poles of interpolating kernels. Nor are monotonicities by inclusion of subspaces this result: the rational spaces of distinct poles are not nested, and the new proof identifies the same numerator and compares reweighted probabilities.

Defensible novelty: specific lemma of monotonicity of eigenenergies of an even increasing multiplier under individual increase of real poles of rational denominators, proved by covariance. No novelty is attributed to the general covariance principle for two increasing functions nor to the rational bases. The local search does not certify novelty across the whole literature.

## 2. Full formula with the polar term

For poles u_j>1/2 and fixed numerator P, write H_u(s)=P(s)/prod_j(u_j+s), the Laplace transform of f_u. Then

    A_u=H_u(-1/2), B_u=H_u(1/2),
    2A_u B_u=2P(-1/2)P(1/2)/prod_j(u_j²-1/4).

When increasing u_j to v_j>=u_j,

    R(tau)=prod_j(u_j²+tau²)/(v_j²+tau²),
    r0=prod_j(u_j²-1/4)/(v_j²-1/4).

If mu is the old normalised spectral density and p_u=(2A_u B_u)/||f_u||², the difference of the archimedean PLUS polar quotient is exactly

    E_v-E_u=[Cov_mu(m,R)+(r0-E_mu[R])p_u]/E_mu[R].       (AP)

This keeps the normalisation of the norm: ||f_v||²=E_mu[R]||f_u||². Omitting that factor would change the comparison.

Each factor (u²+t)/(v²+t) is nondecreasing for t>-u²; therefore r0<=R(tau) and r0<=E_mu[R], with strict inequality if some pole increases. Verified consequences:

* If p_u<=0, both terms of the numerator of AP are nonnegative: the movement does preserve the archimedean+polar quotient for that numerator.
* If p_u>0, the second term has opposite sign. The archimedean theorem is not automatically transported to that part of the form.
* The sufficient and exact obligation for that numerator is Cov_mu(m,R)>=(E_mu[R]-r0)p_u. It remains a real inequality that can be attacked; it is not declared false in the relevant range of four poles.

The comb is not included here; its variation introduces another distinct term.

## 3. Elementary falsifier with the REAL archimedean datum

Dimension one, numerator P=1. For f_u(y)=e^(-uy), u>1/2, the archimedean+polar quotient is

    E(u)=psi((u+1/2)/2)-log pi+4u/(u²-1/4).

Moving u=1 to v=2 increases the pole but decreases this quotient. Indeed

    psi(5/4)-psi(3/4)=4-pi,
    4*2/(2²-1/4)-4*1/(1²-1/4)=32/15-16/3=-16/5,
    E(2)-E(1)=4/5-pi<0.

The psi identity uses its recurrence and the reflection values at 1/4,3/4. This is the exact gamma multiplier and polar term of the form, not a substitute scalar model. It uses no numerical computation or sweep.

**Scope:** it refutes the extension of the archimedean movement to archimedean+polar for ALL poles >1/2. The poles 1,2 lie outside the range >=31.5; it does not refute a dimension-four comparison in that range, nor the sign of that family, nor the bounds proved for three.

## 4. Next bounded check

For the next four-generator theorem, the positive polar term that rescues the low archimedean block must be kept, and its comparison proved via AP or via a different inequality. The property p_u<=0 already has favourable transport and is not the hard sector. A movement candidate in p_u>0 requires the compensating covariance bound; recalling that m is increasing is not enough. No falsifier has been sought by sweep, nor is it claimed that there is one for four rates >=31.5.

## 5. Certificate of four confluent poles: complete review

POWER_CONFLUENT_FOUR_005.md and the actual file phase-211-sign-sandbox/tools/power_confluent_four_005_verify.py: APPROVED. The verifier was run with output PASS. The fourth Toeplitz coefficient is checked from the third Laguerre function: 2up'+4u²p''+(4/3)u³p''' produces exactly b+(3969/8)psi''(16)+(250047/96)psi'''(16). The moments sqrt(63)(-32)^j/31^(j+1) and sqrt(63)(-31)^j/32^(j+1) are the exact Laplace integral of Laguerre; their polar product is Toeplitz and rational.

The upper bound for d uses gamma>H256-log256-1/256 and pi>223/71; r=76/147 is exactly the atanh parameter of 223/71. Their directions are correct, as are the tails of S2,S3,S4 and the alternating signs of psi'',psi'''. The norm of the Toeplitz error is controlled by maximal row sum <1/200. The LDL checks and those of the two centrosymmetric blocks are correct. In LDL the pivot column is not modified during the step.

Certified: Arch+Polar>(49/200)I and |Comb|<(13/1000)I via B4=32552; therefore W>(29/125)I>(1/5)I on the confluent space of four poles u=31.5. The Laguerre vector (1,-1,1,-1) does have Arch/||v||²<-.1, without contradicting the positive polar compensation. This result is not transferred to four arbitrary rates via the archimedean movement: the AP warning of §2 remains in force.

## 6. Review of the confluent transport quartic

POWER_POLAR_MOVEMENT_005 §§4–5: APPROVED as identities and as a scalar theorem n=1, u>=8. The trigamma comparison >=1/x, the bound 16/(17u) and the loss <5/u² give E'>0 in that range.

To verify D4, set f=sum x_j F_j, g=sum x_j F_(j+1), ||x||=1. The derivative with respect to a single pole with fixed numerator is -(f-g)/(2u), while the derivative of the norm is -(1-c1)/u. Hence

    uE'=inner(g,Mf)-E c1,
    inner(g,Mf)=m1+(m0+m2)c1+(m1+m3)c2+(m2+m4)c3,
    E=m0+2m1c1+2m2c2+2m3c3.

Substituting gives exactly D4 and cancels m0. The formulas for mk derived from the kernel and its polar addition coincide with the previously audited cases up to order three; the same binomial expansion produces the declared general formula. The quartic is a genuine finite sign target, not an automatic consequence of the earlier monotonicities. The minimisation diagnostics are not used in this approval.

## 7. Antecedents of the next arithmetic test of dimension twelve

The local search for a specific confluent Laguerre test at rate 31.5 and dimension twelve found no exact antecedent. There are earlier uses of Laguerre with different objects: phase-104/104_46_FIXED_LAGUERRE_MARKOV_EXTREMAL_GATE uses L_(n-1)^(1)(s log d) as a transport vector by divisors; phase-168/R168_203_LOCAL_LAGUERRE studies a differential inequality for entire functions. Neither is the present universal exterior block.

The general need for a prime contribution when the number of negative archimedean directions grows already has antecedents: the negative counts of Paper 47 and the fact that the polar term has finite rank prevent expecting archimedean+polar positivity on all growing subspaces. Therefore any novelty of a dimension-twelve test must be declared as an explicit rational vector in THIS space, with certified AP deficit and comb repair; not as a first discovery that arithmetic is needed. The concrete certificate is awaited before recording its sign.

## 8. Exact local SOS certificate received and reviewed

POWER_POLAR_MOVEMENT_005§6 and tools/polar_derivative_sos_005.py: APPROVED and rerun with PASS. The series of psi^(j)(16), j1..4, are summed up to 2000 and their tails lie correctly between the integrals from 2001 and 2000; the rational interval class I keeps outward rounding. The four intervals of radius 10^-4 around (8887,1116,2213,1126)/10000 are proved.

The verifier builds the homogeneous quartic Dbar-.08N² and checks EXACTLY all its coefficients against z^TQz. The matrix Q is symmetric and its rational LDL has ten pivots >.2. The in-place update preserves the pivot columns. The sensitivities of D4 with respect to m1,m2,m3,m4 are bounded by 4N²,4N²,3N²,N² respectively using |c_k|<=N. Therefore the total loss is <.0012N² and D4>.0788N²>.075N².

The derivative factor was reviewed explicitly: moving ONE pole, f'=-f/(s+u), whence uE'=D4 for norm one. Moving all four simultaneously would give FOUR times that derivative. The individual claim dE/dv_j>3/(40u)=1/420 at u31.5 is therefore correct with no omitted factor. E here means ARCH+POLAR, it does not include the comb. The compactness step to a common neighbourhood of rates is valid in the fixed space of numerators, without providing a quantified radius. Transport over the whole orthant is not inferred.
