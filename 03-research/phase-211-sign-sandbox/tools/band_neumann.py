"""Band Schur complement and Neumann truncations (ROUND_008_A). NUMERICAL."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as g, mpmath as mp

def eig(M):
    E, V = mp.eigsy(M); idx = sorted(range(len(E)), key=lambda i: E[i])
    return [E[i] for i in idx], V[:, idx] if False else mp.matrix([[V[r, i] for i in idx] for r in range(V.rows)])

def sector(D, par, thr):
    Q = g.sector_basis(D, par)
    A = Q.T * D['Arch'] * Q; P = Q.T * D['Pi'] * Q
    al, U = eig(A); Pu = U.T * P * U
    m = len(al); b = [i for i in range(m) if al[i] <= thr]; c = [i for i in range(m) if al[i] > thr]
    sub = lambda R, C: mp.matrix([[Pu[i, j] for j in C] for i in R])
    Pbb, Pcb, Pcc = sub(b, b), sub(c, b), sub(c, c)
    s = [1 / mp.sqrt(al[i]) for i in c]
    X = mp.matrix(len(c), len(c)); Y = mp.matrix(len(c), len(b))
    for i in range(len(c)):
        for j in range(len(c)): X[i, j] = s[i] * Pcc[i, j] * s[j]
        for j in range(len(b)): Y[i, j] = s[i] * Pcb[i, j]
    x, W = eig(X); Z = W.T * Y
    Db = mp.diag([al[i] for i in b])
    return dict(al=al, nb=len(b), tc=al[c[0]], x=x, Z=Z, base=Db - Pbb,
                YY=Y.T * Y, lamsec=eig(A - P)[0][0])

def SK(sec, K):  # K=None -> exact
    nb = sec['nb']; S = sec['base'].copy()
    for j, xj in enumerate(sec['x']):
        gk = 1 / (1 - xj) if K is None else (1 - xj ** (K + 1)) / (1 - xj)
        for a in range(nb):
            for b in range(nb): S[a, b] -= gk * sec['Z'][j, a] * sec['Z'][j, b]
    return S

def lmin(M): return eig(M)[0][0] if M.rows else mp.inf

def run(T, comb=None, label='Lambda', Ks=None, N=90, dps=40, thrmode='plus'):
    D = g.build(T, N, dps, comb=comb, verbose=False)
    with mp.workdps(dps + 20):
        # thresholds: pi_+ (global over both sectors), or ||Pi||
        ext = []
        for par in ('ev', 'odd'):
            Q = g.sector_basis(D, par); e = eig(Q.T * D['Pi'] * Q)[0]; ext += [e[0], e[-1]]
        pip, pim = max(ext), -min(ext)
        thr = pip if thrmode == 'plus' else max(pip, pim)
        out = dict(T=T, label=label, pip=pip, pim=pim)
        for par in ('ev', 'odd'):
            s = sector(D, par, thr)
            ex = lmin(SK(s, None)); r = max(abs(s['x'][0]), abs(s['x'][-1])); rp = max(s['x'][-1], 0); rm = max(-s['x'][0], 0)
            yy = lmin(-s['YY']) * -1  # placeholder
            yyn = eig(s['YY'])[0][-1] if s['nb'] else 0
            rec = dict(nb=s['nb'], tc=s['tc'], r=r, rp=rp, rm=rm, exact=ex, lam=s['lamsec'], YY=yyn, K={})
            Kmax = 400; Ksign = None; Kcert = None; vals = {}
            for K in range(0, Kmax + 1):
                v = lmin(SK(s, K)); vals[K] = v
                eps = max(rp ** (K + 1) / (1 - rp), rm ** (K + 1) / (1 + rm))
                if Kcert is None:
                    if ex > 0 and lmin(SK(s, K) - eps * s['YY']) > 0: Kcert = K
                    if ex < 0 and K % 2 == 1 and v < 0: Kcert = K
                if Kcert is not None and K > Kcert + 2: break
            # Ksign: smallest K with sign(v_K') = sign(ex) for all K' >= K computed
            ks = sorted(vals)
            Ksign = next((k for k in ks if all(mp.sign(vals[q]) == mp.sign(ex) for q in ks if q >= k)), None)
            rec.update(Ksign=Ksign, Kcert=Kcert, Kmax=max(ks), v=vals)
            out[par] = rec
        return out

if __name__ == '__main__':
    T = float(sys.argv[1]); which = sys.argv[2]; mode = sys.argv[3] if len(sys.argv) > 3 else 'plus'
    with mp.workdps(60):
        lam = g.lambda_comb(mp.mpf(T))
        if which == 'Lambda': comb = None
        elif which == '1.01': comb = [(x, mp.mpf('1.01') * v) for x, v in lam]
        elif which == '1.1': comb = [(x, mp.mpf('1.1') * v) for x, v in lam]
        elif which == 'eta': comb = [(x, v + (mp.mpf('0.1') if abs(x - mp.log(2)) < 1e-30 else 0)) for x, v in lam]
    t0 = time.time(); o = run(T, comb, which, thrmode=mode)
    print(f"T={T} {which} mode={mode} pi+={mp.nstr(o['pip'],6)} pi-={mp.nstr(o['pim'],6)} time={time.time()-t0:.0f}s")
    for par in ('ev', 'odd'):
        r = o[par]
        print(f" {par}: nb={r['nb']} tc={mp.nstr(r['tc'],6)} r={mp.nstr(r['r'],6)} r+={mp.nstr(r['rp'],6)} r-={mp.nstr(r['rm'],6)} |Y*Y|={mp.nstr(r['YY'],4)} "
              f"lmin(S)={mp.nstr(r['exact'],8)} lam_sec={mp.nstr(r['lam'],8)} Ksign={r['Ksign']} Kcert={r['Kcert']} Kmax={r['Kmax']}")
        print("   v_K:", ' '.join(f"{k}:{mp.nstr(r['v'][k],3)}" for k in [0,1,2,3,4,5,7,9,11,15,21,31,51,101,201,301,400] if k in r['v']))
