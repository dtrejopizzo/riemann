# Audit of phases 90–101: from the Kato current to the divisor-identification wall

## Executive verdict

Block 90–101 does not prove RH. Its valid contribution is a long sequence of finite identities,
polynomial continuations, cofactor factorizations, conditional closure theorems, and no-go results that
eliminate shortcuts. The reduction is coherent: the initial object, the Kato line, the Euler cocycle,
the bordered numerator, the characteristic Jacobian, the von Mangoldt response, the commutator, the
Fourier shell, and the Stieltjes/heat currents are coordinates of the same obstacle, not cumulative
proofs of lesser strength.

The RH-strength point is localized in three content-equivalent ways:

```text
DIRECT-BORDERED-ANCHOR / RDI-ANCHOR
        = Gamma–Euler identification of the bordered determinant;

LOCAL-COVARIANT-IDENT / STIELTJES-IDENT
        = identification of a positive transform on a safe interval;

XI-PARITY-CURRENT-NULL
        = vanishing of all the main currents separating Xi's divisor.
```

The third is **EQUIVALENT-TO-RH**; `TRUE-DIVISOR-IDENT` (convergence sensitive to support and linear
multiplicity before contracting) is an even stronger sufficient condition. Convergence of logarithmic
derivatives on any safe interval from E101.095 also has RH strength by Pick–Nevanlinna propagation.
The identities, finite self-adjointness results, tail bounds, cofactor diagrams, and finite trials do
not cover this identification.

**Convention.** PROVED designates an identity or implication with exposed hypotheses and an internal
proof. CONDITIONAL requires its hypotheses. NUMERICAL is reproducible only at a finite section.
CONJECTURAL is a mechanism not yet closed. REFUTED is a discarded inference or route.
EQUIVALENT-TO-RH is a reformulation that forces RH. INCOMPLETE is a program with a gap not turned into a
theorem.

## Documentary coverage

The READMEs, all closures, the 101 ledger, and the `E90`–`E101` mathematical documents were read. The
101 series contains 96 documents `E101.001`–`E101.096`; its three Python probes were also inspected.
Running the available probes together finished without failure, but produced no additional asymptotic
certificate; their outputs, when present in the texts, are classified as NUMERICAL. No probe was treated
as proof of a limit.

| Phase | Coverage | Dominant classification | Inheritable result |
|---|---:|---|---|
| 90 | 7/7 Markdown | PROVED + INCOMPLETE | exact Kato current and two-sided defect |
| 91 | 6/6 Markdown | PROVED + REFUTED | coboundary/leak equivalence and derivation defect |
| 92 | 9/9 Markdown | PROVED + EQUIVALENT-TO-RH | global projective numerator; anchor intact |
| 93 | 7/7 Markdown | PROVED + EQUIVALENT-TO-RH | theorem `DIRECT-BORDERED-ANCHOR ⇒ Omega7` |
| 94 | 8/8 Markdown | PROVED + NUMERICAL | global cofactor current and two-generator polynomial |
| 95 | 7/7 Markdown | PROVED + CONDITIONAL | characteristic Jacobian on simple charts |
| 96 | 7/7 Markdown | PROVED + EQUIVALENT-TO-RH | coupled global von Mangoldt response |
| 97 | 8/8 Markdown | PROVED + NUMERICAL | canonical sensitivity and Euler commutator |
| 98 | 7/7 Markdown | PROVED | exactly matched internal/shell division |
| 99 | 8/8 Markdown | PROVED + NUMERICAL | bordered sandwich and separated characteristic correction |
| 100 | 7/7 Markdown | PROVED | characteristic correction = chain rule |
| 101 | 98/98 Markdown, 3/3 probes | PROVED/NO-GO + EQUIVALENT-TO-RH | discriminant atlas, no cofinal identification |

Coverage of 101 is grouped only for readability; each entry `E101.001`–`.096` was cross-checked against
the README and ledger, without counting the summaries as an independent result.

| E101 series | Audited status | Surviving content |
|---|---|---|
| .001–.009 | PROVED | horizontal/cotangent projection, factorization, and exact covariant current |
| .010–.023 | PROVED; final closure EQUIVALENT-TO-RH | safe compactness and uniqueness; identifying the limit on an interval remains the load |
| .024–.031 | PROVED / REFUTED | sign walls, rightward drift, resolvent, and coherence; finite conditions do not determine the divisor |
| .032–.044 | PROVED; goal EQUIVALENT-TO-RH | moment–heat–Weil compactification, explicit tails, and stability; the central comparison is missing |
| .045–.053 | PROVED + CONDITIONAL | exact attribution of `DIRECTIONAL-IDENT`; reduction of tails to unproved quantitative estimates |
| .054–.061 | PROVED / REFUTED | novelty gate, flat holonomy, Hardy obstacle, and Abel no-go; no norm closing IDENT appears |
| .062–.070 | PROVED / REFUTED / INCOMPLETE | secants, mixed moments, shifts, and Pearson; return to the same signed residual |
| .071–.085 | PROVED / REFUTED | quartet falsifiers, jet walls, diagonal, and conjugate graph; the parity Gram separates only after identifying the divisor |
| .086–.090 | PROVED / INCOMPLETE | Abel/Mellin discriminants and Toeplitz–Hankel separation; an RH-strength quotient covariance remains |
| .091–.092 | PROVED / REFUTED | normal/non-normal adjoint audit; universal metrics and corrections do not build the conjugate graph |
| .093 | PROVED under even-simple; EQUIVALENT-TO-RH | finite star and zero Hessian; Xi's current not transported |
| .094 | PROVED / CONDITIONAL | feature-normality classification; square normality does not identify Xi |
| .095 | PROVED; goal EQUIVALENT-TO-RH | exact source defect and Pick–Nevanlinna propagation; `C_core→0` has RH strength |
| .096 | PROVED / REFUTED | single-level inversion no-go; `TRUE-DIVISOR-IDENT` remains open and of RH strength |

## Phase-by-phase reconstruction

| Phase | Classified claims and real dependency |
|---|---|
| **90** | **PROVED:** spectral residue, the Kato formula with exact cancellation of `dot mu`, finite expansion by prime cells, and the two-sided layer defect. **CONDITIONAL:** single-line dominance and the static Feshbach comparison require non-vanishing and a complementary resolvent. **INCOMPLETE/EQUIVALENT-TO-RH:** `PROJECTIVE-KATO-EULER = RDI-ANCHOR` is not a new criterion. |
| **91** | **PROVED:** `C_t dot v_t=Q_tH_Pv_t` and an exact equivalence between the inverse-free formula and the coboundary with reduced leak. **REFUTED:** integrating the physical line via the base vector's gauge; the defect `(I-Z^{-1})delta v` does not vanish because the physical `ker X` is trivial. **INCOMPLETE:** the safe leak is the same bottleneck. |
| **92** | **PROVED:** the global bordered determinant eliminates the Feshbach denominator, crosses singularities, and absorbs both parities into a projective class. The cofinal diagonal only combines two convergences already given. **REFUTED as a minimal obligation:** `DOM-E`, `DOM-M`, windows, and paired widths. **EQUIVALENT-TO-RH:** `CLUSTER-RDI-ANCHOR`; eliminating singular coordinates does not identify the Euler–Gamma limit. |
| **93** | **PROVED:** `DIRECT-BORDERED-ANCHOR ⇒ SR-SAFE ⇒ Omega7 ⇒ RH`, under the cited inputs of independent product, real-rootedness, and normality. **EQUIVALENT-TO-RH:** the anchor is exactly `RDI-ANCHOR`, not a relaxation. **INCOMPLETE:** the phrase "a single open theorem" describes its accounting, not a reduction of difficulty. |
| **94** | **PROVED:** `N=det M-h^T adj(M)b`, the shift law, and the two-generator polynomial formula, valid even at `det M=0`. **NUMERICAL:** multi-precision certification of finite identities. **REFUTED:** pairing derived cofactors separately. **EQUIVALENT-TO-RH:** `COFACTOR-CELL-ANCHOR` is equivalent to the direct anchor. |
| **95** | **PROVED:** the `(t,mu)` lift, the formula `Jac(P,chi)/(P partial_mu chi)`, and chart transition. **CONDITIONAL:** a tangent-based proof requires a simple branch or a cluster pass; dividing by `partial_mu chi=0` is not allowed. **EQUIVALENT-TO-RH:** `CHARACTERISTIC-JACOBIAN-ANCHOR`. |
| **96** | **PROVED:** polarization and linear expansion of Jacobians by prime cells, keeping the full nonlinear coupling. **REFUTED:** cell-by-cell matching. **EQUIVALENT-TO-RH:** the signed sum `BASE+SUMDEF→0` is the same determinantal anchor. |
| **97** | **PROVED:** a unique trace representative, the Euler-commutator identity, and a safe polynomial reduction of the bordered adjugate. **NUMERICAL:** finite-dimensional trace residues. **INCOMPLETE:** the normalized characteristic adjugate does not become a sandwich; introducing an inverse on the singular curve would be invalid. |
| **98** | **PROVED:** a finite-rank physical lift and the exact split `BJ=INT+SHELL`; there are exactly four Fourier crossings, no more, no fewer. **INCOMPLETE/EQUIVALENT-TO-RH:** estimating before pairing destroys the cancellation; the sum `SENSITIVITY-BOUNDARY-SHELL` is the anchor. |
| **99** | **PROVED:** restricted sensitivity, augmented commutator, sandwich identity, and Gamma–Euler/boundary/shell sources. **NUMERICAL:** certification on a simple singular curve. **Essential correction:** `adj(K)[Z,H]adj(K)=0` is compatibility, not a formula for `[Z,adj(K)]`; the characteristic correction must be kept normalized. |
| **100** | **PROVED:** `adj(K)/partial_mu chi=-Pi`, and the commutator's trace gives `dot mu`. **PROVED:** `Gamma_t dot mu_t` is exactly the chain rule. **REFUTED:** counting it as an additional arithmetic source or requiring its separate smallness. |
| **101** | **PROVED:** a large atlas of finite coordinates, Stieltjes/moment/heat transforms, rank-two reduction, dual identities, and no-go results for routes losing conjugation, linear multiplicity, or signed cancellation. **CONDITIONAL:** the star and operator constructions of `.093` require cofinal even-simple. **NUMERICAL:** heat, Jacobi, and Abel profiles are diagnostics. **EQUIVALENT-TO-RH:** `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT`, `XI-PARITY-CURRENT-NULL`, and the safe logarithmic-derivative limit. **REFUTED:** finite or holomorphic single-level inversion as a substitute for the divisor. |

## 90→101 dependency matrix

```text
90  line current / layer defect
     └─ 91  coboundary = reduced leak; base-vector no-go
         └─ 92  global bordered numerator and projective continuation
             └─ 93  DIRECT-BORDERED-ANCHOR = RDI-ANCHOR ⇒ Omega7
                 ├─ 94  cofactors + shift
                 │   └─ 95  Jacobian on the characteristic curve
                 │       └─ 96  von Mangoldt response sum
                 │           └─ 97  sensitivity and Euler commutator
                 │               └─ 98  internal + Fourier shell
                 │                   └─ 99  bordered-source sandwich
                 │                       └─ 100 mu's chain rule
                 │                           └─ 101 covariant current,
                 │                              Stieltjes/heat/divisor
                 └─ 101 optional LP/prolate/radical routes and their no-go

101: LOCAL-COVARIANT-IDENT = STIELTJES-IDENT
       = identification of 93's same anchor in another coordinate
       └─ XI-PARITY-CURRENT-NULL ⇔ RH ⇔ Omega7
             ↑
   TRUE-DIVISOR-IDENT: stronger sufficient condition; not proved
```

There is no proved arrow from `90`–`101` toward the final identification. The horizontal arrows of
94–100 are algebraic coordinate changes of 93's defect. The routes in 101 using prolate theory,
Fourier, Abel, jets, moments, or transports are only useful if they supply a signed identity that fails
on the off-line-quartet control; so far they do not.

## Consistency checks and critical findings

1. **Circularity and disguised equivalences.** E93.003 itself identifies `DIRECT-BORDERED-ANCHOR` with
   `RDI-ANCHOR`; E96.005, E98.005, E99.005, and E100.005 only rewrite its coupled sum. Presenting them
   as independent advances would inflate the evidence. E101.054 confirms that Stieltjes, moments, beta,
   heat, Gaussian Weil, directional residue, and paired current form an atlas of the same discriminant.

2. **The direct anchor has exact RH strength.** E93.002 is a correct implication under its finite-family
   and independent-product hypotheses. It does not authorize treating `DIRECT-BORDERED-ANCHOR`,
   `C_core→0`, `SR-LOG`, or `STIELTJES-IDENT` as auxiliary estimates: E101.019/.021/.038/.095 classify
   them as **EQUIVALENT-TO-RH**.

3. **Adjugates and cofactors.** The polynomial continuation avoids the singular inverse and is valid.
   But neither `B[W,adj(B)]B=-det(B)[W,B]` nor its sandwich version resolves the characteristic term: at
   `det K=0` only `adj(K)[W,K]adj(K)=0` remains. E99 correctly preserves `[Z,adj(K)/partial_mu chi]`;
   E100 proves it is the chain rule and requires recombination, not disappearance.

4. **Raw/core definition change.** E101.025 and E101.095 require withdrawing from the goals any formula
   that confuses the raw hyperbolic mass with the kernel characteristic or that omits the outer mesh.
   The correct source object is `C_core`, after exactly removing the outer factor; the bilateral product
   and the linear antisymmetrization of two boundaries differ by an explicit phase defect. There is no
   license to substitute `T_+-T_+(-z)` by `T_+` nor by `T_+T_+(-z)`.

5. **Pick–Nevanlinna.** E101.095 proves a valid propagation for real even entire functions of order at
   most one with real zeros. Its strength comes from the positive multiplicities of the full logarithmic
   quotient, not from an incremental rational transfer. One safe point is not enough; an interval is.
   The finite/even-simple real-rootedness hypothesis remains CONDITIONAL across a cofinal family.

6. **Parity, current, and the finite star.** E101.093 closes the positive star and the Hessian only
   under even-simple. The rank-one atom contraction is zero on every finite section because each fiber
   is already real: this is **PROVED but not discriminating**. `NA-4_F` does not imply `NA-4_Xi`;
   conflating them would be a circular substitution of the limit divisor by the finite self-adjointness
   fact.

7. **Draft E101.094.** The overlap inequality and the feature-normality classification are algebraic
   results proved in the text. Its correct conclusion is negative: square normality of even features
   only cancels leak in a given metric; building a metric from root blocks is interpolation of the
   divisor. There is no step toward `Xi`.

8. **Draft E101.095.** The factorizations, tails, and the propagation theorem correctly separate
   infrastructure from identification. The open gap is precisely `C_core_(L,N)→0` on a safe interval, or
   the weighted ground-model bound; both must fail on the planted control. Any reading that concludes RH
   from the Euler tail's convergence or the eigenvalue equation is **REFUTED** by its sections 9–10.

9. **Draft E101.096 and `TRUE-DIVISOR-IDENT`.** The real signed representation of any quartet for a
   finite holomorphic space and the finite-difference lattice show that holomorphic moments, even
   cofinal ones, do not control transversal support. Trace products create all-pairs and a
   `m_rho^2` weight; restricting afterward to the conjugate graph does not recover linear multiplicity.
   A real Radon/distributional convergence of finite divisors would preserve real support and is
   therefore **EQUIVALENT-TO-RH**, not a topological detail. This no-go is decisive against calling the
   one-level matrix a "divisor current".

10. **Energy and support no-go.** E101.088 invalidates an average bound based on summing unreached
    classes of floor quotients. E101.089–.090 leave the Hermitian covariance of balanced quotients as a
    live object; the already-bounded product holomorphic form does not replace it. These results are
    **PROVED/REFUTED** within their classes, not a universal impossibility of a signed arithmetic
    identity.

11. **Tests and data.** Certifications in E94, E97, E99, E101.016, .034, .040, .043, .061, and .064
    check signs, scales, identities, and falsifiers at finite precision. None fixes an order of limits,
    cofinal compactness, divisor multiplicity, or the coupled residual. Their status does not exceed
    **NUMERICAL**.

## Usable status

**PROVED:** all the finite linear/polynomial identities indicated, the safe elimination of singular
inverses, the source/shell decompositions, the abstract diagonal and closure theorems under hypotheses,
the explicit tails, and the no-go results that preserve their application classes.

**CONDITIONAL:** simple-branch domain, cofinal even-simple, chart non-vanishing, source/prolate/tail
convergence, model identification with a base vector, and any use of compactness that presupposes the
spectral goal.

**NUMERICAL:** all multi-precision certifications and finite-section falsifiers.

**REFUTED:** the physical base vector's gauge, term-by-term matching, estimating shells before pairing,
erasing the characteristic correction, substituting antisymmetrization with a boundary or bilateral
product, single-level inversion, tensor restrictions with linear multiplicity, and unreached-support
bounds.

**EQUIVALENT-TO-RH:** `RDI-ANCHOR`, `DIRECT-BORDERED-ANCHOR`, `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT`,
`C_core→0` on a safe interval, `SR-LOG`, `XI-PARITY-CURRENT-NULL`, and every divisor convergence
sensitive to real support.

**INCOMPLETE:** a canonical-source Gamma–Euler identity comparing the full defect with `Xi`, preserving
linear multiplicity, and detecting the off-line control; in the current coordinates,
`TRUE-DIVISOR-IDENT`/`DIRECTIONAL-IDENT`/`DISCRIMINANT`.

Safe reuse must be limited to the finite identities and to the no-go results with visible hypotheses. An
observed convergence, a singular chart, a metric adapted to roots, a product of two traces without pair
auditing, or a support condition whose proof is already RH must not be reused as a lemma.
