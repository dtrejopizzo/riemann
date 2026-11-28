# Paper 54: generación general, revisión V2

Texto: `04-papers/54-covolume-theorem-one-theta-lift-hecke-l-values/main.tex`, versión de trabajo del 28-11-2026. No se modificó el manuscrito. Esta revisión cubre **po:span/psp:main/psv:main en rango general**, no sólo el caso de rango uno `psu:arch`, y no sustituye su prueba por `auxcore` de53. Se leyeron íntegramente 4673–7108, además de la prueba de no anulación del carrier2544–2687 y sus propiedades2528–2542. `ppe:main` general se revisa en un informe separado por el agente theta.

## Dictamen actualizado: fallo de carácter en la versión impresa

**(b) La prueba literal de po:span no queda demostrada.** Durante el cruce final con el agente theta y root se identificó que la definición `νflat=ν'' υ^m/χ'` de2695 (repetida7584) contiene un factor υ^m que las aplicaciones posteriores omiten. La primera igualdad incompatible de la tercera exchange es2732; dentro de la prueba aquí auditada, la primera línea fallida es **6448**, que atribuye a νflat υ^m peso a=m−μ1. La definición impresa da a=2m−μ1.

Esto tiene una consecuencia comprobable más fuerte que una discrepancia de nombres. Cambiar el carácter fuente de a=m−μ1 a a=2m−μ1 multiplica la acción de U(S) por det(h)^(−m). Por tanto la identidad H5 impresa debe llevar ese factor extra. En la integral que define F⁰(1), el integrando pretendido tenía peso central cero (u3=(0;3m)+u1+u2); el integrando real lleva det(h)^(−m). Bajo el centro compacto de U(2m,m), h↦zh, aparece z^(−3m²), no trivial porque m>0. La integral es absolutamente convergente y Haar invariante, de modo que **F⁰(1)=0**, contradiciendo la afirmación F⁰(1)≠0 de la prueba. Esto no demuestra falso po:span; identifica por qué su prueba literal falla.

**Reparación suficiente para esta rama:** definir νflat=ν''/χ', sin υ^m. Entonces α=νflat υ^m vuelve a tener peso m−μ1 y H5, la reproducción y la desigualdad final de abajo quedan restauradas sin cambiar ninguna cota. `psv:char` no cambia: α° se calcula directamente como b/ν'', no mediante νflat. La comprobación de las restantes aplicaciones pte/ptf/pfq y del valor L corresponde al informe del agente theta, y no se presupone aquí.

El resto de este informe constituye **(a) para la deducción reparada, condicionada a los inputs comunes identificados en §6** y las precisiones funcionales de §7. El cotejo de la normalización del splitting49 sigue registrado en `REVISION-FASE49-V2.md`; no se lo convierte en resultado probado por citarlo. Antes del cruce final se había verificado H5 bajo el peso afirmado en6448: esta actualización corrige expresamente esa frontera y tiene precedencia sobre cualquier lectura incondicional de los párrafos siguientes.

## 1. Aproximación y tamaños, psp4673–5276

Se reconstruyó la cadena `avg → decay → pack → hommin → prodtheta → sparse → sparse2 → isol → approx → main`.

* La identificación Fock usada en `avg` da un operador de entrelazamiento escalar. Su coeficiente en el vacío es una integral gaussiana positiva; la cota inferior de ese escalar permite dividir. No se perdió un factor de volumen: se utiliza vacío unitario y medida gaussiana de masa1.
* `decay` aplica Cauchy–Schwarz después de dilatar el polinomio homogéneo de grado d; la masa del mayorante es ≤exp(n)||v||². La desigualdad |y|²≤2||σ||²(|x|²+|σx+y|²) entrega la potencia2n de decaimiento. El caso n=0 es separado.
* En `hommin`, el dual euclídeo es 2ε·different⁻¹Λ; la cota de la última mínima de Banaszczyk produce una base racional corta. Un homomorfismo no nulo tiene imagen no nula de algún vector de esa base. Esto da la separación utilizada para la suma de retículo, con el denominador fnN_d escrito en el texto.
* El promedio finito módulo π_M² elimina exactamente los términos no divisibles por π_M². Como |τ(π_M²)|=M, la separación obtenida crece con M, no con sqrt(M). En la aplicación M≥b²⁰ y producto de mínimas≥b⁻¹³ dan la separación requerida; d≤b^(3/2), q=2n_*.
* `prodtheta` no introduce una constante positiva desconocida: el producto theta·conjugado(theta) cancela la fase global. `psq:thetanorm`5476–5512 lo demuestra por Parseval y normalización del vacío.
* En `isol`, no se necesita seleccionar una familia medible de aproximantes: se fija un aproximante y se integra la función continua obtenida por rotación. La proyección por rotación y H3 producen la cota (4b^{n_*}+1)δ.

En `approx`5188–5233, las mínimas dan (5b^{3/2})⁻¹/²(5b²⁴)⁻¹/²≥b⁻¹³. El error disperso b⁻²⁰ⁿ multiplica la integral acotada por bⁿ I_{u3}; resulta exactamente

    |F(gh)−F⁰(h)| ≤ 2b^(−19n_*) |F⁰(1)| |h|^(6n_*).

H5 y H3 dan F⁰(1)=I_{u3} φ°(g1)||v||²≠0. En5235–5252, B=b^{n_*}>10 y (4B+1)·2<B²≤B¹⁹ contradicen la cota final. La desigualdad numérica necesaria es holgada y se mantiene uniformemente en el rango declarado.

## 2. P y H1–H3, psq5277–5722

La prueba de P usa una transvección asociada a un vector corto que es isotrópico por integridad y producto de normas. La descomposición triangular está determinada por los menores principales p_k=1−2 Re(t)Σ_{i≤k}s_i|v_i|². El factor de peso se acota por exp(2Aη)(1+η Im z)⁻¹/². La periodicidad viene del nivel p puramente imaginario; Schwarz en el disco/cilindro contradice el carácter de pico, pues exp(2−2π)<1/2. Los niveles de las dos aplicaciones son ±sqrt(−d) y ±M sqrt(−d); π_M divide M y por eso la invariancia disponible implica la necesaria.

Para H1–H3 se comprobó: GB es abierto, G∩B=T; la función de menores φ_u está definida porque el menor del bloque positivo no se anula; la rotación diagonal tiene pesos estrictamente positivos en las coordenadas triangulares pertinentes, y por tanto mata todos los monomios de Taylor no constantes. El coeficiente de la serie discreta es φ_u por el vector de K-tipo mínimo y el argumento del cono de K-tipos. La reproducción H3 es Fubini más el promedio por el toro; no requiere una nueva constante formal de grado.

`psq:degree`5527–5563 da d_P≤7fmb≤b^(3/2), usando f≤x¹²,m≤2sqrt(x),b≥x²⁶. `psq:unitvac`5568–5593 explica correctamente que el escalar global c del vacío se absorbe por κ|c|²=1, no que cada realización arbitraria venga normalizada automáticamente.

## 3. R en todo M'>2n, psr5741–6227

Se verificó la prueba de vecinos de retículos: un x∈L'\L con πx∈L da L₁=L_x+Ox autodual, vecino de L, y reduce d(L,L') por al menos1. Para cada hiperplano H hay a lo sumo q₀ líneas isotrópicas diferentes de L/H en el plano hermitiano H♯/H. Así N=q₀(qⁿ−1)/(q−1) y #bola(k)≤(N+1)^k.

Las sumas locales están acotadas por ε_v≤3.6q_w⁻³/²≤.28 en split y ε_v≤1.8q_w⁻¹≤.2 en inert. En el segundo caso q_w=q_v²≥9; las series sobre primos convergen. Una cantidad finita de factores R_v cercanos a1 y una cola cuya suma de ε_v≤1/3 muestran inyectividad de R. **No se exige que la suma global de todos los ε_v sea <1**, lo cual sería una inferencia inválida en grado variable; el texto evita esa inferencia.

`psr:SW/Egrowth`5990–6062 extiende la aplicación Siegel–Weil al target definido positivo y M'>2n. El argumento adicional para la suma de valores absolutos es necesario y está presente: f_Φ≤cf₀ en P(A)\G(A), traslación controlada por normas exteriores, reducción a representantes de normas acotadas por una potencia de la altura. No se intenta deducir el crecimiento de la suma absoluta del crecimiento de la suma con signos.

`psr:rallis`6064–6133 sigue doubling/unfolding con integrabilidad absoluta. El punto de soporte inyectivo es indispensable y se obtiene de sharpness en una plaza del módulo no vacío. R sólo necesita A≠0: no usa el valor absoluto exacto de A. En `vanish`, ortogonalidad a funciones rápidamente decrecientes, Fubini y la serie absolutamente convergente dan ||R(κ*ψ)||²=0; continuidad e inyectividad de R dan κ*ψ=0.

`psr:R`6146–6227 es álgebra lineal finita: la intersección de núcleos de L_{p,i} está contenida en kerℓ. Las clases finitas y la estabilidad de Q bajo el grupo compacto real anulan el lift completo, no sólo sus valores en representantes. δ_ι es sharp, A₀=tι y A₀ι=1. No hay una exigencia de uniformidad en los coeficientes a_{p,i}(g): la prueba posterior sólo requiere su existencia e independencia de ψ.

## 4. H5 y carrier, pss6241–6573 y pte2544–2687

La acción derivada cuadrática se obtiene por conmutadores con el álgebra de Heisenberg. El argumento de pesos de toro restringe los operadores no compactos a derivadas de segundo orden que anulan los polinomios usados. Los operadores compactos se calculan directamente. Las identidades de menores son las identidades de reemplazar una columna por otra ya presente.

Para H5 se factoriza P=P⁺P⁻ en variables disjuntas. Las dos realizaciones de la acción difieren por un carácter det^k del grupo unitario conexo; el peso total sobre el toro determina k. Los coeficientes son exactamente ||P⁺||²m_{w⁺} y ||P⁻||²conjugado(m_{−λ}), de donde

    c_P(h,1)=||P||² m_{u2}(h) conjugado(m_{u3}(h)).

Se verificó u3=(0;3m)+u1+u2 y el umbral de integrabilidad. Esto no presupone una fase arbitraria entre las representaciones.

Carrier no nulo: la descomposición de Witt tiene matriz integral de determinante−1; el coeficiente Fourier H=1 selecciona M_uM_u*=1, una sola órbita racional de U(V). El unfolding elimina el cociente racional. La invariancia compacta da suma sobre cosets finitos. El soporte del vacío en el modelo mixto fuerza Y integral, luego Y∈K_V; sólo queda un coset. La rebanada arquimediana no nula se elige con matriz invertible por densidad. Los elementos del radical unipotente permiten todos los traslados Heisenberg de la rebanada Λ≠0. La no anulación final se puede justificar por Parseval como en §7. La rápida disminución usa el intercambio `pte:carrier` y soporte invertible; la existencia del carácter tame no trivial está disponible en los datos, y no se deduce del propio resultado de generación.

## 5. Datos y pesos de psv6593–7108

El orden o invierte el orden fijo dentro de cada bloque. La fórmula de longitudes de filas se leyó en ese orden; no se intercambiaron las condiciones de segmento inicial y final de los menores.

* α°=υ^{m/2−j}; a''+a°=n/2−κ_j. La paridad m,k pares y r impar hace enteros los exponentes.
* Los polinomios de K° usan sólo columnas negativas y segmentos iniciales de o. Dan u°positivo=−a°, u°negativo=n°−a°+ell⁻. Son no nulos y forman un espacio finito estable bajo U(V°)_∞.
* El dato Ψ° es literalmente δ_ι módulo π_M², sin escala ni nivel adicional. n°=5r−9m−1>2r. La otra aplicación tiene rank(Wflat)=6m+1>2rank(S)=6m.
* La conjugada de y tiene peso u=−Λ^K(varsigma). La derivación de la convolución es lícita por integrabilidad de todas las derivadas del coeficiente; se respeta la conjugación Y↦−εY*ε.
* Los F_i tienen peso u''; sustituyendo las longitudes de filas y a''+a° se obtiene u''+u°=u tanto en coordenadas positivas como negativas.
* Ambos u,u° son dominantes, de gap≥300n_* y entradas≤5b. Las aplicaciones de R y de isol usan exactamente estos pesos.
* `psv:split`7010–7043 coloca α(det x)⁻¹ una sola vez en el factor tildeW; el factor Wflat tiene caracteres (1,υ^m). Esa asignación es la que produce u1=(−Δ';6m+1). No hay duplicación del carácter fuente.

## 6. Imports y ausencia de círculo

La rama revisada utiliza los modelos locales y compatibilidad de sumas de49; los coeficientes de series discretas, integrabilidad y grado formal de49/51; sharpness, doubling, crecimiento y reducción de53; y los intercambios/carrier/identificación F_i de la parte anterior de54. Sus constantes no se recalculan aquí fingiendo que son independientes de esos resultados. Las revisiones respectivas deben incorporarse al dictamen global.

En particular, la fórmula R se prueba por Siegel–Weil en rango convergente y una serie de traslaciones; **no utiliza** po:span, el teorema de covolumen ni la no anulación final de L₀. El carrier nonzero tiene una prueba Fourier independiente de los escalares de intercambio. H5 es representación local y comparación de pesos. No se encontró un círculo en estas dependencias.

## 7. Dos precisiones funcionales locales suficientes

1. **psv:c, alrededor6806**, dice que los smooth vectors son funciones Schwartz en un modelo Schrödinger. Esa identificación necesita especificar la representación respecto de la cual se toma suavidad; no se sigue automáticamente para cualquier subgrupo unitario. No se usa: tome E=Schwartz en la versión general de `pss:coefs(a)`. El polinomio-gaussiano tiene órbita C∞ en Schwartz por el argumento explícito de `pss:carrier`6530–6548; la acción fija y theta son continuas en Schwartz. Resulta la misma holomorfía, con exactamente el mismo peso. Lo mismo justifica el paso paralelo de `psv:F`.

2. **pte:carriernz, párrafo final2680–2686**, llama cerrado al núcleo de todos los funcionales theta trasladados en el Hilbert irreducible. Theta no es por sí misma un funcional continuo de L². Para la rebanada Schwartz Λ basta `psq:thetanorm`: la integral de |theta(rho(w)Λ)|² sobre W_I(F)\W_I(A) es ||Λ||²>0 (o un escalar positivo si se usa una realización no normalizada). Por tanto no pueden anularse todos los traslados. Esta prueba evita la afirmación topológica innecesaria y no cambia constantes: sólo se requiere no anulación.

Estas son reparaciones locales demostradas, no fallos del enunciado de generación. El expediente global debe conservar la distinción entre el texto literal y esta justificación adicional.

## 8. Cierre documental de SW y propagación del defecto

Se descargó y leyó la fuente primaria [Weil, Acta113 (1965)](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5988-11511_2006_Article_BF02391774.pdf), copia local temporal `/tmp/weil-spanning.pdf`, extracción `/tmp/weil-spanning.txt`. Se inspeccionó además visualmente p41 para resolver las fracciones mal reconocidas por OCR. P41: caso hermitiano I₂, ε=1/2. No38/p55: condiciónB m>2n+4ε−2. Proposición8/pp75–76: convergencia si índice r_T=0 o m−r_T>n+2ε−1. Teorema5/pp76–77: medida positiva invariante de masa1, convergencia absoluta, una plaza con U(0) no vacío y transitividad local en cada U(i); entonces I=E. Estas hipótesis corresponden a53:909–925/952–958.

En ambas aplicaciones de R, T es definido positivo, así que r_T=0; los rangos son 6m+1>6m y 5r−9m−1>2r. Una plaza split existe (en particular las del módulo π_M²), y allí se eligen matrices de rango n con imagen isotrópica; la transitividad es la extensión de isometrías/Witt en el caso split. La normalización de masa1 de Weil se transforma exactamente en el factor vol([U(T)]) escrito en53. Para R sólo interesa que el factor global y c' sean no nulos. El crecimiento absoluto adicional es psr:Egrowth ya reconstruido, y no es una hipótesis omitida del teorema clásico. **La importación de SW necesaria para esta rama queda cotejada; no queda un (c) separado por ese rango.** La identificación del modelo/splitting sigue siendo el input común49, no una incertidumbre sobre el rango de Weil.

Propagación literal de νflat defectuoso al volumen58: definiciones en `58*/main.tex` líneas51272 y56151. En54 las dos definiciones están en2695 y7584. Deben corregirse coordinadamente; no basta alterar la afirmación H5. Para el defecto central puede fijarse una sola plaza arquimediana y poner h=z·1_{3m}; el carácter adicional es z^(−3m²), de modo que no existe una cancelación entre distintas plazas. La integrabilidad absoluta permite trasladar por ese centro compacto y fuerza F⁰(1)=z^(−3m²)F⁰(1), luego F⁰(1)=0.

## 9. Ficha final coordinada

Actualización tras lectura de `../revision-v2/REVISION-SPLITTING-V2.md` §§6–7 y recepción del cierre pte/ptf/pfq/KS por el agente theta:

* **Texto actual: (b).** Mantiene νflat con el factor υ^m sobrante. En consecuencia la prueba literal utiliza un F⁰(1) que vale cero; véase el cálculo central de la primera sección. No se certifica el texto actual como si la corrección ya estuviera incorporada.
* **Prueba reconstruida con νflat=ν''/χ': (a), en el alcance auditado.** Se han cerrado psp,psq,psr,pss,psv general; las dos precisiones Schwartz/Parseval están demostradas aquí. El agente theta cerró las importaciones pte/ptf/pfq/KS con la misma definición corregida. No queda una obligación matemática independiente de esas secciones sin resolver para po:span.
* **SW53: (a) para las importaciones necesarias aquí.** La fuente primaria, hipótesis, rango y masa se cotejaron en §8; no se está invocando una fórmula regularizada fuera del rango de convergencia.
* **Splitting49: pendiente histórico retirado para la reconstrucción.** El informe coordinado identifica mediante Chan el índice RV con la gaussiana de la norma y mediante Murase los generadores y la compatibilidad con sumas/doubling. El suplemento conserva la representación, no sólo su clase proyectiva; por ello se pueden utilizar los cálculos de pesos, factores de caracteres y normalizaciones de la presente revisión. La imposibilidad de leer las páginas originales de Kudla queda como limitación bibliográfica, no como una fase matemática indeterminada.

Este(a) se refiere a una comprobación matemática humana asistida y reconstruida, no a una formalización en Lean ni a una certificación automática de cada línea del repositorio. La distinción principal es concreta: el texto impreso requiere corregir las dos definiciones de νflat en54 y su propagación58, mientras que la deducción corregida de generación ya fue reconstruida con sus constantes.
