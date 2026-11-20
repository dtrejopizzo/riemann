# Annex — Complete reading of `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`

Source: `../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md` (2611 lines, all read, 1–2611).
Notation: that of `POWER_CONE_001.md` and `POWER_BRIDGE_002.md` (power kernel
K(u,v)=(M(u)+M(v))/(u+v), M=Z'/Z, temporal kernel A(t,s)=∫_0^∞(t+s+2r)Phi(t+r)Phi(s+r)dr,
W the complete form). «GRAM» = `POWER_GRAM_SLICES_OBSTRUCTION.md`, «HYPER» =
`POWER_HYPERBOLIC_MODEL_GRAM.md`, «BPY» = law of the theta density as a sum of exponentials
with rates πn². Labels copied as they appear in the source. «Reusable» indicates whether the
result is positive (an identity or a proved sign usable as a piece) and its exact scope.

This annex modifies no source. A «NO-GO» entry of the source refers only to the class
declared in it.

---

## Part I. Entries by section, in file order

### 0. Header (L1–3)
- Object: transversal audit of global mechanisms outside the Schur tower.
- Result: «strategic review and discards of concrete classes, without a new proof of global
  positivity. Global sign OPEN». REF-D identifies an internal obligation, not impossibility.
- Reusable: no.

### 1. «Verified coverage and limits» (L5)
- Object: scope of the search (indices, grid, crossword; selective reading).
- Result: it is not an exhaustive audit; WM and 112 activated via coverage 110 and tail 104 from 16;
  program 110 INCONCLUSIVE with respect to its target up to 64. No other chain of finite orders is proposed.
- Reopening: —. Reusable: no (documentary status).

### 2. «1. Gram and sums of squares including the complete arithmetic» (L11)
- Object: multiplier identities + Bochner/Cauchy–Schwarz; pure arithmetic SOS (N019).
- Result: purely arithmetic SOS impossible for T ≥ log(3)/2 (negative atoms require diagonal
  mass ≥ A_T); «does NOT affect every mixed sum of squares». Free positive part = dual class
  (reduction, not impossibility).
- Unsigned remainder: the joint factorization.
- Reopening («Admissible change»): explicitly construct a joint factorization of the archimedean
  measure and ALL the contacts, with uniform control of terms and Tate, without postulating that the free
  part is positive.
- Reusable: no (class discard + obligation).

### 3. «2. Exact arithmetic transfer and near-coincidences» (L19)
- Object: Arch−Div−Near decomposition of the matrix of the sufficient profile.
- Result: Near has no separate sign (finite-resolution remainder of the product with the divisor
  convolution); progressions as class properties are stable under finite modification. Logical
  correction of TB3-neg(ii): the exclusion reaches only premises stable under deletion.
- Reopening («Necessary change»): a joint SIGNED inequality between Arch and the terms m≈kn, uniform
  in vectors and sizes of the sufficient carrier, preserving phases and boundaries. Rewriting as a convolution or
  estimating Near in absolute value does not count. «Live substantive obligation».
- Reusable: no.

### 4. «3. First contact, continuation and global defects» (L29)
- Object: entry of a contact, positive continuation; nonlinear global defect (phase 197).
- Result: the audit requires labelling 197 as a **PROVED reduction**, not a universal NO-GO; corrects
  a factor 2 of the metric. The proved margin bound is simply exponential; a doubly
  exponential pattern is not used as a proved barrier.
- Remainder: the collar/exterior field coupling at the crossing.
- Reopening: a mechanism proving a signed bound of the endpoint or of the rest of the path, or an
  independent structural obstruction to the crossing.
- Reusable: no.

### 5. «4. Density, descent and a uniform lower bound» (L37)
- Object: filtered diagonal union at fixed rate (094/096), bridge 002, descent 036.
- Result: L² density only if liminf r(n)²/n = 0 (094); 096 keeps a positive distance to a fixed
  exponential. Even if all crossings were proved, bridge 002 fails: ell0(h)=∫h vanishes on EVERY
  highpass r≥1, its span and its strong closure; the primitive target h=(1/4−D²)g has ell0=∫g/4>0. A
  block repairing that moment is missing. «Deductive clarification 016+002, not a new NO-GO».
- Remainder (descent 036): complete energy; the known cone contributes O(log L/√L), the complement preserves
  the initial value.
- Reopening («Sufficient input»): uniform arithmetic bound R_L ≥ −ε_L, ε_L→0; or a family of
  jointly positive subspaces approximating in a topology where W is continuous.
- Reusable: yes, the bound |ell0(Zrho)| ≤ ζ(5/4)/√(3/2)·‖rho‖_B (from BRIDGE002 B1), as a tool.

### 6. «5. A positive even representative giving a lower bound» (L45)
- Object: even representative (045).
- Result: the compact EVEN repair of a symbol with fixed tail fails in class 045 (forced zero
  repair); the noncompact subcase with signed finite exterior recovers the dual. It is not a NO-GO of all
  positive pairs.
- Reopening («Admissible change»): a positive real representative with noncompact correction, identity on
  the whole carrier and exact control (or cost) of the interior arithmetic coincidence, uniform in T.
- Reusable: no.

### 7. «Obsolete statuses detected» (L53)
- Object: rows 06 O-151.4 and 06R4 of the index.
- Result: corrected; «already treated; no new mechanism with those hypotheses»; 197 are reductions.
- Reusable: no.

### 8. «Operational conclusion» (L58–85)
Subentries (all summarize results of GRAM):
- HK ≥ J²: GRAM §12 proves it (global convexity of the temporal reciprocal r/V'(r), analytic tail and
  compact certificate); positivity of sufficiently small symmetric temporal triples.
  **Reusable** (scope: small triples; not global, no new T).
- Limit §13: C⁶ countermodels with reciprocal convexity and V'''>0 whose kernel fails at some size. Do not
  use those hypotheses as an induction base. Extension of triples to all R, monotonicity of the
  normalized quotient and preservation by Schur: no proof.
- §14: there is no holomorphic extension of q(u)=√u/V'(√u) to Re u>0 ⇒ there is no positive Laplace representation
  of q (discard).
- K_Phi ≥ εK_0, model a=2π: subsequently REFUTED for every ε>0. Do not relaunch smoothing,
  ordinary Cauchy–Schwarz or the negative minor at ε=1.
- Matrix (S): positive potential on signed squares = absolute comparison CA_K_001.
- Grouping nodes close in log m: the double cancellation carries crossings to the kernel −B''; no relative
  inequality for those crossings; «There is no general NO-GO for groupings».
- GRAM §§16–17: principal part of the complete A at fixed integer scales = gcd matrix, non-uniform limit
  (§16.5); the EXACT resonant part R_res admits SOS of all orders, valid at y=0, with uniform
  margin relative to its divisorial energy (§17.5). **Reusable** (audited positive; only R_res).
- Remaining obligation: Off admits no uniform lower bound by a finite multiple of the divisorial
  energy; A does not dominate a fixed fraction of R_res (§17.6, includes y=0); §17.7 rules out paying for the dilation
  operator with the physical energy weighted by 1+log t. «The joint critical inequality, without
  additional margin, remains open.»
- Bridge §18: PSD of the COMPLETE A at y=0 on all blocks of integer scales ⟺ PSD on all
  real nodes ⟺ (§18.9) λ_A(T) ≥ 0 for EVERY T. **Reusable** (exact reduction PROVED).
- §§19.7–19.9: Q(E1) > 1/2000; plane span{E1,E2} signed: Q11>179/100000, Q22>17/10000,
  |Q12|<79/50000, detQ>2733/5000000000 (certificate FULLPASS). Q_B(E1+E2)<−1/20000. **Reusable**
  (only that plane). Core §19.8: signing ALL the Grams of E_j=p(t)(t−1)q_j(t) ⟺ target for all
  windows.
- §19.10 (scope PROVED): for any FIXED J≥1, signing all blocks of E_j, j≥J ⟺ global
  target (constraints P(1)=0, ∫t^kP=0, k<J). No uniformity in J. **Reusable** (reduction).
- §19.11 (PROVED, application of 008): Q0 on p0R, p0=exp(−πt), with log t and Lg but without C, is NOT PSD
  even with R(1)=0 and ∫pR=0. Does not refute the complete Q.
- §19.12 (PROVED elementary): J*Theta(exp 2r)=2g(r)−4rPhi(r), g=−∫k(r+s)Phi(s)ds; the potential
  ∫Phi g|f|² of the difference identity is NOT globally favourable: g(log2+)<−19/300; there exists an
  exactly primitive combination with V<0. Does not prove Q/A negative.
- Control §18.5: with u=½log t, the complete form returns to the causal W of CONE001/SHIFT§2/phase 199;
  kernel 4cosh(h/2)−2e^{−h/2}/(1−e^{−2h}); C0=ψ(1/4)−log π. «Do not relaunch Mellin alone or that change of
  variable as a new mechanism.»
- Common component and contrasts: separating a rank one avoids the fixed-support class but does not prove;
  closeness to the all-ones matrix does not control contrasts; THREE002 §7 (fixed dimension, large rates) is not
  progress.
- Conclusion: legitimate obligations = explicit mixed factorization, joint arithmetic balance, uniform
  one-sided bound of a remainder, complete positive representative. «Another representation», «nonlinear/global»
  or a new dimension are not enough.
- General reopening: «a concrete additional signed estimate, not repeating the change of variables,
  of normalization or of basis».

### 9. «Later audit: theta Gram by slices» (L88)
- Object: candidate A with double transform and quartic model Gram at all sizes.
- Result: slice-by-slice PSD certification fails for real Phi (CND and growth of V'). Does not decide A.
- Subentry parity/modularity: even and odd sectors give [S(x)−S(y)]/(x−y) and uv[N(y)−N(x)]/(x−y);
  requiring both PSD returns to the Stieltjes/divided differences obligation of 083. Modularity of the complete theta
  product does not split by mode; pairs of modes keep crossings. «These two proposals do not
  by themselves justify reopening.»
- Remainder: compensation between slices without a joint bound.
- Reusable: identity of even/odd sectors (exact, no sign).

### 10. «Later arithmetic review: cells and Euclidean division» (L97)
- Object: ledger, SPEC_B, EI_002, CA_M.
- Result: the ledger identifies coefficients, not an inequality; EI_002: after cutting y≥1 there is a jump and
  a boundary; Poisson is not absolutely convergent without them. Concrete error in L2_BUILD_031 §3 (B_Q does not
  eliminate small components; example M=Q=2, s=(1,1), component q2=v2/2>0); Theorem E remains valid.
- Reopening (gate): a positive joint factorization pairing the small-divisor defect and the second-order
  boundary, preserving y=1, quotient changes and the truncation endpoint.
- Reusable: no.

### 11. «Complement to the density analysis: repairing the moment does not pay for the crossings» (L106)
- Object: DESCENT_AUDIT016 §9, Qδ=(s+1)/(s+63/2) invertible in H_{3/4}.
- Result: the span of any tail of generators is dense and diagonals eventually positive even for
  W4=W−4‖·‖², but W4[f0]<0 ⇒ some finite combination is negative. Falsifies only the inference «density
  + individual positivity ⇒ sign».
- Remainder: the crossings. Reusable: no.

### 12. «Limit of assembling small PSD certificates» (L111)
- Result: no fixed size k of PSD coordinate supports suffices for the ladder 002 (condition
  1ᵀC1 ≤ k·trC fails on late blocks → all-ones matrix of size k+1). Does not exclude adapted bases,
  growing blocks, Schur nor a global positive part.
- Reusable: no.

### 13. «Differences in exponents: digamma identity does not imply block order» (L116)
- Result: the universal order K−K_shift (shift 2) refuted, even on initial blocks; the reverse order
  fails by the diagonal 073. Literal IMS repair (SHIFT §7): remainder with both signs; coefficient
  d/(1−TtTs)→1 near the causal echo (0, log2).
- Reopening: a different repair with a proved independent cost.
- Reusable: no.

### 14. «Clarification of the Stieltjes target: the derivative L' in a has no positive Laplace measure» (L124)
- Label: **PROVED**.
- Object: L'(a)=∫e^{−at}b(t)dt+ΣΛ(n)log n·e^{−a log n}, b(t)=t[1/(e^{2t}−1)−e^t].
- Result: b<0 on (log2, log3) without atoms ⇒ there is NO representation L'(a)=∫e^{−at}dν, ν≥0, on
  ANY ray a>1 (uniqueness of moments/Bernstein).
- Scope: says nothing about N(x)=M(√x)/√x; the anti-Löwner/Stieltjes target of 083 remains OPEN.
- Reusable: yes as a discard (exact L', every ray).

### 15. «Exact deduplication of the Gaussian subordination of N» (L145)
- Result: the formula N(x)=∫e^{−xv}[H_A(v)−P(v)]dv, x>1/4, is already in E101_036 §§1–3; obligation:
  alternating signs of ALL derivatives of H_A−P (order 0 is not enough). Review of the remainder:
  H_A−P=B(v)+R_v, R_v=(πv)^{−1/2}∫_1^∞E(x)w_v'(x)dx, B(v)=[1+m(0)/2]/√(πv)+O(v^{−3/2}), m(0)=ψ(1/4)−log π<−2
  ⇒ B eventually negative; the signed remainder must compensate it.
- Reusable: identity with explicit boundary (no sign).

### 16. «Verified transfer to the Gaussian inverses» (L154)
- Result: mixture REAL027 with absolute Fubini: h_N(1)=E h_{VN}(1), K_N(1)=E K_{VN}(1); the
  certificates 128/129 force some Gaussian with h_a(1)<0 and some (possibly different) one with K_a(1)<0.
  «Universal Gaussian inverse positivity cannot serve as a premise.»
- Reusable: no.

### 17. «Review of budget022: scope and antecedents before reopening it» (L158)
- Result: «There is no new theorem nor NO-GO». For k=0 the obligation is A_N+2∫K_N C_B ≥ 0; ∫K_N C_B ≥ 0
  alone is not enough (A_N negative limit, LOW_TABLE018); SCALAR_BRIDGE017 requires all pairs (N,k).
  K_N M dt is signed; GAMMA_AFFINE_BALANCE062 shows a deficit of the affine part.
- Reopening: «an independent inequality that also pays ARCH_sharp and a justification of its scope
  in k».
- Reusable: no.

### 18. «Balance of the hyperbolic branch: all orders in a model, real transfer open» (L166)
- **PROVED for the model:** phi_a=exp(−a cosh 2t): operator H=−d²/dr²+a²e^{2r} independent of u, Green
  ⇒ Gram of (M_a(u)+M_a(v))/(u+v) in every dimension; Robin extension phi_{a,β}=(β+a cosh 2t)phi_a.
  **Reusable** (models only).
- Discards: Phi is not a pure positive mixture of exp(−a cosh 2t) nor a convolution of a fixed model with a finite positive
  measure (§7); −a∂_aK_a not PSD (§9).
- OPEN: deformation by Phi/phi_{2π} introduces a source; asymptotic rank-one residual, zero on
  contrasts. §10: absorbing the source into a parameter-independent scalar potential forces a constant
  prefactor.
- Reopening: «a preserving operation applicable to the real Phi or an independent estimate of the whole
  correction, valid for any dimension».

### 19. «Rereading the scalar bridge: preserving the averaged obligation» (L182)
- Result: u^{2N}W[h_{N,k}]=Σ_j(−1)^j C(k,j) b_{N+j}: asking for those signs is the same obligation. The signed
  AVERAGE R_L ≥ −ε_L, ε_L→0 for each initial entry (not each atom) suffices. R_L=A_{N,k}−C_L, C_L→0
  does not prove the bound.
- Reusable: no (precision of the obligation).

### 20. «Consolidated status of the temporal kernel and the theta truncations» (L189)
- Result: PSD of the transformed kernel ⟺ temporal PSD (Gaussian bound); by holomorphy PSD on
  any open interval suffices (GRAM §2.1–2.2). **Reusable** (continuation principle).
- Discards: each mode, EVERY finite theta prefix, positive smooth cutoffs with finite Σw_n n² fail PSD on
  any interval; adding a continuous tail fails for M large; symmetrizing fails for every M.
- Decision: do not use pointwise smallness of the tail nor a fixed number of derivatives as a transfer.

### 21. «Deduplication of the theta primitive: keeping the boundary before transforming» (L197)
- Result: Phi=(D²−1/4)q/2 (E101_070 §4); Z_Phi(u)=1/4+(u²−1/4)∫_0^∞q cosh(ut)dt (affine, not a product);
  g=2e^{−|·|/2}*Phi, Z_g=2Z_Phi/(1/4−u²); K_g−K_Phi=2(1/4−uv)/[(1/4−u²)(1/4−v²)] indefinite (two-node
  det −(u−v)²/…<0). No PSD order between the two kernels.
- Reusable: identities (no sign).

### 22. «The regularized primitive is not a PSD temporal kernel either» (L216)
- Label: **PROVED**. U=2cosh(t/2)−F=2g; (4/5)e^{−t/2}<U<e^{−t/2}; minor at nodes (0,8) of A_U:
  det < −(124/25)e^{−8} < 0.
- Reusable: no.

### 23. «Hyperbolic multiplicative transfer: discard prior to another study of models» (L247)
- Result (HYPER §11): Phi ≠ C exp(−a cosh 2t)Π cosh(α_j t) with finite Σα_j² (a=2π, Σα_j=9/2, multiplicity
  π−3/(2π) not an integer). Does not exclude real powers, quotients, other prefactors nor comparisons of forms.
- Reusable: no.

### 24. «Jacobi product: the lost moment prevents using its cutoffs as PSD kernels» (L253)
- Result: criterion GRAM §8.4 (proved/audited): zero exponential moment of a nonzero density ⇒ A not
  PSD; discards all nonconstant polynomial cutoffs in q=e^{−πe^{2t}}, including finite Jacobi ones.
  §8.5: symmetrization of those cutoffs introduces a tail β=2J+1/2; two close nodes give det<0.
- Reopening: a compensation preserving the complete moment.
- Reusable: the zero-moment criterion (falsification tool).

### 25. «Return to (S): deduplicated divisor commutator and corrected normalization» (L261)
- Result: ZΔ=[L,Z] already in N_BUILD_022 §1; it gives no lower bound for Arch−Div−Near. Factor-2 correction:
  D_sym is HALF of Div_P47; sᵀDiv_P47 s=2sᵀ(Z^{−1}LZ−L)s. NO-GO of N022 §3 becomes ARGUED.
- Reusable: corrected normalization.

### 26. «Complete Selberg: domain precision when separating the squares» (L267)
- Result: Re⟨g,B²g⟩=‖Bg‖²−½‖(B−B*)g‖²; the first integral diverges (≥½Σ_{p≤X}log p/p); only the
  difference with common cutoff converges to V of 055. Does not refute compensated Selberg.
- Remainder: joint comparison with ARCH and polar. Reusable: no.

### 27. «Weak modal damping does not give PSD approximants either» (L282)
- Result: phi_δ=Σn^{−δ}Phi_n not PSD for EVERY δ≠0 (GRAM §8.6); ∫e^{t/2}phi_δ=0 versus 1/4 for Phi.
- Reusable: no.

### 28. «Audit of open residues: sufficiency and antecedents» (L288)
- Result: correction of 06: R172_CAND keeps two obligations; ROUND026 does not certify the polar block.
  (N) is a sufficient target with a joint signed estimate pending; R8 needs an independent positive carrier
  + identification with domains; R10 without a concrete inequality.
- Reopening: Arch−Div−Near by Poisson/divisors, family s_w, tails with gauge, near patterns: only with
  «an explicit new hypothesis resolving its identified failure».
- Reusable: no.

### 29. «Hyperbolic additive comparison: two necessary conditions without a falsifier» (L294)
- Status: comparison K_Phi−K_{2π} subsequently FALSIFIED (§33). Kept: x·N_diff(x)=9/4+(3/16−2π²)/√x+…;
  Jensen test n0 ≥ (9/4)C^{8/9}; NUMERICAL diagnostic (n0≈0.00915 > threshold≈0.00555).
- Reusable: no («Do not relaunch this check as a construction»).

### 30. «Geometric interpolation: antecedent filter and exact obligation» (L315)
- Object: phi_s=phi_0 e^{sh}, h=log(Phi/phi_0); ∂_sK_s=[Cov_{s,u}(t,h)+Cov_{s,v}(t,h)]/(u+v).
- Result: PSD of the derivative for each s is STRONGER than the integral; model counterexample
  h=a cosh 2t (derivative −a∂_aK_a not PSD). Scope precision: the falsifier does not exclude a
  RELATIVE bound ∂_sK_{s,U} ≥ −C_U(s)K_{s,U} with C_U integrable for each finite list U (Grönwall; constants
  depending on U suffice).
- Status: interpolation and integrated comparison OPEN.
- Reopening: a specific property of h giving the relative bound and its integrability without assuming the sign.
- Reusable: covariance identity (no sign).

### 31. «Grouped divisorial covariance: the coefficients have both signs» (L328)
- Label: **PROVED**. C_s(n)=Σ_{dm=n}μ(d)log m(gcd(d,m)^s−1); C_s(p²)=−(p^s−1)log p<0;
  C_s(p²q²)=(B−1)(A−2)log p+(A−1)(B−2)log q>0 if p^s,q^s>2 (p=5,q=7 at s=1/2).
- Falsifies only the uniform sign of the COEFFICIENTS. Reusable: no.

### 32. «The divisorial remainder is indefinite even on even primitive tests» (L351)
- Label: **PROVED**. R(F)=Σn^{−1/2}C_{1/2}(n)Re c_F(log n). Palindromic tests with c₊=(1,−5/2,1),
  c₋=(1,−3/2,−1/2,−1/2,−1/2,−3/2,1) (both moments zero, T=3log4+ε): R(F₊)=(7/4)κ‖g‖²>0,
  R(F₋)=−(1/4)κ‖g‖²<0, κ=(√2−1)log2.
- Rules out using R or −R as an isolated positive piece. Does not refute compensation with ARCH. Reusable: no.

### 33. «Fitted Robin comparator: fails already on distant pairs» (L390)
- Label: **PROVED**. M_*=wbM_{a,β}(bu), w=7/2, b=2/7, a=4π/7, β=4π²/49−33/392; D=M_Phi−M_*=d/u³+…, d>0;
  det K_D|_{(u,2u)}=−5d²/(64u⁸)+…<0.
- **Reusable general filter (PROVED):** if D=o(1/u) on a half-line and K_D is PSD on all its pairs,
  D≡0. **Reusable** as a comparator filter.
- NUMERICAL diagnostic N_Phi(0)−N_*(0)≈0.00454>0 (does not intervene).

### 34. «asinh comparator: certified negative confluent minor» (L428)
- Label: **PROVED with interval certificate**. M_0=½asinh(u/4π): K_0 PSD (positive resolvents).
  Jets J=[[n10,n11],[n11,n12]] of N_D: det J ∈ [−1.684,−1.683]·10^{−57}<0 (SHA dff604bc…).
- Result: K_Phi−K_0 NOT PSD (and on no open interval, by GRAM §2.2). Reusable: no (discard);
  the positivity of K_0 is, however, an explicit PSD model.

### 35. «Original hyperbolic comparison: certified indefinite remainder» (L467)
- Label: **PROVED with interval certificate**. det J ∈ [−3.307,−3.306]·10^{−59}<0 (SHA 6749a763…).
- Result: K_Phi−K_{2π} not PSD (nor on an open interval). K_{2π} remains PSD. Reusable: no.

### 36. «HCM, reciprocity and supertails are not enough for the logarithmic kernel» (L496)
- Label: **PROVED**. Countermodel f_ε=C(1+x)^{−2}exp[−ε(x+1/x)], ε=2^{−100}: HCM, reciprocal, all
  Mellin moments; κ4>0 ⇒ det K|_{(h,2h)}=−(κ2κ4/6)h²+…<0.
- Scope: refutes the sufficiency of HCM+reciprocity+moments (with parity, analyticity, supertails).
  Reopening: an additional inequality proved for the complete datum that excludes this example.

### 37. «The theta density in S=exp(2t) is not HCM» (L546)
- Label: **PROVED**. H(w)~(π⁴/Z0²)w^{9/2}e^{−2πw} incompatible with log-convexity ⇒ f not HCM; nor
  its tilts x^r nor scalings.
- Reusable: no.

### 38. «Primitive comparisons: analytic transfer of the discard» (L576)
- Label: **PROVED**. **Lemma:** D odd real-analytic on R, c>0: PSD of K_D on all blocks of
  an open interval I⊂(c,∞) with Σd_i/(u_i−c)=Σd_i/(u_i+c)=0 ⟹ complete PSD (CPD2 + anchors +
  continuation + masses at ±c).
- Application: K_Phi−K_{2π} and K_Phi−K_asinh also fail on primitive blocks of any I⊂(1/2,∞).
- **Reusable:** the lemma (primitive ⟺ complete for kernels of this type).

### 39. «Normalizing by Phi does not produce a positive translational derivative» (L608)
- Label: **PROVED**. B=A/(Phi(t)Phi(s)), C=−(∂_t+∂_s)B=t+s−(p(t)+p(s))B; C(0,0)=0, ∂_sC(0,0)=1−aB(0,0)>0
  ⇒ minor −C(0,s)²<0. Corollary (PROVED): no even analytic normalization g repairs the generator
  (C_g odd ⇒ C_g=0 ⇒ B_g=F(t−s), impossible by H(L,L)=1−1/(4L²)+…).
- Reusable: no.

### 40. «Generator with exponential tilt: initial diagnostic and later discard» (L641)
- Status: identities and necessity c≥1 PROVED; local diagnostic NUMERICAL (det≈+0.00789); comparison
  subsequently FALSIFIED (§41). Identity B(t,s)=∫_0^∞e^{−2cr}C_c(t+r,s+r)dr for c≥1.
- Reusable: the integration identity of the generator (sufficient condition, no sign).

### 41. «Modular cusps: no generator C_c with finite c is PSD» (L692)
- Label: **PROVED**. Mechanism: real PSD ⇒ H_h(iy,−iy) ≥ 0 (jets + Taylor); as y→π/4: |Phi(iy)| ≤
  Cε^{−K}e^{−a/ε} (SMALL), |Phi(h+iy)| ≥ c0ε^{−5/2} (LARGE), A0 ≥ c1ε^{−4}, Ah ≤ C1ε^{−5} ⇒ contradiction.
- **Reusable:** the cusp estimates (SMALL, LARGE, A0, Ah) and the test (NEC) as a falsification
  tool for any kernel holomorphic in |Im|<π/4.

### 42. «Normalization by the complete diagonal: does not admit a positive tilted generator either» (L770)
- Label: **PROVED**. g_c=√A(t,t)e^{ct}, every real c; via Schur exp(4ch)R_h²−R² and DIAG-CUSP
  d(z)=−(9/16)z_*(2i)^{3/2}ζ^{−4}+O(|ζ|^{−3}). Corollary PROVED: dividing by the primitive theta F does not either.
- Reusable: DIAG-CUSP (asymptotics of the diagonal at the even cusp).

### 43. «Asymmetric theta-scale gauge: real two-point falsifier» (L843)
- Label: **PROVED**. g=exp(2π sinh 2t): nodes (−L,L), det C/P⁴ ≤ O(L²/Y)−16κ²<0. Extension PROVED: every real a
  in g_a=exp(a sinh 2t) (jets at −h).
- Reusable: no.

### 44. «Scope of RES-SOS against the remainders of 106_38» (L907)
- Result: Phi(x)=Σi^{−1/2}h_{n²i²}(v), R_n=Σ_{n∤j}j^{−1/2}h_{j²}(v): distinct frequencies; bilateral
  synthesis with c=δ_1 gives X_frac+X_ctr=0 while R_res[δ_1]>0. RES-SOS does not sign those remainders.
- Remainder: joint compensation. Reusable: identity of profiles (no sign).

### 45. «Small hyperbolic comparison: necessary vanishing condition» (L923)
- Label: **PROVED as an implication**; comparison subsequently REFUTED. Bound ‖U_f‖_HS ≤
  ½√(Tr H^{−1})(|f(0)|+‖f'‖_{L1}); K_Phi ≥ εK_h ⟹ U_Phi=0 (via W_Phi[Phi]=0, GRAM §19.12).
- Reusable: the HS bound and W_Phi[Phi]=0 (physical identity).

### 46. «Two exact phases are not ordered by PSD» (L941)
- Label: **PROVED**. Average in θ of A_θ = R_res; D=A_0−A_π has D22=0, D12>0 ⇒ indefinite.
- Subentries (L973–985), all with declared scope:
  - «Infinite symmetric closure without drift» (HYPER §12.2): ‖Q(v)‖²=A+c log cosh v; excludes a continuous
    coordinate q_θ with symmetric operators.
  - «Extension with constant scalar drift» (§12.3): excluded for α≥0 and α<0.
  - «Variable scalar drift» (§12.4): reduces to 12.3. Does not exclude operator drift, variable metrics.
  - «Moving rates and strong bridge» (BRIDGE014 §6): union dense in H_η ⟺ limsup N/u_N=∞; along N ⟺
    N/u_N→∞. **Reusable** (density threshold). W ≥ −ε_N‖f‖² missing.
  - «Arithmetic tail in the dense regime» (§7): |W−W_{≤⌈exp(40N/u)⌉}|<e^{−N}‖f‖² on V_N(u), u≥2.
    **Reusable** (tail control). Finite obligation: lower bound −ε_N‖f‖² for ARCH+POLAR and contacts
    up to exp(40N^{1/4}) with u_N=N^{3/4}.

### 47. «Phase211 — subcritical moving cutoff: necessary threshold» (L988)
- Label: **PROVED, truncated principal part only**. Cutoff log Q_N ≤ (2−δ)N/u_N ⇒ W_{≤Q_N}→−∞ on a vector of
  two Laguerre coordinates; a vanishing lower bound requires liminf u_N log Q_N/N ≥ 2.
- Reusable: necessary threshold (not a sign).

### 48. «Phase211 — moving cutoff insufficient even on primitives» (L993)
- Label: **PROVED for truncated W, not for complete W**. N ≥ 2^{60}, log Q ≤ 2^{−12}N/u: unit vector with
  zero Tate moments, f(0)=0, W_{≤Q}[f]<−3.
- Reusable: no.

### 49. «Closure of the small hyperbolic comparison» (L998)
- Label: **PROVED, computer-assisted: K_Phi does not dominate εK_{2π} for ANY ε>0.** λ1 ∈ [a²+4a√3−9, 25+a²(5/4)³],
  17<ω1<41/2; certificate G(ω)<−10^{−8} on [17,41/2] (SHA cddcc0bf…); U_Phi v1=G(ω1)v1≠0.
- Subentries: «Primitive scope of the closure» (by the lemma §38, fails on primitive blocks of every
  I⊂(1/2,∞)); «Primitive physical family» (g_R=(D²−1/4)(χ_RPhi), zero moments, W[g_R]→0 while
  2‖U_{g_R}‖²_HS → a positive value).
- **Reusable:** f_*=(D²−1/4)Phi with W[f_*]=0 and the primitive family g_R (almost-null tests of W).

### 50. «Phase211 — direct bibliographic antecedent of the temporal kernel» (L1052)
- Result: external public manuscript with j=A/(∫Phi)² and the same logarithmic response (representation
  antecedent). Causal companion: separate majorant ≥[1/(r−1/2)−1/(4r)]/B0(r) diverges as r↓1/2; does not imply
  divergence of the real norm of k.
- Remainder: uniform bound of the inverse of the causal operator. Reusable: no.

### 51. «Theta branching: candidate examined, preservation OPEN» (L1060)
- Object: step T'=A1T1+A2T2 (BPY), symmetrization S.
- Result: seed S δ_c with M=b tanh(bu) PSD (explicit Gram); NUMERICAL diagnostic of jets 0..4 positive.
  Entropy term without sign; signed boundary (p−1)F(p)=B_1(p)−2B_{1/4}(p).
- Subentries: loss of information (S δ_c=S δ_{1/c}, distinct outputs); the fixed mean does not determine
  the step either (ν with Rν=−ν, μ±); fourth cumulant κ4_output<−1/5000 for EVERY c>0 (interval certificate,
  does not falsify); conditioning: C(u,u)=−Var_ν(h_θ)u²/2+…<0 at the second step.
- Status: preservation OPEN. Reopening: «a concrete joint estimate for the step or a justified
  falsifying test».
- Reusable: PSD seed (the seed only).

### 52. «External source for window log11: CITED, pending reproduction» (L1187)
- Final label (L1213): **PROVED with computational assistance, EXTERNAL result reproduced**, complete
  form W_T in both parities, 0<T ≤ log(11)/2 (≈1.1989). Verified local frontier moves from 1.035 to
  log(11)/2. Gives no spectral margin nor uniformity.
- Reopening of windows: «a uniform structural estimate of the complete Schur block is missing».
- Reusable: yes (certified window; not original, not for all T).

### 53. «Subtraction of two smooth cutoffs: principal part and pending remainder» (L1216)
- Result: Q_M(v)=MA(v)+(1/2π)∫Phi s_N[2Re(C_M conj R_M)+|R_M|²]; every smooth compactly supported v is a difference of
  two cutoffs ⇒ the principal part keeps the global obligation. «Neither a new route nor a falsifier».
- Remainder: sign of the remainder, uniform bound for M-dependent interpolants.

### 54. «BPY density: additive infinite PF and reciprocity, multiplicative bridge OPEN» (L1227)
- Results PROVED (classical, applied): Phi(½log v)=πv^{5/4}q(v), q(1/v)=v^{5/2}q(v), 2π∫q=1,
  L(s)=Π(1+s/(πn²))^{−2}; det[q(x_i−y_j)] ≥ 0 at all sizes (additive PF∞); q_aq_a''−q_a'²<0 per mode
  (no contradiction).
- Formula: A(t,s)=π²(ab)^{5/4}/4∫_1^∞v^{3/2}log(abv²)q(av)q(bv)dv.
- Subentries: consequence of the package −(log Phi)'' ≥ 5 (PROVED); exponential Gamma(2): A_a(t,t)<0 for
  very negative t (without reciprocity); symmetrized finite approximants: A[S_N] not PSD and f̃_N not PF₂.
- Status: multiplicative bridge OPEN. **Reusable:** additive PF∞ of q, the formula for A, −(log Phi)'' ≥ 5.

### 55. «Rigidity against finite modifications of BPY rates (delimited class)» (L1318)
- Label: **PROVED**. Modifying finitely many rates (two copies of π intact, the rest >π) and requiring
  reciprocity ⇒ R≡1, f=2πq.
- Reusable: yes as a restriction (there is no other reciprocal law in that class).

### 56. «Additive BPY renewal and reciprocal mixture: construction, no sign bridge» (L1368)
- Result: v f(v)=∫_0^v k(v−u)f(u)du, k=2Σe^{−πn²x}; P_down, P_up transitions of mass 1; the
  equiprobable mixture is not reversible for any density (cocycle R(L,2L)R(2L,3L)/R(L,3L)~1/√(2L)).
- Reusable: renewal identity (exact).

### 57. «Folded bilinear renewal identity and failure of its individual slices» (L1396)
- Label: **PROVED within the stated scope**. A(t,s)=∫∫f(u)f(w)B_ab(u,w)dudw exact; symmetric slices
  S^{(u,w)} not PSD on any interval of (1,∞) (confluent det −C²/δ+…). Corollary: integrating a source
  (C_ab(u)) does not either: −uf(u)²(log u)²/(256δ)+…<0.
- Reusable: the identity (no sign).

### 58. «BPY self-decomposition by scale: auxiliary positive energy, no transport of the orbit» (L1460)
- Result: cX+Y_c ~ X; generator G with −Re∫h̄Ghf=½∫∫fρ|h(x+y)−h(x)|² ≥ 0 (PROVED); the semigroup does not
  preserve the orbit of dilations (Var defect −2σ²c(1−c)(d−1)≠0).
- Reusable: the positive auxiliary energy (not identified with A).

### 59. «The resonant budget requires a one-sided comparison, not a uniform norm» (L1492)
- Label: **PROVED only within the following scope, y=0**. Blocks k..k+N−1, k>N²: R diagonal,
  R^{−1/2}AR^{−1/2}→J_N; refutes Off ≤ CR and |Off| ≤ CR for every C. Does NOT refute H ≤ I.
- Status: Off ≥ −R OPEN.

### 60. «Factorial extension before resonance: complete identity with signed remainders» (L1512)
- Exact identity (PROVED): Q[c]=Σ_mΛ(m)‖P_mb−R_mb‖²_K+b*Db+E(b). Entries of D positive but D not PSD;
  E(δ_1)<0.
- Subentries: E is not paid by squares alone (S_sq[δ_1]=0, E<0); kernel of S_sq = squarefree support
  (Q=D+E there); on SF, Q=L+M, 0 ≤ B ≤ L (PROVED), B+M ≥ 0 FALSE (test c=(1,−1/100), rational bounds).
- **Reusable:** factorial identity, SF kernel, Q=L+M and 0 ≤ B ≤ L.

### 61. «Squarefree scales: graph approximation and exclusion of every fixed fraction» (L1615)
- Result PROVED: the closure of the span of P_d, d SF of a tail, contains all P_k and the compactly supported ones
  (Schwarz + Σ_{SF}1/d=∞). Q ≥ ε(L−B) false for every ε>0 (family g_R). Consequence: D+E not PSD on
  finite theta; Q ≥ εS_sq false; S_sq not continuous on B_a².
- Status: Q ≥ 0 (α=1) OPEN. **Reusable:** SF density in B_a².

### 62. «Scalar resolvents of the product: positivity by parameters fails» (L1671)
- Result PROVED: A=∫_0^∞J_u du; J_u not PSD for every 0 ≤ u<1 (limiting diagonal <0); on finite SF for u
  in [0,η).
- Subentry «Reciprocal pairing»: C_u=J_u+u^{−2}J_{1/u}, A=∫_0^1C_u du, C_u(x,x)>0 for all x; candidate
  OPEN; obligation: integrated crossing inequality for C_u or a falsifier.
- Reusable: the identities (Frullani, pairs).

### 63. «Reciprocal endpoint C_0: positivity of all orders (not a closure of A)» (L1725)
- Label: **PROVED**. C_0=∫2sinh(2r+x+y)Phi(r+x)Phi(r+y)dr; (a+b)Ĉ_0=Z(a+1)Z(b+1)−Z(a−1)Z(b−1);
  S(a)=Z(a−1)/Z(a+1) contractive on Re a>0 (explicit quotient with Euler product and Bernoulli);
  K_S PSD (Hardy) ⇒ C_0 PSD at all real nodes.
- **Reusable:** C_0 PSD, all orders (scope: u=0, measure zero in A=∫C_u).

### 64. «Two transports from C_0 that do not preserve the required sign» (L1778)
- Label: **PROVED in the declared classes**. q_u log-concave ⇒ not a Schur multiplier; there is no fixed
  positive measure μ with C_u ≥ ∫C_0(x+t,y+t)μ(dt) (D_u ≤ u^{−1}e^{−2x}D_0).

### 65. «The positive hyperbolic endpoint does not imply the linear limit: smooth countermodel» (L1808)
- Label: **PROVED in a generic class**. phi=3g+(g(t−2)+g(t+2))/2: B_1 PSD at all orders, B_0 not PSD
  ((42,−41)K(42,−41)ᵗ=1−516/(34ℓ)<0).
- Status: descent for theta OPEN (requires an additional hypothesis or identity).

### 66. «Additive PF and inversion: exact defect of the composition by contractions» (L1859)
- Label: **PROVED in the declared class**. V_λ not contractive on L²(x^{3/2}dx) for any λ>0.
  Cross-check: x²f=(k*k+xk)*f, Möbius conjugation: repetitions stopped.

### 67. «The complete BPY product is not bounded in the reciprocal metric either» (L1882)
- Label: **PROVED, precise class**. ‖T_fh_ε‖_H ≥ cε^{−1/4}→∞; away from the boundary ‖T_fh_R‖²−‖h_R‖²>0.
  T_fq ≠ q.

### 68. «Single falsification diagnostic of the pair C_1» (L1918)
- Label: **NUMERICAL exploratory, NOT certified**. Block of 5 nodes, eigenvalues approximately positive.
  Candidate OPEN.

### 69. «Keeping both branches does not restore the usual monotonicity of the physical process» (L1930)
- Label: **PROVED, precise class**. dQ_x(z)/dx|_0 <0 (K'/K(u0)<−19) ⇒ does not preserve the usual order.

### 70. «The physical semigroup does not preserve even convex functions either» (L1970)
- Label: **PROVED**. (A_markov f_R)''(0)/(2c) → <(2−38/3)K0<0.

### 71. «Duplication control: integration by parts of T and weighted energy» (L2016)
- Label: **Identity verified, NO new inequality**. Q(P)=(π²/2)[4E_4(P')−6E_2(P)−6∫t^{3/2}|P|²],
  P(1)=0. Reformulates as E_4(P') ≥ (3/2)[E_2(P)+∫t^{3/2}|P|²]; not proved.
- Reusable: identity.

### 72. «Conjugate imaginary translations: do not bound the complete form from below either» (L2040)
- Label: **PROVED**. There is no fixed μ ≥ 0 with B ≥ ∫K_η dμ(η), B=A or C_u: K_η(x,x)/D_0 ≥ 1/2,
  A(x,x)/D_0(x) ≤ x/sinh(2x)→0.
- Reusable: the bound A(x,x) ≤ (x/sinh 2x)C_0(x,x), x>0.

### 73. «The integrated quotient A/C_0 is not a positive multiplier either» (L2080)
- Label: **PROVED**. H=A/C_0: H(x,−x)→1/2, H(x,x)→0 ⇒ det→−1/4; H_u analogous −(1+u)^{−4}. Gauges do not repair.

### 74. «Control of the orthogonal substitution in the factorial identity» (L2129)
- Label: **PROVED as an application of earlier density**. Π_m=I; Σ_mΛ(m)‖F−R_mF‖²=∞.

### 75. «Theta operator realization: piece built, sign pending» (L2142)
- Label: **PROVED, not a sign** (HYPER §12.6): H=L²(sech(πω/2)dω)⊕R³, Q=(cos ωv, cosh(v/4), cosh(5v/4),
  cosh(9v/4)), explicit continuous/discrete D, q_θ=Phi(v/2)e^{2π cosh v} exact observation. Integral
  extension: Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).
- Bounded local metric impossible (§12.7, PROVED, class). Does not decide unbounded/nonlocal metrics.
- **Reusable:** the realization (objects and exact observation).

### 76. «Laplace of the reciprocal pairs: valid identity, slice premise subsequently refuted» (L2153)
- Identities PROVED: C_u=∫e^{−uv}D_v dv, A=∫[(1−e^{−v})/v]D_v dv, D_v/v→C_0. Premise «D_v PSD ∀v» FALSIFIED.
- «Factorization trial stopped»: the term vab does not produce a non-diagonal form in (n,m).

### 77. «The Laplace slice D_(2pi) is indefinite: certified falsifier» (L2183)
- Label: **PROVED by intervals with complete analytic tails**. (d1+e)d0−2c² ∈ [−6e−21 ± 8.08e−22]<0;
  test (1,−1/1300000,1) upper −11286479/4.225·10^{23}<−2.6e−17 (SHA e6fee17a…).
- Corollary: no complete monotonicity on every ray u ≥ U. NUMERICAL control at u=1/(2π): positive.
- Status: integrated compensation in v open.

### 78. «Primitives of the slices: deduplication and limit of the argument by radicals» (L2251)
- Result: G_V, F_R, A=∫[−w'(V)]G_V dV; PSD of all G_V «is NEITHER proved nor refuted»;
  G_V(x,x)/C_0(x,x) ≤ V/[2sinh 2x]→0 but →1 as V→∞: limits do not interchange.
- Decision: do not launch a campaign. Reusable: identities.

### 79. «Shifted cosh products: extension discarded before preservation» (L2273)
- Label: **PROVED in a delimited class** (HYPER §13, §13.1: base exp(−a_n cosh 2t), a_n>0 variable,
  factors (cosh(bt)−c)/(1−c)). Not other bases/factors.

### 80. «Later duplication control: four proposals without construction» (L2280)
- Label: **CROSS-CHECK RECORD; no new mathematical result**. (i) nodal localization of a negative witness;
  (ii) positive rates before T; (iii) Jensen/operator concavity; (iv) BPY even/odd scale 1/4.
- Reopening: «an explicit additional claim that controls the indicated obstacle and connects with the complete
  form».

### 81. «Geometrically symmetrized BPY approximants: inconclusive G2 examination» (L2292)
- Label: **OPEN / NUMERICAL exploratory**. G_N=√(Phi_N(t)Phi_N(−t)); f_2=Ce^{−av}H(dv); G_2 tail
  [8π³/(3√6)]e^{−2|t|−π cosh 2t}. Positive jet diagnostic (not certified).
- Reopening: «a new structural hypothesis».

### 82. «Passage to the limit of the geometric approximants: uniform domination» (L2313)
- Label: **PROVED as an analytic bridge, not a sign**. E e^{πY_N}=[2N/(N+1)]² ≤ 4; G_N ≤ 2π²e^{−π cosh 2t}
  (G-DOM); A[G_N]→A[Phi] locally uniformly.
- **Reusable:** PSD of A[G_N] for infinitely many N ⟹ global sign.

### 83. «Later filters: consecutive coupling and simplex» (L2345)
- Label: **CROSS-CHECK RECORD**. Common innovation and simplex/Dirichlet(2,…,2) without a signed identity.
- Reopening: an explicit joint inequality or a concrete falsifier.

### 84. «Later filter: compensated variation of two BPY rates» (L2354)
- **CROSS-CHECK RECORD**. Covered by rigidity (§55) and interpolation (§30). Not enabled.

### 85. «Later filter: cutting a Gaussian bridge realizing the BPY law» (L2362)
- **CROSS-CHECK RECORD**. Reopening: «specify and justify the boundary operator or the cutting identity
  giving the complete A, with positive measure and without a pending sign remainder».

### 86. «Later filter: label operator on the squarefree sector» (L2370)
- **CROSS-CHECK RECORD**. GRAPH: G(P_d)=(log d)Θ_d/2, G=(T Lg)/2−CT; replacing it by an Euler derivative omits the
  cancellation. The SF kernel corresponds to S_sq, not to RES-SOS.

### 87. «Consecutive BPY comparison with sech congruence: analytic falsifier for every c>0» (L2376)
- Label: **NO-GO PROVED in the declared comparison**. A_2 − c sech(2x)A_1 sech(2y) not PSD ∀c>0
  (A_2(iy,−iy) ≤ M/8, A_1(iy,−iy) ≥ a_*, factor 1/cos²(2y)).
- Reusable: H does not vanish on Re z>0; G_2 holomorphic in |Im|<π/4.

### 88. «Extension: no nonzero holomorphic congruence transfers G1 to G2» (L2440)
- Label: **NO-GO PROVED in the declared class** (D holomorphic in the strip, real on R ⇒ D≡0).

### 89. «Closure of the diagonal transfer: automatic regularity of the factor» (L2471)
- Label: **NO-GO PROVED for EVERY real factor** D:R→R arbitrary ⇒ D≡0. Does not exclude non-
  diagonal transfers.

### 90. «Later filters: triangular transfer and two boundary sections» (L2529)
- **CROSS-CHECK RECORD**. (1) Th=h+∫_x^∞k(x,s)h(s)ds with neither k nor intertwining specified: not excluded.
  (2) Alignment of two roots of H(iu): does not control the others.
- Reopening (1): an explicit mechanism controlling crossings, weight 2r+x+y and boundaries, extendable to the sequence;
  (2): joint control prior to blocks.

### 91. «Deduplication: positive differential factors on the fixed model» (L2539)
- **Application of an existing discard**. ΔK=f(u)f(v)+g(u)g(v) ⇒ K_new ≥ K_{2π}; reaching K_Phi would require
  K_Phi ≥ K_{2π}, FALSIFIED.

### 92. «G2: the boundary derivative energy exceeds any fixed collection of branches» (L2554)
- Label: **PROVED within the stated scope**. E_x(ε)/log(1/ε)→+∞; each fixed collection of branches contributes
  O(log 1/ε). B_x(ε)=E_x(ε)−|G2(x+iy_ε)|².
- Pending: |B_12|² versus B_11B_22. PSD of A[G2] neither proved nor refuted.

---

## A. Deduplicated «do not relaunch» list, with reopening condition

Each item: what is not relaunched / reopening condition according to the source / status in `RULES_AVOID.md` §D.

1. Pure arithmetic SOS for T ≥ ½log3 / explicit joint factorization of Arch and all contacts with
   Tate (L17) — in §C of RULES_AVOID («pure arithmetic SOS (empty for T ≥ ½log3)»), not in §D; reopening
   absent.
2. Near in absolute value, reindexed Euler, separate Cauchy–Schwarz, rewriting as a convolution / uniform joint signed
   inequality Arch–m≈kn (L27, L101) — **D8** only mentions «Arch − Div − Near by
   Poisson/divisors». The positive condition of L27 is missing.
3. Continuation of the first contact / nonlinear global defect (197) / signed bound of the endpoint or of the rest of the
   path or an independent obstruction (L35) — absent from §D.
4. Density of the filtered union / see item in E (D3 inaccurate).
5. Descent 036 / R_L ≥ −ε_L **or** a family of jointly positive subspaces approximating in a topology where
   W is continuous (L43) — **D4** omits the second alternative and the precision «average, for each initial
   entry, not atom by atom» (L186).
6. Compact EVEN repair of the representative (045) / noncompact representative with global identity (L51) —
   absent.
7. Grouping close nodes without a relative inequality for crossings (L67) — absent.
8. Comparisons of Off against divisorial energy / fixed fraction of R_res / dilations with weight 1+log t (L69,
   L1507) — **D9** correct; missing that there is no uniform UPPER bound either (L1507) and the discard §17.7.
9. Mellin or the change u=½log t as a mechanism (L77) — covered by A4.
10. Theta Gram by slices / even-odd sectors / modularity by mode (L90–94) — absent from §D (the project rules cite it
    as «Change (m,n)…»); D16 includes it partially.
11. «Cells/Euclidean division» without a factorization pairing the small-divisor defect and the second-order boundary
    (L101) — absent.
12. Assembly of fixed-support PSD certificates — **D12** correct.
13. K − K_shift; IMS repair — **D13** correct; the IMS repair (L121) is missing.
14. Positive Laplace representation of L' on any ray (L138) — absent.
15. Gaussian subordination of N as a new representation (L147); premise of universal Gaussian inverse positivity
    (L156) — absent (D6 covers it generically).
16. Variants of budget 022 — **D7** correct.
17. Positive mixtures/convolutions of exp(−a cosh 2t), scale monotonicity −a∂_aK_a, sequence of models / preserving
    operation for the real Phi or estimate of the whole correction (L176) — B4 mentions it; absent from §D.
18. Pointwise smallness of the tail / fixed number of derivatives — **D10** correct.
19. Theta prefixes, smooth cutoffs with finite Σw_n n², continuous tail, symmetrizations, Jacobi cutoffs, damping
    n^{−δ}, regularized primitive U (L193, L245, L257, L286) — absent from §D.
20. Multiplicative cosh products (§11, §13, §13.1) — in §C («closures by cosh products»), without class scope.
21. Commutator ZΔ=[L,Z] as a bound (L263) — absent.
22. Splitting Selberg into two finite energies (L280) — absent.
23. ARCH−Div−Near by Poisson, s_w, tails with gauge, near patterns — **D8** correct.
24. Asymptotic/Jensen tests of K_Phi−K_{2π} as a construction (L312) — absent.
25. Geometric interpolation phi_s with PSD of the derivative at each s / integrable relative bound ∂_sK ≥ −C_U(s)K
    (L323) — absent; RULES_AVOID B4 treats it as a closed pattern («interpolations»), which is stronger than the
    source.
26. Uniform sign of coefficients of the divisorial covariance; R or −R as a positive piece (L348, L387) — absent.
27. Additive comparators K_Phi − K_* (fitted Robin, asinh, hyperbolic 2π), also primitive; filter D=o(1/u)
    (L421–L605) — absent from §D.
28. HCM + reciprocity + moments as sufficient hypotheses; HCM of the theta density (L543, L573) / additional
    inequality excluding the countermodel — absent.
29. Normalized translational generators: by Phi, by even analytic g, by e^{ct}Phi (every c), by √A(t,t)e^{ct},
    by √d/F, by exp(a sinh 2t) (every a) (L627–L904) — absent; the project rules «Transport by shift and
    congruence» (D16) covers it partially.
30. Poincaré/lossy paths as a consequence of RES-SOS for remainders 106_38 (L921) — absent.
31. PSD order between phases A_0, A_π (L970) — absent.
32. Symmetric continuous coordinate without drift / constant or variable scalar drift (L973–979) — absent (D15 covers
    only §12.7).
33. Optimization of constants of the fixed margin 9 (L982); polynomial moving cutoffs (L990–995) — D2 covers it
    generically.
34. Theta branching: tower of certificates, «another coordinate of the remainder» (L1079) / joint estimate of the step
    or justified falsifier — absent.
35. Campaign of windows (log11) without a uniform structural estimate of the Schur block (L1213) — D2 generic.
36. Tower of determinants for PF∞ + reciprocity (L1269) — absent.
37. Finite modifications of reciprocal BPY rates (L1365); variation of two rates (L2360) — absent.
38. Reversible P_down/P_up mixture (L1393) — absent.
39. Slices of the folded renewal and integrated source (L1438, L1457) — absent.
40. Self-decomposition semigroup as transport of the orbit (L1489); even/odd scale 1/4 — **D11** covers the
    latter.
41. D ≥ 0 and E ≥ 0 separately; E ≥ −C·S_sq; B+M ≥ 0; Q ≥ ε(L−B); Q ≥ εS_sq; substitution Π_m (L1558–L2139) — D16
    covers «factorial squares» and the orthogonal substitution only by name.
42. Individual resolvent slices J_u (L1708) — absent.
43. Transports from C_0: multiplier q_u, mixtures of real translations, conjugate imaginary translations,
    quotient A/C_0 with gauges (L1805, L2077, L2126) — B4 cites «Two transports from C_0»; the other two are missing.
44. Descent B_1 → B_0 without an additional hypothesis (L1856) — absent.
45. Contractivity of factors V_λ and of the BPY product in the reciprocal metric (L1877, L1915) — absent.
46. Stochastic monotonicity of the physical process, even convex cone (L1967, L2013) — absent.
47. Hardy on the positive norms for the identity of T (L2037); rates before T — D11 partial.
48. Slices D_v PSD for all v; expansion in v; factorization vab (L2180, L2238) — in §C («Laplace slice D_{2π}»).
49. Primitives G_V, F_R without an additional theta operation (L2270) — **D16** («compensated primitives»).
50. Finite campaigns on G_N, G_2 (L2310); consecutive coupling, simplex, Gaussian bridge, label
    operator (L2352–L2374) — absent.
51. Diagonal congruence G1→G2 with any real D (L2527) — RULES_AVOID B4 («BPY congruence G1→G2»).
52. Triangular transfer with unspecified k; alignment of two branches (L2533–2535) / see §90 — absent.
53. Factors (D_t²+λ) on the fixed model 2π (L2550) — absent.
54. Isolating one or two branches of G2 as diagonal energy (L2611) — absent.

---

## B. Positive results PROVED (with exact scope)

1. HK > J² and PSD of sufficiently small symmetric temporal triples (GRAM §12; L62).
2. R_res (exact resonant part) admits SOS of all orders, valid at y=0, with uniform margin relative to its
   divisorial energy (GRAM §17, §17.5; L68).
3. Reduction: PSD of the complete A at y=0 on blocks of integer scales ⟺ PSD on real nodes ⟺ λ_A(T) ≥ 0 ∀T (GRAM
   §18, §18.9; L69).
4. Plane span{E1,E2} signed with rational bounds (GRAM §19.9; L71). Q(E1)>1/2000.
5. Reduction to tails of degrees E_j, j ≥ J for fixed J (GRAM §19.10; L72).
6. Identity of the causal potential J*Θ (GRAM §19.12; L75) — identity, unfavourable sign.
7. Hyperbolic model phi_a and Robin extension: Gram in every dimension (HYPER §§1–9; L170).
8. Continuation principle: PSD on an open interval ⟹ PSD on R for holomorphic kernels; transformed PSD ⟺
   temporal (GRAM §2.1–2.2; L191).
9. Pair filter: D=o(1/u) and K_D PSD on pairs ⟹ D≡0 (L423).
10. Lemma primitive ⟺ complete for K_D with D odd real-analytic (L586).
11. asinh model: K_0 PSD (L432–440).
12. Cusp estimates SMALL/LARGE, A0 ≥ cε^{−4}, Ah ≤ Cε^{−5}, DIAG-CUSP (L730–816).
13. Density/tail bounds of BRIDGE014 §6–§7: threshold limsup N/u_N=∞; |W−W_{≤⌈exp(40N/u)⌉}|<e^{−N}‖f‖² on V_N(u)
    (L982–985).
14. W[f_*]=0, f_*=(D²−1/4)Phi; primitive family g_R with W[g_R]→0 (L1043–1049).
15. Complete window W_T ≥ 0 for 0<T ≤ log(11)/2, both parities (external result reproduced; L1213).
16. Seed S δ_c: M=b tanh(bu), kernel with explicit Gram (L1066–1069).
17. Additive PF∞ of q; 2π∫q=1; L(s)=Π(1+s/(πn²))^{−2}; formula for A in q; −(log Phi)'' ≥ 5 under the package
    (L1231–1278).
18. Rigidity of the reciprocal law under finite modifications of rates (L1318–1365).
19. Renewal v f(v)=∫k(v−u)f(u)du and its folded version (exact identities; L1374, L1406–1413).
20. Positive auxiliary energy of the self-decomposition semigroup (L1476).
21. Factorial identity Q=Σ_mΛ(m)‖P_mb−R_mb‖²+b*Db+E(b); SF kernel of S_sq; Q=L+M on SF; 0 ≤ B ≤ L (L1534–1583).
22. SF density in B_a² (contains all P_k and the compactly supported ones) (L1619–1635).
23. Representations A=∫_0^∞J_u du, A=∫_0^1C_u du, C_u(x,x)>0 (L1680–1722).
24. **C_0 PSD at all orders** (contraction S(a)=Z(a−1)/Z(a+1)) (L1725–1775).
25. Generic countermodel B_1 PSD with B_0 not PSD (L1808–1856) — positive only as a model.
26. Duplication identity Q(P)=(π²/2)[4E_4(P')−6E_2(P)−6∫t^{3/2}|P|²] (L2027).
27. Bound A(x,x) ≤ (x/sinh 2x)C_0(x,x), x>0 (L2073).
28. Exact theta operator realization and its integral extension (L2144–2147).
29. Identities C_u=∫e^{−uv}D_v dv, A=∫[(1−e^{−v})/v]D_v dv; G_V, F_R (L2169–2260).
30. Uniform domination G-DOM and A[G_N]→A[Phi] locally uniformly (L2330–2342).
31. H(z)=z−2+(z+2)e^{−z} without zeros on Re z>0; G_2 holomorphic in |Im|<π/4 (L2392–2397).

---

## C. Explicitly open obligations (precise statements)

C1. (Mixed factorization, L17) There exist a Hilbert space ℋ and a map V with a_T(F)=‖VF‖²+(manifestly
    ≥0 remainder) that jointly factorizes the archimedean measure and ALL contacts m=kn, m≈kn, with control uniform
    in T of the terms and of Tate. Attempted: multipliers + Bochner (dual class), pure SOS (empty T ≥ ½log3).
C2. (Joint arithmetic balance, L27) For every size M of the sufficient carrier and every vector s:
    sᵀ(Arch − Div − Near)s ≥ 0 proved by a signed inequality between Arch and the terms m≈kn that
    preserves phases and boundaries. Attempted: shifted convolution, absolute Near, reindexed Euler, commutator ZΔ.
C3. (First contact, L35) Signed bound of the endpoint or of the rest of the continuation path. Attempted: 197.
C4. (Descent, L43, L186) For each initial entry (N,k): the signed average R_L of the boundary complement
    satisfies R_L ≥ −ε_L with ε_L→0; or a family of jointly positive subspaces dense in a topology where
    W is continuous. Attempted: 036, 055, 065, 067, scalar bridge 017.
C5. (Positive representative, L51) Positive real representative with noncompact correction, identity on the whole
    carrier, control uniform in T of the interior arithmetic coincidence. Attempted: 045.
C6. (Critical resonant comparison, L69, L1509) At y=0, on all finite blocks of integer scales:
    Off ≥ −R_res (equivalently H=−R^{−1/2}OffR^{−1/2} ≤ I). Attempted: fixed margins (refuted), uniform
    norm (refuted).
C7. (Open reductions, L69–72) PSD of the complete A on all integer blocks at y=0; or PSD of all the
    Grams of E_j, j ≥ J, for a fixed J. Only E1,E2 signed.
C8. (Theta Gram by slices, L90) A joint bound compensating non-PSD slices.
C9. (Stieltjes of 083, L142) A positive measure representing N(x)=M(√x)/√x as a Stieltjes function; equivalent to
    alternating signs of all derivatives of H_A−P (L149).
C10. (Budget 022, L160) For all (N,k): an independent inequality paying ARCH_♯ (row k=0: A_N+2∫K_NC_B ≥ 0).
C11. (Hyperbolic, L174, L179) A preserving operation applicable to the real Phi, or an estimate of the whole correction
     Phi/phi_{2π} in every dimension; compensation of the source.
C12. (Geometric interpolation, L323) For each finite list U: ∂_sK_{s,U} ≥ −C_U(s)K_{s,U}, C_U ∈ L¹[0,1].
C13. (Compensated Selberg, L280) Joint comparison with ARCH and polar.
C14. Complete (N), uniform in all tests (L292); R8 with an independent positive carrier and identification of
     domains; R10.
C15. (Dense regime, L985) With u_N=N^{3/4}: inf_{f∈V_N(u_N)} W_{trunc}[f]/‖f‖² ≥ −ε_N, ε_N→0, for ARCH+POLAR and all
     contacts up to exp(40N^{1/4}).
C16. (Causal operator, L1057) Uniform bound of the unweighted inverse.
C17. (Theta branching, L1079) An inequality preserving PSD at the step B∘S of the orbit from δ_{π/3}.
C18. (Two cutoffs, L1224) Sign of the remainder R_M, uniform bound for M-dependent interpolants.
C19. (BPY package, L1269, L1877) Additive PF∞ of q + reciprocity + integrability ⟹ A PSD, or a falsifier
     satisfying the package.
C20. (SF, L1653) Q=L+M ≥ 0 on all finite squarefree coefficients (α=1); joint balance D+E with
     the squares (L1668).
C21. (Pairs, L1722, L1775) Integrated crossing inequality for C_u, 0<u ≤ 1 (or for ∫_0^1C_u du), or a falsifier
     preserving the pairing; candidate C_1 (L1927).
C22. (Hyperbolic theta descent, L1856) An additional hypothesis or identity proved for theta leading from B_1 PSD to
     B_0=A PSD.
C23. (Duplication, L2037) E_4(P') ≥ (3/2)[E_2(P)+∫_1^∞t^{3/2}|P|²dt] for smooth compactly supported P with P(1)=0.
C24. (Laplace, L2238, L2262) PSD of A after integrating v (compensation); PSD of G_V for all V (neither proved nor refuted).
C25. (Approximants, L2342, L2611) PSD of A[G_N] for all N (or an infinite subsequence), even A[G_2] at all
     sizes; |B_12|² ≤ B_11B_22 of the complete crossed minor.
C26. (Triples, L63) Extension of small triples to all R; monotonicity of the normalized quotient; Schur preservation.
C27. (Grouping, L67) Relative inequality for crossings in the kernel −B''.
C28. (Metric, L2150) Compatible metric / nonlocal or unbounded positive Green for the realization §12.6.
C29. (RES-SOS vs 106_38, L921) Joint compensation of the remainders.
C30. (Windows, L1213) Uniform structural estimate of the complete Schur block.

---

## D. «Inputs that would change the obligation» named in the source

- L17: explicit joint factorization (Arch + all contacts, uniform control and Tate).
- L27: joint signed inequality Arch–m≈kn, uniform, with phases and boundaries.
- L35: signed bound of the endpoint or of the rest of the path, or an independent obstruction to the crossing.
- L43 («Sufficient input»): uniform R_L ≥ −ε_L; or a family of jointly positive subspaces in a topology where W
  is continuous.
- L51: noncompact positive representative with global identity and control of the interior coincidence uniform in T.
- L79: «a concrete additional signed estimate».
- L83: one of the four: mixed factorization, joint arithmetic balance, uniform one-sided bound of a remainder,
  complete positive representative.
- L101: positive factorization pairing the small-divisor defect and the second-order boundary.
- L121: repair with a proved independent cost.
- L164: inequality paying ARCH_sharp with justified scope in k.
- L176: preserving operation for the real Phi or estimate of the whole correction.
- L292: a new hypothesis resolving the identified failure.
- L323: integrable relative bound ∂_sK ≥ −C_U(s)K (Grönwall).
- L543: additional inequality for the complete datum excluding the HCM countermodel.
- L1079: joint estimate for the step or justified falsifying test.
- L1213: uniform structural estimate of the complete Schur block.
- L1269: joint identity preserving reciprocity and signing the logarithmic crossings.
- L1722: integrated crossing inequality for C_u.
- L1775: control of the interior pairs or of their integral.
- L1856: additional hypothesis or identity for theta.
- L2289: additional claim controlling the obstacle and connecting with the complete form.
- L2310/L2342: new structural hypothesis; PSD of A[G_N] for all N.
- L2352: explicit joint inequality or concrete falsifier.
- L2368: boundary operator or cutting identity giving the complete A with positive measure.
- L2533: explicit mechanism (k, intertwining) controlling crossings, weight 2r+x+y and boundaries.
- L2535: joint control of all singularities.
- L2611: control of |B_12|² versus B_11B_22.

---

## E. Contradictions or weakenings with respect to `RULES_AVOID.md` and `OBJECT_SPEC.md`

E1. **RULES_AVOID D3** says: «Inferring density or sign from a positive union — only with liminf r(n)²/n = 0 and a
    block repairing the moment (211/GLOBAL §4).» The source: liminf r(n)²/n=0 is the L² density condition of the
    union at fixed rate (L41); and L108: «This repairs the zero-moment objection and shows that the independent
    obligation on the crossings still remains». The condition of D3 is insufficient: signed control of the crossings is missing
    (and continuity of the complete form: «L² density alone does not give continuity», L41).
E2. **RULES_AVOID D4** («only with a signed arithmetic bound of the remainder R_L ≥ −ε_L») omits the alternative of L43
    («or a family of jointly positive subspaces approximating in a topology where W is continuous») and the
    precision of L186 (the AVERAGE per initial entry suffices).
E3. **RULES_AVOID B4** sets as a stopping pattern «Mixtures, convolutions, congruences, transports,
    interpolations and comparisons K ≥ εK₀ from a PSD model». The source limits each closure to its class: L323
    leaves open the interpolation with relative bound; L2527 «non-diagonal transfers are not excluded»; L2533 the
    triangular transfer is «NOT» excluded; L1037 «not all models or compensations are excluded». B4 is
    stronger than the source.
E4. **RULES_AVOID §C** includes «defect/continuation» and «closures by cosh products, Laplace slice D_{2π}» as
    closed families. The source: 197 is a «PROVED reduction, not a universal NO-GO» (L35); cosh products only «fixed base
    2π / exp(−a_n cosh 2t)… not other bases/factors» (L2275–2278); D_{2π} refutes only the premise of all slices,
    «Compensation after integrating v remains possible» (L2238).
E5. **OBJECT_SPEC §3 (L-comp)** concludes «ℋ_T cannot come from an exterior model». The source closes K_Phi ≥ εK_{2π}
    via U_Phi v_1 ≠ 0 (not via a boundary measure) and declares «not all models are excluded» (L1037), «not
    other scales, reweightings or signed compensations» (L493). L-comp is not proved in the source.
E6. **OBJECT_SPEC §1** (admitted variants of (G)) does not list PROVED reductions of the source: PSD of A on integer
    blocks y=0 (L69), tails E_j, j ≥ J (L72), PSD of A[G_N] for infinitely many N (L2342), and the external window log(11)/2
    (L1213) as the current verified frontier. Not a contradiction, but an omission.
E7. **RULES_AVOID D9** agrees, but omits the refutation of the uniform upper bound (L1507: «there is no uniform
    UPPER bound either») and the discard §17.7 of dilations (L69).
E8. **RULES_AVOID D11** cites «Jensen / operator concavity» as do-not-relaunch; the source (L2286) says
    «None authorizes excluding every logarithmic comparison»; reopening requires a pair of operators and domains with
    a sufficient inequality. Compatible if read with that condition, which D11 does not state.
E9. **RULES_AVOID B2** («every bound with remainder loses more») is compatible with L35 (simple exponential margin), but the
    source also uses bounds with remainder that are useful when they cancel exactly (e.g. tail control
    |W−W_{≤Q}|<e^{−N}‖f‖², L985). Not a contradiction.

---

## F. Coverage

Last line read: 2611 (end of file). Ranges read consecutively: 1–124, 125–249, 250–349, 350–499,
500–649, 650–799, 800–949, 950–1069, 1070–1219, 1220–1368, 1369–1492, 1493–1617, 1618–1737, 1738–1861,
1862–1985, 1986–2109, 2110–2253, 2254–2378, 2379–2498, 2499–2611. No range left unread.
