# Ensamblaje PSD por bloques de tamaño acotado en la base de potencias

Estado: **PROVED analítico; auditorías matemáticas y literales root/casos/mapa aprobadas.** Sin cómputos nuevos ni cambios en papers. Sólo se excluye una clase precisa de certificados en la base original; no se decide el signo de matrices de orden arbitrario.

## 1. Antecedentes y diferencia de objeto

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX01–06, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; búsquedas transversales de diagonal dominance, scaled diagonal dominance, factor-width, sparse SOS y k-local certificates. Lecturas relevantes: POWER_CONE_001§§1–3, POWER_BRIDGE_002; R186_043§7, R186_044§3.3 y N_BUILD018/019. No se halló esta obstrucción literal de soporte coordenado acotado; no se reclama novedad mundial del instrumento clásico de matrices PSD dispersas.

R186_043–044 delimitan Gershgorin y estructuras de M-matriz en otros bloques de acoplamiento; no prueban que cualquier cambio de base falle. N018 trata cálculo de multiplicadores mediante identidades y Cauchy–Schwarz; N019 trata SOS aritméticos y medidas en lags logarítmicos. Aquí cambia la clase exacta: sumas de matrices PSD, cada una soportada en a lo sumo k COORDENADAS de la base de potencias de002. No se identifica esta clase con todos los certificados.

## 2. Una condición necesaria elemental

Fijar k>=1. Si una matriz real simétrica B es PSD y está soportada en S×S, |S|<=k, entonces

 ones^T B ones <= k tr(B).                             (LOCAL)

En efecto una descomposición de B como suma de vv^T tiene cada vector soportado en S; Cauchy–Schwarz da (sum_i v_i)^2<=|S|sum_i v_i². Sumar prueba LOCAL. No se necesita signo de las entradas individuales.

Por linealidad, toda descomposición C=sum_alpha B_alpha en matrices PSD de soporte <=k satisface

 ones^T C ones <= k tr(C).                             (NECESSARY)

Esto incluye sumas finitas y los límites matriciales de tales sumas: NECESSARY es una desigualdad cerrada. Los coeficientes positivos pueden absorberse en B_alpha. La clase se conserva bajo congruencias diagonales invertibles, porque no cambian los soportes ni PSD.

## 3. Bloques de la MISMA escalera fija002

Usar el núcleo completo de001

 K(a,b)=[L(a)+L(b)]/(a+b-1),
 L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

Fijado k, poner n=k+1 y, para enteros N>=1,

 a_j=32+2N+2j, u_j=a_j-1/2, j=0,...,k.

Son nodos de la escalera fija a=32+m de002, no una familia ajena al puente. La representación real positiva de001 da L(a_j)>0. Para cada k fijo,

 L(a_j)=.5 log N+O_k(1), uniformemente j=0,...,k.        (ASYM)

Esto se prueba sin evaluar funciones especiales: a_j/2=N+16+j entero, psi(a_j/2)=H_(N+15+j)-gamma y las comparaciones integrales de sumas armónicas dan H_(N+15+j)=log N+O_k(1). Los dos términos racionales son O(1/N). La cola aritmética está incluida:

 |zeta'(a)/zeta(a)|=sum_(m>=2)Lambda(m)m^(-a)
 <=sum_(m>=2)m^(1-a)
 <=2^(1-a)[1+2/(a-2)] ->0, a->infinito.

Así ASYM conserva toda la forma completa, sin descartar el peine para obtener un signo no demostrado.

Normalizar el bloque por su diagonal positiva:

 C_ij=K(a_i,a_j)/sqrt[K(a_i,a_i)K(a_j,a_j)]
     =[L_i+L_j]/[u_i+u_j] * sqrt[u_i u_j/(L_i L_j)].

Se tiene C_ii=1 exactamente. ASYM y u_i/u_j->1 implican C_ij->1 para todos i,j. Por tanto

 ones^T C ones -> n² > kn = k tr(C).

Existe un N entero finito suficientemente grande para el que NECESSARY falla estrictamente. No se requiere determinar N ni realizar una búsqueda. En ese bloque real de la escalera002 NO existe una suma de matrices PSD de soporte <=k en la base declarada. Por invariancia diagonal, tampoco existe para el bloque K sin normalizar. Si un bloque inicial mayor de la escalera002 admitiera una descomposición con soportes de tamaño<=k, su submatriz principal en estos nodos heredaría la misma propiedad, por restricción de cada sumando PSD. Esto contradice lo anterior y conecta la obstrucción con los bloques iniciales concretos del puente002.

## 4. Dominancia diagonal y alcance

El caso k=2 incluye certificados por sumas de bloques PSD de tamaño2. También falla directamente la dominancia diagonal escalada absoluta: si C es de3 nodos y todos los C_ij>1/2 para i!=j, las condiciones x_i>=sum_(j!=i)|C_ij|x_j con x_i>0 son incompatibles al sumarlas. La confluencia continua o los bloques tardíos anteriores producen esa situación. Que este criterio falle no implica que C sea indefinida.

Para TODO k fijo aparece algún bloque de tamaño k+1 que no admite el ensamblaje declarado. Así no puede cerrarse toda la escalera sumando únicamente certificados PSD apoyados en conjuntos de 2,4,13 o cualquier otro número FIJO de coordenadas originales, aunque se permitan todos esos subconjuntos y pesos positivos.

No se ha probado que el bloque excluido tenga una dirección negativa. La prueba no presupone su PSD. No se excluyen cambios de base generales, bloques cuyo tamaño crezca, complementos de Schur, descomposiciones con una parte PSD global densa ni otros controles firmados de cruces. No se atribuye un fallo a los resultados positivos de dimensiones finitas existentes; sólo se excluye esta regla de ensamblaje local para todos los órdenes. W global y la escalera completa permanecen OPEN.
