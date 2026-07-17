# E73.222 - Linear functional form of the closed center

Date: 2026-07-14.

## 1. Purpose

E73.220--E73.221 isolate the remaining finite proof-facing task:

```text
wrap the closed scalar center C_a=A_L^digamma[B_a]-P_L[B_a]
by outward arithmetic.
```

This note rewrites that center as a finite linear functional of the packet
coefficients.  This avoids intervalizing the whole expression as an opaque
program.

## 2. Packet coordinates

For each Cauchy row `a`, write

```text
B_a(y)=sum_omega c_omega e^(i omega y)
      +y sum_omega l_omega e^(i omega y).
```

Then the closed center has the form

```text
C_a = sum_omega c_omega W_omega(L,lambda,R)
    + sum_omega l_omega V_omega(L,lambda,R)
    + E_exp(B_a;L,R).                              (1)
```

Here `R=80` in the current implementation.

## 3. Explicit weights

Let

```text
I_0(alpha,omega)=int_0^L exp((alpha+iomega)y)dy,
I_1(alpha,omega)=int_0^L y exp((alpha+iomega)y)dy.
```

The elementary archimedean weights are:

```text
W_omega^elem = I_0(1/2,omega)+I_0(-1/2,omega)
             - sum_{r<R} I_0(-(2r+1/2),omega)
             + 1/2(log4pi+gamma)
             + 1/2 log(tanh(L/2))
             + sum_{r<R} I_0(-(2r+1),0),

V_omega^elem = I_1(1/2,omega)+I_1(-1/2,omega)
             - sum_{r<R} I_1(-(2r+1/2),omega).
```

The signed digamma tail contributes:

```text
W_omega^tail = 1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
V_omega^tail = 1/4 psi_1(R+1/4-iomega/2),
```

plus exponentially small endpoint corrections already separated in
`E_exp`.

The prime weights are finite:

```text
W_omega^prime = sum_{p^k<=e^L} (log p)p^(-k/2) exp(iomega klog p),
V_omega^prime = sum_{p^k<=e^L} (log p)p^(-k/2) klog p exp(iomega klog p).
```

Thus:

```text
W_omega = W_omega^elem + W_omega^tail - W_omega^prime,
V_omega = V_omega^elem + V_omega^tail - V_omega^prime.
```

## 4. Outward radius target

If interval arithmetic gives

```text
c_omega in [c_omega],     l_omega in [l_omega],
W_omega in [W_omega],     V_omega in [V_omega],
E_exp in [E_exp],
```

then (1) gives the proof-facing scalar interval.  A sufficient radius is

```text
rad(C_a)
<= sum_omega |W_omega| rad(c_omega)
 + sum_omega |c_omega| rad(W_omega)
 + sum_omega rad(c_omega)rad(W_omega)
 + sum_omega |V_omega| rad(l_omega)
 + sum_omega |l_omega| rad(V_omega)
 + sum_omega rad(l_omega)rad(V_omega)
 + rad(E_exp).                                      (2)
```

This is the center analogue of E73.219.  The two remaining formal ingredients
are now explicit:

```text
1. coefficient balls for c_omega,l_omega from row and eta balls;
2. weight balls for W_omega,V_omega from elementary functions, finite primes,
   and psi/psi_1 Bernoulli tails.
```

## 5. Status

```text
proved: closed center is a finite linear coefficient functional;
derived: explicit outward radius formula (2);
next: implement the coefficient/weight radius audit.
```
