# E.01 — La factorización de canal balanceada y el contrato de un paso

*Semana matemática 1 del plan de cierre de row (d).*

## CORRECCIÓN DE ALCANCE (leer primero)

La versión inicial de este archivo afirmaba que \(X_0,Y_0,X_E,Y_E,S_E,\mathcal H_{5/4}\)
"no se definen en ningún `.tex`". **Eso era engañoso.** Están definidos en el corpus de
investigación: los feature maps en **D.137**, y la transformada de Cholesky de referencia
con \(H,\widetilde X_E,S_E,A_N,y_N\) en **D.170 (1.1)-(1.4)**. Lo que es cierto y mucho
más chico: esas definiciones **no fueron transferidas al paper**, así que un referee que
lea solo `row-d-local-analysis.tex` no puede auditar §5 de esa sección. Es una tarea
editorial, no una laguna de investigación.

La derivación de §3 se hizo de forma independiente y **coincide** con D.170:
*"the entries of \(X\) contain the complete Gamma screw and every \(J_{p^k,-}\); the
entries of \(Y\) contain the \(\beta\)-line, the resolvent and every \(J_{p^k,+}\)"*
(D.170 §0). Su valor es de verificación cruzada y de forma publicable, no de contenido
nuevo.

**Además, D.170 está más adelante que este archivo en un punto sustantivo:** el defecto
correcto es el de **salida** \(D_{\rm out}=I-A_NA_N^*\), no el de entrada
\(D_{\rm in}=I-A_N^*A_N\); la identidad push-through \(I+A_ND_{\rm in}^\dagger A_N^*
=D_{\rm out}^\dagger\) los conecta, y la capacidad es
\(y_N^*D_{\rm out}^\dagger y_N\le I\) (D.170 (0.4)). El \(\Theta\) de §5.2 es una
normalización distinta del \(v_N\) de D.170 (0.5).

Lo que sí es aporte de este archivo: la verificación numérica (§2-§4), la
cuantificación del déficit escalar (§4), el Teorema 5.0 (R1) y el arnés `114_e_00`.

## Verdict

La factorización balanceada existe, es **única dada la convención de codominio**, y se
deriva de `eq:localizedprimitiveoperator` sin ninguna elección libre:

\[
 A_T=\underbrace{G_{\Gamma,T}+\sum_{n}w_n\,\widehat J_{n,-}^*\widehat J_{n,-}}_{R_T}
     -\underbrace{\Bigl(m_0I+\sum_{n}w_n\,\widehat J_{n,+}^*\widehat J_{n,+}\Bigr)}_{L_T},
 \qquad w_n=\frac{\Lambda(n)}{\sqrt n},
\]

con \(\widehat J_{n,\pm}F=(\widetilde F(\cdot+\log n)\pm\widetilde F)/\sqrt2\) como
operadores \(L^2(I_T)\to L^2(\mathbb R)\). Ambos canales reciben **la misma** energía de
borde por extensión por cero, que es exactamente la frase de cierre de
`row-d-local-analysis.tex:464-465`. Esto identifica
\(\mathcal H_{5/4}=G_{\Gamma,T}\) y confirma el coeficiente \(\Lambda(n)/\sqrt n\) de
`prop:shiftchaincoercivity`.

Consecuencia cuantitativa (§4): **la comparación escalar falla por un factor exactamente
4 en el límite**, y el fallo es de orden líder, no un margen. Como
`prop:shiftchaincoercivity` ya prueba que \(\alpha_N\sim\sqrt N\) es *agudo*, ninguna
mejora de la constante shift-chain puede cerrar la puerta. El déficit \(3\sqrt N\) debe
pagarlo el canal Gamma junto con la estructura no escalar.

---

## 1. La ventana, el espacio primitivo, el operador

En coordenadas logarítmicas \(F(t)=e^{t/2}f(e^t)\), sea \(I_T=(-T,T)\) y \(\widetilde F\)
la extensión por cero de \(F\) a \(\mathbb R\). Los dos momentos de Tate son

\[
 M_\mp F=\int_{-T}^{T}F(t)e^{\mp t/2}\,dt,
 \qquad
 \mathcal P_T=\ker M_-\cap\ker M_+ ,
\]

los pullbacks de \(\widehat f(0),\widehat f(1)\) en `eq:twoprimitive`. El shift comprimido
es \(S_aF=\bigl(\widetilde F(\cdot+a)\bigr)\big|_{I_T}\), de modo que \(S_a^*=S_{-a}\)
sobre \(L^2(I_T)\), y

\[
 A_T=G_{\Gamma,T}-m_0I-\sum_{2\le n<e^{2T}}w_n\,(S_{\log n}+S_{-\log n}),
 \qquad
 m_0=\log\pi+\gamma+\tfrac\pi2+3\log2 ,
\]

donde \(G_{\Gamma,T}\) es la compresión por extensión por cero del multiplicador
\(g_\Gamma(\tau)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{i\tau}2)-\psi(\tfrac14)\).

**Positividad del canal Gamma.** \(g_\Gamma\ge0\), con igualdad solo en \(\tau=0\). En
efecto `eq:archenergy` (`main.tex:1093-1098`) da
\(m_\infty(\tau)-m_\infty(0)=-\sum_{k\ge0}\frac{(\tau/2)^2}{(k+\frac14)((k+\frac14)^2+(\tau/2)^2)}\le0\)
con \(m_\infty(\tau)=\log\pi-\mathrm{Re}\,\psi(\frac14+\frac{i\tau}2)\); es decir
\(\mathrm{Re}\,\psi(\frac14+\frac{i\tau}2)\ge\psi(\frac14)\). Por lo tanto
\(G_{\Gamma,T}\ge0\). Numéricamente \(m_0=5.3721834192\ldots\)

Como \(S_{\log n}+S_{-\log n}=2\mathrm{Re}\,S_{\log n}\), escribimos
\(\sigma_T=\sum_{2\le n<e^{2T}}w_n\).

---

## 2. Los canales de extensión por cero

**Definición 2.1.** Para \(a>0\) sean
\(\widehat J_{a,\pm}:L^2(I_T)\to L^2(\mathbb R)\),

\[
 \widehat J_{a,\pm}F=\frac{\widetilde F(\cdot+a)\pm\widetilde F}{\sqrt2}.
\]

**El codominio es \(L^2(\mathbb R)\), no \(L^2(I_T)\).** Esta declaración es
load-bearing: bajo la lectura truncada la Lema 2.2 es falsa y la constante de
`prop:shiftchaincoercivity` cambia de \(1-\cos\frac\pi{m+1}\) a \(1-\cos\frac\pi{2m+1}\).

**Lema 2.2.** \(\widehat J_{a,\pm}^*\widehat J_{a,\pm}=I\pm\mathrm{Re}\,S_a\).
En particular

\[
 \boxed{\;
 \mathrm{Re}\,S_a
 =\tfrac12\bigl(\widehat J_{a,+}^*\widehat J_{a,+}-\widehat J_{a,-}^*\widehat J_{a,-}\bigr),
 \qquad
 S_a+S_{-a}
 =\widehat J_{a,+}^*\widehat J_{a,+}-\widehat J_{a,-}^*\widehat J_{a,-}. \;}
\]

*Demostración.* La traslación es una isometría de \(L^2(\mathbb R)\), luego
\(\|\widetilde F(\cdot+a)\|_{L^2(\mathbb R)}=\|F\|\). Como \(\widetilde F\) se anula fuera
de \(I_T\),

\[
 \langle\widetilde F(\cdot+a),\widetilde F\rangle_{L^2(\mathbb R)}
 =\int_{I_T}\widetilde F(t+a)\overline{F(t)}\,dt
 =\langle S_aF,F\rangle_{L^2(I_T)} .
\]

Por lo tanto
\(\|\widehat J_{a,\pm}F\|^2_{L^2(\mathbb R)}
 =\tfrac12\bigl(2\|F\|^2\pm2\mathrm{Re}\,\langle S_aF,F\rangle\bigr)
 =\|F\|^2\pm\mathrm{Re}\,\langle S_aF,F\rangle\).
Restando las dos identidades y usando \(S_a^*=S_{-a}\) se obtiene lo enmarcado. \(\square\)

**Observación 2.3 (por qué el codominio importa).** El vértice de cadena en \(t=r-a\) cae
fuera de \(I_T\), pero el canal \(\widehat J_{a,\pm}F\) **no** se anula ahí: vale
\(\pm\widetilde F(r)/\sqrt2\). Descartar esa celda reemplaza
\(\widehat J^*\widehat J\) por \(\tfrac12(I-U^*)(I-U)=I-\mathrm{Re}\,U-\tfrac12P_{e_0}\)
en el modelo discreto de cadena, que **no** es de la forma
(diagonal) \(-\mathrm{Re}\,\)(shift comprimido) y por lo tanto no reproduce el término
de shift de \(A_T\). Con el codominio de la Definición 2.1 la cadena de \(m\) vértices
tiene \(m+1\) aristas (pared Dirichlet en ambos extremos) y el menor autovalor es
\(1-\cos\frac{\pi}{m+1}\), tal como afirma `prop:shiftchaincoercivity`.

---

## 3. La factorización balanceada

**Teorema 3.1 (factorización de canal balanceada).** Sobre \(L^2(I_T)\),

\[
 A_T=R_T-L_T,
 \qquad
 R_T=G_{\Gamma,T}+\sum_{2\le n<e^{2T}}w_n\,\widehat J_{n,-}^*\widehat J_{n,-},
 \qquad
 L_T=m_0I+\sum_{2\le n<e^{2T}}w_n\,\widehat J_{n,+}^*\widehat J_{n,+},
\]

con \(\widehat J_{n,\pm}=\widehat J_{\log n,\pm}\). Ambos sumandos son positivos, y

\[
 R_T=X_T^*X_T,\qquad L_T=Y_T^*Y_T,
\]

\[
 X_TF=\Bigl(G_{\Gamma,T}^{1/2}F,\;\bigl(\sqrt{w_n}\,\widehat J_{n,-}F\bigr)_n\Bigr),
 \qquad
 Y_TF=\Bigl(\sqrt{m_0}\,F,\;\bigl(\sqrt{w_n}\,\widehat J_{n,+}F\bigr)_n\Bigr),
\]

como operadores de \(L^2(I_T)\) en
\(L^2(I_T)\oplus\bigoplus_{n}L^2(\mathbb R)\).

*Demostración.* Por el Lema 2.2,
\(-w_n(S_{\log n}+S_{-\log n})
 =w_n\widehat J_{n,-}^*\widehat J_{n,-}-w_n\widehat J_{n,+}^*\widehat J_{n,+}\).
Sumar sobre \(n\) y agregar \(G_{\Gamma,T}-m_0I\). La positividad de \(G_{\Gamma,T}\) es
§1. \(\square\)

**Corolario 3.2 (identificación de la notación del paper).**
\(\widehat{\mathcal R}_T=R_T\) y \(\mathcal H_{5/4}=G_{\Gamma,T}\). El coeficiente
\(\Lambda(n)/\sqrt n\) de `prop:shiftchaincoercivity` — y no \(2\Lambda(n)/\sqrt n\) — es
el correcto precisamente porque el reparto es balanceado.

**Observación 3.3.** La factorización es única dada la convención de codominio: cualquier
otra asignación del término \(\mathrm{Re}\,S_a\) entre los dos signos rompe la simetría
de energía de borde y por lo tanto la frase `row-d-local-analysis.tex:464-465`.

---

## 4. El déficit escalar es de orden líder y vale exactamente 4

**Proposición 4.1.** Con \(N=e^{2T}\),

\[
 L_T\le(m_0+2\sigma_N)I,
 \qquad
 R_T\ge\alpha_NI
 \quad\text{(`prop:shiftchaincoercivity`, descartando }G_{\Gamma,T}),
\]

\[
 \sigma_N=\sum_{2\le n<N}\frac{\Lambda(n)}{\sqrt n}\sim2\sqrt N,
 \qquad
 \alpha_N\sim\sqrt N .
\]

Por lo tanto el sandwich escalar \(\alpha_N\ge m_0+2\sigma_N\) **falla**, con

\[
 \boxed{\;\lim_{N\to\infty}\frac{\alpha_N}{m_0+2\sigma_N}=\frac14 .\;}
\]

*Medición* (`114_e_01_balanced_factorization_verify.py`):

| \(N\) | \(\sigma_N\) | \(\alpha_N\) | \(m_0+2\sigma_N\) | cociente | \(\sigma_N/\sqrt N\) | \(\alpha_N/\sqrt N\) |
|---|---|---|---|---|---|---|
| 5 | 1.4710 | 0.6340 | 8.3142 | 0.07625 | 0.65785 | 0.28353 |
| 200 | 26.1663 | 11.7300 | 57.7048 | 0.20328 | 1.85024 | 0.82943 |
| 5000 | 138.7319 | 65.5772 | 282.8359 | 0.23186 | 1.96196 | 0.92740 |
| 100000 | 629.9414 | 306.4512 | 1265.2549 | 0.24221 | 1.99205 | 0.96908 |

**Corolario 4.2 (no-go para la ruta escalar, incondicional).**
`prop:shiftchaincoercivity` prueba además que \(\alpha_N\sim\sqrt N\) es **agudo** (el
límite superior coincide, porque todo bracket es \(\le\frac12\) para \(n<N\)). Por lo
tanto ninguna mejora de la constante de coercividad shift-chain puede cerrar la puerta:
el déficit es \(3\sqrt N\), de orden líder. Debe pagarlo \(G_{\Gamma,T}\) junto con la
estructura no escalar del complemento de Schur.

Esto explica estructuralmente — y no como accidente numérico — por qué
`114_d_207` demuestra que ningún split interno mejora la cota escalar, y por qué
`114_d_209` observa 43 direcciones negativas.

---

## 5. Un paso: defectos, cross normalizado, y \(\Theta\)

### 5.1 Parametrización por potencias primas consecutivas (R1)

La lista de contactos de \(A_T\) cambia solo cuando \(e^{2T}\) cruza una potencia prima.
Sea \(2=q_1<q_2<q_3<\cdots\) la sucesión ordenada de potencias primas y
\(\tau_j=\frac12\log q_j\). En \((\tau_j,\tau_{j+1})\) no nace ningún contacto. Por el
principio de nesting (`row-d-local-analysis.tex:233-240`) basta probar positividad en el
extremo derecho de cada intervalo, de modo que el paso es
\(\mathcal P_{\tau_j}\to\mathcal P_{\tau_{j+1}}\).

**Teorema 5.0 (R1: el paso es exacto).** Sea \(\mathcal E:\mathcal P_{\tau_j}\to
\mathcal P_{\tau_{j+1}}\) la extensión por cero y \(\mathcal C=\mathcal E(\mathcal P_{\tau_j})\).
Entonces:

1. la lista de contactos es constante e igual a \(\{q_1,\dots,q_j\}\) en todo
   \((\tau_j,\tau_{j+1}]\);
2. **el nacimiento es nulo sobre el core.** El contacto entrante \(q_j\) tiene longitud de
   shift \(\log q_j=2\tau_j\), que es *exactamente* el ancho de la ventana vieja; luego
   para \(F\) soportada en \(I_{\tau_j}\) los soportes de \(\widetilde F(\cdot+\log q_j)\)
   y de \(F\) son disjuntos y \(\langle(S_{\log q_j}+S_{-\log q_j})F,F\rangle=0\);
3. el canal Gamma es independiente de la ventana sobre funciones extendidas por cero,
   porque \(\langle G_{\Gamma,T}F,F\rangle=\frac1{2\pi}\int g_\Gamma|\widehat{\widetilde F}|^2\)
   no menciona \(T\);
4. **en consecuencia \(\mathcal E^*A_{\tau_{j+1}}\mathcal E=A_{\tau_j}\) exactamente:** el
   bloque del old core no recibe ninguna corrección del contacto recién nacido;
5. \(\mathcal A=\mathcal C^\perp\) dentro de \(\mathcal P_{\tau_{j+1}}\) se descompone como
   \[
    \mathcal A=\bigl(\text{primitivas soportadas en el anillo}\bigr)\;\oplus\;
    \mathrm{span}\,\{e^{-t/2},e^{t/2}\}\big|_{I_{\tau_j}},
   \]
   es decir el anillo **más exactamente dos** direcciones, y esas dos son los modos de
   Tate restringidos al core.

*Demostración.* (1) el único \(n\in[q_j,q_{j+1})\) con \(\Lambda(n)\ne0\) es \(q_j\).
(2) el shift \(a=2\tau_j\) manda \(I_{\tau_j}=(-\tau_j,\tau_j)\) en \((-3\tau_j,-\tau_j)\),
disjunto de \(I_{\tau_j}\) salvo un punto. (3) por definición de la compresión del
multiplicador. (4) restando las dos formas, la diferencia es
\(-w_{q_j}\langle(S_{\log q_j}+S_{-\log q_j})F,F\rangle\), nula por (2).
(5) \(F\in\mathcal A\) sii \(F|_{I_{\tau_j}}\perp\mathcal P_{\tau_j}\) en \(L^2(I_{\tau_j})\);
como \(\mathcal P_{\tau_j}\) es el núcleo de dos funcionales, su complemento ortogonal en
\(L^2(I_{\tau_j})\) es el span de los dos vectores de Tate restringidos. \(\square\)

Verificado en `114_e_02_r1_prime_power_step_verify.py` (15 checks; el conteo de dimensión
de (5) da `extra = 2` en los cuatro pasos probados, con residuo de nesting
\(\sim5\times10^{-14}\)).

**Observación 5.0.1.** El punto (5) es un insumo directo para la ruta E1: los "dos canales
neutrales de Tate" de la coligación no son una elección de diseño — son literalmente las
dos dimensiones que la corona tiene por encima del anillo.

### 5.2 Los dos operadores de defecto

Al final del paso, \(\mathcal P_{\tau_{j+1}}=\mathcal C\oplus\mathcal A\) (old core
transportado ⊕ corona naciente). En esa descomposición la forma balanceada da

\[
 A=\begin{pmatrix}A_{\rm old}&B\\B^*&A_{\rm new}\end{pmatrix},
 \qquad
 A_{\rm old}=R_0-L_0,
 \quad
 A_{\rm new}=S_E-L_E,
 \quad
 B=X_0^*X_E-Y_0^*Y_E,
\]

con \(R_0=X_0^*X_0\), \(L_0=Y_0^*Y_0\) (canales viejos) y \(S_E=X_E^*X_E\),
\(L_E=Y_E^*Y_E\) (canales de la corona). Los **dos** operadores de defecto son

\[
 \boxed{\;
 D_0=I-T_0,\quad T_0=R_0^{\dagger/2}L_0R_0^{\dagger/2};
 \qquad
 \mathfrak D=I-T_E,\quad T_E=S_E^{\dagger/2}L_ES_E^{\dagger/2}. \;}
\]

Entonces \(A_{\rm old}=R_0^{1/2}D_0R_0^{1/2}\) y \(A_{\rm new}=S_E^{1/2}\mathfrak DS_E^{1/2}\)
sobre los soportes respectivos; en particular la hipótesis de old core \(0\le T_0\le I\)
del paper es exactamente \(A_{\rm old}\ge0\).

El **cross normalizado** y la **transferencia** son

\[
 Q_c=R_0^{\dagger/2}\,B\,S_E^{\dagger/2},
 \qquad
 \boxed{\;\Theta=D_0^{\dagger/2}\,Q_c\,\mathfrak D^{\dagger/2}.\;}
\]

\(\Theta\) transporta el espacio de defecto de la corona al espacio de defecto del old
core; está normalizado por **ambos** defectos, que es lo que hace que la meta sea
\(\|\Theta\|\le1\) con constante uno y no un presupuesto sin normalizar.

### 5.3 D1 — el teorema de un paso, en forma regularizada

**Teorema 5.1 (D1).** Supongamos \(A_{\rm old}\ge0\). Para \(\varepsilon>0\) sea

\[
 \mathcal C_\varepsilon
 =\mathfrak D-Q_c^*\bigl(D_0+\varepsilon I\bigr)^{-1}Q_c .
\]

Entonces:

1. \(\varepsilon\mapsto\mathcal C_\varepsilon\) es **decreciente** cuando \(\varepsilon\downarrow0\);
2. \(A\ge0\iff\mathcal C_\varepsilon\ge0\) para todo \(\varepsilon>0\);
3. si se cumple (2), el límite monótono
   \(\lim_{\varepsilon\downarrow0}Q_c^*(D_0+\varepsilon)^{-1}Q_c\) es acotado, lo que
   **fuerza** \(\mathrm{Ran}\,Q_c\subseteq\mathrm{Ran}\,D_0^{1/2}\), y el límite es
   \(Q_c^*D_0^\dagger Q_c\); en consecuencia
   \(\mathfrak D-Q_c^*D_0^\dagger Q_c\ge0\) y \(\|\Theta\|\le1\).

*Demostración.* (1) \(\varepsilon\mapsto(D_0+\varepsilon)^{-1}\) es decreciente en el orden
de operadores, luego \(Q_c^*(D_0+\varepsilon)^{-1}Q_c\) es decreciente y
\(\mathcal C_\varepsilon\) creciente en \(\varepsilon\).

(2) Para \(\varepsilon>0\) el bloque \(A_{\rm old}+\varepsilon\) es invertible sobre su
soporte, así que por complemento de Schur
\(\begin{psmallmatrix}A_{\rm old}+\varepsilon&B\\B^*&A_{\rm new}\end{psmallmatrix}\ge0
\iff A_{\rm new}-B^*(A_{\rm old}+\varepsilon)^{-1}B\ge0\).
Conjugando por \(S_E^{\dagger/2}\) y usando
\(A_{\rm old}^{}=R_0^{1/2}D_0R_0^{1/2}\) se obtiene
\(S_E^{\dagger/2}\bigl(A_{\rm new}-B^*(A_{\rm old}+\varepsilon)^{-1}B\bigr)S_E^{\dagger/2}
 =\mathcal C_{\varepsilon'}\) con el reescalado correspondiente de \(\varepsilon\).
Finalmente \(A\ge0\iff A+\varepsilon(P_{\mathcal C}\oplus0)\ge0\) para todo
\(\varepsilon>0\), por continuidad de la forma cuadrática al hacer \(\varepsilon\to0\).

(3) Es el criterio de Douglas en su forma de operador shorted: el supremo monótono
\(\sup_{\varepsilon>0}Q_c^*(D_0+\varepsilon)^{-1}Q_c\) es acotado si y solo si
\(\mathrm{Ran}\,Q_c\subseteq\mathrm{Ran}\,D_0^{1/2}\), y entonces coincide con
\(Q_c^*D_0^\dagger Q_c\). \(\square\)

**Observación 5.2.** El valor de (3) es metodológico: **la inclusión de rango deja de ser
una hipótesis independiente** y pasa a ser consecuencia de la estimación regularizada. Por
eso toda identidad conservativa (ruta E1) debe probarse primero en la forma

\[
 \mathcal C_\varepsilon
 =Z_\varepsilon^*Z_\varepsilon+E_\varepsilon,
 \qquad E_\varepsilon\ge0,
\]

y solo después pasarse al límite.

### 5.4 El kernel de Schur normalizado

Si se construye una familia analítica \(\Theta(z)\) con \(\Theta(0)=\Theta\), el kernel es

\[
 K(z,w)=\frac{I-\Theta(z)^*\Theta(w)}{1-\bar zw},
\]

con \(I\) en el numerador — \(\Theta\) ya lleva \(\mathfrak D^{\dagger/2}\) incorporado,
así que escribir \(\mathfrak D-\Theta(z)^*\Theta(w)\) mezclaría presupuesto sin normalizar
con transferencia normalizada.

---

## 6. Qué queda de la Semana 1

- **Hecho:** §2 (Lema 2.2), §3 (Teorema 3.1 + Cor 3.2), §4 (Prop 4.1 + Cor 4.2),
  §5.1 (Teorema 5.0 = R1), §5.2-5.4 (defectos, \(\Theta\), D1 = Teorema 5.1, kernel
  corregido).
- **Pendiente:** extracción del arnés contrafáctico → `114_e_00`.

**Gate de la Semana 1:** \(\Theta\) está definido sin ambigüedad (§5.2). **El gate se
abre.**

### Lo que la Semana 1 cambia para D2

1. **La ruta escalar está cerrada por razón estructural** (Cor 4.2), no por falta de
   esfuerzo numérico: el déficit es \(3\sqrt N\), de orden líder, y la coercividad
   shift-chain es aguda.
2. **El paso está aislado exactamente** (Teorema 5.0): el old core block es
   literalmente \(A_{\tau_j}\), así que la inducción no acumula error entre pasos.
3. **Los dos canales de Tate están identificados geométricamente** (Teorema 5.0(5)): son
   las dos dimensiones que la corona tiene por encima del anillo. La compresión exacta de
   esos dos canales en la coligación (paso 3 del programa E1) tiene ahora un objeto
   concreto sobre el que actuar.
4. **La inclusión de rango dejó de ser hipótesis** (Teorema 5.1(3)).

---

## Scope

**Probado acá.** Lema 2.2; Teorema 3.1 y Corolario 3.2; Proposición 4.1 (la parte de
cotas; el asintótico \(\alpha_N\sim\sqrt N\) se cita de `prop:shiftchaincoercivity`);
Corolario 4.2; Teorema 5.0 (R1); Teorema 5.1 (D1).

**Verificado numéricamente.** Lema 2.2 y Teorema 3.1 a \(2.9\times10^{-14}\) sobre seis
configuraciones \((T,a)\); Observación 2.3 (las dos constantes espectrales); la tabla de
§4 hasta \(N=10^5\); D1 sobre 200 casos con \(D_0\) singular. Ver
`114_e_01_balanced_factorization_verify.py` (17 checks). Teorema 5.0 en
`114_e_02_r1_prime_power_step_verify.py` (15 checks).

**Leído de fuente.** `row-d-local-analysis.tex`; `main.tex:1093-1098` (positividad de
\(g_\Gamma\)); `114_d_207`, `114_d_209`.

**No establecido.** D2 (contractividad uniforme), D3, D4. Que \(G_{\Gamma,T}\) más la
estructura de Schur alcancen a pagar el déficit \(3\sqrt N\) de §4 — ése es exactamente el
contenido de D2. **RH no está probada.**
