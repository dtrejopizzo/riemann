# 104_26 — Ataque cuártico, coercividad faltante y stop-gate de cuadrados

> **Corrección vinculante (`104_56A`).** El slack \(A_n/1001\) de (1) es
> exactamente el costo del suficiente uniforme de `104_23` cuando solo se usa
> el piso \(T\ge1000\); no es necesario para RH ni para una transferencia A1
> con cutoff cofinal adaptado. El stop-gate algebraico de cuadrados de este
> documento permanece válido. Se retira únicamente la afirmación de que toda
> ruta cuártica deba producir ese slack proporcional: \(D_n^{[4]}\ge0\) ya
> prueba RH directamente y \(D_n^{[4]}>0\) permite escoger un cutoff que cierra
> A1.

**Rol.** Explotar que el margen uniforme de 104_23,
\(r_*=2002/501\), está a solo \(2/501\) del exponente entero cuatro. El
cociclo cuártico admite una cuarta diferencia local y una factorización
formal como cuadrado de un cociclo de semipotencias. Este documento prueba
que ninguna de esas dos observaciones produce una suma de cuadrados útil:
la potencia local sigue siendo algebraica, el bloque real cambia de signo y
la parte genuinamente cuadrática desaparece al tomar el límite que extrae
los coeficientes. También identifica exactamente el slack que tendría que
producir un ataque cuártico para recuperar **el suficiente uniforme fijado
en** `104_23`:

\[
 D_n^{[4]}:=4\lambda_n-A_n\ge {A_n\over1001}.      \tag{1}
\]

Este documento no prueba (1), A1 ni RH.

## 1. Cuarta diferencia exacta en una torre

Sea \(Q=p^u\), \(\rho=p^{-1-\varepsilon}\) y
\(d_u=J_u^{*4}\). La función generatriz local es

\[
 \sum_{k\ge0}d_u(p^k)x^k
 =\left({1-x\over1-Qx}\right)^4.
\]

Por tanto

\[
 \boxed{
 d_u(p^k)=\nabla^4\!\left[{k+3\choose3}Q^k\right].}        \tag{2}
\]

Con los operadores \(\mathsf P\), \(\mathsf B=I-\rho E_\ell\) y
\(\mathsf C=\mathsf B\mathsf P\) de 104_20, la sumación discreta da

\[
 \boxed{
 \sum_{k\ge0}d_u(p^k)\rho^k\mathsf P^4f(x+k\ell)
 =
 \sum_{k\ge0}{k+3\choose3}(Q\rho)^k
 \mathsf C^4f(x+k\ell).}                           \tag{3}
\]

Aunque \(\mathsf C^4=(\mathsf C^2)^2\), (3) es composición algebraica, no
\(\mathsf C^*\mathsf C\). No define una norma.

## 2. Dos falsificadores locales exactos

Póngase \(w_k=d_u(p^k)\rho^k\). Un cálculo de los primeros tres
coeficientes de (2) da

\[
 \boxed{
 w_1^2-w_0w_2
 ={\rho^2r\over2}(Q-1)\bigl((r-1)Q-(r+1)\bigr)}
                                                               \tag{4}
\]

para la convolución general \(J_u^{*r}\). En particular, con
\(r=4\), \(p=2\), \(u=1/2\), \(\varepsilon=1\),
\(\rho=1/4\), \(Q=\sqrt2\),

\[
 w_1^2-w_0w_2={11-8\sqrt2\over8}<0,               \tag{5}
\]

pues \(121<128\). La cuarta convolución real no es PF2 ni TP2.

El segundo falsificador conserva la torre completa, los cuatro canales
polares y las tres copias Gamma. En grado uno, sobre un fondo \(m\) coprimo
con \(p\), el bloque es un prefactor positivo multiplicado por

\[
 (1-c)^4
 \bigl(1-\log m-3\bar\eta-\ell\mu_{p,4}\bigr)
 +{4c(1-c)^3\over\varepsilon},                    \tag{6}
\]

donde

\[
 M_{p,4}=\left({1-\rho\over1-Q\rho}\right)^4,\qquad
 \mu_{p,4}={4\rho(Q-1)\over(1-\rho)(1-Q\rho)}.     \tag{7}
\]

El signo cambia exactamente en

\[
 \log m=1-3\bar\eta-\ell\mu_{p,4}
          +{4c\over(1-c)\varepsilon}.             \tag{8}
\]

Para \(\varepsilon\) suficientemente pequeño, \(m=1\) queda del lado
positivo y hay infinitos fondos primos del lado negativo. Por ello tampoco
existe positividad bloque a bloque para la aritmética real.

## 3. El cuadrado desaparece en el límite directo

Sea

\[
 B_u(s)=H_u(s)^2K_u(s)^{3/2},\qquad
 \mathcal S_u^{[4]}(s)=H_u(s)^4K_u(s)^3=B_u(s)^2. \tag{9}
\]

Entonces

\[
 {1-\mathcal S_u^{[4]}\over u}
 ={1-B_u\over u}(1+B_u),                          \tag{10}
\]

mientras que, como \(B_u\to1\),

\[
 {(1-B_u)^2\over u}\longrightarrow0.              \tag{11}
\]

El límite de (10), que extrae \(4\lambda_n-A_n\), es lineal. La parte
genuinamente cuadrática se pierde antes de llegar al coeficiente. La
escritura (9) no es un certificado de suma de cuadrados.

La alternativa de generador positivo falla por el mismo testigo exacto de
104_23. Antes del primer átomo \(\log2\), la primera variación de la
inversa completada es

\[
 f_{4,\varepsilon}(x)
 =-4e^{-\varepsilon x}
 +3{e^{-(3+\varepsilon)x}\over1-e^{-2x}},
\]

y en \(x_0=\frac12\log2\),

\[
 f_{4,\varepsilon}(x_0)
 =e^{-\varepsilon x_0}\left(-4+{3\over\sqrt2}\right)<0.   \tag{12}
\]

## 4. Falsificador off-line dentro del rango objetivo

Sea

\[
 w={1\over2}e^{74\pi i/75},\qquad
 \rho={1\over1-w}.                                  \tag{13}
\]

Entonces \(1/2<\Re\rho<1\) y \(\Im\rho\ne0\). Para el cuarteto simétrico
asociado, con \(a=\log2\) y \(\theta=74\pi/75\), la contribución a
\(4\lambda_n\) es

\[
 16\bigl(1-\cosh(na)\cos(n\theta)\bigr).           \tag{14}
\]

En \(n=150\), \(\cos(n\theta)=\cos(148\pi)=1\), de modo que (14) es
estrictamente negativa. Repetir el cuarteto con multiplicidad derrota
cualquier término arquimediano fijo. Así, una suma de cuadrados que use
solo simetría, ecuación funcional y el cuarto exponente también falsificaría
un divisor off-line.

El testigo aparece ya en \(n=2\): para
\(w=\frac12e^{5\pi i/6}\),

\[
 \lambda_2^{\rm quartet}
 =4-4\cosh(2\log2)\cos(5\pi/3)=-{1\over4}.        \tag{15}
\]

## 5. Relación exacta con el margen casi cuártico

Sea

\[
 r_*={2002\over501},\qquad \delta=4-r_*={2\over501}.
\]

Entonces

\[
 \boxed{
 D_n^{[r_*]}
 =D_n^{[4]}-\delta\lambda_n
 ={1001D_n^{[4]}-A_n\over1002}.}                  \tag{16}
\]

Por tanto

\[
 \boxed{
 D_n^{[r_*]}\ge0
 \quad\Longleftrightarrow\quad
 D_n^{[4]}\ge {A_n\over1001}.}                    \tag{17}
\]

La mera semidefinitud \(D_n^{[4]}\ge0\) no alcanza. En coordenadas de
cociclo,

\[
 \mathcal S_u^{[r_*]}
 =\mathcal S_u^{[4]}
 \left({\xi(s-u)\over\xi(s)}\right)^{-2/501}.      \tag{18}
\]

El corrector fraccionario de (18) resta exactamente el slack de (17) y
reintroduce el gate de ceros y ramas.

## Estado

- **Probado:** cuarta diferencia (2), factorización local (3), testigos
  (5), (8), (12), (14), y equivalencia coerciva (17).
- **Descartado:** cuarta potencia como suma de cuadrados local, PF/TP,
  positividad de generador y mera semidefinitud cuártica.
- **Abierto:** una desigualdad global especial que produzca la coercividad
  cuantitativa \(D_n^{[4]}\ge A_n/1001\), o directamente el margen real de
  104_23.
