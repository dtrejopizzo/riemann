# Documento 188 — Auditoría adversarial de D180 (pivote 176.P1 y barreras #2/#3) y D183 (energía de Dirichlet y barrera #4)

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato:** intentar destruir D180 y D183, pieza por pieza, con reconstrucción independiente previa a la lectura de cada prueba. Doble motivación declarada: confirmar barreras correctas ES valioso, pero detectar una barrera sobre-afirmada REABRIRÍA una ruta hacia A — eso sería buena noticia.
**Método:** backward-only; sin numérica; toda constante y cita de literatura reconstruida o marcada [GAP de literatura]; clasificación estructural por orden del director (COERCIVO / CORRELACIONAL / MIXTO / REDUNDANTE).
**Coordenadas:** las de Docs 170/173/176/180/183. $\rho=\tfrac12+b+i\gamma$, $E(T)=\sum_{\gamma\le T,\beta>1/2}b^2$, **A** $\iff E(T)=O(1)$; certificado previo [Thm 170.5]: $E(T)\ll T/\log T$.

---

## 0. Resumen ejecutivo del veredicto

1. **D180 sobrevive en su núcleo, con una degradación importante:** la "barrera #2" ([PROP 180.3]) es **CONDICIONAL AL SUELO DE FARMER**, que NO es teorema en la generalidad que el techo absoluto necesita. El conducto (la cota $E\le\frac{c-1}{2\pi a}\frac T{\log T}$) está probado; el "techo absoluto $\asymp T/\log T$ del conducto entero" NO lo está. **El conducto molificador NO está cerrado incondicionalmente: es la barrera más débil de las cuatro.**
2. **D183 tiene tres errores reales:** (i) errata de signo en $c(\rho)$ ([Thm 183.1]); (ii) la asintótica $(1+o(1))$ de [PROP 183.1.b] es injustificada (el propio doc la contradice en §3); (iii) **la prueba de [PROP 183.4.b] es FALSA** — la parte real de $\zeta'/\zeta$ en la línea crítica NO tiene polos: los ceros on-line aportan singularidad puramente imaginaria y los pares off se cancelan por el cuádruplo. La integral $\int(\partial_\sigma u)^2$ no "diverge por polos": es finita y $\asymp T\log^2T$ (término $\chi$). Además (iv) "$N_{\text{off}}=o(N(T))$ siempre" ([PROP 183.3]) está mal citado: Bohr–Landau solo lo da para $b\ge\delta$ fijo; incondicionalmente solo se sabe $N_{\text{off}}\le(1-c)N(T)$ (proporción crítica de Selberg/Levinson/Conrey).
3. **La barrera #4 ([PROP 183.5]) queda DEGRADADA, no refutada:** el ingrediente "peso isótropo" (183.2, interior) es correcto y basta para la conclusión negativa sobre $\mathcal D_R$; el ingrediente "población evanescente" cae como hecho incondicional; y **el único canal anisótropo del objeto — el flujo del borde $\sigma=\tfrac12$ — fue despachado sin el cálculo que merece** (el doc afirma "orden $\sum b\cdot(\dots)$" sin probarlo; mi reconstrucción lo confirma, pero SOLO tras incluir el gemelo del cuádruplo, paso que el doc nunca ejecuta).
4. **¿Reabre alguna ruta a A?** Limpiamente, no. Pero dos rendijas quedan documentadas en §5: (R1) el suelo de Farmer no-teorema deja el conducto molificador formalmente abierto; (R2) el flujo de borde $\mathcal F_{1/2}$ con su ancla $\int(\mathrm{Re}\,\zeta'/\zeta)^2\asymp T\log^2T$ (finita, contra lo que D183 afirma) no fue explorado — aunque mi análisis preliminar indica que reabsorbe en la barrera #3, merece un documento antes de declarar sellado el muro.
5. **Verdad estructural (punto 10 del mandato):** las "cuatro barreras" NO son cuatro hechos independientes. Son **dos teoremas (uno incondicional, uno condicional-a-Farmer) + un principio semi-formal + un corolario**, todos proyecciones de UN solo hecho: *la señal $\sum b^2$ es un segundo momento transversal, y todo funcional natural incondicional es isótropo (ciego a la dirección) o con signo (ciego por cancelación)*. El "muro cuádruple" tiene un componente de empaque retórico; D183 §4 lo admite él mismo. El hecho único es real; el conteo "cuatro" no añade fuerza lógica.

---

## 1. Auditoría de D180

### 1.1. [LEMA 180.1] (unidades microscópicas $\mu_2$)

**Reconstrucción.** Layer-cake [176.8.a]: $E(T)=\int_0^{1/2}2s\,N(\tfrac12+s,T)\,ds$. Con $s=u/\log T$: $E=\frac2{\log^2T}\int_0^{\frac12\log T}u\,N(\tfrac12+\tfrac u{\log T},T)\,du$ ✓ (cambio de variable elemental, verificado). La segunda igualdad $E=\frac T{\log T}\mu_2$ es **la definición de $\mu_2$**: contenido matemático nulo. (a): $T^{1-s/4}\log T=e^{-u/4}T\log T$ ✓; $\mu_2\ll2\int_0^\infty ue^{-u/4}du=32<\infty$ ✓ (esto recupera 170.5 con constante explícita $\le\frac{32}{2\pi}$... la constante no se afirma, solo $\ll1$ ✓). (b): $E\ll T/\log^2T\iff\mu_2\ll1/\log T$ — inmediato de la definición ✓. (c) inmediato ✓.

**Veredicto: CERTIFICADO, clasificación REDUNDANTE-presentacional.** Todo es correcto, pero el lema es: (definición) + (un cambio de variable en un resultado previo). Su valor es de *lenguaje* — la lectura "Selberg ⟺ desplazamiento cuadrático medio acotado; pivote ⟺ tasa $1/\log T$" es útil y honesta (el doc mismo dice "reformulación exacta") — pero la utilidad de una reformulación no es un teorema, y el doc no pretende que lo sea. Sin objeción; sin contenido nuevo.

### 1.2. [LEMA 180.2] (la franja interior y la configuración saturante)

**Reconstrucción de (b).** Franja: $2\int_0^{1/\log T}s\cdot CT\log T\,ds=CT\log T\cdot\frac1{\log^2T}=CT/\log T$ ✓. Configuración saturante: proporción $\delta$ de los $\sim\frac T{2\pi}\log T$ ceros con $b=\tfrac12/\log T$ da $E\asymp\delta\cdot\frac T{2\pi}\log T\cdot\frac1{4\log^2T}\asymp\delta T/\log T$ ✓, i.e. $\mu_2\asymp\delta$ ✓.

**Tests de compatibilidad (obligatorios del mandato):**
- *¿Compatible con 170.5/Selberg?* Sí: en $s=\tfrac12/\log T$ la cota de Selberg es $e^{-1/8}T\log T$, muy por encima de $\delta\cdot\frac T{2\pi}\log T$ para $\delta$ pequeño ✓. La densidad supuesta en $s\ge1/\log T$ no ve $u<1$ ✓ (los ceros de la configuración tienen $u=\tfrac12$).
- *¿Riemann–von Mangoldt?* La configuración respeta $N(T)\sim\frac T{2\pi}\log T$ por construcción ✓.
- *¿Ecuación funcional?* Los off vienen en cuádruplos; la convención "un representante por cuádruplo" lo absorbe; basta replicar simétricamente ✓ trivial.
- *¿Proporción crítica (Selberg 1942 / Conrey $\ge2/5$)?* Compatible mientras $\delta<1-\tfrac25$ ✓ — el doc no lo menciona, pero no hace falta: $\delta$ es arbitrariamente pequeño.

**Veredicto: CERTIFICADO.** Clasificación: **CORRELACIONAL** (es un enunciado de consistencia/legitimación de la barrera, no produce cota nueva). El refinamiento conceptual — "el pivote exige uniformidad hasta $s\to0^+$, que ya no es un teorema de densidad sino una casi-RH microscópica" — es la aportación real de D180 y está bien probado.

### 1.3. [PROP 180.3] (barrera #2: el conducto molificador) — **EL PUNTO DÉBIL, CONFIRMADO**

**Reconstrucción del conducto.** (i) Littlewood por abscisa para $f=\zeta\varphi$ (coeficiente 1 en $n=1$, así $\log|f|\to0$ cuando $\sigma\to\infty$, requisito del lema ✓; el polo $s=1$ con factor $\varphi(1)$ acotado entra en $O(\log T)$ ✓ — es exactamente la adaptación estándar del marco Levinson/Conrey de ceros-cerca-de-la-línea, con el peso $(\beta-\tfrac12)^2$ en lugar del conteo); los ceros extra de $\varphi$ solo añaden términos $\ge0$, luego $\pi E_\zeta\le\pi E_f$ ✓. (ii) Jensen: $\frac1T\int\log|f|\le\frac12\log(\frac1T\int|f|^2)\le\frac12(\frac1T\int|f|^2-1)$ ✓ (concavidad + $\log x\le x-1$). (iii) $\int_0^{1/2}\frac T2(c-1)e^{-as\log T}ds\le\frac{(c-1)T}{2a\log T}$ ✓. Conclusión $E\le\frac{c-1}{2\pi a}\frac T{\log T}+O(\log T)$: **CORRECTA**, módulo una imprecisión en el rango intermedio de (iii): la frase "en la práctica (M) con $a\asymp\theta$ cubre el rango" es un gesto, no una prueba — la hipótesis (M) se enuncia solo para $0<s\le\tfrac12$ y la cola para $\sigma\ge1$; el rango $[1,\,?]$ con coeficientes de divisores se despacha "término a término". Es reparable (cotas de valor medio estándar) pero está escrito con descuido. **E-188.6** (menor).

**El paso (iv) "optimalidad dentro del conducto"** es el más blando: "los pasos (i)–(ii) son los únicos con holgura... la forma es exacta para el conducto" — esto es un argumento de inspección, aceptable como caracterización del conducto *tal como está definido* (entrada = momento segundo molificado por línea), pero no excluye variantes (momentos molificados de $\log|f|$ directamente, mollificación dependiente de $s$, pesos en $t$). La frase "toda mejora exige $(c_T-1)/a_T\ll1/w$" vale para el conducto definido, no para "toda maquinaria de momentos". Alcance sobre-enunciado en la prosa, correcto en el enunciado formal.

**(b) El suelo de Farmer — verificación de cita.** Aquí está el problema central, y el doc medio lo sabe (declara GAP 180.L2) pero el resumen ejecutivo y la tabla lo enuncian como techo probado ("techo absoluto $\asymp T/\log T$", "Probado módulo [GAP 180.L2] (clase del suelo)"). Reconstrucción del estado de la literatura, de memoria y con honestidad:
- Lo que ES teorema (Conrey, Balasubramanian–Conrey–Heath-Brown, y la línea Levinson): para el molificador estándar (coeficientes $\mu(h)h^{-1/2}P(\cdot)$) de longitud $T^\theta$ con $\theta$ en el rango evaluable ($\theta<\tfrac4 7$ tras Conrey 1989), el momento molificado óptimo en esa clase es $1+\tfrac1\theta+o(1)$ — **asintótica evaluada para una clase concreta y un rango de $\theta$ concreto**.
- Lo que es CONJETURA (Farmer 1993, "Long mollifiers"): que $c(\theta)=1+\tfrac1\theta$ persiste para todo $\theta$ ("conjetura $\theta=\infty$" ⟹ consecuencias RH-adyacentes). Nótese la dirección: **la conjetura de Farmer es que el suelo es también techo** — es una conjetura de OPTIMALIDAD del molificador estándar, no un teorema de cota inferior universal.
- **Lo que la barrera #2 necesita y NO tengo localizado como teorema: $c(\theta)\ge1+\tfrac1\theta$ (ni siquiera $c(\theta)\ge1+\epsilon_0/\theta$) para TODO polinomio de Dirichlet $\varphi$ de longitud $T^\theta$ con $\varphi(1)$-normalización.** Una cota inferior universal del momento molificado sobre toda la clase de coeficientes es un enunciado de tipo "imposibilidad de mollificar por debajo de", y no recuerdo ningún teorema con esa generalidad uniforme en $0<s\le\tfrac12$ como exige (M). [GAP de literatura 188.L1 = 180.L2, elevado de "verificar la clase" a "verificar que exista el teorema".]
- *Techo $\theta\le1$:* verificado como **límite tecnológico**, no como imposibilidad — el teorema del valor medio $\int_0^T|\sum_{n\le N}a_nn^{-it}|^2=(T+O(N))\sum|a_n|^2$ pierde el término principal para $N\gg T$; no hay teoremas de momentos con $X>T$, pero tampoco un teorema de que no pueda haberlos. El doc dice "techo duro": es duro *de facto*, no *de jure*. Matiz obligado.

**Veredicto: DEGRADADO. Versión superviviente:** *[PROP 180.3′] El conducto Littlewood–Jensen–molificador con entrada (M) da $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}+O(\log T)$ (probado); **el techo absoluto $\asymp T/\log T$ del conducto es CONDICIONAL-A-FARMER** (condicional a que el suelo $c(\theta)\gtrsim1+1/\theta$ valga como cota inferior universal sobre la clase de molificadores, lo cual es hoy una asíntota probada solo para clases restringidas y $\theta<4/7$, y conjetura de optimalidad más allá).* Clasificación: **MIXTO** (conducto = COERCIVO probado; techo = CORRELACIONAL-condicional). **Consecuencia importante para el programa: de las dos "gemelas", solo 176.9 (densidades) es barrera incondicional; 180.3 es barrera-bajo-creencia-estándar. La afirmación de D180 §1.4 "juntas cubren las dos únicas maquinarias incondicionales" queda: una cubierta por teorema, la otra por conjetura de la industria.**

### 1.4. [PROP 180.4] (barrera #3: ceguera de signo)

**Reconstrucción de (a).** Cauchy–Schwarz por línea: $\int_0^T(\log|\zeta|)^+\le T^{1/2}(\int(\log|\zeta|)^2)^{1/2}\ll T\sqrt{\log\log T}$ usando el momento de Selberg $\sim\frac T2\log\log T$; por anchura $1/\log T$ de la franja: $\ll T\sqrt{\log\log T}/\log T$ ✓. **Constante de Selberg verificada:** el CLT de Selberg es $\log|\zeta(\tfrac12+it)|/\sqrt{\tfrac12\log\log T}\Rightarrow N(0,1)$ (varianza $\tfrac12\log\log T$; la de $S(t)$ es $\frac1{2\pi^2}\log\log T$ — el doc usa la correcta para $\log|\zeta|$, no la confunde con la de $S$) ✓, luego $\int_0^T(\log|\zeta(\tfrac12+it)|)^2\sim\frac T2\log\log T$ ✓.

**ERRATA DETECTADA (E-188.1):** el resumen ejecutivo (§0.5) afirma "la parte positiva sola **vale $\gg$** $T\sqrt{\log\log T}/\log T$ en la franja microscópica (CLT de Selberg)", pero la *prueba* de 180.4(a) solo establece la dirección $\ll$ (Cauchy–Schwarz da cota SUPERIOR). Para la lógica de la barrera (la masa positiva es *demasiado grande* para que los momentos den $T/\log T$ con signo positivo) **lo que se necesita es la cota inferior $\gg$**, que sí es verdadera por el CLT (la parte positiva de una variable $\approx$ gaussiana centrada de desviación $\sqrt{\tfrac12\log\log T}$ tiene esperanza $\asymp\sqrt{\log\log T}$), **pero requiere el CLT desplazado uniforme en $0\le s\ll1/\log T$** — exactamente el GAP 180.L3 (Tsang). Es decir: la mitad $\ll$ está probada e irrelevante; la mitad $\gg$, que es la que carga la barrera, está solo esbozada y es condicional al GAP de literatura. Sobre la uniformidad: que el momento segundo (y el CLT) de Selberg toleren desplazamientos $s\ll1/\log T$ es plausible y consistente con Tsang 1984 (los desplazamientos hasta el gap medio no cambian la varianza al orden principal), pero lo cito de memoria igual que el doc: el GAP está bien declarado.

**(b)** Littlewood como identidad bidireccional: correcto (Littlewood 1924; la identidad por abscisa con error $O(\log T)$ de bordes es estándar). La lectura "no existe tercer término" es válida.

**Sobre-afirmación de alcance:** la conclusión "la ruta 2 es cambio de moneda, no de información" y "las herramientas que saben integrar $\log|\zeta|$ con signo son exactamente las que saben contar ceros" es un **principio estructural sobre una clase informal de herramientas** ("momentos de $|\zeta|$, de $\log|\zeta|$, de potencias"), no un teorema de imposibilidad cuantificado sobre funcionales. Como barrera, #3 es de naturaleza distinta a #1: #1 (176.9) es un teorema sobre TODA densidad exponencial; #3 es un argumento sobre las herramientas *conocidas*. Honesto en el cuerpo, algo inflado en el resumen ("colapsa").

**Veredicto: CERTIFICADO-CON-ERRATA (E-188.1: $\gg$/$\ll$ desalineados entre enunciado y prueba; la dirección útil es condicional a 180.L3).** Clasificación: **MIXTO** (la identidad (b) es COERCIVA y exacta; la cota (a) y la moraleja son CORRELACIONALES sobre clase informal).

### 1.5. [LEMA 180.5] (identificación $S_1$)

**Verificación.** $S_1(t)=\frac1\pi\int_{1/2}^\infty\log|\zeta(\sigma+it)|\,d\sigma$ es la definición clásica (Littlewood; Titchmarsh §9.9) ✓; $D(T)=\int_{1/2}^\infty\int_0^T\log|\zeta|\,dt\,d\sigma=\pi\int_0^TS_1(t)\,dt$ por Fubini, justificado por integrabilidad local de $\log|\zeta|$ ✓ (las singularidades logarítmicas son integrables; [LEMA 176.2] citado). Corolario (a): $|\int_0^TS_1|\ll T/\log T$ vía 170.5+176.6 ✓ — y es, hasta donde sé, una observación con interés propio (la cota clásica de $\int S_1$ es $O(T/\log T)$... [GAP de literatura 188.L2 = 180.L4: si Littlewood/Fujii ya tienen $\int_0^TS_1\ll T/\log T$ o mejor incondicional, el corolario no es nuevo; el pivote 180.P2 — auditar Fujii — queda como deuda legítima]). (b) es transcripción de 176.4.c ✓.

**Veredicto: CERTIFICADO.** Clasificación: REDUNDANTE-presentacional con valor de conexión a literatura (el puente a la moneda clásica $S_1$ es exactamente lo que permitirá detectar si A ya está refutada-por-omisión en la literatura de Fujii — tarea pendiente correcta).

### 1.6. [PROP 180.6] (LH no compra ni un log)

**Reconstrucción.** Bajo LH: Ingham 1940 da $N(\sigma,T)\ll T^{2(1-\sigma)+\varepsilon}$, i.e. $T^{1-2s+\varepsilon}$ ✓ (cita correcta; Halász–Turán da $T^\varepsilon$ solo en $\sigma\ge\tfrac34+\delta$ ✓, irrelevante cerca de $\tfrac12$ ✓). En la maquinaria 176.9 el exponente pasa de $c=\tfrac14$ a $c=2$: $\mu_2\ll2\int ue^{-cu}du=2/c^2$, ratio $\frac{2/(1/16)}{2/4}=64$ ✓ — **el factor "≍64" del doc es exactamente correcto**, buen indicio de cálculo real. En $s\le K/\log T$ la cota $T^{1-2s+\varepsilon}$ es trivial ✓ (excede $T$), luego la masa fatal de la franja interior persiste ✓. (b): los dos topes de 180.3 (suelo, techo $\theta\le1$) no son tocados por LH ✓ — pero nótese que (b) hereda la degradación de 180.3: "LH no compra" es verdad *para el conducto*, y el conducto solo está techado condicional-a-Farmer. (c) es 176.7 ✓.

**Veredicto: CERTIFICADO**, con el matiz de alcance: el enunciado correcto es "LH no compra ni un log **por los dos conductos analizados**" — así está en la letra de la prueba; la prosa "A es de otra escala que LH" es lectura legítima. Clasificación: CORRELACIONAL (calibración), valiosa: la asimetría A⟹LH sin recíproco ni acercamiento es el resultado de calibración más sólido del doc.

---

## 2. Auditoría de D183

### 2.1. [TEOREMA 183.1] (identidad de Green desingularizada)

**Reconstrucción independiente.** En $\Omega_R$, $u$ armónica ⟹ $|\nabla u|^2=\mathrm{div}(u\nabla u)$ ✓; $|\nabla u|^2=|\zeta'/\zeta|^2$ por Cauchy–Riemann ✓ (verificado: $\partial_\sigma u=\mathrm{Re}\frac{\zeta'}\zeta$, $\partial_tu=-\mathrm{Im}\frac{\zeta'}\zeta$).
- *Esquinas:* $\partial R_T$ tiene 4 esquinas y los círculos interiores; el dominio es Lipschitz y $u$ es suave en un entorno de las esquinas (T no-ordenada, sin ceros ahí; en $t=0$, $\sigma$ real, $\zeta$ real): la fórmula de divergencia vale sin reparos ✓.
- *El polo $s=1$:* está EN el borde $t=0$ ($\gamma=0$). Riesgo: flujo $u\,\partial_tu$ no integrable junto a $\sigma=1$. Salvado por simetría: en el eje real $\zeta$ es real, luego $\partial_tu=-\mathrm{Im}\,\zeta'/\zeta=0$ en $t=0$ fuera de la singularidad, y el límite del flujo es manejable; el doc lo despacha con "$|\gamma_1|=0$ fuera de $t>0$", que es ligero pero el término acaba en el $O(\log^2T)$ del flujo horizontal, defendible ✓ (con la advertencia de que un tratamiento de publicación debe indentar el polo explícitamente).
- *$X\to\infty$:* $|\zeta'/\zeta|\ll2^{-\sigma}$ ✓, flujo se anula ✓.
- *Auto-energía — reconstrucción de signos.* $\mathcal D_R=\oint_{\partial\Omega_R}u\,\partial_nu$ con $n$ saliente de $\Omega_R$; en cada círculo $n=-\partial_r$ ($r$ desde $\rho$). Con $u=\log r+h$: contribución del círculo $=-\oint(\log R+h)(\tfrac1R+\partial_rh)R\,d\theta=-2\pi\log R-2\pi h(\rho)+O(R\log\tfrac1R)$ (propiedad de la media para $\oint h\,d\theta$ ✓; términos cruzados $O(R\log\frac1R)$ ✓). Es decir: auto-energía $=2\pi\log\tfrac1R\;\mathbf{-}\;2\pi h(\rho)+O(R\log\tfrac1R)$.

**ERRATA DETECTADA (E-188.2):** el doc, tras su propia corrección de signo a mitad de prueba (síntoma de redacción apresurada), concluye "$+2\pi\log(1/R)+2\pi h(\rho_0)$". El signo del término armónico es **negativo**: $c(\rho)=-2\pi h(\rho)$, no $+2\pi h(\rho)$. La reconstrucción es inequívoca (el término cruzado es $-\oint h\cdot\tfrac1R\cdot R\,d\theta=-2\pi h(\rho)$). **Impacto: nulo en órdenes de magnitud** (solo se usa $|c(\rho)|\ll\log\gamma$), pero es un error real en una identidad llamada "exacta".

Sanidad: $\mathcal D_R\ge0$ y $\to+\infty$ como $2\pi\log\frac1R$ por cero cuando $R\to0$ ✓ — consistente con [173.E] ✓.

**Veredicto: CERTIFICADO-CON-ERRATA (E-188.2, signo de $c(\rho)$).** Clasificación: COERCIVO (identidad exacta, maquinaria limpia).

### 2.2. [PROP 183.1.b] (orden de $\mathcal D_R$) — **AUTOCONTRADICCIÓN INTERNA**

El enunciado afirma $\mathcal D_R(T)=(1+o(1))\cdot2\pi N(T)\log\log T\asymp T\log T\log\log T$ para $R\asymp1/\log T$. Pero la propia prueba dice de $\sum c(\rho)$: "$\ll N(T)\log T\asymp T\log^2T$ — **del mismo orden o mayor que el principal**; ver §1.5 para el control", y §1.5 NO aporta ese control; peor, §3 del mismo documento afirma "$\sum c(\rho)$ es del orden $T\log^2T$, mil veces mayor que la señal". $T\log^2T\gg T\log T\log\log T$: **el término "corrección" domina al "principal" según la cota que el propio doc da, luego el $(1+o(1))$ no está probado en ninguna parte.** (Una cancelación en $\sum h(\rho)$ es plausible — $h(\rho)$ tiene signos — pero nadie la prueba.) Además el flujo del borde $\sigma=\tfrac12$ se remite a §2, donde solo se demuestra que NO se sabe acotar.

**Veredicto: DEGRADADO. Versión superviviente:** *$\mathcal D_{1/\log T}(T)\ge(2\pi+o(1))N(T)\log\log T-|\sum c|-|\text{flujo}|$ y $\mathcal D_R\ll T\log^2T$; el orden exacto entre $T\log T\log\log T$ y $T\log^2T$ queda SIN determinar.* Impacto en la barrera: nulo o favorable (un fondo aún mayor ahoga más la señal), pero la asintótica enunciada es falsa-como-probada. **E-188.3.**

### 2.3. [PROP 183.2] (ceguera a $b$) y el flujo del borde — **EL PUNTO DELICADO DEL MANDATO**

**Lo probado de verdad:** para $b\ge R$ (disco entero en el dominio), la auto-energía es $2\pi\log\frac1R+c(\rho)+O(R\log\frac1R)$ con $c(\rho)$ función suave de la posición sin estructura $b^2$ aislable ✓. Esto es correcto y es el corazón legítimo de la barrera: **el peso de volumen es isótropo**. El contraste con el peso transversal $v=(\sigma-\tfrac12)^2$ de 173.C es exacto y es la mejor frase del documento.

**Lo NO probado:** la frase "la señal $\sum b^2$ aparece, si acaso, en el flujo del borde $\sigma=\tfrac12$, de orden $\sum b\cdot(\dots)$ — primer orden en $b$, y aun ahí dominado" se ASEVERA sin cálculo. El mandato pregunta: ¿dónde vive la información de $b$ en el borde y la despachó el doc con cuidado? **No la despachó con cuidado.** Reconstrucción:

(i) *Sin el gemelo del cuádruplo, la señal de borde sería logarítmica, no lineal.* Un cero off $\rho=\tfrac12+b+i\gamma$ aporta a $u$ en el borde el término $\log\sqrt{b^2+\tau^2}$ ($\tau=t-\gamma$) y a $\partial_\sigma u$ el término $\mathrm{Re}\frac1{\frac12+it-\rho}=\frac{-b}{b^2+\tau^2}$ (núcleo de Poisson: $\to-\pi\delta$ cuando $b\to0$). El producto cruzado integra exactamente $\int\log\sqrt{b^2+\tau^2}\cdot\frac b{b^2+\tau^2}d\tau=\pi\log(2b)/\dots=\pi\log b+\pi\log2$: **$\asymp\log\frac1{2b}$ por cero off, anisótropo y divergente cuando $b\to0$** — la "energía de imagen" del método de imágenes que el mandato anticipa.

(ii) *El gemelo lo cancela.* Pero $\zeta$ tiene también el cero $1-\bar\rho=\tfrac12-b+i\gamma$ (fuera del dominio, dentro de $\zeta'/\zeta$): su término en $\partial_\sigma u(\tfrac12+it)$ es $\frac{+b}{b^2+\tau^2}$, que **cancela exactamente** la parte singular de (i). Igualmente, los ceros on-line aportan $\mathrm{Re}\frac1{i(t-\gamma)}=0$: **$\partial_\sigma u(\tfrac12+it)$ no tiene parte singular de ceros en absoluto**; su tamaño lo fija el factor $\chi$ de la ecuación funcional: $\partial_\sigma u(\tfrac12+it)=-\tfrac12\log\tfrac t{2\pi}+O(\text{fluctuación})$. Con esto, la dependencia en $b$ del flujo viene de $u$ (cuyo pozo $\log(b^2+\tau^2)$ ensancha con $b$: $\int[\log\sqrt{b^2+\tau^2}-\log|\tau|]d\tau\asymp b$) contra el factor suave $\asymp\log T$: **señal $\asymp b\log T$ por cero off — la afirmación "primer orden en $b$" del doc resulta CORRECTA, pero por un cálculo de dos pasos (Poisson + cancelación del cuádruplo) que el documento jamás hace.** Si el gemelo no existiera (familias sin ecuación funcional alineada), la afirmación sería falsa.

**Veredicto: DEGRADADO (por prueba incompleta, no por falsedad). Versión superviviente:** *183.2′: la auto-energía de volumen es ciega a $b$ (probado); el flujo del borde porta señal anisótropa $\asymp b\log t$ por cero off (probado AQUÍ en §2.3, no en D183), lineal en $b$ gracias a la cancelación del cuádruplo; ninguna de las dos piezas produce $\sum b^2$.* Clasificación: COERCIVO (interior) + hueco-reparado (borde). **E-188.4: la afirmación de borde de 183.2 estaba sin prueba; la cancelación del gemelo es obligatoria y no figura.**

### 2.4. [PROP 183.3] (asimetría de constante y población)

(a) *Factor $\tfrac12$ del semicírculo:* ✓ verificado — el cero on-line tiene medio disco en $\Omega_R$, su semicírculo da $\pi\log\frac1R$, razón $2$ con el off, constante que se diluye en $\log\frac1R$ ✓. La refutación de la apuesta del mandato de D183 es correcta.

(b) **ERROR DE CITA (E-188.5):** "Sin RH, $N_{\text{off}}=o(N(T))$ **siempre** (densidad cero de ceros off — Bohr–Landau / Selberg)". **Falso tal como está enunciado.** Bohr–Landau (1914) da $N(\tfrac12+\delta,T)=o(N(T))$ para cada $\delta>0$ **fijo**; no dice nada de los ceros off con $b\to0$ (que son exactamente los relevantes para A: la configuración saturante de [LEMA 180.2] tiene TODOS sus off con $b\asymp1/\log T$ y proporción $\delta>0$, y es consistente con todo lo conocido). Lo único incondicional sobre $N_{\text{off}}$ total es $N_{\text{off}}\le(1-c)N(T)$ con $c$ = proporción crítica probada (Selberg 1942; Levinson $1/3$; Conrey $2/5$ — para proporción *en la línea*). **"Población evanescente" NO es un hecho incondicional**; es falso en la peor configuración compatible — que es precisamente la que D180 construyó un documento antes. Inconsistencia interna del par D180/D183.

**Veredicto: (a) CERTIFICADO; (b) REFUTADO como enunciado incondicional.** Versión superviviente de (b): $N_{\text{off}}\le(1-c)N(T)$, suficiente para que $\mathcal D^{\text{off}}_R\ll\mathcal D_R$ a nivel de orden no estricto, pero **el "ahogo doble" se reduce a ahogo simple (solo el peso isótropo)**.

### 2.5. [PROP 183.4] (ancla de Selberg) — **PRUEBA (b) REFUTADA**

(a) $\int_0^Tu(\tfrac12+it)^2dt=\tfrac T2\log\log T+O(T)$: **constante verificada** (varianza $\tfrac12\log\log T$ del CLT de Selberg para $\log|\zeta|$; la varianza $\frac1{2\pi^2}\log\log T$ es la de $S(t)$, distinta — el doc usa la correcta) ✓; GAP 183.L1 (uniformidad Tsang en $s\ll1/\log T$) declarado honestamente ✓. CERTIFICADO.

(b) **REFUTADO en su prueba.** El doc afirma que $\int_0^T(\mathrm{Re}\frac{\zeta'}\zeta(\tfrac12+it))^2dt$ diverge "porque los ceros simples dan polos de $\zeta'/\zeta$ en la línea", con prueba: "en $s=\tfrac12+it$ con $\rho=\tfrac12+i\gamma$ el término es $\frac1{i(t-\gamma)}$, cuyo cuadrado real integrado diverge". **Error elemental: $\frac1{i(t-\gamma)}$ es puramente imaginario — su parte real es CERO.** La singularidad del cero on-line vive íntegramente en $\mathrm{Im}\,\zeta'/\zeta$ (i.e. en $S'(t)$), no en $\partial_\sigma u$. Y como se reconstruyó en §2.3, los pares off también cancelan su parte real singular en la línea. Por tanto $\partial_\sigma u(\tfrac12+it)$ es localmente acotada (salvo el conjunto de medida nula de los propios ceros, donde $u=-\infty$ pero $\mathrm{Re}$ del cociente es regular) y $\int_0^T(\partial_\sigma u)^2dt\asymp T\log^2T$ por el término determinista $-\tfrac12\log\tfrac t{2\pi}$ del factor $\chi$ — **finita, no infinita**. La CONCLUSIÓN del doc ("el ancla del borde no cierra": Cauchy–Schwarz da $\sqrt{T\log\log T}\cdot\sqrt{T\log^2T}=T\log T\sqrt{\log\log T}$, inútil) **sobrevive con la razón corregida** — "enorme" sí, "infinito" no. (c) correcto: $\sigma>1$ incondicional por ortogonalidad ✓; $\tfrac12<\sigma<1$ vía correlación de pares, condicional, GAP marcado ✓ (Montgomery 1973 trabaja bajo RH; el doc lo marca como no-incondicional ✓).

**Veredicto: (a) CERTIFICADO; (b) REFUTADO-en-la-prueba / enunciado sustituido** por: *$\int_0^T(\partial_\sigma u(\tfrac12+it))^2dt\asymp T\log^2T$ (dominada por el factor $\chi$, sin polos); el ancla Cauchy–Schwarz da $O(T\log T\sqrt{\log\log T})$, insuficiente.* (c) CERTIFICADO. **E-188.6.**

### 2.6. [PROP 183.5] (barrera #4)

La barrera se enunciaba como conjunción de (1) peso isótropo [183.2] y (2) población evanescente [183.3.b]. Tras esta auditoría: (1) sobrevive (con el hueco del borde reparado aquí); (2) cae como hecho incondicional. **La conclusión central sobrevive con un solo pilar:** el peso isótropo basta — toda cota de $\mathcal D_R$ acota $N_{\text{off}}\cdot\log\frac1R$ (conteo), no $\sum b^2$ (energía), y el conteo ya es territorio de la barrera #1. Pero el enunciado "la señal se ahoga doblemente" y la prosa demográfica deben reescribirse.

**Veredicto: DEGRADADO. Versión superviviente:** *Barrera #4′ (ceguera de anisotropía): la energía de Dirichlet plana pesa cada cero por $\log\frac1R$ sin factor transversal; el único término anisótropo (flujo de borde) es lineal en $b$ con factor $\log t$, y su control incondicional reabsorbe en funcionales con signo (barrera #3). $\mathcal D_R$ no aísla $\sum b^2$.* Clasificación: **MIXTO**, y estructuralmente DERIVADA de #1 (la propia prueba invoca 176.9).

---

## 3. Tabla de veredictos

| Resultado | Veredicto | Nota |
|---|---|---|
| [LEMA 180.1] $\mu_2$ | CERTIFICADO | REDUNDANTE-presentacional: definición + cambio de variable; lectura útil, contenido nulo |
| [LEMA 180.2] franja + saturación | CERTIFICADO | compatible con 170.5/RvM/ec. funcional/proporción crítica; CORRELACIONAL |
| [PROP 180.3] barrera #2 | **DEGRADADO** | conducto probado; **techo absoluto CONDICIONAL-A-FARMER** (el suelo $c(\theta)\ge1+1/\theta$ universal NO es teorema; teorema solo para clase estándar, $\theta<4/7$); $\theta\le1$ = límite de facto, no de jure |
| [PROP 180.4] barrera #3 | CERTIFICADO-CON-ERRATA | E-188.1: $\gg$ enunciado / $\ll$ probado; la dirección que carga la barrera es condicional a 180.L3 (Tsang); alcance = clase informal de herramientas, no teorema de imposibilidad |
| [LEMA 180.5] $S_1$ | CERTIFICADO | identificación y constantes verificadas; pivote Fujii pendiente legítimo |
| [PROP 180.6] LH | CERTIFICADO | factor 64 verificado; alcance correcto = "por los conductos analizados"; (b) hereda condicionalidad de 180.3 |
| [THM 183.1] Green | CERTIFICADO-CON-ERRATA | E-188.2: $c(\rho)=-2\pi h(\rho)$, signo invertido; esquinas/polo/$X\to\infty$ OK |
| [PROP 183.1.b] orden de $\mathcal D_R$ | **DEGRADADO** | E-188.3: $(1+o(1))$ injustificado, $\sum c(\rho)$ admite $T\log^2T$ ≫ principal (el propio doc lo dice en §3); sobrevive solo el encuadre $T\log T\log\log T\lesssim\dots\ll T\log^2T$ |
| [PROP 183.2] ceguera a $b$ | **DEGRADADO** | interior probado; borde ASERTADO sin cálculo (E-188.4); la afirmación "primer orden en $b$" resulta cierta solo vía cancelación del gemelo del cuádruplo, reconstruida aquí |
| [PROP 183.3] (a) factor ½ | CERTIFICADO | constante, se diluye ✓ |
| [PROP 183.3] (b) $N_{\text{off}}=o(N)$ | **REFUTADO** (como incondicional) | E-188.5: Bohr–Landau solo da $o(N)$ para $b\ge\delta$ fijo; incondicional: $N_{\text{off}}\le(1-c)N$; contradice la config. saturante de 180.2 |
| [PROP 183.4] (a),(c) | CERTIFICADO | constante $\tfrac T2\log\log T$ ✓; condicionalidad de Montgomery marcada ✓ |
| [PROP 183.4] (b) | **REFUTADO en la prueba** | E-188.6: $\mathrm{Re}\frac1{i(t-\gamma)}=0$ — no hay polos en la parte real; la integral es $\asymp T\log^2T$ (factor $\chi$), finita; la conclusión "no cierra" sobrevive con razón corregida |
| [PROP 183.5] barrera #4 | **DEGRADADO** | sobrevive con un solo pilar (isotropía); "ahogo doble" → simple; derivada de #1 |

**Erratas:** E-188.1 ($\gg$/$\ll$ en 180.4/§0.5) · E-188.2 (signo $c(\rho)$ en 183.1) · E-188.3 ($(1+o(1))$ de 183.1.b) · E-188.4 (borde de 183.2 sin prueba; falta la cancelación del cuádruplo) · E-188.5 ($N_{\text{off}}=o(N)$ falso como incondicional) · E-188.6 (Re/módulo confundidos en 183.4.b) · E-188.7 (menor: rango intermedio de (iii) en 180.3 despachado con "en la práctica").

---

## 4. Clasificación estructural y la pregunta del director

**¿Son las cuatro barreras independientes?** No. Estructura real tras la auditoría:

- **Barrera #1 (176.9, densidades):** teorema incondicional sobre una clase formal completa. La única barrera de pleno derecho.
- **Barrera #2 (180.3, molificadores):** conducto-teorema + techo **condicional a una conjetura de optimalidad de la industria** (Farmer). Barrera-bajo-creencia, no barrera-teorema.
- **Barrera #3 (180.4, signo):** una identidad exacta (Littlewood bidireccional, fuerte) + un argumento de clase informal ("los momentos son ciegos al signo"). Principio estructural, no teorema de imposibilidad.
- **Barrera #4 (183.5, población/isotropía):** corolario de la isotropía del funcional + (tras esta auditoría) NADA demográfico; su prueba invoca explícitamente la #1.

D183 §4 lo confiesa: "las cuatro barreras son una sola vista cuatro veces". **Esa frase es la verdad estructural y debe gobernar la retórica del programa:** el hecho único es *la señal es un segundo momento transversal ($b^2$ = peso anisótropo de orden 2) y los funcionales incondicionales naturales son isótropos o con signo*. Las "cuatro barreras" son una barrera y media de teorema (la #1 entera, la mitad-conducto de la #2) más dos lecturas del mismo fenómeno. El "muro cuádruple de A" como justificación de inalcanzabilidad es **empaque retórico parcial**: la inalcanzabilidad por las máquinas conocidas está genuinamente probada para densidades, y solo argumentada para el resto.

## 5. Impacto: ¿reabre alguna ruta a A?

**Limpiamente, ninguna. Pero el director debe saber dos cosas:**

- **(R1) El conducto molificador NO está cerrado por teorema.** Si alguien probara (o si en la literatura existiera — [GAP 188.L1]) que NO hay suelo universal $c(\theta)\ge1+\epsilon/\theta$, una familia de molificadores exótica con $c-1=o(\theta/\log T)$ daría $E(T)=o(T/\log T)$ por el conducto YA PROBADO de 180.3(i)–(iii). La barrera #2 es hoy una apuesta sociológica con forma de teorema. Nadie espera que caiga — pero nuestra arquitectura no debe citar el "techo absoluto" como probado. *Estado: ruta no-reabierta pero no-cerrada.*
- **(R2) El flujo de borde $\mathcal F_{1/2}$ es el único canal anisótropo del objeto de D183 y fue infra-analizado.** Esta auditoría reparó el hueco (la señal es $\asymp b\log t$ por cero off, vía cancelación del cuádruplo) y corrigió 183.4.b (el ancla $\int(\partial_\sigma u)^2\asymp T\log^2T$ es FINITA, no infinita). Mi análisis preliminar indica que explotar $\mathcal F_{1/2}$ reabsorbe en integrales tipo $\int\log|\zeta(\tfrac12+it)|\,dt$ — territorio de la barrera #3 — porque la señal es de PRIMER orden en $b$ ($\sum b$, no $\sum b^2$) y reentra por Littlewood. Pero un funcional que acote $\sum_{\text{off}}b$ con factor $\log T$ sería ya un objeto nuevo (interpolante entre conteo y energía, $\sum b\ge(\sum b^2)\cdot(\max b)^{-1}$...). *Recomendación: medio documento (Doc 184 o anexo) sobre $\mathcal F_{1/2}$ ANTES de declarar la #4 sellada; coste bajo, y es exactamente el tipo de término que el programa ha barrido dos veces (D183 lo despachó; 183.4.b lo enterró con una prueba falsa).*
- Lo que SÍ queda confirmado y sale reforzado: el refinamiento de 180.2 (el pivote = casi-RH microscópica, no densidad de industria), la calibración LH (180.6, factor 64 exacto), la identidad de Green 183.1 (con su signo corregido) y el diagnóstico maestro: **la señal vive en el peso transversal de orden 2 y el objeto correcto es $\mu_2$ / GAP-180.1 / GAP-183.1 — todos el mismo objeto, género 141.G1.** La degradación de barreras no toca esa convergencia; al contrario, la limpia de duplicados.

**GAPs de literatura heredados y nuevos:** 188.L1 (= 180.L2 elevado: ¿existe teorema de suelo universal de mollificación?); 188.L2 (= 180.L4, Fujii sobre $\int S_1$ — urgente: podría contener ya el mejor resultado hacia A o su imposibilidad de mejora); 180.L1 (inexistencia log-free cerca de $\tfrac12$ — plausible, sin contraejemplo hallado); 180.L3/183.L1 (uniformidad Tsang — del que ahora depende la mitad útil de la barrera #3).

---

**Documentos internos:** D170, D172, D173, D176, D177, D180 (auditado), D183 (auditado). **Sucesor sugerido:** Doc 189 = anexo $\mathcal F_{1/2}$ (rendija R2) + corrección de erratas en D180/D183 + reescritura del "muro" como UNA barrera-teorema (#1) más un principio estructural unificado.
