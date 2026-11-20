# POWER_SCHUR_TRIPLES_APPLICATION_099 — Triples of the remainder and five anchored nodes

Status: **PROVED using the audited derivation099 FULL PASS; independent reproduction 8310 exit0/FULL PASS2048 and matching hash.** The exact application of the global datum T_h is made explicit, without turning the auxiliary node0 into an admissible test. Papers untouched.

## 1. Inputs and both curvatures

099 certifies T_h>0 on the slope compact0<u<=512;097 proves it for u>=512 and098 adds the positive value at the origin. The full chain gives T_h(x)>0 for all x>0.089 provides global T_R>0 and086 R''<0. All inputs are from the real Phi, not an abstract inheritance refuted in090.

Use a=M'(0)>0, g(x)=aR(x)−1=xb(x), h=1/b.090 already proves h'>0, g'>0, T_g=a²T_R>0 and all distinct pairs of the kernel G_p positive definite.

For P=p² and x=z², the exact identities of090 are

    R_G(x)=z/G_p(z)=(1/a){(x−P)/[h(x)−h(P)]−Pb(P)},
    S_G(x)=zG_p(z)=a{(x−P)/[g(x)−g(P)]−h(P)}.

The reciprocal secant lemma with INTERIOR anchor now applies to f=h and to f=g: both first derivatives are positive and both T_f strictly positive on the whole half-line. Hence R_G''<0 and S_G''<0 for ALL p,x>0. The point x=P is removable and the lemma gives there H_P''(P)=−T_f(P)/(6f'(P)³)<0. The anchor is not omitted.

082, with PD pairs and both strict concavities, proves that ALL triples of distinct positive nodes of the kernel K_Gp(z,w)=[G_p(z)+G_p(w)]/(z+w) are PD, for ALL p>0. Repeated nodes are grouped. G_p increasing is not required;081 remains valid.

## 2. Exact congruence with two pivots

Extend analytically K_M(u,v)=[M(u)+M(v)]/(u+v) to the node0:

    K_M(0,0)=a, K_M(0,z)=M(z)/z.

Fix p>0,c=M(p)>0,delta=a−c/p>0 and define for z>0,z!=p

    d_p(z)=[zc−pM(z)]/[c(z+p)],
    F1(z)=c[zM(z)−pc]/[zc−pM(z)],
    r_p=c²/delta=pc²/(pa−c)>0.

The formulas075–077 give F1(z)=r_p/z+G_p(z). M(z)/z strictly decreasing implies that d_p(z) has the sign of z−p: it is REAL nonzero, but not always positive. The congruence only needs to be real invertible.

The Schur complement of the diagonal K_M(p,p)=c/p satisfies, by exact algebra,

    S00=delta,
    S0z=−c d_p(z)/z,
    Suv=d_p(u)d_p(v)[F1(u)+F1(v)]/(u+v).

Removing in addition the diagonal S00 produces

    Suv−S0u S0v/delta
       =d_p(u)d_p(v){K_F1(u,v)−r_p/(uv)}
       =d_p(u)d_p(v)K_Gp(u,v).

No signed term was arbitrarily removed: r_p/(uv) is exactly the rank1 paid by the second pivot. The two pivot diagonals c/p and delta are positive.

## 3. Scope of the five nodes

For distinct positive p,z1,z2,z3, the ORIGINAL block of nodes{0,p,z1,z2,z3} is PD: its two previous complements leave a real invertible congruence of the PD G_p triple. Repeated nodes produce the usual redundancy and PSD.

The node0 corresponds to the original exponent1/2 and lies OUTSIDE the W carrier of exponents>1. Hence this does NOT prove five arbitrary admissible generators, nor allow replacing0 by a free positive node without another proof. The four positive nodes of that block were already covered in their admissible range by085. The new result is strict control of the triples of the remainder and of an auxiliary anchored matrix, not new W/T coverage.

It is not claimed that T of the reciprocal data of the remainder is preserved nor that the argument can be repeated to all orders. The next level requires a new input and the global sign remains OPEN. The independent reproduction 8310 of the certificate099 ended exit0/FULL PASS2048 with matching hash.
