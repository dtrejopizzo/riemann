# E78.101 - `MU-DIR` reduces to basepoint convergence plus a local paired derivative bound

**Run:** 2026-07-19.  
**Scope:** front B only (`SAFE-GAMMA-IDENT`, fixed-`L` core).  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the live
directional term is not an opaque moving-`mu` defect; it is exactly controlled
by two smaller obligations: convergence of the intrinsic levels `mu_N` to the
fixed basepoint `0`, and a local paired bound for `partial_mu J_{L,N}` on one
small interval around that basepoint.

## 0. Wall checklist

```text
MW-1:  respected. No positivity claim or Weil-form sign target appears.
MW-2:  respected. This stays inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No primewise-to-global assembly.
MW-4:  respected. The reduction uses an upper bound on a paired derivative, not
       a lower-bound/sign mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator, no
       ambient inverse norm before signed cancellation.
P76.061: respected. The derivative is kept in the paired Cauchy/transfer form;
         no ambient resolvent norm is promoted to the target.
E72.16/E77.7az: respected. This is front B, where build separation is expected;
                the planted build is allowed to fail at the basepoint target.
```

## 1. Exact starting point

E78.99 isolated, for one fixed `L` and one safe compact `K`,

```text
MU-DIR(L,K):
  sup_{sigma in K} int_0^{mu_N} |partial_mu J_{L,N}(sigma;t)| dt -> 0.  (M-1)
```

with

```text
J_{L,N}(sigma;mu)
 = L coth(sigma L/2)
   + 2 Re(i T'_{L,N}(i sigma;mu)/T_{L,N}(i sigma;mu))
   - B_ext,L,N(sigma).                                      (M-2)
```

The only `mu`-dependence is in the transfer `T_{L,N}(z;mu)`.

## 2. Exact paired derivative formula

Write

```text
A_N(mu)=H_{L,N}^{inner}-mu I,
x_N(mu)=A_N(mu)^(-1)b_N,                                   (M-3)

T_{L,N}(z;mu)=1/(z-d_b)-sum_j x_N(mu)_j/(z-d_j).           (M-4)
```

Differentiate `(M-3)`:

```text
partial_mu x_N(mu)=A_N(mu)^(-2)b_N.                        (M-5)
```

Therefore

```text
partial_mu T_{L,N}(z;mu)
 = - r_z^{in} A_N(mu)^(-2)b_N,                             (M-6)

partial_mu T'_{L,N}(z;mu)
 = r_{z,2}^{in} A_N(mu)^(-2)b_N,                           (M-7)
```

where `r_z^{in}` is the inner Cauchy row and

```text
r_{z,2}^{in} = (1/(z-d_j)^2)_j.                            (M-8)
```

By differentiating the logarithmic quotient in `(M-2)`,

```text
partial_mu J_{L,N}(sigma;mu)
 = 2 Re i[
     partial_mu T'_{L,N}(i sigma;mu) / T_{L,N}(i sigma;mu)
     - T'_{L,N}(i sigma;mu) partial_mu T_{L,N}(i sigma;mu)
       / T_{L,N}(i sigma;mu)^2
   ].                                                      (M-9)
```

This is an exact paired double-resolvent formula.  No ambient inverse norm has
been introduced.

## 3. The smaller replacement target

Fix `L`, `K`, and one radius `eta>0`.  Define

```text
MU-BASEPOINT(L):
  mu_N -> 0.                                               (M-10)

PAIRED-DMU-LOCAL(L,K,eta):
  there exist C_{L,K,eta} and N_0 such that
  sup_{N>=N_0} sup_{sigma in K} sup_{|t|<=eta}
    |partial_mu J_{L,N}(sigma;t)| <= C_{L,K,eta}.          (M-11)
```

Then, once `|mu_N|<=eta` for `N>=N_1`,

```text
sup_K int_0^{mu_N} |partial_mu J_{L,N}(sigma;t)| dt
 <= |mu_N| C_{L,K,eta} -> 0.                               (M-12)
```

Hence:

```text
MU-BASEPOINT(L) + PAIRED-DMU-LOCAL(L,K,eta)
=> MU-DIR(L,K).                                            (M-13)
```

## 4. Why this is a genuine reduction

This is not a reparametrization of `MU-DIR`.

The old target asked directly for decay of a moving integral along the intrinsic
path `t in [0,mu_N]`.  The new pair separates that into:

```text
1. one scalar convergence statement for the endpoint mu_N -> 0;
2. one local boundedness statement for the paired derivative on a fixed box
   |t|<=eta.                                               (M-14)
```

That is strictly less information than proving the full moving integral small
from scratch.  In particular, `(M-11)` no longer tracks the shrinking path
length, and `(M-10)` no longer carries any derivative information.

## 5. Falsifier location under the reduction

This reduction predicts exactly where the planted build should fail.

For front B, the falsifier is allowed to separate.  The natural break here is:

```text
zeta:   MU-BASEPOINT(L) is compatible with the existing ground-level data
        (E78.3: mu_N decreases rapidly toward 0 on the audited ladder);

plant:  MU-BASEPOINT(L) fails already at the endpoint level, because the same
        audited ladder tends toward an order-one negative floor
        (~ -1.74 at lambda=6), not toward 0.               (M-15)
```

So the reduction obeys the E77.6 falsifier-location rule: the planted build
breaks on the arithmetic/basepoint side of front B, not on a build-neutral LP
mechanism.

## 6. Probe

Companion files:

```text
E78_101_mu_dir_basepoint_probe.py
E78_101_mu_dir_basepoint_results.json
```

The probe evaluates `J_{L,N}(mu_N)-J_{L,N}(0)` directly and estimates the local
derivative size by symmetric finite differences around `t in {0, mu_N/2, mu_N}`
on the safe grid `sigma in {0.6,1,2}`.

### Zeta (`lambda=6`, `N=6,8,10,12`, `dps=50`)

```text
N= 6: |mu_N|=5.68e-23,  defect=1.48e-5,  sup|d_mu J|~8.41e5
N= 8: |mu_N|=3.68e-28,  defect=1.46e-8,  sup|d_mu J|~8.03e5
N=10: |mu_N|=8.93e-33,  defect=4.10e-7,  sup|d_mu J|~1.36e5
N=12: |mu_N|=2.40e-37,  defect=6.79e-7,  sup|d_mu J|~1.05e5              (M-16)
```

On the audited ladder the derivative stays finite on the local box while
`|mu_N|` collapses dramatically.  This does not prove `(M-11)`, but it is
consistent with the reduction `(M-13)`.

### Planted (`lambda=6`, `N=6,8`, `dps=40`)

```text
N= 6: |mu_N|=1.20e-1,  defect=4.12,  sup|d_mu J|~4.69e4
N= 8: |mu_N|=7.20e-1,  defect=3.38,  sup|d_mu J|~5.24e4.                  (M-17)
```

Here the local derivative remains finite on the audited boxes, but the path
length `|mu_N|` is order one.  This is exactly the failure mode predicted in
`(M-15)`: the planted break is at `MU-BASEPOINT`, not at the finite algebra.

## 7. Consequence for the front-B roadmap

After E78.100, the live fixed-`L` core had become

```text
SHELL-LOG + MU-DIR.                                        (M-18)
```

E78.100 autopsied the current shell route.  The present reduction shows that
the remaining directional term is now candidly smaller:

```text
MU-DIR
<= [mu_N -> 0 at the fixed basepoint]
 + [local paired derivative control near that basepoint].  (M-19)
```

So the next admissible front-B attack is no longer "prove MU-DIR directly", but
either:

```text
1. prove PAIRED-DMU-LOCAL from the exact formula (M-9), or
2. autopsy the exact paired denominator/coefficient that prevents (M-11), or
3. prove MU-BASEPOINT(L) in theorem-grade fixed-L form if that implication is
   not already available in the ledger beyond the audited lambda=6 ladder.      (M-20)
```

## 8. Status

```text
candidate closure - pending review

proved:
  the exact paired derivative formula (M-9) for partial_mu J_{L,N};

proved:
  MU-BASEPOINT(L) + PAIRED-DMU-LOCAL(L,K,eta) => MU-DIR(L,K);

reduced:
  the live directional front from a moving integral target to one scalar
  endpoint convergence statement plus one local paired derivative bound;

audited:
  zeta is consistent with small-path-length plus finite local derivative;
  the planted build fails at the endpoint/basepoint condition, as front B
  predicts;

next:
  attack PAIRED-DMU-LOCAL directly from (M-9), or autopsy the exact paired
  obstruction if the local derivative still hides a forbidden inverse-gap wall.
```
