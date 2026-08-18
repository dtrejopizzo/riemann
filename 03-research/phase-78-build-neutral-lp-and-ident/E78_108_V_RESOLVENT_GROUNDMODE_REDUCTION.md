# E78.108 - On the zeta build, `V-RESOLVENT-SOURCE` reduces to the ground mode of `A_N(0)`

**Run:** 2026-07-19.  
**Scope:** front B only, live object `V-RESOLVENT-SOURCE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** on the zeta build,
the resolvent branch `A^{-1}v = A^{-2}1` is already exhausted by the ground
eigenmode of the inner block on the audited ladder; the planted build does not
share this feature, so the separation lands exactly where front B allows it.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator, no
       ambient inverse norm.
P76.061: respected. The reduction is written at the paired finite-algebra level.
E72.16/E77.7az: respected. This is front B; planted failure is admissible here.
```

## 1. Starting point

E78.107 reduced the live source to

```text
V-RESOLVENT-SOURCE(L,K,eta):
  control A^{-1}v cofinally enough to control y_b^(v).      (G-1)
```

At `mu=0`,

```text
v = A^{-1}1,
A^{-1}v = A^{-2}1.                                          (G-2)
```

Write the spectral resolution of the inner block:

```text
A_N(0) v_j^{(N)} = nu_j^{(N)} v_j^{(N)},
0 < nu_0^{(N)} <= nu_1^{(N)} <= ...                         (G-3)
```

Then

```text
A_N(0)^{-2} 1
 = sum_j <v_j^{(N)},1> / (nu_j^{(N)})^2  v_j^{(N)}.        (G-4)
```

The question is whether `(G-4)` is already ground-mode dominated on the zeta
side.

## 2. Probe

Companion files:

```text
E78_108_v_resolvent_groundmode_probe.py
E78_108_v_resolvent_groundmode_results.json
```

The audited data give:

```text
BUILD zeta
N= 6: ||A^-2 1|| = 7.38e30,  mode0 = 7.38e30,  proj0 = 1.0
N= 8: ||A^-2 1|| = 1.68e38,  mode0 = 1.68e38,  proj0 = 1.0
N=10: ||A^-2 1|| = 2.73e45,  mode0 = 2.73e45,  proj0 = 1.0
N=12: ||A^-2 1|| = 2.61e52,  mode0 = 2.61e52,  proj0 = 1.0.   (G-5)

BUILD plant
N= 6: ||A^-2 1|| = 1.03e28,  proj0 = 1.82e-51, proj01 = 1.85e-25
N= 8: ||A^-2 1|| = 3.10e32,  proj0 = 5.72e-32
N=10: ||A^-2 1|| = 8.23e37,  proj0 = 7.29e-39
N=12: ||A^-2 1|| = 7.17e43,  proj0 = 3.63e-45.               (G-6)
```

So on the audited zeta ladder:

```text
A^{-2}1 is numerically equal to its ground-mode projection to displayed scale,
while the planted build is not ground-mode dominated at all.               (G-7)
```

This is exactly the falsifier-location pattern front B allows.

## 3. Reduction

The audited zeta-side evidence `(G-5)` suggests the candid next zeta-side target
is the scalar ground coefficient

```text
G0-RESOLVENT(L):
  |<v_0^{(N)},1>| / (nu_0^{(N)})^2
```

together with a theorem-grade statement that the tail

```text
sum_{j>=1} <v_j^{(N)},1> / (nu_j^{(N)})^2  v_j^{(N)}        (G-8)
```

is negligible.

Thus, on the zeta side,

```text
ground-mode dominance + control of the scalar coefficient
=> V-RESOLVENT-SOURCE.                                      (G-9)
```

This is a genuine reduction because the predecessor asked for the entire vector
`A^{-2}1`, while the new target isolates one scalar coefficient plus one tail.

## 4. Consequence

For the zeta build, the next candid live object is no longer the full resolvent
vector but

```text
G0-RESOLVENT-SOURCE:
  control the ground scalar |<v_0,1>| / nu_0^2, and prove the tail negligible. (G-10)
```

For the planted build, this route is not admissible as a forcing mechanism; its
failure is exactly the front-B separation predicted by the mission rules.

## 5. Status

```text
candidate closure - pending review

proved:
  the exact spectral decomposition A^{-2}1 = sum_j <v_j,1> nu_j^{-2} v_j;

localized:
  on the audited zeta ladder the entire resolvent source is ground-mode
  dominated to displayed scale;

reduced:
  the zeta-side V-RESOLVENT-SOURCE to the scalar/tail target
  G0-RESOLVENT-SOURCE;

next:
  attack the zeta-side tail in (G-8), or autopsy the exact reason it does not
  admit a theorem-grade negligible-tail proof.
```
