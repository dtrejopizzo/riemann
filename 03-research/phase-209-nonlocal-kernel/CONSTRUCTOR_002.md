# CONSTRUCTOR_002 — Design of a normalised theta covariance

2026-10-18. Continuation. **WORKING / PARTIAL:** explicit independent object and positivity; link with Q_T **OPEN**. The positivity of a generic covariance **is not counted as a success of the programme**.

## 0. Corpus and written difference before building

The readings of CONSTRUCTOR_001 and AUDIT_001 are kept. Additional search in index README, 04_PHASES, 05_LITERATURE, 05b and 06: covariance, Fisher, probability, gcd/lcm, log theta, quotients and divisibility. Relevant clashes: SPEC005 Lemma H and H.1 (0-homogeneity of a theta object, possibility of quotients); INV_C (atomic forms and pairs), INV_H/K (divisors used linearly), INV_V_002 (Hermitian Chebyshev transfer), R183_008 (semilocal Gram by gcd), probabilistic G8D/G8H; P1_BBSTAR.

**Reason for this computation, without reopening those programmes.** No attempt is made to equate Q_T with a homogeneous quadratic form in theta coefficients, nor to build a semilocal Sonin Gram, nor to use Λ*1=log as a linear transfer identity. A **normalised covariance** is computed, a degree-zero theta quotient, where the same probability law sees divisibility and whose scale dependence has an exact Poisson identity with the origin term. This is allowed by H.1; not being literally excluded does not give it a sign for the node. The computation must show exactly what is lost if one denormalises to read Mellin. No originality is claimed in the general theory of covariances.

## 1. A single object: divisibility indicators under the discrete Gaussian

Let

`θ(y)=Σ_{n∈Z}exp(−πn²y)`, `τ(y)=θ(y)−1`, y>0.

On Z\{0} I define the probability

`P_y(N=n)=exp(−πn²y)/τ(y)`.

For d≥2, `X_d(N)=1_{d|N}`. I write

`q_y(d)=τ(d²y)/τ(y)`, `l=[d,e]=lcm(d,e)`,

`C_y(d,e)=q_y(l)−q_y(d)q_y(e)`.

**Lemma 1 (PROVED).** For any finite complex sequence a_d,

`Σ conjugate(a_d)a_e C_y(d,e)=Var_y(Σ a_d X_d)≥0`.

It is an elementary covariance: X_dX_e=X_l. It does not require b=Λ. Hence it is **inherited positivity**, whose value for the programme will depend entirely on a specific link identity.

### Exact functional equation of the same object

Poisson for the Gaussian gives

`τ(y)=y^(−1/2)τ(1/y)+y^(−1/2)−1`,

`q_y(d)=[d^(−1)y^(−1/2)τ(1/(d²y))+d^(−1)y^(−1/2)−1]/[y^(−1/2)τ(1/y)+y^(−1/2)−1]`.

This is an exact identity, without stationary phase. The excluded origin reappears as `y^(−1/2)−1`; conductor and scale are those of θ_Z. Duality does not leave each divisibility indicator fixed: the fractional scales 1/d² appear. Hence no closure of the FE in the space of original indicators has been obtained.

### Completeness and deletion

For N≠0:

`Σ_{d|N,d≥2}Λ(d)=log|N|`.

Thus the infinite observable defined by complete arithmetic is log|N|. The sums converge in L²(P_y): their modulus is ≤log|N|, which has finite second moment by the Gaussian weight. In particular,

`Σ_{d,e≥2}Λ(d)Λ(e) C_y(d,e)=Var_y(log|N|)`

understood as a limit of covariances of truncated sums in L²; not as an absolute interchange of each signed term without additional proof.

For b^(p) deleting all powers of p, the observable is

`log|N|−v_p(|N|)log p`.

The identity with log|N| fails at N=p. This is the specific completeness identity; the covariance remains positive after deletion. The sign of Q_T is not attributed to the failure of that identity.

## 2. Positive Mellin down to weight ½: do not invent a barrier

For α>0 and d,e≥2 I define

`I_α(d,e)=∫_0^∞ y^(α−1) C_y(d,e)dy`.

**Lemma 2 (PROVED).** The integral converges absolutely entrywise for all α>0 and defines a PSD form on c_00({2,3,...}). In particular α=1/4 is admissible.

**Proof.** As y↓0, Poisson implies `q_y(d)=1/d+O_d(√y)`, so that

`C_y(d,e)=G_0(d,e)+O_{d,e}(√y)`,

`G_0(d,e)=1/[d,e]−1/(de)=(gcd(d,e)−1)/(de)`.

As y→∞, P_y concentrates on ±1; hence each q_y(d) and C_y(d,e) decays exponentially (for d≥2, q_y(d)=O_d(exp(−π(d²−1)y))). Convergence at both ends. For a finite sum, integrate Lemma 1 against a positive measure. ∎

This does not prove that I_(1/4) has exactly the weight d^(−1/2) required by the node. **The Mellin parameter 1/4 does not replace a homogeneity law:** the denominator τ(y) prevents extracting a power d^(−2α) by change of variable. That is a link question and is not taken as resolved.

The family C_y is not multiplicative Hankel: for the pairs (2,6) and (3,4), both with product 12, the limit y↓0 is respectively 1/12 and 0. Hence it does not collapse universally to a function of the product of the two indices. This does not by itself prove a non-Hankel claim for a single integral I_α at a concrete α.

## 3. Denormalisation: exact identity with classical Mellin and remainder

To recover the theta mass and a Mellin law of dilations, another form of the **same** object is considered:

`B_y(d,e)=τ(y)C_y(d,e)=τ(l²y)−τ(d²y)τ(e²y)/τ(y)`.

For α>1/2 the two parts are separately integrable and

`∫_0^∞ y^(α−1)B_y(d,e)dy`

`=2π^(−α)Γ(α)ζ(2α) l^(−2α) − ∫_0^∞ y^(α−1) τ(d²y)τ(e²y)/τ(y)dy`.

**PROVED** by the Mellin transform of τ and a change of variable. Each left integral defines a PSD kernel in that regime. The right subtraction does not separately turn its terms into sources of sign.

### Real continuation down to α=1/4, with explicit counterterm

One has `B_y=y^(−1/2)G_0+O(1)` at 0 and B_y decays exponentially at infinity. For 0<α<1/2 I define

`R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−y^(−1/2)G_0(d,e)]dy`.

**Lemma 3 (PROVED).** R_α converges absolutely entrywise and is the meromorphic continuation of the previous positive integral through its pole at α=1/2. Its exact representation is

`R_α = ∫_0^1 y^(α−1)(B_y−y^(−1/2)G_0)dy`

`      +∫_1^∞ y^(α−1)B_y dy +G_0/(α−1/2)`.

The proof is to split the integral at 1; the last term coincides in both regimes by elementary integration. At α=1/4, the scalar counterterm is **−4G_0**. Positivity of I_(1/4) does not give that of R_(1/4).

There is also an exact decomposition, without continuation in the first part:

`R_α=I_α+H_α`,

`H_α=∫_0^∞ y^(α−1)[(τ(y)−1)C_y−y^(−1/2)G_0]dy`.

H_α converges for 0<α<1/2 by the same asymptotics; no sign is known for it. This identity locates what a second inequality would have to supply; it does not hide it as a "small error". It is not claimed that R_α or H_α are Q_T.

## 4. Gates and link to the node: concrete pending items

- **SOS.** There is no pointwise identity of a symbol such as μ₀−S_T here nor an archimedean part paying a constant; thm:sos does not apply literally. Nor has a dual certificate of def:PD been produced.
- **P1.** I_α is a generic positive covariance. Simply proposing a map U_T with `Q_T=I_(1/4)(U_TF)` would shift everything to constructing U_T. That existence is not presented as a result.
- **W₂/BR.** Neither BR tests and remainder model nor a P36-4 kernel have been identified. No evasion of its walls is claimed.
- **Domain.** I_α and R_α are defined on finite sequences. There is not yet a non-compact height operator K(t,t′), nor a map from the whole continuous domain of Q_T satisfying the README conditions. A representation of coefficients by exponentials does not automatically resolve this.
- **Degree and support.** Using coefficients `a_d=Λ(d)d^(−1/2)F(log d)` gives a quadratic form in evaluations of F. Using autocorrelations of F as a_d would give degree four and is useless. The form of the node is quadratic in F and linear in Λ; there is no identity between it and the first expression by mere completeness. The lcm terms and theta quotients must be treated explicitly.
- **Poles.** The Poisson origin term is written. It has not been proved that it corresponds to the polar sector of Q_T nor that the orthogonality condition to cosh(x/2) kills it.

## 5. What this design is still working on

The computation avoids two errors: claiming that a normalised covariance cannot exist at the critical parameter (it does exist), and claiming that its Mellin already delivers Γ_R and the required weight (it does not). The exact operation recovering classical Mellin introduces R_α and the term −4G_0 at α=1/4.

The next question within this single candidate is to build a map of tests turning the denormalisation difference H_(1/4), together with the dual Poisson scales, into the archimedean and polar terms with **equality of forms**. There is no such map yet. If one is proposed, the additional atoms must be verified, not just a diagonal or a block compared.

**The README milestone was not reached.** An explicit normalised object, an exact FE identity and the exact point where link and sign are missing were obtained. It is declared neither a sign object nor proved progress towards D; it is left as a construction under examination, not as a closure nor as a universal NO-GO.

## 6. Origin versus punctured covariance: useful identity for the polar link

In order not to confuse the theta association with a useful sign after removing the pole, I denote by `C_y^0` the covariance on Z **including 0** and by `C_y^×` the C_y of §§1–5. Let `p_0=1/θ(y)` and `r_d=τ(d²y)/τ(y)`.

**Lemma 4 (PROVED).** As kernels in d,e,

`C_y^0=(1−p_0)C_y^× + p_0(1−p_0) u_y u_y*`, `u_y(d)=1−r_d`.

**Proof.** Condition on the event N=0 and its complement. On N=0 all X_d equal 1 and have zero covariance. The total covariance formula gives the first term as mean conditional covariance and the second as covariance of the conditional means 1 and r_d. ∎

It is an exact decomposition where the origin contributes rank one, but its direction u_y depends on scale and index. It is not yet identified with cosh(x/2), nor can it be subtracted without justifying the map of tests.

**Lemma 5 (PROVED).** For coprime d,e≥2,

`C_y^×(d,e)=−exp(−π(d²+e²−2)y)(1+o(1))` as y→∞.

Indeed, `q_y(k)=exp(−π(k²−1)y)(1+o(1))`, while `[d,e]=de` and `d²e²−1>d²+e²−2`. Hence the product subtraction dominates the joint probability.

Design consequence: PSD positivity remains, but **entrywise** positivity does not survive removing the origin. Any association argument for the full theta that aims to supply a new sign to the pole-free sector must explicitly control the rank one of Lemma 4. The identity may serve to locate that link; it does not yet prove it.

## 7. First linear map in Λ: logarithmic observable, with exact terms

To bring the quadratic object closer to the linearity of the comb of the node, there is an arm fixed by completeness. I define

`L(y)=E_y(log|N|)=−[∂_β log τ_β(y)]_(β=0)`,

`τ_β(y)=Σ_{n≠0}|n|^(−β)exp(−πn²y)`.

For fixed y>0, all derivatives in β exist and interchange with the sum by the Gaussian tail.

**Lemma 6 (PROVED).**

`L(y)=Σ_{d≥2}Λ(d)q_y(d)`,

`Cov_y(X_d,log|N|)=q_y(d)[log d+L(d²y)−L(y)]`.

The first identity is divisor completeness and monotone convergence. The second is obtained by conditioning N=dM: given d|N, M has punctured discrete Gaussian distribution with parameter d²y and `log|N|=log d+log|M|`.

Hence, for finite a,

`Cov_y(Σ a_d X_d,log|N|)=Σ a_d q_y(d)[log d+L(d²y)−L(y)]`.

If `a_d=Λ(d)v_d`, the moving arm is linear in Λ. The second arm is fixed by the complete arithmetic identity, which changes upon deleting a prime. But it is a **cross covariance**, not a variance: it has no sign for arbitrary v. Replacing it by a variance would reintroduce the quadratic arm. It has not been proved that the tests of the node produce a v of suitable sign or monotonicity.

The weighted Mellin transform of this complete arm is also exact for Re s>1:

`∫_0^∞ y^(s/2−1)τ(y)L(y)dy=−2π^(−s/2)Γ(s/2)ζ′(s)`.

Dividing by `∫ y^(s/2−1)τ(y)dy=2π^(−s/2)Γ(s/2)ζ(s)` one obtains `−ζ′/ζ(s)`. This is a genuine link with the comb, but **still at Re s>1**, and a Mellin quotient is not the integral of a positive covariance. That sign is not carried to Re s=1/2 by analytic continuation. The already indexed transport routes and Helson norms are not reopened with this formula.

In this design, therefore, the two different losses to be avoided are already written: (a) fixing a logarithmic arm recovers linearity in Λ but loses the variance; (b) denormalising allows reading classical Mellin but introduces the counterterm when crossing α=1/2. A new FE identity relating both defects —and the polar sector of the test— would be necessary to pass from this object to the node. That identity has not been built.
