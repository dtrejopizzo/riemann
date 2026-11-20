# Verificación de la transferencia de fase en 370

Usamos b,d,α,ξ,L como en 370. Sea P=exp(b−1/d), Z=exp b, ε=exp(−c√b), reduciendo c si hace falta. En [P,Z] el PNT clásico da |θ(y)−y|≪εy. Tomar h(y)=y^(−α)(1−cos(t log y))/log y. Integrar por partes da

    |∫_(P,Z] h(y) d(θ(y)−y)| ≪ ε M(1+|t|),   M=e^ξ/(db).

En efecto, los bordes y|h(y)| son O(e^ξ/b)=O(dM), y y|h'(y)|≪(1+|t|)y^(−α)/log y. La integral de este último peso sin el factor de altura es comparable a M por el cambio r=d(b−log y). En la integral continua la densidad en [0,1] es ≥cM dr. Por tanto la pérdida es al menos

    cM [1−|sin(t/(2d))/(t/(2d))|] ≫ M min((t/d)²,1).

En 1/b≤|t|≤2√L esto es ≫M/ξ². Basta C grande para que ε(1+2√L)ξ²=o(1). La fórmula maneja fases centradas en múltiplos exactos de 2π y ambos extremos de la banda. La masa resultante M es asintótica a L/b por la ecuación de silla.

Comprobación del tramo local restante de 370: en |t|≤1/b, F(α+it)=O(d), F'=O(1), |L_z|=O(L) y |H|=O(1), de modo que |B_z|=O(Ld). Estas cotas locales permiten descartar la cola gaussiana desde (log L)/√(Lb) sin enfrentar dos constantes indeterminadas multiplicando log² L. En el núcleo local |L_z(α+it)−L_z(α)|≪|t|Lb=o(L), y |t|/d=o(1), uniformemente. Con ello se recuperan los dos coeficientes principales de 370. Verificados también los horizontales por |E_z(σ+it)|≤E_z(α) y x^(1+1/L−α)exp(−2L)=exp(−(2−o(1))L).

Conclusión de la revisión: las desigualdades de 370 se siguen en el rango indicado para C absoluto suficientemente grande. La demostración es asintótica y no proporciona un primer x efectivo.
