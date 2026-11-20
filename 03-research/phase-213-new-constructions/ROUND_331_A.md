# Recorte por divisor común en la energía de pares próximos

En la energía de 325–326, el coste absoluto de los pares distintos con máximo común divisor mayor que G≥1 es

    O(h binom(2m,m)/G),     0<h≤1, m≥1,

con constante absoluta para el núcleo normalizado de 325. El resultado vale incluso si se reemplaza μ por coeficientes de módulo ≤1.

**Prueba.** Como |K|≤1 y K se anula para |log(n/d)|>h, usar 2l_m(n)l_m(d)≤l_m(n)²+l_m(d)² y simetría. Para X≤n<2X, X potencia de dos, mayorar por la suma sobre todos los divisores comunes g>G. Hay a lo sumo 2X/g múltiplos de g en el bloque. Para cada uno los otros múltiplos distan como máximo 2(e−1)hX, luego hay a lo sumo 4(e−1)hX/g vecinos distintos, incluso cuando esa última cantidad es menor que uno. Sumando g^(−2) para g>G, el bloque cuesta a lo sumo una constante por h(log(2X))^(2m)/(GX(m!)²). Dado que ∫_[2X,4X] dv/v²=1/(4X), la suma de (log(2X))^(2m)/X se acota por cuatro veces la integral de (log v)^(2m)/v² desde 1 hasta infinito, igual a 4(2m)! incluyendo el factor cuatro.

**Aplicación al signo.** Para h=exp(−am), 0<a<log 4, basta conservar la diagonal y los pares con mcd ≤ exp((log 4−a)m). Todo lo retirado, incluso tomando módulos, cuesta O(1/√m). En los restantes escribir n=gr, d=gs con (r,s)=1. Entonces μ(n)μ(d)=μ(r)μ(s)μ²(g) si (g,rs)=1 y vale cero en otro caso. A cociente reducido fijo r/s todos los términos tienen el mismo signo, ya que K≥0. La inversión por divisores dentro de una sola familia de múltiplos comunes no produce cancelación entre sus miembros: la ganancia pendiente debe combinar cocientes reducidos distintos. La cota no estima esa suma firmada.

**Antecedente.** 326 estima el coste total de proximidad sin distinguir el mcd. El recorte anterior conserva su argumento de conteo y cuantifica qué parte se puede retirar ya al coste diagonal. No se atribuye novedad a la factorización elemental de μ.
