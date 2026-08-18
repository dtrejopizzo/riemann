# E92.006 - Global bordered fallback

## 1. Full-cluster choice

In E88.001 choose the cluster projection to be the identity.  Then there is no
regular complement and

```text
F_t=M_t,
b_t^eff=b_t,
h_(t,z)^eff=h_z,
G_(t,z)^reg=1.                                       (1.1)
```

The denominator-free numerator becomes

```text
N_t^full(z)
 =det[[M_t,b_t],
      [h_z,1]]                                       (1.2)

 =det M_t-h_z adj(M_t)b_t.                           (1.3)
```

Equation (1.3) is a polynomial identity and is valid even when `M_t` is
singular.

## 2. Exact projective ratio

Whenever `M_t` is invertible,

```text
G_t(z)=N_t^full(z)/det M_t,                           (2.1)
```

so

```text
G_t(z)/G_t(z_*)
 =N_t^full(z)/N_t^full(z_*).                         (2.2)
```

Every local Feshbach numerator is a factorization of the same full bordered
determinant.  Indeed, block determinant elimination gives

```text
N_t^full(z)=det C_t N_t^cluster(z)                   (2.3)
```

whenever the chosen complement block `C_t` is invertible.  The factor
`det C_t` is independent of `z` and therefore also cancels projectively.

## 3. Removal of complementary invertibility

If a proposed regular complement develops another small direction, one may
either enlarge the cluster or use (1.2) directly.  Thus complementary
invertibility is required only for the Feshbach coordinate, not for the
projective bordered object.

The cost of the global fallback is computational: the determinant dimension
grows with the finite section.  It introduces no new logical hypothesis.

## 4. Projective nontriviality

For invertible `M_t` with distinct mesh nodes and nonzero Cauchy weights,
`N_t^full(z)` cannot vanish identically as a function of `z`.  To see this,
put `x_t=M_t^{-1}b_t`.  If

```text
1-h_zx_t=0                                           (4.1)
```

identically, the residues at every mesh pole force every coordinate of
`x_t` to vanish.  The constant term in (4.1) then gives `1=0`, a contradiction.

At a singular endpoint the entire coefficient vector may vanish to a common
order in `t`.  Its limiting projective class, rather than its unnormalized
endpoint value, is the canonical object.

## 5. Status

```text
proved:
  exact global bordered determinant;
  exact factorization through every regular Feshbach complement;
  removal of complementary invertibility as a logical requirement;
  nontriviality before the singular endpoint;

open:
  uniqueness and arithmetic identification of the limiting projective class.
```

