# E72.74 -- Even-sector HPAC certificate

**Date:** 2026-07-08.
**Role:** collapse the full two-resolvent HPAC certificate to a single even-sector scalar identity.

## 0. Even vectors

Both vectors in the HPAC scalar are even:

```text
Pi k_x=k_x,
Pi 1=1.
```

Only the Cauchy-Feshbach vector:

```text
v=C_x^(-1)Q_x(sI-D)^(-1)1
```

has both parity components. Since all target vectors below are even, only:

```text
v_even=(v+Pi v)/2
```

contributes.

## 1. Even resolvent

Define:

```text
S_tau:=R_+(tau)+R_-(tau)
      =2tau(tau^2I-D^2)^(-1),
```

where:

```text
R_+(tau)=(tau I+D)^(-1),
R_-(tau)=(tau I-D)^(-1).
```

For even `k`:

```text
<r_+(tau),k>=<r_-(tau),k>.
```

Also:

```text
r_+(tau)+r_-(tau)=S_tau 1.
```

## 2. Full HPAC scalar in the even sector

From E72.71:

```text
F_x(s;tau)
 = alpha(tau){
     i[<v,R_+k>+<v,R_-k>]
     -(E_tau-1)/L[
       <v,r_+><r_+,k>+<v,r_-><r_-,k>] }.
```

Using parity:

```text
F_x(s;tau)
 = alpha(tau){
     i <v_even,S_tau k>
     -(E_tau-1)/L <v_even,S_tau1><r_-(tau),k> }.                 (EV-HPAC)
```

This identity holds for every `tau` off the mesh, not only at finite roots.

## 3. Finite-root form

At a finite root:

```text
<r_-(tau_j),xi_x>=0.
```

Therefore:

```text
<r_-(tau_j),k_x>=<r_-(tau_j),k_x-xi_x>.
```

The finite-root certificate becomes:

```text
max_{P_x(tau_j)=0}
| i <v_even,S_tau_j k_x>
  -(E_j-1)/L <v_even,S_tau_j1><r_-(tau_j),k_x-xi_x> | -> 0.      (EV-CERT)
```

This is the smallest scalar form reached so far.

## 4. Interpretation

The HPAC residual lives entirely in the even sector after ground-line projection:

```text
v_even=C_even^(-1)Q_even s(s^2I-D^2)^(-1)1.
```

The odd Cauchy channel is invisible to HPAC divisibility.

Thus the remaining proof no longer asks for full reduced leakage. It asks for a single even-sector
identity involving:

```text
S_tau_j k_x,
S_tau_j 1,
r_-(tau_j),
k_x-xi_x.
```

## 5. Status

```text
proved: full HPAC scalar collapses to the even-sector identity (EV-HPAC);
proved: finite-root HPAC certificate is equivalent to (EV-CERT);
open:   prove EV-CERT from even-sector Feshbach shorting and finite Weyl-nullity.
```
