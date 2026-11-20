# Positivity criterion with a fixed Gaussian for the full sieved product

Let φ_V be the centered normal density of variance V. Define Q^*(x;z) with the same doubly sieved coefficients as 360, using the fixed weight exp(u/2)φ_1(u), u=log(x/n). Then

    RH ⇔ Q^*(x;z)>0 for all sufficiently large x
          and all (log x)²≤z≤4(log x)².

The width of the weight is a single constant. The corridor of cuts is used again: the following inverse implication is not claimed with the single cut z=(log x)².

**Direction under RH.** Write L=log x, z=kL², 1≤k≤4. The exponent of the integral is now K(s)=Ls+(s−1/2)²/2+log E_z(s). As in 366 there is a real saddle s₀=1/2+(log(2√k)+o(1))/log z, with K''(s₀)∼L log z, uniformly in k. Indeed Σ log p/(p^σ−1)∼2√k e^(−c)L at σ=1/2+c/log z. The local analysis on |t|≤1/log z is the same: K'''=O(L log²z), B_z/L→−1/ζ(1/2) at the scale 1/√K'', and the real loss of the product is ≫K''t². The main term of Q^* is therefore

    [−L/ζ(1/2)] exp(K(s₀))/√(2πK''(s₀)).

**Control replacing diffusion.** For 1/log z≤|t|≤2√L one has uniformly

    log E_z(s₀)−log|E_z(s₀+it)| ≫ (L/log z) min(t²,1).

The sum of p^(−s₀)(1−cos(t log p)) over z/2≤p≤z suffices. In the variable log p the interval has length log 2. If |t|≤1, removing the part at angular distance <c|t| from the multiples of 2π leaves a subinterval of fixed absolute length. If |t|≥1, divide the interval into pieces of lengths comparable to 1/|t| (use a single one for bounded heights); in each piece of angular length comparable to one there remains a subpiece of comparable length where the angular distance to 2πℤ exceeds a small constant. Thus total length ≫z in the variable p is retained in intervals of length ≫z/(1+|t|)≫z^0.74. By the theorem on primes in short intervals each one contains ≫length/log z primes (the longer ones can be subdivided). The announced estimate gives loss ≥c L/log³z throughout the intermediate stretch. [Guth and Maynard, corollary 1.3](https://arxiv.org/abs/2405.20552)

Under RH, on s₀≤Re s≤1+1/L and |Im s|≤2√L, B_z=F'−F(H+L_z) costs at most exp(O((log L)²)), with the notation of 361. For |t|>4 apply Borel–Carathéodory to log ζ on the disc centered at 2+it of radius 3/2−(s₀−1/2)/4; there are no poles or zeros. The upper real part is O(log(3+|t|)) by polynomial growth, and the central value is bounded with the Euler branch. On the interior disc up to abscissa 1/2+(s₀−1/2)/2 a ceiling O(log(3+|t|)/(s₀−1/2)) results; Cauchy on smaller discs also controls the derivative of F. At bounded heights meromorphy and the distance to the critical line suffice, using that F is regular at 1. The sum H of higher powers is already bounded by its series on Re s≥s₀ and L_z is polylogarithmic in x. Hence the loss of the finite product dominates B_z throughout the intermediate stretch. Move the contour to s₀ without crossing zeros under RH. On the horizontals at ±2√L the Gaussian contributes exp(−2L), sufficient against x^c, E_z=exp(o(L)) and the previous ceiling. The tails on c cost even less by absolute convergence. The local equivalent is thus that of the full sum, eventually strictly positive.

**Converse through the Gaussian semigroup.** For each frozen cut z, the normalized observable e^(−v/2)Q^*(e^v;z) is the convolution in v of φ_1 with the atomic measure of weights b_z(n)/√n at log n. Convolving it with φ_(av−1), using at each evaluation v a fixed numerical parameter av−1>0, produces exactly e^(−v/2)Q_a(e^v;z) of 364. The identity is absolute by |b_z(n)|≤log n. Fix z=2v². For |u−v|≤v/5 one has u²≤z≤4u², so the normalized datum of width one is positive there under the hypothesis, for large v.

Outside that zone its modulus is ≪(1+u)e^(u/2) for u≥0, by absolute summation with the Gaussian weight (group log n into unit intervals). For u<0 it is O(e^u), by the Gaussian tail. With any fixed 0<a<1/1000, the exterior integral against φ_(av−1)(u−v) costs O_a(exp(−c_a v)), c_a>0: completing the square tilts the center by a v/2+O(1), and the loss of the nearest tail is at least exp(−(1/5−a/2)²v/(2a)+O_a(1)), against exp(v/2+av/8) and a polynomial. One obtains e^(−v/2)Q_a(e^v;2v²)≥−o(1).

If there were a zero off the line, choose a>0 small enough for it to violate the parabolic exclusion. The excursion proof of 365 applies with z=2(log x)²: only the estimate of the variation of the cut in blocks changes by a fixed factor, and the factors evaluated at ρ with β>1/2 stay between x^(−o(1)) and x^o(1). It gives negative values of size x^(1/2+c) for some c>0, contradicting the previous inequality. This concludes the equivalence.

**Limit.** 146 uses sinc and a variable variance for another observable; 363 required a modulus and size bound, and 366 positivity for diffusive parameters tending to zero. Here only the sign at fixed width is asked, for the full corridor of cuts. The proof of the direct direction uses RH when moving the contour; unconditional positivity of the fixed pulse remains open.
