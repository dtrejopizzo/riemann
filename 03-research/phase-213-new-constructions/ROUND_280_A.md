# Un máximo sobre muestras prefijadas mide el exponente de los ceros

Para el perfil canónico T de 276 y sus cortes Y,U, se pueden fijar O(log²(2N) log log(3N)) puntos enteros de la banda, sin consultar el perfil. Si M_x es el máximo de |T| en esos puntos, entonces

    lim_(x→∞) log(1+M_x)/log x = Θ/2.

Los puntos pueden exigirse primos. Así, para el signo global bastaría una sucesión x_j→∞ en que TODO ese conjunto prefijado tenga |T|≤x_j^(1/4+o(1)). La escala 1/4 es para valores individuales; 3/4 era para la suma de 279. No hay que medir la integral ni las otras muestras primas en esta prueba.

**Construcción de los puntos.** Poner k=⌈K log(2N)⌉ con constante fija suficientemente grande. Dividir [Y,U] en intervalos con extremos en progresión geométrica de razón (U/Y)^(1/J), J=⌈log(U/Y)/log(1+1/(Ck))⌉, con C grande fijo. Sus longitudes h son comparables a a/(Ck), siendo a el extremo izquierdo. En cada intervalo usar los k nodos interiores de Chebyshev de primera especie, trasladados y reescalados. Redondear al entero más próximo. En la versión prima se puede tomar el menor primo a la derecha de cada nodo a distancia ≤U^(7/10), por 238. Las distancias mínimas entre nodos y hasta los bordes son ≫h/k²≫U^(7/10), de modo que también las muestras redondeadas quedan dentro y son distintas para N grande. Hay Jk puntos, en el orden anunciado.

**Control entre muestras.** La cota puntual de 278 da |T^(k)(y)|≤x log³(2N) C₀^(k+1)(k!)²/y^(k+1). El Taylor de orden k−1 en a aproxima uniformemente T con error ≤x log³(2N)(C₀ h/a)^k k! C₀/a. Por la elección de C y luego K el error es O(N^(−3)). Para cualquier polinomio P de grado <k se tiene ||P||∞≤2k max_i |P(z_i)| con los nodos exactos z_i: al expandir P en los cosenos del ángulo de Chebyshev la ortogonalidad discreta acota cada coeficiente por dos veces el máximo muestreado. La desigualdad de Markov da ||P'||∞≤2k²||P||∞/h. Así el reemplazo de cada z_i por el entero o primo elegido añade al lado derecho a lo sumo (4k³U^(7/10)/h)||P||∞, absorbible uniformemente ya que h≫U/log³(2N). Aplicado al Taylor en cada celda resulta

    M_x ≤ sup_banda |T| ≤ 4k M_x + O(k N^(−3)).

**Paso al exponente.** Por 279 y Chebyshev, sup_banda |T|≥A(x)/O(U)=x^(Θ/2+o(1)) como cota inferior de exponente. El argumento superior de 279 ya da sup_banda |T|≪_θ(x/U)^θ log⁶(2N) para Θ<θ<1. Si Θ=1 se usa la estimación de orden cero de 278, |T(y)|≪x log³(2N)/Y. El factor de muestreo O(k) desaparece en el exponente. Este resultado concierne al perfil suave fijado de antemano. Alterar unas pocas filas para anular las muestras cambiaría el perfil cuya regularidad sustenta la interpolación.

**Antecedente y límite.** 047 reducía una cuadratura firmada a pocos índices exteriores, con una integral y sumas interiores pendientes. Aquí se recupera el exponente mediante un máximo sin signos en puntos explícitos y sin integral adicional. Cada punto todavía contiene una suma aritmética; el conteo de muestras no aporta por sí solo la cota de cuarto de potencia.
