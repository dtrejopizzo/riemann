# POWER_FOUR_TURAN_084 — Un criterio local suficiente para los Pfaffianos de orden cuatro

**Actualización085:** el compacto restante fue certificado y auditado en `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md` y `POWER_STATE_085.md`: TODOS los cuatro exponentes ai>1 tienen W completa positiva. Las menciones de compacto pendiente abajo conservan el estado histórico de084; órdenes superiores siguen abiertos.

Estado: **PROVED como criterio, falsificador de herencia y aplicación exterior, auditoría independiente aprobada.** Véase `POWER_FOUR_TURAN_AUDIT_084.md`. Para la Phi real se prueban aquí las nuevas condiciones sólo en una región exterior explícita. No se declara el compacto restante ni cuatro generadores globales. Papers intactos; sin matrices numéricas o campañas.

## 1. Antecedentes y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados SCHUR003,074,079–083.083 factoriza determinantes en productos de Pfaffianos, sin controlar sus signos.080 y082 controlan exactamente tres nodos mediante concavidad de los dos datos recíprocos. No se extrapola esa concavidad a cuatro.

El álgebra de Pfaffianos, los determinantes generalizados, Rolle y los cocientes de Wronskianos son herramientas clásicas, no se reivindican como nuevas. Aquí se prueba directamente la especialización de cuatro nodos y una desigualdad cuantitativa adicional que sí implica el signo en TODOS esos nodos. Se muestra además, conservando la reciprocidad exacta RS=x, que las propiedades escalares anteriores no bastan por sí solas. No es una refutación del dato theta real ni de toda la hipótesis de potencial073.

## 2. Identidad de cuatro nodos

Sean0<u1<u2<u3<u4, xi=ui², y f una función real. Poner

    A_f,ij=[f(xj)−f(xi)]/(ui+uj),
    P=producto_(i<j)(ui+uj)>0,
    D_f=det[1,xi,f(xi),xi f(xi)]_(i=1,...,4).

Entonces exactamente

    Pf(A_f)=−D_f/P.                                  (PF-DET)

Puede verificarse sin una inversa: expandir Pf=A12A34−A13A24+A14A23, multiplicar por P y expandir el determinante por las dos columnas que contienen f. Los coeficientes de cada producto f(xi)f(xj) coinciden con el signo negativo indicado. Es una identidad polinómica en los ui y los cuatro valores de f; la comprobación simbólica auxiliar dio identidad cero, no un muestreo.

En particular, para R(x)=sqrt(x)/M(sqrt(x)) y S(x)=sqrt(x)M(sqrt(x)),083 da

    det K=Pf(A_R)Pf(A_S)/producto_i R(xi),
    K_ij=[M(ui)+M(uj)]/(ui+uj).

Así un signo positivo de cada Pfaffiano sería suficiente; la identidad sola no lo suministra.

## 3. Criterio cuantitativo global por Rolle

Suponga f∈C³ en un intervalo de cuadrados, f'>0,f''<0, y

    T_f=2f'f'''−3(f'')²>0 en TODO el intervalo.        (TURAN)

Se prueba Pf(A_f)>0 para TODOS los cuatro nodos distintos del intervalo.

Definir

    H(x)=(x f(x))''/f''(x)=x+2f'(x)/f''(x).

Como f'' no se anula,

    H'(x)=−T_f/(f'')²<0.

Si D_f se anulara para cuatro puntos distintos, existiría una combinación no nula

    h(x)=a+bx+cf(x)+dx f(x)

con cuatro ceros distintos. Rolle aplicado dos veces exigiría al menos dos ceros distintos de

    h''(x)=f''(x)[c+dH(x)].

La monotonía estricta de H permite a lo sumo uno, salvo c=d=0. En ese borde h es afín y cuatro ceros obligan a=b=0, contradicción. Por tanto D_f nunca se anula en el dominio conectado de cuádruplas ordenadas y su signo es constante.

El Wronskiano de las cuatro columnas es exactamente

    W(1,x,f,xf)=3(f'')²−2f'f'''=−T_f<0.

Al hacer confluir los nodos en cualquier punto interior,

    D_f/producto_(i<j)(xj−xi) -> −T_f/(0!1!2!3!)<0.

Esto fija D_f<0 para toda cuádrupla ordenada. PF-DET prueba el signo positivo del Pfaffiano. El argumento no se limita a un jet confluyente: Rolle transporta ese signo a TODOS los conjuntos de nodos.

Por consiguiente, para M real, si se demostrara TURAN tanto para R como para S en un intervalo, todos los bloques de cuatro nodos distintos serían definidos positivos: los menores de tamaños1,2,3 ya son positivos por073/080 y el de tamaño4 lo es por083. Nodos coincidentes se agrupan como de costumbre. TURAN de ambos factores es una condición SUFICIENTE; aquí no se afirma que cada una sea necesaria para el producto pfaffiano ni para W.

## 4. Falsificador de la herencia desde las concavidades anteriores

Fijar epsilon=1/16 y, en0<=x<=1,

    R(x)=1+x−epsilon x²,
    S(x)=x/R(x),
    M(u)=u/R(u²), 0<=u<=1.

R>0,R'>0,R''=−1/8<0. Además

    S'=(1+epsilon x²)/R²>0,
    S''R³=−2+6epsilon x+2epsilon²x³
          =(x−4)(x²+4x+64)/128<0.

Se conserva RS=x EXACTAMENTE. Para x=u²,

    M'=[1−x+3x²/16]/R²>0,
    M''R³/(2u)=[3x³−24x²+208x−384]/128<0

para0<u<=1: basta acotar el último numerador por3+208−384<0. También M(0)=0,M'(0)=1, M/u=1/R decrece, y

    g(x)=u/M(u)−1=x−x²/16,
    b(x)=g(x)/x=1−x/16>0

son, respectivamente, estrictamente creciente/cóncava y estrictamente decreciente. El ejemplo satisface por tanto las propiedades escalares usadas en073/077/080, y079 da todos sus triples definidos positivos en nodos distintos del intervalo. No se afirma que este M sea el tilt de una Phi con la hipótesis completa de073.

Sin embargo, para CUALESQUIERA cuatro nodos distintos en(1/2,1), poner V=producto_(i<j)(uj−ui)>0. La descomposición de rango da exactamente

    Pf(A_R)=−epsilon² V,
    Pf(A_S)=epsilon V/producto_i R(xi).

Para la primera identidad, A_R es la suma de las formas simples 1∧u y −epsilon(1∧u³+u²∧u). En la base(1,u,u²,u³), su Pfaffiano de coeficientes es−epsilon²; la congruencia aporta V. Para la segunda, multiplicar filas y columnas de A_S por Ri da la matriz con entradas(uj−ui)(1+epsilon ui²uj²), es decir1∧u+epsilon u²∧u³. Su Pfaffiano es epsilon V. Así

    det K=−epsilon³ V²/[producto_i R(xi)]²<0.         (FAIL-HEREDITY)

Es un falsificador simbólico de TODAS las cuádruplas indicadas, no una matriz numérica seleccionada. Refuta sólo inferir cuatro desde esas propiedades escalares locales; no refuta el dato real Phi,073,080 ni una condición adicional específica.

## 5. Condiciones explícitas para el dato real

Las derivadas siguientes son respecto de x=u². Poner c=M(u),d=M'(u),e=M''(u),f=M'''(u). Derivación directa da

    T_R=N_R/(16c⁴u⁶),
    T_S=N_S/(16u⁶),

con

    N_R=3c²−6ucd−6u²ce−2u³cf
           +3u²d²+6u³de+2u⁴df−3u⁴e²,
    N_S=3c²+6ucd+6u²ce+2u³cf
           −9u²d²−6u³de+2u⁴df−3u⁴e².                 (REAL-TURAN)

Los denominadores son positivos.073/080 ya prueban R',S'>0 y R'',S''<0 para u>1/2. Por tanto N_R>0 y N_S>0 son DOS obligaciones cuantitativas específicas suficientes para el siguiente paso; no se obtienen sólo del signo de las derivadas de orden dos.

En confluencia de cuatro nodos, la identidad también da

    Pf(A_f)/producto_(i<j)(uj−ui) -> T_f/12.

Esto comprueba los factores y signos de REAL-TURAN, pero la suficiencia global viene de§3, no de esa comprobación local.

## 6. Verificación exterior analítica con toda la aritmética

Se prueba N_R,N_S>0 para TODO A=u+1/2>=128. Es una región exterior elegida analíticamente para márgenes holgados, sin barrido ni optimización de un umbral. Escribir

    P_j(A)=Σ_(n>=2)Lambda(n)(log n)^j n^(−A),
    D=ud,E=u²e,F=u³f.

La fórmula aritmética completa y las series de polygamma dan

    c=1/A+1/(A−1)−logpi/2+psi(A/2)/2−P0,
    d=−1/A²−1/(A−1)²+psi1(A/2)/4+P1,
    e=2/A³+2/(A−1)³+psi2(A/2)/8−P2,
    f=−6/A⁴−6/(A−1)⁴+psi3(A/2)/16+P3.

Las comparaciones integrales de las series positivas prueban

    1/t<=psi1(t)<=1/t+1/t²,
    −1/t²−2/t³<=psi2(t)<=−1/t²,
    2/t³<=psi3(t)<=2/t³+6/t⁴.

Con Lambda(n)(log n)^j<=(log n)^(j+1)<=n^(j+1),

    P_j(A)<=2^(j+1−A)[1+2/(A−j−2)], j=0,1,2,3.

Los majorantes relevantes decrecen a partir de A=32 por derivada logarítmica<=3/A−log2<0. Las comparaciones racionales en32 dan

    AP1<1/100, A³P2<1/4, A³P3<1/100,
    (A−1)P0<1,                                      (PRIME-BOUNDS)

válidas para todos A>=32. Por ejemplo A³P3 en32 es29/(27·8192)<1/100; las otras son las cotas ya documentadas078. No se corta la suma de primos sin cola.

Para A>=128 se obtiene, SIN sustituir por un asintótico,

    9/20<D<51/100,
    −51/100<E<−2/5,
    4/5<F<101/100.                                  (BOX)

Detalles de los lados inferiores/superiores menos inmediatos: con(A/(A−1))^k<2 para k<=4,

    D>=1/2−13/(4A)>9/20,
    E>=−1/2−A²P2>−51/100,
    E<=−1/2+13/(2A)<−2/5,
    F>=1−39/(2A)>4/5,
    F<=1+A³P3<101/100.

El bound superior de D es el de078. Para el lower de F se usaron (u/A)³>1−3/(2A) y las dos contribuciones racionales negativas, acotadas por6/A y12/A; para el upper se cancela el término6/A⁴ de psi3 con el racional−6/A⁴.

Además c>3/2. En efecto psi(t)>=logt−1/t y PRIME-BOUNDS dan

    c>(1/2)log[A/(2pi)].

Para A>=128, pi<22/7 da A/(2pi)>224/11. La comparación e<87/32 (serie hasta grado3 más cola5/96) implica e³<(87/32)³<224/11. Así el logaritmo supera3.

Finalmente REAL-TURAN se escribe

    N_R=3c²+c(−6D−6E−2F)+3D²+6DE+2DF−3E²,
    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E².

La caja BOX implica, por comparaciones racionales directas,

    −6D−6E−2F>−3,
    3D²+6DE+2DF−3E²>−2,
    6D+6E+2F>0,
    −9D²−6DE+2DF−3E²>−2.

Por tanto, para TODO A>=128,

    N_R>3c²−3c−2>1/4,
    N_S>3c²−2>19/4.                                (OUTER-TURAN)

Esto prueba TURAN de ambos datos reales en la región exterior con restos aritméticos explícitos. No es una afirmación de suficiencia de su comportamiento límite.

## 7. Obligación pendiente y alcance

Para aplicar este criterio a cuatro generadores en TODO A_i>1 faltaría demostrar N_R,N_S>0 en1/2<u<127+1/2, o hallar otra comparación que pague directamente el producto de Pfaffianos sin exigir signos individuales. No se ejecutó un certificado compacto ni se eligieron parámetros a partir de valores flotantes.

El resultado exterior NO amplía cobertura de cuatro:053 ya probó trece polos arbitrarios en tasas>=63/2. La contribución nueva es el criterio cuantitativo GLOBAL de Pfaffiano4, el falsificador exacto de la herencia desde concavidad y una primera verificación analítica con toda la aritmética de las obligaciones locales. No se prueban cuatro generadores globales, todos los órdenes o una nueva ventana temporal.
