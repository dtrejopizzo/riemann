# E101.024 - First Stieltjes sign and positive-kernel wall

## 1. Riemann kernel representation

Let

```text
F(sigma)=Xi(1/2+sigma).                               (1.1)
```

The classical Riemann-kernel formula has the form

```text
F(sigma)=integral_0^infinity Phi(t)cosh(sigma t)dt,  (1.2)
```

up to a fixed positive normalization, with

```text
Phi(t)>0.                                            (1.3)
```

For `sigma>0`, differentiation under the integral gives

```text
F'(sigma)
 =integral_0^infinity t Phi(t)sinh(sigma t)dt>0.     (1.4)
```

Consequently the arithmetic Stieltjes candidate satisfies

```text
g_Xi(x)
 =F'(sqrt(x))/[sqrt(x)F(sqrt(x))]>0,
x>0.                                                 (1.5)
```

Thus the zeroth sign in the hierarchy

```text
(-1)^k g_Xi^(k)(x)>=0                                (1.6)
```

is closed unconditionally.

## 2. Positivity of the kernel does not give the next sign

Consider the positive even measure

```text
d eta
 =(1/10)delta_2+delta_(1/2),                         (2.1)
```

and its positive cosh transform

```text
f(sigma)
 =(1/10)cosh(2sigma)+cosh(sigma/2).                  (2.2)
```

Set

```text
g_f(x)=f'(sqrt(x))/[sqrt(x)f(sqrt(x))].              (2.3)
```

If

```text
A_(2m)=integral t^(2m)d eta(t),                      (2.4)
```

then Taylor expansion at `x=0` gives

```text
g_f'(0)
 ={A_0 A_4-3A_2^2}/{6A_0^2}.                        (2.5)
```

For (2.1),

```text
A_0=11/10,
A_2=13/20,
A_4=133/80,                                         (2.6)
```

and therefore

```text
A_0A_4-3A_2^2=449/800,
g_f'(0)=449/5808>0.                                 (2.7)
```

A Stieltjes function must satisfy `g'(x)<=0`.  Hence a strictly positive
cosh kernel does not imply even the first derivative sign.  Replacing the two
point masses by narrow positive smooth bumps preserves the strict inequality,
so the obstruction is not distributional.

## 3. Consequence for the route

The Riemann-kernel positivity proves only (1.5).  Any proof of the remaining
Stieltjes hierarchy must use structure beyond positivity of `Phi`, such as the
complete Gamma--prime determinant identification.  Attempting to derive
`STIELTJES-IDENT` from `Phi>0` alone is therefore closed as insufficient.

## 4. Status

```text
proved:
  unconditional positivity of g_Xi on the safe axis;
  exact positive-kernel counterexample to the derivative sign;

closed as insufficient:
  derivation of the Stieltjes hierarchy from Riemann-kernel positivity alone;

open:
  the higher Stieltjes signs and the full identification theorem.
```

