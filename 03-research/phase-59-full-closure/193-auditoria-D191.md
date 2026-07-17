# Documento 193 — Auditoría adversarial del Documento 191 (el suelo universal del momento molificado)

**Programa:** Hipótesis de Riemann — Fase 59 (cierre total)
**Fecha:** 2026-06-12
**Mandato:** decidir si [TEOREMA 191.A] se publica. Reconstrucción completa desde cero ANTES de releer la prueba; ataque a la normalización, a la novedad, al rango de uniformidad y a las proposiciones satélite. Sin numérica; backward-only.
**Auditor:** adversarial; el objetivo declarado es destruir el resultado.

---

## 0. Veredicto ejecutivo

**CERTIFICADO-PUBLICABLE (con reserva de literatura acotada y dos erratas reparables).**

- La prueba de [TEOREMA 191.A] **reconstruye limpia**: los seis pasos (i)–(vi) cierran, con una laguna de redacción en (iv) (hay que invocar la desigualdad de Hilbert generalizada de Montgomery–Vaughan EN SU FORMA PONDERADA, no la forma simple; el error final declarado es el correcto) — errata E-193.3, reparable en cinco líneas.
- **La normalización es la misma que en [PROP 180.3]**: verificado contra el texto de D180 (la hipótesis (M) usa $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt$, sin factor $\log T$; el $c(\theta)$ de D191 §Coordenadas es exactamente mean$(0)$ de D180). El sello [COR 191.B] se sigue, PERO su frase sobre la tasa ("$a\le2(1-\theta)$ por debajo") está mal calibrada y la justificación correcta es otra (errata E-193.1, el corolario sobrevive con prueba reescrita).
- **Consistencia con la verdad conocida:** $1+\log\frac{1-\theta}\theta\le1+\frac1\theta$ siempre ($\log x<x$), trivial en $\theta=\tfrac12$, no trivial en $\theta<\tfrac12$ — coherente como cota inferior estricta del valor BCHB/Farmer. Ninguna contradicción.
- **Novedad:** el punto fino del ataque 3 se resuelve A FAVOR del documento, con matiz importante (§3): la "cota diagonal folklore $c\ge1/\theta$" **NO es inmediata** — el camino ingenuo muere porque $\zeta\varphi$ truncado tiene longitud $TX>T$ y el valor medio pierde el término principal; el camino BCHB+minimización daría más pero no está escrito para coeficientes generales (es exactamente [GAP-191.L1], que el doc declara). La contribución publicable es **el puente, no la tasa**.
- **Impacto sobre R1: la barrera #2 queda TEOREMA en $\theta<\tfrac12$** (tras reparar E-193.1). El estatus "rango-difícil" en $[\tfrac12,1]$ se confirma.

Erratas: E-193.1 (sustantiva, Cor 191.B), E-193.2, E-193.3, E-193.4 (menores). Ningún enunciado refutado.

---

## 1. Ataque 1: reconstrucción independiente de la prueba de 191.A

Reconstruí la prueba antes de releer §2.2, sobre el esqueleto esperable del mandato. Resultado paso a paso:

### 1.1. El esqueleto y dónde podía morir

$F=\zeta\varphi(\tfrac12+it)$, $G=F-1$, test $D=\sum_{X<p\le Y}p^{-1/2-it}$ con $Y=T^{1-\theta-\eta}$. Tres puntos de muerte posibles: (a) el error de la aproximación de Hardy–Littlewood contaminando la forma bilineal; (b) la extracción de la diagonal en $\int F_0\overline D$ cuando $F_0$ tiene longitud $TX\gg T$; (c) el paso de $\int|G|^2$ a $\int|F|^2$ (primer momento). Verifico los tres.

**(a) Correctores de Hardy–Littlewood — CIERRA.** Titchmarsh Thm 4.11 con $x=T$: válido para $\sigma>0$, $|t|\le 2\pi x/C$ — el rango $1\le t\le T$ está dentro. $|F-F_0|\ll(T^{1/2}/t+T^{-1/2})|\varphi|$. Contra $D$: $\int_1^T\frac{T^{1/2}}t\,X^{1/2+o(1)}\,Y^{1/2}\,dt\ll T^{1/2}X^{1/2}Y^{1/2}(\log T)^{B}=T^{(1+\theta+1-\theta-\eta)/2}(\log T)^B=T^{1-\eta/2}(\log T)^B$. Dividido por $T$: $\ll T^{-\eta/2}(\log T)^B$, y con $\eta\ge C_0\frac{\log\log T}{\log T}$ esto es $(\log T)^{B-C_0/2}=o(1)$ eligiendo $C_0>2B+2$. ✓ El segmento $t\le1$: $|FD|\ll X^{1/2}Y^{1/2}(\log T)^{B}\ll T^{(1-\eta)/2}$, sobra (la cota $T^{1/2+\theta}$ del doc es otra mayorante válida pero peor derivada — E-193.2). ✓

**(b) La diagonal de la forma bilineal — CIERRA, con la forma ponderada de MV (E-193.3).** Este era el candidato a asesino. $\int_0^TF_0\overline D\,dt$ con frecuencias $\log N$ ($N\le TX$) contra $\log p$ ($p\in(X,Y]$). Los términos $N=p$ dan EXACTAMENTE $T\cdot\alpha_p/p$ (integrando $1$). Los términos $N\ne k$: $\sum_{N\ne k}\frac{\alpha_N N^{-1/2}\,k^{-1/2}}{i\log(N/k)}(e^{i\cdot}-1)$-tipo; el espaciamiento mínimo de $\{\log N\}$ en $N\asymp M$ es $\asymp1/M$, de modo que la forma simple de Hilbert (con $\delta^{-1}$ global $\asymp TX$) NO basta. La que cierra es la **generalizada con pesos** (Montgomery–Vaughan 1974, Cor. 2): $\big|\sum_{N\ne k}\frac{a_N\bar b_k}{\log(N/k)}\big|\ll\big(\sum_N|a_N|^2\delta_N^{-1}\big)^{1/2}\big(\sum_k|b_k|^2\delta_k^{-1}\big)^{1/2}$ con $\delta_N\asymp1/N$. Con $a_N=\alpha_NN^{-1/2}$: $\sum|\alpha_N|^2N^{-1}\cdot N=\sum_{N\le TX}|\alpha_N|^2\ll TX(\log T)^{B_3}$ (divisor-acotados ✓, pues $|\alpha_N|\le\sum_{n|N}|b_n|\le d_{\kappa+1}(N)(\log T)^{A_0}$ ✓). Con $b_k=p^{-1/2}$: $\sum_p p^{-1}\cdot p=\pi(Y)\ll Y/\log Y$. Error total $\ll(TX)^{1/2}Y^{1/2}(\log T)^{B}=T^{1-\eta/2}(\log T)^B$ — **exactamente el error que el doc declara en (iv)**. La prueba es correcta; la redacción omite que se necesita la forma ponderada (la cita "(1974)" la cubre, pero un árbitro lo pedirá). El término $-1$ contra $D$: frecuencia $0$ contra $\log p\ge\log X$, gap grande, contribución $\ll\sum_pp^{-1/2}/\log p\ll Y^{1/2}$, inocua. ✓
**Crucial:** $\alpha_p=\sum_{n|p,n\le X,p/n\le T}b_n=b_1=1$ para $X<p\le Y$ (el divisor $n=p$ excede el soporte; $p\le Y\le T$ ✓) — [LEMA 191.1] aplicado a la versión truncada también es correcto, no solo a $1*b$ ideal. ✓

**(c) Del cuadrado de $G$ al momento — CIERRA.** $\frac1T\int|F|^2=1+\frac2T\mathrm{Re}\int G+\frac1T\int|G|^2$; el primer momento: la suma $\frac1T\sum_{2\le N\le TX}|\alpha_N|N^{-1/2}/\log N\ll T^{-1}(TX)^{1/2}(\log T)^B=T^{(\theta-1)/2}(\log T)^B=o(1)$ con ahorro de potencia para $\theta<1$ ✓ (aquí la suma de $|\alpha_N|N^{-1/2}$ se mayora por Cauchy–Schwarz contra $\sum N^{-1}\cdot$longitud, mismo orden). Correctores ídem. ✓

**(d) Denominador y ensamblaje.** MV valor medio: $\frac1T\int|D|^2=\sum_{X<p\le Y}\frac1p(1+O(p/T))$, y $\sup_p p/T\le Y/T=T^{-\theta-\eta}$ — el término $O(p/T)$ POR TÉRMINO (la preocupación del mandato) es uniformemente $o(1)$, ni siquiera hace falta sumarlo con cuidado. ✓ Cauchy–Schwarz: $\frac1T\int|G|^2\ge\frac{(\mathcal P-O(T^{-\eta/2}(\log T)^B))^2}{\mathcal P(1+o(1))}=\mathcal P-o(1)$ siempre que $\mathcal P\gg(\log T)^{-C_0/3}$ — garantizado pues $\mathcal P\ge2\delta\ge2C_0\frac{\log\log T}{\log T}$. ✓ Mertens: $\mathcal P=\log\frac{(1-\theta-\eta)}{\theta}+O(1/(\theta\log T))$, error absorbido en el rango declarado. ✓ La verificación interna "$\log\frac{1-\theta-\delta}\theta\ge2\delta$ para $\theta\le\tfrac12-\delta$": $(1-\theta-\delta)/\theta\ge\frac{1/2}{1/2-\delta}=\frac1{1-2\delta}$, $\log\frac1{1-2\delta}\ge2\delta$ ✓ correcta.

**Conclusión del ataque 1: la prueba SOBREVIVE.** El paso donde "podía morir" (la forma bilineal con $F_0$ de longitud $TX>T$) está bien resuelto precisamente porque el test $D$ es corto y la diagonal compartida vive solo en los primos $(X,Y]$; el doc maneja el error de la ecuación aproximada correctamente. La elección $x=T$ (no la approximate functional equation simétrica) es la correcta: evita la parte $\chi$ por completo a costa de la longitud $TX$, que la forma ponderada de Hilbert tolera.

### 1.2. ¿Puede la diagonal compuesta compensar negativamente?

No aplica: la prueba nunca usa la diagonal completa $\sum|A_n|^2/n$ (que para longitud $TX>T$ ni siquiera domina el momento); usa Cauchy–Schwarz, que es insensible al signo del resto. La restricción a primos es legítima como cota inferior de $\int|G|^2\ge|\langle G,D\rangle|^2/\|D\|^2$ sin hipótesis de positividad adicional. ✓

---

## 2. Ataque 2: normalización y la cadena 191.A ⟹ 191.B ⟹ barrera

**Verificado contra el texto de D180 §1.4.** [PROP 180.3] hipótesis (M): $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt\le1+(c-1)e^{-as\log T}$; conclusión $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}$. El $c$ de (M) en $s=0$ es $\frac1T\int|\zeta\varphi(\tfrac12+it)|^2dt$ — **idéntico al $c(\theta)$ de D191 §Coordenadas**. Sin factor $\log T$ en ninguno de los dos, sin discrepancia de peso. La comparación con la industria también cuadra: BCHB/Conrey/Farmer enuncian $\frac1T\int|\zeta\psi|^2\sim1+\frac1\theta$ en esa misma normalización. ✓

**El punto débil real está en [COR 191.B], no en la normalización — E-193.1 (errata sustantiva).** El corolario afirma que la versión desplazada de 191.A da mean$(s)-1\ge\sum_{X<p\le Y}p^{-1-2s}-o(1)$ "que reproduce la forma (M) con tasa $a\le2(1-\theta)$ por debajo". Dos problemas:

1. **La tasa está mal leída.** $\sum_{X<p\le Y}p^{-1-2s}$ está dominada en $s$ grande por el extremo INFERIOR $p\asymp X$: decae como $X^{-2s}=e^{-2\theta s\log T}$, no como $e^{-2(1-\theta)s\log T}$. La restricción correcta sobre cualquier mayorante (M) es $a\lesssim2\theta$ (más fuerte que la declarada; la declarada es consecuencia débil para $\theta<\tfrac12$, luego no es falsa, pero la prueba por sustitución directa tal como está escrita no la establece, porque…
2. **…los errores erosionan la restricción en $s$ grande.** El $-o(1)$ de la versión desplazada (tamaño $(\log T)^{-C_0/3}$) supera a $\sum p^{-1-2s}$ en cuanto $s\gtrsim\frac{\log\log T}{\theta\log T}\cdot C$, de modo que el suelo solo restringe (M) en una VENTANA $s\lesssim C'/\log T$-escala-loglog. **La conclusión del corolario sobrevive por el argumento correcto, que es más simple:** en $s\asymp1/\log T$ el suelo persiste con valor $\asymp\mathcal P\ge\delta$ (los errores son uniformes y solo mejoran con $s>0$, como el doc nota bien), luego (M) fuerza $(c-1)e^{-O(a)}\ge\delta$, es decir $c-1\ge\delta e^{-O(a)}$, y por tanto $\frac{c-1}{a}\gg\delta\cdot\frac{e^{-O(a)}}a\gg\delta$ para $a=O(1)$, mientras que $a\gg1$ exige $c-1\ge\delta e^{ca}$ — el cociente $(c-1)/a$ crece. En ambos regímenes $(c-1)/a\gg\delta$: **ganar un log es imposible en $\theta<\tfrac12$, q.e.d. del corolario con prueba reparada.** El enunciado de 191.B queda TEOREMA; la frase de la tasa debe reescribirse (versión lista en §7).

---

## 3. Ataque 3: novedad — ¿es folklore la cota diagonal $1/\theta$?

Este era el ataque diseñado para degradar el documento a folklore. **Falla, y entender por qué falla delimita la contribución exacta.**

**(a) El camino "diagonal ingenua" NO existe.** La tentación: $\int_0^T|\zeta\varphi|^2\approx T\sum_n|(1*b)(n)|^2/n$ (diagonal), y el mínimo de la forma diagonal $\sum_{n\le T}((1*b)(n))^2/n$ con $b_1=1$, soporte $[1,T^\theta]$, es un cálculo clásico de tipo criba de Selberg dual (Iwaniec–Kowalski; completar cuadrados vía inversión de Möbius) con respuesta $\asymp\log T/\log X=1/\theta$. **Pero el primer paso es falso como cota inferior incondicional:** $\zeta\varphi$ truncado honestamente tiene longitud $TX>T$, y el teorema del valor medio da $\sum|A_n|^2(T+O(n))$ donde el término $O(n)$ para $n\asymp TX$ EXCEDE $T$ y no tiene signo — la diagonal no domina, no hay cota inferior gratis. El problema diagonal clásico produce heurística, no teorema. La pieza que falta es exactamente lo que 191.A construye: un funcional (el test primo corto) que extrae una porción de la diagonal forzada de manera incondicional dentro del rango bilineal $XY\le T^{1-\eta}$.

**(b) El camino "BCHB + minimización".** BCHB 1985 evalúan el momento para coeficientes divisor-acotados generales en $\theta<\tfrac12$; el mínimo de su forma cuadrática explícita sobre coeficientes generales daría presumiblemente $1+\frac1\theta$ — cota MÁS FUERTE que 191.A. **Pero:** (i) esa minimización sobre coeficientes ARBITRARIOS (no la clase variacional suave) no la localizo escrita en ninguna parte — es precisamente [GAP-191.L1], que el doc declara con honestidad; (ii) aun existiendo, requeriría $\theta\le\tfrac12-\varepsilon$ fijo (los errores de BCHB no están enunciados con uniformidad hasta $\tfrac12-C\frac{\log\log T}{\log T}$), mientras que 191.A llega a la esquina; (iii) la versión desplazada en $s$ (que es la que la barrera NECESITA vía (M)) tampoco está en BCHB en la forma requerida, y en 191.A sale gratis.

**Veredicto de novedad:** la TASA $\log\frac{1-\theta}\theta$ es subóptima y nadie debe citarla como el suelo verdadero; el TEOREMA (cota inferior incondicional sobre la clase divisor-acotada completa, elemental, uniforme hasta la esquina, con versión desplazada) **no está en la literatura que conozco** (Farmer 1993 hace cálculo variacional sobre su clase, no cotas inferiores universales; Goldston–Gonek tratan mínimos de formas con $\Lambda,\mu$ en problemas hermanos, no este momento; Bettin–Gonek tratan consecuencias de $\theta=\infty$, no suelos). La obligación pre-publicación es la búsqueda 191.L1 tal como el doc ya ordena — el riesgo residual de folklore se concentra en si algún experto escribió la observación (a)+(test primo); es una observación de dos páginas y pudo aparecer como lema auxiliar en la literatura de proporciones. **Riesgo: moderado-bajo. La declaración de novedad del doc es defendible tal como está formulada (con su GAP declarado).**

---

## 4. Ataque 4: uniformidad y la $o(1)$

Todos los errores son explícitos en la prueba: $T^{-\eta/2}(\log T)^{B}$ (bilineal y correctores), $O(Y/T)$ (denominador), $O(1/(\theta\log T))$ (Mertens), $T^{(\theta-1)/2}(\log T)^B$ (primer momento). Con $\eta\ge C_0\frac{\log\log T}{\log T}$, el peor es $(\log T)^{B-C_0/2}$; $C_0(\kappa,A_0)>3B+3$ basta y la dependencia $B=B(\kappa,A_0)$ es trazable ($B_3$ viene de $\sum d_{\kappa+1}(N)^2\ll x(\log x)^{(\kappa+1)^2-1}$ más $(\log T)^{2A_0}$). El enunciado "$e^{-\eta\log T/3}(\log T)^B$" del teorema es consistente con la suma de los errores. La cabecera del §0 (y del resumen externo) enuncia "$1+\log\frac{1-\theta}\theta-o(1)$" suprimiendo $\eta$ — legítimo porque $\eta$ puede tomarse $C_0\frac{\log\log T}{\log T}=o(1)$, pero el teorema formal debe enunciarse con $\eta$ o con la forma "$c(\theta)-1\ge\delta$" (E-193.4, cosmética). **Uniformidad: CORRECTA y explícita.**

---

## 5. Ataque 5: [PROP 191.C] y [PROP 191.D]

**[PROP 191.C] — CERTIFICADA.** Con $b_n=0$ en $(1,T^\alpha]$, [LEMA 191.1] da $A_p=1+b_p=1$ para TODO $p\le T^\alpha$ además de $p>X$. Test $D=\sum_{1<p\le T^\alpha}p^{-1/2-it}$: longitud $T^\alpha\le Y$, condición bilineal $XT^\alpha\le T^{\theta+\alpha}\le T^{1-\eta}$ ✓ (con $\alpha\le1-\theta-\eta$, que el rango $\alpha<\theta<\tfrac12$ garantiza). $\mathcal P=\sum_{p\le T^\alpha}1/p=\log\log T^\alpha+O(1)=\log(\alpha\log T)+O(1)$ ✓. El error sigue siendo potencia-de-log pequeña, despreciable frente a $\mathcal P\to\infty$. Único matiz: para $\alpha$ extremadamente pequeño ($T^\alpha$ acotado) $\mathcal P$ deja de divergir — el enunciado implícitamente supone $\alpha$ fijo o $\alpha\log T\to\infty$; debe decirse (incluido en E-193.4). La lectura ("cada primo no molificado cuesta $1/p$") es exacta.

**[PROP 191.D] — CERTIFICADA como condicional trivial.** Dada (TW$_y$), la prueba de 191.A se repite con $Y=T^{y-\varepsilon}$; el único paso que usaba $XY\le T^{1-\eta}$ era (iv), sustituido por hipótesis. Correcto. Observación del auditor: (TW$_y$) tal como está formulada ya INCLUYE el control de los correctores de Hardy–Littlewood (está enunciada para $\zeta\varphi$, no para $F_0$) — bien formulada. La calibración del §3.2 (la frontera es de rango, no de aritmética) es fiel a la estructura de la prueba: correcto y es la observación conceptual más valiosa del documento.

---

## 6. Erratas

- **E-193.1 (sustantiva, [COR 191.B]).** La frase "reproduce exactamente la forma (M) con tasa $a\le2(1-\theta)$ POR DEBAJO" está doblemente mal calibrada: la tasa de decaimiento del suelo es $2\theta$ (extremo $p\asymp X$), no $2(1-\theta)$; y la sustitución directa no establece restricción sobre $a$ en $s$ grande porque el error $o(1)$ supera al suelo fuera de una ventana $s=O(\log\log T/\log T)$. **Reparación (incluida aquí, §2):** usar solo la persistencia del suelo en $s\asymp1/\log T$, que fuerza $(c-1)e^{-O(a)}\ge\delta$ y por tanto $(c-1)/a\gg\delta$ en todos los regímenes de $a$. La CONCLUSIÓN del corolario (barrera = teorema en $\theta<\tfrac12$, imposible ganar un log) queda probada con esta reparación.
- **E-193.2 (menor, paso (i)).** La cota del segmento $t\le1$ "$\ll T^{1/2+\theta}$ (convexidad)": la cota natural es $\ll X^{1/2}Y^{1/2}(\log T)^B=T^{(1-\eta)/2}$; la escrita es válida como mayorante solo si se justifica $|D|\ll Y^{1/2}$ y $|\zeta|\ll1$ en $t\le1$, y aún así el exponente correcto es otro. Inocua (ambas se absorben).
- **E-193.3 (menor pero obligatoria para árbitro, paso (iv)).** La extracción de la diagonal exige la desigualdad de Hilbert generalizada PONDERADA de MV 1974 (pesos $\delta_N^{-1}\asymp N$ compensados por los $N^{-1/2}$ de los coeficientes); el doc cita el paper correcto pero no exhibe el cálculo $\sum|\alpha_NN^{-1/2}|^2\delta_N^{-1}=\sum|\alpha_N|^2$. Cinco líneas; el error final declarado ya es el correcto.
- **E-193.4 (cosmética).** (a) El titular de §0 omite $\eta$; enunciar el teorema formal con $\eta$ o en la forma "$\theta\le\tfrac12-\delta\Rightarrow c-1\ge\delta$". (b) 191.C: añadir hipótesis $\alpha\log T\to\infty$. (c) En el enunciado de 191.A el rango de $\eta$ aparece con una frase rota ("…más precisamente"); formalizar.

---

## 7. Enunciado listo para el paper (versión del auditor)

**Teorema.** *Sean $\kappa\in\mathbb N$, $A_0>0$. Existe $C_0=C_0(\kappa,A_0)$ tal que: para todo $T$ grande, todo $\delta$ con $C_0\frac{\log\log T}{\log T}\le\delta\le\tfrac12$, todo $\theta\le\tfrac12-\delta$ y todo polinomio de Dirichlet $\varphi(s)=\sum_{n\le T^\theta}b_nn^{-s}$ con $b_1=1$ y $|b_n|\le d_\kappa(n)(\log T)^{A_0}$, se tiene*
$$\frac1T\int_0^T\big|\zeta\varphi(\tfrac12+it)\big|^2\,dt\;\ge\;1+\log\frac{1-\theta-\delta}{\theta}-\delta\;\ge\;1+\delta.$$
*Más generalmente, para $0\le s\le\tfrac12$: $\frac1T\int_0^T|\zeta\varphi(\tfrac12+s+it)|^2dt\ge1+\sum_{T^\theta<p\le T^{1-\theta-\delta}}p^{-1-2s}-\delta$. La cota no requiere multiplicatividad, signo ni estructura alguna de $b$.*

Mecanismo a destacar en la introducción: $(1*b)(p)=1$ para todo primo fuera del soporte (rigidez de convolución) + test corto en primos vía Cauchy–Schwarz dentro del rango bilineal de Montgomery–Vaughan; señalar explícitamente que la tasa $\log\frac{1-\theta}\theta$ es inferior a la conjetural $\frac1\theta$ y por qué (el test solo ve los primos de la cola). Cita obligada y comparación: BCHB 1985 (evaluación, no cota inferior universal), Farmer 1993 (optimalidad conjetural), MV 1974 (forma ponderada). Pre-requisito: cerrar [GAP-191.L1] con búsqueda real.

## 8. Impacto sobre la arquitectura

1. **R1: la barrera #2 ([PROP 180.3]) es TEOREMA en $\theta<\tfrac12$** sobre la clase divisor-acotada (que agota la industria), con [COR 191.B] reparado por E-193.1. El residuo condicional en $\theta\in[\tfrac12,1]$ (rango-difícil, (TW$_y$)) queda como D191 lo calibra.
2. La frase para P49/el programa: *el conducto molificador está cerrado por teorema en rango corto; el único resquicio es el rango bilineal más allá de la raíz cuadrada.* El residuo vivo del muro vuelve a ser único: [GAP-180.1] ($\mu_2=o(1)$).
3. Publicación: nota corta autónoma (≈4–6 pp.), condicionada a 191.L1 y a incorporar E-193.1–E-193.4. El valor para el lector externo es doble: la cota universal y la localización exacta de la frontera $\theta=\tfrac12$ como frontera de RANGO.

**Veredicto final: CERTIFICADO-PUBLICABLE.** Contribución exacta: el puente incondicional (rigidez de convolución + test primo) que convierte la heurística diagonal en cota inferior sobre la clase general — no la tasa, que es subóptima y debe presentarse como tal.
