# R161_016 — Markov pullback and the direction of the canonical Hardy norm

## 0. Verdict

The Euler--Gamma Markov defect and the canonical product-Hardy norm have now been compared with their arrows kept
explicit.  The direct, or ``same-port'', identification gives

```
N_T(0)-N_T(delta) >= 0,
```

which is exactly the already proved causal monotonicity and has the **wrong direction** for closure.  Thus ambient
contractivity alone cannot prove the first-contact minimum theorem of `R161_015`.

To close D, the additive Poisson/Fourier factor must do more than manufacture the product amplitude: it must provide
an order-zero, source-labelled scattering which reverses the physical input/output identification before the
positive Markov defect is pulled back.  The required finite-difference identity is

```
N_T(delta)-N_T(0) = Q_(T,delta)(F)+o(delta),
Q_(T,delta)(F) >= 0,                                             (0.1)
```

on a primitive first-contact state.  Dividing by `delta` and using `R161_015` then forces the product port to vanish.

The finite Poisson defect `E_N^ren` does not by itself supply this scattering: it tends to zero, whereas the required
order-zero map must carry one nonzero physical port to the other.  This is an exact collision with the open physical
intertwining `(220j)/(223j)` of phase 116, not a proof of it.

## 1. The sign forced by a direct contraction

Let `g` be the canonical right product port and

```
g_delta(t)=exp(-delta(t-T))g(t),
N_T(delta)=||g_delta||_2^2.                                     (1.1)
```

Suppose a family of contractions `M_delta:K_0 -> K_delta` and isometric physical embeddings `E_delta` realise the
port in the direct orientation,

```
M_delta E_0 g = E_delta g_delta.                                (1.2)
```

Then contractivity gives

```
N_T(0)-N_T(delta)
 =||E_0g||^2-||M_delta E_0g||^2 >=0.                             (1.3)
```

Moreover, if the contraction has its canonical Julia defect `D_delta=(I-M_delta^*M_delta)^(1/2)`, then

```
N_T(0)-N_T(delta)=||D_delta E_0g||^2.                            (1.4)
```

By the exact slope formula of `R161_015`,

```
lim_(delta downarrow 0) [N_T(0)-N_T(delta)]/delta
 = E_T^PC(F) >=0.                                                (1.5)
```

Thus (1.2) recovers Sonin--Gamma coercivity; it cannot give the opposite inequality `E_T^PC(F)<=0`.

**Proposition 1.1 (arrow obstruction; PROVED).** Any use of the positive Euler--Gamma Markov defect which identifies
its domain with the critical canonical port and its codomain with the right-shifted canonical port proves only the
already known inequality `N_T'(0+)<=0`.  A closing pullback must exchange the physical input/output identifications
or produce an additional signed terminal cancellation.

*Proof.* Equations (1.3)--(1.5).  No arithmetic hypothesis enters.  In particular first contact cannot change this
conclusion unless it is used in the physical intertwining itself. ∎

## 2. What the closing arrow must say

For a contraction, a positive defect always has the form ``input norm minus output norm''.  Therefore (0.1) requires
the reverse physical typing

```
input metric  = N_T(delta),
output metric = N_T(0),                                          (2.1)
```

after the order-zero scattering and all Gamma/Tate terminals have been connected.  Equivalently, an admissible
construction must give, on the first-contact radical,

```
N_T(delta)-N_T(0)
 = ||D_(E Gamma,delta) E_(T,delta)^phys F||^2
   + R_(T,delta)(F),                                             (2.2)
```

where `liminf R_(T,delta)(F)/delta>=0`.  It is enough to have (2.2) to first order.  Neither side may be *defined*
from the other.

Combining (2.2) with (1.5) gives

```
-E_T^PC(F)>=0.
```

Since `E_T^PC(F)>=0`, the excess is zero, `g=0`, and the critical-jet/Cartwright argument gives `F=0`.

This proves the following precise conditional statement.

**Theorem 2.1 (reverse-pullback closure criterion; PROVED CONDITIONALLY).** A source construction of (2.2), with the
right side obtained from the finite Euler--Gamma contractions and the Poisson/Fourier scattering before imposing row
D, closes first contact and hence row D.

The conditional clause is exactly the construction of (2.2), not any subsequent analytic estimate.

## 3. Why the finite Poisson defect is not yet the scattering

The renormalised finite Poisson defect is

```
E_N^ren=S_N^ren Fcal-JS_N^ren.                                  (3.1)
```

On Schwartz data, `R161_003` proves

```
E_N^ren F -> 0.                                                  (3.2)
```

Consequently a bounded strong limit of maps built linearly from `E_N^ren` has zero order-zero action.  In contrast,
the required scattering has to take the physical minus-delay observation to the distinct plus-delay observation.
For an active shift `a<2T`, their Grams differ by

```
J_(a,+)^*J_(a,+)-J_(a,-)^*J_(a,-)=S_a+S_(-a) !=0.                (3.3)
```

It follows that the disappearing defect (3.1) cannot itself be the required order-zero map.  Rescaling it so that a
nonzero limit survives would require a new uniform graph estimate and a proof that the limit has the reverse metric
typing (2.1); neither follows from `(PC-ren)`.

This does not make `(PC)` irrelevant.  Its role is to build the compensated, source-labelled synthesis through which
the Markov innovation must pass.  What (3.2) excludes is the shortcut

```
Poisson defect = missing scattering.                             (3.4)
```

## 4. Coherent product port versus labelled Markov ports

There is a second typing issue.  The Euler Markov defect is an orthogonal family indexed by prime powers,

```
{d_(n,delta) J_(log n,-)F}_n,                                   (4.1)
```

whereas multiplication by zeta and the Poisson anomaly synthesize those labels into one scalar Hardy port.  Taking
the norm before synthesis gives a diagonal sum; taking it after synthesis introduces all cross-prime terms.  These
two operations are not interchangeable.

The corpus already proves that the unsynthesised exterior family has divergent energy.  Hence the labels cannot be
completed orthogonally and only later summed.  Tate centering and cross-prime synthesis must occur **before** the
exterior norm is taken.  The phase-161 product port performs the needed scalar synthesis, but `(PC)` is a linear
amplitude identity; it has not yet proved that this synthesis is a bounded metric map from (4.1), much less that its
metric has the reversed orientation (2.1).

Thus the exact remaining map is

```
prime Julia innovations
  -- Tate-centred Poisson/Chebyshev synthesis --> product Hardy port
  -- cosine/Gamma scattering --> reverse physical port.          (4.2)
```

Its amplitude and its polar coefficients are known (`R161_007`--`R161_009`).  Its norm derivative is known
(`R161_015`).  Boundedness, isometric terminal bookkeeping and the reverse arrow are the unproved content.

## 5. The first collar is finite, but the norm slope is not

For

```
0.8<T<(log 5)/2,
```

only `n=2,3,4` occur in the endpoint collar.  Let

```
Y_3(F)
 =(log2)/sqrt2 tau_(log2)F
 +(log3)/sqrt3 tau_(log3)F
 +(log2)/2     tau_(log4)F.                                    (5.1)
```

It is tempting to conclude that the first instance of (2.2) is a finite `2,3,4` scattering matrix.  That conclusion
is false.  Formula (5.1) describes only `T<t<T+eta`.  For arbitrarily large exterior `t`, the causal Chebyshev current
contains prime powers with `log n` near `t+[-T,T]`; hence infinitely many labels enter the complete product port.
The norm slope is

```
-N_T'(0+)=2 integral_T^infinity (t-T)|g(t)|^2dt,                 (5.2)
```

so it is not determined by the first collar; indeed the weight in (5.2) vanishes at the endpoint.  A finite matrix
with only the `2,3,4` channels can at most prove a **local collar statement**, not the global reverse-pullback
identity.

There are therefore two distinct admissible continuations:

1. **Local route.**  Couple the finite `2,3,4` collar to the four-state Gamma head and the crossed Tate terminals and
   prove `Y_3(F)=0` on a nonempty interval.  Then use the existing gap-enlargement theorem.  No assertion about the
   global norm slope is needed.
2. **Global route.**  Prove (2.2) using the complete, infinite, Tate-centred cross-prime synthesis.  The phase-116
   divergence theorem forbids taking the prime innovations as an orthogonal exterior sum before that synthesis.

On a primitive first-contact state the Tate terminals in the local route are fixed by the crossed collar system and
the interior Gamma trace is fixed by `R161_013`.  Its load-bearing test is a zero-collar identity, not a finite
replacement for (5.2).

## 6. Status

- direct Markov pullback gives the wrong/automatic norm direction: **PROVED**;
- necessity of reverse input/output typing for closure: **PROVED**;
- `E_N^ren` alone cannot be the order-zero scattering: **PROVED in the bounded strong-limit class**;
- coherent/orthogonal exterior completion cannot be interchanged: **PROVED by the phase-116 divergence theorem**;
- finite `2,3,4` data control only the first collar, not the global norm slope: **PROVED**;
- reverse pullback identity (2.2), requiring complete Tate-centred synthesis: **OPEN**;
- finite Gamma/Tate collar identity forcing `Y_3(F)=0`: **OPEN (alternative local route)**;
- row D: **OPEN**.

The next step is a clean choice of scale: either write the finite `2,3,4` plus Gamma/Tate matrix to force a zero
collar, or construct the full compensated synthesis to prove the global reverse pullback.  A finite matrix cannot
stand in for the latter.
