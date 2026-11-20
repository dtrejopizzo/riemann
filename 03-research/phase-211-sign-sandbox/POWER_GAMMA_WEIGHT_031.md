# POWER_GAMMA_WEIGHT_031 — Real variation and initial budget

Status: PROVED; independent review APPROVED in POWER_WEIGHTED_AUDIT_031.md. FIXED rate u=63/2, all N>=2. No total W sign result. Papers untouched.

## Corpus and difference

Consulted ROUTES-TRIED-INDEX (open residues, primitives, Möbius), master grid R162_2300_MASTER_GRID and CROSSWORD-TO-D (finite identities/monotonicity), the corpus026/025 and the constructions INTERIOR_SCALE030 and GAMMA_BALANCE030. The arithmetic inversion and the primitives are not new. Compared with the finite block030, here the TOTAL VARIATION of the real gamma factor is controlled and the adverse cost of its increasing branch is reduced to M2=u²/(2N−3), keeping in the complement the complete signed arithmetic primitive. Global positivity of that primitive is not assumed: WEIGHTED_BLOCK031 refutes it after contact3.

## 1. Definitions and result

Let d=N−1, rho(t)=e^(-ut)P_N(t), q=−rho'/rho and

    R(t)=rho(t)−(2/3)rho'(t)=rho(t)(1+2q(t)/3).

With D_N=33P_N−P_N', one has R=e^(-ut)D_N/(3/2). By025, D_N is strictly logconcave. There is a unique maximum T_N>0 of R, and

    T_N <= (2/3)d/(d+20) < 2/3     (d>=2),
    T_2=1/33,
    0<R(T_N)−1 <= 2M2/9.                              (PEAK)

In particular the positive variation is R(T_N)−1, the negative one is R(T_N), and TV(R)<=1+4M2/9. These are bounds on the REAL gamma function for all N, not a hypothesis on generic weights.

With H and I_* complete as defined below, the total form satisfies the concrete inequality

    W[g_N]/||g_N||²
      >= int_(T_N)^infty I_*(e^t)[−R'(t)]dt − M2.       (BUDGET)

The weight −R' of this integral is POSITIVE. No absolute value replaces I_* in the complement. The omitted term is bounded one-sidedly, not declared favorable.

## 2. Uniqueness and localization of the maximum

LC025 implies (logR)'=D_N'/D_N−u strictly decreasing. Its initial value is positive, because D_N'(0)/D_N(0)=63(d+10)/(2d−1)>u; at infinity it tends to −u. This proves uniqueness.

Reuse JEN026, f(z)=(d−z)/(2d−z−1), L=D_N'/D_N:

    L<=63(1+10/d) f(tL),       tL<d, d>=2.

At t0=(2/3)d/(d+20), one has exactly

    u=63(1+10/d)f(ut0),       ut0<d.

If L(t0)>u, the strict monotonicity of f contradicts JEN. Hence T_N<=t0. For d1, D_N=3/2+33ut and the maximum is computed directly: T_2=1/33.

## 3. Concavity of q and improvement of the overshoot

By RIC/CURV026,

    q'=q²+2dq/t−u²,  0<q'<M2,
    q=u−d/t+O(t^-2).

Moreover q''<0 for all t>0. Indeed, at any zero of q'' the derivative of RIC gives

    q'(q+d/t)=dq/t²,
    q'''=2(q')²−4dq'/t²+4dq/t³
         =2(q')²+4qq'/t >0.

But q''=−2d/t³+O(t^-4)<0 at infinity. An earlier nonnegative value would require a later downward crossing, impossible by the strict inequality at all zeros. This also excludes tangencies. The extension q(0)=0 is continuous.

Set c=2/3 and T=T_N. On the increasing branch R'=rho(cq'−q−cq²)>0 and R>=R(0)=1. Explicitly, R'=c rho q'−qR<=c q'−q, since rho<=1, q'>0 and q>0. Hence

    R(T)−1 <= c q(T)−int_0^T q(t)dt.

Concavity of q and q(0)=0 give int_0^T q>=Tq(T)/2. Hence

    R(T)−1 <=q(T)(c−T/2)
            <=M2*T(c−T/2)<=M2*c²/2=2M2/9,

since T<c. Here the gamma form is used, not only the localization of the maximum.

## 4. Global integration and explicit initial cost

JOINT-G030 establishes the absolutely convergent identity

    W[g_N]/||g_N||²=int_1^infty G_N(x)H(x)dx,
    G_N(x)=(3/2)x^(-1/2)R(logx),
    H(x)=1+[log((x+1)/(x−1))+c0−1−2Psi_1(x)]/x²,
    c0=−gamma−log(4pi), Psi_1(x)=sum_(q<=x)q Lambda(q).

Define I_*(X)=int_1^X (3/2)x^(-1/2)H(x)dx. Then

    W[g_N]/||g_N||²=−int_0^infty I_*(e^t)R'(t)dt.      (IBP)

There is no boundary term: I_*(1)=0, and I_*(X)=O(sqrt(X)(1+logX)), while R(logX)=O_N(X^-u(logX)^d). The singularity at1 is integrable; the derivatives of the primitive are locally integrable and their values at contacts do not affect the identity.

The increasing branch has e^t<e^(2/3)<2, so it contains NO prime contacts. Since c0−1<0, for 1<=X<2

    I_*(X) <=(3/2)int_1^2 [1+log((x+1)/(x−1))]dx
             =(3/2)[1+3log3−2log2]<9/2.

The last comparison uses log3<11/10 and log2>2/3. Hence

    −int_0^T I_*(e^t)R'(t)dt
      >=−(9/2)[R(T)−1]>=−M2.

This proves BUDGET for the TOTAL form, without truncating the comb and without estimating the complement absolutely.

Equivalently, with the real probability

    dnu_N(t)=[−R'(t)]1_(t>=T)dt/R(T),

one has W/||g_N||² >= R(T) E_nu[I_*(e^t)]−M2. A CONCRETE sufficient criterion is E_nu[I_*]>M2/R(T). This criterion is not proved; its weight is completely specified by the real gamma kernel.

## 5. Scope and limit

Uniqueness derives from the already known LC025; the quantitative contribution is the improved PEAK and BUDGET, of order O(1/N), for the branch preceding any prime contact. W is not deduced from positivity of K, from a finite block or from variation masses. The primitive I_* has real negative values after3 according to WEIGHTED_BLOCK031, so the positive integral in the measure nu still needs a SIGNED ARITHMETIC inequality. The favorable block030/031 and the small initial cost do not by themselves control that complement. No new W region nor closure for N>=6 at fixed rate is claimed.
