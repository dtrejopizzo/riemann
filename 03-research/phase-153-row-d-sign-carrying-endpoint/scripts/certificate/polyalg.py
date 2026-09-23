"""Polynomial algebra over an mpmath context (mp or iv). Coeff lists ascending."""
def pmul(a,b,ctx):
    out=[ctx.mpf(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b): out[i+j]=out[i+j]+x*y
    return out
def padd(a,b,ctx):
    n=max(len(a),len(b)); out=[ctx.mpf(0)]*n
    for i,x in enumerate(a): out[i]=out[i]+x
    for i,y in enumerate(b): out[i]=out[i]+y
    return out
def pscal(a,c,ctx): return [x*c for x in a]
def pder(a,ctx): return [a[i]*i for i in range(1,len(a))] or [ctx.mpf(0)]
def pint(a,ctx):
    out=[ctx.mpf(0)]
    for i,x in enumerate(a): out.append(x/(i+1))
    return out
def peval(a,x,ctx):
    s=ctx.mpf(0)
    for c in reversed(a): s=s*x+c
    return s
def binom(n,k,ctx):
    r=ctx.mpf(1)
    for i in range(k): r=r*(n-i)/(i+1)
    return r
