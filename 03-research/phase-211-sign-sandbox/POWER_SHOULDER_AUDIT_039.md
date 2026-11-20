# POWER SHOULDER AUDIT 039

Estado: INFINITE_SHOULDER039 APROBADO. Papers intactos.

## 1. Corpus y diferencia

Reconsultados índice de rutas, grid y crucigrama; contrastados UNIFORM_CUTOFF026, ENERGY_GROUP037 y SIGNED_MOMENTS038.026 controlaba el inverso compensado K mediante un corte de grado;038 conservó el producto firmado FINITO con un resto Fourier. La diferencia039 es una desigualdad para el producto INFINITO completo en sigma>1, y por tanto elimina la suma coprima omitida en esa región. No se llama nueva a la identidad Euler ni se traslada un resultado de K a h sin prueba.

## 2. Normalizaciones y aritmética infinita — APROBADAS

Leídos `POWER_INFINITE_SHOULDER_039.md` y `tools/power_infinite_shoulder_039_verify.py`; ejecución independiente PASS. Las razones h/H yK/G conservan los jacobianos y el factorn^−1/2. El perfil inclinado con c1/2 o3/2 y sigma=v+1/2 produce exactamenteFULL. La extensión izquierda puede ser firmada y no se considera una probabilidad.

La cota psi≤2x está demostrada: el binomio central controla psi(2n)−psi(n); la inducción con n=ceil(M/2) funciona para M≥6 y las bases1..5 se dominan por Mlog5<2M. Pasar a floor x es legítimo. Las integraciones de A yB son absolutas; paraB se descarta primero un término negativo antes de insertar psi superior. Esto evita un error con kernel de signo cambiante. A≤5/delta yB≤5/delta² valen en todo v≤2.

Todos los productos, momentos y la rama logarítmica centrada convergen absolutamente en sigma>1. f es acotado y su transformada integrable;Σn^−sigma justifica Fubini infinito. No se aplica Jensen firmado. El multiplicador y su resta de la traslación−A conservan todos los enteros Möbius.

## 3. Fourier uniforme y argumento físico — APROBADOS

La densidad positiva auxiliar tiene varianza2N(u²+v²)/(u²−v²)². Riccati da y*=2dv/(a_v+q′), y la separación respecto t_v≤4u²/(u²−4)². El control de variación y Chebyshev justifican el lower en t_v, no en un punto arbitrario. El factor(c+v) se absorbe en el normalizador y deja el mismo prefactor<√N/2 de038. La transformada tiene(c+v−iξ) y denominador a_v+ξ²+2ivξ; beta_v y los extremos uniformes son correctos. Las envolventes centrales y de cola12000/65 permanecen válidas.

En N≥4L²,L1000, t_v>A porqueL²>5·992. El argumento t_v−A es POSITIVO aunque el desplazamiento relativo sea negativo. Integrar q≥v−M s y controlar el cociente c+q da pérdida total≤15u²/L². El upper usa q(t_v)−v≤Mv/(u²+v²) y da exp(5/L²). Ambos errores de Fourier son≤.06 y<.005, con la cola estimada por el tercer término positivo de la exponencial. Quedan aprobadas las razones completas entre(.9)U_sigma y(1.1)U_sigma, para ambos c.

## 4. Toda la cola y comparación con026 — APROBADAS

v→t_v es estrictamente creciente, así los centros parametrizados cubren TODO[T_N,t_2], no una lista de puntos. Después de t_2, q≥2 yq′<M<5/4 implican la logderivada de dilatación<−2 para ambos inversos. La suma absoluta de n≥2 es entonces<3/4; ambos cocientes son>1/4. Así h_N yK_N son positivos para TODA x≥exp T_N y TODO N≥4,000,000.

La expansión T_N=d/992+(1985L/992²)√N+O(1) es correcta. Como v_N≤1, T_N≤2d/(u²−1)<d/330; los dos cortes anteriores deK026 son>d/330. La comparación se hace con el MISMOK, y el resultado también mejora el corte previo deh020. No se confunde ese hecho con positividad de W.

## 5. Alcance

Es nuevo signo del inverso COMPLETO en un hombro energético real y toda su cola, no sólo un grupo finito o su valor absoluto. La región sigma1 crítica y el interior restante no están cubiertos. La cola de ERR es favorable al emparejarh conB<0, pero no se ha demostrado compensación cuantitativa del interior ni de ARCH_sharp. No hay nueva filaW, ventanaT o cierre global. Root coincide independientemente en la prueba y el verificador.
