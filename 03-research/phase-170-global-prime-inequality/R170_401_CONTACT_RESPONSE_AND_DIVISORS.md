# R170_401 — Contraction response and divisor coordinates

**Identities and local criterion proved; global sign
OPEN.** Continuation of R170_301, with no external literature search.

The step in this note is to compute exactly what an arithmetic law for
preserving the sign would have to control. It is not assumed that path
interactions are automatically favorable, nor is it claimed that closure
is near.

## 1. Perturbations with fixed support

Fix T and N=ceil(e^{2T})−1. We separate the parameters a_n from their
arithmetic values Λ(n)/√n, allowing test directions on 2≤n≤N. Write

$$H_n=P_T(S_{\log n}+S_{\log n}^*)P_T,\qquad
W(a)=\Gamma_T+m_0I+2|c\rangle\langle c|-2|s\rangle\langle s|
-\sum_{n=2}^Na_nH_n.$$

The operators E(a), C(a) are those of R170_301. For a curve
a_n(ε)=a_n+εd_n, set

$$s_d=\sum_nd_n,\qquad H_d=\sum_nd_nH_n.$$

Then, exactly,

$$\dot E=2s_dI-H_d,\qquad\dot C=2s_dI,\qquad\dot W=-H_d.\tag{1}$$

The directions may include weights of both signs. In a sufficiently
small neighborhood E remains strictly positive, by its coercivity and
because the perturbation is bounded. This suffices for the differential
calculus; it is not claimed that the perturbed weights are Λ.

## 2. Derivative of the gain

Consider a simple differentiable branch of the generalized problem

$$C(a)f=\kappa E(a)f,\qquad\langle E(a)f,f\rangle=1.$$

The nonzero eigenvalues correspond to K=C¹ᐟ²E⁻¹C¹ᐟ² of R170_301.
Differentiating and cancelling the terms with ḟ gives

$$\boxed{\dot\kappa=2(1-\kappa)s_d\|f\|^2+
\kappa\langle H_df,f\rangle.}\tag{2}$$

For a single weight,

$$\frac{\partial\kappa}{\partial a_n}
=2(1-\kappa)\|f\|^2+2\kappa\Re c_f(\log n).\tag{3}$$

At a contact κ=1,

$$\boxed{\dot\kappa=2\sum_nd_n\Re c_f(\log n).}\tag{4}$$

This formula includes the full response of the coupled operator, not
just a path truncation. There is no independent bonus for having added
more paths: at the threshold, its response reduces to (4).

If the eigenvalue is multiple, a derivative is not arbitrarily assigned
to the maximum: the form ⟨(Ċ−κĖ)f,g⟩ compressed to the eigenspace is
used, with the E product. Its eigenvalues give the slopes of the
branches. The criterion in the next section does not require simplicity.

There is no universal sign for Re c_f(log n). If 0<log n<2T, two disjoint
bumps that are translates of one another give opposite signs when
summed or subtracted, by choosing their supports small enough. This
does not claim that both signs occur at a critical witness of Λ; it
does prevent deducing monotonicity using only the translation operator.

## 3. Cancelling the first variation does not preserve the sign

We work conditionally at a contact: W≥0 has compact resolvent,
Z=ker W≠{0}, P is the projection onto Z and Q=I−P. The operator W_Q on
QH satisfies W_Q≥ηI for some η>0. These are the contact hypotheses on
record; we are not claiming such a contact exists for the real weights.

Let D be a bounded self-adjoint operator, for example H_d. Consider
W_ε=W−εD.

**Theorem 1 — Second-order tangency.** If PDP=0 and QDP≠0, then
W_ε is not positive for all sufficiently small ε≠0, of either sign.

**Constructive proof.** Choose f∈Z with QDf≠0, ‖f‖=1, and define

$$g=W_Q^{-1}QDf,\qquad q=\langle W_Qg,g\rangle>0.$$

Since ⟨Df,f⟩=0 and ⟨Df,g⟩=q, an exact expansion gives

$$\boxed{W_\varepsilon(f+\varepsilon g)
=-\varepsilon^2q-\varepsilon^3\langle Dg,g\rangle.}\tag{5}$$

For small |ε| the quadratic term dominates, with negative sign. W has
not been inverted on its kernel: only the inverse on the complement is
used. ∎

**Corollary — Exact two-sided robustness.** Under those hypotheses,

$$[W-\varepsilon D\ge0\text{ for all }|\varepsilon|<\varepsilon_0
\text{ and some }\varepsilon_0>0]
\quad\Longleftrightarrow\quad DP=0.\tag{6}$$

Necessity: testing on f∈Z for both signs forces PDP=0; then (5)
forces QDP=0. Sufficiency: DP=0 and self-adjointness kill the mixed
blocks, and W_Q−εQDQ≥(η−|ε|‖D‖)I.

Along a tangent direction, therefore, the scalar cancellation
Σd_n Re c_f(log n)=0 is not enough. The full vector H_df and its
coupling to the complement must be controlled. This result is a Schur
computation, related to R169_101 §2; no new spectral principle is
claimed.

The corollary does not exclude one-signed perturbations with a strictly
favorable first variation. Nor does it demand robustness for a proof
that only addresses the exact arithmetic point.

## 4. Putting the identities of ℤ into the response

Let λ_n=√n a_n, with λ_1=0. Define the divisor error

$$e_m=\sum_{d\mid m}\lambda_d-\log m,\qquad1\le m\le N.$$

For the genuine data e_m=0. Since Σ_{d|m}Λ(d)=log m, finite Möbius
inversion gives the exact identity

$$\lambda_n-\Lambda(n)=\sum_{d\mid n}\mu(n/d)e_d.\tag{7}$$

If e(ε)=εh, the direction of the normalized weights is

$$d_n=\frac1{\sqrt n}\sum_{d\mid n}\mu(n/d)h_d.$$

Substituting into (4) and rearranging finite sums, on a simple contact
branch one obtains

$$\boxed{\dot\kappa=
2\sum_{d=2}^N\frac{h_d}{\sqrt d}\,
\sum_{k\le N/d}\frac{\mu(k)}{\sqrt k}
\Re c_f(\log d+\log k).}\tag{8}$$

The vector version, relevant for (5), is

$$H_df=\sum_{d=2}^N\frac{h_d}{\sqrt d}
\left(\sum_{k\le N/d}\frac{\mu(k)}{\sqrt k}H_{dk}f\right).\tag{9}$$

This incorporates the exact factorization into the sensitivity of the
operator, without replacing V*V by V² or confusing products with
ratios. The signs of μ are preserved intact.

**Decisive limit.** Imposing e_m=0 for every m≤N determines λ=Λ
uniquely, by (7). A curve preserving all those identities at fixed T is
constant. Hence "propagating the sign by moving within the exact data"
produces no nontrivial direction here. (8)–(9) compute the response to
violating the identities; they do not prove the sign at the point where
all of them hold. Changing T activates other coordinates and requires
further analysis, as in R165_202/R169_101.

## 5. Reproducible test

`verify_contact_response.py` reuses the matrices of R170_301 and checks:

1. (2)–(3) by central differences for all active jumps at T=1 and T=3/2,
   with 48 cells and a simple branch of the finite model.
2. (7) by exact rational arithmetic up to N=30, with test errors.
3. The response to the divisor errors e₂ and e₃ by two independent
   computations: Möbius inversion and eigenvalue difference.
4. (5) in a 2×2 rational example and in an artificial contact of the
   Galerkin model, obtained by increasing a₂. This contact does **not**
   correspond to the weights Λ nor does it constitute a real first contact.

In the two discretizations tested all individual derivatives were
positive. This is a datum of the test, not a theorem about the witness.
At T=1 the artificial contact requires increasing a₂ by approximately
0.000971466. H₃−rH₂ is then combined to cancel the first variation; the
quadratic cost q comes out to approximately 15.4621 and the Rayleigh
test is negative for small perturbations of either sign.

The numbers are in `contact_response_diagnostics.json`. There is no
interval arithmetic and no control of the Galerkin complement; the
certified range of the inequality is not extended.

## 6. Result of this step

The exact response of the contraction, a vector stability criterion at
the contact, and its expression in divisor coordinates were obtained.
The pending step is better delimited: a first-order scalar cancellation
law is not enough; it must also control the couplings to the
complement, or directly supply the sign at the exact datum.

That law has not been built. The global goal and (14) of R170_301
remain OPEN. These checks do not establish that the route will close RH.
</content>
