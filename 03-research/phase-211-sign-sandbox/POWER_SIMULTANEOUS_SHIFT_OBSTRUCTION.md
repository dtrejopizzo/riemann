# POWER — Failure of the PSD ordering under simultaneous shift

Status: **analytic PROVED; mathematical and literal reviews of cases/invariant approved.** No new data, numerical certificates or paper modifications. It is not a negative value of the real form W.

## 1. Antecedents, object and difference

The project rules, ROUTES-TRIED-INDEX01–06 and README, R162_2300_MASTER_GRID and CROSSWORD-TO-D were consulted. Cross-checked against POWER_CONE_001, POWER_COMMON_TRANSFER_010, POWER_RECIPROCAL_PFAFFIANS_083, POWER_BRIDGE_002 and POWER_AUDIT_002.010 transports bounds under explicit hypotheses, not a full PSD ordering under common shift.083 supplies shift identities, not their sign.

Closest antecedent: phase188 N_BUILD_007, section1(iv) and3(b), uses the difference between an atom at log2 and smooth O(epsilon) terms against a causal resolvent. There the diagonal archimedean energy log(1/epsilon) prevented inferring a falsifier of the full form. Here the FULL form is compared with its modulation e^(-2t); placing the first packet near0 adds a factor O(epsilon) in its diagonal and allows paying that energy. No worldwide novelty is attributed to concentrated packets nor to the continuity argument.

Define, for a,b>1,

 K(a,b)=[L(a)+L(b)]/(a+b-1),
 L(a)=1/a+1/(a-1)-log(pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

The claim that [K(a_i,a_j)-K(a_i+2,a_j+2)] is PSD for ALL finite sets is refuted. More precisely it fails in some FINITE initial block of the SAME ladder a_i=32+i of002. Its size is not specified nor searched numerically.

## 2. Full form, local continuity and smooth part

The causal form W of001/002 is used, extending by0 to the line. For compactly supported smooth real functions, set

 C_fg(h)=1/2 integral_R [f(x)g(x+h)+g(x)f(x+h)]dx,
 A(f)=integral f(t)exp(t/2)dt, B(f)=integral f(t)exp(-t/2)dt.

The bilinear form has archimedean term

 Arch(f,g)=C0 integral fg + integral_0^infinito Karch(h)[integral fg-C_fg(h)]dh,
 Karch(h)=2exp(-h/2)/(1-exp(-2h)),

comb -sum_(n>=2) v_n C_fg(log n), v_n=2Lambda(n)/sqrt(n), and polar A(f)B(g)+A(g)B(f). The Karch formula comes from P46main.tex lines396–418, Levy density lemma. It is smooth on any compact separated from h=0. The normalisation and its identification with K(a,b) for exponentials are fixed in001/002.

On any fixed compact interval I, for each s>0 there exists C_(I,s) such that

 |W(f,g)|<=C_(I,s)||f||_(H^s(R))||g||_(H^s(R)).       (CONT)

Indeed |m(tau)|<=C_s(1+tau^2)^s controls the Fourier integral by weighted Cauchy–Schwarz. There are only FINITELY many contacts compatible with I; each translation is bounded in L2. The two polar moments are bounded in L2(I). The comb is not replaced by a non-summable infinite envelope.

For T f(t)=exp(-2t)f(t) on the causal half-line define

 D(f,g)=W(f,g)-W(Tf,Tg).                              (DEF)

It is a continuous form on each local domain above and on H_eta of014, defined again in§5, with eta=3/4; T is bounded there. No sign of W or D is assumed to deduce this continuity.

## 3. Two fully declared packets

Choose ONE real smooth function phi, compactly supported in(0,1), with L2 norm equal to1. Fix ell=log2 and, for epsilon>0 small enough,

 f_epsilon(t)=epsilon^(-1/2)phi((t-epsilon)/epsilon),
 g_epsilon(t)=f_epsilon(t-ell).

Their supports lie in(epsilon,2epsilon) and(ell+epsilon,ell+2epsilon). They are causal and contained in a fixed interval. No profiles are changed and no points are evaluated: the limit epsilon to0 is taken through analytic bounds.

At the contact h=ell,

 C_(f,g)(ell)=1/2.

The other orientation does not overlap. The support of C_(f,g) for h>0 lies within[ell-epsilon,ell+epsilon]. For epsilon small enough no other log n enters there. Hence the cross comb is exactly -v2/2. The local archimedean part C0 integral fg is0; its integral part is O(epsilon), because Karch is bounded near ell and |C_fg|<=1/2. The polar is also O(epsilon), since each moment of each packet is O(sqrt(epsilon)). It follows that

 W(f_epsilon,g_epsilon)=-v2/2+O(epsilon).

For the modulated packets,

 C_(Tf,Tg)(ell)=exp(-2ell)/2 integral exp(-4t)f_epsilon(t)^2dt ->1/8.

The other smooth cross contributions remain O(epsilon). Thus

 D(f_epsilon,g_epsilon)->-3v2/8
                     =-3log2/(4sqrt2).               (CROSS)

The EXACT contact of2 and all polar and archimedean contributions have been kept; none is omitted on account of presumed positivity.

## 4. The diagonals of the defect do not pay for that cross term

Fix s=1/8, although the argument works for0<s<1/4. Fourier scaling of a smooth packet gives

 ||f_epsilon||Hs+||g_epsilon||Hs=O(epsilon^(-s)).

Since the first packet is at distance O(epsilon) from0,

 ||(1-exp(-2t))f_epsilon||Hs=O(epsilon^(1-s)).

To justify the second bound without assuming a multiplier small only in L_infinity, after changing t=epsilon(1+x) the function is epsilon^(1/2) times

 [(1-exp(-2epsilon(1+x)))/epsilon]phi(x).

This family has fixed compact support and all its derivatives uniformly bounded. Its Hs scaling gives the stated bound. Also ||Tf_epsilon||Hs=O(epsilon^(-s)).

Write h=f_epsilon-Tf_epsilon. By exact bilinearity,

 D(f_epsilon,f_epsilon)=W(h,f_epsilon)+W(Tf_epsilon,h)
                     =O(epsilon^(1-2s)),

using CONT. For the shifted packet, CONT and boundedness of the multiplier on its fixed support suffice:

 D(g_epsilon,g_epsilon)=O(epsilon^(-2s)).

It is not claimed that these diagonals have a definite sign. Their product is O(epsilon^(1-4s)) and tends to0. Together with CROSS,

 det[D(f_i,f_j)]_(f1=f_epsilon,f2=g_epsilon)
       ->-9(log2)^2/32<0.                            (NEGATIVE)

Hence for some FINITE positive epsilon the form D has an indefinite plane. This is not a negative direction of W.

## 5. Transfer to the fixed ladder without confusing coefficients

Fix that epsilon. The two packets are smooth and compactly supported in(0,infinity). Let u0=63/2, eta=3/4 and X_eta={f:exp(eta t)f belongs to H1(0,infinity)}, usual norm. For a packet h set x=exp(-t),

 q(x)=x^(-u0)h(-log x).

It is smooth with compact support in(0,1). Approximate q in C1[0,1] by polynomials P: approximate q' uniformly by polynomials and integrate adjusting the value at0. If ||P-q||C1<=delta, then for h_P(t)=exp(-u0t)P(exp(-t)),

 |h_P-h|<=delta exp(-u0t),
 |(h_P-h)'|<=(u0+1)delta exp(-u0t).

The integrals with weight exp(2eta t) converge because u0>eta; thus h_P->h in X_eta. This argument is the direct density of002/014 and keeps the real coefficients.

W is continuous on X_eta: the archimedean part by extension by0 to Hs,0<s<1/2; the comb by |C_f(t)|<=exp(-eta t)||exp(eta t)f||2^2 and sum Lambda(n)n^(-eta-1/2)<infinity; the polar because eta>1/2. T is bounded on the same space. Therefore the D matrices of approximants of both packets converge entrywise and keep the negative determinant for sufficiently close FINITE approximants.

Each approximant belongs to span{exp(-(u0+j)t):0<=j<=N} for some common finite N. For e_j(t)=exp(-(u0+j)t) on t>0,

 W(e_i,e_j)=K(32+i,32+j),
 W(Te_i,Te_j)=K(34+i,34+j).

The SAME approximating coefficients are used after T. They are not replaced by coefficients of rho nor by coefficients multiplied by zeta: here they are DIRECT causal exponentials. The matrix D on its plane is a congruence compression of the initial block

 [K(32+i,32+j)-K(34+i,34+j)]_(0<=i,j<=N).

That block cannot be PSD. The existence of N is a finite analytic conclusion of continuity; not a certificate found by a sweep.

## 6. Scope

The universal PSD ordering K-K_shift with simultaneous shift2 is refuted, even on the sufficient fixed ladder002. The opposite direction cannot be universally PSD either: by073, M(u)/u is strictly decreasing, so K(a+2,a+2)-K(a,a)<0 for all a>1. This scalar observation is not used for NEGATIVE.

It has not been proved that W is negative, nor that the matrix K is indefinite, nor that other restricted transports fail. Different normalisations with new hypotheses and their own proof, other shift sizes not treated here, and finer joint signed control are not ruled out. No window T or finite tower is added. The record010 and all positive results remain intact.


## 7. Exact IMS remainder: neither sign nor disappearance by telescoping

**Analytic PROVED; mathematical and literal reviews approved.** Direct antecedent: L2_BUILD004§§1–2 already gives the nonlocal IMS identity and keeps the comb as a coupling. That identity is not presented as a new principle. Here its remainder is evaluated for the SAME modulation defect of§2 and the SAME packets of§3, including the polar.

Set T(t)=exp(-2t), S(t)=sqrt(1-T(t)^2), t>0, and

 d(t,s)=1-T(t)T(s)-S(t)S(s)
       =.5[(T(t)-T(s))^2+(S(t)-S(s))^2].

Then 0<=d(t,s)<=1. For f real smooth with compact support in(0,infinity), define

 R[f]=D[f]-W[Sf]=W[f]-W[Tf]-W[Sf].

S is not uniformly Lipschitz near0; here each support is compact SEPARATED from0 and S is smooth in its neighbourhood. It is not extended without domain analysis to arbitrary functions nonvanishing at0. The cancellation T²+S²=1 eliminates exactly the local term C0. The remaining parts are

 R_arch[f]=-integral_(h>0) Karch(h) integral d(t,t+h)f(t)f(t+h)dt dh,
 R_comb[f]=-sum_(n>=2)v_n integral d(t,t+log n)f(t)f(t+log n)dt,
 R_polar[f]=integral integral 2cosh((t-s)/2)d(t,s)f(t)f(s)dt ds.   (IMS)

The t,s integrals are restricted to the half-line. Near the diagonal d=O(|t-s|²) on each support separated from0, which makes the singular archimedean part absolutely convergent. There are only finitely many contacts. The polar and all its cross terms are included.

Apply IMS to f_epsilon,g_epsilon of§3. On t,s in(epsilon,2epsilon), |S'|<=C epsilon^(-1/2), hence d(t,s)<=C|t-s|²/epsilon. Since Karch(h)=O(1/h) near0 and the Cauchy–Schwarz inequality gives integral |f(t)f(t+h)|dt<=1, even if phi changes sign,

 |R_arch[f_epsilon]|<=C/epsilon integral_0^epsilon h dh=O(epsilon).

The diagonal comb is0 by width<log2. The diagonal polar is O(epsilon²): d<=C epsilon and ||f||1²=O(epsilon). Hence R[f_epsilon]=O(epsilon). On the packet g, separated from0 by ell, T,S have uniformly bounded derivatives, d<=C|t-s|² and the same argument gives R[g_epsilon]=O(epsilon²).

At the cross contact2, d(t,t+ell)->1-exp(-2ell)=3/4 uniformly on the first packet. By polarisation, the comb cross term tends to -3v2/8. The archimedean and polar cross terms are O(epsilon), but the error of the contact cross term may be O(sqrt(epsilon)); its limit suffices. Thus

 R(f_epsilon,g_epsilon)->-3v2/8,
 R[f_epsilon+g_epsilon]->-3v2/4,
 R[f_epsilon-g_epsilon]->+3v2/4.                         (IMS-SIGNS)

The IMS remainder is indefinite for packets with finite epsilon small enough. This is not a negative sign of W.

Nor can the remainder be erased by a supposed automatic cancellation upon iterating. For any smooth compactly supported f separated from0, the sum of R[T^r f], r>=0, converges absolutely. In IMS each product f(t)f(s) acquires the factor [T(t)T(s)]^r; summing gives EXACTLY the coefficient

 d(t,s)/(1-T(t)T(s)).                                  (SUM-IMS)

Convergence is legitimate: the denominator has a positive lower bound on the fixed support; the quadratic vanishing on the diagonal keeps archimedean integrability and the comb is finite. Equivalently the form norms of T^r f decay exponentially with a polynomial factor in r from differentiating T^r.

The coefficient SUM-IMS lies in[0,1], since d>=0 and d<=1-T(t)T(s). However, as (t,s) approaches(0,log2) from t,s>0,

 d(t,s)/(1-T(t)T(s))->1,

not0. This observation does not prove a global sign of the sum for all f: it keeps a signed coupling and does not show that no different compensator can pay for it. A PSD compensator plus a summable cost would need an independent inequality, not only this identity. No obstruction to every localisation or ground-state representation is added, and the conclusions of§6 are not modified.
