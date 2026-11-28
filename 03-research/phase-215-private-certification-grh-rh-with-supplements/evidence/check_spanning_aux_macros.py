from pathlib import Path
import json,re
here=Path(__file__).parent
exec(here.joinpath('compare_theta_quotes.py').read_text().split('items=[]')[0])
for n in ['52']:
 sources[n]=next(Path('04-papers').glob(n+'-*/main.tex')).read_text()
rows=json.loads(here.joinpath('junctions_spanning_copies.json').read_text());items=[]
for row in rows:
 src,dest=row['source'],row['dest'];ss=sources[src];s=sources[dest]
 idx=sum(len(x)+1 for x in ss.splitlines()[:row['source_line']-1]);b=re.search(r'\\begin\{'+row['type']+r'\}',ss[idx:]);a=idx+b.end();origin=striphead(ss[a:ss.index('\\end{'+row['type']+'}',a)])
 idx=sum(len(x)+1 for x in s.splitlines()[:row['dest_line']-1]);m=re.search(r'\\begin\{(quoteddef|quotedthm)\}',s[idx:]);i=idx+m.end();_,i=group(s,i);_,i=group(s,i);quote=s[i:s.index('\\end{'+m[1]+'}',i)].strip()
 items.append(dict(**row,src=int(src),source_body=origin,quoted_body=quote))
macrocode=here.joinpath('compare_theta_macros.py').read_text();exec(macrocode[macrocode.index('def defs('):macrocode.index('items=json.loads')])
diffs=[]
for k,x in enumerate(items):
 src,dest=str(x['src']),str(x['dest']);used=set(re.findall(r'\\[A-Za-z]+',x['source_body']+' '+x['quoted_body']));todo=list(used)
 while todo:
  v=todo.pop()
  for n in [src,dest]:
   if v in D[n]:
    for w in re.findall(r'\\[A-Za-z]+',D[n][v][1]):
     if w not in used:used.add(w);todo.append(w)
 for v in used:
  a,b=D[src].get(v),D[dest].get(v)
  if a!=b and (a is not None or b is not None):diffs.append(dict(row=k,macro=v,source=a,target=b))
refcode=here.joinpath('check_theta_refs.py').read_text();A={}
for p in (here/'aux-collation').glob('*/main.aux'):A[int(p.parent.name)]={m[1]:m[2] for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',p.read_text())}
exec(refcode[refcode.index('def remove_tags'):refcode.index('bad=[]')])
bad=[]
for k,x in enumerate(items):
 a,b=refs(x['source_body'],x['src']),refs(x['quoted_body'],int(x['dest']));x['references_source']=a;x['references_quote']=b;x['references_equal']=a==b
 if a!=b:bad.append(dict(row=k,label=x['label'],source=a,target=b))
(here/'collation_51_spanning_macros.json').write_text(json.dumps(diffs,indent=2))
(here/'collation_51_spanning_refs.json').write_text(json.dumps(items,indent=2,ensure_ascii=False))
print('rows',len(items),'macro mismatches',len(diffs),'ref mismatches',len(bad))
for x in bad:print(x)
