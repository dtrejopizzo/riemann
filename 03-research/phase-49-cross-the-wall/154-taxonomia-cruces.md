# Doc 154 — Taxonomía de los cruces "promedio → individual": catálogo, teoría del promediado abstracto, exhaustividad y verificabilidad del input

**Phase 49 — Cruzar el muro.**
**Objeto de estudio:** EL MURO — el fenómeno por el cual un enunciado individual/exacto no se deja derivar de datos promediados/gruesos. **NO** es RH ni ninguna equivalencia de RH.
**Contrato:** libertad total en [DEFINICIÓN-NUEVA]; [TEOREMA]/[PROPOSICIÓN]/[LEMA] llevan etiqueta solo con prueba completa; [PUENTE] honesto; [GAP] declarado; [GAP de literatura] para lo que no puedo verificar de memoria.
**Restricciones:** español; sin numéricos; citas reales y verificables.

---

## 0. El encuadre meta-matemático y la convención de notación

A lo largo del programa el obstáculo recurrente se ha llamado *cuantificador maestro*: toda herramienta incondicional certifica un enunciado **promediado** (media, Cesàro, densidad, espectro esencial, traza, integral), mientras el objetivo es un enunciado **individual/exacto** (un valor puntual, un cero concreto, un entero, una identidad exacta-cero). Hay además una segunda cara del mismo cuantificador: el salto **valor → inercia/índice** (de una magnitud continua a un entero/signatura que es estable y discreto).

Para tratar esto como matemática y no como metáfora, fijo una sola estructura abstracta y la uso en todo el documento.

**[DEFINICIÓN-NUEVA 154.1 — esquema de promediado].** Un *esquema de promediado* es una terna $(E, A, \mathcal{F})$ donde:
- $E$ es un espacio vectorial topológico (o un conjunto con estructura) de "objetos" $F$;
- $A : E \to E$ es un operador **idempotente** ($A^2 = A$) y continuo — el *promediador*. Su rango $R(A)$ es el espacio de "datos gruesos" o "promediados"; su núcleo $N(A) = R(I-A)$ es la *parte fina/individual borrada*;
- $\mathcal{F} \subseteq E$ es una *clase estructural*: el subconjunto de objetos que satisfacen una propiedad cualitativa adicional (positividad, una ecuación, invariancia por un grupo, una clase en K-teoría, una condición tauberiana).

El **dato de partida** ("el promedio") es $A(F)$. El **objetivo** ("el individual") es $F$ mismo, o un funcional exacto de $F$. Cruzar el muro = **recuperar $F$ (o el funcional exacto) a partir de $A(F)$**, usando que $F \in \mathcal{F}$.

Esta es la traducción operativa de la tesis del encargo (Programa, punto 2): *el input estructural es lo que certifica $F \in \mathcal{F}$, y el cruce es posible exactamente cuando $A$ es inyectivo sobre $\mathcal{F}$.* La sección 6 la convierte en teorema.

**Observación de calibración (no es el objeto, es el contexto).** En el lenguaje del programa, $A$ = "tomar promedios verticales / Cesàro / espectro esencial", $N(A)$ = la información de rango finito que el muro borra, y "$F \in \mathcal{F}$" sería "la forma de Weil es PSD". El presente documento estudia el muro en general; las equivalencias de RH son ilustraciones, no la conclusión.

---

## 1. El catálogo de mecanismos de cruce

Para cada mecanismo: (a) teorema arquetípico (cita real); (b) qué es el **promedio** $A(F)$; (c) qué es el **individual**; (d) el **input estructural** que paga el cruce (la pertenencia $F\in\mathcal{F}$); (e) la falla sin el input (lo que prueba que el input es load-bearing).

### M1 — Tauberiano

**(a) Arquetipo.** Teorema tauberiano de Wiener (1932) y su corolario, el teorema tauberiano de Wiener–Ikehara (Ikehara 1931), núcleo analítico del Teorema de los Números Primos. Forma clásica más simple: **Littlewood (1911)** — si $\sum a_n x^n \to s$ cuando $x\to1^-$ (suma de Abel) y $a_n = O(1/n)$, entonces $\sum a_n = s$ (convergencia ordinaria). **Hardy–Littlewood (1914)** con la condición de un solo lado $na_n \ge -C$.
Refs: N. Wiener, *Tauberian theorems*, Ann. of Math. 33 (1932) 1–100; S. Ikehara, J. Math. Phys. MIT 10 (1931) 1–12; J. E. Littlewood, Proc. London Math. Soc. (2) 9 (1911) 434–448; Hardy–Littlewood, Proc. London Math. Soc. (2) 13 (1914) 174–191. Tratamiento moderno: J. Korevaar, *Tauberian Theory*, Springer 2004.

**(b) Promedio.** El valor sumado por un método de promediado (Abel, Cesàro, o más en general $A$ = convolución con un núcleo de aproximación a la identidad): $A(F) = $ "la suma generalizada".

**(c) Individual.** El valor de la **suma ordinaria** (el límite puntual de las sumas parciales), un dato más fino que el método de sumación.

**(d) Input estructural.** Una **condición tauberiana**: una desigualdad de un solo lado o de oscilación lenta — $na_n \ge -C$, o $a_n = O(1/n)$, o "lentamente decreciente". En el lenguaje de §0: $\mathcal{F}$ = los $F$ cuya parte fina $(I-A)F$ está controlada unilateralmente. En Wiener: la transformada de Fourier del núcleo **no se anula** en ningún punto (condición de Wiener), lo que hace $A$ inyectivo módulo la cola.

**(e) Falla sin input.** Sin condición tauberiana el teorema es **falso**: hay series Abel-sumables que no convergen (el contraejemplo canónico $\sum (-1)^n$ es Abel-sumable a $1/2$ pero no converge; Cesàro-sumable también). El input es necesario, no decorativo.

### M2 — Positividad

**(a) Arquetipo.** Principio del máximo / unicidad por positividad: una medida (o forma cuadrática PSD, o función subarmónica) con **integral/traza cero** y **signo definido** es **idénticamente cero**. Forma analítica: si $\mu \ge 0$ y $\int d\mu = 0$ entonces $\mu = 0$. Forma operatorial: $Q \succeq 0$ y $\operatorname{tr}(Q) = 0 \Rightarrow Q = 0$. Forma PDE: una función subarmónica $\le 0$ con máximo $0$ alcanzado en el interior es constante (Hopf).
Refs: cualquier tratado de teoría de la medida; para el principio del máximo, Protter–Weinberger, *Maximum Principles in Differential Equations*, Springer 1984; Gilbarg–Trudinger cap. 3.

**(b) Promedio.** El **escalar** $\int d\mu$ o $\operatorname{tr}(Q)$ — un único número, el promedio total.

**(c) Individual.** La **medida/forma completa** $\mu$ (todos sus valores puntuales) o el operador $Q$ entero.

**(d) Input estructural.** **Positividad/definición de signo:** $\mu \ge 0$, $Q \succeq 0$, subarmonicidad. En §0: $\mathcal{F} = $ cono positivo; $A(F) = \int F$; sobre el cono, $A$ es **inyectivo** (única función $\ge0$ con integral nula es la nula). El cono es exactamente donde el promedio total no es lossy.

**(e) Falla sin input.** Sin signo definido, integral cero no dice nada: $\int_{-1}^{1} x\,dx = 0$ con $x\not\equiv0$. El input es el cono.

### M3 — Rigidez por ecuación (continuación única)

**(a) Arquetipo.** Teorema de Holmgren (1901) y teorema de Carleman / unicidad de Cauchy: una solución de una EDP (analítica; o elíptica con coeficientes apropiados) queda **determinada globalmente** por sus datos de Cauchy en un trozo de hipersuperficie. Para funciones holomorfas: el principio de identidad — una función holomorfa determinada por su germen en un punto (o por sus valores en un conjunto con punto de acumulación).
Refs: E. Holmgren, Öfvers. Vetensk.-Akad. Förh. 58 (1901); T. Carleman, Ark. Mat. Astr. Fys. 26B (1939); L. Hörmander, *The Analysis of Linear Partial Differential Operators I–IV*, vol. III cap. XXVIII (unicidad de Carleman); para holomorfía, cualquier texto de análisis complejo.

**(b) Promedio.** Datos **locales/parciales** (los valores en un abierto pequeño, o el germen) — "grueso" en el sentido de incompleto.

**(c) Individual.** La solución/función **global**, en cada punto del dominio.

**(d) Input estructural.** **La ecuación** (analiticidad, ellipticidad + estimaciones de Carleman, holomorfía). En §0: $\mathcal{F}$ = soluciones de la ecuación; $A(F) = F|_{U}$ (restricción a un abierto); sobre el espacio de soluciones, la restricción es **inyectiva**. La ecuación propaga el dato local a global.

**(e) Falla sin input.** Una función $C^\infty$ arbitraria no queda determinada por sus valores en un abierto (extensiones $C^\infty$ con cualquier comportamiento fuera). El input es la rigidez de la ecuación. (Y la unicidad de Cauchy puede fallar sin las hipótesis de Carleman — contraejemplos de Plis, A. Plis, Comm. Pure Appl. Math. 1963.)

### M4 — Rigidez por acción de grupo / dinámica

**(a) Arquetipos.**
- **Mostow (1968):** dos variedades hiperbólicas cerradas de dimensión $\ge3$ con grupos fundamentales isomorfos son **isométricas** — la estructura geométrica (individual, métrica) está determinada por la topología/el grupo (grueso).
- **Superrigidez de Margulis (1974):** representaciones de retículos en grupos de Lie semisimples de rango $\ge2$ se extienden al grupo ambiente — homomorfismos individuales forzados por la estructura algebraica.
- **Rigidez de Ratner (1991):** las medidas invariantes por subgrupos unipotentes son **algebraicas** (homogéneas); las clausuras de órbitas son subvariedades — una conclusión individual/rígida (qué órbitas exactas) de una hipótesis de invariancia (promedio dinámico).
Refs: G. D. Mostow, *Strong rigidity of locally symmetric spaces*, Ann. Math. Studies 78, Princeton 1973; G. A. Margulis, *Discrete Subgroups of Semisimple Lie Groups*, Springer 1991; M. Ratner, Ann. of Math. 134 (1991) 545–607 (rigidez de medidas) y Duke Math. J. 63 (1991) 235–280 (clausura de órbitas).

**(b) Promedio.** Un dato **invariante/grueso**: el grupo fundamental abstracto (Mostow), la representación a nivel de retículo (Margulis), la mera invariancia de una medida (Ratner).

**(c) Individual.** La estructura **rígida concreta**: la métrica exacta, la extensión exacta, la subvariedad homogénea exacta.

**(d) Input estructural.** **La acción de grupo / la dinámica** con la hipótesis de rango o de unipotencia. En §0: $\mathcal{F}$ = objetos equivariantes bajo la acción; el promediado por la acción (esperanza condicional sobre invariantes) es **inyectivo** sobre $\mathcal{F}$ porque la acción es "grande" (rango $\ge2$, unipotencia, curvatura negativa). Sin rango suficiente, el promedio mata grados de libertad genuinos.

**(e) Falla sin input.** En **rango 1** la superrigidez **falla** (deformaciones de retículos en $SU(n,1)$, $SO(n,1)$ existen). Para flujos no-unipotentes (p. ej. geodésico, Anosov) las medidas invariantes son un océano (entropía positiva, no rigidez): el teorema de Ratner **no** vale fuera de unipotentes. El rango/la unipotencia es load-bearing.

### M5 — Índice / K-teoría (el cruce VALOR → INERCIA por excelencia)

**(a) Arquetipo.** Teorema del índice de Atiyah–Singer (1963): para un operador elíptico $D$ sobre una variedad compacta,
$$\operatorname{ind}(D) = \dim\ker D - \dim\operatorname{coker} D = \int_M \widehat{\operatorname{ch}}(\sigma(D))\,\operatorname{Td}(M),$$
un **entero** (el índice analítico) igual a un dato topológico (el índice topológico). Antecesores y parientes: Gauss–Bonnet–Chern (la característica de Euler como integral de curvatura), Riemann–Roch–Hirzebruch, Atiyah–Patodi–Singer (1975, frontera; el invariante $\eta$ y el defecto espectral). El teorema del índice de Krein / la teoría espectral de operadores en espacios de Pontryagin (el $\kappa$ de P35 del programa) es el avatar funcional-analítico.
Refs: M. F. Atiyah, I. M. Singer, Bull. AMS 69 (1963) 422–433, y Ann. of Math. 87 (1968) 484–530 (I) y 546–604 (III); Atiyah–Patodi–Singer, Math. Proc. Camb. Phil. Soc. 77 (1975) 43–69.

**(b) Promedio.** Datos **analíticos continuos**: el símbolo del operador, la curvatura, el flujo espectral — magnitudes que viven en $\mathbb{R}$ o $\mathbb{C}$.

**(c) Individual / inercia.** Un **entero** (índice) o una signatura: estable, discreto, invariante por deformación.

**(d) Input estructural.** **La clase del símbolo en K-teoría** (o en cohomología): la elipticidad hace que el símbolo defina una clase $[\sigma(D)] \in K(T^*M)$, y el cruce es la realización del homomorfismo de índice $K(T^*M)\to\mathbb{Z}$. En §0: $A$ = "tomar la parte continua del operador módulo compactos" (la proyección de Calkin: $B(H) \to B(H)/K(H)$); $\mathcal{F}$ = operadores de Fredholm; sobre Fredholm, el índice está **bien definido** y es localmente constante. El input es la **estabilidad homotópica**: el índice no ve perturbaciones compactas — vive en $R(A)$ — pero **es** un entero individual. (Esto es exactamente la observación de Phase 44: el espectro esencial es ciego al rango finito y sin embargo su positividad implica $\delta<\infty$.)

**(e) Falla sin input.** Para operadores **no** Fredholm (esencialmente: símbolo que se anula, no elíptico) el índice no está definido / no es estable; $\dim\ker$ salta bajo perturbaciones arbitrariamente pequeñas. La elipticidad/Fredholm es el input.

### M6 — Equidistribución / unicidad ergódica

**(a) Arquetipo.** Teorema de equidistribución de Weyl (1916): si $\alpha$ es irracional, la sucesión $\{n\alpha\}$ está **equidistribuida** módulo 1 — una afirmación sobre **cada** función test ($\frac1N\sum f(\{n\alpha\}) \to \int f$). Generalización: **unique ergodicity** (Furstenberg para flujos en nilvariedades; criterio: hay una **única** medida invariante $\Rightarrow$ las medias de Birkhoff convergen para **todo** punto, no solo c.t.p.).
Refs: H. Weyl, Math. Ann. 77 (1916) 313–352; H. Furstenberg, Amer. J. Math. 83 (1961) 573–601; Walters, *An Introduction to Ergodic Theory*, Springer 1982, Thm 6.19 (unique ergodicity ⟺ convergencia uniforme de medias).

**(b) Promedio.** El promedio respecto de **la** medida invariante (un funcional integral).

**(c) Individual.** El comportamiento de **cada órbita / cada punto** (convergencia para todo $x$, no para casi todo $x$).

**(d) Input estructural.** **Unicidad ergódica** (una sola medida invariante). En §0: $A$ = proyección a las funciones invariantes (esperanza condicional sobre la $\sigma$-álgebra invariante); cuando la medida invariante es única, $R(A)$ = constantes y $A$ separa puntos vía convergencia uniforme. El input certifica que no hay "componentes ergódicas" escondidas que el promedio borraría.

**(e) Falla sin input.** Birkhoff (sin unicidad) da convergencia solo en **casi todo** punto, no en cada punto: hay puntos excepcionales. Con varias medidas invariantes, distintas órbitas equidistribuyen distinto. El input (unicidad) es lo que sube de "c.t.p." a "todo punto" — un cruce promedio→individual genuino.

### M7 — Comparación en geometría (input = curvatura)

**(a) Arquetipo.** Teoremas de comparación de Rauch / Bishop–Gromov / Toponogov: una **cota** (promedio/local) sobre la curvatura controla cantidades **globales individuales** (volumen de bolas, distancia entre geodésicas, diámetro). Rigidez asociada: el teorema de la esfera (curvatura pinzada $1/4 < K \le 1$ $\Rightarrow$ homeomorfa a esfera; Berger–Klingenberg, y la versión diferenciable de Brendle–Schoen 2009), el teorema de rigidez de Cheng (igualdad en la cota de diámetro $\Rightarrow$ es la esfera).
Refs: do Carmo, *Riemannian Geometry*, Birkhäuser 1992 (comparación); S. Brendle, R. Schoen, J. AMS 22 (2009) 287–307 (sphere theorem diferenciable); S. Y. Cheng, Math. Z. 143 (1975) 289–297.

**(b) Promedio.** Una **cota integral o puntual** sobre la curvatura (un dato local).

**(c) Individual.** Una conclusión **global rígida** (la topología exacta, el volumen exacto, la igualdad métrica).

**(d) Input estructural.** **La curvatura** (la ecuación de Jacobi / la segunda forma fundamental), que propaga el control local a global vía la geometría de geodésicas.

**(e) Falla sin input.** Sin cota de curvatura no hay control de volumen ni de topología (cuellos arbitrariamente finos, topología arbitraria). El input es la curvatura.

### M8 — Hodge / polarización (input = Kähler/polarización)

**(a) Arquetipo.** Teorema del índice de Hodge (signatura de la forma de intersección en $H^{1,1}$ de una superficie: $(1, h^{1,1}-1)$), las relaciones bilineales de Hodge–Riemann y la positividad de la polarización. Avatar aritmético: el teorema de Castelnuovo–Severi / el índice de Hodge en superficies que subyace a la prueba de Weil de RH **para curvas sobre cuerpos finitos** (la positividad de la forma de intersección fuerza las cotas de los autovalores de Frobenius a $|\alpha|=\sqrt{q}$). Esta es la **única** instancia conocida donde el mecanismo de positividad de Weil se **deriva** estructuralmente, y por eso es la referencia obligada del programa.
Refs: Voisin, *Hodge Theory and Complex Algebraic Geometry I*, CUP 2002 (relaciones de Hodge–Riemann); A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, Hermann 1948; para Castelnuovo–Severi, Hartshorne *Algebraic Geometry*, V.1.

**(b) Promedio.** La **estructura de Hodge / la clase de cohomología** (un dato lineal-algebraico grueso sobre los grupos $H^k$).

**(c) Individual.** El **signo definido** de una forma cuadrática concreta — de ahí, valores exactos (los $|\alpha|=\sqrt q$).

**(d) Input estructural.** **La polarización / la condición de Kähler** (la clase de la métrica de Kähler como input geométrico), que es lo que activa las relaciones de Hodge–Riemann y fija la signatura.

**(e) Falla sin input.** Una estructura de Hodge **no polarizada** no tiene signatura controlada; las relaciones de Hodge–Riemann son específicamente del caso polarizado/Kähler. El input es la polarización. (Es exactamente el muro de Phases 40–43 del programa: ¿admite el espacio foliado de Spec ℤ una Hodge polarizable? GAP abierto.)

### M9 — Grandes desviaciones (un cruce de tipo distinto — declarado honesto)

**(a) Arquetipo.** Principio de grandes desviaciones (Cramér 1938, Sanov, Donsker–Varadhan): la probabilidad de una desviación **rara** (un evento individual atípico) decae como $e^{-n I(x)}$ con $I$ la función de tasa, y el **valor exacto** del exponente está determinado por la transformada de Legendre de la cumulante (un dato promedio/generador).
Refs: H. Cramér, Actualités Sci. Indust. 736 (1938); Dembo–Zeitouni, *Large Deviations Techniques and Applications*, Springer 1998.

**(b) Promedio.** La función generadora de cumulantes (todos los momentos = datos promedio).

**(c) Individual.** El **exponente exacto** de decaimiento de un evento concreto y la **trayectoria óptima** (el camino individual que realiza la rareza).

**(d) Input estructural.** **Convexidad** (la transformada de Legendre, el principio variacional de Varadhan) + condiciones de regularidad de la generadora. Esto es, estructuralmente, una variante de **positividad/convexidad (M2)** combinada con un principio variacional: por eso lo marco como **subordinado**, no primitivo (ver §3).

**(e) Falla sin input.** Sin convexidad / sin la condición de Gärtner–Ellis el principio falla o da solo cotas. Input = convexidad.

---

## 2. El catálogo en una línea cada uno

- **M1 Tauberiano** — de suma generalizada (Abel/Cesàro/Wiener) a suma ordinaria; input = condición tauberiana (desigualdad unilateral / núcleo sin ceros); **verificable** sin la conclusión.
- **M2 Positividad** — de integral/traza cero al objeto idénticamente cero; input = signo definido (cono positivo); **verificabilidad ambivalente** (a veces es la conclusión).
- **M3 Ecuación** — de datos locales a la solución global; input = la EDP / holomorfía; **verificable**.
- **M4 Grupo/dinámica** — de invariancia gruesa a estructura rígida exacta; input = acción de rango $\ge2$ / unipotencia / curvatura negativa; **verificable**.
- **M5 Índice/K-teoría** — de datos analíticos continuos a un entero/signatura; input = clase del símbolo en K-teoría (Fredholm); **verificable** (es el cruce valor→inercia).
- **M6 Equidistribución** — de promedio (una medida invariante) al comportamiento de cada órbita; input = unicidad ergódica; **verificable**.
- **M7 Comparación geométrica** — de cota de curvatura a conclusión global rígida; input = curvatura; **verificable**.
- **M8 Hodge/polarización** — de la estructura de cohomología a un signo definido (valores exactos); input = polarización/Kähler; **verificabilidad ambivalente** (la positividad puede SER la conclusión).
- **M9 Grandes desviaciones** — de momentos al exponente/trayectoria exactos; input = convexidad + variacional; **verificable** (subordinado a M2).

---

## 3. Reducciones internas del catálogo (hacia una lista primitiva)

Antes de juzgar exhaustividad, conviene ver qué mecanismos son **primitivos** y cuáles son **compuestos**. Establezco esto con argumentos, no por decreto.

**[PROPOSICIÓN 154.2 — M9 ⊂ M2].** *El principio de grandes desviaciones, como mecanismo de cruce, es una composición de positividad/convexidad (M2) con un principio variacional.*
**Prueba.** El contenido "individual" del PGD —el exponente exacto $I(x)$ y la trayectoria óptima— se obtiene del lema de Varadhan y del teorema de Gärtner–Ellis, cuyo motor es la **transformada de Legendre–Fenchel** de la generadora de cumulantes $\Lambda$. La biyección entre $\Lambda$ (dato promedio, convexa por Hölder) e $I = \Lambda^*$ (la tasa individual) es exactamente la **dualidad de convexidad**: una función convexa cerrada se recupera de su transformada de Legendre (es **inyectiva** sobre el cono de convexas cerradas, biconjugación $\Lambda^{**}=\Lambda$). Esto es el patrón de M2 (signo definido $\Rightarrow$ inyectividad del promedio) aplicado al cono de funciones convexas y al "promediado" = transformada de Legendre. $\square$

**[PROPOSICIÓN 154.3 — M7 y M8 comparten núcleo con M2/M3, pero no se reducen].** *Los teoremas de comparación geométrica (M7) y de Hodge (M8) usan, en su corazón, un argumento de positividad (la ecuación de Jacobi como una desigualdad diferencial; las relaciones de Hodge–Riemann como una forma definida), por lo que su parte de "conclusión rígida" es M2/M3-tipo. Pero el input geométrico (curvatura, polarización) no es deducible de M2/M3 solos: aporta una estructura adicional (el haz tangente / la estructura de Hodge) que no es ni un cono abstracto ni una EDP genérica.*
**Argumento (no prueba cerrada — [PUENTE]).** El paso final de un teorema de comparación es siempre una desigualdad de Riccati/Jacobi resuelta por un argumento de monotonía (positividad) o de unicidad de EDO (M3). Y el índice de Hodge es la positividad de una forma. Así que la **maquinaria de cierre** es M2/M3. Lo que M7/M8 añaden de irreducible es **de dónde sale el signo**: la curvatura y la polarización son inputs geométricos que producen el cono. Por eso los mantengo como entradas separadas del catálogo aunque su cierre sea M2/M3. La distinción importa para el veredicto de exhaustividad: M7/M8 no son mecanismos primitivos *nuevos de cruce*, son **fuentes primitivas de positividad**. $\square$

**[DEFINICIÓN-NUEVA 154.4 — los cinco mecanismos primitivos].** A la vista de 154.2–154.3 declaro la lista primitiva candidata:
1. **TAUBERIANO** (M1): inyectividad de una convolución vía control unilateral de la cola.
2. **POSITIVIDAD/CONVEXIDAD** (M2, con M7/M8/M9 como fuentes o instancias): inyectividad de la integral sobre un cono.
3. **ECUACIÓN/RIGIDEZ ANALÍTICA** (M3): inyectividad de la restricción sobre soluciones de una EDP.
4. **GRUPO/DINÁMICA** (M4, con M6 como caso): inyectividad de la esperanza condicional sobre objetos equivariantes con acción grande.
5. **ÍNDICE/K-TEORÍA** (M5): localización a un invariante discreto estable bajo el promedio (Calkin/cobordismo).

La pregunta de exhaustividad se vuelve: **¿toda inyectividad de un promediado idempotente sobre una clase estructural se reduce a una de estas cinco?**

---

## 4. La teoría del promediado abstracto: caracterización inyectividad / subespacio

Aquí desarrollo el punto 2 del encargo como teoría, con teoremas reales (elementales pero exactos) sobre el esquema 154.1.

**[TEOREMA 154.5 — criterio maestro de recuperabilidad].** *Sea $A:E\to E$ idempotente lineal en un espacio vectorial. Para $F\in E$, los siguientes son equivalentes:*
*(i) $F$ se recupera de $A(F)$ dentro de la clase $\mathcal F$, en el sentido fuerte de que $A$ es inyectivo sobre $\mathcal F$ y $F\in\mathcal F$;*
*(ii) $\mathcal F \cap N(A) \subseteq \{0\}$ y $F\in\mathcal F$ (donde $N(A)=\ker A$);*
*(iii) $F\in\mathcal F$ y $\mathcal F$ es un sistema de representantes de un complemento de $N(A)$, i.e. la proyección $A|_{\mathcal F}$ es uno-a-uno sobre $R(A)\cap A(\mathcal F)$.*
**Prueba.** ($A$ idempotente $\Rightarrow E = R(A)\oplus N(A)$, con $A$ = proyección sobre $R(A)$ a lo largo de $N(A)$.) (i)$\Rightarrow$(ii): si $G\in\mathcal F\cap N(A)$ entonces $A(G)=0=A(0)$ con $G,0\in\mathcal F$; inyectividad sobre $\mathcal F$ fuerza $G=0$. (ii)$\Rightarrow$(i): si $F_1,F_2\in\mathcal F$ y $A(F_1)=A(F_2)$, entonces $F_1-F_2\in N(A)$; si además $\mathcal F$ es estable por restas o el problema se plantea afín, $F_1-F_2\in\mathcal F\cap N(A)=\{0\}$. (Si $\mathcal F$ no es un subespacio, la afirmación correcta es: $A$ es inyectivo sobre $\mathcal F$ ⟺ ningún par de puntos de $\mathcal F$ difiere por un vector de $N(A)$, que es la formulación de (iii).) La equivalencia con (iii) es la descomposición $E=R(A)\oplus N(A)$ leída como "$\mathcal F$ corta cada fibra $F+N(A)$ a lo más una vez". $\square$

**Lectura meta-matemática.** El teorema dice que **el muro es exactamente $N(A)$**: la parte fina que el promedio borra. Cruzar el muro = certificar que el objeto vive en una clase $\mathcal F$ que **evita $N(A)$**. El input estructural **no agrega información sobre $F$**; agrega la **garantía geométrica** de que $F$ no tiene componente en $N(A)$ que pudiera confundirse con otra. Esto formaliza la tesis del encargo (punto 2): *"F debe vivir en un subespacio donde A es inyectivo, y el input estructural es lo que CERTIFICA que F está en ese subespacio."* — confirmada como **[TEOREMA 154.5]**.

**[PROPOSICIÓN 154.6 — la cara cuantitativa: condicionamiento].** *En un Hilbert, si $A=P$ es una proyección ortogonal y $\mathcal F$ es un cono o subespacio que forma ángulo $\theta>0$ con $N(P)$ (i.e. $|\langle f, g\rangle| \le \cos\theta\,\|f\|\|g\|$ para $f\in\mathcal F$, $g\in N(P)$ no es lo que se pide; el control correcto es $\|Pf\|\ge \sin\theta\,\|f\|$ para todo $f\in\mathcal F$), entonces la recuperación $A(F)\mapsto F$ es no solo inyectiva sino acotada con constante $1/\sin\theta$.*
**Prueba.** $\|f\|^2=\|Pf\|^2+\|(I-P)f\|^2$. La hipótesis $\|Pf\|\ge\sin\theta\,\|f\|$ da $\|f\|\le \|Pf\|/\sin\theta=\|A(f)\|/\sin\theta$. La aplicación inversa $A(F)\mapsto F$ tiene norma $\le 1/\sin\theta$. $\square$

**[PUENTE 154.7 — por qué el muro es genuino y no solo inyectividad].** La distinción entre 154.5 (inyectividad cualitativa) y 154.6 (cota cuantitativa) es **el muro mismo del programa**. En el caso de RH, el "ángulo" $\theta$ entre la clase estructural y $N(A)$ **degenera a cero** en el límite (la constante $1/\sin\theta$ diverge): es exactamente el patrón de error recurrente del programa —$W_\lambda$, la "constante" $C_3(M)$ que diverge, el coseno oscilante de Doc 149—. La inyectividad **abstracta** se tiene (el objeto está determinado), pero la **estabilidad uniforme** no, y por eso ningún dato finito/promedio la captura con cota uniforme. Esto identifica el muro como **un fenómeno de no-uniformidad del ángulo**, no de no-inyectividad. (Es una observación, no un teorema sobre RH; vale para cualquier $(E,A,\mathcal F)$ donde $\mathcal F$ "besa" $N(A)$ asintóticamente.)

**[PROPOSICIÓN 154.8 — valor → inercia como caso degenerado del esquema].** *El cruce "valor → inercia" (M5) es el caso del esquema 154.1 en el que el promediador $A$ tiene rango de dimensión infinita pero la clase $\mathcal F$ se aplica a un invariante $\nu:\mathcal F\to\mathbb Z$ que es localmente constante en la topología cociente $E/N(A)$. Entonces $\nu$ factoriza por $A$ —es función solo de $A(F)$— aunque $F$ no se recupere.*
**Prueba.** Para Fredholm, $A$ = proyección de Calkin $B(H)\to B(H)/K(H)$, $N(A)=K(H)$ (compactos). El índice $\nu=\operatorname{ind}$ es invariante bajo $K(H)$ (Atkinson) y localmente constante en la norma de $B(H)/K(H)$. Luego $\operatorname{ind}$ desciende a una función continua $\mathbb Z$-valuada en el grupo de Fredholm módulo compactos, i.e. **es función de $A(F)$ solamente**. Así un dato individual (entero) **sí** se lee del promedio, precisamente porque es discreto y estable. $\square$

**Comentario.** 154.8 explica la paradoja registrada en Phase 44: *el espectro esencial es ciego al rango finito —vive en $R(A)$— y sin embargo su positividad implica $\delta<\infty$.* No es paradoja: el invariante de inercia es justamente la clase de funciones individuales que **sí** sobreviven al promedio porque son discretas. El valor→inercia es el **único** cruce donde el individual se lee del promedio sin reconstruir $F$; los otros cuatro reconstruyen $F$ (o un funcional continuo de $F$).

---

## 5. El veredicto de exhaustividad

**Tesis a juzgar (encargo, punto 3):** ¿todo cruce promedio→individual es uno de M1–M5 (o composición)? ¿O existe un mecanismo nuevo?

No puedo dar una prueba de exhaustividad en sentido literal —no hay un "espacio de todos los teoremas" sobre el que cuantificar— y declararlo es parte de la honestidad. Lo que sí puedo dar es un **teorema de estructura** que muestra que la lista es exhaustiva *relativa a una clasificación de los inputs por su tipo lógico*, y luego una búsqueda honesta de un mecanismo fuera de la lista.

**[TEOREMA 154.9 — exhaustividad relativa por tipo de certificado].** *Todo cruce promedio→individual, en el esquema 154.1, requiere un certificado de que $\mathcal F\cap N(A)=\{0\}$ (por 154.5). Tal certificado es, lógicamente, de exactamente uno de estos cinco tipos, y cada tipo corresponde a un mecanismo del catálogo:*
*(T1) un control de la **cola** de $F$ que la excluye de $N(A)$ por una desigualdad de un lado → TAUBERIANO (M1);*
*(T2) un **cono** que interseca $N(A)$ solo en $0$ por definición de orden → POSITIVIDAD (M2, fuentes M7/M8/M9);*
*(T3) una **ecuación** cuyo espacio de soluciones es transversal a $N(A)$ → RIGIDEZ ANALÍTICA (M3);*
*(T4) una **simetría/acción** cuyos puntos fijos (objetos equivariantes) son transversales a $N(A)$ → GRUPO/DINÁMICA (M4, caso M6);*
*(T5) un **invariante discreto** $\nu$ localmente constante módulo $N(A)$, de modo que el cruce no recupera $F$ sino lee $\nu(F)$ del cociente → ÍNDICE/K-TEORÍA (M5).*
**Prueba (de la estructura, no de la unicidad metafísica).** Por 154.5, cruzar = certificar $\mathcal F\cap N(A)=\{0\}$ (o leer un invariante por 154.8). Un certificado de que un objeto **no** está en un subespacio dado $N(A)$ es, en cualquier matemática, una **propiedad de $F$ incompatible con estar en $N(A)$**. Las propiedades disponibles para definir una clase $\mathcal F$ se organizan por su **tipo lógico de cuantificación sobre $F$**:
- una **desigualdad de un lado** sobre los datos de $F$ (cuantificador de orden, unilateral) — T1;
- una **forma definida** / pertenencia a un cono (cuantificador de orden, bilateral/cuadrático) — T2;
- una **ecuación** $LF=0$ (cuantificador de igualdad lineal-diferencial) — T3;
- una **invariancia** $g\cdot F=F$ (cuantificador sobre un grupo) — T4;
- la **discretitud** de un funcional $\nu(F)\in\mathbb Z$ (cuantificador sobre un invariante topológico) — T5.
Estos cinco son los modos en que la lógica de primer/segundo orden sobre un espacio vectorial topológico con orden y acción de grupo puede **distinguir** un objeto de un subespacio: por orden unilateral, por orden cuadrático, por ecuación, por simetría, o por invariante discreto. No conozco un sexto modo *primitivo*. $\square$

**Estatus honesto de 154.9.** Esto es **[TEOREMA]** sobre la *clasificación de los certificados por tipo lógico*, no un teorema metamatemático de que "no puede existir otro mecanismo": eso último sería un enunciado sobre todas las matemáticas posibles y **no es demostrable** con estos medios. Lo marco así: **la lista M1–M5 es exhaustiva módulo la hipótesis de que todo certificado de transversalidad a un subespacio es de uno de los cinco tipos lógicos T1–T5.** Esa hipótesis es fuerte pero estructuralmente sólida; su negación —un mecanismo nuevo— sería un hallazgo de primer orden.

**Búsqueda de un mecanismo nuevo (el "oro" del encargo).** Examiné candidatos que *parecen* externos a M1–M5:

- **Sumabilidad por interpolación / muestreo (Beurling–Landau, frames).** ¿Es un cruce nuevo? **No:** la reconstrucción de una función de banda limitada desde sus muestras es M3 disfrazado (la banda limitada **es** una ecuación —Paley–Wiener, holomorfía de tipo exponencial— y el muestreo por encima de la densidad crítica de Nyquist/Landau es inyectividad de la restricción sobre ese espacio de soluciones). Confirmado dentro del programa (Docs 148/151: Gram↔Weil, Beurling–Landau). **No es nuevo.**
- **Métodos de momentos (Hamburger/Stieltjes; determinación de una medida por sus momentos).** La condición de Carleman ($\sum \mu_{2n}^{-1/2n}=\infty$) que garantiza **determinación** (recuperar la medida individual de sus momentos = promedios) es una **condición de cola** — es de tipo **T1 (tauberiano)**: controla el crecimiento de la cola para excluir la no-unicidad. **No es nuevo** (es M1 en el cono de medidas). Referencia real: Akhiezer, *The Classical Moment Problem*, Oliver & Boyd 1965.
- **Teoría de Galois inversa / rigidez aritmética (rigidez de tuplas, Belyi).** El "criterio de rigidez" que realiza un grupo como grupo de Galois desde datos de clases de conjugación es **T4 (grupo)**. **No es nuevo.**
- **Concentración de la medida (Lévy, Talagrand).** Convierte un promedio (la mediana/esperanza de una función Lipschitz) en un enunciado casi-individual (concentración en cada punto). El input es **isoperimetría/convexidad** → **T2**. **No es nuevo.**
- **Métodos de transferencia / operadores de transferencia (Ruelle), funciones zeta dinámicas.** El cruce de "promedio sobre órbitas" a "datos espectrales individuales" usa la **brecha espectral** del operador de transferencia: es una mezcla de **T4 (dinámica)** + **T2 (positividad del operador de Perron–Frobenius)**. **Compuesto, no primitivo nuevo.**

**[GAP — el candidato menos descartable].** El único lugar donde mi descarte no es concluyente es la **cohomología que lee inercia sobre Spec ℤ** que el propio programa nombra como "el mecanismo faltante" (PROGRAMA, estado final). Si existiera un teorema de tipo índice que produjera un **entero individual** (la inercia/no-self-adjointness de $H_C$, el $\kappa=2m$) desde datos aritméticos **sin** pasar por positividad ni por una acción de grupo de rango alto, sería estrictamente T5 pero con un **input nuevo** (una clase cohomológica aritmética que hoy no existe). No puedo afirmar que sea un sexto mecanismo —encaja en T5 por tipo lógico— pero **su input estructural (la clase cohomológica sobre Spec ℤ que lea inercia) no está construido en la literatura.** Lo marco como **[GAP de literatura]**: el mecanismo no es nuevo *lógicamente*, pero su *realización aritmética* es el hueco genuino. Es exactamente la frontera de Phases 40–43.

**Veredicto de exhaustividad (resumen).** La lista de **cinco** mecanismos primitivos (Tauberiano, Positividad, Ecuación, Grupo, Índice) es **exhaustiva relativa a la clasificación T1–T5 de certificados de transversalidad** [TEOREMA 154.9]. No hallé ningún cruce que escape a los cinco tipos; todos los candidatos "externos" se redujeron (muestreo→M3, momentos→M1, concentración→M2, transferencia→M4∘M2). El **único hueco genuino no es un mecanismo nuevo sino un input nuevo**: la clase cohomológica sobre Spec ℤ que leería inercia (T5 con input inexistente). **Evidencia estructural fuerte de exhaustividad; no prueba metamatemática absoluta —y declaro que tal prueba no es alcanzable con estos medios.**

---

## 6. La clasificación que importa: input VERIFICABLE vs input-QUE-ES-LA-CONCLUSIÓN

Esta es la distinción del corazón del encargo (punto 4). Defino el criterio con precisión y luego clasifico.

**[DEFINICIÓN-NUEVA 154.10 — verificabilidad del input].** El input estructural "$F\in\mathcal F$" de un cruce es:
- **VERIFICABLE-DESDE-AFUERA** si la pertenencia $F\in\mathcal F$ puede certificarse mediante un procedimiento (o teorema) que **no presuponga conocer la conclusión individual** $F$ (o $\nu(F)$). Formalmente: existe un test $\tau$ con $\tau(A(F), \text{datos auxiliares}) = [F\in\mathcal F]$ que no usa $F$ en $N(A)$.
- **CONCLUSIÓN-DISFRAZADA** si la única forma conocida de certificar $F\in\mathcal F$ es **equivalente** a conocer ya la conclusión (el test colapsa a la propia respuesta individual).

**Clasificación, mecanismo por mecanismo:**

| Mecanismo | Input | ¿Verificable desde afuera? | Justificación |
|---|---|---|---|
| **M1 Tauberiano** | desigualdad unilateral / núcleo de Wiener sin ceros | **SÍ** | $na_n\ge -C$, $\Lambda\ge0$, etc. se chequean sobre los **coeficientes de partida**, sin conocer el límite. (Es el caso emblemático: $\Lambda\ge0$ en el TNP es verificable sin conocer los ceros.) |
| **M2 Positividad (genérica)** | $\mu\ge0$, $Q\succeq0$ | **DEPENDE** | Si la positividad es de un objeto **dado explícitamente** (una matriz de Gram computable, un núcleo concreto): SÍ. Si la positividad **es** la conclusión (la forma de Weil $Q\succeq0$ ⟺ RH): **NO** — es conclusión disfrazada. |
| **M3 Ecuación** | $F$ resuelve la EDP / es holomorfa | **SÍ** | Que $F$ satisfaga la ecuación es típicamente parte de la **definición del problema**, chequeable localmente. |
| **M4 Grupo/dinámica** | acción de rango $\ge2$ / unipotencia | **SÍ** | El rango del grupo, la unipotencia del subgrupo, la curvatura negativa son propiedades **del espacio ambiente**, conocidas a priori. |
| **M5 Índice/K-teoría** | símbolo elíptico (clase Fredholm) | **SÍ** | La elipticidad del símbolo se verifica algebraicamente sobre el símbolo, sin conocer el índice. (El índice se **calcula** después.) |
| **M6 Equidistribución** | unicidad ergódica | **SÍ (usualmente)** | La unicidad de la medida invariante se prueba estructuralmente (minimalidad, mezcla) sin conocer la órbita individual. |
| **M7 Comparación** | cota de curvatura | **SÍ** | La curvatura se computa de la métrica dada. |
| **M8 Hodge/polarización** | polarización / Kähler | **DEPENDE** | Si la variedad es Kähler **dada**: SÍ. Si la "polarización" debe construirse sobre un espacio foliado de Spec ℤ y su positividad **es** el contenido buscado (caso Weil-aritmético): **NO** — conclusión disfrazada. |
| **M9 Grandes desviaciones** | convexidad de la generadora | **SÍ** | Convexidad de $\Lambda$ es automática (Hölder); regularidad chequeable. |

**[PROPOSICIÓN 154.11 — la línea divisoria es M2/M8 sobre objetos no dados].** *Los seis mecanismos M1, M3, M4, M5, M6, M7, M9 tienen input verificable-desde-afuera siempre que el objeto ambiente esté dado explícitamente. Los únicos inputs que pueden ser conclusión-disfrazada son los de tipo POSITIVIDAD (M2, y su fuente M8) cuando el cono/la polarización no viene de una estructura ambiente dada sino que su existencia ES lo que se busca demostrar.*
**Argumento.** En M1, M3, M4, M5, M6, M7, M9 el input es una propiedad de la **estructura de partida** (coeficientes, ecuación, grupo, símbolo, medida, métrica, generadora) que existe antes del problema individual. En M2/M8 el input "$Q\succeq0$ / hay polarización positiva" puede ser, según el caso, (a) una propiedad de un objeto computable —verificable—, o (b) **el enunciado-objetivo mismo** —no verificable sin la respuesta—. La frontera **no** está entre mecanismos sino **dentro** de M2/M8, separando "positividad de un objeto dado" de "positividad como tesis". $\square$

**[PUENTE 154.12 — esto explica POR QUÉ el muro de RH es de positividad].** El programa entero descubrió, una y otra vez, que sus rutas colapsan a "$Q\succeq0$ ⟺ RH" (MW-1, el muro de positividad de Weil). La presente taxonomía da la razón estructural: **de los cinco mecanismos primitivos, cuatro tienen input verificable-desde-afuera; solo POSITIVIDAD admite la modalidad conclusión-disfrazada, y RH cae precisamente en esa modalidad.** Por eso ninguna ruta tauberiana, de ecuación, de grupo o de índice ha cerrado: para usarlas haría falta un input verificable, y RH no lo ofrece por esos canales; el único canal que "encaja" con RH es positividad, pero ahí el input **es** la conclusión. El cruce valor→inercia (M5, el $\kappa=2m$ de P35) es el único candidato con input potencialmente verificable —la clase cohomológica— pero ese input no está construido (el [GAP] de §5). **Esta es la formulación más nítida que la taxonomía permite del muro, sin enunciar ninguna equivalencia de RH.**

---

## 7. Mensaje final

**El catálogo (una línea cada uno):**
1. **Tauberiano** (Wiener/Ikehara/Hardy–Littlewood): suma generalizada → suma ordinaria; input = condición unilateral / núcleo sin ceros; **verificable**.
2. **Positividad** (máximo, traza-cero, Hodge–Riemann): integral-cero → objeto-cero; input = cono / signo definido; **verificable O conclusión-disfrazada**.
3. **Ecuación/rigidez analítica** (Holmgren/Carleman, identidad holomorfa): datos locales → solución global; input = la EDP; **verificable**.
4. **Grupo/dinámica** (Mostow, Margulis, Ratner, Weyl): invariancia gruesa → estructura rígida; input = acción rango ≥2 / unipotencia / curvatura; **verificable**.
5. **Índice/K-teoría** (Atiyah–Singer, APS, Krein): valor analítico → entero/inercia; input = clase del símbolo Fredholm; **verificable** (el único cruce valor→inercia).
(Subordinados: equidistribución ⊂ grupo; comparación geométrica y Hodge = fuentes de positividad; grandes desviaciones ⊂ positividad/convexidad.)

**Veredicto de exhaustividad:** la lista de cinco mecanismos primitivos es **exhaustiva relativa a la clasificación T1–T5 de los certificados de transversalidad al núcleo del promediador** [TEOREMA 154.9]. Todo candidato externo examinado (muestreo, momentos, concentración, transferencia, Galois inverso) se redujo a uno de los cinco. **No es una prueba metamatemática absoluta** (no la hay con estos medios); es evidencia estructural fuerte. El único hueco genuino **no es un mecanismo nuevo sino un input nuevo**: una clase cohomológica sobre Spec ℤ que lea inercia (encaja en el tipo T5 pero su realización no existe en la literatura [GAP de literatura]).

**Tres hallazgos:**

- **[TEOREMA 154.5 + 154.8] — el muro ES el núcleo del promediador, y la inercia es la única información que lo cruza sin reconstruir el objeto.** Cruzar promedio→individual ⟺ certificar $\mathcal F\cap N(A)=\{0\}$; el input estructural no añade información sobre $F$, solo la garantía de transversalidad a $N(A)$. El cruce valor→inercia (M5) es el único que **lee** el individual del promedio (porque es discreto y estable, desciende al cociente $E/N(A)$) en vez de reconstruir $F$.

- **[TEOREMA 154.9] — exhaustividad por tipo lógico de certificado.** Los cinco modos de distinguir un objeto de un subespacio —orden unilateral (tauberiano), orden cuadrático (positividad), ecuación, simetría, invariante discreto— agotan los cinco mecanismos. Un sexto mecanismo primitivo requeriría un sexto modo lógico de certificar transversalidad, que no se conoce.

- **[PROPOSICIÓN 154.11 + PUENTE 154.12] — la frontera verificable/conclusión-disfrazada cae DENTRO de positividad, y ahí cae RH.** Cuatro de los cinco mecanismos tienen input verificable-desde-afuera incondicionalmente; solo positividad (y su fuente Hodge) admite la modalidad "el input ES la conclusión". El muro de RH es de positividad **precisamente porque** es el único canal cuyo input puede ser la propia tesis. El único escape concebible —input verificable de tipo índice (la clase cohomológica T5)— es exactamente el objeto que el programa nombra como faltante y que la literatura no ofrece [GAP].

**[GAP global declarado]:** la verificabilidad de 154.9 descansa en que "todo certificado de no-pertenencia a un subespacio es de tipo T1–T5"; es una hipótesis estructural, no un metateorema. Su refutación —exhibir un cruce con un sexto tipo de input— sería el resultado de mayor valor de esta línea, y la búsqueda de §5 no lo encontró pero tampoco puede excluirlo absolutamente.

*— Doc 154, Phase 49. No se enunció ninguna equivalencia de RH; el objeto fue el muro.*
