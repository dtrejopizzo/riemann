# Documento 187 — Auditoría adversarial de D178 (Lema 177.B / tres vías) y D179 (LP-134 forma mínima)

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato:** auditoría destructiva de los Docs 178 y 179. Método: reconstrucción simbólica a mano de cada paso ANTES de aceptar el texto; ataque a cuantificadores, conversiones de carta (H vs Ξ/ζ: factores 2 en posición, 4 en tiempo), manejo de bordes de ventana, y dependencias escondidas. Clasificación estructural por orden del director. Sin numérica. Backward-only.
**Veredicto global anticipado:** los dos documentos sobreviven en su núcleo, pero la auditoría REFUTA un lema auxiliar (178.3), DEGRADA dos piezas con titular (178.10 "equivalencia" y 179.5 "inevitabilidad") y encuentra ocho erratas, dos de ellas con contenido (E-187.1, E-187.5). La deflación de la torre 2 (Cor 178.11) y la calibración cuasi-RH de 177.B (Cor 178.9) SOBREVIVEN porque solo usan la ida de 178.10.

---

## 1. Auditoría de D178

### 1.1. [Lema 178.1] ODE del gap — CERTIFICADO

Reconstrucción independiente. Con $\dot z_k=2\sum'_{j\ne k}(z_k-z_j)^{-1}$ y $g=x_{k+1}-x_k$:

- Término mutuo: $2\bigl[\tfrac1{x_{k+1}-x_k}-\tfrac1{x_k-x_{k+1}}\bigr]=2\bigl[\tfrac1g+\tfrac1g\bigr]=\tfrac4g$ ✓.
- Término del mar, por cada $j$ real: $2\bigl[\tfrac1{x_{k+1}-x_j}-\tfrac1{x_k-x_j}\bigr]=\tfrac{2[(x_k-x_j)-(x_{k+1}-x_j)]}{(x_{k+1}-x_j)(x_k-x_j)}=\tfrac{-2g}{(x_j-x_k)(x_j-x_{k+1})}$ (el producto de denominadores es invariante bajo el doble cambio de signo) ✓. Esto reproduce $S=\sum 2/[(x_j-x_k)(x_j-x_{k+1})]$ ✓.
- Signo: $x_j\notin(x_k,x_{k+1})$ ⟹ ambos factores del mismo signo ⟹ término $\ge0$ ✓.
- **Ceros complejos:** ataque del mandato verificado — el doc NO los barre bajo la alfombra: los confina en $\mathcal{E}$ con hipótesis explícita de exclusión a distancia $\le D$ y cota $|\mathcal{E}|\le C\rho/D^2+C\gamma^{-2}$ (pares conjugados combinados dan contribución real con denominador $\ge D^2$; densidad RvM). La hipótesis de realidad local está declarada en el enunciado ("intervalo de tiempos en que los ceros de la ventana son reales y simples"), no escondida. ✓
- Caveat menor heredado: la dinámica $\dot z=2\Sigma'$ exige simplicidad; está en la hipótesis del lema. ✓

**Veredicto: CERTIFICADO.** Clasificación: COERCIVO (ley de clase, ζ-libre).

### 1.2. [Prop 178.2] saturación del reticulado — CERTIFICADO

Reconstrucción de la saturación. Reticulado a paso $g_*$: el $m$-ésimo vecino a la derecha de $x_{k+1}$ dista $mg_*$ de $x_{k+1}$ y $(m+1)g_*$ de $x_k$; término $=\frac{2}{mg_*\cdot(m+1)g_*}=\frac2{g_*^2}\cdot\frac1{m(m+1)}$. Suma por lado: $\frac2{g_*^2}\sum_{m\ge1}\frac1{m(m+1)}=\frac2{g_*^2}$ (telescópica $=1$ ✓). Dos lados: $S=\frac4{g_*^2}$ ⟹ $\dot g=\frac4{g_*}-g_*\cdot\frac4{g_*^2}=0$ **exacto** ✓.

Convención de signo del calor (ataque del mandato): el doc usa $\partial_tH=-\partial_z^2H$ (carta P15). Con $H=\cos(\lambda z)$: $-\partial_z^2\cos(\lambda z)=\lambda^2\cos(\lambda z)$ ⟹ $H_t=e^{t\lambda^2}\cos(\lambda z)$ — **consistente con la convención declarada del propio doc** (la advertencia del mandato sobre $e^{-\lambda^2t}$ corresponde a la convención opuesta; el doc detecta y aísla la discrepancia con el mandato en §0 honestamente). Los ceros no se mueven (factor escalar) ⟹ estacionariedad exacta ✓. La conclusión metodológica (ningún principio del mínimo desnudo cierra 177.B; hace falta conteo) es correcta y es además la que desactiva la heurística "$g^2\ge8t$, $\theta=\frac12$".

**Veredicto: CERTIFICADO.** Clasificación: CORRELACIONAL (no-go de calibración; no empuja, delimita).

### 1.3. [Lema 178.3] bloques comprimidos cortos — REFUTADO (paso falso: el troceo)

Este es el hallazgo destructivo principal de la auditoría en D178. Reconstrucción:

- Caso $\ell\le1$ (equivalente a $M\le 2\rho$): $M\le\rho\ell+C_0L\le\tfrac M2+C_0L$ ⟹ $M\le2C_0L$ ✓ — pero entonces la hipótesis ya da $M\le2\rho\asymp L/2\pi$, y si $C_0\ge\frac1{4\pi}$ la conclusión es **más débil que la hipótesis del caso**: versión vacua.
- Caso $\ell>1$ ("trocear en subintervalos de longitud 1 y sumar"): cada subintervalo unitario paga su propio término de error: $M\le\rho\ell+C_0L\lceil\ell\rceil$. Con $\ell\le M/(2\rho)$: $M\le M\bigl(\tfrac12+\tfrac{C_0L}{2\rho}\bigr)+C_0L=M\bigl(\tfrac12+2\pi C_0\bigr)+C_0L$, **vacuo en cuanto $C_0\ge\frac1{4\pi}$** — y $C_0$ no es elegible: es la constante verdadera del error RvM. El doc sumó los $\rho|J|$ pero olvidó que el término $C_0L$ se paga POR SUBINTERVALO.
- Contramodelo semántico que sella la refutación: un reticulado a paso exactamente $\frac1{2\rho}$ de longitud arbitraria $\ell$ satisface (RvM-t) en toda ventana ($2\rho\delta\le\rho\delta+C_0L$ ⟺ $\rho\delta\le C_0L$, cierto para $\delta\le1$ si $C_0\ge\frac1{4\pi}$) y tiene $M=2\rho\ell$ **sin cota en $L$**. (RvM-t) en el umbral $\frac1{2\rho}$ **no prohíbe bloques largos**; solo lo haría con umbral de gap $\le c/L$ con $c\ll C_0^{-1}$... que cambia las constantes de todo lo que siguiera.

**Impacto aguas abajo — verificado: NULO.** El Teorema 178.4 cita $M_0=2C_0L+2$ pero **no usa el Lema 178.3**: usa (i) $d_m\ge mg$ para $m\le M_0$ (del gap mínimo, no de 178.3) y (ii) $d_m\ge(m-C_0L)/\rho$ directamente de (RvM-t) (para $d_m>1$: cubrimiento diádico, $d_m\ge c(m-C_0L)/L$, que cambia $C\rho^2$ por $CL^2\cdot\frac1{C_0L}\le CL\le C\rho^2$ en la cola — absorbe ✓). $M_0$ es solo un índice de corte libre. El lema es decorativo; su refutación no propaga.

**Veredicto: REFUTADO** (superviviente: la versión vacua "$M\le2\rho$ ⟹ $M\le2C_0L+2$"). **E-187.1.** Debe retirarse del doc o reescribirse como observación de corte de índice.

### 1.4. [Thm 178.4 / 178.4′] crecimiento sub-difusivo — DEGRADADO a CERTIFICADO-CON-ERRATA (parche de borde pendiente)

**(a) Núcleo del argumento — verificado.** Cadena cercana: $d_m\ge mg$ ⟹ $\sum_{m\le M_0}\frac{2}{d_m(d_m+g)}\le\frac2{g^2}\sum_{m\le M_0}\frac1{m(m+1)}=\frac2{g^2}\bigl(1-\frac1{M_0+1}\bigr)$ ✓ (telescópica parcial). Cola vía RvM-t ✓ (con la corrección diádica de §1.3, mismo orden). Derivada: $2g\dot g\ge8-2g^2S\ge\frac8{M_0+1}-2C\rho^2g^2$ ✓. Integración con Danskin sobre el mínimo de finitas funciones analíticas ✓. Techo $\frac{c_2}{\rho^2L}$ ✓.

**(b) AGUJERO DE BORDE (ataque obligatorio del mandato, confirmado).** $g_*$ es el mínimo sobre la ventana $|\cdot-\gamma|\le5$, pero el par minimizador puede estar a distancia $<2$ del borde, con ceros **justo fuera de $\pm5$ comprimidos por debajo de $g_*$** (la hipótesis (R) garantiza realidad en $\pm10$, NO gaps $\ge g_*$ en $(5,10]$). Entonces $d_m\ge mg$ FALLA para los primeros $m$ del lado del borde y la suma sensible puede exceder $\frac4{g^2}$: tal como está escrito ("mientras los ceros estén en la ventana"), el paso no está justificado. **Reparación estándar existente:** los ceros a distancia $\ge2$ del par contribuyen $\le C\rho^2$ por RvM-t diádico (insensibles a $g$); solo importa el gap-control en un entorno de radio $2$ del par minimizador ⟹ basta un enunciado de dos ventanas (mínimo sobre $\pm5$, control heredado en $\pm7$ vía tomar $g_*$ sobre $\pm7$ y concluir para pares en $\pm5$) o una penalización de borde. Es un parche de media página, pero **no está en el doc**.

**(c) Álgebra de la banda — verificada exacta.** $g_{\rm norm}^2=g^2\rho^2\ge c\,tL$; $tL\ge t^{2\theta_2}\iff L\ge t^{-(1-2\theta_2)}$ ✓; techo no alcanzado $\iff tL^2\le c\iff L\le ct^{-1/2}$ ✓; banda no vacía $\iff\theta_2>\frac14$ ✓; $\theta_1=2\theta_2-\frac12$: $1-2\theta_2=\frac12-\theta_1$ ✓; en el borde superior $g_{\rm norm}\ge ct^{1/4}\ge ct^{\theta_2}$ ✓; $t\le C'L^{-2}$ automática en la banda ($tL^2\le c$) ✓.

**(d) Compatibilidad arquitectónica con 177.7 (ataque del mandato).** El uso de 177.B en el Thm 177.7 es **justo después de un aterrizaje**, donde (R) en $[t/2,t]$ FALLA por construcción (había ceros no reales hasta $t_c$). Luego 178.4′ **no puede sustituir** a 177.B en el Cor 177.8 — y el doc **no lo pretende**: declara explícitamente que "toda la carga queda en la realidad local" y desplaza esa carga a la vía 3. No hay circularidad; hay complementariedad exacta de regímenes (178.4′ cubre donde no hubo aterrizaje; 177.7 explota el aterrizaje). Limpio. ✓

**Veredicto: CERTIFICADO-CON-ERRATA** (E-187.2: borde de ventana; reparable, mecanismo central sano), condicional a (RvM-t)+(R) como declara. Clasificación: COERCIVO condicional.

### 1.5. [Lema 178.6] deriva horizontal — DEGRADADO

Dos defectos:
1. **La prueba contiene una elipsis literal** ("aportan $\le CL\cdot2^r\cdot$... y la suma..."): viola el contrato del propio documento ([LEMA] solo con prueba completa).
2. **La cota de velocidad $|\dot x|\le C\log^2\gamma$ es FALSA como enunciado** en las hipótesis dadas: el compañero del cero a distancia $g$ aporta $2/g$ **sin cancelación** (la "cancelación par-a-par" solo opera entre ceros lejanos simetrizados), y dentro de (R) no hay cota inferior a priori de $g$ — para un gap recién abierto $g\asymp\sqrt{t-t_c}$, $2/g$ es arbitrariamente grande.

**Superviviente:** lo que el Teorema 178.4 necesita no es la velocidad sino el **desplazamiento**: para el par estrecho, $\int_s^t\frac{dt'}{g(t')}\le\int_s^t\frac{dt'}{\sqrt{c(t'-s)/L}}\asymp\sqrt{L(t-s)}\le\sqrt{L\cdot C'L^{-2}}=O(L^{-1/2})$ — pequeño (usando el propio crecimiento $g^2\ge c(t'-s)/L$, bootstrap legítimo); el resto del mar sí da $O(L^2)$ de velocidad y $O(1)$ de desplazamiento en tiempo $L^{-2}$. La conclusión "las ventanas son consistentes" se salva; el enunciado debe reescribirse en términos de desplazamiento. **E-187.3.**

**Veredicto: DEGRADADO** (versión superviviente: desplazamiento $O(1)$ en tiempo $\le C'L^{-2}$, prueba por bootstrap a redactar). Clasificación: COERCIVO auxiliar.

### 1.6. [Puente 178.5 / GAP-178.A] — estatus honesto ✓

(RvM-t) está declarado como GAP de literatura, marcado en cada uso. Nada que destruir; la auditoría añade (de §1.3) que **el valor de $C_0$ importa más de lo que el doc cree**: cualquier cierre futuro de GAP-178.A debe dar $C_0$ explícito porque los umbrales de gap del tipo $\frac1{2\rho}$ interactúan con $C_0$ (la refutación de 178.3 es la demostración).

### 1.7. [Thm 178.7] — CERTIFICADO-CON-ERRATA

Álgebra verificada: en la banda $L\ge t^{-(1/2-\theta_1)}$ ⟹ $t\ge L^{-2/(1-2\theta_1)}\ge2\Lambda_{\rm loc}$ por $(\ast)$ ⟹ (R) en $[t/2,t]$ ✓; $\theta_2=\frac{\theta_1}2+\frac14$ consistente con §1.4(c) ✓. **Errata:** la Def 178.6′ usa ventana $\pm5$ y la hipótesis (R) de 178.4 exige $\pm10$ — desajuste. Reparación trivial: $(\ast)$ es uniforme en $\gamma$, luego $\Lambda_{\rm loc}(\gamma-5)\vee\Lambda_{\rm loc}(\gamma+5)$ cubre $\pm10$ por unión de ventanas. **E-187.4.** Clasificación: MIXTO (puente dinámica↔estática, condicional).

### 1.8. [Prop 178.8] — CERTIFICADO-CON-ERRATA (dependencia de conteo escondida)

**(1) verificado.** Tras aterrizar en $(t_c,\gamma_c)$, a tiempo $t_c+\delta$ hay gap real $g_{\rm norm}\le C\sqrt\delta\log\gamma_c$ a altura $\gamma_c+O(1)$ (pliegue / abanico Hermite). $\Gamma$ es decreciente en $t$, luego $\gamma_c\ge\Gamma(t_c)\Rightarrow\gamma_c\ge\Gamma(t_c+\delta)$ y 177.B aplica: $C\sqrt\delta\log\gamma_c\ge c\,t_c^\theta>0$ para todo $\delta$ pequeño — contradicción en $\delta\to0^+$ ✓. Reordenado: $t_c\le(\log\gamma_c)^{-2/(1-2\theta)}$ ✓. Aterrizaje garantizado a $t\le\Lambda\le0.22<1$ ✓.

**(2) verificado con reserva.** $b^2\le2n^2t_c(1+C\varepsilon)$ + dicotomía: si $n\le2$, $b\le C(\log\gamma)^{-1/(1-2\theta)}$ ✓; si $n>2$, $n\le C\sqrt\tau\log\gamma=C(\log\gamma)^{1-\frac1{1-2\theta}}$ y el exponente $1-\frac1{1-2\theta}=-\frac{2\theta}{1-2\theta}<0$ ⟹ $n\to0$, absurdo ✓ — **el auto-mejoramiento $n\le2$ es álgebra legítima**. PERO: la cota $n\le\max(2,C\sqrt{t_c}\log\gamma)$ es un **insumo de conteo** (número de ceros en ventana de radio $\asymp\sqrt{t_c}$ de la $H_t$ aritmética), importado de D177. La etiqueta "incondicional (no usa (RvM-t))" de §3.3 es entonces **demasiado fuerte**: la dirección B no usa el (RvM-t) de §2.3 *tal cual*, pero usa un conteo del mismo género vía D177. Si el conteo de D177 es a su vez condicional o del mismo GAP, 178.8(2) hereda la condición. **E-187.5** (matizar la etiqueta; auditar la procedencia exacta en D177 — fuera del alcance de esta sesión por backward-only sobre los dos objetos del mandato).

**Cartas (ataque del mandato):** D178 mezcla cartas en §0 — "Re $z=\gamma$" es la carta $\Xi$ pero $\rho=\frac{\log\gamma}{4\pi}$ es la densidad de la carta $H$ ($z_H=2z_\Xi$: densidad $\frac{\log\gamma}{2\pi}\cdot\frac12$). Factor 2 en $\rho$. Verificado que **no daña**: todas las conclusiones de 178.8–178.11 tienen constantes libres y los exponentes son invariantes de carta ($b\mapsto2b$, $t\mapsto4t$, $\log\gamma\mapsto\log\gamma+O(1)$; la ley $b^2=ct$ es invariante bajo $(2b)^2=c\cdot4t$ ✓ — verificado a mano). **E-187.6** (cosmética con potencial de mordedura futura si alguien fija constantes).

**Veredicto: CERTIFICADO-CON-ERRATA.** Clasificación: COERCIVO (la ida dinámica→estática; el contenido real del documento).

### 1.9. [Cor 178.9] calibración — CERTIFICADO (condicional a 178.8)

La comparación con Vinogradov–Korobov es correcta (VK = franja junto a $\sigma=1$, i.e. $b\le\frac12-c(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$; confinamiento = tubo en el centro: objetos incomparablemente más fuertes) ✓. La lógica "si 177.B estuviera en la literatura, el confinamiento sería teorema — y no lo es" es válida dado 178.8 ✓. La explicación de por qué KKL/P15 tienen umbrales no uniformes en $t$ es ahora un teorema de imposibilidad, no una queja bibliográfica: pieza valiosa. Hereda E-187.5. Clasificación: CORRELACIONAL (calibración de dureza; no avanza, mide).

### 1.10. [Thm 178.10] "equivalencia" — DEGRADADO (la vuelta no cierra el círculo cuantitativamente)

Este es el segundo hallazgo destructivo. Reconstrucción de los dos sentidos:

- **Ida** (177.B ⟹ confinamiento): es 178.8, verificada (mod E-187.5). Pérdida de exponente explícita ✓.
- **Vuelta** (confinamiento ⟹ 177.B): la implicación intermedia (confinamiento ⟹ $\Lambda_{\rm loc}\le C'L^{-2-\eta'}$) está bien probada ($\dot\beta\le-\frac1{2\beta}$ válido porque $\beta\le CL^{-1-\eta}\ll\frac1\rho$ ✓; $t_c\le\beta(0)^2$ ✓; entrada horizontal cubierta por la deriva — hereda E-187.3 en versión desplazamiento, OK). Pero el destino es 177.B **solo en la banda sub-difusiva** $\log\gamma\le ct^{-1/2}$ (vía 178.7+178.4′, condicional a (RvM-t)).

**La pregunta que el doc no se hace y la auditoría sí: ¿la versión-banda de 177.B reinyectada en el argumento 177.7/178.8 recupera el confinamiento?** NO. Reconstrucción: con 177.B-banda, la contradicción del pliegue en 178.8(1) solo opera cuando el punto de aplicación $(t_c+\delta,\gamma_c)$ cae en la banda, i.e. $\log\gamma_c\le ct_c^{-1/2}$. Quedan sin prohibir los aterrizajes con $\log\gamma_c>ct_c^{-1/2}$, i.e. $t_c\le c(\log\gamma_c)^{-2}$, que vía $b^2\le2n^2t_c$ dan solo $b\le C/\log\gamma$ — **exactamente la escala de LP-134, sin el margen $\eta$**: la pinza $b\ge c/\log\gamma$ vs $b\le C/\log\gamma$ **no cierra** (constante contra constante, lado malo). Es decir:

$$\text{177.B}\;\Longrightarrow\;\text{178.C}\;\Longrightarrow\;\text{177.B-banda}\;\Longrightarrow\;b\le C/\log\gamma\;\not\Longrightarrow\;\text{178.C}.$$

El círculo pierde el exponente $\eta$ en cada vuelta. 178.10 es: **ida completa + vuelta estrictamente parcial**. El propio doc dice "restringido a su banda útil", pero el adjetivo "útil" es el que cae: la banda NO es la parte que usa 177.7 en el caso general (el régimen del enemigo de la esquina, $t_j\ll t_{\rm dif}$, es justamente $\log\gamma_j\gg t_j^{-1/2}$ — fuera de la banda, como el propio diccionario 179.4 hace evidente). Llamarlo "⟺" es inflación.

**Lo que sobrevive — y es lo que importa:** (i) la **calibración** (178.9) solo necesita la ida → intacta; (ii) la **deflación de la torre 2** no pasa por la vuelta (ver 1.11) → intacta; (iii) el enunciado correcto de 178.10 es: "177.B ⟹ 178.C; y 178.C ⟹ 177.B-en-la-banda-sub-difusiva (mod (RvM-t)). En particular 177.B y 178.C son inter-reducibles módulo la zona super-difusiva [GAP-178.B]". **Pregunta del director ("¿revive 177.B como decidible si 178.10 cae?"): NO** — la ida sola (178.8/178.9) ya lo calibra cuasi-RH-difícil; la caída de la vuelta solo retira la elegancia, no la calibración. 177.B sigue muerto como "lema de literatura".

**Veredicto: DEGRADADO** (versión superviviente arriba). Clasificación: la **ida es COERCIVA** (transporta moneda dinámica → moneda estática con pérdida explícita: dos monedas genuinamente distintas, gaps de $H_t$ en $t>0$ vs posiciones de ceros de $H_0$); la **vuelta es MIXTA-parcial**; el "⟺" del titular es ½ renombre. Respuesta a la pregunta despiadada: 178.10-ida tiene contenido real (no es renombre: el lado izquierdo habla de $t>0$, el derecho de $t=0$, y el puente es el pliegue + la cota de despegue — mecanismo, no relabeling); el "⟺" como tal es marketing.

### 1.11. [Cor 178.11] pinza estática — CERTIFICADO

Verificación de "sin dinámica escondida": la prueba usa SOLO las dos desigualdades $b_j\ge c/\log\gamma_j$ (LP-134) y $b_j\le C(\log\gamma_j)^{-1-\eta}$ (178.C) e incompatibilidad para $\gamma_j\to\infty$ ✓ — aritmética de exponentes pura, ninguna apelación al flujo, a (RvM-t), a (R) ni a 177.B. El flujo es genealogía, no premisa. ✓ Observación de la auditoría que el doc no registra: **basta LP-134∞** (solo se necesita la incompatibilidad en infinitos $j$... de hecho en UNO por cada cola), lo que D179 §1 confirma después; la pinza es entonces 178.C ∧ LP-134∞ ⟹ $m<\infty$ — la forma óptima de la torre 2. El "auto-mejoramiento $n\le2$ gratis" pertenece a 178.8(2) (donde es legítimo, §1.8), no a 178.11, que no menciona $n$: la frase del veredicto de D178 está bien dirigida.

**Veredicto: CERTIFICADO.** Clasificación: REDUNDANTE-lógico (modus tollens inmediato de sus dos premisas) pero arquitectónicamente central: es la deflación misma. La auditoría confirma que la deflación de la torre 2 a pinza estática ES legítima — condicionada solo a la honestidad de la genealogía (la ida de 178.10, que sobrevive).

---

## 2. Auditoría de D179

### 2.1. [Prop 179.2] jerarquía y forma mínima — CERTIFICADO-CON-ERRATA

**Suficiencia (2) — cuantificadores verificados (ataque del mandato):** la conclusión de 177.7(2) tal como se cita es "$b_j\log\gamma_j\le(\log\gamma_j)^{-\eta}$ para TODO $j$ grande", i.e. $b_j\log\gamma_j\to0$ sobre toda la sucesión. La negación exacta de esa convergencia es "∃c>0 con $b_j\log\gamma_j\ge c$ infinitas veces" = LP-134∞ ✓. La contradicción necesita un solo testigo por cola: limpio. **Condicional a que 177.7(2) realmente concluya para todo $j$ grande** — la cita es consistente con el uso que D178 §3.3 hace del mismo teorema; aceptado como prerrequisito.

**Separadores de la jerarquía — errata reparable:** el separador (a) usa $b_j=\frac14$ en $j=2^k$, con $\sum b_j=\infty$, mientras la flexibilidad citada de 141.R2 pide "$\sum b_j$ controlada". La legitimación indirecta vía 141.P1(b) ($b_j\equiv\frac14$ admisible) probablemente lo cubre, pero si la construcción exigiera $\sum b_j<\infty$, la reparación es inmediata: tomar $b_j=1/\log\gamma_j$ en $j=2^k$ ($\gamma_j=2^j$ ⟹ $\sum_k\frac1{2^k\log2}<\infty$ ✓ y $b_j\log\gamma_j=1$ infinitas veces ✓). Separador (b) análogo. **E-187.8.** (c) es cita directa ✓.

**Veredicto: CERTIFICADO-CON-ERRATA.** Clasificación: REDUNDANTE (lógica de cuantificadores) con separadores CORRELACIONALES; valor real = identificación de la forma mínima, que es genuina.

### 2.2. [Prop 179.3] CSV complejo — CERTIFICADO

Dirección de la palanca contra CSV (ataque del mandato): Csordas–Smith–Varga prueban "par de Lehmer ⟹ cota INFERIOR de $\Lambda$" — hacia arriba. 179.3 es la versión compleja del mismo sentido: cuádruplo off ⟹ $\Lambda\ge t_c\ge\frac{b^2}{2n^2}(1-C\varepsilon)$. $\Lambda\ge t_c$ es por definición (ceros no reales para $t<t_c$) ✓; la cota de $t_c$ es 177.6 leído forward, citado ✓. **Cartas verificadas a mano:** la ley $b^2\le2n^2t_c$ es invariante bajo $(b,t)\mapsto(2b,4t)$ — $(2b)^2\le2n^2(4t)$ ⟺ $b^2\le2n^2t$ ✓; la declaración de D179 §0 ("las leyes $\beta^2=ct$ son invariantes de carta") es correcta, y es la razón por la que la mezcla de cartas de D178 (E-187.6) no muerde aquí. La lectura de saturación (la palanca trabaja hacia arriba; LP-134 necesita una prohibición hacia abajo; el techo $\Lambda\le0.22$ da $b\le n\sqrt{0.44}$, vacuo) es exacta y honesta ✓.

**Veredicto: CERTIFICADO.** Clasificación: CORRELACIONAL (puente exacto pero saturado; el doc lo dice él mismo).

### 2.3. [Thm 179.4] diccionario difusivo — CERTIFICADO-CON-ERRATA (cuantificación del caso no aislado correcta pero el titular debe llevarla pegada)

**(1)** Álgebra: $b_j^2\le2n_j^2t_j(1+C\varepsilon)$ ⟹ $t_j\ge\frac{(b_j\log\gamma_j)^2}{2n_j^2}(\log\gamma_j)^{-2}(1-C\varepsilon)$ ✓; con testigos $b_j\log\gamma_j\ge c$ y $n_j\le n_0$: $t_j\ge c't_{\rm dif}$ ✓. Nótese: (1) da solo UNA dirección y **requiere $n_j\le n_0$ en la subsucesión testigo** — hipótesis no removida.

**(2)** El "⟺" exacto vale SOLO bajo aislamiento ($n_j=2$, mar a distancia $\gg\sqrt{t_j}$), que es **hipótesis del enunciado**, no conclusión: dentro de ella, $t_j=\frac12b_j^2(1+o(1))$ ⟹ $\frac{t_j}{t_{\rm dif}}=\frac12(b_j\log\gamma_j)^2(1+o(1))$ y "$\limsup>0$ ⟺ $\ge c$ i.v." es insensible a constantes (lo que también neutraliza el descuido de las constantes $4\pi$ en $t_{\rm dif}:=(\log\gamma)^{-2}$ y los factores de carta — verificado: el cociente $t_j/t_{\rm dif}$ es invariante de carta, $t\mapsto4t$, espaciado$^2\mapsto4\,$espaciado$^2$) ✓. La cláusula "autoconsistente en ⟸" usa "genéricamente $n_j=2$" — palabra-comadreja, pero inocua porque el aislamiento ya está asumido en el enunciado de (2). **El veredicto §7.2 de D179 cuantifica honestamente** ("bajo las hipótesis de cluster del 177.6 y exactamente para aislados") — el mandato preguntaba si la cuantificación es honesta: SÍ, en el veredicto; el titular suelto "LP-134∞ ⟺ no todos los aterrizajes son sub-difusivos" debe llevar siempre la cláusula.

**Pregunta despiadada del director (¿dos monedas o la misma?): LA MISMA.** Dado el modelo del cuádruplo (174.4/177.6), $t_j$ y $b_j$ son la misma cantidad en dos cartas ($t_j=\frac12b_j^2$): 179.4 es un **cambio de variables**, no un teorema-puente entre monedas independientes (contrástese con la ida de 178.10, que sí cruza de $t>0$ a $t=0$ vía el pliegue). Su valor es organizador (el eje único $t_j/t_{\rm dif}$ para las dos mitades de la torre), no probatorio. Todo el contenido no trivial vive en 174.4/177.6, que están aguas arriba.

**Veredicto: CERTIFICADO-CON-ERRATA** (cláusula de aislamiento pegada al titular; "genéricamente" eliminado o degradado a observación). Clasificación: **REDUNDANTE-organizador** (renombre con valor de arquitectura; el propio doc lo roza al decir "consistencia obligada, no nueva información" respecto de 177.7).

### 2.4. [Prop 179.5] inevitabilidad — DEGRADADO

El punto exacto que el mandato ordenaba atacar, y el ataque conecta. La proposición necesita que la configuración de Hadamard satisfaga **todas** las premisas candidatas, incluida 177.B. Lo que el doc ofrece para 177.B es el ítem (iv): "consistente con el Lema 177.B (verificación de doble consistencia del Doc 177 §4.3: sus aterrizajes ocurren muy por debajo del umbral $\Gamma(t_j)$)". Reconstrucción del contenido de esa verificación: con $b_j=e^{-\gamma_j}$, $t_j\asymp b_j^2$, y $\Gamma(t_j)=\exp(t_j^{-(1/2-\theta)})\ggg\gamma_j$: los gaps pequeños creados por SUS aterrizajes están a alturas $\ll\Gamma$ — es decir, **los aterrizajes no violan 177.B**. Pero 177.B es un enunciado universal sobre TODOS los gaps de ceros reales de la $H_t$ de la configuración a alturas $\ge\Gamma(t)$: para afirmarlo hay que controlar también la evolución del mar real (ceros en los puntos RvM exactos) — que los gaps $g_{\rm norm}\asymp1$ iniciales no se compriman por debajo de $ct^\theta$ bajo el flujo. Plausible (reticulado casi estacionario, Prop 178.2; compresión acotada por el mar), **pero no construido ni probado en D179 ni —por lo citado— en D177 §4.3, que verifica consistencia, no validez**. "Consistente con 177.B" ≠ "satisface 177.B". La distinción es exactamente la que separa un teorema de inevitabilidad de una heurística de inevitabilidad.

**Versión superviviente:** *"Ninguna combinación de las leyes dinámicas certificadas (balance, coercividad, presupuesto de vidas, 177.6) puede reemplazar a LP-134∞ en el Cor 177.8"* — esto SÍ está probado (las verificaciones (i)–(iii) son cálculos citados de 174 §3.3, y los cuatro ítems 1–4 de §4 de D179 están bien hechos: el presupuesto converge violentamente ✓, la coercividad es ciega en $t\to0^+$ ✓, el balance ídem ✓, los testigos degeneran con $b_0\to0$ ✓ — reconstruidos, correctos). *Con 177.B en la lista, la inevitabilidad es CONDICIONAL a verificar que la $H_t$ de Hadamard satisface 177.B* (verosímil; tarea concreta: correr 178.4 sobre la configuración, donde (RvM-t) vale por construcción y (R) vale fuera de los aterrizajes — media sesión).

**¿Qué rutas reabren con la degradación?** En principio, la ruta "probar una 177.B-fuerte tal que 177.B ∧ leyes-de-clase ⟹ $m<\infty$ sin aritmética". Pero la auditoría la cierra por otro lado: por 178.8 (certificado), 177.B implica confinamiento de los ceros de ζ — cuasi-RH; cualquier ruta que empiece "probar 177.B" está calibrada como casi-circular **independientemente de 179.5**. La reapertura es académica. La frase del veredicto de D179 ("convertimos 'no se nos ocurre' en 'es imposible'") debe rebajarse a "es imposible para las leyes dinámicas; para la lista con 177.B, condicional".

**Veredicto: DEGRADADO** (superviviente arriba). **E-187.7-bis** registrada como tarea. Clasificación: MIXTO (núcleo coercivo probado + cláusula 177.B heurística).

### 2.5. Vías 1, 2 y 4 de D179 (§2.1, §3, §5) — CERTIFICADAS como consolidaciones

- §2.1 (ceguera de la industria de densidad): consolidación de resultados citados, sin pasos nuevos que auditar; la lectura de 170.5 (holgura infinita bajo ¬LP-134∞) es correcta. ✓
- §3 (Jensen/discriminante): el cálculo $\frac{2b^2}{w(w^2-b^2)}\asymp b^2/|w|^3$ vs ruido $O(\log\gamma)$ ⟹ resolución $|w|\lesssim b^{2/3}L^{-1/3}$ — verificado ($b^2/|w|^3\ge L\iff|w|\le b^{2/3}L^{-1/3}$ ✓). El [GAP-179.B] (Liouville para el discriminante de ξ) está honestamente declarado como ausente incluso conjeturalmente. ✓
- §5.1: **errata** — "¬LP-134∞ fuerza $\sum b_j^2<\infty$" es falsa sin tasa de crecimiento de $\gamma_j$ (contraejemplo: $\gamma_j=e^{\sqrt j}$, $\varepsilon_j=1/\log j$: $\sum\varepsilon_j^2/j$ converge... tómese $\varepsilon_j\to0$ tan lento que $\sum\varepsilon_j^2(\log\gamma_j)^{-2}=\sum\varepsilon_j^2/j=\infty$ — posible). El propio paréntesis del doc contiene la corrección ("convergente si $\gamma_j\gg e^{j^{1/2+}}$"); el enunciado principal debe llevar la condición. Sin impacto: el uso (compatibilidad con 170.5 y con Littlewood) solo necesita la versión de la esquina (γ superexponenciales), donde es cierta. **E-187.7.**
- §5.2 + [GAP-179.A]: la observación de que la señal del enemigo mínimo es $o((b_jL_j)^2)\to0$ — i.e. que debilitar la hipótesis ENCARECE la verificación analítica — es correcta y es la moraleja estructural honesta del documento. ✓
- [Conj 179.6]: registro limpio, sin pretensión de progreso. ✓

---

## 3. Tabla final de veredictos

| Pieza | Veredicto | Clasificación | Notas |
|---|---|---|---|
| Lema 178.1 (ODE del gap) | **CERTIFICADO** | COERCIVO | complejos bien aislados en $\mathcal E$ |
| Prop 178.2 (saturación reticulado) | **CERTIFICADO** | CORRELACIONAL (no-go) | telescópica y signo del calor verificados |
| Lema 178.3 (bloques cortos) | **REFUTADO** | — | troceo no cierra; reticulado a paso $\frac1{2\rho}$ es RvM-t-consistente; **sin impacto: 178.4 no lo usa** (E-187.1) |
| Thm 178.4/178.4′ | **CERTIFICADO-CON-ERRATA** | COERCIVO condicional | agujero de borde reparable (E-187.2); banda exacta ✓ |
| Lema 178.6 (deriva) | **DEGRADADO** | COERCIVO auxiliar | velocidad falsa; desplazamiento $O(1)$ recuperable (E-187.3) |
| Puente 178.5 / GAP-178.A | estatus honesto | — | $C_0$ explícito ahora obligatorio (lección de 178.3) |
| Thm 178.7 | **CERTIFICADO-CON-ERRATA** | MIXTO | ventanas ±5/±10 (E-187.4) |
| Prop 178.8 | **CERTIFICADO-CON-ERRATA** | COERCIVO | "incondicional" matizado: insumo de conteo $n\le C\sqrt t\log\gamma$ (E-187.5); $n\le2$ legítimo |
| Cor 178.9 (calibración) | **CERTIFICADO** (cond. 178.8) | CORRELACIONAL | VK-comparación correcta |
| Thm 178.10 ("⟺") | **DEGRADADO** | ida COERCIVA / vuelta MIXTA-parcial | vuelta solo en banda; reinyectada pierde $\eta$: $b\le C/\log\gamma$, pinza no cierra. Superviviente: ida + inter-reducibilidad mod zona super-difusiva |
| Cor 178.11 (pinza estática) | **CERTIFICADO** | REDUNDANTE-lógico, arquitectónicamente central | sin dinámica escondida ✓; basta LP-134∞ |
| Prop 179.2 (forma mínima) | **CERTIFICADO-CON-ERRATA** | REDUNDANTE + separadores CORRELACIONALES | separador (a) reparable con $b_j=1/\log\gamma_j$ (E-187.8) |
| Prop 179.3 (CSV complejo) | **CERTIFICADO** | CORRELACIONAL (saturado) | cartas invariantes verificadas |
| Thm 179.4 (diccionario) | **CERTIFICADO-CON-ERRATA** | REDUNDANTE-organizador | misma moneda (cambio de variables vía 174.4); cláusula de aislamiento obligatoria en el titular |
| Prop 179.5 (inevitabilidad) | **DEGRADADO** | MIXTO | superviviente: imposibilidad para leyes dinámicas; con 177.B en la lista: condicional a verificar 177.B en la config (no hecho) |
| GAP-179.A / 179.B / Conj 179.6 | bien planteados | — | honestidad confirmada |

## 4. Impacto aguas abajo

1. **La deflación de la torre 2 SOBREVIVE:** $m<\infty\Longleftarrow$ 178.C ∧ LP-134∞ (Cor 178.11, certificado, estático, y con la mejora ∞ de 179.2). Es el resultado neto firme del par D178/D179.
2. **¿Revive 177.B como decidible al caer la vuelta de 178.10? NO.** La ida (178.8, certificada mod E-187.5) basta para calibrarlo cuasi-RH-difícil; el Cor 178.9 queda en pie. Lo único que se pierde es el "⟺" como identidad conceptual exacta: 177.B podría ser estrictamente más fuerte que 178.C (por la zona super-difusiva, GAP-178.B) — pero más fuerte que cuasi-RH sigue siendo cuasi-RH.
3. **La degradación de 179.5 reabre formalmente** la ruta "177.B-fuerte + leyes de clase sin aritmética", pero la calibración del punto 2 la cierra en la práctica: probar 177.B ya es probar confinamiento. Tarea concreta y barata para restaurar 179.5 completo: correr 178.4 sobre la $H_t$ de Hadamard (RvM-t vale por construcción) y verificar sus gaps $\ge ct^\theta$ fuera de los aterrizajes.
4. **La refutación de 178.3 no propaga** (178.4 no lo usa), pero deja una lección de método para GAP-178.A: la constante $C_0$ de (RvM-t) no es decorativa — los umbrales de gap del género $\frac1{2\rho}$ interactúan con ella, y cualquier cierre futuro debe hacerla explícita.
5. **Las erratas de carta (E-187.6) son hoy inocuas** porque todos los enunciados llevan constantes libres y los exponentes son invariantes; serán letales el día que alguien fije una constante numérica (p.ej. en una pinza constante-contra-constante como la del final de §1.10). Recomendación: D178 debe declarar una carta única en §0.

## 5. Erratas

- **E-187.1** [D178, Lema 178.3] El parche "trocear y sumar" omite que el error $C_0L$ se paga por subintervalo: para $\ell>1$ la cuenta da $M\le M(\frac12+2\pi C_0)+C_0L$, vacua si $C_0\ge\frac1{4\pi}$. Contramodelo: reticulado a paso $\frac1{2\rho}$ de longitud arbitraria, RvM-t-consistente. REFUTADO; retirar o reducir a definición del índice $M_0$. Sin impacto en 178.4.
- **E-187.2** [D178, Thm 178.4] Borde de ventana: el par minimizador puede estar a distancia $<2$ del borde de $\pm5$ con ceros comprimidos en $(5,10]$ donde no rige el gap mínimo; $d_m\ge mg$ no justificado ahí. Parche estándar: solo los ceros a distancia $\le2$ del par son $g$-sensibles (el resto absorbe en $C\rho^2$); enunciado de dos ventanas.
- **E-187.3** [D178, Lema 178.6] Prueba con elipsis (viola el contrato) y cota de velocidad $CL^2$ falsa para pares estrechos (término $4/g$ sin cancelación). Reescribir como cota de desplazamiento $O(1)$ vía bootstrap $g^2\ge c(t'-s)/L$.
- **E-187.4** [D178, Thm 178.7 / Def 178.6′] Ventana $\pm5$ de $\Lambda_{\rm loc}$ vs $\pm10$ de (R). Reparación: unión de ventanas usando $(\ast)$ uniforme en $\gamma$.
- **E-187.5** [D178, §3.3/Prop 178.8] La etiqueta "incondicional (no usa (RvM-t))" omite que $n\le\max(2,C\sqrt{t_c}\log\gamma)$ es un insumo de conteo importado de D177, del mismo género. Matizar y auditar su procedencia en D177.
- **E-187.6** [D178, §0] Mezcla de cartas: "Re $z=\gamma$" (carta Ξ) vs $\rho=\frac{\log\gamma}{4\pi}$ (densidad de la carta H): factor 2 en $\rho$. Hoy solo constantes; declarar carta única.
- **E-187.7** [D179, §5.1] "¬LP-134∞ ⟹ $\sum b_j^2<\infty$" falsa sin tasa de $\gamma_j$; condicionar a $\gamma_j$ superexponenciales (como el propio paréntesis ya hace).
- **E-187.8** [D179, Prop 179.2] Separadores (a)/(b) con $b_j=\frac14$ i.v. ⟹ $\sum b_j=\infty$, en tensión con la flexibilidad citada de 141.R2; reparación: $b_j=1/\log\gamma_j$ en $j=2^k$ ($\sum<\infty$ ✓, $b_j\log\gamma_j=1$ i.v. ✓).

## 6. Clasificación estructural (síntesis para el director)

- **COERCIVO genuino:** 178.1, 178.4 (condicional), la **ida** de 178.10 (=178.8). Es el contenido real de la sesión D178: dinámica → estática vía el pliegue, con pérdida de exponentes explícita.
- **CORRELACIONAL:** 178.2, 178.9, 179.3 (calibraciones y no-gos; miden, no empujan).
- **MIXTO:** 178.7, la vuelta de 178.10, 179.5 (núcleo probado + cláusula heurística).
- **REDUNDANTE:** 178.11 (modus tollens — pero ES la deflación, redundante≠inútil), 179.2 (lógica), 179.4 (cambio de variables vía 174.4: misma moneda, valor organizador).
- **Respuestas a las preguntas despiadadas:** 178.10-ida es teorema con contenido (cruza de $t>0$ a $t=0$); el "⟺" es ½ renombre y debe degradarse en los titulares. 179.4 conecta la misma moneda consigo misma en dos cartas; su valor es el eje común $t_j/t_{\rm dif}$, no una prueba.

**Cuenta de la fase: 2 piezas REFUTADAS/DEGRADADAS-fuertes sobre ~16 auditadas (178.3, 178.10-como-equivalencia) + 1 degradación media (179.5) — dentro de la tasa histórica de ~1/4. El esqueleto de la torre 2 (178.C ∧ LP-134∞ ⟹ m<∞, con 177.B calibrado cuasi-RH) queda CERTIFICADO.**
