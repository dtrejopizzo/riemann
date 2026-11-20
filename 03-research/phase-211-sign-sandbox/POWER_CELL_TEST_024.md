# POWER_CELL_TEST_024 — Test integrado de la primera celda, N=129

Estado: PROVED promedios positivos de la primera celda, con suma Möbius completa, certificado racional ejecutado y revisión independiente APROBADA. Un único N129, sin campaña. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, CUMULATIVE_INVERSE022 y su extensión C_B/MASS, CUMULATIVE_TEST023 y auditorías; búsqueda dirigida en índice/grid/crucigrama (criterios celulares, medias de kernels, C_B). La positividad puntual K>=0 ya está refutada para N129,x1. La diferencia aquí es evaluar una condición INTEGRADA más débil en la primera celda, conservando el peso C_B que anula el extremo1, no repetir otra prueba puntual.

Se fija SOLO N129 y la celda[1,2]. Se calcularán exactamente sus integrales mediante un antiderivado polinómico y una cola Möbius completa. Se coordina con `signo`, que trabaja la estructura general S_N(n), para no duplicar tests.

## 1. Resultado dirigido

Para N=129 y u=63/2, la suma COMPLETA satisface

    31/100 <∫_1^2 K_N(x)C_B(x)dx<8/25,
    33/100 <S_N(2)<1/3,                                 (CELL)
    1/2 <∫_1^2 K_N(x)x^-2dx<3/5.                        (MASS1)

Aquí C_B(x)=(1−x^-2)/2 para1<x<2, y S_N(2)=∫_1^2J_N(x)dx−log2 J_N(2). La condición puntual K_129(1)<0 de023 es compatible con estos tres promedios positivos. Por continuidad, K tiene también valores positivos dentro de(1,2); no se concluye una única transición ni un patrón para las siguientes celdas.

La contribución de esta celda a la representación ERR=−2∫KC_B es estrictamente menor que−31/50. No se declara el signo de ERR total ni de W: faltan las otras celdas y la comparación con ARCH_sharp. S_N(2) y la integral con C_B son dos asignaciones distintas de contribuciones de borde/saltos; no deben sumarse como si fueran beneficios independientes.

## 2. Identidades de integración que eliminan la cuadratura

Como h_N=−J_N' y K_N=J_N−xJ_N', integración por partes en la primera celda da EXACTAMENTE

    ∫_1^2 K_N C_B
       =∫_1^2 J_N dx−(3/4)J_N(2),                     (CB1)
    ∫_1^2 K_N x^-2dx=J_N(1)−J_N(2)/2.                 (MA1)

En CB1 se usó (xC_B)'+C_B=1 y xC_B=0 en1,3/4 en2. El valor del peso en el punto2, donde puede saltar su definición por celdas, no altera la integral ordinaria. No se eliminan saltos de la representación global de ERR.

Escriba J_N(x)=x^-32Σmu(m)m^-32P_N(logx+logm). Sea Q_N el polinomio positivo de igual grado definido por

    31Q_N−Q_N'=P_N,
    q_d=p_d/31,
    q_j=[p_j+(j+1)q_(j+1)]/31, d=128.

Entonces

    ∫_1^2J_N(x)dx
      =Σ(m>=1)mu(m)m^-32
          [Q_N(logm)−2^-31Q_N(log(2m))],               (INT)
    J_N(2)=2^-32Σ(m>=1)mu(m)m^-32P_N(log(2m)).

Los coeficientes p_j de P_N se generan por la recurrencia racional gamma de020. Todos los q_j son positivos y el verificador comprueba coeficiente a coeficiente 31Q−Q'=P.

## 3. Segmento exacto y cola infinita común

El script `tools/power_cell_test_024_verify.py` usa mu(m) por factorización entera para1<=m<=64, logaritmos atanh con resto geométrico e intervalos racionales con redondeo exterior. Evalúa P y Q por Horner. No utiliza cuadratura flotante ni funciones especiales numéricas.

Para controlar TODOS los términos m>=65 se usa la monotonicidad del kernel original w_N(x)=x^-1/2rho_N(logx): w_N>0 y−w_N'=H_N>0. Para cada m,

    0<∫_1^2 w_N(mx)dx<=w_N(m),
    0<w_N(2m)<=w_N(m).

Defina T_P=Σ(m>=65)m^-32P_N(logm). Los errores de INT, J_N(1) y J_N(2) son por tanto <=T_P. Los de CB1, MA1 y S_N(2) son menores que2T_P, porque3/4,1/2 y log2 son menores que1.

Como log64>4=128/32, las funciones x^-32(logx)^j decrecen en x>=64 para todos j<=128. Con L=21/5 y

    I_0=64^-31/31,
    I_j=64^-31L^j/31+(j/31)I_(j−1),

se obtiene el mayorante racional completo

    2T_P<=2Σ(j=0..128)p_jI_j<10^-10.                   (TAIL)

Este error se añade simétricamente a cada intervalo finito antes de comprobar CELL/MASS1. No se ha supuesto signo de la cola de Möbius.

## 4. Verificación y alcance

El verificador ejecutado produce PASS para los tres resultados con cola completa. Como orientación únicamente, los valores son aproximadamente .318043377895 para CB1 y .333118004377 para S_N(2); no participan en la prueba.

Se resolvió un criterio integrado concreto que NO estaba refutado por el punto negativo023. No se probó una condición para todos N ni para todas las celdas de N129; tampoco se controló el daño total de K^- ni se estableció el signo de W. La continuación debe sumar las celdas restantes con signos y mantener los términos de borde de la identidad global.
