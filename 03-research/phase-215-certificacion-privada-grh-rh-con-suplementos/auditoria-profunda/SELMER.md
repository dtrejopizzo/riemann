# Auditoría profunda de P55: Selmer y Ribet

Fecha: 2026-11-28. Fuente de líneas: `04-papers/55-covolume-theorem-regular-families-of-twists/main.tex`. Este registro continúa `04-selmer-hodge.md`. No se modificó el paper.

## Estado vigente después de las tandas

Los pendientes de las primeras tablas se recorrieron en §§6–14: G123/G45, Selmer y Ribet, clases impares, pérdida local, Fitting, norm, cadena esférica, Higman y sumas. **No se detecta una hipótesis residual omitida en Ribet.** Hay errores literales (b) en las frases de raíces/generador de §6 y en el polinomio fijo para todo elemento de inercia de §11.1. Las correcciones se explican allí y no cambian las cotas. La convención base level/e_c exige aclaración y una construcción explícita que preserve e_c; §11.2 proporciona una reparación con el mismo N_ch, separada de la construcción escrita. Por ello no se emite un (a) indiscriminado del paper tal como está escrito. Los argumentos reconstruidos se califican individualmente, con sus entradas de P49/P53/P54 y los datos de P46.

## Obligaciones resueltas en esta tanda

| Obligación | Dictamen | Dependencias y alcance |
|---|---|---|
| `pg:burnside`, 805–830 | **(a)** | Da imagen matricial integral para cada retículo, a partir de las hipótesis locales impresas. |
| `pri:ribet-poly`, 2498; `pri:ribet-elt`, 2518 | **(a)** | La construcción por Cayley–Hamilton es integral y funciona sobre O/p para p no unidad, sin hipótesis p primo. |
| Bloque principal de `pri:ribet`, 2605–2619 | **(a)** | Usa exactamente la imagen M_r(O) de (1); la extracción de una matriz por bloques se justifica mediante unidades matriciales. |
| Caracteres y gluing de `pri:ribet`, desarrollo 7199–7425 | **(a)** | Se reconstruyeron tied rows, common unit rows, separación con coste C, Fitting y extracción del coeficiente. Queda como entrada la cota triangular (7), no una hipótesis de separación residual no impresa. |
| `pll:ribet`, 3408–3446 | **(a)** | Toda clase que obedece las relaciones proviene de una clase cristalina de un subretículo de una suma de los u_x. No requiere irreducibilidad. |
| `pse:A`, 1600 aprox.–1658 | **(a)** | Construcción por ideles/Kummer/Chebotarev, también para ℓ=2. |
| `pse:restrict`, `pse:span`, `pse:mirror`, 1720–1843 | **(a)** | La condición fuerte ζ_*²−1 unidad está en la definición de Selmer datum, 995; no basta ζ_*−1. No se divide por 2. |
| `pse:tilting` y `pse:step`, 1847–1915 | **(a)** | La pendiente evita a lo sumo 2n_i e+1 residuos, simultáneamente para todas las potencias de la uniformizante. |
| `pg:poly`, 1195–1255, ensamblaje Selmer | **(a), bajo los inputs locales ya identificados** | El descenso usa longitud no normalizada para terminar, y luego recupera la longitud normalizada. La cota no pierde un factor de ramificación del anillo de coeficientes. |

Esto todavía **no certifica pg:I, pg:II y pg:III completos**. Las obligaciones pendientes se enumeran al final; no son acusaciones de falsedad.

## 1. Dónde se usa la irreducibilidad, y por qué vale a potencias

En `pg:burnside`, las diferencias de autovalores de la inercia son unidades. Los proyectores espectrales son por tanto polinomios integrales en u(s): el retículo, y no sólo el espacio racional, se descompone en líneas. Frobenius las permuta transitivamente. Después de toda extensión del cuerpo residual, una subrepresentación estable por s es suma de esas líneas; la transitividad obliga a que sea cero o todo. Burnside sobre el cuerpo residual y Nakayama en el módulo finito M_n(O) dan la igualdad integral

`span_O{u(g)}=M_n(O)`.

No se infiere esa igualdad de una mera irreducibilidad en característica cero. `pg:cyclic` verifica que la condición sobre autovalores sobrevive a quitar la parte ℓ-primaria de las raíces: como r es potencia de 3 y p≡1 mod 3, una colisión forzaría `x²+x+1` a ser potencia de un solo primo; su valoración 3 es exactamente 1 y el número es >3, contradicción. Para ℓ igual a uno de los primos de nivel se utiliza el otro. La comprobación del input automorfo que identifica esos autovalores es una obligación distinta, `pga:G45`.

La igualdad integral implica su reducción módulo toda potencia de la uniformizante. En el bloque de Ribet, sean d=r′ y m=#gen. Las filas por bloques evaluadas en ρ_π forman un módulo estable por multiplicación a izquierda por M_d(O). Sea L⊂O^(dm) el módulo de las filas escalares que aparecen. Mediante E_ij se aísla una fila y se sitúa en cualquier posición: toda matriz con d filas en L se obtiene de una fila por bloques ligada. Se elige una base de L por Smith, se agrupan sus dm filas en m bloques de d filas y se obtiene la matriz B₀ usada por el paper. La longitud del cociente O^(dm)/L es la del dual aniquilado en (K/O)^(dm), ≤b_ρ. Su determinante tiene exactamente esa valoración. No hay que multiplicar b_ρ por d ni suponer que un retículo racional elegido sea canónico.

La normalización por γ_π es válida porque ρ_π(γ_π)=ζ_π I y ζ_π−1 es unidad. Las filas normalizadoras fuerzan el cociclo a anularse en γ_π. La existencia de este escalar también implica que las matrices ρ_π(g)−1 generan M_d(O): de `(γ_π−1)g=(γ_π g−1)−(g−1)` se recuperan todas las matrices ρ_π(g).

## 2. Ribet integral: construcción y caracteres

`pri:ribet-poly` trabaja en un módulo sobre Λ[X] donde X actúa por **multiplicación derecha por ρ₀**. Esto conmuta con la acción izquierda de Λ; no requiere que ρ₀ sea central. El ideal utilizado allí es bilateral. El ideal inicialmente ligado es sólo izquierdo, pero `pri:ribet-elt` pasa al ideal de anulación de todas las trazas, que es bilateral por ciclicidad de la traza. Ésta es la justificación necesaria para el uso de Cayley–Hamilton. Amitsur conserva coeficientes integrales y evita dividir por factoriales.

En los caracteres, olvidar las coordenadas δ_v fuerza c(δ_v)=0 por las filas de generadores. No es una conclusión obtenida al dividir por o_v(1). Esos factores entran después en el determinante de las filas de δ_v.

La construcción simultánea `prm:unit` tampoco divide por las diferencias de caracteres. Si w sirve para los caracteres de E′, y m_j da las filas unidad para el carácter nuevo, se reemplaza

`w → w+Σ_j(δ_ij−w_j)m_j`.

En los caracteres anteriores los coeficientes añadidos son cero; en el nuevo corrigen la fila a la unidad. Esta inducción es válida incluso cuando los caracteres son congruentes módulo ℓ.

Para separar después las filas de los caracteres sí se usan los q_e, con valores C en el carácter e y cero en los demás. Se construyen porque el producto de diferencias **divide C**; no se afirma que esas diferencias sean unidades. En la matriz final las filas de s llevan CB_e, y las de δ_v llevan o_v(1). Así aparece exactamente

`c_ch=C^(#s) Π_v o_v(1)`.

El cociente por el ideal de monomios no divisores de X_J controla todos los términos inferiores. `prm:coeff` prueba por telescopía que un error ζ_e∈(n:X_<e), multiplicado por los factores anteriores, ya está en n. Por tanto el coeficiente de X_J es el producto de las constantes Γ_e(0), con los factores indicados de B₀, C y c_ch. No hay una inferencia inválida a partir de una sola especialización de los parámetros.

El paso a K/O de `pri:divisible` usa que las relaciones hacen que un cociclo esté determinado por un número finito de valores. Cada cociclo tiene entonces orden finito acotado por el de esos valores. Si un módulo de torsión tiene su p^M-torsión de longitud ≤b para una potencia de valoración >b, no puede contener un elemento de orden mayor: un múltiplo produciría un submódulo cíclico de longitud >b dentro de esa torsión. Esto justifica el paso al límite sin presuponer finitud del grupo divisible.

## 3. El paso local no cambia la categoría de retículos

En `pll:ribet`, Y=⊕End_O(u_x) lleva la acción **por multiplicación izquierda**. Por ello Y es suma de copias de los u_x y pertenece a C. Con acción por conjugación esta afirmación sería falsa; el texto no usa conjugación.

El submódulo S generado por `a(g)=(u_x(g)−1)_x` es estable pues `g a(h)=a(gh)−a(g)`. Es finito libre sobre el DVR. Las relaciones de z definen un mapa equivarante S→T/ℓ^M. Falta comprobar que a, visto con valores en S, sea cristalino; no basta que sea coborde en Y. El paper lo prueba: la clase de 1 en (Y/S)_Q es invariante, y la exactitud de D_cris sobre una extensión común E′ permite levantarla a una sección invariante en B_cris⊗Y. El promedio por Γ/Γ′ se hace **en espacios Qℓ-vectoriales**, donde el índice es invertible, incluso si ℓ lo divide. Restar esa sección de 1 da un período en B_cris⊗S que trivializa a. No se divide S por el índice y no se promete una sección integral falsa.

Esto certifica el mecanismo que conecta las relaciones de Ribet con la clase C_v. La cota numérica del defecto sigue dependiendo del resultado de cup products de P56, cuya obligación cohomológica fue cerrada en las secciones 5–6 de `HODGE.md`.

## 4. Twists: pequeñas potencias y ℓ=2

En `pse:A`, se escoge T que genera el grupo de clases y es disjunto de las inercias prescritas. Las extensiones de Kummer por raíces ℓ^N de T-unidades son no ramificadas en esas inercias. Chebotarev da un primo de norma racional q≡1 mod ℓ^N donde todas esas unidades son potencias ℓ^N. El carácter local se extiende a ideles porque mata precisamente las T-unidades. Antisimetrizar `θ(y/ȳ)` no requiere dividir por 2: en P y P̄ distintos la inercia normalizada aún tiene valor 1. Ajustar Frobenius por una potencia de esa inercia hace λ(φ)=0 sin salir del abierto prescrito.

`pse:mirror` usa ζ_*²−1 unidad para deducir Ψ=0 de la antisimetría y la conjugación por γ_*. Éste es el sustituto de una división por 2 y funciona en ℓ=2. La condición aparece expresamente en 995, y (M5) implica tanto ζ_*−1 como ζ_*²−1 unidades. Con M_n(O) se demuestra que los valores de un cociclo primitivo generan todo T/a, también cuando a es una potencia pequeña; la demostración usa unidades matriciales, no sólo un argumento racional. La restricción al subgrupo U es inyectiva por Sah, con un escalar cuya diferencia de 1 es unidad.

En `pse:tilting`, la matriz auxiliar actúa sobre una preimagen libre de rango m del módulo finito de valores. El conjunto malo son las raíces residuales de su polinomio característico monico: como máximo m. En el descenso, m=2n_i; evitar la unión para todos los exponentes 1,…,e y el residuo cero da el umbral impreso `#k>2n_i e+1`. Agrandar el cuerpo residual es una extensión no ramificada permitida y no aumenta las longitudes normalizadas. La terminación, en cambio, cuenta longitud no normalizada entera, como aclara explícitamente 1210–1213.

## 5. Obligaciones aún abiertas para pg:I/II/III completos

No se reemplazan por la frase «demasiado amplio». Los siguientes pasos concretos requieren cierre:

1. **pg:I:** verificar `pga:G123` y `pga:G45` contra los teoremas primarios en las normalizaciones impresas, incluyendo los constituyentes Speh y ausencia de monodromía al nivel elegido; después `pga:trace` y `pga:weights` para el twist normalizador. El argumento `pg:I` desde G1–G4/L fue leído y las deducciones de M4 y la fórmula de la constante Selmer fueron reconstruidas. Se comprobó que χ=ε_ℓ⁻¹ (332): confundir ambas produciría un falso error en el exponente t′ de `pg:beta`.
2. **pg:II(c):** la entrada integral (IM), 1925–1940, debe coincidir y estar probada en P54 para los valores absolutos y factores Euler escritos. La existencia Selmer (IIa,b) no demuestra por sí misma la cota de L-valores. Queda verificar `pse:stick` desde IM y la elección común de raíces para todos los sistemas.
3. **pg:III:** la hipótesis triangular (7) de `pri:ribet` debe quedar certificada mediante `pri:fitt-triangle`, los módulos odd `pod:odd`, el triángulo Kummer `pku:triangle` y su detector finito. El teorema de Ribet no elimina estas entradas por sí solo.
4. **pg:III → denominadores:** reconstruir `pri:norm` y su desarrollo `prm:normb`, y verificar la identidad exacta del operador de nivel con el emparejamiento integral, incluyendo estabilizadores. Probar un elemento de la álgebra de trazas no basta para esta aplicación automorfa.
5. **Local loss:** la obligación SCC/cup product de P56 quedó cerrada en HODGE §§5–6. Resta cotejar la suma final de defectos para todos los sumandos, sin sustituir una longitud por un exponente. El paso local `pll:ribet` y la dualidad integral ya no quedan como pendientes genéricos.


## 6. Nueva tanda: tipos de nivel, normalizaciones y dos frases falsas reparables

Lectura íntegra de `pga:G123`, `pga:depth0`, `pga:parahoric`, `pga:G45` (3677–3986), `pga:trace`, `pga:weights` (4217–4284), `pax:sign` y `pax:conv` (6594–6665). La aplicación de Moy–Prasad 6.7 a la pro-unipotente del parahórico es realmente una afirmación de isomorfismo sobre invariantes para representaciones admisibles; no debe confundirse con sólo la sobreyectividad de un mapa de Jacquet para un compacto arbitrario. La fuente primaria es [Moy–Prasad, Jacquet functors and unrefined minimal K-types, pp.115–117](https://www.e-periodica.ch/cntmng?pid=com-001%3A1996%3A71%3A%3A10). En el paso de caracteres por bloques, ψ≠1 separa los soportes inerciales; la única componente del módulo de Jacquet con todo el soporte ψ en el primer bloque es Π₁⊗Π₂. Esto justifica concluir que los factores son esféricos después del twist y que N=0. No se infiere N=0 sólo de que la inercia sea semisimple.

La elección de s en `pax:sign` da exponente entero: sustituyendo s≡(N−1−n+m)/2 mod1 en e=(m−1)/2−a−s+(N−n)/2 se obtiene e≡0 mod1. Las entradas infinitesimales de σ están en Z+(n−m)/2, y tras el twist en Z+(N−1)/2. La polarización puede cambiarse por δ(E/E⁺), que es trivial al restringirse vía norma; no cambia el Galois sobre E. En G1 la igualdad de exponentes q es exactamente −s+(N−1)/2−e=(n−m)/2+a. En `trace`, n=r+t es par y qᵗ/β=q^((t−r)/2)(μ⁰θ)⁻¹. En `weights`, el shift es (t−r)/2, no su opuesto, porque χ es la inversa de la ciclotómica. La verificación aritmética de los pesos altos/bajos y del número de negativos cierra M2, condicionada a los teoremas publicados de existencia y compatibilidad y al input de theta (L).

### 6.1 G4: norma de campos finitos no definida en general — (b) para esa justificación

Primera frase incorrecta: líneas 3946–3949, «since the norm F_{q^n}^×→F_{q^d}^× is surjective», con d=lcm(d_k). Un label squarefree de grado n puede tener factores de grados 2 y 3: n=5,d=6. No hay inclusión F_{q^6}⊂F_{q^5}, ni esa norma. En rango potencia de 3 también ocurre: n=9, grados 2 y 7, d=14. P46 3661–3673 permite estos labels; sólo exige que al menos un lugar sobre cada p tenga label primitivo, no que todos lo tengan.

**Alcance y reparación precisa:** el enunciado llama a s generador de la inercia tame. Si significa generador topológico de su cociente pro-primo-a-p, θ_d(s) es un generador de F_{q^d}^× por definición de cociente, sin recurrir a θ_n. Se eligen uniformizadores fraccionarios compatibles; para d_k|d, la potencia (q^d−1)/(q^{d_k}−1) de θ_d(s) es θ_{d_k}(s), y la parametrización de Green usa estas mismas proyecciones y la misma ω. Basta suprimir la norma inexistente y usar d, como ya hace `depth0`. Si se exigiera únicamente que θ_n(s) fuera generador, esa condición sí sería insuficiente: q=13,n=3,d=2 y la séptima potencia de un generador tame conserva θ₃ generador, pero pierde el factor 7 del orden de θ₂. Esa séptima potencia no es un generador topológico tame, por lo cual no es contraejemplo al enunciado con la condición más fuerte. No se afirma aquí que G4 sustantivo sea falso.

### 6.2 M3: orden de los roots — (b) para la línea 883, con reparación sin costo

La línea 883 afirma que en todo lugar elegido los roots rescaled tienen orden divisor de p_i^r−1. Esto sólo se deduce para factores cuyos grados dividen r; no para los labels generales de P46. Un factor primitivo de grado 2, en rango r impar, tiene orden p²−1 que no divide pʳ−1. Multiplicarlo por z∈F_p^× no elimina la componente de orden fuera de p−1. Puede acompañarse de un factor irreducible de grado r−2 y satisfacer la exclusión de raíces en F_p; en otros lugares se eligen los labels primitivos requeridos por good.

La cota M3 escrita después **sí se recupera**: un root de factor de grado d_k≤r tiene orden divisor de p_i^{d_k}−1 (el rescaling por F_p^× lo preserva). Si vℓ(ω−1)>0, su orden es potencia de ℓ y ℓ divide p_i^{d_k}−1, que divide #GL_{rt}(F_{p_i}), y por tanto N_ch. Sigue vℓ(ω−1)≤1/(ℓ−1)≤1 y vℓ(det(R(γ)−1))≤r·vℓ(N_ch), exactamente la constante impresa. El paso de Burnside/M4 usa un lugar primitivo, donde d_k=r y no tiene este defecto. Tampoco cambia el argumento M5, que usa ese mismo lugar primitivo. Son errores de prueba *as written*, reparables por argumentos elementales disponibles; no una refutación de pg:I, III ni GRH.

## 7. Cierre del módulo odd: `pod:odd` — (a), bajo las definiciones impresas

Se reconstruyó la cadena completa 4382–5258, incluidos el detector, las componentes, la congruencia de Voronoi, las sumas de Gauss, el anulador y el descenso para ℓ grande. No se usa irreducibilidad residual ni una conjetura principal. Los puntos que requieren comprobarse para que la prueba cubra realmente ℓ=2 y coeficientes ramificados son éstos:

- `pod:cft`: U_S^(M) no exige nada fuera de S, por lo cual su índice sí es finito. La fórmula local es M·#μ_M(K_v)·|M|_v⁻¹. Al imponer después unidades fuera de S e ideles principales, aparece además el factor h_K. El detector usa K=Q(μ_{Nℓ²}); la inducción en el exponente mata primero Mz y convierte la restricción a G_K en homomorfismo. Así los mismos puntos sirven para toda ν, no sólo una ν fija. El tamaño M≤y⁵ da ≤y²⁰ puntos.
- `pod:split`: la transferencia emplea b(u,g)=u[c,g]u⁻¹ y no idempotentes divididos por φ(N). La suma de caracteres vale φ(N) en el coset trivial; comparar h y chc introduce el factor 4. Por ello pasar de las componentes odd a la clase original sólo requiere multiplicar por 4φ(N), incluso en ℓ=2.
- `pod:X`: la matriz T de convolución tiene autovalores 2Σχβ para la paridad odd, y 2(−1)^e para la otra. Los primeros no se anulan por la ecuación funcional a −e (e≥1, también para caracteres imprimitivos). La adjunta demuestra divisibilidad en el anillo de valores, sin invertir el autovalor. Los dos enteros 1+N y 1+2N aseguran (S1) para cada primo. La congruencia de Voronoi procede de expandir módulo (Nm)² y dividir una identidad en un anillo sin torsión; no divide en O/ℓ^ν. La elección de w en (S2) es independiente de m, hecho necesario para la resta en `thetadiv`.
- `pod:stick` débil: la razón de Gauss G(a+b)/(G(a)G(b)) es fija por inercia, por lo que su valoración es entera. Para t≠0 tanto G(t) como p/G(t) tienen valoración positiva, de modo que la valoración está estrictamente entre 0 y 1. Esto prueba que S es inyectiva y permite parametrizar exactamente el exponente m_c(x), sin invocar una congruencia de Stickelberger más fuerte no citada.
- `pod:J`: el cociente de distribución tiene valoración cero en todos los primos sobre p por la identidad de Hermite, es unidad fuera de p y tiene todas las normas arquimedianas iguales a 1; Kronecker da raíz de unidad. La congruencia J6 resulta de reducir caracteres de orden q módulo un primo sobre q. No requiere que q sea grande.
- `pod:artin` y `annih`: los factores 2(a^e−1) matan respectivamente la contribución real y la contribución sobre ℓ. Para el anulador se toma z′=2X²z; si 4X²z≠0, Sah fuerza un Frobenius que detecta z′. La familia J y la divisibilidad `thetadiv` contradicen su no anulación. Se obtiene 4X², sin dividir por 2 ni por a^e−1. En `thetadiv`, 1−ℓ^eψ(ℓ) es unidad, y e≥1 justifica trasladar la congruencia de nivel n−1 al nivel n.
- `pod:KS`: las raíces y(x) son arbitrarias pero el cociente F_g está en μ_{ℓ^n}. Los cambios de shifts desaparecen por distribución; esto hace que Λ_S(F_g) satisfaga la regla de cociclo con exponente e+1. Para KS3, la identidad de inercia compara W₁ y W_{γ⁻¹}; ambas son raíces de unidad que se reducen a 1 en el lugar apropiado, y su cociente pertenece a μ_{ℓ^n}. Como q≠ℓ, ese cociente es exactamente 1. No se identifica erróneamente una raíz de unidad q-primaria con 1 antes de formar el cociente ℓ-primario.
- `pod:recl` admite O ramificado: V=Oκ(τ), muerto por ℓ, se toma como espacio F_ℓ-vectorial. Las coordenadas usadas para Hilbert 90 no se presuponen O-lineales. La suma final está en mV porque cada coeficiente s_i mata un elemento no nulo y por ello pertenece al maximal m. φ(Nℓ)−t es unidad y fuerza κ(τ)=0.
- `pod:koly`: si faltan m=vℓ(X)+1 detectores, cada conjunto de ≤m primos admite una clase no nula de ℓ-torsión trivial allí. La inducción descendente en i conserva tightness y produce ℓ^iκ_S no ramificada; KS3 contradice la elección de un Frobenius que detecta ℓ^{i+1}κ_S. Al final θ=0 módulo ℓ^m contradice vℓ(X)=m−1. La contradicción sigue siendo válida en O ramificado, pues ℓ^{m−1}X′∈ℓ^mO implicaría X′∈ℓO, siendo X′ unidad.

Para ℓ≤y² sólo se usan el anulador y el detector uniforme; el descenso que divide por unidades residuales se reserva a ℓ>y²>N+e+3. El producto c_odd=(Π_{0<e<t}16φ(N)X_e²)^{y²⁰}h_E tiene la longitud y el tamaño anunciados. La sustitución de datos N≤x¹⁵, r≈x⁵ da log c_odd≤x⁴⁰⁷≤x⁸⁰⁰. Esto cierra `pg:odd` y su contribución a la suma global; todavía no cierra el triángulo de clases even ni el operador norm.

## 8. Cierre del triángulo even y de `pku:main` — (a) desde dualidad finita estándar

Se leyeron y reconstruyeron 5297–5818. Las entradas externas son dualidad local, reciprocidad global y Greenberg–Wiles para módulos finitos, expresadas D1–D4; no una afirmación de existencia de clases especial al problema.

La modificación ε⁺=ε·η del carácter ciclotómico es trivial en todas las conjugaciones complejas. En ℓ=2 su imagen cae en 1+4Z₂ porque μ₄⊂E. Esto permite el generador pro-cíclico usado en los términos locales sobre ℓ. El cociente G_F/G_ν tiene Sylow de ℓ generado por ≤2 elementos, también en ℓ=2; no se afirma falsamente que sea siempre cíclico.

Las relaciones de Kummer se obtienen restringiendo clases duales a G_ν y extendiendo por cero fuera de él. No se promete que esa extensión sea un cociclo global: la definición de relación sólo pide aditividad sobre G_ν y la ley de conjugación. La reciprocidad con los test cocycles se deriva de los anuladores locales exactos en S₀; escoger T=S₀ evita términos extra sin controlar.

En `pku:torsion` se seleccionan por Chebotarev los primos que detectan todas las clases residuales duales no nulas sobre G_ν. Quedan como máximo ℓ² clases infladas desde G_F/G_ν. Greenberg–Wiles, con **H⁰ ordinario** en los reales, aporta ℓ⁻¹ en cada uno de los r_F reales y de los k primos fijados, ≤1 sobre ℓ y ℓ en cada primo relajado. Da ℓ^(#P−k−r_F+3) para M[ℓ]. El paso a H¹(M)[ℓ] añade sólo un factor ℓ: la imagen en H¹(M/M[ℓ]) viene del borde de H⁰(M/ℓM). En el núcleo, el lift a M[ℓ] conserva las condiciones porque los H_v actúan trivialmente y M[ℓ]→M es inyectivo; aquí sería incorrecto usar solamente exactitud de cohomología sin verificar las condiciones locales.

La imagen dual en (M^∨)^P es exactamente el anulador B^⊥: reciprocidad da inclusión y la razón de dos fórmulas Greenberg–Wiles da igualdad de tamaños. Al restringir a X=M[ℓ]^P, resulta #r(B^⊥)=ℓ^#P/#B[ℓ]≥ℓ^(k+r_F−4). Esa restricción depende sólo de las reducciones de los mapas de Kummer; por ello hay al menos k+r_F−4 reducciones independientes, no solamente clases abstractas duales. Como r_F≥576, una queda fuera de cualquier familia de k mapas previos.

`pku:triangle` usa esos mapas para exponentes iguales e, luego el polinomio separador Π_{k≠e}(conj_a·power(ε(a)⁻¹)−ε(a)^k). En los valores aditivos esto mata todos los exponentes diferentes sin dividir sus diferencias; el producto de diferencias divide la potencia presupuestada ℓ^((t′−1)h₀). La antisimetrización en u introduce 2, y el paso del test cocycle de E a F introduce otro 2. La pérdida exacta es 4Π(ε(a)^e−ε(a)^k), que divide ℓ^(hh₀). Para ℓ grande h₀=0 porque todos esos factores y 4 son unidades. Para ℓ pequeño el detector §7 tiene ≤h²⁰ puntos y da el costo h²²h₀. No se utiliza una cota uniforme falsa para el número de detectores cuando ℓ>h².

El test cocycle 2z⁺ sobre F se anula en los reales y sobre D_v∩ker ε⁺ en ℓ porque su valor es el de z⁺(g²), con g²∈G_E. La reciprocidad de κ_j deja sólo el término j: los anteriores se anulan por las hipótesis de z, los posteriores por las condiciones impuestas a los Frobenius al escogerlos. Así se prueba la propiedad triangular (iii) para todo O/ℓ^ν, pasando a coordenadas aditivas Z/ℓ^ν que separan puntos, sin suponer O no ramificado. Este cierre junto con §7 elimina las obligaciones even/odd de la hipótesis triangular de Ribet; resta verificar la álgebra de Fitting y el operador norm.

## 9. Álgebra de Fitting y norm deformada

**Fitting 2393–2471: (a).** La dualidad sobre O/p separa puntos del módulo de longitud finita Oⁿ/Φ⁻¹N. En `fitt-cost`, el cociente de duales por la preimagen de W es exactamente F(N)/(F(N)∩W), aun si z no genera Oⁿ. Una serie de composición del anulador da un factor π por fila añadida. La identidad a·Fitt(N+Rv)⊂Fitt(N) proviene de multilinealidad y de la anulación de términos con dos filas proporcionales a v, no de una supuesta inclusión de ideales sin factor. En el triángulo, cada paso cuesta CX_j; al final se pasa a X=0 sólo después de añadir mR^s. Se recupera d∈Fitt(T) con d(0)=fC^#s. La cota b+(#I+#s)v(C) y el coeficiente X_I son exactos.

**Inducción de la norm 7434–7505: (a), bajo `oneplace` y el Higman operator impreso.** Es importante mantener la afirmación para todos S y todos i≥#S. Para cada j∈S se usa S\{j}; sólo entonces se prueba invariancia bajo cada factor Γ_j, y por tanto Γ. La identidad Σk⁻¹Ψk=c₀ convierte esa invariancia derecha en una factorización por Nm. No se necesita que Ψ ni los operadores Y_S conmuten con la Hecke algebra; sólo los N_S y δ′ lo hacen, y ésos son los únicos cambios de orden usados.

**`pri:norm` 2977–3052: (a) desde `oneplace`.** La relación t₀−X_jr₀ se mata emparejando los coeficientes de S y S∪{j}; Nm_jt₀=0 y ∂_jt₀≡Nm_jr₀. En la consecuencia se aplica a u=Ψ(d₁l), cuyo norm es c₀d₁l. Todos los coeficientes salvo el superior se anulan por la hipótesis d_Sy=0. El error es múltiplo de ℓ^ν/(2n!), y la divisibilidad exigida por (n₀c₀²)^(#J+1) permite cancelar ese factor sin concluir integridad a partir de una congruencia racional injustificada.

**`oneplace` 2901–2975: álgebra reconstruida; pendiente exacto en el diccionario local.** La transferencia de la coordenada k₁₁ del estabilizador de una recta es det: por cada coeficiente del sumatorio Tr L(λ)Tr′ aparecen los logs de los factores de la permutación de cosets. El shift de λ produce −Nm_j. Para la tercera propiedad, B(1) tiene imagen K₁-invariante; insertar Higman da c₀B(1)=L(1)ΨB(1). La anulación δ′NmZ=0 se obtiene primero en característica cero; dividir #K₁ allí no introduce una división en el retículo. Resta cerrar la entrada `pri:dict(b,d)`, concretamente `pax:Ueig` y `pax:toproot`, y la construcción integral del Higman operator y del emparejamiento en `pax:ss-forms`/`pax:ss-pairing`. Por tanto este bloque no certifica todavía el teorema completo de denominadores.

**Base level 7527–7588:** la acción twisted ρ(u)=Πψ_w(det u_w)·right(k′_u) es independiente de los lifts, preserva J_O y cancela el factor inverse del kernel theta. En Q la matriz lower triangular transforma el bloque superior T^(1) por a⁻¹ y produce χ_O=ψ(det a)⁻¹. En los lugares elegidos el dato T≡ι₀ queda fijo por el subgrupo que fija las primeras columnas. Estas cuentas son correctas; la pertenencia a la categoría de inercias de todos los sistemas de este base level necesita además `prm:label`/`prm:inertia` y el diccionario local citado arriba.

## 10. Diccionario U y cadena esférica: cierre adicional

Se reconstruyeron `pax:Ueig`, `pri:dict(b,d)` y la demostración elemental `pay:chain` (6317–6417 y 6710–7086). **(a) en los rangos n≥3 usados aquí, bajo la compatibilidad local–global ya declarada.** Para n=2 la demostración de Ueig invoca formalmente un parahórico de bloques (1,0); se sustituye ese paso por el hecho inmediato de que una representación esférica de GL₁ no admite un carácter ramificado en O_F^×. Esto no afecta el rango n≥6 usado por la prueba de denominadores.

La recta parahórica con carácter ramificado es única: en la descomposición de Bruhat P\G/P hay dos cosets, y el segundo requeriría un carácter ramificado en el soporte cuspidal del factor esférico. Las q^(n−1) clases de I₁dI₁ y el factor δ_P(d)^(1/2)=q^((1−n)/2) dan U=q^((n−1)/2)Π₁(π). La proyección e sobre la única recta ramificada conmuta con Frobenius, y la ciclicidad de la traza justifica tr((γ−1)g p(φ))=p(μ)tr((γ−1)g) aunque g no preserve esa recta.

Para la cadena esférica, el conteo de hiperplanos da q^j preimágenes si e₁ no pertenece al subespacio y cero si pertenece. La dualidad L↦L* produce la segunda recurrencia con q^(n−i−1), y U′ es realmente el adjunto después de insertar el promedio M sobre I₁. Se comprobó la identidad

`c (z_c,x)(q^(n+1)−1)=P(qc)(x,x)`, con z_c=((P−P(c))/(X−c))(U)x.

Si P(c)=P(qc)=0, U′z_c=q^(n−1)c⁻¹z_c y (z_c,x)=0; por adjunción z_c es ortogonal a todos los A(U)x y, en particular, a sí mismo. Esto prueba la cancelación de cada raíz consecutiva sin suponer U normal. La inducción cancela el segmento completo, y la estabilidad de span{x₀,…,x_n} por U′ permite pasar de R(U)x=0 a la identidad adjunta bar R(U′)x=0. Ésta es exactamente la identidad necesaria para la ortogonalidad de `toproot`, no sólo una divisibilidad escalar de polinomios. La simetría P(y)=0 ⇐ P(y′)=0 con y·bar y′=q^(N−1) procede del adjunto T_i* y el carácter central; junto a la cota estricta de `chain(i)` completa todos los roots intermedios. Así se cierra el input local pendiente en §9, sin usar Tadić como sustituto de la prueba.

## 11. Cierre de Higman y pairing; fallo de alcance en base level

**Higman y pairing (6045–6268): (a) con el retículo y norma de P49/P53.** J₀ es libre por la lemma de nivel principal de P46; Γ actúa libremente en cada fibra de los dobles cosets. Multiplicar por un indicador de representantes de Γ′ y sumar sus conjugados produce 1 en el nivel libre. Promediar por H=J_O/J₀, sin dividir por #H, produce Ψ en el nivel base con suma de conjugados c₀=#H. Las traslaciones son integrales en los gauges y c₀|N_ch por inclusión en GL_{rt}. Los estabilizadores se inyectan en H. La cuenta puntual del pairing usa la matriz Gram entera y la identidad polinómica tρ(g)Gρ(tg⁻¹)=G; cancelados los gauges, cada término es integral, y multiplicar por N_ch elimina todos los estabilizadores. El agente responsable de P53 cotejó 9770–9804: el retículo y la norma son precisamente la restricción tensorial estándar, sin un cambio adicional de escala. Esto cierra el pendiente Higman/pairing de §9.

### 11.1 Polinomio fijo para todos los elementos de inercia — (b), primera línea 2271

`pri:BL(c)` afirma `o_w(ρ_x(s))(ρ_x(s)−1)=0` **para s∈I_w**, siendo o_w el polinomio fijo de las imágenes de los roots del label. Se repite al final de Step 5, 6556–6560. Sólo está probado para un generador tame normalizado γ; en γᵃ las raíces son las potencias ξᵃ. Por ejemplo, para un root ζ de orden mayor que 3 y label lineal X−ζ, s=γ² da (ζ²−ζ)(ζ²−1)≠0. Semisimplicidad no convierte esos roots en un conjunto estable bajo todas las potencias.

La aplicación de `pri:columns` 2855–2865 sólo necesita el polinomio en un generador δ_v, por lo que este defecto puntual puede corregirse allí sin costo. Para todos s hay que usar o_{w,s} con roots evaluados en s. **P56 7962–7985 ya formula correctamente esta dependencia** mediante M_s y q_s; no se le atribuye el mismo error. Pero la otra cuestión de alcance siguiente no se arregla sólo cambiando s.

### 11.2 Alcance de «base level» y preservación del tipo e_c — discrepancia de formulación; reparación explícita

Cadena textual comprobada:

1. `prm:def-level` 7527–7543 define F(O) por J_O y χ_O, **sin** condición e_cy=y. En un lugar elegido J_O fija las primeras r′ columnas y deja el bloque GL_{t′} libre. Sobre F(O) actúa el grupo G_c a través de ρ, con todos los tipos permitidos.
2. `prm:label` 7606 exige explícitamente **e_cy=y≠0**. Es esa hipótesis la que permite afirmar que el primer bloque tiene tipo σ_c rescaled. Su prueba es correcta bajo esa hipótesis.
3. `pri:BL(c)` 2265–2273 cuantifica, en cambio, sobre **every system … occurring in base level with principal level at U**, sin limitar a e_cF(O). La frase (a), e_cF(O) consists of forms of base level, no impone esa restricción a F(O).
4. La prueba 6467–6471 comienza `By Lemma prm:label(b), Π_w^{K(1)} contains ... σ_{tilde f_k}`. Si se lee F(O) como en el enunciado, ésta es la primera aplicación que requiere la hipótesis adicional e_c. Sin embargo, la introducción de la subsección pax:ss-BL (6430–6437) declara expresamente que allí «base level» significa además fixed by e_c; bajo esa aclaración el uso sí satisface la hipótesis. Se registra la discrepancia entre formulaciones, no un fallo definitivo de esta aplicación.
5. En `pri:III` 3094–3098 se reemplaza efectivamente Y por el conjunto de **todos** los sistemas de eigenvalores que ocurren en base level con nivel principal en los w_j, y se aplica BL(c) a ese Y. `pri:columns` necesita entonces un polinomio o_w común, de los roots de c, que mate la inercia de cada u_x. Esa uniformidad no se deduce de las hipótesis escritas.

No se ha construido aquí un sistema automorfo global que contradiga la conclusión de pg:III, y no se afirma que sea falsa. La aclaración de 6430 permite una lectura consistente restringida; queda verificar la preservación de esa restricción en los operadores de la prueba de denominadores. La reparación natural sería restringir todos los espacios de operadores y Y al tipo e_c; debe verificarse que los operadores integrales de Higman y la norm deformada se preservan en ese retículo con la misma constante. Ψ no es un operador Hecke y su construcción mediante representantes de cosets no declara conmutación con G_c. Proyectarlo por e_c puede introducir denominadores y no se ha mostrado que estén ya cubiertos por N_ch. Alternativamente habría que construir polinomios de inercia comunes para todos los tipos presentes, y justificar los grados usados en P56; no basta declarar que existen porque los tipos son finitos.

Por tanto los cierres locales/algebraicos de §§7–10 no deben resumirse como certificación incondicional de pg:III. El pendiente global es ahora una obligación concreta en una unión, no amplitud de lectura.


**Reparación reconstruida de la preservación e_c, con la misma cota N_ch.** En el nivel libre J₁ de 6045–6070 actúa D=Π_{w chosen}GL_n(F_w), además de Γ de los lugares auxiliares; las acciones conmutan porque sus soportes son disjuntos. D preserva el carácter de nivel en Q, también disjunto, y los gauges integrales. Partiendo del mismo indicador Ψ₁ con Σ_{k∈Γ′}k⁻¹Ψ₁k=1, definir

`Ψ_D=Σ_{d∈D} d⁻¹ Ψ₁ d`.

Entonces Ψ_D es integral, conmuta con D y satisface Σ_{k∈Γ′}k⁻¹Ψ_Dk=#D. Al conmutar con D preserva el subespacio H-invariante del nivel J_O y las componentes de σ_c para la acción twisted del bloque GL_{r′}; por tanto preserva e_cF(O) y su intersección con el retículo integral, sin aplicar un proyector e_c a los valores. Se puede tomar c₀=#D en lugar de #H: por n≤rt, #D divide N_ch, y todas las estimaciones de `pri:norm` y `pri:III` sólo usan c₀|N_ch. Los operadores de Hecke y las traslaciones en lugares auxiliares también preservan e_c. Con esta sustitución explícita y leyendo Y en e_cF(O) como indica 6430, la obligación de preservación se resuelve sin cambiar β_ℓ. Esta reparación no es el operador escrito en el paper; se distingue de certificar literalmente su construcción original. Es una ambigüedad/omisión subsanable, no evidencia de que la estrategia de denominadores fracase.

## 12. Cotejo de G123/G45 con fuentes primarias

Se cotejaron las formulaciones primarias, no sólo la bibliografía del paper:

- [Labesse, *Changement de base CM et séries discrètes*, Corollaire 5.3, pp.42–44](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf): da los constituyentes discretos conjugado-autoduales y la compatibilidad en lugares split y no ramificados. La condición (*) se cumple para U∞ compacto; el grado real ≥2 figura explícitamente. Son las hipótesis usadas aquí. El paso a Speh y el twist algebraico fue reconstruido en §6.
- [BLGGT, *Potential automorphy and change of weight*, Thm.2.1.1, pp.33–34](https://virtualmath1.stanford.edu/~rltaylor/pa3.pdf): contiene existencia semisimple, los pesos y la compatibilidad incluyendo N fuera de ℓ. En ℓ, ese enunciado sólo da identidad bajo Iwahori y cristalinidad si es esférico. P55 reconoce la restricción y no usa indebidamente esta parte para el nivel tame ramificado.
- [BLGGT, *Local-global compatibility for l=p, II*, Thm.1.1 y §1](https://www.ma.imperial.ac.uk/~tsg/Index_files/localglobalII.pdf): la relación ≺ está afirmada sin Shin-regularidad; ésta sólo se exige para la igualdad general. La definición de ≺ compara sumas parciales de tamaños de bloques. Si el parámetro automorfo tiene N=0, todos esos tamaños son 1, y ≺ obliga también a N=0 en el lado Galois. Éste es exactamente el uso de P55, por lo cual la posible falta de Shin-regularidad no abre un hueco en G4.

**Resultado:** no se detectó una hipótesis externa de irreducibilidad residual, ℓ grande o Fontaine–Laffaille ausente en G123/G45. Las condiciones de automorphy lifting de otras secciones de BLGGT no son condiciones de su Thm.2.1.1. Se mantiene la distinción con las frases incorrectas de generadores y roots señaladas en §§6,11.

## 13. IM54 → twisting55, reconstrucción de la unión

Lectura y reconstrucción de P54 1798–2085 y P55 1925–2088. **(a) para las deducciones desde los inputs de kernel de P49, Rallis y exchange53; identidad de enunciados confirmada en el rango aplicado.** La auditoría independiente de Rallis/exchange corresponde a los agentes P53/P54; aquí se comprueba que IM no añade una hipótesis no justificada en la especialización.

Para z≥2, la expansión de `pex:points` usa un conjunto finito de ideles x_{c,a} dependiente de Q, no de θ. La suma de puntos absorbe el twist por θ(x)⁻¹; el norm cuadrático da θ(x_p x_p′⁻¹) multiplicando un coeficiente independiente de θ. Los estabilizadores dividen N_z; n_p² elimina las denominaciones del kernel y (NmQ)^(1−2z) es unidad en los ℓ que se usan. La integridad requiere las dos inmersiones j y j∘c, exactamente como el pairing de §11. El constante n_p puede depender de p=(ν,z) y no requiere una cota explícita: v₀=vℓ(F(1)) se cancela después.

El caso ℓ=d no se omite: `pex:dint` escala la variable por d. El límite v(x(P))≥−2/(d−1) para d-torsión en el grupo formal da v(g″(0))>−2. Los derivados de orden ≥3 proceden de x y son integrales. Por ello los jets de grado k se vuelven integrales multiplicando por d^k, con k fijo por el peso; el nuevo n_p sigue independiente de Q y θ. Esta cuenta depende de la curva/modelo integral de P49, no de una suposición tácita d∤ℓ.

Para z=1, `pex:E1` aplica exchange53 con N=a=2,b=0,e=1 y μ=c≥1. Los datos matched son exactamente χ_θ∘det, porque el carácter del exchange es el inverso. El proyector compacto sobre invariantes transforma x en κP_c: el espacio de polinomios de ese tipo es una recta por densidad de U(2) y evaluación en matrices invertibles. κ≠0 porque el lado constante del exchange es no nulo. Los tipos arquimedianos no cambian con θ, de modo que κ y C₁ son independientes del twist. Así F(θ)/F(1)=NmQ·ρ_p(θ)².

En `pex:IM1(b)`, expandir el dato en δ_y y trasladarlo a δ₁ cancela χ_θ(det y) con λ_θ(det ŷ)⁻¹. El twist restante es θ(det(hŷ)); al multiplicar por el conjugado se obtiene otra suma finita de caracteres con coeficientes integrales. Para aumentar el módulo por un primo no ramificado, evaluar el Hecke polynomial del vacío en α⁻¹ selecciona las matrices de rango 2. Integrar las traslaciones aporta (1−α⁻¹)(1−qα⁻¹), con α⁻¹=q⁻¹a. Su norm cuadrático da exactamente los factores para e=0,1. No se reemplaza el valor absoluto de un L-valor por una expresión algebraica sin demostrarlo: se obtiene desde el período y la identidad exchange.

En P55, el polinomio P_Y se evalúa sólo en raíces ℓ^N de unidad. La diferencia entre la restricción a la recta y el producto de polinomios Euler es divisible por (1+X)^(ℓ^N)−1, monico, sobre los enteros algebraicos ℓ-ádicos. La valoración del error en v(y)=ρ es ≥Nρ y excede β_Y+s₀ρ. Los factores Euler lineales tienen coeficiente principal unidad y costo ≤ρ cada uno. La elección común de raíces evita los ceros residuales para los finitísimos sistemas y todos los exponentes j≤m. Finalmente v(Fθ)=v₀+(m_IM+1)v(rθ), con NmQ unidad; tomar la parte positiva da la desigualdad usada en II(c). Los factores omitidos son los de M en numerador y denominador, y Q sólo en el numerador; para un twist genuinamente ramificado en cada Q esos últimos ya son triviales. Los módulos ampliados con θ no ramificado allí se usan únicamente en la relación de distribución, donde sí aparecen los factores explícitos.

## 14. Cierre de la suma local y de la suma sobre primos

**(a), como ensamblaje bajo los inputs y reparaciones identificados.** En 3513–3523 los casos (b),(c) usan floor(log_ℓ h³)+1≤m y x_c≤t; en (d), floor(u)≤u da 10⁵(ρ floor(2λ/(kt))m+floor(ρm/(kx))λ)≤3·10⁵ρmλ/(kx). No se multiplica de nuevo la longitud del caso (d) por el rango. La suma 3535–3540 usa Σ_v[E_v:Q_ℓ]=2f y Σ_c rk(L_c)/x_c=r′+t′/t≤2r′; de ahí exactamente r′loc_ℓ. Para ℓ>2b, ℓ∤M, λ_ℓ=0 y el defecto es cero.

En `pg:sums` 493–534, Σv_ℓ(n)logℓ=log n controla tanto N_ch como h₁ y C_odd. La cantidad λ incluye el factorial y una ventana de longitud 60h³, con multiplicidad h³: su suma es ≤3b log b. La parte de M es ≤22b log b, dando 10⁸f(m/k)b log b. La cota de C_odd queda ahora sustentada por §7, y no como premisa no revisada del primer informe. Los restantes términos ≤x¹⁰⁰⁰ se absorben usando b≥x^(10¹²). Finalmente m²≤4x y (log b)²≥8·10⁸ dan el presupuesto fa(log b)³/(mk), con a=xb. El factor logℓ en la unión con P46 está presente; no se suman valoraciones normalizadas como si fueran logaritmos.
