# Estado037 — Agrupación firmada con error explícito y límite del resto absoluto

Estado: PROVED y auditado. Sustituye STATE036 como resumen de trabajo; conserva la cobertura positiva035. Goal activo, signo global OPEN, papers intactos.

## Resultado sobre la aritmética real

POWER_ENERGY_GROUP_037 estudia H_N(x)=−d[x^(-1/2)rho_N(logx)]/dx, en x_N=exp((N−1)/992), centro asintótico de la energía polar. A tasa fija63/2, M_N=u²/(2N−3), prueba para todos m>=1:

    exp(−M_N[log(m)/1985+log²(m)/2])/m
       <= m H_N(mx_N)/H_N(x_N) <= (1+M_N log(m))/m.

El comportamiento crítico es1/m. Un conteo elemental de enteros libres de cuadrados y estas cotas prueban que la suma absoluta de los términos Möbius no principales supera1 para TODOS N>=2^16. Esto refuta contracción absoluta en el centro energético real, a diferencia de la región m^(-2) de033. No determina el signo de la suma firmada.

## Ganancia concreta de conservar signos antes del error

Para Q producto finito de primos, el núcleo agrupado K_(N,Q)(m) conserva exactamente como término principal U_Q/m, U_Q=prod(1−1/p). Se demuestra un error explícito mediante los dos momentos de log(b) bajo los pesos1/b de sus divisores. Una condición uniforme garantiza K_(N,Q)(m) entre U_Q/(2m) y3U_Q/(2m) en una ventana logm de orden sqrtN para Q fijo. Es signo de un núcleo auxiliar agrupado, no signo de W.

La elección creciente Q=prod_(p<=floor(N^(1/8)))p permite, para TODOS N>=2^80, error relativo<.01 en toda la ventana m<=exp(3N^(1/4)). Sin embargo una prueba por inclusión–exclusión y conteo de cuadrados muestra que la suma de módulos del resto agrupado supera1.48, mientras el grupo principal es<.505. Por tanto esta elección tampoco cierra el problema mediante dominación absoluta del resto. La suma exterior con sus signos sigue abierta.

## Alcance y evidencia

POWER_GROUP_AUDIT_037 aprueba núcleo y extensión creciente. Root revisó ambos y reprodujo el verificador exacto ampliado: PASS; auditor independiente también PASS. Se corrigió el uso de conteo entero mediante Abel discreto. Los teoremas uniformes son analíticos; no se evaluaron nuevos datos W ni se enumeraron campañas de primos o Möbius.

La novedad frente018/030/031 no es otra cancelación formal del principal: es una desigualdad cuantitativa del perfil real y de su agrupación finita. Aun así, el mayorante de error de orden log²(m)/m no puede sumarse hasta infinito. Falta controlar el complemento aritmético firmado y su integral. No se afirma que otras agrupaciones sean imposibles.

No hay nueva cobertura positiva de W ni ventana T. Se conservan filas1..17, cualquier k>=0, a u31.5 con W>norma²/40, las regiones previas y el átomo211,1. El objetivo global sigue abierto. La continuación debe aportar control firmado nuevo del complemento; mejorar sólo constantes de las mismas cotas absolutas no resuelve la obligación.
