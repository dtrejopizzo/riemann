# Auditoría109 — intersección analítica de coeficientes

Estado: **DISEÑO Y LITERAL APROBADOS; constructor root52183 terminó exit2/INCONCLUSO. No reproducción independiente109.** Fuente:`POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md`. Consultas107/108 y tres índices conservadas; no nueva evaluación theta.

Cauchy en radio lambda1/2, con funciones holomorfas en entorno del disco ybounds107, da|phi_k|<=2^(40+k),|J_k|,|K_k|<=2^(42+k). La intersección entre estas cajas exactas ylas bolas del builder107 conserva el coeficiente verdadero. No selecciona midpointni presupone una única causa del ancho observado108.

Debe aplicarse aTODOSlos coeficientes BASE0..512, incluidos loserroresde modos/momentos/a, y reconstruir derivadas yQ desdeesas bases. Las cajas de J,K pueden manejarse independientemente: el determinante intervalar sigue conteniendo los coeficientes verdaderos coherentes. El bound de resto2^-200 de108 se conserva porque funciones ytruncamiento no cambian. No se exige correlación favorable de errores.

Se revisó el docstring localde arb.intersection: devuelveuna bola que contiene la intersección; conencierrosno solapados lanzaValueError. La bola exterior puede redondearse ligeramente fuera del intervalo intersección y no debe rechazarse por una falsa exigencia de inclusiónexacta de su redondeo. Una intersección vacía es BUG/INCONCLUSIVE, no signo matemático negativo. Loscódigos107/108 permanecen intactos yse verificaránhashes antesimportar.

Presupuestos ycriteriosfijos108conservados; ningúnsignonuevoseafirma. Faltalecturaliteral delwrapper antescorrida, nosegeneróningúndatoenestaauditoría.

## Literal109

Leído completo`tools/power_mixed_four_cauchy_109_verify.py`. Los tres hashes107/108 se comprueban antesimportar. El proxySimpleNamespace suministra exactamente laAPIusadapor108 yno modificaobjetos niarchivos originales. El builder107se ejecutaráconlosmismosinputs/parámetros,y sóloseintersectanloscoeficientesBASEK/J/phi conexponentes42/42/40+kantesreconstruirderivadas. Si unpolinomio tienegrado menor, sólo seomiten ceros exactamente representados por laAPI, no coeficientes inciertos.

No se selecciona midpoint ni se supone que el ball exterior deintersecciónestécontenidoexactamenteenlacaja porredondeo. Último cambio previo a datos revisado: intersección vacía lanza ValueError con name[k]; main lo captura, imprime INCONCLUSIVE109 construction error y termina exit2. No se confunde con NEGATIVE/exit1. El algoritmo108derivaQyformadeterminantecompleto,condicionandoREST107aPASSorigen. Revisiónliteralaprobada, sin evaluar theta. Root coordinaunúnicoproceso.

## Estado histórico provisional del constructor

Root52183 está en curso según confirmación del root. El origen pasó16/16celdaslambda[0,1/4], yREST sigue activo. Logroot yhashdriver c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba guardados. No se afirmaFULLPASS ni se ejecuta réplica todavía. LosformatosdecimalesgroserosdeArb no reemplazan el guard value>0 sobrelabola binaria. Código/presupuesto intactos. Falta exitreal antes de resultadofinal/registroíndices.

## Auditoría del resultado final109

Root52183 terminóexit2/INCONCLUSIVE por8192evaluacionesREST;4113hojasaceptadas. El origenPASS16/16esresultadoconstructor,noindependientementereproducido. Se auditóelLOGsinrecalcularfunciones:4113intervalosaceptadoscontiguos,sumalongitudesFraction2389/512,extremosREST[1/2,2645/512]. Celda siguiente[2645/512,1323/256],depth6,noevaluada porcap. No parada porprofundidadniballcontrariosigno. El resto deldominio permanece sincertificar.

Driverhashc3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba y107/108intactos. NoafirmaciónFULLPASSnireproducción109. NingúnnuevoW/globalnimatemáticanegativa. Elresultadoesinsuficienciadelpresupuesto fijo enesta representación, noobstrucciónglobal.
