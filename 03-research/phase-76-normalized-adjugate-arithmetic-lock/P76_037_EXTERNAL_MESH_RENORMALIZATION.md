# P76.037 - External mesh renormalization

The right boundary entire function cancels the sine poles on

```text
S_+={-N+1,...,N}.
```

Its reflection cancels `S_-={-N,...,N-1}`.  Therefore the bilateral
characteristic contains the following known, non-arithmetic sine zeros:

```text
k=+/-N:       multiplicity one;
|k|>=N+1:     multiplicity two,
rho_k=2*pi*k/L.
```

Their normalized even canonical product is `Z_ext,L,N`.  Define

```text
Psi_core,L,N(z)=Psi_L,N(z)/Z_ext,L,N(z).         (EM-1)
```

The quotient is an even polynomial, normalized at zero, whose zeros are
exactly the two finite boundary-numerator divisors.  They are all real by
P76.023.  Thus every canonical-product and Hurwitz argument of P76.031-
P76.034 applies to `Psi_core`.

On the safe axis the external logarithmic derivative is explicit:

```text
B_ext,L,N(sigma)
=2 sigma/rho_N^2+sum_{k>N}4 sigma/rho_k^2
=sigma L^2/(2*pi^2*N^2)
 +sigma L^2/pi^2 sum_{k>N}1/k^2.                (EM-2)
```

Hence

```text
d/dsigma log Psi_core(-i sigma)
=L coth(sigma L/2)+2 Re[iT_+'(i sigma)/T_+(i sigma)]
 -B_ext,L,N(sigma).                             (EM-3)
```

This removes the dominant `O(sigma L^2/N)` finite-section background before
comparison with `2 Xi'/Xi`.  It is a canonical mesh correction, not a fitted
background divisor.

The remaining core endpoint is

```text
CORE-SR-LOG:
d/dsigma log Psi_core,L,N(L)(-i sigma)
 ->2 Xi'(1/2+sigma)/Xi(1/2+sigma),              (EM-4)
```

locally uniformly for `sigma>1/2`.

For the uncorrected characteristic, `(EM-2)` tends to zero uniformly on
compact sigma intervals only under the stronger scaling

```text
N(L)/L^2 -> infinity.
```

For `Psi_core`, the natural horizon condition `N(L)/L -> infinity` is
sufficient to send `R=2*pi*N/L` to infinity.

Fixing `sigma_0>1/2` and normalizing `Psi_core` at `-i sigma_0` gives the
core safe-ratio characteristic.  The proof of P76.034 applies unchanged:
local convergence of its safe ratios to the corresponding ratios of
`Xi^2` implies Omega7.
