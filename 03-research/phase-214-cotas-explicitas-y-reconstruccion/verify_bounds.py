"""Evaluate log10 of the exponent in the phase 214 lower bound."""
from flint import arb, ctx

ctx.prec = 160
for radius in (5, 10):
    s = arb(radius + 1)
    u = radius + arb(1) / 100
    # Each dyadic bin is bounded using the central binomial coefficient.
    log_two = arb(2).log()
    bins = (2*u/log_two).ceil().unique_fmpz()
    assert bins is not None
    comb = sum(2 * arb(2)**k * log_two / (arb(2)**(k-1)).sqrt()
               for k in range(1, int(bins)+1))
    log_radius = comb + 5
    # H=200m and m <= 11 s R, hence a >= 1/(9680000 s^2).
    log_cost = (22*s).log() + log_radius + (9680000*s*s).log().log()
    digits = log_cost / arb(10).log()
    ceiling = digits.ceil().unique_fmpz()
    assert ceiling is not None and digits < arb(ceiling)
    print(f'T={radius}: log10 K = {digits}, hence W >= exp(-10^{ceiling}) ||f||^2')
