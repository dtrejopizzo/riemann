"""Exact finite sanity check of the full odd-support reconstruction lemma."""
import itertools,json
from pathlib import Path
out=[]
for d in (1,2,3):
 n=2**d; size=2*n; seen={}; full=0
 for mask in range(2**n):
  f=[int((x//n)==((mask>>(x%n))&1)) for x in range(size)]
  support=all(sum(f[x]*(-1 if (x&k).bit_count()%2 else 1) for x in range(size))!=0 for k in range(n,size))
  if not support: continue
  full+=1
  translates=[sum(f[x^g]<<x for x in range(size)) for g in range(size)]
  canonical=min(translates)
  signature=tuple((translates[0]&translates[a]&translates[b]&translates[c]).bit_count() for a,b,c in itertools.product(range(size),repeat=3))
  if signature in seen: assert seen[signature]==canonical
  seen[signature]=canonical
 out.append({'G':f'C2^{d+1}','CM_types_checked':2**n,'full_odd_support_types':full,'distinct_four_point_profiles':len(seen),'result':'PASS'})
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
