# E72.293 -- Analytic lemma stack for the corrected compact-root route

**Purpose.** Stop the numerical loop and isolate the analytic theorem stack that is now load-bearing.
The point of this note is not to add another diagnostic. It rewrites E72.274--E72.292 as a proof
pipeline: what is already an identity, what follows from explicit analytic estimates, and what remains
as a genuine theorem.

## 1. Compact-root HPAC theorem

Fix a compact Cauchy set `K subset C \ R` and a finite height `H`. Let

```text
L       = log x,
e_pole  = lambda_0(H_model|odd),
C_E     = B_even^T(H_actual-e_pole I)B_even,
mu_x    = lambda_min(C_E),
a_s     = B_even^T k_s,
```

and let `a_s^perp` denote the left actual-ground gauge from E72.275. For each finite Weyl root
`tau_j <= H`, define

```text
S_tau = (tau I-D)^(-1) + (-tau I-D)^(-1).
```

The corrected finite-root source identity is

```text
A_x(tau_j)xi_x = 2xi_x + i(1/2+i tau_j)S_tau_j xi_x.
```

The left gauge kills the `2xi_x` term. Thus the load-bearing compact-root scalar is

```text
R_x(s,tau_j)
 = <a_s^perp, C_E^(-1) S_tau_j xi_x>.
```

### Theorem 293.1

Assume, uniformly for `s in K` and `tau_j <= H`,

```text
GAP:   mu_x >= c L^2,
DCB:   ||[C_E,S_tau_j]xi|| = O_H(L^alpha) for some alpha<7/2,
SIZE:  ||a_s^perp|| <= C_K L^(1/2).
```

Then

```text
sup_{s in K, tau_j <= H} |R_x(s,tau_j)| = O_{K,H}(L^(-1/2)).
```

In particular the fixed-height compact-root HPAC residual vanishes.

### Proof

Use the inverse-collapse identity of E72.277:

```text
<a,C_E^(-1)S_tau xi>
 = mu_x^(-1)<a,S_tau xi>
   - mu_x^(-1)<a,C_E^(-1)[C_E,S_tau]xi>.
```

For the first term, E72.278 gives the exact Cauchy-factor identity

```text
<a_s^perp,S_tau xi>
 = z M_x(z)( -2tau/(z^2-tau^2) - V_x(tau) ),
```

where `z` stays in the fixed compact set and

```text
M_x(z)/mu_x = O_K(L^(-3/2)).
```

The rational factor is `O_{K,H}(1)`. By E72.282,

```text
||S_tau xi|| = O_H(L),
```

hence `|V_x(tau)|=|<xi,S_tau xi>| <= O_H(L)`. Therefore the diagonal contribution is

```text
O_K(L^(-3/2)) * O_H(L) = O_{K,H}(L^(-1/2)).
```

For the commutator term, use the directional commutator bound:

```text
||[C_E,S_tau]xi|| = O_H(L^alpha),      alpha<7/2.
```

Thus

```text
mu_x^(-1) |<a,C_E^(-1)[C_E,S_tau]xi>|
 <= mu_x^(-1)||a|| ||C_E^(-1)|| ||[C_E,S_tau]xi||
 = O(L^(-2)) O_K(L^(1/2)) O(L^(-2)) O_H(L^alpha)
 = O_{K,H}(L^(alpha-7/2)) = o(1).
```

This proves the theorem. No zero of zeta is used; the inputs are the pole-even gap, the source-local
commutator bound, and the exact corrected source/gauge identities.

## 2. Why the old upper complement theorem is retired

E72.295 proves that global APCB is false asymptotically: high Fourier diagonal modes give

```text
lambda_max(Delta_arith)_+ >= c e^(L/2)/L
```

for fixed high mesh frequency. Therefore the previous route

```text
MUCB + APCB => ||C_E||=O(L^2)
```

cannot be load-bearing. It controlled the entire complement, including high Fourier modes that the
compact-root HPAC source does not need.

The replacement is E72.296:

```text
DCB:
sup_{tau_j<=H} ||[C_E,S_tau_j]xi|| = O_H(L^alpha), alpha<7/2.
```

This is source-local and is exactly the vector estimate used by the inverse-collapse proof.

## 3. APCB status

E72.285 gives the exact arithmetic autocorrelation form

```text
Delta_arith = - sum_{n <= exp(L)} Lambda(n)n^(-1/2) Q_{log n},
```

with

```text
<v,Q_yv> = 2 Re int_0^(L-y) f_v(t+y) overline(f_v(t)) dt.
```

Let the even complement be split by mesh frequency into

```text
E_low  = {|d|<4},
E_high = {|d|>=4},
Delta_arith = [[A,B],[B*,D]].
```

Then the block inequality is

```text
lambda_max(Delta_arith)_+
 <= lambda_max(A)_+ + ||B|| + lambda_max(D)_+.
```

The old APCB program tried to prove the following three estimates:

```text
LOW-FIN(C0):   lambda_max(A)_+ <= C0 L^2,
H-GERSH(C1):   sup_i sum_j |D_ij| <= C1 L^2,
CROSS-HS(C2):  ||B||_HS <= C2 L^2.
```

Indeed, Gershgorin gives `lambda_max(D)_+ <= sup_i sum_j |D_ij|`, and `||B|| <= ||B||_HS`.
E72.295 shows this cannot be the final asymptotic route in the full complement. These estimates may
remain useful as finite-window diagnostics or after an additional source projection, but not as a
global upper-complement theorem.

## 4. The next analytic target: DCB

The exact commutator formula is

```text
([Q_y,S_tau]xi)_m
= sum_j Q_y(m,j)(s_j(tau)-s_m(tau))xi_j.
```

E72.298 gives the corresponding double-commutator identity:

```text
<S_tau xi,(C_E-mu I)S_tau xi>
= -1/2 sum_{m,n} xi_m xi_n (s_m-s_n)^2 C_E(m,n),
```

and the direct square form

```text
||[C_E,S_tau]xi||^2
= sum_m |sum_n C_E(m,n)(s_n-s_m)xi_n|^2.
```

The difference factor is the new smoothing. Since

```text
s_j(tau)=2d_j/(tau^2-d_j^2),
```

one has, away from the finite pole neighborhood,

```text
|s_j-s_m| <= C_H |d_j-d_m|/((1+|d_j|)^2(1+|d_m|)^2).
```

This cancels the `1/(j-m)` singularity in `Q_y(m,j)` after using `d_j-d_m=2pi(j-m)/L`. The next proof
must exploit this commutator gain before any absolute values are taken.

## 5. What remains open

The route to scalar WRL is now:

```text
GAP + VBG + DCB + corrected source/gauge
=> compact-root HPAC residual vanishes.
```

The still-open mathematical statements are:

```text
1. GAP lower theorem:
   lambda_0(H_model|even)-lambda_0(H_model|odd) >= c L^2.

2. Directional commutator bound DCB:
   sup_{tau_j<=H} ||[C_E,S_tau_j]xi|| = O_H(L^alpha), alpha<7/2.

3. DCB energy package:
   FORM-DCB in double-commutator form, or preferably DCB-square <= C_H L^6.

4. Source theorem:
   the corrected left-gauged HPAC source is exactly the load-bearing scalar WRL source.

5. High-root tail:
   the compact-root theorem extends from tau_j <= H to the full root window in the final order of
   limits.

6. Bordered-minor divisibility:
   the corrected bordered minor supplies the Mellin spectral divisibility needed for scalar WRL.

7. Transport:
   CGE-K, ROP, and MSB with the final quantifier order.
```

Everything else in E72.274--E72.292 is now either an exact identity or a conditional theorem recorded
above.

## 6. Quantifier order

The final theorem must be stated with the limits frozen as:

```text
for every compact K subset C\R, every root-height T, and every epsilon>0
there exists H0
such that for H>=H0 there exists x0=x0(K,T,H,epsilon)
such that for x>=x0 the compact-root bound, high-root tail, and transport bounds hold together.
```

The fixed-height compact-root estimate above supplies the inner theorem. The high-root tail and
transport gates must justify the passage from fixed `H` to the full scalar WRL concomitant.

## 7. Immediate decision

Do not run another broad spectral probe for APCB. The next work item is:

```text
prove the directional commutator estimate E72.296:
insert s_j-s_m first, use the double-commutator identity E72.298,
then prove FORM-DCB via `ARCH-FORM + MSD-FORM` from E72.301--E72.302 or the stronger DCB-square
inequality.
```

If DCB succeeds, compact-root HPAC no longer needs any global upper complement theorem.
