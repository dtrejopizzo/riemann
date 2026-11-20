# Jensen en la frecuencia recíproca: piso exacto para el complemento de celdas

Sea m el símbolo arquimediano del paper 47. Para un test unitario con primitiva G en L²(ℝ) se cumple

    ∫ m(ξ)|F̂(ξ)|² dξ/(2π) ≥ m(1/||G||₂).

En particular, para el complemento ortogonal de las constantes a trozos en celdas de longitud h, el piso es m(π/h), sin constante aditiva de comparación. «Piso» designa una cota inferior; no se afirma que sea el ínfimo alcanzado.

**Prueba.** Por la expansión exponencial de K en P47, con c_j=1/2+2j, se tiene m(ξ)=C₀+Σ_{j≥0}(2/c_j)ξ²/(c_j²+ξ²). En la variable Z=1/ξ², cada sumando es proporcional a (1+c_j² Z)^(−1), convexa y decreciente. Bajo la probabilidad |F̂|²dξ/(2π), E Z=||G||² por Plancherel. Aplicar Jensen término a término y sumar por monotonía. En cada celda de media cero la primitiva desde el extremo izquierdo se anula en ambos extremos; las primitivas concatenadas se extienden por cero y ||G||≤(h/π)||F|| por Wirtinger. Esto da el piso. El Jensen en ξ² de P47 da la otra dirección y requiere momento positivo; no contradice esta desigualdad con momento inverso.

**Conteo arquimediano.** Para el operador comprimido del símbolo m en un intervalo de longitud L, sean λ_k sus autovalores crecientes con multiplicidad, k≥1. Entonces

    m((k−1)π/L) ≤ λ_k ≤ m(kπ/L).

Para el lado inferior k≥2, tomar el complemento de los k−1 primeros modos de Neumann (incluida la constante). La primitiva del modo cos(nπt/L) es L sin(nπt/L)/(nπ) en coordenadas [0,L]. Ortogonalidad da ||G||≤L/((k−1)π) para ||F||=1, y se aplica el principio min–max. Para k=1 basta m≥m(0). Para la cota superior usar los primeros k senos de Dirichlet y el Jensen de P47 en ξ², con ||F'||≤kπ/L. Así, si ξ₀ es la raíz positiva de m, el número estrictamente negativo está entre el número de enteros k≥1 con kπ/L<ξ₀ y el de enteros k≥1 con (k−1)π/L<ξ₀. Las cotas difieren en uno. El argumento es una prueba elemental de una acotación de tipo Dirichlet–Neumann para un símbolo subordinado; no se atribuye novedad general a ese principio.

**Error del mínimo para la forma completa.** Sobre J compacto de ventanas sea λ_h el mínimo de W en constantes por celdas de longitud h=2T/N. Uniformemente al refinar, para cada 0<s<1/2,
    
    0≤λ_h−λ_W(T)≪_{J,s} h^(2s)(1+|log h|).

Para un minimizador unitario F de 077 y su proyección ortogonal por medias Π_h, ||F−Π_hF||₂≪h^s||F||_{H^s} por la fórmula de varianza en cada celda y la seminorma de diferencias. También ||Π_hF||_{H^s}≪_s||F||_{H^s}. Para verlo usar la malla sobre toda la recta (alineada con el intervalo); en celdas distintas, por Jensen el cuadrado de la diferencia de medias se acota por la media de las diferencias al cuadrado. La integral del núcleo |v−w|^(−1−2s) entre celdas no adyacentes es comparable al área por su valor mínimo; para las adyacentes la misma cota con constante dependiente de s vale por integración directa, finita porque 2s<1. Dentro de una celda la proyección es constante. Esto prueba la estabilidad también en la frontera del soporte.

Para e=F−Π_hF, m(ξ)≤C+log(2+|ξ|) y log(2+|ξ|)≤C_s+|log h|+C_s(h|ξ|)^(2s) para h≤1. Tras integrar y añadir los términos acotados de W queda W(e)−λ_W||e||²≪h^(2s)(1+|log h|). La ecuación propia débil cancela exactamente el término lineal: el exceso del cociente de Π_hF es [W(e)−λ_W||e||²]/||Π_hF||², con denominador uniformemente próximo a uno. El otro signo del error es variacional.

**Uso y límites.** El complemento de las medias tiene para W piso m(π/h)−Σ_{n<exp(2T)}v_n−4sinh T. Si es positivo, el bloque cruzado aún interviene en el complemento de Schur; la positividad aislada de la matriz de celdas no basta. P47 lemmas coer-lowpass/coer-B ya dan coercividad logarítmica usando dos momentos de Tate por celda. Aquí basta la media ordinaria y se obtiene directamente el valor del símbolo en π/h. El conteo a una unidad es para el operador arquimediano solo. No se obtuvo una constante numérica de error para W, una ventana nueva ni un signo uniforme en T.
