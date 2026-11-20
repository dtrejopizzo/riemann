# Todas las dimensiones y ventanas con una suma acotada de tasas recíprocas

Sean tasas reales positivas v_j, contadas con multiplicidad, en cualquier número finito. Supongamos Σ_j 1/v_j≤1/512. Para F(s)=P(s)/∏(s+v_j) estrictamente propia, f su inversa causal, g=f 1_[0,L], vale en toda ventana L>0

    W(g) ≥ (1/4)||g||².

Se conserva el peine completo y el polar. No hay filtro previo en el numerador ni cota al número de polos. Se admiten polos repetidos y coeficientes arbitrarios. Por traslación o reflexión vale el mismo enunciado en la ventana centrada y en la orientación opuesta. 084 permite tasas menores en dimensión ≤13; ambos resultados se complementan.

**Control independiente del orden.** Normalizar ||f||=1. Para σ<min v_j, poner B(s)=∏(s−v_j)/(s+v_j) y G(s)=B(s)conj(F(−conj(s))). Las cancelaciones de denominadores muestran que G es racional estrictamente propia con los mismos polos permitidos, y su norma de Hardy sobre el semiplano derecho es 1 por |B(it)|=1. En la recta Re s=σ usar la contracción de Hardy hacia el interior (Plancherel en la inversa causal de G). Al reflejar se obtiene
    
    ||exp(σt) f||₂ ≤ ∏(v_j+σ)/(v_j−σ).

Tomar σ=128. Entonces cada x_j=σ/v_j≤1/4 y Σx_j≤1/4. Como log((1+x)/(1−x))≤2x/(1−(1/4)²), el producto tiene cuadrado ≤exp(16/15)<3. Este paso permite muchos polos sin que el coste dependa de su cantidad.

**L≥1/64.** Se tiene ||g||²≥1−3 exp(−2σL)≥1−3e^(−4). Por Cauchy, ||g||₁²≤3/(2σ); así la masa de Fourier en |ξ|≤32 es ≤(32/π)3/256=3/(8π). P47 lem:mbounds y monotonía dan m(0)>−6 y m(32)>3/2 (la cota inferior de digamma allí es log(32/(2π))−1/32−1/(2·32²)). Por tanto Arch(g)≥(3/2)||g||²−(15/2)3/(8π). Los dos momentos polares tienen producto en módulo ≤3/√((2σ)²−1) por Cauchy ponderado. Para u≥0, |c_g(u)|≤√3 exp(−σu) por Cauchy en la cola desplazada y ||g||≤1. El coste absoluto del peine es ≤2√3 Σ_{n≥2}(log n)n^(−128.5)<1/1000 (usar log n≤n y comparación integral desde 2). En conjunto W(g)>0.48 en esta normalización y por tanto W(g)>||g||²/4.

**0<L<1/64.** Aquí no hay contactos primos. Independientemente de las tasas, ||g||₁²≤L||g||², y la masa baja es ≤32L||g||²/π. El polar cuesta como máximo 2L exp(L/2)||g||². Luego
    
    W(g)/||g||² ≥ 3/2−(15/2)32L/π−2L exp(L/2)>1/4.

No se necesita un certificado externo de ventanas para este paso.

**Qué clase de formas resulta.** Fijar, por ejemplo, v_j=512·2^j, j=1,2,… . Todas las combinaciones finitas de estas mismas exponenciales pertenecen a un solo espacio lineal de dimensión infinita. La cota se hereda en su cierre en la norma de forma, por continuidad a ventana fija. No se afirma extensión a su cierre en L² por mera continuidad de W. El conjunto de todas las configuraciones admisibles sin fijar una secuencia no es automáticamente un espacio lineal.

**Límite de la estrategia de concentración.** En el caso confluyente v_j=v, la propia clase contiene f(t)=t^(n−1)exp(−vt). Para ese vector normalizado, la ley |f|²dt es gamma de media (2n−1)/(2v) y varianza (2n−1)/(4v²). En particular a v fijo, cuando n→∞ la masa de cualquier intervalo inicial fijo tiende a cero, y ||exp(σt)f||₂=(1−σ/v)^(−(2n−1)/2) para 0<σ<v. Por ello no puede conservarse en esos espacios un presupuesto de localización exponencial uniforme en el orden. Es una obstrucción al argumento empleado; no implica energía negativa del vector. El valor 1/512 es suficiente y no se ha optimizado.

**Cotejo.** POWER_COMMON_TRANSFER_010 ya estima normas ponderadas con bases racionales; POWER_STATE_054/060 ya dan conos en todo orden imponiendo un filtro que depende del orden. La aplicación presente admite todos los numeradores sin ese filtro, controla simultáneamente el truncamiento en cualquier ventana y reemplaza la cota de dimensión por Σ1/v_j. Los criterios de densidad de Müntz no permiten deducir el signo global en una secuencia con suma recíproca finita.
