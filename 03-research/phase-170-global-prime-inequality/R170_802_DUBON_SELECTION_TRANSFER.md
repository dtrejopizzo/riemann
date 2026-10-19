# R170_802 — Dubon: what survives when selecting the frequency

Source: [Dubon, 2609.17875v1](https://arxiv.org/abs/2609.17875v1).
Detailed reading of the proof of lemma 4.1 and of proposition 5.1,
with their hypotheses and the order of limits of section 3. The
historical Jessen–Tornehave theorems invoked have not been re-audited.

## Extractable piece

Lemma 4.1 obtains bounded flat density for a sum of at least five
Steinhaus phases with comparable weights; it integrates the
small-ball probability to control the negative part of the logarithm.
The control is uniform under translation. In proposition 5.1 the
primes of (N/2,N] appear only linearly in the truncated polynomial and
their phases can be integrated by conditioning on the rest. It is
average control, not pointwise.

## Our own consequence: explicit cost of selecting new phases

Let q be the old information and, conditioned on q, let Z_p be
independent Haar phases for a finite set of new primes. Let a_p(q) be
measurable coefficients in q, and

    S(q,Z)=Σ_p a_p(q) Z_p,      V(q)=Σ_p |a_p(q)|².

Any modulation exp(iΓ(q)log p) selected by q is allowed in a_p: it
does not change the moduli nor the conditional law. Then

    E(S|q)=0,      E(|S|²|q)=V(q),
    E(exp(t Re S)|q)≤exp(t² V(q)/4),    t real.

Proof: independence, rotational invariance, and
I₀(u)=Σ(u²/4)^k/(k!)²≤exp(u²/4). RH is not assumed.

If ν_q is a law of new phases absolutely continuous with respect to
Haar μ, with relative entropy H_q=D(ν_q||μ)<∞, then

    E_{ν_q}(Re S) ≤ sqrt(V(q) H_q).

Proof: the entropy variational inequality, obtained by Jensen applied
to exp(t Re S)/(dν/dμ), gives
t Eν ReS≤H_q+log Eμ exp(t ReS). Minimize H_q/t+tV/4.
The cases V=0 or H_q=0 follow directly or by a limit.

Conditioning Haar on an event A of measure p>0, H=log(1/p). Thus

    E(Re S | q,A) ≤ sqrt(V log(1/p)).

This inequality specifies exactly how much it costs to turn selection
into bias. **It does not prove our bound on γ_q:** evaluation at a
single phase configuration is a Dirac measure, singular with respect
to Haar, with infinite entropy. The deterministic spectrum does not
acquire a random law merely by passing to the torus.

## Checking that the gap is real

For a_p>0, the configuration Z_p=1 produces S=Σa_p. By rational
independence of the logarithms of the primes, there exist heights that
simultaneously approximate those phases for any finite set. Hence
unique factorization plus Haar independence does not rule out
pointwise resonances. It is not claimed that those heights are those
of the first contact; precisely what is missing is a property of the
selector that excludes them.

## Admissible use toward D

The conditional result can be useful if it is proved that the extremal
equation allows replacing the evaluation by a phase law with a
controlled selection cost and error smaller than the budget. Today no
such representation exists in our construction. The usefulness of the
extraction is a verifiable quantitative obligation, not a proved
annihilation.
