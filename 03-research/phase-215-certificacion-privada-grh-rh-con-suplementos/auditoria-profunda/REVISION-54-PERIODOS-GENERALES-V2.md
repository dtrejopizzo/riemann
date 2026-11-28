# P54: períodos generales y revisión cruzada de la fase49

Fecha: 2026-11-28. Lectura directa de P54 `main.tex` 3944–4638, `plf:harm` 3685–3699, `plf:L4` 3701 y siguientes, definición del polinomio 498–508; cotejo de la fórmula de Gram 1134–1235. Este suplemento descarga la parte general de períodos que THETA/TL04 sólo había reconstruido en rango uno. No confundir este cierre con el de las tres identidades exchange54 ni con `po:span`, que son obligaciones separadas.

## 1. Revisión cruzada de REVISION-FASE49-V2

No se encontró circularidad ni pérdida aritmética en la prueba suplementaria de las DOS consecuencias necesarias de δ_g, bajo la normalización explícita P3/D2 y la propiedad de la línea vacía. El cotejo de dichas propiedades con las fuentes primarias corresponde a la revisión concurrente de spanning.

El punto crucial es conservar un modelo aritmético común: los coeficientes de los indicadores, fases, transformaciones de Fourier, cambios de polarización y sus inversas están en el campo A indicado; las medidas de soportes son racionales. Que σ conmute con conjugación en A se prueba primero mediante los módulos de todos los conjugados de υ(a), no se deduce de unitariedad abstracta. La conjugación de las identidades finitas de Gram es entonces legítima.

La recuperación de A_g de A_g⊗1 no requiere escoger una fase trascendente: en polarizaciones simplécticas compatibles, el tensor de indicadores normalizados proporciona coeficientes algebraicos explícitos. En característica residual p distinta de ℓ, los denominadores de los cambios de modelo, normalizaciones de vacíos y Fourier son potencias de p. Tanto operador como inverso conservan la estructura integral. Sobre ℓ, la acción sobre la línea vacía del estabilizador compacto es un carácter suave de imagen finita. La primitividad del vacío, transportada por un automorfismo integral, obliga a que el coeficiente común de la expansión sea unidad, no simplemente integral.

Precisión de redacción: escoger representantes con componente ℓ igual a cero es una afirmación sobre representantes adélicos. Si después se requieren representantes racionales, aproximación simultánea permite elegirlos **integrales** sobre ℓ, que es exactamente lo necesario para S1; no se debe exigir que un racional no nulo tenga componente ℓ cero. Esto no altera la conclusión usada.

No se certifica con esta argumentación la fórmula más fuerte que clasifica δ_g como UN valor específico de υ por una raíz de unidad. La fase fuerte sigue fuera del contenido demostrado; sus dos consecuencias suficientes sí están reconstruidas.

## 2. La diferencia entre rango uno y general

La fórmula de Gram general usa `po:glue`, en particular (G3) que remite a `po:periods=ppe:main`, y (G2) que remite a `po:span`. La fórmula compacta `pex:rallis` de rango uno no prueba ninguna de estas dos entradas por sí sola.

En la instancia general, `rank W=r`, `rank V=n=r+t=6r`, `V` es definido positivo y `N″=r+9m+1`. La torre se necesita hasta `p=N″`. Su hipótesis se cumple porque `2r+2N″+3=4r+18m+5<6r`; se usan `r≥x^5`, `m≤2√x` y el rango enorme de los datos admisibles. No se sustituye aquí la comprobación de rango uno `45<2z`.

## 3. Generación polinomial: reparación explícita de una frase demasiado fuerte

En `ppe:harm`, 4202–4223, los pasos (a) y (b) son correctos: Schur ortogonalidad y F1 dan `L(p_ξ)=0` para todo ξ, y la diferenciación por la fuente da `L(ω(X)v)=R_XL(v)`. La integral es sobre el cociente compacto del grupo objetivo; las derivadas de los datos Schwartz permiten la diferenciación. El promedio compacto elimina los tipos distintos del que aparece en los coeficientes de Ξ.

La frase de (d) que identifica todo el espacio de armónicos de ese tipo con `{p_ξ}` necesita, en general, añadir la generación por el compacto de U(W): el tipo mínimo de la fuente no tiene por qué ser unidimensional. La conclusión que se utiliza admite esta prueba más directa, sin una estimación ni una constante nueva:

1. U(V) es compacto; su centralizador en el grupo simpléctico del espacio real subyacente a Hom(W,V) es U(W).
2. El componente polinomial de un tipo irreducible de U(V) es irreducible para la acción conjunta de U(V) y la complexificación de la álgebra de Lie de U(W).
3. El subespacio `U(g_W,C)·{p_ξ}` es estable por ambas acciones, porque las acciones conmutan y ξ↦p_ξ es equivariante. Contiene un vector no nulo: el producto explícito de menores de `plf:harm`.
4. Por irreducibilidad, es todo el componente polinomial. Los pasos (a),(b) anulan L en él; el promedio compacto anula el resto.

El punto 2 se cotejó directamente en el facsímil de [Howe, *Transcending Classical Invariant Theory*, p.542, (3.9)(a)](https://www.math.utah.edu/~ptrapa/math-library/howe/howe-transcending-1989.pdf). En la misma página, Proposition3.1/(3.10)(b) da la generación por armónicos citada en el paper. Esta aplicación usa el par con un miembro compacto; no supone irreducibilidad de componentes de un par arbitrario no compacto, ni requiere Short Forms o inyectividad de un lift global.

Dictamen: **(a) para la conclusión `ppe:harm` reconstruida mediante esta precisión; la frase literal sobre todo el espacio de armónicos no se certifica tal como está escrita.**

## 4. Bottom: todas las matrices, no sólo columnas

`ppe:row` es válido en rango general. Si el bloque superior es singular se toma una fila de su núcleo izquierdo. Si es invertible pero el cociente inferior no cumple la integridad/congruencia requerida, una fila `(y_a,−e_a)` y un coeficiente de tamaño máximo producen exactamente la fila anuladora, incluida la congruencia estricta en Q.

En el caso A de `ppe:bottom`, el soporte del dato normalizado es una sola órbita de K_ϑ, mediante la matriz de bloques `(y′,0;y″,1)`. El promedio con carácter del indicador de un coset se convierte en un múltiplo de ese dato. Persiste la errata ya identificada en TL04: con la acción `Ψ(T)↦Ψ(TA)`, el operador es `ω(A,1)`, no `ω(A^{-1},1)`. Se sustituye también el argumento de la función trasladada; ésta es cero para todo argumento, por lo que la anulación y todas las constantes permanecen iguales.

En el caso B, los elementos `k_s=1+ι₀vl` fijan el centro del coset y su retículo. En M, `R_{k_s}Ξ=ψ(det s)^{-1}ϱ(s)Ξ`; la conjugado-linealidad de Ξ↦L_Ξ se mantiene al sumar, de modo que se obtiene exactamente `L_{ϱ(η_{ψ,λ})Ξ}=0`. No hay que sustituir η por su conjugado: el coeficiente ya está dentro de su argumento. La mención literal a «linearity» debe leerse como aditividad para esta suma de vectores ponderados. En Q, la sobreyectividad del determinante del grupo de hiperplano y ψ≠1 anulan la suma.

La verificación de F2 para los labels generales es `ppe:green`: la restricción Harish–Chandra del label squarefree a GL1×GL(r−1) sólo aporta sus raíces lineales. Emparejar con ψ da cero cuando su nombre no es raíz. Esta aplicación concreta se coordina con el cotejo primario de Green/Zelevinsky de la rama spanning; no se deduce del caso de rango uno.

## 5. Torre y período

`ppe:transfer` se aplica a `(X,V)` con `m_X=r+2p≤n`, en un lugar split fuera del nivel. Mover las traslaciones por la integral invierte el double coset; cambiar al lugar conjugado vuelve a dar el polinomio de Hecke requerido. Sus factores tienen módulos `q^{m_X/2}` y `q^{n/2}`. Así, para p≥1, los factores externos no se anulan porque sus módulos son a lo sumo `q^{-p}<1`; la nueva raíz satisface

`q^{m_X+1}|X′|=q^{(2r+2p+4−n)/2}≤1`.

El lema de raíces pequeñas domina la suma de todos los subespacios por `exp(1/q)<2`, válido también para q=2; sólo necesita que el descenso sea acotado. `ppe:bdd` usa R2/R3 y `pcx:mean` con l=A para cancelar `ht(g)^A·δ^A`, donde δ≪ht(g)^{-1}; esta prueba fue reconstruida en AUXCORE y releída aquí en 4383–4411. No requiere rango uno. El zero term usa el carácter desplazado por υ₁ y una evaluación Schwartz en el modelo mixto, no una evaluación acotada en Hilbert.

`ppe:rallis` en rango general: el coeficiente de Fourier de Gram identidad selecciona frames isométricos; Witt da una órbita racional con estabilizador U(V₂). Fuera del nivel los frames integrales son una órbita del compacto porque su complemento es unimodular y la extensión es no ramificada. La norma de unidades y la traza residual justifican la diagonalización incluso en característica residual dos. En los lugares del nivel los indicadores compactos separan puntos; en infinito las restricciones de polinomios por Gaussian son densas en la variedad compacta de frames. La función continua del período queda cero en la identidad, no meramente casi en todas partes.

Para el último paso de `ppe:main`, trasladar por g_s conserva los datos fuera de Σ. Se multiplica Y₁ por un kernel de W y se usa la suma ortogonal de fuentes para obtener descenso cero desde H^{N″}. El factor del kernel sobre V″ puede escogerse no nulo para cada g,h fijados: los datos finitos fijan un conjunto discreto de puntos racionales y una Gaussian concentrada en un punto donde el dato finito no es cero domina la cola. Dividir por ese valor no fija una constante uniforme ni requiere una hipótesis de no anulación de L. La factorización sobre V″⊥V° usa caracteres fuente cuyo producto es el original y el mismo carácter objetivo en ambos bloques, compatible con la revisión V2 de P53.

Resultado: `ppe:main` general está reconstruido con las precisiones locales indicadas, sujeto al cotejo primario de la entrada F2 individualizada. No hay un nuevo obstáculo analítico de rango superior detectado en esta ruta.

## 6. Lo que queda separado para Gram

La identidad algebraica 1150–1164 usa el determinante de la **compresión** de U_ϑ a Z_ϑ. Con G1, `Θ_ϑ*U_ϑΘ_ϑ=n_Aut H_°² |c′_ϑ|^{-2} Θ°*Θ°`; con `|c′_ϑ|²H_j(ϑ)=C_x`, se obtiene el producto de valores L con potencia d_j exactamente como está escrito. G2 garantiza positividad de C_j; no se presupone invariancia de Z_ϑ por U_ϑ. La integridad usa la resolución de identidad por el frame integral y el factor n_Aut; la cota conjugada usa cσc, no supone que σ conmute con conjugación en todas las coordenadas de las formas.

Esta contabilidad está reconstruida, pero sus entradas **po:exchange (tres exchanges, secciones pte/ptf/pfq) y po:span (psp/psq/psr/psv)** requieren sus propios cierres. La prueba compacta rank1 de SW01 no los reemplaza. El mapa de cierre debe mostrar estas obligaciones hasta que sean auditadas por las ramas asignadas.

## 7. Cierre de F2 mediante Mackey finito

La revisión primaria de Green de la rama Selmer cotejó p.403 (producto igual a inducción parabólica), pp.436–437 y p.439, Theorems12–13. Para el label squarefree c, cada factor irreducible aporta un cuspidal distinto con partición (1); su producto es el irreducible Ξ_c. No hace falta añadir como caja negra una fórmula completa de comultiplicación.

Aplique Mackey a la inducción desde esos bloques y restrinja por invariantes del radical del parabolico de tipo (1,r−1). Las celdas dobles se parametrizan por matrices de intersección de banderas. Su primera fila suma uno, por lo que asigna exactamente una dimensión a uno de los bloques cuspidales. Si ese bloque tiene grado d>1, su contribución contiene el Jacquet propio de tipo (1,d−1), que es cero por cuspidalidad. Si tiene grado uno, sobrevive una única celda, con carácter θ_α en GL1 y producto de los demás bloques en GL(r−1); no hay factor de índice porque se usa el promedio normalizado para invariantes. Resulta precisamente la suma de `ppe:green`, con multiplicidad uno. Para r=1 el segundo factor es el grupo trivial y la misma cuenta es inmediata.

Por tanto, tras este cotejo y la deducción Mackey explícita, **F2 y `ppe:main` general quedan (a) reconstruidos con las precisiones de §§3–4**. El pendiente que §5 conservaba sobre esa entrada queda descargado; las obligaciones distintas de §6 siguen separadas.
