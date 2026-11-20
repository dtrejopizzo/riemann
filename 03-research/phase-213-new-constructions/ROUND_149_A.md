# Qué pendientes polinómicas se pueden certificar tras cancelar las ordenadas verificadas

Mantener la misma c=1.25·10^(−25), W=cT y la normalización gaussiana de 148. Para grado d≤floor(T/2000) la cuadrática ORIGINAL de 148 tiene ya un techo polinómico uniforme en T, que es el tipo de cota exigido por el criterio para esa pendiente. Además se obtiene negatividad estricta uniforme introduciendo una traslación aleatoria fija de varianza <0.06: para B independiente de Y, definido abajo,

    E[P(Y/√W)² U(T+Y+B)] = 1/ζ(1/2) + O(exp(−.005T)).

El error es uniforme para todos los polinomios reales unitarios de esos grados. El nuevo promedio conserva la implicación al signo al probar todas las pendientes de 148.

**Traslación.** Tomar B suma de signos equiprobables independientes multiplicados por π/(2γ), con un factor por cada cero de ordenada positiva γ≤3·10¹², repetido según su multiplicidad. Son exactamente las ordenadas del enunciado Z2 del paper 47; la definición matemática usa sus valores exactos. Su transformada M(s) es el producto finito de cosh(πs/(2γ)). Tiene M(0)=1, se anula al menos con la multiplicidad necesaria en cada polo crítico del rectángulo de 148 y no tiene ceros con Re s>0. Es acotada uniformemente en altura en cualquier tira vertical fija porque B tiene soporte compacto. Su varianza vale (π²/4)Σ_{0<γ≤G}1/γ² con multiplicidades. Por Z1, 1/γ²≤(1+1/(4·14²))/(γ²+1/4). La suma parcial de los últimos términos está acotada por la suma de Re(1/ρ) sobre todos los ceros, pues cada par crítico contribuye 1/(γ²+1/4) y cada término restante es positivo. La identidad clásica de Hadamard da para esa suma 1+γ_E/2−log(4π)/2<0.024, lo que prueba el techo de varianza anunciado.

**Estimación en el contorno.** En 148 tomar κ=1/2000 y desplazar desde σ=.501 hasta −1/4 con altura fija 2.99·10¹²<G'<3·10¹² que evite ordenadas. El exponente por T está acotado por

    σ+c(σ²−τ²)/2 + 2√(cκ) |σ+iτ|.

Para |τ|≥2.99·10¹² el mayorante usando |σ+iτ|≤|σ|+|τ| decrece con |τ| en la tira; en σ=.501, |τ|=2.99·10¹² ya da menos de −.010. Esto controla horizontales y colas derechas, conservando margen y decaimiento integrable en las colas. En σ=−1/4, maximizar −cτ²/2+2√(cκ)|τ| cuesta a lo sumo 2κ=.001. La línea derecha inicial está en la región de convergencia absoluta. Con el factor M(s) sólo contribuye el polo real; en s=0 la normalización da exactamente el sesgo. Se obtiene el error enunciado para la forma trasladada.

Para la forma original sobreviven los polos críticos, pero en ellos se puede usar que |exp(iγY)|=1. Cada residuo de multiplicidad m está acotado por un polinomio en T uniforme en P: al derivar a lo sumo m−1 veces se obtienen factores T y momentos E[P² |Y|^k]. Multiplicar por la coordenada en la base ortonormal de Hermite sube o baja el grado con coeficientes ≤√(d+k+1), por lo que esos momentos son O_k((1+√(W(d+k+1)))^k). El número de polos en el rectángulo es finito. No se presupone que sean simples ni un valor numérico de las constantes.

**El criterio sobre todas las pendientes se mantiene.** Bajo RH desplazar la función U por B conserva la cota de 148 pues E exp(εB) es finita. Si hay un cero fuera de línea, modular en Y la gaussiana como en 148: el contorno del promedio de U(T+Y+B) modulado contiene M(s)R(s), con M no nulo en cada polo con parte real positiva. El máximo positivo único y la aproximación por Taylor de 148 siguen válidos, con constante extra E exp(B/2) en la cota del error. Así alguna pendiente superior da cocientes positivos exponenciales si falla el signo. Esto no afirma que la pendiente 1/2000 baste para detectarlos.

**Alcance.** El salto de pendientes para el techo polinómico en la cuadrática original se debe a estimar los residuos críticos por unitariedad. Para obtener signo estricto se cancela su contribución mediante una distribución positiva que sigue viendo los polos fuera de línea. 122 ya utiliza cosh para concentrar un test en un cero; aquí se coloca un producto de factores para anular una lista finita en la media aritmética. No se construyó una tabla numérica de las traslaciones ni se verificó una ventana adicional de P47.
