# Estado019 — Patrón firmado de contactos, sin cierre global

Estado: PROVED resultados parciales; signo global OPEN. Goal activo. Papers intactos. Sustituye STATE018 como resumen vigente.

## Blanco y cobertura de la forma completa

Sigue vigente el puente escalar017: basta W>=0 para TODOS H_(N,k)=s^k/(s+u)^(N+k) a u31.5. Están probadas las filas N1,2,3 completas y el cono N>=2,k>=10000N². También siguen vigentes los ocho polos arbitrarios y el bloque fijo12. Esta ronda NO amplía esa cobertura de W ni certifica una ventana nueva T>log(5)/2.

La auditoría018 está completa: POWER_TABLE_AUDIT_018. Aprueba filas23, presupuesto exacto LOW_TABLE y modelo arcoseno que conserva las regiones positivas estructurales pero tiene una entrada interior negativa. Ese modelo no es W; demuestra que el descenso debe usar más información aritmética.

## Resultado firmado nuevo sobre el peine real

POWER_ARITHMETIC_DIFFERENCES_019 prueba que la autocorrelación de H_(N,1) tiene exactamente una raíz positiva simple en x=u t. Es positiva antes y negativa después. Para N>=3, sqrt(2N−3)<chi_N<(1+sqrt(8N−11))/2; los extremos N1,2 se calculan explícitamente.

Como u log2>21 para u>=31.5, TODOS los contactos aritméticos quedan después de la raíz para 1<=N<=211. Por tanto el peine COMPLETO es estrictamente positivo en esos casos. Para k0 el peine completo es estrictamente negativo para TODOS N. Así aparece una transición de signo demostrada entre k0 y k1, no una observación numérica ni una suma truncada.

La prueba usa coeficientes explícitos, Descartes y dos recurrencias elementales de polinomios Bessel inversos. La frontera única vale para TODOS N; el umbral211 se refiere sólo al corolario que sitúa todos los contactos en el lado positivo. No se deduce W>=0: ARCH y polar siguen en el balance pendiente. Root leyó la prueba y reprodujo el verificador Fraction PASS; mapa aprobó independientemente.

## Media firmada de dilataciones y límite de su inversión

POWER_SIGNED_MEAN_019 aplica la identidad conocida de divisores al kernel positivo de LOW018. B(x)=sum_(m<=x)E0(x/m)=log(floor(x)!)−xH_floor(x)+floor(x) satisface B(x)<=−(1−log2)(x−1). Integrarlo da una media aritmética de dilataciones estrictamente negativa para todos N>=2. No es la media original ERR.

La recuperación exacta exige h_N(x)=sum mu(m)mH_N(mx), con el jacobiano m. Los primeros tres términos en x1 son <-19/256 para N>=2^17. Esto refuta positividad de cada prefijo, NO el signo del inverso completo, cuyo resto está sin controlar. El agrupamiento Euler/Möbius ya existía en el corpus; el alcance específico es la media firmada y el falsificador del prefijo para este kernel.

Ambos memos fueron auditados en POWER_SIGNED_AUDIT_019. Root revisó también normalizaciones, endpoints, Fubini, constantes y el alcance del prefijo. No se hizo una campaña numérica.

## Obligación siguiente

Falta una estimación cuantitativa que combine el peine firmado con ARCH y polar a órdenes variables. El signo favorable del peine por sí solo no compensa un déficit sin medir su tamaño. No extrapolar positividad de dilataciones a ERR ni prefijos al inverso completo. La región inferior de la tabla sigue abierta y el objetivo no está completado ni bloqueado.
