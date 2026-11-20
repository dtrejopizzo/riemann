# POWER_PRIME_BALANCE_033 — Contracción real y cotas firmadas del peine

Estado: **PROVED; revisión independiente APROBADA en POWER_BALANCE_AUDIT_033.md**: contracción uniforme y brackets aritméticos con resto de signo conocido. No nuevo signo W ni nueva fila. Papers intactos.

## 1. Corpus y diferencia

Consultados ROUTES-TRIED-INDEX (Euler/divisores, transporte Möbius), grid maestro y CROSSWORD-TO-D (Λ*1=log, falta de propagación por dilataciones), y SIGNED_MEAN019, ARITHMETIC_DIFFERENCES019, SIGNED_BALANCE020, CONTACT_BALANCE021, CONTACT_DECISION032. La inversión de Euler por serie de Neumann es clásica y no se presenta como nueva. Tampoco se infiere signo de una identidad.

La diferencia específica es probar para el kernel de contacto GAMMA REAL una norma de dilatación estrictamente contractiva en q>=5, uniforme en un rango explícito N/u². Esta propiedad produce cotas UNILATERALES del peine completo con error relativo geométrico y signo conocido, a partir de sumas sobre enteros con coeficientes cerrados de logaritmos. No se usa un mínimo común que borre la variación entre contactos. El fallo de inversión positiva para otros kernels019 no se extiende a esta clase contractiva. La comparación con ARCH+POLAR permanece como criterio explícito; no se declara resuelta por la mera convergencia.

## 2. Región y kernel real

En todo el memo,

    u>=63/2,  N entero>=3,
    N <= 2u²/9−u/3+3/2.                                  (REGION)

Se conserva el átomo f_(N,1), con norma019, y se define para q REAL>=2

    w(q)=2q^(-1/2) C_(N+1)''(logq)/||f_(N,1)||².

Así el peine normalizado es sum_(q>=2)Λ(q)w(q). Por la frontera019,

    chi_N < [1+sqrt(8N−11)]/2 <=2u/3<u log2,

porque (2u/3)²−2u/3−(2N−3)>=0 por REGION. Luego w(q)>0 para TODO q>=2. No se sustituye Λ por logq.

El resultado NUEVO de control es

    w(mq)<=m^(-2)w(q),  q>=5, m>=1.                      (DECAY)

En particular alcanza simultáneamente todos3<=N<=211 en u63/2, sin verificar cada orden.

## 3. Prueba elemental de DECAY

Use los polinomios positivos019

    p_j(x)=sum_(l=0)^j (2j−l)! x^l/[2^(j−l)(j−l)!l!],
    p_j=(2j−1)p_(j−1)+x²p_(j−2),
    p_j'=p_j−x p_(j−1),  p_j>x p_(j−1)  (j>=1,x>=0).

Para x=u logq, el factor variable de C'' es e^(-x)r_N(x), donde

    r_N=x²p_(N−2)−p_(N−1).

Ponga R=p_(N−1)/p_(N−2). Para N>=3,

    R=2N−3+x² p_(N−3)/p_(N−2)
      >=2N−3+x²/(2N−5+x).                              (RLOW)

Para N3 la comparación del denominador es igualdad; para N>=4 sigue de la recurrencia y p_(N−3)>x p_(N−4). Derivar r mediante las identidades anteriores da

    r_N'=r_N+x p_(N−2)(2N−R),
    (log(e^(-x)r_N))'=x(2N−R)/(x²−R).                  (DER)

La derivada logarítmica sólo se usa donde r_N>0, ya garantizado por REGION y q>=5.

Escriba B=2N−5>0, t=logq>=log5>8/5. Entonces

    u[x/(B+x)−3/x]=u²t/(B+ut)−3/t >3/2.               (SLOPE)

En efecto el lado izquierdo crece en t. En t8/5 la comparación equivale exactamente a

    64u²−216u−270N+675>0.

Por REGION, este polinomio es al menos

    4u²−126u+270=4u(u−63/2)+270>0.

SLOPE implica R−2N>0 por RLOW. Como 0<x²−R<x²,

    x(R−2N)/(x²−R) >=(R−2N)/x
                        >=x/(B+x)−3/x.

Finalmente DER y el factor q^-1/2 producen

    dlogw(q)/dlogq
      =−1/2+u x(2N−R)/(x²−R) <−2.

Integrar entre q y mq prueba DECAY. Es una desigualdad de la forma exacta gamma, no una suposición de monotonía sobre todos los kernels.

## 4. Espacio contractivo y corrección de los tres contactos pequeños

En funciones q>=5 defina

    (Df)(q)=sum_(m>=2)f(mq),
    rho0=2389/3600<2/3.

La estimación elemental

    sum_(m>=2)m^-2
       <=sum_(m=2)^5 m^-2+int_5^infty x^-2dx=rho0

y DECAY implican 0<=Dw<=rho0 w. Además DECAY se conserva al aplicar D, de modo que

    0<=D^j w<=rho0^j w, j>=0.                           (CONTRACT)

Defina el coeficiente aritmético EXPLÍCITO

    b(n)=logn−log2·1_(2|n)−log3·1_(3|n)−log2·1_(4|n),
    L(f)=sum_(n>=5)b(n)f(n),
    A(f)=sum_(q>=5)Λ(q)f(q).

La identidad de divisores exacta muestra

    b(n)=sum_(d|n,d>=5)Λ(d)>=0,
    L(f)=A((I+D)f).                                    (DIV)

Las tres correcciones son esenciales: se quitan q2,3,4 como DIVISORES, no sólo tres términos del sumatorio n. No se usa logn sin corregir y no se prolonga artificialmente w con0 bajo5. Todas las sumas son absolutas: DECAY da w(n)<=25w(5)n^-2 y b(n)=O(logn). Los intercambios positivos de DIV también están justificados por Tonelli.

## 5. Cotas firmadas y resto relativo uniforme

Para K>=0 ponga

    S_K=sum_(j=0)^K (−1)^j L(D^j w).

La telescopía de DIV da exactamente

    S_K=A(w)+(−1)^K A(D^(K+1)w).                        (TEL)

No hay inferencia de signo por un prefijo genérico de Möbius. El resto AQUÍ es positivo por w>=0 y CONTRACT, y

    0<=A(D^(K+1)w)<=rho0^(K+1)A(w)
                         <=rho0^(K+1)L(w).              (REL)

Por tanto, para K IMPAR,

    S_K <= A(w) <= S_K+rho0^(K+1)L(w),
    (1−rho0^(K+1))A(w)<=S_K.                            (BRACKET)

En particular TODOS esos prefijos impares son positivos, uniformemente en REGION. Para K par el prefijo es una cota superior; no se confunden las dos direcciones. Esta es una desigualdad aritmética firmada sobre TODOS los contactos de la cola, con resto geométrico relativo a su magnitud; no es un bound relativo al pequeño residuo W.

Dos corolarios cuantitativos no requieren estimar una cola adicional:

    L(w)/(1+rho0) <= A(w) <= L(w),
    S_K <= A(w) <= S_K/(1−rho0^(K+1))   (K impar).        (INTRINSIC)

El primero sigue de L(w)=A(w)+A(Dw)<=(1+rho0)A(w); el segundo de BRACKET. Por ello también el PROPIO prefijo positivo controla su error relativo. No se afirma que éste sea relativo al pequeño residuo W.

Los coeficientes de L son logaritmos y divisibilidades cerrados. D^j w(n) también puede reagruparse como sum_(m>=2^j)d_j(m)w(nm), donde d_j cuenta factorizaciones ORDENADAS de m en j factores>=2. No se calcula ninguna campaña ni se afirma que esta enumeración sea más económica que032. El objetivo del criterio es mantener el signo de la corrección y ofrecer un error explícito uniforme.

## 6. Comparación concreta con la forma completa, todavía abierta en REGION

Sea

    B_N(u)=ARCH_(N,1)/norm²+POLAR_(N,1)/norm²
            +log2 w(2)+log3 w(3)+log2 w(4).

ARCH admite las fórmulas exactas A0/A1 de ARCH_EXACT032 para todo N, con x=(u+1/2)/2; el polar es exacto019. Para TODO K impar y TODO REGION,

    B_N(u)+S_K <= W[f_(N,1)]/norm²
       <=B_N(u)+S_K+rho0^(K+1)L(w).                     (FULL)

En particular, sin elegir K, la cota de magnitud concreta es

    B_N(u)+(3600/5989)L(w) <= W[f_(N,1)]/norm²
                             <=B_N(u)+L(w).             (MAGNITUDE)

Éste es un criterio suficiente cuantitativo: demostrar B_N(u)+S_K>0 en un rango prueba W en ese rango, conservando todos los contactos y el resto. El error ya tiene signo y factor uniforme, pero NO se ha probado esa desigualdad positiva para un rango nuevo. El margen032 de orden1e−15 no autoriza a borrar el resto por pequeño que sea un prefijo.

Como control de escala, rho0^100<10^-17 por aritmética racional. Eso indica que la jerarquía puede alcanzar errores relativos pequeños con un orden FINITO explícito; no supone que el valor truncado tenga signo positivo ni transforma la convergencia en una prueba global.

## 7. Resultado y límite

Se obtiene una herramienta uniforme NUEVA sobre la clase gamma real: DECAY en REGION, inversión de divisores mediante un operador positivo estrictamente contractivo y BRACKET/FULL con resto relativo firmado. No se presenta la identidad Euler como descubrimiento ni como signo W. Frente019, la positividad de la inversión se prueba por CONTRACT para esta cola específica, y no se exige en prefijos arbitrarios de otros kernels. Frente032, no se certifica otro N.

Sigue abierta una comparación de B_N+S_K que venza la cancelación completa en un rango. Este resultado controla la aproximación aritmética; no aumenta cobertura W ni resuelve las filas de tasa fija que siguen abiertas.
