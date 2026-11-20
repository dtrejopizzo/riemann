# POWER_INTERIOR_CONSTRAINT_027 — Real gamma mixture, positive Jensen remainder and curvature direction

Status: PROVED positive representation of the remainder, strict inequality for ARCH_sharp and analytic refutation of global convexity of the complete Gaussian functional. Independent review APPROVED and verifier reproduced. OPEN sign of the interior pairing. Papers untouched.

## 1. Corpus and precise difference

Read the project rules, LOW_TABLE018, TATE_CHAIN009, PACKET_SCOPE009, ARCH_CELL026 and UNIFORM_CUTOFF026; searches for Gaussian/heat mixture/convexity in the ROUTES-TRIED-INDEX index, master grid and crossword. The gamma heat mixture was already used in 018 to prove C_N>0 and C_N'<0: NO novelty is attributed to that known representation. The generic heat trace or semigroup routes are also recorded and are not relaunched.

The specific difference is imposing that REAL mixture on the interior kernel, building a positive weight for its remainder with respect to the Gaussian of equal second moment, and checking the direction of the inequality that Jensen would provide. A genuine inequality is proved, but its direction for ARCH_sharp is UPPER, not lower. For the complete form a signed curvature is identified and a concrete convexity premise is refuted through an elementary bound on a whole range. This refutation is not presented as impossibility of other inequalities for the specific mixture.

## 2. Exact gamma constraint of the real test

Keep u=63/2, N>=2, rho_N(t)=C_N(t)/C_N(0). The heat mixture of 018, normalized, is

    rho_N(t)=E exp(−V_N t²),
    V_N=beta/G, beta=u²/4,
    G~Gamma(b,1), b=N−1/2.                             (MIX)

In particular V_N has positive density

    p_N(v)=beta^b v^(-b−1)exp(−beta/v)/Gamma(b), v>0,
    m_N=E V_N=beta/(b−1)=u²/[4(N−3/2)].

This does not allow choosing an arbitrary mixture to manufacture K: the law is completely fixed by N and u. The normalized density of the Gaussian form with autocorrelation exp(−vt²) corresponds to the norm-one test phi_v(y)=(4v/pi)^(1/4)exp(−2vy²), on the whole line.

If G_W(v)=W[phi_v], then exactly

    W[g_N]/||g_N||²=E G_W(V_N).                         (WG)

The interchange is legitimate piece by piece: the Lévy term after extracting C0 is nonnegative; the comb in magnitude and the polar term too. Tonelli identifies their expectations with those of rho_N=e^-u|t| times polynomial, which are finite because u>1/2. No conditioned formal identity is integrated and no infinite sum is replaced by its regularized value.

## 3. A positive weight INTRINSIC to the remainder of the mixture

Put delta_N(t)=rho_N(t)−exp(−m_Nt²)>=0. It is strictly positive for t!=0 because V_N is not constant and v↦exp(−vt²) is strictly convex.

Define the remainder of hinge functions

    L_N(a)=E(V_N−a)_+−(m_N−a)_+,
    L_N(a)>=0.

Explicitly,

    L_N(a)=∫_0^a(a−v)p_N(v)dv, a<=m_N,
    L_N(a)=∫_a^infinity(v−a)p_N(v)dv, a>=m_N.

Taylor with integral remainder, or the representation of a convex function through hinges, proves

    delta_N(t)=t^4∫_0^infinity exp(−at²)L_N(a)da.        (GAP)

This is an explicit positive weight that preserves the gamma constraint; delta_N(t)/t^4 is completely monotone in t². For N>=3 it has finite mass

    ∫L_N(a)da=Var(V_N)/2
      =u^4/[32(N−3/2)²(N−5/2)].

At N=2 this mass is infinite, but GAP remains valid for t!=0 by Tonelli and the finite first moment. No nonexistent variance is used at that endpoint.

## 4. A strict inequality: the reduction to the variance gives the wrong direction for ARCH_sharp

The normalized sharp form on a Gaussian is

    A_sharp(v)=d_*+∫_0^infinity K_sharp(t)(1−e^-vt²)dt,
    d_*=psi(5/4)−logpi,
    K_sharp(t)=2e^(-5t/2)/(1−e^-2t)>0.

Hence A_sharp''(v)=−∫K_sharp(t)t^4e^-vt²dt<0. Integrating MIX, or directly delta_N>0, yields the strict inequality for the WHOLE family

    ARCH_sharp[g_N]/||g_N||²
      =E A_sharp(V_N)<A_sharp(E V_N).                  (UPPER)

Thus the lemma proposed as a possible aid, «the gamma mixture is bounded BELOW by the Gaussian with equal second moment», is false for ARCH_sharp: strictly the opposite happens. UPPER is a real upper bound, not a lower certificate of the interior deficit. This does not refute a different comparison that also keeps ERR.

## 5. Complete curvature: what is missing after keeping ALL the cancellation

The complete Gaussian form is written, with K(t) the original Lévy kernel,

    K(t)=2e^(-t/2)/(1−e^-2t)=e^(t/2)/sinh t,
    v_q=2Lambda(q)/sqrt(q), C0=psi(1/4)−logpi,

    G_W(v)=C0+∫K(t)(1−e^-vt²)dt
       +4∫_0^infinity cosh(t/2)e^-vt²dt
       −Σ(q>=2)v_q e^-v(logq)².

Its second derivative is

    R(v):=G_W''(v)
      =4∫cosh(t/2)t^4e^-vt²dt
        −∫K(t)t^4e^-vt²dt
        −Σ(q>=2)v_q(logq)^4e^-v(logq)².                 (CURV)

All these integrals and series converge for v>0. GAP and Tonelli for each piece of fixed sign give the exact identity

    W[g_N]/||g_N||²−G_W(m_N)=∫_0^infinity L_N(a)R(a)da. (JOINT-GAP)

The interchange in JOINT-GAP is absolute piecewise: 0<=delta_N(t)<=min(rho_N(t),m_Nt²). The second bound controls the factor K(t)=O(1/t) at 0; the first controls infinity, the polar term and the sum of contacts through the gamma exponential decay. Finiteness of ∫L_N when N=2 is not needed for these interchanges. The polar term is the only favourable contribution in CURV; ARCH and the comb are unfavourable. The positive weight L_N does not by itself turn this signed curvature into a lower bound.

## 6. Analytic falsifier of complete convexity, without pointwise certificates

The hypothesis «G_W is convex on the whole half-line» is FALSE for the original arithmetic form. In fact

    G_W''(v)<0 for ALL v>=65536.                      (FAIL-CONVEX)

Proof. The formula K(t)=e^(t/2)/[2sinh(t/2)cosh(t/2)] and e^(t/2)>=cosh(t/2) imply K(t)>=1/[2sinh(t/2)]. For 0<t<=1 we have sinh(t/2)<=t; for instance, cosh(s)<2 for 0<=s<=1/2 and integration gives that bound. Hence K(t)>=1/(2t). If v>=2,

    −∫K(t)t^4e^-vt²dt
      <=−[1−(v+1)e^-v]/(4v²)<−1/(8v²).

We used (v+1)e^-v<=3e^-2<1/2. For the polar term, cosh(t/2)<=e^(t/2) and t/2<=vt²/2+1/(8v) give

    4∫cosh(t/2)t^4e^-vt²dt
      <=3sqrt(pi)·2^(3/2)e^(1/(8v))v^(-5/2)
      <24v^(-5/2).

The bounds sqrt(pi)<2, 2^(3/2)<3 and e^(1/(8v))<8/7 suffice for the last number. The prime term in CURV is nonpositive and is not omitted with an invented favourable sign. If sqrt(v)>=256,

    R(v)<v^-2[−1/8+24/256]<0.

This proves FAIL-CONVEX on an infinite range of the SAME functional. It is not concluded that JOINT-GAP is negative for the specific law L_N, nor that a finer convex envelope is impossible: the gamma law distributes mass over all a>0 and it must be kept.

## 7. Interior obligation that remains, and scope

MIX and GAP provide additional real constraints on the mass and the exterior sign of K. They allow rewriting the interior as an integral with explicit positive weight L_N, instead of allowing arbitrary K that violate the autocorrelation. But no inequality was obtained making the sum of G_W(m_N) and JOINT-GAP nonnegative.

A valid continuation would have to control one-sidedly the negative part of R AGAINST THIS law L_N, or provide a different joint comparison using its inverse gamma form. Applying Jensen in the wrong direction to ARCH_sharp, or assuming global convexity of the complete functional, does not suffice; both premises are refuted here. Nor is a sign of all combinations of g_N deduced even if all these diagonals were decided.

Recorded as results: the inequality UPPER for all N, the positive weight GAP and FAIL-CONVEX with explicit range. There is no new W coverage nor modification of papers.


## 8. Transfer of the inverse falsifiers to individual Gaussians

**PROVED analytically; mathematical and literal reviews approved.** No novelty is attributed to MIX of §2. The difference with respect to the convexity falsifier of §6 is using the exact LINEARITY of the Möbius inverses, with absolute Fubini, not Jensen nor a comparison between values of W. Targeted dedup in indices/grid/crossword and sources 019–023, 027, 030, 039–040 did not find this corollary made explicit. No new values, computed parameters or certificates.

For a>0 and x>=1 define

 w_a(x)=x^(-1/2)exp[-a(log x)^2],
 H_a(x)=-w_a'(x)=x^(-3/2)exp[-a(log x)^2](1/2+2a log x)>0,
 J_a(x)=sum_(m>=1)mu(m)w_a(mx),
 h_a(x)=sum_(m>=1)mu(m)mH_a(mx),
 K_a(x)=J_a(x)+x h_a(x).

For each a>0 and x>=1 the series are absolute: the Gaussian in log m dominates any power of m and the polynomial factors in log m. Thus COMPLETE INVERSES are considered, not prefixes. The functions in a are measurable via their partial sums.

The FIXED positive law V_N of §2 gives w_N(x)=E w_(V_N)(x), where w_N=x^(-1/2)rho_N(log x). For N=128 or 129, E V_N is finite. Differentiating under the expectation is legitimate for x fixed in a compact subset of [1,infinity): the derivative is dominated by C(1+V_N), integrable. Then

 H_N(x)=E H_(V_N)(x).

To pass to h at x1, first apply Tonelli to NONNEGATIVE terms:

 E sum_(m>=1)|mu(m)|mH_(V_N)(m)
 <=sum_(m>=1)mH_N(m)<infinity.                        (ABS-H)

The last sum converges because H_N(m)=m^(-33)A_N(log m), A_N a finite polynomial. Analogously,

 E sum_(m>=1)|mu(m)|w_(V_N)(m)
 <=sum_(m>=1)w_N(m)<infinity,                         (ABS-J)

since w_N(m)=m^(-32)P_N(log m). Absolute Fubini, with ALL the signs of mu, proves

 h_N(1)=E h_(V_N)(1),
 J_N(1)=E J_(V_N)(1),
 K_N(1)=E K_(V_N)(1).                                (INV-MIX)

Now the previous complete results are reused exactly, without recomputing them:

 POWER_INVERSE_INTERIOR_022: h_128(1)<-33/50<0,
 POWER_CUMULATIVE_TEST_023: K_129(1)<-1/251<0.

If h_a(1) were nonnegative for ALL a>0, its expectation under the law V_128 could not be negative. By INV-MIX there is therefore a_h>0 with h_(a_h)(1)<0. The same argument under V_129 gives a_K>0 with K_(a_K)(1)<0.

The parameters a_h and a_K may be DIFFERENT. Neither has been computed, nor has it been proved that one Gaussian has both signs. The two UNIVERSAL Gaussian hypotheses h_a(x)>=0 and K_a(x)>=0 for all a>0, x>=1 are refuted, each already at the point x1. An existence statement in the Gaussian family is not deduced from a prefix: it uses the COMPLETE gamma certificate and the absolute interchange of the real law.

No negative ERR, negative W or negativity of the arithmetic heat kernel H_A-P of E101036 is inferred. Nor is the Stieltjes representation of N(x) refuted. The signed budgets of 022–024 remain legitimate goals; what is refuted are those two premises of uniform inverse positivity. The complete Gaussian form and its sign are not the transferred functional here. Papers untouched.
