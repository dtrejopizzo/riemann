# POWER_ENERGY_BAND_041 — Signed benefit on a moving energy band

Status: **PROVED BAND**, independent review approved in [POWER_ENERGY_AUDIT_041.md](POWER_ENERGY_AUDIT_041.md). u=63/2 fixed. Papers untouched. No global W sign.

## 1. Corpus and difference

Consulted ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read LOW_TABLE018, CELL_BALANCE024, ARCH_CELL026, INTERIOR_SCALE030, GAMMA_WEIGHT031 and CRITICAL_BALANCE040. Another integration by parts is not presented as sign. Compared with024/030/031, the band grows and moves with N up to the exponential energy; the differential factor040 is kept BEFORE taking moduli. The remainder is compared with a real benefit of the same energy scale, not with the total W.

## 2. Complete result and definitions

For ALL N>=2^80, put d=N−1, delta=N^(-2), v=1/2+delta,

    T=2dv/(u²−v²), L=sqrt(N)/100,
    g(t)=rho_N(t)/2−rho_N'(t), C_N=exp(T/2)g(T)>0.

With the COMPLETE Möbius inverse h_N of022 and the SAME cell weight

    B(x)=log(floor(x)!)−x H_floor(x)+floor(x),

we prove

    2 int_(exp(T))^(exp(T+L)) h_N(x)B(x)dx
                < −C_N/25600.                        (BAND)

The band is favourable in the identity W/norm²=ARCH_sharp−2int hB. No jump of B is discarded or replaced. The contribution of its complement remains open.

## 3. Expansion040 translated without loss of sign

Use the FIXED profile f(ell)=exp(vell)g(T+ell)/g(T), on the whole line, and

    S(ell)=sum_(n>=1)mu(n)n^(−1−delta)f(ell+logn).

The series is absolute. The same Fourier argument040, multiplying the integrand by exp(i xi ell), gives UNIFORMLY in ell

    S=(delta−D)f−gamma(delta−D)²f+r,
    |r|<=E_N<1/(10000N),                              (EXP)

for this delta,N. This extension does not change any constant of040: the added factor has modulus1.

Put z(ell)=delta f(ell)−f'(ell). Then

    int_0^L exp(−delta ell)S(ell)dell
      =1−exp(−delta L)f(L)
         −gamma[z(0)−exp(−delta L)z(L)]
         +int_0^L exp(−delta ell)r(ell)dell.            (ENDS)

Only a FINITE interval is used; no Euler series is integrated at the critical edge nor is summability of sum|mu(n)|/n assumed.

## 4. Uniform edge benefit for the REAL profile

Write b=q'(T), M=u²/(2N−3). By040, 50/N<b<M<=u²/N, q(T)−v<=M/u², and by CURV040

    (T/(T+s))² b<q'(T+s)<b.

The rational comparisons of the verifier give L>=8, L<T/4. Hence q'(T+s)>b/2 for0<=s<=L. Since q(T)>=v,

    log f(L)
      =−int_0^L(q(T+s)−v)ds
           +log[(1/2+q(T+L))/(1/2+q(T))]
      <=−bL²/4+bL<=−bL²/8<=−1/1600.

Thus f(L)<=1−1/3200. On the whole band, log f(s)<=bs<log2, so f<=2. Moreover

    |f'|<=2M(L+2), |f''|<1.                           (DER)

For the second bound, use directly

    f''/f=(v−q)²−q'+2(v−q)q'/(1/2+q)+q''/(1/2+q),

|v−q|<=M(L+1), |q''|<2M/T and1/2+q>=1. The constants of the verifier imply the strict bound; no new concavity of f is assumed.

In particular |z|<=2delta+2M(L+2). With0<gamma<1, ENDS and EXP give

    int_0^L exp(−delta ell)S(ell)dell
       >1/3200−[4delta+4M(L+2)]−E_N L
       >1/12800.                                     (GAIN)

All functions here are those of the REAL gamma atom; they are not replaced by an eligible profile.

## 5. Real B and its controlled correction

The elementary estimate

    |B(x)+gamma x|<=logx+1, x>=1                      (B-REAL)

suffices on this band. Proof: if n=floorx, theta=x−n, then

    B+gamma x=T_n−theta logn−x epsilon_n,
    1<=T_n:=logn!−nlogn+n<=1+logn,
    0<epsilon_n:=H_n−logn−gamma<1/n.

The first bounds come from comparing sum logk with the monotone integral; the last ones from the elementary integral of the harmonic residue. Since x/n<2, the lower bound is greater than−1−logx and the upper does not exceed1+logx. It includes n1 and the jump endpoints.

On changing x=exp(T+ell), the main term−gamma x of the EXACT B produces

    −2gamma C_N int_0^L exp(−delta ell)S(ell)dell.

The remainder V=B+gamma x keeps all the arithmetic, including jumps. By EXP/DER, delta<1/1000 andE<1, |S|<8. Consequently its absolute contribution, DIVIDED by C_N, is less than

    16exp(−T)L(T+L+1)
       <32N²exp(−N/1984)<1/25600.                    (V-ERROR)

Here N/1984<T<N, L<N, and exp(−x)<=4!x^(-4) allows verifying the last comparison only with rationals at N0=2^80. By gamma>1/2 and GAIN, the main term is less than−C_N/12800. Adding V-ERROR gives BAND.

## 6. Scope and precision

BAND is a signed inequality on a REAL integral, not an identity labelled as positivity. The total derivative and its edges have been retained, and only afterwards are the Fourier remainder and the arithmetic correction bounded. C_N may be exponentially large; the sign of the band is decided because its benefit is of that SAME scale.

This does not control the compensation against the interior before T nor against the other bands. An error of this magnitude does not decide W either, whose total residue may be much smaller than each energy. There is no campaign over N, contacts or precisions. The critical boundary sum|mu|/n is not used to deny signed cancellation: it only prevents a global absolute Fubini that is not needed here.

## 7. Uniform periodic expansion of B and explicit integrated error

Auxiliary complement to BAND, with the complete REAL B019. The expansion is an elementary application of Euler/Stirling summation; it is not presented as a new sign principle. The bound recorded keeps the exact jumps and separates the periodic oscillation from a uniformly O(1/x) error, useful for integrating against the signed inverse. BAND does not depend on this improvement: its earlier proof uses a sufficient coarser bound.

Put n=floorx, theta=x−n, B1(theta)=theta−1/2 and

    kappa=(1/2)log(2pi)−1/2.

For EVERY real x>=1,

    B(x)=−gamma x−B1(theta)logx+kappa+E(x),
    −1/x<E(x)<1/(2x), in particular |E(x)|<=1/x.        (SAWTOOTH)

### 7.1. Two elementary remainders, without numerical data

For EVERY integer n>=1,

    log(n!)=(n+1/2)logn−n+(1/2)log(2pi)+s_n,
                    0<s_n<1/(12n),
    H_n=logn+gamma+1/(2n)+e_n,
                    −1/(12n²)<e_n<0.                  (ELEMENTARY-EM)

Compact proofs of the bounds and the constant are included. Let r=1/(2n+1). The absolutely convergent atanh series gives

    a_n=(n+1/2)log(1+1/n)−1
        =sum_(j>=1) r^(2j)/(2j+1),
    0<a_n<r²/[3(1−r²)]=1/[12n(n+1)].

If Z_n=n!exp(n)/n^(n+1/2), then logZ_n−logZ_(n+1)=a_n. By summability Z_n converges to a positive constant C and logZ_n−logC=sum_(k>=n)a_k lies between0 and1/(12n). The constant is C=sqrt(2pi): the recurrence of the integrals I_j=int_0^(pi/2)sin(t)^jdt and I_(2n+1)<=I_(2n)<=I_(2n−1) give, with b_n=binom(2n,n)/4^n,

    2/[pi(2n+1)]<=b_n²<=1/(pi n),
    sqrt(n)b_n->1/sqrt(pi).

But Z_(2n)/Z_n²=b_n sqrt(n/2)->1/sqrt(2pi), while the same quotient tends to1/C. Thus C=sqrt(2pi), and the first bound of ELEMENTARY-EM is proved.

For the second, define

    tau_n=1/(2n)+1/[2(n+1)]−log(1+1/n)
       =4sum_(j>=1) [j/(2j+1)]r^(2j+1)>0.

The coefficient-wise comparison j/(2j+1)<=j/3 proves

    tau_n<4r³/[3(1−r²)²]
        =(1/12)[1/n²−1/(n+1)²].

The sequence D_n=H_n−logn−1/(2n)−gamma tends to0 and D_n−D_(n+1)=−tau_n. By telescoping, e_n=D_n=−sum_(k>=n)tau_k, which belongs to(−1/(12n²),0). No asymptotic remainder has been cited without justifying its sign.

### 7.2. Uniform remainder and jumps at integers

Substituting ELEMENTARY-EM in B(x)=log(n!)−xH_n+n gives EXACTLY

    E(x)=F(n,theta)+s_n−xe_n,
    F(n,theta)=(theta−1/2)log(1+theta/n)−theta/(2n).

For0<=theta<=1/2, log(1+theta/n)<=theta/n implies F>=−theta(1−theta)/n>=−1/(4n), and F<=0 is immediate. For1/2<=theta<1, log>=0 gives F>=−1/(2n), while log<=theta/n gives F<=theta(theta−1)/n<=0. Altogether,

    −1/(2n)<=F<=0,
    0<s_n−xe_n<(2n+1)/(12n²)<=1/(4n).

Since x<2n, SAWTOOTH follows. At integers the convention theta0 is kept: B1(0)=−1/2, not its average0. The jump of B at an integer m is logm; that of −B1({x})logx is also logm. Hence E is CONTINUOUS at each integer. The jumps are not erased nor are their left and right limits mixed.

### 7.3. Periodic integrated bound with explicit edges

Let

    Q2(x)=(1/2)[{x}²−{x}+1/6]−1/48.

It is a CONTINUOUS periodic function, even at integers, with derivative B1({x}) almost everywhere and uniform norm1/16. If1<=a<b and h is absolutely continuous on[a,b], define

    I=int_a^b h(x)[B(x)+gamma x−kappa]dx,
    F_h(x)=h(x)logx.

SAWTOOTH and integration by parts against the CONTINUOUS primitive Q2 give

    | I+[F_h(x)Q2(x)]_a^b |
      <=(1/16)int_a^b |F_h'(x)|dx
                              +int_a^b |h(x)|/x dx.    (PERIODIC-ERROR)

Equivalently, if one wants to eliminate the signed edge,

    |I|<=(1/16)[|h(a)|loga+|h(b)|logb
                        +int_a^b |h'(x)logx+h(x)/x|dx]
                        +int_a^b |h(x)|/x dx.

No additional jump terms appear: the values at integers do not change the integral and Q2 is continuous there. For infinite b one can pass to the limit when F_h(b)->0 and the integrals of the majorant converge; the gamma/inverse kernels of fixed N have the required polynomial decay.

This inequality assigns no sign to the error or to h. It retains the complete function B, the main term −gamma x and the constant kappa, in addition to the periodic cancellation before the modulus. It does not by itself prove the sign of W nor automatically dominate the complement of the band. Its role is to quantify precisely which edges and which variation of h would make that correction negligible; the real balance BAND already proved is the positive application of this round.
