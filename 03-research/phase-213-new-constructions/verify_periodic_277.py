"""Enclose one coefficient of the sharply truncated local Weil kernel."""
from math import isqrt

from flint import acb, arb, ctx


def prime_contacts(length, frequency):
    total = arb(0)
    # The adjacent integer log tests certify the range of powers.
    assert arb(254).log() < length < arb(255).log()
    for prime in range(2, 255):
        if any(prime % divisor == 0 for divisor in range(2, isqrt(prime) + 1)):
            continue
        power = prime
        while power <= 254:
            total += arb(prime).log() * (frequency * arb(power).log()).cos() / arb(power).sqrt()
            power *= prime
    return -2 * total


def main():
    ctx.prec = 160
    length = arb(277) / 50
    frequency = 50 * arb.pi()
    arch = acb(arb(1) / 4, frequency / 2).digamma().real - arb.pi().log()
    polar = arb(0)
    for a in [arb(1) / 2, -arb(1) / 2]:
        z = acb(a, frequency)
        polar += 2 * (((z * length).exp() - 1) / z).real

    tail = arb(0)
    for j in range(4):
        z = acb(arb(1) / 2 + 2 * j, -frequency)
        tail += 2 * ((-z * length).exp() / z).real
    first_omitted = arb(17) / 2
    error = 2 * (-first_omitted * length).exp() / (
        first_omitted * (1 - (-2 * length).exp())
    )
    scaled_coefficient = arch + polar + tail + prime_contacts(length, frequency)
    assert scaled_coefficient - error > -arb(1230) / 1000
    assert scaled_coefficient + error < -arb(1229) / 1000
    print('PASS: -1.230 < P times Fourier coefficient 450 < -1.229')


if __name__ == '__main__':
    main()
