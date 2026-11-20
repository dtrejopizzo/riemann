# Barrera para el corte equilibrado por encima de la raíz

Poner L=log x y R_t(x,y) como en 303. Existe K absoluto tal que, a frecuencia cero, **todos** los cortes

    √x ≤ y ≤ x exp(−K(log log x)²)

dan R₀(x,y)∼−48 U (log 2)² x/L⁵, uniformemente. El mismo intervalo conserva el equivalente de transición de 302 para cualquier t→0. Así la falta de velocidad en la ronda 304 tiene contenido aritmético: en la región con un único primo grande, un corte con saldo pequeño no puede atravesar esta barrera. Si se prueba el techo unilateral de la primera fila, la barrera mejora a x/y≤(log x)^(8+o(1)) en todo corte con |R₀(x,y)|=o(x/L⁵).

**Transporte entre cortes.** Denotar por B_t(v) el sumatorio completo. Para √x≤y≤x la identidad exacta es

    R_t(x,y)−R_t(x,√x)=2 Σ_(√x<p≤y) u_p B_t(x/p).

El cofactor es estrictamente menor que p. La cota clásica de Mertens por la región sin ceros, M(v)≪v exp(−c√log v), pasa a B_t(v) con otra constante c>0 uniforme para |t|≤1. En efecto usar la factorización de 294: en cada convolución por hipérbola las sumas largas se evalúan a argumentos ≥√v y la suma armónica absoluta de los coeficientes cortos cuesta una potencia de log v. La intersección rectangular satisface la misma estimación. Las sumas parciales de los factores χ(n)n^(±it) son O(log(2v)); las dos copias de μ tienen el techo clásico anterior. Al añadir la corrección absolutamente sumable en Re s=3/4 se divide en d≤√v y d>√v; en la cola se gana v^(−1/8) respecto al techo trivial con logaritmos. Las pérdidas logarítmicas se absorben reduciendo c un número finito de veces.

Puesto z=x/y, la diferencia de cortes cuesta O(x exp(−c√log z)), pues u_p≤2 y Σ_(√x<p≤x)1/p≪1 por el PNT. Elegir K con c√K>6 y aplicar 302 en √x. El error O(x/L⁶) es menor que el término principal en toda la transición, incluso cuando t=0.

**Prueba unilateral que podría falsificar la primera fila.** Si B₀(v)≤C_σ v^σ para 1/2<σ<1, la identidad anterior conserva la orientación porque u_p≥0. Por sumación parcial y la cota de Chebyshev se tiene Σ_(p≤y)p^(−σ)≪_σ y^(1−σ)/log y. Resulta

    R₀(x,y)−R₀(x,√x) ≤ O_σ(C_σ x z^(σ−1)/L).

Para elevar el saldo desde su valor en √x hasta o(x/L⁵) en módulo hace falta por tanto z^(1−σ)≪_σ C_σ L⁴. Si el techo vale para todo σ>1/2, necesariamente z≤L^(8+ε) para cada ε>0 y x suficientemente grande. En particular construir infinitos cortes equilibrados con √x≤y y x/y≥L^(8+δ), para algún δ fijo positivo, refutaría esa primera fila y por 299 también RH. Esta es una implicación condicional; 304 sólo proporciona x/y→∞ sin esa velocidad. Por debajo de √x intervienen enteros con dos primos grandes y la identidad de transporte usada aquí deja de valer.
