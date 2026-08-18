# E78.122 - The boundary-transfer bridge for `<v_2,r_z>` is dead

**Scope:** front B only, live object `MODE2-OVERLAP(z)`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the overlap
`<v_2,r_z>` cannot be identified with the boundary transfer of P76.018. The
exact mismatch is the extra boundary pole/completion built into
`transfer(z,db,inner,x,L)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem.
P76.061: respected. The autopsy is about a wrong identification of paired
         objects, not about a norm estimate.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.121 reduced the live object to the pure overlap

```text
MODE2-OVERLAP(z):
  <v_2,r_z>.                                                (B-1)
```

The most tempting bridge to the finite coupled package is the `transfer(...)`
map used in P76.018 and in the downstream boundary characteristic probes.

The question is whether `transfer(z,...)` evaluated on the mode `v_2` equals
`<v_2,r_z>`.

## 2. Exact formulas

From P76.018,

```text
transfer(z,db,inner,x,L)
 = 1/(z-d_b) - sum_n x_n / (z-d_n).                        (B-2)
```

For the pure overlap we instead have

```text
<v_2,r_z> = sum_n v_2(n) / (z-d_n).                        (B-3)
```

These are different objects already at the formal level:

```text
transfer carries an extra boundary pole 1/(z-d_b)
and the sign/completion appropriate to the bordered right-transfer problem,
whereas <v_2,r_z> is the raw interior Cauchy overlap.                      (B-4)
```

So unless a special cancellation occurs, `(B-2)` and `(B-3)` should not agree.

## 3. Probe

The audited comparison against the mode `v_2` gives:

```text
BUILD zeta
N=8:
  z=i0.6  rel mismatch = 1.25
  z=i1.0  rel mismatch = 0.654
  z=i2.0  rel mismatch = 0.211
N=12:
  z=i0.6  rel mismatch = 1.13
  z=i1.0  rel mismatch = 0.569
  z=i2.0  rel mismatch = 0.152.                            (B-5)

BUILD plant
N=8:
  z=i0.6  rel mismatch = 1.68
  z=i1.0  rel mismatch = 0.781
  z=i2.0  rel mismatch = 0.175
N=12:
  z=i0.6  rel mismatch = 1.59
  z=i1.0  rel mismatch = 0.730
  z=i2.0  rel mismatch = 0.149.                            (B-6)
```

Those errors are order one, not roundoff.

Computing the raw Cauchy overlap directly shows it is already the interior sum
`(B-3)` up to negligible real part, while the P76.018 closure carries the extra
boundary completion term required by the bordered transfer problem.  So the
failure is structural, not numerical.

## 4. Autopsy

This closes the bridge

```text
<v_2,r_z>  ?=  transfer(z,db,inner,v_2,L).                 (B-7)
```

The route fails for an exact named reason:

```text
P76.018 transfer is a bordered boundary characteristic with an explicit pole
at d_b; MODE2-OVERLAP is a pure interior Cauchy overlap.                   (B-8)
```

So any attempt to identify the live object with the boundary-transfer package
of P76.018 is now dead.

## 5. Consequence

The next admissible bridge must respect the pure interior nature of
`<v_2,r_z>`. That means:

```text
1. stay with the raw interior Cauchy transform of v_2, or
2. identify v_2 through a coupled finite interior object, not through the
   bordered transfer closure.                                              (B-9)
```

## 6. Status

```text
candidate closure - pending review

autopsied:
  the bridge from MODE2-OVERLAP(z) to the boundary transfer of P76.018;

proved:
  the mismatch is structural and comes from the extra boundary pole/completion
  term in transfer(z,...);

closed:
  transfer(z,...) as an identification of <v_2,r_z>;

next:
  attack the raw interior Cauchy transform of v_2, or identify v_2 via a
  finite interior coupled object instead of the bordered transfer package.
```
