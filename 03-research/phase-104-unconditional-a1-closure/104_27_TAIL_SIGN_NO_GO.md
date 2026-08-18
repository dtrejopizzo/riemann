# 104_27 — El envelope VK no determina el signo de la cola

**Rol.** Auditar si la mejora A0+ puede reforzarse reemplazando
\(|R_n(T_n)|\) por el signo favorable \(R_n(T_n)\le0\). El resultado es
negativo para los inputs actuales: el mismo envelope
Vinogradov--Korobov admite discrepancias con colas de ambos signos, incluso
si se exige que \(e^u+E(u)\) sea creciente en el rayo final. Por tanto un
teorema de signo para la cola necesitaría estructura aritmética de los pesos
\(\Lambda(m)\), no solo A0, PNT y monotonicidad.

Este documento no afirma que la cola aritmética real tenga ambos signos; es
un no-go lógico para una clase de inputs.

## 1. El signo eventual del kernel

Sea \(x_{*,n}\) el mayor cero de \(L_{n-1}^{(2)}\) y
\(s_n=(-1)^{n-1}\). Para \(u>x_{*,n}\),

\[
 K_n(u)=e^{-u}L_{n-1}^{(2)}(u)
       =s_ne^{-u}|L_{n-1}^{(2)}(u)|.              \tag{1}
\]

Escribamos el envelope PNT como

\[
 W(u)=C_{\rm VK}e^{u-\eta(u)},\qquad
 |E(u)|\le W(u).                                   \tag{2}
\]

Para \(\sigma\in\{-1,1\}\), defínase en el rayo \(u\ge T>x_{*,n}\)

\[
 E_\sigma(u)=\sigma s_nW(u).                      \tag{3}
\]

Ambas funciones satisfacen exactamente el mismo input (2), pero

\[
 \boxed{
 R_{n,\sigma}(T)
 =-\sigma C_{\rm VK}\int_T^\infty
 e^{-\eta(u)}|L_{n-1}^{(2)}(u)|\,du.}             \tag{4}
\]

Así, \(\sigma=-1\) da \(R_{n,\sigma}(T)>0\), mientras
\(\sigma=1\) da \(R_{n,\sigma}(T)<0\), para todo cutoff finito.

## 2. Testigo cuantitativo

La factorización por los ceros reales positivos de Laguerre da

\[
 |L_{n-1}^{(2)}(u)|
 ={1\over(n-1)!}\prod_{j=1}^{n-1}(u-x_{j,n})
 \ge{(T-x_{*,n})^{n-1}\over(n-1)!}
 \quad(T\le u\le T+1).                            \tag{5}
\]

Si \(\eta\) es creciente en ese rayo, (4)--(5) implican

\[
 \boxed{
 |R_{n,\sigma}(T)|
 \ge {C_{\rm VK}e^{-\eta(T+1)}
             (T-x_{*,n})^{n-1}\over(n-1)!}.}      \tag{6}
\]

No se trata, por tanto, de un defecto que desaparezca porque el testigo sea
idénticamente cero.

## 3. Versión suave y monotónica

Para compartir el dato inicial \(E(T)=0\), póngase

\[
 \phi_T(u)=1-e^{-(u-T)},\qquad
 \widetilde E_\sigma(u)=\sigma s_nW(u)\phi_T(u).  \tag{7}
\]

La misma cuenta, restringida a \([T+1,T+2]\), da

\[
 |\widetilde R_{n,\sigma}(T)|
 \ge {C_{\rm VK}(1-e^{-1})e^{-\eta(T+2)}
        (T+1-x_{*,n})^{n-1}\over(n-1)!},          \tag{8}
\]

con signos opuestos para los dos valores de \(\sigma\).

Además, si \(T\) se amplía hasta que

\[
 C_{\rm VK}e^{-\eta(u)}
 \bigl(\phi_T(u)+|\phi_T'(u)-\eta'(u)\phi_T(u)|\bigr)<1
 \qquad(u\ge T),                                  \tag{9}
\]

entonces

\[
 {d\over du}\bigl(e^u+\widetilde E_\sigma(u)\bigr)>0
\]

para ambos signos. Las funciones VK usuales satisfacen (9) en todo rayo
suficientemente lejano, y ampliar un cutoff conserva A0. Por ello añadir
monotonicidad no determina el signo de la cola dentro de esta clase.

## 4. Alcance

El testigo no está soportado en potencias primas ni pretende modelar los
pesos de von Mangoldt. Prueba exactamente lo siguiente:

\[
 \boxed{
 \text{A0/VK + monotonicidad en el rayo final}
 \ \not\Longrightarrow\ R_n(T_n)\le0.}            \tag{10}
\]

Elegir «el primer \(T\) con \(R_n(T)\le0\)» tampoco es una construcción
incondicional: el conjunto puede ser vacío en la clase (3), y verificar que
no lo sea para la discrepancia real ya exige información aritmética nueva.

## Estado

- **Probado:** testigos de ambos signos (4), cotas cuantitativas (6), (8) y
  compatibilidad eventual con monotonicidad.
- **Descartado:** obtener A1 desde el margen cuártico usando solo un signo
  favorable de la cola deducido de A0/VK.
- **Abierto:** cualquier argumento de signo que use de manera esencial el
  soporte en potencias primas y los valores exactos \(\Lambda(m)\).
