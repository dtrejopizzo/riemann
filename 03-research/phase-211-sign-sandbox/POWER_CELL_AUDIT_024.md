# POWER CELL AUDIT 024

Estado: CELL_BALANCE024 y certificado único de primera celda129 APROBADOS. Papers intactos.

## 1. Criterio integrado — APROBADO

Revisado `POWER_CELL_BALANCE_024.md`. La definición S_N(n)=H_(n−1)∫J−log(n)J(n) conserva los saltos y pendientes de B; la suma absoluta es −F_N/2. No se usa esa identidad como supuesto de signo.

La identidad diferencial J(x)=xJ(n)/n+x∫_x^nK(t)t^−2dt, integrada en el triángulo finito, produce exactamente LOCAL con el factor H/2 y peso 1−(n−1)²/t². El peso no negativo integra a1/n. Así BUFFER conserva toda la parte adversa, sin hipótesis de signo sobre J o K. El criterio J(n)≥0 y sup K^-≤4aJ(n), a=3/4−log2, implica S≥0 porque b_n≥a y H/(2n)≤1/4. No están demostradas esas hipótesis para todas las celdas.

## 2. Exterior e interfaz exacta — APROBADOS

OUTER020 implica h≥H/4 en toda la cola x≥exp((N−1)/30), de donde J(n)≥w(n)/4 y J es decreciente en cada celda enteramente exterior. Por tanto OUT-CELL y su mejora por H−log n son correctas. Sólo se localizan posibles celdas adversas a una región finita por cada N; no se controla automáticamente su balance.

La recurrencia31Q−Q′=P tiene coeficientes positivos y genera T(x)=x^−31Q(log x)=∫_x∞w. El cambio y=mx en ∫_1²w(mx)dx produce correctamente el factor m^−32 en la interfaz de suma Möbius. La fórmula de J(2) conserva2^−32. No falta un jacobiano.

## 3. Corpus y alcance

La distinción relativa a023 es un presupuesto integrado explícito que tolera K negativo, no una resurrección de K≥0 universal. Las identidades Möbius y primitivas son antecedentes; la nueva desigualdad local cuantifica un margen y requiere cotas reales de sus términos. La identidad W/C0=ARCH_sharp/C0+2ΣS conserva el déficit arquimediano. Ni F≤0 ni una celda favorable implican W≥0 o una ventana nueva T.


## 4. Primera celda129 — APROBADA

Revisados `POWER_CELL_TEST_024.md` y `tools/power_cell_test_024_verify.py`. Ejecución independiente PASS: 31/100<∫_1²K C_B<8/25, 33/100<S129(2)<1/3 y 1/2<∫_1²K/x²<3/5. El cálculo es racional con cola completa; no usa cuadratura.

La integración por partes da exactamente ∫K C_B=∫J−(3/4)J(2), usando el límite izquierdo del peso en2, y ∫K/x²=J(1)−J(2)/2. El salto de la representación global en2 no se elimina: el valor puntual del peso no cambia esta integral ordinaria. S(2)=∫J−log2 J(2) es otra asignación de borde y no debe sumarse como un beneficio independiente al primero.

El script comprueba31Q−Q′=P coeficiente a coeficiente. Sus integrales finitas y extremos usan los factores m^−32,2^−31 y2^−32 correctos. La factorización de μ y el evaluador intervalar exterior son los ya auditados022/023. Para cada m, w(mx)>0 decreciente da ∫_1²w(mx)dx≤w(m) y w(2m)≤w(m). Por tanto cada error de las tres combinaciones es menor que2T_P. El mayorante positivo por las integrales desde64 cubre TODOS m≥65 y es menor que10^−10. No se supone signo del resto Möbius.

La negatividad K129(1)<0 es compatible con estos promedios positivos y, por continuidad, obliga a que K sea positivo en algún punto interior. No se deduce número de transiciones. El beneficio de ERR de esta celda no determina ERR total ni W. Las otras celdas y el déficit ARCH_sharp siguen pendientes en esta ronda; no se incorpora aquí ninguna construcción posterior.
