# E78.102 - Ground-mode localization does not close `PAIRED-DMU-LOCAL`

**Run:** 2026-07-19.  
**Scope:** front B only, live object `PAIRED-DMU-LOCAL` from E78.101.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the obvious
spectral route to `PAIRED-DMU-LOCAL` is exhausted: the exact local derivative
contains a squared inner-gap denominator, while the available Cauchy/boundary
pairings suppress at most one gap power.  The missing power is the precise
obstruction.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target is introduced.
MW-2:  respected. The analysis stays in the fixed-L arithmetic front.
MW-3:  respected. No primewise assembly.
MW-4:  respected. This is an upper-bound autopsy, not a lower-bound/sign route.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. The obstruction is named through the exact paired spectral
       expansion; no determinant shortcut or Christoffel evaluator is used.
P76.061: respected. The autopsy is precisely about why the paired object still
         hides a dangerous denominator; it does not replace it by an ambient norm.
E72.16/E77.7az: respected. This is front B, so planted separation is admissible.
```

## 1. Starting point from E78.101

E78.101 reduced the live directional target to

```text
PAIRED-DMU-LOCAL(L,K,eta):
  sup_{N>=N_0} sup_{sigma in K} sup_{|t|<=eta}
    |partial_mu J_{L,N}(sigma;t)| <= C_{L,K,eta}.          (A-1)
```

with exact formula

```text
partial_mu J_{L,N}(sigma;mu)
 = 2 Re i[
     partial_mu T'_{L,N}(i sigma;mu) / T_{L,N}(i sigma;mu)
     - T'_{L,N}(i sigma;mu) partial_mu T_{L,N}(i sigma;mu)
       / T_{L,N}(i sigma;mu)^2
   ].                                                      (A-2)
```

The first natural attempt is to control `(A-2)` by the same low-mode
localization mechanism that was tested on the LP side: suppress the ground-mode
component of the paired resolvent.

## 2. Exact spectral expansion of the dangerous term

For the inner block `A_N(0)=H_{L,N}^{inner}` let

```text
A_N(0) v_j^{(N)} = nu_j^{(N)} v_j^{(N)},
0 < nu_0^{(N)} <= nu_1^{(N)} <= ...                         (A-3)
```

in the zeta build, where the fixed-L basepoint is `0`.

Then

```text
r_z^{in} A_N(0)^(-2) b_N
 = sum_j <r_z^{in},v_j^{(N)}> <v_j^{(N)},b_N> / (nu_j^{(N)})^2.   (A-4)
```

So any proof of `(A-1)` through ground-mode localization must first neutralize
the `j=0` term

```text
G_N(z)
 := <r_z^{in},v_0^{(N)}> <v_0^{(N)},b_N> / (nu_0^{(N)})^2.         (A-5)
```

This is the exact coefficient to audit.

## 3. What the existing ledger already gives

The closest prior mechanism is E77.7e.  There the paired double-resolvent route
needed only one power of the interlacing gap, and the data already showed:

```text
small overlap / one gap power is NOT enough for closure.            (A-6)
```

For `PAIRED-DMU-LOCAL`, the derivative route is strictly worse: `(A-5)` carries
**two** gap powers in the denominator.

Thus the only way the same mechanism could still work would be if the product

```text
|<r_z^{in},v_0^{(N)}>| |<v_0^{(N)},b_N>|                        (A-7)
```

were actually `O((nu_0^{(N)})^2)` uniformly on the safe compact.

## 4. Probe

Companion files:

```text
E78_102_paired_dmu_groundmode_probe.py
E78_102_paired_dmu_groundmode_results.json
```

The probe computes the ground-mode factor `(A-5)` directly on the audited safe
grid `sigma in {0.6,1,2}`.

### Zeta (`lambda=6`, `N=6,8,10,12`)

Representative values:

```text
N= 6, sigma=0.6:
  |<r,v0><v0,b>| / nu0      = 2.73e3
  |<r,v0><v0,b>| / nu0^2    = 3.68e23

N= 8, sigma=0.6:
  |<r,v0><v0,b>| / nu0      = 2.70e6
  |<r,v0><v0,b>| / nu0^2    = 2.37e31

N=10, sigma=0.6:
  |<r,v0><v0,b>| / nu0      = 5.43e6
  |<r,v0><v0,b>| / nu0^2    = 2.93e36

N=12, sigma=0.6:
  |<r,v0><v0,b>| / nu0      = 3.04e10
  |<r,v0><v0,b>| / nu0^2    = 7.07e44.                       (A-8)
```

The same blowup appears at `sigma=1` and `sigma=2`; only the constants change.

So the product `(A-7)` does **not** supply the extra gap power required by
`(A-5)`.  The ground-mode term explodes violently on the audited zeta ladder.

### Planted (`lambda=6`, `N=6,8`)

The planted build is not the obstruction here: its basepoint `0` is already the
wrong arithmetic point (E78.101), so front B is allowed to fail earlier.  The
present route is closed because it already fails on the zeta side.

## 5. Autopsy

The route

```text
ground-mode localization
=> bounded partial_mu T and partial_mu T'
=> PAIRED-DMU-LOCAL                                          (A-9)
```

is exhausted.

The precise obstruction is the missing extra power of `nu_0^{(N)}`:

```text
available from pairing:
  |<r_z,v_0>| |<v_0,b>| = o(1) and even very small numerically;

needed for the derivative route:
  |<r_z,v_0>| |<v_0,b>| = O((nu_0^{(N)})^2).                (A-10)
```

The probe shows the contrary.  Therefore no theorem-grade proof of
`PAIRED-DMU-LOCAL` can come from the already-tested low-mode localization
mechanism.

This is not a refutation of `PAIRED-DMU-LOCAL` itself.  It is a refutation of
one specific mechanism for proving it.

## 6. Consequence for the live front

After this autopsy, the only admissible next route to `PAIRED-DMU-LOCAL` is to
avoid the raw spectral expansion `(A-4)` and stay in the coupled finite algebra.

The honest next finite object is:

```text
DMU-COUPLED-GENERATOR:
  rewrite partial_mu T and partial_mu T' through the one-generator
  inhomogeneous Loewner package of P76.042 / P76.041, and determine whether the
  local derivative bound closes there or whether a new exact denominator
  obstruction appears.                                      (A-11)
```

In other words: do not chase `A_N(0)^(-2)` by spectral projection anymore; push
`partial_mu` through the coupled generator identity first.

## 7. Status

```text
candidate closure - pending review

proved:
  the exact dangerous coefficient for the spectral derivative route is the
  ground-mode term (A-5);

refuted:
  the ground-mode localization mechanism as a route to PAIRED-DMU-LOCAL;

identified:
  the exact obstruction is the missing extra factor of nu_0^{(N)} in the paired
  product |<r,v0><v0,b>|;

live:
  PAIRED-DMU-LOCAL remains open;

next:
  attack the coupled-generator derivative route (A-11), or autopsy its exact
  denominator if that route also collapses.
```
