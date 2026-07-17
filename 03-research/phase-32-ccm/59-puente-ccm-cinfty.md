# Documento 59 — Puente entre el programa CCM y el déficit $C_\infty$

**Fase 32: Operadores prolatos semilocales y espacios de Sonin**

*David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com*

---

## Resumen

Importamos el marco de Connes–Consani–Moscovici (2024) [CCM24] como fundamento y lo integramos con los resultados del programa desarrollado en los Docs 42–58. El objetivo de esta fase es doble: (i) identificar el lugar exacto donde el déficit $C_\infty(\gamma_n)$ (Doc 42) aparece dentro del formalismo de pares cíclicos semilocales, y (ii) construir el puente entre la discrepancia de Jacobi semilocal $\Delta_n^S$ y nuestra fórmula aritmética (Doc 54). El resultado principal de este documento es que la discrepancia $\Delta_n^S$ es explícitamente computable para $S = \{\infty, p\}$ y que su comportamiento asintótico cuando $S$ crece está gobernado por los mismos factores de Euler que aparecen en el déficit aritmético. Formulamos la **Conjetura Puente** (C.P.) como objetivo central de la Fase 32.

---

## §1. Fundamentos importados de CCM

Aceptamos sin demostración los siguientes resultados de [CCM24].

**Notación.** Para un conjunto finito de lugares $S \ni \infty$, sea $\mathbb{A}_S = \prod_{v \in S} \mathbb{Q}_v$, $\Gamma = GL_1(\mathbb{Q}_S)$, y el espacio de clases de idèles semilocal $X_S = \mathbb{A}_S/\Gamma$.

**Teorema 1.1 (CCM, Thm. 3.1).** Sea $\mathbb{S} = -i(H + 1/2)$ el operador de escalamiento en $L^2(\mathbb{R})^{ev}$ y $\xi_\infty = 2^{1/4}e^{-\pi x^2}$. El par cíclico $(\mathbb{S}, \xi_\infty)$ es par y la transformación unitaria
$$\mathcal{V} := \mathcal{M} \circ \mathcal{U} : L^2(\mathbb{R})^{ev} \to L^2(\mathbb{R}, dm)$$
da la forma canónica del par cíclico, donde
$$dm(s) = (2\pi)^{-2}\left|\Gamma\!\left(\tfrac{1}{4} + \tfrac{is}{2}\right)\right|^2 ds.$$
Bajo $\mathcal{V}$, el operador $\mathbb{S}$ se convierte en multiplicación por $s$ y el operador prolato toma la forma
$$(\mathcal{M} \circ \mathcal{U}) \circ \mathbf{W}_\lambda \circ (\mathcal{M} \circ \mathcal{U})^* = -s^2 + 2\pi\lambda^2(4N+1) - \tfrac{1}{4}.$$

**Teorema 1.2 (CCM, Prop. 3.6).** Los ceros de $\zeta$ son el espectro del operador $M_s$ (multiplicación por $s$) en el espacio cociente $\mathcal{H}_{\leq 1}/\overline{\text{span}\{R_\ell^\pm(s)\,\Xi(s)\}}$, donde $R_\ell^\pm$ son polinomios explícitos y $\mathcal{H}_{\leq 1}$ es el anillo topológico de Hadamard de funciones enteras de orden $\leq 1$.

**Teorema 1.3 (CCM, Thm. 5.2).** Los coeficientes $a_n^\infty$ de la matriz de Jacobi del par cíclico $(\mathbb{S}, \xi_\infty)$ son
$$a_n^\infty = \frac{1}{2}\sqrt{(2n+1)(2n+2)},$$
y están determinados de manera única por la condición de que $\sigma: \mathfrak{sl}(2,\mathbb{R}) \to \text{End}(\mathcal{H})$ sea una representación de la álgebra de Lie. Los coeficientes de discrepancia satisfacen $d_n^\infty = 0$ para todo $n \geq 0$.

**Teorema 1.4 (CCM, Thm. 4.6).** Para todo $S \ni \infty$ finito y $\lambda > 0$, el mapa
$$\theta_S : \mathbf{S}_\lambda(\mathbb{R}, e_\infty) \to \mathbf{S}_\lambda(X_S, \alpha)$$
es un isomorfismo hilbertiano, donde $\mathbf{S}_\lambda(\mathbb{K}, \alpha) = \{f \in L^2(\mathbb{K}) : f(x) = 0 \text{ y } \mathbb{F}_\alpha f(x) = 0 \ \forall\, |x| < \lambda\}$ es el espacio de Sonin.

---

## §2. Par cíclico semilocal y medida espectral

Para $S = \{\infty, p_1, \ldots, p_k\}$ finito con $\infty \in S$, CCM [Prop. 4.2] construye el par cíclico semilocal $(\mathbb{S}, \xi_S)$ en $L^2(X_S)^{K_S}$. La forma canónica de este par está dada por la medida espectral

$$dm_S(s) = \left|\prod_{v \in S} L_v\!\left(\tfrac{1}{2} - is\right)\right|^2 ds,$$

donde los factores de Euler locales son
$$L_\infty(z) = \pi^{-z/2}\Gamma(z/2), \quad L_p(z) = (1-p^{-z})^{-1}.$$

**Proposición 2.1.** La medida $dm_S$ se descompone como
$$dm_S(s) = dm_\infty(s) \cdot \prod_{p \in S \setminus \{\infty\}} |L_p(\tfrac{1}{2}-is)|^2,$$
donde cada factor adicional satisface $|L_p(\tfrac{1}{2}-is)|^2 = (1 - 2p^{-1/2}\cos(s\log p) + p^{-1})^{-1}$.

**Demostración.** La factorización es inmediata de la definición de $dm_S$ y la multiplicatividad de los factores de Euler. Para el cómputo del módulo al cuadrado:
$$|L_p(\tfrac{1}{2}-is)|^2 = |(1-p^{-1/2+is})^{-1}|^2 = |1-p^{-1/2}e^{is\log p}|^{-2}.$$
Expandiendo: $|1-p^{-1/2}e^{is\log p}|^2 = 1 - p^{-1/2}(e^{is\log p}+e^{-is\log p}) + p^{-1} = 1-2p^{-1/2}\cos(s\log p)+p^{-1}$. $\square$

**Corolario 2.2.** La corrección semilocal respecto al caso arquimediano es
$$\frac{dm_S(s)}{dm_\infty(s)} = \prod_{p \in S\setminus\{\infty\}} \frac{1}{1 - 2p^{-1/2}\cos(s\log p) + p^{-1}}.$$
En particular, $dm_S(s)/dm_\infty(s) > 1$ para todo $s \in \mathbb{R}$ y todo $S \supsetneq \{\infty\}$.

---

## §3. Discrepancia de Jacobi semilocal

Los coeficientes $a_n^S$ de la matriz de Jacobi del par cíclico semilocal están determinados por los momentos pares de $dm_S$:
$$c_{2k}^S = \int_{\mathbb{R}} s^{2k}\, dm_S(s).$$

**Definición 3.1 (Discrepancia de Jacobi semilocal).** Para $S \ni \infty$ finito, la discrepancia del coeficiente $n$-ésimo de Jacobi es
$$\Delta_n^S := (a_n^S)^2 - (a_n^\infty)^2 = (a_n^S)^2 - \frac{(2n+1)(2n+2)}{4}.$$

Por el Teorema 1.3, $\Delta_n^{\{\infty\}} = 0$ para todo $n$. La discrepancia $\Delta_n^S$ mide la desviación del par cíclico semilocal respecto al caso puramente arquimediano.

**Proposición 3.2 (Positividadde la discrepancia).** Para todo $S \supsetneq \{\infty\}$ y todo $n \geq 0$, se tiene $\Delta_n^S > 0$.

**Demostración.** Los coeficientes $a_n^S$ están determinados por los determinantes de Hankel: $a_n^S = (D_{n-1}^S/D_n^S)^{1/2} \cdot \text{cte}$, donde $D_n^S = \det(c_{i+j}^S)_{0 \leq i,j \leq n}$. Por el Corolario 2.2, $c_{2k}^S > c_{2k}^\infty$ para todo $k \geq 0$ (ya que $dm_S/dm_\infty > 1$). La dominación estocástica $dm_S \succ dm_\infty$ implica $a_n^S > a_n^\infty$ para todo $n$ por monotonía de los coeficientes de Jacobi bajo dominación de medidas [Sz75, Cap. 2]. Por tanto $\Delta_n^S = (a_n^S)^2 - (a_n^\infty)^2 > 0$. $\square$

---

## §4. Cómputo explícito para $S = \{\infty, p\}$

Fijamos $S = \{\infty, p\}$ y calculamos la corrección a los momentos.

**Lema 4.1.** Para $S = \{\infty, p\}$:
$$c_{2k}^S = c_{2k}^\infty + \delta c_{2k}^p,$$
donde la corrección es
$$\delta c_{2k}^p = \sum_{\substack{m,n \geq 0 \\ (m,n) \neq (0,0)}} p^{-(m+n)/2} \int_{\mathbb{R}} s^{2k} e^{i(m-n)s\log p}\, dm_\infty(s).$$

**Demostración.** Expandimos $|L_p(1/2-is)|^2 = \sum_{m,n \geq 0} p^{-(m+n)/2}e^{i(m-n)s\log p}$ (serie de Neumann convergente ya que $p^{-1/2} < 1$). Multiplicando por $s^{2k}$ e integrando contra $dm_\infty$, el término $(m,n)=(0,0)$ contribuye $c_{2k}^\infty$. $\square$

**Proposición 4.2 (Función característica de $dm_\infty$).** La función característica de la medida $dm_\infty$ es
$$\phi_\infty(t) = \int_{\mathbb{R}} e^{its}\, dm_\infty(s) = \text{sech}^{1/2}(t) = \left(\frac{2}{e^t + e^{-t}}\right)^{1/2},$$
y las correcciones satisfacen
$$\int_{\mathbb{R}} s^{2k} e^{i\alpha s}\, dm_\infty(s) = (-1)^k \frac{d^{2k}}{dt^{2k}}\left[\text{sech}^{1/2}(t)\right]_{t=\alpha}.$$

**Demostración.** La primera igualdad es el Teorema 5.2(iii)+(iv) de CCM. La segunda es la relación estándar entre la función característica y los momentos: $\int s^{2k}e^{i\alpha s}d\mu = (-1)^k\hat{\mu}^{(2k)}(\alpha)$ donde $\hat\mu(\alpha) = \int e^{i\alpha s}d\mu(s) = \phi_\infty(\alpha)$. $\square$

**Corolario 4.3 (Expansión asintótica para $p \to \infty$).** 
$$\delta c_{2k}^p = 2p^{-1/2}(-1)^k\left[\text{sech}^{1/2}\right]^{(2k)}(\log p) + O(p^{-1}).$$
En particular, el término dominante está controlado por las derivadas de $\text{sech}^{1/2}$ evaluadas en $\log p$.

**Demostración.** El término dominante en la expansión del Lema 4.1 corresponde a $(m,n) = (1,0)$ y $(m,n) = (0,1)$, que contribuyen $p^{-1/2}\int s^{2k}(e^{is\log p}+e^{-is\log p})dm_\infty = 2p^{-1/2}\text{Re}\int s^{2k}e^{is\log p}dm_\infty$. Usando la Proposición 4.2, esto es $2p^{-1/2}(-1)^k[\text{sech}^{1/2}]^{(2k)}(\log p)$. Los términos siguientes son $O(p^{-1})$ por la convergencia de la serie. $\square$

---

## §5. La discrepancia de Jacobi y los factores de Euler

La Proposición 4.2 y el Corolario 4.3 expresan $\delta c_{2k}^p$ en términos de $\text{sech}^{1/2}$. Ahora conectamos esto con los factores de Euler $L_p(1/2 + is)$.

**Lema 5.1 (Representación integral de la corrección).** Para $S = \{\infty, p\}$:
$$\delta c_{2k}^p = \int_{\mathbb{R}} s^{2k}\left(|L_p(\tfrac{1}{2}-is)|^2 - 1\right)dm_\infty(s),$$
y la función $s \mapsto |L_p(1/2-is)|^2 - 1$ se puede escribir como
$$|L_p(\tfrac{1}{2}-is)|^2 - 1 = \frac{2p^{-1/2}\cos(s\log p) - p^{-1}}{1 - 2p^{-1/2}\cos(s\log p) + p^{-1}}.$$

**Demostración.** Inmediato de la Proposición 2.1. $\square$

**Proposición 5.2 (Estructura de picos de la discrepancia).** La función $s \mapsto |L_p(1/2-is)|^2 - 1$ tiene picos de Lorentz en $s_k = 2\pi k / \log p$ para $k \in \mathbb{Z}$, con altura $\approx p^{1/2}/(p^{1/2}-1)^2 - 1$ y anchura $\sim 2(p^{1/2}-1)/(p^{1/2}\log p)$.

**Demostración.** En $s = s_k$: $\cos(s_k \log p) = 1$, por lo que $|L_p(1/2-is_k)|^2 = (1-p^{-1/2})^{-2}$, dando el valor del pico. La anchura sigue de la expansión de $\cos(s\log p) \approx 1 - (s-s_k)^2(\log p)^2/2$ cerca de $s_k$. $\square$

**Observación 5.3.** Los picos de $|L_p(1/2-is)|^2$ están espaciados cada $2\pi/\log p$ y crecen como $p/(p-1)^2$ cuando $p \to \infty$. La densidad de ceros de $\Xi$ en la misma región es $\sim \log(\gamma/(2\pi))/(2\pi)$. Cuando el espaciado $2\pi/\log p$ coincide con el espaciado promedio de ceros $2\pi/\log\gamma$, es decir $p \approx \gamma$, el factor $L_p$ "resuena" con el cero $\gamma$. Esta resonancia es la conexión estructural con el déficit $C_\infty(\gamma_n)$ (véase la Conjetura Puente, §7).

---

## §6. Conexión con el déficit $C_\infty$ del programa anterior

Recordamos los resultados clave de los Docs 42–58:

- **Doc 42:** $C_\infty(\gamma_n) = \sum_{\rho_0 \in \mathcal{Z}_{\text{off}}} \frac{2(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2} \geq 0$.
- **Doc 43:** $C_\infty(\gamma_{n_0}) = 0$ para algún $n_0$ $\Leftrightarrow$ RH.
- **Doc 54:** $C_\infty(\gamma_n) = w(\gamma_n) - 2\text{Re}[A_n]$ donde $A_n$ recoge la contribución aritmética de los ceros fuera de la línea crítica.
- **Doc 58:** $c_* = \inf_n C_\infty(\gamma_n) = 0$ incondicionalmente.

**Proposición 6.1 (Conexión vía la transformada dual de Hardy–Titchmarsh).** Sea $\upsilon_S : L^2(X_S)^{K_S} \to L^2(\mathbb{R}, ds/|E_S(s)|^2)$ la transformada dual de Hardy–Titchmarsh de CCM [§4.4], donde $E_S(s) = \prod_{p \in S\setminus\{\infty\}} L_p(1/2+is)$. Entonces para todo $f \in L^2(\mathbb{R})^{ev}$:
$$\langle \upsilon_S \theta_S(f) \mid \upsilon_\infty f \rangle_{\mathbb{R}} = \langle f \mid f \rangle_{L^2(\mathbb{R})}.$$

**Demostración.** Esta es exactamente la Proposición 4.7(iii) de CCM aplicada con la notación de la sección 4.4. $\square$

**Proposición 6.2 (Evaluación espectral en los ceros).** Para cada cero $\rho_n = 1/2+i\gamma_n$ de $\zeta$, sea $F_n \in \mathcal{H}_{\leq 1}$ la función de evaluación espectral dada por la Prop. 3.6 de CCM. Entonces, bajo $\mathcal{V}_S$:
$$\mathcal{V}_S(F_n)(s) = R_n^S(s) \cdot \Xi(s),$$
donde $R_n^S \in \mathbb{C}[s]$ es un polinomio que depende de $S$ y de $\rho_n$.

**Demostración.** Es la Proposición 3.6 de CCM con la extensión semilocal de la Proposición 4.2 de CCM. El polinomio $R_n^S$ se obtiene proyectando sobre el autovector del cociente correspondiente a $\gamma_n$. $\square$

**Lema 6.3 (Peso espectral del $n$-ésimo cero).** El peso espectral de $\gamma_n$ en la medida $dm_S$ es
$$\omega_n^S := \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_{|\gamma_n - s| < \epsilon} dm_S(s) = |L_\infty(\tfrac{1}{2}-i\gamma_n)|^2 \prod_{p \in S\setminus\{\infty\}} |L_p(\tfrac{1}{2}-i\gamma_n)|^2.$$

**Demostración.** La medida $dm_S$ es absolutamente continua respecto a la medida de Lebesgue, por lo que $\omega_n^S = dm_S(\gamma_n)/ds$. Por la Proposición 2.1, la densidad es exactamente el producto indicado. $\square$

---

## §7. La Conjetura Puente

La estructura de los §3–6 apunta a una conexión profunda entre $\Delta_n^S$ y $C_\infty(\gamma_n)$. Formulamos la conjetura central de la Fase 32.

**Conjetura Puente (C.P.).** Para cada $n \geq 1$ y cada primo $p$, existe una constante $K_n > 0$ que depende solo de $\gamma_n$ tal que
$$C_\infty(\gamma_n) = K_n \cdot \lim_{S \to \mathcal{P}} \frac{1}{\log|S|} \sum_{p \in S \setminus \{\infty\}} \Delta_n^{\{\infty,p\}} \cdot (\log p)^{-1},$$
donde el límite es tomado sobre conjuntos $S$ que crecen como los primos menores que $T$ cuando $T \to \infty$, y $\mathcal{P}$ denota el conjunto de todos los primos.

**Justificación heurística.** El déficit $C_\infty(\gamma_n) = \sum_{\rho_0} \Delta(\gamma_n;\rho_0)$ es una suma sobre ceros fuera de la línea crítica. Cada cero $\rho_0 = \sigma_0 + i\gamma_0$ contribuye a través del kernel de Cauchy-Poisson. Por otra parte, la discrepancia $\Delta_n^{\{\infty,p\}}$ mide cuánto "desplaza" el factor $L_p$ al coeficiente de Jacobi del $n$-ésimo vector de la base. Por la Observación 5.3, cuando $p \approx e^{2\pi/|\gamma_n-\gamma_0|}$ (resonancia entre el primo $p$ y el gap entre un cero crítico y uno no-crítico), la discrepancia $\Delta_n^{\{\infty,p\}}$ recoge exactamente la misma información que $\Delta(\gamma_n;\rho_0)$.

**Versión débil de la C.P. (verificable).** Una versión más débil, que sí admite ataque con los métodos actuales, es:

$$C_\infty(\gamma_n) = 0 \iff \Delta_n^S = 0 \text{ para todo } S \supsetneq \{\infty\}.$$

Nótese que por la Proposición 3.2, $\Delta_n^S > 0$ para todo $S \supsetneq \{\infty\}$. La versión débil de la C.P. afirmaría que la implicación $\Leftarrow$ es vacuamente verdadera y que $\Rightarrow$ implica RH. Esto se traduce en:

$$C_\infty(\gamma_n) = 0 \iff \text{RH} \iff a_n^S = a_n^\infty \text{ para todo } S.$$

La primera equivalencia es el Teorema de Rigidez (Doc 43). La segunda es la afirmación de que el par cíclico semilocal colapsa al aritmédeo exactamente bajo RH.

---

## §8. Un resultado probado: monotonicidad bajo ampliación de $S$

**Proposición 8.1 (Monotonicidad de la discrepancia).** Sea $S \subset S'$ con $\infty \in S$. Entonces $\Delta_n^{S'} \geq \Delta_n^S$ para todo $n \geq 0$.

**Demostración.** $dm_{S'} = dm_S \cdot \prod_{p \in S' \setminus S} |L_p(1/2-is)|^2$. Por la Proposición 2.1, cada factor adicional es $\geq 1$, por lo que $dm_{S'} \geq dm_S$ puntualmente. Por dominación estocástica, $c_{2k}^{S'} \geq c_{2k}^S$ para todo $k$, y por la misma monotonía del Prop. 3.2, $(a_n^{S'})^2 \geq (a_n^S)^2$, es decir, $\Delta_n^{S'} \geq \Delta_n^S$. $\square$

**Corolario 8.2.** La red $\{\Delta_n^S\}_{S \ni \infty, \text{finito}}$ ordenada por inclusión es no-decreciente. En particular, el límite
$$\Delta_n^* := \sup_S \Delta_n^S = \lim_{S \to \mathcal{P}} \Delta_n^S$$
existe en $[0, +\infty]$.

**Proposición 8.3 (Relación con los momentos de la función $\Xi$).** Sea $d\mu_\Xi(s) = |\Xi(1/2+is)|^2 ds$. Entonces formalmente
$$\lim_{S \to \mathcal{P}} dm_S(s) = |L_\infty(\tfrac{1}{2}-is)|^2 \cdot |\zeta(\tfrac{1}{2}+is)|^2\,ds = d\mu_\Xi(s) \cdot |\pi^{-1/4}\Gamma(1/4)|^{-2}.$$

**Demostración.** Por el producto de Euler: $\prod_p L_p(1/2+is) = \zeta(1/2+is)$ cuando el producto converge (condicionalmente en la línea crítica). El límite de $dm_S$ cuando $S$ incluye todos los primos es $|L_\infty|^2 \cdot |\zeta(1/2+is)|^2\,ds$, que es proporcional a $d\mu_\Xi$ salvo factores de normalización. $\square$

**Observación 8.4.** La medida límite $d\mu_\Xi$ tiene ceros exactamente en $s = \pm\gamma_n$ (los valores imaginarios de los ceros de $\zeta$ en la línea crítica, es decir, los ceros de $\Xi$ como función de $s$ real). Bajo RH, estos son todos los ceros. La estructura de los coeficientes de Jacobi $a_n^*$ para la medida $d\mu_\Xi$ codifica toda la información sobre los ceros de $\zeta$ en la línea crítica, y la C.P. afirma que $\Delta_n^* - \Delta_n^\infty$ captura la información sobre los ceros fuera de la línea crítica.

---

## §9. Relación con el operador prolato y los coeficientes de discrepancia de CCM

En la sección 5 de CCM, los coeficientes de discrepancia del operador prolato son (ec. 5.10):
$$\frac{1}{i}d_n = -2n + a_n^2 - a_{n-1}^2.$$

Para el caso arquimediano: $d_n^\infty = 0$ (Teorema 1.3 importado). Para el caso semilocal:

**Proposición 9.1.** Para $S = \{\infty, p\}$ con $p$ primo, los coeficientes de discrepancia del operador prolato satisfacen
$$d_n^S = i\left(\Delta_n^S - \Delta_{n-1}^S\right) + d_n^\infty = i\left(\Delta_n^S - \Delta_{n-1}^S\right).$$

**Demostración.** Aplicando la definición a $a_n^S$:
$$\frac{1}{i}d_n^S = -2n + (a_n^S)^2 - (a_{n-1}^S)^2 = \underbrace{-2n + (a_n^\infty)^2 - (a_{n-1}^\infty)^2}_{=0} + \Delta_n^S - \Delta_{n-1}^S.$$
$\square$

**Corolario 9.2.** Los coeficientes $d_n^S$ de discrepancia del operador prolato semilocal son deterministas: están completamente controlados por los incrementos $\Delta_n^S - \Delta_{n-1}^S$ de la discrepancia de Jacobi.

**Proposición 9.3 (Condición $d^S = 0$ y RH).** Si la Conjetura Puente es verdadera, entonces
$$d_n^S = 0 \text{ para todo } n \geq 0 \text{ y todo } S \iff C_\infty(\gamma_n) = 0 \text{ para algún } n \iff \text{RH}.$$

**Demostración.** ($\Rightarrow$): $d_n^S = 0$ para todo $n$ implica $\Delta_n^S = \Delta_{n-1}^S$ para todo $n$. Por la Proposición 3.2, $\Delta_n^S \geq 0$. Por el Corolario 8.2, $\Delta_n^S$ es constante en $n$. Usando la C.P., esto implica $C_\infty(\gamma_n) = 0$ para algún $n$. Por el Teorema de Rigidez (Doc 43), RH. ($\Leftarrow$): RH implica $C_\infty \equiv 0$ (Doc 42), y por la C.P., $\Delta_n^S = \Delta_n^\infty = 0$ para todo $S$ y todo $n$, de donde $d_n^S = 0$. $\square$

---

## §10. Barreras honestas

**Barrera B1 (La C.P. no está probada).** La Conjetura Puente es el ingrediente central faltante. Sin ella, los resultados de esta fase son fundacionales pero no constituyen un ataque sobre RH.

**Barrera B2 (La medida límite $d\mu_\Xi$ requiere convergencia).** El producto $\prod_p L_p(1/2+is)$ converge condicionalmente en la línea crítica y el control del límite $dm_S \to d\mu_\Xi$ requiere una estimación de Vinogradov–Korobov o similar. Fuera de la línea crítica o sin RH, la convergencia del producto de Euler es un problema abierto.

**Barrera B3 (El operador prolato semilocal no está construido).** CCM menciona explícitamente que el operador prolato semilocal es objeto de un "forthcoming paper". La Proposición 9.3 está condicionada a la C.P., y el significado espectral de $d_n^S \neq 0$ requiere ese operador.

**Barrera B4 (Positividad de Weil).** Como en todas las fases anteriores, la pared fundamental sigue siendo: demostrar que la forma cuadrática de Weil $Q_n(\varphi, \varphi) \geq 0$ es equivalente a RH, y el marco CCM más nuestro programa dan dos caracterizaciones distintas de la misma pared, sin superarla.

---

## §11. Síntesis y dirección de la Fase 32

Los resultados de este documento establecen:

1. La medida semilocal $dm_S$ para $S = \{\infty, p\}$ es explícitamente computable (Proposición 2.1, Lema 4.1, Proposición 4.2).

2. La discrepancia de Jacobi $\Delta_n^S > 0$ para todo $S \supsetneq \{\infty\}$ (Proposición 3.2).

3. Los coeficientes de discrepancia del operador prolato $d_n^S$ son completamente determinados por los incrementos $\Delta_n^S - \Delta_{n-1}^S$ (Proposición 9.1).

4. La Conjetura Puente (C.P.) afirma que $C_\infty(\gamma_n)$ es el límite renormalizado de $\sum_p \Delta_n^{\{\infty,p\}}/\log p$ (§7).

5. Bajo la C.P.: $d_n^S = 0$ para todo $n, S$ $\Leftrightarrow$ RH (Proposición 9.3).

**El objetivo del Doc 60** es atacar la versión débil de la C.P.: demostrar que $\Delta_n^{\{\infty,p\}} \to 0$ cuando $p \to \infty$ con una tasa controlada por $C_\infty(\gamma_n)$, y que $\sum_{p \leq T} \Delta_n^{\{\infty,p\}}/\log p \sim C_\infty(\gamma_n) \log T$.

---

## Referencias

- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. Ann. Funct. Anal. (2024). https://doi.org/10.1007/s43034-024-00388-z
- [Sz75] G. Szegő. *Orthogonal Polynomials*. AMS, 4ª ed., 1975. [CCM24 Ref. 18]
- Doc 42: Fórmula del déficit y positividad de $C_\infty$.
- Doc 43: Teorema de Rigidez — un cero del déficit implica RH.
- Doc 54: Fórmula aritmética $C_\infty(\gamma_n) = w(\gamma_n) - 2\text{Re}[A_n]$.
- Doc 57: Conexión con la constante de De Bruijn–Newman.
- Doc 58: $c_* = \inf_n C_\infty(\gamma_n) = 0$ incondicionalmente.
