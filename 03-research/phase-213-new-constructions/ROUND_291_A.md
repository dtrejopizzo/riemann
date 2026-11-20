# El carácter principal a frecuencia fija oscila demasiado; se puede retirar del promedio completo

En 290 tomar 1≤κ≤N^(1/4) y P impar comparable con κ+1 y mayor o igual que κ. Así el promedio de todos los caracteres reproduce μ exactamente. Hay dos hechos compatibles: para el carácter trivial los sumandos a frecuencia fija exceden el presupuesto de raíz por ambos signos; después de integrar se puede suprimir ese carácter y renormalizar el resto, con error de raíz en cualquier intervalo.

**Obstrucción a frecuencia fija.** Para el carácter trivial, en la representación Fourier de 288 el sumando real es

    a_t(n)=μ²(n) ∏_(p|n)(cos(t log p)−1),     A_t(x)=Σ_(n≤x) a_t(n).

Se obtiene factorizando el cuadrado ordinario centrado primo a primo y dividiéndolo por 2^ω(n). Para cualquier t∈[1,2] se tiene A_t(x)=Ω₊(x/√log x) y Ω₋(x/√log x), donde cada signo tiene su propia subsucesión. Incluso las integrales en t de la parte positiva y de la parte negativa en magnitud tienen, por separado, ese límite superior inferior en orden.

En Re s>1 comparar el producto de Euler de F_t(s)=Σ a_t(n)n^(−s) con

    ζ(s−it)^(1/2) ζ(s+it)^(1/2) / ζ(s).

Los términos de grado uno coinciden, por lo que el factor corrector tiene cola que converge absolutamente y no se anula cerca de Re s=1, uniformemente para t∈[1,2]; los factores finitos se revisan directamente. En s=1+it sólo p=2 podría dar cero en 1+(cos(t log p)−1)p^(−s); exigiría a la vez cos(t log 2)=−1 y exp(−it log 2)=1, imposible. Se toman las ramas desde Re s>1; sólo hacen falta sus módulos. Por el polo simple en 1, la ausencia de ceros de ζ sobre Re s=1 y compacidad,

    |F_t(1+ε+it)| ≫ ε^(−1/2),      |F_t(1+ε)| ≪ ε,

con constantes uniformes. Por sumación parcial F_t(s)/s es la integral de A_t(exp u) exp(−su) para u≥0. La primera estimación implica que la integral del valor absoluto con peso exp(−(1+ε)u) es ≫ε^(−1/2). La segunda acota con el mismo peso la integral firmada por O(ε). Por tanto ambas partes en magnitud tienen masa ≫ε^(−1/2). Como ∫₁^∞ exp(−εu)du/√u≤√(π/ε), se obtiene el Ω anunciado para cada signo; integrando antes en t y aplicando Tonelli se obtiene la versión integrada. Esto excluye acotar los sumandos uno a uno por raíz, aun en frecuencias bajas ordinarias; no usa una hipótesis sobre ceros en la franja abierta.

**Retirar caracteres ya integrados.** Sea R_χ(n) la parte real del filtro con un carácter de 290, integrado con Wδ (es decir, contra su densidad Fourier). Su término diagonal tras complementar vale μ(n). Los demás factores de carácter tienen módulo uno. La prueba de 289, que ya sumaba los módulos antes de agrupar, da por tanto uniformemente

    Σ_(n≤N)|R_χ(n)−μ(n)| ≪ κ√N log(2κ)/(log(2N))^(3/4).

Sea k=2(P−1). Al eliminar cualquier conjunto E de e<k caracteres, la diferencia entre el promedio renormalizado de los k−e restantes y μ es exactamente −Σ_(χ∈E)(R_χ−μ)/(k−e). En particular se pueden retirar los dos caracteres que son triviales en las unidades (y difieren sólo en la paridad de v_P), con error total O(√N log(2κ)/(log(2N))^(3/4)) cuando P≥3 y P≍κ+1. Se conserva esa cota para toda suma en subintervalos. El promedio restante ya no tiene por qué mayorar punto por punto; el error absoluto acumulado basta para el criterio unilateral de 287.

**Qué queda.** Las oscilaciones de A_t hacen inviable buscar una cota de raíz uniforme término a término antes de la integración. El carácter trivial y su variante en la valuación ya no son necesarios en la estimación global. Sigue abierta la cota firmada para el promedio integrado de los caracteres no triviales en las unidades. El producto de Euler de cada uno mantiene el factor común del recíproco de ζ en el término de primer grado.
