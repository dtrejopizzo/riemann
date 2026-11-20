# Signo simultáneo en el espacio completo de coeficientes de divisores

Mantener t, θ, A, φ, δ y D de 313. Para cada vector real λ=(λ₁,…,λ_D) formar w_λ(n)=τ(n)(Σ_(d|n,d≤D) λ_d)². Convolucionar con los coeficientes del mismo filtro positivo P^m de 313, tomando K suficientemente grande **una sola vez**, independiente de λ. Denotar por v_λ los pesos resultantes. La forma cuadrática

    Q_x(λ)=∫ φ(u) Σ_(n≤X) v_λ(n) B_t(X/n) du,    X=x(1+δu),

satisface, para todo x suficientemente grande y simultáneamente para todo λ,

    Q_x(λ) ≤ −c_t √x L^(−3/2) D^(−10) ||λ||∞².

En particular la matriz de esta media es definida negativa en dimensión D, incluyendo los índices que tienen factores primos repetidos. Todos los parámetros del filtro se congelan en el centro x de la ventana. La brecha de 310 es una propiedad del vector específico λ_d=μ(d); el enunciado matricial permite todos los vectores.

**Multiplicador exacto.** La serie de w_λ es ζ(s)²h_λ(s), donde al par d,k le corresponde λ_dλ_k veces el producto sobre p^e exactamente divisores de l=mcm(d,k) de los factores p^(−es)[1+e(1−p^(−s))]. Esto se obtiene sumando el factor de τ a partir de exponente e. El soporte del multiplicador queda en l rad(l)≤D⁴. Normalizar ||λ||∞=1. En Re s=1/2 su norma absoluta es ≤D⁶: cada producto de normas locales es ≤∏(1+2e)≤l², y hay D² pares. Al desplazarse v hacia la izquierda cuesta como máximo otro D^(4v).

**Piso válido para todo el espacio.** Para s real entre 1/3 y 1/2 tomar valuaciones independientes con probabilidades de cola q_p(e)=p^(−es)[1+e(1−p^(−s))], q_p(0)=1. Son las colas de la distribución de masa (j+1)(1−p^(−s))²p^(−js) en j. Sea I_e el indicador de que la valuación en p es al menos e. Escribir Z₀=1 y Z_e=I_e−r_e I_(e−1) con r_e=q_p(e)/q_p(e−1) para e>0. Para un mismo p son ortogonales por anidamiento de los eventos, con norma cuadrada q_p(e)(1−r_e). Por independencia, los productos Z_d sobre los primos y exponentes de d son también ortogonales. Si q(d)=∏q_p(e), la identidad telescópica I_e=Σ_(j≤e)q_p(e)Z_j/q_p(j) da

    Σ_(k≤D) λ_k I_(k divide) = Σ_(d≤D) b_d Z_d,
    b_d = Σ_(d|k,k≤D) λ_k q(k)/q(d).

Aquí I_(k divide) es el producto de los indicadores de k. El segundo momento de este polinomio es h_λ(s), pues la probabilidad conjunta para dos índices es q(mcm(d,k)). Por inversión de Möbius hacia arriba, λ_d=Σ_(d|k,k≤D)μ(k/d)b_k q(k)/q(d), luego max|b_k|≥1/D. Además r_e decrece con e, así que 1−r_e≥1−r₁=(1−p^(−s))²≥(1−2^(−1/3))²>1/32. De q_p(e)≥p^(−e/2) se sigue q_p(e)(1−r_e)≥p^(−8e). En consecuencia ||Z_d||²≥d^(−8) y la suma ortogonal de cuadrados da h_λ(s)≥D^(−10). No basta la positividad cualitativa para vectores fijos porque la dimensión aumenta con x.

**Comparación uniforme de los cortes.** Repetir el contorno de 313 con el nuevo multiplicador. En el corte real todo el integrando de salto conserva su orientación y 0<v<1/L da un módulo ≫_t √x L^(−3/2)D^(−10). En los cortes complejos sustituir D² por D⁶ en 313. Con K>20/(1−2θ) el factor (C_t(m+2)log(C_t D)/L)^m cuesta D^(−K(1−2θ)+o(1)), suficiente para que ambos cortes sean de orden menor que el piso real. En el borde izquierdo exp(−cL/log D) domina toda potencia fija de D; en las horizontales y en la cola elevar el orden fijo de integración por partes para ganar también D^(−10). Todos los errores son uniformes en el vector normalizado. Esto prueba la desigualdad por homogeneidad.

El resultado es sobre la matriz de dilataciones de la media aritmética suavizada. La negatividad simultánea permite ensayar cualquier combinación de divisores hasta D, pero extraer B_t(x) sigue exigiendo controlar los índices superiores que entran en cada combinación.
