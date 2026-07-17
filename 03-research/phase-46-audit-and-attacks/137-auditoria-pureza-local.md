# Doc 137 — Auditoría adversarial del Teorema de Pureza Local (Doc 131, Teorema 6.7)

**Programa:** Hipótesis de Riemann — Phase 46: auditoría y ataques.
**Fecha:** junio 2026.
**Objeto auditado:** Teorema 6.7 de `phase-44-new-mathematics/131-algebra-correspondencias.md`, con toda su cadena de soporte (Def. 2.1, Def. 2.7, Prop. 2.8, Prop. 4.2, Teorema 4.4, Prop. 6.2, Teorema 6.6, Def./Prop. 6.6').
**Mandato:** destruir. Protocolo de 5 pasos ejecutado completo, solo cálculo simbólico en forma cerrada.

---

## 0. Veredicto en una línea

**SOBREVIVE CON ERRATA.** El contenido matemático del Teorema 6.7 (H ⟺ |α|=√p ⟺ |c_m|≤2p^{m/2}) es correcto en ambas direcciones — re-derivado de cero, símbolo a símbolo — pero su cadena formal de soporte tiene **una proposición falsa (Prop. 2.8(b), error de conjugación en el bloque discreto)** y **un error de tipo (F_{p,α} con α∉ℝ no es "hermitiano" según la Def. 2.7, así que la Def. 6.1 y la Prop. 6.2 no le aplican tal como están escritas)**. Ambos defectos son reparables sin tocar ningún cálculo; la reparación está en §4.

---

## 1. Re-derivación independiente (sin copiar la prueba del doc)

### 1.1. El objeto, desde cero

Datos: primo $p$, $L=\log p$, $\alpha\in\mathbb{C}^\times$ con $1<|\alpha|<p$. Pesos
$c_m := \alpha^m + (p/\bar\alpha)^m$, funcional
$$W_F(f) = L\sum_{m\in\mathbb{Z}} c_m f(p^m),\qquad f\in C_c^\infty(G),\ G=\mathbb{R}_+^*.$$

**Identidad espejo (re-derivada).** $c_{-m} = \alpha^{-m} + \bar\alpha^m p^{-m}$ y
$\bar c_m p^{-m} = \bar\alpha^m p^{-m} + (p/\alpha)^m p^{-m} = \bar\alpha^m p^{-m} + \alpha^{-m}$.
**Iguales.** ✓ Esta identidad es la que porta toda la hermitianidad del objeto (ver §4, E1–E2).

**Consistencia con la Def. 2.1.** Con $a(p^m)=-Lc_m$ ($m\ge1$), $c=0$, $\omega\equiv-2L$:
- $-P_a(f) = L\sum_{m\ge1}[c_m f(p^m) + \bar c_m p^{-m} f(p^{-m})]$; por la identidad espejo $\bar c_m p^{-m} = c_{-m}$, esto es $L\sum_{m\ne0} c_m f(p^m)$. ✓
- $-A_\omega(f) = \frac{2L}{2\pi}\int\hat f(\tfrac12+it)\,dt = 2L f(1) = Lc_0 f(p^0)$ (inversión de Mellin en $x=1$ sobre $\mathrm{Re}=\tfrac12$; convergencia absoluta por Paley–Wiener). ✓
- Nota de diseño (no error): el átomo $m=0$ admite dos realizaciones — $\omega\equiv-2L$ o $a(1)=-L$ — i.e. el mapa datos→funcional **no es inyectivo**. Inocuo aquí.

**Diccionario analítico (verificación de la etiqueta "Euler").** Para el polinomio de Dirichlet $D(s)=(1-\alpha p^{-s})(1-(p/\bar\alpha)p^{-s})$: $\log D = -\sum_{m\ge1}c_m p^{-ms}/m$, luego $-D'/D \leftrightarrow$ coeficiente $-Lc_m$ en $p^m$ — exactamente el $a$ del objeto, soportado en $p^{\mathbb N}$: tiene producto de Euler en el sentido del Teorema 1.9. ✓ Los ceros de $D$ son $Z(\alpha)\sqcup Z(p/\bar\alpha)$. ✓

### 1.2. Poisson (Teorema 6.6), re-derivado

$\alpha=p^\beta e^{i\phi}$, $\rho_k=\beta+i(\phi+2\pi k)/L$; chequeo: $p^{\rho_k}=p^\beta e^{i(\phi+2\pi k)}=\alpha$. ✓
Con $F(t):=f(e^t)e^{\beta t}e^{i\phi t/L}\in C_c^\infty(\mathbb{R})$:
$\hat f(\rho_k)=\int F(t)e^{2\pi ikt/L}dt$. Poisson clásico en el retículo $L\mathbb{Z}$ (periodización finita y $C^\infty$ — sin sutilezas de convergencia):
$\sum_k\widehat F(2\pi k/L) = L\sum_m F(mL) = L\sum_m \alpha^m f(p^m)$. ✓ El signo de la convención de Fourier solo reetiqueta $k\mapsto-k$; la suma bilateral es invariante. **Teorema 6.6 correcto.**

Par espectral: $\sigma Z(\alpha)=Z(p/\bar\alpha)$ porque $p^{1-\bar\rho}=p/\overline{p^\rho}=p/\bar\alpha$. ✓ Densidad lineal $N_Z(T)\asymp T$. ✓

### 1.3. Dirección ⟸ (pureza ⟹ H), cálculo cerrado

$|\alpha|=\sqrt p \Rightarrow p/\bar\alpha = \alpha$: las dos progresiones **coinciden** — el divisor es $Z(\alpha)$ con multiplicidad 2, todo en $\mathrm{Re}=\tfrac12$, y $c_m=2\alpha^m$. Para $g=f\star\tilde f$ (que está en $C_c^\infty(G)$):
$$Q_F(f,f)=W_F(g)=2\sum_{\rho\in Z(\alpha)}\hat g(\rho)
=2\sum_{\rho}\hat f(\rho)\,\overline{\hat f(1-\bar\rho)}
=2\sum_{\rho}|\hat f(\rho)|^2\;\ge\;0,$$
usando $\widehat{f\star\tilde f}(s)=\hat f(s)\overline{\hat f(1-\bar s)}$ y $1-\bar\rho=\rho$ en la línea. Convergencia absoluta: Paley–Wiener ($|\hat f(\tfrac12+it)|\ll_N(1+|t|)^{-N}$) contra densidad lineal. ✓
**Punto crítico de la auditoría:** este cálculo usa SOLO (i) la fórmula explícita (Poisson, probada) y (ii) $Z\subset\{\mathrm{Re}=\tfrac12\}$. **No usa en ningún paso que $a$ sea real** — relevante para la errata E2: la prueba sobrevive aunque la hipótesis "hermitiano" de la Prop. 6.2, tal como está tipada, falle.

### 1.4. Dirección ⟹ (impureza ⟹ ¬H), re-derivada

Sin pérdida $\delta'>0$ donde $|\alpha|=p^{1/2+\delta'}$ (el intercambio $\alpha\leftrightarrow p/\bar\alpha$ deja $c_m$ invariante: verificado, $p/\overline{(p/\bar\alpha)}=\alpha$). Test $f=u+\theta\,u(\cdot/p^M)$, $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$, $\chi$ par, $\mathrm{supp}\,\chi\subset[-1,1]$, $\int\chi^2=1$, $\epsilon<L/4$, $\theta\in\mathbb{C}$.

- $g(x)=(f\star\tilde f)(x)=\int f(y)\overline{f(y/x)}(y/x)\,d^*y$: re-derivado de $\tilde f(z)=\overline{f(1/z)}z^{-1}$, $\tilde f(x/y)=\overline{f(y/x)}(y/x)$. ✓ (coincide con el doc).
- Soporte: $g(x)\ne0\Rightarrow\log x\in\{0,\pm ML\}+[-2\epsilon,2\epsilon]$; las únicas potencias $p^m$ alcanzadas son $m\in\{0,\pm M\}$ porque $2\epsilon<L/2<L$. **No hay término en $\pm2M$** (las diferencias de centros de dos bumps son $\{0,\pm ML\}$). ✓
- $g(1)=\int|f|^2y\,d^*y$: soportes disjuntos ⟹ sin cruzados; $\int u^2y\,d^*y=\int e^{\epsilon s}\chi(s)^2ds=1+O(\epsilon)$ y el bump trasladado da $|\theta|^2p^M(1+O(\epsilon))$. ✓
- $g(p^M)=\theta\int u(y/p^M)^2(y/p^M)d^*y=\theta(1+O(\epsilon))$ (único solapamiento: $y\approx p^M$). ✓
- Hermitianidad de $g$: de $\tilde g=g$ sale $g(1/x)=x\,\overline{g(x)}$, luego $g(p^{-M})=p^M\bar\theta(1+O(\epsilon))$. ✓ (re-derivado; coincide).
- Ensamblado, con $c_{-M}g(p^{-M}) = \bar c_M p^{-M}\cdot p^M\bar\theta(1+O(\epsilon)) = \overline{c_M\theta}(1+O(\epsilon))$:
  $$Q_F(f,f)/L = \bigl[\,2(1+|\theta|^2p^M)+2\,\mathrm{Re}(c_M\theta)\,\bigr](1+O(\epsilon)).$$ ✓
- Fase adversaria $\theta=-(\bar c_M/|c_M|)t$, $t>0$: cuadrática $2+2p^Mt^2-2|c_M|t$, mínimo en $t^*=|c_M|/(2p^M)$:
  $$2+\frac{|c_M|^2}{2p^M}-\frac{|c_M|^2}{p^M}=2-\frac{|c_M|^2}{2p^M}<0\iff|c_M|>2p^{M/2}.$$ ✓ (re-derivado término a término; coincide).
- Crecimiento: $|c_M|\ge p^{M(1/2+\delta')}-p^{M(1/2-\delta')}=p^{M/2}\cdot2\sinh(M\delta' L)\to\infty\cdot p^{M/2}$ (desigualdad triangular inversa). ✓
- Orden de los cuantificadores: $M$ se fija primero (margen negativo fijo), $\epsilon$ después; las constantes en $O(\epsilon)$ dependen de $M,\theta$ ya fijados. **Sin circularidad.** ✓
- **Admisibilidad del test:** suma de dos bumps $C^\infty$ de soporte compacto con coeficiente complejo — está en $C_c^\infty(G;\mathbb{C})$, la clase exacta de la Def. 2.1/6.1 (la clase es compleja: la involución $\tilde f$ conjuga). ✓ El test detector de impureza **sí está en la clase admisible**. (Nota: si la clase fuera de funciones reales, $\theta$ real solo extrae $\mathrm{Re}(c_M)$ y la prueba necesitaría equidistribución de $M\phi$; la clase compleja evita ese hueco. Verificado que el doc usa la clase compleja en todo el documento.)
- Realidad de $Q_F(f,f)$ (necesaria para que "$\ge0$" tenga sentido): apareando $\pm m$, $c_mg(p^m)+c_{-m}g(p^{-m})=2\,\mathrm{Re}(c_mg(p^m))$ vía identidad espejo + $g(1/x)=x\overline{g(x)}$; y $g(1)=\int|f|^2y\,d^*y$ real. **$Q_F(f,f)\in\mathbb{R}$ para toda $f$ y todo $\alpha$ (incluso impuro y no real).** ✓

### 1.5. Tercera pata de la equivalencia

$|\alpha|=\sqrt p\Rightarrow|c_m|=2p^{m/2}$ exacto. $|\alpha|=p^{1/2+\delta'}$, $\delta'\ne0$ ⟹ $|c_m|>2p^{m/2}$ en cuanto $\sinh(m|\delta'|L)>1$ (m grande): la cláusula "$\forall m\ge1$" falla. ✓ Equivalencia correcta dentro del dominio declarado $1<|\alpha|<p$.

---

## 2. Tabla paso-de-la-prueba vs verificación

| # | Paso del doc (Teorema 6.7 y soporte) | Verificación independiente | Estado |
|---|---|---|---|
| 1 | Identidad espejo $c_{-m}=\bar c_m p^{-m}$ (6.6') | Re-derivada, exacta | ✓ |
| 2 | Realización del átomo $m=0$ como $\omega\equiv-2L$ | Mellin inverso en $\mathrm{Re}=\tfrac12$; convergencia PW | ✓ |
| 3 | "$F_{p,\alpha}$ es hermitiano" (6.6') | **FALSO según Def. 2.7** para $\alpha\notin\mathbb{R}$: $\bar a\ne a$. Verdadero solo como σ-simetría del funcional: $\overline{W_F(\tilde f)}=W_F(f)$ (re-derivado vía identidad espejo) | ✗ etiqueta / ✓ contenido (E2) |
| 4 | Prop. 2.8(b): $W_{\sigma X}(f)=\overline{W_X(\tilde f)}$ | **FALSA en el bloque discreto** para $a$ no real: el cálculo del propio doc da $\overline{P_a(\tilde f)}=P_a(f)$, y el doc inserta "con $a\mapsto\bar a$" sin justificación (contraejemplo cerrado en §4, E1) | ✗ (E1) |
| 5 | Poisson un factor (Teorema 6.6) | Re-derivado con periodización; signos de convención inocuos | ✓ |
| 6 | Par espectral $(F_{p,\alpha},Z_F)$, σ-estabilidad del divisor | $p^{1-\bar\rho}=p/\bar\alpha$; densidad lineal; convergencia absoluta | ✓ |
| 7 | ⟸ vía Prop. 6.2/Teorema 4.4(a) | El cálculo solo usa espectralidad + $Z\subset$ línea; **la hipótesis "hermitiano" de 6.2/4.4 ni se usa ni se cumple literalmente** — sobrevive con la hipótesis debilitada | ✓ con errata de tipado |
| 8 | Multiplicidad 2 en el caso puro ($Z(\alpha)=Z(p/\bar\alpha)$) | Contada correctamente: factor 2 en la suma de cuadrados | ✓ |
| 9 | $\delta'>0$ sin pérdida (swap $\alpha\leftrightarrow p/\bar\alpha$) | Mismo objeto: $c_m$ invariante | ✓ |
| 10 | Soporte del test: $g(p^m)=0$ salvo $m\in\{0,\pm M\}$ | $2\epsilon<L$; sin término en $\pm2M$ | ✓ |
| 11 | Valores $g(1),g(p^M),g(p^{-M})$ | Re-derivados; pesos $y$ y $p^M$ correctos | ✓ |
| 12 | Ensamblado $Q/L=2(1+|\theta|^2p^M)+2\mathrm{Re}(c_M\theta)$ | Coincide; el espejo da exactamente el conjugado, sin doble conteo | ✓ |
| 13 | Minimización: $2-|c_M|^2/(2p^M)<0\iff|c_M|>2p^{M/2}$ | Aritmética re-hecha | ✓ |
| 14 | Crecimiento de $|c_M|$ y orden $M\to\epsilon$ | $\sinh$; cuantificadores en orden correcto | ✓ |
| 15 | Test en la clase admisible | $C_c^\infty(G;\mathbb{C})$, sí | ✓ |
| 16 | Realidad de $Q(f,f)$ para objetos impuros (implícita en "¬H") | Probada vía espejo; el doc no la enuncia pero la usa | ✓ (laguna menor, ver E4) |
| 17 | Corolario "Euler ⇏ H" | Sigue del teorema + Teorema 1.9 (soporte de $a$ en $p^{\mathbb N}$, verificado vía $D(s)$) | ✓ |

**Búsqueda específica del tipo de error que mató a W_λ** (signo / borde / intercambio de Abel): el único intercambio de sumas es Poisson sobre periodización finita $C^\infty$ (inocuo) y el reordenamiento $\sum_\rho$ absolutamente convergente (PW + densidad lineal). El único borde es el átomo $m=0$, contado UNA vez (como $\omega$, no como $a(1)$ — sin doble conteo, verificado en el paso 2/12). El único error de signo encontrado está en la **conjugación** de la Prop. 2.8(b) (E1) — y no es load-bearing para 6.7.

---

## 3. Casos extremos

- **$\alpha=0$:** fuera del dominio ($|\alpha|>1$); además $p/\bar\alpha$ indefinido — el objeto no existe. El enunciado está bien acotado.
- **$|\alpha|=1$ (borde):** excluido del enunciado. Auditoría del borde: el objeto está definido, $\delta'=-\tfrac12$; el swap da $\delta'=+\tfrac12$ y $|c_M|\ge p^M-1>2p^{M/2}$ para $M\ge2$: el test mata H también ahí. La restricción $1<|\alpha|<p$ es elección de alcance, no encubrimiento de un caso patológico. ✓
- **$\alpha$ no real:** el caso central (Ramanujan genuino). Es exactamente donde aflora E1/E2 (el objeto no es Def-2.7-hermitiano). El contenido sobrevive: $Q$ es hermitiana y la equivalencia vale, vía la reparación de §4. En ⟹, la fase adversaria $\theta=-\bar c_M t/|c_M|$ es la que hace al test robusto frente a $c_M$ complejo. ✓
- **$\alpha=\pm\sqrt p$ (puro real):** $c_m=2(\pm\sqrt p)^m$, hermitiano incluso según Def. 2.7; todo consistente. ✓
- **Multiplicidades:** caso puro = una progresión con multiplicidad 2; el Teorema 4.4 admite multiplicidades y el factor 2 está bien contado. ✓
- **$p=2$:** $L=\log2$, $\epsilon<L/4\approx0.173>0$: el test cabe; nada degenera. ✓
- **Tests de soporte mínimo:** un solo bump ($\theta=0$) da $Q/L=2(1+O(\epsilon))>0$ — un bump nunca detecta impureza (consistente con §6.3: hace falta el mecanismo de Mertens de dos frecuencias). El test de dos bumps es mínimo y suficiente. ✓
- **Ambas direcciones en cada caso:** verificadas; ningún caso del dominio rompe ninguna dirección.

---

## 4. Erratas encontradas y reparación propuesta

### E1 (errata real, proposición falsa): Prop. 2.8(b)

**Enunciado del doc:** $W_{\sigma X}(f)=\overline{W_X(\tilde f)}$ con $\sigma X=(\bar a,\sigma c,\omega)$.
**El error:** en el bloque discreto, el propio cálculo del doc llega a $\sum_n[a(n)f(n)+\bar a(n)n^{-1}f(1/n)]$ — que es **$P_a(f)$, literalmente** — y a continuación afirma "con $a\mapsto\bar a$ — exactamente $P_{\bar a}(f)$" **sin que ninguna línea del cálculo produzca esa conjugación**. La identidad correcta es
$$\overline{P_a(\tilde f)} = P_a(f)\qquad\text{para TODA }a\ (\text{no }P_{\bar a}(f)),$$
porque el término espejo $\bar a(n)n^{-1}f(1/n)$ de la Def. 2.1 ya hardcodea la σ-simetría del bloque discreto.
**Contraejemplo cerrado:** $a$ soportada en $n_0=2$ con $a(2)=i$. Entonces $P_a(\tilde f)=\tfrac i2\overline{f(1/2)}-i\overline{f(2)}$, luego $\overline{P_a(\tilde f)}=if(2)-\tfrac i2 f(1/2)=P_a(f)$; mientras $P_{\bar a}(f)=-if(2)+\tfrac i2f(1/2)=-P_a(f)\ne P_a(f)$ para $f$ genérica. La Prop. 2.8(b) es falsa siempre que $a\ne\bar a$.
**Reparación:** $\overline{W_X(\tilde f)} = W_{X'}(f)$ con $X'=(a,\,\sigma c,\,\bar\omega)$ — **solo el bloque polar y $\omega$ se transforman; el discreto es σ-invariante por construcción.** Para $a$ real (todos los objetos σ-fijos de la Def. 2.7, incluido $\zeta_{\mathrm{ob}}$ con $a=\Lambda$) el enunciado original es correcto: por eso la errata pasó inadvertida.

### E2 (error de tipo): "hermitiano" en 6.6'/6.1/6.2 vs Def. 2.7

La Def. 2.7 exige $\sigma X=X$, i.e. **$a$ real**. Para $\alpha\notin\mathbb{R}$ (y $\alpha\ne$ caso real), $a(p^m)=-Lc_m$ es complejo: $F_{p,\alpha}$ **no es hermitiano según la Def. 2.7**, pese a que 6.6' lo declara tal. Consecuencia formal: la Def. 6.1 (Axioma H, definida "para objetos hermitianos") y las Prop. 6.2/Teorema 4.4 invocadas en la dirección ⟸ **no aplican literalmente al objeto del Teorema 6.7** en su caso genérico.
**Por qué no mata el teorema:** (i) $Q_F(f,f)$ es real para toda $f$ (probado en §1.4 vía identidad espejo), así que H está bien planteado; (ii) la prueba de 4.4(a) usa solo espectralidad + σ-estabilidad de $Z$, nunca $a$ real; (iii) por polarización, $Q_X$ es hermitiana para **toda** $a$ en cuanto $c$ es σ-estable y $\omega$ real — consecuencia directa de la identidad corregida en E1.
**Reparación (la natural):** debilitar "hermitiano" a **σ-simetría del funcional**: $X$ es hermitiano si $\overline{W_X(\tilde f)}=W_X(f)$ para toda $f$ — equivalentemente (con E1 corregida): $c$ σ-estable con pesos conjugados y $\omega$ real, **sin condición sobre $a$**. Con esta definición: la Prop. 2.8(c) vale con hipótesis más débiles (misma prueba), $F_{p,\alpha}$ es hermitiano para todo $\alpha$, y los Teoremas 4.4, 6.2, 6.3, 6.7 quedan correctamente tipados sin cambiar una sola línea de sus pruebas. Notar que **P48 ya usa exactamente esta definición** (su Lemma "hermitian": $\overline{W(\tilde f)}=W(f)$, probado vía la identidad espejo) — el paper se auto-reparó sin declararlo.

### E3 (arrastre menor): Prop. 4.2(b)

Hereda E1: lo demostrable es que $(\,(a,\sigma c,\omega),\,\sigma Z\,)$ es espectral (mismo $a$, no $\bar a$). Para los objetos del catálogo ($a$ real o $F_{p,\alpha}$, donde la simetría la da la identidad espejo) las consecuencias usadas no cambian.

### E4 (cosméticas)

(i) En la prueba de 6.7 queda una frase truncada de borrador: "$c_m=2p^{m/2}e^{im\phi}\cos(0)$… más precisamente". (ii) La realidad de $Q_X(f,f)$ para los objetos impuros (necesaria para que "¬H" signifique "existe $f$ con $Q<0$" y no "Q no real") se usa sin enunciarse; merece una línea (la del §1.4 de esta auditoría).

### Lo que se buscó y NO se encontró

Ningún error de signo en los cálculos de 6.6/6.6'/6.7; ningún intercambio ilegítimo de sumas; ningún doble conteo del átomo diagonal; ningún término de soporte omitido ($\pm2M$ verificado); el test adversarial está en la clase admisible; los cuantificadores $M\to\epsilon$ están en orden correcto. La dirección ⟸ se cerró con la forma explícita $Q=2\sum|\hat f(\rho)|^2$ y la ⟹ con el mínimo exacto $2-|c_M|^2/(2p^M)$. A diferencia del caso W_λ, aquí la positividad del caso puro no es un milagro de cancelación sino una suma manifiesta de cuadrados con Cauchy–Schwarz exacto en el borde.

---

## 5. Consecuencias para P48 (`06-papers/P48-weil-positivity-finite-primes/`)

1. **El teorema base de P48 queda confirmado.** P48 §"Local purity" re-prueba 6.7 de forma autocontenida; cada paso coincide con la re-derivación de §1 de esta auditoría. El teorema de $n$ primos (H ⟺ pureza de todos los factores) descansa en el caso de un primo + aditividad $Q_{X_1\star X_2}=Q_{X_1}+Q_{X_2}$, y el eslabón local es sólido.
2. **P48 NO hereda E1/E2.** Su Lemma "hermitian" define hermitianidad como $\overline{W(\tilde f)}=W(f)$ y la prueba vía $\bar c_{-m}p^m=c_m$ — exactamente la noción reparada de E2. No cita la Prop. 2.8(b) del Doc 131. Ninguna corrección es necesaria en P48 por esta auditoría.
3. **Acción recomendada (no urgente):** (i) corregir en el Doc 131 la Prop. 2.8(b) y la Def. 2.7 según §4 (y registrar en `06-papers/ERRATA.md`, junto a las erratas de Phase 38); (ii) en P48, si se desea blindaje, añadir la línea explícita de realidad de $Q(f,f)$ para factores impuros (E4.ii) — es un cálculo de tres líneas ya hecho aquí.
4. **Estabilidad del corolario estructural.** "Euler ⇏ H; el discriminador es pureza" queda intacto y, con E2 reparada, mejor fundado: la clase donde H está bien planteado es estrictamente mayor que la de la Def. 2.7, y los contraejemplos impuros complejos viven legítimamente dentro de ella.

---

## Referencias

**Internas (backward-only):** Doc 131 (objeto auditado); Doc 107 (clase de tests, Paley–Wiener, núcleo engrosado); Doc 110 (clase ℱ); `06-papers/P48-weil-positivity-finite-primes/main.tex` (Lemma hermitian, Theorem local purity); Phase 38 (precedente W_λ≥0, ERRATA.md).
**Literatura [DATO]:** A. Weil, Comm. Sém. Math. Lund (1952); E. Bombieri, Rend. Mat. Acc. Lincei (9) 11 (2000) (criterio de Weil); H. Montgomery, R. Vaughan, *Multiplicative Number Theory I*, 2007 (mecanismo de Mertens); E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §3.

*Fin del Documento 137.*
