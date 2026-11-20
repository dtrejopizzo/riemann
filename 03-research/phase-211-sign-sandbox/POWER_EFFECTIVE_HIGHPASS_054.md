# POWER_EFFECTIVE_HIGHPASS_054 — Corte explícito de dimensión variable para la forma completa

Estado: PROVED, revisión independiente aprobada en POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md. No requiere evaluar el entero gigantesco del corte. Papers intactos.

## 1. Enunciado y diferencia

Fijar u=63/2 y Q(s)=s/(s+u). Para cada entero n≥1 definir los enteros explícitos

    C_n=9n²9^n,
    D_n=10C_n n!,
    A_n=6C_n n n!,
    K(n)=max{10000n², A_n·3^(4D_n+20)}.

Para TODO polinomio real no nulo P de grado<n, F0=P/(s+u)^n y TODO entero j≥K(n), se demuestra

    W[Q^jF0] > ||Q^jF0||².                              (EFFECTIVE)

El corte crece muy deprisa; no se afirma que sea polinómico ni se optimiza. El nuevo dato es que está dado por operaciones enteras explícitas y cubre TODOS los numeradores simultáneamente a dimensión variable.015 ya probó eventualidad a dimensión fija sin este corte. El presente argumento evita un límite no efectivo de Gram: usa INVERSE_COEFFICIENT054, una cota uniforme explícita en frecuencia inversa, y el contorno ESCALAR auditado017 aplicado a diagonales positivas. No separa dos normas exponenciales de dimensión n ni contradice la obstrucción016.

Se consultaron el índice ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D y los antecedentes descritos en INVERSE_COEFFICIENT054. No se presenta como nuevo el método de contorno017, el bound del símbolo de017 ni la eventualidad015. El cambio de objeto y la nueva desigualdad efectiva son COEFF054 y su integración con los momentos exactos de este memo.

## 2. Momentos explícitos de frecuencia inversa

Para j≥n, poner a=u√j, R(y)=y^(n−1)P(ia/y),

    w(y)=(1+y²/j)^−(n+j),
    H=∫|R(y)|²w(y)dy,
    M_r=∫y^(2r)w(y)dy.

INVERSE_COEFFICIENT054 prueba

    ||Q^jF0||²=a^(1−2n)H/(2π),
    (Σ|coef R|)²≤C_nH.                                 (COEFF)

Para enteros0≤r≤n−1, se tiene la cota efectiva

    M_r≤Γ(r+1/2),   Σ_(r=0)^(n−1)M_r≤2n!.              (MOMENTS)

Prueba. La integral beta exacta es

    M_r=j^(r+1/2)Γ(r+1/2)Γ(b)/Γ(b+r+1/2),
    b=n+j−r−1/2.

Para r≥1, h=r+1/2≥1. Si T tiene densidad Gamma de parámetro b, Jensen da Γ(b+h)/Γ(b)=E[T^h]≥b^h. Como b≥j+1/2 para r≤n−1, resulta M_r≤Γ(r+1/2). No se aplica Jensen con potencia cóncava.

Para r=0 se necesita otra dirección: Cauchy sobre las integrales gamma da

    Γ(x+1)²≤Γ(x+1/2)Γ(x+3/2)=(x+1/2)Γ(x+1/2)².

Así Γ(x+1/2)/Γ(x)≥x/√(x+1/2)≥√(x−1/2). Tomar x=n+j−1/2: la razón Γ(n+j)/Γ(n+j−1/2) es al menos√(n+j−1)≥√j, lo que prueba M_0≤√π.

Finalmente Γ(r+1/2)=√π(2r)!/(4^r r!)<2r!, porque binom(2r,r)≤4^r y√π<2. Sumar r!≤(n−1)! sobre n términos da MOMENTS.

Para el momento adicional r=n, necesario más adelante, su parámetro b es j−1/2, que es MENOR que j. No se hereda la cota anterior. Si j≥10000n², Jensen con h=n+1/2 da

    M_n≤Γ(n+1/2)[j/(j−1/2)]^(n+1/2).

El logaritmo del factor está acotado por(n+1/2)/(2j−1)<1/100. Por exp(1/100)≤100/99<3 se obtiene

    Σ_(r=1)^n M_r ≤3Σ_(r=1)^nΓ(r+1/2) <6n n!.         (EXTRA)

El caso n=1 está incluido: sólo usa la rama r0 y el factor explícito de r=n.

## 3. Extremo escalar N'=1 en el contorno

QUADRATIC_EXPLICIT017 prueba para u=63/2, N'≥2 y k'≥10000N'² que la densidad escalar

    ρ_(N',k')(z)=z^(2k')/(u²+z²)^(N'+k')

satisface ∫|ρ(x+15i)|dx≤5∫ρ(x)dx. Se necesita justificar separadamente N'=1.

INTERIOR017§2 prueba para H_k(s)=s^k/(s+u)^(k+1), TODOS k≥0,

    ||exp(15t)h_k||²≤11||h_k||².

Para dejar visible su contenido elemental: si a0=u−15=33/2, b0=15 y c_k=binom(2k,k)/4^k, Plancherel y la expansión binomial dan

    N_k(15)=(1/(2a0))Σ_(l=0)^k c_(k−l)c_l(b0²/a0²)^l,
    N_k(0)=c_k/(2u).

Vandermonde da c_(k−l)c_l≤c_k, luego N_k(15)/N_k(0)≤u a0/(a0²−b0²)=11. La norma con peso exp(−15t) es menor que la norma sin peso, por causalidad.

En z=x+15i, ρ_(1,k)(z)=H_k(−15+ix)H_k(15−ix). Cauchy y Plancherel producen

    ∫|ρ_(1,k)(x+15i)|dx
      ≤2π||exp(15t)h_k||||exp(−15t)h_k||
      ≤√11∫ρ_(1,k)(x)dx <4∫ρ_(1,k)(x)dx.

Por tanto el bound5 es válido también para N'=1. Esta separación de normas se usa SÓLO para el extremo escalar de dimensión1, donde hay un bound ya probado uniforme en k; no se aplica a los numeradores generales de dimensión n.

## 4. Contorno completo: producto polinómico y norma exacta

Para P real, la densidad completa es

    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j)
        =(−1)^(n−1)a^(−2n+2)
          z^(2(j+n−1))R(a/z)R(−a/z)/(u²+z²)^(n+j).

El signo es esencial para la identidad; en la recta real R(y)R(−y)=(−1)^(n−1)|R(y)|². Para el módulo complejo, COEFF da

    |R(Y)R(−Y)|≤C_nH max(1,|Y|^(2n−2))
                  ≤C_nHΣ_(r=0)^(n−1)|Y|^(2r).

Para j≥10000n², cada término restante es una densidad escalar con

    N'=r+1, k'=j+n−1−r, N'+k'=n+j.

Se tiene k'≥j≥10000N'². Aplicar el contorno5 de017 y el extremo de§3, y conservar todos los factores de escala, da

    ∫|ρ(x+15i)|dx
      ≤5C_nH a^(−2n+2)Σ_r a^(2r)∫ρ_(r+1,j+n−1−r)(x)dx.

El mismo cambio x=a/y demuestra EXACTAMENTE

    ∫ρ_(r+1,j+n−1−r)(x)dx=a^(−2r−1)M_r.

Así las potencias de a se cancelan antes de normalizar. Como ∫ρ(x)dx=a^(1−2n)H, MOMENTS prueba

    ∫|ρ(x+15i)|dx / ∫ρ(x)dx
        ≤5C_nΣ_rM_r ≤10C_n n!=D_n.                    (STRIP)

STRIP es uniforme en TODOS P y TODOS j≥10000n². La constante depende de n; no se confunde con una norma temporal uniforme independiente de n, refutada en016.

## 5. Todo el peine aritmético, con cola sumable

ρ es racional, analítica en |Imz|<u, y decae al menos como|z|^−2 en cada franja cerrada. Desplazar el contorno hasta Imz=15, con los bordes verticales tendiendo a cero, da para t≥0

    |c_(Q^jF0)(t)| ≤D_n exp(−15t)||Q^jF0||².

No se usa un supuesto símbolo puntual del peine infinito. Con Λ(q)≤q y sumando TODOS los enteros q≥2,

    |Comb|/||Q^jF0||²
      ≤2D_nΣ_(q≥2)Λ(q)q^(−31/2)
      ≤2D_nΣ_(q≥2)q^−14
      ≤2D_n·2^−14(1+2/13)<D_n.                         (COMB)

La serie converge absolutamente y conserva todos los contactos, incluidos primos y potencias primas. La pérdida al sustituir Λ por q se paga con el corte posterior; no se atribuye un signo favorable a ningún átomo.

## 6. Momento inverso y ARCH con corte explícito

Sobre la recta real, COEFF implica |R(y)|²≤C_nHΣ_(r=0)^(n−1)y^(2r). Multiplicar por y²w y usar EXTRA da

    E_(Q^jF0)[τ^−2]
      =(1/(u²j)) ∫y²|R(y)|²w/H
      ≤A_n/(u²j),    A_n=6C_n n n!.                    (INVERSE)

Si j≥K(n), entonces

    E[τ^−2]≤u^−2 3^(−4D_n−20).

El bound elemental del símbolo de017 es

    m(τ)≥log(|τ|/(2π))−1/|τ|−1/(2τ²).

Jensen para log y Cauchy producen

    ARCH/||Q^jF0||²
      ≥−(1/2)log Eτ^−2−log(2π)−√(Eτ^−2)−Eτ^−2/2
      ≥log(u/(2π))+(2D_n+10)log3−1/u−1/(2u²)
      >2D_n+9.                                        (ARCH)

Aquí u>2π, log3>1 y1/u+1/(2u²)<1. Todas son desigualdades elementales; no se evalúa K(n), cuyo exponente es un entero explícito.

## 7. Polar completo

A partir de COEFF y evaluando R en±2ia, se obtiene

    |P(1/2)P(−1/2)|≤C_nH.

En efecto la potencia(2a)^(2n−2) del bound de R se cancela exactamente con el prefactor de P, y2a>1. Así

    |Polar[Q^jF0]|/||Q^jF0||²
      ≤(4π/u)C_n[u²/(u²−1/4)]^n j^(n−1/2)3968^−j
      <C_n exp(n)j^n3968^−j.                           (POLAR-RAW)

Para j≥10000n² esta última expresión es menor que1: logC_n<6n (usar log9<3 y logn≤n−1), logj≤√j, n√j≤j/100 y7n≤7j/10000. Como log3968>1, el logaritmo del majorante es menor que

    7n+n logj−j ≤7j/10000+j/100−j<0.

También4π/u<1 y u²/(u²−1/4)<exp1, que justifican POLAR-RAW sin descartar su signo. Por tanto

    |Polar|<||Q^jF0||².                                 (POLAR)

## 8. Conclusión y alcance

ARCH, COMB y POLAR se refieren a la MISMA función y misma norma. Sumarlos con las orientaciones adversas da

    W[Q^jF0]/||Q^jF0||² > (2D_n+9)−D_n−1=D_n+8>1,

demostrando EFFECTIVE. No se omite ningún término cruzado del numerador: todos quedaron incluidos en el producto R(Y)R(−Y) y en COEFF antes de las cotas diagonales.

Se obtuvo un corte explícito de dimensión variable para TODA la órbita racional, aunque su tamaño es enorme. Esto no prueba los índices j<K(n), no demuestra positividad de la tabla completa y no determina una nueva ventana temporal T. La novedad efectiva no sustituye las obligaciones aritméticas interiores aún pendientes. Papers intactos.
