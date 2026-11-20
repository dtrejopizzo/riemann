# Annex 211 — Translation Gram kernel, hyperbolic model and audit

Complete line-by-line reading of three files of `../phase-211-sign-sandbox/`:

- `POWER_GRAM_SLICES_OBSTRUCTION.md` (cited «GS», 2921 lines);
- `POWER_HYPERBOLIC_MODEL_GRAM.md` (cited «HY», 966 lines);
- `POWER_GRAM_SLICES_AUDIT.md` (cited «AU», 16 lines).

Auxiliary notation from `POWER_CONE_001.md` and `POWER_BRIDGE_002.md` (cited CONE001, BRIDGE002). The
numbers «l.» are lines of the file read. Labels are copied as they appear. The problem is
treated only as the sign of the explicit form a_T on the primitive subspace (target
λ_A(T) ≥ 0 for all T); the equivalences that appear are exact internal reductions between
formulations of that same sign.

---

## 0. Dictionary of objects (defining formulas, once)

**Theta density.** h(x)=π e^{5x/2}(2π e^{2x}−3) exp(−π e^{2x}); Φ_n(t)=n^{−1/2}h(t+log n);
Φ=Σ_{n≥1}Φ_n (even, positive, holomorphic in |Im t|<π/4; supertails). Modal equivalent:
Φ((log(kt))/2+iy)=Σ_n n^{−1/2}h_{kn²}(t) with h_λ(t)=π(λt)^{5/4}(2π a_y λt−3)e^{5iy/2}e^{−π a_y λ t},
a_y=e^{2iy}. Radial form: Φ(z)=w^{5/4}[wθ''(w)+(3/2)θ'(w)], w=e^{2z}. Tail: Φ(t)~2π²e^{9t/2}exp(−πe^{2t}) (HY l.120).

**Transforms.** Z(u)=∫_R e^{ut}φ(t)dt; M=Z'/Z; K_M(u,v)=[M(u)+M(v)]/(u+v) (power kernel;
CONE001 §1: Q_Φ=W on exponentials). G(u,v)=1/(u+v) (Cauchy Gram, GS §8.11).

**Temporal kernel A (GS (A), l.26).** A(t,s)=∫_0^∞ (t+s+2r)φ(t+r)φ(s+r)dr. With τ=(t+s)/2, δ=(t−s)/2,
P_δ(σ)=φ(σ+δ)φ(σ−δ): A=∫_{|τ|}^∞ 2σP_δ(σ)dσ>0. Identity (LT): (u+v)∫∫e^{ut+vs}A=Z'(u)Z(v)+Z(u)Z'(v),
whence K_M(u,v)=∫∫e^{ut+vs}A/[Z(u)Z(v)].

**Slices (SLICE, l.123).** A=∫_0^∞ S_v dv, S_v(t,s)=φ(√(τ²+v)+δ)φ(√(τ²+v)−δ).
Normalized B_v=S_v/(φ(t)φ(s)); ∂_vB_v|_0=−K_f, K_f(t,s)=(f(t)+f(s))/(t+s), f=V'.

**Potential.** V=−log φ (or −log Φ); p=V'=−Φ'/Φ; G(u)=V(√u) (GS §9, §12); a(u)=2G'(u)=p(r)/r, u=r²;
q=1/a. Moments H=∫_0^∞ rΦ², J=∫r(Φ')², K=∫r(Φ'')² (GS §12; this H is not the one of the hyperbolic model).

**Reference models (GS §4.3).** G0(t,s)=(t+s)/(e^{2t}+e^{2s}); H0(t,s)=sech²(t−s)−1/(t+s)²;
H(t,s)=∂_t∂_s log A.

**Complex integer scales (GS §16–17).** z_k=(log k)/2+iy, ε=cos 2y, σ=sin 2y,
A_y(k,l)=A(z_k, z̄_l)=∫_1^∞ w_kl(t)Φ_k(t)conj(Φ_l(t))dt, w_kl=[log t+(log k+log l)/2]/(2t).
ρ(k,l)=gcd(a,b)/√(ab) if k=da², l=db² (d squarefree), 0 otherwise.
H(u)=|h_u(1)|²=π²u^{5/2}|2πa_yu−3|²e^{−2πεu}; I_λ=λ^{−1/2}∫_λ^∞H(u)/(2u)du;
J_λ=λ^{−1/2}∫_λ^∞log(u/λ)H(u)/(2u)du.
**R_res,y** = contribution of ALL modal pairs with kn²=lm² (complete integral t≥1, both
terms of the modal polynomial). **Off_y = A_y − R_res,y** (pairs kn²≠lm²).
By squarefree group d, coefficients c_a (k=da²): f_q=Σ_{a|q}√a c_a, g_q=Σ_{a|q}√a log a c_a,
I_q=I_{dq²}, J_q=J_{dq²}, D_q=J_q+[log d+log q]I_q−Σ_{m≥2}Λ(m)I_{qm}.
E_y[c]=Σ_d √d Σ_q I_{dq²}|f_{d,q}|² (divisorial energy).

**Thermal graph (GS §18).** P_κ(t)=κ^{5/4}Σ_n n²e^{−πκn²t}; Θ_κ(t)=Φ(½log(κt)); p=P_1;
T=πt^{5/4}(−2tD−3); Lg P(t)=∫_0^∞[e^{−πr}P(t)−P(t+r)]dr/r; (CF)(t)=Σ_{m≥2}Λ(m)m^{−1/2}F(m²t);
F(P)=TP, G(P)=½T Lg P−C TP; F(P_κ)=Θ_κ, G(P_κ)=½log κ Θ_κ (GRAPH).
Σc_i c̄_jA(x_i,x_j)=∫_1^∞[log t|F|²+2Re(G F̄)]dt/(2t) (A-GRAPH). Norms ‖P‖_{a,2}=max_{j≤2}sup e^{at}|P^{(j)}|,
H_γ=L²([1,∞),e^{γt}dt/t). B=Lg−2Σ_{m≥2}Λ(m)m²D_{m²} (Bp=0). T^{−1}F(t)=(1/2π)t^{−3/2}∫_t^∞u^{−3/4}F(u)du.

**Complete form Q and Q_B (GS §19.1).** Q(P)=∫_1^∞[log t|TP|²+Re(TBP·conj(TP))]dt/(2t)=Q_log(P)+Q_B(P).
Tate moments ⇔ P(1)=0 and ∫_1^∞P=0 (GS §18.9).

**Thermal core E_j (GS §19.8).** w(t)=(t−1)p(t); q_j monic orthogonal polynomials of w (q_0=1);
E_j=p(t)(t−1)q_j(t), j≥1; Γ_ij=Q(E_i,E_j). E_1=p(t)(t−1)(t−a), a=1+(2/π)S_4/S_2, S_j=Σn^{−j}e^{−πn²}.

**First-mode reference (GS §19.11).** p_0=e^{−πt}; Q_0(R)=∫[log t|T(p_0R)|²+Re(T Lg(p_0R)conj(T(p_0R)))]dt/(2t).

**Causal adjoint (GS §19.12).** k(h)=2cosh(h/2)−e^{−h/2}/(1−e^{−2h})−Σ_{n≥2}Λ(n)n^{−1/2}δ_{log n}(h);
g(r)=−∫_0^∞k(r+s)Φ(s)ds; V(f)=∫_0^∞Φ(r)g(r)|f(e^{2r})|²dr.

**Hyperbolic model (HY).** φ_a(t)=exp(−a cosh 2t), Z_a, M_a=Z_a'/Z_a;
y_x(r)=∫_0^∞exp(−a e^r cosh v)cosh(√x v)dv, Z_a(u)=y_{u²/4}(0), y_x''=[a²e^{2r}+x]y_x;
**H=−D_r²+a²e^{2r}** on the half-line, Dirichlet at 0; Green G_x(r,s)=y_x(r)y_x(s)∫_0^{min(r,s)}y_x^{−2};
REP: M_a(u)/u=½Tr(H+u²/4)^{−1}. Robin: φ_{a,β}=[β+a cosh 2t]e^{−a cosh 2t}, boundary f'(0)=βf(0).
Prefactor: Y_ν(b)=∫_0^∞e^{−b cosh v}q(v)cosh(νv)dv, b=ae^r; q_θ(v)=Φ(v/2)e^{2π cosh v} (Y_{u/2}(2π)=Z(u)).

**Theta realization (HY §12.6).** ℋ=L²((0,∞),sech(πω/2)dω)⊕R³; λ_j=j+¼ (j=0,1,2);
Q(v)=(cos(ωv),cosh λ_0v,cosh λ_1v,cosh λ_2v); F(t)=sech t+Σcosh λ_jt;
C=mult. by −ω² (continuum), λ_j² (masses); D=mult. by d(ω)=1+ω coth(πω/2)+(15/2)cosh(πω/2)/cosh(2πω)
and masses (−29/4,−23/4,−9/4); B Q(v)=sinh v Q'(v)+cosh v DQ(v) on S=span{Q(v)}; h=(k/ρ,2d_{λ_j}) with
⟨Q(v),h⟩=q_θ(v); Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).

---

## 1. Entries of `POWER_GRAM_SLICES_OBSTRUCTION.md` (GS), in order

**GS l.1–5 — Title, Status, additional audit.** Status: «PROVED as an identity and obstruction of
a class of certificates». It does not decide the sign of the complete A nor of W. The additional audit (l.5)
corrects the scope: the tail discards hold for Φ_M with every M≥1 and for Q_M only with M large.

**GS §1 (l.7) Query and object that changes.** Target: a single two-variable kernel whose
positive representation would pay for all sizes. It claims no novelty for the Gram/Pólya framework.
**l.15 Public antecedent.** An external draft already contains the same normalized kernel
(j=A/Z0²) and its logarithmic response M; it leaves the positivity of the form open. Consequence: **do not
attribute novelty to A nor to the LT bridge**. Reusable: yes, as a scope citation.

**GS §2 (l.17) Exact kernel and transform.** Object: A, DOM 0<A≤[C²/(2N)]e^{−N(t²+s²)} if
φ≤Ce^{−Nt²}; (∂_t+∂_s)A=−(t+s)φ(t)φ(s); (LT). Result: identities PROVED. If A were PSD, K_M
would be PSD on all blocks («precise sufficiency, NOT a proof of PSD of the real A»). Reusable: yes.

**GS §2.1 (l.65) Converse under DOM.** PROVED. A PSD on R ⇔ K_M PSD on all finite blocks of
nodes in any open interval I⊂(0,∞). It does not hold at fixed size nor for discrete ladders. For
the hyperbolic model it gives PSD of its A. Reusable: yes (exact reduction).

**GS §2.2 (l.80) For real Φ, local temporal positivity implies global.** PROVED. A is holomorphic in
|Im t|,|Im s|<π/4; PSD (all sizes) on an open interval propagates by jets/Taylor to all of R.
It gives no factorization nor sign. Reusable: yes (continuation principle, used in §§4.3, 8, 8.11, 19.10).

**GS §2.3 (l.100) Restriction of the translational Hankel factorization.** PROVED as a restriction
(classical antecedent cited). There is no A(t,s)=∫_0^∞⟨h(t+r),h(s+r)⟩dr on t,s>0: it would force
(t+s)φ(t)φ(s) PSD, whose 2×2 determinant is −(t−s)²φ(t)²φ(s)²<0. It does not exclude PSD of A, general Grams,
other coordinates nor sums of two Hankel products. Reusable: only as a discard.

**GS §3 (l.119) Slices and sufficient certificate.** Object: SLICE. PROVED: if S_v is PSD for all v≥0,
A is PSD. Defines the «class of certificates by positive slices». Reusable: as a sufficient criterion.

**GS §4 (l.131) Integrable model.** φ=exp(−at⁴−bt²): S_v=φ(t)φ(s)e^{−2av²−2bv−4av(t²+s²)}e^{4avts};
all slices PSD and A PSD. Not extrapolated to theta. Reusable: positive model.

**GS §4.1 (l.144) Conditionally positive logarithm.** PROVED for the model, not for Φ. CPD of
log A (sums c with Σc=0) is sufficient for A PSD; it fails for the quartic model b=0 (κ_5(V)<0,
coefficient [t⁵s⁵]log A<0, six nodes jh). Real diagnostics: NUMERICAL, not certified (positive
eigenvalues on {0,¼,½,1,2}; [t⁵s⁵]log A≈+1.904 for Φ). Identity: ∂_t∂_s log A=Cov_μ(p(t+r),p(s+r))−
Cov_μ(1/q,·)−(E_μ[1/q])², not Gram. Decision: real condition OPEN.
- **l.184 Complex diagonal cusps (PROVED).** F²H(z,z̄)=4D+L²+2xbL−Fb, D complex projection;
  eventually positive at the alternating cusp x=0 (L≥cε^{−4}, F≤Cε^{−5}) and at the even one x=h=log2/2
  (m(f)≥1/9375 for f=(1+2iu)^{−5/2}). Only these two tests; CPD and sign OPEN.
- **l.227 Limit of the joint projection (PROVED).** There is no c>0 independent of η with R≥cB
  (projection residual against boundary) on pairs z0, z0+iτ. Moreover S=A^{⊙2}⊙H PSD does not imply H PSD.
  Falsifier: evaluation on the first coordinate vector.
- **l.235 Horizontal average (PROVED).** ε^{9/2}B_y→c_*=315(log2)²/(512√2), A(iy,−iy)≥cε^{−9/2};
  crossings n≠m bounded by integration by parts without discarding near-resonances; an isolated cusp
  contributes O(√ε) relatively. Only B_y, not the complete A (completed by §16).

**GS §4.2 (l.285) A is not log-supermodular.** PROVED. H(t,s)=−1/(t+s)²+O_K(e^{−2t})<0 for large t:
A is not TP2 on the half-line. Falsifier: rectangular minors. It does NOT discard a signed Gram, PSD of H,
CPD nor PSD of A.

**GS §4.3 (l.331) The tail model is not a PSD reference.** PROVED. G0 and H0 are not PSD on any
open interval of (0,∞) (G0(t,t)<0 for t<0 after continuation; H0(¼,¼)=−3). A=[Φ(t)Φ(s)/2π]G0(1+O(e^{−2L})),
H=H0+O(e^{−2L}) in tails. Sandwich (1−ε)H0≤H≤(1+ε)H0 impossible. It does not exclude other positive references
nor exact signed compensation.

**GS §5 (l.363) Infinitesimal condition and real failure.** PROVED. PSD slices ⇒ K_f CND (JET); with nodes
(α,β,R), c=(1,−1−ε,ε), ε=−B/Q_bR, the form equals Q_ab+B²/(−Q_bR)~(β−α)²f(R)/R³>0 if f(R)/R³→∞.
Real Φ: f(R)=2πe^{2R}+O(1). Falsifier: finite slice S_v not PSD at three positive nodes (d_i=c_i/Φ(t_i)).

**GS §6 (l.423) Scope.** Only the slices are refuted; not A, nor K_M, nor W. It does not exclude cancellation between
slices, signed reordering nor another Gram. A(t,t)=∫_t^∞2uφ²; A(t,−t)=∫_0^∞2rφ(r+t)φ(r−t)dr.

**GS §7 (l.440) Generic hypotheses and positive operations.** PROVED. (i) V=g(t²) convex (074) gives A
not PSD. (ii) Positive mixtures of Gaussians: uM'>M, minor u,u+h negative. (iii) Convolution preserves K
(M=M1+M2), but Φ is not a convolution/positive mixture with factor exp(−at⁴−bt²). (iv) Integration by parts
with B(t,s)=(t+s)/(f(t)+f(s)) has a negative diagonal correction. (v) A positive operator Bop with
Bop(−Φ')=tΦ does not control the form on the half-line. Real PSD OPEN.

**GS §7.1 (l.455) Gaussian convolution: converse.** PROVED. Rank-one lemma: if K(u,R)→0, K(R,R)→0,
then K+b PSD ⇔ K PSD. For Φ, M(u)/u→0; K_σ=K+σ² (M_σ=M+σ²u). Signing ONE smoothed density
G_σ∗Φ would close the sign; smoothing cannot turn indefinite into PSD. Obligation OPEN.

**GS §8 (l.485) No individual theta mode gives a local Gram.** PROVED. A_n(t,t)→(2H/n)(m−log n)<0,
m<½log(5/(4π)); by §2.2 A_n is not PSD on any interval. It does not refute A: crossings n≠m are missing.

**GS §8.1 (l.528) Complete theta prefix Φ_M.** PROVED (M large): ∫tΦ_M²~−H M log M; limiting diagonal
negative. **l.572 Strengthening: every M≥1** via Z_{Φ_M}(u)=(u−½)H_M(u): test ZZ'/u<0.

**GS §8.2 (l.591) Continuous tail Q_M=Φ_M+πM³e^{5t/2}e^{−πM²e^{2t}}.** PROVED: Q_M→Φ in L²((1+|t|)dt),
but ∫tQ_M²=−[‖h‖²/(4M)]log M+O(·)<0: not PSD (M large).

**GS §8.3 (l.636) Symmetrize S_M=[Q_M(t)+Q_M(−t)]/2.** PROVED every M≥1: tails −D_Me^{−5|t|/2},
Z_M→−∞ at 5/2, point with Z>0, Z'<0.
- **l.677 Common scope: repairing only the left.** If ψ=f on [R,∞), A_ψ=A_f on t,s≥R; the negative
  minor persists. It does not exclude corrections of the right tail.
- **l.680 Smooth cutoffs w_n≥0, Σw_n n²<∞.** PROVED: Z=(u−½)H_w, not PSD. Does not cover w_n=1.

**GS §8.4 (l.693) Cancelled exponential moment.** PROVED. Lemma: if Z(c)=0 for some c>0 (CANCEL),
A_φ is not PSD (and not PSD on any interval if holomorphic). Applies to φ_P=(D²−¼)[e^{t/2}P(q)]/4,
q=e^{−πe^{2t}} (∫e^{t/2}φ_P=0), and to the cutoffs P_J of the Jacobi product. Does not pass to the infinite product
(Z_Φ(½)>0).

**GS §8.5 (l.743) Symmetrizing Jacobi cutoffs.** PROVED J≥1: tail D_Je^{−β|t|}, β=2J+½; ε²det→−1/(16β²)<0.

**GS §8.6 (l.773) Weights n^{−δ}.** PROVED δ≠0 real: Z_δ Z_δ'/u<0; ∫e^{t/2}|φ_δ−Φ|≥¼. δ=0 excluded.

**GS §8.7 (l.815) Even analytic positive perturbations.** PROVED: ∀ε, ψ>0 even holomorphic with
sup|ψ/Φ−1|<ε, ψ/Φ→1, A_ψ not PSD on any interval. Construction ψ=Φ(1−g_σ), g_σ=h_M∗γ_σ.

**GS §8.8 (l.862) Preserving finite moments.** PROVED: moreover ∫w_iψ=∫w_iΦ exactly (finite family
fixed beforehand); in particular equality of K(u_i,u_j) on preselected finite blocks. Falsifier:
the same ψ.

**GS §8.9 (l.901) Stability of blocks of order ≤4.** PROVED: ∃δ_*: ‖h‖_20<δ_* ⇒ K_ψ PD on all
blocks of ≤4 nodes u_i>½ (uses certificates 084/085: N_R>¼, N_S>19/4). There is such ψ with A_ψ not PSD:
the negative block has >4 nodes.

**GS §8.10 (l.967) Uniform relative control and thirteen poles.** PROVED. Contractive
interpolation lemma: |Σc_ic̄_j[μ(u_i)+μ(u_j)]/(u_i+u_j)|≤2B_nΣc_ic̄_j/(u_i+u_j), B_n=Σ_{j<n}(2^j/j!)‖F^{(j)}‖_∞,
F(z)=μ(a(1+z)/(1−z)). With 053 (W>‖f‖²/4000 at thirteen poles ≥63/2): Q_ψ>‖f‖²/8000. There is ψ with all that
and K not PSD (block with >13 nodes). Reusable: the lemma, at fixed dimension.

**GS §8.11 (l.1038) No uniform Cauchy margin.** PROVED: M real analytic, M=O(u) at 0, c>0:
K_M−cG is not PSD on any interval I⊂(0,∞). Holds for K_Φ and the hyperbolic model. If K_Φ were PSD,
inf Q_Φ[f]/‖f‖²=0. A−a is not accretive (translation of the half-plane is not free). Reusable: restriction.

**GS §9 (l.1064) Temporal pairs.** PROVED: V'''>0 (073) ⇒ G(u)=V(√u) strictly convex ⇒
S_v(t,s)²<S_v(t,t)S_v(s,s) (PAIR-SLICE) ⇒ [A(t_i,t_j)]_{2×2} PD for t_1≠t_2. Minimal size of a
slice falsifier: 3. All orders OPEN.

**GS §10 (l.1106) Symmetric triples (−R,0,R).** PROVED: SPD for all R≥8 (2c²<d_0 d; d−b>0); slices
initially negative at the same nodes (Q_R=2p'(R)−6p(R)/R+4p'(0)>0, w_R=(1/P,−2/Φ(0),1/P));
∫w_R^TS_vw_R dv>0: compensation proved for that family. Not uniform.

**GS §11 (l.1194) Andréief.** PROVED: det[A_ij]=(1/6)∫S; S(r,r,r+h)=−4det[g,f,f_h]det[g,f,g_h]<0 on an
open set. It only refutes pointwise positivity of the integrand; not det A<0.

**GS §12 (l.1227) Reciprocal of the potential.** PROVED (identity, sufficiency, exterior bound).
(HK−J²)/H²=Var(a+ua')+E[u²(2a'²−aa'')]; if a>0 and (1/a)''≥0 then HK≥J². Tail: N=2r²p'²−r²pp''−rpp'−p²>2r²Y²
for r≥1, q''(u)>0 on u≥1.

**GS §12.1 (l.1265) Compact closure.** PROVED by an Arb ball certificate (script and SHA256 at l.1267):
a(u)>0 and q''(u)>0 for all u≥0; HK>J².

**GS §12.2 (l.1310) Small triples.** PROVED: D(R)=d_0(d+b)−2c²=2(HK−J²)R⁴+O(R⁶)>0: SPD for 0<R<R0
(R0 not quantified). Intermediate R OPEN.

**GS §12.3 (l.1324) Scope versus 074 and slices.** Consequences: the falsifier 074 violates q''>0;
V=r²/2+r⁴/4+εr⁶/6 satisfies q''>0 but its slices fail (§5). Intermediate R and all orders OPEN.

**GS §13 (l.1340) Reciprocal convexity is not enough.** PROVED (generic class): positive even ψ, close to
Φ in relative C6, with V'''>0, a>0, (1/a)''>0, HK>J², and A_ψ not PSD.

**GS §14 (l.1390) No positive Laplace representation of q.** PROVED: q has no holomorphic extension to
Re u>0 (cusps τ_m=16+2/m, Gauss sums |G_m|²=m, Q(z_m²)=0 accumulating). Coefficients 0–39
alternating positive: test not used.

**GS §15 (l.1436) Convex G is not enough for triples.** PROVED: φ=exp(−r²/2−εr⁶/6), ε=1/1000:
HK−J²<0 ⇒ triple (−R,0,R) indefinite for small R.

**GS §16 (l.1467), §16.1 (l.1471) Equivalent on integer scales.** PROVED:
A(z_k,z̄_l)=[105/(512√2)]ρ(k,l)ε^{−9/2}L²+O_{k,l}(ε^{−9/2}L), L=log(1/ε); exact representation (MAIN).
**§16.2 (l.1503)** NEAR: Σ'n⁴m⁴e^{−δ(kn²+lm²)}/|kn²−lm²|≤C_{k,l}δ^{−4}log(2+1/δ); (OFF) ≤Cε^{−4}log(2+1/ε),
near-resonances preserved. **§16.3 (l.1529)** resonances n=(b/g)j, m=(a/g)j; constant 4π⁴F0=105/(128√2).
**§16.4 (l.1555)** corollary: [ρ(k_i,k_j)] PD (gcd=Σφ(q)); complex block [A(z_{k_i},z̄_{k_j})] PD for
small ε depending on the list. Not real A PSD.
**§16.5 (l.1570)** PROVED: with y fixed, |C_y(k,k+1)|→1 while ρ(k,k+1)=0: there is no c_y>0 with C_y≥c_yρ;
sup|C_y−ρ|≥1. Falsifier: consecutive pairs.

**GS §17 (l.1605) Exact SOS of the resonant part.** PROVED. Objects: R_res, I_λ, J_λ, H(u). Bibliographic
antecedents (von Mangoldt chains, criticality on graphs) cited without names here; they add no sign.
**§17.1 (l.1624)** one frequency (k=1,4, λ=4): det=−2(log2)²I_4²<0 (per frequency only).
**§17.2 (l.1634)** g_q=log q f_q−Σ_{m|q,m≥2}Λ(m)f_{q/m};
(RES-SOS) R_res[c]/√d=Σ_qD_q|f_q|²+Σ_qΣ_{m|q,m≥2}Λ(m)I_q|f_q−f_{q/m}|².
**§17.3 (l.1662)** D_q>0 ∀d,q (log(N!)≥(X/2)Σ_{m≤X}Λ(m)/m).
**§17.4 (l.1683)** R_res positive definite on any finite set of distinct integers, every
|y|<π/4 incl. 0. Joint control of the nonresonant contribution is missing.
**§17.5 (l.1693)** (UNIF-D) D_q≥c_*I_q, c_*=(log2/3)(4π−3)²e^{−6π}/[(4π+3)²+(4π−3)²e^{−6π}];
(DIV-LOWER) R_res[c]≥c_*E_y[c].
**§17.6 (l.1731)** PROVED: falsifier c^{(k)} on (k,k+1): E_y=1, Off_y=−log k+o(1), R_res=log k+o(1),
A_y=o(1). Excludes Off_y≥−C_yE_y and A_y≥δ_yR_res,y. Does not decide Off_y≥−R_res,y.
**§17.7 (l.1776)** PROVED: there is no M with |Q_C(F)|≤M W(F), W=∫(1+log t)|F|²dt/(2t), on the finite span of
Θ_k (y=0); span dense in H_γ (0<γ<2π); plateaus F_R=1_[1,R].
**§17.8 (l.1829)** PROVED: R̃_s=TR_sT^{−1} not all accretive in the physical product dt/(2t)
(q=(π²/2)[7∫|u'|²−(9/16)∫|u|²]<0), transferred to the theta span. Does not falsify the conjugate logarithm.

**GS §18 (l.1878) Integer A ⇔ real A.** PROVED. **§18.1 (l.1889)** GRAPH, A-GRAPH. **§18.2 (l.1915)**
continuity B_a²→H_γ×H_γ. **§18.3 (l.1933)** approximation by integer scales, MOB-P
e^{−πkt}=k^{−5/4}Σμ(n)n^{−1/2}P_{kn²}. **§18.4 (l.1953)** transfer; the complete integer sign remains OPEN.
**§18.5 (l.1960)** PROVED: K(t,v)=t^{−1/4}v^{−3/4}−t^{5/4}v^{−5/4}/(v−t) (JUMP-K), positive for 2<v/t<3;
TBT^{−1} admits no positive rates JF=∫[F(t)−F(v)]ν_t(dv)+VF.
**§18.6 (l.2010)** PROVED: (PDE-A); ΔA_ii(x,0)=4[I−Φ(x)²]>0: no superharmonicity.
**§18.7 (l.2037)** PROVED: any tail k≥K suffices; (TAIL-ZERO); (NO-FIN-MARGIN): there is no
A_0[c]≥δ|ℓ(c)|² with ℓ finitely supported; nor a minorant Σw_k|c_k|² (w≥0 not all zero); nor a unique global
SOS with ℓ_α of finite support. It does not exclude continuous global observables nor non-diagonal SOS.
**§18.8 (l.2073)** PROVED: there is no A_0[c]≥δ|ℓ_σ(c)|², ℓ_σ a real exponential moment (A(−R,−R)/|ℓ_σ|²→0).
**§18.9 (l.2105)** PROVED as scope: (1) λ_A(T)≥0 ∀T; (2) K_{M_Φ} PSD; (3) real A PSD; (4) integer A PSD
(or any tail) — equivalent. ℓ_σ(TP)=πP(1)+π(σ/2−¼)∫t^{σ/2+1/4}P. TAIL-ZERO holds primitively.

**GS §19 (l.2151) First thermal polynomial.** **§19.1 (l.2157)** E_1, a=1+(2/π)S_4/S_2, P(1)=∫P=0.
**§19.2 (l.2188)** BP=Σe^{−πn²t}L_n(t), (POLY-QB). **§19.3 (l.2229)** Q_{B,11}(a_0)>1/1200.
**§19.4 (l.2261)** |δ|<1/40000. **§19.5 (l.2292)** |Q_{B,12}+Q_{B,21}|<1/4500.
**§19.6 (l.2351)** remainder <1/30000. **§19.7 (l.2390)** PROVED: Q_B(E_1)>1/2000, Q(E_1)>1/2000.
**§19.8 (l.2406)** PROVED (density/scope): span{E_j} is a core; Γ_{1..N} PSD ∀N ⇔ λ_A(T)≥0 ∀T.
**§19.9 (l.2462)** PROVED by a rational/Arb certificate (SHA256 l.2468): Q_11>179/100000, Q_22>17/10000,
|Q_12|<79/50000, det>2733/5·10⁹: 2×2 block PD; Q_B(E_1+E_2)<−1/20000 (falsifier of the separate sign of Q_B).
**§19.10 (l.2653)** PROVED scope: Γ_{J..N} PSD ∀N≥J ⇔ target; (TAIL-MOM), (TAIL-SIGMA), lemma CPD-m.
**§19.11 (l.2725)** PROVED: ∃R, R(1)=0, ∫pR=0, Q_0(R)<0 (archimedean deficit 008: Arch≤−4‖f‖²+17‖f'‖²).
**§19.12 (l.2785)** PROVED: Q_phys(Θf)=−½∫ΘΘ|f(v)−f(t)|²dν+V(f) (POT-V); g(log2+)<−19/300;
V(f)<0 for bumps (also exact primitives). Not Q negative; difference term of mixed sign.

## 2. Entries of `POWER_HYPERBOLIC_MODEL_GRAM.md` (HY), in order

**HY l.1–3 Title and Status.** PROVED for the model; every transfer to Φ OPEN.
**§1 (l.5)** object φ_a; asserts K_{M_a} PSD at all sizes.
**§2 (l.17)** y_x, Z_a=y_{u²/4}(0), (ODE), (RATIO) y_x(r+h)/y_x(r)≤exp(−ae^rh).
**§3 (l.38)** z_x=∂_x log y_x; (LOG-DER) with justified boundaries.
**§4 (l.62)** H, Green G_x (continuous Gram), Tr R_x=∂_x log y_x(0)≤1/(2a); (REP).
**§5 (l.83)** PROVED: K_ij=½Tr(HR_iR_j)+(u_iu_j/8)Tr(R_iR_j); (GRAM) Σc_ic_jK_ij=½‖H^{1/2}A‖²_HS+⅛‖B‖²_HS≥0,
A=Σc_iR_i, B=Σc_iu_iR_i. All sizes. Reusable: scale Green mechanism.
**§6 (l.106)** OPEN: there is no ODE/Green with REP for real Z; mixtures do not transfer.
**§7 (l.114)** PROVED; THETA-TAIL. **§7.1 (l.124)** there is no μ≥0 with Φ=∫e^{−a cosh 2t}dμ(a).
**§7.2 (l.138)** there is no finite ν≥0 with Φ=φ_a∗ν. Does not exclude temporal prefactors, signed
combinations nor other Greens; «No general prohibition of transfers is recorded».
**§8 (l.161)** PROVED: Robin φ_{a,β}, (ROBIN) R_{β,x}=R_x+k_x⊗k_x/(m_x+β); GRAM holds with term
(β/2)∫|F(0,s)|². Transfer OPEN (prefactor e^{2t} vs e^{9t/2}).
**§9 (l.200)** PROVED: D_a=−a∂_aK_a not PSD (A_nA_{n+2}−A_{n+1}²<0). Scale flow without matrix order.
**§10 (l.249)** PROVED: fixed prefactor q, F_ν=E(b)Y_ν at two scales ⇒ q constant; q_θ excluded.
**§10.1 (l.282)** PROVED: with drift A(b): only q=C or C cosh(v/2). **l.316 Extension:** weight w(b)ν² forced
w=1; change of scale h'²=1: no repair.
**§11 (l.335), §11.1 (l.345), §11.2 (l.368), §11.3 (l.377)** PROVED: there is no Φ=Ce^{−a cosh 2t}Πcosh(α_jt)
(a=2π, Σα_j=9/2, c1=π−3/(2π)∈(2,3) not an integer).
**§11.4 (l.389)** PROVED: nor locally uniform approximation at fixed scale 2π.
**§12 (l.427)** PROVED: finite vector of prefactors without drift: sinh v Q'=BQ ⇒ Q bounded.
**§12.1 (l.458)** PROVED: with matrix drift: a rational operator would annihilate g; impossible.
**§12.2 (l.508)** PROVED: infinite symmetric dimension (INF-SYM) ⇒ ‖Q(v)‖²=A+c log cosh v.
**§12.3 (l.554)** PROVED: constant scalar drift α: (DRIFT-K), (DRIFT-HOL); even cusp excludes theta.
**§12.4 (l.605)** PROVED: scale-dependent scalar drift forced constant (β=0).
**l.650 Operator control** example Q=(1,2cosh v), D,C,B 2×2: the scalar reduction does not extend;
potential not symmetric except r=0. **l.662 Local metric for that example**: M'=−DM−MD, [E+D²,M]=0
⇒ M0=0: impossible. **l.675 Update**: GLOBAL refutes K_Φ≥εK_{2π} ∀ε>0.
**§12.5 (l.678)** PROVED: L(v,z)=⟨DQ(v),Q(z)⟩=[G(v+z)+G(v−z)]/2, G(t)=−coth(t/2)F'(t); L_vv=L_zz.
**§12.6 (l.720)** PROVED as a realization, not a sign: ℋ, Q, C, D, B, h with ⟨Q(v),h⟩=q_θ(v); B symmetric
closable, not declared self-adjoint; H_θ=O_b(e^{−|Re t|/4}). **l.800 Integral realization**: strong equation
and ⟨Y_ν(2π),h⟩=Z(2ν). Metric and positive Green missing.
**§12.7 (l.823)** PROVED (declared class): there is no bounded self-adjoint strictly positive M(r), C²,
local in r, with M'=−DM−MD (weak) and E=−C+D²+2bB̄ symmetric in ⟨M·,·⟩; contradiction on the pair e_2,e_1
(exponents 25/2, 21/2, 11/2, 8).
**§13 (l.873)** PROVED: shifted cosh products Π(cosh(b z)−c)/(1−c), −1<c<1, fixed scale 2π: integer
limits; even cusp prevents q_θ.
**§13.1 (l.927)** PROVED: variable positive scale a_n bounded by concavity; same exclusion.

## 3. Entries of `POWER_GRAM_SLICES_AUDIT.md` (AU)

**AU l.1–11.** APPROVED: checks parity, DOM, LT without factor 2, SLICE, quartic, CND, ε=−B/Q_bR,
tail 105§4. «PSD of the integral remains OPEN».
**AU l.14 Addendum on operations.** APPROVED §7; does not decide real A.

---

## A. Deduplicated «do not relaunch» list (with the reopening condition from the text)

1. Certificate by PSD slices S_v (GS §§3,5). Reopen: only with cancellation between slices or a different Gram (GS §6).
2. Translational Hankel factorization in the original variables (GS §2.3). Reopen: other coordinates or an additional transformation.
3. Inferring CPD of log A from A and PSD slices (GS §4.1). Reopen: a theta-specific estimate.
4. TP2 / log-supermodularity of A on the half-line (GS §4.2). Does not exclude a signed Gram.
5. G0/H0 as a PSD reference; sandwich (1±ε)H0 (GS §4.3). Reopen: another positive reference or exact signed compensation.
6. Positive mixtures of Gaussians; Φ as a convolution with factor exp(−at⁴−bt²); hazard integration by parts with B=(t+s)/(f+f) certifying two PSD terms; positive operator for tΦ (GS §7).
7. Smoothing to obtain PSD (GS §7.1). Reopen: independent proof of the sign of ONE smoothed density.
8. Separate modal Grams; prefixes Φ_M (every M); Q_M (M large); S_M; left-only repairs; cutoffs w_n with Σw_nn²<∞; Jacobi cutoffs and symmetrizations; weights n^{−δ}, δ≠0 (GS §§8–8.6). Reopen: corrections of the right tail, regularizations preserving the complete compensation (δ=0).
9. Relative closeness, finite moments, blocks ≤4 or 13 poles as a guarantee (GS §§8.7–8.10). Reopen: use of the exact theta structure or signed comparison in the norm of forms.
10. Uniform Cauchy margin K_M ≥ cG (GS §8.11).
11. Pointwise positivity of the Andréief integrand (GS §11).
12. Reciprocal convexity q''>0 (with V'''>0, C6) as sufficient (GS §13); convex G for triples (GS §15); positive Laplace representation of q (GS §14).
13. Comparator ρ with uniform domination (GS §16.5).
14. PSD per individual resonant frequency (GS §17.1).
15. Off_y ≥ −C_yE_y; A_y ≥ δ_yR_res,y (GS §17.6). Open: Off_y ≥ −R_res,y.
16. |Q_C| ≤ M W on the theta carrier (GS §17.7).
17. Accretivity of all T R_s T^{−1} in the physical metric (GS §17.8).
18. Positive rates after T (GS §18.5); minimum principle by superharmonicity (GS §18.6).
19. Finite-support minorants / unique SOS with finite observables, also primitive (GS §§18.7, 18.9); minorant by a real exponential moment (GS §18.8).
20. Separate sign of Q_B on the family E_j (GS §19.9); first-mode reference Q_0 PSD (GS §19.11); V(f) ≥ 0 on local bumps (GS §19.12).
21. Transfer of the hyperbolic model by positive mixture/convolution (HY §7); matrix monotonicity of the scale flow (HY §9).
22. Scale equations with fixed prefactor: scalar (HY §10), with drift (HY §10.1), variable weight ν²/change of scale (HY l.316), finite vector (HY §12), finite matrix drift (HY §12.1), infinite symmetric without drift (HY §12.2), constant or scale-dependent scalar drift (HY §§12.3–12.4). Reopen: b-dependent prefactors, genuinely operator drift, variable metrics, other representations.
23. Local metric for the 2×2 example (HY l.662) and bounded local metric for the theta realization (HY §12.7). Reopen: nonlocal metrics, unbounded ones, new connections, other realizations.
24. Cosh products: exact representation (HY §11), approximation at fixed scale (HY §11.4), shifted with fixed or variable positive scale (HY §§13–13.1). Undecided: whether a cosh factor preserves PSD.

**Cross-check with RULES_AVOID.md §D.** Present: 15 (D9), 23 partially (D15), 8 partially (D16 «discrete summation by
parts in theta») and 24 only as a label in §C («closures by cosh products»). **Missing from §D:**
1–7, 9–14, 16–22 and the part of 23 about the 2×2 example.

Inaccuracies:
- RULES_AVOID D9: «Comparisons of Off against E_y or of A against a fixed fraction of R_res as a
  consequence of the margin of the resonant sum of squares». GS §17.6 does not speak of a consequence
  of the margin: it gives an explicit falsifier, «There is no finite C_y such that Off_y>=-C_y E_y …
  Nor is there delta_y>0 with A_y>=delta_y R_res,y». Moreover D9 says «Off ≥ −R_res does remain
  open, without additional margin», but at y=0 that inequality is literally A_0 ⪰ 0 on integer
  blocks (A=R_res+Off). By GS §§18, 18.9, that is equivalent to the complete target. It is not a minor residue.
- RULES_AVOID D15: «Bounded positive local metric for the theta realization». HY §12.7 requires
  moreover that it be self-adjoint, C² and strictly positive, with «leading coefficient -I and without adding
  connections», and declares «Nonlocal metrics, unbounded metrics with other domains,
  new connections and other realizations are not excluded». D15 mentions only the nonlocal ones.
- RULES_AVOID D16 / the project rules memory: «Change (m,n) to (m+n,m−n) … POWER_GRAM_SLICES_OBSTRUCTION.md
  §§17.1–17.2». That change does not appear in GS §§17.1–17.2. They contain the one-frequency block
  (det=−2(log2)²I_4²) and the divisorial reindexing RES-SOS. The citation is not literal.

## B. Positive results PROVED (statement and exact scope)

1. GS §2: (LT) and K_M=∫∫e^{ut+vs}A/(Z(u)Z(v)); A>0 pointwise; DOM. Scope: φ even positive, Gaussian bound.
2. GS §2.1: A PSD on R ⇔ K_M PSD on all blocks of any open interval I⊂(0,∞) (all sizes).
3. GS §2.2: for real Φ, A PSD on some open interval ⇔ A PSD on R.
4. GS §3: S_v PSD ∀v ⇒ A PSD.
5. GS §4: φ=exp(−at⁴−bt²): all slices and A are PSD.
6. GS §4.1: F²H(z,z̄)>0 eventually (ε→0) at x=0 and x=log2/2; ε^{9/2}B_y→c_*.
7. GS §7: convolution preserves K. GS §7.1: K+b PSD ⇔ K PSD if K(u,R),K(R,R)→0; K_σ=K+σ² PSD ⇔ K PSD.
8. GS §8.9: ∃δ_*: ‖h‖_20<δ_* ⇒ K_ψ PD on blocks of ≤4 nodes u>½. GS §8.10: contractive interpolation
   lemma (fixed dimension n); Q_ψ>‖f‖²/8000 at thirteen poles ≥63/2 if ‖h‖_100 small.
9. GS §9: [A(t_i,t_j)]_{2×2} PD for real t_1≠t_2; S_v PD on pairs, v>0.
10. GS §10: A on (−R,0,R) SPD for all R≥8; ∫w_R^TS_vw_R>0 with negative integrand near v=0.
11. GS §§12–12.1: a(u)>0, q''(u)>0 ∀u≥0 (Arb); HK>J². GS §12.2: triples SPD for 0<R<R0.
12. GS §16.1: (INT-ASYM) for fixed k,l; GS §16.4: fixed complex blocks PD for small ε (threshold depending on the list).
13. GS §17.2–17.5: (RES-SOS); D_q>0; R_res PD on any finite set of distinct integers, ∀|y|<π/4;
    R_res ≥ c_*E_y with explicit c_*.
14. GS §18: integer A PSD ⇔ real A PSD; §18.7 any tail suffices; §18.9: λ_A(T)≥0 ∀T ⇔ K_{M_Φ} PSD ⇔
    real A PSD ⇔ integer A PSD (or tail); Tate ⇔ P(1)=0, ∫P=0.
15. GS §19.7: Q(E_1)>Q_B(E_1)>1/2000. §19.8: Γ_{1..N} PSD ∀N ⇔ target. §19.9: block {E_1,E_2} PD.
    §19.10: Γ_{J..N} PSD ∀N ⇔ target; lemma CPD-m (m finite constraints).
16. HY §5: K_{M_a} PSD at all sizes via (GRAM); HY §8: the same for φ_{a,β}, β≥0 (Robin).
17. HY §12.5: wave formula for L; HY §12.6: exact realization with theta observation and strong equation (no sign).
18. HY §2.1 via GS §2.1: A of the hyperbolic model PSD.

## C. OPEN obligations (precise statements)

C1. **Global target** (equivalents, GS §§2.1, 2.2, 18, 18.7, 18.9, 19.8, 19.10): for every finite
family (x_i)⊂R and c∈C^n, Σc_ic̄_jA(x_i,x_j)≥0. Already attempted: §§3–19 and all of HY.

C2. **Joint critical inequality (GS §17).** For y with |y|<π/4, every finite support S⊂Z_{>0}
and every c∈C^S: Σ_{k,l}c_kc̄_l Off_y(k,l) ≥ −Σ_{k,l}c_kc̄_l R_res,y(k,l). At y=0 this is exactly
A_0 ⪰ 0 on integer blocks, equivalent to C1. For y≠0 no equivalence is claimed. Already proved:
R_res,y ≻ 0 and R_res,y ≥ c_*E_y (§17.5).
- **§17.6 excludes**, for each fixed y∈[0,π/4), the existence of C_y<∞ with Off_y ≥ −C_yE_y, and that of
  δ_y>0 with A_y ≥ δ_yR_res,y (i.e. Off_y ≥ −(1−δ_y)R_res,y). Falsifier: pairs (k,k+1), k→∞,
  with A_y[c^{(k)}]/R_res[c^{(k)}]→0.
- **§17.6 does not exclude** Off_y ≥ −R_res,y (zero margin), non-uniform constants, other weights, nor negative A.
- **§17.7 excludes**, at y=0, |Q_C(F)| ≤ M·W(F) for F in the finite span of Θ_k, W with weight 1+log t.
- **§17.7 does not exclude** control of the nonresonant remainder by R_res nor a joint signed balance.
- Consequences of other sections: GS §8.11 (no Cauchy margin), §18.7 (no margin on
  finite observables) and §18.8 (nor on a real moment). A proof of C2 must be margin-free.

C3. **CPD of log A** (GS §4.1): Σc_ic_j log A(t_i,t_j) ≥ 0 if Σc_i=0; also PSD of H=∂_t∂_s log A (GS §4.2 l.329).

C4. **Triples** (−R,0,R) for R∈[R0,8) and arbitrary triples (GS §§10, 12.2–12.3).

C5. **Thermal family:** Γ_{1..N} ⪰ 0 ∀N, or Γ_{J..N} ⪰ 0 ∀N for a fixed J (GS §§19.8, 19.10). Signed: N≤2.

C6. **One smoothed density:** K_σ PSD for some σ>0 (GS §7.1).

C7. **Compensation between slices** (GS §6), **difference term against V<0** (GS §19.12) and
**joint control of the nonresonant part** (GS §17.4).

C8. **Green-type representation for Φ** (HY §6): construct a positive H independent of u with
M_Φ(u)/u = ½Tr(H+u²/4)^{−1}, or a positive Green identity reproducing A.
- **HY §12.6 constructs** ℋ, Q, C, D (self-adjoint), B (symmetric, densely defined and closable,
  not self-adjoint), an exact continuous observation h with ⟨Q(v),h⟩=q_θ(v), and the strong equation
  Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y with ⟨Y_ν(2π),h⟩=Z(2ν).
- **HY §12.7 excludes** every M(r) self-adjoint, bounded, strictly positive, C² in operator
  norm and local in r with M'=−DM−MD (weak) and E=−C+D²+2bB̄ symmetric in ⟨M·,·⟩. Leading coefficient −I, no new connections.
- **HY §12.7 does not exclude** nonlocal metrics, unbounded metrics with other domains, new connections
  nor other realizations. It does not produce negativity of A.

## D. Contradictions or weakenings with respect to RULES_AVOID.md / OBJECT_SPEC.md

1. RULES_AVOID D9 (see A): «does remain open» presents Off ≥ −R_res as a residue. At y=0 it is the
   complete integer target (GS §§17.6, 18, 18.9), and it must be proved with zero margin.
2. RULES_AVOID D15: incomplete scope (see A).
3. RULES_AVOID B4 cites «211/HYPERBOLIC §§6–13» as closing «mixtures, convolutions, congruences,
   transports, interpolations». HY only excludes declared classes. HY §7.2 says that no general prohibition
   of transfers or of positive operators is recorded. HY §8 (Robin) is a proved positive
   operation, and HY §§12.5–12.6 are positive constructions. GS §4.3: «Other positive references
   and an exact signed compensation are not excluded».
4. RULES_AVOID §C «closures by cosh products»: HY §§11, 13 exclude representation and approximation.
   They do not decide whether multiplying by cosh preserves PSD («Such preservation has been neither proved nor refuted»).
5. RULES_AVOID B2 («every bound with remainder loses more»): there are fixed signed blocks with explicit remainder
   bounds (GS §§10, 12.1, 19.7, 19.9). B2 holds for the global margin, not for fixed vectors.
6. OBJECT_SPEC §1, form (G) a_T=‖V_TF‖²+ρ_T. GS §18.7 (and §18.9 primitive) prevents, in integer-scale
   coordinates, a unique identity Σw_α|ℓ_α|² with all ℓ_α of finite support. It also prevents
   any diagonal ρ_T with nonnegative weights (including the observables f_{d,q}). GS §8.11 prevents
   ρ_T from containing a uniform margin c‖f‖², and GS §18.8 a minorant by a real moment. OBJECT_SPEC
   does not record these restrictions: V_T must use global observables not finitely supported.
7. OBJECT_SPEC §3 (L-comp, «unreviewed»): GS §8.11 already proves one case, with Cauchy comparator cG,
   for any real analytic M with M=O(u) at 0 and on any interval. HY l.675 records that
   GLOBAL already refutes K_Φ ≥ εK_{2π}. GS §§8.7–8.10 give positive even analytic densities
   arbitrarily close to Φ with K not PSD.
8. OBJECT_SPEC §1 «PROVED reductions»: the exact reductions of GS §§2.1, 7.1, 18, 18.7,
   18.9, 19.8, 19.10 are missing. Not a contradiction.
9. GS l.15: the kernel A and the LT bridge have a public antecedent. Novelty must not be attributed.

## E. Coverage

- `POWER_GRAM_SLICES_OBSTRUCTION.md`: read completely, lines 1–2921 (last 2921). Consecutive
  reading in stretches of 200 lines, without skips.
- `POWER_HYPERBOLIC_MODEL_GRAM.md`: read completely, lines 1–966.
- `POWER_GRAM_SLICES_AUDIT.md`: read completely, lines 1–16.
- Also read completely: `RULES_AVOID.md`, `OBJECT_SPEC.md`, `POWER_CONE_001.md` and `POWER_BRIDGE_002.md`.
- Ranges not read: none. The externally cited files (GLOBAL, 053, 073, 084,
  085, 088, 105 and others) were not read.
