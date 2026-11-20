# D(R) ya tiende a cero sin RH y el límite fuerte tiene una fórmula rectangular

**Estado: PROVED, con revisión independiente de la densidad uniforme y de las ramas y signos de Littlewood.**

Sea M(T)=Σ_{0<γ≤T}δ² con multiplicidad, δ=Reρ−1/2. Para N(σ,T) contando ceros estrictamente a la derecha de σ, la simetría de la función completada y la integración de indicadores dan exactamente

    M(T)=4∫₀^(1/2) v N(1/2+v,T)dv.

El estimado uniforme de densidad de Selberg N(1/2+v,T)≪T log T exp(−v log T/4) implica M(T)≪T/log T. Basta integrar v exp(−v log T/4) hasta infinito. [Simonič, estimación de densidad cerca de la recta](https://arxiv.org/abs/1910.08274).

Por 412, el bloque γ≤R en D(R) cuesta O(M(R)/R)=O(1/log R). El bloque 2^j R<γ≤2^(j+1)R cuesta O(2^(−j)/log(2R)), sumable. Por tanto incondicionalmente

    0≤D(R)≪1/log R.

Aun si hubiera un solo cuarteto exterior, se tendría D(R)→0; ese cuarteto aporta del orden de 1/R y no es descartado por este techo. Hacer tender D a cero no constituye el paso faltante: se requiere R D(R)→0 por una subsucesión. Como corolario, si todos los ceros hasta H están en la recta, el déficit proyectado de 410 es O(1/(H³ log H)), por la misma descomposición en bloques aplicada a δ²/γ⁴.

**Representación sin una lista de ceros como dato de entrada.** Fijar t₀=1 y T>t₀ sin ceros a esa ordenada. Para a∈[1/2,2], aplicar el lema rectangular de Littlewood a ζ en [a,2]×[1,T]. No hay polo en ese rectángulo. Tomar la rama del argumento en cada horizontal por continuación desde la rama de Euler en 2, no reducirla después al argumento principal. Integrar después en a y permutar integrales. Resulta

    π M(T)/2 =
      ∫₁ᵀ ∫_(1/2)^2 log|ζ(σ+it)| dσ dt
      − (3/2) ∫₁ᵀ log|ζ(2+it)| dt
      + ∫_(1/2)^2 (σ−1/2)[arg ζ(σ+iT)−arg ζ(σ+i)]dσ.

En efecto, el miembro de ceros antes de integrar es 2π Σ_{β>a}(β−a), cuya integral vale πΣ_{β>1/2}δ²=πM(T)/2. Las abscisas singulares se tratan por límite; los logaritmos locales son integrables. Así el límite 412 es cuatro sobre π veces el límite de la expresión rectangular. El antecedente del corpus es el método Green–Littlewood registrado en 173.C; esta derivación especifica los pesos y las tapas para el momento de 412. No se obtiene un mecanismo aritmético nuevo por reemplazar la suma por esta integral. En particular, omitir el término de argumento de la tapa superior carece aquí de justificación.

**Registro de revisión.** La referencia de Simonič contiene la cota de Selberg en(3) y una versión explícita uniforme enσ∈[1/2,0.831] en el teorema1 y su corolario. Para la deducciónM≪T/logT basta ese rango: integrar0≤v≤1/4 con la constante uniforme, y para v≥1/4 usar N(1/2+v,T)≤N(3/4,T)≪T^(15/16)logT, que es o(T/logT). No se emplean constantes dependientes de un v que después tienda a0. La identidad de indicadores lleva factor4 porque cada cero derecho de desplazamientoδ tiene un reflejado izquierdo con igualδ². Los bloques diádicos y el resto proyectado conservan sus cotas con esta mejora deM.

En Littlewood la orientación es vertical izquierda menos vertical derecha, más tapa superior menos tapa inferior. Las ramas horizontales se fijan desde la misma rama de Euler en2, independientemente dea; por eso al integrar el peso de cada tapa esσ−1/2. El polo real en1 queda debajo de la base t=1. Integrar2π(β−a) en a aportaπδ² por cero derecho; la simetría convierte la suma derecha en M(T)/2 y fijaπM(T)/2. Los límites en abscisas con ceros usan la integrabilidad local de log|s−ρ|, con multiplicidades. El factor4/π respecto del límite de412 sigue entonces sin un término de tapa omitido.
