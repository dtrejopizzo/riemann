# Doc 117 — Auditoría adversarial: la identidad del índice tensorial (Doc 106, Prop. 3.5)

**Phase 38 — Auditoría final. Junio 2026.**

**Objeto auditado:** Proposición 3.1 / Corolario 3.2 / Proposición 3.3 / Proposición 3.5
del Doc 106 (`phase-36-ABC-forms/106-funtor-amplificador-busqueda.md`), tal como se
citan en P42 (Theorems 4.2 `thm:tensor-index` y 4.3 `thm:amplify`,
`06-papers/P42-amplification-survivor/main.tex`) y en P43 (ledger, ítem L3,
`06-papers/P43-master-quantifier/main.tex`, líneas 330–332). Insumo: la signatura
$(2m,2m)$ de $Q|_{\mathcal{K}_{\mathrm{off}}}$ (Doc 98, Prop. 6.1; Doc 96, Teo. 8.1).

**Mandato:** destruir, si es posible, los enunciados (A), (B), (C) descritos abajo.

---

## 0. Veredicto

**SOBREVIVE CON CORRECCIONES.**

- **(A)** la identidad $\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$: **SOBREVIVE
  INTACTA**. Álgebra lineal clásica, demostración correcta, consistente con la
  multiplicatividad de la signatura en el anillo de Witt.
- **(B)** $\kappa(\psi^{\otimes k})=(4m)^k/2$ para signatura $(2m,2m)$: **SOBREVIVE
  INTACTA como álgebra**; el *insumo* (la signatura $(2m,2m)$ del bloque off) es
  condicional al marco (V.1 / Hipótesis D) y P42 lo enuncia con menos cautela que los
  documentos fuente.
- **(C)** la superaditividad: la *identidad de defecto* es correcta, pero el
  **Corolario 3.2 del Doc 106 es falso tal como está escrito** (afirma $\geq 0$ sin la
  hipótesis $p_1,p_2\geq 1$; contraejemplo: $\langle-1\rangle\otimes\langle-1\rangle$),
  y su cláusula "i.e." de estrictitud también falla sin esa hipótesis. El **ítem L3 de
  P43** sobre-enuncia ("strictly superadditive" sin cualificador). El Theorem 4.2 de
  P42, en cambio, está redactado con la condición exacta y es correcto.

Ninguna de las correcciones toca el caso de uso ($p=q=2m$, $m\geq 1$, donde todo vale
con holgura), pero dos enunciados publicables (Cor. 3.2 del Doc 106 y L3 de P43)
necesitan retoque, y la condicionalidad del insumo debe declararse en P42.

---

## 1. Enunciado (A): $\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$

### 1.1 Verificación de la demostración (Doc 106, Prop. 3.1; P42, Thm. 4.2)

La prueba por bases de Sylvester es correcta en todos sus pasos, verificados uno a uno:

1. **Existencia de bases ortonormales con signos $\pm1$.** Para una forma hermitiana no
   degenerada sobre un $\mathbb{C}$-espacio de dimensión finita, la ley de inercia de
   Sylvester vale en versión hermitiana: existe base $Q$-ortogonal con
   $Q(e_a,e_a)=\varepsilon_a\in\{\pm1\}$ y la pareja $(p,q)$ es invariante. Referencia
   estándar: Bognár, *Indefinite Inner Product Spaces* (Springer 1974), Cap. I; también
   Gohberg–Lancaster–Rodman [GLR83], Cap. I (ya citado en Doc 98).
2. **El producto tensorial de formas hermitianas es hermitiano.** Con
   $(Q_1\otimes Q_2)(u_1\otimes u_2, v_1\otimes v_2)=Q_1(u_1,v_1)Q_2(u_2,v_2)$ y
   extensión sesquilineal: la simetría hermitiana del producto se hereda
   ($\overline{Q_1(v_1,u_1)Q_2(v_2,u_2)} = Q_1(u_1,v_1)Q_2(u_2,v_2)$), y la extensión
   sesquilineal a $V_1\otimes V_2$ está bien definida (bilinealidad del tensor en cada
   factor; la sesquilinealidad es en la *segunda* entrada de cada $Q_i$
   simultáneamente, sin conflicto). Sin sutileza oculta entre el caso simétrico real y
   el hermitiano complejo: la fórmula de signatura es la misma.
3. **La base producto es $(Q_1\otimes Q_2)$-ortogonal con valores
   $\varepsilon^{(1)}_a\varepsilon^{(2)}_b$.** Inmediato de la fórmula del producto.
4. **Conteo.** El valor es $-1$ sii exactamente un factor es negativo:
   $p_1q_2+q_1p_2$ direcciones negativas, $p_1p_2+q_1q_2$ positivas. Total
   $(p_1+q_1)(p_2+q_2)=\dim$, correcto.
5. **No-degeneración del producto.** Base ortogonal sin vectores isótropos ⟹ matriz de
   Gram diagonal con entradas $\pm1$ ⟹ invertible. Correcto. **La hipótesis de
   no-degeneración de los factores está declarada** en la Prop. 3.1 del Doc 106
   ("formas hermitianas no degeneradas") — sin ella el argumento falla (una dirección
   del radical de $Q_1$ tensorizada con cualquier cosa cae en el radical del producto,
   y "neg.ind" deja de estar dado por el conteo de Sylvester). P42 Thm 4.2 dice
   "quadratic forms of signature $(p_i,q_i)$" sin la palabra "non-degenerate";
   implícito en que la signatura agota la dimensión, pero conviene explicitarlo
   (corrección menor de redacción, no de contenido).

### 1.2 Verificaciones independientes

- **Ejemplo mínimo:** $(1,1)\otimes(1,1)$: dimensión 4, fórmula
  $1\cdot1+1\cdot1=2$ ⟹ signatura $(2,2)$. A mano: plano hiperbólico ⊗ plano
  hiperbólico = dos planos hiperbólicos. ✓
- **Caso definido-negativo:** $\langle-1\rangle\otimes\langle-1\rangle$: la fórmula da
  $0\cdot1+1\cdot0=0$ y en efecto $(-1)(-1)=+1$: el producto es definido positivo. La
  *fórmula* (A) maneja correctamente incluso este caso. (Quien falla aquí es la
  superaditividad; véase §3.)
- **Consistencia con el anillo de Witt** (sanity check de literatura): la signatura
  $\mathrm{sig}=p-q$ es multiplicativa bajo ⊗ — hecho clásico, Lam, *Introduction to
  Quadratic Forms over Fields* (AMS GSM 67, 2005), Cap. II (homomorfismo de signatura
  del anillo de Witt). Verificación:
  $p'-q'=(p_1p_2+q_1q_2)-(p_1q_2+q_1p_2)=(p_1-q_1)(p_2-q_2)$. ✓ La fórmula (A) es
  exactamente la única compatible con multiplicatividad de $p-q$ y de $p+q$ (dimensión).

**Conclusión (A): INTACTA.** No encontré grieta. La fórmula es correcta, la prueba es
correcta, y es literatura clásica reempaquetada (lo cual el propio Doc 106 no oculta).

---

## 2. Enunciado (B): $\kappa(\psi^{\otimes k})=(4m)^k/2$ para $\mathrm{sig}(\psi)=(2m,2m)$

### 2.1 La recursión y la forma cerrada

Recursión de signaturas bajo ⊗ (consecuencia directa de (A)):
$p'=p_1p_2+q_1q_2$, $q'=p_1q_2+q_1p_2$. Con $p_1=q_1=p_k$, $p_2=q_2=2m$ e inducción
sobre la hipótesis $p_k=q_k=(4m)^k/2$:
$$p_{k+1}=q_{k+1}=\tfrac{(4m)^k}{2}\cdot 2m+\tfrac{(4m)^k}{2}\cdot 2m
=2m\,(4m)^k=\tfrac{(4m)^{k+1}}{2}.$$
Base $k=1$: $(2m,2m)$, y $(4m)^1/2=2m$. ✓ Alternativamente, por la forma cerrada de la
Prop. 3.3 del Doc 106: $\mathrm{neg.ind}(Q^{\otimes k})=\frac{(p+q)^k-(p-q)^k}{2}$, que
con $p=q=2m$ da $\frac{(4m)^k-0^k}{2}=(4m)^k/2$ para $k\geq1$. (El término $0^k$ es $0$
para $k\geq1$; la fórmula no se aplica a $k=0$ y el Doc la restringe a $k\geq1$. ✓)

Verifiqué la Prop. 3.3 en general con un caso asimétrico a mano: $(p,q)=(1,2)$, $k=2$:
direcciones negativas = pares con exactamente un factor negativo = $2\cdot(1\cdot2)=4$;
fórmula: $\frac{3^2-(-1)^2}{2}=4$. ✓ La identidad binomial de la prueba es estándar. ✓

- **Enteridad:** $(4m)^k/2$ es entero para $k\geq1$ ($4m$ par); para $m=0$ da $0$. ✓
- **Coherencia estructural:** $\mathrm{sig}(\psi)=0$ (neutral) ⟹ por multiplicatividad
  de Witt todas las potencias son neutrales ⟹ $p_k=q_k=\dim/2=(4m)^k/2$. La fórmula es
  *forzada* por la estructura: medio espacio negativo en cada potencia. ✓
- **Caso $m=0$:** $\mathcal{K}_{\mathrm{off}}=0$, todas las potencias triviales,
  $\kappa=0$: la cláusula final del Thm 4.3 de P42 es correcta. ✓

### 2.2 El insumo $(2m,2m)$: dónde está la condicionalidad real

La Prop. 3.5 es álgebra incondicional **dado** que
$\mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}})=(2m,2m)$ y que la restricción es no
degenerada. Auditoría del insumo (Doc 98, Prop. 6.1):

1. **No-degeneración.** Probada en Doc 98 Prop. 6.1(c): si algún apareamiento
   $q_i=Q(v_{z_i},v_{\bar z_i})$ fuera $0$, la descomposición $Q$-ortogonal del Doc 96
   Teo. 8.1 sería degenerada. El argumento es correcto *dentro del marco* (depende de
   la no-degeneración global del Teo. 8.1, que a su vez depende de V.1).
2. **Colisiones y multiplicidades.** ¿Qué pasa con configuraciones especiales
   ($\gamma_i=\gamma_j$, ceros múltiples, bloques de Jordan para $\delta>0$)? Aquí la
   estructura es **robusta**, y conviene dejarlo escrito porque ninguno de los
   documentos lo dice con la referencia exacta: para una forma hermitiana no degenerada
   $Q$ y un operador $Q$-simétrico, los subespacios raíz de autovalores **no reales**
   (en el parámetro $z$; equivalentemente $\rho\notin\frac12+i\mathbb{R}$ tras el
   apareamiento $z\leftrightarrow\bar z$) se aparean en pares $\lambda,\bar\lambda$ con
   $Q$ restringida al par no degenerada y **neutral** — la característica de signos
   (sign characteristic) solo se adhiere a autovalores reales [GLR83, Cap. I, forma
   canónica de pares hermitianos]. Por tanto la signatura $(d,d)$ del bloque off (con
   $2d=\dim$) sobrevive a colisiones de cuádruplos y a no-semisimplicidad, mientras los
   autovalores sigan fuera del eje. La única degeneración es $\delta\to0$ (colisión
   *sobre* el eje crítico), que es exactamente el cambio de $m$ — y el GAP G4 del
   Doc 98 lo declara. Sin grieta nueva.
3. **¿Está declarada la Hipótesis D?** En el **Doc 106 sí**, ejemplarmente: §2 dice
   "Bajo Hipótesis D con $m$ órbitas… (P35, Conjetura puente, **asumida como marco**)".
   En **P42 la cautela se pierde**: la §2.4 (Framework) dice "the bridge theorem
   \cite{P35} *identifies*…" — P35 es una *conjetura puente* con programa de
   verificación V.1–V.4 abierto, no un teorema. Y el Thm 4.3 abre con "With $m\geq1$
   off-critical quadruples, $\psi$ *has* signature $(2m,2m)$" y el texto siguiente lo
   llama "unconditional". Lo incondicional es la *implicación algebraica*
   (signatura $(2m,2m)$ ⟹ $\kappa$ de las potencias); la *atribución* de esa signatura
   al objeto $(\mathcal{K}_{\mathrm{off}},Q)$ del programa hereda V.1 (vía Doc 96
   Teo. 8.1 y Doc 98 Prop. 6.1, cuya propia tabla de honestidad dice "V.1 de P35
   implícita"). **Corrección requerida en P42**: o declarar V.1/marco en el enunciado
   del Thm 4.3, o reformularlo como condicional ("If $\psi$ has signature $(2m,2m)$ —
   as it does under the framework of §2.4 — then…").

**Conclusión (B): INTACTA como álgebra; condicionalidad del insumo sub-declarada en
P42** (no en Doc 106, que es honesto).

---

## 3. Enunciado (C): superaditividad — aquí hay sangre

### 3.1 La identidad de defecto es correcta

$$\mathrm{neg.ind}(Q_1\otimes Q_2)-(q_1+q_2)=p_1q_2+q_1p_2-q_1-q_2
=(p_1-1)q_2+(p_2-1)q_1.$$
Identidad algebraica exacta, verificada. De aquí, el **Theorem 4.2 de P42** ("strictly
superadditive *whenever* $(p_1-1)q_2+(p_2-1)q_1>0$") es **literalmente correcto**: la
desigualdad estricta vale exactamente cuando esa cantidad es positiva, porque *es* esa
cantidad.

### 3.2 El Corolario 3.2 del Doc 106 es FALSO tal como está escrito

El Cor. 3.2 afirma, sin más hipótesis que las de la Prop. 3.1 (no-degeneración):
$$(p_1-1)q_2+(p_2-1)q_1\;\geq\;0.$$
**Contraejemplo:** $Q_1=Q_2=\langle-1\rangle$, i.e. $(p_i,q_i)=(0,1)$. Entonces
$\mathrm{neg.ind}(Q_1\otimes Q_2)=0$ pero $q_1+q_2=2$: el defecto es
$(0-1)\cdot1+(0-1)\cdot1=-2<0$. El índice negativo **no** es superaditivo en general:
negativo ⊗ negativo = positivo. La cláusula "i.e." de estrictitud también falla sin
hipótesis: con $(p_1,q_1)=(2,5)$, $(p_2,q_2)=(0,1)$ se cumple "$p_1\geq2$ y
$q_2\geq1$" pero el defecto es $(2-1)\cdot1+(0-1)\cdot5=-4<0$ (subaditivo).

**Corrección:** añadir la hipótesis $p_1,p_2\geq1$. Con ella ambos términos
$(p_i-1)q_j$ son $\geq0$, la superaditividad vale, y la estrictitud equivale a
"($p_1\geq2$ y $q_2\geq1$) o ($p_2\geq2$ y $q_1\geq1$)". En el caso de uso del programa
($p_1=p_2=2m\geq2$ para $m\geq1$, o $p=\infty$ en el espacio completo) la hipótesis se
cumple con holgura: **el daño no se propaga a ninguna aplicación**, pero el corolario
publicado como pieza quotable está mal enunciado.

### 3.3 P43, ledger L3: sobre-enunciado

L3 dice: "for indefinite quadratic forms of signatures $(p_i,q_i)$,
$\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$, **strictly superadditive**". Dos
problemas: (i) aun restringiendo a formas *indefinidas* ($p_i,q_i\geq1$), la
superaditividad **no siempre es estricta**: $(1,1)\otimes(1,1)$ da
$\mathrm{neg.ind}=2=q_1+q_2$, aditividad exacta; (ii) si "indefinite" no se asume
(la identidad vale en general), entra el contraejemplo de §3.2. **Corrección mínima en
P43:** "strictly superadditive whenever $(p_1-1)q_2+(p_2-1)q_1>0$" (la redacción de
P42 Thm 4.2, que es la correcta).

### 3.4 $\kappa(\psi^{\otimes k})\geq k\,\kappa(\psi)$

Para el caso enunciado ($\mathrm{sig}=(2m,2m)$, $m\geq1$):
$(4m)^k/2\geq 2mk\iff(4m)^{k-1}\geq k$, cierto para todo $k\geq1$ por inducción
($4^k\geq 4k\geq k+1$), con igualdad solo en $k=1$. La cláusula "with equality only at
$k=1$" del Thm 4.3 de P42 es correcta para $m\geq1$. ✓ Nota adversarial: la
$k$-superaditividad es **falsa en general** (con $(p,q)=(0,1)$:
$\kappa(\psi^{\otimes k})$ alterna $1,0,1,0,\dots<k$), pero ni P42 ni el Doc 106 la
reclaman fuera del caso $(2m,2m)$ — de hecho la Prop. 3.6 (esterilidad) *usa*
correctamente ese caso patológico. Sin grieta.

---

## 4. El uso en P42 §5 / P43 / P44 (acotado, sin re-auditar Doc 107)

- **P42 Thm 5.4 (`thm:signature`)** afirma signatura "exactly $(8,8)$ … with no
  degeneration" para el bloque doble. El Doc 107 (Teo. 5.5 + **Obs. 5.7**) prueba esto
  con tres caveats declarados que P42 omite: (i) el enunciado es sobre la forma $B$ del
  bloque off×off en el cociente de evaluación, y la localización doblada se hereda
  "módulo V.1-doblado" (mismo estatus que G4/G5 del Doc 98); (ii) pesos 1 por ceros
  simples (con multiplicidades la signatura no cambia — eso sí está cubierto);
  (iii) convención de apareamiento $z\leftrightarrow-\bar z$. Además, la
  sobreyectividad del mapa de evaluación (Lema 5.4 del Doc 107) es la que garantiza que
  el peso $\hat\varphi$ no degenera la realización; eso requiere condiciones de
  no-anulación de $\hat\varphi$ en los 16 puntos de diferencia — una condición de
  genericidad sobre $\varphi$ que P42 no enuncia. **Recomendación:** una frase en
  Thm 5.4 del estilo "for $\varphi$ with $\hat\varphi$ nonvanishing at the relevant
  difference points; inherited-framework caveats as in [Doc 107, Obs. 5.7]".
- **P43 L3:** corrección de §3.3. El resto del ítem ($\kappa(\psi^{\otimes k})
  =\frac12(4m)^k$ on $\mathcal{K}_{\mathrm{off}}$) es fiel a lo probado, módulo la misma
  observación de condicionalidad del insumo que en P42. El Thm B de P43 (línea 160ss)
  dice "amplifies exponentially **and unconditionally**" — misma corrección: la
  amplificación es incondicional *dada* la signatura; la signatura es del marco.
- **P44:** no cita la identidad tensorial directamente (solo menciona la amplificación
  de pasada, líneas 228–233, como mecanismo "transplantado"); nada que corregir allí.

---

## 5. Resumen de correcciones exigidas

| # | Lugar | Defecto | Corrección |
|---|---|---|---|
| 1 | Doc 106, Cor. 3.2 | "$\geq0$" falso sin $p_1,p_2\geq1$ ($\langle-1\rangle\otimes\langle-1\rangle$) | añadir hipótesis $p_1,p_2\geq1$; reescribir la cláusula "i.e." |
| 2 | P43, L3 | "strictly superadditive" sin cualificador (falso para $(1,1)\otimes(1,1)$ y para formas definidas negativas) | añadir "whenever $(p_1-1)q_2+(p_2-1)q_1>0$" |
| 3 | P42, §2.4 + Thm 4.3 | "the bridge theorem" (P35 es conjetura, V.1–V.4 abiertos); "unconditional" sin separar implicación algebraica de insumo | declarar el marco/V.1 en el enunciado o condicionar |
| 4 | P42, Thm 4.2 | "quadratic forms" sin "non-degenerate" (y son hermitianas) | una palabra |
| 5 | P42, Thm 5.4 | omite caveats de Doc 107 Obs. 5.7 y la genericidad de $\hat\varphi$ | una frase de remisión |

Ningún defecto toca el contenido matemático en el caso de uso $(2m,2m)$, $m\geq1$:
la Prop. 3.5 y su cadena de consecuencias son álgebra correcta y clásica
(Lam, *Introduction to Quadratic Forms over Fields*, GSM 67, Cap. II;
Bognár, *Indefinite Inner Product Spaces*, Cap. I; [GLR83], Cap. I).

**VEREDICTO: SOBREVIVE CON CORRECCIONES** — (A) y (B) intactas como álgebra; (C) y las
citas requieren los retoques de la tabla; la condicionalidad del insumo $(2m,2m)$ debe
declararse donde P42/P43 la omiten.
