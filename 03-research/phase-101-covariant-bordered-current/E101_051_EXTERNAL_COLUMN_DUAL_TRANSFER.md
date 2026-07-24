# E101.051 - External-column dual transfer

## 1. Extension of the rectangular displacement law

Let `M_N` have row mesh `D_r` and selected column mesh `D_c`.  Let `m(d)` be
an additional CCM column at a real mesh point `d` outside the row mesh, and
let `s(d)` be the odd-symbol value at that point.  The one-column form of the
displacement identity is

```text
(D_r-dI)m(d)=-a[s_r-s(d)1_r],
a=2/L.                                                (1.1)
```

Since `d` is not a row node,

```text
m(d)=-a(D_r-dI)^(-1)[s_r-s(d)1_r].                  (1.2)
```

Let `p_zM_N=q_z` be the dual Green row of E101.046.

### Theorem 1.1 - Exact external transfer

Define

```text
U_z(d)=p_z(D_r-dI)^(-1)s_r,
V_z(d)=p_z(D_r-dI)^(-1)1_r.                         (1.3)
```

Then

```text
p_zm(d)=-a[U_z(d)-s(d)V_z(d)].                      (1.4)
```

### Proof

Left-multiply (1.2) by `p_z`. `QED`

Thus every omitted Fourier column is transported by two scalar rational
functions.  No rectangular inverse and no external spectral node occurs.

## 2. Exact shell current

Let `J_ext` be any finite external column set and let `c_d` be source
coefficients.  Put

```text
t_ext=sum_(d in J_ext)c_d m(d).                      (2.1)
```

Then

```text
p_zt_ext
=-a sum_(d in J_ext)c_d[U_z(d)-s(d)V_z(d)].         (2.2)
```

Equation (2.2) is the proof-facing form of the recombined Fourier collar in
E101.047.  The source coefficients, odd symbol and dual response remain
inside one signed sum.

## 3. Dual moment expansion

Let

```text
R_N=max{|d_j|:d_j is a row node}.                    (3.1)
```

For `|d|>R_N`, the diagonal resolvent has the convergent expansion

```text
(D_r-dI)^(-1)
=-sum_(k>=0)D_r^k/d^(k+1).                           (3.2)
```

Define the two dual moment towers

```text
A_k(z)=p_zD_r^k s_r,
B_k(z)=p_zD_r^k 1_r.                                 (3.3)
```

Then

```text
p_zm(d)
=a sum_(k>=0)[A_k(z)-s(d)B_k(z)]/d^(k+1).           (3.4)
```

For an external set contained in `|d|>R_N`, absolute convergence permits
recombination as

```text
p_zt_ext
=a sum_(k>=0)[A_k(z)S_(k+1)-B_k(z)T_(k+1)],         (3.5)

S_m=sum_(d in J_ext)c_d/d^m,
T_m=sum_(d in J_ext)c_d s(d)/d^m.                   (3.6)
```

Formula (3.5) identifies the exact data needed by repeated displacement:
two dual moment towers paired with two signed source-tail moment towers.

## 4. Parity cancellation

Assume the external set is symmetric, `s(-d)=-s(d)`, and the source is even,

```text
c_(-d)=c_d.                                          (4.1)
```

Pairing `d` with `-d` gives

```text
S_m=0 for m odd,
T_m=0 for m even.                                    (4.2)
```

Consequently (3.5) reduces to

```text
p_zt_ext
=a sum_(j>=0)[
     A_(2j+1)(z)S_(2j+2)
    -B_(2j)(z)T_(2j+1)].                             (4.3)
```

The nominal leading `A_0/d` term cancels exactly.  The surviving leading
terms are the even constant-generator moment `B_0` paired with the odd
symbol tail, and the first odd-symbol moment `A_1` paired with the even
coefficient tail.

For an odd source, `c_(-d)=-c_d`, the complementary parity tower survives.

## 5. Collar and far-tail split

Fix `eta>0` and split the omitted columns into

```text
COLLAR: R_N<|d|<=(1+eta)R_N,
FAR:    |d|>(1+eta)R_N.                              (5.1)
```

On `FAR`, (3.2) has geometric ratio at most `(1+eta)^(-1)`.  Therefore
(3.5) is a uniformly convergent moment expansion once the normalized dual
moments

```text
|A_k(z)|/R_N^k,
|B_k(z)|/R_N^k                                      (5.2)
```

have a locally summable envelope.

The near collar cannot be controlled by truncating (3.2), because its ratio
approaches one.  It must be retained in the exact rational form (2.2).  This
is the precise role of `RDP-SHELL`.

## 6. Coupled RT-2 theorem

The split in Section 5 is an exact coordinate identity, but vanishing of
the complete shell is not equivalent to separate vanishing of its two
regions.  If

```text
C_N(z)=the exact signed sum (2.2) on COLLAR,
F_N(z)=the exact signed sum (2.2) on FAR,              (6.1)
```

then the minimal obligation is

```text
RT-2-COUPLED:
  C_N(z)+F_N(z)->0.                                  (6.2)
```

The conjunction

```text
C_N(z)->0,
F_N(z)->0                                            (6.3)
```

is sufficient for (6.2), but it is not necessary.  Even scalar sequences
`C_N=N` and `F_N=-N` have zero sum while neither term tends to zero.
Therefore (6.3) may discard precisely the cancellation across the artificial
collar boundary.

The far moment expansion (3.5) remains available inside the coupled formula:
it may be substituted for `F_N` without first estimating its magnitude.  No
termwise absolute value is permitted before the full `C_N+F_N` combination
is formed.

The earlier shell-generator moments `1` and `s` are the first entries
`B_0` and `A_0` of (3.3).  E101.051 shows why controlling only those two
numbers cannot prove the full collar theorem: the exact external response
contains the complete rational functions `U_z,V_z`, equivalently all moment
orders.

## 7. Relation to IDENT

The external transfer identity is build-neutral.  It applies unchanged to a
planted CCM block.  Hence the separate sufficient clauses (6.3), when proved
from mesh and source localization alone, are transport infrastructure.

The arithmetic force remains in the joint limit with the shifted endpoint
leakage of E101.048 and the direct Gamma-prime source.  A shell estimate
which separates the plant by itself must be audited as a finite detector or
as an implicit strengthening beyond operational LP.

## 8. Status

```text
proved:
  exact two-function transfer for every external column;
  complete signed shell-current formula;
  convergent dual/source moment expansion outside the row radius;
  parity elimination of half the moment hierarchy;
  exact collar versus far-tail split;

reduced:
  RT-2 to the coupled exact current C_N+F_N;

corrected:
  separate FAR-MOMENT and COLLAR-RATIONAL vanishing is sufficient, not
  equivalent, and is no longer the minimal target;

open:
  a cofinal estimate for their coupled signed sum;
  RT-3 and DIRECTIONAL-IDENT.
```
