# R170_701 — What phase 170 contributes relative to Paper 47

Status: structural comparison and check of the
relevant proofs; not an independent audit of every proof
nor a new run of the paper's interval certificates.

## Comparison result

Phase 170 contributes an explicit realization via resolvents and
paths, with truncation bounds and reproducible prototypes. **It does
not yet contribute a sign-arithmetic inequality stronger than Paper
47.** Some necessary pieces of our construction are already better
resolved in that paper.

| Phase 170 construction | Precedent / difference in Paper 47 |
|---|---|
| Positive archimedean energy after subtracting `m(0)` | Lemma K and theorems S/A: Lévy representation and Bernstein structure. |
| Split `W=E-C`, gain, and coherent paths (301) | The paper already uses Schur and polar capacities; the explicit series of paths and their tails is an additional implementation, not a proof of the budget. |
| Contact response and second-order coupling (401) | The Schur complement and the prime coupling are already present. A perturbation formula must not be confused with the sign of its outcome. |
| Phase compensation (501) and nonlocal storage (601) | Both preserve or reformulate the spectral difficulty; neither uses the minimality of the first contact to force a new sign. |
| Möbius-commutator detector (601) | Its fidelity remained open. Paper 47's Gamma detector is already injective on all of `L²(-T,T)`. |
| Galerkin diagnostics | Paper 47 also controls the infinite complement with interval certificates. Our floating-point matrices do not improve on that certificate. |

## What remained to incorporate

1. **Faithful Gamma detector.** Use it instead of the detector whose
   kernel we do not know. R170_702 incorporates it into the storage
   and gives an exact Hilbert–Schmidt tail.
2. **Exterior collars.** Even if a prime shift does not act inside the
   window, it contributes to the collar and to the moment multiplier;
   both cancel exactly. Cutting by support does not authorize
   eliminating them separately.
3. **Full polar and parity terms.** A null vector of the complete form
   need not be primitive. R170_702 extends the finite collar balance
   while explicitly keeping the polar term.
4. **Oriented integer identity.** The finite Poisson–commutator
   section uses the sum over all integers and `Λ*1=log`, with two
   orientations and exterior terms. Putting the exact values of Λ into
   a matrix or rewriting them with Möbius does not prove that this
   identity forces the sign.
5. **Minimality.** The paper's annihilation problem requires using the
   fact that the contact is the first one. The identities 301–601 also
   hold far from the first contact; by themselves they do not exploit
   that hypothesis.

The next substantive step must produce a consequence of the oriented
integer identity and of minimality that is not valid for an arbitrary
self-adjoint operator. The detector's fidelity is no longer the
obstacle.

## Verifiable adjustments to the paper text

References: `04-papers/47-row-d-dual-certificates/main.tex`, stable labels.

- Before the concentration (approx. line 714), "The program (P) has no
  minimizer (Theorem O)" contradicts the proof of O and the OvsB
  observation: the primal attains its minimum; the dual does not. That
  sentence must be corrected.
- In the KEP discussion (approx. 1674), "m≥0" is false for the
  original symbol: `m(0)=-γ-π/2-3log(2)-log(π)<0`. It is `m-m(0)` that
  is nonnegative. Negative coefficients in the prime atoms likewise do
  not mean that their convolutive form is negative semidefinite; see
  corollary Qp.
- The introduction to first contact and the list of open problems must
  be updated to `lem:contA`, which already proves primitive
  continuity.
- **The existential extension beyond `T5=log(5)/2` is already derivable
  from the paper.** `thm:log5W` gives a strictly positive full gap in
  both parities; `lem:contT` gives continuity. Hence there exists ε>0
  such that `λW(T)>0` for `T5≤T≤T5+ε`, even after prime 5 enters. This
  does not provide a certified numeric ε nor a uniform extension to
  all heights. The open problem must ask for an **explicit and
  certified** window, not mere existence.
- Claims about the nonexistence of a dual certificate must distinguish
  existence via strong duality from an explicit formula for the
  particular family being sought.

## Scientific assessment

There is progress in the explicit construction and in separating
proof obligations. The comparison also recovers structure we had left
out. There is no basis for claiming that we already possess the
sign-arithmetic law, a new numerical certification of the continuum,
or a proof of RH.
