# POWER_PAIR_OBSERVABLE_SCOPE_100 — Real observable of the J/K pair

Status: **PROVED; final reading and independent audit approved.** See `POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md`. For the REAL positive pair J,K of078, the observable eta=−K'/J is positive on the half-line, starts at0 and returns to0. It does not belong to the class of increasing observables that would allow reusing073 directly. The sign of T_h, the positivity of its kernels, other classes of pairs and the general recursion are not refuted. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked073–078,081,090 and097–099.078 already builds the positive densities J,K.081 already studies F(u)=a/M(u)−1/u=uB(u), proves F>0 and F→0 and excludes inheriting the monotonicity of G_p through a normalized limit. Those results are not presented again as novelty.

The object here is POINTWISE in the time variable: eta(t)=−K'(t)/J(t) for the same real pair. The inequality0<eta(t)<a/t rules out reconstructing the next mean via an increasing observable of this pair. Neither another proof of the obstruction081 nor a NO-GO for all Laplace-pair methods is recorded.

## 2. Definitions and signs already established

Let Phi be the real positive even density, Z its bilateral transform and a=M'(0)>0. Use the EVEN densities of078

    J(t)=int_|t|^infinito sPhi(s)ds>0,
    K(t)=int_|t|^infinito(s−|t|)[aPhi(s)−J(s)]ds>0.

Here K is the even density, not the odd primitive of093/095. One has

    K''=aPhi−J, K'(0)=0,
    Z_J=Z'/u, u²Z_K=aZ−Z_J,
    b(u²)=Z_K/Z_J, h=1/b.

To complete the sign of K', set q=aPhi−J.077/078 prove that tau=J/Phi decreases strictly and that q has one negative/positive crossing. Moreover int_0^infinito q=0, since int J=a int Phi. Hence int_t^infinito q>0 for ALL t>0: after the crossing the integrand is positive; before the crossing the integral is−int_0^t q>0. Thus

    −K'(t)=int_t^infinito q(s)ds>0, t>0.

The boundary terms and the superexponential tails come from the same integrals of Phi and introduce no distributional terms at0.

## 3. Real pointwise inequality and absence of monotonicity

Define

    eta(t)=−K'(t)/J(t).

It is a smooth odd function because K,J are smooth even and J>0. In particular eta(0)=0 and eta(t)>0 for t>0. The formula for K' gives

    −K'(t)=a int_t^infinito Phi(s)ds
                      −int_t^infinito J(s)ds
            <a int_t^infinito Phi(s)ds.

On the other hand

    J(t)=int_t^infinito sPhi(s)ds
           >t int_t^infinito Phi(s)ds, t>0,

with strict inequality because Phi is positive beyond t. Dividing both inequalities by J(t)>0 proves

    0<eta(t)<a/t, ALL t>0.                       (POINTWISE)

Thus eta(t)→0 as t→infinity. No asymptotics, bounds derived from a real remainder, truncations of the arithmetic nor a new certificate were used.

A positive function on(0,infinity) returning to0 cannot be nondecreasing. Nor can eta be nonincreasing on[0,infinity), because eta(0)=0 and eta(t)>0. Hence the REAL observable is not monotone in either of the two global directions. It has at least one interior maximum, without this proving a single maximum or unimodality.

## 4. Exact reconstruction of h and antecedent081

For u>0, consider the positive tilted law with density J(t)exp(ut)/Z_J(u). An integration by parts on the whole line, with vanishing boundary terms, gives

    int_R exp(ut)eta(t)J(t)dt
       =int_R exp(ut)[−K'(t)]dt=uZ_K(u).

Consequently

    E_(J,u)[eta]=uZ_K/Z_J=u b(u²)=a/M(u)−1/u,
    h(u²)=u/E_(J,u)[eta].                          (PAIR-MEAN)

The function on the right is exactly F(u) of081, which was already positive and tended to0. Its lack of monotonicity in the parameter u is not claimed as new. The limited gain of this source is to identify the corresponding time observable and prove POINTWISE, which rules out imposing increasing monotonicity on it.

## 5. Scope for an invariant class

073 uses a mean of the coordinate under a positive law and a conditional comparison of two copies. PAIR-MEAN could motivate repeating that mechanism with eta instead of the coordinate; doing so under the hypothesis that eta were increasing would be incorrect for the real data themselves, by§3.

This does not decide which two-copy comparison could work with non-monotone eta, nor exclude a dual class allowing ascent and descent. Nor is it claimed that the bound a/t is preserved under new Green or secant steps. No closed class for all orders is offered here; that goal remains OPEN.

The global T_h positivity of099 and its consequences, already proved and audited with independent FULL PASS reproduction, are compatible with this pointwise obstruction. No W counterexample is deduced from it and no already proved sign coverage is withdrawn.
