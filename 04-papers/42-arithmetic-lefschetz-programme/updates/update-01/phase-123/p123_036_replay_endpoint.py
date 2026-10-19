#!/usr/bin/env python3
"""Replay the original endpoint scripts; retain logs and exact input hashes.
Run with the isolated Python containing python-flint and numpy.
Exit status records execution only; inspect enclosures before claiming Tier 2.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
import subprocess
import sys
import threading

base=Path(__file__).resolve().parent
repo=base.parents[1]
source=repo/'04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2'
out=base/'endpoint_replay_20260905'
out.mkdir(exist_ok=True)
report_path=out/'report.json'
if report_path.exists():
    raise SystemExit('Existing replay report: inspect the live handle/report before creating another run.')
manifest=json.loads((source/'114_d_85_log2_full_space_manifest.json').read_text())
for name,want in manifest['sha256'].items():
    assert hashlib.sha256((source/name).read_bytes()).hexdigest()==want,name
jobs=[
 ('even_gap','114_d_84_log2_degree23_projected_gap_arb_verify.py',{'D84_DEG':'9','D84_HIGH_GAP':'1'}),
 ('odd_gap','114_d_84_log2_degree23_projected_gap_arb_verify.py',{'D84_DEG':'9','D84_ODD_GAP':'1'}),
 ('vector1','114_d_85_fixed_vector_analytic_verify.py',{}),
 ('vector2','114_d_85_fixed_vector_analytic_verify.py',{'D85_VECTOR':'2'}),
 ('vector_odd','114_d_85_fixed_vector_analytic_verify.py',{'D85_VECTOR':'odd'}),
 ('generic_bounds','114_d_85_fixed_vector_analytic_verify.py',{'D85_GENERIC_BOUNDS':'1'}),
 ('capacity','114_d_85_capacity_arb_prototype.py',{}),
 ('recombination','114_d_85_two_level_endpoint_budget_verify.py',{}),
]
now=lambda:datetime.now(timezone.utc).isoformat()
report={'started':now(),'python':sys.version,'executable':sys.executable,
 'packages':{n:importlib.metadata.version(n) for n in ['python-flint','numpy']},
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source.glob('*.py')},
 'scope':'Original endpoint replay; not global D; outputs require enclosure review',
 'jobs':{n:{'script':s,'environment':e,'status':'pending'} for n,s,e in jobs}}
lock=threading.Lock()
def persist():
    temporary=out/'report.tmp'
    temporary.write_text(json.dumps(report,indent=2)+'\n')
    temporary.replace(report_path)
persist()

def run(job):
    name,script,extra=job
    env={k:v for k,v in os.environ.items() if not k.startswith(('D84_','D85_')) and k!='PYTHONPATH'}
    env.update(extra)
    env.update({'PYTHONUNBUFFERED':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
    with (out/(name+'.log')).open('w') as log:
        child=subprocess.Popen([sys.executable,str(source/script)],cwd=source,env=env,stdout=log,stderr=subprocess.STDOUT)
        with lock:
            report['jobs'][name].update(status='running',pid=child.pid,started=now())
            persist()
        print('START',name,'pid',child.pid,flush=True)
        code=child.wait()
    with lock:
        report['jobs'][name].update(status='exited',returncode=code,finished=now())
        persist()
    print('EXIT',name,'code',code,flush=True)
    return code

with ThreadPoolExecutor(max_workers=2) as pool:
    codes=list(pool.map(run,jobs))
report['finished']=now()
report['all_exit_zero']=all(c==0 for c in codes)
persist()
print('REPLAY FINISHED; all exit zero:',report['all_exit_zero'],flush=True)
sys.exit(0 if report['all_exit_zero'] else 1)
