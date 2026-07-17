# Phase 24 — Cotas inferiores para $b_j$ y rigidez local del logaritmo de $|\zeta|$

**Fecha:** junio 2026
**Predecesora:** Phase 23 (barrera espectral, corrección de 23-A.6)
**Estado:** Activa

---

## 0. El cambio de pregunta

Hasta Phase 23, la pregunta era:

> ¿Produce un cero fuera de línea una contradicción observable?

La respuesta fue sistemáticamente negativa (Paley–Wiener, candidatos I/II/III, CMG estándar, función de estructura).

La **corrección de 23-A.6** cambió el panorama: la compatibilidad CMG no es uniforme en $b_j$. Hay tres regímenes:

| Régimen | Condición | Profundidad Hadamard | Mínimo CMG | ¿Compatible? |
|---------|-----------|---------------------|------------|--------------|
| I | $b_j \geq \gamma_j^{-C}$ | $O(C\log\gamma_j)$ | $O(-\log\gamma_j)$ | Sí |
| II | $b_j = e^{-\gamma_j^\alpha}$, $\alpha \in (0,1)$ | $\sim 2\gamma_j^\alpha \gg \log\gamma_j$ | $O(-\log\gamma_j)$ | Potencialmente no |
| III | $b_j \leq e^{-c\gamma_j}$ | $\sim 2c\gamma_j \gg \log\gamma_j$ | $O(-\log\gamma_j)$ | No (condicionalmente) |

La pregunta central de Phase 24 es:

$$\boxed{\text{¿Qué restricciones existen sobre la velocidad con que }b_j \to 0?}$$

---

## 1. Auditoría bibliográfica: lo que existe y lo que no

### 1.1 Lo que sí está bien establecido (cotas superiores sobre $b_j$)

**Región libre de ceros (Korobov–Vinogradov, 1958):**
$$b_j \leq \frac{1}{2} - \frac{c_0}{(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}.$$
Cota superior. Da la velocidad máxima de acercamiento de un cero a $\Re(s)=1$, no a $\Re(s)=1/2$.

**Región libre de ceros de Hadamard–de la Vallée-Poussin (1896):**
$$b_j \leq 1/2 - c/\log\gamma_j.$$
Más débil que KV. Aún sólo cota superior.

Ninguna de estas da información sobre cuán pequeño puede ser $b_j$.

### 1.2 Teoremas de densidad (estadísticos, no individuales)

Selberg, Ingham, Huxley, Montgomery, Jutila:
$$N(\sigma, T) \ll T^{A(1-\sigma)} (\log T)^B$$
donde $N(\sigma, T)$ es el número de ceros con $\Re(\rho) > \sigma$, $|Im(\rho)| \leq T$.

Estos controlan cuántos ceros pueden existir con $\Re(\rho) > 1/2 + \delta$ (son raros cuando $\delta \to 1/2$), pero no excluyen que exista un cero aislado con $b_j = e^{-10^{100}}$.

### 1.3 Resultados sobre proporción de ceros en la línea

Levinson (1974): al menos 1/3 de los ceros están en la línea.
Conrey (1989): al menos 2/5.
Bui–Conrey–Young (2011): al menos 41%.

Ninguno da información sobre la distancia de los ceros fuera de línea.

### 1.4 Repulsión de ceros (Deuring–Heilbronn)

Para funciones $L$ de Dirichlet: si $L(s,\chi)$ tiene un cero de Siegel $\beta = 1-\delta$ cerca de $\Re(s)=1$, repele otros ceros. Pero esto concierne ceros cerca de $\Re(s)=1$, no cerca de $\Re(s)=1/2$.

Para la función $\zeta$ misma: no hay fenómeno de repulsión conocido cerca de $\Re(s)=1/2$.

### 1.5 Correlación de pares (Montgomery, 1973)

La conjetura de correlación de pares predice que los ceros en la línea tienen estadísticas GUE. Esto describe la distribución de espaciados entre ceros en la línea crítica, no la posición de ceros fuera de línea.

### 1.6 Conclusión del auditoría

**No existe ningún resultado publicado de la forma $b_j \geq F(\gamma_j)$ para un cero fuera de línea individual.**

La pregunta "¿qué tan pequeño puede ser $b_j$ si RH es falsa?" parece estar genuinamente abierta en la literatura. Hay una razón conceptual: si alguien probara $b_j \geq \gamma_j^{-A}$ para todo $j$, automáticamente excluiría una familia enorme de escenarios de contraejemplo a RH, lo que sería un resultado mayor.

---

## 2. La cadena nueva: $b_j \to \delta\log|\zeta| \to$ CMG

Lo que sí es nuevo en el programa actual (y no aparece en la literatura clásica) es la cadena:

$$b_j \xrightarrow{\text{Hadamard}} \delta_j\log|\zeta(1/2+it)| \xrightarrow{\text{CMG}} \text{compatibilidad/incompatibilidad}$$

El paso de la derecha requiere, para ser riguroso:
1. Una cota **inferior** probada para $\min_{t \in [T,2T]} \log|\zeta(1/2+it)|$ (no disponible incondicionalmente).
2. O bien: una cota **inferior** para $b_j$ (Phase 24-A).
3. O bien: que el perfil local completo de $\log|\zeta|$ inducido por $\mathcal{O}_j$ sea incompatible con la geometría del campo log-correlacionado (Phase 24-B).

---

## 3. Estructura de Phase 24

### Phase 24-A: Teoría de cotas inferiores para $b_j$

**Pregunta central:** ¿Puede demostrarse alguna cota $b_j \geq F(\gamma_j)$ asumiendo que RH es falsa?

**Enfoques a explorar:**
- (24-A.1) Fórmula explícita: $\psi(x)-x$ contiene $x^{1/2+b_j}$; ¿puede la KV bound condicionar?
- (24-A.2) La identidad de Hadamard en $t=\gamma_j$: la evaluación de $\log|\zeta(1/2+i\gamma_j)|$ proviene del producto de todos los ceros; ¿puede acotarse desde abajo?
- (24-A.3) Momentos de $|\zeta|$: $\int_T^{2T}|\zeta(1/2+it)|^{2k}dt$ y la contribución de la órbita fuera de línea.
- (24-A.4) Identidades de van der Corput / estimaciones de suma exponencial.
- **Honestidad a priori:** mi expectativa es que no exista ninguna cota inferior, pero el diagnóstico preciso de por qué no existe es en sí mismo un resultado publicable.

### Phase 24-B: Perfil local universal de $\log|\zeta|$ inducido por $\mathcal{O}_j$

**La observación clave (nueva):**

No estudiar el valor puntual $\log|\zeta(1/2+i\gamma_j)|$, sino el perfil completo:
$$\ell_j(u) := \log|\zeta(1/2+i(\gamma_j + u b_j))|, \quad u = O(1).$$

El término de Hadamard de $\mathcal{O}_j$ en este perfil es:
$$\delta_j\ell_j(u) = \log(1+u^2) + O(1).$$

Esto es un perfil **universal** (independiente de $b_j$ y $\gamma_j$) con forma de "campana invertida" logarítmica. No es una fluctuación gaussiana.

**La pregunta:** ¿Es la geometría de este perfil incompatible con las correlaciones del campo log-correlacionado en una escala $b_j$ de separación?

### Phase 24-C: Compatibilidad CMG rigurosa

Usar los resultados probados sobre campos log-correlacionados:
- Arguin–Belius–Bourgade–Radziwiłł–Soundararajan (2019) sobre distribución del máximo de $\log|\zeta|$.
- Najnudel (2018), Paquette–Zeitouni (2018) sobre extremos.
- Harper (2013, 2020) sobre momentos de $|\zeta|$.

Determinar si alguno de estos implica una cota inferior para $\min_{t\in[T,2T]}\log|\zeta(1/2+it)|$ que sea rigurosa y suficientemente fuerte.

### Phase 24-D: Conexión con el programa $\omega$

El programa $\omega$-clase identificó la correspondencia $z = \beta^2$ (conexión M13.1 del programa de investigación). Estudiar si esta correspondencia, aplicada a un cero fuera de línea, produce restricciones sobre $b_j$ en el lenguaje de clases $\omega$.

---

## 4. Reglas de Phase 24

- No computación numérica.
- Solo definiciones, lemas, proposiciones, teoremas, demostraciones.
- Honestidad absoluta: si 24-A no produce ninguna cota inferior, documentar precisamente por qué no.
- Criterio de éxito: o bien $b_j \geq F(\gamma_j)$ (un resultado nuevo), o bien el diagnóstico preciso de por qué ningún argumento estándar puede dar tal cota.

---

## 5. Documentos de Phase 24

- `00-setup.md` — este documento
- `01-lower-bounds-bj.md` — Phase 24-A (cotas inferiores, auditoría de métodos)
- `02-local-profile.md` — Phase 24-B (perfil local $\ell_j(u)$ y geometría)
- `03-rigorous-chaos.md` — Phase 24-C (compatibilidad CMG rigurosa)
