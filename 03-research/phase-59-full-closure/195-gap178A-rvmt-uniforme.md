# Documento 195 — Cierre del GAP-178.A: el conteo de Riemann–von Mangoldt en ventanas unitarias es uniforme en $t\in[0,1]$ para la $H_t$ aritmética (teorema completo vía Jensen con convolución vertical)

**Programa:** Hipótesis de Riemann — Fase 59 (cierre total)
**Fecha:** 2026-06-12
**Mandato:** probar [GAP-178.A] = [PUENTE 178.5] (Doc 178 §2.6): la hipótesis (RvM-t), único insumo técnico pendiente de la mitad dinámica de la Torre 2 (Thms 178.4/178.4′/178.7/178.10).
**Contrato:** [TEOREMA]/[LEMA] solo con prueba completa; muertes documentadas; citas backward-only (de Bruijn 1950; Ki–Kim–Lee 2009; Polymath 15, 2019; Titchmarsh, *Theory of the Riemann Zeta-Function*, para RvM clásico, Stirling y convexidad).

---

## 0. Convenciones y enunciado exacto

Carta de Polymath 15 como en Doc 167 §0.1 / Doc 178 §0: $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}$, con $\partial_tH_t=-\,\partial_z^2H_t$ y $H_0=\tfrac18\,\Xi(\cdot/2)$, i.e. $H_0(z)=\tfrac18\,\xi\!\bigl(s(z)\bigr)$, $s(z):=\tfrac12+\tfrac{iz}2$. Los ceros de $\zeta$ en la franja $0<\sigma<1$ corresponden a ceros de $H_0$ en la banda $|\operatorname{Im}z|<1$; "altura $\gamma$" = $\operatorname{Re}z\asymp\gamma$ (reescalado fijo del Doc 178, irrelevante para constantes absolutas). $L:=\log\gamma$, $\rho:=L/4\pi$.

**[ENUNCIADO OBJETIVO (RvM-t), verbatim Doc 178 §2.3].** *Existe $C_0$ absoluto tal que para todo $t\in[0,1]$ y todo intervalo $J\subset\mathbb R$ con $|J|\le1$ centrado a altura $\gamma$ grande: $\#\{x\in Z_t\cap J\}\le\rho(\gamma)|J|+C_0\log\gamma$* (ceros reales de $H_t$, con multiplicidad). Probaremos algo más fuerte: el conteo de **todos** los ceros (reales o no) de $H_t$ en la caja $J\times[-1,1]$ es $\le C_0\log\gamma$, uniforme en $t\in[0,1]$.

**Verificación de signo (obligada por el mandato).** El mandato escribe "forward $\partial_tH=\partial_z^2H$, convolución gaussiana sobre $w$ REAL". En la carta del Doc 178 el signo es el **opuesto** ($e^{tu^2}$ en Fourier: de Bruijn 1950), y por tanto la representación integral correcta es la convolución **vertical**:

**[LEMA 195.0] (representación vertical).** Para $t>0$ y todo $z\in\mathbb C$,
$$H_t(z)\;=\;\frac1{\sqrt{4\pi t}}\int_{\mathbb R}H_0(z+iw)\,e^{-w^2/4t}\,dw .$$
*Prueba.* Para $H_0=\cos(\lambda z)$: $\cos(\lambda(z+iw))=\tfrac12(e^{i\lambda z-\lambda w}+e^{-i\lambda z+\lambda w})$ y $\frac1{\sqrt{4\pi t}}\int e^{\pm\lambda w-w^2/4t}dw=e^{t\lambda^2}$, luego el promedio es $e^{t\lambda^2}\cos(\lambda z)$ — exactamente el factor $e^{tu^2}$ de la carta. El caso general sigue por superposición: $H_0(z+iw)=\int_0^\infty\Phi(u)\cos((z+iw)u)du$ con $\Phi$ de decaimiento superexponencial, Fubini aplica ($\int\int\Phi(u)e^{|w|u-w^2/4t}<\infty$ pues $u^2$ pierde contra $w^2/4t$… más precisamente $\int e^{|w|u-w^2/4t}dw=O(e^{tu^2})$ y $\int\Phi e^{u^2}<\infty$). $\square$

Esta corrección de signo no es pedante: es **la razón por la que la ruta 1 cierra en todo $[0,1]$** (Observación 195.6).

Factorización aritmético–arquimediana: para $\sigma=\operatorname{Re}s>1$, $\xi(s)=\mathfrak G(s)\,\zeta(s)$ con $\mathfrak G(s):=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)$, y $\zeta(s)=\sum n^{-s}$ absolutamente convergente. Escribimos $\mathfrak g(z):=\mathfrak G(s(z))$ (holomorfa y sin ceros en $\operatorname{Re}z>0$, $\operatorname{Im}z<-1$, región donde la usamos).

---

## 1. Los dos lemas de tamaño (Stirling)

Sea $\gamma$ grande y $z_0:=\hat\gamma-iB$ con $\hat\gamma:=\gamma+\tfrac12$ (centro de la ventana) y $B\ge6$ par fijo (se elegirá absoluto en §3). Entonces $s(z_0)=\tfrac12+\tfrac B2+\tfrac{i\hat\gamma}2$, con $\sigma_0=\tfrac12+\tfrac B2\ge\tfrac72$.

**[LEMA 195.1] (envolvente local de $H_0$ en una franja).** Existen $A,C>0$ absolutos tales que para $x\ge2$, $|y|\le 4B+8$:
$$|H_0(x+iy)|\;\le\;C\,(1+x)^{A}\,|\mathfrak g(x)|\;e^{\varphi(x)\,|y|},\qquad \varphi(x):=\tfrac14\log\tfrac{x}{4\pi}.$$
*Prueba.* Por la ecuación funcional $\xi(s)=\xi(1-s)$ basta $\operatorname{Im}z\le0$, i.e. $\sigma\ge\tfrac12$. Stirling uniforme en $\sigma\in[\tfrac12,\,2B+5]$, $|s|\asymp x$: $\log|\mathfrak G(\sigma+i\tau)|=\log|\mathfrak G(\tfrac12+i\tau)|+(\sigma-\tfrac12)\cdot\tfrac12\log\tfrac{|\tau|}{2\pi}+O(\log(2+|\tau|))$; con $\tau=x/2$, $\sigma-\tfrac12=|y|/2$, el incremento es $\varphi(x)|y|+O(\log x)$. Para $\zeta$: en $\sigma\ge2$, $|\zeta|\le\zeta(2)$; en $\tfrac12\le\sigma\le2$, $|\zeta(s)|\le C|s|$ (cota de convexidad cruda, [Titchmarsh §5]). Los factores $O(\log x)$ y $|s|$ se absorben en $(1+x)^A$. $\square$

**[LEMA 195.2] (expansión exacta de primer orden de $\mathfrak g$ a lo largo de la vertical).** Sea $\psi:=-\frac{d}{dw}\log\mathfrak g(z_0+iw)\big|_{w=0}$. Entonces $\psi=\varphi(\hat\gamma)+\tfrac{i\pi}8+O(\hat\gamma^{-1})$ y, para $-\gamma/2\le w\le B-4$,
$$\mathfrak g(z_0+iw)\;=\;\mathfrak g(z_0)\,e^{-\psi w+R(w)},\qquad |R(w)|\le C\,w^2/\gamma .$$
*Prueba.* $\frac{d}{dw}\log\mathfrak g(z_0+iw)=i\cdot\frac{i}{2}\frac{d}{ds}\log\mathfrak G=-\tfrac12\bigl[\tfrac12\log\tfrac{s}{2\pi}+O(|s|^{-1})\bigr]$; con $s\approx i\hat\gamma/2$, $\log\tfrac{s}{2\pi}=\log\tfrac{\hat\gamma}{4\pi}+\tfrac{i\pi}2+O(\hat\gamma^{-1})$, lo que da $\psi$. En el segmento indicado $\sigma\in[\tfrac52,\tfrac\gamma4+B]$ y $|s|\asymp\gamma$, luego $\bigl|\tfrac{d^2}{dw^2}\log\mathfrak g\bigr|=\tfrac14\bigl|\tfrac{d}{ds}\log\tfrac{s}{2\pi}+\dots\bigr|\le C/\gamma$; Taylor con resto integral da $R$. $\square$

(Nota: $\varphi=\pi\rho+O(1)$: el "frente de fase" de $\xi$ es la densidad RvM — coherencia interna.)

---

## 2. La cota inferior puntual, uniforme en $t\in[0,1]$

**[TEOREMA 195.3] (no-anulación cuantitativa en $z_0$).** Existen $B$ (par, absoluto), $c>0$, $A'>0$ absolutos tales que para todo $t\in[0,1]$ y $\gamma\ge\gamma_0$:
$$|H_t(z_0)|\;\ge\;c\,\gamma^{-A'}\,|\mathfrak g(\hat\gamma)|\;e^{B\varphi+t\varphi^2},\qquad \varphi=\varphi(\hat\gamma).$$
*Prueba.* Caso $t=0$: $|H_0(z_0)|=\tfrac18|\mathfrak g(z_0)||\zeta(s_0)|\ge\tfrac18|\mathfrak g(z_0)|(2-\zeta(\sigma_0))\ge c|\mathfrak g(\hat\gamma)|e^{B\varphi}\gamma^{-A'}$ (Lema 195.2 para comparar $|\mathfrak g(z_0)|$ con $|\mathfrak g(\hat\gamma)|e^{B\varphi}$ módulo $\gamma^{O(1/\gamma)}$ y polinomios; $\zeta(\sigma_0)<2$ pues $\sigma_0\ge\tfrac72$). Sea $t\in(0,1]$. Por el Lema 195.0, $8H_t(z_0)=(4\pi t)^{-1/2}\int\xi(s(z_0+iw))e^{-w^2/4t}dw$. Partimos $\mathbb R=G\cup G^c$, $G:=(-\gamma/2,\,w_c]$, $w_c:=B-4$ (en $G$, $\sigma(w)=\tfrac12+\tfrac{B-w}2\ge\tfrac52$: rango de factorización).

**(i) Término principal.** En $G$: $\xi=\mathfrak g\cdot(1+(\zeta-1))$. El término con el $1$:
$$\frac{\mathfrak g(z_0)}{\sqrt{4\pi t}}\int_G e^{-\psi w+R(w)}e^{-w^2/4t}dw .$$
La gaussiana completa sin $R$: $(4\pi t)^{-1/2}\int_{\mathbb R}e^{-\psi w-w^2/4t}dw=e^{t\psi^2}$ (exacto, cuadrado completado; $\psi$ complejo, sin desplazar contornos), con $|e^{t\psi^2}|=e^{t(\varphi^2-\pi^2/64)+O(t\varphi/\gamma)}\ge0.85\,e^{t\varphi^2}$ para $\gamma$ grande. Errores: (a) colas — en $w>w_c$, $|e^{-\psi w}|=e^{-\varphi w}$ y $e^{-w^2/4t}\le1$ dan masa relativa $\le e^{-\varphi w_c-w_c^2/4t-t\varphi^2}\cdot e^{t\varphi^2}\!\big/e^{t\varphi^2}$; como $\tfrac{w_c^2}{4t}+t\varphi^2\ge\varphi w_c$ (AM–GM), la cola relativa al principal es $\le e^{-2\varphi w_c}\cdot O(\sqrt{1+t}\,(1+\varphi\sqrt t))=O(\gamma^{-w_c/2+\epsilon})$; en $w<-\gamma/2$, $e^{\varphi\gamma/2-\gamma^2/16t}\le e^{-\gamma^2/32}$ para $t\le1$, despreciable frente a todo lo presente. (b) curvatura — $|e^{R}-1|\le C\tfrac{w^2}\gamma e^{Cw^2/\gamma}$ y la masa efectiva de $e^{-\varphi w-w^2/4t}$ vive en $|w|\le2t\varphi+C\sqrt t\le C L$: contribución relativa $O(L^2/\gamma)$. Total: término principal $=\mathfrak g(z_0)e^{t\psi^2}(1+O(\gamma^{-1/2}))$, de módulo $\ge0.8\,|\mathfrak g(z_0)|e^{t\varphi^2}$.

**(ii) Error aritmético en $G$.** $|\zeta(s(w))-1|\le\zeta(\sigma(w))-1\le\zeta(\tfrac52)-1<0.342$ puntualmente en $G$; por triángulo y el mismo cálculo de Laplace sobre $|\mathfrak g(z_0+iw)|=|\mathfrak g(z_0)|e^{-\varphi w+\operatorname{Re}R}$:
$$\Bigl|\frac1{\sqrt{4\pi t}}\int_G\mathfrak g\,(\zeta-1)\,e^{-w^2/4t}dw\Bigr|\;\le\;0.342\,|\mathfrak g(z_0)|\,e^{t\varphi^2}\,(1+O(\gamma^{-1/2})).$$
Margen: $0.8-0.342>0.45$. *(Aquí está el único ajuste fino: el déficit $e^{-t\pi^2/64}\ge0.85$ del término principal debe superar $\zeta(\sigma_0')-1$ en el rango bueno; $\sigma\ge\tfrac52$ basta con holgura. No se necesita ninguna cancelación: solo convergencia absoluta de la serie de Dirichlet.)*

**(iii) Resto $w\in(w_c,\infty)$** (la vertical cruza la banda de ceros y sale por arriba; ahí no hay factorización, solo el Lema 195.1 con $|y(w)|=|w-B|$):
$$\le\;C\gamma^{A}|\mathfrak g(\hat\gamma)|\,\frac1{\sqrt{4\pi t}}\int_{w_c}^\infty e^{\varphi|w-B|-w^2/4t}dw\;\le\;C\gamma^{A}|\mathfrak g(\hat\gamma)|\,e^{t\varphi^2}\,e^{-2\varphi w_c}\,,$$
usando otra vez $\varphi w+\tfrac{w^2}{4t}+t\varphi^2\ge2\varphi w\ge2\varphi w_c$ en la rama $w\le B$ y $\varphi(w-B)-\tfrac{w^2}{4t}\le t\varphi^2-2B\varphi$ en la rama $w>B$. Como $|\mathfrak g(z_0)|\ge c\gamma^{-A}|\mathfrak g(\hat\gamma)|e^{B\varphi}$, el resto relativo al principal es $\le C\gamma^{2A}e^{-2\varphi w_c-B\varphi}=C\gamma^{2A-(w_c/2)-(B/4)}\cdot(4\pi)^{O(B)}$. **Elección absoluta:** $B:=8A+16$ (luego $w_c=8A+12$): el exponente es $\le-2$. Sumando (i)–(iii): $|8H_t(z_0)|\ge0.4\,|\mathfrak g(z_0)|e^{t\varphi^2}$, y el Lema 195.2 traduce $|\mathfrak g(z_0)|\ge c\gamma^{-A'}|\mathfrak g(\hat\gamma)|e^{B\varphi}$. $\square$

**Lectura estructural.** El flujo de la carta ($e^{tu^2}$) **amplifica** el modo arquimediano: $e^{+t\varphi^2}$. La amplificación aparecerá idéntica en la cota superior y se cancela en el cociente de Jensen. El término dominante es el $n=1$ de la serie de Dirichlet en *todo* el rango $t\in[0,1]$ porque el punto de silla de la integral vertical está en $w^*\approx-2t\varphi$ (profundidad $\asymp tL$, i.e. $\sigma\asymp tL$ creciente): **el flujo empuja la evaluación efectiva hacia la región de convergencia absoluta**, donde $\zeta\to1$. Cuanto mayor $t$, más dominante el $n=1$.

---

## 3. La cota superior local y Jensen

**[LEMA 195.4] (cota superior local, uniforme en $t$).** Para $|z-z_0|\le 2B+4$ y $t\in[0,1]$:
$$|H_t(z)|\;\le\;C\,\gamma^{A}\,|\mathfrak g(\hat\gamma)|\,e^{(3B+4)\varphi+t\varphi^2}.$$
*Prueba.* Triángulo en el Lema 195.0 + Lema 195.1 (con $|y|\le|\operatorname{Im}z|+|w|\le 3B+4+|w|$ donde para $|w|$ grande se usa la cota global de orden $1$ de $\xi$, $\log|H_0(x+iy)|\le C(1+|y|)\log(2+|x|+|y|)$, aplastada por $e^{-w^2/4t}$ con $t\le1$):
$(4\pi t)^{-1/2}\int e^{\varphi|w|-w^2/4t}dw\le 2e^{t\varphi^2}+O(1)$; la variación horizontal de $|\mathfrak g(x)|$ en $|x-\hat\gamma|\le2B+4$ es $\gamma^{O(1)}$, absorbida en $\gamma^A$ (re-etiquetando $A$). $\square$

**[TEOREMA 195.5] (= (RvM-t); GAP-178.A cerrado).** Existe $C_0$ absoluto tal que para todo $t\in[0,1]$ y todo $\gamma\ge2$, el número de ceros de $H_t$ (con multiplicidad) en la caja $[\gamma,\gamma+1]\times[-1,1]$ es $\le C_0\log\gamma$. En particular vale el enunciado (RvM-t) del Doc 178 §2.3.
*Prueba.* Para $\gamma\ge\gamma_0$: la caja está contenida en $D(z_0,r_1)$, $r_1:=B+2$ (distancia del centro $z_0=\hat\gamma-iB$ a cualquier punto de la caja $\le\sqrt{\tfrac14+(B+1)^2}<B+2$). Jensen con $r_2=2r_1$:
$$N\;\le\;\frac{1}{\log2}\Bigl[\log\max_{|z-z_0|\le 2r_1}|H_t|-\log|H_t(z_0)|\Bigr]\;\le\;\frac{1}{\log 2}\Bigl[(2B+4)\varphi+(A+A')\log\gamma+C\Bigr]\;\le\;C_0\log\gamma,$$
por los Teoremas 195.3 y Lema 195.4: **los términos $t\varphi^2$ se cancelan exactamente** y lo que queda es lineal en $\log\gamma$ con constantes absolutas, uniforme en $t\in[0,1]$ (el caso $t=0$ es el clásico, [Titchmarsh §9.2], o el límite $t\to0^+$ de lo anterior). Para $2\le\gamma\le\gamma_0$: $(t,z)\mapsto H_t(z)$ es continua, $H_t\not\equiv0$ (su transformada de Fourier $e^{tu^2}\Phi$ no es nula), y por Hurwitz + compacidad de $[0,1]$ el conteo en el compacto fijo $[0,\gamma_0+1]\times[-1,1]$ está acotado uniformemente en $t$; se absorbe en $C_0$. $\square$

---

## 4. Muertes y observaciones

**[OBS 195.6] (por qué el signo decide; muerte de la lectura "forward").** Con el signo del mandato ($\partial_tH=+\partial_z^2H$, convolución gaussiana **horizontal**) la misma estrategia muere para $t\gtrsim1/\log\gamma$: el modo arquimediano local tiene frecuencia compleja $-\tfrac\pi8\pm i\varphi$ y el calor *forward* lo amortigua por $e^{-t\varphi^2}$, hundiendo el valor en $z_0$ bajo los términos $n\asymp\sqrt{\gamma}$ del rango central de la ecuación funcional aproximada (cuya cota inferior puntual es un problema de no-anulación de sumas cortas, fuera de alcance); el costo de Jensen sería $t\log^2\gamma$. Verificamos por eso la convención del Doc 178 §0 línea a línea: es la de de Bruijn ($e^{tu^2}$), backward en $z$, y entonces la amplificación $e^{+t\varphi^2}$ es **común** a máximo y centro y se cancela. La frase del mandato "la convolución es sobre la recta real (de Bruijn §2)" es incorrecta en esta carta; la versión correcta es el Lema 195.0. Esta corrección es la prueba.

**[OBS 195.7] (ruta 2 innecesaria; su muerte).** La transferencia por flujo (conteo en $t=0$ + flujo neto por el borde) es circular en su forma natural: la velocidad de los ceros se acota con el conteo (Lema 178.6 ya la necesita) y el flujo por el borde requiere minorar $|H_t|$ en el borde — el mismo problema que la ruta 1 resuelve directamente. No ejecutada: la ruta 1 cerró.

**[OBS 195.8] (ruta 3 innecesaria).** No se invoca ningún enunciado efectivo de [P15] ni las asintóticas de [KKL 2009]: la prueba usa solo Stirling, la serie de Dirichlet en $\sigma\ge\tfrac52$, convexidad cruda de $\zeta$ en una franja fija y la representación integral de de Bruijn. El [GAP de literatura] del Puente 178.5 queda sustituido por prueba autocontenida.

**[OBS 195.9] (qué es más fuerte que lo pedido).** (a) Se cuenta la caja compleja entera, no solo ceros reales; (b) la uniformidad es en todo $t\in[0,1]$ (y la prueba da igual $t\in[0,T_0]$ con $C_0(T_0)$ para cualquier $T_0$ fijo), mientras los Thms 178.4/178.4′ solo la usan en $t\le C'L^{-2}$; (c) subproducto: $H_t(\hat\gamma-iB)\ne0$ con minorante explícito — una "región libre de ceros cuantitativa" bajo el eje, uniforme en el flujo, coherente con de Bruijn 1950 (la banda de ceros no crece) pero independiente de él.

**Test anti-circularidad.** Inputs: Stirling (Γ), convergencia absoluta de $\sum n^{-s}$ en $\sigma>1$, $|\zeta|\le C|s|$ en $\tfrac12\le\sigma\le2$ (convexidad, sin regiones libres de ceros), ecuación funcional de $\xi$, representación de de Bruijn. **No** se usa: ninguna información sobre posición de ceros de $\zeta$ ni de $H_t$, ninguna hipótesis tipo RH/densidad, ningún resultado de los Docs 167–190 (solo se *cita* el enunciado a probar del Doc 178). El conteo concluido no reentra en ningún input. Sin circularidad.

---

## 5. Veredicto

**[GAP-178.A] CERRADO: (RvM-t) es un [TEOREMA] (195.5), incondicional y uniforme en $t\in[0,1]$, con prueba completa y autocontenida.** Consecuencias inmediatas para la Torre 2 (mitad dinámica):

1. **[Thm 178.4/178.4′]** pierde la condición "(RvM-t)": queda condicional **solo** a la realidad local (R) en $[t/2,t]$ — que es hipótesis estructural declarada, no deuda técnica. La mitad dinámica de la Torre 2 queda **sobre teoremas**.
2. **[Lema 178.3]** (bloques comprimidos cortos) es ahora incondicional.
3. **[Thm 178.7]** y **[Thm 178.10]** (177.B ⟺ confinamiento) pierden el módulo "(RvM-t)"; lo irreducible sigue siendo 178.C/el confinamiento en $t=0$, exactamente como diagnosticó el Doc 178 — la calibración cuasi-RH-difícil de 177.B no cambia.

**GAPs residuales de este documento:**
- **[GAP-195.A] (menor, cosmético):** las constantes $A,B,C_0$ no están optimizadas numéricamente (el contrato excluye numérica); cualquier uso futuro que necesite $C_0$ explícito debe rehacer §1–§3 con Stirling explícito — rutina, sin pared.
- Ningún GAP matemático queda abierto sobre (RvM-t).

**Estado de la Torre 2 tras este documento:** pinza estática $178.\mathrm C\wedge\mathrm{LP}\text{-}134^\infty\Rightarrow m<\infty$ (Cor 178.11, certificada en Phase 58) + mitad dinámica 178.4′ ahora libre de deuda técnica. Los objetos duros restantes son los de siempre: 178.C y LP-134∞.
