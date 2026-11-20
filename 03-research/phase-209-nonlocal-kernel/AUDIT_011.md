# AUDIT_011 — Continuous Mellin–Gauss map and cross-check with the paper's form

2026-10-19. Independent check. Read LINK_011, P47 eq:form, eq:Aform, eq:W, lem:combsine and the precision added to the criterion of CONSTRUCTOR006.
**Verdict: PROVED convergence, domain, even FE and smoothing character of the map; PROVED that its norm does not coincide with Q_T. Domination with positive remainder OPEN. Full target D active.**

## 1. Exact form that the link must represent or dominate

For each T, P47 fixes the domain

    D_T={F∈L²(−T,T): ∫log(2+|t|)|Fhat(t)|²dt<∞},
    P_T={A(F)=B(F)=0}.

Its primitive form is

    a_T(F)=C₀||F||²+∫₀∞[c_F(0)−Re c_F(u)]K(u)du
           −Σ_{log n<2T}2Λ(n)/√n Re c_F(log n).

The full form adds 2Re(A(F)conjugate(B(F))). On the even carrier with C(F)=∫Fcosh(x/2)=0, that term is zero and Q_T=a_T. The sign of that sector alone does not automatically resolve the odd one; a claim about W outside the primitive one must also keep its pole. Contacts are not replaced by Λ(n)−1 without the correct continuous term.

A sufficient link may prove a_T(F)≥K(U_TF)≥0 on a PRIMITIVE core dense in form norm for all T, with its sectors and internal reductions declared. It does not need to extend U if there is already a sign on the core and continuity of the target form. L² density alone is not enough. The separate correspondences G→comb, v→polar and Π→gamma of 006 were a possible scheme, not necessary conditions: TOTAL equality or domination with remainders of proved sign suffices. The precision added to 006 correctly corrects that overdemand.

## 2. Actual domain of the proposed map

The proof of S_α(d,d)≤C_αd^(−s) is correct. From the lower bound τ(d²y)≥c/d−1, the upper τ≤c and q_d≤1/d one gets

    0≤1/d−q_d≤min(1/d,√y).

If c/d−1 is negative, 1/d≤√y; if not, dividing by τ≤c keeps the required direction. Thus

    Π_α(d,d)≤∫y^(α−3/2)min(d^(−2),y)dy
      =[1/(α+1/2)+1/(1/2−α)]d^(−2α−1).

The exponents and constants are exact and the integral converges on the α interval used. The diagonal H_s term is O(d^(−s)).

On a compact set of x, the function τ(d²exp(2x)) and all its derivatives have Gaussian decay in d² with controlled polynomial factors. The other part W_d is a fixed smooth function divided by d. The bounds C_(T,j)/d are obtained uniformly in each order of differentiation.

Hence Σ|a_d(F)|·||f_d|| converges for all F∈L² and defines a bounded linear U. The vector series b(x), with all its derivatives, also converges uniformly in Hilbert norm. The Bochner integral represents U and the formula for L(x,x′) is correct; Cauchy–Schwarz for S absolutely controls the double series and its derivatives. The operator is Hilbert–Schmidt, compact and its kernel is C∞. No formal series domain is assumed without proof.

## 3. FE of the coefficient and limit of the polar expansion

For even F and α=1/4, reflecting x and substituting W_d(exp(−2x)) gives exactly formula(2). The last moment is ∫Fexp(−x/2)=∫Fcosh(x/2) by parity. The final version does not extrapolate this identity to non-even F without keeping F(−x); that correction is necessary and already incorporated.

The coefficient shows the same linear cosh constraint of the even carrier. It does NOT prove an identity of the quadratic pole of Q_T. The control of the two separate series is particularly important: Σ(1−1/d)f_d diverges in H because its rank-one PSD component has lower norm

    (−Z_α)|Σ(1−1/d)(d^(−s)−d^(−1))|²→∞.

Therefore the cancellation must be carried out IN EACH COEFFICIENT before summing. The FE formula does not produce an independent polar vector. On C(F)=0 the polar line vanishes and the already controlled O(1/d) coefficient remains. All these claims are correct and of precise scope.

## 4. Comparison with gamma and comb

The symbol of P47 satisfies

    m(t)=Re ψ(1/4+it/2)−logπ
         =log|t|−log(2π)+O(|t|^(−2)).

The normalisation and the sign coincide with eq:form. The Lévy energy has K(u)~1/u: it is an operator of logarithmic order, not a claim that its physical kernel is log|u|. The final wording incorporates that precision.

For fixed T, the comb sum is bounded in L² by Σv_n||F||², while the gamma part is not. In lem:combsine the full comb on the sine basis keeps the divided differences D_T(ω_k)±D_T(ω_l) and its diagonal C_T(ω_k)+D_T(ω_k)/(2Tω_k). It cannot be replaced by a single-argument matrix nor by an average of phases; nor is the compressed gamma by definition diag(m(ω_k)). Candidate011 makes none of those substitutions.

## 5. Exact refutation of equality for this map

The test φ(x)cos(λx), with φ even smooth of interior support, has L² norm tending to ||φ||/√2. Its cosh moment decreases faster than any power. Subtracting the corresponding multiple of an explicitly EVEN χ with nonzero moment keeps parity, support and smooth domain; after normalising, F_λ lies in the even primitive core.

Its Fourier transforms are two translates of φhat to ±λ plus a superpolynomially small correction. The asymptotics of m and the rapid decay of φhat give gamma(F_λ)=logλ+O(1). The correction does not alter that term; the comb remains uniformly bounded. Thus Q_T(F_λ)→+∞.

On the other hand F_λ converges weakly to 0 and U is compact, hence ||UF_λ||²→0. **The identity Q_T=||U·||² is refuted for THIS candidate and every fixed T.** The argument is independent of the unknown sign in the low directions and does not use zeros.

## 6. Remainder and final scope

B_T=Q_T−||U·||² is defined as a form on the domain of Q_T; it keeps the unbounded gamma and the comb translations, subtracting only a smooth kernel. B_T≥0 has not been proved. The positive growth at high frequency controls neither low frequencies nor couplings.

The result does not refute a domination Q_T≥||U·||², nor other non-smoothing maps or maps with different domains. It does not authorise replacing the remainder by a free positive symbol. The map actually computed is NOT the form of the node, and the cosh FE is not enough to identify it.

**Explicit candidate audited; equality ruled out with proof; domination and actual link still OPEN. Target D remains incomplete.**
