# AUDIT_006 — FE of Π and self-duality defect

2026-10-18. Initial and final review of CONSTRUCTOR_006. No parallel candidates were built. Full target D active.

**Verdict: PROVED the FE identities and the deleted self-duality defect, with a precision of scope on non-Hankel noted at the end. Q_T link OPEN.**

## 1. Corpus and scope of the round

Consulted: index (Tate/Poisson, SPEC005, R11_2_ORIGIN, INV_C/V, Mellin transport audits) and the 209 constructions. The new reason is kept: compute the EXACT transformation of the already built kernel Π and ask about its link to the node, without swapping it for a favourable Gram. The self-dual mass m=c−τ is classical; do not present it as a second new bridge.

Sending coefficients by Möbius inversion is not reopened as a sign route: proving PSD of a finite pushforward of a PSD form is a generic norm. To enable a new link one must explain the difference with respect to P1 and the indexed attempts, besides proving equality with terms of Q_T.

## 2. FE formula for W_d

Let W_d(y)=τ(d²y)−τ(y)/d. Then

    Π_α(d,e)=∫_0^∞ y^(α−1)W_d(y)W_e(y)/τ(y)dy.

Poisson gives exactly

    W_d(1/y)=√y/d [θ(y/d²)−θ(y)]−(1−1/d).

**PROVED:** τ(d²/y)=√y θ(y/d²)/d−1 and τ(1/y)/d=√y θ(y)/d−1/d. Subtract. The constant term is negative with the indicated sign. It is not lost when excluding the origin; it is precisely the origin correction.

The FE transforms integer scales d² into fractional scales d^(−2). To turn this identity into a closed transformation of Π one must keep those scales, their denominators and all cross terms; not only the homogeneous part. No sign of Π results from ignoring the constant terms.

## 3. Classical missing mass and deletion test

For m(y)=c(y)−τ(y), the integral comparison of the Gaussian gives m>0 and Poisson implies

    m(1/y)=√y m(y).

It is a precise self-dual positive object, but prior to this round. Its Mellin is −Z_α on 0<α<1/2. This proves the normalisation of the auxiliary; it does not by itself produce the archimedean part of Q_T.

For squarefree P>1, τ_P=Σ_{a|P}μ(a)τ(a²y), δ_P=Π_{p|P}(1−1/p), m_P=δ_P c−τ_P. Since Σμ(a)=0,

    τ_P(1/y)=√y Σ_{a|P}μ(a)/a ·θ(y/a²).

This is the specific defect of the FE: coefficients 1/a and fractional scales appear simultaneously. That dual sum cannot be replaced by τ_P(y) or θ(y) without an additional identity.

In particular,

    m_P(y)=O_P(c(y)exp(−c_P/y)) as y↓0,
    m_P(y)~δ_P c(y) as y→∞,

because the constant of τ_P cancels at zero and τ_P decays exponentially at infinity. Thus

    m_P(1/y)−√y m_P(y)→−δ_P≠0 as y→∞.

The self-duality of m breaks exactly under this deletion. This is compatible with the kernel −R^P keeping PSD after integration: positivity and self-duality are distinct properties and one must not be confused with the other.

## 4. What can and cannot be concluded

The previous defect locates an identity that fails for a falsifier. It does not yet prove that this identity supplies the sign of Q_T; separation is not domination of the gamma deficit. The rank one of (5)/(7) is also not identified with the cosh polar part by analogy.

The next review must require an explicit map and domain, quadratic degree, justified interchanges/limits, and term-by-term correspondence. If only an FE for the auxiliary is obtained, record it as a structural identity. If there is no link yet, do not close the target nor turn an internal equivalence into a reason to abandon.

Final review pending CONSTRUCTOR_006.

## 5. Final review of CONSTRUCTOR_006

§§1–4 approved in their identities and signs:

- 0<m<1, m(y)=y^(−1/2)m(1/y), τ(1/y)=√y(1−m(y)): correct. The first bound comes from strict integral comparison and the second from Poisson.
- W_d=m/d−m(d²y): exact cancellation of the profile c. Inversion yields W_d(1/u)=√u[d^(−1)](m(u)−m(u/d²)). Dividing by τ(1/u), the Jacobian leaves u^((1/2−α)−1)/(de). α=1/4 is a fixed point of the parameter of THIS identity.
- The direct formula with τ carries −(1−1/d); it coincides with the θ formula because the constants inside the difference cancel. There is no omission of the origin.
- For P>1, m_P^∨=−Σ_{a|P}μ(a)τ(y/a²)/a. The term δ_P cancels with Σμ(a)/a=δ_P. The formulas Δ_P and their limits δ_P at zero and −δ_Pc at infinity are correct. The dual representation of Π_P keeps δ_P−m_P^∨>0 and is a Gram matrix; it requires no sign of m_P or of m_P^∨.
- The discrepancy of profiles is real and not identically zero. The equality of a forward/backward profile is lost; this does not prove that any part of the defect has the sign required for Q_T.

**Precision of scope §3:** the formula for Π keeps two scales separately. That does not by itself prove that the INTEGRATED kernel Π_α differs from every function w(de) for a fixed α; an integral may collapse dependencies. Theorem 3 of CONSTRUCTOR004 is about A_α, not about Π_α in isolation. The sentence was flagged for adjustment. It does not affect any FE identity.

The rejection of the finite Möbius pushforward is understood as a filter of the concrete class of convolutive symbols of P1, not as a new NO-GO for every linear map towards the auxiliary. Such a map could have content if its specific link is built; its abstract existence or its PSD is not enough.

§§5–6 correctly keep as pending the continuous domain map, degrees, lcm/quotients, gamma, pole, tails and all modes. The self-duality of m is an explicit classical object; its action on Π is computed, but does not by itself constitute the second bridge sought. **FE and defect proved; target D active and not closed.**
