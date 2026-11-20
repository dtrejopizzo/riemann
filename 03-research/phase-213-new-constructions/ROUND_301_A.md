# Familias positivas mayores que la raíz después de sumar todas sus partes cuadradas

Para la discrepancia impar A de 300 escribir n=d²e, con d,e libres de cuadrados, coprimos, formados por primos impares congruentes con 2 módulo 3. El peso firmado es w(d)χ(e)w(e), donde w(m)=4^ω(m) en ese soporte y cero fuera. Fijar 0<δ<1, E=x^δ, un entero h de ese soporte y un conjunto finito F de primos impares inertes ajenos a h. Incluir todos los términos con

    e=h p a,    E<p≤2E primo inerte,    a divisor del producto de F.

El primo grande es único para x suficientemente grande; se suman todos los d admisibles. El resultado es asintótico a una constante no nula por x^((1+δ)/2), de signo −χ(h). En particular h=5 deja una contribución positiva mayor que la escala de raíz incluso después de admitir u omitir independientemente cada primo de F. Para h=1 la contribución tiene signo opuesto. F es fijo al pasar al límite.

**Media positiva de la parte cuadrada.** Para g fijo del soporte, la serie de w(d) con (d,g)=1 tiene un polo doble en 1 y su sumatorio hasta Y es asintótico a

    c Y log Y · ∏_(ℓ|g)(1+4/ℓ)^(−1),     c>0.

En efecto la serie básica ∏_(p impar inerte)(1+4p^(−s)) factoriza como ζ(s)²/L(s,χ)² por una corrección absolutamente convergente para Re s>1/2: el término lineal coincide en cada primo salvo 2,3, que se ajustan por separado. En Re s=1 las funciones ζ y L carecen de ceros, y en s=1 la corrección es positiva. Omitir g modifica sólo los factores locales finitos, que pueden ajustarse antes de factorizar. El teorema tauberiano de Ikehara–Delange para coeficientes positivos y polo doble da la fórmula, en particular un techo O(Y log(2Y)). Para excluir también el primo móvil p, la pérdida es ≤4Σ_(d'≤Y/p) w(d') ≪ (Y/p)log(2Y) si p≤Y y cero en otro caso. Así es despreciable uniformemente en el intervalo considerado.

**Constante y signo.** Para g=ha y cada primo p tomar Y=√(x/(gp)). El logaritmo de Y es asintótico uniformemente a (1−δ)log x/2. La suma de p^(−1/2) en la clase inerte entre E y 2E es asintótica a (√2−1)√E/log E por el PNT en progresión. Para a=1 la contribución es entonces asintótica a

    −χ(h) · 4c w(h)/√h · ∏_(ℓ|h)(1+4/ℓ)^(−1)
          · (1−δ)(√2−1)/(2δ) · x^((1+δ)/2).

Admitir todos los a multiplica esa constante por ∏_(ℓ∈F)(1−4√ℓ/(ℓ+4)). Cada factor es (√ℓ−2)²/(ℓ+4)>0. El denominador ℓ+4 es importante: al incluir ℓ en e se pierde la opción de incluirlo en d. Ignorar esa coprimalidad daría incluso el signo equivocado para algunos primos.

**Frontera del argumento.** Para e≤(log x)^B, el coste absoluto es O_B(√x·(log x)^(1+B/2)(1+log log x)^3), pues w(e)≤τ₄(e) en su soporte, Σ_(e≤z)τ₄(e)/√e≪√z(1+log z)^3, y el techo para la suma en d vale uniformemente al omitir coprimalidad. Esta parte sí cabe en x^(1/2+ε). Para e creciendo como potencia, el ejemplo positivo demuestra que un tratamiento bloque por bloque con sólo un conjunto fijo de primos de compensación no puede dar ese presupuesto a cada bloque. Todavía puede haber cancelación entre bloques de signos opuestos. No se ha obtenido una cota para A ni para C.
