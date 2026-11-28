# Ronda 003 — Defecto dyádico y un coste aritmético exactamente igual a uno

Corte: 28/11/2026. Continuación de ROUND-002, §8. **Resultado:** la generalización a p=2 con las mismas clases adyacentes es falsa. Sobre Q_2, repetir κ(3) en una cadena de tres o más graduados de Tate consecutivos da c_cris=1, a cualquier longitud. Es una consecuencia de una obstrucción cup clásica, no un descubrimiento de obstrucciones superiores nuevas.

## 1. El medio coborde es la clase Kummer de −1

Sea χ:G_{Q_2}→Z_2^× el carácter ciclotómico. El cociclo

    δ(g)=(1−χ(g))/2

toma valores en Z_2(1), porque χ(g) es impar. Es un coborde racional, pero su clase integral τ no es cero. En efecto, escoger raíces compatibles de −1 dadas por ζ_(2^(m+1)). El cociclo Kummer de −1, expresado mediante ζ_(2^m), es (χ(g)−1)/2 módulo 2^m. Por paso al límite,

    [(χ−1)/2]=κ(−1),    [δ]=−κ(−1)=κ(−1).

La última igualdad usa 2κ(−1)=κ(1)=0. La clase es no nula: su reducción módulo 2 corresponde a Q_2(i)/Q_2. En particular, aquí dividir un coborde por 2 cambia la clase integral.

En el retículo binomial de la ronda anterior las clases adyacentes son

    [c]+(j−1)τ,     j=1,…,n.

Para c=κ(u), alternan κ(u),κ(−u),κ(u),κ(−u),…. El retículo sigue siendo estable y cristalino racionalmente; lo que falla es que tenga todas las clases originales.

## 2. Por qué centrar los binomiales o hacer un twist común no lo arregla

Sustituir binom(t,j) por binom(t−λ,j), para un desplazamiento racional λ que permita un retículo estable, cambia el cociclo afín a c+(1−χ)λ. El cociclo adyacente j queda

    c+(1−χ)(λ+(j−1)/2).

La diferencia entre dos posiciones vecinas sigue representando τ. Por tanto, si τ≠0 y hay al menos dos posiciones adyacentes, ningún desplazamiento único hace que ambas clases sean [c]. Esto descarta esa familia de reparaciones; no pretende clasificar todos los retículos.

Un twist común de toda la representación conserva los cocientes de caracteres de los graduados y las clases de sus extensiones. Tampoco elimina τ. Twistear los graduados por separado modifica los datos prescritos y no resuelve el problema original.

## 3. Obstrucción binaria que excluye TODA realización

Si existen tres graduados T_0,T_1,T_2 y clases adyacentes a,b en una representación triangular integral, el producto Yoneda a∪b debe ser cero en H²(K,Hom(T_2,T_0)). Se ve directamente en la ecuación del bloque (0,2): ese bloque es una primitiva del producto de los dos bloques adyacentes, con los twists correspondientes. La misma condición subsiste después de reducir módulo 2.

Para graduados Z_2(2),Z_2(1),Z_2, la acción ciclotómica es trivial módulo 2. La reducción de κ(u)∪κ(u) corresponde al símbolo de Hilbert (u,u)_2. Para una unidad impar,

    (u,u)_2=(u,−1)_2=(−1)^((u−1)/2).

Así, si u≡3 (mod 4), el producto módulo 2 es no nulo. No puede existir una realización integral con dos clases adyacentes iguales a κ(u). Una cadena más larga tampoco puede existir: su subcociente de tres graduados daría precisamente la realización excluida.

En particular, κ(3) es una clase cristalina integral no torsión —3 es una unidad, y no una raíz de unidad— y sus repeticiones tienen coste al menos uno. La clase torsión κ(−1) da también un ejemplo, pero κ(3) evita que el fenómeno se reduzca a prescribir clases puramente torsión.

No hace falta recurrir a la fórmula completa de Hilbert para verificar la obstrucción concreta: si u≡3 (mod4), una solución primitiva de z²=u x²+u y² implicaría z²+x²+y²≡0 (mod4), imposible para una terna primitiva. Esto prueba (u,u)_2=−1 mediante la definición del símbolo.

## 4. Una potencia de 2 siempre basta en la familia repetida

Sea K/Q_2 finito y E una extensión de Z_2 por Z_2(χ), dada por un cociclo integral c, con racionalización cristalina y χ cristalino. En Sym^n(E⊗Q_2), la base de potencias divididas

    w_j=X^(n−j)Y^j/j!,   j=0,…,n,

tiene matrices con entrada (i,j)

    χ(g)^(n−j) c(g)^(j−i)/(j−i)!.

Conjugar por D=diag(1,2,…,2^n). Para k=j−i la entrada se multiplica por 2^k. Como

    v_2(k!)=Σ_{r≥1} floor(k/2^r) ≤ k−1   para k≥1,

el cociente 2^k/k! es integral. Las matrices y las inversas son integrales; la bandera estándar es saturada y sus clases adyacentes son exactamente 2[c]. La representación racional sigue siendo cristalina. En consecuencia c_cris≤1 para cualquier longitud en esta familia, sin restricción Fontaine–Laffaille.

**Teorema calculado.** Para K=Q_2, n≥2, T_j=Z_2(n−j), j=0,…,n, y todas las clases adyacentes κ(u), con u∈Z_2^× y u≡3 (mod4),

    c_cris(T_j; κ(u),…,κ(u)) = 1.

La cota inferior del §3 y la superior anterior son independientes de n. No hay crecimiento de una pérdida superior con la longitud. Para n=1 sólo se prescribe una extensión y el coste es cero.

## 5. Lo que no se ha resuelto ni se deduce de esto

Para u≡1 (mod4), el cup reducido anterior se anula. Eso no prueba por sí solo coste cero en cualquier longitud bajo la condición cristalina y con clases integrales fijadas. Aquí sólo establecemos la cota 0≤c_cris≤1 para esa familia; no afirmamos que la disyuntiva sea una pregunta nueva.

La vanishing de Massey mod 2 cuando el producto está definido no elimina la obstrucción del §3: allí el triple repetido ni siquiera satisface la condición cup necesaria. Tampoco proporciona automáticamente un sistema compatible sobre todas las potencias de 2, una realización sobre Z_2 y la condición cristalina.

## 6. Fuentes primarias, cobertura y filtro de novedad

- **Serre, A Course in Arithmetic**, capítulo III, §1.2, teorema 1, p.20 y demostración dyádica p.22 ([PDF primario](https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf)). Inspeccionadas visualmente esas páginas y p.18 sobre cuadrados dyádicos; no el libro entero. La fórmula del símbolo y el argumento módulo 4 son clásicos.
- **Colliot-Thélène–Skorobogatov, The Brauer–Grothendieck group**, §1.3.4 ([texto de autores](https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf)): consultado el pasaje sobre Kummer, productos cup y álgebras cíclicas. Sirve para identificar la reducción cohomológica con el símbolo; no se auditó todo el capítulo.
- **Merkurjev–Scavia, On the Massey Vanishing Conjecture and Formal Hilbert 90**, [arXiv:2308.13682](https://arxiv.org/abs/2308.13682): leída la introducción con definición de Hilbert90 formal y teoremas 1.3–1.4; no sus demostraciones. Sus conclusiones citadas son mod p; las hipótesis usan además levantamiento de H¹ a potencias de p. No se debe confundir esto con una certificación de realizaciones cristalinas integrales.
- **Guillot–Minač**, [arXiv:1711.07711](https://arxiv.org/abs/1711.07711): sólo resumen primario, sobre cuatro productos mod p y condiciones sobre campos locales. **Sharifi**, [arXiv:math/0308165](https://arxiv.org/abs/math/0308165): sólo resumen primario, que ya trata Massey con raíces de unidad de orden potencia de p. Ambos deben entrar en una búsqueda seria de prioridad; no se presenta aquí un teorema integral nuevo basado en sus resúmenes.

**Dictamen:** se obtuvo un ejemplo aritmético positivo y exacto del coste definido en fase216. El mecanismo es enteramente clásico y binario. Este cálculo valida que el invariante no es siempre cero, pero no acredita una conexión matemática inédita ni una nueva subárea.

Control auxiliar reproducible: [check_dyadic_cost.py](experiments/check_dyadic_cost.py), con 100 valoraciones factoriales, 128 ternas módulo 4 y 256 identidades de cociclo verificadas. No reemplaza la prueba general ni modela por ordenador el grupo de Galois.
