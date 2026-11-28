"""Inventario reproducible; las coincidencias textuales NO prueban teoremas."""
from pathlib import Path
import re, json, hashlib

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
numbers = [43,44,45,46,49,50,51,52,53,54,55,56,57,58]
manifest, statements, citations = [], {}, []
envs = r"theorem|proposition|lemma|corollary|definition|remark"
pattern = re.compile(r"\\begin\{(" + envs + r")\}(.*?)\\end\{\1\}", re.S)
for number in numbers:
    path = next((ROOT / '04-papers').glob(f'{number}-*/main.tex'))
    raw = path.read_bytes(); text = raw.decode()
    manifest.append({'paper':number, 'path':str(path.relative_to(ROOT)),
                     'sha256':hashlib.sha256(raw).hexdigest(), 'lines':len(text.splitlines())})
    for cm in re.finditer(r'\\cite(?:\[([^\]]*)\])?\{([^}]+)\}',text):
        for key in cm.group(2).split(','):
            target=re.fullmatch(r'(?:P|Paper)(43|44|45|46|49|50|51|52|53|54|55|56)',key.strip())
            if target:
                citations.append((number,text.count('\n',0,cm.start())+1,
                                  target.group(1),cm.group(1) or '',key.strip()))
    for m in pattern.finditer(text):
        labels = re.findall(r'\\label\{([^}]+)\}', m.group(2))
        normalized = re.sub(r'(?m)(?<!\\)%.*$', '', m.group(2))
        normalized = re.sub(r'\\label\{[^}]+\}', '', normalized)
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        for label in labels:
            statements.setdefault(label,[]).append({'paper':number,
                'path':str(path.relative_to(ROOT)), 'line':text.count('\n',0,m.start())+1,
                'environment':m.group(1), 'statement':m.group(2).strip(),
                'normalized_sha256':hashlib.sha256(normalized.encode()).hexdigest()})
(OUT/'fuentes.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
# Generic labels are retained: shared labels do not by themselves mean imports.
shared = {k:v for k,v in statements.items() if len({x['paper'] for x in v})>1}
(OUT/'enunciados_compartidos.json').write_text(json.dumps(shared,indent=2,ensure_ascii=False)+'\n')
with (OUT/'uniones_textuales.tsv').open('w') as f:
    f.write('label\tpapers_and_lines\tidentical_after_whitespace_and_label_removal\n')
    for label, items in sorted(shared.items()):
        f.write(label+'\t'+','.join(f"{v['paper']}:{v['line']}" for v in items)+'\t'+
                str(len({v['normalized_sha256'] for v in items})==1)+'\n')
print(f'{len(manifest)} fuentes; {len(shared)} etiquetas compartidas. No es auditoría semántica.')
with (OUT/'citas_internas.tsv').open('w') as f:
    f.write('source\tline\ttarget\tlocator\tbibkey\n')
    for row in citations:
        f.write('\t'.join(str(v).replace('\n',' ') for v in row)+'\n')
print(f'{len(citations)} referencias internas explícitas inventariadas; no incluye claves bibliográficas con otros nombres.')
