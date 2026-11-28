# Ventanas fijadas de paper 46: reproducción independiente

Alcance aclarado por el autor: T=(log 5)/2 y T=2.8022 son parámetros fijados. No se intenta descubrirlos ni optimizarlos. Sí se revisan los argumentos y certificados que pretenden demostrar cotas en esas ventanas. Los programas de esta carpeta de evidencia no modifican manuscritos.

## Resto de cuadratura en la primera ventana

La reconstrucción usa 480 paneles de longitud 1/2 y Gauss–Legendre de 46 nodos, con bolas Arb de 640 bits. La elipse de parámetro ρ=3.2 sobre cada panel tiene semieje imaginario y=(ρ−ρ⁻¹)/8=0.3609375. Para w=1/4±iτ/2, Re w≥1/4−y/2>0. Se tiene |w+8|<130 y Re(w+8)>8.

La recurrencia de digamma y la cota de Binet escrita en el manuscrito dan |ψ(w+8)|<7, |w|⁻¹<15 y Σ_{k=1}^7 |w+k|⁻¹<3. Por tanto |ψ(w)|<25. Al continuar analíticamente el símbolo real se usa (ψ(1/4+iτ/2)+ψ(1/4−iτ/2))/2, no la operación no holomorfa Re ψ sobre τ complejo. Con log π<2, s∞<1, A<3 y cosh(y log 4)<2 resulta |g(τ)|<34.

La cota de Bessel impresa puede reforzarse gratuitamente usando su representación de Legendre:

`j_n(z)=(2i^n)⁻¹ ∫_{−1}^1 exp(izt) P_n(t) dt`.

Cauchy–Schwarz y ∫P_n²=2/(2n+1) dan √(2n+1)|j_n(z)|≤exp(|Im z|). Por ello, para todos los índices usados,

`|√((2i+1)(2l+1)) g(τ) j_i(Tτ) j_l(Tτ)| < 34 exp(2Ty) < 68 < 70`.

Esto evita multiplicar la cota por los índices de las funciones de Legendre. No se necesita asumir el decimal menor 1.5·10⁻⁴³ anunciado en el manuscrito.

Para una función analítica acotada por M=70 en la elipse, los coeficientes de Chebyshev de grado k≥1 tienen módulo ≤2Mρ⁻ᵏ. Gauss de 46 nodos es exacto hasta grado 91. Para cada T_k, el valor absoluto de la integral y el de la regla son ≤2; su diferencia es ≤4. Los grados impares contribuyen cero por simetría. Por suma geométrica el error en [−1,1] es a lo sumo

`8M ρ⁻⁹² / (1−ρ⁻²)`.

Al multiplicar por 480 cambios de variable de factor 1/4 y por 2T/π, resulta un error por entrada menor que **1.282·10⁻⁴²**, y por tanto menor que la bola **2·10⁻⁴²** usada en la reconstrucción. Ésta es una demostración directa del resto suficiente; no presupone una convención de numeración de nodos en el teorema citado.

El programa `evidencia/verificar_restos_46.py` comprueba con predicados de bolas las desigualdades numéricas de esta demostración. También comprueba Λ*₂₈₀<4.5·10⁻²⁰ y Λ*₃₃₀<3.9·10⁻⁷⁰: el primer término de la serie se multiplica por 1/(1−r), con r=c²/(2k+3)², que domina todos los cocientes sucesivos. Resultado guardado en `restos_46_arb.json`.

## Matrices e inercias

`reconstruir_matriz_46.py` genera las matrices de 165×140 en cada paridad, incluyendo la bola anterior. La recurrencia de Bessel se reinicia mediante evaluación directa cuando crece su radio; todas las bolas de Bessel pasan el predicado radio<10⁻⁶⁰. La ejecución reanudada concluyó y escribió `matrices_46_arb.json`.

`verificar_inercias_46.py` construye la matriz de la proposición `prop:lowercert`. Los productos de columnas sobre índices 280≤l<330 se suman explícitamente. La cola de cada columna de G se domina por (ω₊+ω₋)√Λ*₃₃₀; los productos de colas se encierran por Cauchy–Schwarz. Los coeficientes de cosh/sinh se calculan con Bessel I. La cola de su norma se obtiene restando de sinh T±T la suma finita de cuadrados, tomando el extremo superior no negativo.

Se reemplaza únicamente la entrada diagonal del borde por una cota inferior, obteniendo R′≤R. Para el sector impar con c=1/2 se prueba positividad mediante LDL por intervalos. En los demás casos se usa el bloque principal formado por la primera coordenada y el borde: si su determinante es negativo tiene exactamente una dirección negativa; se verifica positividad de su complemento de Schur. En el caso par de W_T se alinea primero la columna del borde mediante una matriz de Householder construida con sus puntos medios; se certifica su invertibilidad mediante ‖HᵗH−I‖∞<1.

**Estado: las cuatro inercias pasaron.** La eliminación LDL directa del complemento de Schur par de W_T pierde precisión por dependencia de intervalos. Se conserva ese intento fallido en el resultado, seguido de una verificación exitosa: se construye L unitriangular con entradas exactas de punto medio y D diagonal positiva; P=D⁻¹ᐟ²L⁻¹ es invertible, y se calcula P S Pᵗ con bolas. Sus diagonales menos la suma de módulos fuera de la diagonal son todas positivas, con margen mínimo mayor que 0.9999999999999999999999. Gershgorin prueba positividad; no se infiere del éxito de una factorización de puntos medios.

| Forma / paridad | μ | Inercia negativa del borde | Evidencia positiva |
|---|---:|---:|---|
| Primitiva par | 2.5·10⁻¹² | 1 | LDL, pivote mínimo >0.00846 |
| Primitiva impar | 3·10⁻¹⁰ | 1 | LDL, pivote mínimo >0.02026 |
| W_T par | 10⁻¹⁸ | 1 | Congruencia certificada y Gershgorin |
| W_T impar | 10⁻¹⁶ | 0 | LDL, pivote mínimo >8.14·10⁻¹⁴ |

El pivote mínimo de la factorización de puntos medios del tercer caso es aproximadamente 0.00044730756, consistente con la tabla del autor, pero el certificado es la congruencia con intervalos y Gershgorin. Resultados en `inercias_46_arb.json`; restos justificados arriba y en `restos_46_arb.json`.

**Dictamen para las cotas pedidas en T=(log 5)/2: (a), mediante esta reconstrucción independiente y las correcciones de redondeo ya señaladas.** Por inclusión de soportes se extienden a ventanas menores: los términos nuevos de la suma de primos no contribuyen cuando las traslaciones de los soportes no se intersectan (la coincidencia en un extremo tiene medida cero). Esto no certifica que el programa original ausente fuera exactamente el mismo.

La ventana 2.8022 sigue pendiente de su filtro y de las 17 verificaciones anunciadas.
