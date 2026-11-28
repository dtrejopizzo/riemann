from pathlib import Path
exec(Path(__file__).with_name('compare_theta_quotes.py').read_text().split('items=[]')[0])
def defs(s):
 out={}
 for m in re.finditer(r'\\(newcommand|renewcommand|providecommand)\*?\s*(?:\{(\\[A-Za-z]+)\}|(\\[A-Za-z]+))',s):
  name=m[2] or m[3];i=m.end();args=[]
  while i<len(s) and s[i].isspace():i+=1
  while i<len(s) and s[i]=='[':
   a,i=group(s,i,'[',']');args.append(a)
   while i<len(s) and s[i].isspace():i+=1
  if i>=len(s) or s[i]!='{':continue
  a,i=group(s,i);val=(args,re.sub(r'\s+',' ',a).strip())
  if m[1]!='providecommand' or name not in out:out[name]=val
 return out
D={n:defs(s) for n,s in sources.items()}
items=json.loads((base/'cotejo_275_theta.json').read_text());diffs={}
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
  if a!=b and (a is not None or b is not None):
   key=(src,dest,v);diffs.setdefault(key,dict(src=src,dest=dest,macro=v,source=a,target=b,rows=[]))['rows'].append(k)
(base/'cotejo_275_theta_macros.json').write_text(json.dumps(list(diffs.values()),indent=2,ensure_ascii=False))
for d in diffs.values():print(d)
print('MACRODIFFS',len(diffs))
