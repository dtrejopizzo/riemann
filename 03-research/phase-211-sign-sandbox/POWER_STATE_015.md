# Estado 015 — mezcla completa y positividad eventual

Estado: PROVED resultados parciales; signo global OPEN. Goal activo. Papers intactos. Sustituye POWER_STATE_014 como resumen vigente.

## Resultados consolidados

Se mantiene W[f]>||f||²/1000 para todos los espacios de ocho polos reales >=63/2, con repeticiones, numerador de grado menor que ocho y todos los contactos aritméticos. Certificado racional y auditoría en POWER_SIGNED_TRANSFER_014 y POWER_SIGNED_AUDIT_014.

El puente POWER_CONFLUENT_BRIDGE_014 demuestra que basta la no negatividad de todos los bloques confluentes de una sola tasa. No exige margen uniforme en dimensión. Todos los tamaños siguen abiertos.

## Resultado general nuevo

POWER_HIGHPASS_015, revisado íntegramente en POWER_HIGHPASS_AUDIT_015: fijados u>1 y N, existe K_N tal que la forma COMPLETA es positiva en todos los subespacios Q^k V_N para k>=K_N, donde Q(s)=s/(s+u) y V_N tiene transformadas P(s)/(s+u)^N, grado P<N. La uniformidad incluye todos los numeradores, incluso dependientes de k.

La parte arquimediana normalizada es >=(log k)/2-C_N; el peine completo y el polar normalizados tienden uniformemente a cero. La prueba usa convergencia de matrices Gram reescaladas, no sólo el término dominante de un polinomio fijo. K_N no es todavía efectivo ni uniforme en N.

## Mezcla exacta

POWER_GEOMETRIC_TRANSFER_015, revisado en POWER_MIXTURE_AUDIT_015 y POWER_HIGHPASS_AUDIT_015, expresa el transporte de polos mediante una mezcla positiva de las energías W[Q^k f_base]. Incluye el polar y todos los contactos, converge absolutamente y tiene pesos de Rayleigh correctamente normalizados por las normas. La identidad finita conserva el resto sobre la función de destino.

La novedad frente al déficit puntual013 es conservar la corrección firmada completa y su estructura espectral. Frente a014, la expansión y su cola uniforme están ahora demostradas. Estas identidades no prueban por sí solas el signo aritmético.

## Obligación pendiente

Para cada N fijo queda una condición suficiente de transporte sobre un segmento finito de bloques iniciales. No se conoce aquí su extremo efectivo ni su signo para todos los N. La positividad eventual no permite inferir la positividad de esos términos iniciales ni de toda mezcla. No hay prueba global ni contraejemplo de la forma completa.

Próximo trabajo: buscar un mecanismo para controlar el segmento inicial y su dependencia en N, contrastándolo previamente con el índice y los falsificadores de alto orden007–008. No repetir una campaña de certificados finitos como sustituto de ese mecanismo.
