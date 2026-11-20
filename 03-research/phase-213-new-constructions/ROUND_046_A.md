# El déficit se localiza en los primeros j−1 términos de la cuadratura

Antecedentes: el resto firmado de 045; N_BUILD_006 §1 ya usa una segunda integración para el resto periódico. Aquí se elimina exactamente la constante log K antes de partir el logaritmo por su cero. Eso permite acotar toda la parte sobre k≥K por O(x/K²) sin factor log K ni error de borde de primer orden. Se trabaja con la discrepancia de cuadratura, no con el tamaño de la suma prima original.

Sea x=j⁴>81, W=W_j y g su inverso de 045. Para H integrable con suma convergente escribir ΔH=∫₀^∞H(u)du−Σ_{k≥1}H(k). Definir

    H₋(u)=g(u/x) min(log(u/j),0).

Entonces el signo global equivale a que ΔH₋≤C j² para todos los enteros j suficientemente grandes, con una C común. La suma de ΔH₋ sólo usa los índices 1≤k<j. Su integral llega hasta cero y cada evaluación de g sigue conteniendo coeficientes de Möbius a escalas grandes.

**Centrado exacto.** Por 045, ∫g=0 y Σ g(k/x)=Dg(1/x)=W(1/x)=0 porque 1/x<1/81. Por ello el déficit completo de 045 es Δ[g(u/x)log(u/K)] para cualquier K>0. Las partes positiva y negativa del logaritmo dan dos sumandos continuos en el punto de corte.

**Cota uniforme de la parte superior.** Para 1≤K≤x sea H₊(u)=g(u/x)max(log(u/K),0). En su expansión por Möbius sólo aparecen m≤16x/K. En la variable s=mu/x el sumando sin μ es F_z(s)=W(s)max(log(s/z),0) con z=mK/x. El soporte está en [1/81,16], y la variación de su derivada, incluyendo extremos y esquinas, cumple

    Var(F_z') ≤ C(1+log(16/z)),    0<z≤16.

En efecto, en s>z la derivada es W'(s)log(s/z)+W(s)/s. La variación de W' y las normas de W,W' están uniformemente acotadas por 045. La derivada del logaritmo es 1/s, acotada en el soporte. En el corte sólo se añade el salto W(z)/z si z pertenece al soporte. En u la variación de la derivada se multiplica por m/x.

Para una función continua compacta, absolutamente continua con derivada de variación acotada, el error de la regla trapezoidal de paso uno es a lo sumo una constante por la variación total de su derivada: en cada celda, la diferencia con la interpolante lineal es a lo sumo la oscilación de la derivada; sumar las celdas. Aplicarlo extendiendo por cero a la recta. Con M=16x/K, se deduce

    |ΔH₊| ≤ (C/x) Σ_{m≤M} m(1+log(M/m)) ≤ C' x/K².

La última suma es O(M²), por ejemplo agrupando m en intervalos diádicos. No se usa cancelación de μ. Tomar K=j da |ΔH₊|≤C' j². Por 044–045 el déficit completo debe estar acotado superiormente por O(j²); la cota bilateral sobre H₊ prueba la equivalencia anunciada. En particular sólo la parte inferior podría producir un exceso sin cota después de dividir por j².

**Pendiente.** Falta estimar la diferencia entre la integral y la suma en H₋. Contar j−1 índices exteriores no limita a j el número de términos aritméticos internos ni controla el comportamiento de la integral cerca de cero.

**Límite de la estimación por variación absoluta.** En escalas pares, la derivada de g tiene un salto de magnitud mW'(1/16+) en t=1/(16m) para cada m libre de cuadrados: los otros dos términos posibles llevan μ(16m)=μ(256m)=0, como en 044. En u=x/(16m)∈[2K,4K], la derivada de H₊ tiene por tanto un salto de magnitud al menos (log 2)mW'(1/16+)/x. Para x/K→∞ hay ≫x/K enteros libres de cuadrados en el correspondiente intervalo de razón dos, por la densidad positiva clásica de esos enteros. Sumando saltos distintos se obtiene Var(H₊')≫x/K². El orden que se paga usando la variación total es exacto para esta subfamilia. La afirmación deja abierta cualquier cancelación en el error de cuadratura efectivo.
