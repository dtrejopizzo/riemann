# Documento 184 — Auditoría adversarial de D175 (dicotomía de energía) y D181 (GAP 175.A / LP-112 mínimo)

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato:** auditoría a destrucción de la cadena que sostiene la torre de energía: [Lema 175.1] → [Thm 175.2 / Obs 175.3 / Cor 175.4–175.5] → [Thm 175.6] → [Prop 175.7–175.8] → [Thm 181.1 / Thm 181.2 / Cor 181.3]. Pregunta del director: **¿LP-112 murió de verdad como input independiente, o revive?**
**Fuentes leídas completas, línea por línea:** D175 (`phase-55-two-arrows/175-dicotomia-de-energia.md`), D181 (`phase-56-two-towers/181-gap175A-lp112-minimo.md`). Citas load-bearing verificadas en fuente: D112 §2.2 (enunciados LP-112 y LP-112⁻, Teorema 2.3, líneas 219–256 del archivo fuente) — coinciden textualmente con la reproducción de D175 §1; Thm 170.5 ($E(T)\ll T/\log T$) aceptado como certificado por la auditoría de Fase 54 (no re-auditado aquí).
**Postura:** adversarial. Cada paso fue atacado con intención de romperlo. Donde digo CERTIFICADO, la prueba se verificó término a término, constantes incluidas.

---

## 0. Veredicto ejecutivo

**La cadena AGUANTA.** Tras ataque sistemático a los nueve puntos del mandato (réplica de Rouché, dirección del traslado, separación de testigos, convenciones de cuádruplo, factores 2/4, acotación de los intervalos $T_z$, mismatch de definiciones 175↔181, vacuidad de Bagchi en $I=0$, circularidad 175.2↔175.8↔181.1), **no se encontró ningún error fatal ni degradante**. Se encontraron dos erratas inocuas (E-184.1, E-184.2) y una observación de clasificación estructural que el propio D181 ya hace a media voz: **el Thm 181.1 es matemáticamente redundante (contrapositiva exacta del Thm 175.2 en su forma fuerte Obs 175.3), pero su lectura estratégica es correcta y decisiva**. Respuesta al director: **LP-112 murió de verdad como atajo; no revive.** La torre $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$ es la formulación correcta.

---

## 1. [LEMA 175.1] (Rouché–Hurwitz con tasa) — **CERTIFICADO**

Verificación término a término.

**(i).** Hipótesis: $g$ holomorfa en entorno de $\bar D(z_0,R)$, cero único $z_0$ de multiplicidad $m_0$, $\eta(\delta)=\min_{|z-z_0|=\delta}|g|>0$ (positivo porque $g$ no se anula en $\bar D\setminus\{z_0\}$ y el círculo $|z-z_0|=\delta\le R$ no pasa por $z_0$). Si $\sup_{\bar D}|f-g|<\eta(\delta)$, en el círculo $|z-z_0|=\delta$ vale $|f-g|<\eta(\delta)\le|g|$: Rouché clásico ([T39 §3.42]) da que $f$ tiene en $D(z_0,\delta)$ tantos ceros con multiplicidad como $g$, esto es $m_0$. ✓ Sin huecos.

**(ii).** $g=c(z-z_0)^{m_0}h$, $h(z_0)=1$, $|h|\ge\tfrac12$ en $\bar D(z_0,\delta_1)$ por continuidad. En $|z-z_0|=\delta\le\delta_1$: $|g|\ge\tfrac{|c|}2\delta^{m_0}$, luego $\eta(\delta)\ge\tfrac{|c|}2\delta^{m_0}$. Con $\delta(\varepsilon)=(4\varepsilon/|c|)^{1/m_0}$: la condición $\varepsilon\le\tfrac{|c|}4\delta_1^{m_0}$ garantiza $\delta(\varepsilon)\le\delta_1$, y $\eta(\delta(\varepsilon))\ge\tfrac{|c|}2\cdot\tfrac{4\varepsilon}{|c|}=2\varepsilon>\varepsilon\ge\sup|f-g|$. La aplicación de (i) es legítima. Aritmética verificada: el factor $4$ en $\delta(\varepsilon)$ es exactamente el necesario para que el margen sea $2\varepsilon$, no $\varepsilon$ (estricto). ✓

Ataque intentado: ¿$\delta_1$ podría no existir si $h$ oscila? No: $h$ es holomorfa (extensión removible) con $h(z_0)=1$; continuidad basta. ¿Y si $f$ tiene ceros en el anillo $\delta(\varepsilon)<|z-z_0|\le R$? Irrelevante: el lema solo afirma el conteo DENTRO de $D(z_0,\delta)$. No hay sobre-afirmación.

---

## 2. [TEOREMA 175.2] + [Obs 175.3] (dicotomía de energía) — **CERTIFICADO**

**Constantes del cero (§2.2).** $r=\tfrac12\min(b_0,\ \tfrac12-b_0,\ \mathrm{dist}(\rho_0,Z(\zeta)\setminus\{\rho_0\}))$. Tres consecuencias verificadas:
1. $r\le b_0/2$ ⟹ $D_0\subset\{\sigma>\tfrac12+\tfrac{b_0}2\}$: **todo el disco está estrictamente a la derecha de la línea** — esto responde el punto de ataque 1(b) del mandato: ningún cero replicado dentro de $D(\rho_0+i\tau,r)$ puede ser on-line; el cero es off por construcción del radio, no por argumento posterior. ✓
2. $r\le\tfrac12(\tfrac12-b_0)$ ⟹ $D_0\subset\{\sigma<1\}$, dentro de la franja abierta (Hadamard–dVP da $b_0<\tfrac12$ estricto, la holgura existe). ✓
3. $r\le\tfrac12\mathrm{dist}(\rho_0,Z(\zeta)\setminus\{\rho_0\})$ ⟹ $\zeta$ no se anula en $D_0\setminus\{\rho_0\}$ — hipótesis exacta del Lema 175.1, incluida la unicidad del cero. ✓ **Hallazgo positivo no señalado en D175:** como $\bar\rho_0\in Z(\zeta)$ y $\mathrm{dist}(\rho_0,\bar\rho_0)=2\gamma_0$, la definición de $r$ da automáticamente $r\le\gamma_0$; esto garantiza (sin argumento adicional) que los discos trasladados $D(\rho_0+i\tau,r)$ con $\tau>0$ viven en $\{\operatorname{Im}>0\}$ — usado tácitamente en 175.6 ("solo el miembro derecho-superior del cuádruplo puede caer en el disco"). El tácito es correcto.

**Paso 1 (dirección de la réplica — punto de ataque 1(b)).** Verificada la dirección lógica con cuidado: $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|=\varepsilon_k<\eta$ ⟹ (Lema 175.1(i), $g=\zeta|_{D_0}$, $f=\zeta(\cdot+i\tau_k)|_{D_0}$, $\delta=R=r$) ⟹ $\zeta(\cdot+i\tau_k)$ tiene $m_0$ ceros en $D(\rho_0,r)$ ⟹ si $\zeta(s'+i\tau_k)=0$ con $s'\in D(\rho_0,r)$, entonces $s'+i\tau_k$ es **cero genuino de $\zeta$** en $D(\rho_0+i\tau_k,r)$, a altura $\in(\gamma_0+\tau_k-r,\gamma_0+\tau_k+r)$. ✓ La cota $b(\rho_k)\in(\tfrac{b_0}2,\tfrac{3b_0}2)$ sale de $|\operatorname{Re}\rho_k-(\tfrac12+b_0)|<r\le\tfrac{b_0}2$. ✓ La tasa fina $|\rho_k-(\rho_0+i\tau_k)|\le\delta(\varepsilon_k)$ es aplicación directa de 175.1(ii); D175 declara correctamente que es refinamiento, no insumo (Obs 175.3). ✓

**Paso 2 (separación — punto de ataque 3).** El paso a subsucesión $\tau_{j+1}>\tau_j+2r+1$ es legítimo ($\tau_k\to\infty$). Intervalos $(\gamma_0+\tau_j-r,\gamma_0+\tau_j+r)$: disjuntos (separación de centros $>2r$). El argumento "cuádruplos distintos": los dos miembros superiores de un cuádruplo ($\rho$ y $1-\bar\rho$) comparten parte imaginaria; partes imaginarias en intervalos disjuntos ⟹ cuádruplos distintos. Ataque: ¿podría $\rho_j$ ser el miembro IZQUIERDO ($1-\bar\rho$, con $\sigma<\tfrac12$) de un cuádruplo cuyo representante derecho ya fue contado en otro intervalo? No: $\rho_j\in D(\rho_0+i\tau_j,r)\subset\{\sigma>\tfrac12\}$, luego $\rho_j$ es siempre el miembro derecho-superior, y el conteo por intervalos de Im es conteo de cuádruplos sin colisión. ✓ Distintos del cuádruplo de $\rho_0$: para $\tau_j>r$ (eventual), $\operatorname{Im}\rho_j>\gamma_0$. Hueco aparente: ¿y $1-\bar\rho_0$ con la MISMA altura $\gamma_0$? Irrelevante: mismo cuádruplo que $\rho_0$, y alturas $>\gamma_0$ lo excluyen igual. ✓

**Paso 3 (conteo de energía — punto de ataque 1(d)).** $I=\sum_j b_j^2$ con UN representante por cuádruplo (convención fijada en cabecera, idéntica a D170). Cada cuádruplo de réplica es distinto (Paso 2) y su representante tiene $b\ge b_0/2$, aportando $\ge b_0^2/4$. **No hay doble conteo ni factor 4 fantasma**: la prueba usa una réplica por shift y un término por cuádruplo; la Obs 175.3 declara correctamente que la simetría del cuádruplo no se usa (multiplicaría la cota por 4 — pero la cota inferior $\infty$ no lo necesita). Si $I$ se sumara con multiplicidad, la cota inferior solo crecería. ✓ Divergencia: serie de términos $\ge b_0^2/4>0$ en cantidad infinita. ✓

**Obs 175.3.** Verificado contra la prueba: el único uso de la hipótesis es $\varepsilon_k<\eta$ para $k\ge k_0$ con $\{\tau_k\}$ no acotada — exactamente LP-112[$\rho_0$]. La instancia es realmente a precisión fija y disco único. ✓ **Sin mismatch de definiciones**: LP-112[$\rho_0$] (D175 §1b) y la que usa D181 §0 son idénticas letra a letra (mismo $D_0$ canónico, mismo $\eta$, "UN $\varepsilon<\eta$ fijo", sucesión no acotada).

**Verificación contra D112 en fuente.** Los enunciados LP-112 y LP-112⁻ de D175 §1 coinciden con D112 (líneas 219–224 del fuente, incluida la cláusula $\tau>\mathrm{altura}(D)$). La "honestidad sobre la novedad" de D175 §2.2 es exacta: el Teorema 2.3 de D112 ya contenía la réplica con $b\ge b_0-r$ implícita; lo nuevo es la lectura en $I$ y la tasa. ✓

---

## 3. [COR 175.4] (LP-112⁻ basta) — **CERTIFICADO-CON-ERRATA** (E-184.2, inocua)

La inducción de radios sumables, atacada paso a paso:
- $r_k\le b_0 2^{-k-2}$ ⟹ $\sum_{j\ge0} r_j\le b_0\sum 2^{-j-2}=b_0/2$ ⟹ $b^{(k+1)}\ge b^{(k)}-r_k\ge b_0-\sum_{j\le k}r_j\ge b_0/2$. La aritmética es correcta y el punto conceptual (sin sumabilidad la abscisa se fuga geométricamente) es genuino — este es el contenido no trivial del corolario. ✓
- Los demás brazos del $\min$ garantizan $D_k\subset$ franja abierta y unicidad del cero en $D_k$ (hipótesis de 175.1). ✓
- Crecimiento estricto de alturas: $\gamma^{(k+1)}>\gamma^{(k)}+\tau-r_k$ y $\tau>\mathrm{altura}(D_k)=\gamma^{(k)}+r_k>r_k$ ⟹ $\gamma^{(k+1)}>\gamma^{(k)}$. ✓ Alturas estrictamente crecientes ⟹ cuádruplos distintos (mismo argumento del Paso 2; los replicados viven en $\sigma>\tfrac12$, $\operatorname{Im}>0$ — son representantes). ✓
- Aplicación de LP-112⁻ con $(D_k,\eta_k/2)$: instancia legal del cuantificador "para todo $D$ y todo $\varepsilon$" verificado en D112. ✓

**E-184.2 (errata inocua).** El paréntesis "$\tau>\mathrm{altura}(D_k)\ (>2r_k+1)$" no está justificado en general ($\mathrm{altura}(D_k)=\gamma^{(k)}+r_k$, y $\gamma^{(k)}>r_k+1$ no se argumenta; vale para ζ porque todo cero tiene $\gamma>6$, pero el texto no lo invoca). Es decorativo: la prueba solo necesita $\tau>r_k$, que sí se sigue. Corrección en línea: borrar el paréntesis o sustituirlo por "$>r_k$".

---

## 4. [COR 175.5] (arquitectura) — **CERTIFICADO-CON-ERRATA** (E-184.1, inocua)

(1) $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$: si $1\le m<\infty$, $I$ es suma finita de términos en $(0,\tfrac14)$ ⟹ $0<I<\infty$, contradicción. ✓ La subsunción del Thm 2.3 de D112 con la misma hipótesis es correcta. (2) La lógica de la torre es trivialmente válida dada la dicotomía. ✓ $m<\infty\Rightarrow I<\infty$ trivial. ✓

**E-184.1 (errata inocua, repetida en 175.7.3).** El contraejemplo "$b_j=1/j$" viola la restricción $b\in(0,\tfrac12)$ en $j=1,2$ ($b_1=1$, $b_2=\tfrac12$). Corrección en línea: $b_j=1/(j+2)$ (o cualquier cola). La separación estricta cardinal/momento que el contraejemplo ilustra es correcta. **Nota adversarial que el doc omite:** no se discute si una configuración $b_j\to0$ es realizable por una función con la ecuación funcional y densidad de ceros de ζ — pero el corolario solo necesita que $I<\infty$ no implique formalmente $m<\infty$ *en la clase de configuraciones a priori*, que es como se usa (la primera flecha se debilita como ENUNCIADO). Uso legítimo.

---

## 5. [TEOREMA 175.6] (rareza con tasa) — **CERTIFICADO**

Punto de ataque 4 del mandato: el exponente y el mecanismo.

**El mapa de réplica.** Para $\tau\in A_\varepsilon$ ($\varepsilon<\eta$ — nótese: $A_\varepsilon$ con $\le\varepsilon$, y 175.1(i) requiere $<\eta(\delta)=\eta$; como $\varepsilon<\eta$ estricto, el margen existe ✓), zero replicado con $b\ge b_0/2$, $\operatorname{Im}\in(\gamma_0+\tau-r,\gamma_0+\tau+r)$. Identificación de cuádruplo: el disco vive en $\{\sigma>\tfrac12\}\cap\{\operatorname{Im}>0\}$ (lo segundo por $r\le\gamma_0$, §2 arriba), luego solo el representante puede caer en él. ✓ (El argumento del texto vía "radio $<\tfrac14$" es más débil que el necesario pero el hecho es cierto por la observación $r\le\gamma_0$; no lo cuento como errata porque la frase "vive en $\sigma>\tfrac12$" ya descarta los miembros izquierdo y, con $\operatorname{Im}>0$, los inferiores.)

**El cubrimiento (punto de ataque 2c).** $T_z=\{\tau:|\beta+i\gamma-\rho_0-i\tau|<r\}$: la condición sobre $\operatorname{Im}$ da $|\gamma-\gamma_0-\tau|<r$, luego $T_z\subset(\gamma-\gamma_0-r,\gamma-\gamma_0+r)$, intervalo de longitud $\le2r$, **acotado, con extremos determinados por la altura fija $\gamma=\gamma_z$ del cuádruplo**. ✓ $A_\varepsilon\cap[0,T]\subset\bigcup_{z\in\mathcal Z(T)}T_z$: todo testigo replica a un cuádruplo con $b\ge b_0/2$ y $\gamma\le T+\gamma_0+r$ ✓ (la holgura $+\gamma_0+r$ en el truncamiento es exactamente la necesaria). $\mathrm{meas}\le 2r\#\mathcal Z(T)$ ✓.

**Las dos cotas de $\#\mathcal Z(T)$.**
- Selberg: $\#\mathcal Z(T)\le N(\tfrac12+\tfrac{b_0}2,T+\gamma_0+r)$ — cada cuádruplo aporta al menos su representante al conteo de $N$ ✓ (de hecho $N$ puede contar más; la desigualdad va en la dirección buena). **Origen del $1/8$:** [S46] da $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; con $\sigma-\tfrac12=b_0/2$ el exponente es $1-\tfrac14\cdot\tfrac{b_0}2=1-b_0/8$. ✓ El $\tfrac18=\tfrac14\times\tfrac12$ es (constante de Selberg)×(pérdida de Rouché en la abscisa). Verificado.
- Chebyshev: $\#\mathcal Z(T)\le\sum_{\gamma_j\le T+\gamma_0+r}b_j^2/(b_0/2)^2=4E(\cdot)/b_0^2$ — Chebyshev legítimo porque $E$ suma sobre representantes, uno por cuádruplo, exactamente la población de $\mathcal Z$. **El factor 4 es $(b_0/2)^{-2}$, no convención de cuádruplo** — verificado, sin colisión de convenciones. ✓
- (iii) inyectividad: $|\tau_k-\tau_{k'}|>2r$ ⟹ discos trasladados disjuntos ⟹ los representantes replicados (puntos únicos por cuádruplo) son distintos. ✓

(ii) usa Thm 170.5 — certificado en Fase 54, cadena de citas backward-only en orden. Las lecturas 1–4 del §3 son sobrias; el GAP 175.B está bien declarado como gap. ✓

---

## 6. [PROP 175.7] — **CERTIFICADO-CON-ERRATA** (la misma E-184.1 en 175.7.3). Chebyshev y colas de serie convergente; sin contenido atacable.

## 7. [PROP 175.8] (anti-recurrencia) — **CERTIFICADO**. El eslabón maestro.

Es el Thm 175.6(ii)–(iii) con $T\to\infty$, legítimo porque bajo $I<\infty$ el Chebyshev global da $\#\mathcal Z(\infty)\le 4I/b_0^2<\infty$ **sobre la serie completa** — aquí está la respuesta al punto fino 2(c) del mandato: la finitud NO es por altura acotada de los replicados (sus alturas crecen con $\tau$) sino porque la población total de cuádruplos con $b\ge b_0/2$ en TODO el semiplano es finita cuando $I<\infty$. Cada uno de esos $\le 4I/b_0^2$ cuádruplos tiene altura fija $\gamma_z$ y solo puede servir a testigos en su intervalo $T_z\subset(\gamma_z-\gamma_0-r,\gamma_z-\gamma_0+r)$. Unión finita de intervalos acotados ⟹ $A_\varepsilon$ acotado ⟹ sin sucesión no acotada. ✓ Medida $\le 2r\cdot 4I/b_0^2=8rI/b_0^2$ ✓ (aritmética verificada). Conteo separado $\le 4I/b_0^2$ ✓.

**Ataques 2(d):** (a) ¿Replicados que coinciden para distintos $\tau$? Permitido y manejado: el cubrimiento por $T_z$ no exige inyectividad — varios testigos pueden compartir cuádruplo, pero entonces viven en el MISMO intervalo $T_z$ de longitud $2r$; la medida los absorbe y el conteo separado los excluye por disjunción de discos. ✓ (b) ¿$2b_0>\tfrac12$ (disco saliendo de la franja)? Imposible por construcción: $r\le\tfrac12(\tfrac12-b_0)$ mantiene $D_0$ en $\sigma<1$, y la franja relevante es $\sigma>\tfrac12$, garantizada por $r\le b_0/2$; ningún caso de $b_0$ rompe nada (todos los brazos del $\min$ se escalan). ✓ (c) ¿Multiplicidad de $\rho_0$? $\eta>0$ no la ve; 175.1(i) la maneja; el conteo es de cuádruplos, no de ceros con multiplicidad — y si $I$ se define con multiplicidad, las cotas solo mejoran. ✓ (d) ¿$\varepsilon$ escondido tendiendo a 0? **No**: toda la prueba es a $\varepsilon$ fijo $<\eta$; el único umbral es $\eta$, y D175 §5 prueba además que es exacto (con $\varepsilon\ge\eta$ Rouché no gana — correcto, y honesto). ✓

## 8. [TEOREMA 181.1] — **CERTIFICADO** (con clasificación: redundante como matemática, decisivo como lectura)

Prueba de tres líneas, verificada: $0<I<\infty$ ⟹ existe $\rho_0$; LP-112[$\rho_0$] daría sucesión no acotada en $A_\varepsilon$ (algún $\varepsilon<\eta$); 175.8 (válida para TODO $\varepsilon<\eta$, en particular ése) la prohíbe. Para LP-112 pleno: instancia en $D_0$ da convergencia uniforme, eventual $<\eta/2<\eta$, sucesión no acotada en $A_{\eta/2}$. ✓ **Sin mismatch** (punto 2a): mismo disco canónico, mismas constantes, misma definición de testigo que 175.8 — verificado carácter a carácter entre D181 §0/§1 y D175 §1b/§2.2/§5. **Sin $\varepsilon\to0$ escondido** (punto 2b): confirmado. **Test anti-circularidad de D181 §1:** correcto — 181.1 usa solo 175.8 (incondicional) y la definición de LP-112[$\rho_0$]; no usa 175.2.

**Pero hay que decirlo sin media voz:** 181.1 es exactamente la contrapositiva de la forma fuerte del Thm 175.2 (Obs 175.3: LP-112[$\rho_0$] ⟹ $I=\infty$ dado $I>0$). D181 lo admite ("contrapositivas la una de la otra"). El contenido matemático NUEVO de 181.1 es nulo; el contenido ESTRATÉGICO (GAP 175.A pedía probar un enunciado falso en el único mundo con contenido; LP-112 no es input independiente) es la extracción correcta y no se había hecho. No es circular: es la misma moneda mirada del otro lado, y el programa necesitaba mirarla.

## 9. [TEOREMA 181.2] y [COR 181.3] — **CERTIFICADOS**

**El test Bagchi (punto de ataque 6) — la sospecha de vacuidad FALLA.** LP-112 no es condicional-a-existencia: cuantifica sobre TODOS los discos cerrados de la franja (verificado en D112 fuente, línea 219), sin mención de ceros. Bajo RH ($I=0$) no hay disco-con-cero-off, pero el enunciado pleno sigue exigiendo auto-aproximación en todos los discos — y eso es un teorema genuino, no vacuo: es la dirección RH ⟹ recurrencia fuerte de Bagchi (densidad inferior positiva para todo $\varepsilon$, de donde sucesiones no acotadas por diagonal $\tau_k\in A_{1/k}$, $\tau_k>k$). El "por Bagchi" de 181.2(1) es correcto y necesario, no sloppiness. ✓ 181.2(2)=181.1 ✓; 181.2(3) declarado gap ✓.

**Cor 181.3.** (1) ida = 175.2 ✓; vuelta-en-$I=0$ = 181.2(1) ✓; "⟺ módulo GAP 181.A" es bookkeeping exacto. (2) Condicional a $A$ ($I<\infty$): LP-112 ⟹ (por 181.1) ¬($0<I<\infty$) ⟹ $I=0$ ⟹ RH; recíproco Bagchi. ✓ (3) es lectura, y es la correcta: cualquier prueba de LP-112 contiene una exclusión del estado intermedio. ✓ El test D–H del §3 está honestamente etiquetado ([GAP de literatura 181.C], universalidad conjunta no verificada en fuente — bien declarado, no cuenta como afirmación).

**Ataque de consistencia 175.2↔175.8↔181.1 (punto 5).** Mapa lógico final verificado: 175.2 se prueba directo (réplica iterada); 175.8 se prueba por conteo (cubrimiento); son dos PRUEBAS independientes de dos caras del mismo bicondicional parcial. 181.1 no añade prueba; añade el nombre. Ninguna invoca a la otra circularmente. ✓

---

## 10. (i) Tabla resumen

| Pieza | Veredicto | Nota |
|---|---|---|
| Lema 175.1 | **CERTIFICADO** | Rouché–Hurwitz cuantitativo; constantes verificadas |
| Thm 175.2 + Obs 175.3 | **CERTIFICADO** | condicional a LP-112[$\rho_0$], declarado; sin doble conteo |
| Cor 175.4 | **CERTIFICADO-CON-ERRATA** | E-184.2 (paréntesis decorativo injustificado) |
| Cor 175.5 | **CERTIFICADO-CON-ERRATA** | E-184.1 ($b_j=1/j$ viola $b<\tfrac12$) |
| Thm 175.6 | **CERTIFICADO** | exponente $1-b_0/8$ = Selberg $\tfrac14\times$ Rouché $\tfrac12$, verificado |
| Prop 175.7 | **CERTIFICADO-CON-ERRATA** | misma E-184.1 |
| Prop 175.8 | **CERTIFICADO** | el eslabón maestro AGUANTA todos los ataques del mandato |
| Thm 181.1 | **CERTIFICADO** | redundante como matemática (contrapositiva), decisivo como lectura |
| Thm 181.2 | **CERTIFICADO** | caso $I=0$ NO es vacuo; "por Bagchi" es correcto |
| Cor 181.3 | **CERTIFICADO** | bookkeeping exacto; GAPs 181.A/181.C bien declarados |

## 11. (ii) Clasificación estructural (orden del director)

- **Lema 175.1:** herramienta clásica cuantificada — fuera de la taxonomía (no aporta información sobre ζ).
- **Thm 175.2 / Cor 175.4:** **COERCIVO condicional** (exclusión del estado $0<I<\infty$ bajo un axioma). PERO, a la luz de 181.1/181.3: su hipótesis equivale (módulo GAP 181.A, y exactamente bajo $A$) a su conclusión — **como par axioma→conclusión es REDUNDANTE: es la dicotomía con nombre de recurrencia**. La sospecha del director se confirma aquí: LP-112-como-input era una equivalencia local de RH disfrazada (condicional a $A$, LP-112 ⟺ RH). El doc 181 es precisamente el que lo destapa.
- **Thm 175.6:** **CORRELACIONAL genuino** — incondicional, segundo orden, transfiere el certificado $E(T)$ a rareza de auto-aproximación. La única pieza con contenido incondicional nuevo de D175. Es el puente real energía↔universalidad.
- **Prop 175.8:** **COERCIVO incondicional** — exclusión genuina de estados (recurrencia no acotada) dentro del mundo $0<I<\infty$. No es tautología: el presupuesto $4I/b_0^2$ es información real sobre ese mundo.
- **Thm 181.1:** **REDUNDANTE** matemáticamente (relectura contrapositiva de 175.2-fuerte); su valor es metateórico.
- **Thm 181.2 / Cor 181.3:** **MIXTO** — ensamblaje correcto cuya función es demoler una lectura estratégica falsa. El "resultado" es la demolición, no un teorema nuevo.

## 12. (iii) Respuesta directa al director: ¿LP-112 murió o revive?

**Murió, y la muerte está certificada.** La cadena 175.8 → 181.1 no tiene error: en el mundo $0<I<\infty$ — el único donde la torre necesitaba a LP-112 con contenido — LP-112 (incluso su instancia mínima a precisión fija en un solo disco) es **falsa**, incondicionalmente. Por tanto: (a) LP-112 no puede usarse como input independiente, porque probarla exige antes excluir el estado intermedio, que era el trabajo que se le encomendaba; (b) condicional a $A$, LP-112 ⟺ RH (Cor 181.3.2, verificado): es una equivalencia local de RH, no un lema parcial; (c) el único resquicio de vida es GAP 181.A ($I=\infty\Rightarrow$ LP-112), que en ambos escenarios S1/S2 deja a LP-112 sin estatus de input. **No revive.**

## 13. (iv) Impacto en la arquitectura

**$\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$ es la formulación correcta y queda confirmada.** Matices: (1) la torre NO se debilitó con la reescritura — Dic era ya el contenido efectivo de LP-112 en el rango relevante; lo que se perdió es una ilusión, no un activo; (2) el activo incondicional real de la fase es el par {Thm 175.6, Prop 175.8} más el certificado 170.5: la dirección sucesora de D181 §"Dirección sucesora" (atacar Dic vía coercividad D174 / Cesàro D176) es la consecuencia correcta de esta auditoría, no solo del entusiasmo del autor; (3) advertencia: Dic = $I\in\{0,\infty\}$ es, bajo $A$, equivalente a RH — el director debe vigilar que la fase 57+ no rebautice Dic con un tercer nombre y lo declare "lema atacable" (el patrón que LP-112 acaba de ejemplificar). El criterio de esta auditoría: un enunciado es input legítimo solo si tiene contenido en algún mundo donde no equivalga a la conclusión.

## 14. (v) Erratas

- **E-184.1** (D175, Cor 175.5.2 y Prop 175.7.3): el contraejemplo "$b_j=1/j$" viola $b\in(0,\tfrac12)$ en $j=1,2$. Corrección: $b_j=1/(j+2)$. Inocua (el punto cardinal-vs-momento sobrevive intacto).
- **E-184.2** (D175, Cor 175.4): el paréntesis "$\tau>\mathrm{altura}(D_k)\ (>2r_k+1)$" no se justifica; la prueba solo necesita $\tau>r_k$, que sí se sigue de $\tau>\mathrm{altura}(D_k)=\gamma^{(k)}+r_k$. Corrección: borrar el paréntesis. Inocua.
- (No-errata registrada): en Thm 175.6 la exclusión de miembros inferiores del cuádruplo descansa tácitamente en $r\le\gamma_0$, que se sigue de $\bar\rho_0\in Z(\zeta)$ en la definición de $r$ — correcto pero conviene hacerlo explícito en una futura revisión de D175 §3.

**Veredicto global: la cadena 175.1→175.2→175.6→175.8→181.1→181.3 está CERTIFICADA. Ningún resultado cae ni se degrada. La fase 55–56, en esta cadena, rompe la estadística de 1-de-4.**
