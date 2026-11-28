# Ronda 002 — El coste cristalino pasa una prueba adversarial

Fecha y corte: 28/11/2026. Frente independiente de RH. Resultado: **el candidato c_cris tiene un régimen amplio donde vale cero**. Esto descarta presentar como nueva la mera compatibilidad integral de extensiones en Fontaine–Laffaille. Fuera de ese régimen todavía no tenemos un ejemplo aritmético de coste positivo. El ensayo Kummer repetido de §7 también tiene coste cero, como demuestra §8, a cualquier longitud para primos impares.

## 1. Qué medimos y qué podría trivializarlo

Se fijan retículos cristalinos T_0,…,T_{r−1} y clases adyacentes ξ_i en H¹_f(K,Hom(T_{i+1},T_i)), entendido integralmente como preimagen del espacio racional. c_cris es el menor e≥0 que permite una representación cristalina integral filtrada, con graduados identificados con T_i y clases adyacentes π^eξ_i; infinito si no existe.

No fijamos una representación racional global concreta: podemos escogerla. Esta libertad es decisiva. Un coste de retículos dentro de una representación fija puede ser positivo aunque c_cris sea cero. Tampoco fijamos bloques superiores, polarización ni compatibilidad entre diferentes twists. Agregar esos datos define otro problema y debe declararse.

## 2. Cálculo aritmético explícito: coste cero no ramificado

Sea K/Q_p finito y T_i=Z_p con acción trivial. Sean ξ_i clases no ramificadas, determinadas por a_i∈Z_p como valores en Frobenius. Para cualquier longitud r, poner N_{i,i+1}=a_i y los demás coeficientes de N iguales a cero; F=I+N.

Sea n:G_K→Gal(K^nr/K)=Ẑ→Z_p la proyección normalizada por n(Frob)=1. Definir

    ρ(g)=(I+N)^{n(g)}=Σ_{j=0}^{r−1} binom(n(g),j) N^j.

Los polinomios binomiales toman valores en Z_p para n∈Z_p. La identidad binomial, primero en enteros y después por continuidad, prueba que ρ es una representación continua integral. Su filtración por los primeros vectores de la base es saturada; los graduados son triviales y las clases adyacentes son exactamente ξ_i. Es no ramificada, por lo que su racionalización es cristalina. En consecuencia **c_cris=0 para todos estos datos, cualquier p y cualquier r**. No se usa una exponencial con denominadores factoriales no controlados: los coeficientes binomiales ya son integrales.

Ejemplo r=4, a_0=a_1=a_2=1: los bloques de distancias 1,2,3 son n, binom(n,2), binom(n,3). Incluso para p=2 o 3 el coste sigue siendo cero. Un cálculo con exp(nN) podría introducir pérdidas artificiales que este cálculo evita. Este resultado es elemental y no se reivindica como nuevo.

## 3. Régimen Fontaine–Laffaille: todas las clases adyacentes se ensamblan

**Proposición.** Sea p≥3, K=Q_p. Sean M_0,…,M_{r−1} módulos libres Fontaine–Laffaille de rango uno cuyos pesos de filtración h_j pertenecen a una misma ventana [0,p−2]. Prescribir para cada par vecino una extensión libre estricta de M_j por M_{j−1} en esa categoría. Entonces existe un módulo libre Fontaine–Laffaille filtrado por esos graduados que induce simultáneamente todas las extensiones prescritas. No se necesita escalar ninguna clase.

**Demostración constructiva.** Elegir un generador e_j de M_j, con Fil^s M_j=M_j para s≤h_j y cero en caso contrario, y φ_{h_j}(e_j)=u_j e_j, donde u_j∈Z_p^×. Cada extensión vecina admite un desdoblamiento de sus módulos filtrados: la estrictitud y los cocientes libres permiten levantar una base adaptada de cada pieza. En esa base, su dato de Frobenius sobre el segundo generador tiene la forma

    φ_{h_j}(e_j)=u_j e_j+t_j e_{j−1},    t_j∈Z_p.

La restricción al primer generador es el dato ya fijado de M_{j−1}. Formar M=⊕Z_p e_j con Fil^s M=⊕_{h_j≥s}Z_p e_j, y definir, para h_j≥s,

    φ_s(e_j)=p^{h_j−s}(u_j e_j+t_j e_{j−1}),

con t_0=0. Las relaciones φ_s|Fil^{s+1}=pφ_{s+1} son inmediatas. Las columnas φ_{h_j}(e_j) forman una matriz triangular de determinante ∏u_j∈Z_p^×, luego generan M: se satisface la divisibilidad fuerte. Los submódulos generados por e_0,…,e_j son estables y estrictos. El subcociente de cada par vecino reproduce su extensión. Esto prueba la proposición.

Por el functor exacto Fontaine–Laffaille, pasando al límite en las reducciones módulo p^n, obtenemos el enunciado para retículos cristalinos. El functor usual es contravariante: se invierte el orden de los graduados al traducir, sin cambiar la afirmación de existencia. Por tanto **c_cris=0 cuando los datos adyacentes se transportan a estas extensiones libres en una misma ventana Fontaine–Laffaille**. Esta formulación explícita evita esconder una hipótesis de exactitud en un cambio de categoría. En la equivalencia integral habitual dentro de dicha ventana, las extensiones cristalinas de los retículos corresponden a estos datos.

Este ensamblado es una consecuencia directa de la teoría existente. No se presenta como un teorema original ni como una contradicción con el DGA de la ronda anterior: ese DGA no estaba realizado en esta categoría aritmética.

## 4. Bibliografía más próxima y lectura efectiva

**Kalloniatis, *On flagged framed deformation problems of local crystalline Galois representations*.** [Texto primario](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/103849911/On_flagged_framed_deformation_KALLONIATIS_Firstonline17December2018_GREEN_AAM_CC_BY_NC_ND_.pdf), DOI 10.1016/j.jnt.2018.11.010. Leídos definiciones y resultados de §2.1, §2.3 completa y teorema 3.6 con su prueba en §3.1; no todo el artículo. La proposición 2.17 representa extensiones por datos lineales tras desdoblar filtraciones. El teorema 3.6 estudia suavidad de deformaciones con bandera. El argumento constructivo anterior pertenece a ese mecanismo conocido; la suavidad por sí sola no se debe citar como una prueba automática de prescripción de todas las clases adyacentes. Corrección al aviso preliminar: la sección del teorema 3.6 es §3.1, no §3.2.

**Gao, *Crystalline liftings and weight part of Serre’s conjecture*, [arXiv:1504.01233](https://arxiv.org/abs/1504.01233).** Leídas §§5.2–5.3, incluido el argumento de la proposición 5.16; del teorema 7.10 se leyó el enunciado y comienzo de la prueba, no la demostración completa. La proposición 5.16 identifica espacios Ext después de invertir p: la inversa del functor de módulos no es necesariamente exacta integralmente. Su demostración elimina denominadores de bloques de Frobenius y de la acción adicional mediante potencias de p. Es un antecedente directo de cualquier propuesta que llame nueva a la mera finitud de un coste de comparación. No da en esas líneas una fórmula óptima para el coste simultáneo de clases prescritas.

**Riedel, *Integral structures on the finite part H¹_f(K,V) of a crystalline representation*, [arXiv:1609.07627](https://arxiv.org/abs/1609.07627).** Leídos §4 y §5, incluidos teorema 5.2 y prueba; de §3 sólo proposición 3.10 y prueba. No se auditó el artículo íntegro. Trata estructuras integrales y un complejo de dos términos bajo K no ramificado y P(V,1)≠0. No se deduce que la categoría integral tenga todas las extensiones superiores nulas: el complejo de §5 no identifica por sí solo todos los Ext de esa categoría.

El primer intento de descargar Kalloniatis por /portal/files/ devolvió 403; el espejo primario /ws/portalfiles/portal/ permitió leer el PDF. Las referencias Massey de la ronda anterior siguen revisadas sólo a nivel de resúmenes: esta ronda no amplía artificialmente su cobertura.

## 5. Candidato reducido: exactitud integral en la primera salida de FL

**Problema C216-C, abierto aquí.** Fijar p≥5, K=Q_p, cuatro caracteres cristalinos integrales con pesos en [0,p], al menos uno fuera de toda ventana común de longitud p−2, y tres clases cristalinas integrales adyacentes. Suponer que admiten una realización filtrada racional cristalina. Determinar si c_cris puede ser positivo. Si puede, producir un ejemplo con c_cris exacto y un certificado de imposibilidad para e menor; si no puede en ese rango, probar c_cris=0 con hipótesis precisas.

Este enunciado tiene una alternativa falsable. No se conjetura que la respuesta sea positiva. Antes de llamarlo nuevo hay que completar la comparación con los teoremas de levantamiento de Gao y Gee–Liu–Savitt: levantar una representación residual con determinados caracteres no es lo mismo que fijar tres clases sobre Z_p, pero esa diferencia debe demostrarse relevante.

Un refinamiento cuantitativo para investigar es el siguiente: para cada par, medir el índice de la imagen del Ext de modelos integrales en Ext_cris de retículos; después preguntar si esos tres índices bastan para el ensamblado o si aparece un defecto adicional de longitud cuatro. La comparación exige fijar categoría, altura y acción adicional. Un índice de un modelo no debe confundirse con c_cris, pues éste permite cualquier realización cristalina integral.

**Condición para seguir invirtiendo trabajo:** obtener primero un ejemplo aritmético positivo o un teorema de anulación fuera de la ventana anterior. Sin uno de esos dos resultados, llamar a esto una nueva subárea sería prematuro. Si c_cris resulta siempre cero para el régimen estudiado, abandonar ese invariante allí y estudiar datos realmente adicionales —una realización racional fija, polarización o compatibilidad entre twists—, declarando el cambio de problema.

## 6. Resultado de la ronda

Probados aquí como consecuencias elementales de teoría conocida: coste cero no ramificado y ensamblado sin pérdidas en el régimen FL explicitado. No se obtuvo coste aritmético positivo. El progreso consiste en eliminar falsos candidatos de novedad y localizar una pregunta más estrecha, con antecedentes concretos y un criterio verificable de éxito.

## 7. Cálculo inicial p=3: cota 0≤c_cris≤1, mejorada a cero en §8

**Actualización:** la alternativa planteada al final de esta sección queda resuelta afirmativamente por §8. Se conserva la construcción inicial para distinguir la cota obtenida de la optimización del retículo.

Este ensayo es más específico que el problema general del §5. Tomar K=Q_3, T_i=Z_3(3−i) para i=0,1,2,3, y ξ_i=κ(4) en cada Hom(T_{i+1},T_i)=Z_3(1). Con la convención que asigna peso +1 a la ciclotómica, los pesos son 3,2,1,0; con la otra convención se cambian todos los signos. No caben en una ventana FL de longitud p−2=1.

La identificación de Kummer sitúa la clase de una unidad en H¹_f(Q_3,Q_3(1)); κ(4) es integral y no nula. Se usa aquí el cálculo estándar H¹_f(K,Q_p(1))=O_K^×⊗Q_p, explicado también en Bellaïche–Chenevier, *Families of Galois representations and Selmer groups*, capítulo 5 ([texto primario](https://www.numdam.org/item/AST_2009__324__R1_0.pdf)). No se relee en esta ronda la demostración completa de ese cálculo clásico.

**Cota probada: 0≤c_cris(T_i;κ(4),κ(4),κ(4))≤1.** Sea E la extensión cristalina integral de Z_3 por Z_3(1) dada por κ(4). En una base X,Y, escribir

    gX=χ(g)X,    gY=Y+c(g)X,

con c(g)∈Z_3 representante Kummer y c(gh)=c(g)+χ(g)c(h). En Sym³(E⊗Q_3), usar e_j=X^{3−j}Y^j. La entrada (i,j), i≤j, es

    binom(j,i) χ(g)^{3−j} c(g)^{j−i}.

Conjugar por D=diag(1,1,1/2,1/6). La entrada (i,j) pasa a

    χ(g)^{3−j} c(g)^{j−i}/(j−i)!.

Por tanto todas las clases adyacentes son exactamente κ(4); existe realización racional cristalina. Conjugar además por S=diag(1,3,9,27). La entrada de distancia k se multiplica por 3^k, y 3^k/k!∈Z_3 para 0≤k≤3. Todas las matrices resultan integrales, y lo mismo para sus inversas porque la fórmula vale también para g^−1. La filtración estándar es saturada, los graduados son los T_i y las tres clases adyacentes son 3κ(4). Esto demuestra la cota.

No se afirma que el coste sea 1: demostrarlo exige excluir **todas** las realizaciones cristalinas integrales con las clases originales. Que la matriz escogida tenga un denominador 3 en el bloque de distancia 3 no excluye otros retículos o representaciones. El problema siguiente queda reducido a una pregunta binaria concreta:

> ¿Existe un retículo cristalino filtrado de rango 4 con graduados Z_3(3),Z_3(2),Z_3(1),Z_3 y las tres clases adyacentes κ(4)?

Una respuesta afirmativa prueba coste 0; una negativa, junto con la construcción anterior, prueba coste exactamente 1. La construcción posterior de §8 resuelve esa alternativa: el coste es cero. Las factorizaciones de denominadores factoriales de potencias simétricas son conocidas; no se reivindica originalidad de la cota. La potencial contribución sería resolver la realizabilidad con todos esos datos fijos y compararla exhaustivamente con los antecedentes.

## 8. Resolución adversarial del ensayo: el retículo de polinomios enteros da coste cero

**Proposición.** Sea p impar, K/Q_p finito, χ:G_K→Z_p^× un carácter cristalino y c:G_K→Z_p(χ) un cociclo continuo cuya extensión E de Z_p por Z_p(χ) es cristalina racionalmente. Para cualquier n≥1, los graduados T_j=Z_p(χ^{n−j}), j=0,…,n, con todas las clases adyacentes iguales a [c], admiten una realización cristalina integral filtrada sin escalar las clases. Por tanto c_cris=0.

**Prueba.** En E⊗Q_p elegir X,Y con gX=χ(g)X y gY=Y+c(g)X. Poner t=Y/X y considerar en Sym^n(E⊗Q_p) el retículo

    L = ⊕_{j=0}^n Z_p v_j,
    v_j = X^n binom(t,j)
        = X^{n−j} ∏_{k=0}^{j−1}(Y−kX)/j!.

Aunque la fórmula contiene denominadores j!, L es un retículo libre legítimo dentro de la representación racional. No se requiere que coincida con Sym^n del retículo original.

El módulo de polinomios P∈Q_p[t] de grado≤n que toman valores en Z_p sobre todo Z_p es exactamente ⊕_{j=0}^n Z_p binom(t,j). En efecto, binom(t,j) es continuo e integral en Z_p por densidad de los enteros no negativos. Recíprocamente, la fórmula de interpolación de Newton escribe P=Σ_j Δ^jP(0) binom(t,j); si P toma valores integrales, sus diferencias finitas también son integrales.

La acción de g sobre X^nP(t) es

    g(X^nP(t)) = X^n χ(g)^n P((t+c(g))/χ(g)).

La transformación afín (t+c(g))/χ(g) preserva Z_p, y χ(g)^n es una unidad. Por tanto preserva el módulo de polinomios enteros de grado≤n. Aplicando lo mismo a g^−1, obtenemos gL=L. La acción es continua porque la representación racional lo es. La bandera L_j=⊕_{i≤j}Z_pv_i es estable y saturada, con carácter χ^{n−j} en L_j/L_{j−1}.

Falta verificar las clases exactas, no sólo los caracteres. Comparando los dos coeficientes superiores de los polinomios binomiales, el coeficiente de v_{j−1} en gv_j es

    χ(g)^{n−j} [c(g)+(j−1)(1−χ(g))/2].

Tras dividir por el carácter del cociente, el cociclo de la extensión adyacente es c(g)−(j−1)(χ(g)−1)/2. Su diferencia con c(g) es el coborde de la constante −(j−1)/2, que pertenece a Z_p porque p es impar. Las clases integrales son, por tanto, exactamente [c]. Si se desean representantes idénticos, se cambian las secciones de los subcocientes por esas constantes integrales. Finalmente, Sym^n de una representación racional cristalina sigue siendo cristalina. Esto prueba la proposición.

**Aplicación al §7.** Con p=3, χ ciclotómico, c=κ(4) y n=3, obtenemos exactamente **c_cris=0**. El denominador 3 de la base dividida anterior no era una obstrucción intrínseca: el cambio a polinomios binomiales la elimina conservando las clases prescritas. No se ha usado una hipótesis Fontaine–Laffaille; n puede ser arbitrariamente grande.

**Alcance y novedad.** Esta construcción utiliza teoría clásica de polinomios con valores enteros y potencias simétricas. No se reivindica prioridad. Es una nueva comprobación dentro de esta investigación y un descarte efectivo del candidato de coste positivo. El resultado no cubre clases adyacentes arbitrarias, caracteres cociente distintos ni requisitos adicionales sobre una polarización o varios twists. Tampoco demuestra que el coste sea positivo en esos otros casos. Para p=2, la estabilidad del retículo sigue siendo cierta, pero la identificación de clases puede diferir por un coborde racional no integral; no se incluye ese caso en el enunciado.

**Recomendación corregida.** No seguir buscando coste positivo en cadenas de una misma clase con cociente de caracteres común para p impar. La pregunta general del §5 queda abierta, pero el ejemplo de §7 ya no es una frontera útil. El próximo ensayo debe evitar explícitamente esta construcción, y antes de desarrollar una teoría hay que obtener un caso aritmético cuya no trivialidad sobreviva a la optimización sobre todos los retículos.

### 8.1. Extensión a múltiplos integrales: en Q_p cubre todas las clases de Tate consecutivas

La proposición anterior se amplía: para cualquier a_1,…,a_n∈Z_p, se pueden prescribir las clases a_j[c] en las posiciones adyacentes, manteniendo c_cris=0. Si todos los a_j son no nulos, sobre la matriz integral en la base v_j conjugar por

    D=diag(d_0,…,d_n),   d_0=1,   d_j=a_1⋯a_j.

La entrada (i,j), i<j, se multiplica por d_j/d_i=a_{i+1}⋯a_j∈Z_p. La matriz sigue siendo integral para todo g y su inversa, los caracteres diagonales no cambian y la clase adyacente j se multiplica por a_j. No es necesario que D sea invertible sobre Z_p: define un nuevo retículo en la misma representación racional. Si algún a_j=0, dividir la cadena en bloques en esos lugares y tomar la suma directa de las construcciones, con el twist de carácter necesario para cada bloque. Las clases entre bloques son cero.

Para K=Q_p, p impar y χ ciclotómico, Kummer identifica

    H¹_f(Q_p,Z_p(1)) = (Z_p^×)^∧_p ≅ Z_p.

No hay raíces de unidad de orden p en Q_p; el factor de orden p−1 desaparece en la completación y 1+pZ_p es de rango uno, generado topológicamente por 1+p. Así todas las clases adyacentes son múltiplos integrales de κ(1+p). En consecuencia, **para Q_p y p impar, cualquier cadena de retículos de Tate consecutivos y cualesquiera clases cristalinas integrales adyacentes tiene coste cero, a cualquier longitud**.

Esto elimina toda esa familia de ensayos, no sólo el triple κ(4). Un siguiente ensayo debe cambiar realmente los datos: por ejemplo, cocientes de caracteres distintos o un campo K donde las clases escogidas no pertenezcan al mismo submódulo cíclico. No se afirma que tales modificaciones produzcan coste positivo.

Verificación auxiliar independiente: [check_binomial_lattice.py](experiments/check_binomial_lattice.py) comprueba por diferencias finitas los coeficientes de χ^n binom((t+c)/χ,j), su integralidad, diagonales y primera superdiagonal. La ejecución reportó 7040 columnas verificadas para p=3,5,7 y n=1,…,8. Es un control finito de las fórmulas; la demostración para cualquier longitud es la de §8.
