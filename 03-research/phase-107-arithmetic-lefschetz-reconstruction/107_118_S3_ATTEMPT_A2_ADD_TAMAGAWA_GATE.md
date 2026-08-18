# 107.118 -- S3 attempt A2: add-Tamagawa gate

## 1. Purpose

`107_117` records the first independent construction attempt

\[
R_{A1}(row)=(g,p,f_p,v_p(\Delta)),
\]

and exact-checks that it fails on real curve data.

This note records the second independent attempt:

\[
R_{A2}(row)=(g,p,f_p,v_p(\Delta),c_p).
\]

So `A2` upgrades `A1` by adding the Tamagawa number \(c_p\), while
still remaining a genuine computable prime/Gamma/pole style source
packet on real curves.

The binary question is the same as in `107_117`:
does this candidate packet reach visible \(S_3\) on a fixed atlas of
real curves, or does it still collapse distinct target states?

## 2. Fixed atlas

The atlas is fixed before calculation and contains five real curves:

1. `14a5` over \(\mathbf Q\), probed at \(p=7\);
2. `21a1` over \(\mathbf Q\), probed at \(p=7\);
3. `20a1` over \(\mathbf Q\), probed at \(p=2\);
4. `36a4` over \(\mathbf Q\), probed at \(p=2\);
5. the genus-2 curve
   \[
   C_{\mathrm{sup}}:\ y^2+y=x^5+x^2
   \]
   over \(\mathbf Q\), probed locally at the PARI-detected bad prime
   \(p=10037\).

This still satisfies the hard constraints:

1. at least five real curves;
2. at least one curve of genus \(2\);
3. the genus-2 control remains supersingular over \(\mathbf F_2\), with
   exact equality \(a_8=64\) and \(\det G_8^0=0\).

## 3. Target state

The verifier uses the same visible target state convention as before.

1. For elliptic curves:
   \[
   T_E(row)=(\text{Kodaira symbol},c_p,\text{reduction label}).
   \]
2. For the genus-2 curve:
   \[
   T_{C_{\mathrm{sup}}}(row)=
   (\text{PARI local stable-reduction class at }p=10037).
   \]

The candidate `A2` reaches visible \(S_3\) on this atlas iff equal
source packets always imply equal target states.

## 4. Why this is independent of `A1`

This attempt is not a replay of the `A1` failure.

In `A1`, the obstruction came from the pair

\[
20a1@2,\qquad 36a4@2,
\]

which share the same coarse packet but have different Tamagawa numbers.

`A2` adds \(c_p\), so that pair is now separated:

\[
(1,2,2,8,3)\neq(1,2,2,8,1).
\]

The new test is therefore sharper:
it asks whether adding \(c_p\) is enough, or whether the remaining
split/nonsplit sector still forces a `NO`.

## 5. Exact binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: NO
```

The explicit failing collision is:

\[
14a5@7
\qquad\text{and}\qquad
21a1@7.
\]

These two real local rows have the same `A2` packet

\[
(g,p,f_p,v_p(\Delta),c_p)=(1,7,1,2,2),
\]

but different target states:

\[
(I_2,2,\text{split})
\neq
(I_2,2,\text{nonsplit}).
\]

So adding \(c_p\) does **not** yet reach visible \(S_3\) on the fixed
atlas.

## 6. Result status

This is a real second failed construction attempt:

1. the atlas is fixed before calculation;
2. the verifier runs on real curve data from Sage and PARI;
3. the script can return `YES` or `NO`, and here it returns `NO`;
4. the failure is independent of `A1`, because the `A1` collision is
   removed and a different split/nonsplit obstruction remains.

No paper status is promoted here. If the same standard is maintained,
this counts as the second independent failed `A`-attempt under the
stopping rule.
