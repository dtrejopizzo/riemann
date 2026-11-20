# Qué mide exactamente la varianza después de retirar los pares críticos

**Estado: PROVED, con revisión independiente de Hadamard emparejado, multiplicidades y órdenes de los restos.**

Sea V₀=ξ''(1/2)/ξ(1/2), varianza del núcleo normalizado de 406. Escribir los ceros del semiplano superior con multiplicidad como ρ=1/2+δ+iγ. Entonces

    V₀ = Σ_{γ>0} 2(γ²−δ²)/(γ²+δ²)².

En efecto, para la función par w↦ξ(1/2+w) el producto de Hadamard agrupado por pares wρ,−wρ tiene factores 1−w²/wρ². Converge localmente por Σ|wρ|^(−2)<∞; el factor exponencial lineal es constante por paridad. Dos derivadas logarítmicas en cero y conjugación dan la fórmula. Todos los sumandos son estrictamente positivos ya que γ>|δ| (basta la franja 0<Re ρ<1 y la verificación a altura 1). No interviene la simplicidad.

**Consecuencia para 407–409.** Después de dividir por todos los pares de ceros sobre la recta hasta altura H, la segunda derivada normalizada que queda es exactamente la suma anterior sobre los ceros no retirados. Esto vale incluso si aún no se conoce la positividad del núcleo cociente. Al crecer H el residuo tiende a la suma sobre los ceros exteriores, por convergencia absoluta; por tanto tiende a cero si y sólo si RH. La positividad a cada paso, aun demostrada para todos los pares críticos en orden, no basta por sí sola para identificar ese límite con cero. Si la recta está verificada hasta H, el residuo después de retirar esos pares es O(log H/H), por sumación parcial del conteo de ceros. El certificado de 409 sí aporta positividad para su etapa finita; la identidad de varianza por sí sola no aporta ese signo de núcleo.

**Separar el efecto de desplazar ceros horizontalmente.** Comparemos V₀ con el momento que resultaría de proyectar sobre la recta todos los ceros, conservando ordenadas y multiplicidades. El déficit es

    Σ_{γ>0} 2/γ² − V₀
      = Σ_{γ>0} 2 δ²(3γ²+δ²)/[γ²(γ²+δ²)²] ≥0.

Se anula exactamente bajo RH. Cada término mide un desplazamiento horizontal al cuadrado. En particular, tras una verificación rigurosa hasta H, el déficit total es O(log H/H³): basta δ²≤1/4, sumar O(γ^(−4)) para γ>H y usar N(T)=O(T log T). Aquí Σ2/γ² incluye las ordenadas de TODOS los ceros con multiplicidad; sustituir las de los únicos ceros conocidos en la recta cambiaría el enunciado. La ganancia de dos potencias de H respecto de la varianza residual viene de restar la contribución vertical común, no de excluir ceros más altos.

**Registro de revisión.** Elegir un representante conγ>0 de cada par±wρ produce el producto∏(1−w²/wρ²), incluyendo cada multiplicidad. Al agrupar las exponenciales canónicas de género1 se cancelan dentro de cada par; el único factor global restante es exp(a+bw), y la paridad obliga b=0. No aparece un factor cuadrático adicional. La segunda derivada de log ξ en0 es−2Σwρ^(−2); los dos representantes superioresδ+iγ y−δ+iγ de un cuarteto cancelan sus partes imaginarias y dejan exactamente los sumandos escritos, sin dividir otra vez por2. En ceros críticos múltiples se resta2/γ² por cada orden retirado.

Cada término residual está entre0 y2/γ². El déficit exacto es2δ²(3γ²+δ²)/(γ²(γ²+δ²)²) y, paraγ grande con|δ|≤1/2, es O(γ^(−4)). Sumación parcial conN(T)=O(Tlog T), contando todos los ceros y sus multiplicidades, da respectivamente los restos O(log H/H) y O(log H/H³). La hipótesis de verificación hastaH significa que todos los ceros de esa franja están en la recta, no sólo que se conoce una lista de ceros críticos. Sin positividad del núcleo cociente, el valor es una segunda derivada normalizada formal, no una afirmación de positividad de una medida; la identidad espectral y su límite siguen siendo válidos.

Este cálculo da una prueba de obstrucción al paso de finito a global: el dato adicional requerido para concentración ya codifica todo el posible espectro exterior en una suma positiva. Para deducir RH por esta vía haría falta una cota independiente que fuerce ese residuo o el déficit a cero; contar etapas de positividad o sustituir un H finito no proporciona tal cota. No se afirma novedad histórica del producto de Hadamard ni de sus momentos.
