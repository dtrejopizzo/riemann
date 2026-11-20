# AUDIT_008 — Inversión ambiental, adjunto y dominio de grafo

2026-10-19. Revisor independiente. Leído CONSTRUCTOR_008 completo.
**Veredicto: PROVED lemas1–4 con pruebas elementales incluidas. Clausurabilidad e invariancia del módulo OPEN. D íntegro activo.**

## 1. Corpus y cambio de objeto

La inversión unitaria de un L² ponderado es estándar y no es una nueva fuente de signo. La razón nueva del memo es calcular su conjugación EXACTA sobre G_n del kernel −R ya construido, con su medida no homogénea, y auditar la completación concreta. Esto no reabre los espejos de sectores/portadores de fase199 ni introduce una nueva norma abstracta de Q_T. El memo conserva correctamente esas distinciones.

## 2. Involución ambiental y defecto

La densidad de una inversión unitaria satisface

    a(y)²=ρ(1/y)/(y²ρ(y))=y^(−2α)τ(1/y)/τ(y).

Por tanto la fórmula de U es correcta; a(y)a(1/y)=1, su norma se conserva y U es autoadjunto involutivo. Para α=1/4, el factor y^(−1/4) se cancela exactamente con la raíz del √y de Poisson, produciendo sqrt((1−m(y))/τ(y)). No se elimina el denominador ni se identifica U con una operación en el componente aritmético.

La conjugación directa da el coeficiente

    n^(−α) sqrt[τ(n²/y)τ(y/n²)/(τ(1/y)τ(y))].

Esto es b_n(y) veces G_n*, con b_n²=r(y/n²)/r(y). El producto M_bG_n* tiene sentido sobre toda imagen G_n*(L_α): la fórmula coincide punto a punto con el operador acotado U G_n U. No hace falta que M_b aislado sea acotado; no se reclama tal cosa.

Para h(x)=logτ(e^x), la concavidad estricta ya aprobada da que h(x)+h(−x) es par y estrictamente decreciente con |x|. La comparación |log y−2log n| frente a |log y| prueba correctamente b_n<1 para y<n, =1 para y=n y >1 para y>n. El defecto cambia de orientación. Sólo se excluye la igualdad ingenua U G_n U=G_n* para ESTA inversión ambiental; no se afirma un NO-GO para otras realizaciones o involuciones.

## 3. El cierre no es automáticamente un grafo

El cierre de la imagen A↦(√κ A,TA) en un producto de Hilbert existe, pero eso no demuestra inyectividad de su primera proyección. La presencia de componentes verticales y la clausurabilidad de T son preguntas distintas de la existencia de ese cierre. El memo no supone resueltas ninguna de ellas.

Aunque P_s y las probabilidades gaussianas sobre enteros tengan soportes medibles muy distintos, esa observación sola no prueba no clausurabilidad de un operador que integra en y con un peso singular. Hace falta una sucesión con convergencia apropiada o un argumento completo de dominio del adjunto. No se presenta ninguno sin probar.

## 4. La sucesión de exclusiones primoriales

Cada A_L es un polinomio finito de divisibilidad Haarcentrado. La fórmula de su norma aritmética es exacta:

    E_s|A_L|²=δ_{s,L}−2δ_Lδ_{s,L}+δ_L²→0,

pues 0≤δ_{s,L}≤δ_L→0. Para y fijo, la suma gaussiana es dominada y el indicador de enteros sin primos ≤L converge a 1_{|N|=1}. Así T A_L→2e^(−πy)/τ(y) punto a punto. Este límite pertenece a L_α: es O(√y) en cero y tiende a1 en infinito, donde τ decrece exponencialmente.

La convergencia puntual NO es fuerte en L_α. Para y∈[1/L,2/L], todo entero positivo permitido salvo1 excede L. La cola es uniformemente O(L exp(−cL)); Poisson da τ(y) comparable a √L. Así la media del indicador es O(L^(−1/2)). La cota elemental δ_L≥e^(−2)/(1+log²L) implica |TA_L|≥δ_L/2 en ese intervalo para L grande. Integrar la densidad produce

    ||TA_L||²≥c_α δ_L² L^(1/2−α)→∞.

La prueba final no necesita Mertens. Para verificar su cota elemental, escribir P_L(t)=Π_{p≤L}(1−p^(−t))^(−1), ε=1/log²L. La serie logarítmica da

    log[P_L(1)/P_L(1+ε)]≤εΣ_{p≤L}log p/(p−1)
       ≤ε log L (1+log L)<2  (L≥3).

Además P_L(1+ε)≤ζ(1+ε)≤1+1/ε por comparación integral. Así δ_L=P_L(1)^(−1)≥e^(−2)/(1+log²L). Por otro lado P_L(1) contiene la suma armónica de n≤floor(L), luego δ_L≤1/H_floor(L)→0. Ambas cotas y sus sentidos son correctos; son suficientes para todas las convergencias y divergencias usadas. La divergencia sólo descarta ESTA sucesión como argumento de límite fuerte vertical. No demuestra clausurabilidad ni impide otras sucesiones.

## 5. Alcance final

Las tres fórmulas ambientales y el diagnóstico de la sucesión están aprobados. No se probó que U preserve la imagen cerrada de 007, ni un entrelazamiento con una operación aritmética compensatoria, ni una traza o forma sobre todos los tests de Q_T. No se debe importar el adjunto ambiental al módulo sin reductividad o cálculo de la compresión correspondiente.

**Auxiliar de dominio resuelto en el alcance escrito; clausurabilidad/invariancia y enlace Q_T OPEN. Objetivo D no cumplido.**
