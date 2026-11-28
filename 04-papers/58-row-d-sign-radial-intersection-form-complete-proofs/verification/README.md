# Row D verification notebook

`row-d-verification.ipynb` documents the numerical consistency checks and the logical
falsification attempts applied to individual statements of the proof chain of row D:

    Short Forms, Spanning and Covolume Theorems ⇒ main inequality ⇒ one-sided bound
    ⇒ one-sided criterion ⇒ GRH ⇒ RH.

The three theorems are Theorems A, B and C of [Paper 58](../README.md); the statements are
referred to by their labels (`ph:thm`, `au:moment`, …), which are the same in Paper 58 and in
[Paper 46](../../46-row-d-sign-radial-intersection-form/) with its companions (Papers 49–56).

## What it contains

| Section | Contents |
|---|---|
| Scope | What the checks are and what they are not. |
| 2. Map of the chain | The links of the chain and the eight nodes N1–N8 that carry its weight. |
| 3. Falsifiers of the whole argument | Where the argument uses the Euler product (with the Davenport–Heilbronn function as illustration), variations of the argument that would give false statements (K1–K4), the circularity check, the junction of the Short Forms and Spanning Theorems. |
| 4. Numerical tests, node by node | For each test: the statement, the outcome that would have refuted it, the script, its output, and assertions on the output. |
| 5. Results table | Generated from the tests that ran. In the saved run: 39 executed tests passed; 15 rows are illustrations, results recorded only, analytic arguments, or statements not tested. |
| 6. Limits of these checks | The statements that have no numerical test, and why. |

## What it does not show

The checks use small cases: small primes, ranks, degrees and fields. Passing them is evidence
that the tested statements are not wrong in those cases. It is **not** a proof, and it does not
verify the theorems in their actual range, which requires ranks of order $x^5$ and moduli larger
than $b^{20}$. Several statements that carry weight have no numerical test at all, among them the
seesaw identity (N2), the Spanning Theorem itself (N4) and the determinant of the comparison
operator (N6). The falsifier on functions without Euler product is vacuous: the argument cannot
be run on such functions, so it is not "passed".

## Opening in Google Colab

1. Go to <https://colab.research.google.com>.
2. Choose **File → Upload notebook** and select `row-d-verification.ipynb`.
3. Choose **Runtime → Run all**.

The saved notebook contains the executed outputs, so the results can be read without running
anything. The notebook is self-contained: it writes its test scripts to the runtime's disk with
`%%writefile` cells, so no other files are needed.

## Runtime

- Packages: `numpy`, `sympy` and `mpmath`, which Colab provides. The first code cell installs
  any that are missing.
- With the default parameters, a full run takes about 10–15 minutes on a standard CPU runtime
  (536 s in the saved run). No GPU is needed.
- Some tests ran at a larger size in the original verification. The parameter cells
  (`N1_T1_FULL`, `N1_T4_FULL`, `N7C_KS`, `N7C_INT_FULL`) switch to those sizes, which adds several
  minutes. The full-size results are quoted in the notebook.
