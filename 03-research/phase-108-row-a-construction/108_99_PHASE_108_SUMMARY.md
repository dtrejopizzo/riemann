# 108.99 — Phase 108 summary

Every verifier in this directory was re-run independently from the
repository; all exit 0. No status was promoted.

## 1. The stage board

| Stage | Mandate | Verdict |
|---|---|---|
| 0 | corner pairing, its radical, its signature | **closed** (phase 107) |
| 1 | a zero-free pairing evaluable on principal elements | **closed** (108_33) |
| 2 | is the pairing principally invariant? | **closed, negatively** (108_38): invariance fails; radical = zeros of $\Phi$ |
| 3 | the correspondence functionals assemble | **closed** (108_36): the assembly is $-\zeta'/\zeta$ |
| 4 | archimedean fibre — identity, operator, geometry | **closed**: identity ✓ (108_39), operator ✓ (108_40), **geometry negative** (108_41–43) |
| 5 | is the assembly an intersection number? | **closed, negatively** (108_50, 108_53–55): no, by either route |
| 6 | the primitive inequality — row (d) | open; entry conditions set by 108_43 §2 and 108_91 §4.2 |
| 7 | scaling compatibility | open |

## 2. What the phase produced

### 2.1 Positive theorems

* **The character classification (108_02).** The nonzero continuous solutions
  of $f(r/n)=\chi(n)f(r)$ are exactly $f=c\,r^{s}$, $\chi(n)=n^{-s}$; the
  log-periodic factor 108_00 §5 anticipated is **forced trivial**.
* **Stage 1's bridge (108_33).** For $s_0,s_1\in(0,1)$ off the singular set,
  $\Lambda_g^0(\mathrm{div}\,U_{s_0}-\mathrm{div}\,U_{s_1})
  =L_g(s_0)-L_g(s_1)$, finite, with the divergent constant of 108_12
  contributing exactly zero at every finite regularization depth. This made
  principal invariance a **well-formed statement** for the first time.
* **Stage 3's assembly (108_34–36).** $\Gamma_{p,k}^{\mathrm{Tate}}(f_{1/2})
  =\Lambda(p^k)/\sqrt{p^k}$, assembling to $-\zeta'/\zeta(s)$.
* **Stage 4's operator form (108_40).** $\det_{\mathrm{reg}}(s-\Theta)
  =c(s)\Gamma_\R(s)^{-1}$ with $c(s)=2^{1-s/2}\pi^{(1-s)/2}$ derived, not
  fitted.
* **The symmetrization collapse (108_91).** $\zeta'/\zeta(s)+\zeta'/\zeta(1-s)
  =\log\pi-\tfrac12\psi(\tfrac s2)-\tfrac12\psi(\tfrac{1-s}2)$: symmetrizing
  the logarithmic derivative of $\zeta$ under $s\mapsto1-s$ cancels **every**
  pole at a zero of $\xi$. Hence $\Phi$ is elementary and prime-free.
* **The strip is one-dimensional (108_91 Thm 2.1, Cor. 2.2–2.3).**
  $\Phi'(s)=-\psi_1(1-s)-\tfrac14\psi_1(\tfrac s2)-\tfrac14\psi_1(1-\tfrac s2)
  <0$ on $(0,1)$, so $\Phi$ has **exactly one** zero there, simple, at
  $s^*=0.301692388160422091519371\ldots$, and $\mathrm{rad}\,\Lambda^0$
  restricted to the strip is **one-dimensional**.
* **The embedding no-go (108_42 Thm 4.3, Cor. 4.4).** If RH holds, there is
  no isometric injection $(W_\infty,B_\infty)\hookrightarrow
  (V,\overline I_\partial)$. Uses only positive-definiteness of the diagonal
  sector, hence is independent of the stipulated parts of the construction.
  **Not** a statement about RH's truth.

### 2.2 Proved negatives

* **Stage 2 (108_38).** Principal invariance **fails**; the radical is spanned
  by point masses at the zeros of $\Phi$.
* **Stage 5, naive route (108_50).** No comparison map at generator level, in
  **either** direction: a nonzero dilation eigenfunction under an unbounded
  group cannot have compact support; and the Mellin transform of a compactly
  supported function has infinitely many zeros.
* **Stage 5, regularized route (108_53–55).** Condition III **fails**, by
  three independent obstructions — $\Phi$ is holomorphic at every zero of
  $\xi$; the mirror involution holds only on $\tfrac12+\Z$, where $\Phi\ne0$;
  and $\Phi$ has simple poles of residue $+1$ at $s=0,1$, exactly Stage 0's
  non-radical hyperbolic block. Condition I **holds** (explicit cutoff family
  constructed); Condition II fails for the toy model under both schemes
  examined. Condition III alone closes the route.
* **Stage 4, geometry (108_43).** G3 proved ($n_+=n_-=\aleph_0$
  unconditionally — no arithmetic invariant to measure); G2 and G4 **not
  proved**, both circular; see §3.
* **Earlier negatives, unchanged.** 108_01 (strict invariance kills every
  nonzero $f\in C_c$); 108_10 (Part I and Part II sit on disjoint
  test-function categories); 108_20 ($\mathcal G$ is non-finite-PL for every
  $s$); 108_30 (universal component-triviality is false).

## 3. The two circular results, recorded

G2 and G4 of Stage 4 were initially reported closed positively. They are not,
and the failure mode belongs on the record:

* **G2**: $B_\infty$ was *defined* to make the polar block hyperbolic, so
  "the Gram matrices coincide" is a normalization, not a theorem.
* **G4**: the pairing vector $U$ was reverse-engineered from $\cot$; the
  resulting identity is the Mittag-Leffler expansion of $\cot$, which is
  108_40 Proposition 6.1 — the construction's own input.

Both had **passing verifiers**. No numerical check could have caught either,
because both statements are arithmetically true; the defect is that they are
contentless. They were found by unwinding definitions. This is a limitation
of the verification discipline used throughout the phase and should be
assumed to apply elsewhere.

An analogous defect was found and fixed in 108_53: Theorem 3.1 originally
gave the residues of $\Phi$ at $s=0,1$ as $-2$ and $+2$ (both are $+1$), and
survived its verifier because that verifier tested only the blow-up *rate*, a
check that passes for any nonzero residue. It now tests the residue **value**
by refinement, with a control clause rejecting $\pm2$.

## 4. The through-line

Stages 2–5 each produced correct identities carrying no arithmetic
information, and there is a single mechanism (108_91). The construction that
made Stage 1 well-posed — passing to mass-zero differences, symmetric under
$s\mapsto1-s$ — is the same construction that makes $\Phi$ blind to the zeros
of $\zeta$. Summing a functional over the mirror orbit cancels its poles at
the zeros; pairing two functionals across the mirror does not. Stage 0 pairs;
Stages 2–4 symmetrize. That difference is the whole of Stage 5's
impossibility, and it was visible in advance.

## 5. Effect on the a/b/c/d table over $\Z$

**Unchanged: 0 of 4.** Row (a) has a space, a divisor theory, a well-posed
pairing and a proved assembly; it does not have an intersection number, and
Stage 5 proves the two natural routes to one are closed.

`ROW_A_STATUS` remains `partial`. Nothing in this phase bears on RH.

## 6. Entry conditions for Stage 6

Stage 6 is the primitive inequality — row (d). Two constraints are proved,
and both are prohibitions:

1. **Do not symmetrize the arithmetic side before pairing** (108_91 §4.2).
   Keep $\widehat f(\rho)$ and $\overline{\widehat g(\rho)}$ as separate
   coordinates. Any step replacing a two-argument pairing by a one-argument
   symmetrized functional provably discards the zeros. Note that 107_241
   Corollary 3.4's primitive form $Q(f)=-\sum_\rho m_\rho\widehat f(\rho)
   \overline{\widehat f(\rho')}$ is quadratic in one function but is **not** a
   symmetrization — it evaluates $\widehat f$ at $\rho$ and at $\rho'$ and
   multiplies them, rather than summing a fixed functional over the orbit.
   That distinction must be preserved.
2. **The archimedean fibre cannot enter as a sub-object** (108_43 §2). Its
   form is too positive: an isometric injection into the corner form would
   force infinitely many off-line zeros. It must enter as a quotient, an
   orthogonal complement, or with the opposite sign.

## 7. The open question this phase leaves

108_91 §5 states it: Theorem 1.2 shows that *symmetrizing* $\zeta'/\zeta$
destroys the zeros; it does **not** show that every route to Stage 1's
well-posedness must symmetrize. Whether a non-symmetrizing route to
well-posedness exists is open, and is the natural thing to settle before
committing to Stage 6.
