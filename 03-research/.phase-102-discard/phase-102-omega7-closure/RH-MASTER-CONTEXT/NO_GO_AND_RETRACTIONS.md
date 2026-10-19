# Consolidated register of no-go results, circularities and retractions

## Rule of use

A no-go has the form

\[
\mathcal H+\mathcal M\Longrightarrow
\text{the mechanism cannot deliver }\mathcal C,
\]

where \(\mathcal H\) are hypotheses and \(\mathcal M\) is a formalized class of methods. It only closes
\(\mathcal M\) under \(\mathcal H\). It does not authorize the phrase "no method of this language can
work" if the theorem only analyzes one kernel, one normalization, or a finite family.

The register separates:

- **REFUTATION:** there is a counterexample or an invalid inference;
- **INSUFFICIENCY:** the input still admits an off-line zero or loses decisive information;
- **CIRCULARITY:** the hypothesis already contains an RH-strength condition;
- **DUPLICATION:** it changes the coordinate of the same residue without creating a new estimate;
- **CONDITIONALITY:** the mechanism would be valid if an object that does not yet exist were built.

## Matrix of routes already traveled

| Family | Verdict | Exact scope |
|---|---|---|
| Multiplicativity and \(\omega\) classes | **REFUTED as a zero criterion** | Liouville and random multiplicative functions break the inference. The energy identities remain valid. |
| Coherence, tails, GEV and classification | **REFUTED as a proof chain** | The parameters depend on generator, selection and scale; a finite classifier does not quantify over unknown zeros. |
| Peak matrices as spectral inversion | **REFUTED** | They respond mainly to coefficients, conductor, support and ablations; zero injection does not reproduce the effect. |
| Gram matrix built only from zeros | **REFUTED as a horizontality detector** | It is PSD by construction and may have discarded the very coordinate it was supposed to distinguish. |
| TDA and cloud geometry | **INSUFFICIENT** | A finite distance or a truncated cloud does not exclude a future zero nor control the full divisor. |
| Finite positivity of Li, Mercer or Weil | **INSUFFICIENT** | A finite stretch does not control all indices or tests. Full quantification has RH-strength. |
| Weil form versus truncated residue | **REFUTED CONFUSION** | The residue between two cuts does not inherit the positivity of the full form. |
| Pointwise bounds on \(\psi(x)-x\) taken in absolute value | **INSUFFICIENT in the route tried** | The phase against the Laguerre kernel is lost and a measured-order deficit appears; it does not rule out every signed inequality. |
| Term-by-term positivity of \(\Lambda(n)\) | **INSUFFICIENT** | The whitening amplifies individual norms and destroys the inter-prime interference that sustains the sign. |
| Positive prime truncation | **REFUTED** | Finite sections can be negative while the observed full form is positive; there is no "positive part minus small tail". |
| Zero-free regions and zero density | **INSUFFICIENT for all \(n\)** | They admit an off-line zero; that single zero can force negative Li coefficients at large indices. |
| Near-periodic recurrence across all phases | **INSUFFICIENT for the quantified scheme** | The cost of matching the full vector exceeds the available detection gain. It is not a universal no-go for every scalar function. |
| Fejér–Riesz | **CIRCULAR in the proposed application** | It requires nonnegativity of the boundary symbol, which is precisely the sought positivity. |
| Kreĭn and positive extensions | **INSUFFICIENT** | Existence of some positive extension does not identify the arithmetic kernel as that extension. |
| Heat flow and de Bruijn–Newman | **INSUFFICIENT without arithmetic input** | The dynamics characterizes the real regime, but does not determine the terminal parameter; the additional cascade has open uniform bounds. |
| de Branges and Hermite–Biehler | **CIRCULAR or incompatible under the conditions tried** | The useful conditions imply real-rootedness; concrete classical formulations already fail for the proposed object. |
| Approximants with real zeros | **RH-STRENGTH in the convergence** | If they converge locally to \(\Xi\), Hurwitz transmits reality. Building that convergence is the decisive work. |
| Finite Pontryagin index | **CONDITIONAL / INSUFFICIENT** | It depends on finiteness of the defect and does not exclude infinitely many off-line orbits. |
| GLT symbol, index and passivity | **DUPLICATION** | In the full limit they return to global positivity or an equivalent Herglotz condition. |
| Hodge, Lefschetz and absolute surface | **CONDITIONAL** | A real geometry could be decisive; the corpus does not build a compatible object, diagonal, cohomology, Frobenius and polarization. |
| Castelnuovo/Minkowski transplant | **REFUTED as written** | The X3 condition for positive norm is applied to a negative-norm class. |
| Prolate, gap and quasimode | **INSUFFICIENT** | A gap does not identify the ground state nor exclude a negative index without an additional bound; that bound returns to Weil. |
| Pseudoinverse on the singular curve | **REFUTED** | Polynomial adjugates/cofactors must be used; dividing at the singular point loses the object. |
| Cell-by-cell matching | **REFUTED** | The cancellation is coupled; separating summands destroys the signed identity. |
| Single-level holomorphic moments | **REFUTED as divisor recovery** | Different signed representations have the same finite moments; transversal support and linear multiplicity are missing. |
| Trace products to recover conjugation | **REFUTED** | They create every pair and a quadratic weight on multiplicities; restricting afterward does not reconstruct the conjugate graph. |
| Real-divisor convergence sensitive to support | **RH-STRENGTH** | If it preserves real support up to \(\Xi\), it already excludes off-line zeros. It is not neutral topological infrastructure. |

## Equivalences disguised under different names

The following families must be counted only once.

### Positivity and real-rootedness

\[
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow \text{full Weil positivity}\\
&\Longleftrightarrow \lambda_n\ge0\quad\forall n\\
&\Longleftrightarrow \Xi\text{ has all its zeros real}\\
&\Longleftrightarrow -\Xi'/\Xi\text{ has the appropriate Pick property}.
\end{aligned}
\]

Herglotz, Laguerre–Pólya, useful Hilbert–Pólya, zero negative index, and a Hodge star already
identified with Weil are coordinates of this family. None adds independent evidence.

### Cauchy–Feshbach chain

The names

\[
\texttt{PW-Cauchy},\ 
\texttt{HPR-DIV},\ 
\texttt{K-DIAGOFF},\ 
\texttt{EG\_LOCK},\ 
\texttt{ADJ-ARITH-LOCK}
\]

represent successive versions of a signed arithmetic cancellation or divisibility. The Cauchy,
Feshbach and adjugate identities are proved on finite sections; the arithmetic lock is not.

### Bordered anchor

\[
\begin{aligned}
&\texttt{RDI-ANCHOR}
=\texttt{DIRECT-BORDERED-ANCHOR}
=\texttt{CLUSTER-RDI-ANCHOR}\\
&=\texttt{COFACTOR-CELL-ANCHOR}
=\texttt{CHARACTERISTIC-JACOBIAN-ANCHOR}
=\texttt{BASE+SUMDEF}\to0.
\end{aligned}
\]

Kato, Euler cocycle, bordered determinant, cofactors, characteristic Jacobian, von Mangoldt response,
commutator and Fourier shell change the representation of the same Gamma–Euler anchor.

### Identification atlas

\[
\texttt{LOCAL-COVARIANT-IDENT}
=
\texttt{STIELTJES-IDENT}
=
\texttt{SR-LOG}
=
\bigl[C_{\mathrm{core}}\to0\text{ on a safe interval}\bigr].
\]

By Pick–Nevanlinna propagation, identification on a safe interval already has RH-strength.
`XI-PARITY-CURRENT-NULL` is the same content expressed as the vanishing of separating currents.
`TRUE-DIVISOR-IDENT` is an even stronger sufficient condition, sensitive to support and multiplicity.

## Binding retractions and corrections

| Previous claim | Binding status |
|---|---|
| Multiplicativity suppresses the dangerous resonance | **WITHDRAWN** by Liouville and random multiplicative controls. |
| Inter-class covariances are predominantly negative | **WITHDRAWN**; resampling does not sustain the figure and the peaks are constructive. |
| \(\omega=2\) is a singular cause | **WITHDRAWN**; neighboring classes have comparable mass and response. |
| An off-line zero automatically produces a growth law in the truncated object | **WITHDRAWN as a lemma**; the derivation is missing and the operative control does not show it. |
| A zeros-only Gram matrix can detect horizontality via negativity | **REFUTED** by tautological PSD. |
| H0 has a universal linear or quadratic law | **WITHDRAWN**; it depends on the setup, parity and definition of the operator. |
| `det Y≡1` closes Hermite–Biehler convergence | **WITHDRAWN** as a non sequitur. |
| Phase 65's QED label closes signature continuity | **SUPERSEDED** by later corrections leaving `D8.5` open. |
| H2 covers heights bounded by compactness and positive diagonals | **REFUTED**; that reasoning does not prove PSD. |
| H6 gives a quantitative negative witness for every cluster | **DOWNGRADED** to a bound with pending tail domination and an inconsistent \(|\kappa|\) factor. |
| \(\Omega_4\) uses a single global whitening | **CORRECTED**; the positive reference and \(J_N^\infty\) have different domains. |
| \(\Omega_5\) proves boundary positivity for \(N\) | **CORRECTED**; it only proves continuity, and transmits sign only under interior positivity. |
| \(\Omega_7\) is equivalent to \(|\lambda_n^{\mathrm{prime}}|<\lambda_n^{\mathrm{arch}}\) for all \(n\) | **REFUTED**; the exact target is \(\lambda_n^{\mathrm{prime}}\ge-\lambda_n^{\mathrm{arch}}\). The absolute bound is only a sufficient strategy when the archimedean part is positive and already fails as an equivalence at \(n=1\). |
| The prime integration by parts is \(-\int(\psi-y)f'_{n,\varepsilon}\) | **REFUTED**; the correct sign is \(-n+\int(\psi-y)f'_{n,\varepsilon}=\int(\psi-y+1)f'_{n,\varepsilon}\). The earlier formula flips the sign and omits the lower boundary term. |
| The envelope asymptotics can omit the linear term | **REFUTED**; this split contains \(\frac{\gamma-1}{2}n\), which is not \(O(\sqrt n\log n)\). The bound \(c\sqrt n\log n\) for the prime part must start at \(n\ge2\). |
| The sum \(\sum_\rho(1-1/\rho)^n\) can be isolated | **REFUTED**; it diverges even under RH. |
| The adjugate's characteristic term vanishes | **REFUTED**; it is a chain rule and must be recombined. |
| Raw mass, antisymmetrized boundary and core mass are interchangeable | **REFUTED**; they differ by an explicit outer factor and phase defect. |
| A holomorphic single level recovers the divisor | **REFUTED** by signed representations and loss of linear multiplicity. |

## Precedence and quarantine

A document with `QED`, `closure` or `theorem` is placed in quarantine if a later correction exhibits
the gap. It is not deleted: it is kept as a record, but does not enter as a premise. To reuse it, a
repair file is required containing:

1. corrected statement with all quantifiers;
2. a single definition of each object;
3. a proof that does not cite the result it claims to repair;
4. an off-line control;
5. an explicit list of superseded documents.

## Consequence for the restart

No new line is opened by changing Li to Weil, Weil to Pick, Pick to Herglotz, Herglotz to index, index
to Hodge, or Cauchy to adjugate. A line is admitted only if it supplies a new arithmetic inequality or
identity that is not in the earlier atlas and that fails on the off-line model before the divisor is
invoked.

In particular, the no-go results obtained by replacing oscillation with absolute values do not close
off a one-sided inequality that preserves the Laguerre kernel. When \(\lambda_n^{\rm arch}\ge0\), that
inequality only controls the negative excursion; at indices with negative archimedean part, it must
preserve the full lower bound. This class is admissible again, although by H0 its closure will still
have RH-strength.

The full cross-cutting synthesis is in [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md).
