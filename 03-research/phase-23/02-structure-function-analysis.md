# Phase 23 — Step 23-B: Análisis de la función de estructura $S_2$

## El argumento central: cota inferior y superior

Definición (de Phase 22):
$$S_2(\tau, T) = \frac{1}{T}\int_0^T |X(t+\tau)-X(t)|^2\,dt, \qquad X(t) = \frac{\psi(e^t)-e^t}{e^{t/2}}$$

### Cota inferior (demostrada en Phase 22)

**Proposición 23-B.1** (Cota inferior bajo Hipótesis D). Para $\tau \neq 2\pi k/\gamma_j$ ($k \in \mathbb{Z}$):
$$S_2(\tau, T) \geq \frac{A_j^2(e^{2b_j T}-1)}{2b_j T} \sin^2(\gamma_j\tau/2) + O(e^{b_j T}/\sqrt{T})$$

donde $A_j = 2/|\rho_j^+|$. Asintóticamente $S_2(\tau,T) \gg e^{2b_j T}/T$.

*Demostración*. De la Proposición 22-D.2, el término dominante de $|X(t+\tau)-X(t)|^2$ es el cuadrado del defecto $|Y(t+\tau)-Y(t)|^2$ donde $Y(t) = D_m(e^t)/e^{t/2}$. El cálculo directo da la cota. $\square$

### Cota superior (desde el TNP de Korobov-Vinogradov)

**Proposición 23-B.2** (Cota superior incondicional). Por el teorema de los números primos incondicional (Korobov-Vinogradov), para todo $t > 0$:
$$|X(t)| = \frac{|\psi(e^t)-e^t|}{e^{t/2}} \leq C e^{t/2} \exp(-c_1\sqrt{t})$$

para constantes absolutas $c_1, C > 0$.

Por tanto:
$$S_2(\tau, T) \leq \frac{2}{T}\int_0^T (|X(t+\tau)|^2 + |X(t)|^2)\,dt \leq \frac{C}{T}\int_0^T e^t e^{-2c_1\sqrt{t}}\,dt$$

El integral: $\int_0^T e^t e^{-2c_1\sqrt{t}}\,dt \leq C_2 e^T e^{-2c_1\sqrt{T}}$ (dominado por el término $t=T$).

Por tanto:
$$S_2(\tau, T) \leq C_3 e^T e^{-2c_1\sqrt{T}}$$

*Demostración*. Estimación directa usando la cota de Korobov-Vinogradov en $|X(t)|$. $\square$

---

## Análisis de la compatibilidad

**Teorema 23-B.3** (Compatibilidad de las cotas). Las dos cotas son compatibles: la cota inferior bajo Hipótesis D no excede la cota superior incondicional.

Bajo Hipótesis D: $S_2(\tau,T) \gg e^{2b_j T}$.
Incondicional: $S_2(\tau,T) \leq C e^T e^{-c\sqrt{T}}$.

Para una contradicción se necesitaría: $e^{2b_j T} \gg e^T e^{-c\sqrt{T}}$, es decir $2b_j > 1 - c/\sqrt{T}$. Para $T$ grande: $2b_j \geq 1$, es decir $b_j \geq 1/2$. Pero $b_j = \sigma_j - 1/2 < 1/2$ siempre (pues $\sigma_j < 1$). **No hay contradicción.**

*Demostración*. Para cualquier $b_j \in (0, 1/2)$: $2b_j < 1$, así $e^{2b_j T} / (e^T e^{-c\sqrt{T}}) = e^{(2b_j-1)T+c\sqrt{T}} = e^{-(1-2b_j)T+c\sqrt{T}} \to 0$. Las cotas son compatibles. $\square$

**Observación**: Este teorema es el análogo preciso de la Proposición 22-C.5 (frontera de Paley-Wiener). Ambos establecen la misma conclusión: la frontera exacta de los métodos actuales es $b_j = 1/2$ (es decir $\sigma_j = 1$), que es imposible para ceros de $\zeta$.

---

## El espectro de $X_0(t)$ y su función de estructura

Para completar el cuadro, calculamos la función de estructura del componente en línea $X_0(t) = -2\operatorname{Re}\sum_{Z_{\rm CL}} x^\rho/\rho|_{x=e^t}$.

**Proposición 23-B.4** (Función de estructura de $X_0$). Bajo la hipótesis de que los ceros en línea satisfacen $\sum_\rho 1/|\rho|^2 < \infty$ (que se sigue de la distribución de ceros estándar):
$$\lim_{T\to\infty} S_2^{X_0}(\tau, T) = 8\sum_{\rho \in Z_{\rm CL}} \frac{\sin^2(\gamma\tau/2)}{|\rho|^2} < \infty$$

*Demostración*. $X_0(t) = -2\sum_\gamma |\rho|^{-1}\cos(\gamma t - \theta)$. La función de estructura:
$$S_2^{X_0}(\tau, T) = \frac{1}{T}\int_0^T |X_0(t+\tau)-X_0(t)|^2 dt$$
$$= \frac{16}{T}\sum_{\gamma,\gamma'} \frac{\sin(\gamma\tau/2)\sin(\gamma'\tau/2)}{|\rho||\rho'|} \int_0^T \sin(\gamma t)\sin(\gamma't) dt + O(1)$$

Los términos diagonales contribuyen $8\sin^2(\gamma\tau/2)/|\rho|^2$ (usando $\frac{1}{T}\int_0^T \sin^2(\gamma t)dt \to 1/2$). Los términos fuera de diagonal son $O(1/(T|\gamma-\gamma'|))$ que tienden a 0. La convergencia de $\sum_\rho 1/|\rho|^2$ garantiza que el límite existe y es finito. $\square$

**Corolario 23-B.5**: $S_2^{X_0}(\tau, T) = C_\tau + O(1/T)$ donde $C_\tau = 8\sum_\rho \sin^2(\gamma\tau/2)/|\rho|^2$ es una constante finita que depende de $\tau$.

**Consecuencia**: La función de estructura de la componente en línea $X_0$ es ACOTADA (converge a una constante). La divergencia exponencial de $S_2^X$ bajo Hipótesis D proviene ENTERAMENTE del defecto $D_m$.

---

## Resumen: las tres escalas del defecto

| Escala | Variable | Efecto del cero fuera de línea | Cota incondicional | ¿Contradicción? |
|--------|----------|-------------------------------|-------------------|-----------------|
| $x$ (conteo de primos) | $D_j(x) \asymp x^{1/2+b_j}$ | Crecimiento algebraico | $\psi-x = O(xe^{-c\sqrt{\log x}})$ | No ($b_j < 1/2$) |
| $t = \log x$ (función de estructura) | $S_2 \gg e^{2b_j T}$ | Crecimiento exponencial | $S_2 \leq Ce^T e^{-c\sqrt{T}}$ | No ($2b_j < 1$) |
| $t$ (alturas imaginarias de $\zeta$) | $\delta_j\log|\zeta| \sim 2\log b_j$ | Depresión local de profundidad $O(\log\log\gamma_j)$ | CMG: fluctuación $\sim (\log\log T)^{1/2}$ | No (compatible) |

**Conclusión del Step 23-B**: Las tres escalas son internamente consistentes y ninguna produce una contradicción.

---

## El obstáculo fundamental preciso

**Teorema 23-B.6** (Formulación precisa del obstáculo). Las siguientes tres afirmaciones son simultáneamente consistentes con los resultados conocidos:

1. $\zeta$ tiene un cero en $\sigma_j + i\gamma_j$ con $\sigma_j \in (1/2, 1)$.
2. $S_2(\tau, T) \gg e^{2b_j T}$ (divergencia exponencial de la función de estructura).
3. $S_2(\tau, T) \leq C e^T e^{-c\sqrt{T}}$ (cota superior de Korobov-Vinogradov).

Para obtener una contradicción entre (2) y (3) se necesita una cota $\psi(x)-x = o(x^{1/2+\varepsilon})$ para algún $\varepsilon < b_j$. Tal cota es equivalente a que no existen ceros con $\Re(\rho) > 1/2 + \varepsilon$. Esto es **circular**.

*Demostración*. (1)–(3) son compatibles como mostró el Teorema 23-B.3. Para contradecir (1)+(2) con (3), se necesita que $e^{2b_j T} \gg e^T e^{-c\sqrt{T}}$, que requiere $b_j > 1/2$, imposible. Alternativamente, una cota $\psi-x = O(x^{1/2+\varepsilon})$ con $\varepsilon < b_j$ daría $S_2 \leq C e^{(1+2\varepsilon)T/2}$ (en lugar de $e^T$), y para $\varepsilon < b_j$ esto contradiría (2). Pero tal cota es exactamente la no-existencia de zeros con $\Re(\rho) > 1/2+\varepsilon$. Circular. $\square$
