# L2_BUILD_015 — Prime interactions in the cube: no structural sign; (Q) is ill-posed; reconciliation with Φ

## Corpus check
Paper 46 prop:wit-sens (Rayleigh sensitivity, κ_T), finmod(ii); N_BUILD_005 §2 (partial Euler products a_S fail for large
T), N_BUILD_007/008 (cone order NO-GOs), N_BUILD_009 (Poisson–Euler map Φ, unique nonnegative fixed point Λ);
L2_BUILD_014 (cube). grep "interaction / cross term p^a q^b / Hessian in the weights / second-order perturbation /
mixed difference": R186_008 Thm C ("Λ by logarithmic derivative; additive in S") states additivity of the phase in S;
no memo computes prime–prime interactions of the bottom. §1 is a consequence of R186_008-type additivity; §2–§4 new.

## 1. The form has no prime–prime terms (PROVED)
comb(t) = −∂_s log Π_p Z_p(t_p) = Σ_p comb_p(t_p) (log of a product is a sum; 𝔄_T commutative). Equivalently Λ(p^a q^b) = 0
for a, b ≥ 1: the cross terms n = p^a q^b of Z appear in Z but cancel in −∂_s log Z. Hence 𝔞_T^{(w)} = 𝔞_∞ − Σ_p L_p(w_p),
affine and separately additive in the prime blocks w_p = (w_{p,k})_k. **Multiplicativity contributes no cross term to the
form; there is no structural sign of p^a q^b type to exploit.** All interaction in λ comes from the infimum.

## 2. The interaction is a Gram entry of indefinite sign (PROVED)
Let w ↦ λ(w) near a point where the bottom eigenvalue λ of the self-adjoint operator A(w) = A_∞ − Σ_p L_p(w_p) on P_T is
simple with unit eigenvector h, and let R := (A − λ)^{−1} restricted to h^⊥ (≥ 0, bounded since λ is isolated: discrete
spectrum, 007 §1). Second-order perturbation (Kato, CITED; analytic in finitely many parameters):
  ∂λ/∂w_{p,k} = −v_{p^k} Re c_h(k log p)   (Hellmann–Feynman; L_p(w_p)(F) = Σ_k w_{p,k} v_{p^k} Re c_F(k log p)),
  ∂²λ/∂w_{p,k}∂w_{q,l} = −2 Re⟨R g_{p,k}, g_{q,l}⟩,  g_{p,k} := P_{h^⊥} 𝓛_{p,k}h,
with 𝓛_{p,k} the bounded operator of the form v_{p^k}Re c_F(k log p) (½ v_{p^k}(τ_{k log p} + τ_{−k log p}) compressed to
P_T). The Hessian is −2·(Gram matrix of the g's in the R-metric): negative semidefinite (concavity, 014 A2), and its
off-diagonal entries — the infinitesimal 2-prime interactions I_{p,q} := Σ_{k,l}∂²λ/∂w_{p,k}∂w_{q,l} = −2⟨R g_p, g_q⟩ with
g_p = Σ_k g_{p,k} — have the sign of −⟨g_p, g_q⟩_R, which is not fixed by any structure: for two vectors in a Hilbert space
the R-inner product can have either sign. Example class (PROVED abstractly): if g_q is replaced by −g_q (reverse the sign of
one prime's coupling) the interaction flips; a positive-definite R does not constrain ⟨g_p,g_q⟩_R.
Exact evaluation at T just above ½log 6 (active primes 2, 3, 5) requires h and R, which have no closed form (008 §2):
NOT computable by pen and paper; numerics are excluded here. Sign of I_{2,3}: OPEN.

## 3. The discrete interaction and (Q) (PROVED: (Q) at Hamming neighbours is ill-posed)
Discrete 2-prime Möbius term: Λ̂({p,q}) = λ(1) − λ(1−e_p) − λ(1−e_q) + λ(1−e_p−e_q) (indices relative to the full set).
Rayleigh with the minimizer h at t = 1 (prop:wit-sens argument): λ(1 − e_p) ≤ λ(1) + κ_p, κ_p := Σ_k v_{p^k}Re c_h(k log p),
Σ_p κ_p = κ_T. So deleting a prime with κ_p < 0 lowers the bottom below λ_A(T), and λ_A(T) ≤ 4·10⁹Te^{−15.449T} for T ≥ 1
(cor:margin1): the Hamming neighbours with κ_p < −λ_A are NEGATIVE. Whether such p exists at a given T is not known
(κ_p signs are functionals of h*), but whenever it does, any inequality "λ(1) ≥ Σ (neighbour values) + corrections"
must have corrections carrying more than the whole deficit of the neighbours, i.e. it is the statement λ(1) ≥ 0 itself
in different coordinates. Moreover, by Prop 0 of 013, corrections can be redistributed between the archimedean part and
the prime blocks at will, so no correction term is canonical. Conclusion: (Q) in the form "vertex dominance at Hamming
neighbours" is ill-posed — NO-GO for this formalization (PROVED modulo existence of a κ_p < −λ_A, which is CONDITIONAL;
without it, (Q) is still a restatement).

## 4. Reconciliation with N_BUILD_009 (Φ)
- Cube (014): parametrizes the Euler side — all comb(t) are log-derivatives of Euler products in 𝔄_T; the FE enters only as
  the coefficient-1 point t = 1 (A4).
- Φ (N_BUILD_009): a map on prime-power combs whose fixed points are combs with Poisson self-dual integer comb; the unique
  nonnegative fixed point is Λ.
- They are the same constraint from two sides: on the cube, the fixed-point residual r(comb(t)) = comb(t) − Φ(comb(t)) vanishes
  exactly at t = 1 (by A4 and N_BUILD_009 uniqueness). So {Euler cube} ∩ {Fix Φ} = {Λ} — the identification of crossword I5,
  seen twice. A quantitative link would be: λ(t) ≥ λ(1) − C·‖r(comb(t))‖ (stability of the bottom w.r.t. the Poisson
  residual) — but this bounds λ(t) from λ(1), the wrong direction for (L2). The useful direction would be a lower bound of
  λ(1) by data at points t ≠ 1 where λ is known positive (small windows) — not available, since the cube is at fixed T.
- Joint proposal (OPEN, shared with the track (N)): use T as the second axis. On the product (cube × windows), the known
  positive region contains all t at windows T < 0.58 with no active prime (there λ = λ_{∞,P} > 0, cor:Tarch CITED), and the
  fixed-point locus t = 1 is known positive on {1} × (0, ½log5] (certified, thm:log5A). (L2) is the propagation of positivity along {1} × T.
  The cube adds nothing to that propagation unless an inequality transports positivity from {t ≠ 1} × T to {1} × T.

## 5. Review
- §1: correct and simple; it is the content of "Λ supported on prime powers" (corpus R186_008 Thm C has the same additivity
  for the phase). Labelled PROVED, low novelty.
- §2: requires a simple bottom eigenvalue (generic; not proved for ζ's window); formulas standard (Kato). The "either sign"
  statement is abstract: it shows no structural sign follows from the form's structure; it does not show the actual I_{2,3}
  has either particular sign. PROVED in that reading.
- §3: correct; partly CONDITIONAL. The conclusion that (Q) is a restatement does not depend on the condition.
- §4: reconciliation correct; the "wrong direction" observation is the key negative: the cube/Φ object gives stability AT ζ,
  not positivity OF ζ.
- No sign certified; no negative value of 𝔞_T for ζ.
Verdict: the cube's interaction lever does not exist structurally (no cross terms; interaction = indefinite Gram entry);
(Q) closed as ill-posed. The cube/Φ pair is an identification object; it needs a transport inequality in T to be useful.
