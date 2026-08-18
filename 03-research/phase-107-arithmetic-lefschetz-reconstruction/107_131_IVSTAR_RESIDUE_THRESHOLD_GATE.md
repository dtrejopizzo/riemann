# 107.131 -- IV* residue threshold gate

## 1. Purpose

`107_129` and `107_130` leave the local search in an interesting state:

1. the mod-8 residue of the local minimal model is a real family-level
   arithmetic signal;
2. but mod 8 still does not determine \(c_p\) on the scanned
   \(IV^\ast\) additive family at \(p=2\).

The next exact question is:

\[
\text{how fine must the residue modulus }2^m\text{ be before the
family stops mixing }c_p?
\]

This note answers that question on the same real family.

## 2. Fixed real family

The verifier uses exactly the family already fixed in `107_129` and
`107_130`:

1. elliptic curves over \(\mathbf Q\);
2. local prime \(p=2\);
3. additive reduction;
4. Kodaira type \(IV^\ast\);
5. common coarse local packet
   \[
   (2,4,6,8,4,IV^\ast,2,0,1).
   \]

This family contains `count = 60` real curves in the scanned conductor
range \(11\le N\le 500\).

## 3. Threshold test

For each \(m=1,\dots,8\), the verifier groups the family by the residue
class of the local minimal-model coefficient tuple

\[
\mathbf a_{\min}(E,2)\pmod{2^m}
\]

and checks whether any residue class still contains curves with both
\(c_p=1\) and \(c_p=3\).

The exact output is:

```text
mod 2   groups 2   mixed_groups 2
mod 4   groups 3   mixed_groups 3
mod 8   groups 3   mixed_groups 3
mod 16  groups 6   mixed_groups 6
mod 32  groups 22  mixed_groups 0
mod 64  groups 47  mixed_groups 0
mod 128 groups 57  mixed_groups 0
mod 256 groups 59  mixed_groups 0
```

So the first tested modulus at which the scanned family stops mixing
\(c_p\) is:

\[
2^5 = 32.
\]

## 4. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: YES
```

where `YES` means:
there is a finite tested threshold in the scanned family, and the first
one found is modulus \(32\).

## 5. Interpretation

This result does **not** prove that mod \(32\) residue is the correct
Phase 107 source channel, nor that it determines \(c_p\) beyond the
scanned family.

It does prove a sharper local frontier:

1. residues mod \(8\) and mod \(16\) are still too coarse;
2. by mod \(32\), the scanned \(IV^\ast\) family no longer mixes
   \(c_p\);
3. the search for a finer local channel is no longer unstructured:
   the real data now exhibit a concrete residue-depth threshold.

So the correct reading is:

\[
\text{the current source grammar is too coarse,}
\]
\[
\text{mod-8 residue is not enough,}
\]
\[
\text{and mod-32 residue is the first tested depth that separates the
scanned real family.}
\]
