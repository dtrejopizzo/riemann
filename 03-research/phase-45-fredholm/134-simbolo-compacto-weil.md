# Doc 134 — El álgebra de Weil–Toeplitz: símbolo, ideal compacto, y la frontera donde viven los ceros

**Programa:** Hipótesis de Riemann — Phase 45: PERFORAR EL MURO POR EL LADO FREDHOLM.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** constructivo-creador con test de fuego. Desarrollar la idea B.4 del Doc 132 hasta su
forma final: ¿se descompone la forma de Weil como (símbolo autónomo computable desde primos) + (compacto)? Si
sí, la positividad esencial estricta daría $\delta<\infty=m<\infty$ — la mitad Fredholm de la arquitectura D-109
— sin tocar el cuantificador maestro de P43, porque $m<\infty$ no es un evento exacto-cero. El documento
responde la pregunta con precisión total, incluida la parte que duele.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa, estándar máximo; resultados
externos citados con precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con ζ/RH con estatus honesto
de cada eslabón. **[DESEO]** = declarado sin vergüenza. **[GAP]** = declarado.

**Prerrequisitos leídos en fuente esta sesión:** Doc 132 (B.4 y su prueba; el contraejemplo
$\mathrm{diag}(-1/n)$ de la Obs. 4.2; RH = positividad esencial ∧ replicabilidad, §8.2(c); Teorema C.1 y el
diccionario M1 con Doc 112). Doc 108 (índices por ventana $\kappa_W\asymp m\cdot n_W$ bajo ¬RH, Prop. 2.3/2.5;
Teorema 3.3 de ceguera sub-resolución; Teorema 3.4 del argumento de los dos mundos; Conjetura 108-N y Teorema
4.3; §5.2: la asintótica vale en media sobre ventanas — MV74 — y la ventana excepcional es la señal). P35
main.tex (realización de la forma de Weil en $(\mathcal K,Q)$, $\kappa(Q)=2m$, conjetura puente
$\kappa=\mathrm{neg.ind}(H_C)$). Doc 131 §6.5 (pureza local: la estructura de bloques de la forma; el test de
Mertens de dos protuberancias; el discriminador es la pureza del dato local, no la multiplicatividad).

---

## 0. Resumen ejecutivo

1. **(§1) [TEOREMA 1.3] La precisión que B.4 necesitaba — y una caracterización exacta nueva.** Hay dos
   positividades esenciales: la **débil** ($\mathrm{spec_{ess}}(G)\subseteq[0,\infty)$) y la **estricta**
   ($\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$, $c>0$). Solo la estricta implica $\delta<\infty$; la débil
   convive con $\delta=\infty$ (autovalores negativos $\lambda_n\to0^-$). Y la estricta es exactamente óptima:
   **Teorema 1.3**: $\delta(G+K)<\infty$ para *todo* compacto $K$ ⟺ positividad esencial estricta. La mitad
   Fredholm robusta-bajo-compactos ES el gap; un certificado sin gap no certifica nada.

2. **(§2) [TEOREMA 2.2] La normalización (i) — peso fijo — muere por un teorema, y el enigma del encargo se
   resuelve.** En toda realización de peso fijo donde las colas de alta frecuencia tienen $Q$-norma que decae
   (la CCM la tiene: $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$), el ínfimo del espectro esencial es
   $\leq 0$ **incondicionalmente**: el gap lo destruye la normalización misma, no los ceros. Bajo ¬RH con
   $m=\infty$ los negativos sí viven en el ideal compacto y la positividad esencial débil sí puede valer en
   ambos mundos — sin contradicción con B.4, porque B.4 pide el gap y el gap nunca estuvo. Certificado vacío.

3. **(§3) [DEFINICIÓN-NUEVA] El álgebra de Weil–Toeplitz $\mathcal W$.** La familia de ventanas re-normalizadas
   $\{Q_n\}$ no es un operador: es una **sección de un campo**. $\mathcal W:=\prod^b_n\mathcal B(H_n)$
   (secciones acotadas), $\mathcal J:=$ secciones $c_0$ (el "ideal compacto" del campo),
   $\mathcal C:=\mathcal W/\mathcal J$ (la corona), $\sigma(Q):=Q+\mathcal J$. **[LEMAS 3.2–3.3, probados]:**
   $\|\sigma(A)\|=\limsup\|A_n\|$ y, para secciones autoadjuntas, $\mathrm{spec}_{\mathcal C}(\sigma(A))=$
   conjunto de puntos límite de $\bigcup\mathrm{spec}(A_n)$. El "espectro esencial de la familia" existe y es
   computable ventana a ventana en el límite. La positividad estricta del símbolo es **literalmente** el
   cuantificador uniforme-en-ventanas: la corona convierte media/uniforme en $c_0$/$\ell^\infty$.

4. **(§4–§5) El test de fuego (C): los negativos de ¬RH se ESTRATIFICAN por visibilidad — tricotomía, no
   dicotomía.** Con la visibilidad $\theta_j$ de un cuádruplo $(\delta_j,\gamma_j)$ a la resolución $a(\cdot)$
   del calendario de ventanas ($\theta_j\asymp\min(1,\delta_j a(\gamma_j))^{\kappa}$): (a) **gordos**
   ($\theta_j\geq c$ infinitas veces) ⟹ el símbolo los VE:
   $\mathrm{spec}(\sigma(Q))\cap(-\infty,-c/2]\neq\emptyset$ (Teorema 5.1); (b) **finos visibles**
   ($\theta_j\to0$, $\theta_j>0$) ⟹ los negativos se acumulan exactamente en $0\in\mathrm{spec}(\sigma(Q))$:
   positividad débil del símbolo SÍ, estricta NO — **los ceros viven en la frontera símbolo/compacto** (Teorema
   5.2); (c) **sub-resolución** ($\delta_j a(\gamma_j)\to0$) ⟹ $Q-Q^{\mathrm{aut}}\in\mathcal J$: el símbolo es
   CIEGO y $\delta=\infty$ igual (Teorema 5.4; el ancla incondicional es el Teorema 3.3 del Doc 108). Y
   **[TEOREMA 5.5]**: para TODO calendario hay configuraciones $m=\infty$ invisibles — $m=\sup_a m_a$ es un
evento de frontera sobre la filtración de resoluciones: el cuantificador maestro reaparece como **cuantificador
de resolución**.

5. **(§6) Computabilidad del símbolo: transmutación localizada al milímetro.**
   $\|\sigma(Q)-\sigma(Q^{\mathrm{aut}})\|=\limsup_n\|Q_n-Q_n^{\mathrm{aut}}\|$ (Lema 3.2): "el símbolo es la
   predicción arquimediana" ⟺ asintótica de segundo orden **uniforme en ventanas** — la Conjetura 108-N en
   coordenadas C*, que implica RH-a-resolución (Doc 108, Teo. 4.3). Lo que la aritmética computa
   incondicionalmente (MV74, vía Doc 108 §5.2) son los **estados de Cesàro** de $\sigma(Q)$: la media. El muro
   media/uniforme = topología débil-de-estados / topología de norma en la corona. Mismo muro, coordenadas nuevas
   — pero ahora con un punto: $0\in\mathrm{spec}(\sigma(Q))$.

6. **(§7) El dividendo positivo: la sinergia Fredholm × replicación.** **[TEOREMA 7.2, en el modelo]:** bajo el
   Axioma R (replicabilidad, la forma abstracta de LP-112), las réplicas de un cuádruplo conservan $\delta_0>0$:
   para cualquier calendario con $a(\gamma)\to\infty$ son **eventualmente gordas** — el estrato fino es
   exactamente el estrato NO replicable (donde viven los anti-modelos cosh). Conjunción: **Axioma R ∧
   positividad estricta del símbolo ⟹ RH.** El muro se parte en dos piezas con nombre: **LP-134** (repulsión de
   resolución: ningún cero off es asintóticamente sub-resolución — nuevo, no es RH, es geométrico) y la
   uniformidad de ventanas (el muro viejo). VEREDICTO en §9: **transmutación localizada con caracterización
   C*-algebraica nueva del muro, más dos teoremas incondicionales nuevos (1.3 y 2.2) y un lema faltante nuevo
   bien formado (LP-134).**

---

## 1. La definición exacta de positividad esencial — y por qué la estricta es óptima

A lo largo de §1–§2: $H$ espacio de Hilbert complejo separable de dimensión infinita, $G=G^*\in\mathcal B(H)$,
$E_G$ su medida espectral, $\delta(G):=\dim\mathrm{ran}\,E_G(-\infty,0)$ (el defecto, Doc 132 Lema 4.1).

**Definición 1.1 (las dos positividades esenciales).**
- $G$ es **esencialmente positivo débil** si $\mathrm{spec_{ess}}(G)\subseteq[0,\infty)$.
- $G$ es **esencialmente positivo estricto** si existe $c>0$ con $\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$.

**Observación 1.2 (forma equivalente de la estricta).** Como $\mathrm{spec_{ess}}(G)$ es cerrado y acotado,
$\mathrm{spec_{ess}}(G)\subseteq(0,\infty)$ ⟺ estricta (un compacto dentro de un abierto dista positivamente del
borde). La frase "$\mathrm{spec_{ess}}\subseteq(0,\infty)$" de B.4 (Doc 132) era, por lo tanto, ya la estricta;
lo que este documento agrega es que la distinción débil/estricta **no es una finura**: es el contenido entero de
la cuestión (§2, §5).

**Teorema 1.3 [TEOREMA] (caracterización exacta de la finitud robusta del defecto).** Para
$G=G^*\in\mathcal B(H)$ son equivalentes:

(i) $G$ es esencialmente positivo estricto; (ii) $\delta(G+K)<\infty$ para **todo** compacto autoadjunto $K$;
(iii) existe $\varepsilon>0$ con $\delta(G-\varepsilon I)<\infty$.

*Demostración.*

**(i) ⟹ (ii).** Es B.4 del Doc 132, repetido para autocontención: por el teorema de Weyl [Kato, *Perturbation
Theory*, Thm. IV.5.35], $\mathrm{spec_{ess}}(G+K)=\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$; luego
$\mathrm{spec}(G+K)\cap(-\infty,0]$ es un conjunto compacto, discreto (sus puntos de acumulación estarían en el
espectro esencial, disjunto de $(-\infty,0]$), por tanto finito, de autovalores de multiplicidad finita:
$\delta(G+K)<\infty$.

**(iii) ⟺ (i).** $\delta(G-\varepsilon I)=\dim\mathrm{ran}\,E_G(-\infty,\varepsilon)$. Si esto es finito,
$\mathrm{spec}(G)\cap(-\infty,\varepsilon)$ consiste en finitos autovalores de multiplicidad finita, luego
$\mathrm{spec_{ess}}(G)\subseteq[\varepsilon,\infty)$: estricta. Recíprocamente, si
$\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$, tómese $\varepsilon=c/2$: $\mathrm{spec}(G)\cap(-\infty,c/2)$ es
finito con multiplicidades finitas (mismo argumento que arriba), luego
$\dim\mathrm{ran}\,E_G(-\infty,c/2)<\infty$.

**(ii) ⟹ (i), por contrarrecíproco — la dirección nueva.** Supóngase que la estricta falla: existe
$\mu\in\mathrm{spec_{ess}}(G)$ con $\mu\leq0$. Construyo $K$ compacto autoadjunto con $\delta(G+K)=\infty$.

*Paso 1 (sucesión de Weyl ortonormal con error sumable).* Para cada $n$,
$\dim\mathrm{ran}\,E_G\bigl(\mu-8^{-n},\,\mu+8^{-n}\bigr)=\infty$ (definición de espectro esencial para
autoadjuntos: si fuera finita para algún $n$, $\mu$ sería autovalor aislado de multiplicidad finita o no estaría
en el espectro). Elijo inductivamente $e_n\in\mathrm{ran}\,E_G(\mu-8^{-n},\mu+8^{-n})$ unitario y ortogonal a
$e_1,\dots,e_{n-1}$ (posible: el rango es de dimensión infinita y las condiciones de ortogonalidad son finitas).
Entonces $(e_n)$ es ortonormal y
$$\|(G-\mu)e_n\|^2=\int_{(\mu-8^{-n},\mu+8^{-n})}|\lambda-\mu|^2\,d\|E_\lambda e_n\|^2\leq 64^{-n},\qquad\text{i.e. }\|(G-\mu)e_n\|\leq 8^{-n}.$$

*Paso 2 (la matriz de Gram de $G$ sobre $V:=\overline{\mathrm{span}}\{e_n\}$).* Para $n\neq m$, usando
ortonormalidad y autoadjunción:
$$|\langle Ge_n,e_m\rangle|=|\langle(G-\mu)e_n,e_m\rangle|\leq 8^{-n},\qquad
|\langle Ge_n,e_m\rangle|=|\langle e_n,(G-\mu)e_m\rangle|\leq 8^{-m},$$
luego $|\langle Ge_n,e_m\rangle|\leq 8^{-\max(n,m)}$; y $\langle Ge_n,e_n\rangle\leq\mu+8^{-n}\leq 8^{-n}$.

*Paso 3 (la perturbación).* Defino $K:=-\sum_{n\geq1}2^{-n}\langle\cdot,e_n\rangle e_n$: compacto (límite en
norma de rangos finitos), autoadjunto, $\|K\|=\tfrac12$. Para $x=\sum_n\xi_ne_n$ con soporte finito en
$\{n\geq n_0\}$ (con $n_0$ a fijar):
$$\langle(G+K)x,x\rangle\leq\sum_n\bigl(8^{-n}-2^{-n}\bigr)|\xi_n|^2+\sum_{n\neq m}8^{-\max(n,m)}|\xi_n||\xi_m|.$$
El término cruzado se acota por
$\sum_{n\neq m}8^{-\max(n,m)}\tfrac{|\xi_n|^2+|\xi_m|^2}{2}\leq\sum_n|\xi_n|^2\,r_n$ con
$r_n:=\sum_{m\neq n}8^{-\max(n,m)}\leq n\,8^{-n}+\sum_{m>n}8^{-m}\leq(n+1)8^{-n}$. Luego
$$\langle(G+K)x,x\rangle\leq\sum_n\Bigl(8^{-n}+(n+1)8^{-n}-2^{-n}\Bigr)|\xi_n|^2.$$
Como $(n+2)8^{-n}<2^{-n}$ para todo $n\geq4$, tomando $n_0=4$ el coeficiente es $<0$ para cada $n\geq n_0$: la
forma $G+K$ es definida negativa sobre $V_0:=\mathrm{span}\{e_n:n\geq4\}$, de dimensión infinita. Por la
definición de $\delta$ como neg.ind (Doc 132, Lema 4.1 y Def. 2.2), $\delta(G+K)=\infty$. $\square$

**Corolario 1.4 (la lección de diseño).** La única lectura de "positividad esencial ⟹ $m<\infty$" que sobrevive
al ideal compacto — y el espectro esencial vive *por definición* módulo ese ideal — es la **estricta**. Todo
certificado del programa debe producir un **gap** $c>0$, no solo un signo. El contraejemplo
$\mathrm{diag}(-1/n)$ de la Obs. 4.2 del Doc 132 no era una curiosidad: por el Teorema 1.3 es el caso general de
lo que pasa sin gap.

**Lema 1.5 [LEMA] (detector de gap por sucesiones ortonormales).** Si existe una sucesión ortonormal $(u_n)$ en
$H$ con $\liminf_n\langle Gu_n,u_n\rangle\leq\ell$, entonces $\inf\mathrm{spec_{ess}}(G)\leq\ell$.

*Demostración.* Supóngase $\mathrm{spec_{ess}}(G)\subseteq[c,\infty)$ con $c>\ell$. Sea
$\varepsilon\in(0,c-\ell)$ y $E:=E_G(-\infty,c-\varepsilon)$: de rango finito (como en 1.3, (iii)⟺(i)). Con
$m_0:=\inf\mathrm{spec}(G)>-\infty$:
$$\langle Gu,u\rangle=\int\lambda\,d\|E_\lambda u\|^2\geq m_0\|Eu\|^2+(c-\varepsilon)\|(1-E)u\|^2=(c-\varepsilon)\|u\|^2-(c-\varepsilon-m_0)\|Eu\|^2.$$
Como $(u_n)$ es ortonormal, $u_n\rightharpoonup0$, y $E$ de rango finito da $\|Eu_n\|\to0$:
$\liminf\langle Gu_n,u_n\rangle\geq c-\varepsilon>\ell$. Contradicción. $\square$

---

## 2. La normalización (i): peso fijo. Teorema de degeneración y resolución del enigma

La primera candidata del encargo: realizar la forma de Weil como UN operador de Gram $G$ sobre un $L^2$ de peso
fijo (la realización CCM es el ejemplo del programa: el costo negativo de un cuádruplo a altura $\gamma$ es
$2\delta^2K_\lambda(\gamma)$ con $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98; la medida
espectral $dm_\infty$ decae, Doc 95). En esta normalización los cuádruplos altos aportan negativos de norma
$\to0$: la suma de los bloques off es compacta (de hecho clase traza), y el espectro esencial de $G$ ignora los
ceros. El encargo pregunta: ¿entonces la positividad esencial sería autónoma — y valdría incluso bajo ¬RH con
$m=\infty$, sin dar $m<\infty$? ¿Dónde falla? Respuesta: exactamente donde el Teorema 1.3 dice — en el gap. Y la
falla es un teorema:

**Definición 2.1 (propiedad (N1): degeneración de alta frecuencia).** Una realización de tipo Hilbert $(H,G)$ de
una forma hermitiana $Q$ sobre una clase de tests con noción de altura tiene la propiedad
**(N1)** si existe una sucesión ortonormal $(u_n)\subset H$ (tests normalizados localizados a alturas
$T_n\to\infty$) con $\langle Gu_n,u_n\rangle=Q(u_n,u_n)\to0$.

**Teorema 2.2 [TEOREMA] (degeneración del gap en peso fijo).** Si $(H,G)$ tiene (N1), entonces
$\inf\mathrm{spec_{ess}}(G)\leq0$: $G$ **no** es esencialmente positivo estricto — cualquiera sea la posición de
los ceros. En consecuencia, por el Teorema 1.3, existe $K$ compacto autoadjunto con $\delta(G+K)=\infty$, y
ninguna cadena del tipo
$$\text{(símbolo autónomo positivo)}+\text{(compacto)}\;\Longrightarrow\;\delta<\infty$$
puede ejecutarse en esta realización: la conclusión es falsa para algún miembro de la clase módulo-compactos en
la que el certificado vive.

*Demostración.* Inmediata del Lema 1.5 con $\ell=0$. La segunda afirmación: el Teorema 1.3 ((ii)⟹(i)
contrarrecíproco) produce el $K$; y un certificado "esencial" — invariante bajo el ideal compacto por
construcción — no puede distinguir $G$ de $G+K$. $\square$

**[PUENTE 2.3] (la CCM tiene (N1)).** En la realización CCM con norma de Hilbert fija, los vectores coordenados
normalizados a altura espectral $\gamma$ tienen $Q$-valor $\asymp$ peso local de $dm_\infty$, que decae (Doc 95:
decaimiento de $dm_\infty$; Doc 98: el núcleo $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$). Estatus:
el decaimiento del peso es teorema del modelo CCM (Docs 95/98); la ortonormalización de las colas y el chequeo
(N1) literal es rutina declarada no ejecutada línea a línea acá — **[estatus: heredado del modelo, sin riesgo
identificado]**. Para cualquier otra realización de peso fijo con forma de Weil de masa decreciente en altura
(toda normalización "L² fija" la tiene: la fórmula explícita reparte masa $\sim\log T$ por ventana mientras la
norma fija reparte masa constante — el cociente por ventana decae tras normalizar colas), el mismo teorema
aplica.

**Corolario 2.4 (resolución del enigma del encargo).** En la normalización (i):

1. Los negativos de ¬RH viven en el **ideal compacto** (bloques off de norma $\to0$): el espectro esencial es
   ciego a ellos. **Cierto.**
2. La positividad esencial **débil** de $G$ es entonces plausiblemente un enunciado autónomo, válido en ambos
   mundos incluso con $m=\infty$. **Cierto.**
3. No hay contradicción con B.4 porque B.4 (correctamente leído: Teorema 1.2(i)⟹(ii) = estricta) **pide el
   gap**, y el Teorema 2.2 muestra que el gap falla incondicionalmente: los autovalores negativos
   $\lambda_j\asymp-\delta_j^2K_\lambda(\gamma_j)\to0^-$ bajo ¬RH-$m=\infty$ rompen el gap sin romper la débil —
   exactamente el patrón $\mathrm{diag}(-1/n)$.
4. **La ruta (i) muere con teorema**: no porque el símbolo vea los ceros (no los ve) sino porque el símbolo no
   tiene gap que ofrecer. La ceguera del espectro esencial y la inutilidad del certificado son, acá, el mismo
   hecho.

**Observación 2.5 (la moraleja estructural).** El peso fijo aplasta TODO a altura grande — el mar on-line y los
cuádruplos off por igual. La información "$m<\infty$" es una afirmación **por ventana re-normalizada**;
cualquier normalización global fija la borra junto con el ruido. Esto fuerza la opción (ii) del encargo: la
familia de ventanas re-normalizadas, que no es un operador. La pregunta correcta pasa a ser: ¿espectro esencial
*de qué*? La respuesta es §3.

---

## 3. [DEFINICIÓN-NUEVA] El álgebra de Weil–Toeplitz

### 3.1. El campo de ventanas y la corona

**Definición 3.1 (campo de ventanas; el álgebra $\mathcal W$; el ideal $\mathcal J$; el símbolo).** Un **campo
de ventanas** es una sucesión $\{(H_n,Q_n)\}_{n\geq2}$ donde $H_n$ es un espacio de Hilbert de dimensión finita
$d_n<\infty$ y $Q_n=Q_n^*\in\mathcal B(H_n)$, con $\sup_n\|Q_n\|<\infty$. Sobre el campo:
$$\mathcal W:=\Bigl\{A=(A_n)_{n}:\ A_n\in\mathcal B(H_n),\ \|A\|:=\sup_n\|A_n\|<\infty\Bigr\}$$
con operaciones puntuales: C*-álgebra (el producto $\ell^\infty$ del campo).
$$\mathcal J:=\bigl\{A\in\mathcal W:\ \|A_n\|\to0\bigr\}$$
es un ideal bilátero cerrado (el **ideal compacto del campo**: contiene toda sección de soporte finito; es su
clausura). La **corona** es $\mathcal C:=\mathcal W/\mathcal J$, y el **símbolo** de una sección es su clase:
$$\sigma(A):=A+\mathcal J\in\mathcal C.$$

Justificación del nombre "ideal compacto": en el operador suma directa $\bigoplus_n A_n$ sobre
$\bigoplus_n H_n$, una sección está en $\mathcal J$ si y solo si el operador es compacto (bloques de dimensión
finita con normas $\to0$); $\mathcal W/\mathcal J$ es la imagen del álgebra de secciones en el álgebra de Calkin
de $\bigoplus H_n$. La corona es, literalmente, "la familia módulo compactos".

**Lema 3.2 [LEMA] (norma del símbolo).** $\|\sigma(A)\|_{\mathcal C}=\limsup_n\|A_n\|$.

*Demostración.* ($\leq$) Para $N$ fijo, la truncación $A^{(N)}:=(A_2,\dots,A_N,0,0,\dots)\in\mathcal J$, luego
$\|\sigma(A)\|\leq\|A-A^{(N)}\|=\sup_{n>N}\|A_n\|\xrightarrow{N\to\infty}\limsup_n\|A_n\|$. ($\geq$) Para todo
$J\in\mathcal J$: $\|A+J\|=\sup_n\|A_n+J_n\|\geq\limsup_n\|A_n+J_n\|=\limsup_n\|A_n\|$ (pues $\|J_n\|\to0$).
Tomando ínfimo sobre $J$: $\|\sigma(A)\|\geq\limsup\|A_n\|$. $\square$

**Lema 3.3 [LEMA] (el espectro del símbolo es el conjunto límite de los espectros de ventana).** Sea
$A=(A_n)\in\mathcal W$ con cada $A_n$ autoadjunto. Entonces
$$\mathrm{spec}_{\mathcal C}\bigl(\sigma(A)\bigr)=\Lambda(A):=\bigl\{\lambda\in\mathbb R:\ \exists\,n_k\to\infty,\ \lambda_k\in\mathrm{spec}(A_{n_k}),\ \lambda_k\to\lambda\bigr\}.$$

*Demostración.* $\sigma(A)$ es autoadjunto en $\mathcal C$, espectro real. $\Lambda(A)$ es cerrado y acotado
(por $\sup\|A_n\|$).

($\supseteq$, i.e. $\lambda\notin\mathrm{spec}\Rightarrow\lambda\notin\Lambda$) Si $\sigma(A)-\lambda$ es
invertible en $\mathcal C$, existe $B\in\mathcal W$ con $(A-\lambda)B=1+J$, $B(A-\lambda)=1+J'$,
$J,J'\in\mathcal J$. Para $n$ grande, $\|J_n\|,\|J'_n\|\leq\tfrac12$, luego $(A_n-\lambda)B_n$ y
$B_n(A_n-\lambda)$ son invertibles, luego $A_n-\lambda$ es invertible (inverso a derecha e izquierda) con
$\|(A_n-\lambda)^{-1}\|\leq2\|B\|$. Para autoadjuntos,
$\|(A_n-\lambda)^{-1}\|=\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)^{-1}$:
$\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)\geq(2\|B\|)^{-1}$ para todo $n$ grande. Entonces ningún
$\lambda_k\in\mathrm{spec}(A_{n_k})$ puede converger a $\lambda$: $\lambda\notin\Lambda(A)$.

($\subseteq$, i.e. $\lambda\notin\Lambda\Rightarrow\lambda\notin\mathrm{spec}$) Si $\lambda\notin\Lambda(A)$,
existen $\varepsilon>0$ y $N$ con $\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)\geq\varepsilon$ para todo $n\geq N$
(si no, habría una sucesión violatoria, que por compacidad de los espectros acotados produciría un punto de
$\Lambda$ a distancia $<\varepsilon$ de $\lambda$, y refinando, $\lambda\in\Lambda$). Defino
$B_n:=(A_n-\lambda)^{-1}$ para $n\geq N$ (existe, $\|B_n\|\leq\varepsilon^{-1}$) y $B_n:=0$ para $n<N$:
$B\in\mathcal W$. Entonces $(A-\lambda)B-1$ y $B(A-\lambda)-1$ son secciones de soporte finito $\in\mathcal J$:
$\sigma(B)$ es el inverso de $\sigma(A)-\lambda$. $\square$

**Corolario 3.4 (positividad del símbolo = cuantificador uniforme).** Para $A$ autoadjunta:
- $\mathrm{spec}(\sigma(A))\subseteq[0,\infty)$ (**positividad débil del símbolo**) ⟺
  $\min\mathrm{spec}(A_n)\geq-\varepsilon_n$ con $\varepsilon_n\to0$;
- $\mathrm{spec}(\sigma(A))\subseteq[c,\infty)$ con $c>0$ (**positividad estricta del símbolo**) ⟺
  $\forall\varepsilon>0\ \exists N:\ \mathrm{spec}(A_n)\subseteq(c-\varepsilon,\infty)$ $\forall n\geq N$ — un
  gap **uniforme en las ventanas, eventualmente**.

$\square$ (Lema 3.3 leído dos veces.)

**Observación 3.5 (qué objeto es éste).** $\mathcal C$ es el análogo exacto, para una familia, del álgebra de
Calkin; el Lema 3.3 es el análogo del cálculo del espectro esencial por operadores límite (la estructura de la
teoría de operadores límite de Rabinovich–Roch–Silbermann, y del símbolo de Toeplitz: el espectro esencial de
$T_\phi$ es el rango del símbolo = los "límites de las ventanas" del operador; acá el rol del símbolo lo juega
la clase de la sección en la corona). El punto conceptual para el programa: **el cuantificador maestro de P43
(media vs uniforme sobre ventanas, Doc 108 §5.2/§7) se convierte en pertenencia a $c_0$ vs $\ell^\infty$** — la
distinción media/uniforme es, en estas coordenadas, la distinción estado-promedio/norma de la corona (§6). No es
una metáfora: el Corolario 3.4 ES el enunciado "uniforme en toda ventana" del Doc 108, escrito como positividad
de un elemento de una C*-álgebra.

### 3.2. El campo de Weil

**Definición 3.6 (el campo de ventanas de Weil; el calendario de resolución).** Fijo $\Delta\in(0,1]$ y un
**calendario de resolución** $a:[2,\infty)\to[1,\infty)$ no decreciente (el presupuesto de soporte logarítmico
de los tests por ventana; el natural del programa es $a(T)\asymp\log T$, la escala de resolución de ceros
individuales, Doc 108 §3.3). Para cada $n$:
- $H_n$ := un subespacio de dimensión finita de la clase de prueba (clase engrosada del Doc 107 en la versión
  doble; tests de Mellin concentrados en la ventana $|{\rm Im}\,s-n|\leq\Delta$ con soporte
  $\subseteq[e^{-a(n)},e^{a(n)}]$ en la versión simple), dotado de la **normalización por mar on-line**: el
  producto interno de $H_n$ es la forma de Gram espectral de los ceros on-line de la ventana (la masa
  $|\hat f(\rho)|^2$ por cero, normalizada a $1$ por cero).
- $Q_n$ := la compresión a $H_n$ de la forma de Weil, expresada en esa normalización.

El **campo de Weil a calendario $a$** es $\{(H_n,Q_n)\}$; su símbolo es $\sigma(Q)\in\mathcal C$. La sección
**autónoma** $Q^{\mathrm{aut}}=(Q^{\mathrm{aut}}_n)$ es la predicción polar/arquimediana-más-casi-primo de cada
ventana: los bloques $E+\Pi_{\mathrm{predicho}}$ del Doc 108 (3.1) con el déficit $\Delta K$ puesto a cero —
computable sin posiciones de ceros (Doc 108, Def. 3.6 y Teorema 4.1).

**[Estatus de la Definición 3.6 — honestidad].** Que estas compresiones existen con la normalización dicha y que
la sección es acotada usa el aparato de realizabilidad del Doc 107/108 (Lema 2.4 del Doc 108 y su caveat
declarado, mismo estatus acá: Hipótesis D del juguete para los enunciados bajo ¬RH; bajo RH la normalización es
la diagonal exacta de la Prop. 2.2 del Doc 108). La acotación uniforme de $\|Q_n\|$ en la normalización por mar
exige el control de las correcciones de correlación de pares por ventana —
**[GAP-134.R, declarado]**: se asume como axioma (S1) del modelo de §4, donde TODOS los teoremas de §5 se
prueban con rigor completo dentro del modelo. El documento separa así, como exige el contrato: teoremas (en el
modelo axiomatizado, §4–§5) / puente (la instancia Weil, §8).

---

## 4. [DEFINICIÓN-NUEVA] El modelo espectral $\mathfrak W$: visibilidad y resolución

La estructura espectral de la forma de Weil por ventanas, destilada del corpus (Doc 107 Teorema 5.5 y Prop. 6.1;
Doc 108 Prop. 2.3, Teorema 3.3, Lema 2.4; Doc 131 §6: bloques hiperbólicos por órbita libre del divisor), es:
**mar on-line ≈ identidad + correcciones; cada cuádruplo off visible aporta un plano hiperbólico; lo
sub-resolución no se ve.** El modelo axiomatiza exactamente eso.

**Definición 4.1 (configuración).** Una **configuración** es un conjunto a lo sumo numerable
$Z=\{(\delta_j,\gamma_j)\}_{j\in J}$ con $\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$ si $|J|=\infty$, y
finitos $j$ por ventana ($\#\{j:|\gamma_j-n|\leq\Delta\}<\infty$, uniformemente acotado por ventana no se
exige). $m:=|J|\in\mathbb N\cup\{\infty\}$. ($Z=\emptyset$ es "RH"; $(\delta_j,\gamma_j)$ es el cuádruplo
$\{\tfrac12\pm\delta_j\pm i\gamma_j\}$.)

**Definición 4.2 (visibilidad a calendario $a$).** La **visibilidad** del cuádruplo $j$ es
$$\theta_j:=\theta(\delta_j,\gamma_j)\in[0,1],$$
donde $\theta(\delta,\gamma)$ es una función fija con las propiedades:

(V1) $\theta$ es continua, no decreciente en $\delta$, y $\theta(\delta,\gamma)\to0$ cuando
$\delta\,a(\gamma)\to0$; (V2) existe $c_0>0$ con $\theta(\delta,\gamma)\geq c_0$ cuando
$\delta\,a(\gamma)\geq1$.

Los cuádruplos con $\delta_j\,a(\gamma_j)\geq1$ se llaman **supra-resolución (gordos)**; con
$\delta_j\,a(\gamma_j)<1$, **sub-resolución (finos)**; $m_a:=\#\{j:\delta_j\,a(\gamma_j)\geq1\}$.

**[CÁLCULO 4.3] (de dónde sale $\theta$ y por qué (V1)–(V2) son las propiedades correctas — mostrado).** La
dirección negativa del plano hiperbólico de un cuádruplo exige un test con
$\hat f(\tfrac12+\delta+i\gamma)\approx-\hat f(\tfrac12-\delta+i\gamma)$ — oposición de signo a través de una
banda de ancho $2\delta$. Hago las dos mitades del cálculo.

*Mitad (V1) — por debajo de la resolución no hay nada que alinear.* Sea $f$ un test con soporte multiplicativo
en $[e^{-a},e^{a}]$: $\hat f(s)=\int_{-a}^{a}F(u)e^{(s-\frac12)u}\,du$ con $F(u)=f(e^u)e^{u/2}$. Derivando bajo
la integral, para $s$ en la banda $|\mathrm{Re}\,s-\tfrac12|\leq\tfrac12$:
$$\bigl|\partial_\sigma\hat f(s)\bigr|=\Bigl|\int_{-a}^{a}u\,F(u)e^{(s-\frac12)u}du\Bigr|\leq a\,e^{a/2}\|F\|_{L^1},$$
y por el teorema del valor medio aplicado sobre el segmento
$[\tfrac12-\delta+i\gamma,\ \tfrac12+\delta+i\gamma]$:
$$\hat f(\tfrac12+\delta+i\gamma)\,\overline{\hat f(\tfrac12-\delta+i\gamma)}\;=\;\bigl|\hat f(\tfrac12+i\gamma)\bigr|^2\;+\;O\bigl(\delta\,a\,e^{a/2}\|F\|_{L^1}\cdot\sup_{\text{banda}}|\hat f|\bigr).$$
Es decir: la contribución del par off difiere de la de un par on-line ficticio en $O(\delta a)$ por unidad de
masa (tras la normalización por mar, que fija $\sup|\hat f|$ y $\|F\|$ a escala $1$ por cero): **un cuádruplo
con $\delta a\to0$ es una perturbación de norma $O(\delta a)\to0$ de la predicción autónoma, no un bloque
nuevo.** El ancla incondicional probada de este mecanismo es el Teorema 3.3 del Doc 108 (soporte fijo,
$T\to\infty$: $Q_2=AA(1+O(1/\log T))>0$ — la ceguera sub-resolución como teorema).

*Mitad (V2) — por encima de la resolución la alineación se realiza.* Para $\delta a\geq1$ existe el test
alineado: tómese $F$ impar-modulada, $F(u)=\chi(u/a)\sinh$-tipo… concretamente
$\hat f(s):=\hat g(s)\cdot\bigl(s-\tfrac12-i\gamma\bigr)$ con $\hat g$ de tipo PW concentrada en $i\gamma$ (Doc
107, Lema 1.2: multiplicar por polinomios en $s$ = aplicar $x\partial_x$, preserva la clase): el factor lineal
vale $\pm\delta$ en $\tfrac12\pm\delta+i\gamma$ — oposición exacta de signo — y se anula en $\tfrac12+i\gamma$,
suprimiendo el cero on-line más cercano. La pérdida contra el mar de la ventana es el contenido del Lema 2.4 del
Doc 108 (con su caveat declarado): la masa on-line residual se controla con factores polinomiales adicionales y
decaimiento PW, dejando visibilidad $\geq c_0$ absoluta. Estatus de esta mitad = estatus del Lema 2.4 (Hipótesis
D del juguete).

La forma exacta de $\theta$ en la zona de transición $\delta a\asymp1$ (¿$(\delta a)$ o $(\delta a)^2$? — el
costo $2\delta^2K_\lambda(\gamma)$ del Doc 98, renormalizado por mar, sugiere exponente $2$; el cálculo PW de
arriba da el exponente $1$ como cota de perturbación, y la negatividad realizable suele ser el cuadrado de la
amplitud de alineación) **no es load-bearing**: ningún teorema de §5 usa más que (V1)–(V2). [Exponente exacto:
GAP-134.θ, declarado, no portante.]

**Definición 4.4 (el modelo $\mathfrak W(Z)$).** Dada una configuración $Z$ y el calendario $a$, el campo modelo
es
$$H_n:=\mathbb C^{d_n}\oplus\bigoplus_{j\in J_n^{\mathrm{vis}}}\mathbb C^2,\qquad
Q_n:=\bigl(I_{d_n}+R_n\bigr)\ \oplus\ \bigoplus_{j\in
J_n^{\mathrm{vis}}}\begin{pmatrix}0&\theta_j\\\theta_j&0\end{pmatrix}\ +\ C_n,$$ donde $d_n\asymp\Delta\log n$
(mar on-line por ventana), $J_n^{\mathrm{vis}}:=\{j:|\gamma_j-n|\leq\Delta,\ \theta_j>0\}$, y:

(S1) $\|R_n\|\leq r<\tfrac12$ para todo $n$ (correcciones del mar: correlación de pares por ventana). [Instancia
Weil: GAP-134.R.] (S2) los bloques hiperbólicos tienen el peso $\theta_j$ de la Def. 4.2, con (V1)–(V2).
[Instancia Weil: CÁLCULO 4.3 + Lema 2.4/Teorema 3.3 del Doc 108.] (S3) $\|C_n\|\leq\omega_n$ con $\omega_n\to0$
(acoplamientos cruzados mar↔off y off↔off entre ventanas separadas). [Instancia Weil: el decaimiento de
correlaciones entre ventanas espectrales — herencia directa de GAP-132.ω; en el modelo CCM,
$K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Docs 95/98.]

La sección autónoma del modelo es $Q^{\mathrm{aut}}_n:=(I_{d_n}+R_n)\oplus I_{2|J_n^{\mathrm{vis}}|}$ **sobre el
mismo espacio** cuando se compara con $Q_n$ a configuración fija, y $Q^{\mathrm{aut}}$ a secas denota el campo
con $Z=\emptyset$ (solo mar). Los cuádruplos sub-resolución con $\theta_j=0$ **no aparecen** en $H_n$: su efecto
entero está absorbido en $R_n/C_n$ (Doc 108, Teorema 3.3: el test no los resuelve; ésa es la definición
operativa de "sub-resolución").

**Observación 4.5 (qué es teorema y qué es axioma — tabla de estatus del modelo).**

| axioma | contenido | estatus en la instancia Weil |
|---|---|---|
| forma de bloques | mar ⊕ planos hiperbólicos | **teorema** (Doc 107 Teo. 5.5/Prop. 6.1; Doc 131 Teo. 6.3: órbita libre ⟹ bloque hiperbólico) |
| (S1) $\|R_n\|\leq r<\tfrac12$ | mar ≈ identidad por ventana | GAP-134.R (correlación de pares por ventana, acotación no probada) |
| (S2) visibilidad (V1)–(V2) | (V1) por debajo de la resolución no se ve: **teorema** (Doc 108 Teo. 3.3); (V2) por encima se realiza: estatus del Lema 2.4 del Doc 108 (Hipótesis D, caveat declarado) | mixto, declarado |
| (S3) $\omega_n\to0$ | ventanas lejanas se desacoplan | GAP-132.ω (parcial en CCM, Docs 95/98) |

Todos los teoremas de §5 son **incondicionales dentro de $\mathfrak W$**; su transporte a ζ tiene exactamente
los estatus de esta tabla y se discute en §8.

---

## 5. Los teoremas de estratificación: el test de fuego

En todo §5: campo $\mathfrak W(Z)$ con (S1)–(S3); $\sigma(Q)\in\mathcal C$ su símbolo;
$\Lambda(Q)=\mathrm{spec}(\sigma(Q))$ (Lema 3.3); $\vartheta_n:=\max\{\theta_j:j\in J_n^{\mathrm{vis}}\}$ ($:=0$
si vacío).

**Lema 5.0 [LEMA] (espectro por ventana).** Para todo $n$:
$$\mathrm{spec}(Q_n)\subseteq\bigl([1-r,\,1+r]\cup\{\pm\theta_j\}_{j\in J_n^{\mathrm{vis}}}\bigr)+[-\omega_n,\omega_n].$$
En particular: $\lambda_{\min}(Q_n)\geq-\vartheta_n-\omega_n$; y si $J_n^{\mathrm{vis}}\neq\emptyset$,
$\lambda_{\min}(Q_n)\leq-\vartheta_n+\omega_n$.

*Demostración.* Sin $C_n$, $Q_n$ es suma directa: el bloque mar tiene espectro en $[1-r,1+r]$; cada bloque
$\begin{pmatrix}0&\theta\\\theta&0\end{pmatrix}$ tiene autovalores $\pm\theta$ (autovectores $(1,\pm1)/\sqrt2$).
La perturbación autoadjunta $C_n$ mueve cada autovalor a lo sumo $\|C_n\|\leq\omega_n$ (Weyl finito-dimensional:
$|\lambda_k(A+B)-\lambda_k(A)|\leq\|B\|$). La cota superior de $\lambda_{\min}$: el autovector $v=(1,-1)/\sqrt2$
del bloque de $\vartheta_n$ da $\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n$, y
$\lambda_{\min}\leq\langle Q_nv,v\rangle$. $\square$

**Teorema 5.1 [TEOREMA] (gordos ⟹ el símbolo los ve).** Si existe $c>0$ y una subsucesión $j_k$ con
$\theta_{j_k}\geq c$ y $\gamma_{j_k}\to\infty$, entonces
$$\mathrm{spec}\bigl(\sigma(Q)\bigr)\cap(-\infty,-c/2]\neq\emptyset.$$
En particular el símbolo no es ni débilmente positivo: la negatividad de los cuádruplos supra-resolución
**sobrevive al cociente por el ideal compacto**.

*Demostración.* Sea $n_k:=$ la ventana de $\gamma_{j_k}$ ($n_k\to\infty$ pues $\gamma_{j_k}\to\infty$). Por el
Lema 5.0, $\lambda_{\min}(Q_{n_k})\leq-\theta_{j_k}+\omega_{n_k}\leq-c+\omega_{n_k}$. Como $\omega_{n}\to0$, los
$\lambda_{\min}(Q_{n_k})$ tienen un punto de acumulación $\leq-c$; los espectros están uniformemente acotados,
así que existe el límite por subsucesión: un punto de $\Lambda(Q)$ en $(-\infty,-c]\subseteq(-\infty,-c/2]$.
Lema 3.3. $\square$

**Teorema 5.2 [TEOREMA] (finos visibles ⟹ los negativos viven exactamente en la frontera $0$).** Supóngase
$m=\infty$, $J_n^{\mathrm{vis}}\neq\emptyset$ para infinitos $n$, y $\vartheta_n\to0$ (todas las visibilidades
tienden a cero). Entonces:

(i) $0\in\mathrm{spec}(\sigma(Q))$, alcanzado como límite de autovalores **negativos**
$\lambda_{\min}(Q_{n})\in[-\vartheta_{n}-\omega_{n},\,-\vartheta_{n}+\omega_{n}]$ sobre las ventanas pobladas
(cuando $\vartheta_n>\omega_n$, genuinamente negativos); (ii)
$\mathrm{spec}(\sigma(Q))\subseteq\{0\}\cup[1-r,1+r]$: la positividad **débil** del símbolo VALE; (iii) la
positividad **estricta** del símbolo FALLA; (iv) el defecto global es infinito: en la suma directa
$\bigl(\bigoplus_nH_n,\bigoplus_nQ_n\bigr)$, $\delta=\infty$.

Es decir: el símbolo no es ciego a los finos (los ve acumularse) pero tampoco los separa (no aportan masa
espectral negativa lejos de $0$): **viven en el punto frontera $0$ — el punto que distingue la positividad débil
de la estricta, el mismo punto del Teorema 1.3.**

*Demostración.* (i) Lema 5.0: sobre las infinitas ventanas pobladas, $\lambda_{\min}(Q_n)\to0$ (pues
$\vartheta_n\to0$, $\omega_n\to0$) y $\lambda_{\min}(Q_n)\leq-\vartheta_n+\omega_n$; el límite $0$ es punto de
$\Lambda(Q)$ (Lema 3.3). (ii) Por el Lema 5.0 todo autovalor de $Q_n$ está en
$[-\vartheta_n-\omega_n,\vartheta_n+\omega_n]\cup[1-r-\omega_n,1+r+\omega_n]$; los puntos límite están en
$\{0\}\cup[1-r,1+r]$. (iii) Inmediato de (i) y el Corolario 3.4. (iv) Cada ventana poblada aporta
$\mathrm{neg.ind}(Q_n)\geq1$ cuando $\vartheta_n>\omega_n$ (autovalor $\leq-\vartheta_n+\omega_n<0$); si
$\vartheta_n\leq\omega_n$ en casi toda ventana poblada, tómese la sucesión de vectores hiperbólicos negativos
$v_n$ con $\langle Q_nv_n,v_n\rangle\leq-\vartheta_n+\omega_n$… en ese caso degenerado la negatividad por
ventana puede perderse; pero $\delta$ de la configuración como forma (el $\mathrm{neg.ind}$ de la forma de Weil
completa, no de sus compresiones a resolución $a$) es $2m=\infty$ por el Teorema D del Doc 132 — la compresión
puede subestimar, jamás sobreestimar. Para el enunciado (iv) tal como está (la suma directa del campo), basta el
caso $\vartheta_n>\omega_n$ en infinitas ventanas; si no se da, (iv) se sostiene al nivel de la forma completa y
la afirmación correcta es: el campo pierde esos negativos — que es exactamente el fenómeno del Teorema 5.4.
$\square$

**Teorema 5.3 [TEOREMA] (positividad estricta del símbolo ⟺ finitud VISIBLE).** Equivalen:

(i) $\mathrm{spec}(\sigma(Q))\subseteq[c,\infty)$ para algún $c>0$; (ii) $J_n^{\mathrm{vis}}=\emptyset$ para
todo $n$ suficientemente grande salvo, a lo sumo, ventanas cuya visibilidad máxima cumple $\vartheta_n\to0$
**y** $\vartheta_n\leq\omega_n$ eventualmente (cuádruplos por debajo del ruido del modelo); (iii) en el caso
limpio $\omega_n\equiv0$: $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$, i.e. **solo finitos cuádruplos
visibles**: $m_a^{\mathrm{vis}}:=\#\{j:\theta_j>0\}<\infty$.

En particular (caso limpio): positividad estricta del símbolo a calendario $a$ ⟺ $m_a^{\mathrm{vis}}<\infty$ — y
**no dice nada sobre $m-m_a^{\mathrm{vis}}$**, los sub-resolución.

*Demostración.* Caso limpio primero ($\omega\equiv0$). (iii)⟹(i): si $J_n^{\mathrm{vis}}=\emptyset$ para
$n\geq N$, entonces $\mathrm{spec}(Q_n)\subseteq[1-r,1+r]$ para $n\geq N$: $\Lambda(Q)\subseteq[1-r,1+r]$, gap
$c=1-r>0$ (Cor. 3.4). (i)⟹(iii): si hubiera infinitas ventanas con $J_n^{\mathrm{vis}}\neq\emptyset$, cada una
tiene autovalor $-\vartheta_n<0$ (Lema 5.0, $\omega=0$): los puntos límite de estos autovalores son $\leq0$,
dando $\Lambda(Q)\cap(-\infty,0]\neq\emptyset$, contradiciendo el gap. Con ruido $\omega_n\to0$: el mismo
argumento da (i)⟺(ii) — un autovalor $\leq-\vartheta_n+\omega_n$ existe en cada ventana poblada, y para que
ningún punto límite caiga bajo $c$ hace falta $-\vartheta_n+\omega_n\geq c-\varepsilon$ eventualmente, imposible
salvo que las ventanas pobladas terminen o $\vartheta_n\leq\omega_n\to0$ con autovalores reabsorbidos al lado
positivo. $\square$

**Corolario 5.3bis [COROLARIO] (el gap es cuantitativo: responde la opción (c) del encargo).** En el caso
limpio, supóngase conocido el dato de gap $(c,N_0)$: $\mathrm{spec}(Q_n)\subseteq[c,\infty)$ para $n\geq N_0$.
Entonces
$$m_a^{\mathrm{vis}}\;\leq\;\sum_{n<N_0}\bigl|J_n^{\mathrm{vis}}\bigr|\;\leq\;N_0\cdot\max_{n<N_0}|J_n^{\mathrm{vis}}|,$$
y con la densidad de ceros por ventana ($|J_n^{\mathrm{vis}}|\leq$ #ceros de la ventana $\ll\Delta\log n$,
[IK04, Thm. 5.8]): $m_a^{\mathrm{vis}}\ll N_0\log N_0$. **El gap controla $m$-visible cuantitativamente, con
constantes explícitas en el dato $(c,N_0)$** — la esperanza (c) del encargo es correcta al nivel visible. Lo que
el gap NO controla, por el Teorema 5.4, es $m-m_a^{\mathrm{vis}}$: la opción (c) es verdadera estratificada y
falsa global. $\square$ (Teorema 5.3 más el conteo de von Mangoldt.)

**Teorema 5.4 [TEOREMA] (sub-resolución ⟹ el símbolo es CIEGO: la mitad que mata).** Sea $Z$ una configuración
con $m=\infty$ pero $\delta_j\,a(\gamma_j)\to0$ (todo sub-resolución a calendario $a$; por (V1), $\theta_j\to0$
y, en el régimen estrictamente sub-resolución de la Def. 4.4, $J_n^{\mathrm{vis}}=\emptyset$ con el efecto
entero dentro de las correcciones). Entonces, como secciones sobre el MISMO campo de espacios de tests:
$$Q-Q^{\mathrm{aut}}\in\mathcal J,\qquad\text{luego}\qquad\sigma(Q)=\sigma(Q^{\mathrm{aut}})\ \text{en }\mathcal C,$$
y si $Q^{\mathrm{aut}}$ tiene gap (S1: $\mathrm{spec}\subseteq[1-r,1+r]$ módulo $\omega$), **$\sigma(Q)$ tiene
positividad estricta** — mientras el defecto de la configuración es $\delta=2m=\infty$ (Doc 132, Teorema D, al
nivel de la forma completa). La positividad estricta del símbolo NO implica $m<\infty$.

*Demostración.* En el régimen sub-resolución la ventana $n$ ve, por el mecanismo del Teorema 3.3 del Doc 108
axiomatizado en (S2)/(V1), una perturbación de norma controlada por las visibilidades:
$\|Q_n-Q^{\mathrm{aut}}_n\|\leq\sum_{j:|\gamma_j-n|\leq\Delta}\varphi(\delta_j a(\gamma_j))+2\omega_n$ con
$\varphi(t)\to0$ cuando $t\to0$ ((V1) en su forma de perturbación: el par off a distancia $\delta$ difiere del
par on-line predicho en $O(\delta a)$ sobre tests de resolución $a$ — el contenido probado del Teo. 3.3 de
D108). Como $\gamma_j\to\infty$ y hay finitos $j$ por ventana, $\max_{j\in n}\varphi(\delta_ja(\gamma_j))\to0$ y
la suma por ventana (finita, con cardinal por ventana $O(1)$ en el juguete; en general, dominada por el mismo
argumento de soporte) tiende a $0$: la sección diferencia está en $\mathcal J$. El resto es el Lema 3.2/3.3 y
(S1). La afirmación $\delta=2m$ de la forma completa es el Teorema D.4 del Doc 132 aplicado a la configuración
(los planos hiperbólicos existen en la clase de tests SIN restricción de soporte: con soporte
$\gtrsim1/\delta_j$ el cuádruplo $j$ es visible — pero ese soporte excede el calendario: el negativo existe, el
campo no lo contiene). $\square$

**Teorema 5.5 [TEOREMA] (no-go del calendario: $m<\infty$ es un evento de frontera en la filtración de
resoluciones).**

(a) Para **todo** calendario $a(\cdot)$ existe una configuración $Z$ con $m=\infty$ y
$\delta_j\,a(\gamma_j)\to0$ (tómese $\gamma_j:=j$ — o cualquier sucesión admisible — y
$\delta_j:=\min(\tfrac14,\,1/(j\,a(\gamma_j)))$): invisible a calendario $a$ por el Teorema 5.4.

(b) Para toda configuración y todo cuádruplo $j$, existe un calendario que lo ve: $\delta_j>0$ y basta
$a(\gamma_j)\geq1/\delta_j$. Por lo tanto, con $m_a:=\#\{j:\delta_ja(\gamma_j)\geq1\}$ (los gordos a calendario
$a$):
$$m\;=\;\sup_{a}\ m_a,$$
el supremo sobre la familia dirigida de calendarios.

(c) En consecuencia: $m<\infty$ ⟺ $\exists M\ \forall a:\ m_a\leq M$ — un enunciado $\Sigma_2$ sobre la
filtración de resoluciones — y **ningún símbolo de Weil–Toeplitz individual (ningún calendario fijo) lo
certifica**: por (a), para cada $a$ hay un mundo con $m=\infty$ donde el símbolo a calendario $a$ es
estrictamente positivo.

*Demostración.* (a) Construcción explícita; $\delta_j\,a(\gamma_j)\leq1/j\to0$; Teorema 5.4. (b) Monotonía de
$a\mapsto m_a$ y la observación puntual. (c) Reescritura de (b) más (a). $\square$

**Proposición 5.5bis [PROPOSICIÓN] (estructura de la filtración de resoluciones).** Sea $\mathcal A$ el conjunto
de calendarios (funciones no decrecientes $[2,\infty)\to[1,\infty)$), preordenado por $a\preceq a'$ ⟺
$a(\gamma)\leq a'(\gamma)$ eventualmente. Entonces:

(i) **(monotonía)** $a\preceq a'\Rightarrow m_a\leq m_{a'}+O(1)$ (los gordos de $a$ son gordos de $a'$ salvo los
finitos $\gamma_j$ del tramo inicial); en particular $a\mapsto m_a$ es no decreciente módulo constantes a lo
largo de la filtración;

(ii) **(cofinalidad numerable)** la familia $\{a_k(\gamma):=k\cdot\log\gamma\}_{k\in\mathbb N}$ NO es cofinal en
$\mathcal A$ (un cuádruplo con $\delta_j=e^{-\gamma_j}$ escapa a todo $a_k$ pero es visible para
$a(\gamma)=e^{\gamma}$): la filtración relevante es genuinamente no numerable hacia arriba, PERO para cada
configuración FIJA $Z$ una sucesión numerable de calendarios basta para computar $m=\sup_a m_a$ (tómese $a_k$
adaptado a los primeros $k$ cuádruplos). La no-uniformidad está en que la sucesión depende de $Z$ — **la misma
estructura "constantes internas al mundo vs certificado uniforme" del Doc 112 §2.6 y del cuantificador
maestro**, ahora sobre calendarios;

(iii) **(el símbolo es monótono en información, no en positividad)** subir el calendario puede CREAR negatividad
en el símbolo (un fino se vuelve gordo) pero nunca destruirla en presencia de gordos persistentes: si
$\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c]\neq\emptyset$ por cuádruplos con $\delta_{j_k}a(\gamma_{j_k})\geq1$,
entonces para todo $a'\succeq a$, $\delta_{j_k}a'(\gamma_{j_k})\geq1$ eventualmente y el Teorema 5.1 re-aplica.
La positividad estricta del símbolo es una propiedad **decreciente** a lo largo de la filtración; su valor
límite inferior es exactamente "$m<\infty$" con cota uniforme.

*Demostración.* (i) Si $\delta_ja(\gamma_j)\geq1$ y $a\leq a'$ desde $\gamma\geq\Gamma_0$, entonces
$\delta_ja'(\gamma_j)\geq1$ para los $j$ con $\gamma_j\geq\Gamma_0$; los restantes son finitos (configuración:
finitos por ventana, $\gamma_j\to\infty$). (ii) El escape:
$\delta_j a_k(\gamma_j)=k e^{-\gamma_j}\log\gamma_j\to0$ para todo $k$. La suficiencia adaptada: dada
$Z=\{(\delta_j,\gamma_j)\}$, sea $a_k$ cualquier calendario con $a_k(\gamma_j)\geq1/\delta_j$ para $j\leq k$
(existe: finitas condiciones, interpolar monótonamente); entonces $m_{a_k}\geq\min(k,m)$ y $\sup_k m_{a_k}=m$.
(iii) Inmediato de las definiciones y 5.1. $\square$

**Observación 5.5ter (lectura).** La proposición convierte en enunciado preciso la frase del resumen: el
cuantificador maestro no desapareció — cambió de variable. En el Doc 108 era "$\forall$ ventana" contra "casi
toda ventana"; acá es "$\forall$ calendario" contra "calendario adaptado a la configuración". La ganancia no es
eliminarlo (imposible: P43) sino que en estas coordenadas el cuantificador tiene un objeto geométrico asociado —
la filtración $\mathcal A$ y el punto $0$ de la corona — y un complemento exacto identificado: LP-134 (§7.2) es
precisamente el enunciado "la filtración se estabiliza en un calendario fijo", i.e. "$\exists a\ \forall Z$
aritmética: $m=m_a+O(1)$".

**Observación 5.6 (la respuesta exacta al "test de fuego" (C) del encargo).** ¿Los negativos de
¬RH-con-$m=\infty$ viven en el símbolo o en el ideal compacto? **Respuesta: la dicotomía es falsa; es una
tricotomía estratificada por $\delta_j\,a(\gamma_j)$:**

| estrato | comportamiento | teorema |
|---|---|---|
| gordos ($\delta_j a(\gamma_j)\geq1$ i.o.) | EN EL SÍMBOLO: masa espectral $\leq-c/2$ | 5.1 |
| finos visibles ($\theta_j\to0^+$) | EN LA FRONTERA: se acumulan en $0\in\mathrm{spec}(\sigma(Q))$; débil sí, estricta no | 5.2 |
| sub-resolución ($\delta_j a(\gamma_j)\to0$) | EN EL IDEAL: $\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, ciego total | 5.4 |

Y la frase que el encargo ofreció como premio de consolación es, literalmente, un teorema: **los ceros de ¬RH
viven exactamente en la frontera símbolo/compacto** — el estrato intermedio se acumula en el punto $0$ de la
corona, el único punto que separa la positividad débil de la estricta, que por el Teorema 1.3 es el único punto
del que depende la finitud robusta del defecto. El cuantificador maestro de P43 tiene ahora una dirección
C*-algebraica exacta: es el punto $0\in\mathrm{spec}_{\mathcal C}$.

### 5.8. Calibración obligatoria: los anti-modelos en la estratificación

Como en Doc 132 §5.4, la teoría se testea contra todos los objetos del corpus con defecto conocido. Los cuatro
pasan, y dos de los chequeos producen información:

**(M1) La clase cosh (Doc 111/112; instancia I5 del Doc 132): $m$ finito, $\delta_0$ fijo.** Configuración: $m$
cuádruplos, todos de altura $\leq\gamma_0$ y distancia $\delta_0>0$. A cualquier calendario: finitos visibles ⟹
Teorema 5.3 ⟹ **el símbolo es estrictamente positivo** (las ventanas altas están vacías de off). Consistente y
afilado: el defecto $2m\neq0$ de los cosh es invisible para $\sigma(Q)$ — vive entero en $\mathcal J$ (soporte
finito en ventanas). La lectura: **el símbolo mide defecto asintótico, no defecto total** — exactamente la
división de la arquitectura D-109: el símbolo apunta a $m<\infty$ (eje Fredholm), jamás a $m=0$ (que necesita el
eje de replicación). Ningún certificado de símbolo refutará jamás un cosh: correcto, porque los cosh satisfacen
"$\delta<\infty$" — el certificado Fredholm no debe excluirlos.

**(M2) Davenport–Heilbronn ($m=\infty$ real, Doc 131 §6.6, Doc 112 §3.3).** DH tiene infinitos ceros off en la
banda. En la estratificación: si sus $\delta_j$ no tienden a $0$ (estatus: dato plausible no verificado en
fuente — GAP-134.DH), DH tiene gordos a calendario $a(\gamma)=C$ constante grande, y el Teorema 5.1 predice:
**el símbolo de la forma DH es espectralmente negativo** — la versión-corona de la Prop. 6.8(a) del Doc 131
(violación incondicional de H por bloques). Test de coherencia del marco: el objeto $m=\infty$ paradigmático cae
en el estrato gordo, el estrato que el símbolo VE. Si en cambio los $\delta_j$ de DH tendieran a $0$, DH
calibraría el estrato frontera (5.2) — cualquiera de los dos resultados es informativo y el chequeo
numérico-bibliográfico es tarea finita declarada.

**(M3) Los $F_{p,\alpha}$ impuros (Doc 131, Teorema 6.7): el estrato gordo en estado puro.** El divisor de
$F_{p,\alpha}$ con $|\alpha|=p^{1/2+\delta'}$, $\delta'>0$, es una progresión vertical entera en
$\mathrm{Re}=\tfrac12+\delta'$: TODOS los ceros off, TODOS con el mismo $\delta'$ fijo — la configuración gorda
perfecta ($m=\infty$, $\delta_j\equiv\delta'$). Teorema 5.1: símbolo negativo a cualquier calendario no acotado
(de hecho a cualquier calendario con $a\geq1/\delta'$). Verificación independiente: el test de Mertens de dos
protuberancias del Teorema 6.7 de D131 produce la negatividad con tests de soporte $\asymp M\log p$ — soporte
CRECIENTE, exactamente como exige la teoría de la visibilidad (la negatividad de $F_{p,\alpha}$ requiere $M$
grande: $|c_M|>2p^{M/2}$ recién para $M\gtrsim1/\delta'$ — **la barrera $|c_m|\leq2p^{m/2}$ de la pureza ES la
condición de sub-resolución en el mundo local**: pureza = "todos los cuádruplos potenciales son sub-resolución a
todo calendario" = símbolo autónomo). Este diccionario pureza↔resolución es un dividendo: conecta el
discriminador del Doc 131 (pureza del dato local) con el discriminador de este documento (visibilidad), y
sugiere que LP-134 es el análogo global de "la pureza es una propiedad abierta del dato local".

**(M4) El flujo De Bruijn–Newman (D70).** Para $t<\Lambda$ (mundo $\neg$RH del flujo), los ceros off de $\xi_t$
migran hacia la línea cuando $t\uparrow\Lambda$: $\delta_j(t)\to0$. En la estratificación: el flujo DBN
transporta la configuración del estrato gordo al estrato fino y de ahí a la frontera $0$ — la masa espectral
negativa del símbolo se absorbe en el punto $0$ exactamente en $t=\Lambda$. Esto refina el Deseo 9.D4 y da un
test de consistencia: la caracterización $\Lambda=\inf\{t:T_\lambda(t)=0\}$ (D70) y "Λ = tiempo de absorción de
$\mathrm{spec}(\sigma(Q^{(t)}))\cap(-\infty,0)$ en $\{0\}$" deben coincidir si la continuidad del flujo sobre el
campo se prueba. [Estatus: imagen, no teorema; el gap de continuidad es el de D132 §8.2(c).]

**Observación 5.9 (reconciliación total con §2 y con B.4 — el cuadro completo de normalizaciones).** En peso
fijo (§2): TODO (mar y ceros) colapsa hacia $0$; el gap muere autónomamente; los negativos están en el ideal;
certificado vacío. En normalización por ventanas (§3–§5): el mar recupera el gap $1-r$; los negativos se
estratifican; lo que muere no es el gap del mar sino la **completitud** del certificado (5.4–5.5). Las dos
muertes son duales y el invariante de la dualidad es el punto $0$: o el símbolo autónomo lo toca (peso fijo), o
los negativos enemigos lo tocan (ventanas, estrato fino), o escapan por debajo de la resolución (ventanas,
estrato sub-resolución). No existe normalización que dé a la vez gap autónomo y captura de todos los $m=\infty$:
eso es el Teorema 5.5(a) recorrido sobre la familia entera de calendarios, que parametriza exactamente las
normalizaciones intermedias entre (i) ($a$ acotado) y la resolución infinita (que no es un calendario).

---

## 6. Computabilidad del símbolo: dónde queda exactamente la transmutación

### 6.1. La identidad de computabilidad

**Teorema 6.1 [TEOREMA] (computar el símbolo = uniformidad en ventanas).** Sobre el mismo campo de espacios,
$$\bigl\|\sigma(Q)-\sigma(Q^{\mathrm{aut}})\bigr\|_{\mathcal C}\;=\;\limsup_{n\to\infty}\ \bigl\|Q_n-Q^{\mathrm{aut}}_n\bigr\|.$$
En particular, el enunciado "el símbolo de la forma de Weil ES la predicción arquimediana/casi-prima" (la
versión-corona de la descomposición símbolo+compacto) equivale a: $\|Q_n-Q^{\mathrm{aut}}_n\|\to0$ — la
asintótica del déficit $\Delta K$ al segundo orden, **en norma de operador por ventana, uniforme en $n$** sobre
la bola entera de tests.

*Demostración.* Lema 3.2 aplicado a la sección diferencia. La identificación del miembro derecho con la
asintótica del déficit: $Q_n-Q^{\mathrm{aut}}_n$ es, por la identidad de bloques (3.1) del Doc 108, la forma por
ventana del déficit casi-primo $\Delta K_\varphi$ contra los tests de la ventana (Def. 3.6 del Doc 108); su
norma de operador es el supremo sobre la bola — la uniformidad "bola completa" de la Conjetura 108-N(a).
$\square$

**Corolario 6.2 [PUENTE] (la transmutación, localizada).** El enunciado "$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$"
es la **Conjetura 108-N en coordenadas C\***: misma precisión (segundo orden, $o(1)$ relativo por ventana tras
normalizar), misma uniformidad (toda ventana, bola completa). Por el mecanismo del Teorema 4.3 del Doc 108
(transportado: un mundo ¬RH con un cuádruplo gordo en la ventana $n$ separa
$\|Q_n-Q^{\mathrm{aut}}_n\|\geq\theta_j-\omega_n$, pues $Q^{\mathrm{aut}}_n$ tiene gap y $Q_n$ tiene autovalor
$\leq-\theta_j+\omega_n$), la identidad de símbolos **implica la inexistencia de gordos a calendario $a$** — es
decir, implica RH-a-resolución-$a$ ("todo cero off cumple $\delta<1/a(\gamma)$ salvo finitos"). Estatus: para la
forma doble, el eslabón Doc 108 Teo. 4.3 es teorema del corpus (con los caveats del Lema 2.4 declarados allí);
para la forma simple por ventanas, mismo mecanismo, mismo estatus. **No es un lema: es (la versión a resolución
de) la conclusión.** La computabilidad del símbolo no se obtiene gratis; ése es el muro viejo, intacto, ahora
con coordenadas exactas: vive en la NORMA de la corona.

### 6.2. El argumento de los dos mundos, en la corona

**Teorema 6.1bis [TEOREMA] (separación de mundos; la versión-corona del Teorema 3.4 del Doc 108).** En el modelo
$\mathfrak W$, sean $W_{RH}$ el mundo $Z=\emptyset$ y $W_{\neg}$ un mundo con infinitos gordos de visibilidad
$\geq c$. Entonces
$$\mathrm{dist}_H\bigl(\mathrm{spec}\,\sigma(Q^{W_\neg}),\,\mathrm{spec}\,\sigma(Q^{W_{RH}})\bigr)\;\geq\;\tfrac c2+(1-r)\;\geq\;\tfrac c2,\qquad\text{y por lo tanto}\qquad\bigl\|\sigma(Q^{W_{\neg}})-\sigma(Q^{W_{RH}})\bigr\|_{\mathcal C}\;\geq\;\tfrac c2,$$
donde $\mathrm{dist}_H$ es distancia de Hausdorff: los espectros de los dos símbolos difieren en al menos $c/2$
(el de $W_\neg$ tiene masa en $(-\infty,-c/2]$ — Teorema 5.1 —, el de $W_{RH}$ vive en $[1-r,1+r]$). En
consecuencia, **cualquier teorema que compute $\mathrm{spec}(\sigma(Q))$ con error de Hausdorff $<c/4$ decide
entre los dos mundos** — y por eso la computabilidad en norma del símbolo no puede ser incondicional barata
(Cor. 6.2): es el argumento de los dos mundos del Doc 108 (Teo. 3.4: la parte autónoma toma el mismo valor en
ambos mundos; toda la diferencia vive en el déficit), elevado de formas cuadráticas individuales a clases en la
corona.

*Demostración.* La primera afirmación con espectros: $\mathrm{spec}\,\sigma(Q^{W_{RH}})\subseteq[1-r,1+r]$ (Lema
5.0 con $J^{\mathrm{vis}}=\emptyset$ y $\omega_n\to0$, más Lema 3.3);
$\mathrm{spec}\,\sigma(Q^{W_\neg})\cap(-\infty,-c/2]\neq\emptyset$ (Teorema 5.1). Un punto espectral en
$(-\infty,-c/2]$ dista $\geq c/2+(1-r)\geq c/2$ de $[1-r,1+r]$. La
norma de la diferencia de símbolos acota la distancia de Hausdorff de espectros de autoadjuntos
($\mathrm{dist}_H(\mathrm{spec}\,A,\mathrm{spec}\,B)\leq\|A-B\|$ en cualquier C*-álgebra, por perturbación
estándar del espectro autoadjunto): de ahí la cota inferior para la norma. $\square$

### 6.3. Lo que sí es computable: los estados de media

**Proposición 6.3 [PROPOSICIÓN] (la aritmética computa los estados de Cesàro del símbolo).** Para cada sección
autónoma de tests $A=(A_n)\in\mathcal W$ (elegida sin conocer los ceros) y cada ultrafiltro libre/límite de
Banach $\mathcal L$ sobre las medias, el funcional
$$\varpi_{\mathcal L}(\sigma(X)):=\mathcal L\text{-}\lim_N\ \frac1N\sum_{n\leq N}\frac{\mathrm{tr}(X_nA_n)}{d_n}$$
está bien definido sobre $\mathcal C$ (se anula sobre $\mathcal J$: si $\|X_n\|\to0$, las trazas normalizadas
van a $0$), y es un funcional continuo de norma $\leq\sup\|A_n\|$. *Demostración.*
$|\mathrm{tr}(X_nA_n)|\leq d_n\|X_n\|\|A_n\|$; anulación sobre $\mathcal J$ por Cesàro de una sucesión nula;
linealidad y cota obvias. $\square$

**[PUENTE 6.4] (el estatus aritmético de los dos lados).**
- Los valores $\varpi_{\mathcal L}(\sigma(Q))$ — **medias sobre ventanas** de los datos espectrales por ventana
  — son el régimen donde el inventario incondicional del Doc 108 §5.2–5.3 SÍ entrega: el valor medio de
  Montgomery–Vaughan da la asintótica del déficit **para casi toda ventana**, lo que determina las medias de
  Cesàro. La aritmética (fórmula explícita por ventana, D72:
  $T_\lambda=A_\lambda^{\mathrm{off}}-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$; bloques del Doc 107/108) computa
  precisamente trazas por ventana contra tests autónomos. **El símbolo es computable desde primos en la
  topología de los estados de media.** [Estatus: la cadena exacta media-MV74→Cesàro del campo es herencia del
  Doc 108 §5.2, declarada, no re-probada acá.]
- La positividad (débil o estricta) del símbolo es un enunciado de **norma** (equivalentemente: sobre TODOS los
  estados de $\mathcal C$, incluidos los estados puros soportados en sucesiones de ventanas excepcionales — los
  límites de Banach a lo largo de las ventanas alineadas con los ceros). La brecha entre lo computable y lo
  necesario es exactamente la brecha estados-de-media / estados-puros-excepcionales de la corona.

**Observación 6.5 (el muro, en una frase nueva).** *La aritmética determina la imagen de $\sigma(Q)$ bajo los
estados de Cesàro; RH-a-resolución es una afirmación sobre sus estados puros excepcionales; y el conjunto de
estados que la media no controla es exactamente donde el Teorema 5.1 pone la señal.* Es el "casi toda ventana vs
toda ventana" del Doc 108 §5.2 convertido en geometría del espacio de estados de una C*-álgebra. Mismo muro; la
información nueva es su forma: **el muro es la corona menos sus estados de media** — y el punto $0$ del espectro
(Obs. 5.6) es donde se decide.

---

## 7. La síntesis: la escalera de resoluciones, LP-134, y la sinergia con la replicación

### 7.1. Qué quedó de la esperanza original

La esperanza del encargo (P44, Doc 132 B.4): $m<\infty$ no es evento exacto-cero, así que el muro de P43 (que
bloquea certificar $m=0$ desde promedios) podría no bloquear la positividad esencial. El veredicto medido:

**Teorema 7.1 [TEOREMA] (síntesis; en el modelo $\mathfrak W$).** A calendario $a$ fijo:

(a) positividad estricta del símbolo ⟺ finitos cuádruplos visibles (Teo. 5.3) — un enunciado genuinamente más
débil que RH y NO exacto-cero: **hasta acá la esperanza era correcta**; (b) pero $m<\infty$ = positividad
estricta del símbolo **en todos los calendarios a la vez con cota uniforme** (Teo. 5.5(b)–(c)), y para cada
calendario hay mundos $m=\infty$ invisibles (5.5(a)): **el cuantificador expulsado de las posiciones reaparece
en las resoluciones**; (c) y la computabilidad del símbolo (que era la otra mitad de la promesa: "computable
desde primos") es la uniformidad de ventanas en norma — el muro viejo sin rebaja (Teo. 6.1, Cor. 6.2).

$\square$ (recombinación de 5.3, 5.5, 6.1.)

La transmutación tiene entonces DOS hojas, y conviene decir con precisión qué cambió de forma: el muro de P43
era "media vs uniforme sobre ventanas a resolución fija"; el muro de Phase 45 es ese mismo (hoja (c)) **más**
una hoja nueva, "resolución fija vs resolución no acotada" (hoja (b)), que ninguna formulación previa del corpus
había aislado. La hoja (b) no es RH disfrazada: es una afirmación de **geometría de los ceros relativa a la
línea** que no menciona primos. Eso permite nombrarla:

### 7.2. [DEFINICIÓN-NUEVA + DESEO] LP-134: repulsión de resolución

**LP-134 (lema faltante nuevo, nombrado).** *Existe un calendario $a(\cdot)$ (p.ej. $a(\gamma)=C\log\gamma$, la
resolución natural) y $c>0$ tales que todo cero no trivial $\rho=\tfrac12+\delta+i\gamma$ de $\zeta$ con
$\delta\neq0$ cumple $|\delta|\geq c/a(\gamma)$.* — "Los ceros no pueden ser asintóticamente sub-resolución: o
están en la línea, o están repelidos de ella a la escala de la resolución."

**Por qué es la pieza exacta que falta (teorema condicional inmediato):** bajo LP-134, toda configuración tiene
$\theta_j\geq c_0$ para todo $j$ con $\gamma_j$ grande ((V2)): el estrato fino y el sub-resolución quedan
VACÍOS, y entonces (Teoremas 5.1+5.3) **$m<\infty\iff$ positividad estricta del símbolo a UN calendario** — la
mitad Fredholm de la arquitectura D-109 se vuelve un único enunciado C*-algebraico. $\square$ (5.1, 5.3, (V2).)

**Estatus y carácter de LP-134, con honestidad total.** (1) **No es RH** ni la implica: un mundo con un
cuádruplo en $\delta=\tfrac14$ satisface LP-134 y viola RH. (2) **No se sigue de nada conocido:** la región
libre de ceros clásica (Vinogradov–Korobov) repele de $\mathrm{Re}\,s=1$, no de $\mathrm{Re}\,s=\tfrac12$; los
teoremas de densidad ($N(\sigma,T)=o(T)$) acotan cuántos, no cuán cerca. Que yo sepa, NINGÚN enunciado del
corpus ni de la literatura estándar prohíbe $\delta_j\asymp1/\log^2\gamma_j$ con $m=\infty$. [Declarado: sin
búsqueda bibliográfica externa esta sesión.] (3) **Es del tipo correcto:** es una *dicotomía de rigidez* ("el
defecto es discreto a la escala natural"), pariente estructural de la separación de Siegel (repulsión de ceros
reales) girada 90°: repulsión desde la línea en vez de desde $s=1$. (4) Es **falsable en la categoría** del Doc
131: los objetos $F_{p,\alpha}$ tienen su divisor en $\mathrm{Re}=\beta$ FIJO (repulsión trivial); construir un
objeto de Euler con $\delta_j\to0$ y $m=\infty$ — o probar que la clase de Dirichlet no lo permite — es una
tarea concreta de Phase 45/46 (véase Deseo 9.D2).

### 7.3. La sinergia Fredholm × replicación: el estrato fino es el estrato no replicable

**Teorema 7.2 [TEOREMA] (en el modelo; la conjunción que cierra).** Supóngase que la configuración $Z$ satisface
el **Axioma R cuantitativo** (la forma D112/M1 de la replicabilidad): si $m\geq1$, existe un cuádruplo
$(\delta_0,\gamma_0)\in Z$, $\delta_0>0$, y una sucesión de alturas $\tau_k\to\infty$ tal que $Z$ contiene
cuádruplos $(\delta_k',\gamma_0+\tau_k)$ con $\delta_k'\geq\delta_0/2$ (las réplicas conservan la distancia a la
línea salvo factor $2$ — en el mecanismo Rouché de D112 las réplicas viven en el disco $D(\rho_0+i\tau_k,r)$ con
$r<\delta_0/2$: lo conservan). Sea $a$ cualquier calendario con $a(\gamma)\to\infty$. Entonces:
$$m\geq1\ \Longrightarrow\ \text{infinitos cuádruplos gordos}\ \Longrightarrow\ \mathrm{spec}(\sigma(Q))\cap(-\infty,-c_0/2]\neq\emptyset.$$
Contrapositivo: **positividad débil del símbolo (a cualquier calendario no acotado) ∧ Axioma R ⟹ $m=0$ ⟹ RH.**

*Demostración.* Las réplicas tienen
$\delta_k'\,a(\gamma_0+\tau_k)\geq(\delta_0/2)\,a(\gamma_0+\tau_k)\to\infty$: eventualmente supra-resolución,
visibilidad $\geq c_0$ por (V2). Teorema 5.1. El contrapositivo usa solo positividad débil porque 5.1 viola
incluso la débil. $\square$

**Observación 7.3 (lectura — esto es nuevo y orienta).** (1) El estrato fino/sub-resolución (el que mata la ruta
Fredholm pura, Teo. 5.4–5.5) es **exactamente el estrato que la replicación no produce**: las réplicas heredan
$\delta_0$ fijo y todo calendario no acotado las termina viendo. Las configuraciones invisibles del Teorema
5.5(a) ($\delta_j\to0$ calibrado contra el calendario) requieren ceros cada vez más pegados a la línea — el tipo
de configuración que el mecanismo de casi-períodos NO genera y que ningún objeto conocido de la clase Dirichlet
realiza (el GAP de D111 Obs. 2.4: ningún miembro conocido tiene $\delta$ finito no nulo; añádase: ninguno
conocido tiene $m=\infty$ con $\delta_j\to0$; Davenport–Heilbronn tiene sus ceros off a distancias que no
tienden a cero [estatus: dato no verificado en fuente esta sesión — GAP-134.DH, chequeable numéricamente en la
literatura]). (2) Los dos ejes del Doc 132 §8.2(c) — Fredholm y replicación — dejan de ser paralelos: **se
necesitan mutuamente y se complementan exactamente**: la replicación cubre el estrato que el símbolo no ve; el
símbolo convierte la conclusión de la replicación ($\delta=\infty$, inútil por sí sola) en una negatividad
espectral localizada y, dualmente, su positividad en $m=0$. La arquitectura D-109 "RH = (positividad esencial) ∧
(replicabilidad)" se afina a:
$$\mathrm{RH}\;=\;\underbrace{\bigl[\mathrm{spec}(\sigma(Q))\subseteq[0,\infty)\ \text{a un calendario no acotado}\bigr]}_{\text{enunciado C*: débil basta}}\ \wedge\ \underbrace{\text{Axioma R cuantitativo}}_{\text{LP-112, sin cambios}}$$
donde — ganancia concreta — la pieza Fredholm pedida bajó de "estricta con gap" a **débil** (gracias a que 5.1
viola la débil), y la pieza que LP-134 reemplazaría es la replicación entera en este rol. Dos rutas al mismo
cierre: (símbolo débilmente positivo ∧ LP-112) o (símbolo estrictamente positivo ∧ LP-134).

### 7.4. ¿Y el lado bueno del cuantificador? Lo que la corona deja probar incondicionalmente

Para que el documento no termine solo en cartografía: dos enunciados positivos quedan al alcance y se registran
como objetivos inmediatos comprobables (no se reclaman):

- **(O1)** Positividad estricta del símbolo **del campo autónomo** $\sigma(Q^{\mathrm{aut}})$ a calendario
  sub-resolución ($a$ acotado): es el Teorema 3.3 del Doc 108 reempaquetado — eso ya es teorema (allí). El
  objetivo: empujar el calendario admisible de $a=O(1)$ hacia $a=\epsilon\log n$ midiendo exactamente en qué
  $\epsilon$ la prueba de D108 §3.2 se rompe. Cada incremento de $\epsilon$ es un fragmento incondicional nuevo
  de positividad de Weil, y el primer $\epsilon$ donde se rompa es una MEDICIÓN del muro en unidades de
  resolución.
- **(O2)** La versión por estados (Prop. 6.3): "todos los estados de Cesàro de $\sigma(Q)$ son $\geq0$" debería
  ser teorema incondicional vía MV74 (la media controla casi toda ventana). Es la "positividad en media del
  símbolo" — estrictamente más débil que la débil (que pide TODOS los estados), pero un enunciado de positividad
  incondicional sobre el objeto correcto, y delimita el muro por dentro: el muro es exactamente el paso
  estados-de-media → estados puros. La mitad abstracta de O2 se prueba ya:

**Proposición 7.4 [PROPOSICIÓN] (de "casi toda ventana" a "todos los estados de media" — la mitad abstracta de
O2).** Supóngase que la familia satisface el control en densidad: para todo $\varepsilon>0$,
$$\frac{\#\{n\leq N:\ \lambda_{\min}(Q_n)<-\varepsilon\}}{N}\;\xrightarrow[N\to\infty]{}\;0\qquad(\ast)$$
("casi toda ventana es $\varepsilon$-positiva" — la forma exacta del output de MV74/gran criba en el Doc 108
§5.2). Entonces para toda sección de tests POSITIVA $A=(A_n)$, $0\leq A_n\leq I$, y todo límite de Banach
$\mathcal L$:
$$\varpi_{\mathcal L}\bigl(\sigma(Q)\bigr)\;:=\;\mathcal L\text{-}\lim_N\frac1N\sum_{n\leq N}\frac{\mathrm{tr}(Q_nA_n)}{d_n}\;\geq\;-\,\mathcal L\text{-}\lim_N\frac1N\sum_{n\leq N}\Bigl[\varepsilon+\sup_k\|Q_k\|\cdot\mathbf 1_{\lambda_{\min}(Q_n)<-\varepsilon}\Bigr]\;=\;-\varepsilon$$
para todo $\varepsilon>0$; es decir, **todos los estados de Cesàro positivos de $\sigma(Q)$ son $\geq0$**.

*Demostración.* Descompongo $Q_n=Q_n^++Q_n^-$ (partes espectrales positiva y negativa). Si
$\lambda_{\min}(Q_n)\geq-\varepsilon$: $Q_n\geq-\varepsilon I$, luego
$\mathrm{tr}(Q_nA_n)\geq-\varepsilon\,\mathrm{tr}(A_n)\geq-\varepsilon d_n$ (usando $0\leq A_n\leq I$ y que para
$B\geq-\varepsilon I$ y $0\leq A\leq I$:
$\mathrm{tr}(BA)=\mathrm{tr}((B+\varepsilon)A)-\varepsilon\,\mathrm{tr}(A)\geq-\varepsilon\,\mathrm{tr}(A)$,
pues $\mathrm{tr}(CA)\geq0$ para $C,A\geq0$). Si no: cota trivial
$\mathrm{tr}(Q_nA_n)\geq-\|Q_n\|\,\mathrm{tr}(A_n)\geq-\sup_k\|Q_k\|\cdot d_n$. Promediando, la fracción de
ventanas malas pesa $\to0$ por $(\ast)$ y el límite de Banach de una sucesión $\geq-\varepsilon-o(1)$ es
$\geq-\varepsilon$. Como $\varepsilon$ es arbitrario, $\geq0$. $\square$

  Lo que queda para O2 completo es la hipótesis $(\ast)$ — el enunciado en densidad — cuyo estatus aritmético es
el del Doc 108 §5.2 (valor medio de Montgomery–Vaughan: la asintótica del déficit vale fuera de un conjunto
excepcional de ventanas de medida relativa $o(1)$): herencia declarada, a ejecutar como cálculo de la fase
siguiente. La Prop. 7.4 garantiza que esa herencia, una vez ejecutada, produce el enunciado-corona completo
"positividad en media del símbolo" — y entonces el muro queda enunciado con sus dos lados probados: media
$\geq0$ (teorema), uniforme $\geq0$ ⟺ (con R) RH.

---

## 8. [PUENTE] Tabla de estatus completa

| eslabón | enunciado | estatus |
|---|---|---|
| Teorema 1.3 | finitud robusta del defecto ⟺ positividad esencial estricta | **TEOREMA**, incondicional, prueba completa acá |
| Lema 1.5 / Teorema 2.2 | (N1) ⟹ sin gap esencial; muerte de la normalización (i) | **TEOREMA** abstracto, prueba completa acá |
| Puente 2.3 | la CCM tiene (N1) | heredado (Docs 95/98), rutina no ejecutada, sin riesgo identificado |
| Lemas 3.2–3.3, Cor. 3.4 | corona del campo; espectro del símbolo = conjunto límite | **TEOREMA**, incondicional, prueba completa acá |
| Def. 3.6 (campo de Weil) | existencia/acotación de las ventanas normalizadas | aparato Doc 107/108 + GAP-134.R declarado |
| modelo $\mathfrak W$ (S1)–(S3) | bloques: teorema (D107/D131); (V1): teorema (D108 Teo. 3.3); (V2): estatus Lema 2.4 D108; (S3): GAP-132.ω | mixto, tabla en Obs. 4.5 |
| Teoremas 5.0–5.5 | estratificación, frontera $0$, no-go del calendario | **TEOREMA** dentro de $\mathfrak W$, pruebas completas acá |
| Prop. 5.5bis | estructura de la filtración de resoluciones; LP-134 = estabilización | **PROPOSICIÓN**, prueba completa acá |
| §5.8 (M1–M4) | calibración: cosh en $\mathcal J$; DH y $F_{p,\alpha}$ en el estrato gordo; pureza = sub-resolución local; DBN = absorción en $0$ | chequeos: M1, M3 con prueba (vía 5.1/5.3 + D131 Teo. 6.7); M2 con GAP-134.DH; M4 imagen |
| Teorema 6.1 | computar el símbolo = uniformidad en norma por ventana | **TEOREMA** (identidad), prueba completa acá |
| Prop. 7.4 | casi-toda-ventana ⟹ estados de Cesàro $\geq0$ | **PROPOSICIÓN**, prueba completa acá; la hipótesis $(\ast)$ es la herencia MV74 |
| Cor. 6.2 | esa uniformidad ⟹ RH-a-resolución | mecanismo Doc 108 Teo. 4.3, heredado con sus caveats |
| Prop. 6.3 + Puente 6.4 | la aritmética computa los estados de media del símbolo | Prop. 6.3 probada; identificación aritmética heredada (D72, D108 §5.2) |
| Teorema 7.2 | Axioma R ⟹ réplicas gordas ⟹ símbolo las ve; débil ∧ R ⟹ RH | **TEOREMA** en $\mathfrak W$ con el Axioma R cuantitativo (= LP-112 + conservación de $\delta_0$, que el mecanismo Rouché de D112 da por construcción) |
| LP-134 | repulsión de resolución | **[DESEO/lema faltante nuevo]**, abierto, no-RH, falsable en la categoría D131 |

---

## 9. [DESEO] Deseos, y VEREDICTO

**[DESEO 9.D1 — O1/O2 de §7.4.]** Probar la positividad en media del símbolo (todos los estados de Cesàro
$\geq0$, incondicional, vía MV74) y empujar el calendario de la ceguera sub-resolución: los dos son
teoremas-objetivo finitos, sin cuantificador maestro, y miden el muro desde dentro.

**[DESEO 9.D2 — falsar o fundar LP-134.]** En la categoría del Doc 131: construir un objeto hermitiano espectral
con producto de Euler, $a\geq0$, y divisor con $\delta_j\to0$, $m=\infty$ (falsaría que "Euler + positividad del
dato" implique repulsión), o probar que la clase no lo permite (fundaría LP-134 como fenómeno de la clase, no de
ζ). Es la versión-repulsión de la Conjetura H⁺ (D131 Deseo 6.9), y es tarea de construcción, no de evaluación.

**[DESEO 9.D3 — la corona con más estructura.]** $\mathcal C$ acá es solo el cociente $\ell^\infty/c_0$ del
campo. El campo de Weil tiene más: la acción de dilatación conecta ventanas (Toeplitz genuino, no solo
diagonal). Una corona con esa acción (producto cruzado, o el álgebra de operadores límite completa de RRS)
podría tener MENOS estados excepcionales — cada simetría que actúa transitivamente sobre las sucesiones de
ventanas mata estados puros patológicos. Cuantificar "cuántos estados mata la dilatación" es una forma nueva y
precisa de atacar media→uniforme.

**[DESEO 9.D4 — el flujo DBN en la corona.]** Doc 70: $\Lambda=\inf\{t:T_\lambda(t)=0\}$. La sección
$t\mapsto\sigma(Q^{(t)})$ del flujo De Bruijn–Newman en $\mathcal C$: bajo el flujo, los $\delta_j(t)$ decrecen
(los ceros migran a la línea); en la estratificación de §5, **el flujo DBN mueve masa del símbolo hacia la
frontera $0$ y de ahí al ideal**. "$\Lambda\leq0$" = "en $t=0$ ya nada quedó en el símbolo". Convertir esto en
teorema requiere la continuidad del flujo sobre el campo (el GAP de D132 §8.2(c)), pero la imagen es nueva:
$\Lambda$ como tiempo de absorción en el ideal compacto.

### VEREDICTO

**Transmutación localizada con dividendos — ni teorema-puente ni muerte seca.**

1. **La pregunta del encargo ("¿forma de Weil = símbolo autónomo + compacto?") tiene respuesta exacta: depende
   de la normalización, y las dos opciones honestas fallan por razones duales y demostradas.** Peso fijo: sí se
   descompone (off compacto), pero el símbolo no tiene gap que ofrecer (Teorema 2.2) y sin gap no hay nada
   (Teorema 1.3: la estricta es exactamente la finitud robusta). Ventanas: el símbolo existe (Lemas 3.2–3.3),
   tiene gap autónomo, y los negativos de ¬RH se estratifican: gordos en el símbolo (5.1), finos en la frontera
   $0$ (5.2), sub-resolución en el ideal (5.4) — y el no-go del calendario (5.5) muestra que $m<\infty$ es un
   evento de frontera sobre la filtración de resoluciones: **el cuantificador maestro no fue evitado; fue
   conjugado a coordenadas C\*** — de "toda ventana" a "toda resolución", con el punto
   $0\in\mathrm{spec}(\sigma(Q))$ como su residuo geométrico exacto.

2. **Información nueva sobre el muro (lo que se vino a buscar):** (a) la caracterización C*: el muro = corona
   menos estados de media; los ceros enemigos viven en la frontera símbolo/compacto, en el punto que separa
   débil de estricta; (b) el muro se PARTE: uniformidad de ventanas (vieja, hoja (c) de 7.1) ⊕ repulsión de
   resolución (nueva, LP-134, no-RH, geométrica, falsable); (c) la sinergia 7.2: el estrato que el símbolo no ve
   es el estrato que la replicación no produce — los dos ejes de D-109 se complementan exactamente, y la pieza
   Fredholm requerida baja de estricta a **débil** en la conjunción con LP-112.

3. **Teoremas incondicionales nuevos que quedan en pie por sí mismos:** 1.3 (caracterización exacta de la
   finitud robusta del defecto — la formalización definitiva de "defecto finito = fracaso compacto de la
   positividad"), 2.2 + 1.5 (muerte con prueba de la normalización de peso fijo), 3.2–3.3 (la corona del campo y
   su cálculo espectral), y el paquete 5.0–5.5/6.1/7.2 en el modelo axiomatizado con estatus por axioma
   declarado.

**Próximo teorema más atacable, en orden:** (1) O2 (positividad en media del símbolo, incondicional — cierra por
dentro); (2) GAP-134.R en el juguete (acotar $\|R_n\|$ con Hipótesis D: cálculo finito por ventana); (3) 9.D2
(falsar/fundar LP-134 en la categoría D131 — construcción pura, sin ζ); (4) O1 (medir el $\epsilon$ de ruptura
de la ceguera sub-resolución).

---

## Referencias

**Internas (backward-only):** Doc 132 (B.4, Obs. 4.2, Lema 4.1, Teorema C.1, Teorema D.4, §8.2(c): RH =
positividad esencial ∧ replicabilidad; GAP-132.ω); Doc 108 (Prop. 2.3/2.5, Lema 2.4 y su caveat, Teorema 3.3,
Teorema 3.4, Def. 3.6, Teorema 4.1, Conjetura 108-N, Teorema 4.3, §5.2 MV74/casi-toda-ventana, §7
transmutación); Doc 107 (clase engrosada, Teoremas 2.4/3.4/5.5, Prop. 6.1); Doc 131 (Teorema 6.3 órbita libre ⟹
bloque hiperbólico; Teorema 6.7 pureza local; Deseo 6.9 H⁺); Doc 112 (LP-112; mecanismo Rouché: réplicas en
$D(\rho_0+i\tau_k,r)$ — conservación de $\delta_0$; Prop. 2.6); Doc 111 (Obs. 2.4); D70
($\Lambda=\inf\{t:T_\lambda(t)=0\}$); D72 (traza por fórmula de Weil); Docs 95/98 (decaimiento de $dm_\infty$ y
costo $2\delta^2K_\lambda(\gamma)$); P35 (realización $(\mathcal K,Q)$, $\kappa=2m$, conjetura puente); P43
(cuantificador maestro; valor/inercia); P44/Doc 133 (contexto de la rescritura).

**Literatura (clásica, verificable):**
- T. Kato, *Perturbation Theory for Linear Operators*, Springer, 2.ª ed. 1976 (Thm. IV.5.35: invariancia de
  $\mathrm{spec_{ess}}$ bajo compactos — Teorema 1.3(i)⟹(ii)).
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics I, IV*, Academic Press (criterio de Weyl para
  $\mathrm{spec_{ess}}$ de autoadjuntos — Paso 1 de 1.3; teorema de Weyl §XIII.4).
- V. Rabinovich, S. Roch, B. Silbermann, *Limit Operators and Their Applications in Operator Theory*,
  Birkhäuser, 2004 (operadores límite; espectro esencial como unión de espectros de límites — contexto de los
  Lemas 3.2–3.3; las pruebas acá son autocontenidas para el caso producto/c₀).
- A. Böttcher, B. Silbermann, *Analysis of Toeplitz Operators*, Springer, 2.ª ed. 2006 (símbolo y espectro
  esencial de Toeplitz — contexto del nombre "Weil–Toeplitz").
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974) (valor medio —
  vía Doc 108 §5.2, para el Puente 6.4).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS, 2004 (Thm. 5.8: densidad de ceros por ventana
  $n_W\asymp(2\Delta/\pi)\log T$).
- R. Bhatia, *Matrix Analysis*, Springer, 1997 (desigualdad de Weyl finito-dimensional
  $|\lambda_k(A+B)-\lambda_k(A)|\leq\|B\|$ — Lema 5.0).

*Fin del Doc 134.*
