# Row D verification notebook

`row-d-verification.ipynb` documents the numerical consistency checks and logical falsification attempts applied to individual statements of the paper's proof chain (Theorems A, B, C ⇒ main inequality ⇒ one-sided criterion ⇒ GRH ⇒ RH). The checks use small cases. Passing them is evidence that the tested statements are not wrong in those cases. It is **not** a proof, and it does not verify the theorems in their actual parameter range. The notebook lists every test with its outcome and its limits, including the statements that were never tested.

The saved notebook contains the executed outputs, so you can read the results without running anything.

## Opening in Google Colab

1. Go to https://colab.research.google.com.
2. Choose **File → Upload notebook** and select `row-d-verification.ipynb`.
3. Choose **Runtime → Run all**.

The notebook is self-contained. It writes its test scripts to the runtime's disk with `%%writefile` cells, so no other files are needed.

## Runtime

- Packages: `numpy`, `sympy` and `mpmath`, which Colab preinstalls. The first code cell installs any that are missing.
- With the default parameters, a full run takes about 10–15 minutes on a standard CPU runtime. No GPU is needed.
- Some tests ran at a larger size in the original verification. The parameter cells (`N1_T1_FULL`, `N1_T4_FULL`, `N7C_KS`, `N7C_INT_FULL`) switch to those sizes, which adds several minutes. The full-size results are quoted in the notebook.
