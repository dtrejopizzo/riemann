import re,json,pathlib,difflib
root=pathlib.Path('.')
mp=json.load(open('03-research/phase-215-certificacion-privada-grh-rh-con-suplementos/evidencia/mapa_numeros_theta.json'))
texts={str(n):next(root.glob(f'04-papers/{n}-*/main.tex')).read_text() for n in (46,49,53,54,55,56)}
def arg(s,i,op='{',cl='}'):
 while s[i].isspace():i+=1
 assert s[i]==op,(s[i:i+30],op)
 j=i+1;d=1
 while d:
  if s[j]==op:d+=1
  if s[j]==cl:d-=1
  j+=1
 return s[i+1:j-1],j
def norm(s):
 s=re.sub(r'\\label\{[^}]+\}','',s)
 return re.sub(r'\s+',' ',s).strip()
mp['56']={}
s=texts['56'];sec=count=0
for m in re.finditer(r'\\section\{|\\begin\{(theorem|proposition|lemma|corollary|definition|problem|remark)\}',s):
 if m[0].startswith('\\section'):sec+=1;count=0;continue
 count+=1
 part=s[m.end():s.index('\\end{'+m[1]+'}',m.end())]
 lab=re.search(r'\\label\{([^}]+)\}',part)
 mp['56'][f'{sec}.{count}']=dict(label=lab[1] if lab else '',line=s.count('\n',0,m.start())+1,type=m[1])
rows=[]
for dest in ('55','56'):
 s=texts[dest]
 for m in re.finditer(r'\\begin\{(quotedthm|quoteddef)\}',s):
  env=m[1];head,i=arg(s,m.end());title,i=arg(s,i);end=s.index('\\end{'+env+'}',i);body=s[i:end].strip()
  ref=re.search(r'\\cite\[[^\]]*?~([\d.]+)\]\{P(\d+)\}',head);assert ref,head
  num,src=ref[1],ref[2];info=mp[src][num];t=texts[src];offset=sum(len(x) for x in t.splitlines(True)[:info['line']-1]);beg=re.search(r'\\begin\{([^}]+)\}',t[offset:]);j=offset+beg.end();env2=beg[1]
  while t[j].isspace():j+=1
  if t[j]=='[':_,j=arg(t,j,'[',']')
  sb=t[j:t.index('\\end{'+env2+'}',j)].strip()
  row=dict(dest=dest,line=s.count('\n',0,m.start())+1,source=src,number=num,label=info['label'],source_line=info['line'],equal=norm(body)==norm(sb),quote=body,original=sb)
  rows.append(row)
json.dump(rows,open('03-research/phase-215-certificacion-privada-grh-rh-con-suplementos/evidencia/uniones_selmer_hodge.json','w'),indent=2,ensure_ascii=False)
for i,r in enumerate(rows):
 print(i,r['dest'],r['line'],r['source'],r['number'],r['label'],r['equal'])
 if not r['equal']:
  print('\n'.join(difflib.unified_diff(norm(r['original']).split(' '),norm(r['quote']).split(' '),n=3)))
