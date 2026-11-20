# Estado026 — Corte uniforme y balance conjunto firmado

Estado: resultados parciales PROVED y auditados; signo global de W OPEN. Sustituye STATE025 como resumen vigente. Goal activo; papers intactos.

## Corte uniforme, sin extrapolar certificados

POWER_UNIFORM_CUTOFF_026 demuestra para d=N−1>=2 dos cortes:

    t_J=d(d+220)/(330d+6300),
    M=u²/(2d−1), Q=sqrt(9/4+M), t_R=2dQ/(u²−Q²), u=63/2.

Para t>=min(t_J,t_R), D_N'/D_N<=30. Por ello la suma Möbius COMPLETA satisface K_N(x)>=x^-32 D_N(logx)/4>0 cuando logx supera ese corte. Ambos cortes son d/330+O(1), mejorando el anterior d/30. El caso N2 se trata mediante el polinomio afín. Jensen sobre los coeficientes y barreras elementales de Riccati proporcionan pruebas uniformes, no una campaña de filas.

Además K_N(x)>0 para TODOS 2<=N<=129 y x>=exp(2/3). La monotonía de la fórmula y dos comprobaciones racionales de extremos prueban el rango. Todas las celdas enteras contenidas en la cola tienen balance favorable y una cota gamma explícita. El interior sigue pendiente y crece con N.

## La comparación pendiente no queda resuelta por ERR129

POWER_ARCH_CELL_026 demuestra ARCH_sharp129/norma²<−.81. El beneficio garantizado por ERR129<−.66 no basta para certificar W129: sumar solamente .66 deja un comparador menor que −.15. NO es una cota superior de W ni un contraejemplo; el beneficio real puede ser mayor.

La agrupación exacta W[g_N]/norma²=int K_N(t)Omega(t)dt conserva ARCH_sharp y todos los términos aritméticos. Sin embargo Omega(3/2)<−.1, demostrado exactamente. Queda refutada solamente la positividad puntual universal de ese peso. Las restricciones de K_N procedente de la autocorrelación gamma no se eliminan y pueden controlar el emparejamiento firmado.

## Evidencia y alcance

POWER_ARCH_CELL_AUDIT_026 aprueba ambas pruebas, incluido Fubini agrupado, barreras Riccati y colas completas. Root leyó ambos textos y reprodujo los dos verificadores Fraction: PASS. No se atribuye uniformidad a los scripts: la proporcionan las demostraciones.

La cobertura de W permanece sin cambios: filas N1,2,3 para todo k, cono k>=10000N², ocho polos arbitrarios y bloque fijo12. El puente escalar017 exige TODOS N,k. No hay una nueva ventana T certificada ni cierre del signo global.

## Continuación027

Buscar una desigualdad del balance conjunto que use la forma gamma real y su curvatura, conservando cancelaciones. Las masas integrales o discretas aisladas y la positividad exterior no sustituyen el control interior. Dos constructores continúan, con revisión independiente; no se reintenta positividad puntual universal de K ni Omega.
