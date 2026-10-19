# Phase 20 — Step 0: analysis of the Dirichlet series of q^{ω(n)}

**Purpose:** Rigorously determine which singularities control M_k(N) and its fluctuations,
BEFORE designing experiments. This answers the advisor's warning: without this analysis,
Experiments 1–3 of the initial design may be looking for signals that mathematically do not exist.

---

## 1. The exact Dirichlet series

The Euler product for q^{ω(n)} is well known:

```
         ∞
F_q(s) = Σ  q^{ω(n)} / n^s
        n=1

       = ∏_p  (1 + q·p^{-s} + q·p^{-2s} + ...)
         [each prime p contributes: ω(p^k) = 1 for k ≥ 1, and ω(1) = 0]

       = ∏_p  (1 + q·p^{-s}/(1 − p^{-s}))

       = ∏_p  (1 − p^{-s} + q·p^{-s}) / (1 − p^{-s})

       = ∏_p  (1 + (q−1)·p^{-s}) / (1 − p^{-s})
```

Factoring with ζ(s) = ∏_p (1 − p^{-s})^{−1}:

```
F_q(s) = ζ(s) · ∏_p (1 + (q−1)·p^{-s})
```

**Check:** for q = 1: F_1(s) = ζ(s) · ∏_p 1 = ζ(s) ✓ (q^{ω(n)} = 1 for all n → F_1 = ζ).

---

## 2. The Selberg–Delange factorization

The form that appears in the Selberg–Delange theorem is:

```
F_q(s) = ζ(s)^q · G_q(s)
```

where G_q(s) is holomorphic and NOT zero for Re(s) > 1/2.

Explicit derivation:

```
F_q(s) = ζ(s) · ∏_p (1 + (q−1)p^{-s})

       = ζ(s)^q · ζ(s)^{1-q} · ∏_p (1 + (q−1)p^{-s})

       = ζ(s)^q · G_q(s)
```

where:

```
G_q(s) = ζ(s)^{1-q} · ∏_p (1 + (q−1)p^{-s})

        = ∏_p  [(1 + (q−1)p^{-s}) · (1 − p^{-s})^q]
```

(using ζ(s)^{1-q} = ∏_p (1−p^{-s})^{q-1} in the Euler product).

**Key property of G_q(s):**

- For Re(s) > 1/2, each factor of the product is (1 + (q−1)p^{-s})(1−p^{-s})^q = 1 + O(p^{-2σ}).
- The product converges absolutely for Re(s) > 1/2.
- G_q does not vanish for Re(s) > 1 (absolute convergence of the Euler product).
- Under RH, G_q does not vanish for Re(s) > 1/2.

---

## 3. The critical question: where do the zeros of ζ enter?

Perron's formula gives:

```
M_k(N) = Σ_{n≤N} q^{ω(n)}/n = (1/2πi) ∫_{c-i∞}^{c+i∞} F_q(s)/s · N^s ds
```

When the contour is moved to the left of Re(s) = 1, the residues come from the POLES of F_q(s)/s.

**Does F_q(s)/s have poles at the nontrivial zeros ρ of ζ?**

- ζ(ρ) = 0 → ζ(s)^q has a ZERO of order q at ρ.
- G_q(ρ) ≠ 0 (holomorphic and nonzero).
- Hence F_q(ρ) = ζ(ρ)^q · G_q(ρ) = 0.

**F_q has ZEROS at ρ, NOT poles.**

Perron's formula collects residues of POLES only.

→ **The nontrivial zeros of ζ do NOT contribute residues in Perron's formula for M_k(N).**

The only poles are:
- s = 1 (pole of order q = k² of ζ(s)^q): gives the main term C_k(logN)^{k²}.
- s = 0 (simple pole of 1/s): small contribution, O(1).
- There are no others.

---

## 4. Direct consequence: M_k(N) is MONOTONIC

Since q^{ω(n)}/n > 0 for all n ≥ 1:

```
M_k(N) = Σ_{n=1}^{N} q^{ω(n)}/n   is STRICTLY INCREASING in N.
```

It cannot oscillate. There are no oscillatory terms N^ρ. M_k(N) rises monotonically toward its asymptote.

**The "fluctuations" of R_k(N) = M_k(N)/(logN)^{k²} are ALWAYS NEGATIVE:**

```
M_k(N) < C_k(logN)^{k²}   for every finite N.
```

The residual R_k(N) − C_k < 0 and converges to 0 from below, monotonically.

---

## 5. What controls the fluctuations of M_k

The fluctuations of R_k(N) are the difference between the asymptotic functional and the finite value.
That difference is controlled by the Laurent expansion of F_q(s)/s at s = 1:

```
F_q(s)/s = [ζ(s)^q · G_q(s)] / s

ζ(s) = 1/(s−1) + γ_E + ...   [Laurent expansion]

→ F_q(s)/s has a pole of order q = k² at s = 1.
```

The full residue gives:

```
M_k(N) = C_k(logN)^{k²}  +  C_k^{(1)}(logN)^{k²-1}  +  ...  +  C_k^{(k²)}  +  O(N^{-δ})
```

That is: the full expansion of the main term has k² coefficients (one for each power of
log N of k² down to 0). The "error" O(N^{-δ}) comes from the integral over the line Re(s) = 1−δ
where F_q is holomorphic.

**Conclusion:** the rate of convergence of R_k(N) → C_k is governed by the coefficients
of the Laurent expansion of F_q at s = 1 — not by the zeros of ζ.

---

## 6. Design correction: what needs to change in Phase 20?

### What does NOT work (refuted by Step 0)

❌ **Hypothesis C of the original design:** "If κ > 0, the amplitude of the oscillation of M_k(N)/(logN)^{k²}
grows faster than N^{-1/2}."

This hypothesis is incorrect: M_k(N) is monotonic (does not oscillate) and the zeros of ζ do not appear as
residues in the Perron formula for M_k. The amplitude of the "oscillation" is 0 (the residual is always
negative). There is nothing to measure.

❌ **Experiment 1 (fluctuation analysis of M_k):** Designed to detect an oscillation that
does not exist. The experiment will measure the rate of convergence of R_k(N) → C_k from below, which
is a second-layer phenomenon of the Laurent expansion at s=1. It has value for Branch B
(multifractal arithmetic theory) but NOT for detecting κ > 0.

### What CAN be sensitive to the zeros

✅ **Experiment 3 (multiplicative correlations):** The sum C_k(h,N) = Σ k^{2ω(n)}·k^{2ω(n+h)}/n
involves the PRODUCT of two arithmetic functions that are NOT multiplicative in n (because the shift h breaks
multiplicativity). Its analysis requires the Hardy–Littlewood circle method or multiplicative
sieve methods. In that context, the zeros of ζ DO appear via:

```
Σ_{p≤N} 1/p · 1/p  ~  (loglogN)²  [without h]
Σ_{p≤N, p|n, p|(n+h)} ...         [with h: double sum over primes, via sieve]
```

But the connection with the zeros is subtler: it goes through the distribution of primes in arithmetic
progressions and the von Mangoldt error, not directly through the zeros as residues of F_q.

✅ **A DIFFERENT version of Experiment 1:** Instead of M_k, study the function:

```
Ψ_k(N) := Σ_{n≤N} q^{ω(n)} · Λ(n)
```

where Λ(n) is the von Mangoldt function. This sum DOES have the form ζ'/ζ · F_q, and there the zeros
DO appear as poles (through ζ'/ζ). This is the direction that would genuinely connect to κ.

✅ **The correct question for Route C:** Instead of "does M_k oscillate?", the correct question is:

> Is the CORRELATION between ω(n) and the function Λ(n) sensitive to κ?

Formally: does the ratio Σ_{n≤N} q^{ω(n)}·Λ(n)/n  /  (Σ_{n≤N} q^{ω(n)}/n) have oscillations
controlled by the zeros?

This ratio would indeed see the zeros, because Σ q^{ω(n)}·Λ(n)/n^s = −F_q(s) · ζ'(s)/ζ(s), and ζ'/ζ
has simple poles at the zeros of ζ.

---

## 7. The value of Step 0

**What it found:**

1. F_q(s) = ζ(s)^q · G_q(s), with G_q holomorphic and nonzero for Re(s) > 1/2.
2. The zeros ρ of ζ are ZEROS of F_q (not poles) → they do not contribute Perron residues.
3. M_k(N) is monotonically positive → it does not oscillate → the design of Experiment 1 was invalid.
4. The rate of convergence of R_k → C_k is controlled by the Laurent expansion at s=1.
5. The connection with zeros requires involving ζ'/ζ (Mangoldt) or shifted sums (Exp 3 has potential).

**What it means:**

The advisor's Route C is still the best direction — but the observable must be changed.
M_k(N) is not the carrier of zero information. The carrier is Σ q^{ω(n)}·Λ(n)/n.

**What was NOT refuted:**

- The fact that the zeros are ABSENT from M_k does not rule out that there exist natural observables
  of ω that DO encode zero information. Step 0 closes the door on M_k and opens
  the question of ω-weighted objects via Λ or shifted correlations.

---

## 8. Revised plan for Phase 20

| Step | Revised experiment | Observable | Zero mechanism |
|---|---|---|---|
| 0 | This document | Factorization F_q = ζ^q · G_q | Zeros are zeros of F_q (not poles) |
| 1* | ω-Λ sum: Σ q^{ω(n)}Λ(n)/n | ω weighted by Mangoldt | ζ'/ζ · F_q: poles at ρ |
| 2 | Short-interval ω | Distribution of ω on [N,N+H] | Negative expected (sieve) |
| 3 | Correlations C_k(h,N) | Σ k^{2ω(n)}k^{2ω(n+h)}/n | Circle method, real potential |
| 4 | Bridge verdict | Synthesis | Does an ω↔zeros bridge exist? |

*The revised Step 1 is mathematically more honest than the original Experiment 1.*

---

*Cross-refs:* `00-PHASE20-DESIGN.md` (original design to correct), `../phase-19-omega-rate-freezing/05-k2-from-erdjoskac.md`
(G_q(1) Euler product, consistent with G_q holomorphic), Selberg–Delange theorem (Tenenbaum, §II.5).
*Decision:* Experiments 2–3 of the original design are kept; Experiment 1 is replaced
by the ω-Mangoldt sum.
