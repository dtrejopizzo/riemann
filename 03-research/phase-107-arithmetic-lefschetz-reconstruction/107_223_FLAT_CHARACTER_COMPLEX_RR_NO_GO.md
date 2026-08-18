# 107.223 -- Flat character complexes cannot be the divisor RR complexes

## 1. Universal Euler cancellation

Let \(M\) be any invertible module over a Dedekind domain \(O\), and let

\[
 C_M(a,b):
 0\to M\xrightarrow{(-b,a)}M^2
 \xrightarrow{(a,b)}M\to0.
 \tag{1.1}
\]

In \(K_0(O)\), independently of \(a,b\),

\[
 \chi(C_M)=[M]-2[M]+[M]=0.
 \tag{1.2}
\]

If \((a,b)\ne(0,0)\), the cohomology calculation of 107_217 gives

\[
 H^0=M/IM,qquad
 H^1=I^{-1}M/M,qquad H^2=0.
\]

At every finite prime \(\mathfrak p\),

\[
 \operatorname{length}_{\mathfrak p}H^0
 =\operatorname{length}_{\mathfrak p}H^1
 =v_{\mathfrak p}(I),
 \tag{1.3}
\]

so the numerical Euler characteristic also vanishes place by place.  For
the trivial character the free ranks are \((1,2,1)\), again giving zero.

The cancellation remains true for the codifferent twist
\(M=\mathfrak D^{-1}\) and for every finite direct sum in 107_219.

## 2. Conflict with the published divisor RR

For an archimedean divisor \(D=a\{\infty\}\) with
\(n=\lfloor e^a\rfloor\ge1\), Connes--Consani prove

\[
 \dim_{\mathbb S[\pm1]}H^0(D)
 =\left\lceil\log_3(2n+1)\right\rceil.
 \tag{2.1}
\]

For \(a\ge0\), their \(H^1(D)\) has dimension zero.  Hence the Euler
characteristic takes the positive values

\[
 \chi(D)=1,2,3,4
 \quad\text{at}\quad n=1,4,13,40.
 \tag{2.2}
\]

### Theorem 2.1 (ordinary flat-Euler no-go)

No assignment of every Connes--Consani divisor module \(O(D)\) to a
finite direct sum of the flat character complexes
\(C_M(a,b)\), equipped only with ordinary rank/length Euler
characteristic, can preserve the Riemann--Roch Euler characteristic.

The contradiction is already \(0=\chi(C_M)\ne\chi(D)\) for any of the
controls in (2.2).  It is independent of the chosen cyclotomic level,
codifferent twist, and tolerance presentation.

## 3. Geometric meaning

The result does not invalidate the middle torsion or duality of
107_217--107_222.  It identifies their correct scope: they are flat
local-system cohomology.  A divisor line bundle with nonzero degree needs
a nonflat differential or transition cocycle carrying a first Chern
class, or a divisor-dependent bounded/tolerance structure whose integer
dimension is not the ordinary rank/length Euler characteristic.  On a
surface, one of these missing data must produce the quadratic
RR/intersection term.

Therefore the next row-(a) object cannot be obtained by changing only
the character labels while retaining ordinary homological size.  It must
introduce divisor-dependent curvature, boundary maps, mass bounds, or
tolerance relations, while reducing to the flat complexes on degree-zero
character sectors.

## 4. Falsifier

`107_223_flat_character_complex_rr_no_go.sage` recomputes the mixed
cyclotomic homology, checks prime-by-prime equality of the torsion
lengths, checks the trivial free ranks, and compares their zero Euler
characteristic with the exact published dimensions at the four fixed
archimedean divisors.  A mutated nonflat complex is included as a
negative control and must be capable of producing nonzero Euler
characteristic.
