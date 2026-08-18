# 107.37 -- Paper B audit coverage matrix after the first exact controls

## 1. Purpose

Paper B now has a first exact audit anchor in `107_36`, but Part II is
still far from fully audited.  This note records, in one place, which
pieces of `107_07`--`107_09` are now pressure-tested and which pieces
remain theorem-level only.

Its role is governance, not new geometry:

\[
 \text{one audited shadow}
 \neq
 \text{full Part II independently closed}.
 \tag{1.1}
\]

## 2. Coverage matrix

The current audit state of Part II is:

| Part II component | Current evidence | Status |
|---|---|---|
| Same-tower return semigroup \(\Gamma_{p,k}\circ\Gamma_{p,\ell}=\Gamma_{p,k+\ell}\) | `107_36` exact audit on the fixed control \(E/\mathbf F_5\) | exact-audited shadow |
| Same-tower multiplicative degree \(p^{k+\ell}\) | `107_36` exact audit on the fixed control | exact-audited shadow |
| Diagonal Lefschetz trace \(\Gamma_n\cdot\Delta=N_n\) | `107_36` exact audit via the fixed control recurrence; source theorem in `107_31`/`107_32` | exact-audited shadow |
| Graph-vs-graph cross-check \(\Gamma_m\cdot\Gamma_n=q^nN_{m-n}\) | `107_36` exact audit on the fixed control; source theorem in `107_31`/`107_32` | exact-audited shadow |
| Connected extractor needed after cyclic trace | `107_35` exact Hopf-algebra audit and fixed-control Euler/log audit | exact-audited prerequisite |
| Prime-power local support needed by the prime sector | `107_34` exact resultant audit | exact-audited prerequisite |
| Mixed-tower refinement object \(\Gamma_{p,k}\star\Gamma_{q,\ell}\) | `107_39` exact combinatorial shadow audit | exact-audited shadow |
| Common-phase suspension geometry | `107_38` exact combinatorial shadow audit | exact-audited shadow |
| Joint Gamma--polar boundary page | `107_41` high-precision factor-consistency audit | exact-audited factor shadow |
| No-prescribed-trace renormalized source shadow | `107_65` exact symbolic audit of identity cleanup, boundary coupling, and injective source-to-trace control; `107_88` exact-audits the assembled source-determined page shadow | exact-audited shadow |
| One-step joint prime--Gamma--polar fixed-point production | theorem statement in `107_09`; `107_65` exact-audits the visible no-prescribed-trace shadow, `107_76` exact-audits one finite joint fixed-point assembly shadow, and `107_88` exact-audits the assembled no-prescribed-trace discipline | partial shadow |
| Davenport--Heilbronn external failure witness | `107_40` exact arithmetic non-Euler witness | exact-audited shadow |

## 3. What has genuinely improved

The Part II package is now stronger than it was before `107_36`.

1. The same-tower return law is no longer supported only by formal prose.
2. The degree, diagonal trace, and graph-vs-graph arithmetic shadows are
   now tied to the exact positive control.
3. The Part II audit now depends on exact prerequisites already checked
   separately in `107_34` and `107_35`.
4. Mixed-tower non-collapse and the load-bearing role of the common
   phase now have exact combinatorial shadow audits in `107_39` and
   `107_38`.
5. The renormalized trace of `107_09` is no longer protected only by
   prose: `107_65` exact-audits a visible symbolic shadow in which
   diagonal subtraction cleans only the identity channel and the
   remaining arithmetic trace is injectively source-defined.
6. `107_76` now exact-audits one finite joint assembly shadow in which
   prime returns, the common boundary page, mixed-tower refinements, and
   identity cleanup coexist in one renormalized source package without
   collapsing mixed data into the primitive prime page.
7. `107_88` now exact-audits one assembled no-prescribed-trace shadow
   in which that whole renormalized visible page remains source-
   determined and rejects external retouching as an exact failure.

This means the audited portion of Part II is now at least anchored to:

\[
 \text{local support}
 \longrightarrow
 \text{connected extraction}
 \longrightarrow
 \text{same-tower return/Lefschetz shadow}
 \longrightarrow
 \text{mixed-tower/common-phase shadows}.
 \tag{3.1}
\]

## 4. What remains unaudited

The strongest open audit gaps inside Part II are now easy to state.

### 4.1. Mixed towers

`107_39` now exact-audits the finite combinatorial shadow that keeps the
mixed refinement object distinct from every primitive return.  What is
still missing is the actual derived-fiber-product geometry and its
determinant-line realization.

### 4.2. Common-phase gluing

`107_38` now exact-audits the finite combinatorial shadow in which the
common phase is an articulation locus.  What is still missing is the
full suspension geometry on the Tate orbit pages and its determinant/
archimedean compatibility.

### 4.3. Gamma--polar joint page

`107_41` now exact-audits the explicit coupled Gamma--pole factor
identity used by `107_05` and imported by `107_09`.  What is still
missing is the full one-step fixed-point production of the joint
prime--Gamma--polar page from the suspended correspondence geometry.

### 4.4. No prescribed trace vs. full fixed-point theorem

`107_65`, `107_76`, and `107_88` now exact-audit three finite symbolic shadows of the
fixed-point assembly rule: diagonal renormalization removes only the
identity channel, the boundary page produces Gamma and pole jointly, the
renormalized visible trace has trivial kernel relative to the source
generators, mixed-tower refinements remain visible without collapsing
into the primitive prime page, and the whole visible renormalized page
stays source-determined rather than externally prescribable.  What is still missing is the
real geometric proof that the full arithmetic side of `107_09` is
produced in one fixed-point calculation on the suspended correspondence
flow.

### 4.5. External falsifier

`107_40` now exact-audits the arithmetic non-Euler witness: the
normalized Davenport--Heilbronn coefficients are not multiplicative, so
the control has no Euler product and no unchanged primitive return
tower.  What remains open is not the falsifier itself, but the full
geometric packaging of the zeta-side flow.

## 5. Status consequence

The correct reading of Part II after `107_36`, `107_38`, `107_39`,
`107_40`, `107_41`, `107_65`, and `107_76` is:

\[
 \text{Paper B no longer merely formalized},
 \qquad
 \text{same-tower function-field shadow exact-audited},
 \qquad
 \text{mixed-tower shadow exact-audited},
 \qquad
 \text{common-phase combinatorial shadow exact-audited},
 \qquad
 \text{external DH falsifier exact-audited},
 \qquad
 \text{joint Gamma--pole factor exact-audited},
 \qquad
 \text{no-prescribed-trace visible shadow exact-audited},
 \qquad
 \text{joint fixed-point assembly shadow exact-audited},
 \qquad
 \text{assembled no-prescribed-trace shadow exact-audited},
 \qquad
 \text{joint fixed-point page still only partially shadowed}.
\tag{5.1}
\]

So Paper B is now best read as `partial`, not `formalized`: several
load-bearing rows of Part II have exact shadows, while the full
suspended-geometry/fixed-point theorem is still open.  This note is
therefore a stop against future overpromotion.  Any later upgrade of
Paper B must identify which row of the matrix has actually been closed,
and by which new verifier or independent audit artifact.
