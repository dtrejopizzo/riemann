"""Batch source Grams with shared preparations and moment contractions.

Real columns only. Guarantees are those of (71)-(72), applied entrywise.
The returned interval matrix is not asserted positive semidefinite.
"""
from interval_source_integrals import Integrator, local_source


def local_gram(integrator, prepared):
    """Compute C^t M C by applying the moment operator once to each column."""
    c = integrator.ctx
    count = len(prepared)
    assert count
    length = prepared[0][3]
    assert all(p[3] == length for p in prepared)
    sizes = [max(len(p[0][s]) for p in prepared) for s in range(3)]
    rows = [(s,k) for s in range(3) for k in range(sizes[s])]
    powers = ((0,0),(1,0),(0,1))
    columns = [[p[0][s][k] if k < len(p[0][s]) else c.mpf(0)
                for s,k in rows] for p in prepared]
    transformed = []
    for column in columns:
        active = [(i,x) for i,x in enumerate(column) if not x == 0]
        transformed.append([
            sum((x*integrator.logarithmic_moment(k+rows[j][1],
                         powers[s][0]+powers[rows[j][0]][0],
                         powers[s][1]+powers[rows[j][0]][1])
                 for j,x in active),c.mpf(0)) for s,k in rows])
    gram = [[c.mpf(0) for _ in range(count)] for _ in range(count)]
    for i in range(count):
        for j in range(i,count):
            value = sum((x*y for x,y in zip(columns[i],transformed[j])),c.mpf(0))
            gram[i][j] = length*value
            gram[j][i] = gram[i][j]
    norms = []
    for i in range(count):
        upper = gram[i][i].b
        if not upper >= 0:
            raise ArithmeticError('Squared-norm enclosure has negative upper endpoint')
        sharp = c.sqrt(upper).b
        norms.append(min(prepared[i][2].b,sharp))
    for i in range(count):
        for j in range(i,count):
            _,ei,_,_ = prepared[i]
            _,ej,_,_ = prepared[j]
            ni,nj = norms[i],norms[j]
            error = ei*nj+ej*ni+ei*ej
            gram[i][j] += c.mpf([-1,1])*error
            gram[j][i] = gram[i][j]
    return gram


def source_gram(ctx, columns, T, degree=160):
    """Shared exact partition of (0,T); endpoints obey source_inner's contract."""
    assert columns and columns[0]
    reference = columns[0]
    assert reference[0][0] == 0 and reference[-1][1] == T
    assert all(p[1] == q[0] for p,q in zip(reference,reference[1:]))
    for column in columns:
        assert len(column) == len(reference)
        assert all(a == aa and b == bb for (a,b,_),(aa,bb,_) in zip(reference,column))
    c = ctx
    count = len(columns)
    total = [[c.mpf(0) for _ in range(count)] for _ in range(count)]
    integrator = Integrator(c)
    for piece,(a,b,_) in enumerate(reference):
        cache = {}
        prepared = [local_source(c,col[piece][2],a,b,T,degree,
                                 first=(piece==0),last=(piece==len(reference)-1),
                                 log_cache=cache) for col in columns]
        gram = local_gram(integrator,prepared)
        for i in range(count):
            for j in range(count): total[i][j] += gram[i][j]
    return total
