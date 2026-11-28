> **V2 update:** any reference in this note to the former global character failure of 53 is withdrawn. The current verdict and the new inventory of repairs are in the V2 final report. This note preserves the thematic programme, not an external endorsement.

# Dossier for external review — audit version

Not sent. None of the persons named has been contacted by this audit or has endorsed the manuscripts. The names are the referees suggested by the author; their inclusion does not imply availability for, or acceptance of, a review.

## Material and version

Repository: dtrejopizzo/riemann, reference commit `97fb4e78d5a858baa926829a42336ae3b914e59a`. The hashes and paths of the sources examined appear in `../evidence/sources.json`. Papers 47 and 48 excluded. The map is 57 and the unified volume is 58.

The author fixed the cut-off values T=(log 5)/2 and T≈2.8022 and made clear that he does request a review of the bounds and their certificates. The four inertias of the first window have already been reproduced with Arb, analytic remainder and cross-review: `NUMERICS-46.md` and `NUMERICS-46-CROSS-REVIEW.md`. The program for the second window was found in the research folders and in the public version: its 17 checks and the functional bridge were reconstructed and reviewed; see `WINDOW-28022.md` and `WINDOW-28022-BRIDGE.md`. The global deduction examined does not use these bounds as premises.

## Request for review

A review is requested of the statements and their proofs **as written**, with three possible outcomes: (a) correct, specifying the inputs admitted; (b) incorrect, identifying the first invalid inference and why; (c) not verified, identifying exactly which step remains to be checked. It is asked that errors of formulation, repairable gaps, substantially incomplete proofs and counterexamples to statements be kept separate.

It is not requested that a specialist endorse areas outside his or her competence, nor that agreement with a single paper be interpreted as certification of RH. For any global conclusion it is also required to check each hypothesis and range in the imports.

## Proposed distribution by speciality

| Front | Papers and referees suggested by the author | Priority question and record |
|---|---|---|
| Complete argument | 46,49–56; Levent Alpoge | Deduction from the three theorems to GRH, and precise dependence on the new steps. `ANALYTIC.md`, `STATUS.md`. |
| Analysis of zeros | 46; Roger Heath-Brown, Kannan Soundararajan, Maksym Radziwiłł, James Maynard, Terence Tao | One-sided criterion, large sieve/density, admissible data and final inequality. `ANALYTIC.md`. |
| Weil framework | 43–45; Alain Connes, Caterina Consani, Enrico Bombieri, Ralf Meyer | Hochschild/topology, trace and normalisation of the explicit formula; comparison with antecedents. `../07-rows-a-b-c.md`, `HOCHSCHILD-43.md` and `COMPLETION-FORM-43.md`. |
| Theta and unitary groups | 49,53,54; Wee Teck Gan, Atsushi Ichino, Michael Harris, Stephen Kudla | Seesaw, exchange, splitting factors and Rallis. `THETA.md`, `COVOLUME.md`, **`ERROR-53-CHARACTERS.md`**. |
| CM and exact periods | 49,54; Kenichi Bannai, Shinichi Kobayashi, Haruzo Hida | Exact normalisation of Chowla–Selberg, conjugates, integrality and test form attaining the valuation. `THETA.md`. |
| Integral Hecke | 50 and application in 49; Benedict Gross, Matthew Emerton | Truncated elementary divisors, rank and arithmetic realisation. `THETA.md` and first report `../02-theta-hecke-covolume.md`. |
| Second moment and trace | 51,52; Wei Zhang, Paul Nelson, Philippe Michel, Akshay Venkatesh | Exact main constant, all pairs and ranges, comparison of multiplicities. `SPANNING.md`, `MULTIPLICITIES.md`. |
| Galois/Selmer | 55; Christopher Skinner, Eric Urban, Kenneth Ribet, Frank Calegari, Ana Caraiani | Ribet to prime powers, local types and scope of the labels, twists for each prime and sum of losses. `SELMER.md`. |
| Integral Hodge | 56; Laurent Berger, Tong Liu, Mark Kisin, Toby Gee | Annihilators and lengths, NM, tame and range outside Fontaine–Laffaille; novelty. `HODGE.md`. |
| Formalisation | 06-alpoge-verification; Kevin Buzzard | Determine which theorems are formally checked, which axioms or interfaces remain and whether the translation reproduces the mathematical statement. `../08-lean-records.md`. |

## First priority package: characters in 53

Suggested subject: "Request for a check of a splitting identity in a proposed proof of GRH — paper 53".

Attach the source of 53, definitions 671/1732, lemma `pcu:product` 3347–3361, application `pcu:period` 3369–3415 and the report `ERROR-53-CHARACTERS.md`. The audited finding is a quotient of characters α(det g)α(det y)β(det l) between the two printed sides. It is requested to confirm or refute that computation with the full conventions of the manuscript and, if it is confirmed, to state whether there exists a repair that preserves the period and the exact modulus of the exchange scalar.

This package is concrete and can be reviewed before the complete audit of the rest of 53. The absence of a counterexample to the exchange statement does not resolve the defect of its proof.

## Record of external replies

Empty: there are no external replies. When there are, they must be recorded separately from the verdicts of this review, with authorisation of attribution, version reviewed and exact scope. The [corrections inventory](CORRECTIONS-INVENTORY.md) and the [answers matrix](ANSWERS-MATRIX.md) contain the current verdict and its unresolved obligations.


## Text of a request prepared for a specialist

Subject: Request for a focused mathematical review of a theta exchange identity

Dear Professor,

I am seeking a focused review of an identity in paper 53 of the attached series, rather than an endorsement of its claimed GRH conclusion. The accompanying audit identifies a possible decisive error in the character factors of Lemma `pcu:product`, with its downstream use in `pcu:period`.

Using the displayed convention for ω_(α,β), the audit obtains the factor α(det g)α(det y)β(det l) between the two sides. In the subsequent period l is an integration variable, so the missing factor appears to change the period itself. The attached note gives the exact definitions, lines and dependency chain. Could you check that calculation against the full conventions, and assess whether a corrected identity can retain the nonvanishing and absolute constant required later?

A useful response would be: correct as written; incorrect with the first failing inference; or not verified with the specific missing step. The report distinguishes these statuses and includes independently reproduced finite-window certificates. No external expert endorsement is claimed.

Thank you for considering this request.

[Author name and contact information]

This text is a draft message ready to be adapted by speciality, **not a message that has been sent**. The other packages must replace the central question by the corresponding row of the table and attach the specific ledger. It is not advisable to ask all the recipients to certify simultaneously areas foreign to them, nor to send the report as if it were an already validated proof.

## Minimal review package

1. `../FINAL-REPORT.md` and `CORRECTIONS-INVENTORY.md`.
2. The exact version of the relevant manuscript identified in `../evidence/sources.json`, with its appendices.
3. The ledger of the speciality and the notes on its junctions; for exchange, `ERROR-53-CHARACTERS.md`, `COVOLUME.md`, `MAP-53.md`, `CHAIN-53.md` and `AUXCORE-53-54.md`.
4. For the analysis of 46, scripts, outputs and proof of the remainders and of the functional bridge; a log without that proof is not enough.
5. A reply attributable only with the consent of the reviewer, indicating version, statements reviewed and scope. A partial favourable reply must not be turned into a global endorsement.

No completed review by external specialists is available in this audit. The delivery of the dossier does not oblige any of the specialists named to accept it, nor does it provide by itself a certification.
