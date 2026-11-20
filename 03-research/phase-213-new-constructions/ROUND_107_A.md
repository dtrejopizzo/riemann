# A weight of ratio exp(0.88) with ceiling equal to its integral

Let h=11/25 and w(t)=t^(−1/2)(h−|log t|)_+/h². Then Σ_p log p w(p/x)≤x∫w eventually is equivalent to the global sign. Its band has ratio exp(2h)<2.412. Under RH the margin exceeds 0.022√x eventually.

Indeed, V(s)=∫w(t)t^(s−1)dt=[sinh(h(s−1/2)/2)/(h(s−1/2)/2)]², by convolution of two centered uniforms. V(1/2)=1 and all its zeros lie on the critical line. Hence if the ceiling holds, every possible pole of P off the line to its right survives in V P; Landau as in 106 forces the sign.

Under RH the explicit formula for the sum with Λ gives xV(1)−Σρ x^ρ V(ρ)+o(√x). To justify it one can integrate the formula for ψ against the piecewise derivative of the compact weight; at each zero the resulting coefficient is V(ρ)=O((1+|γ|)⁻²), and the integrated explicit formula of 092 also allows two integrations by parts in the sense of measures (the second logarithmic derivative of the weight is a finite measure). The terms of the origin and the trivial zeros are o(√x) by the same integrated formula. The squares contribute (1/2+o(1))√x by PNT and the substitution t=u², and the higher powers O(x^(1/3)log²x). The V(ρ)=sinc²(hγ/2) are non-negative. It then suffices that their sum be <0.478.

Certificate under RH: Σγ^(−2)≤(1+1/784)D by |γ|>14 and the identity of 092, D<0.0462. Subtract the cos² contributions of the first hundred pairs from the bound for Σ1/γ², keeping the full remainder as majorant. Reproduction with python-flint:

    from flint import acb, arb
    h = arb(11)/25
    ordinates = [acb.zeta_zero(i).imag for i in range(1,101)]
    bound = 4/h**2 * (arb('0.0462')*(1+arb(1)/784)
                      -sum(2*(g*h/2).cos()**2/g**2 for g in ordinates))
    assert bound < arb('0.478')

The majorant is 0.477376849102 or less. The constant 0.022 stays strictly below the difference with 1/2. The certificate decides the margin under RH; the unconditional prime proof of the ceiling remains open. Antecedents: hat of 105 and compact-weight transform of 106; here the factor t^(−1/2) places the zeros of the transform exactly on the line and makes its spectral evaluation positive under RH.
