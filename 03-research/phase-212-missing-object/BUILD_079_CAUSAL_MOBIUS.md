# Construcción 079 — Corrector causal de Möbius con reparación de momentos

Estado: fórmulas (1)–(5), dominios y fallo de V1 revisados independientemente. Positividad de V2 pendiente. No se afirma signo global ni novedad de los ingredientes. Se desarrolla bajo la autorización de construir candidatos incompletos y revisarlos después.

## Datos y operador escrito

Se trabaja primero con F suave, compacto en I=(-T,T), con ambos momentos nulos. Las funciones se extienden por cero. Sea U_l F(t)=1_I(t)F(t-l), l>0. Como I es un intervalo, U_l U_r=U_(l+r). Si l≥2T, U_l=0.

Definir, con sumas finitas n<exp(2T),

    E=Σ_{n≥2} Λ(n)/(sqrt(n) log n) U_log n,
    L=Σ_{n≥2} Λ(n)/sqrt(n) U_log n,
    R=exp(-E)=Σ_{n≥1} μ(n)/sqrt(n) U_log n.

La exponencial es un polinomio finito: E^k=0 si k log 2≥2T. La igualdad con Möbius se verifica en cada coeficiente mediante el producto formal de Euler; no requiere convergencia de una serie infinita. Es una fórmula propia, no una inversión de la forma objetivo. Para pesos genéricos w se define E_w y exp(-E_w), pero sus coeficientes no son μ(n).

Antecedentes de los ingredientes: 212-58 (inversa aritmética en celdas), R170_856 (extracción causal de Möbius), 212-73 (términos de rango finito), 212-77 (Gram continuo no HS). El propósito aquí es calcular una realización concreta con corrección exacta de momentos, no atribuir signo a la inversa de Möbius.

## Reparación exacta de los dos momentos

Sean e_σ(t)=exp(σt/2) en I, σ=±1, y ℓ_σ(f)=∫_I e_σ(t)f(t)dt. La matriz H de momentos es

    H = [[2 sinh T, 2T], [2T, 2 sinh T]].

Es invertible para T>0. Escribir Qf=f−Σ_σ e_σ (H^(-1)ℓ(f))_σ. Q es la proyección ortogonal sobre P_T (también para funciones complejas, con la convención usual de conjugación). Sea Y=Q(R−I)F; entonces QRF=F+Y.

Los momentos de cada desplazamiento son explícitos. Con l=log n<2T,

    ℓ_σ(U_l F)=exp(σl/2)∫_{-T}^{T-l}exp(σs/2)F(s)ds
              =−exp(σl/2)∫_{T-l}^T exp(σs/2)F(s)ds.

La segunda igualdad usa ℓ_σ(F)=0. Así, toda reparación se determina por integrales de borde escritas, no por un autovector o minimización.

## Primer cuadrado y su residuo

Poner β=1−C0>0, donde C0=ψ(1/4)−log π. Definir el operador explícito de incrementos

    Jf = ( f, (u,t)↦sqrt(K(u)/2)[f(t)−f(t-u)] )

con valores en L²(R)⊕L²((0,∞)×R). Su norma es

    b(f)=||Jf||²=Arch(f)+β||f||².

La integral se conserva como cuadrado conjunto. No se separa su diagonal divergente. Denotar también por b(f,g)=<Jf,Jg> su polarización.

El candidato inicial es V^(0)F=JQRF=J(F+Y). Su residuo exacto es

    a_T(F)−||V^(0)F||²
      =−β||F||²−2 Re<F,LF>−2 Re b(F,Y)−b(Y).             (1)

Todos los términos son finitos para el núcleo suave: R produce una suma finita de funciones suaves a trozos con soporte compacto; la reparación añade exponenciales cortadas. Son BV compactas, por tanto pertenecen a H^s para s<1/2 y al dominio logarítmico de J.

## Primera corrección motivada por un fallo exacto

Si 2T≤log 2, E=L=0 y R=I. Entonces Y=0 y el residuo (1) es −β||F||²<0 para F≠0. El candidato inicial NO puede ser una pieza positiva dominada por a_T, ni siquiera en la ventana sin primos. Este fallo es exacto, no numérico.

Para eliminar esa sobrecarga se quita el canal identidad del corrector y se define

    V^(1)F=JQ(R−I)F=JY.

Ahora el cuadrado se anula exactamente cuando no hay contactos. Es no lineal en los pesos a través de exp(-E), y usa las dos restricciones mediante los bordes de Q. Su residuo queda escrito como

    ρ^(1)(F)=Arch(F)−2 Re<F,LF>−b(Y).                    (2)

No se afirma ρ^(1)≥0. La modificación repara el fallo de la ventana sin contactos, pero todavía no proporciona el mecanismo aritmético que firme (2).

## Ecuaciones explícitas del residuo, sin abreviatura espectral

Para n≥2 con μ(n)≠0, poner d_n=μ(n)/sqrt(n),

    Z_nF=U_log n F−Σ_σ e_σ (H^(-1)ℓ(U_log n F))_σ.

Entonces Y=Σ_n d_n Z_nF y

    ρ^(1)(F)=Arch(F)−2Σ_n Λ(n)/sqrt(n) Re<F,U_log n F>
             −Σ_{m,n≥2} μ(m)μ(n)/sqrt(mn) b(Z_mF,Z_nF). (3)

La última suma conserva los cruces m≠n; no se los descarta. El problema de diseño siguiente es encontrar una cancelación firmada entre esos cruces, los contactos y Arch. Reemplazar esa obligación por «ρ^(1) es positivo» no constituye una prueba.

## Controles y límites de lo obtenido

La identidad (1) existe también para pesos reescalados y para un sistema de retardos Beurling, sustituyendo E y L. La identificación exacta de R con μ sobre enteros sólo corresponde al peso verdadero; ello NO demuestra el signo del residuo. No hay todavía una línea de signo que distinga todos los falsificadores.

Resultado: dos fórmulas explícitas de candidato, residuo completo calculado, primer fallo localizado y una modificación que elimina ese fallo. Positividad del segundo residuo: OPEN. No se ha obtenido una prueba de a_T≥0.

## Segunda corrección: limitar la ganancia del corrector

Estado de esta sección: álgebra e integrabilidad revisadas independientemente; sin signo global.

La corrección V1 conserva demasiada energía en paquetes de alta frecuencia con traslaciones disjuntas. Su ganancia cuadrática allí es Σ_{2≤n<exp(2T)}μ(n)²/n, que ya supera 1 cuando entran 2,3,5. La reparación de momentos no afecta esos paquetes si cada traslado conserva íntegro su soporte y sus momentos nulos.

Se modifica la amplitud mediante una fórmula independiente de a_T:

    S_T=Σ_{2≤n<exp(2T)}|μ(n)|/sqrt(n),
    α_T=1/[2(1+S_T)],
    W_T=α_T Q(R−I)Q,
    V^(2)F=J W_T F.

Aquí Q se extiende a L²(R) como la proyección sobre P_T de las restricciones a I, seguida de extensión por cero. Así ||W_T||≤S_T/[2(1+S_T)]<1/2. No se normaliza usando un autovalor de a_T ni su inversa. Si no hay contactos, W_T=0.

Definir D_u=I−τ_u sobre la recta y C_u=D_uW_T−W_TD_u. Para F primitivo del núcleo suave,

    D_u W_T F=W_TD_uF+C_uF.

Por expansión de este cuadrado,

    a_T(F)=||V^(2)F||²+P_T^new(F)−B_T^new(F),             (4)

con

    P_T^new(F)=<F,(I−W_T*W_T)F>
       +(1/2)∫_0∞K(u)<D_uF,(I−W_T*W_T)D_uF>du,

    B_T^new(F)=β||F||²+2 Re<F,LF>
       +(1/2)∫_0∞K(u)[2 Re<W_TD_uF,C_uF>+||C_uF||²]du. (5)

Se tiene P_T^new(F)≥(3/4)b(F). Esto NO prueba P_T^new≥B_T^new: β y los contactos siguen presentes, y el término mixto del conmutador no tiene signo conocido. No se sustituye por valor absoluto.

La identidad (4) conserva explícitamente el defecto de conmutación con la ventana y con las restricciones. Ése es el término a modificar en el siguiente diseño. C_u no es un símbolo de la forma original ni un residuo definido por su autovalor: es el conmutador de operadores ya escritos.

En el núcleo considerado todas las integrales de (5) existen: W_TF es BV compacto y está en el dominio de J, W_T es acotado, y C_uF=D_uW_TF−W_TD_uF tiene norma cuadrada integrable con peso K. El término mixto es integrable por Cauchy–Schwarz en (u,t); aquí se usa sólo para justificar existencia, no para estimar el signo.

El factor α_T elimina el fallo de ganancia de los paquetes disjuntos, pues α_T²Σμ(n)²/n≤α_T²S_T²<1/4. No se afirma que elimine otros testigos negativos del residuo. La parte aritmética de W_T sigue siendo causal y no lineal en los pesos antes de especializar a Λ.


## Localización del conmutador y cambio del orden de operaciones

Cálculo nuevo pendiente de revisión. Poner χ=1_I y Π=χ−Q, la proyección de rango dos sobre las exponenciales cortadas. Como Qχ=χQ=Q,

    W=α Σ_{n≥2} d_n Q τ_log n Q,
    A_u=[D_u,Q]=Qτ_u−τ_uQ,
    C_u=α Σ_n d_n(A_u τ_log n Q+Q τ_log n A_u).           (6)

Aquí d_n=μ(n)/sqrt(n), con el mismo corte finito. Las traslaciones de la recta conmutan; por ello todo C_u proviene de Q, no de un conmutador entre retardos aritméticos. Más explícitamente,

    A_u=M_(χ−χ(·−u)) τ_u−Πτ_u+τ_uΠ.                     (7)

El primer término está soportado en franjas de los extremos; los otros dos tienen rango finito. No se atribuye signo a ninguna de estas piezas.

En lugar de JWF, se define ahora el candidato con el orden invertido en cada canal:

    V^(3)F=(WF, (u,t)↦sqrt(K(u)/2)(W D_uF)(t)).          (8)

Es una fórmula explícita en los mismos datos. No exige que D_uF pertenezca a P_T: Q dentro de W realiza esa corrección. Se tiene

    ||V^(3)F||²=||WF||²+(1/2)∫K(u)||W D_uF||²du≤b(F)/4.

Poner Z=(I−W*W)^(1/2), raíz de un operador acotado positivo independiente de la forma objetivo. Si se quiere evitar la notación de raíz, todos los términos siguientes se leen como <g,(I−W*W)g>.

    a_T(F)=||V^(3)F||²+||ZF||²
       +(1/2)∫K(u)||Z D_uF||²du
       −β||F||²−2 Re<F,LF>.                             (9)

Esta identidad ya no contiene C_u. Las integrales existen por acotación de W y Z y por F∈Dom(J). La modificación elimina el conmutador exactamente, pero deja por controlar el coste β||F||²+2 Re<F,LF> frente a los canales de Z. No se afirma que ese coste esté dominado.

Relación con V2: la diferencia entre los cuadrados de V2 y V3 es exactamente la integral del término mixto y del cuadrado de C_u en (5). No tiene signo predeterminado; V3 no se declara menor que V2.

Advertencia de diseño: (9) es una descomposición exacta de la energía positiva b mediante una contracción. La contracción sola sigue siendo válida para los falsificadores. La prueba global requeriría una cancelación adicional entre el coste y los canales Z que aproveche los coeficientes verdaderos; no está obtenida aquí.

## Diagnóstico numérico: el primer canal de V2 y V3 excede el margen

NUMÉRICO, no certificado. Se reutilizó el vector par inferior de T=0.8 del solver enriquecido, conservado en `build_079_data/vec_T0.8.pkl`. Origen: una carpeta temporal de trabajo anterior. El valor de forma guardado es 5.29432592315062e−12; no se lo recertificó aquí.

El script `build_079_data/check_extraction.py` reconstruye el vector, corrige sus dos momentos en la precisión de trabajo y evalúa el canal WF por cuadratura Gauss separada en todas las fronteras de piezas originales y trasladadas. Órdenes 32,64,96 producen respectivamente

    ||WF||² = 0.008298446283822565,
              0.008298446283822581,
              0.008298446283822570.

La norma reconstruida difiere de 1 en menos de 3e−15; los momentos antes de corregir son menores que 7e−16. Ambas versiones tienen ||V^(j)F||²≥||WF||². Comparado con el valor guardado de a_T, el primer canal ya excede el margen por aproximadamente 1.57e9. Esto es evidencia numérica fuerte contra la dominación del cuadrado, no una prueba con aritmética de intervalos.

Consecuencia de diseño: cambiar el orden de incrementos no basta. El defecto ya existe en el canal WF, común a V2 y V3. No se ajusta α usando el autovalor observado. Hace falta un corrector que se anule estructuralmente sobre las direcciones casi nulas; se investiga un diagnóstico analítico con los tests explícitos del corpus antes de reemplazar su fórmula.

## Descarte analítico de V2 y V3 para ventanas grandes

Estado: demostración revisada, RELATIVA a la siguiente estimación CITED del corpus. No se rederiva mediante objetos externos al sandbox.

Insumo: R160_M4_R1 §4 Teorema B(i), párrafo «Primitive bottom», y ANNEX_MARGIN_CONFLICT §3, proporcionan un test escrito

    X_T=Mχ_T−a_T^corr u_ev∈P_T,
    a_T(X_T)≤C exp(cT) exp(−2π exp(2T)),                 (10)

con χ_T→1 en compactos, 0≤χ_T≤1, y u_ev soportada en (-1/2,1/2). Se usa la cota de ESTE test, no una cota del ínfimo. M es el perfil explícito de BUILD080 (un factor constante de normalización no altera el argumento).

Para t negativo definir

    H(t)=Σ_{n≥2} μ(n)/sqrt(n) M(t−log n).

Las cotas de cola de M y sus derivadas dan, para cada j fijo,

    |M^(j)(t−log n)|/sqrt(n)
      ≤C_j exp(−(17/2+2j)t)n^(8+2j)exp(−π n² exp(−2t)). (11)

En compactos negativos el mayorante es sumable. El término n=2 domina cuando t→−∞: poniendo X=exp(−2t), se obtiene

    H(t)=16π⁴·2⁸ X^(17/4)exp(−4πX)(1+O(1/X)),          (12)

en la normalización de M usada en BUILD080. El resto n≥3 es exponencialmente menor, también después de derivar un número fijo de veces. Por ello (1/4−∂²)H(t)<0 para t suficientemente negativo.

Elegir un intervalo fijo J⊂(-∞,-2) en esa zona y η≥0 suave compacta no nula en J. Entonces g=(1/4−∂²)η es primitivo y

    c_g=<g,H>=<η,(1/4−∂²)H><0.                         (13)

Para T grande, Q_Tg=g y Q_TX_T=X_T. Por la fórmula de W_T,

    <g,W_TX_T>/α_T=<g,(R_T−I)X_T>→c_g.                (14)

La corrección u_ev desaparece exactamente porque, para t∈J y n≥2, t−log n<-1/2. La proyección de salida desaparece al aparear contra g. El límite restante sigue de(11), 0≤χ_T≤1 y convergencia puntual del corte. El corte n<exp(2T) tampoco obstruye la convergencia dominada.

Por Cauchy–Schwarz, para T grande,

    ||W_TX_T||²≥|c_g|² α_T²/(4||g||²).                 (15)

La normalización de BUILD079 satisface S_T≤2exp(T), luego α_T≥exp(−T)/6. Así el primer canal es ≥c1 exp(−2T), incompatible con(10). Ambos candidatos V2 y V3 contienen ese canal, por lo que sus residuos son negativos sobre X_T para T suficientemente grande.

Más generalmente, para mantener la dominación con ESTA misma forma de corrector y una amplitud escalar α_T, (10) y(15) obligarían a

    |α_T|≤C′exp(c′T)exp(−π exp(2T)).                   (16)

No se declara imposible una amplitud de esa escala; se muestra que una normalización meramente exponencial no repara el mecanismo. BUILD080 cambia el operador para anular el perfil, en lugar de ajustar el escalar usando el autovalor.

Esta prueba no refuta a_T≥0. Refuta la dominación de los cuadrados concretos V2 y V3, bajo el insumo(10). El diagnóstico numérico T=0.8 no interviene en la demostración.
