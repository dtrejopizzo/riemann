# Elementary cases, 2026-11-04

Status: auxiliary result proved and algebraic counterexamples to possible lemmas; **no proof of the global sign**. Local sources read: Paper 46, especially `reson`, `nearfree`, `transl`, and the README/map of Paper 48; the map and meta notes rule out presenting another positive reformulation as a new route.

## 1. Provable improvement of nearfree: removing log log M

Let χ be real, smooth, compactly supported in (-1,1), nonzero. Write χε(t)=χ(t/ε), P=1/4−∂², ψε=Pχε and Dχ=∫x⁴|χ̂(x)|²dx>0. For ε≤1,

    ||ψε||² ≥ Dχ/(2π ε³).

The Lévy function of the paper has the expansion K(s)=2Σ(j≥0) exp(−(2j+1/2)s). Therefore

    |P²K(s)| ≤ 2Σ(j≥0)(2j+1/2)⁴ exp(−(2j+1/2)s) ≤ 400 s⁻⁵.

Proof of the last number: a⁴exp(−as/2)≤(8/(es))⁴ and Σexp(−(2j+1/2)s/2)=exp(−s/4)/(1−exp(−s))≤(1+4/e)/s; then 2(8/e)⁴(1+4/e)<400. The j=0 term of P²K is in fact zero.

If u≥4ε, the Fourier identities and two double integrations by parts give

    m(ψε,V_uψε)=−(1/2)∫cχε(v) P²K(u−v)dv.

There are no boundary terms because χ is smooth and compactly supported; the diagonal term C0 disappears because the two functions have disjoint supports. Since |v|≤2ε and ||cχε||1≤ε²||χ||1²,

    |m(ψε,V_uψε)| / ||ψε||² ≤ Cχ (ε/u)⁵,
    Cχ=12800π ||χ||1²/Dχ.

For the centres xm=log m−(1/2)log M, |xm−xk|≥|m−k|/M. If ε=1/(KM), K≥8, the norm of the cross-term matrix, divided by ||ψε||², is bounded by 2ζ(5)Cχ/K⁵. The diagonal term of the paper satisfies m(ψε)/||ψε||²≥log(1/ε)−C'χ. Its exact divisibility estimate remains ≤log M+E. This gives

    a(Fb)/||Fb||² ≥ log K−C'χ−E−2ζ(5)Cχ/K⁵.

In particular there exists K0(χ) giving margin ≥1 for every M and every vector b with ε=1/(KM). This improves the ε=1/[8KM(2+log M)] of Paper 46. No novelty is claimed relative to the full corpus: this argument did not appear in the sections reviewed.

Limit: large K still prevents the near-coincidences. The improvement removes a technical loss, without reaching the missing carrier of the sign.

## 2. First visible defect: two packets

Take centres log k and log(2k+1), with profile ψε, and δ=log((2k+1)/(2k)). As ε grows above δ/2, the contact n=2 can be activated, since its autocorrelation is cψε(δ). For large k and ε=O(1/k), no other integer is close to the ratio and the packets remain disjoint. Define

    a=m(ψε), h=m(ψε,V_log((2k+1)/k)ψε), c=cψε(δ), v2=2log2/√2.

The exact matrix on these two packets is

    [[a, h−v2 c/2], [h−v2 c/2,a]].

Thus the exact condition is a≥|h−v2 c/2|. Incorporating the near-contact changes the matrix by [[0,−v2 c/2],[−v2 c/2,0]], which has both signs if c≠0. Hence the lemma "activating a near contact improves/worsens the form in Loewner order" is false even in dimension two. Choosing opposite signs of the two coefficients reverses the effect.

In this example no asymptotic threat to the sign appears: a/||ψε||²=log k+O(1), |c|≤||ψε||² and h/||ψε||²=O(ε⁵). The inequality holds for k large enough. A single local defect does not explain the global cancellation.

## 3. Two and three edges: the pairwise proof is not enough

The matrix with diagonal 1 and all three off-diagonal entries −0.6 has every 2×2 section positive definite, but eigenvalues −0.2,1.6,1.6. An induction based only on pairwise bounds loses the coherent sum. With only two edges (a three-vertex chain) and weight c, the condition is c≤1/√2; with three equal edges it is c≤1/2, although each pair allows c≤1.

The arithmetic pattern close to the triangle (2,2,4) is given by k,2k+1,4k+3. The distances to the contact are

    δ12=log((2k+1)/(2k)),
    δ23=log((4k+3)/(4k+2)),
    δ13=log((4k+3)/(4k)).

They are respectively ~1/(2k),1/(4k),3/(4k). With ε of order 1/k the three become progressively visible. This identifies a concrete test of the cooperation of two prime contacts and their power. **The abstract matrix above has not been realised as a negative matrix of the Weil form**; for three packets, again the diagonal log k dominates the fixed weights. Confusing the abstract counterexample with a counterexample to the sign would be incorrect.

## Operational conclusion

No new route to close the sign survives. What does survive: (i) an auxiliary improvement with explicit proof; (ii) a minimal counterexample to monotonicity of near-contacts; (iii) a 2×2/chain/triangle battery to refute proofs by independent control of edges. Any proposal based on these patterns needs to control the collective norm of the near-contact matrix against the archimedean energy, and that inequality has not been obtained here.

## 4. Audit of the first cycle with real arithmetic weights

Antecedents additionally reviewed: phase-193 `CA_J_002_GKS_FRUSTRATION_AND_FKG_ON_THE_DIVISOR_LATTICE.md` and `CA_K_SYNTHESIS.md`. Frustration, holonomy, gauge and diamagnetic comparison **are not a new proposal** and are expressly exhausted there.

For the three indices above one has exactly δ13=δ12+δ23, and the Euler factor forces Λ(4)=Λ(2). Choose ε=k^(−1/2). Although this resolution sees near-coincidences, in this three-packet subspace only the contacts 2,2,4 are activated for k large enough. The packets still have disjoint supports. By scaling and continuity,

    cψε(δij)/||ψε||² → 1,
    m(ψε,V_log(mi/mj)ψε)/||ψε||² → 0.

Therefore the normalised off-diagonal entries tend to −x,−x,−z, where

    x=log2/√2, z=log2/2=x/√2.

If d=m(ψε)/||ψε||², the limiting determinant of the template is

    d³−d(2x²+z²)−2x²z.

The oriented cubic term −2x²z is strictly negative. **Precise falsifier:** the claim "the first near cycle of type (p,p,p²), thanks to Λ(p²)=Λ(p), has a nonnegative cubic contribution to the determinant" is false already for p=2 in the regime described. There is no favourable cancellation of the first cycle from that arithmetic identity. The exact spectral threshold of the template is d≥(z+√(z²+8x²))/2, larger than the chain threshold d≥√2 x and the single-edge threshold d≥x.

This falsifier refers only to the sign of the proposed cubic term; **it is not negativity of the form**, because here d→∞. It shows that neither the power identity nor the shift cocycle provides by itself the desired compensation. A different collective conjecture would have to specify and prove an additional mechanism; no defensible one has been found in this exploration.
