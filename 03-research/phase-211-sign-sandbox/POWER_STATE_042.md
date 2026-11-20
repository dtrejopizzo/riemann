# Estado042 — Cancelación global y cola residual en escala absoluta

Estado: PROVED y auditado. Sustituye STATE041 como resumen de trabajo. Goal activo, signo global OPEN, papers intactos.

## Resultado relevante para la precisión de la forma completa

POWER_RENORMALIZED_TAIL_042 utiliza la masa exacta sum_(n>=1)J_N(n)=1, h_N=−J_N′ y la expansión periódica041 para cancelar GLOBALMENTE el término afín de B. Con kappa=(log(2pi)−1)/2 se obtiene exactamente:

    F_N/2=−gamma+(kappa−gamma/2)J_N(1)+R_N,
    R_N=−int_1^infinito h_N B1({x})(logx+gamma)dx
                                      +int_1^infinito h_N E(x)dx.

Se conservan el término J_N(1), las constantes, los saltos y los bordes. La identidad sola no determina signo.

Para TODOS N>=2^80, si T=(N−1)/992+5 y X=exp(T), se prueba:

    |R_N^cola| <=N(T+2)exp(−3T/2)<exp(−N/1000).

Ésta es una cota ABSOLUTA, no relativa a la energía exponencial C_N de041. En consecuencia:

    W[g_N]/norma²=ARCH_sharp+2gamma−(2kappa−gamma)J_N(1)
                           −2R_N^interior+epsilon_N,
    |epsilon_N|<2exp(−N/1000),

con el interior real de1 aX. No se ha probado el signo de la expresión interior ni un margen que domine epsilon_N.

## Mecanismo y diferencia de alcance

Euler por celdas y MASS022 eliminan el afín sin intercambiar una integral con una serie crítica divergente. Después de esa cancelación, el corte040 implica q(T)>1/2+2000/N; la dilatación real permite controlar TODOS los divisores y las derivadas: |h(x)|<=Nx^(-3/2), |h′(x)|<=2Nx^(-5/2) en la cola.

La primitiva periódica continua de norma1/16 conserva explícitamente el borde inferior X. Junto con |E|<=1/x, produce el decaimiento absoluto declarado. No se presupone monotonía de h ni signo favorable del error periódico.

Frente041, se resuelve la escala de precisión de la cola tras cancelar globalmente el principal. No se suma el beneficio energético de otra representación ni se llama favorable al complemento entero: el interior renormalizado continúa pendiente.

## Auditoría y estado global

POWER_RENORMALIZED_AUDIT_042 aprueba toda la prueba. Root revisó normalizaciones, bordes, constantes y el paso a escala absoluta; root y auditor reprodujeron el verificador exacto: PASS. No se evaluaron nuevos casos W ni campañas de primos.

No hay nueva cobertura positiva W, combinación arbitraria ni ventana T del Paper47. Se conservan filas1..17, todos k>=0 a u31.5, y las regiones previas. El objetivo global requiere decidir el balance interior y después cubrir la tabla/portador suficiente; permanece OPEN.
