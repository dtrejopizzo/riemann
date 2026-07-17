# Doc 140 — Auditoría adversarial: el álgebra de Weil–Toeplitz, la tricotomía por visibilidad, y el teorema de Fredholm

**Programa:** Hipótesis de Riemann — Phase 46: AUDITORÍA Y ATAQUES.
**Fecha:** junio 2026.
**Rol del documento:** adversarial puro. Mandato: destruir. Objetos auditados: Doc 134 (símbolo/compacto,
tricotomía, Thm 1.3), Doc 132 (B.4, Teorema D, Witt), y las secciones operatoriales de P47
(`06-papers/P47-weil-toeplitz-logistic/main.tex`, §§2–4 y thm:exact/thm:strict/thm:thin/thm:blind/thm:nogo).
**Método:** re-derivación línea a línea de cada prueba, búsqueda de casos degenerados, contraejemplos
explícitos en forma cerrada. Sin numéricos. Citas solo hacia atrás (corpus + Kato, Reed–Simon, Murphy,
Bognár, Iohvidov–Kreĭn–Langer, Böttcher–Silbermann, Rabinovich–Roch–Silbermann).

---

## 0. VEREDICTO POR PIEZA

| pieza | objeto | veredicto |
|---|---|---|
| **(a)** | Thm 1.3 (D134) / thm:exact (P47): $\delta(G+K)<\infty\ \forall K$ compacto ⟺ positividad esencial estricta | **SOBREVIVE.** Prueba correcta en las tres direcciones, incluido el caso límite $\mu=0$. Una errata cosmética (el $n_0=4$ es innecesariamente conservador; vale $n_0=1$). Ámbito: $G=G^*$ **acotado** — la restricción es load-bearing y está declarada (Def. 2.4 D132), pero ver §2 abajo: la aplicación a $Z_\zeta$ está fuera del ámbito probado. |
| **(b)** | B.4 (D132): positividad esencial ⟹ $\delta<\infty$, estable bajo compactos | **SOBREVIVE** como teorema sobre $G$ acotado de tipo Hilbert. **SOBREVIVE CON ADVERTENCIA** como herramienta del programa: la positividad esencial NO es un invariante de la forma de Weil — es un invariante del par (forma, norma de Hilbert), y el propio Doc 134 (Teorema 2.2) prueba que en la normalización natural el enunciado es vacío. El doc lo sabe; el riesgo es que citas futuras lo olviden. |
| **(c)** | $\mathcal W$, $\mathcal J$, corona, símbolo; Lemas 3.2–3.3; **Thm 5.2 / tricotomía** | El esqueleto C\* **SOBREVIVE** íntegro (§1). El Thm 5.2 **SOBREVIVE CON ERRATA** (la cláusula (iv) de D134 falla en el caso degenerado y la propia prueba lo admite; P47 ya la eliminó). El **Thm 5.3 MUERE EN SU CLÁUSULA RUIDOSA**: la excepción "$\vartheta_n\le\omega_n$ eventualmente" es FALSA — contraejemplo en §4.2; la versión corregida (sin excepción) es más limpia y todo lo downstream sobrevive. La frase "los ceros viven en la frontera" es **TEOREMA-EN-MODELO para estratos puros, METÁFORA como enunciado global sobre ζ** (las clases gordo/fino/sub-resolución son relativas al calendario; el propio Thm 5.5 lo dice). El Thm 5.4 es **casi-axioma disfrazado de teorema** dentro de $\mathfrak W$ (§4.3). |
| **(d)** | $\delta=1$ prohibido (Teorema D.4, D132) | **SOBREVIVE CON CAVEAT DE ÁMBITO.** La prueba es correcta. Pero la hipótesis $z^2\notin\mathbb R$ es load-bearing y excluye exactamente los casos por los que pregunta el protocolo: espectro real (tipo Siegel) y el punto fijo $z=0$ ($s=\tfrac12$). El eslogan "la simetría funcional fuerza paridad" es falso sin esa hipótesis (contraejemplo §5.2). Para ζ es inocuo (ζ no tiene ceros reales en $(0,1)$); para la categoría general NO lo es. |
| **(e)** | $\mathcal K_{\mathrm{off}}$ Witt-trivial (D132 §8.2(b)) | **SOBREVIVE para $m<\infty$; deslizamiento para $m=\infty$.** La cadena D.1→D.2→D.4→E.2 es correcta en dimensión finita. La frase "vive en el ideal absorbente" usa la teoría de Witt finito-dimensional (E.2); bajo $\neg$RH con $m=\infty$ la signatura $(\infty,\infty)$ no está cubierta por E.2 y el enunciado debe leerse por truncación. Además depende de la no-degeneración de $Q|_{\mathcal K_{\mathrm{off}}}$, heredada del modelo. |

**No se encontró ningún error que tumbe la arquitectura.** Se encontraron: un enunciado falso reparable
(Thm 5.3 ruidoso), una cláusula admitida-fallida (5.2(iv)), dos deslizamientos de lenguaje ("campo
continuo", "los ceros viven en la frontera" como global), y dos fronteras de ámbito que el corpus debe
respetar a perpetuidad ($G$ acotado; $z^2\notin\mathbb R$).

---

## 1. Verificación C\* de $\mathcal W$ (protocolo 1)

### 1.1. ¿Es $\mathcal W$ genuinamente una C\*-álgebra? — SÍ

$\mathcal W=\prod^b_n\mathcal B(H_n)$ con $\|A\|=\sup_n\|A_n\|$ y operaciones puntuales es el
**producto $\ell^\infty$ de C\*-álgebras**: completitud (límite uniforme de secciones acotadas por
componentes), $\|A^*A\|=\sup_n\|A_n^*A_n\|=\sup_n\|A_n\|^2=\|A\|^2$ (la identidad C\* pasa al sup
porque vale en cada componente y el sup de cuadrados es el cuadrado del sup para no-negativos).
Estándar [Murphy, *C\*-Algebras and Operator Theory*, §1; Dixmier, *C\*-algèbres*, §1.9]. Sin objeción.

### 1.2. ¿Es $\mathcal J$ un ideal bilátero cerrado? — SÍ

$\mathcal J=\{A:\|A_n\|\to0\}$: (i) subespacio cerrado — si $A^{(k)}\to A$ en sup-norma con
$\|A^{(k)}_n\|\to_n0$, entonces $\limsup_n\|A_n\|\leq\|A-A^{(k)}\|\to_k0$; (ii) bilátero —
$\|B_nA_n\|,\|A_nB_n\|\leq\|B\|\,\|A_n\|\to0$. Es la suma directa $c_0$,
$\bigoplus_{c_0}\mathcal B(H_n)$. Sin objeción.

### 1.3. ¿El símbolo es un \*-homomorfismo bien definido? — SÍ, trivialmente

$\sigma:\mathcal W\to\mathcal C=\mathcal W/\mathcal J$ es el cociente C\* canónico: \*-homomorfismo
sobreyectivo de norma 1. No hay nada que verificar más allá de 1.1–1.2. La identificación con el Calkin:
$\bigoplus_nA_n$ es compacto en $\bigoplus_nH_n$ ⟺ $\|A_n\|\to0$ (cada bloque es de dimensión finita,
luego compacto; la cola domina la distancia a rangos finitos) — correcto. Y la inclusión
$\mathcal W/\mathcal J\hookrightarrow$ Calkin$(\bigoplus H_n)$ es un \*-monomorfismo unital
($\ker=\mathcal W\cap\mathcal K=\mathcal J$), luego **isométrico y espectralmente permanente**
[Murphy, Thm. 2.1.11, Thm. 3.1.5]: $\mathrm{spec}_{\mathcal C}(\sigma(A))=\mathrm{spec_{ess}}(\bigoplus A_n)$.
Esto valida la palabra "espectro esencial de la familia" con precisión total. Sin objeción.

### 1.4. ¿"Campo continuo" en el sentido de Dixmier? — NO, y es un deslizamiento de lenguaje (menor)

Un campo continuo de Dixmier requiere base topológica y condiciones de continuidad de $n\mapsto\|A_n\|$.
Aquí la base es $\mathbb N$ **discreto**: toda sección acotada es "continua" vacuamente. El Doc 134 §3
define el objeto con precisión y no reclama estructura de Dixmier; pero el **abstract de P47** dice
"continuous field of finite-dimensional Hilbert spaces" — técnicamente cierto y matemáticamente vacío
sobre base discreta. **Deslizamiento declarado:** la palabra "continuo" no porta contenido; debería decir
"$\ell^\infty$-producto" o "campo sobre $\mathbb N$". No afecta ningún teorema (ninguna prueba usa
continuidad).

### 1.5. Lemas 3.2–3.3 re-derivados — CORRECTOS

**Lema 3.2** ($\|\sigma(A)\|=\limsup\|A_n\|$): ambas desigualdades verificadas; es el caso diagonal del
cálculo de la norma esencial por truncación. Correcto. (Es además el hecho clásico
$\ell^\infty/c_0$-norma = $\limsup$.)

**Lema 3.3** (espectro del símbolo = conjunto límite de los espectros de ventana): re-derivado. La
dirección ($\supseteq$ por contrarrecíproco) usa correctamente que para autoadjuntos
$\|(A_n-\lambda)^{-1}\|=\mathrm{dist}(\lambda,\mathrm{spec}\,A_n)^{-1}$; la dirección ($\subseteq$)
construye el inverso por ventanas con cola uniformemente acotada y resto de soporte finito. Correcto.
Punto fino verificado: la invertibilidad por izquierda y derecha de $(A_n-\lambda)B_n$,
$B_n(A_n-\lambda)$ para $n$ grande sí da invertibilidad de $A_n-\lambda$ (inverso a derecha + inverso a
izquierda ⟹ invertible). Es el caso diagonal-trivial de la teoría de operadores límite de RRS, como el
doc declara honestamente. **El Corolario 3.4 es correcto** y la identificación cuantificador-uniforme =
positividad estricta del símbolo es exacta (sin metáfora): verificada leyendo 3.3 dos veces, con el punto
fino de que "débil" ⟺ $\liminf_n\lambda_{\min}(A_n)\geq0$ (una sucesión acotada con
$\lambda_{\min}(A_{n_k})\leq-\varepsilon$ i.o. produce punto límite $\leq-\varepsilon$).

**Veredicto §1: el esqueleto C\*-algebraico es impecable.** Lo que NO es teorema es la instancia Weil del
campo (Def. 3.6): la acotación $\sup_n\|Q_n\|<\infty$ es GAP-134.R, declarado. Correctamente etiquetado.

---

## 2. Re-derivación de B.4, con el asunto dominio/acotación explícito (protocolo 2)

### 2.1. El teorema tal como está enunciado — CORRECTO

D132 Def. 2.4 restringe a objetos **de tipo Hilbert**: $Q_C(x,y)=\langle Gx,y\rangle$ con
$G=G^*\in\mathcal B(H)$ **acotado**. Bajo esa hipótesis:

1. **Lema 4.1** ($\delta=\dim\mathrm{ran}\,E_G(-\infty,0)$): re-derivado; la inyectividad de
   $E_G(-\infty,0)|_N$ para $N$ negativo es correcta. ✓
2. **B.4:** $\mathrm{spec_{ess}}(G)\subseteq(0,\infty)$ con $G$ acotado ⟹ $\mathrm{spec_{ess}}$ es
   **compacto** no vacío ⟹ automáticamente $\subseteq[c,\infty)$ con $c>0$ (Obs. 1.2 de D134 — el doc
   detectó él mismo este punto). Entonces $\mathrm{spec}(G)\cap(-\infty,0]$ es compacto, discreto (puntos
   de acumulación irían al espectro esencial), finito, de multiplicidades finitas: $\delta(G)<\infty$.
   Weyl [Kato, Thm. IV.5.35] da la estabilidad bajo $K$ compacto. ✓ Sin error.

### 2.2. El punto que el protocolo señaló como más probable de fallo — y cómo los docs lo esquivan (y dónde NO)

**El argumento "parte negativa de rango infinito ⟹ espectro esencial negativo" requiere tres cosas:**
operador (no solo forma), autoadjunto, **acotado** (o al menos semiacotado con dominio de forma cerrado).
Para formas cuadráticas no acotadas la cadena se rompe en dos lugares: (i) sin representación de operador
(KLMN exige semiacotación + clausurabilidad relativa) ni siquiera existe $E_G$; (ii) para $G$ no acotado
con $\mathrm{spec_{ess}}\subseteq(0,\infty)$, el espectro esencial es cerrado pero **no compacto**, y
$\subseteq(0,\infty)$ ya NO implica gap (ej.: espectro esencial $\{1/n\}_n\cup[1,\infty)$… cerrado no lo
es; pero $\overline{\{1/n\}}\ni0$ — el punto es que sin compacidad la Obs. 1.2 falla y débil/estricta
deben distinguirse a mano). **Los docs NO cometen este error**: todos los teoremas B están bajo Def. 2.4
(G acotado). El asunto Pontryagin: en un espacio de Pontryagin $\Pi_\kappa$ con majorante de Hilbert, el
Gram $J$ de la forma es acotado e invertible [Bognár, *Indefinite Inner Product Spaces*, Ch. V;
Iohvidov–Kreĭn–Langer, §1], así que la instancia (I1) es de tipo Hilbert **si** la realización P35
entrega el majorante — que es exactamente la conjetura puente P35, declarada.

**Donde el deslizamiento SÍ amenaza:** DESEO 8.D1 ("probar que el Gram de la forma de Weil es
esencialmente positivo") está formulado como si "el Gram de la forma de Weil" fuera un objeto único. No
lo es: **la positividad esencial es un invariante del par (forma, producto interno de Hilbert), no de la
forma**. El propio Doc 134 lo prueba de la manera más dura posible: Teorema 2.2 (en peso fijo el gap
muere incondicionalmente, certificado vacío) versus §3–5 (en normalización por ventanas el mar tiene gap
$1-r$ pero el certificado pierde completitud). Mi re-derivación del Teorema 2.2 vía Lema 1.5: correcta
(el detector de gap por sucesiones ortonormales es el criterio de Weyl en forma cuadrática; la prueba con
$E$ de rango finito y $u_n\rightharpoonup0$ es estándar y sin fisuras). **Conclusión adversarial:** B.4
sobrevive como teorema; "positividad esencial del Gram de Weil" como objetivo del programa es un
enunciado **incompleto hasta fijar la realización**, y las dos realizaciones honestas conocidas fallan o
quedan condicionadas (Thm 2.2 / GAP-134.R). Esto no es un error de los docs — es su hallazgo central —
pero queda registrado como **regla de cita obligatoria**: ninguna invocación futura de B.4/8.D1 sin
especificar la norma.

### 2.3. Contraejemplo delimitador re-verificado

$G=\mathrm{diag}(-1/n)$: $\mathrm{spec_{ess}}=\{0\}$, débilmente positivo, $\delta=\infty$. Correcto, y
por el Thm 1.3 es el caso genérico. ✓

---

## 3. Thm 1.3 / thm:exact, ambas direcciones (protocolo 3)

### 3.1. (i)⟹(ii) y (iii)⟺(i) — CORRECTAS

(i)⟹(ii) es B.4 (§2.1). (iii)⟺(i): $\delta(G-\varepsilon I)=\dim\mathrm{ran}\,E_G(-\infty,\varepsilon)$
(traslación de la medida espectral, exacto); finitud ⟺ $\mathrm{spec}(G)\cap(-\infty,\varepsilon)$
finito de multiplicidades finitas ⟺ $\mathrm{spec_{ess}}\subseteq[\varepsilon,\infty)$. ✓

### 3.2. (ii)⟹(i), la dirección nueva — CORRECTA, re-derivada paso a paso

Sea $\mu\in\mathrm{spec_{ess}}(G)$, $\mu\leq0$ (la negación de estricta para $G$ acotado es exactamente
esto, por compacidad de $\mathrm{spec_{ess}}$).

- **Paso 1.** $\dim\mathrm{ran}\,E_G(\mu-\epsilon,\mu+\epsilon)=\infty$ para todo $\epsilon>0$: es la
  caracterización del espectro esencial de autoadjuntos [Reed–Simon IV, §XIII.4]. La elección inductiva
  ortonormal con $\|(G-\mu)e_n\|\leq8^{-n}$: correcta (la estimación integral espectral es exacta). ✓
- **Paso 2.** $|\langle Ge_n,e_m\rangle|\leq8^{-\max(n,m)}$ para $n\neq m$: verificado por las dos vías
  (autoadjunción da las dos cotas $8^{-n}$ y $8^{-m}$). Diagonal:
  $\langle Ge_n,e_n\rangle=\mu+\langle(G-\mu)e_n,e_n\rangle\leq\mu+8^{-n}\leq8^{-n}$ usando $\mu\leq0$. ✓
- **Paso 3.** $K=-\sum2^{-n}\langle\cdot,e_n\rangle e_n$ compacto autoadjunto. Cota del término cruzado
  vía Schur por filas: $r_n\leq(n+1)8^{-n}$ — re-derivada, correcta (y válida para vectores $\ell^2$
  completos, no solo soporte finito, de modo que la negatividad se extiende al span cerrado; para
  $\delta=\infty$ basta el span algebraico). Coeficiente final $(n+2)8^{-n}-2^{-n}<0$ ⟺ $n+2<4^n$, que
  vale para **todo $n\geq1$** — el $n_0=4$ del doc es innecesario (errata cosmética, no error). ✓

**La pregunta del protocolo** ("¿qué pasa si $0\in\mathrm{spec_{ess}}$ pero no hay parte negativa
esencial?"): es exactamente el caso $\mu=0$, y la construcción lo cubre sin modificación — el diagonal
queda $\leq8^{-n}$ y la perturbación $-2^{-n}$ domina. Es el ataque "diag$(+1/n)$ más compacto que lo
hunde". **El doc anticipó y resolvió el punto más probable de fallo.** La equivalencia es genuinamente
exacta y el cuantificador "para todo compacto" es necesario (sin él, (ii) con $K=0$ no implica (i):
diag$(-1/n)$ tiene… no: diag$(-1/n)$ tiene $\delta=\infty$ ya con $K=0$; el ejemplo correcto es
diag$(+1/n)$: $\delta(G)=0$ pero $\delta(G+K)=\infty$ para el $K$ del Paso 3 — la finitud no-robusta
existe, el cuantificador no es decorativo). ✓

**Veredicto: (a) SOBREVIVE.** Es, junto con los Lemas 3.2–3.3, la pieza más sólida del paquete.

---

## 4. La tricotomía (protocolo 4)

### 4.1. ¿"Gordo/fino/sub-resolución" están definidos sin referencia a RH? — SÍ, pero NO sin referencia al calendario

Las clases se definen por $\delta_j\,a(\gamma_j)$ — datos de la configuración $Z$ y del calendario $a$,
cero referencia a RH ni a primos. ✓ Pero **no son intrínsecas a los ceros**: un mismo cuádruplo es gordo
para un calendario y sub-resolución para otro (Thm 5.5(b): todo cuádruplo es gordo para algún $a$). El
propio documento lo convierte en teorema (5.5: $m=\sup_a m_a$, cuantificador de resolución). Por lo
tanto la frase-titular **"los ceros viven en la frontera símbolo/compacto" es:**

- **TEOREMA dentro de $\mathfrak W$ para configuraciones de estrato puro fino-visible** (Thm 5.2(i)–(iii),
  verificado abajo): los negativos se acumulan en $0\in\mathrm{spec}(\sigma(Q))$;
- **METÁFORA como enunciado global sobre los ceros de ζ**: (1) los estratos son relativos a $a$; (2) los
  gordos NO viven en la frontera (viven en el interior negativo del símbolo, 5.1) y los sub-resolución NO
  viven en la frontera (viven en el ideal, 5.4) — la frase exacta sería "el estrato intermedio vive en la
  frontera"; (3) la instancia Weil de los axiomas (S1)–(S3),(V2) es mixta/GAP (tabla Obs. 4.5, declarada).
  La Observación 5.6 del Doc 134 es honesta (tabla por estrato); el titular del resumen y de P47
  (Remark rem:trichotomy: "off-critical zeros live exactly on the symbol/compact boundary") **eleva el
  estrato intermedio a global**. Deslizamiento retórico declarado; no hay error matemático detrás porque
  los enunciados formales sí están estratificados.

### 4.2. EL HALLAZGO PRINCIPAL: el Teorema 5.3 (caso ruidoso) es FALSO tal como está enunciado

**Enunciado auditado** (D134 Thm 5.3(ii); P47 thm:strict, paréntesis): con ruido $\omega_n\to0$, la
positividad estricta del símbolo equivale a que las ventanas visibles terminen, *salvo a lo sumo ventanas
cuya visibilidad máxima cumple $\vartheta_n\to0$ y $\vartheta_n\leq\omega_n$ eventualmente* — es decir,
el enunciado afirma que infinitas ventanas pobladas "por debajo del ruido" **son compatibles con la
positividad estricta del símbolo**.

**Refutación (forma cerrada).** Supóngase $J_n^{\mathrm{vis}}\neq\emptyset$ para infinitos $n$, con
$\vartheta_n>0$ cualesquiera (en particular $\vartheta_n\leq\omega_n$). En $\mathfrak W$, la matriz
$Q_n-C_n$ tiene el autovalor exacto $-\vartheta_n$ (bloque hiperbólico). Por Weyl finito-dimensional
[Bhatia], $Q_n$ tiene un autovalor $\mu_n\in[-\vartheta_n-\omega_n,\,-\vartheta_n+\omega_n]$. La sucesión
$(\mu_n)$ sobre las ventanas pobladas es acotada; sea $\ell$ cualquier punto de acumulación. Entonces
$$\ell\;\leq\;\limsup_n\,(-\vartheta_n+\omega_n)\;\leq\;\limsup_n\,\omega_n\;=\;0 .$$
Por el Lema 3.3, $\ell\in\mathrm{spec}(\sigma(Q))\cap(-\infty,0]$: **la positividad estricta FALLA,
siempre que haya infinitas ventanas visibles, sin importar la comparación $\vartheta_n$ vs $\omega_n$.**
Instancia explícita que satisface la cláusula de excepción y refuta la equivalencia: $\omega_n=1/n$,
una población en cada $n$ par con $\vartheta_n=1/(2n)$; los autovalores perturbados del bloque están en
$[-3/(2n),\,1/(2n)]\to0$, luego $0\in\mathrm{spec}(\sigma(Q))$ y no hay gap — pero la cláusula del
teorema la declara compatible con la estricta. Contradicción.

**Diagnóstico.** El error está en la última línea de la prueba de D134 ("autovalores reabsorbidos al lado
positivo"): que el autovalor pueda ser $\geq0$ ventana a ventana no impide que tienda a $0$, y $0$ como
punto límite ya mata la estricta (Lema 3.3). La intuición correcta que el autor persiguió es "por debajo
del ruido el bloque no debería estar en el modelo" — defensa de modelado legítima, pero entonces el
enunciado debe modificar la **Definición 4.4** ($J_n^{\mathrm{vis}}$ con umbral $\theta_j>\omega$), no
añadir una excepción falsa al teorema.

**Reparación (y es una mejora).** El enunciado correcto, probado por el argumento de arriba más la
dirección limpia ($J_n^{\mathrm{vis}}=\emptyset$ eventualmente ⟹
$\mathrm{spec}(Q_n)\subseteq[1-r-\omega_n,1+r+\omega_n]$ ⟹ $\Lambda(Q)\subseteq[1-r,1+r]$):

> **Thm 5.3′ (corregido, caso ruidoso incluido).** Positividad estricta del símbolo ⟺
> $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$. Sin cláusula de excepción.

La equivalencia corregida es **más fuerte y más limpia**; el Cor. 5.3bis (cota cuantitativa
$m_a^{\mathrm{vis}}\ll N_0\log N_0$), la ruta LP-134 (que usa 5.1+5.3 con el gap (V2) $\theta\geq c_0$,
régimen donde la cláusula nunca se invocaba) y el Thm 7.2 sobreviven sin cambio. **Errata a propagar:
D134 Thm 5.3(ii) y P47 thm:strict (paréntesis) — añadir a 06-papers/ERRATA.md.**

### 4.3. Thm 5.2 — SOBREVIVE CON ERRATA (la cláusula (iv))

(i)–(iii) re-derivados: correctos dentro de $\mathfrak W$ (con el punto fino de que (i) requiere
$\vartheta_n>\omega_n$ en infinitas ventanas para que los autovalores límite sean *genuinamente
negativos*; si no, $0\in\Lambda$ igualmente como límite de autovalores de signo no controlado — la
acumulación en $0$ y el fallo de la estricta (iii) valen en todos los casos; la frase "alcanzado como
límite de autovalores negativos" requiere la sub-hipótesis). **(iv)** ($\delta=\infty$ en la suma directa
del campo): la propia prueba de D134 admite a mitad de camino que "en ese caso degenerado la negatividad
por ventana puede perderse" y re-dirige al nivel de la forma completa — es decir, **el enunciado (iv) tal
como está formulado no está probado en el caso degenerado** $\vartheta_n\leq\omega_n$ a.e. P47 eliminó
(iv) de thm:thin: corrección ya ejecutada en el paper. Para D134: restringir (iv) a
"$\vartheta_n>\omega_n$ en infinitas ventanas pobladas, o leer $\delta$ al nivel de la forma completa".

### 4.4. Thm 5.4 — VERDADERO pero con contenido mayormente axiomático; etiquetarlo

En $\mathfrak W(Z)$, la Definición 4.4 estipula que los cuádruplos con $\theta_j=0$ "no aparecen en
$H_n$: su efecto entero está absorbido en $R_n/C_n$". Con esa estipulación,
$Q_n-Q_n^{\mathrm{aut}}=C_n$ (ambas secciones comparten $I+R_n$), y $\|C_n\|\leq\omega_n\to0$:
$Q-Q^{\mathrm{aut}}\in\mathcal J$ **por construcción del modelo**. La prueba de D134 invoca además una
cota de perturbación $\sum_j\varphi(\delta_ja(\gamma_j))$ que NO es ninguno de los axiomas (S1)–(S3) tal
como están escritos — es la "forma de perturbación de (V1)", una extensión implícita del modelo cuyo
contenido real es el CÁLCULO 4.3 (Paley–Wiener) más el Teorema 3.3 del Doc 108 (estatus declarado).
**Veredicto:** el enunciado es verdadero (en la versión estipulada es trivial; en la versión con cota es
una extensión declarable del modelo), pero la etiqueta [TEOREMA] sobre-vende: la ceguera sub-resolución
es esencialmente el axioma de absorción, y el único ancla no-axiomática es D108 Teo. 3.3. El no-go 5.5 y
la Prop. 5.5bis (re-derivados: construcción explícita $\delta_j=\min(\tfrac14,1/(ja(\gamma_j)))$,
monotonía, cofinalidad) son correctos — y son la parte honesta y dura del documento: el cuantificador
maestro reaparece como cuantificador de resolución, dicho por los propios docs.

### 4.5. Lemma 5.0, Thm 5.1, Thm 7.2, Teorema 6.1/6.1bis, Prop. 6.3/7.4 — CORRECTOS

Re-derivados todos. Notas menores: (1) P47 lem:window-spec tiene la cadena tipográfica
"$\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n\geq\lambda_{\min}$" — debe ser
"$\lambda_{\min}\leq\langle Q_nv,v\rangle\leq-\vartheta_n+\omega_n$" (errata tipográfica, contenido
correcto). (2) Thm 6.1bis usa $\mathrm{dist}_H(\mathrm{spec}A,\mathrm{spec}B)\leq\|A-B\|$ para
autoadjuntos en una C\*-álgebra — correcto (perturbación estándar del espectro; vale en cualquier
C\*-álgebra vía representación fiel). (3) Prop. 7.4: la cota $\mathrm{tr}(BA)\geq-\varepsilon\,\mathrm{tr}(A)$
para $B\geq-\varepsilon I$, $0\leq A\leq I$ es correcta; el promedio con densidad de ventanas malas
$\to0$ y límite de Banach: correcto.

---

## 5. Paridad y Witt (protocolo 5)

### 5.1. Re-derivación de D.1–D.4 — pruebas CORRECTAS

- **D.1** (ortogonalidad radical, $w\neq\bar z$): la inducción sobre $p+q$ con
  $(z-\bar w)Q(u,v)=Q(u,v')-Q(u',v)$ es correcta (verificada la sesquilinealidad: $Q(u,Av)$ con
  $A$ $Q$-simétrico y autovalor $w$ en la segunda variable produce $\bar w$). ✓
- **D.2** (apareamiento hiperbólico): isotropía de $H[z]$ para $z\notin\mathbb R$ vía D.1 con $w=z$
  ($\bar z\neq z$); el apareamiento no degenerado $H[\bar z]\cong H[z]^*$ y la signatura $(d_z,d_z)$
  vía SVD del bloque $\begin{psmallmatrix}0&B\\B^*&0\end{psmallmatrix}$: correctos. ✓
- **D.3** ($\delta=\sum d_z$): aditividad A.1(ii) sobre la descomposición $Q$-ortogonal. ✓
- **D.4** (paridad): $SH[z]=H[-z]$ (inducción en el índice nilpotente, correcta); los cuatro puntos
  $z,\bar z,-z,-\bar z$ son distintos **exactamente porque** $z\notin\mathbb R\cup i\mathbb R$;
  $\delta=2\sum d_z$ par. ✓ La prueba no usa $\epsilon_S$: correcto, solo necesita $S$ biyectiva
  conmutando como $SAS^{-1}=-A$.

### 5.2. El error de paridad que el protocolo pedía buscar — NO existe dentro del ámbito, pero el ÁMBITO es la trampa

**Ceros EN la línea crítica (multiplicidad par o impar):** $z=\rho-\tfrac12\in i\mathbb R$ ⟹
$z^2\in\mathbb R$ ⟹ **excluidos de $P$ por definición**. El teorema no dice nada de ellos; en la forma
de Weil contribuyen masa $\geq0$ y no tocan $\delta$. Sin error. **El punto fijo $s=\tfrac12$:** $z=0$,
excluido igual. Sin error.

**Pero — espectro real ($z\in\mathbb R\setminus\{0\}$, i.e. $\rho$ real $\neq\tfrac12$): aquí la paridad
es FALSA y la hipótesis $z^2\notin\mathbb R$ es la única muralla.** Contraejemplo en forma cerrada dentro
de la categoría: $H=P=\mathbb Cu\oplus\mathbb Cv$, $A=\mathrm{diag}(t,-t)$ con $t\in\mathbb R\setminus\{0\}$,
$Su=v$, $Sv=u$ (entonces $SAS^{-1}=-A$ ✓, $S^2=1$ ✓), y $Q=-I$ (negativa definida; $Q(Sx,Sy)=Q(x,y)$ ✓;
$A$ es $Q$-simétrico pues $Q(Ax,y)=-\langle Ax,y\rangle$ y $A$ es… tómese $A$ real diagonal, simétrico
para $-\langle\cdot,\cdot\rangle$ ✓). Objeto espectral con simetría funcional plena y
$\delta=2$ — bien; ahora tómese el sub-objeto $H=P=\mathbb Cu\oplus\mathbb Cv$ con
$Q=\mathrm{diag}(-1,+1)$: $Q(Sx,Sy)=\epsilon_SQ$ con $\epsilon_S=-1$ ✓ y $\delta=1$ **impar, con
simetría funcional** — posible únicamente porque el espectro es real. Traducción aritmética: un **cero de
tipo Siegel–Landau** ($\beta\in(\tfrac12,1)$ real; $z=\beta-\tfrac12\in\mathbb R$) cae fuera de D.4: la
pareja $\{z,-z\}$ que da la ecuación funcional NO produce plano hiperbólico forzoso (D.1 no se aplica:
$\bar z=z$), y $Q|_{H[z]}$ puede ser definida de dimensión impar. **Para ζ es inocuo** (ζ no tiene ceros
reales en $(0,1)$: $\zeta(s)<0$ allí — clásico), pero el eslogan categórico "todo objeto espectral con
simetría funcional tiene defecto par" (Obs. 6.1 D132) **es falso sin el caveat $z^2\notin\mathbb R$
explícito en cada cita**, y la categoría 𝒫ol_δ pretende alojar objetos de Dirichlet generales (D131,
$F_{p,\alpha}$, DH), donde ceros reales no están excluidos a priori. **Veredicto: SOBREVIVE CON CAVEAT DE
ÁMBITO obligatorio**; la formulación de D.4 es correcta porque la hipótesis está en la definición de
"objeto espectral", pero toda paráfrasis sin la hipótesis es falsa.

### 5.3. $\mathcal K_{\mathrm{off}}$ Witt-trivial — re-derivado

Para $m<\infty$: D.2+D.4 dan signatura $(2m,2m)$ sobre $\mathcal K_{\mathrm{off}}$; E.2 ("$\sigma=0$ ⟺
hiperbólico", vía el argumento del segmento real para el vector isótropo + parte anisótropa definida
[Scharlau]): re-derivado, correcto. $\theta=\tfrac12$ está en el ideal absorbente E.2: correcto. **Dos
deslizamientos menores:** (1) bajo $\neg$RH con $m=\infty$, la signatura es $(\infty,\infty)$ y E.2 (un
teorema finito-dimensional) no aplica literalmente — el enunciado vale por truncación/exhaución y así
debería decirse; (2) la no-degeneración de $Q|_{\mathcal K_{\mathrm{off}}}$ (necesaria para D.2) es
herencia del modelo de cuádruplos (D96/D106), no verificada aquí — riesgo bajo, declarable. La
consecuencia estructural (invisible para todo invariante multiplicativo; A.4 re-derivado vía el anillo
$\mathbb Z[\varepsilon]/(\varepsilon^2-1)$, correcto con la observación de que también exige dominio
íntegro **de característica 0 o $\neq2$** para $u=\pm1$ distintos — en característica 2 los dos
caracteres colapsan; irrelevante para el uso) queda en pie.

---

## 6. Consecuencias para P47

1. **thm:exact (= Thm 1.3): intacto.** Es publicable tal cual; es la mejor pieza del paper.
2. **thm:strict: ERRATA OBLIGATORIA.** El paréntesis "(With noise $\omega_n\to0$, the same equivalence
   holds up to windows whose maximal visibility satisfies $\vartheta_n\to0$ and
   $\vartheta_n\leq\omega_n$ eventually.)" es falso (§4.2). Reemplazar por: "With noise
   $\omega_n\to0$ the equivalence holds verbatim: strict symbol positivity iff
   $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$." La corrección **fortalece** el teorema y no toca
   cor:gap-quant, conj:lp134, thm:synergy ni rem:trichotomy.
3. **thm:thin: ya corregido** respecto de D134 (la cláusula (iv) fue eliminada); añadir si se desea la
   sub-hipótesis $\vartheta_n>\omega_n$ i.o. para la frase "attained as a limit of *negative*
   $\lambda_{\min}$"; (ii)–(iii) no la necesitan.
4. **lem:window-spec:** errata tipográfica en la cadena de desigualdades (§4.5).
5. **Abstract/intro:** sustituir "continuous field" por "$\ell^\infty$-product field over $\mathbb N$"
   o declarar la base discreta (§1.4).
6. **rem:trichotomy:** la frase "off-critical zeros live exactly on the symbol/compact boundary" debería
   decir "the *thin-visible stratum* lives on the boundary; fat strata in the symbol, sub-resolution in
   the ideal" — el cuerpo del paper ya lo dice bien; el remark global sobre-condensa.
7. **D134 propio:** corregir Thm 5.3(ii), restringir Thm 5.2(iv), re-etiquetar Thm 5.4 como
   "[TEOREMA-en-modelo-extendido; contenido no-axiomático = D108 Teo. 3.3]". Añadir las tres entradas a
   `06-papers/ERRATA.md`.
8. **Regla de cita a futuro (las dos murallas de ámbito):** (i) B.4/Thm 1.3 jamás sin "G acotado en la
   realización de Hilbert especificada" (la positividad esencial no es invariante de la forma — Thm 2.2
   lo prueba); (ii) D.4/paridad/Witt jamás sin "$z^2\notin\mathbb R$" (los ceros reales tipo Siegel rompen
   la paridad; para ζ inocuo, para la categoría no).
9. **Lo que esta auditoría NO toca:** la sección logística de P47 (thm:logistic, thm:realiz, thm:main) no
   fue objeto del mandato (a)–(e); sus dependencias declaradas (rem:deps) son honestas. Queda como
   objetivo natural de una auditoría separada (en particular el Step 3 de thm:realiz: el presupuesto de
   colas vía lem:tail, y la afirmación "the caveat was an artifact" del rem:key, que des-condiciona la
   Hipótesis D de P40 — es exactamente el tipo de des-condicionamiento que en este programa ha muerto
   antes bajo audit).

---

## Referencias

**Internas:** Doc 134 (objeto principal); Doc 132 (objeto principal); Doc 108 (Teo. 3.3, Lema 2.4,
§5.2); Doc 112 (LP-112, Prop. 2.6); Doc 98/95 (CCM); P35; P43; P47 main.tex; 06-papers/ERRATA.md
(destino de las erratas).

**Literatura:** G. J. Murphy, *C\*-Algebras and Operator Theory*, Academic Press, 1990 (Thm. 2.1.11
permanencia espectral; Thm. 3.1.5 monomorfismos isométricos). J. Dixmier, *Les C\*-algèbres et leurs
représentations*, Gauthier-Villars, 1969 (§1.9 productos; §10 campos continuos — la noción que el
abstract de P47 invoca vacuamente). T. Kato, *Perturbation Theory for Linear Operators*, 2.ª ed.,
Springer, 1976 (Thm. IV.5.35). M. Reed, B. Simon, *Methods of Modern Mathematical Physics IV*, Academic
Press, 1978 (§XIII.4, criterio de Weyl). J. Bognár, *Indefinite Inner Product Spaces*, Springer, 1974
(majorantes de Hilbert, Gram acotado en $\Pi_\kappa$). I. S. Iohvidov, M. G. Kreĭn, H. Langer,
*Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*, Akademie-Verlag,
1982. W. Scharlau, *Quadratic and Hermitian Forms*, Springer, 1985 (Witt). R. Bhatia, *Matrix Analysis*,
Springer, 1997 (Weyl finito-dimensional). A. Böttcher, B. Silbermann, *Analysis of Toeplitz Operators*,
2.ª ed., Springer, 2006. V. Rabinovich, S. Roch, B. Silbermann, *Limit Operators and Their Applications
in Operator Theory*, Birkhäuser, 2004. I. C. Gohberg, M. G. Kreĭn, *Introduction to the Theory of Linear
Nonselfadjoint Operators*, AMS, 1969 (contexto Fredholm/índice; ninguna prueba auditada lo requiere).

*Fin del Doc 140.*
