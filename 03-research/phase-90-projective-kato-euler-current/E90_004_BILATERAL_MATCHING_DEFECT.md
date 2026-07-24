# E90.004 - Bilateral Euler-matching defect

## 1. Bilateral projective current

Put `u=s-1/2`, choose a safe base point `s_*`, and define

```text
B_t(s;s_*)
 =[phi_t(iu)phi_t(-iu)]
  /[phi_t(iu_*)phi_t(-iu_*)].                        (1.1)
```

Then

```text
partial_t log B_t(s;s_*)
 =J_t(iu,iu_*)+J_t(-iu,-iu_*).                       (1.2)
```

By E90.003 this equals

```text
sum_(2<=n<=exp L) Lambda(n)n^(-1/2)
 [K_t(iu,iu_*;log n)+K_t(-iu,-iu_*;log n)].          (1.3)
```

## 2. Independent Euler current

For the independently normalized product,

```text
partial_t log[E_(L,t)(s)/E_(L,t)(s_*)]
 =J_L(s)-J_L(s_*),                                   (2.1)

J_L(s)-J_L(s_*)
 =2 sum_(2<=n<=exp L)
   [Lambda(n)/log n][n^(-s)-n^(-s_*)].               (2.2)
```

Both sides are finite von Mangoldt sums, but their kernels are different.

## 3. Exact layer defect

For a layer interval `I=[1-epsilon,1]`, define

```text
LAYER-DEF_(L,N)(s;s_*)
 =integral_I partial_t log B_t(s;s_*)dt
  -epsilon[J_L(s)-J_L(s_*)].                         (3.1)
```

Using (1.3) and (2.2),

```text
LAYER-DEF_(L,N)(s;s_*)
 =sum_(2<=n<=exp L) Lambda(n)n^(-1/2)
  {
   integral_I
    [K_t(iu,iu_*;log n)+K_t(-iu,-iu_*;log n)]dt
   -[2epsilon/log n]
    [n^(-(s-1/2))-n^(-(s_*-1/2))]
  }.                                                  (3.2)
```

Equation (3.2) is exact whenever the selected line is simple and its four
safe profiles are nonzero throughout the layer.

## 4. Correct combined target

The layer defect is not required to vanish separately.  E87.005 proved that
the admissible statement is signed cancellation with `BASE-BULK`.  After the
dominance replacement error is included, the live theorem is

```text
PROJECTIVE-KATO-EULER:
BASE-BULK_(L,N)(s;s_*)
 +LAYER-DEF_(L,N)(s;s_*)
 +DOM-ERR_(L,N)(s;s_*) ->0                           (4.1)
```

locally uniformly on `Re s>1`, first through the finite-section passage and
then through the outer limit.

This is RDI-ANCHOR in explicit prime-response coordinates.  It is not a new
criterion weaker than RDI.

## 5. Status

```text
proved:
  exact bilateral projective current;
  exact comparison with the independent Euler current;
  exact layer-defect formula;

open:
  PROJECTIVE-KATO-EULER, including the signed base-layer cancellation and
  dominance replacement error.
```

