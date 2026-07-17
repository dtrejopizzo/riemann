# Documento 167 — Dinámica del índice κ: cuantización, muros de Maslov y la ley de balance de la energía de inestabilidad

**Programa:** Hipótesis de Riemann — Fase 54 (dinámica del índice)
**Fecha:** 2026-06-10
**Prerrequisitos:** Phase 26 (κ=2m, espacio de Pontryagin), Phase 28 (DBN = gradiente de E_log), Phase 33 / Docs 70–72 (traza T_λ(t), derivada temporal, fórmula de Weil), Phase 44 / Doc 132 (B.4, δ=1 prohibido), Phase 46 / Doc 143 (exponente Lehmer = 2; LP-134/LP-143), Phase 48 / Doc 144 (contraejemplo de Hadamard, m=∞ analítico), Phases 52–53 (ζ ES la dualidad; el muro en lenguaje de Krein).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] con prueba completa o sin etiqueta; [PUENTE] honesto; [GAP]/[DESEO] declarados. **Este documento NO intenta probar κ=0.** El objeto es κ mismo: su cuantización, sus muros, su dinámica.

---

## 0. Convenciones y normalización

### 0.1. La función y el flujo

$\Xi(z) = \xi(\tfrac12 + iz)$, entera de orden 1, par, real en $\mathbb{R}$. Un cero $\rho = \tfrac12 + b + i\gamma$ de $\zeta$ corresponde al cero $z = \gamma - ib$ de $\Xi$; RH $\iff$ todos los ceros de $\Xi$ son reales. La banda crítica da $|\operatorname{Im} z| < \tfrac12$ para todo cero (región libre de ceros de Hadamard–de la Vallée Poussin da la desigualdad estricta).

Flujo de De Bruijn–Newman en la normalización de Polymath 15: con $\Phi$ la densidad superexponencial estándar y

$$H_t(z) = \int_0^\infty e^{tu^2}\,\Phi(u)\cos(zu)\,du, \qquad H_0 = \tfrac18\,\Xi(\cdot/2)\ \text{(salvo reescalado fijo)},$$

se tiene la ecuación del calor *hacia atrás*

$$\partial_t H_t = -\partial_z^2 H_t.$$

$\Lambda$ = constante de De Bruijn–Newman: $H_t$ tiene solo ceros reales $\iff t \ge \Lambda$. Hechos duros que usamos como input:

- **de Bruijn 1950** [dB]: $\Lambda \le \tfrac12$; la realidad de los ceros es absorbente (si $H_{t_0}$ tiene ceros reales, $H_t$ también para $t \ge t_0$).
- **Newman 1976** [N]: $\Lambda > -\infty$; conjetura $\Lambda \ge 0$.
- **Ki–Kim–Lee 2009** [KKL]: $\Lambda < \tfrac12$; y para **todo $t>0$**, $H_t$ tiene a lo sumo **finitos** ceros no reales, y todos los ceros salvo finitos son reales y simples.
- **Rodgers–Tao 2020** [RT]: $\Lambda \ge 0$. Luego RH $\iff \Lambda = 0$.
- **Polymath 15, 2019** [P15]: $\Lambda \le 0{.}22$; dinámica de ceros $\partial_t x_k = 2\sum'_{j\ne k} 1/(x_k - x_j)$ (suma simetrizada).

### 0.2. El índice

Para una configuración de ceros $Z$ (multiconjunto en $\mathbb{C}$, cerrado bajo $z\mapsto\bar z$ y $z\mapsto -z$):

$$\kappa(Z) := \#\{z \in Z : \operatorname{Im} z > 0\} \quad (\text{con multiplicidad}).$$

Para $\zeta$: cada cuádruplo off-line $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$ da 4 ceros no reales de $\Xi$, de los cuales 2 en el semiplano superior; con $m$ = número de cuádruplos, $\kappa = 2m$. Esto **coincide** con el índice de Kreĭn de Phase 26 (κ = neg.ind$(Q)$ = 2m): cada cuádruplo aporta exactamente un plano hiperbólico al espacio negativo de la forma de Weil. Escribimos $\kappa(t) := \kappa(Z_t)$ con $Z_t$ = ceros de $H_t$. Por [KKL], $\kappa(t) < \infty$ para todo $t > 0$ **incondicionalmente**; $\kappa(0) < \infty$ es la mitad de finitud abierta ($m<\infty$), que **no** se prueba aquí.

---

## 1. Nivel 1: κ como invariante topológico — el espacio 𝒞 y los muros

### 1.1. El espacio de configuraciones

**[DEFINICIÓN-NUEVA 1.1] (espacio de configuraciones $\mathcal{C}$).** $\mathcal{C}$ es el conjunto de multiconjuntos localmente finitos $Z \subset \{|\operatorname{Im} z| \le \tfrac12\}$ tales que:

1. *(realidad)* $\bar Z = Z$;
2. *(ecuación funcional)* $-Z = Z$;
3. *(densidad RvM)* $N_Z(T) := \#\{z : |\operatorname{Re} z| \le T\} = \frac{T}{\pi}\log\frac{T}{2\pi e} + O(\log T)$;
4. *(género)* $\sum_{z \in Z, z\neq 0} |z|^{-2} < \infty$ (automático de 3).

Topología: la inducida por convergencia **local de Hurwitz** — $Z_n \to Z$ si las medidas de conteo convergen vagamente y, en cada compacto cuya frontera evita $Z$, los conteos coinciden eventualmente. Un **camino admisible** es $u \mapsto Z_u$ continuo en esta topología; lo llamamos **propio** si existe un compacto $K$ que contiene $\{z \in Z_u : \operatorname{Im} z \ne 0\}$ para todo $u$ (los ceros no reales no escapan al infinito ni entran desde él).

*Por qué hace falta "propio":* en la topología vaga sola, un par no real puede deslizarse hacia $\operatorname{Re} z \to \infty$ y "desaparecer", cambiando κ sin evento local. La propiedad es la hipótesis honesta mínima; para el flujo DBN con $\kappa<\infty$ se cumple automáticamente en intervalos compactos de tiempo (los ceros se mueven con velocidad localmente acotada, Lema 2.1).

### 1.2. Los dos muros

**[DEFINICIÓN-NUEVA 1.2] (muros).** Dentro de $\mathcal{C}$:

- **Muro de colisión** $W_{\mathrm{col}} := \{Z : Z$ tiene un cero real de multiplicidad $\ge 2\}$. Codimensión 1 (una condición real: la colisión de dos ceros reales, o el aterrizaje de un par conjugado, ocurre en un punto del eje).
- **Muro de Siegel** $W_{\mathrm{Sieg}} := \{Z : Z$ tiene un cero no real en el eje imaginario$\}$. En él, la órbita del grupo de Klein degenera de tamaño 4 a tamaño 2 ($\{i\beta, -i\beta\}$), y κ puede ser **impar**. Para la clase de $\zeta$ (sin ceros reales de $\zeta$ en $(0,1)$) los caminos relevantes evitan $W_{\mathrm{Sieg}}$; este muro es exactamente el que rompe la paridad en el sentido de "Siegel rompe paridad" (Doc 140).

**[PROP 1.3] (paridad).** En $\mathcal{C} \setminus W_{\mathrm{Sieg}}$, $\kappa \in 2\mathbb{Z}$.

*Prueba.* Los ceros no reales del semiplano superior son permutados por $z \mapsto -\bar z$ (composición de las dos simetrías), que preserva $\operatorname{Im} z$. Fuera de $W_{\mathrm{Sieg}}$ esta involución no tiene puntos fijos en $\{\operatorname{Im} z > 0\}$ (un punto fijo cumple $\operatorname{Re} z = 0$). Un conjunto finito —o cada estrato de un multiconjunto— con involución libre tiene cardinal par. $\square$

Esto re-deriva "δ=1 prohibido" (Doc 132) en lenguaje configuracional: la paridad es un fenómeno de **teoría de grupos del grupo de Klein**, no de positividad.

### 1.3. κ es localmente constante fuera de los muros: el teorema del grado

**[TEOREMA 1.4] (cuantización homotópica de κ).** Sea $u \mapsto F_u$ una familia de funciones enteras reales en $\mathbb{R}$, pares, de orden $\le 1$, no idénticamente nulas, continua en la topología de convergencia uniforme local en $\mathbb{C}$, con configuraciones de ceros $Z_u \in \mathcal{C}$, $\kappa(Z_u) < \infty$ para todo $u$, y camino **propio**. Entonces:

1. $u \mapsto \kappa(Z_u)$ es localmente constante en $\{u : Z_u \notin W_{\mathrm{col}} \cup W_{\mathrm{Sieg}}\}$;
2. en un cruce de $W_{\mathrm{col}}$ en el que un único par conjugado simple aterriza en (o despega de) un punto $x_0 \ne 0$ del eje, κ salta exactamente en $\mp 2$ (el par y su espejo $-x_0$ aterrizan simultáneamente por la paridad de $F$; cada aterrizaje aporta $\mp 1$ al conteo del semiplano superior);
3. κ admite la representación de **grado**: para cualquier rectángulo $R = [a,b] \times [\eta, \tfrac12 + \eta']$ con $\partial R \cap Z_u = \emptyset$ que contenga todos los ceros del semiplano superior estricto,

$$\kappa(Z_u) = \frac{1}{2\pi i} \oint_{\partial R} \frac{F_u'(z)}{F_u(z)}\,dz = \deg\left(\frac{F_u}{|F_u|} : \partial R \to S^1\right).$$

*Prueba.* (3) es el principio del argumento: los ceros dentro de $R$ son exactamente los no reales del semiplano superior (los reales quedan fuera porque $\eta > 0$; la propiedad y $\kappa<\infty$ permiten elegir $R$). (1): por Hurwitz, si $Z_{u_0}$ no toca $\partial R$, para $u$ cerca de $u_0$ el conteo en $R$ es constante; hay que poder mantener $\eta > 0$ fijo: esto falla solo si ceros no reales se acercan al eje, lo que en el límite produce un cero real de multiplicidad $\ge 2$ (los ceros llegan en pares conjugados, y el punto límite real absorbe ambos) — es decir, solo en $W_{\mathrm{col}}$; o si un cero no real cruza $\operatorname{Re} z = 0$... que no cambia el conteo (la involución lo preserva), salvo que esté *sobre* el eje imaginario aterrizando en $0$, caso $W_{\mathrm{Sieg}} \cap W_{\mathrm{col}}$. La propiedad excluye fugas por los lados verticales (se toman $a,b$ fuera del compacto $K$). (2): localmente, cerca del aterrizaje, $F_u(z) = c(u)\,(z - z_+(u))(z - z_-(u))\,G_u(z)$ con $G$ no nula, $z_\pm = x_0(u) \pm i\beta(u)$ antes del cruce y $z_\pm$ reales después; el conteo en un disco pequeño alrededor de $x_0$ baja de 1 (en el semiplano superior) a 0, y la paridad de $F$ duplica el evento en $-x_0$. $\square$

**Lectura.** κ **es** un invariante topológico: el grado de $F/|F|$ sobre el borde de la banda de inestabilidad. No es localmente constante en todo $\mathcal{C}$ — y eso es lo correcto: si lo fuera, el flujo DBN no podría llevar κ a 0. Es localmente constante **entre muros**, y los muros son exactamente los eventos de colisión en el eje crítico. La respuesta a "¿de qué espacio es κ un π₀?": κ clasifica las componentes conexas de $\{$caminos propios$\} \setminus (W_{\mathrm{col}} \cup W_{\mathrm{Sieg}})$, es decir, $\kappa$ es la función localmente constante universal del complemento de los muros (junto con los datos discretos triviales).

### 1.4. El muro es una colisión de Kreĭn: por qué "Maslov" es el nombre correcto

**[PUENTE 1.5] (colisión de signaturas).** Vía el teorema-puente de Phase 26 (κ = neg.ind de la forma de Weil $Q$; los ceros off-line = autovalores no reales del operador $Q$-simétrico $H_C$ en el espacio de Pontryagin $(\mathcal{K}, Q)$), el cruce de $W_{\mathrm{col}}$ es exactamente el mecanismo clásico de **colisión de Kreĭn**: en un espacio con producto indefinido, un par de autovalores reales de un operador $Q$-autoadjunto solo puede abandonar el eje real mediante la colisión de dos autovalores de **signatura de Kreĭn opuesta**; en la colisión se forma un bloque de Jordan y el par sale a $\mathbb{C}$ llevándose un plano hiperbólico (un $+$ y un $-$) del espacio. Esto es el criterio de estabilidad fuerte de Kreĭn (1950) y Gel'fand–Lidskii (1955) para sistemas Hamiltonianos lineales periódicos; exposición moderna: MacKay 1986; marco abstracto: Bognár 1974, Azizov–Iokhvidov 1989. El estatus de puente es honesto: la identificación operatorial completa depende de V.1–V.4 de Phase 26 (abiertas); la versión **configuracional** (Teorema 1.4) es incondicional.

**Esta es la respuesta estructural a la pregunta del director (nivel 1):** las direcciones negativas vienen en paquetes discretos porque *nacen por pares en colisiones de signatura* — el mismo mecanismo por el que los modos inestables de un sistema Hamiltoniano estable no aparecen gradualmente sino por cuantos, en resonancias de Kreĭn. En la física esto produce los teoremas de conteo de índice (Kapitula–Kevrekidis–Sandstede 2004, "Counting eigenvalues via the Krein signature...": el número de modos inestables está acotado por el índice negativo de la energía; criterio de Vakhitov–Kolokolov 1973 como caso escalar). El diccionario es exacto: modos inestables ↔ cuádruplos off-line; índice negativo de la Hessiana de energía ↔ κ = neg.ind(Q); resonancia de Kreĭn ↔ par de Lehmer en el muro.

El nombre "Maslov": el salto de κ en cruces transversales de una codimensión-1 con signo es formalmente un índice de intersección de tipo Maslov (Arnol'd 1967; Robbin–Salamon 1993, índice espectral por cruces). $m = \kappa/2$ es el número de intersección del camino con $W_{\mathrm{col}}$ contado con signo, relativo al estado final κ=0.

### 1.5. El exponente Lehmer = 2 es el pliegue normal del muro

**[PROP 1.6] (forma normal de pliegue).** Sea $u \mapsto F_u$ como en el Teorema 1.4, con un cruce de $W_{\mathrm{col}}$ en $u = u_0$, $x_0$ cero real doble de $F_{u_0}$, y supóngase transversalidad: $\partial_u [\text{discriminante local}] \ne 0$. Entonces existen coordenadas locales en las que los dos ceros son $x_0 \pm \sqrt{c\,(u - u_0)} + O(u-u_0)$, $c \neq 0$. En particular: del lado "real" del muro, el **gap** entre los dos ceros reales escala como $|u - u_0|^{1/2}$, i.e. $\text{gap}^2 \asymp \text{dist al muro}$; del lado "complejo", la **altura** $\beta$ del par escala igual: $\beta^2 \asymp \text{dist al muro}$.

*Prueba.* Weierstrass: localmente $F_u(z) = e(z,u)\,(z^2 + a_1(u) z + a_0(u))$ con $e \ne 0$ y $a_i$ continuas (de clase la de la familia); el cruce es el cero del discriminante $\Delta(u) = a_1^2 - 4a_0$; transversalidad ⟹ $\Delta(u) \sim c'(u-u_0)$; los ceros son $(-a_1 \pm \sqrt{\Delta})/2$. $\square$

**[PUENTE 1.7] (unificación con Doc 143 y LP-134/LP-143).** El "exponente Lehmer = 2 exacto" de Doc 143 (cota Gram–Vandermonde: el coste de un casi-cero-doble entra al cuadrado, con testigo antisimétrico) es la manifestación *estática* del pliegue: la forma cuadrática ve $\text{gap}^2$ porque el muro es cuadrático en la coordenada transversal. Las dos repulsiones conjeturales son las dos distancias laterales al **mismo** muro, normalizadas a la escala local $1/\log\gamma$:

- LP-143 ($\liminf \text{gap}\cdot\log\gamma > 0$): el punto aritmético no se acerca a $W_{\mathrm{col}}$ **desde el lado real** (lado $t = 0^+$ del flujo);
- LP-134 ($\liminf |\beta - \tfrac12|\cdot\log\gamma > 0$, en coordenada $b = \beta_{\mathrm{off}}$): no se acerca **desde el lado complejo** (lado $t = 0^-$).

El "puente heurístico DBN" de Doc 143 (misma frontera) queda así con hogar geométrico: ambas son transversalidad del punto aritmético al muro de colisión, medida en la métrica reescalada por la densidad RvM. *Estatus:* la identificación de las dos coordenadas transversales con los dos lados del mismo muro es un teorema local (Prop 1.6); las repulsiones mismas siguen siendo LP (abiertas, y LP-143 conjeturalmente falsa bajo GUE en su forma uniforme — Doc 143; el módulo correcto es relativo al gap).

---

## 2. Niveles 1→3: la ley de balance de la energía de inestabilidad

Aquí está el contenido nuevo principal del documento. Los Docs 70–72 calcularon $\partial_t T_\lambda$ (una traza *ponderada*) y encontraron una forma cuadrática con cancelación aritmética bajo RH. Leído como física: $T_\lambda$ es una energía de Lyapunov con pesos espectrales. Quitamos los pesos y trabajamos con la energía geométrica desnuda; el resultado es más limpio de lo que los pesos dejaban ver: **la ley es puramente disipativa, con tasa universal cuantizada por κ.**

### 2.1. La dinámica de ceros

**[LEMA 2.1] (buena definición de la dinámica; CSV94, P15, KKL).** Sea $t_0 > 0$ y $J \ni t_0$ un intervalo en el que todos los ceros de $H_t$ son simples. Entonces los ceros admiten parametrizaciones $z_k(t)$ reales-analíticas en $J$ con

$$\dot z_k = 2 \sum_{j \ne k}{}^{\!\!'} \frac{1}{z_k - z_j},$$

donde $\sum'$ es la suma simetrizada (agrupando $z_j$ con $-z_j$, o truncando simétricamente), absolutamente convergente tras el agrupamiento gracias a la densidad RvM ($\sum_j |z_k - z_j|^{-2} < \infty$, y el agrupamiento simétrico reduce los términos lejanos a $O(|z_j|^{-2})$).

*Prueba.* Estándar: $0 = \frac{d}{dt} H_t(z_k(t)) = \partial_t H_t + H_t'\,\dot z_k = -H_t'' + H_t' \dot z_k$ en $z_k$, luego $\dot z_k = H_t''/H_t'(z_k)$, y para una entera de género 1 real y par con ceros simples, $H''/H'(z_k) = 2\sum'_{j\neq k} (z_k - z_j)^{-1}$ (derivada logarítmica del producto de Hadamard; el factor exponencial lineal es nulo por paridad). La versión real es exactamente la ecuación de [RT, §2] y [P15]; la extensión a ceros complejos aislados es idéntica (holomorfía local + función implícita). Por [KKL], para $t > 0$ las hipótesis (finitos no reales, casi todos simples) valen, y los instantes de colisión son localmente finitos. $\square$

### 2.2. La energía de inestabilidad

**[DEFINICIÓN-NUEVA 2.2] (energía de inestabilidad).**

$$I(t) := \sum_{\substack{z_k(t)\,:\, \operatorname{Im} z_k > 0}} (\operatorname{Im} z_k(t))^2 \;=\; \sum_{k \text{ sup}} \beta_k(t)^2 .$$

Es la mitad del segundo momento imaginario total. Para $t > 0$ es una suma finita [KKL]. $I(t) = 0 \iff \kappa(t) = 0$, y $\Lambda = \inf\{t : I(t) = 0\}$ — la versión geométrica del Teorema 4.1 de Doc 70 ($\Lambda$ como tiempo de extinción de $T_\lambda$).

### 2.3. La ley de balance

**[TEOREMA 2.3] (ley de balance, disipación pura con tasa cuantizada).** Sea $J$ un intervalo de tiempos $> 0$ en el que $\kappa(t) \equiv \kappa$ es finito y constante y todos los ceros son simples. Escribimos $z_k = \alpha_k + i\beta_k$ ($\beta_k > 0$) para los ceros del semiplano superior y $x_j$ para los reales. Entonces, en $J$:

$$\boxed{\;\frac{dI}{dt} \;=\; -\,2\,\kappa(t)\;-\;D(t), \qquad D(t) \ge 0\;}$$

con disipación explícita

$$D(t) = 4\sum_{k \text{ sup}} \beta_k^2 \left[ \sum_{x_j \in \mathbb{R}} \frac{1}{|z_k - x_j|^2} + \frac{1}{2|z_k|^2} \right] \;+\; 2\sum_{\substack{k \ne l \text{ sup}}} \left[ \frac{(\beta_k - \beta_l)^2}{|z_k - z_l|^2} + \frac{(\beta_k - \beta_l)^2}{|z_k + \bar z_l|^2} + \frac{(\beta_k + \beta_l)^2}{|z_k - \bar z_l|^2} + \frac{(\beta_k + \beta_l)^2}{|z_k + z_l|^2} \right]$$

(suma sobre pares ordenados; cada sumando es manifiestamente $\ge 0$; si $z_k$ está en el eje imaginario los términos espejo coincidentes se cuentan una vez).

*Prueba.* Por el Lema 2.1, $\dot\beta_k = \operatorname{Im} \dot z_k = -2\sum_{w \in Z \setminus \{z_k\}} \dfrac{\beta_k - \operatorname{Im} w}{|z_k - w|^2}$, luego

$$\frac{dI}{dt} = \sum_{k \text{ sup}} 2\beta_k \dot\beta_k = -4 \sum_{k \text{ sup}} \sum_{w \ne z_k} \frac{\beta_k(\beta_k - \operatorname{Im} w)}{|z_k - w|^2}.$$

Clasificamos $w$:

1. **El conjugado propio $w = \bar z_k$:** $\beta_k(\beta_k - (-\beta_k))/|2i\beta_k|^2 = 2\beta_k^2/4\beta_k^2 = \tfrac12$. Contribución: $-4 \cdot \tfrac12 = -2$ **por cada cero superior**, total $-2\kappa(t)$. *Este es el término universal: no depende de dónde esté el cero, solo de que exista.*
2. **El espejo $w = -\bar z_k$:** $\operatorname{Im} w = \beta_k$, contribución $0$.
3. **El antípoda $w = -z_k$:** $\beta_k(2\beta_k)/|2z_k|^2 = \beta_k^2/(2|z_k|^2)$; contribución $-2\beta_k^2/|z_k|^2 \le 0$.
4. **Ceros reales $w = x_j$:** $\beta_k^2/|z_k - x_j|^2$; contribución $-4\beta_k^2 \sum_j |z_k - x_j|^{-2} \le 0$ (convergente por RvM).
5. **Otros ceros superiores y sus órbitas** $w \in \{z_l, \bar z_l, -z_l, -\bar z_l\}$, $l \ne k$: los términos con $\operatorname{Im} w = \beta_l$ dan $\beta_k(\beta_k - \beta_l)/d^2$ con $d \in \{|z_k - z_l|, |z_k + \bar z_l|\}$, simétricos al intercambiar $k \leftrightarrow l$; sumando los pares ordenados $(k,l)$ y $(l,k)$: $\beta_k(\beta_k - \beta_l) + \beta_l(\beta_l - \beta_k) = (\beta_k - \beta_l)^2$. Los términos con $\operatorname{Im} w = -\beta_l$ dan análogamente $(\beta_k + \beta_l)^2$ con $d \in \{|z_k - \bar z_l|, |z_k + z_l|\}$. Todos $\le 0$ tras simetrizar.

Sumando, $dI/dt = -2\kappa - D$ con $D \ge 0$ como en el enunciado. La convergencia absoluta de cada bloque está garantizada por $\kappa < \infty$ y RvM. $\square$

**Comentarios estructurales.**

- **La tasa universal $-2\kappa$ es la cuantización dinámica del índice:** cada modo inestable disipa energía de inestabilidad a tasa exactamente 2, por su interacción con su propio conjugado, *independientemente de la configuración*. La energía no puede gotear: se pierde en cuantos de pendiente 2 por modo.
- **No hay término fuente.** Esto responde la pregunta central del mandato (punto 2): bajo el flujo DBN no existe "fuente aritmética" que alimente inestabilidad. La ley es disipativa pura. Los primos **no son una fuerza** sobre los ceros: el flujo del calor no sabe aritmética. Toda la aritmética está en la **condición inicial** $Z_0$ (y, dualmente, en la representación de Weil de esa condición inicial: Doc 72). Véase §4.
- **Monotonía de Conj. 5.1 de Doc 70, resuelta en la versión geométrica:** $I$ es estrictamente decreciente mientras $\kappa > 0$. (La monotonía de la traza ponderada $T_\lambda$ sigue abierta; los pesos pueden romperla localmente, pero la energía desnuda no.)

### 2.4. Corolarios: viriales para Λ

**[COR 2.4] (cota de extinción).** Si en $(t_0, \Lambda)$ los tiempos de colisión son localmente finitos y $\kappa < \infty$ (cierto para $t_0 > 0$ por [KKL]), entonces, puesto que $\kappa(t) \ge 2$ para todo $t < \Lambda$ (paridad, Prop 1.3, y $\kappa > 0$ por definición de $\Lambda$):

$$\frac{dI}{dt} \le -4 \quad \text{en } (t_0, \Lambda) \qquad\Longrightarrow\qquad \Lambda \;\le\; t_0 + \tfrac14\, I(t_0).$$

($I$ es continua a través de las colisiones: los ceros se mueven continuamente y en un aterrizaje el término que se extingue tiende a 0.) En particular, si $\kappa(0) < \infty$ (la mitad de finitud, **no probada**): $\Lambda \le \tfrac14 I(0^+) \le \tfrac14 \cdot \kappa(0)\cdot \sup_k \beta_k(0)^2 \le \kappa(0)/16$, usando $\beta \le 1/2$. *Honesto:* esta cadena es **condicional a $m < \infty$**; no compite con [dB]/[KKL] (incondicionales) salvo cuando $\kappa(0)$ es pequeño, y es del mismo espíritu "energético" que el método de barrera de [P15].

**[COR 2.5] (la frontera $\Lambda = 0$ como balance energético; reformulación de Rodgers–Tao).** Por [RT], $\Lambda \ge 0$, luego $\kappa(t) > 0$ para todo $t < 0$. En cualquier intervalo $(t, 0)$ con dinámica bien definida y $\kappa$ finito, el Teorema 2.3 da $I(t) \ge I(0^+) + 4|t|$; si $\kappa$ o $I$ son infinitos en $(t,0)$ la conclusión vale trivialmente. Es decir:

$$I(t) \;\ge\; 4\,|t| \qquad \text{para todo } t < 0,$$

y RH equivale a que esta cota lineal sea *exacta en el borde*: RH $\iff I(0^+) = 0 \iff$ la energía de inestabilidad del punto aritmético, mirada hacia atrás en el tiempo, despega de cero con pendiente mínima universal $4$. El punto aritmético está **exactamente en la frontera del basin** no como metáfora: es el punto donde el funcional de Lyapunov toca cero con la pendiente cuantizada mínima.

**[PROP 2.6] (el pliegue dinámico: Lehmer = 2 otra vez).** En un aterrizaje aislado en $t_c$ ($\beta_k(t_c) = 0$, demás ceros a distancia $\ge d > 0$), la ecuación de $\beta_k$ es $\dot\beta_k = -1/\beta_k + O(1)$, luego

$$\beta_k(t)^2 = 2\,(t_c - t)\,(1 + o(1)), \qquad t \to t_c^-,$$

y simétricamente el gap real tras el aterrizaje se abre como $\mathrm{gap}(t)^2 \asymp (t - t_c)$. *Prueba:* el término propio domina ($-1/\beta_k \to -\infty$) y la EDO $\beta\dot\beta = -1 + O(\beta)$ se integra. $\square$

El exponente $1/2$ ($\beta \sim \sqrt{2(t_c - t)}$) es el **mismo pliegue** de la Prop 1.6: el muro estático (Gram–Vandermonde, Doc 143) y el aterrizaje dinámico tienen la misma forma normal. El "2" de Lehmer es el grado del discriminante en la coordenada transversal al muro — un solo objeto visto en dos cartas (estática $u$, dinámica $t$). Y CSV 1994 cierra el círculo por el otro lado: los pares de Lehmer (casi-colisiones en $t=0$) fuerzan cotas inferiores para $\Lambda$ — i.e., estar *cerca del muro por el lado real en $t=0$* implica *haber estado del lado complejo para $t<0$ apenas anterior* — exactamente la lectura de dos lados del mismo muro del Puente 1.7.

### 2.5. ¿Qué se conserva?

Respuesta honesta y completa:

1. **La paridad de κ** (fuera de $W_{\mathrm{Sieg}}$): conservada absolutamente. Trivial pero no vacía: es lo que prohíbe el escape "de a uno".
2. **κ entre muros:** conservado (Teorema 1.4) — κ es la "carga topológica" y los muros son los únicos vértices de des-excitación. Junto con el signo del cruce: bajo DBN los cruces son **solo de bajada** ([dB]: realidad absorbente; nuestro Cor 2.4 lo cuantifica). κ es un entero monótono escalonado: la des-excitación en cascada de un sistema cuantizado.
3. **No hay momento conservado no trivial.** El primer momento $\sum' z_k$ se conserva (= 0 por simetría, trivial). El candidato $I$ **no** se conserva: decrece — y esa es la tesis: la estructura correcta no es una ley de conservación sino un **par de Lyapunov $(\kappa, I)$** con leyes unilaterales acopladas: κ escalonado no-creciente, $I$ absolutamente continua con $\dot I = -2\kappa - D$. La identidad de los Docs 70–72 ($\partial_t T_\lambda|_{t=0}$ como forma cuadrática con cancelación exacta bajo RH) es la sombra ponderada de esta ley: bajo RH, $\kappa = 0$, $I \equiv 0$, y la "cancelación aritmética exacta" del Doc 72 es la afirmación de que la representación prima de la condición inicial no tiene componente de inestabilidad — i.e., positividad de Weil. La ley de balance no la prueba; la *localiza* como dato inicial.

---

## 3. Nivel 2 caracterizado dinámicamente: la finitud como no-explosión en la frontera

No probamos $m < \infty$ (mandato). La caracterizamos.

**[PROP 3.1] (regularización instantánea, incondicional).** Para todo $t > 0$: $\kappa(t) < \infty$ e $I(t) < \infty$. *Prueba:* [KKL]. $\square$

Es decir: el flujo aterriza **instantáneamente** en el estrato de índice finito. Toda la dificultad de nivel (2) es el comportamiento en $t \to 0^+$:

**[PROP 3.2] (la mitad de finitud como condición de frontera).**

1. $\kappa(0) < \infty \implies \kappa(t) \le \kappa(0)$ para $t \ge 0$ y $\limsup_{t\to 0^+}\kappa(t)<\infty$ (los ceros no reales de $H_t$ para $t$ pequeño provienen, por Hurwitz, de los no reales de $H_0$ o de colisiones de reales; bajo el flujo las colisiones solo *destruyen* pares — [dB]).
2. $I(0^+) := \lim_{t \to 0^+} I(t)$ existe en $[0,\infty]$ ($I$ es monótona), y $I(0^+) < \infty \iff \int_0^s [2\kappa(u) + D(u)]\,du < \infty$: la finitud de la *energía* inicial es la **integrabilidad de κ en la frontera**, no su acotación.
3. $I(0^+) < \infty$ es **estrictamente más débil** que $\kappa(0) < \infty$: el contraejemplo de Hadamard del Doc 144 (clase analítica, $m = \infty$, alturas $\delta_j = e^{-\gamma_j}$) tiene $\sum_j \delta_j^2 < \infty$, i.e. energía de inestabilidad finita con índice infinito.

*Prueba de 3:* inmediata de la definición de $I$. $\square$

**Lectura (nueva estratificación cuantitativa del nivel 2).** Entre "κ(0) = 0" (RH) y "κ(0) < ∞" (mitad de finitud) y "ninguna condición" hay un escalón intermedio genuino: $I(0^+) < \infty$ (energía finita, índice posiblemente infinito). La jerarquía
$$\kappa(0)=0 \;\subsetneq\; \kappa(0)<\infty \;\subsetneq\; I(0^+)<\infty \;\subsetneq\; \mathcal{C}$$
es estricta en la clase analítica (Doc 144 separa los dos del medio). Pregunta abierta apuntada, más débil que $m<\infty$ y quizá atacable por la vía Fredholm de B.4:

**[GAP 167.A] ¿Es $I(0^+) < \infty$ demostrable para ζ?** Equivalentemente: ¿es $\kappa(t)$ integrable en $t \to 0^+$? Nótese que es una afirmación de tipo "promedio en $t$", del lado bueno del cuantificador maestro (la observación clave de Phase 44: el espectro esencial vive del lado promedio); y que $I(0^+)<\infty$ es exactamente "$\sum_j b_j^2 < \infty$ sobre los ceros off", la versión $\ell^2$ de la finitud — el análogo cuadrático de la mitad de finitud, en la misma coordenada donde el exponente Lehmer es 2. [DESEO: que B.4 (positividad esencial módulo compactos) implique la versión $\ell^2$ antes que la versión de conteo.]

---

## 4. ¿Por qué pares y no continuo? — qué añade la aritmética

Respuesta en tres capas, con la honestidad exigida:

**(a) La discretitud es barata.** Cualquier objeto de la clase de ξ (entera de orden 1, real en la línea, ecuación funcional) tiene ceros aislados; la "negatividad" de la forma de Weil asociada está soportada en átomos (cada cuádruplo aporta un plano hiperbólico de dimensión finita al espacio negativo — Phase 26/44). Una "densidad continua de negatividad" exigiría espectro no-real continuo, imposible para una entera no nula. **Esto no es profundo:** es Hadamard. En la clase analítica la cuantización es gratis.

**(b) La paridad y el empaquetamiento son simetría, no aritmética.** κ ∈ 2ℤ es el grupo de Klein (Prop 1.3); el nacimiento/muerte por pares es la colisión de Kreĭn (Puente 1.5) — válida para cualquier $Q$-dinámica, sin un solo primo.

**(c) La finitud es lo único que la aritmética debe pagar — y es la mitad Fredholm otra vez. Lo decimos sin adornos.** El contraejemplo del Doc 144 muestra $m = \infty$ realizable analíticamente: ningún argumento de carga topológica en la clase analítica puede dar κ < ∞. Lo que la aritmética añade no es un mecanismo de cuantización extra, sino (conjeturalmente) una **obstrucción de compacidad**: B.4 (Doc 132) dice que positividad esencial módulo compactos ⟹ δ < ∞; el contenido aritmético necesario es que el "símbolo" de la forma de Weil (la parte que ven los primos en promedio) sea positivo, dejando la negatividad en un compacto. El presente documento añade a ese cuadro solo dos cosas: (i) la versión dinámica — la finitud es una condición de **frontera del flujo** ($\kappa(t)$ acotado o al menos integrable en $t\to 0^+$, Prop 3.2), no una condición estática misteriosa: el interior $t>0$ ya es finito gratis [KKL]; (ii) el escalón intermedio $I(0^+)<\infty$ (GAP 167.A), que es la forma $\ell^2$ —no de conteo— de la finitud, y por tanto el primer candidato si la ruta es espectral-esencial. Veredicto honesto del punto 3 del mandato: **"nada nuevo" en cuanto a mecanismo de cuantización; la finitud es Fredholm; lo nuevo es la coordenada (frontera del flujo, norma $\ell^2$) en la que la mitad Fredholm debe medirse.**

---

## 5. Test anti-circularidad

Aplicado a cada objeto construido:

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde reentra ζ |
|---|---|---|---|
| $\mathcal{C}$, muros, Teorema 1.4 (κ grado) | sí | **sí** (vale para toda la clase) | no reentra |
| Colisión de Kreĭn (versión configuracional) | sí | sí | no reentra; la versión operatorial hereda V.1–V.4 |
| Pliegue / Lehmer = 2 (Props 1.6, 2.6) | sí | sí | no reentra |
| **Ley de balance** $\dot I = -2\kappa - D$ (Thm 2.3) | **sí** | **sí** (calor + Hadamard; ni un primo en la prueba) | no reentra |
| Cor 2.5 ($I(t) \ge 4|t|$, $t<0$) | sí | **no**: usa [RT] | ζ entra por Rodgers–Tao (estadística local de ceros) |
| **Valor** $I(t_0)$, $I(0^+)$, $\kappa(0)$ | — | **no**: computarlos = conocer los ceros | en la condición inicial |

**El patrón predicho se confirma y se localiza con precisión.** La LEY (la ecuación de movimiento de la inestabilidad) es RH-libre y de hecho ζ-libre: es un teorema de la clase de Pólya. El VALOR inicial no lo es — y *no puede* serlo: por Phase 52, ζ ES la dualidad, y la condición inicial del flujo es exactamente el lado "ceros" de la dualidad. La novedad respecto de Phase 52 es la separación limpia: allí cada estructura auxiliar reintroducía ζ en su núcleo; aquí hay una estructura (la dinámica) que demostradamente **no** contiene ζ, y un dato (la condición inicial) que lo contiene **todo**. Es exactamente "conocer la ecuación de movimiento sin la condición inicial".

Dos matices que impiden inflar la conclusión:

1. **Avatares computables RH-libres del dato inicial existen, pero con signo, no con cuadrado.** Los coeficientes de Li $\lambda_n = \sum_\rho [1 - (1 - 1/\rho)^n]$ (Li 1997; Bombieri–Lagarias 1999) y los valores $(\log\xi)''(\tfrac12) = -\sum_\rho (\rho - \tfrac12)^{-2}$ son computables sin conocer los ceros (desde los coeficientes de Taylor de $\log\xi$, i.e. constantes de Stieltjes — RH-libres), y son *momentos firmados* de la misma configuración cuyo *momento cuadrático positivo* es $I(0)$. La obstrucción exacta: extraer de los momentos holomorfos firmados la cantidad definida-positiva $\sum b_j^2$ es el problema de positividad de siempre (RH ⟺ $\lambda_n \ge 0$). El muro no se movió; quedó localizado en "momento firmado → momento cuadrático".
2. **El único enunciado dinámico con contenido aritmético (Cor 2.5) hereda su aritmética íntegramente de [RT].** No hay aritmética nueva en este documento; la hay *importada* y separada del resto.

---

## 6. Veredicto

### Teoremas nuevos (nivel 1 y ley de balance)

- **[TEOREMA 1.4 + Props 1.3, 1.6]** κ es un invariante topológico genuino: grado de $F/|F|$ sobre el borde de la banda de inestabilidad, localmente constante en caminos propios fuera de dos muros explícitos ($W_{\mathrm{col}}$, $W_{\mathrm{Sieg}}$), con saltos $\pm 2$ en cruces transversales y forma normal de pliegue — lo que identifica el exponente Lehmer = 2 (Doc 143) como el grado del discriminante del muro, y LP-134/LP-143 como las dos distancias laterales al mismo muro (Puente 1.7). La pregunta "¿de qué es κ un π₀?" tiene respuesta: del complemento de los muros en el espacio de caminos propios de $\mathcal{C}$.
- **[TEOREMA 2.3]** Ley de balance: $\dot I = -2\kappa - D$, $D \ge 0$ explícita; disipación pura con **tasa universal cuantizada $-2$ por modo inestable** (proveniente de la interacción de cada cero con su propio conjugado), sin término fuente. Corolarios: monotonía estricta de $I$ (resuelve la versión geométrica de Conj. 5.1, Doc 70); virial $\Lambda \le t_0 + I(t_0)/4$ (Cor 2.4); pliegue dinámico $\beta^2 = 2(t_c - t)(1+o(1))$ (Prop 2.6).
- **[PROP 3.2]** Estratificación nueva del nivel 2: $\kappa(0)<\infty \subsetneq I(0^+)<\infty$ (estricto por Doc 144); la mitad de finitud es una condición de frontera del flujo (el interior es finito incondicionalmente por [KKL]); GAP 167.A ($I(0^+)<\infty$, la finitud $\ell^2$) nombrado como objetivo estrictamente más débil que $m<\infty$ y del lado "promedio" del cuantificador maestro.

### Reformulaciones (lenguaje nuevo, muro viejo — declaradas como tales)

- **La frontera $\Lambda = 0$ como balance energético** (Cor 2.5): RH ⟺ la energía de inestabilidad, mirada hacia atrás desde el punto aritmético, despega con la pendiente mínima cuantizada ($I(t) \ge 4|t|$, $t<0$, vía [RT]). No es más fácil que RH; es la misma frontera con estructura de prueba de estabilidad.
- **"No hay fuente aritmética":** los primos no son una fuerza del flujo sino la representación dual (Weil, Doc 72) de la condición inicial; la pregunta del director "¿por qué la fuente no alimenta inestabilidad en $t=0$?" se transforma en: "¿por qué la representación prima del dato inicial carece de componente de inestabilidad?" = positividad de Weil. Localización, no progreso.
- **Cuantización (punto 3 del mandato):** mecánicamente resuelta y deflacionada — discretitud = Hadamard, paridad = Klein, pares = colisión de Kreĭn; la aritmética solo es necesaria (y suficiente, si B.4 se realizara) para la **finitud**, que es la mitad Fredholm otra vez. Dicho sin adornos, como exige el contrato.

### Herramientas de estabilidad apuntadas al hueco, con condiciones precisas

1. **Łojasiewicz–Simon** (Łojasiewicz 1963; Simon 1983): el flujo DBN es gradiente de $E_{\log}$ (Phase 28). Una desigualdad de Łojasiewicz en la configuración RH daría tasas de aterrizaje y rigidez del basin. **Condición de aplicabilidad exacta: Hessiana de $E_{\log}$ Fredholm en la configuración límite** — que es *literalmente* B.4/la mitad de finitud. Las dos mitades del programa ("m<∞" y "m<∞⟹m=0") se encuentran en la hipótesis y en la conclusión de un solo teorema de estabilidad: este es el punto de soldadura más limpio que conocemos.
2. **Teoremas de conteo de índice Hamiltonianos** (Kreĭn 1950; Gel'fand–Lidskii 1955; MacKay 1986; Vakhitov–Kolokolov 1973; Grillakis–Shatah–Strauss 1987; Kapitula–Kevrekidis–Sandstede 2004): el diccionario κ = índice negativo de la energía ⟹ cota sobre modos inestables es exactamente la dirección "(1) acotar antes de excluir". Condición de aplicabilidad: la identificación operatorial de Phase 26 (V.1–V.4); mientras tanto, la versión configuracional (este doc) ya da el conteo.
3. **Identidades viriales:** realizada aquí (Cor 2.4/2.5): $I$ es el virial correcto del flujo, con pendiente cuantizada. Lo que un virial no puede hacer: distinguir $I(0^+) = 0$ de $I(0^+)$ pequeño — esa es la condición inicial, i.e. el muro.

### [GAPs] declarados

- **GAP 167.A:** ¿$I(0^+) < \infty$ para ζ? (finitud $\ell^2$; más débil que $m<\infty$).
- **GAP 167.B:** monotonía de la traza ponderada $T_\lambda(t)$ (Conj. 5.1 Doc 70) — la versión desnuda está resuelta (Thm 2.3); la ponderada requiere controlar el conmutador de los pesos con la disipación.
- **GAP 167.C:** la versión operatorial del muro (colisión de Kreĭn para $H_C$ en $(\mathcal{K},Q)$) hereda V.1–V.4 de Phase 26.
- **[GAP de literatura]:** la monotonía del *conteo* de ceros no reales bajo el flujo (usada solo en Prop 3.2.1 vía [dB]) está en de Bruijn 1950 para la realidad absorbente; la versión cuantitativa por pares que usamos se deriva aquí de la dinámica (Lema 2.1), no de la literatura; y no conocemos referencia que enuncie la ley $\dot I = -2\kappa - D$ — la tasa universal $-2$ por modo podría ser conocida en la comunidad de flujos de Calogero/calor sobre ceros, no la hemos visto escrita.

### Referencias

de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226. — Newman, C.M. (1976), *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129. — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306. — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6. — Polymath, D.H.J. (2019), *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. 6, 31. — Kreĭn, M.G. (1950), sobre estabilidad fuerte de sistemas Hamiltonianos lineales periódicos (Dokl. Akad. Nauk SSSR 73). — Gel'fand, I.M., Lidskii, V.B. (1955), Uspekhi Mat. Nauk 10 (trad. AMS Transl. 8, 1958). — MacKay, R.S. (1986), *Stability of equilibria of Hamiltonian systems*, en Nonlinear Phenomena and Chaos. — Bognár, J. (1974), *Indefinite Inner Product Spaces*, Springer. — Azizov, T.Ya., Iokhvidov, I.S. (1989), *Linear Operators in Spaces with an Indefinite Metric*, Wiley. — Arnol'd, V.I. (1967), *Characteristic class entering in quantization conditions*, Funct. Anal. Appl. 1, 1–13. — Robbin, J., Salamon, D. (1993), *The Maslov index for paths*, Topology 32, 827–844. — Vakhitov, N.G., Kolokolov, A.A. (1973), Radiophys. Quantum Electron. 16, 783–789. — Grillakis, M., Shatah, J., Strauss, W. (1987), *Stability theory of solitary waves in the presence of symmetry I*, J. Funct. Anal. 74, 160–197. — Kapitula, T., Kevrekidis, P.G., Sandstede, B. (2004), *Counting eigenvalues via the Krein signature in infinite-dimensional Hamiltonian systems*, Physica D 195, 263–282. — Li, X.-J. (1997), *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65, 325–333. — Bombieri, E., Lagarias, J.C. (1999), *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory 77, 274–287. — Łojasiewicz, S. (1963), *Une propriété topologique des sous-ensembles analytiques réels*, Colloques CNRS 117. — Simon, L. (1983), *Asymptotics for a class of non-linear evolution equations*, Ann. of Math. 118, 525–571.
