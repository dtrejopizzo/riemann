# E67.1c — Plancherel anchor for the q-Gamma archimedean sector

**Date:** 2026-07-06.
**Role:** turn the word "Plancherel" from plausible label into a sourced representation-theoretic
anchor. This is not a new numerical test; it is the literature bridge that explains why `Gamma_q` is
the correct q-canonical carrier of the archimedean polygamma tower.

## Claim

The archimedean sector of CAND-67 is legitimately closed at the following level:

```text
Gamma_q / q-digamma is a canonical q-special-function object,
zeta-free, whose q -> 1 limit gives the exact P52 h_A and hence A_N.
```

The stronger wording

```text
Gamma_q is the Plancherel/Haar c-function carrier for quantum SU(1,1)
```

is supported by the quantum SU(1,1) harmonic-analysis literature, but should be cited as a bridge
rather than treated as an independently reproved theorem inside Phase 67.

## Primary-source anchors

1. **Koelink--Stokman--Rahman, _Fourier transforms on the quantum SU(1,1) group_**
   (`arXiv:math/9911163`, Publ. RIMS 37 (2001), 621--715).

   Relevant facts from the paper:

   - They study a Haar weight on the C*-algebra of functions on quantum `SU(1,1)` and determine
     restrictions of that Haar weight in terms of Jackson and Askey-Wilson type measures.
   - Spherical functions are computed in terms of Askey-Wilson and big q-Jacobi functions, and the
     corresponding spherical Fourier transforms are identified with q-Jacobi/Askey-Wilson function
     transforms.
   - Their Appendix A uses a `c`-function expansion for the Jacobi operator spectral analysis; the
     spectral measure is expressed through the boundary values and `|c(e^{i chi})|^{-2}`-type terms.
   - They state that the Plancherel measure support of the spherical Fourier transform is the
     principal unitary series plus a discrete strange-series part.

   Phase-67 reading: this is precisely the non-compact q-harmonic-analysis place where the q-Gamma /
   q-shifted-factorial tower belongs. It supports the vocabulary "Haar/Plancherel carrier"; it does
   not by itself prove the exact normalisation used in P52.

2. **Caspers, _Spherical Fourier Transforms on Locally Compact Quantum Gelfand Pairs_**
   (`arXiv:1104.2459`, SIGMA 7 (2011), 087).

   Relevant facts:

   - Gives an operator-algebraic interpretation of quantum Gelfand pairs and shows that the quantum
     Plancherel transformation restricts to a spherical Plancherel transformation.
   - Treats the quantum analogue of the normaliser of `SU(1,1)` in `SL(2,C)` with its diagonal
     subgroup.

   Phase-67 reading: this supplies the modern locally compact quantum group framework for saying
   "spherical Plancherel" rather than only "q-special-function transform".

## What E67.1b actually proves

E67.1b proves the following computational/theoretical statement:

```text
h_A,q(z) = i[-(1/s + 1/(s-1)) + 1/2 log pi - 1/2 psi_q(s/2)]
          -> h_A(z)

and pick_jet(h_A,q) -> A_N.
```

This is **not circular** in the QSC sense because `h_A` is not an arbitrary target: it is the canonical
completed archimedean factor `pi^{-s/2} Gamma(s/2)` plus the canonical polar `s(s-1)` cell. There are
no tunable coefficients analogous to `a_{k,p}` in the prime current.

## Remaining precision issue

The polar term

```text
-(1/s + 1/(s-1))
```

is still inserted as the classical pole cell. This is appropriate for P52 matching, but in a fully
q-representational story it should be realized as the distinguished rank-one/pole direction `H`.
That is the same direction removed in rank-one escape (Phase 66). It is not a zeta-circularity issue,
but it is a structural bookkeeping item.

## Verdict

Use the following wording in Phase 67:

```text
The archimedean carrier is Gamma_q / Haar-Plancherel q-special-function data.
E67.1b closes the P52 A_N matching in the zeta-free Gamma_q sense.
E67.1c supplies the literature bridge for the Plancherel/Haar vocabulary.
The pole cell still needs an explicit q-home as the rank-one H direction.
```

