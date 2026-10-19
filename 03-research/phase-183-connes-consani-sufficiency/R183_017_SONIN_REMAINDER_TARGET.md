# R183.017 — Resume the Sonin comparison, not the determinant

## Source and scope

Connes–Consani, *Weil positivity and Trace formula, the archimedean place*,
https://arxiv.org/html/2006.13771, Theorems 1 and 11 and Lemma 9.
The archimedean inequality compares the energy with a positive Sonin
trace, admitting a correction c|ĝ(0)|². The condition ĝ(0)=0 removes
that correction. The cited theorem has prescribed support: it does not
prove the corresponding inequality for every semilocal set.

This mechanism is not presented as new. The research goal is to
build and estimate its semilocal remainder, including its negative
direction.

## Exact alignment threshold — PROVED, consequence of Lemma 9

Let v,e be unit vectors in a Hilbert space and b,c>0. Set α²=|<v,e>|² and

    R_0 = -b |v><v| + c(I-|v><v|).

There exists a finite nonnegative a such that R_0+a|e><e|≥0 if and only if

    δ=(b+c)α²-b > 0.

In that case the smallest coefficient is a_min=bc/δ.

Proof. If α²=1, a≥b is both sufficient and necessary, in accordance with
the formula. If α²<1, on the plane spanned by v,e the determinant of the
matrix of R_0+a|e><e| is aδ-bc. For δ≤0 it is negative for every a≥0.
If δ>0 and a≥bc/δ, the second diagonal entry is
c+a(1-α²)>0 and the determinant is nonnegative, so the matrix is
positive. Off that plane the operator is cI. This proves both
directions without assuming the sought sign.

## Conditional application to the Sonin remainder

If a semilocal remainder form R_{S,T} is rigorously built, on a Hilbert
space with continuous evaluation g↦ĝ(0), and it is proved from source
data that

    R_{S,T} ≥ -b_{S,T}|v_{S,T}><v_{S,T}|
                 + c_{S,T}(I-|v_{S,T}><v_{S,T}|),

with c_{S,T}>0, the lemma gives a correction on the evaluation at zero
when the vector e representing it satisfies δ_{S,T}>0. On the kernel
of that evaluation, the remainder will be positive. The normalization of e
turns a_min into the coefficient of the squared evaluation.

The cost a_min may grow: the algebraic argument only requires it to be
finite in each instance. But allowing the direction e to change to a
negative eigenvector chosen after diagonalizing is not the same thing:
the fixed vanishing condition used by Connes's proof would be lost.

## Unmet obligations

1. Build the semilocal remainder and its domain with the exact identity
   energy = Sonin trace + remainder, including Gamma and the polar terms.
2. Prove the above bound from Euler–Poisson data. In particular,
   it has not been proved that there is only one negative direction.
3. Prove δ_{S,T}>0 for the fixed evaluation direction, on the supports
   and sets S required by the global inequality.

These are sufficient conditions, not necessary for every proof of D.
Their failure would not exclude a different Sonin comparison. The
algebraic lemma resolves none of these three obligations and is not new
mathematics relative to the cited Lemma 9.

## Crossing with the corpus

R162_301_C1_NONCOMMUTATIVE_EULER_LIFT proves that the anomaly between the
global Hankel root and the local roots has no sign; hence it cannot be
identified with this positive remainder. R166_401_SURVEY_2_OF_3_A,
rows 47–56, records limits on Hardy ports, Sonin range, and local
squares. None of those identities proves obligations 1–3.

Status: archimedean comparison CITED; algebraic threshold PROVED;
construction and estimation of the semilocal remainder OPEN; D OPEN.
