# E72.387 - SignedFar frequency certificate

## 1. Purpose

E72.386 proves that FarWall cannot be estimated by absolute prime-cell variation.  This note gives the
correct signed certificate: the wall error is a high-frequency tail of the actual compact packet
against one finite Dirichlet polynomial.

## 2. Finite measure and Dirichlet polynomial

Define the finite weighted prime measure

```text
dmu_{L,c}(u)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c) delta_{log n}(u),
```

and its Fourier transform

```text
P_{L,c}(tau)
:=int e^(-itau u)dmu_{L,c}(u)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c-itau).              (1)
```

For the wall-gauged packet

```text
g_z(t)=e^(ct)B_z^M(|t|)1_{|t|<=L},
```

write

```text
\widehat g_z(tau)=int_{-L}^{L}g_z(t)e^(-itau t)dt.    (2)
```

## 3. Exact frequency identity

The full finite-height wall quadrature is

```text
PrimeWall_T(z)=<g_z,D_T*dmu_{L,c}>,
```

where `D_T` is the symmetric Fourier cutoff kernel.  The infinite-height wall term is

```text
PrimeWall_infty(z)=<g_z,dmu_{L,c}>.
```

Therefore

```text
ErrWall_T(z)
=PrimeWall_T(z)-PrimeWall_infty(z)
=1/(2pi) int_{|tau|>T} \widehat g_z(-tau) P_{L,c}(tau)dtau,    (3)
```

with the standard symmetric cutoff convention.

### Proof

Fourier inversion gives

```text
D_T*dmu
```

as the projection of `dmu` onto frequencies `|tau|<=T`.  Pairing with `g_z`,

```text
<g_z,D_T*dmu>
=1/(2pi)int_{|tau|<=T}\widehat g_z(-tau)P_{L,c}(tau)dtau.
```

Similarly,

```text
<g_z,dmu>
=1/(2pi)int_R \widehat g_z(-tau)P_{L,c}(tau)dtau,
```

in the tempered distribution sense.  Subtracting gives (3). `QED`

## 4. Finite certificate form

For a computational certificate choose a finite high-frequency cutoff `U>T`:

```text
ErrWall_T(z)
=1/(2pi) int_{T<|tau|<=U} \widehat g_z(-tau)P_{L,c}(tau)dtau
 + Tail_U(z).                                         (4)
```

If `g_z` is piecewise `q` times absolutely continuous and endpoint jumps are treated explicitly, then
integration by parts gives

```text
|\widehat g_z(tau)| <= C_q(z,L)|tau|^(-q).
```

Since

```text
|P_{L,c}(tau)| <= sum_{n<=e^L} Lambda(n)n^(-1/2-c) <= C_c,
```

for `c>1/2`, the outer tail satisfies

```text
|Tail_U(z)| <= C_{q,c}(z,L) U^(1-q).                  (5)
```

Thus `SignedFar` is reduced to:

```text
finite oscillatory integral over T<|tau|<=U
+ explicit integration-by-parts tail.
```

No zero divisor and no prime-cell absolute ceiling appears.

## 5. Proof-facing target

The remaining theorem can be stated as:

```text
SFREQ:
For T=e^L L^A and suitable U=U(L),
|int_{T<|tau|<=U} \widehat g_z(-tau)P_{L,c}(tau)dtau|
+ |Tail_U(z)|
<= C_K L^B.
```

This is the sharp finite-frequency form of SignedFar.

## 6. Status

```text
proved: exact high-frequency identity for SignedFar;
proved: finite cutoff plus explicit tail certificate;
reduced: FarWall to SFREQ, a finite oscillatory integral involving only B_z^M and Lambda(n) for n<=e^L;
open: prove SFREQ uniformly for the actual Feshbach packet.
```
