# Doc 152 — Ataque pureza ⟹ rigidez: las dos purezas, la pureza semi-global, y el intento «m<∞ + Λ≥0 + ecuación funcional ⟹ m=0»

**Programa:** Hipótesis de Riemann — Phase 48: AUDITORÍA Y PUREZA.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** atacar la mitad de rigidez **m<∞ ⟹ m=0** de la arquitectura
$\mathrm{RH}=(m<\infty)\wedge(m<\infty\Rightarrow m=0)$ (D-109), a la luz del hallazgo de Phase 47
(Doc 146): la repulsión es barata (la da el casi-Euler de Davenport–Heilbronn) y lo que falta es la
**pureza/positividad** que colapsa $m$ a 0. El encargo: (1) clarificar las dos purezas del programa
(local/global) y la discrepancia de peso; (2) proponer la pureza **semi-global** intermedia — lo que D–H
viola y ζ tiene; (3) intentar el teorema «$m<\infty$ + $\Lambda\ge0$ + ecuación funcional $\Rightarrow m=0$»
vía fórmula explícita/oscilaciones, con cada paso etiquetado; (4) localizar el fallo exacto y la hipótesis
mínima que lo salvaría, comparada con RH y con LP-112; (5) veredicto.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados
con precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con estatus honesto. **[GAP]** = declarado.
**[DESEO]** = declarado. **[GAP de literatura]** = dato no verificado al nivel de página esta sesión, NO
usado como premisa de ningún [TEOREMA]. Jamás se fabrica una prueba de RH ni de la rigidez.

**Prerrequisitos leídos en fuente esta sesión:** Doc 146 completo (repulsión barata / pureza cara; D–H
gorda, ceros con $\beta>1$); Doc 144 completo (LP-141, categoría D131-H⁺, Conjetura 144.D); Doc 131 §6
completo (Teorema 6.7 pureza local, test de Mertens de dos protuberancias, Prop. 6.5 masa diagonal,
Prop. 6.8 D–H por bloques, Deseo 6.9 = Conjetura H⁺); Doc 112 completo (LP-112, Teorema 2.3/5.1,
Prop. 2.6 densidad cero, Prop. 4.2 tautología de la fórmula explícita, Obs. 4.3 evaluadores externos);
Doc 135 §7.2 (puntos de ruptura B1–B4; B3 = desajuste de peso); Doc 137 (auditoría del borde
$|\alpha|=1$). ERRATA Phase 38 respetada: $W_\lambda\ge0$ está refutado y NO se usa.

---

## 0. Resumen ejecutivo

1. **(§1) Las dos purezas, clarificadas, y la discrepancia de peso resuelta en un enunciado.** La pureza
   local del Doc 131 (Teorema 6.7) es pureza **de peso 1**: $|\alpha|=\sqrt p$, divisor local en el
   **centro** $\mathrm{Re}=\tfrac12$, barrera $|c_m|\le 2p^{m/2}$. El factor local de ζ tiene $\alpha=1$:
   es **puro de peso 0** (divisor local en la **frontera** $\mathrm{Re}\in\{0,1\}$, órbita $\sigma$-libre)
   y, leído en la normalización de peso 1, es **maximalmente impuro** ($c_m=1+p^m>2p^{m/2}$ para todo
   $m\ge1$; el borde $|\alpha|=1$ auditado en Doc 137 mata H). La ecuación funcional global recentra los
   **pesos arquimedianos** (gamma, polo: el canje B1 del Doc 135) pero NO los ceros: **RH es el recentrado
   de los ceros del peso 0 al peso 1, la única pieza que la ecuación funcional no hace** (= B3 del Doc 135,
   ahora como enunciado de purezas).

2. **(§2) La pureza semi-global existe y tiene un teorema.** [DEFINICIÓN-NUEVA 152.1]: la **correlación
   gaussiana de primos** $S_T(\tau):=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$, el
   **peso de impureza** $\omega(\tau):=\limsup_T T^{-2}\log(2+|S_T(\tau)|)$ y el **espectro de impureza**.
   **[TEOREMA 152.2]** (incondicional, prueba completa): para $\tau\ge1$,
   $\omega(\tau)=\max\bigl(0,\max_{j:\,|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2)\bigr)$,
   donde $(\delta_j,\gamma_j)$ recorren los cuádruplos off de ζ; y en la altura exacta de un cuádruplo
   dominante el sesgo tiene **signo negativo forzado**:
   $S_T(\gamma_J)=-2\sqrt\pi\,m_J\,T\,e^{\delta_J^2T^2}(1+o(1))$. En frecuencia 0, $\omega(0)=\tfrac14$:
   **el polo es la impureza de peso $\tfrac14$ en frecuencia 0 — la masa diagonal**. Corolario:
   $\mathrm{RH}\iff\omega(\tau)=0$ para todo $\tau\ge1$ ⟺ *la interacción infinita de los primos crea
   exactamente una resonancia: el polo*.

3. **(§2.4–2.5) La jurisdicción exacta de $\Lambda\ge0$: la frontera, ni un epsilon más.**
   **[PROPOSICIÓN 152.4]**: $\Lambda\ge0\Rightarrow|S_T(\tau)|\le S_T(0)\asymp Te^{T^2/4}\Rightarrow
   \omega(\tau)\le\tfrac14$ para todo $\tau$ — *nada supera a la diagonal* (el avatar semi-global exacto de
   la barrera local $|c_m|\le2p^{m/2}$ y del test de Mertens del Doc 131). **[PROPOSICIÓN 152.5]** (prueba
   completa en el marco): con la desigualdad de Mertens $3+4\cos\theta+\cos2\theta\ge0$, la igualdad
   $\omega=\tfrac14$ solo la realiza el polo: no hay ceros con $\beta\ge1$. Es decir: **la positividad de
   von Mangoldt certifica exactamente la pureza de frontera (peso 0) y se agota ahí** — reproduce de la
   Vallée Poussin y no da un paso hacia el centro. Además **[PROPOSICIÓN 152.7]**: cada primo aislado y
   cada conjunto finito de primos es semi-globalmente puro ($\omega\equiv0$); la impureza —incluido el
   polo— es un fenómeno **irreduciblemente colectivo**, coherente con B1–B4 del Doc 135 (el muro vive en
   el límite, no en ningún paso finito).

4. **(§2.6) Lo que D–H viola, visiblemente y al máximo.** D–H tiene ceros con $\beta>1$ (Doc 146): su
   espectro de impureza espectral tiene pesos $>\tfrac14$ — **supera a su propia diagonal**, cosa que
   ningún dato de von Mangoldt $\ge0$ con abscisa 1 puede alimentar (**[PROPOSICIÓN 152.6]**). La pureza
   semi-global de peso $\le\tfrac14$ es exactamente la frontera que separa a ζ (teorema, vía $\Lambda\ge0$)
   de D–H (violada): el pedido (a)–(b) del encargo se cumple. El pedido (c) —que con $m<\infty$ implique
   $m=0$— es donde está el muro: §3.

5. **(§3) El intento «$m<\infty+\Lambda\ge0+$EF $\Rightarrow m=0$» se ejecuta hasta el final y falla en un
   punto único y nombrado.** Paso A [teorema]: bajo H(m), el cuádruplo dominante fuerza el sesgo exponencial
   negativo $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_J^2T^2}$ — la dominancia sobre los ceros on-line se
   consigue TOTALMENTE (e^{δ²T²} contra $O(\log\gamma_J)$) y el signo queda forzado. Paso B [proposición]:
   la única ley con signo que $\Lambda\ge0$ da es $|S_T(\tau)|\le S_T(0)$. Paso C [el choque]: la
   contradicción exige $\delta_J\ge\tfrac12$ — positividad refuta exactamente la frontera, ya excluida. El
   slack es $e^{-(1/4-\delta_J^2)T^2}$: **el mundo H(m) vive entero dentro del margen de Cauchy–Schwarz de
   la pureza de frontera.** Fallo localizado: **la positividad es información de frecuencia cero; el cero
   off es un evento de frecuencia $\gamma_J$; no existe puente de frecuencias sin RH** (coherente con el
   Cálculo 141.M4: la palanca de Landau es nula en la línea). La ruta de oscilaciones (Ingham/Pintz) falla
   con una inversión exacta: la positividad no impide la oscilación de $\psi(x)-x$ — es el **motor clásico
   que la demuestra** (teorema de oscilación de Landau, que REQUIERE integrando de un signo); el
   complemento que falta (cota superior $|\psi(x)-x|=O(x^{1/2+\delta_J-\epsilon})$) es la negación de la
   hipótesis: circularidad estructural.

6. **(§3.6, §4) La hipótesis mínima que salva, nombrada y medida.** [DEFINICIÓN-NUEVA 152.8] LP-152$(\tau_0)$:
   *$S_T(\tau_0)$ es subexponencial en $T^2$*. Por 152.2: LP-152$(\tau_0)$ ⟺ «ningún cuádruplo off con
   $|\gamma_j-\tau_0|<\delta_j$»; LP-152 en TODA frecuencia ⟺ RH; bajo H(m) la rigidez necesita LP-152 solo
   en las $m$ ventanas desconocidas. **[PROPOSICIÓN 152.9]**: la media de Besicovitch en $\tau$ de
   $|S_T(\tau)|^2$ es $O(T^2)$ — las frecuencias exponenciales, si existen, tienen densidad CERO en $\tau$:
   certificar LP-152 en la frecuencia mala es certificar un punto excepcional invisible a todo promedio —
   el cuantificador maestro de P43, en la coordenada **dual** a la de LP-112 (Doc 112 Prop. 2.6).
   LP-112 (existencial: producir UN $\tau$ bueno de un conjunto de densidad cero) y LP-152 (universal:
   excluir UNA frecuencia mala de un conjunto de densidad cero) son los dos brazos —réplica y evaluación—
   de la misma pinza, incomparables entre sí, ambos estrictamente más débiles que RH como instancias.

7. **VEREDICTO (§5): REDUCCIÓN NUEVA + MAPA-DEL-FALLO.** No hay teorema
   «$m<\infty+\Lambda\ge0+$EF$\Rightarrow m=0$» y este documento demuestra POR QUÉ esta ruta no puede
   darlo (tres puntos de fallo F1–F3, §3). Lo que sí queda: la mitad de rigidez tiene ahora una forma
   equivalente nueva y cuantizada — *bajo $m<\infty$, el espectro de impureza de ζ es un menú finito de
   parábolas con pesos $\delta_j^2\in(0,\tfrac14)$ y signo negativo forzado; rigidez ⟺ el menú es vacío* —
   y un objetivo dual de LP-112 (LP-152) con su certificado de excepcionalidad (152.9). La jerarquía de
   purezas queda medida: frontera ($\omega\le\tfrac14$, teorema, barata) ⊊ centro ($\omega=0$, RH); $m<\infty$
   no mueve $\omega$ ni un epsilon (la finitud protege argumentos internos, no evaluadores externos —
   Obs. 4.3 del D112, confirmada en la coordenada nueva).

---

## 1. Las dos purezas y la discrepancia de peso

### 1.1. Pureza local (recuerdo exacto, Doc 131)

El objeto de Euler de un primo $F_{p,\alpha}$ ($1<|\alpha|<p$; Doc 131 Prop. 6.6′) tiene divisor
$Z(\alpha)\sqcup Z(p/\bar\alpha)$ (dos progresiones verticales en $\mathrm{Re}=\log_p|\alpha|$ y
$1-\log_p|\alpha|$) y datos $c_m=\alpha^m+(p/\bar\alpha)^m$. El **Teorema 6.7** (pureza local): 

$$F_{p,\alpha}\ \text{satisface H}\iff|\alpha|=\sqrt p\iff|c_m|\le2p^{m/2}\ \forall m\ge1.$$

La positividad de Weil local es **decidible** y equivale a que el divisor caiga en el centro
$\mathrm{Re}=\tfrac12$. El mecanismo de la dirección negativa es el test de Mertens de dos protuberancias
(masa diagonal en $1$ contra coeficiente en $p^M$ con fase adversaria), con barrera exacta
$|c_M|\le2p^{M/2}$ — Cauchy–Schwarz justo en el caso puro.

**Lectura de pesos.** Llamo **pureza de peso $w$** al caso $|\alpha|=p^{w/2}$: el divisor local vive en
$\mathrm{Re}=\tfrac w2$ y (por $\sigma$-estabilidad, vía la pareja $p/\bar\alpha$) en $\mathrm{Re}=1-\tfrac w2$.
Para $w=1$ las dos rectas coinciden en el **centro** $\tfrac12$: el divisor es $\sigma$-fijo punto a punto
(autodual). Para $w=0$ son la **frontera** $\{0,1\}$: una órbita $\sigma$-libre. El Teorema 6.7 es el caso
$w=1$; los objetos del teorema de dos primos (Doc 135, Teorema A) son puros de peso 1.

### 1.2. El factor de ζ es puro de peso 0 e impuro de peso 1 — la discrepancia

El dato local de ζ es $a(p^m)=\Lambda(p^m)=\log p$; el factor local es $(1-p^{-s})^{-1}$, es decir
$\alpha=1$. Hechos exactos (Doc 135 §7.2 B3; Doc 137 auditoría del borde):

- $|\alpha|=1=p^{0/2}$: el factor de ζ es **puro de peso 0**. Su divisor local (la retícula
  $Z(1)\sqcup Z(p)$) vive en $\mathrm{Re}\in\{0,1\}$ — la frontera de la banda, órbita libre de
  $\sigma:s\mapsto1-\bar s$.
- Leído en la normalización de peso 1 del Doc 131, $c_m=1+p^m$ y $1+p^m>2p^{m/2}$ para todo $m\ge1$
  (AM–GM estricta): **violación maximal de la barrera de Ramanujan de peso 1**. El borde $|\alpha|=1$ fue
  auditado en el Doc 137: el test de dos protuberancias mata H también ahí ($\delta'=\pm\tfrac12$ tras el
  swap). **Cada factor de ζ, aislado, viola la positividad de Weil de peso 1.**
- Los objetos puros del programa (dos primos, $n$ primos: Doc 135) tienen término aritmético
  *constructivo*; ζ vive en el régimen *destructivo* ($a=\Lambda\ge0$ restando contra el bloque polar).
  El desajuste constructivo/destructivo es la sombra del desajuste de peso (B3).

**La discrepancia, en un enunciado.** La ecuación funcional de ζ realiza el recentrado $0\to\tfrac12$ en
los **pesos arquimedianos** (el polo $[0]+[1]$, el factor gamma, el canje
$\theta(y)\leftrightarrow\Omega(t)$ de B1) — por eso el divisor GLOBAL es $\sigma$-estable respecto del
centro. Pero $\sigma$-estable no es $\sigma$-fijo: la ecuación funcional empareja $\rho$ con $1-\bar\rho$,
no obliga $\rho=1-\bar\rho$. **RH es el recentrado de los CEROS: que el divisor global, fabricado con
datos locales puros de peso 0 (frontera), sea puro de peso 1 (centro). Esa es la pieza que la ecuación
funcional no hace y que ninguna pureza local puede hacer (los factores son individualmente impuros de
peso 1).** La "pureza global" $m=0$ no es la agregación de las purezas locales: es una propiedad de la
**interacción** — exactamente la intuición que la pureza semi-global de §2 formaliza.

### 1.3. Lo que la pureza de frontera certifica globalmente

La pureza de peso 0 de los factores tiene una manifestación global clásica e incondicional: ζ no se anula
en $\mathrm{Re}\,s\ge1$ (Euler para $\sigma>1$; de la Vallée Poussin/Mertens para $\sigma=1$ [dVP96],
[Mer98]), y por la ecuación funcional tampoco en $\mathrm{Re}\,s\le0$ (salvo triviales). Es decir: **los
ceros globales son repelidos de la frontera — la posición del divisor local puro de peso 0.** La sección
§2.4–2.5 mostrará que esto es EXACTAMENTE lo que la positividad $\Lambda\ge0$ certifica en el marco
semi-global ($\omega\le\tfrac14$, con igualdad solo en el polo), y que ahí se agota. La tabla de purezas
del programa queda:

| pureza | enunciado | posición del divisor | estatus |
|---|---|---|---|
| local de peso 0 | $\vert\alpha_p\vert=1$ para cada $p$ | frontera local $\{0,1\}$ | **trivialmente cierta para ζ** |
| de frontera (global) | sin ceros en $\mathrm{Re}\ge1$ ∪ $\mathrm{Re}\le0$ | repulsión de la frontera | **teorema** (dVP; §2.5 en el marco) |
| semi-global | $\omega(\tau)=0$ $\forall\tau\ge1$ (§2) | sin resonancias salvo el polo | **⟺ RH** (Cor. 152.3) |
| global de peso 1 | $m=0$: divisor $\sigma$-fijo (centro) | centro $\tfrac12$ | RH |

---

## 2. Pureza semi-global: la definición y el teorema del espectro de impureza

### 2.1. La definición

**[DEFINICIÓN-NUEVA 152.1] (correlación gaussiana, peso de impureza, espectro de impureza).** Para
$\tau\in\mathbb R$ y $T\ge1$:
$$S_T(\tau)\;:=\;\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,e^{-(\log n)^2/4T^2}\,\cos(\tau\log n)$$
(absolutamente convergente: la gaussiana mata la cola). El **peso de impureza** en la frecuencia $\tau$:
$$\omega(\tau)\;:=\;\limsup_{T\to\infty}\;\frac{\log\bigl(2+|S_T(\tau)|\bigr)}{T^2}\;\in\;[0,\infty],$$
y el **espectro de impureza** $\Sigma_{\mathrm{imp}}:=\{\tau\ge0:\omega(\tau)>0\}$. Digo que ζ es
**semi-globalmente pura en $\tau$** (PSG$(\tau)$) si $\omega(\tau)=0$, i.e. si los primos no esconden
ninguna correlación exponencial (en $T^2$) con la fase $\cos(\tau\log n)$ a escala gaussiana $T$.

**Por qué esta es la noción de "pureza de la interacción".** $S_T(\tau)$ involucra TODOS los primos a la
vez: es la transformada de Fourier (en $\tau$) de la medida positiva
$\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\delta_{\log n}$ — el dato de von Mangoldt completo, pesado
en la línea crítica. La Prop. 152.7 mostrará que ningún primo aislado ni conjunto finito de primos puede
producir $\omega>0$: la impureza semi-global, si existe, es un fenómeno de la interacción infinita.
La definición es el avatar global exacto del dato local del Doc 131: allí la impureza de $F_{p,\alpha}$
se detecta en los coeficientes $c_m$ a soporte $m\gtrsim1/\delta'$ (barrera $|c_m|\le2p^{m/2}$, diccionario
M3 del D134 §5.8); aquí se detecta en $S_T(\tau)$ a soporte $T\gtrsim1/\delta$ (Cor. 152.3(iii)).

### 2.2. El teorema del espectro de impureza

**Convención de fórmula explícita.** Uso la fórmula explícita de Weil–Guinand en la normalización de
[IK04, Thm. 5.12] para ζ: para $h$ par, holomorfa en $|\mathrm{Im}\,t|\le\tfrac12+\epsilon$, con
decaimiento $h(t)\ll(1+|t|)^{-2-\epsilon}$ en la banda,
$$\sum_{\rho}h(t_\rho)\;=\;h\bigl(\tfrac i2\bigr)+h\bigl(-\tfrac i2\bigr)
+\frac1{2\pi}\int_{\mathbb R}h(t)\,\Omega_\infty(t)\,dt
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),$$
donde $\rho=\beta+i\gamma$ recorre los ceros no triviales, $t_\rho:=(\rho-\tfrac12)/i$ (de modo que
$\rho=\tfrac12+\delta+i\gamma\mapsto t_\rho=\gamma-i\delta$), $g(u)=\tfrac1{2\pi}\int h(t)e^{-iut}dt$, y
$\Omega_\infty(t)=\mathrm{Re}\,\frac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{it}2)-\log\pi=O(\log(2+|t|))$.
[Las constantes absolutas se arrastran simbólicamente; lo load-bearing del teorema —tasas exponenciales y
signos— es robusto frente a la convención.]

**Test gaussiano.** $h_{T,\tau}(t):=e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}$ (par, entera; en
$|\mathrm{Im}\,t|\le1$, $|h|\le e^{T^2}\bigl(e^{-T^2(\mathrm{Re}\,t-\tau)^2}+e^{-T^2(\mathrm{Re}\,t+\tau)^2}\bigr)$:
admisible con margen). Su transformada: $g(u)=\frac1{\sqrt\pi\,T}e^{-u^2/4T^2}\cos(\tau u)$. La fórmula
queda, exactamente:
$$\boxed{\;\frac{2}{\sqrt\pi\,T}\,S_T(\tau)\;=\;-\sum_\rho h_{T,\tau}(t_\rho)\;+\;4\,e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)\;+\;A_T(\tau),\;}\tag{152.E}$$
con $A_T(\tau)=\frac1{2\pi}\int h_{T,\tau}\,\Omega_\infty=O\bigl(T^{-1}\log(2+\tau)\bigr)$
(pues $\int h=2\sqrt\pi/T$ y $\log(2+|s\pm\tau|)\le\log(2+\tau)+\log(2+|s|)$ bajo la gaussiana), y donde el
término del polo se calculó en cerrado:
$h(\pm\tfrac i2)$ suma $4e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)$ (cálculo directo de
$(\tfrac i2\mp\tau)^2=-\tfrac14\mp i\tau+\tau^2$).

**[TEOREMA 152.2] (espectro de impureza de ζ; incondicional).** Sea
$\{(\delta_j,\gamma_j)\}_{j\in J}$ la lista (finita o infinita) de cuádruplos off de ζ
($\delta_j\in(0,\tfrac12)$, $\gamma_j>14$), con multiplicidades $m_j$. Entonces:

**(a) (fórmula exacta del peso).** Para todo $\tau\ge1$:
$$\omega(\tau)\;=\;\max\Bigl(0,\;\max_{j:\,|\gamma_j-\tau|<\delta_j}\bigl(\delta_j^2-(\gamma_j-\tau)^2\bigr)\Bigr),$$
donde el máximo interior recorre un conjunto FINITO (los cuádruplos con $|\gamma_j-\tau|<\delta_j\le\tfrac12$).
En particular $\Sigma_{\mathrm{imp}}\cap[1,\infty)=\bigcup_j(\gamma_j-\delta_j,\gamma_j+\delta_j)$, una
unión de "casquetes parabólicos" centrados en las alturas off con pesos pico $\delta_j^2$.

**(b) (signo forzado en la altura exacta).** Si $m\ge1$ y $J^*$ es el conjunto de cuádruplos con
$\delta_j=\delta_{\max}:=\max_j\delta_j$ (máximo atendido: bajo $m<\infty$ trivial; en general, los
cuádruplos con $|\gamma_j-\tau|<\delta_j$ para $\tau$ fijo son finitos y basta el máximo local), y
$\gamma_J$ es la altura de uno de ellos con multiplicidad total $m_J$ en $(\delta_{\max},\gamma_J)$,
entonces
$$S_T(\gamma_J)\;=\;-\,2\sqrt\pi\;m_J\;T\;e^{\delta_{\max}^2T^2}\,\bigl(1+o(1)\bigr)\qquad(T\to\infty).$$
El sesgo es **negativo permanente** (sin fase libre): el cuádruplo entero anti-correlaciona los primos
con $\cos(\gamma_J\log n)$.

**(c) (pureza bajo RH; el polo).** Si $m=0$, entonces $S_T(\tau)=O\bigl(T\log(2+\tau)\bigr)$ para todo
$\tau\ge1$: $\omega\equiv0$ en $[1,\infty)$. Incondicionalmente, $\omega(0)=\tfrac14$ con
$S_T(0)=2\sqrt\pi\,T\,e^{T^2/4}(1+o(1))$: **el polo es la impureza de peso $\tfrac14$ en la frecuencia 0.**

*Demostración.* Todo sale de (152.E) evaluando cada bloque.

*(i) Bloque del polo.* $\bigl|4e^{T^2(\frac14-\tau^2)}\cos(\tau T^2)\bigr|\le4e^{-T^2(\tau^2-\frac14)}=o(1)$
para $\tau\ge1$. Para $\tau=0$: $h_{T,0}(t)=2e^{-T^2t^2}$ y el término del polo es $4e^{T^2/4}$, dominante
(abajo).

*(ii) Ceros on-line.* Para $\rho=\tfrac12+i\gamma$: $h_{T,\tau}(\gamma)\in(0,2]$. Por Riemann–von Mangoldt,
el número de ceros con $|\gamma-\tau|\in[k,k+1)$ es $O(\log(2+\tau+k))$; entonces
$$0\;\le\;\sum_{\gamma\ \mathrm{on}}h_{T,\tau}(\gamma)\;\le\;C\sum_{k\ge0}e^{-T^2k^2}\log(2+\tau+k)\;\le\;C'\log(2+\tau)\qquad(T\ge1).$$

*(iii) Cuádruplos off.* El cuádruplo $(\delta_j,\gamma_j)$ aporta los cuatro puntos
$t=\pm\gamma_j\mp i\delta_j$. Como $h$ es par y de coeficientes reales,
$$X_j:=\sum_{\mathrm{cu\acute adruplo}}h_{T,\tau}(t)\;=\;4\,\mathrm{Re}\,e^{-T^2(\gamma_j-\tau-i\delta_j)^2}\;+\;4\,\mathrm{Re}\,e^{-T^2(\gamma_j+\tau-i\delta_j)^2}.$$
Cálculo del exponente: $-T^2[(\gamma_j-\tau)^2-\delta_j^2-2i(\gamma_j-\tau)\delta_j]$, luego
$$\mathrm{Re}\,e^{-T^2(\gamma_j-\tau-i\delta_j)^2}\;=\;e^{T^2(\delta_j^2-(\gamma_j-\tau)^2)}\,\cos\bigl(2T^2(\gamma_j-\tau)\delta_j\bigr),$$
y el término espejo tiene tasa $\delta_j^2-(\gamma_j+\tau)^2<0$ para $\tau,\gamma_j>0$ (despreciable).
**Cota superior:** agrupando por $|\gamma_j-\tau|\in[k,k+1)$ y usando $\delta_j\le\tfrac12$,
$$\Bigl|\sum_jX_j\Bigr|\;\le\;8\!\!\sum_{j:|\gamma_j-\tau|<1}\!\!e^{T^2(\delta_j^2-(\gamma_j-\tau)^2)}\;+\;C\log(2+\tau)\sum_{k\ge1}e^{-T^2(k^2-\frac14)}\;\le\;C''\log(2+\tau)\,e^{T^2\,r(\tau)},$$
con $r(\tau):=\max\bigl(0,\max_{|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2)\bigr)$ (los $j$ con
$|\gamma_j-\tau|<1$ son $O(\log(2+\tau))$, finitos). Insertando (i)–(iii) en (152.E):
$|S_T(\tau)|\le CT\log(2+\tau)\,e^{T^2r(\tau)}$, de donde $\omega(\tau)\le r(\tau)$. Esto prueba "≤" en (a)
y prueba (c) ($m=0\Rightarrow r\equiv0$ en $\tau\ge1$; y $S_T(0)$: en (152.E) con $\tau=0$ el polo da
$4e^{T^2/4}$, los ceros aportan $O(1)$ —todo cero tiene $|\gamma|>14$, luego $h_{T,0}(t_\rho)$ es
$O(e^{-T^2(14^2-1/4)})$—, así $S_T(0)=\frac{\sqrt\pi T}2\cdot4e^{T^2/4}(1+o(1))$; coincide con el cálculo
directo de silla $\sum\Lambda(n)n^{-1/2}e^{-u^2/4T^2}\approx\int_0^\infty e^{u/2-u^2/4T^2}du=2\sqrt\pi Te^{T^2/4}(1+o(1))$,
control de consistencia ✓).

**Cota inferior de (a) y (b) — el lema de no-cancelación.** Sea $\tau\ge1$ con $r(\tau)>0$ y sea
$a_{\max}=r(\tau)$ la tasa máxima, alcanzada por un conjunto finito $I$ de cuádruplos (ventana
$|\gamma_j-\tau|<\delta_j$, finita). Los términos de tasa $a_{\max}$ en $-\sum_\rho h$ son
$$f(T^2),\qquad f(x):=-\sum_{i\in I}4m_i\cos(b_ix),\qquad b_i:=2(\gamma_i-\tau)\delta_i,$$
**todos con coeficiente del mismo signo** (negativo) y fase nula. La función $f$ es un polinomio
trigonométrico real no nulo: su media cuadrática de Besicovitch es
$M(f^2)=8\sum_{b}\bigl(\sum_{i:b_i=b}m_i\bigr)^2>0$ (frecuencias iguales suman coherentemente — mismo
signo—; frecuencias distintas son ortogonales en media; el caso $b_i=0$, i.e. $\gamma_i=\tau$, da término
constante negativo, aún mejor). Por tanto existe $c>0$ y un conjunto de $x$ de densidad positiva con
$|f(x)|\ge c$; a lo largo de una sucesión $T_n\to\infty$ con $T_n^2$ en ese conjunto,
$$|S_{T_n}(\tau)|\;\ge\;\frac{\sqrt\pi T_n}2\Bigl[c\,e^{a_{\max}T_n^2}-C\log(2+\tau)\,e^{(a_{\max}-\eta)T_n^2}-C\log(2+\tau)\Bigr]\;\ge\;c'\,T_n\,e^{a_{\max}T_n^2},$$
donde $\eta>0$ es el gap entre $a_{\max}$ y la siguiente tasa (finitas tasas en la ventana; las tasas del
polo y de los espejos son $\le\tfrac14-\tau^2<0$ para $\tau\ge1$). Luego $\omega(\tau)\ge a_{\max}$:
igualdad en (a). Para (b): en $\tau=\gamma_J$ con $\delta_J=\delta_{\max}$, el conjunto de tasa máxima es
exactamente el de los cuádruplos en $(\delta_{\max},\gamma_J)$ (cualquier otro $j$ tiene
$\delta_j^2-(\gamma_j-\gamma_J)^2<\delta_{\max}^2$, estrictamente: o $\delta_j<\delta_{\max}$, o
$\gamma_j\ne\gamma_J$ con separación fija), su frecuencia es $b=0$ y su contribución es la CONSTANTE
$-4m_J e^{\delta_{\max}^2T^2}$: sin oscilación, sin subsecuencia —
$S_T(\gamma_J)=-\frac{\sqrt\pi T}2\cdot4m_Je^{\delta_{\max}^2T^2}(1+o(1))$, límite pleno, signo negativo
permanente. $\square$

**Observación 152.2bis (qué es exactamente el $o(1)$ de (b)).** Los términos comidos: otros cuádruplos
(tasa estrictamente menor, gap fijo del mundo H(m) — las constantes congeladas de D112 §1.2 (F1)), ceros
on-line ($O(\log\gamma_J)$, sin exponencial), polo ($e^{-T^2(\gamma_J^2-1/4)}$, ridículo para
$\gamma_J>14$), arquimediano ($O(T^{-1}\log\gamma_J)$). **La dominancia del término off sobre la densidad
on-line se consigue por completo** — el temor de que los ceros de la línea ahoguen la señal era infundado;
lo que NO se consigue es convertir la dominancia en contradicción (§3).

### 2.3. Corolarios: equivalencia, cuantización, diccionario

**[COROLARIO 152.3].**

**(i) (pureza semi-global ⟺ RH).** $\mathrm{RH}\iff\omega(\tau)=0$ para todo $\tau\ge1$
$\iff\Sigma_{\mathrm{imp}}=\{0\}$ (con $\omega(0)=\tfrac14$, el polo). En palabras: *RH dice que la
interacción infinita de los primos produce exactamente una resonancia exponencial: la diagonal (el polo).
Cada resonancia adicional es un cuádruplo off y viceversa, con diccionario exacto
(posición, peso) = (altura, $\delta^2$).*

**(ii) (dicotomía cuantizada).** Para cada $\tau\ge1$ fijo: o bien $S_T(\tau)=O(T\log(2+\tau))$
(polinomial), o bien $|S_T(\tau)|=e^{(\omega(\tau)+o(1))T^2}$ a lo largo de una sucesión, con
$\omega(\tau)$ tomado del menú $\{\delta_j^2-(\gamma_j-\tau)^2\}$ — **no hay crecimientos intermedios**
(p.ej. $e^{cT}$ es imposible). Bajo H(m), el menú es finito y los picos son
$\delta_1^2,\dots,\delta_m^2\in(0,\tfrac14)$: la impureza está **cuantizada** por las distancias de los
ceros a la línea.

**(iii) (el diccionario impureza↔resolución, ahora teorema global).** El casquete del cuádruplo
$(\delta,\gamma)$ es invisible en $S_T$ mientras $\delta^2T^2\lesssim\log(T\log\gamma)$ y domina cuando
$\delta^2T^2\gg\log(T\log\gamma)$: el umbral de detección es $T\asymp\delta^{-1}$ módulo factores
polilogarítmicos. Es el diccionario M3 del D134 §5.8 ("cero off a distancia $\delta$ ⟷ impureza detectable
a soporte $\asymp1/\delta$"), antes calibrado en el mundo local $F_{p,\alpha}$, ahora **probado para ζ a
nivel global** (vía 152.2). 

*Demostración.* (i): "⟸" si hay cuádruplo $(\delta^*,\gamma^*)$, por 152.2(a) $\omega(\gamma^*)\ge\delta^{*2}>0$.
"⟹" es 152.2(c). (ii): lectura directa de la prueba de 152.2 (las únicas tasas disponibles en (152.E) son
las del menú; si todas $\le0$, cada bloque es a lo sumo $O(T\log)$). (iii): comparación de
$T e^{\delta^2T^2}$ contra $T\log\gamma$. $\square$

### 2.4. La barrera de positividad: la única ley con signo

**[PROPOSICIÓN 152.4] (nada supera a la diagonal).** Incondicionalmente, de $\Lambda(n)\ge0$:
$$|S_T(\tau)|\;\le\;S_T(0)\;=\;2\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1))\qquad\forall\tau\in\mathbb R,$$
y por tanto $\omega(\tau)\le\tfrac14$ para todo $\tau$. Equivalentemente (vía 152.2(a)): todos los ceros
están en la banda cerrada $0\le\beta\le1$.

*Demostración.* $|\cos(\tau\log n)|\le1$ y todos los términos de $S_T(0)$ son $\ge0$: la desigualdad es
término a término. El tamaño de $S_T(0)$: cota de Chebyshev $\psi(x)\asymp x$ (incondicional) más silla
gaussiana, o directamente 152.2(c). La lectura espectral: si hubiera un cero con $\delta>\tfrac12$
(i.e. $\beta>1$), 152.2(b) daría $|S_T(\gamma_J)|\sim2\sqrt\pi m_JTe^{\delta^2T^2}>S_T(0)$ para $T$
grande: contradicción. $\square$

**Lectura estructural (el avatar exacto del mundo local).** La barrera $|S_T(\tau)|\le S_T(0)$ es la
versión semi-global de la barrera local $|c_m|\le2p^{m/2}$ del Teorema 6.7 del D131 — "coeficiente acotado
por diagonal", Cauchy–Schwarz aritmético — y del mecanismo de masa diagonal de la Prop. 6.5 del D131. La
masa diagonal global es el polo ($\omega(0)=\tfrac14$); la positividad dice que ninguna frecuencia puede
resonar más fuerte que la diagonal. **Y eso es exactamente la pureza de frontera de §1.3:**
$\omega\le\tfrac14$ ⟺ banda cerrada.

### 2.5. Mertens en la frontera: la positividad se agota exactamente ahí

**[PROPOSICIÓN 152.5] (frontera estricta dentro del marco).** $\omega(\tau)=\tfrac14$ es imposible para
$\tau\ge1$: no hay ceros con $\beta=1$ (ni, por 152.4, con $\beta>1$). La positividad de von Mangoldt,
ejecutada al máximo (desigualdad de Mertens), certifica la **banda abierta** y nada más.

*Demostración.* Supóngase un cero con $\delta_J=\tfrac12$ (i.e. $\beta=1$) a altura $\gamma_J\ge14$, con
multiplicidad $m_J\ge1$; por 152.4, $\delta_{\max}=\tfrac12$. De $\Lambda(n)\ge0$ y
$3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\ge0$ con $\theta=\gamma_J\log n$, término a término:
$$3\,S_T(0)\;+\;4\,S_T(\gamma_J)\;+\;S_T(2\gamma_J)\;\ge\;0.$$
Por 152.2(b)(c): $S_T(0)=2\sqrt\pi Te^{T^2/4}(1+o(1))$ y $S_T(\gamma_J)=-2\sqrt\pi m_JTe^{T^2/4}(1+o(1))$.
Luego
$$S_T(2\gamma_J)\;\ge\;(8m_J-6)\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1))\;\ge\;2\sqrt\pi\,T\,e^{T^2/4}\,(1+o(1)),$$
un sesgo POSITIVO de tasa $\tfrac14$ en la frecuencia $2\gamma_J\ne0$. Pero por (152.E) en
$\tau=2\gamma_J$: el polo aporta $O(e^{-T^2(4\gamma_J^2-1/4)})$ (nada); los ceros on-line aportan a $S_T$
a lo sumo $O(T\log\gamma_J)$; y los casquetes off en $2\gamma_J$ tienen tasa
$\delta_j^2-(\gamma_j-2\gamma_J)^2\le\tfrac14$, con igualdad SOLO si $\delta_j=\tfrac12$ y
$\gamma_j=2\gamma_J$ exactamente — en cuyo caso su contribución a $S_T(2\gamma_J)$ es, por 152.2(b),
**negativa** ($-2\sqrt\pi m'Te^{T^2/4}$), no positiva. Es decir: un sesgo positivo de tasa $\tfrac14$ en
frecuencia no nula no tiene productor en (152.E) — el único término positivo de tasa $\tfrac14$ del
formulario es el polo, que vive en frecuencia 0. Contradicción. $\square$

**Comentarios.** (i) Esto reproduce, dentro del marco, el teorema clásico $\zeta(1+i\gamma)\ne0$ [dVP96],
[Mer98] — no es nuevo como hecho; es nuevo como **medición de jurisdicción**: el mecanismo 3-4-1 (el test
de dos protuberancias del D131 §6.5, en versión global: frecuencias $0,\gamma_J,2\gamma_J$ contra la masa
diagonal) es TODO lo que $\Lambda\ge0$ sabe hacer, y alcanza exactamente hasta la frontera. (ii) El
refinamiento clásico $\beta\le1-c/\log\gamma$ (de la Vallée Poussin) sale del mismo mecanismo compitiendo
contra el término arquimediano a $T$ finito calibrado con $\log\gamma$; el **calendario** $1/\log\gamma$
de la repulsión de frontera es la misma escala que el calendario natural de LP-134/LP-141 (Docs 141/144) —
pero medido desde la frontera $\mathrm{Re}=1$, no desde el centro. No lo re-derivo (clásico, citado); lo
registro porque exhibe la simetría: **repulsión de frontera a calendario log = teorema (positividad);
repulsión de centro a calendario log = LP-134/141, no-analítica y abierta.** (iii) Tras 152.4+152.5, la
positividad está EXHAUSTA: $\omega(\tau)<\tfrac14$ estricto, sin información sobre $\omega\in(0,\tfrac14)$
— la zona donde vive H(m).

### 2.6. La impureza es irreduciblemente colectiva

**[PROPOSICIÓN 152.7] (cada primo es semi-globalmente puro; las truncaciones finitas también).** Para
cualquier conjunto finito $P$ de primos, la suma parcial
$S^{(P)}_T(\tau):=\sum_{p\in P}\sum_{k\ge1}(\log p)\,p^{-k/2}e^{-(k\log p)^2/4T^2}\cos(\tau k\log p)$
satisface $|S^{(P)}_T(\tau)|\le\sum_{p\in P}\frac{\log p}{\sqrt p-1}=O_P(1)$, uniforme en $T$ y $\tau$:
$\omega^{(P)}\equiv0$, **incluida la frecuencia 0**.

*Demostración.* Cota trivial: gaussiana y coseno $\le1$, serie geométrica en $k$. $\square$

**Lectura.** Ni el polo ($\omega(0)=\tfrac14$) ni ninguna impureza hipotética en $\tau>0$ es visible en
ningún tramo finito de primos: ambos son fenómenos del LÍMITE — la masa de Chebyshev emergiendo de la cola
infinita. Coherente, y ahora cuantitativamente alineado, con B1–B4 del Doc 135 (la positividad pasa al
límite; la espectralidad no; toda la dificultad está en el límite, no en ningún paso finito) y con el
teorema de dos primos (Doc 135, Teorema A: cruzados = 0 — en el mundo finito puro no hay interacción que
pueda resonar). **La pureza semi-global es, literalmente, pureza de la interacción infinita: el objeto que
la decide no es ningún dato local ni semilocal finito.**

### 2.7. Davenport–Heilbronn viola la pureza semi-global, visiblemente y al máximo

**[PROPOSICIÓN 152.6] (la violación de D–H supera el techo de la positividad).**

(a) Si $F$ es cualquier función tal que $-F'/F$ admite una expansión de Dirichlet
$\sum_n\Lambda_F(n)n^{-s}$ con $\Lambda_F(n)\ge0$ y $\sum_n\Lambda_F(n)n^{-\sigma}<\infty$ para todo
$\sigma>1$ (normalización $F\to1$ cuando $\sigma\to+\infty$), entonces $F$ no se anula en $\sigma>1$.

(b) La función de Davenport–Heilbronn $f$ tiene infinitos ceros con $\beta>1$ ([DH36]; Doc 146, Hecho
146.4, verificado). Por (a), **$f$ no admite ningún dato de von Mangoldt positivo con abscisa 1**. En el
lenguaje del marco: el análogo espectral de su peso de impureza en las alturas de esos ceros es
$\delta^2>\tfrac14$ — D–H **supera el techo $\tfrac14$ que ningún objeto con dato positivo puede superar**
(152.4).

*Demostración.* (a) Para $\sigma\ge\sigma_0$ grande, $\log F(s)=\sum_n\frac{\Lambda_F(n)}{\log n}n^{-s}$
(integración término a término, lícita por convergencia absoluta); la serie de la derecha converge
absolutamente en todo $\sigma>1$, definiendo $G$ holomorfa en $\sigma>1$ con $e^G=F$ en
$\sigma\ge\sigma_0$; por continuación analítica $e^G=F$ en $\sigma>1$ y $F=e^G\ne0$ allí. (b) [DH36] +
(a), contrapositiva. La lectura espectral del peso: el casquete de un cero con $\delta>\tfrac12$ tiene
pico $\delta^2>\tfrac14$ (el bloque (iii) de la prueba de 152.2 es un cálculo sobre el lado de los ceros
y aplica a cualquier divisor dado; para D–H no afirmo la identidad (152.E) — que requeriría SU fórmula
explícita — sino solo la lectura del divisor). $\square$

**El balance del encargo (a)–(b)–(c).** (a) D–H viola la pureza semi-global **visiblemente**: sus ceros
con $\beta>1$ son violaciones de peso $>\tfrac14$, imposibles para cualquier dato positivo — la forma más
cruda de "pureza de interacción" ($\Lambda\ge0$) ya separa, y la separación es la que el Doc 146 pedía
(la positividad del término de primos es lo único que D–H no tiene). (b) ζ satisface **por teorema** la
pureza semi-global de peso $\le\tfrac14$ con frontera estricta (152.4+152.5), porque $\Lambda\ge0$.
(c) Pero la pureza que la rigidez necesita es $\omega\equiv0$ ($\tau\ge1$), que por el Corolario 152.3(i)
**es RH**: el intervalo $(0,\tfrac14)$ de pesos de impureza es exactamente el espacio de los mundos H(m).
La pregunta del encargo queda reducida a su forma exacta: ¿puede $m<\infty$ cerrar el intervalo
$(0,\tfrac14)$? La sección §3 ejecuta el intento y localiza el fallo.

---

## 3. El intento «m<∞ + Λ≥0 + ecuación funcional ⟹ m=0», paso a paso

Hipótesis de trabajo H(m) (Doc 112 §1.1): ζ tiene exactamente $m$ cuádruplos off, $0<m<\infty$,
$\{\tfrac12\pm\delta_j\pm i\gamma_j\}_{j\le m}$, parámetros congelados (F1 del D112): $\delta_{\max}>0$,
alturas fijas. Objetivo: contradicción. Cada paso lleva etiqueta.

### 3.1. Paso A [TEOREMA — instancia de 152.2(b)]: el sesgo exponencial forzado

Bajo H(m), con $J$ el cuádruplo dominante ($\delta_J=\delta_{\max}$, altura $\gamma_J$, multiplicidad
$m_J$):
$$S_T(\gamma_J)\;=\;-\,2\sqrt\pi\,m_J\,T\,e^{\delta_{\max}^2T^2}\,(1+o(1))\;\longrightarrow\;-\infty.$$
Tres rasgos, todos probados: (i) **dominancia total**: el término off excede a los ceros on-line
($O(\log\gamma_J)$, sin exponencial), al polo y al arquimediano — la esperanza del encargo ("el término
off domina la densidad on-line en tests largos") se REALIZA por completo; (ii) **signo forzado**: la
ecuación funcional + la realidad en el eje convierten al cuádruplo en señal de fase cero — los cuatro
ceros empujan en la MISMA dirección, anti-correlación pura de los primos con $\cos(\gamma_J\log n)$, sin
fase libre que pudiera rotar el sesgo; (iii) **constantes congeladas**: el umbral de visibilidad
$T\gtrsim1/\delta_{\max}$ es un número fijo del mundo H(m) — ningún problema de uniformidad interna.

### 3.2. Paso B [PROPOSICIÓN — 152.4/152.5]: la única ley con signo disponible

¿Qué cota con signo tiene el lado de los primos? La positividad $\Lambda\ge0$ produce exactamente
$$|S_T(\tau)|\;\le\;S_T(0)\;=\;2\sqrt\pi\,T\,e^{T^2/4}(1+o(1)),\qquad\text{más la mejora de Mertens en el borde,}$$
y nada más. En particular, **el lado de primos NO "tiene un signo" frente al test que detecta
$\gamma_J$**: el test $\cos(\gamma_J\log n)$ oscila, y $\Lambda\ge0$ solo da signo contra tests no
negativos ($g\ge0\Rightarrow\sum_n\Lambda(n)n^{-1/2}g(\log n)\ge0$), cuyo contenido espectral se
concentra en $t\approx0$ y no ve la altura $\gamma_J>14$. Este es el punto que el encargo pedía
identificar: **la positividad de von Mangoldt es información de frecuencia cero.** Es además la versión
en frecuencias del Cálculo 141.M4 (Doc 141): la palanca de positividad de Landau, que en $s=1$ da
Deuring–Heilbronn, es idénticamente nula en la línea crítica.

### 3.3. Paso C [el choque]: dónde muere la contradicción — GAP-152.A

Combinar A y B: la contradicción $|S_T(\gamma_J)|>S_T(0)$ exige
$$e^{\delta_{\max}^2T^2}\;>\;e^{T^2/4}\qquad\Longleftrightarrow\qquad\delta_{\max}\;\ge\;\tfrac12\;\Longleftrightarrow\;\beta\ge1.$$
La positividad refuta exactamente los ceros en/tras la frontera — que YA están excluidos (152.5 = dVP).
Para $\delta_{\max}<\tfrac12$, el sesgo requerido es un factor $e^{-(1/4-\delta_{\max}^2)T^2}$ MÁS
PEQUEÑO que la masa total disponible: **el mundo H(m) vive entero dentro del margen de Cauchy–Schwarz de
la pureza de frontera.** No hay contradicción; la identidad (152.E) se satisface idénticamente con el
sesgo incluido — la tautología de la fórmula explícita (Doc 112, Prop. 4.2) reaparece intacta en
coordenadas de frecuencia: la fórmula no sobredetermina; el único contenido no-tautológico es el signo, y
el signo disponible (Paso B) se agota en la frontera.

**[GAP-152.A] (el eslabón que falta, nombrado).** Una cota incondicional
$$|S_T(\tau_0)|\;=\;O_{\epsilon,\tau_0}\!\bigl(e^{\epsilon T^2}\bigr)\quad\forall\epsilon>0,\qquad\text{para algún }\tau_0\in(\gamma_J-\delta_J,\;\gamma_J+\delta_J),$$
i.e. subexponencialidad de la correlación de primos en UNA frecuencia. Por 152.2(a) esto equivale a
«ningún cuádruplo off cuya ventana cubra $\tau_0$» — la conclusión buscada, por frecuencia. El Paso C no
puede cerrarse sin GAP-152.A, y GAP-152.A en la frecuencia mala ES (una instancia local de) lo que se
quiere probar. **Circularidad localizada con precisión: el intento convierte «no hay cuádruplo
$(\delta_J,\gamma_J)$» en «no hay correlación exponencial en $\gamma_J$», que es el mismo enunciado bajo
el diccionario exacto 152.2.** El valor del diccionario no es nulo (§4); el camino directo no cierra.

### 3.4. La ruta de oscilaciones (Ingham/Pintz) y su inversión exacta

La idea (2) del encargo: un cero off fuerza oscilación de $\psi(x)-x$ de amplitud creciente; ¿con
$m<\infty$ la oscilación "no se puede cancelar" y contradice algo? Inventario honesto:

- **[Dato clásico, verificado en lo cualitativo].** Si ζ tiene un cero $\rho_0=\beta_0+i\gamma_0$,
  entonces $\psi(x)-x=\Omega_\pm(x^{\beta_0-\epsilon})$; las formas finas dan oscilación bilateral de
  tamaño comparable a $x^{\beta_0}/|\rho_0|$ (E. Schmidt [Sch03] para $\Omega_\pm(x^{1/2})$; Ingham
  [Ing36] y [Ing32, Cap. V] para la versión con cero hipotético; Pintz [Pin80] para versiones efectivas y
  localizadas). **[GAP de literatura]:** constantes y formas exactas de [Ing36]/[Pin80] no verificadas al
  nivel de página esta sesión; uso SOLO el contenido cualitativo "la oscilación ocurre de verdad", que no
  es premisa de ningún [TEOREMA] de este documento.
- **El mecanismo de esos teoremas es el teorema de oscilación de Landau** (un integrando eventualmente de
  UN signo fuerza que la abscisa de convergencia sea singularidad real; [Ing32, Cap. V]): se aplica a
  $\psi(x)-x$ **usando $\Lambda\ge0$**.

**La inversión.** La esperanza ingenua era: "$\Lambda\ge0$ da un signo al lado de primos, y el término
oscilante $x^{1/2+\delta_J}\cos(\gamma_J\log x+\phi)$ del cero off contradice ese signo". Es exactamente
al revés: **la positividad es el motor que DEMUESTRA que la oscilación del cero off se realiza** (Landau
necesita el integrando de un signo). Positividad y oscilación de $\psi(x)-x$ no chocan: cooperan. $\psi$
es no decreciente (positividad), pero los términos oscilantes son $o(x)$ y la monotonía no los ve;
$\psi(x)-x$ es una diferencia y oscila libremente.

**Dónde fallaría una contradicción y qué la salvaría.** Una contradicción por oscilaciones necesita un
PAR: (oscilación forzada $\ge X$) ∧ (cota superior $<X$). La mitad inferior existe (Landau/Ingham, vía
positividad). La mitad superior necesaria sería $|\psi(x)-x|=O(x^{1/2+\delta_{\max}-\epsilon})$ — que es
**la negación de H(m)** (esa cota elimina el cuádruplo dominante): la ruta es estructuralmente circular,
no le falta una estimación. $m<\infty$ no aporta la mitad superior: bajo H(m), $\psi(x)-x$ tiene
genuinamente los términos $x^{1/2+\delta_j}$ y ninguna cota mejor es verdadera EN ese mundo. **La
hipótesis mínima que salva la ruta de oscilaciones es la negación de la hipótesis: valor cero como
ruta.** (Confirma, por tercera coordenada independiente, la Obs. 4.3 del D112: la finitud protege los
argumentos internos al mundo, no los evaluadores externos.)

### 3.5. Qué compra m<∞ de verdad, y qué no

**Compra (probado):**
1. **Menú finito y cuantizado** (Cor. 152.3(ii)): el espectro de impureza es una unión FINITA de
   casquetes con picos $\delta_1^2,\dots,\delta_m^2$ y signo negativo forzado en las alturas exactas. La
   rigidez se vuelve: *un menú finito de resonancias prohibidas debe estar vacío.*
2. **Constantes congeladas**: el umbral de detección $T\asymp1/\delta_{\max}$ es un número del mundo, no
   un límite degenerante: el enunciado a certificar (GAP-152.A en $\gamma_J$) es UNA instancia individual,
   sin uniformidad interna pendiente — el análogo exacto de lo que H(m) compró para Rouché en el D112
   §2.6.
3. **Dominancia y signo** (Paso A): bajo H(m) la señal del defecto no es sutil — es exponencial, de signo
   fijo, en frecuencia fija. Ningún promedio la tapa DENTRO del mundo.

**No compra (probado):**
1. La cota del Paso B no mejora con $m$: la barrera $|S_T|\le S_T(0)$ es ciega al cardinal de ceros off.
   El intervalo $(0,\tfrac14)$ de pesos permitidos no se estrecha ni un epsilon con $m<\infty$.
2. La tautología (D112 Prop. 4.2) no se rompe: (152.E) es UNA identidad satisfecha idénticamente por la
   configuración verdadera; el sesgo del Paso A es la fórmula auto-consistiéndose, no una tensión.
3. El caso $m=1$ no es más fácil (paralelo exacto del D112 §5.3): la dificultad es la certificación de
   UNA frecuencia, independiente de $m$.

### 3.6. La excepcionalidad dual: las frecuencias malas son invisibles a todo promedio

**[PROPOSICIÓN 152.9] (media de Besicovitch en la frecuencia).** Para cada $T\ge1$ fijo, $S_T(\cdot)$ es
una función de Bohr casi-periódica de $\tau$ (límite uniforme de polinomios trigonométricos: la serie
converge absoluta y uniformemente), y su media cuadrática es
$$M_\tau\bigl(|S_T|^2\bigr)\;:=\;\lim_{\Omega\to\infty}\frac1{2\Omega}\int_{-\Omega}^{\Omega}|S_T(\tau)|^2\,d\tau
\;=\;\frac12\sum_{n\ge2}\frac{\Lambda(n)^2}{n}\,e^{-(\log n)^2/2T^2}\;\le\;C\,T^2.$$
En consecuencia, para todo umbral $V>0$, la densidad superior (de Besicovitch) del conjunto
$\{\tau:|S_T(\tau)|\ge V\}$ es $\le CT^2/V^2$; con $V=e^{\epsilon T^2}$, las **frecuencias exponenciales
tienen densidad $\le CT^2e^{-2\epsilon T^2}\to0$**: son excepcionales para todo promedio en $\tau$.

*Demostración.* Casi-periodicidad de Bohr: convergencia absoluta y uniforme en $\tau$ de la serie de
$S_T$. Parseval para funciones casi-periódicas [Bes32, Cap. I–II]: las frecuencias $\log n$ son distintas
dos a dos y cada término $\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$ aporta la mitad del
cuadrado de su amplitud. La suma: con $u=\log n$ y $\sum_{n\le x}\Lambda(n)^2/n\asymp(\log x)^2$
(Chebyshev + sumación parcial),
$\sum_n\Lambda(n)^2n^{-1}e^{-u^2/2T^2}\asymp\int_0^\infty ue^{-u^2/2T^2}du\asymp T^2$. Chebyshev
(desigualdad de medida) para la densidad. $\square$

**Lectura — la pinza con el Doc 112.** Bajo H(m), la frecuencia mala $\gamma_J$ existe y es UNA; la
Prop. 152.9 dice que el conjunto de frecuencias capaces de portar señal exponencial tiene densidad cero:
**certificar GAP-152.A en $\gamma_J$ es decidir un punto excepcional de la estadística que lo gobierna**
— el Principio 3.1 de P43 (el cuantificador maestro), en la coordenada DUAL a la de la Prop. 2.6 del
D112. Allí: los $\tau$ de réplica buenos (para Rouché) forman un conjunto de densidad cero y hay que
PRODUCIR uno. Aquí: las frecuencias $\tau$ malas (resonantes) forman un conjunto de densidad cero y hay
que EXCLUIR una. Réplica y evaluación, existencial y universal: la misma pared, las dos caras.

---

## 4. La hipótesis mínima y el mapa comparativo

### 4.1. LP-152: la forma puntual de la pureza semi-global

**[DEFINICIÓN-NUEVA 152.8] (LP-152).** Para $\tau_0\ge1$:
$$\mathrm{LP\text{-}152}(\tau_0):\qquad |S_T(\tau_0)|\;=\;O_\epsilon\bigl(e^{\epsilon T^2}\bigr)\ \ \forall\epsilon>0
\qquad(\text{subexponencialidad en }T^2).$$
Por el Teorema 152.2(a): $\mathrm{LP\text{-}152}(\tau_0)\iff$ ningún cuádruplo off de ζ tiene
$|\gamma_j-\tau_0|<\delta_j$. Consecuencias inmediatas, todas probadas:

1. LP-152 en TODA frecuencia $\tau\ge1$ $\iff$ RH (Cor. 152.3(i)). La familia completa es
   RH-equivalente — declarado sin maquillaje.
2. Una instancia individual LP-152$(\tau_0)$ es **estrictamente más débil que RH**: solo prohíbe
   cuádruplos en la ventana de $\tau_0$ (es la "RH por frecuencia").
3. Bajo H(m), la contradicción necesita LP-152 en UNA frecuencia (cualquier punto de la ventana del
   cuádruplo dominante, p.ej. $\tau_0=\gamma_J$) — pero la frecuencia es DESCONOCIDA (dato del mundo
   hipotético): la rigidez completa $m<\infty\Rightarrow m=0$ equivale a la familia
   $\{\mathrm{LP\text{-}152}(\tau)\}$ sobre las finitas frecuencias adversarias.

**Honestidad sobre el estatus.** No afirmo que LP-152$(\tau_0)$ sea demostrable para ningún $\tau_0$ más
allá de lo que las regiones clásicas dan (para ventanas dentro de la zona verificada
$\gamma\le3\cdot10^{12}$ [PT21], LP-152 vale trivialmente: no hay ceros off ahí; la zona no verificada es
exactamente donde vive el problema). El contenido de la definición es **el diccionario y la dualidad**,
no una promesa de demostrabilidad.

### 4.2. LP-152 contra LP-112: las dos caras de la pinza

| | **LP-112** (Doc 112) | **LP-152** (este doc) |
|---|---|---|
| tipo lógico | existencial: exhibir UN $\tau$ con $\sup_D\vert\zeta(s+i\tau)-\zeta(s)\vert<\epsilon$ | universal: acotar $S_T(\tau_0)$ en UNA frecuencia |
| mecanismo contra H(m) | réplica (Rouché): produce el cero $m{+}1$ | evaluación (fórmula explícita): prohíbe el sesgo del cuádruplo $J$ |
| qué congela H(m) | radio, margen, umbral de altura (F1–F4 del D112) | frecuencia y umbral $T\asymp1/\delta_{\max}$ |
| conjunto relevante bajo H(m) | testigos buenos: densidad CERO (D112 Prop. 2.6) | frecuencias malas: densidad CERO (Prop. 152.9) |
| relación con RH | RH ⟹ LP-112 (Bagchi); LP-112 ⇏ RH conocido; LP-112 ⟹ $m\in\{0,\infty\}$ | RH ⟹ LP-152$(\tau)\,\forall\tau$; instancia individual más débil que RH; familia ⟺ RH |
| insumo aritmético | independencia $\mathbb Q$-lineal de $\{\log p\}$, soporte de Bagchi | equidistribución fina de $\Lambda$ contra $\cos(\tau\log n)$ |
| forma del muro | producir un punto de un conjunto excepcional | excluir un punto de un conjunto excepcional |

**Comparación de fuerza, honesta.** No conozco implicación en ninguna dirección entre LP-112 y la familia
relevante de instancias LP-152: LP-112 ataca H(m) por la geometría de auto-aproximación de ζ (toro de
Kronecker, D112 §3); LP-152 por la estadística de los primos en una frecuencia. Bajo H(m) AMBOS son
enunciados sobre eventos individuales que toda la maquinaria de promedios clasifica como excepcionales:
la pared de P43 no distingue existencial de universal — distingue genérico de excepcional (la lección del
D112 §6.3, ahora con su gemelo dual). La ganancia de tener DOS formas: son rutas con insumos
independientes — un mecanismo de selección no-genérica en CUALQUIERA de las dos coordenadas cerraría la
rigidez.

### 4.3. Posición frente a 144.D, H⁺ y el límite B1–B4

- **Contra la Conjetura 144.D (mitad de finitud).** 144.D pide que la continuación del Euler genuino
  fuerce una subsucesión de ceros off GORDOS ($\delta_j\log\gamma_j\ge c$): es de la mitad $m<\infty$. La
  pureza semi-global es ortogonal y complementaria: no cuenta ceros; dice cómo CUALQUIERA de ellos resuena
  en los primos. El diccionario 152.3(iii) (detección a $T\asymp1/\delta$) es la versión global probada
  del mecanismo que 144.D postula localmente (impureza sostenida a soporte $\asymp\log\gamma$). Si 144.D
  vale, los off de un mundo $m=\infty$ son gordos ⟹ sus resonancias son detectables a
  $T\asymp\log\gamma_j$: coherencia de calendarios entre las dos mitades, registrada.
- **Contra la Conjetura H⁺ (Doc 131, Deseo 6.9).** El teorema deseado del encargo —«hermitiano + Euler +
  $a\ge0$ + polar + $m<\infty$ ⟹ H»— es H⁺ degradado por $m<\infty$. El resultado de §3 es que la
  degradación NO compra mecanismo: la pieza de H⁺ que $\Lambda\ge0$ ya da (frontera, $\omega\le\tfrac14$,
  152.4–152.5) no usa $m<\infty$, y la pieza restante ($\omega=0$) no se abarata con $m<\infty$ (§3.5).
  H⁺ sigue RH-dura; su primer caso genuino sigue siendo GAP-135.B (el objeto semilocal destructivo de dos
  primos).
- **Contra B1–B4 (Doc 135 §7.2).** La Prop. 152.7 cuantifica B1/B4 en el marco nuevo: ningún tramo finito
  de primos produce impureza NI diagonal; el polo (la diagonal global, $\omega(0)=\tfrac14$) y las
  resonancias hipotéticas ($\omega(\gamma_J)=\delta_J^2$) emergen juntos en el límite. RH es la afirmación
  de que el límite crea LA diagonal y NADA más — *resonancia única*. La pureza semi-global es la primera
  formulación del programa en que el polo y los ceros off son objetos del MISMO tipo (casquetes de
  impureza) distinguidos solo por posición (frecuencia 0 vs $\ne0$), peso ($\tfrac14$ vs $\delta^2$) y
  signo (positivo vs negativo).

---

## 5. VEREDICTO

### VEREDICTO: **REDUCCIÓN NUEVA + MAPA-DEL-FALLO. No hay teorema de rigidez; hay una forma equivalente nueva, teoremas internos al marco, y el fallo del camino de positividad localizado en un punto único.**

**Lo probado (incondicional, prueba completa en este documento):**

1. **[TEOREMA 152.2 + COROLARIO 152.3] (espectro de impureza).** $\omega(\tau)=\max(0,\max_j(\delta_j^2-(\gamma_j-\tau)^2))$
   para $\tau\ge1$; el polo es la impureza de peso $\tfrac14$ en frecuencia 0; en la altura de un cuádruplo
   dominante el sesgo es negativo permanente, $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}$.
   RH ⟺ $\omega\equiv0$ en $[1,\infty)$ ⟺ *resonancia única (el polo)*. Crecimientos intermedios
   imposibles; impureza cuantizada por los $\delta_j^2$; diccionario detección $T\asymp1/\delta$ (M3 del
   D134) probado a nivel global.

2. **[PROPOSICIONES 152.4 + 152.5 + 152.6 + 152.7] (jurisdicción exacta de la positividad y frontera
   ζ/D–H).** $\Lambda\ge0\Rightarrow\omega\le\tfrac14$ con igualdad solo en el polo (Mertens global,
   frontera estricta = dVP reproducido en el marco) — exactamente la manifestación global de la pureza
   local de peso 0 de los factores de ζ, y nada más. La impureza es irreduciblemente colectiva (todo tramo
   finito de primos es puro, coherente con B1–B4). D–H supera el techo $\tfrac14$ (ceros con $\beta>1$ ⟹
   ningún dato de von Mangoldt positivo es posible): la separación repulsión/pureza del Doc 146,
   formalizada como $\omega\le\tfrac14$ (teorema, ζ) vs $\omega>\tfrac14$ (D–H).

3. **[§3: Pasos A–C + GAP-152.A + PROPOSICIÓN 152.9] (mapa del fallo).** El intento
   «$m<\infty+\Lambda\ge0+$EF ⟹ $m=0$» falla en tres puntos exactos: **(F1)** la positividad es
   información de frecuencia cero — su única ley es $|S_T(\tau)|\le S_T(0)$ y la contradicción exigiría
   $\delta_{\max}\ge\tfrac12$ (la frontera, ya excluida): el mundo H(m) vive en el margen de Cauchy–Schwarz
   $e^{-(1/4-\delta_{\max}^2)T^2}$; **(F2)** la tautología de la fórmula explícita (D112 Prop. 4.2) se
   confirma en coordenadas de frecuencia: el sesgo del Paso A es auto-consistencia, no tensión; **(F3)**
   la ruta de oscilaciones es circular con inversión de Landau: la positividad es el MOTOR de la oscilación
   de $\psi(x)-x$, no su freno, y la cota superior que falta es la negación de H(m).

**La hipótesis mínima, medida.** LP-152$(\gamma_J)$ (subexponencialidad de UNA correlación de
frecuencia): estrictamente más débil que RH como instancia; como familia sobre las frecuencias
adversarias, equivalente a la rigidez; dual exacto de LP-112 (réplica/evaluación,
existencial/universal); con certificado de excepcionalidad propio (152.9: frecuencias malas de densidad
cero) — el cuantificador maestro de P43 por su segunda cara.

**Cómo queda la mitad de rigidez.** Mejor enfocada y con dos brazos independientes: LP-112 (réplica) y
LP-152 en las frecuencias adversarias (evaluación), ambos no-RH-equivalentes como instancias, ambos
bloqueados por el mismo muro de selección no-genérica, con insumos distintos. La síntesis pedida queda
establecida: hay TRES purezas, no dos — **frontera** (peso 0, teorema: lo que $\Lambda\ge0$ compra),
**semi-global** ($\omega\equiv0$: lo que la rigidez necesita, ⟺ RH), **global** ($m=0$, idéntica a la
anterior vía el diccionario 152.2) — y el contenido exacto de la mitad de rigidez es cruzar de
$\omega\le\tfrac14$ a $\omega=0$ en un menú finito de frecuencias desconocidas. $m<\infty$ congela el
menú; no lo vacía. **La positividad de von Mangoldt no es la pureza que colapsa $m$: es la pureza que
confina la impureza al intervalo $(0,\tfrac14)$.** Lo que el Euler genuino debe aportar de más —si el
programa tiene razón— es un mecanismo de selección no-genérica en una de las dos coordenadas duales;
ninguno de los métodos catalogados (promedios, recurrencia, amplificación, positividad, momentos) lo
produce.

### Mensaje final

**VEREDICTO: REDUCCIÓN NUEVA + MAPA-DEL-FALLO.** No existe (y este documento muestra por qué no puede
existir por esta ruta) el teorema «$m<\infty+\Lambda\ge0+$ecuación funcional ⟹ $m=0$»: la positividad de
von Mangoldt certifica exactamente la pureza de frontera ($\omega\le\tfrac14$, de la Vallée Poussin) y es
ciega a toda frecuencia no nula; el mundo H(m) vive en el margen de Cauchy–Schwarz de esa barrera. A
cambio, la mitad de rigidez gana una forma equivalente nueva (espectro de impureza, cuantizado, con signo
forzado) y un objetivo dual de LP-112.

**Tres resultados principales:**

1. **[TEOREMA 152.2 + COROLARIO 152.3]** — *Espectro de impureza de ζ:* fórmula exacta
   $\omega(\tau)=\max(0,\max_j(\delta_j^2-(\gamma_j-\tau)^2))$ para $\tau\ge1$; sesgo negativo forzado
   $S_T(\gamma_J)\sim-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}$; el polo = impureza de peso $\tfrac14$ en
   frecuencia 0; RH ⟺ resonancia única; dicotomía polinomial/exponencial cuantizada; el diccionario
   impureza↔resolución ($T\asymp1/\delta$, M3 del D134) probado a nivel global para ζ.

2. **[PROPOSICIONES 152.4 + 152.5 + 152.6 + 152.7]** — *Jurisdicción exacta de la positividad y frontera
   ζ/D–H:* $\Lambda\ge0\Rightarrow\omega\le\tfrac14$ con igualdad solo en el polo (test de Mertens
   global, frontera estricta); la impureza es irreduciblemente colectiva; D–H supera el techo $\tfrac14$
   y no admite dato de von Mangoldt positivo — la separación repulsión/pureza del Doc 146, formalizada; y
   la discrepancia de peso (B3 del D135) clarificada: RH = recentrar los CEROS del peso 0 al peso 1, lo
   único que la ecuación funcional no hace.

3. **[GAP-152.A + DEFINICIÓN-NUEVA 152.8 + PROPOSICIÓN 152.9]** — *Mapa del fallo y dual de LP-112:* el
   camino positividad+finitud muere en F1–F3 (frecuencia cero / tautología / circularidad de oscilaciones,
   con la inversión de Landau identificada: la positividad demuestra la oscilación, no la impide); la
   hipótesis mínima es LP-152 (subexponencialidad de la correlación de primos en una frecuencia), más
   débil que RH por instancia, dual existencial/universal de LP-112, con frecuencias malas de densidad
   cero — la segunda cara del cuantificador maestro.

---

## Referencias

**Internas (backward-only):** Doc 146 (repulsión barata/pureza cara; D–H gorda; Hechos 146.4–146.6);
Doc 144 (LP-141, categoría D131-H⁺, Conjetura 144.D, GAP-144.C); Doc 141 (LP-134; Cálculo 141.M4 palanca
nula en la línea; Conjetura 141.E); Doc 137 (auditoría del borde $|\alpha|=1$); Doc 135 (Teorema A de dos
primos; §7.2 B1–B4, B3 desajuste de peso); Doc 134 (§5.8 M3 diccionario pureza↔resolución; calendarios);
Doc 131 (§6: Teorema 6.7 pureza local, Prop. 6.5 masa diagonal, Prop. 6.8 D–H por bloques, Deseo 6.9
Conjetura H⁺); Doc 112 (LP-112; Teorema 2.3/5.1; Prop. 2.6 densidad cero; Prop. 4.2 tautología de la
fórmula explícita; Obs. 4.3 evaluadores externos; §5.3 caso m=1; §6.3 genérico vs excepcional); Doc 109
(arquitectura D-109); P43 (Principio 3.1, cuantificador maestro); P35 ($\kappa=2m$). ERRATA Phase 38
respetada ($W_\lambda\ge0$ refutado, no usado).

**Literatura (publicada, verificable salvo marca):**
- [Wei52] A. Weil, *Sur les «formules explicites» de la théorie des nombres premiers*, Comm. Sém. Math.
  Univ. Lund (1952), 252–265. (Fórmula explícita; criterio de positividad ⟺ RH.)
- [Gui48] A. P. Guinand, *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2)
  50 (1948), 107–119. (Forma de sumación de la fórmula explícita.)
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. (Thm. 5.12:
  fórmula explícita con clase de tests admisibles — la convención usada en (152.E).)
- [dVP96] Ch.-J. de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers*,
  Ann. Soc. Sci. Bruxelles 20 (1896), 183–256. (No anulación en $\mathrm{Re}\,s=1$; región libre clásica.)
- [Mer98] F. Mertens, *Über eine Eigenschaft der Riemannschen ζ-Funktion*, Sitzungsber. Akad. Wiss. Wien
  107 (1898), 1429–1434. (La desigualdad $3+4\cos\theta+\cos2\theta\ge0$.)
- [Sch03] E. Schmidt, *Über die Anzahl der Primzahlen unter gegebener Grenze*, Math. Ann. 57 (1903),
  195–204. ($\Omega_\pm$ para $\psi(x)-x$.)
- [Ing32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge Tracts 30, Cambridge Univ. Press,
  1932. (Cap. V: teoremas de oscilación; el teorema de Landau de integrandos de un signo.)
- [Ing36] A. E. Ingham, *A note on the distribution of primes*, Acta Arith. 1 (1936), 201–211.
  (Oscilación forzada por un cero hipotético. **[GAP de literatura]:** constantes exactas no verificadas
  al nivel de página esta sesión; uso solo cualitativo, no load-bearing.)
- [Pin80] J. Pintz, *On the remainder term of the prime number formula* I–II, Acta Arith. 36–37 (1980).
  (Oscilaciones efectivas localizadas por un cero. **[GAP de literatura]:** enunciados exactos no
  verificados al nivel de página esta sesión; uso solo cualitativo, no load-bearing.)
- [Bes32] A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Parseval para
  funciones casi-periódicas — Prop. 152.9.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11
  (1936), 181–185 y 307–312. (Ceros con $\beta>1$ — Prop. 152.6.)
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Riemann–von Mangoldt: $O(\log)$ ceros por ventana unitaria; §10.25 D–H.)
- [PT21] D. Platt, T. Trudgian, *The Riemann hypothesis is true up to* $3\cdot10^{12}$, Bull. London
  Math. Soc. 53 (2021), 792–797. (Zona verificada — §4.1.)

*Fin del Doc 152.*
