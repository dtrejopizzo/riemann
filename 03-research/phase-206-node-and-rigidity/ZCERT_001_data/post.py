# Recalcula tau (version con N(t)<=(t/2pi)log t) y la bandera del nodo en todas las salidas.
import json, ast, math
exec(open('zcert.py').read().split("if __name__")[0])
def ks_of(T,m=1): return list(range(1,m*NT(T)+1,2))
out={}
for line in open('run.log'):
    name,d=line.split(' ',1); d=ast.literal_eval(d); d['tau']=tau(d['T'],ks_of(d['T'],d['mult'])); d['node']=d['cert'] is not None and float(d['cert'])>d['tau']; out[f"{name}|{d['mult']}N"]=d
json.dump(out,open('zcert_results.json','w'),indent=1,ensure_ascii=False)
for f in ['tstar.json','finegrid.json']:
    r=json.load(open(f))
    for d in r: d['tau']=tau(d['T'],ks_of(d['T'])); d['node']=d['cert'] is not None and float(d['cert'])>d['tau']
    json.dump(r,open(f,'w'),indent=1); print(f,[(d['T'],d['N']) for d in r if not d['node']][:8])
for k,d in out.items(): print(k,d['dim'],d['cert'],'%.2e'%d['tau'],d['node'])
