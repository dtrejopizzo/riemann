"""Exact finite check of a CM-profile example; no analytic or GRH assumptions."""
import json
from itertools import product
from pathlib import Path
G=list(product(range(2),range(12)))
S={0,1,4,6}; T={0,1,3,7}
def add(x,y):return ((x[0]+y[0])%2,(x[1]+y[1])%12)
def phi(A,x):return int(x[0]==int(x[1] in A))
def count(A,shifts):return sum(all(phi(A,add(x,h)) for h in shifts) for x in G)
def autocorr(A):return [sum(i in A and (i+h)%12 in A for i in range(12)) for h in range(12)]
pair_equal=all(count(S,[(0,0),g])==count(T,[(0,0),g]) for g in G)
triple_equal=all(count(S,[(0,0),g,h])==count(T,[(0,0),g,h]) for g in G for h in G)
translates_equal=any(all(phi(S,add(x,g))==phi(T,x) for x in G) for g in G)
quad=[(0,i) for i in range(4)]
result={'group':'C2 x C12','S':sorted(S),'T':sorted(T),'autocorrelation_S':autocorr(S),'autocorrelation_T':autocorr(T),'all_24_pair_counts_equal':pair_equal,'all_576_triple_counts_equal':triple_equal,'G_translation_equivalent':translates_equal,'four_point_shifts':quad,'four_point_counts':[count(S,quad),count(T,quad)],'normalization_denominator':24}
result['tensor_hodge_numbers_p_0_to_4'] = [[sum(sum(phi(A,add(x,h)) for h in quad)==p for x in G) for p in range(5)] for A in (S,T)]
assert result['tensor_hodge_numbers_p_0_to_4'][0] == [2,4,12,4,2]
assert result['tensor_hodge_numbers_p_0_to_4'][1] == [1,8,6,8,1]
assert pair_equal and triple_equal and not translates_equal
assert result['four_point_counts']==[2,1]
print(json.dumps(result,ensure_ascii=False,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
