# Estado de registro — hasta siete polos arbitrarios

Estado: PROVED resultados indicados; signo de todos los órdenes OPEN. Goal activo. Ningún paper modificado.

## Avance de la ronda

El paso de confluencia a tasas arbitrarias ya no depende de monotonía AP. La identidad de filtro transporta un margen y retiene exactamente la norma nueva. Sólo se acota la pérdida en la región donde m−c es negativo y la posible pérdida polar. Una cota de traza ponderada, máxima en la confluencia por convoluciones de núcleos positivos, controla TODOS los contactos primos.

Resultados con revisión independiente y verificadores racionales ejecutados:

| Clase: tasas reales >=31.5, sin separación ni cota superior | Margen de W respecto de ||f||² | Prueba |
|---|---:|---|
| Hasta tres polos | 1/20 | POWER_POLE_MOVEMENT_004, AUDIT_004 |
| Hasta cuatro polos | 2/25 | POWER_FOUR_GLOBAL_009, FOUR_GLOBAL_AUDIT_009 |
| Hasta cinco polos | 1/100 | POWER_FIVE_GLOBAL_010, FIVE_AUDIT_010 |
| Hasta seis polos | 1/25 | POWER_SIX_GLOBAL_011, SIX_AUDIT_011 |
| Hasta siete polos | 1/500 | POWER_SEVEN_GLOBAL_012, POWER_SEVEN_AUDIT_012 y verifier PASS |

Todas las cotas son estrictas para f no nula; las constantes no fueron optimizadas y no deben compararse como fondos óptimos. Se admiten multiplicidades. Para exponentes exteriores a_i>=32, las imágenes Z de las mezclas de potencias pertenecen exactamente a estas clases. Los casos de menor dimensión se incluyen por cancelación de factores adicionales en el numerador.

POWER_COMMON_TRANSFER_010 contiene el criterio común y las cotas ponderadas. La mejora de traza NO afirma monotonía del eigenvalor máximo ponderado: usa operatornorm<=trace y monotonía de la traza. POWER_SEVEN_GLOBAL_012 cubre el déficit por 196 intervalos racionales completos, no por muestreo entre puntos.

El bloque fijo Laguerre12 de POWER_ARITHMETIC_BLOCK_007 conserva su prueba separada, W>||f||²/10000. Allí AP es indefinida y el contacto2 es necesario para reparar ciertas direcciones. NO se infiere de ese bloque signo para doce tasas arbitrarias.

## Auditoría del objetivo completo

- Caso de tres potencias: resuelto en TODO el rango propuesto a_i>=32, incluso triples desiguales.
- Puente en norma de forma: probado, incluido PW_N y cualquier test compacto mediante Möbius finito y aproximación fuerte (POWER_BRIDGE_002).
- Extensión a órdenes arbitrarios de una familia densa: no probada. Certificados de tamaño fijo no suplen este requisito.
- Cierre del signo del Paper47: no obtenido. El goal no está completo y no se editan papers.

La cadena Tate009 tiene identidad exacta W[f_n]=992^(2−n)Δ²q_n y monotonía de la parte arquimediana; su convexidad aritmética sigue abierta. Su límite es el centro crítico E0 ya registrado, no una nueva holgura asintótica. Además la familia individual no es densa: probar sólo sus diagonales no sustituye el signo de todas las combinaciones.

## Próxima decisión matemática

Auditar el límite del criterio de pérdida uniforme al llegar a ocho polos. Si falla, señalar la clase exacta de estimaciones que falla; no atribuir negatividad a W. Conservar la información positiva descartada por la cota uniforme o acoplar el peine puede ser necesario. La propiedad requerida para todos los órdenes todavía no está construida.

## Límite del método ya auditado (013)

POWER_DEFICIT_LIMIT_013 y POWER_DEFICIT_AUDIT_013 prueban que, en dimensión ocho, incluso el MEJOR déficit uniforme puntual directo no permite el transporte anterior: el margen base óptimo es <1/25 (test racional), mientras la pérdida puntual forzosa es >1/20. Esto excluye seguir afinando constantes dentro de esa clase de estimación. No prueba negatividad de AP ni W, ni excluye conservar la ganancia espectral positiva o usar restricciones de las funciones racionales.

La siguiente ronda conserva la integral firmada del filtro y explora su descomposición en formas sobre numeradores con un cero adicional. Esa construcción todavía está en desarrollo; no forma parte de los resultados PROVED de este estado.
