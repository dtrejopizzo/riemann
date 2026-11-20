# POWER_STATE_054 — Corte explícito para la forma completa en toda dimensión

Estado: PROVED para la región declarada; signo global OPEN. Papers intactos.

Con u=63/2, Q(s)=s/(s+u), definir

    C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n!,
    K(n)=max(10000n²,A_n·3^(4D_n+20)).

Para TODO n>=1, TODO polinomio real P no nulo de grado<n y TODO j>=K(n),

    W[Q^j P/(s+u)^n] > ||Q^j P/(s+u)^n||².

Fuente POWER_EFFECTIVE_HIGHPASS_054.md; revisión independiente aprobada en POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md. Root leyó y verificó ambas pruebas completas. No se requiere evaluar K(n), ejecutar una campaña numérica ni verificar casos individuales.

## Mecanismo nuevo y alcance exacto

POWER_INVERSE_COEFFICIENT_054 y su auditoría establecen una cota efectiva de coeficientes al invertir y reescalar frecuencia. Un intervalo fijo y la expansión de Legendre sustituyen el menor eigenvalor de Gram no cuantificado de015. La constante depende de n y cubre todos los numeradores simultáneamente.

El contorno de la densidad completa tiene integral absoluta <=D_n veces la norma espectral. La prueba conserva el producto polinómico completo, aplica017 a diagonales positivas y justifica separadamente dimensión1. Los momentos beta exactos controlan las constantes; la autocorrelación queda acotada por D_n exp(-15|t|)norma². Esto paga TODOS los contactos aritméticos mediante una serie absolutamente convergente.

El momento inverso es <=A_n/(u²j). DesdeK(n), ARCH>2D_n+9, el módulo del peine<D_n y el módulo del polar<1, todos divididos por la misma norma². El balance prueba el resultado con margen.

Es una mejora efectiva de la eventualidad015: ahora existe una fórmula universal explícita en n. Su tamaño es enorme y no se afirma optimalidad. No prueba los segmentos j<K(n), no demuestra que esta región positiva sea densa en el portador requerido y no amplía la ventana temporalT. La positividad en trece polos arbitrarios053 sigue vigente separadamente.

## Propuestas descartadas por duplicación y obligación viva

La extrapolación absoluta de momentos053 reproduce el obstáculo016. Renombrar como energía negativa el resto pendiente reproduce036; la cola renormalizada042 no resuelve su interior ni uniformidad en k. No son nuevos NO-GO. El control temporal ponderado independiente de n tampoco se supone.

El paso pendiente hacia el objetivo general requiere controlar el segmento inicial al variar n conservando su aritmética firmada. El corte efectivo no autoriza eliminar ese segmento por recurrencia ni por masa pequeña. No hay bloqueo externo ni cierre del goal.
