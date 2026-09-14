# B126.004 — row B ledger

Date: 2026-09-12.

```text
ROW B:  WEIL-STRENGTH-COMPLETE  on the graph sector G of Paper 43, for the
        arithmetic family Γ_n = E_{a_S(n)} (n ≥ 1), its index contact, its
        primitive extraction and the degree law deg_det = Λ with analytic
        weight n^{−1/2}.  No external citation.
```

Clauses B.1–B.9 and their proofs: Paper 44 §10.  Reclassified items:

| item | source | disposition |
|---|---|---|
| fixed vs ramification contact not quasi-isomorphic | P123.060 §3–4 | correct, and not an obstruction — coprime support (B126.001) |
| lattice index not realized as the diagonal shadow | P123.038 §5 | `PROVED` (B126.002) |
| `T_n` is not `E_n` | P123.039 §5 | resolved without identifying them (B126.002) |
| primitive extraction not monoidal | P123.037 §5, P123.038 §5, plan §6.6 | `REFUTED as a requirement` (B126.003) |
| divisor arrows absent from `G` | P123.082 | not needed — the cube lives on the shadow target (B126.003) |
| `h ↦ A_h(r)` does not preserve convolution | P123.039 §5 | `OPEN`, reassigned to row C |
| the `n−1` factor | P123.060 §4 | the unit sector; new row C obligation |

## Handed to row C

1. The prime packet (P123.039 §4 (4.1)) is available with weight `n^{−1/2}`
   and degree `Λ(n)`; the two terms `h(±log n)` are `Γ_n` and `Γ_n^†`, equal
   in local weight because `τ_v(σ^{−1}) = τ_v(σ)`.  Still `OPEN` for C: that
   `h ↦ A_h(r)` is an integrated representation.
2. **New, stated exactly for the first time:** `w_unit(Γ_n) = n−1` is
   canonical, nonzero, and absent from the explicit formula.  Row C must prove
   it is absorbed by the Tate and Gamma sectors.  It is supported on `V(n−1)`,
   disjoint from `V(n)`, so the matching can be made place by place.
