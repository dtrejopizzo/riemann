# Estado de registro — ocho polos y transporte firmado

Estado: PROVED ocho polos arbitrarios y puente confluente fuerte; signo global OPEN. Goal activo. Ningún paper modificado.

## Resultado nuevo revisado

POWER_SIGNED_TRANSFER_014, revisado en POWER_SIGNED_AUDIT_014 y reproducido con tools/power_signed_transfer_014_verify.py, prueba

    W[f] > ||f||²/1000

para todo f real no nulo de Laplace P(s)/Π_(j=1)^8(s+v_j), grado P<8, v_j>=63/2. Se admiten repeticiones y cancelaciones; no hay separación mínima ni cota superior. Incluye toda mezcla de hasta ocho potencias exteriores con exponentes>=32.

## Insight que supera el límite013

El defecto de filtro conserva la ganancia positiva: (R−R0)|F0|² se descompone EXACTAMENTE en suma positiva de |G_j|². Cada G_j tiene nueve polos y un cero del numerador en s=0. El movimiento arquimediano de polos se aplica en ese mismo subespacio de numeradores; una coercividad confluente restringida>1/4 certifica el signo de toda la corrección.

Base AP8>7/200, norma polar<3/2, margen de transporte y control completo del peine por traza ponderada producen el resultado. No se contradice013: se conserva la distribución espectral y la ganancia que aquel método descartaba. No se afirma monotonía AP general.

## Puente exacto a la tarea completa

POWER_CONFLUENT_BRIDGE_014 fue revisado independientemente por casos. Para cualquier tasa fija u>1/2, TODOS los bloques span{y^k e^-uy:0<=k<N} son densos en una norma ponderada H1 que controla toda la forma. La prueba de densidad usa la transformada de Laplace de un vector H1 ortogonal, incluye el término de borde y no presupone densidad L² suficiente.

Por ello basta demostrar W>=0 en cada bloque confluente de UNA tasa, por ejemplo31.5. NO hace falta una constante positiva uniforme en N. La no negatividad de todos los bloques y continuidad fuerte bastan para pasar al límite y trasladar tests compactos a cualquier ventana.

Esto no está conseguido: el bloque fijo de dimensión doce tiene certificado separado, pero no están probados todos los tamaños posteriores. Los certificados finitos, aun universales en sus tasas, no sustituyen ese requisito.

## Identidad completa disponible y obligación restante

PRIME_TRANSFER_014 contiene la identidad de un polo, auditada en POWER_PRIME_AUDIT_014:

    W[f_v]−R0 W[f_u]=(1−R0)W[G], G(s)=sF_u(s)/(s+v).

Incluye el polar y TODOS los contactos; el generador no se declara positivo sin probar W[G]. La versión multipolo se integra en SIGNED_TRANSFER. Para cerrar todos los órdenes hará falta controlar estas correcciones con la forma completa, no sólo repetir identidades.

Una expansión geométrica y el comportamiento de iteraciones que añaden ceros en s=0 están en construcción en la ronda015. No se incluyen aquí como teoremas verificados ni se deduce signo de una mezcla cuyas componentes todavía no estén controladas.

## Auditoría del goal

Caso de tres: resuelto y ampliado hasta ocho. Puente en norma de forma: resuelto, ahora para tasa confluente única. Extensión a TODOS los órdenes: abierta. Cierre del signo del Paper47: abierto. Goal no completado ni bloqueado; queda trabajo matemático autorizado.
