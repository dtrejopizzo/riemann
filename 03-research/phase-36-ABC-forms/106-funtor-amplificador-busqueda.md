# Doc 106 — El funtor amplificador ⊠: búsqueda sistemática

**Phase 36 — Formas A/B/C · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Estado: búsqueda sistemática completada — axiomatización, inventario de cinco candidatos, análisis de colapso, veredicto**

---

## 0. Resumen ejecutivo

Este documento ejecuta el programa de la Forma B del paper P41 (Problema 7.2): buscar
sistemáticamente una operación $\boxtimes$ sobre el espacio de Pontryagin $(\mathcal{K},Q)$
de Weil–Connes — o sobre la categoría de triples CCM — que realice el esqueleto de
Deligne: invariante entero, amplificación superaditiva, cota uniforme sublineal.

**Hallazgos principales:**

1. **(§1) Axiomatización.** El mecanismo de Deligne se reduce a un teorema elemental
   (Teorema 1.4, con prueba completa): si $\kappa(\psi^{\boxtimes k}) \geq k\,\kappa(\psi)$
   y $\kappa(\psi^{\boxtimes k}) \leq f(k)$ con $f(k)/k \to 0$, entonces $\kappa(\psi)=0$.
   La dificultad nunca está en el teorema abstracto: está en exhibir $(\mathcal{C},
   \boxtimes, \kappa, f)$ con ambas propiedades **no circulares**.

2. **(§3.1) El cálculo central.** Para formas hermitianas de signaturas $(p_1,q_1)$ y
   $(p_2,q_2)$:
   $$\mathrm{neg.ind}(Q_1 \otimes Q_2) = p_1 q_2 + q_1 p_2.$$
   Consecuencia inmediata: el producto tensorial de espacios de Krein es **estrictamente
   superaditivo** en el índice negativo siempre que $(p_1-1)q_2 + (p_2-1)q_1 > 0$.
   **El falsador declarado en P41 ("κ es exactamente aditivo bajo todo ⊠ disponible")
   queda REFUTADO**: existe un producto natural con superaditividad estricta — de hecho,
   exponencial: sobre $\mathcal{K}_{\mathrm{off}}$ (signatura $(2m,2m)$),
   $\kappa(\mathcal{K}_{\mathrm{off}}^{\otimes k}) = (4m)^k/2$.

3. **(§3.1–3.2) El problema de dimensión infinita y su doble filo.** Sobre el espacio
   completo ($p = \infty$, $q = 2m$), $\mathrm{neg.ind}(Q\otimes Q) = \infty$ ya en $k=2$:
   el producto tensorial destruye la estructura de Pontryagin y con ella el teorema de
   Kreĭn–Langer. La regularización obligada (restricción a $\mathcal{K}_{\mathrm{off}}$,
   legítima por el Teorema 8.1 del Doc 96) salva (a) pero revela el problema real: **la
   superaditividad y el crecimiento del índice del tensor abstracto se calculan con los
   mismos datos de signatura; no hay input independiente**, luego del tensor abstracto no
   puede salir contradicción alguna (Proposición 3.9, el "lema de esterilidad").

4. **(§3.2) El objeto analítico del producto.** Los "ceros" de $\mathcal{K}_{\mathrm{off}}
   \otimes \mathcal{K}_{\mathrm{off}}$ son sumas $z_1+z_2$ de parámetros espectrales, i.e.
   puntos $\rho_1+\rho_2-1/2$. **Ninguna función L conocida tiene esos ceros.** La
   convolución de Rankin–Selberg, que es el realizador analítico natural de ⊗, es
   *grupal* en GL(1): $\mathbf{1} \boxtimes \mathbf{1} = \mathbf{1}$, $L(s, \mathbf{1}
   \times \mathbf{1}) = \zeta(s)$ — devuelve $\zeta$ sin amplificar nada. Toda operación
   que permanezca dentro de la clase de funciones L multiplica funciones L, y multiplicar
   funciones L **une** conjuntos de ceros (suma directa, κ aditivo exacto), no los
   **suma** (tensor). Dicotomía estructural: §3.2.4.

5. **(§3.3) Las correspondencias de Frobenius del sitio de escala** satisfacen
   $\Psi(\lambda)\circ\Psi(\lambda') = \Psi(\lambda\lambda')$ (con la deformación
   tangencial $\mathrm{Id}_\varepsilon$ en el caso mixto racional/irracional) — verificado
   en Connes–Consani. Son un **monoide multiplicativo de endomorfismos**, no un producto
   binario sobre objetos: sobre $(\mathcal{K},Q)$ inducen (módulo V.1) isometrías, y las
   isometrías **preservan** κ exactamente. No amplifican. El único lugar donde la
   estructura del sitio de escala ofrece un ⊠ genuinamente binario es el **cuadrado del
   sitio** — y eso es exactamente el programa Riemann–Roch inconcluso de Connes–Consani
   (MW-5).

6. **(§3.4) La convolución multiplicativa** sobre funciones de prueba colapsa a
   positividad CAP por el patrón de transmutación: hacer de $Q$ un funcional positivo
   sobre el álgebra $(\mathcal{S},\star)$ es literalmente la positividad de Weil (MW-1).
   FAIL I2a.

7. **(§5) Donde queda el peso.** Para el único candidato con (a) demostrada
   (tensor relativo sobre $\mathcal{K}_{\mathrm{off}}$), **todo el peso cae sobre (b)**:
   se necesita una familia $\{\psi^{\boxtimes k}\}$ con cota de finitud tipo C5 cuya
   fuente sea independiente de la posición de los ceros. El análogo exacto de "los polos
   de la L de la familia no se mueven" (racionalidad de Grothendieck en Weil I) sería una
   **racionalidad/Riemann–Roch sobre el cuadrado del sitio de escala**. Ese teorema no
   existe; es MW-5. El gap queda nombrado con precisión (Lema Faltante 5.3).

**VEREDICTO: PARCIAL** (§6). La sub-pregunta decisiva de P41 tiene respuesta afirmativa
— sí existe un producto natural con superaditividad estricta del índice negativo, y el
cálculo es incondicional — pero la cota sublineal (b) es estructuralmente inaccesible
para ese producto sin salir de la clase de funciones L, y las realizaciones analíticas
disponibles, o bien son aditivas exactas (suma directa / multiplicación de funciones L),
o bien colapsan a CAP (convolución), o bien requieren el programa CC inconcluso
(cuadrado del sitio de escala). Queda un enunciado falsable preciso (Problema 6.2).

---

## 1. Axiomatización: el teorema de amplificación abstracto

### 1.1 Qué hay exactamente en Weil I

Recordamos el esqueleto lógico de la prueba de Deligne de RH sobre cuerpos de funciones
[Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974), 273–307], en la forma
ya destilada en P41 §7:

1. **Invariante entero.** Para un autovalor de Frobenius $\alpha$ de un haz $\ell$-ádico
   de peso $w$ sobre una curva, el "defecto de peso" es $\delta = 2\log_q|\alpha| - w$.
   RH (para ese haz) es $\delta = 0$. El dato crucial: $\delta$ vive en un conjunto
   discreto controlado (de hecho, el argumento final lo fuerza a un intervalo
   $[0, c/k]$ para todo $k$, y la única posibilidad es $0$; la versión categórica limpia
   usa que el invariante relevante es un entero o un real atrapado por enteros).

2. **Amplificación.** La potencia tensorial (par) $\mathcal{F}^{\otimes 2k}$ tiene
   autovalor $\alpha^{2k}$: el defecto se multiplica, $\delta \mapsto 2k\,\delta$.

3. **Cota uniforme sublineal.** La racionalidad de Grothendieck de la función L de la
   familia, $L(U, \mathcal{F}^{\otimes 2k}, T) = \prod P_i(T)^{(-1)^{i+1}}$, junto con la
   convergencia absoluta del producto de Euler en un semiplano fijo y el control de los
   polos (que provienen de $H^2_c$, cuyo peso se conoce **a priori** y **no depende de
   $k$** más que linealmente con constante aditiva uniforme), da
   $2k\,\delta \leq C$ con $C$ **independiente de $k$** (o $\leq C(k)$ con $C(k)/k\to0$).
   El punto estructural: la cota proviene de un input **independiente** del autovalor
   $\alpha$ — la geometría de la curva y la teoría de pesos de los $H^i_c$, que "no se
   mueven" al variar $k$.

4. **Conclusión.** $2k\,\delta \leq C$ para todo $k \geq 1$ fuerza $\delta \leq C/2k \to 0$,
   luego $\delta = 0$.

Ninguno de los cuatro pasos es una positividad tipo CAP: no hay forma cuadrática cuya
no-negatividad equivalga a RH en ningún punto del argumento. El paso (3) es el corazón
no trivial; (1), (2), (4) son estructura.

### 1.2 La estructura categórica mínima

**Definición 1.1 (Dato de amplificación).** Un **dato de amplificación** es una cuádrupla
$(\mathcal{C}, \boxtimes, \kappa, \mathcal{F})$ donde:

- $\mathcal{C}$ es una clase de objetos (no se requiere categoría tensorial simétrica
  completa; basta una clase cerrada bajo la operación que sigue);
- $\boxtimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ es una operación binaria
  (no se requiere asociatividad estricta; basta que las potencias $\psi^{\boxtimes k}$
  estén definidas de forma coherente, p.ej. por iteración a izquierda);
- $\kappa : \mathcal{C} \to \mathbb{N} \cup \{\infty\}$ es un invariante con valores
  enteros no negativos (o $+\infty$);
- $\mathcal{F} \subseteq \mathcal{C}$ es una subclase ("la familia acotada").

**Definición 1.2 (Propiedades (a) y (b)).** El dato de amplificación satisface:

- **(a) Superaditividad a lo largo de potencias** si para todo $\psi \in \mathcal{C}$ y
  todo $k \geq 1$:
  $$\kappa(\psi^{\boxtimes k}) \;\geq\; k\,\kappa(\psi).$$
  (Nótese: esto es más débil que la superaditividad binaria
  $\kappa(\psi_1\boxtimes\psi_2) \geq \kappa(\psi_1)+\kappa(\psi_2)$, que la implica por
  inducción. Para el teorema basta la versión a lo largo de potencias.)

- **(b) Cota uniforme sublineal sobre $\mathcal{F}$** si existe $f : \mathbb{N} \to
  [0,\infty)$ con $f(k)/k \to 0$ tal que para todo $\psi$ con $\psi^{\boxtimes k} \in
  \mathcal{F}$ para todo $k$:
  $$\kappa(\psi^{\boxtimes k}) \;\leq\; f(k) \quad \text{para todo } k \geq 1.$$

**Observación 1.3 (qué es esencial y qué no).** No se necesita: unidad, dualidad,
rigidez, trenzado, ni siquiera funtorialidad de $\boxtimes$ en morfismos. Se necesita
exactamente: (i) que $\kappa$ tome valores en un conjunto con la propiedad arquimediana
discreta ($\mathbb{N}$, o cualquier subconjunto de $[0,\infty)$ con ínfimo positivo en
su parte estrictamente positiva), (ii) la desigualdad (a), (iii) la desigualdad (b) con
**la misma** $\boxtimes$-potencia en ambas. La trampa clásica está en (iii): si la
familia $\mathcal{F}$ sobre la que se prueba la cota no contiene las potencias del
objeto de interés, el argumento no arranca.

### 1.3 El teorema abstracto

**Teorema 1.4 (Amplificación abstracta).** Sea $(\mathcal{C}, \boxtimes, \kappa,
\mathcal{F})$ un dato de amplificación que satisface (a) y (b). Entonces para todo
$\psi \in \mathcal{C}$ tal que $\psi^{\boxtimes k} \in \mathcal{F}$ para todo $k \geq 1$:
$$\kappa(\psi) = 0.$$

*Demostración.* Sea $\psi$ tal. Por (a) y (b), para todo $k \geq 1$:
$$k\,\kappa(\psi) \;\leq\; \kappa(\psi^{\boxtimes k}) \;\leq\; f(k),$$
luego $\kappa(\psi) \leq f(k)/k$ para todo $k$. Tomando $k \to \infty$ y usando
$f(k)/k \to 0$: $\kappa(\psi) \leq 0$. Como $\kappa(\psi) \in \mathbb{N} \cup \{\infty\}$,
se concluye $\kappa(\psi) = 0$. $\square$

**Corolario 1.5 (Instanciación RH).** Si existe un dato de amplificación con
$\mathcal{C} \ni \psi_\zeta$ (el objeto cuyo $\kappa$ es el índice negativo de la forma
de Weil, $\kappa(\psi_\zeta) = \kappa(Q) = 2m$ bajo Hipótesis D, por P35 y Doc 96
Teorema 8.1), con (a), (b), y $\psi_\zeta^{\boxtimes k} \in \mathcal{F}$ para todo $k$,
entonces $2m = 0$, i.e. RH.

**Observación 1.6 (dónde puede esconderse la circularidad).** El Teorema 1.4 es
elemental; toda la sustancia está en exhibir el dato. Los tres puntos de fuga posibles:

- **(C1)** $\kappa$ no es calculable / la igualdad $\kappa(\psi_\zeta) = 2m$ ya supone
  estructura condicional (en nuestro caso: Hipótesis D más el programa V.1–V.4 de P35 —
  asumido como marco de trabajo en todo este documento, igual que en P41).
- **(C2)** (a) se prueba solo usando información sobre los ceros (circular).
- **(C3)** (b) se prueba solo asumiendo una positividad RH-equivalente para la familia
  (el colapso CAP esperado: ver §4).

El discriminador del programa (I2a: ¿existe input independiente incondicional que haga
el trabajo?) debe aplicarse por separado a (a) y a (b) en cada candidato. Esa es la
disciplina de §3 y §4.

---

## 2. El objeto a amplificar: estructura de $(\mathcal{K}, Q)$ y de $\mathcal{K}_{\mathrm{off}}$

Fijamos el marco de P35 + Doc 96 + Doc 98, que es el marco de la Forma B:

- $(\mathcal{K}, Q)$: espacio de Pontryagin de Weil–Connes; $Q(f,g) =
  \mathcal{W}(f \star \tilde g)$ la forma de Weil; $H_C = -ix\partial_x$ el operador de
  escala, $Q$-simétrico módulo V.1.
- Bajo Hipótesis D con $m$ órbitas de Klein de ceros off-críticos:
  $\kappa(Q) = \mathrm{neg.ind}(H_C) = 2m$ (P35, Conjetura puente, asumida como marco;
  la desigualdad $\leq$ es incondicional vía Kreĭn–Langer).
- **Localización** (Doc 96, Teorema 8.1): $\mathcal{K} = \mathcal{K}_{\mathrm{crit}}
  \oplus_Q \mathcal{K}_{\mathrm{off}}$, con $Q|_{\mathcal{K}_{\mathrm{crit}}} \geq 0$ y
  $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = \kappa = 2m$.
- **Estructura fina de $\mathcal{K}_{\mathrm{off}}$** (Doc 98, Proposición 6.1, caso
  $m=1$, extendido a $m$ cuádruplos por ortogonalidad espectral): cada cuádruplo
  $\{1/2 \pm b_j \pm i\gamma_j\}$ genera un bloque de dimensión 4 con matriz de Gram
  igual a **dos planos hiperbólicos**: signatura $(2,2)$, $\kappa = 2$ por cuádruplo,
  independiente de $b_j$. En total:
  $$\dim \mathcal{K}_{\mathrm{off}} = 4m, \qquad
    \mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}}) = (2m,\, 2m), \qquad
    \kappa = 2m.$$
- La parte positiva del espacio completo es de dimensión infinita:
  $\mathrm{sig}(Q) = (\infty,\, 2m)$ en el sentido de que $p = \dim\mathcal{K}_+ = \infty$,
  $q = \dim\mathcal{K}_- = 2m$.

Los autovalores de $H_C$ sobre $\mathcal{K}_{\mathrm{off}}$ son $z_j^{(\pm\pm)} =
\pm b_j \pm i\gamma_j$ (parámetro $z = \rho - 1/2$, cuatro por cuádruplo, apareados en
los dos planos hiperbólicos por $z \leftrightarrow \bar z$; convención del Doc 98,
Obs. 6.2).

Este es el objeto $\psi_\zeta$ del Corolario 1.5. La pregunta de este documento:
¿qué $\boxtimes$?

---

## 3. Inventario de candidatos

### 3.1 Candidato 1: producto tensorial de espacios de Krein

#### 3.1.1 El cálculo de signaturas

**Proposición 3.1 (signatura del producto tensorial de formas hermitianas).** Sean
$(V_1, Q_1)$ y $(V_2, Q_2)$ espacios vectoriales complejos de dimensión finita con
formas hermitianas no degeneradas de signaturas $(p_1, q_1)$ y $(p_2, q_2)$. Entonces la
forma hermitiana $Q_1 \otimes Q_2$ sobre $V_1 \otimes V_2$, definida por
$(Q_1 \otimes Q_2)(u_1 \otimes u_2,\, v_1 \otimes v_2) = Q_1(u_1, v_1)\,Q_2(u_2, v_2)$
y extensión sesquilineal, es no degenerada de signatura
$$\mathrm{sig}(Q_1 \otimes Q_2) = \bigl(\,p_1 p_2 + q_1 q_2,\;\; p_1 q_2 + q_1 p_2\,\bigr).$$
En particular:
$$\boxed{\;\mathrm{neg.ind}(Q_1 \otimes Q_2) \;=\; p_1 q_2 + q_1 p_2.\;}$$

*Demostración.* Elíjanse bases $Q_i$-ortonormales $\{e^{(i)}_a\}$ de $V_i$ con
$Q_i(e^{(i)}_a, e^{(i)}_a) = \varepsilon^{(i)}_a \in \{+1, -1\}$ (existen por el teorema
de inercia de Sylvester, válido para formas hermitianas complejas). La base
$\{e^{(1)}_a \otimes e^{(2)}_b\}$ de $V_1 \otimes V_2$ es
$(Q_1\otimes Q_2)$-ortogonal con
$$(Q_1 \otimes Q_2)(e^{(1)}_a \otimes e^{(2)}_b,\, e^{(1)}_a \otimes e^{(2)}_b)
  = \varepsilon^{(1)}_a\,\varepsilon^{(2)}_b.$$
El signo es $-1$ exactamente cuando los signos de los factores difieren. El número de
pares $(a,b)$ con signos distintos es $p_1 q_2 + q_1 p_2$; con signos iguales,
$p_1 p_2 + q_1 q_2$. La no-degeneración es inmediata (ningún vector de la base es
isótropo y la base es ortogonal). $\square$

**Corolario 3.2 (superaditividad estricta).** Con la notación anterior, escribiendo
$\kappa_i = q_i$:
$$\mathrm{neg.ind}(Q_1 \otimes Q_2) - (\kappa_1 + \kappa_2)
  = p_1 q_2 + q_1 p_2 - q_1 - q_2
  = (p_1 - 1)\,q_2 + (p_2 - 1)\,q_1 \;\geq\; 0,$$
con **desigualdad estricta** si y solo si $(p_1-1)q_2 + (p_2-1)q_1 > 0$, i.e. en cuanto
algún factor tenga a la vez parte positiva de dimensión $\geq 2$ y el otro factor tenga
índice negativo $\geq 1$.

*Demostración.* Cálculo directo desde la Proposición 3.1. $\square$

**Esto refuta el falsador de P41 en su primera mitad**: no es cierto que κ sea
exactamente aditivo bajo todo producto disponible. El producto tensorial de Krein es
estrictamente superaditivo en cuanto hay direcciones positivas de sobra — que es
exactamente la situación de $(\mathcal{K}, Q)$, con $p = \infty$.

#### 3.1.2 Potencias tensoriales: crecimiento exacto

**Proposición 3.3 (índice negativo de la potencia tensorial).** Para $(V, Q)$ de
signatura $(p, q)$, la potencia $k$-ésima tiene
$$\mathrm{neg.ind}(Q^{\otimes k})
  = \sum_{j \,\mathrm{impar}} \binom{k}{j} p^{\,k-j} q^{\,j}
  = \frac{(p+q)^k - (p-q)^k}{2}.$$

*Demostración.* En la base producto, el signo de un vector básico es el producto de los
signos de sus $k$ factores; es negativo cuando el número $j$ de factores negativos es
impar. La forma cerrada se obtiene de $(p+q)^k = \sum_j \binom{k}{j} p^{k-j} q^j$ y
$(p-q)^k = \sum_j (-1)^j \binom{k}{j} p^{k-j} q^j$. $\square$

Dos lecturas:

- **Si $q = 0$**: $\mathrm{neg.ind}(Q^{\otimes k}) = 0$ para todo $k$. La positividad es
  estable bajo ⊗ (consistencia: bajo RH no se genera nada).
- **Si $q \geq 1$ y $p \geq 1$**: el índice crece como $\tfrac12(p+q)^k$ —
  **exponencialmente**, mucho más que la amplificación lineal $k\kappa$ que pide (a).

#### 3.1.3 El problema de dimensión infinita

**Proposición 3.4 (colapso de la estructura de Pontryagin).** Si $(\mathcal{K}, Q)$ tiene
$p = \dim \mathcal{K}_+ = \infty$ y $q = \kappa \geq 1$, entonces toda completación
razonable de $(\mathcal{K} \otimes \mathcal{K},\, Q \otimes Q)$ tiene índice negativo
infinito.

*Demostración.* Sea $v_- \in \mathcal{K}_-$ con $Q(v_-, v_-) = -1$ y sea
$\{e_n\}_{n\geq1} \subset \mathcal{K}_+$ ortonormal ($Q(e_n,e_n)=+1$). Los vectores
$\{e_n \otimes v_-\}_{n \geq 1}$ son mutuamente $Q\otimes Q$-ortogonales con
$(Q\otimes Q)(e_n \otimes v_-, e_n \otimes v_-) = -1$: un subespacio negativo de
dimensión infinita. $\square$

**Consecuencia.** $(\mathcal{K}^{\otimes 2}, Q^{\otimes 2})$ **no es un espacio de
Pontryagin**: $\kappa = \infty$, el teorema de Kreĭn–Langer no aplica, y el invariante
$\kappa$ deja de ser un entero útil ya en la primera potencia. Tomado ingenuamente, el
Candidato 1 muere aquí — no por falta de superaditividad sino por exceso: la
amplificación es tan violenta que destruye el invariante.

**Opciones de regularización:**

- **(R1) Índice relativo:** definir $\kappa_{\mathrm{rel}}(Q^{\otimes 2}) :=
  \mathrm{neg.ind}(Q^{\otimes 2}) - \mathrm{neg.ind}(Q_{\mathrm{ref}}^{\otimes 2})$
  respecto de una forma de referencia $Q_{\mathrm{ref}} \geq 0$ (p.ej. la forma de Weil
  de $\zeta_{\mathrm{on}}$, Doc 83). Problema: ambos términos son $\infty$; haría falta
  una teoría de índice relativo tipo Fredholm para pares de formas (perturbación de
  rango finito: $Q - Q_{\mathrm{ref}}$ tiene "rango" $4m$ en el sentido del Doc 98). Es
  desarrollable pero, nótese, el resultado de cualquier definición consistente será el
  índice de la parte de rango finito — i.e. la opción (R2). **No es una ruta
  independiente.**
- **(R2) Restricción a $\mathcal{K}_{\mathrm{off}}$:** legítima e invariantemente
  definida por el Teorema 8.1 del Doc 96 (la descomposición es espectral, no una
  elección). Es el Candidato 2.

**Evaluación Candidato 1: (a) ✅ estricta (Corolario 3.2) — (b) ✗ catastróficamente
falsa ($\kappa = \infty$ en $k=2$). Estado: redirige a Candidato 2.**

### 3.2 Candidato 2: el tensor relativo sobre $\mathcal{K}_{\mathrm{off}}$

#### 3.2.1 El cálculo

Por §2, $\mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}}) = (2m, 2m)$ (suma de $2m$ planos
hiperbólicos). Por la Proposición 3.3 con $p = q = 2m$:

**Proposición 3.5.** $\mathrm{neg.ind}\bigl((Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes k}\bigr)
= \tfrac{(4m)^k - 0^k}{2} = \tfrac{(4m)^k}{2}$ para $k \geq 1$.

La amplificación (a) se cumple con holgura exponencial:
$\tfrac{(4m)^k}{2} \geq k \cdot 2m$ para todo $k \geq 1$, $m \geq 1$. **El ingrediente
(a) del esqueleto de Deligne está disponible, incondicionalmente, como pura álgebra
lineal.** Y si $m = 0$, todas las potencias tienen índice 0: el invariante distingue
exactamente RH de ¬RH en cada nivel $k$.

#### 3.2.2 El lema de esterilidad

Aquí está el punto conceptual más importante del documento.

**Proposición 3.6 (esterilidad del tensor abstracto).** Sea $\mathcal{C}_0$ la clase de
espacios hermitianos de dimensión finita con $\boxtimes = \otimes$ y $\kappa =
\mathrm{neg.ind}$. Entonces **no existe** ninguna función $f$ con $f(k)/k \to 0$ tal que
(b) valga sobre una familia $\mathcal{F}$ que contenga las potencias de algún objeto con
$\kappa \geq 1$. En otras palabras: dentro de $\mathcal{C}_0$, (a) y (b) son
**conjuntamente insatisfacibles** salvo en el caso trivial $\kappa = 0$.

*Demostración.* Por la Proposición 3.3, si $\kappa(\psi) = q \geq 1$ (y $p \geq 0$),
entonces $\kappa(\psi^{\otimes k}) = \tfrac{(p+q)^k - (p-q)^k}{2} \geq
\tfrac{(q+p)^k - |p-q|^k}{2} \to \infty$ con crecimiento exponencial (si $p\geq1$) o
$\kappa(\psi^{\otimes k}) = q^k/2 \cdot [1-(-1)^k]$... en todo caso
$\limsup_k \kappa(\psi^{\otimes k})/k = \infty$ para $q \geq 1$, $p+q \geq 2$, y para
$p=0,q=1$ se tiene $\kappa(\psi^{\otimes k}) = \tfrac{1-(-1)^k}{2}$, que es acotada pero
entonces (a) falla ($k\kappa = k \not\leq 1$). En ningún caso coexisten (a) y (b) con
$\kappa \geq 1$. $\square$

**Observación 3.7 (lectura estructural).** La Proposición 3.6 no es una mala noticia
accidental: es la manifestación precisa de que en el tensor abstracto **los dos lados de
la desigualdad del Teorema 1.4 se calculan con los mismos datos** (la signatura). No hay
de dónde sacar una contradicción, porque no hay dos fuentes de información que puedan
discrepar. En Weil I, (a) es álgebra lineal (autovalores de potencias tensoriales) pero
(b) es **geometría** (racionalidad de la L de la familia, pesos de $H^2_c$): dos fuentes
independientes. La conclusión operativa:

> **El candidato 2 solo puede funcionar si las potencias $\psi^{\boxtimes k}$ se
> re-encarnan en objetos analíticos cuya finitud de índice tenga una fuente propia
> (tipo C5), independiente del cálculo de signaturas.**

Esto transfiere todo el problema a la pregunta: ¿qué objeto analítico es
$\mathcal{K}_{\mathrm{off}} \otimes \mathcal{K}_{\mathrm{off}}$?

#### 3.2.3 El objeto analítico del producto: ceros que se suman

Los generadores de $\mathcal{K}_{\mathrm{off}}$ están rígidamente indexados por los
ceros off-críticos (Doc 98, Obs. 6.3): $v_z$ con autovalor $z = \rho - 1/2$ de $H_C$.
Sobre $\mathcal{K}_{\mathrm{off}} \otimes \mathcal{K}_{\mathrm{off}}$ el operador
natural es
$$H^{(2)} \;=\; H_C \otimes I + I \otimes H_C,$$
(el generador del flujo de escala diagonal $U_\lambda \otimes U_\lambda$), con
autovalores $z_1 + z_2$ sobre $v_{z_1} \otimes v_{z_2}$. En parámetro $s$: los "ceros"
del objeto producto son
$$s = \rho_1 + \rho_2 - \tfrac12, \qquad \rho_1, \rho_2 \text{ ceros de } \zeta.$$

**Pregunta 3.8.** ¿Qué función L tiene ceros en $\{\rho_1 + \rho_2 - 1/2\}$?

**Respuesta (negativa, con tres comparaciones):**

1. **Rankin–Selberg en GL(1).** La convolución RS de caracteres de Hecke es grupal:
   $L(s, \chi_1 \times \chi_2) = L(s, \chi_1\chi_2)$. Para el objeto $\zeta$
   ($\chi = \mathbf{1}$): $L(s, \mathbf{1} \times \mathbf{1}) = \zeta(s)$. Los ceros del
   RS de $\zeta$ consigo misma son **los ceros de $\zeta$**, no sus sumas. Esta es la
   trivialidad grupal señalada en P41 §7.3, ahora vista del lado analítico: RS es el
   realizador analítico del producto tensorial de **representaciones automorfas**
   (Jacquet–Shalika, etc.), y en GL(1) ese tensor es el producto de caracteres — la
   capa de "ceros" no se tensoriza, se queda quieta.

2. **$\zeta(s)^k$.** Tiene los ceros de $\zeta$ **con multiplicidad $k$**: eso es
   amplificación de multiplicidad, no suma de parámetros. En el lado $(\mathcal{K},Q)$
   corresponde a la **suma directa** $\mathcal{K}_{\mathrm{off}}^{\oplus k}$
   ($\kappa \mapsto k\kappa$, aditividad exacta: Candidato 5). Importante: $\zeta^k$ sí
   es "amplificación real de multiplicidad" en el sentido de la tarea (iii), con
   crecimiento lineal del índice — retomado en §5.

3. **Sumas de ceros en la literatura.** Las combinaciones $\rho_1 + \rho_2$ aparecen en
   los productos de Hadamard de $\Xi(t_1)\Xi(t_2)$ y en el estudio de
   $\zeta(s)\zeta(s+w)$ (momentos desplazados), pero **ninguna función de una variable
   con producto de Euler conocida** tiene divisor de ceros $\{\rho_1+\rho_2-1/2\}$. No
   afirmamos un teorema de no-existencia (no lo tenemos); registramos que el objeto no
   está en la clase de Selberg ampliada por ninguna construcción conocida.
   **[GAP ABIERTO 3.8: no hay realizador analítico conocido; tampoco hay prueba de que
   no exista.]**

#### 3.2.4 La dicotomía multiplicar/sumar

**Observación 3.9 (dicotomía estructural).** Sea $\boxtimes$ cualquier operación sobre
objetos $\psi_L$ asociados a funciones L tal que el objeto $\psi_{L_1} \boxtimes
\psi_{L_2}$ vuelva a ser el objeto de una función L, digamos $L_3$, construida por
procedimientos de la teoría (productos, cocientes, RS, inducción automorfa, cambio de
base). Entonces el conjunto de ceros de $L_3$ (con multiplicidad) es una **unión** de
conjuntos de ceros de funciones L individuales — nunca una **suma de Minkowski** de los
conjuntos de parámetros espectrales. En el diccionario de $(\mathcal{K},Q)$: las
operaciones internas a la clase de funciones L realizan sumas directas (y sus
sub/cocientes), nunca el tensor $H_C \otimes I + I \otimes H_C$.

*Justificación.* Toda función L de la clase es producto de Euler con factor arquimediano
gamma; su divisor de ceros proviene de su propia ecuación funcional. Las construcciones
listadas operan a nivel de representaciones/factores de Euler, y el divisor del
resultado es el divisor de una función de **una** variable $s$; los ceros de un producto
$\prod_i L_i^{n_i}$ son la unión con multiplicidad. La suma de Minkowski
$\{\rho_1+\rho_2-1/2\}$ requeriría una operación bilineal a nivel de **divisores**, no
de funciones — un "producto aditivo de espectros" que la teoría de funciones L no
provee. $\square$ (estructural, no un teorema formal: depende de la lista de
construcciones admitidas)

**Consecuencia.** El Candidato 2 enfrenta una bifurcación exacta:

- O bien $\boxtimes$ permanece en la clase de funciones L $\Rightarrow$ suma directa
  $\Rightarrow$ κ aditivo exacto $\Rightarrow$ la mitad (a)-estricta del falsador de P41
  se activa (no hay superaditividad estricta dentro de la clase);
- o bien $\boxtimes$ es el tensor genuino $\Rightarrow$ (a) estricta y exponencial,
  pero el objeto producto sale de la clase de funciones L y **pierde el único mecanismo
  conocido de finitud tipo C5** (Doc 94: C5 se formula para la forma de Weil de una
  función L vía la cola prima de **su** fórmula explícita; sin fórmula explícita, no hay
  C5).

**Evaluación Candidato 2: (a) ✅ estricta, exponencial, incondicional — (b) GAP ABIERTO
total: sin realizador analítico no hay fuente de cota. Es el candidato más prometedor y
su gap está nombrado en §5.**

### 3.3 Candidato 3: correspondencias de Frobenius del sitio de escala

#### 3.3.1 Hechos verificados

Del corpus Connes–Consani, verificado contra las fuentes públicas
([The Arithmetic Site, arXiv:1405.4527](https://arxiv.org/pdf/1405.4527);
[CRAS 352 (2014) 971–975](https://alainconnes.org/wp-content/uploads/The-arithmetic-site-2014.pdf);
[The Scaling Site, arXiv:1507.05818](https://arxiv.org/pdf/1507.05818);
[Geometry of the scaling site, arXiv:1603.03191](https://arxiv.org/pdf/1603.03191);
[Connes, An essay on the Riemann Hypothesis, arXiv:1509.05576](https://arxiv.org/pdf/1509.05576)):

- El **sitio aritmético** es $(\widehat{\mathbb{N}^\times},\, \mathbb{Z}_{\max})$ con
  $\mathbb{N}^\times$ actuando por endomorfismos de Frobenius sobre el semianillo
  $\mathbb{Z}_{\max} = (\mathbb{Z}\cup\{-\infty\}, \max, +)$ de característica 1.
- El **sitio de escala** se obtiene por extensión de escalares al semicuerpo tropical
  $\mathbb{R}_{\max}^+$; sus puntos sobre $\mathbb{R}_{\max}^+$ dan el cociente
  $[0,\infty) \rtimes \mathbb{R}_+^*$ relacionado con el espacio de clases de adeles.
- Las **correspondencias de Frobenius** $\Psi(\lambda)$, $\lambda \in \mathbb{R}_+^*$,
  se construyen para $\lambda = n/m$ racional componiendo con $Fr_{n,m}$, y para
  $\lambda$ irracional por aproximación diofántica (curvas en el cuadrado del sitio).
- **Ley de composición** (verificada): $\Psi(\lambda) \circ \Psi(\lambda') =
  \Psi(\lambda\lambda')$ cuando $\lambda\lambda' \notin \mathbb{Q}$, y también cuando
  ambos son racionales; en el caso mixto ($\lambda, \lambda' \notin \mathbb{Q}$,
  $\lambda\lambda' \in \mathbb{Q}$) aparece la **deformación tangencial**:
  $\Psi(\lambda) \circ \Psi(\lambda') = \Psi(\lambda\lambda') \circ \mathrm{Id}_\varepsilon$,
  donde $\mathrm{Id}_\varepsilon$ es la deformación tangencial de la identidad.
- La estructura de **λ-anillo** del semianillo de correspondencias, y la analogía con
  los Frobenius en característica $p$, es la motivación declarada de la estrategia
  Riemann–Roch de CC. Los detalles de la estructura de λ-anillo más allá de la ley de
  composición anterior: **[NO VERIFICADO en detalle; no se usan más abajo].**

#### 3.3.2 Acción sobre $(\mathcal{K}, Q)$ y el índice

El puente con nuestro marco: la acción de escala $U_\lambda$ sobre $L^2(C_\mathbb{Q})$
**es** la sombra hilbertiana del Frobenius $\Psi(\lambda)$ (es la acción de
$\mathbb{R}_+^*$ cuyo generador es $H_C$; P35 §3).

**Proposición 3.10 (los Frobenius no amplifican κ).** Supóngase V.1 (invariancia de
escala de la forma de Weil: $Q(U_\lambda f, U_\lambda g) = Q(f,g)$; Objetivo V.1 de P35,
abierto). Entonces cada $U_\lambda$ es una $Q$-isometría de $(\mathcal{K},Q)$, y para
todo subespacio $V \subseteq \mathcal{K}$:
$$\mathrm{neg.ind}(Q|_{U_\lambda V}) = \mathrm{neg.ind}(Q|_V).$$
En particular $\kappa(U_\lambda \psi) = \kappa(\psi)$: las correspondencias de Frobenius
inducen sobre $(\mathcal{K},Q)$ **isometrías**, que preservan el índice negativo
exactamente. No hay $\mu$ con comportamiento no trivial sobre κ.

*Demostración.* Una isometría lineal biyectiva transporta subespacios negativos en
subespacios negativos de la misma dimensión, en ambas direcciones. $\square$

**Observación 3.11 (por qué era esperable, y qué queda).** Las $\Psi(\lambda)$ forman un
**monoide a un parámetro de endomorfismos**: son la análoga del Frobenius
$\mathrm{Fr}^k$, no del producto tensorial $\mathcal{F}^{\otimes k}$. En Weil I el
Frobenius tampoco amplifica el defecto: lo *mide*. Quien amplifica es ⊗. Confundir los
dos papeles sería un error de tipo. Lo que las correspondencias sí ofrecen es la
estructura sobre la cual un ⊠ binario podría definirse geométricamente: el **cuadrado
del sitio** (aritmético o de escala), donde las $\Psi(\lambda)$ viven como
correspondencias (subobjetos del cuadrado) y donde CC desarrollan los polígonos de
Newton con sus dos operaciones (envolvente convexa de la unión = suma tropical; suma de
Minkowski = producto tropical). Nótese el eco exacto de la dicotomía de la Observación
3.9: **unión vs. suma de Minkowski** — la geometría tropical del cuadrado del sitio es
el único lugar del corpus verificado donde la operación "suma de Minkowski de divisores"
existe como estructura nativa. Si el tensor genuino del Candidato 2 tiene un realizador
geométrico, está aquí. Pero el aparato cohomológico (Riemann–Roch sobre el cuadrado,
teoría de divisores con índices y la fórmula esperada tipo $\dim H^0 - \dim H^1 =
\deg + \ldots$) es exactamente el programa CC inconcluso = **MW-5**.

**Evaluación Candidato 3: como operación sobre $(\mathcal{K},Q)$: (a) ✗ (isometrías,
κ exactamente invariante — ni siquiera aditivo: no es operación binaria). Como
proveedor de geometría para el Candidato 2: la única pista estructural viva, bloqueada
por MW-5.**

### 3.4 Candidato 4: convolución multiplicativa sobre el grupo de clases de ideles

La operación natural del lado de funciones de prueba: $(f_1 \star f_2)(x) =
\int_0^\infty f_1(y) f_2(x/y)\, dy/y$ (y su versión adélica sobre $C_\mathbb{Q}$). Hace
de $\mathcal{S}$ un álgebra conmutativa con involución $f \mapsto \tilde f$, y la forma
de Weil es el funcional $\tau = \mathcal{W}$ evaluado en el álgebra:
$Q(f,g) = \tau(f \star \tilde g)$.

**Proposición 3.12 (qué hace ⋆ con la forma).** En el lado de Mellin,
$\widehat{f_1 \star f_2}(s) = \hat f_1(s)\,\hat f_2(s)$. Por tanto:
$$Q(f_1 \star f_2,\, f_1 \star f_2) = \mathcal{Z}[f_1\star f_2] - \mathcal{P}[\cdot] +
\mathcal{A}[\cdot], \qquad
\mathcal{Z}[f_1 \star f_2] = \sum_\rho |\hat f_1(\rho)|^2\,|\hat f_2(\rho)|^2.$$
Los ceros que pesan son **los mismos ceros de $\zeta$**, re-ponderados
multiplicativamente. No hay amplificación de ceros ni de multiplicidades: la operación
es interna al objeto $\zeta$, diagonal en el espectro.

**Proposición 3.13 (relación con κ: nula como amplificador, exacta como módulo).** Para
$h$ fija con $\hat h(\rho_j) \neq 0$ en los $4m$ ceros off-críticos, el mapa
$f \mapsto f \star h$ preserva $\mathcal{K}_{\mathrm{off}}$ (escala los residuos $v_z$
por $\hat h(1/2+z)$) y los bloques hiperbólicos del Doc 98 van a bloques hiperbólicos
($q_j \mapsto q_j\, \hat h(1/2+z_j)\overline{\hat h(1/2+\bar z_j)}$, off-diagonales no
nulas): $\kappa$ **no cambia**. Si $\hat h$ se anula en algún cero off-crítico, κ puede
**bajar** (nunca subir). En ningún caso hay superaditividad: $\star$ no combina los
índices de dos argumentos — el índice del producto está acotado por el de cada factor.

*Demostración.* Cálculo directo sobre los generadores $v_z$ ($\widehat{f\star h} =
\hat f \hat h$ multiplica el funcional residual en $z$ por el escalar
$\hat h(1/2+z)$); un bloque $\bigl(\begin{smallmatrix}0&q\\\bar q&0\end{smallmatrix}\bigr)$
con $q \neq 0$ tiene signatura $(1,1)$ para todo $q \neq 0$, y signatura $(0,0)$
(degenera) si $q = 0$. $\square$

**Aplicación del discriminador.** ¿Qué enunciado habría que probar para extraer RH de
$\star$? El único disponible: "$\tau$ es un funcional positivo sobre el álgebra
involutiva $(\mathcal{S}, \star, \tilde{\ })$", i.e. $\tau(f \star \tilde f) \geq 0$
para todo $f$. Eso **es** la positividad de Weil, carácter por carácter: MW-1. El patrón
de transmutación del Doc 99 aplica en su forma pura: la estructura algebraica nueva
(el álgebra de convolución, los estados GNS, las C*-completaciones) no debilita el
enunciado; lo reformula. La hipótesis estructural que haría funcionar el candidato es
CAP disfrazado. **FAIL I2a.**

**Evaluación Candidato 4: (a) ✗ (sub-multiplicativo en κ, no superaditivo) — y el
único uso posible colapsa a CAP. CERRADO.**

### 3.5 Candidato 5: suma directa (base de comparación)

$(\mathcal{K}_1 \oplus \mathcal{K}_2,\, Q_1 \oplus Q_2)$:
$\mathrm{neg.ind}(Q_1 \oplus Q_2) = q_1 + q_2$, exactamente aditivo. Realizador
analítico: $L_1 \cdot L_2$ (producto de funciones L; para $\psi_\zeta^{\oplus k}$:
$\zeta^k$, ceros con multiplicidad $k$). Aquí (a) vale con igualdad —
$\kappa(\psi^{\oplus k}) = k\kappa(\psi)$, la "amplificación real de multiplicidad" de
la tarea (iii) — y por tanto **todo el peso cae en (b)**: ¿hay una cota
$\kappa(\psi_{\zeta^k}) \leq f(k)$ sublineal demostrable? Pero $\kappa(\psi_{\zeta^k}) =
k \cdot 2m$ se calcula trivialmente desde $\psi_\zeta$: la "familia" $\{\zeta^k\}$ no
contiene información nueva — sus ceros son los de $\zeta$. Una cota sublineal para la
familia **es** $m = 0$, i.e. RH. Circular por contenido (el mismo fenómeno de
esterilidad de la Proposición 3.6: una sola fuente de datos).

**Evaluación Candidato 5: (a) con igualdad (no estricta), (b) RH-equivalente. Es la
vara de medir: cualquier candidato cuyo análisis lo reduzca a suma directa queda
cerrado.**

---

## 4. Riesgo de colapso: transmutación y discriminador, candidato por candidato

Aplicamos el patrón del Doc 99 (la circularidad no se elimina: se transmuta y reaparece
con su nombre de muro) y el discriminador I2a (FAIL = la hipótesis estructural es
positividad CAP disfrazada).

| Candidato | (a) superaditividad | (b) cota sublineal | ¿Dónde reaparece el muro? | I2a |
|---|---|---|---|---|
| 1. ⊗ Krein pleno | ✅ estricta (Cor. 3.2) | ✗ falsa ($\kappa=\infty$, Prop. 3.4) | dimensión infinita destruye Π_κ (eco de MW-3) | pasa (álgebra lineal incondicional) pero el dato muere |
| 2. ⊗ relativo en $\mathcal{K}_{\mathrm{off}}$ | ✅ exponencial (Prop. 3.5) | GAP: sin realizador analítico no hay fuente C5 | MW-5 (cuadrado del sitio) o MW-7 (sin fórmula explícita propia, la finitud requeriría conocer ceros) | (a) pasa I2a; (b) sin candidato a input |
| 3. Frobenius $\Psi(\lambda)$ | ✗ (isometrías, Prop. 3.10) | n/a | el papel de Frobenius es medir, no amplificar | n/a |
| 4. convolución ⋆ | ✗ (Prop. 3.13) | n/a | MW-1 directo: positividad del funcional τ = Weil | **FAIL I2a** |
| 5. suma directa | igualdad exacta | RH-equivalente | esterilidad: una sola fuente de datos | FAIL (circular por contenido) |

**El colapso esperado, documentado con precisión (tarea iv).** La sospecha declarada en
la tarea era: "si la cota sublineal (b) resulta equivalente a una positividad de Weil
generalizada (GRH para la familia Rankin–Selberg), documentarlo". El análisis muestra
algo más fino:

1. Para la familia RS genuina no hay nada que documentar **porque la familia RS de
   $\zeta$ es $\zeta$ misma** (trivialidad grupal de GL(1), §3.2.3.1). El colapso
   "(b) = GRH de la familia RS" no puede ni siquiera formularse: la familia no existe
   como objeto distinto. Este es el modo de muerte específico de GL(1), distinto del
   colapso CAP: no circularidad, sino **vacuidad**.
2. Para el tensor genuino (Candidato 2), (b) no es equivalente a una positividad
   conocida: es **inexpresable** con las herramientas actuales, porque el objeto
   $\psi^{\boxtimes k}$ no tiene fórmula explícita propia. Si algún día la tiene (vía
   cuadrado del sitio de escala), habrá que pasar esa fórmula por el discriminador: el
   riesgo concreto es que la "racionalidad" que se pruebe contenga, escondida en sus
   polos, la posición de los ceros de $\zeta$ (re-encodeo MW-7).
3. Para la convolución (Candidato 4) el colapso es CAP puro y simple, ya documentado.

Comparación con el único mecanismo no-CAP del corpus (Doc 102, amplificador de Bagchi):
Bagchi amplifica por **recurrencia ergódica** (un cero off-crítico → $\gg T$ ceros) y
choca contra $N(\sigma,T) = o(T)$, que es un techo incondicional con fuente
independiente (Carlson/Ingham). Su premisa (SR) es RH-equivalente: FAIL I2b. El
candidato 2 tiene la estructura especular: su "premisa" (a) es incondicional (¡mejor
que Bagchi!), pero su **techo** (b) no existe todavía. Bagchi tiene techo sin premisa;
el tensor relativo tiene premisa sin techo. Esta complementariedad exacta es el
resultado comparativo central del documento.

---

## 5. El candidato más prometedor: especificación del gap

El superviviente es el **Candidato 2** (tensor relativo sobre
$\mathcal{K}_{\mathrm{off}}$), eventualmente realizado geométricamente vía el cuadrado
del sitio de escala (Candidato 3 como infraestructura). Especificamos qué habría que
probar, con el peso ya distribuido por el análisis anterior.

### 5.1 Lo que ya está probado (lado (a))

**Teorema 5.1 (resumen de (a); incondicional módulo el marco P35/Doc 96/Doc 98).** Bajo
Hipótesis D con $m \geq 1$ órbitas, sea $\psi = (\mathcal{K}_{\mathrm{off}},
Q|_{\mathcal{K}_{\mathrm{off}}})$, de signatura $(2m, 2m)$. Con $\boxtimes = \otimes$ de
espacios hermitianos:
$$\kappa(\psi^{\boxtimes k}) = \frac{(4m)^k}{2} \;\geq\; k \cdot 2m = k\,\kappa(\psi)
  \quad (k \geq 1),$$
con igualdad solo en $k=1$. La superaditividad es estricta para $k \geq 2$ y la
amplificación es exponencial. Además $m = 0 \Rightarrow \kappa(\psi^{\boxtimes k}) = 0\;
\forall k$: el invariante de las potencias detecta RH en cada nivel.

No hay nada que probar aquí: es la Proposición 3.5. (a) **no es el gap.**

### 5.2 El gap exacto (lado (b))

**Lema Faltante 5.2 (realización analítica del cuadrado).** *Construir un objeto
analítico-geométrico $X_2$ (candidato natural: una estructura de tipo "función L de dos
variables colapsada", o un divisor sobre el cuadrado del sitio de escala con su suma de
Minkowski tropical) tal que:*

1. *su "fórmula explícita" propia exprese un funcional $\mathcal{W}_2$ cuya forma
   cuadrática asociada $Q_2$ contenga $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$
   como bloque espectral (los autovalores $z_1 + z_2$ de
   $H_C \otimes I + I \otimes H_C$);*
2. *$\mathcal{W}_2$ tenga un lado "geométrico/aritmético" computable sin conocer las
   posiciones de los ceros de $\zeta$ (el análogo del lado de primos de la fórmula de
   Weil).*

**Lema Faltante 5.3 (finitud C5 para la familia).** *Probar para la familia
$\{X_k\}_{k\geq1}$ (potencias) una cota de tipo C5 (Doc 94): el índice negativo de
$Q_k$ está acotado por la contribución de una "cabeza" finita controlada
uniformemente en $k$,*
$$\kappa(Q_k) \;\leq\; f(k), \qquad f(k)/k \to 0,$$
*donde $f$ proviene de datos que "no se mueven con $k$" — el análogo exacto de "los
polos de la L de la familia no se mueven" de Weil I. Candidato a fuente: una fórmula
tipo Riemann–Roch sobre el cuadrado del sitio de escala, donde $f(k)$ sería una
característica de Euler (dimensión de un $H^0$ menos un $H^1$ tropicales) cuyo
crecimiento en $k$ es geométrico-presupuestado, no espectral.*

**Por qué el peso cae íntegramente en 5.3 y no en 5.2+a.** Si los ceros del objeto
producto incluyeran los de $\zeta$ con multiplicidad $k$ (caso $\zeta^k$ = suma
directa), el índice crece linealmente y (b) sublineal es RH (§3.5): circular. La única
configuración no circular es la del tensor genuino, donde (a) da crecimiento
**exponencial** $\;(4m)^k/2$; entonces (b) ni siquiera necesita ser sublineal — bastaría
$f(k) = o((4m)^k)$ *para algún $m\geq1$ fijo*… pero como $m$ es desconocido, la forma
robusta de la contradicción sigue siendo la sublineal contra $k\kappa$: cualquier
$f(k)/k \to 0$ mata todo $m \geq 1$ de una vez vía $k\cdot 2m \leq \kappa(\psi^{\boxtimes k})
\leq f(k)$... **cuidado**: esta cadena usa (a) en la forma $k\kappa \leq
\kappa(\psi^{\boxtimes k})$ y (b) sobre el mismo objeto. Si $X_k$ realiza el tensor,
entonces bajo ¬RH su índice ES $(4m)^k/2$ (Teorema 5.1), de modo que (b) con cualquier
$f$ subexponencial ya da la contradicción. Es decir: **la fuerza de (a) abarata (b)**
— no se necesita sublineal, basta subexponencial — pero a cambio (b) debe probarse para
un objeto cuya existencia (Lema 5.2) es ella misma el problema. El presupuesto total de
dificultad no baja; se concentra.

**Comparación con la racionalidad de Deligne (tarea iii, respuesta directa).** En Weil I
el análogo de 5.2 es gratuito (la categoría de haces $\ell$-ádicos tiene ⊗ interno y
toda potencia tensorial es de nuevo un haz sobre la misma curva), y 5.3 es la
racionalidad de Grothendieck más la pureza conocida de $H^0, H^2_c$: "los polos no se
mueven" significa que los polos de $L(U, \mathcal{F}^{\otimes 2k}, T)$ están en
$|T| = q^{-1-kw}$ exactamente (coinvariantes de peso conocido), con error aditivo
uniforme en $k$. La maquinaria que lo garantiza es la **finitud cohomológica** (los
$H^i_c$ son de dimensión finita con pesos presupuestados). El análogo conjeturado aquí:
finitud cohomológica tropical sobre el cuadrado del sitio de escala. CC probaron
Riemann–Roch sobre la curva (el sitio de escala mismo, en sus versiones para divisores
sobre $\mathbb{R}_{\max}$-módulos); **el cuadrado está abierto** y es la formulación
precisa de MW-5 en este contexto. No es casual: la prueba de Weil para curvas usa la
intersección en la superficie $C \times C$; CC declaran explícitamente que su estrategia
busca el análogo de $C \times C$ — el cuadrado del sitio — y la positividad
tipo Hodge-index allí. La Forma B aterriza en el mismo cuadrado, pero pidiendo otra
cosa: no positividad (Hodge index = CAP-riesgo), sino **finitud + racionalidad**
(presupuesto de índice). Esta distinción es la contribución específica del documento:

> **Dentro del cuadrado del sitio de escala hay dos teoremas posibles: el de
> positividad (índice de Hodge, la ruta CC declarada, riesgo CAP directo) y el de
> finitud (característica de Euler acotando el índice negativo de la potencia
> tensorial, la ruta Forma B). El segundo no es una positividad: es un conteo. Si el
> aparato cohomológico del cuadrado llega a existir, la Forma B ofrece un consumidor
> alternativo no-CAP del mismo aparato.**

### 5.3 Enunciado falsable

**Problema 5.4 (el experimento decisivo, finito y honesto).** Tómese el modelo de
juguete del Doc 98 ($m = 1$, un cuádruplo, $\mathcal{K}_{\mathrm{off}}$ de dimensión 4,
signatura $(2,2)$). Constrúyase explícitamente el espacio
$\mathcal{K}_{\mathrm{off}}^{\otimes 2}$ (dimensión 16, índice negativo 8 por la
Proposición 3.5) y pregúntese: ¿existe un funcional $\mathcal{W}_2$ sobre funciones de
prueba de **dos** variables $(x_1, x_2) \in (\mathbb{R}_+^*)^2$, construido con datos
aritméticos de $\zeta$ (primos, polo, factor gamma — sin posiciones de ceros), cuya
restricción diagonal reproduzca los 8 bloques negativos? La fórmula explícita de Weil en
dos variables aplicada a $h(x_1, x_2) = f_1(x_1) f_2(x_2)$ factoriza
($\mathcal{W} \otimes \mathcal{W}$), y el término de ceros es
$\sum_{\rho_1, \rho_2} \hat f_1(\rho_1) \hat f_2(\rho_2) \cdot (\ldots)$ — los pares
$(\rho_1, \rho_2)$ aparecen, y la suma $\rho_1 + \rho_2$ aparece si se inserta el núcleo
diagonal $h(x_1, x_2) = g(x_1 x_2)$ (¡la suma de Minkowski de espectros es la
restricción al producto $x_1 x_2$!): en efecto, $\int g(x_1 x_2) x_1^{\rho_1-1}
x_2^{\rho_2-1} dx_1 dx_2 = \hat g(\rho_1 + \rho_2 - 1) \cdot B(\ldots)$ tras el cambio
$u = x_1 x_2$. **Este cálculo de una página — qué funcional bilineal resulta de la
fórmula de Weil doble restringida al núcleo multiplicativo diagonal, y si su lado de
primos es autónomo (sumas $\log p_1 + \log p_2 = \log p_1p_2$: ¡el lado de primos del
producto vive en los enteros $p_1 p_2$, no en primos!)** — es el primer test del Lema
5.2 y es ejecutable con las herramientas del programa. Si el lado "aritmético" del
funcional diagonal resulta expresable en los semigrupos $\{p_1 p_2\}$ (números
casi-primos) con coeficientes computables, el Lema 5.2 tiene un candidato; si el lado
aritmético requiere las posiciones de los ceros para cerrarse, MW-7 reaparece y el
candidato 2 muere donde todos.

---

## 6. Veredicto

**VEREDICTO: PARCIAL.**

**Razón precisa.** La pregunta decisiva de P41 ("¿ALGÚN producto natural sobre
$(\mathcal{K},Q)$ hace al índice negativo estrictamente superaditivo?") tiene respuesta
**SÍ, incondicional y con cálculo cerrado**: el producto tensorial de Krein, con
$\mathrm{neg.ind}(Q_1 \otimes Q_2) = p_1q_2 + q_1p_2$ (Proposición 3.1), estrictamente
superaditivo en cuanto $(p_1-1)q_2 + (p_2-1)q_1 > 0$, y sobre
$\mathcal{K}_{\mathrm{off}}$ (signatura $(2m,2m)$) con crecimiento exponencial
$\kappa(\psi^{\otimes k}) = (4m)^k/2$. La primera mitad del falsador de P41 queda
refutada: κ NO es exactamente aditivo bajo todo ⊠ disponible. La Forma B **no muere por
(a)**.

Pero la ruta no queda VIVA sin calificación, por tres hechos igualmente precisos:

1. **Esterilidad del tensor abstracto** (Proposición 3.6): (a) y (b) del tensor puro se
   calculan con los mismos datos de signatura; ningún dato de amplificación íntegramente
   interno al álgebra lineal puede producir contradicción. Se necesita una segunda
   fuente — analítica o geométrica — para (b).
2. **Dicotomía multiplicar/sumar** (Observación 3.9): toda operación que permanece en la
   clase de funciones L realiza la suma directa (κ aditivo exacto, sin contradicción
   extraíble: segunda mitad del falsador, que sí se sostiene *dentro de la clase*); el
   tensor genuino (ceros $\rho_1+\rho_2-1/2$) sale de la clase, y con ella pierde la
   fórmula explícita y el mecanismo C5. La trivialidad grupal de GL(1) reaparece del
   lado analítico como **vacuidad de la familia Rankin–Selberg de $\zeta$**
   ($\mathbf{1}\boxtimes\mathbf{1}=\mathbf{1}$): el colapso esperado "(b) = GRH de la
   familia RS" ni siquiera se formula.
3. **El único realizador geométrico concebible del tensor genuino es el cuadrado del
   sitio de escala** (suma de Minkowski tropical de divisores; correspondencias de
   Frobenius como infraestructura, que sobre $(\mathcal{K},Q)$ son isometrías y no
   amplifican — Proposición 3.10), y el aparato cohomológico del cuadrado es MW-5:
   inconcluso, no refutado.

**El enunciado falsable que queda** (Problema 5.4): la fórmula de Weil en dos variables
restringida al núcleo diagonal multiplicativo $h(x_1,x_2) = g(x_1x_2)$ produce el
espectro suma $\{\rho_1+\rho_2-1\}$ del lado de ceros; ¿es su lado aritmético (soportado
en productos $p_1p_2$, i.e. casi-primos) **autónomo** — computable sin posiciones de
ceros — o re-encodea MW-7? Cálculo finito, ejecutable, con dos salidas limpias: un
candidato concreto para el Lema Faltante 5.2, o la muerte del Candidato 2 en el mismo
muro que los demás. Hasta que ese cálculo se haga, la Forma B está **PARCIAL: viva en
(a) con teorema, abierta en (b) con gap nombrado (Lemas 5.2–5.3) y un test decisivo
finito (Problema 5.4)**.

---

## Referencias

**Internas (backward-only):** P35 (teorema puente $\kappa(Q)=\mathrm{neg.ind}(H_C)$,
Hipótesis D, programa V.1–V.4); P39 (criterio de traza); P41 §7 (Forma B, Problema 7.2,
falsador); Doc 83 (factor del cuádruplo, $d\nu \geq 0$); Doc 91 (espacio de Pontryagin
de Weil–Connes, Kreĭn–Langer); Doc 94 (condición C5, perturbación Azizov–Iokhvidov,
brecha finitud→nulidad, Conjetura $\mathbf{C}_B$); Doc 96 (Teorema 8.1: localización del
índice en $\mathcal{K}_{\mathrm{off}}$; obstáculo $\mathbf{O}_D$); Doc 98 (Proposición
6.1: dos planos hiperbólicos por cuádruplo, $\kappa=2$, dim 4); Doc 99 (patrón de
transmutación; discriminador I2a; rigidez CF); Doc 102 (amplificador de Bagchi, único
mecanismo no-CAP del corpus, FAIL I2b); meta-docs/DISCRIMINATOR-hardening-phase-A.md
(criterios I1–I4).

**Literatura verificada:**
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS **43** (1974), 273–307.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952).
- T. Ya. Azizov, I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite
  Metric*, Wiley, 1989 (teorema de inercia y perturbación en espacios de Pontryagin).
- A. Connes, C. Consani, [*The Arithmetic Site*, arXiv:1405.4527](https://arxiv.org/pdf/1405.4527)
  y [CRAS 352 (2014) 971–975](https://alainconnes.org/wp-content/uploads/The-arithmetic-site-2014.pdf)
  (sitio aritmético, $\mathbb{Z}_{\max}$, Frobenius $\mathbb{N}^\times$; ley de
  composición $\Psi(\lambda)\circ\Psi(\lambda')=\Psi(\lambda\lambda')$ con deformación
  tangencial $\mathrm{Id}_\varepsilon$ en el caso mixto — verificado).
- A. Connes, C. Consani, [*The Scaling Site*, arXiv:1507.05818](https://arxiv.org/pdf/1507.05818);
  [*Geometry of the scaling site*, arXiv:1603.03191](https://arxiv.org/pdf/1603.03191)
  (extensión tropical $\mathbb{R}_{\max}^+$, $[0,\infty)\rtimes$ estructura,
  Riemann–Roch sobre la curva tropical — verificado a nivel de enunciados generales).
- A. Connes, [*An essay on the Riemann Hypothesis*, arXiv:1509.05576](https://arxiv.org/pdf/1509.05576)
  (estrategia Riemann–Roch, papel del cuadrado del sitio).
- H. Jacquet, J. Shalika, sobre Rankin–Selberg para $\mathrm{GL}(n)$ — citado solo por
  el hecho estándar $L(s, \chi_1 \times \chi_2) = L(s, \chi_1\chi_2)$ en GL(1)
  [estándar; cualquier referencia de RS lo contiene].
- Estructura fina de λ-anillo del semianillo de correspondencias CC más allá de la ley
  de composición: **[NO VERIFICADO; no usado en ningún argumento]**.

*Fin del Doc 106.*
