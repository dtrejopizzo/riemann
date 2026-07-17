# SURF-B — The operator T: survey against (T1)–(T4), and the symmetry-vs-positivity verdict

**Phase 17, SURF-B.** Follows `03-route2-testbed.md` (SURF-A collapsed into SURF-B; the single
hard object is the operator `T`). **Experiment:** `experiments/surfB_realstructure_vacuous.py`
(runs clean). **Date:** 2026-06-06.

> **Reformulated SURF-B (per the step-3 review).** Do **not** ask "what geometry produces `T`?"
> After Route-2 the central object is the operator, and the natural F-indep operators that
> produce the explicit formula are *few and already in the literature*. Ask instead:
>
> **Which existing F-indep operator survives the full catalogue (T1)–(T4), and does the
> real-structure constraint (T2) add any handle on the sign?**
>
> Catalogue (from `03`): (T1) spectrum `= {γ_ρ}`; (T2) intertwines the real structure `j`;
> (T3) resolvent obeys de Branges (dB2); (T4) F-indep (built from primes/explicit formula, not
> from `{γ_ρ}`).

---

## 1. The key question first: is (T2) a sign handle? — No.

Steps 1–2 added the real structure `j(s)=1−s̄` as the new ingredient. Before surveying operators
we test whether it helps, because if it does not, the survey reduces to the classical
inverse-spectral problem. The experiment is decisive.

> **(T2) splits into two readings:**
> - **(T2-weak)** `j` permutes the spectrum *as a set*;
> - **(T2-strong)** `j` *fixes each eigenvalue* (spectrum `⊂ Fix(j)` = critical line).

**Result** (`surfB_realstructure_vacuous.py`):

| spectrum | (T2-weak) `j` permutes set? | on `Fix(j)` pointwise | `κ` (neg index) |
|---|---|---|---|
| RH-true (all on-line) | **True** | 4/4 | 0 |
| RH-false (off-line quartet) | **True** | 0/4 | 1 |
| RH-false (mixed on+off) | **True** | 2/6 | 1 |

So **(T2-weak) holds unconditionally** — `j` permutes the spectrum just as well for an off-line
(RH-violating) configuration as for an on-line one, because off-line zeros come in `j`-symmetric
quartets. It carries **no** information about the sign. And **(T2-strong) ⟺ spectrum `⊂ Fix(j)`
⟺ all zeros on-line ⟺ RH**, which is the missing positivity itself. The thing that detects
off-line zeros is the **negative index `κ`** (the bilinear Pontryagin index of P25/P26),
unchanged by adding the real structure.

> **Verdict on (T2):** the real-structure constraint is a **symmetry, not a positivity**. It is
> satisfied vacuously (weak reading) or equals RH (strong reading). The real structure adds **no
> new handle on the sign**. This is the pre-registered outcome (`00-SURF-2.0-design.md` §8,
> S5-fail) reached one level deeper — honestly, a negative.

---

## 2. Survey of the F-indep operators against (T1)–(T4)

With (T2) neutralized, the survey is over the few operators that natively produce the explicit
formula and asks which carries a **(T3) de Branges resolvent**.

| operator (literature) | (T1) spec `={γ}` | (T2) `j` | (T3) dB2 resolvent | (T4) F-indep | wall |
|---|---|---|---|---|---|
| **Connes scaling flow** (adele class space; absorption spectrum) | yes (spectral realization) | yes (symmetry, vacuous) | not native; trace-formula form | yes | positivity = Weil = **CAP** |
| **Connes–Consani scaling site / `Spec ℤ`** (zeros = Frobenius eigenvalues) | yes (by design) | yes (vacuous) | needs the global Hodge index | yes | the surface / Hodge index = **SURF** (Route 1) |
| **Burnol** (co-Poisson / Hankel; de Branges spaces for `ζ`) | yes | yes (vacuous) | **native** (de Branges spaces) | yes | `E` Hermite–Biehler = **CAP** |
| **de Branges canonical system** (Hamiltonian `H(t)`, Weyl/transfer `E`) | yes (inverse problem) | yes (vacuous) | **native, by construction** | yes if `H(t)` arithmetic | `H(t)`/`E_ξ` open; **Conrey–Li refutes** the specific dB positivity |

**Reading of the table.** All four are avatars of the explicit formula (T1+T4). Two of them —
**Burnol** and the **de Branges canonical system** — carry the (T3) resolvent *natively*: a
canonical system `dy/dt = z\,J\,H(t)\,y` with `H(t) ⪰ 0` *is* a resolvent obeying (dB2), and its
Weyl function is the structure function `E`. So (T3) is not the obstacle either; it is realized
by classical inverse-spectral theory the moment a Hamiltonian `H(t)` is in hand.

---

## 3. The reduction: SURF-B = the canonical-system inverse spectral problem

Combining §1 and §2: (T2) is vacuous, (T3) is native to the canonical-system family, (T1)+(T4)
are the explicit formula. What remains is exactly:

> **Construct the canonical-system Hamiltonian `H(t)` (equivalently the de Branges structure
> function `E = E_ξ`) whose spectrum is `{γ_ρ}`, from arithmetic (F-indep) data — and decide its
> positivity (`E_ξ` Hermite–Biehler ⟺ RH).**

This is **(T1)+(T3) = the inverse spectral problem for ζ**, and it is a **known, RH-equivalent**
formulation:
- it is precisely the de Branges program (canonical systems / `H(E_ξ)`), whose **specific
  positivity criterion was refuted by Conrey–Li (1998)**;
- it is the same object as P28's residual identification `E = E_ξ` plus the (dB2) resolvent — i.e.
  the obstruction chain and SURF-B meet at the *same* `H(t)/E_ξ`;
- its positivity is the **wrong-sign capstone** (CAP): the canonical system supplies the
  symmetry and the resolvent, but `H(t) ⪰ 0` carrying the sign is exactly what is unproven.

**So SURF 2.0, pursued honestly, lands back on the de Branges canonical-system wall** — now
reached from the real-structure side, and *stripped of the geometric ambiguity*: it was never
"find a mysterious surface," it is "solve the F-indep inverse spectral problem for the canonical
system," a single identifiable object.

---

## 4. The durable structural conclusion: symmetry vs positivity

Phase 17 did not move the wall, but it produced a sharp, RH-independent **explanation of why the
entire operator family stalls at the same wall** — the most useful output of the phase:

> **Symmetry-vs-positivity dichotomy.** Every realization of the Weil form by an operator with a
> real structure — Connes' scaling flow, Connes–Consani, Burnol, the de Branges canonical system —
> supplies the full *symmetry* package: (T1) the spectrum, (T2) the real-structure/quartet
> symmetry, (T3) the resolvent. RH is **none** of these. RH is the **pointwise** statement that
> the spectrum lies on `Fix(j)` (the `(T2-strong)` positivity), which is *orthogonal* to the
> entire symmetry structure: `κ`, not any symmetry, is its detector. Hence no amount of
> symmetry/resolvent structure can decide RH; the sign is a genuinely separate, one-sided
> constraint.

This is the wrong-sign capstone, **localized and sharpened**: it explains the capstone's
*mechanism* in the operator picture — symmetry is unconditional, positivity is the index `κ`, and
the two never imply each other. It unifies why Connes, Burnol, and de Branges all reach the same
place, and it is provable, RH-independent, and citable (it would be the natural **P29**:
"Symmetry versus positivity in real-structure realizations of the Weil form").

---

## 5. Honest net for Phase 17 (SURF 2.0)

- **Search space collapsed to one object.** The program no longer chases a surface; it chases the
  F-indep canonical-system Hamiltonian `H(t)` / `E_ξ` (= P28's `(dB2)`+identification). This is
  the user's "single identifiable object," now confirmed from two directions (obstruction chain
  **and** real-structure analysis).
- **Real structure: characterized, but vacuous for the sign.** Steps 1–2 fully characterized the
  `(j, b)` half (a real structure with transverse coordinate `b`); step-3/SURF-B showed it is
  γ-blind and sign-blind. A clean *negative* about the new ingredient.
- **Distance to RH: unchanged (CAP / Conrey–Li).** The positivity `H(t) ⪰ 0` is the standing
  wall. Phase 17 explains the wall's mechanism (symmetry vs positivity) without crossing it.
- **The one new theorem available:** the symmetry-vs-positivity dichotomy (§4) — RH-independent,
  the candidate P29.

---

## 6. Next — two honest options

1. **Write P29** (the symmetry-vs-positivity dichotomy, §4): an RH-independent structural theorem
   explaining why real-structure / canonical-system realizations cannot decide RH. This
   *consolidates* Phase 17 into a publishable result, in the program's "why RH resists" lineage
   (P15, P21), now at the operator/real-structure level. **Recommended:** it banks the durable
   output and is honest about the wall.
2. **Attack the inverse spectral problem (T1)+(T3) directly** — construct `H(t)` from primes
   (F-indep) — knowing in advance it terminates at `H(t) ⪰ 0` = CAP / Conrey–Li. Only worth doing
   if there is a *specific* new idea for the positivity; absent one, it re-derives the known wall.

**Pre-registered:** option 2 without a new positivity idea is CAP re-derived; we do it only with a
named new mechanism, else we consolidate (option 1) and stop pretending the wall is closer than it
is.

---

*Cross-refs:* `03-route2-testbed.md` (the (T1)–(T4) catalogue), `00-SURF-2.0-design.md` (§4
SURF-B, §8 falsifiers), `experiments/surfB_realstructure_vacuous.py`, `../06-papers/P28`
(canonical-system / `E_ξ` identification), `../06-papers/P15,P21` (why-RH-resists lineage).
*Memory:* `[[project-rh-current-direction]]`, `[[riemann-key-contradiction]]`.
