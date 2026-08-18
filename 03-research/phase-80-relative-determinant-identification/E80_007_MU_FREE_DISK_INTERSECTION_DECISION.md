# E80.007 - Decision of the mu-free disk-intersection alternative

## 1. Abstract uniqueness theorem

Let `E` be a complex vector space, let `ell:E->C` be linear, and let
`C:E->F` be an injective linear map.  Define

```text
N={v in E: ell(v)=1}.                                  (1.1)
```

### Theorem 1.1

The set `C(N)` is a nonempty singleton if and only if

```text
dim E=1  and  ell is not identically zero on E.         (1.2)
```

### Proof

Suppose first that `C(N)` is a nonempty singleton.  Choose `v_0 in N`.  For
every `h in E cap ker ell`, both `v_0` and `v_0+h` belong to `N`.  Hence
`C(h)=0`.  Injectivity gives `h=0`, so

```text
E cap ker ell={0}.                                      (1.3)
```

Since `ell(v_0)=1`, every `v in E` decomposes as

```text
v=ell(v)v_0+(v-ell(v)v_0),
```

and the second term belongs to `E cap ker ell`.  It is zero by (1.3), so
`E=span{v_0}`.  This proves (1.2).

Conversely, if `E=span{e}` and `ell(e)!=0`, then

```text
N={e/ell(e)},
```

and its image is a singleton. `QED`

## 2. Application to safe Cauchy transforms

For a square-summable mesh vector `v`, define

```text
C(v)(z)=sum_n v_n/(z-d_n)                               (2.1)
```

on a safe domain disjoint from the real mesh.  If `C(v)` vanishes on a set
with an interior accumulation point, analytic continuation and the residues at
the simple poles `d_n` give `v_n=0` for every `n`.  Thus `C` is injective.

Let `E_L` be the full square-summable solution space of the infinite CCM
equation and let

```text
ell_0(v)=C(v)(z_0).                                     (2.2)
```

The original safe limit-point endpoint says that the safe transform is unique
among all `v in E_L` satisfying `ell_0(v)=1`.  Theorem 1.1 therefore gives the
exact equivalence

```text
unique normalized safe transform
<=> dim E_L=1 and ell_0|_{E_L} is nonzero.               (2.3)
```

This conclusion does not depend on a spectral coordinate or on a finite
section.  It follows only from the quantifier "among all square-summable
solutions" and injectivity of the safe Cauchy transform.

## 3. Decision between the two ledger scenarios

The post-audit ledger proposed:

```text
S1: derive disk intersection from a mu-free remnant and never need the
    simplicity/nonvanishing clauses;

S2: construct admissible replacements for those clauses.               (3.1)
```

For the original endpoint, Theorem 1.1 rules out `S1`.  A mu-free construction
may select one source-normalized response even when `dim E_L>1`, but it then
proves uniqueness only inside a source-selected subclass.  It does not exclude
another `h in E_L cap ker ell_0`, and therefore does not prove uniqueness among
all square-summable solutions.

Hence `S2` is logically compulsory unless the downstream endpoint is replaced
and its implication to `SR-SAFE` is proved anew.

## 4. What mu-free replacement must contain

Avoiding a build-discriminating spectral parameter does not remove the
requirements; it changes how they must be proved.  A valid mu-free interface
theorem must include:

```text
MF-1  one fixed infinite equation and one fixed boundary normalization;
MF-2  nonemptiness of its normalized square-summable solution set;
MF-3  one-dimensionality of the full solution space;
MF-4  nonvanishing of ell_0 on that space;
MF-5  finite bordered objects whose intersection equals exactly the image of
      that full normalized solution set;
MF-6  local uniform control on safe compact sets, including singular
      finite-section regularization.                                  (4.1)
```

Under `MF-1`--`MF-6`, scalar disk contraction gives the original LP endpoint.
Without `MF-3` or `MF-4`, Theorem 1.1 supplies an explicit obstruction.

## 5. Separation from MIN-CONV

The disk-intersection theorem controls normalized solution transforms at one
fixed `L`.  `MIN-CONV` controls bilateral logarithmic derivatives of the
finite characteristic.  No proved identity in the archive maps one family to
the other with the local bounds needed by the normal-family criterion.

Therefore the mu-free interface does not presently supply `VITALI-Z`; it is a
separate LP obligation.  Any claimed implication must first give an exact
formula relating the bordered disk coordinate to `T'/T`, including a uniform
zero-free denominator on safe compact sets.

## 6. Status

```text
proved:
  the abstract uniqueness theorem;
  injectivity of the safe Cauchy transform;
  equivalence (2.3);

decided:
  the ledger alternative S1 is impossible for the original full-solution
  endpoint;
  S2, in a genuinely mu-free form, is necessary;

reduced:
  the interface front to the explicit clauses MF-1--MF-6;

open:
  theorem-grade MF-1--MF-6 for the infinite CCM system;
  a replacement source-selected endpoint would also remain open until its
  direct implication to SR-SAFE were proved;

separate:
  the LP interface does not close MIN-CONV or the arithmetic anchor.
```

