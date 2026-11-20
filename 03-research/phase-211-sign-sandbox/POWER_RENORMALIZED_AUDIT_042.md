# POWER RENORMALIZED AUDIT 042

Estado: RENORMALIZED_TAIL042 APROBADO. Papers intactos.

## 1. Corpus y diferencia

Reconsultados índice, grid y crucigrama y los antecedentes MASS022, ARCH_CELL026 y SAWTOOTH041. La masa y la integración celular son conocidas. La diferencia042 es un bound ABSOLUTO exponencialmente pequeño del residuo renormalizado posterior al mismo corte energético040. No es otra banda favorable de escalaC_N ni una identidad presentada como signo de W.

## 2. Renormalización global — APROBADA

Revisados `POWER_RENORMALIZED_TAIL_042.md` y `tools/power_renormalized_tail_042_verify.py`; ejecución independiente PASS. En cada celda, integrarB1J′ incluye los dos semibordes y el salto periódico. Al sumar se obtiene∫J=1−J(1)/2+∫B1h. Integrar−xJ′ conserva el borde inferiorJ(1), dando∫xh=1+J(1)/2+∫B1h. Los bordes infinitos se anulan y las series/integrales son absolutos paraN fijo, sin sigma1 crítico.

Sustituir SAWTOOTH produce exactamente F/2=−γ+(κ−γ/2)J(1)+R. La constanteκ y el términoJ(1) no se descartan. La identidad W=ARCH_sharp+2γ−(2κ−γ)J(1)−2R conserva todos los términos reales.

## 3. Decaimiento del inverso y borde de cola — APROBADOS

El corte040 implica q(T)>.5+2000/N y q crece. Por ello la suma completaΣm^−1/2rho(t+logm) está dominada por rho(t)(1+N/2000)<N rho(t)/1000. El bound se usa DESPUÉS de eliminar el afín, no como una cancelación crítica no justificada.

Los factores g≤32rho y|g′−1.5g|<1100rho son correctos. Al derivar h=Σμm·mH(mx), aparece m²H′ y queda de nuevo el peso m^−1/2; no falta un jacobiano. Las series de derivadas convergen con el mismo mayorante en la cola. Se obtienen|h|≤Nx^−3/2 y|h′|≤2Nx^−5/2, sin presumir signo deh′.

La primitivaQ2 es continua en enteros. Integrar−hVB1, V=logx+γ, deja el borde INFERIOR+h(X)V(X)Q2(X) y la integral de(h′V+h/x)Q2. El borde infinito se anula. El errorE se conserva en módulo≤1/x, sin signo favorable supuesto.

Los integrales explícitos producen exactamente NX^−3/2[(7/48)(T+1)+55/72]. El mayoranteN(T+2)e^−3T/2 es correcto. ComoT>N/992,T+2<N yN²<e^(N/2000), la diferencia3/1984−1/2000>1/1000 demuestra|R_tail|<e^−N/1000 para TODOSN≥2^80.

## 4. Alcance

La cola residual queda controlada en escala absoluta con todos los bordes, saltos y divisores. El restante interiorRENORMALIZADO y su balance conARCH_sharp,J(1) no se han decidido. La identidad global y el error exponencial no equivalen a un margen positivo de W; tampoco se suma sin contabilidad el beneficioC_N de041. No hay nueva coberturaW o ventanaT ni modificación de papers.

Root revisó independientemente el memo completo y reprodujo el verificador PASS, coincidiendo en MASS, normalizaciones, derivadas, bordeX, coeficientes y escala exponencial absoluta. La revisión queda finalizada.
