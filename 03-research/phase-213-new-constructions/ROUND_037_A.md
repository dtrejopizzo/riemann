# A single compact test for all centres of the first filter

Fix a>0. The global sign fails if and only if there exist a real profile F∈C_c^∞(0,1), with ∫F dx=∫F dx/x=0, and c>0 such that

    B∞(Rγ F) ≤ −c/(1+γ²)   for all real γ,

where Rγ multiplies the Mellin transform by 1/(s+a−iγ). F can be chosen of energy norm one by homogeneity. F depends on a. The converse is immediate because each RγF belongs to X₀. The direct implication requires a simultaneous approximation; the pointwise density of 033 does not suffice to interchange the quantifiers.

**Proof.** If Γ>0, choose the real unit extremizer u of 034. By 036, B∞(Rγu)=−κ I(Rγu) with κ=Γa/(a+1/2). Take a real nonnegative mollifier of mass one, smooth and compactly supported in (0,ε), and call J its causal convolution in t=−log x, extending by zero for t<0. It is an average of the isometries S_r of 034, r=exp(−t) for the shift t. It preserves the zero mean and commutes with Rγ. J and its adjoint in X₀ converge strongly to the identity: the translations are strongly continuous isometries and ||S_r* v−v||≤||v−S_r v||. By compactness of the representative A, approximating it by finite-rank operators one obtains ||J*AJ−A||→0. Fix ε with error less than κ/2. Then B∞(Rγ Ju)≤−κ I(Rγu)/2 for all centres at once.

Write G for the Fourier transform of the logarithmic derivative of u. There is positive mass of |G|² on some bounded interval. On that interval a²+(t−γ)²≤C(1+γ²), hence I(Rγu)≥c₀/(1+γ²). On the other hand, for the J already fixed, with Schwartz symbol j(t), one has

    sup_γ (1+γ²)||Rγ J||² ≤ sup_t |j(t)|² [2+(1+2t²)/a²] < ∞

in energy norm, by Plancherel. Thus the forms (1+γ²)B∞(Rγ Jp) are equicontinuous on each energy ball: their difference between p and u is bounded by a constant independent of γ times ||p−u|| (||p||+||u||). Use the doubly primitive density of 033 to choose now p real smooth compactly supported with both moments zero with error less than half the margin. F=Jp is smooth and compactly supported in (0,1); each translation preserves the vanishing of the two moments, and the same holds for their average. This gives the announced inequality.

**Tail with the original weights.** For a compact test like this one, a=1 can be chosen from the start. In general, if supp F⊂[δ,1], w=a−iγ and M_F(s)=∫F(x)x^(s−1)dx, the filtered profile v is

    v(x)=x^w ∫ₓ¹ F(y)y^(−w−1)dy,   0<x<1.

Below δ it equals exactly M_F(−w)x^w. For n≥1/δ the physical contact of 032 is therefore ∫conj(v(y))v(y/n)dy = n^(−w) M_F(−w) conj(M_v(1+conj(w))). Here M_v(1+conj(w))=M_F(1+conj(w))/(1+2a). Multiplying by Λ(n)/n and summing, the whole discrete tail is evaluated by the absolutely convergent series ΣΛ(n)n^(−1−w) minus its prefix. In the form twice the real part is subtracted. The identity computes the tail and leaves to control the sign of its sum with the prefix and the archimedean part. If the hybrid of 032 is used, the corresponding continuous tail must also be discounted when comparing the two forms.

**Consequence.** To prove the sign it suffices to find a centre of nonnegative energy for each doubly primitive smooth compactly supported initial test, at a single fixed width. More weakly, it suffices to exclude a strictly negative uniform margin after multiplying by 1+γ². The construction does not yet find that centre. 018 gave test-by-test recovery and 033 density in norm; the additional step is to fix a mollifier before the approximation to control the unbounded family of centres. Proof and tail computation independently reviewed.

## Exact vanishing of the tail on a whole lattice

Under the same hypothesis Γ>0, the test can be chosen so that its first filters remain negative at every real centre and, moreover, *all* the filters of an infinite lattice are smooth, doubly primitive and supported in a single finite window. This eliminates the discrete tail at those centres without estimating the Dirichlet series.

Let F be the previous test, supp F⊂[δ,b]⊂(0,1), and define F_D=F−e^(−aD) S_{exp(−D)}F, where S_r F(x)=F(x/r) with extension by zero. In energy norm S_r is isometric and commutes with Rγ. By 036 and continuity at finite γ, H=sup_γ(1+γ²)I(RγF)<∞. The change in filtered energy, multiplied by 1+γ², has absolute value at most ||A|| H(2e^(−aD)+e^(−2aD)). Fix D sufficiently large so that this error is less than half of the initial margin. The same D works for all γ. Both moment conditions pass to F_D.

On the lattice γ_k=2πk/D, k an integer, the Mellin numerator is 1−exp(−(s+a−iγ_k)D). Hence there is an identity of profiles

    R_{γ_k}F_D = T_k F = ∫₀ᴰ exp((−a+iγ_k)t) S_{exp(−t)}F dt.

Each profile is smooth and its two moments vanish by integrating those of the dilations. Its physical support lies within [δ exp(−D),b]. Every contact with n≥exp(D)/δ disappears, with the same cut for each k. On that lattice the full form coincides with the primitive energy of P46 on a common logarithmic window. The necessary half-width is at most (D+log(b/δ))/2 after centring. There is no universal bound for D here.

**Check by summation.** For any F in X₀, Parseval on [0,D] with values in the energy space gives

    Σ_{k∈ℤ} B∞(T_kF) = D [1−exp(−(2a+1)D)]/(2a+1) B∞(F).

Indeed T_kF are the unnormalized Fourier coefficients of exp(−at)S_exp(−t)F; apply polarized Parseval with the bounded operator A. The series converges absolutely by |B∞(v)|≤||A|| I(v) and Parseval for I. Finally B∞(S_exp(−t)F)=exp(−t)B∞(F). The identity sums the individual signs; it does not ensure the sign of each term.

Antecedents: SELECTION_027, P46 rem:Sren and POWER_DESCENT_016 already contain the delay that truncates an exponential average. Here a single small perturbation of F preserves the margin and simultaneously truncates the whole lattice. Negativity of these individual profiles does not imply negativity of their span nor give an unconditional negative test. Proof audited.
