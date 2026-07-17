# E72.278 -- Cauchy-factor identity

**Purpose.** Factor the diagonal term from E72.277 into explicit scalar rational sums.

The compact-root residual after the corrected pole-even gauge is reduced to

```text
R_x(s,tau_j)
= i alpha(tau_j)mu_x^(-1)<a_s^perp,S_tau_j xi_x>
  + commutator term.
```

E72.277 shows that the commutator term is the separate invisible channel.  This note factors the
diagonal pairing.

## Definitions

Let

```text
z = conjugate(s),
f_z(d)=z/(z^2-d^2),
S_tau(d)=2tau/(tau^2-d^2).
```

In full mesh coordinates,

```text
a_s=f_z(D)1,
a_s^perp=a_s-xi_x<xi_x,a_s>/<xi_x,xi_x>.
```

Define the two finite scalar sums

```text
M_x(z)     = sum_n xi_n/(z^2-d_n^2),
V_x(tau)  = sum_n xi_n^2 S_tau(d_n).
```

## Root identity

At a finite Weyl root `tau_j`,

```text
sum_n xi_n/(tau_j-d_n)=0.
```

Since `xi_x` is even, also

```text
sum_n xi_n/(tau_j+d_n)=0.
```

Therefore

```text
sum_n xi_n/(tau_j^2-d_n^2)=0.                              (W-null)
```

Using the partial fraction identity

```text
f_z(d)S_tau(d)
= 2ztau/(z^2-tau^2)
   [1/(tau^2-d^2)-1/(z^2-d^2)],
```

the first term in `<a_s^perp,S_tau xi_x>` becomes

```text
sum_n f_z(d_n)S_tau(d_n)xi_n
= -2ztau/(z^2-tau^2) M_x(z).
```

The gauge subtracts

```text
<xi_x,a_s> <xi_x,S_tau xi_x>
= z M_x(z) V_x(tau).
```

Hence the exact factorization is

```text
<a_s^perp,S_tau_j xi_x>
= z M_x(z)
   [-2tau_j/(z^2-tau_j^2)-V_x(tau_j)].                    (CF)
```

This is the diagonal Cauchy-factor identity.

## Probe

Run:

```text
python3 E72_278_cauchy_factor_identity_probe.py
```

Output:

```text
E72.278 Cauchy-factor identity probe
Identity: <a_s^perp,S_tau xi> = z M_x(z)(-2tau/(z^2-tau^2)-V_x(tau)), z=conj(s).
Roots are restricted to the fixed compact window 0<tau<=8.
lam L roots maxRel maxInner maxM maxBracket maxRootNull
 16 5.545177     7 1.609e-10 3.958301e-02 9.429865e-03 4.196783e-01 7.904e-12
 20 5.991465     7 2.061e-11 3.309295e-02 1.216450e-02 2.719910e-01 1.398e-12
 24 6.356108     5 2.137e-14 1.634596e-02 4.774344e-03 3.423023e-01 3.601e-16
 28 6.664409     6 3.017e-10 1.293381e-02 4.052699e-03 3.190769e-01 2.624e-14
 32 6.931472     8 1.763e-07 7.970421e-03 2.781352e-03 2.865091e-01 9.327e-15
```

## Reading

The diagonal compact-root target is no longer a matrix inverse estimate.  It is the product of:

```text
1. Cauchy mass:       M_x(z)=sum xi_n/(z^2-d_n^2),
2. bounded bracket:  -2tau/(z^2-tau^2)-V_x(tau),
3. gap factor:       alpha(tau)/mu_x.
```

Thus a sufficient compact-root theorem is:

```text
for fixed compact K and H,
sup_{s in K} |M_x(conjugate(s))|/mu_x -> 0,
and
sup_{0<tau_j<=H,s in K}
|-2tau_j/(conjugate(s)^2-tau_j^2)-V_x(tau_j)| = O_{K,H}(1),
```

plus the commutator invisibility term of E72.277.

This is a finite explicit identity, not a fitted estimate.  The hard part has moved to controlling the
Cauchy mass `M_x(z)` and the bounded variance bracket uniformly.
