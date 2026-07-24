# E99.002 - Exact augmented bordered commutator

## 1. Augmented Euler unit

Let

```text
widehat Z=[[Z,0],[0,1]].                              (1.1)
```

For

```text
B_z=[[M,b],[h_z,1]],                                  (1.2)
```

direct block multiplication gives

```text
[widehat Z,B_z]
 =[[[Z,M], Zb-b],
   [h_z-h_zZ, 0]].                                   (1.3)
```

### Proof

The two products are

```text
widehat Z B_z=[[ZM,Zb],[h_z,1]],
B_z widehat Z=[[MZ,b],[h_zZ,1]].                     (1.4)
```

Their difference is (1.3). `QED`

## 2. Three sources

Equation (1.3) separates the exact internal sources:

```text
operator source: [Z,M];
column source:   Zb-b;
row source:      h_z-h_zZ.                           (2.1)
```

The scalar bordered corner commutes and contributes nothing.

## 3. Full characteristic commutator

For `K=H_t-mu I`,

```text
[Z,K]=[Z,H_t],                                       (3.1)
```

so the moving scalar level is absent from the full characteristic source as
well.

## 4. Status

```text
proved:
  exact augmented bordered commutator;
  exact disappearance of the scalar level from every commutator source.
```

