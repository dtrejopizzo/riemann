# VIRTUAL_SOURCE_017 — Virtual metric: computed positive source and failure of the link

2026-10-19. **PROVED, audited in AUDIT_017.md:** an explicit modification of the metric removes the adjoint defect of 008 and gives a positive source with a continuous unitary map. When computing the full Q_T, a strictly negative counterterm reappears that this construction does not control. **No functional source of sign for D was obtained.**

## 0. Corpus and written difference before the test

Consulted: the project rules, the ROUTES-TRIED-INDEX index, grid and base crossword `CROSSWORD-TO-D.md`. Relevant entries: CONSTRUCTOR008 (defect b_n of the inversion), INV_T (gauges), INV_N (jump energy and potential), P1_BBSTAR (polarisation and total cost of the comb), norms/Helson and LINK011–016.

**Explicit change with respect to 008:** the algebraic formulas G_n are kept, but the Gaussian metric is changed from `y^(α−1)τ(y)dy` to `y^(α−1)τ(y)²dy`. This allows checking a concrete virtualisation; it is not assumed to be an isometry of the original completion 005/015 nor to preserve its arithmetic link.

An already excluded gauge is not reopened as a proof of sign. The object is computed in order to know whether the change of metric adds a mechanism; at the end its reduction to an already indexed jump decomposition is identified. No novelty is attributed to that decomposition, and no other index, phase or kernel of the node is constructed.

## 1. Virtual space and exact action

Let τ(y)=θ(y)−1>0. For α>0 define

`ℒ_α^virt=L²((0,∞),y^(α−1)τ(y)²dy)`.

Keep, for real n>0,

`(G_nf)(y)=n^α τ(n²y)/τ(y) f(n²y)`.

The operator

`S:ℒ_α^virt→L²((0,∞),y^(α−1)dy)`, `Sf=τf`,

is unitary, and

`SG_nS^(−1)g(y)=n^α g(n²y)`.

The last operator is unitary by change of variable. Thus G_n is unitary in the virtual metric for all n>0 and

`G_n* =G_n^(−1)=G_(1/n)`.

Define

`(J_virt f)(y)=y^(−α)τ(1/y)/τ(y) f(1/y)`.

It is the conjugate by S of `J_0g(y)=y^(−α)g(1/y)`, hence it is a unitary involution and

`J_virt G_n J_virt=G_n*`.                           (1)

All these identities are verified on the full space, not only formally on a collection of profiles.

**Difference from 009:** this continuous group lives in another Hilbert space and with another norm. It neither interpolates nor compresses the actions V_n of the original module via the fixed bounded maps that 009 excluded.

## 2. The metric includes the known profiles

For `ψ_d(y)=q_d(y)−1/d=W_d(y)/τ(y)`,

`||ψ_d||²_virt=∫_0^∞y^(α−1)|W_d(y)|²dy`.

Since `W_d=m(y)/d−m(d²y)<0`, one has

`|W_d(y)|≤m(d²y)≤min(1,1/(d√y))`.

Hence, for 0<α<1,

`||ψ_d||²_virt≤[1/α+1/(1−α)]d^(−2α)`.              (2)

The integral is split at y=d^(−2). In particular the metric is finite on all profiles of the critical case α=1/4. An infinite norm is not postulated as if it were an already realised space.

If the coefficients a_d(F) of 011 were reused, the series `Σa_d(F)ψ_d` would also converge in this norm, because a_d=O_T(||F||/d) and Σd^(−1−α)<∞. Its map would still be smoothing by the same derivative bounds of 011. This only verifies the domain; it is not proposed as a repair of the map closed in 011–016.

## 3. Continuous unitary map: the full carrier can be computed

For F∈L²(R), define

`(𝒞_αF)(y)=2^(−1/2)y^(−α/2)τ(y)^(−1)F((log y)/2)`.

With y=exp(2x),

`||𝒞_αF||²_virt=∫_R|F(x)|²dx`.

It is a unitary map onto all of ℒ_α^virt: the inverse formula is obtained by solving for F. For F supported in [−T,T], its image is supported in [exp(−2T),exp(2T)].

Direct computation gives

`G_n𝒞_αF=𝒞_α[F(·+log n)]`,

`J_virt𝒞_αF=𝒞_α[F(−·)]`.                         (3)

The factors τ and the powers n^α cancel exactly. This is a computed link with the continuous carrier, not an abstract existence of square roots of Q_T.

## 4. Explicit positive source and recovery of the comb

Fix a window T and put `v_n=2Λ(n)/√n`, n<exp(2T), as in Paper46. For `f=𝒞_αF`, define the finite positive energy

`E_prime^virt(f)=(1/2)Σ_n v_n||(I−G_n)f||²_virt`.

By (3) and the norm of a difference of translations,

`E_prime^virt(𝒞_αF)`

`=A_T||F||²−Σ_n v_n Re c_F(log n)`,

`A_T=Σ_n v_n≥0`.                                  (4)

The comb linear in Λ is recovered exactly, together with its constant cost A_T. The source is positive for Λ and for any non-negative selection of those weights; there is not yet a completeness property.

The positive part of gamma can be written in the same space using the group for real n:

`E_Γ^virt(f)=(1/2)∫_0^∞K(u)||(I−G_(exp u))f||²_virt du`,

`K(u)=1/[2sinh(u/2)]+1/[2cosh(u/2)]>0`.

By (3),

`E_Γ^virt(𝒞_αF)=∫_0^∞K(u)[||F||²−Re c_F(u)]du`

`=Levy(c_F)`.

Its domain is exactly the gamma energy domain of Paper46. The infinity of the integral on tests outside that domain is not ignored.

The sign-independent virtual source is therefore

`E_pos^virt=E_Γ^virt+E_prime^virt≥0`.                (5)

## 5. Total identity with Q_T in the polar-free sector

On the even carrier with `∫F cosh(x/2)=0`, the pole of the form of the paper vanishes. Its exact definition is

`Q_T(F)=C₀||F||²+Levy(c_F)−Σ_n v_n Re c_F(log n)`,

`C₀=ψ(1/4)−logπ<0`.

Combining it with (4)–(5) gives the **total** identity, with no omitted remainder,

`Q_T(F)=E_pos^virt(𝒞_αF)−(A_T−C₀)||F||²`.          (6)

The counterterm `A_T−C₀` is strictly positive. Thus the difference between Q_T and the proposed positive source is strictly negative for all F≠0. (5) cannot be used to conclude the sign of (6).

Positivity of the residual energy `E_pos^virt−(A_T−C₀)||F||²` would require an additional inequality coupling the arithmetic jumps with gamma on the restricted carrier. Defining that difference as a «positive source» would amount to assuming the target sign again; **this is not done**.

Identity (6) is the term-by-term polarisation indexed in P1_BBSTAR/INV_N. Here it reappears after computing the virtual metric; it is not presented as a new bridge. In particular the cancellation of b_n in (1) did not reduce the cost A_T of the comb.

Outside the polar-free sector the polar block of the paper must be added. The change of metric does not prove a new identity for that block; it does not follow from the fact that J_virt acts as a reflection.

## 6. Specificity: the virtual sign does not see the complete product

The computations of §§1–3 work when replacing τ by **any measurable, finite, strictly positive almost everywhere function** a(y), using the space `L²(y^(α−1)a(y)²dy)`, S_a f=af and the corresponding conjugated formulas. They also work for τ_P of the finite deletion, which is positive.

After the map 𝒞, all those data cancel and one obtains the same representation by translations and reflection of L²(R). Hence unitarity and identity (1) select neither the FE of conductor 1 nor the complete Euler product.

The only appearances of Λ in (4) are the explicitly introduced weights v_n. Their non-negativity is inherited by the deletion. The counterterm changes with the mass of those weights, but no additional arithmetic sign identity appears that would pay for it.

This is the exact point where the proposed source fails: its positivity and its «virtual duality» are gauge phenomena; the realisation generating the weights of the node contributes no independent control of the negative term in (6).

## 7. Outcome and scope

An explicit virtual source was constructed and computed, positive as a difference energy, with realised space, domain, involution, action and unitary map. The comb and the gamma part were cross-checked via a total identity of the polar-free node.

**Outcome of the test: non-functional source for D.** The change of metric removes an auxiliary adjoint defect but not the cancellation required by Q_T; the exact residue remains the negative potential (6). Impossibility of other counterterms, realisations or sources is not proved; no general NO-GO against every virtualisation is claimed.

Paper46 was not modified, no new phase was opened and this diagnostic is not counted as positive progress on D. The full goal remains OPEN. The investigation was resumed; the recorded status remains `blocked`.
