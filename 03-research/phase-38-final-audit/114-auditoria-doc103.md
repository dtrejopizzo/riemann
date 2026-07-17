# Documento 114 — Auditoría adversarial del Doc 103 (positividad de $W_\lambda$ y afilado de P39)

**Programa:** Hipótesis de Riemann — Fase 38 (auditoría final)
**Fecha:** junio 2026
**Rol:** auditor adversarial — mandato: destruir el resultado antes de su uso público
**Objetos auditados:** Doc 103 (Lema 2.1, Teorema 2.2, Teorema 3.1), Doc 63 §3 y §7, Doc 76 §4, Doc 83 §1, P39 (`06-papers/P39-ccm-trace-criterion/main.tex`, Def. `def:Wlambda`, Thm. `thm:Wpos`, Thm. `thm:main`)

---

## Veredicto anticipado

**REFUTADO.** El kernel $W_\lambda$ realmente definido en Doc 63 §5.2 / P39 Def. `def:Wlambda`,
$$W_\lambda(s) = \sum_{n\,:\,\gamma_n\leq\lambda} (a_n^\infty)^2\bigl(|\mathcal{P}_{n+1}(s)|^2-|\mathcal{P}_n(s)|^2\bigr),$$
**no es no-negativo**: toma valores estrictamente negativos en regiones abiertas de $\mathbb{R}$, para todo $\lambda$. La forma "sumada por partes" de Doc 63 §7.1 / Doc 103 ec. (1) / P39 ec. `eq:abel`,
$$\sum_{n=1}^{N} n\,|\mathcal{P}_n|^2 + (a_N^\infty)^2|\mathcal{P}_{N+1}|^2,$$
**no es igual a $W_\lambda$**: la suma de Abel está hecha con el signo del término interior invertido y con el término de frontera inferior omitido, y además el coeficiente "$n$" está mal calculado (el valor correcto de la diferencia de cuadrados es $2n+\tfrac12$, no $n$). El Teorema 2.2 del Doc 103 es verdadero *para el polinomio de la ec. (1)*, pero ese polinomio no es $W_\lambda$; aplicado al verdadero $W_\lambda$ es **falso**. El Teorema 3.1 (afilado de P39 a un solo $\lambda_0$) queda **sin sustento**, y —peor— la dirección $(ii)\Rightarrow(i)$ del propio teorema principal de P39 (Thm. `thm:main`), que se apoya en Thm. `thm:Wpos`, queda **sin demostración**.

El único enunciado que sobrevive es el Lema 2.1 (no-anulación simultánea de $\mathcal{P}_n,\mathcal{P}_{n+1}$), que es teoría clásica correcta (Szegő). Pero blinda un teorema sobre el kernel equivocado.

---

## §1. La prueba de un renglón: $W_\lambda$ tiene media $dm_\infty$ nula

Antes de cualquier álgebra de sumas de Abel, hay un argumento estructural que decide la cuestión. Los $\{\mathcal{P}_n\}$ son **ortonormales** respecto de $dm_\infty$: $\int |\mathcal{P}_n|^2\,dm_\infty = 1$ para todo $n$. Integrando la definición de $W_\lambda$ término a término:
$$\int_\mathbb{R} W_\lambda(s)\,dm_\infty(s) \;=\; \sum_{n\,:\,\gamma_n\leq\lambda} (a_n^\infty)^2\,\bigl(\,\underbrace{\|\mathcal{P}_{n+1}\|^2_{L^2(dm_\infty)}}_{=1} - \underbrace{\|\mathcal{P}_n\|^2_{L^2(dm_\infty)}}_{=1}\,\bigr) \;=\; 0.$$
**Exactamente cero, para todo $\lambda$.** Un kernel continuo, no idénticamente nulo, con integral cero contra una medida de soporte $\mathbb{R}$, **no puede ser no-negativo**. Esto refuta de un golpe:

- Doc 63, Cor. 7.2 ("$W_\lambda \geq 0$"): **falso**.
- P39, Thm. `thm:Wpos` ("$W_\lambda(s)\geq 0$ para todo $\lambda,s$"): **falso**.
- Doc 103, Teorema 2.2 ("$W_\lambda > 0$ en todo $\mathbb{R}$"): **falso** para el verdadero $W_\lambda$.

Nótese que esta misma integral está calculada en el **Doc 76, Prop. 4.1**, que obtiene $\widehat{W_\lambda dm_\infty}(0) = \frac{N(N+1)}{2}+(a_N^\infty)^2 > 0$ usando la forma sumada por partes. La contradicción $0 \neq \frac{N(N+1)}{2}+(a_N^\infty)^2$ es la demostración interna, con los propios documentos del programa, de que **la forma sumada por partes no es igual a la definición**. (Toda la serie de Fourier del Doc 76 hereda el error.)

---

## §2. Línea de ataque 1: la identidad $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ es aritméticamente falsa

Con $a_k^\infty = \tfrac12\sqrt{(2k+1)(2k+2)}$ (definición usada de forma consistente en Doc 63 Prop. 7.1, Doc 103 §1, P39 líneas 48, 128, 296):
$$(a_k^\infty)^2 = \frac{(2k+1)(2k+2)}{4} = \frac{4k^2+6k+2}{4}.$$
Entonces
$$(a_n^\infty)^2-(a_{n-1}^\infty)^2 = \frac{(4n^2+6n+2)-(4n^2-2n)}{4} = \frac{8n+2}{4} = 2n+\tfrac12 \;\neq\; n.$$
- Doc 63, Prop. 7.1 (línea 146): afirma que la diferencia "$= n$". **Falso**: es $2n+\tfrac12$.
- Doc 103, ec. (1) y §1: copia "$(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ (cálculo directo)". **Falso**, mismo error.
- P39, prueba de `thm:Wpos` (línea 519) y Remark posterior: afirma $(a_{n+1}^\infty)^2-(a_n^\infty)^2 = n+1$ y que "the differences of its square are exactly the positive integers". **Falso**: $(a_{n+1}^\infty)^2-(a_n^\infty)^2 = \frac{(4n^2+14n+12)-(4n^2+6n+2)}{4} = \frac{8n+10}{4} = 2n+\tfrac52$.

Por sí solo, este error sería benigno ($2n+\tfrac12 > 0$ igual que $n > 0$: "fórmula mal copiada, teorema sobrevive"). La sucesión que sí cumple "diferencias $=n$" sería $(a_n)^2 = n(n+1)/2$, que no es la CCM. El error fatal es el siguiente.

## §3. Línea de ataque 2: la suma de Abel tiene el signo interior invertido y omite la frontera inferior

Suma de Abel correcta, con $u_n=(a_n^\infty)^2$, $v_n=|\mathcal{P}_n(s)|^2$, índices consecutivos $n_0,\dots,N$:
$$\sum_{n=n_0}^{N} u_n(v_{n+1}-v_n) \;=\; u_N v_{N+1} \;-\; u_{n_0}v_{n_0} \;-\; \sum_{n=n_0+1}^{N}(u_n-u_{n-1})\,v_n.$$
Los coeficientes interiores entran con **signo menos** (pues $u_n$ es creciente, $u_n-u_{n-1}=2n+\tfrac12>0$), y hay un término de frontera inferior $-u_{n_0}v_{n_0}$ que **no es despreciable** ($v_{n_0}=|\mathcal{P}_{n_0}(s)|^2$, y para $n_0=0$, $v_0\equiv 1$).

**Verificación explícita con $N=2$** (suma $n=0,1,2$; $c_n:=u_n$, $b_n:=v_n$):
$$c_0(b_1-b_0)+c_1(b_2-b_1)+c_2(b_3-b_2) = c_2 b_3 - c_0 b_0 + (c_0-c_1)b_1 + (c_1-c_2)b_2,$$
con $(c_0-c_1)<0$, $(c_1-c_2)<0$. La forma reclamada por Doc 63 §7.1 / Doc 103 (1) es
$$ (c_1-c_0)b_1 + (c_2-c_1)b_2 + c_2 b_3,$$
es decir, **signo opuesto en ambos coeficientes interiores y frontera inferior $-c_0b_0$ eliminada**. No hay reindexación ni convención de signos de $\kappa_n$ que reconcilie las dos expresiones (probé las dos orientaciones $\kappa_n = \pm(a_n)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$: ninguna produce coeficientes interiores positivos *y* frontera superior positiva a la vez).

**El propio Doc 63 contiene la versión correcta.** La Prop. 3.2 del Doc 63 (línea 60) escribe la suma de Abel bien:
$$\sum_{n=0}^N(a_n^\infty)^2\!\int(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)\,d\mu = (a_N^\infty)^2\!\int|\mathcal{P}_{N+1}|^2 - (a_0^\infty)^2\!\int|\mathcal{P}_0|^2 + \sum_{n=0}^{N-1}\bigl[(a_n^\infty)^2-(a_{n+1}^\infty)^2\bigr]\!\int|\mathcal{P}_{n+1}|^2,$$
con coeficientes interiores $(a_n)^2-(a_{n+1})^2 = -(2n+\tfrac52) < 0$ y frontera $-(a_0)^2\int|\mathcal{P}_0|^2$. **Doc 63 §7.1 contradice a Doc 63 §3.2.** La §3.2 es la correcta.

**Mecanismo del error en P39.** La prueba de `thm:Wpos` (líneas 514–525) enuncia la suma de Abel con frontera "$-u_{-1}v_0$" (debe ser $-u_0v_0$; el truco "$u_{-1}:=0$" borra ilegítimamente la frontera) y luego, al pasar a la ec. `eq:abel`, transcribe el término interior "$-\sum(u_{n+1}-u_n)v_{n+1}$" como "$+\sum(n+1)|\mathcal{P}_{n+1}|^2$": **dos errores de signo/frontera más el error aritmético del §2, los tres en cinco líneas**. Este es exactamente el patrón de los errores históricos del programa (Doc 93: signo; Doc 70: signo; Doc 71: bloque omitido).

**La forma correcta** (índices $0\dots N$) es:
$$W_\lambda(s) = (a_N^\infty)^2|\mathcal{P}_{N+1}(s)|^2 \;-\; (a_0^\infty)^2 \;-\; \sum_{n=0}^{N-1}\Bigl(2n+\tfrac52\Bigr)|\mathcal{P}_{n+1}(s)|^2.$$

## §4. Contraejemplo explícito ($N=1$): $W_\lambda$ es negativo en un intervalo macroscópico

Con $a_0^\infty=\tfrac{\sqrt2}{2}$, $a_1^\infty=\sqrt3$, $\mathcal{P}_0\equiv1$, $\mathcal{P}_1(s)=\sqrt2\,s$ (recurrencia: $s\mathcal{P}_0=a_0\mathcal{P}_1$), $\mathcal{P}_2(s)=\frac{s\mathcal{P}_1-a_0\mathcal{P}_0}{a_1}=\sqrt{\tfrac23}\,(s^2-\tfrac12)$. La definición da, sumando $n=0,1$:
$$W = \tfrac12(2s^2-1) + 3\Bigl(\tfrac23(s^2-\tfrac12)^2 - 2s^2\Bigr) = 2s^4-7s^2 = s^2(2s^2-7).$$
**$W(s)<0$ para todo $0<|s|<\sqrt{7/2}\approx 1.87$**; p. ej. $W(1)=-5$. La forma del Doc 103 ec. (1) daría en cambio $1\cdot 2s^2 + 3\cdot\tfrac23(s^2-\tfrac12)^2 = 2s^2+2(s^2-\tfrac12)^2 \geq 0$; en $s=1$ vale $+\tfrac52$. Las dos expresiones son polinomios distintos. (Verificación cruzada con la forma correcta del §3: $3\cdot\tfrac23(s^2-\tfrac12)^2 - \tfrac12 - \tfrac52\cdot 2s^2 = 2s^4-7s^2$ ✓.)

Más aún, en general: en cualquier cero $s_0$ de $\mathcal{P}_{N+1}$ (hay $N+1$, todos reales y simples: Szegő, *Orthogonal Polynomials*, AMS Colloq. Publ. 23, Thm. 3.3.1), la forma correcta da
$$W_\lambda(s_0) = -(a_0^\infty)^2 - \sum_{n=0}^{N-1}\Bigl(2n+\tfrac52\Bigr)|\mathcal{P}_{n+1}(s_0)|^2 \;\leq\; -\tfrac12 \;<\;0,$$
con desigualdad estricta reforzada porque $\mathcal{P}_N(s_0)\neq0$ (entrelazamiento). El conjunto $\{W_\lambda<0\}$ es abierto y no vacío para **todo** $N\geq 0$.

## §5. Línea de ataque 3: la cadena de definiciones Doc 63 → Doc 76 → P39 → Doc 103

- Doc 63 §5.2 (Prop. 5.2) y P39 Def. `def:Wlambda` definen $W_\lambda$ como la suma de $\kappa_n$: **coinciden** y esta es la definición vinculante, porque es la única para la cual vale la representación integral $T_\lambda = \int W_\lambda\,d\nu$ (P39 Prop. `prop:integral`), que es lo que usa todo lo demás. No hay escape redefiniendo $W_\lambda$ como la forma positiva: se perdería la identidad con $T_\lambda$.
- Doc 63 §7.1, Doc 76 §4.1 (línea 244, con coeficientes "$k$") y Doc 103 ec. (1) usan la forma sumada por partes espuria: **coinciden entre sí** (módulo el desplazamiento $n$ vs $n+1$ de P39 `eq:abel`, otro indicio de descuido), y **todas difieren de la definición**. El error nace en Doc 63 §7.1 y se propagó por copia a Doc 76, P39 y Doc 103 sin que nadie rehiciera la suma con $N=2$.
- Indexación: P39 suma "$n\geq 0,\ \gamma_n\leq\lambda$" mientras Doc 63 §7.1 produce el término superior $(a_{N(\lambda)})^2|\mathcal{P}_{N(\lambda)+1}|^2$ con $N(\lambda)=\#\{n:\gamma_n\leq\lambda\}$; si los ceros se indexan desde $n=0$ el término superior debería ser $(a_{N-1})^2|\mathcal{P}_N|^2$, si desde $n=1$ cuadra. Ambigüedad off-by-one nunca fijada; irrelevante para la refutación (cualquier rango consecutivo da coeficientes interiores negativos), pero debe fijarse en la corrección.
- Sobre si este $W_\lambda$ es "el kernel de Abel de CCM" (Connes–Consani–Moscovici): no pude verificarlo contra la fuente externa en esta auditoría offline; el nombre es interno del programa (los pesos $(a_n^\infty)^2$ no son pesos de Abel $e^{-\lambda k}$ ni de Cesàro $(1-k/N)$). Recomiendo no atribuir la forma a CCM en P39 sin cita puntual.

## §6. Línea de ataque 4 y 7: el Lema 2.1 sobrevive (es clásico)

La medida $dm_\infty$ es par (simétrica en $s\mapsto -s$; cf. Doc 83 §2, paridad de $|\zeta(1/2+is)|^2$ y del factor $\Gamma$), luego $b_n=0$ y la recurrencia (2) del Doc 103 es la convención correcta. Los $\mathcal{P}_n$ tienen coeficientes reales, así que $|\mathcal{P}_n(s)|^2=\mathcal{P}_n(s)^2$ en $\mathbb{R}$: sin problema. El argumento de descenso del Lema 2.1 es válido tal cual **también para $s_0\in\mathbb{C}$** (solo usa la recurrencia algebraica y $a_k>0$, $\mathcal{P}_0\equiv1$); el paso final usa la recurrencia en el índice $1$ ($s_0\mathcal{P}_1 = a_1\mathcal{P}_2+a_0\mathcal{P}_0$), sin necesitar $\mathcal{P}_{-1}$. La multiplicidad es irrelevante (solo se usa anulación). Es un hecho estándar: los ceros de $\mathcal{P}_n$ y $\mathcal{P}_{n+1}$ se entrelazan estrictamente y en particular no coinciden (Szegő, op. cit., Thm. 3.3.2; también B. Simon, *Szegő's Theorem and Its Descendants*, Princeton, 2011, §1.2, vía el Wronskiano de Christoffel–Darboux $a_n(\mathcal{P}_{n+1}'\mathcal{P}_n-\mathcal{P}_n'\mathcal{P}_{n+1})=\sum_{k\leq n}\mathcal{P}_k^2>0$). **No existe contraejemplo posible** a este lema para ninguna medida con momentos finitos: es estructural. Lema 2.1: **SOBREVIVE INTACTO** — pero es el cerrojo de una puerta que da a la habitación equivocada.

## §7. Líneas de ataque 5 y 6: Doc 83, Doc 89 y la convergencia (correctos pero ahora insuficientes)

- **Doc 83, Cor. 1.2**: $|\zeta|^2\geq|\zeta_{on}|^2$ puntual e incondicional, vía cociente de productos de Hadamard $\prod_j(1+\delta_j^2/(u-\gamma_j)^2)^{\,\cdot}\geq 1$. El mecanismo es sólido (cada factor $\geq1$; convergencia por $\sum\delta_j^2/\gamma_j^2<\infty$); no requiere normalización que presuponga los ceros. Concedo $d\nu\geq0$.
- $|\zeta_{on}|^2>0$ salvo ceros aislados: legítimo (conjunto discreto, $dm_\infty$-nulo).
- $d\nu=0\iff$RH (Doc 89, cond. 2): legítimo ($R\equiv1$ c.t.p. fuerza todos los $\delta_j=0$ por continuidad de los factores).
- Convergencia de $T_{\lambda_0}=\int W_{\lambda_0}\,d\nu$: $W_\lambda$ crece polinomialmente (grado $2N+2$), $dm_\infty$ decae como $e^{-\pi|s|/2}$ (factor $\Gamma$) y $|\zeta(1/2+is)|^2$ crece polinomialmente; la integral converge absolutamente. Sin objeción.

Pero todo esto es ahora insuficiente: con $W_{\lambda_0}$ **indefinido**, $T_{\lambda_0}=0$ (e incluso $T_\lambda=0$ para todo $\lambda$) es compatible a priori con $d\nu\neq0$ por cancelación entre las regiones $\{W>0\}$ y $\{W<0\}$. El paso "integrando no-negativo $\Rightarrow$ nulo c.t.p." del Teorema 3.1 ($\Leftarrow$) pierde su hipótesis. **Teorema 3.1: REFUTADO en su demostración; el enunciado queda como conjetura abierta.**

## §8. Daño colateral en P39 y resultados aguas abajo

1. **P39, Thm. `thm:Wpos`**: falso (§1, §4). Debe retirarse.
2. **P39, Thm. `thm:main`, dirección (ii)$\Rightarrow$(iii)**: la prueba invoca `thm:Wpos`; queda inválida. Observo que de $T_\lambda=0\ \forall\lambda$ sí se deduce $\Delta_n^{full}=\Delta_n^{full,on}$ término a término (diferencias consecutivas de $T_\lambda$ en los saltos $\lambda=\gamma_n$), es decir $\int\kappa_n\,d\nu=0\ \forall n$, o sea $\int|\mathcal{P}_n|^2 d\nu$ constante en $n$. Pero **esto no implica $d\nu=0$** sin un argumento nuevo (una medida positiva cuya densidad respecto de $dm_\infty$ sea ortogonal a todos los $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ no es automáticamente nula). El criterio RH$\iff T_\lambda=0\ \forall\lambda$ **no está demostrado** en la dirección que importa. La dirección RH$\Rightarrow T_\lambda=0$ sobrevive (trivial: $d\nu=0$).
3. **Doc 63, §7 completo** (Prop. 7.1, Cor. 7.2, Thm. 7.3, Cor. 7.5): refutado. Atención: Doc 63 §6 (línea 122) pretende $\Delta_n^{full}-\Delta_n^{full,on}\geq0$ para cada $n$ vía suma de kernels de Poisson, lo cual contradice la Obs. 2.2 del mismo documento ("$\kappa_n$ tiene signo indefinido" + $d\nu\geq0$ ⟹ signo a priori indefinido). Esa ruta alternativa, si fuera correcta, podría rescatar $T_\lambda\geq0$ sin pasar por $W_\lambda$; **requiere auditoría independiente y urgente** — es ahora el único soporte concebible del criterio.
4. **Doc 76** (transformada de Fourier de $W_\lambda dm_\infty$): toda la serie usa la forma espuria; en particular Prop. 4.1 ($\widehat{W_\lambda dm_\infty}(0)>0$) contradice el valor exacto $0$ (§1). Refutado en bloque; debe recalcularse con la forma correcta del §3 (donde, por cierto, $\widehat{\,\cdot\,}(0)=0$ saldrá automáticamente).
5. **Doc 103 íntegro** salvo el Lema 2.1; la Obs. 2.4 ($N=0$: "$W=(a_0)^2|\mathcal{P}_1|^2$") también es falsa: el valor real es $(a_0)^2(|\mathcal{P}_1|^2-1)=s^2-\tfrac12$, negativo cerca de $0$.
6. **P41**: cualquier uso del "colapso de la familia $\{T_\lambda\}$ a un punto" (Doc 103 §4, Cor. 3.2) debe retirarse.

## §9. Qué es rescatable

- $T_\lambda=\int W_\lambda\,d\nu$ con $d\nu\geq0$ (Doc 83) y la fórmula correcta de Abel del §3: todo eso es sólido como *identidad*.
- $\int W_\lambda\,dm_\infty=0$: nueva identidad exacta, gratis, que cualquier reconstrucción debe respetar.
- Lema 2.1 / entrelazamiento (Szegő 3.3.1–3.3.2): disponible para futuros usos legítimos.
- Posible vía de reparación: probar $T_\lambda>0$ bajo ¬RH directamente desde Doc 63 §6 (Poisson), o encontrar pesos $w_n>0$ tales que $\sum w_n\kappa_n$ sí sea suma de cuadrados (requeriría $w_n$ **decrecientes**, p. ej. tipo Abel genuino $w_n=e^{-\lambda n}$: con $u_n$ decreciente la suma por partes da coeficientes interiores positivos $+(u_{n-1}-u_n)$, frontera inferior $-u_{n_0}v_{n_0}$ aún negativa — habría que absorberla; no es trivial pero es la dirección correcta si se quiere un kernel positivo honesto).

## §10. Tabla de veredictos

| Enunciado | Veredicto |
|---|---|
| $(a_n^\infty)^2-(a_{n-1}^\infty)^2=n$ (D63 7.1, D103 §1, P39) | **FALSO**: $=2n+\tfrac12$ (y $2n+\tfrac52$ en la variante de P39) |
| Forma sumada por partes $=W_\lambda$ (D63 §7.1, D76 §4.1, D103 (1), P39 eq:abel) | **FALSO**: signo interior invertido + frontera $-(a_0)^2|\mathcal{P}_0|^2$ omitida; contraejemplo $N=1$: $W=s^2(2s^2-7)$ |
| $W_\lambda\geq0$ (D63 Cor 7.2, P39 thm:Wpos) | **REFUTADO**: $\int W_\lambda dm_\infty=0$ exacto; $W_\lambda<0$ en abiertos |
| Lema 2.1 (D103) | **SOBREVIVE** (clásico: Szegő Thm 3.3.2; descenso válido en $\mathbb{C}$) |
| Teorema 2.2 (D103) | **REFUTADO** para el verdadero $W_\lambda$ (verdadero solo para el kernel espurio) |
| Teorema 3.1 / Cor. 3.2 (D103), afilado a un $\lambda_0$ | **REFUTADO** (sin demostración; plausiblemente falso por cancelación) |
| P39 thm:main, (ii)$\Rightarrow$(i) | **SIN DEMOSTRACIÓN** (gap real: $\int\kappa_n d\nu=0\ \forall n \not\Rightarrow d\nu=0$ sin argumento nuevo) |
| $d\nu\geq0$ (D83), $d\nu=0\iff$RH (D89), convergencia de $T_{\lambda_0}$ | Sin objeción |

**VEREDICTO FINAL: REFUTADO** — en Doc 63 §7.1 (origen), propagado a Doc 76, P39 (`thm:Wpos` y la dirección clave de `thm:main`) y Doc 103 (Teoremas 2.2 y 3.1). El error es del mismo tipo que los de Docs 70/93/95/97: signo invertido en una suma por partes más un término de frontera omitido, ratificado por una identidad aritmética mal calculada. La detección interna estaba disponible: Doc 63 §3.2 ya contenía la suma de Abel correcta, y $\int W_\lambda\,dm_\infty=0$ era verificable en una línea.

---

*Fin del Documento 114.*
