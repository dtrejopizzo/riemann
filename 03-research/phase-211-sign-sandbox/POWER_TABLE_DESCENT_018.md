# POWER_TABLE_DESCENT_018 — Primeras DOS diferencias estrictamente positivas, en todos los pasos

Estado: PROVED para todos k>=0 y u>=63/2. No demuestra completa monotonía de la fila ni signo de todas las filas. Papers intactos.

## 1. Corpus y razón nueva frente al descenso estructural

Leídos POWER_STATE_017, POWER_DESCENT_016, POWER_INTERIOR_017 §7, POWER_SCALAR_BRIDGE_017 y TATE_CHAIN/PACKET_SCOPE009; consultados índice/grid/crucigrama buscando primeras diferencias, fila N=2 y completa monotonía. La recurrencia exacta y las propiedades eventuales no bastan por sí solas, como muestra W4 de016.

La diferencia nueva es probar DOS niveles de descenso en TODOS los pasos, usando el multiplicador real, dos cotas explícitas de derivadas de digamma, la cota ponderada uniforme de017 y el signo alternado exacto del polar. No se deduce signo de una identidad ni se repite una campaña de certificados de k finitos.

Ponga F_{N,k}(s)=s^k/(s+u)^{N+k}, a_{N,k}=W[f_{N,k}], c_k=binom(2k,k)/4^k. Se demuestra

    W[f_{2,k}]>(1/8)||f_{2,k}||²,
    W[f_{3,k}]>(1/8)||f_{3,k}||², todos k>=0,u>=63/2.     (ROWS23)

Por la recurrencia completa, esto implica desigualdades NUEVAS cuantitativas:

    a_{1,k}-a_{1,k+1}>c_k/[32u(k+1)],
    a_{1,k}-2a_{1,k+1}+a_{1,k+2}
                        >3c_k/[64u(k+1)(k+2)].           (DIFF)

Así la fila de valores sin normalizar a_{1,k} es estrictamente decreciente y estrictamente convexa en TODO k, no sólo eventualmente.

## 2. Recurrencia exacta y normas

Con Q=s/(s+u), L=u/(s+u), la identidad completa016 da

    a_{N,k}=a_{N,k+1}+u²a_{N+1,k}.

Por inducción u^{2(N-1)}a_{N,k}=(-Δ)^{N-1}a_{1,k}. Esta parte sola no impone signo. Las normas exactas beta satisfacen

    ||f_{N,k}||²/||f_{N,0}||²
      =c_k/binom(k+N-1,N-1),
    ||f_{2,k}||²=c_k/[4u³(k+1)],
    ||f_{3,k}||²=3c_k/[8u^5(k+1)(k+2)].

(DIFF) se obtiene de (ROWS23) y estas normas, sin extrapolar una desigualdad entre cocientes normalizados.

## 3. Parte arquimediana: dos cotas de todos los órdenes k

Para cada N,u fijo, el cambio k->k+1 repondera la probabilidad espectral por tau²/(u²+tau²). Covarianza positiva con m demuestra que Arch[f_{N,k}]/||f_{N,k}||² no disminuye con k. Basta entonces acotar k=0.

Sea d(u)=psi((u+1/2)/2)-logpi. Derivar la integral arquimediana de la exponencial, conservando la norma, da

    A_{2,0}=d-u d',
    A_{3,0}=d-u d'+(u²/3)d''.

La serie de polygamma e integración comparativa dan, para x>0,

    psi'(x)<=1/x+1/x²,
    psi''(x)>=-2/x³-1/x².

Con x=(u+1/2)/2, para todo u>=63/2,

    u d'<=1+2/u<=67/63,
    (u²/3)d''>=-1/3-4/(3u)>=-71/189.

Además d aumenta porque psi'>0, y el intervalo racional ya probado en017 verifica d(63/2)>159/100>3/2. Por tanto

    A_{2,k}>=A_{2,0}>3/2-67/63>2/5,
    A_{3,k}>=A_{3,0}>159/100-67/63-71/189
                              =2851/18900>3/20.          (ARCH)

No se utilizó monotonía de AP bajo movimiento de polos, que en general es falsa: la uniformidad en u proviene de estas cotas explícitas de cada componente.

## 4. Control efectivo del peine infinito, uniforme en TODO k

Use WRN de017 con eta=15, a=u-15, rho=(15/a)². Sus constantes para N=2,3 son

    R2=(u/a)^3(1+rho)/(1-rho)²,
    R3=(u/a)^5(1+2rho-rho²/3)/(1-rho)³.

La representación por series de coeficientes positivos de017 muestra que ambas constantes decrecen al aumentar u>=63/2. En u=63/2,

    R2=4641/11, 2sqrt(R2)<42,
    R3=15658881/1331, 2sqrt(R3)<220.

Como ||e^{15y}f||²<=R_N||f||², la misma cota de autocorrelación usada en017 da, para TODOS los k y todos esos u,

    |Comb[f_{2,k}]|/||f_{2,k}||²
       <42Σ_{q>=2}q^-14<=42*15/[13*2^14]<3/1000,
    |Comb[f_{3,k}]|/||f_{3,k}||²
       <220Σ_{q>=2}q^-14<=220*15/[13*2^14]<1/60.         (PRIME)

Se conserva el peine entero con sus coeficientes reales: se usó sólo Lambda(q)<=logq<=q y la cola integral convergente, sin truncamiento ni suposición de que cada contacto ayude.

## 5. El signo alternado del polar permite el segundo descenso

Para cualquier N,k,

    Polar[f_{N,k}]=2(-1/4)^k/(u²-1/4)^{N+k}.

Sea p_{N,0}=Polar[f_{N,0}]/||f_{N,0}||²>0 y q=1/(4u²-1). Las normas beta de§2 dan

    |Polar[f_{N,k}]|/||f_{N,k}||²
      =p_{N,0}q^k binom(k+N-1,N-1)/c_k.

Por c_k>=2^-k y binom(k+N-1,N-1)<=N^k (contar multisets frente a secuencias ordenadas), esto es <=p_{N,0}(2Nq)^k. Los prefactores p_{N,0} y q decrecen con u; para p_{N,0}, la derivada logarítmica tiene numerador -u²-(2N-1)/4<0.

En N=2, p_{2,0}=8u³/(u²-1/4)²<13/50 y 4q<1, luego todo el polar tiene valor absoluto normalizado <13/50.

En N=3 no se desperdicia el signo positivo de k par. Para k impar se tiene k>=1 y 6q<1. En el extremo u=63/2,

    p_{3,0}=32u^5/[3(u²-1/4)^3]<7/20,
    p_{3,0}(6q)<(7/20)*(6/3968)<1/1000.

Así, para TODOS los k, el polar de N=3 es >=-(1/1000)||f||²; para k par es incluso no negativo. Esta conservación de su signo evita la pérdida demasiado grande que daría acotar todo el polar de N=3 por p_{3,0}.

## 6. Cierre y alcance del descenso

De ARCH, PRIME y§5,

    W[f_{2,k}]/||f_{2,k}||²
       >2/5-13/50-3/1000=137/1000>1/8,
    W[f_{3,k}]/||f_{3,k}||²
       >3/20-1/1000-1/60=397/3000>1/8.

Quedan demostrados (ROWS23) y (DIFF). El verificador tools/power_table_descent_018_verify.py comprueba las constantes con Fraction y los intervalos racionales previos; no contiene muestreo en k ni un espectro numérico.

Se obtuvieron sólo los dos primeros niveles de diferencias. No se infiere completa monotonía de a_{1,k}, ni signo de N>=4, ni la tabla completa necesaria en el puente escalar. La información que distingue el multiplicador real del desplazado W4 de016 está explícita en (ARCH) y su balance con PRIME/POLAR. El generador de la fila y la recurrencia siguen siendo identidades; el aporte nuevo es su signo cuantitativo en todos los pasos de estos dos niveles.
