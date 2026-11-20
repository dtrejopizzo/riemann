# Techo para el mínimo completo con masa local posiblemente no acotada

Sea D₂(y) la suma, con multiplicidad, de (Reρ−1/2)² para los representantes de cuartetos fuera de la recta con ordenada positiva a distancia <1 de y, como en fase 159 G2_B2_R5. Supóngase D₂(y)≪[log(2+|y|)]^κ para algún 0≤κ≤1. Para la parte negativa M_W del fondo completo y M_A del primitivo,

    limsup log(1+M_A(T))/(2T) ≤ limsup log(1+M_W(T))/(2T)
                                  ≤ min(1/2, Δ+κ/2).

Por tanto, si la hipótesis vale para todo κ>0, ambos cocientes convergen a Δ=sup Reρ−1/2, sin exigir alcance del supremo (115). La hipótesis admite masa local que crezca sin cota. El paper 33 controla la media de D₂, no este crecimiento uniforme.

**Coste en frecuencia de un test negativo.** Para F unitario real y suave en [−T,T], T≥1, con W_T(F)<0, escribir L(ξ)=log(2+|ξ|). La fórmula aritmética W=m(D)−C_T+polar y m(ξ)≥cL(ξ)−C implican ∫L|F̂|²dξ/(2π)≪e^T. En efecto el peine tiene norma O(e^T) por 081 y el término polar está acotado por O(e^T) por Cauchy–Schwarz contra exp(±t/2). También M_W≪e^T. Jensen en la medida de Plancherel da ∫L^κ|F̂|²≪e^(κT) en esos tests, sin requerir que exista un minimizador.

**Tira espectral.** Reutilizar el segmento, la subarmonicidad y los rectángulos de G2_B2_R5 §4 con radio 1/(2T). En vez de tomar sup D₂ resulta
     
    −W_T(F) ≪ T² ∫_{|σ|≤Δ+1/(2T)} ∫ L(ξ)^κ |(t exp(σt)F)^∧(ξ)|² dξ dσ.

Vale multiplicidad ponderada local en el integrando porque cada rectángulo que cubre (σ,ξ) tiene su ordenada a distancia ≤1/(2T) de ξ. El paso nuevo es conservar el peso dentro de la integral hasta restringirse a vectores negativos.

**Multiplicación y cierre.** Extender el multiplicador t exp(σt) desde [−T,T] por un corte suave igual a uno allí, cero fuera de [−T−1,T+1], con primeras dos derivadas del corte uniformemente acotadas. El multiplicador extendido y su segunda derivada tienen normas L¹ ≪(1+T)² exp(|σ|T) para |σ|≤1. Su Fourier está acotada por esa cantidad por O((1+|ξ|)⁻²). Como L(ξ)^(κ/2)≪L(ξ−v)^(κ/2)L(v)^(κ/2), Young da una cota para la norma L² ponderada de la transformada del producto por O((1+T)² exp(|σ|T)) veces la de F̂. Insertando y usando el momento anterior se obtiene −W_T(F)≪(1+T)^6 exp((2Δ+κ)T). Tomar el ínfimo por densidad de los tests y combinar con 115.

**Cotejo y límite.** El uso de sinh y de las masas cuadráticas ya es exactamente U₂ de G2_B2_R5 y no se cuenta como nuevo. El teorema M allí descarta una cota del canal negativo aislado en toda la bola unidad si D₂ no está acotada. Aquí sólo se paga el peso sobre los tests con energía completa negativa, que sí tienen presupuesto logarítmico por la fórmula aritmética. No se prueba que D₂ crezca subpolinómicamente en log |y| para ζ; sin ese insumo no se cierra la cota superior general a exponente Δ.
