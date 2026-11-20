# Dilataciones primas: signo negativo de la parte finita ciclotómica

Estado: **PROVED**, con revisión independiente de la prueba y de su alcance. No decide el signo de la forma completa.

## Cotejo

1. Antecedente: Parte V del índice maestro, «Corte ciclotómico dependiente del índice», posterior a 212-94. Allí se obtiene la parte finita homogénea J_sc, se certifica su positividad en b_6 y se deja abierto su signo general. «Selección de agregación por dilataciones» había quedado sin regla para los cruces.
2. Objeto nuevo: un test entero explícito que suma dilataciones primas de b_6 y tiene J_sc negativo. No se aumenta una tabla de matrices ni se busca otra representación de la forma objetivo.
3. Diferencia: para primos distintos mayores que el soporte de b_6, el mcd de los índices dilatados se calcula exactamente. Esto proporciona el término cruzado dominante con signo, que faltaba en la selección anterior. La puerta independiente aprobó investigar sólo esta obstrucción auxiliar.
4. Enlace con el objetivo: se decide si J_sc puede ser una pieza PSD en la separación a=J_sc+(a−J_sc). Un valor negativo descarta esa separación en dos piezas PSD, pero no descarta a≥0 ni una compensación conjunta distinta. No se reclama novedad de las herramientas elementales sobre primos o mcd.

## Definiciones y enunciado

Para sucesiones reales de soporte finito, usar la forma bilineal simétrica

    B(b,c)=−Σ_(i,j≥1) gcd(i,j)b_i c_j log((i+j)/gcd(i,j)),
    J_sc(b)=B(b,b).

El portador entero K consta de las sucesiones enteras de soporte finito que cumplen

    Σ_j b_j=0,    Σ_j j b_j=0,    Σ_j b_j v_r(j)=0 para cada primo r.

Sea b=b_6=(−1,3,−1,−2,0,1), con índices 1,...,6. Para un entero p positivo, D_p b coloca b_i en el índice pi y cero en los restantes. Para cualquier entero k≥4096, definir

    X=2^k,    P_X={p primo: sqrt(X)<p≤X},    N=|P_X|,
    β_X=Σ_(p∈P_X) D_p b.

**Enunciado.** β_X es un elemento no nulo de K y J_sc(β_X)<0. Por tanto J_sc no es PSD sobre el portador entero.

## 1. Datos del test y conservación de las restricciones

Para b, la suma y el momento son cero. Las únicas filas primas no vacías son

    Σ_i b_i v_2(i)=3−4+1=0,
    Σ_i b_i v_3(i)=−1+1=0.

La identidad v_r(pi)=v_r(p)+v_r(i) muestra que cada D_p b y su suma pertenecen a K. Si p,q>6 son primos distintos y 1≤i,j≤6, pi=qj es imposible: obligaría a p|j. Sus soportes son disjuntos; en particular β_X no es nulo cuando N>0.

Por cálculo finito exacto, ya registrado para este mismo b,

    A=Σ_(i,j=1)^6 gcd(i,j)b_i b_j=14,
    J_sc(b)=−72log2+36log3+10log5−2log7<3.

Para la última cota basta la desigualdad entera

    3^36·5^10 < 2^75·7²,

que da J_sc(b)<log8<3. No se usa el certificado intervalar anterior. Además Σ_i|b_i|=8, de modo que

    H=Σ_(i,j=1)^6 gcd(i,j)|b_i b_j|≤6·8²=384.

La homogeneidad exacta da B(D_p b,D_p b)=pJ_sc(b)<3p.

## 2. Cruces completos entre primos distintos

Sean p≥q>6 primos distintos. Como ninguno divide los índices i,j≤6,

    gcd(pi,qj)=gcd(i,j)=g.

Luego, sin omitir ningún cruce,

    B(D_p b,D_q b)
      =−A log p−Σ_(i,j=1)^6 g b_i b_j log((i+(q/p)j)/g).

Se tiene 1≤(i+(q/p)j)/g≤12. Por tanto

    |B(D_p b,D_q b)+14log p|≤H log12<1152.

Aquí log12<3, pues la suma de los primeros cuatro términos de exp(3) es 13. Para p,q∈P_X, log p>(log X)/2. Si k≥4096, log X=klog2>(2/3)k>2304, y así

    B(D_p b,D_q b)<−(13/2)log X.                 (CRUCE)

La cota es uniforme en todos los pares usados. No requiere que p/q esté separado de cero.

## 3. Cantidad suficiente de primos, sin teorema asintótico

Para X=2^k, el coeficiente central satisface

    binom(X,X/2)≥2^X/(X+1).

Para cada primo p≤X, la fórmula de valuación factorial expresa su valuación en ese binomial como suma de floor(X/p^a)−2floor(X/(2p^a)). Cada sumando es 0 o 1 y desaparece para p^a>X. En consecuencia,

    v_p(binom(X,X/2))log p≤log X,
    π(X)log X≥Xlog2−log(X+1).

Como π(sqrt X)≤sqrt X,

    Nlog X≥Xlog2−log(X+1)−sqrt X log X.

Para k≥16, k+1≤2^k/16 y k≤2^(k/2)/16. Ambas se comprueban en k=16 y se conservan al incrementar k. Usando log2<1, se obtiene

    log(X+1)≤k+1≤X/16,
    sqrt X log X≤2^(k/2)k≤X/16.

La cota elemental log2>2/3 (por ejemplo, integrar el desarrollo de 1/(1−t²) entre 0 y 1/3) implica

    Nlog X>(2/3−1/8)X>X/2,
    N>X/(2log X).                                (CUENTA)

En particular N>0. Todo el conteo es elemental y efectivo.

## 4. Signo negativo

Expandir la forma cuadrática, con dos veces cada par no ordenado. Las diagonales y (CRUCE) dan

    J_sc(β_X)<3XN−(13/2)log X·N(N−1).

Por (CUENTA), el miembro derecho es menor que

    N[−X/4+(13/2)log X].

Este número es negativo, porque 2^k>26k>26log X para k≥4096. Esto prueba el enunciado sobre tests finitos explícitamente definidos. No se necesita enumerar sus primos ni calcular una matriz de tamaño creciente.

## Resultado

**Qué se probó:** la parte finita J_sc del regularizador ciclotómico homogéneo tiene valores negativos en el portador entero, pese al valor positivo conocido en b_6. La familia β_X conserva exactamente todas las restricciones de valuaciones y los dos momentos.

**Qué falló y por qué:** sustraer la autoenergía positiva del regularizador no conserva PSD. Las dilataciones individuales escalan su energía por p, mientras que los cruces entre muchas escalas primas acumulan un término negativo de orden N² log X. El resultado excluye tomar J_sc como una pieza no negativa universal en a=J_sc+(a−J_sc).

**Siguiente paso concreto:** cualquier reapertura ciclotómica debe especificar una compensación conjunta con el resto que responda a esta familia de tests; no basta el corte homogéneo ni su positividad en un test. No se propone aquí tal compensación. No se afirma negatividad de a, ni signo del resto, ni imposibilidad de otros regularizadores, ni cierre de la positividad global. La batería de falsificadores de una prueba positiva de a no se aplica a esta refutación de una forma auxiliar: no se ha dado ese paso de signo.
