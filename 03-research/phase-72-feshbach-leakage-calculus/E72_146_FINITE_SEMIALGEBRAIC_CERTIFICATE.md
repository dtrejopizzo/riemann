# E72.146 -- Finite semialgebraic certificate for scalar WRL

**Date:** 2026-07-09.
**Role:** state the current Phase 72 endpoint as one explicit finite certificate.

## 0. Data

For each finite CCM window `x`, physical band `H`, Cauchy compact `K`, and root-height window `T`,
construct the finite matrices and vectors:

```text
C_model,
C_actual,
K_rel=C_model^(-1/2)(C_actual-C_model)C_model^(-1/2),
b_H,
c_H^{pm}(tau_j),
R_x,
Y_x(tau_j),
g_{x,s}=B_xC_E^(-1)B_x^*r_s^even.
```

All objects are already explicit in E72.101--E72.142.

## 1. Certificate

The finite certificate consists of five inequalities.

### 1. Model Gershgorin coercivity

For some `a_H>0`:

```text
C_model(i,i)-sum_{j!=i}|C_model(i,j)| >= a_HL
```

for all rows `i`.                                                     `(GCOER)`

### 2. PSD distance certificate

There exists a Hermitian matrix `P_x` such that:

```text
P_x >= 0,
Tr((K_rel-P_x)^2) <= eta_H^2 < 1.                         (PSD-DIST)
```

Equivalently, `P_x>=0` may be written as nonnegativity of all principal minors.

### 3. Mass source bound

For some `B_H`:

```text
sup_{tau_j<=T} ||b_H||||c_H^{pm}(tau_j)|| <= B_H.            (MSB)
```

### 4. Bounded shorted flux

For some `F_H`:

```text
sup_{tau_j<=T} ||R_xY_x(tau_j)|| <= F_H.                    (ROP)
```

### 5. Cauchy graph-energy tail

For every compact `K`:

```text
lim_{H->infty} limsup_{x->infty} sup_{s in K}
H^2 CCGD_x(H,s) <= C_K,                                    (CGE-K)
```

with `CCGD_x(H,s)<=H^(-2)Graph_x(s)`.

## 2. Theorem 72.146

If `(GCOER)`, `(PSD-DIST)`, `(MSB)`, `(ROP)`, and `(CGE-K)` hold uniformly in the stated windows, then
scalar WRL resonance annihilation holds:

```text
x^rho L_x(s;x) - int_1^x u^rho partial_u L_x(s;u)du -> 0.
```

### Proof

1. By E72.137, `(GCOER)` implies:

```text
C_model >= a_HLI.
```

2. By E72.142, `(PSD-DIST)` is equivalent to `NHS`; by E72.140, `NHS` implies `RFBD`; by E72.138,
`RFBD` implies:

```text
C_actual >= theta_H C_model
```

with `theta_H=1-eta_H>0`.

3. Hence:

```text
C_actual >= theta_H a_H L I.                                (COER)
```

4. By E72.132, `(COER)+(MSB)` imply the mass gain:

```text
sup_{tau_j<=T}|b_H^*C_actual^(-1)c_H^{pm}(tau_j)|=O(L^(-1))->0.
```

5. By E72.127, `(ROP)` plus the mass gain imply post-main finite-band root transport.  The flux part
vanishes by centered summation by parts:

```text
h||Psi||_1 <= C_HL^(-1/2)||R_xY_x||_2 -> 0.
```

6. By E72.120 and E72.127, `(CGE-K)` removes the Cauchy physical tail.

Therefore scalar WRL resonance annihilation follows. `QED`

## 3. What is still not proved

The certificate is finite and explicit, but the uniform proof of the five inequalities is still open.
The current numerical evidence supports all five in the tested windows:

```text
GCOER:    E72.136,
PSD-DIST: E72.142 and E72.144,
MSB:      E72.132,
ROP:      E72.112/E72.118,
CGE-K:    E72.120/E72.121.
```

## 4. Status

```text
achieved: scalar WRL reduced to one finite semialgebraic certificate;
open:     prove the five certificate inequalities uniformly from the finite CCM construction.
```
