# Una sola muestra por orden, sin órdenes excepcionales

En 215 una muestra D_k por orden cuadrado detectaba el fallo del signo con un limsup, pues varios ceros de ángulo extremo podían cancelar sus fases para algunos k. La cuadrática en una banda solucionaba esa cancelación integrando en frecuencia. Aquí basta un único integral LINEAL sobre tasas para CADA k. Cambiar la parte real del exponente de Mellin permite aislar un solo punto complejo aunque varios compartan ángulo extremo.

Sea N=k², s_k=−√k+ik y

    C_k=∫₃ᴺ A_N(u) u^(s_k−1)du.

Para k→∞ se tiene lim log(1+|C_k|)/k=Θ. Bajo RH, C_k→0. Si Θ>0, sea w₀ el punto de menor módulo r₀ entre los w de 214 con arg w=−Θ, y m₀ su multiplicidad (incluyendo coincidencias de w). Entonces

    C_k=−(1+o(1)) · m₀ K_N(s_k) w₀^(s_k)/2,
    log |C_k| = Θk − (log r₀)√k − log k + log(m₀√π/2) − 1/4 + o(1).

En particular hay detección en toda subsucesión no acotada. Incluso r₀ queda determinado por el segundo término del crecimiento. Los parámetros de la prueba prima no utilizan ni Θ ni r₀.

**Un punto dominante.** Para cada k grande, la identidad beta de 214 se extiende a s_k: −2N<Re s_k<−1, que asegura integrabilidad en cero y sumabilidad en altura por Z3. En Z(s_k) el término w₀^(s_k) tiene módulo exp(kΘ)r₀^(−√k). Hay sólo un número finito de w con arg w=−Θ, con los repetidos agrupados por multiplicidad. Cada otro de ese ángulo tiene módulo estrictamente mayor y aporta una fracción O(exp(−c√k)). Para los demás la separación angular η>0 de 215 da un total O(exp(k(Θ−η))Σ|w|^(−√k)), despreciable respecto del dominante, pues Σ|w|^(−√k) es acotada por Z3 para k≥4. Esto prueba una equivalencia compleja, no sólo una cota de módulo. Si Θ=0, en cambio |Z(s_k)|≤Σ|w|^(−√k)=o(1).

**Factor beta.** Con z=s_k/2, la expansión de Stirling simétrica en N±z da log(K_N(s_k)/K_N(0))=z²/N+o(1) pues |z|=O(√N). Esto se obtiene por Taylor de (N+z−1/2)log(N+z) en z/N, con el término lineal cancelado y resto O(|z|³/N²+|z|²/N²+1/N). Como z²/N→−1/4 y K_N(0)∼√(π/N), se obtiene K_N(s_k)=(1+o(1))√π exp(−1/4)/k.

**Paso a primos.** La identidad de Mellin usa todo u>0. En [3,N] la diferencia b_N+2A_N tiene módulo ≤Cu log(2u) por 210. Su integral contra u^(−√k−1) es o(1). En u>N, la envolvente Cu log(2u) exp(CN/u²) de 214 da igualmente o(1). Para 0<u≤3 debe rehacerse la estimación porque el peso varía: por |γ|>14 y |δ|≤1/2 se tiene |h_u|≤5u²/γ² (usar |u²+w²|≥Re(u²+w²)≥γ²−1/4). Por tanto Σ|h_u|^N≤C u²(5u²/196)^(N−1) por Σγ⁻²<∞. Integrar contra u^(−√k−1) da O(3^(2−√k)(45/196)^(N−1)/(2N−√k)). Se sigue 2C_k=−K_N(s_k)Z(s_k)+o(1). Fuera de RH la magnitud del término principal diverge, por lo que el error aditivo da error relativo o(1), incluido en el logaritmo.

**Obligación aritmética.** Basta una cota |C_k|≤exp(o(k)) en ALGUNA subsucesión. Frente a la variante lineal de 215 se elimina la necesidad de estimar todos los grandes k. El peso nuevo concentra tasas menores, con coste exp(−O(√k)) para cada tasa fija; ese coste deja visible la señal exp(Θk) de cualquier contraejemplo fijo. No se deduce que el valor absoluto término a término en los primos baste: la pérdida exp(c k²) de 216 vive en una capa u−3 de ancho comparable a 1/k² donde este peso sólo paga exp(−O(√k)).
