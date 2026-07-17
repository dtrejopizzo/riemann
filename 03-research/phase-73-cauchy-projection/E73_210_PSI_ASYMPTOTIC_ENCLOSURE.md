# E73.210 - Asymptotic enclosure for the digamma tail

Date: 2026-07-14.

## 1. Purpose

E73.209 reduces the bordered Krawczyk matrix interval to a per-entry radius
target.  The only non-elementary component of each closed entry is the
digamma/polygamma tail:

```text
D_1(R,omega)=1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
D_2(R,omega)=1/4 psi_1(R+1/4-iomega/2).
```

This note gives the proof-facing enclosure method for `D_1,D_2`.

## 2. Asymptotic formula

For `|arg z|<pi`, use the classical Bernoulli expansion:

```text
psi(z)
= log z - 1/(2z) - sum_{k=1}^{K-1} B_{2k}/(2k z^(2k)) + R_K(z),

psi_1(z)
= 1/z + 1/(2z^2) + sum_{k=1}^{K-1} B_{2k}/z^(2k+1) + R'_K(z).
```

In our application

```text
z=R+1/4-iomega/2,        R>=60,
```

so `Re z` is large and positive.  The branch of `log` is the principal branch,
with no cut crossing.

## 3. Remainder target

For a finite matrix entry

```text
Q_mn(y)=sum c_omega e^(iomega y)+y sum l_omega e^(iomega y),
```

the digamma-tail radius is bounded by

```text
R_digamma
<= sum_omega |c_omega| Rad(D_1(R,omega))
 + sum_omega |l_omega| Rad(D_2(R,omega)).
```

E73.209 requires:

```text
R_entry <= r_entry ~= L^-49--L^-56
```

in the tested windows.  Since all other pieces are finite elementary sums, the
first proof-facing requirement is:

```text
R_digamma << r_entry.
```

## 4. Practical certified bound

The implementation target is:

```text
ASYM-PSI-CERT(R,K):
For every frequency omega appearing in the finite matrix window,
the Bernoulli remainder bounds for psi and psi_1 at z=R+1/4-iomega/2
give R_digamma <= r_entry/10.
```

The remaining `9/10` is then available for elementary finite-sum rounding,
prime-side rounding, and outward conversion to matrix operator radius.

## 5. Why this is not a new analytic assumption

The Bernoulli expansion is only used to enclose the special functions in the
already proved identity E73.198.  It does not estimate primes, zeros, or the
final cancellation.  It is a numerical-analysis certificate for the finite
special-function value.

## 6. Status

```text
reduced: non-elementary entry enclosure to Bernoulli remainders for psi/psi_1;
open: compute conservative K,R budgets for the Phase 73 matrix windows.
```
