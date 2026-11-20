# Estado 052 — V13 confluyente completo y signo real del pivote

POWER_CONFLUENT_THIRTEEN_052 prueba, con auditoría independiente aprobada, que

    W[f] > ||f||²/4000

para TODOS los numeradores reales propios en V13={P(s)/(s+63/2)^13}. Se mantienen todos los términos cruzados, el polar y todos los contactos aritméticos. Es una ampliación del bloque confluyente; no se ha probado todavía trece polos arbitrarios. El resultado050 de doce polos arbitrarios sigue vigente.

## Información del caso que orienta el siguiente paso

El pivote de Schur complementario a la restricción F(0)=0 queda positivamente encerrado para la forma COMPLETA, entre0.0003 y0.0005. No se dedujo su signo de la positividad de esa restricción: se cuantificó el acoplamiento real.

E2 ya es positiva sobreV13, pero su cota de cola absoluta desde3 no alcanza para certificarW. Conservar exactamente el contacto3 permite pagar la cola desde4 por menos de0.00001 veces la norma². E23>0.00028 norma², suficiente para el margen declarado.

El contacto3 es adverso en el pivote: lo reduce de aproximadamente0.00040545 a0.00038348, con intervalos racionales certificados. En la dirección racional elegida por el Schur central deE2, contacto2 también es adverso y casi cancela el beneficio deARCH+POLAR. Estas energías se evalúan en un único vector de complemento fijo, no se confunden con cocientes de Rayleigh de norma1. Que2 repare otras direcciones no autoriza atribuirle signo favorable en ésta.

Este dato descarta usar un patrón de mejora por cada contacto añadido. El certificado mejora al conservar3 exactamente porque evita una pérdida excesiva de la cota absoluta, no porque ese contacto añada energía positiva.

## Verificación y alcance

POWER_CONFLUENT_THIRTEEN_AUDIT_052 aprueba la prueba. El script tools/power_confluent_thirteen_052_verify.py emplea fracciones, intervalos de constantes con restos y LDL; encierra los pivotes mediante orden de formas, preservando todos sus cruces. Constructor, auditor y root reprodujeron PASS. Se estudió un solo bloque nuevo, no una campaña de dimensiones o tasas.

La búsqueda paralela de una norma ponderada uniforme en j para toda Q^jV_n no produjo una nueva cota: los bounds monomiales no controlan automáticamente la Gram mixta, y la traza deV_n no se traslada sin prueba a la órbita. No se declara una imposibilidad general.

Siguen abiertos trece polos arbitrarios, los órdenes generales y el signo global. No hay una nueva ventana T del Paper47; papers intactos y goal activo.
