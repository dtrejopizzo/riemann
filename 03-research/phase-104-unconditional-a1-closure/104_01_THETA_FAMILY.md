# 104_01 — La familia \(C_n^\theta\)

**Rol:** normalización. Primer teorema exacto de la fase. No contiene matemática nueva
respecto de RH; fija el objeto sobre el que trabajan `104_02` y `104_10`, y **resuelve con
signo** la pregunta de si el reparto A0/A1 congelado en \(\theta=\frac14\) puede mejorarse.

Notación de `main.tex:6718`–6729:
\[
A_n:=\lambda_n^{\rm arch},\quad
E(u):=\psi(e^u)-e^u,\quad
K_n(u):=e^{-u}L^{(2)}_{n-1}(u),\quad a:=\log 2,
\]
\[
R_n(T):=-\int_T^\infty E(u)K_n(u)\,du .
\]
Las integrales se entienden por la regularización de Abel polo–primo emparejada; en todo
\(T\) finito la primera es una integral ordinaria de la discrepancia de Chebyshev.

---

## Teorema 1 (identidad exacta, todo \(\theta\))

Para todo \(n\ge1\), todo \(\theta\in\mathbb R\) y todo cutoff admisible \(T\), sea
\[
C_n^\theta(T):=(1-\theta)A_n-n-\int_0^T E(u)K_n(u)\,du .
\]
Entonces
\[
\boxed{\;C_n^\theta(T)=\lambda_n-\theta A_n-R_n(T).\;}
\tag{1}
\]

**Demostración.** La integración por partes de Stieltjes corregida
(`main.tex:6743`–6748, con el borde \(-n\) **retenido**, erratum vinculante) da
\[
\lambda_n^{\rm prime}=-n-\int_0^\infty E(u)K_n(u)\,du,
\]
y \(\lambda_n=A_n+\lambda_n^{\rm prime}\), luego
\(\int_0^\infty EK_n=-n-\lambda_n+A_n\). Como \(\int_T^\infty EK_n=-R_n(T)\),
\[
\int_0^T EK_n=\int_0^\infty EK_n-\int_T^\infty EK_n=(-n-\lambda_n+A_n)+R_n(T).
\]
Sustituyendo en la definición,
\[
C_n^\theta(T)=(1-\theta)A_n-n+n+\lambda_n-A_n-R_n(T)=\lambda_n-\theta A_n-R_n(T).\qquad\square
\]

\(\theta=\frac14\) recupera `prop:li-compact-tail` (`main.tex:6734`). No hay intercambio de
límites ni término divergente sin emparejar.

**Corolario 1.1.** Si \(A_n>0\), \(|R_n(T_n)|\le\theta A_n\) y \(C_n^\theta(T_n)\ge0\),
entonces \(\lambda_n\ge0\).
*Prueba:* \(\lambda_n=C_n^\theta(T_n)+\theta A_n+R_n(T_n)\ge C_n^\theta(T_n)\ge0\). \(\square\)

---

## Teorema 2 (colapso y reserva)

Para todo \(n\ge1\), todo \(\theta\) y todo cutoff admisible \(T\ge a\),
\[
C_n^\theta(T)\ge0
\iff
\boxed{\;\int_{a}^{T} E(u)K_n(u)\,du\ \le\ q_{n,\theta},\qquad
q_{n,\theta}:=(1-\theta)A_n+1-L_n^{(1)}(\log 2).\;}
\tag{2}
\]

**Demostración.** Para \(0\le u<a\) no hay potencias de primo, luego \(\psi(e^u)=0\) y
\(E(u)=-e^u\), de donde \(E K_n=-L^{(2)}_{n-1}\). Como \((L_n^{(1)})'=-L^{(2)}_{n-1}\) y
\(L_n^{(1)}(0)=n+1\),
\[
\int_0^a E K_n=-\int_0^a L^{(2)}_{n-1}(u)\,du=-(n+1)+L_n^{(1)}(a).
\]
Sustituyendo en la definición de \(C_n^\theta\),
\[
C_n^\theta(T)=(1-\theta)A_n-n+(n+1)-L_n^{(1)}(a)-\int_a^T EK_n
=q_{n,\theta}-\int_a^T EK_n.\qquad\square
\]

Ninguna reserva base, término de polo ni contribución exponencial de borde sobrevive en (2):
la cancelación \(-n+(n+1)=+1\) es exacta.

**Escala.** Con \(A_n=\frac n2(\log n+\gamma-1-\log2\pi)+O(\log n)\) y
\(L_n^{(1)}(a)=O_a(n^{1/4})\) (`main.tex:6856`),
\[
q_{n,\theta}=(1-\theta)\frac n2(\log n+\gamma-1-\log 2\pi)+O(n^{1/4}+\log n).
\]
**En todo argumento se usa \(q_{n,\theta}\) exacto, nunca esta asintótica** (regla 3).

---

## Teorema 3 (A0 con \(\theta\) libre y \(T_n(\theta)\) efectivo)

Sea una estimación PNT explícita tipo Vinogradov–Korobov
\[
|\psi(y)-y|\le A\,y\,e^{-\eta(\log y)}\quad(y\ge e^{U_0}),\qquad
\frac{\eta(u)}{\log(1+u)}\to\infty ,
\]
con \(A,U_0,\eta\) **fijados de una vez** (una sola elección declarada, no optimizada por caso).
Si \(T\ge U_0\) cumple
\[
\eta(u)\ \ge\ (n+1)\log(1+u)+\log\frac{3An^2}{\theta A_n}
\qquad(u\ge T),
\tag{B$_\theta$}
\]
entonces \(|R_n(T)|\le\theta A_n\).

**Demostración.** Igual que `thm:a0-tail-direct` (`main.tex:6786`–6804): la expansión finita de
Laguerre da \(|f'_{n,\varepsilon}(y)|\le 3n^2y^{-2}(1+\log y)^{n-1}\) para \(0\le\varepsilon\le1\),
luego
\[
|R_n(T)|\le 3An^2\int_T^\infty(1+u)^{n-1}e^{-\eta(u)}\,du .
\]
(B\(_\theta\)) equivale a \(e^{\eta(u)}\ge\frac{3An^2}{\theta A_n}(1+u)^{n+1}\), luego el
integrando está mayorado por \(\theta A_n(1+u)^{-2}\) y
\(|R_n(T)|\le\theta A_n\int_T^\infty(1+u)^{-2}du\le\theta A_n\). \(\square\)

**Tripla PNT explícita fijada (declarada de una vez, no optimizada).** Johnston--Yang,
Theorem 1.4 (`2204.01980v2`), prueban para todo \(x\ge23\)
\[
 |\psi(x)-x|\le 0.026x(\log x)^{1.801}
 \exp\!\left(-0.1853{(\log x)^{3/5}\over(\log\log x)^{1/5}}\right).
\]
Por tanto se adopta la tripla más débil pero directamente compatible con el Teorema 3
\[
A=1,\qquad U_0=1000,\qquad
\eta(u)=0.1853\,u^{3/5}(\log u)^{-1/5}-1.801\log u.
\]
El factor \(0.026\le1\) se descarta favorablemente. Para \(u\ge1000\), diferenciación directa
da
\[
 u\eta'(u)=0.1853\,u^{3/5}(\log u)^{-1/5}
 \left({3\over5}-{1\over5\log u}\right)-1.801>0,
\]
y el primer término es creciente; además \(\eta(u)/\log(1+u)\to\infty\).
**Toda la fase usa esta tripla y ninguna otra.** Cualquier documento que la cambie debe decirlo
en su encabezado y rehacer \(T_n(\theta)\).

**Definición.** \(T_n(\theta):=\min\{T\ge U_0:\ \text{(B}_\theta)\ \text{vale para todo }u\ge T\}\).

**Lema 3.1 (monotonía).** Para \(0<\theta\le\theta'\) se tiene \(T_n(\theta)\ge T_n(\theta')\).

*Demostración.* Sea \(\Phi_\theta(u):=(n+1)\log(1+u)+\log\frac{3An^2}{\theta A_n}\) el lado
derecho de (B\(_\theta\)). De \(\theta\le\theta'\) sale \(\log(1/\theta)\ge\log(1/\theta')\),
luego \(\Phi_\theta\ge\Phi_{\theta'}\) puntualmente. Sea
\(S_\theta:=\{T\ge U_0:\eta(u)\ge\Phi_\theta(u)\ \forall u\ge T\}\). Si \(T\in S_\theta\)
entonces \(\eta(u)\ge\Phi_\theta(u)\ge\Phi_{\theta'}(u)\) para todo \(u\ge T\), es decir
\(T\in S_{\theta'}\). Luego \(S_\theta\subseteq S_{\theta'}\) y
\(\min S_\theta\ge\min S_{\theta'}\). \(\square\)

*(El mínimo existe: \(\eta(u)/\log(1+u)\to\infty\) garantiza \(S_\theta\ne\emptyset\), y
\(S_\theta\) es un rayo cerrado por su propia definición.)*

En particular \(T_n(\theta)\ge T_n(\tfrac14)\) para \(\theta\le\tfrac14\), que es lo que usa la
Proposición 4. Además \(|R_n(T)|\le\theta A_n\) **para todo** \(T\ge T_n(\theta)\), no solo en
\(T_n(\theta)\): (B\(_\theta\)) se pidió para todo \(u\ge T\).

**Dependencia en \(\theta\).** \(\theta\) entra en (B\(_\theta\)) **solo** por el sumando aditivo
\(\log(1/\theta)\). Con \(\eta(u)\asymp c\,u^{3/5}(\log u)^{-1/5}\), la ecuación de definición es
\(c\,T^{3/5}(\log T)^{-1/5}=(n+1)\log(1+T)+O(\log T)+
\log\frac{3An^2}{\theta A_n}\), con \(c=0.1853\), de donde
\[
T_n(\theta)-T_n(\tfrac14)\ \approx\ \frac{5}{3c}\,T^{2/5}(\log T)^{1/5}\,\log\frac{1}{4\theta},
\qquad T\asymp T_n(\tfrac14).
\]
El crecimiento del cutoff es **logarítmico en \(1/\theta\)**; el de la reserva es lineal en
\((\tfrac14-\theta)\). Eso es lo que hace la pregunta no trivial, y lo que se resuelve abajo.

---

## Proposición 4 (transporte firmado y balance exacto)

Para \(0<\theta\le\frac14\) defínase el **transporte firmado**
\[
\boxed{\;\Delta_{n,\theta}:=-\int_{T_n(1/4)}^{T_n(\theta)}E(u)K_n(u)\,du
\;=\;R_n\bigl(T_n(\tfrac14)\bigr)-R_n\bigl(T_n(\theta)\bigr).\;}
\tag{3}
\]
(La segunda igualdad es inmediata de \(R_n(T)=-\int_T^\infty EK_n\).)
Entonces el objetivo (2) en \(\theta\) y en \(\frac14\) difieren exactamente en

\[
\Bigl[q_{n,\theta}-\int_a^{T_n(\theta)}EK_n\Bigr]
-\Bigl[q_{n,1/4}-\int_a^{T_n(1/4)}EK_n\Bigr]
=\underbrace{(\tfrac14-\theta)A_n}_{\text{ganancia de reserva}}
+\underbrace{\Delta_{n,\theta}}_{\text{costo del cutoff, con signo}} .
\tag{4}
\]

Llamemos \(\mathcal N_n(\theta):=(\tfrac14-\theta)A_n+\Delta_{n,\theta}\) la **mejora neta**.

**Cotas incondicionales.** Por el Teorema 3, \(|R_n(T_n(\tfrac14))|\le\tfrac14A_n\) y
\(|R_n(T_n(\theta))|\le\theta A_n\), luego \(|\Delta_{n,\theta}|\le(\tfrac14+\theta)A_n\) y
\[
\boxed{\;-2\theta A_n\ \le\ \mathcal N_n(\theta)\ \le\ \tfrac12 A_n .\;}
\tag{5}
\]

**Lectura correcta de (5).**

1. **No hay ganancia gratuita.** El signo de \(\mathcal N_n(\theta)\) **no está determinado** por
   A0: depende del signo del transporte \(\Delta_{n,\theta}\), es decir de la correlación de
   \(E\) con \(K_n\) en la ventana \([T_n(\tfrac14),T_n(\theta)]\). Afirmar "\(\theta\to0\) da un
   \(4/3\) gratis" es **falso**: es una redistribución del contenido RH entre reserva y bloque.
2. **Pero la pérdida es controlable y tiende a cero.** Para todo \(\varepsilon>0\), eligiendo
   \(\theta\le\varepsilon/2\) se tiene \(\mathcal N_n(\theta)\ge-\varepsilon A_n\): bajar
   \(\theta\) **no puede costar más que \(\varepsilon A_n\)**, uniformemente en \(n\).
3. **La ganancia posible es real y acotada:** a lo sumo \(\tfrac12A_n\approx\tfrac14 n\log n\),
   frente a \(q_{n,1/4}\approx\tfrac38n\log n\).
4. **Conclusión operativa: se fija \(\theta=\tfrac14\).** Hacer \(\theta_n\downarrow0\) es
   *admisible* (su costo está acotado por \(2\theta_nA_n=o(A_n)\)) pero **no aporta ningún signo**
   y complica el cutoff: mueve \(T_n\) hacia afuera y agranda la ventana de transporte sin
   comprar nada demostrable. **`104_10` (M1) trabaja con \(\theta=\tfrac14\)**, es decir con la
   normalización heredada de fases 102–103, \(q_{n,1/4}=\tfrac34A_n+1-L_n^{(1)}(\log2)\).
   La familia \(\theta\) queda disponible, no en uso.

**Lo que faltaría para convertir (5) en ganancia.** Un signo para \(\Delta_{n,\theta}\), es
decir \(\int_{T_n(1/4)}^{T_n(\theta)}EK_n\le0\). En esa ventana \(u\ge T_n(\tfrac14)\) el kernel
\(K_n\) está **más allá de todos sus ceros** y tiene signo fijo \((-1)^{n-1}\)
(`103_08` corrección 5; nótese que `103_03` decía "siempre positivo", lo cual es falso), pero
\(E\) no tiene signo unilateral incondicional (Littlewood: \(E=\Omega_\pm(\sqrt x\log\log\log x)\)).
Por tanto **el signo de \(\Delta_{n,\theta}\) es exactamente del tipo de información que A1
necesita** y no puede obtenerse aquí sin circularidad. Se registra como tal y no se persigue.

---

## Diagnóstico VK (no es parte de la demostración)

\[
\mathrm{Cost}_n(\theta):=\int_{T_n(1/4)}^{T_n(\theta)}|E(u)K_n(u)|\,du
\]
se calcula **solo** para ver el orden de magnitud del intercambio con la envolvente VK.

> **Ninguna elección de \(\theta\) puede justificarse citando \(\mathrm{Cost}_n\), y
> \(\mathrm{Cost}_n\) no aparece en ningún enunciado.** Es un diagnóstico, no una optimización
> concluyente: sustituir \(\Delta_{n,\theta}\) por \(\mathrm{Cost}_n(\theta)\) es exactamente
> el paso de valores absolutos prohibido por la regla 2, y reproduce el déficit \(\Theta(n)\)
> de `rmk:pointwise-insufficient`.

---

## Parámetros que **no** son libres

**Índice de Laguerre \(\alpha\).** \(\alpha=2\) está fijado por la identidad exacta de
integración por partes \((L_n^{(1)})'=-L^{(2)}_{n-1}\), que es la que produce la cancelación
\(-n+(n+1)=+1\) del Teorema 2. El kernel \(\alpha=3\) de
`phase-103-direct-a1-closure/tools/raised_kernel.py` es auxiliar (se usa en la estimación por partes de
`103_58`); sustituirlo en la identidad **exige rederivar todos los bordes**, incluido el
análogo de \(L_n^{(1)}(0)=n+1\). No se toca en esta fase.

**Punto base generalizado de Li.** Los \(\lambda_F(n,a)\) de Omar–Mazhouda pueden ser
admisibles, pero:
- deben quedar **fijos** — si \(a=a(n)\), la equivalencia con RH no es automática;
- obligan a reconstruir A0, A1, la fórmula arquimedeana y el criterio completo.
Se registra como opción con costo, no como ajuste. Ver `104_00` §2 para el deslinde con
`1506.01755`.

---

## Verificación

| Ítem | Test |
|---|---|
| Teorema 1 | Evaluar \(C_n^\theta(T)+\theta A_n+R_n(T)-\lambda_n\) contra los certificados racionales de `103_51` para \(n\le149\) y varios \(\theta\); debe anularse dentro del intervalo |
| Teorema 2 | \(q_{n,\theta}\) reconstruido desde \(A_n\) y \(L_n^{(1)}(\log2)\); comparar con \(q_{n,1/4}\) de `103_02` |
| Teorema 3 | \(T_n(\theta)\) generado desde la tripla PNT explícita **declarada**; verificar (B\(_\theta\)) numéricamente en \(u=T_n(\theta)\) y monotonía \(T_n(\theta)\ge T_n(1/4)\) |
| Prop. 4 | Verificar (5) reconstruyendo \(\Delta_{n,\theta}\) por ambas vías de (3) |

Herramienta diagnóstica: `tools/theta_family_check.py`. Usa punto flotante para tabular los
cutoffs; las identidades y la monotonía se prueban en el texto y no dependen de esa tabla.

---

## Resultado del documento, en una línea

La familia \(C_n^\theta\) es exacta para todo \(\theta\), la reserva es
\(q_{n,\theta}=(1-\theta)A_n+1-L_n^{(1)}(\log2)\), y **bajar \(\theta\) no regala nada**: la
mejora neta \(\mathcal N_n(\theta)=(\tfrac14-\theta)A_n+\Delta_{n,\theta}\) tiene signo
indeterminado, acotada incondicionalmente por \(-2\theta A_n\le\mathcal N_n\le\tfrac12A_n\).
**Se fija \(\theta=\tfrac14\)** para el resto de la fase.

## Estado

- **Cerrado algebraicamente:** Teoremas 1–3, Lema 3.1 y Proposición 4.
- **Cerrado efectivamente:** la tripla PNT de Johnston--Yang está publicada y declarada, luego
  \(T_n(\theta)\) es computable.
- **Diagnóstico ejecutado:** `tools/theta_family_check.py`; no sustituye las pruebas exactas.
