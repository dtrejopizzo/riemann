# POWER_POST013_CONSTRAINTS_014 — Condiciones de una continuación firmada

Estado: auditoría de alcance y requisitos concretos; no cierra ninguna ruta por ser reformulación. Papers intactos.

## 1. Lo que realmente dice el cálculo de operadores registrado

Leídos Paper47 prop:opcalc (líneas8419 y siguientes), lem:shape-lin, phase188/N_BUILD_018_LINEAR_CENTRE_REDUCES_TO_OMEGA_MU.md, índice y los memos de filtros004–013. La proposición de operadores muestra que identidades de convolución son identidades lineales en la autocorrelación; por sí solas no suministran un signo nuevo. Expresamente cubre operadores de convolución. No clasifica ni excluye toda desigualdad que conserve una medida espectral restringida a numeradores racionales, los términos positivos de frecuencia o un acoplamiento exacto con el polar.

Los filtros racionales presentes son convoluciones causales de delta y núcleos exponenciales integrables. Su identidad de transporte sí pertenece al lenguaje de opcalc. Lo nuevo debe estar en la desigualdad que se prueba DESPUÉS: afirmar de nuevo la identidad, aplicar Cauchy--Schwarz sin una ganancia demostrada, o reescribir el peine con Euler no proporciona ese paso. Los cierres finitos de cuatro a siete ya demuestran por construcción por qué no se debe convertir esa observación de alcance en un NO-GO absoluto.

## 2. Qué descartó exactamente la ronda013

POWER_DEFICIT_LIMIT_013 excluye la estimación que reemplaza la pérdida por su peor envolvente puntual, independientemente de la probabilidad racional, y descarta la ganancia positiva. Sus números sólo impiden optimizar esa estimación en ocho. Conservar ganancias o las restricciones del numerador cambia una hipótesis esencial de la clase. No se descarta esa continuación por ser una representación de la misma forma.

Un desarrollo válido debe identificar con precisión:

* el subespacio de numeradores y las condiciones que preserva el mapa de polos;
* la medida espectral o el bloque firmado que se estima;
* la desigualdad uniforme sobre TODOS sus coeficientes, con su margen probado;
* la polar y el peine completos, con intercambios de sumas o límites justificados.

Los certificados finitos pueden emplearse como inputs reales de esa desigualdad; un patrón de eigenvalores o un único vector no sustituye su positividad en todo el subespacio.

## 3. Aritmética necesaria cuando crece la dimensión

Un mecanismo que sólo busque AP positiva para TODOS los grados falla en el test concreto de WITNESS006: ese vector de dimensión doce tiene AP negativa. Esto no impide usar AP para avanzar en un grado declarado, ni construir una desigualdad AP más aritmética. El certificado BLOCK007 sí cruza esa región al conservar el contacto2 con sus términos cruzados y controlar la cola.

Además WITNESS006 y su cota superior de cola prueban signo negativo cuando se borra EXCLUSIVAMENTE el contacto2. Por ello cualquier supuesto de un teorema para todos los bloques que también valga tras ese borrado no puede producir la conclusión buscada. Esta es una prueba por falsificador específico, no una clasificación de todos los argumentos. Un uso exacto de pesos o identidades aritméticas que distinga el borrado sigue siendo un objetivo legítimo.

En un filtro que incluya el peine, los cos(tau logq) no son monótonos en frecuencia. Su covarianza no adquiere signo de Lambda>=0; debe demostrarse una compensación firmada. Trabajar primero con un peine finito y pasar luego al completo requiere controlar la suma de diferencias de correlaciones; para los espacios racionales de tasas>=31.5 esa convergencia puede justificarse por exponencial por polinomio, pero no convierte la identidad en desigualdad.

## 4. Blanco suficiente más pequeño en parámetros

POWER_CONFLUENT_BRIDGE_014 prueba que basta semidefinitud de TODOS los bloques Laguerre a UNA sola tasa fija u>1/2. El puente es en H¹ ponderado que controla la forma completa, no sólo en L². Esto elimina una obligación innecesaria para un cierre: no hace falta probar todos los conjuntos arbitrarios de tasas si se logra directamente la sucesión confluente completa con todos sus términos cruzados.

Una sola cadena escalar f_n y una unión de espacios pequeños no heredan esa suficiencia. Las desigualdades de la cadena siguen siendo avances legítimos y blancos necesarios; sólo deben conservar su alcance. La identidad escalar CHAIN009 requiere una nueva estimación para su combinación aritmética firmada y no queda cerrada por las fórmulas de Euler.
