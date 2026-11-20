# POWER_SEVEN_AUDIT_012 — Revisión del signo global en siete polos

Estado: PROVED. POWER_SEVEN_GLOBAL_012.md y tools/power_seven_global_012_verify.py revisados desde las fórmulas; script ejecutado independientemente con PASS. Papers intactos.

## 1. Matriz confluente

Las bandas AP y sus factores coinciden con el kernel y las transformaciones Laguerre previamente auditados. La fórmula compacta psi^(r)*u^r/(2r!) usada por el programa es exactamente equivalente a g^(r)*(2u)^r/r!, no pierde una potencia de dos. Las sumas16..2000 y colas integrales desde2001/2000 tienen signo y orden correctos. Las siete eliminaciones intervalares de AP-.069I tienen pivotes inferiores positivos y mantienen intactas las columnas del pivote. El certificado decide todo el bloque.

Las normas de momentos AA,BB usan siete términos y la comprobación4AA BB<1 basta para la cota polar empleada. No se extrapola esa comparación desde un grado menor.

## 2. Producto de déficit, no producto de máximos independientes

Los196 paneles de longitud1/4 cubren exactamente[0,49]. En cada uno, c-ell(x) decrece mientras el polinomio del filtro crece. El máximo del PRODUCTO queda por tanto acotado por el primer factor en el extremo izquierdo, truncado a positivo, y el segundo en el extremo derecho. Esto justifica DIRECT sobre cada intervalo completo. El lower49>.05>.01 y la monotonía de m controlan todo el exterior.

La pérdida integral es<.057R0N0, sin necesitar factor x ni cota separada K_n. El filtro sigue teniendo factor polar Bernoulli7/(4u²), con la orientación correcta. El corchete .069-.01-.057-7/(4u²) es positivo; su holgura es pequeña pero está comprobada racionalmente. De ello se obtiene AP>.01I en todos los siete polos>=u, manteniendo la norma nueva en la identidad.

## 3. Traza ponderada y factores de la cola

El lema de traza de POWER_COMMON_TRANSFER_010§6 fue revisado en su telescopaje, núcleo inverso positivo decreciente y conexión Laguerre. Su hipótesis sigma21<min v_j se satisface. La traza confluente exacta T7=176673441 y2sqrt(T7)<26600 están comprobadas. Se usa sólo operatornorm<=trace; no se asume monotonía del mayor eigenvalor de la Gram.

La correlación pierde q^-21 y el coeficiente del peine añade q^-1/2, de modo que el exponente es21.5. El factor adicional1/sqrt(q)<=1/sqrt2<5/7 está conservado por la comparación racional(7/5)^2<2. Al sumar logq*q^-21 se obtiene exactamente el mayorante2^-21[.7+1.4/20+2/20²]=31/(40*2^21). Así el coste infinito es<1/125, con todos los contactos y sin hipótesis de signo matricial.

Concluye W>.01I-.008I=.002I=1/500 I en todos los espacios declarados, incluso polos repetidos o arbitrariamente separados. Nada en este certificado implica el resultado para ocho polos o todos los grados.
