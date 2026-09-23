import math
from q2_tscan import parity_spec, tip
from track2_needle import LOG3
K=160
print("T      b*-log3        lam(b*)        even(log3)       odd(log3)")
for T in (0.700,0.702,0.704,0.706,0.708,0.710,0.712,0.714,0.716):
    bst,lst=tip(T,K,LOG3-2e-3,LOG3+2e-3)
    e,o=parity_spec(T,K,LOG3)
    print(f"{T:.3f}  {bst-LOG3:+.4e}  {lst: .6e}  {e: .6e}  {o: .6e}")
