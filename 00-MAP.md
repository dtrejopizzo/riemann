# Map of the Repository and of the Research

## The repository

| Folder | Contents | Entry point |
|---|---|---|
| `00-references/` | External literature: Connes–Consani, Connes–Moscovici (prolate), Beurling, arXiv reviews, literature surveys. | `00-references/README.md` |
| `01-context/` | Research programs RH1–RH9: raw computational notebooks and outputs. | `01-context/README.md` |
| `02-foundations/` | Validated computational engine, zero data, precision checks. | `02-foundations/engine/` |
| `03-research/` | The phase sequence 0–209: memos, proofs, audits, certificates. | `03-research/README.md` |
| `04-papers/` | Papers 01–48. | `04-papers/README.md` |
| `05-meta-and-planning/` | Plans, audits, the master context, the index of routes attempted, and earlier versions of the top-level documents (`archive-top-level/`). | `05-meta-and-planning/README.md` |
| `06-grafico/` | Illustrative plots and sonifications. | — |
| `07-calculos-adicionales/` | Closed numerical side audits. | — |
| `08-sent/` | Notes as sent to correspondents. | — |

## The research, in order

```
RH1–RH9 (01-context)        computational base: ω-classes, resonance, localized Weil detector
   │
Phases 0–9    Arc A         ω-class decomposition; parity wall              → Papers 02–05, 21
Phases 10–28  Arc B         inverse operators / Hilbert–Pólya               → Papers 08, 11, 18–19
Phases 29–33  CCM frame     spectral triples, trace and measure criteria    → Papers 22–25
Phases 34–106 Weil form     Kreĭn/Pontryagin realizations, no-go catalogue,
                            Pick architecture to Li–Keiper                  → Papers 06–41 (36)
Phases 107–133 Arc C        arithmetic Lefschetz programme, rows A–C        → Papers 42–45
Phases 134–209 Row D        the sign: duality, certificates, barriers,
                            finite reduction, the node                      → Papers 47, 48
```

## Row D, in more detail

| Phases | Content | Where it is written |
|---|---|---|
| 134–152 | Opening campaign: canonical class, falsifiers, method theorems T1–T5, function-field model | earlier row D record; superseded by Paper 47 |
| 153–156 | First sign-carrying theorem; dual certificate theory; certificates at $\tfrac12\log 3$ | Paper 47 §§2–8 |
| 157–162 | Mechanism search, master grid of routes, first contact; certificates at $\tfrac12\log5$ | Papers 47, 48 |
| 163–189 | Tail theorem, residues, crossword of open nodes, toolbox; finite reduction $\lambda_A(T)>0 \iff S_{T,k}\succ0$ | Paper 47 §§16–19 |
| 190–204 | Creation campaigns, barrier theorem, untried families, tractability review of reformulations | Paper 47 §20; routes index |
| 205–208 | The composing object; the node; class impossibility; scope audit of the node | `03-research/phase-205…208` |

The certified frontier is $T\le\tfrac12\log15$ (Mori, cited in Paper 47). The node and the live
gate are described in [`MASTER-PLAN.md`](MASTER-PLAN.md).

## Records of what failed

- `05-meta-and-planning/ROUTES-TRIED-INDEX/` — about 1,400 routes with the reason each failed.
- Paper 48 — the routes on an 8×8 grid, with walls W1–W12 and the specification S1–S12.
- `05-meta-and-planning/RH-MASTER-CONTEXT/` — audit of phases 0–101 and programs RH1–RH9.
