# POWER WEIGHTED AUDIT 031

Estado: WEIGHTED_BLOCK031 y GAMMA_WEIGHT031 APROBADOS. Papers intactos.

## 1. Corpus y diferencia

Se mantienen los antecedentes auditados030 y las restricciones del índice/grid/crucigrama: JOINT-G e integración de escalones son identidades; primitivas de H sin peso ya fallaron030. La novedad requerida es una desigualdad contra G_N real que conserve aritmética y compare lesiones con recuperaciones, no sólo otro test de signo de un peso abstracto.

## 2. Bloque ponderado y recuperación — APROBADOS

Revisados `POWER_WEIGHTED_BLOCK_031.md` y `tools/power_weighted_block_031_verify.py`; ejecución independiente PASS. La fórmula de I*(X) incorpora todos los escalones con factores−2Λ(q)/√q+2X^−3/2qΛ(q). Si q=X sus dos términos cancelan; el contacto4 no tiene contribución integral en el extremo4. Sólo q2,q3 contribuyen a los extremos declarados.

La fórmula general de J(X), con z=√X y arctan((z−1)/(z+1)), resulta de la primitiva verificada030. Las cotas de√2 y√3 y sus recíprocos conservan correctamente las direcciones de las evaluaciones superior/inferior. Los intervalos exactos certifican I*(225/64)<−.004 e I*(4)>.02.

El error gamma local satisface |G_N−G*|<3M2 en[1,4], porque log4<1.4 y(3/4)(1.4)²+1.4<3. El mayorante de∫|H|<10 incluye longitud, constante, singularidad y ambos contactos. Por tanto el error30M2 y los umbrales N≥2^22 y N≥2^24 están certificados uniformemente, sin barrido de órdenes.

Quedan aprobados los tres resultados REALES a u31.5 fijo: prefijo hasta225/64<−.003 para N≥2^24; bloque hasta4>.015 para N≥2^22; recuperación entre esos extremos>.018 para N≥2^24. La última se obtiene restando sobre la misma función G_N, no combinando modelos o truncamientos distintos.

La negatividad del prefijo ponderado refuta I*≥0 universal, pero no W. El bloque ampliado muestra compensación interior cuantitativa real y es distinto de repetir las primitivas sin peso030. Falta controlar todo[4,infinito); no se reemplaza por una cola de otra representación ni se certifica una nueva ventana T.


## 3. Factor gamma real y costo inicial — APROBADOS

Revisado `POWER_GAMMA_WEIGHT_031.md`. La estricta logconcavidad de D implica un único máximo de R=e^−utD/(3/2), pues la logderivada inicial es positiva y su límite es−u. Reutilizar Jensen026 con umbral u da exactamente t0=(2/3)d/(d+20), con ut0<d para d≥2. El caso d1 tiene el máximo afín1/33. No se introduce un nuevo supuesto de monotonía desde el origen.

La prueba global q″<0 es válida: en todo cero de q″, la Riccati y su derivada dan q‴=2(q′)²+4qq′/t>0. La asintótica q″<0 al infinito impide un cruce descendente desde un valor no negativo anterior y excluye contactos. La concavidad y q(0)=0 implican∫_0^Tq≥Tq(T)/2.

En la rama creciente el paréntesis cq′−q−cq² es positivo; por eso reemplazarρ≤1 antes de descartar−cq² conserva la dirección del bound de R′. Integrar produce el sobrepaso≤q(T)(c−T/2)≤M2T(c−T/2)≤2M2/9. La TV resultante conserva ambas ramas reales.

La integración por partes global no tiene borde: I*(1)=0 y el decaimiento gamma domina su crecimiento. La singularidad inicial es integrable. La rama creciente termina antes de log2, así que no contiene contacto primo. La cota superior de I* en esa rama es<9/2, usando el signo de c0−1 y el integral exacto del logaritmo. Multiplicada por la variación positiva≤2M2/9, deja un costo adverso≤M2. BUDGET conserva toda la primitiva firmada contra el peso positivo−R′ de la rama restante.

El criterio de esperanza indicado es suficiente pero sigue sin prueba. No se transforma el peso positivo en signo del promedio, porque I* sí tiene lesiones reales. La diferencia respecto030 es un control cuantitativo de variación TOTAL del factor gamma y del costo de su rama inicial, de orden1/N; no una nueva escritura de IBP como signo.

## 4. Cierre

La ronda añade compensación real hasta4 y un presupuesto global de rama inicial, ambos a tasa fija y sin campaña de órdenes. Ni sumarlos ni la medida positiva de la rama descendente resuelven automáticamente todos los contactos restantes. No hay signo total W, nueva fila completa o ventana T certificada. Los resultados negativos de primitivas sólo delimitan criterios suficientes, no una imposibilidad global. Root coincide independientemente en la revisión de WEIGHTED_BLOCK031 y en la localización del máximo por Jensen.

Aclaración final de la rama creciente: también R′=cρq′−qR≤cq′−q porqueρ≤1, q′>0 y R≥R(0)=1. Esta formulación, explicitada por el constructor a petición de root, conserva de manera directa la dirección de la cota del sobrepaso y está aprobada.
