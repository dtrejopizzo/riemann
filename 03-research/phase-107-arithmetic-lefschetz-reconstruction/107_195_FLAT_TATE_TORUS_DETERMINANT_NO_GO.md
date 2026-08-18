# 107.195 -- The standard flat Tate-torus determinant adds unwanted modes

## 1. Minimal compact complexification

For a real spectral parameter \(s>1\) and prime \(p\), put

\[
 q=p^{-s},\qquad
 \tau={is\log p\over2\pi},
 \qquad e^{2\pi i\tau}=q.
\]

The standard compact complexification of the two periods is the flat
elliptic curve

\[
 E_{p,s}=\mathbb C/(\mathbb Z+\tau\mathbb Z).
\]

This is an actual compact Kahler manifold and therefore repairs the
dimension-parity obstruction of `107_194`.

## 2. Its determinant

Kronecker's limit formula gives, up to the universal normalization fixed
by the area convention,

\[
 \det{}'\Delta_{E_{p,s}}
 =C\,\Im(\tau)|\eta(\tau)|^4.
 \tag{2.1}
\]

For the present imaginary \(\tau\),

\[
 |\eta(\tau)|^4
 =q^{1/6}\prod_{n\ge1}(1-q^n)^4.
 \tag{2.2}
\]

The prime-orbit complex of `107_185`, by contrast, has holomorphic
determinant

\[
 d_p(s)=1-q,
 \qquad |d_p(s)|^2=(1-q)^2.
 \tag{2.3}
\]

## 3. No-go theorem

**Theorem.**  The standard scalar-Laplacian/Quillen determinant on the
flat compactification \(E_{p,s}\) is not the prime-orbit determinant
\(|1-p^{-s}|^2\) up to a universal constant independent of \(p,s\).

**Proof.**  Dividing (2.1)--(2.2) by (2.3) gives

\[
 {\det{}'\Delta_{E_{p,s}}\over|1-q|^2}
 =C\,{s\log p\over2\pi}\,
 q^{1/6}(1-q)^2\prod_{n\ge2}(1-q^n)^4.
 \tag{3.1}
\]

The right side is nonconstant in \(q\); it tends to zero as
\(q\to0\), while it is positive for every \(0<q<1\).  Hence no
universal constant can identify the two determinants. \(\square\)

The discrepancy is structural: compactifying the second real direction
introduces the full two-dimensional Fourier tower.  Selecting only the
\(n=1\) factor would be a nonlocal spectral projection, not the
determinant of the standard compact torus.

## 4. Exact scope

This closes only the naive bridge

\[
 C_p\longrightarrow E_{p,s}
 \longrightarrow\text{standard flat scalar determinant}.
\]

It does not exclude:

1. a virtual complex whose extra Fourier modes cancel;
2. a relative determinant dividing by a reference torus;
3. a noncompact cylinder with boundary conditions;
4. a transverse superconnection or secondary current.

Any of those replacements must derive the cancellation rather than
divide by the eta tail after inspecting (3.1).

## 5. Falsifier

The verifier fixes the real prime atlas \(2,3,5,7,11\) and spectral
parameters \(3/2,2,3\) before evaluation.  It computes the eta product
with a rigorous geometric tail bound, confirms the presence of the
\(n\ge2\) modes, and rejects constancy of (3.1).  A one-mode mutation
is required to match (2.3), demonstrating exactly which illicit
truncation would hide the discrepancy.
