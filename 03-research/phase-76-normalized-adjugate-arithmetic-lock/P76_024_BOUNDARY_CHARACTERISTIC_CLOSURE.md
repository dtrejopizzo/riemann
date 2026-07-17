# P76.024 - Boundary characteristic closure theorem

## Canonical approximant

For an admissible nested cutoff, let `T_{+,L,N}` be the right-boundary Schur
transfer from P76.013 and define

```text
Phi_{L,N}(z)
=sin(zL/2)T_{+,L,N}(z)
 /lim_{w->0} sin(wL/2)T_{+,L,N}(w).             (BCF-1)
```

Then `Phi_{L,N}(0)=1`.  It is constructed from finite Gamma-prime CCM data,
the ground level `mu_{L,N}`, and one Schur solve.  It uses no eigenvector,
zero list, fitted scalar, or background divisor.

By P76.023, every finite `Phi_{L,N}` has only real zeros under strict
interlacing and the stated nondegeneracy.

## Conditional closure theorem

Assume there is an admissible resolved path `N=N(L)` such that:

```text
N(L)/L -> infinity.
```

### BCF-NORMAL

```text
{Phi_{L,N(L)}} is locally bounded on the centered strip
S={z: |Im z|<1/2+epsilon}.
```

### BCF-SAFE-ID

On a nonempty open subset corresponding to the Euler absolute-convergence
region `Re(s)>1`,

```text
Phi_{L,N(L)}(z) -> Xi(1/2+iz)/Xi(1/2)
```

locally uniformly.

Then

```text
Phi_{L,N(L)} -> Xi(1/2+iz)/Xi(1/2)
```

locally uniformly throughout `S`.

### Proof

`BCF-NORMAL` gives a normal family by Montel.  Every subsequence has a
locally uniform sublimit.  `BCF-SAFE-ID` identifies every sublimit with the
same completed-zeta function on a nonempty open set; the identity theorem
identifies it on the connected strip.  Hence the full family converges.

Every approximant is real-rooted by P76.023.  Hurwitz therefore forbids a
nonreal zero in the limit.  Thus all nontrivial zeros of zeta lie on the
critical line.  Equivalently, Omega7 closes.  QED conditional on the two
analytic hypotheses.

## Numerical evidence

At fixed `lambda=6`, increasing `N=6,...,12` gives on the real interval
`[0,12]`:

```text
relative L2 error of even part: 0.347 -> 0.199,
relative sup error:             0.342 -> 0.189,
odd/even ratio:                 0.163 -> 0.107.
```

In the Euler-safe sample `s=1.25,1.5,2.0`:

```text
maximum relative error: 0.086 -> 0.037,
odd/even ratio:          0.097 -> 0.051.
```

At `N=9`, full-function falsifiers on `[0,12]` give:

```text
zeta:    relative L2 error 0.258, odd/even 0.129;
planted: relative L2 error 2.228, odd/even 0.563;
random:  relative L2 error 2.076, odd/even 0.881.
```

These data support both identification and arithmetic discrimination.  They
are not used as proof premises.

## Exact remaining work

Omega7 is reduced to two explicit analytic lemmas for the new canonical
relative characteristic:

```text
BCF-NORMAL:
derive local bounds from the real divisor, sine-type normalization, and
boundary Schur determinant ratio;

BCF-SAFE-ID:
evaluate the boundary determinant ratio in Re(s)>1 from the finite
Euler/Gamma formula and prove convergence along an admissible N(L).
```

Unlike the Phase-71 abstract stable projection, `(BCF-1)` supplies the
previously missing functorial comparison between consecutive finite
sections.  Unlike the Phase-75 adjugate, it has no exploding mesh product and
no eigenvector phase.

P76.026 gives an exact Fourier representation and a strong sufficient
weighted-`L1` theorem.  The norm audit P76.027-P76.028 shows that strong
inverse-kernel convergence is unnecessarily restrictive.  P76.029 gives
the corresponding weak exponential theorem.  The bilateral characteristic
of P76.030 and the canonical-product bound of P76.031 remove the separate
stability hypothesis entirely.  The current sharp endpoint is the single
Euler-safe determinant limit `SA-SAFE`.
