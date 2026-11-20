# Estado036 — Dónde permanece la energía que falta controlar

Estado: PROVED y auditado. Sustituye STATE035 como resumen de trabajo; conserva íntegramente su cobertura positiva. Goal activo, signo global OPEN, papers intactos.

## Frontera de recurrencia: el cono conocido no elimina el resto

POWER_RECURRENCE_BOUNDARY_036 prueba para cualquier entrada fija N>=18,k>=0,u=63/2 que, en la expansión diagonal de profundidad L, la contribución COMPLETA del cono k'>=10000N'^2 satisface

    0 <= C_L <= M_L(H_L+1/500) = O(log(L+2)/sqrt(L+1)) -> 0.

Los pesos beta-binomial son exactos. Un momento inverso exacto controla la masa del cono creciente; una cota arquimediana por Jensen y los bounds completos017 de peine y polar controlan su energía. El complemento cumple R_L=A_(N,k)−C_L y converge exactamente al valor inicial. La novedad frente016 es controlar TODO el cono parabólico creciente en energía de W real, no sólo un borde fijo o una probabilidad. El ejemplo ya decidido211,1 proporciona un resto real no nulo sin nuevas evaluaciones.

También se prueban pesos exactos para detener caminos al primer contacto con el cono y una masa superviviente positiva. No se atribuye a esa masa un límite de energía sin control adicional. La obstrucción concierne a omitir el resto del esquema diagonal; no prohíbe otras fronteras ni una compensación aritmética nueva.

## Ventana de energía: las dos partes reales viven en otra escala

POWER_MOVING_BALANCE_036 parte de la ley P_d exacta035, d=N−1. Aunque P_d tiene escala m~sqrt(d), las leyes obtenidas al ponderarla por la contribución polar y por el módulo del peine aritmético COMPLETO satisfacen

    m/d -> 1/32 en probabilidad.

Se demuestra mediante una inclinación positiva exacta a_m(63/62)^m, representada como mezcla binomial contra q(t)^d. El máximo de q está en1/64, su valor es3969/3968 y la probabilidad binomial allí es1/32. Cotas exponenciales explícitas y dominaciones de ambas energías reales justifican el límite. La comparación aritmética inferior usa un bound elemental de psi_Lambda, demostrado con el binomio central; no se altera ni trunca el peine.

Ambas partes tienen fase exponencial (3969/3968)^N. En cualquier prefijo m<=C sqrt(d), su energía relativa tiende a cero. Por tanto no es válido descartar esas colas por separado basándose en la concentración normativa035. La igualdad de fases NO prueba que la razón entre prime y polar tienda a1, ni controla su diferencia. La ventana del funcional firmado total continúa OPEN: una cancelación interna puede cambiarla.

## Evidencia, cobertura y siguiente obligación

POWER_FRONTIER_AUDIT_036 aprueba ambas pruebas; root las revisó independientemente. El verificador de constantes de MOVING036 fue reproducido con PASS por root y auditor; sólo verifica constantes, no sustituye los argumentos uniformes. No hubo campaña de N, primos o nuevos casos W.

No hay nueva cobertura positiva en036. Permanece el resultado035: todos los átomos de filas1..17, cualquier k>=0, a u31.5, tienen W>norma²/40; se conservan los espacios y regiones previos, incluido el cono017 y el caso211,1. No se prueban nuevas combinaciones arbitrarias ni una ventana T mayor que log(5)/2.

El siguiente paso debe conservar conjuntamente la contribución polar y aritmética antes de estimar colas, con una diferencia explícita frente a las representaciones conjuntas018/030/031. La localización036 identifica dónde falla el descarte separado; no se presenta por sí sola como un método de signo. El objetivo completo permanece abierto.
