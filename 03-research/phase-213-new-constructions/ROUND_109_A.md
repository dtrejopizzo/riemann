# A local inequality that only needs to be proved at prime centers

Set h=11/25, r=exp(h), C=cosh(h/2). Let w(t)=t^(−1/2)sinh((h−|log t|)/2) for |log t|≤h and zero outside. With V(s)=∫w(t)t^(s−1)dt, the global sign is equivalent to the following inequality for each sufficiently large prime q:

    Σ_{q/r≤p≤rq} log p w(p/q) ≤ q V(1).

The band has ratio exp(0.88) as in 107. In this criterion both the center and the samples of the sum are primes. The recovery of the real centers is exact, without gap estimates or interpolation tolerance.

**Between prime centers.** As a function of x, w(p/x) is zero up to p/r, then (√r x/p−1/√r)/2 up to p, then (√r−x/(p√r))/2 up to rp, and then zero. It has upward slope jumps at the two endpoints and a downward one only at p. Thus E(x)=Σ log p w(p/x)−xV(1) is convex between each pair of successive primes. If E≤0 at both endpoints, E≤0 on the whole interval. In particular an excess can only occur if at least one of the adjacent prime centers has an excess. The continuous and the discrete verification are equivalent for any tail starting at a prime.

**Continuous equivalence.** For z=s−1/2, integrating the two exponentials (or using the three jumps) gives V(s)=[cosh(hz)−C]/(z²−1/4), with removable singularities; V(1/2)=4(C−1). Its possible zeros have Re z=±1/2, so it does not cancel any pole of P in 1/2<Re s<1. Landau gives the converse as in 106–107. Under RH, by the same weighted explicit formula of 107 (continuous weight and second logarithmic derivative of finite variation in the sense of measures), E(x)/√x=−V(1/2)/2−Σρ x^(iγ)V(ρ)+o(1). Here V(ρ)=(C−cos(hγ))/(γ²+1/4)>0. The certificate below bounds Σ V(ρ)/V(1/2) by 0.487, so the ceiling holds under RH with eventual margin ≥0.013 V(1/2)√x.

**Certificate.** Use Σ1/(γ²+1/4)=D<0.0462 under RH and subtract only the first hundred pairs of the non-negative summand 1+cos(hγ). Code for python-flint:

    from flint import arb, acb
    h = arb(11)/25
    C = (h/2).cosh()
    gs = [acb.zeta_zero(i).imag for i in range(1,101)]
    bound = ((C+1)*arb('0.0462') -
             sum(2*(1+(h*g).cos())/(g*g+arb(1)/4) for g in gs))/(4*(C-1))
    assert bound < arb('0.487')

**Cross-check.** 044 uses homogeneous interpolation at prescribed centers; 094 locates maxima at crossings of θ and gaps. Here the local sum itself is convex between primes, even when crossing the moving endpoints of other contributions. This directly selects the prime centers q without a crossing condition. The bound on the sum over the neighbors of each q remains to be proved.
