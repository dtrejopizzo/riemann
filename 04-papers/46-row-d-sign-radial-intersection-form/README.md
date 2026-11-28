# Paper 46 — The sign of the radial intersection form on the idele class group

Row D of the Weil-type route over $\mathrm{Spec}\,\mathbb Z$: the index inequality. Papers 43, 44
and 45 give rows A, B and C (correspondences, Frobenius, explicit formula); this paper determines
the sign. It is the main paper of the series: it proves that no Dirichlet $L$-function vanishes
in $\Re s>1/2$, and with it the Riemann hypothesis, from three theorems on integral algebraic
modular forms whose inputs are proved in eight companion papers (Papers 49–56).

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `sign-radial-intersection-form-idele-class-group.pdf` | The paper (55 pages). |

## The paper

The radial trace on the idele class group of $\mathbb Q$ defines a Hermitian form $W_T$ on
functions supported in $(-T,T)$; on smooth tests it equals $\sum_\rho|\Phi_F(\rho)|^2$ over the
nontrivial zeros of $\zeta$.

**The form (Sections 2–11).** The archimedean multiplier, duality and certificates, the explicit
formula on flat-top weights, the two Tate directions, the equivalence of the sign on all windows
with positive semidefiniteness in every degree of one sequence of explicit matrices, and lower
bounds on bounded windows. $W_T\ge 0$ on every window is equivalent to the Riemann hypothesis.
For $T\le\tfrac12\log 5$ the lower bounds on unit vectors are $10^{-18}$ for the complete form
and $2.5\cdot10^{-12}$ for its primitive restriction; a certificate using finite-height zero data
gives an explicit positive lower bound up to $T=2.8022$. This part uses no hypothesis beyond
those stated with each bound.

**The zero-free half-plane (Sections 12–15).** No Dirichlet $L$-function vanishes in
$\Re s>1/2$ (Theorem `thm:GRH-half`). The chain has four links.

1. **A one-sided criterion of Landau type** (Theorem `an:thm-criterion`). For a modulus $q$ and
   an imaginary quadratic field $K=\mathbb Q(\sqrt{-d})$, let $R_q(x)$ be the prime sum over
   $n\equiv 1\pmod q$ weighted by $(1-\chi_K(n))(1/n-1/x)$, minus its main term. If
   $R_q(x)\le x^{\beta-1}$ for all large $x$ and every prime $d$ in a residue class, then no
   $L(s,\psi)$ with $\psi$ modulo $q$ vanishes in $\Re s>\beta$. Proved here, with Landau's lemma
   and Heath-Brown's large sieve for real characters.
2. **Admissible data** (Theorem `an:thm-data`): for every large $x$, scales, a CM field
   $E=K(\zeta_{q_1})$ of degree between $x^{11}$ and $x^{12}$ over $K$, a sparse set of its
   infinite places, weights and three primes. Proved here.
3. **Three theorems** on a lattice of integral algebraic modular forms on a chain of theta lifts
   between unitary groups over $E$:
   - the **Short Forms Theorem**: the lattice contains explicit forms that are integral up to a
     controlled index and short at every conjugate;
   - the **Spanning Theorem**: few translates of them span almost the whole space;
   - the **Covolume Theorem**: no family of almost full rank has covolume plus twice its index
     below a stated bound.

   The paper states them and deduces them from a list of propositions. A table at the end of
   the automorphic section names, for each proposition, the companion paper and the place of
   its proof, and the published results on which it rests.
4. **The main inequality** (Theorem `an:thm-main`), which combines the three theorems and gives
   $R_{q_0}(y)\le y^{-1/2+\varepsilon}$, the hypothesis of the criterion for every
   $\beta>\tfrac12$. Proved here.

**Conclusion (Section 16).** The Riemann hypothesis (Theorem `thm:RH`) is the case of the trivial
character, and with it $W_T(F)=\sum_\rho|\Phi_F(\rho)|^2\ge 0$ on every window
(Corollary `cor:all-windows`): the sign in Weil's programme over $\mathrm{Spec}\,\mathbb Z$.

## The companion papers

| Theorem | Paper | What it proves |
|---|---|---|
| Short Forms | [49](../49-short-forms-theorem-theta-lifts-complex-multiplication/) | The seesaw identity, the bound at every conjugate for CM theta derivatives, their divisibility at every prime; the foundations used in the series. |
| Short Forms | [50](../50-elementary-divisors-edge-hecke-operator/) | Elementary divisors of a scaled Hecke operator at inert primes. |
| Spanning | [51](../51-spanning-theorem-second-moment-poincare-map/) | The second moment of the Poincaré map; equality of multiplicities. |
| Spanning | [52](../52-sieve-systems-siegel-step/) | Sieve systems at the real and finite places; Siegel's step. |
| Covolume | [53](../53-covolume-theorem-exchange-identities-chain-determinant/) | The exchange identity and the determinant of the chain of lifts. |
| Covolume | [54](../54-covolume-theorem-one-theta-lift-hecke-l-values/) | One lift, Hecke $L$-values, test forms of least valuation. |
| Covolume | [55](../55-covolume-theorem-regular-families-of-twists/) | Regular families of twists, Selmer groups, Ribet's method. |
| Covolume | [56](../56-explicit-cup-exponents-local-galois-representations/) | Explicit cup exponents for local Galois representations. |

[Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole
series. [Paper 58](../58-row-d-sign-radial-intersection-form-complete-proofs/) gives row D with
the whole chain in a single volume, and has a notebook of numerical checks and falsification
attempts on the statements of the chain.

## On what the proof rests

The proof of Theorem `thm:GRH-half`, and so of the Riemann hypothesis, is contained in this paper
and Papers 49–56, which rest on published theorems, cited where they are needed. Papers 43, 44
and 45 are not used in that proof; they enter in the reading of the result as an index
inequality.

**Credit.** The mathematics behind the three theorems, and the way from them to the zero-free
half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis and
does not depend on this series. The division of the argument into these three theorems, and
their proofs as written in this series, are the series' way of organising it as mathematics on
paper. The independent compilation of his archive is recorded in
[`../../06-alpoge-verification/`](../../06-alpoge-verification/).

**Status.** Not refereed. There may be mistakes.

**Earlier version.** This folder previously held a version of the paper that took the
arithmetic input directly from the Lean formalization, with an annex (*Column packages for
character families*) and a notebook on bounded windows. They remain in the history of the
repository.

## Building

```
pdflatex -jobname=sign-radial-intersection-form-idele-class-group main.tex
```

three times.
