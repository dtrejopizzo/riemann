"""Round 9, A3 addendum: the tail row's budget grows like log(tau1), so tau1 is the free
parameter of Lemma T.  One process, four solves."""
import json
import r9lp
runs = []
for tau1, J, step in [(300.0, 20, 0.04), (300.0, 0, 0.04), (1000.0, 20, 0.05), (3000.0, 20, 0.08)]:
    tag = f"tau1={tau1:.0f}_J={J}"
    print('===', tag, flush=True)
    r = r9lp.run(tag=tag, orders=(0,), J=J, tau1=tau1, step=step, hsep=0.005, iters=6)
    if r: runs.append(r[0])
json.dump(runs, open('r9_tau1.json', 'w'), indent=1)
for d in runs:
    print({k: d[k] for k in ['tag','LP','truemin_grid1e3','Lfloor','tailcost','tail_rhs','tail_slack','col_cost','atom_cost','beta_cost','b0','b1','secs']})
