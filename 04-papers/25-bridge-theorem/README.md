# The Weil form and the scaling operator: a Pontryagin-index dictionary in zero coordinates

The paper studies the Weil quadratic form Q(f,g) = W(f * g~) on C_c^infty(R_+^*) together with the generator H_C of the unitary scaling action. It writes Q in the coordinates f -> (hat f(rho)) given by the Mellin transform at the zeros of zeta, and uses this to describe the Pontryagin completion of the test space and a Q-self-adjoint extension of H_C when the off-line zeros are finitely many.

What the paper proves:

- Q is Hermitian and invariant under unitary scaling, so H_C is Q-symmetric on test functions (Prop. 4.1, Lemma 4.4).
- Zero-side form: Q(f,g) = sum over zeros of n_rho hat f(rho) conj(hat g(1 - conj rho)); if the off-line zeros form m quartets (Hypothesis D), then the negative index kappa(Q) is at most 2m (Lemma 4.6).
- Under Hypothesis D: kappa(Q) = 2m exactly, ker Q = {f : hat f(rho) = 0 for all rho}, and the completion is l^2 over the critical zeros plus a 4m-dimensional hyperbolic space (Prop. 4.7).
- Under Hypothesis D, H_C extends to a Q-self-adjoint diagonal operator in this completion with real spectrum the ordinates of the critical zeros and with 4m simple non-real eigenvalues i(1/2 - rho), 2m of them in the upper half-plane, so the count equals kappa(Q); J(S) is a core, and M is the unique Q-self-adjoint extension (Prop. 5.3).

All of this is a restatement of Q in zero coordinates: it does not decide whether off-line zeros exist, and nothing about RH is proved. The case of infinitely many off-line zeros is left open. There are no numerical computations.

Known and new: Weil's criterion, the explicit formula (Bombieri's form), Pontryagin's theorem and Connes' trace-formula approach are known. The zero-side description of the completion and of the scaling operator under Hypothesis D, elementary as it is, is the content of the paper; it complements the bound kappa_V <= m on even test functions of Paper 18.

Files:

- [main.tex](main.tex) - LaTeX source
- [bridge-theorem.pdf](bridge-theorem.pdf) - compiled paper (8 pages)
