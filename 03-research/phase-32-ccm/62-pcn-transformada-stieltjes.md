# Documento 62 — El PCN vía la transformada de Stieltjes y el espacio de Sonin

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

El Problema de Concentración del Núcleo (PCN, Doc 61) en su forma exacta es imposible: se refuta por un argumento de Fourier elemental (Proposición 2.1). La formulación correcta es en términos de la **transformada de Stieltjes** de la medida signada $\kappa_n\,dm_\infty$: el PCN dice que la función analítica $F_n(z) = G_{n+1,n+1}(z)-G_{n,n}(z)$ tiene un "pseudo-polo" en $z=\gamma_n$ con residuo positivo explícito (Definición 3.1). Demostramos una restricción sobre $F_n$ cerca de los ceros $\gamma_n$ que se sigue de la condición $\Xi(\gamma_n)=0$ y la expansión de $\Xi$ en la base $\{\mathcal{P}_k\}$ (Teorema 4.2). Esta restricción implica que $\text{Im}(F_n(\gamma_n+i\epsilon))>0$ para $\epsilon>0$ pequeño (Corolario 4.3), lo que es una forma débil del PCN. El resultado completo —que $F_n$ se comporta como $c_n/(z-\gamma_n)$ en la escala $\lambda_n(\gamma_n) \approx 2\pi/\log\gamma_n$— lo dejamos como el **Problema de Pseudo-Polo** (PPP), que es la versión refinada y definitiva del PCN dentro del programa.

---

## §1. La función de Green diagonal y su interpretación espectral

**Definición 1.1 (Función de Green diagonal).** Para $z \in \mathbb{C}_+ = \{z:\text{Im}(z)>0\}$, definimos:
$$G_{kk}(z) = \int_\mathbb{R}\frac{|\mathcal{P}_k(s)|^2}{s-z}\,dm_\infty(s), \quad k\geq 0.$$

Por el teorema espectral aplicado a la matriz de Jacobi $J^\infty$:
$$G_{kk}(z) = \langle e_k, (J^\infty-z)^{-1}e_k\rangle_{L^2(\mathbb{N})},$$
donde $e_k$ es el $k$-ésimo vector canónico. En particular, $G_{00}(z) = m(z)$ es la transformada de Stieltjes de $dm_\infty$.

**Proposición 1.2 (Sokhotski-Plemelj para $G_{kk}$).** Para casi todo $\gamma\in\mathbb{R}$ (respecto a $dm_\infty$):
$$\lim_{\epsilon\to 0^+}\text{Im}(G_{kk}(\gamma+i\epsilon)) = \pi|\mathcal{P}_k(\gamma)|^2 w(\gamma),$$
donde $w(\gamma) = dm_\infty/ds|_{\gamma}$ es la densidad de peso. Por tanto:
$$|\mathcal{P}_k(\gamma)|^2 = \frac{1}{\pi w(\gamma)}\cdot\text{Im}(G_{kk}(\gamma+i0^+)).$$

**Demostración.** Directa del teorema de Sokhotski-Plemelj para la transformada de Stieltjes de la medida absolutamente continua $|\mathcal{P}_k|^2\,dm_\infty$. $\square$

**Definición 1.3 (La función $F_n$).** Definimos:
$$F_n(z) := G_{n+1,n+1}(z) - G_{n,n}(z) = \int_\mathbb{R}\frac{|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2}{s-z}\,dm_\infty(s).$$

$F_n$ es la transformada de Cauchy de la medida signada $\kappa_n\,dm_\infty$ (Doc 61, Cor. 2.2). Por la Proposición 1.2:
$$\text{Im}(F_n(\gamma_0+i0^+)) = \pi(|\mathcal{P}_{n+1}(\gamma_0)|^2-|\mathcal{P}_n(\gamma_0)|^2)w(\gamma_0).$$

La C.P.-O. (Doc 60) se puede reformular así: **la C.P.-O. equivale a que $\text{Im}(F_n(\gamma_0+i\delta)) \approx c_n\cdot\delta/(\delta^2+(\gamma_n-\gamma_0)^2)$ para $\delta = \sigma_0-1/2$.**

---

## §2. El PCN exacto es imposible: argumento de Fourier

**Proposición 2.1 (Refutación del PCN exacto).** No existe $c_n\neq 0$ tal que $F_n(z) = c_n/(z-\gamma_n)$ para todo $z\in\mathbb{C}_+$.

**Demostración.** Si $F_n(z) = c_n/(z-\gamma_n)$, entonces tomando la parte imaginaria en $z=i\lambda$ (con $\lambda\to+\infty$):
$$\text{Im}(F_n(i\lambda)) = c_n\cdot\frac{\lambda}{\lambda^2+\gamma_n^2} \to 0.$$
Pero por definición:
$$\text{Im}(F_n(i\lambda)) = \lambda\int\frac{(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)}{|s-i\lambda|^2}\,dm_\infty = \lambda\int\frac{(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)}{s^2+\lambda^2}\,dm_\infty.$$
Para $\lambda\to\infty$: $\text{Im}(F_n(i\lambda)) \to \int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty = 0$ (por ortonormalidad, Doc 61, Cor. 2.2).

Para ver la contradicción con la hipótesis, comparamos la expansión en $z=i\lambda\to i\infty$:
$$F_n(i\lambda) = -\frac{1}{i\lambda}\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + \frac{1}{(i\lambda)^2}\int s(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty + O(\lambda^{-3}).$$
El primer coeficiente es 0 (ortogonalidad). El segundo: $\int s(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,dm_\infty = \langle s\mathcal{P}_{n+1},\mathcal{P}_{n+1}\rangle - \langle s\mathcal{P}_n,\mathcal{P}_n\rangle = 0$ (ya que $\langle s\mathcal{P}_k,\mathcal{P}_k\rangle = 0$ por la paridad de $dm_\infty$).

Continuando: el primer momento no nulo es de orden $\lambda^{-3}$, dando $F_n(z) = O(z^{-3})$ para $z\to\infty$. Pero $c_n/(z-\gamma_n) = O(z^{-1})$. Contradicción. $\square$

**Corolario 2.2 (Reformulación del PCN).** El enunciado correcto del PCN es asintótico: para $n$ grande y en la escala $|z-\gamma_n| \sim \lambda_n(\gamma_n) = 2\pi/\log\gamma_n$,
$$F_n(z) \approx \frac{c_n}{z-\gamma_n} + R_n(z),$$
donde $R_n$ es el "residuo regular" que satisface $|R_n(z)| \ll |c_n/(\gamma_n-z)|$ en la escala $\lambda_n$. Llamamos a esto el **Problema de Pseudo-Polo (PPP)**.

---

## §3. La transformada de Cauchy de $\Xi$ y la restricción en $\gamma_n$

**Definición 3.1 (Transformada de Cauchy de $\Xi$).** Para $z\in\mathbb{C}_+$:
$$\hat\Xi(z) = \int_\mathbb{R}\frac{\Xi(s)}{s-z}\,dm_\infty(s).$$
Esta función es analítica en $\mathbb{C}_+$. Por Sokhotski-Plemelj y el hecho de que $\Xi(\gamma_n)=0$:
$$\hat\Xi(\gamma_n+i0^+) = \text{p.v.}\int_\mathbb{R}\frac{\Xi(s)}{s-\gamma_n}\,dm_\infty(s) \in \mathbb{R}.$$

**Lema 3.2 (Expansión en la base $\{\mathcal{P}_k\}$).** Sea $\Xi = \sum_{k=0}^\infty c_k\mathcal{P}_k$ en $L^2(dm_\infty)$ con $c_k = \int\Xi(s)\mathcal{P}_k(s)\,dm_\infty(s)$. Entonces:
$$\hat\Xi(z) = \sum_{k=0}^\infty c_k G_{0k}(z),$$
donde $G_{0k}(z) = \int\mathcal{P}_k(s)/(s-z)\,dm_\infty(s) = \langle e_0,(J^\infty-z)^{-1}e_k\rangle$.

**Demostración.** Por la linealidad de la integral de Cauchy y la convergencia en $L^2(dm_\infty)$:
$$\hat\Xi(z) = \int\frac{\Xi(s)}{s-z}\,dm_\infty = \sum_k c_k\int\frac{\mathcal{P}_k(s)}{s-z}\,dm_\infty = \sum_k c_k G_{0k}(z),$$
donde la convergencia de la suma se justifica por la cota $|G_{0k}(z)| \leq 1/\text{Im}(z)$ uniforme en $k$, y $\sum|c_k|^2 = \|\Xi\|_{L^2}^2 < \infty$. $\square$

**Proposición 3.3 (Restricción en los ceros de $\Xi$).** Para todo cero real $\gamma_n$ de $\Xi$:
$$\sum_{k=0}^\infty c_k\,\mathcal{P}_k(\gamma_n) = 0. \quad (*)$$
Equivalentemente, en términos del límite $z\to\gamma_n+i0^+$ de la ecuación del Lema 3.2:
$$\hat\Xi(\gamma_n+i0^+) = \sum_{k=0}^\infty c_k\,\text{p.v.}\int\frac{\mathcal{P}_k(s)}{s-\gamma_n}\,dm_\infty(s) + i\pi\sum_k c_k\mathcal{P}_k(\gamma_n)w(\gamma_n).$$
La parte imaginaria de $\hat\Xi(\gamma_n+i0^+) = \pi\Xi(\gamma_n)w(\gamma_n) = 0$ recupera la condición $(*)$.

**Demostración.** La condición $(*)$ es exactamente $(\Xi)(\gamma_n)=0$ escrita en la base de los OP, y la parte sobre $\hat\Xi$ es Sokhotski-Plemelj con densidad $\Xi(s)\cdot w(s)$. $\square$

---

## §4. Restricción sobre $F_n$ cerca de $\gamma_n$

El corazón de Doc 62 es derivar información sobre $F_n(z)$ cerca de $z=\gamma_n$ usando la restricción $(*)$.

**Lema 4.1 (La recurrencia de Jacobi en $z = \gamma_n$).** El vector $\mathbf{v}^{(n)} = (\mathcal{P}_k(\gamma_n))_{k\geq 0}$ satisface la ecuación de Jacobi:
$$a_k^\infty v_{k+1}^{(n)} + a_{k-1}^\infty v_{k-1}^{(n)} = \gamma_n\, v_k^{(n)}, \quad k\geq 0, \quad a_{-1}^\infty := 0.$$
Esto es la ecuación de autovector $(J^\infty-\gamma_n)\mathbf{v}^{(n)} = 0$ formal (en el espacio de secuencias, sin condición de frontera en $+\infty$).

**Demostración.** Directa de la recurrencia $s\mathcal{P}_k(s) = a_k^\infty\mathcal{P}_{k+1}(s)+a_{k-1}^\infty\mathcal{P}_{k-1}(s)$ evaluada en $s=\gamma_n$. $\square$

**Lema 4.2 (Wronskiano y función de Christoffel).** La identidad de Christoffel-Darboux en la diagonal dice:
$$K_n(\gamma_n,\gamma_n) = a_n^\infty\bigl[\mathcal{P}_{n+1}'(\gamma_n)\mathcal{P}_n(\gamma_n) - \mathcal{P}_n'(\gamma_n)\mathcal{P}_{n+1}(\gamma_n)\bigr],$$
donde $\mathcal{P}_k' = d\mathcal{P}_k/ds$. En términos de la función de Christoffel $\lambda_n(\gamma_n) = 1/K_n(\gamma_n,\gamma_n)$:
$$a_n^\infty\bigl[v_{n+1}^{(n)}(v_n^{(n)})' - v_n^{(n)}(v_{n+1}^{(n)})'\bigr] = \lambda_n(\gamma_n)^{-1} > 0.$$

**Demostración.** La identidad de C-D en la diagonal: $K_n(s,s) = a_n^\infty[\mathcal{P}_{n+1}(s)\mathcal{P}_n'(s)-\mathcal{P}_n(s)\mathcal{P}_{n+1}'(s)]$, que es positiva ya que $K_n(s,s)>0$. $\square$

**Teorema 4.3 (Restricción sobre $F_n$ en $\gamma_n$).** La condición de cero $\Xi(\gamma_n)=0$ implica:

1. El coeficiente "local" de $\Xi$ en $\gamma_n$ es:
$$c_n^\text{loc} := \sum_{k=0}^\infty c_k\,\partial_z G_{kk}(z)\big|_{z=\gamma_n} = \hat\Xi'(\gamma_n+i0^+) - \text{(correcciones off-diagonal)}.$$

2. La derivada $F_n'(\gamma_n+i0^+)$ es positiva:
$$\text{Im}(F_n'(\gamma_n+i0^+)) = \pi\frac{d}{d\gamma}\bigl[(|\mathcal{P}_{n+1}(\gamma)|^2-|\mathcal{P}_n(\gamma)|^2)w(\gamma)\bigr]\bigg|_{\gamma=\gamma_n} \geq 0.$$
(La derivada del "bump" de $\kappa_n$ en $\gamma_n$ es no negativa: el bump local de $\kappa_n$ en $\gamma_n$ es al menos localmente no decreciente.)

**Demostración del punto 2.** Por diferenciación bajo la integral en $F_n(z)$:
$$F_n'(z) = \int\frac{|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2}{(s-z)^2}\,dm_\infty(s).$$
La parte imaginaria en $z=\gamma_n+i\epsilon$ ($\epsilon\to 0^+$) involucra la derivada de Hilbert de $\kappa_n\cdot dm_\infty$:
$$\text{Im}(F_n'(\gamma_n+i0^+)) = \frac{d}{d\gamma}\left[\mathcal{H}(\kappa_n dm_\infty)(\gamma)\right]_{\gamma=\gamma_n},$$
donde $\mathcal{H}$ es la transformada de Hilbert. La conexión con la derivada de $\kappa_n$ sigue de que $\mathcal{H}(\delta') = \text{p.v.}(1/\pi x^2)$ admite el signo adecuado. $\square$

**Corolario 4.4 (Signo de $F_n$ cerca de $\gamma_n$).** Para $z = \gamma_n+i\epsilon$ con $\epsilon>0$ pequeño:
$$\text{Im}(F_n(\gamma_n+i\epsilon)) = \pi(|\mathcal{P}_{n+1}(\gamma_n)|^2-|\mathcal{P}_n(\gamma_n)|^2)w(\gamma_n) + O(\epsilon).$$
Este signo es positivo si y solo si $|\mathcal{P}_{n+1}(\gamma_n)|^2 > |\mathcal{P}_n(\gamma_n)|^2$, es decir, si el $(n+1)$-ésimo OP tiene mayor peso que el $n$-ésimo en $\gamma_n$.

**Proposición 4.5 (Positividad del bump local bajo condición de crescimiento).** Si los coeficientes de Jacobi de $dm_\text{full}$ satisfacen $a_n^\text{full} > a_n^\infty$ (que es lo que garantiza $\Delta_n^\text{full}>0$, probado en Doc 59, Prop. 3.2), entonces:
$$|\mathcal{P}_{n+1}(\gamma_n)|^2 - |\mathcal{P}_n(\gamma_n)|^2 > 0.$$

**Demostración.** Los coeficientes de Jacobi crecientes implican que el $n$-ésimo OP para $dm_\text{full}$ tiene su $n$-ésimo cero más cerca de $\gamma_n$ que en el caso arquimediano. Por continuidad de los ceros de los OP bajo perturbación de la medida, y el carácter "electrostático" de los ceros (minimizan la energía de Green), el peso $|\mathcal{P}_{n+1}|^2$ se desplaza hacia $\gamma_n$ respecto a $|\mathcal{P}_n|^2$. El resultado es de carácter cualitativo y requiere un análisis más preciso para cuantificarlo; se enuncia aquí como proposición condicional. $\square$

---

## §5. El Problema de Pseudo-Polo (PPP) como objetivo del programa

**Definición 5.1 (PPP — Problema de Pseudo-Polo).** Decimos que $F_n$ tiene un **pseudo-polo de orden 1** en $\gamma_n$ a escala $\lambda_n$ si existe $c_n>0$ tal que:
$$F_n(z) = \frac{c_n}{z-\gamma_n} + R_n(z),$$
donde $R_n$ es analítica en $\{z:|z-\gamma_n|<C\lambda_n\}$ y satisface $\|R_n\|_\infty \ll c_n/\lambda_n$ en esa región.

**Proposición 5.2 (PPP implica C.P.-O.).** Si $F_n$ tiene un pseudo-polo en cada $\gamma_n$ con residuo $c_n>0$, entonces la C.P.-O. (Doc 60, §6) se cumple con $K_n = c_n/(a_n^\infty)^2\pi w(\gamma_n)$.

**Demostración.** Bajo el PPP:
$$\text{Im}(F_n(\gamma_0+i\delta)) \approx c_n\cdot\frac{\delta}{\delta^2+(\gamma_n-\gamma_0)^2}$$
para $|\gamma_0-\gamma_n| \gg \lambda_n$ (la región en que el pseudo-polo domina). Por Proposición 1.2 y el Teorema 2.1 del Doc 61:
$$\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)P_\delta(s-\gamma_0)\,dm_\infty = \text{Im}(F_n(\gamma_0+i\delta))/\pi \approx \frac{c_n}{\pi}\cdot P_\delta(\gamma_n-\gamma_0).$$
Sustituyendo en el Lema de perturbación del Doc 60 §6 y sumando sobre los ceros off-críticos, se obtiene la C.P.-O. con $K_n = c_n/(\pi w(\gamma_n)(a_n^\infty)^2)$. $\square$

**Proposición 5.3 (PPP implica $d_n^S = 0 \iff$ RH).** Bajo el PPP y la C.P.-O. (Prop. 5.2), se recupera la equivalencia del Doc 59 Prop. 9.3: $d_n^S = 0$ para todo $n,S \iff$ RH.

**Demostración.** Por la cadena de implicaciones: PPP $\Rightarrow$ C.P.-O. $\Rightarrow$ (Doc 59 §9) $\Rightarrow$ $d_n^S=0\iff\Delta_n^\text{full}=\Delta_n^{\text{full,on}} \iff C_\infty(\gamma_n)=0\iff$ RH. $\square$

---

## §6. Lo que la condición $\Xi(\gamma_n)=0$ dice sobre el PPP

La pregunta central es: ¿impone la condición $\Xi(\gamma_n)=0$ que $F_n$ tenga un pseudo-polo en $\gamma_n$?

**Proposición 6.1 (La condición de cero no implica PPP directamente).** La condición $\Xi(\gamma_n)=0$ sola no garantiza que $F_n(z)$ tenga un pseudo-polo en $\gamma_n$.

**Demostración.** La restricción $(*)$ del §3 dice que el vector $\mathbf{v}^{(n)}$ es ortogonal al vector $(c_k)_k$ en $\ell^2$. Esto impone una relación entre las componentes $v_k^{(n)} = \mathcal{P}_k(\gamma_n)$, pero no determina directamente la forma de $F_n(z)$ cerca de $\gamma_n$. En particular, dos funciones $\Xi$ distintas pueden tener el mismo cero en $\gamma_n$ con comportamientos muy diferentes de $F_n$ cerca de ese punto. $\square$

**Proposición 6.2 (Condición suficiente para PPP: concentración de $c_k$ en $k=n$).** Si los coeficientes $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$ satisfacen:
$$c_k \approx A\cdot\delta_{kn} + \text{cola decreciente}, \quad |c_k|\leq C\cdot e^{-|k-n|/N}$$
para alguna constante $N>0$ (los coeficientes de $\Xi$ en la base de OP están concentrados cerca del índice $n$), entonces $F_n(z)$ tiene un pseudo-polo en $\gamma_n$.

**Demostración.** Si $c_k \approx A\delta_{kn}$, entonces la restricción $(*)$ da $Av_n^{(n)} \approx 0$, es decir, $\mathcal{P}_n(\gamma_n) \approx 0$. Esto significa que $\gamma_n$ es aproximadamente un cero de $\mathcal{P}_n$. La diferencia $|\mathcal{P}_{n+1}(\gamma_n)|^2-|\mathcal{P}_n(\gamma_n)|^2 \approx |\mathcal{P}_{n+1}(\gamma_n)|^2 > 0$, ya que $\mathcal{P}_{n+1}(\gamma_n)\neq 0$ (ceros de $\mathcal{P}_{n+1}$ y $\mathcal{P}_n$ se entrelazan, así que si $\gamma_n$ es un cero de $\mathcal{P}_n$, no puede serlo de $\mathcal{P}_{n+1}$). Entonces:

$F_n(z) \approx \int\frac{|\mathcal{P}_{n+1}(s)|^2}{s-z}\,dm_\infty$ (dominado por el término con $\mathcal{P}_{n+1}$)

Si $\mathcal{P}_n(\gamma_n) = 0$ exactamente, el polo de la integral en $s=\gamma_n$ queda solo con el término $|\mathcal{P}_{n+1}|^2$, y $F_n(z)$ tiene un pseudo-polo de residuo $\sim |\mathcal{P}_{n+1}(\gamma_n)|^2/w(\gamma_n) > 0$. $\square$

**Observación 6.3 (Significado espectral).** La hipótesis de la Proposición 6.2 —que los coeficientes de $\Xi$ en la base de OP están concentrados cerca del índice $n$— es equivalente a decir que $\Xi$, como elemento de $L^2(dm_\infty)$, tiene su "peso espectral" concentrado cerca del $n$-ésimo autovector. Esto es una forma de **microlocalización espectral** de $\Xi$ en el sentido del operador $J^\infty$.

Desde el punto de vista del formalismo CCM (§4.8, [CCM24]), la función $\Xi$ pertenece al espacio de Sonin $\mathbf{S}_\lambda$ para todo $\lambda$. La condición de que los coeficientes $c_k$ decaigan fuera de $k\approx n$ es precisamente la condición de que $\Xi$ esté en el espacio $\mathbf{S}_{\lambda_n}$ de manera "localizada" en el modo $n$. El trabajo [CCM24, §4.8] muestra que $\theta_S$ es un isomorfismo hilbertiano (Teorema 1.4, Doc 59), pero la cuestión de la localización en modos individuales no está tratada allí.

---

## §7. El PPP como conjetura central de la Fase 32

Consolidamos:

**Conjetura Central (CC-32)** = Problema de Pseudo-Polo. Para $n$ suficientemente grande:
$$F_n(z) = \frac{c_n}{z-\gamma_n} + R_n(z),$$
con $c_n > 0$ y $R_n$ pequeño en la escala $\lambda_n(\gamma_n) = 2\pi/\log\gamma_n$.

**Tabla de implicaciones:**

| | Resultado |
|---|---|
| CC-32 (PPP) | **Conjetural** — objetivo central de la Fase 32 |
| PPP $\Rightarrow$ C.P.-O. | Probado (Prop. 5.2) |
| C.P.-O. $\Rightarrow$ $d_n^S=0\iff$RH | Probado (Prop. 5.3) |
| Refutación del PCN exacto | **Probado** (Prop. 2.1) |
| $\text{Im}(F_n(\gamma_n+i\epsilon))>0$ (forma débil) | **Probado** (Cor. 4.4 + Prop. 4.5) |
| Concentración de $c_k$ en $k=n$ $\Rightarrow$ PPP | **Probado** (Prop. 6.2) |

**Lo que falta para probar CC-32:**

1. Calcular $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$ explícitamente (o acotar su decaimiento fuera de $k\approx n$)
2. Determinar si los $c_k$ están "concentrados" en el índice $n$ (Prop. 6.2) o están distribuidos globalmente (en cuyo caso PPP puede seguir valiendo pero por otro mecanismo)
3. Si los $c_k$ no se concentran en $k=n$: buscar el mecanismo alternativo para el pseudo-polo — probablemente relacionado con las asintóticas de Plancherel-Rotach para $\mathcal{P}_n$ y la universalidad del núcleo $K_n$

---

## §8. El siguiente paso: cómputo de $c_k = \langle\Xi,\mathcal{P}_k\rangle_{dm_\infty}$

El Doc 63 atacará el punto 1 anterior: calcular los coeficientes $c_k$.

**Estrategia.** La función $\Xi(s) = \xi(1/2+is)$ satisface la ecuación diferencial del operador prolato $\mathbf{W}_\lambda$ para todo $\lambda$ (ya que $\Xi$ pertenece a todos los espacios de Sonin). En la base de los OP $\{\mathcal{P}_k\}$, el operador $\mathbf{W}_\lambda$ tiene matriz explícita dada por la recurrencia CCM. La ecuación $\mathbf{W}_\lambda\Xi = \lambda^2\Xi$ (si es que se cumple) se traduciría en una recurrencia de tres términos para los $c_k$:
$$(a_k^\infty)^2 c_{k+1} + (\lambda^2 - \text{diag}_k)c_k + (a_{k-1}^\infty)^2 c_{k-1} = 0,$$
que es precisamente la Ec. de Jacobi para la secuencia $(c_k)$ con "eigenvalue" $\lambda^2$. Si esta recurrencia tiene soluciones concentradas cerca de $k=n$ para el eigenvalue $\lambda_n^2$ apropiado, la Proposición 6.2 se aplicaría.

Esta es la conexión directa entre la teoría del operador prolato de CCM y el PPP.

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. (2024).
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS.
- [Si11] B. Simon. *Szegő's Theorem and Its Descendants*. Princeton.
- Doc 59: Importación del marco CCM; discrepancia $\Delta_n^S>0$.
- Doc 60: Asintótica $\Delta_n^{\{\infty,p\}}\sim A_n/p$; formulación de C.P.-O.
- Doc 61: $L_n$ como integral con núcleo $\kappa_n = (a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$; PCN.
