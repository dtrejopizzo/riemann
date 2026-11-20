"""Validate interval integral engine on exact identities and an A_K source.

Integral enclosures use analytic remainder bounds. Numerical references are
only independent implementation diagnostics, never the source of the bound.
"""
from pathlib import Path
import json
import mpmath as mm
from certify_kernel_polynomial import coefficients
from polynomial_source import rational, pieces, source_value
from interval_source_integrals import source_inner


def overlaps(a,b): return a.a <= b.b and b.a <= a.b


def main():
    mm.iv.dps = 120
    mm.mp.dps = 130
    c = mm.iv
    T = c.mpf(4)/5
    zero = c.mpf(0)
    def single(source): return [(zero,T,source)]
    left = single(([],[c.mpf(1)],[],[]))
    right = single(([],[],[c.mpf(1)],[]))
    smooth = single(([],[],[],[c.mpf(1)]))
    exact_cases = [
        (left,left,2*T,'log squared'),
        (left,right,T*(2-c.pi**2/6),'mixed endpoints'),
        (smooth,smooth,T*(2*c.log(2)**2-4*c.log(2)+2),'smooth log squared')]
    for f,g,expected,name in exact_cases:
        result = source_inner(c,f,g,T,degree=192)
        assert overlaps(result,expected),name
        assert (result.b-result.a) < c.mpf('1e-60'),name
    coeff = coefficients(8)
    exact_f = ['2/3','-7/5','11/4','-2','1/7']
    ki = [rational(c,x) for x in coeff]
    fi = [rational(c,x) for x in exact_f]
    kp = [rational(mm.mp,x) for x in coeff]
    fp = [rational(mm.mp,x) for x in exact_f]
    Tp = mm.mp.mpf(4)/5
    records = []
    for sigma in (1,-1):
        print('Integrating parity',sigma,flush=True)
        pi = pieces(c,fi,ki,sigma)
        result = source_inner(c,pi,pi,T,degree=192)
        reference = sum(mm.mp.quad(lambda x: source_value(mm.mp,source,x,Tp)**2,[a,b])
                        for a,b,source in pieces(mm.mp,fp,kp,sigma))
        ref = c.mpf(mm.mp.nstr(reference,130))
        assert result.a <= ref.a and ref.b <= result.b
        assert (result.b-result.a) < c.mpf('1e-25')
        records.append(dict(sigma=sigma,enclosure=str(result),
                            width=str(result.b-result.a),numerical_reference=str(reference)))
    report = dict(status='PASS',scope='validated scalar source integral tests; no full matrix or sign certificate',
                  interval_dps=120,kernel_degree=8,input_degree=4,
                  smooth_log_degree=192,exact_identities=len(exact_cases),records=records)
    Path(__file__).with_name('interval_source_integrals_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
