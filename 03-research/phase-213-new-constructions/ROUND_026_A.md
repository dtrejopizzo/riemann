# Conteo espectral en el corte completo de celdas

Sea M_X la matriz física sin polos de BUILD084 (3) en todas las celdas de índices 1,...,X, con X entero. Se cumple

    n_{≤0}(M_X) = O(X/(log X)²).

El mismo mayorante vale al restringir a los dos momentos primitivos y para la forma con polos en todas las celdas (perturbación de rango a lo sumo dos). Antecedentes cotejados: matrices de 212-59/75, conteos de P47 prop:NC y lem:ext-hf, y el piso por grupos de 025. La desigualdad de Bessel es clásica. Aquí la separación de los contactos en la cola permite aplicarla a la suma aritmética completa.

Eliminar las primeras ⌈√X⌉ coordenadas. Para i<j restantes, el intervalo j/(i+1)<n≤j/i tiene longitud j/(i(i+1))<1. Por tanto la entrada aritmética es cero o un solo peso Λ(n)/n. Para cada n hay a lo sumo ⌊X/n⌋ índices i posibles y a lo sumo n índices j por i. Contando ambos triángulos, la suma de cuadrados de las entradas aritméticas es a lo sumo 2X Σ_{n≥2} (log n/n)²=O(X). Por h(m)≤C/(m+1) las entradas arquimedianas fuera de diagonal son O(1/|j−i|), con suma de cuadrados O(X). La matriz E de todos los términos fuera de diagonal de la cola satisface pues ||E||²_HS=O(X). La diagonal D tiene mínimo δ≥(log X)/2−O(1) por (3).

En un subespacio no positivo del bloque retenido, cada vector unitario z cumple δ≤−⟨z,Ez⟩≤||Ez||. Sumando sobre una base ortonormal se obtiene dimensión ≤||E||²_HS/δ² para X grande. Reponer las coordenadas iniciales añade a lo sumo ⌈√X⌉ al índice no positivo por intersección de subespacios. Esto prueba el enunciado. El argumento también admite cΛ para un c fijo. Su conclusión cuantifica la fracción de autovalores no positivos; deja abierta la existencia de uno solo. El parámetro X mide celdas y la semilongitud logarítmica del corte es (log(X+1))/2. PROVED tras revisión matemática independiente.
