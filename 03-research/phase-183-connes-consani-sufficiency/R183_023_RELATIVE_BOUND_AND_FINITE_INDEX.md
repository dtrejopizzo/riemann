# R183.023 — Null relative bound of the prime term against Sonin and finite index of E_S − (1−η)Son

## 0. Verdict

* **Tension resolved (PROVED).** The prime term is bounded on L²(I_T) in
  the h variable, and hence *form-bounded relative to Son with relative
  bound 0*: Son controls ∫log(2+|s|)|ĥ|², which dominates any multiple of
  ‖h‖² outside a frequency band. In CC's ξ variable (h=(½−∂)ξ) the prime
  term has kernel (¼−d²/du²)·½(δ_{log2}+δ_{−log2})(u), is bounded on H¹
  and Son controls the "log-H¹" norm ∫(¼+s²)log(2+|s|)|ξ̂|². There is no
  contradiction with R183.018/019's NO-GO: that one subtracts Son with
  coefficient **exactly 1** (η=0).
* **Central theorem (Theorem 3.1, PROVED, given R183.020's Lemma
  ε-L∞).** For every T>0, S={∞}∪{p<e^{2T}}, η∈(0,1] and γ>0 there is an
  explicit finite range N=N(η,T,S,γ), an explicit space V_N (prolates of
  I_T at bandwidth s_*) and c>0 with

      E_S − (1−η)Son ≥ −L·Π_{V_N} + c(Son + ‖·‖²)   on C_c^∞(I_T),

  hence n₋(E_S − (1−η)Son) ≤ N < ∞. Growth: s_* ≈ 2π e^{2A/η},
  N ≲ (2T s_*/π)(L/γ): exponential in 1/η.
* **Lower bound (Theorem 4.1, PROVED except for the rate).**
  n₋(E_S − (1−η)Son | primitives ∩ ker ℓ) → ∞ as η↓0, for each T>½log 2.
  More precisely, n₋ ≥ N if η < η_N(T), with η_N ≍ 1/log N (rate:
  CONDITIONAL, sketch). Hence n₋(η) = exp(Θ(1/η)) at fixed T.
* **Threshold η_1(T).** n₋ is nonincreasing in η, so {η : n₋ ≤ 1} is an
  interval [η_1(T),1] (possibly empty). For T ≤ ½log2, η_1=0 (CITED, CC);
  for T>½log2, η_1(T) ≥ c₀/log(C/(2T−log2)) > 0 (PROVED, §4.3). That
  η_1(T)<1 essentially amounts to *coercive* positivity of E_S in the
  window (§5, PROVED in both directions except alignment): Lemma (L-Son)
  is a **reformulation** of semilocal row D, not a weakening.
* **Relation to Paper 46.** Theorem 3.1 is Paper 46's "finite section +
  Schur complement with a tail controlled by thm:P" mechanism (l.2503),
  now applied with the primes included and a fraction η of Son retained.
  Novelty: only the resolution of the tension and the exp(Θ(1/η))
  behavior; the rest is **reformulation** (§6).

Neither RH nor the closure of D is claimed.

## 1. Corpus consulted

* R183.015 (phase identity, m(s)=−log π+Re ψ(¼+is/2)); R183.018 (§3
  identity E_S=Son+R, §4 fiberwise Toeplitz, Thm 5.1 NO-GO); R183.019
  (§1 ξ dictionary, §4 symbol (¼+s²)cos(s log p), Thm 4.1); R183.020
  (Lemma ε-L∞: M_T:=sup_{[1,e^{2T}]}|ε|<∞).
* CC 2006.13771 §6 (local text phase-137, l.2900–3200): K_I, (134)–(137),
  Lemma 6.9/6.10, Thm 6.11 — the case η=0, S={∞}, T=½log2, n₋=1.
* **114_d_67** (phase-116/previous-phase-114, Thm 3.1): the arithmetic
  defect has **infinite** relative bound against Green's energy
  E_G≈‖u'‖² (no logarithm). Here: relative bound **zero** against Son
  (with a logarithm). Compatible: 114_d_67 already notes that "the full
  Gamma term reverses high-frequency growth"; this file quantifies that
  statement.
* Master grid R162_2300: grep for "relative bound", "finite rank",
  "Ky Fan", "inertia" found no results in the current grid. MAP_1 NG-E4
  (pointwise routes for relatively bounded forms: PROVED-IMPOSSIBLE)
  refers to interpolation/Gram, not to this spectral argument.
* Paper 46: thm:P (Ky Fan ceiling, l.2672), cor:P3 (n₋ ≤ 5/7/8), rem:P4,
  the Schur reduction (l.2500–2505), thm:index.

## 2. Normalizations and the exact prime term in the window S={∞,2}

ĥ(s)=∫h e^{−ist}dt, ‖h‖²=(1/2π)∫|ĥ|². I_T=(−T,T). By R183.015/018:

    E_S(h) = W_∞(h) − B(h),   W_∞(h)=(1/2π)∫m|ĥ|²,
    Son(h) = W_∞(h) + E(h),   E(h)=∫c_h(x)ε(e^{|x|})dx = ⟨h,C_ε h⟩,
    R_{S,T} = −C_ε − B,       B=Σ_{p<e^{2T}} B_p.

Hence, for η∈[0,1],

    E_S − (1−η)Son = η W_∞ − (1−η) E − B.                          (2.1)

(PROVED: algebra on R183.018 Prop. 3.1.) η=0 is R183.018's remainder R.

### 2.1 Window ½log2 < T < ½log3, S={∞,2} — PROVED

Since 2T<log 3<2 log 2, only p=2, k=1 contributes. With a=log2, x=2^{-1/2}:

    B(h) = 2 log2 · 2^{-1/2} Re c_h(a) = √2 log2 · Re c_h(a).

**Variable h.** Fibering as in R183.018 §4, n(r)=2 for r∈[0,2T−a) and
n(r)=1 for r∈[2T−a,a). On the 2-dimensional fibers, B is
(√2 log2)·[[0,½],[½,0]], with eigenvalues ±log2/√2 ≈ ±0.4901; on the
1-dimensional ones, B=0. Hence

    spec(B) = {−log2/√2, 0, +log2/√2}, each of infinite multiplicity,
    ‖B‖ = log2/√2.                                                 (2.2)

**Variable ξ (CC).** For ξ∈C_c^∞(I_T) and η_ξ=(½−∂)ξ, the cross term
∫(ξ'(t)ξ̄(t−a)+ξ(t)ξ̄'(t−a))dt=∫∂_t[ξ(t)ξ̄(t−a)]dt=0, so

    c_{η_ξ}(a) = ¼ c_ξ(a) + c_{ξ'}(a),
    B = √2 log2 ∫∫ ξ̄(x) k(x−y) ξ(y) dx dy,
    k(u) = (¼ − d²/du²) [½(δ(u−log2)+δ(u+log2))],                   (2.3)

and its symbol is √2 log2 (¼+s²) cos(s log2) (confirming R183.019 §4;
E_S's sign carries −B). k is a second-order distribution supported at
|u|=log2.

**Space where it is bounded.** By (2.2), |B(h)| ≤ (log2/√2)‖h‖²_{L²}; in ξ:

    |B| ≤ (log2/√2)(¼‖ξ‖² + ‖ξ'‖²)        (ξ∈H¹_0(I_T)).             (2.4)

It is bounded on H¹_0(I_T) (ξ) ≡ L²(I_T)∩{∫h e^{−t/2}=0} (h); **not** on
L²(ξ) (R183.019 Thm 4.1). In the ξ metric, 2ε'(1^+)(Id−K_I) (S={∞},
T≤½log2) is bounded on L²(ξ), which explains why CC's mechanism does not
admit primes with η=0.

## 3. What norm Son controls, and the finite-index theorem

### Lemma 3.0 (m) — PROVED (Stirling CITED)
(i) m is even and strictly increasing in |s|: by the series
Re ψ(a+iy)−ψ(a)=Σ_{n≥0} y²/((n+a)((n+a)²+y²)), a=¼, y=s/2.
(ii) m(0)=−log π+ψ(¼)≈−5.372; m(s)=log(|s|/2π)+O(s^{−2}) (Stirling), with
zero s_0≈2π; |m(s)−log(2+|s|)| ≤ C_m for all s.

### Proposition 3.0 (Son's norm) — PROVED
With κ_T:=‖C_ε‖ ≤ ∫_{−2T}^{2T}|ε(e^{|u|})|du ≤ 4T M_T (Young for the
difference kernel; M_T from Lemma ε-L∞):

    (1/2π)∫log(2+|s|)|ĥ|² − (C_m+κ_T)‖h‖² ≤ Son(h) ≤ (1/2π)∫log(2+|s|)|ĥ|² + (C_m+κ_T)‖h‖².

That is, Son+K‖·‖² ≍ ‖h‖²_{L log}:=(1/2π)∫log(2+|s|)|ĥ|²; in ξ,
≍ (1/2π)∫(¼+s²)log(2+|s|)|ξ̂|² ("log-H¹"). Proof: Son=W_∞+E, |E|≤κ_T‖h‖²,
Lemma 3.0(ii). □

**Corollary 3.0' (relative bound 0) — PROVED.** For every δ>0,
|B(h)| ≤ δ·Son(h) + ‖B‖·⟨h,S_{c}h⟩ + δ(κ_T+|m(0)|)‖h‖², where
S_c=Q_T 1_{|s|<s_δ} Q_T is Paper 46 thm:P's time–band operator with
c=T s_δ and m(s_δ)=‖B‖/δ. (Outside |s|<s_δ, ‖B‖ ≤ δm; inside, one pays
⟨S_c h,h⟩.) S_c is compact of trace 2c/π: the "constant" is compact, not
merely bounded. This holds in both variables (the forms do not depend on
the metric).

### Theorem 3.1 (finite index) — PROVED (given Lemma ε-L∞)

Let T>0, S={∞}∪{p<e^{2T}}, β_S:=‖B‖ (≤Σ_{p<e^{2T}}2log p·p^{−1/2}/(1−p^{−1/2});
=log2/√2 in §2.1), η∈(0,1], γ>0. Define

    A := (1−η)κ_T + β_S + 2γ,   s_* := min{s≥0 : m(s) ≥ 2A/η},
    L := η|m(0)| + A,           N := #{k : λ_k(S_{T s_*}) > γ/L},
    θ := min{1, γ/(2A+ηκ_T)},   c := min{θη/2, γ/2}.

Let Π_N be the projection onto the first N prolates ψ_0,…,ψ_{N−1} of I_T
at bandwidth s_* (eigenvectors of S_{Ts_*}). Then, for h∈C_c^∞(I_T),

    E_S(h) − (1−η)Son(h) ≥ −L‖Π_N h‖² + c(Son(h) + ‖h‖²).            (3.1)

*Proof.* By (2.1) and |E|≤κ_T‖h‖², |B|≤β_S‖h‖²:
LHS ≥ (1/2π)∫(ηm − A)|ĥ|² + 2γ‖h‖². If |s|≥s_*, ηm−A ≥ ηm/2 ≥ 0
(monotonicity, Lemma 3.0(i)); if |s|<s_*, ηm−A ≥ ηm(0)−A = −L. Hence

    LHS ≥ (η/2)(1/2π)∫_{|s|≥s_*} m|ĥ|² − L⟨S_{Ts_*}h,h⟩ + 2γ‖h‖².

By the spectral theorem, L·S_{Ts_*} ≤ LΠ_N + γ·Id. Also, since m_+<2A/η on
|s|<s_*, Son ≤ (1/2π)∫m_+|ĥ|² + κ_T‖h‖² ≤ (1/2π)∫_{|s|≥s_*}m|ĥ|² + (2A/η+κ_T)‖h‖².
Multiplying by θη/2 ≤ η/2 and using θ(A+ηκ_T/2) ≤ γ/2:

    LHS ≥ (θη/2) Son − (γ/2)‖h‖² − LΠ_N + γ‖h‖² ≥ −LΠ_N + c(Son+‖h‖²). □

**Corollary 3.2 — PROVED.** n₋(E_S−(1−η)Son) ≤ N on C_c^∞(I_T) (and on
the closure in the Son+‖·‖² norm), and the negative part lives (in the
Schur sense) on V_N=span{ψ_k}_{k<N}: see §5. Bounds on N:

* trace (PROVED): N ≤ (L/γ)·2Ts_*/π;
* Ky Fan (Paper 46 thm:P, PROVED): N ≤ min{k : Λ_k(Ts_*) ≤ γ/L};
* Landau–Widom (CITED): N = (2/π)Ts_* + O(log(Ts_*)·log(L/γ)).

With Lemma 3.0(ii), s_* = 2π e^{2A/η}(1+o(1)) as η→0, so

    N(η,T,S) ≲ 4T e^{2A/η}·(L/γ)   (trace)   ~ 4T e^{2A/η} (Landau–Widom).   (3.2)

**Growth in T.** In window S={∞,2}, A=(1−η)κ_T+log2/√2+2γ with
κ_T ≤ 4TM_T bounded: N linear in T. With all primes, β_S≲4e^{T}(1+o(1))
(PNT, crude norm bound), so N ≤ exp(O(e^{T}/η)): finite, but doubly
exponential. This upper bound is crude; see §4.4.

**Reading.** R183.018's NO-GO is exactly η=0: then s_*=∞ and the negative
band of the prime term, with positive density at every frequency
(spectrum ±log2/√2 of infinite multiplicity), has nothing to absorb it.
For η>0 the negative window is the band |s|≲2πe^{β/η}, whose number of
degrees of freedom in I_T is ~(2T/π)·2πe^{β/η}: finite.

## 4. Lower bound: the index explodes as η↓0

### Lemma 4.0 (off-diagonal kernel of W_∞) — PROVED (standard)
The distribution m̌ (W_∞'s difference kernel) is, off u=0, a smooth
function with |m̌(u)| ≤ C_W/|u| for 0<|u|≤4T. (m−log(2+|s|) is an
order-−1 symbol with derivatives of order −1−j by Stirling with
derivatives; the transform of log(2+|s|) away from the origin is
−1/(2|u|)+smooth; standard integration by parts.) Consequently, if f,g
have supports at distance ≥d>0, |W_∞(f,g)| ≤ (C_W/d)‖f‖₁‖g‖₁.

### Theorem 4.1 — PROVED (given Lemma ε-L∞ and Lemma 4.0)
Let T>½log2 and S⊇{∞,2}∪{p<e^{2T}}. For each N≥1 there exists η_N(T)>0
such that, for 0≤η<η_N(T), the form E_S−(1−η)Son is negative definite on
an N-dimensional subspace of primitive tests (∫h e^{±t/2}=0) — in the ξ
variable, of C_c^∞(I_T) — and hence n₋ ≥ N−1 on primitives ∩ ker ℓ.

*Proof.* R183.018 Thm 5.1's construction with N pairs
x_j=β(·−t_j)+β(·−t_j−a), β=c_w''−c_w/4, a=log2, points t_j fixed
**before** w with mutual separations ≥ d_N>0 outside F (possible for
small w, since 2T−a>0 and F is finite). For x=Σc_jx_j,
‖x‖²=2‖β‖²Σ|c_j|² (disjoint supports) and:
(a) primes: −B(x) = −√2 log2‖β‖²Σ|c_j|² (R183.018, exact);
(b) compact archimedean: |E(x)| ≤ M_T‖x‖₁² ≤ 4NM_T‖β‖₁²Σ|c_j|² = O_N(w)‖β‖²Σ|c_j|²;
(c) W_∞: diagonal W_∞(β(·−t))=(1/2π)∫m|β̂|² ≤ (log(1/w)+C_β)‖β‖² (β̂
concentrated at |s|~1/w, Lemma 3.0(ii)); cross terms (two bumps of a
pair, at distance ≥a−2w, and different pairs, at distance ≥d_N−2w): by
Lemma 4.0, O_N(‖β‖₁²)=O_N(w)‖β‖².
By (2.1), (E_S−(1−η)Son)(x) ≤ ‖β‖²Σ|c_j|²[2η(log(1/w)+C_β) − √2log2 + O_N(w)].
Fix w=w_N with O_N(w_N) ≤ (√2log2)/4 and η_N := (√2log2)/(4(log(1/w_N)+C_β)). For
η<η_N the bracket is ≤ −(√2 log2)/4 <0. β and its translates are
primitive (R183.018), and in ξ, ξ_j=(½−∂)^{-1}x_j has compact support.
ker ℓ removes one dimension. □

### 4.2 Rate — CONDITIONAL (sketch)
Taking d_N≍(2T−a)/N and w_N≍d_N/(N log N)^{1+o(1)} (so the cross-term
sums Σ_j C_W‖β‖₁²/(j d_N) are small) gives η_N ≍ 1/log N, i.e.
n₋(η) ≥ exp(c₁/η) with c₁≈√2log2/8 (heuristic). Together with (3.2):
**n₋(E_S−(1−η)Son) = exp(Θ(1/η)) at fixed T.** The upper-bound (2A) and
lower-bound (≈0.12) constants do not match; the "correct" exponent from
the frequency picture is the solution of ηm(s)=log2/√2, i.e.
s≈2πe^{0.49/η} (heuristic).

### 4.3 Threshold η_1(T) — PROVED
(E_S−(1−η)Son) is nondecreasing in η (Son≥0), so n₋(η) is nonincreasing.
Let η_1(T,S):=inf{η∈[0,1] : n₋(E_S−(1−η)Son | primitives∩ker ℓ) = 0}. For
R183.017's rank-one correction the relevant thing is n₋ ≤ 1 on
primitives, and = 0 on ker ℓ (R183.019 Cor. 3.2: alignment ⟺ positivity
with a gap on ker ℓ). Then:
* T≤½log2, S={∞}: in the ξ metric, η=0 works (CC Thm 6.11, CITED): η_1=0.
* T>½log2: by Thm 4.1 with N=2 (two pairs, in ker ℓ there remains ≥1
  negative direction), η_1(T) ≥ η_2(T)>0. With a window of length
  2T−log2, the separations and w scale with it and the ratio
  ‖β‖₁²/(d‖β‖²)=O(w/d) is invariant; this gives
  log(1/w_2) ≈ log(C/(2T−log2)), hence

      η_1(T) ≥ c₀ / log(C/(2T−log2))   (T↓½log2),                    (4.1)

  with c₀,C>0 independent of T near ½log2. The jump 0→>0 at T=½log2 is
  continuous (η_1→0 in the lower bound), consistent with CC.

### 4.4 Growth in T at fixed η — OPEN
The construction of §4.1 requires w smaller than the minimal distance
between points of F={k log q}, which with all primes p<e^{2T} is
~e^{−2T}; this only gives η_N ≲ 1/T. It is not proved that n₋(η,T)→∞ with
T at fixed η, nor the opposite. The upper bound (3.2) is doubly
exponential; the truth lies between the two. OPEN.

## 5. Consequences: Lemma (L-Son) is a reformulation

### Proposition 5.1 (Schur reduction to dimension N) — PROVED
Under (3.1), let V=V_N, P=Π_N. On V^⊥∩domain, E_S ≥ (1−η)Son + c(Son+‖·‖²)
≥ c‖·‖²>0. Hence (R183.019's Theorem 3.1 in block version, Schur
complement): E_S ≥ 0 on C_c^∞(I_T) ⟺ the N×N matrix

    M_N(T,S) := E_S|_V − E_S(V,V^⊥)(E_S|_{V^⊥})^{−1}E_S(V^⊥,V)

is ≥0. Same statement restricted to primitives/ker ℓ. **Restatement:** it
is Paper 46's "finite section + Schur complement over the tail" (l.2503,
there for A_∞ with no prime comb, with the tail controlled by thm:P's
trace), now with primes included and the tail made coercive by ηSon. The
dimension N (exponential in 1/η) is much larger than cor:P3's 5/7/8 or
phase 155's arena ≥12: the reformulation does not reduce the difficulty.

### Proposition 5.2 (L-Son ⟺ coercive positivity) — PROVED
(a) If E_S ≥ c'(Son+‖·‖²) on primitives∩ker ℓ with c'∈(0,1], then
E_S−(1−η)Son ≥ (c'−(1−η))Son + c'‖·‖² ≥ c'‖·‖² for 1−η ≤ c': (L-Son)
holds with b=0 and η=1−c'<1.
(b) If (L-Son) holds with η<1 (and alignment δ>0), then on ker ℓ
E_S ≥ (1−η)Son + c''X ≥ c''(Son+‖·‖²) for some c''>0 (R183.019
Cor. 3.2). Hence (L-Son, η<1, aligned) ⟺ coercive positivity of E_S on
ker ℓ in the window. It is a **reformulation** of semilocal row D (the
version with a gap), not a weaker condition. With η=1 it is not even
coercive.

### 5.3 Comparison with the "single direction" requirement
For R183.017's rank-one correction to work, η∈[η_1(T),1) is needed.
Proved: η_1(T)>0 for T>½log2 (4.1), and η_1<1 ⟺ (5.2). §3's upper
bounds (N≫1) **do not** prove N>1 for every η: they are upper bounds.
Hence there is **no** structural NO-GO for a single-correction mechanism
with η near 1; only for η<η_1(T) (in particular for every η below
c₀/log(C/(2T−log2))). The honest formulation:

    D in the window ⟸ positivity of an N(η,T)×N(η,T) matrix (Prop. 5.1),
    with V_N = explicit prolates of I_T at bandwidth s_*(η),

which is Paper 46's finite-mode arena — a reformulation, not a new
mechanism.

## 6. What is new and what is not

* New (PROVED): (i) relative bound 0 of the primes against Son in both
  metrics and with a compact "constant" (Cor. 3.0'), reconciling the
  NO-GO (η=0) of R183.018/019 with 114_d_67 (Green with no log: infinite
  relative bound); (ii) Theorem 3.1 with explicit V_N and
  N(η) ≤ exp(O(1/η)); (iii) Theorem 4.1: n₋→∞ as η→0 and η_1(T)>0 with
  bound (4.1); (iv) exact spectrum {0,±log2/√2} of the prime term in
  window {∞,2} (2.2) and kernel (2.3).
* Reformulation: Prop. 5.1 (Schur, Paper 46 l.2503) and Prop. 5.2
  (L-Son ⟺ coercive positivity).

## Status

```text
exact prime-2 kernel in ξ, (¼−d²/du²)½(δ_{±log2}); bounded on H¹_0      PROVED
spec(B)={0,±log2/√2}, mult. ∞, window {∞,2}                            PROVED
Son+K‖·‖² ≍ ∫log(2+|s|)|ĥ|² (log-H¹ in ξ)                               PROVED (Stirling CITED, ε-L∞)
relative bound 0 of B against Son, compact remainder (time–band)         PROVED
Thm 3.1: E_S−(1−η)Son ≥ −LΠ_N + c(Son+‖·‖²), N<∞ explicit                PROVED (given Lemma ε-L∞)
N ≲ 4T e^{2A/η}; bound via thm:P / Landau–Widom                          PROVED / CITED
Thm 4.1: n₋→∞ as η→0, T>½log2                                            PROVED (standard Lemma 4.0)
rate n₋ = exp(Θ(1/η))                                                    CONDITIONAL (sketch)
η_1(T) ≥ c₀/log(C/(2T−log2)) >0;  η_1=0 for T≤½log2                     PROVED / CITED (CC)
n₋(η,T) at fixed η as T→∞                                                OPEN
Prop. 5.1 reduction to N×N matrix (Schur)                                 PROVED (reformulation of Paper 46)
Prop. 5.2 (L-Son, η<1) ⟺ coercive positivity on ker ℓ                     PROVED (reformulation)
η_1(T)<1 for some T>½log2 / E_S≥0 / row D                                 OPEN
```

## Review points

1. **Lemma ε-L∞.** All the quantitative material uses κ_T ≤ 4TM_T; it
   inherits R183.020's series convergence. Without it, ‖C_ε‖ is still
   finite if C_ε is Hilbert–Schmidt (R183.018 §3), which suffices for
   Thm 3.1.
2. **Lemma 4.0.** The bound |m̌(u)| ≤ C/|u| is stated via standard symbol
   theory (m ∈ S^0 log-classical); the integration by parts is not
   written out. It is Thm 4.1's weakest point. Robust alternative: use
   only that W_∞ restricted to pairs of separated supports is an
   integral operator with a smooth bounded kernel, which is immediate
   (m̌ smooth away from 0).
3. **Domain.** (3.1) is proved on C_c^∞(I_T) and extended to the closure
   in the Son+‖·‖² norm; n₋ is the same in both (density + closed form).
   Switching to the ξ variable is a bijection C_c^∞↔{∫h e^{−t/2}=0}: n₋
   changes by ≤1.
4. **(4.1)** uses that the geometry scales with 2T−log2; the constant C
   depends on profile c₀ and it must be checked that O(w/d) is uniform
   (it is by scaling, but the E and diagonal W_∞ terms are not
   scale-invariant: the diagonal gives log(1/w), exactly the logarithmic
   loss).
5. **There is no NO-GO for η near 1**: §5.3 should not be read as
   impossibility; Thm 3.1's N(η) is an upper bound.
6. No statement uses zeros of ζ nor RH; E_S≥0 is not claimed.
