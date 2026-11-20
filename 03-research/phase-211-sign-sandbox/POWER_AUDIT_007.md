# POWER_AUDIT_007 — Falsifier of uniform transport in high dimension

Status: PROVED, independent review of POWER_HIGH_ORDER_PM_NOGO_007.md. Refutes neither sign nor sign transport; does not affect the local four-pole theorem. Papers untouched.

## 1. Digamma bound checked

The positive series for tau m'(tau) is correct, with t=|tau|/2 and a_k=k+1/4. For t<=1, the initial term is bounded by 1/(2a0)=2. The tail is bounded by 2sum_(k>=1)(k+1/4)^-3; the first term plus the integral from 1 is exactly 208/125. Thus the total is <=458/125<4.

For t>=1, the function f(a)=2at²/(a²+t²)^2 has integral 1 and maximum 3sqrt(3)/(8t)<1. The unimodal lattice comparison by integral plus two maxima is valid: set aside up to two sites whose adjacent panels touch the continuous maximum; on the increasing branch assign to each site its right panel and on the decreasing branch its left panel. The remaining panels are disjoint and the function on each dominates the assigned value. The omitted sites cost at most two maxima. Thus sum f(a_k)<=integral_0^infinito f+2max f<3. It is proved globally that 0<=tau m'(tau)<4. The series can be differentiated on compacts by uniform convergence of the derivatives; at tau0 the expression extends by 0.

## 2. Exact polar term and derivative

The Gamma norm of y^(n-1)e^(-uy) and its moments produce exactly

    P_n=4^n/[u binom(2n-2,n-1)]*(1-1/(4u²))^-n>=4/u.

The logarithmic derivative, computed both from this formula and from the unsimplified moments, is

    uP_n'=-(1+n/[2(u²-1/4)])P_n.

The scale of the spectral probability is u^-1 times a fixed density of tau/u. The global bound of §1 provides uniform domination to differentiate its average of m and proves uA_n'<4 without assuming Stirling asymptotics or spectral bounds.

At u63/2, u²-1/4=992, n131072 and n/1984=2048/31. The lower polar loss is exactly

    (4/u)(1+n/[2(u²-1/4)])=(8/63)(2079/31)=264/31.

Therefore uE_diag'<4-264/31=-140/31. All these are exact rational comparisons.

## 3. Individual movement and scope

The quotient of the rational function 1/prod(s+u_j) is differentiable and symmetric for u_j>1/2. By the chain rule on the diagonal, E_diag'=sum partial_jE=n partial_1E. The diagonal derivative just bounded is therefore n times each individual movement; the negative sign does not come from confusing two parametrisations. In a small positive individual direction all poles remain >=31.5 and the ARCH+POLAR quotient decreases.

The falsified class is the monotonicity of this quotient for all numerators and all orders in the high range. No negative energy is shown, no prime contacts are included, and a transport rule preserving only the sign is not refuted. The positive local case n4 and the purely archimedean movement remain intact.

Additional precision of scope: the falsifier only decreases the Rayleigh quotient of a fixed numerator. It is not a counterexample to the monotonicity of lambda_min or of another compressed eigenenergy of ARCH+POLAR. The minimum over the space may remain nondecreasing even though one of the particular quotients decreases. Nor is that inference made in this audit.
