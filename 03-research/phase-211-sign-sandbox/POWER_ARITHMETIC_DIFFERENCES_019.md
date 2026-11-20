# POWER_ARITHMETIC_DIFFERENCES_019 — Una frontera firmada del peine completo

Estado: **PROVED** lema de una sola transición para toda la columna k=1; **PROVED** signo positivo del peine para 1<=N<=211,u>=63/2. Signo completo de la tabla **OPEN**. Papers intactos.

## 1. Antecedentes y diferencia precisa

Leídos las reglas del proyecto, STATE018, TABLE_DESCENT018, CONE001§4 (theta positiva no implica las desigualdades de cocientes), TATE_CHAIN009§§2–4 y LOW_TABLE018. Consultados el índice de rutas (residuos Euler/Möbius, Λ*1=log y momentos), el grid maestro (entradas Bernstein y POWER017/018) y CROSSWORD-TO-D.md (uso lineal de Λ*1=log, error aritmético firmado). No se atribuye signo a una identidad de Euler, a una medida abstracta de momentos ni a la positividad de la fila inicial.

La diferencia es una propiedad exacta de la autocorrelación de TODA una columna de los átomos reales F_(N,k)(s)=s^k/(s+u)^(N+k): el kernel que pesa Λ en k=1 tiene una sola frontera de signo, localizada analíticamente en O(sqrt(N)). Esto permite sumar TODO el peine con signo en una región explícita de N variables, sin certificados separados de W para filas4,5,... y sin omitir el polar de la obligación final. Los polinomios Bessel inversos y Descartes son herramientas clásicas; el resultado específico es la frontera y la consecuencia firmada para estos contactos.

## 2. Normalización y kernel

Sea u>0, g_M(y)=y^(M−1)e^(−uy)/(M−1)! para y>0, y C_M(t)=c_(g_M)(t). Su densidad de Fourier es (u²+tau²)^(-M). Para t>=0, x=ut y d=M−1,

    C_M(t)=e^(−x) p_d(x)/[2^(d+1)u^(2d+1)d!],
    p_d(x)=sum_(j=0)^d (2d−j)! x^j/[2^(d−j)(d−j)!j!].             (C)

Integrar g_M(y)g_M(y+t) da (C) directamente. Para f_(N,1), la densidad es tau²/(u²+tau²)^(N+1), por lo cual

    c_(f_(N,1))(t)=−C_(N+1)''(t).                              (D)

La derivación es legítima incluso N=1: la densidad multiplicada por tau² sigue siendo integrable. Aquí no se deriva una función causal en el borde.

## 3. Una sola transición de signo para TODO N

**Teorema.** Para cada N>=1 existe exactamente un chi_N>0 tal que c_(f_(N,1))(t)>0 si 0<=ut<chi_N, se anula en chi_N, y es negativa para ut>chi_N. La raíz es simple. Además

    chi_1=1, chi_2=(1+sqrt(5))/2,
    sqrt(2N−3)<chi_N<(1+sqrt(8N−11))/2       (N>=3).             (B)

Prueba. Escriba a_j=[x^j]p_N(x)>0 y r_N=p_N−2p_N'+p_N''. Para N>=2 el cociente de coeficientes se simplifica exactamente a

    [x^j]r_N / a_j = [j(j+1)−2N]/[(2N−j)(2N−j−1)] .           (COEF)

El denominador es positivo para 0<=j<=N,N>=2. El numerador crece estrictamente con j, es negativo en j=0 y positivo en j=N. Ignorando eventuales coeficientes nulos, hay exactamente un cambio de signo. Descartes da como máximo una raíz positiva contando multiplicidad; r_N(0)<0 y su coeficiente principal es positivo, así que existe una y es simple. Por (D) los signos son los declarados. Para N=1, r_1=x−1.

Las identidades polinomiales clásicas, verificables coeficiente a coeficiente, son

    (e^(−x)p_d(x))'=−x e^(−x)p_(d−1)(x),
    p_d=(2d−1)p_(d−1)+x²p_(d−2)              (d>=2).            (R)

También p_j(x)>x p_(j−1)(x) para j>=1,x>=0. En efecto, para 1<=l<=j el cociente entre [x^l]p_j y [x^(l−1)]p_(j−1) es (2j−l)/l>=1; el término constante de p_j es positivo. Para j>=2 los otros coeficientes salvo el principal son estrictos.

Derivar la primera identidad de (R) da r_N=x²p_(N−2)−p_(N−1) para N>=2. Para N=2 se obtiene x²−x−1. Para N>=3, en la raíz,

    chi_N² = p_(N−1)(chi_N)/p_(N−2)(chi_N)
            = 2N−3 + chi_N² p_(N−3)(chi_N)/p_(N−2)(chi_N).

Todos los polinomios son positivos; el último sumando pertenece estrictamente a (0,chi_N), por la desigualdad anterior. Resolver las dos desigualdades prueba (B). QED.

## 4. Consecuencia firmada para la aritmética REAL

Defina exclusivamente la contribución del peine

    P_(N,k)(u)=−2 sum_(q>=2) Λ(q)q^(−1/2)c_(f_(N,k))(log q).

Todas las series convergen absolutamente para u>1/2: la autocorrelación es e^(−ut) por un polinomio finito y Λ(q)<=log q. No es necesario truncar, reemplazar ni modificar Λ.

**Corolario.** Para TODOS 1<=N<=211 y u>=63/2,

    P_(N,1)(u)>0.                                             (ARITH)

En efecto log2>2/3 implica u log q>=u log2>21. Para 3<=N<=211, 21²−21−(2N−3)>=1>0, de modo que la raíz superior de (B) es menor que21. Los casos N1,2 son explícitos y también menores que21. Por tanto C_(N+1)''(log q)>0 en TODOS los contactos q>=2 y c_(f_(N,1))(log q)<0. Cada sumando no nulo del peine es positivo; q=2 asegura estrictitud.

Más generalmente, para CUALQUIER N, el tramo q>exp(chi_N/u) del peine tiene sumandos positivos; los contactos con log q<chi_N/u tienen sumandos negativos. La frontera única es exacta, no una cota de error absoluto.

## 5. Qué inferencia sobre diferencias queda falsificada

El peine aislado NO aporta siempre las diferencias positivas buscadas. En k=0, C_N(t)>0 para TODOS t>=0 por (C), y por tanto

    P_(N,0)(u)<0                 (N>=1,u>1/2).                 (NEG)

La misma identidad complementaria que vale para W vale para P porque sólo utiliza las densidades racionales:

    P_(N,k)=P_(N,k+1)+u²P_(N+1,k).

Así para todo r>=0,

    (−Delta)^r P_(1,0)(u)=u^(2r) P_(r+1,0)(u)<0.              (FD)

Esto falsifica explícitamente el lema concreto «la positividad Λ>=0 hace no negativas las diferencias completas de la contribución aritmética a la fila1». Se usa la Λ real y su suma completa, no una medida abstracta ni una constante arquimediana desplazada. En particular, para N<=211 el peine cambia de signo entre k0 y k1. No se afirma que (FD) falsifique las diferencias de la fila COMPLETA: sus contribuciones arquimediana y polar son esenciales.

## 6. Alcance y obligación restante

ARITH es una desigualdad nueva firmada de una columna, válida simultáneamente para211 órdenes y todas las tasas declaradas; la frontera única vale para TODOS órdenes. No prueba W_(N,1)>=0 para esos órdenes y no borra el polar. Tampoco proporciona las diferencias completas de TODO orden. Para la obligación global falta una desigualdad que conserve la cancelación de ARCH, peine y polar a órdenes variables. Ni el generador de la fila1 ni esta frontera aportan por sí solos ese paso.

Verificación exacta auxiliar: tools/power_arithmetic_differences_019_verify.py comprueba las identidades polinomiales, los extremos y el umbral211; las pruebas simbólicas anteriores cubren todos los N sin depender de un barrido.
