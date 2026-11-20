"""Exact rational kernel truncation certificate, BUILD083 (60)-(63).

Certifies only the uniform operator approximation, not positivity.
No floating point evaluation or numerical quadrature is used.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def coefficients(degree):
    # B(u)=(1-exp(-2u))/u; B*r=(exp(-u/2)-B/2)/u.
    b = [F((-1)**j * 2**(j+1), factorial(j+1))
         for j in range(degree+2)]
    c = []
    for k in range(degree+1):
        rhs = F((-1)**(k+1), 2**(k+1)*factorial(k+1))-b[k+1]/2
        c.append((rhs-sum((b[j]*c[k-j] for j in range(1,k+1)), F(0)))/2)
    return c


def main():
    degree = 384
    c = coefficients(degree)
    assert c[:4] == [F(1,4), F(-1,48), F(-1,32), F(7,11520)]
    delta = F(21,4)*F(4,5)**(degree+1)
    xi = F(8,5)*delta
    assert xi < F(1,10**35)
    # A convenient conservative transfer budget for (63), both sizes.
    theta = F(1,10**20)
    eta = F(1,10**370)
    rho = F(1783,500)
    budget = xi+(1+1/theta)*xi**2*(rho+8*(1+eta))
    assert budget < F(1,10**35)
    report = dict(status='PASS',
                  scope='kernel operator approximation and transfer constants only; no sign certificate',
                  T='4/5', degree=degree,
                  coefficient_recurrence='B*r=(exp(-u/2)-B/2)/u',
                  coefficients=[str(v) for v in c],
                  delta_exact=str(delta), xi_exact=str(xi),
                  xi_upper='1/10^35', theta=str(theta),
                  transfer_budget_upper='1/10^35')
    path = Path(__file__).with_name('kernel_polynomial_certificate.json')
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()
                      if k not in ('coefficients','delta_exact','xi_exact')},indent=2))


if __name__ == '__main__':
    main()
