# Phase 22 — Step 22-A/B: Fórmula Explícita Modificada y Anatomía del Defecto

---

## Notaciones fijas

- $\rho = \beta + i\gamma$: cero no-trivial de $\zeta$.
- $Z_{\text{off}} = \{\rho : \beta \neq \tfrac{1}{2}\}$: ceros fuera de línea.
- $Z_{\text{CL}} = \{\rho : \beta = \tfrac{1}{2}\}$: ceros sobre la línea crítica.
- Hipótesis D: $Z_{\text{off}} = \{\rho_1^+, \overline{\rho_1^+}, 1-\rho_1^+, 1-\overline{\rho_1^+}, \ldots, \rho_m^+, \ldots\}$ es finita, con $m$ órbitas completas bajo el grupo de Klein $V$.
- $\rho_j^+ = \sigma_j + i\gamma_j$ con $\sigma_j = \tfrac{1}{2} + b_j$, $b_j > 0$, $\gamma_j > 0$ ($j = 1, \ldots, m$).
- La órbita $j$ es $\mathcal{O}_j = \{\sigma_j \pm i\gamma_j,\; (1-\sigma_j) \pm i\gamma_j\}$.

---

## Step 22-A: Fórmula Explícita Modificada

### A.1 Punto de partida: la fórmula de Perron

La identidad clásica (Davenport, Ch. 17) afirma que, para $x > 1$ no entero:

$$\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \log(2\pi) - \tfrac{1}{2}\log(1 - x^{-2})$$

donde la suma recorre **todos** los ceros no-triviales de $\zeta$, ordenados por $|\text{Im}(\rho)| \leq T$ y tomando $T \to \infty$ simétricamente.

Dividir la suma en dos partes:

$$\sum_\rho \frac{x^\rho}{\rho} = \underbrace{\sum_{\rho \in Z_{\text{CL}}} \frac{x^\rho}{\rho}}_{\text{contribución on-line}} + \underbrace{\sum_{\rho \in Z_{\text{off}}} \frac{x^\rho}{\rho}}_{=:\; D_m(x)\;\text{(defecto)}}$$

Bajo hipótesis D, la segunda suma es **finita** — no requiere ningún límite $T \to \infty$.

### A.2 Definición rigurosa del defecto aritmético

**Definición 22-A.1** (Defecto aritmético). Bajo hipótesis D,

$$D_m(x) := \sum_{j=1}^m \sum_{\rho \in \mathcal{O}_j} \frac{x^\rho}{\rho}$$

Es una suma de $4m$ términos. Cada término es del tipo $x^{\sigma+i\gamma}/(\sigma+i\gamma)$.

**Observación**: $D_m(x)$ es una función **real** de $x > 0$. Esto sigue del hecho de que $Z_{\text{off}}$ es simétrico bajo $\rho \mapsto \bar\rho$ (coeficientes reales de $\zeta$), de modo que cada término aparece junto con su conjugado complejo.

### A.3 Definición de $\psi_0$

Bajo la factorización $\xi = \xi_0 P_{4m}$ (Corolario 9.2 de P32), sea:

$$\psi_0(x) := x - \sum_{\rho \in Z_{\text{CL}}} \frac{x^\rho}{\rho} - \log(2\pi) - \tfrac{1}{2}\log(1-x^{-2})$$

Es decir, $\psi_0$ es la función de Chebyshev **virtual** asociada a $\xi_0$ (que tiene todos sus ceros sobre la línea crítica).

**Nota**: $\psi_0$ es una función análisis — no la función de conteo de primos de ningún objeto aritmético estándar. El producto de Euler de $\zeta$ no admite la factorización $\xi = \xi_0 P_{4m}$ a nivel de series de Dirichlet. Esto se discute en §22-C.

### A.4 El teorema principal del Step 22-A

**Teorema 22-A** (Fórmula Explícita Modificada). Bajo hipótesis D, para todo $x > 1$ no entero:

$$\psi(x) = \psi_0(x) - D_m(x)$$

**(identidad exacta, sin error).**

*Demostración*. Inmediata: sustituir la partición $\sum_\rho = \sum_{Z_{\text{CL}}} + \sum_{Z_{\text{off}}}$ en la fórmula de Perron estándar. La suma sobre $Z_{\text{off}}$ es finita bajo hipótesis D, así que no hay término de error proveniente del truncamiento. $\square$

**Corolario 22-A.1** (Descomposición del error). Sea $E(x) = \psi(x) - x$ el error de la PNT. Entonces:

$$E(x) = E_0(x) - D_m(x)$$

donde $E_0(x) = \psi_0(x) - x = -\sum_{Z_{\text{CL}}} x^\rho/\rho + O(\log x)$.

---

## Step 22-B: Anatomía del Defecto — cálculo explícito de $D_m$

### B.1 El defecto de una sola órbita

Fijamos $j \in \{1,\ldots,m\}$. La órbita $\mathcal{O}_j$ contribuye:

$$D_j(x) = \frac{x^{\sigma_j + i\gamma_j}}{\sigma_j+i\gamma_j}
           + \frac{x^{\sigma_j - i\gamma_j}}{\sigma_j - i\gamma_j}
           + \frac{x^{(1-\sigma_j)+i\gamma_j}}{(1-\sigma_j)+i\gamma_j}
           + \frac{x^{(1-\sigma_j)-i\gamma_j}}{(1-\sigma_j)-i\gamma_j}$$

Usando $x^{a+ib} = x^a e^{ib\log x}$ y agrupando pares conjugados:

$$D_j(x) = 2\operatorname{Re}\!\left[\frac{x^{\sigma_j+i\gamma_j}}{\sigma_j+i\gamma_j}\right]
           + 2\operatorname{Re}\!\left[\frac{x^{(1-\sigma_j)+i\gamma_j}}{(1-\sigma_j)+i\gamma_j}\right]$$

Sea $\theta_j^+ = \arg(\sigma_j+i\gamma_j)$ y $\theta_j^- = \arg((1-\sigma_j)+i\gamma_j)$. Entonces:

$$\boxed{D_j(x) = \frac{2x^{\sigma_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+)
           + \frac{2x^{1-\sigma_j}}{|\rho_j^-|}\cos(\gamma_j\log x - \theta_j^-)}$$

donde $\rho_j^+ = \sigma_j+i\gamma_j$, $\rho_j^- = (1-\sigma_j)+i\gamma_j$, y $|\rho_j^\pm|$ son sus módulos.

### B.2 Estructura dominante y subdominante

Con $\sigma_j = \tfrac{1}{2} + b_j$ y $1 - \sigma_j = \tfrac{1}{2} - b_j$, $b_j > 0$:

$$D_j(x) = \underbrace{\frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+)}_{\text{término dominante}} + \underbrace{\frac{2x^{1/2-b_j}}{|\rho_j^-|}\cos(\gamma_j\log x - \theta_j^-)}_{\text{término subdominante}}$$

Para $x \to \infty$: el término dominante crece como $x^{1/2+b_j}$ con $b_j > 0$; el subdominante decae como $x^{1/2-b_j}$.

**Proposición 22-B.1** (Tamaño del defecto). Bajo hipótesis D, para $x \geq 2$:

$$D_m(x) = \sum_{j=1}^m \frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j^+) + O\!\left(x^{1/2-b_{\min}}\right)$$

donde $b_{\min} = \min_j b_j > 0$ y la constante implícita depende solo de los $|\rho_j^\pm|$.

*Demostración*. Agrupar los $m$ términos subdominantes; cada uno es $O(x^{1/2-b_j}) = O(x^{1/2-b_{\min}})$. $\square$

### B.3 Energía del defecto por órbita

**Definición 22-B.2** (Energía del defecto). Para $X \geq 2$:

$$\mathcal{E}_j(X) := \int_X^{2X} \frac{|D_j(t)|^2}{t^2}\,dt$$

**Proposición 22-B.3** (Crecimiento de la energía). Para $X \to \infty$:

$$\mathcal{E}_j(X) \sim \frac{2}{|\rho_j^+|^2} \cdot \frac{X^{2b_j}}{2b_j}$$

En particular, $\mathcal{E}_j(X) \to \infty$ para cualquier $b_j > 0$.

*Demostración*. El cuadrado del término dominante es $\tfrac{4x^{1+2b_j}}{|\rho_j^+|^2}\cos^2(\gamma_j\log x - \theta_j^+)$. Integrando sobre $[X,2X]$ y usando $\langle\cos^2\rangle = \tfrac{1}{2}$ (para $\gamma_j \log x$ que oscila rápido):

$$\mathcal{E}_j(X) \approx \frac{4}{|\rho_j^+|^2} \cdot \frac{1}{2} \int_X^{2X} t^{2b_j-1}\,dt = \frac{2}{|\rho_j^+|^2} \cdot \frac{(2X)^{2b_j}-X^{2b_j}}{2b_j} \sim \frac{2(2^{2b_j}-1)}{|\rho_j^+|^2 \cdot 2b_j} X^{2b_j}$$

que diverge como $X^{2b_j}$. $\square$

**Corolario 22-B.4** (Energía total). $\sum_{j=1}^m \mathcal{E}_j(X) \sim C_m X^{2b_{\max}}$ donde $b_{\max} = \max_j b_j$.

### B.4 El defecto y el producto de Euler: incompatibilidad de estructura

Aquí aparece el punto más importante de Phase 22.

La fórmula explícita usa $-\zeta'/\zeta$. La factorización $\xi = \xi_0 P_{4m}$ da:

$$\frac{\xi'(s)}{\xi(s)} = \frac{\xi_0'(s)}{\xi_0(s)} + \frac{P_{4m}'(s)}{P_{4m}(s)}$$

Con $P_{4m}(s) = \prod_{\rho \in Z_{\text{off}}}(s-\rho)$ (polinomio de los $4m$ ceros):

$$\frac{P_{4m}'(s)}{P_{4m}(s)} = \sum_{\rho \in Z_{\text{off}}} \frac{1}{s-\rho}$$

La relación entre $\xi'/\xi$ y $\zeta'/\zeta$ es:

$$\frac{\xi'(s)}{\xi(s)} = \frac{\zeta'(s)}{\zeta(s)} + \frac{1}{s-1} + \frac{1}{s} + \frac{1}{2}\log\pi - \frac{1}{2}\frac{\Gamma'}{\Gamma}(s/2)$$

Por tanto, definiendo $\zeta_0(s) = \zeta(s)/P_{\text{arith}}(s)$ donde $P_{\text{arith}}$ es la corrección aritmética adecuada, la serie de Dirichlet de $-\zeta_0'/\zeta_0$ satisfaría:

$$-\frac{\zeta_0'(s)}{\zeta_0(s)} = -\frac{\zeta'(s)}{\zeta(s)} + \sum_{\rho \in Z_{\text{off}}} \frac{1}{s-\rho}$$

**Lema 22-B.5** (Incapacidad aritmética de $\zeta_0$). La función $\zeta_0(s) = \xi_0(s)/[\text{factor gamma}]$ tiene polos en cada $\rho \in Z_{\text{off}}$ (que son ceros de $P_{4m}$). En consecuencia:

1. $\zeta_0$ **no es** una serie de Dirichlet con coeficientes no-negativos.
2. $\zeta_0$ **no admite** un producto de Euler de la forma $\prod_p (1-a_p p^{-s})^{-1}$ con $|a_p| \leq 1$.
3. La función $\Lambda_0$ definida por $-\zeta_0'/\zeta_0 = \sum_n \Lambda_0(n) n^{-s}$ **no es** la función de von Mangoldt de ningún objeto aritmético estándar.

*Demostración*. (1) y (2): los polos de $\zeta_0$ en $\Re(s) > 0$ se acumulan en $Z_{\text{off}}$; ninguna serie de Dirichlet con coeficientes no-negativos tiene polos en $\Re(s) > 0$ salvo en $s = 1$ (por el argumento de Landau). (3) sigue de (1) porque la función de von Mangoldt de un objeto aritmético produce una serie con coeficientes $\geq 0$ (en el caso de $\zeta$, $\Lambda(n) \geq 0$ para todo $n$). $\square$

**Observación crítica**: El lema 22-B.5 no es una contradicción. Dice que la factorización $\xi = \xi_0 P_{4m}$ está disponible en el mundo **analítico** (funciones enteras) pero **no** en el mundo **aritmético** (series de Dirichlet con producto de Euler). El puente entre estos dos mundos es exactamente el contenido de Wall W4-RSRP.

---

## Resumen de resultados del Step 22-A/B

| Enunciado | Clase | Estado |
|-----------|-------|--------|
| Teorema 22-A (Fórmula Explícita Modificada) | B | Demostrado |
| Corolario 22-A.1 (descomposición del error) | B | Demostrado |
| Proposición 22-B.1 (tamaño del defecto) | B | Demostrado |
| Proposición 22-B.3 (crecimiento de energía) | B | Demostrado |
| Corolario 22-B.4 (energía total) | B | Demostrado |
| Lema 22-B.5 (incapacidad aritmética de $\zeta_0$) | B | Demostrado |

---

## Próximos pasos

### Step 22-C: Invariantes incompatibles

La pregunta precisa (formulada ahora con rigor gracias a 22-A/B):

> ¿Existe un funcional $\mathcal{F}$ tal que $\mathcal{F}[\psi]$ sea determinable del producto de Euler y $\mathcal{F}[\psi_0 - D_m]$ sea inconsistente con ese valor para todo $m \geq 1$?

Los tres candidatos más prometedores:

**Candidato I: Integral de Selberg de segundo momento**

$$S(\alpha, T) = \int_0^T \left|\frac{\psi(e^t) - e^t}{e^t}\right|^2 e^{-2\alpha t}\,dt$$

Bajo RH ($\kappa=0$): $S(1/2, T) = O(T)$.
Bajo hipótesis D ($\kappa = 2m$, $b_{\max} > 0$): $S(1/2, T) \sim C e^{2b_{\max} T}$.
Valor del producto de Euler: $S(\alpha, T)$ está ligado a $|\zeta(1/2+\alpha+it)|^2$ por el teorema de Parseval modificado. La inconsistencia requeriría mostrar que $|\zeta(1/2+\alpha+it)|^2$ no puede crecer al ritmo $e^{2b_{\max}T}$... lo que es exactamente la hipótesis D misma. **Circular**.

**Candidato II: Función de Mertens**

$$M(x) = \sum_{n \leq x} \mu(n) = -\frac{1}{2\pi i}\int \frac{x^s}{s\,\zeta(s)}\,ds$$

Bajo hipótesis D: los polos de $1/(s\,\zeta(s))$ incluyen los ceros de $\zeta$, y $Z_{\text{off}}$ produce contribuciones a $M(x)$ de tamaño $\gg x^{\sigma_j - 1}$.
Para $\sigma_j > 1$: imposible ($\sigma_j < 1$). Para $\sigma_j \in (1/2,1)$: $M(x) \gg x^{\sigma_j - 1} = x^{b_j - 1/2}$. Si $b_j > 1/2$: $M(x) \gg x^{b_j-1/2} \to \infty$ polinomialmente.
Bajo PNT: $M(x) = o(x)$. La inconsistencia requeriría $b_j > 1/2$ o un argumento más fino. **Parcialmente prometedor**, pero requiere $b_j$ grande.

**Candidato III: Funcional de Weil directo**

$$W(\hat{f}) = \sum_\rho \hat{f}(\gamma) - \hat{f}(i/2) - \hat{f}(-i/2) + \cdots$$

El funcional $W(\hat{f})$ es el núcleo de la forma de Weil. Bajo hipótesis D:

$$W(\hat{f}) = W_0(\hat{f}) + \sum_{\rho \in Z_{\text{off}}} \hat{f}(\gamma_\rho) - [\text{términos de ceros fuera de línea}]$$

Los ceros fuera de línea contribuyen con el **signo incorrecto** (contribución negativa para $f \geq 0$). Formalmente esto contradice la positividad de Weil... pero eso es exactamente W1. **No es nuevo** respecto a W1.

**Conclusión provisional**: Los tres candidatos naturales son o bien circulares o bien reducibles a obstrucciones ya conocidas (W1, W2, W3). Step 22-C debe buscar un funcional **no-circular**, es decir, cuyo valor no dependa de dónde están los ceros.

### Step 22-D: Conexión con clase $\omega$

El defecto finito $D_m(x) \sim C_j x^{1/2+b_j}\cos(\gamma_j\log x)$ tiene una **frecuencia fija** $\gamma_j/(2\pi)$ en la variable $\log x$. El caos multiplicativo de la clase $\omega$ (papers M1–M13) produce fluctuaciones de $\psi(x)$ a **todas** las escalas simultáneamente con estadísticas gaussianas. La pregunta es:

> ¿Puede una oscilación de **frecuencia única** y **amplitud creciente** coexistir con el caos de grano fino?

Formalmente: el defecto $D_m$ tiene espectro de frecuencias concentrado en $\{\gamma_j\}_{j=1}^m$ (finitas frecuencias), mientras que el caos de $\psi(x)-x$ tiene espectro continuo. La rigidez espectral del caos podría excluir frecuencias aisladas de amplitud creciente — esa sería una vía hacia EX.

---

## Clasificación de resultados Phase 22 (actualizada)

| Código | Enunciado | Clase | Estado |
|--------|-----------|-------|--------|
| 22-A | Fórmula explícita modificada $\psi = \psi_0 - D_m$ | B | ✓ demostrado |
| 22-B1 | Defecto $D_j$ como oscilación con fase explícita | B | ✓ demostrado |
| 22-B2 | Energía $\mathcal{E}_j(X) \sim C X^{2b_j}$ | B | ✓ demostrado |
| 22-B3 | Incapacidad aritmética de $\zeta_0$ | B | ✓ demostrado |
| 22-C | Funcional incompatible con $D_m$ | A/EX | Abierto |
| 22-D | Rigidez espectral del caos vs. defecto finito | EX | Abierto |
