# Phase 27 — adelic rigidity

Accepting the Kreĭn-Connes bridge conjecture of phase 26 as a working
hypothesis, the phase tries to prove that the Connes scaling operator H_C
has no non-real eigenvalues (neg.ind(H_C) = 0) by exploiting the arithmetic
structure of the idèle class group C_ℚ, in particular by asking whether a
local-global (Euler, prime-by-prime) factorization of the Weil form Q could
reduce global positivity to local positivity at each prime.

## Results
- Proposition 27-A.1: given the bridge, each of the κ = 2m negative
  directions of Q corresponds to exactly one pair of complex eigenvalues of
  H_C. **PROVED** (direct consequence of the bridge plus Kreĭn-Langer).
- Proposition 27-B.1/27-B.2 (Theorem 27-B.4): each such complex eigenvalue
  corresponds to a non-unitary Grössencharacter |x|^{b_j+iγ_j} of C_ℚ, and
  these are exactly the characters excluded from the unitary dual (Tate's
  Plancherel theory supports only unitary characters on L²(C_ℚ)). **PROVED**.
- Central identification: the non-L² obstruction found in phase 26 (item
  V.2) and the non-unitarity obstruction found here (27-B) are shown to be
  the *same* obstacle stated in two languages — phase 27 is not an
  independent route around V.2, it is V.2 restated adelically. **PROVED**.
- §27-C (local-global principle): the Weil form's prime-power term does
  factor over primes, Q_prime = Σ_p Q_p^pr, but each local factor Q_p^pr is
  shown by explicit example to be neither positive-definite nor independent
  of the zeros; the archimedean term is a single non-factoring piece; and
  the zero term Q_zero does **not** factor over primes at all (Proposition
  27-C.1). Both "Wall A" (does a local-global decomposition of Q even
  exist) and "Wall B" (would local positivity imply global positivity) are
  left **OPEN**.
- Diagnosis of Wall A: it is shown to be equivalent to constructing an
  arithmetic cohomology H¹(Spec ℤ, ℱ) with a Frobenius-equivariant
  intersection form whose positivity is the Hodge-index analogue of RH —
  i.e., Wall A is Wall W4-RSRP (from phases 22-25) restated in the language
  of the Connes-Consani arithmetic-site program, the most precise
  formulation reached by the program at this point.
- Chain of equivalences established: RH ⟺ κ(Q)=0 ⟺ neg.ind(H_C)=0 ⟺ Q≥0 ⟺
  (Wall A resolved + local positivity ∀p) ⟺ positivity of the intersection
  form on H¹(Spec ℤ). No step of this chain is proved beyond the first
  (classical Weil criterion); the phase closes with the chain itself as its
  deliverable, not a resolution. **OPEN** throughout.

## Documents
- `00-setup.md` — restates the bridge hypothesis and states the sole
  objective (proving neg.ind(H_C) = 0).
- `01-A-B-classification.md` — classification of negative directions as
  complex eigenvalues (27-A) and their adelic identification as non-unitary
  Grössencharacters (27-B), culminating in the V.2 = 27-B identification.
- `02-C-wall-analysis.md` — the local-global factorization audit of the
  Weil form Q, isolating Wall A (existence of the decomposition) and Wall B
  (local-to-global positivity transfer), both open.
- `03-verdict.md` — final verdict: the chain of seven equivalent
  reformulations of RH, the diagnosis of Wall A as equivalent to the
  Connes-Consani arithmetic site program, and the assessment that this is a
  methodological success (sharper reformulation) rather than a resolution.

## Relation to other phases
Depends on the Kreĭn-Connes bridge conjecture of phase 26 (accepted here as
a working hypothesis, not re-derived); identifies its central obstacle with
Wall W4-RSRP from phases 22-25; proposes a hypothetical phase 28 to attempt
an explicit construction of the arithmetic intersection form.
