# Estado revisado de la ruta de potencias — ronda 003

El turno anterior produjo progreso verificable: teoremas de orden finito y puente. Esta ronda certifica la familia fija hasta orden seis y refuta una inducción escalar propuesta. El goal sigue activo, sin cierre del signo.

## Resultados de registro

- POWER_BRIDGE_002 y POWER_AUDIT_002: puente completo revisado. Basta positividad de todas las matrices líderes K_ij=(L(32+i)+L(32+j))/(63+i+j). Cualquier test compacto trasladado se representa por inversión Möbius finita y se aproxima en norma de forma por la escalera fija.
- POWER_FIXED_GRID_003: todos los órdenes 1–6 certificados por intervalos racionales. El script tools/power_fixed_grid_003.py fue reejecutado por coordinación y auditor con salida coincidente. Incluye transformación Schur exacta; no supone que el patrón de seis parámetros se extienda.
- POWER_POLYNOMIAL_003: coordenadas Jacobi y dilataciones exactas; las dilataciones no son autoadjuntas ni contracciones positivas en esa métrica. Identidades, no signo uniforme.
- POWER_SCHUR_003: F(z)=(z²-z+10)/10 tiene F'>0 y F/z decreciente en [1,3]; todos sus pares pasan, pero su triple 1,2,3 tiene determinante -13/270000. Contraejemplo a preservación desde esas dos propiedades. La versión por tramos del §7 agrega concavidad y también falla. Ningún falsificador es del dato aritmético.

## Qué falta

P3 para todos A>=32,h>0 no está demostrado: hay un rango alto y el caso exacto A32,h1 (incluido en seis potencias). Tampoco hay control uniforme en orden. El puente sí está resuelto. La unión de rangos altos u>=2^{40n} no es densa, con prueba cuantitativa de concentración: no extrapolar esa familia.

## Próximo ensayo autorizado

Atacar el caso confluente (h→0) con una base estable de exponenciales por polinomios y auditar si mover las tasas hacia arriba preserva el mínimo arquimediano. Esa monotonía NO está probada. Un contraejemplo a ella obligaría a pivotar, no refutaría el signo. Evitar Gram monomial cerca de confluencia: produce falsos negativos por mal condicionamiento.

Estado: OPEN. Papers intactos. No hay bloqueo externo; queda trabajo matemático sustantivo.
