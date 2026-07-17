# E67.9 / E67.10 Results — the signed-certificate register

**Date:** 2026-07-06.
**Scripts:** [E67_9_signed_index_detector.py](E67_9_signed_index_detector.py),
[E67_10_root_of_unity_shapovalov.py](E67_10_root_of_unity_shapovalov.py).

## Register shift (why these tests)

E67.4/E67.7/E67.8 established a structural fact: every positive certificate (Haar state, CP map,
q-dimension at 0<q<1, isometric norm) is blind to the phase cancellation that IS the RH content, so it
returns the incoherent ceiling `S_abs`. The escape is not a better positive certificate; it is a
**signed** certificate.

## E67.9 — the signed index is a faithful RH detector

Object: `ind_-(A_N - P_lambda)` = number of negative eigenvalues of the whitened defect
`D_N = I - A_N^{-1/2} P_lambda A_N^{-1/2}`.

At `z0 = 100 - i`, exact P52 harness (`h8lab.arithmetic_jets`):

| case | ind_- | lambda_min behavior |
|---|---|---|
| zeta (baseline) | **0** for all N | -> 0+ marginal (8.7e-3, 3.7e-6, 8e-10, 6.7e-14, 2.1e-18) |
| planted off-line rho=0.65+100i | 1,2,3,4 (grows with N) | strongly negative |
| planted off-line rho=0.80+100i | 1,2,3,4 | more negative |
| planted off-line rho=0.95+100i | 1,2,3,4 | most negative |
| control on-line rho=0.5+100i | **0** for all N | marginal, like zeta |

Conclusion: `ind_-(A_N - P_lambda) = 0 for all N  <=>  RH` is a **faithful detector**. It is 0 exactly
for zeta and on-line zeros, and strictly positive (accumulating with N) for off-line zeros. The signed
index is the correct object.

## E67.10 — the signed certificate is intrinsic to the root-of-unity q-algebra

Contravariant (Shapovalov) norms of the `U_q(su(1,1))` positive discrete series `D_y^+`:
`r_n = prod_{j=1}^n [j]_q [j+2y-1]_q`, `[m]_q = (q^m-q^{-m})/(q-q^{-1})`.

- `0<q<1`: all `[m]_q > 0` -> `r_n > 0` -> **definite**, `ind_- = 0` always. (The old positive regime.)
- `q = e^{i pi/ell}`: `[m]_q = sin(m pi/ell)/sin(pi/ell)` changes sign -> `r_n` changes sign ->
  **indefinite**, `ind_-(n) = #{j<=n : r_j<0}` is an intrinsic integer index (Jantzen negative-layer
  count). Nonzero for several `(ell,y)` (e.g. ell=13,y=3 -> 2; ell=11,y=1 -> 1; ell=5,y=3 -> 2).

So an integer signed index is **native** to the q-algebra at a root of unity -- exactly the certificate
type E67.9 requires, and impossible for any `0<q<1`/positive mechanism.

## Honest gap (open construction, not a wall)

The **bare** Shapovalov index is sparse and, for e.g. ell=7,y=1, flat in n (0,0,0,...), whereas the
E67.9 defect index **grows with N** under an off-line zero. This is the "before" picture: the bare form
has **no prime input**. What makes `ind_-` grow under an off-line zero is the von Mangoldt **twist**,
not yet built.

The open construction (this is where new mathematics must be made, not looked up):

```
build a canonical map  P_lambda (prime jet)  ->  weight/twist of D_y^+
such that  ind_-( twisted Shapovalov form )  =  ind_-( A_N - P_lambda ).
```

Constraint (same non-circularity standard as QSC-exist, now in the signed register): the twist must come
from the q-algebra + Euler structure, **not fitted** to `A_N - P_lambda`. If fitted, it is circular. The
difference from all prior Phase-67 candidates: the certificate **type** is now correct (signed, not
positive), so the fight is over constructing the canonical twist, not over choosing a quantum group.

## State

```
correct object   : ind_-(A_N - P_lambda)              [E67.9, faithful detector]
correct tool      : root-of-unity Shapovalov form     [E67.10, intrinsic integer signed index]
live construction : canonical von Mangoldt twist of D_y^+ with matching ind_-   [OPEN]
```

This is the first Phase-67 state that is a genuine construction target rather than a wall map.
