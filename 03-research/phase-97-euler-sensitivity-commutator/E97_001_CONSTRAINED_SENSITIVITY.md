# E97.001 - Characteristic-constrained sensitivity

## 1. Directional response

Fix `(t,mu,z)` and let `Y` be a perturbation of the full finite CCM matrix.
It induces perturbations of the inner block, boundary column and full
characteristic matrix.  Define

```text
delta_Y P,
delta_Y chi.                                         (1.1)
```

The characteristic-constrained response is the linear functional

```text
R_z(Y)
 =[(delta_Y P)(partial_mu chi)
   -(partial_mu P)(delta_Y chi)]
  /[P partial_mu chi].                               (1.2)
```

For a cell direction `Y=Q_y`, equation (1.2) is exactly the response
`R_t(z;y)` of E96.003.

## 2. Trace representative

The space of real symmetric finite matrices is finite-dimensional and the
trace pairing is nondegenerate.  Therefore there is a unique complex symmetric
matrix `S_z` such that

```text
R_z(Y)=Tr(S_zY)                                      (2.1)
```

for every symmetric direction `Y`.

On a simple characteristic branch, `S_z` is the pullback of the two cofactor
sensitivities

```text
adj(B_z)/det(B_z),

-(partial_mu P/P)
  adj(H_t-mu_tI)/partial_mu chi,                      (2.2)
```

with the block restrictions and boundary-column duplication included.  The
second matrix is singular but its normalized adjugate is finite when the
characteristic level is simple.  No characteristic inverse is used.

## 3. Bilateral sensitivity

Put `u=s-1/2` and define

```text
S_t^bil(s;s_*)
 =S_(iu)+S_(-iu)-S_(iu_*)-S_(-iu_*).                 (3.1)
```

Then E96.003 becomes

```text
BJ_t(s;s_*)=-Tr[S_t^bil(s;s_*)H_P].                  (3.2)
```

The minus sign is the sign of `H_t=H_A-tH_P`.

## 4. Status

```text
proved:
  unique trace representative of the global cell response;
  exact bilateral sensitivity formula.
```
