# POWER_DIRECT_RECIPROCAL_TURAN_097 — T_h directa y cola real desde512

**Actualización099:** la obligación REAL T_h>0 global quedó cerrada en `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, auditada en `POWER_EXACT_H_GLOBAL_AUDIT_099.md` y resumida en `POWER_STATE_099.md`. Se prueban ambas curvaturas y todos los triples del resto G_p; el bloque auxiliar de cinco nodos está anclado en0 y NO son cinco generadores W admisibles. Las menciones de compacto/hipótesis pendiente abajo conservan el estado histórico de esta ronda; la herencia al siguiente nivel sigue abierta.

Estado: **PROVED la fórmula, la regularización y T_h>0 para TODO u>=512; auditorías independientes aprobadas.** Véase `POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md`. El compacto0<u<512 sigue OPEN. No se requiere el signo puntual de las densidades particulares K. No se afirma preservación de Turán, signo de todos los órdenes ni nueva cobertura W. Papers intactos; sin nuevos certificados numéricos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados078,083–085,089–090,092–093 y095.090 identifica T_h>0 como una obligación exacta para las curvaturas R_G en todos los pivotes y refuta su herencia genérica desde T_R>0. El signo del Wronskiano de densidades particulares investigado093/095 es una condición suficiente MÁS FUERTE, todavía sin prueba global.

Aquí se trabaja directamente con la MISMA h en datos reales M,Z. Se conserva su cancelación algebraica y se obtiene una nueva desigualdad de cola mediante las series completas ya auditadas084. No se vuelve a certificar otra dimensión ni se promueve la identidad anclada de cinco columnas como una ganancia de signo.

## 2. Fórmula explícita en M y tres derivadas

Poner x=u², a=M'(0)>0 y

    c=M(u), d=M'(u), e=M''(u), f=M'''(u),
    D=ud, E=u²e, F=u³f,
    h(x)=u²M(u)/[au−M(u)].

Las derivadas de h son respecto de x; d,e,f son respecto de u.073 da au−c>0 para u>0. Definir el polinomio N_S ya utilizado084 y un polinomio C_h nuevo:

    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E²,
    C_h=3c³+c²(3D+6E+F)+c(−12D²−6DE)+6D³.

Entonces exactamente

    T_h=2h'h'''−3h''²
        =a[au N_S−4C_h]/[16u³(au−c)^4].           (DIRECT)

Son coeficientes explícitos: N_S y C_h sólo contienen a,u,M,M',M'',M'''. No se necesita derivar un resto asintótico. Una comprobación por derivación usa

    h'=[acu+adu²−2c²]/[2(au−c)²],
    h''=a[−acu+adu²+aeu³+3c²−5cdu−ceu²+2d²u²]
                                      /[4u(au−c)³].

Derivar h'' por(2u)^(-1)d/du y combinar2h'h'''−3h''² da DIRECT. El numerador no se sustituye por errores absolutos independientes antes de efectuar esa cancelación.

Como control estructural, S(x)=uM(u) satisface T_S=N_S/(16u^6), y

    T_h={a²u⁴T_S+2ac⁴(d/dx)^3[u³/M(u)]}/(au−c)^4.

El segundo sumando puede ser negativo; por eso T_S>0, por sí solo, no resuelve el signo. La prueba siguiente paga su coste mediante C_h.

## 3. Entrada aritmética completa y caja exterior auditada

Escribir A=u+1/2.084 prueba por series reales completas

    c=1/A+1/(A−1)−logpi/2+psi(A/2)/2−P_0,
    d=−1/A²−1/(A−1)²+psi_1(A/2)/4+P_1,
    e=2/A³+2/(A−1)³+psi_2(A/2)/8−P_2,
    f=−6/A⁴−6/(A−1)⁴+psi_3(A/2)/16+P_3,
    P_j(A)=sum_(n>=2)Lambda(n)(log n)^j n^(−A).

Todas estas sumas son absolutas en la región empleada. No se truncan primos. Los restos completos se pagan mediante

    P_j(A)<=2^(j+1−A)[1+2/(A−j−2)], j=0,1,2,3,

y comparaciones integrales de las series de polygamma, detalladas084. Su consecuencia auditada para A>=128 es

    c>3/2,
    9/20<D<51/100,
    −51/100<E<−2/5,
    4/5<F<101/100,
    N_S>3c²−2>2c².                                (INPUT-084)

La última comparación usa c²>9/4>2. Se reutiliza una cota c-dependiente de084, no sólo el margen constante N_S>19/4.

La misma caja permite una cota superior conjunta de C_h. En efecto,

    3D+6E+F<3(51/100)+6(−2/5)+101/100=7/50,
    −12D²−6DE<−12(9/20)²+6(51/100)²
                  =−4347/5000<0,
    6D³<6(51/100)³<4/5.

Por ello

    C_h<3c³+(7/50)c²+4/5<4c³, c>3/2.             (COST)

La última desigualdad es elemental: c³−(7/50)c²−4/5 es creciente para c>=3/2 y en3/2 vale113/50>0. Si C_h fuese negativo, el coste sería todavía menor; no se presume su signo.

INPUT-084 y COST dan

    au N_S−4C_h>2c²(au−8c).

Así basta demostrar au>8M(u) en la cola.

## 4. Comparación escalar que paga TODO u>=512

078 prueba el dato REAL a>1/25, usando el ancla L(8)>3/10 y073. También, para u>=128,

    M(u)<log(u/5)/2+2/(u−1/2).                    (UPPER-M)

En u=512, 512/5<128 y log2<7/10 implican

    M(512)<(7/2)log2+2/(512−1/2)
           <49/20+1/100=123/50.

La cota log2<7/10 se demuestra, por ejemplo, con la suma positiva de la serie de exp(7/10) hasta grado4, que es mayor que2. Así

    8M(512)<492/25<512/25<a·512.

Para extender la comparación sin malla, considerar

    H(u)=u/25−4log(u/5)−16/(u−1/2).

El cálculo anterior da H(512)>0, y para TODO u>=512,

    H'(u)=1/25−4/u+16/(u−1/2)²
           >1/25−4/512>0.

UPPER-M implica entonces au>u/25>8M(u) para todos esos u. DIRECT queda estrictamente positivo:

    T_h>a c²(au−8c)/[8u³(au−c)^4]>0,
    TODOS u>=512.                                (DIRECT-TAIL)

El umbral se fijó por estas desigualdades analíticas holgadas. No se buscó un extremo favorable ni se evaluó numéricamente T_h. El dominio es del parámetro de inclinación u; no es el dominio temporal t de095.

## 5. Regularización exacta del origen

La paridad de Z y su positividad cerca del origen hacen analítica N(x)=M(u)/u en x=u². Escribir

    N(x)=a+b_1x+b_2x²+b_3x³+b_4x^4+O(x^5),
    b_1=kappa4/6, b_2=kappa6/120,
    b_3=kappa8/5040, b_4=kappa10/362880,

donde kappa_(2j) son los cumulantes de la ley real Phi sin inclinación. No se afirma su signo por separado.086 da R'(0)>0, así b_1<0, pues R=1/N. La expresión regular es

    h(x)=N(x)/B_0(x),
    B_0(x)=[a−N(x)]/x,
    B_0(0)=−b_1>0.

Por tanto h y sus derivadas son analíticas en un entorno de0; el denominador aparentemente singular de DIRECT no implica una singularidad real. No se usa el numerador y denominador pequeños por separado para decidir un signo.

Los valores explícitos son

    h(0)=−a/b_1,
    h'(0)=a b_2/b_1²−1,
    h''(0)=2a(b_1b_3−b_2²)/b_1³,
    h'''(0)=6a(b_1²b_4−2b_1b_2b_3+b_2³)/b_1^4.

Combinar estas derivadas cancela términos y da

    T_h(0)=(12a/b_1^4)
       ·det[[a,b_1,b_2],[b_1,b_2,b_3],[b_2,b_3,b_4]]. (ORIGIN-HANKEL)

Así el dato de origen es un Hankel3 de los coeficientes NORMALIZADOS de cumulantes. No se infiere su signo de la positividad de una medida distinta ni de la positividad individual de algunos cumulantes. En esta fuente no se calculan nuevos momentos ni se certifica el signo de ORIGIN-HANKEL.

## 6. Obligación restante y alcance

DIRECT-TAIL descarga la obligación EXACTA T_h en una cola de u. En0<u<512 sigue faltando un bound conjunto para auN_S−4C_h, o una comparación equivalente que conserve su cancelación. Para decidir el propio origen puede usarse ORIGIN-HANKEL con un encierro de momentos previamente diseñado; no se inició ese cálculo aquí.

El dato es más débil que exigir un Wronskiano temporal firmado en cada punto: no necesita esa hipótesis suficiente ni deriva sus restos reales. No se ha demostrado T_h global, R_G'' para todos los pivotes, todos los triples del kernel G_p, cinco generadores originales o todos los órdenes. La nueva cola no modifica por sí sola la cobertura W ya probada085. El contraejemplo de herencia090 permanece válido y no refuta esta desigualdad REAL. Objetivo global OPEN.
