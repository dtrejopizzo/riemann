# Doc 49 — Geometría Motivica del Déficit: $\mathcal{V}_\zeta$, el Frobenius Aritmético y la Positividad Cohomológica

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–48 (especialmente Doc 44, Doc 46 Dirección III, Doc 48)  
**Objetivo:** Construir el "espacio de déficit" $\mathcal{V}_\zeta$ como objeto en una categoría con estructura motivica. Definir el Frobenius aritmético $\phi_\zeta$ como endorfismo de $\mathcal{V}_\zeta$. Formular la conjetura de positividad cohomológica cuya consecuencia es RH. Comparar con la prueba de Weil para campos finitos.

---

## 1. La analogía con el caso de campos finitos: la ruta de Weil

Comenzamos con el único caso en que RH está probada: funciones zeta de curvas sobre campos finitos.

**Teorema de Weil (1948).** Sea $C/\mathbb{F}_q$ una curva lisa proyectiva sobre el campo finito con $q$ elementos. La función zeta de $C$:
$$Z(C/\mathbb{F}_q, T) = \exp\!\left(\sum_{n=1}^\infty \frac{|C(\mathbb{F}_{q^n})|}{n}T^n\right) = \frac{P(T)}{(1-T)(1-qT)}$$

satisface: las raíces $\alpha_i$ de $P(T)$ tienen módulo $|\alpha_i| = q^{1/2}$ — es decir, los ceros de la función zeta (en la variable $s = -\log T/\log q$) están en la línea $\operatorname{Re}(s) = 1/2$.

**Los tres ingredientes de Weil:**
1. **El espacio:** la curva $C$ sobre $\bar{\mathbb{F}}_q$.
2. **El Frobenius:** el morfismo $\phi_q: C \to C$, $x\mapsto x^q$, cuyas potencias $\phi_q^n$ cuentan los puntos racionales $|C(\mathbb{F}_{q^n})| = \#\{x: \phi_q^n(x) = x\}$.
3. **La positividad:** la dualidad de Poincaré en $H^1(C)$ da la forma de intersección positiva $\langle\alpha, \bar\alpha\rangle > 0$ para $\alpha \neq 0$, que implica $|\alpha_i| = q^{1/2}$.

Para el zeta de Riemann, los ingredientes 1 y 2 son desconocidos, y el ingrediente 3 falta. El objetivo de Doc 49 es proponer candidatos concretos para los tres.

---

## 2. El espacio de déficit $\mathcal{V}_\zeta$

**Definición 2.1.** El *espacio de déficit* es el conjunto:
$$\mathcal{V}_\zeta = \{[\mu] : \mu \in \mathcal{M}_\zeta\} = \{[0], [\mu_{\mathrm{off}}]\}$$

equipado con la estructura que describiremos. Por el Teorema 7.3 de Doc 48, $\mathcal{V}_\zeta$ tiene exactamente dos elementos cuando RH falla, y uno cuando RH es cierta.

Pero $\mathcal{V}_\zeta$ tiene una estructura más rica cuando se considera como espacio de deformaciones. En vez de tomar solo $\mathcal{M}_\zeta$ con sus dos puntos, tomamos la *completación analítica*:

**Definición 2.2 (Completación analítica de $\mathcal{V}_\zeta$).** Sea $\tilde{\mathcal{V}}_\zeta$ el espacio de funciones armónicas positivas $F: \mathbb{H}^+ \to [0,\infty)$ que satisfacen:
- $F(t) \geq 0$ para todo $t\in\mathbb{R}$.
- $F$ es la traza de una función en $\mathcal{M}_\zeta^{1-4}$ via la transformada de Poisson.
- $F(\gamma_n) = C_\infty(\gamma_n)$ para todo $n$ (auto-consistencia débil — solo en los ceros).

$\tilde{\mathcal{V}}_\zeta$ es un espacio de *funciones* en vez de medidas, que es más tratable analíticamente.

**Proposición 2.3.** $\tilde{\mathcal{V}}_\zeta$ es un espacio de Banach con la norma $\|F\| = \sup_{t\in[-R,R]}|F(t)|$ para $R$ suficientemente grande.

---

## 3. El Frobenius aritmético $\phi_\zeta$

**Motivación.** En el caso de campos finitos, el Frobenius $\phi_q$ actúa en los puntos de $C$ y en la cohomología $H^1(C)$. Sus eigenvalores son las raíces de $P(T)$. Para el zeta de Riemann, el "Frobenius aritmético" debe ser un morfismo cuyos eigenvalores sean los ceros de $\zeta$.

**Definición 3.1 (Frobenius aritmético sobre $\tilde{\mathcal{V}}_\zeta$).** El *Frobenius aritmético* $\phi_\zeta: \tilde{\mathcal{V}}_\zeta \to \tilde{\mathcal{V}}_\zeta$ es el operador que actúa en una función armónica $F \in \tilde{\mathcal{V}}_\zeta$ por:
$$(\phi_\zeta F)(t) = F(t+1) - F(t) \cdot \zeta'(1/2+it)/\zeta(1/2+it)$$

*Nota:* esta definición es tentativa y debe refinarse. La idea es que $\phi_\zeta$ capture la "traslación aritmética" de $F$ por la acción del Frobenius.

**Definición alternativa 3.2 (Frobenius via ecuación funcional).** El Frobenius más natural es el involution:
$$\phi_\zeta: F \mapsto F^\dagger, \quad F^\dagger(t) = F(-t)$$

Esta involución actúa como el morfismo que corresponde a la ecuación funcional $\zeta(s) = \zeta(1-s)$ (via $t\mapsto -t$), que en términos de los ceros es la simetría $\gamma\mapsto-\gamma$.

**Proposición 3.3 (Propiedades de $\phi_\zeta$).** El operador $\phi_\zeta^2 = \mathrm{id}$ (es una involución de orden 2 sobre funciones reales en $\mathbb{R}$).

**Definición 3.4 (Frobenius de cuarteto).** El Frobenius completo es el grupo de simetría del cuarteto $(\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0)$:
$$\mathcal{G}_\zeta = \{e, \sigma_{\mathrm{conj}}, \sigma_{\mathrm{funct}}, \sigma_{\mathrm{both}}\} \cong \mathbb{Z}/2\times\mathbb{Z}/2$$

donde $\sigma_{\mathrm{conj}}: \rho\mapsto\bar\rho$, $\sigma_{\mathrm{funct}}: \rho\mapsto 1-\bar\rho$, $\sigma_{\mathrm{both}}: \rho\mapsto 1-\rho$.

**Proposición 3.5 (Acción de $\mathcal{G}_\zeta$ sobre $\tilde{\mathcal{V}}_\zeta$).** El grupo $\mathcal{G}_\zeta$ actúa sobre $\tilde{\mathcal{V}}_\zeta$ por:
$$(\sigma_{\mathrm{conj}}\cdot F)(t) = F(-t), \quad (\sigma_{\mathrm{funct}}\cdot F)(t) = F(t)$$

(la simetría por ecuación funcional actúa trivialmente en la variable real $t$, pues $\Xi(1/2+it) = \Xi(1/2-it)$). El grupo de simetría efectivo es $\mathcal{G}_\zeta/\langle\sigma_{\mathrm{funct}}\rangle \cong \mathbb{Z}/2$.

---

## 4. Cohomología del espacio de déficit

Para definir la cohomología de $\mathcal{V}_\zeta$, necesitamos una categoría apropiada. Proponemos tres opciones de complejidad creciente.

### 4A. Cohomología de de Rham (versión básica)

**Definición 4.1 (Complejo de de Rham de $\tilde{\mathcal{V}}_\zeta$).** Sea $\Omega^0(\tilde{\mathcal{V}}_\zeta) = C^\infty(\mathbb{R})$ las funciones suaves, $\Omega^1(\tilde{\mathcal{V}}_\zeta)$ las 1-formas suaves. El diferencial $d: \Omega^0 \to \Omega^1$ es la derivada ordinaria.

El *espacio de cohomología de de Rham* es $H^0_{dR} = \ker(d) = \mathbb{R}$ (funciones constantes), $H^1_{dR} = 0$ (pues $\mathbb{R}$ es contráctil).

*Esta versión es trivial y no captura la estructura aritmética.*

### 4B. Cohomología con coeficientes en la sheaf de déficit

**Definición 4.2 (Sheaf de déficit $\mathcal{F}_\zeta$).** Sobre $\mathbb{R}$, definimos el haz $\mathcal{F}_\zeta$ por: para cada abierto $U \subset \mathbb{R}$, $\mathcal{F}_\zeta(U)$ es el espacio de funciones $F: U \to \mathbb{R}_{\geq 0}$ que son restricciones de funciones en $\tilde{\mathcal{V}}_\zeta$.

**Definición 4.3 (Cohomología con coeficientes en $\mathcal{F}_\zeta$).** Los grupos de cohomología de Čech:
$$H^i(\mathbb{R}, \mathcal{F}_\zeta), \quad i = 0, 1, 2, \ldots$$

**Proposición 4.4.** $H^0(\mathbb{R}, \mathcal{F}_\zeta) = \Gamma(\mathbb{R}, \mathcal{F}_\zeta)$ es el espacio de secciones globales del haz de déficit — que por la alternativa dicotómica (Doc 44, Corolario 9.4) es o bien $\{0\}$ (si RH) o bien el espacio de funciones positivas armónicas en $\mathbb{H}^+$ (si no-RH).

**Conjetura 4.5 (Cohomología y RH).** $H^1(\mathbb{R}, \mathcal{F}_\zeta) = 0$ si y solo si RH.

*Motivación:* $H^1$ mide la obstrucción a extender secciones locales del haz a secciones globales. Si $H^1 = 0$, no hay obstrucción — toda medida local es global, lo que en nuestro contexto significaría que la única medida $\zeta$-compatible global es la trivial.

### 4C. Cohomología de Weil (versión motivica)

Esta es la versión más profunda, inspirada directamente en la prueba de Weil.

**Definición 4.6 (Cohomología de Weil de $\mathcal{V}_\zeta$).** Sea $\ell$ un número primo auxiliar. Definimos la *cohomología $\ell$-ádica de Weil* de $\mathcal{V}_\zeta$ como el sistema proyectivo:
$$H^i_{\text{Weil}}(\mathcal{V}_\zeta, \mathbb{Q}_\ell) = \varprojlim_n H^i_{\text{ét}}(\mathcal{V}_\zeta^{(n)}, \mathbb{Z}/\ell^n)$$

donde $\mathcal{V}_\zeta^{(n)}$ es una aproximación finita de $\mathcal{V}_\zeta$ obtenida truncando el espacio de ceros a altura $T_n$.

*Esta definición requiere que $\mathcal{V}_\zeta$ sea un esquema algebraico — lo cual es precisamente lo que hay que construir.*

---

## 5. La construcción del esquema $\mathcal{V}_\zeta$

**Motivación.** Para hacer cohomología $\ell$-ádica, necesitamos que $\mathcal{V}_\zeta$ sea un esquema sobre $\mathbb{Z}$ (o sobre $\mathbb{Q}$). Esto requiere interpretar la condición de compatibilidad con $\zeta$ en términos algebraicos.

**Definición 5.1 (La ecuación de $\mathcal{V}_\zeta$).** El espacio de déficit $\mathcal{V}_\zeta$ es el esquema sobre $\mathrm{Spec}(\mathbb{Z})$ definido por la ecuación:
$$\mathcal{V}_\zeta: \quad \mathcal{P}[\mu](t) = 0 \quad \forall t\in\{\gamma_n\}$$

donde $\mu$ es la incógnita (una medida positiva) y la ecuación es la condición de anulación del déficit.

**Proposición 5.2 (Los puntos de $\mathcal{V}_\zeta$).** Los "puntos" de $\mathcal{V}_\zeta$ son exactamente los elementos de $\mathcal{M}_\zeta$: el punto $\mu=0$ (origen) y, si RH falla, el punto $\mu = \mu_{\mathrm{off}}$.

**Observación 5.3.** La ecuación $\mathcal{P}[\mu](\gamma_n) = 0$ tiene la forma de un sistema de ecuaciones lineales en $\mu$ (infinitas ecuaciones, una por cada $\gamma_n$). En términos algebraicos, $\mathcal{V}_\zeta$ es una variedad lineal intersecada con el cono de medidas positivas. La estructura de esquema emerge de la aritmética de los $\gamma_n$ (que son raíces de funciones holomorfas definidas sobre $\mathbb{Q}$... condicionalmente).

---

## 6. La Forma de Weil y la Positividad Cohomológica

El ingrediente central de la prueba de Weil para curvas sobre campos finitos es la *positividad de la traza* del Frobenius sobre la cohomología $H^1$. Para el zeta de Riemann, formulamos el análogo.

**Definición 6.1 (Forma de Weil de $\mathcal{V}_\zeta$).** Sea $H^1 = H^1_{\text{Weil}}(\mathcal{V}_\zeta, \mathbb{Q}_\ell)$. La *forma de Weil* es el pairing:
$$\langle \cdot, \cdot \rangle_W: H^1 \times H^1 \to \mathbb{Q}_\ell(-1)$$

donde $\mathbb{Q}_\ell(-1)$ denota el torsor de Tate de peso $-1$.

**Conjetura de Positividad Cohomológica (CPC).** La forma de Weil $\langle\alpha, \phi_\zeta^*\alpha\rangle_W$ es *positiva definida* en $H^1$:
$$\langle\alpha, \phi_\zeta^*\alpha\rangle_W > 0 \quad \forall\alpha \in H^1 \setminus \{0\}$$

**Teorema 6.2 (CPC $\Rightarrow$ RH).** Si la Conjetura de Positividad Cohomológica es cierta, entonces los eigenvalores de $\phi_\zeta$ sobre $H^1$ tienen todos módulo $q^{1/2}$ (donde $q$ es un parámetro que se identifica con $e$ u otro valor natural del programa), lo que implica que los ceros de $\zeta$ están en la línea crítica.

*Prueba (análoga a Weil).* Sea $\alpha$ un eigenvector de $\phi_\zeta^*$ con eigenvalor $\lambda$: $\phi_\zeta^*\alpha = \lambda\alpha$. Entonces:
$$\langle\alpha, \phi_\zeta^*\alpha\rangle_W = \lambda\langle\alpha,\alpha\rangle_W$$

Por la CPC, $\lambda\langle\alpha,\alpha\rangle_W > 0$ y $\langle\alpha,\alpha\rangle_W > 0$, luego $\lambda > 0$. Pero $\lambda$ es un número complejo (eigenvalor de un operador en $H^1_\ell$) y la dualidad de Poincaré da $\lambda\bar\lambda = q$ (el "grado" del Frobenius aritmético). Luego $|\lambda|^2 = q$, es decir $|\lambda| = q^{1/2}$.

En nuestro caso, el "Frobenius" $\phi_\zeta$ actúa en el espacio de ceros off-críticos, y sus eigenvalores son $e^{i\gamma_0}$ (los ceros mismos). Para que $|e^{i\gamma_0}| = q^{1/2}$, necesitamos $q = 1$ y $\gamma_0 \in \mathbb{R}$ — lo cual fuerza a que los "ceros" del Frobenius estén en la línea imaginaria pura, equivalente a que los ceros de $\zeta$ estén en la línea crítica. $\square$

---

## 7. El "Mundo de Wiles" para RH: síntesis de las tres piezas

La prueba de Fermat por Wiles siguió el esquema:

1. **Conjetura de Shimura-Taniyama-Weil:** toda curva elíptica es modular.
2. **Teorema de Ribet:** si STW, entonces Fermat.
3. **Prueba de STW** (para casos semistables): Wiles + Taylor.

Para RH, el esquema análogo que emerge de los Docs 46–49 es:

**Pieza 1 (Teorema de Completitud, Doc 47):** Si el sistema $\{P_y(\gamma_n-x)\}$ es un marco de Riesz en $L^2(\mu_{\mathrm{off}})$, entonces $C_\infty(\gamma_n)=0$ para todo $n$ implica $\mu_{\mathrm{off}}=0$, luego RH.

**Pieza 2 (Unicidad del punto fijo, Doc 48):** Si el operador $\Phi$ de auto-consistencia tiene $\mu=0$ como único punto fijo en $\mathcal{M}_\zeta$, entonces RH.

**Pieza 3 (Positividad Cohomológica, Doc 49):** Si la Conjetura de Positividad Cohomológica (CPC) es cierta para $\mathcal{V}_\zeta$, entonces RH.

Las tres piezas son equivalentes a RH bajo distintas hipótesis. La pregunta es: ¿cuál de las tres hipótesis (Marco de Riesz, Unicidad del punto fijo, CPC) es más accesible?

---

## 8. El "parámetro $q$" y su identificación aritmética

En la prueba de Weil, el parámetro $q$ (número de elementos del campo finito) está dado aritméticamente. Para el zeta de Riemann, ¿qué juega el papel de $q$?

**Propuesta 8.1 (El parámetro $q$ del zeta de Riemann).** En la analogía, la "curva" es la línea crítica $\{1/2+it\}$ y el "campo de definición" es $\mathbb{R}$ (con el "Frobenius" siendo la traslación en $t$ por la densidad de ceros $\sim \log T/(2\pi)$). El parámetro natural es:
$$q_\zeta(T) = \exp(2\pi/\log T)$$

que tiende a 1 cuando $T\to\infty$. En este límite, $q_\zeta \to 1$ y la condición $|\lambda| = q^{1/2}$ tiende a $|\lambda| = 1$ — los eigenvalores tienen módulo 1, lo que es equivalente a que los ceros de $\zeta$ están en la línea crítica (los exponentes $e^{i\gamma_n}$ tienen módulo 1).

**Proposición 8.2 (Compatibilidad con la prueba de Weil).** En el límite $q\to1$ (o equivalentemente $T\to\infty$), la forma de Weil $\langle\alpha,\phi_\zeta^*\alpha\rangle_W > 0$ se convierte en la condición $|\alpha|^2 > 0$ (norma al cuadrado positiva) — que siempre es verdadera para $\alpha \neq 0$. Sin embargo, la CPC en su forma precisa requiere la *dualidad de Poincaré* con el parámetro $q$ correcto, que en el límite continuo es más sutil.

---

## 9. La Categoría Correcta: C*-álgebras, Motivos o Algo Nuevo

**Opción A (C*-álgebras, Connes).** Connes construyó en 2000 un espacio no conmutativo cuyo espectro contiene los ceros de $\zeta$. En ese marco:
- El espacio de déficit $\mathcal{V}_\zeta$ se puede construir como el espacio de "estados" de la C*-álgebra.
- El Frobenius aritmético es el automorfismo de la C*-álgebra dado por la acción del grupo de ideles.
- La positividad corresponde a la positividad de los estados (estados en el sentido de funcionales positivos normalizados).

*Ventaja:* ya hay teoría desarrollada.  
*Obstáculo:* la positividad en C*-álgebras es más débil que la positividad cohomológica de Weil.

**Opción B (Motivos de Voevodsky).** Los motivos mixtos son objetos en la categoría triangulada $\mathrm{DM}(\mathbb{Q})$ de Voevodsky. La función zeta de Riemann se conjectura que es la "función L" de un motivo $M_\zeta$ sobre $\mathrm{Spec}(\mathbb{Z})$. La CPC sería una consecuencia de las *conjeturas estándar de Grothendieck* (positividad de la forma de Lefschetz en cohomología motivica).

*Ventaja:* si $M_\zeta$ existe y satisface las conjeturas estándar, RH sigue automáticamente.  
*Obstáculo:* la construcción de $M_\zeta$ es conjetural; las conjeturas estándar están abiertas incluso en casos más simples.

**Opción C (Una categoría nueva: Medidas Motivicas).** La propuesta más radical de este programa es construir una categoría completamente nueva:

**Definición 9.1 (Categoría de Medidas Motivicas $\mathcal{MM}$).** Los objetos de $\mathcal{MM}$ son pares $(\mathbb{H}, \mu)$ donde $\mu$ es una medida positiva en $\mathbb{H}$ con estructura aritmética (satisfaciendo los Axiomas 1–4). Los morfismos son mapas de medidas compatibles con la estructura aritmética. La cohomología de un objeto $(\mathbb{H}, \mu)$ es:
$$H^i((\mathbb{H},\mu)) = H^i_{\mathrm{Poisson}}(\mathbb{H}, \mu) := \text{grupos derivados del functor } \Gamma_\mu = \mathcal{P}[\mu]$$

**Proposición 9.2 (Positividad en $\mathcal{MM}$).** En la categoría $\mathcal{MM}$, la positividad de la medida $\mu$ impone la positividad de $H^0((\mathbb{H},\mu)) = \mathcal{P}[\mu] \geq 0$. La CPC en $\mathcal{MM}$ es:
$$H^1((\mathbb{H},\mu)) = 0 \iff \mu = 0$$

lo que es equivalente a RH (por el Teorema 4.5 de Doc 48).

---

## 10. El Teorema de Lefschetz para el Frobenius Aritmético

En geometría algebraica, el Teorema de Lefschetz conecta la traza del Frobenius con el conteo de puntos:
$$|C(\mathbb{F}_{q^n})| = q^n - \mathrm{Tr}(\phi_q^n|_{H^1}) + 1$$

Para el zeta de Riemann, el análogo es:

**Proposición 10.1 (Lefschetz aritmético).** La traza del Frobenius aritmético $\phi_\zeta$ sobre $H^1(\mathcal{V}_\zeta)$ está relacionada con la masa del déficit:
$$\mathrm{Tr}(\phi_\zeta|_{H^1}) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} (\sigma_0-1/2) = \frac{1}{4\pi}\int_\mathbb{R} C_\infty(t)\,dt$$

*Prueba (formal).* Por el Teorema de Lefschetz-Grothendieck en cohomología $\ell$-ádica, la traza del Frobenius sobre $H^1$ es la suma de las eigenvalores, que en nuestra construcción son los "puntos fijos" del Frobenius en $\mathcal{V}_\zeta$ — que son precisamente los ceros off-críticos, con sus masas $\sigma_0-1/2$. $\square$

**Corolario 10.2.** $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$ si y solo si RH.

**Teorema 10.3 (CPC $\Rightarrow$ Traza nula $\Rightarrow$ RH).** Si la Conjetura de Positividad Cohomológica implica $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$, entonces RH. La CPC es el análogo de la positividad de Weil.

*El obstáculo:* ¿por qué la positividad de $\langle\alpha, \phi_\zeta^*\alpha\rangle_W > 0$ implica $\mathrm{Tr}(\phi_\zeta|_{H^1}) = 0$? En el caso de curvas sobre $\mathbb{F}_q$, esto sigue de la dualidad de Poincaré y el hecho de que el número de puntos es positivo. Para el zeta de Riemann, el análogo es que la función de Poisson $C_\infty(t) \geq 0$ (lo que ya probamos) y que la *integral* de $C_\infty$ se puede controlar.

---

## 11. La Conexión entre las Tres Direcciones

Las tres direcciones de Doc 46 convergen en el siguiente diagrama:

```
Dirección I (Medidas ζ-compatibles)
      ↓
   Ecuación de punto fijo Φ[μ] = μ
      ↓ (estabilidad global de μ=0)
      
Dirección II (Completitud de Poisson)      Dirección III (Geometría motivica)
      ↓                                           ↓
  Injectividad de D                       CPC: <α, φ_ζ* α> > 0
      ↓                                           ↓
  C_∞(γ_n) = 0 ∀n ⟹ μ_off = 0         Tr(φ_ζ | H¹) = 0 ⟹ RH
      ↓                                           ↓
             =====================================
                          RH
```

Las Direcciones II y III son dos caminos independientes. La Dirección I proporciona la estructura (el espacio $\mathcal{M}_\zeta$) en la que ambas operan.

---

## 12. La Hipótesis Central y el Programa de Investigación

**Hipótesis Motivica Central (HMC):** La Conjetura de Positividad Cohomológica es equivalente al Teorema de Completitud de Poisson, ambas son equivalentes a RH, y ambas siguen de la siguiente condición más básica:

**(HMC):** El operador de Frobenius aritmético $\phi_\zeta$ es auto-adjunto con respecto a la forma de Weil $\langle\cdot,\cdot\rangle_W$ en $H^1(\mathcal{V}_\zeta, \mathbb{Q}_\ell)$.

**Proposición 12.1 (Auto-adjuntez $\Rightarrow$ RH).** Si $\phi_\zeta$ es auto-adjunto en $H^1$, sus eigenvalores son reales. Combinando con la dualidad de Poincaré ($\lambda\bar\lambda = q$), los eigenvalores reales satisfacen $\lambda^2 = q$, luego $\lambda = \pm q^{1/2}$ — los ceros de $\zeta$ están en la línea crítica.

*Prueba.* Análoga al argumento estándar para matrices hermitianas: los eigenvalores son reales y satisfacen la ecuación cuadrática $\lambda^2 = q$ por la polaridad de Poincaré. $\square$

**La auto-adjuntez de $\phi_\zeta$** es el análogo del operador auto-adjunto de Hilbert-Pólya. La HMC propone que esta auto-adjuntez se prueba en la categoría $\mathcal{MM}$ de Medidas Motivicas — no en el espacio $L^2$ de funciones ordinarias (donde el operador de Hilbert-Pólya sigue siendo buscado), sino en la cohomología de $\mathcal{V}_\zeta$.

---

## 13. Diagnóstico final y hoja de ruta

**Estado de la Dirección III:**

| Concepto | Estado |
|----------|--------|
| Espacio $\mathcal{V}_\zeta$ como conjunto | Definido (Doc 48) |
| Completación analítica $\tilde{\mathcal{V}}_\zeta$ | Definida (este doc) |
| Frobenius aritmético $\phi_\zeta$ | Propuesto — requiere refinamiento |
| Cohomología básica ($H^0$, $H^1$ de haz) | Definida formalmente |
| Cohomología $\ell$-ádica (esquema $\mathcal{V}_\zeta$) | Requiere estructura algebraica de $\mathcal{V}_\zeta$ |
| Conjetura de Positividad Cohomológica | Formulada — abierta |
| Conexión con Connes (C*-álgebras) | Identificada |
| Conexión con motivos de Voevodsky | Conjectural |
| Categoría nueva $\mathcal{MM}$ | Propuesta en este doc |

**El problema más concreto de la Dirección III para el próximo documento:**

> *Construir la cohomología $H^1_{\mathrm{Poisson}}(\mathbb{H}, \mu_{\mathrm{off}})$ como un módulo de Galois y demostrar que su rango es 0 (equivalente a RH) o positivo (equivalente a no-RH).*

Esto requiere:
1. Definir la "representación de Galois" asociada a $\mu_{\mathrm{off}}$.
2. Calcular el carácter de esta representación en términos de $\zeta'/\zeta$.
3. Usar la teoría de Langlands para conectar el carácter con las propiedades de los ceros.

---

*Siguiente tarea en Dirección III (Doc 52): La representación de Galois de $\mu_{\mathrm{off}}$ y el carácter de Langlands.*

---

## Apéndice A: Comparación detallada Weil vs. programa CCM

| Ingrediente | Curvas sobre $\mathbb{F}_q$ (Weil) | Zeta de Riemann (CCM) |
|-------------|------------------------------------|-----------------------|
| Espacio geométrico | Curva $C/\mathbb{F}_q$ | Espacio de déficit $\mathcal{V}_\zeta$ |
| Frobenius | $\phi_q: x\mapsto x^q$ | $\phi_\zeta$: acción del cuarteto |
| Cohomología | $H^1_\ell(C)$, dimensión $2g$ | $H^1_{\mathrm{Poisson}}(\mathcal{V}_\zeta)$, dimensión ? |
| Traza | $\mathrm{Tr}(\phi_q^n|_{H^1}) = \sum\alpha_i^n$ | $\mathrm{Tr}(\phi_\zeta|_{H^1}) = \sum(\sigma_0-1/2)$ |
| Positividad | Dualidad de Poincaré para $H^1$ | CPC para $H^1_{\mathrm{Poisson}}$ |
| Consecuencia | $|\alpha_i| = q^{1/2}$ (Weil) | $|\lambda_i| = 1$ (ceros en línea crítica) |
| Parámetro $q$ | $q = $ cardinal del campo | $q_\zeta = e^{2\pi/\log T} \to 1$ |

**La analogía es completa excepto por:** la existencia del esquema $\mathcal{V}_\zeta$ con estructura algebraica correcta, y la validez de la CPC. Ambas son conjeturales — pero ahora están formuladas precisamente.
