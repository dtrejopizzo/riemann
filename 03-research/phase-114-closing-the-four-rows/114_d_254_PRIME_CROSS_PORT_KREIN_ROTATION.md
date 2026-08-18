# D.254 — Exact cross-port Krein rotation for the complete prime score

## Verdict

The first-order identity of D.245 can be upgraded to an exact two-port
Krein feature factorization without inverting either tangent filter.  The
complete prime-power score is the cross Gram of the even Euler tangent and
the dual central Euler state.  A fixed Hadamard rotation converts that
cross Gram into a difference of two positive Grams.

This supplies the explicit prime-side port wiring missing from the naive
square-tangent attempt of D.250.  It is an identity of complete Fourier
multipliers and includes every \(p^k\).  It does not prove that the
support-compressed load is contractive; the global degree/contact, Tate and
Gamma elimination remains the sharp gate.

## 1. Tangent and dual central ports

Fix a prime, put

\[
 r=p^{-1/2},\qquad L=\log p,\qquad U=e^{i\theta},
 \qquad h=I-rU.
\]

On \(L^2(\mathbb T)\), define the bounded multiplication operators

\[
 B=h^{-1},
 \qquad
 D={Lr\over2}h^{-1}(U+U^*-2r).                     \tag{1.1}
\]

Here \(D\) is the even Euler tangent of D.245 and \(B\) is the dual
central state.  Since all displayed operators commute as multipliers,

\[
 \begin{aligned}
 D^*B+B^*D
 &= {Lr(U+U^*-2r)\over|1-rU|^2}\\
 &=L(P_r-I),                                       \tag{1.2}
 \end{aligned}
\]

where

\[
 P_r={1-r^2\over|1-rU|^2}.
\]

The last equality follows from

\[
 P_r-I={r(U+U^*-2r)\over|1-rU|^2}.                 \tag{1.3}
\]

Thus the score is a cross effect, not the difference of the squared even
and odd tangent norms.

## 2. Hadamard Krein rotation

Put

\[
 W_+^{\rm cr}={B+D\over\sqrt2},\qquad
 W_-^{\rm cr}={B-D\over\sqrt2}.                    \tag{2.1}
\]

Then

\[
 \boxed{
 (W_+^{\rm cr})^*W_+^{\rm cr}
 -(W_-^{\rm cr})^*W_-^{\rm cr}
 =L(P_r-I).
 }                                                   \tag{2.2}
\]

Indeed the two diagonal terms \(B^*B\) and \(D^*D\) cancel and the cross
terms add.  Equivalently,

\[
 \begin{pmatrix}W_+^{\rm cr}\\W_-^{\rm cr}\end{pmatrix}
 ={1\over\sqrt2}
 \begin{pmatrix}I&I\\I&-I\end{pmatrix}
 \begin{pmatrix}B\\D\end{pmatrix}.               \tag{2.3}
\]

The matrix in (2.3) is unitary.  No inverse of \(D\), \(W_{p,+}\) or
\(W_{p,-}\) occurs, so the boundary zeros of D.250 cause no type error.

## 3. All prime powers

The Poisson expansion is

\[
 P_r-I=\sum_{k\ge1}r^k(U^k+U^{*k}).                \tag{3.1}
\]

Multiplying by \(L\) gives

\[
 L(P_r-I)
 =\sum_{k\ge1}{\log p\over p^{k/2}}
   (U^k+U^{*k}).                                   \tag{3.2}
\]

Hence (2.2) contains the exact row-B/C coefficient
\(\Lambda(p^k)/\sqrt{p^k}\) at every power \(p^k\), with no truncation.
On a support window, compression simply deletes translations whose
supports do not meet; it does not change the identity for the active
powers.

## 4. Connection to the four-port conservation law

In D.247 the even tangent is an output of the source-defined conservative
map

\[
 (\text{odd tangent},\text{degree})
 \longrightarrow
 (\text{even tangent},\text{contact}).             \tag{4.1}
\]

Equation (2.3) now gives an explicit second wiring step:

\[
 (\text{dual central state},\text{even tangent})
 \longrightarrow
 (W_+^{\rm cr},W_-^{\rm cr}).                      \tag{4.2}
\]

Both arrows are source-defined and conservative on their stated ports.
The unresolved operation is the identification/feedback of the dual
central state in (4.2) with the global degree/contact and Gamma/Tate ports
in (4.1).  Closing it prime by prime is forbidden by D.252.  It must be
done after the global degree sum and before primitive shorting.

## 5. Comparison status

Equation (2.2) proves equality of the **signed prime multiplier** with the
prime part of D.137.  It does not assert separate unitary equivalences

\[
 W_+^{\rm cr}\simeq W_{p,+},\qquad
 W_-^{\rm cr}\simeq W_{p,-}.
\]

Such separate identifications are unnecessary for the form but would be
too strong: spectral factorizations of an indefinite multiplier are not
unique, and D.250 rules out the proposed bounded-inverse transport through
the tangent blocks.

The next finite calculation is to compose (4.1) and (4.2) as a
Pontryagin/Redheffer relation while keeping the degree and contact ports
external.  Its state elimination must be compared with the prime-only
part of the D.170 boundary load.

## 6. Classification

* Cross identity (1.2): **PROVED OPERATOR IDENTITY**.
* Hadamard Krein factorization (2.2): **PROVED**.
* Inclusion of all powers (3.2): **PROVED**.
* Avoidance of the D.250 inverse obstruction: **PROVED**.
* Signed prime multiplier comparison with D.137: **PROVED**.
* Global degree/contact feedback and old/born transfer comparison:
  **OPEN**.
* Gamma/Tate completion and row D: **OPEN**.

