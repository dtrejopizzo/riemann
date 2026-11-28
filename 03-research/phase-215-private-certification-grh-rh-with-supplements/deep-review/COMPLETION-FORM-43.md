# Paper 43: symbol, form, completions and rulings

Verdict **(a)** for the theorems of this front, under their declared hypotheses and normalisations. Read in full: P43:2919–5544, together with the topology 851–876 and the dependencies indicated below. No first failing step was found. This does not assert bibliographic priority nor deduce RH: the results describe a form for finite S, its chosen completions and limits of specific families.

| Statement | Verdict | Reference and obligation discharged |
|---|---|---|
| Regularisation, convergence and uniqueness away from 1 | (a) | 2919–3190: subtraction at the identity; a distribution supported at 1 has real finite order, independent of the compact level. |
| Separation of tests of equal modulus and coinvariants | (a) | 3198–3303: a single local coset contributes; the p-adic logarithm is used only on 1+pZp, or 1+4Z2. |
| Symbol on all components, maximum and Plancherel | (a) | 3305–3717: conductor term, parity, constants and absolutely dominated Fubini. |
| Meromorphic continuation and contours | (a) | 3720–3903: residues ∓i, grouped sums O(k^-2), heights and orientation correct. |
| Radical, Tate, absence of splitting on tests | (a) | 3905–4183: isolated zeros of the symbol, translations and separating characters. |
| Strong completion and extended splitting | (a) | 4185–4430: complete strong dual, reflexivity, trivial annihilator and density. |
| Rulings and failure of scalar continuous extension | (a) | 4313–4615: two families converging to the same pair of points and giving incompatible limits. |
| Signature, including primitive and ε-invariant parts | (a) | 4617–4823: weighted concentration, diagonally dominant Gram and finite codimension. |
| Proper positive cone in the completion | (a) | 4825–4891: positive bidegrees control L¹ and then the distributional component. |
| Banach algebra and relative determinant | (a) | 4893–5083: injectivity in L¹, control of powers, domain and branch of Log. |
| RR pairing and limits | (a) | 5085–5182: exponentiation of two forms, without asserting a geometric index identity. |
| Change of S and stabilisation | (a) | 5184–5350: new compact set of mass 1 and support eliminating all large primes. |
| Rulings in the limit over S | (a) | 5351–5544: Mertens partial summation, control of diagonals and family between prime powers. |

## Reconstructions that support the verdicts

### Symbol and trace

In the ramified term the telescoping sum of layers of units equals exactly `−cond(κ)`, also for p=2: the layer V0 may be empty and the formula remains valid. The real parity changes only the sech term; on using the reflection of digamma one obtains `logπ−Reψ(3/4+iτ/2)` for the odd component. The regularised integral of the even component gives `logπ−Reψ(1/4+iτ/2)`. The identities and the sector of the asymptotic expansion agree with [DLMF5.9.16](https://dlmf.nist.gov/5.9#E16), [5.7.6](https://dlmf.nist.gov/5.7#E6) and [5.11.2](https://dlmf.nist.gov/5.11#E2).

The maximum is attained only on the principal component at τ=0: the real part of digamma increases strictly with |τ| and each finite factor has its maximum when its phase is 1; a ramified character produces instead a negative term. The Fourier exchange is dominated near 0 by means of `min(2,τ²t²/2)` and elsewhere by exponential decay. There are only finitely many components for a given test.

The meromorphic continuation does not consist in continuing Reψ literally: it is replaced by the half-sum of ψ with conjugate arguments on the real axis and then that holomorphic expression is continued. The residues and the sign of the change of contour were checked. For the prime p, the vertical sides are chosen halfway between the periodic poles; the summation of residues is absolutely convergent by the decay of the transform of the test.

### Radical and completion

If F is orthogonal to all tests, on each component its transform multiplied by the symbol annihilates the transforms of C_c^∞. These are dense in Schwartz and in C0; the product is L¹. Hence it is zero. The isolated zeros of the symbol and continuity of the transform force F=0. If it is orthogonal only to the primitive ones, the form factors through the two Tate moments. Translating a non-negative test keeps N but makes the two moments grow alternately; the two coefficients must be zero.

The topology of D_A is a strict LF: a cofinal sequence of compact sets and levels has closed inclusions with the induced topology. A bounded set lies in one step, and Arzelà–Ascoli for all the derivatives makes it relatively compact. This is the Montel property used to identify the bidual. The completeness of the strong dual is proved directly for Cauchy nets; it is not assumed that a completion automatically gives an injection into distributions.

The density of J(D_A) in `D_A'⊕C²` is deduced from its annihilator: the first component is eliminated by means of primitive orthogonality, and the second by surjectivity of M. The action on the dual is asserted to be continuous only for each fixed H; no stronger assertion of joint continuity is introduced without proving it. The initial topology of J is strictly weaker than the original: the differences of the extended family F_n converge through J and their supports escape every compact set in the LF topology.

### Limits, signature and cone

The extended tests F_n have exponentially small L¹ and N bounded by `C n^-2 e^-na/2`; the second bound integrates by parts twice before estimating. This gives uniform convergence against any bounded set of tests. The peaks Φ_n, by contrast, concentrate their convolution exactly at n log p and produce a contribution of at least `(log p)p^-n ||ω||²/r_n`. With r_n=p^-2n it diverges, although both arguments converge to the same rulings. For this reason the impossibility of sequential scalar extension is proved, not an expository reservation. The iterated limits remain 0; the text distinguishes correctly uniformity, diagonal and iterated limits.

The signature is not inferred merely from finding one positive and one negative function. Infinitely many functions are constructed with spectral concentration in disjoint intervals and prescribed weighted tails. Cauchy–Schwarz in three regions gives the off-diagonal entries. The summable geometric bounds guarantee definiteness of every finite combination and linear independence. Intersecting with a subspace of codimension 2 preserves infinite dimension. For c=−m, the symbol vanishes only at one point; no non-zero test can have continuous transform supported there, so negative definiteness still holds.

### Relative determinant and Mertens limit

The trace norm combines L¹ with two multiplicative weights and an L¹ norm on the Fourier side. Its completion injects into L¹ because a Cauchy sequence has compatible limits in both weighted norms: uniform Fourier convergence identifies the second limit almost everywhere. The logdet series converges in the disc `|z| ||F||_1<1`, by means of a bound on powers that uses a single norm N, not ||F||_tr^r.

In the multiplicativity the two factors `1+z Fhat` and `1+z Ghat` lie in the right half-plane; their arguments add up to a number strictly between −π and π. Hence the product does not cross the cut and Log is additive. To identify that value with the series Δ_H the additional inequality ensuring `|z| ||H||_1<1` is expressly imposed. No operator with Fredholm determinant has been constructed here: it is the relative determinant defined by means of T∘Log.

Mertens is used only in its classical form `Σ_{r≤x}Λ(r)/r=log x+O(1)`. Partial summation gives an error `C||φ'||_1`; for two extended profiles the derivative can fall on the wider one and explains `1/max(n,m)`, not 1/min. The diagonal terms are controlled with the support and the decay `n^-1 e^-na e^-|t|/2`; the prime summation adds at most a factor n. The alternative family centred at log36^n has width smaller than half the distance to the logarithm of any integer other than 36^n, and 36^n is not a prime power: every prime contribution disappears and only a real term tending to 0 remains.

## Logical necessity and junctions

These results prove the main theorems `introB`, `introC` and `introD`; the homological part `introH` was closed in HOCHSCHILD-43.md. For `introA`, the smeared identity is a scalar convolution using the homomorphic section: its proof and `prop:hom`, lines 975–1150, were also read. The only component of an intertwiner can be at a=γb; invariance under p^n and real decay force its coefficient to be constant. Thus the announced line of morphisms is checked, without interpreting the smeared ones as a new geometric category.

P44:698–724 cites exactly the strong completion, density and seminorm of P43, in its normalisation c=0. P44:1071–1138 uses those inputs to approximate the radial measure: the Fourier error is `min(2,ε|τ|)`, the tail is uniformly integrable over bounded sets and the moments converge to `(r^{1/2},r^{-1/2})`. This junction is checked. The Frobenius/contact laws of 44 do not need the signature of 43.

P45 uses the local distribution, the measures and the stabilisation over S; the completion, the rulings and the determinant of 43 are not hypotheses of its comparison with Weil nor of its positivity criterion. The indefinite signature of 43 is for **fixed** S and is not transported to the limit over S. The text itself warns of this. No closure of this ledger supplies by itself the sign required by 46.

## Bibliographic scope

The local formulas and the idea of Weil's trace have explicit antecedents. The constructions of the chosen completion, incompatible families of limits and relative determinant are verifiable as written; their priority has not been established. The pairing called RR is, by definition, the pair of exponentials of two forms, and the text acknowledges that it does not add its components nor prove a Hodge index. This precision prevents attributing to it a geometric result stronger than the one proved.
