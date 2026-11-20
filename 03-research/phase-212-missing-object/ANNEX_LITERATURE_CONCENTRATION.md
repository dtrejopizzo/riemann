# Anexo — literatura: mecanismos de positividad de tipo concentración

Notación de la fase: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, sop F ⊂ [−T,T],
∫F e^{±t/2} = 0; Arch(F) = ∫W F² + ¼∬K(|t−s|)(F(t)−F(s))², K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)).

Nota de búsqueda de herramientas. No se deriva nada y no se afirma que la solución esté en la literatura.
Lo que se busca: una expresión positiva que sea a la vez (a) de tipo concentración (transformada seguida
de restricción), (b) isométrica sólo para los enteros verdaderos (usa Σ_{d|n}Λ(d) = log n y el espaciado
igual), (c) no local por primo, (d) exacta, (e) de dimensión creciente con la ventana.

Etiquetas: CITED = lo que el artículo enuncia; ARGUED = lectura propia. Los números de teorema son los de la
versión arXiv consultada; los que se dan «sin número» no se pudieron leer en primaria y hay que verificarlos
antes de citarlos en otro sitio. Lo mismo vale para los datos de revista (volumen, año) de los ítems cuyo
registro arXiv no los trae: el identificador arXiv es el dato comprobado. Para cada ítem se indican: mecanismo de signo; si ve estructura aditiva y
multiplicativa; conducta bajo (i) peso ×2, (ii) borrado de una potencia de primo, (iii) sistema de Beurling;
clase de la taxonomía de `ROUND_009_G3.md` §1 (1–25).

**Conclusión adelantada.** Ningún ítem reúne las cinco características. En particular, ninguno tiene un
signo que dependa de los valores exactos del peso: todos los mecanismos encontrados son o bien libres de
peso (dependen de los nodos, no de v_n), o bien desigualdades con holgura, o bien identidades válidas para
todo peine. Hay cinco mecanismos sin marca sustantiva en el corpus (§6); ninguno pasa la puerta tal cual.

---

## 0. Cotejo previo con el corpus

Casi todo el perímetro pedido ya está registrado. Se da la entrada del índice (IDX =
`05-meta-and-planning/ROUTES-TRIED-INDEX/`) para no repetirlo; de estos ítems sólo se reporta lo que el
corpus no usó.

| Tema | Dónde está | Estado allí |
|---|---|---|
| Radchenko–Viazovska, Bondarenko–Radchenko–Seip, Kulikov–Nazarov–Sodin | `phase-35-five-fronts/101-…`; IDX P35-4, L30, L102 | NO-GO (refutación independiente del peso) |
| Medidas cristalinas, Kurasov–Sarnak, Olevskii–Ulanovskii, Wei | IDX L30, L60, L101; R162_1002 | bajo / no aplica |
| Funciones mágicas, CKMRV | IDX frentes L, N | NO-GO (thm:O) |
| Incertidumbre de signo | 8 archivos; IDX 1 | sin ruta |
| Prolatos, Sonin, forma semilocal, triples espectrales, forma truncada | IDX L06–L09, L39–L41, L68, L106; fase 183 | cadena de Sonin PROVED sin signo |
| de Branges, Kreĭn, Hermite–Biehler, Lagarias, Burnol (co-Poisson, operador conductor), Suzuki, Bombieri, Yoshida | IDX L02, L03, L11, L12, L16, L17, L20, L36, L38 | usados / reformulación |
| H² de series de Dirichlet, Hedenmalm–Lindqvist–Seip, Helson, Perfekt, matriz de Hilbert multiplicativa | IDX L87; `AUDIT_PHASE193`; fase 159 (G1_P2_R3) | sólo cotas superiores; genérico en el peine |
| Nyman–Beurling, Báez-Duarte, Vasyunin, Bettin–Conrey | IDX L18, L61, L79, L95; fase 150 (T3); G2_B10_R1 | reformulación; Vasyunin «no usado en la fila D» |
| Álgebra de Toeplitz de ℕ ⋊ ℕ^× (Laca–Raeburn), Bost–Connes | fase 159 (G1_B5_R3, G1_P4_R5) | citado |
| Conmutante diferencial de la ventana (bispectralidad) | `phase-200-sign-object/SPEC_SIGN_OBJECT_011.md`; IDX README CS0_COMMUTE_001 | orden ≤ 2 PROVED trivial; orden > 2 OPEN |
| Reflexión positiva | clase 17; R-K1 | por lugar / borde, excluida |
| Procesos determinantales | IDX G8D-R160_S5; `ROUND_009_G3.md` §3 | «no virgen» |
| SOS / Positivstellensatz | IDX frente E, G2C-159 | REF-D |
| Borodin–Okounkov | sólo fase 67 (otro objeto) | no aplicado a la ventana |

Sin coincidencia en `03-research/` ni en `05-meta-and-planning/` (grep; no prueba novedad conceptual):
«hyperbolic Fourier series», «quasimodular», «Serre derivative», «Dritschel», «Geronimo», «Neeb»,
«Katsnelson», «Olofsson», «reflect… differential operator». Con una sola coincidencia: «Heisenberg
uniqueness» (nota de laguna bibliográfica en `phase-47-live-fronts/148-…`), «Frank–Lieb / inversion
positivity», «Ramos», «Stoller».

---

## 1. Interpolación de Fourier, pares de unicidad, medidas cristalinas

**1.1 Bondarenko–Radchenko–Seip.** A. Bondarenko, D. Radchenko, K. Seip, *Fourier interpolation with zeros
of zeta and L-functions*, Constr. Approx. 57 (2023); arXiv:2005.02996. Teorema 1.1 (CITED): para f par,
analítica en una banda |Im z| < ½+ε con integrabilidad ponderada, f se reconstruye de los valores de f̂ en
los nodos log n/(4π), n ≥ 1, y de los valores (con derivadas hasta la multiplicidad) de f en un segundo
conjunto discreto, el del título; las funciones base U_n, V son enteras, pares, de decaimiento rápido, y
la fórmula deja de valer si se quita un solo nodo. Teoremas 2.1–2.2: núcleos de series de Dirichlet
asociados a la sucesión y a su dual. La sección 5 cubre otras series, incluida una subsección «Dirichlet
series without Euler products».
- Mecanismo: identidad lineal de dualidad (formas modulares débilmente holomorfas para el grupo theta);
  no hay enunciado de signo.
- Aditivo/multiplicativo: usa los nodos log n (aditivos en n vía el grupo theta) y la ecuación funcional;
  no usa el producto de Euler.
- Falsificadores: (i) no depende del peso, no se rompe; (ii) el nodo log n sigue estando aunque se borre
  v_n, no se rompe; (iii) se rompe (necesita los enteros como nodos), pero por los nodos, no por el peso.
- Clase 20 (identidad válida para todo peine con esos nodos). Lo que el corpus no usó: el enunciado de
  minimalidad («no sobra ningún nodo»). ARGUED: es una propiedad del par de conjuntos, no de v_n; no
  distingue cΛ de Λ. No habilita nada.

**1.2 Kulikov–Nazarov–Sodin.** A. Kulikov, F. Nazarov, M. Sodin, *Fourier uniqueness and non-uniqueness
pairs*, J. Math. Phys. Anal. Geom. 21 (2025); arXiv:2306.14013. Definición 2 (CITED): (Λ,M) es
supercrítico si limsup |λ_j|^{p−1}(λ_{j+1}−λ_j) < ½ y limsup |μ_j|^{q−1}(μ_{j+1}−μ_j) < ½, 1/p+1/q = 1;
subcrítico con liminf > ½. Teorema 1: supercrítico ⟹ par de unicidad; subcrítico ⟹ no unicidad.
Teorema 2: para pares supercríticos separados, c‖f‖² ≤ Σ pesos·|f(λ)|² + Σ pesos·|f̂(μ)|² ≤ C‖f‖² en un
espacio de Sobolev simétrico ℋ_{s,p,q}. Corolario 2: fórmula de interpolación. Corolario 3: para todo par
supercrítico hay medidas cristalinas no triviales, en dimensión infinita.
- Mecanismo: desigualdades de Poincaré–Wirtinger en los huecos entre nodos, luego Phragmén–Lindelöf. Es una
  cota inferior coercitiva de tipo marco, con constantes no explícitas.
- Falsificadores: sin peso; insensible a (i) y (ii); depende sólo de la densidad de nodos, así que un
  sistema de Beurling con la misma densidad lo conserva.
- Clase 21 (estimación con resto). ARGUED: en el punto crítico (constante exactamente ½) el Teorema 2 no
  da cota; la forma objetivo vive en ese régimen (margen exponencialmente pequeño). Lo no usado en el
  corpus es el Teorema 2; no sirve por P5.

**1.3 Ramos–Sousa.** J. P. G. Ramos, M. Sousa, *Fourier uniqueness pairs of powers of integers*, J. Eur.
Math. Soc. 24 (2022); arXiv:1910.04276. Unicidad para nodos ±n^α, ±n^β en un rango de exponentes, por
perturbación de la fórmula de Radchenko–Viazovska (CITED del resumen; sin número). Mismo diagnóstico
que 1.2; superado por 1.2.

**1.4 Rigidez cristalina.** N. Lev, A. Olevskii, *Quasicrystals and Poisson's summation formula*, Invent.
Math. 200 (2015): una medida en ℝ con soporte y espectro uniformemente discretos es combinación finita de
peines de Dirac de retículos (CITED; sin número). P. Kurasov, P. Sarnak, *Stable polynomials and
crystalline measures*, J. Math. Phys. 61 (2020); A. Olevskii, A. Ulanovskii, *Fourier quasicrystals with
unit masses*, C. R. Math. 358 (2020): masas positivas enteras ⟺ conjunto de ceros de un polinomio
exponencial con raíces reales.
- Es el único enunciado del perímetro que *deduce* el espaciado igual de una hipótesis bilateral de
  discreción (característica (b)). Mecanismo: rigidez (Helson–Cohen/idempotentes), no signo.
- Ya cotejado (IDX L30, L60, L101): el par de la forma tiene una densidad absolutamente continua del lado
  arquimediano y un peine con signo; la hipótesis no se cumple. Clase 25/20. Nada nuevo.

**1.5 Hedenmalm–Montes-Rodríguez; series de Fourier hiperbólicas.** H. Hedenmalm, A. Montes-Rodríguez,
*Heisenberg uniqueness pairs and the Klein–Gordon equation*, Ann. of Math. 173 (2011) 1507–1527;
arXiv:0910.1246. Enunciado principal (CITED; sin número): para la hipérbola x₁x₂ = 1 y la cruz de
retículo (αℤ×{0}) ∪ ({0}×βℤ), hay unicidad si y sólo si αβ ≤ 1; equivalentemente, el sistema
{e^{iπαnt}, e^{iπβn/t}}_{n∈ℤ} es débil-∗ denso en L^∞(ℝ) exactamente cuando αβ ≤ 1. F. Canto-Martín,
H. Hedenmalm, A. Montes-Rodríguez, *Perron–Frobenius operators and the Klein–Gordon equation*, J. Eur.
Math. Soc. 16 (2014). A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, M. Viazovska,
*Hyperbolic Fourier series*, arXiv:2110.00148 (CITED del resumen): sistema biortogonal explícito en L¹(ℝ)
para {1, e^{iπnx}, e^{iπn/x}}, completo, y desarrollo convergente en distribuciones temperadas; la parte de
unicidad equivale a la de Radchenko–Viazovska en densidad crítica.
- Mecanismo: operador de transferencia (Perron–Frobenius) de una aplicación de tipo Gauss x ↦ −1/x mód 2
  en [−1,1], con medida invariante infinita; la unicidad en el caso crítico αβ = 1 sale de que los
  iterados del operador de transferencia (positivo) tienden a cero. Es positividad de cono bajo un operador
  que **no es una convolución** (composición con una aplicación expansiva).
- Aditivo/multiplicativo: traslaciones enteras e inversión t ↦ −1/t (grupo theta); la inversión es la
  «transformada de Fourier + inversión de escala» en otra presentación. Sin primos, sin peso.
- Umbral exacto en un parámetro: cambiar el espaciado (α ó β) rompe el enunciado en el valor crítico.
  Es la única dicotomía exacta del perímetro cuyo punto crítico es el retículo entero. Pero el parámetro
  es el espaciado de los nodos, no el peso: (i) y (ii) no aplican; (iii) rompe (hace falta ℤ).
- Clase: cercana a 14 (Markov/operador positivo), pero la operación es un operador de transferencia de una
  aplicación expansiva, no un semigrupo de convolución plegado; ARGUED: no queda cubierta por la razón de
  fracaso de 14 (rama reflejada |t−u|) ni por P12. El corpus tiene operadores de transferencia sólo en la
  forma Mayer/Dolgopyat (IDX G3H-152, estimaciones) — otro uso.

---

## 2. Funciones mágicas, cotas de programación lineal, incertidumbre de signo

**2.1 Cómo se certifica allí un signo exacto.** M. Viazovska, *The sphere packing problem in dimension 8*,
Ann. of Math. 185 (2017); H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, *Universal
optimality of the E₈ and Leech lattices and interpolation formulas*, Ann. of Math. 196 (2022), Teorema 1.7
(interpolación con f, f′, f̂, f̂′ en √(2n); CITED, número según la introducción publicada). El signo de la
función mágica se obtiene escribiéndola como sin²(πr²/2) por una transformada de Laplace de un núcleo
modular de signo definido en el eje imaginario; el signo del núcleo se probó originalmente con aritmética
de intervalos sobre coeficientes de Fourier.
- Mecanismo: (ceros dobles forzados en las longitudes del retículo) × (transformada de Laplace de una
  función de signo constante). Es un certificado dual: funcional lineal sobre la autocorrelación.
- Corpus: thm:O (frentes L, N), NO-GO. Clase 1/20. No se repite.

**2.2 Prueba algebraica de las desigualdades modulares.** S. Lee, *Algebraic proof of modular form
inequalities for optimal sphere packings*, arXiv:2406.14659. Definiciones (§3): una forma cuasimodular F
es *positiva* si F(it) ≥ 0 para t > 0, y *completamente positiva* si todos sus coeficientes de Fourier son
≥ 0. Proposición 3.4: completamente positiva ⟺ todas las derivadas son positivas (Bernstein).
Proposición 3.5 (CITED): si (∂_kF)(it) ≥ 0 en 0 < t < t₀ y F(it₀) > 0, entonces F(it) > 0 en (0,t₀]; la
prueba es que F/Δ^{k/12} es monótona en el eje imaginario. Corolario 3.6: si la derivada de Serre ∂_kF es
positiva y F(it) > 0 para t grande, F es positiva. Proposición 3.8: condiciones bajo las que ∂_k conserva
la positividad completa. Con esto se prueban sin cómputo numérico las desigualdades de las dimensiones 8 y
24. Mismo autor, *Positive quasimodular forms and the sign uncertainty principle*, arXiv:2608.15415:
A₊(d) ≤ √(2⌊d/16⌋+2) para 4 | d (CITED del resumen).
- Mecanismo: comparación de una EDO de primer orden a lo largo del eje imaginario (la derivada de Serre es
  la derivada logarítmica covariante respecto de Δ^{k/12}), con caso base dado por *integralidad con signo*
  de los coeficientes q. Ecuación funcional (modularidad) e integralidad entran en el mismo paso: el anillo
  diferencial de formas cuasimodulares es cerrado por derivación (identidades de Ramanujan).
- No ve producto de Euler ni primos. Falsificadores: no hay peso; no aplican.
- Clase 16 (monotonía bajo un flujo), con una diferencia: el flujo es en la variable modular y el caso base
  es aritmético. Sin marca en el corpus («quasimodular», «Serre derivative»: 0 archivos).
- ARGUED: da signo puntual de una función en el eje, no semidefinición positiva de un núcleo; el corpus ya
  registra que el signo puntual de la función tornillo es a lo sumo una condición necesaria (IDX L72) y que
  Bochner en θ está excluido (regla C-hom, `RULES_AVOID.md` §G2).

**2.3 Incertidumbre de signo.** J. Bourgain, L. Clozel, J.-P. Kahane, *Principe d'Heisenberg et fonctions
positives*, Ann. Inst. Fourier 60 (2010); H. Cohn, F. Gonçalves, *An optimal uncertainty principle in
twelve dimensions via modular forms*, Invent. Math. 217 (2019) (constante óptima √2 en dimensión 12, con
autofunción −1 de la transformada de Fourier construida por la transformada de Viazovska); F. Gonçalves,
D. Oliveira e Silva, J. P. G. Ramos, *On regularity and mass concentration phenomena for the sign
uncertainty principle*, J. Geom. Anal. 31 (2021), arXiv:2003.10765 (los minimizantes se pueden tomar en la
clase de Schwartz en d = 1; infinitos ceros después del último cambio de signo); de los mismos autores,
*New sign uncertainty principles*, arXiv:2003.10771.
- Mecanismo: sumación de Poisson aplicada a una autofunción ±1; el signo se certifica por un funcional
  lineal con signo (dualidad de programación lineal). Para el lado +1 en d = 1 no se conoce la constante.
- Covariante por escala, sin peso, sin primos. Clase 1/20 (clase dual = el propio objetivo, C3). Nada que
  transferir.

---

## 3. Operadores prolatos, espacios de Sonin, fórmulas semilocales (posteriores a 2020)

Todo lo localizado está en IDX (L06–L09, L39–L41, L68, L106, L109). No se encontró ningún trabajo de estos
autores posterior a los allí listados. Se precisa qué está probado sobre los autovalores pequeños y por qué
mecanismo, porque es el punto donde la característica (a) aparece en la literatura.

**3.1** A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. 27
(2021); arXiv:2006.13771. La parte arquimediana de la forma sobre una ventana se identifica con una traza
de la acción de escala comprimida al espacio de Sonin, y de ahí se obtiene positividad en ventanas
pequeñas, reduciendo el resto a una restricción de codimensión finita (CITED del resumen e introducción).
Mecanismo: compresión de un unitario (transformada + restricción). Sólo el lugar arquimediano.

**3.2** A. Connes, C. Consani, *Spectral triples and ζ-cycles*, Enseign. Math. 69 (2023);
arXiv:2106.01715. Probado (CITED del resumen): la forma restringida a soporte en un intervalo fijo tiene
autovalores muy pequeños, y los vectores correspondientes se obtienen aplicando la suma aritmética
E(f)(x) = x^{1/2}Σ_n f(nx) a funciones prolatas en la escala de la ventana; el radical de la forma es la
imagen de E. Es una **cota superior** del fondo del espectro (existencia de direcciones casi nulas).
- Lectura (ARGUED): E es exactamente «transformada que usa el espaciado igual» y la restricción es la
  ventana; el mecanismo produce la pequeñez superexponencial, no el signo. Ninguna cota inferior sale de
  él. Coincide con la cadena de Sonin del corpus (fase 183: PROVED, sin signo; muro W-Sonin).

**3.3** A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, arXiv:2310.18423; y
*Zeta spectral triples*, arXiv:2511.22755. De la segunda (CITED): Teorema 3.6, el operador de la forma en
la ventana tiene espectro discreto acotado inferiormente; Corolario 3.7, existe un autovector del fondo
μ_λ; el texto declara que no se puede afirmar μ_λ ≥ 0. Teoremas 1.1 y 5.10: bajo la hipótesis de que el
autovalor mínimo de la truncación de dimensión finita es simple y su autovector par (hipótesis, no
teorema), un operador perturbado es autoadjunto para el producto interno T = Q − ε_N ≥ 0 y vale una
identidad de determinante. La aproximación del autovector mínimo por funciones prolatas es observada y
apoyada en estimaciones citadas (Lema 7.2); el paso que la justificaría se declara abierto.
- Mecanismo del único signo que aparece: T ≥ 0 por construcción (se resta el autovalor mínimo). No es un
  signo de la forma.

**3.4** A. Connes, W. van Suijlekom, *Quadratic forms, real zeros and echoes of the spectral action*,
arXiv:2511.23257 (IDX L09). Mecanismo: propiedad de raíces reales del estado fundamental de la forma
truncada, de tipo Hermite–Biehler sobre un vector, no signo de la forma (clases 7 y 9 del corpus, B9).

Resumen de §3 (ARGUED): la literatura prolata prueba (1) discreción y acotación inferior, (2) cotas
superiores superexponenciales del fondo vía E∘prolatas, (3) estructura condicionada a simplicidad y
paridad. La positividad en la ventana no se obtiene de ninguno de los tres. Clases 10 y 20.

---

## 4. Espacios de de Branges, Hermite–Biehler, sistemas canónicos con entrada aritmética

Todo cubierto en IDX. Enunciados incondicionales de positividad en ventanas y su mecanismo:

| Fuente | Enunciado incondicional | Mecanismo |
|---|---|---|
| H. Yoshida, *On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21 (1992) (IDX L03) | positividad para soporte pequeño (sin número verificado) | para soporte por debajo de log 2 el peine no entra; queda la parte arquimediana, tratada por comparación y cómputo |
| E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Rend. Mat. Acc. Lincei (9) 11 (2000) (IDX L01–L02; el corpus usa Thm 3, 5, 12) | mínimo alcanzado, continuidad, costo de los primos | compacidad y cálculo de variaciones; el signo no sale del método |
| J.-F. Burnol, *The explicit formula and the conductor operator*, arXiv:math/9902080; *Sur les formules explicites I*, C. R. Acad. Sci. 331 (2000) | cada término local es −(log|x|_v + log|y|_v) conjugado por Fourier; acotación inferior por lugar | positividad local por lugar (clase 2; P8) |
| J.-F. Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, J. Théor. Nombres Bordeaux 16 (2004), arXiv:math/0203120; *Entrelacement de co-Poisson*, Ann. Inst. Fourier 57 (2007) | completitud y minimalidad de sistemas en espacios de Sonin; fórmula co-Poisson | unitaridad de «Fourier + inversión» y condiciones de soporte (clase 10/20); sin signo de la forma |
| M. Suzuki, serie de sistemas canónicos y función tornillo (IDX L12, L36, L38) | existencia del hamiltoniano y positividad localizada para ventanas pequeñas; continuidad del autovalor mínimo en el tamaño de la ventana | invertibilidad de I ± K en ventana pequeña (perturbación de la identidad; clase 3/21) |
| J. C. Lagarias, espacios de funciones enteras (IDX L17) | reformulación | — |

ARGUED: los resultados incondicionales en ventanas vienen de uno de tres mecanismos: (a) el peine no entra
en el rango de soporte; (b) el peine es una perturbación dominada por la coercividad arquimediana
(P2 lo excluye para T ≳ 0.60); (c) certificado numérico por ventana (W-fam). Ninguno es de tipo
concentración con entrada aritmética. Nada no usado.

---

## 5. Mecanismos de otros campos

**5.1 Positividad por inversión para núcleos no locales.** R. L. Frank, E. H. Lieb, *Inversion positivity
and the sharp Hardy–Littlewood–Sobolev inequality*, Calc. Var. PDE 39 (2010): para el núcleo |x−y|^{−λ}
hay positividad por reflexión respecto de inversiones en esferas, ∬ f(x) f(Θy)… ≥ 0 para f soportada en un
lado (CITED; sin número). K.-H. Neeb, G. Ólafsson, *Reflection positive one-parameter groups and
dilations*, Complex Anal. Oper. Theory 9 (2015), arXiv:1312.6161; *Reflection Positivity*, Springer
Briefs (2018), cap. 4: clasificación de los grupos unitarios de un parámetro con reflexión positiva y su
relación con espacios salientes de Lax–Phillips.
- Observación elemental (ARGUED): con x = e^t, y = e^s se tiene √(xy)/|x−y| = 1/(2sinh(|t−s|/2)) y
  √(xy)/(x+y) = 1/(2cosh((t−s)/2)); es decir, K es el núcleo |x−y|^{−1} + |x+y|^{−1} en la semirrecta en
  medida de Haar, y la inversión x ↦ 1/x es t ↦ −t. La parte sinh es completamente monótona en u; la parte
  cosh es una serie alternada de exponenciales y no lo es.
- Mecanismo: ⟨ΘF,F⟩ ≥ 0 para F soportada en t > 0. Para F soportada en [−T,T] sólo controla el término
  cruzado entre las dos mitades, y sólo de la parte sinh. Sin peso, sin primos; los tres falsificadores no
  aplican. Clase 17; el cotejo de `ROUND_009_G3.md` §3 (reflexión en 0 = ⟨JF,F⟩, cae en R3-a) y la regla
  R-K1 ya lo cubren. Frank–Lieb aparece en un solo archivo del corpus; el mecanismo no es nuevo.

**5.2 Toeplitz / Wiener–Hopf sobre el semigrupo multiplicativo.**
- H. Hedenmalm, P. Lindqvist, K. Seip, *A Hilbert space of Dirichlet series and systems of dilated
  functions in L²(0,1)*, Duke Math. J. 86 (1997): {φ(nx)} es base de Riesz de L²(0,1) si y sólo si la
  serie de Dirichlet de los coeficientes de φ y su inversa son multiplicadores de ℋ² (CITED; sin número).
  Las dilataciones D_n son isometrías que representan (ℕ,·) sobre funciones 2-periódicas impares: es el
  único objeto clásico donde el espaciado igual (ortonormalidad de sin πnx) y la multiplicación actúan a
  la vez. Citado en la fase 159.
- H. Helson, *Hankel forms and sums of random variables*, Studia Math. 176 (2006): (Σ|a_n|²/d(n))^{1/2} ≤
  ‖f‖_{ℋ¹}. Mecanismo: iteración primo a primo de una desigualdad de una variable. Sólo monoide libre:
  vale en cualquier sistema de Beurling (B7).
- O. F. Brevig, K.-M. Perfekt, K. Seip, A. Siskakis, D. Vukotić, *The multiplicative Hilbert matrix*, Adv.
  Math. 302 (2016), arXiv:1411.7294: norma π; forma de Hankel multiplicativa. Cota superior (B10).
- J.-F. Olsen, *Local properties of Hilbert spaces of Dirichlet series*, J. Funct. Anal. 261 (2011),
  arXiv:1011.3370. Teorema 1 (CITED): Σ_{n≤x} w_n ≲ x/(log x)^α ⟺ el espacio ponderado ℋ_w se sumerge
  localmente (en cada intervalo acotado de la recta Re s = ½) en D_α del semiplano. Teoremas 2 y 4: bajo
  la cota inferior correspondiente, toda f de D_α coincide en la ventana con una F ∈ ℋ_w salvo un término
  que se prolonga analíticamente. Teorema 3: mismas medidas de Carleson de soporte compacto y mismas
  sucesiones interpolantes acotadas. Ejemplo 3: w_n = Λ(n)/log n. Antecedentes: J.-F. Olsen, K. Seip, *Local
  interpolation in Hilbert spaces of Dirichlet series*, Proc. AMS 136 (2008); J.-F. Olsen, E. Saksman,
  J. reine angew. Math. 663 (2012).
  - Es un enunciado **de ventana** en el peso crítico con entrada de primos. Mecanismo: densidad de
    muestreo de la medida Σ w_n δ_{log n}/n (Beurling–Jaffard–Seip, Ortega-Cerdà–Seip). Equivalencias
    hasta constantes: clase 21. Depende sólo de cotas de Chebyshev del peso: se conserva con peso ×2, con
    un borrado y en sistemas de Beurling con la misma densidad. No lleva signo.
- Nyman–Beurling–Báez-Duarte: la matriz de Gram de las partes fraccionarias dilatadas tiene forma cerrada
  (Vasyunin) y la suma de cotangentes c₀(h/k) cumple una fórmula de reciprocidad (S. Bettin, J. B. Conrey,
  *Period functions and cotangent sums*, Algebra Number Theory 7 (2013)). Es una identidad exacta que ve
  h/k aditiva y multiplicativamente, sobre una matriz manifiestamente semidefinida positiva y libre de Λ.
  ARGUED: no es una forma en una ventana de soporte, y Λ entra sólo por los coeficientes del aproximante;
  factoriza por un objeto Λ-libre fijo (P9). El corpus la registra como no usada (G2_B10_R1) y cierra la
  familia como reformulación (T3).
- M. Laca, I. Raeburn, *Phase transition on the Toeplitz algebra of the affine semigroup over the natural
  numbers*, Adv. Math. 225 (2010), arXiv:0907.3760. Teorema 4.1 (CITED): 𝒯(ℕ ⋊ ℕ^×) es universal para una
  isometría s y isometrías v_p con (T1) v_p s = s^p v_p, (T2) v_p v_q = v_q v_p, (T3) v_p^* v_q = v_q v_p^*,
  (T4) s^* v_p = s^{p−1} v_p s^*, (T5) v_p^* s^k v_p = 0 para 1 ≤ k < p. Proposición 6.1: en el cociente de
  frontera (álgebra de Cuntz 𝒬_ℕ) vale Σ_{k<p} (s^k v_p)(s^k v_p)^* = 1.
  - (T5) y la desigualdad 1 − Σ_{k<p} s^k v_p v_p^* s^{*k} ≥ 0 son la forma operatorial de «las clases
    residuales mód p son ortogonales y llenan ℤ»: una positividad exacta que sólo vale para los enteros
    verdaderos y usa suma y producto en una misma relación. Se rompe en Beurling (no hay s). No tiene
    peso: insensible a (i) y (ii).
  - Citado en la fase 159 (presentación). ARGUED: lo que no encontré usado es (T5) como proyección
    complementaria dentro de la compresión a la ventana. Es un objeto Λ-libre fijo (P9) y la ventana no
    es invariante por v_p; clase 9/10 sin operación nueva. No lo propongo.

**5.3 Fejér–Riesz en varias variables y sumas de cuadrados.** M. A. Dritschel, *On factorization of
trigonometric polynomials*, Integral Equations Operator Theory 49 (2004): un polinomio trigonométrico en
varias variables, con valores operadores, estrictamente positivo es suma finita de cuadrados hermíticos de
polinomios analíticos (CITED; sin número; sin cota de grado). M. A. Dritschel, *Factoring non-negative
operator valued trigonometric polynomials in two variables*, arXiv:1811.06005: en dos variables basta no
negatividad, con control de número y grados, por complementos de Schur. J. Geronimo, H. Woerdeman,
*Positive extensions, Fejér–Riesz factorization and autoregressive filters in two variables*, Ann. of
Math. 160 (2004): condición necesaria y suficiente, en términos de los coeficientes de Fourier, para la
factorización espectral estable en dos variables.
- Por el levantamiento de Bohr, un polinomio de Dirichlet en los primos ≤ P es un polinomio trigonométrico
  en π(P) variables. Mecanismo: existencia de SOS dada la positividad; el certificado existe si y sólo si
  vale el objetivo, y sin cota de grado con margen e^{−cT}. Clases 1 y 4 (B3, J3). Además la forma en la
  ventana es una compresión, no un operador de Toeplitz en el toro. Nombres nuevos, mecanismo ya cerrado
  (frente E).

**5.4 Identidad de Borodin–Okounkov en intervalo finito.** E. Basor, Y. Chen, *A note on Wiener–Hopf
determinants and the Borodin–Okounkov identity*, Integral Equations Operator Theory 45 (2003),
arXiv:math/0202062 (CITED): det(I − K_{[0,α]}) = Z e^{cα} det(I − L_{[α,∞)}), con Z y c dados por la
factorización de Wiener–Hopf del símbolo y L un operador en la semirrecta complementaria de núcleo
pequeño. Variantes Wiener–Hopf + Hankel: Basor–Ehrhardt, arXiv:math/0304002.
- Es exactamente de tipo concentración y exacta: el determinante en la ventana es una constante por un
  determinante de Fredholm de la restricción complementaria de un producto de operadores de Hankel, que es
  superexponencialmente cercano a 1. Dimensión creciente con α.
- Mecanismo: identidad de Jacobi para menores complementarios de A y A^{−1}. Vale para todo símbolo con
  factorización (identidad genérica: B1, clase 20); exige símbolo sin ceros e índice cero, y el símbolo de
  la forma cambia de signo; y controla un determinante, no el autovalor mínimo (muro W-det). En el corpus
  sólo aparece en la fase 67, sobre otro objeto.
- ARGUED: la versión de inercia (complemento de Schur de Haynsworth entre PAP y QA^{−1}Q) es la clase 4/6.

**5.5 Operadores integrales que reflejan un operador diferencial.** W. R. Casper, F. A. Grünbaum,
M. Yakimov, I. Zurrián, *Reflective prolate-spheroidal operators and the KP/KdV equations*, Proc. Natl.
Acad. Sci. 116 (2019), arXiv:1909.01448; *Reflective prolate-spheroidal operators and the adelic
Grassmannian*, Comm. Pure Appl. Math. 76 (2023), arXiv:2003.11616. Definición (CITED): T refleja a R si
T∘R(−z,−∂_z) = R(z,∂_z)∘T en un subespacio denso. Teorema 1: todo punto del Grassmanniano adélico de Wilson
da un operador integral que refleja un operador diferencial no constante de orden ≤ 2min(d₁,d₂).
Teorema 3: bajo una simetría, el operador de tipo Fourier limitado en tiempo y banda conmuta con un
operador diferencial de coeficientes racionales del mismo orden. Teorema 4: operador común a una familia
finita. Los ejemplos tienen orden 1, 3 y 6.
- Mecanismo: álgebra de Fourier de una función biespectral; fuente algebraica de la conmutación prolata.
  No es un mecanismo de signo: da autovectores y estructura de Sturm para operadores de concentración.
- Cotejo: CS0_COMMUTE_001 probó que no hay conmutante diferencial de orden ≤ 2 para el operador de la
  ventana con peine, y dejó OPEN el orden > 2. La noción de *reflexión* (más débil que conmutación) y los
  órdenes altos son precisamente ese residuo. ARGUED: el argumento de periodicidad por átomo de CS-0
  (cada δ_{log n} fuerza coeficientes periódicos) no depende del orden y probablemente también excluye la
  reflexión; no está escrito.
- Sin peso: la obstrucción de CS-0 vale para cΛ, a_P, Beurling (IDX), luego aunque existiera sería
  genérica en el peine. Clase 13 (Sturm) / 10.

**5.6 Procesos determinantales; transporte óptimo y entropía con estructura entera.** No se encontró ningún
enunciado con núcleo «restricción de un unitario aritmético» que no sea el de concentración ya registrado
(0 ≤ PQP ≤ 1, clase 10), ni identidades de transporte o entropía que usen el espaciado de los enteros
más allá de lo cotejado en IDX P33-11 y `ROUND_009_G3.md` §3. Búsqueda poco profunda en este punto; no
cuenta como exclusión.

---

## 6. Lista corta

Mecanismos sin marca sustantiva en el corpus, ordenados por número de características que reúnen. **Ninguno
reúne las cinco y ninguno pasa la puerta de cuatro puntos**: a todos les falta lo mismo, un signo que
dependa de los valores exactos de v_n (ninguno se rompe con peso ×2 por una razón de signo).

1. **Operador de transferencia de una aplicación de tipo Gauss en densidad crítica** (§1.5; Hedenmalm–
   Montes-Rodríguez; Canto-Martín–Hedenmalm–Montes-Rodríguez; series de Fourier hiperbólicas).
   Reúne: exactitud (umbral αβ = 1), espaciado igual + inversión de escala, no localidad, dimensión
   infinita; la operación positiva no es una convolución (esquiva P12 en la letra).
   Primer enunciado a transferir: el lema de que los iterados del operador de Perron–Frobenius de
   x ↦ −1/x mód 2 anulan en el límite toda función que aniquila al sistema {e^{iπnt}, e^{iπn/t}};
   su análogo sería un operador de transferencia sobre la ventana que entrelace la compresión del
   operador Σ v_n τ_{log n} con una aplicación expansiva del lado multiplicativo.
   Por qué puede fallar: es un teorema de unicidad, no de signo de una forma, y en densidad crítica no da
   cota de marco; no tiene peso (insensible a c = 2 y al borrado); la aplicación expansiva natural del lado
   multiplicativo conduce a un semigrupo de saltos, que es la clase 24 (sin densidad reversible).

2. **Criterio de la derivada de Serre con caso base de integralidad** (§2.2; Lee, Prop. 3.5, Cor. 3.6).
   Reúne: exactitud, ecuación funcional e integralidad en un mismo paso, sin holgura.
   Primer enunciado a transferir: sobre la realización theta de la función de un perfil, hallar un peso k
   para el que la derivada de Serre sea completamente positiva y aplicar el Cor. 3.6.
   Por qué puede fallar: da signo puntual en un eje, no semidefinición de un núcleo (Bochner en θ excluido,
   C-hom); no ve el producto de Euler (vale para modelos sin él, B6); el objeto de la fase no es una forma
   cuasimodular de nivel fijo.

3. **Reflexión, no conmutación, de un operador diferencial de orden > 2** (§5.5; Casper–Grünbaum–Yakimov–
   Zurrián, Teoremas 1, 3, 4). Reúne: tipo concentración, exactitud, dimensión creciente.
   Primer enunciado a transferir: extender el lema CS-0 a la identidad T∘R(−z,−∂_z) = R(z,∂_z)∘T con R de
   orden arbitrario; el resultado esperado es negativo y cerraría con prueba el residuo OPEN de
   CS0_COMMUTE_001.
   Por qué puede fallar como fuente de signo: aunque existiera R, daría estructura de autovectores, no
   signo, y sería genérico en el peine. Su valor es de cierre, no de construcción.

4. **Identidad de Borodin–Okounkov en intervalo finito** (§5.4; Basor–Chen). Reúne: tipo concentración,
   exactitud, dimensión creciente, pequeñez superexponencial del factor complementario.
   Primer enunciado a transferir: la identidad para el símbolo de la forma regularizado (sumando una
   constante que lo haga positivo), y seguir el factor complementario al retirar la regularización.
   Por qué puede fallar: es válida para todo símbolo factorizable (no lleva signo, B1); exige símbolo sin
   ceros; da un determinante (W-det), no el autovalor mínimo; retirar la regularización es el objetivo.

5. **Teoría local de Olsen para ℋ_w en una ventana de la recta crítica** (§5.2; Teoremas 1–4). Reúne: es de
   ventana, peso crítico, entrada de primos, no local por primo.
   Primer enunciado a transferir: el Teorema 2 con w_n = Λ(n)/log n como descripción exacta del espacio de
   valores de frontera en la ventana, para escribir el término aritmético como norma en un espacio de Hardy
   local.
   Por qué puede fallar: equivalencias hasta constantes (P5); depende sólo de cotas de Chebyshev del peso
   (genérico: sobrevive a c = 2, al borrado y a Beurling con la misma densidad).

Dicho llanamente: **nada de lo encontrado coincide con la especificación.** La característica (b) —
isometría sólo para los enteros verdaderos con Σ_{d|n}Λ(d) = log n dentro del paso de signo — no aparece
en ningún enunciado de positividad de la literatura consultada. Donde aparece el espaciado igual (§1.4,
§1.5, §5.2 Laca–Raeburn, Hedenmalm–Lindqvist–Seip) no hay peso; donde aparece el peso (§5.2 Olsen, Helson)
no hay exactitud ni estructura aditiva. Los dos objetos que juntan suma y producto en una sola relación
exacta son la relación (T5) de Laca–Raeburn y la reciprocidad de Vasyunin–Bettin–Conrey; ambos son libres
de Λ y ya están citados en el corpus.

## 7. Afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Enunciados y números de teorema de §§1–5 | CITED (versión arXiv; los marcados «sin número» sin verificar en primaria) |
| 2 | Tabla de cotejo §0 | NUMÉRICO (grep; no prueba novedad) |
| 3 | K(u) = √(xy)(|x−y|^{−1} + (x+y)^{−1}) con x = e^t, y = e^s | PROVED (identidad elemental) |
| 4 | Clasificación de cada ítem en las clases 1–25 y conducta bajo los tres falsificadores | ARGUED |
| 5 | El mecanismo E∘prolatas da cotas superiores del fondo y no cotas inferiores | ARGUED (sobre enunciados CITED) |
| 6 | El argumento de periodicidad de CS-0 se extiende a la reflexión y a todo orden | OPEN (ARGUED que es probable) |
| 7 | Ningún mecanismo encontrado tiene signo dependiente de los valores exactos del peso | ARGUED |
| 8 | Signo global | OPEN |
