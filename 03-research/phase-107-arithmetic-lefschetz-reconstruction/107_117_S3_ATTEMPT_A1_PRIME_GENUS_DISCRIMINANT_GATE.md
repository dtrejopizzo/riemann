# 107.117 -- S3 attempt A1: prime/genus/discriminant packet gate

## 1. Purpose

As of Saturday, August 1, 2026, `107_104` through `107_109` establish
that the current finite-place source row of `107_04` only yields

\[
S_0(row)=\log p,
\]

and therefore cannot be faithful on the real local atlas.

The present tramo requires exactly one new result artifact that can
return `YES` or `NO` on real curve data, with the atlas fixed before
calculation. This note records the first independent construction
attempt:

\[
A1:\qquad R_{A1}(row)=(g,\ p,\ f_p,\ v_p(\Delta)).
\]

Here

1. \(g\) is the curve genus;
2. \(p\) is the probed finite prime;
3. \(f_p\) is the local conductor exponent;
4. \(v_p(\Delta)\) is the local discriminant valuation.

This is a genuine prime/Gamma/pole style packet: it uses only coarse
arithmetic source-side local data that are computable on real curves.

## 2. Fixed atlas

The verifier uses the following five curves, fixed before calculation.

1. `14a1` over \(\mathbf Q\), probed at \(p=2\);
2. `14a5` over \(\mathbf Q\), probed at \(p=7\);
3. `20a1` over \(\mathbf Q\), probed at \(p=2\);
4. `36a4` over \(\mathbf Q\), probed at \(p=2\);
5. the genus-2 curve
   \[
   C_{\mathrm{sup}}:\ y^2+y=x^5+x^2
   \]
   over \(\mathbf Q\), probed locally at its PARI-detected bad prime
   \(p=10037\).

This atlas satisfies the hard constraints:

1. it contains at least five real curves;
2. it contains a curve of genus \(2\);
3. that genus-2 curve has supersingular reduction at \(p=2\), certified
   independently by exact point counts up to \(n=8\), with equality
   \(a_8=64=2g\cdot 2^4\).

## 3. Target S3-state used in this gate

For this attempt, "reaches S3" means:
the source packet \(R_{A1}\) must distinguish the full visible local
target state on the pinned atlas.

The target state is taken to be:

1. for elliptic curves,
   \[
   T_E(row)=(\text{Kodaira symbol},\ c_p,\ \text{reduction label});
   \]
2. for the genus-2 curve,
   \[
   T_{C_{\mathrm{sup}}}(row)=
   (\text{PARI local stable-reduction class at }p=10037).
   \]

So the verifier asks a binary question:

\[
\text{if }R_{A1}(row_1)=R_{A1}(row_2),\text{ must }T(row_1)=T(row_2)?
\]

If yes on the whole fixed atlas, the verdict is `YES`.
If a real collision survives, the verdict is `NO`.

## 4. What the verifier checks

The verifier:

1. queries Sage for the four elliptic local rows;
2. queries PARI, through Sage, for the genus-2 local reduction data;
3. independently re-certifies that
   \(C_{\mathrm{sup}}/\mathbf F_2\) is the supersingular equality-case
   control used earlier in `107_28`;
4. forms the candidate source packet
   \(R_{A1}=(g,p,f_p,v_p(\Delta))\);
5. groups the five real rows by that packet;
6. returns `NO` if any packet class contains more than one distinct
   target state.

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: NO
```

The failing collision is real and explicit:

\[
20a1@2
\qquad\text{and}\qquad
36a4@2
\]

have the same coarse packet

\[
(g,p,f_p,v_p(\Delta))=(1,2,2,8)
\]

but different target states:

\[
(IV^\ast,3,\text{additive})
\neq
(IV^\ast,1,\text{additive}).
\]

Therefore attempt `A1` does **not** reach \(S_3\) on the fixed real
atlas.

## 6. Result status

This is a real failed construction attempt, not an audit:

1. the atlas was fixed before calculation;
2. the verifier runs on real curve data from Sage and PARI;
3. the script can genuinely return `NO`, and here it does;
4. this counts as one independent failed `A`-attempt toward the stopping
   rule if the same standard is maintained for later attempts.

No paper status is promoted here, and nothing in this note weakens the
Davenport--Heilbronn falsifier requirement.
