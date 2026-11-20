# POWER_FIVE_AUDIT_010 — Revisión independiente del signo global de cinco polos

Estado: PROVED. POWER_FIVE_GLOBAL_010.md y tools/power_five_global_010_verify.py revisados; script ejecutado con PASS. Papers intactos.

El certificado confluente conserva las mismas bandas y momentos ya auditados. La nueva banda de orden cuatro usa las derivadas correctas y las colas integrales con orientación de signo pertinente. El centro racional, el error máximo de fila<1/200 y LDL(centroAP-39/200 I)>0 implican AP>19/100 I. La eliminación in-place no altera la columna de pivote durante la actualización. El cálculo exacto4AA BB<1 aporta |Polar|<I en todo el bloque, no sólo sobre sus vectores de base.

La aplicación del criterio de transporte usa n5,u63/2,b19/100,C1,c1/50,X81,D23. Las cotas de símbolo de FOUR009 para c1/10 siguen válidas al bajar c. El filtro se eleva a potencia cinco y la pérdida polar cambia a5/(4u²); el corchete está certificado>.03. Así AP>1/50 I para todas las cinco tasas>=u.

El peso sigma21=2u/3 tiene inicialnorm²<=3 y cada all-pass normaYoung<=7. Por tanto B5=3sum49^j=(49^5-1)/16, sin asumir ortogonalidad ponderada. La cola de correlación usa exp(-21t) y Lambda(q)<=q, dejando q^-20.5<=q^-20. Las comparaciones2sqrt(B5)<8404 y sumq^-20<=2^-20(21/19) son exactas y la pérdida resultante es<.01. En combinación con AP>.02 se obtiene W>.01 en TODOS los espacios de cinco polos reales>=31.5, sin separación, sin cota superior y permitiendo repetición de polos.

La mejora opcional de norma ponderada Fourier de POWER_COMMON_TRANSFER_010 no es necesaria para este certificado: todas las constantes utilizadas aquí están probadas con la cotaYoung original. La afirmación sigue siendo de dimensión fija, sin extensión automática a seis o todos los órdenes.
