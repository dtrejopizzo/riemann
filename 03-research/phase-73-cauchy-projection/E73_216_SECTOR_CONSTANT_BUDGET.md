# E73.216 - Sector constant budget for Bernoulli remainder

Date: 2026-07-14.

## 1. Purpose

E73.214 allows the Bernoulli remainder bound to carry a fixed sector constant
`C_sec`.  This note computes how large `C_sec` may be before the
`BALL-ENTRY-CERT` entry target fails.

## 2. Computation

For each entry, write:

```text
R_entry(C_sec)=R_ball+R_exp+C_sec R_psi_unit(K).
```

The allowed constant is:

```text
C_sec <= (r_entry-R_ball-R_exp)/R_psi_unit(K).
```

The certificate takes the minimum over all entries.

## 3. Status

```text
diagnostic: quantifies how much sector-constant slack the Bernoulli lemma has;
usage: choose K large enough that formal constants cannot threaten the entry certificate.
```
