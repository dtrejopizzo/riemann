# Documento 186 — Auditoría adversarial de los Docs 174 y 177

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato:** auditoría adversarial de D174 (coercividad/backward) y D177 (despegue Hermite). Reconstrucción independiente de cada prueba antes de leer; las constantes importan; backward-only respecto del flujo DBN en carta $H_t$. Incluye la clasificación estructural ordenada por el director (COERCIVO / CORRELACIONAL / MIXTO / REDUNDANTE).
**Convenciones auditadas y aceptadas:** carta $H_t$ (Polymath 15), $\partial_tH_t=-\partial_z^2H_t$; backward $\sigma=t_0-t$, $H_t=e^{\sigma\partial_z^2}H_{t_0}$; $\dot z_k=2\sum'(z_k-z_j)^{-1}$; ley de balance $\dot I=-2\kappa-D$, $D\ge0$ (Doc 167, certificada, no re-auditada); $\kappa$ = número de ceros superiores (2 por cuádruplo: $z$, $-\bar z$) — convención verificada consistente en ambos documentos.

---

## 1. Auditoría del Doc 174

### 1.1. [PROP 174.1] No-coercividad $D\ge cI$ — **CERTIFICADO**

Reconstrucción independiente. Para $z_1=\alpha+i\beta$ en el cuádruplo $\{\pm z_1,\pm\bar z_1\}$:
- conjugado $\bar z_1$: $2/(2i\beta)=-i/\beta$ ⟹ aporte a $\dot\beta$: $-1/\beta$;
- antípoda $-z_1$: $2/(2z_1)=\bar z_1/|z_1|^2$ ⟹ aporte $-\beta/|z_1|^2$;
- espejo $-\bar z_1$: $2/(2\alpha)$ real ⟹ aporte $0$.

$\dot\beta=-1/\beta-\beta/|z_1|^2$; con dos modos superiores, $\dot I=4\beta\dot\beta=-4-4\beta^2/|z_1|^2$, $D=4\beta^2/|z_1|^2$, $D/I=2/|z_1|^2\to0$. Coincide término a término con el documento. El contraejemplo a $D\ge cI$ es correcto. ✓

### 1.2. [THM 174.2] Coercividad exponencial — **CERTIFICADO-CON-ERRATA** (E-186.4, de redacción)

El punto de ataque era la dirección de la cadena $\dot I\le-2I/M\le-2I$. Verificado: $I\le\kappa M$ ⟹ $-2\kappa\le-2I/M$; y $-2I/M\le-2I$ **requiere $M\le1$**, que el documento sí establece (banda estricta $|\operatorname{Im}z|<1$ en $t=0$ + Lema 174.3 ⟹ $M(t)<1$ para $t\ge0$). La cadena está en el orden correcto y la hipótesis de banda está usada explícitamente, no tácita. **Advertencia de alcance que el enunciado ya respeta:** la desigualdad $-2I/M\le-2I$ se invertiría si $M>1$; el teorema solo se aplica forward desde $t\ge0$, donde $M<1$. Para lecturas backward ($t<0$, donde $M(t)\ge2|t|$ puede superar 1) el documento usa correctamente solo la forma $\dot I\le-2I/M$ con $M\le\bar M$ (§2.1) — sin error.

Integración verificada: $d\log I\le-2\,dt/(M_0-2(t-t_0))$ ⟹ $I\le I_0\bigl(1-2(t-t_0)/M_0\bigr)$; la dirección $M(s)\le M_0-2(s-t_0)$ ⟹ $-2I/M(s)\le-2I/(M_0-2(s-t_0))$ es la correcta. ✓

**Unidades/cartas verificadas:** $I_\zeta=I/4$, $\tau=t/4$ ⟹ $dI_\zeta/d\tau=dI/dt$; $-2I=-8I_\zeta$ ✓; $M_\zeta=M/4<1/4$ ✓; $-2I_\zeta/M_\zeta=-2I/M$ ✓. La conversión es consistente (no se repite el patrón E-171.x).

**E-186.4 (menor):** "extinción lineal exacta" — la fórmula es una cota superior lineal, no una ley exacta (la igualdad solo se realiza en el par aislado). Redacción, no matemática.

### 1.3. [LEMA 174.3] Principio del máximo — **CERTIFICADO**

Reconstruido: para $\beta_k$ maximal, conjugado propio $=-2$ exacto; cruzados $-4\beta_k(\beta_k-\beta_l)/d^2\le0$ y $-4\beta_k(\beta_k+\beta_l)/d^2\le0$ sin simetrizar (correcto: la maximalidad da el signo directamente); antípoda y reales $\le0$ (parte imaginaria de $1/(z-x)$ es $-\beta/|z-x|^2$). La convergencia absoluta de la suma sobre el mar real exige la densidad RvM de la clase — hipótesis presente vía Thm 167-2.3. La atribución honesta a de Bruijn Thm 13 es correcta. ✓

### 1.4. [THM 174.4] Modelo cerrado del cuádruplo — **CERTIFICADO**

Reconstrucción completa:
- $H=z^4+az^2+c=(z^2-w)(z^2-\bar w)$ ⟹ $a=-2\operatorname{Re}w$, $c=|w|^2$; $\operatorname{Re}w=-a/2$, $(\operatorname{Im}w)^2=c-a^2/4$ ✓.
- $\partial_z^2H=12z^2+2a$ ⟹ $\dot a=-12$, $\dot c=-2a$ ✓.
- $\frac{d}{dt}\operatorname{Re}w=6$ ✓; $\frac{d}{dt}(\operatorname{Im}w)^2=\dot c-\tfrac{a\dot a}2=-2a+6a=4a=-8\operatorname{Re}w$ ✓.
- $t_c$: $24t^2+8R_0t-(\operatorname{Im}w_0)^2=0$ ⟹ la fórmula del recuadro ✓.
- **Expansión (donde suelen esconderse los errores de signo):** con $R=\alpha^2-\beta^2$, $\operatorname{Im}w_0=2\alpha\beta$: $\sqrt{R^2+6\alpha^2\beta^2}\approx R+3\alpha^2\beta^2/R-\tfrac92\alpha^4\beta^4/R^3$; $t_c\approx\frac{\alpha^2\beta^2}{2R}-\frac34\frac{\beta^4}{\alpha^2}=\frac{\beta^2}2+\frac{\beta^4}{2\alpha^2}-\frac{3\beta^4}{4\alpha^2}=\frac{\beta^2}2-\frac{\beta^4}{4\alpha^2}$ — **el término $-\beta_0^4/4\alpha_0^2$ y su signo (interacción acelera) son correctos**.
- Verificación cruzada: $\dot I=2\operatorname{Re}w/|w|-6=(-4\alpha^2-8\beta^2)/|z_1|^2=-4-4\beta^2/|z_1|^2$ = Prop 174.1 ✓.

La respuesta al director ($t_c=\beta_0^2/2$, no $\beta_0^2/4$; $=I_0/4$ por cuádruplo) es aritméticamente correcta. ✓

### 1.5. [THM 174.5] Forward cerrado — **CERTIFICADO** (combinación de piezas certificadas + [KKL]).

### 1.6. [THM 174.8] Presupuesto de vidas — **CERTIFICADO**

Punto de ataque obligatorio: el solape de vidas. **Veredicto: el solape no rompe nada porque la prueba no usa disyunción temporal.** La identidad $\int_0^\Lambda\kappa\,dt=2\sum_j\ell_j$ es de Fubini–Tonelli para funciones indicador: $\kappa(t)=\sum_j2\cdot\mathbf 1_{\{j\text{ off}\}}$ es aditiva en cuádruplos simultáneos, y la integral cuenta cada vida con multiplicidad correcta. Si dos cuádruplos solapan, $\kappa\ge4$ durante el solape e $\dot I\le-8$ ahí — lo cual hace la desigualdad $I(0^+)\ge2\int\kappa$ **más holgada**, nunca más estrecha (la holgura extra va a parar al término $\int D\ge0$ y al hecho de que la integral hasta $\Lambda$ descarta $I(\Lambda)\ge0$... de hecho $I(\Lambda)=0$). La cadena $I(\varepsilon)=\int_\varepsilon^\Lambda(2\kappa+D)\ge2\int_\varepsilon^\Lambda\kappa$ y convergencia monótona: correcta. La validez de la ley a través de colisiones descansa en la reparación 5 del Doc 168 (certificada, prerequisito). ✓

### 1.7. [THM 174.10] Jerarquía de momentos — **CERTIFICADO** (la sospecha máxima del mandato se resuelve a favor)

Reconstrucción del término cruzado para $n\ge2$, que era el punto débil designado:
$$\dot I_{2n}=-4n\sum_k\sum_{w\ne z_k}\beta_k^{2n-1}\frac{\beta_k-\operatorname{Im}w}{|z_k-w|^2}.$$
- Conjugado propio: $\beta_k^{2n-1}\cdot2\beta_k/(4\beta_k^2)=\beta_k^{2n-2}/2$ ⟹ $-2nI_{2n-2}$ ✓.
- Cruzados tipo $(z_k,z_l)$: los denominadores son **idénticos** ($|z_k-z_l|^2$); numerador simetrizado $\beta_k^{2n-1}(\beta_k-\beta_l)+\beta_l^{2n-1}(\beta_l-\beta_k)=(\beta_k-\beta_l)(\beta_k^{2n-1}-\beta_l^{2n-1})\ge0$ — **válido para todo $n$ porque $x\mapsto x^{2n-1}$ es creciente** (no se necesita cuadrado perfecto; basta monotonía: es una desigualdad de Chebyshev de 2 puntos). El temor de que "el binomio no es cuadrado perfecto para $n\ge2$" es infundado: la prueba de $n=1$ no usaba el cuadrado per se, sino la monotonía de $x\mapsto x$, y ésta escala.
- Cruzados tipo $(z_k,\bar z_l)$: denominadores $|z_k-\bar z_l|=|z_l-\bar z_k|$ (conjugación) ✓; numerador $(\beta_k+\beta_l)(\beta_k^{2n-1}+\beta_l^{2n-1})\ge0$ ✓. Lo mismo para los pares con espejos $-z_l,-\bar z_l$.
- Antípoda y reales: signo trivialmente correcto ($\beta_k^{2n}\ge0$).

$D_{2n}\ge0$ término a término **sobrevive para todo $n$**. Verificación en el par aislado ($D_{2n}=0$, cascada libre) ✓. **La familia $D_{2n}\ge0$ está sana; lo que cae es el corolario virial:**

### 1.8. [COR 174.11(2)] Familia virial — **REFUTADO en su prueba; DEGRADADO en su enunciado** (E-186.1, la baja principal de esta auditoría)

**El paso falso, exhibido.** La prueba afirma: "$(I_{2n}/\kappa)^{1/n}\le(I_{2n-2}/\kappa)^{1/(n-1)}$ (monotonía de medias de potencias)", de donde deduce $I_{2n-2}\ge\kappa^{1/n}I_{2n}^{(n-1)/n}$. **La monotonía de medias de potencias dice exactamente lo contrario:** para $a_k=\beta_k^2\ge0$ y exponentes $n-1<n$,
$$\Bigl(\tfrac1\kappa\sum a_k^{\,n-1}\Bigr)^{1/(n-1)}\;\le\;\Bigl(\tfrac1\kappa\sum a_k^{\,n}\Bigr)^{1/n},$$
es decir $I_{2n-2}\le\kappa^{1/n}I_{2n}^{(n-1)/n}$ — la desigualdad usada está **invertida**.

**Contraejemplo a la desigualdad diferencial deducida.** Dos pares con alturas $a\gg b$ ($\kappa=4$, pero basta el caso mínimo): $I_{2n-2}\approx2a^{2n-2}$, $I_{2n}^{(n-1)/n}\approx(2)^{(n-1)/n}a^{2n-2}$. La desigualdad que la prueba necesita, $I_{2n-2}\ge2^{1/n}I_{2n}^{(n-1)/n}$, exige $2\ge2^{1/n}\cdot2^{(n-1)/n}=2$ — igualdad justa en este caso; pero con un solo par dominante y $\kappa=2$ (un cuádruplo con $\beta_2\ll\beta_1$ tras perturbación, o en la clase general dos pares de alturas dispares): $I_{2n-2}\approx a^{2n-2}<2^{1/n}a^{2n-2}\approx2^{1/n}I_{2n}^{(n-1)/n}$. La EDO $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ **no se sigue** de $\dot I_{2n}\le-2nI_{2n-2}$; el sobrante tendría que venir de $D_{2n}$, que no tiene cota inferior (Prop 174.1).

**Qué sobrevive (versión degradada):**
1. Los extremos son teoremas por vías independientes: $n=1$ ($\Lambda\le t_0+I/4$, Cor 167-2.4) y $n=\infty$ ($\Lambda\le t_0+M/2$, Lema 174.3).
2. Para $n$ intermedio vale la versión con constante peor: $I_{2n}\ge M^n$ (el término maximal) ⟹ $I_{2n}^{1/n}\ge M$ ⟹ por la banda, $\boxed{\Lambda\le t_0+\tfrac12 I_{2n}(t_0)^{1/n}}$ — denominador $2$, no $2^{1+1/n}$. Esta versión es **trivial módulo el Lema 174.3** (no aporta información nueva sobre los extremos).
3. Cor 174.11(1) ($\dot I_{2n}\le-2nI_{2n}$, decaimiento $e^{-2nt}$) es **correcto**: usa solo $I_{2n}\le M\,I_{2n-2}$ y $M<1$, verificado.

**Impacto:** la narrativa "la jerarquía interpola exactamente entre virial y banda — una sola familia" queda **degradada a retórica**: los extremos son teoremas, el interior interpolante no está probado con la constante anunciada (y la mejora $2^{1+1/n}$ vs $2$ es exactamente lo que haría a la familia no-trivial). El "mejor teorema del documento" según su propio veredicto pierde su corolario estrella; el Teorema 174.10 ($D_{2n}\ge0$) permanece íntegro.

### 1.9. [§3.3] Refutación de "$I<\infty\Rightarrow m<\infty$" en la clase — **CERTIFICADO** (load-bearing verificado)

Auditoría de la configuración Hadamard ($\gamma_j=2^j$, $b_j=e^{-\gamma_j}$, ceros reales en puntos RvM), los tres ítems del mandato:

(i) **Clase y convergencia.** Ceros: red real de densidad RvM ($x_n\asymp$ solución de $N(x)=n$) más cuádruplos $\{\pm\gamma_j\pm ib_j\}$. $\sum1/|z|^2<\infty$ (densidad logarítmica) ⟹ producto de Hadamard de género $\le1$ converge; orden $\le1<2$; simetrías (real en $\mathbb R$, par) construibles. El semigrupo $e^{-t\partial_z^2}$ actúa en orden $<2$ (de Bruijn §2). ✓

(ii) **RvM.** Los cuádruplos añaden $O(1)$ ceros por bloque diádico $[2^j,2^{j+1}]$, que contiene $\asymp2^j\log2^j$ ceros reales: la densidad RvM se preserva con error relativo $O(2^{-j})$. ✓

(iii) **¿Fluye?** Objeción potencial: en $t=0$, $\kappa=\infty$ y el sistema de ODEs con infinitos ceros no reales no está justificado. **Resolución correcta (implícita en el doc, la hago explícita):** el flujo se define por el semigrupo sobre la *función*, no por las ODEs; las ODEs solo se invocan donde $\kappa<\infty$. Y para todo $t>0$: el cuádruplo $j$ aterriza en $t_j\approx b_j^2/2=e^{-2^{j+1}}/2$, sumable y decreciente superexponencialmente, luego para todo $t>0$ solo los finitos $j$ con $t_j>t$ siguen off: $\kappa(t)<\infty$ — la configuración satisface el análogo de KKL por construcción. Vidas $\ell_j\approx b_j^2/2$ con $\sum\ell_j\ll I/4$: presupuesto consistente. ✓ (El aislamiento súper-exponencial hace los cuádruplos efectivamente independientes: el modelo del Thm 174.4 aplica con corrección $O(b_j^2/\gamma_j^2)$.)

**La refutación se sostiene.** Las "imposibilidades ζ-libres" que cuelgan de ella (D176, D177 §4.3 doble consistencia, la arquitectura de dos torres) conservan su soporte.

### 1.10. Resto del Doc 174

- **[Cálculo 174.6]** ($t_c=-g^2/8$): $H=z^2-g^2/4-2t$, ceros $\pm\sqrt{2t+g^2/4}$ ✓. **CERTIFICADO** (cálculo elemental).
- **[Prop 174.7]** (red punto fijo): $\partial_t(e^t\cos z)=e^t\cos z=-\partial_z^2(e^t\cos z)$ ✓. **CERTIFICADO.** Nota: $\cos z$ tiene ceros en $\pi(k+\frac12)$, espaciado constante — no es de densidad RvM creciente; la *lectura* ("la densidad no compra despegues") es legítima como contraejemplo a la heurística de densidad, pero el punto fijo es una configuración muy no-genérica (toda simetría exacta). Correcto tal como se usa.
- **[Cálculo 174.9]** (cluster $\ell^2$): es heurístico y está etiquetado CÁLCULO, no TEOREMA — admisible bajo el contrato. La exclusión de colisiones real–real por repulsión ($\dot g=4/g+O(1)$) es correcta para el gap mínimo.
- **[Prop 174.12]** (entropía): $\varphi(\beta)=2\beta\log(1/\beta)-\beta$ ✓; $\varphi\ge0\iff\beta\le e^{-1/2}$, $\varphi'\ge0\iff\beta\le e^{-3/2}$ ✓; la simetrización con peso monótono es el mismo mecanismo (sano) del Thm 174.10. **CERTIFICADO** (condicional a $\sup\beta\le e^{-3/2}$, declarado).
- **[§2.3, GAP-174.B, huérfanos]:** especulación etiquetada como GAP — sin reclamos que auditar; la heurística de pendiente $2k$ de §2.3(b) fue refutada por el propio D177, ver abajo.

---

## 2. Auditoría del Doc 177

### 2.1. [THM 177.1] Despegue Hermite exacto — **CERTIFICADO**

Identidad $e^{s\partial_z^2}z^n=(-s)^{n/2}H_n\bigl(z/(2\sqrt{-s})\bigr)$, verificada a mano:
- $n=2$: $(-s)H_2(z/2\sqrt{-s})=(-s)\bigl(4\cdot\frac{z^2}{4(-s)}-2\bigr)=z^2+2s$; directo: $e^{s\partial^2}z^2=z^2+2s$ ✓.
- $n=3$: $(-s)^{3/2}\bigl(8\frac{z^3}{8(-s)^{3/2}}-12\frac{z}{2\sqrt{-s}}\bigr)=z^3+6sz$; directo: $z^3+s\cdot6z$ ✓.
- $n=4$ (no pedido por el doc, lo añado): directo $e^{s\partial^2}z^4=z^4+12sz^2+12s^2$; fórmula con $H_4=16x^4-48x^2+12$: $s^2\bigl[16\frac{z^4}{16s^2}\bigr]=z^4$; $(-s)^2(-48)\bigl(\frac{-z^2}{4s}\bigr)=12sz^2$; $12s^2$ ✓. Coincidencia exacta.

Ceros $z=x_0+2i\sqrt\sigma\,h_j$ ✓ ($w=(z-x_0)/(2i\sqrt\sigma)$). Verificación cruzada de momentos: $\frac{d}{d\sigma}\sum z_k^2=-2n(n-1)$ por la simetrización $\frac{z_k}{z_k-z_j}+\frac{z_j}{z_j-z_k}=1$ ✓; en el modelo $\sum z_j^2=-4\sigma\sum h_j^2$ y $\sum h_j^2=n(n-1)/2$ (de $H_n=2^nx^n-n(n-1)2^{n-2}x^{n-2}+\cdots$, $e_1=0$, $\sum h^2=-2e_2$; chequeo $H_4$: $n(n-1)2^{n-2}=48$ ✓; chequeo $H_3$: ceros $0,\pm\sqrt{3/2}$, suma $3=3\cdot2/2$ ✓) ⟹ $-2n(n-1)\sigma$ ✓. Consistencia perfecta.

### 2.2. [§1.2] Tabla y asintótica — **CERTIFICADO**

- $c(2)$: $H_2$ ceros $\pm1/\sqrt2$, $4\cdot\frac12=2$ ✓.
- $c(3)$: $h_{\max}^2=3/2$, $c=6$ ✓.
- $c(4)$: $16x^4-48x^2+12=0\iff4x^4-12x^2+3=0\iff x^2=\frac{3\pm\sqrt6}2$; $c(4)=4\cdot\frac{3+\sqrt6}2=2(3+\sqrt6)\approx10.899$ ✓.
- $c(5)$: $32x^4-160x^2+120=0\iff4x^4-20x^2+15=0\iff x^2=\frac{5\pm\sqrt{10}}2$; $c(5)=2(5+\sqrt{10})\approx16.32$ ✓.
- Asintótica: $h_{\max}^2=(2n+1)-2^{2/3}|a_1|(2n+1)^{1/3}+O(1)$ ⟹ $c(n)=8n+4-2^{8/3}|a_1|(2n+1)^{1/3}+O(n^{-1/3})$ ✓ (el factor $2^{8/3}=4\cdot2\cdot2^{-1/3}$ verificado). Cota $c(n)\le8n+4$ de $h_{\max}<\sqrt{2n+1}$ (clásica) ✓.

**[PROP 177.2]** (refutación de la constante $2k$ del GAP-174.B): consecuencia inmediata de la tabla, ambas lecturas de $k$ tratadas honestamente. **CERTIFICADO.** La heurística del Doc 174 §2.3(b) muere correctamente.

### 2.3. [PROP 177.3] Modelo con resto — **CERTIFICADO-CON-RESERVA**

La prueba es un esquema (Rouché + representación gaussiana). Los ingredientes son estándar y la lógica correcta, pero: la separación de los ceros de Hermite reescalados en el *bulk* es $\asymp\sqrt\sigma/\sqrt n$, no $\sqrt\sigma$ — el documento lo reconoce entre paréntesis ("salvo el factor de densidad local del semicírculo") sin propagar ese factor a la constante del desplazamiento. Para la cantidad que se usa aguas abajo ($\beta_{\max}$, ceros del borde, separación $\asymp\sqrt\sigma\,n^{-1/6}$) la pérdida es polinomial en $n$ y queda absorbida si $\sqrt{n\sigma}/d$ es pequeño con margen polinomial. Reserva: el enunciado tal cual ($O(\sqrt{n\sigma}\cdot\sqrt{n\sigma}/d)$ uniforme en $j$) no está probado para el bulk con esa constante. No se usa cuantitativamente en 177.6–177.8 (que van por la vía término a término), así que la reserva no propaga.

### 2.4. [LEMA 177.4] Cota del mar — **CERTIFICADO** (suma dentro/fuera de la ventana $|x-\alpha|\le\beta$ reconstruida: $\rho\beta$ términos de tamaño $\le1/\beta$ más cola integrable ⟹ $C\rho$ uniforme ✓; convergencia absoluta bajo RvM ✓).

### 2.5. [PROP 177.5] Cuarteto apilado — **CERTIFICADO**

Reconstrucción: con $w_i=-\beta_i^2$ raíces de $X^2+aX+c$: $S=\beta_1^2+\beta_2^2=a$, $P=c$. Backward ($\sigma$): $a'=12$, $c'=2a$ ⟹ $S'=12$, $P'=2S$ ✓; $P=P_0+2S_0\sigma+12\sigma^2$ ✓; $(S^2-4P)'=24S-8S=16S>0$ ✓ (no fusión en altura); asintótica $S\sim12\sigma$, $P\sim12\sigma^2$, $\sqrt{S^2-4P}\sim4\sqrt6\,\sigma$, $\beta_2^2\sim(6+2\sqrt6)\sigma=c(4)\sigma$ ✓ — la saturación exacta de la ley de Hermite del cluster fusionado es un chequeo de consistencia notable y pasa. Cota $\beta_2^2\le S\le S_0+12\sigma$ trivial de $P\ge0$ ✓. Fracciones de "robo" $(6\pm2\sqrt6)/12$ ✓.

### 2.6. [THM 177.6] Cota global $2n^2\sigma$ — **CERTIFICADO-CON-ERRATA** (E-186.2, constante conservadora)

Bloques reconstruidos:
1. Conjugado propio: $4\beta_k\cdot2\beta_k/(4\beta_k^2)=2$ por modo superior ⟹ $2\kappa_W$ ✓.
2. Cruzados: por par no ordenado $(k,l)$, simetrizando sobre denominadores idénticos: numeradores $(\beta_k-\beta_l)^2$ y $(\beta_k+\beta_l)^2$, cada uno $\le d^2$ porque $|z_k-z_l|\ge|\beta_k-\beta_l|$ y $|z_k-\bar z_l|\ge\beta_k+\beta_l$ (la distancia compleja domina la componente vertical — correcto tal como está escrito). Con el factor $4$: $\le8$ por par no ordenado ⟹ total $\le8\cdot\binom{\kappa_W}2=4\kappa_W(\kappa_W-1)$. **El documento escribe $8\kappa_W(\kappa_W-1)$: factor 2 de holgura** (cuenta pares ordenados). Como es cota superior, el teorema sigue siendo válido; la suma interna real es $\le2\kappa_W(2\kappa_W+2r_W-1)$, mejor que la anunciada. Errata inofensiva en la dirección segura.
3. Reales: $4\beta_k^2/|z_k-x|^2\le4$ ✓ ($|z_k-x|\ge\beta_k$); total $\le4\kappa_Wr_W$ ✓.
4. Aritmética final: $2\kappa(1+4\kappa-4+2r)=2\kappa(4\kappa+2r-3)$ ✓; con $n=2\kappa+r$: $4\kappa+2r-3=2n-3$ exacto ✓; $2\kappa(2n-3)\le n(2n-3)\le2n^2$ ✓.
5. Exterior vía Lema 177.4 + Cauchy–Schwarz ✓; Grönwall con término multiplicativo pequeño: estándar ✓.

Calibración contra el monomio ($dI_W/d\sigma=n(n-1)$ exacto: mitad superior de $2n(n-1)$... verificado: $I_W=\sum_{\beta>0}\beta^2=-\frac12\operatorname{Re}\sum z_j^2$ en el caso vertical puro, $\frac{d}{d\sigma}=n(n-1)$ ✓): factor $\approx2$ de holgura en energía, como afirma. ✓

### 2.7. [THM 177.7] Aterrizajes en la esquina — **CERTIFICADO-CON-ERRATA** (E-186.3, condicional al Lema 177.B)

**Lógica de la contradicción (los dos casos):** si $\gamma_c\ge\Gamma(t_c)$ entonces, como $\Gamma$ decrece en $t$, $\gamma_c\ge\Gamma(t_c+\delta)$ para todo $\delta>0$ y el Lema 177.B se aplica al gap recién nacido en $t_c+\delta$: $C\sqrt\delta\log\gamma_c\ge c\,(t_c+\delta)^\theta\ge c\,t_c^\theta$. Tomando $\delta\to0^+$ el lado izquierdo $\to0$: contradicción. Luego $\gamma_c<\Gamma(t_c)$. **Correcta**, incluida la nota de signo (el lema prohíbe gaps pequeños *encima* de $\Gamma$; el aterrizaje los crea; ergo el aterrizaje vive *debajo*). La dirección del pliegue se usa como cota superior del gap ($g\le C\sqrt\delta$, de la forma normal), que es la dirección que se necesita. La frase intermedia con $\delta=t_c$ es un rodeo innecesario pero no falso.

**Álgebra de exponentes en (2), reconstruida:**
- $\gamma_j\le\exp(t_j^{-(1/2-\theta)})$ ⟹ $t_j\le(\log\gamma_j)^{-2/(1-2\theta)}$ ✓.
- **E-186.3:** el documento escribe "$n_j\le C\rho(\gamma_j)\sqrt{n_jt_j}$ ... i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$". Resolver la autoconsistencia da $\sqrt{n_j}\le C\rho\sqrt{t_j}$, es decir $\boxed{n_j\le C^2\rho^2t_j=C\,t_j\log^2\gamma_j}$ — **no** $C\sqrt{t_j}\log\gamma_j$. El "i.e." es falso como implicación directa. **Sin embargo**, en el régimen impuesto por la cadena, $x:=t_j\log^2\gamma_j\le(\log\gamma_j)^{2-2/(1-2\theta)}<1$ (pues $2/(1-2\theta)>2$), y para $x<1$ se tiene $x\le\sqrt x$, luego la cota escrita es *más débil que la correcta* y por tanto válida a posteriori. Con la cota correcta el resultado mejora: $n_j\le\max(2,Ct_j\log^2\gamma_j)=2$ eventualmente ⟹ $b_j^2\le Ct_j\le C(\log\gamma_j)^{-2/(1-2\theta)}$ ⟹ $b_j\le(\log\gamma_j)^{-1-\eta'}$ con $\eta'=\frac{2\theta}{1-2\theta}>0$. Con la cadena tal como está escrita: $b_j^2\le Ct_j^2\log^2\gamma_j\le C(\log\gamma_j)^{2-4/(1-2\theta)}$, exponente $<-2$ para $\theta<\frac12$ ⟹ $b_j\le(\log\gamma_j)^{-1-\eta}$, $\eta=\frac{4\theta}{1-2\theta}>0$ ✓. **La conclusión cualitativa ($b_j\le(\log\gamma_j)^{-1-\eta}$, $\eta>0$) es correcta por ambas rutas**; la errata afecta el valor de $\eta$ y la prolijidad del paso, no el teorema.
- La validez del rango del mar lejano ($t_j\ll(n_j\log^2\gamma_j)^{-1}$) garantizada a posteriori por la cadena: con $n_j\le2$ y $t_j\log^2\gamma_j\to0$, ✓.
- $m=\infty$ + KKL ⟹ $t_j\to0^+$; alturas acotadas solo albergan finitos cuádruplos ✓.

**Estatus condicional honesto:** el Lema 177.B está declarado como GAP de literatura no probado, y la plausibilidad difusiva ($\Gamma(t)=\exp(t^{-(1/2-\theta)})<\exp(t^{-1/2})$ = el lado donde el calor ya actuó) es razonable pero no es prueba. Correctamente etiquetado.

### 2.8. [COR 177.8] — **CERTIFICADO** (condicional a 177.B ∧ LP-134; la implicación lógica es inmediata del Thm 177.7(2) y es válida). La doble consistencia contra el contraejemplo de Hadamard verificada: $b_j=e^{-\gamma_j}$ viola LP-134 ($b_j\log\gamma_j\to0$) y sus aterrizajes ($t_j\approx e^{-2^{j+1}}/2$, $\gamma_j=2^j$) están astronómicamente por debajo de $\Gamma(t_j)$ — el corte es limpio y ninguna de las dos hipótesis es redundante ✓.

### 2.9. [THM 177.10] Huérfanos — **CERTIFICADO-CON-RESERVA**

(1) y (3) son aplicación directa de 177.6 + superaditividad de §2.2 (verificada: $G(n)=2n^2$ y $G=c(n)$ superaditivas ✓; el pegado monótono en fusiones es correcto). (2): $M(t)\ge M(0)+2|t|\ge b_{\max}^2$ vía Lema 174.3 backward ✓; el portador de $M$ es huérfano cuando $|t|<b_{\max}^2/(4n(t)^2)$ ✓. **Reserva estructural (no errata):** todo el teorema es condicional a la "hipótesis de separación a escala corriente" en $(t,0)$, que no está probada para ninguna configuración concreta y que en el régimen denso de ζ ($n(t)\asymp\rho\sqrt{|t|}$ crece) es exactamente lo difícil. El documento lo declara; la ventana de detección $|t|\lesssim\min(b_{\max}^2,\rho^{-2})$ es no vacía pero su no-vacuidad útil depende de $b_{\max}$ vs $\rho^{-1}$ — para la patología de la esquina del propio Thm 177.7 ($b\le(\log\gamma)^{-1-\eta}\ll\rho^{-1}$) la ventana es minúscula y el censo backward inoperante en la práctica. Consistente con la conclusión del doc de que la ruta forward es la buena.

---

## 3. Clasificación estructural (orden del director)

Pregunta clave: ¿el aparato dinámico produce información que NO sea reformulación de "los ceros off existen/no existen"?

| Pieza | Clase | ζ-libre | Comentario |
|---|---|---|---|
| Thm 174.2 + Lema 174.3 (coercividad, máximo) | **COERCIVO** | sí | Desigualdades genuinas, pero ζ-libres ⟹ por §3.3 no pueden decidir RH solas |
| Thm 174.8 (presupuesto $\sum\ell\le I/4$) | **COERCIVO** | sí | Conversión energía↔vidas real; mismo límite |
| Thm 174.10 (jerarquía $D_{2n}\ge0$) | **COERCIVO** | sí | Sano; su corolario virial intermedio cayó |
| Cor 174.11(2) (familia virial) | **REDUNDANTE** (tras degradación) | sí | Versión superviviente trivial módulo banda; extremos ya conocidos |
| Thm 174.4 / Prop 174.1 / Cálc 174.6 | **COERCIVO** (modelos exactos) | sí | Calibran constantes; el contenido es de modelo |
| Thm 174.5(3) ("RH vive en $t\le0$") | **CORRELACIONAL** | sí | Reformulación: re-localiza la dicotomía, no la reduce |
| §2.3(c) (transporte de la dicotomía) | **CORRELACIONAL** | — | El propio doc lo admite: el backward computa $I(0)$ |
| Prop 174.7 (red punto fijo) | **MIXTO** | sí | Coercivo en sí; su *lectura* (fluctuaciones de gaps = puerta aritmética) es el contenido correlacional valioso |
| §3.3 (refutación soldadura) | **COERCIVO-NEGATIVO** | sí | Cierre con contraejemplo; load-bearing, verificado |
| Thm 177.1/177.5, tabla $c(n)$ | **COERCIVO** (modelo exacto) | sí | Matemática nueva-para-el-programa, impecable |
| Thm 177.6 (cota $2n^2\sigma$) | **COERCIVO** | sí | El teorema técnico central de D177 |
| Thm 177.10 (huérfanos) | **CORRELACIONAL** | sí | Es la *definición* dinámica de ¬RH-finito; no añade información, organiza |
| Thm 177.7 + Cor 177.8 | **MIXTO** | **no** | **La única pieza del bloque que produce información no-reformulativa**: confinamiento cuantitativo de la patología ($\gamma$ superexponencial, $b\le(\log\gamma)^{-1-\eta}$) condicional a 177.B; la soldadura 177.B∧LP-134⟹$m<\infty$ reduce el input aritmético a una sola repulsión |

**Respuesta a la pregunta del director:** todo lo incondicional de D174/D177 es ζ-libre y, por el contraejemplo del §3.3 (verificado), **incapaz por construcción de decidir RH**: es geometría de la clase. El valor no-reformulativo del bloque se concentra en un único punto: el par (Lema 177.B, LP-134) como hipótesis mínimas separadas — la dinámica redujo el *tamaño* del input aritmético necesario, que es progreso real aunque condicional. El resto del aparato coercivo (presupuestos, jerarquías, viriales) acota *cuánto* viven los ceros off si existen, nunca *si* existen: correlación con la dicotomía, no resolución.

---

## 4. Tabla de veredictos

| Resultado | Veredicto |
|---|---|
| Prop 174.1 (no-coercividad $D\ge cI$) | **CERTIFICADO** |
| Thm 174.2 (coercividad $\dot I\le-2I/M\le-2I$) | **CERTIFICADO-CON-ERRATA** (E-186.4, redacción) |
| Lema 174.3 (principio del máximo) | **CERTIFICADO** |
| Thm 174.4 ($t_c$ exacto del cuádruplo) | **CERTIFICADO** (expansión y signo verificados) |
| Thm 174.5 (forward cerrado) | **CERTIFICADO** |
| Cálc 174.6 / Prop 174.7 | **CERTIFICADO** |
| Thm 174.8 (presupuesto $\sum\ell_j\le I(0^+)/4$) | **CERTIFICADO** (solape: la identidad lo cuenta exactamente) |
| Cálc 174.9 (clusters) | sin etiqueta de teorema; heurística admisible |
| Thm 174.10 (jerarquía, $D_{2n}\ge0$ ∀n) | **CERTIFICADO** (la simetrización escala: monotonía de $x^{2n-1}$, no cuadrados) |
| Cor 174.11(1) (decaimiento $e^{-2nt}$) | **CERTIFICADO** |
| **Cor 174.11(2) (familia virial $2^{1+1/n}$)** | **REFUTADO en su prueba / DEGRADADO** (E-186.1: media de potencias invertida; sobrevive $\Lambda\le t_0+I_{2n}^{1/n}/2$, trivial, + extremos $n=1,\infty$) |
| Prop 174.12 (entropía) | **CERTIFICADO** (condicional declarado) |
| §3.3 refutación "$I<\infty\Rightarrow m<\infty$" en clase | **CERTIFICADO** (las tres verificaciones del mandato pasan) |
| Thm 177.1 (Hermite exacto) + tabla §1.2 | **CERTIFICADO** ($n=2,3,4$, momentos, $c(2..5)$, asintótica: todo verificado a mano) |
| Prop 177.2 (refutación de $2k$) | **CERTIFICADO** |
| Prop 177.3 (modelo con resto) | **CERTIFICADO-CON-RESERVA** (esquema; separación bulk no propagada; no usado aguas abajo) |
| Lema 177.4 (mar) | **CERTIFICADO** |
| Prop 177.5 (cuarteto apilado) | **CERTIFICADO** (satura $c(4)\sigma$: chequeo de consistencia fuerte, pasa) |
| Thm 177.6 (cota $2n^2\sigma$) | **CERTIFICADO-CON-ERRATA** (E-186.2: cruzados $\le4\kappa(\kappa-1)$, el doc escribe $8\kappa(\kappa-1)$ — holgura, dirección segura) |
| Thm 177.7 (esquina) | **CERTIFICADO-CON-ERRATA** (E-186.3: paso "$n_j\le C\sqrt{t_j}\log\gamma_j$" mal derivado pero válido a posteriori; conclusión y $\eta>0$ correctos; condicional a 177.B) |
| Cor 177.8 (177.B ∧ LP-134 ⟹ $m<\infty$) | **CERTIFICADO** (condicional; implicación válida; doble consistencia verificada) |
| Thm 177.10 (huérfanos) | **CERTIFICADO-CON-RESERVA** (hipótesis de separación no probada; ventana de detección minúscula en el régimen relevante) |

## 5. Erratas

- **E-186.1 (Cor 174.11(2), GRAVE):** la prueba invoca "monotonía de medias de potencias" en la dirección inversa: lo cierto es $(I_{2n-2}/\kappa)^{1/(n-1)}\le(I_{2n}/\kappa)^{1/n}$, i.e. $I_{2n-2}\le\kappa^{1/n}I_{2n}^{(n-1)/n}$, lo opuesto de lo usado. La EDO $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ falla para perfiles con un par dominante. La familia virial $\Lambda\le t_0+I_{2n}^{1/n}/2^{1+1/n}$ queda sin prueba para $2\le n<\infty$; corregir el Doc 174 §4.2 y su Veredicto ("interpola exactamente" ⟶ "los extremos son teoremas; el interior, abierto").
- **E-186.2 (Thm 177.6, menor):** la cota de cruzados correcta es $4\kappa_W(\kappa_W-1)$ (pares no ordenados), no $8\kappa_W(\kappa_W-1)$; el teorema mejora a $2\kappa_W(2\kappa_W+2r_W-1)$, sigue $\le2n^2$.
- **E-186.3 (Thm 177.7(2), menor):** "$n_j\le C\rho\sqrt{n_jt_j}$ i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$" — la resolución correcta es $n_j\le C\rho^2t_j=Ct_j\log^2\gamma_j$; la forma escrita solo vale a posteriori en el régimen $t_j\log^2\gamma_j<1$. Con la forma correcta, $\eta$ mejora a $2\theta/(1-2\theta)$ y de hecho $n_j\le2$ eventualmente. Conclusión intacta.
- **E-186.4 (Thm 174.2, redacción):** "extinción lineal exacta" debería ser "cota lineal de extinción".

## 6. Impacto aguas abajo

- **Caída de Cor 174.11(2):** afecta solo a la narrativa "una sola familia interpolante" (citada en el veredicto de D174 y en el resumen de fase como "jerarquía de momentos interpola de Bruijn ($n=\infty$)"). **Nada técnico cuelga de los $n$ intermedios**: D176 y D177 usan $n=1$ (presupuesto/virial de energía) y $n=\infty$ (banda), ambos intactos. Corregir la memoria de fase: la interpolación es conjetural, los extremos son teoremas.
- **177.7/177.8 (alimentan la torre 2 vía D178/179): SOBREVIVEN.** Las erratas E-186.2/3 no tocan la conclusión $b_j\le(\log\gamma_j)^{-1-\eta}$ ni la soldadura 177.B∧LP-134⟹$m<\infty$. La segunda torre sigue en pie con su estatus condicional declarado (177.B abierto, LP-134 conjetural).
- **§3.3 (Hadamard fluye) verificado:** todas las "imposibilidades ζ-libres" del programa que se apoyan en él (D176, la doble consistencia de D177, la arquitectura de dos torres) conservan su soporte.
- **Thm 174.10 ($D_{2n}\ge0$) certificado:** disponible como herramienta; pero nótese que tras la caída del virial intermedio, su único consumidor no trivial hoy es Cor 174.11(1).

**Balance de la auditoría:** 1 refutación de prueba con degradación (Cor 174.11(2)), 2 certificados-con-reserva, 4 erratas; el núcleo de ambos documentos (174.2/3/4/8/10, §3.3, 177.1/5/6/7/8) resiste la reconstrucción término a término. Tasa de bajas dentro del patrón histórico (~1/4 contando el corolario estrella).
