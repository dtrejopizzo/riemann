# Presupuesto positivo que sólo usa primos entre x y 2x

Sea L=log 2, ω=2π/L y g(y)=y^(−1/2)(1−cos(ω log y)) en [1,2], cero fuera. Poner h=∫₁²g(y)dy y

    D(x)=xh−Σ_(x<p≤2x) g(p/x)log p.

El signo global equivale a D(x)≥0 eventualmente. Bajo RH se obtiene liminf D(x)/√x≥0.029L. Sin asumir RH, D(x)>0.009√x en todo 10^12≤x≤10^38. Se cambia el peso de 256 para suprimir por completo ambas colas. El presupuesto correcto para esta suma es xh; no se está truncando la suma de 256 con su mismo umbral.

**Por qué el signo eventual decide.** La transformada H(s)=∫g(y)y^(s−1)dy vale (exp(Lz)−1)ω²/[z(z²+ω²)], z=s−1/2, por integración elemental, con singularidades removibles y H(1/2)=L. En particular no se anula para Re s>1/2. El Mellin de D para x≥1 es h/(s−1)−H(s)P(s), con P de 253: el soporte de g(p/x) está en [p/2,p], siempre con x≥1. El principal se cancela en 1. Cualquier cero a la derecha daría un polo, mientras que no hay singularidad real allí; Landau excluye entonces signo eventual. Incluso controlar D en todos los enteros suficientemente grandes bastaría: la derivada del sumatorio es O(1) por θ(y)≤2y y el peso C¹, y fuera de RH hay excursiones negativas de orden x^d para cada 1/2<d<Θ como en 249.

**Separación sin pagar los cubos.** Para el conteo con Λ el principal es xH(1), los términos espectrales son −ΣH(ρ)x^ρ y el resto arquimediano es −∫ g(u/x)du/[u(u²−1)] para x>1, por la fórmula explícita de ψ contra el peso compacto C¹, de derivada segunda por tramos. Las series de ceros convergen absolutamente por el decaimiento cúbico. Restar el conteo con Λ de peso g((u/√x)²) elimina todos los exponentes pares. Su principal es √x L/2 y sus ceros tienen multiplicador H(ρ/2)/2. Las potencias impares propias restantes son positivas, de modo que su retirada sólo aumenta D. En una cota inferior para D la única pérdida arquimediana proviene del peso en √x y cuesta a lo sumo 2/x para x≥2, por g≤2 e integración del núcleo desde √x a infinito.

**Margen de los ceros en la línea.** Para un cero crítico de ordenada γ se tiene
     
    |H(ρ)|/L=|sin(γL/2)/[(γL/2)(1−γ²/ω²)]|.

Hasta G=3·10¹² son críticos por Z2. Usar la traza positiva de 248, con techo 0.047 para la suma baja de 1/|ρ|², y quitar de ese presupuesto los primeros 20 pares. Desde T=γ₂₀ el cociente de |H(ρ)|/L a 1/|ρ|² es ≤(1+1/(4T²))2ω²/[LT(1−ω²/T²)]. El verificador de bolas suma explícitamente los primeros pares y añade este resto, obteniendo menos de 0.471 en total. Bajo RH vale para toda la serie. Así el coste es menor que el principal de cuadrados L/2, aun usando sólo el intervalo [x,2x]. Para la serie de cuadrados los ceros críticos tienen coste ≤2ω² L·0.047 x^(1/4): integrar dos veces por partes la ventana 1−cos(ωt) en H(ρ/2), usando |(ρ−1)/2|=|ρ|/2. Esto da el margen asintótico anunciado bajo RH.

**Cota finita sin hipótesis.** La cola |γ|>G de |H(ρ)|/L es término a término ≤300/|γ|³, por la expresión racional-exponencial, y la de |H(ρ/2)|/(2L) es ≤2ω²/γ² por las mismas integraciones por partes (Re(ρ/2−1/2)≤0). Usar Σ_cola 1/γ²<6.4·10^(−12) de 248. En unidades L√x el coste alto es ≤6.4·10^(−12)[300√x/G+2ω²]. Junto al coste bajo 0.471+2ω²·0.047/x^(1/4), esto deja el margen indicado en todo el intervalo. Ejecutar python3 verify_257.py para reproducir el cálculo con ordenadas certificadas y cotas redondeadas hacia afuera.

**Antecedentes.** 236 ya estudia un coseno en [x,2x], con cambios de signo y un criterio de energía. 247 certifica un presupuesto por la traza con un peso que cambia de signo y llega hasta el origen. Aquí la ventana es diádica, el peso es positivo, el umbral es la integral continua exacta y la traza residual tras los 20 pares prueba dominación por los cuadrados. La desigualdad eventual para primos arbitrariamente grandes queda abierta.
