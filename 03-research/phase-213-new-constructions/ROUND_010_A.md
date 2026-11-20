# Combinaciones de traslaciones próximas de un perfil escalonado

Antecedentes: BUILD084(1)–(2) firma rectas de perfiles físicos escalonados, P47 lem:transl da la matriz de cruces, y lem:mbounds y lem:compact proporcionan crecimiento del símbolo y acotación del peine en ventana fija. La operación aquí usa que todas las traslaciones coinciden salvo por un escalar fuera de tubos alrededor de los saltos. Esto permite afrontar cancelaciones de coeficientes de tamaño arbitrario. Cotejo independiente dirigido, sin pretensión de prioridad.

**Enunciado.** Sea F(t)=exp(t/2)f(exp t), donde f es escalonada con finitos saltos y soporte compacto dentro de (0,∞). Si la energía física sin polos a(F) es estrictamente positiva, existe δ(F)>0 tal que a es estrictamente positiva sobre todo vector no nulo del espacio generado por V_d F, 0≤d≤δ(F). Si F cumple los momentos primitivos, todo el espacio los cumple. Se permiten coeficientes complejos y cualquier número finito de traslaciones.

**Prueba.** Fijar una ventana que contenga los soportes de las traslaciones con 0≤d≤1, trasladando el conjunto si es necesario. El peine comprimido es un operador acotado de norma B, por ser suma finita de traslaciones. Escribimos a(g) como integral de m|ĝ|² con medida dτ/(2π), menos la forma del peine. El símbolo real tiene cota inferior m₀ y tiende a infinito al crecer |τ|. Escoger R con m≥B+2 fuera de [−R,R], tomando m₀≤B+2. Si g está soportado en un conjunto U de medida ℓ, Cauchy–Schwarz da |ĝ|²≤ℓ||g||². Por Plancherel resulta

    a(g) ≥ [2−(B+2−m₀)Rℓ/π]||g||².

En particular a(g)≥||g||² para ℓ suficientemente pequeño y g en el dominio de forma, aun si g no satisface los momentos.

F es de variación acotada y compacta, de modo que su transformada es O((1+|τ|)⁻¹). Como m=O(log(2+|τ|)), el multiplicador m aplicado a F está en L². Restando el peine en la ventana obtenemos h∈L² tal que a(F,g)=〈h,g〉 para los g considerados. En consecuencia |a(F,g)|≤||1_U h|| ||g||.

Sea U la unión de los intervalos [s,s+δ] donde s recorre las posiciones logarítmicas de los saltos, incluidos los extremos. Para 0≤d≤δ y fuera de U se tiene V_d F=exp(−d/2)F casi en todas partes. Por tanto toda combinación Y es exactamente cF+g, con c la suma de los coeficientes ponderados por exp(−d/2) y g soportado en U. Este g pertenece al dominio por linealidad. Al tender δ a cero la medida de U tiende a cero y ||1_U h|| tiende a cero. Elegir 0<δ≤1 de modo que valga el piso anterior y ||1_U h||²<a(F). Entonces

    a(Y) ≥ a(F)|c|²−2||1_U h|| |c| ||g||+||g||².

El lado derecho es una forma definida positiva en (|c|,||g||). Esto prueba el enunciado. Las traslaciones preservan la anulación de ambos momentos por P47 lem:transl.

**Alcance.** BUILD084 permite aplicar el resultado a cada f_k de esa familia, con k arbitrariamente grande. Se obtiene un radio que puede depender de k. La prueba usa la energía positiva del perfil inicial y la acotación del peine visible. Queda pendiente comparar traslaciones con separaciones arbitrarias y demostrar el signo de la ventana completa. Estado PROVED tras revisión matemática independiente.

## Inercia de las réplicas próximas y aplicación a BUILD084

Corolario para la selección de amplificación del índice posterior a 212-84. Sea F un perfil de este lema con energía estrictamente negativa para el peso considerado. Para cualquier número r de traslaciones distintas con desplazamientos en un intervalo suficientemente corto, el Gram tiene exactamente un autovalor negativo y r−1 positivos. Por traslación común basta considerar [0,δ]. Las traslaciones son independientes: el primer extremo izquierdo del soporte esencial deja un intervalo donde sólo interviene el primer perfil y éste es no nulo; se itera tras eliminarlo. El hiperplano de coeficientes con Σc_j exp(−d_j/2)=0, de dimensión r−1, produce funciones soportadas en los tubos pequeños de la prueba anterior. El piso allí sólo requiere norma finita del peine visible y da positividad estricta. Una traslación por sí sola es negativa. Estas dimensiones agotan la inercia.

Con el mismo perfil congelado de BUILD084 (16)–(17) y los mismos desplazamientos se obtiene, tomando el menor de los dos radios, un Gram definido positivo para Λ y uno con exactamente un negativo para (11/10)Λ. En este último caso todas las diagonales son negativas. Esto decide la inercia de un grupo próximo entero para todo r sin invertir matrices. El resultado restringe la amplificación por densificación en un intervalo corto; la interacción entre grupos separados sigue abierta. En particular la amplificación lineal en T planteada en el índice, aun si se probara, es compatible con 026-A, cuyo mayorante en el corte de celdas crece como X/(log X)² para T=(log(X+1))/2. PROVED tras auditoría matemática independiente.

## Descenso cuantitativo del umbral de un perfil por dos traslaciones

Sea F un perfil real escalonado en la variable física como antes, y a_c=A−cΠ la forma con pesos cΛ (Π es la contribución del peine con su signo sustraído). Suponer Π(F)>0. Escribir c*=A(F)/Π(F), J=Σ_s |F(s+)−F(s−)|², sumando los saltos en la variable logarítmica. Para Y_d=F+V_dF el umbral individual satisface, al tender d a cero por la derecha,

    A(Y_d)/Π(Y_d) = c* − J d log(1/d)/(4Π(F)) + O_F(d).

El cotejo distingue este cociente del umbral mínimo sobre todos los perfiles o ventanas de P47. La conclusión cualitativa en c* también se sigue de los tubos de 010 y polarización; el término principal mide el descenso.

En efecto, sea H=V_dF−F. La separación de los saltos implica ||H||²=dJ+O_F(d²): en cada intervalo [s,s+d) la diferencia es el salto con signo cambiado más O_F(d); fuera de ellos la diferencia es O_F(d) sobre un soporte de longitud acotada. Por variación acotada, |Ĥ(τ)|≤C_F min(d,1/(1+|τ|)) para 0<d<1/2, usando el factor de traslación y la cota de Fourier de F. P47 lem:mbounds da m(τ)=log(2+|τ|)+O(1). Por Plancherel,

    A(H)=log(1/d)||H||²+O_F(d).

Para ver el error, integrar el cuadrado de la cota de Ĥ por 1+|log(d(2+|τ|))|. Con u=d(2+|τ|) se obtiene a lo sumo C_F d veces la integral finita de min(1,u⁻²)(1+|log u|) en (0,∞). En una ventana común fija el peine es acotado, por lo que Π(H)=O_F(d). El paralelogramo y la invariancia por traslación dan a_{c*}(Y_d)=−a_{c*}(H)=−Jd log(1/d)+O_F(d), y Π(Y_d)=4Π(F)−Π(H)=4Π(F)+O_F(d). Dividir prueba la fórmula.

BUILD084 (16)–(17) satisface la hipótesis porque a_1(F)>0>a_{1.1}(F); c* está estrictamente entre 1 y 1.1. Para d suficientemente pequeño la suma también es positiva en c=1, por 010. El descenso es local y conserva los dos momentos para F primitivo. PROVED tras auditoría matemática independiente.

## Óptimo local sobre todos los promedios positivos del perfil fijo

Mantener F real fijo con Π(F)>0 y escribir H_μ=∫V_sF dμ(s) para una probabilidad en [0,δ], δ→0. Esta integral existe en norma de forma: las traslaciones son continuas en la norma de Fourier con peso log(2+|τ|) por convergencia dominada y los soportes quedan en una ventana común. Para S,T independientes de ley μ y h=|S−T|, la identidad cuadrática de varianza y la invariancia por traslación dan

    a_{c*}(H_μ)=−(1/2) E a_{c*}(V_hF−F),
    Π(H_μ)=Π(F)−(1/2) E Π(V_hF−F).

Las identidades siguen por polarización e integración de formas continuas en esa ventana. Por la sección anterior, el primer integrando de la derecha (antes del factor −1/2) vale Jh log(1/h)+O_F(h), y el segundo O_F(h). En h=0 se toma cero. El error de reemplazar h log(1/h) por h log(1/δ) está entre 0 y δ/e. Así, uniformemente en μ,

    A(H_μ)/Π(H_μ)=c*−[J/(2Π(F))] log(1/δ) E|S−T|+O_F(δ).

Si G(t)=μ([0,t]), la identidad |S−T|=∫|1_{S≤t}−1_{T≤t}| dt sobre [0,δ] da E|S−T|=2∫G(t)(1−G(t))dt≤δ/2. La medida que reparte su masa por igual entre 0 y δ alcanza la igualdad. Por tanto el ínfimo sobre todas estas medidas es

    c*−[J/(4Π(F))] δ log(1/δ)+O_F(δ).

El par de extremos alcanza el término principal. La fórmula admite átomos o soporte continuo y cualquier número de promedios positivos sucesivos de este F si sus desplazamientos acumulados quedan en [0,δ]. No decide el minimizador exacto al orden δ.

En particular, para el F de BUILD084 y cualquier ε entre 0 y c*−1, elegir δ suficientemente pequeño mantiene todos los cocientes por encima de c*−ε. Aun así existen infinitos descensos estrictos dentro de ese presupuesto. Desde H_0=F formar H_{n+1}=(H_n+V_d H_n)/2, eligiendo 0<d<δ2^(−n−1) suficientemente pequeño para el descenso del perfil actual y evitando el conjunto finito de diferencias entre sus saltos. Cada H_n sigue siendo escalonado en la variable física, Π(H_n)>0 por la cota uniforme del denominador, y los dos conjuntos de saltos disjuntos dan J(H_{n+1})=J(H_n)/2. Sus umbrales decrecen a un límite ≥c*−ε>1. La elección de pasos es existencial. El comportamiento con diámetro total creciente queda abierto. PROVED tras auditoría matemática independiente.

## Qué implicaría un test nulo en una matriz de celdas

Corolario de la expansión de saltos anterior y de la réplica entera de 212-75. Escribir λ=a(F)/||F||² para un perfil físico fijo no nulo, primitivo, constante en las celdas 1,...,N y nulo fuera. Puede tomarse real para decidir el signo de la matriz real. Sean f_q(x)=q^(−1/2)f(x/q) y Y_q=U(f_q+f_{q+1}). Son tests primitivos en celdas enteras. Y_q llega a lo sumo a la celda (q+1)(N+1)−1. Entonces

    a(Y_q)/||Y_q||² = λ − [J_F/(4||F||²)] (log q)/q + O_F(1/q).

En efecto, por traslación común el cálculo corresponde a F+V_dF con d=log(1+1/q). La forma a−λ||·||² se anula en F. En H=V_dF−F, la expansión de 010 da energía arquimediana J_F d log(1/d)+O_F(d) y tanto el peine en la ventana común como el término de norma cuestan O_F(d). Por el paralelogramo el valor de la forma desplazada en la suma es el opuesto del valor en H. Su denominador es 4||F||²−||H||²=4||F||²+O_F(d). Sustituir d da el enunciado.

En particular, encontrar una energía exactamente nula en un test primitivo de celdas no nulo ya bastaría para refutar el signo global: las réplicas consecutivas construyen energías estrictamente negativas para q suficientemente grande. Por 212-75, positividad definida de todas las matrices físicas finitas restringidas a los momentos equivale por tanto a la semidefinitud global. La suficiencia usa el puente de 212-75; la necesidad estricta usa el coste de los saltos J_F>0. No se obtiene una cota uniforme del q requerido al cambiar el perfil. Cotejo con BUILD083 (136)–(137) y la monotonía estricta en ventana: la precisión aquí es el test de celdas y su descenso cuantificado. PROVED tras auditoría matemática independiente.
