"""Exact step-source formulas evaluated with mpmath; no interval certificate.

The primitive/high projections must still be applied with their full actions.
This module alone does not evaluate a projected corrector or its gain.
"""
import json
from pathlib import Path
import mpmath as mp


def tail(d):
    if not d > 0:
        raise ValueError('Step endpoints have logarithmic singularities')
    z = mp.exp(-d/2)
    return mp.atanh(z)+mp.atan(z)


def arch_step(x,a,b):
    if not a < b:
        raise ValueError('Require a < b')
    if x == a or x == b:
        raise ValueError('Evaluate away from step endpoints')
    if x < a:
        return -tail(a-x)+tail(b-x)
    if x > b:
        return -tail(x-b)+tail(x-a)
    constant = -mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi)
    return constant+tail(x-a)+tail(b-x)


def physical_step(x,a,b,contacts):
    """contacts are (log n, Lambda(n)/sqrt(n)), already cut at 2T."""
    value = arch_step(x,a,b)
    for length,weight in contacts:
        value -= weight*(int(a < x+length < b)+int(a < x-length < b))
    return value


def exponential_increment(d,sign):
    """Integral H0(u)*(1-exp(sign*u/2)) from zero to d."""
    if d < 0 or sign not in (-1,1):
        raise ValueError('Require d >= 0 and sign +/-1')
    q = mp.exp(-d/2)
    if sign == 1:
        return (-d-mp.log1p(q)-mp.log1p(q*q)/2-mp.atan(q)
                +3*mp.log(2)/2+mp.pi/4)
    return (-mp.log1p(q)+mp.log1p(q*q)/2-mp.atan(q)
            +mp.log(2)/2+mp.pi/4)


def arch_exponential(x,T,sign):
    """Arch action on exp(sign*x/2)*1_(-T,T), only for interior x."""
    if not -T < x < T or sign not in (-1,1):
        raise ValueError('Require interior x and sign +/-1')
    constant = -mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi)
    return mp.exp(sign*x/2)*(constant+tail(x+T)+tail(T-x)
               +exponential_increment(x+T,-sign)
               +exponential_increment(T-x,sign))


def physical_exponential(x,T,sign,contacts):
    value = arch_exponential(x,T,sign)
    for length,weight in contacts:
        for t in (x+length,x-length):
            if -T < t < T:
                value -= weight*mp.exp(sign*t/2)
    return value


def check():
    mp.mp.dps = 70
    a,b = -mp.mpf(2)/5,mp.mpf(3)/5
    constant = -mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi)
    def kernel(u):
        return mp.exp(-u/2)/(-mp.expm1(-2*u))
    errors = []
    for x in (-mp.mpf(4)/5,-mp.mpf(1)/10,mp.mpf(1)/5,mp.mpf(4)/5):
        if a < x < b:
            direct = constant+mp.quad(kernel,[x-a,mp.inf])+mp.quad(kernel,[b-x,mp.inf])
        else:
            direct = -mp.quad(lambda y: kernel(abs(x-y)),[a,b])
        errors.append(abs(direct-arch_step(x,a,b)))
        assert abs(arch_step(-x,-b,-a)-arch_step(x,a,b)) < mp.mpf('1e-60')
    assert max(errors) < mp.mpf('1e-60')
    report = dict(status='PASS_NUMERICAL_FORMULA_CHECK',decimal_digits=70,
                  points=4,maximum_error=str(max(errors)),
                  scope='unprojected step source; no interval enclosure or sign claim')
    Path(__file__).with_name('step_source_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    check()
