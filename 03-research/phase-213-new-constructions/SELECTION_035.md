# Traslado directo de certificados por mezcla de cambios de escala

**Selección.** El promedio convexo de torsiones sin cambio de escala ya fue descartado en G2_B8_R2 §3.2 y R162_1102_CHARACTER_FAMILY. La razón es la extremalidad de la fase uno en cada coordenada de módulo ≤1. No se reabre. Consideramos sólo el cambio adicional que permitiría aplicar literalmente una forma completa positiva de ventana T₀ a todos los tests de una ventana mayor T.

Sea F un test en (−T,T). Comprimir su variable logarítmica mediante G(t)=a⁻¹ᐟ²F(t/a), con 0<a≤T₀/T<1. Se permiten traslación y modulación unitarias de G. Por polarización basta comparar los núcleos en las diferencias |r|<2T. Un contacto fuente de desplazamiento log n pasa al desplazamiento (log n)/a porque c_G(s)=c_F(s/a) antes de modular. En consecuencia todos los contactos de todos los términos quedan fuera del intervalo abierto (0,(T/T₀)log 2). Si 2T>log 2, el contacto objetivo en log 2 es interior a la ventana y pertenece a ese intervalo.

También para una mezcla de masa finita no puede aparecer allí un átomo procedente del fondo continuo. En una vecindad compacta de log 2 dentro del intervalo indicado, la parte arquimediana fuera de la diagonal tiene densidad acotada uniformemente tras el cambio de escala: aK(ar)=O(1/r) por la singularidad K(s)=O(1/s) en cero de P47. La parte polar tiene densidad proporcional a a cosh(ar/2), uniformemente acotada. Las modulaciones introducen factores de módulo uno y los términos diagonales conservan soporte en cero. Por tanto el núcleo mezclado es absolutamente continuo en esa vecindad, mientras W tiene allí un átomo de peso no nulo. Se distinguen en formas completas sobre tests suaves: polarizar y usar parejas de bumps en el interior de la ventana, a distancia log 2, permite probar los núcleos localmente (fijar un bump aproximando una delta y variar el otro).

**Decisión.** Descartada una identidad exacta de W en una ventana mayor mediante mezcla finita en variación total de estas compresiones, aun con modulaciones. La prueba vale para medidas sobre escalas continuas. No decide una desigualdad con un resto firmado, ni descomposiciones que recorten trozos del perfil y recompongan sus cruces. La obstrucción usa el lugar del primer contacto y no el signo de W. Cotejo y revisión independientes.

## También falla la dominación directa, incluso en el sector primitivo objetivo

Fijar a₀=T₀/T<1. Hay tests reales primitivos Fδ, normalizados en L², tales que, uniformemente en 0<a≤a₀ y en toda modulación ω de la fuente,

    W(Mω D_a Fδ) − W(Fδ) ≥ log(1/a₀) − o(1),       δ↓0.

Aquí D_a es la compresión unitaria anterior. Se permiten traslaciones que ajusten el soporte a la ventana fuente. La estimación excluye W(F)≥∫W(Mω D_a F)dμ para todo F primitivo y toda elección de un promedio de masa uno, incluso con parámetros dependientes del test.

**Test.** Elegir d>0 con 2d<min(log 2,2T). Centrar tres copias del mismo bump liso no negativo de anchura δ y norma L² uno en −d,0,d. Combinarlas con coeficientes 1,−2cosh(d/2),1 y normalizar la suma en L². Ambos momentos con pesos exp(±t/2) se anulan exactamente. Para δ pequeño los soportes están separados y el diámetro total es menor que log 2. Tanto el test como todas sus compresiones quedan libres de contactos aritméticos. Su norma L¹ es O(√δ).

**Estimación.** Denotar por H la forma arquimediana de multiplicador m de P47 y por fδ=|Fδ|. La representación de Lévy con núcleo positivo da H(Mω D_a Fδ)≥H(D_a fδ) por la desigualdad puntual de módulos en los incrementos. En el test original H(Fδ)−H(fδ)=O(δ): sólo contribuyen cruces de bumps de signo contrario. Allí el núcleo está acotado uniformemente por la distancia entre soportes y cada producto de normas L¹ es O(δ). El término polar en la fuente vale O(δ) en módulo uniformemente: su núcleo en diferencias está acotado en este diámetro y la norma L¹ tras comprimir vale √a veces la inicial. En el objetivo el término polar es cero.

Por monotonía de m en |t|, H(D_a fδ)≥H(D_a₀ fδ). La diferencia de multiplicadores m(t/a₀)−m(t) es acotada y tiende a log(1/a₀) en ambos extremos por la asíntota de m. La masa espectral de fδ totaliza uno y escapa de cualquier intervalo acotado pues |widehat(fδ)|≤||fδ||₁=O(√δ). Plancherel prueba H(D_a₀ fδ)−H(fδ)→log(1/a₀). Combinando las cotas resulta la desigualdad anunciada.

El test detecta el coste arquimediano antes de encontrar ningún primo. Una estrategia con resta explícita de ese coste, coeficientes subnormalizados o un operador que combine trozos distintos tendría otra desigualdad pendiente. Antecedentes de la estimación: P47 thm:A, lem:mbounds y prop:nearfree.

## Coste residual del primer primo después de corregir cada escala

Supóngase 2T>log 2 y a₀=T₀/T<1. Incluso restando el coste log(1/a) *propio de cada escala* queda, para una familia de tests primitivos unitarios, la cota uniforme

    inf_{0<a≤a₀, ω real} [ W(Mω D_a Fδ) − log(1/a) − W(Fδ) ]
        ≥ (log 2)/√2 − o(1).

Para la prueba, sea Gδ el triple primitivo unitario anterior, con d fijo tan pequeño que dos copias separadas por log 2 tengan diámetro total inferior a min(2T, log 3, (log 2)/a₀) para δ pequeño. Centrar su suma Fδ en la ventana y dividir por √2. Las copias disjuntas conservan los momentos nulos y c_Fδ(log 2)=1/2 exactamente: al trasladar por log 2 sólo se superponen las dos copias idénticas. El objetivo tiene por tanto W(Fδ)=H(Fδ)−v₂/2. Después de comprimir no queda ningún contacto. La cota polar O(δ), la desigualdad diamagnética y la comparación H(Fδ)−H(|Fδ|)=O(δ) siguen vigentes por separación de los seis pulsos.

Para permitir a arbitrariamente próximo a cero hace falta una estimación uniforme adicional. Poner f=|Fδ| y h_a(t)=m(t/a)−log(1/a)−m(t). En 0<|t|≤R se tiene h_a(t)≥log|t|−C_R, pues m(z)−log z tiene ínfimo finito en z>0. La parte negativa en ese intervalo cuesta a lo sumo O_R(δ) al integrar contra |widehat f|² dt/(2π). Para |t|>R, escribir m(t)=log|t|+c+η(t), donde η(t)→0. Entonces |h_a(t)|≤2 sup_{|z|≥R}|η(z)|. Primero hacer δ↓0 a R fijo y después R↑∞. Así H(D_a f)−log(1/a)≥H(f)−o(1) uniformemente, lo que da la cota. Para promedios se integra la energía ya corregida escala por escala.

El coste adicional necesario es al menos v₂/2, incluso para a₀ arbitrariamente próximo a uno; el test depende de a₀. La cota es para el error de comparación y no da la energía mínima de W. PROVED tras auditoría independiente.

Antecedente directo identificado en el cotejo: el paquete doble que aísla log 2 y su valor 1/2 ya son P47 lem:cpos y cor:Qp. Lo adicional aquí es la cota uniforme después de restar log(1/a), aplicada al traslado de certificados.
