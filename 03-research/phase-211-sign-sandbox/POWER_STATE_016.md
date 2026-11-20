# Estado016 — localización exacta del hueco de descenso

Estado: resultados estructurales y obstrucciones PROVED; signo global OPEN. Goal activo. Papers intactos. Sustituye STATE015 como resumen vigente.

## Lo que sigue probado

Ocho polos arbitrarios >=63/2: W>norma²/1000. Bloque confluente fijo de dimensión12: certificado separado. Puente fuerte: basta probar todos los bloques confluentes de una tasa, sin margen uniforme en dimensión. Teorema015: cada órbita Q^k V_N es uniformemente positiva para k suficientemente grande con N fijo. No están probados todos los bloques iniciales.

## Nuevo patrón exacto

POWER_DESCENT_016 prueba W[f]=W[Qf]+W[Lf], Q=s/(s+u), L=u/(s+u), con polar y peine completos. En consecuencia cada orden fijo de diferencias finitas de W[Q^k f] tiene signo alternado eventualmente. No se afirma monotonía global de Rayleigh.

El refinamiento binomial conserva la energía original. Sus pesos de norma son exactamente una mezcla de distribuciones Binomial(m,p), p=tau²/(u²+tau²), bajo la medida espectral de f. El error para observables Lipschitz es <=Lip/(2sqrt(m)). El borde con un número fijo de factores L tiene masa Y contribución energética tendientes a cero. Ese borde es precisamente lo cubierto directamente por015. La obligación de signo permanece en el interior, donde crecen juntos ambos índices.

## Por qué dos extrapolaciones no funcionan

POWER_JOINT_SCALE_016: para F=s^k/(s+u)^(N+k), Z=tau²/(u²+tau²) tiene ley Beta(k+1/2,N−1/2). Si k/N->c>0, los contactos normalizados tienden a cos(u sqrt(c)t), no necesariamente a0. Puede elegirse c en cualquier cono lineal para que el contacto2 tienda a1. No es un contraejemplo al signo completo.

La media temporal es (N−1/2)/u para TODO k, y la varianza para k>=1 es (N−1/2)[1+1/(4(k−1/2))]/u². Jensen impide uniformizar los pesos exponenciales usados015 en N, cualquiera sea el crecimiento de k. Centrar tampoco uniformiza simultáneamente los dos pesos opuestos. Quedan abiertas estimaciones que exploten cancelación y los conos de positividad mismos.

POWER_DESCENT_AUDIT_016: los ceros high-pass imponen momentos ordinarios nulos, funcionales continuos en la norma ponderada usada. Ni siquiera los datos primitivos son aproximables por esa unión: (1/4−D²)g, g compacto positivo, tiene momentos Tate nulos pero integral ordinaria positiva. Si k tiende a infinito y hay límite fuerte común, ese límite sólo puede ser0. Esto limita ese puente topológico, no toda aproximación posible.

## Falsificador de una inferencia, no de la forma real

W_4=W−4norma² conserva mezclas, particiones y positividad eventual015, pero su valor normalizado sobre e^(-63y/2) es <-1. Verificador racional tools/power_descent_016_verify.py reproducido PASS. Por tanto estructura+cola no implica signo inicial; el descenso necesita una estimación adicional sensible al multiplicador real. No se afirma que W_4 conserve los certificados iniciales de W.

## Revisión y siguiente obligación

Root revisó las identidades de DESCENT, las fórmulas completas de JOINT_SCALE y los lemas de momentos del auditor. La revisión independiente final de ambos memos está APROBADA en POWER_DESCENT_AUDIT_016 §§6–8; los lemas propios del auditor fueron revisados por root. No se utilizó una campaña numérica.

La siguiente construcción debe tratar el interior de la partición con el peine firmado completo o aportar una corrección controlada de momentos. No repetir densidad de colas, desaparición uniforme de contactos en conos lineales ni pesos exponenciales uniformes en N. La escala cuadrática espectral y los conos de signo siguen OPEN: no han sido refutados. El objetivo global no está completado ni bloqueado.
