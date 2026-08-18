# Phase 102 execution plan

## Target

Prove Omega7:

[
  \lambda_n=\lambda_n^{arch}+\lambda_n^{prime}\ge0
  \qquad(n\ge1).
]

The finite exceptional range is already closed by a rational interval
certificate. The only mathematical target still capable of closing the
problem is the infinite signed inequality

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8).
]

## Closed trunk

| Item | Status | Phase 102 reference |
|---|---|---|
| Exact one-sided target | Closed | Snapshot restart plan |
| Paired arithmetic continuation | Closed | Snapshot restart plan |
| Laguerre integration by parts with boundary term | Closed | Snapshot restart plan |
| Finite range `1 <= n <= 7` | Closed | Snapshot finite certificate |

## Open trunk

| Item | Required closure |
|---|---|
| Global signed inequality | A proof of the lower bound for all `n>=8`. |
| Boundary limit | Uniform passage `epsilon downarrow 0` without separating divergent terms. |
| All scales in `n` | A theorem covering transition, oscillatory and tail ranges. |
| Sign preservation | A decomposition that estimates only after global signed pairing. |
| Discriminant mechanism | An arithmetic mechanism that distinguishes off-line controls without assuming the conclusion. |
| Li assembly | Combine finite and infinite ranges and apply Li. |

## Direct route

The direct route is split into two targets.

### A0

Prove an unconditional uniform tail theorem:

[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T(n)}}^\infty
  (\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

This target is not expected to carry the full RH difficulty. It should use
only explicit PNT input and uniform Laguerre bounds.

### A1

Prove the signed core inequality:

[
  -n+
  \int_1^{e^{T(n)}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

This is the first isolated force-RH target in this phase.

## Alternative route

The LP+IDENT/RDI route is not the priority unless it produces one of the two
literal bridges:

[
  \mathrm{RDI}\Longrightarrow \lambda_n\ge0
]

or

[
  \mathrm{RDI}\Longrightarrow\text{all zeros of }\Xi\text{ are real}.
]

Without such a bridge, BTG and GAP-Z remain infrastructure, not closure of
Omega7.

## Work order

1. Lock the finite range in the phase ledger.
2. A0 is closed by `102_A0_UNIFORM_TAIL_THEOREM.md`, up to inserting the chosen explicit PNT and archimedean constants.
3. Attack A1 through one of the two surviving global mechanisms: Mellin coboundary or bordered Euler current.
4. Keep the RDI route in triage unless a literal Li bridge appears.
5. Assemble Li only when no open hypothesis remains.

## Phase 102 reductions now available

| Block | Status | Reference |
|---|---|---|
| A0 tail | Proved modulo external explicit constants | `102_A0_UNIFORM_TAIL_THEOREM.md` |
| Boundary limit | Reduced to A0 plus A1 | `102_BOUNDARY_LIMIT_AND_LIMIT_ORDER.md` |
| Scale/truncation bookkeeping | Closed as bookkeeping | `102_SCALE_DECOMPOSITION_AND_TRUNCATION.md` |
| Off-line sensitivity | Formulated as required discriminator | `102_A1_ZERO_SIDE_DISCRIMINANT.md` |
| A1 mechanisms | Two local routes eliminated; two global routes survive | `102_A1_SIGNED_COMPENSATION_CANDIDATES.md` |
| RDI bridge | Minimal theorem stated; not proved | `102_RDI_TO_LI_MINIMAL_BRIDGE.md` |
| Li assembly | Conditional theorem proved | `102_LI_ASSEMBLY_CONDITIONAL_THEOREM.md` |
