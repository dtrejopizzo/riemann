# AUDIT_016 — Rango denso del mapa011

2026-10-19. Revisor hostil independiente. **PASA / PROVED.** Revisión de
`LINK_016_DENSE_RANGE.md` contra LINK011, CONSTRUCTOR015, AUDIT015, las
entradas correspondientes del índice, el grid y el crucigrama actual.
Sin numérica nueva, sin modificación de papers y sin nueva ruta de signo.

## 1. Anulador y normalizaciones

La cota de011 da `|η_d|≤C||h||d^(-1/4)` en α=1/4. Por tanto
`c=Ση_d/d` converge absolutamente y la función b_h está bien definida y
es holomorfa en `|Im z|<π/4`, por convergencia uniforme de las series
gaussianas en compactos. La ortogonalidad al origen par polar libre fuerza
que su parte par sea λcosh(x/2); la continuación analítica extiende esta
identidad desde cualquier ventana T>0 a todo el eje real.

La convención de006 es `τ=θ−1`, con ambos signos de los enteros. Así la
distribución μ de016 satisface exactamente
`Θ_μ(y)=Ση_dτ(d²y)−cτ(y)`. No falta un factor2. La identidad par implica

`Θ_μ(y)+y^(-1/2)Θ_μ(1/y)=(λ/2)(1+y^(-1/2))`.

En consecuencia `μ′=μ−(λ/2)δ_0` es la corrección correcta. Sus coeficientes
tienen crecimiento polinomial y μ′ es una distribución temperada par.

## 2. Inyectividad gaussiana y periodicidad

El Lema2 es válido en S′. Derivar las gaussianas en y=1 en la topología
de Schwartz entrega los momentos pares; la paridad anula los impares.
La función `G(z)=⟨ν,exp(−πx²+zx)⟩` es entera porque todos los seminormas
de Schwartz de sus derivadas están uniformemente controlados en compactos
de z. Sus coeficientes de Taylor nulos dan G=0.

En el eje imaginario, la identidad con la transformada de Fourier de
`exp(−πx²)ν` se justifica por dualidad en Schwartz; esa transformada es una
función suave de crecimiento polinomial. La normalización de frecuencia
para z=it es −t/(2π), sin efecto sobre la anulación. La inyectividad de
Fourier da `exp(−πx²)ν=0`. Multiplicar tests compactos por exp(πx²)
recupera ν=0 localmente y, por densidad de los tests compactos en Schwartz,
también como distribución temperada. No hace falta una cita de completitud
de Hermite.

La transformada exacta de la gaussiana da
`Θ_(𝓕ν)(y)=y^(-1/2)Θ_ν(1/y)`. Aplicar el lema a μ′+𝓕μ′, que es par,
prueba `𝓕μ′=−μ′`. Puesto que μ′ es suma de deltas puras en enteros,
su Fourier es1-periódica; luego μ′ también. Comparar las masas obliga a
coeficientes constantes, incluida la masa en0. En y=1, la identidad
antisimétrica anula esa constante porque θ(1)>0. Resultan μ′=0, λ=0,
c=0 y, por inducción sobre divisores, η_d=0 para todo d≥2. La densidad
del span de f_d en la definición de H concluye h=0. La prueba no clasifica
distribuciones con derivadas de deltas, que no aparecen aquí.

## 3. Core y alcance

El core par suave de momento polar nulo es denso en el subespacio L²
correspondiente: aproximación suave par y corrección del momento con un
test fijo. La acotación de U_T transporta esa aproximación. Se obtiene
rango denso para cada T>0 también desde ese core.

Una forma hermítica continua en H positiva sobre esa imagen es positiva
en todo H por continuidad. Por015, la consecuencia para el span real de
las tres piezas es exactamente el ortante no negativo. Combinada con014,
la exclusión se refiere a combinaciones fijas no nulas y al mismo mapa011;
no se extiende a coeficientes dependientes de T.

La densidad no implica inyectividad, sobreyectividad ni inversa acotada
de U_T. Tampoco implica densidad de la imagen de un bloque finito: tal
imagen es finito-dimensional y cerrada. No identifica V con todo el
ambiente gaussiano, no controla otros mapas ni formas discontinuas y no
produce igualdad, dominación ni signo de Q_T. La fila D no cambia de estado.

## Nota editorial independiente: archivo06

Las correcciones de [margin] y R6 en
`05-meta-and-planning/ROUTES-TRIED-INDEX/06_OPEN_RESIDUES_DEAD_SUBROUTES.md`
coinciden con P47 cor:margin1 y rem:moriceiling: el techo probado para λ_A
es `4·10^9 T exp(−15.449T)`, T≥1. El techo doblemente exponencial de Mori
se registra como citado y no verificado, y corresponde a λ_W. La relación
λ_W≤λ_A no lo transfiere a λ_A. De
`L(T)(1−o(1))≤λ_A(T)≤4·10^9 T exp(−15.449T)`, con L>0, sí se deduce
`L(T)≤(1+o(1))4·10^9 T exp(−15.449T)`. **Sin fallos detectados.**
