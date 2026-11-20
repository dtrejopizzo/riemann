# POWER_HIGH_ORDER_PM_NOGO_007 — High falsifier of arch+polar movement uniform in dimension

Status: PROVED. It does NOT refute sign transport, nor the local order-four result, nor the complete sign. Papers untouched.

## 1. Corpus and new reason

Consulted the ROUTES-TRIED-INDEX index, master grid and crossword through searches high-order pole, gamma packet, pole no-go, 131072 and digamma derivatives; reviewed POWER_POLE_MOVEMENT_004 and POWER_POLAR_MOVEMENT_005. The order-one counterexample of 005 only had small rates (1 and 2). The new reason is an EXACT falsifier inside the range u>=63/2, with large explicit dimension and a scalar identity: no spectra of large matrices are searched for. The construction is verified here.

## 2. Global archimedean lemma

For m(tau)=Re psi(1/4+i tau/2)-log pi,

    0<=tau m'(tau)<4, tau real.                             (G)

Proof. Put t=|tau|/2 and a_k=k+1/4. The differentiated digamma series gives

    tau m'(tau)=Σ_{k>=0} 2 a_k t²/(a_k²+t²)².

If t<=1, the term k=0 is <=1/(2a_0)=2. The rest is at most

    2Σ_{k>=1}(k+1/4)^-3
      <=2[(5/4)^-3+∫_1^∞(x+1/4)^-3 dx]=208/125.

The sum is <=458/125<4. If t>=1, f(a)=2at²/(a²+t²)² is nonnegative and unimodal, with integral over (0,infinity) equal to 1 and maximum 3sqrt3/(8t)<1. Comparing separately the increasing and decreasing branches with integrals over panels of length one, and setting aside at most two terms near the maximum, the sum over any lattice of step one is <=∫f+2max f<3. This applies to a_k. At t=0 the result is immediate. Absolute convergence justifies differentiating the series.

## 3. Fixed-numerator family and exact polar term

For integer n>=1, u>1/2, let f_{n,u}(y)=y^{n-1}exp(-uy)1_{y>0}. Its Laplace transform is (n-1)!/(s+u)^n; the constant factor does not alter quotients. It is the fixed numerator 1 with n equal poles u. Directly,

    ||f||²=(2n-2)!/(2u)^{2n-1},
    A=(n-1)!/(u-1/2)^n, B=(n-1)!/(u+1/2)^n.

The normalized polar quotient is

    P_n(u)=2AB/||f||²
      =4^n/[u binom(2n-2,n-1)]*(1-1/(4u²))^-n.            (P)

Since binom(2n-2,n-1)<=4^{n-1}, we have P_n(u)>=4/u. Moreover

    u d(log P_n)/du=-1-n/[2(u²-1/4)].                     (PD)

The normalized spectral probability is a constant times u^-1[1+(tau/u)²]^-n. Changing tau=ut in the archimedean energy A_n(u) and using (G) gives

    u A_n'(u)=E[tau m'(tau)]<4.                           (AD)

Differentiation under the integral is justified by (G). No matrix of size n is evaluated.

## 4. Explicit high counterexample, also for each individual pole

Take u=63/2, n=2^17=131072. For E_n=A_n+P_n,

    u E_n'(u)<4-(4/u)[1+n/(2(u²-1/4))]
              =4-264/31=-140/31<0.                       (NEG)

The equality is exact rational arithmetic; it uses no approximations of factorials or large powers.

To pass to INDIVIDUAL movements, define E(u_1,...,u_n) with transform 1/Π_j(s+u_j). It is differentiable and symmetric for u_j>1/2. At confluence all partials are equal, and

    E_n'(u)=Σ_j ∂E/∂u_j=n ∂E/∂u_1.

Hence, at the declared point,

    u ∂E/∂u_j < -140/(31n), each j.

There is epsilon>0 such that increasing only ONE pole from 63/2 to 63/2+epsilon decreases the arch+polar quotient of the fixed numerator. All poles stay in the high range. Global dilation is not confused with individual change: differentiable symmetry is the explicit argument allowing passage between the two.

## 5. Precise scope

The statement «for all n and all poles >=63/2, individually increasing the poles does not reduce the arch+polar quotient of any numerator» is FALSIFIED. The positive derivative of POWER_POLAR_MOVEMENT_005 §6 cannot be extended uniformly in dimension.

It is NOT concluded that the energy is negative, nor is a transport that preserves only the sign discarded: a positive energy may decrease and remain positive. The comb has not been included either. The archimedean covariance theorem remains valid; the sign change comes from the derivative of the positive polar term. The local result n=4 is not affected.

New reusable tool: the global bound (G) and the exact polar term (P) allow auditing transport proposals without building large matrices.

The falsified statement is the Rayleigh quotient for EVERY numerator under the rational identification of fixed numerators. No counterexample to monotonicity of lambda_min or of other compressed eigenenergies is provided here: a decrease of the quotient of a particular vector does not imply a decrease of the minimum over the space. Monotonicity of eigenenergies of the ARCHIMEDEAN part remains proved by the separate argument of 004.
