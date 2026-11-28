from pathlib import Path
import re,json
base=Path('03-research/phase-215-private-certification-grh-rh-with-supplements/evidence');items=json.loads((base/'collation_275_theta.json').read_text());A={}
for p in (base/'aux-collation').glob('*/main.aux'):
 A[int(p.parent.name)]={m[1]:m[2] for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',p.read_text())}
def remove_tags(s):
 for m in list(re.finditer(r'\\tag\*?\{',s))[::-1]:
  i=m.end();d=1
  while d:
   if s[i]=='{':d+=1
   if s[i]=='}':d-=1
   i+=1
  s=s[:m.start()]+s[i:]
 return s
def refs(s,paper):
 out=[]
 s=remove_tags(s)
 for m in re.finditer(r'\\(?:eqref|ref)\{([^}]+)\}|\\cite(?:\[([^\]]*)\])?\{([^}]+)\}',s):
  if m[1]:out.append((paper,A[paper].get(m[1],'MISSING:'+m[1])))
  elif m[3].startswith('P') and m[3][1:].isdigit():
   for num in re.findall(r'(?<![A-Za-z0-9])\d+(?:\.\d+)*',re.sub(r'\\[A-Za-z]+',' ',m[2] or '')):out.append((int(m[3][1:]),num))
  else:out.append(('external',m[0]))
 return out
bad=[]
for k,x in enumerate(items):
 a,b=refs(x['source_body'],x['src']),refs(x['quoted_body'],x['dest'])
 x['references_source']=a;x['references_quote']=b;x['references_equal']=a==b
 if a!=b:bad.append((k,x['label'],x['dest'],x['line'],a,b))
(base/'collation_275_theta.json').write_text(json.dumps(items,indent=2,ensure_ascii=False))
for z in bad:print(z)
print('REFMISMATCHES',len(bad))
