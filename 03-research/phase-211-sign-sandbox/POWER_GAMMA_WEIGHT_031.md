# POWER_GAMMA_WEIGHT_031 — Variación real y presupuesto inicial

Estado: PROVED; revisión independiente APROBADA en POWER_WEIGHTED_AUDIT_031.md. Tasa FIJA u=63/2, todos N>=2. No resultado de signo total W. Papers intactos.

## Corpus y diferencia

Consultados ROUTES-TRIED-INDEX (residuos abiertos, primitivas, Möbius), grid maestro R162_2300_MASTER_GRID y CROSSWORD-TO-D (identidades finitas/monotonía), el corpus026/025 y las construcciones INTERIOR_SCALE030 y GAMMA_BALANCE030. La inversión aritmética y las primitivas no son nuevas. Frente al bloque finito030, aquí se controla la VARIACIÓN TOTAL del factor gamma real y se reduce el costo adverso de su rama creciente a M2=u²/(2N−3), conservando en el complemento la primitiva aritmética firmada completa. No se supone positividad global de esa primitiva: WEIGHTED_BLOCK031 la refuta después del contacto3.

## 1. Definiciones y resultado

Sea d=N−1, rho(t)=e^(-ut)P_N(t), q=−rho'/rho y

    R(t)=rho(t)−(2/3)rho'(t)=rho(t)(1+2q(t)/3).

Con D_N=33P_N−P_N', se tiene R=e^(-ut)D_N/(3/2). Por025, D_N es estrictamente logcóncavo. Hay un único máximo T_N>0 de R, y

    T_N <= (2/3)d/(d+20) < 2/3     (d>=2),
    T_2=1/33,
    0<R(T_N)−1 <= 2M2/9.                              (PEAK)

En particular la variación positiva es R(T_N)−1, la negativa es R(T_N), y TV(R)<=1+4M2/9. Son cotas sobre la función gamma REAL para todo N, no una hipótesis sobre pesos genéricos.

Con H e I_* completos definidos abajo, la forma total satisface la desigualdad concreta

    W[g_N]/||g_N||²
      >= int_(T_N)^infty I_*(e^t)[−R'(t)]dt − M2.       (BUDGET)

El peso −R' de esta integral es POSITIVO. Ningún valor absoluto reemplaza I_* en el complemento. El término omitido se acota unilateralmente, no se declara favorable.

## 2. Unicidad y localización del máximo

LC025 implica (logR)'=D_N'/D_N−u estrictamente decreciente. Su valor inicial es positivo, porque D_N'(0)/D_N(0)=63(d+10)/(2d−1)>u; al infinito tiende a −u. Esto prueba unicidad.

Reutilice JEN026, f(z)=(d−z)/(2d−z−1), L=D_N'/D_N:

    L<=63(1+10/d) f(tL),       tL<d, d>=2.

En t0=(2/3)d/(d+20), se tiene exactamente

    u=63(1+10/d)f(ut0),       ut0<d.

Si L(t0)>u, la monotonía estricta de f contradice JEN. Luego T_N<=t0. Para d1, D_N=3/2+33ut y el máximo se calcula directamente: T_2=1/33.

## 3. Concavidad de q y mejora del sobrepaso

Por RIC/CURV026,

    q'=q²+2dq/t−u²,  0<q'<M2,
    q=u−d/t+O(t^-2).

Además q''<0 para todo t>0. En efecto, en cualquier cero de q'' la derivada de RIC da

    q'(q+d/t)=dq/t²,
    q'''=2(q')²−4dq'/t²+4dq/t³
         =2(q')²+4qq'/t >0.

Pero q''=−2d/t³+O(t^-4)<0 al infinito. Un valor no negativo anterior exigiría un cruce descendente posterior, imposible por la desigualdad estricta en todos los ceros. Esto también excluye tangencias. La extensión q(0)=0 es continua.

Ponga c=2/3 y T=T_N. En la rama creciente R'=rho(cq'−q−cq²)>0 y R>=R(0)=1. Explícitamente, R'=c rho q'−qR<=c q'−q, pues rho<=1, q'>0 y q>0. Por tanto

    R(T)−1 <= c q(T)−int_0^T q(t)dt.

La concavidad de q y q(0)=0 dan int_0^T q>=Tq(T)/2. Luego

    R(T)−1 <=q(T)(c−T/2)
            <=M2*T(c−T/2)<=M2*c²/2=2M2/9,

pues T<c. Aquí se utiliza la forma gamma, no sólo la localización del máximo.

## 4. Integración global y costo inicial explícito

JOINT-G030 establece la identidad absolutamente convergente

    W[g_N]/||g_N||²=int_1^infty G_N(x)H(x)dx,
    G_N(x)=(3/2)x^(-1/2)R(logx),
    H(x)=1+[log((x+1)/(x−1))+c0−1−2Psi_1(x)]/x²,
    c0=−gamma−log(4pi), Psi_1(x)=sum_(q<=x)q Lambda(q).

Defina I_*(X)=int_1^X (3/2)x^(-1/2)H(x)dx. Entonces

    W[g_N]/||g_N||²=−int_0^infty I_*(e^t)R'(t)dt.      (IBP)

No hay término de borde: I_*(1)=0, e I_*(X)=O(sqrt(X)(1+logX)), mientras R(logX)=O_N(X^-u(logX)^d). La singularidad en1 es integrable; las derivadas de la primitiva son localmente integrables y sus valores en contactos no afectan la identidad.

La rama creciente tiene e^t<e^(2/3)<2, por lo que NO contiene contactos primos. Puesto que c0−1<0, para 1<=X<2

    I_*(X) <=(3/2)int_1^2 [1+log((x+1)/(x−1))]dx
             =(3/2)[1+3log3−2log2]<9/2.

La última comparación usa log3<11/10 y log2>2/3. Por tanto

    −int_0^T I_*(e^t)R'(t)dt
      >=−(9/2)[R(T)−1]>=−M2.

Esto prueba BUDGET para la forma TOTAL, sin truncar el peine y sin estimar absolutamente el complemento.

Equivalentemente, con la probabilidad real

    dnu_N(t)=[−R'(t)]1_(t>=T)dt/R(T),

se tiene W/||g_N||² >= R(T) E_nu[I_*(e^t)]−M2. Un criterio suficiente CONCRETO es E_nu[I_*]>M2/R(T). Este criterio no está probado; su peso queda completamente especificado por el kernel gamma real.

## 5. Alcance y límite

La unicidad deriva del LC025 ya conocido; la contribución cuantitativa es PEAK mejorado y BUDGET, de orden O(1/N), para la rama anterior a cualquier contacto primo. No se deduce W de la positividad de K, de un bloque finito o de masas de variación. La primitiva I_* tiene valores negativos reales después de3 según WEIGHTED_BLOCK031, por lo que la integral positiva en medida nu sigue necesitando una desigualdad ARITMÉTICA FIRMADA. El bloque favorable030/031 y el costo inicial pequeño no controlan por sí solos ese complemento. No se afirma nueva región W ni cierre para N>=6 a tasa fija.
