# POWER_THETA_RATIO_COMPACT_077 — Dos signos locales en el intervalo restante

Estado: **PROVED/APROBADO**, corrida constructor1589 exit0/PASS y auditoría matemática/code en POWER_THETA_REMAINDER_AUDIT_077.md. Reproducción independiente root36038 terminada exit0/FULL PASS; hash del script coincidente. El signo del cociente utiliza además la prueba separada del ensamblaje. Papers y phase103 intactos.

## 1. Residuo específico y signos que se comprueban

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos073–076 y los límites de la clase genérica074. El objeto es la MISMA Phi real, V=−logPhi. Para x>0 poner

    p=V', q=V'', r=V''', s=V'''',
    C=p³+xp²q−pq−xpr+xq²,
    N=(xq−p)C'−xrC,
    C'=4p²q+2xpq²+xp²r−2pr+xqr−xps.

Las obligaciones de esta fuente son

    C(x)>0, N(x)>0 para TODO0<x<=1.                  (COMPACT)

Así L=(xq−p)/C>0 y L'=−N/C²<0 en ese intervalo. El numerador xq−p es positivo por V'''>0 de073. La fuente separada POWER_THETA_RATIO_OUTER_077.md trata x>=1 analíticamente.

La diferencia frente075/076 es comprobar DOS desigualdades locales específicas de Phi, no suponer la monotonía de un cociente integral ni volver a presentar la ODE como una prueba. Una condición de clase genérica que bastaba para dos generadores no controla estas combinaciones, como074 ya mostró.

## 2. Desingularización analítica en el origen

En0, p y r se anulan y los numeradores tienen cancelaciones de orden alto. Para x>0 definir

    P=p/x, Q=q, R=r/x,
    D=(Q−P)/x²,
    E=C/x³=QD+P³+P²Q−PR,
    U=D'/x, T=R'/x.

Estas funciones admiten extensiones pares suaves a0. Se tienen las identidades

    P'=xD, Q'=xR,
    D=∫_0^1 t²R(tx)dt,
    (E²/x)L'=P{U(P²+PQ−R)−D[3PD+2DQ+PR−T]}.        (REG)

Son identidades algebraicas, revisadas independientemente. Sea a=V''(0)>0 y b=V''''(0)>0. Si en0<=x<=1/16 se certifica

    V^(6)(x)<0, b<2a²,                              (ORIGIN-DATA)

entonces la paridad implica V^(5)(0)=0 y por ello V^(5)(x)<0 para x>0. Luego V'''' decrece y R=∫_0^1V''''(tx)dt también decrece, dando T<0. La fórmula integral de D da U<0.073 y la logconcavidad10334 dan P,Q>=a>0 y R,D>0. Además R<=b<2a²<=P²+PQ. Por tanto E=QD+P(P²+PQ−R)>0 y REG es estrictamente negativo. Esto prueba COMPACT en0<x<=1/16 a partir de datos con margen NO nulo, sin dividir intervalos por x³ o x⁷.

## 3. Modelos racionales de la suma theta y su cola completa

Escribir, como073,

    Phi(x)=pi exp(5x/2) S(x),
    S=Σ_(m>=1)m²(2y−3)exp(−y), y=pi m²exp(2x).

Con Q0(y)=2y−3 y Q_(j+1)=2y(Q_j'−Q_j), se tiene S^(j)=Σm²Q_j(y)exp(−y). El verificador genera Q0,...,Q8 con coeficientes enteros exactos. Sea A=max_(j<=8)Σ|coef Q_j|. Cada grado es<=9 y, para y>=1, |Q_j(y)|<=A y⁹.

Se retienen m=1,...,6. Para TODO0<=x<=1 y m>=7, y>=3m²>=147>9. La función y⁹exp(−y) decrece allí, y exp(3)>16 por una suma Taylor racional. Así

    m²|Q_j(y)|exp(−y)<=A·3⁹m²⁰2^(−4m²).

La razón consecutiva es<=(8/7)²⁰2^(−60)<1/2. Por tanto la cola COMPLETA de cada S^(j),j<=8, queda encerrada en[−epsilon,epsilon], con

    epsilon=2A·3⁹·7²⁰·2^(−196).                     (TAIL)

Se eligieron seis modos y esta cola ANTES de ejecutar para que la división por S cerca de x=1 no amplificara una cota uniforme demasiado gruesa. No se modifica la cola según el resultado.

Las derivadas logarítmicas se reconstruyen por la recurrencia exacta

    ell_j=[S^(j)−Σ_(k=1)^(j−1)binom(j−1,k−1)ell_k S^(j−k)]/S,
    ell_j=(logS)^(j).

Entonces p=−ell_1−5/2 y V^(j)=−ell_j para j>=2. En cada evaluación se certifica S.lower>0 antes de dividir.

## 4. Encierros elementales y las DOS mallas fijas

El script tools/power_theta_local_077_verify.py usa intervalos outward con extremos enteros sobre10^70. Pi se encierra con Machin y128 términos alternantes por arctangente, con resto explícito, como073.

Para exp(z),0<=z<=2048, se evalúa Taylor hasta grado128 en z/2048<=1 con resto[0,2/129!]; once cuadrados exteriores recuperan exp(z). El rango incluye todos los argumentos de los seis modos en[0,1]. No se usa un valor flotante como dato de prueba.

La primera malla consta de1024intervalos uniformes de[0,1/16]. Si m es el centro de un panel de radio h, se encierra V^(6) por

    V6(m)+[-h,h]V7(m)+[0,h²/2]V8(panel).              (TAYLOR-V6)

El signo estricto superior negativo en todos los paneles, junto con los asserts racionales a,b>0 y2a²>b en0, certifica ORIGIN-DATA.

La segunda malla consta de8192intervalos uniformes de[1/16,1]. En cada panel se evalúan C,N y sus primeras derivadas en el CENTRO puntual, no se ignoran las cancelaciones tratando el valor final como una suma de términos absolutos. Las identidades simplificadas son

    N'=(xq−p)C''−(r+xV4)C,
    N''=xrC''+(xq−p)C'''−(2V4+xV5)C−(r+xV4)C'.

C,C',C'',C''' se calculan por jets de derivadas hasta orden3, con la regla del producto binomial; sólo requieren V hasta orden6. Se encierran en todo el panel

    Cwhole=C(m)+[-h,h]C'(m)+[0,h²/2]C''(panel),
    Nwhole=N(m)+[-h,h]N'(m)+[0,h²/2]N''(panel).        (TAYLOR-CN)

Los asserts son Cwhole.lower>0 y Nwhole.lower>0. Las mallas y los signos estrictos son fijos, no elegidos por un barrido de parámetros.

## 5. Historia del encierro y reproducibilidad

La primera implementación intentó encerrar V6 por evaluación directa del log-jet sobre el primer panel. Produjo un intervalo con extremo superior positivo, aunque el diagnóstico puntual era negativo. Ese FAIL era falta de dependencia, no un contraejemplo a ORIGIN-DATA; no se promovió como cambio de signo. Se conservan exactamente1024/8192paneles, dominios y márgenes, pero se reemplaza el encierro directo por los modelos Taylor de segundo orden anteriores, con sus derivadas y colas adicionales justificadas. Un error de edición relanzó accidentalmente ese mismo assert antiguo y repitió el FAIL inmediato antes de corregir el archivo; no fue otra selección de parámetros.

La corrida del certificado corregido es

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_local_077_verify.py

La corrida corregida1589 terminó exit0 y produjo PASS para ORIGIN-DATA y para C>0,N>0 en los8192paneles restantes. Esto prueba COMPACT completo, sin muestras ni flotantes. La cola racional impresa fue

    epsilon=42965568563849534658039831/98079714615416886934934209737619787751599303819750539264.

El SHA256 del verificador exacto reproducible es

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

No se modificó el script durante su corrida; el hash fija la versión que terminó PASS.

## 6. Alcance y conexión

COMPACT y OUTER, ambos auditados, proporcionan C>0,L'<0,L(infinito)=0 para la Phi REAL. La prueba separada POWER_THETA_REMAINDER_077 y su auditoría integran el cociente de colas y concluyenG_u(z)>0 parau,z>0; este certificado local no lo obtiene por sí solo. No se infiere un kernel Schur de orden dos positivo, tres generadores, todos los órdenes o una nueva ventana temporal. No se optimiza una constante auxiliar ni se evalúan matrices de dimensiones crecientes.
