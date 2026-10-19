# R170_704 — Trial of a flux law at the first contact

Status: identity and sign restriction proved; the
arithmetic law that would exclude the contact is not obtained. This
trial does not introduce a new detector.

## A test object that does use minimality

Assume T is a first full contact: W_T≥0, there exists F≠0 with
W_T(F)=0, and smaller windows have nonnegative form. For `0<h<1/2` we
define the finite quantity
\[
 \mathcal J_h(F)=\frac{W_T(F)-W_{(1-h)T}(U_{1-h}F)}h.
\]
Minimality gives **J_h(F)≤0** for every h, without differentiating the
eigenvector and without imposing additional regularity. Indeed, mere
nonnegativity of W_T, by window inclusion, already suffices; hence this
restriction alone does not distinguish the first contact from other
semidefinite contacts. This limitation of the trial is essential.

Setting `r=1-h`, `v_n=2Λ(n)/√n`, and `P_r(F)` equal to the polar term
of `U_rF`, we have the exact identity
\[
 \begin{split}
 h\mathcal J_h(F)={}&\frac1{2\pi}\int
 [m(\tau)-m(\tau/r)]|\widehat F(\tau)|^2d\tau\\
 &-\sum_{2\le n<e^{2T}}v_n\Re[c_F(\log n)-c_F(\log n/r)]
 +P_1(F)-P_r(F).
 \end{split}
\]
Here all three terms share exactly the same F and the same dilation.
The archimedean term is nonpositive because m increases with |τ|. The
other two terms have no fixed individual sign.

## What inequality would work, and why we have not proved it

A strict conclusion `J_h(F)>0` for some h at every hypothetical first
contact would produce a contradiction. But at that contact such a
conclusion is equivalent to `W_{(1-h)T}(U_{1-h}F)<0`: writing it down
is not proving it. Moreover, an estimate valid for every F cannot
replace a specific law of the arithmetic structure and of the contact
selection.

The direct attempt to use the integer identity gives, with
`q_h(n)=n^{-1/2}Re[c_F(log n)-c_F(log n/r)]`,
\[
 \sum_{n<X}\Lambda(n)q_h(n)
 =\sum_{dk<X}\mu(d)\log k\,q_h(dk),\qquad X=e^{2T}.
\]
This is an exact finite identity from `Λ=μ*log`. It preserves the
interactions, but its terms have both signs. Taking absolute values
loses the needed cancellations, and it does not link the primes beyond
X to the window's selector. Hence this trial does not satisfy the
cross-scale interaction requirement of R169_000 and does not supply a
SpecZ law.

## Honest result of the trial

The local extension R170_703 is indeed a new quantitative theorem
within these notes, derived from the existing certificate. The flux
trial has not produced a new arithmetic inequality. We do not propose
elevating the condition `J_h>0` to an axiom, nor calling it a law, nor
inferring it from unique factorization. A one-sided estimate on the
tail at the frequency chosen by the window is still missing, with the
conditions and hypotheses of R169_000 still pending. The local
continuity bound does not supply that estimate.
