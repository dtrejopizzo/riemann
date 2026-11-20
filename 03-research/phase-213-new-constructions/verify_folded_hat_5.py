"""Certify a sampling net for the piecewise linear space of radius five."""
from pathlib import Path
from flint import arb, acb, ctx

ctx.prec = 96
period = 2 * arb.pi() * 1024 / 10
path = Path(__file__).resolve().parents[2] / "06-grafico" / "zeros_10000.txt"
# Decimal guesses only locate brackets. Sign changes verify existence.
guesses = path.read_text().splitlines()[:10000]
radius = arb(1) / 100000
log_pi = arb.pi().log()

def hardy_sign_value(t):
    s = acb(arb(1)/2, t)
    phase = (s/2).lgamma().imag - t*log_pi/2
    return (acb(0, phase).exp()*s.zeta()).real

def fold(x):
    return x - period * (x/period).floor().unique_fmpz()

# One candidate per narrow cell suffices. Center choices affect run time only.
selected = {}
for raw in guesses:
    x = arb(raw)
    for sign in (1, -1):
        center = fold(sign*x)
        cell = int((center*300).floor().unique_fmpz())
        selected.setdefault(cell, (raw, sign, center))
ordered = sorted(selected.values(), key=lambda entry: float(entry[2]))
# Keep a subcover, then verify its actual cyclic gaps with balls.
kept = [ordered[0]]
for i in range(1, len(ordered)-1):
    if ordered[i+1][2] - kept[-1][2] > arb('0.335'):
        kept.append(ordered[i])
kept.append(ordered[-1])
checked = set()
for raw, sign, center in kept:
    if raw not in checked:
        x = arb(raw)
        assert x+radius < 10000
        assert hardy_sign_value(x-radius)*hardy_sign_value(x+radius) < 0
        checked.add(raw)
centers = [entry[2] for entry in kept]
assert all(0 < b-a for a,b in zip(centers, centers[1:]))
assert max(b-a for a,b in zip(centers, centers[1:]+[centers[0]+period])) + 2*radius < arb('0.34')
gain = arb('0.15')**2 / 10000**4
loss = arb('0.0465') * arb(5).exp() / (3*10**12)**2
assert gain > 1000000*loss
print(f'PASS: {len(checked)} certified sign changes, cyclic gap <0.34, gain >10^6 times tail')
