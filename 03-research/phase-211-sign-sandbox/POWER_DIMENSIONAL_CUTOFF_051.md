# POWER_DIMENSIONAL_CUTOFF_051 — Corte arquimediano lineal en la dimensión

Estado: **PROVED; auditoría independiente APROBADA en POWER_DIMENSIONAL_AUDIT_051.md y revisión root, incluida la corrección del factor del segundo sector.** Cota efectiva para ARCH sobre TODA Q^j V_n, simultánea en n y j. No es todavía un corte de signo de W. Papers intactos.

## 1. Antecedentes y diferencia precisa

Consultados ROUTES-TRIED-INDEX/README, grid maestro y CROSSWORD-TO-D; releídos HIGHPASS015, CENTERED_CUTOFF049 y STATE050. HIGHPASS015 demuestra una eventualidad uniforme en numeradores para CADA dimensión fija, sin corte efectivo en función de ella. CENTERED_CUTOFF049 da j>=14 en dimensión12. La reducción por sectores Jacobi existe en JOINT_SCALE016 y no se presenta como nueva.

La diferencia es una cota explícita de momento inverso para TODOS n,j y TODOS los numeradores, y de ella un corte LINEAL j>=ceil(7n/6) con un lower arquimediano independiente de n. También se da un corte explícito para cualquier margen arquimediano pedido. No se afirma que el mismo corte controle los otros términos de W.

## 2. Bound general de momento

Fije u=63/2 y Q(s)=s/(s+u). Para n>=1 entero, F!=0 en V_n={P(s)/(s+u)^n:degP<n}, y j>=1 entero, tome la probabilidad espectral normalizada de G=Q^jF. Ponga

    r=u² E_G[tau^-2], d=n-1, t=2j-1.

Entonces

    t r <= 1+2sqrt[d(d+2j)r].                            (GENERAL)

En particular,

    r <= [sqrt(d(d+2j))+sqrt(d(d+2j)+2j-1)]²/(2j-1)².   (ROOT)

Prueba: sobre el círculo z=(i tau-u)/(i tau+u), F es el modo base por un polinomio A(z) de grado<=d. Ponga z=exp(2ix), q=cos²x, y=sin x. Centrar por exp(-idx) deja frecuencias de la misma paridad que d. Para d impar aparecen cos x R(y)+S(y), con R par grado<=d-1 y S impar grado<=d. Para d par aparecen S(y)+cos x R(y), con S par grado<=d y R impar grado<=d-1. Si d=0, el segundo sector se omite. En TODOS los casos los términos cruzados son impares y se anulan en norma y momento.

Los dos sectores tienen pesos (1-y²)^a y grados máximos

    (a,Degree)=(j-1/2,d), (j+1/2,d-1).

La integración por partes y el bound polinómico probado en CENTERED_CUTOFF049§3 dan para cada sector

    2a r_sector <= 1+2sqrt[Degree(Degree+2a+1)r_sector].

El segundo sector tiene 2a mayor y Degree(Degree+2a+1)=(d-1)(d+2j+1)<=d(d+2j): la diferencia entre el último mayorante y ese producto es 2j+1>0. Por ello queda dominado por la misma raíz que el primero. La razón total es una mezcla positiva de las razones sectoriales; todas quedan por debajo de ROOT. Esto prueba GENERAL y ROOT para TODOS los numeradores reales o complejos. Las integraciones son finitas porque j>=1 implica a>0.

## 3. Un corte lineal explícito, con constante racional

Para TODO n>=1 y TODO j>=ceil(7n/6),

    r<49/20,
    E_G[tau^-2]<1/405,
    ARCH[G]/||G||²>859/800.                              (LINEAR)

Prueba: los coeficientes1/(2j-1) y sqrt[d(d+2j)]/(2j-1) de GENERAL normalizada decrecen con j; para el segundo basta derivar(d+2j)/(2j-1)², cuya derivada es negativa para d>=0,j>=1. Cuando d=0, ese coeficiente es cero. Por ello basta verificar en el valor REAL j0=7n/6, aunque j de la órbita sea entero.

Con b=49/20,

    (2j0-1)b-1=(343n-207)/60>0,
    [(2j0-1)b-1]²-4b(n-1)(n-1+2j0)
      =(49n²+10878n+7569)/3600>0.

La raíz positiva de la cuadrática en sqrt r queda por debajo de sqrt b. GENERAL da r<b para todos los j indicados. Dividir por u²=3969/4 da E tau^-2<1/405. La misma prueba de Jensen/digamma de CENTERED_CUTOFF049§6, que sólo usa ese momento, da ARCH>859/800. No depende de la dimensión. Para n=12 el corte recupera exactamente j>=14.

## 4. Corte para cualquier momento o margen arquimediano

Para cualquier b>0 defina

    T(n,b)=1/2+[(2n-1)+2sqrt((1+b)n(n-1))]/(2b),
    J(n,b)=floor(T(n,b))+1.

Entonces para TODOS j>=J(n,b), GENERAL implica r<b. En efecto, poner t=2j-1 y exigir que b esté por encima de ROOT equivale a

    bt-1>0,
    b²t²-2b(2n-1)t+1-4bn(n-1)>0.

La raíz mayor de esta última cuadrática es[(2n-1)+2sqrt((1+b)n(n-1))]/b; la definición de J la supera estrictamente. Este corte es O_b(n), y es explícito, sin una constante de convergencia escondida.

En consecuencia,

    ARCH[G]/||G||²
      > log[u/(2pi sqrt b)]-sqrt b/u-b/(2u²).            (ARCH-b)

Para un margen h>=0 prescrito puede elegirse, por ejemplo,

    b_h=(u²/64)exp[-2(h+1)].

Entonces j>=J(n,b_h) garantiza ARCH[G]>h||G||²: el logaritmo de ARCH-b es mayor que h+1 porque2pi<8, mientras los dos errores suman menos que1/8+1/128<1. Se obtiene así un corte lineal explícito para cualquier margen arquimediano fijo.

## 5. Qué no proporciona como inducción desde050

El resultado050 aporta el bloque completo de doce polos y un espacio restringido de trece polos con numerador cero. LINEAR no certifica los índices j<ceil(7n/6) de una dimensión nueva y no ordena la forma COMPLETA al cambiar n. FULLTEL transporta en una dimensión n a partir de un bloque base V_n ya positivo y ganancias restringidas de dimensión n+1; no crea la positividad de V_(n+1) desde V_n.

Por eso no se obtiene de050 una recurrencia de signo en n con los datos aquí probados. Faltan tanto el segmento inicial de cada dimensión como el control conjunto del polar y TODOS los contactos en la cola. En particular, la traza ponderada010 usada para pagar los contactos en050 aumenta con la dimensión; un lower constante de ARCH no paga automáticamente ese coste. El bound polar específico de dimensión12 tampoco se declara uniforme en n. HIGHPASS015 conserva su eventualidad completa a cada dimensión fija, pero LINEAR es por ahora un corte efectivo de ARCH, no de W.

La tabla completa y el signo global siguen OPEN. No se certifica una nueva ventana T ni se edita ningún paper.
