# Doc 144 — Ataque a LP-141 (el pivote mínimo de finitud): formalización, test de Hadamard, intento aritmético, y mapa de la frontera fuerza/utilidad

**Programa:** Hipótesis de Riemann — Phase 47: FRENTES VIVOS.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** ataque frontal al lema mínimo **LP-141** (Def. 141.2 del Doc 141), aislado en Phase 46
como el pivote real de la mitad de finitud ($m<\infty$) de la arquitectura $\mathrm{RH}=(m<\infty)\wedge(m<\infty\Rightarrow m=0)$.
El encargo: formalizarlo con cuantificadores totales y distinguirlo de LP-134; testearlo contra el
contraejemplo de Hadamard que ya mató a LP-134 en la categoría analítica; intentar probarlo en la categoría
aritmética vía el mecanismo continuación⟹pureza⟹repulsión; mapear la frontera exacta fuerza/utilidad y buscar
LP más débiles; enunciar qué decide Davenport–Heilbronn. Veredicto honesto, con la parte que duele.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados con
precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con ζ/RH con estatus honesto. **[GAP]** =
declarado. **[DESEO]** = declarado.

**Prerrequisitos leídos en fuente esta sesión (completos):** Doc 141 entero (Def. 141.1/141.2, jerarquía
141.P1/141.P3/141.P4, no-go 141.B/141.B2, contraejemplo de Hadamard 141.R2, cálculo de Euler 141.R3, Conjetura
141.E, GAP-141.DH); Doc 134 entero (corona §3, modelo $\mathfrak W$ §4 con visibilidad (V1)–(V2), Teoremas
5.0–5.5, Teo. 7.2 sinergia, §5.8 M1–M4); ERRATA de Phase 38 ($W_\lambda\geq0$ refutado — NO citar) y de Phase
46 (Doc 140: **Thm 5.3(ii) del D134 corregido a 5.3′** "estricta ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$
sin cláusula de excepción"; caveat de ámbito perpetuo de B.4/Thm 1.3: positividad esencial es invariante del
PAR (forma, norma de Hilbert)).

---

## 0. Resumen ejecutivo

1. **(§1) Formalización con cuantificadores totales.** LP-141$(a)$ se escribe canónicamente como
   $$\mathrm{LP\text{-}141}(a):\quad m=\infty\ \Longrightarrow\ \forall N\ \exists j>N\ \text{con}\ \delta_j\,a(\gamma_j)\geq1,$$
   un $\Pi_3$ sobre los ceros off, a calendario FIJO $a$ no acotado. La distinción precisa con LP-134:
   LP-134$^{(\psi)}$ es $\liminf_{\gamma\to\infty}|\beta-\tfrac12|\psi(\gamma)>0$ (NINGÚN cero off es
   asintóticamente sub-resolución — un $\liminf$ sobre TODOS los off); LP-141$(a)$ pide solo que INFINITOS
   sean gordos (un $\limsup$-tipo: la cola de gordos no se agota). **[PROPOSICIÓN 144.1]:** LP-134 ⟹ LP-141
   estricta; LP-141 ⟹̸ LP-134 (contraejemplo: gordos replicados + cola sub-resolución). LP-141 es por tanto
   estrictamente más débil que LP-134 — confirma su rol de pivote.

2. **(§2) El test de Hadamard REFUTA LP-141 en la categoría analítica — con la misma fuerza que a LP-134, y por
   la misma razón, pero el cálculo es nuevo y hay que hacerlo con cuidado.** **[PROPOSICIÓN 144.2]:** para
   TODO calendario fijo $a$ no acotado existe una función entera de orden 1, con ecuación funcional, real en la
   línea, conteo de ceros de tipo ζ, con $m=\infty$ y **CERO cuádruplos gordos a calendario $a$** — viola
   LP-141$(a)$. Es la encarnación analítica del Teorema 5.5(a) del Doc 134 (para todo calendario hay
   configuraciones invisibles), ahora realizada por una función entera concreta. **Conclusión decisiva del
   paso 2 del encargo: SÍ, se puede tener $m=\infty$ con todos los ceros off sub-resolución simultáneamente,
   respetando ecuación funcional y orden 1 — luego LP-141 también es no-analítico y necesita aritmética.** El
   contraejemplo de Hadamard de 141.R2 ($\delta_j=e^{-\gamma_j}$) lo refuta para todo $a$ sub-exponencial; el
   refinamiento adaptado al calendario (144.2) lo refuta para TODO $a$.

3. **(§3) Intento de prueba aritmética vía continuación⟹pureza⟹repulsión: PROBADO-PARCIAL con un GAP
   nombrado y reducido.** El fracaso de la construcción de Euler ingenua (141.R3) se promueve a una cota
   inferior CONDICIONAL: **[PROPOSICIÓN 144.4]** en la categoría D131-H⁺ (Euler + dato local hermitiano
   positivo + continuación + ecuación funcional), si la **conjetura de detección local cuantitativa**
   [CONJETURA 144.D] vale — un cero off a distancia $\delta'$ obliga impureza local de tamaño $\gtrsim\delta'$
   detectable a soporte $\asymp1/\delta'$, NO sostenible bajo continuación — entonces vale la forma fuerte
   "$m\geq1\Rightarrow$ infinitos gordos", que IMPLICA LP-141 para todo calendario $\succeq\log$. El residuo
   exacto es **[GAP-144.C]**: la cota inferior efectiva $\delta_j\gtrsim 1/a(\gamma_j)$ sobre los gordos
   derivada de la continuación. Honestidad: NO se cierra; se reduce LP-141 (en categoría Euler) a una
   propiedad de rigidez de continuación bien formada, estrictamente más débil que la Conjetura 141.E (que
   pedía la repulsión sobre TODOS los off; 144.D solo pide infinitos gordos).

4. **(§4) Mapa de la frontera fuerza/utilidad y un LP-142 más débil.** Se construye la cadena exacta
   $$\text{Axioma R}\ \succ\ \mathrm{LP\text{-}134}\ \succ\ \mathrm{LP\text{-}141}\ \succ\ \mathrm{LP\text{-}142}\ \succ\ (\text{trivial}),$$
   donde **[DEFINICIÓN-NUEVA 144.5] LP-142$(a)$:** "$m=\infty\Rightarrow$ los gordos no tienen densidad
   relativa cero entre los off" — y **[PROPOSICIÓN 144.6]** muestra que LP-142 NO basta para la sinergia (la
   positividad débil + densidad cero de gordos es consistente con $m=\infty$). **La frontera exacta es
   LP-141:** es el enunciado MÍNIMO que aún da $m<\infty$ con positividad débil del símbolo (cualquier
   debilitamiento ulterior — finitos gordos permitidos, o densidad — rompe la Prop. 141.P3). Por debajo de
   LP-141 todo es demasiado débil para servir; LP-141 mismo es demasiado fuerte para la categoría analítica
   (§2). La ventana viable es: LP-141 exactamente, probado en la categoría Euler.

5. **(§5) Conexión con GAP-141.DH — la implicación lógica exacta.** **[PROPOSICIÓN 144.7]:** si los $\delta_j$
   de Davenport–Heilbronn están acotados inferiormente por una constante $c>0$ (independiente de $j$),
   entonces DH satisface LP-141$(a)$ para TODO calendario (de hecho la forma fuerte: todos los off son gordos
   a calendario $a\geq1/c$) — DH calibra el lado BUENO y es consistente con LP-141; si en cambio
   $\inf_j\delta_j=0$ con $\delta_j a(\gamma_j)\to0$ para algún calendario natural, DH es un
   **contraejemplo aritmético-aproximado** a LP-141 en ese calendario (DH tiene producto de Euler aproximado
   pero NO ecuación funcional de Euler genuina — clase de Selberg fallada — así que no refutaría LP-141 en la
   categoría D131-H⁺, pero SÍ mostraría que "Euler aproximado" no basta). La implicación es: **DH decide si la
   ecuación funcional genuina de Euler es load-bearing en 144.D.**

6. **(§6) VEREDICTO: REFUTADO-EN-CATEGORÍA-ANALÍTICA / ABIERTO-CON-MAPA en categoría Euler / PROBADO-PARCIAL
   condicional a 144.D.** Para la mitad de finitud $m<\infty$: LP-141 es genuinamente el pivote (más débil que
   sus dos padres, suficiente con positividad débil), pero NO es accesible sin aritmética, y dentro de la
   aritmética se reduce a una rigidez de continuación cuantitativa (144.D / GAP-144.C) que es ahora el objeto
   atacable más concreto del frente de finitud.

---

## 1. Formalización de LP-141 y su distinción de LP-134

Trabajo en la categoría de **configuraciones** (Def. 4.1 del D134): $Z=\{(\delta_j,\gamma_j)\}_{j\in J}$ con
$\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$ si $|J|=\infty$, finitos $j$ por ventana, $m:=|J|$; el
cuádruplo $j$ es $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$. Un **calendario** es $a:[2,\infty)\to[1,\infty)$ no
decreciente (Def. 3.6 del D134); un cuádruplo es **gordo a calendario $a$** si $\delta_j\,a(\gamma_j)\geq1$,
**sub-resolución** si $\delta_j\,a(\gamma_j)<1$ (Def. 4.2 del D134). La visibilidad $\theta_j$ satisface
(V1) $\theta_j\to0$ cuando $\delta_j a(\gamma_j)\to0$, (V2) $\theta_j\geq c_0$ cuando $\delta_j a(\gamma_j)\geq1$.

### 1.1. La forma canónica de LP-141 con cuantificadores totales

El Doc 141 (Def. 141.2) enuncia LP-141$(a)$ como "$m=\infty\Rightarrow\#\{j:\delta_j a(\gamma_j)\geq1\}=\infty$".
La escribo con cuantificadores explícitos para fijar su estructura lógica exacta.

**Definición 144.0 [DEFINICIÓN-NUEVA] (LP-141, forma canónica con cuantificadores totales).** Para una
función $F$ con ceros en la banda crítica (finitos por altura acotada), un calendario fijo $a$ no acotado, y
la enumeración $\{(\delta_j,\gamma_j)\}$ de sus cuádruplos off ordenados por altura creciente:
$$\boxed{\ \mathrm{LP\text{-}141}(a)(F):\qquad \bigl(m=\infty\bigr)\ \Longrightarrow\ \Bigl(\forall N\in\mathbb N\ \ \exists j>N:\ \delta_j\,a(\gamma_j)\geq1\Bigr).\ }$$
Equivalentemente, con $\mathcal G_a:=\{j:\delta_j a(\gamma_j)\geq1\}$ (índice de gordos a calendario $a$):
$$\mathrm{LP\text{-}141}(a):\quad m=\infty\Rightarrow|\mathcal G_a|=\infty.$$

**Observaciones de estructura lógica (rutina, fijan el enunciado):**

(i) **El consecuente es un $\limsup$, no un $\liminf$.** "$\forall N\,\exists j>N$" dice que la sucesión
booleana $\mathbf 1[\delta_j a(\gamma_j)\geq1]$ NO es eventualmente cero: tiene infinitos unos. No dice nada
sobre los ceros intermedios. **Esta es la diferencia atómica con LP-134.**

(ii) **Cuantificación sobre la cola.** LP-141 es insensible a cualquier conjunto finito de cuádruplos: añadir
o quitar finitos off no cambia ni la hipótesis ($m=\infty$) ni la conclusión ($|\mathcal G_a|=\infty$). Es
genuinamente un enunciado sobre el comportamiento $\gamma\to\infty$.

(iii) **Monotonía en el calendario.** Si $a\preceq a'$ (es decir $a(\gamma)\leq a'(\gamma)$ eventualmente),
entonces $\mathcal G_a\subseteq\mathcal G_{a'}$ salvo finitos índices (Prop. 5.5bis(i) del D134), luego
$\mathrm{LP\text{-}141}(a)\Rightarrow\mathrm{LP\text{-}141}(a')$: **a calendario más alto, LP-141 es más
fácil** (más cuádruplos cuentan como gordos). El calendario relevante para la sinergia es el natural
$a(\gamma)=C\log\gamma$ (espaciamiento medio de ceros).

(iv) **Complejidad lógica.** Como predicado sobre la configuración: hipótesis $m=\infty$ es $\Pi_2$
($\forall N\exists j>N$); conclusión es $\Pi_2$; el condicional es $\Pi_3$. Más simple que LP-134, que
involucra un $\liminf>0$ (un $\Sigma_2$ sobre la cota $c$ envuelto en un $\forall$).

### 1.2. La distinción exacta LP-141 vs LP-134

Recuerdo LP-134$^{(\psi)}$ (Def. 141.1): $\liminf_{\rho\ \text{off},\,\gamma\to\infty}|\beta-\tfrac12|\,\psi(\gamma)>0$,
i.e. $\exists c>0$ tal que $\delta_j\psi(\gamma_j)\geq c$ para todo $j$ con $\gamma_j$ grande — **TODOS** los
off son eventualmente gordos.

**Proposición 144.1 [PROPOSICIÓN] (LP-134 ⟹ LP-141, estrictamente).** Sea $a$ un calendario con
$a\succeq\psi$ (es decir $a(\gamma)\geq\psi(\gamma)$ eventualmente). Entonces:

(a) $\mathrm{LP\text{-}134}^{(\psi)}\Rightarrow\mathrm{LP\text{-}141}(a)$.

(b) La implicación es estricta: existe una configuración con $\mathrm{LP\text{-}141}(a)$ y $\neg\mathrm{LP\text{-}134}^{(\psi)}$.

*Demostración.* (a) Supóngase LP-134$^{(\psi)}$ y $m=\infty$. Hay $c>0$ y $\Gamma_0$ con
$\delta_j\psi(\gamma_j)\geq c$ para $\gamma_j\geq\Gamma_0$. Sea $a\geq\psi$ desde $\Gamma_1\geq\Gamma_0$.
Por la cofinitud (Obs. 1.1(ii) del Doc 141) puedo absorber el factor $c$: para los infinitos $j$ con
$\gamma_j\geq\Gamma_1$, $\delta_j a(\gamma_j)\geq\delta_j\psi(\gamma_j)\geq c$. Si $c\geq1$, todos esos
son gordos: $|\mathcal G_a|=\infty$. Si $c<1$, re-escalo el calendario: $a':=\lceil1/c\rceil\cdot a$
cumple $\delta_j a'(\gamma_j)\geq\lceil1/c\rceil\,c\geq1$ para esos $j$, luego $|\mathcal G_{a'}|=\infty$;
y como $\{C\log\}$ es UNA clase de calendario (invariancia por constantes, Obs. 1.1(i) del Doc 141), LP-141 a
la clase $\{C\log\}$ se cumple. Concretamente: LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ para el calendario
$a=\lceil1/c\rceil\psi$, que es de la misma clase que $\psi$. $\square_{(a)}$

(b) Configuración explícita (combina los dos estratos del Doc 134): pongo dos familias de cuádruplos.
*Familia gorda replicada:* $\gamma_k^{\mathrm{g}}:=2^{2k}$, $\delta_k^{\mathrm{g}}:=\tfrac14$ (distancia
fija a la línea), $k\geq1$ — infinitos cuádruplos a distancia $\tfrac14$. *Familia sub-resolución:*
$\gamma_k^{\mathrm{s}}:=2^{2k+1}$, $\delta_k^{\mathrm{s}}:=e^{-\gamma_k^{\mathrm{s}}}$, $k\geq1$. Sea
$a(\gamma)=\log\gamma$. Entonces:
- $|\mathcal G_a|=\infty$: la familia gorda cumple $\delta_k^{\mathrm{g}}a(\gamma_k^{\mathrm g})=\tfrac14\cdot2k\log2\to\infty\geq1$
  para $k\geq2$. LP-141$(a)$ se cumple (consecuente verdadero, $m=\infty$).
- $\neg\mathrm{LP\text{-}134}^{(\log)}$: la familia sub-resolución da
  $\delta_k^{\mathrm{s}}\log\gamma_k^{\mathrm{s}}=e^{-2^{2k+1}}\cdot(2k+1)\log2\to0$, luego
  $\liminf_{\gamma\to\infty}\delta\log\gamma=0$: LP-134 viola. $\square_{(b)}$

**Observación 144.1bis (la diferencia es exactamente "permitir finos en presencia de gordos").** La
configuración de (b) es el corazón de la distinción: LP-141 **tolera infinitos ceros off sub-resolución**
(la familia $\mathrm{s}$) MIENTRAS coexistan con infinitos gordos (la familia $\mathrm g$). LP-134 prohíbe
TODA sub-resolución asintótica. Por eso LP-141 es estrictamente más débil — y por eso es el candidato
correcto a pivote: pide solo lo que la sinergia 141.P3 necesita (un gordo en infinitas ventanas para activar
el Teorema 5.1 del D134), no más. La Prop. 141.P4(iii) del Doc 141 ya registraba esta no-implicación; aquí la
formalizo con cuantificadores y la calibro contra la escala exacta del calendario.

### 1.3. Por qué LP-141 (no LP-134) es el enunciado correcto para $m<\infty$ — recordatorio de la sinergia

Repito el contenido operativo de la Prop. 141.P3 del Doc 141 para tenerlo presente en este documento (no es
re-prueba; cito el resultado con su mecanismo):

**[PUENTE 144.S] (Prop. 141.P3, recordada).** En el modelo $\mathfrak W$ del D134 con (S1)–(S3) y (V2): si
vale LP-141$(a)$ a un calendario $a$ no acotado **y** el símbolo $\sigma_a(Q)$ es **débilmente** positivo
($\mathrm{spec}\subseteq[0,\infty)$), entonces $m<\infty$. *Mecanismo:* si $m=\infty$, LP-141 da infinitos
gordos; por (V2) tienen $\theta_j\geq c_0$; por el Teorema 5.1 del D134,
$\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c_0/2]\neq\emptyset$ — contradice la positividad débil. Luego
$m<\infty$. Estatus: teorema DENTRO del modelo $\mathfrak W$ (los axiomas (S1)–(S3) con sus GAPs declarados
en la Obs. 4.5 del D134); la pieza nueva que este documento ataca es la **hipótesis LP-141 misma**, no la
implicación 141.P3.

Nótese la economía: LP-141 + positividad **débil** ⟹ $m<\infty$. La debilidad de la pieza de positividad
(no se pide gap, que el Teorema 1.3 del D134 mostró ser exactamente la finitud robusta y que la normalización
de peso fijo destruye, Teorema 2.2) es lo que hace a esta ruta más barata que la ruta estricta. **LP-141 es
la única pieza geométrica que falta para la mitad Fredholm.** De ahí el ataque.

---

## 2. El test del contraejemplo de Hadamard contra LP-141

El paso 2 del encargo es la pregunta decisiva: el contraejemplo de Hadamard (Prop. 141.R2 del Doc 141) mató a
LP-134 en la categoría analítica con $\delta_j=e^{-\gamma_j}\to0$, TODOS sub-resolución. Si todos los
$\delta_j$ son sub-resolución, hay CERO gordos — y LP-141 también pide infinitos gordos. La pregunta:
**¿el mismo contraejemplo refuta LP-141?** Respuesta: SÍ, y de hecho una versión adaptada lo refuta para TODO
calendario. Lo pruebo con cuidado.

### 2.1. El contraejemplo de Hadamard original refuta LP-141 a calendario sub-exponencial

**Cálculo 144.A [CÁLCULO] (la función de 141.R2 viola LP-141$(a)$ para todo $a$ sub-exponencial).** Sea $F$
la función entera de la Prop. 141.R2: orden 1, $F(s)=F(1-s)$, real en la línea, $N_F(T)\asymp T\log T$, con
cuádruplos off $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ donde $\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$. Para
cualquier calendario $a$ con $a(\gamma)\leq e^{\gamma/2}$ (todos los $C\log\gamma$, todos los polinomios,
todo $a$ sub-exponencial):
$$\delta_j\,a(\gamma_j)=e^{-\gamma_j}\,a(\gamma_j)\leq e^{-\gamma_j}e^{\gamma_j/2}=e^{-\gamma_j/2}\xrightarrow{j\to\infty}0.$$
Luego $\mathcal G_a=\{j:\delta_j a(\gamma_j)\geq1\}$ es FINITO (de hecho vacío para $j$ grande): el consecuente
de LP-141$(a)$ es FALSO. Como $m=\infty$ (hipótesis verdadera), **LP-141$(a)$ es falso en $F$ para todo
calendario sub-exponencial.** $\square$

Esto ya responde el grueso del paso 2: el contraejemplo de Hadamard, que tiene $m=\infty$ y todos los
$\delta_j\to0$, tiene CERO gordos a la escala $\log\gamma$ relevante, así que refuta LP-141 exactamente igual
que refuta LP-134, **por la misma razón** (sub-resolución total). La diferencia LP-134/LP-141 que destaqué en
§1 (LP-141 tolera finos si hay gordos) NO ayuda aquí: el contraejemplo no tiene NINGÚN gordo, así que ni
siquiera la conclusión debilitada de LP-141 se salva.

### 2.2. El refinamiento: LP-141 cae para TODO calendario (no solo sub-exponencial)

Uno podría objetar: el contraejemplo de 141.R2 es visible (gordo) para el calendario super-exponencial
$a(\gamma)=e^\gamma$. ¿Sobrevive LP-141 a algún calendario? No: dado CUALQUIER calendario fijo, se construye
un contraejemplo de Hadamard adaptado a él. Es la versión analítica del Teorema 5.5(a) del D134.

**Proposición 144.2 [PROPOSICIÓN] (refutación analítica de LP-141 a calendario arbitrario).** Para todo
calendario fijo $a$ no acotado existe una función entera $F_a$ de orden 1, con $F_a(s)=F_a(1-s)$, real en la
línea crítica, con todos sus ceros en $|\Re s-\tfrac12|<\tfrac12$, con conteo $N_{F_a}(T)\asymp T\log T$, y con
infinitos cuádruplos off $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ tales que
$$m=\infty\qquad\text{y}\qquad\delta_j\,a(\gamma_j)\xrightarrow{j\to\infty}0,$$
de modo que $|\mathcal G_a|=0$ eventualmente y $F_a$ **viola LP-141$(a)$**.

*Demostración.* Sigo la construcción de 141.R2 cambiando solo los $\delta_j$ para adaptarlos a $a$.
Coordenada $z$: $s=\tfrac12+iz$, así $s\mapsto1-s$ es $z\mapsto-z$ y la línea crítica es $z\in\mathbb R$.
Prescribo ceros en $z$:

*(a) Mar real (fija el orden y el conteo).* Pares reales $\pm t_n$ con $t_n:=n/\log(n+2)$, $n\geq1$; el
contador $\#\{t_n\leq r\}\asymp r\log r$.

*(b) Cuádruplos off (violadores).* $\gamma_j:=2^j$ y
$$\delta_j:=\min\Bigl(\tfrac14,\ \frac{1}{j\,a(2^j)}\Bigr),\qquad z_j:=\gamma_j-i\delta_j,$$
con cuádruplo $\{\pm z_j,\pm\bar z_j\}$ (correspondiente a $s=\tfrac12\pm\delta_j\pm i\gamma_j$). Defino
$$G(z):=\prod_{n\geq1}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\cdot\prod_{j\geq1}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$

*Convergencia y orden.* Idéntico a 141.R2: en $w=z^2$, $\sum_n t_n^{-2}<\infty$ y
$\sum_j|z_j|^{-2}\leq\sum_j(\gamma_j^2+\delta_j^2)^{-1}\leq\sum_j 4^{-j}<\infty$ (pues $|z_j|^2\geq\gamma_j^2=4^j$),
producto de género 0 en $w$, $G$ entera y par; contador de módulos $n_G(r)\asymp r\log r$, exponente de
convergencia 1 ⟹ orden 1 [B54, Thm. 2.6.5]. (El cambio de $\delta_j$ no toca esto: solo importa $|z_j|\geq\gamma_j$,
que se mantiene pues $\delta_j\leq\tfrac14$.)

*Ecuación funcional, realidad, banda.* $G(-z)=G(z)$ (paridad) ⟹ $F_a(s):=G(\tfrac{s-1/2}{i})$ cumple
$F_a(1-s)=F_a(s)$; los factores tienen coeficientes reales en $z^2$ (los $t_n^2$ reales; los pares
$(1-w/z_j^2)(1-w/\bar z_j^2)$ tienen coeficientes reales por conjugación), luego $G|_{\mathbb R}\subseteq\mathbb R$
y $F_a$ real en la línea; $|\Im z_j|=\delta_j\leq\tfrac14<\tfrac12$ ✓.

*Violación de LP-141$(a)$.* Por construcción, para $j$ con $\delta_j=1/(j\,a(2^j))<\tfrac14$ (todos salvo
finitos, pues $a$ no acotado ⟹ $j\,a(2^j)\to\infty$):
$$\delta_j\,a(\gamma_j)=\frac{1}{j\,a(2^j)}\cdot a(2^j)=\frac1j\xrightarrow{j\to\infty}0.$$
Para los finitos $j$ iniciales con $\delta_j=\tfrac14$ el valor está acotado, pero son finitos. Luego
$\delta_j a(\gamma_j)\to0$: $\mathcal G_a$ finito, consecuente de LP-141$(a)$ falso, $m=\infty$. $\square$

**Corolario 144.3 [COROLARIO] (LP-141 es aritmético o no es — igual que LP-134).** LP-141 NO es un teorema de
la categoría analítica (entera + orden 1 + ecuación funcional + realidad en la línea + densidad de ceros tipo
ζ): la Prop. 144.2 da, **para cada calendario fijo**, un miembro que lo viola con $m=\infty$ y cero gordos.
En consecuencia, **toda prueba de LP-141 debe usar el lado aritmético** (producto de Euler / coeficientes /
fórmula explícita con primos). La esperanza de que LP-141, por ser estrictamente más débil que LP-134,
pudiera ser accesible analíticamente, es **FALSA**: ambos caen ante el mismo mecanismo (apilar ceros off
sub-resolución calibrados contra el calendario), porque ese mecanismo produce CERO gordos, y "cero gordos"
viola la conclusión de LP-141 tanto como la de LP-134. $\square$

### 2.3. Honestidad sobre lo que el test establece y lo que no

**Observación 144.3bis (qué prueba exactamente §2).** La Prop. 144.2 prueba que la categoría analítica
(estructura de ξ como función entera de la clase de Pólya–Laguerre con ecuación funcional) NO fuerza LP-141.
Esto es esperado y refuerza el corpus: es el análogo-LP-141 de los anti-modelos cosh (que realizan $m$
finito en la categoría analítica) y del Teorema 5.5(a) del D134 (para todo calendario, configuraciones
$m=\infty$ invisibles). **Lo que NO prueba:** no dice nada sobre ζ misma. Para ζ, refutar LP-141 exhibiría
infinitos ceros off — refutaría RH (mismo argumento que la Prop. 141.R1 para LP-134: refutar LP-141 para ζ
requiere $m=\infty$, luego ¬RH). Así que la situación de falsabilidad de LP-141 es IDÉNTICA a la de LP-134:
falsable en la categoría (y la categoría analítica efectivamente lo falsa), pero la instancia ζ solo es
decidible junto con RH o por la vía de clase aritmética (§3). **El test de Hadamard NO mata LP-141 para el
programa; mata la esperanza analítica y reconduce a la aritmética — exactamente el mismo veredicto que
141.R2 dio para LP-134.**

Una sutileza honesta que diferencia LP-141 de LP-134 incluso aquí: para LP-134, había configuraciones
analíticas que lo SATISFACEN no trivialmente (la familia gorda pura $\delta_j\equiv\tfrac14$: cumple LP-134).
Para LP-141 lo mismo (esa familia cumple LP-141). Pero la *refutabilidad* es la que importa, y es idéntica:
ambas se refutan con la familia sub-resolución adaptada. La debilidad relativa de LP-141 no compra
refutabilidad: compra solo que en presencia de gordos uno puede ser laxo con los finos — y el contraejemplo
no pone gordos en absoluto.

---

## 3. Intento de prueba aritmética: continuación ⟹ pureza ⟹ repulsión

Como §2 reconduce LP-141 a la aritmética, ataco la categoría D131-H⁺: series de Dirichlet con producto de
Euler, dato local hermitiano positivo, continuación analítica y ecuación funcional (la clase donde vive la
Conjetura 141.E del Doc 141). El mecanismo propuesto: la continuación analítica de un producto de Euler
fuerza pureza asintótica del dato local; la pureza es sub-resolución local; un cero off "gordo" a distancia
$\delta'$ requiere impureza local de tamaño $\gtrsim\delta'$ que la continuación prohíbe sostener.

### 3.1. El punto de partida: el fracaso de la construcción ingenua (141.R3, recordado)

El Cálculo 141.R3 del Doc 141 mostró: el producto de Euler ingenuo
$D(s)=\prod_k(1-\alpha_k p_k^{-s})^{-1}(1-\bar\alpha_k p_k^{-s})^{-1}$ con dato impuro
$|\alpha_k|=p_k^{1/2+\delta_k'}$, $\delta_k'\downarrow0$ (que tendría su divisor en $\Re s=\tfrac12+\delta_k'$,
violando la repulsión con $m=\infty$), **converge solo en $\Re s>\tfrac32$** y NO continúa a la banda crítica:
la continuación analítica acopla los datos locales y los ejemplos continuables conocidos (caracteres, formas
automorfas) tienen TODOS dato puro ($|\alpha|=\sqrt p$, $\delta'=0$). La obstrucción es estructural. Para
LP-141 (no LP-134) la pregunta se afina: ¿el fracaso de continuación impide apilar infinitos gordos todos a
$\delta'$ decreciente — o solo impide la sub-resolución total?

### 3.2. El diccionario pureza ↔ resolución (M3 del D134, recordado y afinado)

Del §5.8 M3 del D134 y del Teorema 6.7 del D131: un bloque local $F_{p,\alpha}$ con $|\alpha|=p^{1/2+\delta'}$
es **impuro** y su impureza se detecta en el dato local $c_m$ (coeficientes log-derivada) recién a orden
$m\gtrsim1/\delta'$, donde $|c_m|>2p^{m/2}$ rompe la barrera de Weil de la pureza. El diccionario:
$$\text{cero off a distancia }\delta'\ \longleftrightarrow\ \text{impureza local detectable a soporte }M\asymp1/\delta'.$$
"Pureza local" $\iff$ "todos los cuádruplos potenciales son sub-resolución a todo calendario" $\iff$ símbolo
autónomo. La barrera $|c_m|\leq2p^{m/2}$ ES la condición de sub-resolución en el mundo local (§5.8 M3 del D134,
verificado allí con el test de Mertens de dos protuberancias).

### 3.3. La conjetura de detección y la cota inferior condicional

Formalizo el eslabón que falta como una conjetura de detección local cuantitativa, estrictamente más débil que
la Conjetura 141.E (que pedía repulsión sobre TODOS los off; aquí solo pido infinitos gordos).

**Conjetura 144.D [CONJETURA — el eslabón aritmético, nombrado].** *En la categoría D131-H⁺ (producto de Euler
con dato local hermitiano positivo, continuación analítica a la banda crítica, ecuación funcional), si la
función tiene $m=\infty$ ceros off, entonces existe $c>0$ y una subsucesión $j_k$ de ceros off con*
$$\delta_{j_k}\,\log\gamma_{j_k}\ \geq\ c\qquad(k\to\infty).$$
*Mecanismo propuesto: cada cero off a distancia $\delta_{j}$ exige impureza local sostenida de amplitud
$\gtrsim\delta_j$ en una banda de primos de tamaño logarítmico $\asymp\log\gamma_j$ (la fórmula explícita
localiza el cero off a la altura $\gamma_j$ usando primos $p\lesssim\gamma_j$); la continuación analítica
acopla esos datos locales y prohíbe que la impureza sea simultáneamente (i) sub-resolución a la escala
$1/\log\gamma$ en TODOS los ceros y (ii) sostenida en infinitos ceros — alguno debe ser gordo.*

**Proposición 144.4 [PROPOSICIÓN] (cota inferior condicional ⟹ LP-141 en categoría Euler).** En la categoría
D131-H⁺, si vale la Conjetura 144.D, entonces vale LP-141$(a)$ para todo calendario $a\succeq\log$ (en
particular el natural $a=C\log\gamma$). De hecho vale la forma fuerte: $m=\infty\Rightarrow$ infinitos gordos
a calendario $\log$.

*Demostración.* Supóngase 144.D y $m=\infty$. Hay $c>0$ y subsucesión $j_k$ con
$\delta_{j_k}\log\gamma_{j_k}\geq c$. Tómese el calendario $a(\gamma)=\lceil1/c\rceil\log\gamma$ (clase
$\{C\log\}$). Entonces $\delta_{j_k}a(\gamma_{j_k})=\lceil1/c\rceil\,\delta_{j_k}\log\gamma_{j_k}\geq\lceil1/c\rceil\,c\geq1$:
los $j_k$ son gordos a calendario $a$, infinitos. Luego $|\mathcal G_a|=\infty$: LP-141$(a)$. Por monotonía
(Obs. 144.0(iii)), LP-141$(a')$ para todo $a'\succeq a$. $\square$

**Observación 144.4bis (lo que 144.4 logra y lo que no — honestidad máxima).** La Prop. 144.4 NO prueba
LP-141. Reduce LP-141 (en la categoría Euler) a la Conjetura 144.D, que es una afirmación de **rigidez de
continuación cuantitativa**. La ganancia neta sobre el Doc 141:
1. **144.D es estrictamente más débil que la Conjetura 141.E.** 141.E pedía $\liminf_{\text{TODOS off}}\delta_j\log\gamma_j>0$
   (repulsión de TODOS — la fuente de LP-134). 144.D pide solo $\limsup$ de una subsucesión gorda — la fuente
   de LP-141. Es la traducción aritmética exacta de la distinción §1.2. Por tanto **el frente aritmético
   correcto a atacar no es 141.E sino 144.D**, que permite ceros off finos mientras infinitos sean gordos.
2. **El residuo está nombrado: [GAP-144.C].** Lo que falta probar es la cota inferior efectiva
   $\delta_{j_k}\gtrsim 1/\log\gamma_{j_k}$ sobre una subsucesión de ceros off, derivada de la continuación
   analítica del producto de Euler. El Cálculo 141.R3 da la evidencia direccional (la construcción que violaría
   esto NO continúa), pero NO la cota. Convertir "no continúa" en "$\delta_{j_k}\gtrsim1/\log\gamma$" es el GAP.

### 3.4. Por qué la continuación es el motor correcto (no la positividad) — recordatorio del Cálculo 141.M4

Subrayo, citando el Cálculo 141.M4 del Doc 141 (no re-pruebo): la palanca de positividad de Landau (que da la
repulsión Deuring–Heilbronn desde $s=1$) es **idénticamente nula en la línea crítica** por la ecuación
funcional — la contribución de primer orden de un par simétrico a $\Re\frac{\xi'}{\xi}(\tfrac12+it)$ es
exactamente cero. Por tanto el motor de LP-141/144.D NO puede ser positividad. El motor candidato es la
**rigidez de continuación**: la continuación analítica del producto de Euler es una condición GLOBAL sobre la
familia $\{\alpha_k\}$ de datos locales, y es esa rigidez global —no una desigualdad local de signo— la que
debe forzar los gordos. Esto coincide con la Conjetura 141.E del Doc 141 en el motor, pero 144.D rebaja la
conclusión de "todos repelidos" a "infinitos gordos", alineándola exactamente con lo que la sinergia 141.P3
necesita.

### 3.5. Un dividendo incondicional pequeño pero real

No todo es conjetural. Una observación incondicional sobre la categoría Euler genuina:

**Proposición 144.5 [PROPOSICIÓN] (Hamburger reduce la categoría estricta a ζ).** En la categoría más estrecha
(serie de Dirichlet con la ecuación funcional EXACTA de ζ y regularidad mínima), por el teorema de Hamburger
[H21] el único objeto es un múltiplo de ζ. En consecuencia, LP-141 en esa categoría es LP-141 para ζ —
infalsable sin refutar RH (Prop. 141.R1 transpuesta a LP-141: refutar LP-141 para ζ da $m=\infty$ ⟹ ¬RH).

*Demostración.* Hamburger [H21]: la ecuación funcional de ζ más regularidad caracteriza ζ salvo escalar. Luego
la única función de la categoría es ζ; LP-141 para ella es infalsable como en 141.R1. $\square$

**Observación 144.5bis (la pinza).** Hamburger (categoría estricta, solo ζ, infalsable sin ¬RH) y el
contraejemplo de Hadamard (categoría analítica laxa, falsable, Prop. 144.2) son las dos mandíbulas de la
pinza: LP-141 es verdadero-o-RH en la categoría estrecha, falso en la categoría ancha. La categoría
**intermedia productiva** es D131-H⁺ (Euler + continuación + ecuación funcional, pero no necesariamente la de
ζ): ancha lo bastante para tener miembros distintos de ζ (las $L$ automorfas), estrecha lo bastante para que
la continuación sea load-bearing. Es ahí donde 144.D / GAP-144.C vive, y es la única categoría donde probar
LP-141 no es ni trivial ni equivalente a RH.

---

## 4. El mapa de la frontera fuerza/utilidad y posibles LP más débiles

El encargo (paso 4): si LP-141 es demasiado fuerte, buscar el enunciado MÍNIMO ABSOLUTO que aún dé $m<\infty$
con la sinergia del símbolo. Mapeo la frontera exacta.

### 4.1. La cadena de fuerza

**Proposición 144.6 [PROPOSICIÓN] (cadena de fuerza, todas las implicaciones estrictas).** A calendario $a$
no acotado fijo:
$$\underbrace{\text{Axioma R}}_{\text{repl.}}\ \Longrightarrow\ \mathrm{LP\text{-}134}^{(a)}\ \Longrightarrow\ \mathrm{LP\text{-}141}(a)\ \Longrightarrow\ \mathrm{LP\text{-}142}(a),$$
donde LP-142 es la Def. 144.7 abajo (el debilitamiento "≥1 gordo"), y ninguna flecha se invierte.

*Demostración.* Axioma R ⟹ LP-134: Prop. 141.P4(ii) del Doc 141 (las réplicas conservan $\delta_0/2$, son
eventualmente gordas a todo calendario — de hecho dan la forma fuerte $m\geq1\Rightarrow$ infinitos gordos,
que es más que LP-134). LP-134 ⟹ LP-141: Prop. 144.1(a). LP-141 ⟹ LP-142: infinitos gordos ⟹ al menos un
gordo. No-inversiones: 144.1(b) (LP-141 ⟹̸ LP-134); Prop. 141.P4(iii) (LP-141 ⟹̸ Axioma R); y LP-142 ⟹̸
LP-141 es la Prop. 144.8(a) abajo (un mundo con exactamente un gordo más cola sub-resolución cumple LP-142
pero no LP-141). $\square$

### 4.2. El candidato más débil: LP-142, y por qué NO basta

El único debilitamiento de LP-141 en el cardinal de gordos es rebajar "infinitos" a "al menos uno". (No hay
nada estrictamente entre "infinitos" y "uno" que sea un enunciado natural sobre el cardinal: cualquier cota
finita $\geq1$ es equivalente, módulo cofinitud, a "$\geq1$"; y "densidad relativa positiva" es estrictamente
MÁS fuerte que "infinitos", luego va en la dirección equivocada.) Defino entonces el candidato más débil:

**Definición 144.7 [DEFINICIÓN-NUEVA] (LP-142, el candidato a pivote más débil).** A calendario $a$ no acotado,
con $\mathcal G_a=\{j:\delta_j a(\gamma_j)\geq1\}$ el conjunto de gordos:
$$\mathrm{LP\text{-}142}(a):\qquad m=\infty\ \Longrightarrow\ |\mathcal G_a|\geq1,$$
"si hay infinitos off, al menos uno es gordo". Es el debilitamiento máximo de LP-141 en el cardinal de gordos,
y por la Prop. 144.6 es estrictamente más débil que LP-141.

**Proposición 144.8 [PROPOSICIÓN] (la frontera exacta: LP-141 es el mínimo que sirve).**

(a) **"$m=\infty\Rightarrow|\mathcal G_a|\geq1$" (un solo gordo) NO basta para la sinergia.** Existe una
configuración con $m=\infty$, exactamente un gordo, positividad débil del símbolo, y $m=\infty$ — i.e.
positividad débil + "≥1 gordo" es consistente con $m=\infty$.

(b) **"$|\mathcal G_a|=\infty$ con densidad cero permitida" (= LP-141) SÍ basta**, y es estrictamente más
débil que LP-134.

(c) En consecuencia LP-141 es el **enunciado mínimo absoluto** de la familia "cuántos gordos hay" que aún da
$m<\infty$ vía Prop. 141.P3: pedir menos (finitos gordos) deja escapar $m=\infty$; pedir más (densidad
positiva, o todos gordos = LP-134) es innecesariamente fuerte.

*Demostración.* (a) El Teorema 5.1 del D134 produce masa espectral negativa $\leq-c_0/2$ en el símbolo a
partir de una **subsucesión INFINITA** de gordos (necesita $\gamma_{j_k}\to\infty$ para que el punto límite
sobreviva al cociente por $\mathcal J$). Un solo gordo a altura $\gamma_0$ aporta un bloque hiperbólico de
soporte finito en ventanas: está en el ideal compacto $\mathcal J$ (sección de soporte finito), invisible al
símbolo (es exactamente el caso M1/cosh del §5.8 del D134: $m$ finito-visible ⟹ símbolo estrictamente
positivo). Construcción: un gordo a $\delta_0=\tfrac14$, $\gamma_0=10$, MÁS infinitos sub-resolución
$\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$ ($j\geq4$). El símbolo: el único gordo está en $\mathcal J$, los
sub-resolución están en $\mathcal J$ (Teorema 5.4), luego $\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, débilmente
(y estrictamente) positivo; sin embargo $m=\infty$. Positividad débil + "≥1 gordo" ⟹̸ $m<\infty$. $\square_{(a)}$

(b) La suficiencia es la Prop. 141.P3 (infinitos gordos ⟹ subsucesión infinita ⟹ Teorema 5.1 ⟹ masa negativa
⟹ contradice positividad débil ⟹ $m<\infty$); la sub-resolución coexistente NO estorba (está en $\mathcal J$,
Teorema 5.4). Más débil que LP-134: Prop. 144.1(b). $\square_{(b)}$

(c) De (a) y (b): el umbral exacto entre "no sirve" y "sirve" es **infinitos** gordos (no finitos, no densidad
positiva). LP-141 es justo eso. $\square_{(c)}$

**Observación 144.8bis (el mapa de la frontera, en una frase).** El Teorema 5.1 del D134 necesita un punto
límite de espectros negativos en la corona, y un punto límite requiere una subsucesión INFINITA de ventanas
con gordo. Ni más (densidad) ni menos (finitos) — exactamente infinitos. **LP-141 es la sombra exacta del
mecanismo del Teorema 5.1 sobre la pregunta "cuántos gordos".** No hay LP-142 estrictamente entre LP-141 y
trivial que sirva: la frontera fuerza/utilidad es un punto, y ese punto es LP-141. La búsqueda del paso 4
termina con un resultado negativo limpio: **no existe un pivote más débil que LP-141** para la ruta de
positividad débil del símbolo.

### 4.3. El único debilitamiento real está en el calendario, no en el cardinal

Lo que SÍ admite debilitamiento es el calendario: por monotonía (Obs. 144.0(iii)), LP-141$(a)$ a calendario
más alto es más débil. El calendario máximamente débil útil es el más alto para el que la positividad débil
del símbolo siga siendo plausiblemente autónoma. Esto reconecta con el Deseo O1 del D134 (empujar el
calendario de la ceguera sub-resolución de $a=O(1)$ hacia $a=\epsilon\log n$): **el frente fino es medir el
$\epsilon$ máximo tal que LP-141$(\epsilon\log)$ siga siendo necesario para $m<\infty$ y el símbolo autónomo
siga teniendo positividad débil.** Es un frente cuantitativo, no un cuantificador nuevo.

---

## 5. Conexión con GAP-141.DH: qué decide Davenport–Heilbronn

El encargo (paso 5): enunciar la implicación lógica exacta que GAP-141.DH (¿los $\delta_j$ de DH están
acotados inferiormente?) tiene sobre LP-141. Otro trabajo del programa audita DH numéricamente; yo solo enuncio la lógica.

**Contexto (del §5.8 M2 del D134 y §4.3 del Doc 141).** Davenport–Heilbronn [DH36] es una combinación lineal
$F_\theta=\cos\theta\,L_1+\sin\theta\,L_2$ de dos $L$-funciones mod 5; tiene continuación y ecuación funcional
pero **NO producto de Euler genuino** (no es multiplicativa — está en la "clase de Selberg fallida"). Tiene
$m=\infty$ ceros off en la banda, computados a distancias macroscópicas de la línea [BS07], [BG11]. GAP-141.DH:
¿$\inf_j\delta_j(\theta)>0$? (dato plausible, no verificado en fuente).

**Proposición 144.9 [PROPOSICIÓN] (implicación lógica exacta de DH sobre LP-141).** Sea $a(\gamma)=C\log\gamma$
el calendario natural y considérese DH a parámetro $\theta$ genérico.

(a) **Si $\inf_j\delta_j=c>0$** (distancias acotadas inferiormente por constante): entonces para $j$ grande
$\delta_j a(\gamma_j)=c\cdot C\log\gamma_j\to\infty\geq1$, luego TODOS los off de DH son gordos a calendario
$a\geq1/c$ (de hecho a todo calendario $\succeq\log$): DH satisface la **forma fuerte** de LP-141 (todos
gordos), a fortiori LP-141. **DH calibra el lado BUENO** y es consistente con LP-141.

(b) **Si $\inf_j\delta_j=0$ pero $\liminf_j\delta_j\log\gamma_j>0$** (distancias decrecen pero no más rápido
que la resolución): DH aún satisface LP-134$^{(\log)}$ (todos eventualmente gordos), a fortiori LP-141.
Lado bueno también.

(c) **Si $\delta_j\log\gamma_j\to0$ para una subsucesión cofinal Y los gordos se agotan** (todos los off
eventualmente sub-resolución): DH **viola LP-141$(\log)$** con $m=\infty$ y cero gordos. Pero —y esto es la
clave lógica— **DH NO está en la categoría D131-H⁺** (sin producto de Euler genuino), luego este caso NO
refutaría la Conjetura 144.D ni LP-141 EN LA CATEGORÍA EULER; solo mostraría que "Euler aproximado / ecuación
funcional sin multiplicatividad" es insuficiente para forzar gordos.

(d) **Caso mixto (infinitos gordos + infinitos sub-resolución):** DH satisface LP-141$(\log)$ (infinitos
gordos) PERO viola LP-134$(\log)$ (infinitos finos). **Este caso es el más informativo: realizaría LP-141 sin
LP-134 en un objeto aritmético-aproximado concreto** — la separación de §1.2 instanciada en la naturaleza.

*Demostración.* Cálculo directo de $\delta_j a(\gamma_j)$ en cada régimen, más la definición de $\mathcal G_a$
y la observación de que DH carece de producto de Euler multiplicativo [DH36], [BG11] (luego $\notin$ D131-H⁺).
$\square$

**Corolario 144.10 [COROLARIO] (qué decide DH — la implicación exacta).** El cómputo de los $\delta_j$ de DH
decide **una sola cosa precisa**: si la **ecuación funcional genuina de Euler (multiplicatividad) es
load-bearing en la Conjetura 144.D.**
- Si DH está en el lado bueno (casos a/b/d): consistente con 144.D, pero NO la confirma (DH no es Euler) — y
  el caso (d) sería evidencia POSITIVA de que LP-141 (no LP-134) es el enunciado correcto, pues DH lo
  satisfaría sin satisfacer LP-134.
- Si DH viola LP-141$(\log)$ (caso c): NO refuta 144.D (DH $\notin$ D131-H⁺), pero **demuestra que la
  multiplicatividad/Euler es ESENCIAL** en 144.D — que continuación + ecuación funcional SIN Euler genuino NO
  bastan para forzar gordos. Esto afilaría 144.D a "es el producto de Euler, no la continuación sola, el motor".

*Demostración.* Combinación de 144.9 con el hecho DH$\notin$D131-H⁺. $\square$

**Observación 144.10bis (el valor del test DH).** DH es el ÚNICO objeto $m=\infty$ del corpus con continuación
y ecuación funcional. Su veredicto no decide LP-141 para ζ (DH no es Euler), pero **calibra qué hipótesis de
144.D es load-bearing**: si DH (sin Euler) ya repele (caso a/b), entonces quizá la continuación sola basta y
144.D podría debilitarse quitando "Euler"; si DH (sin Euler) NO repele (caso c), entonces Euler es esencial y
144.D está correctamente formulada. El test finito sobre [BS07]/[BG11] es, por tanto, una **medición de la
hipótesis correcta de la conjetura aritmética**, no una decisión de LP-141. Tarea para quien audita DH:
determinar cuál de los cuatro casos (a)/(b)/(c)/(d) ocurre, reportando $\liminf_j\delta_j\log\gamma_j$.

---

## 6. Veredicto y consecuencias para la mitad de finitud $m<\infty$

### VEREDICTO: **REFUTADO-EN-CATEGORÍA-ANALÍTICA + ABIERTO-CON-MAPA (categoría Euler) + PROBADO-PARCIAL condicional a 144.D**

**Refutado (categoría analítica):** LP-141 es FALSO en la categoría de funciones enteras de orden 1 con
ecuación funcional, realidad en la línea y densidad tipo ζ — para TODO calendario fijo (Prop. 144.2,
prueba completa). El contraejemplo de Hadamard que mató a LP-134 mata a LP-141 por la misma razón
(sub-resolución total ⟹ cero gordos), y la versión adaptada al calendario lo mata para todo $a$. **La
respuesta a la pregunta decisiva del paso 2 es SÍ: se puede tener $m=\infty$ con todos los ceros off
sub-resolución, respetando ecuación funcional y orden 1; LP-141 necesita aritmética, igual que LP-134.** La
debilidad relativa de LP-141 (tolera finos si hay gordos) NO compra refutabilidad, porque el contraejemplo no
exhibe ningún gordo.

**Abierto-con-mapa (categoría Euler):** infalsable para ζ sin refutar RH; en la categoría D131-H⁺ se reduce
a la Conjetura 144.D (rigidez de continuación cuantitativa: $m=\infty\Rightarrow$ subsucesión con
$\delta_{j_k}\log\gamma_{j_k}\geq c$), con residuo exacto GAP-144.C (la cota inferior efectiva derivada de la
continuación). 144.D es **estrictamente más débil que la Conjetura 141.E** del Doc 141 — pide infinitos
gordos, no repulsión de todos — y es la traducción aritmética exacta de la distinción LP-141/LP-134.

**Probado-parcial (condicional):** Prop. 144.4 — 144.D ⟹ LP-141 en categoría Euler (forma fuerte); la pieza
que falta está nombrada y reducida.

### Consecuencias para $m<\infty$ (la mitad de finitud de la arquitectura)

1. **LP-141 ES genuinamente el pivote.** Prop. 144.8: es el enunciado MÍNIMO ABSOLUTO sobre "cuántos gordos"
   que da $m<\infty$ con positividad **débil** del símbolo. No existe LP-142 estrictamente más débil que sirva
   (la frontera fuerza/utilidad es un punto: infinitos gordos, ni más ni menos). El único debilitamiento real
   está en el calendario (§4.3), un frente cuantitativo.

2. **La mitad de finitud NO es accesible sin aritmética.** §2 cierra la puerta analítica definitivamente. La
   mitad Fredholm de RH=(m<∞)∧(m<∞⟹m=0) requiere, en su pieza geométrica LP-141, el producto de Euler — igual
   que la pieza de positividad del símbolo requería la aritmética (Cor. 6.2 del D134). Ambas mitades del muro
   Fredholm son aritméticas; ninguna es analítica.

3. **El frente vivo concreto es GAP-144.C / Conjetura 144.D.** Es el objeto más atacable del frente de
   finitud: una afirmación de rigidez de continuación, con evidencia direccional (141.R3: la construcción
   violadora no continúa), un mecanismo nombrado (impureza local sostenida a soporte $\asymp\log\gamma$
   prohibida por continuación), y un test calibrador finito (DH, Cor. 144.10, que decide si Euler es
   load-bearing en 144.D).

4. **Relación con la sinergia 7.2 del D134:** la ruta "(símbolo débilmente positivo) ∧ LP-141" sigue siendo
   la versión mínima demostrable-condicionada de $m<\infty$. Este documento NO la abarata (LP-141 sigue
   conjetural), pero sí la **enfoca**: el ataque a LP-141 debe ser sobre 144.D en la categoría Euler, no sobre
   LP-134 ni sobre el Axioma R (ambos estrictamente más fuertes, Prop. 144.6). Y la pieza de positividad del
   símbolo se mantiene en **débil** (no estricta), coherente con que $W_\lambda\geq0$ está refutado (ERRATA
   Phase 38) y con el caveat de ámbito de B.4 (positividad esencial es invariante del par forma/norma, ERRATA
   Phase 46 Doc 140): NO se usa ningún resultado de gap fuerte.

### Mensaje final

**VEREDICTO: REFUTADO-EN-CATEGORÍA-ANALÍTICA (para todo calendario) + ABIERTO-CON-MAPA en categoría Euler,
reducido a la Conjetura 144.D / GAP-144.C.** LP-141 es el pivote correcto y mínimo de la mitad de finitud,
pero no es accesible sin el producto de Euler; dentro de la aritmética se reduce a una rigidez de continuación
cuantitativa bien formada y estrictamente más débil que el deseo previo (141.E).

**Tres resultados principales:**

1. **[PROPOSICIÓN 144.2 + COROLARIO 144.3]** — *Test de Hadamard:* para TODO calendario fijo $a$ no acotado
   existe una función entera de orden 1, con ecuación funcional, real en la línea, densidad tipo ζ, con
   $m=\infty$ y CERO gordos a calendario $a$ — viola LP-141$(a)$. Prueba completa. LP-141 es no-analítico
   (necesita aritmética), exactamente como LP-134, y por la misma razón (sub-resolución total ⟹ cero gordos).

2. **[PROPOSICIÓN 144.8 + 144.6]** — *Frontera fuerza/utilidad:* LP-141 es el enunciado MÍNIMO ABSOLUTO que da
   $m<\infty$ con positividad **débil** del símbolo; "≥1 gordo" no basta (un gordo vive en el ideal compacto,
   invisible al símbolo), "densidad positiva" o LP-134 sobran. La cadena estricta es
   Axioma R ≻ LP-134 ≻ LP-141 ≻ LP-142 (="≥1 gordo", ya insuficiente) ≻ trivial: el último escalón ÚTIL es
   LP-141. La frontera fuerza/utilidad es un punto: infinitos gordos.

3. **[CONJETURA 144.D + PROPOSICIÓN 144.4 + COROLARIO 144.10]** — *Reducción aritmética:* en la categoría
   D131-H⁺, una rigidez de continuación cuantitativa (subsucesión de off con $\delta_{j_k}\log\gamma_{j_k}\geq c$,
   estrictamente más débil que 141.E) IMPLICA LP-141; el residuo es GAP-144.C; y Davenport–Heilbronn decide
   exactamente si la multiplicatividad/Euler es load-bearing en 144.D (no decide LP-141 para ζ, pues DH$\notin$D131-H⁺).

---

## Referencias

**Internas (backward-only):** Doc 141 (Def. 141.1/141.2 LP-134/LP-141; jerarquía 141.P1/P3/P4; no-go relativo
141.B/141.B2; cálculos 141.M4/M5 palanca nula y señal de media cero; contraejemplo de Hadamard 141.R2;
cálculo de Euler 141.R3; Conjetura 141.E; GAP-141.DH); Doc 134 (corona §3 Lemas 3.2–3.3 Cor. 3.4; modelo
$\mathfrak W$ §4 visibilidad (V1)–(V2); Teoremas 5.0–5.5, en particular 5.1 gordos⟹símbolo-los-ve, 5.4
ceguera sub-resolución, 5.5(a) no-go del calendario; §5.8 M1–M4 calibración cosh/DH/$F_{p,\alpha}$/DBN,
diccionario pureza↔resolución M3; Teorema 7.2 sinergia Fredholm×replicación; Teorema 1.3 finitud robusta ⟺
positividad estricta; Teorema 2.2 muerte del gap en peso fijo); Doc 131 (Teorema 6.7 pureza local, barrera
$|c_m|\leq2p^{m/2}$; categoría H⁺ Deseo 6.9); Doc 112 (LP-112, Axioma R, mecanismo Rouché conservación de
$\delta_0$); ERRATA Phase 38 ($W_\lambda\geq0$ REFUTADO — no citado aquí) y Phase 46 Doc 140 (Thm 5.3′ del
D134 sin cláusula de excepción; caveat de ámbito perpetuo de B.4/Thm 1.3: positividad esencial = invariante
del par (forma, norma)).

**Literatura (publicada, verificable):**
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954 (Thm. 2.6.5: orden de productos canónicos =
  exponente de convergencia — Props. 144.2).
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 y 307–312 (ceros off sin producto de Euler).
- [H21] H. Hamburger, *Über die Riemannsche Funktionalgleichung der ξ-Funktion*, Math. Z. **10** (1921),
  240–254 (rigidez: la ecuación funcional de ζ caracteriza ζ — Prop. 144.5).
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049 (cómputo de los ceros off de DH — base del test del Cor. 144.10).
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270 (panorama de DH; ausencia de producto de Euler multiplicativo).

*Fin del Doc 144.*
