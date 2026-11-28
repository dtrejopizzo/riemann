# FRONT 01 — Tipos CM, homometría y observables aritméticos de cuatro puntos

Fecha de corte bibliográfico: 28 de noviembre de 2026. Estado: lemas elementales demostrados y programa de investigación; no se afirma prioridad bibliográfica absoluta ni se presupone una certificación de RH/GRH.

El resultado concreto de esta exploración es una obstrucción: ciertos núcleos binarios de pesos CM no ven más que la autocorrelación que ya aparece en la teoría de Colmez. Pasar a tres puntos tampoco recupera la información perdida, por la simetría de conjugación compleja. Construimos dos tipos CM sobre un mismo campo CM concreto que tienen idénticas correlaciones de dos y tres puntos y distinta correlación de cuatro puntos. La sección 8 realiza esta información como número de Hodge de un tensor CM racional. La pregunta aritmética pendiente es dotarlo de control integral y arquimediano explícito.

## 1. Modelo preciso y alcance

Sea G un grupo abeliano finito de orden N con una involución c distinta de la identidad. Una función indicadora Φ:G→{0,1} es un tipo CM formal cuando Φ(cx)=1−Φ(x). Para 0<u<v ponemos κ(x)=u+(v−u)Φ(x) y definimos

\[
K_\kappa(t,g)=\sum_{x\in G}(t\kappa(x)-\kappa(gx))_+,\qquad t\ge0.
\]

Este es un modelo agregado de dos pesos y un mismo perfil en fuente y destino. **No es una identificación de todo el núcleo de divisibilidad de los papers con K**: allí intervienen perfiles, sumas sobre primos y datos automorfos adicionales. Cualquier transferencia al manuscrito requiere demostrar esa identificación y sus hipótesis.

Escribamos CΦ(g)=Σx Φ(x)Φ(gx) y AΦ(g)=CΦ(g)/N. Los cuatro números de pares de valores (Φ(x),Φ(gx)) son

\[
n_{11}=n_{00}=C_\Phi(g),\qquad n_{10}=n_{01}=N/2-C_\Phi(g).
\]

En efecto, cada marginal contiene N/2 unos, y la suma de los cuatro números es N. Por tanto, para todo t, sin aproximación,

\[
K_\kappa(t,g)=C_\Phi(g)((tu-u)_++(tv-v)_+)
 +(N/2-C_\Phi(g))((tu-v)_++(tv-u)_+).
\]

Recíprocamente Kκ(1,g)=(v−u)(N/2−CΦ(g)) recupera CΦ. **Todo este núcleo equivale exactamente a la autocorrelación.**

Para un campo CM abeliano con grupo G, AΦ es la función de Colmez Φ*Φ∨ con Haar normalizada; la centralización adicional que aparece en el caso general es trivial aquí. Esta conexión tiene un antecedente explícito: la definición de AΦ y su centralización están en §2 de [Parenti, arXiv:1803.02535](https://arxiv.org/abs/1803.02535), [versión publicada](https://www.numdam.org/item/CRMATH_2018__356_8_833_0.pdf). No estamos introduciendo un nuevo invariante de segundo orden.

## 2. Por qué tres puntos no bastan para tipos CM

Definimos, admitiendo repeticiones entre los g_j,

\[
T_r(g_1,\ldots,g_r)=N^{-1}\sum_x\prod_{j=1}^r\Phi(g_jx),\qquad T_0=1.
\]

**Lema.** Si r es impar, T_r está determinado por las correlaciones de orden estrictamente menor:

\[
2T_r(g_1,\ldots,g_r)=\sum_{S\subsetneq\{1,\ldots,r\}}(-1)^{|S|}
 T_{|S|}((g_j)_{j\in S}).
\]

**Prueba.** Sustituir x por cx en la suma, usar que c es central y Φ(cg_jx)=1−Φ(g_jx), y expandir el producto. El término del subconjunto completo es −T_r. Pasarlo a la izquierda prueba la identidad. □

En particular, T1=1/2 y

\[
T_3(e,g,h)=\tfrac12\big(A_\Phi(g)+A_\Phi(h)+A_\Phi(hg^{-1})\big)-\tfrac14.
\]

Esto no contradice los teoremas clásicos de reconstrucción mediante bispectros. Si f=2Φ−1, entonces f(cx)=−f(x): toda correlación centrada impar se anula. En Fourier, f̂(χ)=0 para χ(c)=1. Para Φ, todos los caracteres pares no triviales tienen coeficiente cero. No se puede importar una hipótesis de no anulación de todas las componentes de Fourier. La teoría general del bispectro ya está desarrollada en [Kakarala, arXiv:0902.0196](https://arxiv.org/abs/0902.0196); aquí únicamente probamos la obstrucción CM directamente, sin invocar un teorema de reconstrucción fuera de sus hipótesis.

El primer orden que *puede* añadir información es cuatro. No afirmamos que cuatro siempre reconstruya un tipo CM.

## 3. Ejemplo exacto en un campo CM existente

En H=Z/12 consideremos

\[
A=\{0,1,4,6\},\qquad B=\{0,1,3,7\}.
\]

Sus autocorrelaciones cS(k)=#{i:i∈S, i+k∈S}, en orden k=0,…,11, son ambas

\[
(4,1,1,1,1,1,2,1,1,1,1,1).
\]

Esto se comprueba enumerando las 16 diferencias ordenadas de cada conjunto. Es un ejemplo clásico de homometría; la idea y el ejemplo combinatorio no se ofrecen como nuevos. La teoría estructural general es anterior: [Rosenblatt–Seymour, The Structure of Homometric Sets, 1982](https://epubs.siam.org/doi/10.1137/0603035).

Tomamos G=C2×H, c=(1,0), y

\[
\Phi_S(a,i)=\mathbf1_{a=\mathbf1_S(i)}.
\]

Cada par {(0,i),(1,i)} contiene exactamente un punto del tipo, por lo que satisface la condición CM. Para g=(0,k),

\[
C_{\Phi_S}(g)=12-2|S|+2c_S(k)=4+2c_S(k),
\]

y CΦS((1,k))=12−CΦS((0,k)). En consecuencia AΦA=AΦB: coinciden todos los K binarios anteriores y todos los T3.

Sin embargo, con g=(0,1),

\[
T_4(e,g,g^2,g^3)=\frac1{24}\sum_{a,i}
\Phi_S(a,i)\Phi_S(a,i+1)\Phi_S(a,i+2)\Phi_S(a,i+3).
\]

Cada ventana de cuatro bits iguales de 1S contribuye exactamente una unidad. En A hay dos, que empiezan en 7 y 8; en B sólo la que empieza en 8. No hay cuatro unos consecutivos. Así,

\[
T_4^{\Phi_A}(e,g,g^2,g^3)=1/12,\qquad
T_4^{\Phi_B}(e,g,g^2,g^3)=1/24.
\]

Los tipos no son trasladados uno del otro por G. Una traslación con componente C2 no trivial complementa S y cambia cardinalidad 4 por 8. Las restantes exigirían que A y B fueran trasladados cíclicos. Sus multiconjuntos de huecos consecutivos son {1,2,3,6} y {1,2,4,5}; ni una traslación ni una inversión los identifica. La equivalencia aquí considerada es por automorfismos del campo CM fijado, no una afirmación sobre todas las equivalencias categóricas posibles de motivos CM.

**Realización como campo.** Sea F el subcampo de grado 12 de Q(ζ73). El grupo ciclotómico es cíclico de orden 72; el subgrupo de orden 6 contiene la conjugación compleja, de modo que F es totalmente real. Entonces E=F(i) es CM, F∩Q(i)=Q y Gal(E/Q)=C12×C2, con conjugación compleja en el factor C2. Así ΦA y ΦB son tipos CM de un campo concreto, no sólo funciones en un grupo abstracto.

Esto prueba realización *como tipos CM*. No prueba realización como datos admisibles de theta lifts, polarizaciones prescritas o sistemas de divisibilidad de la cadena original.

## 4. Segunda conexión: métricas de cortes y obstrucciones a la realización

Para un perfil positivo arbitrario, la igualdad de las sumas de κ y de κ∘g da

\[
D_\kappa(g):=K_\kappa(1,g)=\frac12\sum_x|\kappa(x)-\kappa(gx)|.
\]

Con A_s={x:κ(x)>s}, la fórmula de capas da Dκ(g)=∫|A_s△g⁻¹A_s|/2 ds. Por ello d(g,h)=Dκ(gh⁻¹) es una pseudométrica invariante de tipo L1. Además es condicionalmente negativa: para números reales a_g de suma cero, cada coordenada binaria b_g satisface Σg,h a_g a_h|b_g−b_h|=−2(Σg a_g b_g)²≤0; integrar y sumar prueba el resultado.

Es una aplicación de teoría clásica de métricas de cortes, no una novedad en análisis. Aporta un filtro concreto: un candidato a núcleo balanceado que viole la desigualdad triangular o esta negatividad no puede realizarse en este modelo. En el caso CM binario aparece la restricción adicional D(g)+D(cg)=(v−u)N/2. Ninguna de estas condiciones necesarias es aquí proclamada suficiente para realización aritmética.

## 5. Problema de investigación que sí va más allá del segundo orden

**Problema CM4 (versión cuantitativa abierta; realización racional en §8).** Construir un observable geométrico o aritmético canónico O(E,Φ), con ley explícita de transformación y normalizaciones integrales, que detecte la diferencia entre ΦA y ΦB mediante T4, y demostrar un coste controlado de denominadores, conductor y normas arquimedianas. Candidatos a investigar: un emparejamiento de cuatro realizaciones CM o una identidad de cuatro factores theta con un modelo integral común. Llamarlo simplemente «producto tensorial» no resuelve la canonicidad ni el coste.

Un teorema útil debería especificar: objeto y equivalencias bajo las cuales es invariante; fórmula exacta de sus factores locales; existencia y compatibilidad de redes; pérdida en todos los primos, incluidos ramificados; constante arquimediana y comportamiento bajo composición. La existencia de E y Φ no proporciona estas propiedades.

Para vincularlo a distribución de primos se puede definir, en el caso abeliano,

\[
F_\Phi(g)=T_4(e,g,g^2,g^3),\quad
\Psi_\Phi(X)=\sum_{p\le X,\ p\nmid D_E}F_\Phi(\mathrm{Frob}_p)\log p.
\]

La definición y su tratamiento como función de clase son clásicos: Chebotarev ya permite promediarla. La literatura reciente incluso estudia momentos para funciones de clase generales: [de La Bretèche–Fiorilli–Jouve, arXiv:2301.12899](https://arxiv.org/abs/2301.12899). **Definir Ψ no constituye un nuevo teorema sobre primos.** La pregunta más precisa es si una realización integral de FΦ puede producir cotas de coste o identidades geométricas que no se recuperen del dato AΦ y que sean uniformes en familias de campos y tipos CM. No deducimos ninguna mejora de Chebotarev o afirmación sobre nuevas funciones L.

## 6. Qué es conocido y qué permanece candidato

| Elemento | Estado |
|---|---|
| Positivos parciales, cortes L1, autocorrelaciones y pérdida de fase | Herramientas clásicas |
| AΦ como función de Colmez | Ya en la literatura CM |
| Bispectros y reconstrucción por correlaciones | Literatura extensa; sus hipótesis importan |
| Distinguir homometría de dos puntos mediante cuatro puntos | Ya existe en difracción: [Ravy, arXiv:1303.3792](https://arxiv.org/abs/1303.3792) |
| Identidad impar CM y ejemplo concreto anterior | Demostrados aquí; sin afirmación de prioridad |
| Observable CM4 canónico con coste integral y arquimediano | Objetivo no resuelto; novedad bibliográfica pendiente |

Una denominación de trabajo razonable es «geometría aritmética de correlaciones CM». No es todavía una nueva área establecida: para merecerlo debe producir un objeto aritmético, un teorema de realización y aplicaciones independientes. La búsqueda registrada no identificó una referencia que resuelva exactamente CM4 con esos costes. Ese resultado negativo de una búsqueda finita **no demuestra que el insight no exista en toda la bibliografía hasta la fecha de corte**.

## 7. Antecedentes adicionales y criterio de cierre

La teoría de k-decks ya estudia exactamente la reconstrucción de conjuntos por sus correlaciones: [Keleti–Kolountzakis, arXiv:math/0603415](https://arxiv.org/abs/math/0603415), y la reconstrucción bajo acciones de grupos aparece en [Pebody, arXiv:1607.05675](https://arxiv.org/abs/1607.05675). Por ello «profundidad mínima de correlación» tampoco debe presentarse como concepto nuevo por sí mismo. Su versión *con realizabilidad y coste aritméticos* es lo que queda por desarrollar.

Existe además un antecedente aritmético cercano y reciente: [Roy Zhao, Towards the Colmez Conjecture, arXiv:2505.06541v2, enero de 2026](https://arxiv.org/abs/2505.06541v2) introduce alturas de tipos CM parciales y relaciona períodos CM con grados aritméticos de fibrados hermitianos. Su resumen propone una fórmula de períodos sobre superficies. Aquí sólo se inspeccionó ese resumen, no se auditó todo el artículo: es una lectura obligatoria antes de afirmar que el objetivo CM4 es nuevo, y antes de elegir como observable un período o grado aritmético.

Una primera meta verificable es decidir si las construcciones de tipos parciales ya distinguen nuestro par y con qué normalización. Si lo hacen con el control requerido, corresponde usar ese resultado y abandonar la pretensión de novedad de esa parte. Si no, hay que identificar y probar la obstrucción precisa que impide extraer T4.

Las cuentas finitas del ejemplo están reproducidas en [experiments/cm_correlations.py](experiments/cm_correlations.py), con salida en [experiments/cm_correlations.json](experiments/cm_correlations.json). El programa no sustituye las pruebas de las secciones 1–3 ni una construcción aritmética CM4.

## 8. Realización inmediata como número de Hodge: avance y límite precisos

**Proposición (formalismo CM clásico).** Sea E un campo CM galoisiano abeliano de grado N y Φ un tipo CM. Para g∈G se puede construir una estructura de Hodge racional polarizable de peso cuatro, de dimensión N, cuyo número h^{4,0} es N·T4(e,g,g²,g³).

**Construcción y prueba.** Para j=0,1,2,3, sea H_j la E-línea con estructura de Hodge de peso uno cuyo sumando complejo indexado por la inmersión x:E→C tiene tipo (1,0) si Φ(g^jx)=1, y tipo (0,1) en caso contrario. La identidad Φ(cx)=1−Φ(x) garantiza compatibilidad con conjugación. Estos son los objetos de Hodge de dimensión uno sobre E asociados a tipos CM; pueden realizarse como H¹ de variedades abelianas CM, adoptando explícitamente esta convención para H^{1,0}.

Definamos

\[
V_{\Phi,g}=H_0\otimes_E H_1\otimes_E H_2\otimes_E H_3.
\]

El tensor sobre E se obtiene del tensor sobre Q imponiendo las relaciones (av)⊗w=v⊗(aw) en factores sucesivos. La multiplicación por a∈E es un endomorfismo de Hodge en cada factor; por tanto el subespacio generado por estas relaciones es un subobjeto de Hodge. El cociente tiene una estructura de Hodge racional bien definida. Es polarizable, pues los tensores y subcocientes de estructuras de Hodge puras polarizables lo son. Su dimensión sobre E es uno.

Al extender a C, E⊗Q C=∏x C obliga a que los cuatro factores de cada sumando tengan la misma etiqueta x. Por tanto

\[
(V_{\Phi,g})_\mathbb C=\bigoplus_{x\in G}\mathbb C_x,
\qquad \mathbb C_x\text{ tiene tipo }(p_x,4-p_x),\quad
p_x=\sum_{j=0}^3\Phi(g^jx).
\]

Se sigue inmediatamente que

\[
h^{p,4-p}(V_{\Phi,g})=\#\{x:p_x=p\},\qquad
h^{4,0}(V_{\Phi,g})=N T_4(e,g,g^2,g^3).
\]

Para los dos tipos de §3, g=(0,1), los histogramas en orden p=0,1,2,3,4 son

| Tipo | h^{0,4} | h^{1,3} | h^{2,2} | h^{3,1} | h^{4,0} |
|---|---:|---:|---:|---:|---:|
| ΦA | 2 | 4 | 12 | 4 | 2 |
| ΦB | 1 | 8 | 6 | 8 | 1 |

Para comprobarlos sin álgebra numérica, contar las doce ventanas de longitud cuatro en 1S. Para A, las cantidades de ventanas con k unos, k=0,…,4, son (2,4,6,0,0); para B son (1,7,3,1,0). La componente a=1 contribuye k al peso y a=0 contribuye 4−k. Sumar las dos distribuciones da los histogramas escritos. □

**Qué añade esto a CM4.** Ya existe un observable de Hodge concreto, h^{4,0}, que distingue los tipos. Por tanto el problema pendiente de §5 debe leerse en su versión fuerte: no falta la mera existencia de un objeto tensorial racional; faltan una realización integral cuantitativa y una identidad útil de períodos/normas/divisibilidad. No se afirma que h^{2,2} cuente ciclos algebraicos, ni que se haya demostrado algebraicidad de un proyector de Hodge arbitrario, ni una mejora de distribución de primos.

El tensorialismo CM es clásico; véase [Milne, Complex Multiplication](https://jmilne.org/math/CourseNotes/CM.pdf), sobre estructuras de Hodge CM y sus representaciones. Tampoco es nuevo el objetivo general de realizar estructuras CM efectivas en cohomología: [Abdulali, Hodge structures of CM-type, arXiv:math/0601052](https://arxiv.org/abs/math/0601052). Esta proposición es una aplicación explícita, útil para formular la siguiente pregunta: **¿qué cuesta integrar y normalizar V_{Φ,g} de manera compatible con los cuatro factores y con las identidades theta que se desean utilizar?**
