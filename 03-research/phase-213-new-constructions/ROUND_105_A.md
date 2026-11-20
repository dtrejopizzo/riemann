# Un techo sin tolerancia en una banda de razón cuatro

Para x grande, sea w_x(p)=log(x/p) en x/2≤p≤x y log(4p/x) en x/4≤p<x/2, y cero fuera. El signo global equivale a Σ_p w_x(p)log p≤x/4 eventualmente. La integral del peso es exactamente x/4. Bajo RH hay además margen ≥0.034√x eventualmente. La localización por diferencias ya figura en 044 con otro peso y otra tolerancia.

**Dirección cuantitativa.** Con F=S−id de 104, la discrepancia es H(x)=F(x)−2F(x/2)+F(x/4), por cancelación punto a punto de los pesos inferiores. Por 092 bajo RH F(x)=−√x[2+J((log x)/2)+o(1)] con |J|≤D<0.047. Así

    H(x)/√x ≤ −2(1−1/√2)²+D(1+1/√2)²+o(1).

Usando el valor D=2+γ_E−log(4π)<0.0462, la magnitud del margen supera 0.036 antes del o(1), por lo que vale el margen declarado.

**Recuperación elemental.** Extender S=0 para x<2 y F=S−x para x>0. En cada x fijo vale F(x)=Σ_{j≥0}(j+1)H(x/2^j) por telescopado, pues las colas decrecen geométricamente. Si H≤0 desde X₀≥2, el tramo x/2^j≥X₀ sólo ayuda al techo. Para 2≤x/2^j<X₀ quedan O_(X₀)(1) valores, de peso O(log x), y por debajo de 2 se tiene H(t)=−t/4. Luego F(x)≤O(log x), suficiente por 092 y el mismo argumento unilateral de 088 (J queda acotada inferiormente). Esto recupera el signo sin evaluar ceros para invertir el corte.

**Alcance.** Con razón general r>1 el mismo cálculo sirve si 2(1−1/√r)²>D(1+1/√r)², con soporte [x/r²,x]. En r=2, toda la aritmética queda en dos intervalos adyacentes con pesos logarítmicos simétricos. En 044 la ventana en cuartas potencias es de razón 256 para índices pares y el criterio admite una constante libre tras normalización. Aquí el techo es la propia integral; ésta y la inversa positiva salen de la misma segunda diferencia. La prueba del techo aritmético queda abierta.
