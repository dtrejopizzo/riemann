# E73.215 - Native ball entry certificate

Date: 2026-07-14.

## 1. Purpose

E73.213 used a rounding audit model.  This note replaces that model for the
finite elementary parts by explicit complex-ball propagation.

The special-function tail remains certified separately by the Bernoulli
remainder lemma of E73.214.

## 2. Ball model

A complex ball is represented as:

```text
B(c,r)={z: |z-c|<=r}.
```

The implemented operations are:

```text
B(c,r)+B(d,s)=B(c+d,r+s),

B(c,r)B(d,s)
=B(cd, |c|s+|d|r+rs),

exp(B(c,r))
subset B(exp(c), exp(Re c+r)(exp(r)-1)+round).
```

This is enough for the finite entry components:

```text
exp_int(alpha,L)=(exp(alpha L)-1)/alpha,
y_exp_int(alpha,L)=(exp(alpha L)(alpha L-1)+1)/alpha^2,
prime samples B(klog p).
```

## 3. Certificate

For each entry:

```text
R_entry = R_ball_elementary + R_digamma + R_exp_tail.
```

The certificate checks:

```text
R_entry < r_entry(lambda,N).
```

## 4. Status

```text
implemented: native complex-ball propagation for finite elementary pieces;
implemented: component radius check against E73.209 targets;
still separate: formal proof/citation for Bernoulli psi remainder (E73.214).
```
