# Las potencias primas superiores consumen a lo sumo la mitad de la norma crítica

Usar la ventana indicatriz S_h(x)=Σ_{xe^(−h)<n≤x} μ(n), 0<h≤1. Escribir ‖·‖_X para L²([X,2X],dx/x). Definir la contribución de primos simples

    P_h(x)=Σ_p (log p) S_h(x/p).

RH equivale a ‖P_h‖_X ≪_ε √(hX) X^ε log(2X) para cada ε>0, todo X≥2 y toda anchura indicada. La reducción procede de una contracción de las potencias superiores a la escala de raíz. No se toma valor absoluto dentro de P_h.

**Identidad para el pulso.** De μ(n)log n=−(μ*Λ)(n), separando k=1 y aplicando la identidad log n=log x−h+∫_0^h 1_{n>xe^(−v)}dv para cada n del pulso (salvo extremos de medida cero), resulta

    (log x−h)S_h(x)=−P_h(x)−Σ_{p,k≥2}(log p)S_h(x/p^k)−∫_0^h S_v(x)dv.

Definir A(X)=sup_{1/2≤Y≤X, 0<h≤1} ‖S_h‖_Y/√(hY). Es finito para X acotado: cuando h<1/(4X+4) los intervalos de x activados por enteros distintos hasta 2X son disjuntos y cada uno tiene medida logarítmica a lo sumo h. El coste normalizado de las potencias superiores en el bloque X es a lo sumo

    A(X/4) Σ_{p^k≤2X,k≥2} (log p)/p^(k/2) ≤ A(X/4) ((log X)/2+O(1)).

Aquí se usa la fórmula clásica de Mertens Σ_{p≤z}log p/p=log z+O(1); la suma de k≥3 converge absolutamente. El coeficiente 1/2 es el de este mayorante, sin aseveración de que se alcance en la norma. La integral de pulsos cuesta a lo sumo (2/3)h A(X) después de normalizar.

**Absorción.** Si vale el techo propuesto para P_h, aplicar la identidad en cada bloque Y grande y dividir por log Y−1. Para Y≤X resulta una cota C_ε X^ε+(1/2+O(1/log Y))A(X). Elegir Y₀ fijo para que el coeficiente sea ≤3/4 cuando Y≥Y₀; los bloques inferiores cuestan A(Y₀). Tomar el supremo demuestra A(X)≪_ε X^ε. Inversamente, con este techo de A, la identidad y los mismos mayorantes dan la cota propuesta para P_h.

**Enlace con los ceros.** Bajo RH el método de 337 en abscisa σ=1/2+ε' da ‖S_h‖_X²≪ X^(2σ)h^(1−2γ), usando |1/ζ(σ+it)|≪(2+|t|)^γ para cualquier 0<γ<1/2 y el multiplicador (1−e^(−hs))/s de módulo O(min(h,1/|t|)). La identidad de Plancherel con el pulso discontinuo se obtiene primero con el multiplicador suavizado por convolución en log x con una aproximación suave de la identidad, y luego por convergencia local en L² y convergencia dominada en la recta σ. Para h≥1/(4X+4) elegir ε',γ arbitrariamente pequeños; para h menor usar disjunción, dando ‖S_h‖_X²≪hX. Así A(X)≪_ε X^ε. A la inversa basta h=1: por Cauchy–Schwarz y suma diádica la transformada de Mellin del pulso converge holomórficamente en Re s>1/2 bajo ese techo. Coincide allí por continuación con (1−e^(−s))/(sζ(s)) y el numerador nunca se anula en ese semiplano.

**Alcance.** El contramodelo 352 rompe la identidad μ log=−μ*Λ. Con esa identidad exacta se puede cerrar la dependencia recursiva respecto de todas las potencias p^k, k≥2, en la norma crítica. La tarea abierta es controlar la suma firmada sobre p a la escala indicada; el resultado no otorga ese control. La identidad de derivación logarítmica es clásica. Lo que se registra aquí es el coeficiente de absorción y su uniformidad para ventanas indicatrices de cualquier anchura.
