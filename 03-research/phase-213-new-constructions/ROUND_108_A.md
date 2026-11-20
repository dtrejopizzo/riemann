# Joint constraint of the harmonics of the first zero on the prime ceiling

With E,V,L,m,γ of 106 one has unconditionally

    limsup E(x)/√x ≥ 2 cos(π/34) m |V(1/2+iγ)| − V(1/2)/2.

In particular every nonzero non-negative continuous weight with endpoint ratio ≤1.20484 produces positive excesses of root order along a sequence. In 106 the universal obstruction only reached ratio approximately 1.160.

**Proof.** Assume E(x)≤c√x on a tail and set g(u)=c−exp(−u/2)E(exp u) on that tail u≥U. As in 106 its Laplace transform converges for Re s>0 by Landau. For δ>0 take the Gram matrix of the functions exp(ijγu), 0≤j≤32, with positive measure δexp(−δu)g(u)du on the tail. As δ goes down to zero, each entry converges to the residue of the transform at the corresponding frequency. On the diagonal one gets c+V(1/2)/2; on the first off-diagonals m V(ρ) and its conjugate. The rest are zero: the points 1/2+ikγ with 2≤k≤32 are not zeros by the lower certificate, and ζ(1+2ikγ) does not vanish either. The limit is positive semidefinite. By a unitary diagonal change the phase of its first off-diagonal is removed. The vectors with components sin(jlπ/34), 1≤j≤33, diagonalize the real tridiagonal matrix; the smallest eigenvalue is c+V(1/2)/2−2m|V(ρ)|cos(π/34). Pass to the limsup as in 106.

By the phase projection of 106, L<2 arccos(1/(4 cos(π/34)))/γ suffices to force an excess. Reproducible certificate with ball arithmetic:

    from flint import acb, arb, ctx
    ctx.prec = 100
    g = acb.zeta_zero(1).imag
    values = [abs(acb(arb(1)/2,k*g).zeta()) for k in range(2,33)]
    assert all(v > arb('0.1589') for v in values)
    threshold = (2*(1/(4*(arb.pi()/34).cos())).acos()/g).exp()
    assert threshold > arb('1.20484')

The smallest certified modulus exceeds 0.1589174. Neither rational independence nor RH is presupposed. The 31 certified points are multiples of the first ordinate, not a list of additional zeros. The test widens the excluded range; it does not provide the sign for the admissible band of 107.
