# P121 -- coprime contact does not kill the opposite causal return

## Status

Rows (a)--(c) contain an exact coprime vanishing which at first sight looks
like the missing nonlinear source law:

\[
 \mathbb F_p\otimes_{\mathbb Z}^{\mathbf L}\mathbb F_q\simeq0
 \qquad(p\ne q).                                    \tag{1.1}
\]

This note checks its interaction with the inactive-prime mixed return of
phase 121.  The verdict is exact: (1.1) controls same-orientation
composition, whereas the detecting return is an opposite-orientation
Toeplitz defect.  Bézout does not contract that defect.  Importing the
ordinary divisor Koszul homotopy would moreover annihilate the logarithmic
contact itself, reproducing the phase-104 stop-gate.

## 1. The two products have different labels

Let `U_a f(t)=f(t-a)`.  Same-orientation composition is

\[
 U_{\log p}U_{\log q}=U_{\log(pq)}.                 \tag{1.2}
\]

It is the analytic realization of
`Gamma_p Gamma_q=Gamma_(pq)`.  For distinct primes the reduced contact of
that composite vanishes because `Lambda(pq)=0`, equivalently because of
the coprime derived tensor (1.1).

The phase-121 detecting return is instead

\[
 P U_{\log p}(I-P)U_{-\log q}P
 =P U_{\log(p/q)}P                                  \tag{1.3}
\]

when both primes are inactive.  Its multiplicative label is `p/q`, not
`pq`.  It crosses the Real/opposite orientation before returning to the
physical window.  Neither `Lambda(pq)=0` nor (1.1) is a statement about
this rational label.

### Proposition 1.1 -- type separation

There is no formal implication from coprime contact vanishing to vanishing
of (1.3).

#### Proof

Take any nonzero `F in L2(I_T)` and consecutive sufficiently large primes
`p,q`.  Equation (1.1) and `Lambda(pq)=0` hold arithmetically, independently
of `F`.  But

\[
 \langle F,PU_{\log(p/q)}PF\rangle
 \longrightarrow\|F\|_2^2                         \tag{1.4}
\]

as `p/q to 1`, by strong continuity of translations.  Hence the hypotheses
hold while the proposed conclusion fails.  QED.

This countermodel does not refute an equality-state-only law.  It proves
that such a law needs information beyond coprime contact.

## 2. Why the ordinary Koszul repair deletes too much

The divisor Koszul differential has contractions `iota_p` satisfying

\[
 d_E\iota_p+\iota_pd_E=N_p.                         \tag{2.1}
\]

Thus every individual prime generator is null-homotopic.  With the degree
operator one obtains

\[
 M\delta Z=d_EH+Hd_E,
 \qquad H=\sum_p(\log p)\iota_p.                   \tag{2.2}
\]

So the same homotopy which cancels mixed quotient channels makes the
von-Mangoldt contact zero in cohomology.  This is the exact phase-104
Koszul stop-gate.  It cannot be used to prove (1.3) vanishes while retaining
row (c).

## 3. Consequence

The attractive chain

```text
coprime derived intersection is zero
 -> mixed inactive return is a boundary
 -> first-contact pairing kills it
```

breaks at the first arrow: it changes from same to opposite orientation.
Making the arrow true with the ordinary Koszul homotopy kills the desired
contact as well.

Therefore the inactive-return criterion remains valid as a terminal
descent, but rows (a)--(c) do not yet provide its normalized source
asymptotic.  A successful law must be nonadditive before scalar supertrace
and must retain the opposite-orientation `p/q` class.  No paper-42 change
follows.

