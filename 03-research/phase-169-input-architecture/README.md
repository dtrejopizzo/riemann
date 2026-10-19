# Phase 169 — Architecture of the single missing input needed to close row D

Phases 163–168 reduced row D to a single remaining gap: an inequality 𝓘 (Re 𝒮 < B) at the lowest
hypothetical off-line "witness" quartet. This phase specifies exactly what properties any such
input 𝓘 would need to have (without asserting it exists), audits that specification against the
record, and tests the most natural concrete candidate — an "Eratosthenes induction" step
propagating a positivity property from scale T to scale T+Δ — against the corpus and against a
direct construction attempt.

## Results

- The six-step proof skeleton reducing "no witness ⟹ row D" to the single missing input 𝓘 (line 5: Re 𝒮 < B) is laid out with every other step **PROVED** or **PROVED given (Dom_θ)**.
- Audit (R169_091) finds two errors in the first version of the architecture: the witness ordinate γ_q is **PROVED** not to be determined by the window (a counterexample exists in the record), and the "new primes" in [X,Y] are **PROVED** not free — they are fixed by the Eratosthenes sieve of the window since Y < X². Corrected, 𝓘 must hold on an entire positive-density set of heights Γ_S(F), not a single γ_q.
- With the correction, 𝓘's RH-equivalence over Γ_S(F) is **OPEN** (not proved either way); every known input class (γ-uniform statements, measure statements, Type I/sieve estimates, bilinear estimates) is excluded as a source for 𝓘 — the surviving admissible form (correlating the Eratosthenes image of the window with the node set of its own witness function) has **no known candidate** — "formally non-empty, practically empty."
- Lemma D₀ (decorrelation in the Cramér probabilistic model): **PROVED** in that model but shown uninformative, since it holds uniformly in γ there and so cannot distinguish [D] — the real, deterministic obstruction is that the tail is Eratosthenes-determined by the window, not independent of it.
- The natural candidate construction — an "Eratosthenes induction" step W_T ≥ 0 ⟹ W_{T+Δ} ≥ 0 — is built out exactly (activation identity, Schur-complement reduction) and shown to require, via Theorem M, a doubly-exponentially precise cancellation that no known sieve, Type I/II, or large-sieve estimate can supply — **NO-GO** (wall W2); specific sub-routes (Legendre decomposition, Fourier/zero-free-region side) are shown to fail for stated structural reasons.
- Corpus audit reveals this exact propagation law was already on record from phase 159 (Theorem Ψ1 "sieve flow" + Theorem NB "no-bootstrap trichotomy"), both already marked DEAD in the grid — **confirms** the phase-169 construction independently reaches the same closed result, with one correction: mere window-determinacy does not separate ζ from other automorphic L-functions (strong multiplicity one gives it for free); the relevant class is Euler products determined by sieving, for which no falsifier is known (one would refute GRH).
- Overall closure: the input architecture is written and corrected; at any fixed scale the input 𝓘 reduces to a finite, certifiable window computation (as in Paper 47's certificates up to ½log5), and the entire infinite content of row D is the quantifier over all scales T — the "master quantifier" problem (W2/Theorem M). The only residue with independent content left open is the Beurling-frontier question (E_θ): whether N(x) = Ax + O(x^θ), θ < ½, forces RH for a general multiplicative system.

## Documents

- `R169_000_INPUT_ARCHITECTURE.md` (and `R169_000_v1.md`, an earlier draft) — the proof skeleton and the specification of input 𝓘, with a corrected v2 appended after audit.
- `R169_091_AUDIT_ARCHITECTURE.md` — finds and corrects the two errors (γ_q not window-determined; Eratosthenes-determined tail).
- `R169_101_ERATOSTHENES_INDUCTION.md` — the direct construction attempt at the induction step, closed NO-GO via Theorem M.
- `R169_102_INDUCTION_CORPUS_AUDIT.md` — shows the propagation law already exists on record (phase 159 Ψ1/NB) and corrects the determinacy hypothesis.
- `R169_190_AUDIT.md` — consolidated ledger and closure of the phase.

## Relation to other phases

Direct continuation of the (★_cell)/(WS*) witness program of phases 163–168 (especially phase 168's small-y residue P_gap); rediscovers and confirms the phase-159 sieve-flow/no-bootstrap results; its residual open question (the Beurling frontier E_θ) is the same frontier attacked constructively in phase 171.
