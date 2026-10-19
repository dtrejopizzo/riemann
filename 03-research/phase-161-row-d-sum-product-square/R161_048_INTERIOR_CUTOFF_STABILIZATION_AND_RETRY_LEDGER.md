# R161_048 — Exact interior cutoff stabilization and retry ledger

## Polar compression at a fixed window

Let F be supported in [-T,T] with its positive Tate moment zero. R161_003 gives

    C_N F(t) = exp(-t/2) integral_(-infinity)^(t+log N) exp(u/2)F(u) du,
    supp C_N F subset [-T-log N,T-log N].

For log N>=2T this support is disjoint from the open physical window, up to a null endpoint. Thus

    P_T C_N F = 0.                                         (1)

Also P_T tau_(log n) F=0 whenever log n>=2T. Consequently, once N>=exp(2T),

    P_T Z_N F = P_T S_N F
              = sum_(n<exp(2T)) n^(-1/2) P_T tau_(log n) F. (2)

The strict endpoint convention in the sum is immaterial in L2. Equations (1)-(2) are exact, with no asymptotic passage. They hold on primitive sources in either parity sector. They do not assert the same support for the noncompact source Fcal F.

Therefore increasing the synthesis cutoff beyond the window scale changes only the exterior of Z_N F. Its compressed exponential moments have already stabilized to the finite collar formula of R161_047. No new interior moment equation follows merely by sending N to infinity. The polar layer is wholly exterior at these cutoffs, exactly as in R161_028.

## What the Poisson relation still says

The finite identity

    Z_N Fcal F - epsilon Z_N*F = E_N F

retains the noncompact Fourier-transformed source. Equation (2) cannot be applied to that source. Nor does convergence of E_N F alone give the coherent differentiated difference; R161_041 computes the opposite orientation in that derivative. This leaves a definite, rather than unspecified, missing step: control the exterior Fourier block jointly with the renormalized translated collars.

## Audit of this resumed attempt

1. R161_046 reconstructed the closure implications and proved finite detection on a fixed finite-dimensional radical. It corrected the unsupported claim of independence from the full physical hypotheses.
2. R161_047 extracted the fixed Gamma residue, located it in the exterior distribution, and computed the exact exponential translation collar. It did not annihilate that coefficient.
3. The present calculation includes the continuum counterterm and shows that the interior compression stabilizes exactly. This does not supply a sign for the remaining exterior block.

Thus the resumed attempt has repeatedly reached the same missing exterior annihilation law. The known identities and the completed calculations do not prove it. None of these observations rules out such a law for the physical operator, and none warrants declaring D closed.

Current status: the backward dependency map and finite collar calculations are complete; the requested gate and D remain unproved. A further closure claim requires an independently checked exterior identity or estimate that forces the Gamma moments to vanish. No such identity has been derived in this attempt.
