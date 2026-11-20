# POWER_SCHUR_BASE_OBSTRUCTION_081 — BASE no se hereda por el resto real

Estado: **PROVED, auditoría independiente aprobada.** Véase `POWER_SCHUR_BASE_AUDIT_081.md`. Obstrucción a una clase recursiva específica: el resto regularizado G_p de la Phi REAL no conserva ser creciente y cóncavo para todos los pivotes positivos. No es un contraejemplo a W, a la positividad de su kernel, ni a la recursión de Schur general. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados POWER_SCHUR_003, POWER_TWO_COPY_SCOPE_074, POWER_THETA_REMAINDER_077 y el apéndice078 de POWER_STATE_077.003 y074 refutan promociones genéricas desde monotonías o desde una clase de potenciales; aquí se considera exclusivamente el resto exacto de la Phi real ya construido075–077.079 motiva preguntar si ese resto puede volver a satisfacer BASE073 para aplicar el mismo paso. El nuevo objeto es G_p REAL y el resultado es que su monotonía falla para pivotes suficientemente grandes, con un punto de derivada negativa fijado analíticamente, sin barrido.

## 2. Datos y normalización exacta

Usar las notaciones probadas073/077:

    a=M'(0)>0, B(z)=[az/M(z)−1]/z²>0,
    G_p(z)=az[B(p)−B(z)]/[B(p)(z²B(z)−p²B(p))].

Las singularidades en z=p son removibles.077 da G_p(z)>0 para todos p,z>0. Definir

    F(z)=zB(z)=a/M(z)−1/z,
    g(z)=z²B(z)=az/M(z)−1,
    K_p=p²B(p)=ap/M(p)−1,
    C_p(z)=[p²B(p)²/a]G_p(z).

El símbolo g aquí tiene argumento z, no x=z² como en079. Álgebra exacta da

    C_p(z)=z[B(z)−B(p)]/[1−g(z)/K_p].               (NORMAL)

BASE073 implica g'(z)>0 y

    0<F(z)<a/M(z),
    0<g'(z)=a[M(z)−zM'(z)]/M(z)²<a/M(z).          (BOUNDS)

## 3. Límites sin una hipótesis asintótica nueva

Las cotas reales completas usadas078 dan M(z)→infinito y M(z)/z→0. Más explícitamente, para z>=128,

    M(z)<log(z/5)/2+2/(z−1/2)<sqrt(z).

La última desigualdad usa log z<=sqrt z y 2/(z−1/2)<1<sqrt(z)/2. Una cota inferior creciente hasta infinito proviene de078:

    M(z)>=log[(z+1/2)/(2pi)]/2−1/100, z>=63/2.

Por ello B(p)→0, K_p→infinito, F(z)>0 y F(z)→0 cuando z→infinito. NORMAL converge a F, con todas sus derivadas en cualquier compacto de z>0. Ya esto impide que todos los G_p sean crecientes: un límite puntual de funciones crecientes sería creciente, pero F es positiva y tiende a cero.

La sección siguiente fija un punto y un umbral explícito, sin depender sólo de este argumento límite.

## 4. Punto explícito de derivada negativa

Poner z_*=1024, c_*=M(z_*). El apéndice078 prueba a>1/25 mediante el ancla real L(8)>3/10 y la concavidad073. Para A=z+1/2>=32, las series reales completas y psi_1(A/2)>=2/A dan

    M'(z)>=1/(2A)−1/A²−1/(A−1)²
           >1/(2A)−3/A²>1/(3A).

Se usó A²/(A−1)²<2 y A>18. En z_*, la fórmula de M con psi(y)<=log y, P_0>=0 y pi>3 da

    c_*<2/(A−1)+log(A/6)/2
        <1/100+log(243)/2<1/100+11/4<3.

Aquí A=2049/2, A/6=683/4<243 y log3<11/10, constante ya usada078. Además

    z_*²M'(z_*)>z_*²/[3(z_*+1/2)]>300,

pues 1048576>922050. Por tanto

    a z_*² M'(z_*)/c_*²>300/(25·9)=4/3,
    F'(z_*)=1/z_*²−aM'(z_*)/c_*²<−1/(3z_*²).       (NEGATIVE)

No se evalúa numéricamente ningún dato theta nuevo.

## 5. Umbral explícito de pivote

Definir constantes positivas de la misma Phi real

    g_*=az_*/c_*−1,
    L=2g_*+24a²z_*²/c_*²,
    p_0=[25(L+2)]².

Este umbral es simbólico y efectivo en términos de a y c_*, sin búsqueda de pivotes. Como p_0>2500>z_* y M(p)<sqrt p para p>=p_0,

    K_p=ap/M(p)−1>sqrt p/25−1>=L+1>L.

En particular 0<g_*/K_p<1/2. Derivar NORMAL, manteniendo p fijo, da

    C_p'(z)=[F'(z)−B(p)]/[1−g(z)/K_p]
       +z[B(z)−B(p)]g'(z)/{K_p[1−g(z)/K_p]²}.

En z_*, el primer sumando es menor que F'(z_*), porque este es negativo, B(p)>0 y el denominador está entre0 y1. Por BOUNDS, el segundo sumando es menor que 4a²/(c_*²K_p). Esta cota sigue siendo válida incluso si su numerador fuese negativo. Así, para TODO p>=p_0,

    C_p'(z_*)<−1/(3z_*²)+4a²/(c_*²K_p)
              <−1/(3z_*²)+1/(6z_*²)
              =−1/(6z_*²)<0.

La normalización p²B(p)²/a es positiva. En consecuencia

    G_p'(1024)<0, TODOS p>=p_0.                     (FAIL-BASE)

Esto refuta heredar la condición G'>0 globalmente. También impide heredar G''<=0 globalmente: si una función positiva en toda la semirrecta fuera cóncava y tuviera una derivada negativa en1024, quedaría por debajo de una recta que acaba siendo negativa. En particular para cada p>=p_0 existe algún punto posterior donde G_p''>0.

## 6. Alcance y residuo vivo

G_p>0 permanece probado077. El fallo de G_p'>0 no contradice que un kernel de dos nodos pueda ser positivo: el criterio |zG_p'/G_p|<=1 permite derivadas negativas. Tampoco se elimina el residuo positivo de Schur R_p/z, ni se afirma que el kernel completo regularizado falle.

Por tanto no se puede iterar079 simplemente declarando BASE073 para cada nuevo G_p. Queda abierta una clase más amplia que permita funciones decrecientes, o una prueba que conserve el residuo y controle los cruces directamente. La doble concavidad opcional078 daba precisamente una posible condición para pares del kernel G_p sin exigir G_p'>0; este documento no la refuta, no prueba su preservación y no decide órdenes superiores. Signo global OPEN.
