# 107.119 -- S3 attempt A3: add split-flag gate

## 1. Purpose

`107_117` and `107_118` record two independent failed attempts to reach
visible \(S_3\) on real curve data:

1. `A1` used
   \[
   (g,p,f_p,v_p(\Delta));
   \]
2. `A2` used
   \[
   (g,p,f_p,v_p(\Delta),c_p).
   \]

The surviving obstruction after `A2` is exactly the split/nonsplit
multiplicative ambiguity.

This note records the third candidate refinement:

\[
R_{A3}(row)=
(g,p,f_p,v_p(\Delta),c_p,\sigma_p),
\]

where

\[
\sigma_p=
\begin{cases}
 1,& \text{split multiplicative},\\
 -1,& \text{nonsplit multiplicative},\\
 0,& \text{otherwise}.
\end{cases}
\]

This is the minimal visible upgrade that directly attacks the remaining
`A2` collision.

## 2. Fixed atlas

The atlas is fixed before calculation and consists of six real curves:

1. `14a1` over \(\mathbf Q\), probed at \(p=2\);
2. `14a5` over \(\mathbf Q\), probed at \(p=7\);
3. `21a1` over \(\mathbf Q\), probed at \(p=7\);
4. `20a1` over \(\mathbf Q\), probed at \(p=2\);
5. `36a4` over \(\mathbf Q\), probed at \(p=2\);
6. the genus-2 curve
   \[
   C_{\mathrm{sup}}:\ y^2+y=x^5+x^2
   \]
   over \(\mathbf Q\), probed locally at its PARI-detected bad prime
   \(p=10037\).

This atlas contains:

1. at least five real curves;
2. a curve of genus \(2\);
3. a supersingular control, because \(C_{\mathrm{sup}}/\mathbf F_2\)
   satisfies \(a_8=64\) and \(\det G_8^0=0\).

## 3. Target state and binary criterion

The target state is again taken to be:

1. for elliptic curves,
   \[
   T_E(row)=(\text{Kodaira symbol},c_p,\text{reduction label});
   \]
2. for the genus-2 curve,
   \[
   T_{C_{\mathrm{sup}}}(row)=
   (\text{PARI local stable-reduction class at }p=10037).
   \]

The verifier returns `YES` iff equal `A3` packets always imply equal
target states on the fixed atlas.

## 4. Why this is a genuine third attempt

This attempt is independent of the previous two:

1. `A1` failed because it did not see \(c_p\);
2. `A2` fixed that but still failed on the split/nonsplit pair
   `14a5@7` versus `21a1@7`;
3. `A3` adds exactly the missing split-flag \(\sigma_p\).

So `A3` is not a replay of the earlier failures; it changes the source
packet in the only place where `A2` still collided on real data.

## 5. Exact binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: YES
```

On the fixed atlas, every `A3` packet class has exactly one target
state. In particular:

1. `20a1@2` and `36a4@2` are already separated by \(c_p\);
2. `14a5@7` and `21a1@7` are now separated by
   \(\sigma_7=1\) versus \(\sigma_7=-1\).

So the first real source-side packet in this tramo that reaches the
visible \(S_3\) discrimination threshold on the fixed atlas is

\[
(g,p,f_p,v_p(\Delta),c_p,\sigma_p).
\]

## 6. Scope and limitation

This result proves only the atlas-level statement:
the packet \(R_{A3}\) is sufficient to separate all currently pinned
real local target states.

It does **not** yet prove:

1. that the existing source route of `107_04` actually derives
   \(\sigma_p\);
2. that \(R_{A3}\) is globally sufficient beyond the fixed atlas;
3. any full realization theorem for row (c) on arithmetic surfaces over
   \(\mathrm{Spec}\,\mathbf Z\).

So the correct reading is:

\[
\text{visible S3 reached on the fixed real atlas by }R_{A3},
\]
\[
\text{source derivability of that packet inside Phase 107 still open}.
\]
