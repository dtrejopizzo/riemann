# 115.01 — Row (a)'s Green term is a rank cut, and row (a) is row (d)'s equality case

Verifier: `115_01_green_rank_cut_verify.py` (exact finite linear algebra).

## Verdict

Both row-(a) forms are purely **off-diagonal** in the two rulings, so each is
carried by a single \((\text{primes}\times\text{primes})\) matrix \(M\):

\[
 \text{form}(x,y)=x_1^{\!\top}My_2+x_2^{\!\top}M^{\!\top}y_1
 \quad\Longleftrightarrow\quad
 \begin{pmatrix}0&M\\M^{\!\top}&0\end{pmatrix},
 \qquad \ell_p:=\log p .
\]

With that,

\[
 \boxed{
 M(C_\Lambda)=\mathrm{diag}(\ell),
 \qquad
 M(B_{\rm int})=\ell\ell^{\!\top},
 \qquad
 M(G)=\ell\ell^{\!\top}-\mathrm{diag}(\ell).
 }
\]

The inertia of \(\begin{pmatrix}0&M\\M^{\!\top}&0\end{pmatrix}\) is
\((\mathrm{rank}\,M,\mathrm{rank}\,M,\cdot)\).  Therefore

| | \(\mathrm{rank}\,M\) | inertia |
|---|---|---|
| \(C_\Lambda\) (local contact) | \(r\) | \((r,r,0)\) |
| \(B_{\rm int}\) (row-(a) total) | \(1\) | \((1,1,2r-2)\) |

> **The Green term of `eq:greenline` is exactly a rank cut \(r\to1\).**

And it is a rank cut of precisely the advertised kind: \(\ell\ell^{\!\top}\)
**couples every pair of distinct primes**, while \(-\mathrm{diag}(\ell)\)
**subtracts nothing but the local contact**.  That is, verbatim, what
`main.tex` says is missing from row (d) after `eq:finitealternative`:
*"a global Green term which couples distinct primes while preserving their
local contact."*  Row (a) has it in closed form.

## 1. Two different subspaces — do not confuse them

Row (a)'s ruling model has **two** distinguished subspaces, and they are not
the same.  Measured (`115_01` verifier, \(r=7\)):

| subspace | codim | \(B_{\rm int}\) there |
|---|---|---|
| \(H^\perp\), \(H\) the polarization | 1 | \((0,1,13)\) — **no positive directions** |
| both degrees zero, \(\ell^{\!\top}x_1=\ell^{\!\top}x_2=0\) | 2 | \(\equiv0\) |

The first line is the Hodge conclusion itself: on the orthogonal complement of
the polarization, the form has zero positive index.  Row (a) satisfies it, and
it does so **because** of the rank cut — \(\mathrm{rank}\,M=1\) leaves one
positive direction in the whole space, and that one direction is \(H\).

The second line is the analogue of \(\mathcal T^0\), which is also cut out by
two degree conditions (`eq:twoprimitive`: \(\widehat f(0)=\widehat f(1)=0\)).
There row (a) gives \(=0\), and on the radical \(G=-C_\Lambda\) exactly.

> Row (d) asks for \(B_{\rm nuc}\le0\) on the **codimension-two** space.
> Row (a) delivers \(=0\) there.
> The mixed classes must deform that identity so the space opens **downwards**.

Note the freedom this exposes: row (d) is a codimension-two statement, strictly
weaker than the full Hodge index on \(H^\perp\), which
`thm:mixedsectionforcing` would deliver.

## 2. Division of labour: where each sign has to come from

A cross form \(\begin{pmatrix}0&M\\M^{\!\top}&0\end{pmatrix}\) has inertia
\((\mathrm{rank}\,M,\mathrm{rank}\,M,\cdot)\) — always **neutral**,
equal positive and negative counts.  That is not an obstruction; after the cut
\(\mathrm{rank}\,M=1\) it gives exactly \((1,1,\cdot)\), one polarization
plus one negative.  But it does force a conclusion:

> The infinitely many negative directions row (d) needs **cannot come from the
> contact**.  A cross form can only ever produce them in equal number with
> positives.

There is exactly one other source in the paper, and it is diagonal rather than
cross: the archimedean term.  `eq:archmultiplier` gives
\(G_\infty(f,f)=\frac1{2\pi}\int m_\infty(\tau)|\widehat f|^2d\tau\), a Fourier
multiplier with \(m_\infty(\tau)\to-\infty\).  Its single zero crossing sits at
\(\tau^*=6.28984\approx2\pi\) (computed; \(m_\infty(0)=5.37218\)).  So
\(G_\infty\) has **finitely many** positive directions — the band
\(|\tau|<2\pi\) — and **infinitely many** negative ones, the tail.

That assigns each piece a job:

```text
ruling block      cross, rank 2   ->  supplies the ONE positive: the polarization H
contact block     cross per prime ->  hyperbolic pairs, neutral (r,r)
Green cut         ell ell^T - diag(ell)  ->  cuts rank r -> 1, so only H stays positive
archimedean G_inf diagonal multiplier ->  the infinitely many negatives (the tail)
```

The finite budget to be beaten is therefore exactly the band \(|\tau|<2\pi\).
This is consistent with, and explains the shape of, the indefiniteness proved
in D.262 §3 and in `main.tex`: it is one interior band, not a diffuse defect.

## 3. Both prime-power contact shapes still need the same cut

Extend the contact from primes to prime powers, \(M_{mn}\) supported where
\(m,n\) are powers of the same \(p\).  \(M\) is block diagonal with one
all-ones block per prime, so \(\mathrm{rank}\,M=r\) regardless of \(|S|\).
Measured:

| \(|S|\) | \(r\) | SELF \(K_S(e_m,e_n)=\Lambda(mn)\) | CROSS \(\begin{pmatrix}0&M\\M&0\end{pmatrix}\) |
|---|---|---|---|
| 16 | 10 | \((10,0,6)\) | \((10,10,12)\) |
| 25 | 17 | \((17,0,8)\) | \((17,17,16)\) |
| 40 | 30 | \((30,0,10)\) | \((30,30,20)\) |

Both shapes need the Green term to cut \(r\to1\).  The difference is what the
leftovers are:

* **SELF** (row (d)'s `eq:finitecandidate`) leaves \(r\) **positive**
  directions and nothing negative — the Green term must fight a
  positive-semidefinite form.  This is `thm:finitecontactobstruction`.
* **CROSS** (row (a)'s shape) pairs them into hyperbolic planes — the exact
  situation row (a) demonstrably cancels, since \(\ell\ell^{\!\top}\) is the
  rank-one cut of \(\mathrm{diag}(\ell)\).

So the shape choice is not cosmetic.  It decides whether the Green term is
being asked to do something row (a) has already done, or something it has not.

## 4. Where the extension will actually break

Row (a)'s cut works because \(M(B_{\rm int})=\ell\ell^{\!\top}\) is the outer
square of the **degree vector**, \(d_i(x)=\ell^{\!\top}x_i\).  The mixed-class
analogue would be \(M=vv^{\!\top}\) with \(v_n=\Lambda(n)/\sqrt n\).

**That vector is not summable**: \(\sum_{n\le N}\Lambda(n)/\sqrt n=2\sqrt N+
\dots\).  The naive degree functional on mixed classes diverges.

This is not an obstruction — it is the reason the rest of the programme looks
the way it does.  The divergence is removed by subtracting the continuous
synthesis, i.e. by the two Tate conditions, i.e. by passing to
\(\mathcal T^0\); and the resulting centred object is exactly D.260's

\[
 dA=d\Psi-dx,\qquad A(x)=\Psi(x)-x+1 .
\]

So three things that were separate in the ledger are one thing:

```text
row (a)'s degree vector  ell        -- the rank-one cut
the two Tate conditions / rulings   -- what makes its extension finite
D.260's centred measure dPsi - dx   -- the extended vector itself
```

**Working hypothesis for this phase.**  \(d\Psi-dx\) is the centred degree
vector of the mixed classes, and the row-(d) Green term is its outer square
minus the local contact — the exact analogue of
\(\ell\ell^{\!\top}-\mathrm{diag}(\ell)\).

That is a statement about an object, not an estimate, so it is not excluded by
`main.tex` §1 and it does not use the sign.  It is also falsifiable: the
outer-square must reproduce `thm:forcedgreen`'s \(G_\infty\), which is already
pinned exactly by row (c).

## 5. Classification

* Block form and \(M(G)=\ell\ell^{\!\top}-\mathrm{diag}(\ell)\):
  **PROVED** (exact, verified).
* Inertia \(=(\mathrm{rank}\,M,\mathrm{rank}\,M,\cdot)\) and the
  \(r\to1\) cut: **PROVED**.
* \(G=-C_\Lambda\) on the radical; \(B_{\rm int}\equiv0\) on the
  codimension-two space; \((0,1,\cdot)\) on \(H^\perp\): **PROVED** (computed).
* Cross forms are neutral, so the negatives must come from the archimedean
  diagonal: **PROVED** (the eigenvalues of a cross block are \(\pm\sigma_i\)).
* Row (a) is row (d)'s equality case on the codimension-two space:
  **OBSERVATION** — a reading of the above; no comparison map is constructed.
* SELF vs CROSS inertia on prime powers: **PROVED** (computed).

### Correction log

An earlier draft of this note claimed that row (a)'s degeneracy *explains* the
size of the margins measured in the certificates
(\(3.1\cdot10^{-12}\), \(4.4\cdot10^{-9}\), \(1.1\cdot10^{-7}\)).  That does
not follow: the ruling model and the localized operator \(A_T\) are different
objects with no comparison map between them, so nothing about the first
constrains the second.  The claim was rhetorical and has been removed.

The same draft also argued the opposite error — that the neutrality of cross
forms *refutes* the rank-cut route, and that a rank-one cross form would vanish
on the primitive space and contradict row (c).  Both are wrong: neutrality is
the mechanism, not an obstruction (§2), and the vanishing happens on the
codimension-**two** space, not on \(H^\perp\) (§1).  Confusing those two
subspaces is the error to watch for in this phase.
* \(d\Psi-dx\) as the centred degree vector: **HYPOTHESIS**, the phase's
  target.
* Row D: **OPEN**.
