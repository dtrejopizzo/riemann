# Una cota explícita en cada ventana a partir de la representación positiva

**Proposición.** Tomemos como entrada la conclusión espectral del paper 46: cada cero no trivial de ζ tiene parte real 1/2. En la normalización de su forma completa, para todo T>0 y toda función de su dominio soportada en [−T,T] se tiene

    W_T(f) ≥ exp(−K) ||f||₂².

Para calcular K se puede reemplazar T por max(1,T). Escribimos s=T+1, U=T+1/100, n=ceil(2U/log 2) y definimos

    L = 2 log(2) ∑_{k=1}^n 2^k / √(2^{k−1}),
    R = exp(L+5),    K = 22sR log(9680000 s²).

En particular sirven exp(−10^529) en radio 5 y exp(−10^67360) en radio 10. Son pisos deliberadamente pequeños en la norma original. La deducción usa la fórmula explícita de Row C y el resultado de localización de ceros de Row D con los insumos indicados allí. Es distinta de extender el certificado de altura fija 3·10¹². El papel de la localización se ve en una sola desigualdad de comparación.

## Demostración

Por inclusión basta T≥1. Normalizamos ||f||₂=1 y comenzamos con el núcleo suave. Sea m=ceil(10sR), H=200m, a=R²/(2H²). En frecuencia aplicamos el multiplicador

    u(t) = 1 − sinc(t/H)² / sinhc(1/(2H))²,     ĝ(t)=u(t)^m f̂(t),

donde sinc(x)=sin(x)/x y sinhc(x)=sinh(x)/x con valor uno en cero. Sobre la recta real 0≤u≤1. En ±i/2 se tiene exactamente u=0. El inverso de Fourier de sinc(t/H) es una uniforme de radio 1/H. Por convolución, g se soporta en [−U,U] pues 2m/H=1/100, y sus dos momentos de Tate son cero. La expresión espectral del paper 46 da

    W_T(f) − W_U(g) = ∑_γ (1−u(γ)^{2m}) |f̂(γ)|² ≥ 0.                 (1)

Esta comparación conserva la forma completa y usa todas las ordenadas, con multiplicidad.

**Estimación aritmética de g.** El operador primo en [−U,U] tiene norma a lo sumo 2∑_{q≤exp(2U)} Λ(q)/√q ≤ L. En efecto, para j=2^{k−1}, toda potencia prima en (j,2j] aporta su logaritmo primo al logaritmo de (2j sobre j), por la fórmula de las valuaciones del factorial. Los demás sumandos en esa fórmula son no negativos y (2j sobre j) ≤ 2^{2j}. Esto explica los términos de L. El multiplicador arquimediano M de Row D cumple M(t)≥M(0)>−6, así como M(t)≥log(|t|/(2π))−1/|t|−1/(2t²) para |t|≥R. Por la definición de R, M−L≥1 allí. El coste polar de g es cero.

**Filtro.** En |t|≤R se tiene u≤a: usar 1−sinc² x≤x²/3 y 1−sinhc(y)^(−2)≤y², consecuencia de sinhc(y)≤exp(y²/2) por comparación de series. Resulta u≤(R²/3+1/4)/H²≤a. En |t|≥4R se tiene u≥4a. Para 4R/H≤|x|=|t/H|≤1, la serie alternada da sinc(x)≤1−x²/7 y por tanto 1−sinc² x≥x²/4. En 1≤|x|≤2 usar el decrecimiento de sinc y sin(1)²<3/4; desde 2 usar |sinc x|≤1/2. En ambos casos 1/4>4a por H≥2000sR.

**Fuga.** Si Ω=4R, la fracción de masa de |f̂|² en |t|>Ω es al menos η=[1+(1+TΩ) exp(2TΩ+2)]^(−1). Recordamos la prueba. Sea l=1/T y A=Ω+l. La integral J(z) de f̂(z+y) conjugado(f̂(conjugado(z)+y)) para −l≤y≤l es entera de tipo 2T. Sobre los rayos reales |x|≥A está acotada por la masa exterior E. En la banda |Re θ|<π/2, J(A sin θ) exp(−2TA cos θ) está acotada, pues Re cos θ≥|Im sin θ|; en los bordes tiene módulo ≤E. Por tres líneas J(x)≤E exp(2TA) en [−A,A]. Integrar allí cuenta cada frecuencia interior durante una longitud 2l, dando 2l E_in≤2A exp(2TA) E. Esto prueba la desigualdad. En particular −log η≤8TR+2+log(2(1+4TR))≤12sR (usar log(1+x)≤x).

La expresión aritmética, Plancherel y las tres regiones anteriores implican

    W_U(g) ≥ a^{2m} [4^{2m}η − (L+6)] ≥ a^{2m}.

En la banda intermedia R≤|t|≤4R el integrando minorante es no negativo. Para la última comparación, 2m log 4−12sR>15sR y exp(15sR)>L+7. Finalmente m≤11sR y a≥1/(9680000s²), de donde a^{2m}≥exp(−K). Aplicamos (1) y pasamos al dominio por densidad en norma de forma. El piso vale en cada ventana; depende de T.

## Relación con el certificado de altura finita

La conclusión global del paper 46, por sí sola, da el piso cero. Aquí permite retirar la densidad correctora de las fases anteriores y usar un filtro contractivo que anula exactamente los dos polos. El filtro de potencias y la fuga tienen antecedentes en fase 213, rondas 176–179; la fase 176 ya da una ley asintótica bajo alturas de verificación crecientes. Esta nota da parámetros en todas las ventanas y los especializa en 5 y 10.

Si se usa sólo la altura verificada G, (1) adquiere sumandos para los ceros exteriores evaluados en frecuencias complejas; la contracción real no da el signo de esos sumandos. Para obtener los mismos radios con esos insumos bastaría acotar por debajo su contribución total a la diferencia por −(a^{2m}/2)||f||². Ninguna de las evaluaciones numéricas de esta carpeta acredita esa desigualdad.

Fuentes del repositorio: paper 45, fórmula explícita; paper 46, conclusión y sección sobre los insumos de la demostración; anexo, teorema etiquetado i4:thm-final y sus cuatro hipótesis. Fase 213, ROUND_195_A, auditoría inversa del radio 5: la estimación de la norma del operador primo con la altura anterior ya encuentra una obstrucción en U=3.156. La presente deducción no requiere auditar las entradas aritméticas del anexo de nuevo.

**Reproducción.** Ejecutar python3 verify_bounds.py con python-flint. El programa encierra log10 K mediante Arb; la desigualdad funcional se justifica arriba.
