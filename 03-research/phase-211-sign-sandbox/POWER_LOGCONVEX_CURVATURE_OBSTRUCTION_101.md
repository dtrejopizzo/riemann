# POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101 — Log-convex curvature is insufficient

Status: **PROVED, independent audit approved.** See `POWER_LOGCONVEX_CURVATURE_AUDIT_101.md`. Explicit analytic falsifier of a class of auxiliary potentials. It is not the real Phi nor a negative value of W. Papers untouched.

## 1. Consultation, new hypothesis and scope

Consulted the project rules, ROUTES-TRIED-INDEX/README.md, the grid R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md. Cross-checked POWER_TWO_COPY_SCOPE_074.md, SCHUR003, 081 and the authoritative status099. The additional search in the index and phase211 for log-convexity of V'', hierarchies of derivatives of the potential and cosh mixtures did not find this falsifier.

074 already proves that V even, strongly convex and V'''>0 on the half-line do not suffice to obtain positivity of triples. Here a strictly strengthened hypothesis is refuted: in addition, V'' is strictly log-convex on the whole line, all even derivatives V^(2j) are strictly positive, and all odd ones V^(2j+1) are strictly positive on t>0. Hence V'''/V'' is strictly increasing. The polynomial potential of074 does not belong to this class: in its tail, (log V'')'' is negative, and its sufficiently high derivatives vanish. This explicit difference justifies the new test and avoids repeating074 under another name.

It is not claimed that the real Phi satisfies all these hypotheses, nor that they are necessary for the sign. Only their generic sufficiency is discarded, even before trying to preserve them under Schur. The real coverage099 is not modified and no global obstruction for W is inferred.

## 2. Potential, law and nodes completely fixed

Define

    v(t)=cosh(t)+10^(-4)cosh(10t), A=10^46,
    V(t)=A v(t), delta=10^(-4), u_i=i delta, U_i=A u_i,
    c=(1,-2,1), i=1,2,3.

Let M(U) be the mean of the law on the whole line proportional to exp[-A v(t)+Ut], and

    K_M(U,W)=[M(U)+M(W)]/(U+W).

The decay of exp[-A v(t)+Ut] pays for all subsequent moments and integrations by parts. We will prove

    c^t [K_M(U_i,U_j)] c < -3 delta^4/(2A) < 0.       (NEGATIVE)

The potential is even and smooth, v''>=101/100>1. All its even derivatives are positive; all its odd derivatives are positive for t>0. Moreover

    v''(t)=cosh(t)+10^(-2)cosh(10t)

is a positive sum of the exponentials with rates -10,-1,1,10. If the four normalized masses tilted by t are p_r(t), then

    (log v'')''=sum_r p_r r^2-(sum_r p_r r)^2 > 0.

The inequality is strict because the four masses are positive and the rates are distinct. Multiplying by A does not change this logarithmic second derivative. All additional hypotheses are verified globally.

## 3. Elementary approximation of the inverse function

Let f=(v')^(-1), well defined on the whole line by v''>1. Write

    alpha=101/100, beta=1/3, gamma=101/120,
    a=1/alpha, b=-beta/alpha^4,
    d=(3 beta^2-alpha gamma)/alpha^7,
    q(u)=a u+b u^3+d u^5.

The coefficient cancellations up to degree5 in

    alpha q+beta q^3+gamma q^5-u

are direct: alpha a=1, alpha b+beta a^3=0 and alpha d+3 beta a^2 b+gamma a^5=0. The rational numbers satisfy

    99/100<a<1, -1/3<b<0,
    d=-51675000000000/107213535210701,
    -1<d<-2/5.                                      (COEFF)

We prove, for 0<=u<=3 delta,

    |f(u)-q(u)| <= 100 u^7.                         (INVERSE)

At u=0 it is immediate. For u>0 set w=b u^3+d u^5. By COEFF, |w|<=2u^3 and 0<q(u)<=u: both correction terms are negative and q/u>99/100-u^2/3-u^4>0. The cubic expansion gives

    |q^3-a^3u^3-3a^2b u^5|
       <=3u^7+12u^7+8u^9 <16u^7.

The mean value theorem applied to the fifth power, using 0<q<=a u<=u, gives

    |q^5-a^5u^5|<=5u^4 |w|<=10u^7.

Also the complete series of sinh, for 0<=q<=3/10000, gives

    0<=v'(q)-alpha q-beta q^3-gamma q^5<3q^7<=3u^7.

Indeed its first omitted coefficient is 10001/5040<2, and the ratio of each subsequent term to the previous one is at most (10q)^2/(8*9)<1/7200. The majorizing geometric sum is less than3. Combining these three bounds and the exact cancellations,

    |v'(q(u))-u| < (16/3+10+3)u^7 <20u^7.

Since v''>=1 and v'(f(u))=u, the mean value theorem implies |f(u)-q(u)|<=|u-v'(q(u))|<20u^7<=100u^7. No integrals are evaluated and no asymptotic expansion without remainder is used.

## 4. A negative triple for the modes

Define K_f(u,w)=[f(u)+f(w)]/(u+w). For the fixed vector c,

    sum_i c_i=0, sum_i c_i u_i=0,
    sum_i c_i u_i^2=2delta^2.

By the polynomial identities (u^3+w^3)/(u+w)=u^2-uw+w^2 and (u^5+w^5)/(u+w)=u^4-u^3w+u^2w^2-uw^3+w^4, the linear and cubic parts of q disappear in the form, and

    c^t[K_q(u_i,u_j)]c=4d delta^4<-8delta^4/5.

INVERSE and (u^7+w^7)/(u+w)<=max(u,w)^6 imply

    |(K_f-K_q)(u_i,u_j)|<=100(3delta)^6.

Since sum|c_i|=4, the error of the form is at most

    16*100*729 delta^6
      = (729/62500)delta^4 <(3/250)delta^4.

Thus

    c^t[K_f(u_i,u_j)]c<-(397/250)delta^4.          (MODE)

## 5. From modes to means, with explicit error

For each u_i, the unique mode of the law proportional to exp[-A(v(t)-u_i t)] is x_i=f(u_i). Let X_i be a variable with that law. Exact integration by parts of (t-x_i) against the density gives

    E[(X_i-x_i)(v'(X_i)-u_i)]=1/A.

By v''>=1 and v'(x_i)=u_i, the integrand is at least (X_i-x_i)^2. Hence

    E[(X_i-x_i)^2]<=1/A,
    |M(Au_i)-f(u_i)|<=1/sqrt(A)=10^(-23).         (MEAN)

Define B_ij=A K_M(Au_i,Au_j). Then

    B_ij=[M(Au_i)+M(Au_j)]/(u_i+u_j).

Since u_i+u_j>=2delta, MEAN implies

    |B_ij-K_f(u_i,u_j)|<=1/[delta sqrt(A)],
    |c^t(B-K_f)c|<=16/[delta sqrt(A)]
       =(2/125)delta^4.

Finally MODE gives

    c^tBc<-(397/250-4/250)delta^4
          =-(393/250)delta^4 < -3delta^4/2.

Dividing by A proves NEGATIVE. The diagonals are positive because parity and positivity of the density imply M(U)>0 for U>0; thus this block is indefinite.

## 6. Result and limits of the conclusion

The strengthened class of potentials of§1 does not guarantee positivity of the complete three-node kernel. The falsifier uses a single potential, three nodes and a prefixed rational vector; it is not a numerical campaign. The small rational check of COEFF and of both error costs gave PASS; the proof above is self-contained and does not depend on that computation.

The result does not concern the real theta kernel nor does it produce a negative W. Nor does it refute a more specific condition on J/K pairs, a recurrence using more data than those differential inequalities of the potential, or the general Schur recursion. All real results up to099 remain in force. The global sign remains OPEN.

In particular this example does NOT jointly satisfy the comparisons of077/089/099 that already pay for the real triples: its negative triple prevents attributing those inputs to it. An invariant class incorporating them has not been refuted. The limited usefulness is to avoid replacing those pair data by the mere differential hierarchy of the potential; it is not a terminal pivot and does not justify a sequence of generic strengthenings of073 that omit the available real inputs.
