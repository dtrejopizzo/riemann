"""NUMERICAL diagnostic: inertia of the midpoint of S (cert.py) by recursive Schur complements with
approximate solves at the working precision (no error bounds). usage: as cert.py, single mu."""
import sys, runpy
src = open('cert.py').read()
src = src.replace("    piv = pd(S, n)", """    Sm = arb_mat(n, n, [arb(S[a, b].mid()) for a in range(n) for b in range(n)])
    negs = []
    def inert(A, n):
        if n <= 48:
            B = [[A[i, j] for j in range(n)] for i in range(n)]
            out = []
            for k in range(n):
                pk = B[k][k]; out.append(float(pk.mid()))
                for i in range(k + 1, n):
                    f = B[i][k] / pk
                    for j in range(k + 1, i + 1):
                        B[i][j] = arb((B[i][j] - f * B[j][k]).mid()); B[j][i] = B[i][j]
            return out
        h = n // 2
        A11 = sub(A, 0, h, 0, h); B12 = sub(A, 0, h, h, n)
        X = A11.solve(B12, algorithm='approx')
        Sc = sub(A, h, n, h, n) - B12.transpose() * X
        Sc = arb_mat(n - h, n - h, [arb(Sc[a, b].mid()) for a in range(n - h) for b in range(n - h)])
        return inert(A11, h) + inert(Sc, n - h)
    pv = inert(Sm, n)
    neg = [p for p in pv if p < 0]
    print('PIVOTS: n_neg', len(neg), 'neg', sorted(neg)[:5], 'smallest positive', sorted(p for p in pv if p > 0)[:5], flush=True)
    piv = None""")
exec(compile(src, 'cert_inertia', 'exec'))
