import math
from r153_q1_xi_a import run
A_LIST=[0.1,0.3,0.45,0.49]
for ref in (32,64,128,256):
    run(math.log(2), ref, A_LIST, "log2")
