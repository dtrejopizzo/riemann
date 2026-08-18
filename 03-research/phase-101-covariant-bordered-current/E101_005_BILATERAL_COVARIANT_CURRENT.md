# E101.005 - Bilateral covariant current

## 1. Bilateral horizontal sensitivity

Put `u=s-1/2`.  For a direction `Y`, define

```text
HC_t(z;Y)
 =Tr[adj(B_z)beta_z(Hor_(K_t)(Y))]/P(t,mu_t,z),      (1.1)

HC_t^bil(s;s_*;Y)
 =HC_t(iu;Y)+HC_t(-iu;Y)
  -HC_t(iu_*;Y)-HC_t(-iu_*;Y).                      (1.2)
```

The exact bilateral physical current is

```text
BJ_t(s;s_*)=-HC_t^bil(s;s_*;H_P).                   (1.3)
```

## 2. Recovery of the Phase 100 split

Expand the horizontal direction:

```text
beta_z(Hor_(K_t)(H_P))
 =beta_z(H_P)+dot mu_t J.                            (2.1)
```

Since

```text
gamma_t(z)=-Tr[adj(B_z)J]/P(t,mu_t,z),               (2.2)
```

the negative cofactor pairing in (1.3) is

```text
fixed-level bordered current
 +Gamma_t(s;s_*)dot mu_t.                            (2.3)
```

Thus (1.3) is exactly the recombination required by E100.005.

## 3. Integrated defect

The direct bordered anchor has the covariant-current form

```text
BASE_(L,N)(s;s_*)
 +integral_0^1 {
    -HC_t^bil(s;s_*;H_P)
    -[J_L(s)-J_L(s_*)]
  }dt
 ->0.                                                (3.1)
```

When the physical Euler unit is compressed to the Fourier section, its exact
shell crossings are included in `beta_z(H_P)`.  If they are split off as in
Phase 98, the same formula reads

```text
BASE_(L,N)
 +integral_0^1 {
    COVBOUND_t+SHELL_t-[J_L(s)-J_L(s_*)]
  }dt
 ->0.                                                (3.2)
```

No characteristic term remains outside `COVBOUND_t`.

## 4. Status

```text
closed:
  exact recombination of the bordered and moving-level currents;
  covariant form of the integrated determinant defect;

open:
  signed cofinal cancellation in (3.1), equivalently the direct bordered
  anchor.
```

