# 107.206 -- Morishita transports the balanced local character, but forgets packet differences

## 1. Fixed published inputs

Meyer [arXiv:math/0412277, (2)] uses the involution

\[
 (Jf)(x)=x^{-1}f(x^{-1})
 \tag{1.1}
\]

and obtains, at a finite prime,

\[
 W_p(f)=W_p^+(f)+W_p^+(Jf),\qquad
 W_p^+(f)=\log p\sum_{e\geq1}f(p^e).
 \tag{1.2}
\]

Equivalently,

\[
 W_p(f)=\log p\sum_{e\geq1}
 \bigl(f(p^e)+p^{-e}f(p^{-e})\bigr).
 \tag{1.3}
\]

Morishita [arXiv:2508.15971v5, Lemma 3.5 and Theorem 3.6]
constructs an anti-equivariant continuous map

\[
 \Psi_{\mathbb Q}:\mathfrak X_{\mathbb Q}
 \longrightarrow\mathscr X_{\mathbb Q}
 \tag{1.4}
\]

and proves that every Deninger circle in the packet \(\Gamma_p\) maps
onto the Connes--Consani circle \(C_p\).  Anti-equivariance changes the
multiplicative flow coordinate from \(x\) to \(x^{-1}\).  On test
densities this is precisely the modular involution (1.1).

## 2. The invariant local distribution

### Proposition 2.1

For every admissible test function \(f\),

\[
 W_p(Jf)=W_p(f).
 \tag{2.1}
\]

In contrast, \(W_p^+\) is not invariant under \(J\).

### Proof

Since \(J^2=1\), equation (1.2) gives

\[
 W_p(Jf)=W_p^+(Jf)+W_p^+(J^2f)
        =W_p^+(Jf)+W_p^+(f)=W_p(f).
\]

Take a nonzero nonnegative smooth function supported in \((1,\infty)\)
and meeting a prime power.  Then \(W_p^+(f)>0\), while
\(W_p^+(Jf)=0\).  Thus neither oriented half descends independently
through the flow reversal. \(\square\)

This is not an optional symmetrization.  The second term in (1.2) is
the second nuclear trace term in Meyer's geometric character
calculation.  It is exactly what makes the local character compatible
with Morishita's anti-equivariant bridge.

## 3. Pushforward and its exact packet kernel

Let \(\mu_{p,a}\) denote the normalized return-trace distribution on a
circle \(\gamma_{p,a}\) in the packet \(\Gamma_p\).  Its return times
are \(e\log p\).  Because the restriction of \(\Psi_{\mathbb Q}\) maps
every such circle onto the same \(C_p\), reverses its flow, and Haar
orbit trace is invariant under phase translation, Proposition 2.1
gives

\[
 (\Psi_{\mathbb Q})_*\mu_{p,a}=W_p
 \quad\text{for every }a.
 \tag{3.1}
\]

There is no hidden covering multiplicity in (3.1).  An
anti-equivariant map between two transitive \(\mathbb R_+\)-orbits with
stabilizer \(p^{\mathbb Z}\) is determined by the image \(c\) of the
identity coset and has the form \(x\mapsto c/x\).  It is therefore a
homeomorphism of circles, of degree \(-1\).

Consequently, for every finite packet combination,

\[
 (\Psi_{\mathbb Q})_*
 \left(\sum_a c_a\mu_{p,a}\right)
 =\left(\sum_a c_a\right)W_p.
 \tag{3.2}
\]

### Theorem 3.1 (finite-character transport with packet no-go)

Morishita's map transports Meyer's balanced finite-prime character from
Deninger return orbits to the Connes--Consani periodic orbit.  On the
span of normalized packet orbit traces its kernel is exactly

\[
 \left\{(c_a):\sum_a c_a=0\right\}.
 \tag{3.3}
\]

Hence the base Connes--Consani orbit retains the local character of
\(\zeta\), but cannot retain a packet-sensitive or Galois-sensitive
current without an enriched coefficient system upstairs.

### Proof

Equation (3.1) follows from Morishita's Theorem 3.6 and Proposition
2.1.  Linearity gives (3.2).  The distribution \(W_p\) is nonzero:
choose the positive test function used in Proposition 2.1.  Therefore
the right side of (3.2) vanishes if and only if \(\sum_a c_a=0\), which
proves (3.3). \(\square\)

## 4. Relation to the Phase 107 rows

This closes one previously missing part of the interface between rows
(b) and (c): the finite-place *balanced trace character* survives the
published Deninger--Connes--Consani bridge.  It also proves a precise
loss statement.  Galois/packet differences, of the kind already shown
necessary by the local-component obstruction of `107_133`, cannot be
recovered from a scalar current on the base orbit.

The theorem does **not** construct:

1. a current on the arithmetic square;
2. an intersection product or a diagonal class;
3. the archimedean term \(W_\infty\);
4. a packet-enriched sheaf retaining the kernel (3.3);
5. a Hodge pairing or positivity theorem.

Thus it neither reopens legacy row (c) nor promotes Papers A--E.

## 5. Falsifier

`107_206_morishita_balanced_local_character_pushforward.py` evaluates
the two terms of (1.3) independently on five actual prime orbit
lengths and asymmetric smooth test functions.  It can return `NO` if
flow inversion fails to exchange the terms, if an oriented half appears
to descend, or if a nonzero-sum packet combination is spuriously lost.
