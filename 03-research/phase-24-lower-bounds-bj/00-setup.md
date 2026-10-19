# Phase 24 — Lower bounds for $b_j$ and local rigidity of the logarithm of $|\zeta|$

**Predecessor:** Phase 23 (spectral barrier, correction of 23-A.6)
**Status:** Active

---

## 0. The change of question

Through Phase 23, the question was:

> Does an off-line zero produce an observable contradiction?

The answer was systematically negative (Paley–Wiener, candidates I/II/III, standard GMC, structure function).

The **correction of 23-A.6** changed the picture: GMC compatibility is not uniform in $b_j$. There are three regimes:

| Regime | Condition | Hadamard depth | GMC minimum | Compatible? |
|---------|-----------|---------------------|------------|--------------|
| I | $b_j \geq \gamma_j^{-C}$ | $O(C\log\gamma_j)$ | $O(-\log\gamma_j)$ | Yes |
| II | $b_j = e^{-\gamma_j^\alpha}$, $\alpha \in (0,1)$ | $\sim 2\gamma_j^\alpha \gg \log\gamma_j$ | $O(-\log\gamma_j)$ | Potentially no |
| III | $b_j \leq e^{-c\gamma_j}$ | $\sim 2c\gamma_j \gg \log\gamma_j$ | $O(-\log\gamma_j)$ | No (conditionally) |

The central question of Phase 24 is:

$$\boxed{\text{What restrictions exist on how fast }b_j \to 0?}$$

---

## 1. Bibliographic audit: what exists and what does not

### 1.1 What is well established (upper bounds on $b_j$)

**Korobov–Vinogradov zero-free region (1958):**
$$b_j \leq \frac{1}{2} - \frac{c_0}{(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}.$$
Upper bound. Gives the maximum speed at which a zero can approach $\Re(s)=1$, not $\Re(s)=1/2$.

**Hadamard–de la Vallée-Poussin zero-free region (1896):**
$$b_j \leq 1/2 - c/\log\gamma_j.$$
Weaker than KV. Still only an upper bound.

Neither gives information about how small $b_j$ can be.

### 1.2 Density theorems (statistical, not individual)

Selberg, Ingham, Huxley, Montgomery, Jutila:
$$N(\sigma, T) \ll T^{A(1-\sigma)} (\log T)^B$$
where $N(\sigma, T)$ is the number of zeros with $\Re(\rho) > \sigma$, $|Im(\rho)| \leq T$.

These control how many zeros can exist with $\Re(\rho) > 1/2 + \delta$ (they are rare as $\delta \to 1/2$), but they do not exclude an isolated zero with $b_j = e^{-10^{100}}$.

### 1.3 Results on the proportion of zeros on the line

Levinson (1974): at least 1/3 of the zeros are on the line.
Conrey (1989): at least 2/5.
Bui–Conrey–Young (2011): at least 41%.

None of these gives information about the distance of off-line zeros.

### 1.4 Zero repulsion (Deuring–Heilbronn)

For Dirichlet $L$-functions: if $L(s,\chi)$ has a Siegel zero $\beta = 1-\delta$ near $\Re(s)=1$, it repels other zeros. But this concerns zeros near $\Re(s)=1$, not near $\Re(s)=1/2$.

For the function $\zeta$ itself: no repulsion phenomenon is known near $\Re(s)=1/2$.

### 1.5 Pair correlation (Montgomery, 1973)

The pair correlation conjecture predicts that on-line zeros have GUE statistics. This describes the spacing distribution between zeros on the critical line, not the position of off-line zeros.

### 1.6 Conclusion of the audit

**There is no published result of the form $b_j \geq F(\gamma_j)$ for an individual off-line zero.**

The question "how small can $b_j$ be if RH is false?" appears to be genuinely open in the literature. There is a conceptual reason: if someone proved $b_j \geq \gamma_j^{-A}$ for all $j$, they would automatically exclude an enormous family of counterexample scenarios to RH, which would be a major result.

---

## 2. The new chain: $b_j \to \delta\log|\zeta| \to$ GMC

What is new in the current program (and does not appear in the classical literature) is the chain:

$$b_j \xrightarrow{\text{Hadamard}} \delta_j\log|\zeta(1/2+it)| \xrightarrow{\text{GMC}} \text{compatibility/incompatibility}$$

For the step on the right to be rigorous, we need:
1. A proved **lower** bound for $\min_{t \in [T,2T]} \log|\zeta(1/2+it)|$ (not available unconditionally).
2. Or: a **lower** bound for $b_j$ (Phase 24-A).
3. Or: that the full local profile of $\log|\zeta|$ induced by $\mathcal{O}_j$ be incompatible with the geometry of the log-correlated field (Phase 24-B).

---

## 3. Structure of Phase 24

### Phase 24-A: Theory of lower bounds for $b_j$

**Central question:** Can any bound $b_j \geq F(\gamma_j)$ be proved assuming RH is false?

**Approaches to explore:**
- (24-A.1) Explicit formula: $\psi(x)-x$ contains $x^{1/2+b_j}$; can the KV bound condition this?
- (24-A.2) The Hadamard identity at $t=\gamma_j$: the evaluation of $\log|\zeta(1/2+i\gamma_j)|$ comes from the product over all zeros; can it be bounded from below?
- (24-A.3) Moments of $|\zeta|$: $\int_T^{2T}|\zeta(1/2+it)|^{2k}dt$ and the contribution of the off-line orbit.
- (24-A.4) van der Corput identities / exponential sum estimates.
- **Frankness in advance:** my expectation is that no lower bound exists, but the precise diagnosis of why it does not exist is itself a publishable result.

### Phase 24-B: Universal local profile of $\log|\zeta|$ induced by $\mathcal{O}_j$

**The key (new) observation:**

Do not study the pointwise value $\log|\zeta(1/2+i\gamma_j)|$, but the full profile:
$$\ell_j(u) := \log|\zeta(1/2+i(\gamma_j + u b_j))|, \quad u = O(1).$$

The Hadamard term of $\mathcal{O}_j$ in this profile is:
$$\delta_j\ell_j(u) = \log(1+u^2) + O(1).$$

This is a **universal** profile (independent of $b_j$ and $\gamma_j$) with the shape of a logarithmic "inverted bell". It is not a Gaussian fluctuation.

**The question:** Is the geometry of this profile incompatible with the correlations of the log-correlated field at a separation scale $b_j$?

### Phase 24-C: Rigorous GMC compatibility

Use the proved results on log-correlated fields:
- Arguin–Belius–Bourgade–Radziwiłł–Soundararajan (2019) on the distribution of the maximum of $\log|\zeta|$.
- Najnudel (2018), Paquette–Zeitouni (2018) on extremes.
- Harper (2013, 2020) on moments of $|\zeta|$.

Determine whether any of these implies a lower bound for $\min_{t\in[T,2T]}\log|\zeta(1/2+it)|$ that is rigorous and strong enough.

### Phase 24-D: Connection with the $\omega$ program

The $\omega$-class program identified the correspondence $z = \beta^2$ (connection M13.1 of the research program). Study whether this correspondence, applied to an off-line zero, produces restrictions on $b_j$ in the language of $\omega$ classes.

---

## 4. Rules of Phase 24

- No numerical computation.
- Only definitions, lemmas, propositions, theorems, proofs.
- Absolute frankness: if 24-A produces no lower bound, document precisely why.
- Success criterion: either $b_j \geq F(\gamma_j)$ (a new result), or the precise diagnosis of why no standard argument can give such a bound.

---

## 5. Documents of Phase 24

- `00-setup.md` — this document
- `01-lower-bounds-bj.md` — Phase 24-A (lower bounds, audit of methods)
- `02-local-profile.md` — Phase 24-B (local profile $\ell_j(u)$ and geometry)
- `03-rigorous-chaos.md` — Phase 24-C (rigorous GMC compatibility)
