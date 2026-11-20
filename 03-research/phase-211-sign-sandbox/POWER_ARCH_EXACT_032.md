# POWER_ARCH_EXACT_032 — Stable formulas and certified remainder for ARCH2111

Status: **PROVED**, independent review approved in POWER_CONTACT_AUDIT_032.md and verifier PASS reproduced. For the SAME atom N211,k1,u63/2 of 021 one obtains a normalised rational interval for ARCH of width<10^(-18), without quadrature or matrices. Papers untouched. The balance with comb/polar is a separate certificate built in parallel; no global sign is claimed here.

## 1. Corpus and new reason

Read: the project rules, CONTACT_BALANCE021 (numerical diagnosis of the single atom), ROW_PATTERN029 (GAIN), INTERIOR_SCALE030 and their audits; exact module 003 and audit 002 of the Euler/Bernoulli constants. Consulted index/grid/crossword on Poisson, gamma coefficients, derivatives and Euler–Maclaurin. The Poisson recurrence and EM are prior tools and are not presented as new.

The precise difference from 021 is to replace the diagnostic quadrature of ARCH by a formula with summands of controlled sign and an explicit integral remainder. No other N is scanned, no matrix of order 211 is built, and precision is not massively increased. The only series cutoff is 32, with 16 direct summands via Hurwitz and 8 Bernoulli terms. The symbolic formula serves all N, but only the already authorised atom is certified.

The negative value of the partial sum of 021 up to 300 is NOT attributed to quadrature error: a real favourable tail was missing. The ARCH interval is built in order to decide the full balance with more contacts, keeping that accounting.

## 2. Positive series for ARCH of k0, valid at EVERY N

Let u>1/2, N>=2, d=N−1, x=(u+1/2)/2 and

    rho_N(t)=e^(−ut)sum_(j=0)^d p_jt^j,
    p0=1,
    (j+1)p_(j+1)/p_j=2u(d−j)/(2d−j).

The probability is the exact normalised gamma autocorrelation. Set

    b_j=p_j j!/2^j,
    b0=1, b_(j+1)/b_j=u(d−j)/(2d−j),
    S_p(x)=sum_(l>=0)(x+l)^(-p), p>1,
    a(u)=psi(x)−logpi.

The time integral of psi has kernel

    k_gamma(t)=2e^(−t/2)/(1−e^(−2t))=2sum_(l>=0)e^(−(1/2+2l)t).

Comparing rho_N with rho_1=e^(−ut), whose energy is a(u) by Poisson, gives by Tonelli for positive summands

    A_(N,0)(u):=ARCH_(N,0)/norm²
       =a(u)−sum_(j=1)^d b_j S_(j+1)(x).                (A0)

There are no alternating coefficients of high-order derivatives. All subtracted terms are positive and the expression converges absolutely. The formula is also interpreted for N1 with empty sum.

## 3. First column: formula still stable without subtracting two large orders

The exact identity GAIN029 is A_(N,1)=A_(N,0)+uA_(N,0)'. Since b_j is proportional to u^j, a'(u)=S2(x)/2 and dS_p/du=−pS_(p+1)/2, differentiating the FINITE sum A0 produces

    A_(N,1)=a(u)+(u/2)S2(x)
       −sum_(j=1)^d (j+1)b_j [S_(j+1)(x)−(u/2)S_(j+2)(x)]. (A1)

Each bracket has positive sign, since

    S_p(x)−(u/2)S_(p+1)(x)
      =sum_(l>=0)(x+l)^(-p)[1−u/(2(x+l))]>0,
    x=u/2+1/4>u/2.

Thus A1 even avoids subtracting 2N A_(N,0)−(2N−1)A_(N+1,0). There may be the final physical cancellation between quantities of order 1, but no list of huge derivatives with alternating signs is subtracted. Positivity of the form is not inferred from A1.

## 4. Explicit Euler–Maclaurin remainder, without a next-term hypothesis

For x16, p>=2 and M32, S_p(16) is enclosed by

    Z_p=sum_(n=16)^(M−1)n^(-p)+M^(1−p)/(p−1)+(1/2)M^(-p)
       +sum_(r=1)^8 B_(2r)/(2r)! ·(p)_(2r−1) M^(-p−2r+1),
    |S_p(16)−Z_p|<=E_p,
    E_p=|B16|/(16)! ·(p)_15 M^(-p−15).                  (EM)

Here (p)_r is the rising factorial and B16=−3617/510. The bound does NOT depend on the terms of the expansion decreasing nor on an assumed sign of the remainder.

Indeed the periodic integral remainder has modulus <=(p)_16/(16)!·sup|B16({t})| int_M^infty t^(-p−16)dt. The absolutely convergent Fourier series of the periodic Bernoulli function gives sup|B16({t})|<=|B16(0)|; integrating reduces the majorant exactly to E_p. This is an absolute integral bound valid for ALL p used, including p212.

The eight Bernoulli numbers are B2=1/6, B4=−1/30, B6=1/42, B8=−1/30, B10=5/66, B12=−691/2730, B14=7/6, B16=−3617/510, all rational.

## 5. Stable error control and shared API

The verifier computes S_p for 2<=p<=212 by (EM), keeping the endpoints as Fraction WITHOUT premature rounding. In A1 each bracket is multiplied by its rational coefficient b_j before converting to the intervals of 003. This is essential: first rounding a power 16^(-p) to a fixed grid and then multiplying it by a large b_j would lose its information.

The total contribution of the Hurwitz remainder is bounded by the positive rational sum

    E_ARCH=(u/2)E2
       +sum_(j=1)^210 (j+1)b_j[E_(j+1)+(u/2)E_(j+2)]
       <(1/2)10^(-18).                                 (ERROR)

The script also checks the width of the FINAL interval, including gamma, logpi and the outer roundings of 003: it is <10^(-18). The brackets have strictly positive lower endpoint and this fact is also verified rationally, without taking its sign from an approximation.

For u63/2, a(u)=H15−gamma−logpi. The constants inherited from 003 use explicit intervals of series and remainders already audited; no decimal value of special functions is consulted.

The API of the module `tools/power_arch_exact_032_verify.py` exports `ARCH`, the interval of ARCH2111/norm². A simple outer envelope of its endpoints is

    −1094177384741806137370/10^21
      <=ARCH2111/norm²
      <=−1094177384741806136520/10^21.                    (ARCH2111)

This printed envelope is somewhat wider than the internal interval, but still far below the error 10^(-16) required for the balance of 021. No precision greater than necessary is pursued.

## 6. Scope of the certificate and combination

The parallel certificate adds the contacts of the same atom and the polar term by exact arithmetic, using the lower endpoint of ARCH. The omitted contacts are ALL favourable by ARITHMETIC_DIFFERENCES019, because N211, u31.5 are in its range; that tail must not be discarded for an upper bound, but it may be omitted in a legitimate lower bound.

ARCH2111 by itself does not prove W>=0, and its negative sign was known. The real improvement is a small certified analytic error sufficient to decide the concrete balance, keeping ALL its terms and without blaming the earlier partial diagnosis for a global sign it never claimed.

The family of N is not extended by inference, nor is a new window T. Papers untouched.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_arch_exact_032_verify.py

Result PASS. The module can be imported without printing results and directly shares `ARCH` with the parallel contact certificate.


## 7. Audited final combination

POWER_CONTACT_DECISION_032.md combines this ARCH interval with the exact polar term and the contacts up to 512, and controls the full tail. The independent certificate POWER_CONTACT_AUDIT_032.md approves

    3.4·10^(-15)<W[f_(211,1)]/norm²<4.5·10^(-15), u=63/2.

It is a single real atom resolved; not a row nor the global sign. The diagnosis 021/032 concerned different partial sums and did not claim W negative.
