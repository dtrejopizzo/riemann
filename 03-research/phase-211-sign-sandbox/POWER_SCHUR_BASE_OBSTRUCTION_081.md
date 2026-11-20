# POWER_SCHUR_BASE_OBSTRUCTION_081 — BASE is not inherited by the real remainder

Status: **PROVED, independent audit passed.** See `POWER_SCHUR_BASE_AUDIT_081.md`. Obstruction to a specific recursive class: the regularized remainder G_p of the REAL Phi does not remain increasing and concave for all positive pivots. It is not a counterexample to W, to the positivity of its kernel, nor to the general Schur recursion. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked POWER_SCHUR_003, POWER_TWO_COPY_SCOPE_074, POWER_THETA_REMAINDER_077 and the appendix078 of POWER_STATE_077.003 and074 refute generic promotions from monotonicities or from a class of potentials; here only the exact remainder of the real Phi already constructed in075–077 is considered.079 motivates asking whether that remainder can again satisfy BASE073 to apply the same step. The new object is REAL G_p and the result is that its monotonicity fails for sufficiently large pivots, with a point of negative derivative fixed analytically, without a sweep.

## 2. Data and exact normalization

Use the proved notations073/077:

    a=M'(0)>0, B(z)=[az/M(z)−1]/z²>0,
    G_p(z)=az[B(p)−B(z)]/[B(p)(z²B(z)−p²B(p))].

The singularities at z=p are removable.077 gives G_p(z)>0 for all p,z>0. Define

    F(z)=zB(z)=a/M(z)−1/z,
    g(z)=z²B(z)=az/M(z)−1,
    K_p=p²B(p)=ap/M(p)−1,
    C_p(z)=[p²B(p)²/a]G_p(z).

The symbol g here has argument z, not x=z² as in079. Exact algebra gives

    C_p(z)=z[B(z)−B(p)]/[1−g(z)/K_p].               (NORMAL)

BASE073 implies g'(z)>0 and

    0<F(z)<a/M(z),
    0<g'(z)=a[M(z)−zM'(z)]/M(z)²<a/M(z).          (BOUNDS)

## 3. Limits without a new asymptotic hypothesis

The full real bounds used in078 give M(z)→infinity and M(z)/z→0. More explicitly, for z>=128,

    M(z)<log(z/5)/2+2/(z−1/2)<sqrt(z).

The last inequality uses log z<=sqrt z and 2/(z−1/2)<1<sqrt(z)/2. A lower bound increasing to infinity comes from078:

    M(z)>=log[(z+1/2)/(2pi)]/2−1/100, z>=63/2.

Hence B(p)→0, K_p→infinity, F(z)>0 and F(z)→0 as z→infinity. NORMAL converges to F, with all its derivatives on any compact set of z>0. This alone prevents all G_p from being increasing: a pointwise limit of increasing functions would be increasing, but F is positive and tends to zero.

The next section fixes a point and an explicit threshold, without depending only on this limit argument.

## 4. Explicit point of negative derivative

Set z_*=1024, c_*=M(z_*). The appendix078 proves a>1/25 via the real anchor L(8)>3/10 and the concavity073. For A=z+1/2>=32, the full real series and psi_1(A/2)>=2/A give

    M'(z)>=1/(2A)−1/A²−1/(A−1)²
           >1/(2A)−3/A²>1/(3A).

We used A²/(A−1)²<2 and A>18. At z_*, the formula for M with psi(y)<=log y, P_0>=0 and pi>3 gives

    c_*<2/(A−1)+log(A/6)/2
        <1/100+log(243)/2<1/100+11/4<3.

Here A=2049/2, A/6=683/4<243 and log3<11/10, a constant already used in078. Moreover

    z_*²M'(z_*)>z_*²/[3(z_*+1/2)]>300,

since 1048576>922050. Hence

    a z_*² M'(z_*)/c_*²>300/(25·9)=4/3,
    F'(z_*)=1/z_*²−aM'(z_*)/c_*²<−1/(3z_*²).       (NEGATIVE)

No new theta datum is evaluated numerically.

## 5. Explicit pivot threshold

Define positive constants of the same real Phi

    g_*=az_*/c_*−1,
    L=2g_*+24a²z_*²/c_*²,
    p_0=[25(L+2)]².

This threshold is symbolic and effective in terms of a and c_*, without a search over pivots. Since p_0>2500>z_* and M(p)<sqrt p for p>=p_0,

    K_p=ap/M(p)−1>sqrt p/25−1>=L+1>L.

In particular 0<g_*/K_p<1/2. Differentiating NORMAL, keeping p fixed, gives

    C_p'(z)=[F'(z)−B(p)]/[1−g(z)/K_p]
       +z[B(z)−B(p)]g'(z)/{K_p[1−g(z)/K_p]²}.

At z_*, the first summand is less than F'(z_*), because the latter is negative, B(p)>0 and the denominator is between0 and1. By BOUNDS, the second summand is less than 4a²/(c_*²K_p). This bound remains valid even if its numerator were negative. Thus, for ALL p>=p_0,

    C_p'(z_*)<−1/(3z_*²)+4a²/(c_*²K_p)
              <−1/(3z_*²)+1/(6z_*²)
              =−1/(6z_*²)<0.

The normalization p²B(p)²/a is positive. Consequently

    G_p'(1024)<0, ALL p>=p_0.                     (FAIL-BASE)

This refutes inheriting the condition G'>0 globally. It also prevents inheriting G''<=0 globally: if a function positive on the whole half-line were concave and had a negative derivative at1024, it would lie below a line that ends up negative. In particular for each p>=p_0 there is some later point where G_p''>0.

## 6. Scope and live residue

G_p>0 remains proved in077. The failure of G_p'>0 does not contradict that a two-node kernel can be positive: the criterion |zG_p'/G_p|<=1 allows negative derivatives. Nor is the positive Schur residue R_p/z eliminated, nor is it claimed that the full regularized kernel fails.

Hence079 cannot be iterated simply by declaring BASE073 for each new G_p. A broader class allowing decreasing functions remains open, or a proof that keeps the residue and controls the crossings directly. The optional double concavity078 gave precisely a possible condition for pairs of the kernel G_p without requiring G_p'>0; this document does not refute it, does not prove its preservation and does not decide higher orders. Global sign OPEN.
