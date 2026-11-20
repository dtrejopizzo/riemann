# POWER_CONE_001 — Cono elemental de potencias en la forma exterior

Estado: PROVED (identidades y criterios finitos); OPEN (mezclas reales arbitrarias para el dato aritmético). No modifica ningún paper.

## Antecedentes y diferencia declarada

Consultados índice ROUTES-TRIED-INDEX/README.md:393,655; NODE_001.md:195; grid/part3.md:12 y part5.md:7; CROSSWORD-TO-D.md (búsqueda theta/cosh/Pick). La positividad general de núcleos tipo Pick y la insuficiencia de positividad theta ya constan. No se relanza esa ruta. La diferencia es un cálculo cerrado de casos particulares de la forma exterior, con frontera algebraica exacta de dos generadores y contraejemplo racional verificable. No se atribuye novedad al principio general.

## 1. Identidad por integración directa

Sea a>1, rho_a(X)=X^{-a}, X>1. Aunque estas funciones no pertenecen a PW_N, sí son datos de la forma universal exterior con todas las integrales absolutamente convergentes. Su imagen es

    Z rho_a(e^y)=zeta(a) exp(-(a-1/2)y), y>0.

Defina L(a) por la expresión real explícita

    L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

No se necesita ninguna representación espectral. Para h_b(y)=exp(-by)1_{y>0}, b=a-1/2:

* norma cuadrada: 1/(2b);
* autocorrelación: exp(-bu)/(2b), u>=0;
* término arquimediano: [psi(a/2)-log pi]/(2b), por la integral de Poisson de psi;
* peine: zeta'(a)/(b zeta(a));
* polar: 2/[a(a-1)].

La suma es L(a)/b. Por polarización, si rho=Σ c_i X^{-a_i}, a_i>1, d_i=c_i zeta(a_i), entonces

    Q[rho]=Σ_ij d_i d_j [L(a_i)+L(a_j)]/(a_i+a_j-1).

El factor polar cancela exactamente los términos racionales que separan L de psi y zeta'/zeta. Esta fórmula fija la normalización.

## 2. Caso positivo probado

L(a)>0 para a>1: la función completada real tiene representación H(u)=C∫_0^∞ Phi(t)cosh(ut)dt con u=a-1/2 y Phi(t)>0. La positividad del núcleo se ve en cada sumando (2 pi n² exp(2t)-3)>0 para t>=0; por diferenciación H'(u)>0 y L(a)=H'(u)/H(u)>0. Esta demostración utiliza solamente la integral theta y su derivación por Poisson.

En consecuencia Q[rho]>0 para toda combinación no nula c_i>=0. También vale si todos los c_i<=0. El resultado no pasa a combinaciones de signos arbitrarios por polarización.

## 3. Dos generadores: criterio exacto

Ponga u=a-1/2, v=b-1/2, u>=v>1/2. El determinante del núcleo de dos puntos es no negativo exactamente cuando

    (u+v)^2 L(a)L(b)>=uv(L(a)+L(b))²,

o, equivalentemente,

    v/u <= L(a)/L(b) <= u/v.

Para todos los pares de un intervalo esto equivale a

    |u d/du log L(u+1/2)|<=1.

Prueba: tomar logaritmos del criterio de cocientes, dividir por log u-log v y pasar al límite; en sentido inverso integrar la desigualdad diferencial. La positividad de H y su logconvexidad sólo prueban L>0 y L'>=0; no prueban la cota superior u L'<=L.

## 4. Falso lema theta genérica: contraejemplo exacto

Contraejemplo comunicado por el constructor principal: H(u)=3+cosh u, L(u)=H'(u)/H(u). H es par, positiva, transformada bilateral de una medida positiva; L>0 y L'>0 para u>0. Para x=log2, y=2log2,

    L(x)=3/17, L(y)=15/41, L(y)/L(x)=85/41>2=y/x.

Así [ (L(u_i)+L(u_j))/(u_i+u_j) ] tiene determinante negativo. No basta una representación cosh positiva para controlar ni siquiera dos generadores. No es contraejemplo al dato aritmético del paper.

## 5. Avance positivo: todo plano de potencias con exponentes >=32 (PROVED)

Para a>=32, u=a-1/2, se tiene L(a)-u L'(a)>0. En efecto los términos racionales de esta diferencia son positivos. Las desigualdades elementales ψ(t)>=log t-1/t y ψ'(t)<=1/t+1/t² dan

    L-uL' >= (1/2)log(a/(2pi))-1/2-2/a-S(a),
    S(a)=Σ_{n>=2}Lambda(n)n^{-a}(1+u log n).

La primera desigualdad para ψ se obtiene de su integral (o Euler--Maclaurin con resto de signo); la segunda de ψ'(t)=Σ_{k>=0}(t+k)^{-2} y comparación integral. Como Lambda(n)<=log n<=n y u<a,

    S(a)<=2^{-(a-1)}(1+2/(a-2))
           +a 2^{-(a-2)}(1+2/(a-3))<1/100.

Se usó Σ_{n>=2}n^{-p}<=2^{-p}(1+2/(p-1)). Ambas cotas de la última línea decrecen para a>=32, y en a=32 su suma es menor que 1/100 por aritmética racional. Por pi<4 y log2>2/3,

    (1/2)log(a/(2pi))-1/2-2/a
       >= log2-9/16 > 5/48 >1/10.

Así L-uL'>0 sin evaluación numérica de funciones especiales. La representación cosh positiva demuestra además L'>=0: log H es convexa, por Cauchy--Schwarz para su medida bilateral positiva. Por tanto, para a>=b>=32,

    1<=L(a)/L(b)<=(a-1/2)/(b-1/2).

El criterio de §3 prueba Q[c X^{-a}+d X^{-b}]>=0 para cualesquiera c,d reales y a,b>=32 (estricto para a!=b y dato no nulo). Es positividad sobre una unión de planos, no sobre su suma: no se afirma positividad de matrices de orden tres. Es además un caso exterior ajeno a PW_N; falta un puente a las colas admisibles del paper.

## 6. Residuo constructivo preciso

El siguiente objetivo local es extender la desigualdad de §5 hacia 1<a<32, usando la serie convergente de zeta'/zeta y las integrales de psi. Su composición sobre tres generadores requiere además el determinante de orden tres; los menores de orden dos no bastan. No se ha obtenido signo sobre PW_N/gauge.

## 7. Revisión independiente y detalle theta

La normalización, el criterio de dos puntos y la estimación a>=32 fueron revisados de forma independiente. Puede tomarse, salvo constante positiva, Phi(t)=Σ pi n² exp(5t/2)(2pi n² exp(2t)-3) exp(-pi n² exp(2t)), t>=0. Cada sumando es positivo; el decaimiento doblemente exponencial justifica todas las derivadas bajo la integral cosh en compactos de u. La medida bilateral no está concentrada en un punto, de donde (log H)''>0.

Para el falsificador, (42,-41)K(42,-41)^t=-129/(34 log2) exactamente.
