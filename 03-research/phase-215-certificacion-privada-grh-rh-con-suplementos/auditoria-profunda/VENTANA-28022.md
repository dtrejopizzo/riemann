# Ventana fija 2.8022: certificado localizado y ejecutado

Fecha de esta comprobación: 2026-11-28. Alcance: localizar y comprobar el certificado de 17 verificaciones citado por paper46, sin buscar ni optimizar el extremo T. No se consultaron papers47/48. La auditoría del puente analítico de las notas de investigación se realiza separadamente por el agente principal: este documento no convierte la ejecución del código en una certificación automática de la desigualdad funcional.

## Resultado que sustituye la anterior búsqueda incompleta

**El certificado existe, es público y se ejecuta satisfactoriamente.** La afirmación anterior de que faltaba el archivo debe retirarse. La búsqueda limitada a los papers no encontraba el código porque está en el árbol de investigación:

- Archivo: `03-research/phase-213-new-constructions/verify_periodic_pivot_280.py`, 81 líneas, 3368 bytes.
- Prueba analítica anterior y adaptación: `03-research/phase-213-new-constructions/ROUND_195_A.md:3897–3903` y `:5167`.
- Enunciado correspondiente: `04-papers/46-row-d-sign-radial-intersection-form/main.tex:1914–1930`.
- Revisión pública consultada: `97fb4e78d5a858baa926829a42336ae3b914e59a`.
- [Archivo público fijado a esa revisión](https://github.com/dtrejopizzo/riemann/blob/97fb4e78d5a858baa926829a42336ae3b914e59a/03-research/phase-213-new-constructions/verify_periodic_pivot_280.py).
- SHA256 local y remoto idénticos: `2a3dbca06c75e6e7557978263997f146d50aa96259a43f7ce77a7fff46adff68`.

La búsqueda decisiva fue `rg -l --hidden`, excluyendo `.git`, los directorios47/48 y nuestros informes, con la expresión `120110026807|120122483651|2673507086718`. Encontró el script, ROUND_195_A, papers46/58 y ROUTES-MASTER-INDEX. La API recursiva de GitHub informó árbol no truncado; se descargó el archivo raw de la revisión indicada y se comparó byte por byte con el local.

## Ejecución y contenido de las 17 verificaciones

Se ejecutó directamente, sin editarlo:

```sh
python3 03-research/phase-213-new-constructions/verify_periodic_pivot_280.py
```

Entorno: python-flint0.9.0; precisión Arb192 bits fijada por el propio código, línea5. Código de salida0; los 17 controles emitieron PASS. Parámetros exactamente coincidentes con paper46: T=14011/5000, U=57/20, R=2014985964, b=13, m=9115062736, H=2673507086718, G=3000000000000 y N=120122483651. No se efectuó búsqueda de parámetros.

| # | Línea del script | Etiqueta y desigualdad comprobada | Resultado |
|---|---:|---|---|
| 1 | 21 | `prime enumeration range`: exp(2U)<300 | PASS |
| 2 | 49 | `positive symmetric weights`: los2048 pesos enteros son positivos y simétricos | PASS |
| 3 | 52 | `all continuous Schur rows`: cada fila superior es estrictamente menor que19.486 veces su peso | PASS |
| 4 | 53 | `support`: T+(b+1)(m+48)/H<U y2U<13/2 | PASS |
| 5 | 55 | `archimedean margin`: log(R/(2π))−1/R−1/(2R²)−19.486>1/10 | PASS |
| 6 | 56 | `global low floor`: ψ(1/4)−logπ−19.486>−26 | PASS |
| 7 | 57 | `spectral regions`: G≤2H, H<G y2R<H | PASS |
| 8 | 62 | `mask band edge`: v<1 y las dos cantidades escritas superan7a/2 | PASS |
| 9 | 70–71 | `polar and signed low band versus gain`: ganancia logarítmica supera coste polar y2logJ por más de10; coste polar positivo | PASS |
| 10 | 72 | `denominator floor`: m arcosh(2/a−1)<120110026806 | PASS |
| 11 | 73 | `low mask positive`: a<1/2 y m arcosh(2/a−1)−log4>2logJ | PASS |
| 12 | 74 | `cutoff prefactor`: 2·16·exp(19/4)·25/(2π)<10⁵ | PASS |
| 13 | 75 | `cutoff tail ratio`: H+2.718N<G | PASS |
| 14 | 76 | `low correction`: log(10⁹)+loglog(3+G)−Nlog2.718<−120110026808 | PASS |
| 15 | 78 | `series converges`: z=m/cosh²b<1 | PASS |
| 16 | 80 | `high correction`: high=2z²⁵/(1−z)<1/2 y high·10⁹log(3+G)<1/1000 | PASS |
| 17 | 81 | `reserved density`: 1/(80π)>1/1000 | PASS |

Las expresiones a, v, J, coste y ganancia están definidas en líneas58–69. Las comparaciones Arb certifican separación estricta de intervalos; una comparación indecidida no se trata como PASS. `unique_fmpz()` exige que los pisos y techos utilizados sean un entero único.

## Qué sí prueba la parte de Schur, sin extrapolar una malla

Esta parte puede justificarse directamente a partir del código. Sea h=2U/2048 y w la función positiva constante en las celdas, extendida por0 fuera de la ventana. Para cada potencia prima q=p^k, el código obtiene d=floor(log(q)/h) y c=ceil(10⁸log(p)/sqrt(q)). Un punto x de la celda i trasladado por log(q) pertenece, salvo fronteras de medida cero, a la celda i+d o i+d+1. Por eso el máximo de los dos pesos vecinos de línea36 es una cota válida **en toda la celda**, no sólo en los nodos. Si el traslado sale de la ventana se usa el peso0. La simetría de w identifica la cota para traslaciones negativas con la reflexión de la positiva, línea41.

La enumeración de primos por división hasta isqrt(p) es exacta. Se enumeran todas las potencias relevantes: exp(2U)<300, y las que tienen desplazamiento mayor o igual al número de celdas no contribuyen en L². La cota de cada coeficiente es hacia arriba. Línea52 comprueba por aritmética entera las2048 desigualdades de Schur. En consecuencia, el operador simétrico de traslaciones por potencias primas, con coeficientes log(p)/sqrt(q) en ambas orientaciones, tiene norma≤19.486 en esa ventana.

Las70 iteraciones previas únicamente producen un candidato de pesos. No se usa ninguna hipótesis de convergencia ni optimalidad de esas iteraciones: la positividad, simetría y desigualdad final se comprueban después. **Dictamen(a) para esta cota de Schur tal como la implementa el certificado.**

## Puente analítico que debe acompañar al certificado

ROUND_195_A:3897–3903 describe primero T=14/5 y parámetros anteriores. La línea5167 sustituye los parámetros y el exponente por los actuales y afirma que se conserva la misma prueba. Esta localización es sustancialmente distinta de una ausencia de prueba o código.

Para certificar la desigualdad universal de paper46 hace falta verificar, además de los17 resultados numéricos, estas obligaciones concretas en las fórmulas anteriores179/190/192/193 de las notas:

1. Definición del multiplicador entero de tipo exponencial, su máscara no negativa y el polinomio recíproco truncado en grado24; justificación del soporte T+(b+1)(m+48)/H y del factor J=25(2m)^24.
2. Paso de la fuga de masa de Fourier a la ganancia de Chebyshev, con los factores1/10,26,4,80 y la normalización de Plancherel.
3. Identificación de B con el denominador de Chebyshev y traducción del control10 a la cota exponencial para B.
4. Construcción del cutoff con N uniformes; densidad de error de ceros exteriores y constante10⁹log(3+G), basada en Z2/Z3. El cociente2.718 y el prefactor del control12 sólo verifican las hipótesis numéricas de esa estimación.
5. Cola alta de máscara≤2z²⁵/(1−z)(H/|τ|)^50, signo sobre los átomos, reserva1/(80π) y cobertura completa de regiones espectrales.
6. Extensión desde funciones suaves al dominio cerrado de la forma y monotonía por inclusión de soportes.

El agente principal revisa estas obligaciones. **Estado de este documento: ejecución numérica y Schur demostrados; inferencia funcional completa condicionada al cierre de ese puente.** Esto no es un dictamen de falsedad de la cota ni una alegación de certificado ausente.

## Z1: fuente primaria y comprobación independiente del dato exacto utilizado

Paper46:1788–1791 necesita sólo: existe un cero simple en1/2+i[14.13,14.14] y no hay otros ceros no triviales con0<Imρ≤21. La versión para alturas negativas se deduce por conjugación. No requiere los decimales adicionales impresos.

Se consultó directamente [Platt–Trudgian, The Riemann hypothesis is true up to 3·10¹²](https://arxiv.org/pdf/2004.09765), teorema1 y §2, páginas2–3. El teorema da el alcance; la descripción metodológica explica que cuentan cambios de signo y los cotejan con el número total mediante Turing. Igualdad entre cantidad de intervalos con cambio de signo y cantidad total de ceros **con multiplicidad** implica simplicidad: cada intervalo aporta al menos una unidad y un cero múltiple consumiría más. El teorema de RH por sí solo, sin este argumento de conteo, no justificaría simplicidad. Este artículo no imprime una tabla con las primeras dos ordenadas; no se le atribuye una tabla inexistente.

Como comprobación separada de la parte precisa de Z1 se ejecutó, también a192 bits:

```python
from flint import acb, arb, ctx
ctx.prec = 192
rho = acb.zeta_zero(1)
assert arb(1413)/100 < rho.imag < arb(707)/50
assert rho.real == arb(1)/2
assert arb(21).zeta_nzeros() == 1
```

Las tres aserciones pasan. Resultado de la primera ordenada:

`[14.1347251417346937904572519835624702707842571156992431757 +/- 1.77e-56]`.

N(21) devuelve el entero exacto1. Este número cuenta la franja crítica, no sólo los ceros ya localizados sobre la recta. Existencia del cero aislado y N(21)=1 bastan para unicidad y simplicidad. Se cotejó la semántica con las fuentes primarias del programa: [documentación FLINT sobre ceros](https://flintlib.org/doc/acb_dirichlet.html) y [función de conteo N(t)](https://flintlib.org/doc/acb_dirichlet/acb_dirichlet_zeta_nzeros.html). Esta es una comprobación de Z1 a altura21, no una búsqueda del extremo de la ventana. Otro agente efectuó independientemente la misma comprobación.

**Dictamen(a) sobre el contenido matemático de Z1 utilizado.** La consulta histórica directa del original Rosser–Yohe–Schoenfeld1968 no se completó aquí; por eso no se da por cotejada cada página de esa referencia. La confirmación anterior no depende de atribuirle resultados no leídos.

## Cierre posterior del puente

El puente funcional fue reconstruido por el agente principal y revisado independientemente por el agente theta. Véase [VENTANA-28022-PUENTE.md](VENTANA-28022-PUENTE.md). Las 17 comprobaciones, junto con ese argumento y Z1–Z3, sí dan la desigualdad universal en la ventana declarada. El estado condicional de las secciones históricas anteriores queda superado por este cierre. Paper46 reporta el resultado sin desarrollar ese argumento: para una lectura autocontenida debe incorporar o citar precisamente estos anexos y el programa.

## Segunda revisión independiente del puente analítico

Tras la primera entrega se leyó íntegramente `VENTANA-28022-PUENTE.md` del agente principal y se cotejó con ROUND_172_A,173_A,175_A,178_A,179_A,190_A,192_A; con la construcción inicial de ROUND_193_A; y con ROUND_195_A:3897–3903,5167. No se encontró un fallo sustancial en esta reconstrucción. Las siguientes comprobaciones fueron rehechas, no inferidas del resultado PASS:

- **Identidad espectral firmada.** El emparejamiento β↔1−β sustituye las exponenciales reales por cosh(δt); la corrección recortada reproduce el mismo dato sobre las diferencias de ambos soportes. El cutoff es1 hasta6.5 y2U=5.7. La cota sumable de las correcciones y el crecimiento logarítmico de su densidad justifican el intercambio para tests suaves. Por tanto la resta exacta entre W(f) y W(g) sí produce el factor1−Q² contra la misma medida, sin presuponer que esa medida sea positiva.
- **Filtro entero.** La serie par de cosh elimina la rama de la raíz. La desigualdad |Re sqrt(1−(x+iy)²)|≤sqrt(1+y²) controla el tipo; multiplicar por el polinomio de grado m/2+24 cuesta exactamente (m+48)(b+1)/H. La cota real de Q permite Paley–Wiener en L². La transformada inversa es una distribución de soporte compacto; convolucionarla con un test suave conserva la suavidad y el soporte declarado.
- **Coeficientes recíprocos.** Las raíces r_i∈(0,a) dan producto ∏(1−v/(1−r_i))⁻¹. Sus coeficientes son sumas de monomios completos, dominados por la expansión multinomial de (Σ_i(1−r_i)⁻¹)^j, de donde c_j≤m^j. En0≤u≤a, J=25(2m)^24 domina la suma; en a≤u≤1 la truncación tiene signo positivo y no excede el recíproco. Las dos regiones prueban0≤Q²≤1 globalmente. La cola empieza precisamente en grado25, de donde la potencia50, no48.
- **Fuga.** En la franja de la prueba de179, Re cos(x+iy)=cos(x)cosh(y)≥cos(x)|sinh(y)|=|Im sin(x+iy)|. Así la función auxiliar es acotada sin una hipótesis oculta de crecimiento. En los bordes su argumento es real exterior. La integral de J sobre[−A,A] incluye exactamente el peso2d de cada frecuencia interior; se obtiene el denominador de η escrito, también para f complejo.
- **Polo y ganancia.** u(i/2)≤0; |1−u(i/2)|≤2 y |u(i/2)|≤(b+2)/(2H²) con estos parámetros. La cota Chebyshev al argumento negativo introduce arcosh(1+(b+2)/(H²a)), sin factor2 adicional. El factor m aparece después de elevar al cuadrado el Chebyshev de grado m/2. El coste polar4exp(T) es una cota válida por Cauchy–Schwarz. De las dos desigualdades de ganancia con margen10 se deduce rigurosamente ganancia−coste_polar−26J²>2, pues tanto coste_polar como J² son≤exp(gain_log−10), y J≥1.
- **Dos colas y normalización.** La corrección baja es una densidad respecto de dτ, por eso cuesta2πexp(−D−2) en unidades de ‖f‖². La reserva alta es densidad respecto de dτ y vale al menos1/(80π), usando Q²≥1/2. H≥G/2 garantiza que existe en todo el rango donde se usa. La desigualdad2π/e²<1 permite restar la cola baja a los más de2B conservados y todavía dejar más de B, con B>exp(−D). No se contó dos veces la misma reserva.

**Precisión de extremos en el conteo unitario.** Para contar ceros en[j,j+1), el cociente N(j+1)−N(j) podría omitir un cero situado exactamente en j. No hace falta suponer ausencia de tales ceros. Para j≥3 usar N(j+1)−N(j−1), que incluye el intervalo completo con multiplicidades. Si M(t)=t/(2π)log(t/(2πe))+7/8 y E(t)=0.137logt+0.443loglogt+1.588, Z3 da

`N(j+1)−N(j−1) ≤ log(j+1)/π + 2E(j+1) < 4log(3+j)`.

La última desigualdad sigue de loglog(j+1)≤log(j+1) y log(3+j)≥log6. La constante100 usada en el puente conserva un margen amplio. Las alturas pequeñas se cubren por Z1, y las negativas por conjugación. Esta precisión evita una hipótesis tácita sobre alturas enteras sin alterar ningún control numérico.

Para el agrupamiento de colas, a lo sumo cuatro intervalos unitarios cubren l≤|τ−γ|<l+1. La desigualdad log(3+|j|)≤log(3+|τ|)+log(3+l) sigue aun admitiendo el desplazamiento adicional de los extremos, pues (3+|τ|)(3+l)≥5+|τ|+l. Las sumas acotadas en el puente dan un coste≤4·10⁷[2log(3+|τ|)+2log3+3], menor que10⁹log(3+|τ|). El factor2.718⁻ᴺ puede extraerse uniformemente en la región baja porque sólo corrigen ceros con|γ|>G yG−H>2.718N.

**Dictamen actualizado:** la desigualdad de ventana fija queda **reconstruida correctamente con los anexos de investigación, Z1–Z3 y el certificado ejecutado**, sujeto a las convenciones y al cierre del dominio ya auditados para paper46. No debe reformularse como «paper46 contiene por sí solo toda esta demostración»: sus líneas1914–1930 reportan el resultado sin desarrollar este puente. La precisión de conteo de extremos arriba es una reparación explícita de la exposición, no un cambio de hipótesis ni de parámetros.

Complemento bibliográfico de Z1 comunicado por el agente de spanning: [documentación histórica Arb2.23 de acb_dirichlet](https://arblib.org/acb_dirichlet.html) especifica que N(t) cuenta multiplicidades; es una fuente primaria adicional a la documentación FLINT actual.
