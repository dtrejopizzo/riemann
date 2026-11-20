# Ningún peso positivo de banda suficientemente estrecha admite el techo de su integral

Sea w continua, no negativa, no nula, de soporte en [a,b]⊂(0,∞), y L=log(b/a). Escribir V(s)=∫ w(t)t^(s−1)dt y E(x)=Σ_p(log p)w(p/x)−xV(1). Si γ es la primera ordenada positiva y ρ=1/2+iγ el cero crítico conocido, de multiplicidad m, entonces incondicionalmente

    limsup E(x)/√x ≥ m |V(ρ)| − V(1/2)/2.

En particular para L<2π/(3γ) el lado derecho es estrictamente positivo para TODOS esos pesos, cualquiera sea su perfil. El cociente b/a crítico para esta obstrucción es aproximadamente 1.160. No se asegura suficiencia para bandas que excedan esa razón.

**Polos y comparación.** En Mellin unilateral sobre x≥1 con medida x^(−s−1)dx, la transformada de E coincide, salvo una función entera, con V(s)P(s)−V(1)/(s−1), donde P(s)=Σ_p log p/p^s. El tramo retirado de la suma sólo ve finitos primos y está alejado de x=0. En Re s>1/3 se tiene P(s)=−ζ'(s)/ζ(s)+ζ'(2s)/ζ(2s)+R(s), con R holomorfa allí, por separación de potencias (los órdenes impares ≥3 convergen absolutamente). Se cancela el polo en 1 y hay regularidad en el eje real s>1/2. Los residuos en 1/2 y ρ son respectivamente −V(1/2)/2 y −m V(ρ), usando ζ(1+2iγ)≠0.

Si E≤c√x eventualmente, aplicar Landau a c√x−E en la cola: su integral converge para Re s>1/2 por regularidad real en ese semieje. Para s=1/2+δ, el módulo de su transformada en s+iγ no supera su valor en s, por positividad. Multiplicar por δ y pasar al límite da m|V(ρ)|≤c+V(1/2)/2. Retirar la cabeza compacta no cambia residuos. Aplicar a cualquier c superior al limsup prueba la afirmación, incluido el caso infinito por la interpretación usual.

**Geometría.** En V(ρ) las fases γlog t están en un arco de longitud γL. Para γL<2π/3, proyectar sobre la dirección central da |V(ρ)|≥cos(γL/2)V(1/2)>V(1/2)/2. Un solo cero crítico fuerza así excesos raíz a escalas arbitrariamente tardías, aun si hubiera otros ceros fuera de la recta. La detección por residuos aparece en 074; 105 prueba un techo equivalente al signo para un sombrero concreto de razón cuatro. Aquí la imposibilidad de un techo sin tolerancia vale para toda una clase de pesos y no exige RH.
