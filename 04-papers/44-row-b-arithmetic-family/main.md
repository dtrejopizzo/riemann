# Paper 44 — Row B: the arithmetic family inside row A, and the separation of the two contacts

David Alejandro Trejo Pizzo.
Repository: `research/riemann`.  Companion to [Paper 43](../43-row-a-torsion-theory/main.md), which closes row A
at Weil strength on the graph sector `G`.  This paper closes row B on the same
carrier: it produces the arithmetic correspondences inside `G`, computes their
derived contacts, and proves that the contact degree is `Λ(n)` with analytic
weight `n^{−1/2}`.

**Status label established here.**

> **Lead decision of record (R131.019).** `ROW B: WEIL-STRENGTH-COMPLETE`
> on Paper 43's declared carrier (§14.0a–b), as a theorem about row A's declared
> trace; B.4 amended (accepted ), B.7 amended (author,
> ) — **[phase 133, amendment accepted : this read "B.7 by
> ruling with the adversarial auditor's dissent recorded"; the author accepted
> the B.7 amendment of PANEL_SYNTHESIS §4.2 on , superseding the
> the earlier ruling `R131.005` §2, and the dissent is kept verbatim in the §10
> table as history]**. Granted after seven construction rounds and five
> adversarial audits (R131.002, .008, .011, .014, .017), the last grading the label
> **EARNED**. Recorded beside the label: no sign, no positivity, no `𝓝_∞ = 0`;
> two quarantined `CLASSICAL` imports used by no clause (**[phase 132]** the
> explicit-formula half of the first is now `PROVED-IN-REPOSITORY`, Paper 45
> Thm 9.4; Weil's **criterion** stays `CLASSICAL`); the interface with
> Weil's criterion is a **colimit** statement and false at a finite chart; no
> divergence rate is convention-free; `(Wgr)` withdrawn as false (W23) and
> "positivity on Dirichlet profiles ⟹ RH" is `OPEN`. Full text: §10.4 and
> [R131.019](../../03-research/phase-131-row-b-closure/R131_019_FINAL_AUDIT_AND_LABEL.md).

```text
ROW B, after the phase-131 rebuild:

  ROUND 3.  The object that carries the arithmetic is the FROBENIUS
  FAMILY (section 3ter): Frob_{p^k} = Haar measure of the fixed-point
  stratum j_p(p^k Z_p^x), Frob_n = star_{p|n} Frob_{p^{v_p(n)}}.
    * strong monoidal on (N,x) with a TRUE UNIT Frob_1 = Delta (a point
      mass, not a projector);  Frob_n * Frob_n^dagger = Delta^(n), the
      averaged half-density form of Weil's Gamma_F Gamma_F^t = q Delta
      (Delta^(n) is NOT Delta, and the paper says so);
    * the dagger-closed family is a commutative INVERSE SEMIGROUP indexed
      by Q_>0^x GRADED BY finite prime sets, idempotents Delta^(F);
    * supp Frob_n determines n AND P(n); no continuous family
      interpolates the Frob_n;   Gamma_n^rad = Frob_n * Delta^rad;
    * finite contact = Lambda(n) n^{-1/2} h(1/n) EXACTLY at every level;
      zero at composite n because the support meets NO stratum;
    * INTEGRAL SHADOW Sh_Z(Frob_n) = [L_S -> n -> L_S] on the OBJECTS
      (section 6bis), Moebius cofiber [Z -> Phi_n(1) -> Z]: the accepted
      amended B.4 is proved on objects.  Complex realization acyclic;
      degrees only; P123.022 untouched;
    * [ROUND 5: the divergence RATES below are normalization-dependent
      (finding M5) and are no longer headlined; what is stated is that
      the point-class pairing I_A(Frob_n, Frob_n) DOES NOT EXIST.  The
      equivalence with RH is a COLIMIT statement (finding M4); at a
      finite chart it is false.  And "the sign of the Frobenius form is
      not RH" is WITHDRAWN as a non-sequitur (W19) and replaced by the
      PROVED Thm 8bis.4a: at every finite chart there is a primitive
      class with Q_fin > 0, so positivity FAILS on the pure Frobenius
      form, unconditionally.]
    * [CORRECTED IN ROUND 4, adversarial finding F1, confirmed in the final audit:]
      TWO GRAM FORMS.  The FROBENIUS family carries only the FINITE half
      W_fin of the Weil kernel -- its archimedean block vanishes for
      large N, because supp Frob_n misses Im j_infinity (Cor 3ter.10b) --
      with a diagonal that has NO (eps,N)-independent value: the pairing
      I_A(Frob_n, Frob_n) DOES NOT EXIST (Rem 8bis.1c), and no rate is
      stated because none is convention-free (Cor 8bis.1b').
      The UNIT-AVERAGED family Frob * Delta^rad = Gamma^rad carries the
      FULL Weil kernel W_fin + omega_infinity, exactly, at every level.
      So the averaging projector is what converts the finite half into
      the whole, at the cost of forgetting factorization (Thm 8bis.1').
      Delta . Delta = -infinity (infinite genus), AT A FIXED CHART
      (Thm 8bis.2 is EXEMPTED from (C1); under T_infinity the finite
      part is identically 0 and the divergence is purely archimedean).
      The object whose Hodge index is at issue is the Gram form of
      Frob * Delta^rad, NOT the Frobenius Gram form -- by Thm 8bis.4(iii)
      (Weil's criterion on the RADIAL family, in the COLIMIT) together
      with Thm 8bis.1e.
      [ROUND 7, findings A2/N4 of R131.017: rounds 4-6 wrote "rate
      computed", "diverges LINEARLY in N", and attributed the last
      sentence to Thm 8bis.4(iv) -- the clause whose round-4 form is
      WITHDRAWN by W19.  Round 6 reported this bullet as rewritten and
      it was not.  Corrected here.]
      ROW B DELIVERS THE GRAM FORM, NOT THE SIGN.

  [ROUND 2: the round-1 banner called Gamma_n^rad "the ideal class".
   Finding F1 of R131.002 refuted that: on a chart with P(n) in S_f the
   ideal (n) is the UNIT ideal (Lemma 3bis.3b), and the object is the
   NORM (level) class.  Renamed throughout.]

  The object is the NORM CLASS Gamma^rad_(t), the normalized Haar measure
  of the level set {|x|_S = e^-t}, with Gamma_n^rad := Gamma^rad_(log n).
  It is a K^natural-invariant compactly supported probability measure on
  C_S (K^natural = {+-1} x prod_p Z_p^x): a multiplier of D_A, an element
  of Paper 43's completion N_A^dist, NOT an element of D_A (Def 3bis.4,
  Rem 3bis.4b, Thm 8.3).  AS AN OBJECT it forgets factorization: the
  realization factors through (N,x) -> (R_>0,x) (Lemma 3bis.3b).

  WHERE THE ARITHMETIC IS (Thm 3bis.7'): in the CONTACT LOCUS of the
  one-parameter family {Gamma^rad_(t)}.  The finite-place part of T,
  disintegrated along the family, is the unique purely atomic Radon
  measure omega_fin with support exactly {+-k log p} and atom masses
  (log p) p^-k/2.  Prime powers, Lambda, and Lambda(composite) = 0 are
  READ OFF THE CONTACT, not carried by the objects.

  PROVED here on Paper 43's declared carrier:
    * monoidality, dagger, bidegree M = (n^1/2, n^-1/2), and independence
      of lift, gauge, uniformizers and chart          (Thm 3bis.5);
    * the FINITE CONTACT of Gamma_n^rad in row A's own declared trace is
      Lambda(n) n^-1/2, with Lambda(p^k) = log p = the multiplicative Haar
      VOLUME OF THE VALUATION SHELL p^k Z_p^x, and 0 at composite n
      (Thm 3bis.7, Def-Thm 3bis.8).  Lambda is DERIVED, never input;
    * the ARCHIMEDEAN CONTACT is the density K(log n) = n^3/2/(n^2-1)
      (Def-Thm 3bis.8); it is of a different type (density, not atom) and
      is not part of Lambda;
    * the smeared classes Gamma_h are objects of D_A and T(Gamma_h) is
      the prime packet plus the Gamma term                (Thm 3bis.9);
    * DEGREE MATCHING: log[L_S:nL_S] = log n = sum_{d|n} Lambda(d), and
      deg_det Prim_n = log|Phi_n(1)| = log|det(1-T|V_n)| = Lambda(n)
      = n^1/2 * contact_fin(Gamma_n^rad)                 (Thm 3bis.10);
    * coprime support of the two Z-linear contacts        (Thm 3.3);
    * Prim is NOT monoidal for (x)^L                      (Thm 5.4).

  CORRECTED here: w_unit(Gamma_n) = n-1 is a property of the LIFT
  a_S(n), not a contact of the class: delta_S(1/n) is not in the image
  of any slice map j_q, q in S_f (Prop 3bis.2, Cor 3bis.3).  The
  "unit-sector obligation" of the former section 9.2 is WITHDRAWN.

  Clause B.4 stays REFUTED AS STATED (LDelta^* Gamma_n is the fixed
  complex, differential n-1) and is PROVED AS AMENDED in section 6.2a.
  The amendment is a PROPOSAL for decision, mirroring the A.6 decision.

  NOT claimed: that Z/Phi_n(1) is an object of G; any object-level
  realization of the integral contact (P123.022 refutes it); any
  statement about zeros, any sign, any positivity.
```

> **Status, 2026-09-12.**  An adversarial audit (phase 128, `D128.002`) found
> real errors, including a backwards inference in Theorem 8.1(iii).  The label
> `WEIL-STRENGTH-COMPLETE` is **withdrawn**.  Every finding, my verification of
> it and its disposition are in
> [phase 128](../../03-research/phase-128-adversarial-audit/D128_002_AUDIT_B.md).
> The corrections are applied in place below and marked.
>
> **[REBUILT, phase 131, round 3.]**  The **author accepted the B.4 amendment**
> on  and asked for the recorded reservations to be dissolved with
> new mathematics.  Round 3 adds three sections: **§3ter, the Frobenius
> family** — the Haar measures of the fixed-point strata `j_p(p^kZ_p^×)`,
> a strong monoidal realization of `(N_{≥1},×)` with a **true unit** `Δ`,
> whose objects remember `n` **and** `P(n)`, and whose finite contact is
> `Λ(n)n^{−1/2}` exactly; **§6bis, the integral shadow** `Sh_Z(Frob_n) =
> [L_S →n→ L_S]`, which proves the accepted amended B.4 **on the objects**;
> and **§8bis, the Gram form**, with the theorem that the regularized
> self-intersection of the diagonal is `−∞` and an interface with Weil's
> criterion whose open half is stated exactly.  **No sign is claimed.**
> §3bis is kept in full: its negative result (the radial objects are
> arithmetic-free) is true, and §3ter is only meaningful against it.  Round-3
> withdrawals and three refuted blueprint claims are in §9bis.
>
> **[REBUILT, phase 131; revised in round 2.]**  The paper is rebuilt around
> the **norm class** `Γ^{rad}_{(t)}` and its **contact locus** (new §3bis).
> Round 1 called this object "the ideal class"; finding `F1` of `R131.002`
> refuted that name and the framing that went with it, and the repair —
> Lemma 3bis.3b and Theorem 3bis.7′ — is round 2's main addition.  Every
> round-2 change is marked `[REBUILT, phase 131, round 2]`, and
> `R131_004_ROUND2.md` disposes of every finding of `R131.002`
> (`F1`–`F13`) and `R131.003` (`F1`–`F5`).  Every new or changed passage is marked `[REBUILT, phase 131]`.
> What was withdrawn in this phase — including the `n−1` obligation formerly
> handed to row C — is recorded in §9bis.  Paper 43 is cited in its
> post-phase-130 state, where it carries the label `WEIL-STRENGTH-COMPLETE`
> **on its declared carrier and with its recorded qualifications** (Paper 43
> §14.0a–b).  No label is granted to row B here: the closure rule reserves it
> to an adversarial audit, and §10 states what the construction believes the
> mathematics earns.

---

## 0. Summary

Row B had one blocking calculation, proved in P123.060 and repeated as a
stopping rule in the closure plan (§6, "test que puede descartar rápidamente
la candidata"):

> the correspondence `Γ_n` carries **two** derived contact operations with
> **different differentials** — the fixed-graph differential `n−1` and the
> ramification differential `n` — and they are not quasi-isomorphic.  Row B
> needs the second (it produces the cyclotomic factor, hence `Λ`), row A's
> analytic trace appears to deliver the first.

Every previous attempt tried to identify the two complexes, or to replace one
determinant by the other.  P123.060 proves that cannot work: at a prime power
`n=p^k` the fixed complex is **contractible over `Z_p`** while the primitive
ramification complex has cohomology `Z/p`.

**The insight of this paper is that the two operations are not competitors.
They have coprime support on `Spec Z`, and row A's invariant is their
product.**  Concretely (Theorem 3.3):

    supp H⁰(C_ram(n)) = V(n),      supp H⁰(C_fix(n)) = V(n−1),
    gcd(n, n−1) = 1,

and for the local factor `τ_p(σ)=|σ_p|_p^{1/2}/|1−σ_p|_p` of Paper 43,

    at p | n    :  |1−n|_p = 1,  so  τ_p(Γ_n) = |n|_p^{1/2}   (ramification),
    at p ∤ n    :  | n |_p = 1,  so  τ_p(Γ_n) = |1−n|_p^{−1}  (fixed),

so that the principal weight of `Γ_n` factors **canonically and place-wise**
as `w(Γ_n) = w_ram(Γ_n) · w_unit(Γ_n)`, with

    w_ram(Γ_n) = n^{−1/2} = (det C_ram(n))^{−1/2},
    w_unit(Γ_n) = n−1     = # H⁰(C_fix(n)).

Nothing is discarded and nothing is chosen: the place set is determined by
`Γ_n` itself.  The "mismatch" of P123.060 is a **decomposition theorem**.
(The dichotomy is a property of the local factor at a single place, so it
splits every term of the lattice sum (8.2) of Paper 43, not only the
principal one; row B needs the principal term, which is the diagonal
contact.  See Remark 3.7.)

Everything else follows.  `−2 log w_ram(Γ_n)` is the logarithmic index of the
correspondence on its integral lattice, `log[L_S : nL_S] = log n`, which is
the determinant degree of the index complex `Q_{S,n}` of P123.038; this is
exactly the arrow that P123.038 §5 and P123.039 §5 declared missing
("the lattice-index operation must be realized as the admissible diagonal
shadow").  Applying the divisor cube of P123.037 — which we prove is the
categorified Möbius operation of the divisor poset (Lemma 5.1) — turns
`log n` into

    (μ ∗ log)(n) = Λ(n),

with the analytic weight `n^{−1/2}` carried along untouched.  That is
`deg_det(contact) = Λ(n)` with weight `n^{−1/2}`, the target of §6.5 of the
closure plan.

One further requirement of the closure plan is shown to be **impossible and
therefore mis-specified**: primitive extraction cannot be a monoidal functor,
because `Λ` is not additive on coprime labels (`Λ(6)=0 ≠ log 2 + log 3`).
Theorem 5.4 replaces it by the correct structure — the realization `Γ` is
monoidal on the label monoid, and primitive extraction is the Möbius operation
of the divisor **poset** acting on the shadow target, which is not a monoidal
operation and was never required to be.

The paper also isolates a symmetry already used inside Paper 43 but not stated
place-wise: the local factor is inversion-invariant, `τ_v(σ^{−1}) = τ_v(σ)`
(Lemma 4.5).  Place by place this is the pairing of `Γ_n` with `Γ_n^†` behind
the two terms `h(log n)+h(−log n)` of the explicit formula.

**[REBUILT, phase 131 — what this paper is really about.]**  Everything above
concerns the **element** `a_S(n)` and two `Z`-linear complexes attached to the
label `n`.  It is correct and it is kept, but it is not the contact of the
arithmetic correspondence, because the class of `a_S(n)` in the carrier is

    δ_S(1/n) = ( 1/n at ∞ ; 1 at every finite place of S ),

with unit coordinate `1`, not `n` (Lemma 3bis.1; Paper 43 Lemma 3.3).  The
arithmetic object on the carrier is the **radial family of norm classes**

    Γ^{rad}_{(t)} := normalized Haar measure of `{|x|_S = e^{−t}}` ,
    Γ_n^{rad} := Γ^{rad}_{(\log n)} = ∫_{K^♮} δ_S(1/n)·u\,du ,
    K^♮ = {±1}×∏_{p∈S_f}Z_p^× ,

the unit average of the classes of all lifts of `a_S(n)` of modulus `1/n`
(Definition 3bis.4).  It is monoidal in `n`, `†`-covariant on the group
completion `Q_{>0}^×`, of bidegree `(n^{1/2},n^{−1/2})`, and independent of
lift, gauge, uniformizers and chart (Theorem 3bis.5).  **[REBUILT, phase 131,
round 2.]**  As an **object** it forgets factorization — the realization
factors through `(N_{≥1},×) ↪ (R_{>0},×)` (Lemma 3bis.3b) — so the arithmetic
is not in the objects but in the **contact locus** of the family
(Theorem 3bis.7′): the finite-place part of `T`, disintegrated along
`\{Γ^{rad}_{(t)}\}`, is the unique purely atomic Radon measure `ω_{fin}` with
support exactly `\{±k\log p\}` and atom masses `(\log p)p^{−k/2}`, so the
prime powers, `Λ`, and `Λ(\text{composite}) = 0` are **read off the contact
with the diagonal**.  The atom at `t = \log n` is

    contact_{fin}(Γ_n^{rad}) = Λ(n)\,n^{−1/2} ,
    Λ(p^k) = \log p = vol_{d^*x}(p^kZ_p^×) ,                          (0.1)

the multiplicative Haar volume of the valuation shell (Theorem 3bis.7,
Definition–Theorem 3bis.8): `Λ` is **derived** as a shell volume, exactly in
the sense Paper 43 Remark 9.7a(1) requires, and it vanishes at composite `n`
because no single place has a shell of modulus `1/n`.  Its **archimedean
contact** is the density `K(\log n) = n^{3/2}/(n^2−1)`, an object of a
different type which is not part of `Λ` (Remark 3bis.8a).  And the degrees
match:

    \log[L_S:nL_S] = \log n = Σ_{d|n}Λ(d) ,
    deg_det Prim_n = \log|Φ_n(1)| = \log|\det(1−T|V_n)| = Λ(n)
                   = n^{1/2}·contact_{fin}(Γ_n^{rad}) ,               (0.2)

which is the comparison P123.038 §5 and P123.039 §5 declared missing
(Theorem 3bis.10).

**[REBUILT, phase 131, round 3 — the object that does carry the arithmetic.]**
The radial family is not the only one available.  The **Frobenius family**
(§3ter) consists of the Haar measures of the fixed-point strata of the local
dilations,

    Frob_{p^k} := Haar measure of j_p(p^kZ_p^×) ,
    Frob_n := ⋆_{p|n}Frob_{p^{v_p(n)}} ,   Frob_1 = Δ ,

and it is **not** radial.  It realizes `(N_{≥1},×)` strong monoidally with the
**diagonal itself** as unit (Theorem 3ter.4); `Frob_n⋆Frob_n^† = Δ^{(n)}`, the
averaged, half-density-normalized form of Weil's `Γ_F⋆Γ_F^t = qΔ`
(Theorem 3ter.6, with `Δ^{(n)} ≠ Δ` recorded); the `†`-closure is a commutative
**inverse semigroup** graded by finite prime sets (Theorem 3ter.7); the support
of `Frob_n` determines `n` **and** `P(n)` (Theorem 3ter.4(iv)); and

    Σ_q W_q\big(Frob_n^{[h,N]}\big) = Λ(n)\,n^{−1/2}\,h(1/n)

**exactly, at every level `N`**, with no regularization and no limit at the
finite places (Theorem 3ter.10) — the vanishing at composite `n` being the
**disjointness of the object's support from every fixed-point stratum**
(Theorem 3ter.12).  Averaging destroys this: `Γ_n^{rad} = Frob_n ⋆ Δ^{rad}`
(Proposition 3ter.5).  On the objects, `Sh_Z(Frob_n) := [L_S →n→ L_S]` is the
integral shadow (§6bis), with Möbius cofiber `[Z→Φ_n(1)→Z]`, and
Theorem 6bis.4 proves the accepted amended clause B.4 there.  Finally §8bis
computes the **two Gram forms**.  **[REBUILT, phase 131, round 4, after the
adversarial finding `F1`, confirmed by the final audit: the round-3 text said "the Gram
form of the Frobenius family is the Weil kernel", which this paper's own
Corollary 3ter.10b refutes; see §9bis W16.]**  The **Frobenius** family carries
only the **finite half** `W_{fin}`: its archimedean block is multiplied by the
arithmetic indicator `∏_{s∉F}\mathbf 1[s^N | (n−m)]` of (3ter.9) and vanishes
for large `N`, because `supp\,Frob_n` misses `Im\,j_∞`.  The **unit-averaged**
family `Frob ⋆ Δ^{rad} = Γ^{rad}` carries the **full** Weil kernel
`W_{fin} + ω_∞`, exactly and at every level (Theorem 8bis.1e).  So the
averaging projector is precisely what converts the finite half of the Weil
kernel into the whole of it — at the cost, by Lemma 3bis.3b, of forgetting the
factorization: **two readings of one projector** (Theorem 8bis.1′).  §8bis also
proves that the regularized self-intersection of the diagonal **diverges to
`−∞`** (infinite genus), computes the Frobenius diagonal exactly, and states
the interface with Weil's criterion.  **[REBUILT, phase 131, round 5.]**  Three
quantifiers must travel with that sentence, and now do: the trace throughout
§8bis is the **colimit** trace `T_∞` (convention (C1)), so the equivalence with
Weil's criterion is a **colimit** statement and is *false* at a finite chart;
the divergence **rate** of the Frobenius diagonal depends on the normalization
of the level-`N` factors (convention (C2), Corollary 8bis.1b′), so **no rate is
headlined** — what is stated is that `I_A(Frob_n,Frob_n)` **does not exist**;
and the round-4 claim "the sign of the Frobenius Gram form is not RH" is
**withdrawn** as a non-sequitur (§9bis W19), replaced by the proved
Theorem 8bis.4a: at every finite chart there is an explicit **primitive** class
with `Q_{fin} > 0`, so **positivity fails on the pure Frobenius form** — the
quadratic form `Q_{fin}` with kernel `W_{fin}` alone, named once at
Theorem 8bis.4(iv) — **unconditionally, at every finite chart**.  The object
whose Hodge index is at issue is the Gram form of `Frob ⋆ Δ^{rad}`, **by
Theorem 8bis.4(iii)** — the colimit statement, which is Weil's criterion
carried by row A's trace — **together with Theorem 8bis.1e**.
**[REBUILT, phase 131, round 7, finding `A1` of `R131.017`: round 6 reported
this repair as done and it was not; the sentence "since the latter's kernel
lacks the indefinite `ω̂_∞`" survived verbatim here.  It **is** the
symbol-comparison argument withdrawn by §9bis W19, and it is deleted.  The
conclusion is attributed to (iii) and to Theorem 8bis.1e, never to a comparison
of symbols.]**
**Row B delivers the Gram form; it does not deliver the sign.**

**The `n−1` is withdrawn as a contact.**  The earlier §9.2 handed row C the
obligation of absorbing `w_unit(Γ_n) = n−1`.  There is no such obligation:
`δ_S(1/n)` is not in the image of the slice map `j_q` for **any** `q ∈ S_f`
(Proposition 3bis.2), so a test concentrated at the class meets no finite
shell and no finite unit packet, and `n−1` is a product of local factors of
the **lift** `a_S(n)`, not a contribution of the class to any local term of
`T` (Corollary 3bis.3).  §9bis records the withdrawal and corrects the
cross-reference to Paper 45 §11, which discharged an obligation that does not
exist.

---

## 1. Standing conventions

### 1.1 Status labels

`PROVED` (here), `PROVED-IN-REPOSITORY` (with the exact note), `IMPORTED`
(external, hypotheses checked), `CONDITIONAL`, `REFUTED`.  No arrow is used
without a label.

### 1.2 Carried over from Paper 43

We use, without reproving:

- the carrier `X_S`, source `U = A_sm^u(P) = (E_P ⊕ C1) ⋊ Γ_S`, and the
  graph sector `G = C_tw(U)` with its compact-section Fell completion
  (Paper 43 §2–3; P123.064, P123.016, P123.121);
- graph bimodules `E_a` and composition `E_u ⋆ E_v ≅ E_{uv}`, `E_1 = Δ`
  (Paper 43 (3.1)–(3.2); P123.016, P123.019);
- morphisms `Hom(E_a,E_b) = C·U_γ` if `a=γb`, else `0` (Paper 43 (3.3);
  P123.082);
- the canonical half-density `h = |·|_S^{−1/2}`, fixed by the product formula,
  and the realization `Π(b,a) = |a|_S^{−1/2}T_{b,a}` (Paper 43 §5.2;
  P123.074, P123.073);
- the dagger `E_a^† = E_{a^{−1}}`, the Hilbert adjoint, with `Δ^† = Δ`
  (Paper 43 Def. 5.2, Thm. 5.3);
- the analytic trace invariant `T` of Paper 43 §8, with local factors

      τ_v(σ) = |σ_v|_v^{1/2} / |1−σ_v|_v                              (1.1)

  at every place with `σ_v ≠ 1` (Paper 43 (8.1); P123.042–046, P123.060 §2),
  and `T` additive on sums, sign-reversing on shifts, with the cone law.

### 1.3 Normalizations fixed once

`Λ(n) = log p` if `n=p^k` (`k≥1`), `Λ(n)=0` otherwise, `Λ(1)=0`.  `μ` is the
Möbius function.  `P(n)` is the set of distinct primes dividing `n`.  `V(m) ⊂
Spec Z` is the closed set of primes dividing `m`.  Absolute values are
normalized so that the product formula `∏_v |x|_v = 1` holds for `x ∈ Q^×`,
with `|p|_p = 1/p`.  A chart `S` always contains `∞` and every prime dividing
the label under discussion; `S_f = S ∖ {∞}` and `L_S = ∏_{p∈S_f} Z_p`.

---

## 2. The acceptance contract for row B

We fix the clauses before constructing, mirroring the row A specification
(`P123_A_ACCEPTANCE_SPECIFICATION.md`) and §6 of the closure plan.

| clause | requirement |
|---|---|
| **B.1** | A source category of arithmetic labels with its operation and its divisor structure, stated with objects and morphisms.  **[REBUILT, phase 131, round 3.]**  Read as: the monoid `(N_{≥1},×)` with its divisor poset, **together with its inverse-semigroup completion** `𝔉 = \{(r,F) : r ∈ Q_{>0}^×,\ P(r) ⊆ F ⊂ S_f\ \text{finite}\}` (Thm. 3ter.7), which is what the dagger forces and which is **not** a group: its idempotents `Δ^{(F)}` form the semilattice `(𝒫_{fin}(S_f),∪)`. |
| **B.2** | A realization into row A's category, monoidal on labels, independent of uniformizers, charts, lifts and gauge. |
| **B.3** | Unit, transposition and half-densities preserved by the realization. |
| **B.4** | The derived contact of `Γ_n` computed in the declared category; for `n>1` its arithmetic part identified with `[Z →Φ_n(1)→ Z]`, with every truncation made explicit.  **`REFUTED AS STATED`; `PROVED AS AMENDED`** (§6.2a, Thm. 6.3a).  **[REBUILT, phase 131.]**  **ACCEPTED BY THE OWNER, 2026-09-12.**  **[REBUILT, phase 131, round 3: the accepted amendment is now proved **on the objects** of the Frobenius family (Thm. 6bis.4), not only on the radial labels; the round-2 wording is kept verbatim below because it is the text that was accepted.]**  **[REBUILT, phase 131, round 2, finding `F2`: the round-1 wording said "the value on it of `T`", which is ill-typed — `T(Γ_n^{rad})` is undefined, and the naive place-wise evaluation returns `0`.  The amendment is re-worded around the representing measure.]**  *Proposed amendment text, for decision:* "the derived contact of the **norm class** `Γ_n^{rad}` with the diagonal, computed in the declared category — that is, the **mass at `t = \log n` of the unique finite-place Radon measure `ω_{fin}` representing `T` on the radial sector `D_A^{rad} ∩ D_A^0`** (Thm. 3bis.7; existence and uniqueness are Def–Thm 3bis.8, uniqueness because a Radon measure is determined by its integrals against `C_c^∞` tests), whose integrand is place by place the Haar-regularized rank of the relative Hochschild shadow times the half-density–Lefschetz weight (Paper 43 Thm. 7.1, Thm. 8A.9 (8A.24)–(8A.24′)) — equals `Λ(n)n^{−1/2} = n^{−1/2}·deg_det[Z→Φ_n(1)→Z]`, the integral cotangent model of P123.037 transported to the lattice `L_S ⊂ X_S` (P123.038); the identification is of **degrees**, and an object-level identification is impossible in a `C`-linear category (P123.022)."  This mirrors the A.6 decision of Paper 43 §14.2 and was **accepted by the author on **.  **[REBUILT, phase 131, round 3 — strengthened form, now proved on objects (Thm. 6bis.4):]**  the same identity holds with `Γ_n^{rad}` replaced by the **Frobenius object** `Frob_n` (Def. 3ter.2), whose finite contact is `Λ(n)n^{−1/2}` **exactly** (Thm. 3ter.10 — no limit at the finite places, no regularization), and with the right-hand side the Möbius cofiber of the **integral shadow** `Sh_Z(Frob_n) = [L_S →n→ L_S]`, a construction on the objects themselves (Lemma 6bis.2): this is the "integral or lattice category with a complex realization" that P123.022 §2's *Scope* paragraph states must be constructed, and its complex realization is acyclic exactly as that paragraph predicts.  The identification remains one of **degrees**. |
| **B.5** | `deg_det(contact) = log|Φ_n(1)| = Λ(n)`, with `n=1` treated as identity/excess and not by that formula. |
| **B.6** | The general family proved by structure, not by extrapolation from cases; its classes and primitive components entering row A's numerical object. |
| **B.7** | The discriminating test: the linear-dilation contact `1−u^{−1}` versus the cyclotomic contact, computed with rings and valuations for `p` and `p²`; if they differ, the geometric mechanism producing the cyclotomic factor must be located. |
| **B.8** | Adversarial verification on `p, p², p³, pq, p²q, pqr`, with the index by places preserved (phase 119: grouping by norms alone loses information). |
| **B.9** | Compatibility with row A, and independence from zeros and from any positivity statement. |

B.7 is the clause that had stopped every earlier attempt.  It is settled in
Section 3.

---

## 3. The separation theorem

This is the new content.  Everything later in the paper is a consequence.

### 3.1 The two operations, stated exactly

Let `n ≥ 2`.  P123.060 constructs both of the following over `R = Z` or `Z_p`.

**The fixed-graph contact.**  On `X = Spec R[z]` with the dilation
`d_n : z ↦ nz`, the derived intersection of the graph of `d_n` with the
diagonal is the Koszul complex `K_fix(n) = [R[z] →(n−1)z→ R[z]]`, and its
transverse cotangent factor at the zero section is

    C_fix(n) = [R →(n−1)→ R],       H⁰ = R/(n−1).                    (3.1)

**The ramification contact.**  For the power map `π_n : z ↦ z^n` on `G_m`,
the relative cotangent complex pulled to the identity section is

    C_ram(n) = [Z →n→ Z],           H⁰ = Z/n,                         (3.2)

equivalently (P123.037 §2) the cotangent complex of the root fibre `μ_n`
pulled to its unit, and equivalently (P123.061 §1) the ramification complex of
the single integral deformation `F_n(t,z) = ((1+tz)^n − 1)/t`, whose generic
fibre is `π_n` in the coordinate `w = 1+tz` and whose special fibre `t=0` is
`d_n`.

P123.060 §3 proves these are not quasi-isomorphic, decisively at `n=p^k`
localized at `p`: `n−1 ∈ Z_p^×` makes (3.1) contractible, while the primitive
extraction of (3.2) has cohomology `Z/p`.

### 3.2 Why the two differentials coexist

The deformation makes the reason visible, and it costs one line.

**Lemma 3.1.**  Inside the family `F_n(t,z)` of P123.061, in the coordinate
`w = 1+tz`:

    fixed locus of the correspondence : w^{n−1} = 1, i.e. μ_{n−1};
    relative fibre over the unit      : w^n     = 1, i.e. μ_n.

*Proof.*  `1 + tF_n(t,z) = (1+tz)^n`, i.e. `F_n` is `w ↦ w^n`.  The fixed
equation `F_n(t,z) = z` reads `w^n = w`, so `w(w^{n−1}−1)=0`, and on the
invertible locus `w^{n−1}=1`.  The relative fibre `F_n(t,z)=0` reads
`w^n = 1`.  ∎  `PROVED`

So the fixed data are governed by `μ_{n−1}` and the ramification data by
`μ_n`: **the fixed group and the deck group of the same morphism**.  They are
different groups, of coprime orders.  No identification was ever available,
and none is needed.

**Remark 3.2.**  This also identifies the *geometric mechanism* demanded by
clause B.7: the cyclotomic factor is the determinant of the deck translation
on the orbit lattice, not a fixed-point determinant.  Section 6 computes it.

### 3.3 The separation theorem

**Theorem 3.3 (coprime support; the two contacts never compete).**
Let `n ≥ 2`.  Then

  (i) `supp H⁰(C_ram(n)) = V(n)` and `supp H⁰(C_fix(n)) = V(n−1)`;
  (ii) `V(n) ∩ V(n−1) = ∅`;
  (iii) for every finite place `p`,

        p | n   ⟹  |1−n|_p = 1  and  τ_p(Γ_n) = |n|_p^{1/2},
        p ∤ n   ⟹  | n |_p = 1  and  τ_p(Γ_n) = |1−n|_p^{−1};

  (iv) consequently the **principal weight**

        w(Γ_n) := ∏_{p finite} τ_p(a_S(n))

— defined as the product of the **proved local factors** of P123.042 (2.1),
  **not** as a value of Paper 43's invariant `T`; see the correction below —
  factors place-wise and canonically as

        w(Γ_n) = w_ram(Γ_n) · w_unit(Γ_n),                            (3.3)
        w_ram(Γ_n) := ∏_{p | n} τ_p(a_S(n)),
        w_unit(Γ_n) := ∏_{p ∤ n, p finite} τ_p(a_S(n)),   (over ALL finite p)

  and

        w_ram(Γ_n) = n^{−1/2} = (det C_ram(n))^{−1/2},                (3.4)
        w_unit(Γ_n) = n − 1   = # H⁰(C_fix(n)).                       (3.5)

  **[CORRECTED, phase 128 B5.]**  Both products must be taken over **all**
  finite places of `Q`, not over `S_f`: on the minimal chart
  `S = {∞} ∪ P(n)` the second product is empty, hence `1`, not `n−1`.  This is
  legitimate and canonical because `τ_p = 1` off the finite set
  `V(n) ∪ V(n−1)`, and because both products depend only on the
  gauge-invariant anchor `b_S = n` of P123.038 §2.  A chart sees the whole
  quantity as soon as `S ⊇ V(n) ∪ V(n−1)`.  **[Also, phase 128 B6:]** these are
  the **finite** parts; `a_S(n)` has `σ_∞ = 1`, where the local factor (1.1) is
  undefined, and Paper 43 handles the identity class by the declared constant
  `c` of Definition 8.6, now **declared** `c := 0` (Definition 8A.7d).
  **[REBUILT, phase 131, round 2, finding `F12`(c): the round-1 text cited
  "Paper 43 Def. 8.1 … the renormalized identity determinant (P123.012,
  P123.105)", which is the **withdrawn** Definition 8.1 of the pre-phase-129
  paper (Paper 43 §13.6); the current Definition 8.1 is the local density
  (8.1).]**  Row B's contract is about the finite contact.

  **[REBUILT, phase 131 — (iv) and (v) are statements about the LIFT.]**
  Parts (i)–(iii) are statements about the two integral complexes and about
  the local factor `τ_p` as a function on `Q_p^×`; they are unchanged.  Parts
  (iv)–(v) are statements about the **idele** `a_S(n)`, a chosen lift, and
  about nothing else.  They are **not** statements about the class
  `δ_S(1/n) = a_S(n)/n` of that idele in the carrier `C_S`, and they are
  **not** values of, or contributions to, any local term `W_v` of Paper 43's
  declared trace.  The reason is Proposition 3bis.2: the class has unit
  coordinate `1` at every finite place, and is in the image of **no** slice
  map `j_q`, `q ∈ S_f`.  Corollary 3bis.3 states the consequence.  In
  particular:

  * `w_unit(Γ_n) = n−1` is the product over `q ∤ n` of the local factors of
    the lift; it is a real and canonical number **attached to the lift**, and
    it is not a contact of anything in `G`;
  * `w_ram(Γ_n) = n^{−1/2}` is likewise computed from the lift here.  That the
    same number `n^{−1/2}` is the canonical half-density of the class, and the
    second coordinate of the bidegree `M(Γ_n^{rad}) = (n^{1/2},n^{−1/2})`, is
    an **independent** fact, proved from `|δ_S(1/n)|_S = 1/n` in Theorem
    4.4(iii) and Theorem 3bis.5(iii).  The coincidence is the product formula,
    not a transport.

  With (iv)–(v) read this way, the whole of Theorem 3.3 is correct and
  load-bearing for §§5–6 (the `Z`-linear models), and carries no claim about
  the carrier.

*Proof.*
(i) `H⁰(C_ram(n)) = Z/n` and `H⁰(C_fix(n)) = Z/(n−1)` by (3.1)–(3.2); the
support of a finite cyclic group `Z/m` in `Spec Z` is `V(m)`.

(ii) `gcd(n, n−1) = 1`.

(iii) If `p | n` then `n ≡ 0 (p)`, so `1−n ≡ 1 (p)` is a unit, `|1−n|_p = 1`,
and (1.1) gives `τ_p = |n|_p^{1/2}`.  If `p ∤ n` then `|n|_p = 1` and (1.1)
gives `τ_p = |1−n|_p^{−1}`.  The two cases are exhaustive and exclusive, and
the case distinction is a property of `n` alone, so the factorization (3.3)
involves no choice.

(iv) For (3.4): by (iii),

    w_ram(Γ_n) = ∏_{p|n} |n|_p^{1/2} = ( ∏_{p finite} |n|_p )^{1/2}
               = ( |n|_∞^{−1} )^{1/2} = n^{−1/2},

using `|n|_p = 1` for `p ∤ n` and the product formula `∏_v |n|_v = 1` for the
rational integer `n`.  And `det C_ram(n) = n = # H⁰(C_ram(n))`.

For (3.5): by (iii), `w_unit(Γ_n) = ∏_{p ∤ n}|1−n|_p^{−1}`.  Since `|1−n|_p=1`
for `p | n`, this equals `∏_{p finite}|1−n|_p^{−1}`, which by the product
formula applied to `n−1 ∈ Q^×` equals `|n−1|_∞ = n−1`.  And
`# H⁰(C_fix(n)) = #(Z/(n−1)) = n−1`.  ∎  `PROVED`

**Corollary 3.4 (what Theorem 3.3 does and does not give).**  **[CORRECTED,
phase 128 B4.]**  The first version said the two operations of P123.060 are
"both **realized** by row A's invariant".  That overstates it, and P123.060 §2
forbids exactly this reading: of the factor `p^{−k/2}` it says "the half-density
numerator comes from the dilation action.  **Neither supplies a `Z/p`
ramification contact as the cohomology of (2.1)**", and §4 forbids obtaining the
relation "by **renaming**".  Theorem 3.3 produces no complex at `p|n`; it
observes that the number `|n|_p^{1/2}` appears there.

What survives, and is correct, is the **support statement**: the two operations
have coprime support, so they never compete, and the numerical data of each
appear at disjoint sets of places with their own exponents.  That is a correct
and useful reading of P123.060 — but it is not a realization of either contact,
and the obstruction P123.060 identifies is unchanged.  ∎  `PROVED as restated`

**Remark 3.5 (why this respects phase 119).**  The factorization (3.3) exists
only place-wise.  There is no function of the norm `|a_S(n)|_S` alone that
separates `w_ram` from `w_unit`, because both are products of local factors of
the same idele.  This is precisely the phase-119 warning that grouping by
norms loses information, now turned into a positive statement: the index by
places is exactly the data that makes row B possible.

**Remark 3.6 (the classical shadow of Theorem 3.3).**  In the local form of
the Weil distribution, the integrand `1/|1−u|_v` is bounded and equal to `1`
on the set `|u|_v ≠ 1` and divergent on average on the units.  Theorem 3.3(iii)
is that dichotomy read on a single arithmetic idele: the ramified places carry
the prime terms, the unramified places carry the unit terms.  The statement
here is not that dichotomy quoted, but its proof on the A-carrier from (1.1).

**Remark 3.7 (`w` is not a value of row A's invariant).**  **[CORRECTED,
phase 128 B7.]**  The first version described `w(Γ_n)` as "the exponential of
the finite part of the `γ=1` term of the lattice sum (8.2) of Paper 43".  That
framing is unsafe.  Paper 43's `T` is *defined* by its Definition 8.1, not by
(8.2), which that paper itself states is not absolutely convergent; and its
Remark 8.6b and Definition 8A.7d say that two admissible regularizations
differ by the identity-class constant `c`, and the phase-128 form of this
remark added a term `c·log|w|`, which for
`w = a_S(n)` is `−c·log n` — exactly the magnitude row B extracts.  Paper 43
(9.1) escapes this only because it is a **difference** of two classes of
modulus one.

**[REBUILT, phase 131, round 2, finding `F12`(a): the citation "Paper 43
Lemma 8.2" for the regularization ambiguity is **stale** — that number now
belongs to the exact-orbital-values lemma (`τ_p(p^k) = p^{−|k|/2}`), and the
ambiguity statement is Remark 8.6b / Definition 8A.7d, where `c` is moreover
now **declared** to be `0`.  The substance of Remark 3.7 is unaffected,
because it never uses either.]**

**[REBUILT, phase 131.]**  Two further things are now true and were not
available in phase 128.  (1) The *reason* `w(Γ_n)` is not a value of `T` is
geometric, not analytic: the class sits on the archimedean slice and on no
finite slice (Proposition 3bis.2).  (2) There *is* a quantity attached to the
arithmetic label which **is** a value of row A's declared local terms, exactly
and with no regularization — the finite contact of the **norm** class,

    contact_{fin}(Γ_n^{rad}) = Λ(n)\,n^{−1/2}   (Theorem 3bis.7),

because `Γ_h ∈ D_A^{off}` for `0 ∉ supp h` and Paper 43 Theorem 8.8 then gives an
absolutely convergent finite sum with no counterterm and no dependence on the
constant `c`.  Lemma 8.2's ambiguity `c·\log|w|` does not arise: the objects
paired are not of modulus one, but the regularization is never invoked, since
`Γ_h` vanishes near the identity class.  So Remark 3.7's caution stands for
`w(Γ_n)` and is **not needed** for the contact of the norm class.

So `w(Γ_n)` is defined here directly as the product of the local factors of
P123.042 (2.1), which are **proved** and unambiguous: for a fixed `x` with
`x ≠ 1` and `k = v_p(1−x)` finite, `Tr(E_{MN}D_x) = |x|_p^{1/2}min(p^L,p^k)` is
exactly `|x|_p^{1/2}/|1−x|_p` for every `L ≥ k`.  Nothing in row B depends on
Paper 43's Definition 8.1, and this is deliberate: it keeps row B independent
of the open item recorded against that definition (phase 128, A2).

---

## 3bis. The norm class `Γ^rad_{(t)}`, the contact locus, and the shell volume

**[REBUILT, phase 131 — this section is new.]**  Section 3 studies the
**element** `a_S(n)` and the two `Z`-linear complexes attached to the label
`n`.  This section studies the **class** of that element in the carrier, and
then the **norm** class obtained from it by averaging over units.  The
arithmetic object of row B on the carrier is the **radial family** of norm
classes `\{Γ^{rad}_{(t)}\}_{t∈R}` together with its **contact locus**:
the objects are arithmetic-free (Lemma 3bis.3b), and the prime powers, `Λ`,
and the vanishing of `Λ` at composite labels are recovered as the support and
the atom masses of the finite-place part of row A's trace, disintegrated along
the family (Theorem 3bis.7′).  Everything the contract asks for at the level
of the carrier is proved about that family here.  **[REBUILT, phase 131,
round 2: this replaces the round-1 framing "the arithmetic object is the ideal
class", which finding `F1` of `R131.002` correctly refuted.]**

Throughout, `S` is a fixed finite chart with `∞ ∈ S` and `S_f ≠ ∅`, and we use
Paper 43 in its post-phase-130 state, where it carries the label
`WEIL-STRENGTH-COMPLETE` **on its declared carrier** (Paper 43 §14.0a–b: fixed
finite chart, chart system and colimit as additional structure, invertible
sector; A.6 under the  amendment, A.8 with target `Pic_b(B_T)`; no
sign, `𝓝_∞^W = 0` not claimed).  Every citation below is to a theorem inside
that carrier.

### 3bis.1 The class of the element, computed

**Lemma 3bis.1 (the class of `a_S(n)` has unit coordinate `1`).**  Let
`n ≥ 1` and `S ⊇ {∞} ∪ P(n)`.  In the coordinates of Paper 43 Lemma 3.3,

    C_S ≅ ker φ = R^× × ∏_{p∈S_f} Z_p^× ,   φ(x) = ∏_{p∈S_f} p^{v_p(x_p)},

the class of the idele `a_S(n) = (1 at ∞; n at each p ∈ S_f)` is

    δ_S(1/n) := a_S(n)/φ(a_S(n)) = ( 1/n at ∞ ; 1 at every p ∈ S_f ),  (3bis.1)

and `|δ_S(1/n)|_S = 1/n`.

*Proof.*  `φ(a_S(n)) = ∏_{p∈S_f} p^{v_p(n)} = n`, which is a positive `S`-unit
because `S ⊇ P(n)`; so `n ∈ Γ_S` and `a_S(n)/n` is the canonical
representative of the class furnished by the splitting `A_S^× = Γ_S × ker φ`
of Paper 43 Lemma 3.3.  Its archimedean coordinate is `1/n` and its
`p`-coordinate is `n/n = 1` for every `p ∈ S_f`.  Finally `|x|_S = |x_∞|` on
`ker φ` (Lemma 3.3), so `|δ_S(1/n)|_S = 1/n`.  ∎  `PROVED`

This is the first correction of phase 131, and it is the one everything else
follows from: **the finite coordinates of the class are `1`, not `n`.**  The
number `n` survives only in the archimedean coordinate and in the modulus.

**Proposition 3bis.2 (the element class lies on the archimedean slice and on
no finite slice).**  Let `n ≥ 2` and `|S_f| ≥ 2`.  With the slice maps (9.5b)
of Paper 43,

    j_q(q^k w) = ( q^{−k} at ∞, w at q, q^{−k} at every other place of S ),
    j_∞(x)    = ( x at ∞, 1 at every finite place of S ),

we have

  (i) `δ_S(1/n) = j_∞(1/n) ∈ Im j_∞`;
  (ii) `δ_S(1/n) ∉ Im j_q` for **every** `q ∈ S_f` — in particular for every
       `q ∤ n`, but also for `q | n`;
  (iii) there is a neighbourhood basis of `δ_S(1/n)` in `C_S` consisting of
       open sets disjoint from `⋃_{q∈S_f} Im j_q`.

*Proof.*  (i) is the displayed formula for `j_∞` with `x = 1/n`.

(ii) Suppose `δ_S(1/n) = j_q(q^k w)`.  Pick `r ∈ S_f ∖ {q}` (possible since
`|S_f| ≥ 2`).  The `r`-coordinate of `j_q(q^k w)` is `q^{−k}`, and that of
`δ_S(1/n)` is `1`, so `q^{k} = 1` in `Z_r^×`, i.e. `k = 0`.  Then the
archimedean coordinate of `j_q(w)` is `q^0 = 1`, while that of `δ_S(1/n)` is
`1/n ≠ 1`.  Contradiction.

(iii) Fix `q ∈ S_f` and `r ∈ S_f∖{q}`.  Consider the basic open sets

    N_{ε,m} := { x : |x_∞ − 1/n| < ε } × ∏_{p∈S_f} (1 + p^m Z_p) ,

a neighbourhood basis of `δ_S(1/n)` (the classes are written multiplicatively
against the representative (3bis.1)).  A point `j_q(q^kw) ∈ N_{ε,m}` must have
`q^{−k} ∈ (1/n−ε, 1/n+ε)`; for `ε < 1/(2n)` at most one integer `k` qualifies,
and there is such a `k` only if `q^{−k}` is that close to `1/n`.  If no such
`k` exists the intersection is empty.  If `k` exists, the `r`-coordinate of
the point is `q^{−k}`, and we need `q^{−k} ∈ 1 + r^m Z_r`.  Now `q^{−k} ≠ 1`
(else `q^{-k}=1` forces `k=0` and then `|1 − 1/n| < ε < 1/(2n)` is false for
`n ≥ 2`), and `q^{−k} ∈ Z_r^×` since `r ≠ q`, so `v_r(q^{−k} − 1)` is a finite
integer `m_0`; taking `m > m_0` makes the condition fail.  Doing this for the
finitely many `q ∈ S_f` and taking the largest `m` gives (iii).  ∎  `PROVED`

**Remark 3bis.2a (the minimal chart `|S_f| = 1`, and why the dichotomy does
not depend on it).**  **[REBUILT, phase 131, round 2, finding `F8` of
`R131.002` = `F3` of `R131.003`.]**  Proposition 3bis.2(ii)–(iii) **fails**
for `|S_f| = 1`: if `S_f = \{p\}` and `n = p^k`, then
`j_p(p^k·1) = (p^{−k}\text{ at }∞;\ 1\text{ at }p) = δ_S(1/n)` exactly, so
the element class **does** lie on the finite slice.  Since `S = \{∞,p\}` is
the minimal legitimate chart for `n = p^k`, this is not a vacuous case, and
the hypothesis `|S_f| ≥ 2` is carried in every statement below and in every
informal restatement (banner, §0, §9, §9bis).  Three things must be said.

  (i) *The `n−1` still does not appear on the minimal chart, for a second and
      independent reason.*  On `S = \{∞,p\}` the product defining
      `w_unit(Γ_n)` over `q ∈ S_f`, `q ∤ n`, is **empty**, hence `1`; this is
      exactly the phase-128 `B5` correction recorded inside Theorem 3.3.  The
      number `n−1` appears only when the product is taken over **all** finite
      places of `Q`, i.e. over places the chart does not contain.  So on every
      chart the conclusion is the same — the class contributes no `n−1` — but
      the reason differs: emptiness of the product at `|S_f| = 1`, absence
      from every slice at `|S_f| ≥ 2`.
  (ii) *The element/norm-class dichotomy is chart-independent.*  Even at
      `|S_f| = 1`, where `δ_S(1/n) ∈ Im\,j_p`, the **element point class**
      still has finite contact `0`: by (8.5) the shell term integrates
      `a = F∘j_p` over `p^kZ_p^×` against `d^*x`, whose restriction to the
      shell is `\log p` times the **probability** Haar measure of `Z_p^×`, and
      a point mass at the single unit `u = 1` is a set of measure zero for it.
      Only the **unit-spread** class — the norm class `Γ_n^{rad}`, which is
      Haar on the whole shell — receives the shell volume `\log p`.  So the
      statement "the element does not have the contact; the unit average does"
      holds on every chart, for two different reasons, and it is the statement
      §9bis W1 actually rests on.
  (iii) *The dissolution of the `n−1` obligation is therefore unconditional*,
      while the sharp geometric form of Proposition 3bis.2 — "the class is on
      no finite slice" — is a **large-chart phenomenon**, true exactly when
      `|S_f| ≥ 2`.  Both are stated with their hypotheses wherever they are
      used.

**Corollary 3bis.3 (`w_unit` is a property of the lift, not a contact).**
**[REBUILT, phase 131.]**  Let `n ≥ 2`, `|S_f| ≥ 2`.  Let `F ∈ D_A` be
supported in one of the neighbourhoods of Proposition 3bis.2(iii).  Then
`W_q(F) = 0` for every `q ∈ S_f`, and `T(F) = W_∞(F)` (with `c := 0`,
Paper 43 Def. 8A.7d).

Consequently the quantity

    w_unit(Γ_n) = ∏_{q ∤ n} |1 − n|_q^{−1} = n − 1

of Theorem 3.3(v) is the product of the local factors of the **idele
`a_S(n)`**, i.e. of a chosen **lift**, evaluated at the places `q ∤ n`.  It is
**not** the contribution of the class `δ_S(1/n)` to any local term `W_q` of
row A's trace, because the class is not in the image of the slice map `j_q`
and a test concentrated at it meets no finite shell and no finite unit packet.
The same remark applies to `w_ram(Γ_n) = n^{−1/2}`: it is a number attached to
the lift, and §3bis.3 below recovers `n^{−1/2}` at the class by a different
and independent route (the half-density of the modulus).

*Proof.*  By (8.5) of Paper 43, `W_q(F)` is an integral of `a = F∘j_q` over
`Q_q^×` (shell part plus unit packet).  If `supp F` misses `Im j_q` then
`a ≡ 0` and `W_q(F) = 0`.  Proposition 3bis.2(iii) provides such supports.
Definition 8.6 of Paper 43 then leaves `T(F) = W_∞(F) + c·F(1)`, and `c = 0`.
The statement about `w_unit` is Theorem 3.3(v) read together with this.  ∎
`PROVED`

**Remark 3bis.3a.**  Phase 128 finding `B7` already recorded that `w(Γ_n)` is
not a value of row A's invariant `T` (Remark 3.7).  Corollary 3bis.3 supplies
the **reason**, which is geometric and not analytic: the class is on the wrong
slice.  This is what dissolves the obligation Paper 44 §9.2 handed to row C;
see §9 and §9bis.

### 3bis.2 The norm class

**[REBUILT, phase 131, round 2 — renamed, after finding `F1` of `R131.002`.]**
The previous version called the object of Definition 3bis.4 "the ideal class".
That name is wrong and it inflated what §§B.1–B.2 mean.  The adversarial audit's
argument is correct and is adopted here as mathematics:

**Lemma 3bis.3b (why "ideal" is the wrong word).**  Let `S ⊇ {∞}∪P(n)`.  Then
`n ∈ Γ_S = Z_S^×`, so `nZ_S = Z_S` is the **unit** ideal, and the ideal class
group of `Z_S` is trivial (every ideal of a localization of `Z` is principal,
and `C_S` has no ideal class group to speak of).  Moreover the assignment
`n ↦ Γ_n^{rad}` factors as

    (N_{≥1},×)  ↪  (R_{>0},×)  ≅  {level-set Haar measures on C_S} ,  (3bis.2a)

the second map being an isomorphism of topological monoids; so **as an
object**, `Γ_n^{rad}` forgets the factorization of `n` completely, and
`Γ_6^{rad}` is structurally indistinguishable from `Γ_t^{rad}` for any real
`t > 0`.

*Proof.*  `Γ_S` is the group of positive rationals supported on `S_f`
(Paper 43 Lemma 3.3), and `P(n) ⊆ S_f`, so `n ∈ Γ_S` and `n` is invertible in
`Z_S`.  For (3bis.2a): by Paper 43 Lemma 3.3, `|·|_S : C_S → R_{>0}` is a
surjective homomorphism with kernel `K^♮` (3bis.2), so `C_S/K^♮ ≅ R_{>0}`, and
`r ↦ μ_{r^{-1}K^♮}` (normalized Haar measure of the fibre) is a monoid
isomorphism onto the level measures by the coset computation of
Theorem 3bis.5(i).  ∎  `PROVED`

So the correct name is **norm class** (equivalently *level class* or *modulus
class*): `Γ^{rad}_{(t)}` is the normalized Haar measure of the level set
`{|x|_S = e^{−t}}`, defined for every `t ∈ R`, and `Γ_n^{rad} :=
Γ^{rad}_{(\log n)}` is its value at an integer label.  **The arithmetic is not
in the objects.**  It is in the *contact locus* of the one-parameter family —
the support and the atom masses of the measure `ω_{fin}` — which is
Theorem 3bis.7′ below.  Every occurrence of "ideal class" in the previous
version is replaced by "norm class"; the honest reading of B.1, B.2 and the
first half of B.6 is stated in Remark 3bis.5b and in the §10 ledger.

**Definition 3bis.4 (the norm class).**  Let

    K^♮ := {±1} × ∏_{p∈S_f} Z_p^×  ⊂  C_S                          (3bis.2)

be the maximal compact subgroup of `C_S ≅ R^× × ∏_{p∈S_f}Z_p^×`, with its
normalized Haar **probability** measure `du`.  For `t ∈ R` define the **norm
class**

    Γ^{rad}_{(t)} := the normalized Haar probability measure of the level set
                     { x ∈ C_S : |x|_S = e^{−t} } ,                  (3bis.3)

a compactly supported Radon probability measure on `C_S`, and write

    Γ_n^{rad} := Γ^{rad}_{(\log n)} = ∫_{K^♮} δ_S(1/n)·u \, du       (3bis.3′)

for the value at an integer label `n ≥ 1`, the coset `δ_S(1/n)·K^♮` being
exactly the level set `{|x|_S = 1/n}`.  `{Γ^{rad}_{(t)}}_{t∈R}` is the
**radial family**; `t` is its label, and the object depends on `t` only.

**[REBUILT, phase 131 — a correction to the averaging group.]**  The average
must be taken over `K^♮`, which contains the archimedean sign factor `{±1}`,
and not only over `∏_{p∈S_f}Z_p^×`.  Two things force this.  First, only then
is the support of `Γ_n^{rad}` the **whole** level set `{|x|_S = 1/n}`, which is
what makes composition (Theorem 3bis.5(i)) a one-line Haar computation.
Second, the archimedean contact of Theorem 3bis.8 is the **half-sum**
`½[τ_∞(1/n)+τ_∞(−1/n)]`; the two signs are both present and carry the two
archimedean densities (8.5a) of Paper 43.

**Remark 3bis.4a (what the coset is, corrected).**  **[REBUILT, phase 131,
round 2, finding `F1`.]**  The previous version read this as "the average over
all generators of the ideal `(n)`", which is vacuous because `(n) = Z_S`
(Lemma 3bis.3b).  The correct statement is the weaker one, and it is all that
is used: the ideles `a ∈ A_S^×` with `φ(a) = n` and `|a|_S = 1/n` — the lifts
of `a_S(n)` with the declared archimedean normalization — are exactly
`a = (u_∞ ; (u_p n)_p)` with `u_∞ ∈ {±1}`, `u_p ∈ Z_p^×`, and their classes
are exactly `δ_S(1/n)·u`, `u ∈ K^♮`; so `Γ_n^{rad}` is the unit average of the
classes of all such lifts, and **the coset depends only on the modulus**
`|a|_S = 1/n`.  That is the whole content: the averaging kills the unit part
of the lift, and what remains is the level set.  In terms of the
element realization (4.2) and of Paper 43 Corollary 3.4 (`F ↦ E_F`),

    Γ_n^{rad} = ∫_{K^♮} E_u ⋆ Γ_n \, du                              (3bis.4)

in the sense of measures on `C_S`, because `E_u ⋆ Γ_n` is the class
`δ_S(1/n)·u` by `E_uE_v ≅ E_{uv}`.  What (3bis.4) does *not* say is that the
right-hand side remembers `n` as an object: by Lemma 3bis.3b it remembers only
`|a_S(n)|_S`.

**Remark 3bis.4b (the type of `Γ_n^{rad}`: a multiplier, not an element).**
**[REBUILT, phase 131.  This corrects the earlier blueprint, which asserted
that `Γ_n^{rad}` "lies in the Fell completion of `G` … a continuous compactly
supported section".  It does not: (3bis.3) is a point mass in the archimedean
coordinate, hence not a continuous function of `x_∞`, and `D_A = C_c^∞(C_S)`
requires smoothness there (Paper 43 Def. 8.5).]**  The correct statement is:

  (i) `Γ_n^{rad} ∉ D_A`;
  (ii) `Γ_n^{rad}` is a **multiplier** of `D_A`: convolution with it maps
       `D_A` continuously into the radial subalgebra
       `D_A^{rad} := {F ∈ D_A : F is K^♮-invariant}`, since
       `(Γ_n^{rad}⋆G)(x) = ∫_{K^♮} G(u^{−1}δ_S(n)x)du` is smooth in `x_∞`
       (differentiation under a finite measure), `K^♮`-invariant, and
       compactly supported;
  (iii) `Γ_n^{rad}` **is** an element of the completion `N_A^{dist}` of
       Paper 43 Theorem 9.14, and that is where row B's classes live; this is
       Theorem 8.3 below.

This is the same type distinction Paper 43 Remark 8.11 makes for the diagonal
`Δ = E_1`, which is a multiplier of the Fell core and not an element of it.
Indeed `Γ_1^{rad}` is the Haar measure of `K^♮` and is the unit-averaging
projector, which is the identity of `D_A^{rad}` and **not** the identity of
`D_A`.

**Theorem 3bis.5 (B.2, B.3 for the norm classes: monoidality, dagger,
bidegree, and independence of all choices).**  Let `m,n ≥ 1` and `s,t ∈ R`.
Then:

  (i) *Monoidality.*  `Γ_m^{rad} ⋆ Γ_n^{rad} = Γ_{mn}^{rad}`, and
      `Γ_1^{rad} = Δ^{rad}` is the unit-averaging projector, the identity of
      `D_A^{rad}` and of the monoid `{Γ_n^{rad}}`.  Hence
      `n ↦ Γ_n^{rad}` is a strong monoidal functor from the monoid
      `(N_{≥1}, ×)` to the convolution monoid of `K^♮`-invariant compactly
      supported probability measures on `C_S`.
  (ii) *Dagger, and the `†`-monoid it forces.*  **[REBUILT, phase 131,
      round 2, finding `F7`.]**  `Γ^{rad}_{(t)\,†} = Γ^{rad}_{(−t)}` and
      `(Γ^{rad}_{(s)}⋆Γ^{rad}_{(t)})^† = Γ^{rad}_{(−s)}⋆Γ^{rad}_{(−t)}`.  In
      particular `(Γ_n^{rad})^† = Γ^{rad}_{(−\log n)}`, the norm class of
      modulus `n`, which is **not** in `\{Γ_m^{rad} : m ∈ N_{≥1}\}`.  So the
      realized family is **not** `†`-stable: the smallest `†`-stable
      submonoid of the radial family containing all `Γ_n^{rad}` is indexed by
      `Q_{>0}^×` (labels `n` and `1/n` and their products), inside the full
      radial family indexed by `(R,+) ≅ (R_{>0},×)`.  Clause B.3's
      "transposition preserved by the realization" is therefore proved for
      the `†`-monoid `(Q_{>0}^×, ×, (\,)^{-1})`, and clause B.1's source
      category `W = (N_{≥1},×)`, as declared in Definition 4.1, **has no
      dagger**; the honest statement is that the realization extends
      canonically from `W` to its group completion `Q_{>0}^×` and the dagger
      is realized there.  *Deleted in round 2:* the sentence "each
      `Γ_n^{rad}` is `†`-real in the sense that it is a positive measure".
      That is a non sequitur — `†`-real means `μ^† = μ`, which is **false**
      for every `n ≥ 2`, since `Γ^{rad}_{(\log n)} ≠ Γ^{rad}_{(−\log n)}`.
      The only `†`-fixed member of the family is `Γ_1^{rad} = Δ^{rad}`, and
      `Δ^{rad\,†} = Δ^{rad}` because `K^♮` is a group.
  (iii) *Bidegree.*  With the Tate functionals (9.2) of Paper 43,

        M(Γ_n^{rad}) = (λ_−, λ_+)(Γ_n^{rad}) = ( n^{1/2}, n^{−1/2} )
                     = n^{−1/2}·(n, 1) ,                             (3bis.5)

      multiplicative in `n` and exchanged by `†` under the swap `♯`.  The
      half-density normalization `n^{−1/2}` is the canonical one of Paper 43
      §5.2 and is forced by the product formula.
  (iv) *Independence.*  `Γ_n^{rad}` is independent of the lift, of the gauge
      `γ ∈ Γ_S`, of the uniformizers and of the chart: for `S ⊆ T`,
      `(π_{TS})_*Γ_n^{rad}(T) = Γ_n^{rad}(S)` and `Γ_n^{rad}(T)` is the
      inflation of `Γ_n^{rad}(S)`, so the family is defined on the colimit
      `D_A^∞` of Paper 43 (8A.22).  Moreover `Γ_n^{rad}` is defined for every
      chart `S`, including charts with `P(n) ⊄ S_f`.

*Proof.*  (i)  Let `K := K^♮`, a compact subgroup, and let `μ_{aK}` denote the
normalized Haar measure of a coset.  `μ_{aK} ⋆ μ_{bK}` is the image of
`μ_K ⊗ μ_K` under `(u,v) ↦ abuv`; since `u,v` are independent Haar on `K` and
`K` is a compact group, `uv` is Haar on `K`; so the image is `μ_{abK}`.  With
`a = δ_S(1/m)`, `b = δ_S(1/n)` and `δ_S(1/m)δ_S(1/n) = δ_S(1/mn)` (immediate
from (3bis.1)) this is `Γ_m^{rad}⋆Γ_n^{rad} = Γ_{mn}^{rad}`.  For `n = 1` the
coset is `K` itself and `μ_K⋆F` is the `K`-average of `F`, which is the
identity on `K`-invariant `F` and a projector in general.  Strong
monoidality is then the statement that the isomorphisms are equalities, and
associativity and unit coherence are those of convolution of measures on the
locally compact abelian group `C_S`.

(ii)  `†` on measures is the push-forward along `x ↦ x^{−1}` composed with
complex conjugation (Paper 43 (8.2)); the level measures are real, and
`\{|x|_S = e^{−t}\}^{−1} = \{|x|_S = e^{t}\}`, with Haar measure carried to
Haar measure by the inversion automorphism of `C_S`.  Anti-multiplicativity is
commutativity of `C_S`.  `Δ^{rad\,†} = Δ^{rad}` because `(K^♮)^{−1} = K^♮`.
Non-`†`-stability of `\{Γ_n^{rad}\}_{n∈N}`: `Γ^{rad}_{(−\log n)} =
Γ^{rad}_{(\log m)}` would force `\log m = −\log n`, i.e. `mn = 1`, i.e.
`m = n = 1`.  The `†`-stable submonoid generated by the `Γ_n^{rad}` is the
image of `Q_{>0}^×` under (3bis.2a), because the group generated by
`\{\log n\}` inside `(R,+)` is `\log Q_{>0}^×`.

(iii)  `λ_∓(μ) = ∫_{C_S}|x|_S^{∓1/2}dμ(x)` by (9.2), and `|x|_S ≡ 1/n` on the
support of `Γ_n^{rad}`, a probability measure; so `λ_∓ = n^{±1/2}`, i.e.
`λ_− = n^{1/2}`, `λ_+ = n^{−1/2}`.  Multiplicativity follows from (i) or
directly.  `λ_∓(F^†) = conj(λ_±(F))` is Paper 43 Theorem 9.1, and here gives
the swap.  That `n^{−1/2}` is the canonical half-density is Theorem 4.4(iii)
together with `|δ_S(1/n)|_S = 1/n` (Lemma 3bis.1).

(iv)  *Lift and gauge.*  By Remark 3bis.4a the support of `Γ_n^{rad}` is the
set of classes of **all** admissible lifts, and the measure is the Haar
measure of that set; so no lift is preferred.  A gauge change `a ↦ γa`,
`γ ∈ Γ_S`, does not move the class at all (Paper 43 Lemma 3.3).  This is the
exact point at which the lift ambiguity of P123.018 §2 is removed: that note
exhibits two lifts of one class whose extensions by one to a larger chart are
**not** equivalent; the averaged object (3bis.3) is defined by the modulus
alone, which is a chart-independent function (Paper 43 Lemma 3.3,
Theorem 8A.7c(d)), so the ambiguity has no purchase on it.
*Charts.*  **[REBUILT, phase 131, round 2, finding `F10`.]**  The round-1
proof argued through a push-forward along "the coordinate projection
`π_{TS} : C_T → C_S`".  That map is the projection of the *coordinate models*
supplied by Lemma 3.3's splitting; on ideles the projection
`A_T^× → A_S^×` does **not** carry `Γ_T` into `Γ_S` (a `T`-unit `q ∉ S_f` maps
to a non-`S`-unit), and P123.018 §2 says so explicitly.  The clause is
therefore re-proved without it.

`Γ^{rad}_{(t)}(S)` is **defined** by the single equation `|x|_S = e^{−t}`.  By
Paper 43 Lemma 3.3, `|x|_S = |x_∞|` on `C_S`, and by Paper 43
Theorem 8A.7c(d), for `S ⊆ T` the modulus `|·|_T` on `C_T` and `|·|_S` on
`C_S` are both the modulus of the archimedean coordinate and Haar measure is
`dt ⊗ (\text{probability})` on both.  Hence:

  * the defining condition is chart-invariant, so the family `{Γ^{rad}_{(t)}}`
    is defined in every chart by the same equation, with no comparison map
    needed;
  * the **inflation** `J_{ST}` of Paper 43 §3.3bis — pullback along the chart
    retraction, which is the direction the colimit `D_A^∞` (8A.22) actually
    uses — carries `Γ_h(S)` to `Γ_h(T)` for every `h`, because
    `Γ_h = h∘(−\log|·|)` is a function of the modulus and `J_{ST}` preserves
    it; so the smeared classes are a family over the colimit, and `T_∞` is
    defined on them (Theorem 3bis.7, last paragraph);
  * consequently `M(Γ^{rad}_{(t)})` and all the trace values computed below
    are chart-invariant in the exact sense of Theorem 8A.7c(c)–(d).

No statement about a descent of ideles along `A_T^× → A_S^×` is made or
needed.  Finally (3bis.3) refers to `n` only through the real number `1/n`, so
it makes sense in every chart, including charts with `P(n) ⊄ S_f`.  ∎
`PROVED`

**Remark 3bis.5a (what is realized and what is not).**  Theorem 3bis.5 realizes
the **monoid** `(N_{≥1},×)` and nothing more.  The divisor arrows of the
source category `W` (Definition 4.1) still have no image: Paper 43 (3.3)
(P123.082) kills morphisms between distinct external classes, and averaging
does not create any.  Clause B.1 is discussed in §10 with this sentence
attached.

**Remark 3bis.5b (the honest reading of B.1, B.2 and B.6's first half).**
**[REBUILT, phase 131, round 2, finding `F1`.]**  Theorem 3bis.5 is true with
`n` replaced by any positive real, because by Lemma 3bis.3b the realization
factors through `(R_{>0},×)`.  It therefore proves *nothing arithmetic on its
own*, and the following is the exact statement of what row B realizes and
where the arithmetic sits.

  (a) **Realized as objects:** the monoid `(N_{≥1},×)` embedded in the modulus
      group `(R_{>0},×)`, with composition, unit, dagger (on the group
      completion `Q_{>0}^×`, Theorem 3bis.5(ii)) and half-density.  The
      objects forget factorization.
  (b) **Realized on the integral model:** the divisor poset, strictly, on the
      index complexes `Q_{S,·}` of P123.038 §3 (Theorem 4.3(b), Remark 5.6).
      Not in `G`.
  (c) **Detected on the carrier, not carried by the objects:** the
      factorization of `n`, through the **contact locus** of the radial
      family — the support and the atom masses of `ω_{fin}` (Theorem 3bis.7′).
      The divisor structure appears there as
      `Σ_{d|n}Λ(d) = \log n`, the sum of the atoms of `ω_{fin}` over the
      moduli of the divisors of `n` (Theorem 3bis.10(ii)).
  (d) Consequently, for composite `n` the object `Γ_n^{rad}` is structurally
      indistinguishable from a generic `Γ^{rad}_{(t)}`, and the statement "the
      finite contact vanishes at composite `n`" is a statement about the
      contact locus, **not** a property the object carries.  The §10 ledger
      says so on the B.2 and B.6 rows.

**Remark 3bis.5c (smeared classes versus point classes; clause B.2's target).**
**[REBUILT, phase 131, round 2, finding `F4`.]**  Clause B.2 asks for "a
realization into row A's category".  There are two levels and they land in
different objects of Paper 43, exactly as Paper 43 Remark 3.5 requires:

  * the **smeared** classes `Γ_h` (Definition 3bis.6) lie in
    `D_A^{rad} ⊂ D_A`, hence — via `F ↦ E_F` (Paper 43 Corollary 3.4) and
    Definition 8A.1 — in `Corr_A^{tr}`; monoidality `Γ_h ⋆ Γ_g = Γ_{h∗g}` is
    literal there (Lemma 3bis.6a), so B.2 is satisfied **inside row A's
    category** on this level;
  * the **point** classes `Γ^{rad}_{(t)}` are multipliers of `D_A`, not
    elements (Remark 3bis.4b), and live in the completion `N_A^{dist}`
    (Theorem 8.3); B.2's monoidality for them is Theorem 3bis.5(i), an
    identity of measures, and it is compatible with the smeared level by
    `Γ_h = ∫h(t)Γ^{rad}_{(t)}dt`.

No statement proved at one level is transported to the other without this
dictionary, which is Paper 43 Remark 3.5's discipline.

### 3bis.3 The contact locus of the radial family

**[REBUILT, phase 131, round 2.]**  By Remark 3bis.5b the objects carry no
arithmetic.  This subsection proves where the arithmetic *is*: in the contact
locus of the one-parameter family `\{Γ^{rad}_{(t)}\}_{t∈R}` with the diagonal,
i.e. in the support and the atom masses of the finite-place part of row A's
trace, disintegrated along the family.  The classes `Γ^{rad}_{(t)}` are not
test functions, so the disintegration is taken through the smeared family; the
finite part turns out to be a purely **atomic** measure and the archimedean
part a **continuous density**.  The distinction is not cosmetic
(Remark 3bis.8a).

**Definition 3bis.6 (the smeared norm classes).**  For `h ∈ C_c^∞(R)` put

    Γ_h(x) := h(−\log|x|_S) ,     x ∈ C_S .                          (3bis.6)

**Lemma 3bis.6a.**  `Γ_h ∈ D_A^{rad}`; `Γ_h = ∫_R h(t)\,Γ^{rad}_{(t)}\,dt`;
`Γ_h ⋆ Γ_g = Γ_{h∗g}` with `∗` additive convolution on `R`;
`Γ_h^† = Γ_{h^∨}`, `h^∨(t) = conj(h(−t))`; `λ_∓(Γ_h) = ∫_R h(s)e^{±s/2}ds`;
and if `0 ∉ supp h` then `Γ_h ∈ D_A^{off}`.

*Proof.*  Membership: `|x|_S = |x_∞|` (Paper 43 Lemma 3.3), so `Γ_h` is a
smooth function of `x_∞` on `R^×`, is constant (hence locally constant) in the
compact coordinates, and is supported in
`\{e^{−b} ≤ |x_∞| ≤ e^{−a}\}×∏Z_p^×` for `supp h ⊆ [a,b]`, a compact subset of
`C_S`.  The integral formula and the `λ_∓` formula are the disintegration
`d^*w = dt ⊗ du` of Haar measure on `C_S` in the coordinate `t = \log|w|_S`,
with `du` the probability Haar measure of `K^♮` (this is the normalization
established in the proof of Paper 43 Theorem 9.14a, where `d^*x_∞ = dx/(2|x|)`
gives the two signs total mass one and each `Z_q^×` has mass one):
`λ_∓(Γ_h) = ∫_R h(−t)e^{∓t/2}dt = ∫_R h(s)e^{±s/2}ds`.  Convolution:
`(Γ_h⋆Γ_g)(x) = ∫h(−\log|y|_S)g(−\log|x|_S+\log|y|_S)d^*y
= ∫_R h(−σ)g(−\log|x|_S+σ)dσ = (h∗g)(−\log|x|_S)`.  Dagger is (8.2).  The last
clause: `|x|_S` near `1` means `−\log|x|_S` near `0`, and `h` vanishes there,
so `Γ_h` vanishes on a neighbourhood of the identity class.  ∎  `PROVED`

**Theorem 3bis.7 (the trace on the radial sector; the finite contact is the
shell volume).**  Let `h ∈ C_c^∞(R)` with `0 ∉ supp h`, and let `c := 0`
(Paper 43 Definition 8A.7d).  Then `T(Γ_h)` is an absolutely convergent finite
sum, with **no regularization and no counterterm**, and

    T(Γ_h) = Σ_{p∈S_f} Σ_{k≥1} (\log p)\,p^{−k/2}\,[\,h(k\log p)+h(−k\log p)\,]
             + ∫_R K(|t|)\,h(t)\,dt                                  (3bis.7)

           = Σ_{n≥2,\ n=p^k,\ p∈S_f} Λ(n)\,n^{−1/2}[\,h(\log n)+h(−\log n)\,]
             + ∫_R K(|t|)\,h(t)\,dt ,                                (3bis.7′)

with `K(t) = e^{−t/2}/(1−e^{−2t})` as in (8.5∞).  Here

    Λ(p^k) = \log p = vol_{d^*x}(\,p^kZ_p^×\,) ,                      (3bis.8)

the **multiplicative Haar volume of the valuation shell** `p^kZ_p^×`
(P123.042 §1), and `Λ(n) = 0` for composite `n` because no single place has a
shell of modulus `1/n`.  On the colimit `D_A^∞` with the chart-invariant trace
`T_∞` (Paper 43 Theorem 8A.7c) the restriction `p ∈ S_f` disappears and the
sums run over all prime powers `n` with `|\log n| ≤ R(Γ_h)`.

*Proof.*  By Lemma 3bis.6a, `Γ_h ∈ D_A^{off}`, so Paper 43 Theorem 8.8 applies:
`T(Γ_h) = Σ_{v∈S}∫_{Q_v^×}Γ_h(j_v(x))τ_v(x)d^*x`, absolutely convergent, with
no `c` term and no counterterm.

*Finite places.*  By (9.5b), `j_p(p^kw) = (p^{−k}` at `∞`, `w` at `p`,
`p^{−k}` at every other place of `S)`.  This lies in `ker φ` (its valuation is
`0` at every place of `S_f`), so `|j_p(p^kw)|_S = p^{−k}` by Lemma 3.3, and

    a(p^kw) := Γ_h(j_p(p^kw)) = h(-\log p^{−k}) = h(k\log p),

**independent of `w`**.  Two consequences.  (1) The unit packet of (8.5)
vanishes identically: for `k = 0`, `a(u) = h(0) = a(1)` for every `u ∈ Z_p^×`,
so `∫_{Z_p^×}(a(u)−a(1))/|1−u|_p\,du = 0`.  This is a property of **radial**
sections, it is **pointwise**, and it needs no smallness hypothesis.  (*Aside,
used nowhere:* in Fourier terms this is the case `κ_p = 1`, where `c(1) = 0`
in Paper 43 (9.14).  **[REBUILT, phase 131, round 2, finding `F12`(b): (9.14)
is a statement about the coefficient of a **character**, so it is an analogy,
not the reason; the direct argument above is the proof and is self-contained.]**)  (2) The shell part is, by Paper 43
Lemma 8.2(i) (`τ_p = p^{−|k|/2}`, constant on the shell) and
`vol_{d^*x}(p^kZ_p^×) = \log p` (P123.042 §1),

    Σ_{k≠0}(\log p)p^{−|k|/2}h(k\log p)
        = Σ_{k≥1}(\log p)p^{−k/2}[h(k\log p)+h(−k\log p)] ,

a finite sum because `supp h` is compact.

*The archimedean place.*  `j_∞(x) = (x` at `∞`, `1` at every finite place`)`,
so `|j_∞(x)|_S = |x|` and, in the coordinate `x = ±e^t`,
`b(t) := Γ_h(j_∞(±e^t)) = h(−t)`, the same for both signs.  By Paper 43
Remark 8.6a with the declared measure `d^*x_∞ = dx/(2|x|)` of (8.5b),

    ∫_{R^×}Γ_h(j_∞(x))τ_∞(x)\,d^*x_∞ = ∫_0^∞K(t)[b(t)+b(−t)]dt
        = ∫_0^∞K(t)[h(−t)+h(t)]dt = ∫_R K(|t|)h(t)dt .

*Grouping.*  Setting `n = p^k` turns `(\log p)p^{−k/2}` into `Λ(n)n^{−1/2}`,
which is (3bis.7′); and (3bis.8) is the identification of `\log p` as the
shell volume just used.  Composite `n` contributes nothing because
`n = p^k` has at most one solution and none when `n` has two prime divisors.

*Colimit.*  Theorem 8A.7c(b) of Paper 43 adds, for each prime `ℓ ∉ S_f` with
`\log ℓ ≤ R(Γ_h)`, exactly the term
`(\log ℓ)Σ_{k≠0}ℓ^{−|k|/2}Γ_h(δ_S(ℓ^{−k}))`, and
`Γ_h(δ_S(ℓ^{−k})) = h(k\log ℓ)` since `|δ_S(ℓ^{−k})|_S = ℓ^{−k}`; this is the
missing part of the sum, and Theorem 8A.7c(a)(c) says nothing else is added.
∎  `PROVED`

**Definition–Theorem 3bis.8 (the representing measures, and the two
invariants).**  **[REBUILT, phase 131, round 2, finding `F2`: existence and
uniqueness of the representing measures is now stated as the theorem it is,
and the word "contact" is attached only to the atom.]**  There are a
unique Radon measure `ω_{fin}` and a unique continuous density `ω_∞` on
`R∖\{0\}` with

    Σ_{p∈S_f}W_p(Γ_h) = ∫ h\,dω_{fin} ,   W_∞(Γ_h) = ∫ h\,ω_∞ ,
    for all h ∈ C_c^∞(R∖\{0\}) ,

namely, by Theorem 3bis.7,

    ω_{fin} = Σ_{n=p^k,\ p∈S_f} Λ(n)n^{−1/2}(δ_{\log n} + δ_{−\log n}) ,
    ω_∞     = K(|t|)\,dt .                                           (3bis.9)

Define the **finite contact** of the norm class `Γ_n^{rad}` (`n ≥ 2`) as the
mass of the atom of `ω_{fin}` at `t = \log n`, and the **archimedean density
of the radial family at the label `\log n`** as the value of `ω_∞/dt` there:

    contact_{fin}(Γ_n^{rad}) := ω_{fin}(\{\log n\}) = Λ(n)\,n^{−1/2} , (3bis.10)
    ω_∞(\log n) := (ω_∞/dt)\,|_{t=\log n}
          = K(\log n) = \tfrac12[\,τ_∞(1/n)+τ_∞(−1/n)\,]
          = \frac{n^{3/2}}{n^2−1} = n^{−1/2}Σ_{j≥0}n^{−2j} .          (3bis.11)

**Both are well-defined invariants, not free definitions**: `ω_{fin}` and
`ω_∞` exist and are **unique**, so the atom mass at `\log n` and the density
value at `\log n` are determined by `T`, by the radial sector, and by nothing
else.  That is the content of the theorem; the word "define" applies only to
the two **names**.

**[REBUILT, phase 131, round 2, finding `F2` — the honest type warning.]**
`T(Γ_n^{rad})` is **undefined**: `T` is a functional on `D_A` (Paper 43
Def. 8.6) and `Γ_n^{rad} ∉ D_A` (Remark 3bis.4b(i)), and this paper nowhere
extends `T` to multipliers.  Worse, the naive place-wise extension
`W_p(μ) := ∫ (μ∘j_p)\,τ_p\,d^*x` returns **`0`**, not `Λ(n)n^{−1/2}`: for
`|S_f| ≥ 2` the set `Im\,j_p ∩ \{|x|_S = 1/n\}` is, in each coordinate
`Z_r^×` with `r ≠ p`, the single point `n^{−1}`, hence a `Γ_n^{rad}`-null set
(this is Proposition 3bis.2's computation).  So `Λ(n)n^{−1/2}` is obtained
**only** as the atom mass of the unique representing measure `ω_{fin}` of the
radial disintegration, and every statement in this paper that attaches a
number to `Γ_n^{rad}` is to be read that way — including the amended clause
B.4 (§6.2a′), which is worded accordingly.

*Proof.*  Existence and the displayed forms are (3bis.7), read as the
statement that the linear functionals `h ↦ Σ_pW_p(Γ_h)` and `h ↦ W_∞(Γ_h)` on
`C_c^∞(R∖\{0\})` are given by integration against the displayed measures; both
are positive and locally finite (the finite one is a locally finite sum of
atoms because prime powers are discrete in `R_{>0}`; the archimedean one has
continuous density `K(|t|)` on `R∖\{0\}`), hence Radon.  Uniqueness is the
fact that a Radon measure on `R∖\{0\}` is determined by its integrals against
`C_c^∞(R∖\{0\})` (Riesz representation).  For (3bis.11): `τ_∞(x) = |x|^{1/2}/|1−x|`
gives, at `x = 1/n` and `x = −1/n`,

    τ_∞(1/n) = \frac{n^{−1/2}}{1−1/n} = \frac{n^{1/2}}{n−1},
    τ_∞(−1/n) = \frac{n^{−1/2}}{1+1/n} = \frac{n^{1/2}}{n+1},

whose half-sum is `\tfrac12 n^{1/2}\frac{2n}{n^2−1} = n^{3/2}/(n^2−1)`; and
`K(\log n) = n^{−1/2}/(1−n^{−2}) = n^{3/2}/(n^2−1)`, whose geometric expansion
is `n^{−1/2}Σ_{j≥0}n^{−2j}`.  The half-sum form is Paper 43 (8.5a) with the
declared measure (8.5b), which is exactly the `½` in front.  ∎  `PROVED`

**Theorem 3bis.7′ (the contact locus of the radial family; where the
arithmetic is).**  **[REBUILT, phase 131, round 2, finding `F1`.]**  Let
`ω_{fin}` be the finite-place representing measure of Definition–Theorem
3bis.8.  Then:

  (i) *`ω_{fin}` is purely atomic, and its support is exactly the set of
      logarithms of prime powers.*

        supp\,ω_{fin} = \{ ±k\log p : p ∈ S_f,\ k ≥ 1 \} ⊂ R∖\{0\} ,

      and on the colimit (`T_∞`, Paper 43 Thm. 8A.7c) the condition `p ∈ S_f`
      is dropped and the support is `\{±k\log p : p \text{ prime},\ k ≥ 1\}`.
  (ii) *The atom masses are the shell volumes against the half-densities.*
      `ω_{fin}(\{±k\log p\}) = (\log p)\,p^{−k/2}`, and `\log p` is the
      multiplicative Haar volume `vol_{d^*x}(p^kZ_p^×)` of the valuation
      shell, independent of `k`.
  (iii) *Therefore the arithmetic is recovered from the family by its contact
      with the diagonal, and is not carried by the objects.*  For every
      `t > 0`,

        ω_{fin}(\{t\}) ≠ 0  ⟺  e^{t} is a prime power,

      and then `ω_{fin}(\{t\}) = Λ(e^t)e^{−t/2}`.  In particular `Λ` and the
      set of prime powers, and the vanishing `Λ(\text{composite}) = 0`, are
      **read off the contact locus** of the one-parameter family
      `\{Γ^{rad}_{(t)}\}_{t∈R}`, which by Lemma 3bis.3b is an arithmetic-free
      object.  Composite labels are exactly the `t` at which the family has
      **no** contact.

*Proof.*  All three parts are (3bis.7) of Theorem 3bis.7, read as an identity
of measures.  The finite-place functional is
`h ↦ Σ_{p∈S_f}Σ_{k≥1}(\log p)p^{−k/2}[h(k\log p)+h(−k\log p)]`, which is
integration against `Σ_{p,k}(\log p)p^{−k/2}(δ_{k\log p}+δ_{−k\log p})`; the
coefficients are strictly positive, so the support is exactly the index set,
and the measure is purely atomic.  Local finiteness (needed for "Radon") is
the discreteness of `\{k\log p\}` in `R_{>0}`: in a compact window `[a,b]`
with `0 < a`, only finitely many pairs `(p,k)` satisfy `a ≤ k\log p ≤ b`,
since `k ≤ b/\log 2` and `p ≤ e^{b}`.  The shell volume is P123.042 §1 and
the `k`-independence is translation invariance of `d^*x` on `Q_p^×`
(Theorem 6.5(ii)).  The colimit statement is the last paragraph of
Theorem 3bis.7.  For (iii): `e^t = p^k` for some prime `p` and `k ≥ 1` is
exactly the condition that `t` is in the support, and then
`Λ(p^k)(p^k)^{−1/2} = (\log p)p^{−k/2}`.  ∎  `PROVED`

**Remark 3bis.7′a (what Theorem 3bis.7′ does and does not claim).**  It is a
theorem **about row A's trace restricted to the radial sector**, and it is the
honest form of row B's carrier-side content: the family is arithmetic-free,
the trace is not, and the prime powers are the contact locus.  It is **not** a
theorem about an object of `G` carrying factorization data — no such object is
constructed here, and Lemma 3bis.3b says none is available on the radial
sector.  Row B's genuinely object-level arithmetic is on the `Z`-linear side
(§§5–6.2), which is not in `G` and says so.

**Remark 3bis.8a (the finite contact and the archimedean density are of
different type, and are not added).**  **[REBUILT, phase 131, round 2, finding
`F6`: the archimedean quantity is no longer called a contact.]**
`contact_{fin}(Γ_n^{rad})` is the mass of an **atom** of `ω_{fin}`: a number
attached to the single norm class `Γ_n^{rad}`, and zero unless `n` is a prime
power.  `ω_∞(\log n)` is the value of a **continuous density** at a point of
its argument: it is an invariant of `ω_∞` and of the label `\log n`, it is
defined for **every** real `t`, and **nothing about the object `Γ_n^{rad}`
enters it** — the family has no archimedean atom at all.  It is therefore not
a contact and is not called one; the two are not summed, and `ω_∞(\log n)` is
**not** part of `Λ(n)`.

Phase-128 finding `B6` ("the archimedean place is dropped without accounting")
is answered in exactly this form: *the archimedean place contributes a
continuous density `K(|t|)dt` to the radial disintegration of `T`, and the
arithmetic family has no atom there.*  That is a complete accounting and it
needs no archimedean `Λ`.  The expansion
`n^{−1/2}Σ_{j≥0}n^{−2j}` in (3bis.11) exhibits one term for each exponent
`−2j`; **no statement about zeros, trivial or otherwise, is made or used
here**, and none is available: the explicit formula for a point class
diverges.

**Remark 3bis.8b (`Λ` is derived, not input — and the derivation is row A's,
inherited).**  **[REBUILT, phase 131, round 2, finding `F9`.]**  The reading
"`Λ(p^k) = \log p` is the multiplicative Haar volume of the valuation shell"
is **not new here**: Paper 43 Remark 9.7a already states it, with the same
P123.042 §1 justification, and already answers clause A.10 with it.  Row B
**inherits** that derivation; what row B adds is to attach it to the family
and to its contact locus (Theorem 3bis.7′), i.e. to say *which objects have
the atoms* and *that composite labels have none*.  The claim "row B derives
`Λ`" would be an overclaim and is not made.

A second honest point.  The normalization `vol_{d^*x}(Z_p^×) = \log p` is a
**declared** convention of row A (Paper 43 (8.5), Rem. 8.6a; P123.042 §1),
chosen so that the local multiplicative measure is compatible with `dt` on the
modulus line.  "`Λ` is a volume" is therefore true *relative to that declared
normalization*, which is the normalization that makes the local terms come out
as they do.  The statement row B is entitled to is the negative one and it is
enough for B.9: **no zero, no RH, no positivity, and no von Mangoldt function
is used as an input anywhere**; the normalization is declared, and it is row
A's.

Formula (3bis.8) exhibits
`Λ(p^k) = \log p` as the multiplicative Haar volume of the valuation shell
`p^kZ_p^×` of the carrier, and the vanishing of `Λ` at composite `n` as the
statement that no single place has a shell of modulus `1/n`.  Nothing in the
derivation selects an arithmetic family from outside, uses the von Mangoldt
function as an input, or uses the explicit formula: the only ingredients are
Paper 43's proved local terms (8.5), the exact orbital values
`τ_p(p^k) = p^{−|k|/2}` of Lemma 8.2(i) (P123.042), and the shell volume of
P123.042 §1.  This is precisely the discipline Paper 43 Remark 9.7a(1)
imposes, and row B here satisfies it with the same argument as row A.

**Theorem 3bis.9 (the smeared form: row B's classes and row C's geometric
side).**  For `h ∈ C_c^∞(R)` with `0 ∉ supp h`, the class
`Γ_h = ∫h(t)Γ^{rad}_{(t)}dt` is an object of `D_A^{rad}` and, by (3bis.7′),
`T(Γ_h)` is the finite-place packet of the explicit formula plus its
archimedean term, evaluated on `h`.  In particular the prime packet (9.1) is
the value of row A's declared trace on the arithmetic family, not an analogy
with it.  `PROVED` (this is Theorem 3bis.7 restated).

### 3bis.4 The integral model and the matching of degrees

**Theorem 3bis.10 (degree matching; blueprint item (f), proved).**  Let
`n ≥ 2` and `S ⊇ \{∞\}∪P(n)`.  Then

  (i) `\log[L_S : nL_S] = deg_det Q_{S,n} = deg_det C_{ram}(n) = \log n`;
  (ii) `\log n = Σ_{d|n} Λ(d) = Σ_{d|n} d^{1/2}·contact_{fin}(Γ_d^{rad})`;
  (iii) `deg_det Prim_n = \log\#(Z/Φ_n(1)) = \log|\det(1−T|V_n)| = Λ(n)
       = n^{1/2}·contact_{fin}(Γ_n^{rad})`;
  (iv) the passage from (i)–(ii) to (iii) is Möbius inversion over the divisor
       poset, categorified by the cube of P123.037 (Lemma 5.1, Theorem 5.3).

Thus the lattice-index degree of P123.038, the finite-orbit determinant
`\det(1−T|V_n) = Φ_n(1)` of P123.039, and the shell volume of the carrier
compute the same numbers.  **What is a theorem in the declared category is the
shell volume** (Theorem 3bis.7): `Q_{S,n}`, `Prim_n`, `V_n` are `Z`-linear
models indexed by the same labels, and the identification with them is of
**degrees** only.

*Proof.*  (i) is Theorem 6.1(i)–(ii) and Definition 5.2.  (ii): the first
equality is Corollary 5.3a (`Λ = μ∗\log` Möbius-inverted), the second is
(3bis.10) of Definition–Theorem 3bis.8, which gives
`d^{1/2}·contact_{fin}(Γ_d^{rad}) = Λ(d)` for every `d ≥ 2`, together with
`Λ(1) = 0` (the label `1` is identity/excess, Theorem 5.3, and `t = 0` is
excluded from `ω_{fin}` by construction).  (iii) is Theorem 5.3 and
Theorem 6.3(c) (P123.039 §3) together with (3bis.10).  (iv) is Lemma 5.1 and
Theorem 5.3.  ∎  `PROVED`

**Remark 3bis.10a (what this does not say).**  It does **not** say that
`Z/Φ_n(1)` is an object of `G`, or that any complex over `Z` is a shadow of
`Γ_n^{rad}`.  It cannot: by Paper 43 Theorem 7.1(c) the shadow of an external
class at a finite place `p | n` is the single origin class `C[0]`, and
P123.022 records as `REFUTED` the recovery of nonzero integral torsion by an
additive contact functor from a `C`-linear category.  The content of
Theorem 3bis.10 is an equality of **numbers**, each of which is independently
computed on its own side, and the reason the equality is not a tautology is
that the left-hand sides are lattice indices and determinants over `Z` while
the right-hand sides are Haar volumes of shells of `X_S`.

**Remark 3bis.10b (the arrow P123.038 §5 asked for, now with a carrier
statement).**  P123.038 §5 asked for "the lattice-index operation realized as
the admissible diagonal shadow … compared with the analytic trace".
Theorem 6.1(iii) supplies the first half as a definitional identity (this is
phase-128 finding `B2`, and it stands).  Theorem 3bis.10(ii) supplies the
**comparison with the analytic trace** that was missing: the lattice index
degree `\log n` is the divisor sum of the finite contacts of the norm
classes, each of which is a value of row A's declared trace.  That comparison
is new in phase 131 and is not a renaming: the right-hand side is computed
from (8.5) and P123.042 §1, the left-hand side from `L_S/nL_S`.

---

## 3ter. The Frobenius family

**[REBUILT, phase 131, round 3 — this section is new.]**  §3bis proved a
negative: on the radial sector the objects are arithmetic-free (Lemma 3bis.3b),
and the arithmetic sits in the contact locus (Theorem 3bis.7′).  That negative
is correct, and it is a statement about the **radial** sector only.  This
section constructs objects that are *not* radial and that do carry the
arithmetic: the **Frobenius family**.  They are the Haar measures of the
fixed-point strata of the local dilation actions, they compose with a **true
unit**, their supports remember `n` **and** the set of primes dividing `n`, and
their finite contact is `Λ(n)n^{−1/2}` — zero at composite `n` *for a reason
visible in the object*.

Throughout, `S` is a chart with `∞ ∈ S`, and `n ≥ 1` with `P(n) ⊆ S_f`.  We use
Paper 43 (9.5b),

    j_p(p^k w) = ( p^{−k} at ∞ ; w at p ; p^{−k} at every other place of S ),
    j_∞(x)    = ( x at ∞ ; 1 at every finite place of S ),

and recall that `j_p : Q_p^× → C_S` is an injective continuous homomorphism
(Paper 43 Lemma 3.3: `v_r(p^{−k}) = 0` for `r ≠ p`, so `j_p` lands in
`ker φ ≅ C_S`).

### 3ter.1 The local Frobenius

**Definition 3ter.1.**  For `p ∈ S_f` and `k ≥ 1` let

    Z_p^{(S)} := j_p(Z_p^×) = { (1 at ∞ ; w at p ; 1 elsewhere) : w ∈ Z_p^× } ,

a compact subgroup of `C_S`, and define the **local Frobenius**

    Frob_{p^k} := ∫_{Z_p^×} E_{j_p(p^k u)}\,du
                = the normalized Haar probability measure of the coset
                  j_p(p^k)·Z_p^{(S)} = j_p(p^kZ_p^×) ,                (3ter.1)

`du` the probability Haar measure of `Z_p^×`.  **`Frob_{p^k}` is the Haar
measure of the valuation shell `p^kZ_p^×`, transported to the carrier by the
slice map `j_p`.**  For a finite set `F ⊆ S_f` put

    K_F := ∏_{p∈F} Z_p^{(S)} ⊆ C_S ,   Δ^{(F)} := normalized Haar measure of K_F,

and for `n ≥ 1` write `Δ^{(n)} := Δ^{(P(n))}`.  `Δ^{(∅)} = δ_1 = Δ`, the point
mass at the identity class, i.e. the diagonal `E_1`.

**Definition 3ter.2 (the arithmetic Frobenius).**  For `n = ∏_p p^{k_p} ≥ 1`,

    Frob_n := ⋆_{p | n} Frob_{p^{k_p}} ,    Frob_1 := Δ .              (3ter.2)

Equivalently, with the **integral idele** `ι(n) := (1` at `∞`; `p^{v_p(n)}` at
every finite place of `S)` and `c_n := ` the class of `ι(n)`,

    Frob_n = ∫_{∏_{p|n}Z_p^×} E_{c_n·u}\,du
           = the normalized Haar measure of the coset c_n·K_{P(n)} .   (3ter.3)

**Lemma 3ter.3 (the class of `ι(n)`, and the support).**  `c_n = ∏_{p|n}
j_p(p^{v_p(n)})`, and

    supp\,Frob_n = c_n K_{P(n)}
      = { ( 1/n at ∞ ; u_p ∈ Z_p^× at each p | n ; 1/n at each r ∤ n ) } . (3ter.4)

In particular `|x|_S = 1/n` on the support, and `Frob_n` is supported in the
**positive** archimedean component.

*Proof.*  `φ(ι(n)) = ∏_{p∈S_f}p^{v_p(n)} = n ∈ Γ_S`, so by Paper 43 Lemma 3.3
the class of `ι(n)` is `ι(n)/n = (1/n` at `∞`; `p^{v_p(n)}/n` at `p)`.  At
`p | n` the coordinate `p^{v_p(n)}/n = (n/p^{v_p(n)})^{−1}` is a unit of `Z_p`;
at `r ∤ n` it is `1/n ∈ Z_r^×`.  Separately,
`∏_{p|n}j_p(p^{v_p(n)})` has archimedean coordinate `∏_{p|n}p^{−v_p(n)} = 1/n`,
`r`-coordinate `∏_{p|n, p≠r}p^{−v_p(n)}` for `r | n` (a unit of `Z_r`) and
`1/n` for `r ∤ n`.  The two agree at `∞` and at every `r ∤ n`, and at `p | n`
they differ by a unit of `Z_p`, which the coset `c_nK_{P(n)}` absorbs.  Hence
(3ter.3) and (3ter.4) describe the same coset, and `|x|_S = |x_∞| = 1/n` on it
by Lemma 3.3.  ∎  `PROVED`

**Theorem 3ter.4 (B.2 for the Frobenius family: a strong monoidal realization
with a TRUE unit).**  For all `m,n ≥ 1`:

  (i) `Frob_m ⋆ Frob_n = Frob_{mn}`, an **equality** of measures;
  (ii) `Frob_1 = Δ = E_1`, the diagonal itself — a point mass, **not** a
       projector;
  (iii) `n ↦ Frob_n` is a strong monoidal functor from the monoid
       `(N_{≥1},×)` to the convolution monoid `M_c(C_S)` of compactly
       supported Radon measures, with its **unit preserved on the nose**;
  (iv) it is **injective**, and `supp\,Frob_n` determines both `n` and `P(n)`.

*Proof.*  (i)  Write `μ_{cK}` for the normalized Haar measure of a coset of a
compact subgroup `K ≤ C_S`.  If `K, K'` are compact subgroups then
`μ_{cK} ⋆ μ_{c'K'} = μ_{cc'KK'}`: the convolution is the image of
`μ_K ⊗ μ_{K'}` under `(u,v) ↦ cc'uv`, and `uv` is Haar-distributed on the
compact group `KK'` because `K,K'` are compact subgroups of an abelian group
and Haar ⋆ Haar = Haar on `KK'` (the image of `μ_K⊗μ_{K'}` under
multiplication is a `KK'`-invariant probability measure on `KK'`, hence
`μ_{KK'}` by uniqueness).  Now `K_{P(m)}K_{P(n)} = K_{P(m)∪P(n)} = K_{P(mn)}`,
and `c_mc_n = ∏_p j_p(p^{v_p(m)})j_p(p^{v_p(n)}) = ∏_p j_p(p^{v_p(m)+v_p(n)})
= c_{mn}`, using that each `j_p` is a homomorphism and that distinct `j_p`
commute.  Hence `Frob_m⋆Frob_n = μ_{c_{mn}K_{P(mn)}} = Frob_{mn}`.

(ii)  For `n = 1` the product (3ter.2) is empty, `c_1 = 1` and
`K_{P(1)} = K_∅ = \{1\}`, so `Frob_1 = δ_1`, the point mass at the identity
class, which is `E_1 = Δ` under `F ↦ E_F` (Paper 43 Corollary 3.4).  `δ_1` is
the unit of `(M_c(C_S), ⋆)`.

(iii)  is (i)+(ii); associativity and unit coherence are those of convolution
of measures on the locally compact abelian group `C_S`.

(iv)  By (3ter.4), `\sup_{x∈supp Frob_n}|x|_S = 1/n` recovers `n`, and the set
of finite places at which the support projects **onto** the whole of `Z_p^×`
(rather than to a single point) is exactly `P(n)`.  ∎  `PROVED`

**Remark 3ter.4a (this is the object `R131.005`'s reservation R1 asked for).**
By Lemma 3bis.3b the radial realization factors through `(R_{>0},×)` and
forgets factorization.  The Frobenius realization does **not**: by
Theorem 3ter.4(iv) the object determines `(n, P(n))`, and it is *defined* only
for integer labels, because the datum `K_{P(n)}` — which finite coordinates are
averaged — has no meaning for a real label.  Concretely there is **no**
one-parameter family `\{Frob_{(t)}\}_{t∈R}` of compactly supported measures
with `Frob_{(\log n)} = Frob_n` that is continuous in the weak-⋆ topology: the
support of `Frob_n` has `\dim`-type invariant `|P(n)|` (the number of
coordinates on which the support is a full `Z_p^×`), and `|P(n)|` is not
locally constant along any ordering of the integers — e.g. `|P(2)| = |P(4)| =
1` but `|P(6)| = 2`, and any weak-⋆ limit of measures supported on
`\{x_r = 1/n\}` for `r ∤ n` is again supported in such a set.

**Relation to §3bis.**  Averaging the Frobenius over the remaining coordinates
destroys exactly the arithmetic information:

**Proposition 3ter.5.**  `Frob_n ⋆ Γ_1^{rad} = Γ_n^{rad}`, where `Γ_1^{rad} =
Δ^{rad}` is the Haar measure of `K^♮ = \{±1\}×∏_{p∈S_f}Z_p^×` (Definition
3bis.4).  So the norm class is the image of the Frobenius under the total
unit-averaging projector, and Lemma 3bis.3b's loss of factorization is the
kernel of that projector.

*Proof.*  `μ_{c_nK_{P(n)}} ⋆ μ_{K^♮} = μ_{c_nK_{P(n)}K^♮} = μ_{c_nK^♮}` by the
coset formula in the proof of Theorem 3ter.4(i), since `K_{P(n)} ⊆ K^♮`.  And
`c_nK^♮ = \{|x|_S = 1/n\}` because `|c_n|_S = 1/n` and `K^♮ = \ker(|·|_S)`
(Lemma 3bis.3b).  ∎  `PROVED`

### 3ter.2 The dagger, the degree relation, and the inverse semigroup

**Theorem 3ter.6 (B.3 for the Frobenius family; Weil's degree relation in
averaged form).**  For `m,n ≥ 1`:

  (i) `Frob_n^† = μ_{c_n^{−1}K_{P(n)}}`, supported on `\{|x|_S = n\}`;
  (ii) `Frob_n ⋆ Frob_n^† = Δ^{(n)}`, the Haar measure of `K_{P(n)}`, an
       **idempotent**: `Δ^{(n)}⋆Δ^{(n)} = Δ^{(n)}`;
  (iii) `M(Frob_n) = (λ_−,λ_+)(Frob_n) = (n^{1/2}, n^{−1/2})`, and
       `M(Δ^{(n)}) = (1,1) = M(Δ)`;
  (iv) `Δ^{(n)} ≠ Δ` for every `n > 1`.

*Proof.*  (i)  `†` is push-forward along inversion composed with conjugation
(Paper 43 (8.2)); `Frob_n` is a real positive measure, and
`(c_nK_{P(n)})^{−1} = c_n^{−1}K_{P(n)}` because `K_{P(n)}` is a group.
`|c_n^{−1}|_S = n`.

(ii)  By the coset formula, `μ_{c_nK}⋆μ_{c_n^{−1}K} = μ_{KK} = μ_K` with
`K = K_{P(n)}`.  Idempotence is the same formula with `c = 1`.

(iii)  `λ_∓(μ) = ∫|x|_S^{∓1/2}dμ` (Paper 43 (9.2)); `|x|_S ≡ 1/n` on
`supp Frob_n`, a probability measure, so `λ_− = n^{1/2}`, `λ_+ = n^{−1/2}`.
On `K_{P(n)}` the modulus is `1`, giving `(1,1)`.

(iv)  `Δ^{(n)}` is the Haar measure of the compact group `K_{P(n)}`, which is
infinite for `P(n) ≠ ∅` (it contains `Z_p^×`, which is infinite); a Haar
measure of an infinite compact group has no atoms, whereas `Δ = δ_1` is an
atom.  ∎  `PROVED`

**Remark 3ter.6a (what (ii) is and is not).**  Weil's relation for the
Frobenius correspondence on a curve over `F_q` is `Γ_F ⋆ Γ_F^t = q·Δ`.
Theorem 3ter.6(ii) is its **averaged, half-density-normalized** analogue: the
factor `q` is absent because the canonical half-density `|·|_S^{−1/2}` has
already been applied (Theorem 4.4(iii); the bidegree
`M(Frob_n) = (n^{1/2},n^{−1/2})` has product `1`, which is where the degree
went), and `Δ` is replaced by the **idempotent `Δ^{(n)}`, which is not `Δ`**
(part (iv)).  This paper therefore does **not** claim Weil's relation; it
claims (ii), and (iv) records exactly how the two differ.  The analogy is
stated as an analogy and is used nowhere.

**Theorem 3ter.7 (the `†`-closed family is an inverse semigroup — and it is
*not* indexed by `Q_{>0}^×`).**  For `r ∈ Q_{>0}^×` with `P(r) ⊆ S_f` and a
finite `F ⊆ S_f` with `P(r) ⊆ F`, put

    c_r := ∏_p j_p(p^{v_p(r)}) ,   Frob_{r,F} := μ_{c_r K_F} ,        (3ter.5)

so that `Frob_n = Frob_{n,P(n)}`.  Then:

  (i) `Frob_{r,F} ⋆ Frob_{s,G} = Frob_{rs,\,F∪G}` and
      `Frob_{r,F}^† = Frob_{r^{−1},F}`;
  (ii) `𝔉_S := \{Frob_{r,F}\}` is a **commutative inverse semigroup** under
      `⋆`, with inverse `Frob_{r,F}^†`, whose idempotents are exactly
      `\{Δ^{(F)}\}`, forming a semilattice isomorphic to
      `(𝒫_{fin}(S_f), ∪)`;
  (iii) `𝔉_S` is `†`-closed and contains every `Frob_n` and every
      `Frob_n^†`; it is the smallest such set closed under `⋆` and `†`;
  (iv) **the assignment `r ↦ Frob_r ⋆ Frob_s^†` does NOT descend to
      `Q_{>0}^×`.**

*Proof.*  (i)  is the coset formula, `c_rc_s = c_{rs}` and
`K_FK_G = K_{F∪G}`, exactly as in Theorem 3ter.4(i).

(ii)  `𝔉_S` is closed under `⋆` by (i) and commutative because `C_S` is
abelian.  Each element is regular: `x⋆x^†⋆x = Frob_{r,F}⋆Frob_{r^{−1},F}⋆
Frob_{r,F} = Δ^{(F)}⋆Frob_{r,F} = Frob_{r,F}` (the last because
`K_FK_F = K_F` and `c_r K_F K_F = c_rK_F`), and symmetrically
`x^†⋆x⋆x^† = x^†`.  A commutative regular semigroup is an inverse semigroup
with unique inverses.  Idempotents: `Frob_{r,F}⋆Frob_{r,F} = Frob_{r²,F}`,
which equals `Frob_{r,F}` iff `c_{r²}K_F = c_rK_F` iff `c_r ∈ K_F` iff
`|c_r|_S = 1` and `v_p(r) = 0` for `p ∉ F`, i.e. iff `r = 1`.  So the
idempotents are the `Frob_{1,F} = Δ^{(F)}`, and `Δ^{(F)}⋆Δ^{(G)} = Δ^{(F∪G)}`
gives the semilattice `(𝒫_{fin}(S_f),∪)`.

(iii)  `Frob_n = Frob_{n,P(n)}`, `Frob_n^† = Frob_{n^{−1},P(n)}`, and (i)
shows any `⋆`/`†` word in these lies in `𝔉_S`; minimality is (i) again.

(iv)  **[REBUILT, phase 131, round 3 — this refutes a claim of the round-3
blueprint; see the report `R131.007` §2.]**  The blueprint asserts that the
`†`-closed family is `\{Frob_r : r ∈ Q_{>0}^×\}` with
`Frob_{a/b} := Frob_a ⋆ Frob_b^†`.  That assignment is **not well defined**.
*Counterexample.*  `2/1 = 6/3`, but

    Frob_2 ⋆ Frob_1^† = μ_{j_2(2)\,K_{\{2\}}} ,
    Frob_6 ⋆ Frob_3^† = μ_{c_6c_3^{−1}K_{\{2,3\}}} = μ_{j_2(2)\,K_{\{2,3\}}} ,

and these differ: the first is supported on a coset of `Z_2^{(S)}`, the second
on a coset of `Z_2^{(S)}×Z_3^{(S)}`, sets of different dimension — the second
projects onto all of `Z_3^×` at the place `3`, the first onto the single point
`1/2 ∈ Z_3^×`.  (Both are probability measures on those cosets, and a measure
determines its support, so they are distinct.)  The correct index set is the
one of (3ter.5): pairs `(r,F)` with `P(r) ⊆ F`, i.e. `Q_{>0}^×` **graded by
the semilattice of finite prime sets**.  This is not a defect: it is the
statement that the idempotents `Δ^{(F)}` are genuine extra data, which is
precisely what makes `𝔉_S` an inverse semigroup rather than a group.  ∎
`PROVED`

### 3ter.3 The contact of the Frobenius family

The smearing is chosen so that the finite contact is **exact for every level**,
with no limit taken at the finite places.

**Definition 3ter.8 (the smeared Frobenius).**  Let `n ≥ 2`, `P := P(n)`.  Fix
`h ∈ C_c^∞(R_{>0})` with

    supp\,h ⊂ ( n^{−1}e^{−ε},\; n^{−1}e^{ε} ) ,                       (3ter.6)

and an integer `N ≥ 1`.  Define `Frob_n^{[h,N]} : C_S → C` by

    Frob_n^{[h,N]}(x) := h(x_∞)·∏_{r ∈ S_f∖P} 1_{\,n^{−1}(1+r^NZ_r)}(x_r) , (3ter.7)

with **no condition** at the places `p ∈ P` (the function is constant `1` in
those coordinates) and the indicators **unnormalized**.  Write
`Frob_n^{[h,N],\flat} := (∏_{r∉P}vol(1+r^NZ_r))^{−1}·Frob_n^{[h,N]}` for the
normalized version.

**Lemma 3ter.9.**  `Frob_n^{[h,N]} ∈ D_A`, and if `ε < \log n` then
`Frob_n^{[h,N]} ∈ D_A^{off}`.  Moreover `Frob_n^{[h,N],\flat} → Frob_n` weak-⋆ as
`ε → 0` and `N → ∞`.

*Proof.*  Smooth in `x_∞` (a `C_c^∞` function of the archimedean coordinate),
locally constant in the compact coordinates (indicators of cosets of the open
subgroups `1+r^NZ_r`), and supported in a compact subset of `C_S` (compact in
`x_∞` by (3ter.6), and the compact part of `C_S` is compact).  `D_A^{off}`: the
identity class has `x_∞ = 1`, and `1 ∉ supp\,h` because
`n^{−1}e^{ε} < 1` when `ε < \log n`; `supp h` is closed in `R^×`, so the
function vanishes on a neighbourhood of the identity class.  Weak-⋆
convergence: the normalized function is a probability density on a
neighbourhood basis of the coset `c_nK_P` intersected with the level
`\{x_r ∈ n^{−1}(1+r^NZ_r)\}`, and these shrink to `c_nK_P`.  ∎  `PROVED`

**Theorem 3ter.10 (the finite contact of the Frobenius is exact at every
level).**  Let `n ≥ 2`, `h` and `N` as in Definition 3ter.8, with `ε` small
enough that `supp\,h` contains no point of `\{q^{−m} : q ∈ S_f, m ∈ Z\}`
**other than** `1/n` itself.  Then, with `c := 0` (Paper 43 Def. 8A.7d),

    Σ_{q ∈ S_f} W_q( Frob_n^{[h,N]} ) = Λ(n)\,n^{−1/2}\,h(1/n)         (3ter.8)

**exactly, for every `N ≥ 1`** — no regularization, no counterterm, no limit at
the finite places — and in particular the left-hand side is `0` for every
composite `n`.  The archimedean term is

    W_∞( Frob_n^{[h,N]} ) = \Big(∫_0^∞ K(t)\,h(e^{−t})\,dt\Big)·
        ∏_{r ∈ S_f∖P(n)} \mathbf 1\big[\,r^N \mid n−1\,\big] ,        (3ter.9)

`K(t) = e^{−t/2}/(1−e^{−2t})`; in particular it **vanishes for every
sufficiently large `N`** as soon as `S_f ⊋ P(n)`, and the limit object
`Frob_n` has no archimedean contribution at all in that case
(Corollary 3ter.10b).

*Proof.*  `F := Frob_n^{[h,N]} ∈ D_A^{off}` by Lemma 3ter.9, so Paper 43
Theorem 8.8 applies and `T(F) = Σ_{v∈S}∫F(j_v(x))τ_v(x)d^*x`, absolutely
convergent, with no `c` term.  Write `a_q := F∘j_q`.

*Shells at `q ∈ S_f`, `m ≠ 0`.*  By (9.5b) the archimedean coordinate of
`j_q(q^mw)` is `q^{−m}`, so `a_q(q^mw) = h(q^{−m})·(\text{indicators})`.  By
hypothesis `h(q^{−m}) = 0` unless `q^{−m} = 1/n`, i.e. unless `n = q^m` (so
`m ≥ 1` and `n` is a power of `q`).

 — *If `n` is not a prime power*, no `(q,m)` qualifies and every shell integral
vanishes.

 — *If `n = p^k`*, the only surviving term is `q = p`, `m = k`.  Then `P = \{p\}`
and, for `r ∈ S_f∖\{p\}`, the `r`-coordinate of `j_p(p^kw)` is `p^{−k} = 1/n`,
which lies in `n^{−1}(1+r^NZ_r)` for **every** `N` (it is the centre of that
coset).  So every indicator equals `1`, and

    a_p(p^kw) = h(p^{−k}) = h(1/n) ,   independent of w ∈ Z_p^× .

By Paper 43 Lemma 8.2(i), `τ_p ≡ p^{−k/2}` on the shell, and
`vol_{d^*x}(p^kZ_p^×) = \log p` (P123.042 §1).  Hence

    ∫_{p^kZ_p^×} a_p τ_p\,d^*x = (\log p)\,p^{−k/2}\,h(1/n)
                               = Λ(n)\,n^{−1/2}h(1/n) .

*Unit packets at `q ∈ S_f`, `m = 0`.*  By (9.5b), `j_q(w) = (1` at `∞`; `w` at
`q`; `1` elsewhere`)` for `w ∈ Z_q^×`, whose archimedean coordinate is `1`.
Since `1 ∉ supp\,h` (Lemma 3ter.9), `a_q(w) = 0` for every `w ∈ Z_q^×`, and
`a_q(1) = 0`; hence

    (\log q)∫_{Z_q^×}\frac{a_q(u)−a_q(1)}{|1−u|_q}\,du = 0 ,

for **every** `q`, whether `q | n` or `q ∤ n`.  (This is the check the round-3
instruction asks for at `r ∤ n`, and it holds for the same reason at `q | n`:
the unit slice sits at archimedean coordinate `1`, and the Frobenius is
supported at archimedean coordinate `1/n ≠ 1`.  No cancellation, no principal
value, no smallness hypothesis beyond `n ≥ 2`.)

Summing gives (3ter.8), and `Λ(n) = 0` for composite `n` matches the vanishing
of all shell terms.

*Archimedean.*  `j_∞(x) = (x` at `∞`; `1` at every finite place`)`, so
`b := F∘j_∞` is `b(x) = h(x)·∏_{r∈S_f∖P}1_{n^{−1}(1+r^NZ_r)}(1)`, and the
`r`-th indicator equals `1` **iff** `n ∈ 1+r^NZ_r`, i.e. iff `r^N \mid n−1`.
By Paper 43 Remark 8.6a with the declared measure `d^*x_∞ = dx/(2|x|)` of
(8.5b), and since `h` is supported in `R_{>0}`,

    W_∞(F) = ∫_0^∞K(t)\big[\,b(t) + b(−t)\,\big]dt
           = \Big(∫_0^∞K(t)h(e^{−t})dt\Big)∏_{r∈S_f∖P}\mathbf 1[r^N \mid n−1],

**[REBUILT, phase 131, round 4, finding `F4`: round 3 wrote the bracket as
`b(e^{−t})+b(−e^{−t})`, i.e. with the sign-flipped *argument*; that misquotes
(8.5∞), whose bracket is `b(t)+b(−t)` in the **logarithmic** variable, the
sign of `x_∞` having already been folded into `K` by Remark 8.6a.  The value
is unaffected here: writing `b(t) := F(j_∞(e^{t}))` and noting that `F` is
supported in `x_∞ > 0`, the term `b(t)` vanishes for `t > 0` because
`e^{t} > 1 > n^{−1}e^{ε} ≥ supp\,h`, so only `b(−t) = h(e^{−t})` survives —
which is the displayed value.]**

which is (3ter.9).  For each `r ∈ S_f∖P` the condition `r^N \mid n−1` fails
once `r^N > n−1`, so the whole term is `0` for all large `N` whenever
`S_f ∖ P(n) ≠ ∅`.  ∎  `PROVED`

**Corollary 3ter.10b (the Frobenius is off the archimedean slice; the exact
dual of Corollary 3bis.3).**  Let `n ≥ 2` and `S_f ⊋ P(n)`.  Then

    supp\,Frob_n ∩ Im\,j_∞ = ∅ ,

so the Frobenius object has **no archimedean contact**, and by Theorem 3ter.12
it has a finite contact exactly when `n` is a prime power.  Dually, by
Corollary 3bis.3 the **element** class `Frob_∞(\log n) = δ_S(1/n)` lies on
`Im\,j_∞` and on no `Im\,j_q` (for `|S_f| ≥ 2`), so it has an archimedean
density and no finite contact.  The two families are supported on
complementary slices of the carrier.

*Proof.*  A point of `Im\,j_∞` has every finite coordinate equal to `1`; a
point of `supp\,Frob_n` has `r`-coordinate `1/n` for `r ∈ S_f∖P(n)`
(Lemma 3ter.3), and `1/n ≠ 1` in `Z_r^×` because `n ≥ 2` and `r ∤ n`, so
`v_r(n−1) < ∞` and `n^{−1} ∉ 1+r^mZ_r` for `m > v_r(n−1)`; in particular
`n^{−1} ≠ 1`.  ∎  `PROVED`

**Remark 3ter.10a (a correction to the round-3 blueprint).**  **[REBUILT,
phase 131, round 3.]**  The blueprint states that the smeared finite contact is
"exactly `Λ(n)n^{−1/2}·∫ρ_ε` for every `N` and small `ε`".  That is **false**:
the shell integral evaluates the archimedean profile at the single point
`x_∞ = p^{−k}`, because `a_p` is *constant* on the shell and equal to
`h(p^{−k})`; what appears is the **value** `h(1/n)`, not the integral `∫h`.
With an `L^1`-normalized bump `h = ρ_ε` one has `h(1/n) ≍ 1/ε → ∞`, so the
quantity `Λ(n)n^{−1/2}∫ρ_ε = Λ(n)n^{−1/2}` is *not* the contact of
`Frob_n^{[ρ_ε,N]}`.  The correct statement is (3ter.8), and it is strictly
better than what the blueprint claimed: it is **exact for every `N` and every
admissible `h`**, with the profile entering only through `h(1/n)`.  The
normalization-free invariant is recovered as in §3bis: the finite part of `T`
on this family is represented by a measure whose atom at the label is
`Λ(n)n^{−1/2}` (Corollary 3ter.11).

**Corollary 3ter.11 (the finite contact of the object).**  Fix `N`.  The map
`h ↦ Σ_qW_q(Frob_n^{[h,N]})` is, by (3ter.8), integration of `h` against the
measure `Λ(n)n^{−1/2}·δ_{1/n}` on `R_{>0}`, independently of `N`.  Define

    contact_{fin}(Frob_n) := Λ(n)\,n^{−1/2} ,                        (3ter.10)

the mass of that atom.  It is the unique such invariant (a Radon measure is
determined by its `C_c^∞` integrals), and for `n = p^k`

    contact_{fin}(Frob_{p^k}) = vol_{d^*x}\big(j_p(p^kZ_p^×)\big)·p^{−k/2}
                              = (\log p)\,p^{−k/2} ,                 (3ter.11)

**the multiplicative Haar volume of the support of the object itself**, times
its half-density.  ∎  `PROVED`

**Remark 3ter.11a (`Λ` as the volume of the object's own support — reservation
R4).**  In row A, `Λ(p^k) = \log p` appears as a Fourier coefficient of the
symbol and is justified by the shell-volume normalization `vol(Z_p^×) = \log p`
of P123.042 §1 (Paper 43 Remark 9.7a); §3bis inherited that reading
(Remark 3bis.8b).  Here the statement is about a **named object**:
`Frob_{p^k}` *is* the Haar measure of the stratum `j_p(p^kZ_p^×)`, and
(3ter.11) says its finite contact is the volume of that stratum against the
half-density.  The numerical normalization is still row A's declared one — that
concession of round 2 stands, and is not withdrawn — but the *attribution* is
now to an object of row B and not only to a symbol of row A.

**Theorem 3ter.12 (B.6 is non-vacuous: composite labels carry a theorem about
the object).**  Let `n ≥ 2`.  Then

    contact_{fin}(Frob_n) ≠ 0  ⟺  supp\,Frob_n ∩ Im\,j_q has positive
    Haar measure in some shell  ⟺  n is a prime power,

and in that case the intersection is the **whole** shell `j_p(p^kZ_p^×)`,
i.e. `supp\,Frob_{p^k} = j_p(p^kZ_p^×) ⊆ Im\,j_p`.  For composite `n`, the
support meets `Im\,j_q` for no `q` at all.

*Proof.*  For `n = p^k` the support is `c_nK_{\{p\}} = j_p(p^k)·j_p(Z_p^×) =
j_p(p^kZ_p^×)` (Lemma 3ter.3 with `P(n) = \{p\}`; the coordinates at `r ≠ p`
are `p^{−k}`, exactly as (9.5b) prescribes), which is the whole shell.  For `n`
with at least two prime divisors, a point of `supp\,Frob_n` has archimedean
coordinate `1/n`, while a point of `Im\,j_q` has archimedean coordinate
`q^{−m}` for some `m ∈ Z`; and `1/n = q^{−m}` forces `n = q^m`, contradicting
`|P(n)| ≥ 2`.  So the supports are disjoint.  ∎  `PROVED`

**Remark 3ter.12a (reservation R6 dissolved).**  Round 2 recorded B.6's first
half as "`PROVED` but vacuous for composite `n`", because the radial object
`Γ_n^{rad}` carried nothing distinguishing composite from prime-power labels.
Theorem 3ter.12 is a statement **about the object** `Frob_n`, different for
every `n` (Theorem 3ter.4(iv)), and it says the vanishing of the contact at
composite `n` is the **disjointness of its support from every fixed-point
stratum**.  That is not vacuous, and it is not a statement about a real label:
`Frob_6` and `Frob_4` are distinguished by their supports before any trace is
computed.

### 3ter.4 The archimedean Frobenius, and the two flows

**Definition–Proposition 3ter.13.**  For `t ∈ R` set
`Frob_∞(t) := E_{j_∞(e^{−t})} = δ_{j_∞(e^{−t})}`, the point mass at
`(e^{−t}` at `∞`; `1` at every finite place`)`.  Then:

  (i) `Frob_∞` is a one-parameter **group**: `Frob_∞(s)⋆Frob_∞(t) =
      Frob_∞(s+t)`, `Frob_∞(0) = Δ`, `Frob_∞(t)^† = Frob_∞(−t)`;
  (ii) `Frob_∞(\log n) = δ_S(1/n)` is exactly Paper 44's **element class**
      `Γ_n = E_{a_S(n)}` of (4.2) (Lemma 3bis.1);
  (iii) its finite contact is `0` for every `t ≠ 0` with `|S_f| ≥ 2`
      (Corollary 3bis.3), and its archimedean invariant is the **density**
      `ω_∞(t) = K(|t|)` (Definition–Theorem 3bis.8), not an atom.  So
      `Frob_∞` carries exactly the invariant that `Frob_n` does not, and
      conversely (Corollary 3ter.10b).

*Proof.*  (i) `j_∞` is an injective homomorphism `R^× → C_S` (Paper 43 (9.5b)
and Lemma 3.3), and push-forward of point masses along a homomorphism is
multiplicative.  (ii) is Lemma 3bis.1.  (iii) is Corollary 3bis.3 and
Definition–Theorem 3bis.8, restricted to the positive component.  ∎  `PROVED`

**Remark 3ter.13a (the two Frobenius flows).**  Row A's declared trace has
exactly two kinds of local term, and §3ter exhibits the objects they measure:

    finite places    : Frob_n, n a prime power — DISCRETE, supported on the
                       fixed-point strata j_p(p^kZ_p^×); contact = ATOM of
                       mass Λ(n)n^{−1/2};
    archimedean place: Frob_∞(t), t ∈ R — a CONTINUOUS one-parameter group on
                       the slice Im j_∞; invariant = DENSITY K(|t|).

The finite family is a monoid with a true unit and proper idempotents
(Theorems 3ter.4, 3ter.7); the archimedean family is a group.  They meet only
at `n = 1`, `t = 0`, where both are `Δ`.  **No statement about zeros is made
or used**: the expansion `K(\log n) = n^{−1/2}Σ_{j≥0}n^{−2j}` of (3bis.11) is a
geometric series, and the explicit formula for a point class diverges
(Remark 3bis.8a).

### 3ter.5 The Frobenii are classes of the numerical object

**Theorem 3ter.14 (`Frob_n ∈ N_A^{dist}`).**  Let `n ≥ 2` and let
`F_{ε,N} := Frob_n^{[h_ε,N],\flat}` with `h_ε` an `L^1(d^*x_∞)`-normalized
bump satisfying (3ter.6).  Then:

  (i) `Frob_n ⋆ G^† ∈ D_A` for every `G ∈ D_A`, so
      `ℓ_n^{F}(G) := T(Frob_n⋆G^†) = I_A(Frob_n,G)` is defined, and
      `|\widehat{Frob_n}| ≤ 1` pointwise, whence `|ℓ_n^F(G)| ≤ N(G)` with `N`
      the seminorm (9.20a) of Paper 43 Lemma 9.14a0;
  (ii) `I_A(F_{ε,N},·) → ℓ_n^F` in the strong dual `D_A'` as `ε→0`, `N→∞`;
  (iii) `M(F_{ε,N}) → (n^{1/2},n^{−1/2}) = M(Frob_n)`;
  (iv) hence `J(Frob_n) := (ℓ_n^F,(n^{1/2},n^{−1/2})) ∈ N_A^{dist}`, with
      canonical primitive component `(ℓ_n^F, 0)` and **nonzero** ruling
      component `σ(n^{1/2},n^{−1/2})` (Paper 43 Theorem 9.14b).  In
      particular the Frobenius classes are **not primitive**.

*Proof.*  (i)  `Frob_n` is a compactly supported measure, so `Frob_n⋆G^†` is
smooth in `x_∞`, locally constant in the compact coordinates (it is an average
of translates of `G^†`, each locally constant, over a compact group, and the
average of a locally constant function over a compact subgroup is again
locally constant because the function is invariant under a fixed open
subgroup) and compactly supported.  For the Fourier transform: for a character
`χ` of `C_S`,

    \widehat{Frob_n}(χ) = ∫\overline{χ}\,dFrob_n
      = \overline{χ(c_n)}∫_{K_{P(n)}}\overline{χ(u)}\,du
      = \overline{χ(c_n)}·[\,χ|_{K_{P(n)}} = 1\,] ,

by orthogonality on the compact group `K_{P(n)}`; so `|\widehat{Frob_n}| ≤ 1`,
and the bound is Paper 43 (9.16)/Lemma 9.14a0.

(ii)  Let `B ⊆ D_A` be bounded.  By the proof of Paper 43 Lemma 9.14a0 there
are `N_B`, `d_{N_B}`, `C''_B` such that every `G ∈ B` is `U_{N_B}`-invariant,
`\hat G` is supported on `d_{N_B}` components of `\hat C_S`, and
`|\hat G(𝔠,τ)| ≤ C''_B\min(1,τ^{−2})`; and `|\hat T(𝔠,τ)| ≤ A_S +
B_S\log(2+|τ|)` by Theorem 9.7.  Take `N ≥ N_B`.  On a component carrying a
character `κ_r` trivial on `1+r^{N_B}Z_r ⊇ 1+r^NZ_r`, the `r`-factor of
`\hat F_{ε,N}` is
`vol(1+r^NZ_r)^{−1}∫_{n^{−1}(1+r^NZ_r)}\overline{κ_r(x)}dx =
\overline{κ_r(n^{−1})}`, which is **exactly** the `r`-factor of
`\widehat{Frob_n}`; and the `p`-factors (`p ∈ P(n)`) agree for the same reason
(both are `[κ_p = 1]\overline{κ_p(\cdot)}` computed on `Z_p^×`).  Hence on
every component met by `B`,

    \hat F_{ε,N}(χ) − \widehat{Frob_n}(χ)
      = \widehat{Frob_n}(χ)·\Big(\tfrac{\hat h_ε(τ)}{(1/n)^{−iτ}} − 1\Big) ,

whose modulus is `≤ \min(2, |τ|ε)` by `|e^{iθ}−e^{iθ'}| ≤ |θ−θ'|` and
`|\log x_∞ + \log n| ≤ ε` on `supp h_ε`.  The `R`-then-`ε` split then gives,
exactly as in Theorem 8.3(ii),

    \sup_{G∈B}|I_A(F_{ε,N},G) − ℓ_n^F(G)| ≤ C_B\,ε\,R^2\log R + η(R) ,
    η(R) := 2C''_B∫_{|τ|>R}τ^{−2}(A_S+B_S\log(2+|τ|))\tfrac{dτ}{2π} → 0 ,

**[REBUILT, phase 131, round 4, finding `F6`: the round-3 display read
`Rε·N_B`, which suppresses the symbol growth on `|τ| ≤ R`.  The honest bound
combines `|\hat F_{ε,N}−\widehat{Frob_n}| ≤ |τ|ε` with
`|\hat G| ≤ C''_B\min(1,τ^{−2})` and `|\hat T| ≤ A_S+B_S\log(2+|τ|)`, giving
`∫_{|τ|≤R}|τ|ε·C''_B·(A_S+B_S\log(2+|τ|))dτ/2π ≤ C_B\,ε\,R^2\log R`.  The
`R`-then-`ε` order is unaffected and the theorem stands.]**

uniformly on `B`; choose `R` then `ε`.

(iii)  `λ_∓(F_{ε,N}) = ∫F_{ε,N}(w)|w|_S^{∓1/2}d^*w = ∫h_ε(x)|x|^{∓1/2}d^*x_∞
→ n^{±1/2}` since `h_ε` concentrates at `x = 1/n` with unit mass.

(iv)  `J(F) = (I_A(F,·),M(F))` (Paper 43 (9.18)); combine (ii),(iii); each
`J(F_{ε,N}) ∈ J(N_A)` so the limit is in `N_A^{dist}`.  The splitting is
Theorem 9.14b, and `M(Frob_n) ≠ 0`.  ∎  `PROVED`


## 4. The source category and its realization (clauses B.1–B.3)

### 4.1 The source

**Definition 4.1 (the arithmetic label category `W`).**  `W` has objects the
integers `n ≥ 1`.  There is exactly one morphism `d → n` when `d | n`, and
none otherwise; composition is transitivity of divisibility.  The monoidal
product is `n ⊗ m = nm` on objects, and on morphisms `(d→n) ⊗ (e→m) =
(de → nm)`, which is well defined because `d|n` and `e|m` imply `de|nm`.  The
unit is `1`.  `W` is a symmetric monoidal poset category.

Two structures are carried by `W` and must be kept apart, because the whole
of §5 turns on the distinction:

- the **monoid** `(N_{≥1}, ×)` of objects, which the realization will
  preserve;
- the **divisor poset** `D(n) = {d : d|n}` for each `n`, whose arrows are the
  `i_{d,n}` of P123.037 §1 and whose cube is the site of primitive extraction.

This is exactly the structure P123.037 §1 verified on complexes: the maps
`i_{d,n} = (id, n/d)` satisfy `i_{b,n} i_{d,b} = i_{d,n}` **literally**, so
`d ↦ C_d` is a strict functor `D(n) → Ch(Z)`, not a diagram commuting up to
coherent homotopy.  `PROVED-IN-REPOSITORY` (P123.037 §1).

**Remark 4.2 (what "Witt/cyclotomic source" should mean).**  §6.1 of the
closure plan asked for "the Witt/cyclotomic category of origin, its morphisms
and its operation", warning that an equality of Witt rings with certain finite
cycles is not yet a monoidal functor.  Definition 4.1 is that category in the
only form the construction needs: the divisor poset is the indexing site of
the necklace/Möbius operation that carries `log` to `Λ`, and the multiplicative
monoid is what the realization must respect.  Theorem 5.4 proves that no
category can carry both structures to one monoidal functor, so this separation
is not a convenience.

### 4.2 The realization

Fix a chart `S` and, for `n ≥ 1`, the semilocal idele of P123.038 §1

    a_S(n) = (1 at ∞ ; n at each finite place of S),
    a_S(m) a_S(n) = a_S(mn),                                          (4.1)

and set

    Γ_n := E_{β_{a_S(n)}} ∈ G.                                        (4.2)

**Theorem 4.3 (B.2: monoidal on the label monoid only).**  **[CORRECTED, phase
128 B9:]** there is **no** functor `W → G`.  By P123.082, `Hom(Γ_d,Γ_n) = 0`
for distinct classes, so the divisor morphisms of `W` have no image in `G`;
only the monoid of objects is realized, and the poset is realized in a
different target (`Ch(Z)`), with no comparison functor between the two.  The
symmetry of `W` asserted in Definition 4.1 is likewise not realized.  What is
proved is: `n ↦ Γ_n` is a strong monoidal functor from the monoid
`(N_{≥1}, ×)` to `(G, ⋆)`:

    Γ_m ⋆ Γ_n ≅ Γ_{mn},        Γ_1 = Δ,                               (4.3)

with the associativity and unit coherences of `G`.  Moreover the class of
`Γ_n` is independent of the chosen lift of the external class, of the
uniformizers, and of the chart, in the following exact senses:

  (a) *gauge*: the finite arithmetic anchor `b_S(a) = a_f / a_∞` of P123.038
      §2 is invariant under `a ↦ γa` for a positive rational `S`-unit `γ`,
      is multiplicative, and takes the value `n` on both `a_S(n)` and its
      normalized representative `h_S(n)`; hence the invariant lattice `nL_S`
      is attached to the class, not to the lift;
  (b) *charts*: for `S ⊆ T`, the lift transition of P123.020 satisfies
      `L_{ST}(a_S(n)) = a_T(n)` literally, and the coordinate projection
      `L_T → L_S` is a quasi-isomorphism `Q_{T,n} → Q_{S,n}` of index
      complexes, composing exactly on chart triples and commuting with all
      divisor maps.

*Proof.*  (4.3) is (4.1) together with `E_u ⋆ E_v ≅ E_{uv}` (Paper 43 (3.2);
P123.016 (3.1)–(3.3), P123.019) and `E_1 = Δ`.  Coherence is P123.019 §4, which proves associativity for
`μ_{β,η}(x⊗y) = xβ(y)` on elementary tensors and extends it by density; the
first version cited Paper 43 Prop. 3.2, which says nothing about associators.  (a) is P123.038 §2; (b) is P123.038 §1 and §3, the
kernel of the projection being multiplication by `n` on the added `Z_p` with
`p ∤ n`, hence contractible.  ∎  `PROVED` (assembly), with (a),(b)
`PROVED-IN-REPOSITORY`.

**Theorem 4.4 (B.3: unit, transpose, half-density).**

  (i) `Γ_1 = Δ` is the monoidal unit of `G` and `Δ^† = Δ`.
  (ii) `Γ_n^† = E_{a_S(n)^{−1}}`, an object of `G`, and `(Γ_m ⋆ Γ_n)^† ≅
       Γ_n^† ⋆ Γ_m^†`.
  (iii) The half-density of `Γ_n` is canonical: `|a_S(n)|_S = 1/n`, so the
       half-density weight is `n^{−1/2}`, and the product formula
       (`|γ|_S = 1` for `γ ∈ Γ_S`) makes it independent of the lift.  There is
       no two-torsion ambiguity.

*Proof.*  (i),(ii) are Paper 43 Def. 5.2 and Thm. 5.3 applied to the objects
(4.2).  (iii): `a_S(n)` has entry `1` at `∞` and `n` at every `p ∈ S_f`, and
`S` contains every prime dividing `n`, so `|a_S(n)|_S = ∏_{p∈S_f}|n|_p =
∏_{p finite}|n|_p = |n|_∞^{−1} = 1/n`.  Canonicity of `h = |·|_S^{−1/2}` is
Paper 43 §5.2 (P123.074).  ∎  `PROVED`

**Lemma 4.5 (the local factor is inversion-invariant).**  For every place `v`
and every `σ_v ≠ 1`,

    τ_v(σ_v^{−1}) = τ_v(σ_v).                                         (4.4)

*Proof.*  `|1 − σ^{−1}|_v = |σ^{−1}|_v · |σ − 1|_v = |σ|_v^{−1}|1−σ|_v`, so

    τ_v(σ^{−1}) = |σ|_v^{−1/2} / ( |σ|_v^{−1}|1−σ|_v )
                = |σ|_v^{1/2} / |1−σ|_v = τ_v(σ).   ∎

This computation already appears inside the proof of Paper 43 Thm. 9.4, where
it establishes `†`-stability of the numerical radical; it is isolated here
because for row B its place-wise form is what carries content.
`PROVED-IN-REPOSITORY` (Paper 43 Thm. 9.4).

**Corollary 4.6.**  `T(Γ_n^†) = T(Γ_n)` place by place; in particular
`w_ram` and `w_unit` are separately invariant under `†`.  **[CORRECTED, phase 128 B9:]** the first version called this "the exact source"
of the symmetric pair `h(log n)+h(−log n)` in P123.039 §4.  It is not: there
that pair is part of the *definition* of `w_n(h)`.  The correct statement is
that `†`-invariance of the local weight is **consistent** with the symmetric
form of `w_n(h)`.  ∎  `PROVED`

**Remark 4.7.**  Lemma 4.5 also removes an apparent discrepancy in the
stopping rule of §6 of the closure plan, which describes the linear-dilation
contact through `1 − u^{−1}` while P123.060 computes it through `1 − u`.  By
(4.4) the analytic factor does not distinguish them; the integral complexes
`[Z→1−u→Z]` and `[Z→1−u^{−1}→Z]` differ by the unit `u^{−1}` when `u` is
invertible, hence are isomorphic.  The comparison of clause B.7 is therefore
unambiguous, and is carried out in Theorem 6.4.

---

## 5. Primitive extraction is Möbius inversion, and cannot be monoidal
   (clauses B.5, B.6)

### 5.1 The categorified Möbius identity

**Lemma 5.1.**  Let `n ≥ 1`, `P(n)` its set of distinct prime divisors, and
`f` any function on the divisors of `n` with values in an abelian group.  Then

    Σ_{J ⊆ P(n)} (−1)^{|J|} f( n / ∏_{p∈J} p )  =  Σ_{d | n} μ(d) f(n/d).  (5.1)

*Proof.*  `μ(d) = 0` unless `d` is squarefree, so the right side is supported
on the squarefree divisors of `n`.  The map `J ↦ ∏_{p∈J} p` is a bijection
from subsets of `P(n)` onto the squarefree divisors of `n`, and
`μ(∏_{p∈J}p) = (−1)^{|J|}`.  Substituting gives the left side.  ∎  `PROVED`

So the cube of P123.037 §3 — vertices `C_{n/∏_J p}`, edges `i_{d,pd}`, total
cofiber `Prim_n` — is a categorification of Möbius inversion over the divisor
poset, and its Euler-type invariants compute `μ ∗ f`.

**Definition 5.1a (the radical cube and `Prim`).**  **[ADDED ; see
§12.]**  Let `N > 1` and let `∅ ≠ P ⊆ P(N)`.  The **radical cube** of `(N,P)`
is the `|P|`-dimensional commutative cube

    J ↦ C_ram( N / ∏_{p∈J} p ) ,      J ⊆ P ,

whose edge in the direction `q`, from the vertex at `J∪{q}` to the vertex at
`J`, is the chain map `i_{d,qd} = (id, q)` with `d = N/(q∏_J p)`.  Write
`Prim(N,P)` for its total cofiber and put `Prim_n := Prim(n, P(n))` for
`n > 1`.  The cube is indexed by the **radical** divisors, not by all divisors
of `n`: for `n = p^k` the divisor poset is a chain of length `k`, whereas the
radical cube is the single edge `C_ram(p^{k−1}) → C_ram(p^k)`.  The squares
commute strictly — in degree `−1` both composites are the identity, in degree
`0` both are multiplication by the same integer — so no coherence data are
needed.

**Lemma 5.1b (structure of the radical cofiber).**  **[ADDED 2026-09-13.]**
Let `N > 1` and `∅ ≠ P ⊆ P(N)`.  Then `Prim(N,P) ≃ Z/q` in degree `0`, i.e.
`≃ [Z →q→ Z]`, when `P = {q}`; and `Prim(N,P) ≃ 0` when `|P| ≥ 2`.  In
particular, for `n > 1`,

    Prim_n ≃ [Z →Φ_n(1)→ Z] ,   H^{−1}Prim_n = 0 ,  H^0Prim_n = Z/Φ_n(1) ,

so `Prim_n ≅ Z/p` in degree `0` when `n = p^k` and `Prim_n ≃ 0` when `n` has
at least two prime divisors.

*Proof.*  Induction on `r = |P|`.

*Base `r = 1`, `P = {q}`.*  The cube is the single edge
`i = (id,q) : C_ram(N/q) → C_ram(N)`, and its total cofiber is `Cone(i)`.  The
map `i` is injective in each degree — the identity in degree `−1`,
multiplication by `q` in degree `0` — so `Cone(i)` is quasi-isomorphic to the
degreewise cokernel `[0 → Z/q]`, concentrated in degree `0`.  Since
`[Z →q→ Z]` is a free resolution of `Z/q`, this is `[Z →q→ Z]` in `D(Z)`.

*Step `r ≥ 2`.*  Fix `q ∈ P`, `P' := P∖{q}`.  Splitting the cube along the
direction `q` exhibits it as a map of `(r−1)`-cubes: the face `{J : q ∉ J}` is
the radical cube of `(N,P')`, the face `{J : q ∈ J}` is the radical cube of
`(N/q,P')`, and the direction-`q` edges give a map `φ` from the second to the
first.  Total cofibers being iterated cones, taken in any order,

    Prim(N,P) = Cone( φ_* : Prim(N/q,P') → Prim(N,P') ) .

If `r ≥ 3` then `|P'| ≥ 2`, both source and target are acyclic by induction,
and the cone is acyclic.  If `r = 2`, write `P = {q,q'}`.  By the base case
`Prim(N,{q'})` is `Z/q'` presented as the degree-`0` term of `C_ram(N)` modulo
`q'`, and `Prim(N/q,{q'})` is `Z/q'` presented as the degree-`0` term of
`C_ram(N/q)` modulo `q'`.  The direction-`q` edges are `(id,q)` in both cases,
so `φ_*` is multiplication by `q` on `Z/q'`; as `q ≠ q'` are distinct primes,
`q` is invertible mod `q'`, `φ_*` is an isomorphism, and the cone is acyclic.

*Consequence.*  If `n = p^k` then `P(n) = {p}` and the base case gives `Z/p`;
and `Φ_{p^k}(x) = Φ_p(x^{p^{k−1}})` gives `Φ_{p^k}(1) = p`.  If `|P(n)| ≥ 2`
then `Prim_n ≃ 0` and `Φ_n(1) = 1`, so `[Z →Φ_n(1)→ Z]` is acyclic too.  ∎
`PROVED`

**Definition 5.2.**  For a perfect two-term complex `K = [Z →m→ Z]` with
`m ≠ 0`, set `deg_det K := log # H⁰(K) = log|m|`; extend additively to finite
direct sums, with a sign reversal on shifts, and by the cone law to total
cofibers.  For `m = 0` (the contractible-after-inversion case `n=1`) the
invariant is `0`.

### 5.2 The degree law

**Theorem 5.3 (B.5).**  For every `n > 1`,

    deg_det Prim_n = Σ_{d|n} μ(d) · deg_det C_ram(n/d)
                   = Σ_{d|n} μ(d) log(n/d)
                   = Λ(n) = log|Φ_n(1)|,                              (5.2)

(the structure of `Prim_n` itself is **Lemma 5.1b**, proved there by induction
on `|P(n)|`; **[CORRECTED : this theorem previously asserted
`Prim_n ≅ Z/p` resp. `0` and proved only the degree identity, while Theorem
6.3(a) deduced the structure from this theorem — a citation loop.  The
structural claim is now Lemma 5.1b and is proved; see §12]**).  For `n = 1` the
complex `C_ram(1)` is contractible
and `Γ_1 = Δ`; the identity label is treated as identity/excess by Paper 43
Definition 8.6's identity-class term `c·F(1)` with `c := 0`
(Definition 8A.7d) and **not** by (5.2).  **[REBUILT, phase 131, round 2,
`F12`(c): the round-1 citation to Paper 43 "Def. 8.1 (the renormalized
relative determinant at the identity)" is to the **withdrawn** definition
(Paper 43 §13.6).]**

*Proof.*  `deg_det C_ram(d) = log # (Z/d) = log d` by (3.2) and Definition
5.2.  The cone law applied along each cube direction gives that `deg_det` of
the total cofiber is the alternating sum of the vertex degrees; by Lemma 5.1
that alternating sum is `Σ_{d|n} μ(d) log(n/d)`.  Since `Σ_{d|n} μ(d) = 0` for
`n>1`, this equals `−Σ_{d|n} μ(d) log d = Λ(n)`, the classical identity
`Λ = μ ∗ log`.  (The `deg_det` of the total cofiber may equally be read off
Lemma 5.1b, which gives `deg_det Prim_n = log Φ_n(1)` directly.)  The equality
`log|Φ_n(1)| = Λ(n)` on the nose follows from `∏_{d|n}Φ_d(x) = x^n−1` and
multiplicative Möbius inversion, and is also recorded in P123.037 §3–§4
(theorem and table),
P123.038 §4 (the same cube on the arithmetic lattice), and P123.039 §3
(`det(1−T|V_n) = ∏_{d|n} d^{μ(n/d)}`, equal to `p` for `n=p^k` and `1`
otherwise).  ∎  `PROVED`, with the object-level identifications
`PROVED-IN-REPOSITORY`.

**Corollary 5.3a (the ghost relation).**  `deg_det C_ram(n) = Σ_{d|n}
deg_det Prim_d`, i.e. `log n = Σ_{d|n} Λ(d)`.  The index degree of `Γ_n` is
the sum of the primitive degrees of its divisors.  ∎  `PROVED` (Möbius
inversion of (5.2)).

### 5.3 Why primitive extraction is not, and must not be, monoidal

The closure plan (§6.6) and P123.037 §5 and P123.038 §5 all record the same
open item: primitive extraction "has not been shown to commute monoidally with
multiplication of labels".  It cannot.

**Theorem 5.4 (`Prim` is not monoidal for `⊗^L`).**  In `D(Z)`,

    Prim_2 ⊗^L Prim_2 = Z/2 ⊗^L Z/2 = Z/2 ⊕ Z/2[1]  ≇  Z/2 = Prim_4.

Hence there is no natural isomorphism `Prim_m ⊗^L Prim_n ≅ Prim_{mn}`.

*Proof.*  Resolve `Z/2` by `[Z →2→ Z]` and tensor with `Z/2`: the complex
becomes `[Z/2 →0→ Z/2]` with zero differential, so `H_0 = Z/2` and
`H_1 = Tor_1^Z(Z/2,Z/2) = Z/2`, and the complex splits.  By Theorem 5.3,
`Prim_4 ≅ Z/2` concentrated in degree `0`.  ∎  `PROVED`

**[CORRECTED, phase 128 B8.]**  The first version proved instead that no
functor with an *additive degree* can have `deg Prim_n = Λ(n)`, from
`Λ(6) = 0 ≠ Λ(2)+Λ(3)`.  That is true but refutes a conjunct nobody asserted:
the open item of P123.037 §5 is object-level — "transitivity (1.2) is an exact
triangle, not such an isomorphism".  The theorem above settles that item
properly.  The degree observation is retained as a corollary.

**Corollary 5.5a.**  Since `Λ(6) = 0 ≠ Λ(2)+Λ(3) = log 6`, no monoidal `Prim`
with an additive degree invariant can satisfy `deg Prim_n = Λ(n)` either.

**Corollary 5.5 (the structure that does hold).**

  (i) the realization `Γ : (N_{≥1},×) → (G,⋆)` **is** strong monoidal
      (Theorem 4.3), and its degree `deg_det C_ram(n) = log n` **is** additive;
  (ii) primitive extraction is the Möbius operation of the divisor **poset**,
      not of the monoid (Lemma 5.1);
  (iii) the two are compatible exactly through Corollary 5.3a.

So the open item of P123.037 §5 is now **closed by refutation at the object
level** (Theorem 5.4), not reclassified.  ∎  `PROVED`

**Remark 5.6.**  This is also why the divisor cube must live on the *shadow
target* and not on correspondences.  By Paper 43 (3.3) (P123.082),
`Hom_{U-U}(Γ_d, Γ_n) = 0` for `d ≠ n` unless the classes differ by a gauge
unit, so the divisor arrows `i_{d,n}` have no realization as morphisms of
correspondences in `G`.  They are realized, strictly, on the index complexes
`Q_{S,d} → Q_{S,n}` of P123.038 §3.  **[CORRECTED, phase 128 B9:]** the first
version called these "the shadow target".  They are not: Paper 43's shadow of
`Γ_n` is Thm. 7.1(c) and is not `Q_{S,n}` (§6.2a).  They are an **auxiliary
`Z`-linear model indexed by the same labels**, and P123.082's own conclusion —
that the source category must contain additional non-invertible or localized
objects — stands untouched.

---

## 6. The contact of `Γ_n` computed in row A's category (clauses B.4, B.7)

### 6.1 The index complex and the missing arrow

**Theorem 6.1 (the lattice index is the ramified half of the shadow).**
Let `n ≥ 2` and `S ⊇ {∞} ∪ P(n)`.  Put `Q_{S,n} := [L_S →n→ L_S]` in degrees
`−1,0`.  Then:

  (i) `Q_{S,n}` is perfect and the diagonal `Z → L_S` induces a
      quasi-isomorphism `C_ram(n) → Q_{S,n}`, naturally on the whole divisor
      cube;
  (ii) `[L_S : nL_S] = n = |a_S(n)|_S^{−1}`, the inverse Tate modulus of the
      correspondence;
  (iii) **(a definitional identity, not the missing arrow — see the
      correction below)**

        − 2 log w_ram(Γ_n) = log [L_S : nL_S] = deg_det C_ram(n) = log n. (6.1)

*Proof.*  (i) and (ii) are P123.038 §3 and §4: the cokernel of `n` on `L_S`
is `∏_{p∈S_f} Z_p/nZ_p ≅ Z/n` by primary decomposition, since `S` contains
every prime dividing `n`; the divisor maps `(id, n/d)` commute strictly with
the diagonal, and the chart projections are quasi-isomorphisms.
(iii): by Theorem 3.3(iii)–(3.4), `w_ram(Γ_n) = ∏_{p|n}|n|_p^{1/2} =
n^{−1/2}`, so `−2 log w_ram(Γ_n) = log n`; and `deg_det C_ram(n) = log n` by
Definition 5.2.  ∎  `PROVED`

Equation (6.1) is the arrow that P123.038 §5 and P123.039 §5 declared missing
("the lattice-index operation must be realized as the admissible diagonal
shadow"; "`T_n` is the finite translation, not the external dilation `E_n`").
It is supplied without identifying `T_n` with `E_n`: what is proved is that
the **half-density of the external dilation is the square root of the inverse
index of that same dilation on its invariant lattice**, and that this index is
the determinant of the ramification contact.  The finite translation `T`
enters only in §6.2, as the canonical automorphism of the quotient
`L_S/nL_S`, which both constructions produce.

**[REBUILT, phase 131.]**  Phase-128 finding `B2` is right that (6.1) is a
**definitional identity** and therefore not by itself the missing arrow, and
that assessment is kept.  The arrow P123.038 §5 asked for — the comparison of
the lattice-index operation *with the analytic trace* — is supplied instead by
Theorem 3bis.10(ii),

    \log[L_S:nL_S] = \log n = Σ_{d|n}Λ(d)
                  = Σ_{d|n} d^{1/2}·contact_{fin}(Γ_d^{rad}) ,

whose two sides are computed independently: the left from `L_S/nL_S` over `Z`,
the right from Paper 43 (8.5) and the shell volumes of P123.042 §1.  See
Remark 3bis.10b.

**Remark 6.2 (what the complex shadow does and does not see).**  Over `C` the
torsion disappears: by Paper 43 Thm. 7.1(c) the shadow of `Γ_n` at a finite
place `p | n` is the rank-one class of the fixed point `0`, and P123.037 §5
notes that complexification kills the finite torsion.  The integral
information is carried by the lattice `L_S ⊂ X_S`, which is part of the
coefficient geometry (the chart transitions already use `1_{Z_p}`, P123.038
§2), and the only trace of it in the analytic invariant is the half-density
exponent.  Theorem 6.1(iii) says that this trace is **complete**: the
half-density determines `log n`, and `log n` determines the perfect complex
`C_ram(n)` up to quasi-isomorphism, since a two-term complex `[Z→m→Z]` with
`m>0` is determined by `m`.  No information is lost in the passage, and none
is smuggled in.

### 6.2 The primitive contact, three ways

### 6.2a Clause B.4 is false as stated, and what replaces it

**[CORRECTED, phase 128 B3.]**  Two separate facts, both verified.

  (i) **The literal clause is false.**  `LΔ^*Γ_n`, the derived pullback of the
      graph along the diagonal, is the **fixed** complex, with differential
      `n−1` and `H⁰ = Z/(n−1)` (P123.060 (1.1)–(2.1)).  It is not
      `[Z→Φ_n(1)→Z]`, and P123.060 §3 proves it cannot be: at `n = p^k`
      localized at `p`, the fixed complex is contractible while the primitive
      ramification complex has cohomology `Z/p`.  So the closure plan's B.4
      conflates the diagonal contact with the ramification contact.
  (ii) **None of the four constructions below is an operation on `Γ_n ∈ G`.**
      They are a cotangent complex on `G_m/Z`, a complex of abelian groups on
      `L_S`, an operator on `Z[L_S/nL_S]`, and a Koszul complex in `Z[t,z]`.
      The actual derived self-contact of `Γ_n` in `G` is Paper 43 Thm. 7.1(c)
      and is `C[0]` at `p|n`, independent of the twist.  A `C`-linear shadow
      cannot carry `Z/p`; P123.022 records the corresponding statement as
      `REFUTED` for additive contact functors.

So B.4 is replaced by: *the arithmetic contact of row B is the **ramification**
contact, constructed on the integral lattice `L_S ⊂ X_S`, which is part of the
declared coefficient geometry (P123.038 §2); its realization as a shadow of the
`C`-linear sector `G` is `OPEN` and requires an integral carrier.*  This is the
contact rows C and D actually use, through its degree.

#### 6.2a′ The amended clause B.4, stated and proved

**[REBUILT, phase 131.]**  The replacement above is correct but incomplete: it
says what the contact is **not** computed in, and leaves the clause with no
positive statement inside the declared category.  The amended clause supplies
one.  It is stated for the **norm** class, which is the object the clause
should have been about.

> **Clause B.4, amended — ACCEPTED by the repository author on  (mirrors the A.6 amendment of
> Paper 43 §14.2).**  **[REBUILT, phase 131, round 2, finding `F2` of
> `R131.002` and `F5` of `R131.003`.]**  The derived contact of the norm class
> `Γ_n^{rad}` with the diagonal, computed in the declared category — that is,
> the **mass at `t = \log n` of the unique finite-place Radon measure
> `ω_{fin}` representing `T` on the radial sector `D_A^{rad} ∩ D_A^0`**
> (Theorem 3bis.7; existence and uniqueness are Definition–Theorem 3bis.8,
> uniqueness because a Radon measure on `R∖\{0\}` is determined by its
> integrals against `C_c^∞` tests), whose integrand is, place by place, the
> Haar-regularized rank of the relative Hochschild shadow times the
> half-density–Lefschetz weight (Paper 43 Theorem 7.1, Theorem 8A.9
> (8A.24)–(8A.24′)) — equals `Λ(n)n^{−1/2}`, which equals
> `n^{−1/2}·deg_det[Z →Φ_n(1)→ Z]`, the integral cotangent model of P123.037
> transported to the lattice `L_S ⊂ X_S` (P123.038).  The identification is of
> **degrees**.  An object-level identification is impossible in a `C`-linear
> category (P123.022).

**[phase 133: the accepted text above is reproduced verbatim and is not
edited.  Its `D_A^0` is the **off-identity** set of Paper 43 §8, renamed
`D_A^{off}` in phase 133; it is not Paper 43 Definition 9.10's primitive
sector.  The same applies to the copy of this text in the §10 clause table
(clause B.4).]**

Four remarks on the wording before the proof.

0. *`T(Γ_n^{rad})` is undefined, and the amendment does not use it.*
   **[REBUILT, phase 131, round 2, finding `F2`.]**  `T` is a functional on
   `D_A` (Paper 43 Definition 8.6) and `Γ_n^{rad} ∉ D_A`
   (Remark 3bis.4b(i)); this paper never extends `T` to multipliers.
   Moreover the naive place-wise extension `W_p(μ) := ∫(μ∘j_p)τ_p\,d^*x`
   returns **`0`**, not `Λ(n)n^{−1/2}`, because for `|S_f| ≥ 2` the set
   `Im\,j_p ∩ \{|x|_S = 1/n\}` is `Γ_n^{rad}`-null (Proposition 3bis.2's
   computation).  The round-1 wording of this box said "the value on
   `Γ_n^{rad}` of `T`" and was therefore ill-typed — the same type error the
   construction charged against the earlier blueprint.  It is replaced by the
   representing-measure formulation, which is a **theorem** (existence and
   uniqueness, Definition–Theorem 3bis.8), not a free definition.
1. *Why the atom of `ω_{fin}` is the right reading of "derived contact with
   the diagonal".*  The diagonal `Δ = E_1` is a **multiplier** of the Fell
   core and not an element of it (Paper 43 Remark 8.11), so `T(Δ)` is
   undefined and the literal pullback `LΔ^*` is unavailable on the trace side.
   What the declared category supplies is Paper 43 Theorem 8A.9: `T` is the
   **Haar-regularized Lefschetz number** of the categorical shadow, with the
   fixed-point weight `1/|1−σ|_v` and the half-density `|σ|_v^{1/2}` appearing
   separately and explicitly.  Disintegrated along the radial family, its
   finite part is `ω_{fin}`, and the contact of a single label is the mass
   `ω_{fin}` puts at that label — which by Theorem 3bis.7′ is nonzero exactly
   at the prime powers.
2. *Why `Γ_n^{rad}` and not `Γ_n`.*  By Corollary 3bis.3 (`|S_f| ≥ 2`) and
   Remark 3bis.2a(ii) (`|S_f| = 1`) the element class has finite contact `0`
   on every chart; the clause as originally written had no object.
3. *Why "degrees".*  Because of (ii) of §6.2a above, which is unchanged.

**Theorem 6.3a (clause B.4 as amended: `PROVED`).**  Let `n ≥ 2` and let `S`
be a chart with `S_f ≠ ∅`.  Then, with `c := 0` (Paper 43 Def. 8A.7d):

  (i) *the contact exists, is unique, and is computed in the declared
      category.*  The finite-place part of `T` on the radial sector is
      represented by the **unique** Radon measure `ω_{fin}` of (3bis.9)
      (Definition–Theorem 3bis.8), and

        contact_{fin}(Γ_n^{rad}) = ω_{fin}(\{\log n\}) = Λ(n)\,n^{−1/2} ,

      with `Λ(n) = 0` unless `n = p^k` with `p ∈ S_f`, and
      `Λ(p^k) = \log p = vol_{d^*x}(p^kZ_p^×)`;
  (ii) *the integrand is the Lefschetz integrand of Paper 43 Theorem 8A.9.*
      At the shell `p^kZ_p^×`, `k ≥ 1`, the shadow factor is the rank-one
      origin class `C[0]` (Theorem 7.1(c)), the fixed-point weight is
      `1/|1−p^ku|_p = 1`, the half-density is `|p^k|_p^{1/2} = p^{−k/2}`, and
      the Haar weight of the shell is `\log p`.  So the contact is
      `(\text{rank }1)×(\text{Lefschetz }1)×(\text{half-density }p^{−k/2})×
      (\text{shell volume }\log p)`;
  (iii) *degree identity.*  `Λ(n) = deg_det Prim_n = \log\#H^0[Z→Φ_n(1)→Z]
      = \log|\det(1−T|V_n)|`, hence

        contact_{fin}(Γ_n^{rad}) = n^{−1/2}·deg_det\,[\,Z →Φ_n(1)→ Z\,] ;

  (iv) *the identification is of degrees only, and cannot be more.*  There is
      no additive contact functor from the `C`-linear declared category
      carrying `Γ_n^{rad}` to a complex with cohomology `Z/p` (P123.022,
      `REFUTED`), and the shadow of the class at `p | n` is `C[0]`
      (Theorem 7.1(c) of Paper 43).

*Proof.*  (i) is Theorem 3bis.7 together with Definition–Theorem 3bis.8; the
computation is an application of Paper 43 Theorem 8.8 to `Γ_h ∈ D_A^{off}`, so it
is absolutely convergent, needs no regularization, and does not depend on `c`.

(ii) `τ_p(p^ku) = |p^k|_p^{1/2}/|1−p^ku|_p`; for `k ≥ 1`, `|p^ku|_p < 1` gives
`|1−p^ku|_p = 1`, so the Lefschetz factor is `1` and `τ_p = p^{−k/2}` (Paper
43 Lemma 8.2(i)).  Paper 43 Theorem 8A.9(a) is precisely the statement that at
a non-unit shell the shadow factor has rank one and the whole weight is the
half-density–Lefschetz factor, and (8A.24′) records the split
`rk^{Haar} = 1`, `w_p = τ_p` there.  The shell volume is P123.042 §1.
Multiplying, the shell `k` contributes `(\log p)p^{−k/2}`, which for `n = p^k`
is `Λ(n)n^{−1/2}`.

(iii) is Theorem 5.3 (`deg_det Prim_n = Λ(n) = \log|Φ_n(1)|`) and
Theorem 6.3(c) (`\det(1−T|V_n) = Φ_n(1)`, P123.039 §3), combined with (i).

(iv) is §6.2a(ii) and P123.022's verdict block, quoted there.  ∎  `PROVED`
(the amended clause), with the `Z`-linear components `PROVED` in §5–6.2 and
`CONSTRUCTED-IN-REPOSITORY` at the object level.

**Remark 6.3b (what the amendment does not buy).**  It does not close the item
"realization of the integral contact as a shadow of `G`", which remains
`OPEN` and, at object level, `REFUTED` for additive `C`-linear contact
functors (P123.022).  It does not produce an integral carrier.  It replaces an
unprovable clause by a provable one of the same shape — a **degree**
identity between the declared category's Lefschetz integrand and the integral
cyclotomic model — and it names the object the clause is about.  Whether that
is an acceptable amendment is the author's decision, exactly as with A.6.

**Theorem 6.3 (B.4 as replaced; four `Z`-linear models).**  For `n > 1` the primitive contact of `Γ_n` is the
perfect complex

    K_n := [Z →Φ_n(1)→ Z],        H⁰ = Z/Φ_n(1),  H^{−1} = 0,         (6.2)

with no truncation, and the following four constructions agree in `D(Z)`:

  (a) `Prim_n`, the total cofiber of the divisor cube of `C_ram(·)`
      (P123.037 §3);
  (b) the same cube taken on the arithmetic lattice complexes `Q_{S,·}`
      (P123.038 §4), via the natural quasi-isomorphism of Theorem 6.1(i);
  (c) `D_n = [V_n →1−T→ V_n]` where `V_n = Z[T]/Φ_n(T)` inside the orbit
      module `Z[L_S/nL_S]` and `T` is translation by the class of the
      diagonal integer `1`, with `H⁰(D_n) = Z/Φ_n(1)` and
      `det(1−T|V_n) = Φ_n(1)` (P123.039 §1, P123.038 §5);
  (d) `K_prim(n,t) = [Z[t] →Φ_n(1)→ Z[t]]`, the derived intersection of the
      primitive cyclotomic factor `P_n(t,z) = Φ_n(1+tz)` of the relative
      fibre with the zero section, constant in `t` and specializing to (6.2)
      at every `t = c` (P123.061 §2).

*Proof.*  (a) is **Lemma 5.1b** (`H^{−1}Prim_n = 0`, `H⁰Prim_n = Z/Φ_n(1)`),
in agreement with P123.037 §3 and its §4 identification with the unit
cyclotomic contact `K_n^W` of P123.022–025; **[CORRECTED : (a)
previously cited Theorem 5.3 for the structure, which cited this theorem in
return]** (b) follows from (a) by
the natural quasi-isomorphism of the whole cube (P123.038 (4.1), Theorem
6.1(i)); (c) is P123.039 §1 (1.1) with P123.038 §5, which identifies the
primitive submodule of `Z[L_S/nL_S]` with `V_n`; (d) is the Koszul resolution
of the nonzerodivisor `P_n` in `Z[t,z]` (P123.061 (2.1)–(2.2)), with the
cited proof that ordinary and derived specialization agree because
`P_n(0,z) = Φ_n(1) ≠ 0`.  All four have `H^{−1} = 0` and `H⁰ = Z/Φ_n(1)`,
and (6.2) is a free resolution, so the agreement is an isomorphism in `D(Z)`,
not an equality of orders.  `PROVED` (assembly); the components are
`CONSTRUCTED-IN-REPOSITORY` — P123.037, P123.038 and P123.039 all carry the
status `CONSTRUCTED` with their object-level calculations proved and their
comparison with the shadow explicitly `OPEN`.  **[CORRECTED, phase 128 B9]**
"four independent constructions" is an overclaim: (b) is transported from (a)
by Theorem 6.1(i), and (c) is built on the same finite quotient.  There are two
routes — the cotangent/lattice cube and the deformation Koszul of P123.061 —
plus two transports.  ∎

Combining Theorem 6.3 with Theorem 5.3 gives clause B.5 in the form demanded
by the closure plan:

    deg_det(contact of Γ_n) = log|Φ_n(1)| = Λ(n),
    analytic weight of Γ_n  = n^{−1/2},                               (6.3)

the second by Theorem 4.4(iii) and (3.4), unchanged by primitive extraction
because extraction acts on the divisor cube of contacts and not on the label.

### 6.3 The discriminating test (clause B.7)

The closure plan requires this comparison with rings and valuations for `p`
and `p²`, and, if the two differ, the location of the geometric mechanism
producing the cyclotomic factor.

**Theorem 6.4.**  Let `p` be a prime.

  (i) *Linear-dilation (fixed) contact.*  `C_fix(p) = [Z →p−1→ Z]`, with
      `H⁰ = Z/(p−1)`; `C_fix(p²) = [Z →p²−1→ Z]`, with `H⁰ = Z/(p²−1)`.
      Localized at `p`: `p−1` and `p²−1` are units in `Z_p`, so both complexes
      are **contractible over `Z_p`**, and `v_p` of both determinants is `0`.
  (ii) *Cyclotomic (ramification) contact.*  `K_p = [Z →p→ Z]` and
      `K_{p²} = [Z →p→ Z]`, since `Φ_p(1) = Φ_{p²}(1) = p`; both have
      `H⁰ = Z/p`, and `v_p` of both determinants is `1`.
  (iii) They differ, at `p` and at `p²`, already in the `p`-primary part:
      `0` versus `Z/p`.
  (iv) *The mechanism.*  The cyclotomic factor is the determinant of the
      **deck translation**, not of the correspondence: `Φ_n(1) =
      det(1 − T | V_n)`, where `T` is the canonical order-`n` automorphism of
      the orbit quotient `L_S/nL_S ≅ Z/n` given by translation by the class of
      `1 ∈ L_S` (Theorem 6.3(c)).  Geometrically, by Lemma 3.1, `T` generates
      `μ_n`, the deck group of the relative fibre of the correspondence, while
      the fixed contact is the determinant of `1 −` (the correspondence) on
      the ambient, governed by `μ_{n−1}`.  The two live on `V(n)` and
      `V(n−1)` respectively (Theorem 3.3), which are disjoint.

*Proof.*  (i) is P123.060 §2 evaluated at `n = p, p²`; `p−1` and `p²−1` are
prime to `p`, hence units in `Z_p`, so the differential is an isomorphism and
the complex is contractible.  (ii) is `Φ_p(x) = 1+x+…+x^{p−1}`, so
`Φ_p(1)=p`, and `Φ_{p²}(x) = Φ_p(x^p)`, so `Φ_{p²}(1)=p`; then (6.2).
(iii) compares (i) and (ii).  (iv) is Theorem 6.3(c) together with Lemma 3.1
and Theorem 3.3.  ∎  `PROVED`

So the test is passed in the only way it could be passed: the two contacts do
differ, the mechanism is located (deck group versus fixed group), and no
determinant has been substituted for another.  Clause B.7 is discharged, and
with it the stopping rule that had blocked row B.

**[REBUILT, phase 131.]**  Phase 128 attached to this line the note "it is
located on `G_m/Z`, not on the carrier", and that note was fair: Theorem 6.4
is a computation in `Z` and in `Z_p`, not in `X_S`.  Theorem 6.5 now locates
the same mechanism **on the carrier**.

**Theorem 6.5 (the mechanism on the carrier; clause B.7 on `X_S`).**
**[REBUILT, phase 131.]**  Let `p ∈ S_f` and `k ≥ 1`, `n = p^k`.  In the
declared category:

  (i) *the linear-dilation (fixed) factor contributes nothing at `p | n`.*
      The fixed-point weight `1/|1−x|_p` of Paper 43 Theorem 8A.9(a) is
      identically `1` on the valuation shell `p^kZ_p^×`, because
      `|1 − p^k u|_p = 1` for every `u ∈ Z_p^×` and `k ≥ 1`.  So the entire
      analytic weight of the shell is the half-density `p^{−k/2}`, and no
      `1−u^{−1}` data survive there.  Dually, the places where the fixed
      factor **is** nontrivial are the `q` with `v_q(1−σ_q) > 0`, and the
      norm class never visits them: by Proposition 3bis.2 it is on no finite
      slice, and by Theorem 3bis.7 its finite local terms come from shells
      only.
  (ii) *the cyclotomic factor is the Haar volume of the unit orbit of the
      ideal.*  The shell `p^kZ_p^×` is exactly the set of generators of the
      ideal `p^kZ_p`, i.e. the `Z_p^×`-orbit of `p^k`, and

        Λ(p^k) = \log p = vol_{d^*x}(p^kZ_p^×) = vol_{d^*x}(Z_p^×)

      (P123.042 §1), **independent of `k` by translation invariance of `d^*x`
      on `Q_p^×`** — that, and nothing more, is what is located on the carrier.
      The dependence on `k` sits entirely in the half-density `p^{−k/2}`.
      **[REBUILT, phase 131, round 2, finding `F5`: the round-1 text continued
      "this is the carrier-side statement **matching** `Φ_p(1) = Φ_{p²}(1) =
      p`".  That clause is removed from the theorem and demoted to
      Remark 6.5a′, because it asserts a correspondence for which no map is
      supplied.]**
  (iii) *the two labels, explicitly.*

        contact_{fin}(Γ_p^{rad})    = (\log p)\,p^{−1/2}   (shell k = 1),
        contact_{fin}(Γ_{p²}^{rad}) = (\log p)\,p^{−1}     (shell k = 2),

      both with primitive degree `Λ = \log p`, differing only by the
      half-density — whereas the **fixed** data of the same labels are
      `|1−p|_q^{−1}` at `q | p−1` and `|1−p²|_q^{−1}` at `q | p²−1`, numbers
      attached to the **lift** which the class does not see (Corollary
      3bis.3).

*Proof.*  (i) For `k ≥ 1`, `v_p(p^ku) = k > 0`, so `p^ku ∈ pZ_p` and
`1 − p^ku ∈ 1 + pZ_p ⊂ Z_p^×`, whence `|1−p^ku|_p = 1`; Paper 43 Lemma 8.2(i)
and Theorem 8A.9(a), (8A.24′) then give `rk^{Haar} = 1`, `w_p = τ_p =
p^{−k/2}`.  The dual clause is Proposition 3bis.2 and Theorem 3bis.7's proof,
where the unit packet is shown to vanish identically on radial sections.
(ii) `p^kZ_p^× = \{x : v_p(x) = k\}` is the coset `p^k·Z_p^×`, and `d^*x` is
translation-invariant with `vol(Z_p^×) = \log p` (P123.042 §1); the
generators of `p^kZ_p` are exactly the elements of valuation `k`.
The equality `Λ(p^k) = \log p` is Definition 1.3 and (3bis.8).
(iii) is Theorem 3bis.7 at `n = p` and `n = p²`, and Theorem 3.3(v) for the
lift data.  ∎  `PROVED`

**Remark 6.5a′ (a numerical coincidence, no map supplied).**  **[REBUILT,
phase 131, round 2, finding `F5`.]**  Both quantities are independent of `k`:
`vol_{d^*x}(p^kZ_p^×) = \log p` by translation invariance of multiplicative
Haar measure, and `Φ_{p^k}(1) = p` because `Φ_{p^k}(x) = Φ_p(x^{p^{k−1}})`.
These are two unrelated reasons.  **No map, functor or comparison between the
two objects is supplied by this paper**, and by P123.039 §5 ("a collection of
equal trace values is insufficient for those functorial claims") the
coincidence does not by itself locate a mechanism.  What is therefore proved
for clause B.7 is: *the test is passed* — the two contacts differ, decisively
at `p`, `p²` (Theorem 6.4) — and *the fixed-point weight is trivial on the
shell while the surviving weight is a Haar volume* (Theorem 6.5(i)–(ii)).  The
**mechanism** — a construction carrying one determinant to the other — is
`PARTIAL`: located on `G_m/Z` as the deck-versus-fixed group (Theorem 6.4(iv),
Lemma 3.1), and on the carrier only as the shell volume, with no arrow
between the two locations.  The §10 ledger says exactly this.

**Remark 6.5a (a dictionary, flagged as such).**  It is tempting to say that
`\log p = vol(p^kZ_p^×)` "is the deck group `μ_n` in measure form", since the
unit orbit of the ideal is the carrier-side avatar of the orbit lattice
`L_S/nL_S` on which `Φ_n(1) = \det(1−T|V_n)` is computed (Theorem 6.3(c)).
That sentence is a **dictionary entry, not a theorem**, and this paper does
not use it.  What is proved is the numerical coincidence of Theorem 6.5(ii)
and Theorem 3bis.10, and by P123.022 nothing stronger is available in a
`C`-linear category.

---

## 6bis. The integral shadow of the Frobenius, on objects

**[REBUILT, phase 131, round 3 — this subsection is new.  It addresses
reservation `R2` of `R131.005`: "`Z/Φ_n(1)` is not the value of anything on
the objects".]**

§6.2a records, and does not withdraw, the two negative facts: `LΔ^*Γ_n` is the
fixed complex, and **no additive `C`-linear functor** can carry an object of
the declared category to a complex with `Z/p` cohomology (P123.022 §2).  The
second is a proposition with a two-line proof: in a `C`-linear additive
category `p·id_X` is invertible, an additive functor preserves that, and
`p` acts bijectively on the cohomology of the image, while it acts as `0` on
`H^0[Z→p→Z] = Z/p`.  Nothing in this subsection contradicts it.  What
P123.022 §2 also says, verbatim, is its **Scope**:

> "The proposition does not forbid an integral or lattice category with a
> complex realization.  That realization may send a nonzero torsion object to
> zero while a metrized determinant retains an arithmetic degree.  It also
> does not prohibit a scalar regularized trace or a nonlinear construction
> using extra integral data.  **Such additional structure must be
> constructed, however; it is absent from the pure `C`-linear kernel
> category.**"

This subsection constructs that additional structure on the Frobenius family.
It is not a functor on the `C`-linear category and does not pretend to be: it
is defined on the **arithmetic monoid of Frobenius objects**, using the
integral lattice `L_S = ∏_{p∈S_f}Z_p ⊂ X_S`, which is part of the declared
coefficient geometry (P123.038 §2; the chart transitions already use
`1_{Z_p}`).

**Definition 6bis.1 (the integral shadow).**  For `n ≥ 1` with `P(n) ⊆ S_f`,
let `ι(n)_f = (p^{v_p(n)})_{p∈S_f} ∈ ∏_p Z_p∖\{0\}` act on `L_S` by
coordinatewise multiplication, and put

    Sh_Z(Frob_n) := Cone\big( L_S \xrightarrow{\;ι(n)_f\;} L_S \big)
                  = [\,L_S →^{n} L_S\,]  = Q_{S,n} ,                  (6bis.1)

in degrees `−1, 0`, the index complex of P123.038 §3 and of Theorem 6.1.

**Lemma 6bis.2 (well defined on the object).**  `Sh_Z(Frob_n)` depends only on
the measure `Frob_n`, not on the chosen idele representative:

  (i) `ι(n)_f L_S = nL_S`, so (6bis.1) is `[L_S →n→ L_S]`;
  (ii) *unit averaging acts trivially.*  For every `u ∈ K_{P(n)}` — i.e. every
       point of the coset over which (3ter.3) averages — the corresponding
       idele `ι(n)u` satisfies `(ι(n)u)_f L_S = nL_S`, because the entries of
       `u` are units of the respective `Z_p`;
  (iii) *gauge invariance.*  For `γ ∈ Γ_S`, the arithmetic anchor
       `b_S(a) := a_f/a_∞` of P123.038 §2 satisfies `b_S(γa) = b_S(a)`, and
       `b_S(ι(n)u) = n·(\text{unit})`, so `b_S(ι(n)u)L_S = nL_S`;
  (iv) *the object alone determines `n`* (Theorem 3ter.4(iv)), so (6bis.1) may
       equivalently be read as a definition in terms of `supp\,Frob_n` with no
       lift at all.

*Proof.*  (i) `∏_p p^{v_p(n)}Z_p = ∏_p nZ_p = nL_S`, since for `p ∈ S_f` we
have `nZ_p = p^{v_p(n)}Z_p` (the cofactor `n/p^{v_p(n)}` is a unit of `Z_p`).
(ii) Same computation with `u_p ∈ Z_p^×`.  (iii) `b_S(γa) = γa_f/(γa_∞) =
a_f/a_∞` is P123.038 §2, and `b_S(ι(n)u) = (p^{v_p(n)}u_p)_p/1`, which
generates `nL_S` by (i)–(ii).  (iv) is Theorem 3ter.4(iv).  ∎  `PROVED`

**Theorem 6bis.3 (structure of the integral shadow).**  For `m,n ≥ 1` with
`P(mn) ⊆ S_f`:

  (i) *cohomology.*  `H^{−1}Sh_Z(Frob_n) = 0` and
      `H^0Sh_Z(Frob_n) = L_S/nL_S ≅ Z/n`;
  (ii) *transitivity triangle.*  The chain map `(\,id,\ n\,) :
      Sh_Z(Frob_m) → Sh_Z(Frob_{mn})` is injective with cokernel
      quasi-isomorphic to `Sh_Z(Frob_n)`, giving an exact triangle

        Sh_Z(Frob_m) → Sh_Z(Frob_{mn}) → Sh_Z(Frob_n) \xrightarrow{+1} ;  (6bis.2)

  (iii) *additivity of the degree.*  `deg_det Sh_Z(Frob_{mn}) =
      deg_det Sh_Z(Frob_m) + deg_det Sh_Z(Frob_n)`, i.e. `\log mn =
      \log m + \log n`;
  (iv) *and `Sh_Z` is NOT monoidal on the nose.*  (6bis.2) is an exact
      triangle, not a splitting, and by Theorem 5.4 the associated primitive
      extraction is not monoidal for `⊗^L`; `Sh_Z(Frob_m)⊗^L Sh_Z(Frob_n)
      \not≅ Sh_Z(Frob_{mn})` in general (already for `m = n = 2`:
      `[Z→2→Z]⊗^L[Z→2→Z]` has `H^{−1} = Z/2 ≠ 0`);
  (v) *Möbius cofiber.*  The **Möbius total cofiber over the divisor poset**
      of `d ↦ Sh_Z(Frob_d)`, `d | n`, is `Prim_n ≅ [\,Z →^{Φ_n(1)} Z\,]`, with
      `H^0 = Z/Φ_n(1)`.  **[phase 133, PANEL_1 finding B3: this said "the
      divisor **cube**".  For non-squarefree `n` the divisor poset is not a
      cube — for `n = p^k` it is a chain of length `k` — and the cube is the
      one indexed by the **radical** divisors, of which this is the top layer.
      The identity `Σ_{d|n}μ(n/d)\log d = Λ(n)` is unaffected.]**

*Proof.*  (i)  `n ≠ 0` and `L_S` is torsion-free, so multiplication by `n` is
injective, whence `H^{−1} = 0`; and `L_S/nL_S = ∏_{p∈S_f}Z_p/nZ_p ≅
∏_{p|n}Z/p^{v_p(n)} ≅ Z/n` by primary decomposition, the factors at `p ∤ n`
being `0` (P123.038 §3; Theorem 6.1(ii)).

(ii)  The square
`L_S \xrightarrow{m} L_S`, `L_S \xrightarrow{mn} L_S` with left vertical `id`
and right vertical `n` commutes: `n∘m = mn∘id`.  Both verticals are injective
(`L_S` torsion-free).  The cokernel complex is `[\,0 → L_S/nL_S\,]`,
concentrated in degree `0`, which is quasi-isomorphic to `Sh_Z(Frob_n)` by (i)
(the latter is a free resolution of `L_S/nL_S`).  A short exact sequence of
complexes gives the exact triangle (6bis.2).

(iii)  By Definition 5.2, `deg_det[L_S→n→L_S] = \log\#H^0 = \log n` by (i);
alternatively apply the cone law of Definition 5.2 to (6bis.2).

(iv)  The triangle (6bis.2) is the object-level form of P123.037 §5's open
item ("transitivity (1.2) is an exact triangle, not such an isomorphism"), and
the displayed counterexample is Theorem 5.4's computation: resolving `Z/2` by
`[Z→2→Z]` and tensoring gives `H_1 = Tor_1^Z(Z/2,Z/2) = Z/2 ≠ 0`, whereas
`Sh_Z(Frob_4)` has `H^{−1} = 0` by (i).

(v)  By Theorem 6.1(i) the diagonal `Z → L_S` induces a quasi-isomorphism
`C_{ram}(d) → Q_{S,d}` **naturally on the whole divisor cube**, so the two
cubes have isomorphic total cofibers; and the total cofiber of the
`C_{ram}`-cube is `Prim_n ≅ [Z→Φ_n(1)→Z]` by Theorem 6.3(a) (P123.037 §3–§4)
and Theorem 5.3.  ∎  `PROVED` (with the object-level components
`PROVED-IN-REPOSITORY`: P123.037 §3–§4, P123.038 §3–§4).

**Theorem 6bis.4 (the amended clause B.4, now on objects).**  Let `n ≥ 2`,
`P(n) ⊆ S_f`.  Then:

    contact_{fin}(Frob_n) = n^{−1/2}·deg_det\,Prim\big(Sh_Z\big)_n ,   (6bis.3)
    deg_det\,Sh_Z(Frob_n) = \log n = Σ_{d|n} d^{1/2}·contact_{fin}(Frob_d) . (6bis.4)

Both sides of each identity are attached to the **objects** `Frob_d` of the
arithmetic monoid — the left by Corollary 3ter.11 (an invariant of the
measure), the right by Definition 6bis.1 and Lemma 6bis.2 (an invariant of the
same measure through its action on `L_S`).  The identification is of
**degrees**; an identification at the level of objects, in the `C`-linear
declared category, is impossible (P123.022 §2, and Paper 43 Theorem 7.1(c):
the shadow of an external class at `p | n` is the rank-one class `C[0]`).

*Proof.*  (6bis.3): the right-hand side is `n^{−1/2}\log\#(Z/Φ_n(1)) =
n^{−1/2}\log|Φ_n(1)| = n^{−1/2}Λ(n)` by Theorem 6bis.3(v), Definition 5.2 and
Theorem 5.3; the left-hand side is `Λ(n)n^{−1/2}` by Corollary 3ter.11.
(6bis.4): the first equality is Theorem 6bis.3(iii)/(i); the second is
`\log n = Σ_{d|n}Λ(d)` (Möbius inversion of `Λ = μ∗\log`, `CLASSICAL`,
Corollary 5.3a) together with `d^{1/2}contact_{fin}(Frob_d) = Λ(d)` for
`d ≥ 2` and `Λ(1) = 0` (the label `1` is `Frob_1 = Δ`, treated as
identity/excess by the term `c·F(1)` of Paper 43 (8.4) with `c := 0`, and not
by the degree formula — Theorem 5.3).  ∎  `PROVED`

**Lemma 6bis.3a (`Sh_Z` is a functor on the divisor poset, and a function on
the monoid).**  **[REBUILT, phase 131, round 4, finding `F8`.]**  For `d | e`
let `i_{d,e} := (\,id,\ e/d\,) : Sh_Z(Frob_d) → Sh_Z(Frob_e)` be the chain map
of Theorem 6bis.3(ii).  Then

    i_{e,f} ∘ i_{d,e} = i_{d,f}   for all d | e | f ,   i_{d,d} = id ,  (6bis.3)

**literally** (not up to homotopy), so `d ↦ Sh_Z(Frob_d)` is a strict functor
from the divisor poset `(N_{≥1}, \mid)` to `Ch(Z)`.  On the **monoid**
`(N_{≥1},×)` — a one-object category — `Sh_Z` is a **function**, not a
functor, and it is **not monoidal** (Theorem 6bis.3(iv)).

*Proof.*  Degreewise: in degree `−1` the composite is `id∘id = id`; in degree
`0` it is `(f/e)·(e/d) = f/d`.  Both are the components of `i_{d,f}`.
Identity: `i_{d,d} = (id, 1) = id`.  This is P123.037 §1's observation
("`i_{b,n}i_{d,b} = i_{d,n}` **literally**") transported to `Q_{S,·}` by
Theorem 6.1(i).  ∎  `PROVED`

### 6bis.1 The additive extension, and the P123.038 §5 arrow

**[REBUILT, phase 131, round 4 — instruction `L2` of `R131.009`.]**

**Definition 6bis.3b (Dirichlet-polynomial correspondences).**  Let
`Z[𝔉^+]` be the free abelian group on the Frobenius monoid `\{Frob_n\}_{n≥1}`,
whose elements `Σ_{n∈A}c_nFrob_n` (`c_n ∈ Z`, `A` finite) we call **integral
Dirichlet-polynomial correspondences**.  Extend `Sh_Z` additively,

    Sh_Z\Big(Σ_{n∈A}c_nFrob_n\Big) := ⊕_{n∈A} Sh_Z(Frob_n)^{⊕c_n}
      = ⊕_{n∈A}\,[\,L_S →^{n} L_S\,]^{⊕c_n} ,                       (6bis.4)

with `c_n < 0` read as a shift `[1]` (Definition 5.2's sign reversal), and
extend `contact_{fin}` linearly by `contact_{fin}(Σc_nFrob_n) :=
Σ c_n\,contact_{fin}(Frob_n)`.

**Theorem 6bis.3c (the P123.038 §5 arrow, in the only form that can exist).**
**[REBUILT, phase 131, round 4.]**

  (i) *Well defined and additive.*  (6bis.4) is well defined on `Z[𝔉^+]`, and
      `deg_det` is additive on it by the cone law of Definition 5.2:
      `deg_det Sh_Z(Σc_nFrob_n) = Σ_n c_n\log n`.
  (ii) *Cyclic, trivially.*  `Z[𝔉^+]` is a commutative ring under the
      convolution product induced by `Frob_m⋆Frob_n = Frob_{mn}`
      (Theorem 3ter.4(i)); cyclic invariance of any trace on a **commutative**
      algebra is automatic, so the "cyclic extension to mixed
      correspondences" of P123.038 §5 is satisfied here for the trivial
      reason, and this is said rather than hidden.
  (iii) *Comparison with the analytic trace, linearly.*  For every
      `Σc_nFrob_n ∈ Z[𝔉^+]` with all `n ≥ 2`,

        Σ_n c_n\,n^{1/2}\,contact_{fin}(Frob_n)
          = Σ_n c_n\,deg_det\,Prim(Sh_Z)_n ,                        (6bis.5)

      both sides being linear functionals on `Z[𝔉^+]`, the left computed from
      Paper 43's declared trace on the smeared Frobenii (which lie in `D_A`,
      hence in `Corr_A^{tr}`, where Paper 43's nuclear trace is defined) and
      the right from the lattice `L_S`.
  (iv) *What is refuted, not open.*  An **object-level** functor from the
      declared `C`-linear category `G` producing these complexes is
      **`REFUTED`** (P123.022 §2), not `OPEN`: in a `C`-linear additive
      category `p·id` is invertible, an additive functor preserves that, and
      `Z/p` cannot occur.  The complex realization of `Sh_Z` is acyclic
      (Remark 6bis.5).

*Proof.*  (i) Additivity of `deg_det` on `⊕` and the shift rule are
Definition 5.2; Theorem 6bis.3(iii) gives the value on generators.  (ii)
`Z[𝔉^+]` is the monoid ring of the commutative monoid `(N_{≥1},×)`, hence
commutative; a trace on a commutative algebra satisfies `T(ab) = T(ba)`
trivially.  (iii) Both sides are additive in the generator by construction,
and on a generator the identity is Theorem 6bis.4 (6bis.3) multiplied by
`n^{1/2}`.  (iv) is P123.022 §2's Proposition, quoted at the head of §6bis.
∎  `PROVED`

**Remark 6bis.3d (how much of P123.038 §5 this is, exactly).**  The note asks
for the lattice-index operation "realized as the admissible diagonal shadow,
**extended cyclically to mixed correspondences** and compared with the
analytic **nuclear** trace", adding that "an invariant of the arithmetic
family does not itself provide that trace functor"; P123.039 §5 adds that
"a collection of equal trace values is insufficient for those functorial
claims".  Measured against that:

  * *(b) cyclic extension to mixed correspondences* — **supplied**, for
    finite `Z`-combinations of Frobenii, trivially because the algebra is
    commutative (Theorem 6bis.3c(ii));
  * *(c) comparison with the analytic trace* — **supplied as an identity of
    degrees**, linearly on `Z[𝔉^+]` (Theorem 6bis.3c(iii)), where the analytic
    side is Paper 43's trace on genuine elements of `D_A` (the smeared
    Frobenii), not on labels;
  * *(a) the realization as a shadow functor on the `C`-linear `G`* —
    **`REFUTED`**, not open (Theorem 6bis.3c(iv), P123.022 §2).

That is the whole of the arrow as far as it can exist on a `C`-linear carrier,
and §10's ledger row is graded accordingly.  What is **not** claimed: that
`Sh_Z` is a shadow in Paper 43's sense (Thm. 7.1(c)), that it is defined on all
of `Corr_A^{tr}`, or that the comparison is anything other than one of degrees.

**Remark 6bis.5 (what has and has not changed since round 2).**  Round 2's
Theorem 6.3a proved the same numerical identity with the left-hand side read
as an atom of a representing measure attached to a **label**; reservation `R2`
of `R131.005` objected that `Z/Φ_n(1)` was "not the value of anything on the
objects".  Theorem 6bis.4 answers that objection: `Sh_Z` is a construction on
the objects `Frob_n` (Lemma 6bis.2), functorial for the divisor arrows through
the triangle (6bis.2), and `Prim(Sh_Z)_n = [Z→Φ_n(1)→Z]` is its Möbius
cofiber.  What has **not** changed, and is not claimed:

  * `Sh_Z` is **not** a functor on the declared `C`-linear category `G`, and
    it is not a shadow in Paper 43's sense (Thm. 7.1(c)).  It is the "integral
    or lattice structure with a complex realization" that P123.022 §2 says
    must be constructed, and it is constructed here on the arithmetic monoid
    only;
  * the complex realization of `Sh_Z(Frob_n)` — base change to `C` — is
    **acyclic**, exactly as P123.022 §2 predicts ("that realization may send a
    nonzero torsion object to zero while a metrized determinant retains an
    arithmetic degree"): `[C→n→C]` is contractible for `n ≠ 0`.  So the
    integral object cannot be recovered from `G`, and this paper does not
    recover it;
  * the identification (6bis.3)–(6bis.4) is therefore of **degrees only**, and
    the functorial demand of P123.038 §5 and P123.039 §5 — cyclic extension to
    mixed correspondences, comparison with the analytic **nuclear** trace as a
    trace functor — is **untouched and remains `OPEN`** (Remark 3bis.10b,
    where both notes are quoted in full).


---

## 7. Adversarial verification (clause B.8)

The closure plan requires `p, p², p³, pq, p²q, pqr`, with the index by places
preserved.  Every entry below is forced by Theorems 3.3, 5.3, 6.3; the table
is a check, not a source.

| `n` | `P(n)` | `deg_det C_ram = log n` | `Prim_n` | `Φ_n(1)` | `Λ(n)` | `H⁰(C_fix) = Z/(n−1)` | `V(n)` | `V(n−1)` | `w_ram` (lift) | `w_unit` (lift) |
|---|---|---|---|---|---|---|---|---|---|---|
| `2`  (`p`)     | `{2}`     | `log 2`  | `Z/2` | `2` | `log 2` | `0`     | `{2}`     | `∅`         | `2^{−1/2}`  | `1`  |
| `4`  (`p²`)    | `{2}`     | `log 4`  | `Z/2` | `2` | `log 2` | `Z/3`   | `{2}`     | `{3}`       | `4^{−1/2}`  | `3`  |
| `8`  (`p³`)    | `{2}`     | `log 8`  | `Z/2` | `2` | `log 2` | `Z/7`   | `{2}`     | `{7}`       | `8^{−1/2}`  | `7`  |
| `6`  (`pq`)    | `{2,3}`   | `log 6`  | `0`   | `1` | `0`     | `Z/5`   | `{2,3}`   | `{5}`       | `6^{−1/2}`  | `5`  |
| `12` (`p²q`)   | `{2,3}`   | `log 12` | `0`   | `1` | `0`     | `Z/11`  | `{2,3}`   | `{11}`      | `12^{−1/2}` | `11` |
| `30` (`pqr`)   | `{2,3,5}` | `log 30` | `0`   | `1` | `0`     | `Z/29`  | `{2,3,5}` | `{29}`      | `30^{−1/2}` | `29` |
| `9`  (`p²`)    | `{3}`     | `log 9`  | `Z/3` | `3` | `log 3` | `Z/8`   | `{3}`     | `{2}`       | `9^{−1/2}`  | `8`  |
| `10` (`pq`)    | `{2,5}`   | `log 10` | `0`   | `1` | `0`     | `Z/9`   | `{2,5}`   | `{3}`       | `10^{−1/2}` | `9`  |
| `16` (`p⁴`)    | `{2}`     | `log 16` | `Z/2` | `2` | `log 2` | `Z/15`  | `{2}`     | `{3,5}`     | `16^{−1/2}` | `15` |

**[CORRECTED, phase 128 B9.]**  The last three rows were added because in the
first six `n−1` is prime in every row, so `V(n−1)` was a singleton throughout
and the multi-place structure of `w_unit` was never exercised.  Row `16` has
`V(15) = {3,5}`; row `9` has `v_2(8) = 3`; row `10` has `v_3(9) = 2`.
Verified: `Φ_9(1) = 3`, `Φ_{10}(1) = 1`, `Φ_{16}(1) = 2`.

**[REBUILT, phase 131 — the two `w` columns are relabelled, and the columns
that matter are added.]**  The columns `w_ram` and `w_unit` above are
properties of the **lift** `a_S(n)`: `w_unit` in particular is the product of
the local factors of the idele at the places `q ∤ n`, and is **not a contact**
of the class (Corollary 3bis.3).  They are kept because Theorem 3.3 is about
the lift and the table is a check on Theorem 3.3.  The following table is the
continuation of the same nine rows with the quantities of §3bis — the ones
clause B.4 (amended), B.5 and B.7 are actually about.

| `n` | finite contact (atom of `ω_{fin}`) `Λ(n)n^{−1/2}` | numerically | archimedean **density** `ω_∞(\log n) = n^{3/2}/(n²−1) = K(\log n)` | numerically | bidegree `M(Γ_n^{rad}) = (λ_−,λ_+)` | `Σ_{d|n}Λ(d) = \log n` |
|---|---|---|---|---|---|---|
| `2`  | `2^{−1/2}\log 2` | `0.490129072` | `2^{3/2}/3`      | `0.942809042` | `(2^{1/2}, 2^{−1/2})`   | `0.693147181` |
| `4`  | `\tfrac12\log 2` | `0.346573590` | `8/15`           | `0.533333333` | `(2, \tfrac12)`         | `1.386294361` |
| `8`  | `8^{−1/2}\log 2` | `0.245064536` | `8^{3/2}/63`     | `0.359165349` | `(8^{1/2}, 8^{−1/2})`   | `2.079441542` |
| `6`  | `0`               | `0.000000000` | `6^{3/2}/35`     | `0.419912527` | `(6^{1/2}, 6^{−1/2})`   | `1.791759469` |
| `12` | `0`               | `0.000000000` | `12^{3/2}/143`   | `0.290693842` | `(12^{1/2},12^{−1/2})`  | `2.484906650` |
| `30` | `0`               | `0.000000000` | `30^{3/2}/899`   | `0.182777272` | `(30^{1/2},30^{−1/2})`  | `3.401197382` |
| `9`  | `\tfrac13\log 3` | `0.366204096` | `27/80`          | `0.337500000` | `(3, \tfrac13)`         | `2.197224577` |
| `10` | `0`               | `0.000000000` | `10^{3/2}/99`    | `0.319421986` | `(10^{1/2},10^{−1/2})`  | `2.302585093` |
| `16` | `\tfrac14\log 2` | `0.173286795` | `64/255`         | `0.250980392` | `(4, \tfrac14)`         | `2.772588722` |

Three structural facts are exercised by these rows and are proved in general,
not read off:

  * the finite contact **vanishes at every composite `n`** (`6,12,30,10`),
    because no single place has a shell of modulus `1/n` (Theorem 3bis.7);
  * `Λ(p^k) = \log p` is **independent of `k`** (`2,4,8,16` all give
    `\log 2`), because the unit orbit of an ideal has the same Haar volume
    whatever the exponent (Theorem 6.5(ii)); the `k`-dependence is entirely in
    the half-density;
  * the archimedean column is **positive for every `n`**, composite or not,
    and is a **density**, not an atom, and not a contact of any object
    (Remark 3bis.8a); it is not part of `Λ`.  **[REBUILT, phase 131, round 2,
    finding `F6`.]**  It is defined for every real label `t` and is displayed
    here only because the rows are indexed by `n`.

These nine rows, together with `Σ_{d|n}Λ(d) = \log n`, `K(\log n) =
n^{3/2}/(n^2−1) = n^{−1/2}Σ_{j≥0}n^{−2j}`, `\log|Φ_n(1)| = Λ(n)` and
`∏_{d|n}d^{μ(n/d)} = Φ_n(1)`, are verified numerically by
`03-research/phase-131-row-b-closure/scripts/verify_131_contacts.py`
(all checks pass).  **The numerics verify; they prove nothing.**  Every entry
is forced by Theorems 3bis.7, 3bis.8, 3bis.10, 5.3 and 6.5.

Checks performed on the table:

1. **Cube = Möbius = `Λ`.**  The alternating sum `Σ_{J⊆P(n)}(−1)^{|J|}
   log(n/∏_J p)` equals `Σ_{d|n}μ(d)log(n/d)` equals `Λ(n)` in every row; e.g.
   for `n=12`, `log12 − log6 − log4 + log2 = log(24/24) = 0`; for `n=30`,
   `log30 − log15 − log10 − log6 + log5 + log3 + log2 = log(900/900) = 0`;
   for `n=8`, `log8 − log4 = log2`.  This is Lemma 5.1 and Theorem 5.3; the
   rows are instances, and the general statement is proved, not extrapolated.
2. **`Φ_n(1)`.**  `Φ_4(x)=x²+1`, `Φ_8(x)=x⁴+1`, `Φ_6(x)=x²−x+1`,
   `Φ_{12}(x)=x⁴−x²+1`, `Φ_{30}(x)=x⁸+x⁷−x⁵−x⁴−x³+x+1`, giving
   `2,2,1,1,1` at `x=1`.  Matches column `Λ` through `log|Φ_n(1)|`.
3. **Disjointness.**  `V(n) ∩ V(n−1) = ∅` in every row, visibly.
4. **Prime-power degeneracy is real.**  `Prim_4 ≅ Prim_8 ≅ Z/2`: the primitive
   contact of `p^k` does not grow with `k`.  This is required: `Λ(p^k)=log p`
   for every `k`.  The dependence on `k` sits entirely in the analytic weight
   `w_ram = p^{−k/2}`, which is where the explicit formula puts it.
5. **Index by places.**  **[CORRECTED, phase 128 B1.]**  The first version
   claimed "no function of `w(Γ_4)` and `w(Γ_8)` recovers `Λ`".  That is false,
   and contradicts Remark 6.2 of this paper: `w_ram(Γ_n) = n^{−1/2}` is
   injective in `n`, hence determines `(v_p(n))_p`, hence determines `Λ(n)`.
   What is true and harmless is that `n ↦ Λ(n)` is **not monotone** in
   `|a_S(n)|_S`.  The place-indexed bookkeeping is still how the split (3.3) is
   *defined*, but it is not forced by an information-theoretic obstruction.
   **[REBUILT, phase 131, round 2, finding `F4`:]**  This check is correct and
   the proof of Theorem 8.1(iii) has now been brought into line with it — the
   round-1 proof asserted the opposite in the same paper.  The positive form
   of the statement is Theorem 3bis.7′(iii): `Λ` **is** a function of the
   modulus, namely `Λ(e^t) = e^{t/2}ω_{fin}(\{t\})`, and its support is the
   contact locus.

**Proposition 7.1 (B.6: the family is proved by structure).**  Theorems 3.3,
5.3, 6.1 and 6.3 are stated and proved for all `n ≥ 2` with no case analysis
beyond "one prime divisor or several", which is itself proved (P123.037 §3)
by a primary-decomposition argument valid for all `n`.  No statement in this
paper is obtained by extrapolating from the labels `2,3,4,6` or from the table
above.  ∎  `PROVED`

---

## 8. Compatibility with row A, and independence (clauses B.6, B.9)

**[REBUILT, phase 131 — `𝓝 = 0` and `N_A = D_A` are now theorems.]**  Phase
128 recorded `N_A` as resting on an invariant `T` that was then `CANDIDATE`.
That is no longer the state of Paper 43: since phase 129–130 its `T` is
**declared** by Definition 8.6 from the proved local terms (8.5) and (8.5∞),
its constant is **declared** `c := 0` (Def. 8A.7d), and Theorem 9.8 proves
`𝓝 = \{0\}`, hence

    N_A = D_A = C_c^∞(C_S) ,                                          (8.0)

with `I_A(F,G) = T(F⋆G^†)` nondegenerate on all of it, and with the completion
`N_A^{dist} = \overline{J(N_A)} ⊆ D_A' ⊕ B_T` of Theorem 9.14 splitting
canonically as `N_A^{dist,prim} ⊕ σ(B_T)` (Theorem 9.14b).  Paper 43 now
carries the label `WEIL-STRENGTH-COMPLETE` on its declared carrier (Paper 43
§14.0a–b), with its qualifications: A.6 under the  amendment, A.8
with target `Pic_b(B_T)`, no sign, `𝓝_∞^W = 0` not claimed, and the auditor's
dissent on A.8 recorded there.  Row B cites it in that form and no stronger.

**Theorem 8.1 (the classes enter row A's numerical object).**  Let `N_A =
Corr_A^{tr}/𝓝 = D_A` be the numerical object of Paper 43 §9 (Theorem 9.8).
Then:

  (i) `Γ_n ∈ G` for every `n ≥ 1`, with `Γ_1 = Δ` (Theorem 4.3); so the
      arithmetic family is a subfamily of row A's category, not an extension
      of it;
  (ii) the pairing of Paper 43 Def. 9.2 restricts to the family as
      `⟨Γ_m, Γ_n⟩ = T(E_{a_S(m)a_S(n)^{−1}})`, which is defined in `G`
      because `G` contains all external twists, not only those with integral
      entries;
  (iii) **[CORRECTED, phase 128 B1.]**  The first version argued that the
      primitive components are *invisible* to the ruling plane.  That argument
      was backwards — `n ↦ log n` is injective, so anything that is a function
      of `n` **is** determined by `log n`, and `Λ(4)=Λ(8)` with `log4≠log8` is
      perfectly consistent with `Λ` being a function of `log n`.  The truth is
      the **opposite**: the ruling pairings depend on `|a_S(n)|_S = 1/n`, which
      determines `n`, which determines `Λ(n)`.  So the arithmetic family **is**
      separated by the ruling plane, and the appeal to Paper 43's mixed sector
      (which concerns *unit* twists `|u|=1`, and `Γ_n` is not one) is withdrawn.
      The correct statement is that the family's unit-sector content sits at the
      places `q | n−1` — an entirely different assertion;
  (iv) **[phase 133, PANEL_2 MAJOR-1: this read "Paper 43 Remark 9.5 states
      exactly this family and leaves open 'what these equal in terms of
      `Λ(n)`'".  **Paper 43 has no Remark 9.5**, and no statement of Paper 43
      poses that question: Theorem 9.5 separates two unit-sector sections of
      equal modulus, Remark 9.6 comments on what that does and does not
      establish, and Remark 9.7a says only that `Λ` appears in `T̂` as a
      derived shell volume.  The question is **row B's own**, raised here;
      the attribution is withdrawn.]**  The question "what does the arithmetic
      family's finite contact equal in terms of `Λ(n)`?" is row B's, and is
      prompted by Paper 43 Remark 9.7a, where `Λ(p^k) = \log p` arises as the
      shell volume inside `T̂`.  **[REBUILT, phase 131.]**  The answer
      is Theorem 3bis.7, not Theorem 3.3: for the **norm** classes the
      finite-place value is `Λ(n)n^{−1/2}`, an exact value of `T` with no
      regularization; the `q | p^k−1` factors belong to the lift and are not
      values of `T` (Corollary 3bis.3).  The phase-128 reading — "`w_ram` and
      `w_unit` answer Remark 9.5" — is withdrawn (§9bis W3), both for its
      answer and for its attribution.

*Proof.*  **[REBUILT, phase 131, round 2, finding `F4` of `R131.002` = `F1` of
`R131.003`: the round-1 proofs of (iii) and (iv) contradicted their own
corrected statements and §7 check 5.  Both are replaced.]**

(i) is Theorem 4.3.  (ii) is Def. 9.2 with (4.3).

(iii)  The ruling data of a class is its image under `M = (λ_−,λ_+)`.  By
Theorem 3bis.5(iii), `M(Γ_n^{rad}) = (n^{1/2}, n^{−1/2})`, and `n ↦ n^{1/2}`
is injective on `N_{≥1}`; so the ruling data **determine `n`**, hence determine
`Λ(n)` and every other function of the label.  That is the whole of (iii), and
nothing further is to be proved.

*The clause deleted here, and why.*  The round-1 proof continued: "if `Λ(n)`
were a function of the ruling data it would be a function of `n`, hence
determined by `\log n`, but `Λ(4)=Λ(8)` with `\log 4 ≠ \log 8` shows the
level sets differ, so `Λ` is not pulled back from the ruling plane".  That
inference is **invalid** — it is exactly the fallacy `D128.002` finding `B1`
accepted as an error — and its conclusion is **false**: `Λ(n) = f(\log n)`
with `f(t) := \log p` if `e^t = p^k` and `0` otherwise, so `Λ` **is** pulled
back from the ruling plane.  (`Λ(4) = Λ(8)` with `\log 4 ≠ \log 8` says only
that `f` is non-injective, which no one disputed.)  The deleted clause also
contradicted §7 check 5 of this same paper.  Theorem 3bis.7′(iii) is the
correct positive statement of the same phenomenon: `f(t) ≠ 0` exactly on the
contact locus.

(iv)  By Theorem 3bis.7 and (3bis.10), the finite-place data of the label `n`
in row A's declared trace is the atom `ω_{fin}(\{\log n\}) = Λ(n)n^{−1/2}`,
an exact value obtained with no regularization.  That is the answer to row
B's own question "what does the family's finite contact equal in terms of
`Λ(n)`?"  **[phase 133, PANEL_2 MAJOR-1: previously attributed to "Remark
9.5's question"; Paper 43 has no Remark 9.5 and poses no such question.]**  The round-1
proof instead cited Theorem 3.3(iii) and the places `q | p^k−1`; that is
withdrawn (§9bis W3), because those are local factors of the **lift** and the
class is on no finite slice (Corollary 3bis.3, for `|S_f| ≥ 2`; Remark 3bis.2a
for `|S_f| = 1`).  ∎  `PROVED`

**Theorem 8.3 (B.6, second half: the norm classes are elements of
`N_A^{dist}`, with their primitive components and their moments).**
**[REBUILT, phase 131.]**  Let `n ≥ 2`.  Choose `h_ε ∈ C_c^∞(R)`, `h_ε ≥ 0`,
`∫h_ε = 1`, `supp h_ε ⊆ [\log n − ε, \log n + ε]` with `ε < \tfrac12\log 2`,
and put `F_ε := Γ_{h_ε} ∈ D_A = N_A` (Lemma 3bis.6a).  Then:

  (i) *the pairing extends.*  `Γ_n^{rad} ⋆ G^† ∈ D_A` for every `G ∈ D_A`, so

        ℓ_n(G) := T(Γ_n^{rad} ⋆ G^†) = I_A(Γ_n^{rad}, G)

      is defined; `\widehat{Γ_n^{rad}}` is supported on the principal
      component `𝔠_0 ⊂ Ĉ_S` and equals `n^{iτ}` there, of modulus `1`, whence
      `|ℓ_n(G)| ≤ N(G)` with `N` the seminorm (9.20a) of Paper 43 Lemma
      9.14a0.  In particular `ℓ_n ∈ D_A'` and `ℓ_n` is bounded on bounded
      sets;
  (ii) *convergence in the strong dual.*  `I_A(F_ε,·) → ℓ_n` in `D_A'`, i.e.
      **uniformly on every bounded subset of `D_A`**;
  (iii) *convergence of the moments.*  `M(F_ε) → (n^{1/2}, n^{−1/2}) =
      M(Γ_n^{rad})`, the bidegree of Theorem 3bis.5(iii);
  (iv) *membership.*  Consequently

        J(F_ε) → \big(\,ℓ_n,\;(n^{1/2},n^{−1/2})\,\big) =: J(Γ_n^{rad})
        \quad\text{in } D_A'⊕B_T ,

      and `J(Γ_n^{rad}) ∈ N_A^{dist} = \overline{J(N_A)}`;
  (v) *canonical components.*  In the canonical splitting (9.23) of Paper 43
      Theorem 9.14b,

        J(Γ_n^{rad}) = \underbrace{(ℓ_n, 0)}_{∈\,N_A^{dist,prim}}
                     + \underbrace{σ(n^{1/2},n^{−1/2})}_{∈\,σ(B_T)} ,

      so the **primitive component** of the norm class is `(I_A(Γ_n^{rad},·),
      0)` and its **ruling component** is `σ(M(Γ_n^{rad}))`.  The ruling
      component is **nonzero for every `n`**; `Γ_n^{rad}` is therefore *not*
      a primitive class, and no positivity or primitivity is claimed for it
      anywhere in this paper.

*Proof.*  (i) `Γ_n^{rad}` is a multiplier of `D_A` (Remark 3bis.4b(ii)), so
`Γ_n^{rad}⋆G^† ∈ D_A^{rad} ⊂ D_A` and `T` of it is defined.  For the Fourier
transform: `Γ_n^{rad}` is the Haar measure of the coset `δ_S(1/n)K^♮`, so for
a character `χ` of `C_S`,
`\widehat{Γ_n^{rad}}(χ) = ∫\overline{χ}\,dΓ_n^{rad}
= \overline{χ(δ_S(1/n))}∫_{K^♮}\overline{χ(u)}du`, which vanishes unless
`χ|_{K^♮} = 1` — that is, unless `χ` lies on the principal component `𝔠_0`,
where `χ(w) = |w|_S^{iτ}` — and then equals `\overline{(1/n)^{iτ}} = n^{iτ}`.
The bound is Paper 43 (9.16)/Lemma 9.14a0 with `\sup_χ|\hat F| = 1`, and
`I_A(Γ_n^{rad},G) = ∫\widehat{Γ_n^{rad}}\overline{\hat G}(\hat T + c)dχ` is
(9.13) applied to `Γ_n^{rad}⋆G^†`, legitimate because that element lies in
`D_A`.

(ii) `F_ε` is `K^♮`-invariant, so `\hat F_ε` is also supported on `𝔠_0`, where
`\hat F_ε(τ) = ∫Γ_{h_ε}(w)\overline{χ(w)}d^*w = ∫_R h_ε(−t)e^{−iτt}dt
= ∫_R h_ε(s)e^{iτs}ds`.  Write `Δ_ε(τ) := \hat F_ε(τ) − n^{iτ}
= ∫h_ε(s)(e^{iτ s} − e^{iτ\log n})ds`.  Then `|Δ_ε(τ)| ≤ 2` always, and
`|Δ_ε(τ)| ≤ |τ|\,ε` since `|e^{iθ}−e^{iθ'}| ≤ |θ−θ'|` and
`|s − \log n| ≤ ε` on `supp h_ε`.  Let `B ⊆ D_A` be bounded.  By the proof of
Paper 43 Lemma 9.14a0 there are `d_N`, `C''_B` with `\hat G` supported on
`d_N` components and `|\hat G(𝔠,τ)| ≤ C''_B\min(1,τ^{−2})` for all `G ∈ B`,
and `|\hat T(𝔠,τ)| ≤ A_S + B_S\log(2+|τ|)`.  Hence for `R > 0`

    \sup_{G∈B}|I_A(F_ε,G) − ℓ_n(G)|
      ≤ \sup_{G∈B}∫_{𝔠_0}|Δ_ε||\hat G|(|\hat T|+|c|)\,dτ
      ≤ Rε·N_B + 2·\sup_{G∈B}∫_{|τ|>R}|\hat G|(|\hat T|+|c|)\,dτ ,

where `N_B := \sup_{G∈B}N(G) < ∞` (Lemma 9.14a0).  The second term is
`≤ 2C''_B∫_{|τ|>R}τ^{−2}(A_S+B_S\log(2+|τ|))\,dτ/2π =: η(R)`, which is
finite and `→ 0` as `R → ∞`, uniformly on `B`.  Given `δ > 0` pick `R` with
`η(R) < δ/2` and then `ε < δ/(2RN_B)`.  This is uniform convergence on `B`,
i.e. convergence in the strong dual.

(iii) By Lemma 3bis.6a, `λ_∓(F_ε) = ∫h_ε(s)e^{±s/2}ds → e^{±\log n/2}`, i.e.
`λ_−(F_ε) → n^{1/2}` and `λ_+(F_ε) → n^{−1/2}`, which is `M(Γ_n^{rad})` by
Theorem 3bis.5(iii).

(iv) `J(F) = (I_A(F,·), M(F))` by (9.18); combine (ii) and (iii).  Each
`J(F_ε)` lies in `J(N_A)`, so the limit lies in its closure `N_A^{dist}`.

(v) is Theorem 9.14b of Paper 43 applied to `x = (ℓ_n, M(Γ_n^{rad}))`: the
splitting sends `x` to `(ℓ_n,0) + σ(\bar M x)`.  Nonvanishing of the ruling
component: `M(Γ_n^{rad}) = (n^{1/2},n^{−1/2}) ≠ (0,0)`.  ∎  `PROVED`

**Remark 8.3a (what Theorem 8.3 closes, and what it does not).**  It closes
the second half of clause B.6 — "its classes and primitive components entering
row A's numerical object" — in the precise sense available: the classes are
elements of the canonical completion `N_A^{dist}`, their primitive and ruling
components are canonically defined, and their moments are `λ_± = n^{∓1/2}`.
It does **not** claim that `Γ_n^{rad} ∈ D_A` (it is not, Remark 3bis.4b), that
`I_A` extends to `N_A^{dist} × N_A^{dist}` (Paper 43 does not claim this
either), or that the classes are primitive (they are not, (v)).

**Theorem 8.2 (B.9: independence).**  **[REBUILT, phase 131, round 5, finding
`M6`(c) of `R131.011`: the blanket form of this sentence is now literally
contradicted by §8bis.3–§8bis.4, and carries the carve-out that §10's round-4
block already carried.]**  **Outside the clauses of §8bis explicitly labelled
`CLASSICAL` — Theorem 8bis.4(ii)–(iii) and the whole of §8bis.4, whose imports
are named in §11 and which are used by no clause of B.1–B.9** — no
construction, statement or proof in this paper uses a zero of `ζ`, the Riemann
Hypothesis, the positivity of any form, or any statement from rows C or D.
Deleting §8bis.3–§8bis.4 changes no clause verdict.  **[REBUILT, phase 131,
round 7, minor `p4`: round 6 reported this sentence de-garbled and it was not
— the colon, the double space and the capital survived verbatim.]**  With that
carve-out the statement of B.9 is unchanged, and the objects used are: rational
integers and their ideles; the lattices `L_S`; cyclotomic polynomials; the
graph sector `G` of Paper 43 with its composition, dagger and half-density;
the local factor (1.1); and the divisor poset.  The verification is the same
audit as Paper 43 §11: the dependency list of Section 11 below contains no
note that assumes a zero location, and the two analytic inputs — (1.1) and
Paper 43's **declared** trace of Definition 8.6, whose local terms (8.5) and
(8.5∞) are `PROVED-IN-REPOSITORY` in P123.042 and P123.035 — rest on Fourier
analysis on `Q_p` and `R` alone.  **[REBUILT, phase 131, round 2, finding
`F12`(c): the round-1 text cited Paper 43 "Def. 8.1", the definition Paper 43
§13.6 **withdrew**; the correct citation is Definition 8.6, and Remark 3.7's
sentence "nothing in row B depends on Paper 43's Definition 8.1" is thereby
literally true and no longer in tension with §11.]**

**[REBUILT, phase 131 — independence of the new material, stated exactly.]**
The new §3bis rests on: Paper 43 Lemma 3.3 (the valuation splitting), (9.5b)
(the slice maps), Definition 8.6 and (8.5)/(8.5∞) (the declared local terms,
both `PROVED-IN-REPOSITORY` from P123.042 and P123.035), Lemma 8.2 (the exact
orbital values), Theorem 8.8 (absolute convergence off the identity),
Definition 8A.7d (`c := 0`), Theorem 8A.7c (the colimit trace), Theorem 7.1(c)
and Theorem 8A.9 (the shadow and the Lefschetz integrand), Theorem 9.1 (the
Tate characters), Theorem 9.8 (`𝓝 = 0`), Lemma 9.14a0 and Theorems 9.14,
9.14a–b (the completion and its splitting).  Not one of these uses a zero of
`ζ`, RH, positivity, or the explicit formula as an input.

In particular, and still without any carve-out, **`Λ` is derived, never
assumed**: (3bis.8) exhibits
`Λ(p^k) = \log p` as the multiplicative Haar volume of the valuation shell
`p^kZ_p^×` (P123.042 §1), and the vanishing of `Λ` at composite `n` as the
statement that no single place has a shell of modulus `1/n`.  This is the
discipline of Paper 43 Remark 9.7a(1), applied here to row B: nothing selects
an arithmetic family from outside — the family is selected by the monoid
`(N_{≥1},×)` and realized by (3bis.3) — and no identity between the trace and
a sum over zeros is used, asserted or implied.  Two things are therefore
**not** claimed anywhere in this paper: any statement about zeros (the
explicit formula for a point class such as `Γ_n^{rad}` diverges, and §3bis
never writes it), and any sign or positivity (Paper 43 Theorem 14.1 forbids a
Hodge-index shape on `N_A` as it stands, and Theorem 8.3(v) shows the
arithmetic classes are not even primitive).  ∎  `PROVED`

---

## 8bis. The two Gram forms, the infinite genus, and the Weil interface

**[REBUILT, phase 131, round 4.  The round-3 version of this section claimed
that the Gram form of the Frobenius family *is* the Weil kernel.  That is
**false**, and it is refuted by this paper's own Corollary 3ter.10b: the
archimedean block of the Frobenius Gram matrix carries the arithmetic
indicator of (3ter.9) and **vanishes for large `N`**.  The adversarial audit
`R131.008` finding `F1` and the final audit `R131.009` both state this, and it
is repaired here — not softened.  The repair is an improvement: the Weil
kernel is the Gram form of the **unit-averaged** family `Frob ⋆ Δ^{rad}`, and
the split into finite and archimedean halves is exactly the
complementary-slice dichotomy of Remark 3ter.13a.  The round-3 statements are
recorded as withdrawn in §9bis W16–W18.]**

Row B's deliverable here is an *object*: a Gram form.  **The sign is row D's,
and nothing below claims it.**

#### Standing conventions for §8bis  **[REBUILT, phase 131, round 5.]**

The round-4 section dropped two hypotheses that it had itself established
elsewhere — the auditor's standing warning (`R131.011` §6) — and both are now
fixed **once, here**, and carried explicitly into every statement below.

**(C1) The chart quantifier: `T` means `T_∞` on `D_A^∞`.**  **[Finding `M4` of
`R131.011`; mandatory.]**  Paper 43's `T = T_S` at a fixed finite chart has
finite part running over `p ∈ S_f` **only** (Theorem 3bis.7, §9.1).  Whenever a
statement of §8bis involves a profile whose support radius exceeds the chart
window `\log ℓ_{next}(S)` — and §8bis.4 uses windows `[L/2,L]` with `L → ∞`,
hence all primes up to `e^{L}` — the trace meant is the **colimit trace**
`T_∞` on `D_A^∞` (Paper 43 Theorem 8A.7c), for which the prime sum is complete
at every fixed support radius (a finite sum, by Theorem 8A.7c(a)–(b)).
Accordingly, **throughout §8bis**:

  * `W_{fin} := Σ_{q\ \text{prime},\,k≥1}(\log q)q^{−k/2}(δ_{k\log q}+δ_{−k\log q})`
    is the **colimit** kernel, over **all** primes;
  * `T` means `T_∞`, and `I_A(·,·) := T_∞(·⋆·^†)` on `D_A^∞`;
  * at a **fixed finite chart** `S`, every displayed identity holds verbatim
    provided `supp` of the relevant profile lies inside the window
    `\{|t| < \log ℓ_{next}(S)\}` (Theorem 8A.7c(e)); outside it the two differ
    by the finite sum (8A.21).
  * **In particular (8bis.10) is a colimit statement.**  At a fixed finite
    chart it is *false*: a kernel carrying only the primes of `S_f` is not the
    Weil kernel, and by Paper 43 Theorem 14.1 **both** forms are indefinite
    there.  This is said again inside Theorem 8bis.4.

Every value computed in §8bis is unchanged by (C1): for a Gram entry,
`m/n = q^{±k}` forces `q | mn`, hence `q ∈ S_f` for any chart containing
`P(mn)`.  Only the quantifier moves.

**(C2) The normalization of the level-`N` factors.**  **[Finding `M5`.]**
Definition 3ter.8 offers two conventions: the **bare** one, with unnormalized
indicators `\mathbf 1_{n^{−1}(1+r^NZ_r)}`, and the **`♭`** one, divided by
`∏_{r}vol(1+r^NZ_r)`.  §8bis works in the **bare** convention — the one
Theorem 8bis.1 adopts and whose convolution constants it carries — and every
statement below says which normalization it is in.  The conversion factor is

    V_N(n) := ∏_{r ∈ S_f∖P(n)} vol(1+r^NZ_r)
            = ∏_{r ∈ S_f∖P(n)} \big((r−1)r^{N−1}\big)^{−1} ,          (8bis.0)

which **decays geometrically in `N`**.  Consequently a quantity that grows
linearly in `N` in one convention tends to `0` in the other, and §8bis
headlines **no rate**: what is convention-free, and what is stated, is
Remark 8bis.1c — the point-class pairing `I_A(Frob_n,Frob_n)` **does not
exist**, because `Frob_n ∉ D_A`.

### 8bis.1 The two Gram forms

**Theorem 8bis.1 (off-diagonal entries of the Frobenius Gram form).**  Let
`m,n ≥ 2`, `m ≠ n`, with `P(mn) ⊆ S_f`, and let
`Frob_m^{sm}, Frob_n^{sm} ∈ D_A` be smeared Frobenii (Definition 3ter.8) with
archimedean profiles `h_m, h_n` and level `N`.  **[REBUILT, phase 131,
round 4, finding `F3`:]**  assume `ε < ε_0(A,S)`, where `A ⊆ N_{≥2}` is the
finite set of labels in play and `ε_0(A,S) > 0` is chosen so that for every
`m,n ∈ A` the support of the convolved profile `h_m ⋆ h_n^†` — an interval of
width `≤ 2ε` around `n/m` — contains **no** point of the discrete set
`\{q^{−k} : q ∈ S_f, k ∈ Z\}` other than `n/m` itself when `n/m` is such a
point.  (Such an `ε_0` exists because `\{q^{−k}\}` is discrete in `R_{>0}`
and `A` is finite.)  Then

    I_A(Frob_m^{sm}, Frob_n^{sm}) = T\big(\,Frob_{m/n,\;P(m)∪P(n)}^{sm}\,\big) , (8bis.1)

a smeared Frobenius at the rational label `r = m/n` and prime set
`F = P(m)∪P(n)` (Theorem 3ter.7).  Its finite part is

    contact_{fin}\big(Frob_{r,F}\big) =
      \begin{cases} (\log q)\,q^{−k/2} & r = q^{±k},\ q\ \text{prime},\ k ≥ 1,\\
                    0 & \text{otherwise,}\end{cases}                  (8bis.2)

i.e. **nonzero exactly when `m/n` is a positive or negative power of a single
prime**; and it is symmetric under `r ↦ r^{−1}`, i.e. under `†`.

and the **archimedean part of the same entry** carries the arithmetic
indicator of (3ter.9):

    W_∞\big(Frob_{r,F}^{sm}\big) = \Big(∫_0^∞K(t)\,(h_m⋆h_n^†)(e^{−t})\,dt\Big)
        ·∏_{s ∈ S_f∖F}\mathbf 1\big[\,s^N \mid (n−m)\,\big] ,           (8bis.2a)

which **vanishes for every sufficiently large `N`** whenever `S_f ⊋ F`.
Finally the convolution of the level-`N` coset indicators contributes the
constant

    c_N(m,n) := ∏_{s ∈ S_f ∖ (P(m) ∩ P(n))} vol(1+s^NZ_s) ,          (8bis.2b)

whose index set is the complement of the **intersection** `P(m)∩P(n)`, not of
the union `F = P(m)∪P(n)`.  **[CORRECTED ; see §12.  The earlier
text read `∏_{s∈S_f∖F}vol(1+s^NZ_s)`, "which is `1` in the normalized (`♭`)
convention".  Both clauses were false whenever `P(m) ≠ P(n)`: the places of
`P(m) △ P(n)` each contribute a further `vol(1+s^NZ_s)`, because there one
factor carries a coset indicator and the other carries no condition at all.]**
In the `♭` convention the entry is divided by `V_N(m)V_N(n)`, and since
`V_N(m)V_N(n) = c_N(m,n)·∏_{s∈S_f∖F}vol(1+s^NZ_s)`, the constant there is
`∏_{s∈S_f∖F}vol(1+s^NZ_s)^{−1}`, which is `1` exactly when `F = S_f`.

*Proof.*  `I_A(F,G) = T(F⋆G^†)` (Paper 43 Def. 9.2), and at the level of point
classes `Frob_m⋆Frob_n^† = Frob_{m/n,\,P(m)∪P(n)}` by Theorem 3ter.7(i); the
smeared version is the convolution of that measure with the composed
archimedean profile and the convolved coset indicators, which is again of the
form (3ter.7) with `n` replaced by `r`, `P` by `F`, `h` by `h_m⋆h_n^†`, and an
extra scalar computed place by place as follows.  Write `U_s := 1+s^NZ_s`.  By
(3ter.7) the factor of `Frob_m^{sm}` at `s` is `1_{m^{−1}U_s}` if `s ∉ P(m)`
and the constant `1_{Z_s^×}` if `s ∈ P(m)`; and the factor of
`(Frob_n^{sm})^†` at `s` is `1_{nU_s}` if `s ∉ P(n)` (the dagger inverts
`x_s`, and `1_{n^{−1}U_s}(x_s^{−1}) = 1_{nU_s}(x_s)`) and `1_{Z_s^×}` if
`s ∈ P(n)`.  Convolving on the compact group `Z_s^×` with its **probability**
Haar measure gives four cases:

  * `s ∉ P(m)∪P(n)`: `1_{aU_s} ⋆ 1_{bU_s} = vol(U_s)·1_{abU_s}`, contributing
    `vol(U_s)` and leaving the coset indicator at `(n/m)U_s`;
  * `s ∈ P(n)∖P(m)`: `(1_{m^{−1}U_s} ⋆ 1_{Z_s^×})(x) = ∫_{m^{−1}U_s}1\,dy
    = vol(U_s)` for every `x ∈ Z_s^×`, contributing a **further** `vol(U_s)`
    and leaving no condition;
  * `s ∈ P(m)∖P(n)`: symmetrically, another `vol(U_s)`;
  * `s ∈ P(m)∩P(n)`: `1_{Z_s^×} ⋆ 1_{Z_s^×} = 1_{Z_s^×}`, contributing `1`.

Multiplying over `s ∈ S_f` gives (8bis.2b); and in every case the surviving
factor has the shape (3ter.7) prescribes for the index `r` and the prime set
`F`, namely a coset indicator at `s ∉ F` and no condition at `s ∈ F`.
**[CORRECTED : the earlier proof asserted the scalar
`∏_{s∉F}vol(1+s^NZ_s)`, justified only by "convolution of the indicator of a
coset of an open subgroup with itself is that volume times the indicator of the
product coset", which does not cover the places of `P(m) △ P(n)`.]**  For (8bis.2) repeat the proof of Theorem 3ter.10 with
`c_r K_F` in place of `c_nK_{P(n)}`.  The support is

    \{\,(1/r\ \text{at}\ ∞;\ u_q ∈ Z_q^×\ \text{at}\ q ∈ F;\ 1/r\ \text{at}\
      s ∉ F\,)\,\}

(`1/r` meaning the positive real `n/m`), and a shell `q^{m'}Z_q^×` of `Im j_q`
meets it in a set of positive Haar measure **iff** the archimedean coordinates
agree, `q^{−m'} = 1/r`, i.e. `r = q^{m'}` — and then automatically `q ∈ F`,
because `r = q^{m'}` forces `q ∈ P(r) ⊆ P(m)∪P(n) = F`.  **[REBUILT, phase 131,
round 5, note `n2` of `R131.011`: the round-4 text gave "`q ∈ F` so that the
whole of `Z_q^×` is covered" as a *second* condition.  That is not the
operative reason: for the **smeared** class the level-`N` coset at `s ∉ F` is
**open**, so a shell at `s ∉ F` can meet the support in positive measure.  What
actually kills it is the archimedean coordinate together with `ε < ε_0`:
`s^{−m'}` must lie within `2ε` of `n/m`, which by the choice of `ε_0` forces
`s^{−m'} = n/m`, hence `s ∈ P(r) ⊆ F`.  The conclusion is unchanged.]**  On that shell
`τ_q = q^{−|m'|/2}` (Paper 43 Lemma 8.2(i)) and the shell volume is `\log q`
(P123.042 §1; Theorem 8bis.8 below), giving (8bis.2); the unit packets vanish
for the reason of Theorem 3ter.10 (`1 ∉ supp(h_m⋆h_n^†)`, which holds because
`m ≠ n` and `ε < ε_0`).  Symmetry under `r ↦ r^{−1}` is `τ_q(x^{−1}) = τ_q(x)`
(Lemma 4.5, Paper 43 Lemma 8.4), and equals the statement that (8bis.2)
depends on `|m'|` only.  For (8bis.2a) apply the archimedean computation of
Theorem 3ter.10 with `r` in place of `n`: the numerator of `r − 1 = (m−n)/n`
is `m−n`, so the condition `r ∈ 1+s^NZ_s` reads `s^N \mid (n−m)`.  ∎  `PROVED`

**Theorem 8bis.1b (the diagonal of the Frobenius Gram form, computed).**
**[REBUILT, phase 131, round 4, finding `F2`: the round-3 section excluded
`r = 1` and therefore never computed the diagonal of the matrix it called
`PROVED`.]**  Let `n ≥ 2`, `P := P(n)`, and let `Δ^{(n),[φ_ε,N]} ∈ D_A` be the
smeared idempotent

    Δ^{(n),[φ_ε,N]}(x) := φ_ε(\log|x_∞|)·∏_{r∈S_f∖P}\mathbf 1_{1+r^NZ_r}(x_r) ,

with `φ_ε ∈ C_c^∞(R)` real, even, supported in `[−ε,ε]`, and **of unit
height**, `φ_ε(0) = 1` (write `φ_ε(t) = φ(t/ε)` for a fixed even
`φ ∈ C_c^∞([−1,1])` with `φ(0) = 1`).  **[REBUILT, phase 131, round 5, finding
`M5`: the normalization is now part of the statement.  This theorem computes
`T_∞` of the displayed object — unit archimedean height, **bare** level-`N`
indicators — and of nothing else; the passage to the actual Gram diagonal, in
either convention, is Corollary 8bis.1b′, where the conversion factor
`V_N(n)` of (8bis.0) appears.]**  Then, with `c := 0`:

  (i) *no shell contributes*: for every `q ∈ S_f` and `k ≠ 0` the shell term
      vanishes, because the archimedean coordinate of `j_q(q^kw)` is `q^{−k}`
      and `\log q^{−k} ∉ supp\,φ_ε` for `ε < \tfrac12\log 2`;
  (ii) *the unit packets at `p | n` vanish*, because `a_p = Δ^{(n),[φ_ε,N]}∘j_p`
      is **constant** on `Z_p^×` (there is no condition at `p`), so
      `a_p(u) − a_p(1) ≡ 0`;
  (iii) *the unit packets at `r ∤ n` do not vanish, and are computed exactly*:

        (\log r)∫_{Z_r^×}\frac{a_r(u)−a_r(1)}{|1−u|_r}\,du
          = −(\log r)\Big[\,\frac{r−2}{r−1} + (N−1)\,\Big] ,        (8bis.3)

      so that

        Σ_{q∈S_f}W_q\big(Δ^{(n),[φ_ε,N]}\big)
          = −Σ_{r∈S_f∖P}(\log r)\Big[\frac{r−2}{r−1} + (N−1)\Big] ,  (8bis.3′)

      **exactly, for every `N ≥ 1`** — a divergence that is **linear in `N`**
      at each place `r ∉ P(n)`;
  (iv) *the archimedean term diverges logarithmically in `ε`*:

        W_∞\big(Δ^{(n),[φ_ε,N]}\big) = −\log\tfrac1ε + O(1) ,          (8bis.4a)

      by the mechanism of Theorem 8bis.2.

  Consequently `T_∞(Δ^{(n),[φ_ε,N]})` is finite for each fixed `(ε,N)` and
  **has no limit as `ε → 0` or `N → ∞`**; both divergences are **negative**.

*Proof.*  (i) `φ_ε` is supported in `|\log|x_∞|| ≤ ε` and
`|\log q^{−k}| = |k|\log q ≥ \log 2 > 2ε`.

(ii) By (9.5b), `j_p(u) = (1` at `∞`; `u` at `p`; `1` elsewhere`)` for
`u ∈ Z_p^×`; the archimedean coordinate is `1`, so `φ_ε(0) = 1`, and the
indicators at `r ∈ S_f∖P` are evaluated at `1 ∈ 1+r^NZ_r`, giving `1`.  Since
`p ∈ P` carries no condition, `a_p ≡ 1` on `Z_p^×` and the packet vanishes.

(iii) For `r ∈ S_f∖P`, the same computation gives
`a_r(u) = \mathbf 1_{1+r^NZ_r}(u)` and `a_r(1) = 1`, so

    (\log r)∫_{Z_r^×}\frac{a_r(u)−1}{|1−u|_r}du
      = −(\log r)∫_{Z_r^×∖(1+r^NZ_r)}|1−u|_r^{−1}\,du .

Stratify `Z_r^×` by `j := v_r(1−u)`.  With `du` the **probability** Haar
measure of `Z_r^×` (the normalization of (8.5)), the subgroup `1+r^jZ_r` has
index `(r−1)r^{j−1}` in `Z_r^×` for `j ≥ 1`, so
`vol(1+r^jZ_r) = \big((r−1)r^{j−1}\big)^{−1}`, and

    vol\{\,v_r(1−u) = j\,\} = \frac{1}{(r−1)r^{j−1}} − \frac{1}{(r−1)r^{j}}
        = r^{−j}   (j ≥ 1),
    vol\{\,v_r(1−u) = 0\,\} = 1 − \frac{1}{r−1} = \frac{r−2}{r−1} ,

the two adding to `1` as they must (`(r−2)/(r−1) + Σ_{j≥1}r^{−j} = 1`).  On
the stratum `j` the integrand `|1−u|_r^{−1}` is `r^{j}`, constant.  Hence

    ∫_{Z_r^×∖(1+r^NZ_r)}|1−u|_r^{−1}du
      = \frac{r−2}{r−1}·1 + Σ_{j=1}^{N−1} r^{−j}·r^{j}
      = \frac{r−2}{r−1} + (N−1) ,

which is (8bis.3).  (For `r = 2` the first term is `0`, correctly: `Z_2^×
= 1+2Z_2`.)  Summing over `r ∈ S_f∖P` and adding the vanishing terms (i),(ii)
gives (8bis.3′).

(iv) `b := Δ^{(n),[φ_ε,N]}∘j_∞` is `b(t) = φ_ε(t)` in the logarithmic
coordinate, because `j_∞(x)` has every finite coordinate `1 ∈ 1+r^NZ_r`.  Here
`b(0) = φ_ε(0) = 1 ≠ 0`, so the identity class **is** in the support and
(8.5∞) is used with its counterterm:

    W_∞ = (γ+\log 4π)·1 + ∫_0^∞K(t)\big[\,b(t)+b(−t)−2e^{−t/2}\,\big]dt .

Split at `t = ε`.  On `(0,ε)`: `K(t) = \tfrac1{2t}+O(1)` and, since `φ` is
even and smooth with `φ(0)=1`, `φ(t/ε)−e^{−t/2} = O((t/ε)^2)+O(t)`, so
`∫_0^ε K(t)·2[φ(t/ε)−e^{−t/2}]dt = O(1)` (indeed
`∫_0^ε \tfrac1{2t}·O(t^2/ε^2)dt = O(1)` and
`∫_0^ε\tfrac1{2t}O(t)dt = O(ε)`).  On `(ε,∞)`: `b(±t) = 0`, so the integrand
is `−2K(t)e^{−t/2}`, and `K(t)e^{−t/2} = \tfrac1{2t}+O(1)` near `0` gives
`−2∫_ε^∞K(t)e^{−t/2}dt = −\log\tfrac1ε + O(1)`.  Adding the constant
`γ+\log4π` gives (8bis.4a).

The last sentence: (8bis.3′) is exact and linear in `N` with negative slope
`−Σ_{r∈S_f∖P}\log r`, and (8bis.4a) tends to `−∞`; both are negative, and
neither has a limit.  ∎  `PROVED`

**Corollary 8bis.1b′ (the Gram diagonal, in both conventions).**  **[REBUILT,
phase 131, round 5, finding `M5` of `R131.011`.]**  Let `F := Frob_n^{sm}` be
the smeared Frobenius of Definition 3ter.8 with archimedean profile `h` and
level `N`, in the **bare** convention (C2).  Then

    F ⋆ F^† = V_N(n) · Δ^{(n),[\,h⋆h^†,\,N\,]} ,                       (8bis.3a)

because at each `r ∈ S_f∖P(n)` the convolution of `\mathbf 1_{n^{−1}U_r}` with
`\mathbf 1_{nU_r}` is `vol(U_r)\cdot\mathbf 1_{U_r}`, `U_r := 1+r^NZ_r`, and at
`p ∈ P(n)` there is no condition.  Hence, with `Q_N(n)` the bracketed value of
Theorem 8bis.1b,

    I_A(F,F) = V_N(n)·\Big[\,−Σ_{r∈S_f∖P(n)}(\log r)\big(\tfrac{r−2}{r−1}+N−1\big)
                 − \log\tfrac1{ε} + O(1)\,\Big] .                     (8bis.3b)

Consequently, **and this is the point of stating the convention**:

  * in the **bare** convention, `V_N(n)` decays geometrically while the
    bracket grows linearly, so `I_A(F,F) → 0` as `N → ∞` (for fixed `ε`);
  * in the **`♭`** convention (`F^♭ := V_N(n)^{−1}F`), `I_A(F^♭,F^♭) =
    V_N(n)^{−1}[\,\cdots\,] → −∞` geometrically;
  * in **both**, the bracket is negative and the archimedean part
    `−\log(1/ε)` diverges as `ε → 0` for fixed `N`.

**No rate is headlined anywhere in this paper**, because no rate is
convention-free.  What is convention-free is Remark 8bis.1c.  ∎  `PROVED`
(Theorem 8bis.1b and the displayed convolution of coset indicators)

**Remark 8bis.1c (why the diagonal has no limit, and why that is expected).**
The Frobenius point classes are **not** elements of `D_A` (they are
multipliers, Remark 3bis.4b, Theorem 3ter.14), so there is no reason for
`I_A(Frob_n,Frob_n)` to exist, and Corollary 8bis.1b′ says it does not: the
regularization parameters `(ε,N)` cannot both be removed.  This is consistent
with Paper 43 Theorem 14.1(a) (`I_A` has infinite negative index) and with
Paper 43 Remark 8.11 (`T(Δ)` is undefined).  **[REBUILT, phase 131, round 5,
finding `M5`:]**  it is also the only **convention-free** statement available
about the diagonal: by Corollary 8bis.1b′ the *rate* — indeed the *direction*
of the limit in `N` — depends on the normalization of the level-`N` factors,
so this paper asserts the **non-existence** and **no rate**.
It is also why Theorem 3ter.14 places the point classes in `N_A^{dist}` and
**not** in `D_A`, and why Paper 43 does not extend `I_A` to
`N_A^{dist}×N_A^{dist}`.

**Corollary 8bis.1d (the Frobenius Gram form carries only the FINITE half of
the Weil kernel).**  **[REBUILT, phase 131, round 4, finding `F1`.  The
round-3 Corollary 8bis.1a asserted the opposite and is WITHDRAWN, §9bis W16.]**
Write

    W_{fin}(t) := Σ_{q\ \text{prime},\,k≥1}(\log q)q^{−k/2}
                  \big(δ_{k\log q} + δ_{−k\log q}\big) ,
    ω_∞ = K(|t|)\,dt ,

for the two halves of (3bis.9).  Let `A ⊂ N_{≥2}` be finite,
`G := Σ_{n∈A}c_nFrob_n^{sm}`, `ε < ε_0(A,S)`, and let `N` be large enough that
`s^N ∤ (n−m)` for some `s ∈ S_f∖(P(m)∪P(n))`, for every pair `m ≠ n` in `A`
(possible whenever `S_f ⊋ ⋃_{n∈A}P(n)`, since `n−m ≠ 0`).  Then

    I_A(G,G) = Σ_{m≠n} c_mc_n·V_N^{(m,n)}·W_{fin}(\{\log m−\log n\})
                        ·(h_m⋆h_n^†)(n/m)
               + Σ_{n∈A} c_n^2·I_A(Frob_n^{sm},Frob_n^{sm}) ,          (8bis.5)

`V_N^{(m,n)} := c_N(m,n) = ∏_{s∈S_f∖(P(m)∩P(n))}vol(1+s^NZ_s)` of (8bis.2b)
— which at `m = n` is exactly the `V_N(n)` of (8bis.0), so one formula gives
both the off-diagonal and the diagonal constants — the diagonal being
Corollary 8bis.1b′, and with **no archimedean off-diagonal block at all**.
The Weil kernel is `W_{fin} + ω_∞`; the Frobenius family carries `W_{fin}` and
not `ω_∞`.

**[REBUILT, phase 131, round 5, finding `m2` of `R131.011`: the round-4
display wrote this as `Σ c_mc_n W_{fin}(\{\log m−\log n\})`, an **equality**
with the *atom mass* alone.  The entry is the atom mass times the value of the
convolved profile at the label and times the convolution constants — both of
which (8bis.2)/(8bis.2a) supply and the round-4 display silently dropped.
With unit-height profiles `(h_m⋆h_n^†)(n/m) = 1`; in the `♭` convention the
constant becomes `∏_{s∈S_f∖F}vol(1+s^NZ_s)^{−1}`, which is `1` only when
`F = S_f`.  **[CORRECTED : this passage previously said
`V_N^{(m,n)} = 1` in the `♭` convention, which is false whenever `F ≠ S_f`;
see (8bis.2b) and §12.]**]**

*Proof.*  Theorem 8bis.1 for the off-diagonal finite part, with its profile
value and convolution constant carried; (8bis.2a) with the stated choice of
`N` for the vanishing of the off-diagonal archimedean part; and
Corollary 8bis.1b′ for the diagonal.  ∎  `PROVED`

**Theorem 8bis.1e (the Weil kernel IS the Gram form of the unit-averaged
Frobenius family).**  **[REBUILT, phase 131, round 4 — this is the repair of
`F1`, and it is the new content of §8bis.]**  Let
`Γ_n^{rad} = Frob_n ⋆ Δ^{rad}` (Proposition 3ter.5) and let
`Γ_m^{rad,sm} := Γ_{h_m}`, `Γ_n^{rad,sm} := Γ_{h_n}` be the smeared radial
classes of Definition 3bis.6, with `h_m, h_n ∈ C_c^∞(R)` supported near
`\log m`, `\log n` and `0 ∉ supp(h_m ⋆ h_n^†)`.  **[REBUILT, phase 131,
round 5, findings `m1` and `M4`: the two hypotheses this statement inherits
are now carried explicitly.  (a) *Width:* assume `ε < ε_0(A,S)` in the sense
of Theorem 8bis.1, so that `supp(h_m⋆h_n^†)` meets `\{q^{−k}\}` at most in
`n/m`; without it the right-hand side may pick up further atoms.  (b)
*Chart:* `T` is the colimit trace `T_∞` on `D_A^∞` and `W_{fin}` is the
**colimit** kernel, by (C1); at a fixed finite chart `S` the identity holds
verbatim only for `supp(h_m⋆h_n^†)` inside the window
`\{|t| < \log ℓ_{next}(S)\}`, and otherwise its left-hand side omits the
atoms at the primes `ℓ ∉ S_f`.]**  Then, for **every** level and with **no
indicators and no arithmetic side conditions**,

    I_A\big(Γ_m^{rad,sm}, Γ_n^{rad,sm}\big) = T\big(Γ_{h_m⋆h_n^†}\big)
      = ∫_R (h_m⋆h_n^†)\;d\big(W_{fin} + ω_∞\big) ,                   (8bis.6)

and in the limit of concentrated profiles the entry is

    W_{fin}\big(\{\log m − \log n\}\big) + K\big(|\log m − \log n|\big) : (8bis.7)

**the full Weil kernel**, both halves, for every pair `m ≠ n`.  The diagonal
`m = n` is Theorem 8bis.2, which computes exactly this radial self-pairing.

*Proof.*  `Γ_m^{rad}⋆(Γ_n^{rad})^† = Γ_{m/n}^{rad}` by Theorem 3bis.5(i)–(ii)
(composition of level-set Haar measures on `(R_{>0},×)`), and on profiles
`Γ_{h}⋆Γ_{g}^† = Γ_{h⋆g^†}` by Lemma 3bis.6a.  Then (8bis.6) is Theorem 3bis.7
applied to `h_m⋆h_n^†`, i.e. Definition–Theorem 3bis.8's identity
`T(Γ_h) = ∫h\,d(W_{fin}+ω_∞)` for `0 ∉ supp h`.  There are **no indicators**
because a radial class is `K^♮`-invariant: in the notation of (3ter.7) the
factors `∏_{r}\mathbf 1_{\,·}(x_r)` are replaced by the constant `1` on the
whole compact part, so the evaluation at `j_∞(x)` — whose finite coordinates
are `1` — is unobstructed, and (3ter.9)'s arithmetic indicator is identically
`1`.  Formula (8bis.7) is the atom-plus-density reading of (8bis.6)
(Definition–Theorem 3bis.8) as `h_m⋆h_n^†` concentrates at
`\log m − \log n ≠ 0`.  ∎  `PROVED`

**Theorem 8bis.1′ (the two halves of the Weil kernel; the complementary-slice
dichotomy, as a statement about Gram forms).**  **[REBUILT, phase 131,
round 4.]**  On Paper 43's declared carrier:

  (i) the **Frobenius** family `\{Frob_n^{sm}\}` has Gram form `W_{fin}` off
      the diagonal, with **no** archimedean block (Corollary 8bis.1d), and a
      diagonal that diverges as `−\log(1/ε)` archimedeanly and **linearly in
      `N`** at each place `r ∤ n` (Theorem 8bis.1b);
  (ii) the **unit-averaged** family `\{Frob_n ⋆ Δ^{rad}\} = \{Γ_n^{rad}\}` has
      Gram form the **full** Weil kernel `W_{fin} + ω_∞`, exactly and at every
      level (Theorem 8bis.1e);
  (iii) the mechanism is the complementary-slice dichotomy of Remark 3ter.13a
      and Corollary 3ter.10b: `supp\,Frob_n` is **disjoint from `Im j_∞`**
      (when `S_f ⊋ P(n)`), so the Frobenius sees no archimedean local term;
      convolving with the projector `Δ^{rad}` **spreads the support onto the
      whole modulus level set**, which meets `Im j_∞` in the point
      `j_∞(1/n)`, and that is where `ω_∞` comes from.

So: **the averaging projector `Δ^{rad}` is exactly what converts the finite
half of the Weil kernel into the whole of it**, at the cost (Lemma 3bis.3b) of
forgetting the factorization.  The two facts are two readings of one
projector.

*Proof.*  (i) is Corollary 8bis.1d and Theorem 8bis.1b; (ii) is
Theorem 8bis.1e; (iii) is Corollary 3ter.10b, Proposition 3ter.5 and the proof
of Theorem 8bis.1e (the indicators become trivial precisely because
`Δ^{rad}`-invariance removes the finite-coordinate conditions).  ∎  `PROVED`

### 8bis.2 The self-intersection of the diagonal is `−∞`

**Theorem 8bis.2 (infinite genus).**  **[REBUILT, phase 131, round 6, finding
`N1` of `R131.014`.  This is a **fixed-chart** theorem and is hereby
**explicitly exempted from the standing convention (C1)**; round 5's report
claimed the exemption had been inserted, and it had not.  The proof's uniform
bound (8bis.8b) is the *chart* constant `A_S`, and under `T_∞` the colimit
symbol is unbounded (`ω̂_{fin}^∞(0) = +∞`, Remark 8bis.4b(1)), so that step
would be false as stated.]**  **Fix a finite chart `S` with `S_f ≠ ∅` and read
`T = T_S`, exempting this theorem and Corollary 8bis.2a from (C1).**  Fix a
real even `φ ∈ C_c^∞(R)`, `φ ≢ 0`,
and for `ε > 0` let `F_ε ∈ D_A` be the `K^♮`-invariant test with archimedean
profile `ε^{−1}φ(t/ε)` in the coordinate `t = \log|x|_S` (that is,
`F_ε = Γ_{h}` of Definition 3bis.6 with `h(t) = ε^{−1}φ(−t/ε)`).  Then
`F_ε ⋆ F_ε^† → Δ = δ_1` weak-⋆, and, with `c := 0`,

    I_A(F_ε, F_ε) = T(F_ε ⋆ F_ε^†)
      = −\frac{\|φ\|_{L^2}^2}{ε}\Big(\log\tfrac1ε + O(1)\Big)
      \longrightarrow −∞  \qquad (ε → 0^+).                          (8bis.4b)

Equivalently, in the normalization-free form: if `G_ε := ‖F_ε‖_{L^2}^{−1}F_ε`,
so that `∫_{\hat C_S}|\hat G_ε|^2\,dχ = 1`, then

    I_A(G_ε,G_ε) = −\log\tfrac1ε + C_φ + o(1) ,
    C_φ = \log 2π − \frac{1}{\|φ\|_2^2}∫_R|\hatφ(σ)|^2\log|σ|\tfrac{dσ}{2π}
          + \lim\ \text{(bounded finite-place mean)} .                (8bis.4c)

*Proof.*  `F_ε ∈ D_A` by Lemma 3bis.6a, and `\hat F_ε` is supported on the
principal component `𝔠_0` with `\hat F_ε(τ) = \hatφ(ετ)` (Theorem 3bis.7's
computation of the radial Fourier transform, together with the scaling
`\widehat{ε^{−1}φ(\cdot/ε)}(τ) = \hatφ(ετ)`).  Weak-⋆ convergence
`F_ε⋆F_ε^† → δ_1` is `\widehat{F_ε⋆F_ε^†} = |\hatφ(ετ)|^2 → |\hatφ(0)|^2` with
`∫F_ε = \hatφ(0)`; normalizing `\hatφ(0) = 1` (possible since `φ ≢ 0` is real
even, after scaling) makes `(F_ε⋆F_ε^†)` an approximate identity.

By Paper 43 (14.1) with `c = 0`,

    I_A(F_ε,F_ε) = ∫_{\hat C_S}|\hat F_ε(χ)|^2\,\hat T(χ)\,dχ
                 = ∫_R |\hatφ(ετ)|^2\,\hat T(𝔠_0,τ)\,\tfrac{dτ}{2π} .

*The symbol.*  By Paper 43 **Theorem 9.7(b)** — **[REBUILT, phase 131,
round 4, finding `F5`: round 3 wrote "Theorem 9.7b(b)", conflating Thm. 9.7(b)
with the distinct Thm. 9.7b; the formula used is Thm. 9.7(b)]** — on `𝔠_0`,
`\hat W_∞(0,τ) = \log π − \mathrm{Re}\,ψ(\tfrac14 + \tfrac{iτ}2)`.  Since
`ψ(z) = \log z + O(|z|^{−1})` as `|z| → ∞` with `|\arg z| ≤ π/2`, and
`|\tfrac14+\tfrac{iτ}2| = \tfrac{|τ|}2 + O(|τ|^{−1})`,

    \hat W_∞(0,τ) = −\log|τ| + \log 2π + O(|τ|^{−1}) ,   |τ| → ∞.     (8bis.8)

**[REBUILT, phase 131, round 4, finding `F5`: (8bis.8) is an `|τ| → ∞`
statement and is used below after the substitution `σ = ετ`, where the region
`|σ| ≲ ε` corresponds to *bounded* `τ`, in which (8bis.8) is false.  The
bounded region is handled separately and contributes `O(1)`:]**  `\hat W_∞(0,·)`
is continuous on `R` and bounded above by its value at `τ = 0`,
`\hat W_∞(0,0) = \log π − ψ(1/4) = \log π + γ + 3\log 2 + π/2` (Paper 43
(14.2)), and bounded below on any compact set; hence for every `R_0 > 0`

    \Big|∫_{|τ|≤R_0}|\hatφ(ετ)|^2\,\hat T(𝔠_0,τ)\,\tfrac{dτ}{2π}\Big|
      ≤ C(R_0)·\|\hatφ\|_∞^2 = O(1)  \quad\text{uniformly in } ε,  (8bis.8a)

so the `|σ| ≤ εR_0` part of the scaled integral contributes
`ε^{−1}·O(ε) = O(1)` and does not affect (8bis.4b).

By Paper 43 (9.11), for `p ∈ S_f` and `κ_p = 1`,
`\hat W_p(𝔠_0,τ) = (\log p)\,2\,\mathrm{Re}\big(ζ_p/(1−ζ_p)\big)` with
`|ζ_p| = p^{−1/2}`, so

    \big|Σ_{p∈S_f}\hat W_p(𝔠_0,τ)\big| ≤ A_S
      := Σ_{p∈S_f}(\log p)\frac{2p^{−1/2}}{1−p^{−1/2}} < ∞ ,         (8bis.8b)

**uniformly in `τ`**.  Hence `\hat T(𝔠_0,τ) = −\log|τ| + O(1)` with an
explicit `O(1)` bounded by `\log 2π + A_S + o(1)`.  **[REBUILT, phase 131,
round 6, note `n2′` of `R131.014`:]**  note that `A_S = ω̂_{fin}(0)`
**exactly**, not merely a bound: every summand of `ω̂_{fin}` is maximized at
`τ = 0`, where `ζ_p = p^{−1/2}` is real and positive.  This is why
Theorem 8bis.4a concentrates its test at `τ = 0` — the symbol's maximum — and
why the numerics print one number for both quantities.

*The scaling.*  Substitute `σ = ετ`, using (8bis.8) on `|τ| > R_0` and
(8bis.8a) on `|τ| ≤ R_0`:

    I_A(F_ε,F_ε) = \frac1ε ∫_R |\hatφ(σ)|^2\,
        \big[\,\log ε − \log|σ| + O(1)\,\big]\,\tfrac{dσ}{2π} .

The integral `∫|\hatφ(σ)|^2\log|σ|\,dσ` converges absolutely (`\hatφ` is
Schwartz, and `\log|σ|` is locally integrable), and
`∫|\hatφ|^2\tfrac{dσ}{2π} = \|φ\|_{L^2}^2` by Plancherel.  Therefore

    I_A(F_ε,F_ε) = \frac{\|φ\|_2^2}{ε}\Big(\log ε + O(1)\Big) ,

which is (8bis.4b).  Dividing by `‖F_ε‖_{L^2}^2 = ε^{−1}\|φ\|_2^2` gives
(8bis.4c).  **[REBUILT, phase 131, round 6, finding `N2` of `R131.014`: round 5
renumbered the cross-references and **not** the displays, leaving six pointers
to equations that did not exist.  The displays themselves are renumbered here:
`(8bis.4b)`, `(8bis.4c)`, `(8bis.8b)`; the double assignments of `(8bis.5)` and
`(8bis.7)` are resolved.]**

**[REBUILT, phase 131, round 6, finding `N1` — and under `T_∞` the conclusion
is unchanged and *easier*.]**  For `ε < \tfrac12\log 2` the profile of
`F_ε⋆F_ε^†` is supported in `|t| ≤ 2ε < \log 2`, so it meets **no** atom of
`W_{fin}^∞`, whose support is `\{±k\log q\}` with every point of modulus
`≥ \log 2` (Theorem 3bis.7′(i)).  The finite part of `T_∞(Γ_{F_ε⋆F_ε^†})` is
therefore **identically zero** and (8bis.4b) is purely archimedean; no appeal
to (8bis.8b) is needed there.  So the theorem is stated at a fixed chart and
holds a fortiori on the colimit.  ∎  `PROVED` (at a fixed finite chart `S`; and
a fortiori for `T_∞`)

**Corollary 8bis.2a (Weil's `Δ·Δ = 2−2g` forces `g = ∞`).**  For a smooth
projective curve of genus `g` over `F_q`, `Δ·Δ = 2−2g`.  Theorem 8bis.2 says
the regularized self-intersection of the diagonal on the declared carrier
**diverges to `−∞`**; under Weil's dictionary this is `g = ∞`.  *This is an
interpretation, labelled as such, and is used by no theorem of this paper.*
The theorem is (8bis.4b).  It is consistent with — and sharpens — Paper 43
Theorem 14.1(a), which proves that `I_A` has infinite negative index;
(8bis.4b)–(8bis.4c) supply the **rate**, `\log(1/ε)` per unit of
`L^2`-normalized test, with the divergence coming entirely from the
archimedean symbol (8bis.8), the finite-place symbol being bounded by
(8bis.8b) at the fixed chart.  **[REBUILT, phase 131, round 5, finding `m3`:
the round-4 text cited "(8bis.6)" and "(8bis.7)", which by then denoted
Theorem 8bis.1e's radial Gram identity and its kernel value; the displays are
renumbered and the cross-references corrected.]**

**Remark 8bis.2b (a correction to the round-3 blueprint).**  **[REBUILT,
phase 131, round 3.]**  The blueprint states that the smeared self-pairing
"diverges like `−2\log(1/ε)`".  The factor `2` is not obtained in either
natural normalization, and the *rate* differs between them: with the
mass-normalized approximate identity (`∫F_ε = 1`) the divergence is
`−ε^{−1}\|φ\|_2^2\log(1/ε)`, one power of `ε^{−1}` faster than stated; with the
`L^2`-normalization the divergence is `−\log(1/ε) + O(1)`, with coefficient
`1`, not `2`.  Both are proved in Theorem 8bis.2.  The qualitative claim —
`Δ·Δ = −∞`, driven by `\hat W_∞ ∼ −\log|τ|` — is correct and is what the
theorem records.

### 8bis.3 The interface with Weil's criterion, stated honestly

**[REBUILT, phase 131, round 4.  The round-3 §8bis.3 was built on the false
Corollary 8bis.1a and its part (iii) is withdrawn (§9bis W17).  The interface
is rebuilt on the family that actually carries the Weil kernel — the radial
family — where the profile class is **all** of `C_c^∞(R)` and there is no
density question at all.]**

**Definition 8bis.3.**  For real `g ∈ C_c^∞(R)` let `Γ_g ∈ D_A^{rad}` be the
smeared radial class of Definition 3bis.6.  **[REBUILT, phase 131, round 5,
finding `m5` of `R131.011` — real versus complex profiles.]**  For a
**complex** `g ∈ C_c^∞(R;C)` the class `Γ_g` and the pairing are still
defined, and since the kernel `W_{fin} + ω_∞` is **real and even** one has

    I_A(Γ_g,Γ_g) = I_A(Γ_{Re\,g},Γ_{Re\,g}) + I_A(Γ_{Im\,g},Γ_{Im\,g}) ,  (8bis.8c)

with `Γ_g^† = Γ_{g^†}`, `g^†(t) = \overline{g(−t)}` (Lemma 3bis.6a); so every
statement below quantified over **real** profiles applies to a complex profile
through (8bis.8c), and §8bis.4's complex `g_L = ψ(t/L)e^{−iγ_0t}` is covered.
**[REBUILT, phase 131, round 7, minor `p8` of `R131.017`: this note wrote
`e^{+iγ_0t}` while Lemma 8bis.6b uses `e^{−iγ_0t}` — necessarily, so that the
resonance at `ρ_0 = \tfrac12+δ+iγ_0` cancels the oscillation.  Cosmetic (the
two are exchanged by `γ_0 ↦ −γ_0`) and now consistent.]**
*Proof of (8bis.8c):* **[REBUILT, phase 131, round 6, minor `m2′` of
`R131.014`: round 5 wrote the cross term as `2Re`, which is **even** in `τ` and
would **not** integrate to zero against the even symbol; the correct cross term
is `2Im`, which is **odd**.  The conclusion was right and the printed proof
self-defeating.]**  Put `A := \widehat{Re\,g}` and `B := \widehat{Im\,g}`, so
`\hat g = A+iB` and

    |\hat g|^2 = |A|^2 + |B|^2 + 2\,\mathrm{Im}\big(A\overline B\big) .

Since `Re\,g` and `Im\,g` are **real**, `A(−τ) = \overline{A(τ)}` and
`B(−τ) = \overline{B(τ)}`, hence `(A\overline B)(−τ) = \overline{(A\overline
B)(τ)}` and `\mathrm{Im}(A\overline B)` is an **odd** function of `τ`.  The
symbol `T̂` is **even** on the principal component (Paper 43 Theorem 9.7), so
the cross term integrates to `0` in (9.13), leaving (8bis.8c).  ∎  Call `Γ_g` **primitive** when its
ruling component vanishes,

    M(Γ_g) = ( λ_−(Γ_g), λ_+(Γ_g) )
           = ( ∫_R g(s)e^{s/2}ds , ∫_R g(s)e^{−s/2}ds ) = (0,0)
    ⟺ ĝ(∓i/2) = 0 ,                                                  (8bis.9)

the two **Tate conditions** (Lemma 3bis.6a, Paper 43 Theorem 9.1).  Write
`I_∂` for `I_A` restricted to primitive radial classes.  For a finite
`A ⊂ N_{≥2}` and widths `(ε_n)`, call
`g = Σ_{n∈A}c_n ρ_{ε_n}( · − \log n )` a **Dirichlet-polynomial profile**.

**Theorem 8bis.4 (the interface).**  **[REBUILT, phase 131, round 4.]**

  (i) *(`PROVED` here.)*  For real `g,g' ∈ C_c^∞(R)`,
      `I_A(Γ_g,Γ_{g'}) = T(Γ_{g⋆g'^†})`, and by Theorem 8bis.1e this is the
      **full Weil kernel** paired with `g⋆g'^†`: the finite atoms `W_{fin}`
      and the archimedean density `ω_∞ = K(|t|)dt`, plus, when
      `0 ∈ supp(g⋆g'^†)`, the regularized identity term of (8.5∞) with
      `c := 0`.  Primitivity is the pair of linear conditions (8bis.9).
  (ii) *(**`PROVED-IN-REPOSITORY`**; the only place in Paper 44 where zeros
      occur.)*  **[phase 132]** The explicit formula used here is no longer a
      `CLASSICAL` citation: it is **proved in the repository** as Paper 45
      Theorem 9.4 (and Corollary 9.4a for an arbitrary real even test), with a
      correct contour argument; **Weil's criterion itself, part (iii) below,
      remains `CLASSICAL`.**  The Weil explicit formula converts
      `T(Γ_{g⋆g^†})` into `Σ_ρ ĥ(ρ)` minus the Tate/polar terms,
      `h = g⋆g^†`; and **Weil's criterion** states that RH holds **if and only
      if** the resulting functional has a fixed sign for all such `h`.  On the
      primitive sector the Tate/polar terms drop by (8bis.9) (Paper 45
      Theorem 8.1 identifies the polar packet with `β_T`).
  (iii) *(the equivalence, `CLASSICAL`.)*  Consequently

        I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R)
        ⟺ RH .                                                        (8bis.10)

      **[REBUILT, phase 131, round 5, finding `M4` — the quantifier.]**
      (8bis.10) is a **colimit** statement: `I_∂` means `I_∞` on `D_A^∞` and
      `W_{fin}` is the kernel over **all** primes, by (C1).  **At a fixed
      finite chart it is false**: the kernel then carries only the primes of
      `S_f`, which is not the Weil kernel, and by Paper 43 Theorem 14.1 both
      forms are indefinite there.  With that quantifier:
      **this is Weil's criterion carried by row A's declared trace, and it is
      NOT new.**  It is stated here only to name the object whose Hodge index
      is at issue.  Its content over the classical statement is exactly
      Theorem 8bis.1e — that the Weil kernel is the Gram form of the
      **unit-averaged Frobenius family** `Frob ⋆ Δ^{rad}` — and that
      factorization is the new part.  There is **no density question** in
      (8bis.10): the profile class of the radial family is all of `C_c^∞(R)`
      by Definition 3bis.6.
  (iv) *(rebuilt in round 5; see Theorem 8bis.4a.)*  Two statements about the
      **pure Frobenius form** `Q_{fin}`, the quadratic form with kernel
      `W_{fin}` alone:
      **(a) `PROVED`** — `Q_{fin}` is **not** the Weil form: the two differ by
      `∫|ĥ(τ)|^2 ω̂_∞(τ)\,dτ/2π` with `ω̂_∞(τ) = Ŵ_∞(0,τ) =
      \log π − Re ψ(1/4+iτ/2)` **indefinite** (`≈ 5.372 > 0` at `τ = 0` by
      Paper 43 **(9.12b)**, `→ −∞` as `|τ| → ∞` by (8bis.8));
      **[phase 133, PANEL_2 MINOR-3: this cited Paper 43 (14.2), which is a
      lower bound for `m := \sup \hat T` **including the finite places**;
      the exact archimedean value `\max_τ \hat W_∞(0,τ) = \log π − ψ(1/4)
      ≈ 5.372` is Paper 43 (9.12b).  The argument is unaffected — every
      finite-place term at `τ=0` is positive and (14.2) is an inequality —
      but the typing was wrong, and it is the same mis-citation Paper 45 §1.5
      corrected in itself in phase 132.]**
      **(b) `PROVED` at every fixed finite chart (Theorem 8bis.4a)** —
      **positivity fails on `Q_{fin}`**: there is an explicit primitive radial
      class with `Q_{fin} > 0`.
      **[REBUILT, phase 131, round 5, finding `M1` of `R131.011` = `LF3` of
      `R131.012`.  The round-4 text claimed "the sign of the pure Frobenius
      Gram form is NOT RH", `PROVED`, and argued it by comparing the two
      forms.  That argument is a **non-sequitur**: "`Q_{fin} ≤ 0` on the
      primitive sector ⟺ RH" is a biconditional between two propositions of
      fixed truth value, and no comparison of two fixed quadratic forms can
      refute such a biconditional — it shows only that the forms are
      *distinct*, which nobody disputed.  The claim and its proof are
      **withdrawn** (§9bis W19) and replaced by (a), which is what the
      argument proves, and by (b), which is stronger and is the statement that
      actually matters.]**
  (v) *(`OPEN`, with the exact statement.)*  Whether the **Dirichlet-polynomial
      profiles** suffice:

      > `OPEN`: does `I_∂ ≤ 0` on all primitive radial classes `Γ_g` with `g`
      > a Dirichlet-polynomial profile of **constant** width `ε` imply
      > `I_∂ ≤ 0` on all primitive `Γ_g`, `g ∈ C_c^∞(R)`?

      §8bis.4 reduces the variant with **per-`n`** widths to the single
      explicit hypothesis `(H_L)`, which is itself **`OPEN`**
      (Theorem 8bis.7(c)), and records in Remark 8bis.7a(2) both why `(H_L)`
      is not supplied and why the constant-width class is not reached.
      **[REBUILT, phase 131, round 7, finding `A3`: this clause previously
      said §8bis.4 "settles" the per-`n` variant "modulo one named classical
      import"; `W23` withdrew that import as **false**, so nothing is
      settled — the per-`n` variant is reduced, not settled.]**  The **fixed-window obstruction
      stands**: in a window `[a,b] ⊂ (0,∞)` the gaps
      `\log(n+1)−\log n = \log(1+1/n)` are bounded **below** by
      `\log(1+e^{−b}) > 0`, so bumps of width `ε ≪ e^{−b}` at the points
      `\log n ∈ [a,b]` span nothing dense in `C_c^∞((a,b))`, and no limit
      `ε → 0` repairs it.  Only windows moving to `+∞` have vanishing gaps.

> **ROW D'S TARGET (boxed identically in Paper 43 §14.1, Paper 44 §8bis.4(vi)
> and §10.4, and Paper 45 §14.4).**  **[phase 133, PANEL_2 §5 / PANEL_3
> recommendation.]**
>
> **ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and c = 0 (Paper 45 Cor 9.6a); this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4. Standing negatives: Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a; Paper 44 Thm 8bis.7 is conditional under (H_L), OPEN.**

  (vi) *(the honest summary.)*  **Row B delivers the Gram form and its
      factorization through the Frobenius family; it does not deliver the
      sign.**  The object whose Hodge index is RH — in the colimit sense of
      (iii) — is the Gram form of `Frob ⋆ Δ^{rad}`, and **not** the Frobenius
      Gram form.  **[REBUILT, phase 131, round 5, finding `M1`/`LF3`:]** this
      rests on **(iii)** — the full kernel is what the criterion is about —
      and, at a chart, on the proved failure of positivity for `Q_{fin}`
      (Theorem 8bis.4a).  It does **not** rest on a comparison of symbols; the
      round-4 argument to that effect is withdrawn (§9bis W19).  The sign
      is row D's obligation (PLAN §8), and Paper 43 Theorem 14.1 proves that
      no Hodge-index shape is available on `N_A` as it stands, with
      Theorem 8bis.2 supplying the divergence rate.

*Proof.*  (i) is Theorem 8bis.1e, Lemma 3bis.6a and Paper 43 Theorem 9.1
(`λ_∓(Γ_g) = ∫g(s)e^{±s/2}ds`, whose vanishing is `ĝ(∓i/2) = 0` under the
Mellin–Fourier dictionary).  (ii) and (iii) are classical and carry that
label; the drop of the Tate terms is (8bis.9) with Paper 45 Theorem 8.1.
(iv)(a): by (8bis.8) and Paper 43 (9.12b) **[phase 133, PANEL_2 MINOR-3:
was "(14.2)"]**, `ω̂_∞` takes both signs, and the
difference of the two forms is `∫|ĥ|^2ω̂_∞\,dτ/2π` by (9.13); choosing `ĥ`
concentrated where `ω̂_∞ > 0` and where `ω̂_∞ < 0` shows the difference is a
nonzero form of both signs, so the two forms are distinct.  **This is all that
this argument gives, and it is all that (iv)(a) claims.**  (iv)(b) is
Theorem 8bis.4a.  (v) is the gap computation, as in round 3.  (vi) summarizes,
and rests on (iii) — **not** on (iv).  ∎  `PROVED` in (i),(iv); **`PROVED-IN-REPOSITORY` in (ii)**
(Paper 45 Theorem 9.4); `CLASSICAL` in (iii); `OPEN` in (v).
**[phase 133, PANEL_2 MAJOR-2: this footer still read "`CLASSICAL` in
(ii),(iii)".  The phase-132 relabel of (ii) — the explicit formula — to
`PROVED-IN-REPOSITORY` (Paper 45 Thm 9.4) was applied to the body of (ii), to
§10.4 items 2 and 4a, to the §0 banner and to one sentence of §11, but not
here.  Weil's **criterion**, (iii), remains `CLASSICAL`.]**

**Theorem 8bis.4a (positivity fails on the pure Frobenius form —
unconditionally, at every finite chart).**  **[REBUILT, phase 131, round 5,
finding `M1`: this is the auditor's stronger statement, proved.]**  Fix a
finite chart `S` with `S_f ≠ ∅`, and let

    Q_{fin}(g) := ∫_R (g⋆g^†)\,dW_{fin}^{S}
                = ∫_R |\hat g(τ)|^2\,ω̂_{fin}(τ)\,\tfrac{dτ}{2π} ,
    ω̂_{fin}(τ) := Σ_{p∈S_f}\hat W_p(𝔠_0,τ) ,                          (8bis.10a)

be the pure-Frobenius form on real radial profiles at that chart.  Then there
exists a **primitive** real `g ∈ C_c^∞(R)` — `\hat g(∓i/2) = 0` — with

    Q_{fin}(g) > 0 .

Hence the proposition "`Q_{fin} ≤ 0` on every primitive radial class" is
**false**, at every finite chart, with no hypothesis whatever.

*Proof.*  **Step 1 (the symbol is strictly positive at `τ = 0`).**  By Paper 43
(9.11) on the principal component, `\hat W_p(𝔠_0,τ) = (\log p)·
2Re(ζ_p/(1−ζ_p))` with `ζ_p = p^{−1/2}e^{i(τ\log p+θ_p)}`.  At `τ = 0` on the
principal component `θ_p = 0`, so `ζ_p = p^{−1/2} ∈ (0,1)` is real and

    ω̂_{fin}(0) = Σ_{p∈S_f}(\log p)\frac{2p^{−1/2}}{1−p^{−1/2}} > 0 ,   (8bis.10b)

a strictly positive number (each summand is positive and `S_f ≠ ∅`).  Moreover
`ω̂_{fin}` is real-analytic (Paper 43 Theorem 9.7(a)) and bounded,
`|ω̂_{fin}| ≤ A_S` by (8bis.8b).  By continuity choose `δ > 0` with
`ω̂_{fin}(τ) ≥ \tfrac12ω̂_{fin}(0) =: c > 0` for `|τ| ≤ δ`.

**Step 2 (a primitive test, produced by `Π`).**  Let `φ ∈ C_c^∞(R)` be real,
even, `φ ≢ 0`, and for `T > 0` set `g_{0,T}(t) := φ(t/T)` and

    g_T := Π\,g_{0,T} = −g_{0,T}'' + \tfrac14 g_{0,T} ∈ C_c^∞(R) ,

real, with `supp\,g_T = supp\,g_{0,T}` (`Π` is a local operator).  Then `g_T`
is **primitive**:

    λ_∓(Γ_{g_T}) = ∫_R\big(−g_{0,T}''+\tfrac14g_{0,T}\big)e^{±s/2}ds
                 = −\tfrac14∫g_{0,T}e^{±s/2}ds + \tfrac14∫g_{0,T}e^{±s/2}ds = 0,

integrating by parts twice (no boundary terms: `g_{0,T}` has compact support)
and using `\partial_s^2 e^{±s/2} = \tfrac14e^{±s/2}`.  This is Paper 45
Theorem 10.4's operator, and it is exactly why that operator is the
primitivizer.  In Fourier terms `\hat g_T(τ) = (τ^2+\tfrac14)\hat g_{0,T}(τ)
= (τ^2+\tfrac14)\,T\,\hatφ(Tτ)`, and the vanishing at `τ = ∓i/2` is visible as
the zero of `τ^2+\tfrac14`.

**Step 3 (concentration).**  Write `M_{bulk}(T) := ∫_{|τ|≤δ}|\hat g_T|^2
\tfrac{dτ}{2π}` and `M_{tail}(T) := ∫_{|τ|>δ}|\hat g_T|^2\tfrac{dτ}{2π}`.
Substituting `σ = Tτ`,

    ∫_{|τ|>δ}|\hat g_T(τ)|^2\tfrac{dτ}{2π}
      = T∫_{|σ|>Tδ}\Big(\tfrac{σ^2}{T^2}+\tfrac14\Big)^2|\hatφ(σ)|^2\tfrac{dσ}{2π} ,

and since `\hatφ` is Schwartz the integral over `|σ| > Tδ` of
`(σ^2/T^2+1/4)^2|\hatφ(σ)|^2 ≤ (σ^2+1)^2|\hatφ(σ)|^2` (for `T ≥ 1`; **[REBUILT,
phase 131, round 6, minor `m3′`: round 5 wrote the majorant `σ^4+1`, which
**fails** once `σ^2/2 + 1/16 > 1`, i.e. `|σ| ≳ 1.4`.  `(σ^2+1)^2` is a correct
majorant for all `σ` and all `T ≥ 1`, since `σ^2/T^2 + 1/4 ≤ σ^2 + 1`; the
conclusion is untouched, `\hatφ` being Schwartz]**) tends to `0`
faster than any power of `T`; so `M_{tail}(T) = o(T^{-k})·T` for every `k`.
The same substitution over `|σ| ≤ Tδ` gives
`M_{bulk}(T) = T\big(\tfrac1{16}\|\hatφ\|_{L^2}^2/2π + o(1)\big) ≍ T`.
Hence `M_{tail}(T)/M_{bulk}(T) → 0`.

**Step 4 (conclusion).**  Using `ω̂_{fin} ≥ c` on `|τ| ≤ δ` and
`|ω̂_{fin}| ≤ A_S` everywhere,

    Q_{fin}(g_T) ≥ c\,M_{bulk}(T) − A_S\,M_{tail}(T)
                 = M_{bulk}(T)\Big(c − A_S\tfrac{M_{tail}(T)}{M_{bulk}(T)}\Big) ,

which is `> 0` for all `T` large enough.  Taking such a `T` gives the
theorem.  ∎  `PROVED`

**Remark 8bis.4b (the scope of Theorem 8bis.4a, stated exactly).**  **[REBUILT,
phase 131, round 5.]**  Three things must travel with it.

  1. *It is a **fixed-chart** statement,* and it is **not** claimed in the
     colimit.  The proof uses Plancherel against the **bounded** symbol
     `ω̂_{fin}` of a finite chart (8bis.8b).  In the colimit
     `ω̂_{fin}^{∞} = Σ_{\text{all }p}\hat W_p` is **not** a bounded function —
     indeed `ω̂_{fin}^{∞}(0) = Σ_p(\log p)2p^{−1/2}/(1−p^{−1/2}) = +∞` — so the
     Plancherel step does not transfer, and the two scales in the argument
     (the concentration width `≍ 1/T` of `\hat g_T` and the variation scale
     `≍ 1/\log p_{\max}` of the symbol) become comparable.  **The colimit
     version is therefore `OPEN`, and is not asserted.**
  2. *What it does settle.*  Any programme that hoped to obtain RH by proving
     `Q_{fin} ≤ 0` on the primitive sector **at a chart** is dead: the
     inequality is false there.  This is why (vi) names the Gram form of
     `Frob ⋆ Δ^{rad}` — the full kernel — and not the Frobenius Gram form.
  3. *What it does **not** settle.*  It does **not** refute the biconditional
     "`Q_{fin} ≤ 0` ⟺ RH" as a statement of logic: a biconditional between two
     propositions of fixed truth value can only be refuted by deciding one of
     them, and this paper decides neither RH nor anything about zeros.  What
     is proved is the **left-hand side is false** at every finite chart; the
     biconditional would then force RH to be false, which this paper does
     **not** claim, because (iii) — the statement it does use — is a **colimit**
     statement and (iv)(b) is a **chart** statement, and the two quantifiers
     are different.  This distinction is exactly the failure mode the auditor
     named, and it is why (vi) rests on (iii) alone.

### 8bis.4 The Dirichlet-polynomial converse: what closes and what does not

**[REBUILT, phase 131, round 4 — instruction `L3` of `R131.009`; REBUILT AGAIN
in round 5 after findings `M2`/`LF2` (the primitivization estimate and the
import were both wrong), `M3`/`LF1` (the partition-of-unity lemma was false for
a general bump), `M4` (the chart quantifier) and `m4`/`LF4` (an unlabelled
import inside a `PROVED` lemma); and REBUILT AGAIN in round 6 after `LF5`,
which found the import itself **false**.  **[REBUILT, phase 131, round 7,
finding `A3` of `R131.017`: this header still promised that the attempt
"closes modulo one named classical import".  `W23` retracted exactly that.]**
The attempt does **not** close.  What stands is a **conditional transfer
theorem**: its analytic machinery is proved here in full, and its arithmetic
input is isolated as the explicit hypothesis `(H_L)`, which is **`OPEN`**.  Nothing in clauses
B.1–B.9 depends on this subsection, and it is quarantined exactly as Paper 43
Theorem 10.8b is.]**

Throughout §8bis.4 the trace is the **colimit** trace `T_∞` on `D_A^∞` and
`W_{fin}` is the kernel over **all** primes, by (C1); this is not optional —
the windows `[L/2,L]` used below require every prime up to `e^{L}`.

**Lemma 8bis.5 (continuity of `T_∞` on a moving window).**  **[`CLASSICAL`
input: Chebyshev.  Findings `m4`, `LF4`.]**  Let `R ≥ 1` and let
`h ∈ C_c^∞(R)` be supported in `[−R,R]`.  Then

    |T_∞(Γ_h)| ≤ C_0‖h‖_∞ e^{R/2} + C_1‖h‖_{C^1} ,                    (8bis.11)

with `C_0, C_1` absolute constants.  In particular `h ↦ T_∞(Γ_h)` is bounded
by `O(e^{R/2})` on `{ h : supp h ⊆ [−R,R], ‖h‖_{C^1} ≤ 1 }`.

*Proof.*  By Theorem 3bis.7 and Definition–Theorem 3bis.8 read on `D_A^∞`
(Theorem 3bis.7's last paragraph),
`T_∞(Γ_h) = ∫h\,dW_{fin} + ∫h\,ω_∞ + (\text{identity term})`, all three finite.
The finite part is `Σ_k Λ(k)k^{−1/2}[h(\log k)+h(−\log k)]`, a sum over
`k ≤ e^{R}` bounded by `2‖h‖_∞ Σ_{k≤e^{R}}Λ(k)k^{−1/2}`.  By **Chebyshev's
bound** `ψ(X) := Σ_{k≤X}Λ(k) ≤ cX` with an absolute `c` (this is an external
classical input; it is named here and is used nowhere outside §8bis.4), partial
summation gives `Σ_{k≤X}Λ(k)k^{−1/2} ≤ C_0'X^{1/2}` with `C_0'` absolute,
whence the first term of (8bis.11).  **[REBUILT, phase 131, round 5, finding
`m4`: the round-4 display wrote the constant `4`, which requires `ψ(X) ≤ X`;
that inequality **fails for infinitely many `X`** (Littlewood), so the constant
is replaced by an unspecified absolute `C_0` and the import is labelled.]**
The archimedean part is (8.5∞): away from `t = 0`, `K` is integrable against a
bounded compactly supported function; near `t = 0`, `K(t) = 1/(2t)+O(1)` and
the bracket `h(t)+h(−t)−2h(0)e^{−t/2}` is `O(t‖h‖_{C^1})`, so that term is
`O(‖h‖_{C^1})`.  ∎  `CLASSICAL` (import: Chebyshev's bound; used by no clause
of B.1–B.9)

**Lemma 8bis.6 (Riemann-sum approximation on a moving window).**  **[REBUILT,
phase 131, round 5, finding `M3` of `R131.011` = `LF1` of `R131.012`.  The
round-4 lemma took an arbitrary `C^∞` bump `ρ` of **mass 1** and asserted
`Σ_n gap_nρ_{ε_n}(t−\log n) = 1 + O(e^{−L/2})`.  That is **false**: on a
uniform grid of spacing `s` with `ε = s` the sum is, by Poisson summation,
`Σ_kρ(x−k) = Σ_m \hatρ(2πm)e^{2πimx}`, which is not identically `1` for a
general mass-one `ρ` — for `ρ` supported in `[−0.1,0.1]` the sum **vanishes**
on most of the line.  The round-4 proof also conflated a *tested* estimate
(which is `O(Le^{−L/2})`, not `O(e^{−L/2})`) with the *pointwise* statement the
lemma needs.  Both are repaired: the bump is now a smooth **partition of
unity**, and the pointwise statement is proved by slow variation of the
gaps.]**

Fix once and for all a real `ρ ∈ C_c^∞([−1,1])` with

    Σ_{k∈Z} ρ(x−k) ≡ 1   for all x ∈ R                                (8bis.12a)

(a smooth partition of unity subordinate to the unit grid; such `ρ` exists, and
`∫ρ = 1` follows by integrating (8bis.12a) over a period).  Let `L ≥ 4` and let
`g ∈ C^1(R)` be supported in `[L/2, L]`.  For `n` with `\log n ∈ [L/2,L]` put
`gap_n := \log(n+1)−\log n = \log(1+1/n)`, so `e^{−L} ≤ gap_n ≤ 2e^{−L/2}`, and
set

    g_D(t) := Σ_{\log n ∈ [L/2,L]} g(\log n)\,ρ\Big(\frac{t−\log n}{gap_n}\Big) . (8bis.12)

Then `g_D` is a Dirichlet-polynomial profile with **per-`n`** widths
`ε_n = gap_n` (indeed `ρ((t−\log n)/gap_n) = gap_n·ρ_{ε_n}(t−\log n)` with
`ρ_ε := ε^{−1}ρ(·/ε)`), and

    ‖g − g_D‖_∞ ≤ C e^{−L/2} ‖g‖_{C^1} ,
    supp(g−g_D) ⊆ [L/2−1, L+1] ,                                      (8bis.13)

with `C` absolute.

*Proof.*  **Step 1 (the mesh sums to `1 + O(e^{−L/2})`, pointwise).**  Fix
`t ∈ [L/2,L]` and put `x := e^{t} ∈ [e^{L/2}, e^{L}]`.  For `n` with
`|t − \log n| ≤ gap_n` we have `|x/n − 1| ≤ e^{gap_n}−1 ≤ 2/n`, so
`|x − n| ≤ 2`.  For such `n`,

    t − \log n = \log(x/n) = \frac{x−n}{n}\Big(1 + O\big(\tfrac{|x−n|}{n}\big)\Big) ,
    gap_n = \log(1+1/n) = \frac1n\Big(1+O(1/n)\Big) ,

hence

    \frac{t−\log n}{gap_n} = (x−n)\big(1 + O(1/n)\big) .              (8bis.13a)

Therefore, with `K := ‖ρ'‖_∞` and using (8bis.12a) on the **uniform** grid,

    \Big|Σ_n ρ\Big(\frac{t−\log n}{gap_n}\Big) − Σ_n ρ(x−n)\Big|
      ≤ K\,Σ_{|x−n|≤2}|x−n|\,O(1/n) = O(K/n) = O\big(Ke^{−L/2}\big) ,

because at most five integers `n` satisfy `|x−n| ≤ 2` and each has
`n ≥ e^{L/2} − 2`.  With `Σ_nρ(x−n) = 1` this is

    Σ_{\log n ∈ [L/2,L]} ρ\Big(\frac{t−\log n}{gap_n}\Big) = 1 + O(e^{−L/2})  (8bis.13b)

for `t` in the interior of the window (at distance `≥ 2e^{−L/2}` from its
endpoints; near the two endpoints the sum lies in `[0,1]` and `g` vanishes
there up to `O(e^{−L/2}‖g‖_{C^1})`, which is absorbed).  **This is the
*pointwise* statement, and it is what the lemma needs; no tested estimate is
used.**

**Step 2 (the approximation).**  By (8bis.13b),

    g_D(t) − g(t) = Σ_n ρ\Big(\frac{t−\log n}{gap_n}\Big)\big[g(\log n) − g(t)\big]
                    + g(t)\cdot O(e^{−L/2}) ,

and on the support of the `n`-th term `|t − \log n| ≤ gap_n ≤ 2e^{−L/2}`, so
`|g(\log n) − g(t)| ≤ ‖g'‖_∞·2e^{−L/2}`.  Since at most five terms are nonzero
at any `t` and `0 ≤ ρ ≤ ‖ρ‖_∞`, the first sum is `O(e^{−L/2}‖g‖_{C^1})` and the
second is `O(e^{−L/2}‖g‖_∞)`.  The support statement is immediate from
`gap_n ≤ 1`.  ∎  `PROVED`

**Lemma 8bis.6a (`C^1` control of the Riemann-sum approximant).**  **[REBUILT,
phase 131, round 6, finding `N3` of `R131.014` = `LF6`(b) of `R131.015`.  Step 3
of Theorem 8bis.7 pairs two *rough* functions and therefore needs a derivative
bound, which round 5 did not have; the sentence "the derivative always falls on
the smooth factor" is true of one cross term and **false of the other**.]**  In
the notation of Lemma 8bis.6,

    ‖(g_D)'‖_∞ ≤ C\big(‖g‖_{C^1}\big) ,   hence
    ‖(g − g_D)'‖_∞ ≤ C‖g‖_{C^1} ,                                    (8bis.13g)

with `C` depending only on `ρ`.  **The bound is `O(1)`, not `o(1)`; that is all
Step 3 needs.**

*Proof.*  Write `a_n := (t−\log n)/gap_n`, so
`(g_D)'(t) = Σ_n g(\log n)\,ρ'(a_n)/gap_n`.  Split
`g(\log n) = g(t) + [g(\log n)−g(t)]`.

*The coefficient-variation part.*  On the support of the `n`-th term
`|t−\log n| ≤ gap_n`, so `|g(\log n)−g(t)| ≤ ‖g'‖_∞ gap_n`, and the term is
bounded by `‖g'‖_∞‖ρ'‖_∞`; at most five `n` contribute (Lemma 8bis.6, Step 1),
so this part is `O(‖g'‖_∞)`.

*The mesh part, where the cancellation lives.*  It is `g(t)·S(t)` with
`S(t) := Σ_nρ'(a_n)/gap_n`.  Put `x := e^{t}`.  By (8bis.13a),
`a_n = (x−n)(1+θ_n)` with `|θ_n| ≤ C/n`, and only `n` with `|x−n| ≤ 2`
contribute.  Taylor:

    Σ_n ρ'(a_n) = Σ_n ρ'(x−n) + Σ_n ρ''(ξ_n)\,(x−n)θ_n
                = 0 + O\big(‖ρ''‖_∞·C/n\big) = O(1/x) ,

where `Σ_nρ'(x−n) ≡ 0` because it is the derivative of the **partition of
unity** (8bis.12a), and at most five terms occur.  **This cancellation is the
whole point: without it the naive bound would be `‖ρ'‖_∞/gap_n ≍ e^{L}`.**
Finally `1/gap_n = n(1+O(1/n)) = x + O(1)`, so

    S(t) = Σ_nρ'(a_n)\,(x+O(1)) = x·O(1/x) + O\big(‖ρ'‖_∞\big) = O(1) .

Adding the two parts gives (8bis.13g).  ∎  `PROVED`

**Lemma 8bis.6b (the single-frequency test cannot witness a violation).**
**[REBUILT, phase 131, round 6, finding `LF5` of `R131.015`.  This is the
refutation of the round-4/round-5 import `(Wgr)`, and it is proved, not
asserted.]**  For `g ∈ C_c^∞(R)` write, in the `s`-dictionary of the explicit
formula,

    \hat g(s) := ∫_R g(t)\,e^{(s−\tfrac12)t}\,dt ,
    Q(g) := Σ_ρ \hat g(ρ)\,\overline{\hat g(1−\bar ρ)} ,              (8bis.14a)

the sum over the nontrivial zeros of `ζ` with multiplicity.  (`Q` is Hermitian:
`\overline{Q(f,g)} = Q(g,f)` after the involution `ρ ↦ 1−\bar ρ` of the zero
multiset.)  Let `ψ ∈ C_c^∞([1/2,1])` with `ψ ≥ 0`, `ψ ≢ 0`, let `γ_0 ∈ R`, and
put

    g_L(t) := ψ(t/L)\,e^{−iγ_0 t} .                                   (8bis.14b)

Suppose `ρ_0 = β + iγ_0` is a zero with `δ := β − \tfrac12 > 0`.  Then:

  (i) *every zero on the critical line contributes a non-negative amount*: for
      `ρ = \tfrac12+iγ` one has `1−\bar ρ = ρ`, so the term is
      `|\hat g_L(ρ)|^2 ≥ 0`;
  (ii) *the resonant off-line pair contributes a **positive** amount*: the two
      zeros `ρ_0` and `1−\bar ρ_0 = (1−β)+iγ_0` together contribute

        2\,\hat g_L(ρ_0)\,\hat g_L(1−\bar ρ_0) ,
        \hat g_L(ρ_0) = ∫ψ(t/L)e^{δ t}dt > 0 ,
        \hat g_L(1−\bar ρ_0) = ∫ψ(t/L)e^{−δ t}dt > 0 ,                (8bis.14c)

      **both factors being positive real numbers**, of sizes
      `\hat g_L(ρ_0) ≍_ψ e^{δL}` (dominated by the right end `t = L`) and
      `\hat g_L(1−\bar ρ_0) ≍_ψ e^{−δL/2}` (dominated by the **left** end
      `t = L/2`), **up to sub-exponential factors depending on `ψ`** — for a
      smooth `ψ` vanishing to infinite order at the endpoints, Laplace's method
      has a saddle at distance `≍ (δL)^{−1/2}` from the endpoint and
      contributes a factor `e^{−c\sqrt{δL}}`; so the pair contributes
      `≍ +\,e^{δL/2}` up to such factors.  **[REBUILT, phase 131, round 6: the
      first draft of this lemma said "up to factors polynomial in `L` and
      `1/δ`".  That is wrong, and my own numerics (block (H) of
      `verify_131_contacts.py`) found it: the endpoint flatness of a
      `C_c^∞` bump costs `e^{−c\sqrt{δL}}`, which is sub-exponential but not
      polynomial.  Nothing in (i)–(iv) depends on the polynomial factor; what
      matters is the **sign** and the exponent `δ/2` versus `(Wgr)`'s
      `2δ`.]**;
  (ii′) *the conjugate pair is of the same order, with unknown sign, and is
      bounded*: the quadruple of `ρ_0` also contains
      `\{\bar ρ_0,\ 1−ρ_0\}`, whose contribution is
      `2\,\mathrm{Re}\big[\hat g_L(\bar ρ_0)\overline{\hat g_L(1−ρ_0)}\big]`
      with `\hat g_L(\bar ρ_0) = ∫ψ(t/L)e^{δt}e^{−2iγ_0t}dt` and
      `\hat g_L(1−ρ_0) = ∫ψ(t/L)e^{−δt}e^{−2iγ_0t}dt`.  These are oscillatory
      and their **sign is not determined here**, but trivially
      `|\hat g_L(\bar ρ_0)| ≤ \hat g_L(ρ_0)` and
      `|\hat g_L(1−ρ_0)| ≤ \hat g_L(1−\bar ρ_0)`, so the mismatched pair is
      `O\big(\hat g_L(ρ_0)\hat g_L(1−\bar ρ_0)\big)` — the **same** order
      `e^{δL/2}` as the resonant pair, and no larger.  **[REBUILT, phase 131,
      round 7, minor `p1` of `R131.017`: round 6 wrote "quadruple" while
      estimating only the resonant **pair**, and asserted without proof (as did
      the audit) that the mismatched pair is negligible.  It is **not** proved
      negligible — non-stationary phase with a *fixed* `γ_0` gains only a
      constant per integration by parts — but it **is** bounded by the same
      order, which is all the refutation needs.]**;
  (iii) *consequently `(Wgr)` is false in its modulus claim, and its stated
      mechanism is refuted*.  Precisely: by (ii) and (ii′) the whole resonant
      quadruple is `O(e^{δL/2})` up to sub-exponential factors, whereas
      `(Wgr)` asserted a modulus `≍ L^2e^{2δL}`; since `2δ > δ/2` for `δ > 0`,
      **the modulus claim is refuted outright** (`PROVED`).  As for the sign:
      the term `(Wgr)` relied on — the resonant pair — is **positive**, so its
      mechanism is refuted; the sign of the full sum is not decided here and is
      not claimed.  No contradiction with `I_∂ ≤ 0` follows from a
      single-frequency test;
  (iv) *and the failure is structural, not a matter of choosing `ψ`*: for any
      `g(t) = w(t)e^{−iγ_0t}` with `w ≥ 0`,

        \hat g(ρ_0) = ∫w\,e^{δt}dt ≥ ∫w\,e^{−δt}dt = \hat g(1−\bar ρ_0) > 0 ,

      so a **non-negative** amplitude can never make `\hat g` peak at
      `1−\bar ρ_0` rather than at `ρ_0`; more generally, for any real tilt
      `w(t) = ψ(t/L)e^{αt}` the two exponents are `α+δ` and `α−δ`, and
      `α+δ > α−δ` always.  Peaking at `1−\bar ρ_0` therefore requires
      **cancellation** in `∫w e^{δt}dt`, i.e. an amplitude that changes sign or
      phase — which is exactly what Weil's two-frequency construction does, and
      what destroys the sup-norm control needed by Step 3 below;
  (v) *and the conclusion survives primitivization, which is the form §8bis.4
      actually uses*.  **[REBUILT, phase 131, round 7, minor `p2` of
      `R131.017`.]**  `\widehat{Πg}(s) = s(1−s)\hat g(s)`.  Put
      `A := ρ_0(1−ρ_0) = \tfrac14 − (δ+iγ_0)^2`; then at the second resonant
      point `s = 1−\bar ρ_0` the factor is
      `(1−\bar ρ_0)\bar ρ_0 = \overline{A}`, so

        \widehat{Πg_L}(ρ_0)\,\overline{\widehat{Πg_L}(1−\bar ρ_0)} + c.c.
          = 2\,\mathrm{Re}\big(A^2\big)\;\hat g_L(ρ_0)\,\hat g_L(1−\bar ρ_0) ,

      and with `A = \tfrac14 − δ^2 + γ_0^2 − 2iδγ_0`,

        \mathrm{Re}(A^2) = \big(\tfrac14−δ^2+γ_0^2\big)^2 − 4δ^2γ_0^2 > 0
        \quad\text{whenever } |γ_0| > 2δ ,

      in particular for every `|γ_0| ≥ 1` (and a fortiori for every nontrivial
      zero of `ζ`, all of which have `|γ| > 14`), since
      `(\tfrac14−δ^2+γ_0^2)^2 − 4δ^2γ_0^2 = (\tfrac14−δ^2+γ_0^2−2δ|γ_0|)
      (\tfrac14−δ^2+γ_0^2+2δ|γ_0|)` and the first factor is
      `(\,|γ_0|−δ)^2 + \tfrac14 − 2δ^2 > 0` for `|γ_0| > 2δ` with
      `0 < δ < \tfrac12`.  So the resonant pair of the **primitivized** test is
      again **positive**, and Lemma 8bis.6b applies to the class §8bis.4
      actually quantifies over.
      **[Correction to the round-7 instruction, reported in `R131.018` §4: the
      instruction states that the pair term "becomes `2|ρ_0(1−ρ_0)|^2
      \hat g(ρ_0)\hat g(1−\bar ρ_0)`".  That is **wrong**: the two factors are
      `A` and `\overline{A}`, and conjugating the second in the Hermitian
      pairing gives `A·A = A^2`, not `A\overline{A} = |A|^2`.  The correct
      coefficient is `2\,\mathrm{Re}(A^2)`, which is positive under the stated
      condition but is **not** `2|A|^2` and is **not** positive for all
      `γ_0`.]**

*Proof.*  (i) is `1−\bar ρ = ρ` on the line.  (ii): substituting (8bis.14b)
into (8bis.14a), at `s = ρ_0 = \tfrac12+δ+iγ_0` the exponential is
`e^{−iγ_0t}e^{(δ+iγ_0)t} = e^{δt}`, and at `s = 1−\bar ρ_0 =
\tfrac12−δ+iγ_0` it is `e^{−δt}`; both integrals have non-negative integrand,
hence are positive reals, and the pair `\{ρ_0, 1−\bar ρ_0\}` contributes
`\hat g(ρ_0)\overline{\hat g(1−\bar ρ_0)} + \hat g(1−\bar ρ_0)\overline{\hat
g(ρ_0)} = 2\hat g(ρ_0)\hat g(1−\bar ρ_0) > 0`.  The sizes are Laplace's method
on `[L/2,L]`: for `δ > 0` the weight `e^{δt}` is maximal at `t = L` and
`e^{−δt}` at `t = L/2`.  (iii) restates (ii).  (iv) is the monotonicity of
`α ↦ α` and the displayed inequality `e^{δt} ≥ e^{−δt}` for `t > 0`.  ∎
`PROVED` (given the classical zero-sum framework of Theorem 8bis.4(ii), which
is the only external input)

**Theorem 8bis.7 (the converse, as a CONDITIONAL transfer theorem).**
**[REBUILT, phase 131, round 6.  The round-4/5 version asserted an import
`(Wgr)` which Lemma 8bis.6b now **refutes**; the theorem is therefore restated
as a **conditional** transfer, whose analytic machinery (Lemmas 8bis.5, 8bis.6,
8bis.6a and Steps 1–3 below) is proved here in full, and whose arithmetic
hypothesis is isolated, named, and recorded as `OPEN`.  Withdrawal: §9bis
W23.]**

For `L ≥ 4` consider the hypothesis

> **(H_L)**  *there is a **primitive** `g_* ∈ C_c^∞([L/2,L];C)` — i.e.
> `\hat g_*(0) = \hat g_*(1) = 0` — with `Q(g_*) < 0` and*
>
>     R(L) := \frac{L\,e^{−L/4}\,‖g_*‖_∞‖g_*‖_{C^1}
>                    \;+\; L\,e^{−L/2}\,‖g_*‖_{C^1}^2}{|Q(g_*)|} .   (8bis.14d)

**[REBUILT, phase 131, round 7, finding `A5` of `R131.017`: the round-6 ratio
was built from the **first** term of (8bis.13i) only, while that display has
**two**; round 6 covered the second by a side condition asserted in Step 4 and
**not** contained in `(H_L)` — the phase's standing failure mode.  `R(L)` now
covers **both** terms, and the side condition is deleted.  Everything
downstream is unchanged, since the first term dominates on the natural sizes
(`‖g_*‖_{C^1} ≤ e^{L/4}‖g_*‖_∞`).]**

Then:

  (a) *(`PROVED` here — the transfer.)*  If `(H_L)` holds for arbitrarily large
      `L` with `R(L) → 0` along that sequence, then `I_∂ ≤ 0` **fails** on the
      class of primitive Dirichlet-polynomial profiles with per-`n` widths
      (8bis.12); equivalently, positivity on that class implies that no such
      family `(g_*)` exists.
  (b) *(`CLASSICAL` for Weil's criterion, Theorem 8bis.4(iii);
      **`PROVED-IN-REPOSITORY`** for the passage to the primitive class,
      Paper 45 Theorem 10.4.)*  If RH fails then `Q(g) < 0` for **some**
      `g ∈ C_c^∞(R)` — this is Weil's criterion, `CLASSICAL` — and — by
      Paper 45 Theorem 10.4, which supplies `Π = −∂_t^2+\tfrac14` and
      **proves in the repository** that the primitive class suffices — for
      some **primitive** `g`.
      **[phase 133, PANEL_2 MINOR-6: (b) was labelled `CLASSICAL` wholesale,
      via Theorem 8bis.4(ii)–(iii).  The primitive-class half is a theorem of
      this repository (Paper 45 Thm 10.4, from `106_11` Theorem 1 with the
      `C10` fix and imports (E2) last clause, (E3d), (E6)), and 8bis.4(ii) —
      the explicit formula — is itself `PROVED-IN-REPOSITORY` since phase 132
      (Paper 45 Thm 9.4).  Weil's **criterion** stays `CLASSICAL`.  The
      relabel is toward less external dependence; no verdict moves, and (c)
      and the overall `OPEN` of Theorem 8bis.7 are untouched.]**
  (c) *(`OPEN`.)*  Whether such a `g` can be taken **supported in a moving
      window `[L/2,L]` with `L → ∞`** and with `R(L) → 0` is **not** supplied
      by any classical statement known to this paper, and is **not** asserted.
      Remark 8bis.7a(2) records what is known about the obstruction and by how
      much the natural candidates miss.

Consequently the implication *"positivity on Dirichlet-polynomial profiles
⟹ RH"* is **`OPEN`**, and is not claimed.

*Proof of (a).*  Let `g_* = g_*^{(L)}` satisfy `(H_L)`; write `\tilde g := g_*`.

**Step 1 (approximate).**  Let `g_D` be the Riemann-sum profile (8bis.12) of
`\tilde g` and `e := \tilde g − g_D`.  Lemma 8bis.6 and Lemma 8bis.6a give

    ‖e‖_∞ ≤ C\,e^{−L/2}‖\tilde g‖_{C^1} ,   ‖e'‖_∞ ≤ C‖\tilde g‖_{C^1} ,
    supp\,e ⊆ [L/2−1,\ L+1] .                                        (8bis.13c)

**Step 2 (primitivize the approximant).**  **[REBUILT, phase 131, round 7,
finding `A4` of `R131.017`: round 6 condensed this step and **deleted** the
displays (8bis.13c), (8bis.13d), (8bis.13e) while keeping the pointers to them,
recreating the dangling-reference defect it had been written to repair.  The
three displays are restored here with their tags; their values are unchanged
and were verified by the auditor.]**  Let `η ∈ C_c^∞` be a smooth cutoff,
`η ≡ 1` on `[L/2+1, L−1]`, `supp\,η ⊆ [L/2,L]`, `0 ≤ η ≤ 1`, and let
`w_1, w_2` be the Riemann-sum profiles (8bis.12) of `u_1(s) := e^{s/2}η(s)` and
`u_2(s) := e^{−s/2}η(s)`.  These are Dirichlet-polynomial profiles, and by
Lemma 8bis.6 `‖w_i − u_i‖_∞ = O(e^{−L/2}‖u_i‖_{C^1})`, so

    ‖w_1‖_∞ ≍ e^{L/2} ,                    ‖w_2‖_∞ ≍ e^{−L/4} ,
    λ_−(w_1) = ∫w_1e^{s/2}ds ≍ e^{L} ,     λ_+(w_1) = ∫w_1e^{−s/2}ds ≍ L ,
    λ_−(w_2) ≍ L ,                          λ_+(w_2) ≍ e^{−L/2} ,     (8bis.13d)

all four from `∫_{L/2}^{L}e^{s}ds ≍ e^{L}`, `∫_{L/2}^{L}η ≍ L`,
`∫_{L/2}^{L}e^{−s}ds ≍ e^{−L/2}`, the `O(e^{−L/2})` approximation errors being
of lower order; the determinant of the `2×2` system below is
`λ_−(w_1)λ_+(w_2) − λ_−(w_2)λ_+(w_1) ≍ e^{L}e^{−L/2} − L\cdot L ≍ e^{L/2}`.
The mismatches of `e` are, by (8bis.13c),

    |λ_−(e)| ≤ ‖e‖_∞∫_{L/2−1}^{L+1}e^{s/2}ds = O\big(‖\tilde g‖_{C^1}\big) ,
    |λ_+(e)| ≤ ‖e‖_∞∫_{L/2−1}^{L+1}e^{−s/2}ds
             = O\big(e^{−3L/4}‖\tilde g‖_{C^1}\big) .                (8bis.13e)

Solving `λ_∓(e + a w_1 + b w_2) = 0` by Cramer gives

    a = O\big(e^{−L}‖\tilde g‖_{C^1}\big) ,
    b = O\big(e^{−L/4}‖\tilde g‖_{C^1}\big) ,                         (8bis.13e′)

**[REBUILT, phase 131, round 6, finding `LF6`(a) of `R131.015` and minor `m1′`
of `R131.014`: round 5 evaluated `b = O(Le^{−L/2})`, dropping the larger of the
two Cramer terms.  The correct order is
`b ≍ λ_+(e)λ_−(w_1)/\det ≍ e^{−3L/4}e^{L}/e^{L/2} = e^{−L/4}`, which dominates
`λ_−(e)λ_+(w_1)/\det ≍ Le^{−L/2}`.  The **sup norm is unchanged**:
`‖b\,w_2‖_∞ ≍ e^{−L/4}·e^{−L/4} = e^{−L/2}`, so (8bis.13f) stands verbatim and
Step 3's input is unaffected.]**  Hence

    ‖a w_1 + b w_2‖_∞ = O\big(e^{−L/2}‖\tilde g‖_{C^1}\big) ,
    ‖(a w_1 + b w_2)'‖_∞ = O\big(‖\tilde g‖_{C^1}\big) ,              (8bis.13f)

the second by Lemma 8bis.6a applied to `u_1,u_2` together with
`|a|‖u_1‖_{C^1} ≍ e^{−L}·e^{L/2} = e^{−L/2}` and `|b|‖u_2‖_{C^1} ≍
e^{−L/4}e^{−L/4} = e^{−L/2}`.  Put `g_D' := g_D + a w_1 + b w_2`, a **primitive**
Dirichlet-polynomial profile, and `ẽ := \tilde g − g_D'`, so

    ‖ẽ‖_∞ = O\big(e^{−L/2}‖\tilde g‖_{C^1}\big) ,
    ‖ẽ‖_{C^1} = O\big(‖\tilde g‖_{C^1}\big) .                         (8bis.13f′)

**Step 3 (the error is negligible).**  **[REBUILT, phase 131, round 6, finding
`N3`: the expansion is chosen so that **only `\tilde g` and `ẽ` occur**, and the
rough–rough term is bounded with Lemma 8bis.6a.]**  Write
`I(u,v) := I_∞(Γ_u,Γ_v)`.  Since `g_D' = \tilde g − ẽ`,

    I(\tilde g,\tilde g) − I(g_D',g_D') = I(ẽ,\tilde g) + I(\tilde g,ẽ)
                                          − I(ẽ,ẽ) ,                  (8bis.13h)

an identity in which no pairing involves `g_D'`.  Each term is
`T_∞(Γ_{u⋆v^†})` with `u⋆v^†` supported in `[−L/2−2, L/2+2]`, so Lemma 8bis.5
applies with `R = L/2+2`.  By Young, with the derivative falling on the
**smooth** factor in the two mixed terms and on `ẽ` in the last,

    ‖ẽ⋆\tilde g^†‖_∞    ≤ ‖ẽ‖_∞‖\tilde g‖_1 ,
    ‖ẽ⋆\tilde g^†‖_{C^1} ≤ ‖ẽ‖_∞‖\tilde g'‖_1 ,
    ‖ẽ⋆ẽ^†‖_∞          ≤ ‖ẽ‖_∞‖ẽ‖_1 ≤ 2L‖ẽ‖_∞^2 ,
    ‖ẽ⋆ẽ^†‖_{C^1}      ≤ ‖ẽ'‖_∞‖ẽ‖_1 ≤ 2L‖ẽ'‖_∞‖ẽ‖_∞ .

Using `‖\tilde g‖_1 ≤ L‖\tilde g‖_∞`, `‖\tilde g'‖_1 ≤ L‖\tilde g‖_{C^1}` and
(8bis.13f′), Lemma 8bis.5 gives

    |I(ẽ,\tilde g)| + |I(\tilde g,ẽ)|
      = O\big(e^{L/4}·e^{−L/2}‖\tilde g‖_{C^1}·L‖\tilde g‖_∞\big)
        + O\big(e^{−L/2}L‖\tilde g‖_{C^1}^2\big) ,
    |I(ẽ,ẽ)| = O\big(e^{L/4}Le^{−L}‖\tilde g‖_{C^1}^2\big)
               + O\big(Le^{−L/2}‖\tilde g‖_{C^1}^2\big) ,

so that, absorbing the smaller terms,

    \big|\,I(\tilde g,\tilde g) − I(g_D',g_D')\,\big|
       = O\Big(L\,e^{−L/4}\,‖\tilde g‖_∞‖\tilde g‖_{C^1}\Big)
         + O\Big(L\,e^{−L/2}‖\tilde g‖_{C^1}^2\Big) .                 (8bis.13i)

**Step 4 (conclude).**  On the primitive sector the Tate/polar packet vanishes
(Theorem 8bis.4(ii); Paper 45 Theorem 8.1).  **With the sign convention fixed
once in Theorem 8bis.4(ii)** — the explicit formula written with the zero sum on
the spectral side — this gives, **without hedge**,

    I_∂(Γ_u,Γ_u) = −Q(u)  \qquad for every primitive u .              (8bis.14e)

**[REBUILT, phase 131, round 7, minor `p7` of `R131.017`: round 6 wrote
"`I_∂(Γ_u,Γ_u) = −Q(u)` **up to the fixed sign convention** of
Theorem 8bis.4(ii)".  A step whose entire conclusion is a sign may not contain
that phrase; the convention is fixed in 8bis.4(ii) and is cited here without
qualification.]**  By `(H_L)`, `−Q(\tilde g) > 0`
with `|Q(\tilde g)|` exceeding **the whole** of (8bis.13i) by the factor
`1/R(L) → ∞`, since `R(L)` of (8bis.14d) is built from **both** error terms.
Hence
`I_∂(Γ_{g_D'},Γ_{g_D'}) > 0` for all large `L` in the sequence, and `g_D'` is a
primitive Dirichlet-polynomial profile with per-`n` widths.  That is the failure
of `I_∂ ≤ 0` on the class.

**Complex profiles.**  **[REBUILT, phase 131, round 6, minor `m4′` of
`R131.014`: the reduction is now carried out, not merely invoked.]**  `g_*` and
`g_D'` are complex.  The functionals `λ_∓(Γ_g) = ∫g(s)e^{±s/2}ds` are
`R`-linear with **real** kernels, so `λ_∓(g_D') = 0` gives
`λ_∓(\mathrm{Re}\,g_D') = λ_∓(\mathrm{Im}\,g_D') = 0`: **both real and imaginary
parts are primitive**.  Both are again Dirichlet-polynomial profiles with the
same per-`n` widths and real coefficients `\mathrm{Re}\,c_n`,
`\mathrm{Im}\,c_n`.  By (8bis.8c),
`I(g_D',g_D') = I(\mathrm{Re}\,g_D',\mathrm{Re}\,g_D') +
I(\mathrm{Im}\,g_D',\mathrm{Im}\,g_D')`, so `I(g_D',g_D') > 0` forces one of the
two **real** summands to be `> 0`.  Only then does the conclusion contradict a
hypothesis quantified over **real** profiles, as Definition 8bis.3 quantifies
it.  ∎  `PROVED` for (a); `CLASSICAL` for (b); `OPEN` for (c)

**Remark 8bis.7a (exactly what this settles, and what fails).**

  1. **The imports.**  Only two survive: Weil's criterion/explicit formula
     (Theorem 8bis.4(ii)–(iii)) and Chebyshev (Lemma 8bis.5).  The round-4/5
     import `(Wgr)` is **withdrawn as false** (Lemma 8bis.6b, §9bis W23) and is
     cited nowhere.  **[phase 132]** The **explicit-formula half** of this import is `PROVED-IN-REPOSITORY` since phase 132 (Paper 45 Thm 9.4); what remains `CLASSICAL` here is Weil's **criterion**, Thm 8bis.4(iii).  With that, the survivors are
     Weil's **criterion** (`CLASSICAL`) and Chebyshev (`CLASSICAL`); both are
     named in §11, **count toward no clause of B**, and are used by no theorem
     outside §8bis; deleting §8bis.3–§8bis.4 changes no verdict.
  2. **What fails, and by how much.**  Theorem 8bis.7(c) is the gap, and it has
     two distinct parts.
     *(α) The single-frequency route is dead, provably.*  Lemma 8bis.6b(ii)
     shows the resonant quadruple contributes `+e^{δL/2}` (positive, and with
     half the exponent `(Wgr)` claimed).  No choice of `ψ ≥ 0` repairs it, by
     (iv).
     *(β) The two-frequency route is not controlled.*  Weil's actual argument
     uses `g = g_1 + c\,g_2` with `\hat g_1` peaked at `ρ_0`, `\hat g_2` peaked
     at `1−\bar ρ_0`, and extracts negativity from the **off-diagonal** term
     `2\,\mathrm{Re}[\bar c\,B(g_1,g_2)]` of the indefinite Hermitian form `B`,
     choosing the phase and modulus of `c`; negativity requires
     `|B(g_1,g_2)|^2 > Q(g_1)\,Q(g_2)`.  Two obstacles, both quantified.
     First, by Lemma 8bis.6b(iv) the peaking of `\hat g_2` at `1−\bar ρ_0`
     **cannot** be produced by a non-negative amplitude or a real tilt: it needs
     cancellation of order `e^{δL}` in `∫w e^{δt}dt`, so `‖g_2‖_∞` exceeds
     `|\hat g_2(1−\bar ρ_0)|` by a factor that no classical statement bounds.
     Second, the ratio (8bis.14d) is **scale-invariant in `g_*`** but
     **quadratic** in it, so a witness whose amplitude carries a weight
     `e^{αt}` on `[L/2,L]` has `‖g_*‖_∞‖g_*‖_{C^1} ≳ e^{2αL}`, while the only
     lower bound available for `|Q(g_*)|` is `|c|` times the cross term, which
     is polynomial in `L` times `e^{δL}`-type factors.  The ratio `R(L)` then
     closes only if `2α < δ + \tfrac14`.  **[REBUILT, phase 131, round 7,
     minor `p3` of `R131.017`: this is an **indicative threshold on the natural
     sizes, not a theorem**.  Its denominator is "polynomial in `L` times
     `e^{δL}`-type factors" — an assumed order of magnitude for a witness that
     does not yet exist — so the inequality records *where the natural
     candidates miss*, and nothing more.  Round 6's description of it as
     "quantified" is withdrawn.]**  The inequality is not delivered by the
     construction and is not assumed here.  **If a witness with
     `R(L) → 0` is exhibited for all `β`, Theorem 8bis.7(a) upgrades the
     implication to a theorem; if only for `|β−\tfrac12| < θ`, it does so for
     that range.  Neither is claimed here.**
  3. **The Frobenius family is not reached.**  Theorem 8bis.7 is about the
     **radial** classes `Γ_g` (full Weil kernel, colimit).  By Theorem 8bis.4a
     the pure Frobenius form `Q_{fin}` is not `≤ 0` on the primitive sector at
     any finite chart, so no statement about its sign can be the hypothesis of
     a theorem like this one.
  4. **No sign is claimed.**  Theorem 8bis.7(a) is an implication whose
     hypothesis is **not** asserted anywhere in this paper, and Paper 43
     Theorem 14.1 shows the unrestricted form is indefinite.
  5. **Chart.**  The whole subsection is a `T_∞`/`D_A^∞` statement (C1).  At a
     fixed finite chart neither Lemma 8bis.5 nor Theorem 8bis.7 is asserted.
  6. **What round 6 actually gained.**  A false `CLASSICAL` import is gone; the
     transfer machinery — Lemmas 8bis.5, 8bis.6, 8bis.6a, Steps 1–3, including
     the `C^1` control that round 5 lacked — is **proved**; and the arithmetic
     input is reduced to the single explicit, checkable hypothesis `(H_L)`.
     That is a strictly better position than a theorem resting on a false
     citation.

### 8bis.5 The shell normalization is forced by the Tate residue

**[REBUILT, phase 131, round 4 — instruction `L1` of `R131.009`, answering
reservation `R4` and adversarial finding `F7`.  Round 2 conceded that
`vol_{d^*x}(Z_p^×) = \log p` is a *declared* normalization of row A.  It is
not arbitrary: it is the **unique** local normalization for which the Tate
residue is the same at every place.]**

**Theorem 8bis.8 (uniqueness of the shell normalization, up to a global
scale).**  **[REBUILT, phase 131, round 5, note `n1`: the statement now
carries the scale quotient it always had.  The theorem fixes `c_p` **relative
to the declared archimedean measure** (8.5b); rescaling *all* local measures by
one `λ > 0` gives `c_p = λ\log p` and `λ·(dx/2|x|)` at `∞`, and changes no
sign, no vanishing and no ratio.  Read: the normalization is unique **in the
quotient by the global scale**.]**  Let the local multiplicative measures be
declared by

    vol_{d^*x_p}(Z_p^×) = c_p > 0   (p finite),    d^*x_∞ = dx/(2|x|) ,

all other conventions of Paper 43 §8.2 unchanged.  Define the **local Tate
residue** of a place `v` as the residue at `s = 0` of the local zeta integral
`ζ_v(s) := ∫_{|x|_v ≤ 1}|x|_v^{s} d^*x_v`.  Then:

  (i) `ζ_p(s) = c_p/(1−p^{−s})`, a simple pole at `s=0` of residue
      `c_p/\log p`;
  (ii) `ζ_∞(s) = 1/s`, residue `1`;
  (iii) hence **the local Tate residues agree at all places if and only if
      `c_p = \log p` for every finite `p`**;
  (iv) the same conclusion in the symbol: with `vol(Z_p^×) = c_p`, Paper 43
      (9.11) reads `Ŵ_p(𝔠_0,τ) = c_p · 2 Re( ζ_p/(1−ζ_p) )` with
      `ζ_p = p^{−1/2−iτ}` up to the constant phase `θ_p`, and the
      Mittag–Leffler form of Paper 43 Theorem 9.7b(a) is multiplied throughout
      by `c_p/\log p`; so

        Res_{τ=i/2} Ŵ_p = −i·(c_p/\log p) ,   Res_{τ=i/2} Ŵ_∞ = −i , (8bis.14)

      the second by Paper 43 Theorem 9.7b(b), and the two agree iff
      `c_p = \log p`.

*Proof.*  (i) `{|x|_p ≤ 1} = ⨆_{k≥0} p^kZ_p^×`, and `|x|_p^{s} = p^{−ks}` on
the `k`-th shell, whose `d^*x_p`-volume is `c_p` by translation invariance of
`d^*x_p`.  So `ζ_p(s) = c_p Σ_{k≥0}p^{−ks} = c_p/(1−p^{−s})` for `Re s > 0`,
meromorphic, and `1−p^{−s} = s\log p + O(s^2)` gives residue `c_p/\log p`.
(ii) `∫_{|x|≤1}|x|^{s}dx/(2|x|) = 2·(1/2)∫_0^1 x^{s−1}dx = 1/s`.
(iii) is (i)+(ii).
(iv) Paper 43 (9.11) obtains `Ŵ_p` on the principal component as
`Σ_{k≠0} vol(p^kZ_p^×)·p^{−|k|/2}η_p^{k}`; the volume enters as an overall
factor, so replacing `\log p` by `c_p` multiplies the whole function — and
hence every residue of its Mittag–Leffler form (Theorem 9.7b(a)) — by
`c_p/\log p`.  ∎  `PROVED`

**Corollary 8bis.8a.**  Under the requirement of a **universal Tate residue**
— one and the same residue at every place of `S` — the normalization
`vol_{d^*x}(Z_p^×) = \log p` is **unique**, and Corollary 3ter.11 then reads

    Λ(p^k) = \log p = vol_{d^*x}( supp Frob_{p^k} ) :

the Haar volume of the support of the Frobenius object **in the unique local
normalization compatible with the Tate boundary**.  The only remaining freedom
is an overall positive scale on `T`, which rescales `I_A` and changes no sign,
no vanishing and no ratio.  ∎  `PROVED` (Theorem 8bis.8).

**Remark 8bis.8b (what does NOT force it: chart-invariance — stated exactly,
as instructed).**  **[REBUILT, phase 131, round 4.]**  It is natural to hope
that chart-invariance of the ruling pairing forces `c_p = \log p` with no
extra requirement.  **It does not, and here is why.**  Paper 43
Theorem 9.7b(c) computes the **total** Tate residue of `T̂_S` as
`∓i(|S_f|+1)` — one `∓i` per place of `S`.  That number is **manifestly
chart-dependent**: it changes when a place is added.  The colimit trace `T_∞`
of Theorem 8A.7c is chart-invariant on tests of radius `< \log ℓ_{next}(S)`
(Theorem 8A.7c(e)), but a residue is read off the **symbol**, not off values
on a compact window, and no statement of Paper 43 makes the total residue
chart-independent.  Consequently:

  * **an argument "chart-invariance ⇒ equal residues" is not available**, and
    none is given here;
  * what **is** available is Theorem 8bis.8: given the *requirement* that
    every place carry the **same** Tate residue — which is exactly what makes
    `∓i(|S_f|+1)` a *count of places* rather than a normalization-dependent
    number, and what makes `λ_±` "the universal residues of the symbol" in the
    sense of Paper 43 Theorem 9.7b(c) — the normalization is unique.

So Theorem 8bis.8 is a **uniqueness theorem given a named requirement**
(universality of the Tate residue per place), **not** a derivation from
chart-invariance.  The requirement is named, and it is the one Paper 43
already uses when it reads the total residue as `|S_f|+1`.  *`CLASSICAL`
context, cited for orientation only and used nowhere:* this is Weil's
normalization of the local multiplicative measures in "Sur les formules
explicites".

**Remark 8bis.8c (the equivocation of `F7`, removed).**  `Frob_{p^k}` is the
**probability** Haar measure of the stratum `j_p(p^kZ_p^×)` (total mass `1`),
while `Λ(p^k) = \log p` is the **`d^*x`-volume** of that same set.  These are
two different measures on one set, related by the scalar `c_p = \log p`; the
contact (3ter.11) is `(d^*x`-volume of the support`) × (`half-density`)`, and
the probability normalization of `Frob_{p^k}` is what makes the object a
correspondence of mass one — a *class* — rather than a weighted one.  Both
statements are used; neither is conflated.


---

## 9. What row B hands to row C

**[REBUILT, phase 131 — this section is rewritten.  Its former §9.2 handed row
C an obligation which does not exist; the withdrawal is recorded in §9bis.]**

**9.1 The prime packet is a theorem of row B.**  Let `h ∈ C_c^∞(R)` with
`0 ∉ supp h`, and let `Γ_h ∈ D_A^{rad}` be the smeared norm class (3bis.6).
Then, by Theorem 3bis.7 with `c := 0`,

    T(Γ_h) = Σ_{p∈S_f}Σ_{k≥1}(\log p)p^{−k/2}[h(k\log p)+h(−k\log p)]
             + ∫_R K(|t|)h(t)\,dt ,                                    (9.1)

a finite sum plus a convergent integral, with no regularization and no
counterterm; on the colimit `D_A^∞` with `T_∞` (Paper 43 Thm. 8A.7c) the
restriction `p ∈ S_f` disappears.  So the finite-place radial packet of the
explicit formula is **the value of row A's declared trace on row B's
arithmetic family**, not an analogy with it, and the two terms `h(±\log n)`
are `Γ_n^{rad}` and `(Γ_n^{rad})^†` by Theorem 3bis.5(ii).  `PROVED` here
(Theorem 3bis.7).

What row B does **not** claim, and what remains a row C obligation unchanged
by this paper, is that `h ↦ A_h(r)` is an integrated representation: point
evaluations `w_n(h)` do not by themselves preserve convolution (P123.039 §5).
`OPEN (row C)`.  Note that the **smeared** classes do compose correctly here —
`Γ_h ⋆ Γ_g = Γ_{h∗g}` (Lemma 3bis.6a) — so the obligation concerns the
passage to point evaluations, not the algebra.

**9.2 The archimedean density, handed over.**  **[REBUILT, phase 131; this
replaces the former §9.2 entirely.  Round 2, finding `F6`: it is a *density*,
not a contact, and it is not called one.]**  The second item row B hands to
row C is the archimedean half of (9.1).  By Definition–Theorem 3bis.8,

    ω_∞(\log n) = K(\log n) = \tfrac12[τ_∞(1/n)+τ_∞(−1/n)]
                         = n^{3/2}/(n^2−1) = n^{−1/2}Σ_{j≥0}n^{−2j} ,  (9.2)

the value at the label `\log n` of the **continuous density** of `ω_∞`.  It is
positive for every `n`, composite or not; **nothing about the object
`Γ_n^{rad}` enters it** — the radial family has no archimedean atom — and it
is not part of `Λ(n)` (Remark 3bis.8a).  Row C's explicit formula
carries exactly `∫K(|t|)h(t)dt` as its archimedean term, and (9.2) is that
term's value at `t = \log n`.  This is the accounting phase-128 finding `B6`
asked for.  **No statement about zeros — trivial or otherwise — is made here**;
the expansion `n^{−1/2}Σ_{j≥0}n^{−2j}` is a geometric series and nothing more.

**9.1a What row C did with it.**  **[phase 132]**  Row C received §9.1 as
Paper 45 **Theorem 5.1** (and, for the case `0 ∈ supp h` that §9.1 excludes,
Paper 45 **Lemma 5.1a**) and convention **(C1)** as its standing chart
quantifier; and the explicit-formula import of Theorem 8bis.4(ii) is now
Paper 45 **Theorem 9.4**, proved in the repository.

**9.3 The identification `Λ = shell volume`, handed over.**  Row C may use, as
a theorem of row B on Paper 43's carrier,

    Λ(p^k) = \log p = vol_{d^*x}(p^kZ_p^×) ,   Λ(n) = 0 for composite n,

and its consequence `Σ_{d|n}Λ(d) = \log n = \log[L_S:nL_S]`
(Theorem 3bis.10).  This is what makes row C's geometric side a statement
about the carrier rather than a quotation of the von Mangoldt function.

**9.3a The contact locus, handed over.**  **[REBUILT, phase 131, round 2.]**
Row C may also use, as a theorem of row B, Theorem 3bis.7′: the finite-place
representing measure `ω_{fin}` of `T` on the radial sector is purely atomic
with support exactly `\{±k\log p\}` and atom masses `(\log p)p^{−k/2}`.  This
is the precise sense in which row C's geometric side is a *contact locus* of a
one-parameter family on row A's carrier, and it carries with it the honest
caveat that the objects `Γ^{rad}_{(t)}` are themselves arithmetic-free
(Lemma 3bis.3b).

**9.4 The correction to Paper 45 §11 (now deleted there).**  **[REBUILT, phase
131.]**  **[phase 133, PANEL_2 MINOR-1: Paper 45 §11 and its Theorem 11.1 were
**withdrawn in phase 132** (Paper 45 §13 **W45.7**), which deletes the section
rather than discharging the obligation — exactly the outcome this subsection
asked for.  What follows is therefore **history**, in the past tense; Paper 45
W45.7 records that clause (a) below was and remains correct about the lift.]**
Paper 45 §11 (Theorem 11.1) **stated**, in its phase-130 version, that it
*discharges row B's handoff*, namely that
`w_unit(Γ_n) = n−1` is "a sample of the unit integrand across places".  Two
statements must be separated.

  (a) *Paper 45 Theorem 11.1's computation is correct as a computation.*  For
      `q ∤ n`, `τ_q(n) = |1−n|_q^{−1}` is indeed the value at `u = n` of the
      integrand of the regularized unit packet `(\log q)∫_{Z_q^×}(a(u) −
      a(1))/|1−u|_q\,du`.  Nothing in it is false.
  (b) *But there was no obligation to discharge.*  The unit packet is
      evaluated on `a = F∘j_q`, and the arithmetic class is not in the image
      of `j_q` (Proposition 3bis.2); moreover for a **radial** section the
      unit packet vanishes identically, because `a` is constant on `Z_q^×`
      (proof of Theorem 3bis.7).  So the norm class never samples that
      integrand at `u = n`, or anywhere else.  `n−1` is a product of local
      factors of the **lift**.  **[REBUILT, phase 131, round 2, finding
      `F8`:]** the first clause needs `|S_f| ≥ 2` (Proposition 3bis.2); the
      second does not, and on the minimal chart `S = \{∞,p\}` the product
      defining `w_unit` is moreover **empty**, hence `1` (Theorem 3.3, phase-
      128 `B5` correction).  The conclusion — the class contributes no `n−1` —
      holds on every chart; see Remark 3bis.2a.

Row B therefore withdrew the obligation (§9bis) and recorded that Paper 45
§11 discharged something that was never owed.  **[phase 133: Paper 45's
campaign has since decided — §11 and Theorem 11.1 are deleted (W45.7).  The
sentence that stood here, "Paper 45 §12's radial sector `G_rad` is exactly the
sector in which §3bis works", is **struck**: `G_rad`, together with Paper 45
Proposition 12.2 and Theorem 12.3, was withdrawn in phase 132 (Paper 45 §13
**W45.8**), so it names no live object.  The radial sector in which §3bis
works is `D_A^{rad}` of Definition 3bis.6 here, and Paper 45's live statement
about it is Lemma 1.1.  Nothing rested on the struck sentence (PANEL_2
MINOR-1).]**

**Remark 9.3.**  Before Theorem 3.3 the `n−1` factor was read as evidence that
row A's invariant computed the *wrong* contact (P123.060 §4).  Theorem 3.3
showed it was a second, coprimely supported quantity.  §3bis shows the third
and final thing: it is a quantity of the **lift**, and the class does not see
it.  The progression is recorded because each step was a real correction of
the one before.

---

## 9bis. What was withdrawn in phase 131

**[REBUILT, phase 131.]**  Four statements of the previous version are
withdrawn.  Each is listed with what replaces it.  Nothing is deleted from the
record; the phase-128 honesty notes and withdrawal records above are kept
verbatim.

**W1.  The `n−1` obligation handed to row C (former §9.2).**  *Withdrawn.*
The text read: "`w_unit(Γ_n) = n−1` is canonical, nonzero, and **absent from
the explicit formula** … Row C must therefore prove that the unit-sector
contribution of the arithmetic family is absorbed by the Tate and Gamma
terms."  There is no unit-sector contribution of the arithmetic family: the
class `δ_S(1/n)` is in the image of no slice map `j_q` (Proposition 3bis.2,
for `|S_f| ≥ 2`), so it contributes to no finite local term at all
(Corollary 3bis.3), and the radial norm class annihilates the unit packet
identically (Theorem 3bis.7).  `n−1` is a product of local factors of the
idele `a_S(n)`, i.e. of a chosen lift.  **[REBUILT, phase 131, round 2,
finding `F8`:]** on the minimal chart `|S_f| = 1` the geometric statement
fails — `δ_S(1/p^k) = j_p(p^k·1)` lies on the slice — but the withdrawal
stands there too, for two independent reasons given in Remark 3bis.2a: the
product defining `w_unit` is empty on that chart, and a point mass at the
single unit `u = 1` is null for the shell's probability Haar measure, so only
the unit-spread class receives the shell volume.  *Replaced by:* §9.2 (the
archimedean density), §9.3 (`Λ` = shell volume) and §9.3a (the contact
locus), which are the items row B actually has to hand over.

**W2.  The cross-reference "Discharged in Paper 45 §11".**  *Withdrawn as a
discharge*, kept as a correct computation about the lift.  See §9.4.
**[phase 133, PANEL_2 MINOR-1: Paper 45 §11 and Theorem 11.1 no longer exist —
withdrawn in phase 132, Paper 45 §13 W45.7.  The discussion in §9.4 is kept as
history and is read in the past tense.]**

**W3.  `w_unit` and `w_ram` as answers to the `Λ(n)` question (Thm. 8.1(iv)).**
**[phase 133, PANEL_2 MAJOR-1: the heading and the first sentence attributed
the question to "Paper 43 Remark 9.5", which does not exist; the question is
row B's own, prompted by Paper 43 Remark 9.7a.]**
*Withdrawn.*  The question is what the family's pairings equal "in terms of
`Λ(n)`".  The answer is Theorem 3bis.7 — the finite contact of the norm class
is `Λ(n)n^{−1/2}`, an exact value of `T` — and not the lift quantities
`w_ram·w_unit`.  Theorem 8.1(iv) is restated accordingly.

**W4.  Theorem 3.3(iv)–(v) as statements about the correspondence.**
*Withdrawn as such; re-stated as statements about the lift* (the `[REBUILT,
phase 131]` block inside Theorem 3.3).  Parts (i)–(iii) are unchanged and
remain the paper's contribution to reading P123.060.

**W5.  "The arithmetic object is the ideal class" (round-1 framing).**
*Withdrawn.*  **[REBUILT, phase 131, round 2, finding `F1` of `R131.002`.]**
On a chart with `P(n) ⊆ S_f` — the standing hypothesis of §3bis — `n` is an
`S`-unit, so the ideal `nZ_S` is the **unit** ideal and there is no ideal for
the class to be the class of (Lemma 3bis.3b).  The object is the **norm
class**, the Haar measure of a level set of `|·|_S`, and the realization
factors through `(R_{>0},×)`, forgetting factorization.  *Replaced by:*
Lemma 3bis.3b (the negative statement, proved), Theorem 3bis.7′ (the positive
one: the arithmetic is the contact locus of the family), and Remark 3bis.5b
(the honest reading of B.1, B.2 and B.6's first half).

**W6.  "The value on `Γ_n^{rad}` of `T`" in the amended clause B.4.**
*Withdrawn as ill-typed.*  **[REBUILT, phase 131, round 2, finding `F2`.]**
`T` is defined on `D_A` only and `Γ_n^{rad} ∉ D_A`; the naive place-wise
evaluation returns `0`, not `Λ(n)n^{−1/2}`.  *Replaced by:* the mass at
`t = \log n` of the **unique** representing Radon measure `ω_{fin}`
(Definition–Theorem 3bis.8), in §2's table, in §6.2a′'s boxed amendment, and
in the PLAN §6 note.

**W7.  "The arrow P123.038 §5 asked for" (title of Remark 3bis.10b).**
*Withdrawn*, together with the two `PROVED` ledger rows that split that open
item.  **[REBUILT, phase 131, round 2, finding `F3`.]**  The full quotations
(now in Remark 3bis.10b) demand a cyclic extension to **mixed
correspondences** and a comparison with the analytic **nuclear** trace as a
**functor**, and state in advance that neither an invariant of the arithmetic
family nor a collection of equal trace values suffices.  Row B supplies a
comparison of **degrees**.  The item is one row and reads `PARTIAL`.

**W8.  "The mechanism is located on the carrier" (round-1 Theorem 6.5(ii)).**
*Withdrawn as a theorem clause; kept as a numerical coincidence.*  **[REBUILT,
phase 131, round 2, finding `F5`.]**  `vol(p^kZ_p^×) = \log p` and
`Φ_{p^k}(1) = p` are both `k`-independent for unrelated reasons and no map
between them is supplied (Remark 6.5a′).  B.7 reads `PROVED` as a test,
`PARTIAL` as a mechanism.

**W9.  "The archimedean contact of `Γ_n^{rad}`".**  *Withdrawn as a name.*
**[REBUILT, phase 131, round 2, finding `F6`.]**  It is `ω_∞(\log n)`, the
archimedean density of the radial family at the label `\log n`: a value of a
continuous density, defined for every real `t`, with no object attached.  The
family has no archimedean atom, and that is the complete answer to `D128.002`
`B6`.

**W10.  The proof of Theorem 8.1(iii)'s second clause, and of (iv).**
*Withdrawn.*  **[REBUILT, phase 131, round 2, finding `F4` of `R131.002` =
`F1` of `R131.003`.]**  The round-1 proof of (iii) retained the invalid
inference `D128.002` `B1` had accepted as an error, and its conclusion ("`Λ`
is not pulled back from the ruling plane") is **false** and contradicted §7
check 5 of the same paper.  The round-1 proof of (iv) still cited the places
`q | p^k−1`, contradicting the rebuilt statement and W3.  Both proofs are
replaced in place.

### Round 3

**[REBUILT, phase 131, round 3.]**  Nothing proved in rounds 1–2 is withdrawn
in round 3; §§3bis is **kept in full**, including Lemma 3bis.3b's negative
result, because it is true and because §3ter's positive result is only
meaningful against it.  Two **framings** are superseded and one blueprint
claim is refuted.

**W11.  "The arithmetic object on the carrier is the radial family."**
*Superseded, not withdrawn.*  The radial family is arithmetic-free as an
object (Lemma 3bis.3b) and its contact locus is the arithmetic
(Theorem 3bis.7′); both remain true.  But the radial family is not the only
family available, and it is not the Frobenius.  §3ter constructs the
**Frobenius family** `Frob_n`, the Haar measures of the fixed-point strata
`j_p(p^kZ_p^×)`, which is *not* radial, has a **true unit** `Frob_1 = Δ`,
composes strictly (`Frob_m⋆Frob_n = Frob_{mn}`), and whose support determines
`n` **and** `P(n)` (Theorem 3ter.4).  Reservations `R1` and `R6` of
`R131.005` are answered by Theorems 3ter.4(iv), 3ter.12 and Remarks 3ter.4a,
3ter.12a — and `Γ_n^{rad} = Frob_n ⋆ Δ^{rad}` (Proposition 3ter.5), so the
radial object is the image of the Frobenius under the projector that destroys
the factorization.

**W12.  "`Z/Φ_n(1)` is not the value of anything on the objects."**
*Superseded.*  Theorem 6bis.4 proves the accepted amended B.4 on the objects,
via the **integral shadow** `Sh_Z(Frob_n) = [L_S →n→ L_S]` of Definition
6bis.1, well defined on the measure (Lemma 6bis.2) and with Möbius cofiber
`[Z→Φ_n(1)→Z]` (Theorem 6bis.3(v)).  What is **not** superseded, and is
restated in Remark 6bis.5: `Sh_Z` is not a functor on the `C`-linear category,
its complex realization is acyclic, the identification is of **degrees**, and
the functorial demand of P123.038 §5 / P123.039 §5 remains `OPEN`.

**W13 (a refuted blueprint claim).**  The round-3 blueprint asserts that the
`†`-closed Frobenius family is `\{Frob_r : r ∈ Q_{>0}^×\}` with
`Frob_{a/b} := Frob_a⋆Frob_b^†`.  **False**: that assignment is not well
defined.  `2/1 = 6/3`, yet `Frob_2⋆Frob_1^† = μ_{j_2(2)K_{\{2\}}}` and
`Frob_6⋆Frob_3^† = μ_{j_2(2)K_{\{2,3\}}}` have different supports
(Theorem 3ter.7(iv)).  The correct index set is `Q_{>0}^×` **graded by the
semilattice of finite prime sets**, and the resulting object is a commutative
**inverse semigroup**, not a group — which is the structurally right answer,
since the idempotents `Δ^{(F)}` are exactly the extra data.

**W14 (a second refuted blueprint claim).**  The blueprint asserts that the
smeared finite contact is "exactly `Λ(n)n^{−1/2}·∫ρ_ε` for every `N` and small
`ε`".  **False**: the shell integral evaluates the archimedean profile at the
single point `x_∞ = p^{−k}`, so what appears is the **value** `h(1/n)`, not
`∫h`; with an `L^1`-normalized bump this diverges like `1/ε`.  The correct and
stronger statement is Theorem 3ter.10: the finite contact is
`Λ(n)n^{−1/2}h(1/n)` **exactly, for every `N` and every admissible `h`**
(Remark 3ter.10a).

**W15 (a third refuted blueprint claim).**  The blueprint asserts that the
smeared self-pairing "diverges like `−2\log(1/ε)`".  The coefficient `2` is
not obtained in either natural normalization, and the **rate** is
normalization-dependent: `−ε^{−1}\|φ\|_2^2\log(1/ε)` for a mass-normalized
approximate identity, `−\log(1/ε)+O(1)` for the `L^2`-normalization
(Theorem 8bis.2, Remark 8bis.2b).  The qualitative claim `Δ·Δ = −∞` is correct
and is proved.

### Round 4

**[REBUILT, phase 131, round 4.]**  One round-3 claim was **false** and is
withdrawn outright, together with the two statements that rested on it.

**W16.  "The Gram form of the Frobenius family is the Weil kernel"
(round-3 Corollary 8bis.1a; §0; banner; §10 block).**  *Withdrawn as false.*
**[Adversarial finding `F1` of `R131.008`, independently confirmed by the final audit in
`R131.009`.]**  It is refuted by this paper's own Corollary 3ter.10b.  Applying
(3ter.9) with `r = m/n`, the archimedean part of the off-diagonal entry
carries the arithmetic indicator

    ∏_{s ∈ S_f∖(P(m)∪P(n))} \mathbf 1\big[\,s^N \mid (n−m)\,\big] ,

which **vanishes for all large `N`** whenever `S_f ⊋ P(m)∪P(n)`; equivalently,
`supp\,Frob_{m/n,F}` is disjoint from `Im\,j_∞`.  So the Frobenius Gram form
carries `W_{fin}` and **no** archimedean block, whereas the Weil kernel is
`W_{fin} + ω_∞`.  *Replaced by:* Corollary 8bis.1d (the finite half, with the
indicator displayed), Theorem 8bis.1e (**the Weil kernel is the Gram form of
`Frob ⋆ Δ^{rad}`**), and Theorem 8bis.1′ (the complementary-slice dichotomy as
a statement about Gram forms).  The repair is an improvement: the averaging
projector `Δ^{rad}` is exactly what converts the finite half into the whole.

**W17.  Round-3 Theorem 8bis.4(iii): "Weil positivity ⟹ `I_∂ ≤ 0` on the
Frobenius class", and round-3 8bis.4(v) "the object whose Hodge index is RH is
the Frobenius Gram form".**  *Both withdrawn.*  The proof of (iii) asserted
that `I_∂` differs from the Weil functional only by Tate terms killed by
primitivity; by W16 the difference also contains the entire off-diagonal
archimedean block `Σ_{m≠n}c_mc_n\,ω_∞(\log m − \log n)`, which primitivity
does **not** annihilate (take `A = \{2,3,4\}`: the block is a nondegenerate
non-multiple of the rank-two Tate form, and the numerics in
`scripts/verify_131_contacts.py` display it).  *Replaced by:* Theorem 8bis.4
rebuilt on the **radial** family, where the profile class is all of
`C_c^∞(R)` and the equivalence with RH is `CLASSICAL` and unconditional
(8bis.10); plus the new **negative** Theorem 8bis.4(iv).

**[SUPERSEDED BY `W19` (round 5); CORRECTED IN ROUND 6 — minor `m5′` of
`R131.014`.  The round-4 sentence that stood here — "the sign of the pure
Frobenius Gram form is **not** RH, because `ω̂_∞` is indefinite.  The object
whose Hodge index is RH is the Gram form of `Frob ⋆ Δ^{rad}`" — is
**withdrawn**: it is precisely the symbol-comparison non-sequitur.  The round-6
reading is (iv)(a) the two forms are **distinct** (`PROVED`), and (iv)(b)
**positivity fails on `Q_{fin}` at every finite chart** (Theorem 8bis.4a,
`PROVED`; the colimit version `OPEN`).  The object whose Hodge index is at
issue is the Gram form of `Frob ⋆ Δ^{rad}` **by (iii)** — the colimit statement
— and not by any comparison of symbols.  A withdrawals section may not carry an
unmarked live assertion of a withdrawn claim; this is the marker.]**

**W18.  Round-3 Theorem 8bis.1's silent exclusion of the diagonal.**
*Repaired, not withdrawn.*  **[Finding `F2`.]**  Round 3 proved the
off-diagonal entries and excluded `r = 1`, so the diagonal of the matrix it
called `PROVED` was undefined.  Theorem 8bis.1b now computes it: the finite
unit packets at `p | n` vanish, those at `r ∤ n` are
`−(\log r)[(r−2)/(r−1) + (N−1)]` **exactly**, a divergence **linear in `N`**,
and the archimedean term is `−\log(1/ε) + O(1)`.  So `I_A` on the Frobenius
class has **no** `ε → 0` or `N → ∞` limit on the diagonal — consistent with
Paper 43 Theorem 14.1 and with Theorem 3ter.14's point classes lying outside
`D_A` (Remark 8bis.1c).

### Round 5

**[REBUILT, phase 131, round 5.]**  One round-4 `PROVED` claim is withdrawn;
everything else in round 5 is a repair of a hypothesis, a normalization or a
proof.

**W19.  Round-4 Theorem 8bis.4(iv): "the sign of the pure Frobenius Gram form
is NOT RH", `PROVED`, argued by comparing the two forms.**  *Withdrawn.*
**[Finding `M1` of `R131.011` = `LF3` of `R131.012`.]**  The argument is a
**non-sequitur**: "`Q_{fin} ≤ 0` on the primitive sector ⟺ RH" is a
biconditional between two propositions of **fixed truth value**, and no
comparison of two fixed quadratic forms can refute such a biconditional — the
displayed argument shows only that the two forms are **distinct**, which
nobody disputed.  *Replaced by two statements, both proved:* (a) the two forms
differ by `∫|ĥ|^2ω̂_∞` with `ω̂_∞` indefinite, hence are distinct — which is
what the argument gives; and (b) **Theorem 8bis.4a**, which is stronger and is
the statement that matters: at **every fixed finite chart** there is an
explicit primitive radial class with `Q_{fin} > 0`, so **positivity fails on
the pure Frobenius form unconditionally**.  Remark 8bis.4b records that the
colimit version is `OPEN` (the colimit symbol `ω̂_{fin}^∞` is unbounded, so the
Plancherel step does not transfer) and that Theorem 8bis.4(vi) rests on (iii),
not on (iv).

**W20.  Round-4 import `(W)` of Theorem 8bis.7, and its Tate clause.**
*Withdrawn as stated; renamed and restated.*  **[Findings `M2`/`LF2`,
`M6`(b).]**  The clause "the contribution of ... the **Tate** terms is
`O(L^2e^{|β−1/2|L})`" is **false**: for `h_L = g_L⋆g_L^†` with non-primitive
`g_L` the polar contribution is `|\hat g_L(±i/2)|^2 ≍ L^2e^{L}`, which
**dominates** `e^{2|β−1/2|L}` since `2|β−1/2| < 1`.  The repair is to make the
tests **primitive by construction** with `Π = −∂_t^2+1/4` (Paper 45
Theorem 10.4), after which the Tate packet is **absent** and the import
carries no Tate clause.  The symbol is renamed **`(Wgr)`** to avoid the
collision with Paper 43 §12's `W` (Wodzicki) and with `W_{fin}`, `W_p`, `W_∞`.

**W21.  Round-4 Theorem 8bis.7's two-coefficient primitivization.**
*Withdrawn.*  **[Findings `M2`/`LF2`.]**  "Primitivity can be enforced by
altering two coefficients near `\log n ≈ L/2` by `O(e^{−L})`" is wrong by a
factor `≍ e^{5L/4}`: a single mesh bump there has `λ_−`-weight
`≍ gap_n\,n^{1/2} ≍ e^{−3L/4}` against `λ_−(e) = O(1)`.  *Replaced by:* a
**minimal correction along the two Riemann-sum profiles `w_1, w_2` of
`e^{±s/2}η`**, whose `λ`-weights are exponentially large; Cramer gives
`a = O(e^{−L})`, `b = O(e^{−L/4})` and a correction of **sup norm**
`O(e^{−L/2})`, the same size as `‖e‖_∞`, so every estimate survives
(8bis.13d)–(8bis.13f).  **[REBUILT, phase 131, round 7, minor `p6` of
`R131.017`: this withdrawal record still printed the round-5 order
`b = O(Le^{−L/2})`, which `m1′`/`LF6`(a) superseded; the correct order is
`b ≍ λ_+(e)λ_−(w_1)/\det ≍ e^{−L/4}`, and the sup norm is `O(e^{−L/2})`.]**

**W22.  Round-4 Lemma 8bis.6, for a general mass-one bump.**  *Withdrawn as
false.*  **[Findings `M3`/`LF1`.]**  By Poisson summation
`Σ_kρ(x−k) = Σ_m\hatρ(2πm)e^{2πimx}`, which is not `≡ 1` for a general mass-one
`ρ` — for `ρ` supported in `[−0.1,0.1]` the sum **vanishes** on most of the
line.  The round-4 proof also conflated a *tested* estimate (which is
`O(Le^{−L/2})`) with the *pointwise* one the lemma needs.  *Replaced by:* a
smooth **partition of unity** `Σ_kρ(x−k) ≡ 1`, and a **pointwise** proof by
slow variation of the gaps ((8bis.13a)–(8bis.13b)), which also removes the
spurious factor `L`.

### Round 6

**[REBUILT, phase 131, round 6.]**  One `CLASSICAL` import is withdrawn as
**false**; nothing else in the paper changes status.

**W23.  The import `(Wgr)` of Theorem 8bis.7 (rounds 4–5).**  *Withdrawn as
false.*  **[Finding `LF5` of `R131.015`; the adversarial pass did not catch it.]**
`(Wgr)` asserted that for the single-frequency tests
`g_L = ψ(t/L)e^{−iγ_0t}` the sum over zeros of `h_L = g_L⋆g_L^†` has a **fixed
sign** and modulus `≍ L^2e^{2|β−1/2|L}` at a hypothetical off-line zero.  **Both
claims are false**, and Lemma 8bis.6b now proves it:

  * every **on-line** zero contributes `|\hat g_L(ρ)|^2 ≥ 0`;
  * the **resonant** off-line pair `\{ρ_0, 1−\bar ρ_0\}` contributes
    `2\,\hat g_L(ρ_0)\,\hat g_L(1−\bar ρ_0)` with **both factors positive
    reals** when `ψ ≥ 0` — of sizes `e^{δL}` and `e^{−δL/2}`, `δ = β−\tfrac12`
— hence `≍ +e^{δL/2}`: **positive**, and with **half** the exponent, not
    `−L^2e^{2δL}`;
  * and the failure is structural: for any amplitude `w ≥ 0`,
    `\hat g(ρ_0) = ∫we^{δt} ≥ ∫we^{−δt} = \hat g(1−\bar ρ_0) > 0`, so no
    non-negative amplitude and no real tilt can make the transform peak at
    `1−\bar ρ_0` (Lemma 8bis.6b(iv)).

*Replaced by:* Theorem 8bis.7 restated as a **conditional transfer theorem** —
its analytic machinery (Lemmas 8bis.5, 8bis.6, **8bis.6a**, and Steps 1–3,
including the `C^1` control round 5 lacked) **proved in full**, its arithmetic
input isolated as the explicit hypothesis `(H_L)` with the scale-invariant
ratio (8bis.14d), and the question *whether `(H_L)` holds under `¬RH`*
recorded as **`OPEN`**, with the obstruction quantified in
Remark 8bis.7a(2)(α),(β).  The implication "positivity on Dirichlet-polynomial
profiles ⟹ RH" is therefore **`OPEN`** and is **not claimed**.

**Also repaired in round 6, without withdrawal:**  the `C^1` gap in Step 3 of
Theorem 8bis.7 (`N3`/`LF6`(b): new **Lemma 8bis.6a**, `‖(g−g_D)'‖_∞ =
O(‖g‖_{C^1})`, whose proof turns on the cancellation `Σ_kρ'(x−k) ≡ 0` in the
partition of unity — without it the naive bound would be `e^{L}` and the error
would dominate the main term for `|β−\tfrac12| < 1/4`; and the expansion
(8bis.13h), in which only `\tilde g` and `ẽ` occur); the order of `b` in
Cramer (`LF6`(a), `m1′`: `b = O(e^{−L/4})`, not `O(Le^{−L/2})` — the sup norm
`O(e^{−L/2})` is unchanged and (8bis.13f) stands); Theorem 8bis.2's exemption
from (C1) (`N1`, with the observation that under `T_∞` the finite part is
identically zero and the result is *easier*); the display renumbering itself
(`N2`: round 5 renumbered the references and not the displays, leaving six
pointers to nothing); the withdrawn `M1` argument surviving as the stated
reason in §0 and the banner (`N4`) and in §9bis `W17` (`m5′`); the sign in
(8bis.8c)'s cross term (`m2′`: `2\,\mathrm{Im}`, odd, not `2\,\mathrm{Re}`,
even); the false majorant in Theorem 8bis.4a Step 3 (`m3′`: `(σ^2+1)^2`); the
complex→real reduction of Theorem 8bis.7, now carried out (`m4′`); the naming
of `Q_{fin}` (`m6′`); the garbled carve-out sentence of Theorem 8.2 (`m7′`);
`A_S = ω̂_{fin}(0)` **exactly** (`n2′`); and the tautological numerics block
(`n1′`).

**Also repaired in round 5, without withdrawal:**  the chart quantifier
throughout §8bis (`M4`: `T` means `T_∞` on `D_A^∞`, standing convention (C1);
(8bis.10) is a colimit statement and is **false** at a finite chart); the
normalization of the level-`N` factors (`M5`: standing convention (C2),
Corollary 8bis.1b′ with the conversion factor `V_N(n)`, and **no rate
headlined anywhere**, since no rate is convention-free); the ledger row for
P123.038 §5 (`M6`(a), announced twice in rounds 3–4 and not done); §11's
"External inputs: none" and Theorem 8.2's blanket independence claim
(`M6`(b),(c)); the missing `ε_0` in Theorem 8bis.1e (`m1`); the dropped
profile value and convolution constants in (8bis.5) (`m2`); the duplicated
equation numbers and stale cross-references (`m3`); Lemma 8bis.5's unlabelled
import and impossible constant (`m4`); real-versus-complex profiles (`m5`,
now (8bis.8c)); `README`'s unmarked round-3 block (`m6`); §11's stale
phase-131 record (`m7`); the scale quotient in Theorem 8bis.8 (`n1`); and the
operative reason in Theorem 8bis.1's shell criterion (`n2`).

**Also repaired in round 4, without withdrawal:** the missing hypothesis
`ε < ε_0(A,S)` (`F3`, now in Theorem 8bis.1 with its discreteness argument)
and the dropped convolution constants `∏vol(1+r^NZ_r)`; the misquotation of
(8.5∞)'s folding (`F4`); the use of the `|τ| → ∞` asymptotic on bounded `τ`
(`F5`, now split off as (8bis.8a)); the display rate in Theorem 3ter.14(ii)
(`F6`); the unproved composition claim for `Sh_Z` (`F8`, now Lemma 6bis.3a).

**Also corrected, but not withdrawn.**  The the earlier blueprint for this phase
asserted that `Γ_n^{rad}` "lies in the Fell completion of `G`" as "a
continuous compactly supported section".  It does not — it is a point mass in
the archimedean coordinate — and Remark 3bis.4b states the correct type: a
multiplier of `D_A` and an element of `N_A^{dist}`, in exact analogy with
Paper 43 Remark 8.11 for the diagonal.  The blueprint also averaged over
`K = ∏_{p∈S_f}Z_p^×` only; the average must be over
`K^♮ = \{±1\}×∏_{p∈S_f}Z_p^×`, or neither the Haar-coset computation of
Theorem 3bis.5(i) nor the half-sum `½[τ_∞(1/n)+τ_∞(−1/n)]` of (3bis.11) is
available.  Both corrections are stated where they occur.

---

## 10. Verdict and clause ledger

**[REBUILT, phase 131.]**

```text
ROW B, after phase 131 round 7 (apparatus only; no new mathematics).

  R131.017 found that THREE repairs reported as done in R131.016 were
  NOT in main.md.  Round 7 therefore repairs by grep, and every item is
  verified by pasted command output in R131_018.

  A1  section 0: the withdrawn omega_inf symbol-comparison sentence
      ("since the latter's kernel lacks the indefinite omega_inf-hat")
      survived verbatim.  DELETED; the conclusion now cites
      Thm 8bis.4(iii) and Thm 8bis.1e.
  A2  banner round-4 bullet: "rate computed", "diverges LINEARLY in N",
      and the attribution to Thm 8bis.4(iv) survived.  REWRITTEN to the
      round-6 reading (no rate; I_A(Frob_n,Frob_n) DOES NOT EXIST).
  A3  section 8bis.4's header and Thm 8bis.4(v) still promised the
      attempt "closes modulo one named classical import", which W23
      retracted.  BOTH REWRITTEN: conditional transfer theorem, (H_L)
      OPEN, nothing settled.
  A4  N2 regression: round 6 deleted displays (8bis.13c), (8bis.13d),
      (8bis.13e) while keeping the pointers.  ALL THREE RESTORED with
      their tags.  A mechanical cross-reference pass over every
      (8bis.NN) token now returns an EMPTY diff in both directions and
      no double assignment (output pasted in R131_018).
  A5  (H_L) covered only the FIRST of the two error terms of (8bis.13i);
      the second was covered by a side condition asserted in Step 4 and
      NOT contained in (H_L).  R(L) in (8bis.14d) now covers BOTH terms
      and the side condition is DELETED, so the conclusion follows from
      R(L) -> 0 alone.
  p1  Lemma 8bis.6b: "quadruple" where a PAIR was estimated.  New (ii'):
      the conjugate pair is bounded by the SAME order e^{delta L / 2}
      (trivially, by |g-hat| <= the positive resonant values), with sign
      undetermined.  So (Wgr)'s MODULUS claim (~ L^2 e^{2 delta L}) is
      REFUTED OUTRIGHT, and its MECHANISM (the resonant term) is refuted
      by positivity; the sign of the full sum is NOT decided and is not
      claimed.
  p2  New (v): Lemma 8bis.6b also holds for the PRIMITIVIZED tests.
      Pi multiplies the pair term by 2 Re(A^2), A = rho_0 (1 - rho_0),
      and Re(A^2) > 0 whenever |gamma_0| > 2 delta -- in particular for
      every nontrivial zero.  [NOT 2|A|^2: see R131_018 section 4.]
  p3  the threshold 2a < delta + 1/4 is marked INDICATIVE, not a
      theorem; "quantified" is withdrawn.
  p4  Thm 8.2's carve-out sentence de-garbled (it was NOT, in round 6).
  p5  section 11 said "three" imports; it is TWO (Weil's criterion,
      Chebyshev), with (Wgr) moved to a "withdrawn, cited nowhere" line.
  p6  W21 still printed the superseded Cramer order b = O(L e^{-L/2});
      corrected to b = O(e^{-L/4}), sup norm unchanged.
  p7  Step 4's "up to the fixed sign convention" removed; the convention
      is fixed in 8bis.4(ii) and (8bis.14e) states I_d = -Q without
      hedge.
  p8, p9  frequency sign made consistent; numbering gap closed by A4.

  LABEL: NOT SELF-GRANTED AND NOT CLAIMED.  Imports: TWO, both
  CLASSICAL, both quarantined, neither used by any clause of B.1-B.9.
```

```text
ROW B, after phase 131 round 6.  SUPERSEDED WHERE THE ROUND-7 BLOCK
APPLIES (the apparatus items A1-A5 and p1-p9); the mathematics of
round 6 is unchanged.

  ROUND 6 (adversarial R131.014: N1-N5 + 7 minors + 2 notes; final audit R131.015:
  LF5, LF6).  No clause verdict moves.  ONE CLASSICAL IMPORT IS
  WITHDRAWN AS FALSE (W23); the theorem that used it is restated as a
  CONDITIONAL transfer theorem with its arithmetic input isolated.

  LF5 (final audit; the adversarial pass missed it) -- THE MOST SERIOUS ITEM.
      The import (Wgr) of Thm 8bis.7 is FALSE.  For the single-frequency
      test g_L = psi(t/L) e^{-i gamma_0 t} with psi >= 0:
        * on-line zeros contribute |g_L-hat(rho)|^2 >= 0;
        * the RESONANT off-line pair contributes
          2 g_L-hat(rho_0) g_L-hat(1 - conj rho_0), BOTH FACTORS
          POSITIVE REALS, of sizes e^{delta L} and e^{-delta L/2},
          hence ~ +e^{delta L /2}: POSITIVE, and with HALF the exponent
          that (Wgr) claimed (2 delta L), not negative.
        * and structurally: for ANY amplitude w >= 0,
          g-hat(rho_0) = int w e^{delta t} >= int w e^{-delta t}
                       = g-hat(1 - conj rho_0) > 0,
          so no non-negative amplitude and no real tilt can peak the
          transform at 1 - conj rho_0.  Peaking needs CANCELLATION,
          which is what destroys the sup-norm control.
      All of this is PROVED as Lemma 8bis.6b.  (Wgr) is withdrawn (W23)
      and cited nowhere.
  REPLACEMENT.  Thm 8bis.7 is now a CONDITIONAL TRANSFER THEOREM:
      (a) PROVED: if the explicit hypothesis (H_L) holds for arbitrarily
          large L -- a primitive g_* in C_c^inf([L/2,L]) with Q(g_*) < 0
          and R(L) = L e^{-L/4} ||g_*||_inf ||g_*||_{C1} / |Q(g_*)| -> 0
          -- then positivity FAILS on the Dirichlet-polynomial class.
      (b) CLASSICAL: if RH fails, Q(g) < 0 for some primitive g
          (Weil's criterion; Paper 45 Thm 10.4 for primitivity).
      (c) OPEN: whether such g can be taken in a MOVING window with
          R(L) -> 0.  Rem 8bis.7a(2) quantifies the obstruction in both
          of its parts (alpha: the single-frequency route is provably
          dead; beta: the two-frequency route's norms grow like e^{2 a L}
          while the available lower bound on |Q| does not).
      So "positivity on Dirichlet profiles => RH" is OPEN and NOT
      claimed.  The machinery is proved; only the arithmetic input is
      missing, and it is named.
  N3/LF6(b).  New Lemma 8bis.6a: ||(g - g_D)'||_inf = O(||g||_{C1}),
      proved via the cancellation sum_k rho'(x-k) = 0 in the partition
      of unity.  Without it the naive bound is e^{L} and the error would
      DOMINATE the main term for |beta - 1/2| < 1/4.  Step 3 rewritten
      with the expansion I(g,g) - I(g_D',g_D') = I(e,g) + I(g,e) - I(e,e)
      in which only g and e occur.
  N1.  Thm 8bis.2 is EXPLICITLY EXEMPTED from (C1) (fixed chart; A_S is
      a chart constant).  Under T_infinity the conclusion is unchanged
      and EASIER: for eps < (log 2)/2 the profile meets no atom of
      W_fin, the finite part is identically 0, the divergence is purely
      archimedean.
  N2.  The displays themselves are renumbered (8bis.4b), (8bis.4c),
      (8bis.8b); round 5 had renumbered only the references, leaving six
      pointers to equations that did not exist -- including the one
      quantitative hypothesis of Thm 8bis.4a.
  N4, N5, m5'.  The WITHDRAWN symbol-comparison argument is purged from
      section 0, the banner, README's round-4 block and section 9bis W17.
      The conclusion "NOT the Frobenius Gram form" now cites (iii) --
      Weil's criterion on the radial family, in the colimit -- and the
      corrected (iv); never a comparison of symbols.
  LF6(a)/m1'.  b = O(e^{-L/4}), not O(L e^{-L/2}); sup norm unchanged.
  Plus m2' (2 Im, not 2 Re), m3' (majorant (sigma^2+1)^2), m4'
      (complex->real reduction carried out), m6' (Q_fin named once),
      m7' (garbled carve-out), n1' (tautological numerics block
      replaced), n2' (A_S = omega_fin-hat(0) exactly).

  LABEL: NOT SELF-GRANTED AND NOT CLAIMED.  Imports now: TWO, both
  quarantined -- Weil's criterion (Thm 8bis.4(iii), CLASSICAL) and
  Chebyshev (Lemma 8bis.5, CLASSICAL).  [phase 132] The explicit-formula
  half of Thm 8bis.4(ii) is PROVED-IN-REPOSITORY (Paper 45 Thm 9.4) and
  is no longer an import.  (Wgr) is gone.
  No sign, no positivity, no N_infinity = 0, no statement about zeros
  outside those clauses, none of which is used by any clause of B.1-B.9.
```

```text
ROW B, after phase 131 round 5.  SUPERSEDED WHERE THE ROUND-6 BLOCK
APPLIES (the import (Wgr), Thm 8bis.7's status, Thm 8bis.2's chart, and
the attribution of "NOT the Frobenius Gram form"); kept otherwise.

  ROUND 5 REPAIRS (adversarial R131.011 M1-M6 + 7 minors + 3 notes; final audit
  R131.012 LF1-LF4).  No clause verdict moves; section 8bis is not a
  clause.  One round-4 PROVED claim is WITHDRAWN (W19).

  M4 (mandatory, done first).  Standing convention (C1) at the head of
      section 8bis: T means the COLIMIT trace T_infinity on D_A^infinity
      (Paper 43 Thm 8A.7c) and W_fin is the kernel over ALL primes.  In
      particular (8bis.10) -- "I_d <= 0 on primitive radial classes
      <=> RH" -- is a COLIMIT statement; AT A FINITE CHART IT IS FALSE,
      and both forms are indefinite there (Paper 43 Thm 14.1).  Carried
      into Thm 8bis.1e, Thm 8bis.4, Lemma 8bis.5, Thm 8bis.7.
  M1/LF3.  Round-4 Thm 8bis.4(iv) "the sign of the pure Frobenius Gram
      form is NOT RH" is WITHDRAWN as a NON-SEQUITUR (W19): a
      biconditional between propositions of fixed truth value cannot be
      refuted by comparing two fixed quadratic forms.  Replaced by
      (a) PROVED: the two forms differ by int |h-hat|^2 omega_inf-hat,
      omega_inf-hat indefinite, so they are DISTINCT; and
      (b) Thm 8bis.4a, PROVED and STRONGER: at every finite chart
      omega_fin-hat(0) = sum_p (log p) 2p^{-1/2}/(1-p^{-1/2}) > 0, and
      g_T := Pi(phi(./T)) is PRIMITIVE (Pi = -d_t^2 + 1/4 kills both
      Tate moments) with g_T-hat concentrated near tau = 0, so
      Q_fin(g_T) > 0 for large T: POSITIVITY FAILS ON THE PURE FROBENIUS
      FORM, UNCONDITIONALLY, at every finite chart.  The COLIMIT version
      is OPEN and is NOT asserted (omega_fin-hat^infinity is unbounded;
      Rem 8bis.4b).  Thm 8bis.4(vi) rests on (iii), not on (iv).
  M5.  Standing convention (C2): section 8bis works in the BARE
      normalization; the conversion factor V_N(n) = prod vol(1+r^N Z_r)
      is (8bis.0) and Cor 8bis.1b' gives the Gram diagonal in BOTH
      conventions: bare -> 0, flat -> -infinity.  NO RATE IS HEADLINED
      ANYWHERE; what is stated is Rem 8bis.1c -- I_A(Frob_n,Frob_n) DOES
      NOT EXIST, because Frob_n is not in D_A.
  M2/LF2.  Thm 8bis.7 repaired: tests primitive BY CONSTRUCTION via
      Pi (Paper 45 Thm 10.4), import restated with NO Tate clause and
      RENAMED (Wgr) (the round-4 clause was false: the polar terms are
      ~ L^2 e^L and dominate e^{2|beta-1/2|L}); the two-coefficient
      primitivization (wrong by e^{5L/4}) replaced by a minimal
      correction along the Riemann sums of e^{+-s/2}, with a = O(e^-L),
      b = O(L e^{-L/2}) and SUP-norm size O(L e^{-L/2}) = size of e.
  M3/LF1.  Lemma 8bis.6 repaired: the bump is now a smooth PARTITION OF
      UNITY (a general mass-1 bump fails by Poisson), and the POINTWISE
      mesh identity is proved by slow variation of the gaps.
  M6.  P123.038 section 5 ledger row RE-GRADED (announced twice in
      rounds 3-4, not done); section 11 "External inputs: none" replaced
      by the list of the three CLASSICAL imports of section 8bis, each
      "used by no clause of B.1-B.9"; Thm 8.2's blanket independence
      claim now carries the carve-out.
  Plus the 7 MINORs and 3 NOTEs (m1-m7, n1-n3).

  LABEL: NOT SELF-GRANTED AND NOT CLAIMED.  No sign, no positivity, no
  N_infinity = 0, and no statement about zeros outside the clauses
  labelled CLASSICAL (Thm 8bis.4(ii)-(iii); section 8bis.4 with the
  named imports -- ROUND 6: (Wgr) is WITHDRAWN AS FALSE, so the only
  imports left are Weil's criterion and Chebyshev), none of which is used by any
  clause of B.1-B.9.
```

```text
ROW B, after phase 131 round 4.  SUPERSEDED WHERE THE ROUND-5 BLOCK
APPLIES (the divergence rate, the chart quantifier, and Thm 8bis.4(iv));
kept otherwise as the record.

  WHAT ROUND 4 CHANGED.  The adversarial audit R131.008 found ONE FATAL error
  (F1), independently confirmed by the final audit (R131.009): round 3 claimed
  that the Gram form of the Frobenius family IS the Weil kernel.  It is
  NOT -- the paper's own Cor 3ter.10b refutes it.  The claim, and the one
  interface direction that rested on it, are WITHDRAWN (section 9bis
  W16-W17), and the correct statement is proved instead:

    TWO GRAM FORMS (Thm 8bis.1, 8bis.1b, 8bis.1d, 8bis.1e, 8bis.1'):
      Frobenius family        -> W_fin only, no archimedean block
                                 (indicator prod 1[s^N | (n-m)] -> 0),
                                 diagonal divergent: LINEAR in N at each
                                 r not dividing n, and -log(1/eps)
                                 archimedean.  Both divergences negative;
                                 no limit exists (Rem 8bis.1c).
      Frob * Delta^rad        -> the FULL Weil kernel W_fin + omega_inf,
                                 exactly, at EVERY level, no indicators.
    MECHANISM: supp Frob_n misses Im j_infinity; the averaging projector
    spreads the support onto the level set, which meets Im j_infinity.
    So Delta^rad converts the finite half into the whole -- and loses the
    factorization (Lemma 3bis.3b).  Two readings of one projector.

  ALSO NEW IN ROUND 4:
    * Thm 8bis.8 + Cor 8bis.8a (L1, reservation R4): vol(Z_p^x) = log p
      is the UNIQUE local normalization for which the Tate residue is
      the same at every place (local zeta residue c_p/log p vs 1).
      Rem 8bis.8b states EXACTLY what does NOT force it: chart-invariance
      cannot, since Paper 43's total residue -/+ i(|S_f|+1) is itself
      chart-dependent.  So this is a UNIQUENESS theorem given a NAMED
      requirement (universal Tate residue per place), not a derivation.
    * Lemma 6bis.3a, Thm 6bis.3c, Rem 6bis.3d (L2): Sh_Z is a strict
      FUNCTOR on the divisor poset and a FUNCTION on the monoid; it
      extends additively to Z[Frobenius monoid]; the P123.038 section 5
      arrow is supplied in parts (b) cyclic (trivially: commutative) and
      (c) comparison of DEGREES with the analytic trace, while part (a),
      an object-level shadow functor on the C-linear G, is REFUTED
      (P123.022), not open.
    * Thm 8bis.4 rebuilt on the RADIAL family: there the profile class is
      ALL of C_c^inf(R), so I_d <= 0 on primitive radial classes <=> RH
      is CLASSICAL and UNCONDITIONAL -- and is NOT new; it is Weil's
      criterion carried by row A's trace.  The new part is the
      factorization through Frob (Thm 8bis.1e).
    * Thm 8bis.4(iv) NEW NEGATIVE: the sign of the PURE Frobenius Gram
      form is NOT RH, because omega_inf-hat is indefinite.
    * Section 8bis.4 (L3): the Dirichlet-polynomial converse, CLASSICAL
      and QUARANTINED, with import (W) named.  It closes for per-n
      widths; Rem 8bis.7a(2) states exactly why a SINGLE eps fails.
    * B.7 (L4): the earlier ruling R131.005 section 2 is adopted and the
      adversarial auditor's dissent is recorded VERBATIM beside it.

  LABEL: NOT SELF-GRANTED AND NOT CLAIMED.  No sign, no positivity, no
  N_infinity = 0, and no statement about zeros outside the clauses
  labelled CLASSICAL (Thm 8bis.4(ii)-(iii), Thm 8bis.7 with import (W)).
```

```text
ROW B, after phase 131 round 3.  SUPERSEDED WHERE FINDING F1 APPLIES
(the two lines about the Gram form and the Weil kernel), kept otherwise
as the record.  [The round-2 block is reproduced after this one, because
the audit trail matters.]  Author's
decision of : the B.4 amendment is ACCEPTED.  Round 3 answers
the five reservations of R131.005 with NEW MATHEMATICS, not relabeling:

  THE OBJECT.  Section 3ter constructs the FROBENIUS FAMILY
      Frob_{p^k} := Haar measure of the fixed-point stratum j_p(p^k Z_p^x),
      Frob_n     := star_{p|n} Frob_{p^{v_p(n)}} ,  Frob_1 = Delta .
  It is NOT radial.  Frob_m * Frob_n = Frob_{mn} exactly, the unit is the
  DIAGONAL ITSELF (a point mass, not a projector), and supp Frob_n
  determines BOTH n AND P(n) (Thm 3ter.4).  Gamma_n^rad = Frob_n * Delta^rad
  (Prop 3ter.5): the radial object is the image of the Frobenius under the
  projector that destroys the factorization.  [R1 answered]

  R1 (objects forget factorization) ...... ANSWERED, Thm 3ter.4(iv),
      Rem 3ter.4a: no weak-* continuous one-parameter family interpolates
      the Frob_n, because |P(n)| is not locally constant.
  R6 (B.6 vacuous for composite n) ....... ANSWERED, Thm 3ter.12: for
      composite n the SUPPORT of the object meets no fixed-point stratum
      at all; for n = p^k the support IS the shell.  Contact = Lambda(n)
      n^{-1/2} EXACTLY, at every level N, no limit (Thm 3ter.10).
  R3 (no dagger; unit is a projector) .... ANSWERED, Thms 3ter.4(ii),
      3ter.6, 3ter.7: true unit Delta; Frob_n * Frob_n^dagger = Delta^(n),
      the averaged form of Weil's Gamma_F Gamma_F^t = q Delta (with the
      half-density absorbing q, and Delta^(n) NOT EQUAL Delta -- said so);
      the dagger-closed family is a commutative INVERSE SEMIGROUP with
      idempotents Delta^(F), indexed by Q_>0^x GRADED BY finite prime sets
      (NOT by Q_>0^x -- the blueprint's claim is refuted, W13).
  R2 (Z/Phi_n(1) is the value of nothing) ANSWERED, section 6bis: the
      INTEGRAL SHADOW Sh_Z(Frob_n) = [L_S -> n -> L_S] is defined on the
      OBJECT (Lemma 6bis.2), has transitivity triangle (6bis.2), H^0 =
      Z/n, and Moebius cofiber [Z -> Phi_n(1) -> Z].  Thm 6bis.4 proves
      the accepted amended B.4 ON OBJECTS.  This is the "integral or
      lattice category with a complex realization" that P123.022 section 2
      Scope says must be CONSTRUCTED; its complex realization is acyclic,
      exactly as that paragraph predicts.  Degrees only; no C-linear
      object-level identification (P123.022 stands).
  R4 (Lambda inherited) .................. PARTLY ANSWERED, Cor 3ter.11,
      Rem 3ter.11a: Lambda(p^k) = the multiplicative Haar VOLUME OF THE
      SUPPORT OF THE OBJECT Frob_{p^k}, times its half-density.  The
      NUMERICAL normalization vol(Z_p^x) = log p is still row A's declared
      one -- that concession is NOT withdrawn -- but the attribution is now
      to an object of row B.
  R5 (no interface with the sign) ........ ANSWERED WITH ITS LIMITS,
      section 8bis: the GRAM FORM of the Frobenius family is computed
      (Thm 8bis.1) [ROUND 4: and is only its FINITE half W_fin -- see the
      round-4 block at the head of this section];
      primitivity is TWO EXPLICIT LINEAR CONDITIONS on the coefficients
      (8bis.8).  Thm 8bis.2: the regularized self-intersection of the
      diagonal DIVERGES TO -infinity (rate computed, driven by
      W_infinity-hat ~ -log|tau|) -- "the arithmetic curve has infinite
      genus", an interpretation labelled as such.  Thm 8bis.4: Weil
      positivity IMPLIES the Hodge index on this class (PROVED, one
      direction); the converse needs a density statement which is OPEN,
      and the usual "gaps -> 0" argument is shown to FAIL in a fixed
      window.  ROW B DELIVERS THE GRAM FORM, NOT THE SIGN.

  NO SIGN, NO POSITIVITY, NO N_infinity = 0, AND NO STATEMENT ABOUT ANY
  ZERO outside the single clause Thm 8bis.4(ii), which is labelled
  CLASSICAL, is cited rather than proved, and is used only to obtain the
  one direction of Thm 8bis.4(iii).

  CLAUSES AFTER ROUND 3 (changes from round 2 marked *):
  B.1 PROVED* -- source = (N,x) with its divisor poset AND its inverse
      semigroup completion (Thm 3ter.7); the dagger now HAS a home.
  B.2 PROVED* on the label monoid, and now NON-VACUOUSLY: the Frobenius
      realization does not factor through the modulus (Rem 3ter.4a).
  B.3 PROVED* with a TRUE UNIT (Thm 3ter.4(ii)) and the degree relation
      Frob_n * Frob_n^dagger = Delta^(n) (Thm 3ter.6(ii)).
  B.4 REFUTED AS STATED; PROVED AS AMENDED, amendment ACCEPTED by the
      author, and now PROVED ON OBJECTS* (Thm 6bis.4).
  B.5 PROVED twice and the two proved equal; n=1 as excess.
  B.6 BOTH HALVES PROVED, both non-vacuous* (Thms 3ter.12, 3ter.14).
  B.7 PROVED as a TEST; PARTIAL as a MECHANISM (unchanged; Rem 6.5a').
  B.8 PROVED.  B.9 PROVED, independence inherited from row A.
  STILL OPEN, unchanged: the functorial arrow of P123.038 section 5 /
      P123.039 section 5 (cyclic extension to mixed correspondences,
      comparison with the analytic NUCLEAR trace as a trace functor);
      the density statement of Thm 8bis.4(iv); object-level realization
      in a C-linear category REFUTED (P123.022).

  LABEL: NOT SELF-GRANTED AND NOT CLAIMED.
```

```text
ROW B, after phase 131 round 2 -- SUPERSEDED BY THE BLOCK ABOVE, kept as
the record (repairs to R131.002 F1-F13 and R131.003 F1-F5; disposition of
every finding in R131_004):

  WHAT ROW B IS.  A theorem about ROW A's TRACE RESTRICTED TO THE RADIAL
  (MODULUS) SECTOR, plus a Z-linear side that is not in G and says so,
  plus two genuine corrections.  It is NOT the construction of an object
  of G that carries factorization data: by Lemma 3bis.3b no such object
  exists on the radial sector, and the paper now says this in the first
  paragraph of section 3bis instead of implying the opposite.

  B.1  PROVED, trivially and on the reading "no functor into G demanded";
       the source W has NO DAGGER as declared (Thm 3bis.5(ii)).
  B.2  PROVED on the label monoid, WITH THE EMPTINESS NOTE: the
       realization factors through (R_>0,x) and forgets factorization
       (Lemma 3bis.3b, Rem 3bis.5b).  Independence of lift/gauge/chart
       PROVED, re-proved in round 2 without the refuted idele projection.
  B.3  PROVED after extending the source to the group completion
       Q_>0^x, which is what the dagger forces (Thm 3bis.5(ii)).
  B.4  REFUTED AS STATED; PROVED AS AMENDED, with the amendment RE-WORDED
       in round 2 around the representing measure omega_fin (T is
       UNDEFINED on point masses and naive evaluation gives 0).
       The amendment remains a PROPOSAL for decision.
  B.5  PROVED twice and the two proved equal; n=1 handled as excess.
  B.6  first half PROVED but VACUOUS FOR COMPOSITE n (Rem 3bis.5b(d));
       second half PROVED (Thm 8.3, strong-dual convergence).
  B.7  PROVED as a TEST; PARTIAL as a MECHANISM.  No map is supplied
       between the shell volume and Phi_{p^k}(1) (Rem 6.5a').
  B.8  PROVED.   B.9  PROVED, with the independence INHERITED from row A
       (Rem 3bis.8b): the Lambda-as-shell-volume reading is Paper 43
       Rem 9.7a's; row B's addition is to attach it to the family and to
       its contact locus (Thm 3bis.7').

  STILL OPEN (one item, not two; see Rem 3bis.10b for the full
  quotations of P123.038 section 5 and P123.039 section 5):
       the lattice-index OPERATION as an admissible diagonal shadow
       EXTENDED CYCLICALLY TO MIXED CORRESPONDENCES and compared with
       the analytic NUCLEAR trace, preserving composition and analytic
       test action.  Row B supplies a comparison of DEGREES only
       (Thm 3bis.10(ii)), and P123.039 section 5 states in advance that
       "a collection of equal trace values is insufficient for those
       functorial claims".  Object level: REFUTED for additive C-linear
       contact functors (P123.022); OPEN for an integral carrier.

  WHAT THE BUILDER BELIEVES THE MATHEMATICS EARNS:
      ROW B: CLOSED ON PAPER 43'S DECLARED CARRIER, AS A THEOREM ABOUT
      ROW A'S TRACE RESTRICTED TO THE RADIAL SECTOR, MODULO THE OWNER'S
      ACCEPTANCE OF THE RE-WORDED B.4 AMENDMENT; B.7 PARTIAL as a
      mechanism; the P123.038 section 5 functorial arrow OPEN.
  The label WEIL-STRENGTH-COMPLETE is NOT self-granted and is NOT
  claimed: the closure rule reserves it to an adversarial audit, and the
  round-1 adversarial audit graded it NOT EARNED.  Whether the round-2
  repairs convert that grade is the auditor's call, not the the construction's.

  NOT claimed anywhere: any statement about zeros; any sign or
  positivity; that Z/Phi_n(1) is an object of G; that the integral
  contact is realized as a shadow of G; that Gamma_n^rad is primitive
  (Thm 8.3(v) says it is NOT); that N_infty = 0; that T is defined on
  point masses.
```

**Ruling of the adversarial audit of record (
[R131.005](../../03-research/phase-131-row-b-closure/R131_005_FINAL_AUDIT_AND_LABEL.md)).**  B.7: `PROVED` — the mechanism producing the factor that enters
row A's trace (`log p` = shell volume, Thm 6.5) is located on the carrier, the
cyclotomic mechanism is located on `G_m/Z` (Thm 6.4), the degrees agree, and a
map between the two locations is *refuted* (P123.022), not open.  The
P123.038 §5 / P123.039 §5 arrow: closed in degree, refuted at object level on
the declared `C`-linear carrier; "an integral carrier" is a different theory.
Renaming test: pass.  Label:

```text
ROW B: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier,
       CONDITIONAL ON THE OWNER'S ACCEPTANCE OF THE B.4 AMENDMENT
       (section 6.2a'; PLAN section 6 item 4).  If rejected: B.4 stands
       REFUTED on this carrier and row B is CONSTRUCTED.
```

Every finding of the phase-128 audit, my verification of it and its
disposition are in
[D128.002](../../03-research/phase-128-adversarial-audit/D128_002_AUDIT_B.md);
the phase-131 withdrawals are in §9bis.  The round-1 adversarial audit
`R131.002` (`F1`–`F13`), the final audit `R131.003` (`F1`–`F5`) and the
disposition of every one of their findings are in
[R131.004](../../03-research/phase-131-row-b-closure/R131_004_ROUND2.md).
The clause table below is corrected again in round 2.

| clause | status | where |
|---|---|---|
| B.1 source category | **`PROVED`**.  **[REBUILT, phase 131, round 3:]** the source is `W = (N_{≥1},×)` with its divisor poset **together with its inverse-semigroup completion** `𝔉` of Thm. 3ter.7 — pairs `(r,F)`, `r ∈ Q_{>0}^×`, `P(r) ⊆ F` finite — which is where the dagger lives (Thm. 3ter.6) and whose idempotents `Δ^{(F)}` form the semilattice `(𝒫_{fin}(S_f),∪)`.  Round 2's note "the declared source has no dagger" is thereby **answered**, not merely recorded.  With the honest sentence: `W = (N_{≥1},×)` with its divisor poset is stated with objects and morphisms; the **symmetry is realized** (`C_S` is abelian, `G` is commutative on the radial sector, Thm. 3bis.5(i)); the **divisor arrows are realized** on the `Z`-linear model `Q_{S,·}` (P123.038 §3) and on the norm classes as divisibility of moduli, and have **no** morphisms in `G` (P123.082) — which B.1 as written does not ask for.  **[REBUILT, phase 131: upgraded from `PARTIAL`.  Round 2, findings `F1`,`F7`: the upgrade is defensible **only** on the reading "no functor into `G` is demanded", stating a category being otherwise free; and the declared source `W` has **no dagger**, so B.3's transposition is realized only after extending to the group completion `Q_{>0}^×`.]** | Def. 4.1, Thm. 4.3, Thm. 3bis.5, Rem. 3bis.5a, 3bis.5b |
| B.2 monoidal realization | **`PROVED on the label monoid`, and NON-VACUOUSLY since round 3.**  **[REBUILT, phase 131, round 3:]** the **Frobenius** realization `n ↦ Frob_n` is strong monoidal with a **true unit** `Frob_1 = Δ` (Thm. 3ter.4), is **injective**, and its objects determine `(n,P(n))` (Thm. 3ter.4(iv)); it does **not** factor through the modulus, and no weak-⋆ continuous one-parameter family interpolates it (Rem. 3ter.4a).  The emptiness note below applies to the **radial** realization only, and `Γ_n^{rad} = Frob_n⋆Δ^{rad}` (Prop. 3ter.5) exhibits exactly the projector that loses the information.  Round 2's reading, kept:  **[REBUILT, phase 131, round 2, finding `F1`.]**  The realization factors as `(N_{≥1},×) ↪ (R_{>0},×) ≅ {level measures}` and therefore **forgets factorization as an object** (Lemma 3bis.3b, Rem. 3bis.5b); it is true with `n` replaced by any positive real.  What is realized is the monoid inside the modulus group; the divisor structure is realized on the integral model `Q_{S,·}` and **detected** on the carrier by the contact locus (Thm. 3bis.7′, Thm. 3bis.10(ii)).  Independence of lift, gauge, uniformizers and chart `PROVED`, re-proved in round 2 (`F10`) from the modulus alone and the inflation functor, **without** the idele projection `A_T^×→A_S^×` that P123.018 §2 refutes.  Two levels, both stated: smeared classes in `D_A^{rad} ⊂ Corr_A^{tr}`, point classes in `N_A^{dist}` (Rem. 3bis.5c) | Thm. 4.3, Lemma 3bis.3b, Thm. 3bis.5(i),(iv), Rem. 3bis.5b, 3bis.5c |
| B.3 unit, transpose, half-density | **`PROVED`, with a TRUE unit since round 3.**  **[REBUILT, phase 131, round 3:]** `Frob_1 = Δ = E_1` is the diagonal itself, a point mass, **not** a projector (Thm. 3ter.4(ii)); `Frob_n^†` is the Frobenius at `n^{−1}` and `Frob_n⋆Frob_n^† = Δ^{(n)}`, the averaged half-density-normalized form of Weil's `Γ_F⋆Γ_F^t = qΔ`, with `Δ^{(n)} ≠ Δ` recorded explicitly (Thm. 3ter.6(ii),(iv), Rem. 3ter.6a); bidegree `M(Frob_n) = (n^{1/2},n^{−1/2})`.  The round-2 statement for the radial family, kept:  **[REBUILT, phase 131, round 2, finding `F7`.]**  Unit `Δ^{rad} = Γ_1^{rad}` (the unit-averaging projector, identity on the radial sector, `†`-fixed) and bidegree `M = (n^{1/2},n^{−1/2})`: `PROVED` outright.  Transposition: `(Γ_n^{rad})^† = Γ^{rad}_{(−\log n)}`, which is **not** a `Γ_m^{rad}`, so the realized family is `†`-stable only after passing to the group completion `Q_{>0}^×`; B.3 is proved for that `†`-monoid, and the declared source `W = (N_{≥1},×)` has no dagger.  The round-1 sentence "`†`-real because positive" is **deleted**: `μ^† = μ` is false for every `n ≥ 2` | Thm. 4.4, Lemma 4.5, Cor. 4.6, Thm. 3bis.5(ii),(iii) |
| B.4 derived contact in the declared category | **`REFUTED AS STATED`; `PROVED AS AMENDED`; amendment ACCEPTED by the author ; and since round 3 PROVED ON OBJECTS.**  **[REBUILT, phase 131, round 3:]** Thm. 6bis.4 proves `contact_{fin}(Frob_n) = n^{−1/2}deg_det Prim(Sh_Z)_n` and `deg_det Sh_Z(Frob_n) = \log n = Σ_{d|n}d^{1/2}contact_{fin}(Frob_d)`, both sides attached to the **object** `Frob_n` — the left by Cor. 3ter.11, the right through the integral shadow `Sh_Z` of Def. 6bis.1, well defined on the measure by Lemma 6bis.2.  `Sh_Z` is the integral/lattice structure P123.022 §2's *Scope* says must be constructed; its complex realization is **acyclic**, so P123.022's refutation is untouched and the identification is of **degrees**.  Round-2 reading, kept: **`REFUTED AS STATED`** (`LΔ^*Γ_n` is the fixed complex, differential `n−1`; the models of Thm. 6.3 are not operations on `Γ_n ∈ G`); **`PROVED AS AMENDED`** — the amended clause, its wording and its proof are §6.2a′ and Thm. 6.3a.  The amendment is a **proposal for decision**, mirroring Paper 43's A.6 decision; the object-level realization stays **`REFUTED`** for additive `C`-linear contact functors (P123.022) and **`OPEN`** for an integral carrier | §6.2a, §6.2a′, Thm. 6.3a, Thm. 6.3 |
| B.5 `deg_det = log|Φ_n(1)| = Λ(n)`; `n=1` as identity/excess | **`PROVED` twice, and the two are proved equal**: as a shell volume in the declared category (Thm. 3bis.7, `Λ(p^k) = log p = vol(p^kZ_p^×)`) and on the `Z`-linear models (Thm. 5.3); the equality is Thm. 3bis.10(iii).  `n = 1`: `Γ_1^{rad} = Δ^{rad}`, treated as identity/excess by the `c·F(1)` term of Paper 43 (8.4) with `c := 0`, and excluded from `ω_{fin}` by construction — not by the degree formula | Thm. 3bis.7, Def–Thm 3bis.8, Thm. 3bis.10, Thm. 5.3 |
| B.6 general family by structure; classes in `N_A` | **both halves `PROVED`, and since round 3 both NON-VACUOUS.**  **[REBUILT, phase 131, round 3:]** for the Frobenius family the composite case is a **theorem about the object**: `supp\,Frob_n` meets **no** fixed-point stratum when `n` is composite, and **is** the whole shell when `n = p^k` (Thm. 3ter.12, Rem. 3ter.12a); `Frob_4` and `Frob_6` are distinguished before any trace is computed (Thm. 3ter.4(iv)).  Classes in the numerical object: `Frob_n ∈ N_A^{dist}` with strong-dual convergence, canonical primitive component and **nonzero** ruling component (Thm. 3ter.14) — so the Frobenii are **not** primitive, and no positivity is claimed.  Round-2 reading for the radial family, kept:  **[REBUILT, phase 131, round 2, finding `F1`.]**  First half: no case analysis (Prop. 7.1, Thm. 3bis.5 and 3bis.7 hold for all `n`), but by Lemma 3bis.3b the composite members of the family carry no structure distinguishing them from a generic `Γ^{rad}_{(t)}`; the content for composite `n` is the **absence** of an atom in `ω_{fin}` (Thm. 3bis.7′(iii)), which is a statement about the contact locus, not about the object.  Second half: `𝓝 = 0` and `N_A = D_A` are theorems of Paper 43 (Thm. 9.8); `Γ_h ∈ D_A^{rad} = N_A^{rad}` for smooth `h`; `Γ_n^{rad} ∈ N_A^{dist}` with convergence proved **in the strong dual**, canonical primitive component `(I_A(Γ_n^{rad},·),0)` and moments `λ_± = n^{∓1/2}` | Prop. 7.1, Thm. 8.1, **Thm. 8.3** |
| B.7 discriminating test `p`, `p²`; mechanism located | **`REFUTED AS STATED` + `PROVED AS AMENDED` (author).**  **[phase 133, amendment accepted ; this verdict read "`PROVED` (the test and, per the earlier ruling, the mechanism on the carrier); the map to the `Z`-model `REFUTED`, not open", which is kept verbatim below together with the auditor's dissent as the record of how the decision was reached.]**  Previous verdict, kept as history: **`PROVED` (the test and, per the earlier ruling, the mechanism on the carrier); the map to the `Z`-model `REFUTED`, not open.**  **[REBUILT, phase 131, round 4 — instruction `L4` of `R131.009`; the earlier ruling `R131.005` §2 is adopted and the adversarial auditor's dissent is recorded verbatim beside it, as Paper 43 §10.3.3 does for A.8.]**  *Lead's ruling (`R131.005` §2, adopted here):* `PROVED` for test and mechanism on the carrier — Theorem 6.5(i)–(ii) locates the mechanism as the triviality of the fixed-point weight on the shell together with the `k`-independent Haar volume; the passage to `Φ_{p^k}(1)` on `G_m/Z` is **`REFUTED`** at object level by P123.022, and a refutation is not an open item.  *Auditor's dissent, verbatim (`R131.008` §4, B.7):* "`PROVED` as a test; `PARTIAL` as a mechanism, as the paper says. I do **not** endorse `R131.005`'s upgrade to `PROVED`: Rem. 6.5a′ is still the truth (F10)."  *Construction's note:* Remark 6.5a′ is **kept unchanged**, so a reader who follows the auditor reads `PARTIAL` there and loses nothing; no theorem of this paper depends on which grading is adopted.  Round-3 reading, kept below:  **[REBUILT, phase 131, round 2, finding `F5`.]**  *The test*: the two contacts differ decisively at `p` and `p²` — `0` versus `Z/p` in the `p`-primary part (Thm. 6.4) — and no determinant is substituted for another.  *On the carrier*, what is proved is precisely two things: the fixed-point weight `1/|1−x|_p` is identically `1` on the shell `p^kZ_p^×`, and the surviving weight `\log p = vol_{d^*x}(p^kZ_p^×)` is `k`-independent by translation invariance of Haar measure (Thm. 6.5(i)–(ii)).  *The mechanism* is `PARTIAL`: it is located on `G_m/Z` as deck `μ_n` versus fixed `μ_{n−1}` (Thm. 6.4(iv), Lemma 3.1), and on the carrier only as the shell volume, and **no map, functor or comparison between the two locations is supplied** — `Φ_{p^k}(1) = p` holds because `Φ_{p^k}(x) = Φ_p(x^{p^{k−1}})`, an unrelated reason (Rem. 6.5a′).  By P123.039 §5 a coincidence of constants does not locate a mechanism; PLAN §6's stopping rule is met for the test, not for the mechanism.  **[phase 133: the review panel (PANEL_3 §3) sides with the dissent; the author's decision on an amendment is decided: amendment accepted.]**  **[phase 133, amendment accepted : the repository author (D. Trejo Pizzo) accepted on  the amendment of B.7 proposed in PANEL_SYNTHESIS §4.2 — "the discriminating test at `p, p²` is `PROVED`; the mechanism is located on the carrier (shell volume, trivial fixed-point weight, Thm 6.5) and on the `Z`-model (deck `μ_n`, Thm 6.4(iv)); a map between the two locations is `REFUTED` on a `C`-linear carrier (P123.022), so the clause's demand for a single mechanism producing the cyclotomic factor is unsatisfiable as stated."  The the earlier ruling `R131.005` §2 is superseded by the author's decision; the auditor's dissent above is kept verbatim as history; Rem. 6.5a′ is unchanged; the row-B label stands unconditionally.  No theorem and no proof of this paper changes.]** | Thm. 6.4, **Thm. 6.5**, **Rem. 6.5a′**, Thm. 3.3, Lemma 3.1, Rem. 6.5a |
| B.8 adversarial `p,p²,p³,pq,p²q,pqr`; places preserved | `PROVED`, with the table extended by the columns the contract is about (the atom of `ω_{fin}`, the archimedean density, the bidegree) and the `w` columns re-labelled "of the lift" | Section 7, and `scripts/verify_131_contacts.py` for the numerics |
| B.9 compatibility with A; independence | `PROVED`, **with the independence inherited, not earned**.  **[REBUILT, phase 131, round 2, finding `F9`.]**  Compatibility rests on Paper 43 (8.5), Thm. 8.8, Lemma 8.2, Thm. 8A.7c, Thm. 8A.9, Thm. 9.1, Thm. 9.7, Thm. 9.8, Thms. 9.14–9.14b — cited exactly.  Independence: no zero, no RH, no sign, no positivity, and no von Mangoldt input.  The reading `Λ(p^k) = \log p = vol(p^kZ_p^×)` is **Paper 43 Rem. 9.7a's**, with the same P123.042 §1 justification and the same declared normalization; row B **inherits** it and adds only its attachment to the family and its contact locus (Thm. 3bis.7′) | Thm. 8.2, Rem. 3bis.8b, Rem. 3.7 |

**Former open items now closed or reclassified.**

| item | source | disposition |
|---|---|---|
| fixed vs ramification contact not quasi-isomorphic | P123.060 §3–4 | correct, and **not an obstruction**: coprime support, Thm. 3.3 |
| **the lattice-index operation as an admissible diagonal shadow, extended cyclically to mixed correspondences and compared with the analytic *nuclear* trace** | P123.038 §5, P123.039 §5 | **`PARTIAL`.**  **[REBUILT, phase 131, round 2, finding `F3`.  Round 1 split this single item into two rows and marked both `PROVED`; `D128.002` `B2` had restored both halves as open, so that was a ledger regression.  One row, restored.]**  *Proved:* the comparison of **degrees** with the analytic trace, `\log[L_S:nL_S] = \log n = Σ_{d|n}d^{1/2}contact_{fin}(Γ_d^{rad})` (Thm. 3bis.10(ii)); and (6.1), which is a **definitional** identity (`D128.002` `B2`, unchanged).  **[REBUILT, phase 131, round 5, finding `M6`(a) of `R131.011`: rounds 3–4 twice announced that this row had been re-graded and twice did not do it.  It is re-graded now, per Thm. 6bis.3c and the earlier ruling `R131.005` §2.]**  *Also proved since round 4:* the **cyclic extension to mixed (finite-combination) correspondences** — Thm. 6bis.3c(ii), where `Z[𝔉^+]` is the monoid ring of a **commutative** monoid, so cyclicity is automatic **and the paper says it is automatic**; and the **linear** comparison (6bis.5) of `n^{1/2}contact_{fin}` with `deg_det Prim(Sh_Z)` on that group, where the analytic side is Paper 43's trace on genuine elements of `D_A` (the smeared Frobenii).  *Still open:* the trace **functor** itself; the comparison with the analytic **nuclear** trace as such; preservation of composition and analytic test action; the joining of unit, archimedean and Tate sectors.  *Refuted at object level, NOT open:* an additive `C`-linear contact functor producing these complexes (P123.022 §2; Thm. 6bis.3c(iv)).  P123.038 §5 and P123.039 §5 are quoted **in full** in Rem. 3bis.10b, including "an invariant of the arithmetic family does not itself provide that trace functor" and "a collection of equal trace values is insufficient for those functorial claims" — which is exactly why this paper claims degrees only |
| "`T_n` is the finite translation, not the external dilation `E_n`" | P123.039 §5 | not identified, and not resolved: both produce `L_S/nL_S`, which is a coincidence of finite quotients, not a map (Thm. 6.1, Thm. 6.3(c)).  **[REBUILT, phase 131, round 2, `F3`/`F5`:]** folded into the row above; `PARTIAL` |
| "primitive extraction has not been shown to commute monoidally" | P123.037 §5, P123.038 §5, plan §6.6 | `REFUTED as a requirement`: Thm. 5.4; corrected structure in Cor. 5.5 |
| divisor arrows have no morphisms in `G` (P123.082) | P123.082 (1) | not needed: the cube lives on the shadow target, Remark 5.6 |
| "`h ↦ A_h(r)` does not preserve convolution" | P123.039 §5 | `OPEN`, reassigned to row C, §9.1 |
| the `n−1` factor | P123.060 §4 | **[REBUILT, phase 131]** a quantity of the **lift** `a_S(n)`, not a contact: the class is on no finite slice (Prop. 3bis.2, Cor. 3bis.3).  The row C obligation is **withdrawn** (§9bis W1) |
| "realization of the integral contact as a shadow of `G`" | Paper 44 phase 128 | still `OPEN` for an integral carrier and `REFUTED` at object level for additive `C`-linear functors (P123.022).  What is now proved is the **degree** identity, Thm. 6.3a |
| "what the family's pairings equal in terms of `Λ(n)`" | **row B's own question** (§8 Thm. 8.1(iv)), prompted by Paper 43 Rem. 9.7a (`Λ(p^k)=\log p` as a shell volume in `T̂`).  **[phase 133, PANEL_2 MAJOR-1: the source column read "Paper 43 Rem. 9.5", which does not exist; no statement of Paper 43 poses this question.  The verdict column is unchanged — the obligation is discharged by row B's own theorem.]** | `PROVED`: `contact_fin(Γ_n^{rad}) = Λ(n)n^{−1/2}`, Thm. 3bis.7 |
| the lift ambiguity of extension-by-one | P123.018 §2 | removed on the norm classes **by construction** (unit averaging), Thm. 3bis.5(iv) |

**Adversarial audit of this paper — [REBUILT, phase 131].**  The load-bearing
new statements of this phase are **Lemma 3bis.1**, **Proposition 3bis.2** and
**Theorem 3bis.7**.  An auditor should press hardest on:

1. *Lemma 3bis.1.*  Is the class of `a_S(n)` really `δ_S(1/n)`?  If the
   canonical representative were different, §3bis would collapse.  The proof
   is three lines from Paper 43 Lemma 3.3; check that `n ∈ Γ_S` (it is,
   because `S ⊇ P(n)`) and that `|x|_S = |x_∞|` on `ker φ`.
2. *Theorem 3bis.7's unit packet.*  The claim that the packet vanishes
   **identically** on radial sections rests on `a = Γ_h∘j_p` being constant on
   `Z_p^×`, which follows from `|j_p(w)|_S = 1` for `w ∈ Z_p^×`.  If that were
   wrong, `Λ` would acquire a unit correction.
3. *The type of `Γ_n^{rad}` (Remark 3bis.4b) and Theorem 8.3(ii).*  The
   strong-dual convergence is the one genuinely analytic step in §3bis; the
   `R`-then-`ε` argument uses Paper 43 Lemma 9.14a0's **proof**, not only its
   statement.  If Lemma 9.14a0's uniform bound failed, Theorem 8.3 would drop
   to pointwise convergence and B.6's second half would become `PARTIAL`.
4. *Theorem 6.3a as an amendment.*  Is a **degree** identity an acceptable
   reading of "the derived contact identified with `[Z→Φ_n(1)→Z]`"?  This is
   the author's decision and the paper does not pre-empt it.
5. *The renaming test.*  `T(Γ_h)` of (9.1) **is** the prime-power-plus-Gamma
   side of the explicit formula.  Paper 43 Remark 9.7a's three answers apply
   verbatim here, and the crucial one is that `Λ` is **derived** as a shell
   volume (Remark 3bis.8b); an auditor who does not accept that will not
   accept row A either.

The previous audit paragraph is kept below, unchanged, as the record of the
phase-128 state.

**Adversarial audit (phase-128 record, kept).**  The single load-bearing new
statement is Theorem 3.3, and its proof uses only: the definition (1.1) of the local factor
(proved in P123.042–060), the elementary implication `p|n ⟹ p ∤ n−1`, and the
product formula.  If (1.1) were wrong, Paper 43 §8 and row A would fall with
it; nothing here is more fragile than row A.  The four constructions of
Theorem 6.3 are independent (cotangent cube, arithmetic lattice cube, orbit
determinant, deformation Koszul) and agree, which is the strongest internal
check available.  Theorem 5.4 is a one-line refutation and should be checked
first by any reader who doubts the reclassification.  The weakest link is not
in B but in what B hands to C: §9.2 is a genuine new obligation and it is
labelled `OPEN`, not absorbed.

---

### 10.4 Lead decision of record (R131.019)

> **ROW D'S TARGET (boxed identically in Paper 43 §14.1, Paper 44 §8bis.4(vi)
> and §10.4, and Paper 45 §14.4).**  **[phase 133, PANEL_2 §5 / PANEL_3
> recommendation.]**
>
> **ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and c = 0 (Paper 45 Cor 9.6a); this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4. Standing negatives: Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a; Paper 44 Thm 8bis.7 is conditional under (H_L), OPEN.**


**[Inserted by the final audit as audit of record; supersedes the conditional
decision R131.005 and the round-2 ruling block.]**

    ROW B: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier
           (§14.0a–b), as a theorem about row A's declared trace.
           B.4 amended (author); B.7 amended (author) [phase 133, amendment accepted ; this
           line read "B.7 by ruling with the adversarial auditor's
           dissent recorded verbatim (§10 table)", and that dissent is
           kept verbatim in the §10 table as history].
           Granted  after construction rounds 1–7 and adversarial audits
           R131.002/.008/.011/.014/.017, the last grading the label EARNED
           conditional on apparatus items verified by grep in R131.019 §1.

Recorded beside the label:

1. *Reservations of R131.005.* R1, R3, R6 dissolved by theorems (Thm 3ter.4(iv),
   Thm 3ter.12, Rem 3ter.4a); R2 dissolved in degree on the monoid and
   **refuted** at object level (P123.022), not open; R4 dissolved in the only
   available form — uniqueness of `vol(Z_p^×) = \log p` given a universal Tate
   residue, up to one global scale (Thm 8bis.8), the requirement being an axiom
   of the carrier; R5 answered in the form that is true (Thm 8bis.1e: the Weil
   kernel is the Gram form of `Frob ⋆ Δ^{rad}`) and not dissolvable, because it
   asks for a sign.
2. *Not delivered.* No sign, no positivity, no `𝓝_∞ = 0`, no statement about
   zeros outside Thm 8bis.4(ii)–(iii) and §8bis.3–8bis.4; two quarantined
   `CLASSICAL` imports — Weil's **criterion** (Thm 8bis.4(iii)) and Chebyshev —
   each used by no clause of B.1–B.9. The sign is row D's.
   **[phase 132]** The **explicit formula** of Thm 8bis.4(ii), formerly counted
   as half of the first import, is `PROVED-IN-REPOSITORY` (Paper 45 Thm 9.4)
   and is no longer an import at all.
3. *Quantifiers.* The interface with Weil's criterion is a colimit statement
   (`T_∞` on `D_A^∞`, (C1)) and is false at a finite chart; no divergence rate
   of the Frobenius diagonal is convention-free ((C2), Cor 8bis.1b′) — what is
   stated is that `I_A(Frob_n,Frob_n)` does not exist; Thm 8bis.2 and
   Thm 8bis.4a are fixed-chart theorems, the colimit version of 8bis.4a `OPEN`.
4. *Withdrawals of record.* `(Wgr)` withdrawn as false (Lemma 8bis.6b, W23);
   "positivity on Dirichlet-polynomial profiles ⟹ RH" is `OPEN` — Thm 8bis.7 is
   a conditional transfer theorem under `(H_L)`. W16–W23 record every retracted
   round-3/4/5 claim.
4a. *Cross-paper record.* **[phase 132]** Row C (Paper 45, phase 132) received
   **§9.1** (the prime packet, whose content is Thm 3bis.7) as its Thm 5.1 and
   (C1) as its standing convention **[phase 133, PANEL_2 MINOR-4: this read
   "Thm 9.1"; this paper has no Theorem 9.1 — the prime packet is **§9.1**.
   §9.1a and Paper 45 §14.3 already say "§9.1"]**; the explicit
   formula imported at Thm 8bis.4(ii) is now proved in the repository as
   Paper 45 Thm 9.4, and that clause is relabelled `PROVED-IN-REPOSITORY`.
   Weil's criterion, Thm 8bis.4(iii), stays `CLASSICAL`.
5. *Honesty about Weil's proof.* Row B constructs the objects Weil's proof needs
   on `Spec Z` — correspondences, Gram form, integral shadow — not the section
   theory with nonnegative dimension that turns Riemann–Roch into an
   inequality; that is the content of RH and belongs to row D.

## 11. Dependencies

Inside the repository: P123.008, P123.012, P123.016, P123.019, P123.020,
P123.022–025, P123.037, P123.038, P123.039, P123.042–046, P123.060, P123.061,
P123.064, P123.073, P123.074, P123.082, P123.084, P123.105, P123.107–110,
P123.121; `P123_A_ACCEPTANCE_SPECIFICATION.md`;
`05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md` §6.
Papers: [Paper 43](../43-row-a-torsion-theory/main.md) (rows A; §§3, 5, 7–9,
Def. 8.6 with (8.5)/(8.5∞) — **not** the withdrawn Def. 8.1 of §13.6 —
Thms. 9.1, 9.3, 9.4, 9.5, Remark 9.6) and its
[appendix](../43-row-a-torsion-theory/appendix.md).
**[phase 133, PANEL_2 MAJOR-1: "Remark 9.5" does not exist in Paper 43;
corrected to Theorem 9.5 and Remark 9.6, which are what is meant.]**
Paper 45: [Paper 45](../45-row-c-explicit-formula/main.md) — Thm. 5.1,
Lem. 5.1a, Thm. 8.1, **Thm. 9.4** (the explicit formula, `PROVED` there and
cited in §8bis.4(ii) and §10.4), Thm. 10.4 (`Π = −∂_t²+¼`, sufficiency),
Rem. 10.3.  **[phase 133, PANEL_2 MINOR-7: §11 listed Paper 43 only, while
§§8bis.3–8bis.4 and §10.4 cite Paper 45 substantively.]**
Phase 126 record: `03-research/phase-126-row-b-completion/`.
Phase 128 audit: `03-research/phase-128-adversarial-audit/`.
Phase 131 record: `03-research/phase-131-row-b-closure/` — **[REBUILT, phase
131, round 5, finding `m7`: the list was stale at round 1.]**  blueprints
`R131_000` (round 1) and `R131_006` (round 3); construction memo `R131_001`
(round 1), `R131_004` (round 2), `R131_007` (round 3), `R131_010` (round 4),
`R131_013` (round 5); adversarial audits `R131_002` (round 1), `R131_008`
(round 3), `R131_011` (round 4); final audits `R131_003`, `R131_005`
(final audit and label ruling), `R131_009`, `R131_012`; numerical checks in
`scripts/verify_131_contacts.py`.
Paper 43 sections used in §3bis and §8: Def. 3.1, Lemma 3.3, Cor. 3.4,
§7.1 Thm. 7.1/Rem. 7.3, Def. 8.5, Def. 8.6 with (8.5), (8.5a), (8.5b),
(8.5∞), Lemma 8.2, Thm. 8.8, Rem. 8.11, Thm. 8A.7c, Def. 8A.7d, Thm. 8A.9,
Thm. 9.1, (9.5b), Thm. 9.7, Rem. 9.7a, Thm. 9.8, (9.13), (9.14), Thm. 9.14,
Lemma 9.14a0, Thms. 9.14a–b, Thm. 14.1, §14.0a–b, §14.1a.

**External inputs.**  **[REBUILT, phase 131, round 5, finding `M6`(b) of
`R131.011`: the previous line read "External inputs: **none**", which round 4
made false.]**

  * **In clauses B.1–B.9: two elementary `CLASSICAL` facts, in clause B.4
    only.**  **[phase 133, PANEL_1 finding B1: this bullet read "**none**.
    Row B's contract is discharged with no external citation", which is false
    for the amended B.4.]**  Theorem 6bis.4, which is the whole of clause
    **B.4** as amended, is proved from
    (α) `Φ_n(1) = p` if `n = p^k` is a prime power and `= 1` otherwise, hence
    `\log|Φ_n(1)| = Λ(n)` (used in Theorem 6bis.3(v)), and
    (β) `\log n = Σ_{d|n}Λ(d)`, equivalently `Λ = μ ∗ \log` (Corollary 5.3a).
    Both are elementary classical number theory, neither is proved in this
    repository, and neither was in any import table.  They are labelled
    **`CLASSICAL`**; no verdict is at risk, since B.4's content is the
    *identification*, not either fact.  Clauses B.1–B.3 and B.5–B.9 use no
    external citation.  **[phase 133, PANEL_1 finding B2: the clause "adds
    none to the **one** import (`W`, Wodzicki excision) recorded in Paper 43
    §12" misstated Paper 43, whose §12 records four rows — `M`, `W`, `C`, `RR`
— plus the transfer `Tr` added in phase 133, and says in terms "Count.
    Three, not one".  Corrected:]**  row B adds nothing to the imports
    recorded in Paper 43 §12.
  * **In the quarantined §8bis.3–§8bis.4: TWO, both `CLASSICAL`, each used by
    no clause of B.1–B.9 and deletable without changing any verdict.**
    **[phase 132]** The **explicit-formula half** of this import is `PROVED-IN-REPOSITORY` since phase 132 (Paper 45 Thm 9.4); what remains `CLASSICAL` here is Weil's **criterion**, Thm 8bis.4(iii).
    **[REBUILT, phase 131, round 7, minor `p5` of `R131.017`: this bullet still
    said "three" and still numbered the list (i),(ii),(iii) with slot (ii)
    occupied by the round-6 withdrawal note.  §10, the README and `R131_016`
    all say **two**.  Corrected: the two live imports are listed as (i) and
    (ii), and the withdrawn `(Wgr)` is moved to its own line.]**
    (i) *Weil's criterion*, Theorem 8bis.4(iii), `CLASSICAL`.
    **[phase 133, PANEL_2 MAJOR-2: this item read "*Weil's criterion **and the
    explicit formula***, Theorem 8bis.4(ii)–(iii)", contradicting the
    `[phase 132]` sentence three lines above.  The **explicit formula**,
    Theorem 8bis.4(ii), is **`PROVED-IN-REPOSITORY`** (Paper 45 Theorem 9.4)
    and is no longer an external input; the count of external inputs in the
    quarantined §8bis.3–§8bis.4 is therefore **two** only if one counts
    Weil's criterion and Chebyshev, which is how (i) and (ii) now read.]**
    (ii) *Chebyshev's bound `ψ(X) ≤ cX`*, Lemma 8bis.5, with an unspecified
    absolute constant (the round-4 constant `4` presumed `ψ(X) ≤ X`, which
    fails for infinitely many `X` by Littlewood's theorem).
  * **Withdrawn, and cited nowhere: `(Wgr)`** — "Weil's growth estimate at a
    hypothetical off-line zero", imported in rounds 4–5 and **withdrawn as
    FALSE** in round 6 (§9bis W23, Lemma 8bis.6b).  Theorem 8bis.7 is now a
    conditional transfer theorem whose arithmetic hypothesis `(H_L)` is
    **`OPEN`**, not an import.
    Paper 43 Theorem 10.8b's use of Mertens is quarantined in the same way and
    is cited by this paper nowhere.


---

## 12. Corrections of record

Two mathematical defects of this document were found in an adversarial review
of its LaTeX rendering and are corrected above, in place and with a marker at
each site.  Nothing is relabelled: both statements remain `PROVED`, one after
a change of its content and one after the supply of a missing proof.

**K1.  Theorem 8bis.1: the convolution constant of the off-diagonal Gram
entry was wrong whenever `P(m) ≠ P(n)`.**

*What was stated.*  "the convolution of the level-`N` coset indicators
contributes the constant `∏_{s∈S_f∖F}vol(1+s^NZ_s)`, which is … `1` in the
normalized (`♭`) convention", `F = P(m)∪P(n)`, justified in the proof by the
single identity `1_{aU}⋆1_{bU} = vol(U)1_{abU}`.

*Why it is wrong.*  That identity covers only the places `s ∉ P(m)∪P(n)`,
where **both** smeared Frobenii carry a coset indicator.  At a place
`s ∈ P(n)∖P(m)` the first factor carries `1_{m^{−1}U_s}` while the second
carries **no condition**, i.e. the constant `1_{Z_s^×}`; their convolution is
`vol(U_s)·1_{Z_s^×}`, contributing a further `vol(U_s)` which the stated
constant omits.  Symmetrically at `s ∈ P(m)∖P(n)`.  At `s ∈ P(m)∩P(n)` both
factors are `1_{Z_s^×}` and the contribution is `1`.  Already for `m = 2`,
`n = 3`, `S_f = {2,3,5}` the stated constant is `vol(U_5)` and the true
constant is `vol(U_2)vol(U_3)vol(U_5)`.

*What replaces it.*  The constant

    c_N(m,n) = ∏_{s ∈ S_f ∖ (P(m) ∩ P(n))} vol(1+s^NZ_s)              (8bis.2b)

— complement of the **intersection**, not of the union — with the four-case
computation written out in the proof.  Consequently the `♭`-convention value
is `∏_{s∈S_f∖F}vol(1+s^NZ_s)^{−1}`, equal to `1` exactly when `F = S_f`, and
**not** `1` in general; the claim "`V_N^{(m,n)} = 1` in the `♭` convention" in
Corollary 8bis.1d and its note is corrected accordingly, with
`V_N^{(m,n)} := c_N(m,n)`.  At `m = n` the new constant is the `V_N(n)` of
(8bis.0), so the off-diagonal and diagonal constants are now given by one
formula, and Corollary 8bis.1b′ — which verified the case `m = n` — is
unaffected.

*What is unaffected.*  (8bis.2) and (8bis.2a) — the finite atom mass and the
archimedean indicator — are unchanged, as is the index set `F = P(m)∪P(n)` of
the composed object `Frob_{r,F}`.  So Theorem 8bis.1′(i), Corollary 8bis.1d's
qualitative content (the Frobenius Gram form carries `W_fin` and no
archimedean block) and Theorem 8bis.1e are untouched.  Only the scalar moved.

**K2.  The structure of `Prim_n` was asserted in two places, each citing the
other, and was never proved.**

*What was stated.*  Theorem 5.3 asserted `Prim_n ≅ Z/p` in degree `0` for
`n = p^k` and `Prim_n ≅ 0` otherwise, and proved only an identity of
**numbers** (an alternating sum of `deg_det`), which cannot yield `H^{−1} = 0`
or cyclicity of `H⁰`; Theorem 6.3(a) then deduced the structure by citing
Theorem 5.3.  Neither Lemma 5.1 (an identity of sums of group elements) nor
Theorem 5.3 (an identity of real numbers) can produce a statement about
cohomology.  The conclusion is true, but it was not proved, and it carries the
degree identity (6bis.3) through Theorem 6bis.3(v).

*What replaces it.*  A numbered **Definition 5.1a** of the radical cube and of
`Prim(N,P)`, `Prim_n := Prim(n,P(n))`, and a **Lemma 5.1b** proving
`Prim(N,P) ≃ Z/q` in degree `0` for `P = {q}` and `≃ 0` for `|P| ≥ 2`, by
induction on `|P|`: the base case is the cone of a degreewise injective map of
two-term free complexes, hence its degreewise cokernel; the step splits the
cube along one direction and, for `|P| = 2`, identifies the induced map as
multiplication by one prime on `Z/`(another prime), an isomorphism.  Theorem
5.3 is reduced to the degree statement and cites Lemma 5.1b; Theorem 6.3(a)
now cites Lemma 5.1b as well, and the loop is gone.

*A second point of hygiene recorded here.*  Theorem 6bis.3(v) spoke of "the
Möbius total cofiber over the divisor poset", while the object meant is the
total cofiber of the **radical** cube; for non-squarefree `n` these index
different diagrams.  The statement is to be read with Definition 5.1a.
