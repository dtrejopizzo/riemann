"""Run the remaining fixed reproduction stages sequentially; stop on failure."""
from pathlib import Path
import subprocess, sys, os, json, time
import numpy as np
root=Path(__file__).resolve().parent
os.chdir(root)
assert 'EXPORTED_FULL_SAFE_MATRIX 400 256' in Path('even-safe-root.log').read_text()
with np.load('scratch/log11_even_K400_safe_base_arb_256.npz',allow_pickle=False) as d:
    assert int(d['R'])==400 and int(d['N'])==500 and int(d['precision'])==256
    assert str(d['parity'])=='+' and str(d['cache_prefix'])=='log11'
    assert d['S'].shape==(400,400) and d['Rcov'].shape==(400,400)
commands=[]
for tag,parity in [('even','+'),('odd','-')]:
    common=['computations/generate_log10_endpoint_contract_cache.py','256']
    if tag=='odd':
        commands.append((tag+'-safe',common+['400','500',parity,'--endpoint','11','--export-full-safe-matrix']))
    commands.append((tag+'-graph',common+['280','500',parity,'--endpoint','11','--export-verified-graph']))
    commands.append((tag+'-contract',['computations/extract_log10_even_K400_full_contract_base.py','--cache-prefix','log11','--precision','256','--n500-clean']+(['--odd'] if tag=='odd' else [])))
    commands.append((tag+'-family',common+['400','500',parity,'--endpoint','11','--export-yukawa-family','500','850']))
    commands.append((tag+'-checker',['computations/log10_even_K400_sharp_safe_arb.py','--full400','--clean-no-yukawa']+(['--odd'] if tag=='odd' else [])+['--family',f'scratch/log11_{tag}_K400_N500_yukawa_500_850_parseval_arb_256.npz','350','--qf','8000','--cache-prefix','log11','256','11','1']))
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for name,args in commands:
    log=root/(name+'-root.log')
    if log.exists():raise RuntimeError('Refusing to overwrite '+str(log))
    state={'stage':name,'status':'running','command':[sys.executable]+args,'started':time.time()}
    Path('reproduction-state.json').write_text(json.dumps(state,indent=2))
    print('START',name,flush=True)
    with log.open('w') as stream:
        result=subprocess.run([sys.executable]+args,stdout=stream,stderr=subprocess.STDOUT,env=env)
    state.update(status='finished' if result.returncode==0 else 'failed',exit_code=result.returncode,finished=time.time())
    Path('reproduction-state.json').write_text(json.dumps(state,indent=2))
    print('END',name,result.returncode,flush=True)
    if result.returncode:raise SystemExit(result.returncode)
print('ALL REMAINING STAGES EXIT ZERO; OUTPUT AUDIT STILL REQUIRED',flush=True)
