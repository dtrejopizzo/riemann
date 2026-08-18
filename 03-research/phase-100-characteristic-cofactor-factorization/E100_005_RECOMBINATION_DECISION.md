# E100.005 - Recombination decision

## 1. Correct tangent split

The total bilateral derivative is

```text
partial_t log P(t,mu_t)
 =partial_t log P(t,mu)|_(mu=mu_t)
  +dot mu_t partial_mu log P(t,mu_t).                 (1.1)
```

The first term is the bordered source sandwich of Phase 99.  The second is
the characteristic factor E100.004.

## 2. Decision

The two terms in (1.1) must be recombined before comparison with the Euler
current.  Separate smallness is neither true nor required.  In particular,

```text
normalized characteristic-adjugate commutator
  = moving-level chain term,                          (2.1)
```

so it is removed from the list of unidentified boundary sources.

## 3. Correct remaining theorem

`ADJUGATE-BOUNDARY-SANDWICH` is retained with the explicit chain term
`Gamma_t dot mu_t` included inside the same integral as the bordered
sandwich.  Its force-bearing content is the signed total

```text
bordered source sandwich
+ Gamma_t dot mu_t
+ Fourier shell
- Euler current.                                     (3.1)
```

## 4. Status

```text
closed:
  identification of the characteristic cofactor commutator;
  removal of that commutator as a separately unknown source;

open:
  signed cancellation of the recombined current in (3.1).
```

