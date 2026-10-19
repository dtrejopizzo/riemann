# Doc 119 — The forced axioms: backward derivation of the requirements of the sought cohomology

**Program:** Riemann Hypothesis — Phase 39, G1↔G2 interface
**Prerequisites:** roadmap-rh (nodes G1–G4, routes A/B, specification S1–S3, Thm. rank-sensitivity, Milestone ms:spec); P44 (conditional dichotomy, Problem L8, anti-Siegel); Doc 110 (axioms L1–L6 of the inertia reader; Theorem 4.3 of impossibility in ℱ; Prop. 4.5 finite rank ⟹ Newton; §5.2 measurement of CC against L1–L6); Doc 118 (moment rigidity: Carleman + Hardy; Theorem 5.3; the model of "what rigidity does close"); Doc 108 (value vs inertia; binarity per window); Doc 105 (Thm. 5.5: Mertens divergence of the ledger; boundary of the Weil class); Doc 100 (archimedean positivity; exhaustion lemma); Doc 99 (semilocal forms QW_λ, automatic locality); Doc 72 (Weil's ledger); P43 (master quantifier); P35 (κ(Q)=2m).

**Absolute rule of this phase (labeling discipline):** every statement carries ONE of three labels. **[REQUIREMENT]** = a property that the sought cohomology MUST have, with the derivation of why it is forced. **[CONJECTURE]** = something we believe but do not derive. **[DATUM]** = a proved fact (from the analytic side of the program, with a backward-only internal citation, or from verifiable real literature). "Proved" is NEVER written about anything new on the geometric side. What is unverified in the literature is marked [UNVERIFIED]. No numerics.

---

## 0. Executive summary

This document derives, **from the conclusion toward the construction** (G4 → G3 → G2 → G1),
the minimal list of axioms that a cohomological theory $H$ on (the square of)
$\mathrm{Spec}\,\mathbb{Z}$ must satisfy for the roadmap to run. The method is that of the
reverse engineer: at each node one asks *exactly what fails without the axiom*, and the
answer is anchored to a theorem already proved on the analytic side of the program. The list:

| axiom | one line |
|---|---|
| **R-SIG** | $H$ carries a weight grading with an associated integer signature; without it, "finiteness" cannot even be stated (§2.3) |
| **R-FIN** | the *impure*-weight part of $H^1$ has dimension finite and bounded a priori by data of the site, and that dimension bounds $\kappa(Q)=2m$ (§2.2, §2.5) |
| **R-LEF** | a flow $F$ on $H$ whose distributional trace reproduces term by term the explicit formula: pole (R-LEF-POLE), primes as orbits of length $\log p$ (R-LEF-PRIMES), archimedean regularization (R-LEF-REG) (§3) |
| **R-WEIGHT** | the weight invariant of each class is computable from $H$, not from the position of the zero; "weights $=1/2$" must FOLLOW from a geometric positivity (§4) |
| **R-NC** | non-circularity test in four clauses (NC1–NC4): the central contribution of the document; it makes any candidate weight structure falsifiable (§4.3) |
| **R-TR** | traces are evaluable against a test class with strict margin $\varepsilon$ inside the Weil class, and the Newton reconstruction requires R-FIN *beforehand* (§5) |

**Derived order of dependencies (main finding of the backward method):**
$$\text{R-SIG} \;\prec\; \text{R-FIN} \;\prec\; \text{R-LEF} \;\prec\; \text{R-TR},
\qquad \text{with R-WEIGHT/R-NC transverse to R-SIG.}$$
Finiteness (G4) **presupposes** the weight structure (G2): one cannot state "the impure
part is finite-dimensional" without having defined "impure". This confirms from the
geometric side the order of the roadmap (wall G2 is *upstream* of finiteness) and explains
why thirty-seven phases of "purity without finiteness" and "finiteness without weights" both
failed.

**Tensions detected (§6.3):** T1 (finiteness vs continuous flow: a finite-matrix trace
is real-analytic and cannot have its singular support on $\{\log p^k\}$ — finiteness
CANNOT be of all of $H^1$); T2 (archimedean regularization vs signature: signatures are
not continuous under the limits that regularization requires); T3 (arithmetic access vs
non-circularity: the more explicit the trace formula, the greater the risk that the
"geometry" is the explicit formula repackaged); T4 (flow $\mathbb{R}_+^*$ vs weight
integrality: in char $p$ weight quantization is free, here it is an extra axiom with no
analogue).

---

## 1. Method: backward derivation

**[DATUM]** The roadmap (roadmap-rh, §6–§7) establishes the chain
G1 (finite-dimensional cohomology on the square of the site) → G2 (weight/signature
structure) → G3 (Lefschetz = explicit formula) → G4 (a priori bound
$\kappa(Q)=2m<\infty$) → Finiteness → {Route A: dichotomy proved in P44, Thm. 2.2 / Route B:
Newton reading}. The specification S1–S3 (roadmap, Milestone ms:spec) fixes what the
geometry must deliver: S1 finiteness of a *signature* (not of an Euler characteristic),
S2 arithmetic access to the traces, S3 no finite-to-full-limit debt.

The backward derivation inverts the reading: one starts from what G4 must produce
(an a priori bounded integer $\kappa(Q)=2m$ — [DATUM] P35: $\kappa(Q)=2m$ in the Pontryagin
space) and asks, node by node, what structure on $H$ is *forced* — that is, what
already-proved theorem of the program shows that its negation makes the node fail. The
criterion for "forced" is strict: an axiom enters as [REQUIREMENT] only if there exists a
[DATUM] (theorem of the program or of the literature) documenting the failure mode without it.
What is believed necessary but not derived remains as [CONJECTURE].

**Convention on the object.** We write $H=\bigoplus_i H^i$ for the sought theory
on the square of the site (the analogue of $H^\bullet(C\times C)$), without presupposing its
category (vector spaces, modules over $\mathbb{R}_{\max}$, Hilbert spaces
with an indefinite form). The axioms are formulated agnostically with respect to the
category; when a concrete realization demands more, it is said.

---

## 2. FROM G4: the finiteness requirements

### 2.1. What G4 must produce

G4 must deliver: **$\kappa(Q)=2m<\infty$, a priori** — before localizing any zero,
with no finite→full limit (S3). Three data points of the program fix the exact profile of what
"a priori" means:

**[DATUM]** (roadmap, Thm. rank-sensitivity; Doc 110, Prop. 4.5). In a finite rank
*known a priori* $n$, the inertia $(p,q)$ of a Hermitian form $Q$ is determined
by the $n$ power traces $\mathrm{tr}(Q^j)$, $j=1,\dots,n$ (Newton identities
+ Jacobi–Frobenius via Hankel forms; [Gan59, Vol. 2, Ch. X]). In infinite rank the
traces do not determine the signature: the number of negative eigenvalues is not a
continuous function of the traces.

**[DATUM]** (Doc 110, Theorem 4.3). In the class ℱ of arithmetic quadratic functionals
with test-accessible compressions, the axioms (L2 value autonomy) + (L3 inertia
detection) + (L4 stability without an RH toll) are inconsistent: every sub-resolution index is
0 unconditionally (it does not detect), and every resolution index either pays an RH toll or
uses the positions of the zeros. *Status declared there: theorem for the realizations of
the program, scheme for the axiomatic class.*

**[DATUM]** (P44, §3; roadmap, anti-Siegel Obs.). There is no Siegel-type repulsion
mechanism for off-critical quadruples: the costs of two quadruples *add up* in every
counting functional of the program (excluding $m=2$ is harder than excluding $m=1$), and the
local archimedean budget grows like $\log\gamma$. Finiteness will not come from analysis.

### 2.2. R-FIN-1, naive version, and why it is insufficient as such

**[REQUIREMENT] R-FIN-1 (crude form).** $H$ must assign to the "surface" (the square
of the site) an object whose dimension/characteristic bounds $\kappa(Q)$:
$$\kappa(Q) \;\leq\; C\cdot\dim(\text{something of } H), \qquad C \text{ absolute},$$
with the "something" computable functorially from the site, with no input from zero
positions.

*Derivation of why it is forced:* without an a priori rank bound, Prop. 4.5 of
Doc 110 does not apply and Theorem 4.3 of Doc 110 does: any attempt to read
$\kappa(Q)$ from arithmetic quadratic functionals in infinite rank falls into the
sub-resolution/resolution dichotomy. **[DATUM]** (Doc 110, Obs. 5.3) Form B of
the program was exactly "Deligne's method minus finiteness" and died for that reason: the
tensor amplification $\kappa(\psi^{\otimes k})=\tfrac12(4m)^k$ does not gain in infinite
rank because the comparison denominator (the sea on×on) grows at the same rate;
in Deligne it gains because $\dim H^i$ is pinned down.

But R-FIN-1 as such does NOT suffice:

**[DATUM]** (Doc 110, §5.2, row L6; roadmap, S1). An Euler characteristic — a
*difference of dimensions*, a VALUE — does not determine signatures in infinite rank; the
tropical Riemann–Roch of Connes–Consani already produces integer Euler characteristics
([CC-Scaling 2016/2017], verified in Docs 99/100) and that does not bring one any closer to $m$:
no invariant of the site has been connected to $\kappa(Q)$. The real requirement is one of
*signature*.

**[DATUM]** (Doc 108, §7.4, cited via Doc 110 §4.2). Value autonomy ≠ autonomy of
inertia: the arithmetic side computes the total of the window, not the partition into
on/off blocks. The bound needed is of the *off* part — and "off" is a weight attribute.

### 2.3. R-SIG: the signature requires a weight grading — and finiteness is that of a graded piece

**[REQUIREMENT] R-SIG.** $H$ carries a grading (or at least a finite filtration)
$$H^i \;=\; \bigoplus_{w} \mathrm{gr}^W_w H^i \qquad \text{(or } W_\bullet H^i \text{ filtration)},$$
stable under the dynamics of G3, together with an additional structure that assigns to each
graded piece an **integer signature** — not merely a dimension. The finiteness of R-FIN is that
of the *relevant* graded piece, not of $H$ total (§2.5).

*Derivation of why it is forced, precisely:* the final object is $\kappa(Q)$, a negative
index — a datum of *inertia*. A dimension is a cardinal; an inertia is a cardinal
**with a sign**. For an invariant of $H$ to bound an inertia, $H$ must possess
the minimal structure that produces signs. There are exactly three classical realizations of
"structure that produces a signature", and it is worth comparing them because they demand
different things:

**(i) A bilinear/Hermitian form with an involution.** Data: a pairing
$\langle\cdot,\cdot\rangle: H^i\times H^{2d-i}\to H^{2d}(\cong \text{trivial object})$
(Poincaré duality) plus an involution (an analogue of the star operator or of
conjugation) turning it into a Hermitian form on $H^i$. The signature is that of
the pair $(H^i,\langle\cdot,\cdot\rangle)$. *Requires:* Poincaré duality on $H$ (fundamental
cohomology class of the surface), non-degeneracy, and — for the signature to be
stable — finite dimension of the support of the indefinite part. It is the realization closest
to the analytic side: **[DATUM]** (P35) the Weil form $Q$ already lives in a Pontryagin
space $(K,Q)$ with $\kappa(Q)=2m$; the requirement is that $H$ reproduce that pair
functorially.

**(ii) A Hodge $(p,q)$ bigrading with symmetry.** Data: $H^i\otimes\mathbb{C}
=\bigoplus_{p+q=i}H^{p,q}$ with $\overline{H^{p,q}}=H^{q,p}$. The signature comes from the
Hodge–Riemann bilinear relations: the form $\langle x,\Lambda$-primitive$\rangle$
is definite on each piece $(p,q)$ with explicit sign $i^{p-q}(-1)^{\dots}$. *Requires:*
a theory of Lefschetz classes (hyperplane-section operator $L$, primitivity —
i.e., a polarization), in addition to the bigrading. It is the structure of the Hodge
index: positivity comes from the geometry of the polarization. **[DATUM]** (literature)
in the case of surfaces over finite fields, the Castelnuovo–Severi inequality
(Hodge index in the Néron–Severi group of $C\times C$) is what Weil used
[Wei48; Mattuck–Tate 1958, Abh. Math. Sem. Univ. Hamburg 22, 295–299; Grothendieck,
*Sur une note de Mattuck–Tate*, J. reine angew. Math. 200 (1958), 208–215].

**(iii) A Frobenius action with absolute values.** Data: an endomorphism $F$
whose eigenvalues $\alpha$ on $H^i$ have a well-defined $|\alpha|$ (Weil numbers);
the "weight" of $\alpha$ is $w=2\log_q|\alpha|$. The signature/partition comes from the
spectrum: pure of weight $i$ = all $|\alpha|=q^{i/2}$. *Requires:* the eigenvalues to be
algebraic numbers with absolute values independent of the embedding (integrality + the
weight product in tensor products), and finiteness of $\dim H^i$ so that the spectrum is
discrete and the partition makes sense. **[DATUM]** (literature) this is Deligne's
realization [Del74, *La conjecture de Weil. I*, Publ. Math. IHÉS 43, 273–307; Weil II:
Publ. Math. IHÉS 52 (1980), 137–252]; the consistency between distinct Weil
cohomologies is given by [Katz–Messing, Invent. Math. 23 (1974), 73–77].

**Comparison and common minimum.** The three realizations share a core: *a
decomposition of $H$ stable under the dynamics, indexed by a real invariant $w$, such
that (a) $w$ is additive under tensor products, (b) Poincaré duality pairs $w$
with $2d-w$ (weight symmetry), and (c) there is an internal criterion — form, polarization or
absolute value — deciding whether a class belongs to its piece without external input.*
That core is the **minimal version of R-SIG**. The comfortable version is (ii)+(iii)
simultaneously: a polarized bigrading with compatible Frobenius (the situation of the
standard conjectures [Gro69, *Standard conjectures on algebraic cycles*, Bombay 1968;
Ser60, *Analogues kählériens…*, Ann. of Math. 71, 392–394]).

**On what each demands on the arithmetic site** — where the "Frobenius" is a flow
$\mathbb{R}_+^*$ (Doc 110, §5.1): in (iii) the "eigenvalues" are those of the *generator*
of the flow, and the natural weight is $w=2\,\mathrm{Re}(\text{generator eigenvalue})$;
nothing quantizes it to integers (tension T4, §6.3). In (i) and (ii) weight integrality
comes from the grading itself, not from the dynamics: that is why **the minimal version of R-SIG
for $\mathrm{Spec}\,\mathbb{Z}$ must take the grading (not the flow spectrum)
as the primitive datum**, with the flow acting *inside* each graded piece. This is a
derived [REQUIREMENT]: if weight were *defined* as the real part of the spectrum of the
generator, the weight of the class associated with a zero $\rho$ would be $2\beta$ — the position
of the zero — and R-WEIGHT(a) (§4.1) would be violated by immediate circularity.

### 2.4. Finiteness of $\dim H$ total, or of a graded piece?

Here the backward derivation produces its most important correction to the template's
intuition.

**[DATUM]** (classical; [Tit86, §9.4]) $\zeta$ has infinitely many non-trivial zeros
($N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi e}$). **[DATUM]** (literature) in every
known spectral realization of the zeros — Connes's on the adele class
space [Connes, *Trace formula in noncommutative geometry and the zeros of the
Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106] and Meyer's version
[Meyer, Duke Math. J. 127 (2005), 519–595] [UNVERIFIED the exact editorial datum of
Meyer] — the space carrying the zeros is infinite-dimensional.

Forced consequence: **the analogue of $H^1$ for $\mathrm{Spec}\,\mathbb{Z}$ CANNOT
be finite-dimensional.** In the function-field template, $\dim H^1=2g$ is finite
because the curve has finitely many zeros; here the "zero side" is infinite. The
"$\dim H^1=2g$" analogy of the roadmap must be read, with this precision, thus:

**[REQUIREMENT] R-FIN (definitive form).** With the grading of R-SIG in hand:
$$\dim\Bigl(\bigoplus_{w\neq 1}\mathrm{gr}^W_w H^1\Bigr) \;<\;\infty,
\qquad\text{bounded a priori by data of the site},$$
and the bound bounds $\kappa(Q)$: each impure class contributes a countable
negative direction. That is: **finiteness of the IMPURE (weight $\neq 1$) part of $H^1$, not of $H^1$
total.** The pure part (weight 1) may — must — be infinite-dimensional: it carries
the infinitely many critical zeros.

*Derivation:* (α) the infinitude of zeros makes $\dim H^1<\infty$ impossible (above);
(β) what $\kappa(Q)=2m$ counts is exactly the off-critical quadruples
([DATUM] P35), i.e., the classes a weight structure would mark as impure;
(γ) the Newton machinery (Doc 110, Prop. 4.5) only needs finite rank of the *indefinite
block*: the inertia of a form with an infinite-dimensional positive part and a
negative part of known rank $\leq N$ is determined by finitely many *relative*
traces — traces of the compressed block, not of the total. Total finiteness is not only
impossible: it is unnecessary.

**Remark (structural consequence).** R-FIN, in its definitive form, **is not
statable without R-SIG**: "impure part" presupposes "weight". The order of dependencies is
$$\text{R-SIG} \;\prec\; \text{R-FIN}.$$
This is notable because it reverses the template's pedagogy (in char $p$ one learns
"finiteness first, purity after") while simultaneously confirming it at a deep level: in
char $p$ the finiteness of $\dim H^1$ is statable without weights *because the pure part is
also finite*; over $\mathrm{Spec}\,\mathbb{Z}$ that luxury does not exist. Wall G2 (the
weight structure) is upstream of EVERYTHING, including the very formulation of
finiteness. The roadmap already placed G2 before G4 in the chain; this derivation shows
that the placement is not optional.

**[CONJECTURE]** The correct realization of "finite impure part" is: the Pontryagin pair
$(K,Q)$ of P35 is the analytic realization of
$(\mathrm{gr}^W H^1, \text{duality form})$, with the $2m$ negative vectors of $Q$
corresponding to a basis of $\bigoplus_{w\neq1}\mathrm{gr}^W_w H^1$. We believe this
(it is the natural reading of the bridge P35 + Phase 26), but we do not derive it: nothing forces
the *only* source of negative directions to be impure classes of $H^1$ (anomalous
$H^0/H^2$ could contribute). It remains an interface conjecture.

### 2.5. Minimal vs comfortable version of R-FIN

- **Minimal:** there exists a finite-dimensional subquotient $V\subset H^1$, functorially
  defined (without zero positions), such that (a) every impure class falls into $V$, and
  (b) $\dim V$ is computable from data of the site. Knowing $\dim V$ exactly is not
  required: an effective bound $\dim V\leq N_0$ suffices (S3 requires that $N_0$ not come
  from a finite→full limit).
- **Comfortable:** an exact weight sequence $0\to W_{<1}H^1\to H^1\to \mathrm{gr}^W_{\geq1}\to0$
  with $W_{\text{impure}}$ of *computed* finite dimension (the analogue of $2g$), plus
  semisimplicity of the flow action on the graded piece.
- **Fire test:** a candidate $H$ satisfies R-FIN if and only if it produces an integer
  $N_0$ by a site computation (degrees of tropical divisors, Euler
  characteristic of a concrete sheaf, etc.) ACCOMPANIED by a theorem "every negative direction of
  $Q$ comes from $V$" whose proof does not mention zeros. If the "accompaniment" is missing, one
  has just another Euler characteristic — the current state of CC ([DATUM] Doc 110, §5.2).

---

## 3. FROM G3: the requirements of the trace formula

### 3.1. R-LEF: the global statement

**[REQUIREMENT] R-LEF.** There exists a dynamics $F$ on $H$ — endomorphism, correspondence,
or one-parameter flow — such that an alternating sum of traces reproduces EXACTLY the
arithmetic side of Weil's explicit formula. In flow form (the relevant one for
the site, §3.4), for every test function $h$ in the admissible class (§5.1):
$$\sum_{i}(-1)^i\,\mathrm{Tr}\Bigl(\int_0^\infty h(u)\,F_u^*\big|_{H^i}\,d^*u\Bigr)
\;=\; \widehat h(\tfrac{i}{2})+\widehat h(-\tfrac{i}{2})
\;-\;\sum_p\sum_{k\geq1}\frac{\log p}{p^{k/2}}\,h(p^k)
\;-\;(\text{archimedean term}),$$
with the traces on the left-hand side understood distributionally, and the right-hand side
being that of the explicit formula in the program's normalization ([DATUM] Doc 72, Thm. 4.1:
$T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)+$ archim., with the
status corrected by Doc 105, §3.3 below).

*Derivation of why it is forced:* G4 needs to read $\kappa(Q)$ from arithmetically
autonomous traces (S2). **[DATUM]** (roadmap, Thm. rank-sensitivity, "Why this is
the whole point") the autonomous arithmetic data fix the VALUES of the functionals of
the explicit formula; if the traces of $F$ on $H$ do not EXACTLY match those
values, the traces of $H$ are not autonomous and axiom L2 of the inertia reader
(Doc 110, Def. 4.1) fails: the invariant would stop being computable without zeros. Exactness
is not an aesthetic matter: an identity "up to an error term" reintroduces a
finite→full limit and violates S3 ([DATUM] roadmap: every uniform limit of that type in the
analytic category is RH-equivalent; Doc 99, transmutation E4, cited via Doc 105 §7).

We break down term by term what part of $H$ must produce each block.

### 3.2. R-LEF-POLE: the pole term and the trivial $H^0/H^2$

On curves over $\mathbb{F}_q$, the Lefschetz formula gives
$\#C(\mathbb{F}_{q^k}) = q^k - \sum\alpha_i^k + 1$: the terms $q^k$ and $1$ come from
$H^2$ and $H^0$ (weights 2 and 0, one-dimensional), and are the exact analogue of the pole
term $\widehat h(\pm i/2)$ of the explicit formula (the pole of $\zeta$ at $s=1$ and the
"pole" at $s=0$ of the completion).

**[REQUIREMENT] R-LEF-POLE.** $H^0$ and $H^2$ (of the curve-object; their analogues on the
square) are of rank ONE, pure of weights $0$ and $2$, and the flow acts on them with the
trivial characters: trivial on $H^0$, the scaling (modulus) character on $H^2$. Their
contribution to the trace must be exactly $\widehat h(-i/2)+\widehat h(i/2)$.

*Derivation:* the arithmetic side of the explicit formula contains these two terms
unconditionally ([DATUM] Weil 1952; Doc 72); if $H^0/H^2$ did not produce them, the
difference would have to come from $H^1$, i.e., from the zeros — but then the spectral
side would contain terms without an associated zero, and the identification "classes of
$H^1\leftrightarrow$ zeros" (needed for $\kappa$ to count quadruples, §2.4) would
break down. *Minimal version:* two distinguished characters in the trace, with the correct
normalization. *Analogue in function fields:* $q^k+1$; there the one-dimensionality of
$H^0,H^2$ is a theorem (connectedness + duality). *Fire test:* compute the trace of the
flow on the candidates for $H^0,H^2$ of the site and compare with $\widehat h(\pm i/2)$ —
a finite computation, without zeros. **[DATUM]** (Doc 100, §4, via CC Selecta 27 (2021)): the
archimedean + polar term of Weil's formula already has a positive operator
realization on support $(1/2,2)$; it is the only block where candidate CC has already passed a
partial fire test.

### 3.3. R-LEF-PRIMES: local traces and the warning of divergence

The prime term is a sum over finite places. The local structure in char $p$ is: for
each closed point $x$, the local Frobenius contributes $\deg(x)$ when
$k\equiv0\ (\mathrm{mod}\deg x)$. The local decomposition of the explicit formula is the
analogue: a distribution per place (Weil's $W_p$), and the global one is their sum.

**[REQUIREMENT] R-LEF-PRIMES.** For each prime $p$ there exists a local structure in $H$
(a "Frobenius at $p$": the local monodromy of the flow on the corresponding orbit, or the
fiber of the correspondence over the point $p$ of the site) whose local trace reproduces the
Weil distribution $W_p$: $f\mapsto(\log p)\sum_{k\geq1}p^{-k/2}f(p^k)$ (plus the
inversion term $f(p^{-k})$ according to normalization). And — the non-negotiable part —
**the global sum of local traces must converge in the same regularized sense in which
the explicit formula converges, not term by term in absolute value.**

**[DATUM]** (Doc 105, Theorem 5.5 + Obs. 5.6). In the program's naive normalization
(test function $h_{\lambda_0}=W_{\lambda_0}w$, exactly at the boundary of the Weil
class: analytic only for $|\mathrm{Im}\,s|<1/2$, Fourier decay exactly
$e^{-r/2}$), the sum of primes **diverges marginally** like
$\tfrac{5\sqrt2}{8}\log X$ (Mertens-type): the decomposition
$T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ of Doc 72 is
*strictly formal* and requires pairing with the divergent archimedean block
BEFORE summing. **[DATUM]** (Doc 99, Lemma 5.1, cited via Doc 105): the prime
tail $\sum_{p\leq\lambda}\log p/\sqrt p\gtrsim\sqrt\lambda$ for the tent function — same
phenomenon, a different test.

**[REQUIREMENT] R-LEF-REG (archimedean regularization).** The archimedean term of the
trace is not just another summand: it is the **regularizing counterweight** of the prime
block. Theory $H$ must realize the archimedean place as a local contribution of the same type
as the $p$-adic ones (the orbit "of infinitesimal length" / the point at infinity of the
site), with the trace identity holding only for the joint pairing. *Minimal
version:* the identity R-LEF is stated for the total regularized sum (Weil's principal
value at the archimedean place, [DATUM] Weil 1952; Doc 100 §5: additivity over places of
the geometric side is unconditional). *Comfortable version:* each place produces a
well-defined local distribution and the sum converges in the topology of the test class
of §5.1 with margin $\varepsilon$. *What fails without it:* [DATUM] Doc 105 — the
"per-prime increments" are not increments of any convergent quantity; any
term-by-term reading (monotonicity, signs per step) is illegitimate (the sign test of
Form A failed exactly in this way).

*Analogue in function fields:* THERE IS NO analogue of this difficulty — the sum over
closed points of bounded degree is finite for each $k$. Archimedean regularization
is a genuinely new requirement of $\mathrm{Spec}\,\mathbb{Z}$, and feeds
tension T2 (§6.3).

### 3.4. R-LEF-FLOW: endomorphism or semigroup? What changes with the continuous flow

In char $p$, $F$ is a genuine endomorphism and the Lefschetz variable is $k\in\mathbb{N}$
(iterates). On the arithmetic/scaling site, **[DATUM]** (Doc 110, §5.1; CC 2014/2016,
verified there) the "Frobenius" is the scaling flow: an action of
$\mathbb{R}_+^*$, not of $\mathbb{Z}$. The derivation of what changes:

1. **The sum over $k$ becomes a time integral.** Instead of
   $\sum_k h_k\,\mathrm{tr}(F^k)$ one evaluates
   $\mathrm{Tr}\bigl(\int h(u)F_u\,d^*u\bigr)$ against tests $h$ on the group
   $\mathbb{R}_+^*$: the trace formula is a distribution identity over
   time, not a sequence of numbers. Consequence for Route B: "finitely many traces"
   means "traces against finitely many tests" (§5.2).

2. **Fixed points become periodic orbits of length $\log p$.** The count of
   fixed points of $F^k$ is replaced by the sum over periodic orbits of the flow, each
   prime $p$ contributing the orbit of period $\log p$ (and its multiples $k\log p$), with
   the contribution weighted by a $1/|1-p^{k}|$-type factor (the transverse determinant). **[DATUM]**
   (literature) this is exactly Guillemin's distributional trace for flows
   [V. Guillemin, *Lectures on the spectral theory of elliptic operators*, Duke Math. J.
   44 (1977), 485–517], and its arithmetic instance is Connes's theorem: the
   distributional trace of the scaling flow on the adele class space reproduces the
   arithmetic side of Weil's explicit formula, with the periodic orbits of length
   $\log p$ [Connes, Selecta Math. (N.S.) 5 (1999), 29–106]. Deninger's program
   formulates the same desideratum in the language of foliated dynamical
   systems [Deninger, *Some analogies between number theory and dynamical systems on
   foliated spaces*, Doc. Math., Extra Vol. ICM I (1998), 163–186].

3. **The spectral side changes from "eigenvalues of $F$" to "spectrum of the generator".**
   For an endomorphism, the zeros appear as eigenvalues $\alpha$ with $|\alpha|=q^{1/2}$;
   for a flow, they appear as eigenvalues $\rho$ of the infinitesimal generator
   (the spectral side is $\sum_\rho \widehat h(\rho)$ on the line/critical strip). The
   purity condition "$|\alpha|=q^{w/2}$" translates to
   "$\mathrm{Re}(\rho)=w/2$" — which is literally the position of the zero. **Forced
   consequence (feeds R-WEIGHT):** with a continuous flow, purity CANNOT be defined
   spectrally without circularity; it must be defined via the grading (§2.3) and then
   PROVED that the spectrum of the generator on $\mathrm{gr}^W_w$ has real part $w/2$.
   In char $p$ both definitions coincide trivially; here separating them is mandatory.

4. **There are no tensor powers of time.** Deligne's trick uses $F$ acting on
   tensor powers with multiplicative weights ($\alpha^{\otimes k}$, weight $kw$). For
   a flow, the analogue exists (the product flow on $H^{\otimes k}$) and the weights of
   R-SIG must be additive under $\otimes$ (common core of §2.3, clause (a)) for the
   amplification to make sense. **[DATUM]** (Doc 106, tensor identity, cited via
   Doc 110 Obs. 5.3): the program already verified that tensor amplification is
   *formally* transplantable; what was missing was finiteness — consistent with the
   order R-SIG ≺ R-FIN ≺ amplification.

**[REQUIREMENT] R-LEF-FLOW (synthesis).** A flow (continuous semigroup) suffices; a
discrete endomorphism is not required. But then the theory must include: (a) a Guillemin-type
distributional trace as the *definition* of the trace side; (b) the weight grading as a
datum independent of the spectrum of the generator; (c) tensor compatibility of weights. *Comfortable
version:* an auxiliary discrete endomorphism (an "integer Frobenius" — e.g., the action of
each $p\in\mathbb{N}^\times$ separately, which exists on the arithmetic site: the
monoid $\mathbb{N}^{\times}$ acts; [DATUM] CC 2014, verified in Doc 110 §5.1) whose
discrete iterates refine the flow. *Fire test:* the trace identity must be a theorem
for candidate $H$ with BOTH sides computed independently — the left from
the geometry of $H$, the right from Weil — and not a definition of the left side as
"whatever gives the right side" (if it is a definition, G3 is vacuous and the whole burden
passes to G2 with no gain).

---

## 4. FROM G2: the central requirement R-WEIGHT and the non-circularity test

### 4.1. R-WEIGHT(a): the invariant must be computed from $H$, not from $\rho$

**[REQUIREMENT] R-WEIGHT(a).** The weight structure assigns to each class
$c_\rho\in H^1$ (the class associated with a zero $\rho$ via R-LEF) an invariant
$w(c_\rho)\in\mathbb{Z}$ (or $\tfrac12\mathbb{Z}$, depending on normalization) **computable from
the internal structure of $H$** — membership in a graded piece, sign under the duality
form, degree of an algebraic class intersecting it — and NOT from the position of $\rho$.

*Derivation of why it is forced:* if $w(c_\rho)$ were defined as $2\,\mathrm{Re}(\rho)$
(the only definition available without new structure), then "all weights are 1"
would *literally* be RH, restated: zero new content. **[DATUM]** (Doc 108, §7.4,
via Doc 110): the on/off partition is not test-accessible — every arithmetic quadratic
functional computing it uses positions. **[DATUM]** (Doc 110, Theorem 4.3(b)): in
the resolution regime, either the invariant pays an RH toll or it uses positions. R-WEIGHT(a) is
exactly the requirement to leave class ℱ: the invariant must live in a
category where membership in a graded piece is decidable by geometry
(functoriality, algebraic classes, intersection forms), which is what ℱ lacks.

### 4.2. R-WEIGHT(b): "weights = 1/2" must follow from a geometric positivity

**[REQUIREMENT] R-WEIGHT(b).** The purity statement — every class of $H^1$ associated with
a zero has weight 1 (equivalently, the spectrum of the generator has real part $1/2$;
normalization: weight $w$ ⟺ real part $w/2$) — must be a THEOREM whose proof uses a
geometric property of $H$, of one of the two types with precedent:

- **(b-i) Positivity of an intersection form (via Hodge index / Castelnuovo).**
  An inequality on classes in the square — for every correspondence
  $Z\subset X\times X$, a bound of type $\sigma(Z\cdot Z')\leq$ terms of degrees — from
  which the weight bound follows by Weil's argument applied to the graph
  correspondence of the flow. **[DATUM]** (literature) Weil 1948 [Wei48]; the modern
  form: Castelnuovo positivity in $\mathrm{NS}(C\times C)$.
- **(b-ii) Purity by tensor amplification (via Deligne/Rankin).** A crude one-sided bound
  on even tensor powers + uniform finiteness of the rank ⟹ a fine bound upon
  extracting $2k$-th roots. **[DATUM]** (Del74). **[DATUM]** (Doc 110, Obs. 5.3): the
  mechanism requires R-FIN as a prior input — a pinned-down denominator — and the program already
  confirmed firsthand (Form B) that without R-FIN the result is reversed.

*Derivation of why "inserting it by hand" is forbidden:* if purity is postulated as
an axiom of $H$ (instead of a theorem), then the chain G1→G4 proves "RH assuming a
structure whose existence implies RH": the content evaporates. The theorem/axiom
distinction here is exactly the distinction between the standard conjectures (which in
char $p$ remain open but purity was proved by another route, (b-ii)) and purity
itself. **[DATUM]** (P43, master quantifier, cited via P44 §1 and Doc 110 §1): every
property verifiable without zero positions that implies weights $=1/2$ must come from a
structure EXTERNAL to $\zeta$; the full inventory of internal properties (analytic,
spectral, combinatorial) has been catalogued and none crosses.

### 4.3. R-NC: the non-circularity test (the central contribution of this document)

The above is distilled into an operational test. Any future proposal of a weight
structure $(H,W,F,\langle\cdot,\cdot\rangle)$ for the site must be submitted to the four
clauses; failing any one disqualifies it as crossing the wall (it may still be
valuable mathematics — but it is not G2).

**[REQUIREMENT] R-NC (non-circularity test).** Let $P$ be the geometric property from
which purity is to be deduced (the positivity of (b-i), or the crude bound + finiteness of
(b-ii)). The test:

> **NC1 (externality of the definition).** The definition of $W$ and of $P$ does not mention
> $\zeta$, its zeros, nor any function/measure/operator whose spectrum or singular support
> encodes the positions of the zeros. Mentioning primes, adeles, the site and
> its sheaves is allowed. *Concrete discriminator:* substitute, in the definition, the
> explicit formula with that of an arbitrary $L$-function of the same type (or with that of the
> counterexamples without Euler product of P44 §2.3 — [DATUM] Doc 111, Prop. 2.2: every
> finite $m$ is realizable in the order-1 class with a functional equation). If the
> definition of $W$ does not survive the substitution (it cannot be formulated), it is internal to
> $\zeta$: FAILS.
>
> **NC2 (overgeneration).** $P$ is proved for a class of objects of the site
> STRICTLY larger than the one encoding $\zeta$ — all correspondences, all
> divisors, all sheaves of a category — by a uniform method (deformation, specialization,
> geometric induction). *Model:* Castelnuovo holds for EVERY divisor of
> $C\times C$, not only for the graph of Frobenius; the inequality is a theorem of
> surfaces that ignores which curve it is. If $P$ is verifiable only for the specific
> object encoding $\zeta$ (the graph correspondence of the flow), then
> $P$ is a statement about $\zeta$ in disguise: FAILS.
>
> **NC3 (no reduction to catalogued RH-equivalent positivities).** The verification of
> $P$ in any truncation/degeneration must not be logically equivalent to an
> item of the program's catalogue of RH-equivalent positivities: global Weil
> positivity (MW-1), its semilocal uniformization $\lim\mu_\lambda\geq0$ (MW-6; [DATUM]
> Doc 99 §2.2 via Doc 110 §3), constancy of $\Delta_n$ for all $n$ ([DATUM] Doc 118,
> Thm. 5.6 — exact RH-equivalent), $T_\lambda=0\ \forall\lambda$, uniform index bound
> per window ([DATUM] Doc 108, Prop. 2.5 via Doc 110 Thm. 4.3(b)). *Operative:*
> the proponent must exhibit the chain $P\Rightarrow$ purity and verify that no
> intermediate link appears on the NO-GO-LIST (MW-1…MW-7) nor is inter-derivable with one
> that appears, via the equivalences already proved by the program. If $P$, restricted to the
> object encoding $\zeta$, IS one of those positivities, the wall was not
> crossed: it was renamed. FAILS.
>
> **NC4 (two-worlds test).** In the $\neg$RH world (with a hypothetical off-critical
> quadruple), the property $P$ must be FALSE for a reason computable from $H$ without
> localizing the quadruple: the impure class must produce a violation of $P$ visible in
> the structure (a vector of negative norm where $P$ requires positivity, a forbidden
> intersection class), so that $P\Rightarrow$ purity is an implication with
> content in both worlds. If deciding whether $P$ fails in the $\neg$RH world requires
> knowing WHERE the quadruple is (the situation of [DATUM] Doc 108: inaccessible
> binarity), then $P$ did not individuate anything: FAILS.

**Status of the existing candidate against R-NC.** The only partial structure available
(archimedean and semilocal positivities of CC 2021–2024, [DATUM] verified in Doc 100):
passes NC1 (the construction is functorial from adeles/site), partially passes NC2 (the
archimedean positivity holds for every test of support in $(1/2,2)$ — it overgenerates), and
FAILS NC3 today at the global step: the uniformization in $\lambda$ of its
semilocal positivities is MW-6 ([DATUM] Doc 100, Obstacle O_SL; Doc 110 §5.2 row L4). This does
not refute the CC program: it measures exactly how much is missing and where — which is what
the test is for.

**Remark (why R-NC is falsifiable and not rhetorical).** Each clause is a
syntactic check or a reduction to a finite catalogue: NC1 is an inspection of the
definition; NC2 requires exhibiting the class of objects and the uniform method; NC3 is a check
against a closed list (NO-GO-LIST + the proved RH-equivalents, all cited);
NC4 requires a structural certificate of violation in the adversarial world. A proposal
can PASS the test and still fail (the test is necessary, not sufficient — it does not
guarantee that $P$ is provable); what the test prevents is declaring victory with a
reformulation. **[DATUM]** (P43 via P44): the master quantifier guarantees that something like
this was necessary: every property internal to $\zeta$ that implies weights $=1/2$ is
RH-equivalent or stronger; externality (NC1–NC2) is the only remaining logical
space.

**[CONJECTURE]** The R-NC test is moreover *sufficient* in the following weak sense: a
structure $(H,W,F)$ that passes NC1–NC4 and satisfies R-SIG+R-FIN+R-LEF cannot be a
reformulation of RH (its relative consistency does not by itself imply RH). We do not
derive this: the exact boundary between "external structure whose existence implies RH"
and "reformulation" is subtle (the existence of ANY Weil cohomology with purity
implies RH — the point is that the *construction* contribute a proof mechanism, as the
geometry of $C\times C$ contributed one). We declare the gray zone instead of covering it up.

---

## 5. FROM Route B: requirements for arithmetic access to the traces

### 5.1. R-TR-1: the minimal test class

Route B (roadmap, §7) needs to EVALUATE the traces. The explicit formula gives them — but
only against admissible tests, and the program has already paid to learn where the edge is:

**[DATUM]** (Weil 1952; program normalization in Doc 72/Doc 100). The explicit
formula holds for even tests $h$ with analytic transform on a band
$|\mathrm{Im}\,s|\leq 1/2+\varepsilon$ and suitable decay; the prime side converges
absolutely when $\widehat h(r)\ll e^{-(1/2+\varepsilon)|r|}$.

**[DATUM]** (Doc 105, Thm. 5.5 + Obs. 5.6). The natural test of the CCM framework
($W_{\lambda_0}w$) is exactly at the BOUNDARY ($\varepsilon=0$: poles of the weight $w$ at
$\pm i/2$, decay exactly $e^{-r/2}$) and its prime series diverges like Mertens. The
lesson, already paid for: working at the boundary of the class destroys term-by-term reading.

**[REQUIREMENT] R-TR-1.** The trace identity R-LEF must be valid — with both sides
absolutely convergent or canonically regularized — on a test class
$\mathcal{T}$ satisfying: (a) strict margin: $\mathcal{T}\subset\{\,h:\widehat h(r)
\ll e^{-(1/2+\varepsilon)|r|}\ \text{for some }\varepsilon>0\,\}$ (interior of the Weil
class, not its boundary); (b) sufficient richness to separate moments: $\mathcal{T}$
contains a countable family $\{h_n\}$ whose spectral sides generate (in the sense
of Lemma 5.2 of Doc 118: triangularity over even polynomials, or a dense
substitute). *Derivation of (a):* without margin, [DATUM] Doc 105 — divergence,
term-by-term reading illegitimate. *Derivation of (b):* it is the condition under which
the rigidity machinery that DID close ([DATUM] Doc 118, Theorem 5.3: the only positive
measure with $\int\mathcal{P}_n^2\,d\nu$ constant is $c\,m_\infty$, by Carleman) has
traction: moment rigidity needs the family of annihilated functionals to generate all even
polynomials — the gap G-118.1 (blocks of coinciding ordinates) shows what happens
when dimensions are missing: rigidity does not apply. The minimal class is, then, *countable,
generating and with margin*; the comfortable class is a Schwartz-type space on the band
$|\mathrm{Im}\,s|\leq 1$ closed under the program's computations.

### 5.2. R-TR-2: the order of dependencies — finiteness comes BEFORE

**[REQUIREMENT] R-TR-2.** The Newton reconstruction of Route B presupposes R-FIN:
the input datum of the mechanism ([DATUM] Doc 110, Prop. 4.5; roadmap Thm.
rank-sensitivity) is "$Q$ has rank (of the indefinite block) $\leq N_0$ KNOWN".
The traces alone, without the rank bound, determine nothing: **[DATUM]** (roadmap,
proof of Thm. rank-sensitivity) in infinite rank the traces of a self-adjoint operator do not
determine its spectral measure except by moment determination, and they never stably determine
the number of negative eigenvalues. The logical order is therefore
immovable:
$$\underbrace{\text{R-SIG}}_{\text{define "impure"}}
\;\prec\;\underbrace{\text{R-FIN}}_{\text{bound } N_0}
\;\prec\;\underbrace{\text{R-LEF + R-TR-1}}_{\text{evaluate } \mathrm{tr}_1,\dots,\mathrm{tr}_{N_0}}
\;\prec\;\underbrace{\text{Newton/Hankel}}_{\text{read } \kappa(Q)=2m}
\;\prec\;\text{Route B: } m=0.$$
Moreover, in flow form (R-LEF-FLOW), "the $N_0$ traces" are traces against $N_0$
concrete tests of $\mathcal{T}$ for the compressed block: Route B requires that the
compression to the impure block itself be functorial (another facet of R-WEIGHT(a): if
compressing requires positions, Newton receives traces it cannot have).

**Note on relative strength.** Route B requires a stronger G3 than Route A
([DATUM] roadmap, §7 Route B: "potentially stronger than what G3 needs for Route A"):
for Route A it suffices that R-LEF produce the bound $m<\infty$; for B it is necessary to evaluate
traces of the block with enough precision to distinguish $N_0$ integers. The minimal
version of the R-TR package is therefore that of Route A (existence + bound), and the
comfortable one that of B (effective evaluation). Both share R-TR-1/R-TR-2.

### 5.3. The rigidity model that does close, as a gauge

**[DATUM]** (Doc 118, Theorem 5.6). The program's repaired criterion — RH ⟺
$\int\kappa_n\,d\nu=0\ \forall n$ — was proved by moment rigidity: Carleman
(determinacy, $\sum 1/a_n^\infty=\infty$ exactly) + triangular completeness of
$\{\mathcal{P}_n^2\}$ + Hardy. Its lesson for R-TR, in one line: **what turned
a countable family of identities into a theorem was a uniqueness RIGIDITY
(moment determinacy), not a positivity.** The cohomological analogue: the traces
$\{\mathrm{tr}(h_n)\}$ will determine the impure block if the associated moment
problem is determined — automatic in finite rank (R-FIN), which is another way of seeing
why R-FIN precedes. And the symmetric warning ([DATUM] Doc 118, §6.2.3 and §9): without
finiteness, no finite subfamily of identities suffices — the universal quantifier over
$n$ is irreducible; with finiteness, $N_0$ identities suffice. The finite/countably-infinite
boundary of Doc 118 is exactly the G4/non-G4 boundary.

---

## 6. SYNTHESIS

### 6.1. The axiom table

| axiom | minimal version | what fails without it [DATUM] | function-field analogue | fire test |
|---|---|---|---|---|
| **R-SIG** | $W$-graded decomposition stable under $F$, weights additive under $\otimes$, duality $w\leftrightarrow 2d-w$, internal membership criterion | without a signature, only values: Euler characteristic does not determine inertia [Doc 110 Thm. 4.3, §5.2 L6; roadmap S1] | Frobenius weights: $|\alpha|=q^{w/2}$, automatic from the endomorphism | exhibit the internal criterion and verify it is NOT "Re of the generator spectrum" (if it is, circularity: §2.3) |
| **R-FIN** | $\dim\bigl(\text{impure part of }H^1\bigr)\leq N_0$ with $N_0$ from a site computation; it bounds $\kappa(Q)$ | Newton does not apply; tensor amplification reverses (Form B) [Doc 110 Prop. 4.5 + Obs. 5.3; P44 Probl. L8]; without R-SIG it is not even statable (§2.4) | $\dim H^1=2g$ — but HERE the pure part is infinite: finiteness is of the impure graded piece, not of the total | the integer $N_0$ must come from a computation without zeros + the theorem "every negative direction of $Q$ comes from there"; an Euler characteristic alone does not pass |
| **R-LEF-POLE** | two distinguished characters ($H^0,H^2$ of rank 1, weights 0 and 2) giving $\widehat h(\pm i/2)$ | the spectral side would contain terms with no associated zero: the class↔zero identification breaks (§3.2) | $q^k+1$ in $\#C(\mathbb{F}_{q^k})$ | finite computation: trace of the flow on the candidates vs $\widehat h(\pm i/2)$ [already partially passed: Doc 100 §4, CC 2021] |
| **R-LEF-PRIMES** | local trace per prime = Weil's distribution $W_p$; periodic orbit of length $\log p$ | without local structure, the global sum is a postulate; it does not converge term by term [Doc 105 Thm. 5.5] | local Frobenius at each closed point; finite sum for each $k$ | compute the local trace at ONE prime from the geometry and compare with $W_p$ (Conjecture 100.A is the positivity version; here the identity alone suffices) |
| **R-LEF-REG** | trace identity for the total regularized sum (primes + archimedean paired before summing) | illegitimate term-by-term readings; the "ledger" is a reorderable divergent series [Doc 105 Thm. 5.5, Obs. 5.6; Doc 99 Lemma 5.1] | NO analogue (finite sums in char $p$): a new requirement of Spec ℤ | exhibit the test class where both sides converge and verify margin $\varepsilon>0$ (R-TR-1(a)) |
| **R-LEF-FLOW** | Guillemin's distributional trace as the definition of the dynamical side; grading independent of the spectrum | if weight is defined by the flow spectrum, weight = zero position: circularity (§3.4.3) | $k\in\mathbb{Z}$ vs $t\in\mathbb{R}_+^*$; there spectral and graded purity coincide for free | the identity must be a theorem with both sides computed separately, not a definition of one side |
| **R-WEIGHT(a)** | $w(c_\rho)$ computable from $H$ (graded piece/form/algebraic class), never from $\rho$ | it is class ℱ again: either an RH toll or it uses positions [Doc 110 Thm. 4.3(b); Doc 108 §7.4] | membership in $H^i$ with fixed $i$: functorial | apply NC1 to the definition of $w$ |
| **R-WEIGHT(b)** | purity = THEOREM from geometric positivity (Castelnuovo-type) or amplification (Deligne-type, requires R-FIN beforehand) | postulated purity ⟹ the chain proves "RH assuming something that implies RH" [P43 via P44; Doc 110 Obs. 5.3] | Wei48 (Hodge index) / Del74 (Rankin) | the full R-NC test |
| **R-NC** | NC1 externality + NC2 overgeneration + NC3 no reduction to the MW catalogue + NC4 two worlds | without the test, any proposal can be a disguised reformulation; false victory [P43; NO-GO-LIST] | Castelnuovo passes it: a theorem of surfaces, valid for every divisor, prior to any zeta | the test IS the fire test; it is syntactic/by catalogue, executable on any written proposal |
| **R-TR-1** | countable, generating test class $\mathcal{T}$, with margin $\varepsilon>0$ inside the Weil class | boundary ⟹ Mertens divergence [Doc 105]; without generating richness ⟹ rigidity does not apply [Doc 118, gap G-118.1] | any $k$ works: there is no test class (the variable is discrete) | verify decay $e^{-(1/2+\varepsilon)|r|}$ and generating triangularity of $\{h_n\}$ |
| **R-TR-2** | order: R-SIG ≺ R-FIN ≺ R-LEF/R-TR-1 ≺ Newton ≺ $m=0$; functorial compression to the impure block | traces without a rank bound do not determine signatures [roadmap Thm. rank; Doc 110 Prop. 4.5 by contrast] | Lefschetz gives $\#C(\mathbb{F}_{q^k})$; with $2g$ known, finitely many $k$ suffice | check that no step of the reading plan uses a trace before having the bound $N_0$ |

### 6.2. What the table says about the current state

Against the existing candidate (CC program, measured in [DATUM] Doc 110 §5.2): R-LEF-POLE
partially verified (archimedean, CC 2021); R-LEF-FLOW with the dynamical half done
(Connes's 1999 trace IS the R-LEF identity in the adele realization — but on
a space without R-SIG or R-FIN); R-SIG, R-FIN, R-WEIGHT: absent; R-NC: not yet applicable
(there is no proposal for $W$ to submit). The exact hole remains the one Doc 110
named (L6 + positivity), now with the new precision of §2.4: **what is finite is not
$H^1$ — it is its impure part — and that makes R-SIG logically prior to everything.**

### 6.3. Tensions between axioms (where a construction may be impossible)

Declaring them is part of candor: if any tension is a contradiction, the
specification is empty and the roadmap dies at G1–G2. We do not claim that they are; we claim
that every proposal must resolve them explicitly.

**T1 (R-FIN vs R-LEF-FLOW): finiteness cannot carry the trace.** Derivation: if $A$
is the generator of a flow on a finite-dimensional space of dimension $N$, then
$\mathrm{tr}(e^{uA})=\sum_{i\leq N}e^{u\lambda_i}$ is a real-analytic function of $u$;
but the arithmetic side of R-LEF has distributional singular support on
$\{k\log p\}$ (deltas at orbit lengths — [DATUM] Connes 1999; Guillemin 1977).
A finite sum of exponentials has no singular support: **a finite-dimensional $H$
cannot satisfy R-LEF.** Forced resolution (consistent with §2.4): the carrier of
the trace (the full $H^1$, infinite-dimensional, pure part included) and the carrier of
finiteness (the impure graded piece) are DISTINCT. The trace is distributional on the
large one; the signature is algebraic on the small one; R-SIG is the bridge. Every proposal must
exhibit the two spaces and the bridge — and the compression from the large to the small must be
functorial (R-TR-2).

**T2 (R-LEF-REG vs R-SIG): signatures do not survive regularization limits without a
gap.** Archimedean regularization defines the global objects as limits
(pairing of two divergences, [DATUM] Doc 105); but **[DATUM]** (Doc 110, Prop.
3.4(c), via [Phi96]): spectral flow — and with it every signature — is not continuous under
resolvent convergence without a uniform spectral gap; and **[DATUM]** (Doc 108, binarity,
via Doc 110 Thm. 4.3(b)): per-window indices jump from 0 to $\asymp m\log T$ with no
intermediate values. Tension: the signature of R-SIG must be defined BEFORE the
regularizing limit (on the algebraic/geometric object) and proved compatible with it
— not read off the limit. A proposal that defines its intersection form as "a
regularized limit of truncated forms" falls back into S3 (uniformity debt) and must be rejected
by R-FIN's fire test.

**T3 (R-TR vs R-NC): arithmetic access flirts with circularity.** The stronger
G3 (Route B: effective evaluation of traces), the closer the structure is to being
"the explicit formula under another name" — and NC3 exists precisely because the program
proved that reformulations of positivity of the explicit formula are RH-equivalent
at the threshold ([DATUM] NO-GO-LIST MW-1/MW-6; Doc 118 §9: the repaired criterion is
a reformulation, the Hadamard barrier intact). The resolution is not to give up R-TR but to
distribute: the trace IDENTITY can (must) coincide with the explicit formula
(R-LEF is exactness); what must be external is the STRUCTURE that produces the weight
bound (R-WEIGHT/R-NC). The danger to flag: a proposal where the same object
fulfills both roles with no verifiable separation. NC2 is the detector.

**T4 (flow $\mathbb{R}_+^*$ vs weight integrality): quantization is not free.**
In char $p$, weights are integers because $q^{\mathbb{Z}}$ is discrete: the dynamics
quantizes on its own. With a continuous flow there is no spectral quantization; weight
integrality must come from the grading (R-SIG as a primitive datum, §2.3) — that is, from
the structure of the category of coefficients on the site (sheaf rank, degrees of
tropical divisors: the integers the site DOES have, [DATUM] Doc 110 §5.2 row L1).
Tension with R-WEIGHT(b): geometric positivity must force "the spectrum of the generator
on $\mathrm{gr}^W_1$ has real part exactly $1/2$" — a statement of continuous
spectral rigidity with no precedent in the template (there it is automatic). It is the
G2 face of the $\mathbb{Z}$ vs $\mathbb{R}$ difference, and the place where the analogy with
function fields is thinnest. **[CONJECTURE]** The resolution goes through
semisimplicity + duality: if the duality form of R-SIG is non-degenerate on
$\mathrm{gr}^W_1$ and the flow preserves it, the spectrum of the generator is symmetric about
$\mathrm{Re}=1/2$ by the geometric functional equation, and positivity (R-WEIGHT(b))
would exclude pairs off the axis. It is exactly Weil's scheme — but its
transplant to the continuous case is not derived here: an interface conjecture, flagged as
the first concrete problem of Phase 39.

### 6.4. Closing

No new geometric statement has been proved in this document. What has been done is to
force, from theorems already proved on the analytic side (roadmap Thm. rank-sensitivity,
Doc 110 Thm. 4.3 and Prop. 4.5, Doc 105 Thm. 5.5, Doc 118 Thm. 5.6, P35, P44), the exact
shape of the missing object: a theory $H$ with weights first (R-SIG), finiteness of the
impure block after (R-FIN), exact and regularized flow trace (R-LEF-*), purity as an
external theorem (R-WEIGHT) testable by R-NC, and ordered arithmetic access (R-TR). The
four tensions of §6.3 are the points where the specification may turn out to be
inconsistent; resolving them — or proving they cannot be resolved — is the work of G1↔G2, not
this document. A false victory is worse than a failure: that is why the central
contribution is no axiom at all but the R-NC test, which turns "is this progress or a
reformulation?" into a question decidable by inspection and catalogue.

---

## References

**Internal (backward-only):** roadmap-rh (S1–S3, Milestone ms:spec, Thm. rank-sensitivity,
nodes G1–G4, Routes A/B); P44 (Thm. 2.2 dichotomy, Probl. 3.1 = L8, §3 anti-Siegel);
P43 (master quantifier, §4 value/inertia — cited via P44 and Doc 110); P35
(κ(Q)=2m); Doc 118 (Lemma 2.3 Carleman, Thm. 5.3 rigidity, Thm. 5.6 repaired criterion,
gap G-118.1, §6.2.3, §9); Doc 110 (Def. 4.1 axioms L1–L6, Thm. 4.3, Prop. 4.5, Cor. 4.6,
Obs. 5.3, §5.2, Prop. 3.4); Doc 108 (§7.4, Prop. 2.5, binarity — cited via Doc 110);
Doc 105 (Thm. 5.5 Mertens divergence, Obs. 5.6 boundary of the Weil class, §7);
Doc 100 (archimedean positivity §4, additivity over places §5, Obstacle O_SL,
Conjecture 100.A); Doc 99 (QW_λ, automatic locality, Lemma 5.1, E4 — cited via
Docs 100/105/110); Doc 72 (Weil's ledger, Thm. 4.1); Doc 111 (Prop. 2.2 —
cited via P44); NO-GO-LIST (MW-1…MW-7).

**Literature (verifiable):**
- [Connes99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106.
- [Del74] P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974), 273–307;
  *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), 137–252.
- [Den98] C. Deninger, *Some analogies between number theory and dynamical systems on
  foliated spaces*, Doc. Math., Extra Vol. ICM Berlin I (1998), 163–186.
- [Gan59] F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Ch. X.
- [Gro58] A. Grothendieck, *Sur une note de Mattuck–Tate*, J. reine angew. Math. 200
  (1958), 208–215.
- [Gro69] A. Grothendieck, *Standard conjectures on algebraic cycles*, in Algebraic
  Geometry (Bombay Colloquium 1968), Oxford Univ. Press, 1969, 193–199.
- [Gui77] V. Guillemin, *Lectures on the spectral theory of elliptic operators*, Duke
  Math. J. 44 (1977), 485–517 (distributional trace of flows; the source that Connes99
  cites for the dynamical side).
- [KM74] N. Katz, W. Messing, *Some consequences of the Riemann hypothesis for
  varieties over finite fields*, Invent. Math. 23 (1974), 73–77.
- [MT58] A. Mattuck, J. Tate, *On the inequality of Castelnuovo–Severi*, Abh. Math.
  Sem. Univ. Hamburg 22 (1958), 295–299.
- [Mey05] R. Meyer, *On a representation of the idele class group related to primes and
  zeros of L-functions*, Duke Math. J. 127 (2005), 519–595 [UNVERIFIED the exact
  editorial datum].
- [Phi96] J. Phillips, *Self-adjoint Fredholm operators and spectral flow*, Canad. Math.
  Bull. 39 (1996), 460–467 (cited via Doc 110).
- [Ser60] J.-P. Serre, *Analogues kählériens de certaines conjectures de Weil*, Ann. of
  Math. 71 (1960), 392–394.
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford,
  1986.
- [Wei48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*,
  Hermann, Paris, 1948.
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- Connes–Consani (arithmetic/scaling site, tropical RR, positivities 2021–2024) and
  Connes–Consani–Moscovici (ZST): cited with data verified in Docs 99/100/110.

*End of Doc 119.*
