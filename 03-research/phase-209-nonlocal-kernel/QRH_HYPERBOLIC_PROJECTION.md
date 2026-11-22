# QRH7/8 — compensated balance and hyperbolic geometry of the carrier

2026-10-19. **PROVED: geometric computation, moment bound and inflection.**
Independent review of the formulas and asymptotics. **OPEN: sign link
with Q_T.** No new estimate for the primes is claimed.

## 0. Corpus, difference and source

Consulted: the project rules, the ROUTES-TRIED-INDEX index, master grid and
CROSSWORD-TO-D.md. Antecedents: SKELETON_001/AUDIT_205_SKELETON_001,
RFIN_TRACT_001 and hyperbolic models R186_043. The polar Green kernel
and the generic bound of psi−x are not reopened as a source of sign.
The additional computation is the EXACT norm of the projected profile, its
dependence on frequency and the position of its inflection. It is a
geometric diagnostic, not a new route that evades those failures.

External source examined: OpenAI30Sept2026, introduction and §§19–20,
https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf .
The external manuscript was not audited in full.

## 1. What to keep from the 7/8 argument

The argument combines moment estimates of inverse and ordinary
polynomials, with a selection of primes and a balance of parameters.
Lemma20.2 and (20.9) certify −E_*≥49/440640 for a COMPENSATED
EXPONENT, via a polynomial identity with explicit sign.
That number is not a coercivity margin of Q_T.

The applicable lesson is to keep the compensation before estimating the
pieces. To use it in 017, valid arithmetic estimates of the
remainder allowing a similar balance are missing. The technique does not create those bounds.
No sign of the auxiliary family is imported into the form of paper46.

## 2. Exact bound of a hyperbolic moment

In H=L²_even(−T,T), or its complexification, let h_b(x)=cosh(bx), b>0,
and P_b the orthogonal projection onto h_b^perp. Define

    I_T(z,b)=sinh((z+b)T)/(z+b)+sinh((z−b)T)/(z−b),
    I_T(b,b)=T+sinh(2bT)/(2b),

with the quotients extended by continuity. For u_z(x)=cosh(zx),

    ||P_b u_z||²=||u_z||²−|I_T(z,b)|²/I_T(b,b).       (1)

Proof: integrate cosh(zx)cosh(bx) by product-to-sum and apply the
rank-one projection formula. For F⊥h_b, Cauchy–Schwarz gives

    |<F,u_z>|² ≤ ||F||² ||P_bu_z||².                (2)

It is an effective bound for every test of that subspace, without zero
information. For real even tests it also bounds the Laplace moment
∫F(x)cosh(zx)dx. The factor is optimal in the complexified space.
On the even polar-free carrier of the project, b=1/2.

## 3. Real asymptotics and complex frequency

Let 0<a<b and gamma be FIXED reals, z=a+i gamma. Direct integration gives

    ||u_z||²=sinh(2aT)/(2a)+sin(2 gamma T)/(2 gamma),

interpreting the second summand as T if gamma=0. As T→∞,

    ||u_z||² ~ exp(2aT)/(4a),
    I_T(z,b) ~ exp((a+b+i gamma)T)/(2(a+b+i gamma)).

Substituting into (1) proves

    ||P_bu_z||² / ||u_z||²
       → [(b−a)²+gamma²]/[(b+a)²+gamma²].            (3)

For gamma=0, equivalently,

    ||P_b cosh(ax)||²
       ~ exp(2aT)(b−a)²/[4a(a+b)²].                (4)

The number 3/8=7/8−1/2 motivates testing a=3/8 as a MODEL PROFILE.
With b=1/2 one obtains

    ||P_(1/2)cosh(3x/8)||² ~ (2/147)exp(3T/4),
    residual ratio → 1/49,
    complex ratio → [gamma²+1/64]/[gamma²+49/64].  (5)

The attenuation 1/49 corresponds only to the real profile, without oscillation.
The ratio of (3) tends to 1 when afterwards |gamma|→∞. No
uniformity in a joint limit has been used. Even for fixed T, the explicit
formula gives I_T(a+i gamma,b)=O_T(1/|gamma|), while ||u_z||²
tends to sinh(2aT)/(2a)>0. Thus the projection removes a fraction
tending to zero as the frequency grows.

The asymptotics (3)–(4) do not extend without justification to a=0. In that
particular case, for b=1/2, the exact formula is

    ||P_(1/2)1||²
       =2T−16sinh²(T/2)/(T+sinh T)=2T−8+o(1).

## 4. Where a change of convexity does appear

Cosh(ax) is globally convex: its second derivative is a²cosh(ax)>0
for a≠0. Sinh(ax), a>0, changes convexity at 0. The corrected profile

    v_T(x)=cosh(ax)−c_T cosh(bx),
    c_T=I_T(a,b)/I_T(b,b),

does present another geometry. For fixed 0<a<b,

    c_T ~ [2b/(a+b)]exp(−(b−a)T).

The ratio cosh(ax)/cosh(bx) decreases strictly on x>0: its logarithmic
derivative is a tanh(ax)−b tanh(bx)<0. Hence v_T'' vanishes
at most once in (0,T). For T sufficiently large v_T''(0)>0
and v_T''(T)<0, since

    c_T b²cosh(bT)/(a²cosh(aT))
       → K=2b³/[a²(a+b)]>1.

There is then a unique positive inflection x_inf(T), and

    x_inf(T)=T−log(K)/(b−a)+o(1).                 (6)

To justify the position, first x_inf→∞ because c_T→0; one can
then use the exponential equivalences in the equation v_T''=0.
At a=3/8, b=1/2 the distance to the boundary tends to 8log(128/63).
On the whole interval there are two symmetric inflections, not just one.

## 5. Scope for D

The formulas are bounds and limits on the polar-free carrier, but they do not
identify the actual fluctuation of the primes with these profiles. A
7/8 free region does not give an identity E(e^x)exp(−x/2)=cosh(3x/8), nor
its sign, amplitude or frequency. The change of convexity does not decide
the sign of Q_T(v_T) either.

Precise insight: polar elimination reduces profiles close to it,
but does not provide a uniform attenuation in frequency. The computation
makes visible which part could not be paid by an argument based only
on geometric closeness to cosh(x/2). It does not exclude additional arithmetic
controls. The counterterm 017 was not proved and paper46 was not integrated.
