# Paper 46: cierre de los bloques analíticos puros

Fecha: 2026-11-28. Fuente: `04-papers/46-row-d-sign-radial-intersection-form/main.tex`. Lectura íntegra de 248–1598, 1783–1908 y 1930–2454; certificados 1598–1782 en NUMERICA-46 y su revisión cruzada. Las referencias siguientes son líneas de esa fuente, no páginas PDF. «a» valida el enunciado matemático señalado; las erratas explícitas se clasifican separadamente. No se convierte un resultado condicionado al input aritmético en prueba incondicional de RH.

## Dictámenes de las preguntas del usuario

1. **(a)** La equivalencia entre positividad de la forma completa en todas las ventanas y RH: fórmula explícita, criterio de Weil, paso real/complejo y densidad del núcleo de forma son compatibles. Véanse el desarrollo de all-support de ANALITICA y el informe 01. No es una equivalencia entre positividad en una ventana fija y RH. La positividad primitiva y completa en una ventana tampoco son intercambiables sin el Schur polar.
2. **(a), por reproducción independiente**, las cuatro cotas en T=log(5)/2 y su extensión por monotonía; NUMERICA-46 y NUMERICA-46-REVISION-CRUZADA contienen los certificados. La descripción original sin programa no sustituye estos certificados. El éxito certificado usa congruencia precondicionada y Gershgorin; no se afirma que la factorización intervalar ingenua haya pasado.
3. Z1–Z3 y su uso en `thm:margin/cor:margin1`: **(a)** para las cotas finales, con precisión menor explicada abajo. El uso para T=2.8022 corresponde al informe VENTANA-28022 del otro agente; no se duplica aquí.

## Obligaciones reconstruidas

| Líneas / labels | Dictamen | Comprobación efectiva |
|---|---|---|
| 248–333, comparison, eq:W | a salvo errata277 | Factor 1/(2π), masa v_n=2Λ(n)/√n, polo2AB y signos coinciden; contactos de borde tienen autocorrelación cero. |
| 335–417, lem:K, thm:S, thm:A | a | Expansión digamma da K; φ(x)=Σx/[a_k(x+4a_k²)] es Bernstein completa; integral de cola y forma de saltos con factores 1/4 y1/2 comprobadas. Las condiciones cuadráticas de Kprim no se identifican indebidamente con A=B=0. |
| 420–455, cor:mono, lem:mbounds | a para desigualdades | Cota superior también se prueba directamente por concavidad de φ y Jensen sobre el espacio de los tres primeros senos Dirichlet: ∫φ(τ²)|Fhat|²/(2π)≤φ(∫τ²|Fhat|²/(2π))≤φ((3π/2T)²). Dos momentos dejan dimensión≥1. No hace falta decidir la numeración exacta de Song–Vondraček para esta conclusión. Resto Binet por integración por partes≤1/(2|z|). |
| 457–557, form-density, monoT, compact, contA | a | Contracción de soporte y aproximación en peso log; corrección por dos funciones de momentos independientes; cola Fourier y núcleo Hilbert–Schmidt en banda dan compacidad; semicontinuidad y contracción dan continuidad de mínimos. |
| 559–704, prop:weak, gbounds, D1, D1W, O | a | Boas–Kac con raíz compleja de medio soporte; separación de cono finito mediante medias de Cesàro; independencia de momentos por términos de borde; tightness por símbolo coercivo; límite de restricciones densas. La no consecución usa transformada entera no nula y singularidad K/2 en cero. |
| 705–817, W, lem:W, P, roughEF | a para identidades y variación | Anulador del núcleo de momentos, testigos de los dos signos, normalización mediante núcleo de momentos; convolución regularizante de soporte T+ε y convergencia dominada de la suma de ceros. |
| 818–1028, F1, T0, T, T2, hybrid, E, M, TAY | a para cotas | Separación entre periodicidad de átomos y contactos primos no periódicos; caps monótonos; aproximación de átomos con control uniforme de variación; densidad L1 por unicidad de Laplace; Taylor con segunda derivada y términos monótonos al extremo izquierdo. La regla informal de coste c^(-1/2) no se interpreta como complejidad universal. |
| 1029–1219, Z, Zexh, finZ, KEP1/2/dich | a | Densidades y átomos completan exactamente fórmula explícita. En Zexh el átomo de borde se conserva; denominador positivo fuera de2T≥log2; cortes alrededor de finitísimos contactos tienen coste L1 arbitrariamente pequeño. En finZ, medida absolutamente continua con transformada local igual a suma finita tendría soporte contable: contradicción. Perturbación exterior acotada produce continuo de soluciones Krein cuando margen>0. |
| 1220–1360, arch, nodes, parity, zeroext, strict | a para mecanismos y resultados | Salto K>0 da positividad mejorante; dos momentos obligan cambios de signo; igualdad de mínimos en dos soportes fuerza todos los momentos de uf(u) a cero y luego F=0 por Weierstrass. La positividad corta invocada de Yoshida también queda cubierta por el certificado más fuerte NUMERICA-46. No se ha cotejado aquí la página precisa de Yoshida. |
| 1361–1598, Onat, Al, Alband, Cheb, parityschur, polarcap, mult | a | No consecución completa; equivalencia margen estricto/certificado plano; envolvente creciente única; integral Stieltjes sin borde; inversión en complemento del núcleo y condición de rango indispensable; fórmula polar de capacidad; coercividad en multiplicadores y separación compacta de vectores de momentos. |
| 1930–2067, coer-decomp/K1/sector/K/tail/w/poinc | a | Dimensión2k−2, exponenciales truncadas en dominio log, factor1 por pareja de bloques, cancelación del primer exponencial por Tate; doble Poincaré por expansión senoidal y suma Σ1/[n²(n²−4)]<1/3. |
| 2068–2102, coer-A | a para cota; b local2094 | División Paley–Wiener por s²+a usa ambos ceros de Tate, H² con trazas nulas; desigualdad principal correcta pese a ubicación inexacta del máximo para R pequeño (abajo). |
| 2112–2191, coer-lowpass/B | a | Interpolante cosh/sinh iguala valor y derivada al centro; resto L2≤cosh²(r)r⁴/6 por Cauchy–Schwarz; integración por capas con ε′≥0; θ*>r para0<r≤1; primitiva Φ verificada por derivación. |
| 2198–2370, coer-prime/L1/schur, inertiatower, firstcontact | a para desigualdades estructurales | Fibras del desplazamiento son caminos de longitud ceil(2T/ell); Schur por Riesz en bloque coercivo; cotas de Rayleigh respetan inversión del signo cuando λS<0; primer contacto por continuidad y compacidad. Valores tabulados redondeados no son certificados independientes de esta revisión. |
| 2371–2403, ladder | a | K(a,b) tiene polo1/((a−1)b)+1/(a(b−1)) y factor(a+b−1) correctos. Aproximación C1 en x=e^(−y), error Fourier O(ε/(1+|τ|)), momentos y serie prima dominados; matrices de todos los grados suficientes. |
| 2405–2409, comparaciones finitas | c | El propio texto dice sin prueba; no hay aquí certificado para cuatro exponentes arbitrarios ni trece polos con multiplicidades. No se usan en ladder ni en la deducción posterior. |
| 2411–2428, all-degree-gram | a condicionado | El input dirichlet-input da ceros en línea mediante ecuación funcional; sólo entonces conjugación convierte producto en módulo cuadrado. Hadamard pareado y convergencia O(γ^-2) correctos. Su condición no queda demostrada por esta proposición. |

Fuente primaria complementaria para Boas–Kac: [Ehm–Gneiting–Richards, artículo de 2004, resumen institucional](https://pure.psu.edu/en/publications/convolution-roots-of-radial-positive-definite-functions-with-comp/), confirma raíz L2 compleja con soporte mitad. El carácter complejo es suficiente en prop:weak; no se impone una raíz real sin prueba.

## Primeras líneas defectuosas y reparación

**277, (b) literal.** `2 Re(a conjugate(b′))` no es una forma hermitiana en dos vectores: ni es sesquilineal ni satisface la simetría hermitiana. En vectores (1,0),(0,1) da2 en un orden y0 en el inverso. La expresión correcta es `a conjugate(b′)+b conjugate(a′)`. Su diagonal es exactamente2Re(a conjugate(b)), que es la expresión usada en eq:W. No invalida las formas cuadráticas ni las polarizaciones reales posteriores.

**2094, (b) literal.** El máximo sobre0≤x≤R² no está en(2R²−a)/3 cuando R²<a/2. Ejemplo permitido: r=0.1,a=0.0025,R=0.01; el punto es negativo. La cota usada sigue siendo cierta: y=x+a pertenece a[0,R²+a], y²(R²+a−y)≤4(R²+a)^3/27. Dividiendo por R² resulta exactamente M_R. Esta reparación no cambia ninguna constante ni restringe R; la aplicación numérica R=2 ya satisface la condición interior.

**1896–1899, precisión y no refutación.** Con el valor real de γ1, ε9=0.0156613114…<0.01567 es verdadero. Pero la afirmación previa de que sólo se usa14.13≤γ1≤14.14 no basta para ese decimal: γ1≥14.13 sólo da ε9≤0.0157505828. Se puede usar ε≤0.016 y conservar0.5−ε≥0.484, exactamente el denominador posterior. Por tanto cor:margin1 permanece con constante4·10^9 y exponente15.449 usando únicamente el intervalo anunciado. El script Z1 certifica también el valor más preciso, si se desea conservar0.01567.

## Z1–Z3: margen, sin RH presupuesta

Z1 queda certificado independientemente por `evidencia/verificar_Z1_margin_46.py` y `Z1_margin_46_arb.json`: Arb a256 bits encierra rho1=1/2+14.13472514173469…i y devuelve N(21)=1 exactamente. La función de conteo cuenta TODOS los ceros con multiplicidad; por tanto es simple y no existe otro cero con0<Im≤21. Fuente primaria: [documentación Arb2.23 acb_dirichlet](https://arblib.org/acb_dirichlet.html), entradas zeta_zero y zeta_nzeros. No se infiere simplicidad sólo de una aproximación a la raíz.

Z2 permite términos no negativos únicamente hasta H_PT; por encima el texto usa |β|<1/2 y valor absoluto con factor e^T. Z3 se usa en integración por partes para Σp(H), p≥2; el factor2 suma las dos mitades de las ordenadas. Las hipótesis de roughEF se satisfacen: k≥5 produce transformada O(|τ|^(4−k)), peso log integrable, y la misma cota Σp verifica convergencia absoluta de la suma de ceros. No se ha usado RH para la cola no verificada.

En cor:margin1, k=ceil(21T/e), k≥8. Para k fijo ε decrece en T; en extremos izquierdos T=(k−1)e/21, con C=eγ1/(21√2)>9/8, la derivada del logaritmo respecto de k es
`2 log(k/[C(k−1)])−1/(k−1)−2/(2k−1)<0` para k≥9.
El caso k=8 y el extremo k=9 bastan. La constante final usando0.484 es3.9632451423·10^9<3.97·10^9. La cola alta es menor que10^-70 de la primera. Se reconstruyeron el soporte, las cancelaciones de polos y primer par de ceros, el límite superior y la disminución del margen; esto no demuestra positividad.

## Pendientes reales y alcance

No queda una obligación analítica estructural abierta en los bloques puros leídos salvo las dos comparaciones expresamente sin prueba2405–2409. Quedan sin certificación separada los redondeos ilustrativos de umbrales y tablas que no son los certificados solicitados; las cotas estructurales correspondientes sí están reconstruidas. La exactitud bibliográfica de algunas numeraciones de fuentes clásicas no equivale a un hueco en las pruebas alternativas dadas arriba. La cadena aritmética que suministra dirichlet-input se juzga en los otros ledgers y conserva su defecto identificado en P53: esta revisión no lo repara.
