# 107.123 -- Additive valuative/Euler to c_p no-go

## 1. Purpose

The current local target used throughout the recent S3 gates is

\[
T_E(row)=
(\text{Kodaira symbol},c_p,\text{reduction label}).
\]

So under the *current* Phase 107 target design, \(c_p\) is part of the
state that a faithful source package must recover.

This note isolates the decisive additive obstruction pointed out by the
real pair

\[
20a1@2,\qquad 36a4@2.
\]

It shows that any local package built only from standard
valuative/Euler-type invariants is structurally blind to the distinction
between these two rows, while the target still distinguishes them via
\(c_p\).

## 2. Real pair and computed invariants

The verifier computes, directly from Sage, the following local data for
the two genuine elliptic curves over \(\mathbf Q\):

\[
\begin{array}{c|ccccccccc}
\text{curve} & p & v(c_4) & v(c_6) & v(\Delta) & v(j) & \text{Kodaira} & f_p & a_p & c_p \\
\hline
20a1 & 2 & 4 & 6 & 8 & 4 & IV^\ast & 2 & 0 & 3 \\
36a4 & 2 & 4 & 6 & 8 & 4 & IV^\ast & 2 & 0 & 1
\end{array}
\]

Both rows are additive at \(p=2\), so the local Euler factor is the
same trivial additive factor \(1\) on both sides.

Thus they agree on every standard valuative/Euler entry in the table
except \(c_p\).

## 3. Packet tested here

The verifier defines the local valuative/Euler packet

\[
V_{\mathrm{add}}(row)=
\bigl(
 p,\ v(c_4),\ v(c_6),\ v(\Delta),\ v(j),\
 \text{Kodaira},\ f_p,\ a_p,\ L_p^{\mathrm{loc}}
\bigr),
\]

where for these additive rows

\[
L_p^{\mathrm{loc}}=1.
\]

This is exactly the kind of package one would build from standard
valuative data plus Euler-style local coefficients.

The target retained by the current Phase 107 gates is

\[
T_E(row)=
(\text{Kodaira symbol},c_p,\text{reduction label}).
\]

## 4. Exact obstruction

Running the verifier shows:

1. \(V_{\mathrm{add}}(20a1@2)=V_{\mathrm{add}}(36a4@2)\);
2. \(T_E(20a1@2)\neq T_E(36a4@2)\) because \(c_p=3\neq1\).

So no local comparison map factoring through \(V_{\mathrm{add}}\) can be
faithful on the current target.

Equivalently:

\[
\text{same valuative/Euler packet}
\centernot\Longrightarrow
\text{same target state}
\]

once \(c_p\) is required.

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: NO
```

meaning:
the current target state including \(c_p\) cannot be recovered from this
standard additive valuative/Euler packet even on the real two-curve
test.

## 6. Consequence

This is the first exact local no-go in Phase 107 that rules out a whole
family of future attempts rather than only one previously written
packet.

Under the current target design that includes \(c_p\), it proves:

1. purely valuative refinements of `A1` are dead on this pair;
2. additive Euler-style data of the form \(a_p\) and local factor \(1\)
   do not repair that failure;
3. any future faithful source package must contain genuinely
   non-valuative, Galois-sensitive information if it aims to recover
   \(c_p\).

What it does **not** yet prove is:

1. that every possible prime/Gamma/pole refinement is impossible;
2. that row (c) is closed under every imaginable target redesign;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
\text{if the target includes }c_p,
\]
\[
\text{then additive valuative/Euler packets are structurally insufficient on real data.}
\]
