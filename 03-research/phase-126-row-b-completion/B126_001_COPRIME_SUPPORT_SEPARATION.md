# B126.001 — the two contacts have coprime support

Date: 2026-09-12.  Status: `PROVED`.  Full statement and proof: Paper 44 §3.

## The reading that blocked row B

P123.060 proves that for `Γ_n` the fixed-graph contact `C_fix(n)=[Z→n−1→Z]`
and the ramification contact `C_ram(n)=[Z→n→Z]` are not quasi-isomorphic,
decisively at `n=p^k` localized at `p`, where the first is contractible and
the primitive extraction of the second is `Z/p`.  This was read as: row A's
analytic trace computes the wrong contact for row B.

## The correction

They are not competitors.  `gcd(n,n−1)=1`, so

    supp H⁰(C_ram(n)) = V(n),   supp H⁰(C_fix(n)) = V(n−1),   disjoint.

Row A's local factor `τ_p(σ)=|σ_p|_p^{1/2}/|1−σ_p|_p` therefore collapses at
every finite place:

    p | n  ⟹ |1−n|_p = 1 ⟹ τ_p = |n|_p^{1/2}     (ramification, exponent −1/2)
    p ∤ n  ⟹ | n |_p = 1 ⟹ τ_p = |1−n|_p^{−1}    (fixed, exponent +1)

and the principal weight factors canonically — the place set is determined by
`n` itself, nothing is chosen and nothing discarded:

    w(Γ_n) = w_ram · w_unit,
    w_ram  = ∏_{p|n} |n|_p^{1/2}   = n^{−1/2} = (det C_ram(n))^{−1/2},
    w_unit = ∏_{p∤n} |1−n|_p^{−1}  = n − 1    = # H⁰(C_fix(n)),

both by the product formula.  Row A's invariant realizes **both** P123.060
complexes, each on its own closed subset of `Spec Z`.

## Why it was invisible

The deformation `F_n(t,z)=((1+tz)^n−1)/t` of P123.061 makes it one line: in
`w=1+tz` the fixed locus is `w^{n−1}=1` and the relative fibre is `w^n=1`.
The fixed group is `μ_{n−1}`, the deck group is `μ_n`.  Nobody had asked which
groups they were; the question had always been whether the two complexes could
be identified, and P123.060 had answered that correctly with "no".

Consequence for phase 119: the factorization exists only place-wise.  There is
no function of the norm that separates the two halves.  The index by places is
not a bookkeeping preference here — it is what makes row B possible.
