# Doc 98 — Test de juguete B+D: un cuádruplo off-crítico

**Programa:** Hipótesis de Riemann — Fase 35, Cinco Frentes
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Docs 82, 83, 86, 89, 91, 93, 95, 96, 97; Papers P35, P39
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es o bien una demostración completa dentro del modelo de juguete, o bien un GAP declarado con precisión.

---

## Resumen ejecutivo

Este documento somete la conjetura de conexión B+D — "la parte irreducible $d\nu^*$ del problema variacional (Dirección D) corresponde a la localización del índice negativo en $\mathcal{K}_{\mathrm{off}}$ (Dirección B)" — al test más simple posible: $\neg$RH con **exactamente un cuádruplo** de ceros off-críticos $\{1/2\pm\delta\pm i\gamma_0\}$, $\delta\in(0,1/2)$, $\gamma_0>0$, y todos los demás ceros sobre la línea crítica.

**Resultados del test:**

1. (§2) El factor $R_{\gamma_0,\delta}$ y la medida $d\nu$ se computan en **forma cerrada**: $R-1$ es un polinomio exacto de grado 4 en $\delta^2$, sin resto infinito. A orden líder, $d\nu = 2\delta^2 K_0(s)\,f_0^{on}(s)\,dm_\infty + O(\delta^4)$ con $K_0(s) = (s-\gamma_0)^{-2}+(s+\gamma_0)^{-2}$.

2. (§3) El test detecta **dos errores internos en los Docs 93/95**: (a) la "variación transversal" $\epsilon=i\delta$ del Doc 93 §2.3 es en realidad tangencial, y con la transversal correcta la segunda variación transversal en $f_0^{on}$ es **negativa** ($\psi''(0) = -8\mathcal{Q}_\lambda^{(0)} < 0$), no positiva; (b) el kernel de Euler–Lagrange $2s/(s^2-\gamma_j^2)$ de los Docs 95/97 es impar y hace las ecuaciones **vacuas** por paridad; el kernel correcto (compatible con la ecuación funcional) es $-4\gamma_j/(s^2-\gamma_j^2)$, par.

3. (§4–5) **Teorema de absorción** (resultado central): la componente de $d\nu$ de orden $\delta^2$, localizada en las frecuencias $\pm\gamma_0$ del cuádruplo, es **asintóticamente absorbible** dentro de $\overline{\mathcal{M}}$ mediante reorganización deslocalizada de los ceros on-line lejanos (más adición de pares en el infinito). En consecuencia $\tilde\delta_\lambda(\delta) = o(\delta^2)$ y la masa de $d\nu^*$ es $o(\delta^2)$: **no** es $O(\delta^2)$ con coeficiente positivo; si es exactamente $O(\delta^4)$ queda como gap.

4. (§6) Lado B: el cuádruplo genera $\mathcal{K}_{\mathrm{off}}$ de dimensión 4 (autovalores $\pm\delta\pm i\gamma_0$ de $H_C$), con forma de Gram igual a dos planos hiperbólicos: $\kappa = 2$, **independiente de $\delta$** y discontinuo en $\delta=0$. Consistente con P35 ($\kappa = 2m$, $m=1$).

5. (§7) Índice de Maslov del cruce $\delta:0\to\delta_0$: flujo espectral $= -2$, $|\mu| = 2 = \kappa$ (con gaps técnicos de regularidad declarados).

6. (§8) **Pregunta central (vi): la correspondencia fuerte $d\nu^* \leftrightarrow \mathcal{K}_{\mathrm{off}}$ NO se sostiene.** Las magnitudes no coinciden en ningún orden de $\delta$ (entero $\kappa=2$ constante vs. masa $o(\delta^2)$ evanescente); la localización no coincide ($\mathcal{K}_{\mathrm{off}}$ rígidamente anclado al cuádruplo, $d\nu^*$ deslocalizado por el mecanismo de absorción); no hay mapa natural. Lo único que coincide es la anulación simultánea, que es tautológica vía RH. **La conexión B+D, en su forma fuerte, está muerta.** Lo que sobrevive es una correspondencia distinta y más débil: $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$ (el residual de referencia fija en $f_0^{on}$, no el optimizado), ambos de escala $\delta^2$ y ambos localizados en el cuádruplo.

**VEREDICTO: RUTA CERRADA** para la correspondencia fuerte $d\nu^*\leftrightarrow\mathcal{K}_{\mathrm{off}}$ (§10).

---

## §1. El modelo de juguete: definiciones exactas

### 1.1. Hipótesis del modelo

**Hipótesis (T1) — Configuración de ceros.** Los ceros no triviales de $\xi$ son:
- los pares simples $\{1/2 \pm i\gamma_j\}_{j\geq 1}$, con $0 < \gamma_1 < \gamma_2 < \cdots$, $\gamma_j \to \infty$;
- exactamente un cuádruplo off-crítico
$$Z_\delta = \{\,1/2+\delta+i\gamma_0,\; 1/2+\delta-i\gamma_0,\; 1/2-\delta+i\gamma_0,\; 1/2-\delta-i\gamma_0\,\},$$
con $\delta \in (0,1/2)$, $\gamma_0 > 0$, $\gamma_0 \notin \{\gamma_j\}_{j\geq 1}$.

**Hipótesis (T2) — Régimen perturbativo.** Todas las expansiones se hacen en potencias de $\delta^2$ con $\gamma_0$ fijo. Como se verá (Proposición 2.2), en este modelo las expansiones relevantes son polinomios exactos en $\delta^2$: no hay problema de resto.

**Hipótesis (T3) — Estructura CCM heredada (citada, no demostrada aquí).**
- (W-pos) $W_\lambda \geq 0$ (kernel de Abel CCM, Doc 82).
- (W-pol) $W_\lambda$ tiene crecimiento a lo sumo polinomial en $|s|$ (Doc 82 §2, citado vía Doc 95, Lema 2.2).
- (W-par) $W_\lambda(s) = W_\lambda(-s)$. Esta paridad está implícita en el marco simétrico del Doc 83 §2.2 (ambas medidas $dm_{\mathrm{full}}$, $dm_{\mathrm{full,on}}$ son pares y los momentos impares se anulan). Se declara como hipótesis estructural.

**Hipótesis (T4) — Separación espectral (solo para §7).** El cluster $\{\pm i\gamma_0\}$ está a distancia positiva del resto del espectro de $H_C$, uniformemente en $\delta \in [0,\delta_0]$.

### 1.2. $\zeta_{\mathrm{on}}$ en el modelo de juguete

Por la Definición del Doc 83 §1.1, $\xi_{\mathrm{on}}$ se obtiene proyectando cada cero a la línea crítica conservando la parte imaginaria. El cuádruplo $Z_\delta$ se proyecta sobre $\{1/2+i\gamma_0,\,1/2-i\gamma_0\}$, **cada uno con multiplicidad 2** (Doc 83, §1.2, cálculo del cuádruplo). Por tanto, en el modelo de juguete:

- $\xi_{\mathrm{on}}$ tiene ceros simples en $1/2\pm i\gamma_j$ ($j\geq 1$) y ceros **dobles** en $1/2\pm i\gamma_0$.
- Sobre la línea, $f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2$ se anula a orden 2 en $s=\pm\gamma_j$ y a **orden 4** en $s = \pm\gamma_0$. Escribimos
$$f_0^{on}(s) = (s^2-\gamma_0^2)^4\, G(s), \qquad G \text{ continua}, \; G(\pm\gamma_0) > 0. \tag{1.1}$$

**Observación 1.1 (rigidez de la multiplicidad).** La simetría real de $\eta\in\mathcal{E}$ (coeficientes reales tras rotación) junto con la ecuación funcional fuerza que los ceros off-críticos aparezcan en cuádruplos. Consecuencia: un par simple on-line $\{1/2\pm i\gamma_j\}$ **no puede** deformarse fuera de la línea dentro de la clase de funciones con simetrías de $\xi$; solo los puntos on-line de multiplicidad $\geq 2$ admiten desdoblamiento transversal. En el modelo de juguete, $f_0^{on}$ admite exactamente **una** dirección transversal genuina: el desdoblamiento del doble cero en $\pm\gamma_0$. Esto se usará en §3.3.

---

## §2. Objeto (i): el factor $R$ y la medida $d\nu$ en forma cerrada

### 2.1. Forma cerrada de $R$

**Proposición 2.1 (Factor del cuádruplo; Doc 83, Proposición 1.1 especializada).** Para todo $s \in \mathbb{R}$ con $s \neq \pm\gamma_0$:
$$R_{\gamma_0,\delta}(s) := \frac{f_0(s)}{f_0^{on}(s)} = \left(1+\frac{\delta^2}{(s-\gamma_0)^2}\right)^{2}\left(1+\frac{\delta^2}{(s+\gamma_0)^2}\right)^{2} \;\geq\; 1. \tag{2.1}$$

*Demostración.* Es el cálculo exacto del Doc 83, §1.2 (factor $C_j(u)$ del cuádruplo), con un único cuádruplo: el producto de la Proposición 1.1 del Doc 83 tiene un solo término. La desigualdad $\geq 1$ es inmediata. $\square$

En consecuencia, con $d\nu := dm_{\mathrm{full}} - dm_{\mathrm{full,on}} = (f_0 - f_0^{on})\,dm_\infty$ (Doc 83, Corolario 1.3; Doc 89):
$$d\nu(s) = \bigl(R_{\gamma_0,\delta}(s) - 1\bigr)\, f_0^{on}(s)\, dm_\infty(s) \;\geq\; 0 \quad \text{(incondicional)}. \tag{2.2}$$

### 2.2. Expansión exacta en $\delta^2$ (sin resto)

**Proposición 2.2 (Expansión polinomial exacta).** Sea $a = \delta^2/(s-\gamma_0)^2$, $b = \delta^2/(s+\gamma_0)^2$. Entonces
$$R_{\gamma_0,\delta}(s) - 1 = 2(a+b) + (a^2 + b^2 + 4ab) + 2ab(a+b) + a^2b^2, \tag{2.3}$$
es decir, $R-1$ es un **polinomio exacto de grado 4 en $\delta^2$** con coeficientes racionales explícitos en $s$:
$$R - 1 = 2\delta^2 K_0(s) + \delta^4 Q_2(s) + 2\delta^6 Q_3(s) + \delta^8 Q_4(s),$$
donde
$$K_0(s) = \frac{1}{(s-\gamma_0)^2}+\frac{1}{(s+\gamma_0)^2} = \frac{2(s^2+\gamma_0^2)}{(s^2-\gamma_0^2)^2} \;>\;0,$$
$$Q_2 = \frac{1}{(s-\gamma_0)^4}+\frac{1}{(s+\gamma_0)^4}+\frac{4}{(s^2-\gamma_0^2)^2},\quad Q_3 = \frac{K_0(s)}{(s^2-\gamma_0^2)^2},\quad Q_4 = \frac{1}{(s^2-\gamma_0^2)^4}.$$

*Demostración.* $(1+a)^2(1+b)^2 = (1+2a+a^2)(1+2b+b^2)$; expansión directa y agrupación por grado total en $(a,b)$, que coincide con el grado en $\delta^2$. $\square$

**Proposición 2.3 (Integrabilidad y forma cerrada de $d\nu$).** Cada término de (2.3) multiplicado por $f_0^{on}$ es continuo en $s=\pm\gamma_0$ y pertenece a $H_\lambda = L^2(W_\lambda\,dm_\infty)$. En particular:
$$d\nu = \Bigl[\,2\delta^2\, K_0(s)\,f_0^{on}(s) \;+\; \delta^4 E_\delta(s)\,f_0^{on}(s)\Bigr]\, dm_\infty(s), \qquad E_\delta := Q_2 + 2\delta^2 Q_3 + \delta^4 Q_4, \tag{2.4}$$
con $\|E_\delta f_0^{on}\|_{H_\lambda} \leq C(\gamma_0,\lambda)$ uniformemente para $\delta\in(0,1/2)$. El "resto" $\delta^4 E_\delta f_0^{on}$ es exacto, no asintótico.

*Demostración.* Por (1.1), $f_0^{on} = (s^2-\gamma_0^2)^4 G$ con $G$ continua y positiva en $\pm\gamma_0$. El término más singular de (2.3) es $Q_4 = (s^2-\gamma_0^2)^{-4}$, y $Q_4 f_0^{on} = G$ es continuo. Análogamente $K_0 f_0^{on} = 2(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2 G$ se anula a orden 2 en $\pm\gamma_0$. La pertenencia a $H_\lambda$ sigue de (W-pol), del crecimiento polinomial de $f_0(s) \geq f_0^{on}(s)$ sobre la línea (cota de convexidad $|\zeta(1/2+it)| \ll (1+|t|)^{1/4}$, Titchmarsh [T86], Cap. V) y del decaimiento $dm_\infty \asymp |s|^{-1/2}e^{-\pi|s|/2}ds$ (Doc 95, Lema 2.2). $\square$

**Esto responde el objeto (i):** $R$ explícito (2.1), $d\nu \geq 0$ explícita (2.2), expansión a orden $\delta^2$ con resto **exactamente controlado** (2.4). La densidad líder de $d\nu$ es
$$\nu_2(s) := 2\,K_0(s)\,f_0^{on}(s) = 4(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2 G(s), \tag{2.5}$$
una función **suave, par, positiva fuera de $\pm\gamma_0$**, con "resonancia" (concentración del kernel $K_0$) en las frecuencias $\pm\gamma_0$ del cuádruplo.

### 2.3. Masa de $d\nu$ a orden líder

**Corolario 2.4 (Masa exacta a orden líder).** La norma $H_\lambda$ de la densidad de $d\nu$ satisface
$$\bigl\|\,(R_{\gamma_0,\delta}-1)\,f_0^{on}\,\bigr\|_{H_\lambda} = 2\delta^2\,\bigl\|K_0\,f_0^{on}\bigr\|_{H_\lambda} + O(\delta^4), \qquad \bigl\|K_0f_0^{on}\bigr\|_{H_\lambda}^2 = \int_\mathbb{R} W_\lambda\,\bigl(2(s^2+\gamma_0^2)(s^2-\gamma_0^2)^2G(s)\bigr)^2 dm_\infty \in (0,\infty),$$
con la constante dependiente solo de $(\gamma_0,\lambda)$ y de los ceros on-line. Análogamente, $T_\lambda = \int W_\lambda\,d\nu = 2\delta^2\int W_\lambda K_0 f_0^{on}\,dm_\infty + O(\delta^4)$, consistente con la cota inferior $T_\lambda \geq 2\delta^2 K_\lambda(\gamma_0)$ del Doc 86, §6 (el kernel $K_\lambda(\gamma_0)$ del Doc 86 es la integral con el término $(s-\gamma_0)^{-2}$ de $K_0$). Ambos objetos de referencia fija son $\asymp \delta^2$ con constantes positivas explícitas. $\square$

---

## §3. Geometría local de $\mathcal{M}$ en $f_0^{on}$: dos correcciones

Antes de plantear Euler–Lagrange, el modelo de juguete obliga a corregir dos puntos de los Docs 93/95/97. Ambas correcciones se demuestran completamente.

### 3.1. Corrección A: paridad del kernel de Euler–Lagrange

**Lema 3.1 (Las ecuaciones EL de Docs 95/97, tal como están escritas, son vacuas).** Bajo (W-par), para cualquier $g \in \mathcal{M}$ par y cualquier $\gamma > 0$:
$$\int_\mathbb{R} W_\lambda(s)\,\bigl(f_0(s)-g(s)\bigr)\,g(s)\,\frac{2s}{s^2-\gamma^2}\,dm_\infty(s) = 0 \quad \text{idénticamente}.$$

*Demostración.* $f_0$, $f_0^{on}$ y todo $g=|\eta|^2\in\mathcal{M}$ son pares en $s$ (ecuación funcional + reflexión de Schwarz: $|\zeta(1/2-is)| = |\zeta(1/2+is)|$ para $s$ real; ídem para $\eta\in\mathcal{E}$ con ceros simétricos $\pm\gamma_j$). $W_\lambda$ y $dm_\infty$ son pares ((W-par); $|\Gamma(1/4+is/2)|^2$ es par). El kernel $2s/(s^2-\gamma^2)$ es **impar**. La integral de (par)·(impar) respecto a una medida par es cero (valor principal en $\pm\gamma$, donde además el integrando es regular porque $g$ se anula a orden $\geq 2$ si $\gamma$ es cero de $\eta$). $\square$

**Consecuencia 3.2 (corrección al Doc 95, Lema 4.6, y al Doc 97, ec. (EL)).** La afirmación "$f_0^{on}$ no satisface las ecuaciones de Euler–Lagrange bajo $\neg$RH" no puede sostenerse con el kernel impar $2s/(s^2-\gamma_j^2)$: con ese kernel **todo** elemento par las satisface trivialmente. El origen del error es la variación subyacente: el kernel $1/(s-\gamma_j)+1/(s+\gamma_j)$ corresponde a trasladar **ambos** ceros $\pm\gamma_j$ en la misma dirección ($\gamma_j\mapsto\gamma_j+\epsilon$, $-\gamma_j\mapsto-\gamma_j+\epsilon$), lo que rompe la simetría $s\mapsto 1-s$ y sale de $\mathcal{E}$. La variación admisible (que preserva la ecuación funcional) mueve el par simétricamente: $\pm\gamma_j \mapsto \pm(\gamma_j+\epsilon)$.

**Lema 3.3 (Vectores tangentes correctos).** Sea $g_\Gamma \in \mathcal{M}$ con ceros $\{\pm\gamma_j\}$ de multiplicidades $m_j$. La curva admisible $\epsilon \mapsto g_{\Gamma(\epsilon)}$ que mueve $\pm\gamma_j \mapsto \pm(\gamma_j+\epsilon)$ tiene vector tangente en $\epsilon = 0$:
$$t_j(s) = \frac{\partial}{\partial\epsilon} g_{\Gamma(\epsilon)}(s)\Big|_{\epsilon=0} = -\,\frac{4\,m_j\,\gamma_j}{s^2-\gamma_j^2}\; g_\Gamma(s), \tag{3.1}$$
que es **par** en $s$ y pertenece a $H_\lambda$ (el polo aparente en $\pm\gamma_j$ se cancela contra el cero de orden $2m_j$ de $g_\Gamma$).

*Demostración.* Sobre la línea, el par contribuye el factor $\bigl((s^2-\gamma_j^2)^2\bigr)^{m_j}$ a $g_\Gamma$ (módulo constantes positivas y los compensadores exponenciales de Hadamard, cuya contribución conjunta del par es independiente de $s$ módulo una constante multiplicativa que se reabsorbe en la dirección constante, disponible por el Lema 4.1 abajo). Entonces
$$\frac{\partial}{\partial\epsilon}\log\bigl((s^2-(\gamma_j+\epsilon)^2)^{2m_j}\bigr)\Big|_{\epsilon=0} = 2m_j\cdot\frac{-2\gamma_j}{s^2-\gamma_j^2} = -\frac{4m_j\gamma_j}{s^2-\gamma_j^2}. \qquad\square$$

**Ecuaciones de Euler–Lagrange corregidas.** Para $g^* = |\eta^*|^2$ con ceros $\{\pm\gamma_j^*\}$, multiplicidades $m_j^*$:
$$\boxed{\;\mathrm{EL}_j:\quad \int_\mathbb{R} W_\lambda(s)\,\bigl(f_0(s)-g^*(s)\bigr)\, g^*(s)\,\frac{\gamma_j^*}{s^2-(\gamma_j^*)^2}\,dm_\infty(s) = 0 \quad \forall j.\;} \tag{3.2}$$
El kernel es par y las ecuaciones son no triviales. La estructura de ortogonalidad del Doc 97 (Teorema 2.7, Corolario 2.8) se conserva con el reemplazo $K_j^* \rightsquigarrow \tilde K_j^*(s) = \gamma_j^*/(s^2-(\gamma_j^*)^2)$.

### 3.2. Corrección B: el signo de la segunda variación transversal del Doc 93

**Lema 3.4 (Error de parametrización en Doc 93 §2.3).** En el Doc 93, la "variación transversal" se definió como $\epsilon = i\delta$ (Definición 2.1), pero el cálculo de §2.3 sustituye $\alpha_j + i\delta = 1/2 + i(\gamma_j+\delta)$: ese desplazamiento es **tangencial** (a lo largo de la línea crítica). La variación genuinamente transversal es $\epsilon = \delta$ real, con ceros desplazados a $1/2\pm\delta+i\gamma_j$, y produce el factor con signo **más**:
$$|R^{\mathrm{transv}}_{\delta}(1/2+is)|^2 = \left(1+\frac{\delta^2}{(s-\gamma_j)^2}\right)^{2}\left(1+\frac{\delta^2}{(s+\gamma_j)^2}\right)^{2},$$
coincidente con (2.1), no $(1 - 2\delta^2 K_j + O(\delta^4))$ como en el Lema 2.3 del Doc 93.

*Demostración.* Con el cero en $1/2+\delta+i\gamma_j$: $\bigl|(1/2+is) - (1/2+\delta+i\gamma_j)\bigr|^2 = \delta^2 + (s-\gamma_j)^2$. Dividiendo por $(s-\gamma_j)^2$ se obtiene $1+\delta^2/(s-\gamma_j)^2 \geq 1$. Es exactamente el cálculo del Doc 83 §1.2 (que es el correcto). $\square$

**Proposición 3.5 (Segunda variación transversal: signo corregido).** En el modelo de juguete, la única dirección transversal en $f_0^{on}$ (Observación 1.1) es el desdoblamiento del doble cero en $\pm\gamma_0$. Sea $\psi(\delta') := \|f_0 - f_0^{on}\,R_{\gamma_0,\delta'}\|^2_{H_\lambda}$ para $\delta'\in[0,\delta]$ la distancia a lo largo de esa curva transversal. Entonces:

(a) $\psi(\delta) = 0$ exactamente (la curva alcanza $f_0$).

(b) $\psi'(0) = 0$ y
$$\psi''(0) = -8\,\mathcal{Q}_\lambda^{(0)} \;<\; 0, \qquad \mathcal{Q}_\lambda^{(0)} := \int_\mathbb{R} W_\lambda\,(f_0-f_0^{on})\,f_0^{on}\,K_0\,dm_\infty \;>\;0.$$

Es decir: $f_0^{on}$ es un **máximo local estricto**, no un mínimo, a lo largo de la curva transversal; la curva es una dirección de descenso hacia $f_0$.

*Demostración.* (a) Por la Proposición 2.1, $f_0 = f_0^{on}R_{\gamma_0,\delta}$. (b) Por la Proposición 2.2 aplicada con parámetro $\delta'$: $f_0^{on}R_{\gamma_0,\delta'} = f_0^{on} + 2\delta'^2 K_0 f_0^{on} + O(\delta'^4)$ en $H_\lambda$. Entonces
$$f_0 - f_0^{on}R_{\gamma_0,\delta'} = D_0 - 2\delta'^2 K_0 f_0^{on} + O(\delta'^4), \qquad D_0 := f_0 - f_0^{on} \geq 0,$$
y
$$\psi(\delta') = \psi(0) - 4\delta'^2 \int W_\lambda\, D_0\, f_0^{on} K_0\,dm_\infty + O(\delta'^4) = \psi(0) - 4\delta'^2\,\mathcal{Q}_\lambda^{(0)} + O(\delta'^4).$$
La positividad $\mathcal{Q}_\lambda^{(0)}>0$ es el argumento del Doc 93, Proposición 4.3(a) (integrando $\geq 0$, positivo en un conjunto de medida positiva), que es correcto; lo incorrecto era el signo del término de orden $\delta'^2$. $\square$

**Observación 3.6 (Alcance de la corrección).** La Proposición 3.5 **refuta** el Corolario 4.4 y la Proposición 6.6 del Doc 93 ("convexidad de $\mathcal{M}$ hacia $f_0$"): bajo $\neg$RH (en el juguete), la dirección normal genuina es de descenso, lo cual es geométricamente obvio a posteriori — desproyectar los ceros hacia sus posiciones verdaderas acerca $f_0^{on}$ a $f_0$, hasta alcanzarlo en $\delta'=\delta$. No hay contradicción con $\tilde\delta_\lambda^2>0$: la curva transversal sale de $\mathcal{M}$ (para $\delta'>0$ el cuádruplo está fuera de la línea), de modo que el descenso no es realizable dentro de $\mathcal{M}$. La cota $T_\lambda \geq 2\delta^2 K_\lambda(\gamma_0)$ del Doc 86 y el criterio P39 quedan intactos: no dependen del signo de $\psi''$.

---

## §4. Objeto (ii): Euler–Lagrange para $g^*$ y su solución a primer orden

### 4.1. Linealización del problema variacional

Buscamos $g \in \mathcal{M}$ (o $\overline{\mathcal{M}}$) próximo a $f_0^{on}$, $g = f_0^{on} + h$. Como $\|f_0 - f_0^{on}\|_{H_\lambda} = 2\delta^2\|K_0f_0^{on}\|_{H_\lambda} + O(\delta^4)$ (Corolario 2.4) y $g = f_0^{on}$ es admisible, todo competidor relevante satisface $\|h\|_{H_\lambda} \leq C\delta^2$; para curvas en $\mathcal{M}$ parametrizadas por desplazamientos de ceros de tamaño $O(\delta^2)$, las correcciones de segundo orden de la curva son $O(\delta^4)$ (factores racionales exactos, Lema 4.1 abajo). El problema linealizado es entonces:
$$\text{minimizar } \bigl\|\,2\delta^2\, K_0\, f_0^{on} - h\,\bigr\|_{H_\lambda} \quad\text{sobre } h \in \mathcal{T}, \tag{4.1}$$
donde $\mathcal{T}$ es el **cono tangente cerrado** de $\mathcal{M}$ en $f_0^{on}$ dentro de $H_\lambda$ (clausura del conjunto de límites $\lim \tau_n^{-1}(g_n - f_0^{on})$ con $g_n\in\mathcal{M}$, $\tau_n\downarrow0$). Su solución es la proyección métrica de $2\delta^2 K_0f_0^{on}$ sobre $\mathcal{T}$, y
$$d\nu^* = \bigl(\mathrm{Id} - P_{\mathcal{T}}\bigr)\bigl(2\delta^2 K_0 f_0^{on}\bigr)\,dm_\infty + O(\delta^4). \tag{4.2}$$

Todo se reduce, a orden líder, a una pregunta: **¿qué contiene $\mathcal{T}$ y está $K_0f_0^{on}$ en él?** Obsérvese que las EL corregidas (3.2), evaluadas en el problema linealizado, son exactamente las ecuaciones normales de (4.1) respecto a las direcciones $t_j$ del Lema 3.3: $\langle 2\delta^2K_0f_0^{on} - h^*,\, t_j\rangle_{H_\lambda} = 0$. Pero el Lema 4.1 mostrará que $\mathcal{T}$ es estrictamente mayor que $\overline{\mathrm{span}}\{t_j\}$ visto término a término: contiene todas las combinaciones colectivas de movimientos de ceros lejanos, y eso decide el problema.

### 4.2. El cono tangente contiene las direcciones polinomiales pares

**Lema 4.1 (Direcciones polinomiales).** Para todo polinomio par $p(s) = \sum_{k=0}^K p_k s^{2k}$ con coeficientes reales (de cualquier signo) y todo $\epsilon_0 > 0$, existe una familia $\{g_\tau\}_{\tau\in[0,\tau_0]}\subset\mathcal{M}$, obtenida moviendo un número finito de ceros lejanos $\gamma_{j_1} < \cdots < \gamma_{j_N}$ ($N = K+1$) de $\zeta_{\mathrm{on}}$ en cantidades $\tau a_i$, tal que
$$g_\tau = f_0^{on}\,\bigl(1 + \tau\,p(s) + \tau\, e_\tau(s)\bigr), \qquad \|f_0^{on} e_\tau\|_{H_\lambda} \leq \epsilon_0 + C(p,\Gamma)\,\tau,$$
con $C(p,\Gamma)$ independiente de $\tau$. En consecuencia, el cono tangente cerrado $\mathcal{T}$ contiene el subespacio
$$\mathcal{T}_{\mathrm{pol}} := \overline{\mathrm{span}}^{H_\lambda}\bigl\{\, f_0^{on}(s)\, s^{2k} \;:\; k \geq 0 \,\bigr\}.$$

*Demostración.* Mover el par $\pm\gamma_{j}$ en $\epsilon_i = \tau a_i$ multiplica $f_0^{on}$ por el factor exacto $\bigl((s^2-(\gamma_{j}+\epsilon_i)^2)/(s^2-\gamma_{j}^2)\bigr)^2$ (más una constante positiva de los compensadores de Hadamard, que es $1+O(\tau)$ y se absorbe). Para $|s| \leq \gamma_{j}/2$:
$$\log\frac{(s^2-(\gamma_j+\epsilon_i)^2)^2}{(s^2-\gamma_j^2)^2} = 2\log\Bigl(1 - \frac{2\gamma_j\epsilon_i+\epsilon_i^2}{\gamma_j^2 - s^2}\cdot(-1)\Bigr) = \frac{4\epsilon_i}{\gamma_j}\sum_{k\geq 0}\Bigl(\frac{s^2}{\gamma_j^2}\Bigr)^k + O(\epsilon_i^2),$$
usando $1/(s^2-\gamma_j^2) = -\gamma_j^{-2}\sum_k (s^2/\gamma_j^2)^k$. Sumando sobre $i=1,\dots,N$, el coeficiente de $s^{2k}$ es $\sum_i 4 a_i\,\gamma_{j_i}^{-(2k+1)}\,\tau$. La matriz $\bigl(4\gamma_{j_i}^{-(2k+1)}\bigr)_{k=0..K,\,i=1..N}$ es una Vandermonde generalizada en los nodos distintos $x_i = \gamma_{j_i}^{-2}$ con escalados de columna no nulos $4/\gamma_{j_i}$: invertible. Se eligen $a_i$ resolviendo $\sum_i 4a_i\gamma_{j_i}^{-(2k+1)} = p_k$. El error $e_\tau$ tiene dos fuentes: (1) los términos $k > K$ de la serie, de tamaño $\leq C\sum_i |a_i|\,\gamma_{j_i}^{-(2K+3)}\,|s|^{2K+2}$ en $|s|\leq\gamma_{j_1}/2$ — como $\|s^{2m}f_0^{on}\|_{H_\lambda}^{1/(2m)} \leq C\,m$ (momentos de $e^{-\pi|s|/2}$: $\int s^{4m}e^{-\pi s/2}ds = (4m)!\,(2/\pi)^{4m+1}$), basta tomar $\gamma_{j_1} \geq C'(K)$ grande para hacer esta contribución $\leq \epsilon_0/2$; (2) la región $|s| > \gamma_{j_1}/2$, donde el factor exacto es acotado por $C(p)$ y el peso $W_\lambda f_0^{on}\,dm_\infty \lesssim e^{-\pi\gamma_{j_1}/4}$ la aplasta por debajo de $\epsilon_0/2$ eligiendo $\gamma_{j_1}$ grande. Los términos $O(\epsilon_i^2) = O(\tau^2)$ dan la parte $C(p,\Gamma)\tau$. La dirección constante ($k=0$) cubre además las constantes de normalización de los compensadores. Ambos signos de $p_k$ son realizables porque $\epsilon_i = \tau a_i$ admite cualquier signo (los ceros lejanos pueden moverse hacia adentro o hacia afuera). $\square$

**Observación 4.2 (adición de pares en el infinito).** Alternativamente, añadir un par de ceros en $\pm\mu$ con $\mu\to\infty$ produce la dirección $-2s^2f_0^{on}/\mu^2 + O(\mu^{-4})$ (factor exacto $(1-s^2/\mu^2)^2$ tras renormalizar): es el mecanismo de "escape de ceros al infinito" del Doc 95 §2.6, ahora usado constructivamente. Da solo el signo negativo del coeficiente de $s^2$; el Lema 4.1 (movimiento de ceros existentes) da ambos signos, y es lo que usamos.

### 4.3. Densidad polinomial: el paso de Carleman–Riesz

**Lema 4.3 (Densidad de polinomios).** Sea $\mu_\star$ la medida finita $d\mu_\star = W_\lambda(s)\,\bigl(f_0^{on}(s)\bigr)^2\,dm_\infty(s)$ sobre $\mathbb{R}$. Entonces los polinomios son densos en $L^2(\mu_\star)$.

*Demostración.* Por (W-pol), por $f_0^{on} \leq f_0 \ll (1+|s|)^{1/2+\epsilon}$ (cota de convexidad [T86]) y por $dm_\infty \asymp |s|^{-1/2}e^{-\pi|s|/2}ds$ (Stirling; Doc 95, Lema 2.2), existe $A<\infty$ con $d\mu_\star \leq C(1+|s|)^{A}e^{-\pi|s|/2}ds$. Sus momentos satisfacen $m_{2k}(\mu_\star) \leq C\,(2k+A)!\,(2/\pi)^{2k}$, luego $m_{2k}^{-1/(2k)} \gtrsim 1/(Ck)$ y $\sum_k m_{2k}^{-1/(2k)} = \infty$: condición de Carleman, la medida es determinada (Hamburger). Por el teorema de M. Riesz, toda medida determinada tiene polinomios densos en $L^2$ (Akhiezer [A65], Cor. 2.3.3). $\square$

**Lema 4.4 ($K_0 \in L^2(\mu_\star)$).** $K_0$ es continua fuera de $\pm\gamma_0$, $K_0(s) = O(s^{-2})$ en infinito, y cerca de $\pm\gamma_0$ se tiene $K_0^2\,(f_0^{on})^2 \asymp (s\mp\gamma_0)^{-4}\cdot (s\mp\gamma_0)^{16} \to 0$ por (1.1). Luego $K_0 \in L^2(\mu_\star)$. $\square$

### 4.4. Solución de Euler–Lagrange a primer orden: existe en el límite, no en $\mathcal{M}$

**Teorema 4.5 (Absorción de la componente líder).** En el modelo de juguete, bajo (T1)–(T3):
$$\inf_{p \text{ polinomio par}} \bigl\|\,2K_0 f_0^{on} - p\cdot f_0^{on}\,\bigr\|_{H_\lambda} = \inf_p \|2K_0 - p\|_{L^2(\mu_\star)} = 0.$$
Es decir: la dirección de curvatura $K_0f_0^{on}$ (densidad líder de $d\nu$, ec. (2.5)) pertenece a $\mathcal{T}_{\mathrm{pol}} \subseteq \mathcal{T}$: es **totalmente absorbible** por el cono tangente cerrado de $\mathcal{M}$ en $f_0^{on}$.

*Demostración.* Inmediata de los Lemas 4.3 y 4.4. $\square$

**Respuesta al objeto (ii).** Las ecuaciones EL corregidas (3.2), linealizadas en torno a $f_0^{on}$, son las ecuaciones normales de la proyección (4.1). Por el Teorema 4.5, la proyección de la densidad líder es **ella misma**: el sistema linealizado "se resuelve" con
$$g^*_{\mathrm{lin}} = f_0^{on}\,(1 + 2\delta^2 K_0) + o(\delta^2) = f_0 + o(\delta^2),$$
**pero no es alcanzado por ningún elemento de $\mathcal{M}$**: la solución se realiza solo como límite de sucesiones $\{g_n\}\subset\mathcal{M}$ cuyas aproximaciones polinomiales requieren mover ceros cada vez más lejanos ($\gamma_{j_1}(n)\to\infty$). Es la materialización constructiva del fallo de ND1/ND3 anticipado en el Doc 95 §2: en el modelo de juguete, **ND1 falla efectivamente** (no hay minimizador en $\mathcal{M}$ que realice el orden líder; si el ínfimo se alcanza en $\overline{\mathcal{M}}$, el minimizador sombra es un objeto de la clausura con "ceros escapados"). GAP G2 (§9): no se determina aquí si el ínfimo se alcanza en $\overline{\mathcal{M}}$.

---

## §5. Objeto (iii): la descomposición $d\nu = d\nu^* + (g^*-f_0^{on})\,dm_\infty$ a orden $\delta^2$

**Teorema 5.1 (La distancia variacional es $o(\delta^2)$).** En el modelo de juguete, bajo (T1)–(T3):
$$\tilde\delta_\lambda(\delta) := \inf_{g\in\mathcal{M}}\|f_0 - g\|_{H_\lambda} = o(\delta^2) \qquad (\delta\to 0,\ \gamma_0,\lambda \text{ fijos}).$$
Más precisamente: para todo $\epsilon>0$ existe $C_\epsilon = C(\epsilon,\gamma_0,\lambda) <\infty$ con
$$\tilde\delta_\lambda(\delta) \;\leq\; \epsilon\,\delta^2 \;+\; C_\epsilon\,\delta^4 \qquad \forall \delta\in(0,1/2).$$

*Demostración.* Dado $\epsilon>0$: por el Teorema 4.5 elíjase un polinomio par $p_\epsilon$ con $\|2K_0 - p_\epsilon\|_{L^2(\mu_\star)} \leq \epsilon/2$. Por el Lema 4.1 con $\tau = \delta^2$ y $\epsilon_0 = \epsilon/4$, existe $g_\delta \in \mathcal{M}$ (ceros lejanos movidos en cantidades $O(\delta^2)$) con
$$g_\delta = f_0^{on}\bigl(1 + \delta^2 p_\epsilon + \delta^2 e\bigr), \qquad \|f_0^{on}e\|_{H_\lambda} \leq \tfrac{\epsilon}{4} + C(p_\epsilon)\,\delta^2.$$
Por la Proposición 2.3, $f_0 = f_0^{on}(1 + 2\delta^2K_0 + \delta^4 E_\delta)$ con $\|f_0^{on}E_\delta\|_{H_\lambda}\leq C(\gamma_0,\lambda)$. Entonces
$$\|f_0 - g_\delta\|_{H_\lambda} \leq \delta^2\,\|(2K_0-p_\epsilon)f_0^{on}\|_{H_\lambda} + \delta^2\|f_0^{on}e\|_{H_\lambda} + \delta^4\|f_0^{on}E_\delta\|_{H_\lambda} \leq \epsilon\,\delta^2\cdot\tfrac34 + C_\epsilon\delta^4. \qquad\square$$

**Corolario 5.2 (Estructura de la descomposición del Doc 97, Prop. 9.1, en el juguete).** Bajo (H-ND1) (existencia de $g^*$ en $\overline{\mathcal{M}}$; condicional):
$$\underbrace{d\nu}_{\text{masa } \asymp\, \delta^2} \;=\; \underbrace{d\nu^*}_{\text{masa } =\, o(\delta^2)} \;+\; \underbrace{(g^* - f_0^{on})\,dm_\infty}_{\text{masa } \asymp\, \delta^2},$$
donde "masa" denota la norma $H_\lambda$ de la densidad. Es decir:

(a) La parte **absorbible** de $d\nu$ es **todo el orden líder**: $(g^*-f_0^{on})\,dm_\infty = 2\delta^2K_0f_0^{on}\,dm_\infty + o(\delta^2)$.

(b) La parte **irreducible** $d\nu^*$ es $o(\delta^2)$: estrictamente subdominante. Respuesta a la pregunta "(iii) ¿$d\nu^* = O(\delta^2)$ o $O(\delta^4)$?": **no es $O(\delta^2)$ con coeficiente positivo; está probado $o(\delta^2)$; la cota $O(\delta^4)$ exacta es un GAP (G3)**, porque la constante $C_\epsilon$ del Teorema 5.1 puede explotar cuando $\epsilon\to0$ (depende del grado del polinomio aproximante) y el trade-off $\epsilon(\delta)$ óptimo no está cuantificado.

(c) Cota inferior: $\tilde\delta_\lambda(\delta) > 0$ para todo $\delta\in(0,1/2)$ por el criterio del Doc 82 ($\tilde\delta^2_\lambda = 0 \iff$ RH, y en el juguete $\neg$RH). El test no produce ninguna cota inferior cuantitativa en $\delta$; ese es exactamente el contenido no trivial de ND4 (Doc 95 §7.4), que sigue abierto.

**Proposición 5.3 (Separación de funcionales: $T_\lambda$ vs. $\tilde\delta_\lambda^2$).** En el modelo de juguete:
$$T_\lambda = \int W_\lambda\,d\nu \;\geq\; 2\delta^2\,K_\lambda(\gamma_0) \;\asymp\; \delta^2 \qquad (\text{Doc 86, §6}),$$
mientras que $\tilde\delta_\lambda^2 = o(\delta^4)$ por el Teorema 5.1. Por tanto **$T_\lambda$ y $\tilde\delta_\lambda^2$ no son comparables**: el funcional de traza (lineal en $d\nu$, referencia fija $f_0^{on}$) detecta el cuádruplo a orden $\delta^2$; el funcional de distancia (que re-optimiza la referencia sobre $\mathcal{M}$) lo detecta a un orden estrictamente superior. Cualquier identificación cuantitativa $T_\lambda \approx \tilde\delta_\lambda^2$ queda refutada en el juguete. $\square$

**Observación 5.4 (mecanismo).** La razón estructural de la absorción es la identidad
$$K_0(s) = -\tfrac{1}{2}\,\partial_{\gamma_0}\Bigl(\frac{-4\gamma_0}{s^2-\gamma_0^2}\Bigr) = -\tfrac{1}{2}\,\partial_{\gamma_0}\,\hat t_0(s),$$
donde $\hat t_0$ es el kernel tangente (3.1) en $\gamma_0$: la densidad líder de $d\nu$ es la **derivada del campo tangente respecto a la posición del cero** — un objeto de segundo jet (curvatura, segunda forma fundamental del Doc 93 §6), que no está en el span de los tangentes en los ceros fijos $\{\gamma_j\}$, pero sí en su clausura **una vez que se permite la reorganización colectiva de los ceros lejanos** (Lema 4.1 + Lema 4.3). La absorción es necesariamente **deslocalizada**: ningún movimiento finito de ceros cerca de $\gamma_0$ la realiza; las sucesiones minimizantes reparten la corrección sobre colas de ceros que escapan a infinito.

---

## §6. Objeto (iv): la contribución del cuádruplo al índice negativo $\kappa$

Trabajamos en el marco del Doc 91/96: $(\mathcal{K},Q)$ espacio de Pontryagin de Weil–Connes, $H_C$ el operador $Q$-autoadjunto cuyos autovalores son $\rho - 1/2$ para $\rho$ cero de $\xi$ (Doc 96, Prop. 4.10).

**Proposición 6.1 (El subespacio $\mathcal{K}_{\mathrm{off}}$ del cuádruplo).** En el modelo de juguete:

(a) Los autovalores de $H_C$ fuera de $i\mathbb{R}$ son exactamente los cuatro números
$$z_1 = \delta + i\gamma_0,\quad \bar z_1 = \delta - i\gamma_0,\quad z_2 = -\delta + i\gamma_0,\quad \bar z_2 = -\delta - i\gamma_0,$$
con autovectores $v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2}$ (simples, por (T1)). El subespacio del Teorema 8.1 del Doc 96 es
$$\mathcal{K}_{\mathrm{off}} = \mathrm{span}\{v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2}\}, \qquad \dim \mathcal{K}_{\mathrm{off}} = 4.$$

(b) Para $H_C$ $Q$-autoadjunto y autovalores $\lambda,\mu$: $Q(v_\lambda, v_\mu) = 0$ salvo que $\mu = \bar\lambda$. En particular cada autovector es $Q$-neutro: $Q(v_{z_i},v_{z_i}) = 0$.

(c) En la base ordenada $(v_{z_1}, v_{\bar z_1}, v_{z_2}, v_{\bar z_2})$, la matriz de Gram de $Q|_{\mathcal{K}_{\mathrm{off}}}$ es diagonal por bloques con dos bloques hiperbólicos:
$$G(\delta) = \begin{pmatrix} 0 & q_1 & & \\ \bar q_1 & 0 & & \\ & & 0 & q_2 \\ & & \bar q_2 & 0 \end{pmatrix}, \qquad q_i = q_i(\delta) \neq 0,$$
con autovalores $\pm|q_1|, \pm|q_2|$: signatura $(2,2)$.

(d) Por tanto
$$\boxed{\;\kappa = \mathrm{neg.ind}\bigl(Q|_{\mathcal{K}_{\mathrm{off}}}\bigr) = 2 \quad \text{para todo } \delta\in(0,1/2),\;}$$
**independiente de $\delta$**, y discontinuo en $\delta = 0$ (donde $\kappa = 0$). Consistente con el teorema puente P35 ($\kappa = 2m$ con $m = 1$ cuádruplo) y con el Doc 96, Prop. 2.14 ($\dim\mathcal{K}_{\mathrm{ceros}} = 2\kappa = 4$).

*Demostración.* (a) Doc 96, Prop. 4.10 y Teorema 8.1: los autovalores no-$i\mathbb{R}$ son $\rho-1/2$, $\rho\in Z_\delta$. (b) $Q(H_Cv_\lambda, v_\mu) = Q(v_\lambda, H_Cv_\mu)$ da $\lambda\,Q(v_\lambda,v_\mu) = \bar\mu\,Q(v_\lambda,v_\mu)$ (con $Q$ hermitiana, antilineal en la segunda entrada), luego $Q(v_\lambda,v_\mu)=0$ si $\lambda\neq\bar\mu$. Con $\lambda=\mu$ no real: $Q(v_\lambda,v_\lambda)=0$. (c) Por (b), los únicos apareamientos no nulos posibles son $\{z_1,\bar z_1\}$ y $\{z_2,\bar z_2\}$ ($\overline{z_1} = \bar z_1 \neq z_2, \bar z_2$). Si algún $q_i$ fuera $0$, $Q$ sería degenerada sobre $\mathcal{K}_{\mathrm{off}}$, contradiciendo la no-degeneración de la descomposición $Q$-ortogonal del Doc 96, Teorema 8.1 (un vector $Q$-ortogonal a $\mathcal{K}_{\mathrm{off}}$ y a $\mathcal{K}_{\mathrm{crit}}$ sería $Q$-ortogonal a todo $\mathcal{K}$). Cada bloque $2\times2$ de la forma $\bigl(\begin{smallmatrix}0&q\\ \bar q&0\end{smallmatrix}\bigr)$ tiene autovalores $\pm|q|$: signatura $(1,1)$ — es el bloque hiperbólico canónico de la teoría de productos escalares indefinidos ([GLR83], Cap. I). (d) Suma de los dos bloques: $\mathrm{sig} = (2,2)$, $\kappa = 2$; $\dim\mathcal{K}_{\mathrm{off}} = 4 = 2\kappa$. $\square$

**Observación 6.2 (convención de apareamiento).** Algunas presentaciones de la forma de Weil aparean $\rho \leftrightarrow 1-\bar\rho$, es decir $z \leftrightarrow -\bar z$ (que en el cuádruplo aparea $z_1 \leftrightarrow z_2$). Bajo cualquiera de las dos convenciones la matriz de Gram consta de **dos planos hiperbólicos** sobre un espacio de dimensión 4 y $\kappa = 2$: la conclusión (d) es robusta. La elección de convención sí afecta cuál descomposición fina en planos es canónica; véase §8 (fallo del mapa fino). GAP G5: la convención correcta para el $Q$ del Doc 91 no se fija aquí.

**Observación 6.3 (qué son los generadores).** En el modelo de Mellin, $v_{z}$ es (formalmente) la clase en $\mathcal{K}$ del funcional residual $f \mapsto \hat f(1/2+z)$ en el cero correspondiente: los generadores de $\mathcal{K}_{\mathrm{off}}$ están **rígidamente indexados por los cuatro ceros del cuádruplo** — frecuencia $\pm\gamma_0$ y desplazamiento $\pm\delta$. No dependen de ninguna optimización: son datos espectrales puntuales.

---

## §7. Objeto (v): el índice de Maslov del cruce $\delta: 0 \to \delta_0$

**Definición 7.1 (familia de formas del cruce).** Bajo (T4), sea $V(\delta) \subset \mathcal{K}$ el subespacio espectral (proyección de Riesz) de $H_C(\delta)$ asociado al cluster de autovalores cercanos a $\{\pm i\gamma_0\}$, para $\delta \in [0,\delta_0]$, identificado con un espacio fijo $V \cong \mathbb{C}^4$ mediante la familia de proyecciones (Kato). Sea $G(\delta) = Q|_{V(\delta)}$ la familia de formas hermitianas $4\times4$ resultante. Definimos el **índice de Maslov del cruce** como el flujo espectral
$$\mu_{\mathrm{cruce}} := \mathrm{sf}\bigl(\{G(\delta)\}_{\delta\in[0,\delta_0]}\bigr)$$
(número neto de autovalores de $G(\delta)$ que cruzan $0$, contados con signo; convención de Robbins–Salamon [RS93]).

**Proposición 7.2 (cálculo del cruce).** Bajo (T1)–(T4) y la regularidad de la familia (GAP G4 abajo):

(a) Para $\delta > 0$: $\mathrm{sig}\,G(\delta) = (2,2)$ (Proposición 6.1(c)).

(b) Para $\delta = 0$: los cuatro ceros colapsan en los dos ceros dobles críticos $1/2\pm i\gamma_0$. La contribución de un cero crítico de multiplicidad 2 a la forma de Weil es $2\,|\hat f(\rho_0)|^2$: de rango 1 y positiva por punto. Sobre el espacio de jets de dimensión 4 (valores y derivadas $\hat f(\rho_0), \hat f'(\rho_0)$ en $\pm\gamma_0$), $G(0)$ tiene signatura $(2,0)$ con núcleo de dimensión 2.

(c) En consecuencia, dos autovalores de $G(\delta)$ (los $-|q_1(\delta)|, -|q_2(\delta)|$) emergen del núcleo en $\delta = 0$ hacia el semieje negativo:
$$\mu_{\mathrm{cruce}} = -2, \qquad |\mu_{\mathrm{cruce}}| = 2 = \kappa.$$
El cruce ocurre exactamente en $\delta = 0$ y en ningún otro punto de $[0,\delta_0]$ (los $q_i(\delta)\neq 0$ para $\delta>0$).

*Demostración (módulo G4).* (a) y la no-anulación para $\delta>0$ son la Proposición 6.1. (b): la forma límite solo evalúa $\hat f(\rho_0)$ (el término de cero de la fórmula explícita para un cero on-line de multiplicidad $m$ es $m\,\hat f(\rho_0)\overline{\hat f(\rho_0)}$); las direcciones de derivada $\hat f'(\rho_0)$ quedan en el núcleo. (c): conteo de autovalores: signatura $(2,2)$ para $\delta>0$, $(2,0)+\mathrm{nul}\,2$ en $\delta=0$; los dos autovalores negativos tienden a $0^-$ cuando $\delta\to0^+$ (continuidad de autovalores de la familia hermitiana), luego el flujo espectral neto en $[0,\delta_0]$ es $-2$. $\square$

**Detalle del colapso (base de jets).** Para hacer explícito el mecanismo del cruce: los funcionales de evaluación en los ceros que colapsan en $+\gamma_0$ son $e_\pm(\delta): f \mapsto \hat f(1/2\pm\delta+i\gamma_0)$. La base regularizada de jets es
$$x(\delta) = \tfrac{1}{2}\bigl(e_+(\delta)+e_-(\delta)\bigr) \xrightarrow{\delta\to0} \bigl[f\mapsto \hat f(\rho_0)\bigr], \qquad y(\delta) = \tfrac{1}{2\delta}\bigl(e_+(\delta)-e_-(\delta)\bigr) \xrightarrow{\delta\to0} \bigl[f\mapsto \hat f'(\rho_0)\bigr],$$
con $\rho_0 = 1/2+i\gamma_0$. El cambio de base $(e_+,e_-)\mapsto(x,\delta y)$ es singular de orden $\delta$; en la base $(x,y)$ la familia $G(\delta)$ es continua y su menor $2\times2$ asociado a las direcciones $y$ se anula linealmente en $\delta = 0$. Que los dos autovalores que se anulan lo hagan desde el lado negativo para $\delta>0$ está forzado por (a): no hay margen de elección de signos. El control uniforme de este reescalado dentro del espacio de Pontryagin completo (no solo en el modelo $4$-dimensional) es el contenido del GAP G4.

**GAP G4 (declarado).** La construcción de la familia $\{G(\delta)\}$ requiere: (i) que la proyección de Riesz del cluster sea continua en $\delta$ **incluyendo** la degeneración de Jordan en $\delta=0$ (la base de autovectores colapsa; debe pasarse a la base de jets con un reescalado $\sim\delta$ cuyo control no se hace aquí); (ii) la verificación V.1 del programa P35 (autoadjuntía $Q$ de $H_C$ en dominio preciso). Sin (i)–(ii), la Proposición 7.2 es un cálculo en el modelo de dimensión finita de la forma de Weil restringida, no un teorema sobre $H_C$.

**Observación 7.3 (lectura para $\mathbf{C}_D^B$).** La conjetura $\mathbf{C}_D^B$ del Doc 96 (§8.2) propone $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p = 0$. El juguete muestra el contenido mínimo que cualquier teoría tal debe reproducir: un único cuádruplo aporta $|\mu| = 2$ concentrado en el cruce $\delta=0$; bajo RH no hay cruce y $\mu = 0$. El índice de Maslov del cruce es, en el juguete, **exactamente $\kappa$ con signo**: la identificación Maslov–Krein (Conjetura 3.10 del Doc 96) se verifica en dimensión 4 trivialmente, porque ambos lados cuentan los mismos dos planos hiperbólicos. El juguete no aporta evidencia sobre la parte genuinamente difícil (descomposición local adélica $\mu = \mu_\infty + \sum_p\mu_p$).

---

## §8. Objeto (vi): confrontación B+D — la pregunta central

Disponemos ahora de los dos objetos en el mismo modelo:

| | **Dirección D: $d\nu^*$** | **Dirección B: $(\mathcal{K}_{\mathrm{off}}, Q)$** |
|---|---|---|
| Naturaleza | medida (densidad en $H_\lambda$) | subespacio de Pontryagin + forma |
| Magnitud | masa $= o(\delta^2)$ (Cor. 5.2) | $\kappa = 2$, entero, $\forall\delta>0$ (Prop. 6.1) |
| Dependencia en $\delta$ | continua, $\to 0$ | constante, discontinua en $0$ |
| Localización | **deslocalizada**: la componente localizada en $\pm\gamma_0$ ($2\delta^2K_0f_0^{on}$) es absorbida por reorganización de ceros lejanos (Teo. 4.5/5.1) | **rígidamente localizada** en el cuádruplo: 4 autovectores indexados por $\pm\delta\pm i\gamma_0$ (Obs. 6.3) |
| Estructura fina | sin descomposición canónica conocida | 2 planos hiperbólicos (convención-dependiente, Obs. 6.2) |
| Anulación | $d\nu^* = 0 \iff \delta = 0$ | $\mathcal{K}_{\mathrm{off}} = 0 \iff \delta = 0$ |

**Teorema 8.1 (Fracaso de la correspondencia fuerte $d\nu^* \leftrightarrow \mathcal{K}_{\mathrm{off}}$).** En el modelo de juguete, bajo (T1)–(T3) (y (H-ND1) donde se invoque $d\nu^*$ como objeto realizado):

(a) **Las magnitudes no coinciden a orden líder en $\delta^2$, ni en ningún orden.** $\kappa = 2$ es un invariante entero independiente de $\delta$, mientras que $\mathrm{masa}_{H_\lambda}(d\nu^*) \leq \tilde\delta_\lambda = o(\delta^2)$. No existe función $c(\gamma_0,\lambda) > 0$ tal que $\mathrm{masa}(d\nu^*) = c\cdot\kappa\cdot\delta^2 + o(\delta^2)$: el coeficiente de $\delta^2$ del lado D es **cero**, el del lado B (normalizado de cualquier forma no trivial en $\delta$) no lo es.

(b) **La localización no coincide.** La traza del cuádruplo en $d\nu$ a orden $\delta^2$ — el kernel $K_0$ concentrado en las frecuencias $\pm\gamma_0$ — es exactamente la parte que la optimización de la Dirección D **elimina** (Corolario 5.2(a)): es absorbida por una deformación deslocalizada (colas de ceros lejanos). Lo que queda ($d\nu^*$) no tiene, a orden líder, soporte efectivo identificable con las frecuencias del cuádruplo. En cambio $\mathcal{K}_{\mathrm{off}}$ está soportado exactamente en el cuádruplo y no es deformable: el índice negativo no puede "absorberse" moviendo ceros on-line, porque depende solo de los autovalores no-$i\mathbb{R}$ de $H_C$.

(c) **No hay mapa natural.** Un mapa $\Phi$ que envíe los 2 planos hiperbólicos de $\mathcal{K}_{\mathrm{off}}$ a componentes de $d\nu^*$ con masas comparables no puede existir: el dominio tiene estructura fija de dimensión 4 y el codominio es evanescente de orden superior. Incluso a nivel de $d\nu$ (no optimizado), la descomposición natural de la densidad líder es por frecuencias $\{+\gamma_0, -\gamma_0\}$ (los dos polos dobles de $K_0$), mientras que los planos hiperbólicos de $Q$ aparean autovectores **a través** de las frecuencias ($z_1$ con $\bar z_1$, es decir $+\gamma_0$ con $-\gamma_0$, en la convención de la Prop. 6.1(b)): las descomposiciones finas no se corresponden canónicamente (y la del lado B depende de la convención, Obs. 6.2).

(d) **Lo único que coincide es la anulación simultánea:** $d\nu^* = 0 \iff \delta = 0 \iff \mathcal{K}_{\mathrm{off}} = 0$. Pero esto es tautológico: cada lado es por separado equivalente a RH-en-el-juguete (lado D: Doc 82/Teorema 7.5 del Doc 97 bajo H-ND1+ND2; lado B: Doc 96, Cor. 8.2), de modo que la "coincidencia" pasa por RH y no constituye un puente con contenido propio.

*Demostración.* (a) Corolario 5.2(b) + Proposición 6.1(d). (b) Teorema 4.5, Corolario 5.2(a), Observación 5.4, Observación 6.3. (c) consecuencia de (a) (magnitudes) y del análisis de apareamientos en (b)/Obs. 6.2. (d) las dos equivalencias citadas. $\square$

**Conclusión sin rodeos.** **La conexión B+D, en la forma conjeturada ("la parte irreducible $d\nu^*$ es el avatar variacional de la localización del índice negativo en $\mathcal{K}_{\mathrm{off}}$, con magnitudes coincidentes a orden líder"), está muerta.** El modelo de juguete la refuta en el caso más favorable posible: un solo cuádruplo, expansiones exactas, sin interferencia entre ceros off-críticos.

**Teorema 8.2 (Lo que sí sobrevive: correspondencia $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$, no $d\nu^*$).** En el modelo de juguete, el objeto de la Dirección D que sí se corresponde estructuralmente con $\mathcal{K}_{\mathrm{off}}$ es el residual de **referencia fija** $d\nu = (f_0-f_0^{on})\,dm_\infty$ (Doc 89), no el optimizado:

(a) Magnitudes: $\mathrm{masa}_{H_\lambda}(d\nu) = 2\delta^2\|K_0f_0^{on}\|_{H_\lambda} + O(\delta^4) \asymp \delta^2$, y $T_\lambda = \int W_\lambda\,d\nu \geq 2\delta^2K_\lambda(\gamma_0)$ (Doc 86): escala $\delta^2$, el cuadrado del desplazamiento — la misma potencia que gobierna la apertura de los planos hiperbólicos ($z_i - i(\pm\gamma_0) = \pm\delta$) y el desdoblamiento de Jordan del cruce de Maslov (§7), que son fenómenos de segundo orden en la no-autoadjuntía (cf. P35, $\kappa = 2m$).

(b) Localización: la densidad líder $2\delta^2K_0f_0^{on}$ tiene sus dos resonancias en $\pm\gamma_0$, indexadas por el mismo cuádruplo que genera $\mathcal{K}_{\mathrm{off}}$; el conteo "2 resonancias del kernel $\leftrightarrow$ 2 planos hiperbólicos $\leftrightarrow$ $\kappa = 2$" es exacto en el juguete (con la salvedad de apareamiento fino de (c) arriba).

(c) Anulación: $d\nu = 0 \iff \delta = 0 \iff \kappa = 0$, y aquí la equivalencia del lado D es **incondicional** (Doc 83, Cor. 1.2), sin H-ND1/ND2.

*Demostración.* (a) Proposición 2.3 y Doc 86. (b) Proposición 2.2 y Proposición 6.1. (c) Doc 83 y Doc 96. $\square$

**Moraleja estructural.** El paso de $d\nu$ a $d\nu^*$ — es decir, la optimización sobre $\mathcal{M}$ que define la Dirección D en su versión Doc 97 — **destruye** la información localizada que el espacio de Pontryagin ve. El puente B+D debe construirse (si existe) entre $(\mathcal{K}_{\mathrm{off}}, Q)$ y los objetos de referencia fija ($d\nu$, $T_\lambda$, los kernels $K_\lambda(\gamma_j)$ del Doc 86), no con el minimizador sombra. Esto degrada el interés del programa del Doc 97 para el frente B+D, y simultáneamente revaloriza la línea Doc 83–86–89 (P39).

---

## §9. Gaps abiertos declarados

- **G1 (hipótesis estructurales).** (W-pol) y (W-par) se citan del marco CCM (Docs 82, 83, 95) sin demostración nueva aquí. Si $W_\lambda$ no fuera par, el Lema 3.1 cambia (las ecuaciones impares dejan de ser vacuas), pero las correcciones de §3.1–3.2 sobre la variación admisible permanecen.
- **G2 (alcance del ínfimo).** No se determina si $\tilde\delta_\lambda$ se alcanza en $\overline{\mathcal{M}}$ en el juguete; el Teorema 5.1 es una cota superior por sucesiones minimizantes explícitas, suficiente para todo §8. (H-ND1) sigue siendo condicional.
- **G3 (tasa exacta).** $\mathrm{masa}(d\nu^*) = o(\delta^2)$ probado; la conjetura natural es $O(\delta^4)$ (el siguiente término exacto $\delta^4E_\delta f_0^{on}$ de (2.4) contiene la componente $Q_4f_0^{on} = G$, posiblemente también absorbible — no analizado). Cuantificar $C_\epsilon$ del Teorema 5.1 (grado del polinomio vs. $\epsilon$, teoría de aproximación ponderada) decidiría la tasa.
- **G4 (regularidad de la familia de Maslov).** La continuidad de $\{G(\delta)\}$ a través de la degeneración de Jordan en $\delta=0$, y la verificación V.1 de P35, quedan abiertas; la Proposición 7.2 es un cálculo en el modelo finito-dimensional de la forma de Weil.
- **G5 (convención de apareamiento de $Q$).** $\lambda\leftrightarrow\bar\lambda$ vs. $\lambda\leftrightarrow-\bar\lambda$ (Obs. 6.2); $\kappa=2$ es robusto, la estructura fina de planos no.
- **G6 (no-anulación de las EL corregidas en $f_0^{on}$).** Con el kernel par (3.2), $\mathrm{EL}_j(f_0^{on}) = 2\delta^2\int W_\lambda (f_0^{on})^2 K_0(s)\,\frac{\gamma_j}{s^2-\gamma_j^2}\,dm_\infty + O(\delta^4)$; el kernel $\gamma_j/(s^2-\gamma_j^2)$ cambia de signo en $|s|=\gamma_j$ y la no-anulación genérica de estas integrales (que restauraría el Lema 4.6 del Doc 95 en su forma corregida) no se demuestra aquí.

---

## §10. VEREDICTO

**RUTA CERRADA** — para la correspondencia fuerte B+D tal como fue formulada (objeto irreducible $d\nu^*$ de la Dirección D $\leftrightarrow$ localización del índice negativo en $\mathcal{K}_{\mathrm{off}}$ de la Dirección B, con mapa natural y magnitudes coincidentes a orden líder en $\delta^2$).

**Razón precisa.** En el modelo de juguete de un cuádruplo: (1) las magnitudes viven en escalas incompatibles — $\kappa = 2$ es un entero independiente de $\delta$ (Prop. 6.1), mientras que la masa de $d\nu^*$ es $o(\delta^2)$ (Teorema 5.1, Cor. 5.2), de modo que el coeficiente de $\delta^2$ del lado D es nulo y no puede igualar nada no trivial del lado B; (2) la localización es opuesta — $\mathcal{K}_{\mathrm{off}}$ está rígidamente anclado al cuádruplo, mientras que la componente de $d\nu$ localizada en $\pm\gamma_0$ es exactamente la que la optimización variacional absorbe mediante reorganización deslocalizada de ceros on-line lejanos (Teorema 4.5); (3) la única coincidencia restante (anulación simultánea) es tautológica vía RH.

**Lo rescatado por el test** (no altera el veredicto, orienta el programa):
1. La correspondencia viva es $\mathcal{K}_{\mathrm{off}} \leftrightarrow d\nu$ (referencia fija, Doc 89/P39): misma escala $\delta^2$, misma indexación por el cuádruplo, equivalencia de anulación incondicional (Teorema 8.2). El frente B+D debe reformularse sobre $d\nu$ y $T_\lambda$, no sobre $g^*$/$d\nu^*$.
2. Teorema de absorción (Teorema 5.1): $\tilde\delta_\lambda = o(\delta^2)$, con fallo constructivo de ND1 en el juguete y separación cuantitativa $T_\lambda \asymp \delta^2$ vs. $\tilde\delta_\lambda^2 = o(\delta^4)$ (Prop. 5.3) — los dos funcionales del programa no son intercambiables.
3. Dos correcciones internas demostradas: el kernel EL de Docs 95/97 es impar y vacuo por paridad (Lema 3.1; kernel correcto en (3.2)); la segunda variación transversal del Doc 93 tiene el signo equivocado por un error de parametrización ($\psi''(0) = -8\mathcal{Q}_\lambda^{(0)} < 0$: $f_0^{on}$ es máximo local en la dirección normal genuina, Prop. 3.5). Los resultados aguas abajo que dependían de "convexidad de $\mathcal{M}$ hacia $f_0$" (Doc 93 §6, Doc 95 §1.3) deben revisarse.
4. El índice de Maslov del cruce vale $|\mu| = 2 = \kappa$ en el juguete (Prop. 7.2, módulo G4): dato de contraste mínimo para cualquier futura teoría adélica $\mathbf{C}_D^B$.

---

## Apéndice A: Notación del documento

| Símbolo | Significado | Referencia |
|---|---|---|
| $Z_\delta$ | cuádruplo off-crítico $\{1/2\pm\delta\pm i\gamma_0\}$ | (T1) |
| $f_0,\ f_0^{on}$ | $|\zeta(1/2+is)|^2$, $|\zeta_{\mathrm{on}}(1/2+is)|^2$ | Docs 82, 83 |
| $G(s)$ | parte regular: $f_0^{on} = (s^2-\gamma_0^2)^4G$, $G(\pm\gamma_0)>0$ | (1.1) |
| $R_{\gamma_0,\delta}$ | factor del cuádruplo $f_0/f_0^{on}$ | (2.1) |
| $K_0(s)$ | $\frac{1}{(s-\gamma_0)^2}+\frac{1}{(s+\gamma_0)^2} = \frac{2(s^2+\gamma_0^2)}{(s^2-\gamma_0^2)^2}$ | Prop. 2.2; Doc 93, Lema 2.3 |
| $d\nu$ | $(f_0-f_0^{on})\,dm_\infty \geq 0$ (referencia fija) | Doc 83, Cor. 1.3; Doc 89 |
| $d\nu^*$ | $(f_0-g^*)\,dm_\infty$ (referencia optimizada) | Doc 97, Def. 2.1 |
| $\nu_2$ | densidad líder $2K_0f_0^{on}$ de $d\nu/\delta^2$ | (2.5) |
| $t_j$ | vector tangente admisible $-4m_j\gamma_j\,g_\Gamma/(s^2-\gamma_j^2)$ | Lema 3.3 |
| $\mathcal{T},\ \mathcal{T}_{\mathrm{pol}}$ | cono tangente cerrado; subespacio de direcciones polinomiales $f_0^{on}s^{2k}$ | §4.1, Lema 4.1 |
| $\mu_\star$ | $W_\lambda\,(f_0^{on})^2\,dm_\infty$ (medida de aproximación) | Lema 4.3 |
| $\tilde\delta_\lambda$ | distancia variacional $\inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}$ | Doc 82 |
| $\mathcal{K}_{\mathrm{off}}$ | subespacio de Pontryagin del cuádruplo, $\dim 4$ | Doc 96, Teo. 8.1; Prop. 6.1 |
| $q_i(\delta)$ | apareamientos hiperbólicos $Q(v_{z_i}, v_{\bar z_i})$ | Prop. 6.1(c) |
| $\kappa$ | índice negativo $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = 2$ | Prop. 6.1(d); P35 |
| $G(\delta)$ | familia de Gram del cruce sobre $V\cong\mathbb{C}^4$ | Def. 7.1 |
| $\mu_{\mathrm{cruce}}$ | flujo espectral de $G(\delta)$ en $[0,\delta_0]$, $=-2$ | Prop. 7.2 |
| $\mathcal{Q}_\lambda^{(0)}$ | coeficiente de segunda variación en la dirección del cuádruplo | Prop. 3.5; Doc 93, Def. 4.1 |

## Apéndice B: Tabla de dependencias lógicas de los resultados principales

| Resultado | Incondicional en el juguete | Hipótesis usadas |
|---|---|---|
| Prop. 2.1–2.3, Cor. 2.4 ($R$, $d\nu$, masas) | sí | (T1), (W-pos), (W-pol) |
| Lema 3.1 (EL impar vacua) | sí | (W-par) |
| Lema 3.3, ec. (3.2) (EL corregida) | sí | (T1) |
| Prop. 3.5 ($\psi''(0)<0$, corrección Doc 93) | sí | (T1)–(T3) |
| Teorema 4.5 / Teorema 5.1 (absorción, $\tilde\delta_\lambda = o(\delta^2)$) | sí | (T1)–(T3) + [A65] |
| Cor. 5.2 (estructura de $d\nu^*$) | parcial | + (H-ND1) para hablar de $d\nu^*$ realizado |
| Prop. 6.1 ($\kappa=2$) | sí, dado el marco Doc 91/96 | V.1 de P35 implícita en "$H_C$ es $Q$-autoadjunto" |
| Prop. 7.2 (Maslov $=-2$) | modelo finito-dim. | (T4) + GAP G4 |
| Teorema 8.1 (no-correspondencia) | sí | unión de las anteriores |
| Teorema 8.2 (correspondencia con $d\nu$) | sí | (T1)–(T3) + marco Doc 96 |

---

## Referencias

- [A65] N. I. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver & Boyd, 1965. (Teorema de M. Riesz: densidad de polinomios para medidas determinadas; criterio de Carleman.)
- [GLR83] I. Gohberg, P. Lancaster, L. Rodman, *Matrices and Indefinite Scalar Products*, Birkhäuser, 1983. (Formas canónicas de pares $(G, H)$ hermitianos; bloques hiperbólicos.)
- [AI89] T. Ya. Azizov, I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley, 1989. (Teoría de Pontryagin; $Q$-ortogonalidad espectral.)
- [RS93] J. Robbins, D. Salamon, *The Maslov index for paths*, Topology 32 (1993), 827–844. (Flujo espectral y convenciones del índice de Maslov.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown), Oxford, 1986. (Cota de convexidad sobre la línea crítica.)
- Documentos internos del programa: Docs 82, 83, 86, 89, 91, 93, 95, 96, 97 (Fases 33–34); Papers P35 (teorema puente $\kappa = 2m$), P39 (criterio $T_\lambda = 0\;\forall\lambda \iff$ RH).

---

*Fin del Doc 98.*
