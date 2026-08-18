# A1 gate triage and priority

## Purpose

Phase 102 now contains many exact normal forms for A1.  This document
separates them into:

1. equivalent rewritings of A1;
2. sufficient but stronger theorems;
3. genuinely new positivity mechanisms.

The point is to prevent a normal form from being mistaken for a proof.

## Equivalent compact forms

The following are exact forms of the same compact signed theorem:

- direct A1:
  \[
    C_n(T_n)\ge0;
  \]
- collapsed Laguerre kernel:
  \[
    C_n(T)
    =
    -n-\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
    +{3\over4}\lambda_n^{\rm arch};
  \]
- lobe compensation over the zeros of \(L_{n-1}^{(2)}\);
- dual lobe balance with \(B_a(u)=\int_a^u E(e^v)\,dv\);
- raised balance hierarchy \(B_r\) against \(L_{n-1}^{(2+r)}\);
- finite Laplace jets at \(s=1\);
- finite arithmetic certificates over prime powers \(m\le e^{T_n}\);
- moving-diagonal coefficient positivity
  \[
    [z^n]\mathcal C_{T_n}(z)\ge0;
  \]
- fixed-cutoff recurrence plus moving-cutoff transfer.

Each item is valuable because it changes the shape of the missing theorem.
None of them proves A1 without an additional one-sided or positivity input.

## Sufficient stronger routes

The following theorems would imply A1 but are stronger than A1 as stated:

1. strong margin:
   \[
     \lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8);
   \]
2. a genuinely one-sided tail theorem for \(R_n(T_n)\);
3. a completed positive boundary measure for \(\xi'/\xi\);
4. a Hermite--Biehler/de Branges construction;
5. infinite Pick/Stieltjes positivity of the completed Li transform;
6. a non-tautological positive bordered current;
7. a positive square-root/autocorrelation Weil factorization;
8. heat-flow threshold at or below the original time;
9. cofinal Jensen/Laguerre--Pólya convergence.

These routes carry RH-strength.  They are not forbidden; they are precisely
the kind of theorem needed to close Omega7.

## Eliminated shortcuts

The following patterns do not close A1:

1. A0 alone.
2. A fixed cutoff \(T\) without a universal cutoff or signed transfer to
   \(T_n\).
3. A finite positive matrix model without cofinal identification.
4. A linear explicit formula without a positive square root.
5. Euler-product positivity in \(\Re s>1\) without positivity-preserving
   continuation to the Li boundary.
6. A PNT absolute or relative error bound applied to the compact core.
7. A formal cutoff monotonicity assertion.
8. A recurrence in \(n\) without a signed bound for its forcing.

Each eliminated shortcut may still inspire a valid theorem, but only after
the missing signed or positive structure is supplied.

## Current best reduced targets

After the corrections through `157`, the most concrete remaining targets are:

### Target A: direct signed compact inequality

Prove
\[
  \int_0^{T_n}E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \le {3\over4}\lambda_n^{\rm arch}-n
  \qquad(n\ge8).
\tag{A}
\]

This is the shortest form.  It must be proved by signed compensation, not by
absolute estimates.

### Target B: accumulated lobe balance

Prove the dual lobe or raised-balance inequalities from `145` and `146`,
using the explicit balances \(B_r\).  This is the most local arithmetic
target.

### Target C: moving-diagonal coefficient theorem

Prove
\[
  [z^n]\mathcal C_{T_n}(z)\ge0\qquad(n\ge8)
\tag{C}
\]
directly, or prove fixed-cutoff positivity plus the signed transfer theorem
of `153`/`154`.

### Target D: global positive boundary theorem

Construct a positive Euler--Gamma boundary measure, Hermite--Biehler
function, Pick/Stieltjes representation, or Weil square root.  This is the
cleanest conceptual target and the one that would close RH most directly.

### Target E: induction with forcing

Use the recurrence of `156`, with the corrected forcing of `157`, and prove
the full signed cumulative forcing bound plus moving-cutoff transfer.

## Priority decision

The next work should prefer one of two directions:

1. **local arithmetic direction:** attack Target B or E, because they are
   expressed in finite prime-power sums and Laguerre kernels;
2. **global positivity direction:** attack Target D, because it would close
   all Li tests at once.

The fixed-cutoff and jet forms should be used as tools inside those
directions, not treated as independent closures.

## Status

Closed as a triage document.  A1 remains open.

The phase now has a clear separation between exact rewritings and genuine
proof obligations.  A closure of Omega7 must prove one of the targets above,
not merely add another equivalent normal form.
