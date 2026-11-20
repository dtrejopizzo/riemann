# POWER_STATE_053 — Transporte completo a trece polos

Estado: PROVED para la familia declarada; signo general OPEN. Papers intactos.

Para todo polinomio real no nulo P de grado menor que13 y cualesquiera tasas reales v_i>=63/2, incluidas repeticiones,

    W[P/prod_i(s+v_i)] > ||P/prod_i(s+v_i)||²/4000.

Referencia: POWER_FULL_THIRTEEN_053.md. Resultado auxiliar: catorce polos con numerador D de grado<14 y D(0)=0 tienen W>norma²/1000. Es cero de la transformada en s=0, no un valor temporal en el origen.

## Evidencia y mecanismo

CENTERED_MOMENT_053 y su auditoría prueban E23[Q^j F]>norma²/10 para todo F en V13 y j>=96 mediante un único momento exacto y monotonía por covarianza. El segmento restante j=1,...,95 satisface E23>norma²/500: 95 certificados LDL racionales, con errores exteriores y error de operador pagado contra la matriz Gram. Constructor, auditor mapa y root reprodujeron el verificador completo con exit0 y todos los PASS. Root reprodujo también el verificador de momento.

MULTI015 transfiere la órbita completa a catorce polos con numerador cero. La cola aritmética completa desde4 tiene norma<1/1000 por la traza B_T14=947334302964. FULLTEL014 conserva forma, norma, polar y aritmética y transfiere el margen del bloque confluyente13 de052 a todos los trece polos.

La corrida inicial era lenta por denominadores gigantes en logaritmos exactos. Se sustituyó su evaluación por intervalos racionales exteriores en cada operación, conservando 512 términos, precisión260, márgenes y corte; no se relajó ninguna condición del certificado.

## Alcance pendiente

No prueba dimensión arbitraria ni catorce polos con numerador general. No establece una ventana T nueva. El signo global sigue abierto. El próximo trabajo debe buscar control uniforme del segmento inicial al variar la dimensión, no confundir positividad eventual con positividad de toda la órbita.
