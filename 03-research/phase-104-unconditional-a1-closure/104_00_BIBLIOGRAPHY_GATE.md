# 104_00 — Gate bibliográfico

**Rol:** bloqueante. Ningún mecanismo de Phase 104 se desarrolla sin veredicto aquí.

**Sustituye** a `03-research/phase-102-omega7-closure-campaign/102_BIBLIOGRAPHIC_GATE.md`, que tiene 54 líneas y él
mismo declara: *"A full external literature audit should compare this exact theorem by formula
and mechanism before any paper-level novelty claim is made."* Ese audit no se había hecho.

**Convención obligatoria.** Todo enunciado importado lleva etiqueta `[INC]` (incondicional) o
`[COND: RH]` / `[COND: GRH]`. Confundirlas es el error que este gate existe para impedir.

---

## 1. Hallazgo principal del gate

### Lagarias, *Li coefficients for automorphic L-functions*, `math/0404394` (Ann. Inst. Fourier 57 (2007) 1689)

Definición (ec. 1.14), **coeficiente de Li incompleto**:
\[
\lambda_n(T,\pi)=\sum_{\substack{\rho\in Z(\pi)\\ |\Im\rho|<T}}\Bigl[1-\Bigl(1-\frac1\rho\Bigr)^{n}\Bigr].
\]

Teorema 1.1, ec. (1.17), **tal como está impresa**:
\[
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)\,n-\lambda_n(\sqrt n,\pi)+O(\sqrt n\log n).
\]

Ec. (1.18) — **`[COND: RH para L(s,π)]`**:
\[
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)\,n+O(\sqrt n\log n).
\]

Ec. (1.13): \(C_1(\pi)=\frac N2(\gamma-1-\log 2\pi)+\frac12\log Q(\pi)\).
Para \(\zeta\) (\(\pi\) trivial, \(N=1\), \(Q=1\)): \(C_1=\frac12(\gamma-1-\log 2\pi)\).

Ec. (1.15), impresa:
\(S_f(n,\pi)=+\lambda_n(\sqrt n,\pi^\vee)+O(\sqrt n\log n)\).

### Erratum de signo vinculante

Las dos fórmulas anteriores no pueden importarse como teoremas en esa forma. En el punto
\(s_0=\rho-1\), el integrando de la prueba del Teorema 6.1 satisface

\[
\operatorname*{Res}_{s=s_0}
k_n(s)\left(-\frac{L'}L(s+1,\pi)\right)
=-m_\rho k_n(\rho-1),
\qquad
k_n(s)=\left(1+\frac1s\right)^n-1.
\]

El signo menos viene de \(-L'/L\). Al expandir el contorno pequeño antihorario al rectángulo
grande, la prueba impresa usa el signo contrario. Con la simetría de ceros que el artículo usa
para obtener (6.7), póngase

\[
\widehat I_2(n):={1\over2\pi i}\int_{C_2}F_n(s)\,ds.
\]

La fuente define \(I_2\) sin el factor \((2\pi i)^{-1}\), pero después lo usa como si estuviera
normalizado. Con la notación no ambigua anterior, el cálculo corregido da

\[
\widehat I_2(n)=S_f(n,\pi)+\lambda_n(T,\pi^\vee)+O(1),
\]

y la conclusión de contorno se repara como sigue. La elección impresa
\(T=\sqrt n+\varepsilon_n\) no justifica el decrecimiento geométrico de (6.12):
su razón disponible es \(e/2>1\). Tomando primero
\(T=2\sqrt n+\varepsilon_n\), la identidad exacta

\[
 {k_n(s+1)+1\over k_n(s)+1}
 =\left(1-{1\over(s+1)^2}\right)^n
\]

da la razón \(e^{1/4}/2<1\) contra el mayorante absoluto de la serie de
Dirichlet de \(L'/L\). Así
\(\widehat I_2(n)=O_\pi(\sqrt n\log n)\). La banda
\(\sqrt n\le|\gamma|\le2\sqrt n+1\) contiene
\(O_\pi(\sqrt n\log n)\) ceros y cada sumando de Li tiene módulo
\(\le1+e^{1/2}\), de modo que se vuelve al cutoff \(\sqrt n\) con el mismo
orden de error. Resulta

\[
\boxed{
S_f(n,\pi)=-\lambda_n(\sqrt n,\pi^\vee)+O_\pi(\sqrt n\log n).}
\tag{1.15c}
\]

Por la fórmula aritmética exacta
\(\lambda_n=S_\infty-S_f+\delta\), la versión corregida de (1.17) es

\[
\boxed{
\lambda_n(\pi)=\frac N2\,n\log n+C_1(\pi)n
+\lambda_n(\sqrt n,\pi)+O_\pi(\sqrt n\log n).}
\tag{1.17c}
\]

La fórmula condicional (1.18) no cambia. La auditoría completa de orientación, residuo y
simetría está en `104_02` §1. La búsqueda realizada el 25-jul-2026 en la ficha arXiv, la ficha
Numdam y los resultados enlazados desde ellas **no localizó un corrigendum**; (1.15c)–(1.17c)
son por tanto un erratum interno, no una corrección oficial atribuida al autor.

**Constante implícita — dato crítico.** En (1.15), (1.17) y (1.18) Lagarias repite:
*"where the implied constant in the O-notation depends on \(\pi\)"*. **No hay constante
efectiva.** Para \(\zeta\) es una constante absoluta fija pero desconocida. Bloquea cualquier
rango numérico certificado. Efectivizarla no es RH-strength, pero queda **diferida**: no
contribuye al cierre para todo \(n\), que es el objetivo de la fase.

**Rango con RH verificada — enunciado propio de Lagarias**, inmediatamente tras (1.16).
**Atención: las dos versiones difieren en un factor 2 y no deben fundirse.**

- **Publicada** (Ann. Inst. Fourier **57** (2007) 1689, p. 1694), verificada sobre el PDF:
  > *"Furthermore if the Riemann hypothesis holds up to height \(T\), then a bound of shape
  > (1.16) holds for all \(n\leqslant T^2/2(\log T)^2\), with the implied \(O\)-constant
  > depending on \(\pi\)."*
- **Fuente TeX de arXiv** `math/0404394`: mismo párrafo con \(T^2/4(\log T)^2\).

Se registra la versión publicada como texto principal y la fuente arXiv como variante. La
discusión corregida de lo que una altura verificada permite está en `104_02` §5.

El enunciado final usa la truncación **exactamente \(\sqrt n\)**. El factor
\(2\) anterior es solo el contorno auxiliar que repara el tramo horizontal;
se elimina mediante la estimación de la banda.

**Explosión sin RH — la referencia que hace falta.** Tras (1.18), p. 1694:
> *"If the Riemann hypothesis does not hold for \(L(s,\pi)\) then the incomplete Li coefficient
> term \(\lambda_n(\sqrt n,\pi)\) will sometimes be very large, of size exponential in \(n\).
> This fact was already observed for the Riemann zeta function in [4, Theorem 1 (c)]."*

[4] = **Bombieri–Lagarias**. Es el enunciado que se cita en §7; no se rehace a mano.

**Consecuencia corregida para nuestra normalización.** Nuestro bloque arquimediano cumple
(`main.tex:6856`)
\[
A_n=\frac n2(\log n+\gamma-1-\log 2\pi)+O(\log n),
\]
que coincide con \(\frac12 n\log n+C_1 n\) para \(\zeta\), salvo \(O(\log n)\). Definiendo

\[
\widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n),
\]

(1.17c) implica

\[
\boxed{\ A_n-\lambda_n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n,\quad
|\widetilde\varepsilon_n|\le C_*\sqrt n\log n\qquad[\mathrm{INC}]\ }
\tag{G1c}
\]

y como nuestra identidad exacta da \(\lambda_n=A_n-n-\mathcal J_n\) con
\(\mathcal J_n=\int_0^\infty E\,K_n\), se obtiene

\[
\boxed{\ \mathcal J_n+n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n
\qquad[\mathrm{INC}]\ }
\tag{G2c}
\]

La cantidad anterior
\(\varepsilon_n^-=A_n-\lambda_n-\lambda_n(\sqrt n)\) satisface
\(\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n)\). Por ello se **retira** la cota
incondicional \(|\varepsilon_n^-|\ll\sqrt n\log n\): no es una cuestión de efectivizar una
constante. La forma exacta corregida de A1 es

\[
\boxed{
\mathrm{A1}_\theta\iff
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\theta))
\le(1-\theta)A_n.}
\tag{G3c}
\]

En consecuencia, el bloque incompleto requiere una cota **inferior**, no superior.

Aquí solo se registra que **el control colectivo de los ceros de altura \(\gg\sqrt n\) ya está
resuelto en la literatura**, y que el obstáculo restante vive íntegramente en el bloque
incompleto.

**Chequeo de consistencia.** Bajo RH,
\(0\le\lambda_n(\sqrt n)\le4N(\sqrt n)\). El lado que ahora importa en (G3c) es la no
negatividad. Si RH falla, Bombieri–Lagarias muestra que el bloque incompleto tiene excursiones
exponenciales; una cota inferior uniforme del tamaño requerido sigue siendo RH-strength.

**Veredicto:** `no-duplica` para A1, **`duplica`** para la localización de la cola **y también
para el rango finito con altura verificada**.

Antes de incorporar este gate, las fases 1--103 tenían **cero ocurrencias** de "incomplete Li"
(búsqueda sobre `*.md`, `*.tex`, `*.py`), y `rmk:height-range` (`main.tex:6516`) planteaba el
control colectivo de \(\gamma>H\) como abierto
pidiendo "a zero-density input" — input que la versión corregida (1.17c) no necesita. Y el rango \(\approx10^{25}\) de
`main.tex:6531` se obtiene por **análisis de cero único**, no colectivo: ese es el defecto real.
Lagarias enuncia, desde 2007, un rango menor para una cota de forma (1.16)
—\(T^2/2(\log T)^2\approx5.5\times10^{21}\) en la versión publicada—, pero **el valor correcto
queda abierto**: la cuenta directa desde \(\sqrt n\le H\) sí alcanza \(n\le H^2\) para la cota
trivial, y hay además discrepancia editorial (registrada en `104_02` §5).

**Consecuencia para el plan:** el rango finito con altura verificada es terreno mayormente
bibliográfico y **no es el frente**. El frente es (G3c), con el signo corregido.

---

## 2. Ruta del punto de silla / Nörlund–Rice

### Mazhouda, *The saddle-point method and the Li coefficients*, `1506.01755` (Canad. Math. Bull.)

Abstract, textual: *"for any function F in the Selberg class S and **under the Generalized
Riemann Hypothesis**, we have λ_F(n)=…"*. Método: punto de silla + integrales de Nörlund–Rice
sobre los \(\lambda_F(n)\) generalizados de Omar–Mazhouda.

- Etiqueta: **`[COND: GRH]`**. No hay versión incondicional en el enunciado.
- **Solapamiento con `104_03`:** la representación de contorno
  \(S_n=\frac1{2\pi i}\oint R(t)(1+t)^n t^{-(n+1)}dt\) es de la misma familia (transformada
  binomial ↔ Nörlund–Rice). `104_03` debe deslindar explícitamente qué parte del contorno es
  incondicional en nuestro caso y qué parte, allí, se apoya en GRH.
- **Veredicto:** `adyacente`. La técnica está publicada; lo que no está es una conclusión
  incondicional. `104_03` se declara auditoría, no aporte.

---

## 3. Serie Voros

| ref | contenido | etiqueta |
|---|---|---|
| `1602.03292` — *Simplifications of the Keiper/Li approach to the RH* | simplificaciones del esquema | — |
| `1703.02844` — *Discretized Keiper/Li approach to the RH* | deforma \(\{\lambda_n\}\) a sucesiones explícitas, computadas hasta \(n=5\cdot10^5\) (Misguich); tests que "selectively react to zeros off the critical line", validados contra Davenport–Heilbronn | **no da resultado incondicional**; es marco de test computacional |
| `2204.01036` — *From asymptotic to closed forms…* | nueva sucesión en forma cerrada elemental que retiene la sensibilidad asintótica a RH; señala ceros violadores vía DH | **sin afirmaciones incondicionales en el abstract**; no prueba un criterio nuevo equivalente a RH, reformula el de Li |

**Punto que corrige al gate 102.** `102_BIBLIOGRAPHIC_GATE.md` advierte: *"Claims proving only
the asymptotic size of `lambda_n` do not close Omega7."* Es impreciso. Una cota **superior**
subexponencial sobre \(\lambda_n\) sí implica RH: un cuarteto fuera de la línea aporta
\(4-4\cosh(n\alpha)\cos(n\theta)\) con \(\alpha>0\), de amplitud exponencial en \(n\)
(`103_28`, `103_69`). Lo que no cierra nada es una cota **asintótica en el sentido de "orden de
magnitud"** sin uniformidad ni lado. La advertencia correcta es sobre **uniformidad y lado**, no
sobre "asintótico".

Aquí la normalización es la del coeficiente de Li. En una forma de Weil/autocorrelación
\(2\operatorname{Re}\lambda_n\), el mismo cuarteto aporta
\(8-8\cosh(n\alpha)\cos(n\theta)\).

**Veredicto:** `adyacente`. Las conclusiones de Voros **no se transfieren automáticamente a
A1**: sus sucesiones son deformaciones, no la nuestra, y su valor demostrado es diagnóstico.

---

## 4. Coffey

| ref | contenido | riesgo |
|---|---|---|
| `math/0402168` — *Effective method of computing Li's coefficients and their properties* | cómputo efectivo de \(\lambda_n\) | bajo |
| `math/0406312` — *An Explicit Formula Relating Stieltjes Constants and Li's Numbers* | relación explícita constantes de Stieltjes ↔ números de Li | **alto** para la forma escalar de `103_66` |

La forma escalar de `103_66` ec. (8) es
\(\sum_{j=0}^n\binom nj\frac{R^{(j)}(0)}{j!}\le\frac12\Delta A_n\), donde
\(R^{(j)}(0)/j!\) son polinomios explícitos en las constantes de Stieltjes. **Es exactamente el
tipo de objeto de `math/0406312`.**

**Veredicto:** `duplicación probable` de la *coordenada*, no necesariamente de la desigualdad.
Consecuencia operativa: la forma lcm/Stieltjes queda **degradada a auditoría**, no es frente
(consistente con la decisión del plan).

---

## 5. Espacio modelo / de Branges / medidas de Clark

### Suzuki, *On the Hilbert space derived from the Weil distribution*, `2301.00421`, Canad. J. Math., online 3-nov-2025, DOI 10.4153/S0008414X25101739

Completa \(C_c^\infty(\mathbb R)\) respecto de la forma hermitiana de la distribución de Weil
**bajo RH**, y prueba que ese espacio de Hilbert es isomorfo a un **espacio de de Branges** vía
Fourier compuesto con una aplicación simple; deduce nuevas condiciones equivalentes a RH.

- Etiqueta: **`[COND: RH]`** para la construcción del espacio.
- **Elimina la novedad** que se había atribuido a la ruta espacio-modelo / de Branges: el
  puente Weil ↔ espacio modelo ↔ de Branges está publicado.

**Sobre medidas de Aleksandrov–Clark.** La búsqueda no devuelve conexión Clark ↔ RH, y el repo
tiene cero ocurrencias de "Clark measure". Pero eso **no basta para declararla prometedora**:
la medida de Clark de \(\theta_n(s)=((s-1)/s)^n\) depende **solo de \(\theta_n\)**, no de
\(\zeta\), luego es universal y por sí sola no contiene aritmética alguna; además uno de los
nodos puede aparecer como masa en infinito.

**Veredicto:** `descartado como frente`. Se retoma solo si aparece un punto de entrada
aritmético concreto, y en ese caso el deslinde con Suzuki es obligatorio.

---

## 6. Altura verificada

### Platt–Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, `2004.09765`

RH verificada para \(|\gamma|\le H=3\times10^{12}\).

- Etiqueta: **`[INC]`** (es un teorema asistido por computadora, no condicional).
- **Uso admisible en Phase 104: únicamente verificación, corolario finito o prueba de
  consistencia** (`104_02` §5). La demostración uniforme de A1 para todo \(n\ge150\) no puede
  depender de él.
- **Escala: abierta, no corregida.** Coexisten \(H^2\) (cuenta directa desde \(\sqrt n\le H\),
  para la cota trivial \(\lambda_n(\sqrt n)\le4N(\sqrt n)\)), \(H^2/2(\log H)^2\) (Lagarias
  publicada) y \(H^2/4(\log H)^2\) (arXiv). Lo que sí está mal en `rmk:height-range`
  (`main.tex:6531`) es el **argumento**, que es de cero aislado. Ver `104_02` §5.

---

## 7. Fuentes admisibles, y el "competidor" por la misma ruta

### Política de fuentes (vinculante para toda la fase)

**Admisibles como fuente de un resultado:** arXiv, Zenodo, repositorios institucionales, y
revistas con revisión por pares.
**No admisibles como fuente de un resultado:** ResearchGate, Academia.edu, viXra y agregadores
similares — alojan preprints sin revisión ni control de versiones, y su tasa de error en este
tema concreto (pruebas reclamadas de RH) es alta. De ahí **no se importa ningún lema**.

**Distinción necesaria: admisibilidad ≠ prioridad.** Una fuente inadmisible como soporte de un
teorema **sigue contando como posible antecedente de prioridad**: si alguien publicó primero una
idea, el hecho no depende de dónde la alojó. Por tanto los textos inadmisibles **se registran,
se fechan y se comparan mecanismo a mecanismo**; lo único que no se hace es citarlos como
justificación de un paso.

### El texto en cuestión

**"On the Asymptotics of Li coefficients and Proof of the Riemann Hypothesis"**, feb-2026,
alojado **solo en ResearchGate** (publication 400430678). Sin versión en arXiv, Zenodo ni
preprints.org; sin revisión por pares. **Fuente no admisible** por la política de arriba.

Se conserva esta entrada por una única razón: ataca por **nuestra ruta exacta** (fórmula
explícita de \(\psi\) + polinomios de Laguerre) y reclama:
\[
\lambda_n=\frac n2(\log n-1+\gamma-\log 2\pi)+o(n)\quad(n\to\infty)
\ \Longrightarrow\ \text{RH por un teorema de Voros}.
\]

En la normalización de (G1c)–(G2c) eso equivale a afirmar \(\lambda_n(\sqrt n)=o(n)\)
**incondicionalmente** — precisamente el bloque incompleto que aquí está abierto.

**Estado del acceso:** `BLOQUEADO` (HTTP 403 a fetch anónimo) **y fuente no admisible**. Solo se
dispone del enunciado, vía indexación.

**Lo que sí se puede establecer sin el texto.** Su afirmación, traducida por (G1c), es
\[
\lambda_n(\sqrt n)=o(n)\qquad\text{incondicionalmente.}
\]

**Proposición (dicotomía).** *La afirmación del preprint es equivalente a RH; no es un paso
intermedio hacia ella.*

*Demostración.* (\(\Leftarrow\)) Bajo RH, cada par \(\{\rho,\bar\rho\}\) con \(|\gamma|<\sqrt n\)
aporta \(2-2\cos(n\theta_\rho)\in[0,4]\), luego
\(\lambda_n(\sqrt n)\le4N(\sqrt n)=O(\sqrt n\log n)=o(n)\).

(\(\Rightarrow\)) **Se cita Bombieri–Lagarias**, Thm 1(c), que es exactamente el enunciado
necesario: si RH falla, \(\lambda_n(\sqrt n)\) es *a veces* de tamaño **exponencial en \(n\)*.
El propio Lagarias lo señala tras (1.18):

> *"If the Riemann hypothesis does not hold for \(L(s,\pi)\) then the incomplete Li coefficient
> term \(\lambda_n(\sqrt n,\pi)\) will sometimes be very large, of size exponential in \(n\).
> This fact was already observed for the Riemann zeta function in [4, Theorem 1 (c)]."*
> — `math/0404394`, p. 1694; [4] = Bombieri–Lagarias.

Luego \(\lambda_n(\sqrt n)\ne o(n)\), contra la afirmación. \(\square\)

> **Corrección vinculante.** Una versión anterior de esta demostración argumentaba la dirección
> (\(\Rightarrow\)) diciendo que «los demás ceros son finitos en número y de frecuencias
> \(\theta\) fijas», de modo que no pueden cancelar el cuarteto ofensor. **Ese argumento es
> insuficiente:** la truncación \(\sqrt n\) **crece con \(n\)**, así que el conjunto de ceros que
> participan no es fijo — entran ceros nuevos indefinidamente. Controlar la cancelación entre un
> conjunto creciente de términos exponenciales es precisamente el contenido de Bombieri–Lagarias,
> y hay que citarlo, no rehacerlo a mano.

**Consecuencia operativa.** El preprint contiene RH o contiene un error; no hay tercera opción,
y ninguna parte de él puede importarse como lema. **Su valor para nosotros es exclusivamente
diagnóstico:** saber en qué línea concreta se rompe el argumento natural por la ruta
ψ-explícita + Laguerre —que es *nuestra* ruta— ahorra tiempo en `104_10`.

**Hipótesis sobre el punto de ruptura**, en orden de probabilidad, a contrastar cuando se
consiga el PDF:
1. Intercambio ilegítimo del límite \(n\to\infty\) con la suma sobre ceros (o con el regulador
   \(\varepsilon\downarrow0\)): es exactamente donde puede desaparecer una excursión
   exponencial de \(\lambda_n(\sqrt n)\).
2. Cota **puntual** sobre \(\psi(y)-y\) donde hace falta fase — déficit \(\Theta(n)\) de
   `rmk:pointwise-insufficient`.
3. Usar el signo impreso de (1.15)/(1.17) sin recalcular el residuo de \(-L'/L\), o importar
   (1.18) (`[COND: RH]`) como si fuera una estimación incondicional.

**Reclasificación — CERRADO.** Este ítem estaba marcado como **bloqueante para `104_10`**. Se
cierra por dos razones independientes: (a) la fuente no es admisible por la política de esta
sección, luego no puede ser antecedente ni deslinde de novedad; (b) la Proposición de arriba ya
fija sin ambigüedad, y sin necesidad del texto, qué debe probar cualquier argumento por esta
ruta — que es exactamente el muro de `104_02` §4. **`104_10` queda desbloqueado.**
Si apareciera una versión en arXiv o Zenodo, se reabre solo como diagnóstico.

Queda registrado como cambio de alcance respecto del plan aprobado, que lo listaba como
bloqueante.

---

## 8. Tabla de veredictos

| mecanismo Phase 104 | fuente comparada | veredicto |
|---|---|---|
| Reducción de A1 al bloque incompleto (`104_02`) | Lagarias `math/0404394`, §6, con erratum de signo interno | **duplica la localización de la cola**, pero las ecuaciones impresas (1.15)/(1.17) no son utilizables sin la corrección |
| Contorno binomial \(R(t)\) (`104_03`) | Mazhouda `1506.01755` `[COND: GRH]` | `adyacente` — auditoría, no aporte |
| Forma lcm / Stieltjes (`103_66`) | Coffey `math/0406312` | `duplicación probable` de la coordenada → **degradado a auditoría** |
| Espacio modelo / Clark | Suzuki `2301.00421` `[COND: RH]` | `descartado como frente` |
| Familia \(C_n^\theta\) (`104_01`) | — | **no-duplica** — el reparto A0/A1 con \(\theta\) libre no aparece en la literatura consultada |
| M1, núcleo colectivo \(w_{\max(i,j)}\) (`104_10`) | — | **no-duplica** — la identidad es de `103_67` (interna); la descomposición monótona/PSD no aparece ni en el repo ni en la literatura consultada |

---

## 9. Lo que este gate cambia en el plan

1. **`104_02` fija el erratum y el objetivo exacto corregido**:
   \[
   -\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\theta))
   \le(1-\theta)A_n.
   \]
   El frente es una cota inferior del bloque incompleto. Los antiguos Teorema A/A′ y B1/B2
   quedan retirados.
2. **`rmk:height-range` de `main.tex` necesita corrección**: el control
   colectivo de \(\gamma>H\) no requiere input de densidad, lo da la prueba de §6 con el signo
   corregido (1.17c); y su rango
   \(\approx10^{25}\) sale de un **análisis de cero único**, que es el defecto real. El rango
   publicado tiene discrepancia editorial, registrada en `104_02` §5.
3. **`102_BIBLIOGRAPHIC_GATE.md` §Warning necesita corrección**: el problema de una cota
   asintótica no es que sea asintótica, sino su lado y su uniformidad.
4. Dos rutas quedan cerradas antes de gastar esfuerzo: forma lcm/Stieltjes (Coffey) y espacio
   modelo/de Branges (Suzuki).

**Estado de bloqueo de `104_10`: DESBLOQUEADO.** El ítem del preprint (§7) está cerrado allí por
inadmisibilidad de fuente más la dicotomía vía Bombieri–Lagarias, y se mantiene registrado como
posible antecedente de prioridad. *(Una versión anterior de esta sección lo declaraba
bloqueante; contradecía a §7 y queda retirada.)*
