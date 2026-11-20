# POWER_STRIP_NECESSITY_059 — A uniform contour bound requires at least quadratic scale

Status: **PROVED**, exact proof proposed, reviewed and developed here; additional case review APPROVED without changes. Only an obstruction to a declared class of contour bounds. It is not a counterexample to W nor to the sign of a cone. Papers untouched.

## Antecedents and difference

Consulted the project rules, index ROUTES-TRIED-INDEX, master grid and CROSSWORD-TO-D; reread JOINT_SCALE016, QUADRATIC017, QUADRATIC_EXPLICIT017, INVERSE_COEFFICIENT054 and EFFECTIVE_HIGHPASS054. PACKET016 treats j/n tending to a constant: an autocorrelation does not vanish in any linear cone. Here the SAME admissible arithmetic density with P=1 is used and a quantitative obstruction is proved along ANY sequence n<=j=o(n²), even when its central frequency diverges. The linear limit is not extrapolated to growing frequencies without controlling their variance.

## Class of estimates

Fix u>0 and 0<eta<u. For the causal real atom

    F_(n,j)(s)=s^j/(s+u)^(n+j),
    rho_(n,j)(z)=z^(2j)/(u²+z²)^(n+j),

consider the estimate, with finite D independent of n,j,

    ∫_R |rho_(n,j)(x+i eta)|dx <=D∫_R rho_(n,j)(x)dx.  (STRIP)

It cannot hold simultaneously along any sequence n→infinity, n<=j=o(n²). In particular, for no C>0 and p<2 can it hold over ALL integers n,j with j>=C n^p. The conclusion remains true if STRIP is required for all numerators of V_n, since P=1 is one of them.

## Exact variance of the packet

Normalize rho on the line as a spectral probability and write Z=|tau|. The beta-prime law, obtained directly via tau²/u², has parameters alpha=j+1/2 and beta=n−1/2. For n>=3,

    E Z² =u²(j+1/2)/(n−3/2),
    mu=E Z
       =u Γ(alpha+1/2)/Γ(alpha) ·Γ(beta−1/2)/Γ(beta).

The elementary gamma inequalities give

    Γ(alpha+1/2)/Γ(alpha)>=sqrt(alpha−1/2)=sqrt j,
    Γ(beta−1/2)/Γ(beta)>=1/sqrt(beta−1/2)=1/sqrt(n−1).

The first is obtained by Cauchy as in EFFECTIVE054§2. For the second, apply Jensen to sqrt(X) with X of law Gamma(beta−1/2): Γ(beta)/Γ(beta−1/2)=E sqrt(X)<=sqrt(beta−1/2). Therefore mu>=u sqrt(j/(n−1))>=u when j>=n. Subtracting the square of this lower bound from E Z² proves

    Var Z <= u²{j/[2(n−3/2)(n−1)] +1/[2(n−3/2)]}.     (VAR)

The bound tends to zero under n<=j=o(n²). The phase is not approximated through an insufficiently precise deterministic central frequency: the actual mean mu of each packet is used.

## Correlations that contradict STRIP

For fixed T>0, choose

    t_n=2pi ceil(T mu/(2pi))/mu.

One has T<=t_n<=T+2pi/u and t_n mu is a multiple of 2pi. The spectral density is even, so the real normalized autocorrelation satisfies

    c_(n,j)(t_n)/||f_(n,j)||²
      =E cos(t_n tau)=E cos(t_n Z)
      >=1−(t_n²/2)Var Z ->1.                           (PACKET)

On the other hand, the rational density is analytic in the strip of height eta and decays at least like |z|^−2. Shifting the contour in its Fourier transform and using STRIP implies

    |c_(n,j)(t)|/||f_(n,j)||² <=D exp(−eta t), t>=0.

Taking T large enough that D exp(−eta T)<1/2 contradicts PACKET. All functions used are the original real atoms; the symbol, the comb, the polar or the form W are not changed.

Finally, for p<2 take j_n=max{n,ceil(C n^p)}. Then j_n>=C n^p, j_n>=n and j_n=o(n²); by the above there cannot exist a uniform D on that cone.

## Scope

The result requires p>=2 only as a NECESSARY condition for this contour strategy with fixed eta and D. It does not prove its sufficiency for all numerators, nor refute a bound with D depending on n, nor rule out a W sign cone with p<2. It does not prove an obstruction p>=3 through heuristic Hermite arguments. The results 017 of scalar contour at quadratic scale and 054 with constant growing in n remain intact. There is no numerical sweep nor new certificate of isolated dimension.
