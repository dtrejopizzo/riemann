#!/usr/bin/env python3
"""Arb verification of the stable Legendre exponential-kernel formula."""
from flint import arb,ctx
ctx.prec=2048
N=170

def qcols(k):
    q=[[arb(0) for _ in range(N)] for _ in range(N)]
    for n in range(N):
        suffix=[arb(0),arb(0)]
        for j in range(n,-1,-1):
            rhs=arb(1) if j==n else arb(0)
            q[j][n]=(rhs-(2*j+1)*suffix[1-j%2])/k
            suffix[j%2]+=q[j][n]
    return q

for text in ('0.40235947810852507','16','120','257.5'):
    k=arb(text);q=qcols(k)
    qm=[sum(((-1)**j*q[j][n] for j in range(n+1)),arb(0)) for n in range(N)]
    ee=[2*((-1)**n)*(arb.pi()/(2*k)).sqrt()*(-k).exp()*k.bessel_i(arb(n)+arb('.5'))
        for n in range(N)]
    def raw(m,n):
        return (2*q[m][n]/(2*m+1)-ee[m]*qm[n]
               +2*q[n][m]/(2*n+1)-ee[n]*qm[m])
    exact00=4/k-2*(1-(-2*k).exp())/(k*k)
    assert abs(raw(0,0)-exact00) < arb('1e-500')
    for m,n in ((0,169),(37,92),(168,169),(81,81)):
        assert raw(m,n).is_finite()
        assert raw(m,n).rad() < arb('1e-90')
    print('PASS k=',k,'A00=',raw(0,0),'edge radius=',raw(168,169).rad())
print('PASS Arb stable Legendre kernel and scaled-Bessel boundary enclosures')
