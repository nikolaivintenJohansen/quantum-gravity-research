(* T3 independent symbolic weak-field and linearized-Bianchi checks. *)

ClearAll[gNewton, rho, c, laplacianPhi, r, mass];
poisson = First@Solve[2 laplacianPhi/c^2 == 8 Pi gNewton rho/c^2, laplacianPhi];
phi = -gNewton mass/r;
flux = FullSimplify[4 Pi r^2 D[phi, r], Assumptions -> {gNewton > 0, mass > 0, r > 0}];

eta = DiagonalMatrix[{-1, 1, 1, 1}];
kCov = Array[k, 4];
kCon = eta . kCov;
hCov = Table[h[Min[mu, nu], Max[mu, nu]], {mu, 4}, {nu, 4}];
hMixed = eta . hCov;
hCon = eta . hCov . eta;
hTrace = Tr[eta . hCov];
kSquared = kCov . eta . kCov;
kkh = kCov . hCon . kCov;
einstein = Table[
  1/2 (
    -Sum[kCov[[sigma]] kCov[[nu]] hMixed[[sigma, mu]], {sigma, 4}]
    -Sum[kCov[[sigma]] kCov[[mu]] hMixed[[sigma, nu]], {sigma, 4}]
    +kSquared hCov[[mu, nu]]
    +kCov[[mu]] kCov[[nu]] hTrace
    -eta[[mu, nu]] (-kkh + kSquared hTrace)
  ),
  {mu, 4}, {nu, 4}
];
bianchi = FullSimplify[Table[Sum[kCon[[mu]] einstein[[mu, nu]], {mu, 4}], {nu, 4}]];

report = <|
  "PoissonSolution" -> poisson,
  "PointMassGaussFlux" -> flux,
  "LinearizedBianchiResiduals" -> bianchi,
  "RandomnessUsed" -> False
|>;

If[bianchi =!= {0, 0, 0, 0}, Exit[1]];
report
