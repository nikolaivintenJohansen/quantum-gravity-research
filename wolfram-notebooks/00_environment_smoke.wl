(* Deterministic, self-contained Wolfram Language environment smoke test. *)

report = <|
  "Version" -> $Version,
  "VersionNumber" -> $VersionNumber,
  "SystemID" -> $SystemID,
  "Checks" -> <|
    "SymbolicDerivativeResidual" -> FullSimplify[D[x^3, x] - 3 x^2],
    "MatrixDeterminant" -> Det[{{1, 2}, {3, 4}}]
  |>,
  "RandomnessUsed" -> False
|>;

If[report["Checks", "SymbolicDerivativeResidual"] =!= 0, Exit[1]];
If[report["Checks", "MatrixDeterminant"] =!= -2, Exit[1]];

report
