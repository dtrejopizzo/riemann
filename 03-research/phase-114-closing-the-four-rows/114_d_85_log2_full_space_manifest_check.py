#!/usr/bin/env python3
"""Hash/scope checker for the D.85 endpoint manifest."""
import hashlib,json
from pathlib import Path

root=Path(__file__).parent
data=json.loads((root/'114_d_85_log2_full_space_manifest.json').read_text())
assert data['full_space_endpoint'] is True
assert data['global_row_d'] is False
assert data['paper_touched'] is False
assert data['interval_cells']==2000 and data['interval_width']=='0.01'
for name,want in data['sha256'].items():
    got=hashlib.sha256((root/name).read_bytes()).hexdigest()
    assert got==want,(name,got,want)
assert len(data['directed_runs'])==8
print('PASS D.85 manifest hashes and scope flags')
print('full_space_endpoint=true; global_row_d=false; paper_touched=false')
