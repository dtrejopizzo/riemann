# P76.030 - Bilateral boundary characteristic

## Exact reflection

Let `J` reverse the Fourier indices.  The CCM entries satisfy

```text
J H_{L,N} J=H_{L,N}
```

because the cell functions obey `q_{-m,-n}=q_{m,n}`.  The inner Schur block
is centrosymmetric and the two boundary columns are exchanged by `J`.
Consequently their canonical null vectors are reflected and

```text
T_-(z)=-T_+(-z).
```

After multiplication by the sine factor and canonical normalization,

```text
Phi_-(z)=Phi_+(-z).                              (BB-1)
```

## Bilateral characteristic

Define

```text
Psi_{L,N}(z)=Phi_+(z)Phi_-(z)
             =Phi_+(z)Phi_+(-z).                 (BB-2)
```

Then `Psi(0)=1`, `Psi` is even, and every zero of `Psi` is real by P76.023.
No averaging is used: its divisor is the union of the two real boundary
divisors, so real-rootedness is preserved exactly.

## Closure theorem

If along a path with `N(L)/L -> infinity`,

```text
Psi_{L,N(L)}(z)
 -> [Xi(1/2+iz)/Xi(1/2)]^2
```

locally uniformly on the centered strip, then Omega7 follows.  Indeed an
off-line zero of `Xi` is an off-real zero of `Xi^2`, while every finite
approximant has only real zeros; Hurwitz gives a contradiction.

The weak exponential theorem P76.029 applies verbatim to `Psi`.  In Fourier
space its density is the convolution of the right density with its
reflection.  Thus weighted total variation is bounded by the product of the
two one-sided weighted variations, while the odd component vanishes
identically.

## Advantage

The unilateral characteristic had a numerically decreasing but nonzero odd
defect.  `(BB-2)` removes that defect algebraically, retains the arithmetic
Schur construction and finite real-rootedness, and changes only the target
from normalized `Xi` to its square.  No square root or choice of phase is
required.
