# E79.118 - Omega7: what it is, what is closed, and the anatomy of the open point

**Scope:** program orientation document.
**Class:** EXPLICACION. No new mathematics; no new claim.
**Primary reference:** `04-papers/36-obstruction-ledger/main.tex` (paper 36),
sections `sec:live-chain`, `sec:h8-harness`, `subsec:omega7-attack`.

---

## 1. Where the chain lives

Paper 36 (*the obstruction ledger*) contains the complete proof chain. Its
Step 5 substructure isolates a chain of seven statements `Omega_1..Omega_7`.

```text
Omega_1..Omega_6  are Omega-LINKS: closed reductions or equivalences.
Omega_7           is NOT a link. It is the TERMINAL RESIDUE the chain isolates.
```

The LP + IDENT chain of phases 76-79 is a **separate and newer** attack on
`Omega_7`. It does not appear in paper 36 (zero occurrences of `SR-SAFE`,
`SAFE-LIMIT-POINT`, `IDENT` in `main.tex`). Do not cite paper 36 for it.

---

## 2. What is closed, what is open

| | Statement | Status |
|---|---|---|
| `Omega_1` | RH `<=>` all `Xi`-zeros real | **CLOSED** |
| `Omega_2` | real zeros `<=>` ARP-P (Steps 1-15) | **CLOSED** |
| `Omega_3` | ARP-P `<=>` terminal positivity `delta_N(z_0) >= 0` for all `N` | **CLOSED** (reference-whitened form) |
| `Omega_4` | `delta_N >= 0` `<=>` one-sided whitened domination `lambda_max(W_A^{-1/2} T_L W_A^{-1/2}) <= 1` | **CLOSED** (`N <= N_*(t_0)`) |
| `Omega_5` | interior positivity has a positive regular boundary limit `y -> 1/2` | **CLOSED** (per `N`) |
| `Omega_6` | boundary positivity `<=>` Li-Keiper `lambda_n >= 0`, via `w_{-i/2} = 1 - 1/rho` | **CLOSED** |
| `Omega_7` | `lambda_n >= 0` for all `n` | **OPEN** -- the single open input |

```text
There is exactly ONE open point: Omega_7.
Everything else in the Omega-chain is proved in paper 36.
```

---

## 3. The warning that governs everything

```text
Omega_7 is EQUIVALENT to RH (Li 1997).
```

Paper 36 is explicit and repeats this deliberately: `Omega_7` is **not a new
criterion** -- it is the classical Li criterion, reached independently by the
ARP-P architecture. Two consequences that must never be forgotten:

```text
1. "Proving Omega_7" IS "proving RH". The chain does not make RH easier.
   Omega_1..Omega_6 are a DIFFICULTY LOCALIZATION, not a simplification.
2. Its unresolved status must never be described as a "small gap".
   It is the whole gap.                                              (118-1)
```

Paper 36 states the governing principle as **difficulty conservation (H0)**:

> any purported proof contains exactly one step that is either RH-strength
> new mathematics, or an error.

The productive use of the chain is therefore: choose the best route by
elimination, execute it, and autopsy the death point -- the autopsy is itself
a theorem.

---

## 4. Anatomy of Omega_7: the internal structure

`Omega_7` has no sub-lemmas that decompose it -- the chain terminates there.
But it has an exact internal *anatomy*, and each piece is a "why" worth
sitting with.

### 4.1 The exact unconditional decomposition

Splitting `log xi` into archimedean and zeta parts,

```text
log xi = [log s - (s/2) log pi + log Gamma(s/2)] + log((s-1) zeta(s)),
```

and using

```text
lambda_n = n * sum_{k=1}^{n} C(n-1, k-1) * sigma_k,
sigma_k  = [(s-1)^k] log xi(s),
```

gives an **exact, unconditional** split (polygamma for the archimedean part,
Stieltjes constants `gamma_j` for the zeta part):

```text
lambda_n = lambda_n^arch + lambda_n^prime.                           (118-2)
```

Measured to `n = 120` (drivers `omega7_li_decomp.py`, `omega7_li_inject.py`):

```text
- every lambda_n > 0;
- lambda_n^arch follows the Voros trend  ~ (n/2) log(n / 2pi)
  (ratio 0.823, 0.845, 0.873 at n = 40, 80, 120, increasing to 1);
- |lambda_n^prime| / lambda_n^arch falls to 0.002-0.04 for n >= 30
  (still 0.083 at n = 20).                                           (118-3)
```

**So `Omega_7` is one explicit inequality:**

```text
|lambda_n^prime| < lambda_n^arch   for all n,   UNCONDITIONALLY.     (118-4)
```

An archimedean trend of size `(n/2) log n` must dominate an arithmetic
oscillation, for every `n`, with no hypothesis about zeros.

### 4.2 Why it is trivial GIVEN RH -- and why that is the whole problem

Li variables are reciprocal under the functional equation: `w_rho = 1 - 1/rho`,
`w_{1-rho} = 1 / w_rho`, and

```text
|w_rho| = |rho - 1| / |rho|   { = 1  if Re rho = 1/2
                              { > 1  if Re rho < 1/2
                              { < 1  if Re rho > 1/2                 (118-5)
```

If RH holds, pairing `rho = 1/2 + i*gamma` with `1 - rho = conj(rho)` and
writing `w_rho = exp(i*theta_gamma)`:

```text
lambda_n = sum_{gamma>0} (2 - 2 cos(n theta_gamma))
         = 4 sum_{gamma>0} sin^2(n theta_gamma / 2)  >= 0.           (118-6)
```

A manifest sum of squares.

```text
THE POINT: Omega_7 is trivial given RH. Its entire content is establishing
the SAME nonnegativity from the ARITHMETIC definition of lambda_n, in which
the zeros DO NOT APPEAR.                                             (118-7)
```

This is the single most useful sentence for orienting an attack. Any argument
that reaches for the zeros has assumed the answer.

### 4.3 Why an off-line zero destroys it -- the detection mechanism

The obstruction is one geometric term. An off-line `rho_0` has a
functional-equation partner with `|w| > 1`; its quartet contributes

```text
- 2 Re(w^n) + ...,   with |w|^n growing GEOMETRICALLY,               (118-8)
```

which for large `n` overturns the `(n/2) log n` trend and drives
`lambda_n < 0`.

Exhibited numerically:

```text
inject off-line quartet rho_0 = 0.9 + 3i  (max |w| = 1.0434)
  -> lambda_n turns negative first at n = 97
     (lambda_97^inj = -5.95 against true lambda_97 = 113.4)
inject on-line control  rho_0 = 0.5 + 3i
  -> every lambda_n stays > 0 (it only adds 4 sin^2).                (118-9)
```

```text
So: positivity is destroyed precisely, and ONLY, by the geometric growth
|w| > 1 of an off-line zero. Closing Omega_7 means forbidding |w_rho| > 1.
```

### 4.4 Why there is no positive prime truncation -- this fixes the METHOD

**Proposition (no positive prime truncation, computational).** For the
whitened truncated form

```text
m_N(X) := lambda_min( A_N^{-1/2} (A_N - T_Lambda^{<=X}) A_N^{-1/2} ),
```

one finds `m_N(X) < 0` for a range of finite `X` even though the full defect
`m_N(infinity) = delta_N > 0`. At `t_0 ~ 297.24`, `y = 1`, already at `X = 50`:

```text
m_6  = -0.53      delta_6  = 8.0e-05
m_8  = -0.66      delta_8  = 7.7e-08
m_10 = -0.73      delta_10 = 1.8e-11                                (118-10)
```

and the tail norm exceeds `|m_N(X)|` at every listed `X`.

```text
CONSEQUENCE: A_N - P_Lambda is NOT of the form
  (positive truncated part) - (small tail).
No finite prime cutoff yields a positive operator to perturb from.
Positivity is an EXACT CANCELLATION across ALL primes.              (118-11)
```

This is why the archimedean part does not dominate the prime part termwise
or up to a controllable tail. It kills the entire perturbative family:
mollifying the symbol is the `X -> infinity` end of the same truncation and
inherits the indefiniteness; the backward-heat-flow route propagates a
factorially small margin `delta_N ~ (kappa L / N)^(2N)` against polynomial
Gronwall drift and closes only `N <= N_*(L)`.

### 4.5 Why zero-location inputs cannot close it

**Proposition (insufficiency of zero-location inputs).** If `xi` has a zero
with `Re rho_0 != 1/2`, then `lambda_n < 0` for infinitely many `n`
(Bombieri-Lagarias). Therefore:

```text
No hypothesis CONSISTENT WITH the existence of a single off-line zero can
imply lambda_n >= 0 for all n.                                      (118-12)
```

This rules out, as sole input:

```text
- the classical zero-free region beta < 1 - c/log(|gamma|+2);
- any zero-density estimate N(sigma,T) << T^{a(1-sigma)}.
```

Both permit off-line zeros.

**Scope, stated carefully** (paper 36 is explicit here): this restricts the
*input class*. It does **not** say `Omega_7` is unprovable. And the slogan
"the only sufficient input is RH itself" would be circular -- since
`lambda_n >= 0` *is* equivalent to RH, any proof tautologically yields RH.
That is the goal of the chain, not an obstruction to it.

---

## 5. Routes already eliminated (do not re-tread)

| Route | Why it dies |
|---|---|
| Fixed margins | `cor:no-margin` -- no fixed margin at the terminal boundary |
| Losses `e^{o(N log N)}` | the factorial wall |
| Zero-location inputs | `prop:unboundable` (s. 4.5) |
| Pointwise bounds on `psi(y) - y` | the `Theta(n)` deficit |
| Term-by-term `Lambda >= 0` positivity | measured factorial loss |
| Krein extension | short-window positivity is provable and Krein extends *some* positive-definite function -- but the route needs **our** kernel to be the extension, not mere existence |
| Fejér-Riesz factorization `A - T = B*B` | requires the boundary symbol nonnegative `<=>` RH. **Circular** |
| Reflection positivity | per-prime symbol `2 Re[x/(1-x)]`, `|x| = p^{-1/2}`, changes sign; positivity lives in cross-prime interference |

---

## 6. The live route in paper 36, and where it dies

What remains unexplored, per paper 36, is the **gauge structure**:

```text
unconditional positivity at large height for each fixed N (band closure)
                          VERSUS
geometric negativity near an off-line zero (not-RH).                (118-13)
```

Between them lies only a **quantifier exchange**, whose natural tool is
almost-periodicity of the prime side.

**The attack.** Transport a negative witness (Lemma `geom-detection`:
`c*J_N c <= -m_N`, `m_N ~ |b|^{2N}`, `|b| = (y+delta_w)/(y-delta_w) > 1`) to
a gauge `t_0''` with paired phases, away from the quartet, where the zero side
forces `c*J_N(t_0'') c >= -C`. If the geometric `m_N` dominates the errors,
the two estimates collide and RH follows.

**The autopsy -- recurrence/detection imbalance.** The `N`-jets see primes up
to `X = e^{cN}`, and the margin requires `epsilon <= m_N e^{-CN}`. The
Kronecker recurrence gap is

```text
ell(X, epsilon) ~ epsilon^{-pi(X)} = exp(e^{cN} * C' N) = Tower(N),

while the detection gain is only geometric:  m_N = e^{c delta_w N}. (118-14)
```

```text
Full phase matching costs a TOWER; detection pays GEOMETRIC.
They never meet.                                                    (118-15)
```

**The crack that is left.** One need not match all phases -- only force a
single scalar `F(t) := c* P_N(t) c` to return near its value at `t_0`. That
is a *level-return* of an almost-periodic function, which is cheap (positive
density) **if the value is not extremal**. Whether `F(t_0)` is extremal is
decided by *ceiling rigidity* (`prop:ceiling`).

```text
This is the live frontier of Omega_7 inside paper 36.               (118-16)
```

---

## 7. How the phases 76-79 chain relates

Phases 76-79 pursue a **different** route to the same terminal object:

```text
LP + IDENT + RDP-SHELL + (PROLATE + WEIL-TAIL)
  => SAFE-LIMIT-POINT => SAFE-PROLATE-BRIDGE => SR-SAFE
  => Omega_7 => RH
```

This chain aims to *derive* `Omega_7` rather than attack the Li coefficients
directly. Its current state is in `E79.117` (post-audit ledger): no link is
closed unconditionally; `GAP-Z` and the `DISCRIMINANT` are the two open holes.

**The question H0 forces, and the one worth sitting with:**

```text
Omega_7 is equivalent to RH. Therefore the LP+IDENT chain MUST contain
exactly one RH-strength step -- or an error. WHICH STEP IS IT?      (118-17)
```

The program's own answer, recorded in the phase-79 README, is that the
`DISCRIMINANT` (`E79.6`) is "the genuine NEW-mathematics milestone". That is
consistent: the `DISCRIMINANT` is where the plant must provably fail, i.e.
where off-line-ness is forbidden -- structurally the same job that
`|w_rho| > 1` does in section 4.3.

```text
If that identification is right, then:
  - GAP-Z is INFRASTRUCTURE (hard, but not RH-strength: it is
    build-neutral, and a build-neutral statement cannot be RH-equivalent
    -- see E79.116 s.3.3);
  - the DISCRIMINANT carries the entire RH content;
  - and every hour spent on GAP-Z is spent on the part that is NOT the
    real problem.                                                   (118-18)
```

That last line is a hypothesis, not a finding. But it is checkable, and it
is the highest-leverage thing to settle before allocating more effort.

---

## 8. Summary for planning

```text
CLOSED : Omega_1 .. Omega_6  (paper 36, all proved).
OPEN   : Omega_7 only.
        = |lambda_n^prime| < lambda_n^arch for all n, unconditionally.
        = equivalent to RH. Not a small gap -- the whole gap.

Internal anatomy (the "why" of each piece):
  4.1 exact decomposition        -> the inequality is explicit
  4.2 sum-of-squares given RH    -> content = derive it WITHOUT zeros
  4.3 detection mechanism        -> only |w|>1 can break it
  4.4 no positive truncation     -> method is fixed: exact global cancellation
  4.5 zero-location insufficient -> input class restricted

Eliminated routes: s.5 (eight of them).
Live route in paper 36: gauge transport; dies at Tower vs geometric;
  the surviving crack is the level-return of F(t) and ceiling rigidity.
Live route in phases 76-79: LP+IDENT; state in E79.117.
Open orientation question: WHICH step carries the RH-strength content (118-17).
```
