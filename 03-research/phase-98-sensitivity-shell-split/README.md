# Phase 98 - Sensitivity shell split

## 1. Objective

Separate exactly the Fourier-compression contribution in the Euler
sensitivity commutator, without estimating the shell before the safe pairing.

## 2. Main identity

For a Fourier projection `P_N`, its complement `Q_N` and a lifted finite
sensitivity `K_N=P_NK_NP_N`,

```text
[Z,K_N]
 =[P_NZP_N,K_N]
  +Q_NZP_NK_N-K_NP_NZQ_N.                            (2.1)
```

The first term is internal.  The last two are the exact outgoing and incoming
Fourier shell crossings.

## 3. Work order

```text
E98.001  finite-rank physical lift;
E98.002  exact shell commutator split;
E98.003  internal adjugate reduction;
E98.004  bilateral current decomposition;
E98.005  corrected direct boundary target.
```

