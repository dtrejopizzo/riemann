# Doc 132 — Teoría del defecto: la categoría 𝒫ol_δ de espacios polarizados defectuosos

**Programa:** Hipótesis de Riemann — Phase 44: MATEMÁTICA NUEVA.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** constructivo-creador. Invertir el hallazgo del Doc 130 (la polarización de Deninger lleva RH adentro) según el modelo Fredholm/Pontryagin: **no pedir la estructura perfecta; definir la categoría de los objetos cuya polarización falla, y hacer del fracaso un invariante con teoremas.** RH deja de ser "existe el espacio polarizado" y pasa a ser "el defecto del objeto-ζ es 0".

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total, sin obligación de precedente. **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD en este documento, prueba completa, estándar máximo; si un paso usa un resultado externo, se cita con precisión y se declara qué se usa. **[PUENTE]** = conexión con ζ/RH, con estatus honesto de cada eslabón (teorema / conjetura del programa / deseo). **[DESEO]** = declarado sin vergüenza, jamás disfrazado de teorema.

**Prerrequisitos leídos en fuente esta sesión:** Doc 130 (la circularidad de la ruta Kähler–Riemann: la métrica usa Hasse; ENUNCIADO-MÍNIMO-130: bajo ¬RH el espacio debe existir con la polarización fallando *visiblemente*); Doc 112 (dicotomía condicional m∈{0,∞}: reducción a LP-112, Prop. 2.6 de densidad cero, el mecanismo Rouché + casi-períodos + no-discretitud de {log p}); Doc 106 §3 (Prop. 3.1: neg.ind(Q₁⊗Q₂)=p₁q₂+q₁p₂; Prop. 3.3–3.6: crecimiento exponencial y esterilidad del tensor abstracto); Doc 118 (rigidez de momentos: Carleman + positividad del cono ⟹ la única medida con Δₙ constante es c·m_∞); Doc 125 (forma de intersección del cuadrado: signatura (1,ρ−1) en el juguete; Babaee–Huh: superficies tropicales con la signatura del índice de Hodge EQUIVOCADA existen).

---

## 0. Resumen ejecutivo

1. **[DEFINICIÓN-NUEVA] (§2)** La categoría **𝒫ol_δ** de *espacios polarizados con defecto*: objetos $(H,Q,P)$ — forma hermitiana $Q$ sobre $H$, subespacio primitivo marcado $P$ — con decoraciones opcionales (operador de Weil $C$, generador $A$, simetría funcional $S$, estructura real $\tau$). El **defecto** $\delta(X):=\mathrm{neg.ind}(Q_C|_P)\in\mathbb{N}\cup\{\infty\}$ está *siempre* definido: no presupone la existencia de nada perfecto. $\delta=0$ ⟺ el objeto está polarizado (Hodge–Riemann). Las instancias: el Pontryagin $(\mathcal K,Q)$ del programa ($\delta=\kappa=2m$, defecto reducido $\hat\delta=m$), la forma de intersección del cuadrado (Doc 125, $\delta$ = exceso de direcciones positivas sobre el primitivo), el objeto foliado del ENUNCIADO-MÍNIMO-130, y — crucial — **Babaee–Huh como prueba de población**: en la esquina tropical de la categoría existen objetos con $\delta\geq1$ *en la naturaleza*; la categoría no es un nombre vacío para "polarizado o patológico".

2. **[TEOREMA A] (§3) Aritmética del defecto.** $\delta$ es monótono bajo embebimientos isométricos, aditivo bajo $\oplus$, y bajo $\otimes$ satisface la **fórmula de Whitney del defecto** $\delta(X\otimes Y)=p_1\delta_2+\delta_1 p_2 = d_1\delta_2+d_2\delta_1-2\delta_1\delta_2$ (importada de Doc 106 Prop. 3.1, re-probada). Los únicos invariantes aditivos-multiplicativos son la dimensión $d$ y la signatura reducida $\sigma=p-\delta$ (dos caracteres), y $\delta=(d-\sigma)/2$: **el defecto es la diferencia de los dos caracteres** — en dimensión infinita ambos caracteres divergen y $\delta$ es lo que queda: un invariante de tipo Fredholm, no un carácter.

3. **[TEOREMA B] (§4) Rigidez kreiniana.** (B1) Si el operador de Gram es invertible, $\delta$ es localmente constante bajo deformaciones en norma (proyecciones de Riesz); (B2) $|\delta(Q+R)-\delta(Q)|\leq\mathrm{rang}(R)$; (B3) $\delta$ es semicontinuo inferior, y a lo largo de un camino continuo solo puede saltar en cruces de núcleo ($0\in\mathrm{spec}\,G_t$); (B4, **Weyl**) si $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$ — *positividad esencial* — entonces $\delta(G+K)<\infty$ para todo compacto $K$: **la finitud del defecto es una propiedad Fredholm**. (B6) La rigidez de momentos del Doc 118 axiomatizada como *rigidez de cono*: el defecto de separación de un criterio es $\dim(\mathrm{Anulador}\cap\mathrm{Cono})$.

4. **[TEOREMA C] (§5) Dicotomía abstracta.** Si un objeto posee UN vector negativo **replicable** — órbita bajo un grupo de $Q$-isometrías con alturas no acotadas y decaimiento de correlaciones $|Q(\gamma v,\gamma'v)|\leq\omega(|h(\gamma)-h(\gamma')|)$, $\omega\to0$ — entonces $\delta=\infty$. Corolario: en la clase de objetos donde todo defecto es replicable, $\delta\in\{0,\infty\}$. La prueba es Gershgorin sobre la matriz de Gram de las réplicas: convierte el Rouché del Doc 112 en un teorema de la categoría. Versión aproximada incluida (réplicas $\varepsilon$-isométricas bastan).

5. **[TEOREMA D] (§6) Paridad y clasificación en defecto bajo.** Para objetos espectrales ($A$ $Q$-simétrico, espectro primitivo con $z^2\notin\mathbb R$): los autovectores no-reales son neutros, las parejas $\{z,\bar z\}$ aportan planos hiperbólicos, $\delta=\sum_{\{z,\bar z\}}\dim H[z]$. Con la **simetría funcional** $S$ ($SAS^{-1}=-A$) el espectro viene en cuádruplos y $\delta$ es **PAR**: $\delta=1$ está prohibido. Sin $S$, los objetos con $\delta=1$ se clasifican: son exactamente los $\Pi_1$-bloques (un plano hiperbólico, forma normal única). El $\kappa=2m$ de P35 es la instancia.

6. **[TEOREMA E] (§7) El dividendo: el flujo tensorial y el ideal hiperbólico.** La **densidad de defecto** $\theta=\delta/d$ compone bajo $\otimes$ como el sesgo de un canal binario simétrico: $1-2\theta(X\otimes Y)=(1-2\theta_X)(1-2\theta_Y)$. Clasificación completa de las clases ⊗-estables: $\theta=0$ (polarizados, subcategoría tensorial) y $\theta=\tfrac12$ (hiperbólicos = Witt-triviales, **ideal absorbente**); todo lo demás fluye a $\theta=\tfrac12$ a tasa exponencial exacta $|1-2\theta|^k$. Esto explica DESDE DENTRO la esterilidad del tensor (Doc 106 Prop. 3.6) y produce el hallazgo estructural para el puente: **la parte off-crítica del objeto-ζ es hiperbólica (2m,2m), Witt-trivial, $\theta=\tfrac12$: vive exactamente en el ideal absorbente, invisible para todo invariante multiplicativo.**

7. **[PUENTE] (§8)** El objeto-ζ y RH = "$\delta(Z_\zeta)=0$". La arquitectura D-109 del programa se reescribe como la conjunción de los dos ejes de la teoría: **RH = (positividad esencial: eje Fredholm, B4) ∧ (replicabilidad: eje simetría, C)**. Honestidad total: aplicado a $Z_\zeta$, el axioma de replicabilidad restante ES LP-112 disfrazada — la teoría no la prueba; la aísla como EL axioma, separa las hipótesis ya probadas (alturas no acotadas = Lema 2.2 de D112; anti-modelos cosh fallan donde la teoría predice) y muestra que la dicotomía solo necesita datos de UNA órbita, sin uniformidad. Y reformula ENUNCIADO-MÍNIMO-130: la no-circularidad de Deninger ⟺ su construcción define un funtor con valores en 𝒫ol_δ *total* (definido también donde $\delta>0$), no solo en la fibra $\delta=0$.

---

## 1. La inversión creativa: del fracaso de la polarización al invariante

El Doc 130 estableció (con sesgo fuerte) que el espacio "Kähler–Riemann" de Spec ℤ no se sabe construir sin RH: la métrica que polariza usa la localización de los ceros como input. La reacción defensiva sería buscar otra métrica. La reacción **creadora** — el linaje de Kreĭn — es otra:

> Cuando una estructura positiva no existe, la teoría correcta no es la de los espacios donde existe, sino la de los espacios donde falla *de manera medible*. Fredholm: la no-invertibilidad se vuelve el índice. Pontryagin: la no-positividad se vuelve $\kappa$. Aquí: la no-polarizabilidad se vuelve $\delta$.

El requisito de diseño, dictado por el ENUNCIADO-MÍNIMO-130: el invariante debe estar definido **para todo objeto del tipo relevante, exista o no la polarización** — porque la prueba de fuego de la no-circularidad (NC4 del test R-NC) es precisamente que bajo ¬RH el objeto exista con el defecto *visible*. Una categoría donde solo viven los objetos perfectos no puede ni siquiera enunciar NC4. 𝒫ol_δ es el receptáculo donde NC4 es un enunciado.

Tres rigideces del corpus deben quedar contenidas como teoremas modelo: la aritmética exacta del índice bajo productos (Doc 106), la dicotomía $m\in\{0,\infty\}$ condicional a un lema de réplica (Doc 112), y la rigidez de momentos (Doc 118). Las tres aparecen abajo como Teoremas A, C y B6 respectivamente.

---

## 2. [DEFINICIÓN-NUEVA] La categoría 𝒫ol_δ

**Convenciones.** Forma hermitiana = sesquilineal, lineal en la primera variable, $Q(y,x)=\overline{Q(x,y)}$. Para un subespacio $W\subseteq H$, $\mathrm{neg.ind}(Q|_W):=\sup\{\dim N: N\subseteq W$ subespacio con $Q(x,x)<0\ \forall x\in N\setminus\{0\}\}\in\mathbb{N}\cup\{\infty\}$. Análogamente $\mathrm{pos.ind}$.

**Definición 2.1 (objeto de 𝒫ol_δ).** Un *espacio polarizado con defecto* es una terna
$$X=(H,\,Q,\,P)$$
donde $H$ es un $\mathbb C$-espacio vectorial, $Q$ una forma hermitiana sobre $H$ (no se exige no-degeneración ni positividad de nada), y $P\subseteq H$ un subespacio marcado, el **primitivo** — el lugar donde la polarización *debería* ser definida.

**Decoraciones opcionales** (cada una, cuando está, es parte del dato del objeto y los morfismos la respetan):

- **(c)** un *operador de Weil candidato* $C\in GL(H)$ con $C^2=\mathrm{id}$, $Q(Cx,Cy)=Q(x,y)$, $CP=P$. Induce la forma hermitiana torcida $Q_C(x,y):=Q(Cx,y)$ (hermitiana: $Q_C(y,x)=Q(Cy,x)=\overline{Q(x,Cy)}=\overline{Q(Cx,C^2y)}=\overline{Q_C(x,y)}$). Si no hay $C$, se toma $C=\mathrm{id}$, $Q_C=Q$.
- **(a)** un *generador* $A\in\mathrm{End}(H)$ $Q$-simétrico: $Q(Ax,y)=Q(x,Ay)$, $AP\subseteq P$.
- **(s)** una *simetría funcional* $S\in GL(H)$ con $S^2=\mathrm{id}$, $SP=P$, $Q(Sx,Sy)=\epsilon_S\,Q(x,y)$ con $\epsilon_S\in\{+1,-1\}$, y (si hay $A$) $SAS^{-1}=-A$.
- **(r)** una *estructura real* $\tau:H\to H$ antilineal, $\tau^2=\mathrm{id}$, $\tau P=P$, $Q(\tau x,\tau y)=Q(y,x)$, y (si hay $A$) $\tau A=A\tau$.

**Definición 2.2 (el defecto).**
$$\boxed{\;\delta(X):=\mathrm{neg.ind}\bigl(Q_C|_P\bigr)\;\in\;\mathbb{N}\cup\{\infty\}.\;}$$
Cuando además hay simetría funcional $S$ y el espectro primitivo es de tipo cuádruplo (§6), el **defecto reducido** es $\hat\delta(X):=\delta(X)/2$ (entero por el Teorema D).

$\delta$ está definido para TODO objeto: es un supremo de dimensiones, nunca requiere existencia de descomposiciones, métricas, ni completaciones. El objeto está **polarizado** si $\delta(X)=0$, es decir $Q_C|_P\geq0$; está **estrictamente polarizado** si además $Q_C|_P$ es definida (las relaciones bilineales de Hodge–Riemann clásicas).

**Definición 2.3 (morfismos).** $f:X_1\to X_2$ es una aplicación lineal $f:H_1\to H_2$ con $Q_2(fx,fy)=Q_1(x,y)$, $f(P_1)\subseteq P_2$, y compatibilidad con las decoraciones presentes ($fC_1=C_2f$, etc.). 𝒫ol_δ tiene sumas directas y productos tensoriales evidentes:
$$X_1\oplus X_2=(H_1\oplus H_2,\,Q_1\oplus Q_2,\,P_1\oplus P_2),\qquad
X_1\otimes X_2=(H_1\otimes H_2,\,Q_1\otimes Q_2,\,P_1\otimes P_2),$$
con $(Q_1\otimes Q_2)(u_1\otimes u_2,v_1\otimes v_2)=Q_1(u_1,v_1)Q_2(u_2,v_2)$, $C_{\otimes}=C_1\otimes C_2$. El objeto unidad es $\mathbf 1=(\mathbb C,\,z\bar w,\,\mathbb C)$, con $\delta(\mathbf 1)=0$.

**Definición 2.4 (clase topológica).** Un objeto es *de tipo Hilbert* si $H$ es un espacio de Hilbert $(\,\langle\cdot,\cdot\rangle\,)$, $P$ cerrado, y $Q_C(x,y)=\langle Gx,y\rangle$ con $G=G^*$ acotado (el **operador de Gram**). Entonces (Lema 4.1) $\delta(X)=\dim\mathrm{ran}\,E_G(-\infty,0)$ sobre $P$. Esta clase es donde viven los teoremas de rigidez §4.

### 2.5. Las instancias (los objetos del programa SON objetos de 𝒫ol_δ)

**(I1) El Pontryagin del programa.** $Z_\zeta:=(\mathcal K,\,Q,\,P_{\mathrm{off}})$, donde $(\mathcal K,Q)$ es el espacio de la forma de Weil del programa con $\kappa(Q)=2m$ (P35: identificación conjetural $\kappa=\mathrm{neg.ind}(H_C)$, programa V.1–V.4 — estatus: **conjetura puente del programa**, declarada), $A=H_C$ (generador del flujo de escala, $Q$-simétrico), $S$ inducida por $s\mapsto1-s$, $\tau$ por conjugación, $P_{\mathrm{off}}$ = suma de los subespacios radicales con autovalor $z=\rho-\tfrac12$, $z^2\notin\mathbb R$. Entonces $\delta(Z_\zeta)=\kappa=2m$ y $\hat\delta(Z_\zeta)=m$ (Teorema D + P35). **RH ⟺ δ(Z_ζ)=0.**

**(I2) La forma de intersección del cuadrado (Doc 125).** $X_\square:=(\mathrm{NS}_{\mathbb R}\otimes\mathbb C,\,-Q_{\mathrm{int}},\,H^{\perp})$ con $Q_{\mathrm{int}}$ la forma de intersección y $H$ una clase amplia. El índice de Hodge dice $-Q_{\mathrm{int}}|_{H^\perp}>0$; por tanto $\delta(X_\square)=\mathrm{pos.ind}(Q_{\mathrm{int}}|_{H^\perp})$ = **exceso de direcciones positivas** sobre el primitivo. Índice de Hodge ⟺ $\delta(X_\square)=0$. En el juguete $C_p\times C_p$ de Doc 125, $\delta=0$ [CÁLCULO de Doc 125, signatura $(1,2)$].

**(I3) Babaee–Huh: la categoría está poblada.** [DATO — Doc 125 §5.5, arXiv:1502.00299] Existe una superficie tropical cuya forma de intersección NO tiene la signatura $(1,\rho-1)$: su objeto $X_{BH}$ tiene $\delta(X_{BH})\geq1$. Esto es decisivo para la *legitimidad* de la teoría: el defecto positivo **ocurre en la naturaleza matemática**, no solo en mundos contrafácticos ¬RH. 𝒫ol_δ no es la subcategoría $\delta=0$ con decorado.

**(I4) El objeto foliado del ENUNCIADO-MÍNIMO-130.** Si existiera la construcción que el Doc 130 §5.3 pide — polarización foliada sobre Spec ℤ definida por geometría pura, válida cualquiera sea la posición de los ceros — definiría un objeto $X_{\mathrm{fol}}=(\bar H^1_{\mathcal F},\,Q_{\mathrm{pol}},\,\mathrm{Prim})$ en 𝒫ol_δ con $\delta(X_{\mathrm{fol}})$ computable en ambos mundos, y NC4 pasaría ($\delta\geq1$ visible bajo ¬RH). Estatus: **[DESEO]** — el objeto no está construido; la categoría es el codominio que el deseo necesita (§8.4).

**(I5) Los anti-modelos cosh (Doc 111/112).** $F=P_1\cdots P_m\cosh(a(s-\tfrac12))$ con $m$ cuádruplos: forma de Weil análoga con $\delta=2m$ finito no nulo, SIN aritmética. Estos objetos existen en 𝒫ol_δ y la teoría debe (y va a, §5.4) explicar por qué su defecto finito no se replica: su grupo de simetrías de altura no acotada es vacío.

**(I6) El caso clásico polarizado.** Toda estructura de Hodge polarizada (superficie de Kähler compacta, Castelnuovo–Severi sobre $C\times C$) es un objeto con $\delta=0$ probado por geometría externa al espectro: el "milagro de Weil" es, en este lenguaje, un **teorema de anulación de defecto con prueba externa**. El programa entero busca el análogo para (I1).

---

## 3. [TEOREMA A] La aritmética del defecto

A lo largo de §3, los objetos son de dimensión finita con $Q_C|_P$ **no degenerada** salvo indicación; $d(X):=\dim P$, $(p,\delta)$ = signatura de $Q_C|_P$ (Sylvester), $\sigma(X):=p-\delta$ la *signatura reducida*. Escribimos $Q$ por $Q_C$ (la torsión por $C$ ya está absorbida).

**Lema A.0 (descomposición de índice finito; sin hipótesis de dimensión).** Sea $Q$ hermitiana sobre $W$ con $q:=\mathrm{neg.ind}(Q|_W)<\infty$ y sea $N\subseteq W$ negativo maximal ($\dim N=q$). Entonces $W=N\oplus N^{\perp_Q}$ y $Q\geq0$ sobre $N^{\perp_Q}$.

*Demostración.* $Q|_N$ es negativa definida, en particular no degenerada; luego $W=N\oplus N^{\perp_Q}$ (algebraico estándar: para $w\in W$, la funcional $Q(w,\cdot)|_N$ se representa por un único $n\in N$, y $w-n\in N^{\perp_Q}$). Si existiera $w\in N^{\perp_Q}$ con $Q(w,w)<0$, entonces $N\oplus\mathbb Cw$ sería negativo definido (la matriz de Gram es diagonal por bloques con ambos bloques negativos) de dimensión $q+1$, contradiciendo la maximalidad. $\square$

**Teorema A.1 (monotonía y aditividad).**
(i) Si $f:X_1\to X_2$ es un morfismo, entonces $\delta(X_1)\leq\delta(X_2)$. *El defecto no se puede borrar por embebimiento isométrico.*
(ii) $\delta(X_1\oplus X_2)=\delta(X_1)+\delta(X_2)$, sin hipótesis de dimensión ni de no-degeneración.

*Demostración.* (i) Sea $N\subseteq P_1$ negativo. $f|_N$ es inyectiva: $fx=0\Rightarrow Q_1(x,x)=Q_2(fx,fx)=0\Rightarrow x=0$. Y $f(N)\subseteq P_2$ es negativo porque $f$ es isométrico. Luego todo testigo de $\delta(X_1)$ produce uno de $\delta(X_2)$.
(ii) "≥": suma de testigos. "≤": si algún $\delta(X_i)=\infty$ no hay nada que probar. Si ambos finitos, por el Lema A.0 escribimos $P_i=N_i\oplus R_i$ con $Q_i\geq0$ en $R_i$, $\dim N_i=\delta(X_i)$. Sea $N\subseteq P_1\oplus P_2$ negativo y $\pi:N\to N_1\oplus N_2$ la proyección a lo largo de $R_1\oplus R_2$. $\ker\pi=N\cap(R_1\oplus R_2)$; pero $Q_1\oplus Q_2\geq0$ sobre $R_1\oplus R_2$ y $<0$ sobre $N\setminus\{0\}$, luego $\ker\pi=0$ y $\dim N\leq\delta(X_1)+\delta(X_2)$. $\square$

**Teorema A.2 (fórmula de Whitney del defecto; Doc 106 Prop. 3.1, re-probada).** Para $X_1,X_2$ de dimensión finita con formas no degeneradas de signaturas $(p_1,\delta_1)$, $(p_2,\delta_2)$:
$$\mathrm{sig}\bigl(Q_1\otimes Q_2|_{P_1\otimes P_2}\bigr)=(p_1p_2+\delta_1\delta_2,\;p_1\delta_2+\delta_1p_2),
\qquad\text{en particular}\qquad
\boxed{\;\delta(X_1\otimes X_2)=p_1\delta_2+\delta_1p_2.\;}$$

*Demostración.* Bases $Q_i$-ortonormales $\{e^{(i)}_a\}$ con signos $\varepsilon^{(i)}_a\in\{\pm1\}$ (Sylvester). La base $\{e^{(1)}_a\otimes e^{(2)}_b\}$ es $Q_1\otimes Q_2$-ortogonal con signos $\varepsilon^{(1)}_a\varepsilon^{(2)}_b$; el signo es $-1$ exactamente cuando los factores difieren: $p_1\delta_2+\delta_1p_2$ pares. No-degeneración: base ortogonal sin vectores isótropos. $\square$

**Corolario A.3 (formas equivalentes y consecuencias).** Con $d_i=p_i+\delta_i$, $\sigma_i=p_i-\delta_i$:
(i) **inclusión-exclusión:** $\delta(X_1\otimes X_2)=d_1\delta_2+d_2\delta_1-2\delta_1\delta_2$;
(ii) **dos caracteres:** $d(X_1\otimes X_2)=d_1d_2$ y $\sigma(X_1\otimes X_2)=\sigma_1\sigma_2$; y $\delta=(d-\sigma)/2$;
(iii) **superaditividad estricta:** $\delta(X_1\otimes X_2)-(\delta_1+\delta_2)=(p_1-1)\delta_2+(p_2-1)\delta_1\geq0$, estricta en cuanto un factor tiene $p\geq2$ y el otro $\delta\geq1$;
(iv) **potencias:** $\delta(X^{\otimes k})=\tfrac{(p+\delta)^k-(p-\delta)^k}{2}=\tfrac{d^k-\sigma^k}{2}$;
(v) **estabilidad de la polarización:** $\delta_1=\delta_2=0\Rightarrow\delta(X_1\otimes X_2)=0$; recíprocamente, si $p_1,p_2\geq1$ y $\delta(X_1\otimes X_2)=0$, entonces $\delta_1=\delta_2=0$. *Los objetos polarizados forman una subcategoría tensorial, y el defecto no puede esconderse en un producto.*

*Demostración.* (i)–(iv): cálculo directo desde A.2 ($\sigma$ multiplicativo: $\sigma_{\otimes}=(p_1p_2+\delta_1\delta_2)-(p_1\delta_2+\delta_1p_2)=(p_1-\delta_1)(p_2-\delta_2)$). (v): si $\delta_{\otimes}=p_1\delta_2+\delta_1p_2=0$ con $p_i\geq1$, cada sumando es cero. $\square$

**Proposición A.4 (los dos caracteres son los únicos; el defecto no es un carácter).** Sea $\varphi$ un invariante de isomorfismo de objetos finito-dimensionales no degenerados, con valores en un dominio íntegro de característica 0, aditivo bajo $\oplus$, multiplicativo bajo $\otimes$, con $\varphi(\mathbf 1)=1$. Entonces $\varphi=d$ o $\varphi=\sigma$. En particular $\delta$ no es multiplicativo, y es la mitad de la diferencia de los dos únicos caracteres.

*Demostración.* El semianillo de clases de isomorfismo es $\mathbb N^2$ vía $(p,\delta)$, con producto de A.2; su anillo de Grothendieck es $\mathbb Z[\varepsilon]/(\varepsilon^2-1)$ identificando la clase de $X$ con $p+\delta\varepsilon$ (chequeo: $(p_1+\delta_1\varepsilon)(p_2+\delta_2\varepsilon)=(p_1p_2+\delta_1\delta_2)+(p_1\delta_2+\delta_1p_2)\varepsilon$ ✓). Un homomorfismo de anillos $\varphi$ a un dominio íntegro queda determinado por $u:=\varphi(\varepsilon)$, que satisface $u^2=1$, luego $u=\pm1$ (dominio íntegro). $u=1$ da $d$; $u=-1$ da $\sigma$. $\square$

**Corolario A.5 (dimensión infinita: el defecto es Fredholm, no carácter; Doc 106 Prop. 3.4 como instancia).** Si $p(X)=\infty$ y $\delta(X)\geq1$, entonces $\delta(X\otimes X)=\infty$. *Demostración.* Con $v_-$ negativo y $\{e_n\}\subseteq P$ ortonormal positivo, los $e_n\otimes v_-$ son ortogonales de cuadrado $-1$. $\square$
Lectura: en dimensión infinita los dos caracteres $d,\sigma$ divergen y la fórmula $\delta=(d-\sigma)/2$ pierde sentido; lo que sobrevive es el §4: $\delta$ como dimensión de un subespacio espectral negativo, estable bajo perturbaciones — exactamente el formato del índice de Fredholm. **El defecto es a la polarización lo que el índice es a la invertibilidad.**

**Proposición A.6 (dual y conjugado).** Para $X$ finito-dimensional no degenerado: $\delta(X^*)=\delta(X)$ y $\delta(\bar X)=\delta(X)$, donde $X^*=(H^*,Q^*,P^{*})$ con $Q^*(\varphi_x,\varphi_y):=Q(y,x)$ vía el anti-isomorfismo $y\mapsto\varphi_y=Q(\cdot,y)$, y $\bar X$ el conjugado con $\bar Q(x,y):=Q(y,x)$.

*Demostración.* En una base ortonormal de signos $\varepsilon_a$, $Q^*(\varphi_{e_a},\varphi_{e_a})=Q(e_a,e_a)=\varepsilon_a$ y $\bar Q(e_a,e_a)=\varepsilon_a$: mismas signaturas. $\square$

---

## 4. [TEOREMA B] Rigidez: cuándo el defecto no se mueve

Objetos de tipo Hilbert (Def. 2.4): $Q(x,y)=\langle Gx,y\rangle$ sobre $P$ (escribimos $H$ por $P$ para aligerar), $G=G^*\in\mathcal B(H)$.

**Lema 4.1 (el defecto es espectral).** $\delta=\dim\mathrm{ran}\,E_G(-\infty,0)$, donde $E_G$ es la medida espectral de $G$.

*Demostración.* Sobre $N_-:=\mathrm{ran}\,E_G(-\infty,0)$: $\langle Gx,x\rangle=\int_{(-\infty,0)}\lambda\,d\|E_\lambda x\|^2<0$ para $x\neq0$: $N_-$ es negativo, luego $\delta\geq\dim N_-$. Recíprocamente, si $N$ es negativo, $E_G(-\infty,0)|_N$ es inyectiva: si $E_G(-\infty,0)x=0$ entonces $x\in\mathrm{ran}\,E_G[0,\infty)$ y $\langle Gx,x\rangle\geq0$, imposible en $N\setminus\{0\}$. Luego $\dim N\leq\dim N_-$. $\square$

**Teorema B.1 (estabilidad de Riesz: el defecto es localmente constante en el régimen no degenerado).** Sea $G$ invertible, $g:=\mathrm{dist}(0,\mathrm{spec}\,G)>0$. Entonces para todo $G'=G'^*$ con $\|G'-G\|<g$: $G'$ es invertible y $\delta(G')=\delta(G)$.

*Demostración.* Para $|\lambda|<g-\|G'-G\|$, $G'-\lambda=(G-\lambda)\bigl(1+(G-\lambda)^{-1}(G'-G)\bigr)$ es invertible pues $\|(G-\lambda)^{-1}\|\leq(g-|\lambda|)^{-1}$ y $\|(G-\lambda)^{-1}(G'-G)\|<1$: la brecha espectral en torno de $0$ persiste, de ancho $\geq g':=g-\|G'-G\|$ a lo largo de todo el segmento $G_t:=G+t(G'-G)$, $t\in[0,1]$, con $M:=\sup_t\|G_t\|\leq\|G\|+g$. Sea $\Gamma$ el borde del rectángulo $\{-M-1\leq\mathrm{Re}\,z\leq-g'/2,\ |\mathrm{Im}\,z|\leq M+1\}$: $\Gamma$ encierra $\mathrm{spec}(G_t)\cap(-\infty,0)$ y dista $\geq\rho:=\min(g'/2,1)$ de $\mathrm{spec}(G_t)$ para todo $t$ (el espectro es real y evita $(-g',g')$). Por cálculo funcional de Riesz, $E_t:=E_{G_t}(-\infty,0)=\frac{1}{2\pi i}\oint_\Gamma(z-G_t)^{-1}dz$, y por la identidad del resolvente
$$\|E_t-E_s\|\leq\frac{|\Gamma|}{2\pi}\,\rho^{-2}\,\|G_t-G_s\|.$$
Particionando $[0,1]$ en pasos con $\|E_t-E_s\|<1$, basta el lema clásico: si $P,Q$ son proyecciones ortogonales con $\|P-Q\|<1$ entonces $\dim\mathrm{ran}\,P=\dim\mathrm{ran}\,Q$ ($P|_{\mathrm{ran}\,Q}$ es inyectiva: $x\in\mathrm{ran}\,Q$, $Px=0\Rightarrow\|x\|=\|(Q-P)x\|<\|x\|$; y simétricamente). Con el Lema 4.1, $\delta(G_t)$ es constante. $\square$

**Teorema B.2 (perturbación de rango finito).** Para $R=R^*$ de rango $r<\infty$: $|\delta(G+R)-\delta(G)|\leq r$ (con la convención $\infty-n=\infty$: si un lado es infinito, el otro también).

*Demostración.* Sea $N$ negativo para $G+R$ con $\dim N=n$ (cualquier $n\leq\delta(G+R)$). Sobre $N\cap\ker R$ (codimensión $\leq r$ en $N$, pues $\ker R=(\mathrm{ran}\,R)^\perp$ tiene codimensión $r$): $\langle Gx,x\rangle=\langle(G+R)x,x\rangle<0$. Luego $\delta(G)\geq n-r$, es decir $\delta(G)\geq\delta(G+R)-r$. Intercambiando $G\leftrightarrow G+R$ (con $-R$), la otra desigualdad. $\square$

**Teorema B.3 (semicontinuidad y localización de saltos).** (i) $\delta$ es semicontinuo inferior en norma: si $\delta(G)\geq n$, existe $\varepsilon>0$ tal que $\delta(G')\geq n$ para $\|G'-G\|<\varepsilon$. (ii) A lo largo de un camino norm-continuo $t\mapsto G_t$, la función $t\mapsto\delta(G_t)$ es constante en cada subintervalo donde $G_t$ es invertible; **solo puede cambiar en cruces de núcleo** $\{t:0\in\mathrm{spec}\,G_t\}$.

*Demostración.* (i) Tómese $N$ negativo, $\dim N=n<\infty$; por compacidad de la esfera unitaria de $N$, $\langle Gx,x\rangle\leq-c\|x\|^2$ en $N$ para algún $c>0$; cualquier $\|G'-G\|<c$ mantiene $N$ negativo. (ii) Inmediato de B.1 más conexidad. $\square$

**Teorema B.4 (Weyl: la finitud del defecto es Fredholm).** Si $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$ (**positividad esencial**: $G$ positivo módulo compactos con gap), entonces $\delta(G)<\infty$; y para todo compacto autoadjunto $K$, $\delta(G+K)<\infty$.

*Demostración.* Si $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$, entonces $\mathrm{spec}(G)\cap(-\infty,0]$ consiste en autovalores aislados de multiplicidad finita; sus únicos puntos de acumulación posibles pertenecerían a $\mathrm{spec}_{\mathrm{ess}}(G)$, que es disjunto de $(-\infty,0]$; como además ese conjunto es compacto (espectro acotado) y discreto, es finito, y cada uno aporta multiplicidad finita: $\dim\mathrm{ran}\,E_G(-\infty,0)<\infty$, i.e. $\delta(G)<\infty$ (Lema 4.1). Por el teorema de Weyl sobre la invariancia del espectro esencial bajo perturbaciones compactas [Kato, *Perturbation Theory*, Thm. IV.5.35; Reed–Simon IV, §XIII.4], $\mathrm{spec}_{\mathrm{ess}}(G+K)=\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$, y se aplica lo anterior a $G+K$. $\square$

**Observación 4.2 (la frase de linaje, ahora teorema).** B.4 dice exactamente: *defecto finito = fracaso compacto de la positividad*. La positividad esencial es "polarización módulo compactos"; el defecto es la dimensión del subespacio donde el fracaso se realiza. Es la traducción literal del esquema de Fredholm (invertibilidad módulo compactos ⟹ índice finito) a la polarización. Nótese el contraejemplo que delimita: $G=\mathrm{diag}(-1/n)$ tiene $\mathrm{spec}_{\mathrm{ess}}=\{0\}\subseteq[0,\infty)$ pero $\delta=\infty$ — el gap esencial ($0\notin\mathrm{spec}_{\mathrm{ess}}$) no es decorativo.

**Proposición B.5 (qué deformaciones NO mueven el defecto — síntesis).** $\delta$ es invariante bajo: (a) isomorfismos de 𝒫ol_δ; (b) deformaciones continuas en el régimen no degenerado (B.1, B.3); (c) perturbaciones de rango finito, módulo error $\leq r$ (B.2); y la *clase de finitud* $\{\delta<\infty\}$ es invariante bajo perturbaciones compactas en presencia de gap esencial (B.4). $\delta$ puede saltar solo en cruces de núcleo, y el salto en un cruce de núcleo de dimensión $k$ es $\leq k$ (B.2 aplicado al rango espectral que cruza, cuando es finito). $\square$ (recombinación de B.1–B.4).

**Proposición B.6 (rigidez de cono: el esqueleto del Doc 118, axiomatizado).** Sean $V$ un espacio vectorial real, $\mathcal C\subseteq V$ un cono convexo saliente ($\mathcal C\cap-\mathcal C=\{0\}$), $\Phi=\{\varphi_n\}_{n\in\mathbb N}\subseteq V^{\vee}$ una familia de funcionales ("el criterio"), $M:=\bigcap_n\ker\varphi_n$. Definimos el **defecto de separación** $\mathrm{sep}(\Phi,\mathcal C):=\dim\,\mathrm{span}(M\cap\mathcal C)$. Entonces:
(i) el criterio "$x\in\mathcal C,\ \varphi_n(x)=0\ \forall n\Rightarrow x=0$" vale ⟺ $\mathrm{sep}(\Phi,\mathcal C)=0$;
(ii) si $M\cap\mathcal C=\mathbb R_{\geq0}\,e$ con $e\neq0$ (defecto de separación 1), basta añadir UN funcional $\psi$ con $\psi(e)\neq0$: para todo $x\in\mathcal C$ con $\varphi_n(x)=0\ \forall n$ y $\psi(x)=0$ se concluye $x=0$. En efecto, $x\in M\cap\mathcal C=\mathbb R_{\geq0}e$ da $x=ce$ con $c\geq0$, y $0=\psi(x)=c\,\psi(e)\Rightarrow c=0$.

*Demostración.* (i) es una reescritura. (ii) está contenida en el enunciado. $\square$

**Observación 4.3 (el diccionario con Doc 118 — el teorema modelo de rigidez).** En Doc 118: $V$ = medidas signadas pares con momentos finitos, $\mathcal C$ = medidas positivas, $\varphi_n=\nu\mapsto\int\kappa_n\,d\nu$, y el cálculo central (Thm. 5.3, vía Carleman con los $a_n^\infty$ exactos) es exactamente "$M\cap\mathcal C=\mathbb R_{\geq0}\,m_\infty$": defecto de separación 1, eliminado por el funcional de Hardy ($\tilde g(\gamma_*)=0$). La lección estructural que la teoría adopta: **una rigidez útil no exige anulador trivial; exige anulador-en-el-cono de dimensión finita conocida, más un funcional externo por cada dimensión.** El papel de la positividad ($d\nu\geq0$, Doc 83) es ser la membresía en $\mathcal C$: sin cono no hay rigidez (los problemas de momentos no son rígidos para medidas signadas — Doc 118 Obs. 5.4). En 𝒫ol_δ, ese cono es el sustituto operativo de la polarización perdida.

---

## 5. [TEOREMA C] La dicotomía abstracta: defecto replicable ⟹ defecto infinito

Esta sección convierte la prueba de Rouché del Doc 112 (Teorema 2.3) en un teorema de la categoría. La estructura que el Doc 112 usa, destilada: (1) un cero off-crítico da un vector negativo *localizado en una ventana compacta de alturas*; (2) un casi-período $\tau$ transporta la ventana a altura $+\tau$ produciendo un vector negativo *nuevo*; (3) ventanas lejanas se correlacionan débilmente. Abstraemos (1)–(3) sin mencionar ζ.

**Definición 5.1 (vector replicable).** Sea $X=(H,Q,P)$ un objeto. Un vector $v\in P$ con $Q(v,v)=-c<0$ es **replicable** si existen:
- un subgrupo $\Gamma\subseteq\mathrm{Aut}(X)$ (automorfismos = $Q$-isometrías biyectivas que preservan $P$ y las decoraciones),
- un homomorfismo de **altura** $h:\Gamma\to(\mathbb R,+)$ con imagen **no acotada**,
- un módulo de **decaimiento de correlaciones** $\omega:[0,\infty)\to[0,\infty)$, no creciente, $\omega(t)\to0$ cuando $t\to\infty$,

tales que para todos $\gamma,\gamma'\in\Gamma$ con $h(\gamma)\neq h(\gamma')$:
$$\bigl|Q(\gamma v,\,\gamma' v)\bigr|\;\leq\;\omega\bigl(|h(\gamma)-h(\gamma')|\bigr).$$

(Interpretación: $h(\gamma)$ es el desplazamiento de la ventana; $\omega$ mide cuánto "se ven" dos réplicas a ventanas separadas. No se pide NADA sobre la acción de $\Gamma$ fuera de la órbita de $v$: la dicotomía es un fenómeno de UNA órbita.)

**Teorema C.1 (replicación ⟹ defecto infinito).** Si $X$ posee un vector negativo replicable en $P$, entonces $\delta(X)=\infty$.

*Demostración.* Fijo $n\in\mathbb N$; produzco un subespacio negativo de dimensión $n$ dentro de $P$. Como $\omega(t)\to0$, existe $T_n$ con $\omega(T_n)<\dfrac{c}{2n}$. Como $h(\Gamma)$ es un subgrupo no acotado de $\mathbb R$, existe $\gamma\in\Gamma$ con $|h(\gamma)|\geq T_n$; reemplazando $\gamma$ por $\gamma^{-1}$ si hace falta, $h(\gamma)\geq T_n$. Defino $v_j:=\gamma^j v\in P$, $j=1,\dots,n$ ($\gamma^j\in\Gamma$, $h(\gamma^j)=jh(\gamma)$). La matriz de Gram $A=(A_{jk})$, $A_{jk}:=Q(v_j,v_k)$, es hermitiana y satisface:
- $A_{jj}=Q(\gamma^jv,\gamma^jv)=Q(v,v)=-c$ ($\gamma^j$ es $Q$-isometría);
- para $j\neq k$: $|A_{jk}|\leq\omega(|j-k|\,h(\gamma))\leq\omega(h(\gamma))\leq\omega(T_n)<\dfrac{c}{2n}$ ($\omega$ no creciente).

Sumas de fila fuera de la diagonal: $\sum_{k\neq j}|A_{jk}|<(n-1)\dfrac{c}{2n}<\dfrac c2$. Por el teorema de los discos de Gershgorin aplicado a la matriz hermitiana $A$ (autovalores reales), todo autovalor está en $\bigcup_j\,[\,-c-\tfrac c2,\;-c+\tfrac c2\,]\subseteq(-\infty,-\tfrac c2]$: $A$ es definida negativa. En consecuencia: (a) los $v_j$ son linealmente independientes (si $\sum\xi_jv_j=0$ con $\xi\neq0$, entonces $0=Q(\sum\xi_jv_j,\sum\xi_kv_k)=\xi^{\!*}\!A\,\xi<0$, absurdo); (b) sobre $N_n:=\mathrm{span}\{v_1,\dots,v_n\}\subseteq P$, $Q(x,x)=\xi^*A\xi<0$ para $x\neq0$. Luego $\delta(X)\geq n$ para todo $n$. $\square$

**Corolario C.2 (dicotomía).** Sea $\mathcal R$ la clase de los objetos $X$ con la propiedad: *si $\delta(X)\geq1$, entonces algún vector negativo de $P$ es replicable* (Axioma R). Entonces para todo $X\in\mathcal R$:
$$\delta(X)\in\{0,\infty\}.$$
$\square$ (C.1 más la definición.)

**Teorema C.3 (versión aproximada: bastan réplicas imperfectas).** Sea $v\in P$, $Q(v,v)=-c<0$. Supóngase que para cada $n$ existen vectores $u_1,\dots,u_n\in P$ (no se exige que provengan de isometrías) con
$$\bigl|Q(u_j,u_k)-(-c)\,\delta_{jk}\bigr|\;\leq\;\frac{c}{2n}\qquad(1\leq j,k\leq n).$$
Entonces $\delta(X)=\infty$.

*Demostración.* La matriz de Gram es $-cI+E$ con $\|E\|_{\text{filas}}<\tfrac c2+\tfrac{c}{2n}\cdot$… precisemos: $|E_{jk}|\leq\tfrac{c}{2n}$ para todo $j,k$ (incluida la diagonal), luego cada suma de fila de $|E|$ es $\leq n\cdot\tfrac{c}{2n}=\tfrac c2$; Gershgorin da autovalores $\leq-c+\tfrac c2<0$. Se concluye como en C.1. $\square$

**Observación 5.2 (qué cuantificador pide C.3 — honestidad estructural).** C.3 pide, para cada $n$, $n$ réplicas con error $O(c/n)$ en los productos cruzados. Es un enunciado $\Pi_2$ sobre la familia de réplicas — exactamente la forma de LP-112 (una sucesión $\tau_k$ con calidad creciente). La teoría NO esquiva el cuantificador maestro de P43; lo que hace es (i) reducirlo a datos de UNA órbita (ninguna uniformidad sobre configuraciones: comparar con Doc 112 §2.6, "la finitud protege a los argumentos internos"), y (ii) separar las tres hipótesis de la Def. 5.1, que tienen estatus MUY distinto sobre el objeto-ζ (§8.3).

### 5.4. Chequeos de modelo (obligatorios)

**(M1) El Doc 112 es la instancia.** Diccionario: $v$ = el vector negativo asociado al cuádruplo off-crítico hipotético (vía P35, el autovector-par en $\mathcal K_{\mathrm{off}}$; en la coordenada analítica de D112, el cero $\rho_0$ visto en su ventana $D(\rho_0,r)$); $\Gamma$ = el grupo (deseado) de casi-períodos puntuales actuando por traslación vertical $s\mapsto s+i\tau$; $h(\gamma)=\tau$; la no-acotación de $h(\Gamma)$ = "sucesión $\tau_k\to\infty$"; el decaimiento $\omega$ = decaimiento de la correlación de la forma de Weil entre ventanas espectrales separadas (en el modelo CCM, el núcleo $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98/95, decae sobradamente). El Teorema 2.3 de D112 ("LP-112 ⟹ m∈{0,∞}") es C.2 leído a través de ese diccionario: LP-112 es la forma analítica del Axioma R para el objeto-ζ. La ganancia de la abstracción: C.1 muestra que el mecanismo NO usa Rouché, ni holomorfía, ni nada de ζ — usa isometría + alturas no acotadas + decaimiento. Rouché era, en D112, el *certificado* de que el casi-período produce una réplica genuina; en la categoría, ese certificado es el axioma de isometría.

**(M2) Los anti-modelos cosh fallan donde deben.** Los objetos (I5) tienen $\delta=2m$ finito no nulo; por C.2 NO pueden estar en $\mathcal R$. Verificación independiente: el Lema 3.2 del Doc 112 prueba que la clase cosh no admite NINGUNA sucesión de auto-aproximación ($|F(s+i\tau)|\to\infty$ en el disco): el grupo de simetrías de altura no acotada requerido por la Def. 5.1 no existe para ellos — su $\Gamma$ disponible es trivial (o de altura acotada). La teoría predice correctamente en qué clase viven los contraejemplos de defecto finito: **en la clase sin simetrías de altura no acotada.** Y la periodicidad exacta de $\cosh$ no ayuda: sus traslaciones de período no preservan el factor polinómico $P_1\cdots P_m$ (no son automorfismos del objeto completo), reflejo abstracto del hecho de D112 §3.2 (un grupo discreto de períodos exactos mapea los ceros sobre sí mismos y no multiplica nada — en nuestra versión: si las réplicas no son *nuevas*, la matriz de Gram no es la de C.1; la novedad la garantiza $h(\gamma)\neq0$ junto con el decaimiento, que fuerza $Q(v,\gamma v)\approx0\neq-c$, i.e. $\gamma v\not\sim v$).

**(M3) Consistencia con Davenport–Heilbronn.** DH (sin Euler, con ecuación funcional) realizó $m=\infty$ [DH36, vía D112 §3.3]: consistente con que DH posea la casi-periodicidad de su serie de Dirichlet (las hipótesis de C.1 plausiblemente se cumplen para su objeto, y la conclusión $\delta=\infty$ es la observada). Ningún miembro conocido de la clase "serie de Dirichlet + ecuación funcional" tiene $\delta$ finito no nulo — el patrón $\delta\in\{0,\infty\}$ no tiene contraejemplo en esa clase (GAP de D111 Obs. 2.4, sigue abierto, ahora con enunciado categórico).

---

## 6. [TEOREMA D] Paridad y clasificación en defecto bajo

Objetos espectrales: $X=(H,Q,P)$ con generador $A$ ($Q$-simétrico: $Q(Ax,y)=Q(x,Ay)$), donde $P$ es suma (algebraica) de subespacios radicales $H[z]:=\bigcup_m\ker(A-z)^m$ de dimensión finita, con autovalores $z$ tales que $z^2\notin\mathbb R$ (equivalente: $z\notin\mathbb R\cup i\mathbb R$), y $Q|_P$ no degenerada.

**Lema D.1 (ortogonalidad radical).** Si $u\in\ker(A-z)^p$, $v\in\ker(A-w)^q$ y $w\neq\bar z$, entonces $Q(u,v)=0$.

*Demostración.* Inducción sobre $p+q$. Si $p+q=2$ ($u,v$ autovectores): $zQ(u,v)=Q(Au,v)=Q(u,Av)=\overline{w}\,Q(u,v)$ (sesquilinealidad en la segunda variable: $Q(u,wv)=\bar wQ(u,v)$), y $z\neq\bar w$ fuerza $Q(u,v)=0$. Paso: sean $u':=(A-z)u\in\ker(A-z)^{p-1}$, $v':=(A-w)v\in\ker(A-w)^{q-1}$. Entonces
$$Q(u',v)+zQ(u,v)=Q(Au,v)=Q(u,Av)=Q(u,v')+\bar wQ(u,v),$$
es decir $(z-\bar w)Q(u,v)=Q(u,v')-Q(u',v)=0-0$ por hipótesis inductiva (ambos pares tienen suma de exponentes $p+q-1$). Como $z\neq\bar w$, $Q(u,v)=0$. $\square$

**Lema D.2 (isotropía y apareamiento hiperbólico).** Para $z$ no real: $H[z]$ es totalmente isótropo; si además $Q$ es no degenerada sobre $H[z]\oplus H[\bar z]$ (lo es, por D.1 y la no-degeneración global sobre $P$), entonces $\dim H[z]=\dim H[\bar z]=:d_z$ y
$$\mathrm{sig}\bigl(Q|_{H[z]\oplus H[\bar z]}\bigr)=(d_z,\,d_z).$$

*Demostración.* Isotropía: D.1 con $w=z$ (y $z\neq\bar z$). Apareamiento: como $H[z]$ es isótropo y $Q$ no degenerada en la suma, el mapa $H[\bar z]\to H[z]^*$, $v\mapsto Q(\cdot,v)|_{H[z]}$, es inyectivo (un $v$ en su núcleo sería $Q$-ortogonal a $H[z]$, a $H[\bar z]$ por isotropía, y a todo lo demás por D.1: $v=0$), y simétricamente: $\dim H[z]=\dim H[\bar z]$. Eligiendo bases duales, la matriz de Gram en $H[z]\oplus H[\bar z]$ es $\begin{pmatrix}0&B\\B^*&0\end{pmatrix}$ con $B\in GL_{d_z}$. Por descomposición en valores singulares $B=U\Sigma V^*$ ($\Sigma>0$ diagonal), la matriz es unitariamente congruente a $\begin{pmatrix}0&\Sigma\\\Sigma&0\end{pmatrix}$, suma directa de bloques $\begin{pmatrix}0&\sigma_i\\\sigma_i&0\end{pmatrix}$ de autovalores $\pm\sigma_i$: signatura $(d_z,d_z)$. $\square$

**Teorema D.3 (estructura y valor exacto del defecto espectral).** Para $X$ espectral como arriba:
$$\delta(X)\;=\;\sum_{\substack{\text{pares }\{z,\bar z\}\subseteq\mathrm{spec}(A|_P)\\ \mathrm{Im}\,z>0}} d_z.$$

*Demostración.* Por D.1, $P=\bigoplus_{\{z,\bar z\}}\bigl(H[z]\oplus H[\bar z]\bigr)$ es una descomposición $Q$-ortogonal; por aditividad (Teorema A.1(ii)) y D.2, $\delta(X)=\sum d_z$. $\square$

**Teorema D.4 (paridad: la simetría funcional fuerza defecto par).** Si $X$ posee además una simetría funcional $S$ ($S^2=\mathrm{id}$, $SAS^{-1}=-A$, $Q(Sx,Sy)=\epsilon_SQ(x,y)$, $SP=P$), entonces para cada $z$: $S\,H[z]=H[-z]$, los pares $\{z,\bar z\}$ y $\{-z,-\bar z\}$ son disjuntos (pues $z^2\notin\mathbb R$ ⟹ $\bar z\neq-z$ y $z\neq-z$), $d_z=d_{-z}$, y por tanto el espectro primitivo se organiza en **cuádruplos** $\{z,\bar z,-z,-\bar z\}$ con
$$\delta(X)\;=\;2\sum_{\substack{\text{cuádruplos}\\ \mathrm{Im}\,z>0,\ \mathrm{Re}\,z>0}}d_z\;\in\;2\mathbb N\cup\{\infty\}.$$
**En particular $\delta(X)=1$ es imposible**, y el defecto reducido $\hat\delta=\delta/2$ es un entero: el número de cuádruplos contados con multiplicidad.

*Demostración.* $A(Sx)=-SAx=-zSx$ para $x\in\ker(A-z)$, e inductivamente $S\ker(A-z)^m=\ker(A+z)^m$: $SH[z]=H[-z]$, biyectivo ($S^2=1$), luego $d_z=d_{-z}$. Que los cuatro números $z,\bar z,-z,-\bar z$ son distintos: $z\neq\bar z$ ($z\notin\mathbb R$), $z\neq-z$ ($z\neq0$), $z\neq-\bar z$ ($z\notin i\mathbb R$). D.3 suma $d_z$ sobre pares conjugados; los dos pares de cada cuádruplo aportan $d_z+d_{-z}=2d_z$. $\square$

**Teorema D.5 (clasificación en defecto 1, sin simetría funcional).** Los objetos espectrales con $\delta(X)=1$ son, salvo isomorfismo de 𝒫ol_δ, exactamente los
$$\Pi_1(z):\qquad H=P=\mathbb Cu\oplus\mathbb C\bar u,\quad A=\mathrm{diag}(z,\bar z),\quad
Q=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad z\in\mathbb C,\ z^2\notin\mathbb R,\ \mathrm{Im}\,z>0,$$
y $\Pi_1(z)\cong\Pi_1(z')$ ⟺ $z=z'$. Es decir: el defecto mínimo tiene forma normal rígida — un solo plano hiperbólico con un solo par espectral simple.

*Demostración.* Por D.3, $\delta=1$ fuerza un único par $\{z,\bar z\}$ con $d_z=1$ y ningún otro espectro primitivo. $H[z]=\mathbb Cu_0$, $H[\bar z]=\mathbb Cv_0$, $Q(u_0,u_0)=Q(v_0,v_0)=0$, $b:=Q(u_0,v_0)\neq0$. Además $A$ es semisimple sobre cada uno (dimensión 1). Reescalando $v_0\mapsto v_0/\bar b$ se logra $Q(u_0,v_0)=1$ sin tocar $A$. Cualquier isomorfismo debe preservar $\mathrm{spec}(A|_P)=\{z,\bar z\}$ con $\mathrm{Im}\,z>0$ fijando la etiqueta: $z$ es invariante. Recíprocamente, los $\Pi_1(z)$ realizan $\delta=1$ (D.2). $\square$

**Observación 6.1 (lectura para el programa).** D.4 responde "¿qué simetría prohíbe $\delta=1$?": **la anti-conmutación con el generador** — la sombra abstracta de la ecuación funcional $s\mapsto1-s$. El $\kappa=2m$ de P35 deja de ser un cómputo del modelo y pasa a ser un teorema de la categoría: *todo* objeto espectral con simetría funcional tiene defecto par. Combinado con C.2: en la clase $\mathcal R\cap\{\text{espectrales con }S\}$, $\delta\in\{0,\infty\}$, y fuera de $\mathcal R$, $\delta\in2\mathbb N\cup\{\infty\}$ — los anti-modelos cosh ocupan exactamente el estrato $2\mathbb N\setminus\{0\}$ permitido por D.4 y prohibido por el Axioma R. La estratificación es coherente con TODO lo conocido del corpus.

---

## 7. [TEOREMA E] El dividendo: densidad de defecto, el flujo tensorial y el ideal hiperbólico

Dimensión finita, formas no degeneradas; notación de §3.

**Definición 7.1 (densidad de defecto).** $\theta(X):=\delta(X)/d(X)\in[0,1]$. El **sesgo** es $\beta(X):=1-2\theta(X)=\sigma(X)/d(X)\in[-1,1]$.

**Teorema E.1 (composición de canal binario).** $\beta(X_1\otimes X_2)=\beta(X_1)\,\beta(X_2)$; equivalentemente
$$\theta(X_1\otimes X_2)=\theta_1+\theta_2-2\theta_1\theta_2,$$
la ley de composición del ruido de un canal binario simétrico (la probabilidad de "paridad impar" de dos ruidos independientes). En particular $\theta(X^{\otimes k})=\tfrac12\bigl(1-\beta(X)^k\bigr)$.

*Demostración.* $\beta=\sigma/d$ y ambos, $\sigma$ y $d$, son multiplicativos (Cor. A.3(ii)). La identidad $\theta_\otimes=\theta_1+\theta_2-2\theta_1\theta_2$ es la reescritura de $1-2\theta_\otimes=(1-2\theta_1)(1-2\theta_2)$. $\square$

(Probabilísticamente: asignar a $X$ la variable $\pm1$ que vale $-1$ con probabilidad $\theta$ — el "signo de una dirección aleatoria"; el tensor multiplica signos independientes, y $\beta$ es la esperanza. El defecto se compone como el XOR de bits ruidosos. Esta lectura no es decorativa: es la fuente de E.2–E.4.)

**Teorema E.2 (clasificación de las clases ⊗-estables).** Las únicas densidades de defecto invariantes bajo $X\mapsto X\otimes Y$ dentro de su clase son:
(i) $\theta=0$ (objetos **polarizados**): subcategoría tensorial ($\beta=1$ es el elemento neutro del producto de sesgos);
(ii) $\theta=\tfrac12$ (objetos **hiperbólicos**, $\sigma=0$): **ideal absorbente** — si $\theta(X)=\tfrac12$ entonces $\theta(X\otimes Y)=\tfrac12$ para TODO $Y$.
La clase $\theta=1$ (negativos definidos) NO es estable: $\theta(X^{\otimes2})=0$. Y para todo $X$ con $0<\theta(X)<1$:
$$\Bigl|\theta(X^{\otimes k})-\tfrac12\Bigr|=\tfrac12\,|\beta(X)|^{k}\;\longrightarrow\;0\quad\text{exponencialmente.}$$
*Todo defecto estricto fluye al ideal hiperbólico; la tasa es exacta.*

*Demostración.* Todo es inmediato de E.1: $\beta=0$ absorbe; $|\beta|<1$ ⟹ $\beta^k\to0$; $\beta=-1$ ($\theta=1$) alterna $\pm1$. La identificación "$\sigma=0$ ⟺ hiperbólico" es la descomposición de Witt para formas hermitianas complejas: la parte anisótropa de una forma hermitiana compleja es definida (toda forma no definida en dim ≥ 2 tiene vector isótropo: si $Q(u,u)>0>Q(w,w)$, el segmento $t\mapsto Q(u+tw,u+tw)$ con $t$ real cruza 0), y una parte definida no nula da $\sigma\neq0$; luego $\sigma=0$ ⟹ anisótropo nulo ⟹ suma ortogonal de planos hiperbólicos. $\square$

**Corolario E.3 (la esterilidad de Doc 106, explicada desde dentro).** La Prop. 3.6 de Doc 106 (ningún esquema de amplificación tensorial con cota subaditiva puede coexistir con $\delta\geq1$) es el caso cuantitativo de E.2: el flujo tensorial no SEPARA el defecto — lo TERMALIZA. Amplificar con $\otimes$ empuja todo objeto defectuoso hacia $\theta=\tfrac12$, el estado de máxima entropía de signos, donde el defecto es la mitad de la dimensión y no distingue nada. La razón profunda de que "los dos lados se calculan con los mismos datos" (Obs. 3.7 de Doc 106): tras pasar al anillo de Grothendieck, los únicos datos multiplicativos son $d$ y $\sigma$ (Prop. A.4), y la dicotomía RH-relevante vive en $\delta$, que no es carácter. **Ningún invariante multiplicativo verá jamás el defecto del objeto-ζ** (§8.2 lo agrava). $\square$

**Teorema E.4 (rigidez del cono polarizado bajo el flujo tensorial).** (i) $\theta=0$ es el único punto fijo atractor-libre: si $\theta(X)=0$, toda potencia y todo producto con polarizados queda en $\theta=0$, y además $\delta(X\otimes Y)=d(X)\,\delta(Y)$ crece *linealmente en el defecto del cofactor* — el polarizado es transparente. (ii) Detección al primer paso: $\delta(X\otimes\bar X)=2p\delta\geq2\delta$, y $\delta(X\otimes\bar X)=0\iff\delta(X)=0$ o $p(X)=0$: el cuadrado hermitiano detecta el defecto si y solo si hay al menos una dirección positiva. (iii) Pero la detección de (ii) es de nuevo $\delta$, no un carácter: no hay función multiplicativa que la implemente (A.4) — la detección requiere *leer una signatura*, i.e. la inercia de P43.

*Demostración.* (i) y (ii) son A.2 con $(p_2,\delta_2)=(p,\delta)$ del conjugado (A.6: misma signatura): $\delta(X\otimes\bar X)=p\delta+\delta p=2p\delta$. (iii) es A.4. $\square$

**Observación 7.2 (estatus de novedad — honestidad).** Los ingredientes de §7 son clásicos (Sylvester, Witt, multiplicatividad de la signatura). La síntesis — densidad de defecto como sesgo de canal binario, la clasificación E.2 de clases ⊗-estables con el ideal hiperbólico absorbente como explicación estructural de la esterilidad de los amplificadores tensoriales, y la estratificación D.4 + C.2 del defecto — no la conozco escrita en la literatura de espacios de Kreĭn en esta forma. Es el tipo de enunciado que un experto reconocería como "folklore organizado más dos teoremas chicos nuevos" (C.1 y D.4/D.5 en esta generalidad). El reclamo de novedad fuerte queda para C.1: *"un espacio de Kreĭn con un vector negativo replicable — órbita de isometrías con alturas no acotadas y correlaciones decrecientes — tiene índice negativo infinito"* es, hasta donde el corpus y mi conocimiento alcanzan, un enunciado no escrito antes, elemental pero con contenido (la dicotomía de Pontryagin sin Pontryagin). **[Declarado: no se hizo búsqueda bibliográfica externa esta sesión; el reclamo es "no escrita en el corpus ni conocida por mí", no "probadamente inexistente".]**

---

## 8. [PUENTE] El objeto-ζ en 𝒫ol_δ, y qué muerde cada teorema

### 8.1. El diccionario y el enunciado

$$Z_\zeta=(\mathcal K,\,Q,\,P_{\mathrm{off}};\;A=H_C,\;S,\;\tau)\in\mathcal Pol_\delta,\qquad
\boxed{\;\mathrm{RH}\iff\delta(Z_\zeta)=0.\;}$$

Estatus de cada eslabón, sin maquillaje:
- La forma $Q$ (Weil) y su $\kappa(Q)=2m$: **teorema del corpus** (P35 y antecedentes) en el sentido $\kappa(Q)=2m$ sobre el modelo de cuádruplos; la identificación con $\mathrm{neg.ind}$ del operador $H_C$ en el Pontryagin es la **conjetura puente P35** (programa V.1–V.4). El enunciado "RH ⟺ δ=0" vale ya al nivel de la forma de Weil sin pasar por el puente: $\delta=\kappa=2m$ y $m=0$ ⟺ RH. **Este eslabón es sólido.**
- $A=H_C$ $Q$-simétrico, $S$ de la ecuación funcional con $SAS^{-1}=-A$: estructura del modelo de Phase 26; la paridad $\delta=2m$ es ahora el **Teorema D.4** aplicado (antes: cómputo; ahora: instancia de teorema de la categoría).
- $P_{\mathrm{off}}$ = parte espectral con $z^2\notin\mathbb R$: bien definida en el modelo (descomposición espectral del Doc 96 vía Doc 106 §3.2/R2).

### 8.2. Qué teoremas muerden sobre $Z_\zeta$ — y el hallazgo Witt

**(a) Teorema D muerde ya:** $\delta(Z_\zeta)$ es par; $\hat\delta=m$; los objetos $\delta=1$ están prohibidos por la sola simetría funcional. (Contenido nuevo: cualquier intento de construir "medio cuádruplo" como obstáculo intermedio es categóricamente vacío.)

**(b) El hallazgo estructural (Teoremas A/E sobre la parte off):** la signatura de $Q|_{\mathcal K_{\mathrm{off}}}$ es $(2m,2m)$ (Doc 106 §3.2: suma de planos hiperbólicos — re-derivado aquí como D.2+D.4). Por tanto
$$\sigma(\mathcal K_{\mathrm{off}})=0,\qquad\theta(\mathcal K_{\mathrm{off}})=\tfrac12:$$
**la parte defectuosa del objeto-ζ es Witt-trivial y vive exactamente en el ideal absorbente de E.2.** Consecuencias probadas: todo invariante aditivo-multiplicativo le asigna lo mismo que al objeto nulo de su dimensión (A.4); todo flujo tensorial la deja en el ideal (E.2); su defecto es invisible para caracteres y solo legible como *inercia* (E.4(iii)). Esto es la explicación interna, con teorema, de POR QUÉ fracasaron: el amplificador tensorial (Doc 104/106), toda "función multiplicativa detectora", y todo intento de leer $m$ en un valor promediado — el muro valor/inercia de P43 es, en 𝒫ol_δ, el enunciado "δ no es carácter" (A.4). No es una analogía: es el mismo hecho en coordenadas algebraicas.

**(c) Teorema B muerde en la arquitectura:** la identidad D-109 del programa, RH = (m<∞) ∧ (m∈{0,∞}), se reescribe como la conjunción de los dos ejes de la teoría:
$$\mathrm{RH}\;=\;\underbrace{\bigl[\;\delta(Z_\zeta)<\infty\;\bigr]}_{\text{eje Fredholm (B.4): positividad esencial}}\;\wedge\;\underbrace{\bigl[\;\delta(Z_\zeta)\in\{0,\infty\}\;\bigr]}_{\text{eje simetría (C.2): replicabilidad}}.$$
B.4 da la forma exacta del objetivo L8: **basta probar que el Gram de la forma de Weil es esencialmente positivo** (positivo módulo compactos, con gap esencial) para obtener $m<\infty$. Estatus: NO probado para $Z_\zeta$; pero el enunciado es nuevo en esta forma y es estrictamente más débil que la positividad ($\delta=0$): es "polarización módulo compactos". [DESEO 8.D1 abajo.] Y B.3 acota el comportamiento bajo deformaciones: en cualquier familia tipo De Bruijn–Newman $\{Q_t\}$ norm-continua, $\delta(t)$ solo salta en cruces de núcleo — la caracterización $\Lambda=\inf\{t:T_\lambda(t)=0\}$ del Doc 70 es un candidato a "primer cruce de núcleo del flujo"; **estatus: analogía, no identificación probada** (la topología del flujo DBN sobre el Gram no está verificada como norm-continua). [PUENTE-parcial.]

**(d) Teorema C muerde condicionalmente — y aquí la honestidad total (la pregunta del encargo).** Aplicar C.2 a $Z_\zeta$ requiere el Axioma R: *todo vector negativo de $P_{\mathrm{off}}$ es replicable*. Desglose de las tres hipótesis de la Def. 5.1 sobre $Z_\zeta$, en la coordenada analítica donde las réplicas son traslaciones verticales (el diccionario M1):

| hipótesis abstracta | forma analítica sobre ζ | estatus |
|---|---|---|
| $h(\Gamma)$ no acotado | casi-períodos de alturas $\tau\to\infty$ con densidad relativa | **TEOREMA** al nivel B² (D112 Lemas 2.1–2.2, incondicional, vía independencia ℚ-lineal de $\{\log p\}$) |
| decaimiento $\omega$ de correlaciones entre réplicas a ventanas separadas | decaimiento del apareamiento de Weil entre ventanas espectrales lejanas; en el modelo CCM, $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$ | **plausible y parcialmente establecido en el modelo** (Doc 98/95); NO verificado como enunciado sobre el objeto $Z_\zeta$ exacto — [GAP-132.ω, declarado] |
| $\gamma$ actúa por **$Q$-isometría** sobre la órbita de $v$ (o réplicas $\varepsilon$-isométricas, C.3) | $\sup_D|\zeta(s+i\tau_k)-\zeta(s)|\to0$: la traslación es auto-aproximación PUNTUAL en la ventana del cero | **ABIERTO = LP-112.** |

**Respuesta directa a la pregunta del encargo:** la hipótesis que queda al aplicar la dicotomía abstracta al objeto-ζ **es la vieja LP-112 disfrazada — sí, es ella, y declararlo es obligatorio.** La teoría del defecto no fabrica el casi-período puntual; nada elemental podría, porque la Prop. 2.6 de D112 prueba que sus testigos son de densidad cero bajo ¬RH y el cuantificador maestro de P43 bloquea la selección no-genérica. Lo que la teoría SÍ agrega, y no estaba: (i) la dicotomía necesita solo datos de UNA órbita y de UN vector (C.1/C.3), con constantes internas al mundo — confirma y abstrae el hallazgo de D112 §2.6 de que la finitud congela las constantes; (ii) separa LP-112 (el axioma de isometría) de las otras dos hipótesis, que tienen estatus mejor (una es teorema, la otra es [GAP-132.ω] del modelo, atacable sin tocar ζ-puntual); (iii) muestra que el papel de Rouché era solo certificar la isometría aproximada — cualquier OTRO certificado de $\varepsilon$-isometría sobre la órbita (no necesariamente analítico-complejo) alimentaría C.3 igual. El espacio de ataques a LP-112 es más ancho que el de ataques vía Rouché. Eso es un re-encuadre genuino, no una solución.

### 8.3. La reformulación categórica del ENUNCIADO-MÍNIMO-130

El Doc 130 §5.3 pide: una construcción foliada sobre Spec ℤ cuya buena definición no presuponga la localización de los ceros, tal que bajo ¬RH el espacio exista con la polarización fallando visiblemente. En el lenguaje de 𝒫ol_δ:

> **ENUNCIADO-MÍNIMO-130, forma categórica.** La ruta de Deninger es no-circular si y solo si su construcción define un funtor $\mathfrak D:\{\text{mundos aritméticos}\}\to\mathcal Pol_\delta$ con **dominio total** — el objeto $\mathfrak D(\text{mundo})$ existe y su $\delta$ está definido en TODO mundo — y RH es el enunciado $\delta(\mathfrak D)=0$. La circularidad diagnosticada por el Doc 130 es exactamente: la construcción Kähler–Riemann solo define el objeto **dentro de la fibra $\delta=0$** (la métrica usa Hasse; sin el análogo, ni la medida es invariante ni la traza converge). Un funtor definido solo donde su invariante se anula no enuncia nada.

La categoría 𝒫ol_δ es el codominio que falta para que NC4 sea siquiera formulable. Y la instancia (I3) (Babaee–Huh) prueba que el codominio no es vacío en su estrato defectuoso: hay geometrías honestas (tropicales) cuyo objeto tiene $\delta\geq1$ visible. El [DESEO] correspondiente queda nombrado abajo.

### 8.4. Tabla de mordida

| Teorema | ¿muerde sobre $Z_\zeta$? | qué da | qué falta |
|---|---|---|---|
| A (aritmética) | sí, incondicional | $\delta$ monótono/aditivo; Whitney; $\delta$ no es carácter | — |
| E (ideal hiperbólico) | sí, incondicional | $\mathcal K_{\mathrm{off}}$ es Witt-trivial, $\theta=\frac12$: invisible a todo invariante multiplicativo — cierre estructural de la ruta amplificador | — |
| D (paridad) | sí, incondicional sobre el modelo | $\delta=2m$ par; $\delta=1$ prohibido; $\hat\delta=m$ teorema | puente P35 para la versión operatorial |
| B.4 (Fredholm) | enunciado nuevo del objetivo | $m<\infty$ ⟸ positividad esencial del Gram de Weil | probar la positividad esencial [DESEO 8.D1] |
| B.1–B.3 (rigidez) | parcial | saltos de $\delta$ solo en cruces de núcleo; marco para DBN | continuidad del flujo DBN sobre el Gram [no verificada] |
| C (dicotomía) | condicional | $\delta\in\{0,\infty\}$ bajo Axioma R; 2 de 3 hipótesis con estatus mejor que LP-112 | el axioma de isometría = **LP-112** (declarado) + [GAP-132.ω] |
| B.6 (rigidez de cono) | sí, como lente | Doc 118 = defecto de separación 1 + funcional de Hardy | — |

---

## 9. [DESEO] Los deseos, sin vergüenza

**[DESEO 8.D1 — positividad esencial.]** Probar que el operador de Gram de la forma de Weil (en una realización de tipo Hilbert del dominio de tests, p.ej. la CCM) es **esencialmente positivo**: $\mathrm{spec}_{\mathrm{ess}}\subseteq(0,\infty)$. Por B.4 esto daría $m<\infty$ — la diana L8 — y es estrictamente más débil que toda positividad perseguida antes: permite CUALQUIER cantidad finita de direcciones negativas y cualquier perturbación compacta. Es "RH módulo compactos". Ninguna refutación del corpus (W_λ≥0 caída, etc.) toca este enunciado: las positividades refutadas eran puntuales/de kernel, no esenciales-espectrales.

**[DESEO 8.D2 — el funtor total.]** Construir $\mathfrak D$ con dominio total (§8.3) aunque sea para un sustituto de Spec ℤ (el $\mathfrak X_F$ de Morishita, vía Doc 128/130): un objeto foliado de 𝒫ol_δ cuya existencia no use la localización. El test de éxito es frío: computar $\delta$ del objeto en un mundo de juguete ¬RH (un Davenport–Heilbronn foliado) y verlo positivo.

**[DESEO 8.D3 — el certificado no-Rouché.]** Un certificado de $\varepsilon$-isometría sobre la órbita de un vector negativo (C.3) que no pase por la auto-aproximación uniforme en discos: p.ej. isometría aproximada solo sobre el plano hiperbólico del cuádruplo (4 dimensiones, no un disco entero de funciones). LP-112 pide $\sup_D$ sobre un disco; C.3 pide $n^2$ números. La brecha entre ambos es deseo legítimo de Phase 45.

**[DESEO 8.D4 — teoría espectral en el ideal.]** Una teoría de "índice relativo en el ideal hiperbólico": ya que $\mathcal K_{\mathrm{off}}$ es Witt-trivial, el invariante fino debe ser relativo a una referencia (el par $(Q,Q_{\mathrm{ref}})$, tipo flujo espectral / índice de pares de Fredholm). El defecto como **flujo espectral** de una familia que interpola la forma de Weil con su versión on-line: $\delta=\mathrm{sf}(Q_t)$. B.3 es el primer paso (saltos solo en cruces); falta la teoría del cruce.

---

## 10. El mapa final

**PROBADO en este documento (incondicional, prueba completa):**
1. **Lema A.0** (descomposición de índice finito) y **Teorema A.1** (monotonía; aditividad de $\delta$ bajo $\oplus$ sin hipótesis de dimensión).
2. **Teorema A.2 / Corolario A.3** (Whitney del defecto $\delta_\otimes=p_1\delta_2+\delta_1p_2$, inclusión-exclusión, superaditividad, potencias, estabilidad de la polarización) — A.2 re-prueba Doc 106 Prop. 3.1 dentro de la categoría.
3. **Proposición A.4** (los únicos caracteres son $d$ y $\sigma$; $\delta=(d-\sigma)/2$ no es carácter) y **A.5/A.6** (Fredholm en dimensión infinita; dual y conjugado).
4. **Teoremas B.1–B.4** (rigidez: constancia local de Riesz; $|\Delta\delta|\leq\mathrm{rang}$; semicontinuidad y saltos solo en cruces de núcleo; positividad esencial ⟹ defecto finito, estable bajo compactos — Weyl citado con precisión) y **B.6** (rigidez de cono; Doc 118 como instancia con defecto de separación 1).
5. **Teorema C.1** (vector negativo replicable ⟹ $\delta=\infty$; Gershgorin sobre la matriz de Gram de la órbita), **Corolario C.2** (dicotomía $\delta\in\{0,\infty\}$ bajo el Axioma R), **Teorema C.3** (versión con réplicas aproximadas) — la abstracción exacta del mecanismo del Doc 112, con chequeos de modelo M1–M3 (el Doc 112 es instancia; los cosh fallan la hipótesis correcta; DH consistente).
6. **Lemas D.1–D.2 y Teoremas D.3–D.5** (ortogonalidad radical; apareamiento hiperbólico $(d,d)$; valor exacto del defecto espectral; PARIDAD bajo simetría funcional — $\delta=1$ prohibido; clasificación $\Pi_1(z)$ del defecto mínimo).
7. **Teoremas E.1–E.4** (densidad de defecto como sesgo de canal binario; clasificación de clases ⊗-estables: polarizados = subcategoría, hiperbólicos = ideal absorbente; termalización exponencial exacta; esterilidad de Doc 106 explicada; el cuadrado hermitiano detecta pero solo como inercia).

**PUENTE (estatus declarado):** $Z_\zeta\in\mathcal Pol_\delta$ con RH ⟺ $\delta(Z_\zeta)=0$ (sólido al nivel de la forma de Weil; operatorial = conjetura P35). Muerden incondicionalmente: D (paridad, $\hat\delta=m$), E (**hallazgo: $\mathcal K_{\mathrm{off}}$ es Witt-trivial, $\theta=\tfrac12$, en el ideal absorbente** — cierre con teorema de toda ruta multiplicativa/amplificadora), A.4 (el muro valor/inercia de P43 = "δ no es carácter"). Muerden condicionalmente: B.4 (reformula L8 como positividad esencial — enunciado nuevo, más débil que toda positividad previa), C (dicotomía bajo Axioma R: **la hipótesis restante sobre ζ es LP-112 disfrazada**, declarado sin atenuantes; las otras dos hipótesis tienen estatus teorema / gap-de-modelo). ENUNCIADO-MÍNIMO-130 reformulado: no-circularidad de Deninger = funtor con dominio total en 𝒫ol_δ; Babaee–Huh puebla el estrato defectuoso.

**DESEO:** 8.D1 (positividad esencial del Gram de Weil ⟹ L8), 8.D2 (el funtor total, test en mundo de juguete ¬RH), 8.D3 (certificado de $\varepsilon$-isometría no-Rouché para C.3), 8.D4 (defecto como flujo espectral relativo en el ideal hiperbólico).

**SIGUIENTE TEOREMA (el más atacable, en orden):**
1. **[GAP-132.ω]** el decaimiento de correlaciones de la Def. 5.1 para $Z_\zeta$ en el modelo CCM ($\omega$ desde $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98/95): es un enunciado del modelo, sin cuantificador maestro, y dejaría a la dicotomía colgando de UN solo axioma (la isometría).
2. **8.D1 en versión de juguete:** positividad esencial del Gram de Weil para Davenport–Heilbronn y para la clase cosh (donde la respuesta se conoce por otra vía: calibración).
3. **B.3→DBN:** verificar la norm-continuidad del flujo De Bruijn–Newman sobre el Gram en la realización CCM, para convertir "Λ = primer cruce de núcleo" de analogía en teorema.

---

## Referencias

**Internas (backward-only):** Doc 130 (circularidad de la métrica Kähler–Riemann; ENUNCIADO-MÍNIMO-130); Doc 129/128/127 (contexto foliado); Doc 125 (forma de intersección del cuadrado; juguete $(1,2)$; Babaee–Huh [arXiv:1502.00299, vía Doc 125 §5.5]); Doc 119 (test R-NC); Doc 118 (rigidez de momentos: Carleman + cono; Teorema 5.3); Doc 117; Doc 114 (refutación $W_\lambda\geq0$); Doc 112 (LP-112; Teorema 2.3; Prop. 2.6 densidad cero; Lemas 2.1–2.2, 3.1–3.3); Doc 111 (clase cosh; Cor. 2.3); Doc 109 (identidad D-109); Doc 106 §3 (Props. 3.1, 3.3, 3.4, 3.6; Obs. 3.7); Doc 105; Doc 104; Doc 98 (costo $2\delta^2K_\lambda(\gamma)$); Doc 96 (descomposición espectral de $\mathcal K_{\mathrm{off}}$); Doc 95 (decaimiento de $dm_\infty$); Doc 89; Doc 83 ($d\nu\geq0$); P43 (cuantificador maestro; valor/inercia); P35 (conjetura puente $\kappa=\mathrm{neg.ind}(H_C)=2m$; programa V.1–V.4).

**Literatura (clásica, verificable):**
- T. Kato, *Perturbation Theory for Linear Operators*, Springer, 2.ª ed. 1976. (Thm. IV.5.35: invariancia del espectro esencial bajo perturbación compacta — usado en B.4; proyecciones de Riesz y continuidad — usado en B.1.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics IV*, Academic Press, 1978, §XIII.4. (Teorema de Weyl; alternativa de cita para B.4.)
- J. Bognár, *Indefinite Inner Product Spaces*, Springer, 1974. (Teoría general de formas indefinidas; ortogonalidad de subespacios radicales de operadores Q-simétricos — D.1 está probado aquí de forma autocontenida, la referencia es de contexto.)
- I. S. Iohvidov, M. G. Kreĭn, H. Langer, *Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*, Akademie-Verlag, 1982. (Espacios $\Pi_\kappa$; contexto de D.5 y de la lectura "dicotomía de Pontryagin sin Pontryagin" de C.1.)
- W. Scharlau, *Quadratic and Hermitian Forms*, Springer, 1985. (Descomposición de Witt; multiplicatividad de la signatura — contexto de A.2–A.4, E.2; las pruebas usadas son autocontenidas.)
- S. Gershgorin, *Über die Abgrenzung der Eigenwerte einer Matrix*, Izv. Akad. Nauk SSSR 1931. (Discos de Gershgorin — C.1, C.3.)
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959. (Inercia, formas de Hankel; contexto.)
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11 (1936). [vía Doc 112 §3.3 — calibración M3.]

*Fin del Doc 132.*
