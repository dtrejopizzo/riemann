# P76.011 - Exact Loewner interpolation identity

## Scalar symbols

Let `W_L` denote the finite CCM Weil functional, including the coupled
archimedean and prime-power terms.  Define the zero-independent entire
symbols

```text
S_L(t)=W_L[y -> sin(ty)],
C_L(t)=W_L[y -> cos(ty)].
```

On the Fourier mesh `d_n=2 pi n/L`, define the Loewner matrix

```text
Loew(S)_{mn}=(S(d_m)-S(d_n))/(d_m-d_n),  m != n,
Loew(S)_{nn}=S'(d_n).
```

## Exact matrix decomposition

The CCM cells satisfy

```text
q_mn(y)
=(sin(d_m y)-sin(d_n y))/(pi(n-m)),       m != n,

q_nn(y)=2(1-y/L)cos(d_n y).
```

Since `d_n-d_m=2 pi(n-m)/L`, linearity of `W_L` gives

```text
H_L=2 diag(C_L(d_n))-(2/L)Loew(S_L).       (LI-1)
```

This identity keeps Gamma and prime terms coupled inside `S_L,C_L`; it does
not estimate either sector separately.

## Rational interpolation identity

Let

```text
H_L xi=mu xi,
c(z)=sum_n xi_n/(z-d_n),
m_S(z)=sum_n S_L(d_n)xi_n/(z-d_n),
R_S(z)=S_L(z)c(z)-m_S(z).
```

The residues of the two terms in `R_S` cancel at every mesh point, so `R_S`
is analytic at each `d_n`.  Taking the removable value gives

```text
R_S(d_n)
=S_L'(d_n)xi_n
 sum_{m != n}(S_L(d_n)-S_L(d_m))xi_m/(d_n-d_m)
=(Loew(S_L)xi)_n.                            (LI-2)
```

Combining `(LI-1)` with the eigenline equation yields the exact nodal law

```text
R_S(d_n)=L(C_L(d_n)-mu/2)xi_n.               (LI-3)
```

Let `I_xi` be the polynomial Lagrange interpolant on the mesh:

```text
I_xi(d_n)=xi_n,
I_xi(z)=sum_n xi_n D(z)/(D'(d_n)(z-d_n)),
D(z)=prod_n(z-d_n).
```

Then the entire interpolation residual

```text
E_L(z)=R_S(z)-L(C_L(z)-mu/2)I_xi(z)
```

vanishes at every mesh point:

```text
E_L(d_n)=0,
E_L(z)=D(z)G_L(z)                             (LI-4)
```

for an entire function `G_L`.  Equivalently, after writing
`c=P/D` and `m_S=P_S/D`,

```text
S_L(z)P(z)-P_S(z)
=L(C_L(z)-mu/2)D(z)I_xi(z)+D(z)^2G_L(z).     (LI-5)
```

There is a more canonical remainder for contour estimates.  Interpolate the
nodal values of `R_S` directly:

```text
I_R(z)
=sum_n L(C_L(d_n)-mu/2)xi_n
       D(z)/(D'(d_n)(z-d_n)).
```

Then

```text
R_S(z)-I_R(z)=D(z)G_L^can(z),                 (LI-6)
```

and, on every contour enclosing the mesh and `z`, the standard interpolation
remainder is

```text
G_L^can(z)
=(1/(2 pi i)) int
 R_S(zeta)/(D(zeta)(zeta-z)) dzeta.           (LI-7)
```

The product residual in `(LI-4)` and the canonical residual differ by the
explicit entire function

```text
[I_R(z)-L(C_L(z)-mu/2)I_xi(z)]/D(z).
```

## Why this is a new useful object

`LI-4` is not a projection, quotient, pseudoinverse, or fitted residual.  It
is fixed from the scalar finite Euler/Gamma symbols and the eigenline
equation.  It converts the matrix problem into a rational Hermite
interpolation problem.

The remaining theorem is now a remainder estimate for this interpolation:

```text
LOEWNER-REM:
control G_L(gamma), I_xi(gamma), and P_S(gamma)
in the exact identity (LI-5),
```

with `B_L` controlled and the formula fixed away from zeros.  If the exact
interpolation remainder is merely rewritten as `EG_LOCK`, this route closes
as another equivalence.  If compact support gives an independent contour
formula for `E_L`, it can directly force `c(gamma)` without dividing by the
collapsing spectral gap.
