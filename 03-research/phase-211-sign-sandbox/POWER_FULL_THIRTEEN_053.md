# POWER_FULL_THIRTEEN_053 — Forma completa positiva en todos los trece polos reales ≥63/2

Estado: PROVED, segmento exhaustivo y constantes PASS; revisión independiente aprobada en POWER_FULL_THIRTEEN_AUDIT_053.md. Papers intactos.

**Teorema.** Para cualesquiera trece tasas reales v_i≥63/2, con multiplicidades permitidas, y todo polinomio real no nulo P de grado<13,

    W[P/∏_(i=1)^13(s+v_i)] > ||P/∏(s+v_i)||²/4000.

La ganancia nueva es W>norma²/1000 sobre todos los catorce polos≥63/2 con numerador cero en0. Se conservan todos los contactos aritméticos y el polar. No se afirma dimensión arbitraria ni catorce polos con numerador general.

## 1. Corpus y cambio respecto a050/052

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D, COMMON_TRANSFER010, FULLTEL014, MULTI015, CENTERED_CUTOFF049, FULL_TWELVE050 y CONFLUENT_THIRTEEN052.052 ya prueba W>norma²/4000 sobre V13 confluyente. La nueva pieza es una ganancia COMPLETA sobre catorce polos con numerador cero, que transporta ese bloque a trece polos arbitrarios. No se supone que positividad en codimensión1 implique la de todo el bloque.

El primer bloque E2[QV13] se certificó racionalmente >norma²/125, con tools/power_zero_fourteen_endpoint_053_verify.py. El mayorante de cola desde3 obtenido con la traza14 es0.0463807089, demasiado grande para ese margen; incluso el término n=3 de ESE mayorante de Cauchy excede0.036. Por tanto conservar Λ exacta sólo en n≥4 no arregla esa comparación particular. Esto no excluye otro bound del operador de correlación.

Se conserva entonces exactamente el contacto3, además del2, y se paga sólo la cola desde4. No se ha buscado una sucesión de primos o dimensiones. El corte analítico J=96 y su auditoría se obtuvieron ANTES de certificar el segmento j=1,...,95.

## 2. Cola highpass analítica, ya revisada independientemente

CENTERED_MOMENT053 prueba mediante una única matriz racional de momentos de dimensión13, en j=96, que para TODO F0∈V13 no nulo,

    E_(Q^96F0)[tau^-2] <4/19845, Q(s)=s/(s+u), u=63/2.

La reponderación por q=|Q|² y la covarianza negativa con (1−q)/q propagan este bound a TODOS j≥96 sin comprobar matrices adicionales. El mismo memo, auditado en CENTERED_MOMENT_AUDIT053, deduce

    ARCH[Q^jF0]>(12/5)||Q^jF0||².

Los dos coeficientes de contacto satisfacen v2+v3<137/60. El polar normalizado sobre esta órbita es menor que3(169/992)^j<3/5^j<1/1000. Por tanto

    E23[Q^jF0]>(1/10)||Q^jF0||², TODOS j≥96.           (TAIL-ORBIT)

E23 conserva ARCH, POLAR y los contactos2,3. La cola aritmética desde4 aún no está incluida en TAIL-ORBIT.

## 3. Certificado exacto del segmento exhaustivo

El único segmento restante es j=1,...,95, con margen fijado c=1/500. El verificador tools/power_full_thirteen_053_verify.py construye108 bandas Toeplitz E23. Utiliza intervalos racionales redondeados hacia fuera con paso10^−260; los logaritmos usan512 términos de atanh y resto geométrico positivo.

La precisión se fijó antes de la ejecución: para log3 directo, el resto es menor que2^−1022. Los512 términos se evalúan mediante intervalos outward en cada suma, producto y división; el resto se añade como intervalo positivo usando r≤1/2. El error acumulado no se identifica con un único paso de redondeo: queda propagado en los extremos y se comprueba en el bound de suma de filas antes de los LDL. Esta evaluación evita denominadores intermedios enormes sin cambiar la suma matemática ni el resto. Para grado≤107 y argumento63log3<70, un bound grueso de la derivada de los polinomios en juego es108·71^107<10^201. Este bound explica la elección amplia de precisión; la cota efectiva final se verifica directamente a partir de TODOS los extremos intervalares, sin asumir un número de dígitos conservados tras las cancelaciones. No se usa precisión flotante para decidir signos.

La ARCH usa Hurwitz desde16, suma exacta hasta CUT−1 con CUT=256, y Euler–Maclaurin con12 términos Bernoulli. El resto periódico absoluto es

    |B24|(p)_23 / [24!·256^(p+23)].

El bound del Bernoulli periódico |B24({x})|≤|B24| es el mismo usado en ARCH_EXACT032, obtenido de la serie de Fourier absolutamente convergente de B24 y su valor en0. Cada coeficiente racional de la banda multiplica los extremos EXACTOS de Hurwitz ANTES de redondearlos; así no se amplifica un redondeo previo por u^r, como ya advertía032. Gamma usa el mismo recinto Euler con resto de007. Los centros finales tienen denominador10^24 y se exige suma de errores por fila<ε=10^−12 ANTES de intentar los certificados finitos.

La compresión de Q^j se calcula sin una matriz108 densa. Para las trece coordenadas iniciales, Vandermonde da exactamente

    banda_r(C_jᵀTC_j)=Σ_(d=−j)^j binom(2j,j+d)t_|r+d|,
    banda_r(C_jᵀC_j)=binom(2j,j+r), 0≤r≤12,

con cero cuando r>j. El factor4^−j común se omite. El error de operador se paga como ε C_jᵀC_j. Para cada índice del segmento se verifica LDL racional positivo de

    C_jᵀTcC_j − (1/500+ε)C_jᵀC_j.

No se escogió un índice por autovalores flotantes; el segmento completo está determinado por TAIL-ORBIT. La corrida completa terminó exit0: PASS de108 bandas, PASS de suma de errores por fila<10^−12 ANTES de los certificados, y95 mensajes PASS, uno por cada j=1,...,95. No se relajó ningún umbral. El proceso anterior se detuvo únicamente para sustituir una evaluación exacta demasiado costosa de los logaritmos por la misma serie con intervalos por término; no había producido un fallo matemático ni se usó su salida parcial para elegir índices.

## 4. Transporte y cola aritmética completos

Los95 LDL positivos y TAIL-ORBIT prueban E23[Q^jF0]>norma²/500 para TODOS j≥1. Para cualquier numerador D=sP de grado≤13, P de grado<13,

    G0=D/(s+u)^14=QF0.

MULTI015 con CATORCE factores expresa E23 y la norma de cualquier G=D/∏_(i=1)^14(s+v_i), v_i≥u, como las mismas mezclas positivas y absolutamente convergentes de Q^kG0. Resulta E23[G]>norma²/500 uniformemente sobre todos esos espacios restringidos.

La traza010 con n=14, α=1/2 es EXACTAMENTE

    B_T14=947334302964<973312².

Por Cauchy y Λ(n)≤logn, la cola completa n≥4 satisface

    ||cola||≤2·973312 Σ_(n≥4)(logn)n^−65/4.

Usar n^−1/4≤5/7 para n≥4, log4<7/5 y primer término más integral de logx·x^−16, decreciente desde4. Resulta el racional

    L4=2·973312·(5/7)·4^−16
             [7/5+4(7/5)/15+4/225]
       =0.0005798513927...<1/1000.

Por tanto se demuestra

    W[G]>(1/500−L4)||G||²>||G||²/1000,
    TODOS14polos≥u, D(0)=0.                            (ZERO14)

FULLTEL014 con n=13 conserva exactamente forma, norma, polar y todos los contactos. Su base052 tiene W>norma²/4000 y sus correcciones G_j pertenecen a ZERO14, cuyo margen supera1/4000. Se obtiene entonces

    W[P/∏_(i=1)^13(s+v_i)]>norma²/4000,
    TODOS13polos≥u, gradoP<13.                          (TARGET)

La identidad FULLTEL usada aquí es exacta: con R0=∏u²/v_i²>0 y κ_j=(v_j²−u²)/u²·∏_(k<j)v_k²/u²≥0,

    W[F]−c||F||²=R0[(W[F0]−c||F0||²)
                         +Σ_jκ_j(W[G_j]−c||G_j||²)],
    G_j=sP/[(s+u)^(14−j)∏_(k≤j)(s+v_k)].

Cada corrección tiene catorce polos y numerador cero; su margen ZERO14 supera c=1/4000. La misma identidad conserva la norma. El primer término base052 es estrictamente positivo, por lo que TARGET es estricto incluso cuando algunas tasas coinciden con u. La convergencia de todas las series primas es absoluta para estos datos racionales con polos>1/2; no se omite un átomo ni se cambia el signo del polar.

## 5. Alcance

Se amplía V13 fijo052 a TODOS los trece polos reales≥31.5 mediante una ganancia aritmética completa de catorce polos con numerador cero. La cota del momento y la monotonía sustituyen todos los certificados j≥96, y el segmento anterior fue exhaustivo y fijado analíticamente. No se afirma dimensión arbitraria ni catorce polos con numerador general, y no se deduce aquí una nueva ventana T del Paper47. El caso siguiente necesita nuevas hipótesis verificadas; no se extrapolan los márgenes por dimensión. Papers intactos.
