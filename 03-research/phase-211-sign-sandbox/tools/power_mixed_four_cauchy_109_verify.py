"""Design109: intersect computed Taylor coefficients with prior Cauchy bounds.

No theta on import. Modules107/108, all parameters and the correction2^-200
remain unchanged. No coefficient is discarded or replaced by a midpoint.
"""
from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace
import sys
from flint import arb

EXPECTED = {
    'power_mixed_four_origin_branch_107.py':
        '15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553',
    'power_mixed_four_compact_107_verify.py':
        '2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054',
    'power_mixed_four_polynomial_108_verify.py':
        'eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a',
}


def clipped_builder(origin, a):
    K, J, phi = origin.build_origin_polynomials(a)
    rebuilt = []
    for name, derivatives, bound_exponent, order in (
            ('K',K,42,3),('J',J,42,3),('phi',phi,40,4)):
        coefficients = derivatives[0].coeffs()
        assert len(coefficients) <= origin.DEGREE+1
        bounded = []
        for k, coefficient in enumerate(coefficients):
            assert coefficient.is_finite()
            # The bounds refer to the SAME complete Taylor coefficients.
            # Empty intersection is an error, never a value chosen to pass.
            cauchy_box = arb(0, arb(2**(bound_exponent+k)).upper())
            try:
                intersection = coefficient.intersection(cauchy_box)
            except ValueError as error:
                raise ValueError(f'empty Cauchy intersection for {name}[{k}]') from error
            assert intersection.is_finite()
            bounded.append(intersection)
        rebuilt.append(origin.derivative_polynomials(bounded,order))
        print('109 Cauchy coefficient intersections',name,len(bounded),flush=True)
    return tuple(rebuilt)


def main():
    here = Path(__file__).resolve().parent
    print('DRIVER109 SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
    for name,expected in EXPECTED.items():
        actual = sha256((here/name).read_bytes()).hexdigest()
        assert actual == expected,(name,actual,expected)
        print('UNCHANGED MODULE SHA256',name,actual,flush=True)
    import power_mixed_four_origin_branch_107 as origin
    import power_mixed_four_polynomial_108_verify as polynomial
    import power_mixed_four_compact_107_verify as remaining
    # A new namespace supplies an explicitly bounded builder. Neither module
    # objects nor their on-disk sources are modified by this wrapper.
    proxy = SimpleNamespace(**{name:getattr(origin,name) for name in (
        'PREC','CAP','MODES','DEGREE','INITIAL_CELLS','MAX_DEPTH','MAX_EVALS',
        'ball','certified_a')})
    proxy.build_origin_polynomials = lambda a: clipped_builder(origin,a)
    print('109 uses the unchanged108 polynomial algorithm with Cauchy-bounded coefficients',flush=True)
    try:
        result = polynomial.run_correlated_origin(proxy)
    except ValueError as error:
        print('INCONCLUSIVE109: construction error',str(error),flush=True)
        return 2
    if result['status'] != 'PASS':
        print('NO FULLPASS109: ORIGIN',result,flush=True)
        return 1 if result['status']=='NEGATIVE' else 2
    rest = remaining.certify_rest(result['a'])
    if rest['status'] != 'PASS':
        print('NO FULLPASS109: REST',rest,flush=True)
        return 1 if rest['status']=='NEGATIVE' else 2
    print('FULLPASS109: bounded origin and unchanged107 rest',result,rest,flush=True)
    return 0


if __name__=='__main__':
    sys.exit(main())
