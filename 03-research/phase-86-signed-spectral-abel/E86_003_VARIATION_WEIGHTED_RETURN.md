# E86.003 - Variation-weighted return criterion

## 1. The Abel probability measure

Normalize the variation in E86.001 by defining

```text
pi_j=(d_j-d_{j+1})/d_1,  1<=j<m,
pi_m=d_m/d_1.                                         (1.1)
```

Then

```text
pi_j>=0,
sum_{j=1}^m pi_j=1.                                   (1.2)
```

### Theorem 1.1

The signed complement sum is exactly

```text
sum_{j=1}^m b_j(z)Delta_P(lambda_j)
 =-d_1 sum_{j=1}^m pi_j B_j(z).                       (1.3)
```

### Proof

Substitute (1.1) into the Abel identity of E86.001 and use
`Delta_P=-d`. `QED`

Thus the desired cancellation is a return of one scalar cumulative profile
under a probability measure fixed by the cluster Weyl defect.

## 2. Spectral-projector form

Let `E_Q(x)` be the complementary spectral projection onto eigenvalues at
most `x`.  Then

```text
B_j^E(z)=ell_z(E_Q^O(lambda_j)s),
B_j^O(z)=ell_z(E_Q^E(lambda_j)1).                      (2.1)
```

The required averaged returns are

```text
R_P^E(z)=sum_j pi_j^E ell_z(E_Q^O(lambda_j)s),
R_P^O(z)=sum_j pi_j^O ell_z(E_Q^E(lambda_j)1).         (2.2)
```

The parity responses become

```text
PW-E=-alpha d_1^E R_P^E(z),
PW-O=-beta  d_1^O R_P^O(z).                           (2.3)
```

## 3. Exact sufficient theorem

The cofinal cluster closes the reduced leakage if, locally uniformly on every
safe compact and with one derivative,

```text
alpha_N d_{1,N}^E R_{P_N}^E(z)->0,
beta_N  d_{1,N}^O R_{P_N}^O(z)->0.                    (3.1)
```

Condition (3.1) is neither an operator norm nor a maximum ceiling.  It asks
only for the probability-weighted scalar return actually present in the
finite identity.

## 4. Nonextremality and rigidity

If the profile `B_j` is nearly constant at its maximum on the support of
`pi`, then the weighted return is comparable to the crude ceiling and no gain
is possible.  If its large excursions occur outside that support or cancel
under `pi`, the return can be much smaller.

Therefore the exact rigidity question is

```text
does the Weyl-variation measure concentrate on an extremal plateau of the
cumulative safe spectral profile, or on a returning region?           (4.1)
```

This is the quantified ceiling-rigidity fork.  It concerns one scalar profile,
not simultaneous recurrence of all prime phases.

## 5. Status

```text
proved:
  exact Abel probability measure;
  exact spectral-projector formula for cumulative profiles;
  exact variation-weighted return criterion;

open:
  the two returns in (3.1) for a cofinal CCM cluster.
```

