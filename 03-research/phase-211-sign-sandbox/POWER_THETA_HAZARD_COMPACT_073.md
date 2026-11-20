# POWER_THETA_HAZARD_COMPACT_073 — Cierre del intervalo modular de convexidad del hazard

Estado: **PROVED/APROBADO**, auditoría independiente POWER_THETA_AUDIT_073.md y reproducciones independientes exit0/PASS. Un certificado racional compacto, sin campaña de parámetros. No prueba por sí solo el signo de W ni una nueva ventana temporal. Papers y phase103 intactos.

## 1. Residuo y diferencia explícita

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos CONE001 y phase103/103_43_THETA_HAZARD_CONVEXITY_GATE.md. La búsqueda posterior de la puerta hazard-convexity/103_43 sólo encontró esa fuente y su entrada README103, sin cierre del compacto.10343 prueba V'''(t)>0 para t>=1/4, con V=−logPhi, pero deja pendiente0<t<1/4. Su argumento de primer modo no sirve en0: allí la tercera derivada logarítmica de ese modo es positiva y la suma la cancela exactamente por paridad.

Aquí se conserva esa cancelación. La obligación compacta que se certifica es MÁS FUERTE y no tiene margen nulo en el extremo:

    (logPhi)''''(t)<0 para TODO0<=t<=1/4.             (FOURTH)

La paridad de Phi da(logPhi)'''(0)=0; integrar FOURTH da V'''(t)>0 en0<t<=1/4. Junto al outer ya probado10343, se obtiene

    V'''(t)>0 para TODO t>0.                         (HAZARD)

La novedad es resolver un residuo compacto explícito con suma theta completa y cola rigurosa, no invocar una convexidad genérica ni repetir un test de primer modo. Una evaluación diagnóstica de los dos extremos sólo verificó la viabilidad del certificado; no forma parte de la prueba.

## 2. Reducción exacta a cinco sumas theta

Con x=pi exp(2t), y=m²x, escribir

    Phi(t)=pi exp(5t/2) S(t),
    S(t)=Σ_(m>=1)m²(2y−3)exp(−y).

El factor externo tiene logaritmo afín; sus derivadas de orden>=2 se anulan. Por tanto FOURTH equivale a(logS)''''<0. Para D=d/dt, definir polinomios racionales exactos

    Q0(y)=2y−3,
    Q_(r+1)(y)=2y[Q_r'(y)−Q_r(y)].

Entonces S^(r)=Σm²Q_r(y)exp(−y). Los polinomios utilizados son

    Q1=10y−4y²,
    Q2=20y−36y²+8y³,
    Q3=40y−184y²+120y³−16y⁴,
    Q4=80y−816y²+1088y³−368y⁴+32y⁵.

La diferenciación término a término es absolutamente y localmente uniformemente convergente. Si a=S,b=S',c=S'',d=S''',e=S'''', el numerador exacto es

    S⁴(logS)''''=e a³−4d b a²−3c²a²+12c b²a−6b⁴.   (NUM)

El certificado verifica a>0 y NUM<0 en cada intervalo, de modo que no divide por una cantidad de signo indeterminado.

## 3. Cola completa, uniforme hasta la cuarta derivada

Retener m=1,2,3,4. Para TODOS r=0,...,4 y y>=1, la suma de valores absolutos de coeficientes de Q_r es<=9600 y su grado es<=5; así

    |Q_r(y)|<=9600 y⁵.

Para0<=t<=1/4 y m>=5 se tiene y>=3m²>=75. La función y⁵exp(−y) es decreciente para y>=5. La suma Taylor hasta grado7 verifica exp(3)>16. Por tanto

    m²|Q_r(y)|exp(−y)
      <=9600·3⁵ m¹²exp(−3m²)
      <9600·3⁵ m¹²2^(−4m²).

La razón de términos consecutivos de este último majorante es

    (1+1/m)¹²2^(−8m−4)
      <=(6/5)¹²2^(−44)<1/2.

Sumando la geométrica desde m=5, la cola COMPLETA de cada derivada queda encerrada en[−E,E], donde

    E=2·9600·3⁵·5¹²·2^(−100)
     =4449462890625/4951760157141521099596496896.      (TAIL)

No se infiere signo de la suma infinita desde un prefijo theta. La misma E se añade a CADA una de las cinco sumas antes de formar NUM.

## 4. Encierros racionales y malla fijada

El verificador tools/power_theta_compact_073_verify.py usa intervalos cerrados con extremos enteros divididos por10^70. Cada operación se redondea hacia fuera mediante cociente entero floor/ceil, incluidos productos, recíprocos positivos y potencias. Los polinomios Q se generan por la recurrencia exacta anterior.

Pi se encierra mediante Machin pi=16atan(1/5)−4atan(1/239). Cada arctangente utiliza128 términos alternantes y un resto bilateral de radio x^257/257. No hay dato flotante como entrada.

Para encerrar exp(z),0<=z<=128, se divide el argumento por128. Con0<=v=z/128<=1, la suma Taylor hasta grado128 tiene resto entre0 y2/129!, pues la razón entre términos sucesivos desde el primero omitido es<=1/130<1/2. Tras añadir ese resto se eleva al cuadrado siete veces con redondeo exterior. Los argumentos usados satisfacen el rango comprobado; en particular m²pi exp(2t)<128 para m<=4.

La ÚNICA malla, fijada antes de ejecutar, es

    I_i=[i/16384,(i+1)/16384], i=0,...,4095.

En cada I_i se encierran x,y y las cinco sumas S^(r), añadiendo TAIL; después se verifica a.lower>0 y NUM.upper<0. La unión es todo[0,1/4], incluidos extremos. No se seleccionan paneles por un diagnóstico de signo ni se cambia la malla después de resultados.

## 5. Resultado reproducible y conclusión

Ejecutar

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_compact_073_verify.py

La corrida única autorizada terminó exit0/PASS en los4096paneles. Todos los asserts son racionales; la salida imprime también los Q exactos y TAIL. El signo certificado es estricto en cada panel, por lo que prueba FOURTH uniformemente en el compacto.

Como Phi es positiva, suave y par por la identidad modular ya establecida, logPhi es par y su tercera derivada vale0 en0. Para0<t<=1/4,

    (logPhi)'''(t)=∫_0^t(logPhi)''''(s)ds<0.

Esto completa exactamente el hueco de10343. Para t>=1/4 se conserva su prueba analítica de primer modo y cola, que da(logPhi)'''<−20. Así HAZARD es global en t>0, sin modificar la fuente histórica.

## 6. Alcance de la herramienta

HAZARD es una propiedad estructural de la MISMA Phi positiva, no un signo auxiliar de otro kernel. La aplicación propuesta al argumento de dos copias y a la concavidad de un cociente de transformadas requiere su propia prueba; no se da aquí por demostrada. Tampoco la convexidad del hazard ordena por sí sola los cinco covariantes de10343§4. Este certificado no prueba W>=0, una nueva fila, todos los órdenes o una ventana temporal. El signo global permanece abierto.
