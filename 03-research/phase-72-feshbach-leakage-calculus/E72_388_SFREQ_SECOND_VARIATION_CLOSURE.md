# E72.388 - SFREQ second-variation closure

## 1. Purpose

E72.386 shows that the physical-space FarWall term cannot be bounded by absolute prime-cell
variation.  E72.387 rewrites it as the signed high-frequency integral

```text
ErrWall_T(z)
=1/(2pi) int_{|tau|>T} \widehat g_z(-tau)P_{L,c}(tau)dtau.
```

This note proves that `SFREQ` follows from a second-variation estimate for the actual packet at the
natural height `T=e^L L^A`.

## 2. Endpoint structure

Recall

```text
g_z(t)=e^(ct)B_z^M(|t|)1_{|t|<=L}.
```

The finite packet satisfies

```text
B_z^M(L)=0.
```

Hence

```text
g_z(-L)=g_z(L)=0.                                     (1)
```

The function is continuous at `0`, but `g_z'` may have a jump there because of `|t|`.  This is harmless:
piecewise integration by parts on `[-L,0]` and `[0,L]` produces a `1/tau^2` coefficient containing the
jump of `g_z'` at `0` plus the variation of `g_z'`.

## 3. Second-variation Fourier bound

Let

```text
V_2(g_z):=Var_{[-L,0]}(g_z')+Var_{[0,L]}(g_z')+|g_z'(0+)-g_z'(0-)|.
```

Then for `tau != 0`,

```text
|\widehat g_z(tau)| <= V_2(g_z)/tau^2.                (2)
```

### Proof

Integrate by parts once on the two intervals.  The endpoint terms at `+-L` vanish by (1), and the two
terms at `0` cancel because `g_z` is continuous.  This gives

```text
\widehat g_z(tau)=1/(i tau) int_{[-L,0] union [0,L]} g_z'(t)e^(-itau t)dt.
```

Integrate by parts in the Stieltjes sense on each interval.  The total boundary contribution is the
jump `g_z'(0+)-g_z'(0-)`, and the remaining Stieltjes integrals are bounded by the variations of `g_z'`.
This proves (2). `QED`

## 4. Prime polynomial bound

Since `c>1/2`,

```text
|P_{L,c}(tau)|
<=sum_{n<=e^L} Lambda(n)n^(-1/2-c)
<=C_c.                                                (3)
```

Therefore

```text
|ErrWall_T(z)|
<= C_c/(2pi) int_{|tau|>T} V_2(g_z)/tau^2 dtau
<= C_c' V_2(g_z)/T.                                  (4)
```

This is an absolute frequency-tail bound, not an absolute prime-cell bound.  It is allowed because the
prime current has already been coupled into the single Dirichlet polynomial `P_{L,c}`.

## 5. Natural height closure

At natural height

```text
T=e^L L^A,
```

`SFREQ` follows from

```text
SV-K:
V_2(g_z) <= C_K e^((c+sigma_K)L)L^B.                  (5)
```

Indeed, if `c+sigma_K<1`, then (4)--(5) give

```text
|ErrWall_T(z)|
<= C_K e^((c+sigma_K-1)L)L^(B-A),
```

which is polynomial, in fact exponentially decaying up to powers of `L`.

## 6. Reduction of `SV-K` to packet estimates

On `(0,L)`,

```text
g_z'(t)=e^(ct)[cB_z^M(t)+(B_z^M)'(t)].
```

Thus

```text
Var_{[0,L]}(g_z')
<= C_c int_0^L e^(ct)(|B_z^M(t)|+|(B_z^M)'(t)|+|(B_z^M)''(t)|)dt
 + endpoint terms.                                    (6)
```

The negative interval has the same form with `e^(-ct)`, hence is dominated by the positive side.  The
jump at zero is controlled by `|B_z^M(0)|+|(B_z^M)'(0)|`, and E72.336 gives a rank-one formula for
`(B_z^M)'(0)`.

Therefore `SV-K` follows from the finite second-derivative packet gate:

```text
D2BV-K:
int_0^L e^(ct)(|B_z^M|+|(B_z^M)'|+|(B_z^M)''|)dt
<= C_K e^((c+sigma_K)L)L^B.                           (7)
```

## 7. Why this does not contradict the PACK-SMOOTH audit

The rejected `PACK-SMOOTH` tried to make total variation polynomial at fixed or polynomial contour
height.  Here the allowed size is

```text
e^((c+sigma_K)L)L^B,
```

and it is divided by the natural height `T=e^L L^A`.  The condition `c+sigma_K<1` converts that
exponential into decay.  Thus second variation is usable only after the right-wall/natural-height
architecture has been installed.

## 8. Status

```text
proved: SFREQ follows from SV-K at natural height;
reduced: SV-K to D2BV-K for the actual finite packet;
open: prove D2BV-K uniformly from the Dirichlet-Cauchy packet identities.
```
