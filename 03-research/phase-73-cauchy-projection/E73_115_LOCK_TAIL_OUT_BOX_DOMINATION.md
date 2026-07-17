# E73.115 - Box Domination for LOCK/TAIL/OUT

Date: 2026-07-12.

This note converts the remaining center-only parts of E73.114 into a
finite box theorem.  The goal is to avoid more point experiments: after
E73.112/E73.113, `MAIN` is already a box certificate.  The missing pieces
are `LOCK`, `TAIL`, and `OUT`.

## 1. Box and row notation

Fix a box

```text
B=[alpha0,alpha1] x [tau0,tau1],
0<alpha0<=alpha<=alpha1,
tau0<=tau<=tau1.
```

For a critical row `gamma_k`, define the Hermite-Mellin weight

```text
W_k(alpha,tau;L)
 =
 exp(alpha L)
 |G_{alpha+i tau,m}(i gamma_k)|
 |1-exp(i gamma_k L)|.
```

Let `R_k` be the finite Cauchy divisor separation

```text
R_k = dist(-gamma_k, Div(P_x)).
```

E73.110 gives an analytic derivative enclosure

```text
W_k(alpha,tau;L) <= W_k^+(B,L)
```

for all `(alpha,tau) in B`.  Therefore

```text
F_k(alpha,tau;L) := W_k(alpha,tau;L) R_k
                 <= F_k^+(B,L) := W_k^+(B,L) R_k.
```

Let `P_3(B,L)` be the possible top-three set of E73.112:

```text
P_3(B,L)
 =
 { k : fewer than three rows have F_j^-(B,L)>F_k^+(B,L) }.
```

Then for every point of the box, the true `FAR3` rows are contained in
`P_3(B,L)`.

Define the top-three far budget

```text
S_FAR^+(B,L)
 =
 sum of the three largest F_k^+(B,L), k in P_3(B,L).
```

This is the correct box replacement for the center quantity

```text
s_far = sum_{k in FAR3(alpha,tau)} F_k(alpha,tau;L).
```

Thus, uniformly on `B`,

```text
s_far(alpha,tau) <= S_FAR^+(B,L).              (1)
```

## 2. LOCK box domination

The center lock budget in E73.100 is

```text
LOCK(alpha,tau)
 =
 4 (1+exp(alpha L))/alpha
 s_far(alpha,tau)
 N_LC(tau),
```

where

```text
N_LC(tau)=N_lock(tau)+N_comp(tau)
```

is the finite local-lock/complement sum from E73.090.

The alpha factor is elementary.  Set

```text
A_LOCK^+(B,L)
 =
 max_{alpha in [alpha0,alpha1]}
 4 (1+exp(alpha L))/alpha.
```

Since the function is explicit and one-dimensional, the maximum is either
at an endpoint or at the unique critical point, if it lies in the interval.
For the Phase 73 boxes used so far it is attained at `alpha1`, but the
certificate should check both endpoints plus the critical point.

For the tau factor define the finite interval envelope

```text
N_LC^+(B)
 =
sup_{tau in [tau0,tau1]} N_LC(tau).
```

There are two ways to certify this supremum.  The sharper one is exact:
`N_LC(tau)` only changes when the set `local_window(tau,nwin)` changes.
Since `local_window` is the set of the `nwin` closest ordinates among the
finite list `GAMMAS[:ncrit]`, it is constant on the cells cut out by the
midpoints

```text
(gamma_j+gamma_{j+1})/2.
```

Thus `N_LC^+(B)` is obtained by evaluating `N_LC` once on every cell
intersecting `[tau0,tau1]`, plus the endpoints.  No smooth derivative
bound is needed for this local-window factor.

Hence

```text
LOCK(alpha,tau)
 <= A_LOCK^+(B,L) S_FAR^+(B,L) N_LC^+(B).      (LOCK-BOX)
```

The finite condition replacing the center test is

```text
A_LOCK^+(B,L) S_FAR^+(B,L) N_LC^+(B) <= L^-5.
```

## 3. TAIL box domination

The center tail budget in E73.100 is

```text
TAIL(alpha,tau)
 =
 s_far(alpha,tau)
 exp(alpha L) L^2/M^2
 G_loc(tau),
```

where `M=M(L)` is the active cutoff and `G_loc` is the finite local Green
sum from E73.093.

Define

```text
A_TAIL^+(B,L)=exp(alpha1 L) L^2/M^2,
G_loc^+(B)=sup_{tau in [tau0,tau1]} G_loc(tau).
```

Again the sharper certification is exact by local-window enumeration:
`G_loc(tau)` is constant on the same nearest-zero cells, because each row
contribution depends on `gamma`, `L`, `d`, and `xi`, not continuously on
`tau` except through the discrete choice of the local window.  Together
with (1),

```text
TAIL(alpha,tau)
 <= S_FAR^+(B,L) A_TAIL^+(B,L) G_loc^+(B).     (TAIL-BOX)
```

The finite condition is

```text
S_FAR^+(B,L) A_TAIL^+(B,L) G_loc^+(B) <= L^-5.
```

## 4. OUT box domination

The finite `OUT-FAR` term is the complement outside the three dominant
far rows:

```text
OUT(alpha,tau)
 =
 sum_{k notin FAR3(alpha,tau)} O_k(alpha,tau),
```

where `O_k` is the finite row contribution from E73.095.

For a box, use row enclosures

```text
O_k(alpha,tau) <= O_k^+(B,L).
```

The only selection issue is that the excluded three rows vary with the
point.  Use the interval FAR order to enumerate all triples that can be the
top-three set.

```text
T_3(B,L)
 =
 { S subset P_3(B,L), |S|=3 :
   S is compatible with the FAR interval order }.
```

The elementary compatibility test used in E73.116 is:

```text
max_{j notin S} F_j^-(B,L) <= min_{k in S} F_k^+(B,L).
```

This is only a necessary condition, hence it may leave extra triples, but
it cannot remove the true triple.  Therefore a safe upper bound is

```text
OUT^+(B,L)
 =
 max_{S in T_3(B,L)}
 sum_{k notin S} O_k^+(B,L).
```

If `T_3(B,L)` has one element, this is simply the row-wise upper sum over
the complement of the certified top-three rows.  If `T_3(B,L)` has more
than one element, the maximum encodes the finite ambiguity.  Subdividing
the box is legitimate and often removes this ambiguity.

The finite condition is

```text
OUT^+(B,L) <= L^-9.                            (OUT-BOX)
```

## 5. Box GATE-73 theorem

For every admissible box `B`, suppose the following four finite inequalities
hold:

```text
MAIN^+(B,L) <= 1,
LOCK^+(B,L) <= L^-5,
TAIL^+(B,L) <= L^-5,
OUT^+(B,L)  <= L^-9.
```

Here `MAIN^+` is the possible-set certificate of E73.112, and the other
three quantities are defined in Sections 2--4.

Then for every `(alpha,tau) in B`,

```text
GATE-73(alpha,tau,L)
```

holds with the same exponents as E73.099.  Consequently, by the proof of
E73.099,

```text
scalar WRL holds at scale L on the whole box B.
```

## 6. What remains to compute

This note removes the conceptual gap in E73.114.  The remaining work is
finite and explicit:

```text
1. implement N_LC^+(B) by exact nearest-zero cell enumeration;
2. implement G_loc^+(B) by the same enumeration;
3. implement O_k^+(B,L), O_k^-(B,L);
4. verify LOCK-BOX, TAIL-BOX, OUT-BOX on the wide Phase 73 boxes.
```

No new positivity principle is being assumed here.  The only analytic
input is the mean-value/derivative enclosure already isolated in E73.110,
applied to the three remaining finite rational sums.
