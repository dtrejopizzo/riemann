# Master Plan

## Status

Rows A, B and C are closed on the declared carrier (Papers 43–45). Row D — positivity
$\lambda_A(T)\ge0$ of the window form on $P_T$ — is **OPEN**. It is proved for
$T\le\tfrac12\log15$ (certified; endpoint due to Mori, cited in Paper 47). Paper 47 is the single
paper of record for row D; it closes only when row D closes.

## The open node

In the even sector (Paper 47, `prop:H`, `cor:H1minus`), positivity for all $T$ is equivalent to the
statement that the archimedean-plus-prime form has exactly one negative direction. In the finite
coordinates $E_N^{\mathrm{ev}}=\mathrm{span}\{\sin(\pi k(x+T)/2T): k \text{ odd} \le N\}$,
$N\approx4T$ (`lem:combsine`), this becomes the **node**: for every $F$ with
$\ell_T(F)=\int F(x)\cosh(x/2)\,dx=0$,
$$Q_T(F)=(\mathfrak m_T+\mathfrak e_T)(F)+\Phi_T(F)\ \ge\ 0,\qquad
\Phi_T(F)=-\int_{[1^-,e^{2T}]}2t^{-1/2}c_F(\log t)\,d(\psi(t)-t),$$
where $\mathfrak m_T$ is the conductor-one gamma factor, $\mathfrak e_T$ the pole kernel and
$c_F$ the autocorrelation of $F$. On that orthogonal $Q_T=W_T$ exactly.

- PROVED for $T\le\tfrac12\log5$ (corollary of Paper 47 `thm:log5W`).
- A necessary counting consequence: $n_+(\Phi_T)\ge N'-1$ on the polar orthogonal, with
  $N'\approx1.95T$ the negative index of the archimedean part — an exact cancellation, not a
  perturbation.
- Properties any proof must have (phases 200–207): it must use that $\Lambda$ comes from the Euler
  product over $\mathbb N$ (the falsifier $a_P$ shows this); it cannot be a sum-of-squares
  certificate, a size bound $|\Phi|\le\mathfrak m$, a linear Hamburger-type rigidity, a bilinear
  argument through $h^*$, a Szegő/Widom asymptotic, a continuation in $T$, or a Perron–Frobenius
  argument (each is a NO-GO in a declared class).

## The live gate

After the class-impossibility theorem of phase 207 there is one live gate: a sign step whose
premises are theorems only for logarithmic derivatives of $L$-functions with an Euler product over
all primes (hence not inherited by the falsifier models), with margin compatible with
$e^{-15.449T}$. No candidate object is known. The "empty cell" of the literature survey (weight
$n^{-1/2}$, global functional equation, built-in positivity) is the place such an object would
live; the known extremes are Helson's multiplicative Hilbert matrix (weight ½, no functional
equation) and automorphic norms (functional equation, weight 1).

## Working rules

- Before any construction, search the routes index (`05-meta-and-planning/ROUTES-TRIED-INDEX/`),
  the master grid and the crossword; nothing listed there is retried without a new, explicit reason.
- Every result is labelled PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL, and
  every new closed route or falsifier is added to the index.
- Every integration into Paper 47 is checked against the paper's own definitions.
