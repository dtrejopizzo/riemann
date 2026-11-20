# POWER_PRIME_TRANSFER_014 — One-pole filter, signed kernel and ordering limit with contact 2

Status: PROVED identities and explicit falsifier of a concrete universal inequality. OPEN transport restricted to the positive arithmetic block V12. No NO-GO is declared for that restriction nor for the global sign. Papers untouched.

## 1. Antecedents and difference

Consulted the project rules, ROUTES-TRIED-INDEX index (N_018, semilocal/exterior E/J, convexity F), grid/crossword recorded in BRIDGE002; memos POLAR_MOVEMENT005, ARITHMETIC_BLOCK007, PRIME_PATTERN008, TATE_CHAIN009, COMMON_TRANSFER010 and the envelope limit013. The Euler/Möbius identities provide no new sign here, and AP monotonicity was already refuted.

The new question is more specific: whether contact 2, which rescues ALL of V12, is favourably preserved when a pole is shifted. Its change is derived jointly with ARCH and POLAR, without assuming that the autocorrelation evaluations are positive. The result identifies the exact signed operator and refutes a stronger universal ordering that would be tempting to use. That refutation is not confused with failure of the problem restricted to V12, whose base is coercive.

## 2. Exact change of the autocorrelation

For v>u=63/2, filter a causal rational function f0 by H(s)=(s+u)/(s+v), keeping the same numerator. Write f_v=Hf0, R0=u²/v². In Fourier,

    |H(i tau)|²−R0=(1−R0)tau²/(v²+tau²).

Let P_v(t)=(v/2)e^(-v|t|), positive kernel of mass one. Its transform is v²/(v²+tau²). By inversion,

    c_fv(t)−R0 c_f0(t)
      =(1−R0)[c_f0(t)−(P_v*c_f0)(t)].                   (C)

Equivalently, the bracket is

    (v/2)∫_0^infinito e^-vs
      [2c_f0(t)−c_f0(t+s)−c_f0(t−s)]ds.

The change is NOT convolution by a positive kernel: its kernel is delta−P_v, of mass zero and both signs. In particular the sign at t=log2 requires control of a second difference of the autocorrelation around the contact; positive definiteness of c does not fix that sign.

## 3. Coupled change ARCH+contact2+POLAR

Define E2[f]=Arch[f]−v2 c_f(log2)+Polar[f], v2=2Lambda(2)/sqrt2=sqrt2 log2, and w2(tau)=m(tau)−v2 cos(tau log2). The moments under the filter are multiplied by H(−1/2),H(1/2), and

    r0−R0=−(1−R0)/[4(v²−1/4)].

Hence one obtains the exact COUPLED identity

    E2[f_v]−R0 E2[f0]
      =(1−R0){(1/2pi)∫w2(tau)tau²/(v²+tau²)|fhat0|²d tau
                        −Polar[f0]/[4(v²−1/4)]}.        (T2)

No terms have been replaced by their norms nor has a polar of assumed sign been separated. A possible coercive transport with constant c uses the same identity with w2−c in the integral and E2−c||·||² on both sides.

For the FULL form the time version replaces the term of contact 2 by

    −Σ(q>=2)v_q[c_f0(logq)−(P_v*c_f0)(logq)].

For each rational function of fixed order, the sums converge absolutely. No supposed pointwise symbol of the infinite sum of cosines is written, since it would not converge in that way. The required signed cancellation lies precisely in these second differences at all contacts.

## 4. Explicit falsifier of the universal ordering E2[f_v]>=R0E2[f0]

The previous ordering is false if asserted for ALL numerators and orders. Use exactly the Tate test of008:

    n=2^17, g_n=y^(n−1)e^-uy/(n−1)!,
    f0=(∂²−1/4)g_n,
    F0(s)=(s²−1/4)/(s+u)^n.

The filter keeps the Tate numerator, so that Polar[f0]=Polar[f_v]=0 for every v>=u. The right derivative of T2 at v=u is

    d/dv [E2[f_v]−(u²/v²)E2[f0]]_(v=u)
      =(2/u)(1/2pi)∫w2(tau)tau²/(u²+tau²)|F0(i tau)|²d tau. (D)

The integral is strictly negative by a rational bound, without matrix or sweep. It is known from008 that m(tau)≤m(0)+17tau² and m(0)<−4. Moreover v2<1 and log2<1; by cos x>=1−x²/2,

    w2(tau)<−4+18tau².

Normalise the measure of the integral D: its density is proportional to

    tau²(tau²+1/4)²/(u²+tau²)^(n+1).

The beta moments of the base probability of denominator (u²+tau²)^(n+1) give, dividing by its second moment,

    E_D tau²
      ≤3u²/n+120u^4/n²+1680u^6/n³
      <3/128+120/128²+1680/128³<1/25.

The exact denominators 2(n+1)−5,−7,−9 are greater than n, and u²<1024, n=128·1024. The weighted denominator was bounded by (1/16)M2, as in008. Thus E_D w2<−4+18/25<0. The integral D has positive mass and is negative.

Consequence: there exists epsilon>0 such that for u<v<u+epsilon,

    E2[f_v]<(u²/v²)E2[f0].                               (FAIL)

A completely explicit value of v is also obtained, without determining epsilon: take v=65/2. The density of the integral of T2 divided by that of D is multiplied by (u²+tau²)/(v²+tau²), between u²/v² and1. Its normalised second moment is therefore less than (v/u)²/25<1/20, since (65/63)²<5/4. Again E w2<−4+18/20<0. Thus FAIL holds specifically for v=65/2: ONE pole has been shifted from63/2 to65/2 keeping the other n−1 fixed and the numerator s²−1/4.

Exactly the proposed universal ordering is refuted. Transport of coercivity on V12 has NOT been refuted: this test has huge order n and E2[f0] is already negative. The hypothesis «positive restricted base» substantially changes the problem and is not covered by FAIL.

## 5. Restricted obligation that remains valid

To obtain a transport step from the positive arithmetic block V12, a concrete sufficient condition would be to prove, for every f0∈V12 and every v>=u,

    (1/2pi)∫[w2(tau)−c]tau²/(v²+tau²)|fhat0|²d tau
          −Polar[f0]/[4(v²−1/4)]>=0,                    (R12)

with c below its certified E2 coercivity. This would use the joint sign of ARCH+contact2+POLAR and not a pointwise envelope independent of the numerator. The identity T2 proves its sufficiency for that step, but R12 is not proved here.

Even solving R12 only for the first movement from V12 does not authorise moving twelve poles successively: after the first step, the base space has changed. A global induction would need a version for the family of intermediate spaces or a joint inequality for a product of filters. This is an explicit additional obligation, not an omitted detail.

## 6. Exact interpretation as the form of the signed correction G

The new identity of SIGNED_TRANSFER014 identifies a more useful structure than a generic ordering. For a single pole, define the causal function G by

    Ghat_L(s)=s F0(s)/(s+v).

Its Laplace transform has numerator divisible by s, so that ∫G=Ghat_L(0)=0. It belongs to a rational space of n+1 poles, with one linear constraint. Moreover

    |Ghat(i tau)|²=tau²/(v²+tau²)|F0(i tau)|²,
    Polar[G]=−Polar[f0]/[4(v²−1/4)].

Hence the full bracket of T2 is EXACTLY E2[G], and the version with ALL contacts gives

    E2[f_v]−R0E2[f0]=(1−R0)E2[G],
    W[f_v]−R0W[f0]=(1−R0)W[G].                          (GAIN)

The convergence already justified allows the second identity without an infinite pointwise symbol. In several movements the product of filters decomposes into the sum of squares |G_j|² of SIGNED014, and the polar contributions follow the same identity by evaluating the rational factors at ±1/2. Thus the full form of each correction is kept, not only its archimedean part.

This clarifies the scope of the falsifier§4: it proves E2[G]<0 for an explicit G of large order, but does NOT prove W[G]<0. Precisely all the contacts that can repair it are missing, as in008. It is no objection to the restricted route with the FULL comb nor is it used as an additional NO-GO.

**Precise route valid for all orders:** prove a signed inequality for W on the rational corrections G_j with numerator divisible by s, keeping all contacts. If nonnegativity is obtained on those restricted spaces for every order, GAIN transports any corresponding nonnegative base bound under pole movements. To transport a coercivity c one uses W[G_j]−c||G_j||² instead of W[G_j]. The current certificates of SIGNED014 solve cases of finite order by means of the restricted archimedean gain; the regime in which that gain also needs arithmetic asks for a new inequality for these SAME corrections.

This route does not omit the base: proving restricted gains for all orders does not by itself prove all initial confluent blocks, whose positivity is still required if one wants to use the density bridge. Nor does it allow inferring full gains from E2 or from each favourable contact. They are exact obligations that can be worked on jointly.

## Result and scope

The exact signed generator of the change of autocorrelation was obtained, its identification as the full form of the correction G, and an analytic refutation of the universal ordering for the PARTIAL comb {2}. The useful target is the inequality on the corrections G_j with ALL contacts. This target is not refuted by the partial counterexample nor by the envelope limits013. No new full arithmetic sign inequality was obtained here.
