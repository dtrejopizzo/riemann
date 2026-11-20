# LINK_012 — Falsificador certificado de la dominación del mapa011

2026-10-19. Constructor único. **PROVED por aritmética de bolas e integrales validadas con colas analíticas:** para el mapa U de LINK011, con exactamente su normalización, la desigualdad `Q_T(F)≥||UF||²` es falsa. Se usa un test explícito de dos modos, no el margen de ZCERT ni ceros. Esto descarta esa dominación particular; D y otros mapas siguen abiertos.

## 0. Corpus y clase que se prueba

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (entradas LINK011 y sus límites, residuos06), grid maestro, crucigrama, LINK011/AUDIT011 y definiciones de Paper47 eq:Aform y thm:A. La igualdad Q_T=||UF||² ya estaba refutada y **no se reintenta**.

**Razón nueva escrita:** se conserva exactamente el mapa Mellin–Gauss011 y su escala, y se prueba ahora la dominación que había quedado abierta. Cambia la pregunta a signo del resto `Q_T−||UF||²`. La prueba empieza por un falsificador; no atribuye al resto el signo de una aproximación en alta frecuencia.

Un diagnóstico exploratorio de dos modos dio una separación de orden 0.25, que motivó la certificación abajo. El diagnóstico no se usa como prueba. No se introduce otro kernel auxiliar.

## 1. Test explícito polar libre

Fijar

`T=4/5`, `ω=π/(2T)`,

`r=3(ω²+1/4)/(9ω²+1/4)`,

`f(x)=cos(3ωx)+r cos(ωx)`, `|x|≤T`,

`F=f/sqrt(N)`, `N=T(1+r²)`.

Extender por cero fuera del intervalo. Las dos frecuencias son ortogonales, f(±T)=0 y la norma es exactamente N.

La integral polar de cos(ωx) es `2ω cosh(T/2)/(ω²+1/4)`; la de cos(3ωx) es `−6ω cosh(T/2)/(9ω²+1/4)`. Por la elección de r,

`∫_(−T)^T F(x)cosh(x/2)dx=0`.

F es par y pertenece a H¹_0([−T,T]); en particular tiene energía gamma finita y está en el portador de forma usado para los modos de Dirichlet de Paper47.

## 2. Cota inferior de la energía U usando un término ya probado

Usar la descomposición exacta de CONSTRUCTOR005 con α=1/4, s=1/2,

`S=−R=κG_s+κv_s v_s*+Π`,

`κ=−2π^(−1/4)Γ(1/4)ζ(1/2)>0`, `v_s(d)=d^(−1/2)−d^(−1)`.

Como los otros dos términos son PSD, para el mapa011 se tiene

`||UF||²≥κ|M(F)|²`, `M(F)=Σ_(d≥2)a_d(F)v_s(d)`.

La serie converge absolutamente por las cotas de LINK011. Sustituyendo a_d y agrupando el producto entero k=dn:

`M(f)=2∫_(−T)^T f(x)e^(x/2)`

` ·[2Σ_(k≥1)b_k exp(−πk²exp(2x))−z_c τ(exp(2x))]dx`,

`b_k=Σ_(d|k,d≥2)[d^(−1/2)−d^(−1)]`,

`z_c=ζ(3/2)−ζ(2)`.

Aquí `Σ_(d≥2)v_s(d)/d=z_c`. Esta identidad evita truncar la doble suma en d,n de modo inconsistente.

### Cola explícita del perfil, sin signos supuestos sobre f

Se cumple `0≤b_k≤k`. Sea `a=πexp(−2T)` y truncar en k≤K=12. Para t≥K, tanto exp(−at²) como t exp(−at²) decrecen. Por comparación con la integral,

`2Σ_(k>K)b_k exp(−ak²)≤exp(−aK²)/a`,

`2Σ_(k>K)exp(−ak²)≤exp(−aK²)/(aK)`.

Como `|f|≤1+r` y exp(x/2)≤exp(T/2), el error absoluto en M(f) está acotado por

`ε_M=4T(1+r)exp(T/2) exp(−aK²)/a ·(1+z_c/K)`.

El código evalúa esta fórmula con bolas y obtiene `ε_M<2.370·10^(−39)`.

## 3. Cota superior de Q_T sin ceros ni resta numérica incontrolada

Se evalúa directamente la definición de Paper47:

`Q_T(F)=gamma(F)−Σ_(n<exp(2T)) [2Λ(n)/√n]c_F(log n)`.

Para T=4/5 los únicos términos de von Mangoldt son n=2,3,4. Se integran sus autocorrelaciones trigonométricas en el intervalo exacto `[−T,T−log n]`.

La transformada de Fourier de f se evalúa como función entera:

`f̂(t)=T[sinc((t−3ω)T)+sinc((t+3ω)T)]`

`      +rT[sinc((t−ω)T)+sinc((t+ω)T)]`.

Se integra gamma en 0≤t≤H=100 con el símbolo exacto

`m(t)=Re ψ(1/4+it/2)−logπ`.

Para validación compleja se usa la extensión meromorfa analítica

`m_c(z)=[ψ(1/4+iz/2)+ψ(1/4−iz/2)]/2−logπ`,

que coincide con m en el eje real. Se integran cien segmentos unitarios mediante acb.integral, con envolturas de bolas, tolerancias 10^(−18) y precisión 128 bits. Sinc evita los falsos polos removibles de la fórmula racional.

### Cola gamma explícita

Para t≥H>6ω, la fórmula racional equivalente da

`|f̂(t)|≤A/t²`, `A=(8/3)ω(r+3)`.

Además, para t≥1,

`m(t)≤2log t+10`.

**Prueba de la última cota:** la representación de Lévy usa

`K(u)=1/[2sinh(u/2)]+1/[2cosh(u/2)]≤1/u+1/2`.

Separar el integral en `(0,1/t)`, `(1/t,1)` y `(1,∞)`, usar respectivamente `1−cos(tu)≤t²u²/2`, ≤2 y ≤2. El primer trozo es ≤1/4+1/(12t); el segundo ≤2logt+1−1/t. En el tercero,

`∫_1^∞K≤4exp(−1/2)/(1−exp(−2))<28/9`,

pues exp(−1/2)<2/3 y exp(−2)<1/7. Dos veces esa cola, más los otros términos constantes, es <10. C₀=ψ(1/4)−logπ<0 se puede omitir para esta cota superior. ∎

Por tanto la parte omitida del gamma de f tiene la cota superior

`ε_Γ=(A²/π)H^(−3)[(2/3)logH+2/9+10/3]`.

No se sustituye esa cola por cero. El certificado obtiene `ε_Γ<0.000649818` antes de normalizar por N.

## 4. Certificado reproducible y desigualdades separadas

Archivos:

- `LINK012_data/certify.py`: certificado principal con python-flint/Arb.
- `LINK012_data/certified.json`: salida completa de bolas.
- `LINK012_data/explore.py`: diagnóstico previo, sin uso probatorio.

El certificado integra funciones analíticas mediante acb.integral; las únicas sumas o integrales infinitas se cubren por las cotas explícitas anteriores. Las constantes Γ y ζ reales se evalúan con aritmética de bolas de Arb, sin información sobre ceros.

Para el test normalizado, las envolturas dan

`Q_T(F) < 0.002351`,

`|M(F)| > 0.1812652378`,

`κ > 7.95393245`,

`||UF||² ≥κ|M(F)|² >0.26134304`.

En consecuencia

`Q_T(F)−||UF||² < −0.25899 <0`.                     (★)

La prueba no necesita conocer toda la matriz de U ni su norma exacta: basta un término PSD de su descomposición. Tampoco presupone el signo de Q_T; sólo usa una cota superior directa.

## 5. Si el portador se formula sobre tests C_c∞

El test f extendido es H¹_0, y el margen (★) es estricto. Puede aproximarse por funciones pares C_c∞((−T,T)) en H¹. Corregir su momento polar con un test par fijo χ de momento no nulo; el coeficiente de corrección tiende a cero.

Q_T es continuo para la convergencia H¹: el símbolo gamma crece sólo como log(2+|t|), y el peine es acotado en L². U es acotado en L² por LINK011. Por ello el resto converge y permanece negativo para aproximantes suficientemente próximos. Así la dominación también falla en ese core suave, no sólo en la realización de modos de Dirichlet.

## 6. Alcance exacto

Se refuta **la desigualdad con el mapa011 y su normalización fija**. No se afirma que toda forma suave positiva sea demasiado grande, ni que ninguna reescala admita dominación, ni que no exista otro mapa del portador a −R. No se obtiene una exclusión general de compresiones o de O1.

Este resultado completa el examen de las dos afirmaciones directas propuestas para este candidato: la igualdad falló en LINK011 y la dominación falla ahora por el test explícito. El kernel positivo −R, su FE y el objetivo D no cambian de estado. No se modificó ningún paper.

**Estado:** falsificador certificado de la dominación011; revisión independiente favorable en AUDIT_012.md. D continúa abierto y activo.


## 7. Verificación independiente del gamma y peine sin cuadratura

Se obtuvo además una fórmula exacta, revisada independientemente,
para I(a)=∫_0^(2T) exp(−au)c_F(u)du del test normalizado:

    I(a)= a/(1+r²)[r²/(a²+ω²)+1/(a²+9ω²)]
          +(1+exp(−2aT))ω²/[T(1+r²)]
             ·[r/(a²+ω²)−3/(a²+9ω²)]².

Para comprobarla, sea v(x)=∫_(-T)^T exp(−a|x−y|)F(y)dy.
Entonces v''−a²v=−2aF, con v'(T)=−av(T), v'(−T)=av(−T).
La solución particular para cada coseno tiene coeficiente2a/(a²+ω_k²).
La corrección homogénea par es Ccosh(ax), donde
C=2ωexp(−aT)/sqrt(T(1+r²))·[r/(a²+ω²)−3/(a²+9ω²)].
Usar I(a)=½∫Fv da la fórmula anterior, incluidos signo y factor2.

Como K(u)=2Σ_(j≥0)exp(−a_j u), a_j=2j+1/2, se obtiene

    gamma(F)=C₀+2Σ_(j≥0)[1/a_j−I(a_j)].

Todos los sumandos del término de Lévy son no negativos. La desigualdad
1−c_F(u)≤u²||F'||²/2 da, para la cola j≥J,

    0≤tail≤2||F'||²[a_J^(−3)+1/(4a_J²)],
    ||F'||²=ω²(r²+9)/(1+r²).

La comparación de la serie decreciente con su integral justifica el último
corchete. `LINK012_data/check_laplace.py` evalúa J=200 con bolas Arb128bits;
el peine se obtiene directamente de G11,G33,G13 de P47 lem:combsine,
con coeficientes (r,−1)/sqrt(1+r²). La salida independiente está en
`LINK012_data/check_laplace.json` y da

    Q_T(F)<0.001647953.

Esta comprobación evita toda cuadratura del gamma y del peine. La cota
inferior de M sigue certificada por la integral analítica y la cola gaussiana
del certificado principal. Las dos cotas superiores deQ son compatibles.
