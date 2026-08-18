"""W1: high-precision criticality sweep (RESUME.md item c-NEW).

Run:
    python3 W1_hp_run.py <STEPS> <REFS> <DPS> <OUTTAG>
e.g.
    python3 W1_hp_run.py "2,3;3,4" "8,16,32,64" "30,50" main

Writes W1_hp_<OUTTAG>.json incrementally (one entry appended per
step/refine/dps triple, so a killed/backgrounded run leaves partial,
still-valid results) and logs progress to stdout (redirect to
W1_hp_<OUTTAG>.log).

Every run also executes route2 (thm:newdRegularizedStep's C_eps) at the
same eps ladder, for the independent cross-check.
"""
import sys, json, time
import mpmath as mp
import W1_hp_threshold as HT

EPS_LADDER = [mp.mpf(10) ** -e for e in (6, 9, 12)]


def run(steps, refs, dpss, outtag):
    path = f"W1_hp_{outtag}.json"
    try:
        with open(path) as f:
            out = json.load(f)
    except FileNotFoundError:
        out = []

    done = {(r['q_old'], r['q_new'], r['refine'], r['dps']) for r in out}

    for (qo, qn) in steps:
        for refine in refs:
            for dps in dpss:
                key = (qo, qn, refine, dps)
                if key in done:
                    print(f"skip (already done) {key}")
                    continue
                mp.mp.dps = dps + 20
                t0 = time.time()
                try:
                    bk = HT.threshold_blocks_mp(qo, qn, refine=refine)
                    t_assemble = time.time() - t0

                    t1 = time.time()
                    r1 = HT.route1_direct(bk, rtol_A0=mp.mpf('1e-11'), eps_list=EPS_LADDER)
                    t_route1 = time.time() - t1

                    t2 = time.time()
                    r2 = HT.route2_regularized(bk, eps_list=EPS_LADDER)
                    t_route2 = time.time() - t2
                except Exception as e:
                    print(f"{qo},{qn} refine={refine} dps={dps} FAILED: {e}")
                    sys.stdout.flush()
                    continue

                row = dict(
                    q_old=qo, q_new=qn, refine=refine, dps=dps,
                    cells=bk['cells'], dimC=bk['dimC'], dimA=bk['dimA'], dimP=bk['dimP'],
                    lam_min_norm_cutoff=mp.nstr(r1['lam_min_norm_cutoff'], dps + 5),
                    lam_min_norm_eps={mp.nstr(e, 4): mp.nstr(v, dps + 5)
                                       for e, v in r1['lam_min_norm_eps'].items()},
                    minA0=mp.nstr(r1['minA0'], dps + 5),
                    maxA0=mp.nstr(r1['maxA0'], dps + 5),
                    minSE=mp.nstr(r1['minSE'], dps + 5),
                    rankSE=r1['rankSE'],
                    lam_min_Ceps={mp.nstr(e, 4): mp.nstr(v, dps + 5)
                                   for e, v in r2['lam_min_Ceps'].items()},
                    minR0=mp.nstr(r2['minR0'], dps + 5),
                    minD0=mp.nstr(r2['minD0'], dps + 5),
                    t_assemble=t_assemble, t_route1=t_route1, t_route2=t_route2,
                    t_total=time.time() - t0,
                )
                out.append(row)
                with open(path, 'w') as f:
                    json.dump(out, f, indent=1)

                print(f"{qo},{qn} refine={refine:4d} dps={dps:3d} cells={bk['cells']:5d} "
                      f"dimC={bk['dimC']:4d} dimA={bk['dimA']:4d} "
                      f"lam_cut={row['lam_min_norm_cutoff']} minA0={row['minA0']} "
                      f"lam_Ceps(eps=1e-12)={row['lam_min_Ceps'].get('1.0e-12','?')} "
                      f"({row['t_total']:.1f}s)")
                sys.stdout.flush()
    print("done")


def parse_steps(s):
    out = []
    for part in s.split(';'):
        a, b = part.split(',')
        out.append((int(a), int(b)))
    return out


if __name__ == '__main__':
    steps = parse_steps(sys.argv[1])
    refs = [int(x) for x in sys.argv[2].split(',')]
    dpss = [int(x) for x in sys.argv[3].split(',')]
    outtag = sys.argv[4]
    run(steps, refs, dpss, outtag)
