# The Liouville boundary is linear in the root with uniform error

For the sum of 138 with f=λ and 1≤x≤D² one has unconditionally

    S_D(x)=2√x Σ_{a≤D}λ(a)/√a − A(x) + E_D(x),   |E_D(x)|≤2D,
    A(x)=Σ_{r≤x}μ(r) P(√(x/r)),   P(z)=Σ_{ij≤z}1.

Indeed, inverting the two sums of the boundary term of 138, where g is the indicator of squares, gives exactly 2Σ_{a≤D} λ(a) floor(√(x/a)). Replacing each floor by its argument costs at most two units per index. The expression for A is obtained from μ*g*g by convolution. Thus the whole boundary part that could exceed D is a single function of x whose coefficient depends on D.

**Cancelling the coefficient before estimating.** Define C(x)=A(16x)−4A(4x)+4A(x). For 16x≤D², the same combination applied to S_D gives −C(x) with error ≤18D. Inside C one obtains the exact identity

    C(x)=Σ_{r≤16x} μ(r) J(4√(x/r)),
    J(z)=Σ_{ij≤z}(−1)^(i+j)=P(z)−4P(z/2)+4P(z/4).

The Dirichlet hyperbola cuts this sum into two strips i≤√z or j≤√z, subtracting the square counted twice. Each inner alternating sum has modulus ≤1, so |J(z)|≤2√z+1 for z≥1. Hence all r≤x^(1/3) together cost in absolute value O(x^(1/4)Σ_{r≤x^(1/3)}r^(−1/4)+x^(1/3))=O(√x). This elementary estimate pays at once the boundary part and the two divisor sums of the small r at root scale when D is comparable to √x.

**What sign would suffice.** For every ε>0 an eventual upper bound C(x)≪ε x^(1/2+ε) suffices for RH, and under RH it holds even in modulus by 138 or by convolution. Indeed in Re s>1 the Mellin transform of C over (0,∞) is

    (16^s−4·4^s+4) ζ(2s)² / [s ζ(s)].

The part below 1 has support away from zero and contributes an entire function. The dilation factor is (4^s−2)² and does not vanish in Re s>1/2. Neither does ζ(2s) there. The real axis in that strip is regular. Landau applied to a constant times x^(1/2+ε) minus C excludes poles further right than 1/2+ε. By the absolute estimate above the one-sided bound for r>x^(1/3) suffices.

**Limit of an induction by dilations.** Inverting the two finite sums one also has C(x)=Σ_{k≤4√x} b_k M₀(16x/k²), b_k=Σ_{ij=k}(−1)^(i+j). The term k=1 is M₀(16x). At root scale an induction by absolute values would have to pay |b_k|/k per dilation. Already the odd primes have b_p=2 and Σ_p 2/p diverges. The mere alternation inside J does not produce an absolute contraction. Cancellation between dilations, or equivalently here the estimate of the remainder over large r, remains open.

**Cross-check.** Dilation filters and hyperbola cuts are already tools of the corpus (among others 045, 060 and 132); the general transfer is 138. The specific observation is the exact Liouville boundary up to error 2D and the choice of a single filter that cancels it and alternates both coordinates of the divisor of squares. No extension of the window is inferred.

It suffices to check the one-sided ceiling at x=m². The coefficient of A at n=rs², with r squarefree, is μ(r)τ(s) (equivalently, at p^j it is (−1)^j(floor(j/2)+1) by its local factor). Hence each jump is Oε(n^ε). Passing from m² to any x before (m+1)² costs Oε(x^(1/2+ε)) for each of the three sums. The absolute cost of the small-r sector is already O(√x) for all x.

Direct antecedent of the coefficient: 054/055 already use ε*ε (ε(n)=(−1)^(n+1)); 057 works with η² in Mellin. The new use in 139 is the Liouville boundary and the scaled argument 4√(x/r).
