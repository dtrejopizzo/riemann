# POWER_SELBERG_DROP_OBSTRUCTION_067 — El término positivo Selberg no se puede descartar en el caso129

Estado: **PROVED/APROBADO**, revisión independiente en POWER_SELBERG_DROP_AUDIT_067.md. Obstrucción al criterio específico de055; NO contraejemplo al signo de W. Papers intactos. No nuevo N, corte ni campaña numérica.

## 1. Antecedentes y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados ROUND_023_A§2.1, POWER_STATE_055, POWER_GAMMA_BALANCE_030 y POWER_GAMMA_129_DECISION_061 con su auditoría.055 ya estableció la identidad Selberg completa y advirtió que descartar su término positivo requiere un criterio más fuerte que W>=0, pero dejó explícitamente abierta la falsedad de ese criterio. Ahora061 decide W del MISMO test gamma129 con margen diminuto. Ese dato posterior permite refutar la premisa concreta, sin fabricar otro test ni volver a presentar la identidad Selberg como novedad.

## 2. Normalización y criterio exacto

Fijar u=63/2, N=129 y g(t)=t^(N−1)e^(−ut)/(N−1)! para t>0, cero para t<0. Escribir c0=||g||² y rho(t)=c_g(t)/c0. Definir las sumas escalares reales

    S=Σ_(m>=2) Λ(m)m^(−1/2)rho(logm),
    U=Σ_(m>=2) (μ*log²)(m)m^(−1/2)rho(logm)/logm,
    V=Σ_(m>=2) (Λ*Λ)(m)m^(−1/2)rho(logm)/logm.

Todas convergen absolutamente: rho(t) es e^(−ut) por un polinomio fijo de grado128, y basta acotar en valor absoluto cada coeficiente de μ*log² y Λ*Λ por m log²m, contando a lo sumo m divisores y acotando cada sumando por log²m. El factor m^(−u−1/2)=m^(-32) asegura entonces convergencia aun con ese majorante grueso. La identidad de convolución

    Λ·log + Λ*Λ = μ*log²

implica exactamente S=U−V y por tanto

    W[g]/c0 = ARCH[g]/c0 + POLAR[g]/c0 −2U+2V.       (FULL)

No se identifica un operador causal al cuadrado con una norma. Basta esta igualdad de sumas absolutamente convergentes. Como g>=0, rho>0 y V>=0. El criterio que descartaría2V es

    ARCH[g]/c0 + POLAR[g]/c0 −2U >=0,

es decir, W[g]/c0>=2V. Se prueba que ese criterio es falso aquí.

## 3. Lower independiente del término positivo

El único par de divisores2·2 da (Λ*Λ)(4)=(log2)². Por positividad de todos los sumandos,

    V >= (log2)/4 ·rho(log4).                       (PAIR)

La mezcla real030, válida para N>=2, escribe rho(t)=E exp(−Zt²), con Z=(u²/4)/G y G de ley Gamma(N−1/2,1). Su media es

    EZ=u²/[4(N−3/2)]=3969/2040<2.

Jensen para la función convexa z↦exp(−zt²) da rho(t)>=exp(−EZ·t²). Como log4<7/5,

    EZ·(log4)² <2·49/25=98/25<4.

Con e<3 se obtiene rho(log4)>exp(−4)>1/81. Además log2>2/3. Así

    2V >= (log2)/2 ·rho(log4) >1/243.               (GAIN)

Son desigualdades elementales estrictas; no se evalúa una nueva suma de contactos.

## 4. Falsificador del criterio de descarte

DECISION061, certificado racional completo con todos los contactos, establece

    0<W[g]/c0<1.35·10^(−10)=27/(2·10^11).

Usar este upper y GAIN en FULL da

    ARCH[g]/c0+POLAR[g]/c0−2U
       =W[g]/c0−2V
       <27/(2·10^11)−1/243 <−1/250.                (FAIL-DROP)

La última comparación es racional: 1/243−1/250=7/60750>27/(2·10^11). El término positivo Selberg es esencial para este criterio incluso en un test cuya forma completa ya está certificada positiva.

## 5. Calibración de una pérdida parcial aislada

Más generalmente, retener sólo la fracción1−theta del aporte2V produce el lower candidato W[g]/c0−2theta V. Para0<=theta<=1, si ese candidato fuera no negativo, necesariamente

    theta <= (W[g]/c0)/(2V)
          < [27/(2·10^11)]·243
          =6561/(2·10^11)=3.2805·10^(−8).

En particular, descartar incluso la fracción theta=10^(−7) ya hace negativo ese candidato. Esta precisión relativa necesaria se refiere únicamente a perder una fracción aislada del término positivo en ESTA descomposición y ESTE test. No excluye otra organización de Selberg ni una estimación compensada conjunta.

## 6. Alcance

Se refuta únicamente la estrategia suficiente de suprimir2V y demostrar positividad de lo que queda, aplicada al caso real129 ya existente. No se refuta la identidad Selberg, ni la posibilidad de comparar U y V conservando su cancelación, ni el signo de W. Tampoco se obtiene propagación en N, una nueva fila, ventana temporal o conclusión global. El dato útil para una siguiente comparación es cuantitativo: la ganancia que se intentaba descartar supera1/243, mientras W/c0 es menor que1.35·10^(−10). No se separan intervalos correlacionados para recertificar ese margen; se usa directamente el certificado061 aprobado.
