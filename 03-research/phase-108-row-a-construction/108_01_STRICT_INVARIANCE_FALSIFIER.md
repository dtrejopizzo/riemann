# 108.01 -- Strict Frobenius invariance forces the zero test function

## 1. Question

Fix the Frobenius action of 108_00 SS4,

\[
 (n\cdot f)(\lambda)=f(\lambda/n),\qquad n\in\mathbb N^\times,
 \tag{1.1}
\]

on \(f\in C_c((0,\infty),\mathbb R)\).  Does there exist \(f\neq0\) with
\(U_{n\cdot f}-U_f\) affine for every \(n\in\mathbb N^\times\)?

This is the question 107_240 SS3 already answered for the *two-variable*
chart descent \(T_{m,n}\) (its Theorem 3.1, the degree-normalized case).  Here
the action is the one fixed for this phase in 108_00 SS4: the *one-variable*
action on test functions alone, with \(n\) ranging only over \(\mathbb
N^\times\), not \(\mathbb Q_+^\times\).  The reduction below shows the two
questions collapse to the same mechanism, and confirms 107_240's conclusion
is not an artifact of using all of \(\mathbb Q_+^\times\) from the start.

## 2. Reduction to a translation-invariance statement

By 107_237 (2.3), \(u_f''(r)=f(r)/r\), and \(U_f\) is unique modulo affine
functions of \((x,y)\) (107_237 Theorem 2.1).  An affine correction
\(U\mapsto U+\alpha y+\beta x\) restricts, on the slice \(r=y/x\), to
\(u(r)\mapsto u(r)+\alpha r+\beta\), which has vanishing second derivative.
Hence

\[
 U_{n\cdot f}-U_f \text{ affine}
 \iff
 u_{n\cdot f}''(r)=u_f''(r)\ \text{a.e.}
 \iff
 \frac{(n\cdot f)(r)}r=\frac{f(r)}r\ \text{a.e.}
 \iff
 f(r/n)=f(r)\quad\forall r>0.
 \tag{2.1}
\]

This is exactly the reduction anticipated in 108_00 SS5.

### Lemma 2.1 (exponential coordinates)

Put \(r=e^t\), \(F(t):=f(e^t)\).  Then \(F\in C_c(\mathbb R)\) (compact
support in \(t\), since \(\exp:\mathbb R\to(0,\infty)\) is a
homeomorphism), and (2.1) is equivalent to

\[
 F(t-\log n)=F(t)\qquad\forall t\in\mathbb R,\ \forall n\in\mathbb N^\times.
 \tag{2.2}
\]

**Proof.** Direct substitution: \(f(r/n)=f(e^{t-\log n})=F(t-\log n)\) and
\(f(r)=F(t)\). \(\square\)

## 3. The invariance group is dense

### Lemma 3.1 (from one-sided to two-sided, and to a group)

If (2.2) holds for every \(n\in\mathbb N^\times\), it holds with
\(-\log n\) in place of \(\log n\), and hence for every element of

\[
 G:=\Big\{\sum_{p}e_p\log p:\ e_p\in\mathbb Z,\ \text{finitely many nonzero}\Big\}
 =\log\mathbb Q_+^\times .
 \tag{3.1}
\]

**Proof.** Fix \(n\) and apply (2.2) at the point \(t'=t+\log n\):
\(F(t'-\log n)=F(t')\), i.e. \(F(t)=F(t+\log n)\).  So \(F\) is invariant
under \(+\log n\) as well as \(-\log n\), for every \(n\in\mathbb N^\times\).
Since invariance under a set of translations closes under composition and
inversion, \(F\) is invariant under the subgroup of \((\mathbb R,+)\) they
generate.  Every generator \(\log n\) decomposes via unique factorization as
\(\sum_p v_p(n)\log p\), so the generated group is exactly the
\(\mathbb Z\)-span of \(\{\log p:p\text{ prime}\}\), which is \(\log
\mathbb Q_+^\times\). \(\square\)

### Lemma 3.2 (density)

\(G=\log\mathbb Q_+^\times\) is a dense subgroup of \((\mathbb R,+)\).

**Proof.** Every subgroup of \(\mathbb R\) is either cyclic (isomorphic to
\(\mathbb Z\)) or dense.  \(G\) is not cyclic: if \(G=\mathbb Z\alpha\) for
some \(\alpha\), then \(\log2=m\alpha\) and \(\log3=k\alpha\) for integers
\(m,k\), giving \(\log2/\log3=m/k\in\mathbb Q\).  But
\(\log2/\log3\notin\mathbb Q\), since \(2^k=3^m\) has no solution in
positive integers other than forcing \(k=m=0\) (unique factorization: the
left side is a power of \(2\), the right side a power of \(3\)).  Hence
\(G\) is not cyclic, so it is dense. \(\square\)

This is the identical mechanism recorded in 106_185 (1) and used again in
107_240 SS3 for the \(\mathbb Q_+^\times\)-orbit case; Lemma 3.1 shows that
restricting the hypothesis to \(n\in\mathbb N^\times\) loses nothing, because
the one-variable Frobenius action already generates the full group under
composition.

## 4. The falsifier

### Theorem 4.1

The only \(f\in C_c((0,\infty),\mathbb R)\) with \(U_{n\cdot f}-U_f\) affine
for every \(n\in\mathbb N^\times\) is \(f=0\).

**Proof.** By SS2--3, this is equivalent to: \(F\in C_c(\mathbb R)\) is
invariant under the dense subgroup \(G\subset\mathbb R\).  Let \(\mu\) be
Lebesgue measure; fix \(t_0\) and \(a\in\mathbb R\).  Choose \(g_j\in G\) with
\(g_j\to a\); by continuity \(F(t_0-g_j)\to F(t_0-a)\), and each
\(F(t_0-g_j)=F(t_0)\) by hypothesis, so \(F(t_0-a)=F(t_0)\).  Since \(a\) was
arbitrary, \(F\) is constant.  A constant function with compact support is
identically \(0\).  Hence \(F\equiv0\), i.e. \(f\equiv0\). \(\square\)

### Corollary 4.2 (the incompatible hypothesis, named exactly)

The proof uses exactly three hypotheses on \(f\): continuity, compact
support, and the invariance (2.1) for all \(n\in\mathbb N^\times\).
Continuity is never dropped (SS3's density argument is genuinely a
continuity argument).  Invariance is the hypothesis under test.  The
hypothesis that fails to survive contact with density is

\[
 \boxed{\text{compact angular support.}}
\]

A continuous function invariant under a dense group of translations that is
*not* required to have compact support need not vanish (constants are the
extreme case; 108.02 below produces the full non-constant family once
strict invariance itself is relaxed).  It is compactness of the support,
conjoined with strict invariance, that is unsatisfiable.

## 5. Cross-references, not re-derivations

* 106_185 Theorem 2.1 proves the same dense-orbit-kills-invariant-object
  mechanism for diagonal sampling forms on \(\mathcal S(\mathbb R)\); the
  group \(G\) of (3.1) is verbatim its group (1).  It is cited, not
  modified.
* 107_240 Theorem 3.1 proves the degree-normalized two-variable chart
  descent \(f(r)=f(qr)\ \forall q\in\mathbb Q_+^\times\) forces \(f=0\), by
  the identical density argument but starting from a hypothesis already
  posed over all of \(\mathbb Q_+^\times\).  Lemma 3.1 above is the missing
  half-step showing the one-variable, \(\mathbb N^\times\)-only hypothesis
  of 108_00 SS4 generates the same group, so Theorem 4.1 is not a new
  mechanism, only a confirmation that restricting to \(\mathbb N^\times\)
  costs nothing.

## 6. Scope

Proved here, unconditionally, no zero input:

* Lemma 2.1: the affine-mod-out reduction to a pure translation identity;
* Lemma 3.1: the one-sided \(\mathbb N^\times\) hypothesis generates the full
  group \(\log\mathbb Q_+^\times\) under composition;
* Lemma 3.2: that group is dense;
* Theorem 4.1: strict invariance forces \(f=0\) on \(C_c((0,\infty))\);
* Corollary 4.2: the identified incompatible hypothesis is compact angular
  support, not continuity and not the invariance law itself.

Not claimed:

* nothing about characters other than the trivial one (\(\chi\equiv1\)) is
  addressed here; that is 108.02;
* this note does not touch \(U_f\) itself as an object on the quotient
  topos, only the test-function condition that would make \(D_{n\cdot
  f}-D_f\) principal.

## 7. Verifier

`108_01_strict_invariance_falsifier.py`:

1. constructs five nonzero, nonnegative, compactly supported continuous
   candidate test functions (smooth bumps, triangle bumps, truncated
   Gaussians re-based to have exactly compact support) on \([A,B]\subset
   (0,\infty)\);
2. for \(n=2,3,4,5\), samples \(f(r/n)-f(r)\) on a fine grid and confirms it
   is *not* uniformly zero for any nonzero candidate (falsifying strict
   invariance directly, without invoking the general theorem);
3. numerically exhibits density of \(G=\log\mathbb Q_+^\times\): for a bank
   of target reals, finds integer combinations \(\sum e_p\log p\)
   (\(p\le 19\), \(|e_p|\le 40\)) approximating the target to within
   \(10^{-3}\), and confirms the approximating error shrinks as the search
   window widens, consistent with (but not a substitute for) Lemma 3.2's
   proof;
4. confirms the algebraic fact used in Lemma 3.2 (\(\log2/\log3\) is not
   close to any rational \(m/k\) with small \(k\) beyond the accuracy
   forced by irrationality) as a sanity check, and confirms Lemma 3.1's
   group-closure claim symbolically on a finite generating set;
5. prints `VERDICT: NO` for existence of a nonzero strictly invariant test
   function, matching Theorem 4.1.
