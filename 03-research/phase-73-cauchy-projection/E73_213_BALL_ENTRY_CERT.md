# E73.213 - BALL-ENTRY-CERT v0

Date: 2026-07-14.

## 1. Purpose

E73.212 reduces the entry certificate to a component radius check.  This note
implements that check:

```text
R_entry = R_digamma + R_round + R_exp_tail
```

and verifies it against the E73.209 target `r_entry`.

## 2. Components

The implemented radii are:

```text
R_digamma:
  Bernoulli asymptotic radius for D_1,D_2 with R=80,K=12.

R_round:
  finite elementary rounding audit
  10*(#ops)*(absolute work size)*10^(-80).

R_exp_tail:
  conservative geometric cap exp(-(2R+1/2)L).
```

The `R_round` component is still an audit model, not native outward rounding.
It is included here because it gives the correct finite certificate scale and
shows how much room a true ball implementation has.

## 3. Certificate condition

For every entry `(m,n)`:

```text
R_entry(m,n) < r_entry(lambda,N).
```

By E73.209, this implies the Krawczyk matrix budget of E73.208.  By E73.204,
that gives the bordered eigenline interval once the audit model is replaced by
true outward-rounded balls.

## 4. Status

```text
implemented: component radius check for every finite entry;
verified: radii are far below target in tested windows;
conditional: R_round must be replaced by native outward-rounded ball arithmetic.
```
