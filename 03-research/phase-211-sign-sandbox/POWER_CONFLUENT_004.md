# POWER_CONFLUENT_004 — Certificado exacto arquimediano confluente de orden tres

Estado: PROVED, certificado racional ejecutado y revisado independientemente en POWER_AUDIT_004.md§5. Sin barrido numérico. Papers intactos.

Razón nueva: la cota de densidad de POWER_ARCH_TRIPLE_004 perdía .051, pero la restricción a TRES polos permite calcular exactamente la matriz confluente en una base Laguerre. El movimiento de polos investigado por `signo` puede transferir este caso a tasas arbitrarias; no se presupone ese resultado aquí. Antecedentes y restricciones consultados en POWER_BRIDGE_002.

## 1. Matriz exacta

Para u=63/2, tome la base ortonormal en L²(0,infinito)

    phi0=sqrt(2u)e^-uy,
    phi1=sqrt(2u)e^-uy(1−2uy),
    phi2=sqrt(2u)e^-uy(1−4uy+2u²y²).

Si p(u)=[psi((u+1/2)/2)−log pi]/2, el kernel arquimediano entre e^-uy,e^-vy es [p(u)+p(v)]/(u+v). Derivar k veces en u y l veces en v, multiplicando por (-1)^(k+l), da las entradas entre y^k e^-uy y^l e^-vy. Conjugar por los tres polinomios anteriores cancela todas las derivadas de orden >2 y da

    M=[[d,b,c],[b,d,b],[c,b,d]],
    d=psi(16)−log pi,
    b=(63/4)psi'(16),
    c=b+(3969/16)psi''(16).

En general, antes de fijar u, d=2p(u), b=2up'(u), c=2u[p'(u)+up''(u)]. Esto también se comprueba integrando la base racional de Fourier; no se usan datos espectrales externos.

## 2. Cotas racionales suficientes

Se prueban

    d>159/100,  0<b<51/50,  |c|<1/50.                       (R)

Sea H_m=Σ(k=1..m)1/k y

    J_N(r)=2Σ(k=0..N−1) r^(2k+1)/(2k+1),
    E_N(r)=2r^(2N+1)/[(2N+1)(1−r²)].

Para 0<r<1, J_N(r)<log((1+r)/(1−r))<J_N(r)+E_N(r), por la serie geométrica integrada. Con N=24, γ<H256−log256 y pi<22/7 dan

    d > H15−H256+8J24(1/3)−J24(15/29)−E24(15/29) >159/100.

Para las derivadas se usan solamente las series convergentes

    psi'(16)=Σ(k>=16)k^-2,
    psi''(16)=−2Σ(k>=16)k^-3.

Ponga S2=Σ(k=16..255)k^-2, S3=Σ(k=16..255)k^-3. Comparación integral da

    blo=(63/4)(S2+1/256) < b < (63/4)(S2+1/255)=bhi,
    blo−(3969/8)(S3+1/(2·255²)) < c
       < bhi−(3969/8)(S3+1/(2·256²)).

Las cuatro comparaciones de R son puramente racionales y fueron verificadas con Fraction. Se adjunta código exacto abajo. No se redondean funciones especiales.

## 3. Margen probado

La matriz con solo b en las dos aristas de la cadena tiene eigenvalores 0,+sqrt(2)b,−sqrt(2)b; la matriz con c en las esquinas tiene norma |c|. Por tanto

    M >= [d−sqrt(2)b−|c|] I
      > [159/100−(10/7)(51/50)−1/50]I
      > (1/10)I.

Se usó sqrt(2)<10/7. Así la forma ARQUIMEDIANA es coerciva con constante >1/10 sobre span{e^-31.5y,ye^-31.5y,y²e^-31.5y}.

Esto no es todavía la forma completa: el peine y la parte polar deben controlarse, y tasas distintas requieren la prueba de movimiento de polos. En una familia de triples próximos, la base de diferencias divididas converge a esta base confluente en norma de forma, por lo que el margen arquimediano sí persiste en alguna vecindad; no se declara un radio explícito.

## 4. Código de verificación racional

```python
from fractions import Fraction as F
H=lambda n:sum((F(1,k) for k in range(1,n+1)),F())
def J(r):
    return 2*sum((r**(2*k+1)/F(2*k+1) for k in range(24)),F())
def E(r):
    return 2*r**49/(F(49)*(1-r*r))
dlo=H(15)-H(256)+8*J(F(1,3))-J(F(15,29))-E(F(15,29))
S2=sum((F(1,k*k) for k in range(16,256)),F())
S3=sum((F(1,k**3) for k in range(16,256)),F())
blo=F(63,4)*(S2+F(1,256))
bhi=F(63,4)*(S2+F(1,255))
clo=blo-F(3969,8)*(S3+F(1,2*255**2))
chi=bhi-F(3969,8)*(S3+F(1,2*256**2))
assert dlo>F(159,100)
assert 0<blo<bhi<F(51,50)
assert -F(1,50)<clo<chi<F(1,50)
assert F(159,100)-F(10,7)*F(51,50)-F(1,50)>F(1,10)
```
