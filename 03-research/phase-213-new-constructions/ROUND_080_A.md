# Corrección de Schur dependiente de los saltos de cada vector

En 079 se utilizó un único número para el cruce con el complemento. Aquí se conserva la dependencia en el vector. Usar coeficientes u_j en la base de indicadores normalizados de la ventana, extendidos por cero fuera de ella, y Δu_j=u_j−u_{j−1} (incluidos los dos bordes). Poner S_T=Σv_n, d=m(π/h)−S_T−4sinh T y M la matriz de W en la base. Para a>0, λ<d, la desigualdad matricial
    
    M−λI ≥ [(1+a)L_h² Δ*Δ + (1+1/a)e_h² I]/(d−λ)

implica λ_W(T)≥λ. Aquí e_h=2h sinh(T)/π. Se puede elegir L_h=O_T(1+log(1/h)) para h≤1, con la fórmula explícita que sigue. Una variante conserva la varianza completa del símbolo, incluidas las fases de todas las traslaciones primas. No se exige que los autovectores de M lo sean de Δ*Δ.

**Multiplicador y saltos.** En la recta usar el símbolo real b(ξ)=m(ξ)−Σ v_n cos(ξ log n). Para una entrada apoyada en la ventana y proyectada después a ella, da exactamente la parte no polar. En la fibra de 079 sean b_k=b((θ+2πk)/h) y w_k los pesos sinc cuadrados. La contribución global al cuadrado de la norma del cruce es exactamente
    
    ∫_{−π}^π |Σ_j u_j exp(−ijθ)|² [Σ w_k b_k²−(Σ w_k b_k)²] dθ/(2π).

Comprimir la salida al intervalo sólo reduce su norma. Es importante formar b_k antes de la varianza para conservar los términos mixtos del peine con el símbolo arquimediano. Esta integral positiva define una matriz de Toeplitz finita G según la longitud de u. Se puede usar G en lugar de L_h² Δ*Δ en el test anterior.

Para una cota más simple poner D₀=m(1)−m(0), M₁=10 como en 079. Para k≠0 vale |θ+2πk|≥|θ|. Monotonía de m y la estimación sobre su derivada logarítmica dan
    
    |b_k−b_0| ≤ d_k := D₀+10 log(1+3π|k|/h)+2S_T,
    L_h² := Σ_{k≠0} d_k²/(π² k²).

Para la primera desigualdad, hasta frecuencia 1 se paga D₀ y por encima de 1 se integra 10 dt/t. La serie para L_h converge y para h≤1 se acota con log(1/h)+log(1+3π|k|). Al centrar la varianza en b_0 y usar w_k≤4sin²(θ/2)/(πk)², Plancherel discreto da la cota L_h²||Δu||². Para el término polar la salida dentro de la ventana es una combinación de exp(±t/2), con norma de su derivada ≤2 sinh(T)||u|| por Cauchy–Schwarz en los dos momentos. El error en L² de sustituirla por sus medias de celda es a lo sumo h/π por la norma de la derivada. La desigualdad de Young separa las dos normas de cruce, y completar el cuadrado con piso d−λ da el certificado.

**Precisión del coste de salto.** En la malla de toda la recta, para el operador arquimediano solo, si P_h es la proyección por medias y Q_h=1−P_h, entonces para f∈H¹(ℝ)
    
    lim_{h↓0} ||Q_h m(D)P_h f|| /[h log(1/h)] = ||f'||/√12.

Para f de banda de Fourier fija y h suficientemente pequeño, en cada fibra sólo la entrada k=0 de f puede ser no nula. Su proyección a la recta de medias tiene masa |f̂(ξ)|² w_0(hξ) en la variable física ξ. Para θ=hξ fija en esta forma, w_0→1 y para cada k≠0, w_k/h²→ξ²/(4π²k²). Además (m((hξ+2πk)/h)−m(ξ))/log(1/h)→1 por la asintótica de P47. La suma de los cuadrados de estas diferencias ponderadas, dividida por h²log²(1/h), tiende a ξ²/12 pues Σ_{k≠0}1/(4π²k²)=1/12. El cuadrado del desplazamiento de la media de fibra respecto a b_0 es despreciable: por Cauchy–Schwarz es ≤(1−w_0) veces la suma cuadrática recién calculada. La cota d_k aporta dominación sumable en k y uniforme en cualquier banda fija. Finalmente ||Δ(P_h f)||≤||f(·−h)−f||≤h||f'||, ya que P_h conmuta con traslaciones enteras de la malla. La cota de salto extiende el límite por densidad a H¹. La identidad es en toda la recta; para el certificado en ventana sólo se utiliza la correspondiente cota superior.

**Alcance.** La penalización de un vector que proviene de un perfil H¹ fijo cuesta O_T(h² log²(1/h)) antes de dividir por d−λ, frente a la penalización constante de 079. Esto no supone que los minimizadores pertenezcan a H¹; 077 sólo da H^s para s<1/2. El piso de 078, la identidad de fibras de 079 y el método de Schur son antecedentes directos. El nuevo test conserva el coste individual y el límite muestra que el logaritmo es real para la malla de indicadores. No se ha verificado todavía el test matricial para ventanas arbitrariamente grandes.
