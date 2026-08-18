# D.89 — joint-multiplier prolate split

Let `I=[-T,T]`, let `F` be the unitary Fourier transform, and let the complete
Weil multiplier (archimedean term and every active finite contact together)
be the real function `r`.  Suppose

* `r(tau) >= -M` for all real `tau`;
* `r(tau) >= g > 0` for `|tau| >= R`.

Write

`K_R = 1_I F^* 1_[-R,R] F 1_I`

on `L^2(I)`, and enumerate its eigenvalues
`1 > lambda_1 >= lambda_2 >= ... > 0`.  If `P_K` is the span of its first
`K` eigenvectors and `Q_K=1-P_K`, then every `f` in `Q_K L^2(I)` satisfies

`q_r(f) >= [g-(g+M)lambda_(K+1)] ||f||^2`.

## Proof

By the min--max principle for the positive compact contraction `K_R`,

`<K_R f,f> <= lambda_(K+1)||f||^2`

on the orthogonal complement of its first `K` eigenvectors.  Plancherel
identifies the left side with the Fourier mass of `f` in `[-R,R]`.  Splitting
the multiplier integral into the band and its complement gives

`q_r(f) >= -M <K_R f,f> + g(||f||^2-<K_R f,f>)`,

which is the asserted inequality.  No contact operator is estimated
separately, so the non-compact partial translations cause no off-diagonal
loss.  This proves the lemma.

## The `T=log(5)/2` constants

The directed calculation
`114_d_91_log5_tail_multiplier_arb_verify.py` proves

* `M < 8.315` globally;
* `g > 0.22` for every `|tau| >= 150`.

Consequently it is enough to prove

`lambda_(K+1) < 0.22/(8.315+0.22) = 0.025776...`.

The floating prolate calculation gives `lambda_86 = 1.7175e-6`, far below
the required coarse threshold, and the 86-mode constrained low-block lower
model has least Ritz value `1.2841`.  Those two floating values select a
well-conditioned directed computation; they are not themselves certificates.
