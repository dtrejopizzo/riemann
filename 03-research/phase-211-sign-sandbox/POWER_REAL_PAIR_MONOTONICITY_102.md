# POWER_REAL_PAIR_MONOTONICITY_102 — Strictly decreasing real time quotients

Status: **PROVED analytically using075/077/078/089; independent audits approved.** See `POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md`. No new certificate is required. (K/J)'<0 and (Psi_p/D_p)'<0 are proved for all p,t>0. Preservation after new reductions, new W generators and all orders are not proved. Papers untouched.

## 1. Consultation and precise difference

Read the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked075/077, appendix078 of STATE077, POWER_THETA_DENSITY_TRANSPORT_089.md,099 and100. The additional literal search for `Psi_p/D_p`, `Ψ_p/D_p`, `K/J`, `K_even/J`, `K−rJ` and `J,Phi,J` in the three indexes and the POWER corpus of phase211 did not find this result.

075 already builds the positive denominator D_p;077 already controls the crossing of the defect J-beta D_p and pays the positivity of the remainder. That is not presented again as an advance.100 proves that eta=-K'/J is not monotone. Here the objects are different: the TIME quotients of two positive densities K/J and Psi_p/D_p. Their monotonicity is obtained from the specific data077 and089 by means of Rolle with the boundary conditions; pointwise properties of densities are not inferred from their transforms.

The additional specific tool extracted from089 is a Chebyshev system of four EVEN densities, differentiating towards the odd system already proved there. The pair of075/077 is kept intact and its data are not replaced by generic hypotheses on potentials like those falsified074/101.

## 2. Definitions, normalisations and boundary conditions

Phi is the real positive even density; V=-log Phi and Z(z)=int_R Phi(t)exp(zt)dt. Define

    M(z)=Z'(z)/Z(z), a=M'(0)>0,
    J(t)=int_|t|^infinito s Phi(s)ds,
    tau(t)=J(t)/Phi(t).

075/077 prove tau'<0 for t>0. Also tau(t)->0: integration by parts077 gives

    J(t)=t Phi(t)/V'(t)
       -int_t^infinito [sV''(s)-V'(s)]Phi(s)/V'(s)^2 ds,

so 0<tau(t)<t/V'(t)->0. V'>0 and V'(t)/t->infinito are used.

The EVEN density K of078/100 is

    K(t)=int_|t|^infinito (s-|t|)[a Phi(s)-J(s)]ds>0,
    K''=a Phi-J, K'(0)=0.

It is not the odd primitive of093/095.

For each p>0 fix

    c=M(p)>0, beta=a p^2/(ap-c)>0,
    lambda=p^2 c/(ap-c)=p beta-p^2>0,
    D_p=Phi_p of075.

075 gives D_p>0, even, and the exact equation

    D_p''-p^2D_p=c Phi-pJ.                          (D-EQ)

077 gives a unique negative/positive crossing, zero mass and parity of the defect

    Q_p=J-beta D_p, int_0^infinito Q_p=0.

Define

    Psi_p(t)=int_|t|^infinito (s-|t|)Q_p(s)ds.

The tail integral int_t^infinito Q_p is strictly positive for t>0: after the crossing the integrand is positive; before the crossing it is -int_0^t Q_p>0. Thus Psi_p'<0 on t>0 and Psi_p(infinito)=0 imply Psi_p>0. Moreover

    Psi_p''=J-beta D_p, Psi_p'(0)=0.                (PSI-EQ)

The even extension is smooth: Q_p is even smooth and the first boundary term is zero. The equations show the coincidence of all derivatives at0. The functions used are real analytic; in particular no nonzero combination has a null interval or roots of infinite order.

All these densities and all derivatives used decay faster than any exponential. For Phi these are the theta tails already established; for J it follows from J'=-tPhi; for D_p, from075 and D-EQ, which propagates the control to higher derivatives; for K and Psi_p, from their tail integrals and their second-order equations. All boundary terms weighted by cosh(pt), sinh(pt) that follow are therefore zero.

To fix the normalisation with respect to the original remainder, if Z_D,Z_Psi denote the two-sided transforms of D_p,Psi_p, then

    z^2 Z_Psi(z)=Z_J(z)-beta Z_D(z),
    G_p(z)=c z Z_Psi(z)/Z_D(z).

These are the same equations075/077, without changing the remainder G_p or suppressing a signed term.

## 3. Rolle lemmas with multiplicities and boundary conditions

The following counts are on the OPEN interval (0,infinito). They do not count the possible root at0. They apply to analytic functions not identically zero and to any finite list of their roots; hence they also exclude infinitely many roots if a finite bound on the derivative prevents it.

**One-endpoint lemma.** If h(infinito)=0 and h has m positive roots counted with multiplicity, then h' has at least m positive roots, provided h is not identically zero on the tail. Indeed, the multiplicities at the roots contribute m-k roots of h' for k distinct roots; Rolle between them contributes k-1. After the last root there is an additional root of h': choosing a later point with h different from0 and using that h returns to0 at infinity forces an interior extremum. Total m. The argument can be done on compact intervals choosing a sufficiently distant right endpoint.

**Lemma D2.** If moreover h'(0)=0 and h'(infinito)=0, then h'' has at least m+1 positive roots. Applying the previous lemma to h gives at least m positive roots of h'. Their multiplicities and the intervals between them, including the interval from the zero h'(0)=0 to the first one, contribute m positive roots of h''. The return of h' to0 at infinity contributes one more. For m=0, if that version is needed, the two boundary conditions h'(0)=h'(infinito)=0 and h' nonzero equally force an interior extremum. In our contradictions m>=2 is used.

**Lemma Lp.** For p>0, let Lp h=h''-p^2h. If h is even, all relevant functions have superexponential decay and h has n positive roots, then Lp h has at least n+1 positive roots. Put

    g=h/cosh(pt), T=cosh(pt)^2 g'
      =cosh(pt)h'-p sinh(pt)h.

g has the same roots and multiplicities as h. The one-endpoint lemma gives at least n positive roots of g' and of T. By parity T(0)=0; by the boundary conditions T(infinito)=0. The same count from0 and towards infinity gives at least n+1 positive roots of T'. Finally

    T'=cosh(pt)[h''-p^2h].

The factor cosh is strictly positive, so it does not change roots or multiplicities. There is no exception with g' or T identically zero: that would give h constant times cosh(pt), incompatible with the decay unless h=0.

In particular, if F is even and superexponential and has m>=2 positive roots, then

    F'' has at least m+1 positive roots,
    Lp(F'') has at least m+2 positive roots.    (GAIN)

## 4. Quotient K/J: proof from the real valley077

077 proves for the REAL Phi that

    R(t)=[V'(t)+tV''(t)]/[-tau'(t)]

is strictly increasing and infinite. To count multiplicities one can use the more precise conclusion R'(t)>0, which comes from the same proof TAIL-AVERAGE077: if R^-1 is the tail average of L under the strictly positive density w, with L strictly decreasing, then

    (R^-1)'=w(t)[Avg_tail L-L(t)]/int_t^infinito w<0.

Thus R'>0 for t>0 without a new certificate.

Fix r>0 and H_r=K-rJ. Since J''=(tV'-1)Phi,

    H_r''=-r Phi B_(1/r),
    B_l(t)=tV'(t)-1+l[tau(t)-a],
    B_l'=(-tau')[R-l].                             (VALLEY)

Each B_l is strictly increasing or has a unique interior minimum. At a critical point, B_l''=(-tau')R'>0. Hence B_l has at most two POSITIVE roots counted with multiplicity: two simple ones or a double one at the minimum, or fewer. The possible root at0 is not counted and does not affect the argument. B_l is not identically zero, because R is strictly increasing.

Hence H_r'' has at most two positive roots. Lemma D2 implies that H_r cannot have two positive roots counting multiplicity.

Let rho=K/J>0. If rho'(t0)=0 at t0>0, choosing r=rho(t0)>0 would give H_r(t0)=H_r'(t0)=0, that is a root of multiplicity at least2. This is impossible by the previous bound. Hence rho' does not vanish.

Its direction is fixed by a time bound, not by its transforms. Write A0(t)=int_t^infinito Phi(s)ds. Convexity of V gives, for x>=t and y>=0,

    Phi(x+y)<=exp[-V'(t)y]Phi(x),
    A0(t+y)<=exp[-V'(t)y]A0(t).

Positive Fubini implies

    int_t^infinito(s-t)Phi(s)ds
       =int_0^infinito A0(t+y)dy<=A0(t)/V'(t).

By the definition of K and positivity of J,

    K(t)<a int_t^infinito(s-t)Phi(s)ds,
    J(t)>t A0(t).

Thus

    0<rho(t)<a/[tV'(t)] ->0.                       (K-TAIL)

rho' is continuous and never zero, so it has constant sign. Positivity and the limit0 exclude the positive sign. We conclude

    (K/J)'(t)<0 for EVERY t>0.                     (K-RATIO)

This is compatible with100: eta=-K'/J is another observable and is not monotone.

## 5. Four even densities controlled by089

089 proves that the odd system

    [tPhi,-Phi',(tPhi)'',-Phi''']

is extended Chebyshev of dimension4 on (0,infinito): every nontrivial combination has at most three roots counting multiplicities. See the order [1,B,A,C] and its four initial positive Wronskians in POWER_THETA_DENSITY_TRANSPORT_089, section2. Multiplying by tPhi>0 preserves the counts.

Consider now the EVEN system

    [J,Phi,J'',Phi''].                             (EVEN4)

Its derivative is

    [-tPhi,Phi',-(tPhi)'',Phi'''],

which differs from the previous odd system only by factors -1 in the columns. A combination with coefficients not all zero cannot have identically zero derivative, by the independence of the odd system. Nor can it itself be identically zero.

If such an even combination had four positive roots counting multiplicities, the one-endpoint lemma, using its limit0 at infinity, would force at least four positive roots of its derivative. This contradicts089. Hence every nontrivial combination of EVEN4 has at most three positive roots counting multiplicities. No determinant sign unnecessary for the argument is claimed here.

## 6. Quotient Psi_p/D_p for ALL pivots

Fix p,r>0 and define F_r=Psi_p-rD_p. Using D-EQ and PSI-EQ,

    F_r''=(1+rp)J-rcPhi-(beta+rp^2)D_p.

Applying Lp and keeping all contributions gives exactly

    Lp(F_r'')
      =(1+rp)J''+(p beta-p^2)J-rcPhi''-beta cPhi. (FORCING4)

The coefficient of J'' is 1+rp>0. By the independence of EVEN4, FORCING4 is not identically zero and has at most three positive roots counting multiplicities. In particular F_r and F_r'' are not identically zero either.

If F_r had two positive roots counting multiplicities, GAIN would force at least four of Lp(F_r''), a contradiction. Hence F_r has at most one simple positive root.

Define rho_p=Psi_p/D_p>0. If rho_p'(t0)=0 at some t0>0, taking r=rho_p(t0) would give F_r(t0)=F_r'(t0)=0, a forbidden double root. Thus rho_p' never vanishes.

To determine the sign fix p and choose t large enough that tau(t)<=c/(2p). Since tau decreases, on the whole tail s>=t one has

    cPhi(s)-pJ(s)>=cPhi(s)/2.

The anticausal representation of075 and sinh(px)/p>=x for x>=0 give

    D_p(t)=(1/p)int_t^infinito sinh[p(s-t)]
                       [cPhi(s)-pJ(s)]ds
           >=(c/2)I(t),
    I(t)=int_t^infinito(s-t)Phi(s)ds>0.

On the other hand, using PSI-EQ and its boundary conditions,

    Psi_p(t)=int_t^infinito(s-t)[J(s)-beta D_p(s)]ds
             <=int_t^infinito(s-t)J(s)ds
             <=tau(t)I(t).

Thus, for each fixed p,

    0<rho_p(t)<=2tau(t)/c ->0.                     (PAIR-TAIL)

Continuity and non-vanishing of rho_p', together with positivity and limit0, force the negative sign. We conclude

    (Psi_p/D_p)'(t)<0 for ALL p,t>0.             (PAIR-RATIO)

No limit in p has been taken, no transforms interchanged nor an inversion of total positivity assumed. The proof holds directly for each p>0.

## 7. Scope and preservation still pending

K-RATIO and PAIR-RATIO are strict time properties of the real positive densities already built; their proof uses the real valley077 and the fourth comparison of densities089. They are not a consequence of mere positivity of two transforms.

The property PAIR-RATIO controls the pair obtained after the first regularised step. Corollary§8 already builds the positive denominator of the new reduction. Still missing are the positive numerator of another pair, its monotonicity and the comparisons of four densities needed to repeat the count. Such a closure is not claimed, nor that monotonicity by itself pays matrices of all orders.099 remains in force; no new W/T coverage, five arbitrary generators nor the global sign are obtained here.

This result requires only analytic deductions from already audited sources. No quadrature, campaign or new certificate was run and no paper was modified. The entries of the three indexes were updated after the approved independent audit.

## 8. Corollary: positive denominator of the next step and exact remaining obligation

Status of this added corollary: **PROVED analytic; independent audits of the extension approved.** The additional search for `dA-qB`, `d A-q B`, their variants with typographic minus sign and `ZB/ZA` in the three indexes and the POWER corpus did not find this application; only102 contains the new pair. The Green mechanism with one crossing and balance is the one already proved075, applied here to ANOTHER pair thanks to PAIR-RATIO. The abstract mechanism075 is not presented as new.

Fix p>0 and, only in this section, write

    A(t)=D_p(t), B(t)=Psi_p(t), rho(t)=B(t)/A(t),
    ZA(z)=int_R A(t)exp(zt)dt, ZB(z)=int_R B(t)exp(zt)dt,
    F(z)=z ZB(z)/ZA(z)=G_p(z)/c,
    aF=F'(0)=ZB(0)/ZA(0)>0.

Both densities are even, positive and superexponential; rho'<0 on t>0, rho(infinito)=0. For z>0, ZB/ZA is the average of rho under the probability of density A(t)cosh(zt) on t>=0. Differentiating this average gives exactly

    (ZB/ZA)'(z)=Cov_z[rho(T),T tanh(zT)]<0.

Strict negativity is proved with two independent copies: rho decreases strictly and t tanh(zt) increases strictly; the product of their differences has negative sign off the diagonal, which has probability zero. The moments and differentiations are paid by the supertails. In particular, for any q>0 and d=F(q)>0,

    0<d/q=ZB(q)/ZA(q)<aF,
    q aF-d>0.                                     (F-GAP)

Also 0<d/q<rho(0): it is a strict average of rho under a positive density on the whole half-line. Since rho is continuous, strictly decreasing and tends to0, there exists a unique b>0 where rho(b)=d/q. Hence the even weight

    h(t)=d A(t)-q B(t)=q A(t)[d/q-rho(t)]

has a unique negative/positive crossing on the half-line. By the definition of d,

    int_0^infinito cosh(qt)h(t)dt=0.               (BALANCE2)

Define the new even density

    E(t)=(1/q)int_|t|^infinito sinh[q(s-|t|)]h(s)ds.

For t>=0, the weight

    w_t(s)=sinh[q(s-t)]1_(s>=t)/cosh(qs)

is continuous and nondecreasing, and strictly increasing on s>t, with derivative q cosh(qt)/cosh(qs)^2. Multiplying the signed measure cosh(qs)h(s)ds by w_t(s)-w_t(b), the integrand is nonnegative on both sides of the unique crossing and strictly positive on a tail. BALANCE2 eliminates the constant term, exactly as in075. Thus

    E(t)>0 for EVERY real t.                      (NEXT-DENSITY)

Differentiation under the integral and BALANCE2 give

    E''-q^2E=d A-qB, E'(0)=0.

The even extension is smooth, without a delta at0, and E and its derivatives decay superexponentially. Integrating by parts on the whole line gives the entire identity

    ZE(z)=[d ZA(z)-q ZB(z)]/(z^2-q^2),
    ZE(0)=[q ZB(0)-d ZA(0)]/q^2>0.                (NEXT-TRANSFORM)

The values at z=+-q are removable by this identity. In particular ZE(z)>0 at every real z. For the denominator of the next Schur,

    z d-q F(z)=z(z^2-q^2)ZE(z)/ZA(z).              (NEXT-DENOM)

It has not been claimed that E is a logarithmic derivative nor that positivity of ZE proves the sign of the next remainder.

To make precise what is missing, the Schur transform of F anchored at q is

    F1(z)=d[zF(z)-qd]/[zd-qF(z)]
         =(d/z)[ZB(z)/ZE(z)-q].

The second equality uses z^2 ZB-q d ZA=(z^2-q^2)(ZB-q ZE). Its residue at0 is positive and exactly

    r_q=q d^2/(q aF-d)
       =d[ZB(0)/ZE(0)-q]>0.                       (NEXT-RESIDUE)

Removing that pole leaves

    R_next(z)=F1(z)-r_q/z
      =(d/z)[ZB(z)/ZE(z)-gamma],
    gamma=ZB(0)/ZE(0)>0.                          (NEXT-REST)

The NEW crossing obligation is that of the even weight

    U(t)=B(t)-gamma E(t), int_R U=0.

If a unique negative/positive crossing of U were proved, the same tail argument would build a positive density Xi with Xi''=U and even boundary conditions, and then R_next(z)=d z ZXi(z)/ZE(z). That crossing has NOT been proved here. The already established monotonicity of B/A is not replaced by the still unknown monotonicity of E/B nor by another unproved comparison.

Finally, to keep the original normalisation G_p=cF, if e=G_p(q)=cd, the forcing of the denominator is eA-qcB=c h and its positive density is cE. The original Schur transform is G1=cF1, its residue is c r_q and its regularised remainder is c R_next. All these factors are positive. The Green argument of this corollary proves the next denominator and its residue, keeping the explicit obligation on U. By ITSELF it does not prove the sign of the new remainder. The following complement does prove that sign using the ADDITIONAL input099; it does not prove indefinite preservation, new W/T coverage nor all orders.


### Complement with099: sign of the transformed remainder, including the removable point

Status: **PROVED using099 in addition to§8.** The sign of a real transform is not confused with a positive inverse density.

For F=G_p/c,099 proves PD pairs and strict concavity on x>0 of the two data

    R_F(x)=sqrt(x)/F(sqrt(x)), S_F(x)=sqrt(x)F(sqrt(x)).

F=zZB/ZA is odd analytic at0 and aF=F'(0)=ZB0/ZA0>0. Hence R_F and S_F extend analytically to0, with R_F0=1/aF>0,S_F0=0. Their strict concavities extend to the closed interval from0. For X,Y>0, the divided differences R_F[0,X,Y],S_F[0,X,Y] are strictly negative. This includes Y=X, because

    R_F[0,X,X]=[R_F'(X)−(R_F(X)−R_F(0))/X]/X<0,

since the average of R_F' on[0,X] is greater than R_F'(X); analogously for S_F. A strict inequality is not deduced from only a nonnegative limit.

The identityDET3 of082 extended by analyticity to the node0 gives, for distinct q,z>0,

    det K_F(0,q,z)
      =q²z²(z−q)² R_F[0,q²,z²]S_F[0,q²,z²]
         /[R_F(0)R_F(q²)R_F(z²)]>0.

Moreover K_F00=aF and the minor(0,q) is (d/q)(aF−d/q)>0 byF-GAP. Thus that block isPD. Put delta=aF−d/q>0 and

    ell(z)=[zd−qF(z)]/[d(z+q)].

The double Schur identity already used099, now for F with pivotsq and0, gives

    det K_F(0,q,z)=(d/q)delta·ell(z)²·R_next(z)/z.

ell(z) is real nonzero if z!=q, because F/z decreases strictly; hence R_next(z)>0 for those z. At the removable point,

    ell'(q)=[d−qF'(q)]/(2dq)>0,

since the strict DIFFERENTIAL inequality (ZB/ZA)'(q)<0 of the covariance implies d−qF'(q)>0.

The formulaDET3 has leading term (z−q)² with coefficient

    q^4 R_F[0,q²,q²]S_F[0,q²,q²]
        /[R_F(0)R_F(q²)²]>0.

Dividing by the expansion ell(z)²=ell'(q)²(z−q)²+O((z−q)³) also proves R_next(q)>0. F1 has a simple removable point there because d−qF'(q)>0; the remainder is analytic. It is proved that

    R_next(z)>0 for ALL p,q,z>0,

and the remainder in the original normalisation is cR_next>0.

The crossing of U=B−gammaE and the existence of a positive densityXi REMAIN OPEN. The previous real positivity does not pay a positive inverse representation, a monotonicity of the new pair nor the cross terms of its kernel. Nor does it prove new W generators: the node0 used is auxiliary and corresponds to the original exponent1/2, outside the admissible carrier. Preservation of all orders is not declared.
