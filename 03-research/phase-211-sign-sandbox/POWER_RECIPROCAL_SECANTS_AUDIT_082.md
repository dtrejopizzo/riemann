# POWER_RECIPROCAL_SECANTS_AUDIT_082 — Auditoría independiente

Estado: **APROBADO / PROVED como criterio algebraico.** Fuente `POWER_RECIPROCAL_SECANTS_082.md`, lectura completa; auditor mapa. Root e insight verificaron las identidades independientemente. Papers intactos.

## Comprobaciones

DET2 y RECIPROCAL se reprodujeron por simplificación racional exacta. DET3 sigue de DET079 ya reproducido en079 y la identidad RECIPROCAL; la cancelación de (u+w)² mediante (w²−u²)² produce exactamente el Vandermonde impreso, sin factor pendiente.

Para pares PD, el producto de las dos secantes R,S es positivo. Sus factores no pueden ser ambos negativos: R2<R1 y x2/R2<x1/R1 serían incompatibles con x2>x1. Así ambas secantes son estrictamente positivas, beta>0 y alpha>0. No se necesita F creciente ni alpha>beta uv.

La fórmula RECIPROCAL tiene numerador alpha beta(w²−u²)−delta_R(alpha w²+beta u²v²). Si delta_R<=0, delta_S>0. En particular el producto delta_R delta_S no negativo equivale a ambas diferencias no negativas: no se admite erróneamente el caso de ambas negativas. El mismo razonamiento cubre el caso delta_S<0 por simetría. Pares PD y diagonales positivas convierten el signo del determinante3 en PSD/PD por Schur2x2.

Los bordes delta_R=0 o delta_S=0 son rango2; no pueden anularse simultáneamente bajo pares estrictos. Nodos repetidos y vectores que representan la función nula se separan correctamente. La equivalencia para todos los triples es exactamente concavidad de R y S en el intervalo de cuadrados, sin exigir diferenciabilidad. La congruencia F↔1/F y la recuperación de079 son correctas: para M, R''=g''/a y S''=[u²M''+uM'−M]/(4u³)<0 por073.

## Novedad y alcance

Consultados los antecedentes003/074/079/081 y los tres registros. Se cambia de BASE073, que081 muestra no hereditaria por el resto REAL, a un criterio recíproco que permite funciones decrecientes. Es una condición necesaria y suficiente de orden3 en la clase de pares PD; no una prueba de sus hipótesis para G_p.

Para el resto G_p todavía se deben probar pares PD y ambas concavidades, y cualquier preservación posterior sigue abierta.077 sólo da valores positivos. No se afirma orden4, todos los órdenes, descarga compacta080, nueva cobertura W ni una ventana temporal.081 permanece válido para su clase limitada.
