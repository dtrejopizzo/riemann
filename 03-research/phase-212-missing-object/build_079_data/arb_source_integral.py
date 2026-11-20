"""Validated scalar integration of the archived real source using Arb.

Same formulas (65),(66),(71),(76); native ball polynomial arithmetic.
This evaluates one source norm, not the residual sign matrix.
"""
import gzip
import json
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import flint
from flint import arb,arb_poly,ctx

FOLDER = Path(__file__).parent


def from_endpoints(endpoints):
    lo,hi = endpoints
    for sign,mantissa,exponent,bits in endpoints:
        assert sign in (0,1) and mantissa >= 0 and bits == mantissa.bit_length()
        assert bits <= ctx.prec  # Endpoint balls below are exact, not rounded.
    exponent = min(lo[2],hi[2])
    L = (-1)**lo[0]*lo[1]*2**(lo[2]-exponent)
    H = (-1)**hi[0]*hi[1]*2**(hi[2]-exponent)
    assert L <= H
    ball = arb((L+H,exponent-1),(H-L,exponent-1))
    assert ball.contains(arb((L,exponent)))
    assert ball.contains(arb((H,exponent)))
    return ball


def load_source(path):
    record = json.loads(gzip.decompress(Path(path).read_bytes()))
    assert record['pieces']
    assert all(left[1] == right[0] for left,right in zip(record['pieces'],record['pieces'][1:]))
    source = [(from_endpoints(a),from_endpoints(b),
               [arb_poly([from_endpoints(x) for x in p]) for p in s])
              for a,b,s in record['pieces']]
    return record,source


def smooth_log(alpha,beta,degree):
    center = alpha+beta/2
    assert center > 0
    ratio = (abs(beta)/(2*center)).upper()
    assert ratio < 1
    v = arb_poly([-beta/(2*center),beta/center])
    power = arb_poly([1])
    result = arb_poly([center.log()])
    for j in range(1,degree+1):
        power *= v
        result += power*(arb((-1)**(j+1))/j)
    error = (ratio**(degree+1)/((degree+1)*(1-ratio))).upper()
    return result,error


def coeff_bound(p): return sum((a.abs_upper() for a in p.coeffs()),arb(0)).upper()


def prepare(source,a,b,T,degree,first,last):
    length = b-a
    assert length > 0
    change = arb_poly([a,length])
    p,q,r,s = [poly(change) for poly in source]
    out = [p,arb_poly(),arb_poly()]
    error = arb(0)
    for multiplier,alpha,beta,singular in (
            (q,a/T,length/T,1 if first else 0),
            (r,1-a/T,-length/T,2 if last else 0),
            (s,1+a/T,length/T,0)):
        if len(multiplier) == 0: continue
        if singular:
            out[0] += multiplier*(length/T).log()
            out[singular] += multiplier
        else:
            approximation,remainder = smooth_log(alpha,beta,degree)
            out[0] += multiplier*approximation
            error += remainder*coeff_bound(multiplier)
    return out,(length.sqrt()*error).upper(),length


class Moments:
    def __init__(self):
        self.H = [arb(0)]
        self.H2 = [arb(0)]
        self.zeta2 = arb.pi()**2/6
        self.precision = ctx.prec
        self.cache = {}

    def get(self,n,a,b):
        assert ctx.prec == self.precision
        key = (n,a,b)
        if key in self.cache: return self.cache[key]
        k = n+1
        while len(self.H) <= k:
            j = len(self.H)
            self.H.append(self.H[-1]+arb(1)/j)
            self.H2.append(self.H2[-1]+arb(1)/(j*j))
        h,h2 = self.H[k],self.H2[k]
        if (a,b) == (0,0): value = arb(1)/k
        elif (a,b) == (1,0): value = -arb(1)/(k*k)
        elif (a,b) == (0,1): value = -h/k
        elif (a,b) == (2,0): value = arb(2)/(k**3)
        elif (a,b) == (0,2): value = (h*h+h2)/k
        elif (a,b) == (1,1): value = h/(k*k)+(h2-self.zeta2)/k
        else: raise ValueError('Unsupported logarithmic powers')
        self.cache[key] = value
        return value


def approximate_inner(F,G,moments):
    powers = ((0,0),(1,0),(0,1))
    result = arb(0)
    for f,(a,b) in zip(F,powers):
        for g,(c,d) in zip(G,powers):
            product = f*g
            result += sum((v*moments.get(n,a+c,b+d) for n,v in enumerate(product.coeffs())),arb(0))
    return result


def norm_squared(source,T,degree=512,verbose=False):
    """Input must represent a known exact partition of (0,T).

    Coinciding endpoint enclosures stand for the same exact endpoint. This
    comes from the source generator and archive provenance, not contains(T).
    """
    assert source[0][0] == 0 and source[-1][1].contains(T)
    moments = Moments()
    total = arb(0)
    records = []
    for i,(a,b,s) in enumerate(source):
        local,error,length = prepare(s,a,b,T,degree,i==0,i==len(source)-1)
        approximate = length*approximate_inner(local,local,moments)
        assert approximate.upper() >= 0
        norm = approximate.upper().sqrt().upper()
        budget = (2*error*norm+error*error).upper()
        enclosed = approximate+arb(0,budget)
        total += enclosed
        records.append(dict(piece=i,approximate=str(approximate),L2_error_bound=str(error),
                            integral_error_bound=str(budget),enclosure=str(enclosed)))
        if verbose: print('Piece',i,'radius',enclosed.rad().str(8),flush=True)
    return total,records


def check_known():
    T = arb(4)/5
    one = arb_poly([1]);zero = arb_poly()
    sources = [([zero,one,zero,zero],2*T),
               ([zero,zero,zero,one],T*(2*arb(2).log()**2-4*arb(2).log()+2))]
    for source,expected in sources:
        actual,_ = norm_squared([(arb(0),T,source)],T,degree=96)
        assert actual.overlaps(expected)
        assert actual.rad() < arb('1e-40')


def main():
    ctx.dps = 500
    check_known()
    path = FOLDER/'real_source_even_0.json.gz'
    previous = json.loads((FOLDER/'real_source_check.json').read_text())
    assert sha256(path.read_bytes()).hexdigest() == previous['artifact_sha256']
    meta,source = load_source(path)
    start = perf_counter()
    result,pieces = norm_squared(source,arb(4)/5,degree=512,verbose=True)
    report = dict(status='ENCLOSED',scope='one real A384 U source norm; no sign matrix certificate',
                  flint_version=flint.__version__,decimal_digits=ctx.dps,smooth_log_degree=512,
                  kernel_degree=meta['kernel_degree'],column=meta['column_index'],
                  source_sha256=sha256(path.read_bytes()).hexdigest(),enclosure=str(result),
                  radius=str(result.rad()),seconds=perf_counter()-start,pieces=pieces)
    (FOLDER/'real_source_integral.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='pieces'},indent=2))


if __name__ == '__main__':
    main()
