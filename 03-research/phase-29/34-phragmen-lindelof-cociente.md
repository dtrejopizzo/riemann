# Phase 29 — Doc 34: Dirección C — El Principio de Phragmén-Lindelöf para el Cociente $Q$

**Fecha:** junio 2026  
**Dirección:** C (análisis de la función $Q = C_\infty/\Xi$ en la franja $|\Im z| \leq 1/2$)  
**Objetivo:** Usar el principio de Phragmén-Lindelöf para controlar el cociente $Q(z) = C_\infty(z)/\Xi(z)$ en la franja de analiticidad $\mathcal{S} = \{z \in \mathbb{C}: |\Im z| < 1/2\}$. La hipótesis de que $Q$ sea holomorfa en $\mathbb{R}$ equivale a Inc. Inv.; la hipótesis de que $Q$ sea holomorfa en toda $\mathcal{S}$ equivale a RH.

---

## 1. Definición y propiedades básicas del cociente

**Definición (Doc 29, §3).** El cociente espectral es:

$$Q(z) := \frac{C_\infty(z)}{\Xi(z)},$$

donde $C_\infty(z) = w(z) - \Psi(z)$ (potencial límite del CCM, Doc 19) y $\Xi(z) = \xi(1/2 + iz)$ (función $\xi$ de Riemann en la variable $t = z$).

**Proposición 1** (meromorfia de $Q$ en $\mathcal{S}$).

(a) $C_\infty(z)$ es analítica en $\mathcal{S}$ (Proposición 1, Doc 19).

(b) $\Xi(z) = \xi(1/2+iz)$ es entera (sin polos en $\mathbb{C}$).

(c) Luego $Q(z) = C_\infty(z)/\Xi(z)$ es meromorfa en $\mathcal{S}$, con polos exactamente en los ceros de $\Xi$ en $\mathcal{S}$.

**Proposición 2** (ceros de $\Xi$ en $\mathcal{S}$ y RH). Un punto $z_0 \in \mathcal{S}$ satisface $\Xi(z_0) = 0$ iff $1/2 + iz_0$ es un cero no-trivial de $\zeta$. Bajo RH: todos los ceros de $\zeta$ tienen $\Re(s) = 1/2$, luego $\Im(z_0) = 0$, es decir, $z_0 \in \mathbb{R} \cap \mathcal{S}$. En ausencia de RH: puede haber ceros de $\Xi$ en el interior de $\mathcal{S}$.

**Proposición 3** (polo de $Q$ iff fallo de Inc. Inv./RH).

- $Q$ tiene polo en $z_0 \in \mathbb{R}$ iff $\Xi(z_0) = 0$ y $C_\infty(z_0) \neq 0$ iff $z_0 = \gamma_n$ para algún $n$ con $C_\infty(\gamma_n) \neq 0$ iff Inc. Inv. falla en $z_0$.

- $Q$ tiene polo en $z_0 \in \mathcal{S} \setminus \mathbb{R}$ iff $\Xi(z_0) = 0$ (cero de $\zeta$ fuera de la recta crítica) iff RH falla.

**Corolario 1** (equivalencias con $Q$ holomorfa). Las siguientes son equivalentes:

(i) $Q$ es holomorfa en $\mathbb{R}$ (sin polos sobre el eje real): Inc. Inv.

(ii) $Q$ es holomorfa en toda $\mathcal{S}$: RH.

(iii) $Q$ es holomorfa en $\mathcal{S}$: $\{C_\infty = 0\} = \{\Xi = 0\}$ en $\mathcal{S}$.

---

## 2. El principio de Phragmén-Lindelöf para franjas

**Teorema PL clásico (Phragmén-Lindelöf para franjas).** Sea $f$ holomorfa y continua en la franja cerrada $\mathcal{S}_{a,b} = \{z: a \leq \Im z \leq b\}$. Suponga:

(H1) En $\Im z = a$: $|f(x+ia)| \leq M_a$ para todo $x \in \mathbb{R}$.

(H2) En $\Im z = b$: $|f(x+ib)| \leq M_b$ para todo $x \in \mathbb{R}$.

(H3) Cota de crecimiento: $|f(x+iy)| \leq C e^{e^{\alpha|x|}}$ para alguna constante $\alpha < \pi/(b-a)$ y $C > 0$.

Entonces: $|f(x+iy)| \leq M_a^{(b-y)/(b-a)} M_b^{(y-a)/(b-a)}$ para todo $z = x+iy \in \mathcal{S}_{a,b}$.

**Aplicación a $Q$.** Queremos aplicar el PL a $Q(z)$ en $\mathcal{S}_{-1/2,1/2}$ (la franja completa de analiticidad). Para ello necesitamos verificar las hipótesis (H1)-(H3).

---

## 3. El borde inferior de la franja: $\Im z = -1/2$

**Evaluación de $C_\infty$ en $\Im z = -1/2$.** Para $z = t - i/2$ con $t \in \mathbb{R}$:

$$C_\infty(t-i/2) = w(t-i/2) - 2\sum_p\Lambda(p)p^{-1/2}e^{i(t-i/2)\log p} = w(t-i/2) - 2\sum_p\Lambda(p)p^{-1/2+1/2}e^{it\log p}.$$

Pero $\sum_p\Lambda(p)p^0 e^{it\log p} = \sum_p\Lambda(p)e^{it\log p}$, que diverge absolutamente. El borde $\Im z = -1/2$ está FUERA de la región de convergencia absoluta de $\Psi(z) = 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}$ (que converge absolutamente solo para $\Im z > 1/2$).

**El polo de $C_\infty$ en $\Im z = -1/2$.** El símbolo arquimediano $w(z) = \frac{1}{2i}\psi(\frac{1}{4}+\frac{iz}{2}) + \text{c.c.} - \log\pi$ tiene polos en $z = i(2k+1)/2$ para $k \in \mathbb{Z}_{\geq 0}$ — el primer polo en $z = i/2$ (i.e., $\Im z = 1/2$) y el simétrico en $z = -i/2$ (i.e., $\Im z = -1/2$).

**Conclusión.** $C_\infty$ tiene polos en $\Im z = \pm 1/2$. La franja de analiticidad de $C_\infty$ es estrictamente $|\Im z| < 1/2$ — los bordes $\Im z = \pm 1/2$ son SINGULARES.

Esto IMPIDE la aplicación directa del PL en la franja cerrada $\overline{\mathcal{S}}$: $Q$ no se extiende continuamente a $\Im z = \pm 1/2$.

---

## 4. El PL en sub-franjas $|\Im z| \leq 1/2 - \varepsilon$

**Setup.** Para $\varepsilon \in (0, 1/2)$, sea $\mathcal{S}_\varepsilon = \{z: |\Im z| \leq 1/2-\varepsilon\}$ la sub-franja compacta.

**Proposición 4** (comportamiento de $Q$ en $\Im z = \pm(1/2-\varepsilon)$). Para $z = t \pm i(1/2-\varepsilon)$ con $t \in \mathbb{R}$ y $|t| \to \infty$:

(a) $|C_\infty(t\pm i(1/2-\varepsilon))| \leq 2\sum_\rho |\rho|^{-1-(1/2-\varepsilon)}\cdot 1 = 2\sum_\rho |\rho|^{-3/2+\varepsilon}$, que es absolutamente convergente para $\varepsilon < 1/2$ (los ceros de $\zeta$ satisfacen $|\rho| \geq 1$ y $\sum|\rho|^{-3/2+\varepsilon}$ converge). En particular, $|C_\infty|$ es ACOTADO en $\Im z = \pm(1/2-\varepsilon)$ para $\varepsilon > 0$.

(b) $|\Xi(t\pm i(1/2-\varepsilon))| = |\xi(1/2 + i(t\pm i(1/2-\varepsilon)))| = |\xi(\varepsilon \pm it)|$ o $|\xi(1-\varepsilon\pm it)|$.

Para $t\to\infty$: $|\xi(\varepsilon + it)| \sim C|t|^{1/2-\varepsilon}|\zeta(\varepsilon+it)| \cdot \text{factor Gamma}$.

Como $|\zeta(\varepsilon+it)| = O(|t|^\sigma)$ para algún $\sigma > 0$: $|\Xi(t\pm i(1/2-\varepsilon))| \to \infty$ cuando $t\to\infty$ (polinomialmente).

**Proposición 5** (cota para $Q$ en los bordes de la sub-franja). Para $z = t + i\eta$ con $|\eta| = 1/2-\varepsilon$ y $|t| \to \infty$:

$$|Q(t+i\eta)| = \frac{|C_\infty(t+i\eta)|}{|\Xi(t+i\eta)|} \leq \frac{C_\varepsilon}{|t|^{1/2-\varepsilon-\delta}} \to 0 \quad \text{cuando } |t| \to \infty,$$

para algún $\delta > 0$ (usando la cota $|C_\infty| \leq C$ acotado y $|\Xi| \to \infty$ polinomialmente).

*Prueba.* $|C_\infty(t+i\eta)| \leq 2\sum_\rho|\rho|^{-3/2+\varepsilon}$ = constante finita $C_\varepsilon > 0$. Y $|\Xi(t+i\eta)| \geq c|t|^{1/2-\varepsilon-\delta}$ para $|t|$ grande (de las estimaciones estándar de $\xi$ sobre la línea $\Re s = \varepsilon$, usando la ecuación funcional $\xi(s)=\xi(1-s)$). $\square$

---

## 5. Aplicación del PL en la sub-franja

**Configuración.** Para $\varepsilon > 0$ fijo, $Q$ es meromorfa en $\mathcal{S}_\varepsilon$ (con posibles polos donde $\Xi = 0$). Si $Q$ resulta ser holomorfa en $\mathcal{S}_\varepsilon$: las hipótesis del PL son:

(H1) En $|\Im z| = 1/2-\varepsilon$: $|Q| \to 0$ cuando $|z| \to \infty$ (Proposición 5). $\Rightarrow$ $|Q|$ es ACOTADO en los bordes por alguna constante $M_\varepsilon < \infty$.

(H2) Cota de crecimiento: $Q$ es meromorfa en $\mathcal{S}_\varepsilon$; si holomorfa, satisface $|Q(x+iy)| \leq \exp(\exp(\alpha|x|))$ para algún $\alpha > 0$ (de la meromorfia de $C_\infty/\Xi$).

**Teorema PL aplicado a $Q$ en $\mathcal{S}_\varepsilon$.** Si $Q$ es holomorfa en $\mathcal{S}_\varepsilon$ (sin polos):

$$|Q(z)| \leq M_\varepsilon^{1-|\Im z|/(1/2-\varepsilon)} \cdot M_\varepsilon^{|\Im z|/(1/2-\varepsilon)} = M_\varepsilon \quad \forall\, z \in \mathcal{S}_\varepsilon.$$

(En este caso la cota es homogénea: $Q$ es acotado en toda $\mathcal{S}_\varepsilon$.)

**Corolario 2** (RH implica $Q$ acotado en toda sub-franja). Bajo RH: $Q$ es holomorfa en $\mathcal{S}_\varepsilon$ para todo $\varepsilon > 0$ (sin ceros de $\Xi$ fuera de $\mathbb{R}$). Por el PL: $Q$ es uniformemente acotado en cada $\mathcal{S}_\varepsilon$.

**Corolario 3** (fallo de RH implica $Q$ no-acotado). Si RH falla: existe un cero $z_0$ de $\Xi$ con $0 < |\Im z_0| < 1/2$. Entonces $Q$ tiene un polo en $z_0$ y $|Q(z)| \to \infty$ cuando $z \to z_0$.

---

## 6. El PL como herramienta de detección, no de prueba

**El problema lógico del PL aquí.** El teorema PL puede usarse en dos modos:

**Modo de CONSECUENCIA:** Asumir $Q$ holomorfa $\Rightarrow$ PL da acotación. (Útil si ya sabemos que $Q$ es holomorfa, para deducir propiedades.)

**Modo de PRUEBA de holomorfia:** Asumir acotación en los bordes $\Rightarrow$ PL da holomorfia en el interior. (ERRÓNEO: el PL no prueba holomorfia; solo acota funciones ya holomorfas.)

Para probar Inc. Inv. (= $Q$ holomorfa en $\mathbb{R}$): necesitamos el Modo de Prueba. Pero el PL requiere que $Q$ YA SEA HOLOMORFA en el dominio.

**Conclusión.** El PL, tal como está, no puede PROBAR que $Q$ es holomorfa en $\mathbb{R}$. Solo puede:

(a) Dar cotas para $Q$ SI se asume que es holomorfa (Corolarios 2-3).

(b) Dar una CARACTERIZACIÓN negativa: si $Q$ no es holomorfa en $\mathbb{R}$, las cotas del PL en los bordes de la sub-franja no se satisfacen de cierto modo.

---

## 7. El argumento inverso: acotación implica holomorfia

**La herramienta: el teorema de Riemann sobre singularidades removibles.** Si $Q$ es meromorfa en $\mathcal{S}_\varepsilon$ y acotada en una vecindad de cada punto $z_0 \in \mathbb{R}$ con $\Xi(z_0) = 0$: entonces $z_0$ es una singularidad REMOVIBLE de $Q$, y $Q$ se extiende holómorfamente a $z_0$.

Luego: para probar Inc. Inv. (holomorfia de $Q$ en $\mathbb{R}$), basta mostrar que $Q$ es LOCALMENTE ACOTADA en cada $\gamma_n$.

**Proposición 6** (acotación local de $Q$ en $\gamma_n$). $Q$ es acotada en una vecindad de $\gamma_n$ iff $C_\infty(\gamma_n) = 0$ (cuando $\Xi(\gamma_n) = 0$ y la singularidad es removible) iff Inc. Inv. en $\gamma_n$.

*Prueba.* Si $\Xi(\gamma_n) = 0$ con multiplicidad 1 y $C_\infty(\gamma_n) \neq 0$: $Q(z) \sim C_\infty(\gamma_n)/[\Xi'(\gamma_n)(z-\gamma_n)] \to \infty$ cuando $z \to \gamma_n$ — no acotado. Si $C_\infty(\gamma_n) = 0$: $Q$ es acotado cerca de $\gamma_n$ (el polo se cancela). $\square$

**El intento de PL-inverso.** Suponga que podemos probar, desde la estructura de $C_\infty$ y $\Xi$:

(*) $|Q(z)|$ es uniformemente acotado en $\mathcal{S}_\varepsilon$ para algún $\varepsilon > 0$, INDEPENDIENTEMENTE de Inc. Inv.

Entonces: por el Teorema de Riemann, $Q$ no puede tener polos en $\mathbb{R}$ — luego Inc. Inv. seguiría.

¿Puede probarse (*) independientemente?

---

## 8. Intento de cota uniforme para $Q$ sin asumir Inc. Inv.

**Proposición 7** (la cota falla por los polos en $\mathbb{R}$). Si Inc. Inv. falla en algún $\gamma_{n_0}$: entonces $|Q(z)| \to \infty$ cuando $z \to \gamma_{n_0}$, luego (*) no se satisface. La condición (*) es EQUIVALENTE a Inc. Inv. — circular.

**El obstáculo fundamental.** La cota uniforme (*) no puede probarse independientemente de Inc. Inv., porque los polos de $Q$ en $\mathbb{R}$ son exactamente los puntos donde Inc. Inv. falla. Probar (*) requiere saber que no hay polos en $\mathbb{R}$, que es Inc. Inv.

---

## 9. El PL en la dirección diagonal: cotas de $|Q|$ desde el crecimiento

**Aún así, el PL puede usarse para dar cotas condicionales.** Suponga:

(A) $Q$ tiene exactamente $K$ polos en $\mathbb{R}$ (es decir, Inc. Inv. falla en $K$ puntos).

(B) Cerca de cada polo $z_0 = \gamma_{n_k}$: $|Q(z)| \leq M|z-z_0|^{-1}$ (polo simple).

**Proposición 8** (el cociente regularizado $\tilde Q$). Define $\tilde Q(z) = Q(z)\cdot\prod_{k=1}^K (z-\gamma_{n_k})$. Si (A) y (B): $\tilde Q$ es holomorfa en $\mathbb{R}$ y meromorfa en $\mathcal{S}_\varepsilon$.

PL aplicado a $\tilde Q$: si $|\tilde Q|$ es acotado en los bordes de la sub-franja, entonces $|\tilde Q| \leq M_\varepsilon$ en toda $\mathcal{S}_\varepsilon$.

**La cota del producto regularizante.** $\prod_{k=1}^K |z-\gamma_{n_k}|$: en los bordes $|\Im z| = 1/2-\varepsilon$, este producto es de orden $O(1)$ (pues los $\gamma_{n_k}$ son finitos). Luego si $|Q|$ es acotado en los bordes (¿?), $|\tilde Q|$ también.

**El problema de la hipótesis "acotado en los bordes."** En los bordes $|\Im z| = 1/2-\varepsilon$: $|Q| = |C_\infty|/|\Xi|$. Si $\Xi$ NO tiene ceros en $|\Im z| = 1/2-\varepsilon$ (lo cual depende de la distribución de los ceros de $\zeta$ en la franja, un resultado no establecido incondicionalmente): $Q$ es continuo y $|Q| \to 0$ por la Proposición 5.

Si $\Xi$ TIENE ceros en $|\Im z| = 1/2-\varepsilon$ (violación de RH más fuerte, ceros a distancia $1/2-\varepsilon$ de la recta crítica): $Q$ tiene polos en los bordes también, y la hipótesis del PL falla.

---

## 10. Un resultado parcial: el PL condicional

**Teorema 2** (PL condicional, main result de la Dirección C). Suponiendo:

(C1) $\Xi$ no tiene ceros en la franja $1/2-2\varepsilon \leq |\Im z| \leq 1/2-\varepsilon$ (es decir, los posibles ceros de $\zeta$ fuera de la recta crítica están a distancia $> \varepsilon$ del borde de $\mathcal{S}_\varepsilon$).

(C2) $C_\infty$ es acotado en la franja $|\Im z| \leq 1/2-\varepsilon$ (de la Proposición 4(a), esto es cierto con constante $C_\varepsilon$).

Entonces: $Q = C_\infty/\Xi$ satisface $|Q| \leq C_\varepsilon/c_\varepsilon$ en los bordes $|\Im z| = 1/2-\varepsilon$ (donde $c_\varepsilon = \min_{|\Im z|=1/2-\varepsilon}|\Xi|$).

Y si además $Q$ es holomorfa en $\mathcal{S}_\varepsilon$ (sin polos, i.e., sin ceros de $\Xi$ en el interior): $|Q| \leq C_\varepsilon/c_\varepsilon$ en toda $\mathcal{S}_\varepsilon$ (del PL).

*Prueba.* Directa del Teorema PL aplicado a $Q$ bajo las hipótesis (C1)-(C2). $\square$

**Honestidad.** La condición (C1) es una hipótesis sobre la distribución de los ceros de $\zeta$ en la franja, y requiere conocimiento que no está disponible incondicionalmente. La hipótesis "sin ceros de $\Xi$ en $\mathcal{S}_\varepsilon$" es exactamente RH. Circular nuevamente.

---

## 11. Conclusión de la Dirección C

**Lo que funciona.** El análisis de $Q = C_\infty/\Xi$ en la franja es una formulación elegante:

- Inc. Inv. ↔ $Q$ holomorfa en $\mathbb{R}$.
- RH ↔ $Q$ holomorfa en $\mathcal{S}$.
- El cociente $Q$ decae a $0$ en los bordes $|\Im z| = 1/2-\varepsilon$ (Proposición 5) — resultado incondicional.

**El obstáculo estructural.** El PL es una herramienta para ACOTAR funciones holomorfas, no para DEMOSTRAR holomorfia. Para probar que $Q$ no tiene polos en $\mathbb{R}$ (= Inc. Inv.), se necesita un argumento DIFERENTE — no el PL.

**Lo que el PL SÍ da (resultado honesto).** 

Bajo RH (como hipótesis): $Q$ es holomorfa en $\mathcal{S}$ y satisface $|Q| \leq C_\varepsilon$ uniformemente en $\mathcal{S}_\varepsilon$, con $C_\varepsilon \to 0$ cuando $\varepsilon \to 0$. Esto da la cota $|Q(t)| = O(1)$ en $\mathbb{R}$ (condicionalmente a RH). Consistente pero no probatorio.

**Observación geométrica nueva.** El hecho de que $|Q(z)| \to 0$ en los bordes $|\Im z| = 1/2-\varepsilon$ (para todo $\varepsilon > 0$) sugiere que $Q$ "quiere" ser cero en los bordes de la franja — coherente con Inc. Inv. (los polos en $\mathbb{R}$ son el único obstáculo). Si se pudiera mostrar que este decaimiento en los bordes es UNIFORME en $\varepsilon$ (es decir, $|Q|$ decae a 0 uniformemente cuando uno se acerca a $\Im z = \pm 1/2$ desde el interior): por un argumento de límite, $Q$ se anularía en los bordes de la franja — pero los bordes no están en $\mathcal{S}$.

**Propuesta para Phase 31.** La geometría del decaimiento de $Q$ en la franja merece estudio. Específicamente: ¿el decaimiento de $|Q|$ en los bordes $|\Im z| \to 1/2$ es suficientemente uniforme para implicar, via un argumento de subarmónica, que $Q$ no puede tener polos en $\mathbb{R}$?

---

*Siguiente doc: Doc 35 — Dirección D: Deslocalización de Eigenvectores y el Teorema de Szegő.*
