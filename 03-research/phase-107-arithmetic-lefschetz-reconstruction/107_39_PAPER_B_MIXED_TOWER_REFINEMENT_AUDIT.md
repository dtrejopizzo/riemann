# 107.39 -- Paper B exact audit for the mixed-tower refinement shadow

## 1. Purpose

This note adds an exact audit artifact for another open row of the Part
II coverage matrix of `107_37`: the rule that mixed-tower composition
must survive as a refinement object rather than collapse to a primitive
connected return.

The target shadow is:

\[
 \Gamma_{p,k}\circ\Gamma_{p,\ell}=\Gamma_{p,k+\ell},
 \qquad
 \Gamma_{p,k}\circ\Gamma_{q,\ell}
 =\Gamma_{p,k}\star\Gamma_{q,\ell}
 \quad (p\neq q),
 \tag{1.1}
\]

with the second output remembered as a mixed correspondence carrying both
tower labels.

## 2. Verifier

The exact verifier is
`107_39_paper_b_mixed_tower_refinement_preflight.py`.

It models a finite shadow with primes

\[
 p\in\{2,3,5,7\},\qquad 1\le k\le 3.
 \tag{2.1}
\]

The verifier checks:

1. same-tower closure: \((p,k)\circ(p,\ell)\mapsto(p,k+\ell)\);
2. mixed-tower non-collapse: \((p,k)\circ(q,\ell)\) with \(p\neq q\)
   produces a distinct mixed object carrying both labels;
3. the mixed output is not equal to any primitive symbol \((r,m)\);
4. transpose reverses the mixed labels rather than deleting them;
5. the Eulerian primitive extractor kills decomposable mixed words in
   the same sense already exact-audited abstractly in `107_35`.

## 3. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
All mixed-tower refinement shadow checks passed: 36 same-tower,
108 mixed-tower, 12 Eulerian checks.
```

So the workspace now contains an exact audit artifact for the finite
shadow of the statement that mixed-tower composition is a refinement
object, not a primitive return.

## 4. What this does and does not prove

This audit proves something narrower than the full mixed-tower geometry
of `107_07` and `107_08`.

It does prove that, in the finite shadow:

1. same-tower and mixed-tower outputs are categorically distinct;
2. mixed-tower outputs retain both tower labels;
3. the connected extractor does not mistake a decomposable mixed word
   for a primitive return.

It does **not** yet prove:

1. the full derived-fiber-product realization of the mixed square;
2. determinant-line functoriality on actual mixed return strata;
3. the archimedean coupling of those mixed refinements;
4. the joint prime--Gamma--polar fixed-point formula of `107_09`.

So the status consequence remains conservative:

\[
 \text{Paper B overall formalized},
 \qquad
 \text{same-tower shadow exact-audited},
 \qquad
 \text{common-phase shadow exact-audited},
 \qquad
 \text{mixed-tower shadow exact-audited}.
 \tag{4.1}
\]
