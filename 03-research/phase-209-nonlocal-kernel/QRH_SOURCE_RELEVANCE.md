# QRH — relevance for the counterterm of 017

2026-10-19. Focused reading, independently reviewed.
**EXTERNAL CLAIM / OPEN transfer**, not a full validation of the preprints.

## Sources and versions read

- Shiva Kintali, *A Short Proof of the Quasi-Riemann Hypothesis*, 7Oct2026,
  27 pages: https://shivakintali.github.io/papers/QRH.pdf .
  Thm1 claims the free region Re s>47/48 for the declared families.
- OpenAI, *The Quasi-Riemann Hypothesis*, 5Oct2026, current PDF, 47 pages:
  https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf .
  Thm1.1 claims Re s>11/12; 7/8 is another cited document, not this theorem.

L74 already recorded the second approach; the outdated entry is corrected.
The complete Lean formalisation and an alleged 3/4 barrier were not
verified here and are not used as facts. No closed route is repeated:
the tools and hypotheses of these requested sources are examined.

## Concrete tools that do appear

OpenAI Prop3.1 controls a second moment of twisted Möbius sums.
Prop5.2 and Lem5.3 complete cubic indices, apply a quadratic sieve and
transfer estimates by Möbius inversion and iteration. The bounds
are upper bounds, averaged over families, with dependence on derivatives
of the tests. They are not a lower bound for the form of paper47.

Kintali Lem3–4 and §3.3 control a probe via theta reflection and balanced
energy. Lem7 compares probe and signal with saving 1/4800 in the regime
of contradiction beta_*>47/48. The comparison uses classification by zeros
and zero density; the numerator is controlled as nonvanishing in Re s>11/12.
Continuing that bootstrap down to 1/2 is not justified.

The finite exclusions of primes S are an explicit part of both
mechanisms. Their positive norms or isolated estimates do not by themselves select
the complete product required by our link.

## Exact comparison with 017

017 requires, for each window and each even polar-free test,

    E_pos(F) >= (A_T-C0)||F||².

None of the identified lemmas represents this deficit through the
estimated families nor contributes a domination with the required orientation.
The possible application consists in constructing that arithmetic identity;
importing the free-region statement or the positivity of a norm is not enough.

Even granting an estimate E(x)=psi(x)-x=O(x^theta log^B x),
theta>1/2, integration by parts of the fluctuating term involves

    E(x)x^(-3/2)[c_F'(log x)-c_F(log x)/2].

Its absolute estimate up to X=e^(2T) has scale
X^(theta-1/2)log^B X, in addition to the lower boundary. For theta=11/12
it is exp(5T/6), and for 47/48 it is exp(23T/24), with test/log factors.
This is not a source of sign nor a bound relative to the near-kernel.
It is an insufficiency of this direct application, NOT a NO-GO for other links.

## Outcome of the consultation

A potentially reusable toolbox for transfer of cancellation;
no control of the counterterm 017 was identified. These external
results are not integrated as proved theorems in paper47. D is not closed,
no construction 018 is created and no general impossibility is claimed.


## Publication context: Quanta 19Oct2026

https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/

Quanta distinguishes the manuscript of 30Sept (7/8) and that of 5Oct (11/12).
It reports a Lean formalisation of the first and a favourable reading by experts;
it does not present the second as formalised. This is journalistic attribution:
this session did not run the verifier nor audit the proofs in full.
The primary README of 30Sept confirms the title and the threshold 7/8.
The article highlights the selection of a metaplectic family and the synthesis
of existing techniques. It is not appropriate to discard an application to D merely
because it uses known tools; its link needs to be identified.
The requested quantitative extrapolation is analysed separately in
QRH_EXPONENT_MAP.md: replica lemma proved, critical improvement OPEN.
