set -e
cd "$(dirname "$0")"
python3 run_d1000.py log3h_b60 0.5493061443340548 24 1000 60 3 1 60
python3 run_d1000.py log3h_z10  0.5493061443340548 24 10  60 3 1
python3 run_d1000.py log3h_z100 0.5493061443340548 24 100 60 3 1
python3 run_d1000.py w058  0.58 24 1000 60 3 1
python3 run_d1000.py w062  0.62 24 1000 60 3 1
python3 run_d1000.py wlog2 0.6931471805599453 24 1000 60 3 1
for n in log3h log3h_b log3h_b60 log3h_z10 log3h_z100 w058 w062 wlog2; do python3 check.py $n 300 > chk_$n.log 2>&1; echo "checked $n"; done
python3 insight.py log3h_b log3h_b60 w058 w062 wlog2
