# Phase 121 -- inactive-prime pair return rigidity

## Status

This note proves a new equality-state exclusion criterion.  A single prime
whose logarithm exceeds the window diameter is invisible after compression.
Two oppositely oriented inactive primes are not invisible: their excursion
leaves the window and returns with displacement `log(p/q)`.  Consecutive
large primes make that displacement tend to zero.  Hence asymptotic
annihilation of only these scalar mixed returns forces the state itself to
vanish.

No positive all-prime sum, norm comparison, critical-zero divisor, or
Cartwright argument is used.  The remaining unproved statement is a source
law forcing the mixed return to vanish on a first-contact state.

## 1. Compression is linear but not multiplicative

Let `I_T=(-T,T)`, let `P=P_T` be the orthogonal projection onto functions
supported in `I_T`, and let

\[
 (U_af)(t)=f(t-a).
\]

For `a>2T`,

\[
                         PU_aP=PU_{-a}P=0.          \tag{1.1}
\]

For `a,b>2T`, define the oppositely oriented compression defect

\[
 \mathcal R_T(a,b)
 :=PU_a(I-P)U_{-b}P.                               \tag{1.2}
\]

### Proposition 1.1 -- exact inactive-pair activation

For every `a,b>2T`,

\[
 \boxed{\mathcal R_T(a,b)=PU_{a-b}P.}              \tag{1.3}
\]

#### Proof

Since `U_{-b}P` is supported in `(-T-b,T-b)`, it lies outside `I_T`.
Thus `(I-P)U_{-b}P=U_{-b}P`.  The group law gives

\[
 PU_a(I-P)U_{-b}P=PU_aU_{-b}P=PU_{a-b}P.
\]

QED.

Thus two factors which are separately zero after compression can have a
nonzero mixed compression.  This is the smallest exact coordinate in which
the missing mixed-prime information survives.

## 2. Cofinal consecutive-prime rigidity

Let `p_n` be the `n`-th prime and put

\[
 a_n=\log p_{n+1},\qquad b_n=\log p_n,
 \qquad c_n=a_n-b_n.
\]

The prime number theorem implies `p_n~n log n`, hence

\[
                         c_n=\log(p_{n+1}/p_n)\longrightarrow0. \tag{2.1}
\]

For all sufficiently large `n`, both `a_n,b_n` exceed `2T`.

### Theorem 2.1 -- scalar mixed-return exclusion

Let `F in L2(I_T)`.  If

\[
 \left\langle F,
  \mathcal R_T(\log p_{n+1},\log p_n)F
 \right\rangle\longrightarrow0,                   \tag{2.2}
\]

then `F=0`.

The same conclusion follows if only the real part in (2.2) tends to zero.

#### Proof

By Proposition 1.1, the scalar in (2.2) is

\[
             \langle F,PU_{c_n}PF\rangle
             =\langle F,U_{c_n}F\rangle.           \tag{2.3}
\]

Translations are strongly continuous on `L2(R)`.  Equation (2.1) therefore
gives

\[
 \langle F,U_{c_n}F\rangle\longrightarrow\|F\|_2^2. \tag{2.4}
\]

Comparison of (2.2) and (2.4) yields `||F||_2=0`.  QED.

### Corollary 2.2 -- the weakest current target

A hypothetical first-contact state is excluded if its source equation
implies merely

\[
 \operatorname {Re}\left\langle F,
 PU_{\log p_{n+1}}(I-P)U_{-\log p_n}PF
 \right\rangle=o(1).                               \tag{2.5}
\]

No assertion is required prime by prime at a fixed scale, and no summation
over primes is required.  In particular (2.5) is strictly weaker in
topology than finite all-prime seam energy and weaker in data than the
cofinal first-harmonic law: it observes one scalar along one cofinal chain.

The word **mixed return** in (2.5) means the normalized root operator, not
its physical von Mangoldt multiple.  If

\[
 w_p={\log p\over\sqrt p},                          \tag{2.6}
\]

then

\[
 w_{p_{n+1}}w_{p_n}
 \langle F,\mathcal R_T(\log p_{n+1},\log p_n)F\rangle
 \longrightarrow0                                  \tag{2.7}
\]

for every `F`, simply because the coefficient tends to zero.  Thus (2.7)
has no rigidity content.  A physical source identity must give exact
vanishing, or an estimate

\[
 \text{physical mixed flux}
       =o(w_{p_{n+1}}w_{p_n}),                     \tag{2.8}
\]

before division by the known nonzero weights.  Forgetting this
normalization would create a false proof.

## 3. Why this is not the phase-106 positive ratio bank

Phase 106.137 proves the exact positive variance identity for finite
prime-ratio graphs, its failure to observe a continuum with finitely many
edges, divergence of the raw all-prime bank, and the Krein sign introduced
by PNT centering.  Theorem 2.1 uses none of those operations:

* it does not add positive ratio energies;
* it does not seek a uniform inequality;
* it takes no cofinal Hilbert direct sum;
* it does not center a divergent prime measure;
* it uses the near-identity limit only after restricting to a hypothetical
  equality state.

The theorem is consequently not refuted by the finite-character falsifier
of 106.137: the displacement itself tends to zero, so strong continuity,
not finite-path observability, is the mechanism.

There is nevertheless a binding warning.  If (2.5) is obtained by first
placing all pair returns in a positive space and then shorting that space,
the construction has returned to the retired phase-120 architecture.
The admissible source must produce (2.5) as a signed second-order identity
before any norm or placewise orthogonalization.

## 4. Exact remaining source calculation

The localized Weil operator is linear in the von Mangoldt contacts.  Hence
every prime `p>exp(2T)` is invisible to the first-contact equation at first
order.  Proposition 1.1 shows that the first nontrivial inactive datum is
the **opposite-orientation second multiplicative defect**

\[
 (x,y)\longmapsto
 P\,d\pi_+(x)(I-P)d\pi_-(y)P.                     \tag{4.1}
\]

On the prime roots `(x,y)=(p_{n+1},p_n)`, its diagonal matrix coefficient
is exactly (2.5).  Therefore the one remaining calculation is sharply
posed:

> Derive from the unsupertraced Euler--Mobius source identity, on a
> first-contact vector, that the real scalar mixed defect (4.1) is `o(1)`
> for consecutive inactive primes.

Equivalently, in the physical normalization, prove the relative estimate
(2.8).  Absolute `o(1)` for the weighted current is automatic and is not an
acceptable source law.

This asks for neither equality of the two causal vectors nor vanishing of a
whole annular current.  It asks only for asymptotic cancellation of their
single mixed scalar as the two prime scales coalesce.

The universal conormal countermodel in `P121_F2_DIRECT_CLOSURE_AUDIT.md`
does not satisfy such a cofinal multiplicative source law, so Theorem 2.1
is sensitive to information absent from that model.  Conversely, merely
postulating (4.1) is not a proof: by Theorem 2.1 its asymptotic vanishing is
already a faithful exclusion theorem.

## 5. Closure consequence

If the source calculation in Section 4 is proved, then

```text
first contact
 -> consecutive inactive mixed return is o(1)
 -> ||F||^2 = 0                         (Theorem 2.1)
 -> no first contact
 -> global finite-window sign
 -> global square
 -> cofinal row (d).
```

Thus the global square is not closed here.  What is closed is a new,
zero-divisor-free and non-positive-lift terminal descent from one scalar
source asymptotic to `F=0`.
