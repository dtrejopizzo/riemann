# POWER_THETA_G_COMPACT_AUDIT_080 — Audit of the continuous certificate

Status: **APPROVED mathematically and in code; certificate FULL PASS.** Independent reproduction 92790 exit0/FULL PASS of the 4096 panels and matching hash. No unnecessary fourth copy has been run. Source `POWER_THETA_G_COMPACT_080.md` read in full and approved; stable code `tools/power_theta_g_compact_080_verify.py`.

SHA256 hash checked locally:

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc

## 1. Object and difference relative to the antecedents

Consulted the project rules and the three records, 073/078/079. The new obligation is the sign of the REAL curvature on a fixed compact range, not promotion of pairs to higher order by generic monotonicities. 079 already supplies an algebraic proof that BASE073 plus g concave in squares suffices for three generators of the complete form. 078 covers u>=63/2. The present certificate covers the remaining interval [1/2,63/2], keeping all the arithmetic through the real entire function.

## 2. Entire function and jets

With A=u+1/2, E(A)=A[1+(A−1)zeta_deflate(A)]Gamma(A/2)exp(−A log(pi)/2). The official deflation is zeta(A)−1/(A−1), so E=A(A−1)zeta(A)Gamma(A/2)pi^(−A/2), regular also at A=1. E is a positive constant multiple of the transform Z of the real Phi; therefore its logarithmic derivatives coincide with M, M', M'' of the corpus. No u-dependent scale factor is lost.

The REAL API used is documented at https://arblib.org/arb_poly.html and https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html. The self-tests A=1/A=2 are additional controls, not the proof of the identity of functions. The real branch of the log is authorized only after E[0]>0. The jets are computed with python-flint 0.9.0, 256 bits and cap 20. LogE up to degree 19 leaves M'' up to 16; the code requires Delta.prec>=17 and finiteness of all coefficients 0..16. Unknown coefficients are not filled with zero.

Delta=M²+uMM'+u²MM''−2u²(M')². Its positivity gives g''=−a Delta/(4u³M³)<0, with a=M'(0)>0 and M>0. All Taylor coefficients are normalized by k!, without an extra factorial.

## 3. Uniform Cauchy remainder, reviewed independently

For each mesh centre c, complex disc |z−c|<=r=1/16. Positivity/parity of Phi and M increasing give Z(c+r+1)/Z(c)<exp(17/16)<3: on the whole necessary real interval M<1, since the real anchor t=33+1/2, A=34 gives M<log6/2+1/16<1 and covers all necessary points by monotonicity.

The inequalities |x|^k<=k!exp(|x|) and symmetry give |Z^(k)(z)|<=2k!Z(c+r+1). Also |Z(z)−Z(c)|<2r Z(c+r+1)<3Z(c)/8. Thus Z does not vanish on that disc and the ratios of its first three derivatives are bounded by 48/5, 96/5, 288/5. One gets |M|<10, |M'|<120, |M''|<2700. With |u|<32, |Delta|<60000000. These operations and constants were also checked with exact Fraction.

Cauchy controls the WHOLE tail of the degree-16 Taylor polynomial on |u−c|<=h=31/8192 by

    T=60000000(31/512)^17/(1−31/512)
     =5285183618944392932503807265625/
      41901009533176678637026095660718210485846016
     <10^−12.

No zeta jet on a wide interval is needed. The local log series is valid on the disc because Z does not vanish, not merely because the centre is positive.

## 4. Mesh and certificate

The 4096 centres are exact dyadics c_j=1/2+(2j+1)31/8192 and the same h covers exactly [1/2,63/2], without gaps. On each panel the certified lower bound is Delta0(c)−sum(k=1..16)|Deltak(c)|h^k−T>0. All magnitudes are computed outward via arb; neither a float nor a sampled value replaces the panel bound. Run 43260 finished exit0/FULL PASS regularization and 4096 panels, with the hash above. Run 92790 reproduced exit0/FULL PASS and the same hash; no other run was needed.

The history is kept: the first remainder enclosures by interval jets failed because of dependency, without producing negative Delta. Remainder representations were changed (direct, Taylor2, Taylor4, finally Cauchy); interval, mesh 4096, precision 256 and sign margin 0 were not changed. The final certificate is degree 16/cap 20 with external analytic remainder, not the failed degree 5. None of the FAILs is presented as a counterexample or as a PASS.

## 5. Consequence and limits

Splicing this certificate with 078 one obtains g''<0 for all u>=1/2. BASE073 and 079 give the complete kernel positive definite for three distinct nodes ui>1/2, that is, three arbitrary powers ai=ui+1/2>1. Repeated nodes are grouped: strict positivity for the nonzero represented function. The congruence with W is that of CONE001 and keeps ARCH, polar and ALL contacts; it is not positivity of an isolated component.

This extends triples to small and mixed exponents, beyond the region rates>=31.5 of 053. It does NOT prove four nor all orders, nor a new time window nor the global objective of Paper 47. 081/082 and the recursive obligations remain separate. Papers untouched.
