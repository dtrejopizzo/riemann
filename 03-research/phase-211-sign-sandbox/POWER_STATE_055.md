# POWER_STATE_055 — Auditoría del descenso después del corte efectivo

Estado: auditoría de alcance, sin nuevo teorema de signo. Cobertura054/053 vigente; signo global OPEN. Papers intactos.

## El corte efectivo no basta para descender

Root y mapa cotejaron DESCENT016§5 con EFFECTIVE054. La misma forma auxiliar W4=W−4norma² conserva EXACTAMENTE DEF/BIN/MIX/MULTI/FULLTEL, pues la norma satisface sus identidades. La prueba054 obtiene W/norma²>D_n+8 para j>=K(n); por tanto W4/norma²>D_n+4>1 con EL MISMO K(n), sin modificarlo.

Sin embargo, el dato explícito de016, f(t)=exp(−63t/2) sobre t>0, tiene W/norma²<3 y W4/norma²<−1. Esto verifica que añadir el corte efectivo concreto y margen>1 a las identidades no hace válida la inferencia de signo inicial.

Es una comprobación del alcance del falsificador016 con la información nueva054, no otro NO-GO global. W4 NO es la forma del paper y NO conserva los certificados finitos positivos de053 ni la constante arquimediana original. No excluye una desigualdad que use esos datos adicionales.

## Obligación firmada en estudio

El constructor revisa el promedio031 contra el peso positivo −R_N′ en su rama descendente, cuyo costo anterior al máximo está acotado por M2=u²/(2N−3). La primitiva I_* tiene prefijos negativos y recuperaciones probadas, por lo que exigir su positividad puntual ya está refutado. Usar la forma específica del peso para acoplar regiones de ambos signos requeriría una desigualdad nueva; todavía no se ha obtenido.

La representación042 tiene cola absoluta exponencialmente pequeña, pero conserva sin resolver el interior. Renombrar ese interior o volver a su representación030 no contaría como avance. Se consultaron índice/grid/crucigrama y los resultados016,030,031,034,036,042,054 antes de continuar. No se hacen campañas numéricas ni se modifican papers.

## Resultado de la revisión del emparejamiento

Casos confirmó que el emparejamiento local del bolsillo negativo hasta225/64 con la recuperación hasta4 reproduce WEIGHTED_BLOCK031; la recombinación del residuo042 vuelve a030. No se encontró una desigualdad nueva para intervalos móviles. Esta rama no produce nuevo signo ni nuevo NO-GO.

## Comprobación adicional de identidad cuadrática

Se abrió una comprobación contra ROUND_023_A§2.1: para gamma temporal no negativa, el emparejamiento con la convolución Λ*Λ es positivo aunque el operador causal al cuadrado no sea un cuadrado de norma. Con rho la autocorrelación normalizada, integrar el parámetro de amortiguación da exactamente S=U−V, donde

    S=sum_(m>=2) Λ(m)m^(-1/2)rho(logm),
    U=sum_(m>=2) (μ*log²)(m)m^(-1/2)rho(logm)/logm,
    V=sum_(m>=2) (Λ*Λ)(m)m^(-1/2)rho(logm)/logm >=0.

Las sumas escalares convergen absolutamente por el decaimiento gamma; no se supone que el operador infinito sea acotado en L². La identidad implica W/norma²=ARCH/norma²+polar/norma²−2U+2V, pero no proporciona aún una cota del término adversoU. Es una comprobación de una propuesta, NO otro teorema de signo ni una afirmación de novedad de Selberg. Casos e insight048 revisaron la utilidad: V>=0 no controla U. Suprimir el término positivo exige W/norma²>=2V; el único par2·2 da V>=(log2)/4·rho_N(log4), que tiende a(log2)/4. Por tanto la pérdida no es un error que desaparezca conN. No se probó que ese criterio más fuerte sea falso, pero tampoco se obtuvo una cota que lo cumpla. La submultiplicatividad de rho sólo proporciona una cota superior del término cuadrático; no cierra el control requerido. Rama deduplicada sin nuevo NO-GO.

**Actualización067.** El criterio de descartar2V queda refutado en el MISMO caso129 certificado061: 2V>1/243 mientras W/norma²<1.35·10^(−10), por lo que ARCH/norma²+polar/norma²−2U<−1/250. Ver POWER_SELBERG_DROP_OBSTRUCTION_067.md y POWER_SELBERG_DROP_AUDIT_067.md (PROVED/APROBADO). El texto anterior describe el estado histórico055; ya no queda abierta la falsedad de ese criterio particular. No se refuta W ni una comparación que conserve la cancelación de U y V.

## Auditoría del candidato Turán (consulta056)

Mapa localizó un antecedente explícito en el registro046: Turán de los valores completos vuelve a momentos/determinantes sin cota aritmética nueva. La propuesta no se relanza.

Para dejar claro qué se comprobó: a_(N,k)=W[s^k/(s+u)^(N+k)] sin normalizar. El determinante a_(N,k)a_(N+2,k)−a_(N+1,k)² es exactamente la restricción de W a numeradores1,u²−s² sobre base s^k/(s+u)^(N+k+2), incluyendo polar y todos los cruces. Su signo más dos valores iniciales positivos induciría la positividad enN. Cauchy sobreW no lo demuestra sin presuponer la obligación bidimensional.

Casos no encontró una estimación nueva; separar el polar devuelve además la cadena009. No hubo campaña ni otro artefacto de identidad. W4 no se usa como falsificador de esta hipótesis, porque no conserva las anclas positivas necesarias. Esta auditoría no descarta una futura prueba aritmética del determinante.
