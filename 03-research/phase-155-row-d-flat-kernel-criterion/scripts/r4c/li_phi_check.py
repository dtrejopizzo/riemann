# R4c: validate the dictionary identity lambda_n = sum_gamma (1 - cos(n*theta(gamma))),
# theta(gamma) = 2*arctan(1/(2*gamma)),  over gamma>0 zeros (the pair gamma,-gamma already
# folded: for each rho=1/2+i|gamma| and its conjugate, 1-(1-1/rho)^n + c.c. = 2(1-cos n theta)).
import math, json
Z=[float(x) for x in open('/home/trabajo/Documentos/research/riemann/06-grafico/zeros_10000.txt')]
G=Z[-1]
def lam(n):
    s=0.0
    for g in Z:
        th=2.0*math.atan(1.0/(2.0*g))
        s+=2.0*(1.0-math.cos(n*th))
    # tail: 2*sum_{gamma>G} (1-cos n theta) ~ n^2 * int_G^inf (log(t/2pi)/2pi)/t^2 dt
    tail=n*n*(math.log(G/(2*math.pi))+1.0)/(2*math.pi*G)
    return s, s+tail
known={1:0.0230957090,2:0.0923457352,3:0.2076389205,4:0.3687904095,5:0.5757790843}
out={}
for n in [1,2,3,4,5,10,50,100,200,500,1000]:
    s,st=lam(n)
    out[n]={"trunc":s,"with_tail":st,"known":known.get(n),"half_n_log_n":0.5*n*math.log(n) if n>1 else None}
    print(n,round(s,7),round(st,7),known.get(n),round(0.5*n*math.log(n),4) if n>1 else '')
json.dump(out,open('/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts/r4c/li_phi_check.json','w'),indent=1)

# asymptotic split: archimedean/pole prediction (n/2)(log n + gamma_E - 1 - log 2pi)
gE=0.5772156649015329
print("\n n | lambda_n(computed) | arch prediction | residue | sqrt(n)log n")
for n in [100,200,500,1000]:
    _,st=lam(n)
    pred=0.5*n*(math.log(n)+gE-1-math.log(2*math.pi))
    print(n, round(st,3), round(pred,3), round(st-pred,3), round(math.sqrt(n)*math.log(n),2))
