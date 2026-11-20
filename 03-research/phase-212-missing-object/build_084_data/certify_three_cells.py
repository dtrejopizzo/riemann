"""Certify the primitive unit-cell family (1,2,k), all integers k>=3.

Finite Arb check for 3<=k<256; one analytic-tail constant for k>=256.
The binomial bound and the tail comparison are proved in BUILD_084.
This is not a certificate for arbitrary combinations of cell tests.
"""
import json
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scale', default='1')
    args = parser.parse_args()
    scale_fraction = Fraction(args.scale)
    assert scale_fraction > 0
    ctx.dps = 100
    scale = arb(scale_fraction.numerator)/scale_fraction.denominator
    cutoff = 256
    a = arb(2).log()
    b = (arb(3)/2).log()
    d = a-b
    assert b*b+a*a+d*d < 1
    constant = -arb.const_euler()-(2*arb.pi()).log()

    def xlogx(n):
        return arb(n)*arb(n).log() if n else arb(0)

    def h(n):
        return xlogx(n+2)-2*xlogx(n+1)+xlogx(n)

    def diagonal(i):
        return constant+xlogx(i+1)-xlogx(i)-h(2*i)/2

    # Exact prime-power support, enclosing log(p) with Arb.
    mangoldt = [arb(0) for _ in range(cutoff)]
    composite = [False]*cutoff
    for p in range(2, cutoff):
        if composite[p]:
            continue
        for n in range(p*p, cutoff, p):
            composite[n] = True
        power = p
        while power < cutoff:
            mangoldt[power] = scale*arb(p).log()
            power *= p

    def entry(i, j):
        if i == j:
            return diagonal(i)
        i, j = min(i, j), max(i, j)
        arch = -(h(i+j)+h(j-i-1))/2
        comb = sum((mangoldt[n]/n for n in range(2, j+1)
                    if n*i <= j < n*(i+1)), arb(0))
        return arch-comb

    m11, m22, m12 = entry(1, 1), entry(2, 2), entry(1, 2)
    records = []
    for k in range(3, cutoff):
        c = (arb(k+1)/k).log()
        coeff = [b-c, c-a, d]
        cells = [1, 2, k]
        energy = sum((coeff[r]*coeff[s]*entry(cells[r], cells[s])
                      for r in range(3) for s in range(3)), arb(0))
        assert energy > 0, (k, str(energy))
        assert energy > arb(1)/1000, (k, str(energy))
        records.append({'k': k, 'energy': str(energy)})

    # c=log(1+1/k) is contained in [0,1/256] throughout the tail.
    cbox = arb(1)/512 + arb(0, arb(1)/512)
    first_block = (m11*(b-cbox)**2 + m22*(a-cbox)**2
                   -2*m12*(b-cbox)*(a-cbox))
    assert first_block > arb(15)/100
    return_bound = scale*(2*a + 2*arb(cutoff).log()/cutoff)
    arch_cross_bound = (arb(1)/(cutoff+1)+arb(1)/(cutoff-2))/2
    tail = (first_block + d*d*(arb(cutoff).log()+constant)
            -2*b*d*(return_bound+arch_cross_bound))
    assert tail > arb(1)/1000
    if scale_fraction == 1:
        assert tail > arb(8)/100
    report = {
        'status': 'PASS_THREE_CELL_FAMILY',
        'scope': 'primitive tests on cells (1,2,k), every integer k>=3',
        'mangoldt_scale': str(scale_fraction),
        'decimal_digits': ctx.dps,
        'finite_range': [3, cutoff-1],
        'finite_energy_lower': '1/1000',
        'tail_start': cutoff,
        'first_block_interval': first_block.str(60),
        'first_block_lower': first_block.lower().str(60),
        'tail_lower_interval': tail.str(60),
        'tail_lower_bound': tail.lower().str(60),
        'tail_energy_lower': '8/100' if scale_fraction == 1 else '1/1000',
        'uniform_Rayleigh_lower': '1/1000',
        'records': records,
        'limitation': 'does not certify sums of distinct three-cell tests',
    }
    filename = ('three_cell_family_certificate.json' if scale_fraction == 1
                else f'three_cell_family_scaled_{scale_fraction.numerator}_{scale_fraction.denominator}_certificate.json')
    destination = Path(__file__).with_name(filename)
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: val for key, val in report.items() if key != 'records'}, indent=2))


if __name__ == '__main__':
    main()
