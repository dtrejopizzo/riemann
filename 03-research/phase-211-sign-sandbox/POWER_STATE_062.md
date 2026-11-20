# POWER_STATE_062 — Residuo indispensable en el mismo caso129

Estado: diagnóstico cuantitativo PROVED; ninguna nueva región de signo. Objetivo global OPEN. Papers intactos.

Se evaluó el balance renormalizado042 en el MISMO átomo129 ya decidido061. Con normalización por norma², beta=log(2pi)−1−gamma,

    AFF=ARCHsharp+2gamma−beta J129(1),
    R=(ERR+2gamma−beta J129(1))/2,
    W/norma²=AFF−2R.

Los intervalos racionales auditados son

    AFF ∈[−60446492280,−60446492279]/10^12,
    R ∈[−30223246208,−30223246207]/10^12.

La parte afín tiene déficit aproximado.06044649228; el residuo completo lo repara casi exactamente. Por tanto esa parte afín no sirve como una base positiva desde la cual simplemente despreciar el resto. R incluye término periódicoB1 YerrorEuler; no se asigna toda la reparación a uno de ellos.

Fuentes POWER_GAMMA_AFFINE_BALANCE_062.md y POWER_GAMMA_AFFINE_AUDIT_062.md. Verificador tools/power_gamma_affine_balance_062_verify.py reproducido de forma independiente, exit0/PASS. Reutiliza024 y061 sin nuevosN, cortes o precisiones. No usa ABS-TAIL042, que exigeN>=2^80.

El R aquí calculado usaERR061 ya conocido: NO es una nueva estimación independiente capaz de propagar el signo. El pequeño margenW mantiene la prueba061 y no se infiere de redondeos independientes deAFF/R. La comparación de diferencias enN deJ,K yARCHsharp sigue pendiente; Kpositivoexterior yqconcava no ordenan esos términos. Los reagrupamientos024/026/030/042 no se cuentan como nuevas herramientas.

## Consulta063 — integración directa revisada y deduplicada

Casos revisó la propuesta de acotarR directamente por celdas; root comprobó las identidades de divisores. Para U=B+gamma floor(x)+gamma/2−kappa, R=integral hU y el borde esJ(1)(3gamma/2−kappa). Integrar por partes conserva dU=−H_floor(x)dx+sum_(m>=2)(logm+gamma)delta_m. La identidad sum_(m<=y)mu(m)H_floor(y/m)/m=1 sigue de mu*1=delta; conJ=sum mu(m)w(mx), devuelve integralH_floor J=integralw. Asimismo sum logm J(m)=sum Lambda(m)w(m). MASS elimina la suma restante deJ.

Así la evaluación directa reconstruye los mismos contactos, resolvente yJ1 ya utilizados en061/062. No se ejecutó otra implementación ni se obtuvo una cota independiente deR. La vía factorial/Stirling fue revisada por insight048 y también vuelve a030/042 o a los componentesErlang033; no apareció una hipótesis nueva que evite sus pérdidas. Son deduplicaciones de propuestas concretas, no pruebas de imposibilidad general ni nuevos resultados de signo.
