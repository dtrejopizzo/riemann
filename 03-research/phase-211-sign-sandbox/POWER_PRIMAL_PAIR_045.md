# POWER_PRIMAL_PAIR_045 — Reparación espectral compacta de un par representante

Estado: PROVED; revisión independiente APROBADA en POWER_PRIMAL_AUDIT_045.md§4. Resultado acotado: en la primera ventana con contactos2,3, una reparación de baja frecuencia que deje EXACTAMENTE fija la cola del símbolo no puede producir un par positivo con slack pequeño. Esto no cierra L55-B, no refuta pares con correcciones no compactas y no da nueva cobertura de signo.

## 1. Antecedentes y cambio preciso de hipótesis

Consultados ROUTES-TRIED-INDEX/README.md§L55, AUDIT_B.md§1 (especialmente líneas32–41 y L55-B), grid R162_2300_MASTER_GRID, CROSSWORD-TO-D y las definiciones primal/dual de Paper47§3. L55-B sigue registrado como candidato abierto: no se encontró una construcción posterior. La revisión044 ya distinguió un test factible que da un upper de un par REPRESENTANTE que sí puede dar un lower.

No se impone masa total finita a la medida espectral: esa restricción no pertenece a L55-B y es inadecuada para un símbolo de crecimiento logarítmico. Aquí la medida es localmente finita y tiene una cola de esa escala. La hipótesis nueva y específica que se prueba es que toda su CORRECCIÓN sea compacta en frecuencia, manteniendo exactamente la cola real del símbolo. La obstrucción usa unicidad de momentos de una medida compacta y la identidad para TODOS los tests, no W4 ni una modificación del peine.

La unicidad de transformadas compactas es una herramienta clásica. No se presenta como un principio nuevo de signo. El resultado identifica por qué esta reparación particular no construye el par que falta y dónde retorna la libertad dual ya conocida.

## 2. Ventana, normalizaciones y orientación del lower

Fije T=3/5, I=(-T,T), Fourier Fhat(tau)=int F(t)exp(i tau t)dt y

    Phi_F(tau)=|Fhat(tau)|²/(2pi),
    c_F(u)=int F(t)conj(F(t−u))dt.

Tome tests reales F en C_c^infty(I) con A(F)=int F exp(t/2)=0 y B(F)=int F exp(−t/2)=0. La forma COMPLETA coincide allí con la primitiva porque su polar2Re(A conjB) se anula. En esta ventana log3<2T<log4, por lo que los únicos contactos son2,3. Defina

    m(tau)=Re psi(1/4+i tau/2)−logpi,
    a_n=logn, v_n=2Lambda(n)/sqrt(n),
    q_T(tau)=m(tau)−v_2 cos(a_2 tau)−v_3 cos(a_3 tau),
    nu_Lambda=(v_2/2)(delta_(a_2)+delta_(−a_2))
                    +(v_3/2)(delta_(a_3)+delta_(−a_3)).

Así a_T(F)=int q_T Phi_F d tau. No se ha borrado ningún contacto aritmético de la ventana.

Un par representante propuesto consiste en medidas positivas PARES mu,nu, localmente finitas, que satisfagan, para TODOS esos tests,

    ARCH_complete(F)+epsilon||F||²
          =int Phi_F dmu+int c_F dnu,                  (PAIR)
    nu|_(-2T,2T)=nu_Lambda.

Las posibles masas de nu en|u|>=2T no contribuyen, pues c_F es0 allí. Todas las integrales deben existir. Entonces, con orientación correcta,

    a_T(F)+epsilon||F||²=int Phi_F dmu>=0,
    lambda_A(T)>=−epsilon.                             (LOWER)

mu aquí NO es la probabilidad factible del programa(P) de Paper47: aquélla produce un upper de lambda_P. PAIR es una identidad representante para TODOS los tests y es por eso un dato potencial de lower.

## 3. Ansatz de cola fija y lema de rigidez compacto

Suponga que, para algún R finito,

    eta:=mu−(q_T+epsilon)d tau

es una medida firmada PAR soportada en[-R,R]. Por la finitud local, eta tiene variación total finita. La medida mu puede tener masa total infinita; fuera del compacto coincide exactamente con el símbolo real desplazado. Como q_T crece logarítmicamente, esta cola es positiva para R suficientemente grande. No se adopta una restricción artificial de masa finita global.

**Lema.** Si PAIR vale para todos los tests primitivos indicados, entonces eta=0.

Prueba enteramente en variables reales. Restar las dos representaciones da

    int |Fhat(tau)|² d eta(tau)=0.

Para CUALQUIER phi real en C_c^infty(I), tome F=(D²−1/4)phi. Dos integraciones por partes prueban A(F)=B(F)=0, y

    Fhat(tau)=−(tau²+1/4)phihat(tau).

La medida compacta PAR d eta_tilde=(tau²+1/4)²d eta satisface

    int |phihat|²d eta_tilde=0 para toda phi.            (ALL-SQUARES)

Polarizar sobre phi,psi reales y usar paridad da que el núcleo real continuo

    k(u)=int cos(tau u)d eta_tilde(tau)

satisface int int phi(t)psi(s)k(t−s)dt ds=0. Localizando phi y psi con aproximaciones suaves de masas puntuales en dos puntos de I, se obtiene k(u)=0 para TODO|u|<2T. Aquí se usan todos los cruces, no sólo entradas diagonales de una matriz finita.

Por compacidad se puede derivar bajo el integral a cualquier orden en u0. Todos los momentos pares de eta_tilde son0; los impares son0 por paridad. Los polinomios son densos en las funciones continuas del compacto[-R,R], por lo que eta_tilde=0. El factor(tau²+1/4)² es estrictamente positivo en R, luego eta=0. No se necesita ningún argumento sobre objetos espectrales externos a estas formas y medidas.

La condición PAR es esencial. Sin ella, una medida impar arbitraria sería invisible a estas autocorrelaciones reales; sólo se concluiría eta_even=0.

## 4. Falsificador verificable del ansatz con slack pequeño

En tau0,

    m(0)=−gamma−pi/2−3log2−logpi<−53/10,
    v_2>19/20, v_3>5/4,
    q_T(0)<−15/2.                                     (NEGATIVE-DENSITY)

Son comparaciones racionales con los intervalos elementales ya auditados003. Por ejemplo sqrt2<10/7 da v2>(7/5)log2>19/20; sqrt3<26/15 da v3>(15/13)log3>5/4. No se usa cuadratura ni un espectro aproximado.

Si epsilon<=15/2, el lema obliga a mu=(q_T+epsilon)d tau, cuya densidad es NEGATIVA en un entorno de0 por continuidad. Esto contradice mu>=0. Por tanto no existe PAIR de cola exactamente fija con corrección compacta y slack epsilon<=15/2. En particular ese ansatz no construye un par de slack0, aunque la positividad de la forma en esta ventana ya está probada dentro del rango log5/2.

No se ha exhibido un vector con a_T(F)<0. La negatividad puntual del símbolo no es la de su compresión a la ventana; precisamente esa diferencia hace necesaria una representación distinta.

## 5. La corrección no compacta y su relación exacta con(D)

El obstáculo permite correcciones NO compactas. Para reconocer cuándo esa salida ya pertenece al corpus, considere el subcaso mu=(q_T+epsilon+r)d tau, con r una función par continua templada. La identidad representante exige

    int |Fhat|²r d tau=0 para todo F primitivo.

Sea k la transformada inversa de r como distribución. El mismo test F=(D²−1/4)phi y la polarización implican

    (D²−1/4)²k=0 en(-2T,2T).

Las soluciones PARES de esta ecuación diferencial son

    k(u)=alpha cosh(u/2)+beta u sinh(u/2), |u|<2T.

Defina g0=cosh(u/2)1_(|u|<2T), g1=u sinh(u/2)1_(|u|<2T). Si el resto exterior k−alpha g0−beta g1 es una medida finita PAR firmada nu_ext soportada en|u|>=2T, entonces

    r=alpha g0hat+beta g1hat+nu_exthat,
    mu>=0 ⇒ q_T+nu_exthat+alpha g0hat+beta g1hat>=−epsilon.

Éste es EXACTAMENTE un certificado de valor−epsilon del programa(D) de Paper47, con su medida exterior y sus dos multiplicadores Tate. Así la reparación no compacta de ESTE subcaso no es una herramienta primal nueva: su verificación vuelve a llevar el margen dual conocido.

No se extiende esa identificación a todas las medidas espectrales positivas singulares ni a todas las distribuciones exteriores. L55-B conserva una posibilidad constructiva más general, pero este intento no aporta un par independiente de esa clase.

## 6. Entrada del contacto siguiente y alcance

Cuando T pasa log4/2 y permanece debajo de log5/2, el símbolo primitivo actualizado es

    q_(2,3,4)(tau)=q_(2,3)(tau)−log2·cos(tau log4).

La identidad incluye el valor REAL Lambda(4)=log2. Esa actualización es global en frecuencia: no puede efectuarse como una reparación compacta de la antigua cola. El lema anterior se aplica de nuevo al símbolo actualizado; no hay una continuación automática del par anterior.

Si un par representante llegara a extenderse a la nueva ventana pero mantuviera sólo los contactos2,3, la discrepancia del contacto4 tendría variación total log2 y la fórmula044 sólo garantizaría un floor−epsilon−log2. Eso es un costo conservador de TODA la forma, no un control de su margen ni de los cruces de un Schur. La identidad de la ventana anterior por sí sola ni siquiera garantiza esa extensión: su corrección exterior puede dejar de ser invisible al agrandarse el intervalo.

Por tanto no se anuncia cobertura nueva ni un mecanismo para pasar4 o5. El avance de esta exploración es un obstáculo verificable al ansatz concreto de cola fija con reparación compacta, más la identificación precisa del subcaso no compacto que regresa al dual existente. No es un no-go general a pares positivos, no usa una hipótesis de masa global finita y no convierte positividad auxiliar en cierre.

Reproducción de constantes:

    python3 03-research/phase-211-sign-sandbox/tools/power_primal_pair_045_verify.py

La prueba de rigidez y sus cruces es analítica y uniforme en R. El script sólo verifica el punto explícito y el conjunto de contactos, sin campañas.
