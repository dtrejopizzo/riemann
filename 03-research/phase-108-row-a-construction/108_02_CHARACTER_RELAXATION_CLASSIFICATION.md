# 108.02 -- The character relaxation: exit from compact support is forced, and lands exactly on Mellin monomials

## 1. Question

108.01 shows strict invariance kills every nonzero \(f\in C_c((0,\infty))\).
108_00 SS5 asks for the relaxation: classify all \(f\neq0\) and characters
\(\chi:\mathbb Q_+^\times\to\mathbb R^\times\) with

\[
 f(r/n)=\chi(n)f(r)\qquad\forall n\in\mathbb N^\times,\ \forall r>0.
 \tag{1.1}
\]

\(f(r)=r^s\) gives \(\chi(n)=n^{-s}\); 108_00 asks for the general solution
and states the informal expectation "\(r^s\) times a factor periodic in
\(\log r\)".  The theorem below is sharper than that expectation, and the
gap between the two is itself the main content of this note: **the periodic
factor is forced to be trivial**, by the same density mechanism as 108.01,
now acting on \(\chi\) instead of on \(f\).  This is not a re-run of 108.01;
it is a genuinely new rigidity statement (Theorem 3.1) about which
characters can occur at all.

Throughout, \(f\) is required continuous on \((0,\infty)\), matching the
ambient test-function category of 107_237 with compact support dropped
(dropping continuity as well would be a different, much weaker, category;
SS5 records what happens then).

## 2. Two free lemmas: multiplicativity and automatic extension to \(\mathbb Q_+^\times\)

### Lemma 2.1 (\(\chi\) is forced to be totally multiplicative)

If \(f\neq0\) satisfies (1.1), then \(\chi(nm)=\chi(n)\chi(m)\) for all
\(n,m\in\mathbb N^\times\).

**Proof.** Apply (1.1) twice: \(f(r/(nm))=\chi(m)f(r/n)=\chi(m)\chi(n)f(r)\).
Also directly \(f(r/(nm))=\chi(nm)f(r)\).  Since \(f\neq0\), there is
\(r_0\) with \(f(r_0)\neq0\); evaluating both identities at \(r_0\) gives
\(\chi(nm)=\chi(n)\chi(m)\). \(\square\)

### Lemma 2.2 (the \(\mathbb N^\times\) hypothesis reproduces the full \(\mathbb Q_+^\times\) law, and the extension is unobstructed)

If \(f\neq0\) satisfies (1.1), then \(\chi(n)\neq0\) for every \(n\), and
setting \(\chi(a/b):=\chi(a)/\chi(b)\) for \(a,b\in\mathbb N^\times\) is a
well-defined extension of \(\chi\) to a group homomorphism
\(\chi:(\mathbb Q_+^\times,\times)\to(\mathbb R^\times,\times)\), and

\[
 f(r/q)=\chi(q)f(r)\qquad\forall q\in\mathbb Q_+^\times.
 \tag{2.1}
\]

**Proof.** If \(\chi(n_0)=0\) for some \(n_0\), (1.1) gives \(f(r/n_0)=0\)
for every \(r\), i.e. \(f\equiv0\), excluded.  So \(\chi(n)\in\mathbb
R^\times\) for all \(n\).  Evaluating (1.1) at \(r'=r/n\) and rearranging as
in 108.01 Lemma 3.1 gives \(f(r n)=\chi(n)^{-1}f(r)\), i.e. (1.1) extended
to \(q=1/n\) with multiplier \(\chi(n)^{-1}\).  Composing with Lemma 2.1,
(1.1) extends to every \(q=a/b\in\mathbb Q_+^\times\) with multiplier
\(\chi(a)\chi(b)^{-1}\).  Well-definedness: if \(a/b=a'/b'\) then
\(ab'=a'b\) as elements of \(\mathbb N^\times\), so \(\chi(ab')=\chi(a'b)\)
as the same input to the same function \(\chi\); total multiplicativity
(Lemma 2.1) turns this into \(\chi(a)\chi(b')=\chi(a')\chi(b)\), i.e.
\(\chi(a)/\chi(b)=\chi(a')/\chi(b')\).  Hence \(\chi(a/b):=\chi(a)/\chi(b)\)
is a well-defined function of the rational \(a/b\) alone, and it is
multiplicative by construction. \(\square\)

So the compatibility question raised in 108_00 SS5 has a clean, unconditional
answer at this stage: **the extension of \(\chi\) from \(\mathbb N^\times\)
to \(\mathbb Q_+^\times\) is automatic and imposes no constraint on \(s\)**.
This is the easy half of the classification. The hard half is next, and it
does constrain \(\chi\) severely -- not by breaking the extension, but by
ruling out almost every totally multiplicative \(\chi\) as incompatible
with a continuous nonzero \(f\).

## 3. The rigidity theorem: continuity forces \(\chi\) to be a Mellin character

A totally multiplicative function \(\mathbb N^\times\to\mathbb R^\times\)
has one free nonzero real parameter per prime (\(\chi(p)\), arbitrary
nonzero, for each prime \(p\)) -- an infinite-dimensional family. The
following theorem collapses it to the one-parameter family \(n^{-s}\).

### Theorem 3.1 (rigidity of the character)

Let \(f\in C((0,\infty),\mathbb R)\), \(f\neq0\), and let
\(\chi:\mathbb Q_+^\times\to\mathbb R^\times\) be the (forced, by Lemma 2.2)
multiplicative extension satisfying (2.1).  Then there is a unique
\(s\in\mathbb R\) with

\[
 \chi(q)=q^{-s}\qquad\forall q\in\mathbb Q_+^\times .
 \tag{3.1}
\]

**Proof.** Work in exponential coordinates \(r=e^t\), \(F(t)=f(e^t)\),
\(\Gamma=\log\mathbb Q_+^\times\) (dense in \(\mathbb R\) by 108.01 Lemma
3.2). Equation (2.1) reads

\[
 F(t-a)=\chi(e^a)F(t)\qquad\forall a\in\Gamma,\ t\in\mathbb R.
 \tag{3.2}
\]

*Step 1 (\(\chi\circ\exp\) is continuous at \(0\)).* Fix \(t_0\) with
\(F(t_0)\neq0\) (exists since \(F\not\equiv0\)); by continuity of \(F\) such
a \(t_0\) has a neighborhood on which \(F\) does not vanish. For
\(a_j\in\Gamma\), \(a_j\to0\): \(F(t_0-a_j)\to F(t_0)\) by continuity of
\(F\), and \(F(t_0-a_j)=\chi(e^{a_j})F(t_0)\) by (3.2), so
\(\chi(e^{a_j})\to1=\chi(e^0)\).

*Step 2 (continuity at \(0\) plus homomorphism gives continuity
everywhere).* Write \(L(a):=\chi(e^a)\) for \(a\in\Gamma\); \(L\) is a group
homomorphism \((\Gamma,+)\to(\mathbb R^\times,\times)\) by Lemma 2.1--2.2.
For \(a\in\Gamma\) and \(h_j\to0\) in \(\Gamma\): \(L(a+h_j)=L(a)L(h_j)\to
L(a)\cdot1=L(a)\) by Step 1. So \(L\) is continuous at every point of
\(\Gamma\).

*Step 3 (unique continuous extension to \(\mathbb R\)).* \(\Gamma\) is
dense in \(\mathbb R\) and \(L:\Gamma\to\mathbb R^\times\) is continuous, so
\(L\) extends uniquely to a continuous \(\bar L:\mathbb R\to\mathbb R\)
(standard extension of a continuous function on a dense subgroup of a
complete metric space; uniqueness is immediate from density). Continuity of
the group law and density of \(\Gamma\) show \(\bar L\) is again a
homomorphism: for \(a,b\in\mathbb R\), take \(a_j,b_j\in\Gamma\) with
\(a_j\to a\), \(b_j\to b\); then
\(\bar L(a+b)=\lim L(a_j+b_j)=\lim L(a_j)L(b_j)=\bar L(a)\bar L(b)\).

*Step 4 (classification of continuous homomorphisms \((\mathbb
R,+)\to(\mathbb R^\times,\times)\)).* \(\mathbb R\) is connected and
\(\bar L\) is continuous, so \(\bar L(\mathbb R)\) is a connected subset of
\(\mathbb R^\times\); since \(\bar L(0)=1>0\), \(\bar L(\mathbb R)\subset
\mathbb R_{>0}\). A continuous homomorphism \((\mathbb R,+)\to(\mathbb
R_{>0},\times)\) is \(\bar L(a)=e^{ca}\) for a unique \(c\in\mathbb R\)
(classical: \(\log\bar L\) is a continuous additive function \(\mathbb
R\to\mathbb R\), hence linear). Set \(s:=-c\).

*Step 5 (transport back to \(\chi\) and to \(f\)).* Restricting
\(\bar L(a)=e^{-sa}\) to \(a=\log q\in\Gamma\) gives
\(\chi(q)=q^{-s}\), proving (3.1). Uniqueness of \(s\) is immediate since
\(q\mapsto q^{-s}\) determines \(s\) (e.g. from \(q=2\)). \(\square\)

### Remark 3.2 (what this rules out)

Theorem 3.1 excludes, in particular: (a) any nontrivial sign character
(e.g. \(\chi(n)=(-1)^{\Omega(n)}\), Liouville's \(\lambda\)) times
\(n^{-s}\); (b) any character assigning independent exponents to distinct
primes (\(\chi(p)=p^{-s_p}\) with the \(s_p\) not all equal); (c) any
non-real-analytic modulation of \(n^{-s}\). All of these are perfectly good
totally multiplicative functions on \(\mathbb N^\times\) (Lemma 2.1 alone
does not exclude them); it is the *conjunction* with a continuous nonzero
\(f\) via (1.1) that is impossible for them. The verifier illustrates this
concretely with \(\lambda\).

## 4. The functional equation for \(f\) collapses to a pure monomial

Given Theorem 3.1, (3.2) becomes \(F(t-a)=e^{-sa}F(t)\) for \(a\in\Gamma\),
hence (both sides continuous in \(a\), \(\Gamma\) dense) for **every**
\(a\in\mathbb R\):

\[
 F(t-a)=e^{-sa}F(t)\qquad\forall a,t\in\mathbb R.
 \tag{4.1}
\]

### Theorem 4.1 (the classification)

The nonzero continuous solutions of (1.1) are exactly

\[
 \boxed{f(r)=c\,r^s,\qquad c\in\mathbb R^\times,\ s\in\mathbb R,\qquad
 \chi(n)=n^{-s}.}
 \tag{4.2}
\]

**Proof.** Set \(a=t\) in (4.1): \(F(0)=e^{-st}F(t)\), i.e.
\(F(t)=F(0)e^{st}\), so \(f(r)=F(0)r^s\) with \(F(0)=f(1)\neq0\)
(else \(f\equiv0\) by (4.1) itself). Conversely \(f(r)=cr^s\) satisfies
(1.1) with \(\chi(n)=n^{-s}\) by direct substitution. \(\square\)

There is **no residual log-periodic factor**: 108_00's informal expectation
of "\(r^s\) times a factor periodic in \(\log r\)" is corrected by Theorem
4.1 to "\(r^s\) times a constant." A genuine period would require the
invariance group in (3.2) to be a *discrete, rank-one* subgroup of
\(\mathbb R\); but SS3's Step 1--3 shows the group generated by requiring
(1.1) to hold for *every* \(n\in\mathbb N^\times\) simultaneously is dense
(108.01 Lemma 3.2), which is exactly what forces the periodic factor \(P\)
in \(F(t)=e^{st}P(t)\) to itself be \(\Gamma\)-invariant and hence, by the
108.01 mechanism applied to \(P\), constant. (Concretely:
\(P(t):=e^{-st}F(t)\) satisfies \(P(t-a)=P(t)\) for \(a\in\Gamma\) by
(4.1), which is 108.01 SS3's hypothesis on \(P\) verbatim -- except that here
\(P\) is *not* required to have compact support, so 108.01's conclusion
stops at "constant" rather than continuing on to "zero". This is exactly
the mechanism by which relaxing invariance to character-covariance escapes
108.01's no-go: it trades the vanishing conclusion for a nonvanishing
constant, at the price of abandoning compact support entirely, since
\(r^s\) is nowhere zero for \(c\neq0\).)

### Corollary 4.2 (\(s=0\) recovers exactly what 108.01 excluded)

At \(s=0\), (4.2) gives \(f\equiv c\), the constant function -- pure
\(\chi\equiv1\) invariance. This is precisely the object 108.01 shows
cannot be compactly supported and nonzero. The two notes are therefore
consistent statements about the same one-parameter family (4.2) at its two
extremes: 108.01 forbids the \(s=0\), compactly-supported corner; 108.02
identifies the entire family \(f=cr^s\) and shows it is the *only* way out,
necessarily leaving compact support for every \(s\) (including \(s=0\)).

## 5. Without continuity

Dropping continuity turns (1.1) into an unconstrained Cauchy-type equation:
using a Hamel basis of \(\mathbb R\) over \(\mathbb Q\) one can build
non-measurable multiplicative characters \(\mathbb Q_+^\times\to\mathbb
R^\times\) with no continuous extension, and correspondingly wild
non-measurable \(f\). These are set-theoretic artifacts, not part of the
test-function category used anywhere in Phase 107/108 (which is always at
least continuous, usually smooth). We record, without proof (classical
Fréchet/Sierpinski-type fact for measurable solutions of Cauchy's equation
on locally compact groups), that *Lebesgue-measurable* \(f\) already forces
continuity of \(\chi\) and hence the same conclusion (4.2); so relaxing
continuity to measurability changes nothing. Relaxing to arbitrary
(non-measurable) \(f\) is outside the scope of this phase and is not
pursued.

## 6. What (4.2) is, structurally

\(f_s(r)=r^s\) is exactly the kernel of the Mellin transform used
throughout Phase 107 (107_239 SS1, 107_241 SS1: \(\hat f(s)=\int_0^\infty
f(u)u^s\,d^\times u\)). Theorem 4.1 says: **the only way to repair strict
Frobenius invariance is to promote \(f\) itself to a (formal) Mellin
kernel, graded by the same variable \(s\) at which the corner pairing
\(I_\partial\) is already evaluated in 107_241 (2.1)-(2.2).** This is the
structural conclusion 108_00 SS5 asks for: descent forces exit from compact
support into a character-graded family, indexed by exactly the Mellin
degree \(s\), with **no extra freedom** beyond that one real (or, allowing
complex characters into \(\mathbb C^\times\), one complex) parameter.

### Remark 6.1 (complex characters)

If one allows \(\chi:\mathbb Q_+^\times\to\mathbb C^\times\) and complex
\(f\), the identical proof (with \(\mathbb C^\times\) connected, and
continuous homomorphisms \((\mathbb R,+)\to(\mathbb C^\times,\times)\)
classified as \(a\mapsto e^{ca}\), \(c\in\mathbb C\)) gives
\(\chi(q)=q^{-s}\), \(f(r)=cr^s\) for \(s\in\mathbb C\). This is the same
\(s\) used as the evaluation coordinate for zeros \(\rho\) in 107_240
Theorem D and 107_241; the present note does not use that fact for
anything beyond noting the terminology matches. Nothing here computes
\(\hat f\) at a zero, and no zero is used in this construction.

## 7. Scope

Proved here, unconditionally:

* Lemma 2.1--2.2: multiplicativity and the automatic, unobstructed
  extension of \(\chi\) from \(\mathbb N^\times\) to \(\mathbb Q_+^\times\);
* Theorem 3.1: continuity of \(f\) forces \(\chi\) into the one-parameter
  Mellin family \(n^{-s}\), excluding every other totally multiplicative
  character;
* Theorem 4.1: the complete classification \(f=cr^s\), with no residual
  periodic factor -- sharper than 108_00's informal expectation;
* Corollary 4.2: consistency with 108.01 at \(s=0\).

Not established here, and explicitly deferred:

* what object plays the role of \(D_f\) or \(U_f\) for these
  non-compactly-supported \(f\) (108.03);
* whether this graded family resolves 107_240 Theorem C's well-posedness
  complaint (108.04);
* any pairing of these objects against \(I_\partial\) (open; 108.03/108.10
  record why it is not currently well posed either).

## 8. Verifier

`108_02_character_relaxation_classification.py`:

1. confirms \(f=r^s\) satisfies (1.1) with \(\chi(n)=n^{-s}\) to floating
   precision, for a bank of \(s\) and \(n\);
2. confirms total multiplicativity of \(n^{-s}\) and the well-definedness
   of the extension \(\chi(a/b)=\chi(a)/\chi(b)\) on several equal
   fractions with different representations (Lemma 2.2);
3. falsifies rigidity numerically for two classes of non-Mellin totally
   multiplicative characters (Liouville's \(\lambda\); independent
   per-prime exponents), by exhibiting sequences \(q_j\to1\) in
   \(\mathbb Q_+^\times\) along which \(\chi(q_j)\) does *not* converge to
   \(1\), which is exactly the Step-1 continuity-at-identity property that
   Theorem 3.1 shows is necessary;
4. confirms the same convergence *does* hold for \(n^{-s}\), by contrast;
5. confirms Corollary 4.2 (\(s=0\) gives the constant function, matching
   108.01's excluded case) and prints `VERDICT: YES` for the classification
   holding as stated.
