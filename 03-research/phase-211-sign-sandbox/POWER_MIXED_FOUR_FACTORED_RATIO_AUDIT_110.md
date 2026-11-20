# Auditoría110 — cociente theta factorizado

## Actualización verificada: reproducción terminada y WM activada

Los logs constructor y reproducción independiente de110 son idénticos byte por byte, SHA256 `90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539`. Driver: `c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108`; los cuatro módulos importados conservan los hashes auditados. Root comprobó por fracciones exactas el origen completo (16 hojas en lambda[0,1/4]) y 4198 hojas REST contiguas desde1/2 hasta845/32 en AMBOS logs. Ambos programas terminaron INCONCLUSIVE por8192 evaluaciones; no se cambia esa etiqueta ni se afirma FULLPASS hasta64.

La cola analítica104, auditada por root/casos/mapa, prueba Wmixed/Phi^4>6t^2/y^2 para todo t>=16. Por tanto la cobertura reproducida y esa cola se solapan y prueban WM para TODO t>0. Los tres prefijos103 completan MIXED4. Queda activada la aplicación real de las implicaciones auditadas112: segunda densidad Xi positiva para todos p,q>0, E/Psi decreciente, TP2 y confluencia estrictas. Root revisó también el literal§8 y las dos fuerzas verificadas independientemente por casos: se activan las comparaciones de la pareja límite estrella. No se afirma Xi_(p,q)/E_(p,q) decreciente para parámetros finitos, cinco potencias arbitrarias, todos los órdenes ni una ventana nueva.

Las menciones posteriores a réplica pendiente o aplicación condicional describen el estado anterior a esta actualización y quedan superadas exclusivamente por esta evidencia. El signo global permanece OPEN. Véase `POWER_REASSESSMENT.md` para el cambio de estrategia.


Estado: **DISEÑO Y LITERAL APROBADOS. Constructor110 exit2/INCONCLUSO; reproducción independiente12244 en curso. WM todavía no activada.** Fuente:`POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md`.109 terminó sinFULLPASS; sus códigos siguen intactos.

Comprobadas algebraicamenteTheta16=d(1+R16),d=2y−3 y B_m=m4+3m²(m²−1)/d. El coeficiente m4 conserva el prefactor exterior m². Con y'=2y, B_m' temporal=−12ym²(m²−1)/d²; por tanto Rt y p16=2y−9/2−6/d−Rt/(1+R16) coinciden exactamente con la fórmula107. El cociente desplazado conserva el factorcomún1+2v/d sin suponer correlación favorable entreerroresdecorrecciones.

Para y en el dominio106,d≠0 y1+R16(y)≠0. EnlosdiscoscomplejosV deGaussRe(y+v)>2, porloquedshift≠0; no se requiere que laTheta delnumerador sea no nula paraholomorfía. La factorización representa las MISMAS funciones enel MISMOdominio, por tanto loserroresanalíticos106siguenpagados, ademásdelredondeointervalar. No reduceporhipótesisanchosnicostes.

Todoslosparámetros/origen109/REST107/budgets permanecenfijos.109debeterminarsinserparadoomodificado. Si109FULLPASS,110NOseejecuta; deotromodo aúnfaltalecturaliteralindependiente antescorrida. No seafirmaqueelcambioalgebraicologrePASS, signo W o cobertura adicional.

## Lectura literal final110

Leído completo`tools/power_mixed_four_factored_110_verify.py`,sinimportarlo ni ejecutar theta. Cuatrohashesguardadosantesimports; origenproxy109intacto,módulosnopatcheados. CorrecciónBm/Rt yprimerfactor1+2v/d coincidenexactamenteconeldiseño. Cache desplazado usa node.mode_exponentials[m−1] para m2..16, índice correcto delarray107queempiezaenm1. Cap5local/cap4integrales,errorescoefantesfactoriales/menor3x3con signo+ ymismosDFS/presupuestos.

109ya terminósinFULLPASS, porloquesecumple lacondiciónprevia. Literal aprobado paraunaeventualcorridacoordinadaporroot; el auditorNOlaejecutó. No se promete reducircosteniPASS.

Root confirmó lectura literal independiente yautorizó primera corrida110. Auditor no inicia réplica; no se afirmaPASS ni se modifica código.

## Reproducción independiente autorizada en curso

Root autorizó reproducción110 INTACTA mientras su constructor continúa, para contrastar la cobertura parcial con la cola analítica104 desde16. Auditor inició sesión12244; logseparado`tools/power_mixed_four_factored_110_audit.log`. Driverhashc629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108 coincide conlogconstructor. Los cuatrohashes107/108/109 coinciden.

Se conserva objetivo hasta64,presupuesto8192 yalgoritmo completo; no se detendrá al16. Estado en curso, sinpromoverPASSnireproducción completa. Tras salida se auditará la contigüidad exacta de hojas conFraction y se distinguirá cobertura parcial de estado terminal.

## Constructor terminal, réplica todavía activa

Root52878exit2/INCONCLUSIVEpor8192eval,4198hojasaceptadas,origen16/16PASS. ParseoindependientedellogconFractionconfirmahojasRESTcontiguas[1/2,845/32],longitud829/32. Siguienteintervalopendiente[845/32,3381/128],depth4; cap,no signonegativo. NoFULLPASSdelobjetivohasta64. Réplica12244sigueintacta; aúnno seactivalaaplicaciónWM/112hasta confirmar coberturaindependiente16. Hashdrivercoincidente,ycódigossinmodificar.
