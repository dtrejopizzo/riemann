# Consolidated record of no-gos, circularities and withdrawals

## Rule of use

A no-go has the form

\[
\mathcal H+\mathcal M\Longrightarrow
\text{the mechanism cannot deliver }\mathcal C,
\]

where \(\mathcal H\) are hypotheses and \(\mathcal M\) is a formalised class of methods. It closes only \(\mathcal M\) under \(\mathcal H\). It does not license the sentence "no method in this language can work" if the theorem only analyses one kernel, one normalisation or a finite family.

The record distinguishes:

- **REFUTATION:** there is a counterexample or an invalid inference;
- **INSUFFICIENCY:** the input still admits an off-line zero or loses decisive information;
- **CIRCULARITY:** the hypothesis already contains an RH-strength condition;
- **DUPLICATION:** the coordinate of the same residue changes without a new estimate;
- **CONDITIONALITY:** the mechanism would be valid if an object not yet available were constructed.

## Matrix of routes already travelled

| Family | Verdict | Exact scope |
|---|---|---|
| Multiplicativity and \(\omega\)-classes | **REFUTED as a criterion for zeros** | Liouville and random multiplicative functions break the inference. The energy identities remain valid. |
| Coherence, tails, GEV and classification | **REFUTED as a chain of proof** | Parameters depend on generator, selection and scale; a finite classifier does not quantify over unknown zeros. |
| Peak matrices as spectral inversion | **REFUTED** | They respond mainly to coefficients, conductor, support and ablations; injecting zeros does not reproduce the effect. |
| Gram matrix built from zeros only | **REFUTED as a detector of horizontality** | It is PSD by construction and may have discarded the coordinate that was supposed to discriminate. |
| TDA and point-cloud geometry | **INSUFFICIENT** | A finite distance or a truncated cloud does not exclude a future zero nor control the full divisor. |
| Finite Li, Mercer or Weil positivity | **INSUFFICIENT** | A finite range does not control all indices or tests. Full quantification is RH-strength. |
| Weil form versus truncated residue | **CONFUSION REFUTED** | The residue between two cut-offs does not inherit the positivity of the full form. |
| Pointwise bounds on \(\psi(x)-x\) taken in absolute value | **INSUFFICIENT on the route tested** | The phase against the Laguerre kernel is lost and a deficit of measured order appears; it does not exclude every signed inequality. |
| Term-by-term positivity of \(\Lambda(n)\) | **INSUFFICIENT** | Whitening amplifies individual norms and destroys the interference between primes that carries the sign. |
| Positive prime truncation | **REFUTED** | Finite sections can be negative while the observed full form is positive; there is no "positive part minus small tail". |
| Zero-free regions and zero density | **INSUFFICIENT for all \(n\)** | They admit an off-line zero; that single zero can force negative Li coefficients at large indices. |
| Almost-periodic recurrence of all phases | **INSUFFICIENT for the quantified scheme** | The cost of matching the full vector exceeds the available detection gain. Not a universal no-go for every scalar function. |
| Fejér–Riesz | **CIRCULAR in the proposed application** | It requires non-negativity of the boundary symbol, which is the positivity sought. |
| Kreĭn and positive extensions | **INSUFFICIENT** | Existence of some positive extension does not identify the arithmetic kernel as that extension. |
| Heat flow and de Bruijn–Newman | **INSUFFICIENT without arithmetic input** | The dynamics characterise the real regime but do not determine the terminal parameter; the additional cascade has open uniform bounds. |
| de Branges and Hermite–Biehler | **CIRCULAR or incompatible in the conditions tested** | Useful conditions imply real-rootedness; concrete classical formulations already fail for the proposed object. |
| Real-rooted approximants | **RH-STRENGTH in the convergence** | If they converge locally to \(\Xi\), Hurwitz transmits reality. Building that convergence is the decisive work. |
| Finite Pontryagin index | **CONDITIONAL / INSUFFICIENT** | Depends on finiteness of the defect and does not exclude infinitely many off-line orbits. |
| GLT symbol, index and passivity | **DUPLICATION** | In the full limit they return to global positivity or to an equivalent Herglotz condition. |
| Hodge, Lefschetz and absolute surface | **CONDITIONAL** | An actual geometry could be decisive; the corpus does not construct compatible object, diagonal, cohomology, Frobenius and polarisation. |
| Castelnuovo/Minkowski transplant | **REFUTED as written** | The condition X3 for positive norm is applied to a class of negative norm. |
| Prolate functions, gap and quasimode | **INSUFFICIENT** | A gap does not identify the ground state nor exclude a negative index without an extra bound; that bound returns to Weil. |
| Pseudoinverse on a singular curve | **REFUTED** | Polynomial adjugates/cofactors must be used; dividing at the singular point loses the object. |
| Cell-by-cell matching | **REFUTED** | The cancellation is coupled; separating summands destroys the signed identity. |
| One-level holomorphic moments | **REFUTED as divisor recovery** | Different signed representations have the same finite moments; transverse support and linear multiplicity are missing. |
| Products of traces to recover conjugation | **REFUTED** | They create all pairs and a quadratic weight in multiplicities; restricting afterwards does not reconstruct the conjugate graph. |
| Support-sensitive convergence of a real divisor | **RH-STRENGTH** | If it preserves real support up to \(\Xi\), it already excludes off-line zeros. It is not neutral topological infrastructure. |

## Equivalences in disguise under different names

The following families must be counted once.

### Positivity and real-rootedness

\[
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow \text{full Weil positivity}\\
&\Longleftrightarrow \lambda_n\ge0\quad\forall n\\
&\Longleftrightarrow \Xi\text{ has only real zeros}\\
&\Longleftrightarrow -\Xi'/\Xi\text{ has the appropriate Pick property}.
\end{aligned}
\]

Herglotz, Laguerre–Pólya, useful Hilbert–Pólya, zero negative index and a Hodge star already identified with Weil are coordinates of this family. None adds independent evidence.

### Cauchy–Feshbach chain

The names `PW-Cauchy`, `HPR-DIV`, `K-DIAGOFF`, `EG_LOCK`, `ADJ-ARITH-LOCK` are successive versions of a signed arithmetic cancellation or divisibility. The Cauchy, Feshbach and adjugate identities are proved on finite sections; the arithmetic lock is not.

### Bordered anchor

`RDI-ANCHOR` = `DIRECT-BORDERED-ANCHOR` = `CLUSTER-RDI-ANCHOR` = `COFACTOR-CELL-ANCHOR` = `CHARACTERISTIC-JACOBIAN-ANCHOR` = `BASE+SUMDEF` → 0.

Kato, the Euler cocycle, bordered determinant, cofactors, characteristic Jacobian, von Mangoldt response, commutator and Fourier shell change the representation of the same Gamma–Euler anchor.

### Identification atlas

`LOCAL-COVARIANT-IDENT` = `STIELTJES-IDENT` = `SR-LOG` = \([C_{\mathrm{core}}\to0\) on a safe interval\(]\).

By Pick–Nevanlinna propagation, identification on a safe interval is already RH-strength. `XI-PARITY-CURRENT-NULL` is the same content expressed as vanishing of separating currents. `TRUE-DIVISOR-IDENT` is an even stronger sufficient condition, sensitive to support and multiplicity.

## Binding withdrawals and corrections

| Earlier claim | Binding status |
|---|---|
| Multiplicativity suppresses the dangerous resonance | **WITHDRAWN** by Liouville and random multiplicative controls. |
| Inter-class covariances are predominantly negative | **WITHDRAWN**; resampling does not support the figure and the peaks are constructive. |
| \(\omega=2\) is a singular cause | **WITHDRAWN**; neighbouring classes have comparable mass and response. |
| An off-line zero automatically produces a growth law in the truncation | **WITHDRAWN as a lemma**; the derivation is missing and the operational control does not show it. |
| A zeros-only Gram matrix can detect horizontality by negativity | **REFUTED** by tautological PSD. |
| H0 has a universal linear or quadratic law | **WITHDRAWN**; it depends on the set-up, parity and definition of the operator. |
| `det Y≡1` closes Hermite–Biehler convergence | **WITHDRAWN** as a non sequitur. |
| The QED label of phase 65 closes continuity of signature | **SUPERSEDED** by later corrections that leave `D8.5` open. |
| H2 covers bounded heights by compactness and positive diagonals | **REFUTED**; that reasoning does not prove PSD. |
| H6 gives a quantitative negative witness for each cluster | **DOWNGRADED** to a bound with pending tail domination and an inconsistent factor \(|\kappa|\). |
| \(\Omega_4\) uses a single global whitening | **CORRECTED**; the positive reference and \(J_N^\infty\) have different domains. |
| \(\Omega_5\) proves boundary positivity for each \(N\) | **CORRECTED**; it only proves continuity, and transmits sign only under interior positivity. |
| \(\Omega_7\) is equivalent to \(|\lambda_n^{\mathrm{prime}}|<\lambda_n^{\mathrm{arch}}\) for all \(n\) | **REFUTED**; the exact target is \(\lambda_n^{\mathrm{prime}}\ge-\lambda_n^{\mathrm{arch}}\). The absolute bound is only a sufficient strategy when the archimedean part is positive, and it already fails as an equivalence at \(n=1\). |
| The prime integration by parts is \(-\int(\psi-y)f'_{n,\varepsilon}\) | **REFUTED**; the correct sign is \(-n+\int(\psi-y)f'_{n,\varepsilon}=\int(\psi-y+1)f'_{n,\varepsilon}\). The earlier formula reverses the sign and omits the lower boundary. |
| The envelope asymptotics may omit the linear term | **REFUTED**; this split contains \(\frac{\gamma-1}{2}n\), which is not \(O(\sqrt n\log n)\). The bound \(c\sqrt n\log n\) for the prime part must start at \(n\ge2\). |
| The sum \(\sum_\rho(1-1/\rho)^n\) can be isolated | **REFUTED**; it diverges even under RH. |
| The characteristic term of the adjugate vanishes | **REFUTED**; it is a chain rule and must be recombined. |
| Raw mass, antisymmetrised boundary and core mass are interchangeable | **REFUTED**; they differ by an explicit exterior factor and phase defect. |
| One holomorphic level recovers the divisor | **REFUTED** by signed representations and loss of linear multiplicity. |

## Precedence and quarantine

A document labelled `QED`, `closure` or `theorem` is quarantined if a later correction exhibits the gap. It is not deleted: it is kept as a record but does not enter as a premise. Reusing it requires a repair file containing:

1. the corrected statement with all quantifiers;
2. a single definition of each object;
3. a proof that does not cite the result it intends to repair;
4. an off-line control;
5. an explicit list of superseded documents.

## Consequence for the restart

No new line is opened by changing Li to Weil, Weil to Pick, Pick to Herglotz, Herglotz to index, index to Hodge, or Cauchy to adjugate. A line enters only if it brings a new arithmetic inequality or identity not in the earlier atlas and failing on the off-line model before the divisor is invoked.

In particular, the no-gos obtained by replacing oscillation with absolute values do not close a one-sided inequality that keeps the Laguerre kernel. When \(\lambda_n^{\rm arch}\ge0\), such an inequality only controls the negative excursion; at indices with negative archimedean part it must keep the full lower bound. This class is admissible again, although by H0 its closure will still be RH-strength.

The complete cross-cutting synthesis is in [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md).
