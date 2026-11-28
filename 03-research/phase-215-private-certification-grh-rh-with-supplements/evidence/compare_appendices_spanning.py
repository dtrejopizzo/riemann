import json,re,difflib
from pathlib import Path
base=Path('04-papers'); out=Path('03-research/phase-215-private-certification-grh-rh-with-supplements/evidence')
nums=json.loads((out/'number_map_theta.json').read_text())
sources={str(n):next(base.glob(f'{n}-*/main.tex')).read_text() for n in [46,49,51,52]}
# Shared theorem counter, reset by unstarred section; stop before appendix.
s=sources['52'].split('\\appendix')[0]; sec=count=0; nums['52']={}
pat=r'\\section\{|\\begin\{(theorem|proposition|lemma|corollary|definition|problem|remark)\}'
for m in re.finditer(pat,s):
 if m.group(0).startswith('\\section'):sec+=1;count=0;continue
 count+=1;typ=m.group(1);end=s.index('\\end{'+typ+'}',m.end());b=s[m.start():end];lab=re.search(r'\\label\{([^}]+)\}',b)
 nums['52'][f'{sec}.{count}']={'label':lab.group(1) if lab else None,'line':s.count('\n',0,m.start())+1,'type':typ}
def group(s,p):
 assert s[p]=='{'; depth=1;i=p+1
 while depth:
  if s[i]=='{' and s[i-1]!='\\':depth+=1
  if s[i]=='}' and s[i-1]!='\\':depth-=1
  i+=1
 return s[p+1:i-1],i
def norm(s):
 s=re.sub(r'\\label\{[^}]+\}','',s)
 s=re.sub(r'\\(?:eqref|ref)\{[^}]+\}','REF',s)
 s=re.sub(r'\\cite(?:\[[^\]]*\])?\{[^}]+\}','REF',s)
 return re.sub(r'\s+','',s)
rows=[];diff=[]
for dst in ['51','52']:
 s=sources[dst]
 for m in re.finditer(r'\\begin\{(quotedthm|quoteddef)\}',s):
  if m.start()<s.index('\\appendix'):continue
  cite,p=group(s,m.end());title,p=group(s,p);end=s.index('\\end{'+m.group(1)+'}',p);body=s[p:end]
  ref=re.search(r'~([0-9]+\.[0-9]+)\]\{P(\d+)\}',cite)
  if not ref:raise ValueError(cite)
  number,src=ref.groups();meta=nums[src][number];st=sources[src];pos=sum(len(x) for x in st.splitlines(True)[:meta['line']-1]);en=st.index('\\end{'+meta['type']+'}',pos);sbody=st[pos:en];sbody=re.sub(r'^\\begin\{[^}]+\}(?:\[[^\]]*\])?','',sbody)
  row={'dest':dst,'line':s.count('\n',0,m.start())+1,'source':src,'number':number,**meta,'source_line':meta['line'],'dest_line':s.count('\n',0,m.start())+1,'equal_normalized':norm(body)==norm(sbody)}
  rows.append(row)
  if not row['equal_normalized']:
   diff.append(f'\n### {dst}:{row["dest_line"]} <- {src}:{number} {meta["label"]}\n'+''.join(difflib.unified_diff(sbody.splitlines(True),body.splitlines(True),fromfile='source',tofile='quote')))
(out/'junctions_spanning_copies.json').write_text(json.dumps(rows,indent=2));(out/'junctions_spanning_diffs.txt').write_text('\n'.join(diff));(out/'number_map_spanning.json').write_text(json.dumps(nums['52'],indent=2))
print('total',len(rows),'equal',sum(x['equal_normalized'] for x in rows),'diff',len(diff))
