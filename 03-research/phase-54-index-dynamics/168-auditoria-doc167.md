# Documento 168 — Auditoría adversarial del Doc 167 (dinámica del índice κ)

**Programa:** Hipótesis de Riemann — Fase 54
**Fecha:** 2026-06-10
**Objeto:** Doc 167 completo, con re-derivación cerrada de cada pieza load-bearing. Sin numéricos. Protocolo: matar por (i) parámetros tratados como constantes, (ii) cláusulas de excepción no verificadas, (iii) intercambios suma/derivada, (iv) cuantificadores, (v) constantes exponenciales.

---

## 0. Veredicto por pieza

| Pieza | Veredicto | Daño |
|---|---|---|
| **(a) Thm 2.3, ley İ = −2κ − D, D ≥ 0** | **SOBREVIVE** (re-derivada término a término; signo de D hermético; verificada exactamente en modelo cerrado) | ninguno en el núcleo |
| **(b) Thm 1.4, κ = grado; muros; pliegue** | **SOBREVIVE pero deflacionario** — es principio del argumento + Hurwitz sobre rectángulo compacto; "topológico" es empaquetado, no potencia nueva. "Codimensión 1" de los muros: decorativo, sin estructura de variedad probada | menor |
| **(c) Prop 3.2 + GAP 167.A** | **TOCADO** — KKL verificado ✓; Prop 3.2.1 con hueco en t→0⁺ (entrada desde Re→∞ no excluida); la separación 3.2.3 cita un contraejemplo que **no satisface Def 1.1.3** tal como está (reparable); la afirmación "lado promedio" es esperanza no sustanciada y contradicha por el propio §5.1 del doc | medio |
| **(d) Corolarios** | **Cor 2.4: constante final FALSA** (κ(0)/16 → κ(0)/4; mezcla de normalizaciones, modo de fallo (i)). **Cor 2.5: cláusula de excepción FALSA/no justificada** (caso I<∞, κ=∞; modo de fallo (ii)) — la desigualdad incondicional I(t) ≥ 4\|t\| **no está probada**. La tabla ζ-libre del §5: honesta y correcta | grave en (d), pero reparable en parte |

---

## 1. La dinámica de ceros (Lema 2.1): verificada, con sus hipótesis exactas

**Re-derivación.** Con la normalización de Polymath 15, $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$ satisface $\partial_t H_t = -\partial_z^2 H_t$ (derivar bajo la integral es legítimo: el integrando decae superexponencialmente). En un cero simple $z_k(t)$, la función implícita da $\dot z_k = -\partial_t H/\partial_z H = \partial_z^2 H/\partial_z H$ evaluado en $z_k$. Para $H$ entera de orden 1, **par y real**, Hadamard da $H(z)=cz^q\prod_j(1-z^2/z_j^2)$ — **sin factor $e^{bz}$** (paridad), como afirma el doc. Escribiendo $H=(z-z_k)g$: $H''/H'(z_k)=2g'(z_k)/g(z_k)=2\sum'_{j\ne k}(z_k-z_j)^{-1}$ con la suma **emparejada** $z_j\leftrightarrow -z_j$ (cada par lejano contribuye $O(|z_j|^{-2})$, absolutamente sumable por densidad tipo RvM). Esto coincide con [RT §2] y [P15].

**Punto crítico del protocolo (intercambio suma/derivada e Im de la suma condicional).** La parte **real** de la velocidad es solo condicionalmente convergente (requiere el emparejamiento simétrico — correcto en el doc). Pero la parte **imaginaria**, que es lo único que entra en İ, es
$$\operatorname{Im}\frac{1}{z_k-w} = -\frac{\beta_k-\operatorname{Im}w}{|z_k-w|^2},$$
y para $w=x_j$ real lejano esto es $-\beta_k/|z_k-x_j|^2 = O(x_j^{-2})$: la serie de $\dot\beta_k$ es **absolutamente convergente sin emparejamiento**. No hay intercambio ilegítimo escondido en la parte imaginaria. *Este punto, que era el candidato a fallo (i)/(iii), aguanta.*

**Hipótesis exactas bajo las que vale:** (1) ceros simples en el instante considerado; (2) densidad $\sum_j|z_j|^{-2}<\infty$; (3) nada más. Vale igual para ceros complejos aislados (holomorfía + función implícita), incluido $t<\Lambda$. Para $t>0$ las hipótesis las da [KKL] salvo en instantes de colisión; la **finitud local de los instantes de colisión** no está en [KKL] — el doc la afirma de pasada (Lema 2.1, final). Es plausible (analiticidad conjunta de $H_t(z)$ en $(t,z)$ + κ entero no-creciente acota los aterrizajes por $\kappa(t_0)/2$; las colisiones real–real se excluyen por repulsión, §2 abajo), pero el argumento de analiticidad conjunta **no está escrito** en el doc. Flag menor: la cadena lógica es reconstruible, no presente.

**Verificación en modelo cerrado** (control independiente de signos y normalización): $H_t(z)=z^2+c_0-2t$ satisface $\partial_tH=-\partial_z^2H$. Para $c_0>0$: par en $\pm i\beta$, $\beta^2=c_0-2t$; aterrizaje en $t_c=c_0/2$; después, ceros reales $\pm\sqrt{2t-c_0}$. Dinámica: $\dot z_1 = 2/(z_1-z_2)$ ✓ exacto. Y con $I=\beta^2$, $\kappa=1$: $\dot I = -2 = -2\kappa$, $D=0$ ✓ exacto. La Prop 2.6 ($\beta^2 = 2(t_c-t)$) se realiza con igualdad. **La tasa −2 por modo es correcta.**

---

## 2. La ley de balance (Thm 2.3): re-derivación completa — el signo de D es hermético

$\dot\beta_k = -2\sum_{w\ne z_k}\dfrac{\beta_k-\operatorname{Im}w}{|z_k-w|^2}$, $\dot I = \sum_{k\,\text{sup}}2\beta_k\dot\beta_k$ (suma **finita** bajo la hipótesis $\kappa<\infty$ del teorema: no hay intercambio $\sum$/$d_t$ que justificar — el doc enuncia el teorema exactamente en el dominio donde la operación es trivialmente legítima; bien).

Clasificación de $w$, verificada término a término:

1. **$w=\bar z_k$:** $\operatorname{Im}w=-\beta_k$; término $\beta_k\cdot 2\beta_k/|2i\beta_k|^2 = 1/2$; contribución $-4\cdot\tfrac12 = \mathbf{-2}$ por cero superior. **Total $-2\kappa$. Verificado** (y confirmado por el modelo cerrado §1). El factor exacto es $-2$, no depende de la posición.
2. **$w=-\bar z_k$:** $\operatorname{Im}w=+\beta_k$ ⟹ contribución $0$ ✓.
3. **$w=-z_k$:** $\beta_k(2\beta_k)/4|z_k|^2$ ⟹ contribución $-2\beta_k^2/|z_k|^2\le 0$ ✓.
4. **$w=x_j$ real:** contribución $-4\beta_k^2/|z_k-x_j|^2\le0$, serie absolutamente convergente (RvM) ✓.
5. **Términos cruzados entre cuádruplos distintos — el punto de muerte previsto (análogo GAP-B).** Aquí busqué el fallo con intención y **no existe**, por una razón estructural que el doc usa sin subrayar: tras simetrizar $(k,l)+(l,k)$, los dos términos de cada pareja comparten **exactamente el mismo denominador**:
 - $w=z_l$ visto desde $z_k$: denominador $|z_k-z_l|$; $w=z_k$ desde $z_l$: $|z_l-z_k|$ — **idénticos** ⟹ $\beta_k(\beta_k-\beta_l)+\beta_l(\beta_l-\beta_k) = (\beta_k-\beta_l)^2 \ge 0$ sobre el denominador común.
 - $w=\bar z_l$ desde $z_k$: $|z_k-\bar z_l|$; $w=\bar z_k$ desde $z_l$: $|z_l-\bar z_k| = |\overline{z_l-\bar z_k}| = |\bar z_l - z_k|$ — **idénticos** ⟹ $(\beta_k+\beta_l)^2\ge0$.
 - Análogo para $-\bar z_l$ ($|z_k+\bar z_l|=|z_l+\bar z_k|$) y $-z_l$ ($|z_k+z_l|$).

 Si los denominadores no coincidieran, la agrupación dejaría residuos de signo libre y la "disipación" sería falsa — es la simetría de conjugación la que cierra el signo, no una elección de agrupamiento del autor. **D ≥ 0 es término a término genuino.** La contabilidad de factores ($-4$ sobre pares no ordenados $=$ $-2$ sobre ordenados; $-2\beta_k^2/|z_k|^2 = -4\beta_k^2\cdot\frac{1}{2|z_k|^2}$) cuadra con la fórmula del enunciado.

**Veredicto (a): TEOREMA 2.3 CERTIFICADO** en su dominio enunciado ($t$ en un intervalo con $\kappa$ finito constante y ceros simples). Adicional no señalado por el doc: la ley es **invariante de escala** ($z\to\lambda z$, $t\to\lambda^2 t$ deja $\dot I$ y $-2\kappa$ invariantes), lo que la protege del problema de normalización que sí mata constantes en los corolarios (§3). "No hay término fuente" es correcto: la suma se agota en las 5 categorías, sin resto.

---

## 3. Dominio de validez: aquí están las dos muertes

### 3.1. [MUERTE PARCIAL — Cor 2.5] La cláusula de excepción "si κ o I son infinitos, vale trivialmente" es falsa tal como está

Cor 2.5 afirma $I(t)\ge 4|t|$ para todo $t<0$, vía: (caso 1) dinámica bien definida y κ finito en $(t,0)$ ⟹ Thm 2.3 + κ≥2 ⟹ ✓; (caso 2) "si κ o I son infinitos en $(t,0)$ la conclusión vale trivialmente". El caso 2 cubre $I(t)=\infty$ (trivial ✓) y $\kappa=\infty$ en medida positiva **si la forma integral de la ley valiera ahí** — pero **no vale**: el Thm 2.3 está enunciado y probado solo para $\kappa<\infty$. El caso no cubierto es exactamente:

> $I(u)<\infty$ para todo $u\in(t,0)$ pero $\kappa(u)=\infty$ — **posible** en la clase analítica (es la configuración tipo Hadamard del Doc 144: $\sum\beta_j^2<\infty$ con infinitos pares).

En ese caso no se puede concluir nada con lo probado: (α) $\dot I=\sum 2\beta_k\dot\beta_k$ es ahora una serie infinita y el intercambio $d_t/\sum$ requiere convergencia uniforme no establecida (modo de fallo (iii), ahora sí presente); (β) el rescate por truncación a $N$ cuádruplos **rompe el signo de D**: los términos cruzados entre los $N$ elegidos y el resto quedan sin pareja simetrizante, y son de signo libre — exactamente el mecanismo GAP-B del Doc 139. Tampoco hay resultado tipo [KKL] para $t<0$ que excluya $\kappa=\infty$ (KKL es solo $t>0$).

**Consecuencia:** la desigualdad incondicional $I(t)\ge4|t|$, y con ella la mitad cuantitativa del eslogan "RH ⟺ despegue con pendiente mínima cuantizada 4", **no está probada**. Lo que sobrevive: (i) la versión condicional (κ finito y ceros a.e. simples en $(t,0)$); (ii) la equivalencia **RH ⟺ $I(0^+)=0$**, que solo usa el lado $t>0$ (KKL + monotonía + Hurwitz en $t=0$) y está sana. **Reparación posible:** o un lema de truncación con control de cruzados vía la banda decreciente de de Bruijn (Thm 13 de [dB], que da $\beta_k(u)^2 \le \beta_k(t)^2 - 2(u-t)$ ... cuidado: ese teorema controla el **sup**, no la suma), o extender el Thm 2.3 a $\kappa=\infty$, $I<\infty$ probando convergencia absoluta de todos los bloques bajo $\sum\beta_l^2<\infty$ + RvM — plausible (los bloques cruzados están dominados por $\sum_l(\beta_k^2+\beta_l^2)/|z_k-\bar z_l|^2$, sumable salvo control de mínimos de gaps) pero **es un lema nuevo, no un trivialmente**.

### 3.2. [MUERTE de constante — Cor 2.4] Mezcla de normalizaciones: el modo de fallo (i) textual

El doc fija la normalización P15: $H_0(z)=\tfrac18\,\Xi(z/2)$ (línea de §0.1, y es la de [RT]/[P15], verificado). Entonces **los ceros de $H_0$ son los de $\Xi$ dilatados por 2**: la banda es $|\operatorname{Im}z|<\mathbf{1}$, **no** $1/2$. (Consistencia externa: el teorema de banda de de Bruijn — zeros en $|\operatorname{Im}|\le\Delta$ ⟹ en $|\operatorname{Im}|\le\sqrt{\Delta^2-2t}$ — da $\Lambda\le\Delta^2/2 = 1/2$ exactamente con $\Delta=1$ ✓; con $\Delta=1/2$ daría $\Lambda\le1/8$, falso conocido. Además la literatura registra $\Lambda=4\lambda(0)$ entre normalizaciones — el factor 4 en $t$ es real.)

Consecuencias:
- **Cor 2.4 final:** "$\Lambda\le \kappa(0)/16$, usando $\beta\le1/2$" es **falso en la normalización declarada**: ahí $\sup\beta<1$ y la cadena da $\Lambda\le I(0^+)/4 \le \kappa(0)/4$. (En coordenadas $\Xi$ con su tiempo propio $t_\Xi=t_H/4$ el /16 sería correcto — pero entonces $\Lambda_\Xi\ne\Lambda$ y todos los valores citados en §0.1 cambian.) La parte $\Lambda\le t_0+I(t_0)/4$ es coherente **si** $I$ se mide sobre $Z(H_t)$; el deslizamiento ocurre solo al meter "β ≤ 1/2".
- **Def 1.1 (𝒞):** con banda $|\operatorname{Im}z|\le1/2$ y densidad $N_Z(T)=\frac{T}{\pi}\log\frac{T}{2\pi e}+O(\log T)$, que es la de $\Xi$ — **$Z_t = Z(H_t)\notin\mathcal{C}$ literalmente** (banda 1, densidad $\frac{T}{2\pi}\log\frac{T}{4\pi e}$). El Thm 1.4 y el Thm 2.3 no usan los valores exactos (solo $\sum|z|^{-2}<\infty$ y banda acotada), así que **ningún teorema muere por esto**, pero el documento es internamente inconsistente y la inconsistencia ya cobró una constante (el /16). La ley İ = −2κ − D sobrevive por ser invariante de escala; las constantes no lo son.

### 3.3. Convergencia de I y enunciado del dominio

El Thm 2.3 está correctamente confinado a κ<∞: **no** hay deslizamiento de dominio dentro del teorema mismo. El deslizamiento está en los corolarios: Cor 2.5 lo usa donde κ<∞ es exactamente lo no sabido ($t<0$, y $t\to0^+$ con $m=\infty$ posible). Prop 3.2.2 ($I(0^+)<\infty \iff \int_0^s[2\kappa+D]\,du<\infty$) es correcta para el lado $t>0$ (κ(u)<∞ por KKL; $I$ monótona; convergencia monótona para pasar al límite $t\to0^+$), **módulo** la finitud local de colisiones de §1 (reconstruible). El detalle "κ(t)≥2 por paridad" en Cor 2.4/2.5 requiere evitar $W_{\mathrm{Sieg}}$, que el doc solo discute en $t=0$; **se cierra en una línea que el doc no escribió**: $H_t(i\beta)=\int_0^\infty e^{tu^2}\Phi(u)\cosh(\beta u)\,du>0$ porque $\Phi>0$ — el flujo real **nunca** toca el eje imaginario, para ningún $t$. (Regalo de la auditoría: este lema sella la paridad a lo largo de todo el flujo.)

---

## 4. κ como grado (Thm 1.4) y los muros: correcto, deflacionario

- **¿Grado bien definido sobre borde no compacto?** No surge: el rectángulo $R$ es **compacto**, y la hipótesis conjunta (camino propio + κ<∞) coloca todos los ceros superiores en un compacto fijo. La preocupación del protocolo (densidad log T en altura infinita) está desactivada **por hipótesis, no por teorema** — el contenido real de "propio" es asumir que no pasa lo que habría que excluir. El doc es honesto al respecto (§1.1, "hipótesis honesta mínima"), y para el flujo DBN con κ<∞ en intervalos compactos de $(0,\infty)$ la propiedad se sigue de velocidad $O(\log T)$ a altura $T$ (sub-lineal: sin escape/entrada en tiempo finito) — argumento esbozado, válido.
- **¿"Topológico" añade algo?** No en potencia demostrativa: (3) es el principio del argumento, (1) es Hurwitz, (2) es contar. Es una **reformulación correcta**; su valor es organizativo (identifica los dos únicos modos de cambio de κ). El doc lo medio-admite ("la discretitud es barata", §4a). El salto $\mp2$ está bien: el aterrizaje en $x_0$ y su espejo $-x_0$ son simultáneos por paridad de $F$, cada uno resta 1 al conteo superior ✓; el caso "par aterriza sobre un cero real simple preexistente" da multiplicidad ≥3, sigue siendo $W_{\mathrm{col}}$ ✓.
- **Pliegue (Prop 1.6):** Weierstrass + discriminante + transversalidad asumida — correcto y estándar; es la fórmula cuadrática. La conexión con CSV94 es de inspiración, no de dependencia: CSV94 da cotas inferiores de Λ desde pares de Lehmer; la forma normal aquí es autocontenida. El "Lehmer = 2 es el grado del discriminante": consistente con Prop 2.6 (verificada exactamente en el modelo cerrado, §1).
- **Decorativo sin prueba:** "codimensión 1" de $W_{\mathrm{col}}$ (𝒞 no tiene estructura de variedad establecida). No se usa de forma load-bearing. Y la frase "κ clasifica las componentes conexas..." es tautológica tal como está formulada.

---

## 5. GAP 167.A: la separación y el test del "lado promedio"

### 5.1. La separación $I(0^+)<\infty \subsetneq \kappa(0)<\infty$: esencialmente correcta, con un defecto citacional reparable

El contraejemplo real del Doc 141.R2/144 tiene $\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$ (no el $\min(1/4,\,1/(j\,a(2^j)))$ de versiones posteriores; ambos son $\ell^2$). $\sum_j\delta_j^2<\infty$ trivialmente con $m=\infty$: la separación **como configuraciones** es correcta. **Pero:** tal como está construido (ceros reales $t_n=n/\log(n+2)$), su conteo es $N_F(T)\asymp T\log T$ **solo a orden de magnitud** — la Def 1.1.3 del Doc 167 exige el asintótico RvM exacto $\frac{T}{\pi}\log\frac{T}{2\pi e}+O(\log T)$, que la construcción **no** verifica (constante distinta, error no controlado a $O(\log T)$). El contraejemplo, citado contra la Def 1.1 del Doc 167, **no está en 𝒞**. Reparación trivial: tomar como $t_n$ la solución de $\frac{t}{\pi}\log\frac{t}{2\pi e}=n$ (mismo argumento de convergencia, género y orden). Reparable en cinco líneas, pero la cadena citacional tal como está es inválida — tercer ejemplar del patrón "parámetros tratados como si encajaran". ¿Entra al flujo DBN? Sí en el sentido relevante: $e^{-t\partial_z^2}$ actúa sobre enteras de orden $<2$ (la serie $\sum(-t)^nF^{(2n)}/n!$ converge), de modo que la jerarquía de Prop 3.2 es una jerarquía del flujo y no solo estática.

### 5.2. ¿Es $I(0^+)$ visible para las estadísticas verticales? — el test que la sesión predijo

Análisis cerrado. Un cuádruplo $\{\gamma\pm ib,\,-\gamma\pm ib\}$ (coordenada $\Xi$) contribuye a un funcional de fórmula explícita con test par $h$:
$$h(\gamma+ib)+h(\gamma-ib) = 2h(\gamma) + b^2 h''(\gamma) + O(b^4).$$
Conclusión de dos filos:
1. **A primer orden, invisible** — es el no-go 141.B2: la señal lineal en $b$ se cancela. Las estadísticas verticales clásicas (correlación de pares, momentos de $S(t)$, densidades) operan a este orden: **ciegas a $I$**.
2. **A segundo orden, $I$ es exactamente lo que aparece**: $\sum_j b_j^2\,h''(\gamma_j)$. Esto es estructuralmente notable (es la traza cuadrática del exponente Lehmer = 2, y es donde vive la positividad de Weil), y distingue a $I$ de las cantidades lineales que murieron en Phase 46. **Pero no la hace certificable**: (α) el término cuadrático viene **ponderado** por $h''(\gamma_j)$, con $h$ decayente y $h''$ sin signo — extraer $\sum b_j^2$ sin peso es imposible con tests admisibles; (β) está sumergido en el término principal $\sum 2h(\gamma_j)$ sobre TODOS los ceros, conocido solo a error mucho mayor que $b_j^2$ (que puede ser sub-resolución, $e^{-\gamma_j}$); (γ) acotar $\int_0^s\kappa(u)\,du$ exige acotar el número de ceros no reales de $H_u$ cerca de $u=0$ — un problema de densidad de ceros off para la deformación, para el que no existe herramienta de promedio. Y el propio Doc 167 §5 matiz 1 localiza el muro en "momento firmado → momento cuadrático": **esa frase aplica literalmente a GAP 167.A**. La etiqueta "del lado promedio del cuantificador maestro" describe la **forma sintáctica** del enunciado ($\ell^2$, suma, sin sup), no una accesibilidad real con las herramientas existentes.

**Veredicto GAP 167.A:** separación válida (tras reparar la cita), objetivo bien nombrado y genuinamente más débil que $m<\infty$; la esperanza de atacabilidad por promedios queda **degradada de afirmación a deseo**, con tensión interna del doc (GAP 167.A vs §5.1). El único matiz a favor: $I$ es de segundo orden, no de primer orden — es la primera cantidad del programa cuya invisibilidad NO se sigue del mecanismo de integral-cero de 141.B2; su inaccesibilidad viene del peso y de la sub-resolución, un muro distinto y honestamente más débil. Eso merece quedar registrado.

---

## 6. Ki–Kim–Lee: VERIFICADO

Verificación externa (Polymath wiki; survey AMS Bulletin de Newman–Wu tipo "Constants of de Bruijn–Newman type"; blog de Tao; Wikipedia): Ki–Kim–Lee, *On the de Bruijn–Newman constant*, Adv. Math. **222** (2009) 281–306, prueba (1) $\Lambda<1/2$ y (2) **para cada $\lambda>0$, todos los ceros de $\Xi_\lambda$ salvo un número finito son reales y simples** (paso clave: para todo $\lambda,\varepsilon$, los ceros con parte real fuera de la zona crítica tienen altura acotada). La atribución del Doc 167 (§0.1 y Prop 3.1: para todo $t>0$, finitos ceros no reales, casi todos reales y simples, **incondicionalmente**) es **correcta**. Dos precisiones que el Doc 167 no carga sobre KKL pero conviene fijar: (a) KKL **no** da finitud local de instantes de colisión en $t$ (eso hay que derivarlo, §1); (b) KKL es solo $t>0$ — nada para $t<0$, que es donde Cor 2.5 lo necesitaría (§3.1). Nota de normalización: en la literatura coexisten normalizaciones con $\Lambda=4\lambda(0)$; los valores citados en §0.1 del Doc 167 ($\le\tfrac12$, $<\tfrac12$, $\ge0$, $\le0.22$) son los de la normalización $H_t$ estándar, consistentes entre sí — la inconsistencia del doc no está en §0.1 sino entre §0.1 y la Def 1.1/Cor 2.4 (§3.2).

Fuentes de la verificación: [Polymath wiki — De Bruijn-Newman constant](https://michaelnielsen.org/polymath/index.php?title=De_Bruijn-Newman_constant), [Tao, "The De Bruijn-Newman constant is non-negative"](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/), [Rodgers–Tao, arXiv:1801.05914](https://arxiv.org/pdf/1801.05914), [KKL en ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001870809001133), [Wikipedia — de Bruijn–Newman constant](https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant).

---

## 7. Lista de reparaciones exigidas (en orden de gravedad)

1. **Cor 2.5:** restringir el enunciado a su versión condicional (κ<∞ y ceros a.e. simples en $(t,0)$), o probar el lema de extensión del Thm 2.3 a $\kappa=\infty,\ I<\infty$ (convergencia absoluta de los bloques cruzados bajo $\ell^2$ + RvM + cota inferior de gaps — **lema nuevo, no trivial**, y nótese que sin cota inferior de gaps locales los denominadores $|z_k-z_l|$ pueden arruinar la sumabilidad). Re-etiquetar "RH ⟺ despegue con pendiente mínima" como condicional.
2. **Cor 2.4:** corregir $\kappa(0)/16 \to \kappa(0)/4$ (normalización P15, $\sup\beta<1$), o re-coordinatizar todo el doc en variable $\Xi$ con el tiempo reescalado y valores de Λ divididos por 4 — elegir UNA carta.
3. **Def 1.1:** banda $\le 1$ y densidad $N_Z(T)=\frac{T}{2\pi}\log\frac{T}{4\pi e}+O(\log T)$ si la carta es la de $H_t$ (los teoremas no cambian; las constantes sí).
4. **Prop 3.2.3:** reconstruir el contraejemplo de Hadamard con $t_n$ = puntos RvM exactos para que esté en 𝒞.
5. **Lema 2.1 / Prop 3.2.2:** escribir el argumento de finitud local de colisiones (analiticidad conjunta + κ no-creciente + repulsión real–real: $\dot g = 4/g + O(\log T)$ ⟹ $g$ no puede anularse hacia delante).
6. **Añadir el lema regalo:** $H_t>0$ en el eje imaginario para todo $t$ (positividad de $\Phi$ y $\cosh$) — sella $W_{\mathrm{Sieg}}$ y la paridad κ≥2 en todo el flujo, cerrando el hueco de Cor 2.4/2.5 en ese punto.
7. **GAP 167.A:** rebajar "del lado promedio" a [DESEO] y registrar el hecho nuevo real: $I$ es la primera cantidad de segundo orden del programa — escapa al no-go de integral-cero (141.B2) pero choca con el muro peso/sub-resolución.

---

## 8. Veredicto final

- **(a) Thm 2.3 — CERTIFICADO.** La re-derivación completa confirma $\dot I=-2\kappa-D$ con $D\ge0$ término a término; el signo de D está protegido por la coincidencia exacta de denominadores bajo conjugación (no por agrupamiento discrecional); la tasa $-2$ por modo se verifica con igualdad en el modelo cerrado $z^2+c_0-2t$; la parte imaginaria de la dinámica es absolutamente convergente (sin intercambio ilegítimo). Es el teorema más sólido que esta fase ha producido, y es genuinamente ζ-libre.
- **(b) Thm 1.4 — CORRECTO, deflacionario.** Principio del argumento + Hurwitz sobre compacto; la no-compacidad de la banda se evita por hipótesis ("propio" + κ<∞), no por teorema. Pliegue correcto. Sin potencia nueva, organización buena.
- **(c) Prop 3.2 + GAP 167.A — TOCADO, reparable.** KKL verificado; hueco en t→0⁺ (3.2.1, entrada desde el infinito); contraejemplo citado fuera de 𝒞 (reparable); "lado promedio" no sustanciado y en tensión con el propio §5.1 del doc.
- **(d) Corolarios — DOS BAJAS.** Cor 2.4: constante final falsa por mezcla de normalizaciones ($/16\to/4$). Cor 2.5: cláusula de excepción no verificada — la versión incondicional de $I(t)\ge4|t|$ no está probada; sobrevive la condicional y RH ⟺ $I(0^+)=0$. La tabla de circularidad del §5 es honesta.

**Tres hallazgos:**
1. **[KILL parcial] La cláusula de excepción de Cor 2.5 es falsa en el caso $I<\infty,\ \kappa=\infty$** (posible por Hadamard): ahí el Thm 2.3 no aplica, el intercambio $d_t/\sum$ no está justificado y la truncación rompe el signo de D por términos cruzados sin pareja (mecanismo GAP-B). Modo de fallo histórico (ii)+(iii), localizado en una sola frase ("vale trivialmente").
2. **[KILL de constante] Mezcla de cartas $\Xi$/$H_t$:** en la normalización P15 declarada, los ceros de $H_0$ viven en banda $|\operatorname{Im}z|<1$ (no $1/2$) con densidad $\frac{T}{2\pi}\log\frac{T}{4\pi e}$; Cor 2.4 da $\Lambda\le\kappa(0)/4$, no $\kappa(0)/16$, y $Z_t\notin\mathcal{C}$ literalmente. La ley İ=−2κ−D sobrevive por invariancia de escala; las constantes no.
3. **[Hallazgo estructural a favor] $I$ es la primera cantidad de segundo orden del programa:** su huella en la fórmula explícita es $\sum_j b_j^2 h''(\gamma_j)$, que **escapa** al no-go de integral-cero 141.B2 (ese mata el primer orden); su inaccesibilidad actual es por peso $h''$ + sub-resolución, un muro distinto y a priori más débil. Eso, junto con el lema regalo $H_t|_{i\mathbb{R}}>0$ (paridad sellada en todo el flujo), es lo aprovechable de esta auditoría.
