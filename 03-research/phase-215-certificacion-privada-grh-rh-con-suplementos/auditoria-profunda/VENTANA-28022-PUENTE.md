# Puente analítico del certificado 2.8022

Reconstrucción independiente del agente principal. Fuente: ROUND_172_A, ROUND_173_A, ROUND_175_A, ROUND_178_A, ROUND_179_A, ROUND_190_A, ROUND_192_A, primeros párrafos de ROUND_193_A y ROUND_195_A, líneas 3897–3903 y 5167. No se usan papers 47–48. El verificador y su reproducción están en VENTANA-28022.md.

## Identidad de formas que permite usar el filtro

Para un cero ρ=β+iγ se pone δ=|β−1/2|. La simetría de los ceros convierte la distribución espectral en la suma, con multiplicidades, de exp(iγt)cosh(δt). Elegir χ igual a uno en |t|≤6.5 y soportado en |t|≤9.5. Se obtiene una medida temperada firmada

`μ=Σρ δ_γ + C(τ)dτ`,

cuyo término por cero en C es la transformada de χ(t)(cosh(δt)−1)exp(iγt), con factor 1/(2π). Las correcciones de ceros con |γ|≤G=3·10¹² son cero por Z2. Las estimaciones inferiores justifican convergencia local y la identidad distribucional; primero se aplica a funciones suaves de soporte compacto.

Escribir F=f̂, y Q(τ) para el multiplicador real par construido abajo. Sea ĝ=QF, con supp(g)⊂[−U,U], U=2.85. Como 2U<6.5, la misma μ representa W(f) y W(g). Por tanto

`W(f)=W(g)+Σρ (1−Q(γ)²)|F(γ)|²+∫(1−Q(τ)²)C(τ)|F(τ)|²dτ`.

Ésta es la identidad necesaria. No se supone que C sea positiva, ni se reemplaza una integral por una muestra. Al demostrar 0≤Q²≤1 en toda la recta, la suma atómica puede descartarse en una cota inferior.

## Control continuo del operador de primos

El programa enumera todas las potencias primas q<exp(2U), pues exp(2U)<300, con peso Λ(q)/√q para cada traslación positiva y su reflejada. Divide [−U,U] en 2048 celdas. Si log q expresado en unidades de celda tiene parte entera j, una traslación desde la celda i termina en i+j o i+j+1; el máximo de los dos pesos domina todo el intervalo. Fuera del soporte el peso se toma cero. Los pesos construidos son positivos y simétricos, y los coeficientes de las traslaciones se redondean hacia arriba a enteros en escala 10⁸.

La comprobación de todas las filas implica la cota de Schur ‖C_U‖<19.486 para el operador completo de traslaciones. No se interpola un muestreo de cocientes. Así el término arquimediano menos el de primos se domina inferiormente por la integral de q(τ)|ĝ(τ)|²/(2π), donde

`q(τ)=m_arch(τ)−19.486 ≥−26`, y `q(τ)>1/10` cuando `|τ|≥R`.

El segundo enunciado usa la monotonía de m_arch y su cota de digamma en R, verificadas en el programa y paper 46. El término polar de W(g) se trata aparte.

## Filtro, soporte, signos y ganancia

Con v=τ/H y b=13, poner

`u(τ)=1−sinc(v)²[cosh(b√(1−v²))/cosh b]²`.

La serie par de cosh hace esta función entera, independiente de una elección de raíz. Su tipo exponencial es a lo sumo 2(b+1)/H. En la recta 0≤u≤1. Para r=R/H,

`u≤a=r²[1/3+2b/(1+√(1−r²))]` si `|τ|≤R`.

La cota sale de 1−sinc(v)²≤v²/3 y de que log cosh es 1-Lipschitz. En 2r≤|v|≤1, sinc(v) y cosh(b√(1−v²)) son positivas y decrecientes; el chequeo del extremo 2r da u≥7a/2. Para |v|≥1, el segundo factor se convierte en un coseno y 1−u≤sech²(b)/v²; el otro chequeo de borde conserva u≥7a/2.

Sea d=m/2 entero, h(u)=T_d(2u/a−1)/T_d(2/a−1), B=T_d(2/a−1)⁻². Las raíces r_i de h están en (0,a), y h(1)=1. La expansión

`1/h(1−v)=Σ c_j v^j`

tiene c_j≥0 y c_j≤(d/(1−a))^j≤m^j, porque a<1/2. Definir

`Q(τ)=h(u(τ)) Σ_{j=0}^{24} c_j(1−u(τ))^j`, `J=25(2m)^24`.

En a≤u≤1, la truncación de la serie recíproca implica h≤Q≤1. En 0≤u≤a, |h|≤√B y |Q|≤√B J; el chequeo BJ²<1 da 0≤Q²≤1 en toda la recta. Desde |τ|≥2R, la identidad T_d(cosh x)=cosh(dx) da

`Q(τ)²≥h(u(τ))²≥B exp(m arcosh 6)/4`.

El grado de Q en u es d+24; por tanto Q tiene tipo ≤(m+48)(b+1)/H. Paley–Wiener, y la acotación de Q en la recta, dan supp(g)⊂[−T−(m+48)(b+1)/H,T+(m+48)(b+1)/H]⊂[−U,U]. Para f suave, la multiplicación también preserva la suavidad necesaria: Q es transformada de una distribución de soporte compacto y orden finito. No se forman numéricamente sus miles de millones de coeficientes.

## Fuga de energía y término polar

La fuga de energía de f fuera de [−Ω,Ω], Ω=2R, es al menos

`η=[1+(1+TΩ)exp(2TΩ+2)]⁻¹`.

Se comprueba directamente: con d₀=1/T, A=Ω+d₀, J₀(z)=∫_{−d₀}^{d₀}F(z+s)F#(z+s)ds tiene tipo 2T. En la franja |Re θ|<π/2, J₀(A sin θ)exp(−2TA cos θ) es acotada porque Re cos θ≥|Im sin θ|. En sus bordes sin θ es real con módulo ≥1, de modo que |J₀|≤E_out. Tres líneas da J₀(x)≤exp(2TA)E_out en [−A,A]. Integrando, 2d₀E_in≤2Aexp(2TA)E_out, que es la cota escrita. El argumento vale para f complejo.

Reservar la mitad de q en |τ|>G/2 deja al menos 1/20 en el resto positivo. La contribución no reservada se domina por

`B[η exp(m arcosh6)/80−26J²] ‖f‖²`.

La pérdida logarítmica usada en el programa domina −log η. En el polo τ=i/2, u es real no positivo y |u(i/2)|≤(b+2)/(2H²). Además |1−u(i/2)|≤2. Resulta

`|Q(i/2)|² ≤ BJ² exp(m arcosh(1+(b+2)/(H²a)))`.

Ambos momentos polares de f se multiplican por el mismo Q(i/2). Cauchy–Schwarz da 2|A(f)B(f)|≤4exp(T)‖f‖². Por eso `polar_log` del programa domina el coste polar en unidades de B. El chequeo `gain_log > polar_log+10` y `gain_log > 2log J+10` implica que, después de pagar 26J² y ese coste, quedan más de 2B‖f‖²: e¹⁰−27>2 y J≥1. Se conserva todavía la reserva de altas frecuencias.

## Corrección espectral, bajas y altas frecuencias

χ se construye convolucionando 1_[−8,8], dos uniformes de radio 1/4 y N uniformes de radio 1/N. Es uno en [−6.5,6.5], tiene soporte [−9.5,9.5] y regularidad finita suficiente. Para |δ|≤1/2,

`|χ̂(s+iδ)|≤16 exp(9.5/2) min(1,4/|s|)² min(1,N/|s|)^N`.

Cada corrección es la semisuma de dos traslaciones complejas menos la real, dividida por 2π. Como (1+|s|)² min(1,4/|s|)²≤25, el prefactor por cero es menor que 10⁵. Z1 y Z3 dan menos de 100log(3+|j|) ceros por intervalo unitario. Para j≥3 se usa N(j+1)−N(j−1), que contiene [j,j+1) incluso si hay un cero exactamente en j; no se presupone que las ordenadas no sean enteras. La cota holgada 100log(3+j) conserva validez al tomar ese intervalo de longitud dos. Los intervalos pequeños se cubren con Z1 y los negativos por simetría. Agrupando en l≤|τ−γ|<l+1 se necesitan a lo sumo cuatro intervalos. Las sumas de (1+l)⁻² y log(3+l)/(1+l)² son menores que 2 y 2log3+3, respectivamente. Se obtiene con holgura

`|C(τ)|≤10⁹log(3+|τ|)`.

En |τ|≤H, los ceros que corrigen tienen |γ|>G, y |τ−γ|>G−H>2.718N. El mismo argumento añade 2.718⁻ᴺ. El chequeo `low correction` da |C(τ)|<exp(−D−2), D=120110026806.

Para |τ|≥H, escribir v₀=1−u. Entonces 0≤v₀≤sech²(b)(H/|τ|)², y z=m sech²(b)<1. El resto de la serie recíproca da

`0≤1−Q²≤2z²⁵/(1−z)·(H/|τ|)^50`.

Se usa 1−Q²≤2(1−Q), h≤1 y la cota c_j≤m^j. El producto con log(3+|τ|) decrece después de H. Evaluarlo con log(3+G), mayor que log(3+H), lo acota por 1/1000. También 1−Q²<1/2. Como H≥G/2, toda esta región dispone de la reserva: su densidad es al menos (1/2)(1/10)(1/2)/(2π)=1/(80π)>1/1000. Así paga íntegramente la corrección alta. Entre G/2 y H basta la cota baja; no se gasta indebidamente dos veces la reserva.

## Margen final y dominio

El chequeo del denominador asegura B>exp(−D), pues cosh(x)≤exp(x). La corrección baja cuesta menos que 2πexp(−D−2)‖f‖²< B‖f‖². De los más de 2B conservados queda más de B, y en particular más que exp(−D−1). Éste es el exponente 120110026807 del paper.

La desigualdad se demostró primero sobre el núcleo suave. La densidad en norma de forma de paper 46, comprobada en la auditoría analítica, la extiende al dominio completo. La inclusión de soportes extiende el resultado a todo 0<T≤14011/5000. No se deduce positividad para ventanas arbitrarias ni se optimiza el corte fijado.

**Dictamen de esta reconstrucción: (a) para la desigualdad con los inputs Z1–Z3 y los 17 predicados certificados.** El texto de paper 46 por sí solo reporta el certificado y omite el desarrollo; el expediente proporciona ahora el argumento y el programa local público que faltaban en la lectura inicial. La comparación literal del manuscrito debe mantener esa distinción: no había una demostración desarrollada en sus líneas 1915–1930.

## Revisión cruzada

El agente theta leyó independientemente las notas de construcción y este puente: confirmó tipo exponencial, serie recíproca, fuga de energía por la franja, coste polar, reserva de altas frecuencias y factores 2π. Su observación sobre extremos de los intervalos de recuento se incorporó arriba usando N(j+1)−N(j−1). No se detectó otro fallo en esta cadena. El alcance sigue siendo la ventana fijada, con pruebas desarrolladas en los anexos de investigación, no una prueba global de positividad.
