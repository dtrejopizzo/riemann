# E78.109 - The crude spectral tail certificate for `A_N(0)^(-2) 1` is dead

**Scope:** front B only, live object `G0-RESOLVENT-SOURCE`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the naive route
"gap ratio + raw overlap with `1`" cannot certify the negligible tail of
`A_N(0)^(-2)1`; the exact failing coefficient is `|<v_0,1>|^(-1)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm used as a forcing theorem.
P76.061: respected. The argument stays at the paired finite-algebra level.
E72.16/E77.7az: respected. This is front B; planted failure is admissible here.
```

## 1. Starting point

E78.108 reduced the zeta-side live object to

```text
G0-RESOLVENT-SOURCE:
  control the ground scalar |<v_0,1>| / nu_0^2
  and prove the tail negligible in
  A_N(0)^(-2)1 = sum_j <v_j,1> / nu_j^2 v_j.                (T-1)
```

The first obvious attempt is to bound the tail by the first off-ground
eigenvalue.

## 2. Exact certificate

Write

```text
ground_N := <v_0,1> / nu_0^2 v_0,
tail_N   := sum_{j>=1} <v_j,1> / nu_j^2 v_j.               (T-2)
```

Since `{v_j}` is orthonormal,

```text
||tail_N||^2
 = sum_{j>=1} |<v_j,1>|^2 / nu_j^4
 <= nu_1^(-4) sum_{j>=1} |<v_j,1>|^2
 <= nu_1^(-4) ||1||^2.                                     (T-3)
```

Also

```text
||ground_N|| = |<v_0,1>| / nu_0^2.                         (T-4)
```

Therefore the exact ratio bound is

```text
||tail_N|| / ||ground_N||
 <= (sqrt(N) / |<v_0,1>|) * (nu_0/nu_1)^2.                 (T-5)
```

This is a correct certificate.  The question is whether it is useful.

## 3. Probe

Companion files:

```text
E78_109_groundmode_tail_gate_probe.py
E78_109_groundmode_tail_gate_results.json
```

The audited output is:

```text
BUILD zeta
N= 6: tail/ground = 2.71e-8,  certificate = 4.91e4
N= 8: tail/ground = 4.85e-9,  certificate = 2.49e6
N=10: tail/ground = 5.63e-9,  certificate = 6.43e8
N=12: tail/ground = 2.32e-9,  certificate = 8.12e10.       (T-6)

BUILD plant
N= 6: tail/ground = 2.72e74,  certificate = 7.87e49
N= 8: tail/ground = 1.75e31,  certificate = 2.36e0
N=10: tail/ground = 1.37e38,  certificate = 4.46e0
N=12: tail/ground = 2.76e44,  certificate = 7.69e0.        (T-7)
```

On the zeta ladder the actual tail is tiny, but the certificate explodes by
many orders of magnitude and never even becomes subunit.  The failure is not
the gap ratio alone: `nu_1/nu_0` is large on zeta.  The exact bad factor is

```text
|<v_0,1>|^(-1),                                                (T-8)
```

which is enormous on the audited zeta rows.

## 4. Autopsy

The route `(T-5)` is therefore dead as a forcing mechanism.

What fails is precise and theorem-grade:

```text
the crude tail certificate spends the entire l2 mass ||1|| on the off-ground
subspace, and divides by the tiny raw overlap |<v_0,1>|.                    (T-9)
```

That combination destroys the information discovered in E78.108.  The actual
small tail comes from structured cancellation inside the spectral coefficients,
not from a crude gap estimate against `||1||`.

So the route

```text
large gap ratio + raw overlap with 1  => negligible tail                     (T-10)
```

is false as an admissible strategy for `G0-RESOLVENT-SOURCE`.

## 5. Consequence

The next admissible live object must retain more structure than `(T-5)`.  In
particular, it must work with the off-ground component of the *first*
resolvent,

```text
(I-P_0) A_N(0)^(-1) 1,                                       (T-11)
```

or an equivalent paired coefficient package, instead of collapsing everything
to `||1||`.

That is strictly sharper than the dead certificate because it keeps the
resolvent-weighted geometry that `(T-5)` discards.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact tail certificate
  ||tail|| / ||ground|| <= (sqrt(N)/|<v0,1>|) * (nu0/nu1)^2;

autopsied:
  this certificate is useless on the audited zeta ladder because the exact bad
  factor is |<v0,1>|^(-1);

closed:
  the route "gap ratio + raw overlap with 1" as a proof mechanism for the tail
  in G0-RESOLVENT-SOURCE;

next:
  keep the resolvent-weighted off-ground component
  (I-P0)A_N(0)^(-1)1, or an equivalent paired package, as the new finite live
  object.
```
