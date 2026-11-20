# POWER INVERSE LOGCONCAVITY AUDIT 025

Estado: APROBADO. Papers intactos.

Revisados `POWER_INVERSE_LOGCONCAVITY_025.md` y `tools/power_inverse_logconcavity_025_verify.py`; ejecución independiente PASS. El certificado de primera celda `POWER_CELL_TEST_024` y su verificador fueron revisados y reproducidos independientemente en POWER_CELL_AUDIT_024.

## 1. Logconcavidad y corte infinito

La identidad c_j=p_j(3d+30j)/(2d−j) se obtiene exactamente de D=33P−P′ y la recurrencia gamma. El cociente (j+1)c_(j+1)/c_j tiene los dos factores declarados: el primero decrece o es constante cuando d1; el segundo decrece estrictamente. El cociente final r_d=0 conserva la monotonía. Con los pesos c_jt^j/D, D′/D es la esperanza de r_j y su derivada es Cov(r_j,j)/t≤0. Esto prueba LC para todos N≥2, sin deducir de ella un signo Möbius automático.

La comparación Fraction D129′(2/3)<30D129(2/3) está certificada. LC la prolonga a todos t≥2/3; integrar el cociente logarítmico da D(t+log m)/D(t)≤m^30. La suma absoluta de TODOS m≥2 queda entonces dominada por Σm^−2≤3/4. CUT es una afirmación sobre el inverso COMPLETO. Como log2>2/3, se obtiene K129>0 en toda x≥2. No se afirma que haya una sola transición en [1,2].

## 2. Balance integrado completo

La representación J(x)=x∫_x∞K(t)t^−2dt implica J129(x)>0 para x≥2. En cada celda n≥3, LOCAL024 y K>0 dan S129(n)≥b_nJ129(n)>0. La primera celda tiene el certificado independiente S129(2)>33/100 con cola Möbius completa. La convergencia absoluta de la suma celular fue probada antes. Por tanto ERR129=−2ΣS129(n)<−33/50 sobre TODA la semirrecta. No se combina adicionalmente el beneficio C_B de esa misma celda.

## 3. Novedad y alcance

El lema de covarianza y las razones de coeficientes son herramientas clásicas. El progreso específico frente a020/023 es el corte mejorado para el kernel compensado real; frente a024, permite controlar analíticamente todas las celdas restantes y cerrar una desigualdad aritmética firmada COMPLETA en N129. La negatividad K129(1) permanece intacta.

El resultado no es W≥0: W/C0=ARCH_sharp/C0−ERR conserva una comparación cuantitativa pendiente con ARCH_sharp. Tampoco se extiende ERR<0 a todos los órdenes, a toda la tabla ni a una ventana nueva T. El certificado de la forma completa requiere ese balance adicional.
