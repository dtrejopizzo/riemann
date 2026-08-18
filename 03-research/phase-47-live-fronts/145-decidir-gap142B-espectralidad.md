# Doc 145 — Decidir GAP-142.B: la espectralidad del objeto semilocal arquimediano

**Programa:** Hipótesis de Riemann — Phase 47: frentes vivos.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 142 (objeto semilocal $X_S^{\mathrm{ar}}$; peso $\Omega$; Teorema A de ventana corta; Teorema B del fallo; identidad de transmisión; trilema §8; contrapositiva $H^+\Rightarrow$ no-espectral; GAP-142.B); Doc 135 (teorema de dos primos; "espectral" = suma de cuadrados sobre progresiones verticales; H⁺ en P48); Doc 131 §4–§6 (Def. 4.1 objeto espectral; Teo. 4.4 órbitas; Teo. 6.3 H-por-bloques ⟺ divisor en la línea; Def. 6.1 Axioma H; Conjetura H⁺ = Deseo 6.9).
**Contrato creativo:** [DEFINICIÓN-NUEVA] libertad total; [TEOREMA]/[PROPOSICIÓN]/[LEMA] con prueba completa o no llevan etiqueta; [PUENTE] con estatus declarado; [GAP]/[DESEO] nombrados; [DATO] literatura real. Franqueza absoluta. Sin numéricos: solo forma cerrada (digamma/Gamma, integrales y series evaluables simbólicamente).

**Convenciones (las de Doc 142, fijadas una vez).** $G=\mathbb R_+^*$, $d^*x=dx/x$, $f\in C_c^\infty(G)$, $F(t)=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R)$, $\hat F(\xi)=\int_{\mathbb R}F(t)e^{i\xi t}dt$, $\hat f(\tfrac12+i\xi)=\hat F(\xi)$, $g=f\star\tilde f$, $\hat G(\xi)=|\hat F(\xi)|^2$, $\|f\|_w^2=\|F\|_{L^2}^2$. El peso arquimediano (Doc 142, Def. 1.1):
$$\Omega(\xi)=\operatorname{Re}\psi\bigl(\tfrac14+\tfrac{i\xi}2\bigr)-\log\pi,\qquad \mathcal A(f)=\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi.$$
$\psi=\Gamma'/\Gamma$ digamma, $\gamma$ Euler. Recuérdese $\Omega(0)=-\gamma-\tfrac\pi2-3\log2-\log\pi<0$ (Doc 142, Lema 2.2) y $\Omega<0$ exactamente en $(-\xi_*,\xi_*)$ (Lema 2.3).

---

## 0. Resumen ejecutivo

GAP-142.B pedía decidir el trilema de la Conjetura H⁺: el contraejemplo del Doc 142 ($X_S^{\mathrm{ar}}$ viola H) verifica TODAS las hipótesis de H⁺ salvo la **espectralidad** del objeto semilocal. El Doc 142 dejó la contrapositiva ($H^+\Rightarrow$ no-espectral) y nombró tres ramas: (1) espectral ⟹ H⁺ refutada; (2) no-espectral ⟹ H⁺ colapsa hacia RH; (3) indecidible. Este documento decide.

**Veredicto: el objeto semilocal NO es espectral en el sentido del programa (Doc 131, Def. 4.1, con divisor en la línea crítica) — rama (2).** La obstrucción no es heurística: es un **teorema** (Teorema 3.4 abajo). Su núcleo es elemental y robusto:

- "Espectral con divisor en la línea" ⟹ $Q\ge0$ (suma de cuadrados, Doc 131 Prop. 6.2). El Teorema B del Doc 142 da $Q_S(f_T)<0$. Luego **no hay divisor en la línea**: rama de espectralidad-en-línea cerrada incondicionalmente.
- La pieza decisiva, **nueva aquí**, es que la NO-espectralidad ya vive en el **núcleo arquimediano** $\mathcal A$ solo, antes de tocar primos o polo: $\mathcal A$ es una forma cuadrática cuyo **símbolo $\Omega$ cambia de signo** (Lema 2.3 de Doc 142). Una forma $\int|\hat F|^2\,\Omega$ es representable como medida espectral positiva $\sum_k|\langle F,e_k\rangle|^2$ (con $e_k$ exponenciales/evaluaciones) **si y solo si** $\Omega\ge0$ c.t.p. (Teorema 2.2 abajo, vía Bochner). Como $\Omega(0)<0$, **falla**. El término arquimediano de tipo $\zeta$ es intrínsecamente **unilateral con parte negativa**: NO es la transformada de una medida positiva, es una distribución de Weil con densidad de signo indefinido.

**Consecuencia para H⁺ (Teorema 4.1):** H⁺ NO es más débil que RH. Su único contenido no trivial es la hipótesis de espectralidad, y para objetos con arquimediano de tipo $\zeta$ la espectralidad-positiva es esencialmente RH (fuerza el divisor a la línea, que para $\zeta_{\mathrm{ob}}$ ES RH). H⁺ truncada a $S$ finito queda **vaciada** (su clase es vacía: ningún $X_S^{\mathrm{ar}}$ con $S$ finito es espectral-positivo). GAP-135.B estaba mal planteado: el objeto semilocal nunca estuvo en la clase de H⁺. **Resultado negativo: se cierra la ruta ilusoria de interpolación semilocal.**

**Lo que sobrevive incondicionalmente (§5):** el Teorema A de Doc 142 (positividad de ventana corta, $Q_S\ge\tfrac3{10}\|f\|_w^2$ para $2T\le\tfrac1{150}$, uniforme en $S$, incluye $\zeta$) y la identidad de transmisión (Prop. 6.1 de Doc 142) **no dependen del trilema** — son hechos sobre la forma $Q_S$, no sobre su representación. Siguen en pie y se reenuncian.

---

## 1. [DEFINICIÓN-NUEVA] "Espectral" con total precisión

El Doc 131 (Def. 4.1) y el Doc 135 usan "espectral" de modos que conviene separar nítidamente, porque el trilema se juega exactamente en la diferencia entre ellos.

**[DEFINICIÓN-NUEVA 1.1] (espectral-EF: el sentido amplio de Doc 131, Def. 4.1).** Un objeto hermitiano $X$ es **espectral-EF** si existe un multiconjunto numerable $Z\subset\mathbb C$ (el **divisor**), con partes reales acotadas y función de conteo $N_Z(T)=\#\{\rho\in Z:|\operatorname{Im}\rho|\le T\}\ll T^A$ para algún $A<\infty$ (**densidad polinomial**), tal que
$$\sum_{\rho\in Z}\hat f(\rho)\;=\;W_X(f)\qquad\forall f\in C_c^\infty(G),$$
con convergencia absoluta. (Es la fórmula explícita del objeto.)

**[DEFINICIÓN-NUEVA 1.2] (espectral-positivo: el sentido fuerte, programa/Doc 135).** Un objeto hermitiano $X$ espectral-EF con divisor $Z$ es **espectral-positivo** si además $Z\subset\{\operatorname{Re}s=\tfrac12\}$ ($\sigma$-estable con $\sigma\rho=\rho$). Entonces, escribiendo $\rho=\tfrac12+i\xi$ y multiplicidades $m_\rho$,
$$Q_X(f)\;=\;\sum_{\rho\in Z}m_\rho\,\hat f(\rho)\,\overline{\hat f(\sigma\rho)}\;=\;\sum_{\rho\in Z}m_\rho\,\bigl|\hat F(\operatorname{Im}\rho)\bigr|^2\;\ge\;0$$
(Doc 131, Teo. 4.4(a) + Prop. 6.2). En el caso de primos puros (Doc 135, Teo. 3.1) esto es exactamente $Q_X(f)=2\sum_{\Lambda_p}|\hat F|^2$: **suma de cuadrados de evaluaciones de $\hat F$ sobre las progresiones verticales** $\Lambda_p=\{\log p,2\log p,\dots\}$ leídas en el eje de frecuencias. Esta es la representación que H⁺ pide (P48, Conjecture 7.1: "$X$ espectral"); el contenido operacional de "espectral" en la conjetura es **espectral-positivo**.

**[OBSERVACIÓN 1.3] (por qué esta es la lectura correcta para H⁺).** H⁺ concluye $Q_X\ge0$. Si "espectral" significara solo espectral-EF (divisor en cualquier sitio), entonces por Doc 131 Teo. 6.3, un divisor con un punto fuera de la línea fuerza un bloque hiperbólico con dirección negativa: la conclusión $Q_X\ge0$ sería falsa para tales objetos, y H⁺ sería trivialmente falsa por razones ajenas al semilocal. La única lectura bajo la cual H⁺ es una conjetura sustantiva (no trivialmente falsa) es: **"espectral" = espectral-positivo = divisor en la línea**. Con esa lectura, "$X$ espectral $\Rightarrow$ $Q_X\ge0$" es un **teorema** (Prop. 6.2), y H⁺ dice "los datos $(a\ge0,\text{Euler},\text{polar},\Gamma)$ fuerzan que el levantamiento espectral exista y caiga en la línea". Adoptamos esta lectura. Hace la contrapositiva del Doc 142 (Teo. 8.1) un teorema genuino: si $Q_S<0$ para algún $f$, entonces $X_S^{\mathrm{ar}}$ no admite divisor en la línea, i.e. no es espectral-positivo.

**[OBSERVACIÓN 1.4] (la tercera lectura, off-line, y por qué no salva H⁺).** Podría intentarse "espectral con divisor fuera de la línea pero positivo por otra estructura". Pero Doc 131 Teo. 4.4(a) es una identidad: para CUALQUIER divisor $\sigma$-estable, $Q_X(f)=\sum_\rho m_\rho\hat f(\rho)\overline{\hat f(\sigma\rho)}$, y un punto $\rho_0$ con $\operatorname{Re}\rho_0\ne\tfrac12$ contribuye un plano hiperbólico de signatura $(1,1)$ (Teo. 4.4(b)), realizado como dirección negativa por el Lema de evaluación 4.3. Luego **divisor off-line ⟹ $Q_X$ indefinida**. No hay "espectral-positivo con divisor off-line": espectral-positivo ⟺ divisor en la línea, sin escapatoria. Esto cierra la rama (3) del trilema del Doc 142 §8 (la sub-opción "divisor exótico") como caso de la rama (1)/(2), no como tercera vía.

Resumen del marco: **"$X$ espectral" en H⁺ = espectral-positivo = la forma de Weil $Q_X$ se representa como $\sum_k|\langle F,e_k\rangle|^2$ con $e_k(t)=e^{i\xi_k t}$, $\xi_k$ las alturas del divisor en la línea.** Decidir GAP-142.B = decidir si $Q_S$ (equivalentemente $\mathcal A$, ver §3) admite tal representación.

---

## 2. El término arquimediano NO es la forma de una medida espectral positiva

Aquí está el corazón analítico. Aislamos la pregunta de representación para la forma cuadrática $\mathcal A$, sin polo ni primos, y la decidimos con una caracterización tipo Bochner.

**[DEFINICIÓN-NUEVA 2.1] (forma con medida espectral; representación por evaluaciones).** Una forma cuadrática $\mathcal B(f)=\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,d\nu(\xi)$ sobre $C_c^\infty(G)$, dada por una medida/distribución temperada $\nu$ par, **admite representación espectral positiva** si existe una medida de Borel **positiva** $\mu\ge0$ sobre $\mathbb R$, de crecimiento polinomial, tal que $\mathcal B(f)=\int_{\mathbb R}|\hat F(\xi)|^2\,d\mu(\xi)$ para todo $f$. (Cuando $\mu=\sum_k m_k\delta_{\xi_k}$ es atómica con densidad polinomial, esto es exactamente $\mathcal B(f)=\sum_k m_k|\hat F(\xi_k)|^2=\sum_k m_k|\langle F,e^{i\xi_k\cdot}\rangle|^2$: suma de cuadrados de evaluaciones — el sentido espectral-positivo de la Def. 1.2 con $e_k$ las exponenciales del divisor.)

**[TEOREMA 2.2] (criterio de positividad del símbolo).** Sea $w\in L^1_{\mathrm{loc}}(\mathbb R)$ par, real, de crecimiento polinomial, y $\mathcal B_w(f)=\frac1{2\pi}\int|\hat F(\xi)|^2 w(\xi)\,d\xi$. Entonces:
$$\mathcal B_w\ \text{admite representación espectral positiva}\quad\Longleftrightarrow\quad w(\xi)\ge0\ \text{para casi todo }\xi\in\mathbb R.$$
Más aún, $\mathcal B_w(f)\ge0$ para todo $f\in C_c^\infty(G)$ ($\iff$ para todo $F\in C_c^\infty(\mathbb R)$) $\iff w\ge0$ c.t.p.

*Demostración.* ($\Leftarrow$) Si $w\ge0$ c.t.p., $d\mu:=\tfrac1{2\pi}w(\xi)\,d\xi$ es una medida positiva de crecimiento polinomial y $\mathcal B_w(f)=\int|\hat F|^2\,d\mu$: representación positiva, y $\mathcal B_w(f)\ge0$ trivialmente.

($\Rightarrow$, positividad ⟹ $w\ge0$ c.t.p.) Supongamos $\mathcal B_w(f)\ge0$ para todo $F\in C_c^\infty(\mathbb R)$. Sea $E:=\{\xi:w(\xi)<0\}$ y supongamos $|E|>0$ (medida de Lebesgue positiva). Por regularidad existe un punto de densidad de Lebesgue $\xi_0$ de $E$; por paridad de $w$ podemos tomar $\xi_0\ge0$, y si $\xi_0>0$ también $-\xi_0\in E$. Elijamos un test cuya masa espectral $|\hat F|^2$ se concentre cerca de $\{\pm\xi_0\}$ dentro de $E$. Concretamente: sea $\phi\in C_c^\infty(\mathbb R)$ con $\hat\phi\in C_c^\infty$, $\hat\phi\ge0$, $\operatorname{supp}\hat\phi\subset[-1,1]$, $\hat\phi(0)>0$; para $\delta>0$ y $R>0$ pongamos $\hat F_{\delta,R}(\xi):=\hat\phi\bigl(\tfrac{\xi-\xi_0}\delta\bigr)+\hat\phi\bigl(\tfrac{\xi+\xi_0}\delta\bigr)$ (par; corresponde a un $F$ real modulado, $F_{\delta,R}\in\mathcal S$ y aproximable en $C_c^\infty$). Entonces $|\hat F_{\delta,R}|^2$ es una bump de anchura $O(\delta)$ centrada en $\pm\xi_0$ (los dos términos tienen soportes disjuntos para $\delta<\xi_0$), masa total $\asymp\delta\|\hat\phi\|_2^2$ en cada lado, y
$$2\pi\,\mathcal B_w(F_{\delta,R})=\int|\hat F_{\delta,R}|^2 w=2\int\hat\phi\bigl(\tfrac{\xi-\xi_0}\delta\bigr)^2 w(\xi)\,d\xi=2\delta\int\hat\phi(u)^2\,w(\xi_0+\delta u)\,du.$$
Por ser $\xi_0$ punto de densidad de $E$ y $w$ localmente integrable, $\tfrac1{2H}\int_{\xi_0-H}^{\xi_0+H}w\to w$-promedio $<0$; más finamente, como $\xi_0$ es punto de Lebesgue de $w$ (c.t.p. lo es) y $\xi_0\in E$ punto de densidad, el promedio $\int\hat\phi(u)^2 w(\xi_0+\delta u)\,du\to w(\xi_0)\int\hat\phi^2<0$ cuando $\delta\to0$ (eligiendo $\xi_0$ punto de Lebesgue con $w(\xi_0)<0$, lo cual ocurre en c.t.p. de $E$ pues $|E|>0$). Luego $\mathcal B_w(F_{\delta,R})<0$ para $\delta$ pequeño: contradice $\mathcal B_w\ge0$. Por tanto $|E|=0$, i.e. $w\ge0$ c.t.p. La equivalencia con representación positiva sigue por ($\Leftarrow$) (representación ⟹ positiva trivialmente, y positiva ⟹ $w\ge0$ ⟹ representación). El caso $C_c^\infty(\mathbb R)$ vs $\mathcal S$: $C_c^\infty$ es denso y la forma es continua en la topología relevante, así que basta aproximar $F_{\delta,R}$ por $C_c^\infty$ con pérdida arbitrariamente pequeña. $\square$

**[OBSERVACIÓN 2.3] (esto es Bochner del lado correcto).** El Teorema 2.2 es la versión "símbolo" del teorema de Bochner [DATO: Bochner, *Lectures on Fourier integrals*, Princeton 1959; o Reed–Simon II, Thm IX.9]. La forma $f\mapsto\int|\hat F|^2 d\nu$ es la forma cuadrática asociada al **multiplicador de Fourier** $w$; es un funcional de tipo positivo en $F$ ⟺ su símbolo $w$ es $\ge0$ ⟺ $\nu$ es una medida positiva ⟺ existe una "densidad espectral positiva". El contenido es elemental pero decisivo: **la positividad de una forma diagonal en Fourier es puntual en el símbolo**. No hay forma de comprar un símbolo negativo en una región con masa positiva en otra: las direcciones se separan en frecuencia.

**[TEOREMA 2.4] (el peso arquimediano no es representable: la decisión analítica).** El término arquimediano $\mathcal A(f)=\frac1{2\pi}\int|\hat F|^2\Omega$ **NO** admite representación espectral positiva; equivalentemente, $\mathcal A$ **no es** una suma de cuadrados de evaluaciones $\sum_k m_k|\hat F(\xi_k)|^2$ con pesos $m_k\ge0$. La obstrucción es exacta y localizada:
$$\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma-\tfrac\pi2-3\log2-\log\pi<0,\qquad \Omega<0\ \text{en }(-\xi_*,\xi_*),\ \xi_*>0.$$

*Demostración.* Por el Teorema 2.2 con $w=\Omega$: $\mathcal A$ admite representación espectral positiva ⟺ $\Omega\ge0$ c.t.p. Pero $\Omega$ es continua (Doc 142, Lema 2.1) y $\Omega(0)<0$ (Lema 2.2), luego $\Omega<0$ en un entorno de $0$ de medida positiva — de hecho exactamente en $(-\xi_*,\xi_*)$ con $\xi_*>0$ por monotonía estricta (Lema 2.3). Por contrapositiva del Teorema 2.2, $\mathcal A$ no es representable y de hecho $\mathcal A$ es **indefinida**: existe $f$ con $\mathcal A(f)<0$ (tómese masa espectral concentrada en $(-\xi_*,\xi_*)$; es el mecanismo del Teorema B de Doc 142, $\eta$ lenta y ancha). $\square$

**[OBSERVACIÓN 2.5] (la lectura espectral correcta de $\Omega$: ceros triviales, multiplicidad NEGATIVA).** ¿Tiene $\Omega$ *alguna* representación espectral, aunque no positiva? Sí, y es instructiva. $\Omega$ es la contribución del factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ a la fórmula de Riemann–Weil. En la fórmula explícita completa, el término arquimediano se escribe (Weil 1952; Connes 1999) como
$$\mathcal A(f)=-\,g(1)\log\pi+\frac1{2\pi}\int_{\mathbb R}\hat F(\xi)\,\operatorname{Re}\psi\bigl(\tfrac14+\tfrac{i\xi}2\bigr)\,\overline{\hat F(\xi)}\,d\xi,$$
y la identidad de Hadamard para $\Gamma$ da el desarrollo de $\Omega$ como suma sobre los **polos de $\Gamma(s/2)$**, i.e. los **ceros triviales** de $\zeta$ en $s=-2,-4,-6,\dots$ Estos NO están en la línea crítica; entran en la fórmula explícita con el signo que en el lenguaje de Doc 131 corresponde a **multiplicidad/posición que produce signatura indefinida**. En efecto: la "densidad espectral" de $\Omega$, como distribución de Weil, es $\Omega(\xi)$ misma, y su parte negativa $\Omega\mathbf 1_{(-\xi_*,\xi_*)}$ es exactamente la "masa espectral de signo negativo" que ninguna medida positiva puede reproducir. La unilateralidad que el Doc 142 §7 [GAP-142.B.2] señaló — "el término de primos es una mitad con peso espejo, no las sumas de Poisson bilaterales de progresiones verticales completas" — es la misma obstrucción vista del lado aritmético: **el divisor que representaría a $X_S^{\mathrm{ar}}$ tendría que incluir los ceros triviales (off-line, con su contribución de signo indefinido), y por tanto NO sería un divisor en la línea.** Espectral-EF: posiblemente (con ceros triviales + lo que ponga el polo + los primos); espectral-**positivo**: imposible. Esa es la decisión.

**[OBSERVACIÓN 2.6] (contraste con los primos puros de Doc 135, donde SÍ funcionaba).** Para un primo puro, el peso espectral del factor de Euler era $W_F(f)=L_p\sum_m c_m f(p^m)$ con $|c_m|=2p^{m/2}$ en el borde de Ramanujan, y el divisor caía exactamente en la línea (pureza), dando $Q=2\sum_{\Lambda_p}|\hat F|^2\ge0$: símbolo "$\ge0$" porque era literalmente una suma de cuadrados de evaluaciones. El factor de Euler puro es un **peso de tipo positivo** (medida atómica positiva sobre la progresión vertical). El factor $\Gamma$, en cambio, tiene símbolo $\Omega$ con parte negativa: **no es un factor de tipo positivo**. La diferencia entre Doc 135 (espectral, H vale) y Doc 142 (no espectral-positivo, H falla) es exactamente la diferencia entre un símbolo $\ge0$ y un símbolo de signo indefinido. El régimen "destructivo" del Doc 142 ES la negatividad del símbolo arquimediano.

---

## 3. La forma completa $Q_S$ hereda la no-positividad del símbolo

El bloque polar y los primos no cambian el veredicto, y conviene verlo con precisión porque la espectralidad es del objeto completo, no solo de $\mathcal A$.

**[PROPOSICIÓN 3.1] (la negatividad sobrevive a los otros bloques: ya está en Doc 142).** Para todo $S$ finito (incluido $\varnothing$) existe $f$ con $Q_S(f)<0$. *(Es el Teorema B de Doc 142, Teo. 5.1: la familia $f_T$ con $\hat f_T(1)=0$ mata el polar, los primos suman $+B_S\|\eta\|^2$ con su peor signo, y $\mathcal A(f_T)\to\Omega(0)\|\eta\|^2<0$; total $(\Omega(0)-B_S)\|\eta\|^2<0$.)* $\square$

**[TEOREMA 3.4] (GAP-142.B decidido: $X_S^{\mathrm{ar}}$ no es espectral-positivo).** Para todo $S$ finito (incluido $S=\varnothing$), el objeto semilocal $X_S^{\mathrm{ar}}$ **no es espectral-positivo** (Def. 1.2): no existe divisor $Z\subset\{\operatorname{Re}=\tfrac12\}$ de densidad polinomial con $\sum_{\rho\in Z}\hat f(\rho)=W_{X_S^{\mathrm{ar}}}(f)$. Equivalentemente, $Q_S$ **no** se representa como $\sum_k m_k|\hat F(\xi_k)|^2$ con $m_k\ge0$.

*Demostración.* Dos pruebas independientes, ambas completas.

*(A) Vía la forma completa.* Si $X_S^{\mathrm{ar}}$ fuera espectral-positivo, por Doc 131 Prop. 6.2 (= Def. 1.2) tendríamos $Q_S(f)=\sum_{\rho\in Z}m_\rho|\hat F(\operatorname{Im}\rho)|^2\ge0$ para todo $f$. Contradice la Proposición 3.1 ($Q_S(f_T)<0$). $\square_A$

*(B) Vía el símbolo arquimediano, localizando la obstrucción.* Aun antes de invocar la familia $f_T$ completa, la obstrucción ya vive en $\mathcal A$. Restrinjámonos a tests con polar y primos apagados de forma exacta: tómese $f$ con $\operatorname{supp}F\subset(\,\tau,\ \tau+\ell\,)$ para $\ell<\log2$ y $\tau$ tal que ningún $mL_p$ ($p\in S$) caiga en $(-\ell,\ell)$ — automático para $\ell<\log2\le mL_p$ — de modo que $P_S(f)=0$; y con $\hat f(1)=0$ para matar el polar (una condición lineal, posible sin vaciar $C_c^\infty$). Para tal clase, $Q_S(f)=\mathcal A(f)$ exactamente. Por el Teorema 2.4, $\mathcal A$ es indefinida con direcciones negativas concentradas en $(-\xi_*,\xi_*)$. La masa espectral en frecuencias bajas se obtiene con tests anchos; combinando con $\hat f(1)=0$ (costo $e^{-T/8}$, Doc 142 Teo. 5.1 paso 0) y $P_S=0$ (ventana evitando los lags — alternativamente la familia $f_T$ ancha cuyos primos suman $+B_S$, que solo refuerza la negatividad), se realiza $Q_S(f)<0$. Pero más importante que el signo: **la representación espectral-positiva es imposible por razón estructural, no de tamaño.** Si existiera medida $\mu\ge0$ atómica en la línea con $Q_S(f)=\int|\hat F|^2 d\mu$, entonces en particular para los tests con $P_S=0$ y polar muerto tendríamos $\mathcal A(f)=\int|\hat F|^2 d\mu\ge0$ — i.e. $\mathcal A$ admitiría representación positiva, contradiciendo el Teorema 2.4 ($\Omega(0)<0$). $\square_B$

Las dos pruebas coinciden en el veredicto y lo localizan: la no-espectralidad-positiva de $X_S^{\mathrm{ar}}$ es **arquimediana de origen** (el símbolo $\Omega$ con parte negativa), heredada intacta por la forma completa. $\square$

**[OBSERVACIÓN 3.5] (el divisor espectral-EF sí existe — es $\zeta$ truncada, off-line).** $X_S^{\mathrm{ar}}$ no carece de toda estructura espectral: tiene una representación espectral-EF (Def. 1.1, divisor en cualquier sitio) en el sentido débil, porque sus tres bloques son evaluaciones de Mellin y la fórmula de Riemann–Weil truncada lo expresa vía ceros triviales (del $\Gamma$), el polo ($\xi=-i/2$), y los ceros del producto parcial $\prod_{p\in S}(1-p^{-s})^{-1}$ — pero ese divisor **vive fuera de la línea** (ceros triviales en $\operatorname{Re}=-2,-4,\dots$; polos de los factores de Euler en $\operatorname{Re}=0$). Doc 131 Teo. 4.4(b)/6.3: un divisor con puntos off-line da $Q$ indefinida. Coherente con todo: $X_S^{\mathrm{ar}}$ es (a lo sumo) espectral-EF con divisor off-line, **nunca** espectral-positivo. La rama (1) del trilema (espectral-positivo ⟹ H⁺ refutada) está **vacía de hipótesis**: el antecedente nunca se cumple. La rama operante es la (2).

---

## 4. Consecuencia para H⁺: no es más débil que RH; colapsa

**[TEOREMA 4.1] (veredicto del trilema: rama (2) — H⁺ colapsa hacia RH).** Bajo la lectura forzada "espectral = espectral-positivo" (Obs. 1.3, la única que hace H⁺ no-trivialmente-falsa):

(a) **H⁺ sobrevive como enunciado** (no es refutada): su único contraejemplo candidato, $X_S^{\mathrm{ar}}$, NO está en su clase, porque no es espectral-positivo (Teorema 3.4). La contrapositiva del Doc 142 (Teo. 8.1, $H^+\Rightarrow$ no-espectral) se realiza como **hecho**: $X_S^{\mathrm{ar}}$ efectivamente no es espectral. No hay contradicción.

(b) **Pero H⁺ NO es más débil que RH.** La hipótesis de espectralidad-positiva carga el 100% del contenido: para un objeto hermitiano con bloque polar $[0]+[1]$ y peso arquimediano de tipo $\zeta$ (símbolo $\Omega$ con parte negativa), pedir un divisor en la línea **fuerza** que el déficit arquimediano negativo $\Omega\mathbf 1_{(-\xi_*,\xi_*)}$ sea compensado exactamente por el lado del divisor. Las hipótesis restantes (hermitiano + $a=\Lambda\ge0$ Euler + polar + $\Gamma$) son **consistentes con violaciones de H de tamaño $\ge|\Omega(0)|\approx5.37$** (Teorema 3.4 / Doc 142 Teo. 5.1). Luego no aportan positividad. Toda la fuerza está en "existe divisor en la línea", que para el dato completo ($a=\Lambda$ en TODOS los primos) ES la afirmación de que los ceros de $\zeta$ están en la línea: **RH misma**.

(c) **H⁺ truncada a $S$ finito está vacía** (Corolario 4.2 abajo): la clase "objetos espectral-positivos con $S$ finito + $\Gamma$" no contiene ningún $X_S^{\mathrm{ar}}$. La única instancia no vacía de la clase de H⁺ con peso $\Gamma$ es el producto de Euler **completo** (todos los primos), i.e. $\zeta_{\mathrm{ob}}$, y allí espectral-positivo ⟺ RH. H⁺ es **RH disfrazada para objetos con arquimediano**.

*Demostración.* (a) Teorema 3.4. (b) La consistencia de las hipótesis con $Q_S<0$ es el Teorema 3.4 (B); que la espectralidad-positiva implique divisor-en-línea es la Def. 1.2; que para $a=\Lambda$ completo esto sea RH es el criterio de Weil [DATO: Weil 1952; Bombieri 2000] y Doc 131 PUENTE 7.1. (c) Corolario 4.2. $\square$

**[COROLARIO 4.2] (la clase semilocal de H⁺ es vacía; GAP-135.B estaba mal planteado).** No existe ningún $X_S^{\mathrm{ar}}$ con $S$ finito que sea simultáneamente (hermitiano + $a\ge0$ Euler + polar estándar + $\Gamma$) Y espectral-positivo. Por tanto la pretensión de Doc 135 §9 / GAP-135.B — que el objeto semilocal de dos primos con arquimediano fuera "el primer caso genuino, más débil que RH, de H⁺" — es **falsa**: el objeto nunca estuvo en la clase de H⁺. *(Inmediato del Teorema 3.4: $X_S^{\mathrm{ar}}$ no es espectral-positivo para ningún $S$ finito.)* $\square$

**[OBSERVACIÓN 4.3] (resultado negativo, su valor).** Esto cierra una ruta ilusoria del programa, que es exactamente lo que el encargo pedía evaluar como hallazgo valioso. La esperanza de Doc 135/P48 era una **interpolación semilocal**: probar H⁺ para $S$ finito (más fácil que RH) y dejar el límite $S\to\infty$ como GAP. El Teorema 3.4 muestra que **no hay tal escalón intermedio**: en cuanto se añade el peso $\Gamma$ (símbolo con parte negativa), el único objeto de la clase es $\zeta$ completa y la conjetura es RH. El muro de Doc 142 §8 ("no hay interpolación semilocal entre el teorema de dos primos constructivo y RH; el primer paso destructivo cuesta todo el precio") queda **redibujado con precisión**: el precio es la espectralidad-positiva con símbolo arquimediano negativo, y ese precio es RH. Reformulación franca de la conjetura superviviente (H⁺-completa, Doc 142 §8): *hermitiano + espectral-positivo + $a=\Lambda$ completo + polar + $\Gamma$ ⟹ H* — y aquí "espectral-positivo" ⟺ "divisor en la línea" ⟺ RH, así que la conjetura es **RH ⟹ RH**, tautológica. H⁺ no ofrece ningún contenido por debajo de RH.

---

## 5. Lo que sobrevive incondicionalmente (independiente del trilema)

El veredicto del trilema es sobre la **representación** de $Q_S$. Dos resultados del Doc 142 son sobre la **forma** $Q_S$ misma y no dependen de cómo caiga la espectralidad; los reenunciamos como supervivientes.

**[TEOREMA 5.1] (= Teorema A de Doc 142, reafirmado).** Para todo $S$ (finito, infinito o todos los primos, incluido $\zeta$) y todo $f\in C_c^\infty(G)$ de ventana $2T\le\tfrac1{150}$:
$$Q_S(f)\;\ge\;\tfrac3{10}\,\|f\|_w^2.$$
**Estatus tras GAP-142.B:** intacto. La prueba (Doc 142 §3) no usa ninguna representación espectral: descompone $Q_S$ en sus tres bloques y usa $\Omega(\xi)\sim\log|\xi|>0$ a alta frecuencia (forzada por incertidumbre en ventana corta), $P_S=0$ (lags lejanos), polar $=O(T)$. Es positividad **directa de la forma**. Dice, independiente del trilema: **la clase de datos de H⁺ satisface H restringida a ventanas cortas, incondicionalmente y uniforme en el dato** (incluye $\zeta$). Es la primera positividad de Weil del programa con término arquimediano, y sobrevive entera. *(El [DESEO] del encargo original — dominación arquimediana hasta soporte $\theta\log(p_1\cdots p_n)$ — sigue siendo falso como estaba: el umbral es absoluto $O(1)$, arquimediano, no escala con el conductor; GAP-142.A.)* $\square$

**[PROPOSICIÓN 5.2] (= identidad de transmisión, Prop. 6.1 de Doc 142, reafirmada).** Para todo $f$ y todo $S$ finito, incondicionalmente:
$$Q_S(f)\;=\;\underbrace{\sum_{\rho}\hat g(\rho)}_{Q_{\mathrm{full}}(f),\ \text{Riemann–Weil}}\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr].$$
**Estatus tras GAP-142.B:** intacto (es álgebra + fórmula explícita de Weil, [DATO: Weil 1952]). Lo que ahora dice, a la luz del veredicto: el déficit de transmisión $D_S=B_S-\Omega(0)>0$ que mide la violación (Doc 142 Cor. 6.2, bajo RH) es **exactamente** la masa espectral negativa del símbolo $\Omega$ que ningún divisor en la línea puede absorber sin el producto de Euler completo. La identidad localiza dónde el límite $S\to$ todos-los-primos deja de conmutar con la positividad: en la transmisión de la custodia del polo ($\xi=-i/2$) al eje real, que solo la suma completa de primos realiza. Esto **redistribuye** GAP-135.B a la espectralidad — y §3–§4 la decidieron. $\square$

**[PROPOSICIÓN 5.3] (= cono superviviente, Prop. 7.2 de Doc 142, reafirmada).** Con polar muerto y masa espectral baja $\le\varepsilon_S\|f\|_w^2$ bajo $\bar\xi_S$ (definido por $\Omega(\bar\xi_S)=B_S+2$), se tiene $Q_S(f)\ge\|f\|_w^2$. **Estatus:** intacto, por la misma razón (positividad directa de la forma, sin representación). $\square$

**[OBSERVACIÓN 5.4] (lo que sobrevive es positividad de FORMA, no de representación).** La lección estructural de GAP-142.B: hay que distinguir dos preguntas que el programa había fundido. (i) *¿Es $Q_S\ge0$?* — pregunta de **forma**; respuesta: no en general (Teo. B), sí en conos explícitos (Teoremas 5.1, 5.3). (ii) *¿Es $Q_S=\sum|\text{evaluaciones}|^2$?* — pregunta de **representación espectral-positiva**; respuesta: no (Teorema 3.4), porque el símbolo arquimediano tiene parte negativa. La pregunta (ii) es estrictamente más fuerte que la (i): representación positiva ⟹ forma positiva, no al revés. H⁺ pedía (ii) y por eso era RH. Los teoremas que sobreviven son todos de tipo (i) en regiones donde la parte negativa del símbolo está forzada a tener masa pequeña.

---

## 6. El mapa

**Probado [TEOREMA/PROPOSICIÓN/LEMA] con prueba completa aquí:**
- **[TEOREMA 2.2]:** criterio de positividad del símbolo (Bochner del lado del multiplicador): $\int|\hat F|^2 w\ge0\ \forall F$ ⟺ $w\ge0$ c.t.p. ⟺ representación espectral positiva.
- **[TEOREMA 2.4]:** el peso arquimediano $\Omega$ NO admite representación espectral positiva, porque $\Omega(0)<0$ ($\Omega<0$ en $(-\xi_*,\xi_*)$). El término $\Gamma$ es unilateral con parte negativa: no es transformada de medida positiva; su "densidad espectral" son los ceros triviales (off-line) con signo indefinido (Obs. 2.5).
- **[TEOREMA 3.4]:** **GAP-142.B decidido — $X_S^{\mathrm{ar}}$ NO es espectral-positivo, para todo $S$ finito** (dos pruebas: vía forma completa y vía símbolo arquimediano). Rama (2) del trilema.
- **[TEOREMA 4.1] + [COROLARIO 4.2]:** consecuencia para H⁺ — no es más débil que RH; la clase semilocal de H⁺ es **vacía**; GAP-135.B estaba mal planteado; H⁺-completa es tautológica (RH ⟹ RH). Resultado negativo: ruta de interpolación semilocal cerrada.
- **[TEOREMA 5.1], [PROP. 5.2], [PROP. 5.3]:** Teorema A, identidad de transmisión y cono superviviente del Doc 142 **reafirmados incondicionalmente** — son positividad/álgebra de la forma, independientes del trilema.

**[PUENTE] (estatus declarado):** la decisión de GAP-142.B convierte la contrapositiva $H^+\Rightarrow$ no-espectral (Doc 142 Teo. 8.1) en un hecho verificado, y redistribuye TODO el contenido de H⁺ a la espectralidad-positiva, que para datos con $\Gamma$ es RH. Nada de esto prueba o refuta RH; **poda una conjetura** (H⁺ como ruta más débil que RH) mostrando que era ilusoria.

**[GAP] heredado, no cerrado aquí:**
- **GAP-142.A:** el umbral arquimediano $T_\square\in[\tfrac1{300},T_1]$ — signo de $\mu_\varnothing(T)$ en la región intermedia (pregunta de forma, no de representación; ortogonal a GAP-142.B).

**Mensaje final (el veredicto, en tres líneas).**
1. **Veredicto del trilema:** **rama (2)**. El objeto semilocal $X_S^{\mathrm{ar}}$ **NO es espectral** (no espectral-positivo, Teorema 3.4), porque el símbolo del término arquimediano $\Omega$ tiene parte negativa ($\Omega(0)<0$) y por tanto no es la transformada de una medida espectral positiva (Teoremas 2.2 + 2.4).
2. **Qué le pasa a H⁺:** **colapsa hacia RH** (Teorema 4.1). H⁺ no es refutada, pero tampoco es más débil que RH: su única instancia no vacía con peso $\Gamma$ es $\zeta$ completa, donde espectral-positivo ⟺ RH. La clase semilocal-finita de H⁺ es **vacía** (Corolario 4.2); GAP-135.B estaba mal planteado. La ruta de interpolación semilocal queda **cerrada** (resultado negativo valioso: poda una estrategia).
3. **Tres resultados con etiqueta:** **[TEOREMA 2.4]** $\Omega$ no es transformada de medida positiva (decisión analítica, Bochner del símbolo); **[TEOREMA 3.4]** $X_S^{\mathrm{ar}}$ no es espectral-positivo (GAP-142.B decidido); **[TEOREMA 5.1]** el Teorema A de ventana corta ($Q_S\ge\tfrac3{10}\|f\|_w^2$, $2T\le\tfrac1{150}$, uniforme en $S$, incluye $\zeta$) sobrevive incondicionalmente al trilema.

---

## Referencias

**Internas (backward-only):** Doc 142 (`phase-46-audit-and-attacks/142-ataque-gap135B-semilocal.md`: objeto semilocal, $\Omega$, Teorema A, Teorema B, identidad de transmisión, trilema §8, GAP-142.B); Doc 135 (`phase-45-fredholm/135-teorema-dos-primos.md`: "espectral" = suma de cuadrados sobre progresiones; H⁺ en P48); Doc 131 (`phase-44-new-mathematics/131-algebra-correspondencias.md`: Def. 4.1 espectral, Teo. 4.4 órbitas, Teo. 6.3, Def. 6.1 Axioma H, Deseo 6.9 Conjetura H⁺); P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjecture 7.1 = H⁺).

**Literatura [DATO]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265. (Fórmula cuadrática; criterio H ⟺ RH; término arquimediano del factor $\Gamma_{\mathbb R}$.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233. (Normalización del funcional; papel del término arquimediano y del bloque polar; el funcional como forma de tipo positivo ⟺ RH.)
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (Términos locales de la fórmula explícita como distribuciones; el lugar arquimediano y su signo; los ceros triviales como polos de $\Gamma$.)
- S. Bochner, *Lectures on Fourier Integrals*, Annals of Mathematics Studies 42, Princeton 1959. (Teorema de Bochner: forma cuadrática diagonal en Fourier de tipo positivo ⟺ símbolo/medida espectral $\ge0$.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press 1975, Thm IX.9. (Caracterización de distribuciones de tipo positivo vía medidas positivas; versión usada en Teorema 2.2.)
- J.-F. Burnol, *The explicit formula and the conductor operator*, arXiv:math/9902080 (1999); y *Sur les formules explicites I: analyse invariante*, C. R. Acad. Sci. Paris 331 (2000), 423–428. (El término arquimediano $\operatorname{Re}\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi$ como operador conductor; su carácter no-positivo / parte logarítmica.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4ª ed., CUP 1927, §12.3. (Teorema de la digamma de Gauss; $\psi(\tfrac14)=-\gamma-\tfrac\pi2-3\log2$.)

*Fin del Documento 145.*
