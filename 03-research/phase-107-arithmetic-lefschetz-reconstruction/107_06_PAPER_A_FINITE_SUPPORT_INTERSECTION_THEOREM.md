# 107.06 -- Paper A: finite-support intersection theorem

## 1. Purpose

This note closes Milestone I of 107.00.  The purpose is to synthesize
`107_03`, `107_04`, and `107_05` into one theorem-level deliverable:
the finite-support arithmetic intersection package.

Paper A does not claim a Hodge sign, an arithmetic surface realization,
or a Lefschetz trace formula.  Its role is narrower and foundational:
construct, from source data alone, a single metrized determinant theory
whose finite local terms are the prime-power resultant orders, whose
archimedean term is the Gamma--polar determinant, and whose diagonal is
computed by the same Green metric as the cross terms.

## 2. Inputs already established

The theorem below uses the three Phase 107 source papers completed so
far.

### Input A: the free source divisor module

`107_03` constructs the finite-support divisor module
\(\mathrm{Div}_{\mathrm{EF}}\), together with:

1. the raw decorated correspondence package
   \(\mathrm{Corr}_{\mathrm{raw}}\);
2. transpose before connected extraction;
3. the connected-trace map;
4. the connected prime-power generators \(Z_{p,k}\);
5. the distinguished symbols
   \(F_{\mathrm v},F_{\mathrm h},\Delta,Z_\infty\).

### Input B: finite determinant lines

`107_04` constructs the finite determinant-line functor on the
off-diagonal cyclotomic sector and proves:

\[
 \frac1{\varphi(n)}
 \log\left|\mathrm{Res}(\Phi_m,\Phi_n)\right|
 =
 \begin{cases}
 \log p,&m/n=p^a,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{2.1}
\]

It also proves that the diagonal remains an excess-intersection line, not
a finite scalar.

### Input C: the Gamma--polar metric

`107_05` attaches to the same determinant line the archimedean metric
coming from:

1. the exact Gamma--polar determinant identity;
2. the primitive finite-part constant \(\kappa_\infty\);
3. matched-cutoff cancellation on compact logarithmic support;
4. the coherent Green closure of the diagonal.

## 3. Definition of admissible finite-support divisors

Call a divisor

\[
 D=
 a_{\mathrm v}F_{\mathrm v}
 +a_{\mathrm h}F_{\mathrm h}
 +a_\Delta\Delta
 +a_\infty Z_\infty
 +\sum_{(p,k)\in S} c_{p,k} Z_{p,k}
 \in\mathrm{Div}_{\mathrm{EF}}
 \tag{3.1}
\]

admissible if:

1. \(S\subset\{(p,k): p \text{ prime}, k\ge1\}\) is finite;
2. all coefficients are real;
3. the associated logarithmic correlation \(h_D\) has compact support.

The last condition is automatic for the source package built from a
finite support set \(S\), but it is stated explicitly because the Green
metric is defined through that compact logarithmic support.

## 4. Construction of the unified pairing

For admissible divisors \(D,E\), define:

1. the finite determinant line
   \(\langle D,E\rangle_{\mathrm{fin}}\) by `107_04`;
2. the Gamma--polar norm
   \(\|\cdot\|_{\Gamma,\mathrm{pol}}\) by `107_05`;
3. the metrized line

\[
 \overline{\langle D,E\rangle}
 :=
 \bigl(\langle D,E\rangle_{\mathrm{fin}},
        \|\cdot\|_{\Gamma,\mathrm{pol}}\bigr).
 \tag{4.1}
\]

Its arithmetic degree is

\[
 I(D,E)
 :=
 \widehat{\deg}\,\overline{\langle D,E\rangle}.
 \tag{4.2}
\]

The symbol \(I(D,E)\) is used only for Paper A.  It is not yet the final
Weil quadratic form of Phase 107.

## 5. The theorem

### Theorem 5.1: finite-support intersection theorem

For every admissible finite-support pair \(D,E\in\mathrm{Div}_{\mathrm{EF}}\),
the source construction produces a metrized determinant line
\(\overline{\langle D,E\rangle}\) with finite arithmetic degree
\(I(D,E)\).  This construction has the following properties.

1. Symmetry:

\[
 \overline{\langle D,E\rangle}
 \cong
 \overline{\langle E,D\rangle},
 \qquad
 I(D,E)=I(E,D).
 \tag{5.1}
\]

2. Finite local term:
   on off-diagonal cyclotomic generators it is given by the normalized
   resultant law (2.1).

3. Archimedean term:
   its metric is the Gamma--polar determinant of `107_05`, normalized by
   the matched primitive finite part and common-cutoff cancellation.

4. Diagonal coherence:
   the self-pairing \(I(D,D)\) is obtained from the same Green metric as
   the cross-pairing \(I(D,E)\); no separate scalar diagonal is imported.

5. Finite-support exactness:
   once the common cutoff exceeds the logarithmic support of the source
   correlation, the value of \(I(D,E)\) is independent of the cutoff.

#### Proof

Existence of \(\mathrm{Div}_{\mathrm{EF}}\) and of the source
generators is exactly `107_03`.  Existence of the finite determinant line
and its symmetry on the off-diagonal sector is exactly `107_04`.
Existence of the archimedean norm and of the diagonal closure by the same
metrized line is exactly `107_05`.

Property (1) combines the symmetry of the derived tensor product with the
symmetry of the Green metric.  Property (2) is Proposition 5.1 of
`107_04`.  Property (3) is the determinant identity of `107_05`,
ultimately imported from `106.195` and stabilized by `106.181`.
Property (4) is Proposition 7.1 of `107_05`.  Property (5) is the
matched-cutoff identity of `107_05`, which is exact once the support of
the logarithmic correlation is contained in the chosen cutoff window.
\(\square\)

## 6. What Paper A proves and what it does not

The theorem above proves exactly the Milestone I claim of 107.00:
finite-support divisors now carry one coherent arithmetic determinant
theory.

It does **not** yet prove:

1. that these divisors come from a decorated Frobenius category;
2. that their intersections are realized on a regular proper arithmetic
   surface;
3. that their diagonal trace equals the arithmetic side of the explicit
   formula;
4. that the resulting quadratic form has Hodge sign.

Those are later milestones of Phase 107.

## 7. Audit against Milestone I

Milestone I of 107.00 required:

1. a finite-support divisor module;
2. finite local determinant lines with exact prime-power support;
3. an archimedean Gamma--polar metric;
4. one coherent diagonal from the same Green metric;
5. a theorem-level synthesis.

These are now provided respectively by:

1. `107_03`;
2. `107_04`;
3. `107_05`;
4. `107_05`;
5. the present note.

Therefore Paper A is now complete at the interface-construction level
requested by Milestone I.

## 8. Next transition

With Paper A closed, the next stage of Phase 107 is Part II:

1. construct the decorated correspondence category
   \(\mathrm{Corr}_{\mathrm{EF}}\);
2. define its composition and transpose at the derived level;
3. suspend it to the logarithmic prime-orbit flow;
4. derive the arithmetic Lefschetz trace formula from fixed points.

That is the first point where the program leaves the intersection package
and begins reconstructing the Frobenius/Lefschetz side of the target
diagram.
