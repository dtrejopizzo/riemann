"""Complete 2x2 Gram certificates for span(F_3,F_k), every k>=4.

Analytic tail k>=16384, finite interval check below it. Does not certify
spaces with multiple moving indices. See BUILD_084 for cell normalization.
"""
import json
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scale', default='1')
    parser.add_argument('--cutoff', type=int, default=16384)
    args = parser.parse_args()
    scale_fraction = Fraction(args.scale)
    assert scale_fraction > 0
    ctx.dps = 100
    scale = arb(scale_fraction.numerator)/scale_fraction.denominator
    cutoff = args.cutoff
    assert cutoff >= 256
    log = lambda n: arb(n).log()
    xlogx = lambda n: arb(n)*log(n) if n else arb(0)
    h = lambda n: xlogx(n+2)-2*xlogx(n+1)+xlogx(n)
    constant = -arb.const_euler()-(2*arb.pi()).log()
    diagonal = lambda i: constant+xlogx(i+1)-xlogx(i)-h(2*i)/2
    arch = lambda i, j: -(h(i+j)+h(j-i-1))/2
    a, b = log(2), log(3)-log(2)
    d = a-b
    c3 = log(4)-log(3)
    u = [b-c3, c3-a, d]
    m11, m22, m33 = diagonal(1), diagonal(2), diagonal(3)
    m12 = arch(1, 2)-scale*log(2)/2
    m13 = arch(1, 3)-scale*(log(2)/2+log(3)/3)
    m23 = arch(2, 3)
    fixed = [[m11,m12,m13], [m12,m22,m23], [m13,m23,m33]]
    t = [sum((u[r]*fixed[r][i] for r in range(3)), arb(0)) for i in (0,1)]
    g33 = sum((u[r]*fixed[r][s]*u[s]
               for r in range(3) for s in range(3)), arb(0))
    assert g33 > arb(8)/100
    assert b*b+a*a+d*d < 1

    cbox = arb(1)/(2*cutoff)+arb(0,arb(1)/(2*cutoff))
    sbox = (b-cbox)*t[0]+(cbox-a)*t[1]
    arch_bound = lambda i: (arb(1)/(cutoff+i)+arb(1)/(cutoff-i-1))/2
    positive_group = (-u[1])*(scale*3*a/2+arch_bound(2))
    negative_group = (u[0]*(scale*(2*a+2*log(cutoff)/cutoff)+arch_bound(1))
                      +u[2]*(scale*4*a/3+arch_bound(3)))
    cross_upper = max((sbox+d*positive_group).abs_upper(),
                      (sbox-d*negative_group).abs_upper())
    assert cross_upper < arb(1)/4
    block = m11*(b-cbox)**2+m22*(a-cbox)**2-2*m12*(b-cbox)*(a-cbox)
    tail_diagonal = (block+d*d*(log(cutoff)+constant+1-arb(1)/(4*cutoff))
                     -2*b*d*(scale*(2*a+2*log(cutoff)/cutoff)+arch_bound(1)))
    tail_schur = tail_diagonal-cross_upper**2/g33
    if not tail_schur > arb(2)/1000:
        diagnostic = {
            'status': 'UNRESOLVED_TAIL_MAJORANT',
            'mangoldt_scale': str(scale_fraction),
            'tail_start': cutoff,
            'tail_comparison_interval': tail_schur.str(60),
            'meaning': 'sufficient tail bound did not pass; no negative test or sign conclusion',
        }
        name = f'planes_tail_unresolved_{scale_fraction.numerator}_{scale_fraction.denominator}_{cutoff}.json'
        Path(__file__).with_name(name).write_text(json.dumps(diagnostic,indent=2)+'\n')
        print(json.dumps(diagnostic,indent=2))
        raise SystemExit(1)

    mangoldt = [arb(0) for _ in range(cutoff)]
    composite = [False]*cutoff
    for p in range(2,cutoff):
        if composite[p]:
            continue
        for n in range(p*p,cutoff,p):
            composite[n] = True
        power = p
        while power < cutoff:
            mangoldt[power] = scale*log(p)
            power *= p
    prefix = [arb(0)]
    for n in range(1,cutoff):
        prefix.append(prefix[-1]+mangoldt[n]/n)

    smallest = None
    smallest_index = None
    count = 0
    finite_cross_upper = arb(0)
    for k in range(4,cutoff):
        c = log(k+1)-log(k)
        column = [arch(i,k)-prefix[k//i]+prefix[k//(i+1)] for i in (1,2,3)]
        g3k = (b-c)*t[0]+(c-a)*t[1]+d*sum((u[r]*column[r] for r in range(3)),arb(0))
        assert g3k.abs_upper() < arb(1)/4, k
        finite_cross_upper = max(finite_cross_upper,g3k.abs_upper())
        gkk = (m11*(b-c)**2+m22*(a-c)**2-2*m12*(b-c)*(a-c)
                +d*d*diagonal(k)+2*d*((b-c)*column[0]+(c-a)*column[1]))
        schur = gkk-g3k*g3k/g33
        assert schur > arb(1)/1000, (k,str(schur))
        low = schur.lower()
        if smallest is None or low < smallest:
            smallest, smallest_index = low, k
        count += 1
    assert count == cutoff-4
    report = {
        'status': 'PASS_ANCHORED_PLANES',
        'scope': 'span(F_3,F_k) for each integer k>=4, common cell coordinates',
        'mangoldt_scale': str(scale_fraction),
        'decimal_digits': ctx.dps,
        'fixed_pivot': g33.str(60),
        'finite_range': [4,cutoff-1],
        'finite_count': count,
        'finite_schur_lower': '1/1000',
        'finite_cross_upper': finite_cross_upper.str(60),
        'smallest_finite_lower': smallest.str(60),
        'smallest_finite_index': smallest_index,
        'tail_start': cutoff,
        'tail_cross_upper': cross_upper.str(60),
        'tail_schur_lower': tail_schur.lower().str(60),
        'certified_tail_schur_lower': '2/1000',
        'uniform_Rayleigh_lower': '1/50000',
        'limitation': 'no claim for sums involving several distinct moving indices',
    }
    filename = ('anchored_planes_certificate.json' if scale_fraction == 1
                else f'anchored_planes_scaled_{scale_fraction.numerator}_{scale_fraction.denominator}_certificate.json')
    Path(__file__).with_name(filename).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
