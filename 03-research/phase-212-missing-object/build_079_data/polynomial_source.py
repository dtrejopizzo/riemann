"""Polynomial/logarithmic source of BUILD083 (64), including contacts.

Coefficient arithmetic works with mpmath.mp or mpmath.iv. This module
assembles A_K f; it does not integrate the source Gram or prove positivity.
f(-x) in the archimedean part is polynomial continuation. Contacts use
zero extension. Coefficients are ascending powers of the physical x.
"""
from fractions import Fraction
from math import comb, factorial


def rational(ctx, value):
    value = Fraction(value)
    return ctx.mpf(value.numerator)/value.denominator


def add(p, q):
    result = [0]*max(len(p),len(q))
    for i,a in enumerate(p): result[i] += a
    for i,a in enumerate(q): result[i] += a
    return result


def scale(p, a): return [a*x for x in p]


def evaluate(p, x):
    result = 0
    for a in reversed(p): result = result*x+a
    return result


def affine(p, a, b):
    """Coefficients of p(a+b*x), with no numerical interpolation."""
    result = [0]*len(p)
    for m,c in enumerate(p):
        for j in range(m+1): result[j] += c*comb(m,j)*a**(m-j)*b**j
    return result


def regular_action(ctx, f, kernel, T, sigma):
    """Integral [rK(|x-y|)+sigma*rK(x+y)]f(y)dy."""
    degree = len(kernel)-1
    moments = [sum((a*T**(m+j+1)/(m+j+1) for m,a in enumerate(f)),ctx.mpf(0))
               for j in range(degree+1)]
    result = [ctx.mpf(0)]*(len(f)+degree+1)
    for k,c in enumerate(kernel):
        for j in range(k+1):
            factor = (-1)**(k-j)+sigma
            if factor:
                result[k-j] += c*factor*comb(k,j)*moments[j]
        if k%2:
            for m,a in enumerate(f):
                beta = rational(ctx,Fraction(factorial(m)*factorial(k),factorial(m+k+1)))
                result[m+k+1] += 2*c*a*beta
    return result


def arch_source(ctx, f, kernel, T, sigma):
    """Return polynomial, log(x/T), log(1-x/T), log(1+x/T) coefficients."""
    if sigma not in (-1,1): raise ValueError('sigma must be -1 or 1')
    base = scale(f,-ctx.euler-ctx.log(2*ctx.pi*T))
    harmonic = ctx.mpf(0)
    for m,a in enumerate(f):
        if m: harmonic += ctx.mpf(1)/m
        base[m] += harmonic*a
        for j in range(m):
            base[m-1-j] -= a*T**(j+1)/(2*(j+1))
            base[j] -= sigma*a*(-1)**j*T**(m-j)/(2*(m-j))
    base = add(base,scale(regular_action(ctx,f,kernel,T,sigma),-1))
    reflected = [a*(-1)**m for m,a in enumerate(f)]
    return (base,scale(add(scale(reflected,sigma),scale(f,-1)),ctx.mpf(1)/2),
            scale(f,-ctx.mpf(1)/2),scale(reflected,-ctx.mpf(sigma)/2))


def pieces(ctx, f, kernel, sigma):
    """Specialized to T=4/5; interval endpoint ordering is checked."""
    T = ctx.mpf(4)/5
    lengths = [ctx.log(n) for n in (2,3,4)]
    weights = [ctx.log(p)/ctx.sqrt(n) for n,p in ((2,2),(3,3),(4,2))]
    edges = [ctx.mpf(0),T-lengths[0],lengths[1]-T,lengths[2]-T,lengths[0],T]
    # mpmath interval comparisons return True only for separated intervals.
    assert all(a < b for a,b in zip(edges,edges[1:]))
    common = arch_source(ctx,f,kernel,T,sigma)
    result = []
    for a,b in zip(edges,edges[1:]):
        mid = (a+b)/2
        base = list(common[0])
        for length,weight in zip(lengths,weights):
            for offset,slope,factor in ((length,1,1),(-length,1,1),(length,-1,sigma)):
                value = offset+slope*mid
                if value > 0 and value < T:
                    base = add(base,scale(affine(f,offset,slope),-factor*weight))
                elif not (value < 0 or value > T):
                    raise ArithmeticError('Contact activity unresolved at this precision')
        result.append((a,b,(base,*common[1:])))
    return result


def source_value(ctx, source, x, T):
    p,q,r,s = source
    z = x/T
    return (evaluate(p,x)+evaluate(q,x)*ctx.log(z)
            +evaluate(r,x)*ctx.log(1-z)+evaluate(s,x)*ctx.log(1+z))
