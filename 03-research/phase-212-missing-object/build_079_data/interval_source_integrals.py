"""Validated integration of polynomial/log sources, BUILD083 (65)-(66).

The bounds cover smooth-log truncation, coefficients, endpoints and roundoff.
They do not cover replacing A by A_K; that separate cost is in (69).
All input intervals must enclose the intended exact quantities.
"""
from polynomial_source import add, scale, affine, rational
from log_polynomial_moments import moment


def multiply(p,q):
    if not p or not q: return []
    out = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j] += a*b
    return out


def coefficient_bound(p): return sum(abs(a) for a in p)


def smooth_log(ctx, alpha, beta, degree):
    center = alpha+beta/2
    assert center > 0
    ratio = abs(beta)/(2*center)
    assert ratio < 1
    v = [-beta/(2*center),beta/center]
    power = [ctx.mpf(1)]
    poly = [ctx.log(center)]
    for j in range(1,degree+1):
        power = multiply(power,v)
        poly = add(poly,scale(power,ctx.mpf((-1)**(j+1))/j))
    error = ratio**(degree+1)/((degree+1)*(1-ratio))
    return poly,error


def local_source(ctx, source, a, b, T, degree, first=False, last=False, log_cache=None):
    """Return (three local polynomials, L2 error, L2 norm upper, length).

    first/last assert the exact endpoints a=0 / b=T, respectively. They
    must come from the known partition, not approximate endpoint equality.
    """
    length = b-a
    assert length > 0
    p,q,r,s = [affine(poly,a,length) for poly in source]
    out = [p,[],[]]
    error = ctx.mpf(0)
    for slot,(coeff,alpha,beta,singular) in enumerate((
            (q,a/T,length/T,1 if first else 0),
            (r,1-a/T,-length/T,2 if last else 0),
            (s,1+a/T,length/T,0))):
        if all(c == 0 for c in coeff): continue
        if singular:
            out[0] = add(out[0],scale(coeff,ctx.log(length/T)))
            out[singular] = add(out[singular],coeff)
        else:
            key = (id(ctx),slot,degree,ctx.dps)
            if log_cache is None:
                poly,remainder = smooth_log(ctx,alpha,beta,degree)
            else:
                previous = log_cache.get(key)
                if previous is None or not (previous[0] == alpha and previous[1] == beta):
                    poly,remainder = smooth_log(ctx,alpha,beta,degree)
                    log_cache[key] = (alpha,beta,poly,remainder)
                else:
                    _,_,poly,remainder = previous
            out[0] = add(out[0],multiply(coeff,poly))
            error += remainder*coefficient_bound(coeff)
    root = ctx.sqrt(length)
    norm = root*(coefficient_bound(out[0])+ctx.sqrt(2)*(
        coefficient_bound(out[1])+coefficient_bound(out[2])))
    return out,root*error,norm,length


class Integrator:
    def __init__(self,ctx):
        self.ctx = ctx
        self.precision = ctx.dps
        self.cache = {}

    def logarithmic_moment(self,n,a,b):
        assert self.ctx.dps == self.precision
        key = (n,a,b)
        if key not in self.cache:
            u,v = moment(n,a,b)
            self.cache[key] = rational(self.ctx,u)+rational(self.ctx,v)*self.ctx.pi**2
        return self.cache[key]

    def inner(self, f, g):
        """Interval enclosing exact physical-piece pairing of source functions."""
        F,eF,nF,length = f
        G,eG,nG,other_length = g
        assert length == other_length
        powers = ((0,0),(1,0),(0,1))
        value = self.ctx.mpf(0)
        for p,(a,b) in zip(F,powers):
            for q,(c,d) in zip(G,powers):
                product = multiply(p,q)
                value += sum((v*self.logarithmic_moment(n,a+c,b+d)
                              for n,v in enumerate(product)),self.ctx.mpf(0))
        error = eF*nG+eG*nF+eF*eG
        return length*value+self.ctx.mpf([-1,1])*error


def source_inner(ctx, pieces_f, pieces_g, T, degree=160):
    """Integrate over a shared exact partition of the full interval (0,T).

    Matching endpoint intervals must represent the same exact endpoints,
    as provided by polynomial_source.pieces, not independent unknowns.
    """
    assert len(pieces_f) == len(pieces_g)
    assert pieces_f and pieces_f[0][0] == 0 and pieces_f[-1][1] == T
    assert all(left[1] == right[0] for left,right in zip(pieces_f,pieces_f[1:]))
    integrator = Integrator(ctx)
    result = ctx.mpf(0)
    for i,((a,b,F),(aa,bb,G)) in enumerate(zip(pieces_f,pieces_g)):
        assert a == aa and b == bb
        options = dict(first=(i==0),last=(i==len(pieces_f)-1))
        f = local_source(ctx,F,a,b,T,degree,**options)
        g = local_source(ctx,G,a,b,T,degree,**options)
        result += integrator.inner(f,g)
    return result
