# R161_081 — Testing the proposed Q sign away from first contact

## Purpose

We propose proving Q>=0 directly. Before seeking a positive-kernel or sum-of-squares representation, test its possible scope. The Q in R161_071 cannot be nonnegative on the whole primitive space, even at a window where the primitive Weil operator is nonnegative. This does not rule out proving the requested statement on its hypothetical radical by an additional arithmetic argument.

## 1. Canonical extension retaining the Tate term

Use the full window form a, primitive projection Pi, Tate projection Tau=I-Pi, and the primitive selfadjoint operator H. Fix a primitive parity vector f in Dom H. For the finite observation R_L put

    G_L=R_L*R_L, S_L=G_L+J G_L J, K_L=Pi S_L Pi.

These are the operators of R161_071. The finite-rank K_L is nonnegative, parity preserving, and takes vectors into the form domain. Choose N>=exp(2T), N>=2, and retain the definitions c,e,v of that note.

Define r_f in the Tate space by

    a(f,t)=<r_f,t> for every Tate vector t.

This is a finite-dimensional Riesz representation. Tate vectors belong to the full window form domain; no claim of their membership in Dom H is needed. In particular

    <r_f,S_L f>=a(f,Tau S_L f).

Thus r_f equals the original forcing on a first-contact vector and supplies a canonical extension of that forcing away from the kernel. Define Q using R161_071(2.4) with r_f.

The exact recombination in R161_072 now reads, for these general primitive parity vectors,

    Q_(N,L)(f)=-2c_(N,L)(f)-Re a(f,K_L f).             (1.1)

Indeed the correction term removes a(f,Tau S_L f) from a(f,S_L f). All collars are retained through the exact identity c-e=Re<Bf,G_L f>. Nothing exterior is discarded.

## 2. Spectral sign test

Let Hf=lambda f and Jf=epsilon f, with real lambda. By the operator-form correspondence and primitivity of K_L f,

    Re a(f,K_L f)=lambda <f,K_L f>.

Furthermore

    <f,K_L f>=<f,S_L f>
       =||R_L f||^2+||R_L Jf||^2=2||R_L f||^2.

Writing d_(m,N)=sum_(2<=n<=N) Lambda(n)n^(-(a_m+1/2))>0 gives the exact formula

    Q_(N,L)(f)
      =-2 sum_(m=1)^L [d_(m,N)+lambda]|(R_L f)_m|^2.   (2.1)

Consequently, if lambda>=0 and R_L f!=0, then Q_(N,L)(f)<0. This includes strictly positive eigenvalues, not just a hypothetical zero eigenvalue.

For any nonzero compact f, moment completeness ensures that some finite L observes it. At a nonnegative compact-resolvent window with reflection symmetry, eigenvectors can be chosen of definite parity. Thus a claim of Q>=0 for all primitive parity vectors in that window would fail this test. The argument uses the actual defined operators, not an arbitrary matrix replacement or altered prime coefficients.

## 3. Implication for a constructive sign proof

Equation (2.1) excludes a globally valid representation of this Q as a sum of nonnegative squares on the primitive space. It also excludes an argument that derives its positivity solely by combining nonnegativity of H with positive Gamma/Euler weights: the eigenvector test has those properties and gives the opposite sign.

On a hypothetical radical vector lambda=0, (2.1) is exactly Q=-2c. A separately proved Q>=0 there would force every observed coordinate to vanish and, with a detecting collection, exclude the vector. It is not logically circular to try proving that separate statement. But its proof must use a genuinely additional consequence of the physical equality-state equations, not a general sign estimate that also applies to positive eigenvectors.

One could change the auxiliary test or add terms that vanish on ker H to seek a different comparison. Such a modified quantity needs its own domain, collar calculation and sign proof; it is not a positive representation of the present Q.

Status: canonical off-kernel extension and spectral formula (2.1) proved under the stated form/operator hypotheses. A universal primitive-space sign for this Q is ruled out. The radical-specific arithmetic inequality remains unproved; D is not closed.
