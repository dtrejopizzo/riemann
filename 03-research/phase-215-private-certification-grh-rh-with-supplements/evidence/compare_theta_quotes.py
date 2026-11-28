from pathlib import Path
import re,json,difflib
base=Path('03-research/phase-215-private-certification-grh-rh-with-supplements/evidence'); maps=json.loads((base/'number_map_theta.json').read_text());sources={}
for n in maps:
 sources[n]=next(Path('04-papers').glob(n+'-*/main.tex')).read_text()
def group(s,i,op='{',cl='}'):
 assert s[i]==op
 depth=1;j=i+1
 while depth:
  if s[j]==op and (j==0 or s[j-1]!='\\'):depth+=1
  if s[j]==cl and s[j-1]!='\\':depth-=1
  j+=1
 return s[i+1:j-1],j
def striphead(s):
 s=s.lstrip()
 if s.startswith('['):_,j=group(s,0,'[',']');s=s[j:].lstrip()
 return re.sub(r'^\\label\{[^}]+\}','',s).strip()
def norm(s):
 s=re.sub(r'(?<!\\)%[^\n]*','',s)
 s=re.sub(r'\\label\{[^}]*\}','',s)
 s=re.sub(r'\\(?:eqref|ref)\{[^}]*\}',r' REFERENCE ',s)
 s=re.sub(r'\\cite(?:\[[^\]]*\])?\{[^}]*\}',r' REFERENCE ',s)
 s=re.sub(r'\\tag\*?\{[^\n]*','',s)
 s=s.replace('{REFERENCE}','REFERENCE').replace('{ REFERENCE }','REFERENCE')
 s=re.sub(r'\s+',' ',s).strip()
 return s
items=[]
for n in [49,50,53,54]:
 s=sources[str(n)];off=s.index('\\appendix')
 for m in re.finditer(r'\\begin\{(quotedthm|quoteddef)\}',s[off:]):
  start=off+m.start();i=off+m.end();title,i=group(s,i);subtitle,i=group(s,i)
  cit=re.search(r'\\cite\[(?:Definition|Lemma|Theorem|Proposition|Corollary)~([\d.]+)\]\{P(\d+)\}',title);num,src=cit.groups();d=maps[src][num];body=s[i:s.index('\\end{'+m.group(1)+'}',i)].strip()
  ss=sources[src];idx=sum(len(x)+1 for x in ss.splitlines()[:d['line']-1]);b=re.search(r'\\begin\{'+d['type']+r'\}',ss[idx:]);a=idx+b.end();origin=striphead(ss[a:ss.index('\\end{'+d['type']+'}',a)])
  a1,b1=norm(origin),norm(body)
  item=dict(dest=n,line=s[:start].count('\n')+1,src=int(src),number=num,label=d['label'],source_line=d['line'],identical=a1==b1,source_body=origin,quoted_body=body)
  item['diff']='\n'.join(difflib.unified_diff(a1.split(' '),b1.split(' '),fromfile='source',tofile='quote',n=3))
  items.append(item)
(base/'collation_275_theta.json').write_text(json.dumps(items,indent=2,ensure_ascii=False))
with (base/'collation_275_theta_diffs.txt').open('w') as f:
 for k,x in enumerate(items):
  if not x['identical']:f.write(f"\n==== {k} P{x['src']} {x['number']} {x['label']} -> P{x['dest']}:{x['line']} ====\n"+x['diff']+'\n')
print('Total',len(items),'equal normalized',sum(x['identical'] for x in items),'differences',sum(not x['identical'] for x in items))
print('diff bytes',(base/'collation_275_theta_diffs.txt').stat().st_size)
