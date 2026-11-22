# Selection of averages of growing width

After the small-diameter optimum of 010-A two options of arbitrary width D were cross-checked. Verdict of the two independent cross-checks: stop these proposals. No sign mechanism was added.

* Uniform average. For a smooth compact primitive profile F of zero logarithmic mass, its antiderivative G from minus infinity is also compact and primitive by integration by parts. The integral of the translations between 0 and D is G−V_DG. Its sign already falls in the two-translation band of P46, lem:transl and thm:band. For non-zero mass the antiderivative has a constant tail: separating the two individual energies would be invalid. The average is still a legitimate test; its sign remains open outside the known windows.
* Average with exponential density e^(−s/2). For primitive F, G(t)=e^(−t/2)∫_{−∞}^t e^(u/2)F(u)du is compact. The weighted integral of the translations between 0 and D is G−e^(−D/2)V_DG. The operator is the causal resolvent of P46 rem:Sren and its use as a filter has an antecedent in POWER_DESCENT_016. Write A,B for the moments with exponents +1/2,−1/2. By parts, F=G'+G/2 has A(F)=0 and B(F)=B(G). In particular the image of the operator on smooth compact primitive profiles covers the whole smooth compact sector B(G)=0. By the crossing of 018-A, e^(−D/2)a(G,V_DG) tends to −conj(B(G))A(G)=0. One recovers a(G)=W(G) as a limit and its sign remains to be decided. If A(G)≠0, another application of the resolvent produces an exponential tail of infinite support.

Reopening for these options: a signed bound controlling the non-zero-mass plateau or the energy in the filtered sector, independent of the reformulation. No new positivity proof.

## What can be signed on the non-zero-mass plateau

Corollary of P46 prop:sharp and lem:transl(iv). For real, even, smooth, compact and primitive F, let M=∫F≠0, w the diameter of its support, c_F(v)=∫F(t)F(t−v)dt and H_D=1_[0,D]*F. For D>w, write b=m^sharp(0)=C₀+4 and a_k=k+1/4. One obtains an exact majorant with an error of known sign:

    a^sharp(H_D) = b M² D + C_F − Σ_{k≥1} e^(−2a_kD) |∫F(t)e^(2a_kt)dt|²/(2a_k²),
    C_F = −b ∫ |v|c_F(v)dv + Σ_{k≥1} (1/(2a_k²)) ∫ e^(−2a_k|v|)c_F(v)dv.

Indeed ||H_D||²=∫(D−|v|)c_F(v)dv. In the series of prop:sharp, |Ĥ_D|²=(2−2cos(Dτ))|F̂|²/τ². The inverse transform of (τ²+4a_k²)⁻¹ is e^(−2a_k|v|)/(4a_k). The shifted contribution factorizes since D>w; the two exponential moments coincide by parity. The constants of the series are O_F(a_k⁻³) using |c_F|≤||F||²; the shifted series converges by the gap D−w. The class includes F=(1/4−∂²)G for smooth even bumps of non-zero integral.

In particular, if the arithmetic fluctuation of prop:sharp for this H_D strictly exceeds bM²D+C_F at some D>w, the primitive energy is negative. The condition dispenses with an asymptotic error bound and includes the continuous density term in the definition of fluctuation. A comparison for the true weights remains pending. The identity does not by itself establish positivity of any large-window H_D.

## Scope of localizing the curvature by contacts

For the non-zero real even F of the previous section, let E(D)=a(H_D). Translation invariance gives E(D)=2∫₀ᴰ(D−u)a(F,V_uF)du. The integrand is continuous on each bounded interval by continuity in form norm on a common window. By P46 thm:band and lem:transl(iv), for D>w,
    
    E''(D)=−2[A_F(D)+Σ_{n≥2} Λ(n)c_F(D−log n)/√n],
    A_F(D)=Σ_{k≥1} e^{−(2k+1/2)D} |∫ F(t)e^{(2k+1/2)t}dt|² > 0.

Strict positivity uses that the vanishing of all those moments would annihilate the polynomials in e^(2t) against F(t)e^(5t/2)dt. They are dense in the continuous functions on the compact support interval by the change of variable x=e^(2t). Hence an interior minimum requires the arithmetic sum to be ≤−A_F(D); on an interval without contact of negative sign E is strictly concave and the minimum over any closed subinterval is at its endpoints.

The condition of existence of at least one negative contact loses all ability to exclude distant D. Indeed ∫c_F(u)e^(u/2)du=0 by the moments, while c_F(0)>0. By continuity there is an open interval (a,b) with c_F<0. For all sufficiently large D, the PNT gives a prime between exp(D−b) and exp(D−a). The quantitative condition on the sum keeps content. The argument localizes interior minima, without ensuring that a negative energy on the half-line is attained at an interior minimum. Direct antecedent: the crossing of two translates of P46. Global screening based only on the presence of contacts is discarded.
