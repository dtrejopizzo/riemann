# E101.026 - Far-right drift autopsy

## 1. Off-line quartet in the squared variable

Let a symmetric off-line quartet have centered representatives

```text
zeta_0=a+ib,
conj(zeta_0)=a-ib,
a!=0.                                                (1.1)
```

In the squared safe variable, put

```text
alpha=zeta_0^2,
conj(alpha)=conj(zeta_0)^2.                           (1.2)
```

A symmetric polynomial factor carrying this quartet has logarithmic
derivative

```text
q_alpha(x)
 =m{1/(x-alpha)+1/(x-conj(alpha))},                  (1.3)
```

with a positive integer multiplicity `m`.  Since `alpha` is nonreal, (1.3)
has poles away from the negative real axis and is not a Stieltjes transform.

## 2. Loss of detection at infinity

Nevertheless,

```text
q_alpha(x)
 =2m/x+2m Re(alpha)/x^2+O_alpha(x^(-3))              (2.1)
```

as `x->infinity`.  In particular,

```text
q_alpha(x)->0.                                       (2.2)
```

Thus convergence of a safe logarithmic derivative only in a joint regime
where the evaluation point tends to infinity cannot distinguish the true
completed function from a function with finitely many off-line quartets.

## 3. Required order of limits

The determining-set theorem E101.023 requires

```text
first:  fix x_k and take the cofinal matrix limit;
then:   use the fixed accumulation set for analytic uniqueness.     (3.1)
```

It is inadmissible to replace this by

```text
x=x_(L,N)->infinity while (L,N)->infinity.           (3.2)
```

Condition (3.2) samples precisely the region where the off-line signal in
(2.1) vanishes.

## 4. Finite audit

For the corrected core defect

```text
g_core,(L,N)(x)-g_Xi(x),                             (4.1)
```

the multiprecision values at two representative sections are

```text
section       build       sigma=3       sigma=5       sigma=10
L=3.5835      zeta        -0.02189      -0.02183      -0.02157
L=3.5835      planted      0.47444       0.24025       0.07284
L=4.6052      zeta        -0.02417      -0.02408      -0.02370
L=4.6052      planted      0.48391       0.22970       0.05809.
```

The plant signal decays rapidly to the right, consistently with (2.1).  The
table is diagnostic only; the exact autopsy is the rational expansion.

## 5. Decision

A fixed far-right interval remains admissible and may exploit absolute Euler
convergence.  A drifting far-right point or interval is closed as
insufficient.  The proof must establish cofinal identification at fixed safe
points before invoking analytic uniqueness.

## 6. Status

```text
proved:
  exact off-line quartet signature in the squared safe variable;
  asymptotic loss of that signature at infinity;

closed as insufficient:
  every cofinal argument whose safe evaluation points drift to infinity;

open:
  fixed-point COUNTABLE-COFACTOR-IDENT.
```

