# POWER_FOUR_GLOBAL_009 — Signo uniforme en TODOS los espacios de cuatro polos reales >=63/2

Estado: PROVED, con input racional confluente previamente certificado. La verificación exacta escalar y de constantes está en tools/power_four_global_009_verify.py. Papers intactos.

## 1. Resultado y alcance

Sean v_1,...,v_4>=63/2, permitiendo multiplicidades, y f una función real no nula cuya transformada de Laplace sea P(s)/Π_j(s+v_j), con grado P<4. Entonces la forma completa de la línea satisface

    W[f]>(2/25)||f||².                                    (FOUR)

En particular, para cualesquiera cuatro exponentes a_i>=32 y coeficientes reales c_i, la forma exterior es positiva en rho(X)=Σ_i c_i X^-a_i cuando su imagen no es nula. Los coeficientes de la imagen son c_i zeta(a_i); no hay restricción de separación ni cota superior de tasas. También se incluyen todos los límites confluentes.

El transporte que se prueba NO es monotonía de cocientes arch+polar: esa afirmación general fue falsificada. Se transporta una cota coerciva menor conservando un resto estrictamente positivo, mediante una estimación del sector espectral donde el multiplicador es negativo.

## 2. Corpus y diferencia nueva

Consultados índice ROUTES-TRIED-INDEX, grid, crucigrama y memos POWER_POLE_MOVEMENT_004, POWER_POLAR_MOVEMENT_005, POWER_HIGH_ORDER_PM_NOGO_007, POWER_CONFLUENT_FOUR_005. La monotonía arquimediana, el certificado confluente y la derivada local ya estaban disponibles. La diferencia exacta es una desigualdad GLOBAL para el filtro racional completo, que no exige signo favorable de la derivada polar. No es una nueva parametrización del problema ni una campaña de certificados de tasas.

## 3. Inputs confluentes ya probados

Fije u=63/2. El certificado POWER_CONFLUENT_FOUR_005 y su verificador racional prueban, para todo f0 en el espacio confluente de cuatro polos u,

    AP[f0]:=Arch[f0]+Polar[f0]>(49/200)||f0||².             (BASE)

En esa base Laguerre, los dos vectores de momentos polares tienen normas al cuadrado

    AA=(63/31²)Σ_{j=0}³(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}³(31/32)^{2j}.

Se verifica racionalmente 4AA BB<1. Por Cauchy--Schwarz,

    |Polar[f0]|<||f0||².                                  (PB)

La cota no destruye el polar positivo en BASE; sólo se aplicará a su PEQUEÑA variación relativa bajo el filtro.

## 4. Dos desigualdades escalares del multiplicador

Con c=1/10, se tiene

    m(tau)>=c si tau²>=81,
    tau²(c-m(tau))_+<23 para todo tau.                    (NEG)

Prueba por sumas racionales. Primero m(0)>-11/2. Basta usar gamma<3/5, pi<22/7, log2<7/10 y logpi<23/20; la suma de sus cotas superiores es 759/140<11/2. Estas cotas se verifican elementalmente: gamma<H32-log32<3/5 usando tres términos atanh que dan log2>693/1000; log2<25/36<7/10 por una cola geométrica; y Σ_{k=0}^6(23/20)^k/k!>22/7 implica logpi<23/20.

Para x=tau²>=0, los primeros dieciséis términos de la serie de digamma dan

    m(tau)>ell(x):=-11/2+Σ_{k=0}^{15}x/[a_k(4a_k²+x)],
    a_k=k+1/4.

ell es creciente. Evaluación racional exacta prueba

    ell(4)>-4/3, ell(16)>-3/5, ell(32)>-1/4,
    ell(64)>2/25, ell(81)>1/10.

Así m>=c para x>=81. En los cinco intervalos de extremos 0,4,16,32,64,81, se acota x(c-m)_+ por el extremo derecho multiplicado por c menos la cota inferior en el extremo izquierdo. Resultan las cotas racionales

    112/5, 344/15, 112/5, 112/5, 81/50,

todas menores que 23. Esto demuestra (NEG) sin tablas ni barrido numérico.

## 5. Filtro global y conservación de la coercividad

Para f con tasas v_j>=u, use el MISMO numerador para definir

    F0(s)=P(s)/(s+u)^4, F(s)=H(s)F0(s),
    H(s)=Π_j(s+u)/(s+v_j).

Defina

    R(tau)=|H(i tau)|²,
    R0=R(0)=Π_j u²/v_j²,
    r0=H(-1/2)H(1/2)=Π_j(u²-1/4)/(v_j²-1/4).

Todos son positivos. Para x=tau²,

    1<=R(tau)/R0<= (1+x/u²)^4,
    r0/R0 >=(1-1/(4u²))^4>=1-1/u².                       (FILTER)

La segunda línea usa Bernoulli; además r0<=R0. Ponga

    K=[(1+81/u²)^4-1]/81.

Por convexidad del polinomio, para 0<=x<=81,

    (1+x/u²)^4-1<=Kx.

El cambio exacto de la forma respecto de la cota objetivo c es

    AP[f]-c||f||²
     =R0(AP[f0]-c||f0||²)
       +(1/2pi)∫(R-R0)(m-c)|F0(i tau)|²d tau
       +(r0-R0)Polar[f0].                                 (ID)

No se compara el polar por separado con un signo supuesto. Fuera de tau²<=81, el integrando adicional es no negativo por (NEG) y R>=R0. Dentro, (NEG) y FILTER lo acotan inferiormente por -23KR0||f0||². Por (PB), la variación polar es >=-R0||f0||²/u². Finalmente BASE implica

    AP[f]-c||f||²
      >R0[49/200-c-23K-1/u²]||f0||².

La constante entre corchetes satisface la desigualdad racional exacta

    49/200-1/10-23K-1/u²>3/100>0.                         (MARGIN)

Como R0>0 y f0 no es nula,

    AP[f]>(1/10)||f||²                                    (AP4)

para TODAS las tasas v_j>=u, incluso arbitrariamente grandes. La norma objetivo de f ya aparece en (ID), por lo que no se pierde uniformidad cuando R0 es pequeña.

## 6. Peine completo, uniformemente en las cuatro tasas

La desigualdad ponderada previamente probada por bases all-pass es

    ||exp(uy/2)f||²<=B4||f||², B4=(25^4-1)/12=32552.

No exige cota superior ni separación de los polos. Por Cauchy--Schwarz,

    |c_f(t)|<=sqrt(B4)exp(-ut/2)||f||².

Así, usando sqrt(B4)<181, Lambda(q)<=logq<=q y (u-1)/2>15,

    |Comb[f]|/||f||²
       <=362Σ_{q>=2}q^-15
       <=362/28672 <13/1000.

Combinando con (AP4),

    W[f]>(1/10-13/1000)||f||²
         =(87/1000)||f||²>(2/25)||f||².

Queda probado (FOUR). El peine no se ha truncado: la cota controla la suma infinita completa.

## 7. Qué no se extrapola

La prueba usa cuatro polos tanto en BASE como en el exponente del filtro y B4. Para dimensión creciente, la cota del filtro y el coste del peine cambian y BASE puede fallar sin contribución aritmética positiva (el test de dimensión doce ya la necesita). Por tanto el cierre global de dimensión cuatro no prueba el signo en todos los órdenes ni cierra el paper.
