# POWER_STATE_065 — Exact oscillation of the autocorrelation

Status: **PROVED/APPROVED**. Source POWER_CONTACT_OSCILLATION_065.md; independent audit POWER_CONTACT_OSCILLATION_AUDIT_065.md and a further review. Analytic proof, without a numerical campaign. Papers untouched.

## Result and scope

For ALL u>0,N>=1,k>=1, the autocorrelation of s^k/(s+u)^(N+k) has exactly k simple positive zeros, alternating signs starting from positive and last root at x=ut strictly less than4k(N+k−1). For u>1/2, the WHOLE tail of contacts u logq>=4k(N+k−1) has contribution of sign(−1)^(k+1): favourable for odd k, adverse for even k; absolute convergence and strict sign of its sum.

Difference relative to019: exact count for ALL k, not another evaluation k=1. Vanishing moments up to2k−1 plus degree resolve N=1; one-sided exponential filters and Rolle with boundary at infinity preserve simple zeros and propagate in N. The finer bound019 for k=1 is not replaced. No generic total positivity is assumed and no prime is erased. The magnitude against the prefix/ARCH/polar is not controlled: no new W row, windowT nor global sign. Papers untouched.

## Exploration of monotonicity: no new interior inequality

The review of B_N>=A_N from STATE064 produced neither a uniform proof nor a counterexample for the full form. Near u=1/2, LOW_TABLE018 exactly cancels the polar divergence with the continuous principal part of the comb: no polar dominance is available. For fixed N and u→infinity, the computation only gives B_N−A_N=u∂_uA_N→1 (ARCH gain→1; polar and arithmetic derivatives→0). It is an eventual comparison at variable rate, not control of u=63/2 with variable N. No other N was computed and it is not recorded as a new descent tool.

## Query066 — what is missing after separating the sign intervals

Review via insight048 and case and independent checks: the count065 does not by itself provide a compensation estimate. For K=c_f/||f||², w(x)=x^(-1/2)K(log x), D(x)=psi_Lambda(x)−x+1 and u>1/2, the full cancellation018 and Abel keep exactly

    W[f]/||f||² = ARCH_sharp[f]/||f||² + 2 int_1^infinito D(x)w′(x)dx.

The nodes X_i=exp(chi_i/u) satisfy w(X_i)=0. On each interval between two nodes, and on the last up to infinity, int w′=0. If M=int(w′)_+=int(w′)_->0 and nu_± have densities (w′)_±/M, their contribution is exactly M(E_(nu_+)D−E_(nu_−)D). The signed comparison of these TWO means remains pending: the sign of w does not decide it. The first interval [1,X_1] is different, since w(1)=1 and int w′=−1; equal masses are not attributed to it.

A second integration, with E_1(x)=int_1^x D(y)dy, introduces [E_1 w′] on each interval. Since the nodes065 are simple, w′(X_i)≠0: those boundaries cannot be omitted when bounding intervals separately. They do cancel exactly on recomposing the global integral, by continuity of E_1 and w′. No impossibility for other estimates of the residue is deduced. The extreme boundaries are controlled with D=O(x log x), E_1=O(x² log x) and the rational-temporal decay for u>1/2.

The proposal of interpolating smooth weights at the nodes was also checked. With UNNORMALISED autocorrelations K_(N,k)=c_(f_(N,k)) and C_N=c_(g_N), the positive Gaussian mixture already used018/027 and Rodrigues give, under integrability and vanishing of boundaries,

    int_0^infinito K_(N,k)(t) phi(t²)dt
      = (−1)^k Gamma(N)/Gamma(N+k)
          int_0^infinito t^(2k) C_N(t) phi^(k)(t²)dt.

Thus phi^(k)>=0 gives a sign for that smooth pairing without needing the new count065. The ordinary variant with phi(t) and derivative2k is already obtained from K_(N,k)=(−1)^k C_(N+k)^(2k) by integration by parts. Neither variant allows attributing that convexity to the full weight of W: near a contact log q>0 it contains a nonzero atom, while ARCH and polar are smooth there. Differentiating produces a derivative of delta, which is not a positive measure; nonnegative test functions, concentrated at that contact and with derivative of either sign, verify the local defect. This only invalidates that sufficient hypothesis, it does not prove negativity of W.

Query deduplicated: identities and pending conditions, without new W region nor new theorem result for the indices. There was no campaign of cases and the papers remain untouched.
