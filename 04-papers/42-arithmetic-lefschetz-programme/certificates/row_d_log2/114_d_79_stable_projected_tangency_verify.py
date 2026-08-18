#!/usr/bin/env python3
"""Directed projected tangency audit at T=log(2).

This deliberately reuses the audited local-ODE/Legendre implementation of
D.77 and changes only constants, the exact shift mesh, and the global tail
minorant.  It proves a projected lower bound > -1e-7 in each parity.  It is
NOT a full-space positivity certificate: the P--Q Feshbach step is absent.
"""
from pathlib import Path

source_path = Path(__file__).with_name("114_d_77_log3_legendre_arb_verify.py")
s = source_path.read_text()
s = s.replace("DEPTH = 80", "DEPTH = 160")
s = s.replace("T = arb(3).log()/2", "T = arb(2).log()")
s = s.replace(
    "C_PRIME = A/arb(2).sqrt()",
    "C_PRIME=A/arb(2).sqrt()\nC_THREE=arb(3).log()/arb(3).sqrt()",
)
s = s.replace("MB, MM = 28, 20\nNC = 2*MB+MM", "MD,ME=20,8\nNC=4*MD+2*ME")

# Elementary convex-trapezoid tail coefficient:
# sum_{j>=N}(B/b_j)^3 >= B/4+1/2 = 80.625.
s = s.replace(
    'BVALS = [arb(2*j)+arb("0.5") for j in range(DEPTH)]',
    'BTAIL=arb("320.5")\n'
    'CTAIL=arb("80.625")\n'
    'TERMS=[(arb(2*j)+arb("0.5"),arb(1)) for j in range(DEPTH)]'
    '+[(BTAIL,CTAIL)]\nBVALS=[z[0] for z in TERMS]',
)
s = s.replace(
    "sum((2/b for b in BVALS), arb(0))",
    "sum((w*2/b for b,w in TERMS), arb(0))",
)
s = s.replace("for b in BVALS:\n        z = b*h/2", "for b,wgt in TERMS:\n        z = b*h/2")
s = s.replace(
    "plus.append(fp); minus.append(fm)",
    "plus.append([wgt.sqrt()*x for x in fp]); "
    "minus.append([wgt.sqrt()*x for x in fm])",
)
s = s.replace("local[i][j] -= kij", "local[i][j] -= wgt*kij")

# The cancellation-sensitive residual Gram is irrelevant to this projected
# audit; omitting it also prevents this script being mistaken for Feshbach.
a = s.index("    # Exact finite Gram of Q K_local P; trace bounds its operator norm^2.")
b = s.index("\n\ndelta = 2*T-A", a)
s = s[:a] + (
    '    return {"h":h,"plus":plus,"minus":minus,"local":local,'
    '"beta_local_sq":arb(0)}\n'
) + s[b:]

s = s.replace(
    "delta = 2*T-A\nh_boundary = delta/MB\nh_middle = (A-delta)/MM\n"
    'packages = {"b": cell_package(h_boundary), "m": cell_package(h_middle)}',
    "b3=arb(3).log();d=2*A-b3;e=2*b3-3*A\n"
    'packages={"d":cell_package(d/MD),"e":cell_package(e/ME)}',
)
s = s.replace(
    'types = ["b"]*MB+["m"]*MM+["b"]*MB',
    'types=["d"]*MD+["e"]*ME+["d"]*MD+["d"]*MD+["e"]*ME+["d"]*MD',
)
s = s.replace(
    "for i in range(MB):\n    j = MB+MM+i\n    for k in range(D):\n"
    "        mat[i*D+k][j*D+k] -= C_PRIME\n"
    "        mat[j*D+k][i*D+k] -= C_PRIME",
    "starts=[0,MD,MD+ME,2*MD+ME,3*MD+ME,3*MD+2*ME]\n"
    "for si,sj,n,c in [(starts[0],starts[3],MD,C_PRIME),"
    "(starts[1],starts[4],ME,C_PRIME),(starts[2],starts[5],MD,C_PRIME),"
    "(starts[0],starts[5],MD,C_THREE)]:\n"
    "    for u in range(n):\n        i,j=si+u,sj+u\n"
    "        for k in range(D):\n"
    "            mat[i*D+k][j*D+k]-=c;mat[j*D+k][i*D+k]-=c",
)

# Certify only lambda_min > -1e-7, then stop before any high-space claim.
s = s.replace('shift = arb("0.00050")', 'shift = arb("0.00000010")')
s = s.replace(
    'projected_lower[name] = -shift\n    print(f"PASS projected {name}: '
    'lambda_min > -0.00050; preconditioned disk={least}")',
    'projected_lower[name] = -shift\n    print(f"PASS projected {name}: '
    'lambda_min > -1e-7; preconditioned disk={least}")',
)
stop = s.index("# Cross/high residuals for off-cell kernels.")
s = s[:stop] + '\nprint("PASS projected tangency only; Feshbach not claimed")\n'
exec(compile(s, str(source_path) + "::D79", "exec"))
