# Alineación casi total en un intervalo multiplicativo de primos

Bajo la hipótesis crítica de 183, para cada D≥8 fijo y T→∞, poner N=exp(2T−2D). Existe τ con |τ−Γ|≤exp(4T) tal que

    |Σ_{N≤p≤eN}(log p) p^{iτ}| / Σ_{N≤p≤eN}log p ≥ 1−C/D²−o_D(1).

C es absoluta. El intervalo, de razón e, está dentro del soporte aritmético. El umbral se acerca a uno tomando primero T grande y luego D grande. El antecedente 181 usa un supernivel para un peine global; 183 localiza la masa del perfil. Aquí se deduce alineación normalizada casi máxima en un solo intervalo, en una frecuencia efectiva del perfil.

**Ventanas enfrentadas.** Con w y f=M_Γ h de 183, escribir b=exp(T/2)f/w. Definir L(y)=b(−T+D+y), R(y)=b(T−D+y), con extensión por cero. Para y en compactos de (−D,D), las medidas |L(y)|²dy, |R(y)|²dy tienden vagamente a dy/2: en cada extremo la profundidad es D±y y el factor exp(T)/w² cancela exp(−(D±y)). Sea χ suave real no nula soportada en (−1/4,1/4) y poner χ_D(y)=χ(y/D). Para U=χ_D L y V=χ_D R las normas cuadradas tienden ambas a D∫χ²/2.

Escribir d_p=log(p/N) y E el promedio con pesos log p sobre [N,eN], de masa total asintótica (e−1)N por PNT. En el déficit no negativo de 183 conservar únicamente los saltos desde −T+D+y hasta T−D+y+d_p con |y|≤D/2. Después del cambio a b el coeficiente de cada salto es exp(−2T)w(t)w(t+log p)(log p)/√p. En estas franjas w(t)w(t+log p)=(1+o_D(1))√p uniformemente. Por tanto

    E∫_{|y|≤D/2}|L(y)−R(y+d_p)|²dy=o_D(1).

El costo de recortar la traslación, en norma cuadrada promediada, es a lo sumo ||χ'||∞²/D² por la masa de R en |y|≤D/4+2, que es O(D) en el límite (para D=8 usar un compacto dentro de (−D,D)). Se sigue, por desigualdad triangular, que E||U−V(·+d_p)||²≤C/D+o_D(1). La identidad de polarización da una correlación media real ≥(1−C/D²−o_D(1))||U|| ||V||.

**Frecuencia efectiva.** Por Plancherel esta correlación es una integral de la transformada de U contra la de V con multiplicador E exp(iτ d_p), salvo conjugación según convención. Tras desmodular por Γ, ambos recortes tienen variación O_D(exp T): el multiplicador χ_D exp(T/2)/w y su variación están acotados por constantes dependientes de D, y ||h||∞≤Var(h). Su energía de Fourier fuera de |τ−Γ|≤exp(4T) es O_D(exp(−2T)). Cauchy–Schwarz dentro y fuera de la banda da el enunciado. El paso de d_p a log p sólo cambia una fase común.

El resultado exige una frecuencia real que puede depender de D y del perfil. Para excluir saturación por esta vía haría falta una separación uniforme respecto de uno capaz de superar C/D² en algún D, incluyendo las frecuencias excepcionales. Aquí no se prueba esa separación.

**Auditoría independiente.** Se verificó la extracción por Plancherel, el coeficiente del déficit, la pérdida relativa O(D⁻²) y el orden de límites. P47 prop:wit-coh ya deduce coherencia ponderada a partir de un dato negativo. La afirmación adicional aquí es el umbral cercano a uno en un intervalo primo localizado bajo saturación crítica.
