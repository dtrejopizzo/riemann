# POWER_SIGNED_MEAN_019 — Media firmada de dilataciones e inversión truncada que pierde positividad

Estado: PROVED signo de una media aritmética de dilataciones para todos N y falsificador explícito de positividad de su inversión truncada. OPEN la media original ERR. No se modifica ningún paper.

## 1. Corpus y razón nueva, con límite declarado

Leídos las reglas del proyecto, LOW_TABLE018, TATE_CHAIN009 y PACKET_SCOPE009; índice ROUTES-TRIED-INDEX (INV_H/K, Euler/Möbius N_018, PROOF_L_SHARP_F/J y sus correcciones), grid parte3 y CROSSWORD-TO-D (Euler–Maclaurin y clases piso). Las identidades Λ*1=log, su inversión Möbius y las reformulaciones con factoriales ya pertenecen a esas rutas. NO se presentan como herramientas nuevas por cambiarles el nombre.

La diferencia acotada es aplicar ese agrupamiento al kernel POSITIVO exacto de ERR018 y probar qué signo conserva realmente: la media de TODAS las dilataciones tiene signo negativo elemental. Al intentar recuperar la media original, una hipótesis natural de positividad del peso inverso falla ya en los primeros tres dilatados del MISMO kernel gamma, con N explícito grande. El resultado no es un NO-GO para medios firmados ni una prueba de la fila original.

## 2. Media original y kernel

Se conservan u=63/2, g_N=y^(N−1)e^-uy/(N−1)!, C_N=c_gN, c0=C_N(0), y

    E0(x)=psi_Lambda(x)−x+1, x>=1,
    H_N(x)=−(d/dx)[x^-1/2 C_N(logx)]/c0
          =x^-3/2[(1/2)rho_N(logx)−rho_N'(logx)]>0,
    rho_N=C_N/c0.

LOW018 prueba

    F_N=2∫_1^infinito H_N(x)E0(x)dx,
    W[g_N]/c0=Arch_sharp[g_N]/c0−F_N.                  (ERR)

El endpoint E0(1)=0 se conserva. Este es el residuo original, cuyo signo no se presume.

## 3. Agrupamiento por enteros: signo exacto antes de invertir

Para x>=1 y n=floorx, la identidad de divisores da

    Σ(m<=x)psi_Lambda(x/m)
       =Σ(q<=x)Lambda(q)floor(x/q)=log(n!).

Por tanto

    B(x):=Σ(m<=x)E0(x/m)=log(n!)−xH_n+n,               (B)
    H_n=Σ(j=1..n)1/j.

Este B es negativo para TODO x>1. En enteros,

    B(n+1)−B(n)=log(n+1)−H_n<0,

porque H_n>∫_1^(n+1)dt/t. Entre enteros su pendiente es−H_n. Más precisamente,

    B(x)<=−(1−log2)(x−1).                              (NEG)

Para verlo, H_n−log(n+1) crece desde1−log2, pues sus diferencias son1/(n+1)−log(1+1/(n+1))>0. Las pendientes entre enteros satisfacen la misma comparación. Ésta es una desigualdad elemental sobre el agrupamiento real en los enteros, no una consecuencia de tomar valores absolutos del error Chebyshev.

Integrar contra H_N>0 prueba el signo de una media FIRMADA infinita:

    A_N:=2∫_1^infinito H_N(x)Σ(m<=x)E0(x/m)dx
       <=−2(1−log2)J_N(1/2)<0, para TODO N>=2,          (MEAN)

donde J_N(b)=∫_0^infinito e^(bt)rho_N(t)dt. Se usó ∫H_N(x)(x−1)dx=∫x^-1/2 C_N(logx)dx/c0=J_N(1/2), por integración por partes. Todas las sumas e integrales convergen absolutamente para cada N: H_N decae como x^-33 por polinomio en logx.

MEAN es un resultado de signo sobre una media concreta de dilataciones. NO es el signo de F_N: aparecen todos E0(x/m), no solo m=1. No se omite esa diferencia de portador.

## 4. Qué hipótesis adicional exigiría la inversión

La inversión adjunta correcta, incluido su jacobiano, es

    h_N(x)=Σ(m>=1)mu(m)m H_N(mx), x>=1.                (INV)

No basta Σmu(m)H_N(mx): falta el factor m. La serie converge absolutamente para cada N, pues su término es O_N(m^-32 por polinomio en logm). Su inversión cumple Σ(d>=1)d h_N(dy)=H_N(y), y Fubini da exactamente

    F_N=2∫_1^infinito h_N(x)B(x)dx.                    (PAIR)

Si se tuviera h_N>=0, NEG implicaría F_N<=0. Aun eso no bastaría por sí solo para W>=0: habría que alcanzar también el déficit negativo de Arch_sharp. Pero la premisa de positividad inversa no es automática y la siguiente prueba muestra un fallo explícito en su aproximación local más elemental.

## 5. Falsificador en el MISMO kernel gamma: los primeros tres inversos

Para todo N>=2^17 defina

    h_N^[3](1)=H_N(1)−2H_N(2)−3H_N(3).

Entonces

    h_N^[3](1)<−19/256<0.                              (FAIL3)

Prueba sin tablas. La probabilidad espectral de g_N tiene segundo momento M2=u²/(2N−3)<1/128. Para0<=t<=2,

    rho_N(t)>=1−t²M2/2>=1−2M2,
    rho_N'(t)<=0,
    (1/2)rho_N(t)−rho_N'(t)>=1/2−M2>63/128.

Se aplican a log2,log3<2. Además H_N(1)=1/2 y1/sqrt2+1/sqrt3>2/3+1/2=7/6. Por tanto

    h_N^[3](1)
       <1/2−(63/128)(7/6)=−19/256.

No se afirma que h_N COMPLETO sea negativo en1: los términos m>=4 podrían cambiar el signo. FAIL3 refuta exactamente el lema «la inversión por dilataciones preserva positividad en cada prefijo» para los kernels originales, no para un modelo modificado. Tampoco se descarta la posibilidad de controlar el peso inverso firmado completo mediante una desigualdad adicional.

## 6. Variante genuina que falta y por qué la identidad anterior no la prueba

La información que pierde la recuperación de m=1 es la compensación entre las partes positiva y negativa de h_N en PAIR. Una continuación válida tendría que conservar ese emparejamiento firmado con el MISMO B(x)<0, o comparar de manera unilateral la contribución de m>=2 en MEAN con el término m=1. No puede sustituir h_N por su módulo ni suponer positivos sus prefijos.

Una formulación concreta del requisito, manteniendo un objeto aritmético explícito, es la desigualdad

    2∫ h_N^+(x)[−B(x)]dx
       −2∫ h_N^−(x)[−B(x)]dx
        >=−Arch_sharp[g_N]/c0.                         (SIGNED)

Por PAIR es suficiente y exacta para el signo de esta fila. Aquí SIGNED es una obligación ABIERTA, no un lema demostrado; escribirla no aporta por sí mismo progreso de signo. Una variante constructiva debe producir un bound unilateral para el segundo término que use la relación de divisores y la forma específica de H_N, sin anular la contribución favorable del primero. Las rutas Euler/Möbius/EM citadas ya agotaban la identidad sin tal desigualdad; FAIL3 muestra por qué la propuesta de positividad local no suministra esa hipótesis adicional.

La fila original de todos N sigue sin resolverse. Se conserva como resultado nuevo acotado el signo MEAN para la media de dilataciones y el falsificador FAIL3, junto con la identificación precisa del dato de signo que la inversión no preserva automáticamente.
