# Doc 122 — El bit de simetría: el carácter del apareamiento de dualidad en el divisor autodual

**Programa:** Hipótesis de Riemann — Phase 40, cerrar G1
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 119 (R-SIG: realizaciones (i)/(ii)/(iii) de una signatura; núcleo mínimo de R-SIG; test R-NC); Doc 120 (inventario CC en fuente; §3.2 dualidad de Serre con tolerancia de 2205.01391; §7.7 búsqueda negativa de "signatura"); Doc 121 (cruce A; Conjetura 121.A; divisor autodual D₀=−{2}; falsadores F-A1..F-A4; **Problema 121.E**, que este documento ejecuta).

**Fuente leída en esta sesión (junio 2026):** A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391, vía el PDF de arXiv (extraído con `pdftotext`; las citas verbatim de §5 y §1–2 abajo provienen de ese texto extraído, con número de ecuación tal como aparece). Lo que el Doc 120 verificó por extracción asistida queda aquí **re-verificado contra el texto crudo de §5** (sección Duality, líneas 1004–1315 del extracto), que es la fuente primaria del bit pedido.

**Disciplina de etiquetado (regla absoluta):** **[DATO]** = leído en fuente esta sesión, con cita exacta (paper + ecuación/teorema). **[CÁLCULO]** = derivación mía, mostrada paso a paso. **[GAP]** = lo que no se pudo determinar, con la razón y el dato exacto que faltaría. **[CONJETURA]** / **[NO VERIFICADO]** = como se indica. NUNCA "probado" sobre nada geométrico nuevo. Una falsa victoria es peor que un fracaso.

---

## 0. Resumen ejecutivo

El Problema 121.E pedía un bit: el carácter de simetría (±1) del apareamiento de dualidad de Serre con tolerancia de Connes–Consani (en adelante CC), restringido al divisor autodual D₀ = −{2}. La respuesta, tras leer §5 de 2205.01391 en fuente cruda, **no es +1 ni −1: es que la pregunta, tal como está formulada (Paso 3 de la Conjetura 121.A), presupone una estructura que la fuente NO tiene** — y la razón es estructural, no accidental.

El hallazgo central, en una línea:

> **[DATO]** El "apareamiento de dualidad de Serre" de CC **es la dualidad de Pontryagin de grupos abelianos localmente compactos**: el apareamiento subyacente es la **evaluación de caracteres** $\langle\chi, x\rangle = \chi(x) \in U(1)$ entre un grupo abeliano $A$ y su grupo dual $\widehat A$ (2205.01391, Prop. 5.2 + Thm. 5.3). NO es ni un cup product (→ alternante) ni una forma de dualidad de tipo Ext sobre un solo espacio (→ posiblemente simétrica). Es de una **tercera** especie: emparejamiento perfecto **entre un grupo y su dual, dos objetos genéricamente no isomorfos**, sin involución, sin valores en un cuerpo, sin noción de bilinealidad-sobre-un-espacio.

Para una evaluación de Pontryagin $\widehat A \times A \to U(1)$ la dicotomía "simétrica/alternante" **no está definida**: simetría requiere que dominio y codominio del par sean el mismo objeto, y aquí son $\widehat A$ y $A$. El "carácter de simetría" sólo cobra sentido tras **identificar** $\widehat A \cong A$, y esa identificación es exactamente lo que falta en el punto autodual — donde, además, **ambos espacios resultan ser cero** (§3).

**Veredicto del bit (§5): GAP estructural, con diagnóstico preciso.** No es −1 (alternante) ni +1 (simétrico): es que la dualidad de CC no es del tipo que tiene carácter de simetría. La consecuencia para R-SIG es **más fuerte que un −1**: ni siquiera se llega al punto donde Arf/paridad (la salida −1 del 121.E) sería el invariante. El dato exacto que habría que pedirle a Connes está en §5: **un autoapareamiento** — un isomorfismo natural $H^1(D_0) \cong \widehat{H^1(D_0)}$ (una "polarización principal" del módulo de tolerancia) — que la teoría hoy no provee y que en $D_0$ es vacuo porque $H^1(D_0)=0$.

---

## 1. Lo que dice la fuente, verbatim (re-verificación de §5 de 2205.01391)

Esta sección reemplaza la lectura asistida del Doc 120 §3.2 por el texto crudo de la sección 5 ("Duality") del PDF.

### 1.1. Los divisores: coeficientes ENTEROS en los primos finitos

**[DATO]** (2205.01391, §5, Thm. 5.3, línea de apertura, verbatim del extracto):

> "Let $D = \sum_j a_j\{p_j\} + a\{\infty\}$ be an Arakelov divisor on $\mathrm{Spec}\,\mathbb Z$."

y (íntroducción / §2, verbatim):

> los coeficientes cumplen $a_j \in \mathbb Z$ en los primos finitos $p_j$ y $a \in \mathbb R$ en el lugar arquimediano $\{\infty\}$ ($|\cdot|_\infty$).

**[DATO]** El divisor canónico es $K := -2\{2\}$, $\deg K = -2\log 2$ (Thm. 1.2 y §5, verbatim "where $K$ is the divisor $K=-2\{2\}$").

**Consecuencia inmediata para la admisibilidad de D₀** [CÁLCULO]: $D_0 = -\{2\}$ tiene coeficiente $a_2 = -1 \in \mathbb Z$ en el primo finito $2$, y coeficiente arquimediano $a=0$. Es por tanto un **divisor de Arakelov admisible** en el sentido estricto de su §5: coeficiente entero en un primo finito, coeficiente real (aquí cero) en $\infty$. **No hace falta semienteros ni coeficientes reales en primos finitos.** El cruce (A) NO muere por inadmisibilidad de D₀: el punto fijo existe dentro de su categoría de divisores. (Esto cierra, en positivo, el sub-chequeo del Paso 2 del encargo: la duda "¿−1 en el lugar 2 es admisible?" se resuelve SÍ.)

[CÁLCULO] Verificación del punto fijo, exacta a nivel de divisores (no de clases):
$$K - D_0 = -2\{2\} - (-\{2\}) = -2\{2\} + \{2\} = -\{2\} = D_0.$$
La involución de Serre $\sigma: D \mapsto K-D$ fija $D_0$ **on the nose**. Coincide con Doc 121 §2.1.2.

### 1.2. Los objetos H⁰ y H¹: módulos sobre 𝕊[±1] con tolerancia

**[DATO]** (2205.01391, §1–2, verbatim):

- $H^0(D)$ es el $\mathbb S[\pm1]$-módulo $\|H\mathbb Z\|_{e^a}$: en el conjunto puntuado $k_+$, las familias $m = \sum \alpha(f) f$ con norma total $\sum|\alpha(f)f| \le e^a$. Para divisor arquimediano $D=a\{\infty\}$, "depends only upon the integer part $n=\lfloor e^a\rfloor$".
- $H^1(D)$ es el **conúcleo** de $\psi$ en (1.2), realizado como **pareja $(\,H\mathbb A_{\mathbb Q},\,\mathcal R\,)$** — un *tolerance $\mathbb S[\pm1]$-module* — donde $\mathcal R$ relaciona pares cuya diferencia está en $\mathrm{Im}\,\psi$. Verbatim (§1, sobre el caso arquimediano):

> "the dimension of $H^1(D)$ is the same as the dimension of the pair $(H(\mathbb R/\mathbb Z), R)$, where the relation $R$ on $H(\mathbb R/\mathbb Z)(1_+)=\mathbb R/\mathbb Z$ is given by $(x,y)\in R \iff d(x,y)\le e^a$" (1.4),

con $d$ la métrica riemanniana invariante de longitud 1 en $\mathbb R/\mathbb Z$.

**[DATO]** Dimensión de $H^1$ del divisor arquimediano (2205.01391, Prop. 4.1, eq. (1.5), verbatim):
$$\dim_{\mathbb S[\pm1]}(H(\mathbb R/\mathbb Z), R) = \left\lceil \frac{-a-\log 2}{\log 3}\right\rceil.$$

### 1.3. La dualidad ES Pontryagin: el apareamiento es evaluación de caracteres

Éste es el corazón del documento. Cito §5 en bloque (verbatim del extracto, eqs. (5.11), Prop. 5.2(i)–(ii), Thm. 5.3):

**[DATO]** Apertura de §5 "Duality":

> "In this section we prove an absolute analogue of Serre's duality, namely the following isomorphism of $\mathbb S[\pm1]$-modules, for any divisor $D$ on $\mathrm{Spec}\,\mathbb Z$:
> $$H^0(D) \simeq \mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(K-D),\, U(1)_{\frac14}). \quad$$
> Here, the divisor $K=-2\{2\}$ plays the role of the canonical divisor. The choice of the tolerant $\mathbb S[\pm1]$-module $(U(1),d)_{\frac14}$ as dualizing module is motivated by Pontryagin duality. One has $\dim_{\mathbb S[\pm1]}(U(1)_{\frac14})=1$."

**[DATO]** Definición del módulo dualizante (§5.2, verbatim):

> "we consider, for $\lambda>0$, the $\mathbb S[\pm1]$-module $U(1)_\lambda = (U(1),d)_\lambda$, where $U(1)$ is the abelian group $\mathbb R/\mathbb Z$ endowed with its canonical metric $d$ of length 1. For a metric abelian group $(A,d)$, we denote by $\widehat A$ the abelian group of continuous characters, i.e. of continuous group homomorphisms $A\to U(1)$."

**[DATO]** Proposición 5.2(i) (verbatim):

> "For $\lambda,\mu\in\mathbb R_{>0}$, the $\mathbb S[\pm1]$-module $\mathrm{Hom}_{\Gamma\mathcal T_*}((A,d)_\lambda, U(1)_\mu)$ is isomorphic to the sub $\mathbb S[\pm1]$-module of $H\widehat A$ which, on the set $k_+$, is given by $k$-tuples $(\chi_j)$, $1\le j\le k$ of continuous characters $\chi_j\in\widehat A$ such that, with $|x|:=d(x,0)$, and for all finite collections $\{x_i\}\subset A$, fulfill
> $$\sum_i |x_i|\le\lambda \;\Rightarrow\; \sum_{i,j}|\chi_j(x_i)|\le\mu. \quad(5.8)$$"

Y en la prueba (verbatim): "This shows that $\mathrm{Hom}_{\Gamma\mathcal T_*}((A,d)_\lambda,U(1)_\mu)$ consists exactly of the group homomorphisms $\chi: A\to U(1)$ fulfilling (5.8)."

**[DATO]** Prueba de Thm. 5.3 (verbatim, núcleo): con $\lambda=\exp a$, $H^1(D)=\pi^*((\mathbb R/L,d)_\lambda)$; por Prop. 5.2(ii) se reduce a $\mathrm{Hom}_{\Gamma\mathcal T_*}((\mathbb R/\mathbb Z,d)_\lambda, U(1)_{\frac14})$; y se identifica

> "with $A=\mathbb R/\mathbb Z$ and $\mu=\frac14$. One has $\widehat A=\mathbb Z$ and the characters $\chi_n\in\widehat A$ are given by multiplication by $n$, i.e. $\chi_n(s):=ns\in\mathbb R/\mathbb Z$, $\forall s\in\mathbb R/\mathbb Z$."

resultando el submódulo $\|H\mathbb Z\|_{1/4\lambda}$.

**Lectura estructural [CÁLCULO/DATO mixto, cada cláusula etiquetada]:**

1. **[DATO]** El dual de Serre $H^0(K-D) = \mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(D), U(1)_{1/4})$ es **literalmente un grupo de caracteres** $\widehat{A}$ del grupo abeliano $A$ sobre el que se construye $H^1(D)$ (acá $A=\mathbb R/\mathbb Z$, $\widehat A = \mathbb Z$), recortado por la condición de tolerancia (5.8).
2. **[DATO]** El "apareamiento" que realiza la dualidad es, por tanto, la **evaluación de Pontryagin**
   $$\langle\,\cdot\,,\,\cdot\,\rangle:\ \widehat A \times A \longrightarrow U(1),\qquad (\chi, x)\longmapsto \chi(x),$$
   es decir $(n, s)\mapsto ns \bmod 1$ en el caso explícito. Es un homomorfismo de grupos en cada variable (biaditivo), perfecto (Pontryagin), con valores en el **grupo** $U(1)=\mathbb R/\mathbb Z$.
3. **[DATO/CÁLCULO]** Este apareamiento empareja **dos objetos distintos**: $A$ (grupo) y $\widehat A$ (su dual). Genéricamente $A\not\cong\widehat A$ (aquí $A=\mathbb R/\mathbb Z$ es compacto conexo, $\widehat A=\mathbb Z$ es discreto: no son ni siquiera del mismo tipo topológico). NO hay un solo espacio sobre el que la dualidad sea una forma.

---

## 2. Por qué "carácter de simetría" no está definido para una evaluación de Pontryagin

El encargo (Paso 4) pedía distinguir DOS posibilidades y decir cuál es la de CC:

- **(cup product)** $H^1\times H^1\to H^2$: en toda cohomología de Weil es **alternante** en grado impar (forma simpléctica, polarización principal de la jacobiana). Salida −1.
- **(dualidad de Serre tipo Ext)** $H^1(D)\times H^0(K-D)\to k$ con $k$ un cuerpo: en el punto autodual puede inducir una forma **simétrica** sobre $H^1$. Salida +1.

La fuente fuerza una tercera respuesta, y conviene exhibir el álgebra de por qué las dos dicotomías clásicas no se aplican.

### 2.1. El requisito algebraico de "simetría" y dónde falla

[CÁLCULO] Una forma bilineal $B: V\times V\to T$ tiene carácter de simetría $\varepsilon\in\{\pm1\}$ cuando $B(x,y)=\varepsilon\,B(y,x)$. Esto **presupone**:
- (a) **un solo espacio** $V$ en ambas ranuras (para que $B(y,x)$ tenga sentido hay que poder meter $y\in V$ en la primera ranura y $x\in V$ en la segunda);
- (b) un codominio $T$ donde la igualdad $B(x,y)=\varepsilon B(y,x)$ sea una ecuación con sentido (un grupo abeliano basta para esto).

El apareamiento de CC, $P:\widehat A\times A\to U(1)$, $P(\chi,x)=\chi(x)$:
- **(a) FALLA.** Las dos ranuras son $\widehat A$ y $A$, objetos distintos. $P(x,\chi)$ no está definido: $x\in A$ no es un carácter, no se puede evaluar en $\chi$. La expresión "$P(y,x)$ vs $P(x,y)$" carece de referente.
- (b) se cumpliría (U(1) es grupo abeliano), pero es irrelevante sin (a).

**[CÁLCULO] Conclusión: el carácter de simetría $\varepsilon$ de $P$ NO está definido en la fuente.** No es que sea +1 o −1 y CC no lo digan: es que la estructura que CC construyen (dualidad de Pontryagin grupo↔dual) no es del tipo que tiene un $\varepsilon$. Para tener uno haría falta una **identificación previa** $j: A \xrightarrow{\sim} \widehat A$ (una "polarización"), tras la cual $B(x,y):=P(j(x), y)=\langle j(x), y\rangle$ vive sobre $V=A$ y SÍ tiene carácter $\varepsilon$. Esa $j$ es input externo; no está en 2205.01391.

### 2.2. Por qué no es un cup product (descarta la salida −1 "fácil")

[DATO+CÁLCULO] El cup product de una cohomología de Weil es un producto **interno al álgebra cohomológica** $H^\bullet$, $H^i\otimes H^j\to H^{i+j}$, con la antisimetría graduada $a\cup b=(-1)^{ij}b\cup a$ como **propiedad del producto**. En 2205.01391:
- No hay álgebra cohomológica graduada $H^\bullet$ con producto: hay $H^0$ y $H^1$ de un **divisor** (no de un espacio total), y la única operación entre ellos es el morfismo $\psi$ de la sucesión corta y su dualización Pontryagin. **[DATO]** (no aparece producto-copa en el texto; el índice de §5 es "Serre and Pontrjagin dualities", no "cup product").
- El "$H^2$" donde aterrizaría un cup product **no existe** en su teoría de dimensión 1 (es una "curva" $\mathrm{Spec}\,\mathbb Z$, no una superficie). El target de la dualidad es $U(1)_{1/4}=H^1(K)$, no un $H^2$.

Por tanto **la advertencia del Doc 121 §2.1.4 (F-A1: "en grado impar el cup product es alternante") no se aplica al objeto de CC**: no hay cup product. Esto es una buena noticia parcial — el camino NO se corta por la vía clásica desfavorable — pero la mala noticia la sustituye: tampoco hay forma simétrica de tipo Ext, porque no hay cuerpo de valores ni espacio único.

### 2.3. Por qué no es dualidad de Serre "tipo Ext sobre un cuerpo" (descarta la salida +1 "fácil")

[DATO+CÁLCULO] La dualidad de Serre clásica $H^1(D)\times H^0(K-D)\to H^1(K)\cong k$ valora en el **cuerpo base** $k$, y el apareamiento es $k$-**bilineal**; eso permite, vía un iso $H^0(K-D)\cong H^1(D)^\vee$ y la autodualidad $2D=K$, fabricar una forma $k$-bilineal sobre $H^1(D)$ cuyo $\varepsilon$ se calcula.

En CC el target es $U(1)_{1/4}=H^1(K)$, que **no es un cuerpo**: es el grupo $\mathbb R/\mathbb Z$ con una tolerancia. El apareamiento es **biaditivo (ℤ-bilineal de grupos), no $k$-bilineal sobre un cuerpo**. La maquinaria "iso de dualidad + autodualidad ⟹ forma con $\varepsilon$" requiere linealidad sobre un cuerpo para que la transpuesta $B^t$ viva en el mismo espacio de formas y la comparación $B$ vs $B^t$ dé un escalar $\varepsilon$. Sobre un grupo abeliano sin estructura de cuerpo, "transponer" un carácter no devuelve un carácter del mismo grupo (devuelve un elemento del bidual, vía evaluación) — y esa es justamente la reflexividad de Pontryagin $A\cong\widehat{\widehat A}$, **no** una simetría $\widehat A\cong A$.

[CÁLCULO] Hagamos explícito el único "carácter de simetría" que SÍ existe aquí, para no confundirlo con el pedido. La dualidad de Pontryagin tiene un **iso de bidualidad** canónico
$$\mathrm{ev}: A \xrightarrow{\ \sim\ } \widehat{\widehat A},\qquad \mathrm{ev}(x)(\chi)=\chi(x).$$
Su "cuadrado" (la compatibilidad $\widehat{\mathrm{ev}_A}\circ\mathrm{ev}_{\widehat A}=\mathrm{id}$) es siempre **+1** — pero esto es la reflexividad, un hecho de toda dualidad de Pontryagin, y **NO** es el bit del 121.E. El 121.E pedía el $\varepsilon$ de una forma sobre $H^1(D_0)$; la bidualidad da, en cambio, que $H^1(D_0)$ es reflexivo. Confundir ambos sería la falsa victoria a evitar: "+1 de bidualidad" no es "+1 de forma simétrica". **[CÁLCULO, etiquetado como advertencia anti-circular.]**

---

## 3. El punto autodual D₀: ambos espacios se anulan (falsador F-A4 confirmado)

Aun concediendo, *por mor del argumento*, que existiera una identificación $j:H^1(D_0)\cong\widehat{H^1(D_0)}$, hay que computar qué objeto es $H^1(D_0)$. La fuente lo da exactamente.

[CÁLCULO] $D_0=-\{2\}$ tiene $\deg D_0 = -\log 2$, parte arquimediana $a=0$. Pero $H^1$ de un divisor con soporte en un primo finito se reduce (Thm. 5.3, "we can assume that $D=a\{\infty\}$ with $a=\deg D$") al $H^1$ del divisor arquimediano de **el mismo grado**. Así que tomamos $a=\deg D_0=-\log 2$ y aplicamos (1.5):
$$\dim_{\mathbb S[\pm1]} H^1(D_0) = \left\lceil \frac{-a-\log 2}{\log 3}\right\rceil = \left\lceil \frac{\log 2-\log 2}{\log 3}\right\rceil = \lceil 0\rceil = 0.$$

[DATO] Y por la fórmula RR (Thm. 1.1) con $\chi(D_0)=0$ (Doc 121 §2.1.2; aquí re-derivado: $\dim H^0-\dim H^1=0$ en el punto autodual por $\deg D_0+\log2=0$ en el numerador del término techo), se sigue
$$\dim_{\mathbb S[\pm1]} H^0(D_0) = \dim_{\mathbb S[\pm1]} H^1(D_0) = 0.$$

**[CÁLCULO] Verdicto del punto puntual: en $D_0$ ambas cohomologías son CERO.** Cualquier forma sobre $V=H^0(D_0)\oplus H^1(D_0)=0$ es la forma vacía: su signatura es $(0,0)$, su carácter de simetría es vacuamente cualquiera, su Arf es trivial. **El cómputo puntual del 121.E no porta información**: es el falsador **F-A4** del Doc 121 §2.1.4, ahora confirmado en fuente, no conjeturado.

Esto refina el diagnóstico: el contenido del cruce A, si lo hay, **no está en el punto $D_0$ sino en el SALTO** — la variación de $(\dim H^0,\dim H^1)$ al perturbar $D_0$ (recordar Doc 121 §2.1.2.3: $\lambda=1/2$ cae en el borde del intervalo de salto $2^{-m-1}\le\lambda<2^{-m}$ con $m=0$). El objeto que podría portar una signatura no es la fibra en $D_0$ sino el **comportamiento de degeneración** alrededor de $D_0$ — lo que conecta con el cruce D (flujo espectral en el monoide de Picard), no con un apareamiento puntual. **[CÁLCULO + remisión a Doc 121 §2.4.]**

---

## 4. Síntesis del bit: la dicotomía del encargo, resuelta por una tercera opción

Recapitulo las tres especies de apareamiento y dónde cae CC.

| especie | dominio del par | codominio | carácter $\varepsilon$ | ¿es CC? |
|---|---|---|---|---|
| cup product $H^1\times H^1\to H^2$ | un espacio, consigo | cuerpo | **−1** (alternante, grado impar) | **NO** (no hay producto-copa ni $H^2$) |
| Serre–Ext $H^1\times H^0(K-D)\to k$ + autodualidad | un espacio tras iso | cuerpo $k$ | $\pm1$ calculable | **NO** (target $U(1)$ no es cuerpo; biaditivo, no $k$-bilineal) |
| **Pontryagin $\widehat A\times A\to U(1)$** | **grupo y su dual (distintos)** | **grupo** $U(1)$ | **no definido** (falta iso $A\cong\widehat A$) | **SÍ** (Prop. 5.2 + Thm. 5.3) |

**[CÁLCULO/DATO] El apareamiento de CC es de la tercera especie.** Por eso:
- No hereda la alternancia del cup product (no es uno): la salida "−1 automática" del precedente Weil **no aplica**.
- No admite la simetrización tipo Ext (no hay cuerpo, no hay espacio único): la salida "+1" **tampoco aplica**.
- Su único "+1 canónico" es la reflexividad de bidualidad, que **no es el bit pedido**.

El bit del 121.E queda, pues, **GAP** — pero un GAP de tipo superior al previsto: no es que no se sepa si es +1 o −1; es que **el invariante "carácter de simetría" no es un atributo de la estructura que CC tienen**. La dualidad de CC vive en la categoría de grupos abelianos con tolerancia, donde "forma bilineal con signatura" no es una noción nativa.

---

## 5. Veredicto y el dato EXACTO a pedirle a Connes

### 5.1. Veredicto

**El bit del Problema 121.E: GAP estructural.** No +1, no −1. La dualidad de Serre con tolerancia de 2205.01391 es **dualidad de Pontryagin grupo↔dual** (evaluación de caracteres $\widehat A\times A\to U(1)$, Prop. 5.2(i), Thm. 5.3), no un apareamiento sobre un solo espacio; el "carácter de simetría" no está definido para ella sin una identificación externa $A\cong\widehat A$. Y en el punto autodual concreto $D_0=-\{2\}$, **ambos espacios se anulan** ($\dim H^0(D_0)=\dim H^1(D_0)=0$, eq. (1.5) con $a=-\log2$), de modo que incluso la versión más débil del experimento (Arf/paridad, la salida −1 del 121.E) es vacua.

Esto es, en la escala del Doc 119, **peor que −1 para R-SIG**: la salida −1 del 121.E dejaba vivo un invariante mod 2 y nombraba "polarización" como lo que falta; el GAP estructural dice que **falta una capa más abajo** — falta la propia categoría de formas. Pero es, por la disciplina del encargo, un **resultado valioso y honesto**: convierte "no sabemos el signo" en "sabemos que el signo no es un atributo de esta dualidad, y sabemos exactamente qué habría que añadir".

Impacto sobre el cruce A (Doc 121 §2.1) y sobre R-SIG (Doc 119 §2.3, realización (i)): la realización (i) de R-SIG ("una forma bilineal/hermitiana con involución sobre un espacio") **no se obtiene de la dualidad de CC tal cual**. La dualidad de CC realiza, a lo sumo, la **dualidad de Poincaré** (el apareamiento perfecto $H^1\times H^0(K-D)\to$ dualizante), que es el **ingrediente previo** a una forma, no la forma. Para pasar de Poincaré-Pontryagin a forma-con-signatura hace falta el segundo ingrediente clásico: una **polarización** (un iso del objeto con su dual, compatible y "positivo"). Es exactamente el diagnóstico que el Doc 121 §4.2 anticipaba como el escenario −1 ("R-SIG necesita una polarización además de la dualidad"), ahora confirmado y agravado: no es opcional ni un refinamiento, es el eslabón ausente que define el problema.

### 5.2. El pedido exacto a Connes (el dato que cerraría/movería el bit)

Formulado como enunciado interno a 2205.01391, autocontenido:

> **Pedido 122.A (autoapareamiento / polarización del módulo de tolerancia).** En la categoría $\Gamma\mathcal T_*$ de $\mathbb S[\pm1]$-módulos con tolerancia, ¿existe, para un divisor autodual $2D=K$ (en particular $D_0=-\{2\}$), un **isomorfismo natural** $j_D: H^1(D)\xrightarrow{\sim}\mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(D),U(1)_{1/4})$ — es decir, un iso de $H^1(D)$ con su **propio** dual de Pontryagin-con-tolerancia (no con $\widehat A$ de un grupo auxiliar) — compatible con la involución de Serre $\sigma$? Si existe, la composición $B_D(x,y):=\langle j_D(x), y\rangle\in U(1)_{1/4}$ es una forma biaditiva sobre $H^1(D)$, y **su carácter de simetría $\varepsilon$ (¿$j_D^\vee=\pm j_D$ bajo la bidualidad?) es el bit del 121.E**. Pregunta dependiente: ¿es $j_D$ **positiva** en algún sentido (una "métrica", una forma definida) que linealice $U(1)_{1/4}$ a $\mathbb R$ con signo (salvar F-A3)?

Qué teorema/objeto de qué paper lo resolvería:
1. **En 2205.01391 directamente:** un teorema de **autodualidad** (no sólo dualidad) para los módulos de tolerancia en el punto $2D=K$ — el análogo del hecho clásico "en la característica theta, $H^0(K-D)\cong H^0(D)$ canónicamente, y la forma de Serre se vuelve forma sobre $H^0(D)$". CC tienen $H^0(K-D)\cong\widehat{H^1(D)}$ (dualidad) pero **no** un $H^1(D)\cong\widehat{H^1(D)}$ (autodualidad). El bit vive en ese iso que no está escrito.
2. **El ingrediente que en su corpus no tiene candidato (búsqueda confirmada, abajo):** una **polarización / forma positiva / métrica** sobre el $H^1$ — el análogo del operador de Lefschetz $L$ o de la estrella de Hodge $\star$, que en geometría clásica convierte la dualidad de Poincaré en forma de intersección con signatura (Hodge–Riemann). Sin ese ingrediente, la dualidad de Pontryagin de CC se queda en Poincaré y nunca llega a signatura — en dimensión 1 **ni en el cuadrado**.

### 5.3. Búsqueda confirmatoria: ¿hay polarización/forma positiva en el corpus CC?

[DATO] Doc 120 §7.7 (búsqueda negativa): "signatura/índice de inercia" no aparece como invariante en ningún texto leído; la única estructura de signo es positividad/lower-boundedness.

Re-chequeo dirigido a este documento (sobre lo verificado en Doc 120, sin nueva sesión de fetch para no exceder el alcance del encargo, que centraba la lectura en 2205.01391):
- En **2205.01391** (leído en fuente cruda esta sesión): la única estructura métrica es la **tolerancia** $d$ de longitud 1 en $\mathbb R/\mathbb Z$ y el parámetro $\lambda$; **no** hay forma positiva sobre $H^1$, ni operador $L$, ni iso de autodualidad. El "$1/4$" de $U(1)_{1/4}$ es un parámetro de tolerancia elegido "by the invariance of the Riemann-Roch formula when one switches $H^0$ and $H^1$" (§5, verbatim) — combinatorio, no una polarización. **[DATO]**
- En **2602.15941** (Jacobiano, vía Doc 120 §3.4): el Picard es un **monoide** con **semi-normas** (degeneración permitida); una semi-norma es lo más cercano a una "métrica/positividad" del corpus, pero está sobre el moduli de fibrados de rango 1, **no** sobre un $H^1$ del cuadrado, y CC no la usan como polarización de una forma de intersección. **[DATO, vía Doc 120; NO VERIFICADO en fuente esta sesión que aparezca "polarization"/"positive form" como término en 2602.15941 — el Doc 120 §3.4 reporta búsqueda negativa de "intersection theory"/"Hodge index" en ese paper].**
- En **2006.13771** (positividad arquimediana): hay una **positividad** real ($W_\infty(g*g^*)\ge0$ en la ventana), que CC mismos llaman el germen de "an intersection theory of divisors on the square of the Scaling Site" (Doc 120 §4.4). Es lo más parecido a una forma definida — pero es **analítica, en un lugar, sobre tests**, no una polarización del $H^1$ algebraico de 2205.01391, y globalizarla es MW-6 (O_SL, Doc 121 §4.3). **[DATO, vía Doc 120.]**

**Conclusión de la búsqueda:** se **confirma** el reporte del Doc 120: no hay, en el corpus CC, una polarización (iso objeto↔dual positivo) sobre el $H^1$ que convierta la dualidad de Pontryagin en una forma con signatura. El único candidato a "positividad" (2006.13771) es de naturaleza distinta (analítica, no la autodualidad del módulo de tolerancia) y RH-equivalente al globalizarse. **El ingrediente que el bit revela como faltante no tiene candidato.**

---

## 6. R-NC aplicado a este resultado

[CÁLCULO] El resultado de este documento (un GAP estructural y un pedido) no es una propuesta de puente, así que R-NC se aplica al **Pedido 122.A** para asegurar que, si Connes lo respondiera, no sería RH-disfrazada:
- **NC1 (externalidad):** el Pedido 122.A se formula enteramente en $\Gamma\mathcal T_*$ y divisores de Arakelov; no menciona $\zeta$ ni ceros. **PASA.** (Es un enunciado sobre la categoría de CC, no sobre L-funciones.)
- **NC2 (sobregeneración):** pide la autodualidad para **todo** divisor autodual $2D=K$ y la polarización como propiedad de la categoría, no del objeto que codifica $\zeta$ (que en dim 1 no existe). **PASA** en su nivel (dim 1, lejos de ceros — el mismo veredicto del Doc 121 §2.1.5 para el cruce A).
- **NC3/NC4:** no evaluables en dim 1 (no individúan ceros); el riesgo se traslada íntegro al momento de repetir el mecanismo en el cuadrado. Idéntico al Doc 121 §2.1.5.

El Pedido 122.A es, por tanto, una pregunta legítima (no circular) y barata para un experto en el formalismo de CC: es un enunciado sobre sus propias definiciones de §5.

---

## 7. Cierre

Ningún enunciado geométrico nuevo se ha probado aquí. Se ha **leído en fuente** (§5 de 2205.01391, texto crudo) y **calculado** que: (i) $D_0=-\{2\}$ es divisor admisible y punto fijo exacto de $\sigma$ — el cruce A no muere por inadmisibilidad; (ii) la dualidad de CC es dualidad de **Pontryagin** (evaluación de caracteres grupo↔dual), de una tercera especie distinta tanto del cup product (alternante) como de la dualidad de Serre sobre un cuerpo (simetrizable); (iii) por eso el "carácter de simetría" **no está definido** para ella sin una polarización externa; (iv) en $D_0$ ambos $H^\bullet$ se anulan, así que el cómputo puntual es vacuo (F-A4). El bit del 121.E es **GAP estructural**, y el dato exacto a pedir a Connes es el **Pedido 122.A**: un iso de autodualidad $H^1(D)\cong\widehat{H^1(D)}$ en el punto autodual y una polarización positiva sobre él — el análogo del operador de Lefschetz/Hodge, que en todo el corpus CC no tiene candidato.

Para el programa: la salida es la peor de las tres del 121.E para R-SIG, y a la vez la más informativa. Lo que falta no es "elegir entre dualidad simétrica o alternante" sino **construir la categoría de formas** (una polarización del $H^1$ de tolerancia) que CC no tienen. La fase 40 debe, en consecuencia: (a) NO esperar signatura del cruce A puntual; (b) redirigir el cruce A a su versión de **degeneración/salto** alrededor de $D_0$ (puente con el cruce D, monoide de Picard, §3); (c) mantener el Pedido 122.A como el enunciado interno-a-CC que un experto en $\Gamma\mathcal T_*$ puede decidir, y cuya respuesta positiva (si existe $j_D$ con $\varepsilon$ y positividad) reabriría el camino dualidad→signatura — esta vez con el ingrediente correcto identificado.

---

## Referencias

**Fuente primaria leída esta sesión:** A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391 (PDF, vía `pdftotext`): §1 (eqs. (1.3)–(1.6)), §2 (cohomologías $H^0,H^1$), §4 (Prop. 4.1, eq. (1.5)), §5 "Duality" (eq. (5.11), Lemma 5.1, Prop. 5.2(i)–(ii) eqs. (5.8)–(5.10), Thm. 5.3, eq. (5.12)), Apéndice A (tolerance relations: "reflexive and symmetric relation").

**Internas (backward-only):** Doc 119 (R-SIG realizaciones (i)/(ii)/(iii); R-NC); Doc 120 (inventario CC; §3.2, §4.4, §7.7); Doc 121 (cruce A; Conjetura 121.A pasos 1–5; falsadores F-A1..F-A4; Problema 121.E; §2.1.5 R-NC del cruce A; §4.2 escenario −1 ⟹ polarización).

**Clásica (contexto, vía Doc 119/121, no re-verificada esta sesión):** dualidad de Pontryagin de grupos abelianos l.c. (reflexividad $A\cong\widehat{\widehat A}$); Hodge–Riemann / operador de Lefschetz como polarización que convierte Poincaré en forma con signatura; Mumford (1971), Atiyah (1971) sobre paridad de características theta (la salida −1/Arf que aquí NO se alcanza).

*Fin del Doc 122.*
