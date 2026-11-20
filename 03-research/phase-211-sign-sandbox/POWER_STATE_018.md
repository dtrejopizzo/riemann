# Estado018 — Tres filas completas y obligación aritmética pendiente

Estado: resultados parciales PROVED, signo global OPEN. Goal activo. Papers intactos. Sustituye STATE017 como resumen vigente.

## Blanco suficiente y región probada

Por POWER_SCALAR_BRIDGE_017 basta demostrar el signo de TODA la tabla H_(N,k)=s^k/(s+u)^(N+k), N>=1,k>=0, a una tasa fija u=63/2. La representación positiva de densidades por elevación Bernstein conserva todos los cruces y el polar; el puente fuerte014 conecta con los datos del Paper47.

Regiones probadas: N1 para TODOS k con margen4/3; N2 y N3 para TODOS k con margen1/8; y TODOS N>=2,k>=10000N² con margen49/50 a u31.5. Las filas1,2,3 valen también para toda u>=31.5. Además siguen vigentes los certificados de ocho polos arbitrarios y del bloque confluente fijo de dimensión12.

Falta, como blanco suficiente, N>=4 y 0<=k<10000N². No se afirma que todos esos puntos estén sin ningún certificado particular; se identifica la región no cubierta por los teoremas uniformes anteriores.

## Avance positivo018

POWER_TABLE_DESCENT_018 prueba las filas2/3 con el multiplicador real y todos los contactos. Covarianza arquimediana reduce a k0, cotas de dos derivadas de digamma controlan ARCH, WRN017 controla el peine completo, y conservar la paridad del polar evita perder el margen en N3.

La recurrencia exacta a_(N,k)=a_(N,k+1)+u²a_(N+1,k) convierte estos teoremas en primeras y segundas diferencias estrictamente positivas de la fila1 para TODOS k. No prueba completa monotonía ni permite extrapolar a todos los órdenes. Root leyó la prueba y reprodujo tools/power_table_descent_018_verify.py con PASS; mapa aprobó independientemente las constantes y el alcance.

## Límite cuantificado del error absoluto

POWER_LOW_TABLE_018 calcula para k0 el presupuesto exacto D_N(theta)=2+2theta J_N(theta−1/2), usando E0(x)=psi_Lambda(x)−x+1 para fijar el endpoint. D_N(0)=2; para theta<1/2 tiende a1/(1/2−theta); en theta1/2 crece como sqrt(N); para theta>1/2 crece como sqrt(N)[1−(theta−1/2)²/u²]^(-N), en el rango de integrabilidad declarado.

El residuo firmado central y la cancelación del polar con el término principal eran conocidos. La novedad es el presupuesto exacto para esta fila, no un teorema nuevo de signo ni una prohibición global. Mapa revisó endpoints, integración por partes y los tres regímenes. La auditoría consolidada está guardada en POWER_TABLE_AUDIT_018 y fue leída por root.

## Qué cambia en la siguiente construcción

No se continuará una campaña fila4,fila5,... como sustituto del paso universal. Los constructores019 buscan una desigualdad FIRMADA del error aritmético o de las diferencias completas que controle órdenes variables. Deben contrastarla con el corpus y conservar el peine completo. Las identidades de recurrencia y los certificados finitos por sí solos no aportan ese signo.

Ningún resultado anterior certifica por sí solo una nueva ventana T>log(5)/2. El cierre requiere completar el blanco suficiente o probar directamente el signo para todos los datos admisibles. No hay contraejemplo a la forma real W ni cierre global.

## Modelo que delimita el descenso estructural

POWER_TABLE_AUDIT_018 §3 prueba un falsificador explícito de la inferencia basada sólo en recurrencias y regiones positivas. V[f]=2||f||²−(u/100)|F(iu)|² conserva las identidades de filtros, márgenes de todos los espacios de hasta12 polos>=u, las tres filas completas y el cono positivo. Sin embargo su entrada N40402,k40401 es negativa, por una desigualdad elemental para coeficientes binomiales centrales. Root revisó independientemente todos esos cálculos, incluida la uniformidad de filas al variar el polo.

V NO es la forma W del paper; no conserva la aritmética concreta ni el perfil logarítmico preciso. El resultado muestra exactamente por qué aquellos datos estructurales no bastan y obliga a utilizar información aritmética adicional. No se declara bloqueado el objetivo ni se refuta el signo real.
