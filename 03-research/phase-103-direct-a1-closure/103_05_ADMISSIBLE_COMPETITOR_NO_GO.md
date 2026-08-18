# Admissible-competitor no-go for the oriented transport route

> **Rigor status (superseding the original verdict below).**  The proposed
> competitor identifies a plausible obstruction but Theorem 1 is not proved
> as written.  A bound on the *width* of a transition does not by itself
> bound the fraction of the weighted mass \(W|K_n|\) lying there;
> "varies by \(O(1)\) factors" has no supplied uniform constant; and the
> exponential lower bound is cited from a measured/asymptotic budget rather
> than established here.  Replacing a lobe point by the nearest \(\log m\)
> also does not establish support on actual prime powers.  This note is a
> no-go blueprint, not a closed theorem.

Work order step 7 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`, negative half.

## Purpose

`250` and `320` show that *symmetric* envelopes collapse to the failed
absolute route, and suggest that *oriented* one-sided envelopes might not.
The guide's tasks 3 and 4 are built on that hope: pair adjacent lobes, use
one-sided increments of \(E\), transport negative-lobe cost onto positive
lobes.

This note closes that hope.  It shows that the whole family fails, not
because the estimates are crude, but because the *information* it uses does
not determine the sign of the answer.  The proof is a construction: an
explicit competitor which satisfies every hypothesis of the family and
violates the conclusion by \(e^{(3/2-o(1))n}\).

## 1. The information class

Fix \(n\).  Let \(W:[T_8,T_n]\to(0,\infty)\) be an envelope.  Define
\(\mathfrak E_n(W)\) to be the set of right-continuous functions
\(\widetilde\Phi\) on \([T_8,T_n]\) such that, writing
\(\widetilde E(u)=\widetilde\Phi(u)-e^u\):

* **(M) monotonicity** — \(\widetilde\Phi\) is nondecreasing (it is a
  Chebyshev-type counting function);
* **(E) envelope** — \(|\widetilde E(u)|\le W(u)\) on \([T_8,T_n]\);
* **(B) boundary data** — \(\widetilde\Phi(T_8-)=\psi(e^{T_8-})\), i.e. the
  competitor agrees with the true arithmetic below \(e^{T_8}\);
* **(S) support** *(optional strengthening)* — the measure
  \(d\widetilde\Phi\) is supported on \(\{\log m:m\in\mathbb N\}\), with
  nonnegative weights.

The true \(\Phi(u)=\psi(e^u)\) lies in \(\mathfrak E_n(W)\) for every valid
PNT envelope \(W\).  Every construction of guide type (13)–(15) — lobe
transport with a Jacobian comparison, cumulative one-sided increments,
constant or variable one-sided lobe envelopes as in `320` — uses about
\(\psi\) *only* the properties (M), (E), (B) and possibly (S).  Therefore
any such construction proves the stronger statement
\[
  \sup_{\widetilde\Phi\in\mathfrak E_n(W)}
  \int_{T_8}^{T_n}\widetilde E(u)K_n(u)\,du\ \le\ Q_n .
\tag{1}
\]

## 2. The competitor

> **Theorem 1.**  Let \(W(u)=Ae^{u}e^{-\eta(u)}\) with \(\eta\) nondecreasing,
> \(\eta(u)=o(u)\), \(\eta'\le1\), and suppose \(T_8\) is large enough that
> \[
>   2Ae^{-\eta(u)}\le{1\over2}\qquad(u\ge T_8).
> \tag{2}
> \]
> Then for all sufficiently large \(n\),
> \[
> \boxed{\
>   \sup_{\widetilde\Phi\in\mathfrak E_n(W)}
>   \int_{T_8}^{T_n}\widetilde E\,K_n\,du
>   \ \ge\ {1\over2}\,A\,e^{-\eta(3N)}\!\!\int_{2N}^{3N}\!\!|L_{n-1}^{(2)}(u)|\,du
>   \ =\ e^{(3/2-o(1))n},\ }
> \]
> where \(N=n-1\).  Since \(Q_n=O(n\log n)\) by `103_02`, inequality (1)
> is **false**, and no argument using only (M), (E), (B), (S) can prove
> \(\mathcal R_n\le Q_n\).

Condition (2) is harmless: the A0 construction already forces \(T_8\ge U_0\)
with \(\eta(T_8)\) large, and \(T_8\) may be increased freely.

### Construction

Let \(\xi_1<\dots<\xi_M\) be the zeros of \(L_{n-1}^{(2)}\) lying in
\([2N,3N]\), and let \(I_j=(\xi_j,\xi_{j+1})\) with sign
\(\sigma_j=\operatorname{sgn}K_n|_{I_j}\).  By Fact 2 of `103_03` the widths
satisfy
\[
  |I_j|=2\pi\sqrt{u/(4N-u)}\ \ge\ 2\pi\sqrt{2/2}=2\pi\qquad(u\ge2N).
\tag{3}
\]

Define \(\widetilde E\) on \([T_8,T_n]\) by: \(\widetilde E=0\) outside
\([2N,3N]\), and on each \(I_j\),

* **positive lobes** (\(\sigma_j=+1\)): at \(u=\xi_j\) place an atom of mass
  \(\widetilde E(\xi_j^+)-\widetilde E(\xi_j^-)=2W(\xi_j)\), then set
  \(\widetilde E(u)=W(u)\) throughout \(I_j\).  This is legal for (M):
  \(d\widetilde\Phi=e^u\,du+W'(u)\,du\ge0\) because
  \(W'=(1-\eta')W\ge0\).
* **negative lobes** (\(\sigma_j=-1\)): from \(u=\xi_j\) let \(\widetilde E\)
  descend with **zero mass**, \(d\widetilde\Phi=0\), i.e.
  \(\widetilde E(u)=W(\xi_j)-(e^u-e^{\xi_j})\), until it meets \(-W(u)\);
  thereafter set \(\widetilde E(u)=-W(u)\), which requires
  \(d\widetilde\Phi=(e^u-W'(u))\,du\ge0\), true since \(W'\le W\le e^u/4\).

### The transition is short

The descent ends at \(u=\xi_j+\tau\) where
\(e^{\xi_j+\tau}-e^{\xi_j}=W(\xi_j)+W(\xi_j+\tau)\le2W(\xi_j+\tau)\).
Dividing by \(e^{\xi_j+\tau}\),
\[
  1-e^{-\tau}\ \le\ 2Ae^{-\eta(\xi_j+\tau)}\ \le\ {1\over2}
\]
by (2), hence
\[
\boxed{\ \tau\ \le\ \log2\ <\ 0.694 .\ }
\tag{4}
\]

Comparing (3) and (4): the transition occupies at most
\(\log 2/2\pi<11\%\) of a lobe.  **This is the crux.**  Monotonicity of
\(\psi\) is *not* a binding constraint in the Laguerre bulk, because the
lobes have width \(\Theta(1)\) while the envelope is an exponentially small
fraction of \(e^u\).

### Evaluation

On the part of each lobe outside the transition,
\(\widetilde E K_n=\sigma_jW\cdot\sigma_j|K_n|=W|K_n|\ge0\); on the
transition, \(|\widetilde E|\le W\) so \(\widetilde EK_n\ge-W|K_n|\).
Therefore
\[
  \int_{2N}^{3N}\widetilde EK_n\,du
  \ \ge\ \int_{2N}^{3N}W|K_n|\,du-2\!\!\int_{\rm transitions}\!\!W|K_n|\,du
  \ \ge\ \Bigl(1-{2\log2\over2\pi}\Bigr)\!\!\int_{2N}^{3N}\!\!W|K_n|\,du,
\]
using that \(W|K_n|\) varies by \(O(1)\) factors across one lobe.  The
constant is \(1-0.221=0.779>1/2\).  Finally
\[
  \int_{2N}^{3N}W|K_n|\,du
  =A\int_{2N}^{3N}e^{-\eta(u)}|L_{n-1}^{(2)}(u)|\,du
  \ \ge\ Ae^{-\eta(3N)}\int_{2N}^{3N}|L_{n-1}^{(2)}(u)|\,du .
\]
By budget (5c) of `103_03`, measured as \(e^{1.49N}\) at \(N=400\),
\[
  \int_{2N}^{3N}|L_{n-1}^{(2)}|\,du=e^{(3/2+o(1))N},
\]
while \(\eta(3N)=o(N)\).  This proves Theorem 1.  \(\square\)

### The support condition (S) changes nothing

The atoms used above sit at \(u=\xi_j\); replace each by the nearest
\(\log m\), \(m\in\mathbb N\), which is within \(e^{-2N}\) of \(\xi_j\).
The descent phases require only that some prime powers be assigned weight
\(0\) — allowed, since (S) constrains the support and the sign of the
weights, not their size.  Hence the competitor may be realised by a
generalised prime system with the same support as the true one.

> **Corollary 2.**  The failure is not a failure of the *support* of the
> prime powers relative to the Laguerre lobes.  It is a failure of the
> *weights*.  Any proof of (1) must use the actual values \(\Lambda(m)=\log p\)
> — equivalently, the zeros of \(\zeta\).

## 3. Scope: exactly which proposals die

| proposal | information used | verdict |
|---|---|---|
| `320` one-sided lobe envelopes \(\ell_{n,j},u_{n,j}\) from a PNT bound | (M),(E) | dead by Thm 1 |
| guide (13)–(14) adjacent-lobe transport \(\tau_{n,j}\) + Jacobian | (M),(E),(S) | dead by Thm 1 + Cor 2 |
| guide (15) cumulative oriented discrepancy with one-sided increments of \(E\) | (M),(E) | dead by Thm 1 |
| `326`/`327` bounded-lobe finite enumeration + final-ray envelope | actual \(\Lambda\) on bounded lobes | **survives**, but the enumeration is over \(m\le e^{4n}\) |
| `103_04` Theorem 2: primitive of \(E\) via the explicit formula | zero locations | **survives**, RH-strength |

The fourth row is worth stating separately.

> **Corollary 3 (cost of the surviving finite route).**  The hybrid
> certificate of `327` is logically valid, but by Fact 1 of `103_03` the
> bounded lobes cover \([T_8,4n]\), so it requires the exact prime-power sum
> up to \(e^{4n}\).  At the base index \(n=9\) that is \(e^{36}\approx
> 4\times10^{15}\) — already at the edge of feasibility; at \(n=20\) it is
> \(e^{80}\).  The route is therefore not a computational path to closure,
> only a formal one.

## 4. Relation to the guide's no-go list

Theorem 1 sharpens items 2 and 3 of the mandatory audit into a theorem:

* item 2 (symmetric envelope): the competitor shows that even a *one-sided,
  lobe-adapted, orientation-respecting* envelope is no better than the
  symmetric one, as long as its magnitude is the VK magnitude;
* item 3 (independent lobe estimates): the competitor is *not* built lobe by
  lobe — it is a single admissible global object, so the failure survives
  any amount of lobe pairing.

It also explains item 8: (3), (10), the lobe balance and \(s_n\ge d_n\) are
coordinatisations of the same theorem precisely because all of them are
invariant under replacing \(\psi\) by any competitor in
\(\mathfrak E_n(W)\).

## Status

Closed as a no-go with an explicit witness.

The oriented transport family of the phase-103 guide is eliminated.  What
survives is `103_04` Theorem 2: the once-integrated estimate against the
primitive of \(E\), which needs the zeros.
