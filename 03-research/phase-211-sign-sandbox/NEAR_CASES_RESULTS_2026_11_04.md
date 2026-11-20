# Casos elementales, 2026-11-04

Estado: resultado auxiliar demostrado y contraejemplos algebraicos a posibles lemas; **ninguna prueba del signo global**. Fuentes locales leídas: Paper 47, especialmente `reson`, `nearfree`, `transl`, y README/mapa del Paper 48; el mapa y meta descartan presentar otra reformulación positiva como una vía nueva.

## 1. Mejora demostrable de nearfree: eliminar log log M

Sea χ real, suave y compacta en (-1,1), no nula. Escriba χε(t)=χ(t/ε), P=1/4−∂², ψε=Pχε y Dχ=∫x⁴|χ̂(x)|²dx>0. Para ε≤1,

    ||ψε||² ≥ Dχ/(2π ε³).

La función de Lévy del artículo tiene expansión K(s)=2Σ(j≥0) exp(−(2j+1/2)s). Por tanto

    |P²K(s)| ≤ 2Σ(j≥0)(2j+1/2)⁴ exp(−(2j+1/2)s) ≤ 400 s⁻⁵.

Prueba del último número: a⁴exp(−as/2)≤(8/(es))⁴ y Σexp(−(2j+1/2)s/2)=exp(−s/4)/(1−exp(−s))≤(1+4/e)/s; entonces 2(8/e)⁴(1+4/e)<400. El término j=0 de P²K es de hecho cero.

Si u≥4ε, las identidades de Fourier y dos integraciones por partes dobles dan

    m(ψε,V_uψε)=−(1/2)∫cχε(v) P²K(u−v)dv.

No hay términos de frontera porque χ es suave compacta; el término diagonal C0 desaparece porque las dos funciones tienen soportes disjuntos. Como |v|≤2ε y ||cχε||1≤ε²||χ||1²,

    |m(ψε,V_uψε)| / ||ψε||² ≤ Cχ (ε/u)⁵,
    Cχ=12800π ||χ||1²/Dχ.

Para los centros xm=log m−(1/2)log M, |xm−xk|≥|m−k|/M. Si ε=1/(KM), K≥8, la norma de la matriz de términos cruzados, dividida por ||ψε||², está acotada por 2ζ(5)Cχ/K⁵. El término diagonal del artículo satisface m(ψε)/||ψε||²≥log(1/ε)−C'χ. Su estimación exacta de divisibilidad permanece ≤log M+E. Resulta

    a(Fb)/||Fb||² ≥ log K−C'χ−E−2ζ(5)Cχ/K⁵.

En particular existe K0(χ) que da margen ≥1 para todo M y todo vector b con ε=1/(KM). Esto mejora el ε=1/[8KM(2+log M)] del Paper 47. No se afirma novedad frente al corpus completo: no apareció este argumento en las secciones revisadas.

Límite: K grande sigue impidiendo las near-coincidencias. La mejora quita una pérdida técnica, sin acceder al portador del signo que falta.

## 2. Primer defecto visible: dos paquetes

Tome centros log k y log(2k+1), con perfil ψε, y δ=log((2k+1)/(2k)). Al crecer ε por encima de δ/2 puede activarse el contacto n=2, pues su autocorrelación es cψε(δ). Para k grande y ε=O(1/k), ningún otro entero está cerca del cociente y los paquetes permanecen disjuntos. Defina

    a=m(ψε), h=m(ψε,V_log((2k+1)/k)ψε), c=cψε(δ), v2=2log2/√2.

La matriz exacta sobre estos dos paquetes es

    [[a, h−v2 c/2], [h−v2 c/2,a]].

Así la condición exacta es a≥|h−v2 c/2|. La incorporación del near-contact cambia la matriz por [[0,−v2 c/2],[−v2 c/2,0]], que tiene ambos signos si c≠0. Por ello el lema «activar un contacto cercano mejora/empeora la forma en orden de Loewner» es falso incluso en dimensión dos. Escoger signos opuestos de los dos coeficientes invierte el efecto.

En este ejemplo no aparece una amenaza asintótica al signo: a/||ψε||²=log k+O(1), |c|≤||ψε||² y h/||ψε||²=O(ε⁵). La desigualdad se cumple para k suficientemente grande. Un solo defecto local no explica la cancelación global.

## 3. Dos y tres aristas: la prueba por pares no basta

La matriz con diagonal 1 y las tres entradas extradiagonales −0.6 tiene cada sección 2×2 definida positiva, pero eigenvalores −0.2,1.6,1.6. Una inducción basada únicamente en las cotas de pares pierde la suma coherente. Con solo dos aristas (cadena de tres vértices) y peso c, la condición es c≤1/√2; con tres aristas iguales es c≤1/2, aunque cada par permite c≤1.

El patrón aritmético próximo al triángulo (2,2,4) lo dan k,2k+1,4k+3. Las distancias al contacto son

    δ12=log((2k+1)/(2k)),
    δ23=log((4k+3)/(4k+2)),
    δ13=log((4k+3)/(4k)).

Son respectivamente ~1/(2k),1/(4k),3/(4k). Con ε de orden 1/k se ven progresivamente las tres. Esto identifica un ensayo concreto de la cooperación de dos contactos primos y su potencia. **La matriz abstracta anterior no se ha realizado como una matriz negativa del Weil form**; para tres paquetes, nuevamente la diagonal log k domina los pesos fijos. Confundir el contraejemplo abstracto con un contraejemplo al signo sería incorrecto.

## Conclusión operativa

No sobrevive una nueva vía para cerrar el signo. Sí sobreviven: (i) una mejora auxiliar con prueba explícita; (ii) un contraejemplo mínimo a monotonía de near-contactos; (iii) una batería 2×2/cadena/triángulo para refutar pruebas por control independiente de aristas. Cualquier propuesta basada en estos patrones necesita controlar la norma colectiva de la matriz de near-contactos frente a la energía archimedeana, y esa desigualdad no se ha obtenido aquí.

## 4. Auditoría del primer ciclo con pesos aritméticos reales

Antecedentes revisados adicionalmente: phase-193 `CA_J_002_GKS_FRUSTRATION_AND_FKG_ON_THE_DIVISOR_LATTICE.md` y `CA_K_SYNTHESIS.md`. La frustración, holonomía, gauge y comparación diamagnética **no son una propuesta nueva** y están expresamente agotados allí.

Para los tres índices anteriores se tiene exactamente δ13=δ12+δ23, y el Euler factor fuerza Λ(4)=Λ(2). Elija ε=k^(−1/2). Aunque esta resolución ve near-coincidencias, en este subespacio de tres paquetes solo se activan los contactos 2,2,4 para k suficientemente grande. Los paquetes siguen teniendo soportes disjuntos. Por escala y continuidad,

    cψε(δij)/||ψε||² → 1,
    m(ψε,V_log(mi/mj)ψε)/||ψε||² → 0.

Por tanto las entradas extradiagonales normalizadas tienden a −x,−x,−z, donde

    x=log2/√2, z=log2/2=x/√2.

Si d=m(ψε)/||ψε||², el determinante límite de la plantilla es

    d³−d(2x²+z²)−2x²z.

El término cúbico orientado −2x²z es estrictamente negativo. **Falsificador preciso:** la afirmación «el primer ciclo cercano de tipo (p,p,p²), gracias a Λ(p²)=Λ(p), tiene contribución cúbica no negativa al determinante» es falsa ya para p=2 en el régimen descrito. No hay cancelación favorable del primer ciclo por esa identidad aritmética. El umbral espectral exacto de la plantilla es d≥(z+√(z²+8x²))/2, mayor que el umbral de la cadena d≥√2 x y el de una sola arista d≥x.

Este falsificador se refiere únicamente al signo del término cúbico propuesto; **no es negatividad de la forma**, porque aquí d→∞. Demuestra que ni la identidad de potencias ni el cociclo de desplazamientos proveen por sí solos la compensación deseada. Una conjetura colectiva distinta tendría que especificar y probar un mecanismo adicional; no se ha encontrado uno defendible en esta exploración.
