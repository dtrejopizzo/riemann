# Documento 185 — Auditoría adversarial de los Documentos 173 y 176 (Green–Littlewood, el límite de Cesàro, A ⟹ Lindelöf, la barrera de densidades)

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Objetos:** Doc 173 (`173-representacion-de-I.md`) y Doc 176 (`176-ataque-A-green-littlewood.md`), leídos completos, línea por línea.
**Método:** reconstrucción independiente de cada prueba ANTES de leer la del documento; verificación de constantes y factores; clasificación estructural por orden del director.
**Convenciones verificadas:** ambos docs usan $I(T)=E(T)=\sum_{\gamma_j\le T}b_j^2$, un representante por cuádruplo, $b\in(0,\tfrac12)$, $\gamma>0$. La convención es **consistente entre 173, 175, 176** y con el conteo del paso (3) de la prueba de 173.C (ver §1.3 abajo: el cuádruplo aporta exactamente $b^2$ al rectángulo simétrico, es decir $b^2/2$ por cada uno de los dos miembros con $\beta>\tfrac12$, $|\gamma|<T$). ✓

---

## 0. Veredicto ejecutivo

| Resultado | Veredicto |
|---|---|
| [Thm 173.C] Green–Littlewood | **CERTIFICADO** (con observaciones O-1, O-2) |
| [Thm 173.A] sombra–señal | **CERTIFICADO** |
| [Lema 173.B] rigidez de Stieltjes | **CERTIFICADO** |
| [Prop 173.D] clase $X_2$ | CERTIFICADO (nivel de rigor: esquema correcto, tecnicismos de holomorfía débil no explicitados — aceptable por contrato) |
| [Prop 173.E] dicotomía de Dirichlet | **CERTIFICADO** |
| [Prop 173.Cr] Cramér | CERTIFICADO (trivial) |
| [Prop 176.1] región $\sigma\ge1$ | **CERTIFICADO** |
| [Lema 176.2] integrabilidad local | **CERTIFICADO** |
| [Lema 176.3] $\Xi(T)\ll\log T$ | **CERTIFICADO** (mejora real de 173.C) |
| [Thm 176.4] límite de Cesàro | **CERTIFICADO** (el punto delicado del borde está bien resuelto; ver §2.2) |
| [Cor 176.5] cota inferior | CERTIFICADO (consecuencia inmediata) |
| [Thm 176.6] teorema inverso | **CERTIFICADO-CON-ERRATA** (E-185.1, inocua) |
| [Thm 176.7] A ⟹ Lindelöf | **CERTIFICADO** (la cita de Backlund es correcta; ver §3) |
| [Prop 176.8] layer-cake / GAP-A | **CERTIFICADO** |
| [Prop 176.9] barrera | **CERTIFICADO-CON-ERRATA** (E-185.2 en el punto 4, menor) |
| [Cor 176.10] dicotomía de medias | CERTIFICADO condicional (hereda LP-112, declarado) |

**Nada cae. Ningún resultado se degrada en enunciado.** Dos erratas de constante (una en un enunciado auxiliar de 176, una en la configuración de saturación de 176.9.4), ninguna load-bearing. La crítica seria es **estructural**, no de corrección: 173.C y 176.4 son cambio de moneda (§5).

---

## 1. [TEOREMA 173.C] — la identidad de Green–Littlewood

### 1.1. Reconstrucción independiente (hecha antes de leer la prueba del doc)

Sea $u=\log|\zeta|$, $v=\tfrac12(\sigma-\tfrac12)^2$ (nota: $\Delta v=\partial_\sigma^2 v=1$ ✓, $v$ no depende de $t$). En el rectángulo **simétrico** $R=[\tfrac12,A]\times[-T,T]$, $\Delta u=2\pi\big(\sum_{\text{ceros}}\delta_\rho-\delta_1\big)$ como distribución (los ceros triviales están en $\sigma<0$, fuera; el polo $s=1$ es **interior** a $R$ porque $-T<0<T$ — punto importante: en el rectángulo simétrico no hay polo en el borde). Green:
$$\iint_R u\cdot 1-2\pi\Big[\sum_{\rho\in R^\circ,\beta>1/2}v(\rho)-v(1)\Big]=\oint_{\partial R}(u\,\partial_nv-v\,\partial_nu).$$
Conteo: de cada cuádruplo con $\gamma<T$, los miembros con $\beta>\tfrac12$ en $R$ son $\tfrac12+b\pm i\gamma$ (dos), cada uno con $v=b^2/2$: total $b^2$ por cuádruplo ⟹ $\sum v(\rho)=I(T)$ con la convención "una vez por cuádruplo". ✓ $v(1)=\tfrac12\cdot\tfrac14=\tfrac18$ ✓ — **el $+1/8$ es exactamente el polo evaluado en el peso cuadrático**, no $\int_{1/2}^1(1-\sigma)d\sigma$ (esa es la forma en que reaparece en la prueba alternativa; ambas dan $1/8$, ver §1.2).
Bordes: $\sigma=\tfrac12$: $v=v'=0$, nada (y los ceros en línea caen ahí con $v=0$: tratados consistentemente). $\sigma=A\to\infty$: $|u|,|u_\sigma|\ll2^{-\sigma}$ contra $v\ll\sigma^2$: cero. $t=\pm T$: $\partial_nv=0$; queda $-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$ por la simetría $u(\sigma,-t)=u(\sigma,t)$. Con $\partial_tu=-\mathrm{Im}\,\zeta'/\zeta$ y $\iint_R u=2D(T)$:
$$2D(T)-2\pi I(T)+\tfrac\pi4=\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma
\;\Longrightarrow\;I(T)=\tfrac1\pi D(T)+\tfrac18-\Xi(T).$$
**Coincide exactamente con el boxed del doc, factores $\pi$, $2$ y signo incluidos.** ✓

**Verificación diferencial adicional (mía, no está en el doc):** derivando la identidad en $T$ (a.e.): $0=\tfrac1\pi\int u(\sigma,T)d\sigma-\Xi'(T)$, y $\partial_T\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}=\mathrm{Re}\,(\zeta'/\zeta)'=\partial_\sigma^2u$; integrando por partes dos veces $\tfrac1{2\pi}\int(\sigma-\tfrac12)^2u_{\sigma\sigma}=\tfrac1\pi\int u$ (los bordes mueren: $v=v'=0$ en $\tfrac12$, decaimiento en $\infty$). La identidad es auto-consistente término a término. ✓

### 1.2. Las "dos pruebas independientes" y el chequeo $T\to0$

- **Prueba principal (Green):** completa y correcta (§1.1). El paso (1) (descomposición local $u=\sum\log|s-\rho|-\log|s-1|+h$, $h$ armónica) es legítimo: $h=\log|\zeta\cdot(s-1)/\prod(s-\rho)|$ con el cociente holomorfo sin ceros en un entorno simplemente conexo del rectángulo. El paso (2) (Green por piezas, ceros de borde excluidos por "$T$ no ordenada") es el tratamiento clásico del potencial. ✓
- **Cross-check (Littlewood iterado):** es un **esquema de una línea, no una segunda prueba completa** (el display contiene literalmente "$\dots$"). Lo reconstruí: Littlewood en rectángulo simétrico da $\int_0^T\log|\zeta(\sigma_0+it)|dt=2\pi\sum_{\beta>\sigma_0,0<\gamma<T}(\beta-\sigma_0)-\pi(1-\sigma_0)+O(\log T)$ — **polo con factor $\pi$, no $2\pi$** (la suma de ceros se duplica por conjugación al plegar $|t|<T$ a $0<t<T$; el polo, que está en $t=0$, no se duplica). Integrando en $\sigma_0\in[\tfrac12,\infty)$: $\sum_j\int_{1/2}^{\beta_j}(\beta_j-\sigma_0)d\sigma_0=\sum b_j^2/2$ por cero superior $=\sum_jb_j^2/2$... con un cero por cuádruplo en $0<\gamma<T$ esto da $2\pi\cdot\tfrac{I}{2}=\pi I$ ✓, y el polo $\int_{1/2}^1\pi(1-\sigma_0)d\sigma_0=\pi/8$ ✓. La aritmética del doc ("$+\tfrac18$ reaparece como $\frac1\pi\int\pi(1-\sigma_0)d\sigma_0$") usa la constante **correcta** $\pi(1-\sigma_0)$. Coincide con Green. ✓ (Contraste con Doc 176 §1.2 — errata E-185.1, ver §4.)
- **Chequeo $T\to0^+$:** $\mathrm{Im}\,\zeta'/\zeta(\sigma+iT)\to$ masa $\pi\delta_{\sigma=1}$ (del polo, $\mathrm{Im}[-1/(\sigma-1+iT)]=T/((\sigma-1)^2+T^2)$, núcleo de Poisson de masa $\pi$ en la semirrecta); flujo $\to-\tfrac1{2\pi}\cdot\tfrac14\cdot\pi=-\tfrac18$, cancela el $+\tfrac18$, $I(0)=0$. ✓ Verificado.

### 1.3. Truncamiento en $T$ y ceros cercanos al corte

Pregunta obligada: ¿los ceros con $\gamma$ cerca de $T$ contribuyen "parcialmente"? **No hay contribución parcial de átomos**: con $T$ no-ordenada, cada cero está estrictamente dentro o fuera de $R$ y aporta $v(\rho)$ entero o nada — la suma es exactamente $I(T)=\sum_{\gamma\le T}b^2$ sin peso de truncamiento. La influencia de los ceros cercanos al corte vive **íntegramente en el flujo $\Xi(T)$** (que por eso explota cerca de ordenadas y solo es $O(\log^2T)$ en alturas buenas en 173.C). El doc lo maneja correctamente y no lo barre; la existencia de alturas buenas en $[n,n+1]$ ($O(\log n)$ ordenadas ⟹ huecos $\gg1/\log n$) es correcta. ✓

**Veredicto 173.C: CERTIFICADO.**
Observaciones: **O-1**: el "cross-check independiente" es un esquema verificable, no una prueba completa autocontenida; la afirmación de "dos pruebas" es generosa pero el esquema reconstruye sin sorpresas. **O-2**: la cota del flujo $O(\log^2T)$/alturas buenas queda obsoleta por [Lema 176.3] ($O(\log T)$, toda altura) — no es error, es mejora posterior.

---

## 2. Documento 176: el límite de Cesàro y la maquinaria

### 2.1. [Prop 176.1], [Lema 176.2], [Lema 176.3]

- **176.1:** reconstruido: $\int_0^T\cos(t\log n)dt=\sin(T\log n)/\log n$, $\int_1^\infty n^{-\sigma}d\sigma=1/(n\log n)$, producto $\Lambda(n)\sin(T\log n)/(n\log^3n)$ ✓; Tonelli justificado por $\sum\Lambda(n)/(n\log^2n)<\infty$ ✓. Los tres ingredientes de la "lectura" (media cero, frecuencias $\ge\log2$, amplitudes $\ell^1$) son exactamente lo que la prueba usa. **CERTIFICADO.**
- **176.2:** factorización local estándar (Titchmarsh §3.9) + singularidad logarítmica integrable + $O(\log T)$ ceros. Válido para **toda** $T$, ordenada o no — esto es lo que carga el peso en 176.4. **CERTIFICADO.**
- **176.3:** el truco es real y lo verifiqué: $\int_{1/2}^2(\sigma-\tfrac12)^2\big|\mathrm{Im}\tfrac1{\sigma+iT-\rho}\big|d\sigma\le\tfrac94\int_{\mathbb R}\tfrac{|T-\gamma|dx}{x^2+(T-\gamma)^2}=\tfrac{9\pi}4$, masa de Poisson **independiente de $|T-\gamma|$** — la integración previa en $\sigma$ elimina la necesidad de altura buena. $(\sigma-\tfrac12)^2\le\tfrac94$ en $[\tfrac12,2]$ ✓; $O(\log T)$ ceros con $|\gamma-T|\le1$ ✓; resto de fracciones parciales y cola $\sigma\ge2$ ✓. **CERTIFICADO. Mejora estricta genuina de 173.C.**

### 2.2. [TEOREMA 176.4] — el punto más delicado de la auditoría

**El riesgo señalado en el mandato** (el borde de Littlewood en altura $T$ involucra $\int\log|\zeta(\sigma+iT)|d\sigma$, NO acotado uniformemente cerca de ordenadas) **está correctamente neutralizado**, y por la vía honesta:

1. El FTC vertical $\int_{T_0}^{2T_0}\mathrm{Im}\tfrac{\zeta'}{\zeta}(\sigma+iT)dT=\log|\zeta(\sigma+iT_0)|-\log|\zeta(\sigma+2iT_0)|$ vale para toda abscisa $\sigma$ que no porte un cero en el segmento (todas salvo numerables); las singularidades logarítmicas son integrables y la continuidad absoluta a trozos basta. ✓
2. El intercambio Fubini $\int dT\int d\sigma$ está justificado: $|\zeta'/\zeta|\sim|s-\rho|^{-1}$ es **localmente integrable en 2D** (no en 1D — exactamente por eso el promediado doma lo que la altura individual no). ✓
3. Crucial: la cota final usa [Lema 176.2] **en las dos alturas $T_0$, $2T_0$ sin asumir que sean buenas** — si hay un cero con ordenada exactamente $T_0$, la singularidad en $\sigma=\beta$ es logarítmica e integrable en $\sigma$. El doc NO asume "alturas buenas" donde no puede. ✓
4. Detalle que verifiqué y el doc no necesita explicitar: en una ordenada exacta $T=\gamma$, $\mathrm{Im}\tfrac1{\sigma-\beta+i\cdot0}=0$ para $\sigma\ne\beta$ — $\Xi$ no tiene singularidad no-integrable en $T$; la integral $\int\Xi\,dT$ está bien definida. ✓

**(b):** $I(T_0)\le\overline I(T_0)\le I(2T_0)$ por monotonía, válido también con $I(0^+)=\infty$ (el Cesàro diverge **limpiamente a $+\infty$**, sin oscilación: la monotonía de $I$ más el error $O(\log T_0/T_0)$ lo fuerzan). ✓
**(c):** "límite $=-\pi/8\Rightarrow$ RH": requiere positividad estricta de un solo cuádruplo — un cero off tiene $b>0$ estrictamente, luego $b^2>0$ y $I(0^+)>0$. Trivial pero correcto; verificado. ✓

**Veredicto 176.4: CERTIFICADO.** Es el resultado técnico central del documento y resiste el ataque dirigido del mandato.

### 2.3. [Cor 176.5], [Thm 176.6], [Cor 176.10]

176.5: inmediato de $I\ge0$ + 176.3/176.4. ✓ 176.6: (a) = 176.3.1 + 170.5 ✓; (b) Chebyshev $b\le b^2/s$ si $b>s$ ✓; usa el Littlewood por abscisa de §1.2 — la errata E-185.1 del polo vive dentro de $O(1)\subset O(\log T)$, inocua aquí. La declaración de honestidad ("nuevo de enunciado, no de método", GAP de folklore declarado) es ejemplar. **CERTIFICADO-CON-ERRATA.** 176.10: condicional limpio a LP-112, herencia declarada. ✓

---

## 3. [TEOREMA 176.7] — A ⟹ Lindelöf (la calibración load-bearing)

Reconstrucción independiente, idéntica a la del doc:
1. $I<\infty\Rightarrow N(\tfrac12+s,\infty)\le I/s^2<\infty$ para todo $s>0$ (Chebyshev sobre $b^2\ge s^2$). **Más fuerte que lo necesario**: para cada $\sigma>\tfrac12$ solo hay **finitos** ceros a la derecha en total.
2. Por tanto $N(\sigma,T+1)-N(\sigma,T)\to0$ ($T\to\infty$) para cada $\sigma>\tfrac12$ fijo — de hecho es eventualmente $0$.
3. Criterio de Backlund: **LH $\iff$ para todo $\sigma>\tfrac12$, $N(\sigma,T+1)-N(\sigma,T)=o(\log T)$.** Verifiqué la cita: es la equivalencia clásica de Backlund (1918–19), tal como está en Titchmarsh cap. XIII (§13.5, donde se prueba la equivalencia en ambas direcciones — sí es equivalencia, no solo implicación). La dirección que se usa aquí (conteo $o(\log T)\Rightarrow$ LH) es la dirección probada por Backlund vía Hadamard tres círculos/Borel–Carathéodory. La cita es correcta y la versión citada es la que se necesita.
4. $\to0$ es mucho más fuerte que $o(\log T)$ ⟹ LH. $\square$

**Veredicto 176.7: CERTIFICADO.** Sin reservas. Nota del auditor: el doc incluso infraexplota su paso 1 — bajo A, *todo* semiplano $\sigma\ge\tfrac12+s$ contiene finitos ceros; A es "quasi-RH" en un sentido más fuerte del que la cadena necesita. La autoevaluación "trivial una vez dicha, nueva como observación del programa" es honesta. La cadena RH⟹$m<\infty$⟹A⟹LH⟹DH: cada flecha verificada (la última es Ingham 1940 ✓); "estricta" se usa en el sentido de "recíprocos no conocidos", declarado en §4.1 ✓.

---

## 4. [PROP 176.9] — la barrera, y las erratas

**La integral:** $\int_0^{1/2}s\,e^{-cs\log T}ds\le\int_0^\infty s\,e^{-cs\log T}ds=(c\log T)^{-2}$ ✓ ($\Gamma(2)=1$). Layer-cake exacto de 176.8(a) verificado ($b^2=\int_0^b2s\,ds$ + Tonelli ✓). Conclusión $E(T)\le\tfrac{2C}{c^2}T(\log T)^{\kappa-2}$ ✓; **$c$ solo entra en la constante** ✓ (la forma del techo la fija $\kappa$); Selberg $c=\tfrac14,\kappa=1\Rightarrow T/\log T$ ✓ — coherencia con 170.5 verificada. Punto 3 (LH/Halász–Turán vacíos en $s\asymp1/\log T$, donde $T^{-cs}\asymp1$): correcto, es la observación de masa fatal. **¿Formulación honesta?** Sí: está explícitamente enmarcada como barrera del **conducto densidad→energía** ("no puede dar menos sin nueva información en $s\asymp1/\log T$"), no del enunciado A — el layer-cake usa la densidad como única información, y eso está dicho.

**Errata menor (E-185.2):** en el punto 4, la verificación de consistencia de la configuración saturada afirma "$T^{1-cs}\log T=e^{-c}T\log T\le N(T)$ para $\kappa\le1$" en $s=1/\log T$: con $N(T)\sim\tfrac{T}{2\pi}\log T$ esto requiere $e^{-c}\le\tfrac1{2\pi}$, falso para $c$ pequeño (p.ej. Selberg $c=\tfrac14$). Se repara trivialmente insertando una constante pequeña en la configuración ($N\asymp\epsilon\,T^{1-cs}\log T$), que no altera la conclusión $E(T)\asymp_\epsilon T/\log T$. La optimalidad sobrevive; solo la línea de consistencia es descuidada.

**Veredicto 176.9: CERTIFICADO-CON-ERRATA (E-185.2).**

**ERRATA PRINCIPAL (E-185.1), Doc 176 §1.2:** el "Lema de Littlewood por abscisa" se enuncia con término del polo $-2\pi(1-\sigma)$. **La constante correcta es $-\pi(1-\sigma)$** (reconstrucción §1.2 de este doc: al plegar el rectángulo simétrico de $|t|<T$ a $0<t<T$, los ceros se duplican por conjugación pero el polo en $t=0$ no; equivalentemente, Doc 173 §6.1 usa $\pi(1-\sigma_0)$ y obtiene el $1/8$ correcto — los dos documentos se contradicen entre sí en esta constante, y 173 tiene razón). Impacto: solo el display de cota inferior de §1.2 y la prueba de 176.6(b), donde el polo es $O(1)$ absorbido en $O(\log T)$: **ningún teorema afectado**. Si la constante $2\pi$ fuera la correcta, el cross-check de 173.C daría $1/4$ en vez de $1/8$ y contradiría la prueba de Green — no es el caso.

---

## 5. Auditoría de 173.A, 173.B, 173.D, 173.E (punto 5 del mandato)

- **[Thm 173.A]:** Lema 173.0 verificado (Taylor par en $b$; $\varphi''(t)=-\Phi''(\tfrac12+it)$ por $i^2=-1$ ✓; resto $b^4/6$ ✓; cross-check con la resolvente §2.1: $(1-12\gamma^2)/a^3$ recomputado, coincide ✓). (b): $w\ge0\Rightarrow\varphi_r$ cóncava; el argumento de exclusión de $\varphi_r'<0$ y la evaluación $\int w=2\varphi_r'(0)$ correctos. (c): la IBP y $X\varphi_r'(X)\le2\int_{X/2}^X\varphi_r'\to0$ correctos. (d): correcto (concavidad localizada + real-analiticidad de $\varphi_r$). **CERTIFICADO.** Es el teorema de obstrucción con contenido real del Doc 173.
- **[Lema 173.B]:** verificado paso a paso: $\partial_a[a/(a^2+t^2)]=(t^2-a^2)/(a^2+t^2)^2$ ✓ (signo correcto en el doc); bordes de la IBP mueren ✓; el cambio $u=a^2$ da exactamente $\tfrac12m'(\sqrt u)/(u+t^2)$ ✓; la hipótesis $\int(1+a)|m'|<\infty$ es precisamente lo que hace de $g\,du$ medida finita para Widder ✓. La ilustración beta: $\int_0^\infty x^4/(1+x^2)^4=\int x^2/(1+x^2)^4=\pi/32$ (verificado por la simetría $x\mapsto1/x$), $\int(1+x^2)^{-4}=5\pi/32$, $1-6+5=0$ ✓. **CERTIFICADO.**
- **[Prop 173.D]:** el esquema (paridad ⟹ sin término lineal; coeficiente de $b^2$ acoplado a $F_0$; autónomo $=O((\sum b^2)^2)$) es correcto tal como está probado; los tecnicismos de holomorfía débil en $\mathcal H$ no se detallan pero el contrato lo permite y nada posterior carga sobre ellos. El diagnóstico estructural (3) — "$I=\|F\|^2$ exige romper la paridad del cuádruplo = operación no holomorfa" — es la mejor frase del documento y es correcta. **CERTIFICADO** (nivel esquema-riguroso).
- **[Prop 173.E]:** la dirección RH ⟹ $\tilde d\equiv0$ trivial; la divergencia con un átomo ($\int_0^{r_0}2\pi r\,dr/r^2=\infty$) correcta; la acotación local de la serie restante usa $E(T)\ll T/\log T$ — plausible y suficiente para convergencia local uniforme de armónicas (que controla gradientes). **CERTIFICADO.** La "obstrucción de atomicidad" (lineal-en-medida vs cuadrático-en-campo) es un diagnóstico correcto y honesto de por qué $I\ne\|F\|^2$ aquí.
- **Anti-circularidad:** ninguno de los dos documentos asume RH, Lindelöf ni LP-112 fuera de los resultados marcados condicionales (176.10). Los inputs son Hadamard, Littlewood, Selberg, Backlund, von Mangoldt — todos incondicionales y backward. Sin circularidad detectada. ✓

---

## 6. Clasificación estructural (orden del director)

| Resultado | Clase | Justificación despiadada |
|---|---|---|
| 173.A + 173.B + 173.D | **COERCIVO-negativo** (no-go) | Excluyen una clase de representaciones. Contenido real: explican el techo 172.9 sin ventanas. No acercan a RH; cierran puertas con prueba. |
| 173.C | **REDUNDANTE con valor cartográfico** | Identidad exacta = **cambio de moneda**. Los dos lados ($\sum b^2$ y $\iint\log\|\zeta\|$) son *el mismo objeto* por Green; ninguno es más blando que el otro — controlar $\iint\log\|\zeta\|$ hasta $O(1)$ en la banda ES controlar los ceros (y el propio programa lo confirmó después: 180.4, colapso de la ruta integral). Lo que NO es redundante: la taxonomía $m=0,1,2$ de momentos transversales y la identificación de las dos operaciones no-holomorfas (parte real + medio cuádruplo) — eso es cartografía genuina del muro. Pero como *ruta hacia A*, es una reformulación local de A. |
| 173.E | **REDUNDANTE-degenerado** (declarado por el propio doc) | "RH = pertenencia" con norma $\{0,\infty\}$: la dicotomía atómica vacía el contenido. El doc lo dice; el auditor confirma. |
| 176.1–176.3, 176.5, 176.6 | **CORRELACIONAL** (tipo A, segundo orden fino) | Control técnico incondicional del integrando/borde. 176.3 es la pieza técnica más valiosa del par de documentos. |
| 176.4 | **REDUNDANTE con mejora técnica real** | "A ⟺ límite finito de algo que siempre existe" es repackaging de A — el límite *es* $\pi I-\pi/8$ por construcción, la moneda no cambió de dificultad. La mejora real y no redundante: la **eliminación incondicional del borde** ($O(\log T_0/T_0)$, sin alturas buenas) — eso es teorema técnico, no tautología. Pero la frase "A queda convertido" sobrevende: A queda *reescrito*. |
| 176.7 | **MIXTO — puente genuino. El único calibrador real del par.** | Conecta dos enunciados de dificultad heterogénea (A, nodo nuevo; LH, nodo clásico) con prueba completa. Establece "A es Lindelöf-difícil": la única información de *posición* nueva y exportable. Sí: **176.7 es el único resultado con contenido calibrador genuino**, respuesta directa a la pregunta del director. |
| 176.8 | **REDUNDANTE útil** | Repackaging exacto de A (layer-cake); su valor es nombrar GAP-A con precisión. |
| 176.9 | **COERCIVO-negativo** | Barrera del método, honesta, con la cuenta exacta. Junto con 176.7 forma el verdadero entregable del Doc 176: A está *entre* $m<\infty$ y LH, y el conducto de densidades *no llega*. |

**Juicio sobre la pregunta central:** 173.C y 176.4 son identidades, no puentes: igualan dos descripciones del mismo objeto sin que ningún lado sea más tratable (el muro de la banda $\tfrac12<\sigma\le1$ reaparece intacto en §6.2 de 173 — el propio doc lo admite en la forma "campo de primos"). El paquete que sobrevive como progreso es: **obstrucción probada (173.A) + posición probada (176.7 + 176.9)**. Eso es cartografía coerciva del muro, no avance hacia su cruce — y está declarado con honestidad inusual en ambos documentos.

---

## 7. Impacto en la arquitectura

- **Nada cae**: la representación de I (173.C) y la reformulación de A (176.4) quedan certificadas; la arquitectura RH ⟸ A ∧ LP-112 (175) no sufre.
- **La posición de A se consolida**: la cadena RH ⟹ $m<\infty$ ⟹ A ⟹ LH ⟹ DH queda auditada flecha a flecha; "A es Lindelöf-difícil" es ahora un hecho certificado del programa, utilizable como calibración en fases posteriores.
- **Advertencia estructural**: dado que 173.C/176.4 son cambio de moneda, todo plan que ataque A "por el lado integral" (acotar $\overline D$ superiormente) debe declarar de dónde saldrá información que no sea de ceros — la barrera 176.9 más el colapso posterior (180.4) indican que ese lado no es más blando. El residuo accionable que esta auditoría avala: GAP-A (densidad uniforme en $T$, género finitud) y el PIVOTE 176.P1 (log-free cerca de $\sigma=\tfrac12$).

## 8. Erratas

- **E-185.1** (Doc 176 §1.2): término del polo del lema de Littlewood por abscisa: dice $-2\pi(1-\sigma)$, debe decir $-\pi(1-\sigma)$ (en la normalización con ceros contados en $0<\gamma\le T$). Contradice al Doc 173 §6.1, que usa la constante correcta. Impacto: $O(1)$, ningún teorema afectado; corregir antes de publicar 176.6.
- **E-185.2** (Doc 176, Prop 176.9, punto 4): la configuración saturada requiere una constante pequeña ($N\asymp\epsilon T^{1-cs}\log T$) para ser compatible con $N(T)\sim\tfrac T{2\pi}\log T$ cuando $e^{-c}>\tfrac1{2\pi}$; tal como está escrito ("$\le N(T)$ para $\kappa\le1$") es falso para $c<\log2\pi$. La optimalidad de la barrera no se ve afectada.
- **E-185.3** (Doc 173 §6.1, menor): el "cross-check independiente" del $+1/8$ es un esquema con elipsis, no una segunda prueba completa; reconstruible y correcto, pero la etiqueta "dos pruebas independientes" del resumen ejecutivo (si se exporta) debe decir "prueba + chequeo de consistencia en dos formas".

**Auditor:** Documento 185, Fase 58. Veredicto global: **el par 173/176 resiste la auditoría adversarial** — caso raro (~1/4 cae; aquí 0/10 cae). La debilidad del par no es de corrección sino de naturaleza: dos identidades-espejo y dos teoremas de posición/obstrucción; el único puente entre dificultades distintas es 176.7.
