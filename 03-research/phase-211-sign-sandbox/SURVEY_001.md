# Audit of Papers 01–42 for reuse toward window positivity (a_T on P_T)

Scope: standalone audit of the quadratic form a_T(F) and its finite reduction S_{T,k} / the Toeplitz
matrix [Ξ_{F0}(log(m/k))] of problem (S). No equivalence between this problem and any other
classical conjecture is used or implied anywhere below; papers 01–42 are read only as a toolbox of
techniques, independent of what each paper's own narrative frames them as proving.

---

**Paper 01 — Critical-line survey.** Expository (CITED/ARGUED), proves no new theorem. Its only
load-bearing content is the observation that every direction bottoms out in a positivity statement —
already absorbed into the programme's framing. Nothing new for a_T.

**Paper 02 — ω-class decomposition.** PROVED unconditional bounds on an amplification ratio for
Dirichlet polynomials; CONDITIONAL master theorem tying a uniform bound to growth of ζ. The
ω(n)-indexed splitting technique is about size, not sign, and has no quadratic-form structure. Not
applicable to a_T.

**Paper 03 — Sign of inter-class interference.** PROVED (mean value theorem) + NUMERICAL. Explains a
sign artifact of a different, unrelated quantity (energy ratio r of Dirichlet polynomials). No
transferable technique.

**Paper 04 — Davenport–Heilbronn null result.** NUMERICAL only; tests a growth-law prediction for a
function with no Euler product. No structure usable on a_T.

**Paper 05 — ω-class hierarchy / multiplicative chaos.** PROVED arithmetic core connecting moment
exponents to per-prime weights; CITED chaos identification. Combinatorial/probabilistic, not a
quadratic form on L²(−T,T). Nothing reusable.

**Paper 06 — Why RH resists (classifier).** ARGUED/PROVED meta-classification of four positivity
families, each unconditional at finite order, open at full order. Useful only as taxonomy; the
"finitization gap" vocabulary is already subsumed in Paper 47's framing of S_{T,k} as the exact
finite object. No new tool.

**Paper 07 — Localized Weil detector.** PROVED: Gram matrix Q(T₀,σ,J) = M_zeros − M_arith on
Hermite–Gauss tests, `thm:forced` (off-axis perturbation lowers λ_min quadratically with explicit
constant) and `thm:trunc` (truncation error η(X) ≤ A exp(−α(log X)²) from the PNT alone, unconditional).
*Relevant to a_T*: `thm:trunc` is an explicit, unconditional, PNT-only bound on the error from
truncating the prime sum at a finite head — this is exactly the kind of estimate needed to control the
tail beyond the declared contacts N_T in passing between S_{T,k} and S_{T,k(T)+1} as k grows, and it
was never carried into Papers 46–48, which instead treat truncation via the finite comb N_T directly
(no quantitative head-vs-tail error bound of this shape appears in Paper 47). Candidate for reuse in
estimating the margin needed in (L2).

**Paper 08 — Weil–Kreĭn realization.** CONDITIONAL on hypothesis (H) for the operator closure;
unconditional Kreĭn identity E*JE and the no-go that bounding ‖K‖≤1 from the zero side restates
positivity. This is exactly the Kreĭn/Schur/coercivity family marked **closed** in the routes index
("Coercivity, Schur, bundle/inertia, Wiener–Hopf, Nyquist, two sectors, witnesses"). No new reason to
revisit; the no-go (`thm:C`) already anticipates the shape of the (L2) barrier in Paper 47.

**Paper 09 — Stable arithmetic fingerprints.** PROVED stability/concavity of λ_min(Q) under agreement
of local data. Elementary perturbation theory for a *different* finite form (fixed T₀, σ, not the
window-T̂ family). The concavity/extremal-reduction technique (`thm:concave`) — reducing a bound over a
coefficient box to its extreme points — is a reusable device not present in Paper 47's treatment of
S_{T,k}, which never reduces over boxes of admissible Λ(n). Minor candidate.

**Paper 10 — Anatomy as local invariant.** PROVED Euler-product ⇔ factorizing anatomy, Satake
recovery, functoriality. A classification result about L-functions in general, not about the sign of a
single form. Not applicable.

**Paper 11 — Pontryagin index / finite defect.** PROVED reduction to RFB_X; both natural closure
mechanisms closed by computation (NUMERICAL NO-GO): cutoff grows like e^{2d}/10 and the near-null
space is infinite-dimensional. This is a genuine NO-GO already in the Kreĭn/finite-defect closed
family. No new angle for a_T.

**Paper 12 — Band-limited Weil–Carleson.** NUMERICAL: the generalized-eigenvalue constant C_band(d,T₀)
saturates to 1 once 2d/log T₀ ≳ 0.85, so there is **no arithmetic margin** from band-limiting alone —
an explicit NO-GO for that lever, already recorded. `thm:sinekernel` (subdominant spectrum = sine-kernel
determinantal Gram) is a genuinely different object from anything in Paper 47 (which works with the
Tate-exponential block structure, not a sine-kernel second-order expansion) — flagged below as an
overlooked identification, though it was explicitly matched to Connes–Consani prolate compression and
is CITED/NUMERICAL, not a proof tool with sign.

**Paper 13 — Heat-flow Lyapunov / de Bruijn–Newman.** PROVED Lyapunov monotonicity; NO-GO that the
flow alone is arithmetic-blind. Already the closed "Heat flow / de Bruijn–Newman" family. No
technique touches a_T, which has no flow parameter.

**Paper 14 — Modern routes, wrong-sign obstruction.** PROVED Hermite-form criterion (real-rootedness
is itself a positivity) and the arithmetic-blind shift-operator obstruction; the rest NUMERICAL/
CONDITIONAL. The Hermite-form criterion is a general real-rootedness-as-positivity device; a_T's
sign problem is already posed as a quadratic-form inequality, so this adds nothing beyond what is in
Paper 47 already.

**Paper 15 — Finite-to-full uniformity gap.** PROVED criterion for when "eventual" positivity upgrades
to "uniform" positivity (finite type or bounded threshold), and a Hodge–Riemann stability theorem for
towers of forms. *Possibly relevant*: a_T is literally a tower of forms indexed by T (monotone,
Lemma mono T in Paper 47); Paper 15's criterion (`thm:crit`) for when eventual-order positivity
upgrades to full uniform positivity was never checked against the S_{T,k} tower. It is a structural
criterion, not a proof, but it was never applied to this specific tower and is not listed in the
routes-tried index under any closed family. Flagged as a genuine untried application (see Top 10).

**Paper 16 — Unconditional finite bottom.** PROVED band-limited Parseval identity V(d,T) ≥ 0 and a
finite lower bound for the localized Weil form (semiboundedness only, no sign). The "second-moment
identity written as a band-limited square" technique (`thm:id`) is a genuine computational device
(writing a quadratic quantity as ∫|Σ e^{iγξ}|²dξ) distinct from anything carried into Paper 47, which
works from the explicit-formula side, not from a zero-side second moment. Since a_T's sign problem
is explicitly NOT to be attacked from the zero side (closed family: "Zero information"), this
technique is not usable without modification — noted but not promoted.

**Paper 17 — Lefschetz dichotomy.** PROVED no-go for a Tate-twist Lefschetz sl₂ acting on the zero
spectrum (CONDITIONAL on linear independence of ordinates). Geometric/representation-theoretic; the
closed "Function fields, Hodge, Arakelov..." family. Not applicable to the explicit finite matrix
S_{T,k}.

**Paper 18 — Localized Weil–Kreĭn index.** PROVED localization Q = Q_on + Q_off (on-line squares,
off-line Lorentzian blocks) and obstruction theorems excluding positive kernels / one-sided Cauchy
kernels / smooth non-degenerate families from carrying κ. Closed Kreĭn/Pontryagin family. The
Lorentzian-block decomposition technique is specific to an infinite zero-indexed operator, not to the
finite prime-indexed S_{T,k}; no transfer.

**Paper 19 — Arithmetic defect of off-line zeros.** PROVED parity κ ≡ 0 (mod 2); rest CONDITIONAL on
Hypothesis D (existence of off-line zeros), which has no analogue in the a_T problem (there is no zero
hypothesis to condition on). Not applicable.

**Paper 20 — Herglotz criterion.** PROVED unconditional boundary identity Re ξ'/ξ(½+iτ)=0 from the
functional equation alone, and the minimum-principle equivalence (positivity ⇔ no interior poles).
The boundary identity is a clean unconditional fact about the digamma/functional-equation data that
underlies m(τ) in Paper 47's eq:symbol — worth checking whether `thm:boundary`'s derivation gives a
sharper handle on m(τ)'s sign structure than the plain digamma formula currently used, but this is
speculative; no concrete new inequality for a_T is supplied.

**Paper 21 — ω-information barrier.** PROVED `thm:impossible` (no positive combination of ω-class
correlations cancels the zero contribution at any finite order). A genuine impossibility result, but
about a different object (shifted correlations C_k(h,N)), not about S_{T,k} or the near-coincidence
Toeplitz matrix. Not transferable as stated.

**Paper 22 — Moment rigidity (Meixner–Pollaczek).** PROVED ν ≥ 0 pointwise domination and a moment-
rigidity theorem via triangularity + Carleman's condition + Hardy's theorem (no OP asymptotics, no
kernel positivity). *Candidate technique*: the Carleman-determinacy argument ("constant Δ_n forces
ν = c·m_∞") is a genuinely different machine (moment problem determinacy) from anything in Paper 47's
toolbox (Schur complements, lattice/flat-top certificates, SOS). It was never re-examined for the
measure attached to s_T or to the near-coincidence part of (S). Flagged in the Top-10 list.

**Paper 23 — CCM Jacobi-operator reformulation.** PROVED structural facts about a limit Jacobi operator
J_∞ and an equivalence with an "incidence inclusion," reducing the remaining direction to a moment-
determinacy question — same determinacy flavor as Paper 22. Closed family ("Fredholm/determinants",
and indirectly the CCM skeleton already used in Papers 39–40, which feed Paper 47's Schur/Haynsworth
machinery). No new tool beyond what Paper 22 offers.

**Paper 24 — Trace/measure criterion.** PROVED dominance theorem R(s) = |ζ/ζ_on(½+is)|² ≥ 1
(unconditional) and eight pairwise-equivalent criteria; CONDITIONAL trace criterion on completeness of
Abel kernels in L²(dν); PROVED that the Hadamard product alone cannot supply that completeness
("the barrier is genuine"). The *dominance-measure* construction (an explicit nonnegative measure
built as a ratio-of-two-products difference) is structurally close to the near-coincidence part Near_M
of problem (S) — both are "difference of two explicit nonnegative objects, nonnegativity trivial,
completeness/correlation is the hard part." Not reused in Paper 47. Flagged as an overlooked structural
analogy (not a ready-made tool) in the Candidate-overlooked list.

**Paper 25 — Bridge theorem (Kreĭn–Langer).** CITED/CONDITIONAL; central conjecture OPEN. Already the
closed Kreĭn–Langer family. Nothing new.

**Paper 26 — Weil–Toeplitz algebra and logistic criterion.** PROVED trichotomy of window-index growth
(fat/thin/sub-resolution) within an axiomatized spectral model, and an exact corona-algebra symbol
σ(Q) whose spectrum is the limit set of window spectra (Cesàro states vs. norm states). *This is the
single clearest structural match in Papers 01–42 to problem (S)*: problem (S) is explicitly a
**Toeplitz-in-log(m/k) matrix**, and Paper 26 builds a whole C*-algebraic apparatus (bounded field of
window-indexed Hilbert spaces, ideal of sections vanishing at infinity, corona quotient, symbol map)
designed exactly to pass between "true at every window" and "true in the limit/mean over windows" —
which is precisely the quantifier structure of (L2)/(N)/(S) (per-window finite statement vs. the
T→∞ limit, cf. Lemma mono T in Paper 47). This machinery is NOT carried into Papers 46–48 at all; Paper
47 never mentions a corona algebra, a symbol map, or Cesàro-vs-norm states. The axiomatized model in
Paper 26 is a model, not a proof of positivity of the real symbol, so it does not resolve (S) by
itself, but the dictionary (bounded field over ℕ → corona symbol → trichotomy of asymptotic classes)
is an untried lens for the near-coincidence Toeplitz matrix [Ξ_{F0}(log(m/k))]. Top candidate below.

**Paper 27 — Exhaustion of 1D propagation.** ARGUED structural no-go across five mechanisms within the
CCM framework; PROVED strict positivity of the Abel kernel (`thm:wlambda-strict`) and single-scale
collapse. Already folded into the CCM/Kreĭn closed family (feeds Papers 39–40, hence Paper 47's
toolbox). The strict-positivity-of-Abel-kernel lemma is a technical ingredient already inherited
through that chain; no separate new tool for a_T.

**Paper 28 — Amplification survivor.** PROVED tensor-index superadditivity (`thm:tensor-index`,
`thm:amplify`) for the Kre�index of a *different*, two-variable Weil functional on a multiplicative
diagonal; two of three forms closed (NO-GO). The tensor/amplification idea is specific to negative-index
counting under Hypothesis D (an off-line-zero hypothesis), which has no counterpart for a_T (there is
no index to amplify — the question is a single sign, not a count). Not transferable.

**Paper 29 — Master quantifier.** ARGUED/CITED synthesis: identifies the common "quantifier inversion"
(averaged/generic/interior vs. individual/uniform/boundary) across three closed routes. Useful only as
a diagnostic frame; it in fact anticipates the same structure Paper 26's corona trichotomy addresses
more concretely — reinforces that Paper 26's apparatus, not just its slogan, deserves a second look.

**Paper 30 — Two-lemma architecture (Bohr–Rouché).** CONDITIONAL dichotomy on Lemma LP-112; PROVED
unconditional non-Stepanov-almost-periodicity result (shared with Paper 32). Self-approximation /
almost-periodicity machinery has no quadratic-form content; not applicable to a_T.

**Paper 31 — Curvature criterion.** PROVED exact Hadamard curvature identity C(γ) = ∂²_σ log|ξ(σ+iγ)|
at σ=½, written as an explicit sum over zeros, split into an analytic sector (computable from the
functional equation, i.e. essentially the digamma/m(τ) data of Paper 47) and a "zeta sector." This
splitting is structurally close to Paper 47's own split of s_T(τ) into m(τ) (archimedean, closed form)
minus the prime comb — but Paper 31's curvature identity is in σ (off the line, second derivative),
whereas a_T lives entirely on the line in τ. Not directly transferable, but the sector-decomposition
*technique* (isolate the part computable purely from Γ_ℝ and the functional equation; push everything
arithmetic into one residual sector) is exactly what Paper 47 already does for m(τ); no new content.

**Paper 32 — Stepanov almost-periodicity.** PROVED unconditional non-almost-periodicity in the band
sense for any sub-strip. Classical Ω-theorem machinery; no relation to a positive-definiteness
question on L²(−T,T).

**Paper 33 — Energy decomposition.** PROVED Green–Littlewood integral representation and a Cesàro-limit
theorem for the off-line energy I(T), plus a universal lower bound for mollified second moments
(`cor:lower`). The Cesàro-averaging technique for a divergent-looking quantity, and the "universal
lower bound for mollified second moments," are both about zero-counting energies, not about the
window quadratic form; no direct transfer, though the general device "a limsup/Cesàro argument always
has a limit even when the pointwise statement is open" is conceptually close to Paper 47's remark that
a two-sided asymptotic law for λ_A(T) is an open, stronger statement (§ secondary problems). Not a new
tool, just a precedent that such averaged statements can sometimes be proved unconditionally even when
the pointwise one cannot — worth noting as motivation, not as a ready method.

**Paper 34 — Architecture of obstruction (survey).** Survey of Papers 01–33; CITED/PROVED/NO-GO
restated. No new content beyond its sources.

**Paper 35 — Colligation route.** PROVED de Branges–Rovnyak model and an unconditional Bakry–Émery
curvature bound for the prime part of the Weil generator after Doob conjugation (`thm:angle`'s
surrounding material), plus identification of positivity with absence of a Schrödinger bound state for
an explicit Birman–Schwinger operator in which the pole at s=1 pins the spectral radius at 1. Already
largely in the closed "Coercivity ... Fredholm/determinants ... Birman–Schwinger" family (see routes
index). The specific unconditional Bakry–Émery curvature bound for the *prime part alone* (not the full
form) is a genuinely narrower object than what is cited in the index as closed; it was derived for a
different (CCM-generator) operator than S_{T,k}, and no one has checked whether the same Doob-conjugation
device applied to the finite matrix S_{T,k} produces a usable curvature lower bound. Minor candidate,
noted with caution since Bakry–Émery / Γ₂ methods for this programme are listed in `SURVEY_MODERN_
UNTRIED.md` as untried, i.e. the family is not closed for the *finite, window* object even though
related infinite-dimensional incarnations are.

**Paper 36 — Obstruction ledger + ARP-P.** The ARP-P chain reduces (14 of 15 steps closed) to Step 5,
the terminal-defect inequality δ_N ≥ 0 for all N — the classical Li criterion, an infinite discrete
family of inequalities, not the continuous-T window family of Paper 47. `thm:mirror-criterion`
(window positivity ⇔ ARP-P, PROVED as an equivalence) is the one place in Papers 01-42 that already
names something called "window positivity" — this must be checked for terminological or structural
overlap with Paper 47's a_T; from the text it is an equivalence to a Li-type arithmetic-Pick
discrete-N criterion, not literally the same object, but the identical name and the live H1–H5 node
machinery (`thm:live-H1,H2,H3,H5`) deserve a direct comparison against the finite matrix S_{T,k} since
they were never cross-checked against Paper 47 (Paper 36 predates Paper 47's restructure). Flagged as
an overlooked cross-reference requiring a one-round audit rather than a proof tool.

**Paper 37 — Death of the positivity family (Li–Keiper).** The core NO-GO catalogue: sixteen attacks on
(★) closed, each with an explicit witness; central structural claim that every instrument tried
certifies nonnegativity of the wrong kind of object (a measure/square/Gram form/TP kernel/completely
monotone function) while the true target (`the completed cocycle`) has a signed polar factor with an
exactly computable negative density. This diagnostic — "positivity instruments only ever certify
nonnegativity of an auxiliary gadget, never of the signed polar part itself" — is directly structurally
analogous to Paper 47's own finding that every proof attempt on (L2) falls into one of the excluded
classes of Problem (region). Already absorbed (the routes-tried index closed-family list for "Dual,
lattice, flat-top, SOS, exterior certificates" and the sign-carrier specification in phase 194 read as
a generalization of Paper 37's diagnosis). No new tool, but a strong confirming precedent; not
reusable as a method, since the sixteen witnesses are all for the Li/(★) object, not S_{T,k}.

**Paper 38 — Li–FIR stability.** PROVED: Cayley-map correspondence between zero location and FIR mode
stability, the no-cancellation theorem for sliding-window sums, and — most concretely — an explicit
two-channel **adjacent-window coercivity inequality** |H_L(z)|² + |H_{L+1}(z)|² ≥ ½|z|^{2L} on the unit
circle, giving a "no blind spot" bank with no gaps across window lengths L, L+1. *This is a genuinely
different sign-producing device from anything in Paper 47*: instead of trying to prove one window
positive, it shows that a *pair of adjacent windows jointly* has a coercivity floor, with an explicit,
elementary trigonometric identity behind it (the exact quartet response 4−4cosh(na_ρ)cos(nθ_ρ)).
Paper 47's T-indexed tower (lamA(T) monotone in T) has an exact analogue of "adjacent windows": the
step from S_{T,k} to S_{T,k+1} as a new contact log(k+1) enters. No one has tried an adjacent-window
(two-T, or two-k) coercivity inequality of the FIR type on S_{T,k}; it is not in the routes-tried index
under any closed family (FIR/Cayley/sliding-window methods do not appear there). Top candidate below.

**Paper 39 — Cofinal Weil quotients.** PROVED: canonical isometries between successive finite
self-adjoint quotients (CCM/Suzuki), an exact two-channel generator-defect formula, a Cauchy-transform
formula for the second-resolvent trace, and fixed-cutoff summability; the global limit reduces to
convergence of a logarithmic curvature to zero, whose branch choice is a signed source estimate
determined by concentration "up to sign only." This fixed-L-to-L+1 **exact transport defect** —
computed in closed form as "two rank-one channels of opposite parity plus a double-operator-integral
correction" — is conceptually the ancestor of Paper 47's Schur-complement passage between S_{T,k} and
S_{T,k+1}, but it was built for the CCM/Suzuki *infinite* operator, not for the finite S_{T,k} matrix of
Paper 47's own finite reduction, and the exact rank-one/double-operator-integral decomposition was never
re-derived for S_{T,k}. Since Paper 47 states "no bound on ‖K‖ uniform in T is proved" for exactly this
kind of inter-window transfer, Paper 39's exact transport-defect formula is a natural, concrete, and
unused candidate technique for computing that transfer explicitly rather than bounding it abstractly.
Flagged in the Top 10.

**Paper 40 — Connes–CCM proof skeleton.** PROVED/CONDITIONAL chain whose named tools — Loewner
monotonicity, Haynsworth additivity, Schur innovations, adaptive Krylov recovery, heat-core exhaustion
— are *already explicitly reused* in Paper 47 (its abstract cites "a Schur and Haynsworth inertia
count"; Theorem-coer-schur is a Schur-complement theorem). So this paper's main machinery is already
carried forward; nothing new here beyond what Paper 47 inherited. The second part's local geometric
data (cyclic root Laplacian, Gamma spin operator, polar plane) is specific to the function-field-style
geometric programme and is in the closed "Function fields, Hodge, Arakelov" family.

**Paper 41 — Obstruction catalogue (Doob coordinate).** PROVED full-kernel Doob–variance identity
reducing positivity to a sharp Poincaré inequality E_K(r) ≥ ½Var_{μ_K}(r); thirty-one-entry catalogue of
no-gos for that inequality (order/TP, transport/martingale, SOS/Hodge-Korn, determinants, finite-head
filtering, spectral detectors, realization rigidity, branch-selection). This Poincaré-inequality
reformulation is a genuinely different target statement from a_T ≥ 0, phrased as a variance bound in a
Doob h-transform coordinate. It has not been checked against S_{T,k} specifically (it targets the
infinite-kernel CCM object), but the "sharp Poincaré inequality" framing is close in spirit to problem
(N)'s "cancellation of exponent ½ ... with sign" requirement. Given the thirty-one already-closed
mechanisms here largely duplicate the routes-tried closed families (order/TP, transport, SOS, Fredholm,
spectral detectors are all explicitly closed in the index), there is no live, un-duplicated technique
for a_T left in this paper.

**Paper 42 — Arithmetic Lefschetz programme over Z.** PROVED various cohomological/combinatorial
lemmas (spherical non-collapse, Künneth separations, gluing) within a four-row Lefschetz programme,
none of the four rows closed; the one numerical fact, the T = log 2 endpoint certificate, is explicitly
retained but is the same classical T ≤ ½log2 regime already superseded by Paper 47's T ≤ ½log5. A
corrective section states which earlier claims are superseded. Closed "Function fields, Hodge,
Arakelov, Deligne, Laumon, F₁, arithmetic site" family. Nothing new for a_T.

---

## Top 10 reusable items for the sign problem (ranked)

1. **Paper 26, `04-papers/26-weil-toeplitz-logistic-criterion/main.tex`** — the Weil–Toeplitz
   C*-algebra / corona symbol apparatus (bounded field over ℕ, ideal J≅c₀, corona W/J, symbol σ(Q),
   Cesàro-vs-norm states; `cor:master-quantifier`, `thm:fat`/`thm:thin`/`thm:strict`). Directly on
   point for the Toeplitz-in-log(m/k) matrix of problem (S); never used in Papers 46–48.
2. **Paper 38, `38-li-fir-stability/main.tex`** — the adjacent-window coercivity inequality
   |H_L|²+|H_{L+1}|² ≥ ½|z|^{2L} and the "no blind spot" bank construction. A concrete model for an
   adjacent-(T,k)-pair coercivity argument on S_{T,k}, S_{T,k+1}, not attempted in Paper 47.
3. **Paper 39, `39-cofinal-weil-summability/main.tex`** — the exact fixed-cutoff transport-defect
   formula (two rank-one channels + double-operator-integral correction) and the Cauchy-transform
   formula for the second-resolvent trace between successive quotients. A candidate exact tool for the
   S_{T,k} → S_{T,k+1} transfer that Paper 47 currently only bounds abstractly (‖K‖ not controlled
   uniformly in T).
4. **Paper 07, `07-localized-weil-detector/main.tex`**, `thm:trunc` — unconditional PNT-only bound
   η(X) ≤ A·exp(−α(log X)²) on the error of truncating the prime sum at X. Usable as an explicit margin
   estimate for passing between contacts in S_{T,k(T)}.
5. **Paper 22, `22-moment-rigidity-criterion/main.tex`** — the Carleman-determinacy moment-rigidity
   argument (triangularity + Carleman's condition + Hardy's theorem) applied to an explicit nonnegative
   measure ν. A genuinely different machine from Schur/SOS/flat-top certificates; untried on the
   measure attached to s_T or to Near_M of problem (S).
6. **Paper 15, `15-finite-to-full-uniformity/main.tex`**, `thm:crit` — criterion for when eventual
   (finite-order) positivity upgrades to uniform (all-order) positivity, via finite-type or
   bounded-threshold hierarchies. Never checked against the T-indexed tower S_{T,k}; could in
   principle show (L2) at increasing T is of bounded-threshold type, bypassing a window-by-window
   argument.
7. **Paper 24, `24-trace-measure-criterion/main.tex`** — the dominance-measure construction
   R(s)=|ζ/ζ_on|²≥1 and its eight equivalent reformulations; structurally parallel to the
   Arch_M − Div_M − Near_M decomposition of (S) (difference of two nonnegative objects, trivial
   nonnegativity, hard part is completeness/correlation). Analogy only, not a ready tool.
8. **Paper 09, `09-stable-arithmetic-fingerprints/main.tex`**, `thm:concave` — concavity and
   extremal-point reduction of a Gram-form bottom eigenvalue over coefficient boxes. Could reduce
   verification of S_{T,k} ≽ 0 over a box of admissible Λ(n) values to finitely many extreme
   configurations, never tried on S_{T,k}.
9. **Paper 35, `35-colligation-route/main.tex`** — unconditional Bakry–Émery curvature bound for the
   *prime part alone* of a Weil generator after Doob conjugation. Narrower than the closed Krein/
   coercivity family; the specific Doob-conjugated curvature bound on a prime-only generator has not
   been attempted on the finite S_{T,k}.
10. **Paper 36, `36-obstruction-ledger/main.tex`**, `thm:mirror-criterion` and the live-H1–H5 node
    machinery — the one place besides Paper 47 using the phrase "window positivity"; worth a direct
    one-round structural comparison against S_{T,k} to confirm no overlap was missed, since Paper 36
    predates Paper 47's restructure and was never cross-checked against it.

## Candidate overlooked results (look stronger than how they were later used)

- **Paper 26's corona/symbol machinery** (see #1): built as an axiomatized-model framework for a
  trichotomy of off-critical zeros, but the underlying C*-algebraic apparatus is a general tool for
  "pointwise-per-window vs. limit-over-windows" statements and was never pointed at the Toeplitz
  matrix of (S), which is exactly the kind of object that machinery was designed to analyze.
- **Paper 38's adjacent-window coercivity inequality**: proved for the Li–Keiper FIR system, but the
  identity behind it (exact quartet response, Cayley-map mode stability) is elementary and
  model-independent; it was never tested on the window family T ↦ S_{T,k(T)} where "adjacent" means
  one more contact or one unit of T.
- **Paper 39's exact transport-defect formula**: derived for the CCM/Suzuki infinite operators as a
  summability device, but it is an *exact* identity (not an estimate), and exact identities relating
  successive finite quotients are precisely what Theorem thm:coer-schur in Paper 47 needs to upgrade
  from a sandwich inequality (λ_S ≤ (1+‖K‖)²λ_A) to a computation.
- **Paper 22's Carleman-determinacy criterion**: proved for a specific archimedean/Meixner–Pollaczek
  measure, but moment-determinacy via Carleman's condition is a general technique for forcing a
  nonnegative measure to equal a reference measure from agreement of moments — never applied to the
  measure naturally attached to s_T(τ)|F̂(τ)|² or to Near_M.
- **Paper 07's PNT-only truncation bound**: a clean, fully unconditional, non-circular estimate that
  seems to have been superseded in later papers by ad hoc window-specific truncations rather than
  cited and reused as a general-purpose tool.

## Note on the routes-tried index

The following items above sit inside the explicitly **closed** families of
`05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` and are not proposed for retry: Papers 08, 11, 12
(as a lever), 13, 17, 18, 19 (Hypothesis-D-conditional parts), 23 (determinacy as closed via CCM
chain), 25, 27 (as a route), 28, 30, 32, 34, 40 (geometric part), 41 (as a catalogue of closed
mechanisms), 42. Items 1–10 above are either (a) not named in any closed family in that index (Papers
26, 38, 39's exact-transport device, 07's truncation bound, 22's Carleman device, 15's uniformity
criterion), or (b) narrower instances of a closed family applied to an object (the finite S_{T,k}, or
the window tower) that the closed entry does not cover (Paper 35's prime-only curvature bound, Paper
9's box-concavity reduction). No item here re-proposes a route already marked DEAD / NO-GO / FALSIFIED
/ CIRCULAR / REF-D for the *same* object; where a technique's parent family is closed, the specific
application to S_{T,k} or to problem (S)'s Toeplitz matrix is noted as the stated new reason it has not
already failed.
