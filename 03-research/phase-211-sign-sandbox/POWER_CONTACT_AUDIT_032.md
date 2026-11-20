# POWER CONTACT AUDIT 032

Estado: ARCH_EXACT032 y CONTACT_DECISION032 APROBADOS. Papers intactos.

## 1. Corpus y razón nueva

Reconsultados ROUTES-TRIED-INDEX/README, grid R162_2300 y CROSSWORD-TO-D, entradas021. Aquel diagnóstico mantuvo NUMÉRICO el parcial hasta300≈−6.08e−14; no había intervalo de W ni error certificado de cuadratura.032 decide exactamente el MISMO átomo N211,k1,u31.5, reemplazando ARCH por un intervalo analítico y conservando toda la cola. No es una campaña de órdenes ni una extrapolación de signos parciales.

## 2. ARCH exacta — APROBADA

Revisados `POWER_ARCH_EXACT_032.md` y `tools/power_arch_exact_032_verify.py`. La integración del kernel geométrico deψ contra los coeficientes positivos de rho produce A0=a−Σb_j S_(j+1), con b_j=p_jj!/2^j y el factor correcto de Hurwitz. Derivar la suma FINITA mediante GAIN da A1=a+(u/2)S2−Σ(j+1)b_j[S_(j+1)−(u/2)S_(j+2)]. Los corchetes son positivos porque x16>u/2.

EM8 con corte32 usa el resto integral del Bernoulli periódico16. Su supremo está acotado por|B16| mediante la serie Fourier absoluta; integrar reduce el bound exactamente al término E_p declarado. Es válido para todos p2..212 sin exigir decrecimiento de la expansión ni signo de un término siguiente. Los extremos Hurwitz se conservan como Fraction antes de multiplicarlos por b_j; el redondeo exterior se hace después. El ancho final<10^−18 y la envolvente impresa están correctamente certificados.

## 3. Contactos, polar y cola — APROBADOS

Revisados `POWER_CONTACT_DECISION_032.md`, `tools/power_contact_decision_032_contacts.py` y el verificador principal. La norma beta, polar exacto y normalización K/r_j coinciden con019–021. La enumeración determinista incluye TODOS los primos y sus potencias≤512. Para cada q=p^a se usa log p, no log q. El factor q^−32 combina exactamente el peso q^−1/2 y la autocorrelación e^−u log q.

Horner en potencias divididas conserva r(x)=Σa_jx^j/j! mediante v_j=a_j+xv_(j+1)/(j+1). La división por q^32 se aplica primero a extremos racionales; evita redondear un recíproco pequeño antes de multiplicarlo. El ancho del peine finito<10^−40 se comprueba, sin suponer que concordancia decimal certifique error.

Todos los contactos omitidos son positivos por el teorema analítico019 y su umbral211. La cota superior cubre la cola COMPLETA q>512: suma unimodal≤integral+sup, derivada logarítmica≥−32/512 e integral recurrente positiva dan el factor1+32/512. Usar coeficientes absolutos yΛ≤log q conserva la dirección. La recurrencia es la misma ya auditada021 y no depende de una cuadratura ni de un signo de prefijo.

## 4. Decisión independiente y alcance

Ejecutado independientemente `python3 tools/power_contact_decision_032_verify.py` desde su ruta phase211: PASS. Se importan directamente los intervalos internos de ARCH, peine y polar y el mayorante racional de toda la cola. El extremo inferior del parcial certificado>3.4·10^−15 y el superior más cola<4.5·10^−15 prueban

3.4·10^−15 < W[f]/||f||² < 4.5·10^−15.

El punto candidato es POSITIVO. La suma parcial negativa hasta300 era compatible con la cola favorable omitida y no es evidencia de W negativo. No se atribuye ese cambio al minúsculo error del diagnóstico ARCH.

El resultado decide un único átomo; no prueba una fila, un vecindario, parámetros próximos ni nueva ventana T. La fórmula estable de ARCH sí es general, pero aquí sólo se certificó el punto autorizado. No se modifica ningún paper ni se usa información de ceros/equivalencias.
