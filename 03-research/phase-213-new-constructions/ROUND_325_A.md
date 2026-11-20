# Una energía de pares próximos mide exactamente la abscisa extrema de los ceros

Sea Θ el supremo de las partes reales de los ceros no triviales de ζ. Fijar η real, suave, no negativa, de soporte compacto en (0,1) e integral no nula. Definir K(v)=∫η(y)η(y+v)dy / ∫η² y h_m=exp(−√m). Para m≥1 poner l_m(n)= (log n)^m/(m! n^(3/2)) y

    E_m = Σ_(n,d≥1) μ(n)μ(d) l_m(n)l_m(d) K(log(n/d)/h_m).

Entonces E_m≥0, las sumas son absolutamente convergentes a cada orden, y

    limsup_(m→∞) E_m^(1/(2m)) = 1/(3/2−Θ).

En particular RH equivale a E_m≤O_ε((1+ε)^(2m)) para todo ε>0. No hay parámetro de altura ni verificación finita en el enunciado. El mismo resultado vale para cualquier h_m→0 con log(1/h_m)=o(m). Se puede por ejemplo usar exp(−m/log(m+2)).

**Representación positiva.** Usar la transformada ∫η(y)exp(−iuy)dy y la probabilidad de densidad W_m(t)=h_m |hatη(h_m t)|²/(2π∫η²). La inversión de Fourier da exactamente E_m=∫W_m(t)|A_m(t)|²dt, donde A_m(t)=Σ μ(n)l_m(n)n^(−it). Salvo el signo (−1)^m, A_m(t) es el coeficiente de Taylor de orden m de 1/ζ en 3/2+it. A diferencia de la norma de Bohr de 321, el promedio se toma a una escala de altura dependiente de m y conserva los pares cercanos, que llevan la cancelación aritmética.

**Techo determinado por la abscisa.** Fijar 0<r<3/2−Θ. En todos los discos de centros 3/2+it y radio r, el recíproco es holomorfo y está acotado por C_r(2+|t|)^(C_r). Para explicitar la uniformidad, tomar 0<δ<3/2−r−Θ. Para alturas grandes usar log ζ en discos de centro 3+iT, de radio 3−Θ−δ, dentro de la zona sin ceros y sin el polo real. Su parte real superior es O_δ(log(2+|T|)) por el crecimiento polinómico clásico de ζ en franjas fijas; el valor del logaritmo en el centro está acotado por el producto de Euler. Borel–Carathéodory en un disco interior da el mismo techo para el módulo del logaritmo, en particular en las abscisas requeridas a altura T. Las alturas acotadas se tratan por compacidad del recíproco, regular en 1. Cauchy da |A_m(t)|≤C_r(2+|t|)^(C_r)r^(−m). Los momentos fijos de W_m cuestan O_r(h_m^(−2C_r))=exp(o(m)), por el decaimiento rápido de hatη. Esto demuestra la cota superior tras tomar r creciente hasta 3/2−Θ.

**Por qué un cero aislado es detectable.** Supongamos que el limsup fuese menor que el valor anunciado. Elegir radios 3/2−Θ<R<R' con el limsup menor que 1/R'. Hay un cero ρ a distancia horizontal de la recta de centros estrictamente menor que R. Por continuidad, en todo un intervalo fijo de t alrededor de Im ρ, la distancia |3/2+it−ρ| es menor que R. En ese intervalo acotado W_m(t)≥c h_m para todo m grande, porque hatη(0)≠0. Por Cauchy–Schwarz el L¹ local de |A_m| es ≤C h_m^(−1/2)√E_m. De ahí Σ R^m ∫|A_m|dt<∞. Por Tonelli la serie de Taylor converge absolutamente a radio R para casi todo t del intervalo. Esto contradice el polo de 1/ζ en ρ, independientemente de su multiplicidad. No se supuso que Θ fuese alcanzado.

**Dónde vive la estimación faltante.** K es no negativo, vale 1 en cero y se anula para |v|≥1. La diagonal ya cuesta O((m+1)^(−1/2)): al omitir μ² basta comparar Σ (log n)^(2m)n^(−3) con la integral y un máximo por unimodalidad (una constante absoluta basta ante el máximo). La integral dividida por (m!)² es (2m)!/[2^(2m+1)(m!)²]; el máximo dividido por (m!)² es O((2/3)^(2m)). Sólo quedan productos de Möbius con 0<|log(n/d)|<h_m. Un techo subexponencial para esa suma firmada cerraría el signo. La reducción no estima esa suma. El índice registra antecedentes de Turán, momentos y formas de Gram; aquí lo específico es la identidad cuantitativa para Θ con un soporte relativo que se estrecha a velocidad subexponencial en el orden.
