# D.217 — Regenerated directed certificate for the primitive V200 block at T=log(6)/2

## Verdict

The complete primitive compression to the first 200 normalized Legendre
modes at

\[
 T={1\over2}\log 6
\]

is strictly positive.  The statement is **CERTIFIED BY INTERVALS**.  It
includes the complete Gamma block, the scalar term, the two exact Tate
constraints, and every live contact \(2,3,4,5\).  It is a finite
compression theorem only; no conclusion about \(V_{200}^{\perp}\), its
coupling to \(V_{200}\), row D, or RH is drawn.

## 1. Reproducible generation

The directed contact enclosure was generated with

```bash
PYTHONPATH=/tmp/rowd-flint \
D100_N=200 D100_X=6 D100_PREC=2048 \
D100_SAVE=/tmp/d185_contacts6_arb.npz \
python3 114_d_100_log5_contacts_arb.py
```

using `python-flint==0.9.0`.  Its generator reported

\[
 \left|\sum_iw_i-2\right|\le 3.82\,10^{-162},
 \qquad
 \max_{ij}\mathrm{rad}\,C_{ij}le1.282\,10^{-161}
\]

before binary serialization.  The serialized balls are inflated to cover
conversion rounding.

The frame-selection centre was rebuilt with

```bash
PYTHONPATH=/tmp/rowd-flint D215_DPS=1100 \
python3 114_d_215_t6_finite_source_rebuild.py
```

The lower precision `D215_DPS=300` is inadmissible at degree 200: the
factorial endpoint representation loses too many cancellation digits and
its binary serialization overflows.  At 1100 digits the reconstructed
operator enclosure is finite and has maximum serialized radius

\[
 4.718447857758844\,10^{-16}.
\]

This enclosure is used only to select a frozen numerical frame.  It is not
used to decide the final sign.

The directed sign certificate was run with

```bash
PYTHONPATH=/tmp/rowd-flint D199_DPS=1100 \
D199_APPROX=/tmp/t6_complete_operator_legendre.npz \
D199_CONTACT=/tmp/d185_contacts6_arb.npz \
python3 114_d_199_t6_whitened_native_schur.py
```

## 2. Exact primitive frame

The centre chooses 198 columns.  D.199 freezes their binary tails and
solves the two Tate equations in Arb for the first two coordinates.  The
directed residual matrix contains zero entrywise.  Thus every certified
column lies in the exact common kernel of

\[
 F\longmapsto\int_{-T}^T e^{t/2}F(t)\,dt,
 \qquad
 F\longmapsto\int_{-T}^T e^{-t/2}F(t)\,dt.
\]

The diagnostic centre eigenvalues begin

\[
 1.51715947\,10^{-15},\quad
 2.26883258\,10^{-14},\quad
 1.80181212\,10^{-11},\quad
 3.07777447\,10^{-9}.
\]

These are not interval sign statements.  They only identify the two
delicate directions and the 196-dimensional safe block.

## 3. Directed Schur certificate

The complete Gamma projection was evaluated natively at 1100 digits.  Its
maximum enclosure radius was below

\[
 6.13\,10^{-95}.
\]

The serialized contact error on the safe block was propagated as an
entrywise enclosure and converted to a Loewner error budget

\[
 \delta_C\le 5.626066060033288\,10^{-14}.
\]

After directed whitening, the 196-dimensional safe block has Gershgorin
margin enclosing

\[
 0.99999999999999959015983928105>0.
\]

Contacts \(2,3,4,5\) on the two delicate columns were then recomputed
natively using a directed Gauss rule exact for every polynomial product
involved.  After eliminating the safe block, the delicate Schur matrix
was enclosed as

\[
 \begin{pmatrix}
  8.1526804798787876\,10^{-17} &
  6.8500639240917485\,10^{-17}\\
  6.8500639240917485\,10^{-17} &
  2.4790225091734754\,10^{-14}
 \end{pmatrix},
\]

with radii respectively below \(6.79\,10^{-117}\),
\(5.53\,10^{-114}\), and \(5.36\,10^{-112}\).  Its leading principal
entry is positive and its determinant encloses

\[
 2.0163755043954582\,10^{-30}>0
\]

with radius below \(5.00\,10^{-128}\).  Sylvester's criterion therefore
proves that the delicate Schur block is positive.  Restoring the positive
safe block proves strict positivity on the entire exact primitive
compression.

## 4. Artifact hashes for this run

```text
b6b15c2799c2b535144a6a23b13637a8affe1097492f988466656ee29d0207ea  114_d_100_log5_contacts_arb.py
4ff05e0cab9a6c98078fee12c7ef4312a5338aa3a2d713afcb7f34be6ebd7d51  114_d_199_t6_whitened_native_schur.py
f17c39e9f2fb594feda9076639871c43fe761743d75db52e0b8929a3b0821c18  114_d_215_t6_finite_source_rebuild.py
0bd01cdf2f9e0c2e1ed4b6758798467217c85d19f4526d7f5bb64c97026168f8  /tmp/d185_contacts6_arb.npz
2b7b7a82462ff414cdaca4707e2b92f0c565ed7d712c6bc8e9b2ce6dafa378ef  /tmp/t6_complete_operator_legendre.npz
3477d1f48edb25fea7bdc62ac91f3dfb1632667b5debd5ffaf9e8991d8417301  /tmp/t6_direct_primitive_eigs.npz
```

The `/tmp` artifacts are reproducible caches, not archival proof objects;
the commands and directed generators above are authoritative.

## 5. Scope

* Exact primitive Tate compression in \(V_{200}\): **PROVED**.
* Complete Gamma plus contacts \(2,3,4,5\) in that compression:
  **CERTIFIED BY INTERVALS**.
* Strict positivity of the primitive \(V_{200}\) compression:
  **CERTIFIED BY INTERVALS**.
* Coupling to \(V_{200}^{\perp}\): **OPEN**.
* Positivity of the full Hilbert-space endpoint: **OPEN**.
* Uniform birth theorem and row D: **OPEN**.

