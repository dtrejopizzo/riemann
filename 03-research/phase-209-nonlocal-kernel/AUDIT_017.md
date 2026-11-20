# AUDIT_017 — Virtual metric test and jump source

2026-10-19. Independent check. **PASS / PROVED within the declared
scope.** Reviewed `VIRTUAL_SOURCE_017_METRIC_TEST.md`, with 008, 011,
NODE_001, the entries of the routes index, grid and current crossword.
No additional route is built and Paper47 is not modified.

## 1. Metric and domain

Multiplying by τ is a surjective isometry from the virtual space onto the
L² with weight y^(α−1): the inverse divides by τ>0. The conjugated formulas
for dilation and inversion are correct. Hence G_n is unitary,
J_virt is a unitary involution and J_virt G_n J_virt=G_n^*=G_(1/n).
The Hilbert space has been changed with respect to 008; these claims
do not repair the adjoints in the previous metric nor prove invariance
of its completed arithmetic module.

The bound of §2 is correct. From W_d=m(y)/d−m(d²y)<0 and
0<m(t)≤min(1,t^(-1/2)) one gets
|W_d|≤min(1,(d√y)^(-1)). Integrating its square before and after
y=d^(-2) gives exactly

`[1/α+1/(1−α)]d^(-2α)`, for 0<α<1.

Convergence with the coefficients of 011 follows from the sum of norms
Σd^(-1−α). It is not used to recover an already refuted link.

## 2. Map and energies

The factor 1/√2 of C_α is correct: after y=exp(2x), its virtual norm
becomes exactly the L²(dx) norm. The inverse formula proves
surjectivity. G_n corresponds to F(x+log n) and J_virt to F(−x).

For the extension by zero of the window tests,

`(1/2)||F−F(·+u)||²=||F||²−Re c_F(u)`.

This verifies (4), including the cost A_T. The gamma energy uses the whole
interval u∈(0,∞), with the same positive kernel K as NODE_001/P47.
For u>2T the correlation is zero; its contribution is precisely the
tail κ_T||F||² that appears when writing the formula only up to 2T.
Thus no boundary or tail term is missing. The integral may be
infinite outside the form domain, as the memo warns; on the
gamma domain both expressions coincide.

The finite comb sum includes only n<exp(2T); there is no problem with
n=1 because Λ(1)=0, nor with the endpoint because c_F(2T)=0. The real parts
allow the Hermitian version; on the real carrier they coincide with the
bilinear formulas of NODE_001.

## 3. Total identity and scope of the failure

On the even sector with vanishing cosh moment, Q_T=𝔞_T. Substituting the jump
energy into the gamma formula gives exactly

`Q_T(F)=E_pos^virt(C_αF)−(A_T−C₀)||F||²`.

C₀=ψ(1/4)−logπ<0 and A_T≥0, so the counterterm is strictly
negative for F≠0. This refutes the identification of Q_T with the proposed positive
source and the domination Q_T≥E_pos for this source. It does not
refute Q_T≥0: the positive energy may exceed that cost, but the
test does not prove the necessary inequality. The memo keeps this
distinction correctly.

The virtual representation works for any measurable profile,
finite and strictly positive almost everywhere; in particular
for the theta profiles with finite deletion mentioned. After
C_α, that profile disappears. Hence unitarity and inversion
do not select completeness of the Euler product nor conductor 1. The weights
Λ of the comb are introduced explicitly, and their sign does not by
itself pay the counterterm.

The written difference with respect to 008 is a concrete change of metric
to diagnose that realisation; the final decomposition returns to
the jump and potential energy of P1_BBSTAR/INV_N, as 017 acknowledges.
It is not recorded as a new bridge nor as a reopening of that sign
mechanism. Nor is it a NO-GO for other virtualisations, other
counterterms or a future additional link.

**Verdict:** positive auxiliary source well realised, total identity
correct, source not yet functional for the sign of the node. No new
sign of Q_T nor closure of row D.
