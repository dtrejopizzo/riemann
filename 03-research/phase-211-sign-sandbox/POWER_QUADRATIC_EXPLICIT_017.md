# POWER_QUADRATIC_EXPLICIT_017 — Cono cuadrático explícito, todos N>=2, para P=1

Estado: PROVED, revisado por root, mapa y signo; véanse POWER_INTERIOR_AUDIT_017 §9 y POWER_QUADRATIC_EXPLICIT_AUDIT_017. Extensión separada: no modifica el teorema auditado POWER_QUADRATIC_017 ni ningún paper.

## Antecedentes y razón nueva

Se mantienen las consultas de corpus/índice/grid/crucigrama documentadas en QUADRATIC017. Ese memo prueba un cono cuadrático con un umbral N0(c) conservador porque desplaza la densidad espectral solo a Im z=1. La diferencia aquí es utilizar una banda MÁS ANCHA, Im z=15<u/2, y dividir la integral de modo que se conserve su normalización. Así el coste del peine es pequeño y se obtiene un cono EXPLÍCITO desde N=2, sin suponer uniformidad de las normas temporales falsificadas016. No se cambia el numerador P=1 ni se extrapola a todos los numeradores.

## 1. Teorema

Para u=63/2, N>=2 y k entero con k>=10000N², sea f de transformada F(s)=s^k/(s+u)^(N+k). Entonces

    |c_f(t)|/||f||² <5 exp(−15|t|), para todo t real,     (CORR15)
    W[f]>(49/50)||f||².                                  (CONE)

Todos los contactos están incluidos. La constante10000 no pretende ser óptima.

## 2. Densidad desplazada y división correcta de regiones

Use rho(z)=z^(2k)/(u²+z²)^(N+k), I=∫rho(x)dx, eta=15, y=sqrt(x²+eta²), T=u²/(y²+u²), M=N+k. Como en017,

    |rho(x+i eta)|=rho(y)(1−aT²)^(-M/2),
    a=4eta²/u²=400/441.

Divida ahora en |x|>=eta y |x|<=eta. En la región principal y>=sqrt(2)eta y dx/dy<=sqrt(2)<2. Esta división es importante: utilizar y>=2eta en la región principal daría una cota demasiado tosca para la región pequeña al emplear solo u²−eta² como denominador.

Se tiene k>=100N, por lo que M/k<=101/100. La desigualdad −log(1−z)<=z/(1−z) prueba

    (1−aT²)^(-M/2)<=exp(5kT²),

porque aM/[2k(1−a)]<=202/41<5.

## 3. Parte principal: dos usos distintos de la desigualdad logarítmica

Bajo la densidad real rho/I, T~Beta(b,a0), con b=N−1/2 y a0=k+1/2. En T<=32N/k,

    exp(5kT²)<=exp(5120N²/k)<=exp(64/125)<=125/61.

La última cota usa exp(x)<=1/(1−x) para0<x<1.

Para la cola T>32N/k no se utiliza exp(5kT): se conserva una desigualdad mejor de la expresión ORIGINAL. Por convexidad de −log(1−z),

    −log(1−aT²)<=−a log(1−T²)<=−a log(1−T).

Como aM/2<=202k/441<k/2,

    (1−aT²)^(-M/2)<=(1−T)^(-k/2).

El nuevo parámetro beta es a'=k/2+1/2. Por las mismas desigualdades gamma/Jensen que en017,

    B(a',b)/B(a0,b)<=exp(N²/k)2^N.

Markov con el momento entero N da

    P_(a',b)(T>32N/k)
      <=(k/(32N))^N(2N/(k/2))^N=(1/8)^N.

El producto de ambas cotas es menor que

    exp(1/10000)(1/4)^N
      <=[10000/9999]/16=625/9999.

Por tanto la contribución principal a la integral desplazada normalizada es menor que2(125/61+625/9999).

## 4. Región pequeña: su normalización conserva la ganancia exponencial

En |x|<=eta, |x+i eta|²<=2eta² y |u²+(x+i eta)²|>=u²−eta². Usando la cota beta inferior BL de017,

    ∫_(|x|<=eta)|rho(x+i eta)|dx/I
      <=(2eta/u) A^N r^k(2k/N)^(N−1/2)exp(2N),
    A=u²/(u²−eta²)=441/341<2,
    r=2eta²/(u²−eta²)=200/341<3/5.

Ponga t=k/N>=100. La función t/4−log(2t) es creciente desde100, y log200<6, logA<1. Así

    logA+log(2t)+2<t/4,

de donde todos los factores salvo r^k y2eta/u están acotados por exp(k/4). Además log(5/3)>1/2 por el primer término estricto de su serie atanh; por tanto r^k<exp(−k/2). Como2eta/u=20/21<1, la contribución pequeña es <exp(−k/4)<1/100. Las comparaciones exp6>200 y exp5>100, usadas aquí, se verifican con sumas finitas positivas de sus series; no hay aproximaciones numéricas.

Sumar las dos regiones da

    ∫|rho(x+15i)|dx/I
      <1/100+2(125/61+625/9999)<5.

Desplazar el contorno dentro de |Im z|<u, como en017, prueba CORR15. No se separan los factores de rho en dos normas temporales.

## 5. Peine, ARCH y polar con márgenes explícitos

CORR15 y Lambda(q)<=q implican

    |Comb[f]|/||f||²
      <10Σ(q>=2)q^-14
      <=10·2^-14(1+2/13)<1/1000.                         (PR)

Se reemplazó q^-14.5 por q^-14 para simplificar. Todos los contactos permanecen en la suma.

La ley beta y el lower global m(tau)>=log(|tau|/(2pi))−4, auditado en017, dan

    Arch[f]/||f||²
      >=log[u/(2pi) sqrt(k/N)]−4−1/(2k).

Como pi<4, sqrt(k/N)>100 y u·100/8>3^5>exp5, el logaritmo es >5. Además1/(2k)<1/100. Luego

    Arch[f]/||f||²>99/100.                              (AR)

El bound polar de017 vale sin cambios para k>=4N:

    |Polar[f]|/||f||²<400^-k<1/1000.                     (PO)

Combinar AR, PR y PO da W[f]/||f||²>99/100−2/1000>49/50, como se afirmó.

## 6. Alcance

CONE prueba signo en una región conjunta EXPLÍCITA de dimensión y orden, desde N=2, para el numerador P=1. Mejora el umbral de017 mediante la amplitud de la banda analítica y conserva la suma aritmética infinita. No implica el mismo cono para TODOS P de grado<N; allí faltaría controlar conjuntamente el factor polinomial complejo y su Gram de normalización. Tampoco prueba el segmento k<10000N² ni transforma positividad de la cola en positividad de toda la mezcla geométrica.
