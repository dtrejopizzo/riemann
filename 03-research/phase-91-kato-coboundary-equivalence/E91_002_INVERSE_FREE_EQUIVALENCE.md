# E91.002 - Inverse-free coboundary equivalence

## 1. Two-term decomposition

Use the data of E91.001 and let `u_t in ran Q_t` be any explicitly
constructed vector.  Define

```text
e_t=f_t-C_tu_t.                                      (1.1)
```

Then

```text
f_t=C_tu_t+e_t,                                      (1.2)

dot v_t=u_t+C_t^(-1)e_t.                             (1.3)
```

### Proof

Apply `C_t^{-1}` to (1.2) and use E91.001(2.4). `QED`

## 2. Exact current split

Define the projective functional

```text
L_(t;z,z_*)(w)
 =[h_zw]/[h_zv_t]
  -[h_(z_*)w]/[h_(z_*)v_t].                          (2.1)
```

Then

```text
J_t(z,z_*)
 =L_(t;z,z_*)(u_t)
  +L_(t;z,z_*)(C_t^(-1)e_t).                         (2.2)
```

The first term is explicit once `u_t` is constructed.  The second is the safe
reduced leakage.

## 3. Converse

For every proposed approximation `u_t` to the line derivative, (1.1) is the
unique defect for which (1.2) holds.  Therefore

```text
inverse-free line derivative with small projective error

if and only if

explicit line coboundary with small safe reduced leakage.              (3.1)
```

This is the line-current form of the two-term coboundary equivalence in
E82.005.

## 4. Status

```text
proved:
  exact current decomposition;
  equivalence of an inverse-free Kato formula and a line-source coboundary;

open:
  construction of u_t with a controllable reduced leakage.
```

