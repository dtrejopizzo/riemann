# Altura suficiente lineal y 500 millones de polos reales

Sea G=3·10¹². Para cualquier listado con n≤500000000 polos −v_j reales, v_j>1/2, contando repeticiones, y todo numerador complejo de grado <n, la forma completa cumple W(f)≥exp(−35000000000)||f||₂². Para orden general n basta que se verifiquen los ceros hasta G₀=max(G,10000(2n+8)). Esta última afirmación es condicional para G₀>G. Se abandona la exigencia de positividad en bandas disjuntas con borde duro. A continuación se suman bandas ponderadas multiplicativamente.

**Dos desigualdades polinómicas.** En [−1,1] poner w_j=(1−x²)^j y ||p||_j²=∫w_j|p|². Para grado ≤d y entero j≥0,

    ∫w_{j+1}|p'|² ≤ d(d+2j+1)||p||_j².

En efecto el operador −w_j⁻¹(w_{j+1}p')' es simétrico por partes y conserva grados, con coeficiente principal k(k+2j+1) en grado k. En la base de polinomios ortogonales de grados sucesivos es diagonal. Para m=2n+8 y d<m, integrando por partes el término cruzado en el cuadrado de la derivada se obtiene

    ∫(1−x²)|(w_m^(1/2)p)'|² + m²||p||_{m−1}²
      = m(m+1)||p||_m² + ∫w_{m+1}|p'|².

Por la primera desigualdad el miembro derecho es ≤(m+d)(m+d+1)||p||_m², de modo que ||p||_{m−1}²≤5||p||_m². Aplicar ahora la primera desigualdad con j=m−1: ||p'||_m≤√15 m||p||_m.

**Muestreo con peso.** Para I=[A,4A/3], H=A/3, x=2(t−A)/H−1, poner w_A(t)=w_m(x), cero fuera de I. En norma L²(w_A dt) la derivación tiene norma ≤8m/H y la misma cota itera en las derivadas de p. La variación total de w_A|p|² cuesta ≤36(m/H)∫w_A|p|²: la derivada del peso cuesta ≤(4m/H)∫w_{m−1}|p|² y el otro término ≤(16m/H)∫w_m|p|² (pesos reescalados). No hay contribuciones de extremos. Para A≥3G/4 y t∈I la fórmula Z3 sigue teniendo resto ≤log A y derivada principal entre 0.14 log A y 0.17 log A. Integrar por partes como en 202 da constantes de muestreo l log A y h log A, con l=0.14−36m/H y h=0.17+36m/H. La suma discreta cuenta cada ordenada con peso w_A(γ) y con multiplicidad.

**Control de los desplazamientos.** Usar la aproximación de 203 sobre I y su reflejo: U=P Q, grado <m, |U−F|≤10⁻⁴|F| tanto en el eje de ordenadas como en los puntos desplazados |δ|≤1/2. Los cocientes de radios empleados en 203 siguen siendo válidos para A≥3G/4. En cada semieje, el vector X de valores U(iγ) se mide en ℓ² con pesos w_A(|γ|). Taylor y la desigualdad superior de muestreo aplicada a cada derivada dan error relativo en U de a lo sumo √(h/l)[exp(4m/H)−1]. Para n≤500000000 y A≥3G/4 se tiene m/H<0.001334, l>0.091 y h<0.219. Incluyendo el error de aproximación de ambos vectores como en 203, cada vector desplazado verdadero de F dista de X en norma a lo sumo 0.01||X||. Por tanto la suma ponderada real domina 0.97||X||², que a su vez, incluyendo ese factor 0.97, domina ∫_I w_A(t)|F(±it)|²dt pues 0.97·l·log A·(1−10⁻⁴)²>1.

**Reconstrucción sin pérdida de borde.** Integrar en A con medida dA/A para A≥3G/4. Para t≥G el peso recuperado es exactamente la constante positiva
     
    J_m=∫_{3/4}^1 w_{bt}(t) db/b,

independiente de t por homogeneidad. Para t<G se obtiene entre cero y J_m. La suma espectral de 201 converge absolutamente para cada F; la integral del peso en cada ordenada es ≤J_m, justificando el intercambio incluso con signos. Tras dividir por J_m, todos los ceros por encima de G tienen su coeficiente original. Bajo G la parte de peso que falta se restituye porque sus contribuciones son cuadrados. El lado continuo es ≥∫_{|t|≥G}|F(it)|²dt. Esta operación usa de manera esencial que las bandas se solapan y que la zona de transición cae bajo la altura verificada.

**Norma y escala.** En la primera banda completa I=[G,4G/3], el argumento de extrapolación final de 203 para el numerador ORIGINAL da energía baja/alta ≤6n²(27·9·10¹²)^(2n). Su logaritmo es <34000000000 en el rango declarado. Plancherel demuestra el piso anunciado. Para cualquier otro orden tomar A≥3G₀/4; entonces m/H≤4m/G₀≤0.0004 si G₀≥10000m. El mismo razonamiento da signo estricto si se dispone de verificación hasta G₀. Esto mejora la ley cuadrática de 203 a lineal. Sin esa verificación la porción de ceros con peso incompleto no tiene signo demostrado. No se concluye positividad en una banda de extremos duros a altura lineal, ni positividad global.

**Antecedentes.** La aproximación racional local viene de 203 y el muestreo por Z3 de 202. La estimación de Jacobi con exponente proporcional al grado evita el crecimiento cuadrático de Markov en los extremos; la integración en escala restaura exactamente los pesos espectrales altos que se perderían al introducirla en una partición disjunta.

La auditoría independiente comprobó las cotas de derivación y variación, los factores de reescalado, las constantes para 500 millones y la recuperación del peso. Equivalentemente J_m=∫_{−1}¹(1−x²)^m/(7+x)dx; el mismo factor aparece en ambos lados y no reduce el margen.
