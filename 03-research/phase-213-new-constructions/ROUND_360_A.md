# A single linear average at fixed width for the sieved products

Let w be the triangle on [0,2] of height one at 1, the additive convolution of two indicators of [0,1]. Form with the frozen cut z

    Q_w(x;z)=Σ_{pm without primes ≤z} (log p)μ(m) w(log(x/(pm))).

Then RH is equivalent to the following scalar statement: for each ε>0, uniformly in large x and (log x)²≤z≤4(log x)², one has |Q_w(x;z)|≪_ε x^(1/2+ε). It is a single signed measurement at each x,z: it amounts to integrating Q_{z,1}(u) in du/u from x/e to x. Neither widths tending to zero nor a second moment are required. The statement keeps all real centers.

**Recovering the logarithmic weight without asking for another measurement.** Write S_w=Σ μ(n)w(log(x/n)) and P_w for the simple-prime sum before the sieve. The Laplace transform of the triangle is W(s)=(1−e^(−s))²/s². On the positive half-axis take the signed measure ν=2du−2Σ_{k≥1}δ_k. Since its transform is −W'(s)/W(s)=2/s−2/(e^s−1), one gets u w(u)=(ν*w)(u) by uniqueness. Its variation weighted by e^(−σu) is finite for σ>0. The identity μ log=−μ*Λ therefore implies

    (log x) S_w(x) = −P_w(x) − Σ_{p,k≥2}(log p) S_w(x/p^k)
                      + ∫ S_w(x exp(−u)) dν(u).

In the tilted supremum A(X)=sup_{1≤t≤X}|S_w(t)|/t^σ, σ=1/2+ε, the last two corrections cost O_ε(A(X)x^σ) for x≤X. S_w(t)=0 is understood for t<1.

**Reconstruction.** The identities Q_z=K_z(P−L_z S) and P=L_z S+U_z Q_z of 359 are coefficient identities and hold with w. Under RH, M(t)≪_ε t^(1/2+ε) and partial summation give the same ceiling for S_w. The identity above gives it for P_w with an additional log; K_z and L_z cost x^o(1) at a fixed exponent >1/2 and one starts with a loss smaller than the requested one.

Conversely apply P=L_z S+U_z Q_z at x with z=(log x)². In units of x^σ, L_z S costs O_ε((log x)^(1−2ε)A(x)) for 0<ε<1/4. Up to d≤√x in U_z the hypothesis holds at x/d with loss ε/2, by inclusion in the corridor; the sum costs O(x^(−ε/2+o(1))). For d>√x, use in the child the first identity and the preliminary ceiling for P_w coming from the envelope A(x); this yields a cost normalized by the child of A(x)x^o(1). The tail of the parent is O(x^(−ε/4+o(1))) by the Euler product of 359. The children at bounded scales satisfy trivial bounds. Thus P_w(x)/x^σ costs O(1)+o(log x)A(x). Dividing the logarithmic identity by log x and taking the supremum, absorbing as in 359, gives A(X)≪_ε1. The Mellin transform of S_w then converges in Re s>1/2 and extends W(s)/ζ(s); there W does not vanish. This proves the inverse implication.

**Scope.** The use of fixed width without sieve already appears in the inverse stretch of 353. Here the measure ν allows closing the absorption with the same single linear measurement after sieving the whole product. Estimating this signed sum at root scale is missing; the sector means of 354 do not have that precision.
