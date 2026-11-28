# Igualdad de multiplicidades: auditoría profunda en curso

## Fallo literal en `pm:siegel(c)` de paper 51

**Dictamen (b) para la afirmación de convergencia uniforme en todo g.** La primera afirmación incorrecta está en `main.tex:4453`; se repite en la última frase de su demostración, líneas 4511–4512. No se trata de un contraejemplo al teorema de multiplicidades.

El lema afirma que, con x en un compacto, la serie

`Σ_{γ∈G(F)} M_{B′}(g⁻¹γx)`

converge uniformemente respecto de g en todo G(A_F). Tomar x=1 y elegir el compacto Ω_f conteniendo 1, como permite el enunciado. Para cualquier conjunto finito J de índices, elegir γ₀ fuera de J y poner g=γ₀. La cola no negativa es entonces al menos

`M_{B′}(g⁻¹γ₀)=M_{B′}(1)=1`.

Por el criterio uniforme de Cauchy, las colas no tienden uniformemente a cero. Existen infinitos γ₀ en el caso isotrópico de esta sección, por ejemplo en un subgrupo unipotente racional no trivial.

La estimación anterior del lema, uniforme en g para la **suma total**, sí sigue del argumento de conjuntos disjuntos. Esa estimación no implica convergencia uniforme de las colas: al variar g, el término grande puede desplazarse a cualquier índice.

## Reparación y alcance

Reemplazar la conclusión por convergencia uniforme cuando **ambos g y x recorren compactos**. En la prueba de conjuntos disjuntos puede entonces elegirse un entorno fijo U. Para g y x en compactos, los conjuntos g⁻¹γxU correspondientes a γ fuera de un conjunto finito escapan uniformemente de cualquier compacto. Su suma está dominada por la integral de la función integrable M′ fuera de ese compacto, que tiende a cero. La discreción de G(F) hace finito el conjunto de γ que no escapan.

Esto basta para continuidad local de las sumas de `pm:bound(a)` y de la función F de `pm:bound(c)`. La cota global en g de la suma total, que permanece válida, proporciona el mayorante integrable al convolucionar con e∈L¹ en 4587–4589. Por tanto esas aplicaciones no necesitan la afirmación falsa de convergencia uniforme global.

## Comprobaciones adicionales de esta tanda

- `pm:kernel(c)`: la densidad de Cartan se acota por exp(n(n−1)t₁); integrar los restantes parámetros introduce sólo un factor polinómico. B′>n² basta para integrabilidad.
- `pm:kernel(a,b)`: la idempotencia usa ortogonalidad de Schur con el grado formal. La construcción de α usa un espacio finito de tipos K y la densidad de vectores suavizados, de modo que la pertenencia a la clausura implica pertenencia al subespacio. No requiere un inverso de operador infinito.
- `pm:cusp`: una vez admitida la proyección de Harish-Chandra y su finitud sobre el centro, la integral constante satisface una EDO de coeficientes constantes a lo largo de A′. El decaimiento en ambas direcciones excluye todo polinomio exponencial no nulo. El exponente B=5n³ satisface las integrabilidades y el margen B/2>2n² para n≥2.
- `pm:decay`: el argumento de oscilación utiliza la cota global de F, la anulación de su término constante y el supremo ponderado C*. La desigualdad C*≤max(C*/2,T(δ/ε₀)^j) da la conclusión sin exigir que el supremo se alcance.

Estas verificaciones no cierran aún `pm:main`: faltan en esta tanda la comparación de clases elípticas, la eliminación del lugar auxiliar y el cotejo completo de las entradas arquimedianas. Se registran por separado de la reparación anterior.

## Segunda tanda: comparación y eliminación del auxiliar

Se reconstruyeron las líneas 4640–5029. La comparación y la eliminación del auxiliar son correctas como deducción de `pm:arch`, de las entradas clásicas de teoría de cuerpos de clases y clasificación hermitiana citadas, y de (G). La corrección de uniformidad anterior basta para los usos del núcleo en esta deducción.

1. **Polinomios con factores coprimos (`pm:red`).** El proyector de Bézout varía continuamente y proporciona secciones locales del espacio de descomposiciones. La función Ψ sobre H×X tiene soporte compacto: las componentes diagonales m están en un compacto, y la inversa de z↦m₁⁻¹zm₂−z permanece acotada allí porque los polinomios característicos coprimos se fijaron. La integración en N anula Ψ por supercuspidalidad. No se presupone que los factores sean irreducibles localmente. Para potencias propias, la reducción no puede tener un cero simple: es exactamente la obstrucción usada por (Z).
2. **Clases racionales (`pm:classes`).** El cociente c₁/c₂ es norma en todos los lugares finitos por conjugación local, y en los infinitos por igualdad de signos. El teorema de la norma de Hasse para la extensión cuadrática da conjugación racional. Para cambiar signos, la condición de producto es (−1)^{f(q+q′)}=1; f par la garantiza. El núcleo del símbolo de Artin da un x con esos signos y xN(z)=1 en los lugares finitos. Landherr identifica V_{cx} con V′. Así se obtiene el producto de clases finitas por **todas** las elecciones de signos admisibles, y no simplemente una inyección.
3. **Raíces fuera del círculo (`pm:selberg`).** Las líneas propias de módulo mayor que uno forman un subespacio isotrópico no nulo. En el radical del parabólico que lo estabiliza, Ad(γ)−1 es invertible. El cambio triangular en el grupo unipotente reduce la integral orbital al término constante de e, nulo por `pm:cusp`. La convergencia absoluta proviene de `pm:bound(b)` antes del desdoblamiento; el texto trata expresamente los factores de integral absoluta nulos.
4. **Signo y medida (`pm:ell`).** El toro infinito tiene masa 1; por eso la integral sobre G en `pm:arch(b)` concuerda con la integral orbital sobre T\G. Cada asignación de signos aparece p!q! veces en S_n, factor que se cancela. El signo final es (−1)^{pqf}=1. El volumen adelico del toro y las integrales orbitales finitas se identifican por L, independientemente de V. El tratamiento separado del carácter compacto nulo evita cancelar un factor que podría ser cero.
5. **Álgebra lineal del auxiliar (`pm:line`).** Aunque A no sea normal, cada espacio propio generalizado suyo es invariante bajo T y T*, porque A conmuta con ambos; por tanto es un subespacio reductor de T y la restricción de T* es efectivamente el adjunto. Las potencias positivas de T determinan sus autovalores y multiplicidades porque T es invertible. El determinante de TT*=d(1+cε) recupera el rango de ε. El espacio correspondiente a α=0 no contribuye a tr(Aε); no falta recuperar ese bloque.
6. **Cálculo de Hecke (`pm:hecke`).** tJt⁻¹ impone la condición de fila opuesta a la condición de columna de J. Hay dos dobles clases J\K/J. El valor en 1, vol(J)q^{n−1}, y la integral total determinan el segundo valor vol(J)q^{n−2}(q−1). De aquí sale exactamente TT*=q^{n−2}(1+(q^n−1)ε). Las potencias de JtJ matan la primera línea módulo la uniformizante y son invertibles en el cociente; el cero del polinomio reducido sigue siendo simple.
7. **Aplicación del auxiliar.** El lugar u se escoge fuera del soporte y distinto del lugar supercuspidal. Las potencias convolutivas conservan supercuspidalidad por Fubini. La igualdad de trazas de A^lT^i permite aplicar `pm:line` y recuperar el proyector de nivel maximal, con el mismo factor vol(K) en ambos grupos.
8. **Paso a los datos.** Una familia buena tiene al menos una etiqueta irreducible, la que suministra la componente supercuspidal. La demostración de (G) reduce la cuspidalidad a la ausencia del simplex de grado r en productos de caracteres de rangos menores; es correcta si se admiten las identidades de Green expresamente citadas. No atribuyo aquí una comprobación del facsímil original de Green. La igualdad de trazas para el álgebra conmutativa estable por adjuntos determina las multiplicidades por independencia de caracteres. La extensión a lugares inertes de `pm:rem-full` usa la libertad de la función fuera del lugar supercuspidal; no aplica erróneamente la identificación con GL_n en un lugar inerte.

**Pendiente delimitado:** cerrar la entrada arquimediana `pm:arch` (decaimiento y suma orbital) con sus dependencias de series discretas y comprobar documentalmente las formulaciones clásicas citadas. No se afirma igualdad de multiplicidades para dos grupos arbitrarios sólo por ser isométricos en lugares finitos: las condiciones de parámetros, tipos y componente supercuspidal son esenciales en la prueba auditada.

## Tercera tanda: integral orbital y grado formal

Se reconstruyeron los argumentos de `pbr:basic` a `pbr:degree`, líneas 5199–5833. La deducción interna de la integral orbital y de la constante del grado formal es correcta **condicionada a las entradas de series discretas y a las fórmulas de coeficientes de paper 49 declaradas en R1–R4**. La auditoría de esas entradas se comparte con los agentes de theta y spanning; no se oculta bajo la expresión «Harish-Chandra».

- La desigualdad de reordenamiento con ganancia se obtiene perturbando o por ±e_i; su integralidad conserva la inversión débil del orden. El lema de término superior controla también permutaciones dentro de cada bloque: la desigualdad estricta obliga a w=1 al calcular el coeficiente superior. La separación entre signos asegura que κ+ND conserva el orden aun cuando dos pesos del mismo signo estén próximos.
- En `pbr:int`, la identidad del menor positivo convierte el crecimiento de g en separación de autovalores. El exponente pqM cabe dentro de la separación h₀ y el mayorante final es integrable porque 2M>n². Esto justifica una integral de Bochner en C(K), no un intercambio formal de distribuciones.
- En `pbr:laurent`, los coeficientes contra caracteres son enteros por ortogonalidad de Schur y expansión finita del producto de un carácter por el polinomio regularizador. Bessel obliga a que sólo haya finitos coeficientes no nulos. La identificación P=D^Mt se comprueba coeficiente a coeficiente; las sumas relevantes son finitas incluso cuando t es una serie formal infinita.
- En `pbr:flag`, el jacobiano complejo b^{2ρ} se convierte en |b^{2ρ}|² como jacobiano real. La medida compatible se conserva al multiplicar por i las coordenadas entre signos opuestos. Así j_H es el mismo para U(p,q) y U(n). La masa 1 del toro permite la comparación sin un volumen oculto. El complemento de la celda es nulo por analiticidad real y no por una afirmación algebraica de medida no justificada.
- En `pbr:Un` y `pbr:orbit`, la fórmula compacta de coeficientes y dos aplicaciones de Schur dan el factor exacto 1/dim(Vσ). El cambio (y,k)=(vu,u⁻¹) conserva Haar producto. La normalización d_Λ∫_K|m_Λ|²=1 elimina el factor de tipo K. La aplicación de Fubini está respaldada por `flagG`.
- En `pbr:gain`, invertir X cuando se invierte el orden de los pesos conserva las hipótesis. Jacobi y Fischer se aplican sólo a matrices positivas. La cota con una entrada entre bloques cancela el numerador del error mediante `pbr:compact`. En `pbr:Ebound` se conserva el desplazamiento e en la constante C_e; no se exige uniformidad en e.
- En `pbr:low`, se continúa una identidad de una variable holomorfa desde un arco interior del sector. Tras el límite radial, variar e∈Zⁿ separa los exponentes del mismo nivel mediante independencia de caracteres. Esto evita suponer que el término de menor nivel sea único.
- Los cinco pasos finales comparan coeficientes de nivel bajo, eliminan permutaciones entre signos por la ganancia h₀ y recuperan todos los coeficientes por antisimetría. El coeficiente superior impone s₀=1. Por tanto `pbr:degree` da exactamente d=dim(Vσ)=∏_{i<j}(λ_i−λ_j)/(j−i), con Haar compatible, y σ_λ=(−1)^{pq}. Esta constante no se obtiene por una aproximación asintótica.

La obligación restante de este frente queda reducida a los inputs de paper 49 sobre el coeficiente de la serie discreta, su identificación y el cono de tipos K, más el cotejo externo de las entradas clásicas señaladas. No se encontró un fallo adicional en esta reconstrucción interna.
