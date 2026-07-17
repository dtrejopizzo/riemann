# Documento 101 — Interpolación de Fourier y estructura de frame de $\{e^{i\gamma_n s}\}$

**Programa:** Hipótesis de Riemann — Fase 35 (cinco frentes)
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Docs 70, 71, 72, 76, 82, 83, 85, 89; P39; meta-docs DISCRIMINATOR-hardening-phase-A, NOVEL-STRUCTURE-SEARCH-survivors

---

## Resumen

Este documento audita el frente de **interpolación de Fourier** (Radchenko–Viazovska, Bondarenko–Radchenko–Seip, Kulikov–Nazarov–Sodin), identificado en NOVEL-STRUCTURE-SEARCH-survivors como la teoría **dual** de la rigidez cuasicristalina (Kurasov–Sarnak) y no auditada hasta ahora. Se responden seis preguntas: (i) la estructura exacta del sistema $\{e^{i\gamma_n s}\}$ en $L^2(W_\lambda\,dm_\infty)$ — se demuestra, incondicionalmente, que el sistema es completo pero **no es Bessel, no es frame, no es sucesión de Riesz, no es minimal y no es sucesión de interpolación**; (ii) la traducción de cada nivel de la jerarquía en enunciados sobre $d\nu$, incluyendo una **nueva condición equivalente a RH** (Condición 9: anulación de $(W_\lambda d\nu)^\wedge$ en los propios $\gamma_n$); (iii) el análisis del input modular de la maquinaria RV/BRS frente a los muros MW-2 y MW-7 — la conclusión es que la modularidad de $\theta$ **es** la ecuación funcional de $\zeta$ en ropaje automorfo y **no** inyecta información aritmética que evada MW-2; (iv) el problema de unicidad tipo Heisenberg para $d\nu$, con detección explícita de la circularidad (la fórmula explícita aplicada a $d\nu$ reproduce la descomposición del Doc 72); (v) el paso por el discriminador del programa: **FAIL I2b**, el perfil exacto de Connes; (vi) veredicto: **RUTA CERRADA** como palanca hacia RH, con dos subproductos incondicionales que se incorporan al programa.

---

## §0. Notación y marco

Fijamos la notación del programa (Docs 70, 83, 89):

- $dm_\infty(s) = (2\pi)^{-2}\,|\Gamma(1/4 + is/2)|^2\,ds$ sobre $\mathbb{R}$.
- $dm_{full} = |\zeta(1/2+is)|^2\,dm_\infty$; $dm_{full,on} = |\zeta_{on}(1/2+is)|^2\,dm_\infty$, donde $\zeta_{on}$ tiene los ceros de $\zeta$ proyectados a la recta crítica.
- $d\nu = dm_{full} - dm_{full,on} = (R-1)\,dm_{full,on} \geq 0$ incondicionalmente (Doc 83), con $R = \prod_{j:\delta_j>0}\big(1 + \delta_j^2/(s-\gamma_j)^2\big)^2 \geq 1$.
- $W_\lambda(s) = \sum_{k \leq N(\lambda)} k|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2 \geq 0$ el kernel de Abel de la base de Jacobi $\{P_k\}$ de $L^2(dm_{full,on})$ (Doc 70).
- $T_\lambda = \int W_\lambda\,d\nu \geq 0$; **RH $\iff T_\lambda = 0\ \forall\lambda$** (P39; Doc 89, Teorema 10.1).
- $\mu_\lambda := W_\lambda\,dm_\infty$, medida finita sobre $\mathbb{R}$ (Doc 85, §5.1, Paso 1). Escribimos $e_\gamma(s) := e^{i\gamma s}$ y $\widehat{\mu}(r) := \int e^{irs}\,d\mu(s)$.
- $\{\gamma_n\}_{n\geq 1}$: partes imaginarias positivas de los ceros no triviales de $\zeta$, **siempre reales** (Doc 85, Prop. 4.1), con $N(T) = \#\{n : \gamma_n \leq T\} = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T)$ incondicionalmente (Riemann–von Mangoldt).

**Resultado de partida (Doc 85, Teorema 5.1, módulo ítem V.1).** El sistema $\{e_{\gamma_n}\}$ es completo en $L^2(\mu_\lambda)$, incondicionalmente, vía Carlson–Beurling. El gap técnico V.1 (verificación de las hipótesis del argumento de Carlson para funciones enteras de tipo $\leq \pi/4$ con densidad de ceros reales logarítmicamente divergente) sigue abierto y se **hereda** en todo enunciado de este documento que use la completitud.

---

## §1. Literatura verificada: enunciados exactos y condicionalidad

Todos los enunciados de esta sección fueron verificados contra las fuentes el 2026-06-09. Donde la verificación es parcial se marca explícitamente.

### 1.1. Radchenko–Viazovska (Publ. Math. IHÉS 129, 2019)

**Teorema RV (verificado, tal como lo citan BRS, Teorema A y ecs. (1.4)–(1.5)).** Existe una sucesión de funciones de Schwartz pares $a_n : \mathbb{R} \to \mathbb{R}$ tal que para toda $f$ de Schwartz par:
$$f(x) = \sum_{n=0}^\infty f(\sqrt{n})\,a_n(x) + \sum_{n=0}^\infty \widehat{f}(\sqrt{n})\,\widehat{a_n}(x),$$
con convergencia absoluta, y con propiedades interpolatorias $a_n(\sqrt{m}) = \delta_{nm}$, $\widehat{a_n}(\sqrt{m}) = 0$ para $m \geq 1$, más las relaciones en $x=0$: $a_0(0)=\widehat{a_0}(0)=1/2$, $a_{n^2}(0) = -\widehat{a_{n^2}}(0) = -1$, $a_n(0) = -\widehat{a_n}(0) = 0$ en los demás casos.

**Construcción:** las $a_n$ se obtienen de integrales de contorno de formas modulares débilmente holomorfas de peso $3/2$ para el grupo theta $\Gamma_\theta$. **Incondicional.** Observación verificada (BRS, p. 4): evaluada en $x = 0$, la fórmula RV **se reduce a la fórmula de sumación de Poisson** — las relaciones (1.5) son exactamente la corrección que hace consistente la fórmula con Poisson.

### 1.2. Bondarenko–Radchenko–Seip (Constr. Approx., 2023; arXiv:2005.02996, verificado sobre el texto)

Espacio: $\mathcal{H}_1$ = funciones $f$ analíticas en la franja $|\mathrm{Im}\,z| < 1/2 + \varepsilon$ con $\sup_{|y|<1/2+\varepsilon}\int |f(x+iy)|(1+|x|)\,dx < \infty$.

**Teorema BRS 1.1 (INCONDICIONAL; verificado).** Existen funciones enteras pares de decaimiento rápido $U_n(z)$ ($n \geq 1$) y $V_{\rho,j}(z)$ ($0 \leq j < m(\rho)$, $\rho$ recorriendo los ceros no triviales de $\zeta$ con parte imaginaria positiva, $m(\rho)$ = multiplicidad) tales que para toda $f \in \mathcal{H}_1$ par y todo $z$ con $|\mathrm{Im}\,z| < 1/2$:
$$f(z) = \sum_{n=1}^\infty \widehat{f}\Big(\frac{\log n}{4\pi}\Big)\,U_n(z) + \lim_{k\to\infty}\sum_{0<\gamma\leq T_k}\sum_{j=0}^{m(\rho)-1} f^{(j)}\Big(\frac{\rho - 1/2}{i}\Big)\,V_{\rho,j}(z),$$
con propiedades interpolatorias duales (1.3): $\widehat{U_n}(\frac{\log n'}{4\pi}) = \delta_{nn'}$, $U_n^{(j)}(\frac{\rho-1/2}{i}) = 0$, $V_{\rho,j}^{(j')}(\frac{\rho'-1/2}{i}) = \delta_{(\rho,j),(\rho',j')}$, $\widehat{V_{\rho,j}}(\frac{\log n}{4\pi}) = 0$.

**Punto crítico de condicionalidad (verificado).** El teorema es **incondicional**: no asume RH ni simplicidad. Los nodos son $\frac{\rho-1/2}{i} = \gamma - i(\beta - 1/2)$ para $\rho = \beta + i\gamma$: son **reales si y solo si $\beta = 1/2$**. Bajo $\neg$RH la fórmula sigue valiendo, con nodos complejos dentro de la franja. La lectura de BRS como "muestreo no redundante de $f$ y $\widehat{f}$ a lo largo de dos sucesiones reales" (la respuesta a la pregunta tipo Shannon) **sí es condicional a RH + simplicidad de ceros** — los autores lo dicen textualmente ("Assuming for a moment the truth of the Riemann hypothesis and that all the zeta zeros are simple…").

**Corolario BRS 1.1 (incondicional; verificado).** (i) Si $f \in \mathcal{H}_1$ par satisface $\widehat{f}(\frac{\log n}{4\pi}) = 0$ para todo $n \geq 1$ y $f^{(j)}(\frac{\rho-1/2}{i}) = 0$ para todos $\rho, j$, entonces $f \equiv 0$. (ii) Una $f \in \mathcal{H}_1$ par divisible por $\zeta(1/2+is)$ queda determinada por los valores $\widehat{f}(\frac{\log n}{4\pi})$.

**No-redundancia (verificado):** el teorema y el corolario "se rompen si se quita un solo punto" de $\{\frac{\log n}{4\pi}\}$ o del multiconjunto de ceros. El sistema BRS es **exactamente crítico**.

**Mecanismo (verificado, §1 y §4 de BRS):** el kernel es $H(w,s) = \frac{\zeta(s)}{\zeta(w)}\,D(w,s)$, con $D(w,s) = \sum_n \beta_n(s)n^{-w/2}$ una serie de Dirichlet cuyos coeficientes provienen de **integrales modulares para el grupo theta** (principio de abundancia de Knopp reforzado). Los ceros de $\zeta$ entran como **polos de $1/\zeta(w)$**: la posición de los nodos es un output del kernel, no un input de la maquinaria modular.

**Relación con la fórmula de Riemann–Weil (verificado, BRS pp. 3–4 y §4.4).** Cita textual (traducida): *"la deducción de la fórmula de Riemann–Weil parte de la representación en producto de Euler de $\zeta(s)$, mientras que la fórmula (1.2) está atada a la representación en serie de Dirichlet de $\zeta(s)$. Podemos pensar las dos fórmulas como expresando respectivamente una relación de dualidad multiplicativa y una aditiva entre los ceros de zeta y una sucesión distinguida de enteros."* Y además: *"el lado izquierdo de (1.1) define un funcional lineal sobre $\mathcal{H}_1$, mientras que el lado derecho da la representación de este funcional respecto a las funciones base del Teorema 1.1."* Es decir: **la fórmula explícita de Weil ES un funcional lineal representado en la base BRS**. Esto será central en §5 y §6.

### 1.3. Kulikov; Kulikov–Nazarov–Sodin

- **Kulikov** (arXiv:2005.12836): principio de incertidumbre / cota de densidad para bases de interpolación de Fourier. BRS afirman (p. 5, verificado): *"hay una correspondencia precisa entre la condición de densidad de Kulikov y la fórmula de Riemann–von Mangoldt para la densidad de los ceros no triviales de zeta y de funciones $L$."* La constante exacta de la desigualdad de densidad no fue re-verificada aquí [NO VERIFICADO el valor numérico preciso; el enunciado cualitativo sí].
- **Kulikov–Nazarov–Sodin** (J. Math. Phys. Anal. Geom., 2023; arXiv:2306.14013, verificado a nivel de resumen): para pares de sucesiones no decrecientes $(p,q)$-**supercríticas** ($1/p + 1/q = 1$, $p,q>1$, con condiciones de densidad), el par es de **unicidad de Fourier** y aun de interpolación fuerte; para pares **subcríticos** existe una función de Schwartz no nula que se anula en ambos conjuntos (no-unicidad). La dicotomía super/subcrítica es la versión cuantitativa del fenómeno RV.

### 1.4. Contexto adicional

Cohn–Kumar–Miller–Radchenko–Viazovska (Ann. of Math. 196, 2022, "Universal optimality"): fórmulas de interpolación con nodos $\sqrt{2n}$ en dimensiones 8 y 24, también vía formas modulares [enunciado estándar, no re-verificado en detalle]. BRS §2.5 (verificado): las bases de interpolación de Fourier generan familias de **medidas cristalinas**, tema que conecta con Guinand, Meyer, Lev–Olevskii y Kurasov–Sarnak — exactamente la teoría destruida en el audit previo (NOVEL-STRUCTURE-SEARCH, Candidato A). La conexión dual se examina en §8.

---

## §2. El peso $\mu_\lambda = W_\lambda\,dm_\infty$ y la geometría de las frecuencias $\{\gamma_n\}$

### 2.1. Asintótica del peso (cálculo)

Por Stirling, $|\Gamma(\sigma + i\tau)| = \sqrt{2\pi}\,|\tau|^{\sigma - 1/2}e^{-\pi|\tau|/2}\,(1 + O(1/|\tau|))$. Con $\sigma = 1/4$, $\tau = s/2$:
$$|\Gamma(1/4 + is/2)|^2 = 2\pi\,\Big(\frac{|s|}{2}\Big)^{-1/2}e^{-\pi|s|/2}\,(1 + O(1/|s|)),$$
de donde la densidad de $dm_\infty$ es
$$w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 = \frac{\sqrt{2}}{2\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}\,(1 + O(1/|s|)).$$
*(Nota de consistencia: el Doc 85, §1.2, escribe la constante como $1/(4\pi)$; la tasa $e^{-\pi|s|/2}$ y la potencia $|s|^{-1/2}$ coinciden, la constante correcta es $\sqrt{2}/(2\pi)$. La discrepancia es inocua: ningún argumento del programa usa la constante.)*

Como $W_\lambda$ es una suma finita de cuadrados de polinomios, $\mu_\lambda$ tiene densidad $W_\lambda(s)w(s) \asymp |s|^{d_\lambda - 1/2}e^{-\pi|s|/2}$ con $d_\lambda = 2\deg$ efectivo: **decaimiento exponencial de tasa $\pi/2$, modulado polinomialmente**. En consecuencia (Doc 76, Prop. 1.5):
$$|\widehat{\mu_\lambda}(r)| = O(e^{-(\pi/4)|r|}), \qquad \widehat{\mu_\lambda} \ \text{analítica en } |\mathrm{Im}\,r| < \pi/2 \ \text{y uniformemente continua en } \mathbb{R}, \quad \widehat{\mu_\lambda}(0) = \mu_\lambda(\mathbb{R}) > 0.$$

**Lema 2.1 (positividad casi-segura del kernel).** $W_\lambda(s) > 0$ para todo $s \in \mathbb{R}$, siempre que $N(\lambda) \geq 1$.

*Demostración.* $W_\lambda$ es suma de términos no negativos que incluye $k|P_k|^2$ y $(a^\infty_{N})^2|P_{N+1}|^2$ para dos índices consecutivos $k = N, N+1$ (con $N = N(\lambda)$). $W_\lambda(s_0) = 0$ exigiría $P_N(s_0) = P_{N+1}(s_0) = 0$; pero dos polinomios ortogonales consecutivos respecto a una medida con soporte infinito no tienen ceros comunes (propiedad de entrelazamiento estándar, consecuencia de la recurrencia a tres términos). $\square$

### 2.2. Geometría de $\{\gamma_n\}$: densidad divergente, separación nula, racimos logarítmicos

Los tres hechos siguientes son **incondicionales** (solo usan Riemann–von Mangoldt y casillas):

**(D1) Densidad media divergente.** $N(T)/T \sim \frac{1}{2\pi}\log\frac{T}{2\pi} \to \infty$.

**(D2) Gaps que tienden a cero.** En $[T, 2T]$ hay $\gtrsim \frac{T}{2\pi}\log T$ ceros distribuidos en longitud $T$; por casillas, existen infinitos $n$ con
$$\gamma_{n+1} - \gamma_n \;\leq\; \frac{2\pi}{\log(\gamma_n/2\pi)} \;\longrightarrow\; 0.$$
(Si hay ceros múltiples, hay incluso gaps exactamente nulos; no lo necesitamos.)

**(D3) Racimos logarítmicos.** Para todo $\eta > 0$ y todo $T$ grande existe $m$ con $\gamma_m \in [T, 2T]$ tal que
$$\#\{n : |\gamma_n - \gamma_m| \leq \eta\} \;\geq\; c\,\eta\,\log T$$
con $c > 0$ absoluta. *Demostración:* divídase $[T,2T]$ en $\lceil T/\eta \rceil$ ventanas de longitud $\eta$; alguna ventana contiene al menos el promedio $\gtrsim \frac{\eta}{2\pi}\log T$ ceros; tómese $\gamma_m$ en esa ventana. $\square$

La tensión estructural es exactamente la anticipada en el encargo: la densidad de las frecuencias **crece sin cota** ($\sim \frac{1}{2\pi}\log T$), mientras que el peso, por fuerte que sea su decaimiento ($e^{-\pi|s|/2}$), es **fijo**. El decaimiento del peso controla el *tipo exponencial* de las transformadas (eso da la completitud, Doc 85), pero no puede absorber una densidad *divergente* en las desigualdades cuadráticas de frame, como se demuestra a continuación.

### 2.3. El balance Beurling–Malliavin, hecho cuantitativo

Para fijar ideas con la heurística del Doc 85, §2.2, en términos de "radio de Nyquist": el espacio de transformadas $\{G(z) = \int g\,e^{izs}d\mu_\lambda : g \in L^2(\mu_\lambda)\}$ vive en la clase de funciones enteras de tipo exponencial $\leq \pi/4$ (Doc 76, Prop. 1.5). Para esa clase, el umbral de *unicidad* (cuántos ceros reales puede tener una $G \neq 0$) es una densidad lineal finita $\sim \frac{\pi/4}{\pi} = \frac{1}{4}$ por unidad de longitud; los $\gamma_n$ aportan densidad local $\frac{1}{2\pi}\log\frac{T}{2\pi}$, que supera el umbral en un factor $\to \infty$. Ese exceso es lo que da la completitud con margen infinito (y la sobrecompletitud del Teorema 3.3). Pero el mismo cálculo muestra el costo: para una estructura de **frame/Riesz** el requisito no es superar un umbral sino *casarlo* — densidad comparable al ancho de banda, más separación uniforme (teoría de Seip para muestreo/interpolación en espacios de Paley–Wiener y Bargmann–Fock). Aquí el cociente densidad/banda diverge logarítmicamente: el sistema está infinitamente lejos del régimen de frame, en la dirección de sobremuestreo absoluto. **El decaimiento del peso no entra en este cociente**: solo fija la banda $\pi/4$; ningún peso con $\widehat{\mu}$ continua (es decir, ninguno) cambia la conclusión (Corolario 3.5).

---

## §3. Pregunta (i): la jerarquía completa — qué es y qué no es $\{e^{i\gamma_n s}\}$ en $L^2(\mu_\lambda)$

Notación: $e_n := e_{\gamma_n}$, $\mathcal{H} = L^2(\mu_\lambda)$, $\lambda > 0$ fijo con $N(\lambda) \geq 1$. Obsérvese que $\|e_n\|^2_{\mathcal{H}} = \mu_\lambda(\mathbb{R})$ para todo $n$ (las frecuencias son reales: $|e^{i\gamma_n s}| = 1$), y
$$\langle e_m, e_n\rangle_{\mathcal{H}} = \int e^{i(\gamma_m - \gamma_n)s}\,d\mu_\lambda(s) = \widehat{\mu_\lambda}(\gamma_m - \gamma_n).$$
La matriz de Gram del sistema es $G_{mn} = \widehat{\mu_\lambda}(\gamma_m - \gamma_n)$, con diagonal constante $\mu_\lambda(\mathbb{R})$.

### 3.1. No hay cota superior de frame (no es sistema de Bessel)

**Teorema 3.1 (incondicional).** No existe $B < \infty$ tal que $\sum_n |\langle f, e_n\rangle|^2 \leq B\|f\|^2$ para toda $f \in \mathcal{H}$. En particular $\{e_n\}$ **no es un frame** de $L^2(\mu_\lambda)$.

*Demostración.* Por continuidad de $\widehat{\mu_\lambda}$ en $0$ y $\widehat{\mu_\lambda}(0) = \mu_\lambda(\mathbb{R}) > 0$, existe $\eta > 0$ con $|\widehat{\mu_\lambda}(r)| \geq \mu_\lambda(\mathbb{R})/2$ para $|r| \leq \eta$. Por (D3), para cada $T$ grande existe $m = m(T)$ con $\gamma_m \in [T,2T]$ y $\#\{n : |\gamma_n - \gamma_m| \leq \eta\} \geq c\eta\log T$. Tómese $f = e_m$ (que está en el sistema, $\|f\|^2 = \mu_\lambda(\mathbb{R})$):
$$\sum_n |\langle e_m, e_n\rangle|^2 \;\geq\; \sum_{n:\,|\gamma_n - \gamma_m|\leq\eta} |\widehat{\mu_\lambda}(\gamma_m - \gamma_n)|^2 \;\geq\; c\,\eta\,\log T \cdot \frac{\mu_\lambda(\mathbb{R})^2}{4}.$$
Entonces cualquier constante de Bessel satisface $B \geq \frac{c\eta}{4}\mu_\lambda(\mathbb{R})\log T \to \infty$. $\square$

### 3.2. No es sucesión de Riesz

**Teorema 3.2 (incondicional).** No existe $A > 0$ tal que $\big\|\sum_k c_k e_{n_k}\big\|^2 \geq A\sum_k |c_k|^2$ para toda combinación finita. En particular $\{e_n\}$ **no es base de Riesz** ni sucesión de Riesz, ni siquiera tras normalizar.

*Demostración.* Por (D2) existen pares $n, n+1$ con $\delta_n := \gamma_{n+1} - \gamma_n \to 0$. Con $c = (1, -1)$:
$$\|e_n - e_{n+1}\|^2 = 2\big(\mu_\lambda(\mathbb{R}) - \mathrm{Re}\,\widehat{\mu_\lambda}(\delta_n)\big) \longrightarrow 0$$
por continuidad de $\widehat{\mu_\lambda}$ en $0$. Una cota inferior de Riesz exigiría $\|e_n - e_{n+1}\|^2 \geq 2A > 0$ para todos esos pares. Contradicción. $\square$

### 3.3. No es minimal: sobrecompletitud total

**Teorema 3.3 (incondicional, módulo V.1).** Para todo $k$, el sistema $\{e_n\}_{n \neq k}$ sigue siendo completo en $L^2(\mu_\lambda)$. En consecuencia $\{e_n\}$ no es minimal: **ningún elemento es necesario**, y el sistema no es base de Schauder de ningún tipo.

*Demostración.* El argumento de completitud del Doc 85 (Teorema 5.1) solo usa que la densidad de la sucesión de frecuencias es divergente frente al tipo exponencial $\pi/4$ de las transformadas $G(z) = \int g\,e^{izs}d\mu_\lambda$. Quitar un elemento (o cualquier subconjunto de densidad cero) no altera $N(T)/T \to \infty$. Luego el mismo argumento da $G \equiv 0$. (Hereda el gap V.1 del Doc 85.) $\square$

### 3.4. No es sucesión de interpolación

**Teorema 3.4 (incondicional).** $\{\gamma_n\}$ no es sucesión de interpolación para $\mathcal{H}$: existe $(c_n) \in \ell^\infty$ (de hecho con solo dos valores) tal que ningún $f \in \mathcal{H}$ satisface $\langle f, e_n\rangle = c_n$ para todo $n$.

*Demostración.* Para un par cercano $(n, n+1)$ como en 3.2, todo $f \in \mathcal{H}$ cumple
$$|\langle f, e_n\rangle - \langle f, e_{n+1}\rangle| \leq \|f\|\cdot\|e_n - e_{n+1}\| \to 0 .$$
Prescribir $c_n = 1$, $c_{n+1} = -1$ a lo largo de una sucesión de pares con $\delta_n \to 0$ exigiría $\|f\| \geq 2/\|e_n - e_{n+1}\| \to \infty$. $\square$

### 3.5. Robustez: la refutación es independiente del peso

Los Teoremas 3.1–3.4 usan de $\mu_\lambda$ exactamente dos propiedades: $\mu_\lambda(\mathbb{R}) < \infty$ y $\widehat{\mu_\lambda}$ continua en $0$. Pero la segunda es automática para cualquier medida finita. Por tanto:

**Corolario 3.5 (no hay re-pesado que repare la estructura).** Sea $\mu$ **cualquier** medida positiva finita sobre $\mathbb{R}$ con $\mu \neq 0$. Entonces el sistema $\{e^{i\gamma_n s}\}$ en $L^2(\mu)$ no es Bessel, no es sucesión de Riesz y no es sucesión de interpolación. En particular, ninguna elección de $\lambda$, ninguna modificación de $W_\lambda$ dentro de la clase de kernels positivos integrables, y ningún reemplazo de $dm_\infty$ por otra medida finita puede restaurar la estructura de frame.

*Demostración.* Idéntica a 3.1, 3.2, 3.4: solo se usó $\widehat{\mu}(0) = \mu(\mathbb{R}) > 0$, la continuidad uniforme de $\widehat{\mu}$ (automática: $\mu$ finita), (D2) y (D3). $\square$

**Observación 3.6 (la única salida formal está bloqueada).** Para que las refutaciones fallaran se necesitaría $\widehat{\mu}$ discontinua en $0$ o no decaimiento de la masa — es decir, $\mu(\mathbb{R}) = \infty$. Pero con $\mu$ infinita las exponenciales $e^{i\gamma s}$ dejan de pertenecer a $L^2(\mu)$ (su módulo es 1) y el sistema ni siquiera está definido. Alternativa restante: abandonar exponenciales puras por elementos normalizables tipo wavelet/Gabor sobre los $\gamma_n$ — eso cambia el mecanismo (deja de ser el sistema del Doc 85) y no se evalúa aquí; cualquier intento futuro debe pasar primero la Dicotomía 8.1.

**Observación 3.7 (por qué BRS sí obtiene interpolación con los mismos $\gamma_n$).** No hay contradicción entre los Teoremas 3.1–3.4 y el Teorema BRS 1.1. BRS no trabaja en $L^2$ de una medida con un solo lado de muestreo: su espacio $\mathcal{H}_1$ es una clase **analítica en franja** mucho más chica, y su sistema de nodos es **bilateral** — valores de $f$ en los ceros **y** valores de $\widehat{f}$ en $\{\frac{\log n}{4\pi}\}$. La criticidad exacta (no-redundancia) vive en esa geometría de dos lados tiempo-frecuencia. El sistema del programa usa un solo lado (frecuencias $\gamma_n$ contra una medida fija), y con un solo lado la densidad divergente es incurablemente excesiva. Lección estructural: *la geometría natural de los ceros como nodos no es la de una base en un $L^2$ pesado, sino la de la mitad de un par crítico tiempo-frecuencia* — y la otra mitad son los logaritmos de los enteros.

### 3.8. Síntesis de (i)

| Propiedad | ¿Vale? | Estatus |
|---|---|---|
| Completitud | **Sí** | Incondicional (Doc 85, módulo V.1) |
| Sobrecompletitud (no-minimalidad) | **Sí** | Teorema 3.3, incondicional (módulo V.1) |
| Cota superior de frame (Bessel) | **No** | Teorema 3.1, incondicional |
| Frame | **No** | Corolario de 3.1 |
| Sucesión / base de Riesz | **No** | Teorema 3.2, incondicional |
| Sucesión de interpolación | **No** | Teorema 3.4, incondicional |
| Cota inferior de frame aislada | Abierta | Irrelevante: sin cota superior no hay operador de análisis acotado ni reconstrucción estable |

**Conclusión de (i).** La respuesta es definitiva y negativa en todos los niveles cuantitativos: el sistema es *solo* completo. La densidad divergente $\frac{1}{2\pi}\log T$ es simultáneamente la fuente de la completitud (sobra densidad para el argumento de Carlson) y el veneno de toda estructura de frame (racimos logarítmicos rompen Bessel; gaps nulos rompen Riesz e interpolación). El decaimiento exponencial del peso **no compensa**: fija el tipo exponencial $\pi/4$ de las transformadas, pero las desigualdades de frame son insensibles al tipo y sensibles a la densidad local, que diverge. Esto no es un gap: es un teorema en contra.

---

## §4. Pregunta (ii): qué diría cada nivel sobre $d\nu$ — y qué dice el nivel que tenemos

### 4.0. Observación previa: dónde "viven" los $\gamma_n$ respecto a $d\nu$

Conviene fijar la relación geométrica exacta, porque es la fuente de la autorreferencia que se detecta en §6. La medida $d\nu = (R-1)\,dm_{full,on}$ tiene densidad $\propto \sum_{j:\delta_j>0} \delta_j^2/(s-\gamma_j)^2 + O(\delta^4)$ a primer orden (Doc 89, §2.1): está **concentrada alrededor de las ordenadas $\gamma_j$ de los ceros off-critical**. Las frecuencias del sistema $\{e^{i\gamma_n s}\}$ son **todas** las ordenadas (on y off). Es decir: los $\gamma_n$ entran al mecanismo dos veces — como soporte aproximado del objeto a anular y como frecuencias del sistema que lo testea. Toda identidad que produzcamos vinculará ceros consigo mismos a través de los primos; el contenido aritmético entra solo por la rigidez global de $\zeta$ (vía $dm_{full}$), nunca por el sistema de exponenciales.

### 4.1. El puente exacto entre el sistema y $d\nu$

**Lema 4.1 (incondicional).** Sea $h := \dfrac{d\nu}{dm_\infty} = \big(|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2\big) \geq 0$. Entonces $h \in L^2(\mu_\lambda)$ y
$$T_\lambda = \langle h, \mathbf{1}\rangle_{L^2(\mu_\lambda)}, \qquad \langle h, e_n\rangle_{L^2(\mu_\lambda)} = \int e^{-i\gamma_n s}\,W_\lambda(s)\,d\nu(s) = \big(W_\lambda\,d\nu\big)^{\wedge}(-\gamma_n) =: \widehat{\nu_\lambda}(-\gamma_n).$$

*Demostración.* $0 \leq h \leq |\zeta(1/2+is)|^2$ puntualmente (pues $R \geq 1 \Rightarrow |\zeta_{on}| \leq |\zeta|$). Por la cota de convexidad incondicional $|\zeta(1/2+it)| \ll (1+|t|)^{1/4+\varepsilon}$,
$$\int h^2\,d\mu_\lambda \leq \int |\zeta(1/2+is)|^4\,W_\lambda(s)\,w(s)\,ds \ll \int (1+|s|)^{1+\varepsilon}\,|s|^{d_\lambda - 1/2}e^{-\pi|s|/2}\,ds < \infty.$$
Las dos identidades son reescrituras directas de $T_\lambda = \int W_\lambda\,d\nu$ y de la definición del producto interno. $\square$

### 4.2. La escalera de implicaciones (enunciados exactos)

**(Nivel "completo" — el que TENEMOS).**

**Proposición 4.2 (nueva condición equivalente; "Condición 9" para la tabla del Doc 89).** *Incondicionalmente (módulo V.1), para cualquier $\lambda$ fijo con $N(\lambda) \geq 1$:*
$$\mathrm{RH} \iff \big(W_\lambda\,d\nu\big)^{\wedge}(\gamma_n) = 0 \quad \text{para todo } n \geq 1.$$

*Demostración.* ($\Rightarrow$) RH $\Rightarrow d\nu = 0 \Rightarrow$ trivial. ($\Leftarrow$) Por el Lema 4.1, las hipótesis dicen $\langle h, e_n\rangle = 0$ para todo $n$ ($d\nu$ es par, Prop. 8.1 del Doc 89, así que anulación en $\gamma_n$ equivale a anulación en $-\gamma_n$). Por la completitud (Doc 85, Teorema 5.1), $h = 0$ en $L^2(\mu_\lambda)$, es decir $h\,W_\lambda\,w = 0$ a.e.; por el Lema 2.1 ($W_\lambda > 0$) y $w > 0$, $h = 0$ a.e., luego $d\nu = 0$, luego RH (Doc 89, Teorema 10.1, (1)$\iff$(2)). $\square$

Es la primera condición del programa que testea $d\nu$ **solo en las frecuencias $\gamma_n$** (numerable, sin sup sobre $\lambda$ ni sobre $z \in \mathbb{H}$). Su honestidad se audita en §6.3: es una condición CAP-style, no verificable sin los ceros.

**(Nivel "frame" — el que NO tenemos, refutado).** Si $\{e_n\}$ fuera un frame con cotas $A, B$, valdría
$$A\,\|h\|^2_{L^2(\mu_\lambda)} \;\leq\; \sum_n \big|\widehat{\nu_\lambda}(\gamma_n)\big|^2 \;\leq\; B\,\|h\|^2_{L^2(\mu_\lambda)},$$
y con Cauchy–Schwarz $T_\lambda = \langle h, \mathbf{1}\rangle \leq \mu_\lambda(\mathbb{R})^{1/2}\|h\|$ se obtendría la **cota cuantitativa**
$$T_\lambda^2 \;\leq\; \frac{\mu_\lambda(\mathbb{R})}{A}\,\sum_n \big|\widehat{\nu_\lambda}(\gamma_n)\big|^2.$$
Es decir: *un control numérico de las muestras de $\widehat{\nu_\lambda}$ en los ceros controlaría $T_\lambda$, con estabilidad frente a errores*. Esto habría sido un mecanismo de "RH efectiva por muestreo". **El Teorema 3.1 demuestra que la desigualdad derecha es falsa (B = ∞) y por tanto el mecanismo cuantitativo no existe.** La izquierda aislada queda abierta pero sin la derecha no hay reconstrucción estable.

**(Nivel "Riesz/interpolación" — refutado).** Una base de Riesz daría además unicidad de coeficientes y un isomorfismo $\mathcal{H} \simeq \ell^2$ que convertiría $T_\lambda$ en una forma cuadrática explícita en las muestras $\{\widehat{\nu_\lambda}(\gamma_n)\}$ con cotas bilaterales — el sueño cuantitativo completo. Falso por el Teorema 3.2.

### 4.2bis. Sobre los funcionales de coeficientes (por qué tampoco hay sistema dual)

Para completar el cuadro: aun sin frame, un sistema completo puede a veces admitir un **sistema dual** $\{g_n\} \subset \mathcal{H}$ con $\langle g_m, e_n\rangle = \delta_{mn}$ (biortogonalidad), lo que permitiría escribir $T_\lambda$ como serie de coeficientes. El Teorema 3.3 (sobrecompletitud: todo subsistema cofinito sigue completo) lo excluye: si existiera $g_m$ biortogonal, $g_m$ sería ortogonal a $\overline{\mathrm{span}}\{e_n : n \neq m\} = \mathcal{H}$, luego $g_m = 0$, contradiciendo $\langle g_m, e_m\rangle = 1$. **No existe ningún sistema de funcionales de coeficientes**: la expansión de $h$ (la densidad de $d\nu$ respecto a $dm_\infty$) en las exponenciales de los ceros existe como aproximación (completitud) pero sus coeficientes no son ni únicos ni continuos. Esto explica retrospectivamente por qué el Doc 82 no pudo extraer un criterio coeficiente-a-coeficiente del Camino 3, y por qué BRS necesitan salir de $L^2$ a $\mathcal{H}_1$ y añadir la segunda familia de nodos para tener biortogonalidad (sus relaciones (1.3) son exactamente la biortogonalidad que aquí es imposible).

### 4.3. Conclusión de (ii)

La jerarquía colapsa de manera informativa: **la completitud sola ya entrega todo el contenido cualitativo que un frame entregaría** (la equivalencia de la Proposición 4.2: $d\nu$ queda determinada por sus muestras en los $\gamma_n$); lo que el frame añadiría es exclusivamente la **estabilidad cuantitativa** (cotas $A, B$), y eso es exactamente lo que los Teoremas 3.1–3.2 refutan incondicionalmente. No hay versión cuantitativa-estable del muestreo de $d\nu$ en los ceros dentro de $L^2(\mu_\lambda)$.

---

## §5. Pregunta (iii): ¿la maquinaria modular inyecta aritmética externa que evada MW-2/MW-7?

Esta es la pregunta discriminadora central. La respuesta requiere tres pasos: identificar qué input aritmético usan RV/BRS, ver por qué canal toca a $\zeta$, y ver si ese canal es sensible a $\mathrm{Re}(\rho)$.

### 5.1. Qué es realmente el input modular

- **RV:** formas modulares débilmente holomorfas de peso $3/2$ para $\Gamma_\theta$. El generador de toda la estructura es la función theta $\theta(\tau) = \sum_{n\in\mathbb{Z}} e^{\pi i n^2\tau}$ y su ley de transformación $\theta(-1/\tau) = \sqrt{\tau/i}\,\theta(\tau)$. El hecho verificado de que la fórmula RV evaluada en $x = 0$ **se reduce a la sumación de Poisson** (§1.1) delata el contenido: la fórmula RV es un *despliegue interpolatorio* de la modularidad de $\theta$, que a su vez es equivalente a Poisson sobre $\mathbb{Z}$.
- **BRS:** integrales modulares para $\Gamma_\theta$ (cohomología de Eichler / principio de Knopp) construyen $D(w,s)$; el kernel que produce los nodos es $H(w,s) = \frac{\zeta(s)}{\zeta(w)}D(w,s)$, y sus ecuaciones funcionales $H(1-w,s) = -H(w,s)$, $H(w,1-s) = H(w,s)$ descansan en la **ecuación funcional de $\zeta$**.

**Observación 5.1 (el canal es la ecuación funcional).** Por el argumento clásico de Riemann (1859) y el teorema converso de Hecke, la modularidad de $\theta$ bajo $\tau \mapsto -1/\tau$ y la ecuación funcional $\pi^{-s/2}\Gamma(s/2)\zeta(s) = \pi^{-(1-s)/2}\Gamma((1-s)/2)\zeta(1-s)$ son **equivalentes** vía transformada de Mellin. Por tanto, el "input aritmético externo" de la maquinaria RV/BRS, *en cuanto toca a $\zeta$*, es exactamente la ecuación funcional — un dato que el programa (y todos los programas: Weil, de Branges, Connes) ya posee y ya explota. No hay aritmética nueva entrando por ese canal.

### 5.2. Lo que sí es genuinamente nuevo en BRS — y por qué no es la palanca

Hay que ser preciso y justo: BRS demuestran algo que **no** es la fórmula explícita de Weil. La comparación verificada (§1.2):

| | Fórmula de Weil (1.1 en BRS) | Fórmula BRS (1.2) |
|---|---|---|
| Input analítico | **Producto de Euler** + ecuación funcional | **Serie de Dirichlet** + ecuación funcional |
| Sucesión de enteros | potencias de primos $n = p^k$, pesos $\Lambda(n)/\sqrt{n}$, nodos $\frac{\log n}{2\pi}$ | **todos** los enteros, nodos $\frac{\log n}{4\pi}$ |
| Naturaleza de la dualidad | multiplicativa | **aditiva** |
| Estructura | identidad (un funcional lineal) | **base de interpolación** (sistema completo de funcionales) |

La dualidad aditiva (ceros $\leftrightarrow$ todos los enteros) es información estructuralmente distinta de la fórmula explícita: BRS lo subrayan, y el hecho de que la fórmula de Weil sea *un* funcional representado en la base BRS (cita en §1.2) muestra que (1.2) es más fina que (1.1). **Respuesta a la sub-pregunta del encargo: la fórmula dual de BRS NO es exactamente la fórmula explícita de Weil; es estrictamente más fina (Weil = un funcional; BRS = la base entera), y proviene de la serie de Dirichlet, no del producto de Euler.**

Pero aquí está el punto decisivo para MW-2: precisamente porque BRS evita el producto de Euler, su input es (serie de Dirichlet global) + (ecuación funcional) — y la serie de Dirichlet $\sum n^{-s}$ de $\zeta$ **no contiene la información multiplicativa** que MW-2 declara confinada a $\mathrm{Re}(s) > 1$. BRS no rompe MW-2: lo **esquiva renunciando a la aritmética de los primos**. El teorema funciona igual para cualquier serie de Dirichlet con ecuación funcional del tipo adecuado (BRS §5 lo hace para caracteres de Dirichlet y "otras series de Dirichlet" — incluida, nótese, la clase donde viven contraejemplos tipo Davenport–Heilbronn con ceros fuera de la recta). Una maquinaria que se aplica indistintamente a $\zeta$ y a funciones con ceros off-line documentados no puede, por sí sola, sentir $\mathrm{Re}(\rho) = 1/2$.

### 5.3. La prueba de insensibilidad a $\mathrm{Re}(\rho)$ (el test I2b en acto)

Tres verificaciones independientes de que toda la teoría es **ciega a $\beta_j = \mathrm{Re}(\rho_j)$**:

1. **Los nodos.** El Teorema BRS 1.1 es incondicional con nodos $\frac{\rho - 1/2}{i} = \gamma - i(\beta - 1/2)$: si un cero se sale de la recta, el nodo **sale de $\mathbb{R}$ y la fórmula sigue valiendo, intacta**, en la franja. La maquinaria modular no ejerce ninguna presión que empuje los nodos hacia $\mathbb{R}$. La realidad de los nodos no es un output: es una *reformulación* de RH (ver §8: es el avatar interpolatorio de Lee–Yang).
2. **Las densidades.** Todo el contenido cuantitativo de la teoría de unicidad/interpolación (Kulikov; KNS super/subcrítico; la criticidad exacta de BRS) depende de **funciones de conteo**: y $N(T)$ es la misma bajo RH y bajo $\neg$RH (Riemann–von Mangoldt cuenta ceros en la franja, no en la recta; Doc 85, Obs. 4.3). La "correspondencia precisa entre la condición de densidad de Kulikov y Riemann–von Mangoldt" (§1.3) es bella, pero es una correspondencia con un invariante $\beta$-ciego. El paralelo con RV es exacto: allí los nodos $\sqrt{n}$ tienen función de conteo $N(r) = r^2$, que es precisamente la criticidad de KNS para el par $(\sqrt{n}, \sqrt{n})$; la aritmética de los nodos entra solo a través de su conteo y de la modularidad de $\theta$ — en ningún punto de la teoría un teorema convierte conteo en posición.
3. **El único enunciado $\beta$-sensible es condicional.** La lectura "muestreo no redundante sobre dos sucesiones reales" — el único enunciado del corpus que requiere nodos reales — **asume RH y simplicidad** (verificado, §1.2). Es decir: dentro de la propia literatura, la sensibilidad a $\mathrm{Re}(\rho)$ solo aparece como hipótesis, nunca como conclusión.

### 5.3bis. El testigo Davenport–Heilbronn

El test más duro de $\beta$-ceguera es un contraejemplo explícito. La función de Davenport–Heilbronn $L_{DH}$ (combinación de funciones $L$ de Dirichlet mód 5) satisface una ecuación funcional del tipo de Riemann y **tiene ceros fuera de la recta crítica**, demostrados. BRS, §5.3, extienden su construcción a "ceros de otras series de Dirichlet" con ecuación funcional de la forma $Q^{-s}\Gamma(s/2)F(s) = Q^{-(1-s)}\Gamma((1-s)/2)\overline{F(1-\bar{s})}$ (verificado en la p. 5 del PDF: la observación de que basta reemplazar $\zeta(s)/\zeta(w)$ por $F(s)/F(w)$). Que $L_{DH}$ esté literalmente cubierta por las hipótesis exactas de BRS §5.3 queda [NO VERIFICADO en detalle]; lo que sí queda verificado es el principio: **la maquinaria solo consume serie de Dirichlet + ecuación funcional, y esa dupla es satisfecha por funciones con ceros off-line**. Una maquinaria cuyo dominio natural contiene contraejemplos a la "RH local" no puede contener, sin input adicional, el teorema que la probaría para $\zeta$. Este es el mismo patrón que el programa documentó para el flujo DBN (FAIL I4, ceguera aritmética) — aquí la ceguera no es a los primos sino a la posición $\beta$ de los ceros, con idéntico efecto discriminador.

### 5.4. Dictamen de (iii)

**El input modular NO evade MW-2/MW-7.** Con precisión:

- No lo evade porque no transporta producto de Euler: la modularidad de $\theta$ = ecuación funcional (Observación 5.1), y la parte genuinamente nueva (dualidad aditiva, cohomología de Knopp) opera al nivel de series de Dirichlet generales, donde RH es falsa en general.
- El punto estructural a favor registrado en NOVEL-STRUCTURE-SEARCH ("las fórmulas se construyen con formas modulares — input externo no derivado del producto de Euler, posiblemente no bloqueado por MW-2") queda **resuelto en negativo**: el input es externo al producto de Euler, sí — pero por eso mismo es *aún más débil* que el producto de Euler respecto de la franja crítica. MW-2 bloquea la propagación de la aritmética multiplicativa; la maquinaria modular ni siquiera la carga.
- Lo que sí habría sido una evasión: un teorema del lado modular que **fuerce** la realidad de los nodos (el análogo del índice de Hodge en el caso de cuerpos de funciones). No existe en RV/BRS/KNS, y el ítem 1 de §5.3 muestra que la estructura de los teoremas apunta en la dirección contraria (validez incondicional con nodos complejos = ninguna fuerza hacia $\mathbb{R}$).

---

## §6. Pregunta (iv): unicidad tipo Heisenberg para $d\nu$

### 6.1. Propiedades de $d\nu$ verificables sin conocer ceros (lado "datos")

Incondicionales, sin posiciones de ceros (Docs 83, 89 + cálculo nuevo):

- (V-a) $d\nu \geq 0$.
- (V-b) $d\nu(-s) = d\nu(s)$ (paridad).
- (V-c) $\|d\nu\| < \infty$ y más fino: $d\nu \leq dm_{full}$, cuya densidad es verificable desde $\zeta$ y decae como $|s|^{1/2+\varepsilon}e^{-\pi|s|/2}$.
- (V-d) **(nuevo, cálculo)** $\widehat{\nu}(z) = \int e^{izs}d\nu(s)$ es analítica en la franja $|\mathrm{Im}\,z| < \pi/2$ y acotada en subfranjas, porque las colas de $d\nu$ están dominadas por $e^{-\pi|s|/2}$ por (V-c). Análogamente la densidad $h$ de $d\nu$ respecto a $ds$ extiende analíticamente a $|\mathrm{Im}\,s| < 1/2$ (las únicas singularidades de $\zeta(1/2+is)\zeta(1/2-is)$ son $s = \pm i/2$, y la pieza $on$ tiene la misma estructura).

### 6.2. Pares forzantes (lado "teoremas"): qué combinaciones obligan $d\nu = 0$

**(P1) Analiticidad + anulación en un conjunto con acumulación.** Por (V-d), si $\widehat{\nu} = 0$ en cualquier intervalo $(-\delta,\delta)$ (o en un conjunto con punto de acumulación en la franja), entonces $\widehat{\nu} \equiv 0$ y $d\nu = 0$. — *Forzante; pero la condición no es verificable:* $\widehat{\nu} = \widehat{dm_{full}} - \widehat{dm_{full,on}}$, y el segundo término requiere $\zeta_{on}$, es decir, **todas** las posiciones $\beta_j$. (El primer término, $\widehat{dm_{full}}$, es en principio computable desde $\zeta$ — es un objeto de tipo segundo momento / Motohashi — pero eso no rescata nada sin su pareja.)

**(P2) Analiticidad + muestreo en los $\gamma_n$ (densidad divergente).** Versión-medida de la Proposición 4.2: $\widehat{\nu}$ es analítica y acotada en subfranjas; si $\widehat{\nu}(\gamma_n) = 0$ para todo $n$, con $N(T)/T \to \infty$, un argumento tipo Carlson/Levinson en la franja fuerza $\widehat{\nu} \equiv 0$. — *Forzante (módulo la misma verificación técnica V.1); condición no verificable y doblemente autorreferente: los nodos son los ceros y el objeto está construido con los ceros.*

**(P3) Pares de unicidad KNS supercríticos.** Si se toma $F$ = (regularización de $\widehat{\nu}$ en la clase de Schwartz, gap declarado abajo) y un par supercrítico $(\Lambda_1, \Lambda_2)$ de KNS **que no involucre ceros** (p. ej. potencias $n^a$): $F|_{\Lambda_1} = 0$ y $\widehat{F}|_{\Lambda_2} = 0 \Rightarrow F = 0$. — *Forzante; pero las condiciones $F|_{\Lambda_1} = 0$ son evaluaciones de $\widehat{\nu}$, otra vez inaccesibles sin $\zeta_{on}$.* **Gap declarado:** KNS está enunciado para funciones de Schwartz; $\widehat{\nu}$ está en una clase analítica-en-franja con decaimiento que hay que verificar (la densidad $h$ oscila con frecuencias $\sim \log$; el decaimiento de $\widehat{\nu}$ en líneas horizontales se sigue de la analiticidad en $|\mathrm{Im}\,s|<1/2$ de $h\,$, dando $\widehat{\nu}(x) \ll e^{-(1/2-\varepsilon)|x|}$, suficiente; la pertenencia exacta a $\mathcal{H}_1$ o a Schwartz no se verifica aquí — **gap técnico G.101.1**).

**(P4) El par BRS aplicado a $F = \widehat{\nu}$ (si $F \in \mathcal{H}_1$, gap G.101.1).** Corolario BRS 1.1(i): $\widehat{F}\big(\frac{\log n}{4\pi}\big) = 0\ \forall n$ **y** $F^{(j)}\big(\frac{\rho-1/2}{i}\big) = 0\ \forall \rho,j \Rightarrow F \equiv 0 \Rightarrow d\nu = 0 \Rightarrow$ RH. Nótese qué significa cada familia: $\widehat{F}$ recupera la densidad $h$ de $d\nu$ (anulación puntual de $h$ en puntos $\asymp \log n$), y la segunda familia muestrea $\widehat{\nu}$ **en los ceros mismos**, con multiplicidades y con nodos complejos si $\neg$RH. — *Forzante, incondicional, y es el teorema de unicidad más fuerte disponible en la literatura; pero una de las dos familias de nodos ES el multiconjunto de ceros: autorreferencia inevitable.*

### 6.3. La detección de circularidad (explícita, como exige el encargo)

**Proposición 6.1 (la fórmula explícita aplicada a $d\nu$ reproduce $T_\lambda$).** Toda evaluación de los funcionales de (P1)–(P4) por la vía de la fórmula explícita reproduce objetos que el programa ya tiene. Concretamente: el Doc 72 demostró
$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}}\,B_\lambda(\log p),$$
es decir, la evaluación vía Riemann–Weil del funcional $\int W_\lambda\,d\nu$ es exactamente la descomposición ceros/primos del Doc 72. Y la observación verificada de BRS (§1.2) — *la fórmula de Weil es el funcional lineal $\mathcal{H}_1 \to \mathbb{C}$ representado en la base BRS* — implica que representar los funcionales de $d\nu$ en la base BRS es un cambio de base del mismo dato, no dato nuevo. En símbolos: si $\Phi_{Weil}(f) = \sum_\rho f\big(\frac{\rho-1/2}{i}\big) - (\text{lado primos})$, entonces los coeficientes de $\Phi_{Weil}$ en la base $\{U_n, V_{\rho,j}\}$ se calculan evaluando en los nodos — los ceros otra vez. **No hay ganga: la base BRS re-expande la información de los ceros sobre los ceros.** $\square$

### 6.2bis. La matriz datos × teoremas (el cuadro completo del problema de unicidad)

Formulación tipo Heisenberg pedida por el encargo: ¿qué pares (condición sobre $d\nu$, condición sobre transformadas de $d\nu$) fuerzan $d\nu = 0$, y cuáles de sus ingredientes son verificables sin ceros?

| Ingrediente | ¿Forzante (en par adecuado)? | ¿Verificable sin posiciones de ceros? |
|---|---|---|
| $d\nu \geq 0$ (V-a) | No por sí solo (Doc 89, Prop. 11.1) | **Sí** (Doc 83) |
| paridad (V-b) | No | **Sí** |
| $d\nu \leq dm_{full}$, colas $e^{-\pi\vert s\vert/2}$ (V-c) | No | **Sí** |
| $\widehat{\nu}$ analítica en $\vert\mathrm{Im}\,z\vert < \pi/2$ (V-d) | Solo combinada | **Sí** (consecuencia de V-c) |
| $\widehat{\nu} = 0$ en un intervalo (P1) | **Sí** (con V-d) | No — requiere $\widehat{dm_{full,on}}$ |
| $\widehat{\nu}(\gamma_n) = 0\ \forall n$ (P2 / Cond. 9) | **Sí** (con V-d, módulo V.1) | No — doblemente autorreferente |
| $\widehat{\nu}$ nula en $\Lambda_1$ y $h$ nula en $\Lambda_2$, par KNS supercrítico (P3) | **Sí** (módulo G.101.1) | No — mismas evaluaciones inaccesibles |
| par BRS: $h$ en $\asymp\log n$ y $\widehat{\nu}^{(j)}$ en $\frac{\rho-1/2}{i}$ (P4) | **Sí**, incondicional (módulo G.101.1) | No — una familia de nodos ES el multiconjunto de ceros |

La estructura es exacta: **la columna "verificable" y la columna "forzante" tienen intersección vacía**. Las cuatro propiedades verificables (positividad, paridad, mayorante, analiticidad en franja) son compatibles con $d\nu \neq 0$ — de hecho cualquier medida positiva par con colas $O(e^{-\pi|s|/2})$ las satisface, y la clase de tales medidas tiene dimensión infinita. Los cuatro teoremas forzantes consumen evaluaciones puntuales de $\widehat{\nu}$ o de $h$, todas con costo epistémico = conocer $\{\beta_j\}$. La teoría de interpolación desplaza la frontera de los teoremas (más finos, numerables, críticos) sin mover un milímetro la frontera de los datos.

**Síntesis de (iv) — el muro de Hadamard, versión interpolatoria.** La teoría de interpolación/unicidad **amplía genuinamente el catálogo de condiciones forzantes** (P1–P4 son más finas que las del Doc 89: muestreos numerables, pares críticos no redundantes) pero **no añade ni una sola condición verificable**: en cada par (datos, teorema), el lado de datos exige $\widehat{\nu}$ o $h$, y ambos requieren $dm_{full,on}$, es decir, las posiciones $\{\beta_j\}$. El muro MW-7 no está en los conjuntos de prueba (que la interpolación permite elegir con enorme libertad): está en el **objeto** $d\nu$, cuya propia definición consume las posiciones de los ceros. Cambiar los nodos no cambia el objeto. Esta es la formulación más nítida de MW-7 lograda hasta ahora: *la inaccesibilidad epistémica de $d\nu$ es invariante bajo la dualidad de Fourier y bajo cambio de base de interpolación.*

---

## §7. Pregunta (v): el discriminador (I1, I2a, I2b, I3, I4)

Mecanismo evaluado: **"estructura de interpolación de Fourier / frame sobre los ceros como palanca para $d\nu = 0$"**, en sus dos variantes: (a) frame cuantitativo en $L^2(\mu_\lambda)$; (b) maquinaria modular RV/BRS.

| Criterio | Variante (a): frames | Variante (b): modular RV/BRS |
|---|---|---|
| **I1** (codifica todos los primos) | ✅ vía $dm_{full}$ y los $\gamma_n$ | ✅ kernel $\zeta(s)/\zeta(w)$; nodos $\frac{\log n}{4\pi}$ |
| **I2a** (input independiente existe) | ❌ — el espacio $L^2(W_\lambda dm_\infty)$ y las frecuencias son $\zeta$ re-codificada (mismo diagnóstico que de Branges en la tabla de Phase A) | ◐/✅ — la cohomología de Eichler–Knopp y las formas de peso $3/2$ para $\Gamma_\theta$ son estructura genuinamente externa; pero el canal por el que tocan a $\zeta$ es solo la ecuación funcional (Obs. 5.1) |
| **I2b** (teorema decisivo que suministra la restricción) | ❌ — peor que ausente: la restricción cuantitativa deseada (cotas de frame) es **falsa por teorema** (3.1–3.2) | ❌ — ningún teorema del corpus fuerza nodos reales; la validez incondicional con nodos complejos (§5.3, ítem 1) demuestra que la maquinaria no ejerce presión alguna sobre $\mathrm{Re}(\rho)$; todo invariante cuantitativo (densidades) es $\beta$-ciego |
| **I3** (localiza ceros individuales) | ✅ — una frecuencia por cero | ✅ — una función base $V_{\rho,j}$ por cero (con multiplicidad) |
| **I4** (genuinamente aritmético) | ✅ | ✅ |

**Dictamen:** la variante (a) falla I2a e I2b (con I2b refutado constructivamente — el caso más fuerte de fallo registrado en el programa: no "falta el teorema" sino "existe el anti-teorema"). La variante (b) tiene el **perfil exacto de Connes en la tabla de Phase A**: I1 ✅, I2a ✅/◐, I2b ❌, I3 ✅, I4 ✅ → **FAIL I2b**. El input modular existe y es externo, pero no viene con un teorema que haga el trabajo (el análogo del índice de Hodge / Stepanov está ausente). Conforme al criterio endurecido de Phase A, FAIL I2b = programa estancado en el mismo punto que Connes/Deninger/Connes–Consani.

Nota fina sobre el FAIL: no es FAIL I2a (el mecanismo no es *literalmente* una positividad CAP — sus teoremas son incondicionales y $\beta$-ciegos); el modo de fallo es el de la **dicotomía** que se formula en §8.

---

## §8. La dicotomía estructural: interpolación y cuasicristales son el mismo muro visto desde los dos lados

El audit previo destruyó la rigidez cuasicristalina: Kurasov–Sarnak ⟹ toda medida cristalina 1-D $\mathbb{N}$-valuada es el conjunto de ceros toral de un polinomio de Lee–Yang, y "realidad del soporte" = propiedad Lee–Yang = positividad de Hermite = CAP. La interpolación de Fourier es la teoría dual (BRS §2.5: las bases de interpolación *generan* medidas cristalinas; Guinand, Meyer, Lev–Olevskii). El presente audit cierra el otro lado y revela la simetría:

**Dicotomía 8.1.** Todo enunciado de la teoría de interpolación/unicidad/cristalinidad relativo a los ceros de $\zeta$ cae en exactamente una de dos clases:
1. **$\beta$-ciego e incondicional** (Teorema BRS 1.1 con nodos complejos; Corolario 1.1; densidades de Kulikov/KNS; Riemann–von Mangoldt; nuestra completitud Doc 85 y los Teoremas 3.1–3.4): vale igual bajo RH y bajo $\neg$RH, luego **no puede ser palanca**.
2. **$\beta$-sensible y RH-equivalente o RH-condicional** (nodos reales / muestreo no redundante sobre sucesiones reales; cristalinidad de $\sum_\rho \delta_\gamma$; Lee–Yang): aquí la sensibilidad a $\mathrm{Re}(\rho)$ está, pero el enunciado **es** RH (o la asume), luego es CAP con otro nombre.

El lado cuasicristalino colapsa por la rama 2 (Lee–Yang = CAP); el lado interpolatorio colapsa por la rama 1 (incondicional = sin filo). La dualidad de Fourier intercambia las dos ramas pero **mapea el muro sobre sí mismo**. No existe, en el corpus RV/BRS/KNS/KS, un enunciado $\beta$-sensible y no-RH-equivalente: ese enunciado sería precisamente el I2b que falta.

---

## §9. Subproductos que se incorporan al programa

Aunque la ruta se cierra, el audit deja dos resultados y dos gaps nuevos. Para su incorporación al corpus se enuncian en forma citable:

1. **Teorema 101.A (no-estructura; incondicional).** *Sea $\mu$ cualquier medida positiva finita no nula sobre $\mathbb{R}$ y $\{\gamma_n\}$ las ordenadas de los ceros no triviales de $\zeta$. El sistema $\{e^{i\gamma_n s}\}$ en $L^2(\mu)$ no admite cota superior de frame, no es sucesión de Riesz y no es sucesión de interpolación; para $\mu = W_\lambda dm_\infty$ es además completo y sobrecompleto (todo subsistema cofinito es completo, módulo V.1).* — Cierra definitivamente la pregunta que el Doc 85 dejó implícita ("lo que el teorema estándar no puede garantizar directamente es la base de Riesz", Doc 85 §1.2, Obs.): la base de Riesz no es no-garantizada, es **falsa**. Ingredientes: Riemann–von Mangoldt + casillas + continuidad de $\widehat{\mu}$; nada más.

2. **Proposición 101.B (Condición 9; incondicional módulo V.1).** *Para cualquier $\lambda$ fijo con $N(\lambda)\geq 1$: RH $\iff (W_\lambda\,d\nu)^\wedge(\gamma_n) = 0$ para todo $n$.* Se añade a la tabla del Doc 89 §6 con la anotación honesta: CAP-style, no verificable sin posiciones de ceros (MW-7); su interés es de cardinalidad mínima (numerable, sin supremos sobre $\lambda$ ni sobre $z \in \mathbb{H}$) y de forma (es la primera condición del catálogo cuyos puntos de prueba son los propios $\gamma_n$).

3. **Dicotomía 101.C (= 8.1, taxonómica):** todo enunciado del corpus interpolación/unicidad/cristalinidad sobre ceros de $\zeta$ es o bien $\beta$-ciego e incondicional (sin filo), o bien $\beta$-sensible y RH-equivalente/condicional (CAP renombrado). Test de admisión para cualquier candidato futuro de esta familia: exhibir primero un enunciado $\beta$-sensible no-RH-equivalente.

4. **Gap G.101.1:** pertenencia de $\widehat{\nu}$ a $\mathcal{H}_1$ (o a Schwartz tras regularización) — necesaria para activar formalmente (P3)/(P4) del §6.2. Declarado, no resuelto; de interés solo taxonómico dado el veredicto.

5. **Ítem V.1 (heredado, Doc 85):** la verificación Carlson–Beurling sigue pendiente y condiciona la Proposición 101.B y la parte de completitud del Teorema 101.A. Las refutaciones (no-Bessel, no-Riesz, no-interpolación) **no** dependen de V.1.

---

## §10. VEREDICTO

**RUTA CERRADA.**

**Razón precisa, en tres cortes:**

1. **El mecanismo de frames es falso por teorema, no por gap.** La densidad logarítmicamente divergente de los $\gamma_n$ (racimos de tamaño $\log T$, gaps $\to 0$ — todo incondicional, Riemann–von Mangoldt) destruye la cota superior de frame, la cota inferior de Riesz, la minimalidad y la propiedad de interpolación en $L^2(W_\lambda dm_\infty)$, para todo $\lambda$ (Teoremas 3.1–3.4). El decaimiento exponencial $e^{-\pi|s|/2}$ del peso fija el tipo de las transformadas (de ahí la completitud) pero es estructuralmente incapaz de comprar estabilidad cuadrática contra una densidad divergente. No queda ninguna versión cuantitativa del muestreo de $d\nu$ en los ceros que pudiera convertirse en criterio efectivo.

2. **El input modular no evade MW-2/MW-7.** El canal por el que las formas modulares de $\Gamma_\theta$ tocan a $\zeta$ es la modularidad de $\theta$, que es la ecuación funcional de $\zeta$ vía Mellin (Riemann/Hecke) — dato ya poseído y ya inerte frente a la franja crítica. La parte genuinamente nueva de BRS (dualidad **aditiva** ceros↔enteros, estrictamente más fina que la fórmula de Weil, que resulta ser *un* funcional representado en su base) proviene de la serie de Dirichlet, no del producto de Euler: esquiva MW-2 renunciando a la aritmética multiplicativa, y por eso se aplica por igual a series con ceros off-line. Toda la teoría es $\beta$-ciega donde es incondicional y RH-equivalente/condicional donde es $\beta$-sensible (Dicotomía 8.1). El discriminador da **FAIL I2b** — el perfil de Connes: estructura externa real, sin teorema decisivo que fuerce los nodos a $\mathbb{R}$.

3. **La unicidad tipo Heisenberg amplía los teoremas forzantes pero no los datos verificables.** Los pares (P1)–(P4) — incluido el más fuerte disponible en la literatura, el Corolario BRS 1.1 incondicional — fuerzan $d\nu = 0$ a partir de condiciones que requieren $\widehat{\nu}$ o $h$, y por tanto $\zeta_{on}$, y por tanto las posiciones de todos los ceros; además una familia de nodos de BRS *es* el multiconjunto de ceros, y la evaluación vía fórmula explícita reproduce exactamente la descomposición $T_\lambda = A^{off}_\lambda - \sum_p(\log p/\sqrt{p})B_\lambda(\log p)$ del Doc 72 (Proposición 6.1). El muro MW-7 resulta invariante bajo dualidad de Fourier y bajo cambio de base de interpolación: está en el objeto $d\nu$, no en los conjuntos de prueba.

**Se incorporan al programa** los subproductos del §9 (teorema de no-estructura; Condición 9; gaps G.101.1 y V.1 heredado). **No se recomienda** continuar el frente de interpolación como palanca hacia RH; su único uso legítimo futuro es taxonómico (la Dicotomía 8.1 como test rápido: cualquier candidato futuro de esta familia debe exhibir, antes de cualquier otra cosa, un enunciado $\beta$-sensible no-RH-equivalente — el I2b ausente).

---

## Apéndice — Checklist de honestidad

| Afirmación | Estatus |
|---|---|
| Teoremas 3.1, 3.2, 3.4 y Corolario 3.5 (no-Bessel, no-Riesz, no-interpolación, robustez) | **Probados aquí**, incondicionales, autocontenidos (Riemann–von Mangoldt + casillas + continuidad de $\widehat{\mu}$) |
| Teorema 3.3 (sobrecompletitud) y completitud de partida | Incondicionales **módulo V.1** (gap heredado del Doc 85, declarado) |
| Lema 4.1 ($h \in L^2(\mu_\lambda)$) | Probado aquí, incondicional (usa solo la cota de convexidad $\zeta(1/2+it) \ll t^{1/4+\varepsilon}$) |
| Proposición 4.2 / 101.B (Condición 9) | Incondicional módulo V.1; **CAP-style**, no es palanca |
| Enunciados RV y BRS (§1) | Verificados contra fuentes el 2026-06-09; condicionalidad delimitada con precisión (BRS Thm 1.1 incondicional; lectura "nodos reales no redundantes" condicional a RH + simplicidad) |
| Constante de densidad de Kulikov; cobertura exacta de $L_{DH}$ por BRS §5.3 | [NO VERIFICADO], marcado en el texto; ninguna conclusión depende de ello |
| Dicotomía 8.1 / 101.C | Síntesis argumentada sobre el corpus citado; no es un teorema formal — es un patrón sin contraejemplo conocido en RV/BRS/KNS/KS |
| Gap G.101.1 ($\widehat{\nu} \in \mathcal{H}_1$) | Declarado, no resuelto |
| Ninguna prueba de RH, ningún avance sobre $d\nu = 0$ | Correcto: el documento cierra una ruta, no abre una |

## Referencias

**Literatura (verificada el 2026-06-09, salvo marca):**
- D. Radchenko, M. Viazovska, *Fourier interpolation on the real line*, Publ. Math. IHÉS **129** (2019), 51–81. [Enunciado verificado vía el texto de BRS y numdam.]
- A. Bondarenko, D. Radchenko, K. Seip, *Fourier interpolation with zeros of zeta and L-functions*, Constr. Approx. (2023); arXiv:2005.02996v3. [Teorema 1.1, Corolario 1.1, ecs. (1.1)–(1.7), §4.4: verificados directamente sobre el PDF.]
- A. Kulikov, *Fourier interpolation and time-frequency localization*, arXiv:2005.12836. [Cualitativo verificado vía BRS; constante exacta NO VERIFICADA.]
- A. Kulikov, F. Nazarov, M. Sodin, *Fourier uniqueness and non-uniqueness pairs*, J. Math. Phys. Anal. Geom. (2023); arXiv:2306.14013. [Dicotomía super/subcrítica verificada a nivel de resumen.]
- H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, *Universal optimality of the E8 and Leech lattices and interpolation formulas*, Ann. of Math. **196** (2022). [Contexto; no re-verificado en detalle.]
- P. Kurasov, P. Sarnak, *The arithmetic of Lee–Yang/Fourier quasicrystals*, arXiv:2307.13498. [Vía NOVEL-STRUCTURE-SEARCH.]
- Beurling–Malliavin (1962); Korevaar (2004); Seip (2004): teoría clásica de completitud/densidad, citada como en Doc 85.

**Programa:** Docs 70, 71, 72, 76, 82, 83, 85, 89; P39; meta-docs DISCRIMINATOR-hardening-phase-A (criterios I1/I2a/I2b/I3/I4), NOVEL-STRUCTURE-SEARCH-survivors (destrucción de Kurasov–Sarnak; punto abierto sobre interpolación, resuelto aquí).

---

*Fin del Documento 101. La teoría dual de los cuasicristales queda auditada: el muro es el mismo y la dualidad lo deja invariante. RUTA CERRADA, con dos subproductos incondicionales y dos gaps declarados.*
