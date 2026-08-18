# 104_56B — Auditoría de antecedentes del criterio relajado en densidad

## Veredicto ejecutivo

La descomposición en modos exteriores dominantes y la conclusión
«si RH falla, hay coeficientes de Li exponencialmente negativos infinitas
veces» **no son nuevas**. Están en Bombieri--Lagarias y aparecen en forma
trigonométrica explícita, para coeficientes \(\tau\)-Li, en Bucur--Ernvall-
Hytönen--Odžak--Smajlović.

En la búsqueda dirigida descrita abajo no encontré en una fuente primaria
los refuerzos exactos

\[
 \neg\mathrm{RH}\Longrightarrow
 \{n:\lambda_n<0\}\text{ contiene un conjunto sindético de densidad positiva},
\tag{1}
\]

ni los criterios equivalentes

\[
\begin{aligned}
 \mathrm{RH}
 &\Longleftrightarrow
 4\lambda_n>A_n\text{ fuera de una excepción de densidad logarítmica cero},
 \tag{2}\\
 \mathrm{RH}
 &\Longleftrightarrow
 \text{existen bloques consecutivos de longitudes no acotadas donde }
 4\lambda_n>A_n.
 \tag{3}
\end{aligned}
\]

El nivel de novedad correcto es, por tanto:

> **refuerzo aparentemente no registrado de una prueba conocida**, obtenido
> al agregar recurrencia uniforme/equidistribución en el cierre compacto de
> la órbita al término dominante de Bombieri--Lagarias; no es una nueva cota
> analítica para los ceros ni una prueba de A1.

«No encontrado» no equivale a una prueba de prioridad. Antes de reclamar
novedad editorial haría falta una búsqueda bibliográfica profesional más
amplia y consulta a especialistas.

---

## 1. Antecedentes primarios exactos

### 1.1 Bombieri--Lagarias (1999)

E. Bombieri y J. C. Lagarias, *Complements to Li's criterion for the
Riemann hypothesis*, J. Number Theory **77** (1999), 274--287,
[DOI 10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392).

Su Teorema 1 da, para el multiconjunto abstracto admisible, la equivalencia
entre la localización \(\Re\rho\le1/2\), la positividad de todas las sumas de
Li orientadas y una cota inferior subexponencial para todos los grados. La
prueba aísla los puntos transformados de módulo exterior máximo y usa
aproximación diofántica simultánea. Si la localización falla, obtiene valores
negativos de tamaño exponencial **infinitas veces**. El artículo no enuncia
en su teorema una densidad natural/logarítmica de esos grados ni
sindeticidad.

### 1.2 Voros (2006)

A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*,
Math. Phys. Anal. Geom. **9** (2006), 53--63,
[arXiv:math/0506326](https://arxiv.org/abs/math/0506326),
[DOI 10.1007/s11040-005-9002-8](https://doi.org/10.1007/s11040-005-9002-8).

El resumen y la asintótica distinguen el crecimiento
\(n(A\log n+B)\) bajo RH del comportamiento oscilatorio no temperado si RH
es falsa. Esto antecede el diagnóstico «modo exterior exponencial», pero no
formula (1)--(3).

### 1.3 Bucur--Ernvall-Hytönen--Odžak--Smajlović (2016)

A. Bucur, A.-M. Ernvall-Hytönen, A. Odžak y L. Smajlović,
*On a Li-type criterion for zero-free regions of certain Dirichlet series
with real coefficients*, LMS J. Comput. Math. **19** (2016), 259--280,
[PDF de Cambridge](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9D6498CFDB802707E1A0EDFFE5B81C34/S1461157016000115a.pdf/on-a-li-type-criterion-for-zero-free-regions-of-certain-dirichlet-series-with-real-coefficients.pdf),
[DOI 10.1112/S1461157016000115](https://doi.org/10.1112/S1461157016000115).

Éste es el antecedente más cercano. Su ecuación (3.9), p. 266, exhibe para
los modos de módulo máximo un término de la forma

\[
 -2(1+m)^n\sum_{j=1}^k\cos(n\phi_j)
\tag{4}
\]

más términos de radio estrictamente menor y error polinómico. Inmediatamente
después aplican aproximación diofántica simultánea y concluyen que el
coeficiente es negativo, con amplitud exponencial, infinitas veces. En la
discusión de pp. 278--279 vuelven a describir el mismo mecanismo. El texto
no contiene los términos *density* ni *positive proportion* para el conjunto
de grados, y no enuncia sindeticidad ni (2)--(3).

### 1.4 Lagarias (2007), para la dirección bajo RH

J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst.
Fourier **57** (2007), 1689--1740,
[PDF Centre Mersenne](https://aif.centre-mersenne.org/item/10.5802/aif.2311.pdf),
[DOI 10.5802/aif.2311](https://doi.org/10.5802/aif.2311).

Bajo RH obtiene la asintótica

\[
 \lambda_n=A_n+O(\sqrt n\log n)
\tag{5}
\]

en la normalización de zeta usada por Phase 104. Como
\(A_n\sim\frac12n\log n\), (5) da \(4\lambda_n>A_n\) para todo grado
suficientemente grande. Esta es la dirección RH \(\Rightarrow\) (2),(3);
debe conservarse explícitamente la etiqueta **condicional a RH**.

---

## 2. Qué agrega exactamente 104_56

El input publicado tiene la forma

\[
 \lambda_n=-R^n F(n\alpha)
 +O\!\left(n^2R_1^n+n^2\right),
 \qquad 1<R_1<R,
\tag{6}
\]

donde \(F(x)=\sum_{j=1}^K\cos x_j\), después de absorber en el error los
términos constantes inofensivos. Sea

\[
 H=\overline{\{n\alpha:n\in\mathbb Z\}}\subset\mathbb T^K.
\tag{7}
\]

La traslación por \(\alpha\) es mínima y únicamente ergódica en el grupo
compacto monotético \(H\). Para un nivel regular
\(K/2<\eta<K\), el abierto

\[
 U_\eta=\{x\in H:F(x)>\eta\}
\tag{8}
\]

contiene el origen y tiene frontera de medida de Haar cero. Por tanto sus
tiempos de retorno

\[
 D_\eta=\{n:n\alpha\in U_\eta\}
\tag{9}
\]

tienen densidad natural \(\mu_H(U_\eta)>0\). La minimalidad más compacidad
da además que \(D_\eta\) es sindético. Sobre \(D_\eta\), (6) es negativo y
de tamaño \(\gg R^n\) a partir de un prefijo.

Así, el salto desde «infinitas veces» hasta «densidad positiva y conjunto
sindético» no usa información nueva sobre \(\zeta\). Usa una consecuencia
topológico-dinámica más fuerte de la misma suma trigonométrica finita.

La ausencia de una densidad universal \(\delta_0>0\) también es importante:
la familia de núcleos de Fejér de 104_56 muestra que, dentro de la clase
abstracta de Bombieri--Lagarias, la medida de los retornos que fuerzan signo
negativo puede tender a cero. Para la zeta fija existe algún
\(d_\zeta>0\) bajo \(\neg\mathrm{RH}\), pero no sale una constante numérica
universal de esos axiomas.

---

## 3. Auditoría interna del repositorio

El álgebra esencial ya estaba internamente:

* `phase-102/.../136_FINITE_EXTERIOR_SHELL_DOMINANCE.md` usa el cierre de la
  órbita en un toro y obtiene una subsucesión geométrica negativa;
* `phase-102/.../138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md` prueba que un cero de
  zeta fuera de la línea produce una capa exterior máxima finita;
* `phase-102/.../139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` ensambla esa
  discriminación del lado de ceros.

Esos documentos dicen «subsucesión infinita», no densidad positiva ni
sindeticidad. Por tanto la parte nueva interna de 104_56 es el refuerzo del
cuantificador y sus corolarios lógicos, no la capa exterior.

Hay que leer junto con esto:

* `257_AVERAGED_SLACK_POINTWISE_NO_GO.md`;
* `278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md`.

Ambos siguen siendo correctos para la obligación literal
«A1 en cada coordenada». Un teorema de densidad uno no prueba los índices
omitidos de A1. Lo nuevo es que puede **evitar esa obligación interna** y
cerrar RH directamente mediante (1). No debe afirmarse simultáneamente que
se ha probado A1 para todo \(n\).

---

## 4. Dos precauciones técnicas

1. La orientación dominante debe fijarse como
   \(u_\rho=\rho/(\rho-1)\) cuando se usa \(\lambda_{-n}=\lambda_n\).
   Mezclarla con \((\rho-1)/\rho\) invierte qué mitad del cuarteto es
   exterior.
2. Los criterios (2)--(3) solo necesitan el coeficiente completo
   \(\lambda_n\). La fórmula adicional de 104_56 para
   \(\lambda_n(\sqrt n)\) no fue localizada como enunciado publicado en esta
   auditoría y debe conservar su demostración propia; no es necesaria para
   la sindeticidad ni para los criterios relajados.

---

## 5. Alcance de la búsqueda

Se buscaron expresamente, hasta el 26 de julio de 2026, combinaciones de
*Li/Keiper coefficients* con *syndetic*, *positive density*, *natural
density*, *logarithmic density*, *density one* y *arbitrarily long blocks*
en arXiv, páginas de editoriales y repositorios matemáticos públicos. Tras
construir `104_61` se repitió la búsqueda con *Fermi--Dirac*, *logistic
partition*, *bounded nonlinear detector* y *degree partition*. Se
revisaron los textos primarios anteriores y las referencias cercanas que
aparecieron en esa búsqueda. No se usaron blogs ni manuscritos que reclaman
RH como antecedentes matemáticos.

**Clasificación final:**

| Afirmación | Estado bibliográfico |
|---|---|
| Capa exterior máxima y término trigonométrico exponencial | conocida |
| Negatividad exponencial infinitas veces si RH falla | conocida |
| Negatividad sobre un conjunto de densidad natural positiva | no encontrada explícitamente; corolario corto |
| Sindeticidad del conjunto forzante | no encontrada explícitamente; corolario corto |
| Criterio con excepción de densidad logarítmica cero | no encontrado explícitamente |
| Criterio por bloques buenos de longitud no acotada | no encontrado explícitamente |
| Detector Fermi acotado equivalente a RH | no encontrado; corolario funcional de la sindeticidad |
| Lift prima--Laguerre regulado del detector Fermi | no encontrado |
| Constante universal de densidad positiva | no válida en la clase BL abstracta |
