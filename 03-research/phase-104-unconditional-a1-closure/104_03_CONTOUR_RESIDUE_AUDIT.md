# 104_03 — Auditoría del contorno binomial y de los residuos

**Rol:** auditoría de signos y normalización. Este documento no es el frente de Phase 104 y
no contiene una estimación nueva de A1.

**Veredicto.** El contorno pequeño de 103_66 es exacto e incondicional. Los polos triviales
de \(R\) tienen el signo que se esperaba localmente, pero **su suma de residuos desnudos
diverge**. La suma convergente aparece únicamente después de conservar la normalización
canónica de género uno; entonces el bloque trivial es exactamente

\[
 \mathcal T_n^{\rm triv}
 =\sum_{a=3,5,\ldots}{1-(1-1/a)^n\over a}
 =\Delta A_n+{\gamma+\log(4\pi)\over2}-1.
\tag{0}
\]

Por tanto los residuos triviales no reconstruyen \(A_n\) directamente: reconstruyen, tras la
subtracción canónica, su **primera diferencia** salvo el término afín explícito de (0). Una
deformación que sume solo los residuos \((1-1/a)^n/a\) es ilegítima.

---

## 1. El contorno local exacto

Póngase

\[
 Z(t)=t\zeta(1+t),\qquad h(t)=\log Z(t),\qquad
 R(t)=-{Z'(t)\over Z(t)}=-{\zeta'\over\zeta}(1+t)-{1\over t}.
\tag{1}
\]

El polo de \(\zeta(1+t)\) en \(t=0\) se cancela: \(Z\) es entera, \(Z(0)=1\), y \(R\) es
analítica en un disco alrededor del origen. Escribamos

\[
 R(t)=\sum_{j\ge0}r_jt^j,\qquad
 C_n:=\sum_{j=0}^n{n\choose j}r_j.
\tag{2}
\]

### Teorema 1 (contorno binomial)

Si \(0<r<\mathrm{dist}(0,\{t:Z(t)=0\})\), entonces

\[
 \boxed{
 C_n={1\over2\pi i}\int_{|t|=r}
 R(t){(1+t)^n\over t^{n+1}}\,dt.}
\tag{3}
\]

Equivalentemente, con \(t=z/(1-z)\),

\[
 \boxed{
 \sum_{n\ge0}C_nz^n={1\over1-z}R\!\left({z\over1-z}\right).}
\tag{4}
\]

*Demostración.* En (3), el residuo en cero de
\(r_jt^j(1+t)^nt^{-n-1}\) es \({n\choose j}\) para \(0\le j\le n\), y cero
para \(j>n\). La suma es finita. Para (4), se sustituye la serie de Taylor de \(R\) y se usa
\([z^n]z^j(1-z)^{-j-1}={n\choose j}\). No se ha movido el contorno a través de ningún cero.
\(\square\)

No hacen falta ramas de logaritmo para (3): \(R=-Z'/Z\) es meromorfa y monovaluada. Una rama
de \(h=-\int R\) solo debe fijarse si se integra por partes usando la primitiva.

### Corolario 1.1 (relación con los coeficientes de Li)

Si \(P_n=\lambda_n-A_n\) es el bloque primo en la normalización de Phase 103, entonces

\[
 C_n=-\Delta P_n=\Delta A_n-\Delta\lambda_n,
\qquad
 \boxed{\lambda_N=A_N-\sum_{n=0}^{N-1}C_n.}
\tag{5}
\]

*Demostración.* Si \(h(t)=\sum_{k\ge1}p_kt^k\), entonces
\(r_j=-(j+1)p_{j+1}\). La fórmula exacta
\(P_n=\sum_{k=1}^nk{n\choose k}p_k\) de 103_52 da
\(\Delta P_n=\sum_{k=1}^{n+1}k{n\choose k-1}p_k=-C_n\). Telescopar desde
\(\lambda_0=A_0=0\) da la segunda identidad. \(\square\)

Ésta es la razón por la que el contorno de 103_66 controla una primera diferencia y no
\(A_n\) directamente.

---

## 2. Singularidades y signo local

Los polos de \(R\) son los ceros de \(Z\), con multiplicidad y residuo negativo:

* un cero no trivial \(\rho\) de \(\zeta\) produce \(t_\rho=\rho-1\) y
  \(\mathrm{Res}_{t=t_\rho}R=-m_\rho\);
* el cero trivial \(-2k\) produce
  \(t_k=-(2k+1)=-a_k\), \(a_k=3,5,\ldots\), y
  \(\mathrm{Res}_{t=-a_k}R=-1\).

En \(t=-a\),

\[
 {(1+t)^n\over t^{n+1}}
 =-{1\over a}\left(1-{1\over a}\right)^n,
\tag{6}
\]

así que el residuo **del integrando** de (3) es

\[
 +{1\over a}\left(1-{1\over a}\right)^n.
\tag{7}
\]

Si un contorno grande contiene ese polo, el teorema de residuos dice

\[
 C_n=I_{\rm exterior}-\sum_{\text{polos cruzados}}\mathrm{Res}(RK_n).
\tag{8}
\]

Por eso el aporte desnudo de (7) entra en \(C_n\) con signo negativo. Ambos signos —el del
residuo local y el de su traslado a (8)— deben registrarse; confundirlos cambia el resultado.

---

## 3. Por qué la suma desnuda de residuos es falsa

Para \(a=3,5,\ldots\), el término que (8) intentaría sumar es

\[
 -{1\over a}(1-1/a)^n=-{1\over a}+O_n(a^{-2}),
\tag{9}
\]

y por tanto diverge. No existe una «suma de todos los residuos triviales» formada con (9).
El arco exterior y la normalización de Hadamard no pueden descartarse por separado.

La factorización canónica de género uno de \(Z\) asigna al cero \(-a\) el factor

\[
 E_1(-t/a)=(1+t/a)e^{-t/a}.
\tag{10}
\]

Su contribución al logaritmo derivado normalizado es

\[
 -{d\over dt}\log E_1(-t/a)
 ={1\over a}-{1\over a+t}.
\tag{11}
\]

La constante \(1/a\), que es precisamente la exponencial canónica omitida por el residuo
desnudo, aporta \(1/a\) a la transformada binomial. De (11) se obtiene

\[
 \boxed{
 C_n[-a]={1-(1-1/a)^n\over a}>0,\qquad n\ge1.}
\tag{12}
\]

Ahora \(C_n[-a]=O_n(a^{-2})\), de modo que la suma sobre \(a=3,5,\ldots\) converge
absolutamente.

### Teorema 2 (relación exacta con el bloque arquimediano)

Sea \(c=(\gamma+\log(4\pi))/2\). Entonces

\[
 \boxed{
 \sum_{a=3,5,\ldots}{1-(1-1/a)^n\over a}=\Delta A_n+c-1.}
\tag{13}
\]

*Demostración.* La fórmula impar exacta de Phase 103 da

\[
 \Delta A_n=-c+\sum_{a\ \mathrm{impar}}{1-(1-1/a)^n\over a}.
\tag{14}
\]

El sumando \(a=1\) vale \(1\); separarlo prueba (13). \(\square\)

Esto concuerda con 103_60: allí el factor trivial contribuye a \(P_n\)
\(\tau_n(a)=1-(1-1/a)^n-n/a\); como \(C_n=-\Delta P_n\), se recupera (12).

**Conclusión de la auditoría trivial.** La afirmación «los residuos triviales reconstruyen la
suma armónica impar de \(A_n\)» era incorrecta si se entendía literalmente. La afirmación
correcta es (13), y requiere la exponencial canónica.

---

## 4. La recta de Cayley

Sobre \(\Re t=-\tfrac12\),

\[
 |1+t|=|t|,
 \qquad
 \left|{(1+t)^n\over t^{n+1}}\right|={1\over|t|}.
\tag{15}
\]

Es una identidad geométrica **incondicional para toda altura**. Bajo la inversa de
\(t=z/(1-z)\), es la circunferencia \(|z|=1\). Un cero no trivial produce
\(t_\rho=\rho-1\), y está sobre esta recta si y solo si \(\Re\rho=1/2\).

Dos precauciones:

1. Platt–Trudgian permite afirmar que los ceros hasta \(H\) yacen sobre la recta; no hace
   «legítima» la identidad (15), que ya lo era. Esos ceros son polos **sobre** el camino y
   requieren indentaciones o valores principales especificados.
2. Sin RH pueden existir polos a ambos lados. Mover el círculo de (3) hasta la recta no produce
   una estimación libre de ellos. La identidad colectiva complementaria que se importa de
   Lagarias debe usarse con el erratum de signo **y la reparación horizontal
   \(T=2\sqrt n+\varepsilon_n\)** de 104_02:
   \(\lambda_n=A_n+\lambda_n(\sqrt n)+O(\sqrt n\log n)\). No es una consecuencia
   automática de (15), ni una cota inferior para el bloque incompleto.

---

## 5. Arcos, ramas y alcance exacto

El único contorno demostrado aquí es el círculo local de (3). Para una deformación global se
necesitan simultáneamente:

* productos canónicos para que las sumas de polos converjan;
* una prescripción de indentación para los polos sobre el camino;
* cotas de arcos para \(R(t)(1+t)^nt^{-n-1}\);
* si se usa \(h=-\int R\), una rama en cada componente del plano cortado.

La cota \(R(t)=O(\log|t|)\) por sí sola no repara (9): el problema es la separación de una
serie canónica convergente en dos series divergentes. Por ello 104_03 **no rederiva** la
identidad global corregida auditada en 104_02 y no reclama una fórmula de suma sobre ceros
nueva.

---

## 6. Verificador

tools/contour_binomial_check.py hace dos comprobaciones distintas.

1. Extrae \(C_n\) de (4) en complex128, reconstruye \(\lambda_N\) por (5), y lo compara con
   una extracción independiente desde \(\xi'/\xi\). Es un diagnóstico, no un certificado.
2. Con la opción --certified, reconstruye intervalos outward para
   \(\lambda_{20},\lambda_{60},\lambda_{149}\) mediante el mismo motor racional de 103_51 y
   reporta por separado inclusión estricta del valor float64 y compatibilidad a su piso de
   redondeo. Solo el intervalo es certificado; que el FFT caiga fuera por redondeo no refuta
   la identidad y que caiga dentro no certifica el FFT.

Corrida rápida:

    n       lambda(contour)       lambda(xi)       disagreement   radius-stability
    20   8.769276872093   8.769276872093    8.53e-14       0.00e+00
    60  57.133099574875  57.133099574874    2.27e-13       7.11e-15
    149 205.922618629825 205.922618629830   -4.46e-12      -1.47e-11

La estabilidad radial se reporta por separado y no se convierte en certificado. La tabla
trivial del mismo programa
confirma la convergencia a (13), mientras la suma desnuda de (9) sigue derivando
logarítmicamente.

---

## Estado

| afirmación | estado |
|---|---|
| contorno local (3)–(4) | **teorema incondicional** |
| signos de los polos y residuos triviales | **auditados** |
| relación canónica trivial–arquimediana (13) | **teorema incondicional** |
| identidad de módulo de Cayley | **teorema geométrico incondicional** |
| deformación global sin normalización canónica | **no-go: serie (9) divergente** |
| identidad colectiva full/incomplete | se importa con el signo corregido de 104_02; no acota por abajo el bloque incompleto |
| prueba de A1/RH | **no contenida aquí** |
